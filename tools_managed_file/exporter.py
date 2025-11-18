import csv
from pathlib import Path
from .utils import safe_filename

def export_dataset(data: list, output_path: Path) -> Path:
    """
    Export a list of dictionaries into a CSV file.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not data:
        raise ValueError("Dataset is empty.")

    # Extract header from keys of the first item
    headers = data[0].keys()

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    return output_path
