class Model:
    def __init__(self):
        """
        MVC Model - A Stock of Values

        Holds the number of cols and rows.
        """
        self.cols = 8
        self.rows = 4
        self.number = 0
        self.fails = 0
        self.streak = 0
        self.time = 0
        self.interval = 1.5
        self.score = 0
