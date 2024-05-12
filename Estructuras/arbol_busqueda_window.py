import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QPushButton, QVBoxLayout, QWidget, \
    QInputDialog, QMessageBox, QGraphicsEllipseItem, QHBoxLayout, QLabel
from PyQt6.QtGui import QColor, QBrush, QFont, QIcon, QPixmap  # Agregar QFont para ajustar el tamaño de la letra
from binary_search import NodoArbol, T, ArbolBusquedaBinaria


class BinarySearchTreeWindow(QMainWindow):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.tree = ArbolBusquedaBinaria()
        self.setWindowTitle("Menu Árbol Binario")
        self.setGeometry(400, 70, 690, 690)
        icono = QIcon("Logo.png")
        self.setWindowIcon(icono)

        self.initUI()

    def initUI(self):
        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(QColor("white"))
        self.view = QGraphicsView(self.scene)
        self.view.setSceneRect(0, 0, 800, 600)

        layout = QVBoxLayout()

        logo_layout = QHBoxLayout()

        # Logo
        logo_label = QLabel()
        pixmap = QPixmap("logo.png").scaled(130, 130)  # Escalar la imagen a 130x130
        logo_label.setPixmap(pixmap)
        logo_layout.addWidget(logo_label)

        # Título
        title_label = QLabel("Menu Árbol Binario")
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        aux_label = QLabel()
        logo_layout.addWidget(aux_label)
        logo_layout.addWidget(title_label)
        logo_layout.addWidget(aux_label)
        logo_layout.addWidget(aux_label)

        layout.addLayout(logo_layout)

        layout.addWidget(self.view)
        self.button_main(layout)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def button_main(self, layout: QVBoxLayout):
        button_style = "height: 30px; background-color: #86a4ef; color: white; border: 2x solid black; border-radius: 13px;"

        self.insertBtn = QPushButton("Insertar")
        self.insertBtn.setStyleSheet(button_style)
        self.insertBtn.clicked.connect(self.insertValue)
        layout.addWidget(self.insertBtn)

        self.deleteBtn = QPushButton("Eliminar")
        self.deleteBtn.setStyleSheet(button_style)
        self.deleteBtn.clicked.connect(self.deleteValue)
        layout.addWidget(self.deleteBtn)

        self.searchBtn = QPushButton("Buscar")
        self.searchBtn.setStyleSheet(button_style)
        self.searchBtn.clicked.connect(self.searchValue)
        layout.addWidget(self.searchBtn)

    def insertValue(self):
        value, ok = QInputDialog.getInt(self, "Insertar Valor", "Ingrese el valor a insertar:")
        if ok:
            self.tree.insertar(value)
            self.updateTree()

    def deleteValue(self):
        value, ok = QInputDialog.getInt(self, "Eliminar Valor", "Ingrese el valor a eliminar:")
        if ok:
            self.tree.eliminar(value)
            self.updateTree()

    def searchValue(self):
        value, ok = QInputDialog.getInt(self, "Buscar Valor", "Ingrese el valor a buscar:")
        if ok:
            node = self.tree.buscar(value)
            if node:
                QMessageBox.information(self, "Búsqueda", f"El valor {value} está en el árbol.")
            else:
                QMessageBox.information(self, "Búsqueda", f"El valor {value} no está en el árbol.")

    def updateTree(self):
        self.scene.clear()
        if self.tree.raiz is not None:
            self.drawTree(self.tree.raiz, 400, 50, 300)

    def drawTree(self, node, x, y, space):
        if node is not None:
            circle_radius = 40
            value_text = str(node.valor)
            address_text = hex(id(node))

            ellipse = QGraphicsEllipseItem(x - circle_radius, y - circle_radius, circle_radius * 2, circle_radius * 2)
            self.scene.addItem(ellipse)

            value_item = self.scene.addText(value_text)
            value_item.setPos(x - value_item.boundingRect().width() / 2,
                              y - value_item.boundingRect().height() / 2 - 10)
            value_item.setFont(QFont("Arial", 8))  # Ajustar tamaño de letra a 8 puntos

            address_item = self.scene.addText(address_text)
            address_item.setPos(x - address_item.boundingRect().width() / 2,
                                y - address_item.boundingRect().height() / 2 + 10)
            address_item.setFont(QFont("Arial", 8))  # Ajustar tamaño de letra a 8 puntos

            if node.izquierda is not None:
                self.scene.addLine(x, y, x - space, y + 100)
                self.drawTree(node.izquierda, x - space, y + 100, space / 2)

            if node.derecha is not None:
                self.scene.addLine(x, y, x + space, y + 100)
                self.drawTree(node.derecha, x + space, y + 100, space / 2)

    def closeEvent(self, event):
        # Emitir la señal de cierre cuando la ventana se cierra
        self.window_closed.emit()
        super().closeEvent(event)
