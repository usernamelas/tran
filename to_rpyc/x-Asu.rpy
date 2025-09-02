# ========================================
# Enhanced Joker Mod - Fixed Version
# Features: Relationship, Corruption, Money, Gallery
# ========================================

init python:
    # Mod Configuration
    mod_author = Character("ModAuthor", color="#FFD700")
    
    # Initialize persistent variables dengan nilai default yang benar
    def init_persistent_vars():
        if not hasattr(persistent, 'srel') or persistent.srel is None:
            persistent.srel = 0
        if not hasattr(persistent, 'mrel') or persistent.mrel is None:
            persistent.mrel = 0
        if not hasattr(persistent, 'erel') or persistent.erel is None:
            persistent.erel = 0
        if not hasattr(persistent, 'melrel') or persistent.melrel is None:
            persistent.melrel = 0
        if not hasattr(persistent, 'scorr') or persistent.scorr is None:
            persistent.scorr = 0
        if not hasattr(persistent, 'mcorr') or persistent.mcorr is None:
            persistent.mcorr = 0
        if not hasattr(persistent, 'mny') or persistent.mny is None:
            persistent.mny = 0
        if not hasattr(persistent, 'gallery_unlocked') or persistent.gallery_unlocked is None:
            persistent.gallery_unlocked = False
    
    # Panggil fungsi inisialisasi
    init_persistent_vars()
    
    # Gallery unlock function
    def unlock_all_gallery():
        # Make sure to use persistent data for gallery unlocks
        if hasattr(persistent, 'sphotos_progress'):
            persistent.sphotos_progress = 10
        if hasattr(persistent, 'hotphotos_done'):
            persistent.hotphotos_done = 1
        if hasattr(persistent, 'sactiondone_mast'):
            persistent.sactiondone_mast = 1
        if hasattr(persistent, 'sblowjobdone'):
            persistent.sblowjobdone = 1
        if hasattr(persistent, 'msex'):
            persistent.msex = 1
        if hasattr(persistent, 'sanal'):
            persistent.sanal = 1
        if hasattr(persistent, 'mphotos'):
            persistent.mphotos = 1
        if hasattr(persistent, 'jenopen'):
            persistent.jenopen = 1
        if hasattr(persistent, 'elainefuck'):
            persistent.elainefuck = 1
        
        persistent.gallery_unlocked = True
        renpy.notify("Gallery Unlocked!")
    
    def lock_all_gallery():
        # Reset gallery progress
        if hasattr(persistent, 'sphotos_progress'):
            persistent.sphotos_progress = 0
        if hasattr(persistent, 'hotphotos_done'):
            persistent.hotphotos_done = 0
        if hasattr(persistent, 'sactiondone_mast'):
            persistent.sactiondone_mast = 0
        if hasattr(persistent, 'sblowjobdone'):
            persistent.sblowjobdone = 0
        if hasattr(persistent, 'msex'):
            persistent.msex = 0
        if hasattr(persistent, 'sanal'):
            persistent.sanal = 0
        if hasattr(persistent, 'mphotos'):
            persistent.mphotos = 0
        if hasattr(persistent, 'jenopen'):
            persistent.jenopen = 0
        if hasattr(persistent, 'elainefuck'):
            persistent.elainefuck = 0
        
        persistent.gallery_unlocked = False
        renpy.notify("Gallery Locked!")

