import os
import shutil
import subprocess
import sys
import platform
import webbrowser

def list_files(target=None):
    """Lists files and directories in the current directory."""
    if target is not None:
        for item in os.listdir(target):
            print(item)
    else:
        for item in os.listdir():
            print(item)

def change_directory(target):
    """Changes the current working directory."""
    try:
        os.chdir(os.path.expanduser(target))
    except FileNotFoundError:
        print("Error: No such directory")
    except PermissionError:
        print("Error: Permission denied.")

def make_directory(name):
    """Creates a new directory."""
    try:
        os.mkdir(name)
        print(f"Folder: '{name}' created successfully")
    except FileExistsError:
        print("Error: Directory already exists.")
    except PermissionError  :
        print("Error: Permission Denied.")

def remove_directory(name):
    """Removes a directory"""
    try:
        os.rmdir(name)
    except FileNotFoundError:
        print("Error: Directory not found")
    except PermissionError:
        print("Error: Permission Denied")

def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def help_command():
    """Displays a list of available commands with descriptions."""
    help_text = """
\033[1;33m--------------- Available Commands ----------------\033[0m
\033[1;32mhelp\033[0m      - Show this help message
\033[1;32mclear\033[0m      - Clear the terminal screen
\033[1;32mexit\033[0m      - Exit the custom shell
\033[1;32mls <dir>\033[0m      - Lists files and folders in the current directory or in <dir>
\033[1;32mcd <dir>\033[0m      - change the current directory to <dir>
\033[1;32mmkdir <name>\033[0m      - create a new directory named <name>
\033[1;32mrm <name>\033[0m      - removes a file or an empty directory named <name>
\033[1;32mtouch <file>\033[0m      - creates a new empty file named <file>
\033[1;32mcode <target>\033[0m      - opens <target> in Vs code.
\033[1;32msearch [<arguments>]\033[0m      - searches for argument in the browser
\033[1;32mnano <file>\033[0m      - opens a mini file editor in the terminal to edit <file>
\033[1;33m----------------------------------------------------\033[0m
"""

    print(help_text)

def create_file(name):
    """Creates an empty file."""
    try:
        with open(name, "w") as f:
            pass
        print(f"File '{name}' created successfully.")
    except Exception as e:
        print(f"\033[1;31mError: creating file: {e}\033[0m")

def remove_item(name):
    """Deletes a file or directory."""
    if os.path.isfile(name):
        os.remove(name)
        print(f"File '{name}' deleted.")
    elif os.path.isdir(name):
        shutil.rmtree(name)
        print(f"Directory '{name}' removed.")
    else:
        print("\033[1;31mError: FIle/Directory not found.\033[0m")

def move_item(src, dest):
    """Moves or renames a file/directory"""
    try:
        shutil.move(src, dest)
        print(f"Moved '{src}' to '{dest}'")
    except Exception as e:
        print(f"\033[1;31mError: {e}\033[0m")

def copy_item(src, dest):
    """Copies a file or directory """
    try:
        if os.path.isfile(src):
            shutil.copy(src, dest)
        elif os.path.isdir(src):
            shutil.copytree(src, dest)
        print(f"Copied '{src}' to '{dest}'")
    except Exception as e:
        print(f"\033[1;31mError: {e}\033[0m")

def nano(filename):
    """Simple terminal-based text editor"""
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    print(f"Editing: {filename} (Type ':q' to save and exit)")

    while True:
        line = input()
        if line == ":q":
            break
        lines.append(line + "\n")

    with open(filename, "w") as f:
        f.writelines(lines)

    print(f"\033[1;32mFile saved: {filename}\033[0m")
    

def open_vscode(target=None):
    """Opens a file in VS Code."""
    if platform.system() == "Windows":
        vscode_cmd = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Update this path!
    else:
        vscode_cmd = "code"

    try:
        if target:
            subprocess.run([vscode_cmd, target], check=True)
        else:
            subprocess.run([vscode_cmd], check=True)
    except FileNotFoundError:
        print("\033[1;31mError: VS Code not found.\033[0m")
    except PermissionError:
        print("\033[1;31mError: Permission denied. Try running as administrator.\033[0m")

def restart():
    """Restarts the shell."""
    print("\033[1;34mRestarting shell....\033[0m")
    python = sys.executable
    os.execv(python, [python] + sys.argv)

def search(args=None):
    if args:
        query = "+".join(args)
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
    else:
        webbrowser.open("https://www.google.com")