from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPixmap, QFont, QIcon
import sys

class CircularDoublyLinkedListWindow(QWidget):
    window_closed = pyqtSignal()
    def __init__(self):
        window_closed = pyqtSignal()
        super().__init__()
        self.setWindowTitle("Menu Lista Circular Doble")
        self.setGeometry(450, 240, 600, 300)
        icono = QIcon("Logo.png")
        self.setWindowIcon(icono)

        # Layouts
        main_layout = QVBoxLayout()
        logo_layout = QHBoxLayout()

        # Logo
        logo_label = QLabel()
        pixmap = QPixmap("logo.png").scaled(130, 130)  # Escalar la imagen a 130x130
        logo_label.setPixmap(pixmap)
        logo_layout.addWidget(logo_label)

        # Título
        title_label = QLabel("Menu Lista Circular Doble")
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        aux_label = QLabel()
        logo_layout.addWidget(aux_label)
        logo_layout.addWidget(title_label)
        logo_layout.addWidget(aux_label)
        logo_layout.addWidget(aux_label)

        # Botones
        buttons_layout = QVBoxLayout()

        # Estilo de los botones
        button_style = "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 13px;"

        # Botón insertar inicio
        insert_inicio_button = QPushButton("Insertar (Inicio)")
        insert_inicio_button.setStyleSheet(button_style)
        insert_inicio_button.setFont(QFont("Arial", 11))
        buttons_layout.addWidget(insert_inicio_button)

        # Botón insertar final
        insert_final_button = QPushButton("Insertar (Final)")
        insert_final_button.setStyleSheet(button_style)
        insert_final_button.setFont(QFont("Arial", 11))
        buttons_layout.addWidget(insert_final_button)

        # Botón eliminar inicio
        delete_inicio_button = QPushButton("Eliminar (Inicio)")
        delete_inicio_button.setStyleSheet(button_style)
        delete_inicio_button.setFont(QFont("Arial", 11))
        buttons_layout.addWidget(delete_inicio_button)

        # Botón eliminar final
        delete_final_button = QPushButton("Eliminar (Final)")
        delete_final_button.setStyleSheet(button_style)
        delete_final_button.setFont(QFont("Arial", 11))
        buttons_layout.addWidget(delete_final_button)

        # Botón buscar valor
        buscar_valor_button = QPushButton("Buscar valor")
        buscar_valor_button.setStyleSheet(button_style)
        buscar_valor_button.setFont(QFont("Arial", 11))
        buttons_layout.addWidget(buscar_valor_button)

        # Botón rotar a la izquierda
        rotate_left_button = QPushButton("Rotar a la izquierda")
        rotate_left_button.setStyleSheet(button_style)
        rotate_left_button.setFont(QFont("Arial", 11))
        buttons_layout.addWidget(rotate_left_button)

        # Botón rotar a la derecha
        rotate_right_button = QPushButton("Rotar a la derecha")
        rotate_right_button.setStyleSheet(button_style)
        rotate_right_button.setFont(QFont("Arial", 11))
        buttons_layout.addWidget(rotate_right_button)

        # Agregar layouts al layout principal
        main_layout.addLayout(logo_layout)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

    def closeEvent(self, event):
        # Emitir la señal de cierre cuando la ventana se cierra
        self.window_closed.emit()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircularDoublyLinkedListWindow()
    window.show()
    sys.exit(app.exec())
