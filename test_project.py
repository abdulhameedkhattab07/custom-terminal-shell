import os
import shutil
import subprocess
import sys
import pytest
from commands import *  # Import all functions from commands.py

@pytest.fixture(scope="function")
def setup_test_env():
    """Setup a test directory and files before each test."""
    test_dir = "test_dir"
    test_file = "test_file.txt"
    os.makedirs(test_dir, exist_ok=True)
    with open(test_file, "w") as f:
        f.write("Hello, World!")
    yield test_dir, test_file
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)

def test_list_files(setup_test_env):
    """Test listing files in a directory."""
    test_dir, _ = setup_test_env
    list_files(test_dir)
    list_files()

def test_change_directory(setup_test_env):
    """Test changing the directory."""
    test_dir, _ = setup_test_env
    current_dir = os.getcwd()
    change_directory(test_dir)
    assert os.getcwd() == os.path.abspath(test_dir)
    change_directory(current_dir)

def test_make_directory():
    """Test making a new directory."""
    new_dir = "new_test_dir"
    make_directory(new_dir)
    assert os.path.exists(new_dir)
    os.rmdir(new_dir)

def test_remove_directory(setup_test_env):
    """Test removing an existing directory."""
    test_dir, _ = setup_test_env
    remove_directory(test_dir)
    assert not os.path.exists(test_dir)

def test_create_file():
    """Test creating a new file."""
    new_file = "new_test_file.txt"
    create_file(new_file)
    assert os.path.exists(new_file)
    os.remove(new_file)

def test_remove_item(setup_test_env):
    """Test removing a file and a directory."""
    _, test_file = setup_test_env
    remove_item(test_file)
    assert not os.path.exists(test_file)
    test_dir = "test_dir"
    os.mkdir(test_dir)
    remove_item(test_dir)
    assert not os.path.exists(test_dir)

def test_move_item(setup_test_env):
    """Test moving/renaming a file."""
    _, test_file = setup_test_env
    new_location = "moved_test_file.txt"
    move_item(test_file, new_location)
    assert os.path.exists(new_location)
    os.remove(new_location)

def test_copy_item(setup_test_env):
    """Test copying a file."""
    _, test_file = setup_test_env
    copied_file = "copied_test_file.txt"
    copy_item(test_file, copied_file)
    assert os.path.exists(copied_file)
    os.remove(copied_file)

def test_nano(setup_test_env):
    """Test nano function by writing content."""
    _, test_file = setup_test_env
    test_content = "This is a test."
    with open(test_file, "w") as f:
        f.write(test_content)
    nano(test_file)
    with open(test_file, "r") as f:
        content = f.read()
    assert test_content in content

def test_open_vscode(setup_test_env):
    """Test opening a file in VS Code."""
    _, test_file = setup_test_env
    try:
        open_vscode(test_file)
    except FileNotFoundError:
        pytest.skip("VS Code not found on system")

def test_restart():
    """Test restarting the shell (should not actually restart)."""
    with pytest.raises(OSError):
        restart()

def test_search():
    """Test opening a web search."""
    try:
        search(["python", "unit testing"])
    except Exception as e:
        pytest.fail(f"Search failed: {e}")

if __name__ == "__main__":
    pytest.main()
