from socket import *

servidor = "127.0.0.1"
porta = 12345

while True:
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((servidor, porta))
    msg = bytes(input("Digite algo\n[Para sair digite <SAIR>]: "), 'utf-8')
    obj_socket.send(msg)
    resposta = obj_socket.recv(512)
    print("Recebemos: ", str(resposta)[2:-1])
    if str(msg)[2:-1].upper() == "FIM":
        break
obj_socket.close()