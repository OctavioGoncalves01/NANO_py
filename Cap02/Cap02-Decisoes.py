nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
doenca_infecciosa = input("O paciete tem alguma doença infecto-contagiosa: [S/N]\n").upper()

if idade >= 65 and doenca_infecciosa == "S":
    print(f"O paciente será direcionado para a sala AMARELA - COM prioridade")
elif idade <= 65 and doenca_infecciosa == "S":
    print(f"O paciente será direcionado para a sala AMARELA - SEM prioridade")
elif idade >= 65 and doenca_infecciosa == "N":
    print(f"O paciente será direcionado para a sala BRANCA- COM prioridade")
elif idade <= 65 and doenca_infecciosa == "N":
    print(f"O paciente será direcionado para a sala BRANCA - SEM prioridade")
else:
    print("Doença infecto-contagiosa deve ser respondido com S/N")