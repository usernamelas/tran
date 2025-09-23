label EP16_Begin:
    $ EP16_var_1 = True
    stop music
    show text "{size=+20}Press Space{/size}"
    if timothySexContent == True:
        jump EP16_Timothy_1
    else:
        jump EP16_Home
    pause
label EP16_Timothy_1:
    play music SexyTimeSong5
    $ EP16_var_2 = True
    scene 45-8 timothy 131 with Dissolve(0.5)
    fe1 "What are you doing, guys?"
    fe1 "They might overhear us."
    a "Don't worry about it. Keep your voice down."
    scene 45-8 timothy 132 with Dissolve(0.5)
    a "We'll be ok in here."
    t "What now?"
    a "Heh. I have some ideas."
    play sound undress
    scene 45-8 timothy 133 with Dissolve(0.5)
    fe1 "What do you mean by that?"
    a "Heh. You'll see."
    scene 45-8 timothy 134 with Dissolve(0.5)
    ash "Come on, dude. You're at a party, let off some steam."
    ash "Don't be so stuck up."
    ash "Let's just chat up some girls, dance some, drink some, you know?"
    scene 45-8 timothy 135 with Dissolve(0.5)
    a1 "I suppose you're right. It's been a while since I've really done anything fun."
    ash "Exactly. You've been out for some time, Now you have to catch up."
    ash "You think Anna was just sitting on her butt this whole time?"
    a1 "I don't know. But you're right... "
    a1 "Let's get some drinks, and talk to some girls. Talking ain't a problem."
    ash "That's my man."
    scene 45-8 timothy 136 with Dissolve(0.5)
    a "{i}...Huh...{/i}"
    scene 45-8 timothy 137 with Dissolve(0.5)
    t "You think they heard us?"
    a "No. It's all good."
    scene 45-8 timothy 138 with Dissolve(0.5)
    ash "I saw some hot chicks dancing."
    ash "Let's go talk to them."
    a1 "Right."
    scene 45-8 timothy 139 with Dissolve(0.5)
    fe1 "They left, I think we should go."
    a "You sure?"
    a "I thought you wanted to get to know Timothy a bit better."
    fe1 "Well..."
    a "Heh..."
    menu:
        "I could help you with getting to know him.":
            label EP16_Timothy_Sex_Scene:
            $ persistent.scene_47 = True
            scene 45-8 timothy 140 with Dissolve(0.5)
            t "Whaa."
            a "I can tell you one thing, he's pretty impressive."
            scene 45-8 timothy 141 with Dissolve(0.5)
            t "Heh..."
            a "If you know what I mean, Felicia?"
            fe1 "I... I... Heh."
            scene 45-8 timothy 142 with Dissolve(0.5)
            a "Come, come. Don't be shy."
            a "He won't bite. Neither will I."
            scene 45-8 timothy 143 with Dissolve(0.5)
            fe1 "Heh. Ok."
            fe1 "I mean, I could try to... Know you better, Timothy."
            scene 45-8 timothy 144 with Dissolve(0.5)
            t "Whaa..."
            t "{i}...This is crazy...{/i}"
            scene 45-8 timothy 145 with Dissolve(0.5)
            t "Heh... Two hot girls with me in..."
            t "Can a man ask for more?"
            a "Hehe..."
            scene 45-8 timothy 146 with Dissolve(0.5)
            a "So... What are you waiting for?"
            a "Let's see what kind of a monster this gladiator is hiding there, eh?"
            scene 45-8 timothy 147 with Dissolve(0.5)
            fe1 "I have to admit. I'm curious, Timothy."
            fe1 "How about you show it to me?"
            scene 45-8 timothy 148 with Dissolve(0.5)
            fe1 "Wow..."
            a "Well, well... Heh."
            scene 45-8 timothy 149 with Dissolve(0.5)
            a "I bet you like what you see, eh?"
            a "{i}...Hehe... Leading them like this is fun...{/i}"
            fe1 "Yeah..."
            t "Oh... Felicia..."
            play sound jerk
            scene 45-8 timothy 150 with Dissolve(0.5)
            fe1 "It's so big in my hand..."
            t "Aah..."
            a "Yeah... Hehe... Timothy is definitely packing."
            $ different_choice_menu = True
            $ EP16_Anim_Option = 1
            $ EP16_Anim_Speed = 1
            scene black
            show Ep16_Timothy_Anim_1 with Dissolve(0.5)
            label EP16_Timothy_Jerking_Label:
                t "Fuck..."
                t "You are good..."
                menu EP16_Timothy_Jerking_Menu:
                    "View 1":
                        hide Ep16_Timothy_Anim_1
                        hide Ep16_Timothy_Anim_1_Faster
                        $ EP16_Anim_Option = 1
                        show Ep16_Timothy_Anim_1 with Dissolve(0.5)
                        jump EP16_Timothy_Jerking_Menu
                    "Slower":
                        hide Ep16_Timothy_Anim_1
                        hide Ep16_Timothy_Anim_1_Faster
                        $ EP16_Anim_Speed = 1
                        show Ep16_Timothy_Anim_1 with Dissolve(0.5)
                        jump EP16_Timothy_Jerking_Menu
                    "Faster":
                        hide Ep16_Timothy_Anim_1
                        hide Ep16_Timothy_Anim_1_Faster
                        $ EP16_Anim_Speed = 2
                        show Ep16_Timothy_Anim_1_Faster with Dissolve(0.5)
                        jump EP16_Timothy_Jerking_Menu
                    "Continue":
                        hide Ep16_Timothy_Anim_1
                        hide Ep16_Timothy_Anim_1_Faster
                        $ different_choice_menu = False
                        pass
            scene 45-8 timothy 151 with Dissolve(0.5)
            t "Your hands are magical, Felicia."
            fe1 "Your cock... It's huge... Whoa..."
            scene 45-8 timothy 152 with Dissolve(0.5)
            a "We've just begun, Timothy."
            t "That's... Good news. heh..."
            scene 45-8 timothy 153 with Dissolve(0.5)
            a "How about you lower yourself to your knees?"
            fe1 "Wha?"
            fe1 "Right now?"
            a "Yes, hehe..."
            scene 45-8 timothy 154 with Dissolve(0.5)
            t "You don't have to..."
            a "Yes, she does hehe..."
            a "And she wants to."
            play sound cloth_sound1
            scene 45-8 timothy 155 with Dissolve(0.5)
            fe1 "Wooow... Timothy."
            fe1 "It's looks massive."
            fe1 "I didn't expect this."
            a "No one ever does."
            scene 45-8 timothy 156 with Dissolve(0.5)
            fe1 "Well... What would you like me to do?"
            t "I... I don't know... Whatever you'd like to do."
            fe1 "Heh. Good."
            scene 45-8 timothy 157 with Dissolve(0.5)
            fe1 "Oh... Timothy."
            t "Ahh..."
            t "Fucking awesome."
            scene 45-8 timothy 158 with Dissolve(0.5)
            a "Yess... Stroke his cock..."
            a "{i}...This shit's turning me on...{/i}"
            a "I bet you like stroking him, don't you Felicia?"
            fe1 "Yeah..."
            scene 45-8 timothy 159 with Dissolve(0.5)
            a "Come on... Get closer..."
            a "Yeah..."
            a "That's what Timothy likes. Hehe..."
            fe1 "Mmm..."
            fe1 "I'm drawn to it..."
            play sound jerk2
            scene 45-8 timothy 160 with Dissolve(0.5)
            fe1 "Mmmhhhh..."
            t "Ohh... Shit..."
            a "You like that?"
            t "Fuck yes!"
            $ different_choice_menu = True
            $ EP16_Anim_Option = 1
            $ EP16_Anim_Speed = 1
            scene black
            show Ep16_Timothy_Anim_2 with Dissolve(0.5)
            label EP16_Timothy_Blowjob_1_Label:
                play sound jerk3 loop
                t "That mouth..."
                t "Just continue like that."
                menu EP16_Timothy_Blowjob_1_Menu:
                    "View 1":
                        hide Ep16_Timothy_Anim_2
                        hide Ep16_Timothy_Anim_2_Faster
                        hide Ep16_Timothy_Anim_3
                        hide Ep16_Timothy_Anim_3_Faster
                        $ EP16_Anim_Option = 1
                        if EP16_Anim_Speed == 1:
                            show Ep16_Timothy_Anim_2 with Dissolve(0.5)
                        if EP16_Anim_Speed == 2:
                            show Ep16_Timothy_Anim_2_Faster with Dissolve(0.5)
                        jump EP16_Timothy_Blowjob_1_Menu
                    "View 2":
                        hide Ep16_Timothy_Anim_2
                        hide Ep16_Timothy_Anim_2_Faster
                        hide Ep16_Timothy_Anim_3
                        hide Ep16_Timothy_Anim_3_Faster
                        $ EP16_Anim_Option = 2
                        if EP16_Anim_Speed == 1:
                            show Ep16_Timothy_Anim_3 with Dissolve(0.5)
                        if EP16_Anim_Speed == 2:
                            show Ep16_Timothy_Anim_3_Faster with Dissolve(0.5)
                        jump EP16_Timothy_Blowjob_1_Menu
                    "Slower":
                        hide Ep16_Timothy_Anim_2
                        hide Ep16_Timothy_Anim_2_Faster
                        hide Ep16_Timothy_Anim_3
                        hide Ep16_Timothy_Anim_3_Faster
                        $ EP16_Anim_Speed = 1
                        if EP16_Anim_Option == 1:
                            show Ep16_Timothy_Anim_2 with Dissolve(0.5)
                        if EP16_Anim_Option == 2:
                            show Ep16_Timothy_Anim_3 with Dissolve(0.5)
                        jump EP16_Timothy_Blowjob_1_Menu
                    "Faster":
                        hide Ep16_Timothy_Anim_2
                        hide Ep16_Timothy_Anim_2_Faster
                        hide Ep16_Timothy_Anim_3
                        hide Ep16_Timothy_Anim_3_Faster
                        $ EP16_Anim_Speed = 2
                        if EP16_Anim_Option == 1:
                            show Ep16_Timothy_Anim_2_Faster with Dissolve(0.5)
                        if EP16_Anim_Option == 2:
                            show Ep16_Timothy_Anim_3_Faster with Dissolve(0.5)
                        jump EP16_Timothy_Blowjob_1_Menu
                    "Continue":
                        hide Ep16_Timothy_Anim_2
                        hide Ep16_Timothy_Anim_2_Faster
                        hide Ep16_Timothy_Anim_3
                        hide Ep16_Timothy_Anim_3_Faster
                        $ different_choice_menu = False
                        stop sound
                        pass
            $ different_choice_menu = True
            $ EP16_Anim_Option = 1
            $ EP16_Anim_Speed = 1
            scene black
            show Ep16_Timothy_Anim_4 with Dissolve(0.5)
            label EP16_Timothy_Blowjob_2_Label:
                play sound jerk3 loop
                t "AAHHH..."
                t "She ain't stopping... Fuck..."
                menu EP16_Timothy_Blowjob_2_Menu:
                    "View 1":
                        hide Ep16_Timothy_Anim_4
                        hide Ep16_Timothy_Anim_4_Faster
                        $ EP16_Anim_Option = 1
                        show Ep16_Timothy_Anim_4 with Dissolve(0.5)
                        jump EP16_Timothy_Blowjob_2_Menu
                    "Slower":
                        hide Ep16_Timothy_Anim_4
                        hide Ep16_Timothy_Anim_4_Faster
                        $ EP16_Anim_Speed = 1
                        show Ep16_Timothy_Anim_4 with Dissolve(0.5)
                        jump EP16_Timothy_Blowjob_2_Menu
                    "Faster":
                        hide Ep16_Timothy_Anim_4
                        hide Ep16_Timothy_Anim_4_Faster
                        $ EP16_Anim_Speed = 2
                        show Ep16_Timothy_Anim_4_Faster with Dissolve(0.5)
                        jump EP16_Timothy_Blowjob_2_Menu
                    "Continue":
                        hide Ep16_Timothy_Anim_4
                        hide Ep16_Timothy_Anim_4_Faster
                        $ different_choice_menu = False
                        stop sound
                        pass
            scene 45-8 timothy 161 with Dissolve(0.5)
            fe1 "Aahh..."
            t "Shiiit..."
            scene 45-8 timothy 162 with Dissolve(0.5)
            a "Hehe... I bet you're loving this..."
            t "Never would've dreamed of this..."
            t "Not even in my wildest dreams..."
            scene 45-8 timothy 163 with Dissolve(0.5)
            a "Come here..."
            play sound kisspeck
            scene 45-8 timothy 164 with Dissolve(0.5)
            a "Mm..."
            t "Mmmhmmm...."
            "The heat was turning up in the toilet booth..."
            "Timothy was being handled on both fronts..."
            scene 45-8 timothy 165 with Dissolve(0.5)
            "Two women just pleasuring him."
            "Giving him the pleasure he deserved."
            scene 45-8 timothy 166 with Dissolve(0.5)
            a "Hey... Felicia..."
            fe1 "mm?"
            "She wouldn't let go of Timothy's cock."
            scene 45-8 timothy 168 with Dissolve(0.5)
            "Then finally..."
            fe1 "Yeah?"
            a "How about we switch it up a bit?"
            a "I'm getting kind of horny."
            a "Perhaps you could help me with something?"
            scene 45-8 timothy 169 with Dissolve(0.5)
            a "Remove my panties for me, would you?"
            fe1 "Oh? Hehe... Ok."
            play sound undress
            scene 45-8 timothy 170 with Dissolve(0.5)
            pause 0.5
            scene 45-8 timothy 171 with Dissolve(0.5)
            fe1 "Like that?"
            a "Oh Yeah..."
            a "I got pretty wet by looking at you two."
            scene 45-8 timothy 172 with Dissolve(0.5)
            a "So, Timothy."
            a "You want some more?"
            t "Oh... Heh... YEAH!"
            a "Hehe... What are you waiting for, then?"
            a "Felicia. Help him stick it in, please."
            scene 45-8 timothy 173 with Dissolve(0.5)
            fe1 "Ok..."
            fe1 "I can feel your cock pulsating... Oh..."
            scene 45-8 timothy 174 with Dissolve(0.5)
            "They were slowly closing the gap..."
            "The anticipation was building and building..."
            "Anna could feel his cock closing up to her pussy hole..."
            play sound jerk2
            scene 45-8 timothy 175 with Dissolve(0.5)
            a "Ah... Oh... Yeah... That's good..."
            t "Oohh... Fuck..."
            scene 45-8 timothy 176 with Dissolve(0.5)
            a "Come on... Stick it in further."
            t "Ohh..."
            play sound female_moan_3
            scene 45-8 timothy 177 with Dissolve(0.5)
            a "AAHH!!!"
            t "Ahhh!... So good..."
            play sound jerk
            scene 45-8 timothy 178 with Dissolve(0.5)
            "Timothy was pushing his pulsating penis further into Anna."
            "Enjoying every inch."
            "So was Anna..."
            $ different_choice_menu = True
            $ EP16_Anim_Option = 1
            $ EP16_Anim_Speed = 1
            scene black
            show Ep16_Timothy_Anim_8 with Dissolve(0.5)
            label EP16_Timothy_Sex_1_Label:
                play sound jerk loop
                a "That cock!!!"
                t "YEAH!! Your pussy's so good..."
                t "Fuuckk... Anna..."
                fe1 "You fucking her is so hot..."
                menu EP16_Timothy_Sex_1_Menu:
                    "View 1":
                        hide Ep16_Timothy_Anim_8
                        hide Ep16_Timothy_Anim_8_Faster
                        $ EP16_Anim_Option = 1
                        show Ep16_Timothy_Anim_8 with Dissolve(0.5)
                        jump EP16_Timothy_Sex_1_Menu
                    "Slower":
                        hide Ep16_Timothy_Anim_8
                        hide Ep16_Timothy_Anim_8_Faster
                        $ EP16_Anim_Speed = 1
                        show Ep16_Timothy_Anim_8 with Dissolve(0.5)
                        jump EP16_Timothy_Sex_1_Menu
                    "Faster":
                        hide Ep16_Timothy_Anim_8
                        hide Ep16_Timothy_Anim_8_Faster
                        $ EP16_Anim_Speed = 2
                        show Ep16_Timothy_Anim_8_Faster with Dissolve(0.5)
                        jump EP16_Timothy_Sex_1_Menu
                    "Continue":
                        hide Ep16_Timothy_Anim_8
                        hide Ep16_Timothy_Anim_8_Faster
                        $ different_choice_menu = False
                        stop sound
                        pass
            scene 45-8 timothy 179 with Dissolve(0.5)
            "Felicia was very involved... She got turned on more and more while looking at them both."
            fe1 "Oh... How I want that cock in me..."
            scene 45-8 timothy 180 with Dissolve(0.5)
            a "Heh... Well, we can arrange that."
            a "Come on."
            scene 45-8 timothy 181 with Dissolve(0.5)
            a "Let me help you with your outfit a bit."
            fe1 "Ok..."
            play sound jacketcloth
            scene 45-8 timothy 182 with Dissolve(0.5)
            a "There..."
            fe1 "Oh... Heh..."
            "Felicia was a bit shy... She had never done stuff like this before..."
            "But she enjoyed it... A lot."
            scene 45-8 timothy 183 with Dissolve(0.5)
            a "Come on, Timothy. Don't leave a woman waiting."
            t "Oh... Ok..."
            "He was barely keeping up. Fucking one girl, then another..."
            "A most enjoyable activity, for sure."
            play sound female_moan_1
            scene 45-8 timothy 184 with Dissolve(0.5)
            fe1 "OHh... Ahhh!!!"
            fe1 "Timothy..."
            fe1 "That cock..."
            t "Felicia... mhmmmm..."
            "Both of them were so excited to feel each other..."
            "The feelings were deep and so was the penetration."
            scene 45-8 timothy 185 with Dissolve(0.5)
            t "I can't believe I'm actually inside of you."
            fe1 "Your cock... Fuck..."
            t "You like that?"
            fe1 "OHH YES!"
            scene 45-8 timothy 186 with Dissolve(0.5)
            a "Mmm..."
            a "So hot, you two."
            a "Keep going..."
            a "Ahh..."
            $ different_choice_menu = True
            $ EP16_Anim_Option = 1
            $ EP16_Anim_Speed = 1
            scene black
            show Ep16_Timothy_Anim_7 with Dissolve(0.5)
            label EP16_Timothy_Sex_3_Label:
                play sound jerk loop
                fe1 "Oh... First time I've ever felt anything like this..."
                fe1 "Fuck!"
                t "Yeah? You like it?"
                fe1 "I LOVE IT!"
                menu EP16_Timothy_Sex_3_Menu:
                    "View 1":
                        hide Ep16_Timothy_Anim_7
                        hide Ep16_Timothy_Anim_7_Faster
                        $ EP16_Anim_Option = 1
                        show Ep16_Timothy_Anim_7 with Dissolve(0.5)
                        jump EP16_Timothy_Sex_3_Menu
                    "Slower":
                        hide Ep16_Timothy_Anim_7
                        hide Ep16_Timothy_Anim_7_Faster
                        $ EP16_Anim_Speed = 1
                        show Ep16_Timothy_Anim_7 with Dissolve(0.5)
                        jump EP16_Timothy_Sex_3_Menu
                    "Faster":
                        hide Ep16_Timothy_Anim_7
                        hide Ep16_Timothy_Anim_7_Faster
                        $ EP16_Anim_Speed = 2
                        show Ep16_Timothy_Anim_7_Faster with Dissolve(0.5)
                        jump EP16_Timothy_Sex_3_Menu
                    "Continue":
                        hide Ep16_Timothy_Anim_7
                        hide Ep16_Timothy_Anim_7_Faster
                        $ different_choice_menu = False
                        stop sound
                        pass
            scene 45-8 timothy 187 with Dissolve(0.5)
            a "Mmmmm...."
            "They were all as horny as ever... Just fucking... Having fun..."
            play sound female_moan_4
            scene 45-8 timothy 188 with Dissolve(0.5)
            fe1 "Ohh... Timothy!!!"
            "Felicia was closing in on an orgasm..."
            fe1 "I can't believe it... Ahhh..."
            "She had never felt an orgasm from sex before..."
            "This time it was bursting out of her..."
            play sound moaningfour
            scene 45-8 timothy 189 with Dissolve(0.5)
            fe1 "Aahh... I'm... Cumming..."
            t "Fuuck..."
            with flash
            with flash
            fe1 "Yeah..."
            with flash
            fe1 "YEAH.. YEAH!!!!"
            fe1 "AAHHHH..."
            scene 45-8 timothy 190 with Dissolve(0.5)
            fe1 "That... That was... Fuck..."
            fe1 "Your cock is something else, Timothy."
            scene 45-8 timothy 191 with Dissolve(0.5)
            a "I see you're still on, Timothy."
            a "How about you satisfy one more woman, eh?"
            t "Whoa... Fuck yeah!"
            t "This is crazy!"
            scene 45-8 timothy 192 with Dissolve(0.5)
            a "Come on."
            t "Ok, Anna..."
            a "Oh... I can't wait..."
            scene 45-8 timothy 193 with Dissolve(0.5)
            a "Aah..."
            a "Oh, Timothy..."
            a "Just like that..."
            play sound jerk2
            scene 45-8 timothy 194 with Dissolve(0.5)
            t "Fuck... That pussy is as good as ever..."
            a "Hehe... Ahh..."
            a "So good..."
            play audio female_moan_5
            $ different_choice_menu = True
            $ EP16_Anim_Option = 1
            $ EP16_Anim_Speed = 1
            scene black
            show Ep16_Timothy_Anim_5 with Dissolve(0.5)
            label EP16_Timothy_Sex_2_Label:
                play sound jerk loop
                a "Give it all to me..."
                a "Give me your cock..."
                a "Aah... It... Feels... So... Good!!!"
                menu EP16_Timothy_Sex_2_Menu:
                    "View 1":
                        hide Ep16_Timothy_Anim_5
                        hide Ep16_Timothy_Anim_5_Faster
                        $ EP16_Anim_Option = 1
                        show Ep16_Timothy_Anim_5 with Dissolve(0.5)
                        jump EP16_Timothy_Sex_2_Menu
                    "Slower":
                        hide Ep16_Timothy_Anim_5
                        hide Ep16_Timothy_Anim_5_Faster
                        $ EP16_Anim_Speed = 1
                        show Ep16_Timothy_Anim_5 with Dissolve(0.5)
                        jump EP16_Timothy_Sex_2_Menu
                    "Faster":
                        hide Ep16_Timothy_Anim_5
                        hide Ep16_Timothy_Anim_5_Faster
                        $ EP16_Anim_Speed = 2
                        show Ep16_Timothy_Anim_5_Faster with Dissolve(0.5)
                        jump EP16_Timothy_Sex_2_Menu
                    "Continue":
                        hide Ep16_Timothy_Anim_5
                        hide Ep16_Timothy_Anim_5_Faster
                        $ different_choice_menu = False
                        stop sound
                        pass
            scene 45-8 timothy 195 with Dissolve(0.5)
            a "{i}...Timothy enjoying two woman like that...{/i}"
            a "{i}...I bet this is the time of his life...{/i}"
            a "Ah... Shit..."
            scene 45-8 timothy 196 with Dissolve(0.5)
            a "I'm... Getting close... What about you?"
            t "Yeah... Me too..."
            t "Fuck..."
            play sound moaninglong_1
            show Ep16_Timothy_Anim_6 with Dissolve(0.5)
            pause
            a "AAahhaaahhaaaAAa!!!!"
            "Anna was completely lost in the pleasure."
            t "I CAN'T HOLD..."
            menu:
                "Cum inside of Anna.":

                    a "Ahhh..."
                    with flash
                    scene 45-8 timothy 197 with flash
                    with flash
                    t "Fuuuckk... Anna!"
                    t "My cock is throbbing inside of you!!!"
                    with flash
                    play audio cum_sound
                    a "Yeah!"
                    a "Yeah! Fill me!"
                    with flash
                    with flash
                    scene 45-8 timothy 198 with flash
                    a "AAAAHHH"
                    t "AAAAHHHH!!!"
                    scene 45-8 timothy 201 with Dissolve(0.5)
                    t "Damn..."
                    a "Oh, yeah... I can feel that goop inside of me..."
                    a "I bet you liked filling me up?"
                    t "I... Damn... I did..."
                    scene 45-8 timothy 202 with Dissolve(0.5)
                    t "I need to catch my breath. Damn..."
                    t "Crazy good."
                "Cum on Anna's belly.":
                    a "Ahhh..."
                    with flash
                    scene 45-8 timothy 199 with flash_vpunch
                    play audio cum_sound
                    with flash
                    t "Fuuuckk... Anna!"
                    t "My cock is throbbing inside of you!!!"
                    with flash
                    a "Yeah!"
                    scene 45-8 timothy 199 with flash_vpunch
                    t "AAAHHHHH!"
                    with flash
                    a "Yeah!"
                    scene 45-8 timothy 200 with Dissolve(0.5)
                    a "Heh... I'm covered in your cum now..."
                    t "Crazy... Hah."
                    t "I need to catch my breath..."
            scene 45-8 timothy 203 with Dissolve(0.5)
            fe1 "That was quite some performance, Timothy."
            fe1 "You just satisfied two women..."
            fe1 "Impressive ratio."
            scene 45-8 timothy 204 with Dissolve(0.5)
            t "Heh. Well..."
            t "I aim to please."
            fe1 "Heh... You do good."
            t "Still can't believe. Me with two girls? Whaat?"
            scene 45-8 timothy 205 with Dissolve(0.5)
            t "Thanks... Um... For this..."
            a "No need to thank me."
            a "You did me and Felicia really good..."
            t "Heh... Anytime, heh."
            fe1 "Haha."
            $ renpy.end_replay()
            scene black with Dissolve(0.5)
            pause 1
            play sound cloth_sound1
            scene 45-8 timothy 207 with Dissolve(0.5)
            a "Let's clean up and get out of here."
            fe1 "Good idea."
            scene 45-8 timothy 208 with Dissolve(0.5)
            t "Let's get out of here."
            a "Yeah."
            stop music
            play ambient club_ambience_1
            scene 45-8 timothy 209 with Dissolve(0.5)
            a "So. Let's get our dance on."
            a "What do you say?"
            fe1 "YEAH!"
            t "Sure!"
            scene 45-8 timothy 210 with Dissolve(0.5)
            "As they dance, Anna notices Andrew dancing and talking to another girl."
            "She gets slightly jealous..."
            if AnnaCorruption >=20:
                "But that's hypocritical, she sleeps around with a lot of men herself..."
            scene 45-8 timothy 211 with Dissolve(0.5)
            a "{i}...Well, well...{/i}"
            a "{i}...What is Andrew up to... Never thought him to be like this...{/i}"
            scene 45-8 timothy 212 with Dissolve(0.5)
            a "So... How are you guys doing?"
            fe1 "I'm good!"
            fe1 "Awesome, in fact!"
            scene 45-8 timothy 213 with Dissolve(0.5)
            t "Well, I'm actually kind of tired."
            t "I think I'm going to head out. Heh."
            scene 45-8 timothy 214 with Dissolve(0.5)
            fe1 "Ok..."
            fe1 "It was awesome to see you again, Timothy."
            fe1 "I hope we can see each other again some time."
            t "Definitely!"
            t "Alright, see you around, Felicia."
            scene 45-8 timothy 215 with Dissolve(0.5)
            ash "Heh... Nice outfit, Anna."
            a "What?"
            ash "I knew it was you the moment I saw your curves."
            a "Thanks I guess!"
            a "Anyway, see you around."
            scene 45-8 timothy 216 with Dissolve(0.5)
            t "Take care."
            scene 45-8 timothy 217 with Dissolve(0.5)
            t "Who was that?"
            a "Oh, just some guy I know."
            t "I see."
            scene black with Dissolve(0.5)
            pause 1
            "Some time later."
            stop ambient
            play music tranquility
            scene 45-8 timothy 218 with Dissolve(0.5)
            a "So. How did you enjoy the party?"
            t "The best party I've ever been to."
            a "I'm glad you liked it, heh."
            t "I LOVED it!"
            scene 45-8 timothy 219 with Dissolve(0.5)
            t "I'm really thankful..."
            t "And to actually have hooked up with Felicia... It's crazy."
            a "I'm glad I could've helped."
            scene 45-8 timothy 220 with Dissolve(0.5)
            a "Anyway, I'll head out, got some stuff to take care of."
            t "See you at work, Anna."
            a "Later, Timothy."
            scene black with Dissolve(0.5)
            pause 1
        "I'll leave you guys to it then.":
            scene black with Dissolve(0.5)
            pause
            "Anna exits the bathrooms and waits some time..."
            stop music
            play ambient club_ambience_1
            scene 45-8 timothy 209 with Dissolve(0.5)
            a "So. Let's get our dance on."
            a "What do you say?"
            fe1 "YEAH!"
            t "Sure!"
            scene 45-8 timothy 210 with Dissolve(0.5)
            "As they dance, Anna notices Andrew dancing and talking to another girl."
            "She gets slightly jealous..."
            if AnnaCorruption >=20:
                "But that's hypocritical, she sleeps around with a lot of men herself..."
            scene 45-8 timothy 211 with Dissolve(0.5)
            a "{i}...Well, well...{/i}"
            a "{i}...What is Andrew up to... Never thought him to be like this...{/i}"
            scene 45-8 timothy 212 with Dissolve(0.5)
            a "So... How are you guys doing?"
            fe1 "I'm good!"
            fe1 "Awesome, in fact!"
            scene 45-8 timothy 213 with Dissolve(0.5)
            t "Well, I'm actually kind of tired."
            t "I think I'm going to head out. Heh."
            scene 45-8 timothy 214 with Dissolve(0.5)
            fe1 "Ok..."
            fe1 "It was awesome to see you again, Timothy."
            fe1 "I hope we can see each other again some time."
            t "Definitely!"
            t "Alright, see you around, Felicia."
            scene 45-8 timothy 215 with Dissolve(0.5)
            ash "Heh... Nice outfit, Anna."
            a "What?"
            ash "I knew it was you the moment I saw your curves."
            a "Thanks I guess!"
            a "Anyway, see you around."
            scene 45-8 timothy 216 with Dissolve(0.5)
            t "Take care."
            scene 45-8 timothy 217 with Dissolve(0.5)
            t "Who was that?"
            a "Oh, just some guy I know."
            t "I see."
            scene black with Dissolve(0.5)
            pause 1
            "Some time later."
            stop ambient
            play music tranquility
            scene 45-8 timothy 218 with Dissolve(0.5)
            a "So. How did you enjoy the party?"
            t "The best party I've ever been to."
            a "I'm glad you liked it, heh."
            t "I LOVED it!"
            scene 45-8 timothy 219 with Dissolve(0.5)
            t "I'm really thankful..."
            t "And to actually have hooked up with Felicia... It's crazy."
            a "I'm glad I could've helped."
            scene 45-8 timothy 220 with Dissolve(0.5)
            a "Anyway, I'll head out, got some stuff to take care of."
            t "See you at work, Anna."
            a "Later, Timothy."
            scene black with Dissolve(0.5)
            pause 1
    jump EP16_Home
