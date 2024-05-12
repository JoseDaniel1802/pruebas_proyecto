from __future__ import annotations
from typing import TypeVar, Generic
from node_double import  Node

T = TypeVar('T')


class CircularDoublyLinkedList(Generic[T]):
    def __init__(self):
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__size: int = 0
        self.tipo_data = None
        self.count = 0

    def is_empty(self) -> bool:
        return self.__head is None and self.__tail is None

    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.prev = self.__tail
            new_node.next = self.__head
            self.__tail.next = new_node
            self.__head.prev = new_node
            self.__tail = new_node
        self.__size += 1

    def prepend(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            new_node.prev = self.__tail
            self.__head.prev = new_node
            self.__tail.next = new_node
            self.__head = new_node
        self.__size += 1

    def insert_at(self, data: T, pos: int):
        if pos < 0 or pos > len(self):
            raise IndexError('La posición es inválida')
        elif pos == 0:
            self.prepend(data)
        elif pos == len(self):
            self.append(data)
        else:
            new_node = Node(data)
            current_node = self.find_at(pos)
            new_node.prev = current_node.prev
            new_node.next = current_node
            current_node.prev.next = new_node
            current_node.prev = new_node
            self.__size += 1

    def find_at(self, pos: int) -> Node[T]:
        current_pos = 0
        current_node = self.__head
        while current_pos < pos:
            current_node = current_node.next
            current_pos += 1
        return current_node

    def remove_at(self, pos: int) -> T:
        if pos < 0 or pos >= len(self):
            raise IndexError('La posición no existe')
        elif pos == 0:
            return self.shift()
        elif pos == len(self) - 1:
            return self.pop()
        else:
            current_node = self.find_at(pos)
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            current_node.prev = None
            current_node.next = None
            self.__size -= 1
            return current_node.data

    def shift(self) -> T:
        if self.is_empty():
            raise OverflowError("La lista está vacía")
        elif self.__head is self.__tail:
            current_node = self.__head
            self.__head = None
            self.__tail = None
        else:
            current_node = self.__head
            self.__head = current_node.next
            self.__head.prev = self.__tail
            self.__tail.next = self.__head
        self.__size -= 1
        return current_node.data

    def pop(self) -> T:
        if self.is_empty():
            raise OverflowError("La lista está vacía")
        elif self.__head is self.__tail:
            current_node = self.__head
            self.__head = None
            self.__tail = None
        else:
            current_node = self.__tail
            self.__tail = current_node.prev
            self.__tail.next = self.__head
            self.__head.prev = self.__tail
        self.__size -= 1
        return current_node.data

    def get_index(self, item: str) -> int:
        current_node = self.__head
        index = 0
        while current_node is not None:
            if str(current_node.data) == item:
                return index
            current_node = current_node.next
            index += 1
            if current_node == self.__head:  # Break if we have traversed the whole list
                break
        return -1

    def __len__(self):
        return self.__size

    def __iter__(self):
        current_node = self.__head
        for _ in range(len(self)):
            yield current_node.data
            current_node = current_node.next

    def __str__(self):
        return "\n".join(map(str, self))

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

