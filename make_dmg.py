import os
import sys

if len(sys.argv) != 4:
    print("Usage: python make_dmg.py x y z")
    sys.exit(1)

x, y, z = sys.argv[1:4]
app_name = f"altern8-shell-{x}-{y}-{z}"
os.system(f"pyinstaller --onefile --windowed --name {app_name} shell.py")

