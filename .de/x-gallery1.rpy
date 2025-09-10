


init python:

    ge = Gallery()

    ge.locked_button = "locked.png"

    ge.button("gallery_8")
    ge.image("sani03gal")
    ge.condition("persistent.unlock_8")

    ge.button("gallery_9")
    ge.image("spiera13gal") 
    ge.condition("persistent.unlock_9")   

    ge.button("gallery_10")
    ge.image("bworkm1gal") 
    ge.condition("persistent.unlock_10")

    ge.button("gallery_11")
    ge.image("citymel4gal")
    ge.condition("persistent.unlock_11")

    ge.button("gallery_12")
    ge.image("girlnight41gal")
    ge.condition("persistent.unlock_12")

    ge.button("gallery_13")
    ge.image("ralone6gal")
    ge.condition("persistent.unlock_13")

    ge.button("gallery_14")
    ge.image("slkmo18gal") 
    ge.condition("persistent.unlock_14")   

    ge.transition = dissolve


screen gallery1:
    tag menu




    add "gallerymenu1"


    grid 4 2:

        xfill True
        yfill True


        add ge.make_button("gallery_8", "sani03gal_tn.png", xalign=0.5, yalign=0.5)
        add ge.make_button("gallery_9", "spiera13gal_tn.png", xalign=0.5, yalign=0.5)
        add ge.make_button("gallery_10", "bworkm1gal_tn.png", xalign=0.5, yalign=0.5)
        add ge.make_button("gallery_11", "citymel4_tn.png", xalign=0.5, yalign=0.5)
        add ge.make_button("gallery_12", "girlnight41_tn.png", xalign=0.5, yalign=0.5)
        add ge.make_button("gallery_13", "ralone6_tn.png", xalign=0.5, yalign=0.5)
        add ge.make_button("gallery_14", "slkmo18_tn.png", xalign=0.5, yalign=0.5)





        textbutton "Return" action Return() xalign 0.5 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
