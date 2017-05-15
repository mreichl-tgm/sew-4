import os

from pyglet.media import Player

from mdb.products import *


class ATrackFactory:
    def __init__(self):
        self.loaded = False
        self.playing = False

        self.playlist = []
        self.index = 0

        self.player = Player()

    def load(self):
        pass

    def play(self):
        if not self.loaded:
            self.load()

        self.playing = True

        while self.playing:
            track = self.playlist[self.index]
            # Pass the own player
            track.play(self.player)

            self.index += 1
            if self.index >= len(self.playlist):
                self.index = 0

    def pause(self):
        if self.player.playing:
            self.player.pause()
        else:
            self.player.play()

    def next(self):
        if self.playing:
            self.playing = False

        self.index += 1
        self.play()

    def previous(self):
        if self.playing:
            self.playing = False

        self.index -= 1
        self.play()


class MockupFactory(ATrackFactory):
    def load(self):
        self.playlist = []
        self.playlist.append(TrackMockup("Ich bin ein Array", "Dj Martinides", "Sew"))


class FileFactory(ATrackFactory):
    def __init__(self):
        super().__init__()

    def load(self):
        self.playlist = []

        for filename in os.listdir("tracks"):
            self.playlist.append(TrackFile("tracks/" + filename))
