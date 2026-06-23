from time import sleep
import modulos.storage as storage
import modulos.shows as shows
import modulos.artistas as artistas
import modulos.geral as g

# ──────────────────────────────────────────────
# INICIALIZAÇÃO
# ──────────────────────────────────────────────

bilheteria = storage.carregar("bilheteria")
vendas = storage.carregar("vendas")

if not vendas:
    vendas = {

    }
    storage.salvar("vendas", vendas)

# Cadastrar Venda
def cadastrar_venda():
    pass

def cadastrar_venda():
    pass

def cadastrar_venda():
    pass

def cadastrar_venda():
    pass


def menu_vendas():
     while True:

        print('''
=========================================
          Vendas 💰
=========================================
    1. Cadastrar Vendas
              
    2. Listar/Buscar Vendas
              
    3. Editar Vendas
              
    4. Excluir Vendas
              
    0. Sair do Modulo
=========================================
''')
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Valor invalido, por favor tente novamente")
            continue

        if opcao == 1:
            cadastrar_venda()
        elif opcao == 2:
            buscar_venda()
        elif opcao == 3:
            editar_venda()
        elif opcao == 4:
            cancelar_venda()
        elif opcao == 0:
            print("Saindo...")
            sleep(1)
            break



# ──────────────────────────────────────────────
# MENU PRINCIPAL DO MÓDULO
# ──────────────────────────────────────────────
