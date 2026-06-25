from datetime import date, time
from time import sleep
import modulos.storage as storage
import modulos.artistas as artistas
import modulos.geral as g
from modulos.geral import limpar_tela


# ──────────────────────────────────────────────
# INICIALIZAÇÃO
# ──────────────────────────────────────────────

shows = storage.carregar("shows")

if not shows:
    shows = {
        1: {
            'nome': 'Metal Fest',
            'lineup': [1, 2],
            'hora_inicio': time(20, 0),
            'hora_termino': time(23, 30),
            'data': date(2025, 7, 15),
            'cadastrado': True
        }
    }
    storage.salvar("shows", shows)

# HELPERS
def verificar_conflito(data, hora_inicio, hora_termino, ignorar_id=None):
    '''Função para verificar conflitos de horario entre shows'''
    for id_show, dados in shows.items(): # Itera o dicionario
        if id_show == ignorar_id or not dados['cadastrado']: # Verifica o status de cadastro dele
            continue
        if dados['data'] == data: # Verifica se os dados de data são iguais ao de algum outro show cadastrado
            # Se o horario de inicio for maior que o que tiver cadastrado no arquivo e o horario de termino for menor que o de inicio do arquivo ele retorna 'True'
            if hora_inicio < dados['hora_termino'] and hora_termino > dados['hora_inicio']:
                return True  # há conflito
    return False # Se não achar nada, Ok

# EXIBIR SHOW
def exibir_show(id_show):
    show = shows[id_show]
    nomes_lineup = []
    for id_art in show['lineup']:  # ← trocado id_show por id_art, evita sobrescrever o parâmetro
        if id_art in artistas.artistas and artistas.artistas[id_art]['cadastrado']:
            nomes_lineup.append(artistas.artistas[id_art]['nome'])

    print(f"""
  ID do Show: {id_show}
  Nome:       {show['nome']}
  Data:       {show['data'].strftime('%d/%m/%Y')}
  Início:     {show['hora_inicio'].strftime('%H:%M')}
  Término:    {show['hora_termino'].strftime('%H:%M')}
  Lineup:     {', '.join(nomes_lineup) if nomes_lineup else 'Nenhum artista vinculado'}
  ---------------------------------------""") # Tive que usar operador ternario aqui

# ──────────────────────────────────────────────
# CRUD
# ──────────────────────────────────────────────

# CADASTRAR SHOW
def cadastrar_show():
    '''Função de cadastrar show'''
    print("--- Cadastro de Shows ---")
    print()
    novo_id = g.gerar_id(shows)
    nome = input("Nome do show: ")

    print("\nArtistas disponíveis:")
    for id_art, artista in artistas.artistas.items():
        if artista['cadastrado']:
            print(f"  {id_art}. {artista['nome']}")

    lineup = []
    while True:
        try:
            id_art = int(input("\nDigite o ID do artista para adicionar ao lineup (ou 0 para terminar): "))
        except ValueError:
            print("⚠️ ID inválido, tente novamente.")
            continue

        if id_art == 0:
            break
        elif id_art in artistas.artistas and artistas.artistas[id_art]['cadastrado']:
            if id_art not in lineup:
                lineup.append(id_art)
                print(f"{artistas.artistas[id_art]['nome']} adicionado ao lineup.")
            else:
                print("Esse artista já está no lineup.")
        else:
            print("Artista não encontrado.")

    try:
        hora_inicio  = time(*map(int, input("Horário de início (HH MM): ").split()))
        hora_termino = time(*map(int, input("Horário de término (HH MM): ").split()))
        data         = date(*map(int, input("Data (AAAA MM DD): ").split()))
    except ValueError:
        print("❌ Data ou horário inválido.")
        return

    if verificar_conflito(data, hora_inicio, hora_termino):
        print("❌ Já existe um show agendado nessa data/horário.")
        return

    shows[novo_id] = {
        'nome': nome,
        'lineup': lineup,
        'hora_inicio': hora_inicio,
        'hora_termino': hora_termino,
        'data': data,
        'cadastrado': True
    }
    storage.salvar("shows", shows)
    print(f"\n✅ Show '{nome}' cadastrado com sucesso!")

