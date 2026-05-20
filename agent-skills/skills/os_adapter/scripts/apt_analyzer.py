import functools
import json
import logging
import os
import sys
import typing

import apt
import apt_pkg

logger = logging.getLogger(__name__)

cache = apt.Cache()


def cmd_cache(func):
    @functools.wraps(func)
    def wrapper(self, arg):
        func_dict = self.query_cache_dict.setdefault(func.__name__, {})
        return func_dict.setdefault(arg, func(self, arg))

    return wrapper


class AptPkgInfo:

    def __init__(self, name, local_version="", remote_version="", arch="", is_installed=False,
                 is_in_remote_cache=False, dependencies=None):
        self.name = name
        self.local_version = local_version
        self.version = remote_version
        self.arch = arch
        self.is_installed = is_installed
        self.is_in_remote_cache = is_in_remote_cache
        self.dependencies = dependencies or []

    def __hash__(self):
        return hash(self.pkg_name)

    def __eq__(self, other):
        if not hasattr(other, "pkg_name"):
            return False
        return self.pkg_name == other.pkg_name

    def __str__(self):
        return self.pkg_name

    def __repr__(self):
        return str(self)

    @property
    def local_package_name(self):
        return "_".join([self.name, self.local_version, self.arch])

    @property
    def pkg_name(self):
        return "_".join([self.name, self.version, self.arch])


class QueryManager:

    def __init__(self):
        self.query_cache_dict = {}


class QueryAptManager(QueryManager):

    def __init__(self):
        super().__init__()

    @cmd_cache
    def query_apt_pkg_info(self, pkg_name) -> AptPkgInfo:
        if pkg_name not in cache:
            return AptPkgInfo(pkg_name, is_in_remote_cache=False)
        pkg_cache_info = cache[pkg_name]
        apt_pkg_info = AptPkgInfo(pkg_name)
        if pkg_cache_info.is_installed:
            apt_pkg_info.is_installed = True
            apt_pkg_info.local_version = pkg_cache_info.installed.version
        if pkg_cache_info.candidate:
            apt_pkg_info.is_in_remote_cache = True
            apt_pkg_info.version = pkg_cache_info.candidate.version
            apt_pkg_info.arch = pkg_cache_info.candidate.architecture
            apt_pkg_info.dependencies = pkg_cache_info.candidate.dependencies
        return apt_pkg_info


QUERY_APT_MANAGER = QueryAptManager()


def split_list_on_element(lst, delimiter):
    result = []
    current_sublist = []

    for element in lst:
        if element == delimiter:
            if current_sublist:  # 如果当前子列表不为空
                result.append(current_sublist)
            current_sublist = [element]  # 以分割元素作为首元素新建子列表
        else:
            current_sublist.append(element)

    if current_sublist:  # 添加最后的子列表
        result.append(current_sublist)

    return result


class DepTreeOutput:

    def __init__(self, dep_tree, pkgs):
        self.dep_tree = dep_tree
        self.pkgs = pkgs

    def to_json(self):
        return {
            "dep_tree": self.dep_tree,
            "pkgs": self.pkgs
        }


class GroupOutput:

    def __init__(self, dep_from, dep_tree):
        self.dep_from = dep_from
        self.dep_tree = dep_tree

    def to_json(self):
        return {
            "dep_from": self.dep_from,
            "dep_tree": self.dep_tree
        }


class DepGroup:

    def __init__(self, group_name, pkgs):
        self.group_name = group_name
        self.pkgs = list(set(pkgs))


class DepNode:

    def __init__(self, pkg_info, parent_node=None, dep_nodes=None):
        self.pkg_info: AptPkgInfo = pkg_info
        self.parent_node: DepNode = parent_node
        self.dep_nodes: typing.List[DepNode] = dep_nodes or []

    def __bool__(self):
        return bool(self.pkg_info.name)

    @classmethod
    def empty_node(cls):
        return cls(None)

    def to_json(self, show_version=False, show_pkg_name=False):
        res = {
            "name": self.pkg_info.name
        }
        dep_nodes = [node.to_json(show_version, show_pkg_name) for node in self.dep_nodes]
        if dep_nodes:
            res.update({"dep_nodes": dep_nodes})
        if show_version:
            res.update({"version": str(self.pkg_info.version)})
        if show_pkg_name:
            res.update({"pkg_name": self.pkg_info.pkg_name})
        return res


def is_ancestor(cur_node: DepNode, name):
    if cur_node.pkg_info.name == name:
        return True
    if not cur_node.parent_node:
        return False
    return is_ancestor(cur_node.parent_node, name)


