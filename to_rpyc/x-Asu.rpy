# ========================================
# Enhanced Joker Mod - Fixed with Proper Save Support
# Features: Relationship, Corruption, Money, Gallery
# ========================================

# IMPORTANT: Define variables with 'default' for proper saving
default srel = 0
default mrel = 0
default mdom = 0
default sdom = 0
default erel = 0
default melrel = 0
default scorr = 0
default mcorr = 0
default mny = 0
default gallery_unlocked = False

# Current tab variable
default current_tab = "relationship"

init python:
    # Mod Configuration
    mod_author = Character("ModAuthor", color="#FFD700")
    
    # Gallery unlock function - FIXED with all 77 gallery images
    def unlock_all_gallery():
        # Unlock all 77 gallery images (gallery.rpy + gallery1.rpy to gallery10.rpy)
        for i in range(1, 78):  # 1 to 77
            setattr(persistent, f"unlock_{i}", True)
        
        store.gallery_unlocked = True
        renpy.notify("All 77 Gallery Images Unlocked!")
    
    def lock_all_gallery():
        # Lock all 77 gallery images
        for i in range(1, 78):  # 1 to 77
            setattr(persistent, f"unlock_{i}", False)
        
        store.gallery_unlocked = False
        renpy.notify("All 77 Gallery Images Locked!")

# Main Enhanced Mod Screen - Fixed for responsive display
screen enhanced_joker_mod():
    tag menu
    modal True
    
    # Full screen background
    add "#2a2a2a"
    add Solid("#1a1a1a80")
    
    # Use full available screen space
    frame:
        background None
        xfill True
        yfill True
        padding (20, 20)
        
        vbox:
            spacing 15
            
            # Header with exit and save buttons - smaller size
            hbox:
                xfill True
                
                textbutton "{size=32}{color=#ff4444}EXIT{/color}{/size}" action Return():
                    hover_background None
                    background None
                    padding (10, 10)
                
                null width 1.0
                
                textbutton "{size=32}{color=#44ff44}SAVE{/color}{/size}" action [Function(renpy.save, "mod_quicksave"), Function(renpy.notify, "Game Saved!")]:
                    hover_background None
                    background None
                    padding (10, 10)
            
            # Tab navigation - smaller and centered
            hbox:
                xalign 0.5
                spacing 30
                
                textbutton "RELATIONSHIP" action SetScreenVariable("current_tab", "relationship"):
                    if current_tab == "relationship":
                        text_color "#00ff00"
                        text_size 20
                        background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    else:
                        text_color "#888888"
                        text_size 20
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (25, 12)
                
                textbutton "CORRUPTION" action SetScreenVariable("current_tab", "corruption"):
                    if current_tab == "corruption":
                        text_color "#00ff00"
                        text_size 20
                        background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    else:
                        text_color "#888888"
                        text_size 20
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (25, 12)
            
            # Content area - uses remaining space
            frame:
                background Solid("#333333")
                xfill True
                yfill True
                padding (15, 15)
                
                if current_tab == "relationship":
                    use relationship_tab()
                elif current_tab == "corruption":
                    use corruption_tab()

