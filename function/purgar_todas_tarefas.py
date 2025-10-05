import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.carregar_data import salvar_tarefas


def purgar_tarefas():
    certeza = str(input('Voce tem a certeza que quer remover todas as tarefas (sim/s/nao/n)? ')).lower()
    while certeza not in ['s', 'sim', 'n', 'nao']:
        print('A resposta deve ser s ou n ')
        certeza =  str(input('Voce tem a certeza que quer remover todas as tarefas (sim/s/nao/n)? ')).lower()

    if certeza == 'n' or certeza == 'nao':
        print('Voce cancelou as tarefas nao serao removidos')
        return

    novas_tarefas = {}

    salvar_tarefas(novas_tarefas)
    print('Tarefas foram todas removidas')
