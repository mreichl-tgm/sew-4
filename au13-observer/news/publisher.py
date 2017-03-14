import time

from news.newspaper import Newspaper
from observer.observer import Observable


class Publisher(Observable):
    def __init__(self, name=None):
        super().__init__()

        self.id = time.time()
        self.name = name if name else input("This publisher's name: ")

        self.newspapers = []

        while True:
            task = input(">> ")
            if task == "/add":
                name = input("Newspaper's name: ")
                if self.add_newspaper(name):
                    print("Newspaper %s created!" % name)
                else:
                    print("Newspaper %s already created!" % name)

                continue

            if task == "/remove":
                name = input("Newspaper's name: ")
                if self.remove_newspaper(name):
                    print("Newspaper %s removed!" % name)
                else:
                    print("Newspaper %s does not exist!" % name)

                continue

            if task == "/update":
                name = input("Newspaper's name: ")
                if self.get_newspaper(name):
                    content = input("Your content: ")
                    if self.update_newspaper(name, content):
                        print("Published your content to %s!" % name)
                    else:
                        print("Failed to publish content to %s!" % name)
                else:
                    print("Newspaper %s does not exist!" % name)

                continue

            if task == "/quit":
                break

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
