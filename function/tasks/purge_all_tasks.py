import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.manipulate_task_data import save_tasks


def purge_all_tasks():
    certainty = str(input('Are you sure you want to remove all tasks (yes/y/no/n)? ')).lower()
    while certainty not in ['y', 'yes', 'n', 'no']:
        print('The answer must be yes or no')
        certainty =  str(input('Are you sure you want to remove all tasks (yes/y/no/n)? ')).lower()

    if certainty == 'n' or certainty == 'no':
        print('You have cancelled the removal of all tasks. Nothing will be removed.')
        return

    new_tasks = {}

    save_tasks(new_tasks)
    print('All tasks have been removed.')
