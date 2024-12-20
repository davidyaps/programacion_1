"""
2.	Escribir funciones para:
a.	Generar una lista de 50 números aleatorios del 1 al 100. Utilice comprensión de listas para generar el resultado.
b.	Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función no debe modificar la lista.
c.	Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa.
"""
import random

def generar50NumerosAleatorios():
    return [ random.randint(1, 100) for i in range(0, 51) ]

def hayDuplicados(lista):
    for elemento in lista:
        if lista.count(elemento) > 1:
            return True
    
    return False

def sinDuplicados(lista):
    listaSinDuplicados = []

    for elemento in lista:
        if elemento not in listaSinDuplicados:
            listaSinDuplicados.append(elemento)
    
    return listaSinDuplicados


lista = generar50NumerosAleatorios()
print("Lista original: ", lista)
if (hayDuplicados(lista)):
    print("Lista sin duplicados: ", sinDuplicados(lista))
