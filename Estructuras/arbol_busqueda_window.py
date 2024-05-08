from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QPixmap, QFont, QIcon
import sys

class BinarySearchTreeWindow(QWidget):
    window_closed = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Árbol de Búsqueda")
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
        title_label = QLabel("Menu Árbol de Búsqueda")
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

        # Botón insertar
        insert_button = QPushButton("Insertar")
        insert_button.setStyleSheet(button_style)
        insert_button.setFont(QFont("Arial", 11))
        buttons_layout.addWidget(insert_button)

        # Botón eliminar
        delete_button = QPushButton("Eliminar")
        delete_button.setStyleSheet(button_style)
        delete_button.setFont(QFont("Arial", 11))
        buttons_layout.addWidget(delete_button)

        # Botón buscar valor
        buscar_valor_button = QPushButton("Buscar valor")
        buscar_valor_button.setStyleSheet(button_style)
        buscar_valor_button.setFont(QFont("Arial", 11))
        buttons_layout.addWidget(buscar_valor_button)

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
    window = BinarySearchTreeWindow()
    window.show()
    sys.exit(app.exec())
