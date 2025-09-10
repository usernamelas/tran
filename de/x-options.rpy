












define config.name = _("Jen's Dilemma")





define gui.show_name = True




define config.version = "V25"




define gui.about = _p("""
""")






define build.name = "JensDilemma"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True
























define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve





define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "JensDilemma-1569580457"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)



















    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
