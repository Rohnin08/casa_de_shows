from datetime import datetime
from time import sleep
import modulos.storage as storage
import modulos.clientes as clientes
import modulos.artistas as artistas
import modulos.shows as shows
import modulos.ingressos as ingressos
import modulos.geral as g
from modulos.geral import limpar_tela


# ──────────────────────────────────────────────
# INICIALIZAÇÃO
# ──────────────────────────────────────────────

vendas = storage.carregar("vendas")

if not vendas:
    vendas = {}

    storage.salvar("vendas", vendas)

def exibir_venda(id_venda):
    '''Exibe os dados das vendas'''
    venda = vendas[id_venda]
    id_ing = venda['id_ingresso']
    id_show = venda['id_show']
    id_cli = venda['id_cliente']

    if id_show in shows.shows:
        nome_show = shows.shows[id_show]['nome']
    else:
        nome_show = "Show Desconhecido"
    
    if id_cli in clientes.clientes:
        nome_cliente = clientes.clientes[id_cli]['nome']
    else:
        nome_cliente = "Cliente Desconhecido"
    
    if venda['aprovado']:
        status = "Aprovada"
    else:
        status = "Cancelada"
    
    print(f'''
ID da Venda: {id_venda}
Cliente: {nome_cliente} (ID:{id_cli})
Show: {nome_show} (ID: {id_show})
ID Ingresso: {id_ing}
Quantidade: {venda['quantidade']}
Valor Total: R$ {venda['quantidade']:.2f}
Horário: {venda['horario'].strftime('%d/%m/%Y %H:%M')}
Status: {status}
-------------------------------------------
''')
    
def exibir_clientes_disponiveis():
    '''Lista clientes ativos'''
    print("\nClientes cadastrados:")
    for id_cli, dados in clientes.clientes.items():
        if dados['cadastrado']:
            print(f"  {id_cli}. {dados['nome']}")

def exibir_shows_disponiveis():
    '''Exibe os shows disponiveis e o ingresso'''
    print("---Shows Disponiveis---\n")
    for id_ing, ing in ingressos.ingressos.items():
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
    '''Registra uma nova venda, desconta estoque e atualiza histórico do cliente'''  
    print("--- Nova Venda ---")

    if not ingressos.ingressos:
        print("Nenhum ingresso cadastrado no sistema")
        return

    exibir_clientes_disponiveis()

    while True:
        try: 
            id_cli = int(input("ID do Cliente: "))
            break
        except ValueError:
            print("⚠️ ID inválido, tente novamente")
    
    if id_cli not in clientes.clientes or not clientes.clientes[id_cli]['cadastrado']:
        print("❌ Cliente não encontrado")
        return # Volta para o menu anterior
    
    exibir_shows_disponiveis()
        
    while True:
        try:
            id_ing = int(input("\nDigite o ID do ingresso que você deseja comprar: "))
            break
        except ValueError:
            print("⚠️ ID invalido, tente novamente")
            

    if id_ing not in ingressos.ingressos:
        print("❌ Ingresso não encontrado")
        return

    ing = ingressos.ingressos[id_ing]

    if ing['qtd_disponivel'] == 0:
        print("❌ Ingressos esgotados para esse show.")
        return

    while True: 
        try:
            quantidade = int(input(f"Quantos ingressos? (disponíveis: {ing['qtd_disponivel']}) "))

            if quantidade < 0:
                print("⚠️ A quantidade deve ser maior que zero.")
                continue

            if quantidade > ing['qtd_disponivel']:
                print(f"Quantidade indisponivel. Máximo: {ing['qtd_disponivel']}")
                continue
            break    
        except ValueError:
            print("⚠️ Valor invalido, tente novamente")

    # Calcular o valor final da venda.
    valor_total = quantidade * ing['preco']
    id_show = ing['id_show']

    if id_show in shows.shows:
        nome_show = shows.shows[id_show]['nome']
    else:
        return "Show não encontrado"
    nome_cliente = clientes.clientes[id_cli]['nome']

    print(f'''
\n
Resumo da venda:
Cliente : {nome_cliente}
Show    : {nome_show}
Qtd     : {quantidade}
Total   : R$ {valor_total:.2f}
          
          ''')
    

    confirmar = input(f"\nConfirmar venda de {quantidade} ingressos para o '{nome_show}' por R$ {valor_total:.2f}? (sim/não): ").lower()

    if confirmar != 'sim':
       print("❌ Operação Cancelada.")
       return
    
    # Registrar venda
    novo_id = g.gerar_id(vendas)
    vendas[novo_id] = {
        'id_ingresso': id_ing,
        'id_show': id_show,
        'id_cliente': id_cli,
        'quantidade': quantidade,
        'valor_total': valor_total,
        'horario': datetime.now(),
        'aprovado': True
    }

    # Descontar estoque
    ingressos.ingressos[id_ing]['qtd_disponivel'] -= quantidade
    storage.salvar("ingressos", ingressos.ingressos)

    # Atualizar histórico do cliente
    clientes.clientes[id_cli]['historico_compras'].append(novo_id)
    storage.salvar("clientes", clientes.clientes)

    storage.salvar("vendas", vendas)
    print(f"\n✅ Venda registrada com sucesso! (ID: {novo_id})")


