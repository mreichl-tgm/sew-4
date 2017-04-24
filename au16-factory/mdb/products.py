import pyglet


class ATrack:
    def __init__(self, title, interpret, album):
        self.title = title
        self.interpret = interpret
        self.album = album

    def play(self):
        pass


class TrackMockup(ATrack):
    def play(self):
        print("Just a mockup")


class TrackFile(ATrack):
    def __init__(self, filename):
        super(TrackFile, self).__init__("1", "2", "3")
        self.filename = filename

    def play(self):
        music = pyglet.media.load(self.filename)
        music.play()

        pyglet.app.run()

        # Missing some key element...

        pyglet.app.exit()