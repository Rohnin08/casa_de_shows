from time import sleep

artistas = {
    1: {
        'nome': 'Slipknot',
        'cache': 1000.00,
        'genero': 'Metal'
    },
    2: {
        'nome': 'Linkin Park',
        'cache': 1500.00,
        'genero': 'Nu Metal'
    },
    3: {
        'nome': 'Limp Bizkit',
        'cache': 1200.00,
        'genero': 'Nu Metal'
    }
}

def buscar_por_id():
    id_artista = int(input("ID do artista que deseja exibir as informações: "))   

    if id_artista in artistas: #Procura o o id de artistas dentro de artistas
        artista = artistas[id_artista] #Cria uma variavel para o armazenar as informações do artista do indice que o usuário digitol    
        #Exibição das informações
        print(f"Nome: {artista['nome']}")
        print(f"Cache: R${artista['cache']:.2f}")
        print(f"Gênero: {artista['genero']}")
    else:
        print("Artista não encontrado")

def buscar_por_nome():
    pass

def cadastrar_artista(): 
    """ Função para cadastrar os artistas, ela pega os valores digitados pelo usuário e associa-os a chaves dos dicionarios. """
    print("ADICIONAR ARTISTA")
    novo_id = len(artistas)+1
    nome = input("Nome do artista: ")
    cache = float(input("Cache do artista: "))
    genero = input("Genero músical do artista: ")

    artista = {
            'nome': nome,
            'cache':cache,
            'genero': genero
        }
    
    artistas[novo_id] = artista

    return(artistas)

def buscar_artistas():
    print('''
    =========================================
                Buscador de de artistas
    =========================================
          1. Buscar por id(busca mais precisa)
          2. Buscar por nome
          3. Busca por Gênero Músical
          4. Buscar por Cache

          ''')
    print()
    opcao = int(input("Qual a opção? "))
    if opcao == 1:
        id_artista = int(input("ID do artista que deseja exibir as informações: "))   

        if id_artista in artistas: #Procura o o id de artistas dentro de artistas
            artista = artistas[id_artista] #Cria uma variavel para o armazenar as informações do artista do indice que o usuário digitol

            #Exibição das informações
            return f"\nNome: {artista['nome']}\nCache: R${artista['cache']:.2f}\nGênero: {artista['genero']}\n"
        else:
            print("Artista não encontrado")
    elif opcao == 2:
        pass

    elif opcao == 3:
        pass

    elif opcao == 4:
        pass

    else:
        print("Opção desconhecida")




def menu_artistas():
    while  True:
        print('''
    =========================================
              Modulo de Artistas
    =========================================
        1. Cadastrar Artista

        2. Listar Artista

        3. Editar Artistas

        4. Deletar Artitas

        0. Sair do Modulo
    =========================================
    ''')
        
        opcao_artistas = int(input("Escolha uma opção: "))
        if opcao_artistas == 1:
            return cadastrar_artista()

        elif opcao_artistas == 2:
            return buscar_artistas()
        
        elif opcao_artistas == 3:
            print("EDITAR ARTISTAS")
            id_artista = int(input("Digite o ID do artista: "))
            nome = input("Novo nome: ")
            cache = input("Novo Cache: ")
            genero_musical = input("Novo genero músical: ")
        elif opcao_artistas == 4:
            print("Excluir ARTISTAS")
            print("Deletando...")
            sleep(1)
            print("Artista Deletado com sucesso!")
        elif opcao_artistas == 0:
            print("Saindo do modulo...")
            sleep(1)
            break
        else:
            print("✋👺🚫Opção invalida, tente novamente")

menu_artistas()