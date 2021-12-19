import socket
resp = "S"

while (resp == "S"):
    url = input("Digite uma URL: ")
    ip = socket.gethostbyname(url)
    print("O ip referente à URL informada é", ip)
    resp = input("Deseja continuar [S/N]:\n").upper()

