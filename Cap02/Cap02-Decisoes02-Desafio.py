nivel = input("Digite seu nivel de acesso:  ").upper()
genero = input("Digite seu genero: [F/M]    ").upper()
if nivel == 'ADM' or nivel == 'USR':
    if nivel == 'ADM':    
        if genero == 'F':
            print("Olá Administradora")
        else:
            print("Olá Administrador")
    elif nivel == 'USR':    
        if genero == 'F':
            print("Olá Usuária")
        else:
            print("Olá Usuário")
elif nivel == 'GUEST':
    print("Olá Visitante")
else:
    print("Olá Desconhecido")