from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea, \
    QMessageBox
from PyQt6.QtGui import QPixmap, QFont, QIcon
import sys
from edit_cola_data import data
from edit_cola_data import SearchQueueWindow, InsertQueueWindow


class QueueWindow(QWidget):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Pila")
        self.setGeometry(450, 190, 600, 490)
        icono = QIcon("Logo.png")
        self.setWindowIcon(icono)

        # Layouts
        main_layout = QVBoxLayout()

        # Logo y Título Layout
        logo_title_layout = QHBoxLayout()

        # Logo
        logo_label = QLabel()
        pixmap = QPixmap("logo.png").scaled(130, 130)  # Escalar la imagen a 130x130
        logo_label.setPixmap(pixmap)
        logo_title_layout.addWidget(logo_label)

        # Título
        title_label = QLabel("Cola")
        x = QLabel("")
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        logo_title_layout.addWidget(x)
        logo_title_layout.addWidget(title_label)
        logo_title_layout.addWidget(x)

        main_layout.addLayout(logo_title_layout)

        # Crear y agregar el área de desplazamiento con el dibujo
        scroll_area = self.create_scroll_area_with_drawing()

        main_layout.addWidget(scroll_area)

        data_layout = QHBoxLayout()

        style = "height: 10px; background-color: #4d82bc; color: white; border: 6px solid #4d82bc; border-radius: 13px;"

        self.data_label = QLabel(f"Head: {data.head}")
        self.data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_label.setStyleSheet(style)
        data_layout.addWidget(self.data_label)

        self.tail_label = QLabel(f"Tail: {data.tail}")
        self.tail_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tail_label.setStyleSheet(style)
        data_layout.addWidget(self.tail_label)

        self.size_label = QLabel(f"Tamaño: {len(data)}")
        self.size_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.size_label.setStyleSheet(style)
        data_layout.addWidget(self.size_label)

        self.type_label = QLabel(f"Tipo de dato: {data.tipo_data}")
        self.type_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.type_label.setStyleSheet(style)
        data_layout.addWidget(self.type_label)

        main_layout.addLayout(data_layout)


        if data.tipo_data is None:
            self.create_selection_button(main_layout)
        else:
            self.button_main(main_layout)

        self.setLayout(main_layout)

    def update_datos(self):
        self.data_label.setText(f"Head: {data.head}")
        self.tail_label.setText(f"Tail: {data.tail}")
        self.size_label.setText(f"Tamaño: {len(data)}")
        self.type_label.setText(f"Tipo de dato: {data.tipo_data}")

    def create_scroll_area_with_drawing(self):
        # Crear un widget para contener el layout horizontal
        scroll_content = QWidget()
        scroll_layout = QHBoxLayout(scroll_content)  # Definir el layout en el widget, no en la ventana principal

        arrow_labels = []
        min_size = 200  # Tamaño mínimo para los cuadros
        max_size = 100
        current = data.head

        while current is not None:
            label = QLabel("Dato: {}\n Memoria: {}".format(current.data, current.memory_address()))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrar texto
            label.setStyleSheet(
                "height: 30px; background-color: #86a4ef; color: white; border: 2px solid #86a4ef; border-radius: 13px;")
            label.setFixedSize(min_size, max_size)  # Establecer tamaño fijo
            scroll_layout.addWidget(label)
            if current.next is not None:
                # Logo
                arrow_label = QLabel()
                pixmap = QPixmap("flecha-izquierda.png").scaled(20, 20)  # Escalar la imagen a 130x130
                arrow_label.setPixmap(pixmap)
                arrow_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrar flecha
                scroll_layout.addWidget(arrow_label)
                arrow_labels.append(arrow_label)
            current = current.next

        # Crear el área desplazable y establecer el contenido como el widget creado
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOn)  # Mostrar siempre la barra de desplazamiento horizontal
        self.scroll_area.setWidget(scroll_content)

        self.scroll_area.setStyleSheet("background-color: white; border: 4px solid white; border-radius: 11px;")

        # Personalizar estilo de las flechas del QScrollBar
        scroll_bar = self.scroll_area.horizontalScrollBar()
        scroll_bar.setStyleSheet(
            """
            QScrollBar:horizontal {
                background-color: #86a4ef; /* Cambiar el color de fondo de la barra */
            }

            QScrollBar::right-arrow:horizontal {
                image: url(derecha.png); /* Cambiar la imagen de la flecha derecha */
            }

            QScrollBar::left-arrow:horizontal {
                image: url(izquierda.png); /* Cambiar la imagen de la flecha izquierda */
            }
            """
        )

        self.arrow_labels = arrow_labels

        return self.scroll_area

    def closeEvent(self, event):
        # Emitir la señal de cierre cuando la ventana se cierra
        self.window_closed.emit()
        super().closeEvent(event)

    def insert_button_clicked(self):
        self.insert_window = InsertQueueWindow()
        self.insert_window.show()
        self.insert_window.window_closed.connect(self.refresh_window)



    def delete_button_clicked(self):
        if len(data) == 0:
            QMessageBox.warning(self, "Error", 'La Cola no tiene ningún dato',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        else:
            data.pop()
            self.refresh_window()

    def find_button_clicked(self):
        self.find_window = SearchQueueWindow()
        self.find_window.show()
        self.update()

    def refresh_window(self):
        self.update_datos()
        # Obtener el widget contenido del QScrollArea actual
        scroll_content = self.scroll_area.widget()

        # Obtener el layout horizontal dentro del scroll_content
        scroll_layout = scroll_content.layout()

        # Eliminar todos los widgets hijos del layout actual
        while scroll_layout.count():
            item = scroll_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        arrow_labels = []
        min_size = 200
        max_size = 100
        current = data.head

        while current is not None:
            label = QLabel("Dato: {}\n Memoria: {}".format(current.data, current.memory_address()))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrar texto
            label.setStyleSheet(
                "height: 30px; background-color: #86a4ef; color: white; border: 2px solid #86a4ef; border-radius: 13px;")
            label.setFixedSize(min_size, max_size)  # Establecer tamaño fijo
            scroll_layout.addWidget(label)
            if current.next is not None:
                # Logo
                arrow_label = QLabel()
                pixmap = QPixmap("flecha-izquierda.png").scaled(20, 20)  # Escalar la imagen a 20x20
                arrow_label.setPixmap(pixmap)
                arrow_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrar flecha
                scroll_layout.addWidget(arrow_label)
                arrow_labels.append(arrow_label)
            current = current.next

        # Asegurar que el área de desplazamiento se redibuje correctamente
        self.scroll_area.updateGeometry()
        self.scroll_area.verticalScrollBar().setValue(0)
        self.scroll_area.horizontalScrollBar().setValue(0)



    def create_selection_button(self, layout: QVBoxLayout):

        button_style = "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 13px;"

        self.extra_buttons_layout = QHBoxLayout()

        # Botón 1
        self.button1 = QPushButton("Int")
        self.button1.setFont(QFont("Arial", 11))
        self.button1.clicked.connect(lambda: self.button1_clicked(layout))
        self.button1.setStyleSheet(button_style)
        self.extra_buttons_layout.addWidget(self.button1)

        # Botón 2
        self.button2 = QPushButton("Float")
        self.button2.setFont(QFont("Arial", 11))
        self.button2.clicked.connect(lambda: self.button2_clicked(layout))
        self.button2.setStyleSheet(button_style)
        self.extra_buttons_layout.addWidget(self.button2)

        # Botón 3
        self.button3 = QPushButton("Str")
        self.button3.setFont(QFont("Arial", 11))
        self.button3.clicked.connect(lambda: self.button3_clicked(layout))
        self.button3.setStyleSheet(button_style)
        self.extra_buttons_layout.addWidget(self.button3)

        # Agregar layout de botones adicionales al layout principal
        layout.addLayout(self.extra_buttons_layout)

    def button1_clicked(self, layout: QVBoxLayout):
        data.tipo_data = int

        self.button1.deleteLater()
        self.button2.deleteLater()
        self.button3.deleteLater()
        self.button_main(layout)

    def button2_clicked(self, layout: QVBoxLayout):
        data.tipo_data = float

        self.button1.deleteLater()
        self.button2.deleteLater()
        self.button3.deleteLater()
        self.button_main(layout)

    def button3_clicked(self, layout: QVBoxLayout):
        data.tipo_data = str

        self.button1.deleteLater()
        self.button2.deleteLater()
        self.button3.deleteLater()
        self.button_main(layout)



    def button_main(self, main_layout: QVBoxLayout):

        # Botones
        buttons_layout = QVBoxLayout()

        # Estilo de los botones
        button_style = "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 13px;"

        # Botón insertar
        insert_button = QPushButton("Insertar")
        insert_button.setStyleSheet(button_style)
        insert_button.setFont(QFont("Arial", 11))
        insert_button.clicked.connect(self.insert_button_clicked)
        buttons_layout.addWidget(insert_button)

        # Botón eliminar
        delete_button = QPushButton("Eliminar")
        delete_button.setStyleSheet(button_style)
        delete_button.setFont(QFont("Arial", 11))
        delete_button.clicked.connect(self.delete_button_clicked)
        buttons_layout.addWidget(delete_button)

        # Botón buscar valor
        buscar_valor_button = QPushButton("Buscar valor")
        buscar_valor_button.setStyleSheet(button_style)
        buscar_valor_button.setFont(QFont("Arial", 11))
        buscar_valor_button.clicked.connect(self.find_button_clicked)
        buttons_layout.addWidget(buscar_valor_button)

        main_layout.addLayout(buttons_layout)




if __name__ == "__main__":
    data.append(1)
    data.append(2)
    data.append(3)
    data.append(4)
    app = QApplication(sys.argv)
    window = QueueWindow()
    window.show()
    sys.exit(app.exec())
