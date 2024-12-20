"""
17.	Escribe una función recursiva llamada multiplos que tome dos parámetros: numero y divisor. La función deberá contar y devolver la cantidad de números enteros en el rango de 1 a numero que son múltiplos de divisor. 

Por ejemplo, el llamado a la función multiplos(10, 3) debería retornar el valor 3. Debido a que los valores entre 1 y 10, que son divisibles por 3 son: 3, 6 y 9.
"""

def multiplos (numero, divisor):
    if numero == 0:
        return 0
    else:
        esDivisor = 0
        if numero % divisor == 0:
            esDivisor = 1
        return esDivisor + multiplos (numero-1, divisor)


print(multiplos(10, 3))