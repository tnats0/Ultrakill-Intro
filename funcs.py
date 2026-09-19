# -- Modules -- #

import os
import sys
import time
import random

from rich.console import *
from rich.theme import *
from rich.text import *

# -- Variables and Iterables -- #

console = Console(highlight=False,color_system="windows")


styles = {

    "green":"b Green",
    "red":"b Red",
    "red-u":"b Red u",
    "red-s":"b red s",
    "default":"b White",


}

# -- Functions -- #

def generate_text(charNum:int):

    text = ""

    for _ in range(charNum):
        letter = chr(random.randint(65,122))
        text += letter

    return text

def generate_glitch_string(length: int) -> str:
    chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/░▒▓█"
    return "".join(random.choice(chars) for _ in range(length))

def glitch_type(text1:Text,text2:Text,typing,newline:bool=True):

    typing(text1,newline=False)
    
    time.sleep(0.5)

    glitched_text = Text(generate_glitch_string(len(text1)),style="bold white on red")

    deleting(len(text1))

    console.print(glitched_text,end="")

    time.sleep(0.1)

    deleting(len(text1))

    console.print(text2,end="")

    if newline: console.print("")


def cool_type(input_text:Text,speed:int=5,newline:bool=True):

    real_count,count = 0,0

    while real_count < len(input_text):

        count = 0
        real_count += 1

        while count <= speed:

            deleting(len(input_text))

            text = input_text[0:real_count] + generate_text(len(input_text)-real_count)

            console.print(text,style=input_text.style,end="")
            time.sleep(0.05)

            count +=1

    if newline:console.print("")


def type(text:Text,delay:float=0.05,newline:bool=True)->None:  # Function to print with animation.

    for letter in text:
        console.print(letter,style=text.style,end="")
        time.sleep(delay)

    if newline: console.print("")


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

