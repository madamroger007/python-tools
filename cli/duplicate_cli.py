#!/usr/bin/env python3
from pathlib import Path
from tools_managed_file.duplicate import duplicate_file

def main():
    print("=== Duplicate File Tool ===")

    file_path = Path(input("File path: ").strip().strip('"').strip("'"))
    count = int(input("How many copies: "))

    try:
        zip_path = duplicate_file(file_path, count)
        if zip_path:
            print(f"\nZIP created at: {zip_path}")
        print("Success!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
