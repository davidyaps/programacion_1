"""
5.	Suma de números: crea un programa que lea una lista de tuplas, donde cada tupla contiene dos números enteros, y calcule la suma de los números en cada tupla. Por ejemplo, si llamamos a la función con la lista de tuplas [(1, 2), (3, 4), (5, 6)], la función devolverá el valor 21, que es la suma de los números en todas las tuplas.
"""

def sumaTuplas(listaTuplas):
    sumaTotal = 0

    for tupla in listaTuplas:
        sumaTotal += sum(tupla)

    return sumaTotal


valores = [(1, 2), (3, 4), (5, 6)]

print(sumaTuplas(valores))