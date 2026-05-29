import os
from time import sleep

controle = True

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while controle == True:
    limpar_tela()
    # Menu principal do sistema
    print('''
    =========================================
          SISTEMA DE GESTÃO - PYSHOW
    =========================================
    1. Modulo Artistas
    2. Modulo Shows
    3. Modulo Bilheteria
    0. Sair do Sistema
    =========================================
    ''')
    opcao_menu = int(input("Escolha uma opção: "))

    # Modulo de Artistas
    if opcao_menu == 1:
        while  True:
            limpar_tela()
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
                print("ADICIONAR ARTISTA")
                nome = input("Nome do artista: ")
                cache = input("Cache do artista: ")
                genero_musical = input("Genero músical do artista: ")
            elif opcao_artistas == 2:
                print("LISTAR ARTISTAS")
                print("⚠️Estamos desenvolvendo isso")
            elif opcao_artistas == 3:
                print("EDITAR ARTISTAS")
            elif opcao_artistas == 4:
                print("Excluir ARTISTAS")
                print("⚠️Estamos desenvolvendo isso")
            elif opcao_artistas == 0:
                print("Saindo do modulo...")
                sleep(1)
                break
            else:
                print("Opção invalida, tente novamente")

    # Modulo de shows
    elif opcao_menu == 2:
        while True:
            limpar_tela()
            print('''
    =========================================
              Modulo de Artistas
    =========================================
    1. Cadastrar Show
    2. Listar Shows
    3. Editar Shows
    4. Deletar Shows
    0. Sair do Modulo
    =========================================
    ''')
            opcao_show = int(input("Escolha uma opção: "))
            if opcao_show == 1:
                print("ADICIONAR SHOW")
                nome_show = input("Nome do show: ")
                artistas_show = input("Nome dos artistas: ")
                genero_show = input("Estilos músicais: ")
            elif opcao_show == 2:
                print("LISTAR SHOWS")
                print("⚠️Estamos desenvolvendo isso")
            elif opcao_show == 3:
                print("EDITAR SHOWS")
            elif opcao_show == 4:
                print("Excluir SHOWS")
                print("⚠️Estamos desenvolvendo isso")
            elif opcao_show == 0:
                print("Saindo do modulo...")
                sleep(1)
                break
            else:
                print("Opção invalida, tente novamente")
    
    # Modulo de shows
    elif opcao_menu == 3:
        while True:
            limpar_tela()
            print('''
    =========================================
              Modulo de Bilheteria
    =========================================
    1. Cadastrar Ingressos
    2. Listar Ingressos
    3. Editar Ingressos
    4. Deletar Ingressos
    0. Sair do Modulo
    =========================================
    ''')
            opcao_bilheteria = int(input("Escolha uma opção: "))
            if opcao_bilheteria == 1:
                print("ADICIONAR SHOW")
                ingresso_show =  input("Para qual show é o ingresso? ")
                ingresso_quant = input("Número de ingressos? ")
            elif opcao_bilheteria == 2:
                print("LISTAR SHOWS")
                print("⚠️Estamos desenvolvendo isso")
            elif opcao_bilheteria == 3:
                print("EDITAR SHOWS")
            elif opcao_bilheteria == 4:
                print("Excluir SHOWS")
                print("⚠️Estamos desenvolvendo isso")
            elif opcao_bilheteria == 0:
                print("Saindo do modulo...")
                sleep(1)
                break
            else:
                print("Opção invalida, tente novamente")
    
    elif opcao_menu == 0:
        print("Saindo do programa")
        sleep(1)
        controle = False

        



        



