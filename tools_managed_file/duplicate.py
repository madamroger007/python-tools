from pathlib import Path
import shutil
from .utils import validate_file, safe_filename


def duplicate_file(src_path: Path, dst_dir: Path, count: int = 1) -> list[Path]:
    """
    Duplicate a file multiple times.
    src_path -> original file
    dst_dir  -> folder where duplicates will be stored
    count    -> how many duplicates to create
    Returns list of all duplicated file paths.
    """
    validate_file(src_path)

    if count < 1:
        raise ValueError("count must be >= 1")

    dst_dir = Path(dst_dir)
    dst_dir.mkdir(parents=True, exist_ok=True)

    src_name = safe_filename(src_path.stem)
    extension = src_path.suffix

    duplicated_files = []

    for i in range(1, count + 1):
        new_name = f"{src_name}_copy{i}{extension}"
        dst_path = dst_dir / new_name

        shutil.copy2(src_path, dst_path)
        duplicated_files.append(dst_path)

    return duplicated_files
