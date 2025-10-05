import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from menus.menu_principal import menu_principal


if __name__ == '__main__':
    menu_principal()
