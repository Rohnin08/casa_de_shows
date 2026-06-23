from time import sleep
import modulos.storage as storage
import modulos.geral as g

# ──────────────────────────────────────────────
# INICIALIZAÇÃO
# ──────────────────────────────────────────────

artistas = storage.carregar("artistas")

if not artistas:
    artistas = {
        1: {'nome': 'Slipknot',    'cache': 1000.00, 'genero': 'Metal', 'cadastrado':True},
        2: {'nome': 'Linkin Park', 'cache': 1500.00, 'genero': 'Nu Metal', 'cadastrado':True},
        3: {'nome': 'Limp Bizkit', 'cache': 1200.00, 'genero': 'Nu Metal', 'cadastrado':True}
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
    nome = input("Nome do artista: ")
    cache = float(input("Cache do artista: R$ "))
    genero = input("Gênero musical: ")

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
        exibir_artista(id_art, dados) 

def buscar_artistas():
    while True:
        print('''
=========================================
         Buscador de Artistas
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
            id_art = int(input("ID do artista: "))

            if id_art in artistas and artistas[id_art]['cadastrado'] == True:
                exibir_artista(id_art, artistas[id_art])

            else:
                print("❌ Artista não encontrado.")

        elif opcao == 2:
            termo = input("Nome (ou parte dele): ").lower().strip()
            resultado = []

            for id_art, dados in artistas.items():
                if termo in dados['nome'].lower() and artistas[id_art]['cadastrado'] == True:
                    resultado.append((id_art, dados))

            if resultado:
                for id_art, dados in resultado:
                    exibir_artista(id_art, dados) 

            else:
                print("❌ Nenhum artista encontrado com este nome.")

        elif opcao == 3:
            genero_busca = input("Gênero musical: ").lower()

            resultado = [] #Lista para armazenar o que ele achar com aquela informação

            for id_art, dados in artistas.items():
                if genero_busca == dados['genero'].lower() and artistas[id_art]['cadastrado'] == True: # verifica se existe o genero e se o artista que tem aquele género está ativo.
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
                if dados['cache'] <= cache_limite and artistas[id_art]['cadastrado'] == True:
                    resultado.append((id_art, dados))

            if resultado:
                for id_art, dados in resultado:
                    exibir_artista(id_art, dados)

            else:
                print("❌ Nenhum artista encontrado nessa faixa de cache.")

        elif opcao == 0:
            print("Saindo...")
            sleep(1)
            break

        else:
            print("⚠️ Opção inválida.")

        input("\nPressione Enter para continuar...")

def editar_artista():
    '''Busca o artista do ID e fornece para ele o um 'menu' para adicionar as novas informações do artistas associado aquele ID'''
    print("\n--- EDITAR ARTISTA ---")
    id_art = int(input("ID do artista que deseja editar: "))

    if id_art not in artistas or artistas[id_art]['cadastrado'] == False:
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
        cache  = float(novo_cache_str)
    else: 
        cache = atual['cache']
        
    if novo_genero:
        genero = novo_genero
    else:
        genero = atual['genero']

    artistas[id_art] = {'nome': nome, 'cache': cache, 'genero': genero, 'cadastrado': True}
    storage.salvar("artistas", artistas)
    print("✅ Artista atualizado com sucesso!")

def excluir_artista():
    '''Permite o usuário buscar o artista por meio do 'ID' com o objetivo de excluir. Ele tem um validador simples afim de evitar que o usuário apague sem querer'''
    print("\n--- EXCLUIR ARTISTA ---")
    id_art = int(input("ID do artista que deseja excluir: "))

    if id_art not in artistas or artistas[id_art]['cadastrado'] == False:
        print("❌ Artista não encontrado.")
        return

    confirmar = input(f"Tem certeza que quer deletar '{artistas[id_art]['nome']}'? (sim/não): ").lower()
    if confirmar == "sim":
        print("Desabilitando...")
        sleep(1)
        artistas[id_art]['cadastrado'] = False
        storage.salvar("artistas", artistas)
        print("✅ Artista Desabilitado com sucesso!")
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
  2. Listar Todos
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
            cadastrar_artista()
        elif opcao == 2:
            exibir_todos()
        elif opcao == 3:
            buscar_artistas()
        elif opcao == 4:
            editar_artista()
        elif opcao == 5:
            excluir_artista()
        elif opcao == 0:
            print("Saindo do módulo...")
            sleep(1)
            break
        else:
            print("✋👺🚫 Opção inválida!")

if __name__ == "__main__":
    menu_artistas()