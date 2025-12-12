import os

def list_directory(path='.'):
    try:
        entries = os.listdir(path)            # Returns names of files + sub-directories. :contentReference[oaicite:1]{index=1}
        print(f"Contents of directory '{path}':")
        for name in entries:
            print(name)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Example: pass a path, or omit to use current working directory
    dir_path = input("/ ").strip() or '.'
    list_directory(dir_path)


    import os

# Ask the user for a folder path
folder_path = input(" / ")

# List all files and folders inside it
contents = os.listdir(folder_path)

# Print them one by one
for item in contents:
    print(item)

