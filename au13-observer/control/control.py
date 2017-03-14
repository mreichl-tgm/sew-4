from view.view import View


class Control:
    def __init__(self):
        super().__init__()
        self.view = View()

    def update(self):
        self.view.update()
