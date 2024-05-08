import sys
from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsSimpleTextItem
from PyQt6.QtCore import QPointF, QRectF, Qt
from PyQt6.QtGui import QPen, QColor
import math


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cabeza.siguiente = self.cabeza
        else:
            nuevo_nodo.siguiente = self.cabeza.siguiente
            self.cabeza.siguiente = nuevo_nodo

    def visualizar(self, scene):
        if not self.cabeza:
            print("La lista circular está vacía")
            return

        actual = self.cabeza
        nodos = []
        while True:
            nodos.append(actual)
            actual = actual.siguiente
            if actual == self.cabeza:
                break

        radio = 100
        centro = QPointF(200, 200)
        angulo = 0
        incremento_angulo = 360 / len(nodos)
        pen = QPen(QColor("black"))
        for nodo in nodos:
            x = centro.x() + radio * math.cos(math.radians(angulo))
            y = centro.y() + radio * math.sin(math.radians(angulo))
            rect = QGraphicsEllipseItem(QRectF(x - 25, y - 25, 50, 50))
            scene.addItem(rect)
            text = QGraphicsSimpleTextItem(str(nodo.dato))
            text.setPos(x - text.boundingRect().width() / 2, y - text.boundingRect().height() / 2)
            scene.addItem(text)
            angulo += incremento_angulo

            # Dibujar línea de conexión
            siguiente_x = centro.x() + radio * math.cos(math.radians(angulo))
            siguiente_y = centro.y() + radio * math.sin(math.radians(angulo))
            line = scene.addLine(x, y, siguiente_x, siguiente_y, pen)


# Crear la aplicación PyQt
app = QApplication(sys.argv)

# Crear la escena y la vista
scene = QGraphicsScene()
view = QGraphicsView(scene)
view.setWindowTitle("Lista Circular Visualizada como un Círculo")
view.setGeometry(100, 100, 400, 400)

# Crear y visualizar la lista circular
lista = ListaCircular()
lista.insertar(5)
lista.insertar(10)
lista.insertar(12)


lista.visualizar(scene)

# Mostrar la vista
view.show()

# Ejecutar la aplicación
sys.exit(app.exec())