# Main Enhanced Mod Screen - FIXED
screen enhanced_joker_mod():
    tag menu
    modal True
    
    # Initialize screen variable
    default current_tab = "relationship"
    
    # Pastikan variabel persistent terinisialisasi
    on "show" action Function(init_persistent_vars)
    
    # Modern dark background with gradient
    add "#2a2a2a"
    add Transform(Solid("#1a1a1a"), alpha=0.7)
    
    # Container with proper sizing
    frame:
        background None
        xalign 0.5
        yalign 0.5
        xmaximum 1000
        ymaximum 600
        padding (30, 30)
        
        vbox:
            spacing 15
            
            # Header with exit and save buttons
            hbox:
                xfill True
                
                # Exit button (left)
                textbutton "{size=20}{color=#ff4444}EXIT{/color}{/size}" action Return():
                    background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (15, 8)
                    xalign 0.0
                
                # Spacer
                null width 1.0
                
                # Save button (right)
                textbutton "{size=20}{color=#44ff44}SAVE{/color}{/size}" action Function(renpy.notify, "Progress Saved!"):
                    background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (15, 8)
                    xalign 1.0
            
            null height 15
            
            # Tab navigation
            hbox:
                spacing 10
                xalign 0.5
                
                textbutton "RELATIONSHIP" action SetScreenVariable("current_tab", "relationship"):
                    if current_tab == "relationship":
                        text_color "#00ff00"
                        background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    else:
                        text_color "#888888"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    text_size 18
                    padding (25, 8)
                
                textbutton "CORRUPTION" action SetScreenVariable("current_tab", "corruption"):
                    if current_tab == "corruption":
                        text_color "#00ff00"
                        background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    else:
                        text_color "#888888"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    text_size 18
                    padding (25, 8)
            
            null height 20
            
            # Tab content area
            if current_tab == "relationship":
                use relationship_tab()
            elif current_tab == "corruption":
                use corruption_tab()

# Relationship Tab Content - FIXED
screen relationship_tab():
    vbox:
        spacing 15
        xfill True
        
        # Section title
        text "{size=28}{color=#00ff00}RELATIONSHIP{/color}{/size}" xalign 0.5
        
        # Sister relationship - FIXED: Gunakan default value jika None
        hbox:
            spacing 10
            xalign 0.5
            
            text "{size=20}{color=#ffff00}Sister:{/color}{/size}" xsize 120
            
            # Relationship bar
            bar:
                value (persistent.srel if persistent.srel is not None else 0)
                range 100
                xsize 250
                ysize 18
                left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
            
            # +10 button
            textbutton "+10" action [SetField(persistent, "srel", min(100, (persistent.srel if persistent.srel is not None else 0) + 10)), Function(init_persistent_vars)]:
                text_size 18
                text_color "#00ff00"
                background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                padding (12, 4)
            
            # Value display
            text "{size=20}{color=#00ff00}[persistent.srel if persistent.srel is not None else 0]{/color}{/size}" xsize 40 text_align 0.5
        
        # Mother relationship
        hbox:
            spacing 10
            xalign 0.5
            
            text "{size=20}{color=#ffff00}Mother:{/color}{/size}" xsize 120
            
            bar:
                value (persistent.mrel if persistent.mrel is not None else 0)
                range 100
                xsize 250
                ysize 18
                left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
            
            textbutton "+10" action [SetField(persistent, "mrel", min(100, (persistent.mrel if persistent.mrel is not None else 0) + 10)), Function(init_persistent_vars)]:
                text_size 18
                text_color "#00ff00"
                background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                padding (12, 4)
            
            text "{size=20}{color=#00ff00}[persistent.mrel if persistent.mrel is not None else 0]{/color}{/size}" xsize 40 text_align 0.5
        
        # Elaine relationship
        hbox:
            spacing 10
            xalign 0.5
            
            text "{size=20}{color=#ffff00}Elaine:{/color}{/size}" xsize 120
            
            bar:
                value (persistent.erel if persistent.erel is not None else 0)
                range 100
                xsize 250
                ysize 18
                left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
            
            textbutton "+10" action [SetField(persistent, "erel", min(100, (persistent.erel if persistent.erel is not None else 0) + 10)), Function(init_persistent_vars)]:
                text_size 18
                text_color "#00ff00"
                background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                padding (12, 4)
            
            text "{size=20}{color=#00ff00}[persistent.erel if persistent.erel is not None else 0]{/color}{/size}" xsize 40 text_align 0.5
        
        # Melinda relationship
        hbox:
            spacing 10
            xalign 0.5
            
            text "{size=20}{color=#ffff00}Melinda:{/color}{/size}" xsize 120
            
            bar:
                value (persistent.melrel if persistent.melrel is not None else 0)
                range 100
                xsize 250
                ysize 18
                left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
            
            textbutton "+10" action [SetField(persistent, "melrel", min(100, (persistent.melrel if persistent.melrel is not None else 0) + 10)), Function(init_persistent_vars)]:
                text_size 18
                text_color "#00ff00"
                background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                padding (12, 4)
            
            text "{size=20}{color=#00ff00}[persistent.melrel if persistent.melrel is not None else 0]{/color}{/size}" xsize 40 text_align 0.5
        
        # Money section
        null height 15
        
        hbox:
            spacing 10
            xalign 0.5
            
            text "{size=24}{color=#00ff00}Money:{/color}{/size}"
            
            textbutton "+100" action [SetField(persistent, "mny", (persistent.mny if persistent.mny is not None else 0) + 100), Function(init_persistent_vars)]:
                text_size 18
                text_color "#00ff00"
                background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                padding (12, 4)
            
            textbutton "+1000" action [SetField(persistent, "mny", (persistent.mny if persistent.mny is not None else 0) + 1000), Function(init_persistent_vars)]:
                text_size 18
                text_color "#00ff00"
                background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                padding (12, 4)
            
            text "{size=20}{color=#00ff00}$[persistent.mny if persistent.mny is not None else 0]{/color}{/size}" xsize 80 text_align 0.5
        
        # Gallery section
        null height 15
        
        hbox:
            spacing 10
            xalign 0.5
            
            text "{size=24}{color=#00ff00}Unlock Gallery:{/color}{/size}"
            
            # Toggle switch
            if persistent.gallery_unlocked:
                textbutton "{size=18}{color=#00ff00}UNLOCKED{/color}{/size}" action [Function(lock_all_gallery), Function(init_persistent_vars)]:
                    background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (15, 6)
            else:
                textbutton "{size=18}{color=#ff4444}LOCKED{/color}{/size}" action [Function(unlock_all_gallery), Function(init_persistent_vars)]:
                    background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (15, 6)

