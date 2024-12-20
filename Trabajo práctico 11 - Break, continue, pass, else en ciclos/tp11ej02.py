"""2.	Escribe un programa que pida al usuario ingresar una cadena de caracteres y cuente cuántas veces aparece cada vocal en la cadena. El programa debe ignorar cualquier caracter que no sea una vocal y continuar con el siguiente caracter. Utilice for y continue para su resolución."""

cadena = input("Ingresa una cadena de caracteres: ")
vocales = "aeiouáéíóú"

resultados = []
for letra in cadena:
    if letra.lower() not in vocales:
        continue
    resultados.append(f"La letra '{letra}' aparece en la cadena {cadena.count(letra)} veces.")

for resultado in set(resultados):
    print(resultado)