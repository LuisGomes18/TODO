import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from function.criar_tarefas import criar_tarefas
from function.ver_tarefas import ver_tarefas
from function.ver_tarefa_id import ver_tarefa_id
from function.deletar_tarefa import deletar_tarefa
from menus.menu_secundario import menu_segundario


def menu_principal():
    while True:
        escolha = str(input('''
1 - Adicionar tarefa
2 - Ver tarefas
3 - Ver tarefa (id)
4 - Remover tarefa
99 - Menu secundario
0 - Sair
--> '''))
        while escolha not in [
            '0', '1', '2', 
            '3', '4', '9',
            '99'
            ]:
            print('Escolha inválida. Tente novamente.')
            escolha = str(input('''
1 - Adicionar tarefa
2 - Ver tarefas
3 - Ver tarefa (id)
4 - Remover tarefa
9 - Definicoes
99 - Menu secundario
0 - Sair
--> '''))

        if escolha == '1':
            criar_tarefas()
        elif escolha == '2':
            ver_tarefas()
        elif escolha == '3':
            ver_tarefa_id()
        elif escolha == '4':
            deletar_tarefa()
        elif escolha == '99':
            menu_segundario()
        elif escolha == '0':
            exit(0)
