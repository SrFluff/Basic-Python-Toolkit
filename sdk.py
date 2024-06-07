import os

#Screen clearing

def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
cls()

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
