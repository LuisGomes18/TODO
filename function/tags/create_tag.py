import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from utils.manipulate_task_tags import load_tags, save_tags
from utils.create_id import create_unique_id
from datetime import datetime
import re


def create_tags():
    tags = load_tags()
    regex_priority = r'^(-100|-?[1-9]?[0-9]|100)$'
    lines = []

    id = create_unique_id()
    date = datetime.now()

    tag_name = str(input('Enter the name of the new tag: '))
    while tag_name is None:
        tag_name = str(input('Enter the name of the new tag: '))

    description = str(input('Enter the description of the new tag: '))
    while description is None:
        description = str(input('Enter the description of the new tag: '))

    priority = int(input('Enter the priority of the new tag: '))
    check_is_digit = re.fullmatch(regex_priority, str(priority))
    while priority is None or not check_is_digit:
        priority = int(input('Enter the priority of the new tag: '))
        check_is_digit = re.fullmatch(regex_priority, str(priority))

    print('Enter the note of the new tag (END to stop):')
    while True:
        line = str(input())
        if line.strip() == '':
            pass
        if line.strip().upper() == 'END':
            break
        lines.append(line)

    note = '\n'.join(lines)

    tag_info = {
        f'{str(id)}': {
            'id': id,
            'name': tag_name,
            'description': description,
            'uses': 0,
            'create_timestamp': str(date),
            'last_id_task_use': 0,
            'last_timestamp': None,
            'is_active': True,
            'priority': priority,
            'notes': note
        }
    }

    tags.update(tag_info)
    save_tags(tags)

    print(f'Tag {tag_name} created successfully!')
