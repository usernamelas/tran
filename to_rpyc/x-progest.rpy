# ===============================================================================
# ENHANCED GAME MONITOR - MULTIPLE STORYLINES TRACKING
# File: enhanced_monitor.rpy
# 
# Expanded monitoring system that tracks progress for all major storylines
# ===============================================================================

init python:
    import os
    import time
    from collections import OrderedDict
    
    def get_key_variables():
        """Get essential variables for progress tracking across all storylines"""
        vars_dict = {}
        
        # Comprehensive variable list covering all major storylines
        all_key_vars = [
            # Core relationships
            "mrel", "srel", "erel", "drel", "prel", "crel",
            # Money and time
            "mny", "Hour", "day", "wk", "totaldays",
            # Elaine business storyline
            "elaine_convince", "cselaine0", "elaineshowsup", "elaineagain", "elainebusiness",
            # Jenny (mom) storyline
            "momspecial", "mommassage", "mombikini", "momnightie", "momprogress",
            # Sarah (sister) storyline
            "sarspecial", "sarmassage", "sarbikini", "sarnightie", "sarprogress",
            # Work/progress
            "bworkstarted", "bworked", "startnework", "workrequest", "promoted",
            # Items and inventory
            "mbikini", "mnightie", "sbikini", "snightie", "mobilephoneacquired", "camerasacquired",
            # Instagram/social media
            "instadone", "instauploads", "binstaexp", "instafollowers",
            # Beach and locations
            "beachdone", "beachelainedone", "beachmomdone", "beachsardone",
            # Daniel storyline
            "danielprogress", "danieltrust", "danielbusiness",
            # Club storyline
            "clubaccess", "clublevel", "viplevel",
            # Special events and flags
            "specialevent", "endingunlocked", "achievements"
        ]
        
        for var_name in all_key_vars:
            try:
                # Try different methods to access variables
                if var_name in store.__dict__:
                    vars_dict[var_name] = store.__dict__[var_name]
                elif hasattr(store, var_name):
                    vars_dict[var_name] = getattr(store, var_name)
                else:
                    vars_dict[var_name] = "NOT_FOUND"
            except Exception as e:
                vars_dict[var_name] = f"ERROR: {str(e)}"
        
        return vars_dict
    
    def check_storyline_progress(storyline_name):
        """Check progress for a specific storyline"""
        variables = get_key_variables()
        
        # Define storyline-specific variables and their target values
        storylines = {
            "elaine": {
                "vars": ["elaine_convince", "erel", "elainebusiness", "cselaine0"],
                "targets": {"elaine_convince": 4, "erel": 200},
                "description": "Elaine Business Storyline"
            },
            "jenny": {
                "vars": ["mrel", "momspecial", "mommassage", "mombikini"],
                "targets": {"mrel": 200, "momspecial": True},
                "description": "Jenny (Mom) Relationship Storyline"
            },
            "sarah": {
                "vars": ["srel", "sarspecial", "sarmassage", "sarbikini"],
                "targets": {"srel": 200, "sarspecial": True},
                "description": "Sarah (Sister) Relationship Storyline"
            },
            "daniel": {
                "vars": ["drel", "danielprogress", "danieltrust", "danielbusiness"],
                "targets": {"drel": 100, "danielbusiness": True},
                "description": "Daniel Business Storyline"
            },
            "work": {
                "vars": ["bworkstarted", "bworked", "promoted", "workrequest"],
                "targets": {"promoted": True, "bworked": 10},
                "description": "Work/Career Progress"
            },
            "social": {
                "vars": ["instadone", "instafollowers", "clubaccess", "viplevel"],
                "targets": {"instafollowers": 1000, "clubaccess": True},
                "description": "Social Media/Club Progress"
            }
        }
        
        if storyline_name not in storylines:
            return f"Storyline '{storyline_name}' not defined. Available: {list(storylines.keys())}"
        
        storyline = storylines[storyline_name]
        print(f"\n=== {storyline['description'].upper()} ===")
        
        # Display current values
        for var in storyline["vars"]:
            value = variables.get(var, "ERROR")
            print(f"{var}: {value}")
        
        # Calculate completion percentage
        completed = 0
        total_targets = len(storyline["targets"])
        
        for var, target in storyline["targets"].items():
            current_val = variables.get(var, 0)
            try:
                if isinstance(target, bool):
                    if current_val == target:
                        completed += 1
                elif isinstance(target, int):
                    if current_val >= target:
                        completed += 1
            except:
                pass
        
        completion = (completed / total_targets) * 100 if total_targets > 0 else 0
        print(f"\nCompletion: {completion:.1f}% ({completed}/{total_targets} targets met)")
        
        return completion
    
    def check_all_storylines():
        """Check progress for all major storylines"""
        storylines = ["elaine", "jenny", "sarah", "daniel", "work", "social"]
        results = {}
        
        print("\n" + "="*50)
        print("COMPREHENSIVE STORYLINE PROGRESS REPORT")
        print("="*50)
        
        for storyline in storylines:
            progress = check_storyline_progress(storyline)
            results[storyline] = progress
        
        print("\n" + "="*50)
        print("OVERALL PROGRESS SUMMARY")
        print("="*50)
        
        for storyline, progress in results.items():
            print(f"{storyline.upper():<10}: {progress:>5.1f}%")
        
        return results
    
    def create_detailed_progress_file():
        """Create comprehensive progress file with all storylines"""
        try:
            # Get variables
            variables = get_key_variables()
            
            # Create report content
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            report_lines = [
                "COMPREHENSIVE GAME PROGRESS REPORT",
                "=" * 60,
                f"Time: {timestamp}",
                f"Game Day: {variables.get('day', 'Unknown')} (Week: {variables.get('wk', 'Unknown')})",
                f"Game Hour: {variables.get('Hour', 'Unknown')}",
                f"Money: {variables.get('mny', 'Unknown')}",
                "",
            ]
            
            # Storyline sections
            storyline_vars = OrderedDict([
                ("CORE RELATIONSHIPS", ["mrel", "srel", "erel", "drel", "prel", "crel"]),
                ("ELAINE STORYLINE", ["elaine_convince", "cselaine0", "elaineshowsup", "elaineagain", "elainebusiness"]),
                ("JENNY (MOM) STORYLINE", ["momspecial", "mommassage", "mombikini", "momnightie", "momprogress"]),
                ("SARAH (SISTER) STORYLINE", ["sarspecial", "sarmassage", "sarbikini", "sarnightie", "sarprogress"]),
                ("DANIEL STORYLINE", ["danielprogress", "danieltrust", "danielbusiness"]),
                ("WORK PROGRESS", ["bworkstarted", "bworked", "startnework", "workrequest", "promoted"]),
                ("ITEMS & INVENTORY", ["mbikini", "mnightie", "sbikini", "snightie", "mobilephoneacquired", "camerasacquired"]),
                ("SOCIAL MEDIA", ["instadone", "instauploads", "binstaexp", "instafollowers"]),
                ("LOCATIONS", ["beachdone", "beachelainedone", "beachmomdone", "beachsardone", "clubaccess", "clublevel"]),
                ("SPECIAL FLAGS", ["specialevent", "endingunlocked", "achievements"])
            ])
            
            for section, vars_list in storyline_vars.items():
                report_lines.extend(["", section.upper(), "-" * 40])
                for var_name in vars_list:
                    value = variables.get(var_name, "NOT_FOUND")
                    report_lines.append(f"{var_name:<25} = {value}")
            
            report_lines.extend(["", "=" * 60, "END REPORT"])
            
            report_content = "\n".join(report_lines)
            
            # Try multiple file paths
            possible_paths = [
                "game_progress.txt",
                "./game_progress.txt", 
                "../game_progress.txt",
                "progress_report.txt"
            ]
            
            success = False
            for path in possible_paths:
                try:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(report_content)
                    print(f"Comprehensive progress report saved to: {path}")
                    success = True
                    break
                except Exception as e:
                    continue
            
            if not success:
                # Fallback: print to console/log
                print("=== COMPREHENSIVE PROGRESS REPORT (FILE SAVE FAILED) ===")
                print(report_content)
                print("=== END REPORT ===")
            
            return report_content
            
        except Exception as e:
            error_msg = f"Enhanced monitor error: {str(e)}"
            print(error_msg)
            return error_msg

