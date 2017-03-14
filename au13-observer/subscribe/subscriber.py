from observer.observer import Observer


class Subscriber(Observer):
    def __init__(self):
        self.following = []

        while True:
            task = input(">> ")

            if task == "/follow":
                name = input("Publisher's name: ")

                if self.get_publisher(name):
                    print("You are already following this publisher")
                    continue

                continue

            if task == "/subscribe":
                name = input("Newspaper's name: ")

                if name:
                    print("Subscribed to newspaper %s !" % name)
                else:
                    print("Newspaper %s is not available!" % name)

                continue

            if task == "/unsubscribe":
                name = input("Newspaper's name: ")
                if name:
                    print("Subscription revoked from newspaper %s!" % name)
                else:
                    print("No subscription to Newspaper %s!" % name)

                continue

            if task == "/quit":
                break

    def update(self, *args, **kwargs):
        if len(args) > 1:
            publisher = args[0]
            newspaper = args[1]

            if len(args) > 2:
                content = args[2]

                print(publisher.name, "released a new version of", newspaper.name)
                print(content)
                return

            print(publisher.name, "released a new newspaper called", newspaper.name)
            return

        print("Received invalid arguments: %s and keywords: %s!" % ("".join(args), "".join(kwargs)))

    def get_publisher(self, name):
        for publisher in self.following:
            if publisher.name == name:
                return publisher

        return None
