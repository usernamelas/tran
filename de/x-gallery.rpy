

init python:

    g = Gallery()

    g.locked_button = "locked.png"


    g.button("gallery_1")
    g.image("evfagallery")
    g.condition("persistent.unlock_1")



    g.button("gallery_2")
    g.image("mdncgallery")
    g.condition("persistent.unlock_2")

    g.button("gallery_3")
    g.image("srragallery")
    g.condition("persistent.unlock_3")


    g.button("gallery_4")
    g.image("nbm_e12") 
    g.condition("persistent.unlock_4")   

    g.button("gallery_5")
    g.image("etv_e58gallery") 
    g.condition("persistent.unlock_5")

    g.button("gallery_6")
    g.image("jbpractice81gal")
    g.condition("persistent.unlock_6")

    g.button("gallery_7")
    g.image("sbbjob17gal")
    g.condition("persistent.unlock_7")

    g.transition = dissolve


screen gallery:
    tag menu




    add "gallerymenu"


    grid 4 2:

        xfill True
        yfill True


        add g.make_button("gallery_1", "evfagallery_tn.png", xalign=0.5, yalign=0.5)
        add g.make_button("gallery_2", "mdncgallery_tn.png", xalign=0.5, yalign=0.5)
        add g.make_button("gallery_3", "srragallery_tn.png", xalign=0.5, yalign=0.5)
        add g.make_button("gallery_4", "nbm_e12_tn.png", xalign=0.5, yalign=0.5)
        add g.make_button("gallery_5", "etv_e58_tn.png", xalign=0.5, yalign=0.5)
        add g.make_button("gallery_6", "jbpractice81gal_tn.png", xalign=0.5, yalign=0.5)
        add g.make_button("gallery_7", "sbbjob17gal_tn.png", xalign=0.5, yalign=0.5)

        textbutton "Return" action Return() xalign 0.5 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
