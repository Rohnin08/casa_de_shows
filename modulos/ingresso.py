from time import sleep
import modulos.storage as storage
import modulos.shows as shows
import modulos.artistas as artistas
import modulos.geral as g

# ──────────────────────────────────────────────
# INICIALIZAÇÃO
# ──────────────────────────────────────────────

bilheteria = storage.carregar("bilheteria")

if not bilheteria:
    bilheteria = {
        1: {
            'id_show': 1,
            'preco': 150.00,
            'qtd_disponivel': 500
        }
    }
    storage.salvar("bilheteria", bilheteria)

# ──────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────

def obter_nome_show(id_show):
    if id_show in shows.shows:
        return shows.shows[id_show]['nome']
    else:
        return "Show Desconhecido"

def exibir_shows_disponiveis():
    shows_atuais = storage.carregar("shows") #Carrega os shows cadastrados no momento
    print("---Shows Disponiveis---\n")
    for id_ing, ing in bilheteria.items():
        id_show = ing['id_show']
        if id_show not in shows.shows:
            continue
        show = shows.shows[id_show]

        nomes_do_lineup = []
        for id_art in show['lineup']:
            if id_art in artistas.artistas:
                nomes_do_lineup.append(artistas.artistas[id_art]['nome'])
            else:
                print("Artista não encontrado")
        lineup_str = ', '.join(nomes_do_lineup)

        print(f''' 
==========================
ID Ingresso : {id_ing}
Show        : {show['nome']}
Lineup      : {lineup_str}
Horário     : {show['hora_inicio'].strftime('%H:%M')} às {show['hora_termino'].strftime('%H:%M')}
Data        : {show['data'].strftime('%d/%m/%Y')}
Preço       : R$ {ing['preco']:.2f}
Disponíveis : {ing['qtd_disponivel']} ingressos
==========================''')

# ──────────────────────────────────────────────
# CRUD
# ──────────────────────────────────────────────

def cadastrar_ingresso():
    print("--- Cadastro de Ingressos ---")
    print()
    shows_atuais = storage.carregar("shows")

    if not shows_atuais:
        print("Nenhum show cadastrado no sistema. Cadastre um show primeiro!")
        return

    novo_id = g.gerar_id(bilheteria)

    print("Shows disponíveis:")
    for id_show, show in shows_atuais.items():
        print(f"  {id_show}. {show['nome']}")
    print()

    id_show = int(input("ID do show que deseja associar a este ingresso: "))

    if id_show in shows.shows:
        preco = float(input("Preço do ingresso: "))
        qtd_disponivel = int(input("Quantidade de ingressos disponíveis: "))

        ids_cadastrados = [i['id_show'] for i in bilheteria.values()]

        if id_show not in ids_cadastrados:
            bilheteria[novo_id] = {
                'id_show': id_show,
                'preco': preco,
                'qtd_disponivel': qtd_disponivel
            }
            storage.salvar("bilheteria", bilheteria)
            print(f"\nIngresso para o show '{obter_nome_show(id_show)}' cadastrado com sucesso!")

        else:
            print("Esse show já possui ingressos cadastrados, por favor tente com outro show")
    else:
        print("Show não encontrado. Operação cancelada.")


