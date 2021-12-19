from geopy.geocoders import Nominatim
from JSON_local import *

geolocator = Nominatim(user_agent= "wazeyes") #Nome do app
dicionario = ler_arquivos("entrada.json")
lista = dicionario["endereco"]
endereco = lista[0] + ";" + lista[1] + " " + lista[2] + " " + lista[3]
location = geolocator.geocode(endereco)
saida = {"Coordenadas: " (location.latitude, location.longitude)}
gravar_arquivos(saida, "saida.json")