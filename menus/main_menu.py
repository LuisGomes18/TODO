import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from function.create_tasks import create_tasks
from function.lists_all_tasks import lists_all_tasks
from function.task_list_using_id import task_list_using_id
from function.delete_tasks import delete_tasks
from menus.secondary_menu import secondary_menu


def main_menu():
    ACCEPTED_CHOICES = ['0', '1', '2', '3', '4', '9', '99']

    while True:
        choices = str(input('''
1 - Create tasks
2 - Lists all tasks
3 - Task list using id
4 - Delete tasks
99 - Submenu
0 - Exit
--> '''))
        while choices not in ACCEPTED_CHOICES:
            print('Invalid choices, please enter a valid value.')
            choices = str(input('''
1 - Create tasks
2 - Lists all tasks
3 - Task list using id
4 - Delete tasks
99 - Submenu
0 - Exit
--> '''))

        if choices == '1':
            create_tasks()
        elif choices == '2':
            lists_all_tasks()
        elif choices == '3':
            task_list_using_id()
        elif choices == '4':
            delete_tasks()
        elif choices == '99':
            secondary_menu()
        elif choices == '0':
            exit(0)