# Relationship Tab Content - Compact responsive layout
screen relationship_tab():
    viewport:
        xfill True
        yfill True
        mousewheel True
        draggable True
        scrollbars "vertical"
        
        vbox:
            spacing 20
            
            # Section title - smaller
            text "{size=32}{color=#00ff00}RELATIONSHIP STATS{/color}" xalign 0.5
            
            # Sister relationship - more compact
            frame:
                background Solid("#444444")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ffff00}SISTER{/color}" xsize 120
                    
                    bar:
                        value VariableValue("srel", 9999)
                        xsize 200
                        ysize 20
                        left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                        right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
                        thumb None
                    
                    textbutton "+10" action SetVariable("srel", min(9999, srel + 10)):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetVariable("srel", 9999):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    text "{size=24}{color=#00ff00}[srel]/9999{/color}" xsize 80 text_align 0.5
            
            # Mother relationship
            frame:
                background Solid("#444444")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ffff00}MOTHER{/color}" xsize 120
                    
                    bar:
                        value VariableValue("mrel", 9999)
                        xsize 200
                        ysize 20
                        left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                        right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
                        thumb None
                    
                    textbutton "+10" action SetVariable("mrel", min(9999, mrel + 10)):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetVariable("mrel", 9999):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    text "{size=24}{color=#00ff00}[mrel]/9999{/color}" xsize 80 text_align 0.5
            
            # Elaine relationship
            frame:
                background Solid("#444444")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ffff00}ELAINE{/color}" xsize 120
                    
                    bar:
                        value VariableValue("erel", 9999)
                        xsize 200
                        ysize 20
                        left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                        right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
                        thumb None
                    
                    textbutton "+10" action SetVariable("erel", min(9999, erel + 10)):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetVariable("erel", 9999):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    text "{size=24}{color=#00ff00}[erel]/9999{/color}" xsize 80 text_align 0.5
            
            # Melinda relationship
            frame:
                background Solid("#444444")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ffff00}MELINDA{/color}" xsize 120
                    
                    bar:
                        value VariableValue("melrel", 9999)
                        xsize 200
                        ysize 20
                        left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                        right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
                        thumb None
                    
                    textbutton "+10" action SetVariable("melrel", min(9999, melrel + 10)):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetVariable("melrel", 9999):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    text "{size=24}{color=#00ff00}[melrel]/9999{/color}" xsize 80 text_align 0.5
            
            # Money section - more compact
            frame:
                background Solid("#225522")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 20
                    xalign 0.5
                    
                    text "{size=28}{color=#00ff00}MONEY{/color}"
                    
                    textbutton "+$100" action SetVariable("mny", mny + 100):
                        text_size 22
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (15, 8)
                    
                    textbutton "+$1000" action SetVariable("mny", mny + 1000):
                        text_size 22
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (15, 8)
                    
                    textbutton "+$10000" action SetVariable("mny", mny + 10000):
                        text_size 22
                        text_color "#ffaa00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (15, 8)
                    
                    text "{size=26}{color=#00ff00}$[mny]{/color}"
            
            # Gallery section - compact
            frame:
                background Solid("#552255")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 30
                    xalign 0.5
                    
                    text "{size=28}{color=#ff88ff}GALLERY UNLOCK{/color}"
                    
                    if gallery_unlocked:
                        textbutton "{size=24}{color=#00ff00}✓ UNLOCKED{/color}" action Function(lock_all_gallery):
                            background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                            padding (20, 10)
                    else:
                        textbutton "{size=24}{color=#ff4444}✗ LOCKED{/color}" action Function(unlock_all_gallery):
                            background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                            hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                            padding (20, 10)
            
            # Section title - smaller
            text "{size=32}{color=#ff4444}DOMINATION STATS{/color}" xalign 0.5
            
            # JANNY domination 
            frame:
                background Solid("#444444")
                padding (20, 15)
                xfill True
                
                hbox:
                    spacing 20
                    
                    text "{size=36}{color=#ffff00}JANNY Dom{/color}" xsize 120
                    
                    bar:
                        value VariableValue("mdom", 9999)
                        xsize 300
                        ysize 25
                        left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                        right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
                        thumb None
                    
                    textbutton "+10" action SetVariable("mdom", min(9999, mdom + 10)):
                        text_size 28
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (15, 8)
                    
                    textbutton "MAX" action SetVariable("mdom", 9999):
                        text_size 28
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (15, 8)
                    
                    text "{size=36}{color=#00ff00}[mdom]/9999{/color}" xsize 120 text_align 0.5
            
            # Melinda relationship
            frame:
                background Solid("#444444")
                padding (20, 15)
                xfill True
                
                hbox:
                    spacing 20
                    
                    text "{size=36}{color=#ffff00}NADIA Dom{/color}" xsize 120
                    
                    bar:
                        value VariableValue("sdom", 9999)
                        xsize 300
                        ysize 25
                        left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                        right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
                        thumb None
                    
                    textbutton "+10" action SetVariable("sdom", min(9999, sdom + 10)):
                        text_size 28
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (15, 8)
                    
                    textbutton "MAX" action SetVariable("sdom", 9999):
                        text_size 28
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (15, 8)
                    
                    text "{size=36}{color=#00ff00}[sdom]/9999{/color}" xsize 120 text_align 0.5
            


