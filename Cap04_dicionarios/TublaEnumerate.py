usuarios = {}
pergunta = 'S'
emails = []
while pergunta == 'S':
    emails.append(input("Digite um e-mail: ").lower())
    pergunta = input("Digite <S> para contuniar: ").upper()

tupla = list(enumerate(emails))
for chave in range(0, len(tupla)):
    print("E-mail: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome: "), input("Digite o nível de acesso: ")]

for chave, dado in usuarios.items():
    print("Usuário.........:", chave[0])
    print("E-mail..........:", chave[1])
    print("Nome............:", dado[0])
    print("Nível...........:", dado[1])