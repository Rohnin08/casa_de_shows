from time import sleep
import functions.storage as storage
import functions.geral as g
from functions.geral import limpar_tela

# ──────────────────────────────────────────────
# INICIALIZAÇÃO
# ──────────────────────────────────────────────

artistas = storage.carregar("artistas")

if not artistas:
    artistas = {
    1: {'nome': 'Aurora Rock', 'cache': 8500.00, 'genero': 'Rock', 'cadastrado': True},
    2: {'nome': 'Banda Eclipse', 'cache': 7200.00, 'genero': 'Rock', 'cadastrado': True},
    3: {'nome': 'DJ Pulse', 'cache': 6000.00, 'genero': 'Eletrônica', 'cadastrado': True},
    4: {'nome': 'Marina Costa', 'cache': 9500.00, 'genero': 'Pop', 'cadastrado': True},
    5: {'nome': 'Os Sertanejos', 'cache': 11000.00, 'genero': 'Sertanejo', 'cadastrado': True},
    6: {'nome': 'Grupo Raiz', 'cache': 5000.00, 'genero': 'Forró', 'cadastrado': True},
    7: {'nome': 'Lucas Vieira', 'cache': 6700.00, 'genero': 'MPB', 'cadastrado': True},
    8: {'nome': 'Metal Storm', 'cache': 9800.00, 'genero': 'Metal', 'cadastrado': True},
    9: {'nome': 'Jazz Experience', 'cache': 7800.00, 'genero': 'Jazz', 'cadastrado': True},
    10: {'nome': 'Pagode Livre', 'cache': 6900.00, 'genero': 'Pagode', 'cadastrado': True}
}
    storage.salvar("artistas", artistas)

# ──────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────

def exibir_artista(id_art, dados):
    print(f"  ID: {id_art} | Nome: {dados['nome']} | Cache: R${dados['cache']:.2f} | Gênero: {dados['genero']}")

# ──────────────────────────────────────────────
# CRUD
# ──────────────────────────────────────────────

def cadastrar_artista(): 
    print("\n--- CADASTRAR ARTISTA ---")
    while True:
        try:
            nome = input("Nome do artista: ")
            cache = float(input("Cache do artista: R$ "))
            genero = input("Gênero musical: ")
            break
        except ValueError:
            print("Valor invalido em um dos campos, por favor tente novamente")

    novo_id = g.gerar_id(artistas)
    
    artistas[novo_id] = {
        'nome': nome,
        'cache': cache,
        'genero': genero,
        'cadastrado':True
        }
    
    storage.salvar("artistas", artistas)
    print(f"\n✅ {nome} cadastrado com sucesso! (ID: {novo_id})")

def exibir_todos():
    if not artistas:
        print("\n⚠️  Nenhum artista cadastrado.")
        return
    print("\n--- LISTA DE ARTISTAS ---")
    for id_art, dados in artistas.items():
        if artistas[id_art]['cadastrado']:
            exibir_artista(id_art, dados)
    input("\nContinuar...")

def buscar_artistas():
    while True:
        print('''
=========================================
        Buscador de Artistas 👨‍🎤
=========================================
  1. Buscar por ID
              
  2. Buscar por Nome
              
  3. Buscar por Gênero
              
  4. Buscar por Cache (até um valor)
              
  0. Voltar
=========================================''')

        try:
            opcao = int(input("Qual a opção? "))

        except ValueError:
            print("❌Valor invalido, por favor tente novamente")
            continue

        if opcao == 1:
            while True:
                try:
                    id_art = int(input("ID do artista: "))
                    break
                except ValueError:
                    print("⚠️ Valor invalido, tente novamente")

            if id_art in artistas and artistas[id_art]['cadastrado']:
                exibir_artista(id_art, artistas[id_art])

            else:
                print("❌ Artista não encontrado.")

        elif opcao == 2:
            termo = input("Nome (ou parte dele): ").lower().strip()
            resultado = []

            for id_art, dados in artistas.items():
                if termo in dados['nome'].lower() and dados['cadastrado']:
                    resultado.append((id_art, dados))

            if resultado:
                for id_art, dados in resultado:
                    exibir_artista(id_art, dados) 

            else:
                print("❌ Nenhum artista encontrado com este nome.")

        elif opcao == 3:
            termo = input("Gênero musical: ").lower()

            resultado = [] #Lista para armazenar o que ele achar com aquela informação

            for id_art, dados in artistas.items():
                if termo in dados['genero'].lower() and artistas[id_art]['cadastrado']: # verifica se existe o genero e se o artista que tem aquele género está ativo.
                    resultado.append((id_art, dados)) #Adiciona ao final da lista tudo que ele for achando

            if resultado:
                for id_art, dados in resultado:
                    exibir_artista(id_art, dados)

            else:
                print("❌ Nenhum artista encontrado neste gênero.")

        elif opcao == 4:
            cache_limite = float(input("Exibir artistas com cache até: R$ "))

            resultado = []

            for id_art, dados in artistas.items():
                if dados['cache'] <= cache_limite and artistas[id_art]['cadastrado']:
                    resultado.append((id_art, dados))

            if resultado:
                for id_art, dados in resultado:
                    exibir_artista(id_art, dados)

            else:
                print("❌ Nenhum artista encontrado nessa faixa de cache.")

        elif opcao == 0:
            print("Saindo...")
            break

        else:
            print("⚠️ Opção inválida.")

        input("\nPressione Enter para continuar...")

