"""
8.	Sistema de calificaciones: Escribe un programa que permita a los profesores registrar las calificaciones de sus alumnos y les permita calcular la nota final. Crea un diccionario para cada alumno, con su legajo como clave y una lista de notas como valor. Luego, el programa debe permitir al usuario ingresar las notas para cada alumno y calcular su nota final, basándose en un sistema de pesos predeterminado.
"""

# Definir un diccionario vacío para almacenar las notas de los alumnos
alumnos = {}

# Pedir el número de alumnos y las notas
cantidad = int(input("Ingrese el número de alumnos: "))
for i in range(cantidad):
    legajo = input(f"Ingrese el legajo del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} del alumno {i+1}: "))
        notas.append(nota)
    alumnos[legajo] = notas

# Calcular la nota final de cada alumno y mostrarla
for legajo, notas in alumnos.items():
    nota_final = sum(notas) / len(notas)
    print(f"La nota final del alumno {legajo} es: {nota_final}")
