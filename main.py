import sys

import random as rd
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.painter = False
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.painter = True
        self.repaint()

    def paintEvent(self, event):
        if self.painter:
            qp = QPainter()
            qp.begin(self)
            self.paint(qp)
            qp.end()

    def paint(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x, y = rd.choice(range(600)), rd.choice(range(600))
        r = rd.choice(range(min(600 - x, 600 - y)))
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())