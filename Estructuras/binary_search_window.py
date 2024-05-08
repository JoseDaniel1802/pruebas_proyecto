import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QPushButton, QVBoxLayout, QWidget, QInputDialog, QMessageBox, QGraphicsEllipseItem
from PyQt6.QtGui import QColor, QBrush, QFont  # Agregar QFont para ajustar el tamaño de la letra
from binary_search import NodoArbol, T, ArbolBusquedaBinaria

class BinarySearchTreeGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Árbol de Búsqueda Binaria GUI")
        self.tree = ArbolBusquedaBinaria()
        self.initUI()

    def initUI(self):
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.view.setSceneRect(0, 0, 800, 600)

        self.insertBtn = QPushButton("Insertar")
        self.deleteBtn = QPushButton("Eliminar")
        self.searchBtn = QPushButton("Buscar")

        self.insertBtn.clicked.connect(self.insertValue)
        self.deleteBtn.clicked.connect(self.deleteValue)
        self.searchBtn.clicked.connect(self.searchValue)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.insertBtn)
        layout.addWidget(self.deleteBtn)
        layout.addWidget(self.searchBtn)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

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
            value_item.setPos(x - value_item.boundingRect().width() / 2, y - value_item.boundingRect().height() / 2 - 10)
            value_item.setFont(QFont("Arial", 8))  # Ajustar tamaño de letra a 8 puntos

            address_item = self.scene.addText(address_text)
            address_item.setPos(x - address_item.boundingRect().width() / 2, y - address_item.boundingRect().height() / 2 + 10)
            address_item.setFont(QFont("Arial", 8))  # Ajustar tamaño de letra a 8 puntos

            if node.izquierda is not None:
                self.scene.addLine(x, y, x - space, y + 100)
                self.drawTree(node.izquierda, x - space, y + 100, space / 2)

            if node.derecha is not None:
                self.scene.addLine(x, y, x + space, y + 100)
                self.drawTree(node.derecha, x + space, y + 100, space / 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BinarySearchTreeGUI()
    window.show()
    sys.exit(app.exec())