def editar_artista():
    '''Busca o artista do ID e fornece para ele o um 'menu' para adicionar as novas informações do artistas associado aquele ID'''
    print("\n--- EDITAR ARTISTA ---")

    while True:
        try: 
            id_art = int(input("ID do artista que deseja editar: "))
            break
        except ValueError:
            print("⚠️ Valor invalido, tente novamente")
            

    if id_art not in artistas or not artistas[id_art]['cadastrado']: # Verifica se existe algum id igual ao digitado ou se ele não está ativo 
        print("❌ Artista não encontrado.")
        return

    atual = artistas[id_art]
    print(f"Editando: {atual['nome']} | Cache: R${atual['cache']:.2f} | Gênero: {atual['genero']}")
    print("(Deixe em branco para manter o valor atual)\n")

    novo_nome = input(f"Novo nome [{atual['nome']}]: ").strip()
    novo_cache_str = input(f"Novo cache [{atual['cache']:.2f}]: ").strip()
    novo_genero = input(f"Novo gênero [{atual['genero']}]: ").strip()
    
    if novo_nome:
        nome = novo_nome
    else:
        nome = atual['nome']
        
    if novo_cache_str:
        try:
            cache = float(novo_cache_str)
        except ValueError:
            print("Valor invalido para cache")
            return
    else: 
        cache = atual['cache']
        
    if novo_genero:
        genero = novo_genero
    else:
        genero = atual['genero']

    artistas[id_art] = {
        'nome': nome,
        'cache': cache,
        'genero': genero,
        'cadastrado': True
        }
    storage.salvar("artistas", artistas)
    print("✅ Artista atualizado com sucesso!")

def excluir_artista():
    '''Permite o usuário buscar o artista por meio do 'ID' com o objetivo de excluir. Ele tem um validador simples afim de evitar que o usuário apague sem querer'''
    print("\n--- EXCLUIR ARTISTA ---")

    while True:
        try:
            id_art = int(input("ID do artista que deseja excluir: "))
            break
        except ValueError:
            print("⚠️ Valor invalido, tente novamente")


    if id_art not in artistas or not artistas[id_art]['cadastrado']:
        print("❌ Artista não encontrado.")
        return

    confirmar = input(f"Tem certeza que quer excluir '{artistas[id_art]['nome']}'? (sim/não): ").lower()
    if confirmar == "sim":
        print("Excluindo...")
        sleep(1)
        artistas[id_art]['cadastrado'] = False
        storage.salvar("artistas", artistas)
        print("✅ Artista Excluido com sucesso!")
    else:
        print("Operação cancelada.")

# ──────────────────────────────────────────────
# MENU PRINCIPAL DO MÓDULO
# ──────────────────────────────────────────────

def menu_artistas():
    while True:
        print('''
=========================================
          Módulo de Artistas
=========================================
  1. Cadastrar Artista
              
  2. Exibir Todos
              
  3. Buscar Artista
              
  4. Editar Artista
              
  5. Excluir Artista
              
  0. Sair do Módulo
=========================================''')
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("❌Valor invalido, por favor tente novamente")
            continue

        if opcao == 1:
            limpar_tela()
            cadastrar_artista()
            limpar_tela()
        elif opcao == 2:
            limpar_tela()
            exibir_todos()
        elif opcao == 3:
            limpar_tela()
            buscar_artistas()
        elif opcao == 4:
            limpar_tela
            editar_artista()
        elif opcao == 5:
            limpar_tela()
            excluir_artista()
        elif opcao == 0:
            limpar_tela()
            print("Saindo do módulo...")
            sleep(0.5)
            break
        else:
            print("✋👺🚫 Opção inválida!")

if __name__ == "__main__":
    menu_artistas()