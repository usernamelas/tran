# ===============================================================================
# ENHANCED MONITOR - STANDALONE VERSION
# File: x_enhanced_monitor.rpy
# 
# Tidak perlu edit script.rpy, tidak perlu include statement
# ===============================================================================

init python:
    import os
    import time
    import renpy
    from collections import OrderedDict
    
    # ==================== DYNAMIC VARIABLE LOADING ====================
    
    def load_detected_variables():
        # Dynamic load variables tanpa perlu include statement
        try:
            # Coba akses langsung dari store
            if hasattr(store, 'DETECTED_VARIABLES'):
                return store.DETECTED_VARIABLES
            else:
                # Coba import dari file
                try:
                    renpy.load("x-detected_variables.rpy")
                    if hasattr(store, 'DETECTED_VARIABLES'):
                        return store.DETECTED_VARIABLES
                except:
                    pass
                
                # Fallback: scan manual untuk variabel
                print("Scanning for game variables...")
                all_vars = dir(store)
                game_vars = []
                
                for var_name in all_vars:
                    # Skip internal variables
                    if (not var_name.startswith('_') and 
                        len(var_name) > 2 and
                        not var_name in ['true', 'false', 'null', 'none']):
                        try:
                            value = getattr(store, var_name)
                            game_vars.append(var_name)
                        except:
                            pass
                
                return game_vars[:100]  # Batasi 100 variabel pertama
                
        except Exception as e:
            print(f"Error loading variables: {e}")
            return []
    
    # Load variables sekali saat init
    DETECTED_VARIABLES = load_detected_variables()
    
    # ==================== CORE FUNCTIONS ====================
    
    def get_key_variables():
        # Get all variables dari dynamic loading
        vars_dict = {}
        
        for var_name in DETECTED_VARIABLES:
            try:
                if hasattr(store, var_name):
                    vars_dict[var_name] = getattr(store, var_name)
                else:
                    vars_dict[var_name] = "NOT_FOUND"
            except Exception as e:
                vars_dict[var_name] = f"ERROR: {str(e)}"
        
        return vars_dict
    
    def categorize_variables(variables):
        # Auto-categorize variables based on naming patterns
        categories = {
            "relationships": [],
            "progress": [],
            "items": [],
            "time": [],
            "flags": [],
            "business": [],
            "special": [],
            "other": []
        }
        
        for var_name in variables:
            var_lower = var_name.lower()
            
            # Relationship variables
            if any(keyword in var_lower for keyword in ['rel', 'affection', 'love', 'like', 'trust']):
                categories["relationships"].append(var_name)
            # Progress variables
            elif any(keyword in var_lower for keyword in ['progress', 'stage', 'level', 'phase', 'convince']):
                categories["progress"].append(var_name)
            # Item variables
            elif any(keyword in var_lower for keyword in ['item', 'have', 'acquire', 'buy', 'own', 'bikini', 'nightie']):
                categories["items"].append(var_name)
            # Time variables
            elif any(keyword in var_lower for keyword in ['day', 'time', 'hour', 'week', 'wk', 'month']):
                categories["time"].append(var_name)
            # Business variables
            elif any(keyword in var_lower for keyword in ['business', 'work', 'job', 'career', 'promote']):
                categories["business"].append(var_name)
            # Flag variables
            elif any(keyword in var_lower for keyword in ['flag', 'done', 'complete', 'finish', 'show', 'again']):
                categories["flags"].append(var_name)
            # Special variables
            elif any(keyword in var_lower for keyword in ['special', 'event', 'ending', 'achievement']):
                categories["special"].append(var_name)
            else:
                categories["other"].append(var_name)
        
        return categories
    
    def check_storyline_progress(storyline_name):
        # Check progress for specific storyline
        variables = get_key_variables()
        categories = categorize_variables(DETECTED_VARIABLES)
        
        storyline_patterns = {
            "elaine": ["elaine", "e_", "_e", "business"],
            "jenny": ["mom", "m_", "_m", "mother", "jenny"],
            "sarah": ["sar", "s_", "_s", "sister", "sarah"],
            "daniel": ["dan", "d_", "_d", "daniel"],
            "work": ["work", "job", "career", 'bwork', "promote"],
            "social": ["insta", "social", "club", "follow", "media"],
            "all": []  # All variables
        }
        
        if storyline_name not in storyline_patterns:
            available = list(storyline_patterns.keys())
            return f"Storyline '{storyline_name}' not found. Available: {available}"
        
        print(f"\n=== {storyline_name.upper()} STORYLINE CHECK ===")
        
        # Find matching variables
        matches = []
        patterns = storyline_patterns[storyline_name]
        
        if storyline_name == "all":
            matches = DETECTED_VARIABLES[:50]  # First 50 variables
        else:
            for var_name in DETECTED_VARIABLES:
                var_lower = var_name.lower()
                if any(pattern in var_lower for pattern in patterns):
                    matches.append(var_name)
        
        # Display results
        for var in sorted(matches):
            value = variables.get(var, "NOT_FOUND")
            print(f"{var}: {value}")
        
        return len(matches)
    
    def check_all_storylines():
        # Check progress for all major storylines
        storylines = ["elaine", "jenny", "sarah", "daniel", "work", "social"]
        
        print("\n" + "="*60)
        print("COMPREHENSIVE STORYLINE PROGRESS REPORT")
        print("="*60)
        
        results = {}
        for storyline in storylines:
            count = check_storyline_progress(storyline)
            results[storyline] = count
            print(f"Found {count} variables for {storyline}")
            print("-" * 40)
        
        return results
    
    def create_detailed_progress_file():
        # Create comprehensive progress file with categorized variables
        try:
            variables = get_key_variables()
            categories = categorize_variables(DETECTED_VARIABLES)
            
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            report_lines = [
                "ENHANCED GAME PROGRESS REPORT",
                "=" * 70,
                f"Time: {timestamp}",
                f"Total Variables: {len(DETECTED_VARIABLES)}",
                f"Game Day: {variables.get('day', 'N/A')}",
                f"Game Hour: {variables.get('Hour', 'N/A')}",
                f"Money: {variables.get('mny', 'N/A')}",
                "",
            ]
            
            # Add categorized sections
            for category, var_list in categories.items():
                if var_list:  # Only add if category has variables
                    report_lines.extend([
                        "",
                        f"{category.upper()}",
                        "-" * 50
                    ])
                    
                    for var_name in sorted(var_list):
                        value = variables.get(var_name, "NOT_FOUND")
                        report_lines.append(f"{var_name:<25} = {value}")
            
            report_lines.extend(["", "=" * 70, "END REPORT"])
            
            report_content = "\n".join(report_lines)
            
            # Save to file
            possible_paths = [
                "game_progress_full.txt",
                "./enhanced_progress.txt",
                "../game_progress.txt"
            ]
            
            success = False
            for path in possible_paths:
                try:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(report_content)
                    print(f"Full progress report saved to: {path}")
                    success = True
                    break
                except:
                    continue
            
            if not success:
                print("=== FULL PROGRESS REPORT ===")
                print(report_content)
            
            return report_content
            
        except Exception as e:
            error_msg = f"Enhanced monitor error: {str(e)}"
            print(error_msg)
            return error_msg

    # ==================== QUICK CHECK FUNCTIONS ====================
    
    def quick_check():
        # Quick status check with diagnosis
        variables = get_key_variables()
        
        print("\n=== QUICK STATUS CHECK ===")
        print(f"Game Day: {variables.get('day', 'N/A')}")
        print(f"Game Hour: {variables.get('Hour', 'N/A')}")
        print(f"Money: {variables.get('mny', 'N/A')}")
        
        # Check key relationships
        for rel in ['mrel', 'srel', 'erel', 'drel']:
            if rel in variables:
                print(f"{rel}: {variables[rel]}")
        
        return variables
    
    def check_elaine_progress():
        # Specific check for Elaine storyline
        return check_storyline_progress("elaine")
    
    def check_jenny_progress():
        # Specific check for Jenny storyline
        return check_storyline_progress("jenny")
    
    def check_sarah_progress():
        # Specific check for Sarah storyline
        return check_storyline_progress("sarah")
    
    def check_daniel_progress():
        # Specific check for Daniel storyline
        return check_storyline_progress("daniel")
    
    def check_work_progress():
        # Specific check for Work storyline
        return check_storyline_progress("work")
    
    def check_social_progress():
        # Specific check for Social storyline
        return check_storyline_progress("social")
    
    def check_all_variables():
        # Check all detected variables
        return check_storyline_progress("all")

