import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

mixer.init()

def load(path="/no/path/given"):
    if path == "/no/path/given":
        print("ERROR: NO PATH GIVEN\n")
    else:
        mixer.music.load(path)

def volume(vol=1):
    mixer.music.set_volume(vol)

def pause():
    mixer.music.pause()

def unpause():
    mixer.music.unpause()

def stop():
    mixer.music.stop()

def unload():
    mixer.music.unload()

def play():
    mixer.music.play()

def shell():
    print("Type 'help' for help")
    pause = False
    while True:
        a = input("$ ")
        if a == "help":
            print("load   - Loads a song")
            print("unload - Unloads the current song")
            print("Play   - Starts the current song from the beginning")
            print("volume - Sets the volume")
            print("p      - Pauses and unpauses the song")
            print("stop   - Stops the current song")
            print("exit   - Exits the shell")
        elif a == "load":
            b = input("Path: ")
            mixer.music.load(b)
            pause = True
        elif a == "play":
            mixer.music.stop()
            pause = False
            mixer.music.play()
        elif a == "p":
            if pause:
                mixer.music.unpause()
                pause = False
            else:
                mixer.music.pause()
                pause = True
        elif a == "volume":
            b = input("Volume(0-100): ")
            mixer.music.set_volume(int(b)/100)
        elif a == "unload":
            mixer.music.stop()
            pause = True
            mixer.music.unload()
        elif a == "exit":
            break
