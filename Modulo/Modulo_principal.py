from Cap03_Listas_DivisaoPorModulo import *

minha_lista = []
print("Preenchendo...")
preenchimento_inventario(minha_lista)
print("Exibindo...")
exibir_inventario(minha_lista)

print("Pesquisando...")
localizar_item_por_nome(minha_lista)
print("Alterando valores...")
desvalorizar_por_nome(minha_lista, 20)

print("Excluindo...")
print(remover_por_serial(minha_lista))
exibir_inventario(minha_lista)

print("Resumindo valores...")
resumir_valores(minha_lista)