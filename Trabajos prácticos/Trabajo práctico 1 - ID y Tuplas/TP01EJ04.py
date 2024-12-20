"""
4.	Juego de cartas: crea una función que genere aleatoriamente una mano de cinco cartas de una baraja de póker. Cada carta debe ser representada por una tupla que contenga un número y un palo.
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


palos = ['♥', '♦', '♣', '♠']
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

mazo = []
for palo in palos:
    for valor in valores:
        mazo.append((valor, palo))

mazo = tuple(mazo)

mano = cartasAlAzar(mazo, 5)

print(mano)