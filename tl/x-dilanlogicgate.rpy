label DilanLogicGate:
    show screen DowntownScreen
    hide screen disableClick
    if calendar.TimeOfDay == 1:
        if RebeccaGymQuestDone == True:
            if DilanPornShootQuestDone == False:
                hide screen DowntownScreen
                jump DilanEventTwo
    else:

        "This is Dilan's place"
        jump downtownStreet
    if OfficeDayThreeDone == False:
        "I should go to Dilan later."
        jump downtownStreet
    else:
        if DilanEventOneDone == False:
            hide screen DowntownScreen
            jump DilanEventOne
        else:
            "This is Dilans place."
            jump downtownStreet
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
