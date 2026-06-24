from time import sleep
import modulos.storage as storage
import modulos.clientes as clientes
import modulos.artistas as artistas
import modulos.shows as shows
import modulos.ingressos as ingressos
import modulos.geral as g

# ──────────────────────────────────────────────
# INICIALIZAÇÃO
# ──────────────────────────────────────────────

bilheteria = storage.carregar("bilheteria")
vendas = storage.carregar("vendas")

if not vendas:
    vendas = {

    }
    storage.salvar("vendas", vendas)

def exibir_shows_disponiveis():
    '''Exibe os shows disponiveis'''
    print("---Shows Disponiveis---\n")
    for id_ing, ing in ingressos.items():
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

# Cadastrar Venda
def cadastrar_venda():
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
    nome_show = ingressos.obter_nome_show(ingresso['id_show'])

    confirmar = input(f"\nConfirmar venda de {quantidade} ingressos para o '{nome_show}' por R$ {valor_total:.2f}? (sim/não): ").lower()

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
    

def buscar_venda():
    pass

def editar_venda():
    pass

def cancelar_venda():
    pass


def menu_vendas():
     while True:

        print('''
=========================================
          Vendas 💰
=========================================
    1. Cadastrar Vendas
              
    2. Listar/Buscar Vendas
              
    3. Editar Vendas
              
    4. Excluir Vendas
              
    0. Sair do Modulo
=========================================
''')
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Valor invalido, por favor tente novamente")
            continue

        if opcao == 1:
            cadastrar_venda()
        elif opcao == 2:
            buscar_venda()
        elif opcao == 3:
            editar_venda()
        elif opcao == 4:
            cancelar_venda()
        elif opcao == 0:
            print("Saindo...")
            sleep(1)
            break



# ──────────────────────────────────────────────
# MENU PRINCIPAL DO MÓDULO
# ──────────────────────────────────────────────
