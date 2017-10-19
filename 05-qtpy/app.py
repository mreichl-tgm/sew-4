import sys

from PySide import QtGui

from control.control import Control


class App(QtGui.QApplication):
    def __init__(self):
        """
        Initializes the aap and creates an control instance
        """
        super().__init__(sys.argv)
        self.c = Control()


if __name__ == '__main__':
    app = App()
    app.exec_()
