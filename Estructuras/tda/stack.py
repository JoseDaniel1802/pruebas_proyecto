
from __future__ import annotations
from typing import TypeVar, Generic
from Estructuras.nodo import Node

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self, limit: int | None = None):
        self.size = 0
        self.max = limit
        self.head: Node[T] | None = None
        self.tipo_data = None

    def prepend(self, data: T):
        if self.size == self.max:
            raise Exception('Desbordamiento de pila')
        else:
            new_node = Node[T](data)
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def shift(self) -> T:
        if self.head is None:
            raise Exception('Subdesbordamiento de pila')
        else:
            current = self.head
            self.head = current.next
            current.next = None
            self.size -= 1

            return current.data

    def transversal(self):
        current = self.head
        result = ''
        while current is not None:
            result += (f'Dato: {str(current)}, '
                       f'Espacio de memoria: (({current.memory_address()}))')
            current = current.next

            if current is not None:
                result += '->\n'

        return result

    def get_index(self, value: str) -> int:
        current = self.head
        index = 0
        while current is not None:
            if str(current.data) == value:
                return index
            current = current.next
            index += 1
        return -1

    def search_by_value(self, value: T) -> T:
        current = self.head
        index = 0

        while current is not None:
            if current.data == value:
                return index
            current = current.next
            index += 1

        return -1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __len__(self):
        return self.size


