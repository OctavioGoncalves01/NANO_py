def perguntar():
    resposta = input("\tO que deseja fazer?\n<I> - Incerir um usuario\n<P> - Pesquisar\n<E> - Excluir um usuario\n<L> - Listar usuario\n").upper()
    return resposta

def incerir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                    input("Digite a última data de acesso: "),
                                                    input("Qual a última estação acessada: ").upper()]

def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome..............:\t" + lista[0])
        print("Último acesso.....:\t" + lista[1])
        print("Última estação....:\t" + lista[2])

def apagar(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto........:")
        print("Login:........", chave)
        print("Dado..........", valor)