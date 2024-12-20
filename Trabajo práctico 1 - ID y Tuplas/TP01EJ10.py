"""
10.	Crear una función que reciba una lista como parámetro. Dentro de la función, crear una nueva lista y asignarla a la variable original. Imprimir los IDs de ambas listas antes y después de la asignación dentro de la función. ¿Qué puedes concluir sobre el comportamiento de Python en este caso?
"""

def cambiarLista(lista):
    print("El ID de la lista original es:", id(lista))
    lista = [4, 5, 6]
    print("El ID de la lista modificada es:", id(lista))

miLista = [1, 2, 3]
print("El ID de miLista es:", id(miLista))

cambiarLista(miLista)

print(miLista)