# ==================== MANUAL TRIGGER FUNCTIONS ====================

init python:
    def monitor_all():
        # Generate comprehensive progress report immediately
        print("Generating enhanced progress report...")
        create_detailed_progress_file()
        check_all_storylines()
    
    def monitor_quick():
        # Quick monitoring
        print("Quick monitoring...")
        quick_check()

# ==================== AUTO-MONITORING ====================

init python:
    last_monitored_day = None
    
    def auto_monitor_check():
        # Auto-check on day change
        global last_monitored_day
        
        try:
            current_day = getattr(store, 'day', 0)
            if last_monitored_day is None:
                last_monitored_day = current_day
            elif current_day != last_monitored_day:
                print(f"\n=== DAY CHANGED: {last_monitored_day} -> {current_day} ===")
                quick_check()
                last_monitored_day = current_day
        except:
            pass
    
    config.periodic_callbacks.append(auto_monitor_check)

# ==================== UI SCREENS ====================

screen enhanced_monitor():
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 500
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            
            text "ENHANCED GAME MONITOR" size 28 xalign 0.5
            
            # Main actions
            hbox:
                spacing 10
                textbutton "Full Report" action Function(monitor_all):
                    text_size 18
                    xsize 150
                textbutton "Quick Check" action Function(monitor_quick):
                    text_size 18
                    xsize 150
            
            # Storyline checks
            text "Storyline Checks:" size 20 xalign 0.5
            
            grid 3 2:
                spacing 10
                textbutton "Elaine" action Function(check_elaine_progress)
                textbutton "Jenny" action Function(check_jenny_progress)
                textbutton "Sarah" action Function(check_sarah_progress)
                textbutton "Daniel" action Function(check_daniel_progress)
                textbutton "Work" action Function(check_work_progress)
                textbutton "Social" action Function(check_social_progress)
            
            # Advanced
            text "Advanced:" size 20 xalign 0.5
            hbox:
                spacing 10
                textbutton "All Variables" action Function(check_all_variables)
                textbutton "All Storylines" action Function(check_all_storylines)
            
            textbutton "Close" action Hide("enhanced_monitor") xalign 0.5

# ==================== OVERLAY BUTTON ====================

screen monitor_button():
    textbutton "ENHANCED MON":
        text_size 16
        text_color "#ff9900"
        xalign 0.98
        yalign 0.02
        action Show("enhanced_monitor")
        background None
        hover_background "#ffffff20"

# ==================== INITIALIZATION ====================

init python:
    def init_enhanced_monitor():
        print("Enhanced Game Monitor loaded successfully!")
        print(f"Detected {len(DETECTED_VARIABLES)} game variables")
        print("Use monitor_all() or enhanced monitor UI")
    
    config.start_callbacks.append(init_enhanced_monitor)

# Aktifkan tombol overlay
init python:
    config.overlay_screens.append("monitor_button")