"""4.	Escribe un programa que pida al usuario ingresar un número entero y determine si es un número primo. Si el número no es primo, el programa debe mostrar todos los factores del número que no son 1 ni el propio número. Utilice for, break, else para su resolución."""

numero = int(input("Ingresa un número entero: "))

for i in range(2, numero):
    if numero % i == 0:
        print(f"{numero} no es un número primo. Los factores son:")
        for j in range(2, numero):
            if numero % j == 0:
                print(j)
        break
else:
    print(f"{numero} es un número primo.")
