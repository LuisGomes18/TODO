import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from utils.manipulate_task_tags import load_tags, save_tags


def delete_tags():
    tags = load_tags()

    id = str(input('What is the task ID: '))

    if id is None:
        print('ID cannot be null')
        return

    if id not in tags:
        print('ID not found in task list')
        return

    confirmed = str(input('Are you sure you want to delete this task? (Y/N): '))
    if confirmed.upper() != 'Y':
        print('Operation canceled')
        return

    del tags[id]
    save_tags(tags)
    print('Task deleted successfully!')
