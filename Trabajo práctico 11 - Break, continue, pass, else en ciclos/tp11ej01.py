"""1.	Escribe un programa que pida al usuario ingresar una lista de números enteros y encuentre el primer número par en la lista. Si no hay números pares, el programa debe mostrar un mensaje que lo indique. Utilice for, break, else para su resolución."""

numeros = input("Ingresa una lista de números enteros separados por espacios: ")
numeros = [int(numero) for numero in numeros.split()]

for num in numeros:
    if num % 2 == 0:
        print(f"El primer número par en la lista es {num}.")
        break
else:
    print("No hay números pares en la lista.")
