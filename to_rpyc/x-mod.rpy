# ========================================
# Enhanced Mod Menu - Modified for Emma Game
# Features: Stats, Relationships, Money, Gallery
# ========================================

# IMPORTANT: Define variables with 'default' for proper saving
default current_tab = "stats"

init python:
    # Mod Configuration
    mod_author = Character("ModAuthor", color="#FFD700")
    
    # Gallery unlock function - adjust based on game's gallery system
    def unlock_all_gallery():
        # Set gallery mode and unlock persistent variables
        store.for_gallery = True
        # Add any other gallery unlock logic here if needed
        renpy.notify("Gallery Mode Enabled!")
    
    def lock_all_gallery():
        store.for_gallery = False
        renpy.notify("Gallery Mode Disabled!")

# Main Enhanced Mod Screen
screen enhanced_mod_menu():
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
            
            # Header with exit and save buttons
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
            
            # Tab navigation
            hbox:
                xalign 0.5
                spacing 30
                
                textbutton "EMMA STATS" action SetScreenVariable("current_tab", "stats"):
                    if current_tab == "stats":
                        text_color "#00ff00"
                        text_size 20
                        background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    else:
                        text_color "#888888"
                        text_size 20
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (25, 12)
                
                textbutton "RELATIONSHIPS" action SetScreenVariable("current_tab", "relationship"):
                    if current_tab == "relationship":
                        text_color "#00ff00"
                        text_size 20
                        background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    else:
                        text_color "#888888"
                        text_size 20
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (25, 12)
                
                textbutton "EXTRAS" action SetScreenVariable("current_tab", "extras"):
                    if current_tab == "extras":
                        text_color "#00ff00"
                        text_size 20
                        background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    else:
                        text_color "#888888"
                        text_size 20
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                    padding (25, 12)
            
            # Content area
            frame:
                background Solid("#333333")
                xfill True
                yfill True
                padding (15, 15)
                
                if current_tab == "stats":
                    use stats_tab()
                elif current_tab == "relationship":
                    use relationship_tab()
                elif current_tab == "extras":
                    use extras_tab()

