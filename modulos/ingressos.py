from time import sleep
import modulos.storage as storage
import modulos.shows as shows
import modulos.geral as g
from modulos.geral import limpar_tela


# ──────────────────────────────────────────────
# INICIALIZAÇÃO
# ──────────────────────────────────────────────

ingressos = storage.carregar("ingressos")

if not ingressos:
    ingressos = {
    1: {'id_show': 1, 'preco': 120.00, 'qtd_disponivel': 197, 'cadastrado': True},
    2: {'id_show': 2, 'preco': 150.00, 'qtd_disponivel': 198, 'cadastrado': True},
    3: {'id_show': 3, 'preco': 90.00, 'qtd_disponivel': 196, 'cadastrado': True},
    4: {'id_show': 4, 'preco': 80.00, 'qtd_disponivel': 199, 'cadastrado': True},
    5: {'id_show': 5, 'preco': 140.00, 'qtd_disponivel': 198, 'cadastrado': True},
    6: {'id_show': 6, 'preco': 100.00, 'qtd_disponivel': 197, 'cadastrado': True},
    7: {'id_show': 7, 'preco': 170.00, 'qtd_disponivel': 199, 'cadastrado': True},
    8: {'id_show': 8, 'preco': 110.00, 'qtd_disponivel': 198, 'cadastrado': True},
    9: {'id_show': 9, 'preco': 95.00, 'qtd_disponivel': 196, 'cadastrado': True},
    10: {'id_show': 10, 'preco': 180.00, 'qtd_disponivel': 197, 'cadastrado': True}
}
    storage.salvar("ingressos", ingressos)


# ──────────────────────────────────────────────
# Funções uteis
# ──────────────────────────────────────────────

def obter_nome_show(id_show):
    '''Obtem o nome dos shows do arquivo de shows'''
    if id_show in shows.shows and shows.shows[id_show]['cadastrado']:
        return shows.shows[id_show]['nome']
    else:
        return "Show Desconhecido"

# ──────────────────────────────────────────────
# CRUD
# ──────────────────────────────────────────────

def cadastrar_ingresso():
    print("=== Cadastro de Ingressos ===\n")

    if not shows.shows:
        print("Nenhum show cadastrado no sistema. Cadastre um show primeiro!")
        return

    novo_id = g.gerar_id(ingressos)

    print("Shows disponíveis:")
    for id_show, show in shows.shows.items():
        if show['cadastrado']:
            print(f"  {id_show}. {show['nome']}\n")

    while True:
        try:
            id_show = int(input("ID do show que deseja associar a este ingresso: "))
            break
        except ValueError:
            print("⚠️ ID invalido, tente novamente")

    if id_show in shows.shows and shows.shows[id_show]['cadastrado']:
        while True:
            try:
                preco = float(input("Preço do ingresso: "))
                qtd_disponivel = int(input("Quantidade de ingressos disponíveis: "))
                break
            except ValueError:
                print("⚠️ Valor invalido, tente novamente")

        ids_cadastrados = [i['id_show'] for i in ingressos.values() if i['cadastrado']]

        if id_show not in ids_cadastrados:
            ingressos[novo_id] = {
                'id_show': id_show,
                'preco': preco,
                'qtd_disponivel': qtd_disponivel,
                'cadastrado': True
            }
            storage.salvar("ingressos", ingressos)
            print(f"\nIngresso para o show '{obter_nome_show(id_show)}' cadastrado com sucesso!")

        else:
            print("Esse show já possui ingressos cadastrados, por favor tente com outro show")
    else:
        print("Show não encontrado. Operação cancelada.")


