from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T, next_node=None):
        self.__data = data
        self.__next: Node | None = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new_next: Node[T]):
        self.__next = new_next

    def __str__(self):
        return str(self.__data)

    def memory_address(self):
        return hex(id(self))

    @data.setter
    def data(self, value):
        self._data = value