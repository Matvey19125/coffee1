import sys
import math
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QBrush, QColor, QPen
draw_circle = False


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 650, 550)
        self.clicked = QPushButton("Нажать", self)
        self.clicked.move(275, 450)
        self.clicked.resize(150, 100)
        self.clicked.clicked.connect(self.shar)

    def shar(self):
        global draw_circle
        draw_circle = True
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        if draw_circle:
            radius = random.randint(10, 150)
            center_x = self.width() // 2
            center_y = self.height() // 2
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            brush = QBrush(QColor(red, green, blue))
            painter.setBrush(brush)
            painter.drawEllipse(center_x - radius, center_y - radius, 2 * radius, 2 * radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())