# ===============================================================================
# COMPLETE CHOICE GUIDE IMPLEMENTATION
# File: walkthrough_choices_complete.rpy
# 
# This file contains ALL choice modifications based on variable analysis
# Use this as reference to modify existing game files
# ===============================================================================

# ===============================================================================
# MORNING INTERACTIONS (x-morning_hall.rpy, x-jenmorning.rpy)
# ===============================================================================

"""
# Jenny Morning Conversations
menu jenny_morning_talk:
    "[wt_relationship_gain('Good morning, you look beautiful', 2)]":
        $ mrel += 2
        "Jenny smiles warmly at your compliment."
        
    "[wt('Good morning', 'neutral')]":
        "You exchange normal morning greetings."
        
    "[wt_bad_choice('Ignore her', 'relationship damage')]":
        $ mrel -= 1
        "Jenny looks hurt by your coldness."

# Work Discussion  
menu work_discussion:
    "[wt_best_choice('I want to help support the family', '+2 relationship, unlock work')]":
        $ mrel += 2
        $ wrkquestions = 1
        
    "[wt('I need something to do', 'neutral')]":
        $ wrkquestions = 1
        
    "[wt('I just want money', 'bad', '-1 relationship')]":
        $ mrel -= 1
        $ wrkquestions = 1
"""

# ===============================================================================
# WORK CHOICES (x-map_menu.rpy, x-bworkday.rpy)
# ===============================================================================

"""
# Daily Work Selection
menu daily_work:
    "[wt_money_gain('Work with Daniel', 100)]":
        $ mny += 100
        $ bworked = 1
        $ Hour += 8
        jump daniel_work
        
    "[wt('Work with Elaine', 'money_pos', '+$70-80, business progress', 'elaine_convince >= 1')]" if elaine_convince >= 1:
        $ mny += renpy.random.randint(70, 80)
        $ Hour += 6
        jump elaine_business
        
    "[wt_relationship('Stay home with family', 'family time, +1 all relationships')]":
        $ mrel += 1
        $ srel += 1
        $ Hour += 4

# Shopping Decisions
menu shopping_choices:
    "[wt('Buy bikini for Jenny', 'money_neg', '-$75, +3 relationship, unlock beach', 'mny >= 75')]" if mny >= 75 and mbikini == 0:
        $ mny -= 75
        $ mbikini = 1
        $ mrel += 3
        "Jenny will love this bikini!"
        
    "[wt('Buy phone', 'money_neg', '-$500, unlock Instagram features', 'mny >= 500')]" if mny >= 500 and mobilephoneacquired == 0:
        $ mny -= 500
        $ mobilephoneacquired = 1
        "Essential for Instagram development!"
        
    "[wt('Buy cameras', 'money_neg', '-$200, unlock surveillance', 'mny >= 200')]" if mny >= 200 and camerasacquired == 0:
        $ mny -= 200  
        $ camerasacquired = 1
        "Security cameras acquired!"
        
    "[wt('Save money', 'neutral')]":
        "You decide to save your money for now."
"""

# ===============================================================================
# RELATIONSHIP BUILDING (x-hall_menu1.rpy, x-mroom_menu.rpy)
# ===============================================================================

"""
# Jenny Room Interactions
menu jenny_room_talk:
    "[wt_relationship_gain('Compliment her appearance', 2)]":
        $ mrel += 2
        "Jenny blushes at your kind words."
        
    "[wt('Ask about her day', 'relationship', '+1 relationship')]":
        $ mrel += 1
        "You have a nice conversation about her day."
        
    "[wt('Give her a gift', 'relationship', '+3 relationship, -$50', 'mny >= 50')]" if mny >= 50:
        $ mny -= 50
        $ mrel += 3
        "Jenny is delighted with your thoughtful gift!"
        
    "[wt('Ask to wear bikini', 'special', 'bikini scene', 'mbikini >= 1 and mrel >= 100')]" if mbikini >= 1 and mrel >= 100:
        jump jenny_bikini_scene
        
    "[wt('Leave her alone', 'neutral')]":
        "You decide to give her some privacy."

# Evening TV Time
menu evening_tv:
    "[wt_relationship_gain('Sit close to Jenny', 2)]":
        $ mrel += 2
        "You enjoy watching TV together closely."
        
    "[wt_relationship_gain('Sit close to sister', 2)]":
        $ srel += 2
        "You bond with your sister while watching."
        
    "[wt('Watch alone', 'neutral')]":
        "You watch TV by yourself."
        
    "[wt('Suggest adult channel', 'special', 'adult content', 'pornchanel >= 1')]" if pornchanel >= 1:
        "You suggest watching something more... interesting."
"""

