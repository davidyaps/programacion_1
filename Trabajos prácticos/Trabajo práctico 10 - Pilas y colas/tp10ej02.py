"""
2.	Invertir el orden de los elementos de una pila.
"""

from pila import *

def invertirOrdenPila(pila):
    pAuxiliar = crearPila()

    while not estaVacia(pila):
        elemento = desapilar(pila)
        apilar(pAuxiliar, elemento)

    return pAuxiliar

p = crearPila()

# Leer los elementos de entrada y apilarlos en la pila
elementos = input("Ingrese los elementos separados por espacios: ").split()
for elemento in elementos:
    apilar(p, int(elemento))

# Invertir el orden de los elementos de la pila
pInvertida = invertirOrdenPila(p)


# Mostrar los elementos de la pila invertida
while not estaVacia(pInvertida):
    elemento = desapilar(pInvertida)
    print(elemento)

