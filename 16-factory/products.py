import pyglet


class ATrack:
    def __init__(self, title, interpret, album):
        """
        Abstract base for a track
        :param title: title of the track
        :param interpret: interpret of the track
        :param album: album the track is featured in
        """
        self.title = title
        self.interpret = interpret
        self.album = album

    def play(self, player):
        """
        Abstract play function for the track
        :param player: Pyglet player used to play the track
        """
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