label EP16_Home:
    $ EP16_var_3 = True
    scene 45-9 home 1 with Dissolve(0.5)
    a "John..."
    a "Slacking, are we?"
    j "What?"
    j "Just chilling."
    scene 45-9 home 2 with Dissolve(0.5)
    j "You look tipsy yourself."
    j "Fun night?"
    a "Heh... Perhaps."
    scene 45-9 home 3 with Dissolve(0.5)
    a "Can't a girl have fun, too?"
    j "Of course you can, just making an observation."
    scene 45-9 home 4 with Dissolve(0.5)
    j "And it looks like you've been out, heh."
    a "Alright, alright."
    a "What you up to?"
    scene 45-9 home 5 with Dissolve(0.5)
    j "Just watching a new series."
    a "Oh?"
    a "What is it?"
    j "Some series about Japan, samurais, and stuff."
    a "Interesting."
    scene 45-9 home 6 with Dissolve(0.5)
    a "Can you pause it?"
    a "I'm going to go change into something more comfortable."
    j "Sure."
    scene black with Dissolve(0.5)
    play sound door2
    scene 45-9 home 7 with Dissolve(0.5)
    if timothySexContent == True:
        a "I wonder what Andrew was doing with those girls..."
        a "Just dancing? Or more?"
    a "Something more comfortable... Hmm..."
    if timothySexContent == True:
        a "{i}...Something to tease Andrew with... {/i}"
    if AnnaCorruption >=30:
        a "{i}...And John too...{/i}"
    play sound undress
    scene 45-9 home 8 with Dissolve(0.5)
    a "That's better..."
    play music lounge
    scene 45-9 home 9 with Dissolve(0.5)
    j "Whaaat?"
    j "{i}...Damn... She's hot as fuck...{/i}"
    j "{i}...Why is she wearing that, though...{/i}"
    scene 45-9 home 10 with Dissolve(0.5)
    j "Why are you wearing that?"
    a "What, you got a problem with how I dress?"
    j "No... Not in the slightest."
    scene 45-9 home 11 with Dissolve(0.5)
    a "Calm down, John."
    a "I find this comfortable and so I wear it."
    j "Uh... Sure."
    scene 45-9 home 12 with Dissolve(0.5)
    j "{i}...Damn...{/i}"
    a "Let's just watch the series, shall we?"
    j "Yeah, ok."
    scene 45-9 home 13 with Dissolve(0.5)
    a "So far it's pretty interesting."
    j "I know right?"
    a "Story is pretty engaging, and the politics."
    j "Yeah."
    scene 45-9 home 14 with Dissolve(0.5)
    a "What?"
    a "Something wrong?"
    scene 45-9 home 15 with Dissolve(0.5)
    j "Mmm..."
    a "Can't handle yourself?"
    j "Uhh... Crazy hard to do that. To be honest."
    scene 45-9 home 16 with Dissolve(0.5)
    a "How about you do me a favor, then."
    j "Whatever you'd like?"
    scene 45-9 home 17 with Dissolve(0.5)
    a "Massage my feet."
    a "I've had a hard day, need to release the tension in them."
    j "Of course, Anna."
    scene 45-9 home 18 with Dissolve(0.5)
    j "Whoa..."
    a "What?"
    j "Your feet are beautiful."
    a "Thank you."
    scene 45-9 home 19 with Dissolve(0.5)
    a "Well, get on with it then."
    j "Sure, yeah."
    j "Just forgot what I was doing for a moment."
    scene 45-9 home 20 with Dissolve(0.5)
    j "Like this?"
    a "Yeah... Mm..."
    a "That feels good."
    j "Nice."
    scene 45-9 home 21 with Dissolve(0.5)
    a "Really relaxing, that's for sure."
    j "That's good to hear, heh."
    a "Your hands are really good."
    scene 45-9 home 22 with Dissolve(0.5)
    a "Anyway... I wanna continue watching."
    a "But you, don't stop."
    j "Ok, Anna."
    a "Heh..."
    scene 45-9 home 23 with Dissolve(0.5)
    "They continue watching the series unravel..."
    "John continues to gently massage Anna's feet."
    "He is becoming increasingly turned on."
    scene 45-9 home 24 with Dissolve(0.5)
    j "So... How was your day?"
    a "Colorful, as usual."
    a "You?"
    j "Oh... Every day has new adventures, to be honest."
    scene 45-9 home 25 with Dissolve(0.5)
    a "Heh..."
    a "You're pretty good at this."
    j "I'm trying my best."
    scene 45-9 home 26 with Dissolve(0.5)
    j "{i}...Fuck...{/i}"
    j "{i}...Can barely keep my dick in my pants...{/i}"
    a "Mhmm..."
    scene 45-9 home 27 with Dissolve(0.5)
    a "Heh..."
    a "Like what you see?"
    j "I... I... {b}*Gulp*{/b}"
    j "Yeah..."
    j "Are you playing with me?"
    a "Heh... Maybe..."
    play sound door2
    scene 45-9 home 28 with Dissolve(0.5)
    j "What?"
    j "{i}...Andrew coming home? Fuck... Why?{/i}"
    scene 45-9 home 29 with Dissolve(0.5)
    a "Huh?"
    scene 45-9 home 30 with Dissolve(0.5)
    pause 1
    scene 45-9 home 31 with Dissolve(0.5)
    a1 "Hey guys..."
    a1 "Uhh..."
    scene 45-9 home 32 with Dissolve(0.5)
    a1 "Uh... What's going on?"
    a1 "Did I miss something?"
    scene 45-9 home 33 with Dissolve(0.5)
    a "Oh, Hey Andrew. John's just massaging my feet."
    a "We're watching a new series, that's all."
    a1 "I see. Uhh..."
    scene 45-9 home 34 with Dissolve(0.5)
    a1 "Should I go away?"
    a1 "And leave you both to it?"
    a "What? No."
    scene 45-9 home 36 with Dissolve(0.5)
    a "What's the deal? John's just massaging my feet."
    j "Yeah, Andrew. Don't be childish. That's all it is."
    a "Ok..."
    scene 45-9 home 37 with Dissolve(0.5)
    "Andrew sits down and watches the series with them..."
    "But Anna's outfit bothers him..."
    scene 45-9 home 38 with Dissolve(0.5)
    a1 "Uhh..."
    a1 "{i}...That outfit is hot... But...{/i}"
    scene 45-9 home 39 with Dissolve(0.5)
    a "{i}...Heh. I wonder what Andrew is thinking...{/i}"
    a "{i}...Did he enjoy seeing that or not...{/i}"
    scene 45-9 home 40 with Dissolve(0.5)
    a "{i}...Seeing how John's massaging my feet...{/i}"
    scene 45-9 home 41 with Dissolve(0.5)
    a1 "Umm..."
    scene 45-9 home 42 with Dissolve(0.5)
    j "Alright. The episode ended..."
    a "Right..."
    a "Pretty good series, so far."
    j "Definitely is."
    scene 45-9 home 43 with Dissolve(0.5)
    a1 "Yeah. I'm kinda tired."
    a "Let's go?"
    a1 "Yeah."
    scene 45-9 home 44 with Dissolve(0.5)
    a "Thanks for the massage, John."
    j "No problem!"
    scene 45-9 home 45 with Dissolve(0.5)
    a "You ok?"
    a "You seem a bit on edge."
    a1 "Well... Kind of."
    scene 45-9 home 46 with Dissolve(0.5)
    a1 "I'm just wondering..."
    a1 "Why are you wearing something like this?"
    a "What do you mean?"
    a1 "Really?"
    scene 45-9 home 47 with Dissolve(0.5)
    a1 "This outfit... It seems a bit too much in these circumstances."
    a1 "I don't like that you wear stuff like this when John's home."
    a1 "Or in the same room as you."
    scene 45-9 home 48 with Dissolve(0.5)
    a "Well... I thought you'd be home so I wore it for you..."
    a "But you weren't. Was a little too lazy to change into something else."
    a1 "Oh... Umm..."
    scene 45-9 home 49 with Dissolve(0.5)
    a "You don't like it when wear stuff like this, when others see?"
    scene 45-9 home 50 with Dissolve(0.5)
    a1 "I... I don't know..."
    a "Anyway, where were you?"
    a1 "Well... I... I was out with Ashley."
    a1 "Got some drinks. Caught up."
    a "Hm... And nothing more?"
    a1 "Well... Not really."
    scene 45-9 home 51 with Dissolve(0.5)
    a "You sure?"
    a1 "Well, I danced with some girls..."
    a1 "I'm sorry."
    scene 45-9 home 52 with Dissolve(0.5)
    a "Come on. It's ok. You were just dancing. We're adults."
    a "You didn't kiss or do anything else with them, right?"
    a1 "No, definitely not."
    a "It's ok then."
    scene 45-9 home 53 with Dissolve(0.5)
    a "But just because you danced with someone else and feel a bit bad about it, doesn't mean I did something."
    a1 "Sure, I understand. Just not in an outfit like this."
    a "Ok, no problem."
    a "Will keep that in mind."
    play sound undress
    scene 45-9 home 54 with Dissolve(0.5)
    a1 "Let's just... Put this behind us. Ok?"
    a "Absolutely."
    a1 "I'm just a bit drunk. Not thinking straight."
    scene 45-9 home 55 with Dissolve(0.5)
    a "So. Where were you?"
    a1 "There was this one cosplay event."
    a1 "Ashley didn't tell me to bring an outfit."
    a1 "So we were definitely out of place, but it was dope."
    a "Oh. Interesting."
    scene 45-9 home 56 with Dissolve(0.5)
    "Anna slowly drifted to sleep while listening to Andrew."
    scene black with Dissolve(0.5)
    pause
    play sound notificationsound
    show text "Friday Morning." with Dissolve (1)
    pause
    scene 46-1 morning 1 with Dissolve(0.5)
    a "Ah..."
    a "What a nice morning."
    play sound undress
    scene 46-1 morning 2 with Dissolve(0.5)
    a "Hmm..."
    a "Perhaps I should go for a run..."
    a "That's always a good idea."
    play sound jacketcloth
    scene 46-1 morning 5-1 with Dissolve(0.5)
    a "There."
    scene 46-1 morning 6-1 with Dissolve(0.5)
    a "Such a good start to the morning."
    a "Let's go."
    scene black with Dissolve(0.5)
    pause 1
    play ambient citytraffic
    play music pianosound volume 0.7
    scene 46-6 running 1 with Dissolve(0.5)
    "Anna headed out."
    "She decided to have a run around the block."
    "Nothing better than a run in the morning."
    a "{i}...Yesterday was... Rather interesting...{/i}"
    scene 46-6 running 2 with Dissolve(0.5)
    if timothySexContent == True:
        a "{i}...My adventures with Timothy... It was all very fun...{/i}"
        a "{i}...I hope he sees that girl more often... It will be really good for him...{/i}"
        a "{i}...And more fun for me... Heh...{/i}"
    a "{i}...The situation with Andrew at home...{/i}"
    scene 46-6 running 3 with Dissolve(0.5)
    a "{i}...That got a little bit awkward...{/i}"
    a "{i}...But I managed to turn away his suspicions...{/i}"
    a "{i}...He seemed unsure whether or not he liked the outfit and that I was with John...{/i}"
    play sound surprise
    scene 46-6 running 4 with Dissolve(0.5)
    stranger "Damn, girl..."
    stranger "Nice body. Definitely can see you work out."
    a "Hehe... Thanks, mister."
    scene 46-6 running 5 with Dissolve(0.5)
    a "I'll get going, then."
    stranger "You sure you don't wanna take a break? Talk some?"
    scene 46-6 running 6 with Dissolve(0.5)
    a "Naah... I will be fine."
    stranger "Sure. Your loss..."
    a "Nope. You know it's yours..."
    stranger "Damn. Touche."
    scene 46-6 running 7 with Dissolve(0.5)
    a "Ahh..."
    a "{i}...Getting kind of thirsty... Should take a break...{/i}"
    a "{i}...Get some water...{/i}"
    scene black with Dissolve(0.5)
    pause 1
    play sound door2
    stop ambient
    scene 46-6 running 8 with Dissolve(0.5)
    a "Ah... Hello."
    sk "Hello. Anna."
    sk "You're looking nice."
    scene 46-6 running 9 with Dissolve(0.5)
    a "Hah. Thanks."
    a "Where do you guys have water?"
    sk "Down the aisle."
    scene 46-6 running 10 with Dissolve(0.5)
    a "Thanks."
    a "{i}...Got pretty thirsty...{/i}"
    a "{i}...Some nice cold water... ah...{/i}"
    scene 46-6 running 11 with Dissolve(0.5)
    a "There..."
    if BenjaminContent == True:
        b1 "Anna?"
        play sound surprise
        scene 46-6 running 12 with Dissolve(0.5)
        a "Benjamin?"
        b1 "OH! Anna! So good to see you!"
        a "You too!"
        scene 46-6 running 13 with Dissolve(0.5)
        b1 "How is your day going?"
        a "Really well. Went for a morning jog."
        b1 "That's absolutely wonderful."
        scene 46-6 running 14 with Dissolve(0.5)
        a "And looks like you're also busy, eh?"
        b1 "Haha. Indeed, indeed. Got myself a job."
        b1 "Never been better!"
        a "That's great!"
        scene 46-6 running 15 with Dissolve(0.5)
        b1 "Yeah. I know..."
        b1 "But... You know. It's hard to escape that life. The habits that form and just the mindset..."
        b1 "But I'm doing my best. I'd much rather choose washing floors for a living than to be on the streets."
        b1 "100%% of the time every time."
        scene 46-6 running 16 with Dissolve(0.5)
        a "So... Are those bums still bothering you?"
        b1 "Which ones?"
        a "The ones that were in the alleyway. That asked you to steal something for them?"
        scene 46-6 running 15 with Dissolve(0.5)
        b1 "Oh. Those. Naah... You dealt with them."
        a "Good."
        scene 46-6 running 17 with Dissolve(0.5)
        a "Anything else? Any other great news?"
        b1 "No... That's about it."
        b1 "Well... There is one thing."
        a "Tell me?"
        scene 46-6 running 18 with Dissolve(0.5)
        b1 "You see, I'm really grateful for everything you've done for me."
        b1 "Truly."
        b1 "And... I've been thinking of a way to thank you."
        scene 46-6 running 19 with Dissolve(0.5)
        b1 "Um... Would you like to have dinner with me at my place?"
        a "Whaat?"
        b1 "Yes, indeed. I used to be good a cooking. Now I've got the opportunity to do it again."
        b1 "Perhaps you'd like to join me?"
        scene 46-6 running 20 with Dissolve(0.5)
        a "Hm... Sure."
        a "Sounds lovely."
        b1 "Really?"
        a "Yeah, why not?"
        b1 "Wonderful!"
        b1 "Thanks so much, Anna."
        a "Hehe."
        scene 46-6 running 21 with Dissolve(0.5)
        a "Alright. Let me know when you've set up everything, ok?"
        b1 "Definitely, Anna."
        scene 46-6 running 22 with Dissolve(0.5)
        a "See you around, Ben."
        b1 "Goodbye, Anna."
        a "Hehe."
        scene 46-6 running 23 with Dissolve(0.5)
        a "I'm very thankful you took him as a cleaner."
        sk "He's been nothing but helpful so far."
        sk "He does more than cleaning. Helps with the products, like my own personal swiss army knife."
        a "I'm glad heh."
    scene 46-6 running 24 with Dissolve(0.5)
    sk "Will that be all?"
    a "Yeah."
    sk "Have a nice day, Anna."
    a "Thank you! You too."
    play sound drinkingBeverage
    scene 46-6 running 25 with Dissolve(0.5)
    a "{i}...Aahh... So nice...{/i}"
    scene black with Dissolve(0.5)
    pause 1
    play sound door2
    scene 46-6 running 26 with Dissolve(0.5)
    a "Ok. Should take a shower and get ready for work."
    play sound shower3
    scene 46-6 running 27 with Dissolve(0.5)
    a "{i}... So nice...{/i}"
    scene 46-6 running 28 with Dissolve(0.5)
    pause 1
    play sound cloth_sound1
    scene 46-6 running 29 with Dissolve(0.5)
    a "There... Should go get dressed and then head out."
    a "{i}...I wonder what today will bring...{/i}"
    scene black with Dissolve(0.5)
    pause 1
    play sound door2
    scene 46-6 running 30 with Dissolve(0.5)
    a "{i}...Still asleep...{/i}"
    a "{i}...I hope he doesn't suspect anything about anything...{/i}"
    a "{i}...I should head to work...{/i}"
    scene 46-6 running 31 with Dissolve(0.5)
    pause 1
    scene black with Dissolve(0.5)
    pause 1
