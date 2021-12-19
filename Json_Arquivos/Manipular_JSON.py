from Funcoes_JSON import*

inventaio = ler_arquivos("inventario_json.json")
opcao = chamarMenu()
while opcao >0 and opcao <3:
    if opcao == 1:
        print(registrar(inventaio, "inventario_json.json"))
    elif opcao ==2:
        exibir("inventario_json.json")
    opcao = chamarMenu()