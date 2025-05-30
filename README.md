# Required libraries 

You have to install the **Colorama** & **Pygame** libraries through Pip, or your operating system's package manager.

# Current functions

1. Basic math
  - Provides an easy way to add, subtract, divide, and multiply 2 numbers.

2. Screen clearing
  - Using the `cls()` function you can clear the screen on both Windows and Unix-like operating systems.

3. Waiting a set amount of seconds
  - Use the `wait()` function to wait a certain amount of seconds, specified inbetween the parenthesis.

4. Printing the OS using getsys()

  - When you call the `getsys()` function, it will print the OS name, if you aren't on Windows it will print 'Unix-like'.

5. Printing the credits

  - When you call `credits()` it will print the BPT version alongside with my name.

6. Getting the date

  - You can print the current date with the `date()` function in: wday, month day year style.

7. Getting the time

  - To print the time in AM PM 12h plus seconds use the `timed()` function.

8. Getting both time and date

  - Use the `timedate()` function to print both time and date together.

9. Exit messages

  - To set an exit message you can use `emes()` to set one, and call it when you want to close the program.

10. Error message
  - `color.error()` prints a spoof error message. It needs Colorama by the way.

11. The terminal environment
  - Using `init()` you can start the Basic-Python-Toolkit Terminal Environment, where you can run some commands like `cls` and `error`.

12. Colored text
  - You can print(or **return** colored text using the `color.color()` function, the format goes as follows: `color(text-in-color,color(0-6),print-if-true(True/False))`

13. Warning window
  - You can draw a window with a warning message using the `warning()` function. This function does require **Pygame**

14. Version
  - The standard way to return the SDK version.

15. The music shell
  - To initialize the shell you can run the `music.shell()` function. From here run `help` for a list of commands.

16. The music library
  - Inside `sdk.py` there's a library called `music` in here you have `play()`,`load()`,`unload()`,`volume()`,`stop()`,`pause()`,and `unpause()`. If  you're importing `sdk.py` you can run these functions like this: `sdk.music.<function>`.

17. Json parsing
  - To return a specific vriable from a json file run `parse(filename,variable)`

# Patch-notes

1.17.4 - Added the `parse()` function.

1.16.4 - Edited `color.error()`'s formatting a bit.

1.16.3 - Removed `color.hiw()` added highlighting to `color.color()`.

1.15.3 - Added `music` to the BPTTE and cleaned up comments.

1.14.3 - Moved `error()`, `hiw()`, and `color()` into `color.py`.

1.13.3 - Added the `ok` button to `warning()`.

1.12.3 - Moved the music shell into `music.py` and added music functions like `play()` and `pause()`.

1.11.3 - Added `load` and `unload` to the music shell.

1.11.2 - Added `wait()` and `version()` to the BPTTE.

1.10.2 - Added the `musicLoop()` function.

1.9.2 - Added the `version()` command, moved `import pygame` inside `def warning()`.

1.8.2 - Added the `warning()` function.

1.7.2 - Removed init() from the last line.

1.7.1 - Added the `color()` function. Might eventually remove `hiw()`.

1.6.1 - Minor spelling fixes & reimplemented the BPTTE, now uses a function instead of a variable.

1.5.1 - Actually removed all text referring to the `ip()` function, and added the `error` function

1.4.1 - Removed some unnecessary imports

1.4.0 - Switch functions from `print()` to `return`. Removed `getip()`

1.3.0 - Added emes() and a terminal environment

1.2.0 - Added timed(), date(), timedate(), and ip()

1.1.0 - Added wait(), getsys(), and credits() 

1.0.0 - Release
