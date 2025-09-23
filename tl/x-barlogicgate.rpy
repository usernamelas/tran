label BarLogicGate:
    if bar_event_1 == True and bar_var_4 == False:
        jump BarEventOne
    else:
        jump industrialStreet

label toBarArea:
    hide screen disableClick
    if bar_var_3 == False:
        show screen BarOfficeScreen
        "Should talk to Patrick."
        jump barOfficeScreen
    else:
        jump barScreen

label barOfficeScreen:
    show screen disableClick
    $ sceneIsActive.ShowScreens()
    $ isActivePlace = 55
    show screen collectiblesScreen
    show screen characterScreen
    call screen BarOfficeScreen
    pause
    return

label barScreen:
    show screen disableClick
    $ sceneIsActive.ShowScreens()
    $ isActivePlace = 56
    show screen collectiblesScreen
    call screen BarScreen
    pause
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
