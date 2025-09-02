# ========================================
# Enhanced Joker Mod - Configuration File
# Variables and Setup
# ========================================

# Initialize all required variables if they don't exist
init python:
    # Ensure all variables exist with default values
    default_vars = {
        # Relationship Variables
        'srel': 0,          # Sister relationship
        'mrel': 0,          # Mother relationship  
        'erel': 0,          # Elaine relationship
        'melrel': 0,        # Melinda relationship
        'sm_rel': 0,        # Sister-Mother relationship
        'mtrelax': 0,       # Mother relax level
        
        # Money Variables
        'mny': 0,           # Main money
        'smoneym': 0,       # Sister money
        
        # Gallery/Scene Variables
        'sphotos_progress': 0,      # Sister photos progress
        'hotphotos_done': 0,        # Hot photos completion
        'sactiondone_mast': 0,      # Sister action masturbation
        'sactiondone_nomast': 0,    # Sister action no masturbation
        'sblowjobdone': 0,          # Sister blowjob scene
        'msex': 0,                  # Mother sex scene
        'sanal': 0,                 # Sister anal scene
        'mphotos': 0,               # Mother photos
        'jenopen': 0,               # Jenny open scene
        'elainefuck': 0,            # Elaine fuck scene
        
        # Corruption Variables
        'scorr': 0,         # Sister corruption
        'mcorr': 0,         # Mother corruption
        
        # Game Progress Variables
        'day': 1,           # Current day
        'Hour': 8,          # Current hour
        
        # Additional Scene Variables (from value.txt analysis)
        'sburnt': 0,                # Sister burnt status
        'mburnt': 0,                # Mother burnt status
        'bs_sex': 0,                # Beach sex scene
        'cherylintrodone': 0,       # Cheryl introduction
        'ebizcheck': 0,             # Elaine business check
        'hallcamerachecked': 0,     # Hall camera status
        'instadone': 0,             # Instagram completion
        'mobilephoneacquired': 0,   # Mobile phone acquired
        'camerasacquired': 0,       # Cameras acquired
        'ticketrequested': 0,       # Ticket requested
        'mbag': 0,                  # Mother bag
        'mbikini': 0,               # Mother bikini
        'mnightie': 0,              # Mother nightie
        'bikini1': 0,               # Bikini 1
        'bikini2': 0,               # Bikini 2
        'bikini3': 0,               # Bikini 3
        'microskirt1': 0,           # Microskirt 1
        'workrequest': 0,           # Work request
        'bworkstarted': 0,          # Bob work started
        'bworked': 0,               # Bob worked
        'cellshop': 0,              # Cell shop
        'robel': 0,                 # Rob Elaine
        'meldan': 0,                # Melinda Daniel
        'smobilegiven': 0,          # Sister mobile given
        'drinkforbname': 0,         # Drink for b-name
        'coversname': 0,            # Cover s-name
        'showcoverpage': 0,         # Show cover page
        'camerafixing': 0,          # Camera fixing
        'camerarecording': 0,       # Camera recording
        'elaine_convince': 0,       # Elaine convince
        'beachelainedone': 0,       # Beach Elaine done
        'beachdone': 0,             # Beach done
        'beachrowenadone': 0,       # Beach Rowena done
        'startnework': 0,           # Start new work
        'work_intro': 0,            # Work introduction
        'mpracticegift': 0,         # Mother practice gift
        'mbikinirequest': 0,        # Mother bikini request
        'msconvince': 0,            # Mother sister convince
        'laptoprequested': 0,       # Laptop requested
        'etvelaine': 0,             # Evening TV Elaine
        'srbm': 0,                  # Sister room BM
        'rkiss': 0,                 # Rowena kiss
        'shj': 0,                   # Sister handjob
        'sbmrepeat': 0,             # Sister BM repeat
        'nudebeachtalk': 0,         # Nude beach talk
        'bcaught_s': 0,             # Bob caught sister
        'sgtruth': 0,               # Sister game truth
        'b_fightback': 0,           # Bob fightback
        'hidetoiletrowena': 0,      # Hide toilet Rowena
        'rowenadp': 0,              # Rowena DP
        'rowenacall': 0,            # Rowena call
        'rowena_mom': 0,            # Rowena mom
        'toidoorscrew': 0,          # Toilet door screw
        'm_bbruises': 0,            # Mother Bob bruises
        'spiercings': 0,            # Sister piercings
        'mnurse_im': 0,             # Mother nurse image
        'mnurseoutfit': 0,          # Mother nurse outfit
        'stewartcalled': 0,         # Stewart called
        'mbphoto': 0,               # Mother Bob photo
        'thong': 0,                 # Thong
        'mnvylingerie': 0,          # Mother navy lingerie
        'springstring': 0,          # Spring string
        'mmirror': 0,               # Mother mirror
        'hallcamera': 0,            # Hall camera
        'strongdrinksforgirlnight': 0,  # Strong drinks for girl night
        'snamedrink': 0,            # Sister name drink
        'lesbianchannel': 0,        # Lesbian channel
        'pornchanel': 0,            # Porn channel
        'instauploads': 0,          # Instagram uploads
        'nude_binsta_random1_posted': 0,  # Nude Instagram random posted
        'bought_followers': 0,       # Bought followers
        'snameinstaconvinced': 0,   # Sister name Instagram convinced
        'rdf': 0,                   # Rowena date fuck
        'skiss': 0,                 # Sister kiss
        'cvisit': 0,                # Cheryl visit
        'rwena': 0,                 # Rowena
        'stalkb_rowena': 0,         # Stalk Bob Rowena
        'skiss_asked': 0,           # Sister kiss asked
        'snaked_lunch': 0,          # Sister naked lunch
        'wrkquestions': 0,          # Work questions
        'sstrip': 0,                # Sister strip
        'jenteaselingerie': 0,      # Jenny tease lingerie
        'snameworkmelinda': 0,      # Sister name work Melinda
        'beachalone': 0,            # Beach alone
        'naivetalk': 0,             # Naive talk
        'cherylevent': 0,           # Cheryl event
        'cherylfoundout': 0,        # Cheryl found out
        'dphonestolen': 0,          # Daniel phone stolen
        'willmeeting': 0,           # Will meeting
        'melindafiles': 0,          # Melinda files
        'callmel': 0,               # Call Melinda
        'melsw': 0,                 # Melinda switch
        'valshoes': 0,              # Valentine shoes
        'dollnightw': 0,            # Doll night wear
        'msho': 0,                  # Mother shoes
        'chbopen': 0,               # Cheryl Bob open
        'btoldcheryl': 0,           # Bob told Cheryl
        'bnamefixcheryl': 0,        # Bob name fix Cheryl
        'mfuckedsober': 0,          # Mother fucked sober
        'mvisitnudebeach': 0,       # Mother visit nude beach
        'rowena_mom_number': 0,     # Rowena mom number
        'rowena_mom_called': 0,     # Rowena mom called
        's_bbruises': 0,            # Sister Bob bruises
        'browenabm': 0,             # Bob Rowena BM
        'contactrowena': 0,         # Contact Rowena
        'sgrm': 0,                  # Sister game room
        'instresearchdone': 0,      # Instagram research done
        'pagecheckdone': 0,         # Page check done
        'swindowchecked': 0,        # Sister window checked
        'stewcalled': 0,            # Stewart called
        'sroomride': 0,             # Sister room ride
        'hallcameracheckedm': 0,    # Hall camera checked mother
        'stalkdone': 0,             # Stalk done
        'tvwatched': 0,             # TV watched
        'bstudied': 0,              # Bob studied
        'rorepeat': 0,              # Rowena repeat
        'rowenabffuck': 0,          # Rowena boyfriend fuck
        'rowenaslap': 0,            # Rowena slap
        'rvisit': 0,                # Rowena visit
    }
    
    # Check and initialize variables
    for var_name, default_value in default_vars.items():
        if not hasattr(store, var_name):
            setattr(store, var_name, default_value)

