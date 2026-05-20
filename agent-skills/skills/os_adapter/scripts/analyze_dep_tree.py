import abc
import functools
import json
import logging
import re
import subprocess
import sys
import typing

logger = logging.getLogger(__name__)


def run_cmd(cmd_args):
    result = subprocess.Popen(
        cmd_args,
        shell=False,
        universal_newlines=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    out, err = result.communicate()
    return result.returncode, out, err


def cmd_cache(func):
    @functools.wraps(func)
    def wrapper(self, arg):
        func_dict = self.query_cache_dict.setdefault(func.__name__, {})
        return func_dict.setdefault(arg, func(self, arg))

    return wrapper


class QueryManger:

    def __init__(self):
        self.query_cache_dict = {}

    @cmd_cache
    def query_pkg_dep_list(self, pkg_name):
        code, res, _ = run_cmd(["/usr/bin/yum", "deplist", pkg_name])
        if code != 0:
            raise Exception(f"execute cmd: yum deplist {pkg_name} failed.")
        return YumDepList.parse(res)

    @cmd_cache
    def query_provide(self, dep_name):
        code, provider, _ = run_cmd(["/usr/bin/rpm", "-q", "--whatprovides", dep_name])
        return code == 0, provider.strip()


QUERY_MANAGER = QueryManger()


class TypeMeta:

    @classmethod
    def judge_type(cls, other):
        if not isinstance(other, cls):
            return NotImplemented
        return True


class VersionComparator(TypeMeta):
    _NUM_PATTERN = re.compile(r"(\d+)")

    def __init__(self, value):
        self.value = value
        self.parts = self._NUM_PATTERN.split(value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __eq__(self, other):
        if not isinstance(other, VersionComparator):
            return NotImplemented
        return self.value == other.value

    def __gt__(self, other):
        result = self.compare_version(other)
        if result is NotImplemented:
            return NotImplemented
        return result > 0

    def __lt__(self, other):
        result = self.compare_version(other)
        if result is NotImplemented:
            return NotImplemented
        return result < 0

    def __ge__(self, other):
        eq_result = self.__eq__(other)
        if eq_result is NotImplemented:
            return NotImplemented
        if eq_result:
            return True
        return self.__gt__(other)

    def __le__(self, other):
        eq_result = self.__eq__(other)
        if eq_result is NotImplemented:
            return NotImplemented
        if eq_result:
            return True
        return self.__lt__(other)

    def compare_version(self, other):
        type_check = self.judge_type(other)
        if type_check is NotImplemented:
            return NotImplemented
        for part1, part2 in zip(self.parts, other.parts):
            if part1.isdigit() and part2.isdigit():
                result = int(part1) - int(part2)
            else:
                result = (part1 > part2) - (part1 < part2)

            if result != 0:
                return result

        return len(self.parts) - len(other.parts)


class VersionRelease:
    _VERSION_PATTERN = re.compile(r"(?P<version>[a-zA-Z0-9\._-]+)(-(?P<release>[a-zA-Z0-9\._-]+))?")

    def __init__(self, version, release=""):
        self.version = VersionComparator(version)
        self.release = VersionComparator(release or "")

    @classmethod
    def parse(cls, version):
        search = cls._VERSION_PATTERN.search(version)
        if not search:
            return None
        return cls(**search.groupdict())


class PkgInfo:

    def __init__(self, pkg_name, name, version, release, arch, epoch):
        self.pkg_name = pkg_name
        self.name = name
        self.version = VersionComparator(version)
        self.release = VersionComparator(release)
        self.arch = arch
        self.epoch = epoch

    def __bool__(self):
        return len(self.pkg_name) > 0

    def __str__(self):
        return self.pkg_name

    def __repr__(self):
        return self.pkg_name

    def __hash__(self):
        return hash(self.pkg_name)

    def __lt__(self, other):
        if not self.judge_same_pkg(other):
            return False
        return self.version < other.version or \
            (self.version == other.version
             and self.release < other.release
             )

    def __gt__(self, other):
        if not self.judge_same_pkg(other):
            return False
        return self.version > other.version or \
            (self.version == other.version
             and self.release > other.release
             )

    def __le__(self, other):
        if not self.judge_same_pkg(other):
            return False
        return self.version < other.version or \
            (self.version == other.version
             and self.release <= other.release
             )

    def __ge__(self, other):
        if not self.judge_same_pkg(other):
            return False
        return self.version > other.version or \
            (self.version == other.version
             and self.release >= other.release
             )

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.pkg_name == other.pkg_name \
                or (self.name == other.name
                    and self.version == other.version
                    and self.release == other.release
                    and self.arch == other.arch)
        if isinstance(other, str):
            return self.pkg_name == other
        return False

    @classmethod
    @abc.abstractmethod
    def get_name_pattern(cls) -> typing.Pattern:
        pass

    @classmethod
    @abc.abstractmethod
    def get_suffix(cls):
        pass

    @classmethod
    def from_pkg_name(cls, pkg_name):
        search = cls.get_name_pattern().search(pkg_name)
        if not search:
            return None
        return cls(pkg_name, **search.groupdict())

    def get_filename(self):
        return self.pkg_name + "." + self.get_suffix()

    def is_same_pkg(self, other):
        return self.name == other.name

    def judge_same_pkg(self, other):
        if isinstance(other, type(self)) and self.pkg_name != other.pkg_name:
            raise Exception(f"self {self.pkg_name}, other {other.pkg_name}")
        return True


class RpmPkgInfo(PkgInfo):
    _PATTERN = re.compile(
        r"(?P<name>[a-zA-Z0-9\+\._-]+)-(?P<epoch>\d+\:)?(?P<version>[a-zA-Z0-9\._-]+)-(?P<release>[a-zA-Z0-9\._-]+)\.(?P<arch>[a-zA-Z0-9_-]+)"
    )
    _SUFFIX = "rpm"

    def __init__(self, pkg_name, name, version, release, arch, epoch):
        super().__init__(pkg_name, name, version, release, arch, epoch)

    @classmethod
    def get_suffix(cls):
        return cls._SUFFIX

    @classmethod
    def get_name_pattern(cls) -> typing.Pattern:
        return cls._PATTERN


class DebPkgInfo:
    PATTERN = re.compile(r"(?P<name>.+)_(?P<version>[\d\.\+\~\:\-]+)-(?P<release>[\w\d\~\.\-]+)_(?P<arch>[^\.]+)")
    SUFFIX = "deb"

    def __init__(self, pkg_name, name, version, release, arch, epoch):
        super().__init__(pkg_name, name, version, release, arch, epoch)

    @classmethod
    def get_suffix(cls):
        return cls.SUFFIX

    @classmethod
    def get_name_pattern(cls) -> typing.Pattern:
        return cls.PATTERN


class TitleValueParser:

    def __init__(self, title, separator):
        self.title = title
        self.separator = separator

    def parse(self, content: str):
        return content.replace(self.title + self.separator, "").strip()


class VersionedDependency:
    _PATTERN = re.compile(r"(?P<name>.+?)(?P<op>(>|>=|<|<=|=))(?P<version_release>.+)")

    _GT = ">"
    _LT = "<"
    _GE = ">="
    _EQ = "="
    _LE = "<="

    def __init__(self, name, op, version_release):
        self.name = name.strip()
        self.op = op
        self.version_release = VersionRelease.parse(version_release)

    @classmethod
    def parse(cls, content):
        search = cls._PATTERN.search(content)
        if search:
            return cls(**search.groupdict())
        return None

    def compare(self, local_provide_pkg: PkgInfo):
        if self.op == self._GT:
            return local_provide_pkg > self.version_release
        if self.op == self._GE:
            return local_provide_pkg >= self.version_release
        if self.op == self._EQ:
            return local_provide_pkg == self.version_release
        if self.op == self._LT:
            return local_provide_pkg < self.version_release
        if self.op == self._LE:
            return local_provide_pkg <= self.version_release
        return False


class YumDepListDependency:
    _DEPENDENCY_TITLE = "dependency"
    _PROVIDER_TITLE = "provider"
    _SEPARATOR = ":"

    def __init__(self, dependency, providers: typing.List[RpmPkgInfo]):
        self.dependency = dependency
        self.providers = providers

    @classmethod
    def parse(cls, content):
        content_parts = content.split("\n", 1)
        dependency = TitleValueParser(cls._DEPENDENCY_TITLE, cls._SEPARATOR).parse(content_parts[0])
        if len(content_parts) < 2:
            return cls(dependency, [])
        providers_content = content_parts[1]
        provider_parser = TitleValueParser(cls._PROVIDER_TITLE, cls._SEPARATOR)
        provider_contents = [provider_parser.parse(part) for part in providers_content.splitlines()]
        providers = [RpmPkgInfo.from_pkg_name(provider) for provider in provider_contents]
        return cls(dependency, providers)

    def is_provide_existed(self):
        res, provider = QUERY_MANAGER.query_provide(self.dependency)
        return res, provider

    def compare_version(self):
        versioned_dep = VersionedDependency.parse(self.dependency)
        if not versioned_dep or not self.providers:
            logger.warning(f"dependency: {self.dependency} missing provider")
            return True
        source_provider_pkg = RpmPkgInfo.from_pkg_name(self.providers[0].pkg_name)
        res, local_provider = QUERY_MANAGER.query_provide(source_provider_pkg.name)
        if not res:
            return False
        local_provide_pkg = RpmPkgInfo.from_pkg_name(local_provider)
        if self.providers:
            return versioned_dep.compare(local_provide_pkg)
        return False

    def is_dependency_existed(self):
        if any(op in self.dependency for op in ("=", "<", ">")):
            return self.compare_version()
        provide_existed, provider = self.is_provide_existed()
        return provide_existed


class YumDepListItem:
    _PACKAGE_TITLE = "package"
    _SEPARATOR = ":"
    _DEPENDENCY_PATTERN = re.compile(r"dependency[\s\S]+?(?=dependency|$)")

    def __init__(self, package, dependencies: typing.List[YumDepListDependency]):
        self.package: RpmPkgInfo = RpmPkgInfo.from_pkg_name(package)
        self.dependencies = dependencies

    def __bool__(self):
        return bool(self.package)

    @classmethod
    def parse(cls, content: str):
        content_parts = content.strip().split("\n", 1)
        package = content_parts[0]
        package = TitleValueParser(cls._PACKAGE_TITLE, cls._SEPARATOR).parse(package)
        if len(content_parts) < 2:
            return cls(package, [])
        dependency_contents = cls._DEPENDENCY_PATTERN.findall(content_parts[1])
        dependencies = [YumDepListDependency.parse(content.strip()) for content in dependency_contents]
        return cls(package, dependencies)


class YumDepList:

    def __init__(self, items: typing.List[YumDepListItem]):
        self.items = items or []

    def __bool__(self):
        return len(self.items) > 0

    @classmethod
    def parse(cls, content):
        if not content.strip():
            return cls([])
        parts = content.strip().split("\n\n")
        items = [YumDepListItem.parse(part) for part in parts]
        return cls(list(filter(bool, items)))


class DepNode:

    def __init__(self, pkg_info, parent_node=None, dep_nodes=None):
        self.pkg_info: PkgInfo = pkg_info
        self.parent_node: DepNode = parent_node
        self.dep_nodes: typing.List[DepNode] = dep_nodes or []

    def __bool__(self):
        return bool(self.pkg_info)

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


def is_pkg_newest(pkg_name):
    res, provider = QUERY_MANAGER.query_provide(pkg_name)
    provide_pkg = RpmPkgInfo.from_pkg_name(provider)
    pkg_yum_dep_list = QUERY_MANAGER.query_pkg_dep_list(pkg_name)
    if not pkg_yum_dep_list:
        return True, provide_pkg, RpmPkgInfo.from_pkg_name("")
    newest_pkg = pkg_yum_dep_list.items[-1].package
    if not res:
        return False, provide_pkg, newest_pkg
    return newest_pkg == provide_pkg, provide_pkg, newest_pkg


def is_ancestor(cur_node: DepNode, pkg_name):
    if cur_node.pkg_info.pkg_name == pkg_name:
        return True
    if not cur_node.parent_node:
        return False
    return is_ancestor(cur_node.parent_node, pkg_name)


def copy_node(origin_node: DepNode, parent_node: DepNode):
    new_node = DepNode(origin_node.pkg_info, parent_node=parent_node)
    for dep_node in origin_node.dep_nodes:
        new_node.dep_nodes.append(copy_node(dep_node, new_node))
    return new_node

def find_dep_tree(root_pkg_name):
    pkg_dict = {}
    pkg_yum_dep_list: YumDepList = QUERY_MANAGER.query_pkg_dep_list(root_pkg_name)
    if not pkg_yum_dep_list:
        return DepNode.empty_node(), pkg_dict
    root_pkg_info = pkg_yum_dep_list.items[-1].package
    root_node = DepNode(root_pkg_info)
    root_node.pkg_info = root_pkg_info
    que = [root_node]
    while True:
        cur_node: DepNode = que.pop(0)
        if not cur_node:
            continue
        pkg_dict[cur_node.pkg_info] = cur_node
        res, provide_pkg, newest_pkg = is_pkg_newest(cur_node.pkg_info.pkg_name)
        if res:
            continue
        pkg_yum_dep_list: YumDepList = QUERY_MANAGER.query_pkg_dep_list(cur_node.pkg_info.pkg_name)
        new_nodes = []
        next_level_nodes = []
        for dependency in pkg_yum_dep_list.items[-1].dependencies:
            if dependency.is_dependency_existed():
                continue
            if not dependency.providers:
                continue
            dep_provide_pkg = dependency.providers[0]
            # 软件包已经被记录
            if dep_provide_pkg.pkg_name in [node.pkg_info.pkg_name for node in new_nodes]:
                continue
            # 若为祖先节点，则不引用
            if is_ancestor(cur_node, dep_provide_pkg.pkg_name):
                continue

            if dep_provide_pkg in pkg_dict:
                new_node = copy_node(pkg_dict.get(dep_provide_pkg), cur_node)
            else:
                new_node = DepNode(dep_provide_pkg, parent_node=cur_node)
                next_level_nodes.append(new_node)
            new_nodes.append(new_node)
        cur_node.dep_nodes.extend(new_nodes)
        que.extend(next_level_nodes)
        if not que:
            break
    return root_node, pkg_dict.keys()


class DepTreeOutput:

    def __init__(self, dep_tree, pkgs):
        self.dep_tree = dep_tree
        self.pkgs = pkgs

    def to_json(self):
        return {
            "dep_tree": self.dep_tree,
            "pkgs": self.pkgs
        }


def find_pkgs_dep_tree(pkg_names, show_version=False, show_pkg_name=False):
    root_nodes_info = [find_dep_tree(pkg_name) for pkg_name in pkg_names]
    json_nodes = [node_info[0].to_json(show_version, show_pkg_name) for node_info in root_nodes_info if node_info[0]]
    pkgs = set()
    [pkgs.update(node_info[1]) for node_info in root_nodes_info]
    return DepTreeOutput(json_nodes, pkgs)


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
        self.pkgs = pkgs


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


def main():
    cli_setting = CliSetting.parse(sys.argv[1:])
    pkg_set = set()
    dep_groups = []
    for group_setting in cli_setting.dep_groups:
        dep_tree_output = find_pkgs_dep_tree(group_setting.pkgs, cli_setting.show_version, cli_setting.show_pkg_name)
        dep_groups.append(GroupOutput(group_setting.group_name, dep_tree_output.dep_tree))
        pkg_set.update(dep_tree_output.pkgs)
    dep_tree_data = [dep_group.to_json() for dep_group in dep_groups]
    with open("dep_tree.json", "w") as f:
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
    with open("pkg_info.json", "w") as f:
        json.dump(pkg_list, f, indent=2)
    return pkg_list, dep_tree_data


if __name__ == '__main__':
    main()
