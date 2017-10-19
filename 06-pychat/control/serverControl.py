from chat.server import Server
from model.serverModel import Model
from view.serverView import View


class Control:
    def __init__(self):
        """
        Control class used for the server
        """
        self.model = Model()
        self.view = View()

        self.server = Server(msg_handler=self.msg_handler,
                             err_handler=self.err_handler,
                             conn_handler=self.conn_handler,
                             quit_handler=self.quit_handler)
        self.server.start()

        self.view.frame.onclose(self.server.close)

    def msg_handler(self, msg):
        """
        When called a message is logged in the view.

        :param msg: Message to broadcast
        """
        self.view.frame.log.append(msg)

    def err_handler(self, error):
        pass

    def conn_handler(self, client):
        self.view.frame.clients.addItem(client)

    def quit_handler(self, client):
        clients = self.view.frame.clients
        for i in range(clients.count()):
            if clients.item(i) and clients.item(i).text() == client:
                clients.takeItem(i)
