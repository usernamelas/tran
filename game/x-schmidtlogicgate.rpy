label SchmidtEventOne:
    show screen HospitalScreen
    if DayFourVariable == True:
        if GoodBadDoctorChoice == 2:
            if HospitalEventThree == False:
                jump SchmidtEventThree
    if DayThreeVariable == True:
        if GoodBadDoctorChoice == 2:
            if HospitalEventTwo == False:
                jump SchmidtEvenThreeNotUsed
    if GoodBadDoctorChoice == 0:
        $ isActivePlace = 15
        menu:
            "I guess I will cooperate with Dr. Schmidt.":
                jump SchmidtEventTwo
                $ GoodBadDoctorChoice = 2
            "I haven't decided yet.":
                jump hospitalScreen
    elif GoodBadDoctorChoice == 1:
        if HospitalQuestOne == 2:
            jump hospitalEilhartOneTwo
        else:
            $ isActivePlace = 15
            hide screen disableClick
            "I've made my choice."
            jump hospitalScreen
    elif GoodBadDoctorChoice == 2:
        $ isActivePlace = 15
        hide screen disableClick
        "I have nothing to do there right now."
        jump hospitalScreen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
