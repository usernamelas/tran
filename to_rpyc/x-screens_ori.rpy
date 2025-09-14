










init -1 style default:
    properties gui.text_properties()
    language gui.language

init -1 style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

init -1 style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

init -1 style gui_text:
    properties gui.text_properties("interface")


init -1 style button:
    properties gui.button_properties("button")

init -1 style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

init -1 style prompt_text is gui_text:
    properties gui.text_properties("prompt")


init -1 style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)























init -501 screen say(who, what):
    zorder 25
    if preferences.language != "cn":
        style_prefix "say_elite"
        window:
            id "window"
            if who is not None:
                window:
                    id "namebox"
                    style "elite_namebox"
                    text who id "who"
            text what id "what"

    else:
        style_prefix "say"
        window:
            id "window"
            if who is not None:
                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"
            text what id "what"










init -1 python:
    config.character_id_prefixes.append('namebox')

init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue

init -1 style namebox is default
init -1 style namebox_label is say_label


init -1 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

init -1 style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

init -1 style elite_default is default:
    font "SpecialElite.ttf"
    size int(gui.text_size * 1.1)

init -1 style elite_input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False
    font "SpecialElite.ttf"
    size int(gui.text_size * 1.1)

init -1 style elite_hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True
    font "SpecialElite.ttf"
    size int(gui.text_size * 1.1)

init -1 style elite_gui_text:
    properties gui.text_properties("interface")
    font "SpecialElite.ttf"
    size int(gui.text_size * 1.1)

init -1 style elite_button:
    properties gui.button_properties("button")

init -1 style elite_button_text is elite_gui_text:
    properties gui.text_properties("button")
    yalign 0.5
    font "SpecialElite.ttf"
    size int(gui.text_size * 1.1)

init -1 style elite_label_text is elite_gui_text:
    properties gui.text_properties("label", accent=True)
    font "SpecialElite.ttf"
    size int(gui.text_size * 1.1)

init -1 style elite_prompt_text is elite_gui_text:
    properties gui.text_properties("prompt")
    font "SpecialElite.ttf"
    size int(gui.text_size * 1.1)


init -1 style say_elite_label is say_label:
    font "SpecialElite.ttf"
    size int(gui.label_text_size * 1.1)

init -1 style say_elite_dialogue is say_dialogue

init -1 style say_elite_window is default:
    font "SpecialElite.ttf"
    size int(gui.text_size * 1.1)

init -1 style say_elite_thought is say_elite_dialogue

init -1 style elite_namebox is namebox:
    font "SpecialElite.ttf"


init -1 style elite_namebox_label is say_elite_label












init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox
        xanchor gui.dialogue_text_xalign
        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos
        if preferences.language != "cn":
            text prompt style "input_elite_prompt"
        else:
            text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt is default



init -1 style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

init -1 style input_elite_prompt is input_prompt:
    font "SpecialElite.ttf"
    size int(gui.text_size * 1.1)

init -1 style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










init -501 screen choice(items):
    if preferences.language != "cn":
        style_prefix "choice_elite"
    else:
        style_prefix "choice"

    vbox:


        for i in items:

            $ processed_caption = process_choice_text(i.caption)
            textbutton processed_caption action i.action


init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    yalign 0.9



    spacing gui.choice_spacing

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")

init -1 style choice_button_text is default:
    properties gui.text_properties("choice_button")

init -1 style choice_elite_vbox is choice_vbox
init -1 style choice_elite_button is choice_button
init -1 style choice_elite_button_text is choice_button_text:
    font "SpecialElite.ttf"
    size int(gui.text_size * 1.1)







init -501 screen quick_menu():


    default quick_menu_hidden = True


    zorder 100
    if iface:

        imagebutton:
            idle im.Scale("gui/q/hide_idle.webp", 64, 64)
            hover im.Scale("gui/q/hide_hover.webp", 64, 64)
            action SetVariable("iface", False)
            align (.0, 1.0)
    else:
        imagebutton:
            idle im.Scale("gui/q/open_idle.webp", 64, 64)
            hover im.Scale("gui/q/open_hover.webp", 64, 64)
            action SetVariable("iface", True)
            align (.0, 1.0)


    if quick_menu:

        vbox:
            style_prefix "quick"

            xalign 1.0
            yalign 1.0


            if not quick_menu_hidden:

                if renpy.can_rollback():
                    imagebutton idle im.Scale("gui/q/back_idle.webp", 64, 64) hover im.Scale("gui/q/back_hover.webp", 64, 64) action Rollback()

                imagebutton idle im.Scale("gui/q/menu_idle.webp", 64, 64) hover im.Scale("gui/q/menu_hover.webp", 64, 64) action ShowMenu('history')


                if config.allow_skipping:
                    imagebutton idle im.Scale("gui/q/forv_idle.webp", 64, 64) hover im.Scale("gui/q/forv_hover.webp", 64, 64) action Skip() alternate Skip(fast=True, confirm=True)

                imagebutton idle im.Scale("gui/q/prefs_idle.webp", 64, 64) hover im.Scale("gui/q/prefs_hover.webp", 64, 64) action Preference("auto-forward", "toggle")
                imagebutton idle im.Scale("gui/q/save_idle.webp", 64, 64) hover im.Scale("gui/q/save_hover.webp", 64, 64) action ShowMenu('save')
                imagebutton idle im.Scale("gui/q/load_idle.webp", 64, 64) hover im.Scale("gui/q/load_hover.webp", 64, 64) action QuickSave()


                imagebutton idle im.Scale("gui/q/hide_idle.webp", 64, 64) hover im.Scale("gui/q/hide_hover.webp", 64, 64) action SetScreenVariable("quick_menu_hidden", True)


            else:
                imagebutton idle im.Scale("gui/q/open_idle.webp", 64, 64) hover im.Scale("gui/q/open_hover.webp", 64, 64) action SetScreenVariable("quick_menu_hidden", False)




init -1 python:
    config.overlay_screens.append("quick_menu")

default -1 quick_menu = True

init -1 style quick_button is default
init -1 style quick_button_text is button_text

init -1 style quick_button:
    properties gui.button_properties("quick_button")

init -1 style quick_button_text:
    properties gui.text_properties("quick_button")











init -501 screen navigation():
    if preferences.language != "cn":
        style_prefix "navigation_elite"
    else:
        style_prefix "navigation"

    vbox:
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Начать") action Start()
        else:
            textbutton _("История") action ShowMenu("history")
            textbutton _("Сохранить") action ShowMenu("save")

        textbutton _("Загрузить") action ShowMenu("load")
        textbutton _("Настройки") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("Завершить повтор") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Главное меню") action MainMenu()

        textbutton _("Об игре") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            textbutton _("Помощь") action ShowMenu("help")

        if renpy.variant("pc"):

            textbutton _("Выход") action Quit(confirm=not main_menu)


init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

init -1 style navigation_button_text:
    properties gui.text_properties("navigation_button")


init -1 style navigation_elite_button is navigation_button
init -1 style navigation_elite_button_text is navigation_button_text

init -1 style navigation_elite_button_text:
    font "SpecialElite.ttf"


init -501 screen language_selector():
    modal True

    frame:
        style_prefix "language"
        xalign 0.75
        yalign 0.9
        xoffset 40
        padding (20, 20)

        has vbox
        spacing 10
        hbox:
            spacing 10
            add "gui/ic_rus.png" yalign 0.5
            textbutton "Русский" action [Function(switch_language_and_style, None), Hide("language_selector")]
        hbox:
            spacing 10
            add "gui/ic_eng.png" yalign 0.5
            textbutton "English" action [Function(switch_language_and_style, "english"), Hide("language_selector")]
        hbox:
            spacing 10
            add "gui/ic_cn.png" yalign 0.5
            textbutton "{font=NotoSerifSC-SemiBold.ttf}简体中文{/font}" action [Function(switch_language_and_style, "cn"), StylePreference("dialog_font", "FontChinese"), Hide("language_selector")]
        hbox:
            spacing 10
            add "gui/ic_de.png" yalign 0.5
            textbutton "Deutsch" action [Function(switch_language_and_style, "de"), Hide("language_selector")]
        hbox:
            spacing 10
            add "gui/ic_fr.png" yalign 0.5
            textbutton "Français" action [Function(switch_language_and_style, "fr"), Hide("language_selector")]
        hbox:
            spacing 10
            add "gui/ic_sp.png" yalign 0.5
            textbutton "Español" action [Function(switch_language_and_style, "sp"), Hide("language_selector")]
        hbox:
            spacing 10
            add "gui/ic_it.png" yalign 0.5
            textbutton "Italiano" action [Function(switch_language_and_style, "it"), Hide("language_selector")]
        hbox:
            spacing 10
            add "gui/ic_br.png" yalign 0.5
            textbutton "Português (BR)" action [Function(switch_language_and_style, "br"), Hide("language_selector")]
        hbox:
            spacing 10
            add "gui/ic_id.png" yalign 0.5
            textbutton "Indonesia" action [Function(switch_language_and_style, "id"), Hide("language_selector")]


init -1 style language_frame:
    background "#d7cfcfb4"
    padding (20, 20)
    xsize 220

init -1 style language_button:
    xfill True
    background None
    padding (10, 5)

init -1 style language_button_text:
    size 28
    color "#ffffff"
    hover_color gui.hover_color
    outlines [ (2, "#000000", 0, 0) ]
    align (0.5, 0.5)







