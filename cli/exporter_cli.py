#!/usr/bin/env python3
from pathlib import Path
from tools_managed_file.exporter import load_dataset, export_dataset

def main():
    print("=== Data Export Tool ===\n")

    file_path = Path(input("Dataset file (CSV/Excel): ").strip())
    base_name = file_path.stem + "_export"

    df = load_dataset(file_path)

    out_dir = Path(input("Output dir (default ./exports): ").strip() or "./exports")
    filename = input(f"Base name (default {base_name}): ").strip() or base_name

    export_dataset(df, out_dir, filename)
    print("\nExport complete!\n")

if __name__ == "__main__":
    main()
