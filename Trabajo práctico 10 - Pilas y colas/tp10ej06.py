"""6.	Se tiene una cola en la que se han repartido números con el orden de atención. Cada integrante se representa mediante un diccionario (<número de orden>, <DNI>, <Nombre y Apellido>).Sin embargo, hay muchos "colados" en la misma, los que carecen de número("None"). Por eso se le ha ordenado al personal de seguridad que retire a todos aquellos que no tienen número. Mostrar la cola inicial, los DNI de quienes fueron retirados de la cola y la cola final."""

from cola import *

def retirarPersonasSinNumero(cola):
    colaInicial = cola.copy()
    colaFinal = crearCola()
    colaRetiradas = crearCola()

    while not estaVacia(cola):
        persona = desencolar(cola)
        numeroOrden = persona["número de orden"]

        if numeroOrden is not None:
            encolar(colaFinal, persona)
        else:
            dni = persona["DNI"]
            encolar(colaRetiradas, dni)

    return colaInicial, colaFinal, colaRetiradas

# Ejemplo de uso
colaPersonas = crearCola()

# Agregar personas a la cola original
encolar(colaPersonas, {"número de orden": 1, "DNI": "12345678", "Nombre y Apellido": "Juan Pérez"})
encolar(colaPersonas, {"número de orden": None, "DNI": "87654321", "Nombre y Apellido": "Ana Gómez"})
encolar(colaPersonas, {"número de orden": 2, "DNI": "98765432", "Nombre y Apellido": "María Rodríguez"})
encolar(colaPersonas, {"número de orden": None, "DNI": "23456789", "Nombre y Apellido": "Pedro López"})

# Retirar personas sin número de orden
colaInicial, colaFinal, colaRetiradas = retirarPersonasSinNumero(colaPersonas)

# Mostrar la cola inicial
print("Cola inicial:")
while not estaVacia(colaInicial):
    persona = desencolar(colaInicial)
    print(persona)

# Mostrar los DNI de las personas retiradas
print("DNI de las personas retiradas:")
while not estaVacia(colaRetiradas):
    dni = desencolar(colaRetiradas)
    print(dni)

# Mostrar la cola final
print("Cola final:")
while not estaVacia(colaFinal):
    persona = desencolar(colaFinal)
    print(persona)
