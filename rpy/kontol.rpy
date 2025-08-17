# Colorful Test Script
define p = Character("[player_name]", color="#FF0000")

label start:
    p "{color=#FF0000} Red Alert! {/color} {w} Ini serius."
    p "{color=#00FF00} Green berarti pergi! {/color} {w=0.5} Mari kita lanjutkan."
    p "{color=#0000FF} Pikiran biru ... {/color} {i} sangat dalam {/i}"

    menu:
        "{color=#FF00FF} Magenta Choice {/color}":
            $ score += 10
            p "{color=#FFA500} Orange {/color} Anda senang? +{size=+2} 10 {/size} poin!"
            
        "{color=#FFFF00} Yellow hati -hati {/color}":
            $ score -= 5
            p "{color=#800080} Purple {/color} prosa ... -5 poin."

    if score > 15:
        p "{color=#FF0000} r {/color} {color=#00FF00} g {/color} {color=#0000FF} b {/color} Rainbow Success!"
    else:
        p "{color=#A9A9A9} Gray {/color} hari ... coba lagi."

    p "Statistik:"
    p "{color=#FF6347} tomat {/color}: [tomato_count] | {color=#40E0D0} Turquoise {/color}: [turquoise_count]"
    p "{b} {color=#FFD700} golden {/color} ending {/b} {size=-2} ([ending_type]) {/size}"