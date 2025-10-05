import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.carregar_data import carregar_tarefas, salvar_tarefas
from utils.criar_id import criar_id_unico

from datetime import datetime


def criar_tarefas():
    tarefas = carregar_tarefas()
    linhas = []

    id = criar_id_unico()

    titulo = str(input('Qual o titulo da tarefa: '))
    print('Qual a descricao da tarefa (FIMM para parar)')
    while True:
        linha = input()
        if linha.strip().upper() == 'FIM':
            break
        linhas.append(linha)

    data = datetime.now().strftime('%Y-%m-%d %H:%M')

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

    nova_tarefa = {
        f'{str(id)}': {
            'id': id,
            'titulo': titulo,
            'descricao': descricao,
            'data': data,
            'data_limite': data_limite,
            'status': status,
            'prioridade': prioridade
        }
    }

    tarefas.update(nova_tarefa)
    salvar_tarefas(tarefas)

    print(f'\nTarefa foi criada com o id: {id}\n')
