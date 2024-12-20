"""
5.	Una universidad cuenta con una cola de estudiantes y graduados, donde cada persona se representa mediante una tupla (<situación>, <DNI>) (la situación se codifica como 0: estudiante, 1: graduado) dividirla en dos colas según el nivel educativo de cada integrante.
"""

from cola import *

def dividirPorNivel(colaPersonas):
    colaEstudiantes = crearCola()
    colaGraduados = crearCola()

    while not estaVacia(colaPersonas):
        persona = desencolar(colaPersonas)
        situacion = persona[0]
        dni = persona[1]

        if situacion == 0:
            encolar(colaEstudiantes, (situacion, dni))
        elif situacion == 1:
            encolar(colaGraduados, (situacion, dni))

    return colaEstudiantes, colaGraduados

# Ejemplo de uso
colaPersonas = crearCola()

# Agregar personas a la cola original
encolar(colaPersonas, (0, "12345678"))  # Estudiante
encolar(colaPersonas, (1, "87654321"))  # Graduado
encolar(colaPersonas, (0, "98765432"))  # Estudiante
encolar(colaPersonas, (1, "23456789"))  # Graduado

# Dividir la cola de personas por nivel educativo
colaEstudiantes, colaGraduados = dividirPorNivel(colaPersonas)

# Mostrar las colas de estudiantes y graduados
print("Cola de Estudiantes:")
while not estaVacia(colaEstudiantes):
    persona = desencolar(colaEstudiantes)
    print(persona)

print("Cola de Graduados:")
while not estaVacia(colaGraduados):
    persona = desencolar(colaGraduados)
    print(persona)
