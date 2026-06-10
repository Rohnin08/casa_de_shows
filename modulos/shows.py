from datetime import date, time
from time import sleep
import modulos.artistas as artistas

shows = {
    1: {
        'nome': 'Metal Fest',
        'lineup': [1, 2],
        'hora_inicio': time(20, 0),
        'hora_termino': time(23, 30),
        'data': date(2025, 7, 15)
    }
}

def cadastrar_show():
    print("--- Cadastro de Shows ---")
    print()
    if shows: 
        novo_id = max(shows.keys()) + 1
    else:
        novo_id = 1
    nome = input("Nome do show: ")

    print("\nArtistas disponíveis:")
    for id, artista in artistas.artistas.items():
        print(f"  {id}. {artista['nome']}")

    lineup = []
    while True:
        entrada = input("\nDigite o ID do artista para adicionar ao lineup (ou 0 para terminar): ")
        id_artista = int(entrada)

        if id_artista == 0:
            break
        elif id_artista in artistas.artistas:
            if id_artista not in lineup: #Verifica se o artista com aquele id já está no lineup do show.
                lineup.append(id_artista) #se não tiver ele adiciona
                print(f"{artistas.artistas[id_artista]['nome']} adicionado ao lineup.") #Manda essa mensagem para provar que o artista foi adicionado
            else:
                print("Esse artista já está no lineup.")#Se não ele exibe isso daqui. Uma mensagem que te impede de colocar dois Slipknots no mesmo show
        else:
            print("Artista não encontrado.")#Caso ele não encontre nem um artista com aquele id ele exibe isso daqui

    hora_inicio = time(*map(int, input("Horário de início (HH MM): ").split())) #Recebe o valor digitado pelo usuário depois transforma em lista usando splip. Depois aplica o map para converter tudo em inteiro, e desempacota * papra time
    hora_termino = time(*map(int, input("Horário de término (HH MM): ").split())) #Mesma coisa da linha 45
    data = date(*map(int, input("Data (AAAA MM DD): ").split())) #Faz o mesmo só que com data

    shows[novo_id] = {
        'nome': nome,
        'lineup': lineup,
        'hora_inicio': hora_inicio,
        'hora_termino': hora_termino,
        'data': data
    }

    print(f"\nShow '{nome}' cadastrado com sucesso!")


def exibir_show(id_show):
    show = shows[id_show]
    nomes_lineup = []
    for id in show['lineup']:
        if id in artistas.artistas:
            nomes_lineup.append(artistas.artistas[id]['nome'])

    print(f"""
  ID do Show: {id_show}
  Nome:       {show['nome']}
  Data:       {show['data'].strftime('%d/%m/%Y')}
  Início:     {show['hora_inicio'].strftime('%H:%M')}
  Término:    {show['hora_termino'].strftime('%H:%M')}
  Lineup:     {', '.join(nomes_lineup) if nomes_lineup else 'Nenhum artista vinculado'}
  ---------------------------------------""")


def buscar_shows():
    while True:
        print('''
---------------------------------------
        Buscador de Shows
---------------------------------------

  1. Buscar por ID

  2. Buscar por nome

  3. Listar todos

  0. Voltar
''')
        opcao = int(input("Qual a opção? "))

        if opcao == 1:
            id_show = int(input("ID do show: "))
            if id_show in shows:
                parar = " "
                while parar != "sim":
                    exibir_show(id_show)
                    parar = input("Fechar tela (digite 'sim' para sair): ").lower()
            else:
                print("Show não encontrado.")

        elif opcao == 2:
            termo = input("Digite o nome do show (ou parte dele): ").lower()
            encontrados = False
            print("\n--- Resultados da Busca ---")
            for id_show, dados in shows.items():
                if termo in dados['nome'].lower():
                    exibir_show(id_show)
                    encontrados = True
            if not encontrados:
                print("Nenhum show encontrado com esse nome.")
            input("\nPressione Enter para continuar...")

        elif opcao == 3:
            print("\n--- Todos os Shows Agendados ---")
            if not shows:
                print("Nenhum show cadastrado ainda.")
            else:
                # Percorre o dicionário e usa a sua função de exibição formatada
                for id_show in shows.keys():
                    exibir_show(id_show)
            input("\nPressione Enter para continuar...")

        elif opcao == 0:
            break

        else:
            print("Opção desconhecida.")


def editar_show():
    print("--- Editor de Shows ---")
    id_show = int(input("ID do show que deseja editar: "))

    if id_show not in shows:
        print("Show não encontrado.")
        return

    nome = input("Novo nome: ")

    print("\nArtistas disponíveis:")
    for id, artista in artistas.artistas.items():
        print(f"  {id}. {artista['nome']}")

    lineup = []
    while True:
        entrada = input("Digite o ID do artista (ou 0 para terminator): ")
        id_artista = int(entrada)

        if id_artista == 0:
            break
        elif id_artista in artistas.artistas:
            if id_artista not in lineup:
                lineup.append(id_artista)
        else:
            print("Artista não encontrado.")

    hora_inicio = time(*map(int, input("Novo horário de início (HH MM): ").split()))
    hora_termino = time(*map(int, input("Novo horário de término (HH MM): ").split()))
    data = date(*map(int, input("Nova data (AAAA MM DD): ").split()))

    shows[id_show] = {
        'nome': nome,
        'lineup': lineup,
        'hora_inicio': hora_inicio,
        'hora_termino': hora_termino,
        'data': data
    }

    print("Show editado com sucesso!")


def excluir_show():
    print("--- Exclusão de Show ---")
    id_show = int(input("ID do show que deseja deletar: "))

    if id_show not in shows:
        print("Show não encontrado.")
        return

    validar = input(f"Quer mesmo deletar '{shows[id_show]['nome']}'? (Digite sim para confirmar): ").lower()
    if validar == "sim":
        print("Excluindo...")
        sleep(1)
        del shows[id_show]
        print("Show excluído com sucesso.")
    else:
        print("Operação cancelada.")


def menu_shows():
    while True:
        print('''
=========================================
            Modulo de Shows
=========================================
    1. Cadastrar Show

    2. Buscar Show

    3. Editar Show

    4. Deletar Show

    0. Sair do Módulo
=========================================
''')
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_show()
        elif opcao == 2:
            buscar_shows()
        elif opcao == 3:
            editar_show()
        elif opcao == 4:
            excluir_show()
        elif opcao == 0:
            print("Saindo do módulo...")
            sleep(1)
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu_shows()