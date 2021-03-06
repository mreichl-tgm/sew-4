import socket
import threading

from PySide import QtCore


class Server(QtCore.QThread):
    # Create QtSignals
    msgSignal = QtCore.Signal(str)
    errSignal = QtCore.Signal(str)
    connSignal = QtCore.Signal(str)
    quitSignal = QtCore.Signal(str)

    def __init__(self,
                 host="localhost",
                 port=5500,
                 parent=None,
                 msg_handler=None, err_handler=None, conn_handler=None, quit_handler=None):
        """
        A python Server using sockets

        :param msg_handler: Method to call on msgSignal
        :param err_handler: Method to call on errSignal
        :param conn_handler: Method to call on connSignal
        :param quit_handler: Method to call on quitSignal
        :param port: Port used for the server
        :param host: Host used for the server
        """
        super(Server, self).__init__(parent)
        # Defining Host, Port and Client List
        self.HOST = host
        self.PORT = port
        self.CLIENTS = []
        # Connect the signals with their handlers
        self.msgSignal.connect(msg_handler)
        self.errSignal.connect(err_handler)
        self.connSignal.connect(conn_handler)
        self.quitSignal.connect(quit_handler)
        # Create server socket, bind it to HOST and PORT, start listening
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen(10)
        # Log success
        print("Server running on %s: %s)" % (self.HOST, self.PORT))

    def run(self):
        """
        Accepts new connections and adds them to the client list
        """
        counter = 0

        try:
            while 1:
                print("Waiting...")
                (client_socket, address) = self.server_socket.accept()
                self.CLIENTS.append(client_socket)

                self.connSignal.emit("client%s" % counter)

                handler = threading.Thread(target=self.client_handler, args=(client_socket, counter))
                handler.start()

                self.broadcast(client_socket, "client%s is now online!" % counter)

                counter += 1

        except socket.error:
            print("Server was closed!")
            return

    def client_handler(self, sock, counter):
        """
        Handles the client

        :param sock: Clients socket
        :param counter: Clients ID
        """
        while 1:
            try:
                data = sock.recv(4096).decode()
                if data:
                    # Client sends valid data
                    if data.upper() == "QUIT":
                        self.quitSignal.emit("client%s" % counter)
                        self.broadcast(sock, "client%s is now offline!" % counter)

                        sock.close()
                        self.CLIENTS.remove(sock)
                        return
                    else:
                        self.msgSignal.emit(data)
                        self.broadcast(sock, data)

            except socket.error:
                self.quitSignal.emit("client%s" % counter)
                print("client%s is offline" % counter)

                sock.close()
                self.CLIENTS.remove(sock)
                return

    def broadcast(self, sock, msg):
        """
        Send broadcast message to all clients other than the server socket and the client socket from which the data
        is received.
        """
        for s in self.CLIENTS:
            if s != self.server_socket and s != sock:
                s.send(msg.encode())

        self.msgSignal.emit(msg)

    def close(self):
        """
        Public method to close the server
        """
        self.server_socket.close()
        self.quit()
