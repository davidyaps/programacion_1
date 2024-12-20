"""
14.	Se cuenta con una lista en donde cada elemento es la cantidad de páginas de diferentes libros que leyó una persona. Se solicita realizar una función, utilizando recursividad, para obtener la suma total de las páginas leídas por la persona. 
Por ejemplo: 
Si tenemos la siguiente lista:  
libros = [150,100,300,120]
Se debería obtener lo siguiente: 
Total de páginas leídas: 670
"""

def totalPaginas(lista):
    if len(lista)==1:
        return lista[0]
    elif len(lista)==0:
        print('No hay libros')
        return 0
    else:
        return lista[0] + totalPaginas(lista[1:])

    
libros=[150,100,300,120]
print('total de paginas: ' , totalPaginas(libros))
    
libros=[]
print('total de paginas: ' , totalPaginas(libros))
    
libros=[120]
print('total de paginas: ' , totalPaginas(libros))