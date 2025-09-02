# ========================================
# Enhanced Joker Mod - Advanced Features
# Additional screens and functionality
# ========================================

# Advanced Settings Screen
screen mod_advanced_settings():
    tag menu
    modal True
    
    add "#000000" alpha 0.8
    add Transform(Solid("#000000"), zoom=1.0, alpha=0.7, xalign=0.5, yalign=0.5)
    
    text "{size=70}Advanced Mod Settings" color "#FFD700" font "x-font/x-Montserrat-Light.ttf" xcenter 0.5 ypos 30
    
    textbutton "← Back to Main Mod" action ShowMenu("my_cheat_mod") xpos 50 ypos 60 text_size 25
    textbutton "✕ Close" action Return() xpos 1750 ypos 60 text_size 25
    
    viewport:
        xpos 50
        ypos 150
        xsize 1820
        ysize 750
        scrollbars "vertical"
        mousewheel True
        
        vbox:
            spacing 30
            
            # ========== GAME VARIABLES SECTION ==========
            frame:
                background "#1a1a2e"
                padding (20, 20)
                has vbox
                spacing 20
                
                text "{size=50}{color=#FFD700}GAME VARIABLES EDITOR{/color}" font "x-font/x-Montserrat-Light.ttf"
                
                hbox:
                    spacing 50
                    
                    # Column 1 - Time & Progress
                    vbox:
                        spacing 15
                        text "{size=35}{color=#00FF00}Time & Progress{/color}"
                        
                        hbox:
                            spacing 20
                            text "{size=25}Day:" xsize 150
                            bar:
                                value VariableValue("day", 365)
                                xsize 200
                                ysize 25
                            text "{size=20}[day]" color "#FFFFFF" xsize 60
                            textbutton "+7" action SetVariable("day", day + 7) text_size 18
                            textbutton "+30" action SetVariable("day", day + 30) text_size 18
                        
                        hbox:
                            spacing 20
                            text "{size=25}Hour:" xsize 150
                            bar:
                                value VariableValue("Hour", 24)
                                xsize 200
                                ysize 25
                            text "{size=20}[Hour]" color "#FFFFFF" xsize 60
                            textbutton "Morning" action SetVariable("Hour", 8) text_size 18
                            textbutton "Evening" action SetVariable("Hour", 20) text_size 18
                        
                        hbox:
                            spacing 20
                            text "{size=25}Work Week:" xsize 150
                            bar:
                                value VariableValue("wk", 52)
                                xsize 200
                                ysize 25
                            text "{size=20}[wk]" color "#FFFFFF" xsize 60
                            textbutton "+1" action SetVariable("wk", wk + 1) text_size 18
                            textbutton "Reset" action SetVariable("wk", 0) text_size 18
                    
                    # Column 2 - Character Stats
                    vbox:
                        spacing 15
                        text "{size=35}{color=#00FF00}Character Development{/color}"
                        
                        hbox:
                            spacing 20
                            text "{size=25}Sister Dom:" xsize 150
                            bar:
                                value VariableValue("sdom", 100)
                                xsize 200
                                ysize 25
                            text "{size=20}[sdom]" color "#FFFFFF" xsize 60
                            textbutton "MAX" action SetVariable("sdom", 100) text_size 18
                        
                        hbox:
                            spacing 20
                            text "{size=25}Bob Study:" xsize 150
                            bar:
                                value VariableValue("bstudy", 100)
                                xsize 200
                                ysize 25
                            text "{size=20}[bstudy]" color "#FFFFFF" xsize 60
                            textbutton "MAX" action SetVariable("bstudy", 100) text_size 18
                        
                        hbox:
                            spacing 20
                            text "{size=25}Bob Exercise:" xsize 150
                            bar:
                                value VariableValue("bexercise", 100)
                                xsize 200
                                ysize 25
                            text "{size=20}[bexercise]" color "#FFFFFF" xsize 60
                            textbutton "MAX" action SetVariable("bexercise", 100) text_size 18
            
            # ========== ITEM MANAGEMENT SECTION ==========
            frame:
                background "#1a1a2e"
                padding (20, 20)
                has vbox
                spacing 20
                
                text "{size=50}{color=#FFD700}ITEM MANAGEMENT{/color}" font "x-font/x-Montserrat-Light.ttf"
                
                grid 3 4:
                    spacing 20
                    
                    # Clothing Items
                    vbox:
                        text "{size=30}{color=#FFA500}Clothing{/color}"
                        hbox:
                            text "Bikini 1:" xsize 120
                            if bikini1:
                                textbutton "{color=#00FF00}OWNED{/color}" action SetVariable("bikini1", 0) text_size 18
                            else:
                                textbutton "{color=#FF0000}GET{/color}" action SetVariable("bikini1", 1) text_size 18
                        
                        hbox:
                            text "Bikini 2:" xsize 120
                            if bikini2:
                                textbutton "{color=#00FF00}OWNED{/color}" action SetVariable("bikini2", 0) text_size 18
                            else:
                                textbutton "{color=#FF0000}GET{/color}" action SetVariable("bikini2", 1) text_size 18
                        
                        hbox:
                            text "Bikini 3:" xsize 120
                            if bikini3:
                                textbutton "{color=#00FF00}OWNED{/color}" action SetVariable("bikini3", 0) text_size 18
                            else:
                                textbutton "{color=#FF0000}GET{/color}" action SetVariable("bikini3", 1) text_size 18
                        
                        hbox:
                            text "Microskirt:" xsize 120
                            if microskirt1:
                                textbutton "{color=#00FF00}OWNED{/color}" action SetVariable("microskirt1", 0) text_size 18
                            else:
                                textbutton "{color=#FF0000}GET{/color}" action SetVariable("microskirt1", 1) text_size 18
                    
                    # Electronics
                    vbox:
                        text "{size=30}{color=#FFA500}Electronics{/color}"
                        hbox:
                            text "Mobile Phone:" xsize 120
                            if mobilephoneacquired:
                                textbutton "{color=#00FF00}OWNED{/color}" action SetVariable("mobilephoneacquired", 0) text_size 18
                            else:
                                textbutton "{color=#FF0000}GET{/color}" action SetVariable("mobilephoneacquired", 1) text_size 18
                        
                        hbox:
                            text "Cameras:" xsize 120
                            if camerasacquired:
                                textbutton "{color=#00FF00}OWNED{/color}" action SetVariable("camerasacquired", 0) text_size 18
                            else:
                                textbutton "{color=#FF0000}GET{/color}" action SetVariable("camerasacquired", 1) text_size 18
                        
                        hbox:
                            text "Hall Camera:" xsize 120
                            bar:
                                value VariableValue("hallcamera", 3)
                                xsize 100
                                ysize 20
                            text "{size=16}[hallcamera]{/size}" color "#FFFFFF"
                    
                    # Special Items
                    vbox:
                        text "{size=30}{color=#FFA500}Special Items{/color}"
                        hbox:
                            text "Laptop:" xsize 120
                            if laptoprequested:
                                textbutton "{color=#00FF00}OWNED{/color}" action SetVariable("laptoprequested", 0) text_size 18
                            else:
                                textbutton "{color=#FF0000}GET{/color}" action SetVariable("laptoprequested", 1) text_size 18
                        
                        hbox:
                            text "Tickets:" xsize 120
                            bar:
                                value VariableValue("ticketrequested", 5)
                                xsize 100
                                ysize 20
                            text "{size=16}[ticketrequested]{/size}" color "#FFFFFF"
                        
                        textbutton "GET ALL ITEMS" action Function(unlock_all_items) text_size 20 text_color "#00FF00"
            
            # ========== EVENT FLAGS SECTION ==========
            frame:
                background "#1a1a2e"
                padding (20, 20)
                has vbox
                spacing 20
                
                text "{size=50}{color=#FFD700}EVENT FLAGS MANAGER{/color}" font "x-font/x-Montserrat-Light.ttf"
                
                grid 2 1:
                    spacing 50
                    
                    # Column 1 - Character Events
                    vbox:
                        spacing 15
                        text "{size=35}{color=#00FF00}Character Events{/color}"
                        
                        grid 2 6:
                            spacing 10
                            
                            text "Cheryl Intro:" xsize 140
                            if cherylintrodone:
                                textbutton "{color=#00FF00}DONE{/color}" action SetVariable("cherylintrodone", 0) text_size 16
                            else:
                                textbutton "{color=#FF0000}DO{/color}" action SetVariable("cherylintrodone", 1) text_size 16
                            
                            text "Elaine Business:" xsize 140
                            bar:
                                value VariableValue("ebizcheck", 10)
                                xsize 80
                                ysize 20
                            
                            text "Work Started:" xsize 140
                            if bworkstarted:
                                textbutton "{color=#00FF00}YES{/color}" action SetVariable("bworkstarted", 0) text_size 16
                            else:
                                textbutton "{color=#FF0000}START{/color}" action SetVariable("bworkstarted", 1) text_size 16
                            
                            text "Melinda Work:" xsize 140
                            bar:
                                value VariableValue("snameworkmelinda", 5)
                                xsize 80
                                ysize 20
                            
                            text "Instagram Done:" xsize 140
                            bar:
                                value VariableValue("instadone", 3)
                                xsize 80
                                ysize 20
                            
                            text "Beach Events:" xsize 140
                            if beachdone:
                                textbutton "{color=#00FF00}DONE{/color}" action SetVariable("beachdone", 0) text_size 16
                            else:
                                textbutton "{color=#FF0000}DO{/color}" action SetVariable("beachdone", 1) text_size 16
                    
                    # Column 2 - Progress Events
                    vbox:
                        spacing 15
                        text "{size=35}{color=#00FF00}Progress Events{/color}"
                        
                        grid 2 6:
                            spacing 10
                            
                            text "Camera Fixed:" xsize 140
                            bar:
                                value VariableValue("camerafixing", 3)
                                xsize 80
                                ysize 20
                            
                            text "Page Check:" xsize 140
                            if pagecheckdone:
                                textbutton "{color=#00FF00}DONE{/color}" action SetVariable("pagecheckdone", 0) text_size 16
                            else:
                                textbutton "{color=#FF0000}DO{/color}" action SetVariable("pagecheckdone", 1) text_size 16
                            
                            text "Stalk Done:" xsize 140
                            if stalkdone:
                                textbutton "{color=#00FF00}DONE{/color}" action SetVariable("stalkdone", 0) text_size 16
                            else:
                                textbutton "{color=#FF0000}DO{/color}" action SetVariable("stalkdone", 1) text_size 16
                            
                            text "Stewart Called:" xsize 140
                            if stewcalled:
                                textbutton "{color=#00FF00}YES{/color}" action SetVariable("stewcalled", 0) text_size 16
                            else:
                                textbutton "{color=#FF0000}CALL{/color}" action SetVariable("stewcalled", 1) text_size 16
                            
                            text "Research Done:" xsize 140
                            if instresearchdone:
                                textbutton "{color=#00FF00}DONE{/color}" action SetVariable("instresearchdone", 0) text_size 16
                            else:
                                textbutton "{color=#FF0000}DO{/color}" action SetVariable("instresearchdone", 1) text_size 16
                            
                            text "TV Watched:" xsize 140
                            if tvwatched:
                                textbutton "{color=#00FF00}YES{/color}" action SetVariable("tvwatched", 0) text_size 16
                            else:
                                textbutton "{color=#FF0000}WATCH{/color}" action SetVariable("tvwatched", 1) text_size 16
                
                hbox:
                    spacing 30
                    textbutton "{size=25}COMPLETE ALL EVENTS" action Function(complete_all_events) text_color "#00FF00"
                    textbutton "{size=25}RESET ALL EVENTS" action [
                        SetVariable("cherylintrodone", 0),
                        SetVariable("ebizcheck", 0),
                        SetVariable("bworkstarted", 0),
                        SetVariable("instadone", 0),
                        SetVariable("beachdone", 0),
                        SetVariable("camerafixing", 0),
                        SetVariable("pagecheckdone", 0),
                        SetVariable("stalkdone", 0),
                        SetVariable("stewcalled", 0),
                        SetVariable("instresearchdone", 0),
                        SetVariable("tvwatched", 0)
                    ] text_color "#FF0000"
            
            # ========== MOD PREFERENCES SECTION ==========
            frame:
                background "#1a1a2e"
                padding (20, 20)
                has vbox
                spacing 20
                
                text "{size=50}{color=#FFD700}MOD PREFERENCES{/color}" font "x-font/x-Montserrat-Light.ttf"
                
                hbox:
                    spacing 50
                    
                    vbox:
                        spacing 15
                        text "{size=35}{color=#00FF00}Auto Features{/color}"
                        
                        hbox:
                            textbutton "Auto Max Relationships" action ToggleVariable("persistent.mod_auto_max_rel")
                            if persistent.mod_auto_max_rel:
                                text "{color=#00FF00}ON{/color}"
                            else:
                                text "{color=#FF0000}OFF{/color}"
                        
                        hbox:
                            textbutton "Auto Max Money" action ToggleVariable("persistent.mod_auto_max_money")
                            if persistent.mod_auto_max_money:
                                text "{color=#00FF00}ON{/color}"
                            else:
                                text "{color=#FF0000}OFF{/color}"
                        
                        hbox:
                            textbutton "Show Notifications" action ToggleVariable("persistent.mod_show_notifications")
                            if persistent.mod_show_notifications:
                                text "{color=#00FF00}ON{/color}"
                            else:
                                text "{color=#FF0000}OFF{/color}"
                    
                    vbox:
                        spacing 15
                        text "{size=35}{color=#00FF00}Save/Load Settings{/color}"
                        
                        textbutton "{size=25}Save Mod Settings" action Function(save_mod_settings) text_color "#00FF00"
                        textbutton "{size=25}Load Mod Settings" action Function(load_mod_settings) text_color "#0088FF"
                        textbutton "{size=25}Reset All Progress" action Function(reset_all_progress) text_color "#FF0000"

