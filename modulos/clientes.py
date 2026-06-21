from modulos.artistas import gerar_id
import modulos.storage as storage
import modulos.geral as g
from time import sleep

# ──────────────────────────────────────────────
# INICIALIZAÇÃO
# ──────────────────────────────────────────────

clientes = storage.carregar('clientes')

if not clientes:
    clientes = {}

    storage.salvar("clientes", clientes)

############
def exibir_cliente(id_cli, dados):
    print(f"ID: {id_cli}\nNome: {dados['nome']}\nHistórico de compras: {dados['historico_compras']}")

# ──────────────────────────────────────────────
# CRUD
# ──────────────────────────────────────────────

# Cadastro de CLIENTES
def cadastrar_cliente():
    print("\n --- CADASTRAR CLIENTE")
    nome = str(input("Nome do Cliente: "))

    novo_id = g.gerar_id(clientes)

    clientes[novo_id] = {
        'nome': nome,
        'status_cliente':True,
        'historico_compras': []
        }
    
    storage.salvar("clientes", clientes)
    print(f"\nCliente: {nome} cadastrado com sucessso! (ID: {novo_id})")


# Busca de CLIENTES
def buscar_cliente():
    while True: 
        print('''
=========================================
         Buscador de Clientes
=========================================
  1. Buscar por ID
  2. Buscar por Nome
  3. Buscar histórico de vendas
  0. Voltar
=========================================''')
        
        try:
            opcao = int(input("Escolha uma opcão: "))
        except ValueError:
            print("Valor Invalido, por favor tente novamente")
            continue
        
        if opcao == 1:
            id_cli = int(input("ID do cliente: "))
            if id_cli in clientes:
                exibir_cliente(id_cli, clientes[id_cli])
            else:
                print("❌Cliente não encontrado.")
        
        elif opcao == 2:
            termo = input("Nome (Ou parte dele:): ").lower().strip()
            resultado = []
            for id_cli, dados in clientes.items():
                if termo in dados ['nome'].lower():
                    resultado.append((id_cli, dados))
            if resultado:
                for id_cli, dados in resultado:
                    exibir_cliente(id_cli, dados)
            else:
                print("❌Nenhum cliente encontrado com este nome.")
        
        elif opcao == 3:
            pass

        elif opcao == 0:
            print("Saindo...")
            sleep(1)
            break

def listar_clientes():
    pass

def editar_cliente():
    '''Busca o artista do ID e fornece para ele o um 'menu' para adicionar as novas informações do cliente associado aquele ID'''
    print("\n--- EDITAR CLIENTE ---")
    id_cli = int(input("ID do cliente que deseja editar: "))

    if id_cli not in clientes:
        print("❌ Cliente não encontrado.")
        return

    atual = clientes[id_cli]
    print(f"Editando: {atual['nome']}")
    print("(Deixe em branco para manter o valor atual)\n")

    nome      = input(f"Novo nome [{atual['nome']}]: ").strip()

    if nome:
        novo_nome = nome
    else:
        atual['nome']
        
    clientes[id_cli] = {'nome': novo_nome}
    storage.salvar("clientes", clientes)
    print("✅ Cliente atualizado com sucesso!")


def excluir_cliente():
    pass
    

def menu_clientes():
    while True:
        print('''
=========================================
          Módulo de Artistas
=========================================
  1. Cadastrar Cliente
  2. Buscar Cliente
  3. Editar Cliente
  4. Desabilitar Cliente
  0. Sair do Módulo
=========================================''')
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("❌Valor invalido, por favor tente novamente")
            continue

        if opcao == 1:
            cadastrar_cliente()
        elif opcao == 2:
            pass
        elif opcao == 3:
            buscar_cliente()
        elif opcao == 4:
            editar_cliente()
        elif opcao == 5:
            excluir_cliente()
        elif opcao == 0:
            print("Saindo do módulo...")
            sleep(1)
            break
        else:
            print("✋👺🚫 Opção inválida!")

if __name__ == "__main__":
    menu_clientes()