def buscar_venda():
    '''Busca vendas por diferentes critérios'''
    while True:
        print('''
---------------------------------------
         Buscador de Vendas
---------------------------------------
  1. Buscar por ID da Venda
  2. Buscar por Cliente
  3. Buscar por Show
  0. Voltar
''')
        try:
            opcao = int(input("Qual a opção? "))
        except ValueError:
            print("⚠️ Valor inválido, tente novamente.")
            continue

        if opcao == 1:
            while True:
                try:
                    id_venda = int(input("ID da venda: "))
                    break
                except ValueError:
                    print("⚠️ ID inválido, tente novamente.")

            if id_venda in vendas:
                exibir_venda(id_venda)
            else:
                print("❌ Venda não encontrada.")
            input("\nPressione Enter para continuar...")

        elif opcao == 2:
            exibir_clientes_disponiveis()
            while True:
                try:
                    id_cli = int(input("\nID do cliente: "))
                    break
                except ValueError:
                    print("⚠️ ID inválido, tente novamente.")

            encontrou = False
            for id_venda, venda in vendas.items():
                if venda['id_cliente'] == id_cli:
                    exibir_venda(id_venda)
                    encontrou = True
            if not encontrou:
                print("❌ Nenhuma venda encontrada para este cliente.")
            input("\nPressione Enter para continuar...")

        elif opcao == 3:
            print("\nShows cadastrados:")
            for id_show, show in shows.shows.items():
                if show['cadastrado']:
                    print(f"  {id_show}. {show['nome']}")

            while True:
                try:
                    id_show = int(input("\nID do show: "))
                    break
                except ValueError:
                    print("⚠️ ID inválido, tente novamente.")

            encontrou = False
            for id_venda, venda in vendas.items():
                if venda['id_show'] == id_show:
                    exibir_venda(id_venda)
                    encontrou = True
            if not encontrou:
                print("❌ Nenhuma venda encontrada para este show.")
            input("\nPressione Enter para continuar...")

        elif opcao == 0:
            break

        else:
            print("⚠️ Opção desconhecida.")