# Define default values for variables that should exist
define srel = 0
define mrel = 0
define erel = 0
define melrel = 0
define sm_rel = 0
define mtrelax = 0
define mny = 0
define smoneym = 0
define sphotos_progress = 0
define hotphotos_done = 0
define sactiondone_mast = 0
define sactiondone_nomast = 0
define sblowjobdone = 0
define msex = 0
define sanal = 0
define mphotos = 0
define jenopen = 0
define elainefuck = 0
define scorr = 0
define mcorr = 0
define day = 1
define Hour = 8

# Utility functions for the mod
init python:
    def unlock_all_scenes():
        """Function to unlock all gallery scenes"""
        store.sphotos_progress = 10
        store.hotphotos_done = 1
        store.sactiondone_mast = 1
        store.sactiondone_nomast = 1
        store.sblowjobdone = 1
        store.msex = 1
        store.sanal = 1
        store.mphotos = 1
        store.jenopen = 1
        store.elainefuck = 1
        store.bs_sex = 1
        store.ebizcheck = 10
        store.instadone = 2
        store.etvelaine = 1
        store.bcaught_s = 1
        store.nudebeachtalk = 1
        store.mfuckedsober = 1
        store.mvisitnudebeach = 1
        store.rowenabffuck = 1
        renpy.notify("All gallery scenes unlocked!")
    
    def max_all_relationships():
        """Function to maximize all relationships"""
        store.srel = 100
        store.mrel = 100
        store.erel = 100
        store.melrel = 100
        store.sm_rel = 100
        store.mtrelax = 10
        renpy.notify("All relationships maximized!")
    
    def max_money():
        """Function to maximize money"""
        store.mny = 10000
        store.smoneym = 100
        renpy.notify("Money maximized!")
    
    def unlock_all_items():
        """Function to unlock all items and equipment"""
        store.mobilephoneacquired = 1
        store.camerasacquired = 1
        store.bikini1 = 1
        store.bikini2 = 1
        store.bikini3 = 1
        store.microskirt1 = 1
        store.mbag = 1
        store.mbikini = 1
        store.mnightie = 1
        store.mnvylingerie = 1
        store.springstring = 1
        store.mmirror = 1
        store.hallcamera = 1
        store.thong = 1
        store.mnurseoutfit = 1
        renpy.notify("All items unlocked!")
    
    def complete_all_events():
        """Function to complete all major events"""
        store.cherylintrodone = 1
        store.ebizcheck = 10
        store.hallcamerachecked = 1
        store.instadone = 2
        store.ticketrequested = 4
        store.workrequest = 2
        store.bworkstarted = 1
        store.cellshop = 1
        store.smobilegiven = 1
        store.camerafixing = 2
        store.camerarecording = 1
        store.elaine_convince = 4
        store.beachelainedone = 1
        store.beachdone = 1
        store.beachrowenadone = 1
        store.startnework = 1
        store.work_intro = 1
        store.mpracticegift = 1
        store.laptoprequested = 1
        store.stewartcalled = 1
        store.instresearchdone = 1
        store.pagecheckdone = 1
        renpy.notify("All major events completed!")
    
    def reset_all_progress():
        """Function to reset all progress"""
        # Reset relationships
        store.srel = 0
        store.mrel = 0
        store.erel = 0
        store.melrel = 0
        store.sm_rel = 0
        store.mtrelax = 0
        
        # Reset money
        store.mny = 0
        store.smoneym = 0
        
        # Reset gallery
        store.sphotos_progress = 0
        store.hotphotos_done = 0
        store.sactiondone_mast = 0
        store.sactiondone_nomast = 0
        store.sblowjobdone = 0
        store.msex = 0
        store.sanal = 0
        store.mphotos = 0
        store.jenopen = 0
        store.elainefuck = 0
        
        # Reset corruption
        store.scorr = 0
        store.mcorr = 0
        
        renpy.notify("All progress reset!")

