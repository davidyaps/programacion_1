"""3.	Desarrollar una función que devuelva una cadena de caracteres con el nombre del mes cuyo número se recibe como parámetro. 
Los nombres de los meses deberán obtenerse de una tupla de cadenas de caracteres inicializada dentro de la función. 
Devolver una cadena vacía si el número de mes es inválido. La detección de meses inválidos deberá realizarse a través de excepciones."""


def mesNombre(mes):
    meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

    try:
        return meses[mes-1]
    except:
        return ""

for i in range(1, 14):
    print(f"Mes {i}: {mesNombre(i)}")

    