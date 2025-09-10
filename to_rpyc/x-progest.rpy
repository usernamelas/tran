# ===============================================================================
# MODULAR GAME MONITOR SYSTEM - MAIN FILE
# File: x-monitor.rpy
# 
# Uses x-detected_variables.rpy for comprehensive variable detection
# Creates detailed progress reports with smart categorization and analysis
# ===============================================================================

init python:
    import os
    import time
    
    # Monitor system settings
    monitor_settings = {
        "enabled": True,
        "auto_export_on_save": True,
        "auto_export_on_day_change": True,
        "detailed_logging": True,
        "smart_diagnosis": True,
        "categorized_output": True
    }
    
    # File paths for outputs
    output_files = {
        "main_report": "game_monitor_report.txt",
        "progress_summary": "progress_summary.txt", 
        "elaine_focus": "elaine_progress.txt",
        "diagnosis": "game_diagnosis.txt"
    }
    
    def create_main_report():
        """Create comprehensive report using detected variables"""
        try:
            # Get all variables from the variable detection system
            all_variables = get_all_game_variables()
            
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            
            # Build main report
            report_lines = [
                "=" * 80,
                "COMPREHENSIVE GAME MONITOR REPORT",
                "=" * 80,
                f"Generated: {timestamp}",
                f"Total Variables Tracked: {len(all_variables)}",
                ""
            ]
            
            # Current game state summary
            report_lines.extend([
                "CURRENT GAME STATE:",
                "-" * 40,
                f"Day: {all_variables.get('day', 'Unknown')} ({all_variables.get('dayname', 'Unknown')})",
                f"Hour: {all_variables.get('Hour', 'Unknown')}",
                f"Money: ${all_variables.get('mny', 0)}",
                ""
            ])
            
            # Critical progression variables
            report_lines.extend([
                "CRITICAL PROGRESSION STATUS:",
                "-" * 40,
                f"Jenny Relationship (mrel): {all_variables.get('mrel', 0)}",
                f"Sister Relationship (srel): {all_variables.get('srel', 0)}",
                f"Elaine Relationship (erel): {all_variables.get('erel', 0)}",
                f"Elaine Business (elaine_convince): {all_variables.get('elaine_convince', 0)}",
                f"Elaine Progress (cselaine0): {all_variables.get('cselaine0', 0)}",
                f"Work Started: {all_variables.get('bworkstarted', 0)}",
                f"New Work: {all_variables.get('startnework', 0)}",
                ""
            ])
            
            # Items and acquisitions
            report_lines.extend([
                "ITEMS & ACQUISITIONS:",
                "-" * 40,
                f"Mobile Phone: {all_variables.get('mobilephoneacquired', 0)}",
                f"Cameras: {all_variables.get('camerasacquired', 0)}",
                f"Jenny Bikini: {all_variables.get('mbikini', 0)}",
                f"Jenny Nightie: {all_variables.get('mnightie', 0)}",
                f"Sister Bikini 1: {all_variables.get('bikini1', 0)}",
                f"Sister Bikini 2: {all_variables.get('bikini2', 0)}",
                f"Bought Followers: {all_variables.get('bought_followers', 0)}",
                ""
            ])
            
            # Content progression
            report_lines.extend([
                "CONTENT PROGRESSION:",
                "-" * 40,
                f"Instagram Done: {all_variables.get('instadone', 0)}",
                f"Hot Photos Done: {all_variables.get('hotphotos_done', 0)}",
                f"Beach Done: {all_variables.get('beachdone', 0)}",
                f"Beach Elaine Done: {all_variables.get('beachelainedone', 0)}",
                f"Nude Beach Talk: {all_variables.get('nudebeachtalk', 0)}",
                f"Girls Night: {all_variables.get('gnight', 0)}",
                ""
            ])
            
            # Character-specific progress
            report_lines.extend([
                "CHARACTER PROGRESS:",
                "-" * 40,
                f"Jenny Corruption (mcorr): {all_variables.get('mcorr', 0)}",
                f"Jenny Sex: {all_variables.get('msex', 0)}",
                f"Sister Corruption (scorr): {all_variables.get('scorr', 0)}",
                f"Sister Action: {all_variables.get('saction', 0)}",
                f"Sister Blowjob: {all_variables.get('sblowjobdone', 0)}",
                f"Rowena Kiss: {all_variables.get('rkiss', 0)}",
                ""
            ])
            
            # Business and work
            report_lines.extend([
                "BUSINESS & WORK:",
                "-" * 40,
                f"Daniel Work: {all_variables.get('bworked', 0)}",
                f"Melinda Contact: {all_variables.get('callmel', 0)}",
                f"Camera Recording: {all_variables.get('camerarecording', 0)}",
                f"Hall Camera: {all_variables.get('hallcamera', 0)}",
                f"Work Request: {all_variables.get('workrequest', 0)}",
                ""
            ])
            
            if monitor_settings["detailed_logging"]:
                # Detailed variable dump by category
                report_lines.extend([
                    "DETAILED VARIABLE DUMP:",
                    "-" * 40,
                    ""
                ])
                
                # Categorize variables
                categories = {
                    "Relationships": ["mrel", "srel", "erel", "melrel", "sm_rel"],
                    "Time & Progress": ["Hour", "day", "dayname", "wk"],
                    "Money & Items": ["mny", "mbikini", "mnightie", "mobilephoneacquired", "camerasacquired"],
                    "Elaine Business": ["elaine_convince", "cselaine0", "elaineshowsup", "elaineagain", "e_showsupagain"],
                    "Work System": ["bworkstarted", "bworked", "startnework", "workrequest", "meldan", "melsw"],
                    "Instagram & Content": ["instadone", "instauploads", "hotphotos_done", "binstaexp", "smobilegiven"],
                    "Beach Activities": ["beachdone", "beachelainedone", "beachrowenadone", "beachalone", "mvisitnudebeach"],
                    "Character Stats": ["mcorr", "mdom", "msex", "scorr", "sdom", "saction"],
                    "Story Events": ["gnight", "cherylevent", "rowenacall", "pornchanel", "lesbianchannel"]
                }
                
                for category, var_list in categories.items():
                    report_lines.append(f"{category}:")
                    for var in sorted(var_list):
                        if var in all_variables:
                            value = all_variables[var]
                            report_lines.append(f"  {var:<25} = {value}")
                    report_lines.append("")
                
                # All other variables (alphabetical)
                categorized_vars = set()
                for var_list in categories.values():
                    categorized_vars.update(var_list)
                
                other_vars = sorted(set(all_variables.keys()) - categorized_vars)
                if other_vars:
                    report_lines.append("Other Variables:")
                    for var in other_vars:
                        value = all_variables[var]
                        report_lines.append(f"  {var:<25} = {value}")
            
            report_lines.extend(["", "=" * 80, "END REPORT", "=" * 80])
            
            # Save to file
            report_content = "\n".join(report_lines)
            save_report_to_file(output_files["main_report"], report_content)
            
            return report_content
            
        except Exception as e:
            error_msg = f"Error creating main report: {str(e)}"
            print(error_msg)
            return error_msg
    
    def create_elaine_focus_report():
        """Create focused report for Elaine storyline progression"""
        try:
            all_variables = get_all_game_variables()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            
            report_lines = [
                "=" * 60,
                "ELAINE STORYLINE FOCUS REPORT", 
                "=" * 60,
                f"Generated: {timestamp}",
                ""
            ]
            
            # Current status
            elaine_convince = all_variables.get('elaine_convince', 0)
            cselaine0 = all_variables.get('cselaine0', 0)
            mrel = all_variables.get('mrel', 0)
            erel = all_variables.get('erel', 0)
            day = all_variables.get('day', 0)
            hour = all_variables.get('Hour', 0)
            
            report_lines.extend([
                "CURRENT STATUS:",
                f"  Game Day: {day} (Sunday = 7)",
                f"  Game Hour: {hour} (Target = 18)",
                f"  Elaine Business Level: {elaine_convince} / 4",
                f"  Elaine Progress Tracker: {cselaine0}",
                f"  Jenny Relationship: {mrel} (Need 200+)",
                f"  Elaine Relationship: {erel}",
                ""
            ])
            
            # Requirements check
            report_lines.extend([
                "REQUIREMENTS CHECK:",
                f"  ✓ Elaine Business Maxed: {'YES' if elaine_convince >= 4 else 'NO - NEED TO DEVELOP'}",
                f"  ✓ Jenny Relationship High: {'YES' if mrel >= 200 else 'NO - NEED ' + str(200-mrel) + ' MORE'}",
                f"  ✓ Correct Day (Sunday): {'YES' if day == 7 else 'NO - WAIT FOR SUNDAY'}",
                f"  ✓ Correct Time (18:00): {'YES' if hour == 18 else 'NO - WAIT FOR 18:00'}",
                ""
            ])
            
            # All Elaine-related variables
            elaine_vars = [
                "elaine_convince", "cselaine0", "elaineshowsup", "elaineagain",
                "elainefuck", "elaineboobs", "e_showsupagain", "erel"
            ]
            
            report_lines.extend([
                "ALL ELAINE VARIABLES:",
                "-" * 30
            ])
            
            for var in elaine_vars:
                value = all_variables.get(var, "NOT_FOUND")
                report_lines.append(f"  {var:<20} = {value}")
            
            report_lines.extend(["", "=" * 60, "END ELAINE REPORT", "=" * 60])
            
            # Save to file
            report_content = "\n".join(report_lines)
            save_report_to_file(output_files["elaine_focus"], report_content)
            
            return report_content
            
        except Exception as e:
            error_msg = f"Error creating Elaine report: {str(e)}"
            print(error_msg)
            return error_msg
    
    def create_smart_diagnosis():
        """Create intelligent diagnosis of current game state"""
        try:
            all_variables = get_all_game_variables()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            
            diagnosis_lines = [
                "=" * 60,
                "SMART GAME DIAGNOSIS",
                "=" * 60,
                f"Generated: {timestamp}",
                ""
            ]
            
            # Get key values
            elaine_convince = int(all_variables.get('elaine_convince', 0))
            mrel = int(all_variables.get('mrel', 0))
            srel = int(all_variables.get('srel', 0))
            erel = int(all_variables.get('erel', 0))
            day = int(all_variables.get('day', 0))
            hour = int(all_variables.get('Hour', 0))
            mny = int(all_variables.get('mny', 0))
            instadone = int(all_variables.get('instadone', 0))
            mobilephoneacquired = int(all_variables.get('mobilephoneacquired', 0))
            
            issues_found = []
            recommendations = []
            
            # Analyze Elaine storyline (main focus)
            diagnosis_lines.append("ELAINE STORYLINE ANALYSIS:")
            if elaine_convince < 4:
                issues_found.append(f"Elaine business underdeveloped ({elaine_convince}/4)")
                recommendations.append("Work with Elaine multiple times, choose professional approaches")
                diagnosis_lines.append(f"  ISSUE: Business relationship needs development ({elaine_convince}/4)")
            else:
                diagnosis_lines.append(f"  GOOD: Elaine business relationship maxed ({elaine_convince}/4)")
            
            if mrel < 200:
                issues_found.append(f"Jenny relationship insufficient ({mrel}/200)")
                recommendations.append("Focus on Jenny relationship building - morning greetings, gifts, quality time")
                diagnosis_lines.append(f"  ISSUE: Jenny relationship too low ({mrel}/200)")
            else:
                diagnosis_lines.append(f"  GOOD: Jenny relationship sufficient ({mrel}/200)")
            
            # Check timing for Sunday scene
            if day == 7 and hour == 18:
                if elaine_convince >= 4 and mrel >= 200:
                    diagnosis_lines.append("  READY: All requirements met for Sunday 18:00 scene!")
                else:
                    diagnosis_lines.append("  TIMING: Correct time but missing requirements")
            else:
                diagnosis_lines.append(f"  TIMING: Wait for Sunday 18:00 (currently {day}/{hour})")
            
            diagnosis_lines.append("")
            
            # Other progression analysis
            diagnosis_lines.append("OTHER PROGRESSION:")
            
            if mobilephoneacquired == 0 and mny >= 500:
                recommendations.append("Consider buying mobile phone for Instagram progression")
                diagnosis_lines.append("  SUGGESTION: Buy mobile phone for content progression")
            
            if instadone == 0 and srel >= 25:
                recommendations.append("Help sister create Instagram page")
                diagnosis_lines.append("  SUGGESTION: Help sister with Instagram setup")
            
            if mny < 100:
                recommendations.append("Focus on earning money through work")
                diagnosis_lines.append(f"  CONCERN: Low money ({mny}) may limit options")
            
            # Summary
            diagnosis_lines.extend([
                "",
                "SUMMARY:",
                f"  Issues Found: {len(issues_found)}",
                f"  Recommendations: {len(recommendations)}",
                ""
            ])
            
            if issues_found:
                diagnosis_lines.append("ISSUES TO ADDRESS:")
                for issue in issues_found:
                    diagnosis_lines.append(f"  - {issue}")
                diagnosis_lines.append("")
            
            if recommendations:
                diagnosis_lines.append("RECOMMENDED ACTIONS:")
                for rec in recommendations:
                    diagnosis_lines.append(f"  - {rec}")
                diagnosis_lines.append("")
            
            diagnosis_lines.extend(["=" * 60, "END DIAGNOSIS", "=" * 60])
            
            # Save to file
            diagnosis_content = "\n".join(diagnosis_lines)
            save_report_to_file(output_files["diagnosis"], diagnosis_content)
            
            return diagnosis_content
            
        except Exception as e:
            error_msg = f"Error creating diagnosis: {str(e)}"
            print(error_msg)
            return error_msg
    
    def save_report_to_file(filename, content):
        """Save report content to file with multiple fallback paths"""
        success = False
        
        # Try multiple paths for Android compatibility
        paths_to_try = [
            filename,
            f"./{filename}",
            f"../{filename}",
            f"game/{filename}",
            f"saves/{filename}"
        ]
        
        for filepath in paths_to_try:
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Report saved: {filepath}")
                success = True
                break
            except:
                continue
        
        if not success:
            print(f"Could not save {filename} to file, output to console:")
            print(content[:500] + "..." if len(content) > 500 else content)
    
    # Main monitoring functions
    def generate_all_reports():
        """Generate all monitoring reports"""
        print("Generating comprehensive game reports...")
        
        try:
            main_report = create_main_report()
            elaine_report = create_elaine_focus_report()
            diagnosis = create_smart_diagnosis()
            
            print(f"Reports generated:")
            print(f"  - {output_files['main_report']}")
            print(f"  - {output_files['elaine_focus']}")
            print(f"  - {output_files['diagnosis']}")
            
            return {
                "main": main_report,
                "elaine": elaine_report,
                "diagnosis": diagnosis
            }
            
        except Exception as e:
            error_msg = f"Error generating reports: {str(e)}"
            print(error_msg)
            return {"error": error_msg}
    
    def quick_status():
        """Quick status check without full reports"""
        try:
            all_variables = get_all_game_variables()
            
            print("\n=== QUICK STATUS ===")
            print(f"Day {all_variables.get('day', '?')}, Hour {all_variables.get('Hour', '?')}")
            print(f"Money: ${all_variables.get('mny', 0)}")
            print(f"Jenny (mrel): {all_variables.get('mrel', 0)}")
            print(f"Sister (srel): {all_variables.get('srel', 0)}")
            print(f"Elaine Business: {all_variables.get('elaine_convince', 0)}/4")
            print(f"Elaine Progress: {all_variables.get('cselaine0', 0)}")
            
        except Exception as e:
            print(f"Quick status error: {str(e)}")
    
    # Auto-monitoring hooks
    def auto_monitor_on_day_change():
        """Automatically monitor when day changes"""
        if monitor_settings["auto_export_on_day_change"]:
            print("Day changed - generating reports...")
            generate_all_reports()
    
    def auto_monitor_on_save():
        """Automatically monitor when game is saved"""
        if monitor_settings["auto_export_on_save"]:
            print("Game saved - generating reports...")
            generate_all_reports()

