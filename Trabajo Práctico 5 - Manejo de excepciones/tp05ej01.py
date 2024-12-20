"""
1.	Desarrollar una función para ingresar a través del teclado un número. La función rechazará cualquier ingreso inválido de datos utilizando excepciones y mostrará la razón exacta del error. Devolver el valor ingresado cuando éste sea correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma.
"""

def cargarNumeroNatural():
    while True:
        try:
            valor = int(input("Ingrese un valor numérico: "))
            return valor
        except ValueError as e:
            print(f"Valor erróneo: {e}")

numero = cargarNumeroNatural()

print(f"El número ingresado es: {numero}")
    