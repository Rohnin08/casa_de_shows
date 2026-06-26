import functions.storage as storage
import functions.geral as g
from time import sleep
from functions.geral import limpar_tela


# ──────────────────────────────────────────────
# INICIALIZAÇÃO
# ──────────────────────────────────────────────

clientes = storage.carregar('clientes')

if not clientes:
    clientes = {
        1:  {'nome': 'João Pedro',       'email': 'joao.pedro.2003@email.com',  'historico_compras': [1],  'cadastrado': True},
        2:  {'nome': 'Maria Eduarda',    'email': 'madu2005@email.com',  'historico_compras': [2],  'cadastrado': True},
        3:  {'nome': 'Carlos Henrique',  'email': 'carloshenrique@email.com',  'historico_compras': [3],  'cadastrado': True},
        4:  {'nome': 'Ana Clara',        'email': 'clarinha2004@email.com',  'historico_compras': [4],  'cadastrado': True},
        5:  {'nome': 'Felipe Santos',    'email': 'santosfelipe1@email.com',  'historico_compras': [5],  'cadastrado': True},
        6:  {'nome': 'Juliana Lima',     'email': 'limajuliana00@email.com',  'historico_compras': [6],  'cadastrado': True},
        7:  {'nome': 'Rafael Souza',     'email': 'souzafael06@email.com',  'historico_compras': [7],  'cadastrado': True},
        8:  {'nome': 'Beatriz Oliveira', 'email': 'beatriz.oli2002@email.com',  'historico_compras': [8],  'cadastrado': True},
        9:  {'nome': 'Gustavo Almeida',  'email': 'gustavoalmeida2001@email.com',  'historico_compras': [9],  'cadastrado': True},
        10: {'nome': 'Camila Ferreira',  'email': 'camiferreira22@email.com',  'historico_compras': [10], 'cadastrado': True},
    }
    storage.salvar("clientes", clientes)


# ──────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────

def exibir_cliente(id_cli, dados):
    email = dados.get('email', '')
    print(f"\nID: {id_cli}")
    print(f"Nome: {dados['nome']}")
    if email:
        print(f"Email: {email}")
    print(f"Histórico de compras: {dados['historico_compras']}\n")

# Validar Email
def validar_email(email, permitir_vazio=False):
    '''Função simples de valização de Email'''
    if not email.strip(): # Verifica se o email não está vazio
        return permitir_vazio
    
    if '@' not in email: # Verifica se o email tem '@'
        return False
    
    if email.count('@') != 1:
        return False
    
    elif email.startswith(('.', '@')) or email.endswith(('.', '@')): # Verifica se o email começa com '.', '@'  ou termina com esses caracteres.
        return False
    
    if not '.' in email:
        return False
    
    else: 
        return True

# ──────────────────────────────────────────────
# CRUD
# ──────────────────────────────────────────────

def cadastrar_cliente():
    print("\n=== CADASTRAR CLIENTE ===")
    nome = input("Nome do Cliente: ")

    while True:
        email = input("Digite o email do cliente: ")
        if not validar_email(email):
            print("⚠️ Email inválido, tente novamente.")
        else:
            print("✅ Email validado com sucesso!")
            break

    novo_id = g.gerar_id(clientes)

    clientes[novo_id] = {
        'nome': nome,
        'email': email,
        'cadastrado': True,
        'historico_compras': []
    }
    storage.salvar("clientes", clientes)
    print(f"\n✅ Cliente '{nome}' cadastrado com sucesso! (ID: {novo_id})")
    input("Continuar...")



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
            print("⚠️ Valor inválido, por favor tente novamente.")
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
            print("\n=== LISTA DE CLIENTES ===")
            encontrados = False
            for id_cli, dados in clientes.items():
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
                    print(f"\nHistórico de compras de '{clientes[id_cli]['nome']}':")
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
    print("\n=== EDITAR CLIENTE ===")

    while True:
        try:
            id_cli = int(input("ID do cliente que deseja editar: "))
            break
        except ValueError:
            print("⚠️ ID inválido, tente novamente.")

    if id_cli not in clientes or not clientes[id_cli]['cadastrado']:
        print("❌ Cliente não encontrado.")
        return

    atual = clientes[id_cli]
    email_atual = atual.get('email', '')

    print(f"Editando: {atual['nome']}")
    print("(Deixe em branco para manter o valor atual)\n")

    novo_nome  = input(f"Novo nome [{atual['nome']}]: ").strip()
    novo_email = input(f"Novo email [{email_atual}]: ").strip()

    while True:
        if not validar_email(novo_email, permitir_vazio=True):
            print("⚠️ Email inválido, tente novamente.")
            novo_email = input(f"Novo email [{email_atual}]: ").strip()
        else:
            if novo_email:
                print("✅ Email validado com sucesso!")
            break

    clientes[id_cli] = {
        'nome':              novo_nome  if novo_nome  else atual['nome'],
        'email':             novo_email if novo_email else email_atual,
        'cadastrado':        True,
        'historico_compras': atual['historico_compras']
    }
    storage.salvar("clientes", clientes)
    print("✅ Cliente atualizado com sucesso!")


def excluir_cliente():
    '''Permite excluir um cliente pelo ID com confirmação'''
    print("\n=== EXCLUIR CLIENTE ===")

    while True:
        try:
            id_cli = int(input("ID do cliente que deseja excluir: ")) 
            break
        except ValueError:
            print("⚠️ ID inválido, tente novamente.")

    if id_cli not in clientes or not clientes[id_cli]['cadastrado']:
        print("❌ Cliente não encontrado.")
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


# ──────────────────────────────────────────────
# MENU
# ──────────────────────────────────────────────

def menu_clientes():
    while True:
        print('''
=========================================
        Módulo de Clientes 🧑
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
            print("⚠️ Valor inválido, por favor tente novamente.")
            continue

        if opcao == 1:
            limpar_tela()
            cadastrar_cliente()

        elif opcao == 2:
            limpar_tela()
            buscar_cliente()

        elif opcao == 3:
            limpar_tela()
            editar_cliente()

        elif opcao == 4:
            limpar_tela()
            excluir_cliente()

        elif opcao == 0:
            print("Saindo do módulo...")
            sleep(1)
            break

        else:
            print("✋👺🚫 Opção inválida!")


if __name__ == "__main__":
    menu_clientes()