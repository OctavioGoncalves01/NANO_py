equipamentos = []
valores = []
serials = []
departamentos = []
pergunta = 'S'
while pergunta == 'S':
    equipamentos.append(input("Equipamento:\t"))
    valores.append(float(input("Valor:\tR$")))
    serials.append(int(input("Número serial:\t")))
    departamentos.append(input("Departamento:\t"))
    pergunta = input("Deseja continuar [s/n]\n").upper()

for item in range(0, len(equipamentos)):
    print("-----------------------------")
    print("Equipamento....: ", (item+1))
    print("Nome...........: ", equipamentos[item])
    print("Valor..........: ", valores[item])
    print("Serial.........: ", serials[item])
    print("Departamento...: ", departamentos[item])


busca = input("Digite o nome do equipamento que deseja buscar:\t")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Valor.....:", valores[indice])
        print("Serial....:", serials[indice])


desvalorizar = input("Digite o nome do equipamento que será desvalorizado: ")
for indice in range(0,len(equipamentos)):
    if desvalorizar == equipamentos[indice]:
        print("Valor antigo: ", valores[indice])
        valores[indice] = valores[indice] * 0.9
        print(f"Novo valor:  {valores[indice]:2f}")


deletar = int(input("Digite o número do equipamento para ser deletado: "))
for indice in range(0,len(serials)):
    if deletar == serials[indice]:
        del serials[indice]
        del equipamentos[indice]
        del departamentos[indice]
        del valores[indice]
        break

for item in range(0, len(equipamentos)):
    print("Equipamentos.........: ", (item+1))
    print("Nome...........: ", equipamentos[item])
    print("Valor..........: ", valores[item])
    print("Serial.........: ", serials[item])
    print("Departamento...: ", departamentos[item])