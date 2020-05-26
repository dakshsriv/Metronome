#!/usr/bin/env python
import PySimpleGUI as sg
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


def MetronomeGUI():
    # background = '#F0F0F0'
    # Set the backgrounds the same as the background on the buttons
    # sg.SetOptions(background_color=background, element_background_color=background)

    tab1_layout = [
        [sg.Text("Beats in a bar"), sg.Input(key="beats_in_bar")],
        [sg.Text("Value of Beats"), sg.Input(key="value_of_beats")],
        [
            sg.Text("Level of Beats"),
            sg.Button("Accent", key="accent"),
            sg.Button("SubAccent", key="subaccent"),
            sg.Button("Normal", key="normal"),
        ],
        [sg.Text("Level"), sg.Input(key="level_of_beats", disabled=True)],
        [sg.Text("Subdivision of Beats"), sg.Input(key="subdivision_of_beats")],
        [sg.Text("BPM"), sg.Input(key="bpm_of_beats")],
        [sg.Button("Save Rhythm")],
    ]

    tab2_layout = [
        [sg.Text("Ratio 1"), sg.Input(key="beats_in_bar")],
        [sg.Text("Ratio 2"), sg.Input(key="value_of_beats")],
        [sg.Text("BPM"), sg.Input(key="bpm")],
        [sg.Button("Save")],
    ]

    tab3_layout = [
        [sg.Button("Play Rhythm")],
    ]

    tab4_layout = [
        [sg.Button("Play Multirhythm")],
    ]

    layout = [
        [
            sg.TabGroup(
                [
                    [
                        sg.Tab("Edit Rhythm", tab1_layout, tooltip="Edit Rhythm"),
                        sg.Tab(
                            "Edit Multi-Rhythm",
                            tab2_layout,
                            tooltip="Edit Multi-Rhythm",
                        ),
                        sg.Tab("Play Rhythm", tab3_layout, tooltip="Play Rhythm"),
                        sg.Tab(
                            "Play Multi-Rhythm",
                            tab4_layout,
                            tooltip="Play Multi-Rhythm",
                        ),
                    ]
                ]
            )
        ],
    ]

    # Open a form, note that context manager can't be used generally speaking for async forms
    window = sg.Window("Metronome", layout)
    # Our event loop
    level_of_beats = ""
    while True:  # TIMEOUT_KEY
        event, values = window.read()  # Poll every 100 ms
        s = str()
        if event == "Exit" or event is None:
            break
        # If a button was pressed, disTIMEOUT_KEYplay it on the GUI by updating the text element
        if event != sg.TIMEOUT_KEY:
            sg.Print(f"Event: {event}")
        if event == "accent":
            level_of_beats = level_of_beats + " a"
        if event == "subaccent":
            level_of_beats = level_of_beats + " s"
        if event == "normal":
            level_of_beats = level_of_beats + " n"
        if event == "Save Rhythm":
            for i in range(0, int(values["beats_in_bar"])):
                print(s)
            settings = dict()
            s = level_of_beats.strip()
            print(s)
            s = s.split()
            print(s)
            with open("normalSettings.json", "w") as f:
                settings["beatsPerBar"] = int(values["beats_in_bar"])
                settings["valueOfBeat"] = 1 / int(values["value_of_beats"])
                settings["beatLevels"] = s
                settings["subdivision"] = int(values["subdivision_of_beats"])
                settings["beatsPerMinute"] = int(values["bpm_of_beats"])
                json.dump(settings, f, indent=True)
                f.close()
        window["level_of_beats"].update(level_of_beats)
        sg.Print(f"Level of beats: {level_of_beats}")
        if event == "Save":
            r1 = values["beats_in_bar0"]
            r2 = values["value_of_beats1"]
            frequency1 = 1 / int(r1)
            frequency2 = 1 / int(r2)
            l = list()
            n = 0
            bpm = values["bpm"]
            for i in range(0, int(r1)):
                n = n + frequency1
                l.append(n)
            n = 0
            for i in range(0, int(r2)):
                n = n + frequency2
                l.append(n)
            # pprint(l)
            l = sorted(l)
            l = l[:-1]
            # pprint(l)
            for i in range(0, len(l)):
                l[i] = round(l[i], 2)
            settings = dict()
            settings["BPM"] = bpm
            settings["Times"] = l
            with open("multiSettings.json", "w") as f:
                json.dump(settings, f, indent=True)
                f.close()
        if event == "Play Rhythm":
            pygame.mixer.init()
            data = dict()
            with open("normalSettings.json", "r") as f:
                data = json.load(f)
                f.close()
            print(data)
            bpm = data["beatsPerMinute"]
            subdivision = data["subdivision"]
            beats = data["beatsPerBar"]
            value = data["valueOfBeat"]
            level = data["beatLevels"]
            for i in range(0, 100):
                playspeed = bpm * subdivision * int(value / 4)
                playspeed = 100
                for i in level:
                    if i == "a":
                        playAccent()
                    elif i == "s":
                        playSubaccent()
                    elif i == "n":
                        playNormal()
                    if event == "Stop Metronome" or event == None:
                        break
                    time.sleep(60 / int(playspeed))
        if event == "Play Multirhythm":
            pygame.mixer.init()
            data = dict()
            with open("multiSettings.json", "r") as f:
                data = json.load(f)
                f.close()
            l = data["Times"]
            for i in range(0, 10):
                n = 0
                for i in l:
                    f = i - n
                    if i == 1:
                        playAccent()
                    time.sleep(f)
                    print(f, l)
                    playNormal()



MetronomeGUI()

