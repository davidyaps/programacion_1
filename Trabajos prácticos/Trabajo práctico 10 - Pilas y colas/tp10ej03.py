"""
3.	Escribir una función reemplazar(<pila>, <nuevo>, <viejo>) que reemplace todas las apariciones de <viejo> por <nuevo> dentro de la pila suministrada.
"""

from pila import *

def reemplazar(pila, nuevo, viejo):
    pila_auxiliar = crearPila()

    while not estaVacia(pila):
        elemento = desapilar(pila)
        if elemento == viejo:
            apilar(pila_auxiliar, nuevo)
        else:
            apilar(pila_auxiliar, elemento)

    while not estaVacia(pila_auxiliar):
        apilar(pila, desapilar(pila_auxiliar))

# Ejemplo de uso
p = crearPila()

# Leer los elementos de entrada y apilarlos en la pila
elementos = input("Ingrese los elementos separados por espacios: ").split()
for elemento in elementos:
    apilar(p, elemento)

viejo = input("Ingrese el valor a reemplazar: ")
nuevo = input("Ingrese el nuevo valor: ")

# Reemplazar todas las apariciones de viejo por nuevo en la pila
reemplazar(p, nuevo, viejo)

# Mostrar los elementos de la pila actualizada
while not estaVacia(p):
    elemento = desapilar(p)
    print(elemento, end=" ")
