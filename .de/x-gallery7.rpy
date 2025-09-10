

init python:

    xr = Gallery()

    xr.locked_button = "locked.png"

    xr.button("gallery_50")
    xr.image("cmt00")
    xr.condition("persistent.unlock_50")

    xr.button("gallery_51")
    xr.image("mstrp") 
    xr.condition("persistent.unlock_51")   

    xr.button("gallery_52")
    xr.image("mstripst20") 
    xr.condition("persistent.unlock_52")

    xr.button("gallery_53")
    xr.image("msdom") 
    xr.condition("persistent.unlock_53")

    xr.button("gallery_54")
    xr.image("dste") 
    xr.condition("persistent.unlock_54")

    xr.button("gallery_55")
    xr.image("dsm") 
    xr.condition("persistent.unlock_55")

    xr.button("gallery_56")
    xr.image("sdbj") 
    xr.condition("persistent.unlock_56")




    xr.transition = dissolve


screen gallery7:
    tag menu




    add "gallerymenu7"


    grid 4 2:

        xfill True
        yfill True


        add xr.make_button("gallery_50", "bbm_tn.png", xalign=0.5, yalign=0.5)
        add xr.make_button("gallery_51", "mstrp00_tn.png", xalign=0.5, yalign=0.5)
        add xr.make_button("gallery_52", "mstripst20_tn.png", xalign=0.5, yalign=0.5)
        add xr.make_button("gallery_53", "mshirto_tn.png", xalign=0.5, yalign=0.5)
        add xr.make_button("gallery_54", "stst56_tn.png", xalign=0.5, yalign=0.5)
        add xr.make_button("gallery_55", "sdayclea92a_tn.png", xalign=0.5, yalign=0.5)
        add xr.make_button("gallery_56", "sdbjend4_tn.png", xalign=0.5, yalign=0.5)



        textbutton "Return" action Return() xalign 0.5 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
