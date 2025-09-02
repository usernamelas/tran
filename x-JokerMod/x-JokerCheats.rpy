screen cheatmodnavigation():
    modal True
    add "#000"
    add Transform("JokerMod/Images/game_menu.png", zoom=1.00) alpha 0.90 xalign 0.5 yalign 0.5
    text "{size=80}Joker's Cheat Mod" color "#f3c26a" font "JokerMod/Bebas-Regular.otf" xcenter 0.5 ypos 15 outlines [(5, "#000", 0, 10)]

    textbutton "{size=50}Return{/size}" action Return() xalign 0.1 yalign 0.9

screen cheatmod():
    tag menu
    use cheatmodnavigation
    vpgrid:
        xcenter 0.5
        ypos 150
        cols 4
        xspacing 100
        yspacing 50
        vbox:
            spacing 30
            text "{size=50}{color=#f3c26a}Charlotte{/color=#f00}" font "JokerMod/Bebas-Regular.otf" ycenter 0.8 outlines [(2, "#000", 0, 3)]
            fixed:
                xysize (400,40)
                bar value VariableValue("charlotte_rel", 100)
                text "{size=40}{color=#ffffff}[charlotte_rel]{/color=#f00}" font "JokerMod/Bebas-Regular.otf" xcenter 0.5 ycenter 0.45 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 30
            text "{size=50}{color=#f3c26a}Darlene{/color=#f00}" font "JokerMod/Bebas-Regular.otf" ycenter 0.8 outlines [(2, "#000", 0, 3)]
            fixed:
                xysize (400,40)
                bar value VariableValue("darlene_rel", 100)
                text "{size=40}{color=#ffffff}[darlene_rel]{/color=#f00}" font "JokerMod/Bebas-Regular.otf" xcenter 0.5 ycenter 0.45 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 30
            text "{size=50}{color=#f3c26a}Emma{/color=#000}" font "JokerMod/Bebas-Regular.otf" ycenter 0.8 outlines [(2, "#000", 0, 3)]
            fixed:
                xysize (400,40)
                bar value VariableValue("emma_rel", 100)
                text "{size=40}{color=#ffffff}[emma_rel]{/color=#f00}" font "JokerMod/Bebas-Regular.otf" xcenter 0.5 ycenter 0.45 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 30
            text "{size=50}{color=#f3c26a}Katrina{/color=#000}" font "JokerMod/Bebas-Regular.otf" ycenter 0.8 outlines [(2, "#000", 0, 3)]
            fixed:
                xysize (400,40)
                bar value VariableValue("katrina_rel", 100)
                text "{size=40}{color=#ffffff}[katrina_rel]{/color=#f00}" font "JokerMod/Bebas-Regular.otf" xcenter 0.5 ycenter 0.45 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 30
            text "{size=50}{color=#f3c26a}Lauren{/color=#000}" font "JokerMod/Bebas-Regular.otf" ycenter 0.8 outlines [(2, "#000", 0, 3)]
            fixed:
                xysize (400,40)
                bar value VariableValue("lauren_rel", 100)
                text "{size=40}{color=#ffffff}[lauren_rel]{/color=#f00}" font "JokerMod/Bebas-Regular.otf" xcenter 0.5 ycenter 0.45 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 30
            text "{size=50}{color=#f3c26a}Lisa{/color=#000}" font "JokerMod/Bebas-Regular.otf" ycenter 0.8 outlines [(2, "#000", 0, 3)]
            fixed:
                xysize (400,40)
                bar value VariableValue("lisa_rel", 100)
                text "{size=40}{color=#ffffff}[lisa_rel]{/color=#f00}" font "JokerMod/Bebas-Regular.otf" xcenter 0.5 ycenter 0.45 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 30
            text "{size=50}{color=#f3c26a}Triss{/color=#000}" font "JokerMod/Bebas-Regular.otf" ycenter 0.8 outlines [(2, "#000", 0, 3)]
            fixed:
                xysize (400,40)
                bar value VariableValue("patricia_rel", 100)
                text "{size=40}{color=#ffffff}[patricia_rel]{/color=#f00}" font "JokerMod/Bebas-Regular.otf" xcenter 0.5 ycenter 0.45 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 30
            text "{size=50}{color=#f3c26a}Sheila{/color=#000}" font "JokerMod/Bebas-Regular.otf" ycenter 0.8 outlines [(2, "#000", 0, 3)]
            fixed:
                xysize (400,40)
                bar value VariableValue("sheila_rel", 100)
                text "{size=40}{color=#ffffff}[sheila_rel]{/color=#f00}" font "JokerMod/Bebas-Regular.otf" xcenter 0.5 ycenter 0.45 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 30
            text "{size=50}{color=#f3c26a}Beatrice{/color=#000}" font "JokerMod/Bebas-Regular.otf" ycenter 0.8 outlines [(2, "#000", 0, 3)]
            fixed:
                xysize (400,40)
                bar value VariableValue("beatrice_rel", 100)
                text "{size=40}{color=#ffffff}[beatrice_rel]{/color=#f00}" font "JokerMod/Bebas-Regular.otf" xcenter 0.5 ycenter 0.45 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 30
            text "{size=50}{color=#f3c26a}Denise{/color=#000}" font "JokerMod/Bebas-Regular.otf" ycenter 0.8 outlines [(2, "#000", 0, 3)]
            fixed:
                xysize (400,40)
                bar value VariableValue("denise_rel", 100)
                text "{size=40}{color=#ffffff}[denise_rel]{/color=#f00}" font "JokerMod/Bebas-Regular.otf" xcenter 0.5 ycenter 0.45 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 30
            text "{size=50}{color=#f3c26a}Denise Mistakes{/color=#000}" font "JokerMod/Bebas-Regular.otf" ycenter 0.8 outlines [(2, "#000", 0, 3)]
            fixed:
                xysize (400,40)
                bar value VariableValue("denise_mistakes", 100)
                text "{size=40}{color=#ffffff}[denise_mistakes]{/color=#f00}" font "JokerMod/Bebas-Regular.otf" xcenter 0.5 ycenter 0.45 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 30
            text "{size=50}{color=#f3c26a}Kayla{/color=#000}" font "JokerMod/Bebas-Regular.otf" ycenter 0.8 outlines [(2, "#000", 0, 3)]
            fixed:
                xysize (400,40)
                bar value VariableValue("kayla_rel", 100)
                text "{size=40}{color=#ffffff}[kayla_rel]{/color=#f00}" font "JokerMod/Bebas-Regular.otf" xcenter 0.5 ycenter 0.45 outlines [(2, "#000", 0, 2)]

        vbox:
            spacing 30
            text "{size=50}{color=#f3c26a}Erwin{/color=#000}" font "JokerMod/Bebas-Regular.otf" ycenter 0.8 outlines [(2, "#000", 0, 3)]
            fixed:
                xysize (400,40)
                bar value VariableValue("erwin_rel", 100)
                text "{size=40}{color=#ffffff}[erwin_rel]{/color=#f00}" font "JokerMod/Bebas-Regular.otf" xcenter 0.5 ycenter 0.45 outlines [(2, "#000", 0, 2)]

    imagebutton:
        align (1.0,1.0)
        idle Transform("JokerMod/Images/Patreon_Button.png", zoom=0.6)
        hover Transform("JokerMod/images/Patreon_Button_Hover.png", zoom=0.6)
        action OpenURL("https://www.patreon.com/JokerLeader")
    imagebutton:
        align (1.0,0.89)
        idle Transform("JokerMod/Images/Coffee_Button.png", zoom=0.6)
        hover Transform("JokerMod/images/Coffee_Button_Hover.png", zoom=0.6)
        action OpenURL("https://www.buymeacoffee.com/JokerLeader")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
