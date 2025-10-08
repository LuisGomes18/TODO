import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from function.tasks.purge_all_tasks import purge_all_tasks
from function.tasks.mark_unmark_as_completed import mark_all_tasks_as_complete
from function.tasks.mark_unmark_as_completed import unmark_all_tasks_as_complete


def secondary_menu():
    ACCEPTED_CHOICES = ['1', '2', '3', '99', '0']

    while True:
        choice = str(input('''
1 - Purge all task data
2 - Mark all tasks as completed
3 - Unmark all tasks as completed
99 - Main menu
0 - Exit
-> '''))
        while choice not in ACCEPTED_CHOICES:
            choice = str(input('''
1 - Purge all task data
2 - Mark all tasks as completed
3 - Unmark all tasks as completed
99 - Main menu
0 - Exit
-> '''))

        if choice == '1':
            purge_all_tasks()
        elif choice == '2':
            mark_all_tasks_as_complete()
        elif choice == '3':
            unmark_all_tasks_as_complete()
        elif choice == '99':
            break
        elif choice == '0':
            exit(0)
