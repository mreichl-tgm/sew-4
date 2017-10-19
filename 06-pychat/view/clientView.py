from PySide import QtGui

from view.ui.clientUi import Ui_MainWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Main window for the client
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
        View class for the client
        """
        self.frame = MainWindow()
        self.frame.show()

    def recv(self, *args, **kwargs):
        """
        Appends received messages to the chat

        :param args:
        :param kwargs:
        """
        self.frame.chat.append(args[0])
