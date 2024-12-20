"""
3.	Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado. 
Luego se solicita imprimir los últimos 10 valores de la lista utilizando segmentación de listas.
"""
def listaCuadrados(cantidadElementos):
    return [ elemento**2 for elemento in range(1, cantidadElementos + 1) ]

cantidad = int(input("Ingrese la cantidad de elementos que desea generar: "))

lista = listaCuadrados(cantidad)

print("Lista: ", lista)
print(lista[len(lista)-10:])