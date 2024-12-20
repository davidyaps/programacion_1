"""
6.	Escriba una función que reemplace todas las vocales en una cadena con el carácter '_'. Utilice el método sub para el desarrollo.
"""

import re

def reemplazarVocalesPorGuionBajo(cadena):
    patron = '[aeiouAEIOUáéíóúÁÉÍÓÚ]'
    resultado = re.sub(patron, '_', cadena)
    return resultado

# Ejemplo de uso
print(reemplazarVocalesPorGuionBajo("Hola Mundo"))   # Salida esperada: Cadena original: Hola Mundo. Cadena modificada: H-l- M-nd-
