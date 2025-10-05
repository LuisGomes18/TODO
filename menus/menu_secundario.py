import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from function.purgar_todas_tarefas import purgar_tarefas


def menu_segundario():
    while True:
        escolha = str(input('''
1) Espurgar toda os dados
99) Menu principal
0) Sair
-> '''))
        while escolha not in [
            '1', '99', '0'
            ]:
            escolha = str(input('''
1) Espurgar toda os dados
99) Menu principal
0) Sair
-> '''))

        if escolha == '1':
            purgar_tarefas()
        elif escolha == '99':
            break
        elif escolha == '0':
            exit(0)
