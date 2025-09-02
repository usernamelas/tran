# ========================================
# Enhanced Joker Mod - Fixed Version
# Features: Relationship, Corruption, Money, Gallery
# ========================================

init python:
    # Mod Configuration
    mod_author = Character("ModAuthor", color="#FFD700")
    
    # Initialize variables if they don't exist
    if not hasattr(store, 'srel'):
        store.srel = 0
    if not hasattr(store, 'mrel'):
        store.mrel = 0
    if not hasattr(store, 'erel'):
        store.erel = 0
    if not hasattr(store, 'melrel'):
        store.melrel = 0
    if not hasattr(store, 'scorr'):
        store.scorr = 0
    if not hasattr(store, 'mcorr'):
        store.mcorr = 0
    if not hasattr(store, 'mny'):
        store.mny = 0
    if not hasattr(store, 'gallery_unlocked'):
        store.gallery_unlocked = False
    
    # Gallery unlock function
    def unlock_all_gallery():
        store.sphotos_progress = 10
        store.hotphotos_done = 1
        store.sactiondone_mast = 1
        store.sblowjobdone = 1
        store.msex = 1
        store.sanal = 1
        store.mphotos = 1
        store.jenopen = 1
        store.elainefuck = 1
        store.gallery_unlocked = True
        renpy.notify("Gallery Unlocked!")
    
    def lock_all_gallery():
        store.sphotos_progress = 0
        store.hotphotos_done = 0
        store.sactiondone_mast = 0
        store.sblowjobdone = 0
        store.msex = 0
        store.sanal = 0
        store.mphotos = 0
        store.jenopen = 0
        store.elainefuck = 0
        store.gallery_unlocked = False
        renpy.notify("Gallery Locked!")

# Main Enhanced Mod Screen
screen enhanced_joker_mod():
    tag menu
    modal True
    
    # Initialize screen variable
    default current_tab = "relationship"
    
    # Modern dark background with gradient
    add "#2a2a2a"
    add Transform(Solid("#1a1a1a"), alpha=0.7)
    
    # Container with padding
    frame:
        background None
        xfill True
        yfill True
        padding (40, 40)
        
        vbox:
            spacing 0
            
            # Header with exit and save buttons
            hbox:
                xfill True
                
                # Exit button (left) - FIXED
                textbutton "{size=48}{color=#ff4444}exit{/color}{/size}" action Return():
                    hover_background None
                    background None
                    padding (15, 15)
                
                # Spacer
                null width 1.0
                
                # Save button (right) 
                textbutton "{size=48}{color=#ff4444}save{/color}{/size}" action Function(renpy.notify, "Settings Saved!"):
                    hover_background None
                    background None
                    padding (15, 15)
            
            # Tab navigation
            null height 60
            
            hbox:
                spacing 20
                
                textbutton "relationship" action SetScreenVariable("current_tab", "relationship"):
                    if current_tab == "relationship":
                        text_color "#00ff00"
                        background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    else:
                        text_color "#888888"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    text_size 24
                    padding (30, 15)
                
                textbutton "corruption" action SetScreenVariable("current_tab", "corruption"):
                    if current_tab == "corruption":
                        text_color "#00ff00"
                        background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    else:
                        text_color "#888888"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    text_size 24
                    padding (30, 15)
            
            # Tab content area
            if current_tab == "relationship":
                use relationship_tab()
            elif current_tab == "corruption":
                use corruption_tab()

