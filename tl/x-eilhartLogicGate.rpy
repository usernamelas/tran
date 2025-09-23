label hospitalEilhart:
    hide screen disableClick
    show screen HospitalScreen
    if DayThreeVariable == True:
        if GoodBadDoctorChoice == 1:
            if HospitalEventTwo == False:
                jump EilhartEvenTwo
            else:
                $ isActivePlace = 15
                "I don't need to go there right now."
                jump hospitalScreen
    if GoodBadDoctorChoice == 0:
        $ isActivePlace = 15
        menu:
            "I'd better work with Dr. Eilhart.":
                $ GoodBadDoctorChoice = 1
                jump hospitalEilhartOne
            "I haven't decided yet.":
                jump hospitalScreen
    elif GoodBadDoctorChoice == 1:
        if HospitalQuestOne == 5:
            jump hospitalEilhartTwo
        elif HospitalQuestOne == 6:
            $ isActivePlace = 15
            "I have done all I could with Dr. Eilhart Now I have to wait."
            jump hospitalScreen
        else:
            $ isActivePlace = 15
            "I don't need to go there right now."
            jump hospitalScreen
    elif GoodBadDoctorChoice == 2:
        $ isActivePlace = 15
        "I've made my choice."
        jump hospitalScreen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
