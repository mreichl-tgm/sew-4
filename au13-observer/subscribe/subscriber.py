from observer.observer import Observer


class Subscriber(Observer):
    def __init__(self, name=None):
        self.following = []
        self.name = name if name else input("This subscriber's name: ")

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
