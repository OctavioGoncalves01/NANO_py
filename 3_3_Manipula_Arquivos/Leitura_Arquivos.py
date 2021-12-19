with open("Teste.txt", "r") as arquivo:
    conteudo = arquivo.readline()
print("Tipo de dado da variável", type(conteudo))
print("Conteúdo do arquivo:", conteudo)