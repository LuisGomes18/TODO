import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from menus.main_menu import main_menu


if __name__ == '__main__':
    main_menu()
