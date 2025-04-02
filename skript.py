import os
import json
import shutil
from pathlib import Path

# Path to the JSON configuration file
CONFIG_FILE = "categories.json"

def load_config():
    """Load configuration from the JSON file."""
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_category_by_name(filename, config):
    """
    Check for a matching category based on substrings in the file name.
    
    Returns the first category whose 'name_contains' criteria is found in the file name.
    """
    lower_name = filename.lower()
    for category, rules in config.items():
        name_contains_list = rules.get("name_contains", [])
        if name_contains_list:
            if any(sub in lower_name for sub in name_contains_list):
                return category, rules
    return None, None

def get_category_by_extension(filename, config):
    """
    Check for a matching category based on the file extension.
    
    Returns the first category where 'extensions' contains the file's extension.
    """
    file_extension = Path(filename).suffix.lower()
    for category, rules in config.items():
        extensions_list = rules.get("extensions", [])
        if extensions_list and file_extension in [ext.lower() for ext in extensions_list]:
            return category, rules
    return None, None

def main():
    config = load_config()
    
    home_dir = Path.home()
    downloads_dir = home_dir / "Downloads"
    
    # Iterate through all files in the Downloads folder
    for item in downloads_dir.iterdir():
        if item.is_file():
            # First, try to categorize by file name
            category, rules = get_category_by_name(item.name, config)
            # If no match based on name, try matching by file extension
            if not category:
                category, rules = get_category_by_extension(item.name, config)
            if category:
                target_path = home_dir / rules["target_path"]
                target_path.mkdir(parents=True, exist_ok=True)
                destination = target_path / item.name
                print(f"Moving '{item.name}' to '{destination}' (category: {category})")
                shutil.move(str(item), str(destination))
            else:
                print(f"No category for '{item.name}', file skipped.")

if __name__ == '__main__':
    main()
