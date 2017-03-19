from observer.observer import Observer


class Subscriber(Observer):
    def __init__(self, name=None):
        self.name = name if name else input("This subscriber's name: ")
        self.feed = [name + "'s feed:"]

    def update(self, new=False, target=None, *args, **kwargs):
        if new and target:
            self.feed.append("Now following %s" % target.name)

        elif len(args) > 1:
            publisher = args[0]
            newspaper = args[1]

            if len(args) > 2:
                content = args[2]

                self.feed.append("%s released a new version of %s" % (publisher.name, newspaper.name))
                self.feed.append(content)
                return

            self.feed.append("%s released a new newspaper called %s" % (publisher.name, newspaper.name))
            return

        print("Received invalid arguments: %s and keywords: %s!" % ("".join(args), "".join(kwargs)))
