"""
13.	Crear una función recursiva para conceptualizar el funcionamiento de un semáforo con tres luces (rojo, amarillo y verde). La función debe recibir como parámetro el color inicial y seguir esta secuencia para la representación de los colores: rojo, verde, amarillo (y repetir nuevamente a partir del rojo). La cantidad de veces que se va a realizar el ciclo estará parametrizada. La función tendrá la siguiente definición: def semaforo(ciclos, color). 
Ejemplo: semaforo(4, “verde”)
verde
amarillo
rojo
verde

"""

def semaforo(ciclos, color):
    secuencia = {
        "rojo" : "verde",
        "verde" : "amarillo",
        "amarillo" : "rojo"
    }

    if ciclos >= 1:
        print(color)
        semaforo(ciclos-1, secuencia[color])


semaforo(4, "verde")
         