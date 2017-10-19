import socket

from PySide import QtCore


class Client(QtCore.QThread):
    msgSignal = QtCore.Signal(str)

    def __init__(self, host="localhost", port=5500, parent=None, msg_handler=None):
        """
        A simple client connecting to a local server

        :param host: Host to connect to
        :param port: Port used to connect to the server
        """
        super(Client, self).__init__(parent)
        self.HOST = host
        self.PORT = port

        self.msgSignal.connect(msg_handler)

        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client_socket.connect((self.HOST, self.PORT))

    def run(self):
        """
        Receives messages for eternity as long as the socket receives valid data
        """
        while 1:
            try:
                data = self.__client_socket.recv(4096).decode()
                if data:
                    self.msgSignal.emit(str(data))
                else:
                    break
            except OSError as os_err:
                print("RECEIVER >> Socket Error: %s" % os_err)
                break

        self.__client_socket.close()

    def close(self):
        """
        Public method used to disconnect the client from the server
        """
        self.__client_socket.send("QUIT".encode())

    def send(self, msg):
        """
        Public method used to send a message to the server

        :param msg: str
        """
        self.__client_socket.send(msg.encode())
