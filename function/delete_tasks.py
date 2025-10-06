import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.manipulate_task_data import load_tasks, save_tasks


def delete_tasks():
    tasks = load_tasks()

    id = input('What is the task ID: ')
    if id is None:
        print('ID cannot be null')
        return

    if not isinstance(id, str):
        print('The ID must be of type string.')
        return

    if id not in tasks:
        print('ID not found in the task list')
        return

    del tasks[id]
    save_tasks(tasks)
    print('TASK was successfully removed')
