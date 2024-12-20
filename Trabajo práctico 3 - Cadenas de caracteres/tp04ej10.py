"""
10.	Eliminar caracteres: Crea un programa que le pida al usuario que ingrese una cadena y luego elimine todas las ocurrencias de un carácter específico en la cadena. Por ejemplo, puedes pedirle al usuario que ingrese una cadena y luego eliminar todas las letras "a".
"""
def eliminarCaracter(cadena, caracter):
    nuevaCadena = ""

    for letra in cadena:
        if letra != caracter:
            nuevaCadena += letra

    return nuevaCadena


cadena = input("Ingresa una cadena: ")
caracter = input("Ingresa el caracter que quieres eliminar de la cadena: ")

print("La nueva cadena es:", eliminarCaracter(cadena, caracter))