def editar_venda():
    '''Edita quantidade ou cliente de uma venda, reajustando estoque e histórico'''
    print("--- Editar Venda ---")

    while True:
        try:
            id_venda = int(input("ID da venda que deseja editar: "))
            break
        except ValueError:
            print("⚠️ ID inválido, tente novamente.")

    if id_venda not in vendas or not vendas[id_venda]['aprovado']:
        print("❌ Venda não encontrada ou já cancelada.")
        return

    venda = vendas[id_venda]
    exibir_venda(id_venda)

    # Editar cliente
    exibir_clientes_disponiveis()
    print(f"  (Enter para manter cliente atual: {clientes.clientes[venda['id_cliente']]['nome']})")
    entrada = input("\nNovo ID do cliente: ").strip()

    if entrada:
        while True:
            try:
                novo_id_cli = int(entrada)
                break
            except ValueError:
                entrada = input("⚠️ ID inválido, tente novamente: ").strip()

        if novo_id_cli not in clientes.clientes or not clientes.clientes[novo_id_cli]['cadastrado']:
            print("❌ Cliente não encontrado.")
            return
    else:
        novo_id_cli = venda['id_cliente']

    # Editar quantidade
    ing = ingressos.ingressos[venda['id_ingresso']]
    estoque_atual = ing['qtd_disponivel'] + venda['quantidade']  # estoque real sem a venda atual
    print(f"\n  (Enter para manter quantidade atual: {venda['quantidade']})")
    print(f"  Estoque disponível para esta venda: {estoque_atual}")
    entrada = input("Nova quantidade: ").strip()

    if entrada:
        while True:
            try:
                nova_qtd = int(entrada)
                if nova_qtd <= 0:
                    entrada = input("⚠️ Quantidade deve ser maior que zero: ").strip()
                    continue
                if nova_qtd > estoque_atual:
                    entrada = input(f"⚠️ Máximo disponível: {estoque_atual}. Tente novamente: ").strip()
                    continue
                break
            except ValueError:
                entrada = input("⚠️ Valor inválido, tente novamente: ").strip()
    else:
        nova_qtd = venda['quantidade']

    novo_valor = nova_qtd * ing['preco']

    confirmar = input(f"\nConfirmar edição? Novo total: R$ {novo_valor:.2f} (sim/não): ").lower()
    if confirmar != "sim":
        print("Operação cancelada.")
        return

    # Atualizar histórico se cliente mudou
    if novo_id_cli != venda['id_cliente']:
        clientes.clientes[venda['id_cliente']]['historico_compras'].remove(id_venda)
        clientes.clientes[novo_id_cli]['historico_compras'].append(id_venda)
        storage.salvar("clientes", clientes.clientes)

    # Reajustar estoque
    ing['qtd_disponivel'] = estoque_atual - nova_qtd
    storage.salvar("ingressos", ingressos.ingressos)

    # Atualizar venda
    vendas[id_venda]['id_cliente'] = novo_id_cli
    vendas[id_venda]['quantidade'] = nova_qtd
    vendas[id_venda]['valor_total'] = novo_valor
    storage.salvar("vendas", vendas)
    print("✅ Venda editada com sucesso!")

def cancelar_venda():
    '''Cancela uma venda, devolve estoque e remove do histórico do cliente'''
    print("--- Cancelar Venda ---")

    while True:
        try:
            id_venda = int(input("ID da venda que deseja cancelar: "))
            break
        except ValueError:
            print("⚠️ ID inválido, tente novamente.")

    if id_venda not in vendas or not vendas[id_venda]['aprovado']:
        print("❌ Venda não encontrada ou já cancelada.")
        return

    exibir_venda(id_venda)
    confirmar = input("Confirmar cancelamento? (sim/não): ").lower()
    if confirmar != "sim":
        print("Operação cancelada.")
        return

    venda = vendas[id_venda]

    # Devolver estoque
    ingressos.ingressos[venda['id_ingresso']]['qtd_disponivel'] += venda['quantidade']
    storage.salvar("ingressos", ingressos.ingressos)

    # Remover do histórico do cliente
    clientes.clientes[venda['id_cliente']]['historico_compras'].remove(id_venda)
    storage.salvar("clientes", clientes.clientes)

    # Soft delete
    vendas[id_venda]['aprovado'] = False
    storage.salvar("vendas", vendas)
    print("✅ Venda cancelada com sucesso!")

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
        else:
            print("✋👺 Opcão invalida!")