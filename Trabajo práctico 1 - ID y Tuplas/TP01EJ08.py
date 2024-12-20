"""
8.	Crear una lista y asignarla a otra variable diferentes. Luego, imprimir los IDs de ambas variables y comprobar si son iguales o diferentes. ¿Qué puedes concluir sobre el comportamiento de Python en este caso?
"""

lista = [1, 2, 3]
otraLista = lista
print("El ID de lista es:", id(lista))
print("El ID de otraLista es:", id(otraLista))