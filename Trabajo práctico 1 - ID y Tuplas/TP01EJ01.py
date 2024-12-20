""""
1.	Crear una variable utilizando tuplas que sea capaz de almacenar los valores de las cartas de la baraja española (48 cartas; del 1 al 12 de basto, copa, espada y oro). 
a.	Crear una función que retorne una lista con una determina cantidad de cartas seleccionadas al azar que será recibida como parámetro (junto con la variable que se creó el mazo).
b.	Utilizando la función anterior, obtenga 10 cartas del mazo e indique la cantidad de cartas que son de oro.
"""


import random

def cartasAlAzar(mazo, cantidad):
    total = 0
    cartas = []

    while (total < cantidad):
        carta = mazo[random.randint(0, len(mazo)-1)]
        if carta not in cartas:
            cartas.append(carta)
            total += 1
    
    return cartas


def cantidadPorPalo(cartas, paloBuscado):
    total = 0
    for carta in cartas:
        numero, palo = carta
        if (palo == paloBuscado):
            total += 1

    return total


"""
#Alternativa con la creación directa de la varible (tabla: tuplas de tuplas)
mazo = (
        (1, 'basto'), (2, 'basto'), (3, 'basto'), (4, 'basto'), (5, 'basto'), (6, 'basto'), (7, 'basto'), (8, 'basto'), (9, 'basto'), (10, 'basto'), (11, 'basto'), (12, 'basto'),
        (1, 'copa'), (2, 'copa'), (3, 'copa'), (4, 'copa'), (5, 'copa'), (6, 'copa'), (7, 'copa'), (8, 'copa'), (9, 'copa'), (10, 'copa'), (11, 'copa'), (12, 'copa'),
        (1, 'espada'), (2, 'espada'), (3, 'espada'), (4, 'espada'), (5, 'espada'), (6, 'espada'), (7, 'espada'), (8, 'espada'), (9, 'espada'), (10, 'espada'), (11, 'espada'), (12, 'espada'),
        (1, 'oro'), (2, 'oro'), (3, 'oro'), (4, 'oro'), (5, 'oro'), (6, 'oro'), (7, 'oro'), (8, 'oro'), (9, 'oro'), (10, 'oro'), (11, 'oro'), (12, 'oro')
        )
"""

palos = ['basto', 'copa', 'espada', 'oro']
mazo = []

for palo in palos:
    for numero in range(1, 13):
        mazo.append((numero, palo))

mazo = tuple(mazo)

cartas = cartasAlAzar(mazo, 10)
print("Cartas: ", cartas)
print("Cantidad de oros: ", cantidadPorPalo(cartas, 'oro'))
