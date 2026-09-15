from funcs import *


# -- Intro -- #

def boot_up_sequence(): 

    # -- Boot Up Sequence -- #

    
    cool_type("BOOT UP SEQUENCE...",newline=False)
    time.sleep(1)
    deleting(3)
    type(" READY")

    print()

    time.sleep(1)

    
    type("FIRMWARE...",newline=False)
    time.sleep(1)
    deleting(3)
    print("   ")
    type("  LATEST VERSION (2112.08.06)",color="green")

    time.sleep(1)

    type("CALIBRATION...",newline=False)
    time.sleep(1)
    deleting(3)
    print("   ")
    type("  RECENTLY UPTADED",color="green")

    print()

def status_update(): # Second part of the intro

    type("STATUS UPDATE:")
    time.sleep(1)

    print()

    type("MACHINE ID:",newline=False) ; time.sleep(1) ; print("           ",end="") ; type("V1",0.5)

    time.sleep(1)

    type("LOCATION:",newline=False) ; time.sleep(1) ; print("             ",end="") ; type("APPROACHING HELL")

    time.sleep(1)
 
    type("CURRENT OBJECTIVE:",newline=False) ; time.sleep(1) ; print("    ",end="") ; type("FIND A WEAPON")

    print()

def final_lines(): # Final part of the intro

    cool_type("MANKIND IS DEAD.",colors["red"])
    time.sleep(1)
    cool_type("BLOOD IS FUEL.",colors["red"])
    time.sleep(1)
    cool_type("HELL IS FULL.",colors["red"])

def ultrakill_intro(): # All in one

    print("\033[?25l")

    clear()

    time.sleep(1)

    boot_up_sequence()

    time.sleep(1)

    clear()

    status_update()

    time.sleep(1)

    final_lines()

    time.sleep(5)

    print("\033[?25h")

# -- Test Side -- #

final_lines()