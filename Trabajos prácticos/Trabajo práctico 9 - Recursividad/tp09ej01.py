"""
1.	Escribir una función que devuelva la cantidad de dígitos de un número entero, sin utilizar cadenas de caracteres.
"""

def cantidadDigitos(numero):
    if numero > -10 and numero < 10:
        return 1
    else:
        return 1 + cantidadDigitos(numero//10)


print(cantidadDigitos(1))
print(cantidadDigitos(33))
print(cantidadDigitos(-333))