from time import sleep
import modulos.storage as storage
import modulos.shows as shows
import modulos.artistas as artistas
import modulos.geral as g

# ──────────────────────────────────────────────
# INICIALIZAÇÃO
# ──────────────────────────────────────────────

ingressos = storage.carregar("ingressos")

if not ingressos:
    ingressos = {
        1: {
            'id_show': 1,
            'preco': 150.00,
            'qtd_disponivel': 500,
            'cadastrado':True
        }
    }
    storage.salvar("ingressos", ingressos)


# ──────────────────────────────────────────────
# Funções uteis
# ──────────────────────────────────────────────

def obter_nome_show(id_show):
    '''Obtem o nome dos shows do arquivo de shows'''
    if id_show in shows.shows:
        return shows.shows[id_show]['nome']
    else:
        return "Show Desconhecido"



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

    novo_id = g.gerar_id(ingressos)

    print("Shows disponíveis:")
    for id_show, show in shows_atuais.items():
        if show['cadastrado']:
            print(f"  {id_show}. {show['nome']}")
    print()

    id_show = int(input("ID do show que deseja associar a este ingresso: "))

    if id_show in shows.shows and shows.shows[id_show]['cadastrado']:
        preco = float(input("Preço do ingresso: "))
        qtd_disponivel = int(input("Quantidade de ingressos disponíveis: "))

        ids_cadastrados = [i['id_show'] for i in ingressos.values()]

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
            if id_ing in ingressos and ingressos[id_ing]['cadastrado']:
                ing = ingressos[id_ing]
                id_show = ing['id_show']
                nome_show = obter_nome_show(id_show)
                print(f"\nID Ingresso: {id_ing}\nShow: {nome_show}\nPreço: R${ing['preco']:.2f}\nQuantidade: {ing['qtd_disponivel']}\n")
                encontrou = True
            if not encontrou:
                print("❌Nenhum ingresso com esse ID foi encontrado.")
            input("\nPrecione Enter para continuar... ")

        # Busca por Show, filtro simples
        elif opcao == 2:
            id_show_busca = int(input("Digite o ID do show: "))
            encontrou = False
            for id_ing, ing in ingressos.items():
                if ing['id_show'] == id_show_busca and ingressos[id_ing]['cadastrado']:
                    nome_show = obter_nome_show(id_show_busca)
                    print(f"\nID Ingresso: {id_ing}\nShow: {nome_show}\nPreço: R${ing['preco']:.2f}\nQuantidade: {ing['qtd_disponivel']}\n")
                    encontrou = True
            if not encontrou:
                print("❌Nenhum ingresso vinculado a este ID de show.")
            input("\nPressione Enter para continuar...")

        # Busca por preço, filtro simples
        elif opcao == 3:
            preco_max = float(input("Exibir ingressos até qual preço? R$ "))
            encontrou = False
            for id_ing, ing in ingressos.items():
                if ing['preco'] <= preco_max and ingressos[id_ing]['cadastrado']:
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
    id_ing = int(input("ID do ingresso que deseja editar? "))

    if id_ing not in ingressos or not ingressos[id_ing]['cadastrado']:
        print("👺❌ Ingresso não encontrado")
        return

    print("Shows disponíveis:")
    for id_show, show in shows.shows.items(): #Lista todos os shows que estão dentro do dicionario shows
        if show['cadastrado']:
            print(f"  {id_show}. {show['nome']}")
    print()

    id_show = int(input("Novo ID do show: "))

    if id_show in shows.shows and shows.shows[id_show]['cadastrado']:
        preco = float(input("Novo preço: "))
        qtd_disponivel = int(input("Nova quantidade disponível: "))

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
    print("---Exclusão de Ingresso----")
    id_ing = int(input("Digite o ID do ingresso que você quer deletar: "))

    if id_ing not in ingressos or not ingressos[id_ing]['cadastrado']:
        print("Ingresso não encontrado")
        return

    nome_show = obter_nome_show(ingressos[id_ing]['id_show'])
    validar = input(f"Quer mesmo deletar os ingressos do show: {nome_show}? (Digite sim se quiser apagar) ").lower()

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
