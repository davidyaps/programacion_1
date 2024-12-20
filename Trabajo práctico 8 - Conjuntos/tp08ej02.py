"""
2.	Crear tres conjuntos:
•	pares: valores pares entre 0 y 100
•	impares: valores impares entre 0 y 100
•	azar: 50 valores al azar entre 0 y 100
Una vez generados los tres conjuntos, deberá realizar las siguientes acciones:
•	generar dos nuevos conjuntos: uno con la intersección entre azar y pares; y azar e impares. Informe de cada uno de ellos: la cantidad, el valor máximo y mínimo.
"""
import random

pares = {i for i in range(0, 101) if i % 2 == 0}
impares = {i for i in range(0, 101) if i % 2 != 0}
azar = set()

while len(azar) < 50:
    azar.add(random.randint(0, 100))

azarPares = azar & pares
azarImpares = azar & impares

print("Valores pares generados al azar: ", len(azarPares))
print("Valor par más alto generado al azar: ", max(azarPares))
print("Valor par más bajo generado al azar: ", min(azarPares))
print("")
print("Valores impares generados al azar: ", len(azarImpares))
print("Valor impar más alto generado al azar: ", max(azarImpares))
print("Valor impar más bajo generado al azar: ", min(azarImpares))




