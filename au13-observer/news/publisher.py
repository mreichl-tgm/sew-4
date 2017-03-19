import time

from news.newspaper import Newspaper
from observer.observer import Observable


class Publisher(Observable):
    def __init__(self, name=None):
        super().__init__()

        self.id = time.time()
        self.name = name if name else input("This publisher's name: ")

        self.newspapers = []

    def register(self, observer):
        super().register(observer)
        self.notify_all(new=True, target=self)

    def get_newspaper(self, name: str) -> (Newspaper, None):
        for newspaper in self.newspapers:
            if newspaper.name == name:
                return newspaper

        return None

    def add_newspaper(self, name: str = None) -> bool:
        if self.get_newspaper(name):
            return False

        newspaper = Newspaper(self, name)

        self.newspapers.append(newspaper)
        self.notify_all(self, newspaper)

        return True

    def remove_newspaper(self, name: str) -> bool:
        newspaper = self.get_newspaper(name)

        if newspaper:
            self.newspapers.remove(newspaper)
            return True

        return False

    def update_newspaper(self, name: str, content: str) -> bool:
        newspaper = self.get_newspaper(name)

        if newspaper:
            newspaper.publish(content)
            return True

        return False
