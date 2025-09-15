# file_handling.py
"""
File Read & Write Challenge + Error Handling Lab
Reads a file, modifies its content (default: uppercase), and writes to a new file.
"""

import os

def modify_content(content):
    """Modify the content. Default: convert to uppercase.
    Edit this function to change behavior (reverse lines, strip blanks, etc.)."""
    return content.upper()

def file_read_write(input_path, output_path):
    """Read input_path, write modified content to output_path. Returns True on success."""
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: '{input_path}'")
        return False
    except PermissionError:
        print(f"Error: Permission denied reading '{input_path}'")
        return False
    except Exception as e:
        print(f"Error reading '{input_path}': {e}")
        return False

    modified = modify_content(data)

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(modified)
    except PermissionError:
        print(f"Error: Permission denied writing '{output_path}'")
        return False
    except Exception as e:
        print(f"Error writing '{output_path}': {e}")
        return False

    print(f"Success: modified file written to '{output_path}'")
    return True

def main():
    while True:
        filename = input("Enter filename to read (or type 'exit' to quit): ").strip()
        if not filename:
            print("Please enter a filename or 'exit'.")
            continue
        if filename.lower() in ("exit", "quit"):
            print("Exiting.")
            return

        output_filename = "modified_" + os.path.basename(filename)
        ok = file_read_write(filename, output_filename)
        if ok:
            print("Done.")
            return
        else:
            print("If the file exists, check permissions; otherwise try a different filename or type 'exit'.")

if __name__ == "__main__":
    main()
