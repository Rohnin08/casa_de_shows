import pickle
import os

PASTA = "dados"

def salvar(nome_arquivo, dados):
    os.makedirs(PASTA, exist_ok=True)
    with open(f"{PASTA}/{nome_arquivo}.pkl", "wb") as f:
        pickle.dump(dados, f)

def carregar(nome_arquivo):
    caminho = f"{PASTA}/{nome_arquivo}.pkl"
    if not os.path.exists(caminho):
        return {}
    with open(caminho, "rb") as f:
        return pickle.load(f)