from time import sleep


artistas = {
    1: {'nome': 'Slipknot',    'cache': 1000.00, 'genero': 'Metal'},
    2: {'nome': 'Linkin Park', 'cache': 1500.00, 'genero': 'Nu Metal'},
    3: {'nome': 'Limp Bizkit', 'cache': 1200.00, 'genero': 'Nu Metal'}
}


# ──────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────

def _proximo_id():
    """Retorna um ID único mesmo após deleções."""
    if artistas:
        return max(artistas.keys()) + 1
    else:
        return 1


def _exibir_artista(id_art, dados):
    print(f"  ID: {id_art} | Nome: {dados['nome']} | Cache: R${dados['cache']:.2f} | Gênero: {dados['genero']}")


# ──────────────────────────────────────────────
# CRUD
# ──────────────────────────────────────────────

def cadastrar_artista(): 
    """ Função para cadastrar os artistas, ela pega os valores digitados pelo usuário e associa-os a chaves dos dicionarios."""
    print("\n--- CADASTRAR ARTISTA ---")
    nome   = input("Nome do artista: ")
    cache  = float(input("Cache do artista: R$ "))
    genero = input("Gênero musical: ")

    novo_id = _proximo_id()
    artistas[novo_id] = {'nome': nome, 'cache': cache, 'genero': genero}
    print(f"\n✅ {nome} cadastrado com sucesso! (ID: {novo_id})")


def exibir_todos():
    if not artistas:
        print("\n⚠️  Nenhum artista cadastrado.")
        return
    print("\n--- LISTA DE ARTISTAS ---")
    for id_art, dados in artistas.items():
        _exibir_artista(id_art, dados)


def buscar_artistas():
    """Função "guarda-chuva" dos filtros de busca da opção de busca"""
    while True:
        print('''
=========================================
         Buscador de Artistas
=========================================
  1. Buscar por ID
  2. Buscar por Nome
  3. Buscar por Gênero
  4. Buscar por Cache (até um valor)
  0. Voltar
=========================================''')

        opcao = int(input("Qual a opção? "))

        if opcao == 1:
            id_art = int(input("ID do artista: "))
            if id_art in artistas:
                _exibir_artista(id_art, artistas[id_art])
            else:
                print("❌ Artista não encontrado.")

        elif opcao == 2:
            termo = input("Nome (ou parte dele): ").lower()
            resultado = []
            for i, d in artistas.items():
                if termo in d['nome'].lower():
                    resultado.append((i, d))
            if resultado:
                for id_art, dados in resultado:
                    _exibir_artista(id_art, dados)
            else:
                print("❌ Nenhum artista encontrado com este nome.")

        elif opcao == 3:
            genero_busca = input("Gênero musical: ").lower()
            resultado = []
            for i, d in artistas.items():
                if genero_busca == d['genero'].lower():
                    resultado.append((i, d))
            if resultado:
                for id_art, dados in resultado:
                    _exibir_artista(id_art, dados)
            else:
                print("❌ Nenhum artista encontrado neste gênero.")

        elif opcao == 4:
            cache_limite = float(input("Exibir artistas com cache até: R$ "))
            resultado = []
            for i, d in artistas.items():
                if d['cache'] <= cache_limite:
                    resultado.append((i, d))
            if resultado:
                for id_art, dados in resultado:
                    _exibir_artista(id_art, dados)
            else:
                print("❌ Nenhum artista encontrado nessa faixa de cache.")

        elif opcao == 0:
            break

        else:
            print("⚠️  Opção inválida.")

        input("\nPressione Enter para continuar...")


def editar_artista():
    '''Captura o ID digitado procura no dicionario e '''
    print("\n--- EDITAR ARTISTA ---")
    id_artista = int(input("ID do artista que deseja editar: "))

    if id_artista not in artistas:
        print("❌ Artista não encontrado.")
        return

    atual = artistas[id_artista]
    print(f"Editando: {atual['nome']} | Cache: R${atual['cache']:.2f} | Gênero: {atual['genero']}")
    print("(Deixe em branco para manter o valor atual)\n")


    nome   = input(f"Novo nome [{atual['nome']}]: ").strip() #Esse strip vai limpar os espaços em branco para garantir que o usuário digitou alguma coisa se ele não digitou nada
    cache_str = input(f"Novo cache [{atual['cache']:.2f}]: ").strip() #Mesma coisa da linha anterior
    genero = input(f"Novo gênero [{atual['genero']}]: ").strip() #Idem

    if nome:
        novo_nome = nome
    else:
        novo_nome = atual['nome']

    if cache_str:
        novo_cache = float(cache_str)
    else:
        novo_cache = atual['cache']

    if genero:
        novo_genero = genero
    else:
        novo_genero = atual['genero']

    artistas[id_artista] = {
        'nome':   novo_nome,
        'cache':  novo_cache,
        'genero': novo_genero
    }
    print("✅ Artista atualizado com sucesso!")


def excluir_artista():
    print("\n--- EXCLUIR ARTISTA ---")
    id_artista = int(input("ID do artista que deseja excluir: "))

    if id_artista not in artistas:
        print("❌ Artista não encontrado.")
        return

    confirmar = input(f"Tem certeza que quer deletar '{artistas[id_artista]['nome']}'? (sim/não): ").lower()
    if confirmar == "sim":
        print("Excluindo...")
        sleep(1)
        del artistas[id_artista]
        print("✅ Artista excluído com sucesso!")
    else:
        print("Operação cancelada.")


# ──────────────────────────────────────────────
# MENU PRINCIPAL DO MÓDULO
# ──────────────────────────────────────────────

def menu_artistas():
    while True:
        print('''
=========================================
          Módulo de Artistas
=========================================
  1. Cadastrar Artista
  2. Listar Todos
  3. Buscar Artista
  4. Editar Artista
  5. Excluir Artista
  0. Sair do Módulo
=========================================''')

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_artista()
        elif opcao == 2:
            exibir_todos()
        elif opcao == 3:
            buscar_artistas()
        elif opcao == 4:
            editar_artista()
        elif opcao == 5:
            excluir_artista()
        elif opcao == 0:
            print("Saindo do módulo...")
            sleep(1)
            break
        else:
            print("✋👺🚫 Opção inválida!")


if __name__ == "__main__":
    menu_artistas()