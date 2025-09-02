screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback() text_size 15

            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True) text_size 15
            textbutton _("Auto") action Preference("auto-forward", "toggle") text_size 15
            textbutton _("Save") action ShowMenu('save') text_size 15
            textbutton _("Q.Save") action QuickSave() text_size 15
            textbutton _("Q.Load") action QuickLoad() text_size 15
            textbutton _("Opts") action ShowMenu('preferences') text_size 15

    hbox:
        style_prefix "quick"
        xalign 1.0
        yalign 1.0
        textbutton "Cheats" action ShowMenu("cheatmod")




init python:
    config.overlay_screens.append("quick_menu")

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


screen navigation():

    style_prefix "navigation"

    frame xsize 1920 ysize 96 yalign 1.0:
        has hbox
        xalign 0.5 yalign 0.5
        spacing 32
        ysize 30

        if _in_replay:

            textbutton _("END REPLAY") action EndReplay(confirm=True)
            add "gui/separator.png" yalign 0.5

        elif not main_menu:

            textbutton _("MAIN MENU") action MainMenu()
            add "gui/separator.png" yalign 0.5

        if main_menu:

            textbutton _("NEW GAME") action Start()
            add "gui/separator.png" yalign 0.5

        else:

            textbutton _("SAVE GAME") action ShowMenu("save")
            add "gui/separator.png" yalign 0.5

        textbutton _("LOAD GAME") action ShowMenu("load")
        add "gui/separator.png" yalign 0.5

        textbutton _("ACHIEVEMENTS") action ShowMenu("gallery")
        add "gui/separator.png" yalign 0.5

        if not _in_replay:
            textbutton _("MEMORIES") action ShowMenu("memories")
            add "gui/separator.png" yalign 0.5

        textbutton _("OPTIONS") action ShowMenu("preferences")
        add "gui/separator.png" yalign 0.5





        textbutton _("CREDITS") action ShowMenu("credits")
        add "gui/separator.png" yalign 0.5

        if renpy.variant("pc"):
            textbutton _("QUIT") action Quit(confirm=not main_menu)


    text "{size=50}Joker's Mod Installed" color "#f3c26a" xcenter 0.790 ypos 0.067 font "JokerMod/Montserrat-Light.ttf" outlines [(2, "#000", 0, 2)]

    imagebutton:
        align (0.750,0.011)
        idle Transform("JokerMod/Images/Cheats/Button_Patreon.png", zoom=0.8)
        hover Transform("JokerMod/Images/Cheats/Button_Patreon_2.png", zoom=0.8)
        action OpenURL("https://www.patreon.com/JokerLeader")
    imagebutton:
        align (0.920,0.011)
        idle Transform("JokerMod/Images/Cheats/Button_Coffee.png", zoom=0.8)
        hover Transform("JokerMod/Images/Cheats/Button_Coffee_2.png", zoom=0.8)
        action OpenURL("https://www.buymeacoffee.com/JokerLeader")


style navigation_button_text is gui_button_text
style navigation_button_text:
    size gui.menu_button_size
    font gui.text_font_bold
    yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
