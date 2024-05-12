from typing import TypeVar, Generic

from node_double import Node

T = TypeVar("T")


class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.__head: Node | None = None
        self.__tail: Node | None = None
        self.__size: int = 0
        self.tipo_data = None

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    def is_empty(self) -> bool:
        return self.__head is None and self.__tail is None

    def insert_empty(self, data: T):
        new_node = Node(data)
        self.__head = new_node
        self.__tail = new_node
        self.__size = 1

    def delete_by_index(self, index: int) -> T:
        if index < 0 or index >= len(self):
            raise IndexError("Índice fuera de rango")

        if index == 0:
            return self.shift()
        elif index == len(self) - 1:
            return self.pop()
        else:
            ref = self.find_at(index)
            prev_node = ref.prev
            next_node = ref.next
            prev_node.next = next_node
            if next_node is not None:  # Check if there's a next node
                next_node.prev = prev_node
            else:  # If the next node is None, then this node is the tail
                self.__tail = prev_node
            ref.next = None
            ref.prev = None
            self.__size -= 1
            return ref.data

    def prepend(self, data: T):
        if self.is_empty():
            self.insert_empty(data)
        else:
            new_node = Node(data)
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node
            self.__size += 1

    def append(self, data: T):
        if self.is_empty():
            self.insert_empty(data)
        else:
            new_node = Node(data)
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node
            self.__size += 1

    def transversal(self) -> str:
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data)
            if current is not self.__tail:
                result += "->"
            current = current.next
        return result

    def reverse_transversal(self) -> str:
        result = ""
        current = self.__tail
        while current is not None:
            result += str(current.data)
            if current is not self.__head:
                result += "->"
            current = current.prev
        return result

    def find_at(self, pos: int) -> Node:
        current_pos = 0
        ref = self.__head
        while ref is not None:
            if current_pos == pos:
                return ref
            else:
                ref = ref.next
                current_pos += 1

        raise Exception("NO EXISTE LA POSICIÓN")

    def find_by_index(self, index: int) -> T:
        if index < 0 or index >= len(self):
            raise IndexError("Índice fuera de rango")

        current_pos = 0
        current_node = self.__head
        while current_node is not None:
            if current_pos == index:
                return current_node.data
            current_node = current_node.next
            current_pos += 1

    def insert_at_index(self, index: int, data: T):
        if index < 0 or index > len(self):
            raise IndexError("Índice fuera de rango")

        if index == 0:
            self.prepend(data)
        elif index == len(self):
            self.append(data)
        else:
            ref = self.find_at(index - 1)
            new_node = Node(data)
            next_node = ref.next
            new_node.prev = ref
            new_node.next = next_node
            ref.next = new_node
            if next_node is not None:  # Check if there's a next node
                next_node.prev = new_node
            else:  # If the next node is None, then this new node becomes the tail
                self.__tail = new_node
            self.__size += 1

    def insert_at_post(self, pos: int, data: T):
        if pos == 0:
            self.prepend(data)
        elif pos == self.__size:
            self.append(data)
        elif pos > 0 and pos < self.__size:
            ref = self.find_at(pos - 1)
            next_node = ref.next
            new_node = Node(data)
            new_node.next = next_node
            new_node.prev = ref
            ref.next = new_node
            next_node.prev = new_node

            self.__size += 1
        else:
            raise IndexError("La posición está fuera del rango de la lista.")

    def insert_at_prev(self, pos: int, data: T):
        if pos == 0:
            self.prepend(data)
        else:
            ref = self.find_at(pos)
            prev_node = ref.prev
            new_node = Node(data)
            new_node.prev = prev_node
            new_node.next = ref
            ref.prev = new_node
            prev_node.next = new_node
            self.__size += 1

    def shift(self):
        if self.is_empty():
            raise Exception("LA LISTA ESTA VACIA")

        elif self.__head is self.__tail:
            ref = self.__head
            self.__head = None
            self.__tail = None
            self.__size = 0
            return ref
        else:
            ref = self.__head
            self.__head = ref.next
            ref.next = None
            self.__head.prev = None
            self.__size -= 1
            return ref

    def pop(self) -> Node:
        if self.is_empty():
            raise Exception("LA LISTA ESTA VACIA")
        elif self.__head is self.__tail:
            ref = self.__tail
            self.__head = None
            self.__tail = None
            self.__size = 0
            return ref
        else:
            ref = self.__tail
            self.__tail = self.__tail.prev
            self.__tail.next = None
            ref.prev = None
            self.__size -= 1
            return ref

    def get_index(self, ref: str) -> int:
        current = self.__head
        current_position = 0
        while current is not None:
            if str(current.data) == ref:
                return len(self) - current_position - 1
            else:
                current = current.next
                current_position += 1
        return -1

    def delete_at(self, pos: int) -> Node:
        if self.is_empty():
            raise Exception("LA LISTA ESTA VACIA")
        elif self.__head is self.__tail:
            ref = self.__tail
            self.__head = None
            self.__tail = None
            self.__size = 0
            return ref
        else:
            ref = self.find_at(pos)
            prev_node = ref.prev
            next_node = ref.next
            prev_node.next = next_node
            next_node.prev = prev_node
            ref.next = None
            ref.prev = None
            self.__size -= 1

            return ref

    def __len__(self):
        return self.__size

    def __iter__(self):
        current = self.__head
        while current is not None:
            yield current.data
            current = current.next

    def __str__(self):
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data)
            if current is not self.__tail:
                result += "<->"
            current = current.next
        return result

