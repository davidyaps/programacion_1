"""
9.	Crear una función que reciba dos números enteros como parámetros. Ambos valores recibidos como parámetros se deben modificar. Imprimir los IDs de ambos números antes, durante y después de la llamada a la función. ¿Cuál es la relación entre los IDs antes y después de la llamada a la función?
"""

def pruebaId(numero1, numero2):
    print("El ID de numero1 es:", id(numero1))
    print("El ID de numero2 es:", id(numero2))
    numero1 += 1
    numero2 += 2
    print("El ID de numero1 después de la operación es:", id(numero1))
    print("El ID de numero2 después de la operación es:", id(numero2))

miNumero1 = 10
miNumero2 = 20
print("El ID de miNumero1 es:", id(miNumero1))
print("El ID de miNumero2 es:", id(miNumero2))

pruebaId(miNumero1, miNumero2)
