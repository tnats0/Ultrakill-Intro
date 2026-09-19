from funcs import *



# -- Intro -- #

def boot_up_sequence(): 

    # -- Boot Up Sequence -- #

    t1 = Text("BOOT UP SEQUENCE...",style=styles["default"])
    t2 = Text("READY",styles["green"]); t2_1 = Text("READY",styles["red-s"]) 
    t3 = Text("FIRMWARE...",styles["default"])
    t4 = Text("  LATEST VERSION (2112.08.06)",styles["green"])
    t5 = Text("CALIBRATION...",styles["default"])
    t6 = Text("  RECENTLY UPTADED",styles["green"])

    
    type(t1,newline=False)
    time.sleep(1)
    deleting(3)
    console.print(" ",end="")
    glitch_type(t2,t2_1,type)

    print()

    time.sleep(1)

    
    type(t3,newline=False)
    time.sleep(1)
    deleting(3)
    print("   ")
    type(t4)

    time.sleep(1)

    type(t5,newline=False)
    time.sleep(1)
    deleting(3)
    print("   ")
    type(t6)

    print()

def status_update(): # Second part of the intro

    t1 = Text("STATUS UPDATE:",style=styles["default"])

    t2 = Text("MACHINE ID:",style=styles["default"])

    t3 = Text("V1",style=styles["default"]); t3_1 = Text("V1",style=styles["red-u"])

    t4 = Text("LOCATION:",style=styles["default"])

    t5 = Text("APPROACHING HELL",style=styles["default"]); t5_1 = Text("? ? ?",style=styles["red"])

    t6 = Text("CURRENT OBJECTIVE:",style=styles["default"])

    t7 = Text("FIND A WEAPON",style=styles["default"]); t7_2 = Text("F E E D  I T",style=styles["red"])



    type(t1)
    time.sleep(1)

    print()

    type(t2,newline=False) ; time.sleep(1) ; print("           ",end="") ; glitch_type(t3,t3_1,type)

    time.sleep(1)

    type(t4,newline=False) ; time.sleep(1) ; print("             ",end="") ; glitch_type(t5,t5_1,type)

    time.sleep(1)
 
    type(t6,newline=False) ; time.sleep(1) ; print("    ",end="") ; glitch_type(t7,t7_2,type,True)

    print()

def final_lines(): # Final part of the intro

    lines = [Text("MANKIND IS DEAD.",styles["red-u"]),Text("BLOOD IS FUEL.",styles["red-u"]),Text("HELL IS FULL.",styles["red-u"])]

    for line in lines:

        cool_type(line)
        time.sleep(1)


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

ultrakill_intro()