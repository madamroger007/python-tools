#!/usr/bin/env python3
from pathlib import Path
from tools_managed_file.duplicate import duplicate_file

def main():
    print("=== Duplicate File Tool ===")

    src = Path(input("File path: ").strip().replace('"', ''))
    count = int(input("How many copies: ").strip())

    out_dir = Path("./duplicates")
    out_dir.mkdir(exist_ok=True)

    try:
        results = duplicate_file(src, out_dir, count)
        print("\nCreated files:")
        for f in results:
            print(" -", f)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
