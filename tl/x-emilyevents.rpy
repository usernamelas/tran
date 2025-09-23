label emilyofficenospeak:
    default FirstTimeOfficeEmilyTalk = False
    hide screen disableClick
    if CoffeeQuest == 2 or firstTimePartner == True:
        if FirstTimeOfficeEmilyTalk == False:
            hide screen characterScreen
            scene black
            scene 30-7 emilytalk 1 with Dissolve(1)
            a "Hey, Emily."
            e "Hey, sweety."
            a "I just came to say that I will be working from this office from now on."
            e "Yeah, I figured as much, when I saw them setting up your office."
            a "Maybe we can go grab a coffee a bit later?"
            e "I'd like to, but I have a lot to do today."
            scene 30-7 emilytalk 2 with Dissolve(1)
            a "Ah, no problem, Emily. Since I'm working from here now, it will be much easier to come to you and talk."
            e "Absolutely, dear."
            a "Anyway, I have to get to work, talk to you later?"
            e "Yeah, Anna. That would be great."
            e "Catch you later."
            $ FirstTimeOfficeEmilyTalk = True
            jump mainOffice
        else:
            scene openoffice 2 day 1 without people
            e "Hey, honey. I'm a bit busy right now, talk later?"
            jump mainOffice
    else:
        scene openoffice 2 day 1 without people
        e "Hey, honey. I'm a bit busy right now, talk later?"
        jump mainOffice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
