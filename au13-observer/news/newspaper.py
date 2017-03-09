from observer.observer import Observable


class Newspaper(Observable):
    def __init__(self, publisher, name: str):
        super().__init__()
        self.publisher = publisher
        self.name = name

    def publish(self, content):
        self.notify_all(self.publisher, self, content)
