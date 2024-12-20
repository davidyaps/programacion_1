"""2.	Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, 
sume ambos valores y devuelva el resultado como un número real. Devolver None si alguna de las cadenas no contiene un número válido, utilizando manejo de excepciones para detectar el error."""


def sumaReales(cadena1, cadena2):
    try:
        resultado = float(cadena1) + float(cadena2)
        return resultado
    except:
        return None

suma = sumaReales("22.1","11.2")

if suma != None:
    print(f"Resultado: {suma}")
else:
    print("No se pudo realizar la operación")
    