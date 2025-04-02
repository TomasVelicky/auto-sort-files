from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from pathlib import Path
import shutil
import json
import os

CONFIG_FILE = "categories.json"

def load_config():
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_category_by_name(name, config):
    lower_name = name.lower()
    for category, rules in config.items():
        substrs = rules.get("name_contains", [])
        if any(sub in lower_name for sub in substrs):
            return category, rules
    return None, None

def get_category_by_extension(name, config):
    ext = Path(name).suffix.lower()
    for category, rules in config.items():
        exts = rules.get("extensions", [])
        if ext in exts:
            return category, rules
    return None, None

def move_item(item: Path, config):
    if not item.exists():
        return
    category, rules = get_category_by_name(item.name, config)
    if not category and item.is_file():
        category, rules = get_category_by_extension(item.name, config)

    if category:
        dest_dir = Path.home() / rules["target_path"]
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / item.name
        print(f"Moving: {item} -> {dest}")
        shutil.move(str(item), str(dest))
    else:
        print(f"No category for: {item.name}")

class DownloadHandler(FileSystemEventHandler):
    def __init__(self, config):
        self.config = config

    def on_created(self, event):
        path = Path(event.src_path)
        # Wait briefly in case file is still being written
        time.sleep(1)
        move_item(path, self.config)

def main():
    config = load_config()
    downloads_dir = Path.home() / "Downloads"

    event_handler = DownloadHandler(config)
    observer = Observer()
    observer.schedule(event_handler, str(downloads_dir), recursive=False)
    observer.start()
    print(f"Watching {downloads_dir} for new files...")

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
