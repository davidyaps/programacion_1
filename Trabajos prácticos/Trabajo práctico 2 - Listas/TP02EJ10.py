"""
10. Una clínica necesita un programa para atender a sus pacientes. 
Cada paciente que ingresa se anuncia en la recepción indicando su número de afiliado (número entero de 4 dígitos) 
y además indica si viene por una urgencia (ingresando un 0) o con turno (ingresando un 1). 
Para finalizar se ingresa -1 como número de socio. Luego se solicita:

a.	Mostrar un listado de los pacientes atendidos por urgencia y un listado de los pacientes atendidos 
por turno en el orden que llegaron a la clínica.

b.	Realizar la búsqueda de un número de afiliado e informar cuántas veces fue atendido por turno y cuántas por urgencia.
Repetir esta búsqueda hasta que se ingrese -1 como número de afiliado.
"""

continuarCarga = True
continuarBusqueda = True
listaUrgencias = []
listaTurnos = []

while (continuarCarga):

    numeroAfiliado = int(input("Ingrese número de afiliado (cuatro dígitos). Ingrese -1 para finalizar: "))

    if (numeroAfiliado == -1):
        continuarCarga = False
    else:
        if (numeroAfiliado < 1000 or numeroAfiliado > 9999):
            print("El número de afiliado ingresado no es correcto")
        else:
            tipoAtencion = -1
            while (tipoAtencion != 0 and tipoAtencion != 1):
                tipoAtencion = int(input("¿El paciente viene por una urgencia (0) o con turno (1): "))
                if (tipoAtencion != 0 and tipoAtencion != 1):
                    print("Error. Debe ingresar 0 o 1.")
                else:
                    if (tipoAtencion == 0):
                        listaUrgencias.append(numeroAfiliado)
                        print("Se agregó el paciente a la lista de urgencias.")

                    if (tipoAtencion == 1):
                        listaTurnos.append(numeroAfiliado)
                        print("Se agregó el paciente a la lista de turnos.")

while (continuarBusqueda):
    numeroAfiliado = int(input("Ingrese el número de afiliado a buscar. Ingrese -1 para finalizar: "))
    
    if (numeroAfiliado == -1):
        continuarBusqueda = False
    else:
        if (numeroAfiliado < 1000 or numeroAfiliado > 9999):
            print("El número de afiliado ingresado no es correcto")
        else:
            print("Cantidad de turnos solicitados: ")
            print("Urgencias: ", listaUrgencias.count(numeroAfiliado))
            print("Turnos: ", listaTurnos.count(numeroAfiliado))