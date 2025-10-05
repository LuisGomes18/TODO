import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from function.purge_all_tasks import purge_all_tasks


def secondary_menu():
    ACCEPTED_CHOICES = ['1', '99', '0']

    while True:
        choice = str(input('''
1) Purge all task data
99) Main menu
0) Exit
-> '''))
        while choice not in ACCEPTED_CHOICES:
            choice = str(input('''
1) Purge all task data
99) Main menu
0) Exit
-> '''))

        if choice == '1':
            purge_all_tasks()
        elif choice == '99':
            break
        elif choice == '0':
            exit(0)
