import sys
from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QVBoxLayout, QWidget, QPushButton, QLineEdit, \
    QGraphicsItem
from PyQt6.QtCore import QRectF, Qt, QPointF, QLineF

class NodeItem(QGraphicsItem):
    def __init__(self, value):
        super().__init__()
        self.value = str(value)
        self.child_items = []
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

    def add_child(self, child):
        self.child_items.append(child)

    def boundingRect(self):
        return QRectF(-25, -15, 50, 30)

    def paint(self, painter, option, widget):
        painter.drawEllipse(-25, -15, 50, 30)
        painter.drawText(-7, 7, self.value)
        for child in self.child_items:
            start_pos = self.mapToScene(self.boundingRect().center())
            end_pos = child.mapToScene(child.boundingRect().center())
            line = QLineF(start_pos, end_pos)
            painter.drawLine(line)

class TreeView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Árbol Binario")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        layout.addWidget(self.view)

        self.input_box = QLineEdit(self)
        layout.addWidget(self.input_box)

        self.insert_button = QPushButton("Insertar", self)
        self.insert_button.clicked.connect(self.insert_node)
        layout.addWidget(self.insert_button)

        self.delete_button = QPushButton("Eliminar", self)
        self.delete_button.clicked.connect(self.delete_node)
        layout.addWidget(self.delete_button)

        # Ejemplo de árbol binario
        self.root = self.add_node(None, 10)
        node5 = self.add_node(self.root, 5)
        node15 = self.add_node(self.root, 15)
        self.add_node(node5, 3)
        self.add_node(node5, 8)
        self.add_node(node15, 12)
        self.add_node(node15, 18)

    def add_node(self, parent, value):
        node_item = NodeItem(value)
        if parent is None:
            node_item.setPos(400, 50)
        else:
            parent.add_child(node_item)
            node_item.setPos(parent.pos().x() + 100 if value > int(parent.value) else parent.pos().x() - 100, parent.pos().y() + 100)
        self.scene.addItem(node_item)
        return node_item

    def insert_node(self):
        value = int(self.input_box.text())
        self.add_node(self.root, value)

    def delete_node(self):
        # Implementar la lógica para eliminar un nodo aquí
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TreeView()
    window.show()
    sys.exit(app.exec())




