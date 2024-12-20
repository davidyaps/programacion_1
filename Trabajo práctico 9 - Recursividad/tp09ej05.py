"""
5.	Escriba un programa utilizando recursividad, pueda retornar la multiplicación mediante el Método ruso, que consiste en:

•	Escribir los números (A y B) que se desea multiplicar en la parte superior de sendas columnas.
•	Dividir A entre 2, sucesivamente, ignorando el residuo, hasta llegar a la unidad. Escribir los resultados en la columna A.
•	Multiplicar B por 2 tantas veces como veces se ha dividido A entre 2. Escribir los resultados sucesivos en la columna B.
•	Sumar todos los números de la columna B que estén al lado de un número impar de la columna A. Éste es el resultado.

Ejemplo: 27 × 82

A	B	Sumandos
27	82	82
13	164	164
6	328	
3	656	656
1	1312	1312

Resultado: 2214
Nota: el resultado debe visualizarse en pantalla tal como en el ejemplo.

"""

def multiplicacionRusa (a, b):
    resultado = 0

    if a == 1:
        print(f"{a}\t{b}\t{b}")
        return b
    else:
        if a % 2 != 0:
            print(f"{a}\t{b}\t{b}")
            resultado += b
        else:
            print(f"{a}\t{b}")

        return resultado + multiplicacionRusa(a//2, b * 2)

    
print("A\tB\tSumandos")
print("\nResultado: ", multiplicacionRusa(11, 33))
    