# Auto-save functionality for mod settings
init python:
    import json
    import os
    
    def save_mod_settings():
        """Save current mod settings to file"""
        settings = {
            'srel': store.srel,
            'mrel': store.mrel,
            'erel': store.erel,
            'melrel': store.melrel,
            'sm_rel': store.sm_rel,
            'mtrelax': store.mtrelax,
            'mny': store.mny,
            'smoneym': store.smoneym,
            'scorr': store.scorr,
            'mcorr': store.mcorr
        }
        
        try:
            config_dir = renpy.config.savedir
            if not config_dir:
                config_dir = renpy.config.gamedir
            
            settings_path = os.path.join(config_dir, "mod_settings.json")
            with open(settings_path, 'w') as f:
                json.dump(settings, f, indent=2)
            renpy.notify("Mod settings saved!")
        except:
            renpy.notify("Failed to save mod settings")
    
    def load_mod_settings():
        """Load mod settings from file"""
        try:
            config_dir = renpy.config.savedir
            if not config_dir:
                config_dir = renpy.config.gamedir
            
            settings_path = os.path.join(config_dir, "mod_settings.json")
            if os.path.exists(settings_path):
                with open(settings_path, 'r') as f:
                    settings = json.load(f)
                
                # Apply loaded settings
                for key, value in settings.items():
                    if hasattr(store, key):
                        setattr(store, key, value)
                
                renpy.notify("Mod settings loaded!")
            else:
                renpy.notify("No saved mod settings found")
        except:
            renpy.notify("Failed to load mod settings")

# Persistent data for mod preferences
default persistent.mod_auto_max_rel = False
default persistent.mod_auto_max_money = False
default persistent.mod_show_notifications = True
default persistent.mod_quick_access = True

# Startup notification
label after_load:
    if persistent.mod_show_notifications:
        $ renpy.notify("Enhanced Joker Mod Ready!")
    return