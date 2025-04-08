import os

def print_directory_contents(path='.'):
    try:
        # Get the list of all files and directories
        items = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        for item in items:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory path you want to list
directory_path = '.'  # Current directory
print_directory_contents(directory_path)