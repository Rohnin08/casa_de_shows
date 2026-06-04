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

def exibir_todos():
    for chave, artista in artistas.items():
        pass

def cadastrar_artista(): 
    """ Função para cadastrar os artistas, ela pega os valores digitados pelo usuário e associa-os a chaves dos dicionarios."""
    print("Cadastro de Artistas")
    print()
    novo_id = len(artistas)+1 #Define um ID para o usuário com base no tamanho da lista e adiciona 1.
    nome = input("Nome do artista: ") 
    cache = float(input("Cache do artista: "))
    genero = input("Genero músical do artista: ")

    artista = {
            'nome': nome,
            'cache':cache,
            'genero': genero
        }
    
    artistas[novo_id] = artista

# Buscar Artista
def buscar_artistas():
    """Função "guarda-chuva" dos filtros de busca da opção de busca"""
    while True:

        print('''
---------------------------------------       
        Buscador de de Artistas
---------------------------------------

  1. Buscar por id

  2. Buscar por nome

  3. Busca por Gênero Músical

  4. Buscar por Cache
  
  0. Voltar ao modulo de artistas
  ''')
        print()
        opcao = int(input("Qual a opção? "))

        #Busca por id
        if opcao == 1:
            id_artista = int(input("ID do artista que deseja exibir as informações: "))   

            if id_artista in artistas: #Procura o o id de artistas dentro de artistas
                artista = artistas[id_artista] #Cria uma variavel para o armazenar as informações do artista do indice que o usuário digitou

                #Exibição das informações usando um laço. Fiz isso para que as informações não sejam jogadas e o código para para a prixima etapa abruptamente
                parar = " "
                while parar != "sim":
                    print(f"\nNome: {artista['nome']}\nCache: R${artista['cache']:.2f}\nGênero: {artista['genero']}\n")
                    parar = input("Fechar tela(digite 'sim' para sair)?").lower()

            else:
                 print("Artista não encontrado")
        
        elif opcao == 2:
            pass

        elif opcao == 3:
            pass

        elif opcao == 4:
            pass
        elif opcao == 0:
            break

        else:
            print("Opção desconhecida")

#Editar artista
def editar_artista():
    print("Editor de Artistas")
    print()
    id_artista = int(input("ID do artista que deseja editar?"))
    
    if id_artista in artistas:
        nome = str(input("Novo nome: "))
        cache = float(input("Novo cache: "))
        genero = str(input("Novo genero músical: "))

        artista = {
            'nome': nome,
            'cache':cache,
            'genero': genero
        }

        artistas[id_artista] = artista #Atribui o valor do dicionario artista ao item do valor do id do "dicionario pai" artistas
        


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
            cadastrar_artista()

        elif opcao_artistas == 2:
            buscar_artistas()
        
        elif opcao_artistas == 3:
            editar_artista()

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