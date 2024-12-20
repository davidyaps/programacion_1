"""
5.	Escribir un programa que juegue con el usuario a adivinar un número. El programa debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar el número. Si el usuario introduce algo que no sea un número se mostrará un mensaje en pantalla y se lo contará como un intento más.
"""

import random

def adivinarNumero():
    intentos = 0
    numeroAdivinar = random.randint(1, 500)

    while True:
        try:
            entrada = int(input("Ingrese un número: "))
            intentos += 1

            if entrada == numeroAdivinar:
                print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
                return
            elif entrada < numeroAdivinar:
                print("El número a adivinar es mayor.")
            else:
                print("El número a adivinar es menor.")

        except ValueError:
            print("Ingrese un número válido.")


adivinarNumero()
