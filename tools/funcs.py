# -- Modules -- #

import os
import sys
import time

from colorama import *

init(autoreset=True)

# -- Variables and Iterables -- #

colors:dict = {

"white":Fore.WHITE,
"blue": Fore.BLUE,
"green": Fore.GREEN,
"red": Fore.RED,
"yellow": Fore.YELLOW,
"magenta":Fore.MAGENTA,
"cyan": Fore.CYAN,
"lgreen": Fore.LIGHTGREEN_EX,
"lblue": Fore.LIGHTBLUE_EX,
"lred": Fore.LIGHTRED_EX,
"lblack": Fore.LIGHTBLACK_EX,
"lmagenta": Fore.LIGHTMAGENTA_EX,
"lcyan": Fore.LIGHTCYAN_EX

}


# -- Functions -- #

def type(text:str,delay:float=0.05,color:str="white",newline:bool=True)->None:  # Function to print with animation.

    for letter in text:
        print(f"{colors[color] + letter}",end="")
        time.sleep(delay)

    if newline: print("\n",end="")

def deleting(charNum:int)->None:    # Function to delete a specified number of characters from the console output
    
    print(charNum*"\b",end="")  # Move the cursor back by charNum positions using backspace characters
    print(charNum*" ",end="")   # Overwrite the characters with spaces to clear them from the display
    print(charNum*"\b",end="")  # Move the cursor back again to the original position after clearing
    sys.stdout.flush()          # Flush the output buffer to ensure the changes are displayed immediately

def clear()->None: # Function to clear the terminal
    
    if os.name == "nt":
        os.system("cls") # Windows
    else:
        os.system("clear") # Linux and Macos


