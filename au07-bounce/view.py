from PySide.QtGui import QMainWindow, QPainter, QColor

from ui.view_ui import Ui_MainWindow


class View(QMainWindow, Ui_MainWindow):
    points = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.painter = QPainter()

    def paintEvent(self, event):
        self.painter.begin(self)

        for p in self.points:
            self.painter.setPen(QColor(p.clr[0], p.clr[1], p.clr[2]))
            self.painter.drawEllipse(p.x.value, p.y.value, p.rad.value, p.rad.value)

        self.painter.end()

    def resizeEvent(self, event):
        for p in self.points:
            p.resize(self.canvas.size().width(), self.canvas.size().height())

    def closeEvent(self, event):
        for p in self.points:
            p.join()

        event.accept()
