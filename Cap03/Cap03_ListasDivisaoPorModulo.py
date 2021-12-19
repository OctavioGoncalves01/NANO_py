
def preenchimento_inventario(lista):
    pergunta = 'S'
    while pergunta == 'S':
        elemento = [input("Informe o nome do elemento:\t").upper(), 
                    int(input("Informe o número de serie:\t")),
                    float(input("Informe o valor do elemento:\tR$")), 
                    input("Informe o departamento que o corresponde").upper()]
        lista.appendo(elemento)
        pergunta = input("Deseja adcionar novos elementos: [S/N]").upper()

def exibir_inventario(lista):
    for elemento in lista:
        print("Nome................:\t", elemento[0])
        print("Serial..............:\t", elemento[1])
        print("Valor...............:\tR$", elemento[2])
        print("Departamento........:\t", elemento[3])

def localizar_item_por_nome(lista):
    nome = input("Digite o nome do elemento:\t").upper()
    for elemento in lista:
        if elemento[0] == nome:
            print("Nome............", elemento[0])
            print("Serial..........", elemento[1])
            print("Departamento....", elemento[3])

def desvalorizar_por_nome(lista, porc):
    nome = input("Digite o nome do elemento:\t").upper()
    for elemento in lista:
        if elemento[0] == nome:
            print("Nome............", elemento[0])
            print("Serial..........", elemento[1])
            print("Valor...........R$", elemento[2])
            elemento[2] = elemento[2] * (1-porc/100)
            print(f"Novo valor de {elemento[0]} reajustado para R${elemento[2]:.2f}")

def remover_por_serial(lista):
    serial = int(input("Informe o serial do itema a ser removido:\t"))
    for elemento in lista:
        if serial == elemento[1]:
            lista.remove(elemento)
    return "Item deletado com sucesso!!"

def resumir_valores(lista):
    valores = []
    for elementos in lista:
        valores.append(elementos[2])
    if len(valores) > 0:
        print(f"O item mais caro é:..................R${max(valores)}")
        print(f"O item mais barato é:................R${min(valores)}")
        print(f"O total dos valores dos iten é de:...R${sum(valores)}")