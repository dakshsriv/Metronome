#!/usr/bin/python3

# This program is the base idea of the metronome app

import pygame
import time

def play_normal():
    pygame.mixer.music.load("/home/daksh/Downloads/pychess-1.0.0/sounds/obs_end.ogg")
    pygame.mixer.music.play()
    return

def play_subaccent():
    pygame.mixer.music.load("/home/daksh/Downloads/pychess-1.0.0/sounds/move1.ogg")
    pygame.mixer.music.play()
    return

def play_accent():
    pygame.mixer.music.load("/home/daksh/Downloads/pychess-1.0.0/sounds/invalid.ogg")
    pygame.mixer.music.play()
    return

def metronome(bpm):
    pygame.mixer.init()
    print()
    print("Sounds loaded")
    delay = time.sleep(0.1)
    for i in range(0, 10):
        play_normal()
        time.sleep(60 / bpm)
    return

if __name__ == "__main__":
    metronome(100)