# Manual trigger functions
init python:
    def monitor_all():
        """Generate comprehensive progress report immediately"""
        print("Generating comprehensive progress report...")
        create_detailed_progress_file()
        check_all_storylines()
    
    def check_jenny_progress():
        """Specific check for Jenny storyline"""
        return check_storyline_progress("jenny")
    
    def check_sarah_progress():
        """Specific check for Sarah storyline"""
        return check_storyline_progress("sarah")
    
    def check_daniel_progress():
        """Specific check for Daniel storyline"""
        return check_storyline_progress("daniel")
    
    def check_work_progress():
        """Specific check for Work storyline"""
        return check_storyline_progress("work")
    
    def check_social_progress():
        """Specific check for Social storyline"""
        return check_storyline_progress("social")

# Enhanced UI screen
screen enhanced_monitor():
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 400
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            
            text "Enhanced Game Monitor" size 24 xalign 0.5
            
            vbox:
                spacing 10
                textbutton "Comprehensive Report" action Function(monitor_all)
                textbutton "Check All Storylines" action Function(check_all_storylines)
                
                hbox:
                    spacing 10
                    textbutton "Elaine" action Function(check_elaine_progress)
                    textbutton "Jenny" action Function(check_jenny_progress)
                    textbutton "Sarah" action Function(check_sarah_progress)
                
                hbox:
                    spacing 10
                    textbutton "Daniel" action Function(check_daniel_progress)
                    textbutton "Work" action Function(check_work_progress)
                    textbutton "Social" action Function(check_social_progress)
            
            textbutton "Close" action Hide("enhanced_monitor") xalign 0.5

# Replace the monitor button with enhanced version
screen monitor_button():
    textbutton "MONITOR":
        text_size 14
        xalign 0.95
        yalign 0.02
        action Show("enhanced_monitor")

# Uncomment to add monitor button
# config.overlay_screens.append("monitor_button")

# Initialize
init python:
    def init_enhanced_monitor():
        print("Enhanced Game Monitor loaded")
        print("Use monitor_all() or check_[storyline]_progress() commands")
    
    config.start_callbacks.append(init_enhanced_monitor)
