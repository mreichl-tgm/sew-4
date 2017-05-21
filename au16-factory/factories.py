import os

from products import *


class ATrackFactory:
    def __init__(self, player):
        """
        The abstract Track player containing most functionality
        """
        self.player = player
        # Initial values
        self.loaded = False
        self.playing = False
        # Create a playlist and an index (used to avoid closed loop)
        self.playlist = []
        self.index = 0

    def load(self):
        """
        Loads tracks into the playlist
        """
        pass

    def play(self):
        """
        Plays tracks from the playlist and also loads it if not done before
        """
        if not self.loaded:
            self.load()

        self.playing = True

        while self.playing:
            track = self.playlist[self.index]
            # Pass the own player
            track.play(self.player)

            self.index += 1
            if self.index >= len(self.playlist):
                break

    def pause(self):
        """
        Pauses the player
        """
        if self.player.playing:
            self.player.pause()
        else:
            self.player.play()


class MockupFactory(ATrackFactory):
    def load(self):
        self.playlist = []
        self.playlist.append(TrackMockup("Ich bin ein Array", "Dj Martinides", "Sew"))


class FileFactory(ATrackFactory):
    def load(self):
        self.playlist = []

        for filename in os.listdir("tracks"):
            self.playlist.append(TrackFile("tracks/" + filename))
