from FuncoesArquivos import*
inventario = {}
opcao = chamarMenu()
while opcao > 0 and opcao < 4:
    if opcao == 1:
        resgistar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:
            lista = linha.split(";")
            print(" ")
            print("Data..................:\t", lista[1])
            print("Descrição.............:\t", lista[2])
            print("Departamento..........:\t", lista[3])
    opcao = chamarMenu()