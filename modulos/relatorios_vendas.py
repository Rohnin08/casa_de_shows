from datetime import datetime
import modulos.vendas as vendas
import modulos.clientes as clientes
import modulos.shows as shows
from modulos.geral import limpar_tela

# VENDAS POR DATA
def relatorio_vendas_por_data():
    '''Exibe todas as vendas realizadas em uma data específica'''
    print("=== Relatório de Vendas por Data ===\n")

    try:
        data_busca = datetime.strptime(input("Digite a data (DD/MM/AAAA): "), "%d/%m/%Y").date()
    except ValueError:
        print("❌ Data inválida.")
        return

    encontrou = False
    total_vendas = 0
    total_valor = 0.0

    for id_venda, venda in vendas.vendas.items():
        if venda['horario'].date() == data_busca:
            vendas.exibir_venda(id_venda)
            encontrou = True
            if venda['aprovado']:
                total_vendas += 1
                total_valor += venda['valor_total']

    if not encontrou:
        print(f"❌ Nenhuma venda encontrada para {data_busca.strftime('%d/%m/%Y')}.")
        return

    print(f"""
========================================
  Resumo do dia {data_busca.strftime('%d/%m/%Y')}
  Vendas aprovadas : {total_vendas}
  Receita total    : R$ {total_valor:.2f}
========================================
""")
    

#VENDAS POR VALOR
def relatorio_vendas_por_valor():
    '''Exibe todas as vendas acima de um valor mínimo'''
    print("=== Relatório de Vendas por Valor ===\n")

    try:
        valor_minimo = float(input("Digite o valor mínimo (ex: 100.00): ").replace(',', '.'))
    except ValueError:
        print("❌ Valor inválido.")
        return

    if valor_minimo < 0:
        print("❌ O valor deve ser positivo.")
        return

    encontrou = False
    total_vendas = 0
    total_valor = 0.0

    for id_venda, venda in vendas.vendas.items():
        if venda['aprovado'] and venda['valor_total'] >= valor_minimo:
            vendas.exibir_venda(id_venda)
            encontrou = True
            total_vendas += 1
            total_valor += venda['valor_total']

    if not encontrou:
        print(f"❌ Nenhuma venda encontrada acima de R$ {valor_minimo:.2f}.")
        return

    print(f"""
========================================
  Vendas acima de R$ {valor_minimo:.2f}
  Total de vendas  : {total_vendas}
  Receita total    : R$ {total_valor:.2f}
  Ticket médio     : R$ {total_valor / total_vendas:.2f}
========================================
""")
    

def menu_relatorios():
    while True:
        print('''
=========================================
         Relatórios de Vendas 📋
=========================================
  1. Vendas por data
  2. Vendas acima de um valor
  3. Vendas abaixo de um valor
  0. Voltar
=========================================
''')
        
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError: 
            print("⚠️ Opção invalida, tente novamente. ")
            continue

        if opcao == 1:
                limpar_tela()
                relatorio_vendas_por_data()
                input("\nEnter para continuar...")
                
        elif opcao == 2:
            limpar_tela()
            relatorio_vendas_por_valor()
            input("\nEnter para continuar...")

        elif opcao == 0:
            break

        else:
                print("⚠️ Opção inválida.")