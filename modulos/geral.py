# Modulo para guardar funções gerais, aquelas que são usadas por todos.

def gerar_id(colecao: dict) -> int:
    """Retorna um ID único mesmo após deleções."""
    if colecao: #Verifica se o arquivo está vazio
        return max(colecao.keys()) + 1 # Se for True returna o maior id do dicionario e depois
    else:
        return 1


