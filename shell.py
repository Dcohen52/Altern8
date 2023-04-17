import os
import re

import altern8
import datetime
import tkinter as tk
from tkinter import filedialog

os.system("cls" if os.name == "nt" else "clear")


def get_default_test_file():
    os.path.join(os.path.join(os.environ['USERPROFILE' if os.name == 'nt' else '~']), 'Desktop', 'test.alt8')


def load_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[('Altern8 Files', '*.alt8')])
    return f'run("{file_path}")'


def load_test_file():
    default_file_path = get_default_test_file()
    if os.path.exists(default_file_path):
        return f'run("{default_file_path}")'
    else:
        with open(default_file_path, 'w') as f:
            f.write('print("Hello from Altern8!", "nl")')
        return f'run("{default_file_path}")'


# Read version from settings file
with open(".env", "r") as file:
    contents = file.read()
    date_time_match = re.search(r"DATE_TIME=(.+)", contents)
    current_date_time = date_time_match.group(1)
    version_match = re.search(r"VERSION=(\d+)\.(\d+)\.(\d+)-(.+)", contents)
    current_version = version_match.group(0)
    system_match = re.search(r"SYSTEM=(\S+)", contents)
    current_os_type = system_match.group(1) if system_match is not None else "unknown"
    system_type_match = re.search(r"SYSTEM_TYPE=(\S+)", contents)
    current_system_type = system_type_match.group(1) if system_type_match is not None else "unknown"

print(
    f"""Altern8 (v{current_version.strip("VERSION=")}, {current_date_time.strip('"')}) [Python 3.10.2 (v3.10.2:a58ebcc701)] on {current_os_type}.
Type "docs" for general information, supported commands and more.""")

while True:
    try:
        text = input(f">>> ")
        if text.strip() == "":
            continue
        if text == "run -f":
            text = load_file()
        if text == "run -t":
            text = load_test_file()
        else:
            result, error = altern8.run('<stdin>', text)
        if text == "quit" or text == "close":
            altern8.close()
        elif text == "docs":
            altern8.documentation()
        elif error:
            print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(result.elements[0])
            else:
                print(repr(result))
    except Exception as e:
        print(e)
