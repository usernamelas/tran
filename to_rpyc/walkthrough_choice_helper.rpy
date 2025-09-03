# ===============================================================================
# INDEPENDENT WALKTHROUGH CHOICE HELPER
# File: walkthrough_choice_helper.rpy
# 
# Features:
# - Choice text coloring and icons ONLY
# - No UI interference with existing mod
# - Simple toggle system
# - Works independently from any other mod
# ===============================================================================

# Walkthrough Settings - Independent from other mods
default walkthrough_active = True
default walkthrough_show_effects = True
default walkthrough_show_requirements = True

init python:
    # Walkthrough Color Scheme
    wt_colors = {
        "best": "#00ff00",          # Best choice (bright green)
        "good": "#88ff00",          # Good choice (lime green) 
        "neutral": "#ffffff",       # Neutral choice (white)
        "bad": "#ff4444",           # Bad choice (red)
        "money_pos": "#ffd700",     # Money gain (gold)
        "money_neg": "#ff8888",     # Money loss (light red)
        "relationship": "#ff69b4",  # Relationship gain (pink)
        "special": "#00ffff",       # Special/unique choice (cyan)
        "locked": "#666666"         # Locked/unavailable (gray)
    }
    
    # Walkthrough Icons
    wt_icons = {
        "best": "★",
        "good": "✓", 
        "neutral": "•",
        "bad": "✗",
        "money_pos": "$+",
        "money_neg": "$-",
        "relationship": "♥",
        "special": "◆",
        "locked": "🔒"
    }

# Main walkthrough function - ONLY colors text, no other interference
init python:
    def wt(text, choice_type="neutral", effect="", requirement="", icon=True):
        """
        Walkthrough choice helper function
        
        Args:
            text: Original choice text
            choice_type: Type of choice (best, good, neutral, bad, money_pos, money_neg, relationship, special)
            effect: Description of what this choice does (optional)
            requirement: Requirement to show this choice (optional) 
            icon: Show icon before text (default True)
        """
        
        # Return original text if walkthrough is disabled
        if not walkthrough_active:
            return text
        
        # Check requirements if specified
        if requirement and walkthrough_show_requirements:
            try:
                if not eval(requirement):
                    color = wt_colors["locked"]
                    choice_icon = wt_icons["locked"] if icon else ""
                    lock_text = " [LOCKED]" if requirement else ""
                    return "{color=" + color + "}" + choice_icon + " " + text + lock_text + "{/color}"
            except:
                pass  # If requirement check fails, continue normally
        
        # Get color and icon for choice type
        color = wt_colors.get(choice_type, wt_colors["neutral"])
        choice_icon = wt_icons.get(choice_type, wt_icons["neutral"]) if icon else ""
        
        # Build final text
        result_text = text
        
        # Add effect description if enabled and provided
        if effect and walkthrough_show_effects:
            result_text += " {size=-4}(" + effect + "){/size}"
        
        # Return colored text with icon
        if choice_icon:
            return "{color=" + color + "}" + choice_icon + " " + result_text + "{/color}"
        else:
            return "{color=" + color + "}" + result_text + "{/color}"

# Simple toggle overlay (minimal interference)
screen walkthrough_toggle():
    # Only show if not in menu
    if not renpy.get_screen("enhanced_joker_mod"):
        # Small toggle button in corner
        textbutton "WT":
            if walkthrough_active:
                text_color "#00ff00"
                action ToggleVariable("walkthrough_active")
            else:
                text_color "#666666"  
                action ToggleVariable("walkthrough_active")
            text_size 16
            xalign 0.02
            yalign 0.95
            background None
            hover_background None
            padding (5, 2)

# Add minimal overlay
init python:
    if "mod_overlay" not in [screen.name for screen in config.overlay_screens]:
        config.overlay_screens.append("walkthrough_toggle")

# ===============================================================================
# USAGE EXAMPLES - How to modify existing game choices
# ===============================================================================

# EXAMPLE 1: Basic relationship choice
"""
Original:
menu:
    "Be nice to Jenny":
        $ mrel += 2
        
    "Be rude to Jenny":
        $ mrel -= 1

Modified:
menu:
    "[wt('Be nice to Jenny', 'best', '+2 relationship')]":
        $ mrel += 2
        
    "[wt('Be rude to Jenny', 'bad', '-1 relationship')]":
        $ mrel -= 1
"""

