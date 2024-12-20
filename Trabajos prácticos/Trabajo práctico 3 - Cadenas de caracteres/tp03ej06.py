"""
6.	Escribir una función que reciba como parámetro una cadena de caracteres en la que las palabras se encuentran 
separadas por uno o más espacios. Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando un espacio 
entre cada una.
"""

def ordenarPalabras(cadena):
    lista = cadena.split()
    lista.sort()

    return " ".join(lista)


print (ordenarPalabras("el velóz muerciélago come kiwi"))
