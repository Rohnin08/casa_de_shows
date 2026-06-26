import os

def exibir_sobre():
    caminho = os.path.join(os.path.dirname(__file__))
    try:
        with open("README.md", 'r', encoding='utf-16') as f:
            print(f.read())
    except FileNotFoundError:
        print("❌ Arquivo não encontrado")
    input("\nPressione Enter para continuar...")