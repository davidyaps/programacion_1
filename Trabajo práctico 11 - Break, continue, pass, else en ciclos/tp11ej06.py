"""6.	Desarrolle un programa que pida al usuario ingresar una lista de números enteros y encuentre el segundo número más grande en la lista. Si la lista tiene menos de dos elementos, el programa debe mostrar un mensaje de error y pedir al usuario que ingrese una lista válida. Implemente la solución utilizando while True, continue y break."""

while True:
    numeros = input("Ingresa una lista de números enteros separados por espacios: ")
    numeros = [int(numero) for numero in numeros.split()]

    if len(numeros) < 2:
        print("La lista debe tener al menos dos elementos. Inténtalo de nuevo.")
        continue

    numeros.sort(reverse=True)
    print(f"El segundo número más grande en la lista es {numeros[1]}.")

    break
