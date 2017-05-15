import threading

from mdb.factories import FileFactory
from view.view import View


class Control(threading.Thread):
    def __init__(self):
        """
        The GUI's control unit used to update data and process user input
        """
        super().__init__()
        self.view = View()

        self.file_factory = FileFactory()

        self.view.next.clicked.connect(self.file_factory.next)
        self.view.previous.clicked.connect(self.file_factory.previous)
        self.view.play.clicked.connect(self.file_factory.play)

    def run(self):
        self.file_factory.load()
        self.file_factory.play()
