"""
15.	Se solicita realizar una función, utilizando recursividad, para poder invertir los caracteres de una frase dada. 
Por ejemplo, si se cuenta con la siguiente frase: "Hola, buenas noches"
La función debería retornar: "sehcon saneub ,aloH"
"""

def invertirFrase(palabra):
    if len(palabra)==1:
        return palabra
    else:
        return palabra[-1] + invertirFrase(palabra[:-1])
    
palabra = 'Hola mundo'
print(palabra)
print(invertirFrase(palabra))