init -501 screen main_menu():
    tag menu
    add gui.main_menu_background


    if preferences.language is None:
        add "gui/ic_rus.png" xalign 0.0 yalign 0.0 xoffset 10 yoffset 10
    elif preferences.language == "english":
        add "gui/ic_eng.png" xalign 0.0 yalign 0.0 xoffset 10 yoffset 10
    elif preferences.language == "cn":
        add "gui/ic_cn.png" xalign 0.0 yalign 0.0 xoffset 10 yoffset 10
    elif preferences.language == "de":
        add "gui/ic_de.png" xalign 0.0 yalign 0.0 xoffset 10 yoffset 10
    elif preferences.language == "fr":
        add "gui/ic_fr.png" xalign 0.0 yalign 0.0 xoffset 10 yoffset 10
    elif preferences.language == "sp":
        add "gui/ic_sp.png" xalign 0.0 yalign 0.0 xoffset 10 yoffset 10
    elif preferences.language == "it":
        add "gui/ic_it.png" xalign 0.0 yalign 0.0 xoffset 10 yoffset 10
    elif preferences.language == "br":
        add "gui/ic_br.png" xalign 0.0 yalign 0.0 xoffset 10 yoffset 10
    elif preferences.language == "id":
        add "gui/ic_br.png" xalign 0.0 yalign 0.0 xoffset 10 yoffset 10

    if preferences.language != "cn":
        text "[config.version]":
            style "main_menu_version_elite"
            xalign 1.0
            yalign 0.0
            xoffset -10
            yoffset 10

        text "[config.name!t]":
            style "main_menu_title_elite"
            xalign 0.0
            yalign 1.0
            xoffset 20
            yoffset -20

        vbox:
            style_prefix "navigation_elite"
            xalign 1.0
            ypos 441
            xoffset -30
            spacing 29

            textbutton _("НОВАЯ ИГРА") action Start()
            textbutton _("ЗАГРУЗИТЬ") action ShowMenu("load")
            textbutton _("НАСТРОЙКИ") action ShowMenu("preferences")
            textbutton _("ГАЛЕРЕЯ") action ShowMenu("gallery_menu")
            textbutton _("НАШИ ИГРЫ") action OpenURL("https://www.patreon.com/c/novel/posts")
            textbutton _("DISCORD") action OpenURL("https://discord.gg/kguBAf7")


            imagebutton:
                idle "#22222200"
                hover "#83838342"
                xsize 300
                ysize 58
                action Show("language_selector")

        hbox:
            spacing -5
            xalign 0.95
            yalign 0.86
            add "gui/ic_rus.png"
            add "gui/ic_eng.png"
            add "gui/ic_cn.png"
            add "gui/ic_de.png"
            add "gui/ic_fr.png"
            add "gui/ic_sp.png"
            add "gui/ic_it.png"
            add "gui/ic_br.png"
            add "gui/ic_id.png"

        textbutton _("ВЫХОД") action Quit(confirm=True) xalign 1.0 xoffset -40 yalign 0.97 style_prefix "navigation_elite"
    else:
        text "[config.version]":
            style "main_menu_version"
            xalign 1.0
            yalign 0.0
            xoffset -10
            yoffset 10

        text "[config.name!t]":
            style "main_menu_title"
            xalign 0.0
            yalign 1.0
            xoffset 20
            yoffset -20

        vbox:
            style_prefix "navigation"
            xalign 1.0
            ypos 430
            xoffset -25
            spacing 14

            textbutton _("НОВАЯ ИГРА") action Start()
            textbutton _("ЗАГРУЗИТЬ") action ShowMenu("load")
            textbutton _("НАСТРОЙКИ") action ShowMenu("preferences")
            textbutton _("ГАЛЕРЕЯ") action ShowMenu("gallery_menu")
            textbutton _("НАШИ ИГРЫ") action OpenURL("https://www.patreon.com/c/novel/posts")
            textbutton _("DISCORD") action OpenURL("https://discord.gg/kguBAf7")


            imagebutton:
                idle "#22222208"
                hover "#22222222"
                xsize 350
                ysize 70
                action Show("language_selector")

        hbox:
            spacing -5
            xalign 0.94
            yalign 0.86
            add "gui/ic_rus.png"
            add "gui/ic_eng.png"
            add "gui/ic_cn.png"
            add "gui/ic_de.png"
            add "gui/ic_fr.png"
            add "gui/ic_sp.png"
            add "gui/ic_it.png"
            add "gui/ic_br.png"
            add "gui/ic_id.png"

        textbutton _("ВЫХОД") action Quit(confirm=True) xalign 1.0 xoffset -40 yalign 0.97 style_prefix "navigation"



init -1 style main_menu_frame:
    background None
    xsize 1920
    ysize 1080

init -1 style main_menu_left_frame:
    background None
    xsize 960
    ysize 1080

init -1 style main_menu_right_frame:
    background None
    xsize 960
    ysize 1080
    xalign 1.0
    yalign 0.0

init -1 style main_menu_title:
    size 60
    color "#ffffff"
    outlines [ (2, "#000000", 0, 0) ]

init -1 style main_menu_version:
    size 24
    color "#ffffff"
    outlines [ (1, "#000000", 0, 0) ]

init -1 style navigation_button:
    xsize 300
    background None
    padding (10, 5)
    xalign .5


init -1 style navigation_button_text:
    size 32
    color "#ffffff"
    hover_color gui.hover_color
    selected_color gui.hover_color
    outlines [ (2, "#000000", 0, 0) ]
    align (0.5, 0.5)

init -1 style main_menu_version_elite is main_menu_version:
    font "SpecialElite.ttf"
    size int(gui.notify_text_size * 1.1)

init -1 style main_menu_title_elite is main_menu_title:
    font "SpecialElite.ttf"
    size int(gui.title_text_size * 1.1)












init -501 screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    if preferences.language != "cn":
        style_prefix "game_menu_elite"

        if main_menu:
            add gui.main_menu_background
        else:
            add gui.game_menu_background

        frame:
            style "game_menu_outer_frame_elite"
            has hbox

            frame:
                style "game_menu_navigation_frame_elite"
            frame:
                style "game_menu_content_frame_elite"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        has vbox
                        spacing spacing
                        transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        spacing spacing
                        transclude
                else:
                    transclude

        use navigation

        textbutton _("Вернуться"):
            style "return_button"
            action Return()

        label title:
            style "game_menu_label_elite"

        if main_menu:
            key "game_menu" action ShowMenu("main_menu")

    else:
        style_prefix "game_menu"

        if main_menu:
            add gui.main_menu_background
        else:
            add gui.game_menu_background

        frame:
            style "game_menu_outer_frame"
            has hbox

            frame:
                style "game_menu_navigation_frame"
            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        has vbox
                        spacing spacing
                        transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        spacing spacing
                        transclude
                else:
                    transclude

        use navigation

        textbutton _("Вернуться"):
            style "return_button"
            action Return()

        label title:
            style "game_menu_label"

        if main_menu:
            key "game_menu" action ShowMenu("main_menu")


init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar

init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text

init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text

init -1 style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background 'gui/preferences_background.png'

init -1 style game_menu_navigation_frame:
    xsize 420
    yfill True

init -1 style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

init -1 style game_menu_viewport:
    xsize 1380

init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:
    spacing 15

init -1 style game_menu_label:
    xpos 75
    ysize 180

init -1 style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

init -1 style return_button:
    xpos gui.navigation_xpos + 100
    yalign 1.0
    yoffset -45

init -1 style game_menu_outer_frame_elite is game_menu_outer_frame
init -1 style game_menu_navigation_frame_elite is game_menu_navigation_frame
init -1 style game_menu_content_frame_elite is game_menu_content_frame

init -1 style game_menu_label_elite is game_menu_label
init -1 style game_menu_label_text_elite is game_menu_label_text:
    font "SpecialElite.ttf"
    size int(gui.label_text_size * 1.1)



init -1 style return_button_text_elite is return_button_text:
    font "SpecialElite.ttf"









init -501 screen about():
    tag menu




    use game_menu(_("Об игре"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Версия [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Сделано с помощью {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size










init -501 screen save():
    tag menu


    use file_slots(_("Сохранить"))


init -501 screen load():
    tag menu


    use file_slots(_("Загрузить"))


init -501 screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("{} страница"), auto=_("Автосохранения"), quick=_("Быстрые сохранения"))

    use game_menu(title):

        fixed:



            order_reverse True



            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        if persistent.saveName:
                            action If(renpy.get_screen("save"), true=Show("savegameName", accept=FileSave(slot)), false=FileLoad(slot))
                        else:
                            action FileAction(slot)

                        vbox:

                            add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"

                            if FileSaveName(slot):
                                $ fn = FileSaveName(slot)
                                if fn and ("-" in fn):
                                    $ y = fn.split("-")
                                text fn:
                                    style "slot_name_text"

                            key "save_delete" action FileDelete(slot)











            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}А") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Б") action FilePage("quick")


                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Загрузить Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Скачать Sync"):
                            action DownloadSync()
                            xalign 0.5


init -501 screen savegameName(accept=NullAction()):

    modal True
    add "black" alpha 0.8
    style_prefix "savegameName"

    frame:
        has vbox
        xalign 0.5
        spacing 20

        label _("Save Name"):
            text_color gui.text_color
            xalign 0.5

        null height 10

        input size 40 color gui.hover_color changed Namer length 42:
            yalign 1.0
            xalign 0.5
            xysize (550, 40)

        textbutton _("{u}Save the Game{/u}"):
            xalign 0.5
            keysym ['K_RETURN', 'K_KP_ENTER']
            action [accept, (Hide("savegameName"))]

init -1 python:
    def Namer(name):
        store.save_name = name

default -1 persistent.saveName = True

init -1 style savegameName_frame:
    padding gui.confirm_frame_borders.padding
    xsize 650
    xalign 0.5
    yalign 0.5

init -1 style savegameName_frame:
    variant "touch"
    padding gui.confirm_frame_borders.padding
    xsize 650
    xalign 0.5
    yalign 0
    ypos 50

init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text

init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text:
    color '#8bd3ff'
    size 20

init -1 style page_label:
    xpadding 75
    ypadding 5

init -1 style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

init -1 style page_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text:
    properties gui.text_properties("page_button")

init -1 style slot_button:
    properties gui.button_properties("slot_button")

init -1 style slot_button_text:
    properties gui.text_properties("slot_button")








init -501 screen preferences():
    tag menu


    use game_menu(_("Настройки"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Режим экрана")
                        textbutton _("Оконный") action Preference("display", "window")
                        textbutton _("Полный") action Preference("display", "fullscreen")




                vbox:
                    style_prefix "check"
                    label _("Пропуск")
                    textbutton _("Всего текста") action Preference("skip", "toggle")
                    textbutton _("После выборов") action Preference("after choices", "toggle")
                    textbutton _("Переходов") action InvertSelected(Preference("transitions", "toggle"))

                if preferences.language != "cn":
                    vbox:
                        style_prefix "check"
                        xalign 0.0
                        label _("Шрифт диалогов")

                        textbutton _("{font=PTC55F.ttf}Обычный{/font}") action StylePreference("dialog_font", "FontPTC55F") text_size 32
                        textbutton _("{font=PTS56F.ttf}Курсив{/font}") action StylePreference("dialog_font", "FontPTS56F") text_size 33
                        textbutton _("{font=SpecialElite.ttf}Красивый{/font}") action StylePreference("dialog_font", "FontSpecialElite") text_size 36
                else:
                    vbox:

                        xalign 0.0
                        textbutton "点击修复字体" action StylePreference("dialog_font", "FontChinese") xalign 0.5 text_size 28

                vbox:
                    style_prefix "radio"
                    label _("Save game names")
                    textbutton _("Yes") action [SetVariable("persistent.saveName", True), SetVariable("store.save_name", "")]
                    textbutton _("No") action [SetVariable("persistent.saveName", False), SetVariable("store.save_name", "Un-Named")]

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Скорость текста")

                    bar value Preference("text speed")

                    label _("Скорость авточтения")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Громкость музыки")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Громкость звуков")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Тест") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Громкость голоса")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Тест") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Без звука"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox

init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox

init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox

init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox

init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text

init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

init -1 style pref_label_text:
    yalign 1.0

init -1 style pref_vbox:
    xsize 338

init -1 style radio_vbox:
    spacing gui.pref_button_spacing

init -1 style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

init -1 style radio_button_text:
    properties gui.text_properties("radio_button")

init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style check_button_text:
    properties gui.text_properties("check_button")

init -1 style slider_slider:
    xsize 525

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

init -1 style slider_button_text:
    properties gui.text_properties("slider_button")

init -1 style slider_vbox:
    xsize 675









init -501 screen history():
    tag menu




    predict False

    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:



                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("История диалогов пуста.")




define -1 gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5








init -501 screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Помощь"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Клавиатура") action SetScreenVariable("device", "keyboard")
                textbutton _("Мышь") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Геймпад") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


init -501 screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Пробел")
        text _("Прохождение диалогов без возможности делать выбор.")

    hbox:
        label _("Стрелки")
        text _("Навигация по интерфейсу.")

    hbox:
        label _("Esc")
        text _("Вход в игровое меню.")

    hbox:
        label _("Ctrl")
        text _("Пропускает диалоги, пока зажат.")

    hbox:
        label _("Tab")
        text _("Включает режим пропуска.")

    hbox:
        label _("Page Up")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Page Down")
        text _("Откатывает предыдущее действие вперёд.")

    hbox:
        label "H"
        text _("Скрывает интерфейс пользователя.")

    hbox:
        label "S"
        text _("Делает снимок экрана.")

    hbox:
        label "V"
        text _("Включает поддерживаемый {a=https://www.renpy.org/l/voicing}синтезатор речи{/a}.")

    hbox:
        label "Shift+A"
        text _("Открывает меню специальных возможностей.")


