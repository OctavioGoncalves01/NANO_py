import serial
conexao = ''
for porta in range(10):
    try:
        conexao = serial.Serial("COM" + str(porta), 115200, timeout = 0.5)
        print("Conexão na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao != "":
    acao = input("Digite <L> para ligar; <D> para desligar:\n<>").upper()
    while acao == "L" or acao =="D":
        if acao =="L":
            conexao.write(b'1')
        else:
            conexao.write(b'0')
        acao = input("Digite <L> para ligar; <D> para desligar:\n<>").upper()
    conexao.close()
    print("Conexão encerrada!")
else:
    print("Sem portas disponíveis")