"""
7.	Cuenta la cantidad de palabras únicas en una cadena: Crea una función que tome una cadena como argumento y devuelva la cantidad de palabras únicas en la cadena. Para hacerlo, puedes utilizar conjuntos y el método len() de Python.
"""

def cantidadPalabrasUnicas(cadena):
    # Convertimos la cadena en una lista de palabras
    listaPalabras = cadena.split()

    # Convertimos la lista de palabras en un conjunto para eliminar las palabras duplicadas
    conjuntoPalabras = set(listaPalabras)
    return len(conjuntoPalabras)


cadena = "La manzana es roja, la naranja es naranja y la banana es amarilla."
cantidadPalabras = cantidadPalabrasUnicas(cadena)
print("Cadena original: ", cadena)
print("Cantidad de palabras únicas: ", cantidadPalabras)