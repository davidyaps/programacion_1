"""
3.	Suma de Matrices: escribir una función que reciba dos matrices como entrada y devuelva la matriz resultante de su suma. Se asume que ambas matrices tienen las mismas dimensiones.
"""


def sumaMatrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])  # Se asume que ambas matrices tienen las mismas dimensiones

    matrizResultante = []

    for i in range(filas):
        filaResultante = []
        for j in range(columnas):
            sumaElemento = matriz1[i][j] + matriz2[i][j]
            filaResultante.append(sumaElemento)
        matrizResultante.append(filaResultante)

    return matrizResultante

# Ejemplo de uso
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

resultado = sumaMatrices(matriz1, matriz2)

print("Matriz 1:")
for fila in matriz1:
    print(fila)

print("\nMatriz 2:")
for fila in matriz2:
    print(fila)

print("\nResultado de la suma:")
for fila in resultado:
    print(fila)
