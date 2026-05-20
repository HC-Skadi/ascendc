#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import sys
import json
import argparse
import subprocess
import shlex
from pathlib import Path
from typing import Dict, List, Optional, Set

logger = logging.getLogger(__name__)

TYPE_FIELD = "type"
FILES_FIELD = "files"
FILE_FIELD = "file"
PATH_FIELD = "path"
CONTENT_FIELD = "content"
FULL_FIELD = "full"


class SSHConnector:
    """SSH connection handler for remote OS information collection."""
    
    def __init__(self, host: str, port: int = 22, user: str = "root", 
                 password: str = None, key_file: str = None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.key_file = key_file
    
    def run_command(self, command: str, timeout: int = 30) -> tuple:
        """Execute command on remote host via SSH."""
        ssh_cmd = []
        
        if self.password:
            ssh_cmd.extend(["sshpass", "-p", self.password])
        
        ssh_cmd.append("ssh")
        ssh_cmd.extend(["-p", str(self.port)])
        ssh_cmd.extend(["-o", "StrictHostKeyChecking=no"])
        ssh_cmd.extend(["-o", "ConnectTimeout=10"])
        
        if self.key_file:
            ssh_cmd.extend(["-i", self.key_file])
        
        ssh_cmd.append(f"{self.user}@{self.host}")
        ssh_cmd.append(command)
        
        try:
            result = subprocess.run(
                ssh_cmd,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            logger.error(f"SSH connection failed: {e}")
            return -1, "", "SSH connection failed"
    
    def test_connection(self) -> bool:
        """Test SSH connection."""
        returncode, _, _ = self.run_command("echo 'connection_test'")
        return returncode == 0
    
    def get_os_release(self) -> Dict:
        """Get OS release information from remote host."""
        os_info = {}
        returncode, stdout, stderr = self.run_command("cat /etc/os-release")
        
        if returncode == 0:
            for line in stdout.strip().split('\n'):
                if '=' in line:
                    key, value = line.split('=', 1)
                    value = value.strip('"\'')
                    os_info[key] = value
        
        returncode, stdout, _ = self.run_command("uname -m")
        if returncode == 0:
            os_info['ARCH'] = stdout.strip()
        
        return os_info
    
    def get_installed_packages(self) -> List[str]:
        """Get installed packages from remote host."""
        packages = []
        
        returncode, stdout, _ = self.run_command("rpm -qa 2>/dev/null")
        if returncode == 0 and stdout.strip():
            packages = stdout.strip().split('\n')
            return packages
        
        returncode, stdout, _ = self.run_command("dpkg -l 2>/dev/null")
        if returncode == 0 and stdout.strip():
            lines = stdout.strip().split('\n')
            for line in lines[5:]:
                parts = line.split()
                if len(parts) >= 3:
                    packages.append(f"{parts[1]} {parts[2]}")
        
        return packages
    
    def get_repo_info(self) -> Dict:
        """Get repository information from remote host."""
        repo_info = {
            TYPE_FIELD: None,
            FILES_FIELD: []
        }
        
        returncode, stdout, _ = self.run_command("ls /etc/yum.repos.d/*.repo 2>/dev/null")
        if returncode == 0 and stdout.strip():
            repo_info[TYPE_FIELD] = 'rpm'
            for repo_file in stdout.strip().split('\n'):
                if repo_file:
                    returncode, content, _ = self.run_command(f"cat {shlex.quote(repo_file)}")
                    if returncode == 0:
                        repo_info[FILES_FIELD].append({
                            PATH_FIELD: repo_file,
                            CONTENT_FIELD: content
                        })
            return repo_info
        
        returncode, stdout, _ = self.run_command("cat /etc/apt/sources.list 2>/dev/null")
        if returncode == 0 and stdout.strip():
            repo_info[TYPE_FIELD] = 'deb'
            repo_info[FILES_FIELD].append({
                PATH_FIELD: '/etc/apt/sources.list',
                CONTENT_FIELD: stdout
            })
        
        returncode, stdout, _ = self.run_command("ls /etc/apt/sources.list.d/*.list 2>/dev/null")
        if returncode == 0 and stdout.strip():
            for source_file in stdout.strip().split('\n'):
                if source_file:
                    returncode, content, _ = self.run_command(f"cat {shlex.quote(source_file)}")
                    if returncode == 0:
                        repo_info[FILES_FIELD].append({
                            PATH_FIELD: source_file,
                            CONTENT_FIELD: content
                        })
        
        return repo_info
    
    def is_rpm_based(self) -> bool:
        """Check if remote host is RPM-based."""
        returncode, _, _ = self.run_command("which rpm")
        return returncode == 0


class OSAdapter:
    ASCEND_DEPLOYER_MARKERS = [
        "module_utils",
        "downloader_config",
        "scripts/nexus_config.json"
    ]
    
    CANN_PACKAGES_RPM = [
        "gcc", "gcc-c++", "make", "cmake", "unzip", "zlib-devel",
        "libffi-devel", "openssl-devel", "pciutils", "net-tools",
        "sqlite-devel", "lapack-devel", "gcc-gfortran"
    ]
    
    NPU_PACKAGES_RPM = [
        "make", "dkms", "gcc"
    ]
    
    CANN_PACKAGES_DEB = [
        "gcc", "g++", "make", "cmake", "libsqlite3-dev",
        "zlib1g-dev", "libssl-dev", "libffi-dev", "net-tools"
    ]
    
    NPU_PACKAGES_DEB = [
        "dkms", "gcc"
    ]
    
    def __init__(self, project_root: str = None, ssh_connector: SSHConnector = None):
        if project_root:
            self.project_root = Path(project_root)
        else:
            self.project_root = Path.cwd()
        
        self.module_utils_path = self.project_root / "module_utils"
        self.common_info_path = self.module_utils_path / "common_info.py"
        self.compatibility_config_path = self.module_utils_path / "compatibility_config.py"
        self.downloader_config_path = self.project_root / "downloader_config"
        self.scripts_path = self.project_root / "scripts"
        self.nexus_config_path = self.scripts_path / "nexus_config.json"
        
        self.ssh_connector = ssh_connector
        self.os_info = {}
        self.os_name = ""
        self.os_constant_name = ""
        self.hardware_support = []
        self.arch = ""
        self.repo_info = {}
        
    @staticmethod
    def generate_os_name(os_info: Dict) -> str:
        name = os_info.get('NAME', 'Unknown')
        version = os_info.get('VERSION_ID', '')
        arch = os_info.get('ARCH', 'unknown')
        
        name_clean = name.replace(' ', '_').replace('.', '_')
        version_clean = version.replace('.', '_')
        
        os_name = f"{name_clean}_{version_clean}_{arch}"
        return os_name
    
    @staticmethod
    def generate_os_constant_name(os_name: str) -> str:
        return os_name.upper().replace('.', '_')

    @staticmethod
    def get_system_repos() -> List[Dict]:
        repos = []
        
        yum_repos_dir = Path("/etc/yum.repos.d")
        if yum_repos_dir.exists():
            for repo_file in yum_repos_dir.glob("*.repo"):
                repos.append({
                    TYPE_FIELD: 'rpm',
                    FILE_FIELD: str(repo_file),
                    CONTENT_FIELD: repo_file.read_text()
                })
        
        apt_sources_dir = Path("/etc/apt/sources.list.d")
        apt_sources_file = Path("/etc/apt/sources.list")
        
        if apt_sources_file.exists():
            repos.append({
                TYPE_FIELD: 'deb',
                FILE_FIELD: str(apt_sources_file),
                CONTENT_FIELD: apt_sources_file.read_text()
            })
        
        if apt_sources_dir.exists():
            for source_file in apt_sources_dir.glob("*.list"):
                repos.append({
                    TYPE_FIELD: 'deb',
                    FILE_FIELD: str(source_file),
                    CONTENT_FIELD: source_file.read_text()
                })
        
        return repos

    @staticmethod
    def _get_arch() -> str:
        try:
            result = subprocess.run(['/usr/bin/uname', '-m'], capture_output=True, text=True)
            return result.stdout.strip()
        except (OSError, subprocess.SubprocessError) as e:
            logger.error(f"Failed to get system architecture: {e}")
            return 'unknown'

    def is_ascend_deployer_project(self) -> bool:
        """Check if current project is ascend-deployer project."""
        for marker in self.ASCEND_DEPLOYER_MARKERS:
            marker_path = self.project_root / marker
            if not marker_path.exists():
                return False
        return True
    
    def get_os_info_from_system(self) -> Dict:
        """Get OS information from local or remote system."""
        if self.ssh_connector:
            return self.ssh_connector.get_os_release()
        
        os_info = {}
        os_release_path = "/etc/os-release"
        
        if os.path.exists(os_release_path):
            with open(os_release_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if '=' in line:
                        key, value = line.split('=', 1)
                        value = value.strip('"\'')
                        os_info[key] = value
        
        os_info['ID'] = os_info.get('ID', 'unknown')
        os_info['VERSION_ID'] = os_info.get('VERSION_ID', '')
        os_info['NAME'] = os_info.get('NAME', 'Unknown OS')
        os_info['ARCH'] = self._get_arch()
        
        return os_info
    
    def update_common_info(self, os_name: str, os_constant: str) -> bool:
        if not self.common_info_path.exists():
            logger.error(f"common_info.py not found: {self.common_info_path}")
            return False
        
        with open(self.common_info_path, 'r') as f:
            content = f.read()
        
        updated = False
        
        if os_constant not in content:
            osname_class_match = content.find('class OSName:')
            if osname_class_match != -1:
                insert_pos = content.find('\n', osname_class_match) + 1
                new_line = f'    {os_constant} = "{os_name}"\n'
                content = content[:insert_pos] + new_line + content[insert_pos:]
                logger.info(f"Added OSName.{os_constant} = \"{os_name}\"")
                updated = True
        else:
            logger.info(f"OSName.{os_constant} already exists, skipping")
        
        dl_os_list_pattern = 'dl_os_list = ['
        if dl_os_list_pattern in content:
            list_start = content.find(dl_os_list_pattern)
            list_end = content.find(']', list_start)
            list_content = content[list_start:list_end + 1]
            
            if os_name not in list_content:
                new_list_content = list_content.replace(']', f',\n        "{os_name}"\n    ]')
                content = content[:list_start] + new_list_content + content[list_end + 1:]
                logger.info(f"Added \"{os_name}\" to dl_os_list")
                updated = True
            else:
                logger.info(f"\"{os_name}\" already in dl_os_list, skipping")
        
        if updated:
            with os.fdopen(os.open(self.common_info_path, os.O_WRONLY | os.O_CREAT, 0o600), 'w') as f:
                f.write(content)
            logger.info(f"Updated {self.common_info_path}")
        
        return updated
    
    def update_compatibility_config(self, os_name: str, hardware_list: List[str]) -> bool:
        if not self.compatibility_config_path.exists():
            logger.error(f"compatibility_config.py not found: {self.compatibility_config_path}")
            return False
        
        with open(self.compatibility_config_path, 'r') as f:
            content = f.read()
        
        updated = False
        
        os_to_card_pattern = 'OS_TO_CARD_TAG_MAP = {'
        if os_to_card_pattern in content:
            map_start = content.find(os_to_card_pattern)
            map_end = content.find('}', map_start)
            map_content = content[map_start:map_end + 1]
            
            if os_name not in map_content:
                hardware_tags = ', '.join([f'"{h}"' for h in hardware_list])
                new_entry = f'        "{os_name}": [{hardware_tags}],\n'
                insert_pos = map_end
                content = content[:insert_pos] + new_entry + content[insert_pos:]
                logger.info(f"Added hardware mapping for {os_name}: {hardware_list}")
                updated = True
            else:
                logger.info(f"Hardware mapping for {os_name} already exists, skipping")
        
        if updated:
            with os.fdopen(os.open(self.compatibility_config_path, os.O_WRONLY | os.O_CREAT, 0o600), 'w') as f:
                f.write(content)
            logger.info(f"Updated {self.compatibility_config_path}")
        
        return updated
    
    def create_os_config_directory(self, os_name: str) -> Path:
        os_config_dir = self.downloader_config_path / os_name
        os_config_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created directory: {os_config_dir}")
        return os_config_dir
    
    def get_installed_packages(self) -> List[str]:
        """Get installed packages from local or remote system."""
        if self.ssh_connector:
            return self.ssh_connector.get_installed_packages()
        
        packages = []
        
        try:
            result = subprocess.run(['/usr/bin/rpm', '-qa'], capture_output=True, text=True)
            if result.returncode == 0:
                packages = result.stdout.strip().split('\n')
                return packages
        except FileNotFoundError:
            logger.error("rpm command not found, trying dpkg")
        
        try:
            result = subprocess.run(['/usr/bin/dpkg', '-l'], capture_output=True, text=True)
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                for line in lines[5:]:
                    parts = line.split()
                    if len(parts) >= 3:
                        packages.append(f"{parts[1]} {parts[2]}")
                return packages
        except FileNotFoundError:
            logger.error("dpkg command not found")
        
        logger.warning("Could not determine package manager")
        return packages
    
    def create_installed_txt(self, os_config_dir: Path) -> bool:
        installed_file = os_config_dir / "installed.txt"
        
        if installed_file.exists():
            logger.info("installed.txt already exists, skipping")
            return False
        
        packages = self.get_installed_packages()
        
        with os.fdopen(os.open(installed_file, os.O_WRONLY | os.O_CREAT, 0o600), 'w') as f:
            for pkg in packages:
                f.write(f"{pkg}\n")
        
        logger.info(f"Created {installed_file} with {len(packages)} packages")
        return True
    
    def create_source_repo(self, os_config_dir: Path) -> bool:
        is_rpm = self.is_rpm_based()
        
        if is_rpm:
            source_file = os_config_dir / "source.repo"
        else:
            source_file = os_config_dir / "source.list"
        
        if source_file.exists():
            logger.info(f"{source_file.name} already exists, skipping")
            return False
        
        content = None
        
        if self.ssh_connector:
            logger.info("Fetching repository info via SSH...")
            self.repo_info = self.ssh_connector.get_repo_info()
            
            if self.repo_info.get(FILES_FIELD):
                content_parts = []
                for repo_file in self.repo_info[FILES_FIELD]:
                    content_parts.append(f"# Source: {repo_file[PATH_FIELD]}")
                    content_parts.append(repo_file[CONTENT_FIELD])
                    content_parts.append("")
                content = "\n".join(content_parts)
                logger.info(f"Retrieved repository info from {len(self.repo_info[FILES_FIELD])} file(s)")
            else:
                logger.warning("Could not retrieve repository info via SSH")
        
        if not content:
            if is_rpm:
                content = f"""# Repository Configuration for {self.os_name}
# For CentOS/RHEL/openEuler like systems (RPM-based)
# Please fill in the baseurl for each repository

[base]
baseurl=

[docker-ce]
baseurl=

[everything]
baseurl=

[update]
baseurl=

[EPOL]
baseurl=
"""
                logger.warning("Please manually configure repository URLs in source.repo")
            else:
                codename = self.os_info.get('VERSION_CODENAME', '')
                if not codename:
                    version_id = self.os_info.get('VERSION_ID', '')
                    if version_id:
                        codename = f"debian{version_id.split('.')[0]}"
                
                content = f"""# Repository Configuration for {self.os_name}
# For Debian/Ubuntu like systems (DEB-based)
# Please fill in the repository URLs

deb <debian_main_url> {codename} main
deb <debian_main_url> {codename}-updates main
deb <debian_security_url> {codename} updates/main
deb <docker_ce_url> {codename} stable
"""
                logger.warning("Please manually configure repository URLs in source.list")
        
        with os.fdopen(os.open(source_file, os.O_WRONLY | os.O_CREAT, 0o600), 'w') as f:
            f.write(content)
        
        logger.info(f"Created {source_file}")
        return True
    
    def create_pkg_info_json(self, os_config_dir: Path) -> bool:
        pkg_info_file = os_config_dir / "pkg_info.json"
        
        if pkg_info_file.exists():
            logger.info("pkg_info.json already exists, skipping")
            return False
        
        logger.info("Analyzing all dependencies (cann, npu)...")
        packages = self.analyze_dependencies()
        
        with os.fdopen(os.open(pkg_info_file, os.O_WRONLY | os.O_CREAT, 0o600), 'w') as f:
            json.dump(packages, f, indent=4)
        
        logger.info(f"Created {pkg_info_file} with {len(packages)} packages")
        
        packages_with_version = [p for p in packages if p.get('version')]
        packages_without_version = [p for p in packages if not p.get('version')]
        
        if packages_without_version:
            logger.warning(f"{len(packages_without_version)} packages without version:")
            for pkg in packages_without_version:
                logger.warning(f"  - {pkg['name']}")
            logger.info("Please populate package versions manually or via repository API")
        
        return True
    
    def is_rpm_based(self) -> bool:
        """Check if system is RPM-based (local or remote)."""
        if self.ssh_connector:
            return self.ssh_connector.is_rpm_based()
        return os.path.exists("/bin/rpm") or os.path.exists("/usr/bin/rpm")
    
    def analyze_dependencies_rpm(self) -> List[Dict]:
        """Analyze all dependencies for RPM-based systems."""
        packages = []
        
        all_pkgs = self.CANN_PACKAGES_RPM + self.NPU_PACKAGES_RPM
        
        kernel_headers = f"kernel-headers-{self.arch}"
        kernel_devel = f"kernel-devel-{self.arch}"
        all_pkgs = all_pkgs + [kernel_headers, kernel_devel]
        
        seen = set()
        unique_pkgs = []
        for pkg in all_pkgs:
            if pkg not in seen:
                seen.add(pkg)
                unique_pkgs.append(pkg)
        
        for pkg in unique_pkgs:
            version = self._get_package_version_rpm(pkg)
            packages.append({
                "name": pkg,
                "version": version
            })
        
        return packages
    
    def analyze_dependencies_deb(self) -> List[Dict]:
        """Analyze all dependencies for DEB-based systems."""
        packages = []
        
        all_pkgs = self.CANN_PACKAGES_DEB + self.NPU_PACKAGES_DEB
        
        linux_headers = f"linux-headers-{self.arch}"
        all_pkgs = all_pkgs + [linux_headers]
        
        seen = set()
        unique_pkgs = []
        for pkg in all_pkgs:
            if pkg not in seen:
                seen.add(pkg)
                unique_pkgs.append(pkg)
        
        for pkg in unique_pkgs:
            version = self._get_package_version_deb(pkg)
            packages.append({
                "name": pkg,
                "version": version
            })
        
        return packages
    
    def analyze_dependencies(self) -> List[Dict]:
        """Analyze all dependencies based on OS type."""
        if self.is_rpm_based():
            return self.analyze_dependencies_rpm()
        else:
            return self.analyze_dependencies_deb()
    
    def update_nexus_config(self, os_name: str) -> bool:
        if not self.nexus_config_path.exists():
            logger.warning(f"nexus_config.json not found: {self.nexus_config_path}")
            return False
        
        with open(self.nexus_config_path, 'r') as f:
            config = json.load(f)
        
        updated = False
        os_type = "rpm_os" if self.is_rpm_based() else "deb_os"
        
        if os_type in config:
            if os_name not in config[os_type]:
                config[os_type].append(os_name)
                updated = True
                logger.info(f"Added {os_name} to {os_type} in nexus_config.json")
            else:
                logger.info(f"{os_name} already in {os_type}, skipping")
        
        if updated:
            with os.fdopen(os.open(self.nexus_config_path, os.O_WRONLY | os.O_CREAT, 0o600), 'w') as f:
                json.dump(config, f, indent=2)
            logger.info(f"Updated {self.nexus_config_path}")
        
        return updated
    
    def run_full_adapter(self, os_name: str = None, hardware: List[str] = None):
        logger.info("=" * 60)
        logger.info("OS Adapter - Full Adaptation Process")
        logger.info("=" * 60)
        
        if not os_name:
            self.os_info = self.get_os_info_from_system()
            self.os_name = self.generate_os_name(self.os_info)
        else:
            self.os_name = os_name
            self.os_info = {'NAME': os_name}
        
        self.arch = self._get_arch()
        self.os_info['ARCH'] = self.arch
        self.os_constant_name = self.generate_os_constant_name(self.os_name)
        
        is_rpm = self.is_rpm_based()
        os_type = "RPM-based" if is_rpm else "DEB-based"
        
        logger.info(f"OS Name: {self.os_name}")
        logger.info(f"OS Constant: {self.os_constant_name}")
        logger.info(f"Architecture: {self.arch}")
        logger.info(f"OS Type: {os_type}")
        logger.info(f"Hardware Support: {hardware or 'Not specified'}")
        logger.info(f"Dependency Groups: cann, npu (all)")
        
        logger.info("[Step 1] Updating OS basic info...")
        self.update_common_info(self.os_name, self.os_constant_name)
        
        logger.info("[Step 2] Updating hardware compatibility config...")
        if hardware:
            self.update_compatibility_config(self.os_name, hardware)
        else:
            logger.warning("No hardware specified, skipping hardware config update")
        
        logger.info("[Step 3] Creating OS config directory...")
        os_config_dir = self.create_os_config_directory(self.os_name)
        
        logger.info("[Step 4] Creating installed.txt...")
        self.create_installed_txt(os_config_dir)
        
        logger.info("[Step 5] Creating source config...")
        self.create_source_repo(os_config_dir)
        
        logger.info("[Step 6] Analyzing dependencies and creating pkg_info.json...")
        self.create_pkg_info_json(os_config_dir)
        
        logger.info("[Step 7] Updating nexus_config.json...")
        self.update_nexus_config(self.os_name)
        
        source_file_name = "source.repo" if is_rpm else "source.list"
        
        logger.info("")
        logger.info("=" * 60)
        logger.info("OS Adaptation Complete!")
        logger.info("=" * 60)
        logger.info(f"Please review and update the following files:")
        logger.info(f"  - {os_config_dir / 'pkg_info.json'}")
        logger.info(f"  - {os_config_dir / source_file_name}")

    def _get_package_version_rpm(self, package_name: str) -> str:
        """Get package version for RPM-based systems."""
        cmd_args = ["/usr/bin/rpm", "-q", package_name, "--queryformat", "%{VERSION}-%{RELEASE}"]
        
        if self.ssh_connector:
            returncode, stdout, _ = self.ssh_connector.run_command(" ".join(cmd_args))
            if returncode == 0 and stdout.strip():
                return stdout.strip()
        else:
            try:
                result = subprocess.run(
                    cmd_args,
                    shell=False,
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    return result.stdout.strip()
            except (OSError, subprocess.SubprocessError) as e:
                logger.error(f"Failed to get RPM package version for {package_name}: {e}")
        
        return ""
    
    def _get_package_version_deb(self, package_name: str) -> str:
        """Get package version for DEB-based systems."""
        
        if self.ssh_connector:
            cmd = f"dpkg -l {package_name} 2>/dev/null | tail -1 | awk '{{print $3}}'"
            returncode, stdout, _ = self.ssh_connector.run_command(cmd)
            if returncode == 0 and stdout.strip():
                return stdout.strip()
        else:
            try:
                result = subprocess.run(
                    ["/usr/bin/dpkg", "-l", package_name],
                    shell=False,
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    lines = result.stdout.strip().split('\n')
                    if len(lines) >= 1:
                        last_line = lines[-1]
                        parts = last_line.split()
                        if len(parts) >= 3:
                            version = parts[2]
                            if version and version != "Desired":
                                return version
            except (OSError, subprocess.SubprocessError) as e:
                logger.error(f"Failed to get DEB package version for {package_name}: {e}")
        
        return ""


def check_project(adapter: OSAdapter) -> bool:
    """Check if current project is ascend-deployer project."""
    if not adapter.is_ascend_deployer_project():
        logger.error("This is not an ascend-deployer project!")
        logger.error(f"Project root: {adapter.project_root}")
        logger.error("Required markers not found:")
        for marker in adapter.ASCEND_DEPLOYER_MARKERS:
            marker_path = adapter.project_root / marker
            if not marker_path.exists():
                logger.error(f"  - {marker}")
        logger.error("OS Adapter can only be executed in ascend-deployer project.")
        logger.error("Aborting...")
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description='OS Adapter Tool')
    parser.add_argument('--os-name', type=str, help='OS name (e.g., BCLinux_21.10_aarch64)')
    parser.add_argument('--hardware', type=str, help='Hardware support (e.g., I2,A2,A3)')
    parser.add_argument('--step', type=str, choices=['basic-info', 'create-config', FULL_FIELD],
                       default=FULL_FIELD, help='Step to execute')
    parser.add_argument('--project-root', type=str, help='Project root directory')
    
    parser.add_argument('--ssh-host', type=str, help='SSH host for remote OS (e.g., 192.168.1.100)')
    parser.add_argument('--ssh-port', type=int, default=22, help='SSH port (default: 22)')
    parser.add_argument('--ssh-user', type=str, default='root', help='SSH user (default: root)')
    parser.add_argument('--ssh-password', type=str, help='SSH password')
    parser.add_argument('--ssh-key', type=str, help='SSH private key file path')
    
    args = parser.parse_args()
    
    ssh_connector = None
    if args.ssh_host:
        logger.info(f"Connecting to remote host: {args.ssh_user}@{args.ssh_host}:{args.ssh_port}")
        ssh_connector = SSHConnector(
            host=args.ssh_host,
            port=args.ssh_port,
            user=args.ssh_user,
            password=args.ssh_password,
            key_file=args.ssh_key
        )
        
        if not ssh_connector.test_connection():
            logger.error(f"Failed to connect to {args.ssh_host}")
            logger.error("Please check SSH connectivity and credentials")
            sys.exit(1)
        logger.info("SSH connection established successfully")
    
    adapter = OSAdapter(args.project_root, ssh_connector)
    
    if not check_project(adapter):
        sys.exit(1)
    
    logger.info(f"Verified ascend-deployer project: {adapter.project_root}")
    
    hardware_list = []
    if args.hardware:
        hardware_list = [h.strip() for h in args.hardware.split(',')]
    
    if args.step == FULL_FIELD:
        adapter.run_full_adapter(args.os_name, hardware_list)
    elif args.step == 'basic-info':
        os_name = args.os_name or adapter.generate_os_name(adapter.get_os_info_from_system())
        os_constant = adapter.generate_os_constant_name(os_name)
        adapter.update_common_info(os_name, os_constant)
        if hardware_list:
            adapter.update_compatibility_config(os_name, hardware_list)
    elif args.step == 'create-config':
        os_name = args.os_name or adapter.generate_os_name(adapter.get_os_info_from_system())
        os_config_dir = adapter.create_os_config_directory(os_name)
        adapter.create_installed_txt(os_config_dir)
        adapter.create_source_repo(os_config_dir)
        adapter.create_pkg_info_json(os_config_dir)
        adapter.update_nexus_config(os_name)


if __name__ == '__main__':
    main()
