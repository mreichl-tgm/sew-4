import time


class ATrackFactory:
    def __init__(self):
        self.loaded = False

    def load(self):
        pass

    def play(self):
        if not self.geladen:
            self.load()
        for song in self.playlist:
            song.play()
            time.sleep(1)
        print('Wir sind am Ende der Playliste angelangt. Auf Wiedersehen!')


class DisplayFactory(ATrackFactory):
    pass


class FileFactory(ATrackFactory):
    pass