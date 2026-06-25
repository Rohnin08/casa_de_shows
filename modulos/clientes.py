import modulos.storage as storage
import modulos.geral as g
from time import sleep
from modulos.geral import limpar_tela


# ──────────────────────────────────────────────
# INICIALIZAÇÃO
# ──────────────────────────────────────────────

clientes = storage.carregar('clientes')

if not clientes:
    clientes = {}
    storage.salvar("clientes", clientes)

# ──────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────

def exibir_cliente(id_cli, dados):
    print(f"\nID: {id_cli}\nNome: {dados['nome']}\nHistórico de compras: {dados['historico_compras']}\n")

# ──────────────────────────────────────────────
# CRUD
# ──────────────────────────────────────────────

# Cadastro de CLIENTES
def cadastrar_cliente():
    print("\n--- CADASTRAR CLIENTE ---")
    nome = input("Nome do Cliente: ")
    novo_id = g.gerar_id(clientes)

    clientes[novo_id] = {
        'nome': nome,
        'cadastrado': True,
        'historico_compras': []
    }
    storage.salvar("clientes", clientes)
    print(f"\n✅ Cliente '{nome}' cadastrado com sucesso! (ID: {novo_id})")


# Busca de CLIENTES
def buscar_cliente():
    while True:
        print('''
=========================================
         Buscador de Clientes
=========================================
  1. Buscar por ID
  2. Listar Todos
  3. Buscar por Nome
  4. Buscar histórico de compras
  0. Voltar
=========================================''')

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("⚠️ Valor inválido, por favor tente novamente")
            continue

        if opcao == 1:
            while True:
                try:
                    id_cli = int(input("ID do cliente: "))
                    break
                except ValueError:
                    print("⚠️ ID inválido, tente novamente.")

            if id_cli in clientes and clientes[id_cli]['cadastrado']:
                exibir_cliente(id_cli, clientes[id_cli])
            else:
                print("❌ Cliente não encontrado.")
            input("\nPressione Enter para continuar...")

        elif opcao == 2:
            print("\n--- LISTA DE CLIENTES ---")
            encontrados = False
            for id_cli, dados in clientes.items():  # ← corrigido: era clientes sem .items()
                if dados['cadastrado']:
                    exibir_cliente(id_cli, dados)
                    encontrados = True
            if not encontrados:
                print("❌ Nenhum cliente cadastrado.")
            input("\nPressione Enter para continuar...")

        elif opcao == 3:
            termo = input("Nome (ou parte dele): ").lower().strip()
            resultado = []
            for id_cli, dados in clientes.items():
                if termo in dados['nome'].lower() and dados['cadastrado']:
                    resultado.append((id_cli, dados))
            if resultado:
                for id_cli, dados in resultado:
                    exibir_cliente(id_cli, dados)
            else:
                print("❌ Nenhum cliente encontrado com este nome.")
            input("\nPressione Enter para continuar...")

        elif opcao == 4:
            while True:
                try:
                    id_cli = int(input("ID do cliente: "))
                    break
                except ValueError:
                    print("⚠️ ID inválido, tente novamente.")

            if id_cli in clientes and clientes[id_cli]['cadastrado']:
                historico = clientes[id_cli]['historico_compras']
                if historico:
                    print(f"\nHistórico de compras do cliente '{clientes[id_cli]['nome']}':")
                    for id_venda in historico:
                        print(f"  ID da venda: {id_venda}")
                else:
                    print("❌ Este cliente não possui compras registradas.")
            else:
                print("❌ Cliente não encontrado.")
            input("\nPressione Enter para continuar...")

        elif opcao == 0:
            print("Saindo...")
            sleep(1)
            break

        else:
            print("⚠️ Opção inválida.")


def editar_cliente():
    '''Busca o cliente pelo ID e permite atualizar o nome'''
    print("\n--- EDITAR CLIENTE ---")

    while True:
        try:
            id_cli = int(input("ID do cliente que deseja editar: "))
            break
        except ValueError:
            print("⚠️ ID inválido, tente novamente.")

    if id_cli not in clientes or not clientes[id_cli]['cadastrado']:  # ← corrigido: faltava checar 'cadastrado'
        print("❌ Cliente não encontrado.")
        return

    atual = clientes[id_cli]
    print(f"Editando: {atual['nome']}")
    print("(Deixe em branco para manter o valor atual)\n")

    novo_nome = input(f"Novo nome [{atual['nome']}]: ").strip()

    if novo_nome:
        nome = novo_nome
    else:
        nome = atual['nome']  # ← corrigido: faltava a atribuição

    clientes[id_cli] = {
        'nome': nome,
        'cadastrado': True,
        'historico_compras': atual['historico_compras']  # ← corrigido: preserva o histórico
    }
    storage.salvar("clientes", clientes)
    print("✅ Cliente atualizado com sucesso!")


def excluir_cliente():
    '''Permite excluir um cliente pelo ID com confirmação'''
    print("\n--- EXCLUIR CLIENTE ---")  # ← corrigido: dizia ARTISTA

    while True:
        try:
            id_cli = int(input("ID do cliente que deseja excluir: "))  # ← corrigido: dizia artista
            break
        except ValueError:
            print("⚠️ ID inválido, tente novamente.")

    if id_cli not in clientes or not clientes[id_cli]['cadastrado']:
        print("❌ Cliente não encontrado.")  # ← corrigido: dizia Artista
        return

    confirmar = input(f"Tem certeza que quer excluir '{clientes[id_cli]['nome']}'? (sim/não): ").lower()
    if confirmar == "sim":
        print("Excluindo...")
        sleep(1)
        clientes[id_cli]['cadastrado'] = False
        storage.salvar("clientes", clientes)
        print("✅ Cliente excluído com sucesso!")
    else:
        print("Operação cancelada.")


def menu_clientes():
    while True:
        print('''
=========================================
          Módulo de Clientes
=========================================
  1. Cadastrar Cliente
  2. Buscar Cliente
  3. Editar Cliente
  4. Excluir Cliente
  0. Sair do Módulo
=========================================''')
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("⚠️ Valor inválido, por favor tente novamente")
            continue

        if opcao == 1:
            cadastrar_cliente()
        elif opcao == 2:
            buscar_cliente()
        elif opcao == 3:
            editar_cliente()
        elif opcao == 4:
            excluir_cliente()
        elif opcao == 0:
            print("Saindo do módulo...")
            sleep(1)
            break
        else:
            print("✋👺🚫 Opção inválida!")

if __name__ == "__main__":
    menu_clientes()