"""
11.	Capitalizar la primera letra: Crea un programa que le pida al usuario que ingrese una cadena y luego capitalice la primera letra de cada palabra en la cadena. Puedes usar el método title() para hacer esto.
"""
def capitalizarCadena(cadena):
    return cadena.title()


cadena = input("Ingresa una cadena: ")

print("La cadena capitalizada es:", capitalizarCadena(cadena))

