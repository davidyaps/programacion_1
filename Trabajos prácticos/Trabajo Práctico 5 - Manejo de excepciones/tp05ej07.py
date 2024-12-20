"""
7.	Escribe una función llamada calcularRaizCuadrada que reciba un número como argumento y calcule su raíz cuadrada. Si el número es negativo, la función debe generar una excepción ValueError con un mensaje indicando que no se puede calcular la raíz cuadrada de un número negativo.
"""


def calcularRaizCuadrada(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return numero**0.5

# Ejemplo de uso
try:
    numero = float(input("Ingrese un número: "))
    resultado = calcularRaizCuadrada(numero)
    print(f"La raíz cuadrada de {numero} es {resultado}.")
except ValueError as e:
    print(e)