# Corruption Tab Content - Compact responsive layout
screen corruption_tab():
    viewport:
        xfill True
        yfill True
        mousewheel True
        draggable True
        scrollbars "vertical"
        
        vbox:
            spacing 20
            
            # Section title - smaller
            text "{size=32}{color=#ff4444}CORRUPTION STATS{/color}" xalign 0.5
            
            # Sister corruption - more compact
            frame:
                background Solid("#554444")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ff8888}SISTER{/color}" xsize 120
                    
                    bar:
                        value VariableValue("scorr", 9999)
                        xsize 200
                        ysize 20
                        left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                        right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
                        thumb None
                    
                    textbutton "+10" action SetVariable("scorr", min(9999, scorr + 10)):
                        text_size 20
                        text_color "#ff4444"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetVariable("scorr", 9999):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    text "{size=24}{color=#ff4444}[scorr]/9999{/color}" xsize 80 text_align 0.5
            
            # Mother corruption
            frame:
                background Solid("#554444")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ff8888}MOTHER{/color}" xsize 120
                    
                    bar:
                        value VariableValue("mcorr", 9999)
                        xsize 200
                        ysize 20
                        left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                        right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
                        thumb None
                    
                    textbutton "+10" action SetVariable("mcorr", min(9999, mcorr + 10)):
                        text_size 20
                        text_color "#ff4444"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetVariable("mcorr", 9999):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    text "{size=24}{color=#ff4444}[mcorr]/9999{/color}" xsize 80 text_align 0.5


            # uknow
            frame:
                background Solid("#554444")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ff8888}MOTHER{/color}" xsize 120
                    
                    bar:
                        value VariableValue("mcorr", 9999)
                        xsize 200
                        ysize 20
                        left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                        right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
                        thumb None
                    
                    textbutton "+10" action SetVariable("mcorr", min(9999, mcorr + 10)):
                        text_size 20
                        text_color "#ff4444"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetVariable("mcorr", 9999):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    text "{size=24}{color=#ff4444}[mcorr]/9999{/color}" xsize 80 text_align 0.5
                    
                    
                    
                    
#



# Combined mod overlay dengan Enhanced Mod di bawah, Monitor di atas
screen mod_overlay():
    zorder 100
    
    vbox:
        xalign 1.0  # Pojok kanan
        yalign 0.0  # Mulai dari atas
        spacing 5
        
        # Tombol Monitor - DI ATAS
        textbutton "{color=#ff9900}Monitor{/color}" action Show("enhanced_monitor"):
            text_size 16
            background None
            hover_background None
            padding (10, 5)
        
        # Tombol Enhanced Mod - DI BAWAH
        textbutton "{color=#00ff00}Enhanced Mod{/color}" action ShowMenu("enhanced_joker_mod"):
            text_size 16
            background None
            hover_background None
            padding (10, 5)

init python:
    # Aktifkan overlay combined
    config.overlay_screens.append("mod_overlay")
    
    # JANGAN aktifkan monitor_button terpisah lagi
    # config.overlay_screens.append("monitor_button")  # HAPUS/COMMENT BARIS INI

# Add hotkey for quick access (K key)
define config.keymap['enhanced_mod'] = ['K']
init python:
    config.underlay.append(renpy.Keymap(enhanced_mod=ShowMenu("enhanced_joker_mod")))