"""2.	Escriba un programa que lea datos de diez personas 
(nombre, edad, genero, dirección, teléfono), los almacene en 
un diccionario y los muestre. Al realizar dicha muestra, 
destacar la persona más joven en edad."""

personas = []
edad = 999
for i in range(0, 10):
    persona = {}
    persona["nombre"] = input("Ingrese nombre: ")
    persona["edad"] = int(input("Ingrese edad: "))
    persona["genero"] = input("Ingrese genero: ")
    persona["dirección"] = input("Ingrese dirección: ")
    persona["teléfono"] = input("Ingrese teléfono: ")
    
    if persona["edad"] < edad:
        edad = persona["edad"]
        
    personas.append(persona)
 
for persona in personas:
    print(f"Nombre: {persona['nombre']}")
    if persona["edad"] == edad:
        print(f"Edad: {persona['edad']} **MAS JOVEN")
    else:
        print(f"Edad: {persona['edad']}")
    print(f"Genero: {persona['genero']}")
    print(f"Dirección: {persona['dirección']}")
    print(f"Teléfono: {persona['teléfono']}")