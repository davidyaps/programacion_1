def crearPila():
    return []

def estaVacia(pila):
    return len(pila) == 0

def apilar(pila, elemento):
    pila.append(elemento)

def desapilar(pila):
    if estaVacia(pila):
        return None
    return pila.pop()

def tope(pila):
    if estaVacia(pila):
        return None
    return pila[-1]