label EP16_Office_Timothy:
    $ EP16_var_4 = True
    scene 46-3 office 1 with Dissolve(0.5)
    t "Hey, Anna."
    t "You doing good today?"
    a "Hey, Timothy."
    scene 46-3 office 2 with Dissolve(0.5)
    a "Yeah. Went for a run. Pretty nice start to a day."
    t "Yeah. Maybe I should also start running. Get my cardio up."
    a "Never a bad thing, that's for sure."
    scene 46-3 office 3 with Dissolve(0.5)
    t "Anyway, I come bearing gifts."
    a "Oh?"
    t "I cracked the encryption on the files and messages that you needed."
    t "Didn't peak or anything. But... You know. Be careful."
    scene 46-3 office 4 with Dissolve(0.5)
    a "Thanks, Timothy. I appreciate your effort."
    t "Don't think nothing of it."
    t "If you ask, I'll help."
    if timothySexContent == True:
        t "Cause you've always helped me, for example yesterday."
        a "Heh... True."
    scene 46-3 office 5 with Dissolve(0.5)
    if timothySexContent == True:
        a "Anyway. How are you feeling after yesterday."
        t "Pretty good. Didn't drink too much, so no headache."
        t "Just reminiscing about the events. Heh."
        t "Shit got wild, you know?"
        a "I agree, but it was fun."
        t "Definitely."
    else:
        a "So, what you've been up to?"
        t "Eh. Nothing. stayed inside."
    scene 46-3 office 6 with Dissolve(0.5)
    a "Thanks for the help, Timothy!"
    a "Again, I appreciate it."
    t "No problem!"
    t "Let me know if you need anything else."
    scene 46-3 office 7 with Dissolve(0.5)
    a "Whoa..."
    a "Andrew was right... And here is the proof..."
    a "Carl was doing some bad things... Fuck..."
    scene 46-3 office 8 with Dissolve(0.5)
    a "He was double-dealing with Fitzgerald... Damn..."
    a "He was stealing money from the earnings..."
    a "And since he's good with accounting, he hid it well..."
    a "It's all here..."
    scene 46-3 office 9 with Dissolve(0.5)
    a "Sergey's business owes a lot to the leaders of this entire 'enterprise'..."
    a "He betrayed us all... Fuck..."
    scene 46-3 office 10 with Dissolve(0.5)
    a "Fucking bastard..."
    a "Rebecca has to know about this..."
    scene 46-3 office 11 with Dissolve(0.5)
    a "I should probably call her..."
    a "But what do I tell her..."
    a "I suppose, I tell her everything..."
    scene 46-3 office 12 with Dissolve(0.5)
    "Anna calls up Rebecca..."
    a "Hey sis. I'm going to go to you later, that ok?"
    r1 "Hey, Sure!"
    r1 "What's up?"
    a "I have some new info about Carl."
    r1 "Oh..."
    scene 46-3 office 13 with Dissolve(0.5)
    a "That bastard was screwing us all..."
    a "Anyway, I'm going to tell you more later. Ok?"
    r1 "Sure."
    r1 "See you, Anna."
    a "Bye."
    scene 46-3 office 14 with Dissolve(0.5)
    a "Fucking Carl... I hate him... For this... How could he do that."
    a "To us..."
    scene 46-3 office 15 with Dissolve(0.5)
    a "Anyway, I should get some work done."
    "And then head to Rebecca."
    scene black with Dissolve(0.5)
    pause 1
    "Sometime later..."
    scene generic office 6 with Dissolve(0.5)
    if EarlHelp == True:
        a "I should return the phone to the police station after I visit Rebecca."
    else:
        $ EP16_var_7 = True
    if GoodBadDoctorChoice == 2:
        scene generic office 5 with Dissolve(0.5)
        d1 "Hello, Anna. I'd like for you to come in today. Remember the event I told you about? It's today."
        jump EP16_Schmidt
    else:
        $ EP16_var_6 = True
        jump EP16_Rebecca
    scene black with Dissolve(0.5)
    pause 1
