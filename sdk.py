import os

#Imports socket, allows you to fetch your IP adress

import socket

hostname = socket.gethostname()

#Adds the time plugin, this allows us to wait a certain number of second

import time

#Adds the datetime plugin that makes it possible to display date and time

import datetime

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

    print(sys)

#Sets the SDK version

sdkver = "1.0.0"

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

#Using the datetime module it prints the weekday, month, day, and year

def date():

    print(day.strftime("%A") + ", " + day.strftime("%B") + " " + day.strftime("%d") + " " + day.strftime("%Y"))

#Using datetime this prints the time in 12h AM PM

def timed():

    print(day.strftime("%I") + ":" + day.strftime("%M") + ":" + day.strftime("%S") + " " + day.strftime("%P"))

#Using datetime this prints both date and time

def datetime():

    print(day.strftime("%A") + ", " + day.strftime("%B") + " " + day.strftime("%d") + " " + day.strftime("%Y") + " @ " + day.strftime("%I") + ":" + day.strftime("%M") + ":" + day.strftime("%S") + " " + day.strftime("%P"))

#Using sockey it prints your IP

def ip():

    print(socket.gethostbyname(hostname))

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

print("Use the wait() function to wait a certain about of seconds\n")

print("By using the timed() you can print the time in 12h AM PM, by using date() you'll print the weekday, month, day of the month, and year. And by using datetime() you'll print both together\m")

print("If you use the ip() function, you'll print your current IP address\n")

wait(2)

print("You are using a")

getsys()

print("system.\n")

date()

timed()

datetime()

ip()

a = input("> ")

exit()
