from geopy.geocoders import Nominatim
geolocater = Nominatim(user_agent="wazeyes")

latitude = float(input("Digite a latitude.........:\n<>"))
longitude = float(input("Digite a longitude.......:\n<>"))

resultado = str(geolocater.reverse(f"{latitude}, {longitude}")).split(";")
if resultado[0] != 'None':
    print("Endereço Completo...............: ", resultado)
    print("Dado 01.........................: ", resultado[0])
    print("Dado 02.........................: ", resultado[1])
    print("Dado 03.........................: ", resultado[2])