label EP16_Rebecca:
    play music blues
    $ EP16_var_5 = True
    scene 46-5 rebecca 1 with Dissolve(0.5)
    a "{i}...Michael is here too...{/i}"
    a "{i}...I guess I'll just tell them both...{/i}"
    scene 46-5 rebecca 2 with Dissolve(0.5)
    a "Hey guys."
    m2 "Hey, Anna."
    m2 "How are you doing?"
    a "Uhh... Ok, all things considered."
    m2 "Huh?"
    scene 46-5 rebecca 3 with Dissolve(0.5)
    a "Well, it's about Carl and everything."
    a "Rebecca?"
    scene 46-5 rebecca 4 with Dissolve(0.5)
    r1 "Yeah?"
    a "Alright, I'll just get to the point."
    a "You've told anything to Michael?"
    r1 "Not yet."
    a "Ok, so."
    a "I've got proof of Carl double-dealing."
    scene 46-5 rebecca 5 with Dissolve(0.5)
    a "I cracked his file and message encryption, well, a friend did."
    a "And it shows what he's been stealing and how much..."
    a "Also HE was double dealing with Fitzgerald..."
    a "I read messages they exchanged. HE was behind your kidnapping..."
    scene 46-5 rebecca 6 with Dissolve(0.5)
    a "Carl has been doing a lot of bullshit behind our backs, Michael..."
    a "He has put us in danger..."
    m2 "What?"
    scene 46-5 rebecca 7 with Dissolve(0.5)
    a "That son of a bitch..."
    m2 "Holy shit... Motherfucker..."
    m2 "I... Had no idea, he hid it so well, then."
    a "Yeah..."
    scene 46-5 rebecca 8 with Dissolve(0.5)
    r1 "For a moment, I forgot about it..."
    r1 "It's all real, I thought it was just Andrew being a moron again... But he was right..."
    m2 "Andrew?"
    a "Yeah, he had figured out stuff. That's why he tried to take Andrew out..."
    r1 "What will we do... We need money, how will we get money?"
    m2 "Uh... A job always works..."
    play sound surprise2
    scene 46-5 rebecca 9 with Dissolve(0.5)
    r1 "A job?"
    r1 "I've... Never been good at those things."
    r1 "What do you mean, a job?!"
    m2 "Uh... Sorry..."
    scene 46-5 rebecca 10 with Dissolve(0.5)
    m2 "I didn't mean to upset you."
    r1 "This is so ridiculous..."
    scene 46-5 rebecca 11 with Dissolve(0.5)
    r1 "What do we do, Anna?"
    r1 "We are fucked, aren't we?"
    a "I don't know... But..."
    scene 46-5 rebecca 12 with Dissolve(0.5)
    a "I met with the guy who is Sergeys boss..."
    a "He said that this interruption in the 'business' has gone on too long."
    a "We need to restart its functions."
    scene 46-5 rebecca 13 with Dissolve(0.5)
    a "That means... Sorry, Michael, but you will have to deal."
    m2 "Fuck... I see..."
    m2 "I hoped we could make a clean break..."
    m2 "But I guess this life doesn't leave you behind..."
    scene 46-5 rebecca 14 with Dissolve(0.5)
    a "We've been put into quite a predicament."
    a "They expect things, they know about deficits in the books..."
    a "They want us to do everything that we can to bring Carl in to pay for his crimes..."
    scene 46-5 rebecca 15 with Dissolve(0.5)
    m2 "How will we do that?"
    a "No idea, but one thing at a time."
    a "That scumbag Carl can wait."
    a "First let's focus on getting some money right away. That means, you gotta deal stuff again. They brought new product."
    if EP12_Rebecca_Accept_Offer == True:
        r1 "What about... The scene we talked about?"
        a "You mean the porn shoot?"
        r1 "Yeah, Dylan told me that they've set up almost everything."
        scene 46-5 rebecca 16 with Dissolve(0.5)
        r1 "But they need one more actor, no others are available at the moment."
        r1 "The usual. King? He's unavailable, for some reason."
        r1 "Do you know anyone else?"
        a "No..."
        scene 46-5 rebecca 17 with Dissolve(0.5)
        a "Well..."
        a "Perhaps..."
        r1 "Yeah. Michael."
        a "You could help us out in the scene, couldn't you?"
        scene 46-5 rebecca 18 with Dissolve(0.5)
        m2 "What?"
        m2 "Oh well, I... Didn't expect to... But, I guess if we need the money..."
        m2 "I could help out."
        a "Heh."
        scene 46-5 rebecca 19 with Dissolve(0.5)
        a "Problem solved, then."
    a "Anyway. We will brainstorm more soon. Now I've got other things to do. I'll meet you all later at the shoot, ye?"
    r1 "Ok."
    scene 46-5 rebecca 20 with Dissolve(0.5)
    a "Bye for now."
    scene black with Dissolve(0.5)
    if EarlHelp == True:
        jump EP16_Police
    else:
        if EP12_Rebecca_Accept_Offer == True:
            jump EP16_Dylan
        else:
            jump EP16_Ending
