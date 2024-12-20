def crearCola():
    return []

def estaVacia(cola):
    return len(cola) == 0

def encolar(cola, elemento):
    cola.append(elemento)

def desencolar(cola):
    if estaVacia(cola):
        return None
    return cola.pop(0)

def frente(cola):
    if estaVacia(cola):
        return None
    return cola[0]
