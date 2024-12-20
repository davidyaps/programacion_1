"""
8.	Desarrollar una función para reemplazar todas las apariciones de una palabra por otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la cantidad de reemplazos realizados. 
Tener en cuenta que sólo deben reemplazarse palabras completas, y no fragmentos de palabras. 
Escribir también un programa para verificar el comportamiento de la función.
"""

def reemplazar(cadena, busqueda, reemplazo):
    lista = cadena.split()
    resultado = ""

    cantidad = 0
    for palabra in lista:
        if (palabra == busqueda):
            resultado += reemplazo + " "
            cantidad += 1
        else:
            resultado += palabra + " "

    return resultado.rstrip(), cantidad


print (reemplazar("el velóz muerciélago come kiwi y melón", "come", "ingiere"))