# ===============================================================================
# BEACH EVENTS (x-beachevent.rpy, x-nudebeach_jenny.rpy)
# ===============================================================================

"""
# Beach Invitation
menu beach_invite:
    "[wt_best_choice('Invite Jenny to beach', '+5 relationship, beach scene', 'mbikini >= 1')]" if mbikini >= 1 and beachdone == 0:
        $ mrel += 5
        $ beachdone = 1
        jump jenny_beach_scene
        
    "[wt('Invite Elaine to beach', 'relationship', '+3 Elaine relationship', 'erel >= 50')]" if erel >= 50 and beachelainedone == 0:
        $ erel += 3
        $ beachelainedone = 1
        jump elaine_beach_scene
        
    "[wt('Go to beach alone', 'neutral')]":
        $ beachalone = 1
        jump solo_beach_scene

# Beach Activities
menu beach_activities:
    "[wt_relationship_gain('Help with sunscreen', 3)]":
        $ mrel += 3
        "You help Jenny apply sunscreen... intimately."
        
    "[wt('Compliment her bikini', 'relationship', '+2 relationship')]":
        $ mrel += 2
        "Jenny is happy you like how she looks."
        
    "[wt('Suggest swimming', 'good', '+1 relationship')]":
        $ mrel += 1
        "You both enjoy swimming together."
        
    "[wt('Take photos', 'special', 'photo content', 'mobilephoneacquired == 1')]" if mobilephoneacquired == 1:
        "You take some beautiful photos of Jenny."

# Nude Beach Decision
menu nude_beach:
    "[wt_special_scene('Suggest nude beach', 'srel >= 200', 'nude beach unlock')]" if srel >= 200:
        $ nudebeachtalk = 1
        jump nude_beach_scene
        
    "[wt('Stay at regular beach', 'good')]":
        "You decide to stay at the regular beach."
"""

# ===============================================================================
# INSTAGRAM/PHOTOGRAPHY (x-realinstaphotos.rpy, x-saction_study.rpy)
# ===============================================================================

"""
# Instagram Setup
menu instagram_setup:
    "[wt_best_choice('Help create Instagram page', 'unlock photo content', 'srel >= 25')]" if srel >= 25 and instadone == 0:
        $ instadone = 1
        $ srel += 2
        "You help your sister create her Instagram page."
        
    "[wt('Not interested', 'bad', 'miss content opportunity')]":
        "You decide not to help with Instagram."

# Photo Session Choices  
menu photo_session:
    "[wt('Suggest bikini photos', 'good', '+2 relationship, bikini content', 'bikini1 >= 1 and srel >= 100')]" if bikini1 >= 1 and srel >= 100:
        $ srel += 2
        jump bikini_photo_scene
        
    "[wt('Suggest casual photos', 'neutral', '+1 relationship')]":
        $ srel += 1
        "You take some nice casual photos."
        
    "[wt('Suggest hot photos', 'special', 'hot content', 'srel >= 300')]" if srel >= 300:
        $ hotphotos_done = 1
        jump hot_photo_scene
        
    "[wt('No photos today', 'neutral')]":
        "You decide not to do photos today."

# Photo Quality Decisions
menu photo_quality:
    "[wt_money_cost('Buy professional equipment', 500, 'mny >= 500')]" if mny >= 500:
        $ mny -= 500
        $ photo_quality = 3
        "Professional equipment will make amazing photos!"
        
    "[wt('Use phone camera', 'good', 'decent quality')]":
        $ photo_quality = 2
        "Phone photos turn out pretty good."
        
    "[wt('Use basic camera', 'neutral')]":
        $ photo_quality = 1
        "Basic photos, but still nice memories."
"""

# ===============================================================================
# ELAINE BUSINESS (x-elainebusiness.rpy, x-elaineconjen.rpy)
# ===============================================================================

