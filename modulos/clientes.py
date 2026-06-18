from artistas import gerar_id

clientes = {}

def cadastrar_cliente():
    print("\n --- CADASTRAR CLIENTE")
    nome = str(input("Nome do Cliente: "))
    cpf = str(input("CPF do Cliente: "))
    telefone = str(input("Telefone do Cliente: "))
    cidade = str(input("Residencia do Cliente: "))
    historico_compras = str(input("Clientes fodas"))

    novo_id = gerar_id()

    clientes[novo_id] = {
        'nome': nome,
        'cpf': cpf,
        'telefone':telefone,
        'cidade':cidade,
        'historico_compras': []
        }

    return clientes

cadastrar_cliente()