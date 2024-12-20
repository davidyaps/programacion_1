"""
8.	Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 que no sean múltiplos de 5. 
A y B se ingresan desde el teclado.
"""

def multiplosDe7yNo5(desde, hasta):
    return [ numero for numero in range(desde, hasta+1) if numero % 7 == 0 and numero % 5 !=0 ]

desde = int(input("Ingrese el valor desde: "))
hasta = int(input("Ingrese el valor hasta: "))

print(multiplosDe7yNo5(desde, hasta))