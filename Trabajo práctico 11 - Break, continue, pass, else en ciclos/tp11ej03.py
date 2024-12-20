"""3.	Escribe un programa que pida al usuario ingresar una lista de nombres y cree una nueva lista con los nombres que tienen más de 5 letras. Si no hay nombres con más de 5 letras, el programa debe crear una lista vacía."""

nombres = input("Ingresa una lista de nombres separados por espacios: ")
nombres = nombres.split()
nombresLargos = []

for nombre in nombres:
    if len(nombre) <= 5:
        pass
    else:
        nombresLargos.append(nombre)

print(f"Los nombres con más de 5 letras son: {nombresLargos}")
