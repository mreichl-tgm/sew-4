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
        self.view.send_button.clicked.connect(self.send)
        self.view.update_button.clicked.connect(self.update)
        # For testing
        p1 = Publisher("Der beste Verlag")
        p1.add_newspaper("Die beste Zeitung")
        p1.add_newspaper("Die besten News")

        p2 = Publisher("Der coolste Verlag")
        p2.add_newspaper("Die coolste Zeitung")

        self.publishers[p1.name] = p1
        self.publishers[p2.name] = p2

        s1 = Subscriber("Hans")
        s2 = Subscriber("Peter")
        s3 = Subscriber("Günther")

        self.subscribers[s1.name] = s1
        self.subscribers[s2.name] = s2
        self.subscribers[s3.name] = s3
        # Initial update
        self.update()

    def update(self):
        self.view.publishers.clear()
        self.view.subscribers.clear()

        for publisher in self.publishers.values():
            p_widget = QTreeWidgetItem()
            p_widget.setText(0, publisher.name)

            for newspaper in publisher.newspapers:
                n_widget = QTreeWidgetItem(p_widget)
                n_widget.setText(0, newspaper)

            self.view.publishers.addTopLevelItem(p_widget)

        for subscriber in self.subscribers:
            s_widget = QTreeWidgetItem()
            s_widget.setText(0, subscriber)
            self.view.subscribers.addTopLevelItem(s_widget)

    def update_view(self):
        self.view.update()

    def update_feed(self, item, column):
        subscriber = self.subscribers[item.text(column)]

        if subscriber:
            self.view.feed.setText("\n".join(subscriber.feed))

    def send(self):
        for selected in self.view.publishers.selectedItems():
            if selected.parent():
                newspaper = self.publishers[selected.parent().text(0)].newspapers[selected.text(0)]
                newspaper.publish(self.view.input.toPlainText())
                print("Updating newspaper", newspaper.name)

        self.view.input.clear()

    def register(self, item, column):
        for selected_subscriber in self.view.subscribers.selectedItems():
            subscriber = self.subscribers[selected_subscriber.text(column)]

            for selected_observable in self.view.publishers.selectedItems():
                if selected_observable.parent():
                    observable = self.publishers[selected_observable.parent().text(0)].newspapers[selected_observable.text(0)]
                else:
                    observable = self.publishers[item.text(column)]

            if subscriber and observable:
                observable.register(subscriber)
                print("%s subscribed to %s" % (subscriber.name, observable.name))
