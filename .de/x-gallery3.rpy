

init python:

    nws = Gallery()

    nws.locked_button = "locked.png"

    nws.button("gallery_22")
    nws.image("cmlgal")
    nws.condition("persistent.unlock_22")

    nws.button("gallery_23")
    nws.image("chcm1gal")
    nws.condition("persistent.unlock_23")

    nws.button("gallery_24")
    nws.image("row_visit72bgal") 
    nws.condition("persistent.unlock_24")   

    nws.button("gallery_25")
    nws.image("bexer3gal") 
    nws.condition("persistent.unlock_25")

    nws.button("gallery_26")
    nws.image("b_tv_sa8gal")
    nws.condition("persistent.unlock_26")

    nws.button("gallery_27")
    nws.image("mbgn24gal")
    nws.condition("persistent.unlock_27")

    nws.button("gallery_28")
    nws.image("nbm_e45gal")
    nws.condition("persistent.unlock_28")

    nws.transition = dissolve


screen gallery3:
    tag menu




    add "gallerymenu3"


    grid 4 2:

        xfill True
        yfill True


        add nws.make_button("gallery_22", "cml_tn.png", xalign=0.5, yalign=0.5)
        add nws.make_button("gallery_23", "chcm1_tn.png", xalign=0.5, yalign=0.5)
        add nws.make_button("gallery_24", "row_visit72b_tn.png", xalign=0.5, yalign=0.5)
        add nws.make_button("gallery_25", "bexer3_tn.png", xalign=0.5, yalign=0.5)
        add nws.make_button("gallery_26", "b_tv_sa_tn.png", xalign=0.5, yalign=0.5)
        add nws.make_button("gallery_27", "mbgn1_tn.png", xalign=0.5, yalign=0.5)
        add nws.make_button("gallery_28", "nbm_e45_tn.png", xalign=0.5, yalign=0.5)




        textbutton "Return" action Return() xalign 0.5 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