label EP16_Schmidt:
    $ EP16_var_6 = True
    scene 46-2 schm 1 with Dissolve(0.5)
    a "Hello. You said you'd like to see me?"
    d1 "Yes, yes I did."
    scene 46-2 schm 2 with Dissolve(0.5)
    d1 "We've got important business today."
    d1 "I'm leading a presentation today and you, dear Anna, will be the subject."
    scene 46-2 schm 3 with Dissolve(0.5)
    d1 "As you know, we've been testing you for some time now."
    a "I wouldn't call it testing... More like using."
    d1 "Nonsense. We've definitely been testing you. And have to some very interesting conclusions."
    d1 "Now. Since I'm presenting today, and since you're my subject, you'll have to come with me to the auditorium."
    a "Ok... Doesn't sound too hard."
    d1 "On one condition."
    a "Uh..."
    scene 46-2 schm 2 with Dissolve(0.5)
    d1 "Remember what you wore last time?"
    a "That skimpy outfit?"
    d1 "The same one, indeed. You will wear that."
    a "WHAT?"
    d1 "It's a part of our presentation. No other way."
    scene 46-2 schm 4 with Dissolve(0.5)
    a "This has got to be a joke."
    d1 "I assure you, this is no laughing matter."
    d1 "Now, go on."
    d1 "I'm anxious to see you wear it."
    play sound undress
    scene 46-2 schm 5 with Dissolve(0.5)
    a "Ugh..."
    a "I hope you know what you're doing."
    scene 46-2 schm 6 with Dissolve(0.5)
    d1 "Ohh... Trust me. I am."
    d1 "This is of utmost importance. Cutting edge science."
    d1 "For the benefit of all mankind."
    play sound jacketcloth
    scene 46-2 schm 7 with Dissolve(0.5)
    a "So. Is it satisfactory?"
    d1 "More than that."
    d1 "It's ideal, and will fit our presentation perfectly."
    a "Sure..."
    scene 46-2 schm 8 with Dissolve(0.5)
    d1 "Hehe... I like where this is going."
    a "I sometimes forget, for a moment, that you are a perverted old man."
    a "And I do this just because I owe you."
    d1 "You can rationalize it all you want. Deep down, you know that's not true."
    a "Hmph..."
    scene 46-2 schm 9 with Dissolve(0.5)
    a "Let's get this over with."
    a "Shall we?"
    d1 "Hehe... Can't wait to present yourself to people?"
    scene 46-2 schm 10 with Dissolve(0.5)
    a "Can't wait to get out of this ridiculous getup."
    d1 "Oh it's not so bad. Once you get used to it."
    a "I don't think I ever will."
    d1 "With time, we can do a lot more."
    a "Whatever."
    scene 46-2 schm 11 with Dissolve(0.5)
    d1 "Just try to keep it down in there, let me do the talking."
    d1 "Speak when spoken to, ok?"
    d1 "If you do, everything will go swimmingly."
    a "Fine."
    scene black with Dissolve(0.5)
    pause 1
    play sound door2
    play music PPMCasualReception
    scene 46-2 schm 12 with Dissolve(0.5)
    d1 "Alright, settle down class."
    a "..."
    scene 46-2 schm 13 with Dissolve(0.5)
    a "{i}...Fuck...{/i}"
    scene 46-2 schm 14 with Dissolve(0.5)
    a "Are you kidding me?"
    a "This class is full of people."
    d1 "Hehe... A lot of aspiring new scientists, doctors, and whatnot."
    scene 46-2 schm 15 with Dissolve(0.5)
    d1 "Today, I've prepared an inordinary presentation."
    d1 "Since this class is about the human body, and more specifically about the brain."
    d1 "I've prepared some interesting, material for you all today."
    d1 "So. This is Anna."
    scene 46-2 schm 16 with Dissolve(0.5)
    d1 "Some time ago, Anna suffered a traumatic event. injuring her brain somewhat."
    d1 "In a car crash."
    d1 "Luckily it didn't have any adverse effects besides one."
    d1 "Her inhibitions seem to have been impacted."
    d1 "What I mean by that, more specifically, is sexual inhibitions."
    d1 "This head trauma she suffered has caused elevated libido, lowered inhibitions, and self-control."
    scene 46-2 schm 17 with Dissolve(0.5)
    d1 "This is quite an interesting case. Because there isn't much research on this."
    d1 "Yes we know brain injury can fundamentally change a person, their character, their identity even."
    d1 "But this time, it's rather specific. Everything else like memory, intellect, common sense, reasoning are all there, with the exception of sexual contexts."
    d1 "Today you've all been distributed copies of my current hypotheses, and available data, so far."
    scene 46-2 schm 18 with Dissolve(0.5)
    d1 "Now, Anna. Could you answer..."
    d1 "How do you feel right now?"
    if AnnaCorruption >=30:
        a "I don't know... embarrassed?"
    d1 "It's important you be honest."
    a "Well..."
    if AnnaCorruption >=20:
        a "I also feel slightly aroused."
        a "From everyone looking at me in this outfit..."
        a "I don't know..."
        d1 "Wonderful... And intriguing."
    else:
        a "I can't answer that..."
        d1 "Hmm..."
    scene 46-2 schm 19 with Dissolve(0.5)
    a "But... Isn't it normal to feel confident about yourself?"
    d1 "Agreed, the difference here is you can't control yourself. Regular people would feel embarrassed, wouldn't participate, would try to cover up."
    a "I... I suppose..."
    d1 "We should note, that she has not been under the influence of mind-altering drugs or alcohol or anything."
    scene 46-2 schm 20 with Dissolve(0.5)
    d1 "Now. This could be a case of nymphomania or hypersexuality."
    d1 "Since injuries could cause this."
    d1 "But it's often hard to find patients like this."
    d1 "That is what we are here to discover."
    scene 46-2 schm 21 with Dissolve(0.5)
    d1 "For now what I can say for sure is that there are responses that happen when Anna is exposed to triggers."
    d1 "For one, she gets very, very aroused and lubricated down there."
    d1 "Her senses become heightened, and it's easier to pleasure her."
    scene 46-2 schm 22 with Dissolve(0.5)
    d1 "Yes, sir."
    student1 "How many partners have you had in the recent times?"
    a "Umm... I don't know..."
    student1 "Surely you can answer..."
    a "..."
    scene 46-2 schm 23 with Dissolve(0.5)
    a "To be honest, I've lost count..."
    d1 "Exactly."
    d1 "She is curious herself about all of this..."
    scene 46-2 schm 24 with Dissolve(0.5)
    a "Maybe five..."
    if AnnaCorruption >=30:
        scene 46-2 schm 25 with Dissolve(0.5)
        a "Times... five?"
        d1 "So you see... plenty..."
    scene 46-2 schm 26 with Dissolve(0.5)
    a "Ah..."
    d1 "If I touch her, she responds immediately. with uncontrolled gasps."
    d1 "That reflects her increasing arousal."
    scene 46-2 schm 27 with Dissolve(0.5)
    student2 "Sorry sir, but all this seems highly inappropriate."
    student2 "This is a respectable establishment, we shouldn't stoop down to our baser instincts."
    d1 "Of course it's inappropriate."
    d1 "And whatever else. But so is science. It doesn't care about your feelings."
    d1 "Hard facts."
    d1 "And the fact is, we need to study people such as her more."
    d1 "Because we will understand more about ourselves. How to heal ourselves and such."
    scene 46-2 schm 28 with Dissolve(0.5)
    d1 "Now... I'd like to uncover your breasts..."
    a "Oh..."
    play sound undress
    scene 46-2 schm 29 with Dissolve(0.5)
    "The room was filled with audible noises of people being intrigued."
    d1 "How does this make you feel?"
    a "I... I like it when people see my naked breasts."
    d1 "Interesting..."
    scene 46-2 schm 30 with Dissolve(0.5)
    d1 "Is there any more arousal if one person seems them or several?"
    a "The more people, the more aroused I get."
    d1 "Very interesting."
    scene 46-2 schm 31 with Dissolve(0.5)
    d1 "Do you like the idea of all those men seeing your naked breasts?"
    a "Yes..."
    a "It's... Weird... But I do..."
    d1 "Curious."
    scene 46-2 schm 32 with Dissolve(0.5)
    d1 "Very nice indeed..."
    student1 "This is one of the greatest presentations ever."
    student2 "I still think it's wrong."
    scene 46-2 schm 33 with Dissolve(0.5)
    d1 "I hear you but do not fret. This all may seem circumstantial and subjective..."
    d1 "But Like I said before, science doesn't care about feelings, and neither do I."
    d1 "Same as science, I like facts."
    d1 "We will now move on to the MRI room."
    d1 "Where we will put Anna into the machine and scan her brain."
    scene 46-2 schm 34 with Dissolve(0.5)
    a "What?"
    d1 "Yes, this is only the first part."
    d1 "Everyone who's interested please follow me to the MRI room."
    d1 "We shall continue the experiment there."
    scene 46-2 schm 35 with Dissolve(0.5)
    d1 "{i}...This will be fun... Hehe...{/i}"
    a "{i}...What have I gotten myself into...{/i}"
    scene 46-2 schm 36 with Dissolve(0.5)
    d1 "This is the fun part. Heh."
    scene 46-2 schm 37 with Dissolve(0.5)
    a "Eh..."
    a "{i}...But... It will help me understand it all better...{/i}"
    a "{i}...I hope...{/i}"
    scene black with Dissolve(0.5)
    pause 1
    scene 46-2 schm 38 with Dissolve(0.5)
    d1 "So. This is the MRI room."
    d1 "This is where we will conduct the practical part of the experiment."
    d1 "We will produce stimuli while Anna's brain is in the MRI."
    d1 "We shall record them and look for abnormalities."
    scene 46-2 schm 39 with Dissolve(0.5)
    d1 "This is Doctor Harold, he will conduct the stimulation part of the experiment."
    d1 "It's important that we observe every detail."
    d1 "As to not miss anything."
    scene 46-2 schm 40 with Dissolve(0.5)
    h "Hello everyone."
    h "I look forward to bringing new data to the table."
    scene 46-2 schm 41 with Dissolve(0.5)
    h "Hello, Anna."
    a "Harold?"
    scene 46-2 schm 42 with Dissolve(0.5)
    d1 "Now, Anna. I'd like you to undress your top, and get into the machine."
    a "Undress?"
    d1 "Yes. It's a part of the demonstration."
    a "Ugh..."
    scene 46-2 schm 43 with Dissolve(0.5)
    a "I hope this is worth it..."
    a "I wonder if it is, to be honest."
    d1 "Oh it is. Trust me. I would know."
    a "Having a hard time."
    d1 "Now, now. If you've come this far, might as well finish."
    a "Sure..."
    scene 46-2 schm 44 with Dissolve(0.5)
    pause 1
    play sound undress
    scene 46-2 schm 45 with Dissolve(0.5)
    a "Hold this for me, will you?"
    h "Ok."
    scene 46-2 schm 46 with Dissolve(0.5)
    a "{i}...This is so weird... So many men looking at me...{/i}"
    a "{i}...I'm kind of aroused... So many of them looking at me, lusting for me...{/i}"
    scene 46-2 schm 47 with Dissolve(0.5)
    a "{i}...Damn...{/i}"
    "A lof the Students were intrigued... Well, mostly because they were seeing a naked woman doing all this naughty business."
    "Just a few were actually interested in the science behind it... Which was second-rate at best..."
    h "Settle in comfortably."
    scene 46-2 schm 48 with Dissolve(0.5)
    h "And try your best not to move, ok?"
    a "Sure..."
    h "Most of all, keep your head as steady as possible."
    scene 46-2 schm 49 with Dissolve(0.5)
    d1 "Now... We shall all go into the observation room."
    play sound surprise2
    scene 46-2 schm 50 with vpunch
    d1 "LISTEN!"
    scene 46-2 schm 51 with Dissolve(0.5)
    d1 "We've got science to conduct. Follow me into the Observation room!"
    d1 "Otherwise we cannot continue."
    d1 "You all surely would like to see more, yes?"
    cr12 "Mhm..."
    scene 46-2 schm 52 with Dissolve(0.5)
    "All of them entered and stared at Anna from afar."
    d1 "I will start up the MRI machine and we will start to get some readings."
    d1 "At first we will see how her brain is when it's close baseline."
    d1 "Do note, it's not completely baseline since she's already been exposed to stimuli, such as showing her breasts..."
    scene 46-2 schm 53 with Dissolve(0.5)
    d1 "Alright, Harold."
    d1 "You may start the machine."
    scene 46-2 schm 54 with Dissolve(0.5)
    h "Got it."
    scene 46-2 schm 55 with Dissolve(0.5)
    h "Try to remain calm and move as little as possible."
    a "Ok."
    a "What will you do?"
    scene 46-2 schm 56 with Dissolve(0.5)
    h "Oh. Just some stimulation exercises, Don't worry."
    a "What kind of stimulation."
    h "Don't you know?"
    a "Sexual?"
    h "More or less."
    h "Alright, you're going in."
    scene 46-2 schm 57 with Dissolve(0.5)
    h "You feeling all good and comfortable in there?"
    a "Yeah. I'm ok."
    h "Good."
    scene 46-2 schm 58 with Dissolve(0.5)
    h "She's all settled in, the machine is spinning up."
    h "Anything else you need now?"
    d1 "Wait a bit."
    scene 46-2 schm 59 with Dissolve(0.5)
    d1 "We are seeing the first images. they will all be recorded so we will be able to see and compare them afterward."
    d1 "As you see, they are mostly normal. if we take into consideration her current state."
    d1 "We can see the regular areas light up with her arousal more so than usual in patients. But not as much still..."
    scene 46-2 schm 60 with Dissolve(0.5)
    a "{i}...This machine is loud...{/i}"
    a "{i}...I wonder what exactly Harold will try to do to me...{/i}"
    scene 46-2 schm 61 with Dissolve(0.5)
    d1 "Alright, Harold."
    d1 "You may proceed with the first stimulation exercise."
    label EP16_Schmidt_Sex_Scene:
    $ persistent.scene_48 = True
    scene 46-2 schm 62 with Dissolve(0.5)
    h "With pleasure."
    play music SexyTimeSong3
    scene 46-2 schm 63 with Dissolve(0.5)
    h "I will start with light touching."
    h "Slowly moving closer to erogenous zones."
    d1 "Correct."
    scene 46-2 schm 64 with Dissolve(0.5)
    h "How are you feeling in there, Anna?"
    a "Umm... Fine..."
    a "Harold is touching me gently... It's..."
    a "Nice..."
    h "Very good."
    scene 46-2 schm 65 with Dissolve(0.5)
    a "Mm..."
    "Harold was gentle... taking his time."
    "The machine needed to take images with each stimulus."
    h "{i}...Very nice...{/i}"
    scene 46-2 schm 66 with Dissolve(0.5)
    "Harold moved to her pussy area."
    a "Ah..."
    h "Yeah... You like that, Anna?"
    a "I... I..."
    scene 46-2 schm 67 with Dissolve(0.5)
    "The students were all in awe as to how Schmidt was able to get a girl like Anna to participate in such an experiment."
    "They were impressed and also turned on."
    d1 "Very good, we are starting to see the brain light up like crazy."
    d1 "She's showing a lack of inhibitions as seen in the brain scan."
    scene 46-2 schm 68 with Dissolve(0.5)
    student2 "I still think this is inappropriate and wrong."
    d1 "Then how about you leave if you can't handle science in it's rawest form."
    cr12 "Yeah, hush, dude!"
    scene 46-2 schm 69 with Dissolve(0.5)
    d1 "You are doing great Harold. Keep going."
    d1 "All our observations are logical. As Harold increases the stimuli, she reacts more."
    d1 "Makes sense. But the difference is, that she reacts more intensely. Experiences more intense pleasure and so on."
    scene 46-2 schm 70 with Dissolve(0.5)
    "Harold went closer to her vagina."
    a "Mh..."
    "Anna felt somewhat embarrassed, but she had a hard time asking anyone to stop."
    "She liked it."
    play sound undress
    scene 46-2 schm 71 with Dissolve(0.5)
    h "Oh. I see something very appealing."
    h "Hehe... Nice."
    scene 46-2 schm 72 with Dissolve(0.5)
    h "Yesss..."
    d1 "Do not dily daly and get on with it, Harold."
    play sound jerk2
    scene 46-2 schm 73 with Dissolve(0.5)
    pause 1
    play sound femmoan_2
    scene 46-2 schm 74 with Dissolve(0.5)
    a "Oh..."
    h "Yeahh... Awesome."
    play sound femmoan_3
    scene 46-2 schm 75 with Dissolve(0.5)
    a "AAhh..."
    a "That's... Mhm..."
    scene 46-2 schm 76 with Dissolve(0.5)
    pause 1
    $ different_choice_menu = True
    $ EP16_Anim_Option = 1
    $ EP16_Anim_Speed = 1
    scene black
    show Ep16_Schmidt_Anim_1 with Dissolve(0.5)
    play sound jerk2
    label EP16_Schmidt_Fingering_Label:
        a "Oh..."
        a "Ahh..."
        a "Those fingers are good..."
        menu EP16_Schmidt_Fingering_Menu:
            "View 1":
                hide Ep16_Schmidt_Anim_1
                hide Ep16_Schmidt_Anim_1_Faster
                $ EP16_Anim_Option = 1
                show Ep16_Schmidt_Anim_1 with Dissolve(0.5)
                jump EP16_Schmidt_Fingering_Menu
            "Slower":
                hide Ep16_Schmidt_Anim_1
                hide Ep16_Schmidt_Anim_1_Faster
                $ EP16_Anim_Speed = 1
                show Ep16_Schmidt_Anim_1 with Dissolve(0.5)
                jump EP16_Schmidt_Fingering_Menu
            "Faster":
                hide Ep16_Schmidt_Anim_1
                hide Ep16_Schmidt_Anim_1_Faster
                $ EP16_Anim_Speed = 2
                show Ep16_Schmidt_Anim_1_Faster with Dissolve(0.5)
                jump EP16_Schmidt_Fingering_Menu
            "Continue":
                hide Ep16_Schmidt_Anim_1
                hide Ep16_Schmidt_Anim_1_Faster
                $ different_choice_menu = False
                stop sound
                pass
    scene 46-2 schm 77 with Dissolve(0.5)
    a "Yeah... Keep doing that."
    scene 46-2 schm 78 with Dissolve(0.5)
    d1 "Astounding."
    d1 "Her brain lights up like a Christmas tree."
    d1 "A complete disinhibition. She is letting go entirely."
    d1 "She is forgetting that there is a room full of people watching."
    d1 "The stimuli give her feelings so intense, she doesn't care about the social norms and such."
    scene 46-2 schm 79 with Dissolve(0.5)
    cr12 "Wow."
    scene 46-2 schm 80 with Dissolve(0.5)
    student1 "Will we continue increasing the stimuli?"
    student1 "There is bound to be more data to be seen."
    scene 46-2 schm 81 with Dissolve(0.5)
    d1 "Hehe... Spoken like a true scientist."
    d1 "Of course."
    d1 "We will go further."
    scene 46-2 schm 82 with Dissolve(0.5)
    d1 "In the name of science."
    d1 "Go and help Harold."
    d1 "Take this tool with you, use it on Anna."
    d1 "I assume you'll know what to do?"
    student1 "Of course."
    scene 46-2 schm 83 with Dissolve(0.5)
    student1 "I've been instructed by Dr. Schmidt to help you out."
    h "Heh. Cool."
    scene 46-2 schm 84 with Dissolve(0.5)
    h "This girl... I've known her for a while. She's really quite something."
    h "A nympho. It's crazy."
    student1 "Heh... That's interesting."
    h "Come on. give her some love."
    scene 46-2 schm 85 with Dissolve(0.5)
    student1 "Shiiiet."
    play sound jerk2
    scene 46-2 schm 86 with Dissolve(0.5)
    a "AH... AAHHH!!!"
    a "So good..."
    h "Try to not move your head."
    scene 46-2 schm 87 with Dissolve(0.5)
    a "Don't stop... Please..."
    play sound female_moan_1
    scene 46-2 schm 88 with Dissolve(0.5)
    a "Ohh..."
    play sound jerk2
    scene 46-2 schm 89 with Dissolve(0.5)
    student1 "This is awesome. Best lecture ever!"
    play audio female_moan_2
    scene 46-2 schm 90 with Dissolve(0.5)
    student1 "Haha! Fucking awesome. This bitch is crazy!"
    "The tension was building inside of Anna. She was getting closer and closer to climax."
    scene 46-2 schm 91 with Dissolve(0.5)
    "As the rest of the students and Dr. Schmidt looked."
    "But Anna didn't care, she had forgotten about the onlookers."
    "What she had now was just the dildo toy and her pleasure."
    scene 46-2 schm 92 with Dissolve(0.5)
    h "Hehe... I'll join in if you don't mind. And you switch to her anus. Ye?"
    student1 "Great idea!"
    h "Exactly!"
    student1 "This is one of the best experiments I've ever participated in."
    play sound jerk3
    scene 46-2 schm 93 with Dissolve(0.5)
    pause 1
    scene 46-2 schm 94 with Dissolve(0.5)
    pause 1
    scene 46-2 schm 95 with Dissolve(0.5)
    pause 1
    play sound female_moan_3
    scene 46-2 schm 96 with Dissolve(0.5)
    a "AAAHHHaAAAAAAAAH!!"
    "Anna completely lost it when they double penetrated her holes."
    a "OOHAAH FUCK!"
    $ different_choice_menu = True
    $ EP16_Anim_Option = 1
    $ EP16_Anim_Speed = 1
    scene black
    show Ep16_Schmidt_Anim_3 with Dissolve(0.5)
    play sound jerk2 loop
    label EP16_Schmidt_Fingering_2_Label:
        a "Oh..."
        a "Ahh..."
        a "Those fingers are good..."
        menu EP16_Schmidt_Fingering_2_Menu:
            "View 1":
                hide Ep16_Schmidt_Anim_3
                hide Ep16_Schmidt_Anim_3_Faster
                $ EP16_Anim_Option = 1
                show Ep16_Schmidt_Anim_3 with Dissolve(0.5)
                jump EP16_Schmidt_Fingering_2_Menu
            "Slower":
                hide Ep16_Schmidt_Anim_3
                hide Ep16_Schmidt_Anim_3_Faster
                $ EP16_Anim_Speed = 1
                show Ep16_Schmidt_Anim_3 with Dissolve(0.5)
                jump EP16_Schmidt_Fingering_2_Menu
            "Faster":
                hide Ep16_Schmidt_Anim_3
                hide Ep16_Schmidt_Anim_3_Faster
                $ EP16_Anim_Speed = 2
                show Ep16_Schmidt_Anim_3_Faster with Dissolve(0.5)
                jump EP16_Schmidt_Fingering_2_Menu
            "Continue":
                hide Ep16_Schmidt_Anim_3
                hide Ep16_Schmidt_Anim_3_Faster
                $ different_choice_menu = False
                stop sound
                pass
    scene 46-2 schm 97 with Dissolve(0.5)
    d1 "These readings are off the charts."
    d1 "Astounding really. She is experiencing so much pleasure."
    d1 "Despite all the circumstances. It's fascinating."
    d1 "But we have to stop there..."
    scene 46-2 schm 98 with Dissolve(0.5)
    d1 "Alright you two. You can stop."
    d1 "We've got enough data."
    scene 46-2 schm 99 with Dissolve(0.5)
    h "Really?"
    h "You sure, sir?"
    d1 "Absolutely."
    scene 46-2 schm 100 with Dissolve(0.5)
    a "Huh?"
    scene 46-2 schm 101 with Dissolve(0.5)
    a "Why... Why did you stop?"
    h "Doctors orders."
    a "Uhh..."
    scene 46-2 schm 102 with Dissolve(0.5)
    a "Wow... So you used this on me?"
    student1 "Sure did."
    student1 "You are a very interesting case, that's for sure."
    scene 46-2 schm 103 with Dissolve(0.5)
    student1 "I hope you didn't feel too embarrassed."
    a "Actually... Um... I forgot all about it."
    student1 "Really?"
    scene 46-2 schm 104 with Dissolve(0.5)
    d1 "So. We've come to the end of our experiment. We've got some incredible data from the MRI scans."
    d1 "I will need time to go over it. But you did great. Fascinating stuff, indeed."
    scene 46-2 schm 105 with Dissolve(0.5)
    a "Uhh... So what's next?"
    d1 "That is all for now."
    scene 46-2 schm 106 with Dissolve(0.5)
    d1 "Alright class. This concludes our presentation. I will need some time to go over the data, you will be the first to see my analysis of it."
    d1 "We are seeing some new, groundbreaking data. It's a wonderful time to be alive."
    d1 "Truly."
    d1 "I will keep you all appraised of any developments and anything interesting I discover."
    scene 46-2 schm 107 with Dissolve(0.5)
    d1 "We are at the brink of potentially groundbreaking things."
    d1 "So keep your eyes and ears open. We are helping humanity here."
    d1 "That's all, dismissed."
    scene 46-2 schm 108 with Dissolve(0.5)
    d1 "That's all for today."
    d1 "Anna, I want to see you in my office."
    a "Uh. Ok."
    scene 46-2 schm 109 with Dissolve(0.5)
    h "This was an interesting experience."
    a "I... Suppose."
    a "But why did you have to stop."
    d1 "Because I said so."
    d1 "Get dressed and let's go."
    $ renpy.end_replay()
    scene black with Dissolve(0.5)
    pause 1
    play sound door2
    play music pianosound
    scene 46-2 schm 110 with Dissolve(0.5)
    d1 "I will not go into the details of what I saw both in the scans and in your reactions."
    d1 "But I will say this, you are quite the nympho."
    a "Excuse me?"
    d1 "Now, don't get me wrong, I'm very intrigued by the science, but this is very irregular."
    d1 "At one point you didn't care at all."
    a "I... Don't know what to say."
    scene 46-2 schm 111 with Dissolve(0.5)
    a "I'm sorry? I guess..."
    d1 "Sorry? For what? This is amazing stuff. I'm going to become one of the leading scientists with this research."
    a "So..."
    a "I'm just a tool for your ambitions?"
    d1 "Not at all, Anna. Remember, our discoveries will help you resolve your issues."
    a "So it has nothing to do with your depraved fantasies and fetishes?"
    d1 "Heh... I will not comment on that."
    scene 46-2 schm 112 with Dissolve(0.5)
    a "Sure..."
    a "I really want to see results for all this stuff..."
    d1 "Do you really?"
    d1 "Isn't it better when you have sex and you experience pleasure several times more intense than normal people?"
    d1 "That you can get off so much more easily than others? You can have sex with almost anyone and not care?"
    a "Uh..."
    scene 46-2 schm 113 with Dissolve(0.5)
    d1 "Regardless... That's a topic for another time."
    d1 "I'm certain you will have to come in again sometime."
    d1 "For another session."
    a "Another?"
    d1 "Yes. There are some more things we can test for. Finalize the experiment, so to speak."
    d1 "I will contact you when I have need of you."
    a "But..."
    d1 "Trust me that it will be beneficial..."
    d1 "You can get changed."
    play sound undress
    scene 46-2 schm 114 with Dissolve(0.5)
    "At this point Annas head was filled with confusion."
    "Why was she doing this..."
    "Was it because she wanted to solve her issue or simply because she just liked the attention."
    "Liked to be seen by many strangers..."
    scene 46-2 schm 115 with Dissolve(0.5)
    a "Alright. I'm going. I'd like this all to be worth it in the end."
    d1 "Oh it will be."
    d1 "Trust me."
    scene 46-2 schm 116 with Dissolve(0.5)
    d1 "Heh..."
    d1 "Next phase will be that much better."
    scene 46-2 schm 117 with Dissolve(0.5)
    d1 "Next time, those suckers will have to pay..."
    d1 "And they will. Cause they all want to see hot Anna again."
    d1 "Hehe..."
    scene black with Dissolve(1)
    pause 1
    jump EP16_Rebecca
