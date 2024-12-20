"""5.	Crear un programa que pida al usuario ingresar una cadena de caracteres y determine si la cadena contiene al menos una letra mayúscula y al menos una letra minúscula. Si la cadena cumple con estas condiciones, el programa debe mostrar un mensaje de confirmación. Si la cadena no cumple con estas condiciones, el programa debe mostrar un mensaje de error. Utilice for, break y pass para cumplir el objetivo."""

cadena = input("Ingresa una cadena de caracteres: ")
tieneMayuscula = False
tieneMinuscula = False

for letra in cadena:
    if letra.isupper():
        tieneMayuscula = True
    if letra.islower():
        tieneMinuscula = True
    if tieneMayuscula and tieneMinuscula:
        print("La cadena cumple con las condiciones.")
        break
else:
    print("La cadena no cumple con las condiciones.")
    pass
