import os
from time import sleep
import modulos.artistas as artistas
import modulos.shows as shows
import modulos.clientes as clientes
import modulos.bilheteria as bilheteria

controle = True

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# Menu principal do sistema
while controle == True:
    limpar_tela()
    print('''⠀⠀⠀⠀
==============================================
         ♬ ♪ MUSICAL BASEMENT ♬ ♪
==============================================
    1. Artistas 👨‍🎤

    2. Shows 🎤

    3. Bilheteria 🎫
    
    4. Relatorios de Vendas 💹
    
    5. Sobre o sistema 🥸

    0. Sair do Sistema 📤
===============================================
''')
    opcao = int(input("Escolha uma opção: "))

    # Modulo de Artistas
    limpar_tela()
    if opcao == 1:
        limpar_tela()
        print("Carregando...")
        sleep(1)
        artistas.menu_artistas()
    
    elif opcao == 2:
        limpar_tela()
        print("Carregando...")
        sleep(1)
        clientes.menu_clientes()
        
        
    # Modulo de Shows
    elif opcao == 3:
        limpar_tela()
        print("Carregando...")
        sleep(1)
        shows.menu_shows()

    #Modulo Bilheteria
    elif opcao == 4:
        limpar_tela()
        print("Carregando...")
        sleep(1)
        bilheteria.menu_bilheteria()
    
    elif opcao == 5:
        limpar_tela()
        print("Carregando...")
        sleep(1)
        limpar_tela()
        pass

    elif opcao == 6:
        limpar_tela()
        print("Carregando...")
        sleep(1)
        limpar_tela()
        pass


    elif opcao == 0:
        limpar_tela()
        print("Saindo do programa...")
        sleep(1)
        controle = False

    else:
        print("✋👺🚫Opção invalida, tente novamente")