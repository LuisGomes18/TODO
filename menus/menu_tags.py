import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from function.tags.create_tag import create_tags
from function.tags.list_all_tags import list_all_tags
from function.tags.update_tag import update_tag
from function.tags.delete_tag import delete_tags
from menus.main_menu import main_menu


def menu_tags():
    movimentos_escolhidos = ['1', '2', '3', '4', '99', '0']

    while True:
        escolha = str(input('''
1 - Criar a tag
2 - Listar todas as tags
3 - Atualizar a tag
4 - Deletar a tag
99 - Voltar menu secundario
0 - Sair
-> '''))

        while escolha not in movimentos_escolhidos:
            escolha = str(input('''
1 - Criar a tag
2 - Listar todas as tags
3 - Atualizar a tag
4 - Deletar a tag
99 - Voltar menu secundario
0 - Sair
-> '''))

        if escolha == '1':
            create_tags()
        elif escolha == '2':
            list_all_tags()
        elif escolha == '3':
            update_tag()
        elif escolha == '4':
            delete_tags()
        elif escolha == '99':
            return main_menu()
        elif escolha == '0':
            print('Saindo...')
            exit()
