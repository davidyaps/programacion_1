"""
1.	Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30). Debes usar una matriz para su parametrización y una función para la recuperación del dato.
"""

def obtenerDiasDelMes(mes, matrizMeses):
    for i in range(0, len(matrizMeses)):
        if matrizMeses[i][0] == mes:
            return matrizMeses[i][1]


matrizMeses = [
    [1, 31],  # Enero
    [2, 28],  # Febrero
    [3, 31],  # Marzo
    [4, 30],  # Abril
    [5, 31],  # Mayo
    [6, 30],  # Junio
    [7, 31],  # Julio
    [8, 31],  # Agosto
    [9, 30],  # Septiembre
    [10, 31], # Octubre
    [11, 30], # Noviembre
    [12, 31]  # Diciembre
]

mes = int(input("Ingrese un número de mes: "))

if mes >= 1 and mes <= 12:
    print("El mes", mes, "tiene", obtenerDiasDelMes(mes, matrizMeses), "días.")
else:
    print("Número de mes inválido. Ingrese un valor entre 1 y 12.")

