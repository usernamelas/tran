label SexShopLogicGate:
    show screen ShoppingScreen
    if Emily_Sexshop_Quest == True:
        if Emily_Sexshop_Quest_Done == False:
            hide screen ShoppingScreen
            jump SexShopEventOne
        else:
            jump SexShopLabel
    else:
        "This is Local Sex Shop."
        jump shoppingStreet
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
