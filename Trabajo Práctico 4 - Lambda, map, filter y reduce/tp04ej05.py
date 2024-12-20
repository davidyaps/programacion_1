"""5.	Utilizando map, crear un programa que cargue 10 notas de alumnos y, al finalizar, 
genere una nueva lista indicando el estado de aprobación (reutilice lo creado en el punto 1)."""

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

notasResultado = list(map(notaAprobada, notas))

for i in range(0, len(notas)):
    print(f"{i+1} -> Nota: {notas[i]} -> Aprobado: {booleanASiNo(notasResultado[i])}")

