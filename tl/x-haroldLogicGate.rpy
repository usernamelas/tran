label HaroldEventOne:
    show screen HospitalScreen
    $ sceneIsActive.ShowScreens()
    if (HospitalQuestOne == 3):
        hide screen HospitalScreen
        jump HaroldEventOneTwo
    elif HospitalQuestOne == 5:
        if ConvincedHarold == True:
            hide screen disableClick
            scene 29-14 hospital corridor
            "Thanks to Harold I was able to get what I needed."
            jump hospitalScreen
            return
        else:
            hide screen disableClick
            scene 29-14 hospital corridor
            "I don't need to talk to Harold right now."
            jump hospitalScreen
            return
    else:
        hide screen disableClick
        scene 29-14 hospital corridor
        "I don't have time to talk with him right now."
        jump hospitalScreen
        return
label HaroldEventOneTwo:
    $ isActivePlace = 0
    hide screen disableClick
    $ sceneIsActive.HideScreens()
    if haroldconvohappen == True:
        jump HaroldEventOneTwoOne
    else:
        jump HaroldEventOneTwoTwo
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
