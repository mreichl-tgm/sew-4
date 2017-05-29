import pyglet


class ATrack:
    def __init__(self, title, interpret, album):
        self.title = title
        self.interpret = interpret
        self.album = album

    def play(self, player):
        pass


class TrackMockup(ATrack):
    def play(self, player):
        print("Sie hören den Titel %s von %s aus dem Album %s" % (self.title, self.interpret, self.album))


class TrackFile(ATrack):
    def __init__(self, filename):
        super(TrackFile, self).__init__("1", "2", "3")
        self.filename = filename
        self.file = pyglet.media.load(self.filename)
        print("Loading %s successful!" % self.filename)

    def play(self, player):
        player.queue(self.file)
        player.play()
        pyglet.app.run()
        pyglet.app.exit()
        print("Track %s was queued" % self.title)