# BUSCAR SHOW
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
        try:
            opcao = int(input("Qual a opção? "))
        except ValueError:
            print("⚠️ Valor inválido, tente novamente.")
            continue

        if opcao == 1:
            while True:
                try:
                    id_show = int(input("ID do show: "))
                    break
                except ValueError:
                    print("⚠️ ID inválido, tente novamente.")

            if id_show in shows and shows[id_show]['cadastrado']:
                exibir_show(id_show)
            else:
                print("❌ Show não encontrado.")
            input("\nPressione Enter para continuar...")

        elif opcao == 2:
            termo = input("Digite o nome do show (ou parte dele): ").lower()
            encontrados = False
            print("\n--- Resultados da Busca ---")
            for id_show, dados in shows.items():
                if termo in dados['nome'].lower() and dados['cadastrado']:
                    exibir_show(id_show)
                    encontrados = True
            if not encontrados:
                print("❌ Nenhum show encontrado com esse nome.")
            input("\nPressione Enter para continuar...")

        elif opcao == 3:
            print("\n--- Todos os Shows Agendados ---")
            encontrados = False
            for id_show, dados in shows.items():
                if dados['cadastrado']:
                    exibir_show(id_show)
                    encontrados = True
            if not encontrados:
                print("Nenhum show cadastrado ainda.")
            input("\nPressione Enter para continuar...")

        elif opcao == 0:
            break

        else:
            print("Opção desconhecida.")

# EDITAR SHOW
def editar_show():
    print("--- Editor de Shows ---")

    while True:
        try:
            id_show = int(input("ID do show que deseja editar: "))
            break
        except ValueError:
            print("⚠️ ID inválido, tente novamente.")

    if id_show not in shows or not shows[id_show]['cadastrado']:
        print("❌ Show não encontrado.")
        return

    nome = input("Novo nome: ")

    print("\nArtistas disponíveis:")
    for id_art, artista in artistas.artistas.items():
        if artista['cadastrado']:
            print(f"  {id_art}. {artista['nome']}")

    lineup = []
    while True:
        try:
            id_art = int(input("Digite o ID do artista (ou 0 para terminar): "))
        except ValueError:
            print("⚠️ ID inválido, tente novamente.")
            continue

        if id_art == 0:
            break
        elif id_art in artistas.artistas and artistas.artistas[id_art]['cadastrado']:
            if id_art not in lineup:
                lineup.append(id_art)
                print(f"{artistas.artistas[id_art]['nome']} adicionado ao lineup.")
            else:
                print("Esse artista já está no lineup.")
        else:
            print("Artista não encontrado.")

    try:
        hora_inicio  = time(*map(int, input("Novo horário de início (HH MM): ").split()))
        hora_termino = time(*map(int, input("Novo horário de término (HH MM): ").split()))
        data         = date(*map(int, input("Nova data (AAAA MM DD): ").split()))
    except ValueError:
        print("❌ Data ou horário inválido.")
        return

    if verificar_conflito(data, hora_inicio, hora_termino, ignorar_id=id_show):
        print("❌ Já existe um show agendado nessa data/horário.")
        return

    shows[id_show] = {
        'nome': nome,
        'lineup': lineup,
        'hora_inicio': hora_inicio,
        'hora_termino': hora_termino,
        'data': data,
        'cadastrado': True
    }
    storage.salvar("shows", shows)
    print("✅ Show editado com sucesso!")

# EXCLUIR SHOW
def excluir_show():
    print("--- Exclusão de Show ---")

    while True:
        try:
            id_show = int(input("ID do show que deseja excluir: "))
            break
        except ValueError:
            print("⚠️ ID inválido, tente novamente.")

    if id_show not in shows or not shows[id_show]['cadastrado']:
        print("❌ Show não encontrado.")
        return

    validar = input(f"Quer mesmo excluir '{shows[id_show]['nome']}'? (Digite sim para confirmar): ").lower()
    if validar == "sim":
        print("Excluindo...")
        sleep(1)
        shows[id_show]['cadastrado'] = False
        storage.salvar("shows", shows)
        print("✅ Show desabilitado com sucesso.")
    else:
        print("Operação cancelada.")


# ──────────────────────────────────────────────
# MENU PRINCIPAL DO MÓDULO
# ──────────────────────────────────────────────

def menu_shows():
    while True:
        print('''
=========================================
            Modulo de Shows
=========================================
    1. Cadastrar Show
    2. Buscar Show
    3. Editar Show
    4. Excluir Show
    0. Sair do Módulo
=========================================
''')
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("⚠️ Valor invalido, por favor tente novamente")
            continue

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