"""
2.	Crea una matriz con un tamaño que el usuario le indique por teclado (puede ser 6×4, 7×2, etc.) pero como máximo podrá contener 10x10 valores y como mínimo 2x2. Crear una función para la cargar de los valores y, por último, otro procedimiento para visualizar los resultados. Los valores para cargar deberán ser número positivos entre 0 y 100, siendo éstos generados al azar.
"""

import random

def cargarMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(0, 100))
        matriz.append(fila)
    return matriz

def visualizarMatriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end="\t")
        print()



filas = int(input("Ingrese el número de filas (entre 2 y 10): "))
columnas = int(input("Ingrese el número de columnas (entre 2 y 10): "))

if filas >= 2 and filas <= 10 and columnas >= 2 and columnas <= 10:
    matrizGenerada = cargarMatriz(filas, columnas)
    print("\nMatriz generada:")
    visualizarMatriz(matrizGenerada)
else:
    print("El tamaño de la matriz debe estar entre 2x2 y 10x10.")
