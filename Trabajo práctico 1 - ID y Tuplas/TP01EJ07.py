"""
7.	Cálculo de áreas: crea un programa que lea una lista de tuplas, donde cada tupla contiene el nombre de una figura geométrica (cuadrado, rectángulo, triángulo y círculo)  y sus dimensiones, y calcule el área de cada figura.
"""
def calcularArea(figura, dimensiones):
    if figura == 'cuadrado':
        return dimensiones[0] * dimensiones[0]
    elif figura == 'rectángulo':
        return dimensiones[0] * dimensiones[1]
    elif figura == 'triángulo':
        return dimensiones[0] * dimensiones[1] / 2
    elif figura == 'círculo':
        return 3.1416 * dimensiones[0] * dimensiones[0]


listaFiguras = [('cuadrado', [5]), ('rectángulo', [3, 4]), ('triángulo', [6, 2]), ('círculo', [2])]
for figura in listaFiguras:
    print("El área de la figura ", figura[0], " cuyas dimensions son ", figura[1], " es ", calcularArea(figura[0], figura[1]))
