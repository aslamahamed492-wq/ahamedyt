#!/usr/bin/env python3
"""
Automated File Organizer
---------------------------------
Scans a directory, detects files by type, and organizes them into categorized folders.
Supports dry-run mode, logging, and duplicate filename handling.
"""

import os
import shutil
import argparse
import logging
from datetime import datetime
from pathlib import Path

# Define file type categories
FILE_CATEGORIES = {
    "Documents": [".txt", ".pdf", ".docx", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Python_Code": [".py"],
    "Music_Videos": [".mp3", ".wav", ".mp4", ".mkv", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executables": [".exe", ".bat", ".sh"],
}

# Setup logging
logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_category(file_extension):
    """Return category name based on file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return "Other"

def resolve_conflict(destination_path):
    """Rename duplicate files with (1), (2), etc."""
    base = destination_path.stem
    suffix = destination_path.suffix
    parent = destination_path.parent
    counter = 1

    while destination_path.exists():
        destination_path = parent / f"{base}({counter}){suffix}"
        counter += 1
    return destination_path

def organize_files(target_dir, dry_run=False):
    """Organize files by category."""
    target_dir = Path(target_dir)

    if not target_dir.exists():
        print(f"❌ Error: Path '{target_dir}' does not exist.")
        return

    for root, _, files in os.walk(target_dir):
        for file in files:
            file_path = Path(root) / file
            if file_path.name == "organizer.log":
                continue  # skip log file itself

            category = get_category(file_path.suffix)
            category_folder = target_dir / category
            dest_path = category_folder / file_path.name

            dest_path = resolve_conflict(dest_path)

            if dry_run:
                print(f"[DRY-RUN] Would move: {file_path} → {dest_path}")
                continue

            try:
                category_folder.mkdir(exist_ok=True)
                shutil.move(str(file_path), str(dest_path))
                logging.info(f"Moved {file_path} → {dest_path}")
                print(f"✅ Moved: {file_path} → {dest_path}")
            except PermissionError:
                logging.error(f"Permission denied: {file_path}")
                print(f"⚠️ Permission denied: {file_path}")
            except Exception as e:
                logging.error(f"Error moving {file_path}: {e}")
                print(f"⚠️ Error moving {file_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated File Organizer")
    parser.add_argument("path", help="Path to the folder you want to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving files")

    args = parser.parse_args()

    print("📂 Starting File Organizer...")
    start_time = datetime.now()

    organize_files(args.path, dry_run=args.dry_run)

    end_time = datetime.now()
    print(f"\n✅ Completed in {(end_time - start_time).total_seconds():.2f} seconds.")
