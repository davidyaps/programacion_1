"""
7.	Escribe una función que extraiga todos los hashtags de una cadena dada. Un hashtag se define como cualquier secuencia de caracteres alfanuméricos precedida por un símbolo # y puede contener letras, números y guiones bajos. La función debe devolver una lista con todos los hashtags encontrados en la cadena.
"""

import re

def extraerHashtags(cadena):
    patron = '#[a-zA-Z0-9_]+'
    hashtags = re.findall(patron, cadena)
    return hashtags

print(extraerHashtags("Estos son algunos hashtags: #Python, #Programación_1, y #1"))
