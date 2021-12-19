from Funcoes.Funcoes_dicionarios import *
usuarios = {}

opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        incerir(usuarios)
    if opcao == "P":
        pesquisar(usuarios, input("Digite o logindo usuario para ser pesquisado:\t"))
    if opcao == "E":
        apagar(usuarios, input("Digite o login do usuario que será excluido:\t"))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar