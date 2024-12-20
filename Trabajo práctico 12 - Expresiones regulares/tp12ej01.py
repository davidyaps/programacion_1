"""
1.	Escriba un programa que busque la palabra "python" en una cadena ingresada por el usuario, sin importar que sea mayúsculas o minúsculas. Utilice el método findall para resolverlo. 
"""

import re

cadena = input("Ingrese un texto: ")
patron = "python"

matches = re.findall(patron, cadena, re.IGNORECASE)

print(matches) 
