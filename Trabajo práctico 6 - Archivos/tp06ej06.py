"""
6.	Genere un programa que pregunte un nombre de archivo (ubicación) y muestre en pantalla el contenido de ese archivo. 
Informe en pantalla si no existe.
"""

try:
    archivo = input("Ingrese el nombre del archivo: ")
    contenido = open(archivo, "r")
    caracteres = contenido.read()

    print(caracteres)

    contenido.close()
except FileNotFoundError:
    print("No existe el archivo")