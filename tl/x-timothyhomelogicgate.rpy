label TimothyHomeLogicGate:
    show screen DowntownScreen
    if DayFourVariable == True and DayFiveVariable == False:
        if RebeccaGymQuestDone == True:
            if timothySexContent == True:
                if TimothyHomeEventOneDone == False:
                    hide screen DowntownScreen
                    jump TimothyHomeEventOne
                else:
                    "This is Timothy's place."
                    jump downtownStreet
            else:
                "This is Timothy's place."
                jump downtownStreet
        else:
            "This is Timothy's place."
            jump downtownStreet
    else:
        "This is Timothy's place."
        jump downtownStreet
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