# Emma Stats Tab Content
screen stats_tab():
    viewport:
        xfill True
        yfill True
        mousewheel True
        draggable True
        scrollbars "vertical"
        
        vbox:
            spacing 20
            
            # Section title
            text "{size=32}{color=#ff88ff}EMMA'S STATS{/color}" xalign 0.5
            
            # Money section
            frame:
                background Solid("#225522")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 20
                    xalign 0.5
                    
                    text "{size=28}{color=#00ff00}MONEY: $[fcs.money]{/color}"
                    
                    textbutton "+$500" action SetField(fcs, "money", fcs.money + 500):
                        text_size 22
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (15, 8)
                    
                    textbutton "+$5000" action SetField(fcs, "money", fcs.money + 5000):
                        text_size 22
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (15, 8)
                    
                    textbutton "MAX MONEY" action SetField(fcs, "money", 999999):
                        text_size 22
                        text_color "#ffaa00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (15, 8)
            
            # Intelligence
            frame:
                background Solid("#444455")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#88aaff}INTELLIGENCE: [fcs.intelligence]{/color}" xsize 200
                    
                    textbutton "+1" action SetField(fcs, "intelligence", fcs.intelligence + 1):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "+10" action SetField(fcs, "intelligence", fcs.intelligence + 10):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetField(fcs, "intelligence", 100):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
            
            # Morality
            frame:
                background Solid("#444455")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#aaffaa}MORALITY: [fcs.morality]{/color}" xsize 200
                    
                    textbutton "-10" action SetField(fcs, "morality", max(0, fcs.morality - 10)):
                        text_size 20
                        text_color "#ff4444"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "+10" action SetField(fcs, "morality", fcs.morality + 10):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetField(fcs, "morality", 100):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
            
            # Corruption
            frame:
                background Solid("#554444")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ff8888}CORRUPTION: [fcs.corruption]{/color}" xsize 200
                    
                    textbutton "+1" action SetField(fcs, "corruption", fcs.corruption + 1):
                        text_size 20
                        text_color "#ff4444"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "+10" action SetField(fcs, "corruption", fcs.corruption + 10):
                        text_size 20
                        text_color "#ff4444"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetField(fcs, "corruption", 100):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
            
            # Desire/Arousal
            frame:
                background Solid("#885544")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ffaa88}DESIRE: [fcs.desire]{/color}" xsize 200
                    
                    textbutton "+1" action SetField(fcs, "desire", fcs.desire + 1):
                        text_size 20
                        text_color "#ff6666"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "+5" action SetField(fcs, "desire", fcs.desire + 5):
                        text_size 20
                        text_color "#ff6666"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "RESET" action SetField(fcs, "desire", 0):
                        text_size 20
                        text_color "#8888ff"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
            
            # Energy
            frame:
                background Solid("#446644")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#aaffaa}ENERGY: [fcs.energy]{/color}" xsize 200
                    
                    textbutton "+1" action SetField(fcs, "energy", fcs.energy + 1):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "+5" action SetField(fcs, "energy", fcs.energy + 5):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetField(fcs, "energy", 100):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
            
            # Exhibitionism
            frame:
                background Solid("#664466")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ff88ff}EXHIBITIONISM: [fcs.exg]{/color}" xsize 200
                    
                    textbutton "+1" action SetField(fcs, "exg", fcs.exg + 1):
                        text_size 20
                        text_color "#ff66ff"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "+5" action SetField(fcs, "exg", fcs.exg + 5):
                        text_size 20
                        text_color "#ff66ff"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetField(fcs, "exg", 100):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
            
            # Intrigue
            frame:
                background Solid("#666644")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ffff66}INTRIGUE: [fcs.intrigue]{/color}" xsize 200
                    
                    textbutton "+1" action SetField(fcs, "intrigue", fcs.intrigue + 1):
                        text_size 20
                        text_color "#ffff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "+5" action SetField(fcs, "intrigue", fcs.intrigue + 5):
                        text_size 20
                        text_color "#ffff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetField(fcs, "intrigue", 100):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
            
            # Submissive
            frame:
                background Solid("#444466")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#8888ff}SUBMISSIVE: [fcs.submissive]{/color}" xsize 200
                    
                    textbutton "+1" action SetField(fcs, "submissive", fcs.submissive + 1):
                        text_size 20
                        text_color "#6666ff"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "+5" action SetField(fcs, "submissive", fcs.submissive + 5):
                        text_size 20
                        text_color "#6666ff"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetField(fcs, "submissive", 100):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
            
            # Fitness (kemungkinan ada)
            frame:
                background Solid("#446666")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#66ffff}FITNESS: [fcs.fitness]{/color}" xsize 200
                    
                    textbutton "+1" action SetField(fcs, "fitness", fcs.fitness + 1):
                        text_size 20
                        text_color "#00ffff"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "+5" action SetField(fcs, "fitness", fcs.fitness + 5):
                        text_size 20
                        text_color "#00ffff"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetField(fcs, "fitness", 100):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
            
            # Appearance (kemungkinan ada)
            frame:
                background Solid("#664455")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ffaacc}APPEARANCE: [fcs.appearance]{/color}" xsize 200
                    
                    textbutton "+1" action SetField(fcs, "appearance", fcs.appearance + 1):
                        text_size 20
                        text_color "#ff99bb"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "+5" action SetField(fcs, "appearance", fcs.appearance + 5):
                        text_size 20
                        text_color "#ff99bb"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetField(fcs, "appearance", 100):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)

