import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.carregar_data import carregar_tarefas


def ver_tarefa_id():
    tarefas = carregar_tarefas()
    id = str(input('Qual o id da tarefa: '))
    if id is None:
        print('Id nao pode ser nula')
        return

    if id not in tarefas:
        print('Id nao foi achado')
        return

    if not isinstance(id, str):
        print('O id deve ser do tipo string')
        return

    tarefa = tarefas[id]
    print(tarefa)
