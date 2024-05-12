from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QIcon, QFont
from data_identificator import data_identificator_type
from tda.listadoble import DoublyLinkedList

data = DoublyLinkedList()


class InsertInicioSinglyWindow(QDialog):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insertar (Inicio)")
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
        elemt = (self.input_field.text()).strip()
        type = data_identificator_type(elemt)
        y = data.tipo_data
        found = data.get_index(elemt)

        if elemt == "":
            QMessageBox.warning(self, "Error", 'Por favor ingrese datos validos',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        elif type == str:
            data.prepend(elemt)
            QMessageBox.information(self, "Elemento insertado", f"se ha insertado con exito: {elemt}",
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
            self.close()

        elif type != y:
            QMessageBox.warning(self, "Error", 'Por favor ingrese el tipo de dato elegido',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

        elif found != -1:
            QMessageBox.warning(self, "Error", 'El valor ya se encuentra en la lista',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)


        else:
            x = data.prepend(elemt)
            for i in data:
                print(i)
            QMessageBox.information(self, "Elemento insertado", f"se ha insertado con exito: {x}",
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
            self.close()

    def closeEvent(self, event):
        # Emitir la señal de cierre cuando la ventana se cierra
        self.window_closed.emit()
        super().closeEvent(event)


class InsertFinalSinglyWindow(QDialog):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insertar (Final)")
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
        elemt = (self.input_field.text()).strip()

        type = data_identificator_type(elemt)
        y = data.tipo_data
        found = data.get_index(elemt)

        if elemt == "":
            QMessageBox.warning(self, "Error", 'Por favor ingrese datos validos',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

        elif type == str:
            data.append(elemt)
            QMessageBox.information(self, "Elemento insertado", f"se ha insertado con exito: {elemt}",
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
            self.close()

        elif type != y:
            QMessageBox.warning(self, "Error", 'Por favor ingrese el tipo de dato elegido',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

        elif found != -1:
            QMessageBox.warning(self, "Error", 'El valor ya se encuentra en la lista',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

        else:
            x = data.append(elemt)
            for i in data:
                print(i)
            QMessageBox.information(self, "Elemento insertado", f"se ha insertado con exito: {x}",
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
            self.close()

    def closeEvent(self, event):
        # Emitir la señal de cierre cuando la ventana se cierra
        self.window_closed.emit()
        super().closeEvent(event)


class InsertIndexSinglyWindow(QDialog):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insertar (Inicio)")
        self.setGeometry(650, 320, 250, 100)
        icon = QIcon("Logo.png")
        self.setWindowIcon(icon)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.message_label = QLabel("Insertar elemento:")
        self.message_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout.addWidget(self.message_label)

        self.input_field = QLineEdit()
        self.apply_line_edit_style(self.input_field)
        layout.addWidget(self.input_field)

        self.message_label_index = QLabel("Posición:")
        self.message_label_index.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout.addWidget(self.message_label_index)

        self.input_field_index = QLineEdit()
        self.apply_line_edit_style(self.input_field)
        layout.addWidget(self.input_field_index)

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
        elemt = (self.input_field.text()).strip()
        y = data.tipo_data
        index = int((self.input_field_index.text()).strip())
        type = data_identificator_type(elemt)

        found = data.get_index(elemt)

        if elemt == "":
            QMessageBox.warning(self, "Error", 'Por favor ingrese datos validos',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        elif index < 0 or index > len(data):
            QMessageBox.warning(self, "Error", 'El indice no es valido',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

        elif type == str:
            x = data.insert_at_index(index, elemt)
            QMessageBox.information(self, "Elemento insertado", f"se ha insertado con exito: {elemt}",
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
            self.close()

        elif type != y:
            QMessageBox.warning(self, "Error", 'Por favor ingrese el tipo de dato elegido',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)



        elif found != -1:
            QMessageBox.warning(self, "Error", 'El valor ya se encuentra en la lista',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)


        else:
            x = data.insert_at_index(index, elemt)
            for i in data:
                print(i)
            QMessageBox.information(self, "Elemento insertado", f"se ha insertado con exito: {x}",
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
            self.close()

    def closeEvent(self, event):
        # Emitir la señal de cierre cuando la ventana se cierra
        self.window_closed.emit()
        super().closeEvent(event)


class DeletebyIndex(QDialog):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Posición (Eliminar)")
        self.setGeometry(650, 320, 250, 100)
        icon = QIcon("Logo.png")
        self.setWindowIcon(icon)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.message_label_index = QLabel("Posición:")
        self.message_label_index.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout.addWidget(self.message_label_index)

        self.input_field_index = QLineEdit()
        self.apply_line_edit_style(self.input_field_index)
        layout.addWidget(self.input_field_index)

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
        style = "height: 23px; border-radius: 10px; border: 2px  white;"
        line_edit.setStyleSheet(style)

    def insert_element(self):

        index = int((self.input_field_index.text()).strip())

        if index == "":
            QMessageBox.warning(self, "Error", 'Por favor ingrese datos validos',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)


        elif index < 0 or index > len(data):
            QMessageBox.warning(self, "Error", 'El indice no es valido',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)


        else:
            x = data.delete_by_index(index)
            for i in data:
                print(i)
            QMessageBox.information(self, "Elemento Eliminado", f"se ha Eliminado con exito: {x}",
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
            self.close()

    def closeEvent(self, event):
        # Emitir la señal de cierre cuando la ventana se cierra
        self.window_closed.emit()
        super().closeEvent(event)


class SearchSinglyWindow(QDialog):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buscar Elemento")
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
        self.confirm_button.clicked.connect(self.search_element)
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

    def search_element(self):
        elemt = self.input_field.text()

        index = data.get_index(elemt)

        if elemt == "":
            QMessageBox.warning(self, "Error", 'Por favor ingrese datos validos',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

        if index == -1:
            QMessageBox.warning(self, "Error", 'El elemento no se encuentra en la Lista Doble',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

        else:
            x = data.get_index(elemt)
            QMessageBox.information(self, "Elemento encontrado", f"Indice: {x}",
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
            self.close()

    def closeEvent(self, event):
        # Emitir la señal de cierre cuando la ventana se cierra
        self.window_closed.emit()
        super().closeEvent(event)
