import shutil
import os
import os.path
import subprocess
import platform
import sys

command_generator = {
    'gcc': lambda dir: ['gcc', 'tests/' + dir + '/main.cpp', '-fsyntax-only'],
    'clang': lambda dir: ['clang', 'tests/' + dir + '/main.cpp', '-fsyntax-only'],
    'msvc': lambda dir: ['cl', 'tests/' + dir + '/main.cpp', '/Zs'],
}

if len(sys.argv) != 2:
    print("Usage: run.py gcc|clang|msvc")
    sys.exit(1)

if sys.argv[1] not in command_generator:
    print("Usage: run.py gcc|clang|msvc")
    sys.exit(1)

compiler = command_generator[sys.argv[1]]

# Set up tests
print("Setting up 'duplicate' test")
header = "tests/duplicate/header.hpp"
duplicate = "tests/duplicate/duplicate.hpp"
if os.path.isfile(duplicate):
    print(" - Removing existing file (" + duplicate + ")")
    os.remove(duplicate)
print(" - Creating duplicate of header.hpp")
shutil.copy(header, duplicate)
fs = os.stat(header)
print(" - Updating modification time")
os.utime(duplicate, (fs.st_atime + 1, fs.st_mtime))

print("\nSetting up 'hardlink' test")
hardlink = "tests/hardlink/hardlink.hpp"
if os.path.isfile(hardlink):
    print(" - Removing existing hardlink (" + hardlink + ")")
    os.unlink(hardlink)
print(" - Creating hardlink of header.hpp")
os.link("tests/hardlink/header.hpp", hardlink)

print("\nSetting up 'symlink' test")
symlink = "tests/symlink/symlink.hpp"
if os.path.islink(symlink):
    print(" - Removing existing symlink (" + symlink + ")")
    os.unlink(symlink)
print(" - Creating symlink of header.hpp")
os.symlink("header.hpp", symlink)

print("\nSetting up 'case' test")
casedir = "tests/case/dir"
if os.path.isdir(casedir):
    print(" - Removing existing directory (" + casedir + ")")
    shutil.rmtree(casedir, ignore_errors=True)
print(" - Creating directory (" + casedir + ")")
os.mkdir(casedir)
if platform.system == "Windows":
    print(" - Making directory case sensitive (Windows Only)")
    completed = subprocess.run(["powershell", "-Command", "fsutil.exe file SetCaseSensitiveInfo tests\\case\\dir enable"], capture_output=True)
lower = casedir + "/header.hpp"
print(" - Creating (" + lower + ")")
shutil.copy('tests/case/lower.hpp', lower)
upper = casedir + "/HEADER.hpp"
print(" - Creating (" + upper + ")")
shutil.copy('tests/case/upper.hpp', upper)

# Run tests
print("\nRunning tests")
for test in os.listdir("tests"):
    subprocess.run(compiler(test))