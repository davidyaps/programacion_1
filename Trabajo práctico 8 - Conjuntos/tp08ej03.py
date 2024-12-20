"""
3.	Crear dos conjuntos con cinco valores generados al azar, que se encuentre entre 1 y 10. Al finalizar, realizar:
•	Mostrar los valores que son en común entre ambos conjuntos
•	Luego, volcar desde el primer conjunto al segundo, aquellos valores que no se encuentran del primero en el segundo
"""

import random

def crearConjuntoAlAzar(cantidad, valorMinimo, valorMaximo):
    conjunto = set()
    while len(conjunto) < cantidad:
        conjunto.add(random.randint(valorMinimo, valorMaximo))
    
    return conjunto


conjuntoA = crearConjuntoAlAzar (5, 1, 10)
conjuntoB = crearConjuntoAlAzar (5, 1, 10)

interseccionAB = conjuntoA & conjuntoB
diferenciaAB = conjuntoA - conjuntoB

print("Conjunto A: ", conjuntoA)
print("Conjunto B: ", conjuntoB)
print("Intersección A y B: ", interseccionAB)
print("Diferencia A y B: ", diferenciaAB)
print("***Se agregan los elementos faltantes en B***")
conjuntoB.update(list(diferenciaAB))
print("Conjunto B: ", conjuntoB)