def buscar_ingresso():
    while True:
        print('''
---------------------------------------      
         Buscador de Ingressos
---------------------------------------
  1. Buscar por ID do Ingresso
              
  2. Buscar por ID do Show
              
  3. Buscar por Preço Máximo
              
  0. Voltar ao modulo de ingressos
''')
        # Esse try/expect verifica se algo não é um 'int'. Isso evita do usuário digitar uma letra ou um float e o código dar erro. 🥸
        try:
            opcao = int(input("Qual a opção? "))
        except ValueError:
            print("Valor Invalido, por favor tente novamente")
            continue

        # Buscar por ID do ingresso
        if opcao == 1:
            id_ing = int(input("ID do ingresso: "))
            encontrou = False
            if id_ing in bilheteria:
                ing = bilheteria[id_ing]
                id_show = ing['id_show']
                nome_show = obter_nome_show(id_show)
                print(f"\nID Ingresso: {id_ing}\nShow: {nome_show}\nPreço: R${ing['preco']:.2f}\nQuantidade: {ing['qtd_disponivel']}\n")
                encontrou = True
            if not encontrou:
                print("❌Nenhum ingresso com esse ID foi encontrado.")
            input("\nPrecione Enter para continuar... ")

        # Busca por Show
        elif opcao == 2:
            id_show_busca = int(input("Digite o ID do show: "))
            encontrou = False
            for id_ing, ing in bilheteria.items():
                if ing['id_show'] == id_show_busca:
                    nome_show = obter_nome_show(id_show_busca)
                    print(f"\nID Ingresso: {id_ing}\nShow: {nome_show}\nPreço: R${ing['preco']:.2f}\nQuantidade: {ing['qtd_disponivel']}\n")
                    encontrou = True
            if not encontrou:
                print("❌Nenhum ingresso vinculado a este ID de show.")
            input("\nPressione Enter para continuar...")

        # Busca por preço
        elif opcao == 3:
            preco_max = float(input("Exibir ingressos até qual preço? R$ "))
            encontrou = False
            for id_ing, ing in bilheteria.items():
                if ing['preco'] <= preco_max:
                    nome_show = obter_nome_show(ing['id_show'])
                    print(f"\nID Ingresso: {id_ing}\nShow: {nome_show}\nPreço: R${ing['preco']:.2f}\nQuantidade: {ing['qtd_disponivel']}\n")
                    encontrou = True
            if not encontrou:
                print(f"❌Nenhum ingresso encontrado abaixo de R$ {preco_max:.2f}")
            input("\nPressione Enter para continuar...")

        elif opcao == 0:
            break

        else:
            print("Opção desconhecida")

def editar_ingresso():
    print("---Editor de Ingressos---")
    print()
    id_ingresso = int(input("ID do ingresso que deseja editar? "))

    if id_ingresso not in bilheteria:
        print("👺❌ Ingresso não encontrado")
        return

    print("Shows disponíveis:")
    for id_sh, sh in shows.shows.items(): #Lista todos os shows que estão dentro do dicionario shows
        print(f"  {id_sh}. {sh['nome']}")
    print()

    id_show = int(input("Novo ID do show: "))

    if id_show in shows.shows:
        preco = float(input("Novo preço: "))
        qtd_disponivel = int(input("Nova quantidade disponível: "))

        bilheteria[id_ingresso] = {
            'id_show': id_show,
            'preco': preco,
            'qtd_disponivel': qtd_disponivel
        }
        storage.salvar("bilheteria", bilheteria)
        print("Ingresso editado com sucesso!")
    else:
        print("👺❌ Show informado não existe. Operação cancelada.")


def excluir_ingresso():
    print("---Exclusão de Ingresso----")
    id_ingresso = int(input("Digite o ID do ingresso que você quer deletar: "))

    if id_ingresso not in bilheteria:
        print("Ingresso não encontrado")
        return

    nome_show = obter_nome_show(bilheteria[id_ingresso]['id_show'])
    validar = input(f"Quer mesmo deletar os ingressos do show: {nome_show}? (Digite sim se quiser apagar) ").lower()

    if validar == "sim":
        print("Excluindo...")
        sleep(1)
        del bilheteria[id_ingresso]
        storage.salvar("bilheteria", bilheteria)
        print("Ingresso excluido com sucesso")
    else:
        print("Operação cancelada")


def menu_ingressos():
    while True:

        print('''
=========================================
            Ingressos 🎫
=========================================
    1. Cadastrar Ingresso
              
    2. Listar/Buscar Ingressos
              
    3. Editar Ingressos
              
    4. Excluir Ingressos
              
    0. Sair do Modulo
=========================================
''')
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Valor invalido, por favor tente novamente")
            continue

        if opcao == 1:
            cadastrar_ingresso()
        elif opcao == 2:
            buscar_ingresso()
        elif opcao == 3:
            editar_ingresso()
        elif opcao == 4:
            excluir_ingresso()
        elif opcao == 0:
            print("Saindo...")
            sleep(1)
            break
