import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.manipulate_task_data import load_tasks


def lists_all_tasks():
    tasks = load_tasks()

    for id_tasks, tasks_info in tasks.items():
        print(f'\nTask: {id_tasks}')
        for key, value in tasks_info.items():
            print(f'{key.capitalize()}: {value}')

    print('-' * 30)
