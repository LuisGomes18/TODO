import uuid


def create_unique_id(characters : int=None) -> str:
    if characters is None:
        characters = 18

    if not isinstance(characters, int):
        characters = 18

    id_uuid = str(uuid.uuid4())
    id_formatted_without_symbols = id_uuid.replace('-', '')
    final_id = id_formatted_without_symbols[:characters]

    return final_id
