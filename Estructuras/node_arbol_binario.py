from typing import TypeVar, Generic, Optional

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data  # Mantén los datos en su tipo original
        self.left: Optional['Node[T]'] = None
        self.right: Optional['Node[T]'] = None

    @staticmethod
    def compare(a: T, b: T) -> int:
        """Una función de comparación que maneja números y cadenas adecuadamente."""
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return (a > b) - (a < b)  # Comparación numérica
        else:
            # Convertir a cadena si alguno de los dos no es numérico
            a_str, b_str = str(a), str(b)
            if a_str < b_str:
                return -1
            elif a_str > b_str:
                return 1
            return 0

