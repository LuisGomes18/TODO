import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.manipulate_task_data import load_tasks, save_tasks
from utils.create_id import create_unique_id

from datetime import datetime


def create_tasks():
    tasks = load_tasks()
    lines = []

    id = create_unique_id()

    title = str(input('What is the title of the task: '))
    print('What is the description of the task (END to stop)?')
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)

    DATE = datetime.now().strftime('%Y-%m-%d %H:%M')

    priority = str(input('What is the priority of the task: ')).lower()
    while priority not in ['low', 'medium', 'high']:
        priority = str(input('What is the priority of the task: ')).lower()

    status = str(input('What is the status of the task: ')).lower()
    while status not in ['pending', 'in progress', 'completed', 'archived']:
        status = str(input('What is the status of the task: ')).lower()

    deadline = input('What is the deadline: (leave blank if you do not have one) ')
    if not deadline:
        deadline = None

    description = '\n'.join(lines)

    new_task = {
        f'{str(id)}': {
            'id': id,
            'title': title,
            'description': description,
            'date': DATE,
            'deadline': deadline,
            'status': status,
            'priority': priority
        }
    }

    tasks.update(new_task)
    save_tasks(tasks)

    print(f'\nTask was created with id: {id}\n')
