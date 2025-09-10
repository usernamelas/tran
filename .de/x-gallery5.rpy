

init python:

    cp = Gallery()

    cp.locked_button = "locked.png" 

    cp.button("gallery_36")
    cp.image("cinejen4")
    cp.condition("persistent.unlock_36")

    cp.button("gallery_37")
    cp.image("mphotoshoot18")
    cp.condition("persistent.unlock_37")

    cp.button("gallery_38")
    cp.image("cbl22")
    cp.condition("persistent.unlock_38")

    cp.button("gallery_39")
    cp.image("bwaits7") 
    cp.condition("persistent.unlock_39")   

    cp.button("gallery_40")
    cp.image("ehelpgal") 
    cp.condition("persistent.unlock_40")

    cp.button("gallery_41")
    cp.image("cinenadjen12")
    cp.condition("persistent.unlock_41")

    cp.button("gallery_42")
    cp.image("ehelp7")
    cp.condition("persistent.unlock_42")

    cp.transition = dissolve


screen gallery5:
    tag menu




    add "gallerymenu5"


    grid 4 2:

        xfill True
        yfill True


        add cp.make_button("gallery_36", "cinejen4_tn.png", xalign=0.5, yalign=0.5)
        add cp.make_button("gallery_37", "mphotoshoot18_tn.png", xalign=0.5, yalign=0.5)
        add cp.make_button("gallery_38", "cbl22_tn.png", xalign=0.5, yalign=0.5)
        add cp.make_button("gallery_39", "bwaits7_tn.png", xalign=0.5, yalign=0.5)
        add cp.make_button("gallery_40", "ehelp1_tn.png", xalign=0.5, yalign=0.5)
        add cp.make_button("gallery_41", "cinenadjen4_tn.png", xalign=0.5, yalign=0.5)
        add cp.make_button("gallery_42", "ehelp4_tn.png", xalign=0.5, yalign=0.5)





        textbutton "Return" action Return() xalign 0.5 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
