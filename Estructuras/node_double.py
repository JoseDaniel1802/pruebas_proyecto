from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T, prev_node=None, next_node=None):
        self.__data = data
        self.__prev: Node | None = prev_node
        self.__next: Node | None = next_node

    @property
    def data(self):
        return self.__data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, new_prev: Node[T]):
        self.__prev = new_prev

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new_next: Node[T]):
        self.__next = new_next

    def memory_address(self):
        return hex(id(self))

    def __str__(self):
        return str(self.__data)






