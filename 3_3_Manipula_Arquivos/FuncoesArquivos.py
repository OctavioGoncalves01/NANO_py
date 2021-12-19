def chamarMenu():
    print("")
    escolha = int(input("Digite para:\n<1> para registrar ativo\n" + 
                    "<2> para persistir em arquivo\n" + 
                    "<3> para exibir ativos armazenados:\n<>"))
    return escolha

def resgistar(dicionario):
    resp = 'S'
    while resp =='S':
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        dicionario[input("digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "),
            input("digite o departamento: ")]
        resp = input("Digite <S> para continuar: ").upper()

def persistir(dicionario):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" +
                     valor[1] + ";" + valor[2] + "\n")
        return "Persistido com sucesso!"

def exibir():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    with open("inventario.csv", "r") as inv:
        linhas = inv.readlines()
    return linhas