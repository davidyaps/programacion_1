"""4.	Escribir una función filtrarPalabras() que reciba una cadena de caracteres conteniendo una frase y un entero N, 
y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original. 
Escribir también un programa para verificar el comportamiento de la misma. 
"""
def longitudPalabraAlfanumerico(palabra):
    cantidad = 0
    for letra in palabra:
        if (letra.isalnum()):
            cantidad += 1
            
    return cantidad

def filtrarPalabras(frase, cantidad):
    listaPalabras = frase.split()
    
    resultado = [ palabra for palabra in listaPalabras if longitudPalabraAlfanumerico(palabra) >= cantidad ]
    
    return " ".join(resultado)
            
    
frase = "Hola... soy Troy McClure"
print(f"Resultado: \"{filtrarPalabras(frase, 4)}\"")