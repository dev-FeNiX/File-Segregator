import os
from pathlib import Path
from shutil import move

EXTENSIONS = {
    'Videos': ['mp4', 'mkv'],
    'Audios': ['mp3', 'wav', 'ogg'],
    'Images': ['jpg', 'jpeg', 'png', 'gif', 'webp', 'svg'],
    'Docs':   ['pdf', 'doc', 'docx', 'txt', 'ppt', 'pptx', 'xls', 'xlsx', 'csv'],
}

MISC_FOLDER = 'Misc'

def classify_file(extension: str) -> str:
    for category, ext_list in EXTENSIONS.items():
        if extension in ext_list:
            return category
    return MISC_FOLDER

def organize_files(folder_path: str, progress_callback=None):
    folder = Path(folder_path)
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    files_moved = 0
    total_files = sum(1 for f in folder.iterdir() if f.is_file())

    for i, file in enumerate(folder.iterdir()):
        if file.is_file():
            ext = file.suffix[1:].lower()
            category = classify_file(ext)
            target_dir = folder / category
            target_dir.mkdir(exist_ok=True)

            # Handle conflicts by adding suffix if file exists
            dest_file = target_dir / file.name
            counter = 1
            while dest_file.exists():
                stem = file.stem
                suffix = file.suffix
                dest_file = target_dir / f"{stem}({counter}){suffix}"
                counter += 1

            move(str(file), str(dest_file))
            files_moved += 1

            if progress_callback:
                progress_callback(i + 1, total_files)

    return files_moved
