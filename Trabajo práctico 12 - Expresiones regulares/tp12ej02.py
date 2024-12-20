"""
2.	Escriba un programa que busque todas las letras mayúsculas en una cadena ingresada por el usuario e imprima cada una de ellas. Utilice el método findall para resolverlo.
"""
import re

cadena = input("Ingrese un texto: ")
patron = "[A-Z]"

matches = re.findall(patron, cadena)

for match in matches:
    print(match)