# User interface functions
init python:
    def monitor_now():
        """Manual trigger for monitoring"""
        generate_all_reports()
        quick_status()
    
    def monitor_elaine():
        """Focus on Elaine storyline only"""
        create_elaine_focus_report()
        create_smart_diagnosis()
    
    def monitor_toggle():
        """Toggle monitoring system"""
        monitor_settings["enabled"] = not monitor_settings["enabled"]
        status = "ON" if monitor_settings["enabled"] else "OFF"
        print(f"Game Monitor: {status}")

# Initialize monitoring system
init python:
    def initialize_monitor_system():
        """Initialize the modular monitoring system"""
        try:
            print("Modular Game Monitor System initialized")
            print("Available commands:")
            print("  monitor_now() - Generate all reports")
            print("  monitor_elaine() - Focus on Elaine storyline")
            print("  quick_status() - Quick status check")
            print("  monitor_toggle() - Toggle system on/off")
            
            # Generate initial report if enabled
            if monitor_settings["enabled"]:
                print("Generating initial reports...")
                generate_all_reports()
                
        except Exception as e:
            print(f"Monitor initialization error: {str(e)}")
    
    # Add to startup
    config.start_callbacks.append(initialize_monitor_system)

# Day change monitoring
init python:
    monitor_last_day = None
    
    def check_for_day_change():
        """Check for day changes and trigger auto-monitoring"""
        global monitor_last_day
        
        if not monitor_settings["enabled"]:
            return
            
        try:
            current_day = getattr(store, 'day', 0)
            
            if monitor_last_day is None:
                monitor_last_day = current_day
            elif current_day != monitor_last_day:
                print(f"Day changed: {monitor_last_day} -> {current_day}")
                auto_monitor_on_day_change()
                monitor_last_day = current_day
                
        except Exception as e:
            print(f"Day change monitoring error: {str(e)}")
    
    # Add to periodic callbacks
    config.periodic_callbacks.append(check_for_day_change)

"""
=== MODULAR GAME MONITOR SYSTEM ===

REQUIREMENTS:
- x-detected_variables.rpy (for variable detection)

GENERATED FILES:
- game_monitor_report.txt (comprehensive report)
- elaine_progress.txt (Elaine storyline focus)
- game_diagnosis.txt (smart analysis & recommendations)
- progress_summary.txt (quick summary)

MANUAL COMMANDS:
- monitor_now() - Generate all reports
- monitor_elaine() - Elaine-focused analysis  
- quick_status() - Quick console status
- monitor_toggle() - Enable/disable system

AUTO-TRIGGERS:
- Day change (if enabled)
- Game save (if enabled)

This system uses your comprehensive variable detection file
to create detailed, categorized reports with smart analysis
specifically focused on solving your Elaine Sunday 18:00 issue!
"""