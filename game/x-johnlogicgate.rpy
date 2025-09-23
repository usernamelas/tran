label JohnLogicGate:
    show screen homeScreen
    hide screen disableClick
    if DayFourVariable == True:
        if JohnAndrewHospitalQuest == False:
            hide screen homeScreen
            jump JohnEventThree
        else:
            $ isActivePlace = 1
            j "Hey, Anna. I'm deep in thought right now, can this wait?"
            jump livingroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
