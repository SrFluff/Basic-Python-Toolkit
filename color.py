try:
    from colorama import Fore as F
    from colorama import Back as B
except ImportError:
    print("You don't seem to have Colorama installed, refer to README.md for further instructions")
    exit()

def error(errorText="No error given"):
    print(F.RED + "ERROR: " + errorText + F.RESET)
def color(text="This is color text",col=0,ret=False):
    retu = ""
    if col == 0:
        retu = F.RED + text + F.RESET
    elif col == 1:
        retu = F.GREEN + text + F.RESET
    elif col == 2:
        retu = F.BLUE + text + F.RESET
    elif col == 3:
        retu = F.YELLOW + text + F.RESET
    elif col == 4:
        retu = F.CYAN + text + F.RESET
    elif col == 5:
        retu = F.MAGENTA + text + F.RESET
    if ret:
        return retu
    else:
        print(retu)
def hiw(text="No text",ret=False):
    if ret:
        return F.BLACK + B.WHITE + text + F.RESET + B.RESET
    else:
        print(F.BLACK + B.WHITE + text + F.RESET + B.RESET)
