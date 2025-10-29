import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.settings import BASE_DIR
import json


def load_tags() -> dict | None:
    file_path = os.path.join(BASE_DIR, 'data', 'tags.json')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print('Error: Json file corrupted or malformed.')
        return None
    except FileNotFoundError:
        print('Warning: file not found')
        return None
    except Exception as error:
        print(f'Unexpected error loading task: {error}')
        return None


def save_tags(data: dict) -> None:
    file_path = os.path.join(BASE_DIR, 'data', 'tags.json')

    if data is None:
        print('Error: tag data for saving tags cannot be null')
        return

    if not isinstance(data, dict):
        print('Error: data of tags to save tags must be a dictionary')
        return

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as error:
        print(f'Error saving tags: {error}')
        return
