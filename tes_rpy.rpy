# Define characters with color codes and tags
define e = Character("Elena", color="#c8ffc8", image="elena")
define m = Character("Marcus", color="#c8c8ff", image="marcus")
define n = Character("Narrator", color="#ffffff")

# Variables that can affect dialogue
default player_name = "Alex"
default friendship_elena = 50
default friendship_marcus = 30
default has_sword = False
default knows_secret = False
default day = 1

# Image definitions (for sprites)
image elena happy = "elena_happy.png"
image elena angry = "elena_angry.png"
image marcus neutral = "marcus_neutral.png"
image marcus surprised = "marcus_surprised.png"

# The game starts here
label start:
    
    n "Day [day]: Your {b}adventure{/b} begins in the small town of Riverwood.{i}"
    
    scene bg town_day
    
    show elena happy at left
    show marcus neutral at right
    
    e "Oh! You must be the new traveler everyone's talking about!"
    
    menu:
        "Yes, I'm {w}[player_name]. Nice to meet you.":
            $ friendship_elena += 5
            e "Pleasure to meet you, [player_name]! I'm Elena."
            
        "Who's asking?":
            $ friendship_elena -= 10
            show elena angry
            e "Well, that's not very friendly! I was just trying to welcome you."
    
    m "Don't mind Elena. She's always overly enthusiastic with newcomers."
    
    if friendship_elena > 45:
        show elena happy
        e "Marcus! Don't give [player_name] the wrong impression about me!"
    else:
        e "At least someone around here has manners..."
    
    menu:
        "You two seem close. How long have you known each other?":
            $ friendship_marcus += 5
            m "Since we were kids. Elena's family moved here when we were seven."
            
        "I don't care about your backstory. I need supplies.":
            $ friendship_elena -= 15
            $ friendship_marcus -= 10
            show elena angry
            show marcus surprised
            e "Wow, rude much?"
            m "The general store is down the street. Good luck with that attitude."
    
    # Conditional dialogue based on variables
    if friendship_elena >= 50 and friendship_marcus >= 35:
        e "You know, [player_name], you seem alright. Maybe we could show you around?"
        m "Yeah, we could introduce you to some important people in town."
        
        menu:
            "I'd appreciate that, thanks!":
                $ friendship_elena += 10
                $ friendship_marcus += 10
                e "Great! Let's start with the blacksmith."
                
            "I prefer to explore on my own.":
                $ friendship_marcus -= 5
                m "Suit yourself. Don't come crying if you get lost."
                
    elif friendship_elena < 30:
        e "Well, if you'll excuse us, we have things to do."
        hide elena with dissolve
        hide marcus with dissolve
        n "Elena and Marcus leave, clearly unimpressed with your attitude."
        
    else:
        m "Anyway, we should get going. See you around, [player_name]."
    
    # Another scene with different conditions
    scene bg forest with fade
    
    if has_sword:
        show elena happy at center
        e "I see you've got yourself a sword! That'll be useful against the bandits in these woods."
    else:
        show elena angry at center
        e "You came into the forest without a weapon? Are you trying to get yourself killed?"
        
        menu:
            "I fight better with my fists.":
                e "Well... good luck with that, I guess."
                
            "I was hoping you'd protect me.":
                if friendship_elena > 60:
                    e "Oh you! *giggles* Fine, I'll watch your back."
                    $ friendship_elena += 5
                else:
                    e "Ugh, you're hopeless."
                    $ friendship_elena -= 5
    
    # Secret reveal based on flags
    if knows_secret:
        show elena angry
        e "Wait... how do you know about the ancient artifact? That's supposed to be a secret!"
        
        menu:
            "Marcus told me.":
                $ friendship_marcus -= 20
                e "That idiot! I'm going to kill him!"
                
            "I overheard you talking about it.":
                e "You were eavesdropping? That's a serious breach of trust!"
                $ friendship_elena -= 30
                
            "I have my ways.":
                e "Well... just don't go spreading it around, okay?"
                $ friendship_elena += 5
    
    # End of this segment
    n "As the sun sets, you return to town, your relationships changed by today's events."
    $ day += 1
    
    return