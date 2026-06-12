from time import sleep
import modulos.shows as shows
import modulos.artistas as artistas

bilheteria = {
    1: {
        'id_show': 1,
        'preco': 150.00,
        'qtd_disponivel': 500
    }
}

vendas = {}

def obter_nome_show(id_show):
    if id_show in shows.shows:
        return shows.shows[id_show]['nome']
    else:
        return "Show Desconhecido"
    
def exibir_shows_disponiveis():
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





def cadastrar_ingresso():
    """ Função para cadastrar os ingressos, ela pega os valores digitados pelo usuário e associa-os a chaves dos dicionarios. """
    print("--- Cadastro de Ingressos ---")
    print()
    
    # Validação caso não existam shows cadastrados no outro módulo
    if not shows.shows:
        print("Nenhum show cadastrado no sistema. Cadastre um show primeiro!")
        return

    if bilheteria: #Verifica se dicionario tem alguma coisa dentro.
        novo_id = max(bilheteria.keys()) + 1 #Se tiver, ele atribui a variavel o maior termo +1
    else:
        novo_id = 1 #Se não, ele só adiciona o item que não existia como id = 1
    
    print("Shows disponíveis:")
    for id_show, show in shows.shows.items():
        print(f"  {id_show}. {show['nome']}")
    print()
    
    id_show = int(input("ID do show que deseja associar a este ingresso: "))
    
    if id_show in shows.shows:
        preco = float(input("Preço do ingresso: "))
        qtd_disponivel = int(input("Quantidade de ingressos disponíveis: "))

        ingresso = {
            'id_show': id_show,
            'preco': preco,
            'qtd_disponivel': qtd_disponivel
        }

        bilheteria[novo_id] = ingresso
        print(f"\nIngresso para o show '{obter_nome_show(id_show)}' cadastrado com sucesso!")
    else:
        print("Show não encontrado. Operação cancelada.")


# Buscar Ingresso na bilheteria
def buscar_bilheteria():
    """Função "guarda-chuva" dos filtros de busca da opção de busca da bilheteria"""
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
        print()
        opcao = int(input("Qual a opção? "))

        # Busca por id do ingresso
        if opcao == 1:
            id_ingresso = int(input("ID do ingresso que deseja exibir as informações: "))   

            if id_ingresso in bilheteria:
                ingresso = bilheteria[id_ingresso]
                id_show = ingresso['id_show']
                if id_show in shows.shows:
                    nome_show = obter_nome_show(id_show)
                else:
                    nome_show = "Show Desconhecido"
                # Loop de exibição até digitar "sim", fiz isso pra evitar que o código jogue a informação e pule para a proxima parte
                parar = " "
                while parar != "sim":
                    print(f"\nID Ingresso: {id_ingresso}\nShow: {nome_show}\nPreço: R${ingresso['preco']:.2f}\nQuantidade: {ingresso['qtd_disponivel']}\n")
                    parar = input("Fechar tela(digite 'sim' para sair)? ").lower()
            else:
                 print("Ingresso não encontrado")
        
        # Busca por ID do Show
        elif opcao == 2:
            id_show_busca = int(input("Digite o ID do show para filtrar os ingressos: "))
            encontrou = False
            
            for id_ing, ing in bilheteria.items():
                if ing['id_show'] == id_show_busca:
                    if id_show_busca in shows.shows:
                        nome_show = shows.shows[id_show_busca]['nome'] 
                    else: 
                        print("Show Desconhecido")
                    print(f"\nID Ingresso: {id_ing}\nShow: {nome_show}\nPreço: R${ing['preco']:.2f}\nQuantidade: {ing['qtd_disponivel']}\n")
                    encontrou = True
            
            if not encontrou:
                print("Nenhum ingresso vinculado a este ID de show.")
            input("\nPressione Enter para continuar...")

        # Busca por Preço Máximo
        elif opcao == 3:
            preco_max = float(input("Exibir ingressos até qual preço? R$ "))
            encontrou = False
            
            for id_ing, ing in bilheteria.items():
                if ing['preco'] <= preco_max:
                    id_show = ing['id_show']
                    if id_show in shows.shows:
                        nome_show = obter_nome_show(id_show) 
                    else:
                        print("Show Desconhecido")

                    print(f"\nID Ingresso: {id_ing}\nShow: {nome_show}\nPreço: R${ing['preco']:.2f}\nQuantidade: {ing['qtd_disponivel']}\n")
                    encontrou = True
            
            if not encontrou:
                print(f"Nenhum ingresso encontrado abaixo de R$ {preco_max:.2f}")
            input("\nPressione Enter para continuar...")

        elif opcao == 0:
            break

        else:
            print("Opção desconhecida")