init -501 screen mouse_help():

    hbox:
        label _("Левый клик")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Клик колёсиком")
        text _("Скрывает интерфейс пользователя.")

    hbox:
        label _("Правый клик")
        text _("Вход в игровое меню.")

    hbox:
        label _("Колёсико вверх")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Колёсико вниз")
        text _("Откатывает предыдущее действие вперёд.")


init -501 screen gamepad_help():

    hbox:
        label _("Правый триггер\nA/Нижняя кнопка")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Левый Триггер\nЛевый Бампер")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Правый бампер")
        text _("Откатывает предыдущее действие вперёд.")

    hbox:
        label _("Крестовина, Стики")
        text _("Навигация по интерфейсу.")

    hbox:
        label _("Старт, Гид, B/Правая кнопка")
        text _("Вход в игровое меню.")

    hbox:
        label _("Y/Верхняя кнопка")
        text _("Скрывает интерфейс пользователя.")

    textbutton _("Калибровка") action GamepadCalibrate()


init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text

init -1 style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

init -1 style help_button_text:
    properties gui.text_properties("help_button")

init -1 style help_label:
    xsize 375
    right_padding 30

init -1 style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0















init -501 screen confirm(message, yes_action, no_action):

    modal True
    zorder 200

    if preferences.language != "cn":
        style_prefix "confirm_elite"
        add "gui/overlay/confirm.png"

        frame:
            style "confirm_frame_elite"
            has vbox
            xalign 0.5
            yalign 0.5
            spacing 45

            label _(message):
                style "confirm_prompt_elite"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Да") action yes_action style "confirm_button_elite"
                textbutton _("Нет") action no_action style "confirm_button_elite"

    else:
        style_prefix "confirm"
        add "gui/overlay/confirm.png"

        frame:
            style "confirm_frame"
            has vbox
            xalign 0.5
            yalign 0.5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Да") action yes_action style "confirm_button"
                textbutton _("Нет") action no_action style "confirm_button"

    key "game_menu" action no_action


init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")

init -1 style confirm_button_text:
    properties gui.text_properties("confirm_button")

init -1 style confirm_frame_elite is confirm_frame

init -1 style confirm_prompt_elite is confirm_prompt
init -1 style confirm_prompt_text_elite is confirm_prompt_text:
    font "SpecialElite.ttf"
    size int(gui.text_size * 1.1)

init -1 style confirm_button_elite is confirm_button
init -1 style confirm_button_text_elite is confirm_button_text:
    font "SpecialElite.ttf"
    size int(gui.text_size * 1.1)









init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox
        spacing 9

        text _("Пропускаю")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:

    font "DejaVuSans.ttf"









init -501 screen notify(message):

    zorder 100
    if preferences.language != "cn":
        style_prefix "notify"
        frame at notify_appear:
            text "[message!tq]" style "notify_text_elite"
    else:
        style_prefix "notify"
        frame at notify_appear:
            text "[message!tq]" style "notify_text"

    timer 3.25 action Hide('notify')


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    properties gui.text_properties("notify")

init -1 style notify_text_elite is notify_text:
    font "SpecialElite.ttf"
    size int(gui.notify_text_size * 1.1)





















































































































































































































init -1 style pref_vbox:
    variant "medium"
    xsize 675




init -501 screen quick_menu():
    variant "touch"


    default quick_menu_hidden = True


    zorder 100
    if iface:

        imagebutton:
            idle im.Scale("gui/q/hide_idle.webp", 100, 100)
            hover im.Scale("gui/q/hide_hover.webp", 100, 100)
            action SetVariable("iface", False)
            align (.0, 1.0)
    else:
        imagebutton:
            idle im.Scale("gui/q/open_idle.webp", 100, 100)
            hover im.Scale("gui/q/open_hover.webp", 100, 100)
            action SetVariable("iface", True)
            align (.0, 1.0)


    if quick_menu:

        vbox:
            style_prefix "quick"

            xalign 1.0
            yalign 1.0


            if not quick_menu_hidden:

                if renpy.can_rollback():
                    imagebutton idle im.Scale("gui/q/back_idle.webp", 150, 150) hover im.Scale("gui/q/back_hover.webp", 150, 150) action Rollback()

                imagebutton idle im.Scale("gui/q/menu_idle.webp", 150, 150) hover im.Scale("gui/q/menu_hover.webp", 150, 150) action ShowMenu('history')


                if config.allow_skipping:
                    imagebutton idle im.Scale("gui/q/forv_idle.webp", 150, 150) hover im.Scale("gui/q/forv_hover.webp", 150, 150) action Skip() alternate Skip(fast=True, confirm=True)

                imagebutton idle im.Scale("gui/q/prefs_idle.webp", 150, 150) hover im.Scale("gui/q/prefs_hover.webp", 150, 150) action Preference("auto-forward", "toggle")
                imagebutton idle im.Scale("gui/q/save_idle.webp", 150, 150) hover im.Scale("gui/q/save_hover.webp", 150, 150) action ShowMenu('save')
                imagebutton idle im.Scale("gui/q/load_idle.webp", 150, 150) hover im.Scale("gui/q/load_hover.webp", 150, 150) action QuickSave()


                imagebutton idle im.Scale("gui/q/hide_idle.webp", 150, 150) hover im.Scale("gui/q/hide_hover.webp", 150, 150) action SetScreenVariable("quick_menu_hidden", True)


            else:
                imagebutton idle im.Scale("gui/q/open_idle.webp", 150, 150) hover im.Scale("gui/q/open_hover.webp", 150, 150) action SetScreenVariable("quick_menu_hidden", False)


init -1 style window:
    variant "small"
    background "gui/phone/textbox.png"

init -1 style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

init -1 style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

init -1 style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

init -1 style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

init -1 style game_menu_outer_frame:
    variant "small"
    background 'gui/preferences_background.png'

init -1 style game_menu_navigation_frame:
    variant "small"
    xsize 510

init -1 style game_menu_content_frame:
    variant "small"
    top_margin 0

init -1 style pref_vbox:
    variant "small"
    xsize 600

init -1 style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

init -1 style slider_vbox:
    variant "small"
    xsize None

init -1 style slider_slider:
    variant "small"
    xsize 900


init -501 screen tooltip_screen(tooltip_text, x_pos=0.05, y_pos=0.99):
    frame:

        at transform:
            alpha 0.0
            ease 0.15 alpha 1.0
        background Frame("gui/namebox.png", 10, 10)
        padding (15, 8)
        xalign x_pos
        yalign y_pos
        xsize None
        ysize None
        if preferences.language != "cn":
            text tooltip_text:
                style "tooltip_style_elite"
                text_align 0.5
                xfill False
        else:
            text tooltip_text:
                style "tooltip_style"
                text_align 0.5
                xfill False
init -501 screen tooltip_screen2(tooltip_text, x_pos=0.0015, y_pos=0.75):
    frame:

        at transform:
            alpha 0.0
            ease 0.15 alpha 1.0
        padding (15, 8)
        xalign 0.0
        yalign 1.0
        xsize None
        ysize None
        if preferences.language != "cn":
            text tooltip_text:
                style "tooltip_style_elite"
                text_align 0.5
                xfill False
        else:
            text tooltip_text:
                style "tooltip_style"
                text_align 0.5
                xfill False

init -1 style tooltip_style:

    color "#FFFFFF"
    outlines [ (1, "#000", 0, 0) ]

    layout "subtitle"
    xalign 0.5
    yalign 0.5

init -1 style tooltip_style_elite is tooltip_style:
    font "SpecialElite.ttf"
    size int(gui.text_size * 1.1)



init -501 screen info_screen():
    layer 'screens'
    zorder 20
    if iface:
        frame:
            background "#0000002f"
            padding (5, 5)
            xalign 1.0 yalign 0.0
            text "[fcs.money]$   [ctime]":
                text_align 1.0 color "#ffffff" outlines [ (1, "#000", absolute(0), absolute(0)) ] yalign 0.5 style get_text_style()







        vbox:
            yalign .1
            xalign .99
            if preferences.language == "cn":
                vbox:
                    spacing -25
                    add "gui/i_energy.png"
                    text "[fcs.energy]" xalign .5 style "info_button_text"
                vbox:
                    spacing -25
                    add "gui/i_desire.png"
                    text "[fcs.desire]" xalign .5 style "info_button_text"
                vbox:
                    spacing -25
                    add "gui/i_looks.png"
                    text "[fcs.looks]" xalign .5 style "info_button_text"
            else:
                vbox:
                    spacing -25
                    add "gui/i_energy.png"
                    text "[fcs.energy]" xalign .5 style "elite_info_button_text"
                vbox:
                    spacing -25
                    add "gui/i_desire.png"
                    text "[fcs.desire]" xalign .5 style "elite_info_button_text"
                vbox:
                    spacing -25
                    add "gui/i_looks.png"
                    text "[fcs.looks]" xalign .5 style "elite_info_button_text"


        imagebutton:
            align (0.01, 0.01)
            idle "images/nav/ui/ic_start_idle.png"
            hover "images/nav/ui/ic_start_hover.png"
            action Show("character_menu")
            focus_mask True




init -1 style elite_info_button_text:
    color "#fff"
    hover_color "#ffd700"
    size 22
    outlines [(2, "#000", 1, 1)]
    font "SpecialElite.ttf"

init -1 style elite_hbox is default
init -1 style elite_vbox is default
init -1 style elite_frame is default

