from observer.observer import Observer


class Subscriber(Observer):
    def __init__(self, name=None):
        """
        A subscriber of publishers and newspapers

        :param name: str
        """
        self.name = name if name else input("This subscriber's name: ")
        self.feed = [name + "'s feed:"]

    def update(self, new=False, target=None, publisher=None, newspaper=None, content=None, *args, **kwargs):
        """
        Overrides Observer.update to update the subscriber's feed according to various arguments

        :param new: bool
        :param target: Observable
        :param publisher: Publisher
        :param newspaper: Newspaper
        :param content: str
        :param args: any
        :param kwargs: {str: any}

        :return: None
        """
        print("", new, target, publisher, newspaper, content)
        if new and target:
            self.feed.append("Now following %s" % target.name)
            return

        if publisher and newspaper and content:
            self.feed.append("%s released a new version of %s" % (publisher.name, newspaper.name))
            self.feed.append(content)
            return

        if publisher and newspaper:
            self.feed.append("%s released a new newspaper called %s" % (publisher.name, newspaper.name))
            return

        print("Received invalid arguments: %s and keywords: %s!" % ("".join(args), "".join(kwargs)))
