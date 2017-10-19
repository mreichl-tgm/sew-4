from PySide import QtGui

from view.ui.serverUi import Ui_MainWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Main window for the server
        """
        super().__init__()
        self.setupUi(self)
        self.onclose_method = None

    def onclose(self, function):
        """
        Used to modify the function called when closeEvent() is fired

        :param function:
        """
        self.onclose_method = function

    def closeEvent(self, event):
        if callable(self.onclose):
            self.onclose_method()

        event.accept()


class View:
    def __init__(self):
        """
        View used for the server
        """
        self.frame = MainWindow()
        self.frame.show()
