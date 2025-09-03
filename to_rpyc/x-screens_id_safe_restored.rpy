init offset = -1











style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















screen say(who, what):
    style_prefix "mengatakan"

    window:
        id "jendela"

        if who is not None:

            window:
                id "NameBox"
                style "namebox"
                text who id "who"

        text what id "what"




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos












screen input(prompt):
    style_prefix "masukan"

    window:

        has vbox
        xalign gui.dialogue_text_xalign
        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "masukan"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










screen choice(items):
    style_prefix "pilihan"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")







screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            style_prefix "cepat"

            xalign 0.5
            yalign 1.0

            textbutton _("Kembali") action Rollback()
            textbutton _("Sejarah") action ShowMenu('history')
            textbutton _("Melewati") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Mobil") action Preference("auto-forward", "toggle")
            textbutton _("Menyimpan") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')




init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")











screen navigation():

    vbox:
        style_prefix "navigasi"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Awal") action Start()
            textbutton _("{color=#f00}Support My Patreon{/color}") action OpenURL("http://www.patreon.com/SerialNumberComics")
        else:
            textbutton _("Sejarah") action ShowMenu("history")
            textbutton _("Menyimpan") action ShowMenu("save")

        textbutton _("Memuat") action ShowMenu("load")
        textbutton _("Preferensi") action ShowMenu("preferences")
        
        # Gallery buttons
        textbutton _("Galeri") action ShowMenu("gallery")
        textbutton _("Galeri 1") action ShowMenu("gallery1")
        textbutton _("Galeri 2") action ShowMenu("gallery2")
        textbutton _("Galeri 3") action ShowMenu("gallery3")
        textbutton _("Galeri 4") action ShowMenu("gallery6")
        textbutton _("Galeri 5") action ShowMenu("gallery7")
        textbutton _("Galeri 6") action ShowMenu("gallery8")
        textbutton _("Galeri 7") action ShowMenu("gallery9")
        textbutton _("Galeri 8") action ShowMenu("gallery10")

        

        if _in_replay:
            textbutton _("Akhiri replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("Tentang") action ShowMenu("about")

        if renpy.variant("pc"):
            textbutton _("Membantu") action ShowMenu("help")
            textbutton _("Berhenti") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigasi"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")








screen main_menu():
    tag menu



    style_prefix "main_menu"

    add gui.main_menu_background


    frame




    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")











screen game_menu(title, scroll=None, yinitial=0.0):

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
                    scrollbars "vertikal"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertikal"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    textbutton _("Kembali"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30









screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "tentang"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size











screen save():
    tag menu


    use file_slots(_("Save"))


screen load():
    tag menu


    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

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
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "halaman"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")









screen preferences():
    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Menampilkan")
                        textbutton _("Jendela") action Preference("display", "window")
                        textbutton _("Layar penuh") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Sisi rollback")
                    textbutton _("Cacat") action Preference("rollback side", "disable")
                    textbutton _("Kiri") action Preference("rollback side", "left")
                    textbutton _("Benar") action Preference("rollback side", "right")

                vbox:
                    style_prefix "memeriksa"
                    label _("Melewati")
                    textbutton _("Teks yang tidak terlihat") action Preference("skip", "toggle")
                    textbutton _("Setelah pilihan") action Preference("after choices", "toggle")
                    textbutton _("Transisi") action InvertSelected(Preference("transitions", "toggle"))

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "Slider"
                box_wrap True

                vbox:

                    label _("Kecepatan teks")

                    bar value Preference("Kecepatan teks")

                    label _("Waktu maju otomatis")

                    bar value Preference("waktu maju otomatis")

                vbox:

                    if config.has_music:
                        label _("Volume Musik")

                        hbox:
                            bar value Preference("Volume Musik")

                    if config.has_sound:

                        label _("Volume suara")

                        hbox:
                            bar value Preference("volume suara")

                            if config.sample_sound:
                                textbutton _("Tes") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        label _("Volume Suara")

                        hbox:
                            bar value Preference("Volume Suara")

                            if config.sample_voice:
                                textbutton _("Tes") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Bisu semua"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

                    # Enhanced Mod Button - Backup caller (always visible)
                    null height (2 * gui.pref_spacing)
                    
                    textbutton "{color=#00ff00}Enhanced Mod{/color}" action ShowMenu("enhanced_joker_mod"):
                        style "check_button"




style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450