"""
# First Elaine Meeting
menu elaine_introduction:
    "[wt_best_choice('Professional approach', 'unlock business partnership')]":
        $ elaine_convince = 1
        $ erel += 2
        "Elaine is impressed with your professionalism."
        
    "[wt('Friendly approach', 'good', '+3 relationship')]":
        $ erel += 3
        "Elaine appreciates your friendly demeanor."
        
    "[wt('Flirty approach', 'neutral', '+1 relationship, might complicate business')]":
        $ erel += 1
        "Elaine seems a bit uncertain about mixing business with pleasure."

# Business Development
menu business_expansion:
    "[wt('Suggest camera installation', 'special', 'advance to level 2', 'elaine_convince >= 1')]" if elaine_convince >= 1:
        $ elaine_convince = 2
        $ camerasacquired = 1
        "Elaine agrees to the camera installation plan."
        
    "[wt('Focus on current business', 'good', '+$80')]":
        $ mny += 80
        "You earn good money from current operations."
        
    "[wt('Suggest personal meeting', 'relationship', '+2 relationship', 'erel >= 100')]" if erel >= 100:
        $ erel += 2
        jump elaine_personal_meeting

# Camera Recording Decisions
menu camera_recording:
    "[wt('Record everything', 'special', 'surveillance content', 'camerarecording >= 1')]" if camerarecording >= 1:
        $ camexpose = 1
        "You decide to record for 'business purposes'."
        
    "[wt('Selective recording', 'good', 'moderate content')]":
        "You only record when appropriate."
        
    "[wt('No recording', 'neutral', 'respect privacy')]":
        "You respect everyone's privacy."
"""

# ===============================================================================
# FAMILY INTERACTIONS (x-pdinnerm_relax.rpy, x-evening_jennyout.rpy)
# ===============================================================================

"""
# Dinner Conversations
menu family_dinner:
    "[wt_relationship_gain('Praise Jenny\\'s cooking', 2)]":
        $ mrel += 2
        "Jenny is pleased you appreciate her efforts."
        
    "[wt_relationship_gain('Ask about sister\\'s day', 2)]":
        $ srel += 2
        "Your sister enjoys sharing her day with you."
        
    "[wt('Talk about work', 'good', '+1 all relationships')]":
        $ mrel += 1
        $ srel += 1
        "Everyone is interested in your work stories."
        
    "[wt('Stay quiet', 'neutral')]":
        "You eat quietly, enjoying the family atmosphere."

# Evening Activities
menu evening_choice:
    "[wt('Spend time with Jenny', 'relationship', '+3 Jenny relationship')]":
        $ mrel += 3
        jump jenny_evening_scene
        
    "[wt('Hang out with sister', 'relationship', '+3 sister relationship')]":
        $ srel += 3  
        jump sister_evening_scene
        
    "[wt('Family time together', 'good', '+1 all relationships')]":
        $ mrel += 1
        $ srel += 1
        jump family_evening_scene
        
    "[wt('Go to room alone', 'neutral')]":
        jump alone_evening_scene

# Night Time Decisions
menu night_activities:
    "[wt('Visit Jenny at night', 'special', 'night content', 'mrel >= 200 and Hour >= 20')]" if mrel >= 200 and Hour >= 20:
        jump jenny_night_scene
        
    "[wt('Check on sister', 'relationship', '+1 relationship')]":
        $ srel += 1
        "You check to make sure she's doing well."
        
    "[wt('Go to sleep', 'neutral')]":
        "You head to bed for the night."
"""

# ===============================================================================
# SPECIAL SCENES (x-msundaysex.rpy, x-jenpractice.rpy)
# ===============================================================================

"""
# Weekend Special Events
menu weekend_special:
    "[wt_special_scene('Romantic weekend with Jenny', 'mrel >= 300', 'romantic content')]" if mrel >= 300:
        jump jenny_weekend_romance
        
    "[wt('Photography session', 'good', 'photo content', 'instadone >= 2')]" if instadone >= 2:
        jump weekend_photo_session
        
    "[wt('Beach day', 'good', 'beach content', 'mbikini >= 1')]" if mbikini >= 1:
        jump weekend_beach_day
        
    "[wt('Relaxing at home', 'neutral', 'family bonding')]":
        $ mrel += 1
        $ srel += 1
        "You enjoy a peaceful weekend at home."

# Massage Scene Choices
menu massage_scene:
    "[wt_relationship_gain('Offer massage', 5)]":
        $ mrel += 5
        $ mcorr += 2
        "Jenny really appreciates the relaxing massage."
        
    "[wt('Professional massage', 'good', '+3 relationship')]":
        $ mrel += 3
        "You give a proper, therapeutic massage."
        
    "[wt('Maybe another time', 'neutral')]":
        "You suggest perhaps doing it another time."

# Advanced Content Choices
menu advanced_content:
    "[wt_special_scene('Intimate moment', 'mrel >= 400', 'adult content')]" if mrel >= 400:
        jump intimate_scene
        
    "[wt('Romantic gesture', 'relationship', '+5 relationship', 'mrel >= 200')]" if mrel >= 200:
        $ mrel += 5
        jump romantic_gesture
        
    "[wt('Keep it casual', 'good')]":
        "You keep things light and casual."
"""

