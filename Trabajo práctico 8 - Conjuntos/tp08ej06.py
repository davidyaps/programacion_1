"""
6.	Palabras únicas en una cadena: Crea una función que tome una cadena como argumento y devuelva un conjunto que contenga todas las palabras únicas en la cadena.
"""

def palabrasUnicas(cadena):
    # Convertimos la cadena en una lista de palabras
    listaPalabras = cadena.split()

    # Convertimos la lista de palabras en un conjunto para eliminar las palabras duplicadas
    conjuntoPalabras = set(listaPalabras)
    return conjuntoPalabras


cadena = "La manzana es roja, la naranja es naranja y la banana es amarilla."
conjuntoPalabras = palabrasUnicas(cadena)
print("Cadena original: ", cadena)
print("Palabras únicas: ", conjuntoPalabras)