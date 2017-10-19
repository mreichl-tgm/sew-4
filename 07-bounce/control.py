import random
import time
from multiprocessing import Array
from multiprocessing import Process, Value

from view import View


class Control(Process):
    def __init__(self):
        super().__init__()
        self.view = View()
        self.view.button_new.clicked.connect(self.add_point)
        self.view.button_remove.clicked.connect(self.remove_point)

    def update(self):
        self.view.update()

    def add_point(self):
        p = Point(random.randint(10, self.view.canvas.size().width()),
                  random.randint(10, self.view.canvas.size().height()),
                  self.view.canvas.size().width(),
                  self.view.canvas.size().height(),
                  random.randint(100, 1000),
                  random.randint(10, 40),
                  [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])

        p.start()
        self.view.points.append(p)

    def remove_point(self):
        last = len(self.view.points) - 1
        if last > - 1:
            self.view.points[last].join()
            self.view.points.pop(last)


class Point(Process):
    def __init__(self, x, y, mx, my, speed=100, radius=10, color=(255, 255, 255)):
        super().__init__()

        self.x = Value("i", x)
        self.y = Value("i", y)
        self.mx = Value("i", mx)
        self.my = Value("i", my)
        self.rad = Value("i", radius)
        self.spd = Value("i", speed)
        self.clr = Array("i", color)

        self.dx = Value("i", -1)
        self.dy = Value("i", 1)

        self.__closing = Value("i", 0)

    def resize(self, mx, my):
        self.mx.value = mx
        self.my.value = my

    def join(self, timeout=None):
        self.__closing.value = 1

    def run(self):
        while not self.__closing.value:
            time.sleep(1 / self.spd.value)
            self.x.value += self.dx.value
            self.y.value += self.dy.value

            if self.x.value <= 10 or self.x.value >= self.mx.value:
                self.dx.value *= -1

            if self.y.value <= 10 or self.y.value >= self.my.value:
                self.dy.value *= -1
