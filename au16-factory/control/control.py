from view.view import View


class Control:
    def __init__(self):
        """
        The GUI's control unit used to update data and process user input
        """
        super().__init__()
        self.view = View()
