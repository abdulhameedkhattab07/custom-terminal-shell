import subprocess
import shlex
import os
import commands
import glob

try:
    import readline
except ImportError:
    import pyreadline3 as readline

def main():
    ...

def run_python_code(command):
    """Runs a Python script or command in the terminal"""
    try:
        # Ensure the command is correctly split into parts
        args = shlex.split(command)

        # If running a Python script, ensure 'python' is added
        if args[0].endswith(".py"):
            args.insert(0, "python")  # Ensure Python is used to execute scripts

        # Run the command and capture output
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()  # Wait for command to complete

        # Print output
        if stdout:
            print(stdout)

        # Print errors if any
        if stderr:
            print("\033[1;31mError:\033[0m", stderr)

    except FileNotFoundError:
        print("\033[1;31mPython is not found in your PATH.\033[0m")
    except Exception as e:
        print(f"\033[1;31mError:\033[0m {e}")

def start_shell():
    """Runs thee shell with a linux style"""
    
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[1;32m" + "-" * 50)
    print("        Welcome to MyCustomShell  ")
    print("      Type 'help' for available commands.")
    print("      Type 'exit' to close shell.")
    print("-" * 50 + "\033[0m")

    while True:
        try:
            current_dir = os.getcwd().replace(os.path.expanduser("~"), "~")
            prompt = f"\033[1;32m{current_dir}\033[1;34m$ \033[0m"
            user_input = input(prompt).strip()
            if not user_input:
                continue
            command_parts = user_input.split()
            command = command_parts[0]
            args = command_parts[1:]

            if command == "python":
                run_python_code("python " + " ".join(args))

            elif command == "exit":
                print("\n\033[1;31mGoodbye! See you soon! \033[0m")
                break

            elif command == "ls":
                if args:
                    commands.list_files(''.join(args))
                else:
                    commands.list_files()

            elif command == "clear":
                commands.clear_screen()
            
            elif command == "help":
                commands.help_command()

            elif command == "touch":
                if args:
                    commands.create_file(args[0])
                else:
                    print("\033[1;31mUsage: touch <filename>.\033[0m")
            
            elif command == "nano":
                if args:
                    commands.nano(args[0])
                else:
                    print("\033[1;31mUsage: nano <filename>.\033[0m")

            elif command == "code":
                if args:
                    commands.open_vscode(args[0])
                else:
                    commands.open_vscode()

            elif command == "restart":
                commands.restart()

            elif command == "search":
                if args:
                    commands.search(args)
                else:
                    commands.search()

            elif command == "rm":
                if args:
                    commands.remove_item(args[0])
                else:
                    print("\033[1;31mUsage: rm <file/directory>.\033[0m")

            elif command == "mv":
                if len(args) == 2:
                    commands.move_item(args[0], args[1])
                else:
                    print("\033[1;31mUsage: mv <source> <destination>.\033[0m")

            elif command == "cp":
                if len(args) == 2:
                    commands.copy_item(args[0], args[1])
                else:
                    print("\033[1;31mUsage: cp <source> <destination>.\033[0m")

            elif command == "cd":
                target_dir = " ".join(args)
                if target_dir:
                    commands.change_directory(target_dir)
                else:
                    commands.change_directory(os.path.expanduser("~"))
            
            elif command == "mkdir":
                if args:
                    commands.make_directory(args[0])
                else:
                    print("\033[1;31mUsage: mkdir <folder_name>\033[0m")

            else:
                print(f"\033[1;31mError: Command '{command}' not found.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;31mGoodbye! See you soon! \033[0m")
            break

def complete(text, state):
    """Auto-completes file and directory names"""
    return (glob.glob(text + "*") + [None])[state]

def set_read_line():
    readline.set_completer(complete)
    readline.parse_and_bind("tab: complete")

if __name__ == "__main__":
    os.chdir(os.path.expanduser("~"))
    set_read_line()
    start_shell()
