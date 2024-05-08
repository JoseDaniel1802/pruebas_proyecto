from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QGraphicsScene, \
    QGraphicsView, QWidget, QGraphicsEllipseItem, QGraphicsTextItem
from PyQt6.QtGui import QIcon, QFont
from circulares.circular_list import CircularList

list = CircularList()


class InsertInicioCircularWindow(QDialog):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insertar (Inicio) en Lista Circular")
        self.setGeometry(650, 320, 250, 100)
        icon = QIcon("Logo.png")
        self.setWindowIcon(icon)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.message_label = QLabel("Insertar elemento (Inicio):")
        self.message_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout.addWidget(self.message_label)

        self.input_field = QLineEdit()
        self.apply_line_edit_style(self.input_field)
        layout.addWidget(self.input_field)

        self.confirm_button = QPushButton("Insertar")
        self.confirm_button.clicked.connect(self.insert_element)
        self.apply_button_style(self.confirm_button)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def apply_button_style(self, button):
        button_style = "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 10px;"
        button.setStyleSheet(button_style)
        button.setFont(QFont("Arial", 11))

    def apply_line_edit_style(self, line_edit):
        style = "height: 23px; border-radius: 10px; border: 2px solid white;"
        line_edit.setStyleSheet(style)

    def insert_element(self):
        elemt = self.input_field.text()

        if elemt == "":
            QMessageBox.warning(self, "Error", 'Por favor ingrese datos validos',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

        else:
            x = list.prepend(elemt)
            print(list.display())
            list.search_by_value(elemt)
            QMessageBox.information(self, "Elemento insertado", "se ha insertado con exito",
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
            self.close()


class InsertFinalCircularWindow(QDialog):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insertar (Final) en Lista Circular")
        self.setGeometry(650, 320, 250, 100)
        icon = QIcon("Logo.png")
        self.setWindowIcon(icon)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.message_label = QLabel("Insertar elemento (Final):")
        self.message_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout.addWidget(self.message_label)

        self.input_field = QLineEdit()
        self.apply_line_edit_style(self.input_field)
        layout.addWidget(self.input_field)

        self.confirm_button = QPushButton("Insertar")
        self.confirm_button.clicked.connect(self.insert_element)
        self.apply_button_style(self.confirm_button)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def apply_button_style(self, button):
        button_style = "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 10px;"
        button.setStyleSheet(button_style)
        button.setFont(QFont("Arial", 11))

    def apply_line_edit_style(self, line_edit):
        style = "height: 23px; border-radius: 10px; border: 2px solid white;"
        line_edit.setStyleSheet(style)

    def insert_element(self):
        elemt = self.input_field.text()

        if elemt == "":
            QMessageBox.warning(self, "Error", 'Por favor ingrese datos validos',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

        else:
            x = list.append(elemt)
            print(list.display())
            list.search_by_value(elemt)
            QMessageBox.information(self, "Elemento insertado", "se ha insertado con exito",
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
            self.close()


class SearchCircularWindow(QDialog):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buscar Elemento en Lista Circular")
        self.setGeometry(650, 320, 250, 100)
        icon = QIcon("Logo.png")
        self.setWindowIcon(icon)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.message_label = QLabel("Buscar elemento:")
        self.message_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout.addWidget(self.message_label)

        self.input_field = QLineEdit()
        self.apply_line_edit_style(self.input_field)
        layout.addWidget(self.input_field)

        self.confirm_button = QPushButton("Buscar")
        self.confirm_button.clicked.connect(self.find_element)
        self.apply_button_style(self.confirm_button)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def apply_button_style(self, button):
        button_style = "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 10px;"
        button.setStyleSheet(button_style)
        button.setFont(QFont("Arial", 11))

    def apply_line_edit_style(self, line_edit):
        style = "height: 23px; border-radius: 10px; border: 2px solid white;"
        line_edit.setStyleSheet(style)

    def find_element(self):
        elemt = self.input_field.text()

        if elemt == "":
            QMessageBox.warning(self, "Error", 'Por favor ingrese datos validos',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

        if elemt == None:
            QMessageBox.warning(self, "Error", 'El elemento no se encuentra en la pila',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

        else:
            x = list.search_by_value(elemt)
            QMessageBox.information(self, "Elemento encontrado", f"Indice es: {x + 1}",
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
            self.close()


class DeleteCircularWindowB(QDialog):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eleminar Elemento en Lista Circular")
        self.setGeometry(650, 320, 250, 100)
        icon = QIcon("Logo.png")
        self.setWindowIcon(icon)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.message_label = QLabel("Eliminar Elemento:")
        self.message_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout.addWidget(self.message_label)

        self.confirm_button = QPushButton("Eliminar")
        self.confirm_button.clicked.connect(self.shifft)  # Corregido aquí
        self.apply_button_style(self.confirm_button)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def apply_button_style(self, button):
        button_style = "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 10px;"
        button.setStyleSheet(button_style)
        button.setFont(QFont("Arial", 11))

    def apply_line_edit_style(self, line_edit):
        style = "height: 23px; border-radius: 10px; border: 2px solid white;"
        line_edit.setStyleSheet(style)

    def shifft(self):
        if list.is_empty():
            QMessageBox.warning(self, "Error", 'Lista circular vacía, ingresa datos',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

        else:
            x = list.shift()
            print(list.display())
            QMessageBox.information(self, "Elemento Borrado", f"El elemento es: {x}",
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
            self.close()

class DeleteCircularWindowL(QDialog):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eliminar Último Elemento en Lista Circular")
        self.setGeometry(650, 320, 250, 100)
        icon = QIcon("Logo.png")
        self.setWindowIcon(icon)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.message_label = QLabel("Eliminar Elemento:")
        self.message_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout.addWidget(self.message_label)

        self.confirm_button = QPushButton("Eliminar ultimo")
        self.confirm_button.clicked.connect(self.popp)
        self.apply_button_style(self.confirm_button)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def apply_button_style(self, button):
        button_style = "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 10px;"
        button.setStyleSheet(button_style)
        button.setFont(QFont("Arial", 11))

    def apply_line_edit_style(self, line_edit):
        style = "height: 23px; border-radius: 10px; border: 2px solid white;"
        line_edit.setStyleSheet(style)

    def popp(self):
        if list.is_empty():
            QMessageBox.warning(self, "Error", 'Lista circular vacía, ingresa datos',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

        else:
            x = list.pop()
            print(list.display())
            QMessageBox.information(self, "Elemento Borrado", f"El elemento es: {x}",
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
            self.close()

class MoveRight(QDialog):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insertar (Inicio) en Lista Circular")
        self.setGeometry(650, 320, 250, 100)
        icon = QIcon("Logo.png")
        self.setWindowIcon(icon)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.message_label = QLabel("Mover a la Derecha (¿Cuantós pasos?):")
        self.message_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout.addWidget(self.message_label)

        self.input_field = QLineEdit()
        self.apply_line_edit_style(self.input_field)
        layout.addWidget(self.input_field)

        self.confirm_button = QPushButton("Mover")
        self.confirm_button.clicked.connect(self.move_right_)
        self.apply_button_style(self.confirm_button)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def apply_button_style(self, button):
        button_style = "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 10px;"
        button.setStyleSheet(button_style)
        button.setFont(QFont("Arial", 11))

    def apply_line_edit_style(self, line_edit):
        style = "height: 23px; border-radius: 10px; border: 2px solid white;"
        line_edit.setStyleSheet(style)

    def move_right_(self):
        steps_str = self.input_field.text()

        if not steps_str.isdigit():
            QMessageBox.warning(self, "Error", "Por favor ingrese un número válido de pasos.",
                                QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
            return

        steps = int(steps_str)

        if steps <= 0:
            QMessageBox.warning(self, "Error", "Por favor ingrese un número de pasos positivo.",
                                QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
            return

        list.move_right(steps)
        print(list.display())
        QMessageBox.information(self, "Movimiento exitoso", f"Se movió hacia la derecha {steps} pasos",
                                QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
        self.close()

class MoveLeft(QDialog):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mover a la Izquierda en Lista Circular")
        self.setGeometry(650, 320, 250, 100)
        icon = QIcon("Logo.png")
        self.setWindowIcon(icon)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.message_label = QLabel("Mover a la Izquierda (¿Cuántos pasos?):")
        self.message_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout.addWidget(self.message_label)

        self.input_field = QLineEdit()
        self.apply_line_edit_style(self.input_field)
        layout.addWidget(self.input_field)

        self.confirm_button = QPushButton("Mover")
        self.confirm_button.clicked.connect(self.move_left)
        self.apply_button_style(self.confirm_button)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def apply_button_style(self, button):
        button_style = "height: 30px; background-color: #86a4ef; color: white; border: 2px solid black; border-radius: 10px;"
        button.setStyleSheet(button_style)
        button.setFont(QFont("Arial", 11))

    def apply_line_edit_style(self, line_edit):
        style = "height: 23px; border-radius: 10px; border: 2px solid white;"
        line_edit.setStyleSheet(style)

    def move_left(self):
        steps_str = self.input_field.text()

        if not steps_str.isdigit():
            QMessageBox.warning(self, "Error", "Por favor ingrese un número válido de pasos.",
                                QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
            return

        steps = int(steps_str)

        if steps <= 0:
            QMessageBox.warning(self, "Error", "Por favor ingrese un número de pasos positivo.",
                                QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
            return

        list.move_left(steps)
        print(list.display())
        QMessageBox.information(self, "Movimiento exitoso", f"Se movió hacia la izquierda {steps} pasos",
                                QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
        self.close()

