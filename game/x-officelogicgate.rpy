label emilyChangeRoom:
    if changingRoomDone == True:
        if officeOneDone == 2:
            if officeoutfit == True:
                if jeremySexContent == True:
                    if FirstTimeTakeOutVibrator == False:
                        $ sceneIsActive.HideScreens()
                        hide screen disableClick
                        hide screen characterScreen
                        scene black
                        scene 30-8 changing 1 with Dissolve(1)
                        "After the events that occured today, Anna was in a rush to remove the device from her pussy."
                        "It felt really uncomfortable, but she had to do it if she wanted to get up the corporate ladder."
                        a "{i}...What am I doing... Ugh... Focus, Anna."
                        "She wondered for a moment and finaly sat down to remove the device."
                        scene 30-8 changing 2 with Dissolve(1)
                        "She felt the device inside of her most of the time, it wasn't as unpleasant as she had expected."
                        "But she still felt degraded after Jeremy almost forcibly put it in."
                        "But as mentioned before, she had to do it to win his good graces."
                        "Anna touched her pussy and already was extra sensitive."
                        scene black with Dissolve(1)
                        play sound undress
                        "Anna removed the device..."
                        scene 30-8 changing 3 with Dissolve(1)
                        "She pulled out the device and looked at it for a moment."
                        "It was a simple vibrator with a remote somewhere in Jeremy's office."
                        "She wasn't exactly looking forward to what he will do with it."
                        "But for now she thought that she will play along and put it in everytime she arrives at work."
                        scene black with Dissolve(1)
                        play sound undress
                        scene 30-8 changing 4 with Dissolve(1)
                        "Anna changed in to her daily clothes and put away the vibrator."
                        a "{i}...I hope one comes looking through my things and finds this..."
                        a "{i}...Time to get to my other duties..."
                        a "{i}...Atleast that vibrator is not in my for now..."
                        $ officeoutfit = False
                        $ pinkoutfit = True
                        $ FirstTimeTakeOutVibrator = True
                        jump officeReception
                    else:
                        $ sceneIsActive.HideScreens()
                        hide screen disableClick
                        hide screen characterScreen
                        scene black
                        play sound equipsound
                        scene 30-8 changing 2-1 with Dissolve(1)
                        "Anna changed into her everyday clothes and took out the vibrator."
                        $ officeoutfit = False
                        if DayFiveVariable == False:
                            $ pinkoutfit = True
                        else:
                            $ red_outfit = True
                        jump officeReception
                else:

                    $ sceneIsActive.HideScreens()
                    hide screen disableClick
                    hide screen characterScreen
                    scene black
                    play sound equipsound
                    pause 1.5
                    "Anna changed into her everyday clothes."
                    $ officeoutfit = False
                    if DayFiveVariable == False:
                        $ pinkoutfit = True
                    else:
                        $ red_outfit = True
                    jump officeReception
            else:
                if FirstTimeTakeOutVibrator == True:
                    $ sceneIsActive.HideScreens()
                    hide screen disableClick
                    hide screen characterScreen
                    scene black
                    play sound equipsound
                    scene 30-8 changing 2-1 with Dissolve(1)
                    "Anna changed into her office outfit and Put in Jeremy's vibrator."
                    $ officeoutfit = True
                    if DayFiveVariable == False:
                        $ pinkoutfit = False
                    else:
                        $ red_outfit = False
                    jump officeReception
                else:
                    hide screen disableClick
                    hide screen characterScreen
                    scene black
                    play sound equipsound
                    pause 1.5
                    "Anna changed into her office outfit."
                    $ officeoutfit = True
                    if DayFiveVariable == False:
                        $ pinkoutfit = False
                    else:
                        $ red_outfit = False
                    jump officeReception
        else:
            hide screen disableClick
            scene 30-2 office annas reception
            "I already went there."
            jump officeReception
    else:

        jump EmilyChangingRoomEvent
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
