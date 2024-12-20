"""
6.	Mayor Elemento por Columna: implementar una función que tome una matriz como entrada y devuelva una lista con los mayores elementos de cada columna.
"""

def encontrarMayoresPorColumna(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    mayoresPorColumna = []

    for j in range(columnas):
        mayor = matriz[0][j]
        for i in range(1, filas):
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
        mayoresPorColumna.append(mayor)

    return mayoresPorColumna

# Ejemplo de uso
matrizEjemplo = [
    [8, 12, 9],
    [14, 6, 17],
    [3, 15, 7]
]

mayoresColumnas = encontrarMayoresPorColumna(matrizEjemplo)

print("Matriz de ejemplo:")
for fila in matrizEjemplo:
    print(fila)

print("\nMayores elementos por columna:", mayoresColumnas)