# Corruption Tab Content - FIXED
screen corruption_tab():
    vbox:
        spacing 15
        xfill True
        
        # Section title
        text "{size=28}{color=#00ff00}CORRUPTION{/color}{/size}" xalign 0.5
        
        # Sister corruption
        hbox:
            spacing 10
            xalign 0.5
            
            text "{size=20}{color=#ffff00}Sister:{/color}{/size}" xsize 120
            
            bar:
                value (persistent.scorr if persistent.scorr is not None else 0)
                range 100
                xsize 250
                ysize 18
                left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
            
            textbutton "+10" action [SetField(persistent, "scorr", min(100, (persistent.scorr if persistent.scorr is not None else 0) + 10)), Function(init_persistent_vars)]:
                text_size 18
                text_color "#00ff00"
                background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                padding (12, 4)
            
            text "{size=20}{color=#00ff00}[persistent.scorr if persistent.scorr is not None else 0]{/color}{/size}" xsize 40 text_align 0.5
        
        # Mother corruption
        hbox:
            spacing 10
            xalign 0.5
            
            text "{size=20}{color=#ffff00}Mother:{/color}{/size}" xsize 120
            
            bar:
                value (persistent.mcorr if persistent.mcorr is not None else 0)
                range 100
                xsize 250
                ysize 18
                left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
                right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
            
            textbutton "+10" action [SetField(persistent, "mcorr", min(100, (persistent.mcorr if persistent.mcorr is not None else 0) + 10)), Function(init_persistent_vars)]:
                text_size 18
                text_color "#00ff00"
                background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                padding (12, 4)
            
            text "{size=20}{color=#00ff00}[persistent.mcorr if persistent.mcorr is not None else 0]{/color}{/size}" xsize 40 text_align 0.5

# Add mod button to existing quick menu
screen mod_overlay():
    zorder 100
    
    # Modern Enhanced Mod Button positioned separately
    hbox:
        xalign 1.0
        yalign 1.0
        textbutton "{color=#00ff00}Enhanced Mod{/color}" action [ShowMenu("enhanced_joker_mod"), Function(init_persistent_vars)]:
            text_size 16
            background None
            hover_background None
            padding (10, 5)

# Add mod button overlay
init python:
    config.overlay_screens.append("mod_overlay")

# Add hotkey for quick access (K key)
define config.keymap['enhanced_mod'] = ['K']
init python:
    config.underlay.append(renpy.Keymap(enhanced_mod=[ShowMenu("enhanced_joker_mod"), Function(init_persistent_vars)]))