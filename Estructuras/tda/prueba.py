import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QFont
from node import Node
from stack import Stack  # Asegúrate de importar tu implementación de Stack y Node

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualización de Pila")
        self.stack = Stack()
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        # Controles para ingresar datos
        self.input_layout = QHBoxLayout()
        self.data_entry = QLineEdit()
        self.input_layout.addWidget(self.data_entry)
        self.insert_button = QPushButton("Insertar Nodo")
        self.insert_button.clicked.connect(self.insert_node)
        self.input_layout.addWidget(self.insert_button)
        self.layout.addLayout(self.input_layout)

        # Controles para eliminar nodo y mostrar la pila
        self.control_layout = QHBoxLayout()
        self.delete_button = QPushButton("Eliminar Nodo")
        self.delete_button.clicked.connect(self.delete_node)
        self.control_layout.addWidget(self.delete_button)
        self.show_stack_button = QPushButton("Mostrar Pila")
        self.show_stack_button.clicked.connect(self.show_stack)
        self.control_layout.addWidget(self.show_stack_button)
        self.layout.addLayout(self.control_layout)

        # Visualización de la pila
        self.stack_display = QVBoxLayout()
        self.layout.addLayout(self.stack_display)

        self.central_widget.setLayout(self.layout)

    def insert_node(self):
        data = self.data_entry.text()
        if data:
            self.stack.prepend(int(data))
            self.show_stack()

    def delete_node(self):
        try:
            self.stack.shift()
            self.show_stack()
        except Exception as e:
            print(e)  # Maneja el error como desees

    def show_stack(self):
        # Limpiar la visualización actual
        for i in reversed(range(self.stack_display.count())):
            widget = self.stack_display.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        # Mostrar la pila actualizada
        current = self.stack.head
        while current is not None:
            label = QLabel(f'Dato: {str(current)}, Espacio de memoria: (({current.memory_address()}))')
            label.setStyleSheet("border: 1px solid black; padding: 5px; margin: 5px;")
            label.setFont(QFont("Arial", 10))
            self.stack_display.addWidget(label)
            current = current.next

        self.central_widget.update()  # Actualizar la ventana principal

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
