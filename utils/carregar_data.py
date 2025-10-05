import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.settings import BASE_DIR


def carregar_tarefas() -> dict:
    file_path = os.path.join(BASE_DIR, 'data', 'tarefas.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print('Erro: ficheiro JSON corrompido ou mal formatado.')
        return {}
    except FileNotFoundError:
        print('Aviso: ficheiro não encontrado, a iniciar com dicionário vazio.')
        return {}
    except Exception as e:
        print(f'Erro inesperado ao carregar: {e}')
        return {}


def salvar_tarefas(data: dict) -> None:
    file_path = os.path.join(BASE_DIR, 'data', 'tarefas.json')
    if data is None:
        print('Erro: Nenhum dado para salvar.')
        return
    if not isinstance(data, dict):
        print('Erro: os dados devem ser um dicionário.')
        return
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f'Erro ao salvar dados: {e}')
