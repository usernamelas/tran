


init python:

    lb = Gallery()

    lb.locked_button = "locked.png"

    lb.button("gallery_71")
    lb.image("vch0")
    lb.condition("persistent.unlock_71")


    lb.button("gallery_72")
    lb.image("eveningrob13") 
    lb.condition("persistent.unlock_72")   


    lb.button("gallery_73")
    lb.image("robgal") 
    lb.condition("persistent.unlock_73")


    lb.button("gallery_74")
    lb.image("jbpractice20a") 
    lb.condition("persistent.unlock_74")

    lb.button("gallery_75")
    lb.image("melwrk46") 
    lb.condition("persistent.unlock_75")


    lb.button("gallery_76")
    lb.image("darow") 
    lb.condition("persistent.unlock_76")


    lb.button("gallery_77")
    lb.image("msusp23") 
    lb.condition("persistent.unlock_77")




    lb.transition = dissolve


screen gallery10:
    tag menu




    add "gallerymenu10"


    grid 4 2:

        xfill True
        yfill True


        add lb.make_button("gallery_71", "vch0_tn.png", xalign=0.5, yalign=0.5)
        add lb.make_button("gallery_72", "eveningrob13_tn.png", xalign=0.5, yalign=0.5)
        add lb.make_button("gallery_73", "etv_e17r_tn.png", xalign=0.5, yalign=0.5)
        add lb.make_button("gallery_74", "jbpractice20a_tn.png", xalign=0.5, yalign=0.5)
        add lb.make_button("gallery_75", "melwrk46_tn.png", xalign=0.5, yalign=0.5)
        add lb.make_button("gallery_76", "rvsd4_tn.png", xalign=0.5, yalign=0.5)
        add lb.make_button("gallery_77", "msusp23_tn.png", xalign=0.5, yalign=0.5)



        textbutton "Return" action Return() xalign 0.5 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
