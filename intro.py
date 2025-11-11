from tools import *


# -- Intro -- #

def boot_up_sequence()->None: # First part of the intro

    # -- Boot Up Sequence -- #

    
    typing_animation("BOOT UP SEQUENCE...",newline=False)
    time.sleep(1)
    deleting(3)
    typing_animation(" READY")

    print()

    time.sleep(1)

    
    typing_animation("FIRMWARE...",newline=False)
    time.sleep(1)
    deleting(3)
    print("   ")
    typing_animation("  LATEST VERSION (2112.08.06)",color="green")

    time.sleep(1)

    typing_animation("CALIBRATION...",newline=False)
    time.sleep(1)
    deleting(3)
    print("   ")
    typing_animation("  RECENTLY UPTADED",color="green")

    print()

def status_update()->None: # Second part of the intro

    typing_animation("STATUS UPDATE:")
    time.sleep(1)

    print()

    typing_animation("MACHINE ID:",newline=False) ; time.sleep(1) ; print("           ",end="") ; typing_animation("V1",0.5)

    time.sleep(1)

    typing_animation("LOCATION:",newline=False) ; time.sleep(1) ; print("             ",end="") ; typing_animation("APPROACHING HELL")

    time.sleep(1)
 
    typing_animation("CURRENT OBJECTIVE:",newline=False) ; time.sleep(1) ; print("    ",end="") ; typing_animation("FIND A WEAPON")

    print()

def final_lines()->None: # Final part of the intro

    typing_animation("MANKIND IS DEAD.",color="red")
    time.sleep(1)
    typing_animation("BLOOD IS FUEL.",color="red")
    time.sleep(1)
    typing_animation("HELL IS FULL.",color="red")

def ultrakill_intro()->None: # All in one

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

    print("\033[?25l")

# -- Test Side -- #

ultrakill_intro() 

