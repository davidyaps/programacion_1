"""
9.	Contar el número de vocales: Crea un programa que le pida al usuario que ingrese una cadena y luego cuente y muestre el número de vocales que hay en la cadena. Ayuda: Puedes usar un bucle for para recorrer la cadena y un condicional if para comprobar si cada carácter es una vocal.
"""

def contarVocales(cadena):
    vocales = "aeiouáéíóú"
    contador = 0

    for letra in cadena:
        if letra.lower() in vocales:
            contador += 1

    return contador   


cadena = input("Ingresa una cadena: ")
print("La cantidad de vocales en la cadena es:", contarVocales(cadena))
