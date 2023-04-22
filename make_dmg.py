import os
import re


"""
Uses semantic versioning: https://semver.org/: [major.minor.patch-state]
State can be: alpha, beta, rc, release.
"""


with open(".env", "r") as file:
    contents = file.read()
    version_match = re.search(r"VERSION=(\d+)\.(\d+)\.(\d+)-(.+)", contents)
    current_major_version = int(version_match.group(1))
    current_minor_version = int(version_match.group(2))
    current_patch_version = int(version_match.group(3))
    current_state = version_match.group(4)
    system_match = re.search(r"SYSTEM=(\S+)", contents)
    current_os_type = system_match.group(1)
    system_type_match = re.search(r"SYSTEM_TYPE=(\S+)", contents)
    current_system_type = system_type_match.group(1) if system_type_match is not None else "unknown"


app_name = f"altern8-shell-{current_major_version}-{current_minor_version}-{current_patch_version}_{current_state}"
os.system(f'pyinstaller --onefile --windowed --name {app_name} --add-data ".env;." shell.py')
# os.system(f'cp -r "path/to/altern8" "dist/{app_name}/altern8"')

