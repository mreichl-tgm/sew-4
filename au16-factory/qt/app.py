import sys

from PySide import QtGui
from control.control import Control


class App(QtGui.QApplication):
    def __init__(self):
        """
        Initializes the app and creates an control instance
        """
        super().__init__(sys.argv)
        self.control = Control()
        self.control.start()

        while self.control.view.isVisible():
            self.control.view.update()
            self.processEvents()

        sys.exit()

if __name__ == '__main__':
    app = App()
    app.exec_()
