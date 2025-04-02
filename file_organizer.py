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

def get_category_by_name(item_name, config):
    """
    Check for a matching category based on substrings in the file or directory name.
    
    Returns the first category whose 'name_contains' criteria is found in the name.
    """
    lower_name = item_name.lower()
    for category, rules in config.items():
        name_contains_list = rules.get("name_contains", [])
        if name_contains_list:
            if any(sub in lower_name for sub in name_contains_list):
                return category, rules
    return None, None

def get_category_by_extension(item_name, config):
    """
    Check for a matching category based on the file extension.
    
    Returns the first category where 'extensions' contains the file's extension.
    """
    file_extension = Path(item_name).suffix.lower()
    for category, rules in config.items():
        extensions_list = rules.get("extensions", [])
        if extensions_list and file_extension in [ext.lower() for ext in extensions_list]:
            return category, rules
    return None, None

def main():
    config = load_config()
    
    home_dir = Path.home()
    downloads_dir = home_dir / "Downloads"
    
    # Iterate through all items (files and directories) in the Downloads folder
    for item in downloads_dir.iterdir():
        # Process both files and directories
        if item.is_file() or item.is_dir():
            # First, try to categorize by name for both files and directories
            category, rules = get_category_by_name(item.name, config)
            
            # For files, if no match by name, try matching by extension
            if not category and item.is_file():
                category, rules = get_category_by_extension(item.name, config)
            
            if category:
                target_path = home_dir / rules["target_path"]
                target_path.mkdir(parents=True, exist_ok=True)
                destination = target_path / item.name
                print(f"Moving '{item.name}' to '{destination}' (category: {category})")
                shutil.move(str(item), str(destination))
            else:
                print(f"No category for '{item.name}', skipping.")

if __name__ == '__main__':
    main()
