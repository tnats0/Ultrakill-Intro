# -- Modules -- #

import os
import sys
import time
import random

from rich.console import *
from rich.theme import *
from rich.panel import *
from rich.live import *
from rich.text import *


from colorama import *

init(autoreset=True)

# -- Variables and Iterables -- #


console = Console(highlight=False,color_system="windows")

red = "Bold Red"

green = "Bold Green"

white = "Bold White"


colors:dict = {

"white":white,
"green": green,
"red": red,

}


# -- Functions -- #

def generate_letter():

    letter = chr(random.randint(65,122))

    return letter

def cool_type(input_text:str,color)->None:  # Function to print with animation.

    with Live(generate_letter(),refresh_per_second=40) as live:

        count = 0
        real_count = 0

        while real_count < len(input_text):

                real_count += 1
                count = 0

                while count <= 10:

                    letters = []

                    text = ""

                    for i in range(len(input_text)):

                        if i < real_count:
                            letters.append(input_text[i])
                        else:
                            letters.append(generate_letter())

                    text = "".join(letters)

                    live.update(Text.from_markup(text,style=color))
                    time.sleep(0.05)
                    count += 1


def type(text:str,delay:float=0.05,color:str="white",newline:bool=True)->None:  # Function to print with animation.

    for letter in text:
        console.print(letter,style=colors[color],end="")
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


