from node_search import NodoArbol, T


class ArbolBusquedaBinaria:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor: T):
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual: NodoArbol, valor: T) -> NodoArbol:
        if nodo_actual is None:
            return NodoArbol(valor)

        if valor < nodo_actual.valor:
            nodo_actual.izquierda = self._insertar_recursivo(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._insertar_recursivo(nodo_actual.derecha, valor)

        return nodo_actual

    def eliminar(self, valor: T):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo_actual: NodoArbol, valor: T) -> NodoArbol:
        if nodo_actual is None:
            return None

        if valor < nodo_actual.valor:
            nodo_actual.izquierda = self._eliminar_recursivo(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, valor)
        else:
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda

            sucesor = self._encontrar_minimo(nodo_actual.derecha)
            nodo_actual.valor = sucesor.valor
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, sucesor.valor)

        return nodo_actual

    def _encontrar_minimo(self, nodo_actual: NodoArbol) -> NodoArbol:
        while nodo_actual.izquierda is not None:
            nodo_actual = nodo_actual.izquierda
        return nodo_actual

    def buscar(self, valor: T) -> NodoArbol:
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo_actual: NodoArbol, valor: T) -> NodoArbol:
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual

        if valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo_actual.derecha, valor)
