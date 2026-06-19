import pickle
import os

PASTA = "dados"

def salvar(nome_arquivo, dados):
    try:
        with open(f"{PASTA}/{nome_arquivo}.dat", "wb") as file:
            pickle.dump(dados, file)
    except FileNotFoundError:
        os.makedirs(PASTA)
        with open(f"{PASTA}/{nome_arquivo}.dat", "wb") as file:
            pickle.dump(dados, file)

def carregar(nome_arquivo):
    caminho = f"{PASTA}/{nome_arquivo}.dat"
    try:
        with open(caminho, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}
    

