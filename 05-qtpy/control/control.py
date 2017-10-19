import random
import threading
import time

from PySide import QtGui, QtCore

from model.model import Model
from view.view import View


class Interval(threading.Thread):
    def __init__(self, function, condition, interval):
        """
        Iterates over a function while the condition is true in an interval of seconds

        :param function: callable
        :param condition: callable
        :param interval: int, float
        """
        super().__init__()
        self.function = function
        self.condition = condition
        self.interval = interval

    def run(self):
        while self.condition():
            self.function()
            time.sleep(self.interval)


class Control:
    def __init__(self):
        """
        MVC Controller - Master of space and time

        Instantiates view and model and generates the base grid with its buttons bound to an event.
        """
        self.model = Model()
        self.view = View()

        self.iv_update = Interval(self.update, self.view.frame.isVisible, self.model.interval)
        self.iv_time = Interval(lambda: self.update_time(1), self.view.frame.isVisible, 1)

        self.buttons = []

        # Create grid
        for row in range(self.model.rows):
            for col in range(self.model.cols):
                # Create the button and set its name
                button = QtGui.QPushButton(self.view.frame)
                button.setObjectName("b" + str(row) + str(col))

                # Click event for number buttons
                # b=button makes sure the right button is used when executed
                def button_event(b=button):
                    if b.text() == str(self.model.number + 1):
                        # Update stats
                        self.model.score += int(self.model.number + self.model.streak * (1 + 1 / (1 + self.model.time)))
                        self.model.number += 1
                        # Repaint stats
                        self.view.set_number(self.model.number)
                        self.model.streak += 1
                    else:
                        self.model.score -= self.model.number
                        self.model.streak = 0
                        self.model.fails += 1
                        self.view.set_fails(self.model.fails)

                    self.view.set_score(self.model.score)
                    self.view.set_streak(self.model.streak)

                # Connect appropriate button_event to the button
                QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), button_event)
                # Add reference of the button to buttons[]
                self.buttons.append(button)
                # Add button to grid
                self.view.frame.gridLayout.addWidget(button, row, col)
        # Connect scatter to new button
        QtCore.QObject.connect(self.view.frame.bnew, QtCore.SIGNAL("clicked()"), self.reset)
        # Initialize game
        self.reset()
        # Start time control
        self.iv_update.start()
        self.iv_time.start()

    def update(self):
        """
        Generates new numbers for all buttons in the button list
        """
        for b in self.buttons:
            b.setText(str(random.randint(1, self.model.number + len(self.buttons))))
        # Set a random numbers text to the next number
        self.buttons[random.randint(1, len(self.buttons) - 1)].setText(str(self.model.number + 1))

    def update_time(self, interval):
        """
        Increases time by the interval it is updated
        """
        self.model.time += interval
        self.view.set_time(str(self.model.time) + "s")

    def reset(self):
        """
        Resets all stats to their initial value
        """
        self.model = Model()

        self.view.set_number(self.model.number)
        self.view.set_fails(self.model.fails)
        self.view.set_streak(self.model.streak)
        self.view.set_time(self.model.time)
        self.view.set_score(self.model.score)

        self.update()
