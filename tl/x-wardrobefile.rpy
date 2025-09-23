label wardrobeone:
    hide screen disableClick
    show screen bedroomScreen
    if red_outfit == True:
        "I have the outfit I want right now."
        jump bedroom
    if DayThreeVariable == True:
        if pinkoutfit == False:
            hide screen bedroomScreen
            $ sceneIsActive.HideScreens()
            scene black
            play sound undress
            scene 31-1 morning 16 with Dissolve(1)
            "Anna puts on her daily outfit and makes her hair."
            $ sceneIsActive.ShowScreens()
            $ pinkoutfit = True
            jump bedroom
    if annafirsttimehome == False:
        a "{i}...All I need to take a shower is my towel and it's already in the bathroom..."
        jump bedroom
    if annafirsttimesleep == False:
        scene home bedroom evening 2 anna bathrobe
        a "{i}...I should just go to sleep."
        jump bedroom
    if (annafirsttimesleep == True) and (pinkoutfit == False):
        if (calendar.TimeOfDay == 0) or (calendar.TimeOfDay == 1):
            hide screen bedroomScreen
            $ sceneIsActive.HideScreens()
            scene home bedroom morning day 1
            a "{i}...I wonder what I could wear today..."
            scene 30-1 morning 1 with Dissolve(1)
            play sound equipsound
            a "{i}...This is a good choice, I have to keep up my appearances. Cannot look like I've been through something lately..."
            a "{i}...It looks great. I love it..."
            scene 30-1 morning 2 with Dissolve(1)
            a "{i}...Looking at it makes me feel a bit better. It's also comfortable, so there is that..."
            a "{i}...And it's just a tiny bit naughty, the way I like it..."
            $ sceneIsActive.ShowScreens()
            $ pinkoutfit = True
            jump bedroom
        elif calendar.TimeOfDay == 2:
            show screen bedroomScreen
            a "{i}...Maybe I should get into something more comfortable?..."
            jump bedroom
    if annafirsttimesleep == True:
        if (calendar.TimeOfDay == 0) or (calendar.TimeOfDay == 1):
            show screen bedroomScreen
            a "{i}...I should check through my clothes at some point..."
            jump bedroom
        elif calendar.TimeOfDay == 2:
            if AlfredEvent == 1:
                hide screen bedroomScreen
                jump AlfredEvening
            show screen bedroomScreen
            a "{i}...Maybe I should get into something more comfortable?..."
            jump bedroom
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
