from modulos.artistas import gerar_id
import modulos.storage as storage
import modulos.geral as g

# ──────────────────────────────────────────────
# INICIALIZAÇÃO
# ──────────────────────────────────────────────

clientes = storage.carregar('clientes')

if not clientes:
    clientes = {}

    storage.salvar("clientes", clientes)

############
def exibir_cliente(id_cli, dados):
    print(f"  ID: {id_cli} | Nome: {dados['nome']} | CPF: R${dados['cpf']:.2f} | Telefone: {dados['telefone']}")    

# ──────────────────────────────────────────────
# CRUD
# ──────────────────────────────────────────────

def cadastrar_cliente():
    print("\n --- CADASTRAR CLIENTE")
    nome = str(input("Nome do Cliente: "))
    cpf = str(input("CPF do Cliente: "))
    telefone = str(input("Telefone do Cliente: "))

    novo_id = g.gerar_id(clientes)

    clientes[novo_id] = {
        'nome': nome,
        'cpf': cpf,
        'telefone':telefone,
        'historico_compras': []
        }
    storage.salvar("clientes", clientes)
    print(f"\nCliente: {nome} cadastrado com sucessso! (ID: {novo_id})")

def buscar_cliente():
    while True: 
        print('''
=========================================
         Buscador de Clientes
=========================================
  1. Buscar por ID
  2. Buscar por Nome
  3. Buscar por CPF
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
            for i, d in clientes.items():
                if termo in d ['nome'].lower():
                    resultado.append((i, d))
            if resultado:
                for id_cli, dados in resultado:
                    exibir_cliente(id_cli, dados)
                else:
                    print("❌Nenhum cliente encontrado com este nome.")

        elif opcao == 3:
            genero_busca = input("Gênero musical: ").lower()
            resultado = []
            for i, d in clientes.items():
                if genero_busca == d['genero'].lower():
                    resultado.append((i, d))
            if resultado:
                for id_art, dados in resultado:
                    exibir_cliente(id_art, dados)
            else:
                print("❌ Nenhum Cliente encontrado neste CPF.")




def listar_clientes():
    pass

def editar_clientes():
    pass

def excluir_clientes():
    pass

