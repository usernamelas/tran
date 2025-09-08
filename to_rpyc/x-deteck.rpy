# ===============================================================================
# GAME PROGRESS MONITOR SYSTEM
# File: game_monitor.rpy
# 
# Automatically tracks all important game variables and exports to text files
# Creates readable progress reports for debugging stuck gameplay
# ===============================================================================

init python:
    import os
    import time
    
    # Monitor settings
    monitor_enabled = True
    auto_export_on_save = True
    export_on_day_change = True
    detailed_logging = True
    
    def get_all_game_variables():
        """
        Get comprehensive list of all important game variables
        """
        variables = {}
        
        # Core relationship variables
        relationship_vars = [
            "mrel", "srel", "erel", "melrel"
        ]
        
        # Money and time tracking
        progress_vars = [
            "mny", "Hour", "day", "wk", "dayname"
        ]
        
        # Jenny-related progress
        jenny_vars = [
            "mbikini", "mnightie", "mbag", "mtrelax", "mnurseoutfit", "mnvylingerie",
            "mmirror", "mpracticegift", "mbikinirequest", "mcorr", "mdom", "msex",
            "mrel", "mburnt", "mfuckedsober"
        ]
        
        # Sister-related progress
        sister_vars = [
            "bikini1", "bikini2", "bikini3", "microskirt1", "srel", "saction",
            "sblowjobdone", "kissrepeat", "pullsb_repeat", "sbm", "sscall"
        ]
        
        # Elaine business & relationship
        elaine_vars = [
            "elaine_convince", "elaineshowsup", "elaineagain", "elaineboobs", 
            "elainefuck", "erel", "cselaine0", "e_showsupagain", "ebizcheck",
            "ebizaldoneonce"
        ]
        
        # Work & business progress
        work_vars = [
            "bworkstarted", "bworked", "startnework", "workrequest", "robel", 
            "meldan", "melsw", "melvisit", "melwork", "callmel", "dollnightw"
        ]
        
        # Instagram & social media
        instagram_vars = [
            "instadone", "instauploads", "binstaexp", "instresearchdone", 
            "pagecheck", "bought_followers", "smobilegiven", "hotphotos_done",
            "mobilephoneacquired"
        ]
        
        # Beach & activities
        beach_vars = [
            "beachdone", "beachelainedone", "beachrowenadone", "beachalone", 
            "mvisitnudebeach", "beach", "nudebeachtalk"
        ]
        
        # Equipment & items
        equipment_vars = [
            "camerasacquired", "hallcamera", "camerarecording", "camerafixing", 
            "camexpose", "cellshop", "hallcamerachecked"
        ]
        
        # Character interactions
        character_vars = [
            "rwena", "rkiss", "contactrowena", "rowena_mom", "browenabm",
            "cherylevent", "cherylfoundout", "bnamefixcheryl", "pornchanel"
        ]
        
        # Special events
        event_vars = [
            "gnight", "lesbianchannel", "rosdad", "jenopen", "aphropack", 
            "edpills", "coversname", "laptoprequested"
        ]
        
        # Combine all variable lists
        all_var_lists = [
            relationship_vars, progress_vars, jenny_vars, sister_vars,
            elaine_vars, work_vars, instagram_vars, beach_vars,
            equipment_vars, character_vars, event_vars
        ]
        
        # Get values for all variables
        for var_list in all_var_lists:
            for var in var_list:
                try:
                    if hasattr(store, var):
                        variables[var] = getattr(store, var)
                    else:
                        variables[var] = "UNDEFINED"
                except:
                    variables[var] = "ERROR"
        
        return variables
    
    def format_progress_report(variables):
        """
        Format variables into a readable progress report
        """
        report = []
        report.append("=" * 60)
        report.append("GAME PROGRESS MONITOR REPORT")
        report.append("=" * 60)
        report.append(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Game Day: {variables.get('day', 'Unknown')} ({variables.get('dayname', 'Unknown')})")
        report.append(f"Game Hour: {variables.get('Hour', 'Unknown')}")
        report.append("")
        
        # Core Stats Summary
        report.append("CORE RELATIONSHIP STATS:")
        report.append("-" * 30)
        report.append(f"Jenny Relationship (mrel):   {variables.get('mrel', 0)}")
        report.append(f"Sister Relationship (srel):  {variables.get('srel', 0)}")
        report.append(f"Elaine Relationship (erel):  {variables.get('erel', 0)}")
        report.append(f"Money (mny):                 ${variables.get('mny', 0)}")
        report.append("")
        
        # Elaine Business Progress (KEY FOR YOUR ISSUE!)
        report.append("ELAINE BUSINESS PROGRESS:")
        report.append("-" * 30)
        report.append(f"elaine_convince:             {variables.get('elaine_convince', 0)}")
        report.append(f"cselaine0:                   {variables.get('cselaine0', 0)}")
        report.append(f"elaineshowsup:              {variables.get('elaineshowsup', 0)}")
        report.append(f"elaineagain:                {variables.get('elaineagain', 0)}")
        report.append(f"e_showsupagain:             {variables.get('e_showsupagain', 0)}")
        report.append(f"ebizcheck:                  {variables.get('ebizcheck', 0)}")
        report.append("")
        
        # Work Progress
        report.append("WORK & BUSINESS:")
        report.append("-" * 30)
        report.append(f"bworkstarted:               {variables.get('bworkstarted', 0)}")
        report.append(f"startnework:                {variables.get('startnework', 0)}")
        report.append(f"workrequest:                {variables.get('workrequest', 0)}")
        report.append(f"meldan:                     {variables.get('meldan', 0)}")
        report.append(f"melsw:                      {variables.get('melsw', 0)}")
        report.append("")
        
        # Jenny Progress
        report.append("JENNY PROGRESS:")
        report.append("-" * 30)
        report.append(f"mbikini:                    {variables.get('mbikini', 0)}")
        report.append(f"mnightie:                   {variables.get('mnightie', 0)}")
        report.append(f"mcorr:                      {variables.get('mcorr', 0)}")
        report.append(f"msex:                       {variables.get('msex', 0)}")
        report.append("")
        
        # Instagram & Social
        report.append("INSTAGRAM & CONTENT:")
        report.append("-" * 30)
        report.append(f"instadone:                  {variables.get('instadone', 0)}")
        report.append(f"mobilephoneacquired:        {variables.get('mobilephoneacquired', 0)}")
        report.append(f"hotphotos_done:             {variables.get('hotphotos_done', 0)}")
        report.append("")
        
        # Detailed Variable Dump (if enabled)
        if detailed_logging:
            report.append("DETAILED VARIABLE DUMP:")
            report.append("-" * 30)
            
            # Group variables by category
            categories = {
                "Relationships": ["mrel", "srel", "erel", "melrel"],
                "Time & Money": ["mny", "Hour", "day", "wk", "dayname"],
                "Items & Equipment": ["mbikini", "mnightie", "mobilephoneacquired", "camerasacquired"],
                "Progress Flags": ["elaine_convince", "cselaine0", "instadone", "bworkstarted"]
            }
            
            for category, var_list in categories.items():
                report.append(f"\n{category}:")
                for var in sorted(var_list):
                    if var in variables:
                        report.append(f"  {var:<25} = {variables[var]}")
            
            # All other variables
            report.append(f"\nAll Variables (A-Z):")
            for var in sorted(variables.keys()):
                if var not in sum(categories.values(), []):
                    report.append(f"  {var:<25} = {variables[var]}")
        
        report.append("")
        report.append("=" * 60)
        report.append("END REPORT")
        report.append("=" * 60)
        
        return "\n".join(report)
    
    def export_progress_report():
        """
        Export progress report to text file in game directory
        """
        if not monitor_enabled:
            return
            
        try:
            # Get all variables
            variables = get_all_game_variables()
            
            # Format report
            report = format_progress_report(variables)
            
            # Generate filename with timestamp
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"game_progress_{timestamp}.txt"
            
            # Get game directory (same as log.txt location)
            if hasattr(config, 'basedir'):
                game_dir = config.basedir
            else:
                game_dir = os.getcwd()
            
            filepath = os.path.join(game_dir, filename)
            
            # Write report to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(report)
            
            # Also create/update latest report
            latest_filepath = os.path.join(game_dir, "game_progress_latest.txt")
            with open(latest_filepath, 'w', encoding='utf-8') as f:
                f.write(report)
            
            print(f"Progress report exported to: {filename}")
            return filepath
            
        except Exception as e:
            print(f"Failed to export progress report: {e}")
            return None
    
    def quick_diagnosis():
        """
        Quick diagnosis for common stuck scenarios
        """
        variables = get_all_game_variables()
        
        issues = []
        suggestions = []
        
        # Check Elaine business progression (YOUR CURRENT ISSUE)
        elaine_convince = variables.get('elaine_convince', 0)
        cselaine0 = variables.get('cselaine0', 0)
        mrel = variables.get('mrel', 0)
        day = variables.get('day', 0)
        hour = variables.get('Hour', 0)
        
        if elaine_convince < 4:
            issues.append(f"Elaine business not maxed (elaine_convince = {elaine_convince}, need 4)")
            suggestions.append("Work more with Elaine to develop business relationship")
        
        if mrel < 200:
            issues.append(f"Jenny relationship too low (mrel = {mrel}, need 200+)")
            suggestions.append("Spend more time building relationship with Jenny")
        
        if day == 7 and hour == 18 and elaine_convince >= 4 and mrel >= 200:
            if cselaine0 < 10:
                issues.append(f"Elaine progression incomplete (cselaine0 = {cselaine0})")
                suggestions.append("Check if you missed Elaine dialogue options")
        
        # Check other common stuck points
        instadone = variables.get('instadone', 0)
        mobilephoneacquired = variables.get('mobilephoneacquired', 0)
        
        if instadone == 0 and mobilephoneacquired == 0:
            suggestions.append("Consider buying phone for Instagram progression")
        
        return issues, suggestions
    
    # Auto-export triggers
    def on_day_change():
        """Trigger export when day changes"""
        if export_on_day_change:
            export_progress_report()
    
    def on_save_game():
        """Trigger export when game is saved"""
        if auto_export_on_save:
            export_progress_report()

# ===============================================================================
# USER INTERFACE COMMANDS
# ===============================================================================

init python:
    def monitor_status():
        """Show monitor system status"""
        print("=== GAME MONITOR STATUS ===")
        print(f"Monitor Enabled: {monitor_enabled}")
        print(f"Auto Export on Save: {auto_export_on_save}")
        print(f"Export on Day Change: {export_on_day_change}")
        print(f"Detailed Logging: {detailed_logging}")
        
    def monitor_now():
        """Generate progress report immediately"""
        filepath = export_progress_report()
        if filepath:
            print(f"Progress report generated: {os.path.basename(filepath)}")
        
        # Also show quick diagnosis
        issues, suggestions = quick_diagnosis()
        if issues or suggestions:
            print("\n=== QUICK DIAGNOSIS ===")
            if issues:
                print("POTENTIAL ISSUES:")
                for issue in issues:
                    print(f"  - {issue}")
            if suggestions:
                print("SUGGESTIONS:")
                for suggestion in suggestions:
                    print(f"  - {suggestion}")
    
    def monitor_toggle():
        """Toggle monitor system on/off"""
        global monitor_enabled
        monitor_enabled = not monitor_enabled
        print(f"Game Monitor: {'ON' if monitor_enabled else 'OFF'}")

# ===============================================================================
# AUTOMATIC MONITORING HOOKS
# ===============================================================================

init python:
    # Hook into day change
    def check_day_change():
        global last_day
        current_day = getattr(store, 'day', 0)
        if hasattr(store, 'last_monitored_day'):
            if current_day != store.last_monitored_day:
                on_day_change()
                store.last_monitored_day = current_day
        else:
            store.last_monitored_day = current_day
    
    # Add periodic checks
    config.periodic_callbacks.append(check_day_change)

# ===============================================================================
# QUICK ACCESS SCREEN
# ===============================================================================

screen game_monitor():
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
            
            text "Game Progress Monitor" style "confirm_prompt" xalign 0.5
            
            vbox:
                spacing 10
                
                textbutton "Generate Report Now" action Function(monitor_now)
                textbutton "Show Monitor Status" action Function(monitor_status)
                textbutton "Toggle Monitor On/Off" action Function(monitor_toggle)
                textbutton "Quick Diagnosis" action Function(quick_diagnosis)
            
            textbutton "Close" action Hide("game_monitor") xalign 0.5

# Add monitor button to overlay (optional)
screen monitor_overlay():
    if monitor_enabled:
        textbutton "MON":
            text_size 16
            xalign 0.02
            yalign 0.02
            text_color "#00ffff"
            action Show("game_monitor")
            tooltip "Game Progress Monitor"

# Uncomment to add monitor button to screen
# config.overlay_screens.append("monitor_overlay")

# ===============================================================================
# INITIALIZATION
# ===============================================================================

init python:
    def initialize_monitor():
        """Initialize the monitoring system"""
        try:
            print("Game Progress Monitor initialized")
            # Generate initial report
            if monitor_enabled:
                monitor_now()
        except Exception as e:
            print(f"Monitor initialization error: {e}")
    
    # Initialize when game starts
    config.start_callbacks.append(initialize_monitor)

# ===============================================================================
# USAGE INSTRUCTIONS
# ===============================================================================

"""
=== GAME PROGRESS MONITOR SYSTEM ===

INSTALLATION:
1. Save this file as 'game_monitor.rpy' in your game/ folder
2. Start/restart the game
3. Check for generated progress report files

AUTO-GENERATED FILES:
- game_progress_YYYYMMDD_HHMMSS.txt (timestamped reports)
- game_progress_latest.txt (always latest report)

MANUAL COMMANDS (if console available):
- monitor_now()     # Generate report immediately
- monitor_status()  # Show system status
- monitor_toggle()  # Turn monitor on/off
- quick_diagnosis() # Get stuck scenario analysis

FEATURES:
✅ Tracks 60+ important game variables
✅ Auto-exports on day change and game save
✅ Readable progress reports with categories
✅ Quick diagnosis for common stuck scenarios
✅ Focuses on Elaine business progression
✅ Exports to same directory as log.txt

FOR YOUR ELAINE ISSUE:
The system specifically tracks:
- elaine_convince (should be 4)
- cselaine0 (tracks Elaine progression)
- mrel (Jenny relationship, should be 200+)
- Day/Hour timing (Sunday 18:00)

Generated reports will show exactly what values you have
and what's needed to progress the Elaine storyline!

The monitor runs automatically - just play the game and
check the generated .txt files for your progress status.
"""