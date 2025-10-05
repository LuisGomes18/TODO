import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.settings import BASE_DIR


def load_tasks() -> dict | None:
    file_path = os.path.join(BASE_DIR, 'data', 'tarefas.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print('Error: JSON file corrupted or malformed.')
        return None
    except FileNotFoundError:
        print('Warning: file not found')
        return None
    except Exception as e:
        print(f'Unexpected error loading tasks: {e}')
        return None


def save_tasks(data: dict) -> None:
    file_path = os.path.join(BASE_DIR, 'data', 'tarefas.json')

    if data is None:
        print('Error: task data for saving tasks cannot be null')
        return
    if not isinstance(data, dict):
        print('Error: data of tasks to save tasks must be a dictionary')
        return

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f'Error saving task data: {e}')
