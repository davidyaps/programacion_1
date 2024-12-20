"""
11.	Crear una función que reciba dos listas como parámetros. Dentro de la función, concatenar ambas listas y comprobar si el ID de la lista concatenada ha cambiado o se ha mantenido igual.
"""

def concatenarListas(lista1, lista2):
    print("El ID de la lista original es:", id(lista1))
    lista1 += lista2
    print("El ID de la lista concatenada es:", id(lista1))

miLista1 = [1, 2, 3]
miLista2 = [4, 5, 6]
print("El ID de miLista1 es:", id(miLista1))

concatenarListas(miLista1, miLista2)


