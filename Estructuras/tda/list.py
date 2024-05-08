
from typing import TypeVar, Generic

from Estructuras.nodo import Node

T = TypeVar('T')


class List(Generic[T]):
    def __init__(self):
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__size = 0
        self.__current: Node[T] | None = None
        self.tipo_data = None

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    def is_empty(self):
        return self.__head is None and self.__tail is None

    # Metodos de inserción
    def append(self, data: [T]):  # agrega elementos al final
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = self.__head
            self.__size += 1
        else:
            self.__tail.next = new_node
            self.__tail = new_node
            self.__size += 1

    def prepend(self, data: T):  # agrega elementos al principio
        new_node = Node(data, self.__head)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
            self.__size += 1
        else:
            self.__head = new_node
            self.__size += 1

    def insert_at(self, data: T, index: int):
        if index < 0 or index > len(self):
            raise IndexError('La posición es inválida')
        elif index == 0:
            self.prepend(data)
        elif index == len(self):
            self.append(data)
        else:
            new_node = Node(data)
            previous_node = self.find_at(index - 1)
            new_node.next = previous_node.next
            previous_node.next = new_node
            self.__size += 1

    # Metodos de eliminación

    def shift(self) -> T:  # elimina el primer elemento
        if self.is_empty():
            raise ReferenceError('No hay datos')
        elif self.__head is self.__tail:
            current = self.__head
            self.__head = None
            self.__tail = None
            self.__size = 0
            return current.data
        else:
            current = self.__head
            self.__head = current.next
            current.next = None
            self.__size -= 1

            return current.data

    def get_index(self, value: str) -> int:
        current = self.__head
        index = 0
        while current is not None:
            if str(current.data) == value:
                return index
            current = current.next
            index += 1
        return -1

    def pop(self) -> T:  # Elimina el ultimo elemento
        if self.is_empty():
            raise Exception('Subdesbordamiento de lista')
        elif self.__head is self.__tail:
            current = self.__head
            self.__head = None
            self.__tail = None
            self.__size = 0

            return current.data
        else:
            current = self.__tail
            previous = self.find_at(self.__size - 2)
            self.__tail = previous
            previous.next = None
            self.__size -= 1

            return current.data

    def remove_at(self, index: int) -> T:
        if index < 0 or index >= len(self):
            raise IndexError('La posición no existe')
        elif index == 0:
            return self.shift()
        elif index == len(self) - 1:
            return self.pop()
        else:
            current = self.find_at(index)
            previous = self.find_at(index - 1)
            next_node = current.next
            previous.next = next_node
            current.next = None
            self.__size -= 1

            return current.data

    # Metodos de busqueda

    def find_at(self, index: int) -> Node[T]:
        current_index = 0
        current = self.__head

        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range")

        while True:
            if current is None:
                break
            elif current_index == index:
                return current
            else:
                current = current.next
                current_index += 1

    def transversal(self):
        current = self.__head
        result = ''
        while current is not None:
            result += str(current)
            current = current.next

            if current is not None:
                result += '\n'

        return result

    def __iter__(self):
        self.__current = self.__head

        return self

    def __next__(self):
        if self.__current is None:
            raise StopIteration

        data = self.__current.data
        current = self.__current
        self.__current = self.__current.next
        return data

    def __len__(self):
        size = 0
        current_node = self.__head
        while current_node is not None:
            size += 1
            current_node = current_node.next
        return size

    def __reversed__(self):
        current = self.__tail

        while current is not None:
            yield current.data
            current = self.find_previous(current)

    def find_previous(self, node: Node[T]) -> Node[T]:
        current = self.__head
        while current is not None and current.next is not node:
            current = current.next
        return current

    def replace_data(self, old_text, new_text):
        count = 0
        current = self.__head
        while current is not None:
            if old_text in current.data:
                occurrences = current.data.count(old_text)
                current.data = current.data.replace(old_text, new_text)
                count += occurrences
            current = current.next
        return count
