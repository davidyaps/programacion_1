"""7.	Escribe un programa que pida al usuario ingresar un número entero positivo y calcule la suma de los números impares entre 1 y ese número. Si el usuario ingresa un número no positivo, el programa debe mostrar un mensaje de error y pedir al usuario que ingrese un número válido. Implemente la solución utilizando while True, continue y break."""

while True:
    numero = int(input("Ingresa un número entero positivo: "))
    if numero <= 0:
        print("El número debe ser positivo. Inténtalo de nuevo.")
        continue

    sumaImpares = 0   
    for i in range(1, numero+1):
        if i % 2 == 1:
            sumaImpares += i

    print(f"La suma de los números impares entre 1 y {numero} es {sumaImpares}.")
    break
