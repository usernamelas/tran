default persistent.modGalleryUnlock = False

init 100 screen gallery_menu():
    if preferences.language != "cn":
        style_prefix "elite"

    modal True tag menu
    add 'images/nav/gallery/gallery.png'

    textbutton _("Галерея") xanchor .5 xpos 550 yalign .087 action ShowMenu("gallery_menu")
    textbutton _("Ачивки") xanchor .5 xpos 820 yalign .087 action ShowMenu("achievement_menu")
    textbutton _("Карты") xanchor .5 xpos 1100 yalign .087 action ShowMenu("cards_menu")
    textbutton _("Выход") xanchor .5 xpos 1380 yalign .087 action ShowMenu("main_menu")

    vbox:
        xalign 0.5 yalign 0.75
        spacing 45
        hbox:
            spacing 45
            xalign 0.0
            if persistent.gal1 or persistent.modGalleryUnlock:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_gal_1_idle.png"
                    hover "images/nav/gallery/ic_husb_gal_1_hover.png"
                    action [SetVariable('replay_label','prologue_house_sex'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal2 or persistent.modGalleryUnlock:
                imagebutton:
                    idle "images/nav/gallery/ic_dgast_gal_1_idle.png"
                    hover "images/nav/gallery/ic_dgast_gal_1_hover.png"
                    action [SetVariable('replay_label','prologue_day2_problem_0'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal3 or persistent.modGalleryUnlock:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_gal_2_idle.png"
                    hover "images/nav/gallery/ic_husb_gal_2_hover.png"
                    action [SetVariable('replay_label','gallery3'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal4 or persistent.modGalleryUnlock:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_gal_3_idle.png"
                    hover "images/nav/gallery/ic_husb_gal_3_hover.png"
                    action [SetVariable('replay_label','gallery4'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

        hbox:
            spacing 45
            xalign 0.0
            if persistent.gal5 or persistent.modGalleryUnlock:
                imagebutton:
                    idle "images/nav/gallery/ic_boss_gal_1_idle.png"
                    hover "images/nav/gallery/ic_boss_gal_1_hover.png"
                    action [SetVariable('replay_label','prologue_day3_work_meet_boss'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal6 or persistent.modGalleryUnlock:
                imagebutton:
                    idle "images/nav/gallery/ic_djast_1_idle.png"
                    hover "images/nav/gallery/ic_djast_1_hover.png"
                    action [SetVariable('replay_label','prologue_ep2_emma_mast'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal7 or persistent.modGalleryUnlock:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_gal_4_idle.png"
                    hover "images/nav/gallery/ic_husb_gal_4_hover.png"
                    action [SetVariable('replay_label','prologue_ep2_emma_mast2'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal9 or persistent.modGalleryUnlock:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_gard_1_idle.png"
                    hover "images/nav/gallery/ic_husb_gard_1_hover.png"
                    action [SetVariable('replay_label','day4_justin_shelley_sex_tyler'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

        hbox:
            spacing 45
            xalign 0.0
            if persistent.gal8 or persistent.modGalleryUnlock:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_photo_1_idle.png"
                    hover "images/nav/gallery/ic_husb_photo_1_hover.png"
                    action [SetVariable('replay_label','day4_studio2_gallery'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal10 or persistent.modGalleryUnlock:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_lake_1_idle.png"
                    hover "images/nav/gallery/ic_husb_lake_1_hover.png"
                    action [SetVariable('replay_label','day5_lake_sex_gal'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal11 or persistent.modGalleryUnlock:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_maid_idle.png"
                    hover "images/nav/gallery/ic_husb_maid_hover.png"
                    action [SetVariable('replay_label','day11_poss_4_gal11'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal12 or persistent.modGalleryUnlock:
                imagebutton:
                    idle "images/nav/gallery/ic_peep_1_idle.png"
                    hover "images/nav/gallery/ic_peep_1_hover.png"
                    action [SetVariable('replay_label','quest_watcher_4_play'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

    vbox:
        xalign 0.5
        yalign 1.0
        if persistent.modGalleryUnlock:
            textbutton "Lock Scenes":
                action SetVariable("persistent.modGalleryUnlock", False)
        else:
            textbutton "Unlock Scenes":
                action SetVariable("persistent.modGalleryUnlock", True)

        text "By DA":
            size 18
            color "#03b420"
            xalign 0.5
            ypos -15
