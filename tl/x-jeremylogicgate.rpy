label jeremyoffice:
    show screen disableClick
    if DayThreeVariable == True:
        if jeremySexContent == True:
            if JeremyEventTwoQuest == 1:
                jump JeremyEventTwoOne
            else:
                hide screen disableClick
                show screen officeScreen
                "I should get to work."
                jump officeReception
        else:
            if JeremyEventTwoQuest == 1:
                jump JeremyEventTwoNoSexTwo
            else:
                hide screen disableClick
                show screen officeScreen
                "I should get to work."
                jump officeReception
    if dianaGoodRelations == True:
        hide screen disableClick
        show screen officeScreen
        "Nothing to do in his office. Thank god he's gone."
        jump officeReception
    if officeoutfit == True:
        if DeskEventOne == True:
            if CoffeeQuest == 0:
                $ isActivePlace = 10
                hide screen disableClick
                scene 30-2 office annas reception
                a "{i}...I should get him his coffee and then discuss business..."
                jump officeReception
            elif CoffeeQuest == 1:
                jump JeremyEventOneTwo
            elif CoffeeQuest == 2:
                $ isActivePlace = 10
                hide screen disableClick
                scene 30-2 office annas reception
                a "{i}...I had the discussion in Jeremy's office already..."
                jump officeReception
        else:
            $ isActivePlace = 10
            hide screen disableClick
            scene 30-2 office annas reception
            a "{i}...I should get to work and not bother Jeremy..."
            jump officeReception
    else:
        $ isActivePlace = 10
        hide screen disableClick
        scene 30-2 office annas reception
        a "{i}...I should change clothes and not bother Jeremy like this..."
        jump officeReception
    pause
    return
label JeremyLogicGate:
    hide screen disableClick
    show screen DowntownTwoScreen
    if Jeremy_Home_Quest_One == True:
        if Jeremy_Home_Quest_One_Done == False:
            hide screen DowntownTwoScreen
            jump JeremyHomeEventOne
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