# Relationship Tab Content
screen relationship_tab():
    viewport:
        xfill True
        yfill True
        mousewheel True
        draggable True
        scrollbars "vertical"
        
        vbox:
            spacing 20
            
            text "{size=32}{color=#00ff00}RELATIONSHIPS{/color}" xalign 0.5
            
            # Tyler (Husband)
            frame:
                background Solid("#444444")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ffff00}TYLER (Husband): [tyler.love]{/color}" xsize 250
                    
                    textbutton "+1" action SetField(tyler, "love", tyler.love + 1):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "+10" action SetField(tyler, "love", tyler.love + 10):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetField(tyler, "love", 100):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
            
            # Justin
            frame:
                background Solid("#444444")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ffff00}JUSTIN: [justin.love]{/color}" xsize 250
                    
                    textbutton "+1" action SetField(justin, "love", justin.love + 1):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "+10" action SetField(justin, "love", justin.love + 10):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetField(justin, "love", 100):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
            
            # Liliana (Family)
            frame:
                background Solid("#444444")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ff88ff}LILIANA (Family): [liliana.love_fam]{/color}" xsize 250
                    
                    textbutton "+1" action SetField(liliana, "love_fam", liliana.love_fam + 1):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "+5" action SetField(liliana, "love_fam", liliana.love_fam + 5):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetField(liliana, "love_fam", 50):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
            
            # Samantha (Family)
            frame:
                background Solid("#444444")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 15
                    
                    text "{size=24}{color=#ff88ff}SAMANTHA (Family): [samantha.love_fam]{/color}" xsize 250
                    
                    textbutton "+1" action SetField(samantha, "love_fam", samantha.love_fam + 1):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "+5" action SetField(samantha, "love_fam", samantha.love_fam + 5):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)
                    
                    textbutton "MAX" action SetField(samantha, "love_fam", 50):
                        text_size 20
                        text_color "#ff8800"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (10, 5)

# Extras Tab Content
screen extras_tab():
    viewport:
        xfill True
        yfill True
        mousewheel True
        draggable True
        scrollbars "vertical"
        
        vbox:
            spacing 20
            
            text "{size=32}{color=#ff88ff}EXTRAS & CHEATS{/color}" xalign 0.5
            
            # Gallery section
            frame:
                background Solid("#552255")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 30
                    xalign 0.5
                    
                    text "{size=28}{color=#ff88ff}GALLERY MODE{/color}"
                    
                    if for_gallery:
                        textbutton "{size=24}{color=#00ff00}✓ ENABLED{/color}" action Function(lock_all_gallery):
                            background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                            padding (20, 10)
                    else:
                        textbutton "{size=24}{color=#ff4444}✗ DISABLED{/color}" action Function(unlock_all_gallery):
                            background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                            hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                            padding (20, 10)
            
            # Difficulty Changer
            frame:
                background Solid("#445555")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 20
                    xalign 0.5
                    
                    text "{size=24}{color=#88ffff}DIFFICULTY: [difficulty]{/color}"
                    
                    textbutton "CHEAT" action SetVariable("difficulty", "cheat"):
                        text_size 20
                        text_color "#ff4444"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (15, 8)
                    
                    textbutton "EASY" action SetVariable("difficulty", "easy"):
                        text_size 20
                        text_color "#ffaa00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (15, 8)
                    
                    textbutton "NORMAL" action SetVariable("difficulty", "normal"):
                        text_size 20
                        text_color "#00ff00"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (15, 8)
            
            # Time Skip
            frame:
                background Solid("#555544")
                padding (15, 10)
                xfill True
                
                hbox:
                    spacing 20
                    xalign 0.5
                    
                    text "{size=24}{color=#ffffaa}TIME CONTROLS{/color}"
                    
                    textbutton "Skip 1 Hour" action Function(ctime.add, 1):
                        text_size 20
                        text_color "#aaffaa"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (15, 8)
                    
                    textbutton "Skip to Evening" action Function(ctime.set, 19):
                        text_size 20
                        text_color "#ffaaaa"
                        background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.choice_button_tile)
                        padding (15, 8)

# Mod overlay button
screen mod_overlay():
    zorder 100
    
    vbox:
        xalign 1.0
        yalign 0.0
        spacing 5
        
        textbutton "{color=#00ff88}Enhanced Mod{/color}" action ShowMenu("enhanced_mod_menu"):
            text_size 16
            background None
            hover_background None
            padding (10, 5)

init python:
    # Activate overlay
    config.overlay_screens.append("mod_overlay")

# Add hotkey for quick access (M key)
define config.keymap['enhanced_mod'] = ['m']
init python:
    config.underlay.append(renpy.Keymap(enhanced_mod=ShowMenu("enhanced_mod_menu")))