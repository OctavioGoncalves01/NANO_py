num = int(input("Digite um número para ver sua tabuada: "))
print(f'Tabuada do número {num}')
for valor in range(1,11,1):
    print(f"\t{num}x{valor}=\t{valor*num}")