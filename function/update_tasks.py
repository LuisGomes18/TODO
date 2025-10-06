import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.manipulate_task_data import load_tasks, save_tasks


def update_tasks():
    tasks = load_tasks()
    choices_task = None
    lines = []

    id = str(input('What is the task id: '))
    if id is None:
        print('Id cannot be null')
        return

    if not isinstance(id, str):
        print('The id must be string type')
        return

    if id not in tasks:
        print('Id was not found')
        return

    choices_task = tasks[id]

    field_to_modify = str(input('''Which field you want to modify:
1 - Title
2 - Description
3 - Priority
4 - Status
0 - To go back
-> ''')).lower()

    if field_to_modify is None:
        print('The field cannot be null')
        return

    if field_to_modify not in ['1', '2', '3', '4', '0']:
        print('Inserted field invalid please put a valuable value')
        return

    if field_to_modify == '1':
        title = str(input('What is the title of the task: '))
        if title != choices_task['title']:
            choices_task['title'] = title
        tasks[id] = choices_task
        save_tasks(tasks)
        print('Successful modified task')
        return
    elif field_to_modify == '2':
        print('What is the description of the task (END to stop)')
        while True:
            line = input()
            if line.strip().upper() == 'END':
                break
            lines.append(line)

        description = '\n'.join(lines)
        if description != choices_task['description']:
            choices_task['description'] = description
        tasks[id] = choices_task
        save_tasks(tasks)
        print('Successful modified task')
        return
    elif field_to_modify == '3':
        priority = str(input('What is the priority of the task: ')).lower()
        while priority not in ['low', 'medium', 'high']:
            priority = str(input('What is the priority of the task: ')).lower()
        if priority != choices_task['priority']:
            choices_task['priority'] = priority
        tasks[id] = choices_task
        save_tasks(tasks)
        print('Successful modified task')
        return
    elif field_to_modify == '4':
        status = str(input('What is the status of the task: ')).lower()
        while status not in ['pending', 'in progress', 'concluded', 'archive']:
            status = str(input('What is the status of the task: ')).lower()
        if status != choices_task['status']:
            choices_task['status'] = status
        tasks[id] = choices_task
        save_tasks(tasks)
        print('Successful modified task')
        return
    elif field_to_modify == '0':
        return
