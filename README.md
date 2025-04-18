# How to use the color functions

You have to go to https://pypi.org/project/colorama/ to download the colorama package, unzip the file, and move the colorama file to the same directory as the sdk.py file.

# Current functions

1. Basic math
  - Provides an easy way to add, subtract, divide, and multiply 2 numbers.

2. Highlighted text
  - Using the hiw() function, you can print highlighted text for stuff like menus.

3. Screen clearing
  - Using the cls() function you can clear the screen on both Windows and Unix-like operating systems.

4. Waiting a set amount of seconds
  - Use the wait() function to wait a certain amount of seconds, specified inbetween the parenthesis.

5. Printing the OS using getsys()

  - When you call the getsys() function, it will print the OS name, if you aren't on Windows it will print 'Unix-like'.

6. Printing the credits

  - When you call credits() it will print the BPT version alongside with my name.

7. Getting the date

  - You can print the current date with the date() function in: wday, month day year style.

8. Getting the time

  - To print the time in AM PM 12h plus seconds use the timed() function.

9. Getting both time and date

  - Use the timedate() function to print both time and date together

10. Exit messages

  - To set an exit message you can use emes() to set one, and call it when you want to close the program.

# Patch-notes

1.4.1 - Removed some unnecessary imports

1.4.0 - Switch functions from `print()` to `return`. Removed `getip()`

1.3.0 - Added emes() and a terminal environment

1.2.0 - Added timed(), date(), timedate(), and ip()

1.1.0 - Added wait(), getsys(), and credits() 

1.0.0 - Release
