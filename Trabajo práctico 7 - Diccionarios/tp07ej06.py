"""
6.	Juego de adivinanza de frutas: Crea un diccionario con nombres de frutas como claves y sus descripciones como valores. El programa debe elegir aleatoriamente una fruta y mostrar su descripción. Luego, el usuario debe adivinar qué fruta es. Si el usuario adivina correctamente, el programa debe mostrar un mensaje de felicitación.
"""

import random

frutas = {"manzana": "Es una fruta roja o verde con una forma redonda o en forma de pera.",
          "naranja": "Es una fruta redonda, de color naranja, con un sabor dulce y ácido.",
          "banana": "Es una fruta alargada, amarilla y dulce que se pela antes de comer.",
          "kiwi": "Es una fruta pequeña, marrón y peluda, con una pulpa verde y ácida."}

fruta_seleccionada = random.choice(list(frutas.keys()))

print("Adivina qué fruta estoy pensando. Aquí está la descripción:")
print(frutas[fruta_seleccionada])

intentos = 3
while intentos > 0:
    respuesta = input("¿Qué fruta es? ")
    if respuesta.lower() == fruta_seleccionada:
        print("¡Felicidades! Adivinaste la fruta.")
        break
    else:
        intentos -= 1
        print("Incorrecto. Te quedan {} intentos.".format(intentos))
else:
    print("Lo siento, no adivinaste la fruta. Era {}.".format(fruta_seleccionada))
