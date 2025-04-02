# File Organizer Script

## Overview
This Python script automatically organizes files and folders located in the user's **Downloads** folder into target directories specified in an external JSON configuration file (`categories.json`). The script prioritizes file categorization by matching file name substrings first, and if no match is found, it falls back to matching the file extension.

## Requirements
- **Python 3.x** – The script is written in Python.
- **Configuration File (`categories.json`)** – Must be located in the same directory as the script.

## Installation
1. Place the Python script (e.g., `file_organizer.py`) and the `categories.json` file in the same directory.
2. Ensure that Python 3 is installed on your system.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script with the following command:
   ```bash
   python file_organizer.py