"""
5. Escribe un programa que encuentre todas las apariciones de números en una cadena y devuelva cada número encontrado en una lista. Utilice el método finditer para su resolución.
"""

import re

def obtenerNumeros(cadena):

    patron = '[0-9]+'
    numeros = re.finditer(patron, cadena)
    
    return [ numero.group(0) for numero in numeros ]


# Ejemplo de uso
print(obtenerNumeros("Hay 7 manzanas y 11 naranjas."))  