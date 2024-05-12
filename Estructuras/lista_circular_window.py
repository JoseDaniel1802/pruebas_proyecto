from PyQt6.QtCore import pyqtSignal, Qt, QPointF, QRectF
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QGraphicsEllipseItem, QGraphicsSimpleTextItem, QGraphicsView, QGraphicsScene, QScrollArea, QMessageBox, QFileDialog
from PyQt6.QtGui import QPixmap, QFont, QIcon, QColor, QPen
import sys
import math
from edit_lista_circular_data import InsertFinalSinglyWindow, InsertInicioSinglyWindow, SearchSinglyWindow, data


class CircularListWindow(QWidget):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista Circular")
        self.setGeometry(450, 40, 700, 750)
        icono = QIcon("Logo.png")
        self.setWindowIcon(icono)

        main_layout = QVBoxLayout()

        # Logo y Título Layout
        logo_title_layout = QHBoxLayout()

        # Logo
        logo_label = QLabel()
        pixmap = QPixmap("logo.png").scaled(130, 130)  # Escalar la imagen a 130x130
        logo_label.setPixmap(pixmap)
        logo_title_layout.addWidget(logo_label)

        # Título
        title_label = QLabel("Lista Circular")
        x = QLabel("")
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        logo_title_layout.addWidget(x)
        logo_title_layout.addWidget(x)
        logo_title_layout.addWidget(x)
        logo_title_layout.addWidget(title_label)
        logo_title_layout.addWidget(x)
        logo_title_layout.addWidget(x)
        logo_title_layout.addWidget(x)
        logo_title_layout.addWidget(x)

        main_layout.addLayout(logo_title_layout)

        # Crear el área de desplazamiento
        scroll_area = QScrollArea()
        scroll_area.setStyleSheet("background-color: white; border: 4px solid white; border-radius: 11px;")

        scroll_area.setWidgetResizable(True)  # Permitir que el widget contenido se redimensione
        main_layout.addWidget(scroll_area)

        if len(data) > 0:
            # Crear la escena gráfica y configurarla
            self.scene = QGraphicsScene()
            self.grafics()
            self.view = QGraphicsView(self.scene)
            scroll_area.setWidget(self.view)

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

    def closeEvent(self, event):
        self.window_closed.emit()
        super().closeEvent(event)

    def update_datos(self):
        x = None
        if data.tipo_data == int:
            x = "int"
        elif data.tipo_data == float:
            x = "float"
        elif data.tipo_data == str:
            x = "str"
        self.data_label.setText(f"Head: {data.head}")
        self.tail_label.setText(f"Tail: {data.tail}")
        self.size_label.setText(f"Tamaño: {len(data)}")
        self.type_label.setText(f"Tipo de dato: {x}")

    def button_main(self, layout: QVBoxLayout):
        if data.count == 0:
            data.count += 1
            for i in range(0, 3):
                data.shift()

        self.update_datos()

        buttons_layout = QVBoxLayout()

        button_style = "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 13px;"

        # Botones de inserción en una sola línea
        insert_layout = QHBoxLayout()

        insert_inicio_button = QPushButton("Insertar (Inicio)")
        insert_inicio_button.setStyleSheet(button_style)
        insert_inicio_button.setFont(QFont("Arial", 11))
        insert_inicio_button.clicked.connect(self.show_insert_inicio_dialog)
        insert_layout.addWidget(insert_inicio_button)

        insert_final_button = QPushButton("Insertar (Final)")
        insert_final_button.setStyleSheet(button_style)
        insert_final_button.setFont(QFont("Arial", 11))
        insert_final_button.clicked.connect(self.show_insert_final_dialog)
        insert_layout.addWidget(insert_final_button)

        buttons_layout.addLayout(insert_layout)

        # Botones de eliminación en una sola línea
        delete_layout = QHBoxLayout()

        eliminar_inicio_button = QPushButton("Eliminar (Inicio)")
        eliminar_inicio_button.setStyleSheet(button_style)
        eliminar_inicio_button.setFont(QFont("Arial", 11))
        eliminar_inicio_button.clicked.connect(self.show_delete_first)
        delete_layout.addWidget(eliminar_inicio_button)

        eliminar_final_button = QPushButton("Eliminar (Final)")
        eliminar_final_button.setStyleSheet(button_style)
        eliminar_final_button.setFont(QFont("Arial", 11))
        eliminar_final_button.clicked.connect(self.show_delete_last)
        delete_layout.addWidget(eliminar_final_button)

        buttons_layout.addLayout(delete_layout)

        # Otros botones
        otros_layout = QVBoxLayout()

        buscar_valor_button = QPushButton("Buscar valor")
        buscar_valor_button.setStyleSheet(button_style)
        buscar_valor_button.setFont(QFont("Arial", 11))
        buscar_valor_button.clicked.connect(self.show_search_dialog)
        otros_layout.addWidget(buscar_valor_button)

        rotate_left_button = QPushButton("Rotar a la izquierda")
        rotate_left_button.setStyleSheet(button_style)
        rotate_left_button.setFont(QFont("Arial", 11))
        rotate_left_button.clicked.connect(self.show_move_left)
        otros_layout.addWidget(rotate_left_button)

        rotate_right_button = QPushButton("Rotar a la derecha")
        rotate_right_button.setStyleSheet(button_style)
        rotate_right_button.setFont(QFont("Arial", 11))
        rotate_right_button.clicked.connect(self.show_move_right)
        otros_layout.addWidget(rotate_right_button)

        buttons_layout.addLayout(otros_layout)

        save_layout = QHBoxLayout()

        # Guardar archivo
        save_button = QPushButton("Guardar (txt)")
        save_button.setStyleSheet(button_style)
        save_button.setFont(QFont("Arial", 11))
        save_button.clicked.connect(self.save_stack)
        save_layout.addWidget(save_button)

        # Guardar archivo
        save_upload = QPushButton("Cargar (txt)")
        save_upload.setStyleSheet(button_style)
        save_upload.setFont(QFont("Arial", 11))
        save_upload.clicked.connect(self.load_stack)
        save_layout.addWidget(save_upload)

        buttons_layout.addLayout(save_layout)

        layout.addLayout(buttons_layout)

    def show_insert_inicio_dialog(self):
        self.insert_inicio_dialog = InsertInicioSinglyWindow()
        self.insert_inicio_dialog.show()
        self.insert_inicio_dialog.window_closed.connect(self.update_grafic)

    def show_insert_final_dialog(self):
        self.insert_final_dialog = InsertFinalSinglyWindow()
        self.insert_final_dialog.show()
        self.insert_final_dialog.window_closed.connect(self.update_grafic)

    def show_search_dialog(self):
        self.search_dialog = SearchSinglyWindow()
        self.search_dialog.show()

    def show_delete_first(self):
        if len(data) == 0:
            QMessageBox.warning(self, "Error", 'La Cola no tiene ningún dato',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        else:
            data.shift()
            self.update_grafic()

    def show_delete_last(self):
        if len(data) == 0:
            QMessageBox.warning(self, "Error", 'La Cola no tiene ningún dato',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        else:
            data.pop()
            self.update_grafic()

    def show_move_right(self):
        pass

    def show_move_left(self):
        pass

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

    def grafics(self):

        if len(data) > 0:
            nodos = []
            current = data.head

            while True:
                x = f"{current}\n" + f"{current.memory_address()}"
                nodos.append(x)
                current = current.next
                if current == data.head:
                    break

            radio = 250
            centro = QPointF(400, 300)
            angulo = 0
            incremento_angulo = 360 / len(nodos)
            pen = QPen(QColor("Black"))
            for nodo in nodos:
                x = centro.x() + radio * math.cos(math.radians(angulo))
                y = centro.y() + radio * math.sin(math.radians(angulo))
                rect = QGraphicsEllipseItem(QRectF(x - 57, y - 48, 107, 107))
                self.scene.addItem(rect)
                text = QGraphicsSimpleTextItem(nodo)
                text.setPos(x - text.boundingRect().width() / 2, y - text.boundingRect().height() / 2)
                self.scene.addItem(text)
                angulo += incremento_angulo

                siguiente_x = centro.x() + radio * math.cos(math.radians(angulo))
                siguiente_y = centro.y() + radio * math.sin(math.radians(angulo))
                line = self.scene.addLine(x, y, siguiente_x, siguiente_y, pen)


    def update_grafic(self):
        self.update_datos()
        if len(data) > 0:
            # Eliminar todos los elementos gráficos de la escena
            for item in self.scene.items():
                self.scene.removeItem(item)

            nodos = []
            current = data.head

            while True:
                x = f"         {current}\n" + f"{current.memory_address()}"
                nodos.append(x)
                current = current.next
                if current == data.head:
                    break

            radio = 250
            centro = QPointF(400, 320)
            angulo = 0
            incremento_angulo = 360 / len(nodos)
            pen = QPen(QColor("Black"))
            for nodo in nodos:
                x = centro.x() + radio * math.cos(math.radians(angulo))
                y = centro.y() + radio * math.sin(math.radians(angulo))
                rect = QGraphicsEllipseItem(QRectF(x - 43, y - 35, 87, 87))
                self.scene.addItem(rect)
                text = QGraphicsSimpleTextItem(nodo)
                text.setPos(x - text.boundingRect().width() / 2, y - text.boundingRect().height() / 2)
                self.scene.addItem(text)
                angulo += incremento_angulo

                siguiente_x = centro.x() + radio * math.cos(math.radians(angulo))
                siguiente_y = centro.y() + radio * math.sin(math.radians(angulo))
                line = self.scene.addLine(x, y, siguiente_x, siguiente_y, pen)


        else:
            self.scene.clear()

    def save_stack(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt)")
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    count = 1
                    for item in data:
                        file.write(str(item) + '\n')
                        if count == len(data):
                            break
                        count += 1
                QMessageBox.information(self, "Archvo Cargado", f"Cargado correctamente desde: {file_path}",
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)
            except Exception as e:
                print("Error al guardar la Cola:", str(e))

    def load_stack(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Cargar archivo", "", "Archivos de texto (*.txt)")
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    for line in file:
                        data.append(line.strip())
                QMessageBox.information(self, "Archvo Cargado", f"Cargado correctamente desde: {file_path}",
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)
                self.update_grafic()
            except Exception as e:
                QMessageBox.warning(self, "Error al cargar datos desde el archivo:", str(e))
        self.update_grafic()


data.append("Prueba 1")
data.append("Prueba 2")
data.append("Prueba 3")

if __name__ == "__main__":
    data.append(1)
    data.append(2)
    data.append(3)
    data.append(4)
    data.append(5)

    app = QApplication(sys.argv)
    window = CircularListWindow()
    window.show()
    sys.exit(app.exec())
