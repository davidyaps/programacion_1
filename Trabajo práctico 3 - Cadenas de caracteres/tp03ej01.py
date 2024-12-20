"""1.	Desarrollar una función que determine si una cadena de caracteres es capicúa. 
Escribir además un programa que permita verificar su funcionamiento solicitándole al usuario valores hasta que el mismo sea vacío."""

def esCapicua (cadena):
    cadena = cadena.lower()
    return cadena == cadena[::-1]    

cadena = input("Ingrese una cadena: ")
while cadena != "":
    if esCapicua(cadena):
        print(f"La cadena \"{cadena}\" es capicúa")
    else:
        print(f"La cadena \"{cadena}\" NO es capicúa")
    
    cadena = input("Ingrese una cadena: ")