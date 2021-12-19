usuarios = {}
usuarios = {
    "Chaves": ["Chaves da Silva", "17/06/1975", "Recep_01"],
    "Quico": ["Enrico Flores", "03/06/1975", "RaioX_02"],
    "Quico": ["Enrico Flores", "03/06/1975", "RaioX_03"]
}
usuarios["Octavio"] = ["Octavio Gonçalves", "26/11/2017", "Recep_01"]
usuarios["Octavio"] = ["Octavio Gonçalves", "26/11/2016", "Recep_01"]

print(usuarios)
print("-----------------#############-------------------")
print("Dados:\t", usuarios.get("Chaves"))