import unittest
import os
import shutil
import subprocess
import sys
from commands import *  # Import all functions from commands.py

class TestCommands(unittest.TestCase):
    def setUp(self):
        """Setup a test directory and files before each test."""
        self.test_dir = "test_dir"
        self.test_file = "test_file.txt"
        os.makedirs(self.test_dir, exist_ok=True)
        with open(self.test_file, "w") as f:
            f.write("Hello, World!")
    
    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_list_files(self):
        """Test listing files in a directory."""
        list_files(self.test_dir)
        list_files()
    
    def test_change_directory(self):
        """Test changing the directory."""
        current_dir = os.getcwd()
        change_directory(self.test_dir)
        self.assertEqual(os.getcwd(), os.path.abspath(self.test_dir))
        change_directory(current_dir)  # Change back
    
    def test_make_directory(self):
        """Test making a new directory."""
        new_dir = "new_test_dir"
        make_directory(new_dir)
        self.assertTrue(os.path.exists(new_dir))
        os.rmdir(new_dir)
    
    def test_remove_directory(self):
        """Test removing an existing directory."""
        remove_directory(self.test_dir)
        self.assertFalse(os.path.exists(self.test_dir))
    
    def test_create_file(self):
        """Test creating a new file."""
        new_file = "new_test_file.txt"
        create_file(new_file)
        self.assertTrue(os.path.exists(new_file))
        os.remove(new_file)
    
    def test_remove_item(self):
        """Test removing a file and a directory."""
        remove_item(self.test_file)
        self.assertFalse(os.path.exists(self.test_file))
        os.mkdir(self.test_dir)
        remove_item(self.test_dir)
        self.assertFalse(os.path.exists(self.test_dir))
    
    def test_move_item(self):
        """Test moving/renaming a file."""
        new_location = "moved_test_file.txt"
        move_item(self.test_file, new_location)
        self.assertTrue(os.path.exists(new_location))
        os.remove(new_location)
    
    def test_copy_item(self):
        """Test copying a file."""
        copied_file = "copied_test_file.txt"
        copy_item(self.test_file, copied_file)
        self.assertTrue(os.path.exists(copied_file))
        os.remove(copied_file)
    
    def test_nano(self):
        """Test nano function by writing content."""
        test_content = "This is a test."
        with open(self.test_file, "w") as f:
            f.write(test_content)
        nano(self.test_file)
        with open(self.test_file, "r") as f:
            content = f.read()
        self.assertIn(test_content, content)
    
    def test_open_vscode(self):
        """Test opening a file in VS Code."""
        try:
            open_vscode(self.test_file)
        except FileNotFoundError:
            self.skipTest("VS Code not found on system")
    
    def test_restart(self):
        """Test restarting the shell (should not actually restart)."""
        with self.assertRaises(OSError):
            restart()
    
    def test_search(self):
        """Test opening a web search."""
        try:
            search(["python", "unit testing"])
        except Exception as e:
            self.fail(f"Search failed: {e}")
    
if __name__ == "__main__":
    unittest.main()
