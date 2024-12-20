"""
3.	Escribe una función para verificar si una cadena comienza con una letra mayúscula. De ser así, retornará True; False en caso contrario. Utilice el método match para su resolución.
"""

import re

def verificarMayusculaAlInicio(cadena):
    patron = '^[A-Z]'
    if re.match(patron, cadena):
        return True
    else:
        return False


print(verificarMayusculaAlInicio("Hola Mundo"))
print(verificarMayusculaAlInicio("python"))
