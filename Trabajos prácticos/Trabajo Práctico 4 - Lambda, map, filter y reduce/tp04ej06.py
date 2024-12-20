"""6.	Modifique la función anterior, haciendo uso de filter, para poder obtener una lista de notas aprobadas y 
otro de desaprobadas."""

from tp04ej01 import notaAprobada

def booleanASiNo(valor):
    if valor == True:
        return "Si"
    else:
        return "No"

notas = []

while len(notas) < 10:
    nota = int(input("Ingrese una nota: "))
    notas.append(nota)

notasAprobadas = list(filter(notaAprobada, notas))
notasDesprobadas = list(filter(lambda nota : not notaAprobada(nota), notas))

print("NOTAS APROBADAS")
for nota in notasAprobadas:
    print(f"Nota: {nota}")

print("NOTAS DESAPROBADAS")
for nota in notasDesprobadas:
    print(f"Nota: {nota}")
