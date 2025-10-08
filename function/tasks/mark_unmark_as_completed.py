import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.manipulate_task_data import load_tasks, save_tasks


def mark_all_tasks_as_complete():
    tasks = load_tasks()
    if tasks is None:
        print('There are no tasks in the task list.')
        return

    for task_id, task_values in tasks.items():
        task_values['status'] = 'completed'

    save_tasks(tasks)
    print('All tasks marked as complete')


def unmark_all_tasks_as_complete():
    tasks = load_tasks()
    if tasks is None:
        print('There are no tasks in the task list.')
        return

    for task_id, task_values in tasks.items():
        task_values['status'] = 'pending'

    save_tasks(tasks)
    print('All tasks unmark as complete')
