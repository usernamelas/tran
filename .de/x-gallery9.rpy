

init python:

    tk = Gallery()

    tk.locked_button = "locked.png"

    tk.button("gallery_64")
    tk.image("bwr10")
    tk.condition("persistent.unlock_64")

    tk.button("gallery_65")
    tk.image("melwrk29") 
    tk.condition("persistent.unlock_65")   

    tk.button("gallery_66")
    tk.image("msusp14") 
    tk.condition("persistent.unlock_66")

    tk.button("gallery_67")
    tk.image("rdana") 
    tk.condition("persistent.unlock_67")

    tk.button("gallery_68")
    tk.image("sass") 
    tk.condition("persistent.unlock_68")

    tk.button("gallery_69")
    tk.image("adas") 
    tk.condition("persistent.unlock_69")

    tk.button("gallery_70")
    tk.image("elblp") 
    tk.condition("persistent.unlock_70")




    tk.transition = dissolve


screen gallery9:
    tag menu




    add "gallerymenu9"


    grid 4 2:

        xfill True
        yfill True


        add tk.make_button("gallery_64", "bwr10_tn.png", xalign=0.5, yalign=0.5)
        add tk.make_button("gallery_65", "melwrk29_tn.png", xalign=0.5, yalign=0.5)
        add tk.make_button("gallery_66", "dinner10as_tn.png", xalign=0.5, yalign=0.5)
        add tk.make_button("gallery_67", "rgts_tn.png", xalign=0.5, yalign=0.5)
        add tk.make_button("gallery_68", "rgts45_tn.png", xalign=0.5, yalign=0.5)
        add tk.make_button("gallery_69", "rgts41_tn.png", xalign=0.5, yalign=0.5)
        add tk.make_button("gallery_70", "elun_tn.png", xalign=0.5, yalign=0.5)



        textbutton "Return" action Return() xalign 0.5 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
