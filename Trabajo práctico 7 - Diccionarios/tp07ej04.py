"""
4.	Realice un programa que pida datos de personas: nombre, día de nacimiento, mes de nacimiento, y año de nacimiento. 
Después deberá repetir lo siguiente: preguntar un número de mes y mostrar en pantalla los datos de las personas que cumplan los 
años durante ese mes. Terminará de repetirse cuando se teclee vacío en el nombre. Persista y recupere la información en cada 
ejecución en un archivo llamado cumpleaños.json.
"""

import json

try:
    contenido = open("archivos/cumpleanios.json", "r")
    lineas = contenido.read()
    contenido.close()
    cumpleanios = json.loads(lineas)
except FileNotFoundError: 
    print("No se encontró el archivo de cumpleaños. Se creará si se agregan registros.")
    cumpleanios = []

nombre = "-"
while nombre != "":
    nombre = input("Ingrese el nombre de la persona: ")

    if nombre != "":
        dia = int(input("Ingrese el día de nacimiento: "))
        mes = int(input("Ingrese el mes de nacimiento: "))
        anio = int(input("Ingrese el anio de nacimiento: "))
        
        persona = {}
        persona["nombre"] = nombre
        persona["dia"] = dia
        persona["mes"] = mes
        persona["anio"] = anio

        cumpleanios.append(persona)

    cumpleaniosJSON = json.dumps(cumpleanios, indent=4)

try:
    contenido = open("archivos/cumpleanios.json", "w")
    contenido.write(cumpleaniosJSON)
    contenido.close()
except:
    print("No se puede grabar el archivo")

mes = int(input("Ingrese número del mes: "))
for cumpleanio in cumpleanios:
    if cumpleanio["mes"] == mes:
        print(cumpleanio["nombre"], " -> ", cumpleanio["dia"], "/", cumpleanio["mes"], "/", cumpleanio["anio"])
