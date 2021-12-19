nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
doenca = input("O pacinete tem suspeita de alguma doença infecto-contagiosa: [S/N]\n").upper()
genero = input("Digite o genero do paciente: [M/F]\n").upper()
#Primeiro problema
if doenca == "S":
    print("O paciente deve ser alocado na sala Amarela")
elif doenca == "N":
    print("O paciente deve ser alocado na sala Branca")
else:
    print("Responda 'Suspeita de doença infcto-contagiosa' com S/N")
#Segundo problema
if idade >= 65:
    print("O paciente tem prioridade")
else:
    if genero == 'F' and idade >10:
        gestante = input("A paciente é gestante [S/N]\n").upper()
        if gestante == 'S':
            print("A paciente tem prioridade")
        else:
            print("A paciente NÃO tem prioridade")
    else:
        print("A paciente NÃO tem prioridade")