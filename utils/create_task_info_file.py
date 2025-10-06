import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.settings import BASE_DIR

import json


def create_task_info_file() -> None:
    file_path = os.path.join(BASE_DIR, 'data', 'task.json')
    data = {}

    if os.path.exists(file_path):
        print('File is already ignoring')
        return

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            print('Task information file does not exist. Creating file...')
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f'Error saving task data: {e}')
        exit(1)