label EP16_Police:
    play music jazzmusic
    $ EP16_var_7 = True
    scene 46-4 police 1 with Dissolve(0.5)
    pause 1
    scene 46-4 police 2 with Dissolve(0.5)
    a "Hello, sir."
    cop1 "Anna. Uhh... Hello."
    a "I need to talk to you about some information I have."
    scene 46-4 police 3 with Dissolve(0.5)
    cop1 "Sure."
    cop1 "Right this way."
    a "Thank you."
    play sound door2
    scene 46-4 police 4 with Dissolve(0.5)
    cop1 "So uhh..."
    cop1 "What do you have for me?"
    a "I came to return the phone. Decided not to talk about it out loud in front of other officers."
    cop1 "Good call."
    scene 46-4 police 5 with Dissolve(0.5)
    cop1 "Do you have any info or you didn't manage to crack it open?"
    a "I did..."
    cop1 "How? Our best guys couldn't."
    a "I know some people..."
    cop1 "Best I don't ask."
    scene 46-4 police 6 with Dissolve(0.5)
    cop1 "Also, about the other day..."
    a "No need to mention it."
    cop1 "Uhh.. Ok..."
    cop1 "So what did you find out?"
    scene 46-4 police 7 with Dissolve(0.5)
    a "Well... Carl... Has been double-dealing with Fitzgerald. Or was."
    a "They were in on Rebecca's kidnapping."
    cop1 "What the..."
    a "You don't know the half of it..."
    a "And... He had been stealing from the operation."
    a "So... Yeah..."
    scene 46-4 police 8 with Dissolve(0.5)
    cop1 "That's... very serious..."
    cop1 "How have you managed to keep your head through all this ruckus?"
    a "Lucky, I guess..."
    cop1 "Earl should know about this, He'd be able to make heads or tails."
    cop1 "Unfortunately he's been reassigned to another case."
    cop1 "For now."
    a "I'm glad... He's not exactly a person I'd want to see."
    cop1 "Fair enough."
    a "Anyway."
    scene 46-4 police 9 with Dissolve(0.5)
    a "Here's the phone as promised."
    cop1 "Oh..."
    cop1 "Thank you."
    scene 46-4 police 10 with Dissolve(0.5)
    cop1 "So... We have our hands full..."
    cop1 "One thing that bothers me, not connected to your problem is Fitzgerald and his angle..."
    cop1 "After Sergey and Carl were arrested and we found Fitzgerald's brother dead..."
    cop1 "We seemed to have lost Fitzgerald's scent. Like he's gone..."
    cop1 "If you, during your endeavours find out anything new, please let me know..."
    cop1 "Something here smells fishy..."
    a "I'll do what I have to..."
    cop1 "I won't ask... But be careful. If you get caught in the crossfire between the police and the bad guys..."
    cop1 "I cannot guarantee your safety."
    scene 46-4 police 11 with Dissolve(0.5)
    a "Hehe... Perhaps..."
    a "But I know for certain that you'd do what I ask of you..."
    a "Wouldn't you?"
    cop1 "Uhh..."
    a "You haven't forgotten our little activity the other day?"
    cop1 "Umm... I... I have work to do..."
    a "Heh..."
    scene black with Dissolve(0.5)
    pause 1
    scene 46-4 police 12 with Dissolve(0.5)
    a "See you around, sir."
    cop1 "You have a good day, ma'am..."
    scene 46-4 police 13 with Dissolve(0.5)
    pause 1
    scene black with Dissolve(0.5)
    pause 1
    jump EP16_Dylan
