from mdb.factories import FileFactory
from view.view import View


class Control:
    def __init__(self):
        """
        The GUI's control unit used to update data and process user input
        """
        super().__init__()
        self.view = View()

        file_factory = FileFactory()
        file_factory.load()
        file_factory.play()
