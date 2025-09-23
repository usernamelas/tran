label makeCoffeeOffice:
    if DeskEventOne == True:
        if CoffeeQuest == 0:
            $ isActivePlace = 13
            jump jeremymakeCoffee
        elif CoffeeQuest == 1:
            $ isActivePlace = 13
            hide screen disableClick
            scene open office day 1 without anna
            a "{i}...I already made some coffee for Jeremy..."
            jump annasOffice
    else:
        $ isActivePlace = 13
        hide screen disableClick
        scene open office day 1 without anna
        a "{i}...I don't want coffee right now..."
        jump annasOffice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
