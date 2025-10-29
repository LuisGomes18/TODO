import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from utils.manipulate_task_tags import load_tags, save_tags
import re


def update_tag():
    tags = load_tags()
    choice_tag = {}
    lines = []
    regex_priority = r'^(-100|-?[1-9]?[0-9]|100)$'

    id = str(input('What is the tag id: '))
    while id is None:
        print('ID cannot be null')
        id = str(input('What is the tag id: '))

    while id not in tags:
        print('The tag does not exist in the tag list')
        id = str(input('What is the tag id: '))

    choice_tag.update(tags.get(id))

    field_update = str(input('''
Which field do you want to modify:
1 - Name
2 - Description
3 - If it is active
4 - Priority
5 - Notes
-> '''))

    while field_update not in ['1', '2', '3', '4', '5']:
        field_update = str(input('''
Which field do you want to modify:
1 - Name
2 - Description
3 - If it is active
4 - Priority
5 - Notes
-> '''))

    if field_update == "1":
        name = str(input('What would be the name of the tag?: '))
        while name is None:
            name = str(input('What would be the name of the tag?: '))

        choice_tag['name']  = name
    elif field_update == "2":
        description = str(input('What would be the description of the tag?: '))
        while description is None:
            description = str(input('What would be the description of the tag?: '))

        choice_tag['description'] = description
    elif field_update == "3":
        active = str(input('Is the tag active (yes/y/no/n)? ')).lower()
        while active not in ['y', 'yes', 'n', 'no']:
            print('The answer must be yes or no')
            active = str(input('Is the tag active (yes/y/no/n)? ')).lower()

        if active == 'y' or active == 'yes':
            choice_tag['is_active'] = True
        else:
            choice_tag['is_active'] = False
    elif field_update == "4":
        priority = int(input('What would be the priority of the tag?: '))
        check_is_digit = re.fullmatch(regex_priority, str(priority))
        while priority is None or not check_is_digit:
            priority = int(input('What would be the priority of the tag?: '))
            check_is_digit = re.fullmatch(regex_priority, str(priority))

        choice_tag['priority'] = priority
    elif field_update == "5":
        print('Enter the note of the new tag (END to stop):')
        while True:
            line = str(input())
            if line.strip() == '':
                pass
            if line.strip().upper() == 'END':
                break
            lines.append(line)

        notes = '\n'.join(lines)

        choice_tag['notes'] = notes

    tags[id] = choice_tag
    save_tags(tags)
    print('Tag updated successfully!')
