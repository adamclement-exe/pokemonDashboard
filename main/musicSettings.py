"""
:author Basker12
"""

try:
    from tkinter import *
except ImportError:
    from tkinter import *
import pygame
import os
import random


class Music:

    randomSong = None

    def __init__(self):
        self.playlistMusic = list(["music/Lavender_Town.mp3", "music/Team_Skull.mp3", "music/Elite_Four.mp3",
                                   "music/Bede_Battle.mp3", "music/Champion_Battle.mp3", "music/Driftveil_City.mp3",
                                   "music/Pokemon_Theme_Lyrics.mp3"])

        pygame.mixer.init()

    def musicPlay(self):
        randomSong = random.choice(self.playlistMusic)
        pygame.mixer.music.load(randomSong)  # Loads a random song from the playlist
        pygame.mixer.music.queue(randomSong)
        pygame.mixer.music.play(loops=999)
        return randomSong

    def stopMusic(self, event):  # This definition stops the music completely
        pygame.mixer.music.stop()

    def pauseMusic(self, event):  # This definition pauses the music
        pygame.mixer.music.pause()

    def unpauseMusic(self, event):  # This definition unpauses the music
        pygame.mixer.music.unpause()

    def skipMusic(self, event):
        randomSong = random.choice(self.playlistMusic)

        pygame.mixer.music.stop()
        pygame.mixer.music.load(randomSong)
        pygame.mixer.music.play(loops=999)

    def musicControls(self, root):
        root.bind('<Control_L><s>', self.stopMusic)
        root.bind('<Control_L><p>', self.pauseMusic)
        root.bind('<Control_L><u>', self.unpauseMusic)
        root.bind('<Control_L><Right>', self.skipMusic)