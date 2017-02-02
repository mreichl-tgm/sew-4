import sys

from PySide import QtGui

from control.clientControl import Control as clientControl
from control.serverControl import Control as serverControl


class App(QtGui.QApplication):
    def __init__(self):
        """
        Initializes the app and creates an control instance
        """
        super().__init__(sys.argv)
        self.s1 = serverControl()
        self.c1 = clientControl("Markus")
        self.c2 = clientControl("Hannes")


if __name__ == '__main__':
    app = App()
    app.exec_()
