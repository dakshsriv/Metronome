#!/usr/bin/python3

# This program is the CLI version of metronome

from pprint import pprint
import pygame
import time
import argparse
import json


def playNormal():
    pygame.mixer.music.load("/home/daksh/Projects/pychess/sounds/obs_end.wav")
    pygame.mixer.music.play()
    return


def playSubaccent():
    pygame.mixer.music.load("/home/daksh/Projects/pychess/sounds/move1.wav")
    pygame.mixer.music.play()
    return


def playAccent():
    pygame.mixer.music.load("/home/daksh/Projects/pychess/sounds/invalid.wav")
    pygame.mixer.music.play()
    return


def play_music():
    pygame.mixer.init()
    data = dict()
    with open("normalSettings.json", "r") as f:
        data = json.load(f)
        f.close()
    items = data["edit"]
    bpm = items[-1]
    subdivision = int(items[-2])
    beats = items[0]
    value = items[1]
    level = items[2:-2]
    print()
    print("Playing settings")
    pprint(data)
    print()
    for i in range(0, 4):
        playspeed = bpm * subdivision * int(value / 4)
        playspeed = 100
        for i in level:
            if i == "a":
                playAccent()
            elif i == "s":
                playSubaccent()
            elif i == "n":
                playNormal()
            time.sleep(60 / int(playspeed))


def store_settings(args):
    settings = dict()
    a = args.edit
    b = a.split(",")
    b[0] = int(b[0])
    b[1] = int(b[1])
    b[-1] = int(b[-1])
    settings["edit"] = b
    with open("normalSettings.json", "w") as f:
        json.dump(settings, f, indent=True)
        f.close()
    pprint(f"settings loaded is {settings}")
    return


def store_multi(ratio):
    settings = dict()
    a = args.multiedit
    b = a.split(",")
    b[0] = int(b[0])
    b[1] = int(b[1])
    settings["multiedit"] = b
    with open("multiRhythmSettings.json", "w") as f:
        json.dump(settings, f, indent=True)
        f.close()
    pprint(f"settings loaded is {settings}")


def multi_play():
    pygame.mixer.init()
    data = dict()
    with open("multiRhythmSettings.json", "r") as f:
        data = json.load(f)
        f.close()
    items = data["multiedit"]
    print(items)
    ratio1 = int(items[0])
    ratio2 = int(items[1])
    bpm = int(items[1])
    s = 60 / bpm
    frequency1 = 1 / ratio1
    frequency2 = 1 / ratio2
    l = list()
    n = 0
    for i in range(0, ratio1):
        n = n + frequency1
        l.append(n)
    n = 0
    for i in range(0, ratio2):
        n = n + frequency2
        l.append(n)
    #pprint(l)
    l = sorted(l)
    l = l[:-1]
    #pprint(l)
    for i in range(0, len(l)):
        l[i] = round(l[i], 2)
    print()
    print("Playing settings")
    print()
    for i in range(0, 4):
        n = 0
        for i in l:
            f = i - n
            if i == 1:
                playAccent()
            time.sleep(f)
            print(f, l)
            playNormal()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e",
        "--edit",
        type=str,
        default="",
        help="Enter beat settings. Example: 4,4,n,a,r,s,1,60 for 4, 4, Normal, Accent, Rest, Subaccent, 1 beat subdivision, 60 bpm respectively.",
    )
    parser.add_argument(
        "-edit",
        "--multiedit",
        type=str,
        default="",
        help="Enter multirhythm settings. Example: 4,5,60 for Ratio of 4 to 5 at 60 bpm.",
    )
    parser.add_argument("-p", "--play", help="Play?", action="store_true")
    parser.add_argument("-play", "--multiplay", help="Play?", action="store_true")
    args = parser.parse_args()
    if args.play:
        play_music()
    elif args.edit:
        store_settings(args)
    elif args.multiedit:
        store_multi(args)
    elif args.multiplay:
        multi_play()
