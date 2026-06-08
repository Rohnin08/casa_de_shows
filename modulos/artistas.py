from time import sleep

artistas = {
    1: {'nome': 'Slipknot', 'cache': 1000.00, 'genero': 'Metal'},
    2: {'nome': 'Linkin Park', 'cache': 1500.00, 'genero': 'Nu Metal'},
    3: {'nome': 'Limp Bizkit', 'cache': 1200.00, 'genero': 'Nu Metal'}
}

def cadastrar_artista(): 
    print("\n--- ADICIONAR ARTISTA ---")
    # Usando max() para garantir que o ID seja sempre único, mesmo após deleções
    novo_id = max(artistas.keys()) + 1 if artistas else 1
    
    nome = input("Nome do artista: ")
    cache = float(input("Cache do artista: "))
    genero = input("Genero músical do artista: ")

    artistas[novo_id] = {
        'nome': nome,
        'cache': cache,
        'genero': genero
    }
    print(f"\n✅ {nome} cadastrado com sucesso!")

def buscar_artistas():
    while True:
        print('''
    =========================================
             Buscador de Artistas
    =========================================
          1. Buscar por ID
          2. Buscar por Nome
          3. Buscar por Gênero
          4. Buscar por Cache
          0. Voltar
        ''')
        
        opcao = int(input("Qual a opção? "))
        
        if opcao == 1:
            id_art = int(input("ID do artista: "))
            if id_art in artistas:
                art = artistas[id_art]
                print(f"\nID: {id_art} | Nome: {art['nome']} | Cache: R${art['cache']:.2f} | Gênero: {art['genero']}")
            else:
                print("❌ Artista não encontrado.")

        elif opcao == 2:
            termo = input("Nome do artista (ou parte dele): ").lower()
            encontrados = False
            for id_art, dados in artistas.items():
                if termo in dados['nome'].lower():
                    print(f"ID: {id_art} | Nome: {dados['nome']} | Gênero: {dados['genero']}")
                    encontrados = True
            if not encontrados:
                print("❌ Nenhum artista encontrado com este nome.")

        elif opcao == 3:
            genero_busca = input("Gênero musical: ").lower()
            for id_art, dados in artistas.items():
                if genero_busca == dados['genero'].lower():
                    print(f"ID: {id_art} | Nome: {dados['nome']} | Cache: R${dados['cache']:.2f}")

        elif opcao == 4:
            cache_limite = float(input("Exibir artistas com cache até: R$ "))
            for id_art, dados in artistas.items():
                if dados['cache'] <= cache_limite:
                    print(f"ID: {id_art} | Nome: {dados['nome']} | Cache: R${dados['cache']:.2f}")

        elif opcao == 0:
            break
        
        input("\nPressione Enter para continuar...")

def menu_artistas():
    while True:
        print('''
    =========================================
              Modulo de Artistas
    =========================================
        1. Cadastrar Artista
        2. Buscar/Listar Artista
        3. Editar Artistas
        4. Deletar Artistas
        0. Sair do Modulo
    =========================================
    ''')
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            cadastrar_artista() # Removido o return
        elif opcao == 2:
            buscar_artistas()   # Removido o return
        elif opcao == 3:
            # Implementar lógica de edição similar ao cadastro
            pass
        elif opcao == 4:
            # Implementar lógica de exclusão com del artistas[id]
            pass
        elif opcao == 0:
            print("Saindo do modulo...")
            sleep(1)
            break
        else:
            print("✋👺🚫 Opção invalida!")

if __name__ == "__main__":
    menu_artistas()