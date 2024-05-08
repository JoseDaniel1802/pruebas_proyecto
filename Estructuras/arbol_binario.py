from typing import Optional, TypeVar, Generic
from node_arbol_binario import Node

T = TypeVar("T")


class BinaryTree(Generic[T]):
    def __init__(self):
        self.root: Node[T] | None = None

    # FUNCION  PARA CALCULAR LA ALTURA DEL ARBOl
    def altura(self, subtree: Node[T]):

        if subtree is None:
            return 0

        return 1 + max(self.altura(subtree.left), self.altura(subtree.right))

    def insert_left(self, data, ref=None):
        if ref is None:
            if self.root is None:
                self.root = Node(data)
                print("Nuevo nodo establecido como raíz.")
            else:
                raise ValueError("El árbol ya tiene una raíz. Especifique un nodo de referencia para insertar.")
        else:
            parent_node = self.search(ref, self.root)
            if parent_node is not None:
                if parent_node.left is None:
                    parent_node.left = Node(data)
                    print(f"Nodo insertado a la izquierda de {ref}.")
                else:
                    raise ValueError("El nodo ya tiene un hijo izquierdo.")
            else:
                raise ValueError("Nodo de referencia no encontrado.")

    def insert_right(self, data, ref=None):
        if ref is None:
            raise ValueError("Debe especificar un nodo de referencia para insertar a la derecha.")
        else:
            parent_node = self.search(ref, self.root)
            if parent_node is not None:
                if parent_node.right is None:
                    parent_node.right = Node(data)
                    print(f"Nodo insertado a la derecha de {ref}.")
                else:
                    raise ValueError("El nodo ya tiene un hijo derecho.")
            else:
                raise ValueError("Nodo de referencia no encontrado.")

    def search_by_value(self, data, node, path=None):
        if node is None:
            return None
        if path is None:
            path = []  # Inicializa la lista de camino solo en la primera llamada

        path.append(node)  # Agregar el objeto nodo actual al camino
        print(f"Visitando nodo: {node.data}, camino actual: {[n.data for n in path]}")

        # Verificar si el nodo actual contiene el dato buscado
        if int(node.data) == int(data):
            print(f"Dato encontrado: {data} en el nodo {node.data}, camino final: {[n.data for n in path]}")
            return node, path  # Devuelve el nodo y el camino recorrido hasta él

        # Búsqueda en el subárbol izquierdo
        left_result = None
        if node.left is not None:
            print(f"Buscando a la izquierda de {node.data}")
            left_result = self.search_by_value(data, node.left, path)
            if left_result is not None:
                return left_result

        # Búsqueda en el subárbol derecho
        right_result = None
        if node.right is not None:
            print(f"Buscando a la derecha de {node.data}")
            right_result = self.search_by_value(data, node.right, path)
            if right_result is not None:
                return right_result

        # Si el nodo no es encontrado en ninguno de los subárboles y no es el nodo buscado, remover del camino
        if left_result is None and right_result is None:
            path.pop()  # Solo quitar el último nodo añadido si no condujo al nodo buscado
            print(f"Nodo {node.data} no contiene el dato y no fue encontrado en sus subárboles, removiendo de camino.")

        return None

    def search(self, data, node):
        if node is None:
            return None
        elif node.data == data:
            return node
        else:
            left_result = self.search(data, node.left)
            if left_result is not None:
                return left_result
            return self.search(data, node.right)

    def is_empty(self) -> bool:
        return self.root is None

    def __preorder(self, subtree: Node[T] | None) -> str:
        if subtree is None:
            return "None"
        else:
            root = str(subtree.data)
            left = self.__preorder(subtree.left)
            right = self.__preorder(subtree.right)
            result = f"{root}({left},{right})"
            return result

    def preorder(self):
        return self.__preorder(self.root)

    def __inorden(self, subtree: Node[T] | None) -> str:
        if subtree is None:
            return "None"
        else:
            root = str(subtree.data)
            left = self.__inorden(subtree.left)
            right = self.__inorden(subtree.right)
            result = f"{left}({root},{right})"
            return result

    def inorden(self):
        return self.__inorden(self.root)

    def __postorden(self, subtree: Node[T] | None) -> str:
        if subtree is None:
            return "None"
        else:
            root = str(subtree.data)
            left = self.__postorden(subtree.left)
            right = self.__postorden(subtree.right)
            result = f"{left}({right},{root})"
            return result

    def postorden(self):
        return self.__postorden(self.root)

    def get_path(self, ref: T, subtree: Node[T] | None) -> str:
        if subtree is None:
            return ""
        else:
            root = subtree.data
            if root == ref:
                return root

            left = self.get_path(ref, subtree.left)

            if left != "":
                return f"left --> {left}"

            rigth = self.get_path(ref, subtree.right)

            if rigth != "":
                return f"rigth --> {rigth}"
            else:
                return ""

    def get_path_data(self, ref: T, subtree: Node[T] | None) -> str:
        path = self._get_path_helper(ref, subtree)
        if path:
            return " --> ".join(map(str, path))
        else:
            return "Valor no encontrado en el árbol."

    def _get_path_helper(self, ref: T, subtree: Node[T] | None, path: list = None) -> list:
        if path is None:
            path = []
        if subtree is None:
            return []
        elif subtree.data == ref:
            # Añade el valor actual al camino y retorna el camino
            return path + [subtree.data]
        else:
            # Prueba primero por la izquierda
            left_path = self._get_path_helper(ref, subtree.left, path + [subtree.data])
            if left_path:
                return left_path

            # Si no se encontró por la izquierda, prueba por la derecha
            right_path = self._get_path_helper(ref, subtree.right, path + [subtree.data])
            if right_path:
                return right_path

            # Si no se encontró el valor, retorna una lista vacía
            return []

    def insert(self, data: T):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node: Node[T], data: T):
        comp_result = Node.compare(data, node.data)
        if comp_result < 0:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        elif comp_result > 0:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def print_tree(self, node=None, prefix=""):
        if node is None:
            node = self.root
        if node is not None:
            if node.right is not None:
                self.print_tree(node.right, prefix + "    ")
            print(prefix + "-> " + str(node.data))
            if node.left is not None:
                self.print_tree(node.left, prefix + "    ")

    def search_min_node(self, subtree):
        if subtree is None:
            return None

        # Recursivamente busca el nodo con el valor mínimo en el subárbol izquierdo
        if subtree.left is not None:
            return self.search_min_node(subtree.left)

        # Si no hay más nodos a la izquierda, este es el nodo con el valor mínimo
        return subtree

    def search_max(self, subtree):
        # Caso base: Si el nodo es None, simplemente retornar None
        if subtree is None:
            return None

        # Comenzar asumiendo que el nodo actual es el máximo
        node_maximo = subtree

        # Buscar recursivamente el nodo máximo en el subárbol izquierdo
        if subtree.left is not None:
            left_max_node = self.search_max(subtree.left)
            if left_max_node is not None and left_max_node.data > node_maximo.data:
                node_maximo = left_max_node

        # Buscar recursivamente el nodo máximo en el subárbol derecho
        if subtree.right is not None:
            right_max_node = self.search_max(subtree.right)
            if right_max_node is not None and right_max_node.data > node_maximo.data:
                node_maximo = right_max_node

        # Devolver el nodo que contiene el valor máximo encontrado
        return node_maximo

    def delete(self, data: T) -> bool:
        self.root, deleted = self._delete_recursive(self.root, data)
        return deleted

    def _delete_recursive(self, subtree: Node, data) -> tuple[Optional[Node], bool]:
        if subtree is None:
            # Si el subárbol está vacío, no hay nada que eliminar
            return None, False

        if data == subtree.data:
            # Nodo encontrado
            if subtree.left is None and subtree.right is None:
                # El nodo es una hoja
                return None, True
            elif subtree.left is None:
                # Solo tiene hijo derecho
                return subtree.right, True
            elif subtree.right is None:
                # Solo tiene hijo izquierdo
                return subtree.left, True
            else:
                # Tiene dos hijos
                max_node = self.search_max(subtree.left)
                subtree.data = max_node.data  # Asegúrate que max_node es un Nodo y no un entero
                subtree.left, _ = self._delete_recursive(subtree.left, max_node.data)
                return subtree, True
        else:
            # Continuar búsqueda en los subárboles
            subtree.left, deleted_left = self._delete_recursive(subtree.left, data)
            subtree.right, deleted_right = self._delete_recursive(subtree.right, data)
            return subtree, deleted_left or deleted_right

    def insert_into_tree(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.data:
                root.left = self.insert_into_tree(root.left, key)
            else:
                root.right = self.insert_into_tree(root.right, key)
        return root
