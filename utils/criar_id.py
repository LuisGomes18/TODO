import uuid


def criar_id_unico(caracteres : int=None) -> str:
    if caracteres is None:
        caracteres = 18

    if not isinstance(caracteres, int):
        caracteres = 18

    id_uuid = str(uuid.uuid4())
    id_formatado_sem_simbolos = id_uuid.replace('-', '')
    id_final = id_formatado_sem_simbolos[:caracteres]

    return id_final
