from socket import *
servidor = "127.0.0.1"
porta = 12345
arq_socket = socket(AF_UNIX, SOCK_DGRAM)
arq_socket.bind((servidor, porta))
arq_socket.listen(3)
print(".......Loading.......")
while True:
    con, cliente = arq_socket.accept()
    print("Conectando com....\n",cliente)
    while True:
        msg_recebida = str(con.recv(512))
        print("mensagem: ", str(msg_recebida)[2:-1])
        msg_padrao = bytes(input("Digite sua resposta: "), 'uft-8')
        con.send(msg_padrao)
        break
    con.close()