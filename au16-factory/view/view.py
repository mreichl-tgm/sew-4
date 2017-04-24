from PySide.QtGui import QMainWindow

from view.mainwindow import Ui_MainWindow


class View(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Instantiates the graphical user interface
        """
        super().__init__()
        self.setupUi(self)
        self.show()
