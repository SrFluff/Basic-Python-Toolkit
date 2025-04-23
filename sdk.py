main = 0

import os

#Adds the time plugin, this allows us to wait a certain number of second

import time

#Adds the datetime plugin that makes it possible to display date and time

import datetime

#Allows you to set a custom exit messasge when you call this function

def emes(ems):

    cls()

    print(ems)

    exit()

#A more human-friendly version of time.sleep

def wait(sleep):

    time.sleep(sleep)


day = datetime.datetime.now()

#Prints the OS, for stuff like Linux, or MacOS it will return Unix-like instead of the OS name

def getsys():

    if os.name == "nt":

        sys = "Windows"

    else:

        sys = "Unix-like"

    return sys

#Sets the SDK version

sdkver = "1.10.2"

def version():
    global sdkver
    return sdkver

#prints the current PBT version, made for providing credit

def credits():

    print("Basic Python Toolkit version " + sdkver + " By SrFluff. (GitHub)")

#Screen clearing

def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

answer = "1"

#Basic math functions

def add(b, c):
    return b + c
def mul(d, e):
    return d * e
def sub(f, g):
    return f - g
def div(h, i):
    return h / i

#Using the datetime module it prints the weekday, month, day, and year

def date():

    return day.strftime("%A") + ", " + day.strftime("%B") + " " + day.strftime("%d") + " " + day.strftime("%Y")

#Using datetime this prints the time in 12h AM PM

def timed():

    return day.strftime("%I") + ":" + day.strftime("%M") + ":" + day.strftime("%S") + " " + day.strftime("%P")

#Using datetime this prints both date and time

def datetime():

    return day.strftime("%A") + ", " + day.strftime("%B") + " " + day.strftime("%d") + " " + day.strftime("%Y") + " @ " + day.strftime("%I") + ":" + day.strftime("%M") + ":" + day.strftime("%S") + " " + day.strftime("%P")

#Colorama is the plugin required to color or highlight text

try:
    from colorama import Back, Fore
except ImportError:
    emes("Hey, by the way, you need Colorama to run this project, to install use pip, or apt :)")

#Prints colored text

def color(text="",col="w",prin=True):
    match col:
        case "w":
            ret = Fore.WHITE + text + Fore.RESET
        case "r":
            ret = Fore.RED + text + Fore.RESET
        case "g":
            ret = Fore.GREEN + text + Fore.RESET
        case "b":
            ret = Fore.BLUE + text + Fore.RESET
        case "y":
            ret = Fore.YELLOW + text + Fore.RESET
        case "c":
            ret = Fore.CYAN + text + Fore.RESET
        case "W":
            ret = Fore.BLACK + Back.WHITE + text + Fore.RESET + Back.RESET
    if prin:
        print(ret)
    else:
        return ret

# Prints highlighted text

def hiw(hw):

# Resets the background color and text color

    print(Back.WHITE + Fore.BLACK + hw + Fore.RESET + Back.RESET)

# Prints an error message

def error(text="No error message",printf=True):
    
    # You can either print or return

    if printf:
        print(Fore.RED + "ERROR: " + text + Fore.RESET)
    else:
        return Fore.RED + "ERROR: " + text + Fore.RESET

# The BPTTE, I'll add more commands later

def init():

    print("Welcome to the Basic-Python-Toolkit Terminal Environment\n")
    while True:

        a = input("$ ")

        if a == "help":
            print("help       - Prints the help message")
            print("cls        - Clears the screen")
            print("error      - Prints a spoof error message")
            print("hiw [text] - Prints highlighted text")
            print("emes       - Prints a message, and exits")
            print("credits    - Prints the credits")
            print("date       - Prints the date")
            print("time       - Prints the time")
            print("datetime   - Prints both")
            print("getsys     - Prints the currently detected OS")
            print("exit       - Exits the Basic-Python-Toolkit-Terminal-Environment\n")
        elif a == "cls":
            cls()
        elif a == "error":
            b = input("Error message: ")
            error(a)
        elif a == "emes":
            b = input("Message: ")
            emes(b)
        elif a.split()[0] == "hiw":
            hiw(a[4:])
        elif a == "credits":
            credits()
        elif a == "date":
            print(date())
        elif a == "time":
            print(timed())
        elif a == "datetime":
            print(datetime())
        elif a == "getsys":
            print(getsys())
        elif a == "color":
            a = input("Color (w,r,g,b,y,c,W): ")
            b = input("Text: ")
            color(b,a)
        elif a == "exit":
            cls()
            print("Thanks for using the Basic-Python-Toolkit Terminal Environment!\n")
            break

# It's a pop-up window, with a warning

def warning(warning="No warning",x=0,y=0):
    
    try:
        import pygame
    except ImportError:
        print("Woah, you need Pygame to run this, refer to README.md for instructions")
        exit()
    
    main = True
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Warning")

    screen = pygame.display.set_mode((200,100))
    my_font = pygame.font.SysFont("Consolas",20)

    while main:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
        screen.blit(my_font.render(warning,True,(0,0,0)),(x,y))
        pygame.display.flip()

# The music shell, I'll add loading and unloading while in the shell later

def musicLoop(pathToMusic,volume):
    try:
        from pygame import mixer
    except ImportError:
        print("Woah, you need Pygame to run this, refer to README.md for instructions")
        exit()
    mixer.init()
    mixer.music.load(pathToMusic)
    mixer.music.set_volume(volume)
    mixer.music.play()
    pause = False
    main = True
    print("Type 'help' for help")
    while main:
        a = input("$ ")
        if a == "p":
            if pause:
                mixer.music.unpause()
                pause = False
            else:
                mixer.music.pause()
                pause = True
        elif a == "help":
            print("p - Pauses and unpauses the song")
            print("e - Exits the music shell")
        elif a == "e":
            mixer.music.stop()
            main = False
