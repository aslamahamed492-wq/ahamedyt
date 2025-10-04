# Automated File Organizer

## 📖 Project Description
The **Automated File Organizer** is a Python script that scans a specified directory, detects files based on their extensions, and organizes them into categorized folders like **Documents**, **Images**, **Python_Code**, etc.  

The script also:
- Handles duplicate file names (`file(1).txt`)
- Manages permission errors gracefully
- Supports **dry-run mode** to preview changes before organizing files
- Logs all operations with timestamps  

---

## 🚀 Features
- **Recursive Directory Traversal** → Scans subdirectories using `os.walk` or `pathlib`.
- **File Type Detection** → Categorizes files based on extensions with fallback to "Other".
- **Conflict Resolution** → Automatically renames duplicate files.
- **Dry-Run Mode** → Preview actions without making any changes.
- **Error Handling** → Handles invalid paths, permission errors, and locked files.
- **Logging & Reporting** → Creates a `organizer.log` file and prints summary reports.

---

## 📂 Project Structure
```
AutomatedFileOrganizer/
├── organizer.py      # Main Python script
├── README.md         # Project documentation
├── test_files/       # Sample files for testing
└── organizer.log     # Log file generated after running the script
```

---

## 🛠 Requirements
- Python 3.6+
- No external dependencies (uses Python's built-in libraries)

---

## ⚡ Usage

### 1. Run with Dry-Run Mode (Preview Changes)
```bash
python organizer.py /path/to/your/folder --dry-run
```
This will **show what files would be moved** without actually moving them.

### 2. Run for Actual Organization
```bash
python organizer.py /path/to/your/folder
```
This will **move files into categorized folders**.

---

## 🗂 File Categorization Example
| Extension           | Folder Name      |
|---------------------|------------------|
| `.py`               | Python_Code      |
| `.txt`, `.pdf`      | Documents        |
| `.jpg`, `.jpeg`, `.png` | Images        |
| `.mp3`, `.mp4`      | Music / Videos   |
| others              | Other            |

---

## 📝 Logging
- All operations are stored in `organizer.log` with timestamps.
- Example log:
  ```
  2025-09-28 10:30:00 - INFO - Created directory: /path/Documents
  2025-09-28 10:30:00 - INFO - Moved /path/report.txt → /path/Documents/report.txt
  2025-09-28 10:30:01 - ERROR - Permission denied: /path/locked_file.txt
  ```

---

## 🎯 Learning Outcomes
- Python file system navigation (`os`, `pathlib`, `shutil`)
- CLI development using `argparse`
- Error handling with exceptions
- Logging for real-world automation scripts
- Best practices for file system operations

---

## 👨‍💻 Author
Developed as part of a **Python Automation Project** for learning file organization and scripting best practices.
