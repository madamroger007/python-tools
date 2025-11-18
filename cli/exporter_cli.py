#!/usr/bin/env python3
from pathlib import Path
from tools_managed_file.exporter import load_dataset, export_dataset

def main():
    print("=== Data Export Tool ===\n")

    file_path = Path(input("Dataset file (CSV/Excel): ").strip().replace('"', ''))
    df = load_dataset(file_path)

    out_dir = Path(input("Output dir (default ./exports): ").strip() or "./exports")
    base_name = input("Base name (without extension): ").strip() or file_path.stem

    output = export_dataset(df, out_dir, base_name)
    print("\nExported to:", output)

if __name__ == "__main__":
    main()
