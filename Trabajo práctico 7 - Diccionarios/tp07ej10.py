"""
10.	Se desea implementar la funcionalidad del juego «piedra, papel o tijera». Para ello, se tiene una variable del tipo diccionario, en la que se almacena la regla de negocio de quién le gana a quién (la clave es el elemento, el valor a qué elemento le gana):

opcionesGanadoras = {
    "piedra" : "tijera", 
    "papel" : "piedra", 
    "tijera" : "papel"
}

En una segunda variable, se almacenan un lote (lista) de jugadas que deben ser procesadas, distinguiendo a dos jugadores, en los que se especifica como valor su nombre y la opción seleccionada en esa jugada:
jugadas = [ {
"jugador1" : {"nombre": "Oliver", "opcion": "piedra"},
             "jugador2" : {"nombre": "Gabriela", "opcion": "papel"}
             },
             {
"jugador1" : {"nombre": "Oliver", "opcion": "tijera"},
              "jugador2" : {"nombre": "Gabriela", "opcion": "papel"}
             }
            ]

Con relación a dicha información, se deberán elaborar las siguientes funciones: 
 
•	resultado(opcion1, opcion2, opcionesGanadoras): Recibe como parámetro dos opciones (“piedra”, “papel” o “tijera”) junto con la variable de opcionesGanadoras. Deberá retornar None si hay un empate; 1 si gana la opción 1; y el valor 2 si gana la opción 2. Por ejemplo, dado los siguientes llamados, la función deberá retornar:
resultado ('papel', 'papel', opcionesGanadoras) ==>  None
resultado ('tijera', 'papel', opcionesGanadoras) ==>  1
resultado ('tijera', 'piedra', opcionesGanadoras) ==>  2

•	analizarJugada(jugada, opcionesGanadoras): Recibe una jugada como parámetros junto con las opciones ganadoras. Dentro de la función deberá utilizar la función resultado (definida en el ítem anterior) y retornar la leyenda: “Empate”, en caso de igualdad; o bien, “Gana {nombre del jugador}”. Utilizando las variables anteriores como ejemplo, debería retornar:
analizarJugada({'jugador1': {'nombre': 'Oliver', 'opcion': 'piedra'}, 'jugador2': {'nombre': 'Gabriela', 'opcion': 'papel'}}, opcionesGanadoras) ==>  Gana Gabriela

analizarJugada({'jugador1': {'nombre': 'Oliver', 'opcion': 'tijera'}, 'jugador2': {'nombre': 'Gabriela', 'opcion': 'papel'}}, opcionesGanadoras) ==>  Gana Oliver

"""


def resultado(opcion1, opcion2, opcionesGanadoras):
    if opcion1 == opcion2:
        return None

    if opcionesGanadoras[opcion1] == opcion2:
        return 1
    else:
        return 2

def analizarJugada(jugada, opcionesGanadoras):
    resultadoJugada = resultado(jugada["jugador1"]["opcion"], jugada["jugador2"]["opcion"],opcionesGanadoras)
    
    if resultadoJugada == None:
        return "Empate"
    
    if resultadoJugada == 1:
        return "Gana " + jugada["jugador1"]["nombre"]
    else:
        return "Gana " + jugada["jugador2"]["nombre"]




jugadas = [ {"jugador1" : {"nombre": "Oliver", "opcion": "piedra"},
             "jugador2" : {"nombre": "Gabriela", "opcion": "papel"}
             },
             {"jugador1" : {"nombre": "Oliver", "opcion": "tijera"},
              "jugador2" : {"nombre": "Gabriela", "opcion": "papel"}
             }
            ]

opcionesGanadoras = {
    "piedra" : "tijera", 
    "papel" : "piedra", 
    "tijera" : "papel"
}

for jugada in jugadas:
    print(f"analizarJugada({jugada}, opcionesGanadoras) ==> ", analizarJugada(jugada, opcionesGanadoras))

jugadas = [("papel", "papel"), ("tijera", "papel"), ("tijera", "piedra")]

for jugada in jugadas:
    print(f"resultado ('{jugada[0]}', '{jugada[1]}', opcionesGanadoras) ==> ", resultado (jugada[0], jugada[1], opcionesGanadoras))

