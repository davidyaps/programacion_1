"""7.	Escribir un programa que devuelva la concatenación de dos colas de números enteros, intercalando cada elemento, respetando su orden. Tenga en cuenta que ambas colas pueden tener diferente profundidad.
"""
from cola import *

def intercalarColas(cola1, cola2):
    cola_concatenada = crearCola()

    while not estaVacia(cola1) and not estaVacia(cola2):
        elemento_cola1 = desencolar(cola1)
        elemento_cola2 = desencolar(cola2)

        encolar(cola_concatenada, elemento_cola1)
        encolar(cola_concatenada, elemento_cola2)

    while not estaVacia(cola1):
        elemento_cola1 = desencolar(cola1)
        encolar(cola_concatenada, elemento_cola1)

    while not estaVacia(cola2):
        elemento_cola2 = desencolar(cola2)
        encolar(cola_concatenada, elemento_cola2)

    return cola_concatenada

# Ejemplo de uso
cola1 = crearCola()
cola2 = crearCola()

# Agregar elementos a la cola 1
encolar(cola1, 1)
encolar(cola1, 3)
encolar(cola1, 5)

# Agregar elementos a la cola 2
encolar(cola2, 2)
encolar(cola2, 4)
encolar(cola2, 6)
encolar(cola2, 8)

# Concatenar e intercalar las colas
cola_concatenada = intercalarColas(cola1, cola2)

# Mostrar la cola concatenada
print("Cola concatenada:")
while not estaVacia(cola_concatenada):
    elemento = desencolar(cola_concatenada)
    print(elemento)
