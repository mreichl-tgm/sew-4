from PySide.QtGui import QMainWindow

from view.mainwindow import Ui_MainWindow


class View(QMainWindow, Ui_MainWindow):
    points = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
