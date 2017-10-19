from news.newspaper import Newspaper
from observer.observer import Observable


class Publisher(Observable):
    def __init__(self, name=None):
        """
        An observable publisher of newspapers

        :param name:
        """
        super().__init__()

        self.name = name if name else input("This publisher's name: ")
        self.newspapers = {}

    def register(self, observer):
        """
        Overrides observable.register to notify the observer when he is registered

        :param observer: Observer
        """
        super().register(observer)
        self.notify_all(new=True, target=self)

    def add_newspaper(self, name: str = None):
        """
        Adds a new newspaper to the newspaper list

        :param name: str
        """
        newspaper = Newspaper(self, name)

        self.newspapers[newspaper.name] = newspaper
        self.notify_all(publisher=self, newspaper=newspaper)

    def remove_newspaper(self, name: str) -> bool:
        """
        Removes a newspaper from the newspaper list

        :param name: str
        :return: bool
        """
        newspaper = self.newspapers[name]

        if newspaper:
            del self.newspapers[name]
            return True

        return False
