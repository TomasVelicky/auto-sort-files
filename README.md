# File Organizer Script

Working on Windows version and app for custom categories.

## Overview
This Python script automatically organizes files and folders located in the user's **Downloads** folder into target directories specified in an external JSON configuration file (`categories.json`). The script prioritizes file categorization by matching file name substrings first, and if no match is found, it falls back to matching the file extension.

## Requirements
- **Python 3.x** – The script is written in Python.
- **Configuration File (`categories.json`)** – Must be located in the same directory as the script.
- [`watchdog`](https://pypi.org/project/watchdog/): - only for `file_organizer_realtime.py`
  ```bash
  pip install watchdog

## Installation
1. Place the Python script (`file_organizer.py` or `file_organizer_realtime.py`) and the `categories.json` file in the same directory.
2. Ensure that requirements are installed on your system.
3. Ready to use.

# Manual usage
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script with the following command:
   ```bash
   python file_organizer.py
or
   ```bash
   python file_organizer_realtime.py
