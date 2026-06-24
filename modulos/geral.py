# Modulo para guardar funções gerais, aquelas que são usadas por todos.

def gerar_id(colecao: dict) -> int: 
    """Retorna um ID único mesmo após deleções."""
    if colecao: #Verifica se o arquivo genérico está vazio
        return max(colecao.keys()) + 1 # Se for True returna o maior id do dicionario e depois soma 1
    else:
        return 1 