screen history():
    tag menu



    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "sejarah"

        for h in _history_list:

            window:


                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "warna" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("Sejarah dialog kosong.")




define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5








screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "membantu"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Memasuki")
        text _("Memajukan dialog dan mengaktifkan antarmuka.")

    hbox:
        label _("Ruang angkasa")
        text _("Dialog kemajuan tanpa memilih pilihan.")

    hbox:
        label _("Tombol panah")
        text _("Menavigasi antarmuka.")

    hbox:
        label _("Melarikan diri")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Lewati dialog sambil ditahan.")

    hbox:
        label _("Tab")
        text _("Melewati Dialog Mengalir.")

    hbox:
        label _("Halaman UP")
        text _("Bergulir kembali ke dialog sebelumnya.")

    hbox:
        label _("Halaman Down")
        text _("Bergulir ke dialog selanjutnya.")

    hbox:
        label "H"
        text _("Menyembunyikan antarmuka pengguna.")

    hbox:
        label "S"
        text _("Mengambil tangkapan layar.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Klik kiri")
        text _("Memajukan dialog dan mengaktifkan antarmuka.")

    hbox:
        label _("Klik tengah")
        text _("Menyembunyikan antarmuka pengguna.")

    hbox:
        label _("Klik kanan")
        text _("Accesses the game menu.")

    hbox:
        label _("Roda mouse di <! Newline!> Klik Sisi Rollback")
        text _("Bergulir kembali ke dialog sebelumnya.")

    hbox:
        label _("Roda tikus ke bawah")
        text _("Bergulir ke dialog selanjutnya.")


