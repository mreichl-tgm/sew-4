from PySide import QtCore

from chat.client import Client
from model.clientModel import Model
from view.clientView import View


class Control:
    def __init__(self, nickname="Unnamed"):
        """
        Control class used for the client

        :param nickname: Nickname to identify the client
        """
        self.view = View()
        self.model = Model(nickname)
        self.client = Client(msg_handler=self.recv)
        self.client.start()

        self.view.frame.setWindowTitle("Client - " + nickname)
        self.view.frame.onclose(self.client.close)

        QtCore.QObject.connect(self.view.frame.bsend, QtCore.SIGNAL("clicked()"), self.send)

    def recv(self, msg):
        self.view.frame.chat.append(msg)

    def send(self):
        """
        Gets the message from views msgbox and sends it as the client
        """
        msg = self.view.frame.msgbox.text()
        self.client.send(self.model.nickname + ": " + msg)
        self.view.frame.chat.append(msg)
        self.view.frame.msgbox.clear()