# Editar ingresso
def editar_ingresso():
    print("---Editor de Ingressos---")
    print()
    id_ingresso = int(input("ID do ingresso que deseja editar? "))
    
    if id_ingresso in bilheteria:
        # Exibe os shows para caso queira mudar o show do ingresso também
        print("Shows disponíveis:")
        for id_sh, sh in shows.shows.items():
            print(f"  {id_sh}. {sh['nome']}")
        print()
        
        id_show = int(input("Novo ID do show: "))
        
        if id_show in shows.shows:
            preco = float(input("Novo preço: "))
            qtd_disponivel = int(input("Nova quantidade disponível: "))

            ingresso = {
                'id_show': id_show,
                'preco': preco,
                'qtd_disponivel': qtd_disponivel
            }

            bilheteria[id_ingresso] = ingresso  # Atribui o valor do dicionário ingresso ao item do valor do id do "dicionario pai" bilheteria
            print("Ingresso editado com sucesso!")
        else:
            print("👺❌ Show informado não existe. Operação cancelada.")
    else:
        print("👺❌Ingresso não encontrado")
        

def excluir_ingresso():
    print("---Exclusão de Ingresso----")

    id_ingresso = int(input("Digite o ID do ingresso que você quer deletar: "))

    if id_ingresso in bilheteria:
        id_show = bilheteria[id_ingresso]['id_show']
        nome_show = obter_nome_show(id_show)

        validar = input(f"Quer mesmo deletar os ingressos do show: {nome_show}? (Digite sim se quiser apagar) ").lower()
        if validar == "sim":
            print("Excluindo...")
            sleep(1)
            del bilheteria[id_ingresso]
            print("Ingresso excluido com sucesso")

        else:
            print("Operação cancelada")

    else:
        print("Ingresso não encontrado")
        return 
    
def vender_ingresso():
    print("--- Venda de Ingressos ---")

    if not bilheteria: ##Verfiica se o dicionario está fazio
        print("Nenhum ingresso cadastrado no sistema")
        return
    exibir_shows_disponiveis()

    id_ingresso = int(input("\nDigite o ID do ingresso que você deseja comprar: "))

    if id_ingresso not in bilheteria:
        print("❌ Ingresso não encontrado")
        return
    ingresso = bilheteria[id_ingresso]

    if ingresso['qtd_disponivel'] == 0:
        print("❌ Ingressos esgotados para esse show. ")

    quantidade = int(input(f"Quantos ingressos? (disponíveis: {ingresso['qtd_disponivel']})"))

    if quantidade > ingresso['qtd_disponivel']:
        print(f"Quantidade indisponivel. Máximo: {ingresso['qtd_disponivel']}")
        return
    
    valor_total = quantidade * ingresso['preco']
    nome_show = obter_nome_show(ingresso['id_show'])

    confirmar = input(f"\nComfirmar compra de {quantidade} ingressos para '{nome_show}' por R$ {valor_total:.2f}? (sim/não): ").lower()
    
    if confirmar == 'sim':

        if vendas:
            novo_id_venda = max(vendas.keys())+1
            vendas[novo_id_venda] = {
        'id_ingresso': id_ingresso,
        'id_show': ingresso['id_show'],
        'quantidade': quantidade,
        'valor_total': valor_total
    }
        ingresso["qtd_disponivel"] -= quantidade

        print(f"✅Compra realizada! {quantidade} ingresso(s) para '{nome_show}'. Total: R$ {valor_total: .2f} ")
    
    else:
        print("❌Operação cancelada")



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
        
        opcao_bilheteria = int(input("Escolha uma opção: "))
        if opcao_bilheteria == 1:
            cadastrar_ingresso()

        elif opcao_bilheteria == 2:
            buscar_bilheteria()
        
        elif opcao_bilheteria == 3:
            editar_ingresso()

        elif opcao_bilheteria == 4:
            excluir_ingresso()

        elif opcao_bilheteria == 5:
            vender_ingresso()

        elif opcao_bilheteria == 0:
            print("Saindo do modulo...")
            sleep(1)
            break
        
        else:
            print("✋👺🚫Opção invalida, tente novamente")


if __name__ == "__main__":
    menu_bilheteria()