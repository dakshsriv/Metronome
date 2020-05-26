#!/usr/bin/python3

import pygame
import time

def play_sound1():
    pygame.mixer.music.load("/home/daksh/Downloads/pychess-1.0.0/sounds/obs_end.ogg")
    pygame.mixer.music.play()
    return

def play_sound2():
    pygame.mixer.music.load("/home/daksh/Downloads/pychess-1.0.0/sounds/move1.ogg")
    pygame.mixer.music.play()
    return

def play_sound3():
    pygame.mixer.music.load("/home/daksh/Downloads/pychess-1.0.0/sounds/invalid.ogg")
    pygame.mixer.music.play()
if __name__ == "__main__":
    pygame.mixer.init()
    play_sound1()
    time.sleep(1)
    print('Sound loaded')
    for i in range(0,10):
        play_sound1()
        time.sleep(0.5)
        play_sound2()
        time.sleep(0.5)
        play_sound3()
        time.sleep(0.5)
