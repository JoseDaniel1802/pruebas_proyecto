from typing import TypeVar

T = TypeVar("T")

class NodoArbol:
    def __init__(self, valor: T):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
