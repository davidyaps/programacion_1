"""
1.	Generar una lista con 50 números al azar entre 1 y 100 y crear una nueva lista con los elementos de la primera que 
sean impares. El proceso deberá realizarse utilizando listas por comprensión. Imprimir las dos listas por pantalla.
"""
import random

listaAzar = [ random.randint(1, 100) for i in range(0, 50) ]
listaImpares = [ numero for numero in listaAzar if numero %2 != 0 ]

print("Lista al azar: ", listaAzar)
print("Lista de impares: ", listaImpares)
