# Colorful Test Script
define p = Character("[player_name]", color="#FF0000")

label start:
    p "{color=#FF0000}Red Alert!{/color} {w}This is serious."
    p "{color=#00FF00}Green means go!{/color} {w=0.5}Let's proceed."
    p "{color=#0000FF}Blue thoughts...{/color} {i}so deep{/i}"

    menu:
        "{color=#FF00FF}Magenta Choice{/color}":
            $ score += 10
            p "{color=#FFA500}Orange{/color} you glad? +{size=+2}10{/size} points!"
            
        "{color=#FFFF00}Yellow Caution{/color}":
            $ score -= 5
            p "{color=#800080}Purple{/color} prose... -5 points."

    if score > 15:
        p "{color=#FF0000}R{/color}{color=#00FF00}G{/color}{color=#0000FF}B{/color} Rainbow success!"
    else:
        p "{color=#A9A9A9}Gray{/color} day... Try again."

    p "Stats:"
    p "{color=#FF6347}Tomato{/color}: [tomato_count] | {color=#40E0D0}Turquoise{/color}: [turquoise_count]"
    p "{b}{color=#FFD700}Golden{/color} ending{/b} {size=-2}([ending_type]){/size}"