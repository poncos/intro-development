import sys, random

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtCore


# http://zetcode.com/gui/pyqt5/painting/
class Canvas(QWidget):

    coord_x = 10
    coord_y = 10
    width = 150

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.text = "Hello \nHow Are you?"

        self.setGeometry(300, 300, 1024, 1024)
        self.setWindowTitle('Programming is fun')
        self.show()

        timer = QtCore.QTimer(self, timeout=self.update, interval=33)
        timer.start()

    def paintEvent(self, event):
        print("paintEvent")
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        self.drawPoints(qp)
        self.drawArc(event, qp)
        qp.end()

    def update(self):
        super().update()

    def drawText(self, event, qp):
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()

        if size.height() <= 1 or size.height() <= 1:
            return

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)
    def drawArc(self, event, qp):
        qp.setPen(QColor(0, 0, 0))
        qp.setBrush(QColor(255, 0, 0))
        qp.drawPie(self.coord_x, self.coord_y, 150, 150, 45 * 16, 270 * 16)



def main():

    app = QApplication(sys.argv)
    canvas = Canvas()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()