screen gamepad_help():

    hbox:
        label _("Pemicu kanan <! Newline!> Tombol A/Bottom")
        text _("Memajukan dialog dan mengaktifkan antarmuka.")

    hbox:
        label _("Pemicu kiri <! Newline!> Bahu kiri")
        text _("Bergulir kembali ke dialog sebelumnya.")

    hbox:
        label _("Bahu kanan")
        text _("Bergulir ke dialog selanjutnya.")


    hbox:
        label _("D-pad, tongkat")
        text _("Menavigasi antarmuka.")

    hbox:
        label _("Mulai, panduan")
        text _("Accesses the game menu.")

    hbox:
        label _("Tombol Y/TOP")
        text _("Menyembunyikan antarmuka pengguna.")

    textbutton _("Menyesuaikan") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "mengonfirmasi"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Ya") action yes_action
            textbutton _("No") action no_action


    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame(["gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "melewati"

    frame:

        has hbox
        spacing 6

        text _("Melewati")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):

    zorder 100
    style_prefix "memberitahu"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed
            yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "sedang"
    xsize 450



screen quick_menu():
    variant "menyentuh"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "cepat"

            xalign 0.5
            yalign 1.0

            textbutton _("Kembali") action Rollback()
            textbutton _("Melewati") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Mobil") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "kecil"
    background "gui/phone/textbox.png"

style radio_button:
    variant "kecil"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "kecil"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "kecil"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "kecil"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "kecil"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "kecil"
    xsize 340

style game_menu_content_frame:
    variant "kecil"
    top_margin 0

style pref_vbox:
    variant "kecil"
    xsize 400

style bar:
    variant "kecil"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "kecil"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "kecil"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "kecil"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "kecil"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "kecil"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "kecil"
    xsize None

style slider_pref_slider:
    variant "kecil"
    xsize 600


screen phonenavt():
    add "sleep1.jpg"
    hbox:
        xalign 0.98
        yalign 0.02
        imagebutton idle "nav/phone1.png" hover "nav/phone1.png" clicked Jump("opp_menu")


screen opport:
    add "alto.jpg"
    vbox:
        xalign 0.50 yalign 0.50
        text "[mname] Relationship: [mrel]" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        text "[mname] Corruption: [mcorr]" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        text "[mname] Domination: COMING SOON" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        text "[sname] Relationship: [srel]" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        text "[sname] Corruption: [scorr]" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        text "[sname] Domination: [sdom]" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        text "[bname] Brains: [bstudy]" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        text "Lebih banyak segera hadir" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        textbutton "KEMBALI" action Jump("nextday") xalign 0.50 yalign 0.50



screen opportg:
    add "alto.jpg"
    vbox:
        xalign 0.50 yalign 0.50
        text "[mname] Relationship: [mrel]" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        text "[mname] Corruption: [mcorr]" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        text "[mname] Domination: [mdom]" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        text "[sname] Relationship: [srel]" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        text "[sname] Corruption: [scorr]" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        text "[sname] Domination: [sdom]" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        text "[bname] Brains: [bstudy]" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        text "[bname] Fashion page knowledge: [binstaexp]" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        text "Money: [mny]" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        textbutton "KEMBALI" action Jump("broom_menu") xalign 0.50 yalign 0.50



screen gnav():
    hbox:
        xalign 0.02
        yalign 0.98
        imagebutton idle "nav/room.png" hover "nav/roomh.png" clicked Jump("hall_menu")
        imagebutton idle "nav/mroom.png" hover "nav/mroomh.png" clicked Jump("mroom_menu")
        imagebutton idle "nav/sroom.png" hover "nav/sroomh.png" clicked Jump("sroom_menu")
        imagebutton idle "nav/broom.png" hover "nav/broomh.png" clicked Jump("broom_menu")
        imagebutton idle "nav/toi.png" hover "nav/toih.png" clicked Jump("toi_menu")
        imagebutton idle "nav/cel.png" hover "nav/cellh.png" clicked Jump("opp_menug")
        if instadone ==2:
            imagebutton idle "nav/map.png" hover "nav/maph.png" clicked Jump("map_menu")
        else:
            imagebutton idle "nav/mapg.png" hover "nav/mapgh.png"


    hbox:
        xalign 0
        yalign 0
        imagebutton idle "nav/clock.png" hover "nav/clock.png" clicked Jump("dayadv")


    if Hour == 9:
        hbox:
            xalign 0.037
            yalign 0.72
            add "char/mico.png"

    elif Hour == 10:
        if workrequest ==2:
            hbox:
                xalign 0.037
                yalign 0.72
                add "char/mico.png"
            hbox:
                xalign 0.651
                yalign 0.72
                add "char/sico.png"
        else:
            hbox:
                xalign 0.651
                yalign 0.72
                add "char/sico.png"

    elif Hour == 11:
        hbox:
            xalign 0.350
            yalign 0.72
            add "char/sico.png"



    if Hour == 12:
        if workrequest ==3 and day !=7:
            hbox:
                xalign 0.037
                yalign 0.72
                add "char/sico.png"

        else:
            hbox:
                xalign 0.037
                yalign 0.72
                add "char/both.png"




    elif Hour == 13:

        hbox:
            xalign 0.350
            yalign 0.72
            add "char/sico.png"

    elif Hour == 14:
        if workrequest ==3 and day !=7:
            hbox:
                xalign 0.350
                yalign 0.72
                add "char/sico.png"

        else:
            hbox:
                xalign 0.350
                yalign 0.72
                add "char/sico.png"

            hbox:
                xalign 0.037
                yalign 0.72
                add "char/mico.png"

    elif Hour == 15:
        if workrequest ==3 and day !=7:
            hbox:
                xalign 0.037
                yalign 0.72
                add "char/sico.png"
        else:
            hbox:

                xalign 0.651
                yalign 0.72
                add "char/mico.png"

            hbox:
                xalign 0.037
                yalign 0.72
                add "char/sico.png"


    elif Hour ==16:
        if workrequest ==3 and day !=7:
            if elaineshowsup ==1 and day ==6:
                hbox:

                    xalign 0.651
                    yalign 0.72
                    add "char/sico.png"

                hbox:
                    xalign 0.037
                    yalign 0.72
                    add "char/eico.png"


            else:
                hbox:

                    xalign 0.651
                    yalign 0.72
                    add "char/sico.png"
        else:
            hbox:
                xalign 0.193
                yalign 0.72
                add "char/mico.png"

            hbox:

                xalign 0.651
                yalign 0.72
                add "char/sico.png"


    elif Hour == 17:
        if workrequest ==3 and day !=7:
            if cselaine0 == 11:
                hbox:
                    xalign 0.037
                    yalign 0.72
                    add "char/sico.png"

            else:
                pass
        else:
            if cselaine0 == 11:
                hbox:
                    xalign 0.037
                    yalign 0.72
                    add "char/both.png"

            else:
                pass





    elif Hour == 18:
        hbox:
            xalign 0.037
            yalign 0.72
            add "char/mico.png"
        hbox:
            xalign 0.350
            yalign 0.72
            add "char/sico.png"

    elif Hour == 19:

        hbox:
            xalign 0.350
            yalign 0.72
            add "char/sico.png"
        hbox:
            xalign 0.037
            yalign 0.72
            add "char/mico.png"

    elif Hour == 20:
        hbox:
            xalign 0.037
            yalign 0.72
            add "char/both.png"

    elif Hour == 21:
        hbox:
            xalign 0.037
            yalign 0.72
            add "char/mico.png"


    vbox:
        xalign 0.98
        text "[Hour]:00" size 43 xalign 0.98 yalign 0.03 outlines [(3, "#000000", 0, 0)]
        text "[dayname]" size 43 xalign 0.98 yalign 0.05 outlines [(3, "#000000", 0, 0)]




screen mrelup:
    text "YOUR RELATIONSHIP WITH [mname] HAS IMPROVED" size 35 xalign 0.5 yalign 0.5 outlines [(3, "#000000", 0, 0)]

screen mreldw:
    text "YOUR RELATIONSHIP WITH [mname] HAS DECREASED" size 35 xalign 0.5 yalign 0.5 outlines [(3, "#000000", 0, 0)]

screen srelup:
    text "YOUR RELATIONSHIP WITH [sname] HAS IMPROVED" size 35 xalign 0.5 yalign 0.5 outlines [(3, "#000000", 0, 0)]

screen sreldw:
    text "YOUR RELATIONSHIP WITH [sname] HAS DECREASED" size 35 xalign 0.5 yalign 0.5 outlines [(3, "#000000", 0, 0)]

screen sdomup:
    text "YOUR DOMINATION WITH [sname] HAS IMPROVED" size 35 xalign 0.5 yalign 0.5 outlines [(3, "#000000", 0, 0)]

screen sdomdw:
    text "YOUR DOMINATION WITH [sname] HAS DECREASED" size 35 xalign 0.5 yalign 0.5 outlines [(3, "#000000", 0, 0)]

screen scorr:
    text "[sname]'S CORRUPTION LEVEL HAS INCREASED" size 35 xalign 0.5 yalign 0.5 outlines [(3, "#000000", 0, 0)]

screen mcorr:
    text "[mname]'S CORRUPTION LEVEL HAS INCREASED" size 35 xalign 0.5 yalign 0.5 outlines [(3, "#000000", 0, 0)]

screen opnotif:
    text "Opsi baru tersedia" size 35 xalign 0.5 yalign 0.5 outlines [(3, "#000000", 0, 0)]

screen opmap:
    text "Opsi peta sekarang tersedia" size 35 xalign 0.5 yalign 0.5 outlines [(3, "#000000", 0, 0)]

screen opnotif_f:
    text "Opsi baru akan segera tersedia" size 35 xalign 0.5 yalign 0.5 outlines [(3, "#000000", 0, 0)]



screen map:
    add "alto.jpg"
    vbox:
        text "SEGERA HADIR" size 22 xalign 0.50 yalign 0.4 outlines [(3, "#FF0101", 0, 0)]
        textbutton "KEMBALI" action Jump("broom_menu") xalign 0.50 yalign 0.50



screen sbikchoice():
    add "sbikini1.jpg"
    default tt = Tooltip("")

    imagemap:

        ground "sbikini1.jpg"
        idle "sbikini1.jpg"
        hover "sbikini1.jpg"

        if bikini2 ==0:
            hotspot (1, 4, 398, 638) hovered tt.Action("Get this dress") action Jump("highcut")

        if bikini3 ==0:
            hotspot (402, 3, 402, 622) hovered tt.Action("Get this dress") action Jump("stringsling")

        if microskirt1==0:
            hotspot (824, 4, 446, 631) hovered tt.Action("Get this dress") action Jump("microsk")

        hotspot (552, 633, 176, 70) hovered tt.Action("Return Home") action Jump("broom_menu")



screen s_help():
    add "shelpbg.png"

    vbox:
        text "Temui Rowena" xalign 0.50 yalign 0.10 outlines [(3, "#FFC0CB", 0, 0)]
        xalign 0.50 yalign 0.10
        if rwena == 0:
            text "Dia muncul setelah seminggu bermain, pada hari Rabu di aula @15: 00" size 18
        elif rwena >= 1:
            text "Anda telah bertemu dengannya" size 18

    vbox:
        text "Create social media page for [sname]" xalign 0.50 yalign 0.20 outlines [(3, "#FFC0CB", 0, 0)]
        xalign 0.50 yalign 0.20
        if rwena == 0:
            text "Rowena akan berdiskusi dengan Anda tentang halaman tersebut" size 18

        elif rwena >= 2 and binstaexp <=5:
            text "Teliti beberapa alat untuk halaman" size 18


        elif binstaexp >5 and instadone ==0:
            text "You're ready to create the page for [sname]" size 18

        elif binstaexp <=5 and instadone ==0 and instresearchdone ==1:
            text "Lakukan riset lebih lanjut" size 18

        elif instadone >=1 and pagecheck <3:
            text "[sname]'s page is created, did you inform Rowena that you created the page? If yes wait for updates here" size 18

        elif instadone ==2 and skiss_asked == 1 and instauploads <1:
            text "Start uploading some images to [sname] page" size 18

        elif pagecheck >=3 and instauploads == 1 and laptoprequested ==0:
            text "You can now check [sname]'s page, your room, in the morning" size 18

        elif pagecheck >=3 and instauploads == 1 and laptoprequested ==0 and startnework ==1:
            text "[sname] Wants to upgrade her laptop, she's going for a new one while having dinner" size 18

        elif pagecheck >=3 and instauploads == 1 and laptoprequested ==1 and sscall ==0:
            text "Enter [sname] room, either in the morning or at night" size 18

        elif pagecheck >=3 and instauploads == 1 and laptoprequested ==1 and sscall ==1 and sbm ==0:
            text "Time to tell [mname] about [sname] phone call" size 18

        elif pagecheck >=3 and instauploads == 1 and sbm ==1:
            text "[sname] is angry, she's going to get back at you" size 18

    vbox:
        text "Kunjungi Rowena" xalign 0.50 yalign 0.40 outlines [(3, "#FFC0CB", 0, 0)]
        xalign 0.50 yalign 0.40
        if workrequest ==3 and rwena >= 1 and rvisit ==0:
            text "Anda dapat mengunjungi dari Hall menggunakan opsi santai pada pukul 10:00" size 18

        elif workrequest ==3 and rvisit ==1:
            if saction ==0:
                text "Kolam renang Rowena tidak terkunci, terus kunjungi" size 18
            elif saction >=1 and startnework ==0:
                text "You've discovered the nude beach, this helps with [sname]'s photoshoot, now you need [mname] to change the job" size 18
            elif saction >=1 and startnework ==1:
                text "You've discovered the nude beach, this helps with [sname]'s photoshoot!" size 18

        elif workrequest <3:
            text "Meet Rowena, then wait till [mname] starts working" size 18


    vbox:
        text "Pemotretan" xalign 0.5 yalign 0.30 outlines [(3, "#FFC0CB", 0, 0)]
        xalign 0.5 yalign 0.30
        if instadone <1:
            text "Buat halaman media sosial terlebih dahulu" size 18

        elif instadone >= 2 and instauploads == 0 and skiss_asked == 0:
            text "Her room @18:00, Knock, visit map for clothing options, do it many times to see all the outfits, \n Then complete (Talk about Rowena and kiss) below until you can ask to practice kisses with [sname]" size 17

        elif instadone >= 2 and instauploads == 0 and skiss_asked == 1:
            text "Mulai mengunggah gambar ke halamannya" size 18


        elif pagecheckdone ==0 and instauploads == 1 and startnework ==0:
            text "Check [sname]'s page" size 18

        elif pagecheckdone ==0 and instauploads == 1 and startnework ==1:
            text "Hmm anywone said sex with [sname]!" size 18


        elif pagecheckdone >=1 and pagecheck <3 and snameinstaconvinced ==0:
            text "Keep checking the page until you convince [sname] to take more suggestive photos" size 18

        elif pagecheckdone >=1 and pagecheck >3 and snameinstaconvinced ==0:
            text "Periksa halaman dan lihat apa yang terjadi" size 18

        elif pagecheckdone >=1 and snameinstaconvinced ==1:
            text "Besar!! Anda telah meyakinkannya, kunjungi kamarnya @18: 00, ketukan, semoga sukses :)" size 18





    vbox:
        text "Bicara tentang Rowena dan Ciuman" xalign 0.5 yalign 0.50 outlines [(3, "#FFC0CB", 0, 0)]
        xalign 0.5 yalign 0.50

        if rvisit >=1 and stalkb_rowena == 0:
            text "Watch TV in the morning, wait for [sname] to come" size 18

        elif rvisit >=1 and stalkb_rowena == 1:
            text "Bergantian antara menonton TV di pagi hari, dan mengunjungi Rowena" size 18

        elif rvisit >=1 and stalkb_rowena == 2:
            text "Ulangi alternatif antara menonton TV di pagi hari, dan mengunjungi Rowena" size 18

        elif rvisit >=1 and stalkb_rowena == 3 and rowenaslap ==0:
            text "Kunjungi Rowena Pool untuk ditampar" size 18

        elif rvisit >=1 and stalkb_rowena == 3 and rowenaslap ==1 and skiss_asked == 0:
            text "Watch TV in the morning, wait for [sname] to come, you can ask for the kiss, choose your option wisely" size 18

        elif rvisit >=1 and stalkb_rowena == 3 and skiss_asked == 1 and skiss ==0:
            if saction ==0:
                text "Kunjungi Pool Rowena, temui BF -nya (lebih dari satu kali) Nude Beach?" size 18
            elif saction >=1:
                text "You've discovered the nude beach, this helps with [sname]'s photoshoot and other things" size 18

        elif rvisit >=1 and stalkb_rowena == 3 and skiss_asked == 1 and skiss ==1:
            text "Silakan dan cium dia sambil menonton TV di pagi hari" size 18


        elif workrequest <3:
            text "Wait till [mname] starts working" size 18

    vbox:
        text "Work to buy phone for [sname]" xalign 0.5 yalign 0.60 outlines [(3, "#FFC0CB", 0, 0)]

        xalign 0.5 yalign 0.65
        if skiss_asked == 0 and pagecheck <1 and instauploads <1 and bworkstarted ==0:
            text "Kiss [sname] / Images upload to [sname]'s page / Start working" size 18

        elif skiss_asked == 1 and pagecheck <1 and instauploads <1 and bworkstarted ==0:
            text "Images upload to [sname]'s page, check the page often, then you'll be able start working" size 18

        elif skiss_asked == 1 and pagecheck >=1 and instauploads >=1 and bworkstarted ==0:
            text "Siap mulai bekerja, kunjungi peta di siang hari" size 18

        elif bworkstarted ==1 and buy_s_phonecounter <2 and mobilephoneacquired == 0:
            text "To buy phone for [sname] work for some more time, option will unlock in your room" size 18

        elif startnework ==1 and ticketrequested ==0:
            text "Tiket Konser?" size 18

        elif startnework ==1 and ticketrequested ==1:
            text "........ tiket konser? ........" size 18

        elif startnework ==1 and ticketrequested ==2:
            text "........ tiket konser? ........" size 18

        elif startnework ==1 and ticketrequested ==3:
            text "Kapan memberinya tiket konser?" size 18

        elif mobilephoneacquired == 1 and smobilegiven == 0:
            text "Dengan bijak memilih waktu untuk memberikan telepon, Anda memiliki beberapa opsi" size 18




        textbutton "KEMBALI" action Jump("broom_menu") xalign 0.50 yalign 0.80



screen m_help():
    add "shelpbg.png"

    vbox:
        text "[mname] work" xalign 0.50 yalign 0.10 outlines [(3, "#C70039", 0, 0)]
        xalign 0.50 yalign 0.10
        if workrequest ==3 and startnework ==0:
            text "[mname] started working" size 18

        elif workrequest ==3 and startnework ==1:
            text "[mname] started working with Elaine, new options at nights on specific days" size 18

        elif workrequest ==0:
            text "Kunjungi Hall @ 18:00, bicara dengan Elaine tentang menyewa kamar Anda" size 18
        elif workrequest ==1:
            text "Hampir sampai di sana!" size 18
        elif workrequest == 2:
            text "Hampir sampai di sana! Periksa pagi" size 18




    vbox:
        text "[mname] Confidence" xalign 0.50 yalign 0.20 outlines [(3, "#C70039", 0, 0)]
        xalign 0.50 yalign 0.20
        if workrequest ==3 and wrkquestions >=2 and camerasacquired == 0:
            text "Kunjungi Hall on Sunday @ 18:00 Keluhan lalu menguping" size 18

        elif workrequest ==3 and wrkquestions >=2 and camerasacquired == 1 and camerafixing == 2 and elaine_convince== 0:
            text "Anda perlu membujuk Elaine untuk meyakinkannya untuk mengubah pekerjaan, Minggu @ 18:00" size 18

        elif workrequest ==3 and wrkquestions <2:
            text "[mname]? How's the new work? Does it pay well?" size 18

        elif workrequest ==3 and elaine_convince == 1:
            text "Elaine setuju untuk membantu Anda, periksa pada hari Minggu @ 18:00" size 18

        elif workrequest ==3 and elaine_convince == 2:
            text "Elaine setuju untuk membantu Anda, melakukan adegan yang sama pada hari Minggu" size 18

        elif workrequest ==3 and elaine_convince == 3:
            text "Elaine setuju untuk membantu Anda, melakukan adegan yang sama pada hari Minggu sekali lagi" size 18

        elif elaine_convince ==4 and startnework ==0:
            text "Selamat pagi, apa? Pekerjaan Baru?" size 18

        elif elaine_convince ==4 and startnework ==1:
            text "[mname] started a new job, it's your job to boost her confidence, at different times" size 18


    vbox:
        text "Gifts for [mname]" xalign 0.50 yalign 0.30 outlines [(3, "#C70039", 0, 0)]
        xalign 0.50 yalign 0.30
        if mpracticegift == 0 and startnework ==0:
            text "Dia harus mengubah pekerjaan" size 18

        elif mpracticegift == 0 and startnework ==1:
            text "Buat beberapa drama pada hari Minggu di siang hari" size 18

        elif mpracticegift == 1 and startnework ==1:
            text "Anda tahu di mana membelinya" size 18

        textbutton "KEMBALI" action Jump("broom_menu") xalign 0.50 yalign 0.80



screen etvnav():
    hbox:
        xalign 0.02
        yalign 0.98
        imagebutton idle "nav/room.png" hover "nav/roomh.png" clicked Jump("noaccess")
        imagebutton idle "nav/mroom.png" hover "nav/mroomh.png" clicked Jump("mroom_etv")
        imagebutton idle "nav/sroom.png" hover "nav/sroomh.png" clicked Jump("noaccess")
        imagebutton idle "nav/broom.png" hover "nav/broomh.png" clicked Jump("noaccess")
        imagebutton idle "nav/toi.png" hover "nav/toih.png" clicked Jump("noaccess")
        imagebutton idle "nav/cel.png" hover "nav/cellh.png" clicked Jump("noaccess")
        if instadone ==2:
            imagebutton idle "nav/map.png" hover "nav/maph.png" clicked Jump("noaccess")
        else:
            imagebutton idle "nav/mapg.png" hover "nav/mapgh.png"

        hbox:
            xalign 0.037
            yalign 0.72
            add "char/mico.png"




screen noaccessnotif:
    text "Sudah terlambat untuk masuk ke sini" size 35 xalign 0.5 yalign 0.5 outlines [(3, "#000000", 0, 0)]



screen inthelp():
    add "internet.jpg"
    default tt = Tooltip("")

    imagemap:

        ground "internet.jpg"
        idle "internet.jpg"
        hover "internet.jpg"


        hotspot (29, 4, 605, 715) hovered tt.Action("Shop online") action Jump("onlineshop")

        hotspot (648, 8, 627, 711) hovered tt.Action("Get some help") action Jump("socialhelp")

        textbutton "KEMBALI" action Jump("broom_menu") xalign 0.50 yalign 0.80


screen screnotif:
    text "Anda menerima obeng" size 35 xalign 0.5 yalign 0.5 outlines [(3, "#000000", 0, 0)]





screen jdcorr():
    imagemap:
        ground "rooms_ms.jpg"
        hover "rooms_ms_hover.jpg"
        idle "rooms_ms.jpg"
        hotspot (55, 6, 353, 125) action Jump("daytra")
        hotspot (36, 159, 409, 553) action Jump("mroomtra")
        hotspot (860, 148, 405, 567) action Jump("sroomtra")
        hotspot (888, 1, 369, 126) action Jump("toilettra")



screen jdssr():
    imagemap:
        ground "rooms_ss.jpg"
        hover "rooms_ss_hover.jpg"
        idle "rooms_ss.jpg"
        if edpills ==0:
            hotspot (964, 160, 217, 107) action Jump("drawerright")
        if sdildo ==0:
            hotspot (108, 148, 226, 136) action Jump("drawerleft")
        textbutton "MELANJUTKAN" action Jump("d_one_tra") xalign 0.5 yalign 0.89
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