# Quick Gallery Unlock Screen
screen quick_gallery_unlock():
    tag menu
    modal True
    
    add "#000000" alpha 0.9
    
    text "{size=60}Quick Gallery Unlock" color "#FFD700" xcenter 0.5 ypos 50
    
    textbutton "✕ Close" action Return() xpos 1750 ypos 20 text_size 25
    
    viewport:
        xcenter 0.5
        ypos 150
        xsize 1600
        ysize 700
        
        grid 3 4:
            spacing 50
            
            # Scene unlock buttons
            vbox:
                text "{size=30}{color=#FF69B4}Sister Scenes{/color}"
                textbutton "Sister Photos" action SetVariable("sphotos_progress", 10) text_size 20
                textbutton "Sister Action" action SetVariable("sactiondone_mast", 1) text_size 20
                textbutton "Sister BJ" action SetVariable("sblowjobdone", 1) text_size 20
                textbutton "Sister Strip" action SetVariable("sstrip", 1) text_size 20
                textbutton "Sister Kiss" action SetVariable("skiss", 1) text_size 20
            
            vbox:
                text "{size=30}{color=#FF69B4}Mother Scenes{/color}"
                textbutton "Mother Sex" action SetVariable("msex", 1) text_size 20
                textbutton "Mother Photos" action SetVariable("mphotos", 1) text_size 20
                textbutton "Mother Practice" action SetVariable("mpracticegift", 1) text_size 20
                textbutton "Mother Bikini" action SetVariable("mbikinirequest", 1) text_size 20
                textbutton "Mother Relax" action SetVariable("mtrelax", 10) text_size 20
            
            vbox:
                text "{size=30}{color=#FF69B4}Other Scenes{/color}"
                textbutton "Elaine Fuck" action SetVariable("elainefuck", 1) text_size 20
                textbutton "Jenny Open" action SetVariable("jenopen", 1) text_size 20
                textbutton "Beach Sex" action SetVariable("bs_sex", 1) text_size 20
                textbutton "Rowena Fuck" action SetVariable("rowenabffuck", 1) text_size 20
                textbutton "Nude Beach" action SetVariable("mvisitnudebeach", 1) text_size 20
            
            vbox:
                text "{size=30}{color=#FF69B4}Photo Sets{/color}"
                textbutton "Hot Photos" action SetVariable("hotphotos_done", 1) text_size 20
                textbutton "Lingerie Tease" action SetVariable("jenteaselingerie", 1) text_size 20
                textbutton "Instagram Posts" action SetVariable("nude_binsta_random1_posted", 1) text_size 20
                textbutton "Sister Naked" action SetVariable("snaked_lunch", 2) text_size 20
                textbutton "Photo Progress" action SetVariable("mbphoto", 1) text_size 20
    
    # Quick unlock all button
    textbutton "{size=35}UNLOCK ALL GALLERY" action Function(unlock_all_scenes) xcenter 0.5 ypos 900 text_color "#00FF00"

# Add navigation to main mod screen
init python:
    # Add navigation buttons to main mod
    config.keymap['advanced_mod'] = ['shift_K']
    config.keymap['quick_gallery'] = ['ctrl_G']