# EXAMPLE 2: Money choices
"""
menu:
    "[wt('Buy expensive gift', 'money_neg', '-$200, +5 relationship', 'mny >= 200')]" if mny >= 200:
        $ mny -= 200
        $ mrel += 5
        
    "[wt('Buy cheap gift', 'money_neg', '-$50, +2 relationship', 'mny >= 50')]" if mny >= 50:
        $ mny -= 50
        $ mrel += 2
        
    "[wt('Don\\'t buy anything', 'neutral', 'save money')]":
        pass
"""

# EXAMPLE 3: Complex story choices
"""
menu:
    "[wt('Tell the truth', 'good', '+3 trust, advance story')]":
        $ trust += 3
        $ story_progress += 1
        
    "[wt('Lie convincingly', 'neutral', 'avoid conflict')]":
        "You manage to avoid the situation."
        
    "[wt('Lie badly', 'bad', '-2 trust, complications')]":
        $ trust -= 2
        $ complications += 1
"""

# EXAMPLE 4: Special/unique choices
"""
menu:
    "[wt('Kiss her', 'special', 'romantic scene', 'mrel >= 100')]" if mrel >= 100:
        jump romantic_kiss_scene
        
    "[wt('Hug her', 'relationship', '+1 relationship')]":
        $ mrel += 1
        
    "[wt('Do nothing', 'neutral')]":
        pass
"""

# EXAMPLE 5: Work/business choices  
"""
menu:
    "[wt('Work with Daniel', 'money_pos', '+$100, 8 hours')]":
        $ mny += 100
        $ Hour += 8
        
    "[wt('Work with Elaine', 'money_pos', '+$80, advance business', 'elaine_convince >= 1')]" if elaine_convince >= 1:
        $ mny += 80
        $ elaine_business += 1
        
    "[wt('Stay home', 'relationship', 'family time, +1 all relationships')]":
        $ mrel += 1
        $ srel += 1
"""

# ===============================================================================
# QUICK REFERENCE - Choice Types
# ===============================================================================

"""
CHOICE TYPES AVAILABLE:

"best"         - ★ Green  - Clearly the best option
"good"         - ✓ Lime   - Good choice, recommended  
"neutral"      - • White  - Neutral, no major consequences
"bad"          - ✗ Red    - Bad choice, negative consequences
"money_pos"    - $+ Gold  - Earns money
"money_neg"    - $- Pink  - Costs money
"relationship" - ♥ Pink   - Improves relationships
"special"      - ◆ Cyan   - Unique/special scene
"locked"       - 🔒 Gray  - Requirements not met

USAGE FORMAT:
[wt("Choice text", "choice_type", "effect description", "requirement")]

EXAMPLES:
[wt("Best choice", "best", "+5 relationship")]
[wt("Expensive option", "money_neg", "-$500, luxury item", "mny >= 500")]
[wt("Special scene", "special", "unique content", "mrel >= 200")]
"""

# ===============================================================================
# PRESET COMBINATIONS - Common Scenarios
# ===============================================================================

init python:
    # Preset functions for common scenarios
    def wt_relationship_gain(text, amount, requirement=""):
        return wt(text, "relationship", f"+{amount} relationship", requirement)
    
    def wt_relationship_loss(text, amount):
        return wt(text, "bad", f"-{amount} relationship")
    
    def wt_money_gain(text, amount):
        return wt(text, "money_pos", f"+${amount}")
    
    def wt_money_cost(text, amount, requirement=""):
        req = f"mny >= {amount}" if not requirement else requirement
        return wt(text, "money_neg", f"-${amount}", req)
    
    def wt_best_choice(text, effect=""):
        return wt(text, "best", effect)
    
    def wt_bad_choice(text, effect=""):
        return wt(text, "bad", effect)
    
    def wt_special_scene(text, requirement="", effect=""):
        return wt(text, "special", effect, requirement)

# ===============================================================================
# USAGE WITH PRESETS
# ===============================================================================

"""
PRESET USAGE EXAMPLES:

menu:
    "[wt_relationship_gain('Compliment her', 3)]":
        $ mrel += 3
        
    "[wt_money_cost('Buy gift', 100)]" if mny >= 100:
        $ mny -= 100
        $ mrel += 2
        
    "[wt_special_scene('Kiss her', 'mrel >= 200', 'romantic scene')]" if mrel >= 200:
        jump kiss_scene
        
    "[wt_best_choice('Perfect response', 'best outcome')]":
        jump best_outcome
"""