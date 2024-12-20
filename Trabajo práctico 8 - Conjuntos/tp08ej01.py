"""
1.	Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1. Utilizar manejo de excepciones para evitar errores al intentar quitar elementos inexistentes.
"""

conjunto = { i for i in range(0, 10) }

numeroAEliminar = 0

while numeroAEliminar != -1:
    try:
        numeroAEliminar = int(input("Ingrese el valor a eliminar: "))
        if numeroAEliminar != -1:
            conjunto.remove(numeroAEliminar)
            print("Valor del conjunto actual: ", conjunto)
    except KeyError:
       print("El valor ingresado no existe en el conjunto: ", conjunto)
    except ValueError:
       print("Debe ingresar un valor numérico")