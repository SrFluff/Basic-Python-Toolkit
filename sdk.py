main = 0

import os

#Imports socket, allows you to fetch your IP adress

import socket

hostname = socket.gethostname()

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

    print(sys)

#Sets the SDK version

sdkver = "1.3.0"

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

print("By using the timed() you can print the time in 12h AM PM, by using date() you'll print the weekday, month, day of the month, and year. And by using datetime() you'll print both together\n")

print("If you use the ip() function, you'll print your current IP address\n")

print("If you want to set a custom message to display when you end the program, use the emes() function.")

wait(2)

print("You are using a")

getsys()

print("system.\n")

date()

timed()

datetime()

ip()

a = input("> ")

main = 1

s = 1

bptte = 0

while main:

    cls()

    if s == 1:

        hiw("[1] Enter terminal environment")
        print("[2] About BPT terminal")
        print("[3] Exit\n")

    if s == 2:

        print("[1] Enter terminal environment")
        hiw("[2] About BPT terminal")
        print("[3] Exit\n")

    if s == 3:

        print("[1] Enter terminal environment")
        print("[2] About BPT terminal")
        hiw("[3] Exit\n")
    
    a = input("> ")

    if a == "1":

        s = 1

    if a == "2":

        s = 2

    if a == "3":

        s = 3

    if a == "" and s == 1:

        cls()

        main = 0

        bptte = 1

        cls()

        print("Type 'help' for a list of commands")
    
    if a == "" and s == 2:

        s = 1

        cls()

        print("The Basic Python Toolkit Terminal Environment, or BPTTE, is a basic")
        print("terminal emulator, that comes with some commands. This also lets")
        print("you run some BPT commands like 'ipget' and 'getsys'.\n")

        a = input("> ")

        cls()

    if a == "" and s == 3:

        cls()

        exit()

while bptte:

    a = input("> ")

    if a == "help":

        print("getip    -- prints your current IP adress")
        print("cls      -- clears the screen")
        print("time     -- prints the current time")
        print("date     -- prints the date")
        print("datetime -- prints the time and date")
        print("getsys   -- prints your current OS")
        print("credits  -- prints the credits")
        print("exit     -- closes this instance of BPTTE\n")

    if a == "getip":

        ip()

    if a == "cls":

        cls()

    if a == "time":

        timed()

    if a == "date":

        date()

    if a == "datetime":

        datetime()

    if a == "getsys":

        getsys()

    if a == "credits":

        credits()

    if a == "exit":

        emes("Thanks for using The Basic Python Toolkit Terminal Environment\n")
