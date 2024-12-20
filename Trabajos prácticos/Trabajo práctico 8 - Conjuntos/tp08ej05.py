"""
5.	Eliminar duplicados de una lista con conjuntos: Crea una función que tome una lista y elimine los elementos duplicados utilizando conjuntos. La función debe devolver una lista sin elementos duplicados.
"""

def eliminarDuplicados(lista):
    # Convertimos la lista en un conjunto para eliminar los duplicados
    conjunto = set(lista)

    # Convertimos el conjunto de vuelta a una lista para poder devolverla
    listaSinDuplicados = list(conjunto)
    return listaSinDuplicados


lista = ["manzana", "naranja", "manzana", "pera", "naranja", "kiwi", "naranja"]
listaSinDuplicados = eliminarDuplicados(lista)

print("Lista original: ", lista)
print("Lista sin duplicados: ", listaSinDuplicados)
