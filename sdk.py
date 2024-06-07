import os

#Adds the time plugin, this allows us to wait a certain number of second

import time

#A more human-friendly version of time.sleep

def wait(cc):

    time.sleep(cc)

#Prints the OS, for stuff like Linux, or MacOS it will return Unix-like instead of the OS name

def getsys():

    if os.name == "nt":

        sys = "Windows"

    else:

        sys = "Unix-like"

    print(sys)

#Sets the SDK version

sdkver = "1.1.0"

#prints the current PBT version, made for providing credit

def credits():

    print("Basic Python Toolkit version " + sdkver + " By Franco M. (GitHub)")

#Screen clearing

def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
cls()

answer = "1"

#Basic math functions

def add(b, c):
    print(b + c)
def mul(d, e):
    print(d * e)
def sub(f, g):
    print(f - g)
def div(h, i):
    print(h / i)

#Colorama is the plugin required to color or highlight text

from colorama import Back, Fore

#Prints highlighted text

def hiw(hw):

# Resets the background color and text color

    print(Back.WHITE + Fore.BLACK + hw + Fore.RESET + Back.RESET)

cls()

print("Welcome to the Basic Python Toolkit\n")

hiw("You can highlight text by using hiw()")

print(Back.WHITE + Fore.BLACK + Fore.RESET + Back.RESET)

print("You can get your OS by using getsys()\n")

print("Use the wait() function to wait a certain about of seconds")

wait(2)

print("You are using a")

getsys()

print("system.\n")

a = input("> ")

exit()