# ===============================================================================
# MONEY MANAGEMENT CHOICES
# ===============================================================================

"""
# Shopping Priority Decisions
menu shopping_priority:
    "[wt('Buy essentials first', 'best', 'smart money management')]":
        "You prioritize necessary purchases."
        
    "[wt('Buy gifts for family', 'relationship', '+2 all relationships', 'mny >= 200')]" if mny >= 200:
        $ mny -= 200
        $ mrel += 2
        $ srel += 2
        "Everyone loves their thoughtful gifts!"
        
    "[wt('Save for big purchase', 'good', 'future opportunities')]":
        "You save money for important future purchases."
        
    "[wt('Spend freely', 'bad', 'poor money management')]":
        "You spend without much planning."

# Investment Choices
menu investment_decisions:
    "[wt('Invest in photography equipment', 'money_neg', '-$500, better photo quality', 'mny >= 500')]" if mny >= 500:
        $ mny -= 500
        $ photo_equipment = 1
        "Professional equipment will improve photo sessions!"
        
    "[wt('Invest in security system', 'money_neg', '-$300, surveillance options', 'mny >= 300')]" if mny >= 300:
        $ mny -= 300
        $ security_system = 1
        "Enhanced security system installed."
        
    "[wt('Keep money liquid', 'good', 'maintain flexibility')]":
        "You keep your money available for opportunities."
"""

# ===============================================================================
# TIME MANAGEMENT CHOICES
# ===============================================================================

"""
# Daily Schedule Decisions
menu daily_schedule:
    "[wt('Early morning with Jenny', 'relationship', '+2 relationship, costs time')]":
        $ mrel += 2
        $ Hour += 2
        "Quality time with Jenny in the morning."
        
    "[wt('Work full day', 'money_pos', '+$100, full day')]":
        $ mny += 100
        $ Hour += 8
        "You focus on work and earn good money."
        
    "[wt('Balance work and family', 'good', 'moderate income, relationships')]":
        $ mny += 60
        $ mrel += 1
        $ srel += 1
        $ Hour += 6
        "Good balance between work and family."
        
    "[wt('Family focus day', 'relationship', '+3 all relationships')]":
        $ mrel += 3
        $ srel += 3
        $ Hour += 8
        "Full day spent with family."
"""

# ===============================================================================
# ACHIEVEMENT UNLOCKS
# ===============================================================================

"""
# Achievement-related Choices
menu achievement_choices:
    "[wt('Perfect relationship balance', 'special', 'unlock achievement', 'mrel >= 300 and srel >= 300')]" if mrel >= 300 and srel >= 300:
        $ achievement_perfect_balance = True
        "You've achieved perfect relationship balance!"
        
    "[wt('Business mogul path', 'money_pos', 'unlock business achievement', 'mny >= 10000')]" if mny >= 10000:
        $ achievement_business_mogul = True
        "You've become a successful business mogul!"
        
    "[wt('Photography master', 'special', 'unlock photo achievement', 'hotphotos_done >= 1')]" if hotphotos_done >= 1:
        $ achievement_photo_master = True
        "You've mastered the art of photography!"
"""

# ===============================================================================
# USAGE INSTRUCTIONS
# ===============================================================================

"""
HOW TO USE THIS GUIDE:

1. Copy the walkthrough_choice_helper.rpy file to your game/ folder
2. Find the corresponding scenes in your game files
3. Replace the original menu choices with the wt() versions shown above
4. Test to make sure colors and effects work properly

EXAMPLE MODIFICATION:
Original game code:
    menu:
        "Be nice":
            $ mrel += 2
        "Be mean":
            $ mrel -= 1

Modified with walkthrough:
    menu:
        "[wt_relationship_gain('Be nice', 2)]":
            $ mrel += 2
        "[wt_bad_choice('Be mean', '-1 relationship')]":
            $ mrel -= 1

The walkthrough system will automatically color the choices:
- "Be nice" will appear in pink with ♥ icon (relationship gain)
- "Be mean" will appear in red with ✗ icon (bad choice)
"""