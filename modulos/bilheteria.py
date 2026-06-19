from time import sleep
import modulos.storage as storage
import modulos.shows as shows
from modulos.artistas import gerar_id
import modulos.artistas as artistas

# ──────────────────────────────────────────────
# INICIALIZAÇÃO
# ──────────────────────────────────────────────

bilheteria = storage.carregar("bilheteria")
vendas = storage.carregar("vendas")

if not bilheteria:
    bilheteria = {
        1: {
            'id_show': 1,
            'preco': 150.00,
            'qtd_disponivel': 500
        }
    }
    storage.salvar("bilheteria", bilheteria)

if not vendas:
    vendas = {

    }
    storage.salvar("vendas", vendas)

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

    if bilheteria:
        novo_id = max(bilheteria.keys()) + 1
    else:
        novo_id = 1

    print("Shows disponíveis:")
    for id_show, show in shows_atuais.items():
        print(f"  {id_show}. {show['nome']}")
    print()

    id_show = int(input("ID do show que deseja associar a este ingresso: "))

    if id_show in shows.shows:
        preco = float(input("Preço do ingresso: "))
        qtd_disponivel = int(input("Quantidade de ingressos disponíveis: "))

        bilheteria[novo_id] = {
            'id_show': id_show,
            'preco': preco,
            'qtd_disponivel': qtd_disponivel
        }
        storage.salvar("bilheteria", bilheteria)
        print(f"\nIngresso para o show '{obter_nome_show(id_show)}' cadastrado com sucesso!")
    else:
        print("Show não encontrado. Operação cancelada.")


def buscar_bilheteria():
    while True:
        print('''
---------------------------------------      
         Buscador de Ingressos
---------------------------------------
  1. Buscar por ID do Ingresso
  2. Buscar por ID do Show
  3. Buscar por Preço Máximo
  0. Voltar ao modulo de bilheteria
''')
        opcao = int(input("Qual a opção? "))

        if opcao == 1:
            id_ingresso = int(input("ID do ingresso: "))
            if id_ingresso in bilheteria:
                ingresso = bilheteria[id_ingresso]
                id_show = ingresso['id_show']
                nome_show = obter_nome_show(id_show)
                parar = " "
                while parar != "sim":
                    print(f"\nID Ingresso: {id_ingresso}\nShow: {nome_show}\nPreço: R${ingresso['preco']:.2f}\nQuantidade: {ingresso['qtd_disponivel']}\n")
                    parar = input("Fechar tela (digite 'sim' para sair)? ").lower()
            else:
                print("Ingresso não encontrado")

        elif opcao == 2:
            id_show_busca = int(input("Digite o ID do show: "))
            encontrou = False
            for id_ing, ing in bilheteria.items():
                if ing['id_show'] == id_show_busca:
                    nome_show = obter_nome_show(id_show_busca)
                    print(f"\nID Ingresso: {id_ing}\nShow: {nome_show}\nPreço: R${ing['preco']:.2f}\nQuantidade: {ing['qtd_disponivel']}\n")
                    encontrou = True
            if not encontrou:
                print("Nenhum ingresso vinculado a este ID de show.")
            input("\nPressione Enter para continuar...")

        elif opcao == 3:
            preco_max = float(input("Exibir ingressos até qual preço? R$ "))
            encontrou = False
            for id_ing, ing in bilheteria.items():
                if ing['preco'] <= preco_max:
                    nome_show = obter_nome_show(ing['id_show'])
                    print(f"\nID Ingresso: {id_ing}\nShow: {nome_show}\nPreço: R${ing['preco']:.2f}\nQuantidade: {ing['qtd_disponivel']}\n")
                    encontrou = True
            if not encontrou:
                print(f"Nenhum ingresso encontrado abaixo de R$ {preco_max:.2f}")
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
    for id_sh, sh in shows.shows.items():
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


def vender_ingresso():
    print("--- Venda de Ingressos ---")

    if not bilheteria:
        print("Nenhum ingresso cadastrado no sistema")
        return

    exibir_shows_disponiveis()

    id_ingresso = int(input("\nDigite o ID do ingresso que você deseja comprar: "))

    if id_ingresso not in bilheteria:
        print("❌ Ingresso não encontrado")
        return

    ingresso = bilheteria[id_ingresso]

    if ingresso['qtd_disponivel'] == 0:
        print("❌ Ingressos esgotados para esse show.")
        return

    quantidade = int(input(f"Quantos ingressos? (disponíveis: {ingresso['qtd_disponivel']}) "))

    if quantidade > ingresso['qtd_disponivel']:
        print(f"Quantidade indisponivel. Máximo: {ingresso['qtd_disponivel']}")
        return

    valor_total = quantidade * ingresso['preco']
    nome_show = obter_nome_show(ingresso['id_show'])

    confirmar = input(f"\nConfirmar compra de {quantidade} ingressos para '{nome_show}' por R$ {valor_total:.2f}? (sim/não): ").lower()

    if confirmar == 'sim':
        if vendas:
            novo_id_venda = max(vendas.keys()) + 1
        else:
            novo_id_venda = 1

        vendas[novo_id_venda] = {
            'id_ingresso': id_ingresso,
            'id_show': ingresso['id_show'],
            'quantidade': quantidade,
            'valor_total': valor_total
        }
        ingresso['qtd_disponivel'] -= quantidade
        storage.salvar("bilheteria", bilheteria)
        storage.salvar("vendas", vendas)
        print(f"✅ Compra realizada! {quantidade} ingresso(s) para '{nome_show}'. Total: R$ {valor_total:.2f}")
    else:
        print("❌ Operação cancelada")


# ──────────────────────────────────────────────
# MENU PRINCIPAL DO MÓDULO
# ──────────────────────────────────────────────

def menu_bilheteria():
    while True:
        print('''
=========================================
          Modulo de Bilheteria
=========================================
    1. Cadastrar Ingresso
    2. Listar/Buscar Ingressos
    3. Editar Ingressos
    4. Deletar Ingressos
    5. Computar vendas
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
            buscar_bilheteria()
        elif opcao == 3:
            editar_ingresso()
        elif opcao == 4:
            excluir_ingresso()
        elif opcao == 5:
            vender_ingresso()
        elif opcao == 0:
            print("Saindo do modulo...")
            sleep(1)
            break
        else:
            print("✋👺🚫Opção invalida, tente novamente")


if __name__ == "__main__":
    menu_bilheteria()