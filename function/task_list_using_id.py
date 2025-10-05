import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.manipulate_task_data import load_tasks


def task_list_using_id():
    tasks = load_tasks()

    id = str(input('What is the task ID: '))
    if id is None:
        print('The task ID cannot be null.')
        return

    if id not in tasks:
        print('The task with the ID I entered was not found. Please enter a valid ID.')
        return

    if not isinstance(id, str):
        print('The ID must be a string. Please enter a valid ID.')
        return

    task = tasks[id]
    print(task)
