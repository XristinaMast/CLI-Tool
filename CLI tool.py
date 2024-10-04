import cmd
import os

class FileManagerCLI(cmd.Cmd):
    prompt = 'FileMngr>> '
    intro = 'Welcome to FileManagerCLI. Type "help" for available commands.'

    def __init__(self):
        super().__init__()
        self.current_directory = os.getcwd()

    def preloop(self):
        """Initialization before the CLI loop."""
        print("Initialization before the CLI loop")

    def postloop(self):
        """Finalization after the CLI loop."""
        print("Finalization after the CLI loop")

    def precmd(self, line):
        """Code to execute before a command."""
        print("Before command execution")
        return line

    def postcmd(self, stop, line):
        """Code to execute after a command."""
        print()  # Empty line for better readability
        return stop

    def do_list(self, line):
        """List files and directories in the current directory."""
        files_and_dirs = os.listdir(self.current_directory)
        for item in files_and_dirs:
            print(item)

    def do_change_dir(self, directory):
        """Change the current directory. Usage: change_dir <directory>"""
        if not directory:
            print("Usage: change_dir <directory>")
            return
        new_dir = os.path.join(self.current_directory, directory)
        if os.path.exists(new_dir) and os.path.isdir(new_dir):
            self.current_directory = new_dir
            print(f"Current directory changed to {self.current_directory}")
        else:
            print(f"Directory '{directory}' does not exist.")

    def do_create_file(self, filename):
        """Create a new text file in the current directory. Usage: create_file <filename>"""
        if not filename:
            print("Usage: create_file <filename>")
            return
        file_path = os.path.join(self.current_directory, filename)
        try:
            with open(file_path, 'w') as new_file:
                print(f"File '{filename}' created in {self.current_directory}")
        except Exception as e:
            print(f"Error: {e}")

    def do_read_file(self, filename):
        """Read the contents of a text file in the current directory. Usage: read_file <filename>"""
        if not filename:
            print("Usage: read_file <filename>")
            return
        file_path = os.path.join(self.current_directory, filename)
        try:
            with open(file_path, 'r') as existing_file:
                print(existing_file.read())
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def do_delete_file(self, filename):
        """Delete a file in the current directory. Usage: delete_file <filename>"""
        if not filename:
            print("Usage: delete_file <filename>")
            return
        file_path = os.path.join(self.current_directory, filename)
        try:
            os.remove(file_path)
            print(f"File '{filename}' deleted from {self.current_directory}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def do_rename_file(self, args):
        """Rename a file in the current directory. Usage: rename_file <old_filename> <new_filename>"""
        parts = args.split()
        if len(parts) != 2:
            print("Usage: rename_file <old_filename> <new_filename>")
            return
        old_filename, new_filename = parts
        old_file_path = os.path.join(self.current_directory, old_filename)
        new_file_path = os.path.join(self.current_directory, new_filename)
        try:
            os.rename(old_file_path, new_file_path)
            print(f"File '{old_filename}' renamed to '{new_filename}'")
        except FileNotFoundError:
            print(f"File '{old_filename}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def do_quit(self, line):
        """Exit the CLI."""
        return True

if __name__ == '__main__':
    FileManagerCLI().cmdloop()      