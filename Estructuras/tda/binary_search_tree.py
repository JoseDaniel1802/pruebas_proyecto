from typing import Generic, TypeVar, Literal

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def hos_children(self) -> Literal["left", "right", "both", "none"]:
        if self.left is None and self.right is None:
            return "none"
        elif self.left is not None and self.right is not None:
            return "both"
        elif self.left is not None and self.right is None:
            return "left"
        elif self.left is None and self.right is not None:
            return "right"

    def __str__(self):
        return str(self.data)


class BinarySearchTree(Generic[T]):

    def __init__(self):
        self.__root: Node | None = None

    @property
    def root(self):
        return self.__root

    def __preorder(self, subtree: Node | None) -> str:
        if subtree is None:
            return "None"
        else:
            root = str(subtree.data)  # obtener la raiz del arbol
            left = self.__preorder(subtree.left)  # se va ir al subarbol izquierda
            right = self.__preorder(subtree.right)  # se va ir al subarbol derecho
            result = f"{root} ({left}, {right})"
            return result

    def __search(self, ref: T, subtree: Node | None, path: str = "") -> str:
        if subtree is None:
            return "None"
        else:
            root = subtree.data
            if ref < root:
                return self.__search(ref, subtree.left, path + "->" + str(root))
            elif ref > root:
                return self.__search(ref, subtree.right, path + "->" + str(root))
            elif ref == root:
                return path + "->" + str(root)

    def preorder(self):
        return self.__preorder(self.__root)

    def __insert(self, data: T, subtree: Node[T]):
        if data < subtree.data:
            left = subtree.left
            if left is None:
                new_node = Node(data)
                subtree.left = new_node
            else:
                self.__insert(data, left)
        elif data > subtree.data:
            right = subtree.right
            if right is None:
                new_node = Node(data)
                subtree.right = new_node
            else:
                self.__insert(data, right)

    def insert(self, data: T):
        if self.__root is None:
            self.__root = Node(data)
        else:
            self.__insert(data, self.__root)

    def search(self, ref: T):
        return self.__search(ref, self.__root)

    def __delete(self, data: T, subtree: Node | None, father: Node | None) -> Node | None:
        if subtree is None:
            return None
        if subtree.data == data:
            if subtree.is_leaf():
                if subtree is self.__root:
                    self.__root = None
                else:
                    if subtree.data < father.data:
                        father.left = None
                    elif subtree.data > father.data:
                        father.right = None
            else:
                if subtree.hos_children() == "none":
                    pass
                elif subtree.hos_children() == "both":
                    right = subtree.right
                    child_parent = subtree
                    child = right
                    while right.left is not None:
                        child_parent = right
                        child = right.left
                        right = right.left
                    # if child.right is not None:
                    if child_parent.left is child:
                        # El hijo esta a la izquierda
                        child_parent.left = child.right
                    else:
                        # El hijo esta a la derecha
                        child_parent.right = child.right
                    if father is not None:
                        if child.data < father.data:
                            father.left = child
                        elif child.data > father.data:
                            father.right = child
                    else:
                        self.__root = child
                    child.left = subtree.left
                    subtree.left = None
                    child.right = subtree.right
                    subtree.right = None

                elif subtree.hos_children() == "left":
                    child = subtree.left
                    if subtree == self.__root:
                        subtree.left = None
                        self.__root = child
                    else:
                        if subtree.data < father.data:
                            father.left = None
                            subtree.left = None
                            father.left = child
                        elif subtree.data > father.data:
                            father.right = None
                            subtree.left = None
                            father.right = child
                elif subtree.hos_children() == "right":
                    child = subtree.right
                    if subtree == self.__root:
                        subtree.right = None
                        self.__root = child
                    else:
                        if subtree.data < father.data:
                            father.left = None
                            subtree.right = None
                            father.left = child
                        elif subtree.data > father.data:
                            father.right = None
                            subtree.right = None
                            father.right = child
            return subtree
        elif data < subtree.data:
            return self.__delete(data, subtree.left, subtree)
        elif data > subtree.data:
            return self.__delete(data, subtree.right, subtree)

    def delete(self, data: T) -> Node:
        return self.__delete(data, self.__root, None)

    def __min(self, subtree: Node | None) -> Node | None:
        if subtree is not None:
            if subtree.is_leaf():
                return subtree.data
            else:
                return self.__min(subtree.left)
        else:
            return None

    def __max(self, subtree: Node | None) -> Node | None:
        if subtree is not None:
            if subtree.is_leaf():
                return subtree.data
            else:
                return self.__max(subtree.right)
        else:
            return None

    def min(self):
        return self.__min(self.__root)
        # mas a la izquierda

    def max(self):
        return self.__max(self.__root)
