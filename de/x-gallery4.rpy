

init python:

    gh = Gallery()

    gh.locked_button = "locked.png"

    gh.button("gallery_29")
    gh.image("mbgn70gal") 
    gh.condition("persistent.unlock_29")   

    gh.button("gallery_30")
    gh.image("nbrm5gal") 
    gh.condition("persistent.unlock_30")

    gh.button("gallery_31")
    gh.image("chbeachgal")
    gh.condition("persistent.unlock_31")


    gh.button("gallery_32")
    gh.image("mbgn83gal")
    gh.condition("persistent.unlock_32")

    gh.button("gallery_33")
    gh.image("msbb")
    gh.condition("persistent.unlock_33")


    gh.button("gallery_34")
    gh.image("nbcabanabrb") 
    gh.condition("persistent.unlock_34")   

    gh.button("gallery_35")
    gh.image("chnight45agal") 
    gh.condition("persistent.unlock_35")

    gh.transition = dissolve


screen gallery4:
    tag menu




    add "gallerymenu4"


    grid 4 2:

        xfill True
        yfill True


        add gh.make_button("gallery_29", "mbgn74_tn.png", xalign=0.5, yalign=0.5)
        add gh.make_button("gallery_30", "nbrm5_tn.png", xalign=0.5, yalign=0.5)
        add gh.make_button("gallery_31", "chbeach18_tn.png", xalign=0.5, yalign=0.5)
        add gh.make_button("gallery_32", "mbgn83_tn.png", xalign=0.5, yalign=0.5)
        add gh.make_button("gallery_33", "mstrip20_tn.png", xalign=0.5, yalign=0.5)
        add gh.make_button("gallery_34", "nbcabanars24_tn.png", xalign=0.5, yalign=0.5)
        add gh.make_button("gallery_35", "chnight45a_tn.png", xalign=0.5, yalign=0.5)




        textbutton "Return" action Return() xalign 0.5 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
