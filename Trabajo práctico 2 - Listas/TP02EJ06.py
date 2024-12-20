"""
6.	Intercalar los elementos de una lista entre los elementos de otra. 
La intercalación deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará una lista nueva 
sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3] y lista2 = [5, 9, 7], 
lista1 deberá quedar como [8, 5, 1, 9, 3, 7].
"""

def intercalar(lista1, lista2):
    i=1
    for elemento in lista2:
        lista1[i:i] = [elemento]
        i = i+2


lista1 = [8, 1, 3]
lista2 = [5, 9, 7]

intercalar(lista1, lista2)

print(lista1)
