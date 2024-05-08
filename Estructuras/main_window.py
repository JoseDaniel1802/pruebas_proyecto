import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPixmap, QFont, QIcon
from pila_window import StackWindow
from cola_window import QueueWindow
from lista_simple_window import ListWindow
from lista_circular_window import CircularListWindow
from lista_doble_window import ListDoubleWindow
from lista_circular_doble_window import CircularDoublyLinkedListWindow
from arbol_binario_window import BinaryTreeWindow
from arbol_busqueda_window import BinarySearchTreeWindow


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Principal")
        self.setGeometry(550, 210, 450, 460)

        icono = QIcon("Logo.png")
        self.setWindowIcon(icono)

        main_layout = QVBoxLayout()
        logo_layout = QHBoxLayout()

        logo_label = QLabel()
        pixmap = QPixmap("logo.png").scaled(130, 130)
        logo_label.setPixmap(pixmap)
        logo_layout.addWidget(logo_label)

        title_label = QLabel("Menu Principal")
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        aux_label = QLabel()
        logo_layout.addWidget(aux_label)
        logo_layout.addWidget(title_label)
        logo_layout.addWidget(aux_label)
        logo_layout.addWidget(aux_label)

        buttons_layout = QVBoxLayout()

        self.pila_button = QPushButton("Pila")
        self.pila_button.setStyleSheet(
            "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 13px;")
        self.pila_button.setFont(QFont("Arial", 11))
        self.pila_button.clicked.connect(self.pila_button_clicked)
        buttons_layout.addWidget(self.pila_button)

        self.cola_button = QPushButton("Cola")
        self.cola_button.setStyleSheet(
            "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 13px;")
        self.cola_button.setFont(QFont("Arial", 11))
        self.cola_button.clicked.connect(self.cola_button_clicked)
        buttons_layout.addWidget(self.cola_button)

        self.lista_simple_button = QPushButton("Lista Simplemente Ligada")
        self.lista_simple_button.setStyleSheet(
            "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 13px;")
        self.lista_simple_button.setFont(QFont("Arial", 11))
        self.lista_simple_button.clicked.connect(self.lista_simplemente_button_clicked)
        buttons_layout.addWidget(self.lista_simple_button)

        self.lista_circular_button = QPushButton("Lista Circular")
        self.lista_circular_button.setStyleSheet(
            "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 13px;")
        self.lista_circular_button.setFont(QFont("Arial", 11))
        self.lista_circular_button.clicked.connect(self.lista_circular_button_clicked)
        buttons_layout.addWidget(self.lista_circular_button)

        self.lista_doble_button = QPushButton("Lista Doblemente Ligada")
        self.lista_doble_button.setStyleSheet(
            "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 13px;")
        self.lista_doble_button.setFont(QFont("Arial", 11))
        self.lista_doble_button.clicked.connect(self.lista_doble_button_clicked)
        buttons_layout.addWidget(self.lista_doble_button)

        self.lista_circular_doble_button = QPushButton("Lista Circular Doble")
        self.lista_circular_doble_button.setStyleSheet(
            "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 13px;")
        self.lista_circular_doble_button.setFont(QFont("Arial", 11))
        self.lista_circular_doble_button.clicked.connect(self.lista_circular_doble_button_clicked)
        buttons_layout.addWidget(self.lista_circular_doble_button)

        self.arbol_binario_button = QPushButton("Árbol Binario")
        self.arbol_binario_button.setStyleSheet(
            "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 13px;")
        self.arbol_binario_button.setFont(QFont("Arial", 11))
        self.arbol_binario_button.clicked.connect(self.arbol_binario_button_clicked)
        buttons_layout.addWidget(self.arbol_binario_button)

        self.arbol_busqueda_button = QPushButton("Árbol de Búsqueda")
        self.arbol_busqueda_button.setStyleSheet(
            "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 13px;")
        self.arbol_busqueda_button.setFont(QFont("Arial", 11))
        self.arbol_busqueda_button.clicked.connect(self.arbol_busqueda_button_clicked)
        buttons_layout.addWidget(self.arbol_busqueda_button)

        main_layout.addLayout(logo_layout)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

    def reopen_main_menu(self):
        self.show()

    def pila_button_clicked(self):
        self.hide()  # Ocultar la ventana principal
        self.pila_window = StackWindow()
        self.pila_window.show()
        self.pila_window.window_closed.connect(self.reopen_main_menu)

    def cola_button_clicked(self):
        self.hide()  # Ocultar la ventana principal
        self.cola_window = QueueWindow()
        self.cola_window.show()
        self.cola_window.window_closed.connect(self.reopen_main_menu)

    def lista_simplemente_button_clicked(self):
        self.hide()  # Ocultar la ventana principal
        self.lista_simple = ListWindow()
        self.lista_simple.show()
        self.lista_simple.window_closed.connect(self.reopen_main_menu)

    def lista_circular_button_clicked(self):
        self.hide()  # Ocultar la ventana principal
        self.lista_circular = CircularListWindow()
        self.lista_circular.show()
        self.lista_circular.window_closed.connect(self.reopen_main_menu)

    def lista_doble_button_clicked(self):
        self.hide()  # Ocultar la ventana principal
        self.lista_doble = ListDoubleWindow()
        self.lista_doble.show()
        self.lista_doble.window_closed.connect(self.reopen_main_menu)

    def lista_circular_doble_button_clicked(self):
        self.hide()  # Ocultar la ventana principal
        self.lista_circular_doble = CircularDoublyLinkedListWindow()
        self.lista_circular_doble.show()
        self.lista_circular_doble.window_closed.connect(self.reopen_main_menu)

    def arbol_binario_button_clicked(self):
        self.hide()  # Ocultar la ventana principal
        self.arbol_binario = BinaryTreeWindow()
        self.arbol_binario.show()
        self.arbol_binario.window_closed.connect(self.reopen_main_menu)

    def arbol_busqueda_button_clicked(self):
        self.hide()  # Ocultar la ventana principal
        self.arbol_busqueda = BinarySearchTreeWindow()
        self.arbol_busqueda.show()
        self.arbol_busqueda.window_closed.connect(self.reopen_main_menu)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
