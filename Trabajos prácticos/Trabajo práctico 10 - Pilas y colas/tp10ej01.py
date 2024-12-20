"""
1.	Desarrollar un programa que sume los elementos de una pila, conservando intacta la misma al terminar el proceso. Desapile y vuelva a apilar los datos al finalizar (no recorra la lista).
"""
from pila import *

p = crearPila()
pAuxiliar = crearPila()

# Leer los elementos de entrada y apilarlos en la pila
elementos = input("Ingrese los elementos separados por espacios: ").split()
for elemento in elementos:
    apilar(p, int(elemento))

# Calcular la suma de los elementos conservando la pila intacta
suma = 0
while not estaVacia(p):
    elemento = desapilar(p)
    suma += elemento
    apilar(pAuxiliar, elemento)

# Volvemos a restaurar la pila original
while not estaVacia(pAuxiliar):
    apilar(p, desapilar(pAuxiliar))


print("La suma de los elementos es:", suma)
print("Contenido de la pila: ", p)

