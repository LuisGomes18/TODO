import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from utils.manipulate_task_tags import load_tags


def list_all_tags():
    tags = load_tags()

    if not tags:
        print('There are no tags in the tag list')
        return

    for id_tags, tags_info in tags.items():
        print('\n')
        for key, value in tags_info.items():
            print(f'{key.capitalize()}: {value}')
