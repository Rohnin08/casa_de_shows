from time import sleep
import modulos.artistas as artistas
import modulos.shows as shows
import modulos.clientes as clientes
import modulos.bilheteria as bilheteria
import functions.relatorios as relatorio_vendas
import functions.sobre as sobre
from functions.geral import limpar_tela

controle = True

# Menu principal do sistema
while controle == True:
    limpar_tela()
    print('''⠀⠀⠀⠀
==============================================
         ♬ ♪ MUSICAL BASEMENT ♬ ♪
==============================================
    1. Artistas 👨‍🎤
          
    2. Clientes 🧑

    3. Shows 🎸

    4. Bilheteria 🎫 💵
        
    5. Relatorios de Vendas 📋 
    
    6. Sobre o sistema 🥸

    0. Sair do Sistema 📤
===============================================
''')
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Valor invalido, por favor tente novamente")
        continue

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
        relatorio_vendas.menu_relatorios()

    elif opcao == 6:
        limpar_tela()
        print("Carregando...")
        sleep(1)
        limpar_tela()
        sobre.exibir_sobre()

    elif opcao == 0:
        limpar_tela()
        print("Saindo do programa...")
        sleep(1)
        controle = False

    else:
        print("✋👺🚫Opção invalida, tente novamente")