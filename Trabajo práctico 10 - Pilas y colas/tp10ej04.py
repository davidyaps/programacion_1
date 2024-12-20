"""4.	Un conductor viaja de un pueblo origen a un pueblo destino, pasando por varios pueblos intermedios. Una vez en el destino, el conductor debe regresar a casa por el mismo camino. Desarrollar un programa que permita al conductor registrar cada pueblo visitado y al finalizar el viaje le indique el camino de regreso."""

from pila import *

def registrarPueblos():
    pilaPueblos = crearPila()

    while True:
        pueblo = input("Ingrese el nombre del pueblo visitado (o 'fin' para finalizar): ")
        if pueblo == "fin":
            break
        apilar(pilaPueblos, pueblo)

    return pilaPueblos

def obtenerCaminoRegreso(pilaPueblos):
    while not estaVacia(pilaPueblos):
        pueblo = desapilar(pilaPueblos)
        print(pueblo)

# Registrar los pueblos visitados
pilaPueblosVisitados = registrarPueblos()

# Mostrar el camino de regreso
print("Camino de regreso:")
obtenerCaminoRegreso(pilaPueblosVisitados)