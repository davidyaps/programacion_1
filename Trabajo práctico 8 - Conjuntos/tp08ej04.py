"""
4.	Crea una función para unir conjuntos: Crea una función que tome dos conjuntos como argumentos y devuelva un conjunto que contenga todos los elementos de ambos conjuntos. Asegúrate de que la función maneje conjuntos con diferentes tipos de elementos, como cadenas y números.
"""

def unirConjuntos(conjunto1, conjunto2):
    conjunto_union = conjunto1.union(conjunto2)
    return conjunto_union

conjunto1 = set([1, 2, 3])
conjunto2 = set([3, 4, 5])
conjuntoUnion = unirConjuntos(conjunto1, conjunto2)

print(conjuntoUnion)