class CliSetting:
    _SHOW_VERSION = "--show_version"
    _SHOW_PKG_NAME = "--show_pkg_name"
    _GROUP = "--group"
    _PKGS = "--pkgs"

    def __init__(self, dep_groups: typing.List[DepGroup], show_version=False, show_pkg_name=False):
        self.dep_groups = dep_groups
        self.show_version = show_version
        self.show_pkg_name = show_pkg_name

    @classmethod
    def parse(cls, args: list):
        tmp_args = list(args)
        show_version = False
        if cls._SHOW_VERSION in tmp_args:
            tmp_args.remove(cls._SHOW_VERSION)
            show_version = True
        show_pkg_name = False
        if cls._SHOW_PKG_NAME in tmp_args:
            tmp_args.remove(cls._SHOW_PKG_NAME)
            show_pkg_name = True
        groups_list = split_list_on_element(tmp_args, cls._GROUP)
        groups = []
        for group_list in groups_list:
            group_name = group_list[1]
            pkgs = group_list[group_list.index(cls._PKGS) + 1:]
            groups.append(DepGroup(group_name, pkgs))
        return cls(groups, show_version, show_pkg_name)


def apt_pkg_version_compare(src_version, relation, dest_version):
    compare_res = apt_pkg.version_compare(src_version, dest_version)
    if relation == "<":
        return compare_res < 0
    if relation == "<=":
        return compare_res <= 0
    if relation == "=":
        return compare_res == 0
    if relation == ">":
        return compare_res > 0
    if relation == ">=":
        return compare_res >= 0
    raise Exception(f"unmatch relation: {relation}, source version: {src_version}, dest version: {dest_version}")


def find_apt_dep_tree(root_pkg_name):
    pkg_set = set()
    root_pkg_info = QUERY_APT_MANAGER.query_apt_pkg_info(root_pkg_name)
    root_node = DepNode(root_pkg_info)
    que = [root_node]
    while True:
        cur_node: DepNode = que.pop(0)
        cur_pkg_info = cur_node.pkg_info
        pkg_set.add(cur_pkg_info)
        new_nodes = []
        dependencies = cur_pkg_info.dependencies or []
        for dep_list in dependencies:
            for dep in dep_list:
                if dep.name in [node.pkg_info.name for node in new_nodes]:
                    continue
                if is_ancestor(cur_node, dep.name):
                    continue
                dep_pkg_info: AptPkgInfo = QUERY_APT_MANAGER.query_apt_pkg_info(dep.name)
                if not dep_pkg_info.is_in_remote_cache:
                    logger.warning(f"dependency {dep.name} does not exist!")
                    continue
                if dep_pkg_info.is_installed:
                    if not dep.relation and not dep.version:
                        continue
                    if apt_pkg_version_compare(dep_pkg_info.version, dep.relation, dep.version):
                        continue
                new_node = DepNode(dep_pkg_info, parent_node=cur_node)
                new_nodes.append(new_node)
        cur_node.dep_nodes.extend(new_nodes)
        que.extend(new_nodes)
        if not que:
            break

    return root_node, pkg_set


def find_pkgs_dep_tree(pkgs, show_version, show_pkg_name):
    root_nodes_info = [find_apt_dep_tree(pkg_name) for pkg_name in pkgs]
    json_nodes = [node_info[0].to_json(show_version, show_pkg_name) for node_info in root_nodes_info]
    pkgs = set()
    [pkgs.update(node_info[1]) for node_info in root_nodes_info]
    return DepTreeOutput(json_nodes, pkgs)


def main():
    cli_setting = CliSetting.parse(sys.argv[1:])
    pkg_set = set()
    dep_groups = []
    for group_setting in cli_setting.dep_groups:
        dep_tree_output = find_pkgs_dep_tree(group_setting.pkgs, cli_setting.show_version, cli_setting.show_pkg_name)
        dep_groups.append(GroupOutput(group_setting.group_name, dep_tree_output.dep_tree))
        pkg_set.update(dep_tree_output.pkgs)
    dep_tree_data = [dep_group.to_json() for dep_group in dep_groups]
    with os.fdopen(os.open("dep_tree.json", os.O_WRONLY | os.O_CREAT, 0o600), "w") as f:
        json.dump(dep_tree_data, f, indent=2)
    pkg_list = []
    for pkg in pkg_set:
        pkg_item = {"name": pkg.name}
        if cli_setting.show_version:
            pkg_item.update({"version": str(pkg.version)})
        if cli_setting.show_pkg_name:
            pkg_item.update({"pkg_name": str(pkg.name)})
        pkg_list.append(pkg_item)
    pkg_list = sorted(pkg_list, key=lambda x: x.get("name"))
    with os.fdopen(os.open("pkg_info.json", os.O_WRONLY | os.O_CREAT, 0o600), "w") as f:
        json.dump(pkg_list, f, indent=2)
    return pkg_list, dep_tree_data


if __name__ == '__main__':
    main()
