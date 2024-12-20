"""7.	Escriba un programa que utilizando map y una función lambda como argumento, 
permita generar una nueva lista con el resultado de la división en 1 (es decir, 1/x) de cada elemento de la lista. """

def obtenerInversos(lista):
    return list(map(lambda numero : 1/numero, lista))

valores = [1, 1, 2, 3, 5, 8, 13, 21]

if 0 not in valores:
    inversos = obtenerInversos(valores)
    print(inversos)
else:
    print("El valor 0 en la lista no está permitido para completar la operación")
