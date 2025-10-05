import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.carregar_data import carregar_tarefas


def ver_tarefas():
    tarefas = carregar_tarefas()

    for id_tarefa, tarefa in tarefas.items():
        print(f'\nTarefa: {id_tarefa}')
        for chave, valor in tarefa.items():
            print(f'{chave}: {valor}')

    print('-' * 30)
