main = 0

import os

# Adds the time plugin, this allows us to wait a certain number of second

import time

# Adds the datetime plugin that makes it possible to display date and time

import datetime

# Allows you to set a custom exit messasge when you call this function

import music

# Imports the music module, declutters the main file

import color

# Imports the color module, more decluttering

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

try:
    import pygame
except ImportError:
    print("ERROR: You don't seem to have Pygame installed, refer to README.md for further instructions")

def emes(ems):

    cls()

    print(ems)

    exit()

# A more human-friendly version of time.sleep

def wait(sleep):

    time.sleep(sleep)


day = datetime.datetime.now()

# Prints the OS, for stuff like Linux, or MacOS it will return Unix-like instead of the OS name

def getsys():

    if os.name == "nt":

        sys = "Windows"

    else:

        sys = "Unix-like"

    return sys

# Sets the SDK version

sdkver = "1.16.3"

def version():
    global sdkver
    return sdkver

# prints the current BPT version, made for providing credit

def credits():

    print("Basic Python Toolkit version " + sdkver + " By SrFluff. (GitHub)")

# Screen clearing

def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

answer = "1"

# Basic math functions

def add(b, c):
    return b + c
def mul(d, e):
    return d * e
def sub(f, g):
    return f - g
def div(h, i):
    return h / i

# Using the datetime module it prints the weekday, month, day, and year

def date():

    return day.strftime("%A") + ", " + day.strftime("%B") + " " + day.strftime("%d") + " " + day.strftime("%Y")

# Using datetime this prints the time in 12h AM PM

def timed():

    return day.strftime("%I") + ":" + day.strftime("%M") + ":" + day.strftime("%S") + " " + day.strftime("%P")

# Using datetime this prints both date and time

def datetime():

    return day.strftime("%A") + ", " + day.strftime("%B") + " " + day.strftime("%d") + " " + day.strftime("%Y") + " @ " + day.strftime("%I") + ":" + day.strftime("%M") + ":" + day.strftime("%S") + " " + day.strftime("%P")

# Colorama is the plugin required to color or highlight text

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
            print("version    - Prints the current SDK version")
            print("music      - Initializes the music shell")
            print("wait       - Waits a specified amount of seconds")
            print("exit       - Exits the Basic-Python-Toolkit-Terminal-Environment\n")
        elif a == "cls":
            cls()
        elif a == "music":
            music.shell()
        elif a == "wait":
            wait(int(a))
        elif a == "version":
            print(version())
        elif a == "error":
            b = input("Error message: ")
            error(a)
        elif a == "emes":
            b = input("Message: ")
            emes(b)
        elif a.split()[0] == "hiw":
            color.hiw(a[4:])
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
            a = int(input("Color (0-5): "))
            b = input("Text: ")
            color.color(b,a)
        elif a == "exit":
            cls()
            print("Thanks for using the Basic-Python-Toolkit Terminal Environment!\n")
            break

# It's a pop-up window, with a warning

def warning(warning="No warning",x=10,y=10):
    
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gx = pygame.mouse.get_pos()[0]
                gy = pygame.mouse.get_pos()[1]

                if gx > 10 and gx < 190 and gy > 60 and gy < 90:
                    main = False
        screen.blit(my_font.render(warning,True,(0,0,0)),(x,y))
        gx = pygame.mouse.get_pos()[0]
        gy = pygame.mouse.get_pos()[1]
        if not gx > 10 or not gx < 190 or not gy > 60 or not gy < 90:
            pygame.draw.rect(screen,(185,185,185),(10,60,180,30))
            pygame.draw.rect(screen,(255,255,255),(12,62,176,26))
        else:
            pygame.draw.rect(screen,(155,155,155),(10,60,180,30))
            pygame.draw.rect(screen,(200,200,200),(12,62,176,26))
        
        screen.blit(my_font.render("Ok",True,(0,0,0)),(90,65))
        pygame.display.flip()
