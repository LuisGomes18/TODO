import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.carregar_data import carregar_tarefas, salvar_tarefas


def update_tarefa():
    tarefas = carregar_tarefas()
    tarefa_original = None
    linhas = []

    id = str(input('Qual o id da tarefa: '))
    if id is None:
        print('Id nao pode ser nula')
        return

    if not isinstance(id, str):
        print('O id deve ser do tipo string')
        return

    if id not in tarefas:
        print('Id nao foi achado')
        return

    tarefa_original = tarefas[id]

    titulo = str(input('Qual o titulo da tarefa: '))
    print('Qual a descricao da tarefa (FIMM para parar)')
    while True:
        linha = input()
        if linha.strip().upper() == 'FIM':
            break
        linhas.append(linha)

    prioridade = str(input('Qual a prioridade da tarefa: ')).lower()
    while prioridade not in ['baixa', 'media', 'alta']:
        prioridade = str(input('Qual a prioridade da tarefa: ')).lower()

    status = str(input('Qual o status da tarefa: ')).lower()
    while status not in ['pendente', 'em progresso', 'concluida', 'arquivada']:
        status = str(input('Qual o status da tarefa: ')).lower()

    data_limite = input('Qual a data limite: (nada caso nao tenha) ')
    if not data_limite:
        data_limite = None

    descricao = '\n'.join(linhas)

    if titulo != tarefa_original['titulo']:
        tarefa_original['titulo'] = titulo

    if descricao != tarefa_original['descricao']:
        tarefa_original['descricao'] = descricao

    tarefas[id] = tarefa_original
    salvar_tarefas(tarefas)
