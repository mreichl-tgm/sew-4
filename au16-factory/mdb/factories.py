import os

from mdb.products import *


class ATrackFactory:
    def __init__(self):
        self.loaded = False
        self.playlist = []

    def load(self):
        pass

    def play(self):
        if not self.loaded:
            self.load()

        for track in self.playlist:
            track.play()


class MockupFactory(ATrackFactory):
    def load(self):
        self.playlist.append(TrackMockup())


class FileFactory(ATrackFactory):
    def load(self):
        for filename in os.listdir("tracks"):
            self.playlist.append(TrackFile("tracks/" + filename))
