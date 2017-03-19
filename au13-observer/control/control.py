from PySide.QtGui import QTreeWidgetItem

from news.publisher import Publisher
from subscribe.subscriber import Subscriber
from view.view import View


class Control:
    def __init__(self):
        super().__init__()
        self.view = View()
        # Local containers to test functionality
        self.publishers = {}
        self.subscribers = {}
        # Add Qt Signals
        self.view.publishers.itemDoubleClicked.connect(self.register)
        self.view.subscribers.itemClicked.connect(self.update_feed)
        # For testing
        self.add_publisher("Die Tagespresse")
        self.add_publisher("Der Postillion")
        self.add_publisher("Der Kojote")

        self.add_subscriber("Robert")
        self.add_subscriber("Hannes")
        self.add_subscriber("Leon")

    def update(self):
        self.view.update()

    def update_feed(self, item, column):
        subscriber = self.subscribers[item.text(column)][0]

        if subscriber:
            self.view.feed.setText("\n".join(subscriber.feed))

    def add_publisher(self, name):
        # Add widget to tree
        widget = QTreeWidgetItem()
        widget.setText(0, name)
        self.view.publishers.addTopLevelItem(widget)
        # Add publisher to list
        self.publishers[name] = [Publisher(name), widget]

    def add_newspaper(self, publisher_name, name):
        widget = QTreeWidgetItem()
        widget.setText(0, name)

        publisher = self.publishers[publisher_name]
        publisher[0].add_newspaper(name)

    def register(self, item, column):
        for selected in self.view.subscribers.selectedItems():
            subscriber = self.subscribers[selected.text(column)][0]
            publisher = self.publishers[item.text(column)][0]

            if subscriber and publisher:
                publisher.register(subscriber)
                print("%s subscribed to %s" % (subscriber.name, publisher.name))

    def add_subscriber(self, name):
        # Add widget to tree
        widget = QTreeWidgetItem()
        widget.setText(0, name)
        self.view.subscribers.addTopLevelItem(widget)
        # Add subscriber to list
        self.subscribers[name] = [Subscriber(name), widget]
