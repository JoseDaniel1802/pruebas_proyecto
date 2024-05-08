from __future__ import annotations
from typing import TypeVar, Generic
from Estructuras.nodo import Node

T = TypeVar('T')


class CircularList(Generic[T]):
    def __init__(self):
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__size: int = 0
        self.__current: Node[T] | None = None

    def append(self, data: T):
        new_node = Node(data)

        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node

        new_node.next = self.__head
        self.__size += 1

    def prepend(self, data: T):
        new_node = Node(data)

        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node

        self.__tail.next = self.__head  # Enlazamos el último nodo con el primero
        self.__size += 1

    def __iter__(self):
        self.__current = self.__head
        return self

    def __next__(self):
        """if self.__current is None:
                    raise StopIteration"""

        if self.__current.data is self.__current.next.data:
            raise StopIteration

        data = self.__current.data
        self.__current = self.__current.next

        return data

    def is_empty(self) -> bool:
        return (self.__head is None and
                self.__tail is None)

    def search_by_value(self, value: T) -> int | None:
        if self.is_empty():
            return None

        current = self.__head
        index = 0

        while True:
            if current.data == value:
                return index
            current = current.next
            index += 1

            # Si hemos vuelto al inicio, significa que hemos recorrido toda la lista
            if current is self.__head:
                break

        return None

    def display(self):
        if self.is_empty():
            print("La lista está vacía")
            return

        current = self.__head
        print("Elementos de la lista:")
        while True:
            print(current.data)
            current = current.next
            if current is self.__head:
                break

    def shift(self):
        if self.is_empty():
            raise Exception("La lista está vacía")

        if self.__head is self.__tail:
            # Si solo hay un elemento en la lista
            removed_node = self.__head
            self.__head = None
            self.__tail = None
        else:
            removed_node = self.__head
            self.__head = self.__head.next
            self.__head.prev = self.__tail
            self.__tail.next = self.__head

        self.__size -= 1
        return removed_node

    def pop(self) -> T | None:
        if self.is_empty():
            return None

        if self.__head is self.__tail:
            removed_node = self.__head
            self.__head = None
            self.__tail = None
            self.__size = 0
        else:
            current = self.__head
            while current.next is not self.__tail:
                current = current.next
            removed_node = self.__tail
            current.next = self.__head
            self.__tail = current
            self.__size -= 1

        return removed_node.data

    def move_right(self, steps: int) -> None:
        if self.is_empty() or steps <= 0:
            return

        for _ in range(steps):
            self.__tail = self.__head
            self.__head = self.__head.next

    def move_left(self, steps: int) -> None:
        if self.is_empty() or steps <= 0:
            return

        for _ in range(steps):
            current = self.__head
            while current.next != self.__head:
                current = current.next
            self.__head = current
            self.__tail = current
    def __len__(self):
        return self.__size

    @property
    def head(self):
        return self.__head

    def tail(self):
        return self.__tail