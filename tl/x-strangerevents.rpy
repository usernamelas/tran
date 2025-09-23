label strangerEventOne:
    if HospitalQuestOne == 3 or HospitalQuestOne == 4:
        $ isActivePlace = 0
        hide screen disableClick
        $ sceneIsActive.HideScreens()
        hide screen characterScreen
        scene black
        scene 30-10 hospital 7 with Dissolve(1)
        a "You know what, I changed my mind. Let's do it."
        stranger "Did you now? Alright. Don't have to ask me twice."
        $ HospitalQuestOne = 5
        jump strangerBreakIn
    else:
        show screen HospitalScreen
        hide screen disableClick
        scene 29-14 hospital corridor
        $ sceneIsActive.ShowScreens()
        a "{i}...Probably some stranger... checking me out... As always."
        jump hospitalScreen
        return

label strangerBreakIn:
    stranger "Can you cover the door please so no one see what I'm doing."
    a "You actually know how to pick locks... ofcourse you do... For once things are rather easy."
    stranger "I make life easier... In many ways."
    a "Right, I bet you do."
    scene 30-10 hospital 8 with Dissolve(1)
    "The stranger went to the door and pulled out a set of pick locking tools."
    "He got to trying to unlock the door."
    "Meanwhile, Anna was thinking about how illegal this is."
    "But she needed to this to get rid of that doctor... From what she gathered from Cary, he was not exactly the good guy."
    "At the end of the day, it was for the greater good."
    "The stranger got the lock open in a matter of seconds."
    scene 30-10 hospital 9 with Dissolve(1)
    a "Wow... That was fast."
    stranger "I'm very good at what I do."
    stranger "The name's Miles by the way."
    $ stranger = Character("Miles")
    a "I'm Anna."
    stranger "Nice to meet you, Anna."
    stranger "Anyway, let's get in before anyone notices I will be in and out as quickly as possible."
    $ MilesBrokeIn = True
    scene black with Dissolve(1)
    jump DoctorsOffice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
