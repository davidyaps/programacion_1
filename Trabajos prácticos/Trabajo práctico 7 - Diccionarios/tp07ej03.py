"""
3.	Hacer un programa que registre 10 alumnos y guarde: nombre, nombre de la asignatura y 4 notas. Calcular y mostrar el promedio de las notas.
"""

alumnos = []

for i in range (0, 1):
    nombre = input("Ingrese nombre: ")
    asignatura = input("Nombre de la asignatura: ")

    notas = []
    for j in range(0, 4):
        nota = int(input(f"Ingrese la nota {j+1}: "))
        notas.append(nota)

    alumno = {}
    alumno["nombre"] = nombre
    alumno["asignatura"] = asignatura
    alumno["notas"] = notas

    alumnos.append(alumno)

for alumno in alumnos:
    print("Nombre: ", alumno["nombre"])
    print("Asignatura: ", alumno["asignatura"])
    print("Promedio: ", sum(alumno["notas"])/len(alumno["notas"]))
    print("===============================================")

