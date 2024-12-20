"""2.	Leer una cadena de caracteres e imprimirla sin espacios en sus laterales."""

cadena = input("Ingrese una cadena: ")
while cadena != "":
    print(f"La cadena original: \"{cadena}\"")
    print(f"La cadena sin espacios: \"{cadena.strip()}\"")
    cadena = input("Ingrese una cadena: ")