# Relationship Tab Content
screen relationship_tab():
    frame:
        background None
        xpos 0
        ypos 0
        xfill True
        yfill True
        
        vbox:
            spacing 40
            
            # Section title
            text "{size=64}{color=#00ff00}relationship{/color}"
            
            null height 40
            
            # Sister relationship
            hbox:
                spacing 30
                
                text "{size=48}{color=#ffff00}sister{/color}" xsize 200
                
                # Relationship bar
                bar:
                    value VariableValue("srel", 100)
                    xsize 400
                    ysize 20
                    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
                    thumb None
                
                # +10 button
                textbutton "+10" action SetVariable("srel", min(100, srel + 10)):
                    text_size 32
                    text_color "#00ff00"
                    background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (20, 10)
                
                # Value display
                text "{size=48}{color=#00ff00}[srel]{/color}" xsize 100 text_align 0.5
            
            # Mother relationship
            hbox:
                spacing 30
                
                text "{size=48}{color=#ffff00}mother{/color}" xsize 200
                
                bar:
                    value VariableValue("mrel", 100)
                    xsize 400
                    ysize 20
                    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
                    thumb None
                
                textbutton "+10" action SetVariable("mrel", min(100, mrel + 10)):
                    text_size 32
                    text_color "#00ff00"
                    background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (20, 10)
                
                text "{size=48}{color=#00ff00}[mrel]{/color}" xsize 100 text_align 0.5
            
            # Elaine relationship
            hbox:
                spacing 30
                
                text "{size=48}{color=#ffff00}elaine{/color}" xsize 200
                
                bar:
                    value VariableValue("erel", 100)
                    xsize 400
                    ysize 20
                    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
                    thumb None
                
                textbutton "+10" action SetVariable("erel", min(100, erel + 10)):
                    text_size 32
                    text_color "#00ff00"
                    background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (20, 10)
                
                text "{size=48}{color=#00ff00}[erel]{/color}" xsize 100 text_align 0.5
            
            # Melinda relationship
            hbox:
                spacing 30
                
                text "{size=48}{color=#ffff00}melinda{/color}" xsize 200
                
                bar:
                    value VariableValue("melrel", 100)
                    xsize 400
                    ysize 20
                    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
                    thumb None
                
                textbutton "+10" action SetVariable("melrel", min(100, melrel + 10)):
                    text_size 32
                    text_color "#00ff00"
                    background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (20, 10)
                
                text "{size=48}{color=#00ff00}[melrel]{/color}" xsize 100 text_align 0.5
            
            # Money section
            null height 60
            
            hbox:
                spacing 40
                
                text "{size=64}{color=#00ff00}money{/color}"
                
                textbutton "+100" action SetVariable("mny", mny + 100):
                    text_size 36
                    text_color "#00ff00"
                    background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (30, 15)
                
                textbutton "+1000" action SetVariable("mny", mny + 1000):
                    text_size 36
                    text_color "#00ff00"
                    background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (30, 15)
                
                text "{size=36}{color=#00ff00}$[mny]{/color}"
            
            # Gallery section
            null height 80
            
            hbox:
                spacing 40
                
                text "{size=64}{color=#00ff00}unlock gallery{/color}"
                
                # Toggle switch
                if gallery_unlocked:
                    textbutton "{size=36}{color=#00ff00}UNLOCKED{/color}" action Function(lock_all_gallery):
                        background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (40, 20)
                else:
                    textbutton "{size=36}{color=#ff4444}LOCKED{/color}" action Function(unlock_all_gallery):
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (40, 20)

# Corruption Tab Content
screen corruption_tab():
    frame:
        background None
        xpos 0
        ypos 0
        xfill True
        yfill True
        
        vbox:
            spacing 40
            
            # Section title
            text "{size=64}{color=#00ff00}corruption{/color}"
            
            null height 40
            
            # Sister corruption
            hbox:
                spacing 30
                
                text "{size=48}{color=#ffff00}sister{/color}" xsize 200
                
                bar:
                    value VariableValue("scorr", 100)
                    xsize 400
                    ysize 20
                    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
                    thumb None
                
                textbutton "+10" action SetVariable("scorr", min(100, scorr + 10)):
                    text_size 32
                    text_color "#00ff00"
                    background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (20, 10)
                
                text "{size=48}{color=#00ff00}[scorr]{/color}" xsize 100 text_align 0.5
            
            # Mother corruption
            hbox:
                spacing 30
                
                text "{size=48}{color=#ffff00}mother{/color}" xsize 200
                
                bar:
                    value VariableValue("mcorr", 100)
                    xsize 400
                    ysize 20
                    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
                    thumb None
                
                textbutton "+10" action SetVariable("mcorr", min(100, mcorr + 10)):
                    text_size 32
                    text_color "#00ff00"
                    background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (20, 10)
                
                text "{size=48}{color=#00ff00}[mcorr]{/color}" xsize 100 text_align 0.5

# Quick access integration
screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback() text_size 15
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True) text_size 15
            textbutton _("Auto") action Preference("auto-forward", "toggle") text_size 15
            textbutton _("Save") action ShowMenu('save') text_size 15
            textbutton _("Q.Save") action QuickSave() text_size 15
            textbutton _("Q.Load") action QuickLoad() text_size 15
            textbutton _("Opts") action ShowMenu('preferences') text_size 15

    # Modern Enhanced Mod Button
    hbox:
        style_prefix "quick"
        xalign 1.0
        yalign 1.0
        textbutton "{color=#00ff00}Enhanced Mod{/color}" action ShowMenu("enhanced_joker_mod") text_size 16

# Override the original quick menu
init python:
    config.overlay_screens.append("quick_menu")

# Add hotkey for quick access (K key)
define config.keymap['enhanced_mod'] = ['K']
init python:
    config.underlay.append(renpy.Keymap(enhanced_mod=ShowMenu("enhanced_joker_mod")))