


init python:

    tr = Gallery()

    tr.locked_button = "locked.png"

    tr.button("gallery_43")
    tr.image("bgmt1")
    tr.condition("persistent.unlock_43")

    tr.button("gallery_44")
    tr.image("srviag2") 
    tr.condition("persistent.unlock_44")   

    tr.button("gallery_45")
    tr.image("mhbgal") 
    tr.condition("persistent.unlock_45")

    tr.button("gallery_46")
    tr.image("mlove123") 
    tr.condition("persistent.unlock_46")

    tr.button("gallery_47")
    tr.image("stdinner22") 
    tr.condition("persistent.unlock_47")

    tr.button("gallery_48")
    tr.image("iwtm2") 
    tr.condition("persistent.unlock_48")

    tr.button("gallery_49")
    tr.image("mstripstb045") 
    tr.condition("persistent.unlock_49")




    tr.transition = dissolve


screen gallery6:
    tag menu




    add "gallerymenu6"


    grid 4 2:

        xfill True
        yfill True


        add tr.make_button("gallery_43", "bgmt1_tn.png", xalign=0.5, yalign=0.5)
        add tr.make_button("gallery_44", "srviag2_tn.png", xalign=0.5, yalign=0.5)
        add tr.make_button("gallery_45", "mhbgal_tn.png", xalign=0.5, yalign=0.5)
        add tr.make_button("gallery_46", "mlove_tn.png", xalign=0.5, yalign=0.5)
        add tr.make_button("gallery_47", "stdinner22_tn.png", xalign=0.5, yalign=0.5)
        add tr.make_button("gallery_48", "iwtm2_tn.png", xalign=0.5, yalign=0.5)
        add tr.make_button("gallery_49", "mstripstb_tn.png", xalign=0.5, yalign=0.5)



        textbutton "Return" action Return() xalign 0.5 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
