from observer.observer import Observable


class Newspaper(Observable):
    def __init__(self, publisher, name: str):
        """
        Creates an observable newspaper which can publish specific content via a publisher to its observers

        :param publisher: Publisher
        :param name: str
        """
        super().__init__()
        self.publisher = publisher
        self.name = name

    def publish(self, content):
        self.notify_all(publisher=self.publisher, newspaper=self, content=content)
