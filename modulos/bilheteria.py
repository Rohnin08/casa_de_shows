from time import sleep
import modulos.vendas as vendas
import modulos.ingressos as ingressos

# ──────────────────────────────────────────────
# MENU PRINCIPAL DO MÓDULO
# ──────────────────────────────────────────────

def menu_bilheteria():
    while True:
        print('''
=========================================
        Modulo de Bilheteria 
=========================================
    1. INGRESSOS 🎫

    2. VENDAS 💸
              
    0. SAIR DO MODULO 📤
=========================================
''')
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Valor invalido, por favor tente novamente")
            continue

        if opcao == 1:
            ingressos.menu_ingressos()

        elif opcao == 2:
            vendas.menu_vendas()
        
        elif opcao == 0:
            print("Saindo do modulo...")
            sleep(1)
            break

        else:
            print("✋👺🚫Opção invalida, tente novamente")


if __name__ == "__main__":
    menu_bilheteria()