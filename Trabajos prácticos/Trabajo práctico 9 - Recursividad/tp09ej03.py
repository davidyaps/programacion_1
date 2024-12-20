"""
3.	Escribir una función que devuelva la suma de los N primeros números naturales.
"""

def numerosNaturales (numero):
    if numero == 0:
        return 0
    else:
        return numero + numerosNaturales(numero-1)


print("0 = ", numerosNaturales(0))
print("3 = ", numerosNaturales(3))
print("8 = ", numerosNaturales(8))
print("11 = ", numerosNaturales(11))
