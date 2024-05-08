from typing import TypeVar, Generic

T = TypeVar('T')


class Node:
    def __init__(self, data: T):
        self.data = data
        self.next: Node | None = None

    def __str__(self):
        return self.data

    def memory_address(self):
        return hex(id(self))


class Queue(Generic[T]):
    def __init__(self, max: int | None = None):
        self.size = 0
        self.max = max
        self.tipo_data = None
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None

    def is_empty(self) -> bool:
        return self.head is None and self.tail is None

    def append(self, data: T):
        if self.size == self.max:
            raise OverflowError
        else:
            if self.is_empty():
                new_node = Node(data)
                self.head = new_node
                self.tail = new_node
                self.size += 1
            else:
                new_node = Node(data)
                self.tail.next = new_node
                self.tail = new_node
                self.size += 1

    def pop(self) -> T:
        if self.is_empty():
            raise Exception('Subdesbordamiento')
        elif self.head is self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return current.data
        else:
            current = self.head
            self.head = self.head.next
            current.next = None
            self.size -= 1

            return current.data

    def transversal(self) -> str:
        current = self.head
        result = ''
        while current is not None:
            result += (f'Dato: {str(current.data)}, '
                       f'Espacio de memoria: ({current.memory_address()})')
            current = current.next

            if current is not None:
                result += '->\n'

        return result

    def search_by_value(self, value: T) -> int | None:
        current = self.head
        index = 0
        while current is not None:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return None

    def get_index(self, value: str) -> int:
        current = self.head
        index = 0
        while current is not None:
            if str(current.data) == value:
                return index
            current = current.next
            index += 1
        return -1

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self) -> int:
        return self.size


