



init python:

    gt = Gallery()

    gt.locked_button = "locked.png"


    gt.button("gallery_15")
    gt.image("nbm_e31gal") 
    gt.condition("persistent.unlock_15")

    gt.button("gallery_16")
    gt.image("toi_rws8gal")
    gt.condition("persistent.unlock_16")


    gt.button("gallery_17")
    gt.image("rorgy11gal")
    gt.condition("persistent.unlock_17")

    gt.button("gallery_18")
    gt.image("cfm2gal")
    gt.condition("persistent.unlock_18")


    gt.button("gallery_19")
    gt.image("mstrip3gal") 
    gt.condition("persistent.unlock_19")   

    gt.button("gallery_20")
    gt.image("mdt29gal") 
    gt.condition("persistent.unlock_20")

    gt.button("gallery_21")
    gt.image("chnight1gal")
    gt.condition("persistent.unlock_21")


    gt.transition = dissolve


screen gallery2:
    tag menu




    add "gallerymenu2"


    grid 4 2:

        xfill True
        yfill True


        add gt.make_button("gallery_15", "nbm_e31_tn.png", xalign=0.5, yalign=0.5)
        add gt.make_button("gallery_16", "toi_rws6_tn.png", xalign=0.5, yalign=0.5)
        add gt.make_button("gallery_17", "rorgy2_tn.png", xalign=0.5, yalign=0.5)
        add gt.make_button("gallery_18", "cfm2_tn.png", xalign=0.5, yalign=0.5)
        add gt.make_button("gallery_19", "mstrip3_tn.png", xalign=0.5, yalign=0.5)
        add gt.make_button("gallery_20", "mdt00_tn.png", xalign=0.5, yalign=0.5)
        add gt.make_button("gallery_21", "chnight1_tn.png", xalign=0.5, yalign=0.5)




        textbutton "Return" action Return() xalign 0.5 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
