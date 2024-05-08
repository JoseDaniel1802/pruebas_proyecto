class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Node | None = None

    def __str__(self):
        return str(self.data)

    def memory_address(self):
        return hex(id(self))

