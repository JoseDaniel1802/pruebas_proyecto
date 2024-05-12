import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QPushButton, QVBoxLayout, QWidget, \
    QInputDialog, QMessageBox, QGraphicsEllipseItem, QHBoxLayout, QLabel
from PyQt6.QtGui import QColor, QBrush, QIcon, QPixmap, QFont
from pyqtgraph import QtGui

from arbol_binario import BinaryTree, Node


class BinaryTreeWindow(QMainWindow):
    window_closed = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.tree = BinaryTree()
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

        self.insertRootBtn = QPushButton("Insertar Raíz")
        self.insertRootBtn.setStyleSheet(button_style)
        self.insertRootBtn.clicked.connect(self.insertRoot)
        layout.addWidget(self.insertRootBtn)

        self.insertLeftBtn = QPushButton("Insertar Izquierda")
        self.insertLeftBtn.setStyleSheet(button_style)
        self.insertLeftBtn.clicked.connect(self.insertLeft)
        layout.addWidget(self.insertLeftBtn)

        self.insertRightBtn = QPushButton("Insertar Derecha")
        self.insertRightBtn.setStyleSheet(button_style)
        self.insertRightBtn.clicked.connect(self.insertRight)
        layout.addWidget(self.insertRightBtn)

        self.deleteBtn = QPushButton("Eliminar")
        self.deleteBtn.setStyleSheet(button_style)
        self.deleteBtn.clicked.connect(self.deleteNode)
        layout.addWidget(self.deleteBtn)

        self.searchBtn = QPushButton("Buscar")
        self.searchBtn.setStyleSheet(button_style)
        self.searchBtn.clicked.connect(self.searchValue)
        layout.addWidget(self.searchBtn)


    def insertRoot(self):
        data, ok = QInputDialog.getInt(self, "Insertar Raíz", "Ingrese el valor de la raíz:")
        if ok:
            self.tree.root = Node(data)
            self.updateTree()

    def insertLeft(self):
        data, ok = QInputDialog.getInt(self, "Insertar a la Izquierda", "Ingrese el valor a insertar:")
        if ok:
            ref, ok = QInputDialog.getInt(self, "Nodo de Referencia", "Ingrese el valor del nodo de referencia:")
            if ok:
                try:
                    self.tree.insert_left(data, ref)
                    self.updateTree()
                except ValueError as e:
                    QMessageBox.warning(self, "Error", str(e))

    def insertRight(self):
        data, ok = QInputDialog.getInt(self, "Insertar a la Derecha", "Ingrese el valor a insertar:")
        if ok:
            ref, ok = QInputDialog.getInt(self, "Nodo de Referencia", "Ingrese el valor del nodo de referencia:")
            if ok:
                try:
                    self.tree.insert_right(data, ref)
                    self.updateTree()
                except ValueError as e:
                    QMessageBox.warning(self, "Error", str(e))

    def deleteNode(self):
        data, ok = QInputDialog.getInt(self, "Eliminar Nodo", "Ingrese el valor del nodo a eliminar:")
        if ok:
            try:
                deleted = self.tree.delete(data)
                if deleted:
                    self.updateTree()
                else:
                    QMessageBox.warning(self, "Error", "El nodo especificado no existe en el árbol.")
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))

    def searchValue(self):
        data, ok = QInputDialog.getInt(self, "Buscar Valor", "Ingrese el valor a buscar:")
        if ok:
            result = self.tree.search_by_value(data, self.tree.root)
            if result is not None:
                node_found, path = result
                self.highlightPath(path)
            else:
                QMessageBox.information(self, "Búsqueda", "El valor no fue encontrado en el árbol.")

    def updateTree(self):
        self.scene.clear()
        if self.tree.root is not None:
            self.drawTree(self.tree.root, 400, 50, 300)

    def drawTree(self, node, x, y, space):
        if node is not None:
            # Calcular el tamaño del círculo basado en la longitud del texto
            circle_radius = max(25, len(str(node.data)) * 7 + len(hex(id(node))) * 2)

            node_text = f"{node.data}\n{hex(id(node))}"  # Valor y dirección de memoria

            # Ajustar el tamaño de la letra al tamaño del círculo
            font_size = int(circle_radius / 5)  # Puedes ajustar el factor 4 según tus preferencias

            # Crear el elemento de texto con el tamaño de letra ajustado
            text_item = self.scene.addText(node_text)
            text_item.setDefaultTextColor(QColor("black"))
            text_item.setFont(QtGui.QFont("Arial", font_size))  # Ajustar la fuente y el tamaño de la letra

            # Obtener el ancho y alto del texto
            text_width = text_item.boundingRect().width()
            text_height = text_item.boundingRect().height()

            # Calcular la posición centrada dentro del círculo
            text_x = x - text_width / 2
            text_y = y - text_height / 2

            text_item.setPos(text_x, text_y)

            # Añadir el círculo después de ajustar el tamaño de la letra y centrar el texto
            self.scene.addEllipse(x - circle_radius, y - circle_radius, circle_radius * 2, circle_radius * 2)

            if node.left is not None:
                self.scene.addLine(x, y, x - space, y + 100)
                self.drawTree(node.left, x - space, y + 100, space / 2)

            if node.right is not None:
                self.scene.addLine(x, y, x + space, y + 100)
                self.drawTree(node.right, x + space, y + 100, space / 2)

    def highlightPath(self, path):
        for node in path:
            self.highlightNode(node)

    def highlightNode(self, node):
        circle_radius = 25
        highlight_color = QColor(255, 165, 0)  # Color naranja como resaltado

        items = self.scene.items()
        for item in items:
            if isinstance(item, QGraphicsEllipseItem) and \
                    item.rect().width() == circle_radius * 2 and \
                    item.rect().height() == circle_radius * 2 and \
                    item.pos().x() == node.x - circle_radius and \
                    item.pos().y() == node.y - circle_radius:
                item.setBrush(QBrush(highlight_color))
                item.setScale(1.5)  # Aumenta el tamaño del nodo resaltado

    def closeEvent(self, event):
        # Emitir la señal de cierre cuando la ventana se cierra
        self.window_closed.emit()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BinaryTreeWindow()
    window.show()
    sys.exit(app.exec())
