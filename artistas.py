artistas = []

while True:
    print('''
====================
1. Adicionar artista
0. Parar
====================
''')
    op = int(input("O que você quer? "))

    if op == 1:
        nome = input("Nome do artista: ")
        cache = float(input("Valor o cache: "))
        genero_musical = input("Genero músical: ")

        artista = {
            "nome": nome,
            "cache" : cache,
            "genero_musical": genero_musical

        }

        artistas.append(artista)
        print("Artista cadastrado com sucesso👌")
    elif op == 0:
         break

for artista in artistas:
    print(f"Nome: {artista['nome']}|Cache: {artista['cache']}| Gênero:{artista['genero_musical']}\n")

