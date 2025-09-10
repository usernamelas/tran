

init python:

    tg = Gallery()

    tg.locked_button = "locked.png"

    tg.button("gallery_57")
    tg.image("ssm")
    tg.condition("persistent.unlock_57")

    tg.button("gallery_58")
    tg.image("mlbg_g") 
    tg.condition("persistent.unlock_58")   

    tg.button("gallery_59")
    tg.image("bbm23") 
    tg.condition("persistent.unlock_59")

    tg.button("gallery_60")
    tg.image("ddt") 
    tg.condition("persistent.unlock_60")

    tg.button("gallery_61")
    tg.image("eljen8") 
    tg.condition("persistent.unlock_61")

    tg.button("gallery_62")
    tg.image("sdnv") 
    tg.condition("persistent.unlock_62")

    tg.button("gallery_63")
    tg.image("neist22") 
    tg.condition("persistent.unlock_63")




    tg.transition = dissolve


screen gallery8:
    tag menu




    add "gallerymenu8"


    grid 4 2:

        xfill True
        yfill True


        add tg.make_button("gallery_57", "jopen12_tn.png", xalign=0.5, yalign=0.5)
        add tg.make_button("gallery_58", "mlbg_tn.png", xalign=0.5, yalign=0.5)
        add tg.make_button("gallery_59", "bbm23_tn.png", xalign=0.5, yalign=0.5)
        add tg.make_button("gallery_60", "ddt108_tn.png", xalign=0.5, yalign=0.5)
        add tg.make_button("gallery_61", "eljen8_tn.png", xalign=0.5, yalign=0.5)
        add tg.make_button("gallery_62", "sdayclea97_tn.png", xalign=0.5, yalign=0.5)
        add tg.make_button("gallery_63", "neist22_tn.png", xalign=0.5, yalign=0.5)



        textbutton "Return" action Return() xalign 0.5 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
