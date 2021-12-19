inventario = []
resposta = 'S'
while resposta == 'S':
    equipamento = [input("Equipamento: ").upper(), float(input("Valor: R$")),
                    int(input("Número de serie: ")), input("Departamento: ").upper()]
    inventario.append(equipamento)
    resposta = input("Deseja continuar: [S/N]\n").upper()

for elemento in inventario:
    print("----------------------------------")
    print("Nome..............:\t", elemento[0])
    print("Valor.............:\tR$", elemento[1])
    print("Serial............:\t", elemento[2])
    print("Departamento......:\t", elemento[3])

#Irá realizar a busca por um equipamento atraves de seu nome
busca = input("Digite o NOME do equipamento que será buscado: ").upper()
for elemento in inventario:
    if busca == elemento[0]:
        print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")
        print("Valor.........:\tR$", elemento[1])
        print("Serial........:\t", elemento[2])

#Com o passar do tempo os equipamentos são desvalorizados, então os mesmos perdem seu valor
##assim sendo terá um reajusto retirando uma certa porcentagem de seu valor
desvalorizar = input("Digite o NOME do equipamento que será desvalorizado: ").upper()
for elemento in inventario:
    if desvalorizar == elemento[0]:
        print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")
        print("Valor antigo: R$", elemento[1])
        elemento[1] = elemento[1] *0.9
        print(f"Novo valor:\tR${elemento[1]:.2f}")

#Atraves do número de serie dos elementos será feito uma busca e por fim apagará e 
#mostrará os atuais elementos que tem no invetario
serial = int(input("Digite o número do equipamento que será apagado: "))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

for elemento in inventario:
    print("----------------------------------")
    print("Nome..............:\t", elemento[0])
    print("Valor.............:\tR$", elemento[1])
    print("Serial............:\t", elemento[2])
    print("Departamento......:\t", elemento[3])

#Apresenta na tela os equipamentos mais caros e baratos, como também a soma dos valores
valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print("O equipamento mais caro custa......R$", max(valores))
    print("O equipamento mais barato custa....R$", min(valores))
    print("O total de equipamentos é de.......R$", sum(valores))