"""
3.	Desarrolle un programa que procese una tabla con 10 horarios (hora -de 0 a 23- y minutos) en formato tupla; 
e indique por cada una de ellas: si es AM o PM y cuántos minutos falta para la próxima hora. 
El resultado de AM/PM y la cantidad de minutos se debe almacenar en una lista de tuplas con los valores originales y 
los resultados. Imprimir el resultado final en pantalla.
"""

def AMPM(hora):
    if hora >= 12 and hora <=23:
        return "PM"
    else:
        return "AM"

def minutosFaltantes(minutos):
    return 60 - minutos

def procesarHorarios(horarios):
    lista = []

    for horario in horarios:
        hora, minutos = horario
        lista.append((hora, minutos, AMPM(hora), minutosFaltantes(minutos)))
    
    return lista


horarios = [
            (10, 40), (1, 11), (11,33), (13, 10), (23, 0), (9, 59), (0, 10), (5, 30), (7, 8), (3, 33)
           ]

resultado = procesarHorarios(horarios)

for horario in resultado:
    hora, minutos, franja, faltan = horario
    print(hora, ":", minutos, franja, " - Faltan ", faltan, " minutos para la próxima hora...")
