import sys
from typing import TypeVar

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QWidget, QMessageBox, QScrollArea
from PyQt6.QtCore import Qt
from doubly_linked_list import DoublyLinkedList  # Importa la clase DoublyLinkedList que definimos anteriormente

T = TypeVar("T")

class CircularDoublyLinkedListGUI(QMainWindow):
    def __init__(self, linked_list: DoublyLinkedList[T]):
        super().__init__()
        self.setWindowTitle("Lista Doblemente Enlazada Circular")
        self.setGeometry(100, 100, 800, 400)

        self.list = linked_list

        self.input_data = QLineEdit(self)
        self.input_data.setGeometry(50, 50, 200, 30)

        self.btn_insert_beginning = QPushButton("Insertar al Principio", self)
        self.btn_insert_beginning.setGeometry(50, 100, 150, 30)
        self.btn_insert_beginning.clicked.connect(self.insert_at_beginning)

        self.btn_insert_end = QPushButton("Insertar al Final", self)
        self.btn_insert_end.setGeometry(250, 100, 150, 30)
        self.btn_insert_end.clicked.connect(self.insert_at_end)

        self.btn_remove_beginning = QPushButton("Eliminar al Principio", self)
        self.btn_remove_beginning.setGeometry(450, 100, 150, 30)
        self.btn_remove_beginning.clicked.connect(self.remove_at_beginning)

        self.btn_remove_end = QPushButton("Eliminar al Final", self)
        self.btn_remove_end.setGeometry(650, 100, 150, 30)
        self.btn_remove_end.clicked.connect(self.remove_at_end)

        self.btn_search = QPushButton("Buscar Valor", self)
        self.btn_search.setGeometry(50, 150, 150, 30)
        self.btn_search.clicked.connect(self.search_value)

        self.btn_rotate_left = QPushButton("Rotar a la Izquierda", self)
        self.btn_rotate_left.setGeometry(250, 150, 150, 30)
        self.btn_rotate_left.clicked.connect(self.rotate_left)

        self.btn_rotate_right = QPushButton("Rotar a la Derecha", self)
        self.btn_rotate_right.setGeometry(450, 150, 150, 30)
        self.btn_rotate_right.clicked.connect(self.rotate_right)

        self.container = QWidget(self)
        self.container_layout = QHBoxLayout(self.container)
        self.container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)  # Alinear a la izquierda

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setGeometry(50, 200, 700, 100)
        self.scroll_area.setWidget(self.container)

        self.update_display()

    def insert_at_beginning(self):
        data = self.input_data.text()
        if data:
            self.list.prepend(data)
            self.update_display()

    def insert_at_end(self):
        data = self.input_data.text()
        if data:
            self.list.append(data)
            self.update_display()

    def remove_at_beginning(self):
        removed_node = self.list.remove_first()
        if removed_node:
            QMessageBox.information(self, "Elemento Eliminado", f"Elemento eliminado al principio: {removed_node.data}")
            self.update_display()
        else:
            QMessageBox.warning(self, "Lista Vacía", "La lista está vacía")

    def remove_at_end(self):
        removed_node = self.list.remove_last()
        if removed_node:
            QMessageBox.information(self, "Elemento Eliminado", f"Elemento eliminado al final: {removed_node.data}")
            self.update_display()
        else:
            QMessageBox.warning(self, "Lista Vacía", "La lista está vacía")

    def search_value(self):
        value = self.input_data.text()
        if value:
            found_node = self.list.search(value)
            if found_node:
                QMessageBox.information(self, "Valor Encontrado", f"Valor encontrado: {value} ({hex(id(found_node))})")
            else:
                QMessageBox.warning(self, "Valor No Encontrado", f"El valor {value} no está en la lista")
        else:
            QMessageBox.warning(self, "Campo Vacío", "Por favor ingrese un valor para buscar")

    def rotate_left(self):
        self.list.rotate_left()
        self.update_display()

    def rotate_right(self):
        self.list.rotate_right()
        self.update_display()

    def update_display(self):
        # Limpiar la visualización actual
        for i in reversed(range(self.container_layout.count())):
            widget = self.container_layout.itemAt(i).widget()
            self.container_layout.removeWidget(widget)
            widget.setParent(None)

        # Mostrar los datos de la lista en cuadrados y flechas
        elements = self.list.transversal().split("->")
        for element in elements:
            label = QLabel(element.strip(), self)
            label.setStyleSheet("border: 1px solid black; padding: 5px; background-color: lightblue;")  # Estilo CSS para el fondo celeste
            self.container_layout.addWidget(label)

            # Agregar la flecha después de cada cuadro excepto el último
            if element != elements[-1]:
                arrow_label = QLabel(" <--> ", self)
                self.container_layout.addWidget(arrow_label)

        self.input_data.clear()  # Limpiar el campo de entrada después de la inserción

if __name__ == "__main__":
    app = QApplication(sys.argv)
    linked_list = DoublyLinkedList[str]()  # Crear una instancia de la lista doblemente enlazada
    window = CircularDoublyLinkedListGUI(linked_list)
    window.show()
    sys.exit(app.exec())