init -501 screen character_menu():
    zorder 50 tag charui
    modal True

    layer 'screens'
    if preferences.language != "cn":
        style_prefix "elite"
    add "images/nav/character_info/stats.png"
    if fcs.corruption < 20:
        add "images/nav/character_info/corr20.webp"
    elif fcs.corruption < 35:
        add "images/nav/character_info/corr35.webp"
    elif fcs.corruption < 49:
        add "images/nav/character_info/corr49.webp"
    elif fcs.corruption < 60:
        add "images/nav/character_info/corr60.webp"
    elif fcs.corruption < 70:
        add "images/nav/character_info/corr70.webp"
    elif fcs.corruption < 85:
        add "images/nav/character_info/corr85.webp"
    else:
        add "images/nav/character_info/corr100.webp"

    vbox:
        xpos 130 xanchor 0.5 yalign .04
        text get_local("conditions") outlines [ (1, "#000", absolute(0), absolute(0)) ]

    vbox:
        xpos 60 yanchor 0.0 ypos 90
        spacing 10
        if fcs.drunk_status == 1:
            imagebutton:
                idle "images/nav/character_info/Ic_drunk_sost_idle.png"
                hover "images/nav/character_info/Ic_drunk_sost_idle.png"
                action NullAction()
                tooltip get_local("status_drunk1")
                focus_mask True
        elif fcs.drunk_status == 2:
            imagebutton:
                idle "images/nav/character_info/Ic_drunk_sost_idle.png"
                hover "images/nav/character_info/Ic_drunk_sost_idle.png"
                action NullAction()
                tooltip get_local("status_drunk2")
                focus_mask True
        elif fcs.drunk_status == 3:
            imagebutton:
                idle "images/nav/character_info/Ic_drunk_sost_idle.png"
                hover "images/nav/character_info/Ic_drunk_sost_idle.png"
                action NullAction()
                tooltip get_local("status_drunk3")
                focus_mask True
        else:
            add "images/nav/character_info/Ic_drunk_sost_inactive.png" alpha .3

        if fcs.has_buff("health") < 0:
            imagebutton:
                idle "images/nav/character_info/Ic_sweat_sost_idle.png"
                hover "images/nav/character_info/Ic_sweat_sost_idle.png"
                action NullAction()
                tooltip f"{get_local('status_health')} {fcs.has_buff('health')}"
                focus_mask True
        else:
            add "images/nav/character_info/Ic_sweat_sost_inactive.png" alpha .3
        if fcs.desire == 9:
            imagebutton:
                idle "images/nav/character_info/Ic_aurosal_sost_idle.png"
                hover "images/nav/character_info/Ic_aurosal_sost_idle.png"
                action NullAction()
                tooltip get_local("status_arousal")
                focus_mask True
        else:
            add "images/nav/character_info/Ic_aurosal_sost_inactive.png" alpha .3
        if "insult" in fcs.vars:
            imagebutton:
                idle "images/nav/character_info/Ic_obida_sost_idle.png"
                hover "images/nav/character_info/Ic_obida_sost_idle.png"
                action NullAction()
                tooltip get_local("status_insult")
                focus_mask True
        else:
            add "images/nav/character_info/Ic_obida_sost_inactive.png" alpha .3
        if fcs.energy < 5:
            imagebutton:
                idle "images/nav/character_info/Ic_tied_sost_idle.png"
                hover "images/nav/character_info/Ic_tied_sost_idle.png"
                action NullAction()
                tooltip get_local("status_tired")
                focus_mask True
        else:
            add "images/nav/character_info/Ic_tied_sost_inactive.png" alpha .3
        if not fcs.s_check():
            imagebutton:
                idle "images/nav/character_info/Ic_after_sost_idle.png"
                hover "images/nav/character_info/Ic_after_sost_idle.png"
                action NullAction()
                tooltip get_local("status_overstimulated")
                focus_mask True
        else:
            add "images/nav/character_info/Ic_after_sost_inactive.png" alpha .3



    textbutton _("Персонаж") xanchor .5 xpos 550 yalign .087 action Show("character_menu")
    textbutton _("Отношения") xanchor .5 xpos 826 yalign .087 action Show("npc_info")
    textbutton _("Дневник") xanchor .5 xpos 1100 yalign .087 action Show("quest_log")
    textbutton _("Возможности") xanchor .5 xpos 1380 yalign .087 action Show("poss_menu")
    textbutton _("Закрыть") xanchor .5 xpos 1660 yalign .087 action Hide("character_menu")


    vbox:
        xanchor .0 xpos 300
        yalign .5
        spacing 15
        text f"{get_local('s_desire')} {fcs.desire}/{fcs.limits['desire'][1]} {get_buff_display('desire')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        text f"{get_local('s_intrigue')} {fcs.intrigue}/{fcs.limits['intrigue'][1]} {get_buff_display('intrigue')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        text f"{get_local('s_intelligence')} {fcs.intelligence}/{fcs.limits['intelligence'][1]} {get_buff_display('intelligence')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        text f"{get_local('s_corruption')} {fcs.corruption}/{fcs.limits['corruption'][1]} {get_buff_display('corruption')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        text f"{get_local('s_morality')} {fcs.morality}/{fcs.limits['morality'][1]} {get_buff_display('morality')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        text f"{get_local('s_energy')} {fcs.energy}/{fcs.limits['energy'][1]} {get_buff_display('energy')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        text f"{get_local('s_exg')} {fcs.exg}/{fcs.limits['exg'][1]} {get_buff_display('exg')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        if fcs.fitness > 0:
            text f"{get_local('s_fitness')} {fcs.fitness}/{fcs.limits['fitness'][1]} {get_buff_display('fitness')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        if fcs.submissive > 0:
            text f"{get_local('s_submissive')} {fcs.submissive}/{fcs.limits['submissive'][1]} {get_buff_display('submissive')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        if fcs.reputation > 0:
            text f"{get_local('s_reputation')} {fcs.reputation} {get_buff_display('submissive')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        text ""
        text f"{get_local('s_looks')} {fcs.looks}/{fcs.limits['looks'][1]} {get_buff_display('looks')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        text f"{get_local('s_style')} {fcs.style}/{fcs.limits['style'][1]} {get_buff_display('style')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()


    vbox:
        xanchor .0 xpos 1380
        yalign .5
        spacing 15
        if fcs.anal == 0:
            text f"{get_local('ass_stat')} {get_local('s_a_stat0')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        elif fcs.anal == 1:
            text f"{get_local('ass_stat')} {get_local('s_a_stat1')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        elif fcs.anal == 2:
            text f"{get_local('ass_stat')} {get_local('s_a_stat2')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        elif fcs.anal == 3:
            text f"{get_local('ass_stat')} {get_local('s_a_stat3')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        elif fcs.anal == 4:
            text f"{get_local('ass_stat')} {get_local('s_a_stat4')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        else:
            text f"{get_local('ass_stat')} {get_local('s_a_stat5')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()


        if fcs.minet == 1:
            text f"{get_local('blow_stat')} {get_local('s_m_stat1')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        elif fcs.minet == 2:
            text f"{get_local('blow_stat')} {get_local('s_m_stat2')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        elif fcs.minet == 3:
            text f"{get_local('blow_stat')} {get_local('s_m_stat3')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        else:
            text f"{get_local('blow_stat')} {get_local('s_m_stat4')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()

        if fcs.deep_minet == 0:
            text f"{get_local('deep_blow_stat')} {get_local('s_dm_stat0')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        elif fcs.deep_minet == 1:
            text f"{get_local('deep_blow_stat')} {get_local('s_dm_stat1')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        elif fcs.deep_minet == 2:
            text f"{get_local('deep_blow_stat')} {get_local('s_dm_stat2')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        else:
            text f"{get_local('deep_blow_stat')} {get_local('s_dm_stat3')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()

        text f"{get_local('s_streptease')} {fcs.strip}/{fcs.limits['strip'][1]}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        text f"{get_local('s_sex')} {fcs.s_exp}/{fcs.limits['s_exp'][1]}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()

        if fcs.drunk_status == 0:
            text f"{get_local('s_drunk')} {get_local('s_al_stat0')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        elif fcs.drunk_status == 1:
            text f"{get_local('s_drunk')} {get_local('s_al_stat1')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        elif fcs.drunk_status == 2:
            text f"{get_local('s_drunk')} {get_local('s_al_stat2')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        else:
            text f"{get_local('s_drunk')} {get_local('s_al_stat3')}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()
        if not prologue:
            text f"{get_local('s_cum')} {fcs.cum_count}/{fcs.limits['cum_count'][1]}" outlines [ (1, "#000", absolute(0), absolute(0)) ] style get_text_style()

    if difficulty == 'cheat':

        textbutton _("Отключить код подписчика"):
            align (0.95, 0.9)
            action Show("cheat_screen")
    else:
        textbutton _("Ввести код подписчика"):
            align (0.95, 0.9)
            action Show("cheat_screen")


    imagebutton:
        idle "gui/patreon_idle.png"
        hover "gui/patreon_hover.png"
        action OpenURL("https://www.patreon.com/c/novel/about")
        focus_mask True
        align (0.95, 0.99)

    $ tooltip = GetTooltip()

    if tooltip:
        use tooltip_screen(tooltip_text=tooltip, x_pos=0.2, y_pos=0.9   
        )





init -501 screen cheat_screen():
    zorder 100 tag cheat_ui
    modal True



    add "#000000" alpha 0.7


    frame:
        align (0.5, 0.5)
        xsize 400
        ysize 300

        has vbox
        align (0.5, 0.5)
        spacing 20

        if difficulty == "cheat":
            text _("Код подписчика активен") align (0.5, 0.0) style get_text_style()
            textbutton _("Выключить код подписчика"):
                align (0.5, 0.0)
                action [SetVariable("difficulty", "easy"), Hide("cheat_screen")]

        else:

            textbutton _("Ввести код подписчика"):
                align (0.5, 0.0)
                action [SetVariable("cheat_input_mode", True), Show("cheat_input_screen", prompt=_("Введите код:"))]


        textbutton _("Закрыть"):
            align (0.5, 0.0)
            action Hide("cheat_screen")



init -501 screen cheat_input_screen(prompt):
    style_prefix "input"
    zorder 101
    modal True


    add "#000000" alpha 0.7

    window:
        align (0.5, 0.5)
        has vbox
        xanchor gui.dialogue_text_xalign
        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos
        if preferences.language != "cn":
            text prompt style "input_elite_prompt"
        else:
            text prompt style "input_prompt"

        default input_text = ""
        input id "input" value ScreenVariableInputValue("input_text")


        if input_text == "L0ya1 Supporter":
            textbutton _("Подтвердить") action [
                    SetVariable("difficulty", "cheat"), 
                    Hide("cheat_input_screen"), 
                    Hide("cheat_screen")
                ]

        else:
            textbutton _("Подтвердить") action [
                    Hide("cheat_input_screen"), 
                    Show("cheat_error_screen")
                ]


init -501 screen cheat_error_screen():
    zorder 102
    modal True


    add "#000000" alpha 0.7


    frame:
        align (0.5, 0.5)
        xsize 400
        ysize 200

        has vbox
        align (0.5, 0.5)
        spacing 20

        text _("Неправильный код!") align (0.5, 0.0) style get_text_style()

        textbutton _("ОК"):
            align (0.5, 0.0)
            action [Hide("cheat_error_screen"), Show("cheat_screen")]




init -501 screen journal_menu():
    zorder 50
    modal True
    if preferences.language != "cn":
        style_prefix "elite"

    text _("В следующих версиях") align (0.5,0.5) style get_text_style()
    textbutton _("Выход") xanchor .5 xpos 1660 yalign .087 action Hide('journal_menu')



init -501 screen npc_info():
    tag charui
    layer 'screens'
    zorder 50
    modal True
    if preferences.language != "cn":
        style_prefix "elite"
    default selected_npc = None
    default current_page = 1
    default current_npc_list = npcs_list

    add "images/nav/npc_info/layer1.webp"

    if preferences.language != "cn":
        frame:
            background None
            xalign .03
            yanchor 0.0
            ypos 200
            has vbox
            spacing 30
            if selected_npc is not None:
                $ char_name = get_local(selected_npc.name)
                text char_name style "elite_npc_info_name_text"
                text ""
                for param in ("intrigue", "love", "fidelity", "cuckold", "s_power", "corruption", "free_relations", "desire", "s_approval", "love_fam"):
                    $ value = getattr(selected_npc, param)
                    if param in selected_npc.limits:
                        $ min_val, max_val = selected_npc.limits[param]
                    else:
                        $ min_val = ""
                        $ max_val = "20"
                    if value > 0:
                        $ param_name = get_local(f"npc_{param}")
                        if param == "love_fam" and (selected_npc.name == 'liliana' or selected_npc.name == 'samantha'):
                            hbox:
                                spacing 10
                                text _('Отношения с Тайлером') style "elite_npc_info_param_text"
                                text "[value]/[max_val]" style "elite_npc_info_value_text"
                        elif param == "love_fam" and selected_npc.name == 'justin':
                            hbox:
                                spacing 10
                                text _('Отношения с Шелли') style "elite_npc_info_param_text"
                                text "[value]/[max_val]" style "elite_npc_info_value_text"
                        elif param == "love_fam" and selected_npc.name == 'shelley':
                            hbox:
                                spacing 10
                                text _('Отношения с Джастином') style "elite_npc_info_param_text"
                                text "[value]/[max_val]" style "elite_npc_info_value_text"
                        elif param != "love_fam":
                            hbox:
                                spacing 10
                                text "[param_name]:" style "elite_npc_info_param_text"
                                text "[value]/[max_val]" style "elite_npc_info_value_text"
                    if value == 0 and param == "love" and selected_npc.name == 'tyler':
                        $ param_name = get_local(f"npc_{param}")
                        hbox:
                            spacing 10
                            text "[param_name]:" style "elite_npc_info_param_text"
                            text "[value]/[max_val]" style "elite_npc_info_value_text"
    else:
        frame:
            background None
            xalign .03
            yanchor 0.0
            ypos 200
            has vbox
            spacing 30
            if selected_npc is not None:
                $ char_name = get_local(selected_npc.name)
                text char_name style "npc_info_name_text"
                text ""
                for param in ("intrigue", "love", "fidelity", "cuckold", "s_power", "corruption", "free_relations", "desire", "s_approval", "love_fam"):
                    $ value = getattr(selected_npc, param)
                    if param in selected_npc.limits:
                        $ min_val, max_val = selected_npc.limits[param]
                    else:
                        $ min_val = ""
                        $ max_val = "20"
                    if value > 0:
                        $ param_name = get_local(f"npc_{param}")
                        if param == "love_fam" and (selected_npc.name == 'liliana' or selected_npc.name == 'samantha'):
                            hbox:
                                spacing 10
                                text _('Отношения с Тайлером') style "npc_info_param_text"
                                text "[value]/[max_val]" style "npc_info_value_text"
                        elif param == "love_fam" and selected_npc.name == 'justin':
                            hbox:
                                spacing 10
                                text _('Отношения с Шелли') style "npc_info_param_text"
                                text "[value]/[max_val]" style "npc_info_value_text"
                        elif param == "love_fam" and selected_npc.name == 'shelley':
                            hbox:
                                spacing 10
                                text _('Отношения с Джастином') style "npc_info_param_text"
                                text "[value]/[max_val]" style "npc_info_value_text"
                        elif param != "love_fam":
                            hbox:
                                spacing 10
                                text "[param_name]:" style "npc_info_param_text"
                                text "[value]/[max_val]" style "npc_info_value_text"
                    if value == 0 and param == "love" and selected_npc.name == 'tyler':
                        $ param_name = get_local(f"npc_{param}")
                        hbox:
                            spacing 10
                            text "[param_name]:" style "npc_info_param_text"
                            text "[value]/[max_val]" style "npc_info_value_text"

    if preferences.language != "cn":
        hbox:
            if preferences.language is None:
                xpos 745
                ypos 85
                spacing 0
            else:
                xpos 778
                ypos 85
                spacing 0
            for i in range(1, 4):
                textbutton _("Страница [i]"):
                    xalign 0.5
                    style "elite_npc_info_button"
                    action [
                        SetScreenVariable("current_page", i),
                        If(i == 1,
                            SetScreenVariable("current_npc_list", npcs_list),
                            If(i == 2,
                                SetScreenVariable("current_npc_list", npcs_list2),
                                If(i == 3,
                                    SetScreenVariable("current_npc_list", npcs_list3)
                                )
                            )
                        ),
                        SetScreenVariable("selected_npc", None)
                    ]
        textbutton _("Назад"):
            style "elite_npc_info_button"
            action [Hide("npc_info"), Show("character_menu")]
            xanchor 0.0
            xpos 1623
            ypos 85
    else:
        hbox:
            xanchor 0.0
            xpos 733
            ypos 85
            spacing 50
            xsize 900
            for i in range(1, 4):
                textbutton _("Страница [i]"):
                    xalign 0.5
                    style "npc_info_button"
                    action [
                        SetScreenVariable("current_page", i),
                        If(i == 1,
                            SetScreenVariable("current_npc_list", npcs_list),
                            If(i == 2,
                                SetScreenVariable("current_npc_list", npcs_list2),
                                If(i == 3,
                                    SetScreenVariable("current_npc_list", npcs_list3)
                                )
                            )
                        ),
                        SetScreenVariable("selected_npc", None)
                    ]
        textbutton _("Назад"):
            style "npc_info_button"
            action [Hide("npc_info"), Show("character_menu")]
            xanchor 0.0
            xpos 1623
            ypos 85

    frame:
        background None
        xalign 1.0
        yanchor 1.0
        yoffset 1014
        has grid 3 2
        xspacing 100
        yspacing 58
        for i in range(6):
            frame:
                background None
                xysize (350, 390)
                if i < len(current_npc_list):
                    $ npc = current_npc_list[i]
                    vbox:
                        spacing -80
                        imagebutton:
                            xysize (328, 390)
                            idle f"images/nav/npc_info/{npc.name}_idle.webp"
                            hover f"images/nav/npc_info/{npc.name}_hover.webp"
                            action SetScreenVariable("selected_npc", npc)

    add "images/nav/npc_info/layer2.webp"

    frame:
        background None
        xalign 1.0
        yanchor 1.0
        yoffset 1065
        has grid 3 2
        xspacing 100
        yspacing 58
        for i in range(6):
            frame:
                background None
                xysize (350, 390)
                if i < len(current_npc_list):
                    $ npc = current_npc_list[i]
                    vbox:
                        spacing -80
                        xysize (328, 390)
                        if preferences.language != "cn":
                            text get_local(npc.name):
                                style "elite_npc_info_text"
                                xalign 0.5
                                yalign .8
                        else:
                            text get_local(npc.name):
                                style "npc_info_text"
                                xalign 0.5
                                yalign .8



init -501 screen npc_info_tutorial():
    layer 'screens'
    zorder 10
    if preferences.language != "cn":
        style_prefix "elite"
    default selected_npc = None
    default current_npc_list = npcs_list

    add "images/nav/npc_info/layer1.webp"

    if preferences.language != "cn":
        frame:
            background None
            xalign .03
            yanchor 0.0
            ypos 200
            has vbox
            spacing 30
            if selected_npc is not None:
                $ char_name = get_local(selected_npc.name)
                text char_name style "elite_npc_info_name_text"
                text ""
                for param in ("intrigue", "love", "fidelity", "cuckold", "s_power", "corruption", "free_relations", "desire", "s_approval", "love_fam"):
                    $ value = getattr(selected_npc, param)
                    if param in selected_npc.limits:
                        $ min_val, max_val = selected_npc.limits[param]
                    else:
                        $ min_val = ""
                        $ max_val = "20"
                    if value > 0:
                        $ param_name = get_local(f"npc_{param}")
                        if param == "love_fam" and (selected_npc.name == 'liliana' or selected_npc.name == 'samantha'):
                            hbox:
                                spacing 10
                                text _('Отношения с Тайлером') style "elite_npc_info_param_text"
                                text "[value]/[max_val]" style "elite_npc_info_value_text"
                        elif param == "love_fam" and selected_npc.name == 'justin':
                            hbox:
                                spacing 10
                                text _('Отношения с Шелли') style "elite_npc_info_param_text"
                                text "[value]/[max_val]" style "elite_npc_info_value_text"
                        elif param == "love_fam" and selected_npc.name == 'shelley':
                            hbox:
                                spacing 10
                                text _('Отношения с Джастином') style "elite_npc_info_param_text"
                                text "[value]/[max_val]" style "elite_npc_info_value_text"
                        elif param != "love_fam":
                            hbox:
                                spacing 10
                                text "[param_name]:" style "elite_npc_info_param_text"
                                text "[value]/[max_val]" style "elite_npc_info_value_text"
    else:
        frame:
            background None
            xalign .03
            yanchor 0.0
            ypos 200
            has vbox
            spacing 30
            if selected_npc is not None:
                $ char_name = get_local(selected_npc.name)
                text char_name style "npc_info_name_text"
                text ""
                for param, (min_val, max_val) in selected_npc.limits.items():
                    $ value = getattr(selected_npc, param)
                    if param == "s_count":
                        pass
                    elif value > 0:
                        $ param_name = get_local(f"npc_{param}")
                        hbox:
                            spacing 10
                            text "[param_name]:" style "npc_info_param_text"
                            text "[value]/[max_val]" style "npc_info_value_text"

    if preferences.language != "cn":
        textbutton _("Назад"):
            style "elite_npc_info_button"
            action Hide("npc_info_tutorial")
            xanchor 0.0
            xpos 1623
            ypos 85
    else:
        textbutton _("Назад"):
            style "npc_info_button"
            action Hide("npc_info_tutorial")
            xanchor 0.0
            xpos 1623
            ypos 85

    frame:
        background None
        xalign 1.0
        yanchor 1.0
        yoffset 1014
        has grid 3 2
        xspacing 100
        yspacing 58
        for i in range(6):
            frame:
                background None
                xysize (350, 390)
                if i < len(current_npc_list):
                    $ npc = current_npc_list[i]
                    vbox:
                        spacing -80
                        imagebutton:
                            xysize (328, 390)
                            idle f"images/nav/npc_info/{npc.name}_idle.webp"
                            hover f"images/nav/npc_info/{npc.name}_hover.webp"
                            action SetScreenVariable("selected_npc", npc)

    add "images/nav/npc_info/layer2.webp"

    frame:
        background None
        xalign 1.0
        yanchor 1.0
        yoffset 1065
        has grid 3 2
        xspacing 100
        yspacing 58
        for i in range(6):
            frame:
                background None
                xysize (350, 390)
                if i < len(current_npc_list):
                    $ npc = current_npc_list[i]
                    vbox:
                        spacing -80
                        xysize (328, 390)
                        if preferences.language != "cn":
                            text get_local(npc.name):
                                style "elite_npc_info_text"
                                xalign 0.5
                                yalign .8
                        else:
                            text get_local(npc.name):
                                style "npc_info_text"
                                xalign 0.5
                                yalign .8





init -1 style npc_info_button:
    xminimum 235
    padding (10, 10)
    background "#0000"
    size 33



init -1 style npc_info_text:
    color "#fff"
    outlines [(2, "#000", 0, 0)]
    size 33

init -1 style npc_info_param_text is npc_info_text:
    size 29
    color "#ffd700"

init -1 style npc_info_value_text is npc_info_text:
    size 29
    color "#fff"

init -1 style npc_info_button_text:
    color "#fff"
    hover_color "#ffd700"
    size 25
    outlines [(2, "#000", 1, 1)]

init -1 style npc_info_name_text:
    color "#ffd700"
    size 34
    text_align 0.5
    outlines [(2, "#000", 0, 0)]

init -1 style info_button_text:
    color "#fff"
    hover_color "#ffd700"
    size 20
    outlines [(2, "#000", 1, 1)]


init -1 style elite_npc_info_button:
    font "SpecialElite.ttf"
    xsize 280

    background "#0000"
    size 33


init -1 style elite_npc_info_text:
    font "SpecialElite.ttf"
    color "#fff"
    outlines [(2, "#000", 0, 0)]
    size 33

init -1 style elite_npc_info_param_text is elite_npc_info_text:
    size 29
    color "#ffd700"

init -1 style elite_npc_info_value_text is elite_npc_info_text:
    size 29
    color "#fff"

init -1 style elite_npc_info_button_text:
    font "SpecialElite.ttf"
    color "#fff"
    hover_color "#ffd700"
    size 25
    outlines [(2, "#000", 1, 1)]

init -1 style elite_npc_info_name_text:
    font "SpecialElite.ttf"
    color "#ffd700"
    size 34
    text_align 0.5
    outlines [(2, "#000", 0, 0)]

init -1 style elite_info_button_text:
    font "SpecialElite.ttf"
    color "#fff"
    hover_color "#ffd700"
    size 20
    outlines [(2, "#000", 1, 1)]


init -501 screen dice_debug(value, min_value, max_value):
    modal True

    default dice_input_value = ""
    default entering_value = False

    frame:
        if preferences.language != "cn":
            style_prefix "elite_dice_debug"
        else:
            style_prefix "dice_debug"
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        vbox:
            spacing 20

            label _("Результат броска кубика"):
                xalign 0.5

            text _("{} ({}-{})").format(value, min_value, max_value):
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 20

                textbutton _("Принять"):
                    action Return(value)

                null width 50

                textbutton _("Ввести своё значение"):
                    action SetScreenVariable("entering_value", True)

            if entering_value:
                vbox:
                    spacing 10
                    xalign 0.5

                    label _("Введите значение:"):
                        xalign 0.5

                    hbox:
                        xalign 0.5

                        input:
                            value ScreenVariableInputValue("dice_input_value")
                            allow "0123456789"
                            length 5

                    textbutton _("Подтвердить"):
                        xalign 0.5
                        action Return(int(dice_input_value) if dice_input_value.strip() else value)

init -1 style dice_debug_frame:
    background "#222222"
    xalign 0.5
    yalign 0.5

init -1 style dice_debug_label_text:
    size 24

init -1 style dice_debug_text:
    size 36
    color "#ffcc00"

init -1 style dice_debug_button_text:
    size 22

init -1 style elite_dice_debug_frame is dice_debug_frame

init -1 style elite_dice_debug_label_text:
    font "SpecialElite.ttf"
    size 24

init -1 style elite_dice_debug_text:
    font "SpecialElite.ttf"
    size 36
    color "#ffcc00"

init -1 style elite_dice_debug_button_text:
    font "SpecialElite.ttf"
    size 22


init -501 screen fantasies_screen():
    default showing_fantasy = False


    if not showing_fantasy:
        imagebutton:
            idle "gui/ic_think_idle.png"
            hover "gui/ic_think_hover.png"
            action [SetScreenVariable("showing_fantasy", True), Show("fantasy_view", transition=dissolve)]
            tooltip get_local("icon_fant")
            align (.6, .1)


    if showing_fantasy and fantasies.should_close:
        timer 0.1 action [SetField(fantasies, "should_close", False), Return()]



init -501 screen fantasy_view():
    modal True
    if preferences.language != "cn":
        style_prefix "elite"

    if fantasies.is_finished:
        timer 0.1 action Show("fantasy_fin", transition=dissolve)


    imagebutton:
        idle "images/gradient.webp"
        hover "images/gradient.webp"
        action Function(fantasies.mark_as_finished)


    if len(fantasies.images) > 0 and fantasies.current_image_path:
        imagebutton:
            idle fantasies.current_image_path
            hover fantasies.current_image_path
            action If(
                fantasies.instruction_step > 0,
                Function(fantasies.advance_instruction),
                Function(fantasies.next_image)
            )
            align (0.5, 0.5)


    if preferences.language != "cn":
        if fantasies.instruction_step == 1:
            text get_local('fan_1') style "elite_fantasy_text"
        elif fantasies.instruction_step == 2:
            text get_local('fan_2') style "elite_fantasy_text"
        elif fantasies.instruction_step == 3:
            text get_local('fan_3') style "elite_fantasy_text"
        elif fantasies.instruction_step == 4:
            text get_local('fan_4') style "elite_fantasy_text"
    else:
        if fantasies.instruction_step == 1:
            text get_local('fan_1') style "fantasy_text"
        elif fantasies.instruction_step == 2:
            text get_local('fan_2') style "fantasy_text"
        elif fantasies.instruction_step == 3:
            text get_local('fan_3') style "fantasy_text"
        elif fantasies.instruction_step == 4:
            text get_local('fan_4') style "fantasy_text"





    on "show" action Function(fantasies.reset)


    timer 1.0 repeat True action Function(fantasies.decrease_timer)


init -501 screen fantasy_fin():
    modal True
    add "images/gradient.webp"


    if fantasies.fin and fantasies.fin_image_path:
        add fantasies.fin_image_path align (0.5, 0.5)

    timer 2.0 action [
        Function(fantasies.clear), 
        Hide("fantasy_fin"), 
        Hide("fantasy_view"), 
        Function(fantasies.mark_for_closing)
    ]

init -501 screen fantasies_screen_1():


    imagebutton:
        idle "gui/ic_think_idle.png"
        hover "gui/ic_think_hover.png"
        action [SetScreenVariable("showing_fantasy", True), Hide('fantasies_screen_1'), Show("fantasy_view_1", transition=dissolve)]
        align (.6, .1)






init -501 screen fantasy_view_1():
    zorder 200
    modal True


    imagebutton:
        idle "images/gradient.webp"
        hover "images/gradient.webp"
        action [Hide("fantasy_view_1"), Return()]


    imagebutton:
        idle fantasies.fin
        hover fantasies.fin
        action [Hide("fantasy_view_1"), Return()]
        align (0.5, 0.5)


init -1 style fantasy_text:
    size 29
    color "#ffffff"
    text_align 0.5
    align (.5, .1)
    background "#8888883c"
    outlines [(2, "#000000", 0, 0)]
    xmaximum 1000

init -1 style elite_fantasy_text:
    size 32
    color "#ffffff"
    text_align 0.5
    align (.5, .1)
    background "#8888883c"
    outlines [(2, "#000000", 0, 0)]
    xmaximum 1000
    font "SpecialElite.ttf"



init -1 style quest_vscrollbar is vscrollbar:
    thumb "images/nav/phone/scroll_bar.png"
    background None


init -501 screen toggle_dict_button(dict, key):
    if preferences.language != "cn":
        style_prefix "elite"
    if dict[key]:
        textbutton get_local("collapse") action ToggleDict(dict, key, True, False) xsize 30 text_color "#fff" style "category_toggle_button"
    else:
        textbutton get_local("expand") action ToggleDict(dict, key, False, True) xsize 30 text_color "#fff" style "category_toggle_button"

init -501 screen toggle_field_button(quest):
    if preferences.language != "cn":
        style_prefix "elite"
    if quest.expanded:
        textbutton get_local("collapse") action ToggleField(quest, "expanded") xsize 20 text_color "#fff" style "quest_toggle_button"
    else:
        textbutton get_local("expand") action ToggleField(quest, "expanded") xsize 20 text_color "#fff" style "quest_toggle_button"


init -501 screen quest_log():
    modal True tag charui

    layer 'screens'
    zorder 50
    if preferences.language != "cn":
        style_prefix "elite"

    default categories_expanded = {"main": True, "character": True, "quest": True, "work": True}
    key "mouseup_4" action NullAction()
    key "mouseup_5" action NullAction()
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()


    add "images/nav/phone/dnev_fon.png"


    frame:
        background None
        xsize 1800
        ysize 1000

        vbox:
            xfill True
            yfill True
            spacing 20


            fixed:

                viewport id "quest_viewport":
                    mousewheel "vertical"
                    scrollbars None
                    xsize 1500 xpos 250

                    has vbox
                    spacing 20
                    xfill True


                    label get_local("quest_log_title"):
                        xalign 0.5
                        text_size 60


                    if any(quest.stage > 0 for quest in main_quests):
                        null height 20
                        frame:
                            background None
                            xfill True
                            has vbox
                            spacing 15
                            if preferences.language != "cn":
                                text _("На перекрестке:") style "elite_quest_title_text"
                            else:
                                text _("На перекрестке:") style "quest_title_text"
                            xfill True

                            if categories_expanded["main"]:
                                for quest in main_quests:
                                    if quest.stage > 0:
                                        frame:
                                            background None
                                            xfill True
                                            has vbox

                                            hbox:
                                                spacing 15
                                                xalign 0.0
                                                use toggle_field_button(quest)
                                                null height 20
                                                text quest.name:
                                                    style get_quest_name_style(quest)
                                                    xalign 0.0
                                                null height 20
                                                if quest.completed:
                                                    if preferences.language != "cn":
                                                        text get_local("completed"):
                                                            style "elite_completed_text"
                                                            xalign 1.0
                                                    else:
                                                        text get_local("completed"):
                                                            style "completed_text"
                                                            xalign 1.0

                                            if quest.expanded:
                                                $ stage_text = get_quests_local(quest.quest_id, quest.stage)
                                                if stage_text:
                                                    hbox:
                                                        xoffset 80
                                                        spacing 15
                                                        text stage_text:
                                                            style get_quest_description_style(quest)
                                                            xalign 0.0
                                                            xmaximum 1400


                    if any(quest.stage > 0 for quest in character_quests):
                        null height 20
                        frame:
                            background None
                            xfill True
                            has vbox
                            spacing 10
                            xfill True
                            hbox:
                                spacing 15
                                xalign 0.0
                                use toggle_dict_button(dict=categories_expanded, key="character")
                                null height 20
                                if preferences.language != "cn":
                                    text get_local("quest_category_character"):
                                        style "elite_quest_title_text"
                                        xalign 0.0
                                else:
                                    text get_local("quest_category_character"):
                                        style "quest_title_text"
                                        xalign 0.0

                            if categories_expanded["character"]:
                                for quest in character_quests:
                                    if quest.stage > 0:
                                        frame:
                                            background None
                                            xfill True
                                            has vbox
                                            hbox:
                                                spacing 15
                                                xalign 0.0
                                                use toggle_field_button(quest)
                                                null height 20
                                                text quest.name:
                                                    style get_quest_name_style(quest)
                                                    xalign 0.0
                                                if quest.completed:
                                                    if preferences.language != "cn":
                                                        text get_local("completed"):
                                                            style "elite_completed_text"
                                                            xalign 1.0
                                                    else:
                                                        text get_local("completed"):
                                                            style "completed_text"
                                                            xalign 1.0
                                            if quest.expanded:
                                                for stage in quest.data_list:
                                                    $ stage_text = get_quests_local(quest.quest_id, stage)
                                                    if stage_text:
                                                        null height 20
                                                        hbox:
                                                            xoffset 80
                                                            spacing 15
                                                            text stage_text:
                                                                style get_quest_description_style(quest)
                                                                xalign 0.0
                                                                xmaximum 1400



                    if any(quest.stage > 0 for quest in quest_quests):
                        null height 20
                        frame:
                            background None
                            xfill True
                            has vbox
                            spacing 10
                            xfill True
                            hbox:
                                spacing 15
                                xalign 0.0
                                use toggle_dict_button(dict=categories_expanded, key="quest")
                                null height 20
                                if preferences.language != "cn":
                                    text get_local("quest_category_quest"):
                                        style "elite_quest_title_text"
                                        xalign 0.0
                                else:
                                    text get_local("quest_category_quest"):
                                        style "quest_title_text"
                                        xalign 0.0

                            if categories_expanded["quest"]:
                                for quest in quest_quests:
                                    if quest.stage > 0:
                                        frame:
                                            background None
                                            xfill True
                                            has vbox
                                            hbox:
                                                spacing 15
                                                xalign 0.0
                                                use toggle_field_button(quest)
                                                null height 20
                                                text quest.name:
                                                    style get_quest_name_style(quest)
                                                    xalign 0.0
                                                if quest.completed:
                                                    if preferences.language != "cn":
                                                        text get_local("completed"):
                                                            style "elite_completed_text"
                                                            xalign 1.0
                                                    else:
                                                        text get_local("completed"):
                                                            style "completed_text"
                                                            xalign 1.0
                                            if quest.expanded:
                                                for stage in quest.data_list:
                                                    $ stage_text = get_quests_local(quest.quest_id, stage)
                                                    if stage_text and stage_text != quest.name:
                                                        null height 20
                                                        hbox:
                                                            xoffset 80
                                                            spacing 15
                                                            text stage_text:
                                                                style get_quest_description_style(quest)
                                                                xalign 0.0
                                                                xmaximum 1400


                    if any(quest.stage > 0 for quest in work_quests):
                        null height 20
                        frame:
                            background None
                            xfill True
                            has vbox
                            spacing 10
                            xfill True
                            hbox:
                                spacing 5
                                xalign 0.0
                                use toggle_dict_button(dict=categories_expanded, key="work")
                                null height 20
                                if preferences.language != "cn":
                                    text get_local("quest_category_work"):
                                        style "elite_quest_title_text"
                                        xalign 0.0
                                else:
                                    text get_local("quest_category_work"):
                                        style "quest_title_text"
                                        xalign 0.0

                            if categories_expanded["work"]:
                                for quest in work_quests:
                                    if quest.stage > 0:
                                        frame:
                                            background None
                                            xfill True
                                            has vbox
                                            hbox:
                                                spacing 15
                                                xalign 0.0
                                                use toggle_field_button(quest)
                                                null height 20
                                                text quest.name:
                                                    style get_quest_name_style(quest)
                                                    xalign 0.0
                                                if quest.completed:
                                                    if preferences.language != "cn":
                                                        text get_local("completed"):
                                                            style "elite_completed_text"
                                                            xalign 1.0
                                                    else:
                                                        text get_local("completed"):
                                                            style "completed_text"
                                                            xalign 1.0

                                            if quest.expanded:
                                                for stage in quest.data_list:
                                                    $ stage_text = get_quests_local(quest.quest_id, stage)
                                                    if stage_text:
                                                        null height 20
                                                        hbox:
                                                            xoffset 80
                                                            spacing 15
                                                            text stage_text:
                                                                style get_quest_description_style(quest)
                                                                xalign 0.0
                                                                xmaximum 1400


            textbutton _("Закрыть"):
                xalign 0.5
                action [Function(reset_all_notifications), Show("character_menu")]


        bar:
            value YScrollValue("quest_viewport")
            xsize 45
            ysize 900
            xpos 93
            ypos 50
            style "quest_vscrollbar"






init -1 style category_toggle_button:
    size 42
    bold True


init -1 style quest_toggle_button:
    size 33
    bold True


init -1 style quest_title_text:
    size 42

    color "#fff"

init -1 style quest_name_text:
    size 36
    color "#ffffff"

init -1 style quest_name_notification_text:
    size 36
    color "#ffff00"

init -1 style quest_name_completed_text:
    size 36
    color "#aaaaaa"

init -1 style quest_description_text:
    size 33
    color "#ffffff"

init -1 style quest_description_notification_text:
    size 33
    color "#ffff00"

init -1 style quest_description_completed_text:
    size 33
    color "#aaaaaa"

init -1 style completed_text:
    size 33
    color "#aaaaaa"

init -1 style elite_category_toggle_button:
    font "SpecialElite.ttf"
    size 42
    bold True

init -1 style elite_quest_toggle_button:
    font "SpecialElite.ttf"
    size 33
    bold True

init -1 style elite_quest_title_text:
    font "SpecialElite.ttf"
    size 42
    bold True
    color "#fff"

init -1 style elite_quest_name_text:
    font "SpecialElite.ttf"
    size 36
    color "#ffffff"

init -1 style elite_quest_name_notification_text:
    font "SpecialElite.ttf"
    size 36
    color "#ffff00"

init -1 style elite_quest_name_completed_text:
    font "SpecialElite.ttf"
    size 36
    color "#aaaaaa"

init -1 style elite_quest_description_text:
    font "SpecialElite.ttf"
    size 33
    color "#ffffff"

init -1 style elite_quest_description_notification_text:
    font "SpecialElite.ttf"
    size 33
    color "#ffff00"

init -1 style elite_quest_description_completed_text:
    font "SpecialElite.ttf"
    size 33
    color "#aaaaaa"

init -1 style elite_completed_text:
    font "SpecialElite.ttf"
    size 33
    color "#aaaaaa"


init -501 screen poss_menu():
    if preferences.language != "cn":
        style_prefix "elite"
    modal True tag charui

    layer 'screens'
    zorder 50

    key "mouseup_4" action NullAction()
    key "mouseup_5" action NullAction()
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()


    add "images/nav/phone/dnev_fon.png"


    frame:
        background None
        xsize 1800
        ysize 1000

        vbox:
            xfill True
            yfill True
            spacing 20


            fixed:

                viewport id "possibilities_viewport":
                    mousewheel "vertical"
                    scrollbars None
                    xsize 1500 xpos 250

                    has vbox
                    spacing 20
                    xfill True


                    label get_local("possibilities_log_title"):
                        xalign 0.5
                        text_size 60


                    if any(poss.stage > 0 for poss in poss_quests):
                        null height 20
                        frame:
                            background None
                            xfill True
                            has vbox
                            spacing 10
                            if preferences.language != "cn":
                                text _("Возможности:") style "elite_quest_title_text"
                            else:
                                text _("Возможности:") style "quest_title_text"
                            xfill True

                            for poss in poss_quests:
                                if poss.stage > 0:

                                    vbox:
                                        spacing 5
                                        xfill True

                                        text " "
                                        hbox:
                                            spacing 5
                                            xalign 0.0
                                            text " "
                                            text poss.name:
                                                style get_text_style()
                                                xalign 0.0
                                            if poss.completed:
                                                if preferences.language != "cn":
                                                    text get_local("completed"):
                                                        style "elite_completed_text"
                                                        xalign 1.0
                                                else:
                                                    text get_local("completed"):
                                                        style "completed_text"
                                                        xalign 1.0


                                        for stage_item in poss.data_list:

                                            hbox:
                                                xoffset 30
                                                spacing 5

                                                text get_quests_local(poss.quest_id, stage_item):
                                                    style get_text_style()
                                                    xalign 0.0




            textbutton _("Закрыть"):
                xalign 0.5
                action [Function(reset_poss_notifications), Show("character_menu")]


        bar:
            value YScrollValue("possibilities_viewport")
            xsize 45
            ysize 900
            xpos 93
            ypos 50
            style "quest_vscrollbar"


init -501 screen phone_chat(chat, x=0.5, y=0.5):



    frame:
        background "images/nav/phone/phone.png"
        align (x, y)
        xsize 478
        ysize 1000


        frame:
            style "chat_header_frame"
            text chat.get_current_other_name():
                style "chat_header_text"


        frame:
            background None
            xsize 400
            ysize 780
            xpos 30
            ypos 100


            has vbox
            spacing 10
            xsize 390


            for message in chat.messages:

                if message["is_player"]:
                    frame:
                        style "player_message_frame"

                        has vbox
                        spacing 5


                        if message["text"]:
                            text message["text"]:
                                style "message_text"


                        if message["image"]:
                            add message["image"]
                else:
                    frame:
                        style "other_message_frame"

                        has vbox
                        spacing 5


                        if message["text"]:
                            text message["text"]:
                                style "message_text"


                        if message["image"]:
                            add message["image"]:
                                at transform:
                                    zoom 0.5

init -1 style player_message_frame:
    background "#b77cff60"
    padding (5, 5)
    xalign 1.0
    xmaximum 350

init -1 style elite_player_message_frame is player_message_frame



init -1 style other_message_frame:
    background "#82b9f960"
    padding (5, 5)
    xalign 0.0
    xmaximum 350

init -1 style elite_other_message_frame is other_message_frame


init -1 style message_text:
    size 20
    color "#ffffff"

    layout "subtitle"

init -1 style elite_message_text:
    size 20
    color "#ffffff"
    font "DejaVuSans.ttf"
    layout "subtitle"


init -1 style chat_header_frame:
    background None
    xsize 478
    ysize 80
    ypos 20

init -1 style elite_chat_header_frame is chat_header_frame


init -1 style chat_header_text:
    color "#FFFFFF"
    size 28
    align (0.1, 0.5)


init -1 style elite_chat_header_text:
    color "#FFFFFF"
    size 28
    font "DejaVuSans.ttf"
    align (0.1, 0.5)

init -501 screen font_menu():
    if preferences.language != "cn":
        style_prefix "elite"

    modal True tag menu
    add "#3f3f3f"
    add "gradient"
    frame:
        background None
        xalign 0.5 yalign 0.5
        has vbox
        xsize 1300
        spacing 20
        text _("Пример текущего шрифта диалога. Выберите другой, если хотите:") style "say_dialogue" xalign 0.5

        text " "
        text " "

        textbutton _("{font=PTC55F.ttf}Обычный{/font}") action StylePreference("dialog_font", "FontPTC55F") xalign 0.5 text_size 30
        textbutton _("{font=PTS56F.ttf}Курсив{/font}") action StylePreference("dialog_font", "FontPTS56F") xalign 0.5 text_size 32
        textbutton _("{font=SpecialElite.ttf}Красивый{/font}") action StylePreference("dialog_font", "FontSpecialElite") xalign 0.5 text_size 35
        text " "
        text " "
        text " "
        textbutton _("Принять и выйти") action [Hide("font_menu"), Return()] xalign 1.0 text_size 30


init -501 screen gallery_menu():
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
            if persistent.gal1:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_gal_1_idle.png"
                    hover "images/nav/gallery/ic_husb_gal_1_hover.png"
                    action [SetVariable('replay_label','prologue_house_sex'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal2:
                imagebutton:
                    idle "images/nav/gallery/ic_dgast_gal_1_idle.png"
                    hover "images/nav/gallery/ic_dgast_gal_1_hover.png"
                    action [SetVariable('replay_label','prologue_day2_problem_0'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal3:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_gal_2_idle.png"
                    hover "images/nav/gallery/ic_husb_gal_2_hover.png"
                    action [SetVariable('replay_label','gallery3'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal4:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_gal_3_idle.png"
                    hover "images/nav/gallery/ic_husb_gal_3_hover.png"
                    action [SetVariable('replay_label','gallery4'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

        hbox:
            spacing 45
            xalign 0.0
            if persistent.gal5:
                imagebutton:
                    idle "images/nav/gallery/ic_boss_gal_1_idle.png"
                    hover "images/nav/gallery/ic_boss_gal_1_hover.png"
                    action [SetVariable('replay_label','prologue_day3_work_meet_boss'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal6:
                imagebutton:
                    idle "images/nav/gallery/ic_djast_1_idle.png"
                    hover "images/nav/gallery/ic_djast_1_hover.png"
                    action [SetVariable('replay_label','prologue_ep2_emma_mast'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal7:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_gal_4_idle.png"
                    hover "images/nav/gallery/ic_husb_gal_4_hover.png"
                    action [SetVariable('replay_label','prologue_ep2_emma_mast2'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal9:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_gard_1_idle.png"
                    hover "images/nav/gallery/ic_husb_gard_1_hover.png"
                    action [SetVariable('replay_label','day4_justin_shelley_sex_tyler'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'


        hbox:
            spacing 45
            xalign 0.0
            if persistent.gal8:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_photo_1_idle.png"
                    hover "images/nav/gallery/ic_husb_photo_1_hover.png"
                    action [SetVariable('replay_label','day4_studio2_gallery'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal10:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_lake_1_idle.png"
                    hover "images/nav/gallery/ic_husb_lake_1_hover.png"
                    action [SetVariable('replay_label','day5_lake_sex_gal'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal11:
                imagebutton:
                    idle "images/nav/gallery/ic_husb_maid_idle.png"
                    hover "images/nav/gallery/ic_husb_maid_hover.png"
                    action [SetVariable('replay_label','day11_poss_4_gal11'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'

            if persistent.gal12:
                imagebutton:
                    idle "images/nav/gallery/ic_peep_1_idle.png"
                    hover "images/nav/gallery/ic_peep_1_hover.png"
                    action [SetVariable('replay_label','quest_watcher_4_play'), Start("replay_start")]
            else:
                add 'images/nav/gallery/ic_question.png'















init -501 screen achievement_menu():
    if preferences.language != "cn":
        style_prefix "elite"

    modal True tag menu
    add 'images/nav/gallery/gallery.png'

    textbutton _("Галерея") xanchor .5 xpos 550 yalign .087 action ShowMenu("gallery_menu")
    textbutton _("Ачивки") xanchor .5 xpos 820 yalign .087 action ShowMenu("achievement_menu")
    textbutton _("Карты") xanchor .5 xpos 1100 yalign .087 action ShowMenu("cards_menu")
    textbutton _("Выход") xanchor .5 xpos 1380 yalign .087 action ShowMenu("main_menu")

    text _("В следующих версиях") xalign .5 yalign .5 style get_text_style()

init -501 screen cards_menu():
    if preferences.language != "cn":
        style_prefix "elite"

    modal True tag menu
    add 'images/nav/gallery/gallery.png'

    textbutton _("Галерея") xanchor .5 xpos 550 yalign .087 action ShowMenu("gallery_menu")
    textbutton _("Ачивки") xanchor .5 xpos 820 yalign .087 action ShowMenu("achievement_menu")
    textbutton _("Карты") xanchor .5 xpos 1100 yalign .087 action ShowMenu("cards_menu")
    textbutton _("Выход") xanchor .5 xpos 1380 yalign .087 action ShowMenu("main_menu")

    text _("В следующих версиях") xalign .5 yalign .5 style get_text_style()



init -501 screen universal_shop(title, items):
    tag menu
    if preferences.language == "cn":
        style_prefix "choice"
    else:
        style_prefix "choice_elite"



    layer 'screens'
    zorder 50
    default local_title = get_local(title)


    frame:
        padding (40, 40)
        xalign 0.5
        yalign 0.5


        has vbox
        spacing 20
        xalign .5

        text local_title:
            style get_text_style()
            outlines [(2, "#000000ff", 1, 1)]
            xalign 0.5
            size gui.text_size * 1.25

        text _("Деньги: [fcs.money:,.0f]"):
            style get_text_style()
            outlines [(2, "#000000ff", 1, 1)]



        if len(items) > 6:

            viewport:
                id "shop_vp"
                draggable True
                mousewheel True
                align (.5, .5)
                xsize 1150
                ymaximum 800

                has vbox
                xalign 0.5
                spacing 10

                for item in items:
                    python:
                        item_purchased = item.name in fcs.inv
                        has_enough_money = fcs.money >= item.price
                        condition_met = renpy.eval(item.condition) if item.condition else True
                        can_buy_now = has_enough_money and condition_met and not item_purchased
                        cannot_buy_reason_condition = not condition_met and not item_purchased
                        cannot_buy_reason_money = not has_enough_money and condition_met and not item_purchased
                        if item_purchased or (not item_purchased and (not has_enough_money or not condition_met)):
                            current_text_color = "#888888"
                        else:
                            current_text_color = "#ffffff" 

                    button:
                        action If(can_buy_now, Function(buy_item, item), NullAction())
                        sensitive can_buy_now
                        xfill True

                        has hbox
                        spacing 10
                        vbox:
                            xfill True
                            spacing 2
                            text get_local(item.name):
                                color current_text_color
                            text f"({get_local(item.description)})":
                                color current_text_color
                            if cannot_buy_reason_condition:
                                text _("Требуется: [item.condition!t]"):
                                    size -2
                                    color "#aaaaaa"
                        vbox:
                            xalign 1.0
                            yalign 0.5
                            if item_purchased:
                                text "{b}✓{/b}":
                                    color "#0f9200ff"
                            else:
                                text "${:,}".format(item.price):
                                    color current_text_color



        else:
            vbox:
                xalign 0.5
                spacing 10

                for item in items:
                    python:
                        item_purchased = item.name in fcs.inv
                        has_enough_money = fcs.money >= item.price
                        condition_met = renpy.eval(item.condition) if item.condition else True
                        can_buy_now = has_enough_money and condition_met and not item_purchased
                        cannot_buy_reason_condition = not condition_met and not item_purchased
                        cannot_buy_reason_money = not has_enough_money and condition_met and not item_purchased
                        if item_purchased or (not item_purchased and (not has_enough_money or not condition_met)):
                            current_text_color = "#888888"
                        else:
                            current_text_color = "#ffffff" 

                    button:
                        action If(can_buy_now, Function(buy_item, item), NullAction())
                        sensitive can_buy_now
                        xfill True

                        has hbox
                        spacing 10
                        vbox:
                            xfill True
                            spacing 2
                            text get_local(item.name):
                                color current_text_color
                            text f"({get_local(item.description)})":
                                color current_text_color
                            if cannot_buy_reason_condition:
                                text _("Требуется: [item.condition!t]"):
                                    size -2
                                    color "#aaaaaa"
                        vbox:
                            xalign 1.0
                            yalign 0.5
                            if item_purchased:
                                text "{b}✓{/b}":
                                    color "#0f9200ff"
                            else:
                                text "${:,}".format(item.price):
                                    color current_text_color


        button:
            action Return()
            xfill True
            text get_local("shop_exit"):
                xalign 0.5

    if len(items) > 6:
        vbar:
            value YScrollValue("shop_vp")
            xalign .17
            yalign .55
            ysize .72
            xsize 15


init -501 screen pc_desktop():
    zorder 50
    modal True
    add "nav/pc/pc_desktop.webp"















    hbox:
        xpos 100 ypos 100
        spacing 20


        vbox:
            spacing -20
            imagebutton:
                idle "nav/pc/ic_money_idle.webp"
                hover "nav/pc/ic_money_hover.webp"
                action Show("pc_finances")
            text _("Финансы"):
                outlines [(1, "#000000", 0, 0)]
                color "#ffffff"
                size 20
                xalign 0.5


        vbox:
            spacing -20
            imagebutton:
                idle "nav/pc/ic_item_idle.webp"
                hover "nav/pc/ic_item_hover.webp"
                action Show("pc_inventory")
            text _("Инвентарь"):
                outlines [(1, "#000000", 0, 0)]
                color "#ffffff"
                size 20
                xalign 0.5


        vbox:
            spacing -20
            imagebutton:
                idle "nav/pc/ic_achievement_idle.webp"
                hover "nav/pc/ic_achievement_hover.webp"
                action NullAction()
            text _("Достижения"):
                outlines [(1, "#000000", 0, 0)]
                color "#ffffff"
                size 20
                xalign 0.5


        vbox:
            spacing -20
            imagebutton:
                idle "nav/pc/ic_video_idle.webp"
                hover "nav/pc/ic_video_hover.webp"
                action NullAction()
            text _("Мои видеозаписи"):
                outlines [(1, "#000000", 0, 0)]
                color "#ffffff"
                size 20
                xalign 0.5

    vbox:
        xalign .95
        yalign .95
        spacing -20
        imagebutton:
            idle "nav/pc/ic_off_idle.webp"
            hover "nav/pc/ic_off_hover.webp"
            action Hide("pc_desktop")
        text _("Завершить работу"):
            outlines [(1, "#000000", 0, 0)]
            color "#ffffff"
            size 20
            xalign 0.5



init -501 screen pc_finances():
    zorder 51
    modal True


    frame:
        xalign 0.5 yalign 0.5
        xsize 1400 ysize 800
        background "#f0f0f0"

        vbox:

            frame:
                xfill True
                ysize 40
                background "#d0d0d0"

                text _("Финансовый менеджер") color "#000000" size 20 yalign 0.5 xalign .02






            frame:
                xfill True yfill True
                background "#ffffff"
                left_padding 20 right_padding 20 top_padding 20 bottom_padding 20

                has vbox
                spacing 20


                text _("Общий баланс: $[fcs.money]") size 28 color "#000000" bold True


                frame:
                    xfill True ysize 2
                    background "#cccccc"

                hbox:
                    spacing 50


                    vbox:
                        xsize 600
                        text _("ДОХОДЫ") size 24 color "#008000" bold True

                        frame:
                            xfill True ysize 2
                            background "#008000"

                        null height 10

                        python:
                            active_incomes = revenues.get_active_incomes()

                        for name, amount in active_incomes:
                            hbox:
                                text "[name]:" size 18 color "#000000"
                                text "$ [amount]" size 18 color "#008000" xalign 1.0

                        null height 20


                        frame:
                            xfill True ysize 1
                            background "#cccccc"

                        hbox:
                            text _("ИТОГО ДОХОДОВ:") size 20 color "#000000" bold True
                            text "$[revenues.get_total_income()]" size 20 color "#008000" bold True xalign 1.0


                    vbox:
                        xsize 600
                        text _("РАСХОДЫ") size 24 color "#cc0000" bold True

                        frame:
                            xfill True ysize 2
                            background "#cc0000"

                        null height 10

                        python:
                            active_spendings = revenues.get_active_spendings()

                        for name, amount in active_spendings:
                            hbox:
                                text "[name]:" size 18 color "#000000"
                                text "$[amount]" size 18 color "#cc0000" xalign 1.0

                        null height 20


                        frame:
                            xfill True ysize 1
                            background "#cccccc"

                        hbox:
                            text _("ИТОГО РАСХОДОВ:") size 20 color "#000000" bold True
                            text "$[revenues.get_total_spending()]" size 20 color "#cc0000" bold True xalign 1.0


                null height 30

                frame:
                    xfill True ysize 3
                    background "#000000"

                python:
                    balance = revenues.get_balance()
                    balance_color = "#008000" if balance >= 0 else "#cc0000"

                hbox:
                    text _("ЧИСТЫЙ ДОХОД:") size 26 color "#000000" bold True
                    text "$[balance]" size 26 color balance_color bold True xalign 1.0

        textbutton "x":
            action Hide("pc_finances")
            xalign .99
            yalign .0
            text_color "#000000"
            text_size 22



init -501 screen pc_inventory():
    zorder 51
    modal True


    add "nav/pc/pc_file_manager.webp"
    text _("Инвентарь") color "#000000" size 20 xpos .102 ypos .065
    textbutton "x":
        action Hide("pc_inventory")
        xpos .855 ypos .06
        text_color "#000000"
        text_size 22


    frame:
        xpos 574 ypos 220
        xsize 1085 ysize 740
        background "#23232327"

        has vbox


















        frame:
            xfill True yfill True
            background "#05050518"
            left_padding 20 right_padding 20 top_padding 20 bottom_padding 20

            has vbox
            text _("Инвентарь пуст") size 22 color "#666666" xalign 0.5 yalign 0.5

init -501 screen think_button_screen(image_path):

    imagebutton:
        idle "gui/ic_think_idle.png"
        hover "gui/ic_think_hover.png"
        action Show("modal_image_screen", image_to_show=image_path)
        align (0.6, 0.1)


init -501 screen modal_image_screen(image_to_show):
    modal True


    imagebutton:
        idle "images/gradient.webp"
        hover "images/gradient.webp"
        action [Hide("modal_image_screen"), Hide("think_button_screen")]

    add image_to_show:
        xalign 0.5
        yalign 0.5
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
