# Custom Terminal Shell by Khattab
#### Video Demo:  <[URL HERE](https://youtu.be/_jGe-cf1yB0)>
#### Description: 
Custom Terminal Shell is a Python-based command-line interface that allows users to interact with their system efficiently. It supports various built-in commands such as listing files, creating and removing directories, moving and copying files, searching the web, and even opening files in VS Code.

## Features
- **File and Directory Management**: List, create, remove, and navigate directories.
- **File Operations**: Copy, move, create, and delete files.
- **Web Search**: Open a web browser with search queries.
- **Text Editing**: Open files in nano editor.
- **VS Code Integration**: Open files directly in Visual Studio Code.
- **System Commands**: Restart the shell and execute system commands.

## Installation
### Prerequisites
- Python 3.x installed on your system
- Git installed (optional for cloning the repository)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/abdulhameedkhattab07/custom-terminal-shell.git
   ```
2. Navigate to the project directory:
   ```bash
   cd custom-terminal-shell
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the shell:
   ```bash
   python project.py
   ```

## Usage
Once the shell is running, you can use the following commands:

### Directory Operations
- `ls` - List files in the current directory
- `cd <directory>` - Change directory
- `mkdir <directory>` - Create a new directory
- `rmdir <directory>` - Remove a directory

### File Operations
- `touch <filename>` - Create a new file
- `rm <filename>` - Delete a file
- `mv <source> <destination>` - Move or rename a file
- `cp <source> <destination>` - Copy a file

### Other Commands
- `nano <filename>` - Open a file in nano editor
- `code <filename>` - Open a file in Visual Studio Code
- `search <query>` - Perform a web search
- `restart` - Restart the shell
- `exit` - Exit the shell
- `help` - Check Help

## Testing
To run tests using `pytest`, execute:
```bash
pytest test_project.py
```
or Test with unittest
```bash
python test.py
```

## Author
- **Khattab Abdulhameed**
- GitHub: [abdulhameedkhattab07](https://github.com/abdulhameedkhattab07)
- eDx: abdulhameedkhattab07

## License
This project is licensed under the MIT License - see the LICENSE file for details.