def buscar_ingresso():
    while True:
        print('''
=======================================
         Buscador de Ingressos
=======================================
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
            while True:
                try:
                    id_ing = int(input("ID do ingresso: "))
                    break
                except ValueError:
                    print("⚠️ Valor invalido, tente novamente.")

            encontrou = False
            if id_ing in ingressos and ingressos[id_ing]['cadastrado']:
                ing = ingressos[id_ing]
                nome_show = obter_nome_show(ing['id_show'])
                print(f"\nID Ingresso: {id_ing}\nShow: {nome_show}\nPreço: R${ing['preco']:.2f}\nQuantidade: {ing['qtd_disponivel']}\n")
                encontrou = True
            if not encontrou:
                print("❌Nenhum ingresso com esse ID foi encontrado.")
            input("\nPressione Enter para continuar... ")

        # Busca por Show, filtro simples
        elif opcao == 2:
            while True:
                try:
                    id_show_busca = int(input("Digite o ID do show: "))
                    break
                except ValueError:
                    print("⚠️ ID invalido, tente novamente.")

            encontrou = False
            for id_ing, ing in ingressos.items():
                if ing['id_show'] == id_show_busca and ing['cadastrado']:
                    nome_show = obter_nome_show(id_show_busca)
                    print(f"\nID Ingresso: {id_ing}\nShow: {nome_show}\nPreço: R${ing['preco']:.2f}\nQuantidade: {ing['qtd_disponivel']}\n")
                    encontrou = True
            if not encontrou:
                print("❌Nenhum ingresso vinculado a este ID de show.")
            input("\nPressione Enter para continuar...")

        # Busca por preço, filtro simples
        elif opcao == 3:
            while True:
                try:
                    preco_max = float(input("Exibir ingressos até qual preço? R$ "))
                    break
                except ValueError:
                    print("⚠️ Valor invalido, tente novamente.")

            encontrou = False
            for id_ing, ing in ingressos.items():
                if ing['preco'] <= preco_max and ing['cadastrado']:
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
    print("=== Editor de Ingressos ===")
    print()

    while True:
        try:
            id_ing = int(input("ID do ingresso que deseja editar? "))
            break
        except ValueError:
            print("⚠️ ID invalido, tente novamente.")

    if id_ing not in ingressos or not ingressos[id_ing]['cadastrado']:
        print("👺❌ Ingresso não encontrado")
        return

    print("Shows disponíveis:")
    for id_show, show in shows.shows.items(): #Lista todos os shows que estão dentro do dicionario shows
        if show['cadastrado']:
            print(f"  {id_show}. {show['nome']}")
    print()

    while True:
        try:
            id_show = int(input("Novo ID do show: "))
            break
        except ValueError:
            print("⚠️ ID invalido, tente novamente.")

    if id_show in shows.shows and shows.shows[id_show]['cadastrado']:
        while True:
            try:
                preco = float(input("Novo preço: "))
                qtd_disponivel = int(input("Nova quantidade disponível: "))
                break
            except ValueError:
                print("⚠️ Valor invalido, tente novamente.")

        ingressos[id_ing] = {
            'id_show': id_show,
            'preco': preco,
            'qtd_disponivel': qtd_disponivel,
            'cadastrado':True
        }
        storage.salvar("ingressos", ingressos)
        print("Ingresso editado com sucesso!")
    else:
        print("👺❌ Show informado não existe. Operação cancelada.")


def excluir_ingresso():
    print("=== Exclusão de Ingresso ===")

    while True:
        try:
            id_ing = int(input("Digite o ID do ingresso que você quer excluir: "))
            break
        except ValueError:
            print("⚠️ ID invalido, tente novamente.")

    if id_ing not in ingressos or not ingressos[id_ing]['cadastrado']:
        print("Ingresso não encontrado")
        return

    nome_show = obter_nome_show(ingressos[id_ing]['id_show'])
    validar = input(f"Quer mesmo excluir os ingressos do show: {nome_show}? (Digite sim se quiser apagar) ").lower()

    if validar == "sim":
        print("Excluindo...")
        sleep(1)
        ingressos[id_ing]['cadastrado'] = False
        storage.salvar("ingressos", ingressos)
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
            limpar_tela()
            cadastrar_ingresso()

        elif opcao == 2:
            limpar_tela()
            buscar_ingresso()

        elif opcao == 3:
            limpar_tela()
            editar_ingresso()

        elif opcao == 4:
            limpar_tela()
            excluir_ingresso()

        elif opcao == 0:
            print("Saindo...")
            sleep(1)
            break