label EP16_Dylan:
    $ EP16_var_9 = True
    play music bythepool
    scene 46-7 shoot 1 with Dissolve(0.5)
    a "{i}...A bit of a different shoot, where Rebecca is involved...{/i}"
    a "{i}...Something new... Heh...{/i}"
    scene 46-7 shoot 2 with Dissolve(0.5)
    a "Hey guys."
    d3 "Hello, Anna. Alright. Everyone's here."
    j2 "Hey, Anna."
    m2 "Hey!"
    r1 "Oh, hello sweety."
    scene 46-7 shoot 3 with Dissolve(0.5)
    r1 "Got here ok?"
    a "Yeah. All good."
    r1 "Dilan's explaining a few things to Michael."
    a "Oh?"
    scene 46-7 shoot 4 with Dissolve(0.5)
    d3 "Well, not really that much to explain."
    d3 "Just some tips and tricks."
    d3 "General things. he'll help us with the set up of the scene, too."
    scene 46-7 shoot 5 with Dissolve(0.5)
    d3 "I'm short on hands this time."
    d3 "So this will have to do."
    d3 "I think we'll be ok."
    scene 46-7 shoot 6 with Dissolve(0.5)
    m2 "But I haven't really done anything like this before."
    d3 "There isn't much to it."
    m2 "I mean, I don't know the things I'm supposed to do."
    scene 46-7 shoot 7 with Dissolve(0.5)
    m2 "You know?"
    r1 "Heh... If I know one thing, you'll be fine. You're pretty good in bed."
    r1 "That's all there is to it. I think."
    if AnnaCorruption >=30:
        scene 46-7 shoot 8 with Dissolve(0.5)
        a "I... can I also vouch for that."
        m2 "Khem..."
        d3 "Heh... Alright then. That's covered."
        scene 46-7 shoot 9 with Dissolve(0.5)
        a "Hehe..."
    scene 46-7 shoot 10 with Dissolve(0.5)
    d3 "Anyway. We have to carry the gear to the car."
    d3 "Meanwhile you girls can go dressed. I've prepped the outfits for you."
    a "Alright. Thanks."
    scene 46-7 shoot 11 with Dissolve(0.5)
    a "And you? How are you doing?"
    r1 "I'm a bit nervous..."
    scene 46-7 shoot 12 with Dissolve(0.5)
    a "That's understandable."
    a "I also get like that sometimes. No worries."
    scene 46-7 shoot 13 with Dissolve(0.5)
    r1 "I haven't exactly done anything like this, either."
    r1 "Maybe pics, but not a full-on scene."
    a "Really?"
    a "Heh... you'll be natural."
    play sound undress
    scene 46-7 shoot 14 with Dissolve(0.5)
    r1 "You really think so?"
    a "I know so."
    r1 "Thanks."
    r1 "I appreciate the support."
    scene 46-7 shoot 15 with Dissolve(0.5)
    r1 "I wonder what outfits he's got for us."
    a "Probably pretty good ones."
    a "Dilan usually has a good taste."
    scene black with Dissolve(0.5)
    pause 0.5
    play sound cloth_sound1
    scene 46-7 shoot 16 with Dissolve(0.5)
    a "Well, well..."
    r1 "This is pretty darn nice."
    a "Yeah. Hah."
    scene 46-7 shoot 17 with Dissolve(0.5)
    r1 "How do I look?"
    a "Like a bad girl. Heh."
    r1 "Thank you, Anna."
    scene 46-7 shoot 18 with Dissolve(0.5)
    a "Like I said. A natural. You look the part already."
    a "You'll probably act the part, too."
    r1 "Yeah. I'm feeling more confident now."
    a "Good. How do I look?"
    r1 "Do I even have to say?"
    r1 "You look like you're about to steal someone's man, that's for sure."
    a "Hehe..."
    scene 46-7 shoot 19 with Dissolve(0.5)
    j2 "Just keep that little tip in mind."
    m2 "Thanks, Jeff."
    a "Soo... We're ready."
    scene 46-7 shoot 20 with Dissolve(0.5)
    m2 "Whoa..."
    j2 "You definitely are, ladies."
    j2 "You look ready to party."
    a "We don't know the story, really."
    j2 "No problem, Dilan will explain the scene when we get there."
    j2 "Not much acting there."
    scene 46-7 shoot 21-1 with Dissolve(0.5)
    j2 "{i}...This girl... is... Wow...{/i}"
    j2 "{i}...This is crazy, They both compliment each other...{/i}"
    scene 46-7 shoot 21 with Dissolve(0.5)
    j2 "I've got a good feeling about today's shoot."
    r2 "Really?"
    j2 "Yeah. You guys are gonna do great."
    j2 "Always happy to see new faces in the industry."
    scene 46-7 shoot 22 with Dissolve(0.5)
    d3 "Wonderful, Wonderful!"
    d3 "You girls look fantastic."
    a "You never miss, Dilan."
    d3 "Can't agree more."
    scene 46-7 shoot 23 with Dissolve(0.5)
    d3 "Alright, I'm all done."
    d3 "We can head to the location."
    d3 "Whenever you are all ready."
    a "Let's go then."
    scene black with Dissolve(0.5)
    pause 1
    play sound car_sound1
    pause 1
    play music sideroad
    scene 46-7 shoot 25 with Dissolve(0.5)
    d3 "Alright. This is the location."
    d3 "A Nice nightclub."
    d3 "I've rented it out for a few hours, we should have enough time to shoot the scene."
    scene 46-7 shoot 26 with Dissolve(0.5)
    d3 "Now. I'll need the help of Jeff and Michael to carry the gear in here."
    m2 "Whatever you need, Dilan."
    d3 "Great."
    scene 46-7 shoot 27 with Dissolve(0.5)
    d3 "You girls can just go settle in."
    d3 "Get some drinks, relax a bit, prep for the scene."
    d3 "The owner is also in, you can go greet him, and talk a bit."
    a "Sure."
    d3 "Great. we'll be right back."
    scene 46-7 shoot 29 with Dissolve(0.5)
    r1 "Pretty accommodating, aren't they?"
    a "Sure are."
    a "Dilan usually works alone, but he has a lot of contacts."
    a "He can usually set things up nicely."
    a "So, Drinks?"
    r1 "Absolutely."
    scene 46-7 shoot 30 with Dissolve(0.5)
    co1 "Hello, ladies, and welcome."
    co1 "I am Horace. The owner of this club."
    a "Hello."
    r1 "Hi."
    co1 "Please. get comfortable."
    scene 46-7 shoot 31-1 with Dissolve(0.5)
    barten "{i}...Damn... Those girls got some damn nice knockers...{/i}"
    scene 46-7 shoot 31 with Dissolve(0.5)
    r1 "Dilan said we could get some drinks here?"
    barten "Of course, whatever you'd like."
    a "Oh... Great!"
    a "We'll both have Rum cola, please."
    scene 46-7 shoot 32 with Dissolve(0.5)
    co1 "Ha. A classic. Nothing helps better than a Rum cola."
    co1 "We're happy to help any way we can."
    r1 "Thank you, Heh."
    scene 46-7 shoot 33 with Dissolve(0.5)
    barten "Here you go."
    barten "Two rum colas."
    a "Nice!"
    scene 46-7 shoot 34 with Dissolve(0.5)
    co1 "So how are you guys feeling?"
    r1 "A bit nervous. Excited. All kinds of things."
    co1 "Great, great!"
    play sound drinkingBeverage
    scene 46-7 shoot 35 with Dissolve(0.5)
    pause 1
    play sound surprise2
    scene 46-7 shoot 36 with Dissolve(0.5)
    d3 "Whoa... Too bright, too bright..."
    m2 "Fuck, I don't know how to work these things..."
    d3 "All good. Just giving you pointers."
    d3 "You'll get the hang of it."
    scene 46-7 shoot 37 with Dissolve(0.5)
    d3 "Just lower the intensity and that's it."
    d3 "We don't want to over expose the subjects."
    m2 "What?"
    d3 "Never mind, just dim the lights slightly."
    m2 "Alright."
    scene 46-7 shoot 38 with Dissolve(0.5)
    d3 "So, girls."
    d3 "You good?"
    d3 "Drinks tasty?"
    a "Yeah. all good!"
    scene 46-7 shoot 39 with Dissolve(0.5)
    d3 "Ok, so..."
    d3 "There ain't much of a story here."
    d3 "But the general idea is this."
    d3 "You are two friends who have a party later."
    d3 "You decided to pre-game at a bar near the party place."
    d3 "You come in, get some drinks, meet some strangers."
    d3 "You'll get a bit drunk and turned on by the strangers."
    d3 "Then you'll 'seduce' them and get the freak on."
    d3 "Got it?"
    a "Yeah, should be good."
    d3 "Great, get into position."
    scene 46-7 shoot 40 with Dissolve(0.5)
    d3 "Alright. You guys ready?"
    a "We are."
    r1 "Ready."
    d3 "GREAT!"
    d3 "We're about to commence filming. Silence, phones off."
    scene 46-7 shoot 41 with Dissolve(0.5)
    d3 "Three..."
    d3 "Two..."
    d3 "One!"
    d3 "ACTION!"
    label EP16_Dilan_Sex_Scene:
    $ persistent.scene_49 = True
    play music SexyTimeSong5
    scene 46-7 shoot 42 with flash
    a "So... The party's in like an hour?"
    r1 "Something like that."
    a "I like the idea that we decided to pregame here."
    scene 46-7 shoot 43 with Dissolve(0.5)
    a "Never been here."
    r1 "Heh... Yeah."
    r1 "Let's see what the bar's got."
    scene 46-7 shoot 44 with Dissolve(0.5)
    d3 "Nice..."
    scene 46-7 shoot 45 with Dissolve(0.5)
    a "Hello."
    r1 "Hi, guys."
    j2 "Well, well..."
    m2 "Hey, ladies."
    scene 46-7 shoot 46 with Dissolve(0.5)
    m2 "What are girls like you doing in this part of the town?"
    a "Heh... Well... Just having fun."
    r2 "Just warming up before our party."
    m2 "Nice."
    m2 "Perhaps we can get you some drinks?"
    a "Oh, sure."
    scene 46-7 shoot 47 with Dissolve(0.5)
    barten "So. What can I get ya?"
    r1 "Oh... Umm..."
    r1 "Sex on the beach please?"
    barten "Will our special work?"
    barten "It's an alternate version of the drink."
    r1 "Sure!"
    m2 "Put that on our tab."
    barten "Will do!"
    scene 46-7 shoot 48 with Dissolve(0.5)
    barten "Here you go."
    a "Thank you, heh..."
    scene 46-7 shoot 49 with Dissolve(0.5)
    a "This night's going to be awesome!"
    r1 "Yeah!"
    j2 "No doubt about that. Hehe..."
    scene 46-7 shoot 50 with Dissolve(0.5)
    m2 "So..."
    m2 "You look good."
    a "Thank you, sir."
    a "You are pretty handsome yourself."
    play sound drinkingBeverage
    scene 46-7 shoot 51 with Dissolve(0.5)
    pause 1
    scene 46-7 shoot 52 with Dissolve(0.5)
    d3 "Cut!"
    d3 "Guys..."
    d3 "A bit too stiff..."
    d3 "Relax, it's all good. Remember. We ain't trying to capture an Oscar-worthy performance."
    scene 46-7 shoot 53 with Dissolve(0.5)
    d3 "Just look natural enough... I bet you are all looking forward to what's coming, ye?"
    d3 "Just enjoy it."
    d3 "Alright! Action!"
    scene 46-7 shoot 54 with flash
    r1 "Hehe... This is fun."
    a "Yeah! I'm getting tipsy... Heh..."
    scene black with Dissolve(0.5)
    "A few drinks later."
    scene 46-7 shoot 55 with Dissolve(0.5)
    a "I think, maybe we should get going. Meet with our friends."
    r1 "Whaat?"
    r1 "We still got time."
    r1 "I've got an idea."
    a "Oh?"
    scene 46-7 shoot 56 with Dissolve(0.5)
    r1 "Come with me."
    a "Where are you taking me?"
    r1 "Just... relax."
    scene 46-7 shoot 57 with Dissolve(0.5)
    r1 "I really like these guys... And... I'm kinda drunk..."
    r1 "You know what happens when I get drunk..."
    a "Oh... Hehe..."
    a "I know, I know..."
    scene 46-7 shoot 58 with Dissolve(0.5)
    r1 "Let's... Seduce them..."
    r1 "Let's dance and invite them to do it with us..."
    a "I wouldn't say no to some black cock... Hehe..."
    scene 46-7 shoot 59 with Dissolve(0.5)
    r1 "Good girl."
    r1 "I knew you wouldn't disagree with your older, more experienced friend, hehe..."
    scene 46-7 shoot 60 with Dissolve(0.5)
    m2 "Whoa."
    j2 "Niiice... Girls getting turned up!"
    scene 46-7 shoot 61 with Dissolve(0.5)
    a "Oh... Yeah!"
    a "This feels great!"
    scene 46-7 shoot 62 with Dissolve(0.5)
    pause 1
    scene 46-7 shoot 63 with Dissolve(0.5)
    a "You like being naughty, don't you."
    r1 "You know it. Haha!"
    scene 46-7 shoot 64 with Dissolve(0.5)
    j2 "Daamn..."
    m2 "This is great!"
    a "So... What are you waiting for boys? Come here."
    scene 46-7 shoot 65 with Dissolve(0.5)
    m2 "Did they just... For real?"
    j2 "Damn straight, man."
    j2 "Let's give the girls what they askin' for."
    scene 46-7 shoot 66 with Dissolve(0.5)
    pause 1
    scene 46-7 shoot 67 with Dissolve(0.5)
    a "Oh..."
    m2 "Yeah..."
    j2 "You like it when we touch you."
    r1 "Mhm..."
    scene 46-7 shoot 68 with Dissolve(0.5)
    m2 "You're damn hot, girl."
    a "I know... Keep those compliments coming."
    m2 "I wanna do some dirty things to you, girl."
    a "Mhmmm..."
    scene 46-7 shoot 69 with Dissolve(0.5)
    d3 "{i}...AWESOME!! THEY GOT THE IDEA!!!{/i}"
    scene 46-7 shoot 70 with Dissolve(0.5)
    r1 "You got some moves, sir."
    j2 "Being old comes with experience."
    j2 "Not only with dancing, if you know what I mean, heh."
    r1 "Can't wait to find out..."
    scene 46-7 shoot 71 with Dissolve(0.5)
    "The dance was unraveling..."
    "The tension was building... They all couldn't wait for the main course."
    d3 "{i}...So hot...{/i}"
    scene 46-7 shoot 72 with Dissolve(0.5)
    "The man started to touch the girls more and more..."
    "And that's exactly what they wanted..."
    "To be handled by bulls like them."
    scene 46-7 shoot 73 with Dissolve(0.5)
    a "Mm... You're so hot... Sir..."
    a "What's your name?"
    m2 "Michael."
    a "Oh, Michael... I want you to do things to me."
    m2 "Do you have a boyfriend?"
    a "Well, yeah. I have, but he's not here, is he?"
    scene 46-7 shoot 74 with Dissolve(0.5)
    r1 "Ah..."
    r1 "Keep doing that."
    j2 "Oh yeah, I had no plan of stopping."
    r1 "Mhmm..."
    play sound undress
    scene 46-7 shoot 75 with Dissolve(0.5)
    "They were getting more and more handsy."
    "The girls were getting more and more turned on."
    "Starting to crave the cock."
    scene 46-7 shoot 76 with Dissolve(0.5)
    a "Oh... Hehe..."
    a "You got some strong hands, Michael."
    m2 "Thanks... You got the nicest, softest body ever."
    play sound cloth_sound1
    scene 46-7 shoot 77 with Dissolve(0.5)
    pause 1
    scene 46-7 shoot 78 with Dissolve(0.5)
    pause 1
    scene 46-7 shoot 79 with Dissolve(0.5)
    r1 "Oh..."
    j2 "Tell me if you'd like me to stop..."
    r1 "Don't stop..."
    scene 46-7 shoot 80 with Dissolve(0.5)
    "Both girls felt lust building in them..."
    "It was just two girls having fun..."
    scene 46-7 shoot 82 with Dissolve(0.5)
    a "Mm..."
    a "Touch me all over, Michael."
    m2 "Fuck, you might be the hottest girl ever."
    a "Ahh..."
    scene 46-7 shoot 83 with Dissolve(0.5)
    m2 "Damn, those titties."
    a "You like 'em?"
    m2 "Fuck yeah... So round, so squishy."
    scene 46-7 shoot 84 with Dissolve(0.5)
    m2 "How about I loosen up that dress."
    a "Ahh... Go ahead."
    a "Unveil my naked body."
    play sound jerk
    scene 46-7 shoot 85 with Dissolve(0.5)
    r1 "Ahh..."
    scene 46-7 shoot 86 with Dissolve(0.5)
    j2 "Oh... That pussy wet."
    j2 "I can feel it."
    r1 "So you see what you're doing to me."
    j2 "Oh yeah..."
    play sound undress
    scene 46-7 shoot 87 with Dissolve(0.5)
    m2 "Whoops..."
    a "Ah... Do you like what you see?"
    m2 "Fuck, you're so hot!"
    scene 46-7 shoot 88 with Dissolve(0.5)
    a "Keep telling me those things..."
    a "I don't get enough compliments at home..."
    m2 "Girl, I'll give that hot sexy ass the time of its life..."
    m2 "I'll lick those titties so good, you gon moan from pleasure."
    scene 46-7 shoot 89 with Dissolve(0.5)
    a "Ahh..."
    a "I can't wait anymore..."
    a "I need something in my mouth."
    scene 46-7 shoot 90 with Dissolve(0.5)
    j2 "Well, well... Looks like your friend's a nasty one."
    j2 "I wonder, are you like that too?"
    scene 46-7 shoot 91 with Dissolve(0.5)
    r1 "How about we find out?"
    j2 "Read my mind."
    play sound undress
    scene 46-7 shoot 92 with Dissolve(0.5)
    pause 1
    play sound cloth_sound1
    scene 46-7 shoot 93 with Dissolve(0.5)
    j2 "Hehe... I never doubted you."
    r1 "You like what you see?"
    j2 "I can barely believe it..."
    j2 "You are one fucking hot chick."
    scene 46-7 shoot 94 with Dissolve(0.5)
    d3 "{i}...Fucking awesome...{/i}"
    scene 46-7 shoot 95 with Dissolve(0.5)
    d3 "Go sit at the tables..."
    d3 "Do some fun stuff there..."
    scene 46-7 shoot 96 with Dissolve(0.5)
    m2 "Come... I want you to meet someone."
    a "Uuu... I wonder who it is?"
    m2 "A friend of mine, heh."
    play sound undress
    scene 46-7 shoot 97 with Dissolve(0.5)
    m2 "Damn girl... My cock is throbbing for that pussy."
    m2 "But first... I wanna feel that mouth all over my cock."
    a "I want you to fuck my face, Michael..."
    m2 "Damn straight."
    play sound jacketcloth
    scene 46-7 shoot 98 with Dissolve(0.5)
    pause 1
    play sound undress
    scene 46-7 shoot 99 with Dissolve(0.5)
    pause 1
    scene 46-7 shoot 100 with Dissolve(0.5)
    r1 "Wooow..."
    a "That's... So big..."
    a "Damn these cocks..."
    scene 46-7 shoot 101 with Dissolve(0.5)
    a "I want it so bad..."
    m2 "Fuck yeah!"
    r1 "I can't hold myself back any longer."
    j2 "It's all yours, baby."
    scene 46-7 shoot 102 with Dissolve(0.5)
    a "That's such a nice cock..."
    m2 "I know..."
    m2 "Now. Give me what we both want."
    scene 46-7 shoot 103 with Dissolve(0.5)
    r1 "Oh... Fuck... I'm so excited..."
    $ different_choice_menu = True
    $ EP16_Anim_Option = 1
    $ EP16_Anim_Speed = 1
    scene black
    show Ep16_Dilan_Anim_1 with Dissolve(0.5)
    play sound jerk2 loop
    label EP16_Dilan_Handjob_1_label:
        a "Mm..."
        r1 "That's one nice cock..."
        r1 "Fuck... Have to put it in as soon as possible."
        menu EP16_Dilan_Handjob_1_Menu:
            "View 1":
                hide Ep16_Dilan_Anim_1
                hide Ep16_Dilan_Anim_1_Faster
                hide Ep16_Dilan_Anim_2
                hide Ep16_Dilan_Anim_2_Faster
                if EP16_Anim_Speed == 1:
                    show Ep16_Dilan_Anim_1 with Dissolve(0.5)
                if EP16_Anim_Speed == 2:
                    show Ep16_Dilan_Anim_1_Faster with Dissolve(0.5)
                $ EP16_Anim_Option = 1
                jump EP16_Dilan_Handjob_1_Menu
            "View 2":
                hide Ep16_Dilan_Anim_1
                hide Ep16_Dilan_Anim_1_Faster
                hide Ep16_Dilan_Anim_2
                hide Ep16_Dilan_Anim_2_Faster
                $ EP16_Anim_Option = 2
                if EP16_Anim_Speed == 1:
                    show Ep16_Dilan_Anim_2 with Dissolve(0.5)
                if EP16_Anim_Speed == 2:
                    show Ep16_Dilan_Anim_2_Faster with Dissolve(0.5)
                jump EP16_Dilan_Handjob_1_Menu
            "Slower":
                hide Ep16_Dilan_Anim_1
                hide Ep16_Dilan_Anim_1_Faster
                hide Ep16_Dilan_Anim_2
                hide Ep16_Dilan_Anim_2_Faster
                $ EP16_Anim_Speed = 1
                if EP16_Anim_Option == 1:
                    show Ep16_Dilan_Anim_1 with Dissolve(0.5)
                if EP16_Anim_Option == 2:
                    show Ep16_Dilan_Anim_2 with Dissolve(0.5)
                jump EP16_Dilan_Handjob_1_Menu
            "Faster":
                hide Ep16_Dilan_Anim_1
                hide Ep16_Dilan_Anim_1_Faster
                hide Ep16_Dilan_Anim_2
                hide Ep16_Dilan_Anim_2_Faster
                $ EP16_Anim_Speed = 2
                if EP16_Anim_Option == 1:
                    show Ep16_Dilan_Anim_1_Faster with Dissolve(0.5)
                if EP16_Anim_Option == 2:
                    show Ep16_Dilan_Anim_2_Faster with Dissolve(0.5)
                jump EP16_Dilan_Handjob_1_Menu
            "Continue":
                hide Ep16_Dilan_Anim_1
                hide Ep16_Dilan_Anim_1_Faster
                hide Ep16_Dilan_Anim_2
                hide Ep16_Dilan_Anim_2_Faster
                $ different_choice_menu = False
                stop sound
                pass
    scene 46-7 shoot 104 with Dissolve(0.5)
    "Anna was closing in on his cock with her lips."
    "Couldn't wait a moment longer... She craved Michaels dick inside of her."
    a "Mmm..."
    play sound jerk
    scene 46-7 shoot 105 with Dissolve(0.5)
    a "Oh..."
    a "Ahh..."
    m2 "Oh fuck..."
    m2 "That's some good mouth right there."
    scene 46-7 shoot 106 with Dissolve(0.5)
    a "MMmm..."
    m2 "Shiiiet... Girl..."
    "Anna was slurping on that cock like no tomorrow."
    scene 46-7 shoot 107 with Dissolve(0.5)
    "Rebecca saw it all and got a little jealous..."
    scene 46-7 shoot 108 with Dissolve(0.5)
    "But... She'd return the favor on Jeff's schlong."
    r1 "{i}...Oh, Jeff's gonna love this...{/i}"
    r1 "Nice work... Anna... Heh... You've got some skills..."
    scene 46-7 shoot 109 with Dissolve(0.5)
    "Rebecca lowered her face onto Jeff's penis."
    "And started to suck away..."
    "Jeff was about to get some of that famous Rebecca's mouth love."
    play sound jerk3
    scene 46-7 shoot 110 with Dissolve(0.5)
    r1 "AAHHHHH."
    r1 "KHaaa..."
    "Rebecca went deep on that cock."
    j2 "OH FUUCK!"
    $ different_choice_menu = True
    $ EP16_Anim_Option = 1
    $ EP16_Anim_Speed = 1
    scene black
    show Ep16_Dilan_Anim_3 with Dissolve(0.5)
    play sound jerk2 loop
    label EP16_Dilan_Blowjob_1_label:
        r1 "KHaaaaa..."
        a "Aahhhh..."
        menu EP16_Dilan_Blowjob_1_Menu:
            "View 1":
                hide Ep16_Dilan_Anim_3
                hide Ep16_Dilan_Anim_3_Faster
                hide Ep16_Dilan_Anim_4
                hide Ep16_Dilan_Anim_4_Faster
                if EP16_Anim_Speed == 1:
                    show Ep16_Dilan_Anim_3 with Dissolve(0.5)
                if EP16_Anim_Speed == 2:
                    show Ep16_Dilan_Anim_3_Faster with Dissolve(0.5)
                $ EP16_Anim_Option = 1
                jump EP16_Dilan_Blowjob_1_Menu
            "View 2":
                hide Ep16_Dilan_Anim_3
                hide Ep16_Dilan_Anim_3_Faster
                hide Ep16_Dilan_Anim_4
                hide Ep16_Dilan_Anim_4_Faster
                $ EP16_Anim_Option = 2
                if EP16_Anim_Speed == 1:
                    show Ep16_Dilan_Anim_4 with Dissolve(0.5)
                if EP16_Anim_Speed == 2:
                    show Ep16_Dilan_Anim_4_Faster with Dissolve(0.5)
                jump EP16_Dilan_Blowjob_1_Menu
            "Slower":
                hide Ep16_Dilan_Anim_3
                hide Ep16_Dilan_Anim_3_Faster
                hide Ep16_Dilan_Anim_4
                hide Ep16_Dilan_Anim_4_Faster
                $ EP16_Anim_Speed = 1
                if EP16_Anim_Option == 1:
                    show Ep16_Dilan_Anim_3 with Dissolve(0.5)
                if EP16_Anim_Option == 2:
                    show Ep16_Dilan_Anim_4 with Dissolve(0.5)
                jump EP16_Dilan_Blowjob_1_Menu
            "Faster":
                hide Ep16_Dilan_Anim_3
                hide Ep16_Dilan_Anim_3_Faster
                hide Ep16_Dilan_Anim_4
                hide Ep16_Dilan_Anim_4_Faster
                $ EP16_Anim_Speed = 2
                if EP16_Anim_Option == 1:
                    show Ep16_Dilan_Anim_3_Faster with Dissolve(0.5)
                if EP16_Anim_Option == 2:
                    show Ep16_Dilan_Anim_4_Faster with Dissolve(0.5)
                jump EP16_Dilan_Blowjob_1_Menu
            "Continue":
                hide Ep16_Dilan_Anim_3
                hide Ep16_Dilan_Anim_3_Faster
                hide Ep16_Dilan_Anim_4
                hide Ep16_Dilan_Anim_4_Faster
                $ different_choice_menu = False
                stop sound
                pass
    scene 46-7 shoot 111 with Dissolve(0.5)
    "The owner and bartender looked at them... Wishing they could join..."
    co1 "Damn. They really are going at it."
    co1 "Those sluts were so fucking hot."
    barten "Yes, sir. Have to agree..."
    barten "Don't really see that many hot girls around."
    scene 46-7 shoot 112 with Dissolve(0.5)
    d3 "Magnificent shots..."
    d3 "{i}...These girls are naturals...{/i}"
    d3 "{i}...Born to be used for sex...{/i}"
    scene 46-7 shoot 113 with Dissolve(0.5)
    r1 "Heh... How about you two get undressed and give us the fucking of a lifetime."
    m2 "Don't have to say twice."
    j2 "Oh Yeah..."
    a "Can't wait to get fucked... Oh... I'm so aroused right now..."
    scene 46-7 shoot 114 with Dissolve(0.5)
    j2 "Come here..."
    j2 "Turn around, girl."
    play sound cloth_sound1
    scene 46-7 shoot 115 with Dissolve(0.5)
    m2 "Fuck me..."
    m2 "Those asses..."
    j2 "I wanna pound them so bad..."
    m2 "Fuck yeah."
    scene 46-7 shoot 116 with Dissolve(0.5)
    a "Come on... Please don't make us wait."
    r1 "We want them so bad right now..."
    play sound female_moan_5
    play audio jerk2
    scene 46-7 shoot 117 with Dissolve(0.5)
    a "AAHHH!!!"
    a "OH FUCK!"
    a "Just like that!"
    r1 "AAHHH!!!!"
    scene 46-7 shoot 118 with Dissolve(0.5)
    "Their pussies were so wet, that the entry was effortless."
    scene 46-7 shoot 119 with Dissolve(0.5)
    a "Ah... Michael..."
    "Rebecca was a bit jealous. But she didn't protest."
    "Just looked at Anna and her pleasureful emotions."
    scene 46-7 shoot 120 with Dissolve(0.5)
    "As soon as Jeff entered Rebecca, her anticipation evolved into satisfaction."
    "Getting drilled by the black cocks, the girls only thought of one thing. The pleasure."
    play audio femgasp_1
    $ different_choice_menu = True
    $ EP16_Anim_Option = 1
    $ EP16_Anim_Speed = 1
    scene black
    show Ep16_Dilan_Anim_6 with Dissolve(0.5)
    play sound jerk2 loop
    label EP16_Dilan_Sex_1_label:
        r1 "Oh... Ahh..."
        r1 "Push it in me!!!"
        a "Yeah! Give it all to me!"
        play audio moaningthree
        menu EP16_Dilan_Sex_1_Menu:
            "View 1":
                hide Ep16_Dilan_Anim_6
                hide Ep16_Dilan_Anim_6_Faster
                hide Ep16_Dilan_Anim_7
                hide Ep16_Dilan_Anim_7_Faster
                if EP16_Anim_Speed == 1:
                    show Ep16_Dilan_Anim_6 with Dissolve(0.5)
                if EP16_Anim_Speed == 2:
                    show Ep16_Dilan_Anim_6_Faster with Dissolve(0.5)
                $ EP16_Anim_Option = 1
                jump EP16_Dilan_Sex_1_Menu
            "View 2":
                hide Ep16_Dilan_Anim_6
                hide Ep16_Dilan_Anim_6_Faster
                hide Ep16_Dilan_Anim_7
                hide Ep16_Dilan_Anim_7_Faster
                $ EP16_Anim_Option = 2
                if EP16_Anim_Speed == 1:
                    show Ep16_Dilan_Anim_7 with Dissolve(0.5)
                if EP16_Anim_Speed == 2:
                    show Ep16_Dilan_Anim_7_Faster with Dissolve(0.5)
                jump EP16_Dilan_Sex_1_Menu
            "Slower":
                hide Ep16_Dilan_Anim_6
                hide Ep16_Dilan_Anim_6_Faster
                hide Ep16_Dilan_Anim_7
                hide Ep16_Dilan_Anim_7_Faster
                $ EP16_Anim_Speed = 1
                if EP16_Anim_Option == 1:
                    show Ep16_Dilan_Anim_6 with Dissolve(0.5)
                if EP16_Anim_Option == 2:
                    show Ep16_Dilan_Anim_7 with Dissolve(0.5)
                jump EP16_Dilan_Sex_1_Menu
            "Faster":
                hide Ep16_Dilan_Anim_6
                hide Ep16_Dilan_Anim_6_Faster
                hide Ep16_Dilan_Anim_7
                hide Ep16_Dilan_Anim_7_Faster
                $ EP16_Anim_Speed = 2
                if EP16_Anim_Option == 1:
                    show Ep16_Dilan_Anim_6_Faster with Dissolve(0.5)
                if EP16_Anim_Option == 2:
                    show Ep16_Dilan_Anim_7_Faster with Dissolve(0.5)
                jump EP16_Dilan_Sex_1_Menu
            "Continue":
                hide Ep16_Dilan_Anim_6
                hide Ep16_Dilan_Anim_6_Faster
                hide Ep16_Dilan_Anim_7
                hide Ep16_Dilan_Anim_7_Faster
                $ different_choice_menu = False
                stop sound
                pass
    scene 46-7 shoot 121 with Dissolve(0.5)
    r1 "Ah!"
    a "AHH!"
    a "Yeah!"
    m2 "Dammn..."
    j2 "Fuck yeah."
    scene 46-7 shoot 122 with Dissolve(0.5)
    a "This is great!"
    r1 "Is Michael fucking you good, sis?"
    a "Oh..."
    scene 46-7 shoot 123 with Dissolve(0.5)
    co1 "Damn, those girls are quite impressive."
    barten "Indeed."
    co1 "They seem to enjoy getting fucked. That's for sure."
    play sound female_moan_4
    scene 46-7 shoot 125 with Dissolve(0.5)
    r1 "Harder, Jeff..."
    r1 "Your cock is filling me up so GOOD!"
    j2 "You are one sexy lady!"
    scene 46-7 shoot 126 with Dissolve(0.5)
    a "OH!"
    r1 "Ah!"
    "They were all moaning. The room echoed with gasps and pleasured screams."
    "Depravities were unleashed..."
    play sound female_moan_1
    scene 46-7 shoot 127 with Dissolve(0.5)
    r1 "OOhh... Yeah..."
    r1 "You like those titties, don't you."
    r1 "Let me smother you with them."
    j2 "MMmmm..."
    play sound female_moan_2
    scene 46-7 shoot 128 with Dissolve(0.5)
    a "Oh... Michael..."
    m2 "Anna... So hot..."
    a "You like when Rebecca is getting fucked by someone else?"
    m2 "Fuuuck..."
    play audio female_moan_4
    play sound jerk2 loop
    scene 46-7 shoot 129 with Dissolve(0.5)
    "They were as horny as ever..."
    "The dirty talk made the feel even more turned on and they indulged their fantasies..."
    scene 46-7 shoot 130 with Dissolve(0.5)
    a "AH!"
    r1 "FUCK!"
    j2 "That pussy... DAMN!"
    scene 46-7 shoot 131 with Dissolve(0.5)
    j2 "AH SHIET!"
    r1 "Yeah. I bet you're going crazy from that pussy... Yeah?"
    j2 "Fuck yeah, girl."
    play audio moaningtwo
    scene 46-7 shoot 132 with Dissolve(0.5)
    "Their bodies sweaty from the ordeal..."
    "Juices flowing out of the orifices..."
    "Not a care in the world..."
    "Not even acting, just enjoying the activity."
    $ different_choice_menu = True
    $ EP16_Anim_Option = 1
    $ EP16_Anim_Speed = 1
    scene black
    show Ep16_Dilan_Anim_8 with Dissolve(0.5)
    play sound jerk2 loop
    label EP16_Dilan_Sex_2_label:
        r1 "You like it when we ride you?"
        a "Using your cocks for our pussies..."
        play audio moaningthree
        menu EP16_Dilan_Sex_2_Menu:
            "View 1":
                hide Ep16_Dilan_Anim_8
                hide Ep16_Dilan_Anim_8_Faster
                hide Ep16_Dilan_Anim_9
                hide Ep16_Dilan_Anim_9_Faster
                if EP16_Anim_Speed == 1:
                    show Ep16_Dilan_Anim_8 with Dissolve(0.5)
                if EP16_Anim_Speed == 2:
                    show Ep16_Dilan_Anim_8_Faster with Dissolve(0.5)
                $ EP16_Anim_Option = 1
                jump EP16_Dilan_Sex_2_Menu
            "View 2":
                hide Ep16_Dilan_Anim_8
                hide Ep16_Dilan_Anim_8_Faster
                hide Ep16_Dilan_Anim_9
                hide Ep16_Dilan_Anim_9_Faster
                $ EP16_Anim_Option = 2
                if EP16_Anim_Speed == 1:
                    show Ep16_Dilan_Anim_9 with Dissolve(0.5)
                if EP16_Anim_Speed == 2:
                    show Ep16_Dilan_Anim_9_Faster with Dissolve(0.5)
                jump EP16_Dilan_Sex_2_Menu
            "Slower":
                hide Ep16_Dilan_Anim_8
                hide Ep16_Dilan_Anim_8_Faster
                hide Ep16_Dilan_Anim_9
                hide Ep16_Dilan_Anim_9_Faster
                $ EP16_Anim_Speed = 1
                if EP16_Anim_Option == 1:
                    show Ep16_Dilan_Anim_8 with Dissolve(0.5)
                if EP16_Anim_Option == 2:
                    show Ep16_Dilan_Anim_9 with Dissolve(0.5)
                jump EP16_Dilan_Sex_2_Menu
            "Faster":
                hide Ep16_Dilan_Anim_8
                hide Ep16_Dilan_Anim_8_Faster
                hide Ep16_Dilan_Anim_9
                hide Ep16_Dilan_Anim_9_Faster
                $ EP16_Anim_Speed = 2
                if EP16_Anim_Option == 1:
                    show Ep16_Dilan_Anim_8_Faster with Dissolve(0.5)
                if EP16_Anim_Option == 2:
                    show Ep16_Dilan_Anim_9_Faster with Dissolve(0.5)
                jump EP16_Dilan_Sex_2_Menu
            "Continue":
                hide Ep16_Dilan_Anim_8
                hide Ep16_Dilan_Anim_8_Faster
                hide Ep16_Dilan_Anim_9
                hide Ep16_Dilan_Anim_9_Faster
                $ different_choice_menu = False
                stop sound
                pass
    scene 46-7 shoot 133 with Dissolve(0.5)
    a "AHh.. Fuck..."
    m2 "I'm... Can't even speak... Damn some good pussy this."
    play audio moaningone
    scene 46-7 shoot 134 with Dissolve(0.5)
    "Anna was riding Michaels cock as hard as possible."
    "He was barely holding in."
    scene 46-7 shoot 135 with Dissolve(0.5)
    "Neither woman was slowing down."
    "Neither guy wanted to cum yet."
    "They all loved the sensation."
    play audio moaningfive
    scene 46-7 shoot 136 with Dissolve(0.5)
    r1 "OOHH!!"
    r1 "AHHHH."
    r1 "JEFF!"
    scene 46-7 shoot 137 with Dissolve(0.5)
    j2 "I want you to lay on your back."
    j2 "I wanna fuck you real good and real deep."
    r1 "OH, Jeff..."
    play audio MoaningNine
    scene 46-7 shoot 138 with Dissolve(0.5)
    r1 "AAH!!"
    r1 "SO DEEP!"
    j2 "FUCK... This is GOOD!"
    scene 46-7 shoot 139 with Dissolve(0.5)
    m2 "Lemme switch you up too, Anna."
    a "AHHH!"
    a "Whatever you do, just keep fucking me!"
    scene 46-7 shoot 140 with Dissolve(0.5)
    a "OOHHHH!!"
    a "YEAH!"
    m2 "I'm Going DEEP!"
    a "YES! YES!"
    scene 46-7 shoot 141 with Dissolve(0.5)
    j2 "Imma give you something to remember."
    r1 "Fuck me deeper?"
    j2 "Hehe..."
    play audio femgasp
    scene 46-7 shoot 142 with Dissolve(0.5)
    r1 "AAAAHHHHH!!!"
    "Rebecca was flooded with pleasure..."
    scene 46-7 shoot 143 with Dissolve(0.5)
    "So was Anna."
    "And the two gentlemen."
    "Just helping out two damsels."
    play audio female_moan_4
    scene 46-7 shoot 144 with Dissolve(0.5)
    r1 "So good... Anna..."
    a "Oh...... Fuck... They are fucking us so good..."
    "The two hot friends... Depraved as ever..."
    play audio female_moan_5
    scene 46-7 shoot 145 with Dissolve(0.5)
    m2 "Fuck... I'm coming!"
    j2 "Yeah! So am I!"
    j2 "AAHH!!"
    m2 "AAHHH!!"
    $ different_choice_menu = True
    $ EP16_Anim_Option = 1
    $ EP16_Anim_Speed = 1
    scene black
    show Ep16_Dilan_Anim_5 with Dissolve(0.5)
    label EP16_Dilan_Sex_3_Label:
        play sound jerk3 loop
        a "Oh... Fuck..."
        r1 "I'm getting so close..."
        j2 "Yeah... Me too... Fuck..."
        m2 "Ahh... Anna, I can't hold it any longer..."
        menu EP16_Dilan_Sex_3_Menu:
            "View 1":
                hide Ep16_Dilan_Anim_5
                hide Ep16_Dilan_Anim_5_Faster
                $ EP16_Anim_Option = 1
                show Ep16_Dilan_Anim_5 with Dissolve(0.5)
                jump EP16_Dilan_Sex_3_Menu
            "Slower":
                hide Ep16_Dilan_Anim_5
                hide Ep16_Dilan_Anim_5_Faster
                $ EP16_Anim_Speed = 1
                show Ep16_Dilan_Anim_5 with Dissolve(0.5)
                jump EP16_Dilan_Sex_3_Menu
            "Faster":
                hide Ep16_Dilan_Anim_5
                hide Ep16_Dilan_Anim_5_Faster
                $ EP16_Anim_Speed = 2
                show Ep16_Dilan_Anim_5_Faster with Dissolve(0.5)
                jump EP16_Dilan_Sex_3_Menu
            "Continue":
                $ different_choice_menu = False
                stop sound
                pass
    play audio moaninglong_1
    menu:
        "Finish inside of the girls.":
            a "Fill me up, Michael!"
            r1 "Don't you dare pull out, Jeff!"
            play audio cum_sound
            scene 46-7 shoot 146 with Dissolve(0.5)
            hide Ep16_Dilan_Anim_5
            hide Ep16_Dilan_Anim_5_Faster
            a "AAHHHAAAHHHAAA!!"
            with flash
            with flash
            a "OH AHH!!"
            m2 "TAKE MY SEEED!"
            with flash
            a "AAH!!"
            m2 "FUCK!"
            with flash
            play audio cum_sound
            scene 46-7 shoot 153 with Dissolve(0.5)
            j2 "Im filling you up!!!"
            with flash
            r1 "PLEASE, PLEASE PLEASE!!!!"
            r1 "AAHHHHAAAAAA!!!!!!"
            with flash
            with flash
            scene 46-7 shoot 152 with Dissolve(0.5)
            m2 "Damn..."
            m2 "I think I pumped all that I've got in you."
            a "I feel it..."
            scene 46-7 shoot 154 with Dissolve(0.5)
            j2 "One of the best fucks I've had."
            r1 "I noticed you enjoyed yourself... Heh..."
            scene 46-7 shoot 155 with Dissolve(0.5)
            r1 "You good?"
            a "Oh, never better..."
            r1 "Me too... Damn..."
            scene 46-7 shoot 156 with Dissolve(0.5)
            r1 "Are all porn shoots this fun?"
            a "I'd say so, yeah. Heh."
            r1 "I think this could be my calling..."
            scene 46-7 shoot 157 with Dissolve(0.5)
            r1 "Oh sweety..."
            a "I'm spent, sheesh..."
            scene 46-7 shoot 158 with Dissolve(0.5)
            m2 "You girls are crazy."
            j2 "Heh. Can't deny that."
        "Finish on the girls.":

            a "Cum on us!!"
            scene 46-7 shoot 146 with Dissolve(0.5)
            hide Ep16_Dilan_Anim_5
            hide Ep16_Dilan_Anim_5_Faster
            with flash
            m2 "Oh, FUCK!"
            with flash
            scene 46-7 shoot 142 with flash_vpunch
            with flash
            j2 "AAHHH!!"
            play audio cum_sound
            scene 46-7 shoot 147 with flash_vpunch
            with flash
            m2 "AHH ANNA!"
            play audio cum_sound
            scene 46-7 shoot 148 with Dissolve(0.5)
            with flash
            with flash
            j2 "OH FUUUCK!"
            with flash
            r1 "Cum all over me!!!!"
            j2 "AHH. YEAH!"
            scene 46-7 shoot 149 with Dissolve(0.5)
            a "Oh..."
            r1 "Ah..."
            "The girls were gasping for air..."
            scene 46-7 shoot 150 with Dissolve(0.5)
            r1 "Hehe..."
            r1 "You look very satisfied..."
            a "You too, sis."
            scene 46-7 shoot 151 with Dissolve(0.5)
            r1 "Oh I am..."
            r1 "Very, very satisfied."
    stop sound
    $ renpy.end_replay()
    scene 46-7 shoot 159 with flash
    d3 "Alright and it's a wrap!"
    d3 "Well done guys. Well done indeed!"
    d3 "This was one exciting pre-party if I've ever been to one."
    d3 "You were natural!"
    d3 "Definitely got the right people for the job."
    scene 46-7 shoot 160 with Dissolve(0.5)
    r1 "Oh, I really enjoyed myself."
    d3 "Hehe... I saw, yes."
    d3 "This scene will be really good."
    d3 "Anyway. guys, you can go clean un and dress up."
    scene black with Dissolve(0.5)
    pause 1
    play sound cloth_sound1
    scene 46-7 shoot 161 with Dissolve(0.5)
    d3 "Well, that's that."
    d3 "Again. Good scene."
    d3 "At first you guys were a little stiff, but when you got to the seats..."
    d3 "And started to do the real deal, all my doubt disappeared."
    d3 "Absolutely beautiful shots."
    scene 46-7 shoot 162 with Dissolve(0.5)
    d3 "Well done, Michael."
    d3 "You got a nice big cock."
    d3 "Just what the industry needs."
    d3 "Still need some work on the poses and stuff, but that's all with experience."
    m2 "Uhh... Thanks."
    scene 46-7 shoot 163 with Dissolve(0.5)
    barten "Thank you guys for coming."
    barten "The owner had to go, but told me to send regards."
    barten "You are welcome here whenever you'd like."
    barten "Drinks on the house."
    a "Wow... Thank you."
    scene 46-7 shoot 164 with Dissolve(0.5)
    a "See you around."
    barten "Have a nice day."
    scene black with Dissolve(0.5)
    play sound car_sound1
    pause 1
    scene 46-7 shoot 166 with Dissolve(0.5)
    r1 "So..."
    r1 "It was really nice working with you, Jeff."
    r1 "You've got some moves I'll tell you that."
    j2 "Years and years of practice."
    r1 "Hehe..."
    scene 46-7 shoot 167 with Dissolve(0.5)
    d3 "I'll get in touch with you guys about the funds."
    d3 "Give me a couple of days. But I've got a good feeling about this scene."
    a "Thanks, Dilan."
    r1 "Thank you deeply, indeed."
    m2 "Thanks, heh."
    a "See you around, guys."
    scene black with Dissolve(3)
label EP16_Ending:
    pause 2
    jump EP17_Begin
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
