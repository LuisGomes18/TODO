import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.create_task_info_file import create_task_info_file
from menus.main_menu import main_menu


if __name__ == '__main__':
    try:
        create_task_info_file()
        main_menu()
    except InterruptedError:
        print('\nExiting the program. Goodbye!')
        exit(0)
    except Exception as error:
        print(f'Erro Inesperado: {error}')
        exit(1)
