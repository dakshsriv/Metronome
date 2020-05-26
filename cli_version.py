#!/usr/bin/python3

# This program is the base idea of the metronome app

import pygame
import time

def playNormal():
    pygame.mixer.music.load("/home/daksh/Downloads/pychess-1.0.0/sounds/obs_end.ogg")
    pygame.mixer.music.play()
    return

def playSubaccent():
    pygame.mixer.music.load("/home/daksh/Downloads/pychess-1.0.0/sounds/move1.ogg")
    pygame.mixer.music.play()
    return

def playAccent():
    pygame.mixer.music.load("/home/daksh/Downloads/pychess-1.0.0/sounds/invalid.ogg")
    pygame.mixer.music.play()
    return

def playRest():
    return
def getInfo(normal, subaccent, accent):
    def playMetronome():
        pygame.mixer.init()
        print()
        print("Sound player initiated")
        print()
        while True:
            ask = input("""Choose an action:\n
                    Edit for choosing the normal play settings,\n
                    Play for playing the basic,\n
                    Practice for choosing the practice mode feature,\n
                    Automator for choosing the super automating feature,\n
                    Rhythm for choosing the rhythm training feature,\n
                    Multirhythm for the multirhythm feature,\n
                    Subdivision for subdivision options,\n
                    and Quit to exit the app:
                    """
            dct = dict()
            if ask == "Quit":
                break
            elif ask == "Edit":
                a = input("How many beats are in a measure? ")
                b = input("What is the value of the beats? ")
                lst = list()
                for i in range(1, a+1):
                    x = input(f"For the beat number {i}, what tone level do you want? Rest, normal, subaccent, or accent?")
                dct = dict()
                    lst.append(x)
                dct["Playlist"] = lst
                dct["Beats per measure"] = a
                dct["One beat"] = b
            elif ask == "Subdivision":
                
        print()
        print("Leaving Game...")
        return
    print(playMetronome())
    return

if __name__ == "__main__":
    getInfo(playNormal, playSubaccent, playAccent)
