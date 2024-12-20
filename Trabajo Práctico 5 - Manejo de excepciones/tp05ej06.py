"""
6.	Convertir una cadena en un número: Escribe un programa que solicite al usuario una cadena y luego intente convertirla en un número entero. Si la conversión falla, muestra un mensaje de error.
"""
def cadenaAEntero(cadena):
    try:
        numeroEntero = int(cadena)
        return numeroEntero
    except ValueError:
        print("La cadena no puede convertirse en un número entero.")
        return None


cadena = input("Ingrese una cadena: ")

print(cadenaAEntero(cadena))

