import json
import os 

def chamarMenu():
    escolha = int(input("Digite:\n<1>para registrar ativo\n<2>para exibir ativos armazenados: "))
    return escolha

def ler_arquivos(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arq_json:
            dicionario = json.load(arq_json)
    else:
        dicionario = {}
    return dicionario

def gravar_arquivos(dicionario, arquivo):
    with open(arquivo, "w") as arq_json:
        json.dump(dicionario, arq_json)
    
def registrar(dicionario, arquivo):
    resp = 'S'
    while resp == 'S':
        dicionario[input("Digite o número patrimonial: ")] =[
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "), input("Digite o departamento: ").upper()]
        resp = input("Digite <S> para continuar: ").upper()
        gravar_arquivos(dicionario, arquivo)
    return "Arquivo JSON gerado!!"

def exibir(arquivo):
    dicionario = ler_arquivos(arquivo,)
    for chave, dado in dicionario.items():
        print("Data..................:", dado[0])
        print("Descrição.............:", dado[1])
        print("Departamento..........:", dado[2])
