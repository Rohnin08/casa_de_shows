def validar_email(email):
    if not email.strip():
        return False
    
    elif email.startswith(('.', '@')) or email.endswith(('.', '@')):
        return False
    
    elif not email.split('@'):
        return False
    
    if '@' not in email:
        return False
    
    if not '.' in email:
        return False

    else: 
        return True
    

while True:
    email = str(input("Digite um email: "))

    if not validar_email(email):
        print("Email ivalido")

    else:
        print("Email validado com sucesso!")
        break