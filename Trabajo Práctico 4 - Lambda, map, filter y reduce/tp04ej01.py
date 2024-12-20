"""1.	Crear funciones lambda que resuelvan las siguientes problemáticas:
a.	Calcule la superficie de un rectángulo
b.	Determine si una nota esta aprobada o no (mayor o igual que 4 aprueba). Retorna True por aprobado; False por desaprobado.
c.	Que dado un número invierta su signo (de positivo a negativo y viceversa)
d.	Que dado un nombre determine si su longitud es larga (mayor de 10 caracteres). Retorna True o False.
e.	Dado un valor numérico retorne True si es positivo o cero; False en caso contrario.
f.	Escribe una función que tome dos argumentos: a y b y devuelva la multiplicación de ellos.
g.	Que compare dos valores y retorne True si el primer argumento es mayor que el segundo"""

superficieTriangulo = lambda base, altura : base * altura
notaAprobada = lambda nota : nota >= 4
invertirSigno = lambda numero : -numero
longitudLarga = lambda nombre : len(nombre) > 10
numeroPositivoOCero = lambda numero : numero >= 0
multiplicacion = lambda a, b : a * b
compararValores = lambda valor1, valor2 : valor1 > valor2


print("superficieTriangulo --> ", superficieTriangulo(11,22))
print("notaAprobada --> ", notaAprobada(2))
print("notaAprobada --> ", notaAprobada(10))
print("invertirSigno --> ", invertirSigno(11))
print("invertirSigno --> ", invertirSigno(-11))
print("longitudLarga --> ", longitudLarga("Oliver"))
print("longitudLarga --> ", longitudLarga("Maximiliano"))
print("numeroPositivoOCero --> ", numeroPositivoOCero(-1))
print("numeroPositivoOCero --> ", numeroPositivoOCero(33))
print("multiplicacion --> ", multiplicacion(11,22))
print("compararValores --> ", compararValores(2,1))
print("compararValores --> ", compararValores(3,3))
