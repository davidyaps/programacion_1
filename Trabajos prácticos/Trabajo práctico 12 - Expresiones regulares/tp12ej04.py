"""
4.	Desarrolle una función que busque la existencia de una palabra en una cadena, sin importar mayúsculas o minúsculas. De ser así, retornará True; False en caso contrario. Utilice el método search para su resolución.
"""

import re

def buscarPalabra(cadena, palabra):
    if re.search(palabra, cadena, re.IGNORECASE):
        return True
    else:
        return False



print(buscarPalabra("Me gusta Python.", "python"))
print(buscarPalabra("Estoy aprendiendo C++.", "python"))
