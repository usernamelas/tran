# ========================================
# Custom Joker Mod - Enhanced Version
# Features: Relationship Management, Money System, Gallery Unlock
# x-myjokermod.rpy
# ========================================

init python:
    # Mod Configuration
    mod_author = Character("ModAuthor", color="#FFD700")
    mod_green = "{color=#00FF00}"
    mod_red = "{color=#FF0000}"
    mod_gold = "{color=#FFD700}"
    mod_blue = "{color=#00BFFF}"

# Main Cheat Screen
screen my_cheat_mod():
    tag menu
    modal True
    
    # Background
    add "#000000" alpha 0.8
    add Transform("gui/overlay/game_menu.png", zoom=1.0) alpha 0.7 xalign 0.5 yalign 0.5
    
    # Title
    text "{size=80}Enhanced Joker Mod" color "#FFD700" font "gui/font/Roboto-Bold.ttf" xcenter 0.5 ypos 20 outlines [(3, "#000", 0, 5)]
    
    # Close Button
    textbutton "{size=40}Close{/size}" action Return() xpos 50 ypos 50 text_color "#FFFFFF"
    
    # Main Content Area
    viewport:
        xpos 50
        ypos 150
        xsize 1820
        ysize 800
        scrollbars "vertical"
        mousewheel True
        
        vbox:
            spacing 30
            
            # ========== RELATIONSHIP SECTION ==========
            frame:
                background "#222222"
                padding (20, 20)
                has vbox
                spacing 20
                
                text "{size=60}{color=#FFD700}RELATIONSHIP MANAGER{/color}" font "gui/font/Roboto-Bold.ttf"
                
                hbox:
                    spacing 50
                    
                    # Column 1 - Main Characters
                    vbox:
                        spacing 15
                        text "{size=40}{color=#00FF00}Main Characters{/color}"
                        
                        # Sister Relationship (srel)
                        hbox:
                            spacing 20
                            text "{size=30}Sister:" xsize 200
                            bar:
                                value VariableValue("srel", 100)
                                xsize 300
                                ysize 30
                            text "{size=25}[srel]" color "#FFFFFF" xsize 50
                            textbutton "+10" action SetVariable("srel", min(100, srel + 10)) text_size 20
                            textbutton "MAX" action SetVariable("srel", 100) text_size 20
                        
                        # Mother Relationship (mrel)  
                        hbox:
                            spacing 20
                            text "{size=30}Mother:" xsize 200
                            bar:
                                value VariableValue("mrel", 100)
                                xsize 300
                                ysize 30
                            text "{size=25}[mrel]" color "#FFFFFF" xsize 50
                            textbutton "+10" action SetVariable("mrel", min(100, mrel + 10)) text_size 20
                            textbutton "MAX" action SetVariable("mrel", 100) text_size 20
                        
                        # Elaine Relationship (erel)
                        hbox:
                            spacing 20
                            text "{size=30}Elaine:" xsize 200
                            bar:
                                value VariableValue("erel", 100)
                                xsize 300
                                ysize 30
                            text "{size=25}[erel]" color "#FFFFFF" xsize 50
                            textbutton "+10" action SetVariable("erel", min(100, erel + 10)) text_size 20
                            textbutton "MAX" action SetVariable("erel", 100) text_size 20
                        
                        # Melinda Relationship (melrel)
                        hbox:
                            spacing 20
                            text "{size=30}Melinda:" xsize 200
                            bar:
                                value VariableValue("melrel", 100)
                                xsize 300
                                ysize 30
                            text "{size=25}[melrel]" color "#FFFFFF" xsize 50
                            textbutton "+10" action SetVariable("melrel", min(100, melrel + 10)) text_size 20
                            textbutton "MAX" action SetVariable("melrel", 100) text_size 20
                    
                    # Column 2 - Secondary Relationships
                    vbox:
                        spacing 15
                        text "{size=40}{color=#00FF00}Secondary Characters{/color}"
                        
                        # Sister-Mother Relationship (sm_rel)
                        hbox:
                            spacing 20
                            text "{size=30}Sister-Mother:" xsize 200
                            bar:
                                value VariableValue("sm_rel", 100)
                                xsize 300
                                ysize 30
                            text "{size=25}[sm_rel]" color "#FFFFFF" xsize 50
                            textbutton "+10" action SetVariable("sm_rel", min(100, sm_rel + 10)) text_size 20
                            textbutton "MAX" action SetVariable("sm_rel", 100) text_size 20
                        
                        # Mother Relax (mtrelax)
                        hbox:
                            spacing 20
                            text "{size=30}Mother Relax:" xsize 200
                            bar:
                                value VariableValue("mtrelax", 10)
                                xsize 300
                                ysize 30
                            text "{size=25}[mtrelax]" color "#FFFFFF" xsize 50
                            textbutton "+1" action SetVariable("mtrelax", min(10, mtrelax + 1)) text_size 20
                            textbutton "MAX" action SetVariable("mtrelax", 10) text_size 20
                
                # Quick Actions
                hbox:
                    spacing 30
                    textbutton "{size=30}MAX ALL RELATIONSHIPS" action [
                        SetVariable("srel", 100),
                        SetVariable("mrel", 100),
                        SetVariable("erel", 100),
                        SetVariable("melrel", 100),
                        SetVariable("sm_rel", 100),
                        SetVariable("mtrelax", 10)
                    ] text_color "#00FF00"
                    
                    textbutton "{size=30}RESET ALL RELATIONSHIPS" action [
                        SetVariable("srel", 0),
                        SetVariable("mrel", 0),
                        SetVariable("erel", 0),
                        SetVariable("melrel", 0),
                        SetVariable("sm_rel", 0),
                        SetVariable("mtrelax", 0)
                    ] text_color "#FF0000"
            
            # ========== MONEY SECTION ==========
            frame:
                background "#222222"
                padding (20, 20)
                has vbox
                spacing 20
                
                text "{size=60}{color=#FFD700}MONEY MANAGER{/color}" font "gui/font/Roboto-Bold.ttf"
                
                hbox:
                    spacing 50
                    
                    # Main Money (mny)
                    vbox:
                        spacing 15
                        text "{size=40}{color=#00FF00}Main Money{/color}"
                        
                        hbox:
                            spacing 20
                            text "{size=35}Money:" xsize 200
                            bar:
                                value VariableValue("mny", 10000)
                                xsize 400
                                ysize 35
                            text "{size=30}$[mny]" color "#00FF00" xsize 100
                        
                        hbox:
                            spacing 20
                            textbutton "+100" action SetVariable("mny", mny + 100) text_size 25
                            textbutton "+500" action SetVariable("mny", mny + 500) text_size 25
                            textbutton "+1000" action SetVariable("mny", mny + 1000) text_size 25
                            textbutton "MAX" action SetVariable("mny", 10000) text_size 25
                            textbutton "RESET" action SetVariable("mny", 0) text_size 25 text_color "#FF0000"
                    
                    # Sister Money (smoneym)
                    vbox:
                        spacing 15
                        text "{size=40}{color=#00FF00}Sister Money{/color}"
                        
                        hbox:
                            spacing 20
                            text "{size=35}Sister Money:" xsize 200
                            bar:
                                value VariableValue("smoneym", 100)
                                xsize 300
                                ysize 35
                            text "{size=30}[smoneym]" color "#00FF00" xsize 60
                        
                        hbox:
                            spacing 20
                            textbutton "+1" action SetVariable("smoneym", min(100, smoneym + 1)) text_size 25
                            textbutton "+5" action SetVariable("smoneym", min(100, smoneym + 5)) text_size 25
                            textbutton "MAX" action SetVariable("smoneym", 100) text_size 25
            
            # ========== GALLERY UNLOCK SECTION ==========
            frame:
                background "#222222"
                padding (20, 20)
                has vbox
                spacing 20
                
                text "{size=60}{color=#FFD700}GALLERY UNLOCKER{/color}" font "gui/font/Roboto-Bold.ttf"
                
                text "{size=30}{color=#FFFF00}Unlock all gallery images and scenes{/color}"
                
                hbox:
                    spacing 50
                    
                    vbox:
                        spacing 15
                        text "{size=40}{color=#00FF00}Photo Progress{/color}"
                        
                        # S Photos Progress
                        hbox:
                            spacing 20
                            text "{size=30}Sister Photos:" xsize 200
                            bar:
                                value VariableValue("sphotos_progress", 10)
                                xsize 300
                                ysize 30
                            text "{size=25}[sphotos_progress]" color "#FFFFFF" xsize 50
                            textbutton "MAX" action SetVariable("sphotos_progress", 10) text_size 20
                        
                        # Hot Photos Done
                        hbox:
                            spacing 20
                            text "{size=30}Hot Photos:" xsize 200
                            if hotphotos_done:
                                text "{size=25}{color=#00FF00}UNLOCKED{/color}"
                            else:
                                text "{size=25}{color=#FF0000}LOCKED{/color}"
                            textbutton "UNLOCK" action SetVariable("hotphotos_done", 1) text_size 20
                    
                    vbox:
                        spacing 15
                        text "{size=40}{color=#00FF00}Scene Progress{/color}"
                        
                        # Action Scenes
                        hbox:
                            spacing 20
                            text "{size=30}Sister Action:" xsize 200
                            if sactiondone_mast:
                                text "{size=25}{color=#00FF00}UNLOCKED{/color}"
                            else:
                                text "{size=25}{color=#FF0000}LOCKED{/color}"
                            textbutton "UNLOCK" action SetVariable("sactiondone_mast", 1) text_size 20
                        
                        # Blowjob Scene
                        hbox:
                            spacing 20
                            text "{size=30}Sister BJ:" xsize 200
                            if sblowjobdone:
                                text "{size=25}{color=#00FF00}UNLOCKED{/color}"
                            else:
                                text "{size=25}{color=#FF0000}LOCKED{/color}"
                            textbutton "UNLOCK" action SetVariable("sblowjobdone", 1) text_size 20
                
                # Master Gallery Unlock
                hbox:
                    spacing 30
                    textbutton "{size=35}UNLOCK ALL GALLERY" action [
                        SetVariable("sphotos_progress", 10),
                        SetVariable("hotphotos_done", 1),
                        SetVariable("sactiondone_mast", 1),
                        SetVariable("sactiondone_nomast", 1),
                        SetVariable("sblowjobdone", 1),
                        SetVariable("msex", 1),
                        SetVariable("sanal", 1),
                        SetVariable("mphotos", 1),
                        SetVariable("jenopen", 1),
                        SetVariable("elainefuck", 1)
                    ] text_color "#00FF00"
                    
                    textbutton "{size=35}RESET GALLERY" action [
                        SetVariable("sphotos_progress", 0),
                        SetVariable("hotphotos_done", 0),
                        SetVariable("sactiondone_mast", 0),
                        SetVariable("sactiondone_nomast", 0),
                        SetVariable("sblowjobdone", 0),
                        SetVariable("msex", 0),
                        SetVariable("sanal", 0),
                        SetVariable("mphotos", 0),
                        SetVariable("jenopen", 0),
                        SetVariable("elainefuck", 0)
                    ] text_color "#FF0000"
            
            # ========== BONUS FEATURES SECTION ==========
            frame:
                background "#222222"
                padding (20, 20)
                has vbox
                spacing 20
                
                text "{size=60}{color=#FFD700}BONUS FEATURES{/color}" font "gui/font/Roboto-Bold.ttf"
                
                hbox:
                    spacing 50
                    
                    vbox:
                        spacing 15
                        text "{size=40}{color=#00FF00}Character Stats{/color}"
                        
                        # Corruption levels
                        hbox:
                            spacing 20
                            text "{size=30}Sister Corruption:" xsize 200
                            bar:
                                value VariableValue("scorr", 100)
                                xsize 300
                                ysize 30
                            text "{size=25}[scorr]" color "#FFFFFF" xsize 50
                            textbutton "MAX" action SetVariable("scorr", 100) text_size 20
                        
                        hbox:
                            spacing 20
                            text "{size=30}Mother Corruption:" xsize 200
                            bar:
                                value VariableValue("mcorr", 100)
                                xsize 300
                                ysize 30
                            text "{size=25}[mcorr]" color "#FFFFFF" xsize 50
                            textbutton "MAX" action SetVariable("mcorr", 100) text_size 20
                    
                    vbox:
                        spacing 15
                        text "{size=40}{color=#00FF00}Game Progress{/color}"
                        
                        # Day and time controls
                        hbox:
                            spacing 20
                            text "{size=30}Day:" xsize 100
                            text "{size=30}[day]" color "#FFFFFF" xsize 50
                            textbutton "+1" action SetVariable("day", day + 1) text_size 20
                            textbutton "Reset" action SetVariable("day", 1) text_size 20
                        
                        hbox:
                            spacing 20
                            text "{size=30}Hour:" xsize 100
                            text "{size=30}[Hour]" color "#FFFFFF" xsize 50
                            textbutton "+1" action SetVariable("Hour", min(24, Hour + 1)) text_size 20
                            textbutton "Reset" action SetVariable("Hour", 8) text_size 20

# Quick Access Button Integration
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

    # Enhanced Mod Button
    hbox:
        style_prefix "quick"
        xalign 1.0
        yalign 1.0
        textbutton "{color=#FFD700}Enhanced Mod{/color}" action ShowMenu("my_cheat_mod") text_size 16

# Override the original quick menu
init python:
    config.overlay_screens.append("quick_menu")

# Add hotkey for quick access
define config.keymap['mod_menu'] = ['K']
define config.underlay.append(renpy.Keymap(mod_menu=ShowMenu("my_cheat_mod")))

# Initialization message
label start:
    $ renpy.notify("Enhanced Joker Mod Loaded! Press 'K' for quick access or use the button.")
    return