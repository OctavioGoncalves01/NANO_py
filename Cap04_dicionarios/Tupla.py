ips = {}
resp = 'S'
while resp == 'S':
    print("-=-=-=-=-=-=-=-=[##########]=-=-=-=-=-=-=-=-")
    ips[(input("Digite os dois primeiros octetos..........: "),
         input("Digite os dois últimos octetos............: "))] = input("Nome da máquina...........................: ").upper()
    resp = input("Digite <S> para contuniar.................: ").upper()

print("Exibir Ip's:\t")
for ip in ips.keys():
    print(ip[0]+ "." + ip[1])

print("Exibindo máquinas com o mesmo endereço:\t")
pesquisa = input("Digite os dois últimos octetos:\t")
print("Máquinas no mesmo endereço (redes diferentes)")
for ip, nome in ips.items():
    if (ip[1] == pesquisa):
        print(nome)

print("Máquinas que compões a mesma rede:")
rede = input("Digite os dois primeiros octetos:\t")
for ip, nome in ips.items():
    if (ip[0] == rede):
        print(nome)