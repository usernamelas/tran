label EP15_Begin:
    $ EP15_var_1 = True
    stop music
    show text "{size=+20}Press Space{/size}"
    pause
label EP15_John:
    $ EP15_var_2 = True
    scene 44-7 night 5 with Dissolve(0.5)
    j "Shh..."
    a "MMM!"
    scene 44-7 night 6 with Dissolve(0.5)
    a "What are you doing?"
    a "What's going on?"
    j "Heh... Nothing..."
    scene 44-7 night 7 with Dissolve(0.5)
    j "I'm very high. Hah..."
    a "What?"
    j "Yeah... I smoked some weed with some neighbors..."
    j "So amaazing."
    j "I'm like... Super horny..."
    j "Are you down for, you know..."
    scene 44-7 night 9 with Dissolve(0.5)
    a "What the hell is going on..."
    scene 44-7 night 10 with Dissolve(0.5)
    j "I'm super horny... I can't believe it..."
    a "Must've been some good weed."
    j "Yah..."
    scene 44-7 night 12 with Dissolve(0.5)
    a1 "Oh... Wha..."
    a1 "Somethingamajig..."
    scene 44-7 night 13 with Dissolve(0.5)
    j "I would really appreciate some release in the form of sexual pleasure."
    a "What are you blabbering about."
    a "How much did you smoke?"
    j "Oh... Maybe a couple of puffs. Maybe an entire joint, I don't recall. Hah..."
    play sound undress
    scene 44-7 night 14 with Dissolve(0.5)
    j "Yeah... Just the tip..."
    a "Ugh..."
    a "What the fuck are you doing?"
    scene 44-7 night 15 with Dissolve(0.5)
    a "Are you crazy?"
    j "No..."
    j "Maybe... I'm sooo hard right now..."
    menu:
        "Ok, fine... (If Corruption > 55)" if AnnaCorruption >=55:
            label EP15_John_Sex_Label:
            $ persistent.scene_44 = True
            a "Ok. Just to get you out of here."
            j "Don't worry. I will be quick."
            play music closuresong
            play sound jacketcloth
            scene 44-7 night 17 with Dissolve(0.5)
            j "Oh... That's... Yeah..."
            a "You like that?"
            j "Ohhh... Anna, so sexy."
            $ different_choice_menu = True
            $ EP15_Anim_Option = 1
            $ EP15_Anim_Speed = 1
            $ EP15_John_Anim_Menu_Var_1 = False
            $ EP15_John_Anim_Menu_Var_2 = False
            scene black
            play sound jerk2 loop
            show EP15_John_Anim_3 with Dissolve(0.5)
            label EP15_John_Anim_Menu_1_Label:
            if EP15_John_Anim_Menu_Var_1 == False:
                j "Anna..."
                j "Those hands..."
                a "Hehe..."
                $ EP15_John_Anim_Menu_Var_1 = True
            menu EP15_John_Anim_Menu:
                "View 1":
                    hide EP15_John_Anim_0
                    hide EP15_John_Anim_0_Faster
                    hide EP15_John_Anim_3
                    hide EP15_John_Anim_3_Faster
                    $ EP15_Anim_Option = 1
                    if EP15_Anim_Speed == 1:
                        show EP15_John_Anim_3 with Dissolve(0.5)
                    elif EP15_Anim_Speed == 2:
                        show EP15_John_Anim_3_Faster with Dissolve(0.5)
                    jump EP15_John_Anim_Menu
                "View 2":
                    hide EP15_John_Anim_0
                    hide EP15_John_Anim_0_Faster
                    hide EP15_John_Anim_3
                    hide EP15_John_Anim_3_Faster
                    $ EP15_Anim_Option = 2
                    if EP15_Anim_Speed == 1:
                        show EP15_John_Anim_0 with Dissolve(0.5)
                    elif EP15_Anim_Speed == 2:
                        show EP15_John_Anim_0_Faster with Dissolve(0.5)
                    jump EP15_John_Anim_Menu
                "Slower":
                    hide EP15_John_Anim_0
                    hide EP15_John_Anim_0_Faster
                    hide EP15_John_Anim_3
                    hide EP15_John_Anim_3_Faster
                    $ EP15_Anim_Speed = 1
                    if EP15_Anim_Option == 1:
                        show EP15_John_Anim_3 with Dissolve(0.5)
                    elif EP15_Anim_Option == 2:
                        show EP15_John_Anim_0 with Dissolve(0.5)
                    jump EP15_John_Anim_Menu
                "Faster":
                    hide EP15_John_Anim_0
                    hide EP15_John_Anim_0_Faster
                    hide EP15_John_Anim_3
                    hide EP15_John_Anim_3_Faster
                    $ EP15_Anim_Speed = 2
                    if EP15_Anim_Option == 1:
                        show EP15_John_Anim_3_Faster with Dissolve(0.5)
                    elif EP15_Anim_Option == 2:
                        show EP15_John_Anim_0_Faster with Dissolve(0.5)
                    jump EP15_John_Anim_Menu
                "Continue":
                    $ different_choice_menu = False
                    pass
            scene 44-7 night 18 with Dissolve(0.5)
            j "So... Will you let me in the bed?"
            j "Heh... I feel so light... The weed is crazy."
            a "Ugh... Fine."
            scene 44-7 night 19 with Dissolve(0.5)
            a1 "Eh... Mmm..."
            j "The medicine probably got him knocked out cold..."
            a1 "Mmmm... Anna..."
            scene 44-7 night 20 with Dissolve(0.5)
            a "Shhh... It's ok."
            a "It's just a dream..."
            a1 "Mhm..."
            scene 44-7 night 21 with Dissolve(0.5)
            a "Just me here..."
            play sound undress
            scene 44-7 night 22 with Dissolve(0.5)
            j "Yeah... Got some room, Heh..."
            a "Just the tip, got it?"
            j "Yes, Anna... Heh..."
            scene 44-7 night 23 with Dissolve(0.5)
            j "Ooh... I'm soooo excited..."
            j "I didn't know weed makes you this horny..."
            j "Must've smoked different shit before."
            scene 44-7 night 24 with Dissolve(0.5)
            j "Oh, you're so hot... Fuck me..."
            a "Come on..."
            j "Niiice..."
            scene 44-7 night 25 with Dissolve(0.5)
            j "Yeah... Ohh... The tip is sliding innn..."
            j "That pussy... Pristine..."
            a "Oh..."
            "Anna was holding back her moans... But her orifice was sensitive..."
            play sound femmoan_1
            scene 44-7 night 26 with Dissolve(0.5)
            a "Oh..."
            j "Yeahh... That's so good..."
            "John, obviously, didn't stop with just the tip."
            $ different_choice_menu = True
            $ EP15_Anim_Option = 1
            $ EP15_Anim_Speed = 1
            $ EP15_John_Anim_Menu_Var_1 = False
            $ EP15_John_Anim_Menu_Var_2 = False
            scene black
            play sound jerk loop
            show EP15_John_Anim_2 with Dissolve(0.5)
            label EP15_John_Anim_Menu_2_Label:
            if EP15_John_Anim_Menu_Var_1 == False:
                j "Mmm..."
                a "Oh... Mh..."
                j "Yeah. That pussy..."
                $ EP15_John_Anim_Menu_Var_1 = True
            menu EP15_John_Anim_Menu_1:
                "View 1":
                    hide EP15_John_Anim_5
                    hide EP15_John_Anim_5_Faster
                    hide EP15_John_Anim_2
                    hide EP15_John_Anim_2_Faster
                    $ EP15_Anim_Option = 1
                    if EP15_Anim_Speed == 1:
                        show EP15_John_Anim_2 with Dissolve(0.5)
                    elif EP15_Anim_Speed == 2:
                        show EP15_John_Anim_2_Faster with Dissolve(0.5)
                    jump EP15_John_Anim_Menu_1
                "View 2":
                    hide EP15_John_Anim_5
                    hide EP15_John_Anim_5_Faster
                    hide EP15_John_Anim_2
                    hide EP15_John_Anim_2_Faster
                    $ EP15_Anim_Option = 2
                    if EP15_Anim_Speed == 1:
                        show EP15_John_Anim_5 with Dissolve(0.5)
                    elif EP15_Anim_Speed == 2:
                        show EP15_John_Anim_5_Faster with Dissolve(0.5)
                    jump EP15_John_Anim_Menu_1
                "Slower":
                    hide EP15_John_Anim_5
                    hide EP15_John_Anim_5_Faster
                    hide EP15_John_Anim_2
                    hide EP15_John_Anim_2_Faster
                    $ EP15_Anim_Speed = 1
                    if EP15_Anim_Option == 1:
                        show EP15_John_Anim_2 with Dissolve(0.5)
                    elif EP15_Anim_Option == 2:
                        show EP15_John_Anim_5 with Dissolve(0.5)
                    jump EP15_John_Anim_Menu_1
                "Faster":
                    hide EP15_John_Anim_5
                    hide EP15_John_Anim_5_Faster
                    hide EP15_John_Anim_2
                    hide EP15_John_Anim_2_Faster
                    $ EP15_Anim_Speed = 2
                    if EP15_Anim_Option == 1:
                        show EP15_John_Anim_2_Faster with Dissolve(0.5)
                    elif EP15_Anim_Option == 2:
                        show EP15_John_Anim_5_Faster with Dissolve(0.5)
                    jump EP15_John_Anim_Menu_1
                "Continue":
                    $ different_choice_menu = False
                    pass
            scene 44-7 night 27 with Dissolve(0.5)
            a "John... mhmm..."
            j "Yeah... That's good, Do you want me to stop?"
            a "Ah... N... No..."
            scene 44-7 night 28 with Dissolve(0.5)
            j "Those boobs..."
            j "So hot..."
            j "Lemme just..."
            play sound femmoan_3
            scene 44-7 night 29 with vpunch
            j "OOooohhhh...."
            "They tried their best to keep their voices low..."
            "Somehow, he wasn't awoken by the depravities taking place."
            scene 44-7 night 30 with Dissolve(0.5)
            j "Annnaaaa... Ahh..."
            a "Oh..."
            j "I'm getting close..."
            a "Keep it down..."
            j "I'm... I'm... Anna..."
            play sound cum_sound
            scene 44-7 night 31 with flash_vpunch
            j "ah..."
            a "Yeah... Fill it..."
            j "mhmm..."
            scene 44-7 night 32 with Dissolve(0.5)
            a "Oh..."
            a "I feel the warm spunk inside of me..."
            j "Yeah... I unleashed a good load, that's true."
            scene 44-7 night 33 with Dissolve(0.5)
            a "So, not horny anymore?"
            j "Damn... No... But that was good... A nice quickie, just the way I like em."
            j "Every man likes those once in a while."
            a "Heh..."
            play sound undress
            scene 44-7 night 34 with Dissolve(0.5)
            a "So... You done? Just like that?"
            j "Yeah, that's exactly what I needed. Heh."
            a "Well... Fine."
            scene 44-7 night 35 with Dissolve(0.5)
            j "Thanks, Anna. Much appreciated."
            "Was it Anna's fate to be just some quick cum-dump for all the men she comes across..."
            scene 44-7 night 36 with Dissolve(0.5)
            a "Oh... Thank god Andrew didn't wake up."
            a "That would've been a disaster..."
            $ renpy.end_replay()
            scene black with Dissolve(0.5)
            "Anna fell asleep quickly."
        "Are you out of your mind??? NO!":
            scene 44-7 night 11 with Dissolve(0.5)
            a "How could you even ask such a thing?"
            a "I'm your sons girlfriend."
            j "Fine, fine... I just... I thought I received some mixed signals..."
            a "You were wrong..."
            j "Let's keep this between us, ok?"
            a "Of course, Andrew wouldn't take it well..."
            scene black with Dissolve(0.5)
            "Anna fell asleep quickly."

label EP15_Andrew:
    $ EP15_var_3 = True
    pause 1
    stop music
    play sound interface_sound
    show text "Wednesday Morning..." with Dissolve(0.5)
    pause 2
    play music tranquility
    scene 45-1 morning 1 with Dissolve(0.5)
    a "Ahh... Another wonderful morning..."
    a "Waking as the sun shines in."
    a "{i}...Where's Andrew...{/i}"
    scene 45-1 morning 2 with Dissolve(0.5)
    a1 "Good morning, sunshine."
    a1 "Sleep well?"
    a "Oh, hey, honey."
    a "Yeah, thanks."
    scene 45-1 morning 3 with Dissolve(0.5)
    a1 "Listen, I made you coffee."
    a "Oh, really?"
    a "That's so sweet."
    scene 45-1 morning 4 with Dissolve(0.5)
    a1 "Anything for you, Anna."
    a "How are you feeling? How are the wounds?"
    a1 "Well, As you can see..."
    scene 45-1 morning 5 with Dissolve(0.5)
    a1 "I can walk, still hurts, but it's manageable."
    a1 "I'm slightly high from the drugs still..."
    a1 "But, clear enough to get stuff done."
    a1 "How did your contract closing go?"
    a "Oh... You know... It's a different culture. They had some... Interesting rituals."
    a1 "Really?"
    a "Yeah... I'll tell you all about it some other time."
    a1 "Ok."
    scene 45-1 morning 6 with Dissolve(0.5)
    a1 "How's the coffee?"
    a "It's great. Thanks, Andrew!"
    a1 "You're very welcome, anything for my queen."
    a "Heh."
    scene 45-1 morning 7 with Dissolve(0.5)
    a "So. What's your plan for today?"
    a1 "Oh me?"
    a1 "I'll get my bearings. Go for a walk, do some housework, you know?"
    a "Yeah. That's great."
    a1 "Might do something with Ashley."
    scene 45-1 morning 8 with Dissolve(0.5)
    a1 "You never cease to amaze me."
    a1 "Your body is wonderfully amazing!"
    a "Heh... Soon, very soon. Andrew."
    a1 "I. Can't. Wait..."
    play sound undress
    scene black with Dissolve(0.5)
    pause 1
    scene 45-1 morning 9 with Dissolve(0.5)
    a "Alright."
    a "Time for me to go."
    a1 "Oh... Our time together is so short..."
    a "We'll spend more time together soon."
    a "OK?"
    a1 "You bet."
    play sound kisspeck
    scene 45-1 morning 10 with Dissolve(0.5)
    a1 "Mm..."
    scene 45-1 morning 11 with Dissolve(0.5)
    a1 "I'm looking forward to seeing you later."
    a "Me too, Andrew..."
    scene black with Dissolve(0.5)
    pause 1
    play sound door2
label EP15_Boys:
    $ EP15_var_4 = True
    play sound surprise
    play music chill_song_2
    scene 45-2 boys 1 with Dissolve(0.5)
    a "Oh... Hey guys."
    scene 45-2 boys 2 with Dissolve(0.5)
    ro2 "Anna! Hey. Good to see you!"
    st2 "Hey, Anna."
    a "So..."
    a "Care to explain why John came home high?"
    scene 45-2 boys 3 with Dissolve(0.5)
    ro2 "Uhh..."
    scene 45-2 boys 2 with Dissolve(0.5)
    st2 "Who?"
    scene 45-2 boys 4 with Dissolve(0.5)
    a "My boyfriend's dad. Middle-aged man."
    a "He told me about a party he went to with some young dudes."
    a "He smoked a bunch of weed with them..."
    scene 45-2 boys 5 with Dissolve(0.5)
    a "You guys know anything about that?"
    st2 "Uhh..."
    scene 45-2 boys 6 with Dissolve(0.5)
    st2 "Yeah... Hah..."
    st2 "I suppose he smelled the weed and then came down to us."
    st2 "Asked if we had anymore."
    st2 "He seemed cool so we invited him in."
    scene 45-2 boys 7 with Dissolve(0.5)
    st2 "We got preetttyyy high."
    st2 "But John, he was wayy up there."
    st2 "He was funny as fuck, told us stories from his youth."
    st2 "Also said that weed has become way stronger."
    st2 "At some point he disappeared. We assumed he went home."
    a "Well... When he came home... I had to... Deal with him..."
    st2 "Hope he wasn't too much trouble."
    scene 45-2 boys 6 with Dissolve(0.5)
    a "Nah... It was ok."
    st2 "Hey listen, we are planning to go to the beach later today."
    st2 "Care to join?"
    a "Hmm..."
    scene 45-2 boys 8 with Dissolve(0.5)
    a "If there's time, I will join you."
    a "But, I have to run now. Take care guys."
    ro2 "Bye, Anna."
    st2 "Bye, Anna."
    scene black with Dissolve(0.5)
    pause 1

label EP15_Timothy:
    $ EP15_var_10 = True
    scene 45-3 tim 1 with Dissolve(0.5)
    t "Anna. Hey..."
    t "How's your day going?"
    scene 45-3 tim 2 with Dissolve(0.5)
    a "It's good, thanks. What about you?"
    t "Better now that you showed up, heh."
    a "Oh... That's sweet, thanks."
    scene 45-3 tim 3 with Dissolve(0.5)
    a "Listen, I got this issue I could use your help with."
    a "I need some files cracked... Opened. Since you're smart with computers, I thought you might be able to help."
    scene 45-3 tim 4 with Dissolve(0.5)
    t "Well... Yeah, I can... But."
    t "It's not illegal or anything, right?"
    t "Won't get us in trouble."
    scene 45-3 tim 3 with Dissolve(0.5)
    a "Nooo... Of course not... Heh."
    a "When have I done anything shady?"
    scene 45-3 tim 4 with Dissolve(0.5)
    t "You're asking me as if shady is your middle name."
    t "Like Slim Shady..."
    a "..."
    a "Oh you mean the rapper?"
    t "Yeah... Heh..."
    a "Riiight... Yeah, hah..."
    scene 45-3 tim 5 with Dissolve(0.5)
    a "Anyway, here's the phone."
    a "So you can download the files."
    a "Don't worry, you won't get into any trouble, I'll make sure of it."
    t "Ok. Heh... Not that I wouldn't help you in any case."
    scene 45-3 tim 6 with Dissolve(0.5)
    t "Alright... Let's see what we're working with."
    t "Hmm..."
    a "Download message history."
    t "Alright... Hmm..."
    t "These files seem to have some security."
    t "That's pretty impressive. The messaging service has some good encryption."
    scene 45-3 tim 7 with Dissolve(0.5)
    t "Fortunately, I recently went to a seminar about encryption and online system security."
    t "The good thing is that this phone uses an Asymmetric encryption method, not very fast. So we could kind of overwhelm it."
    a "So, you'll be able to crack it?"
    scene 45-3 tim 8 with Dissolve(0.5)
    t "Heh... Yeah."
    a "Wow, you're such a hacker... Heh... Like in the spy movies."
    t "Well, the difference is, in those movies, the visuals are usually super unrealistic."
    t "Mostly, it's black screens with text, command prompts, and powershells and whatnot."
    t "And a lot of text."
    t "Soo... Not really interesting, really boring, in fact."
    scene 45-3 tim 9 with Dissolve(0.5)
    a "Hah... Well, that's why I'm here."
    a "To keep you company, eh?"
    t "Yeah, That's definitely as good as it gets."
    scene 45-3 tim 10 with Dissolve(0.5)
    t "Anyway, here's the phone. I copied the files."
    t "It will take some time to crack it, but it shouldn't take too long."
    a "Hmm... Ok, thanks, Timothy."
    scene 45-3 tim 11 with Dissolve(0.5)
    a "I really appreciate your help."
    t "Think nothing of it, I'm happy to help you, Anna."
    if timothySexContent == True:
        t "By the way."
        t "Are we still on for the Cosplay event?"
        scene 45-3 tim 12 with Dissolve(0.5)
        a "Hehe... You bet."
        t "Awesome! I've got a perfect outfit picked out for you!"
        a "Heh... Can't wait to see it."
        a "Later, Timothy..."
    scene black with Dissolve(0.5)
    pause 1
    jump EP15_Office

label EP15_Jeff:
    play music chill_song_3
    $ EP15_var_5 = True
    play ambient BirdsInPark
    scene 45-4 jeff 1 with Dissolve(0.5)
    a "Jeff! Hey!"
    j2 "Anna!"
    scene 45-4 jeff 1-2 with Dissolve(0.5)
    j2 "Hey... Lovely to see you."
    j2 "Truly is..."
    a "Likewise, Jeff..."
    play sound undress
    scene 45-4 jeff 1-3 with Dissolve(0.5)
    j2 "Mmm..."
    a "Hehe... You ok?"
    j2 "Yes, just savoring the moment."
    scene 45-4 jeff 2 with Dissolve(0.5)
    a "So... How have you been?"
    j2 "Oh me? You know... Just living the good life."
    j2 "My other jobs keep me busy."
    j2 "I might have only one talent... In my pants, but..."
    a "Hehe... It's a BIG talent, to be honest."
    j2 "Hehe... Maybe, but I like to keep active in other aspects too."
    scene 45-4 jeff 3 with Dissolve(0.5)
    j2 "What about you?"
    j2 "How have you been?"
    a "Me? I'm very busy, I've got a lot of things I gotta take care of."
    a "Life just keeps throwing stuff at me, you know?"
    j2 "I get you. It's never a straight road."
    j2 "Gets quite bumpy at times, but we get through it."
    scene 45-4 jeff 4 with Dissolve(0.5)
    j2 "Perhaps you want to sit?"
    a "Sure."
    play sound jacketcloth
    scene 45-4 jeff 5 with Dissolve(0.5)
    a "Anyway. Got any news from Dylan?"
    j2 "Yeah, actually."
    j2 "He said he'll have a job for me, with you actually and"
    j2 "Uhh... Rebecca..."
    a "Niice."
    a "You said you do other things, too?"
    scene 45-4 jeff 6 with Dissolve(0.5)
    j2 "Yeah, I like to keep active in the community."
    j2 "I know I might not be the best role model, but regardless."
    j2 "I try my best to help people who are less fortunate."
    j2 "Mostly I go and help at the homeless shelters. Help Youth outreach centers."
    a "Wow. Really? That's... Amazing."
    j2 "Not much money in helping the helpless, but. I get paid in different ways."
    scene 45-4 jeff 5 with Dissolve(0.5)
    a "I'm very impressed, Jeff."
    a "I liked you before, but now... You have my respect."
    j2 "Heh, Like I said, the thing between my pants might be my only talent, but that doesn't mean I can't help other ways."
    scene 45-4 jeff 7 with Dissolve(0.5)
    j2 "You know, I've been thinking."
    a "Oh?"
    j2 "You are quite a woman, besides our professional relationship."
    a "Heh. I can't argue there."
    j2 "You won't deny that we click, at least on set."
    a "Yeah. And that makes things a lot easier."
    scene 45-4 jeff 8 with Dissolve(0.5)
    j2 "Indeed. So I just decided that I'll throw caution to the wind and invite you out."
    j2 "So that we'd do something outside the set."
    a "Heh, why not."
    j2 "So... I've been wanting to go on a hike, outside Suncity."
    j2 "There are some beautiful mountains a couple of hours drive away from here..."
    scene 45-4 jeff 9 with Dissolve(0.5)
    a "That sounds awesome! Yeah. Sign me up!"
    j2 "Well, I still have to match out the ifs and hows, but I'm glad you're on board."
    a "Absolutely, Jeff. After all, you've told me, I'd definitely be down to do some fun activities."
    scene 45-4 jeff 10 with Dissolve(0.5)
    menu:
        "Kiss on the lips.":
            play sound kisspeck
            scene 45-4 jeff 12 with Dissolve(0.5)
            a "Mmm..."
            j2 "Mmm..."
            scene 45-4 jeff 13 with Dissolve(0.5)
            j2 "See you around, Anna."
            a "You too, Jeff."
        "Kiss on the cheek.":
            play sound kisspeck
            scene 45-4 jeff 11 with Dissolve(0.5)
            j2 "See you around, Anna."
            a "You too, Jeff..."
    stop ambient
    scene black with Dissolve(0.5)
    pause 1
    jump EP15_Beach
label EP15_Beach:
    $ EP15_var_13 = True
    $ JohnIsAtHome = False
    $ EP15_Beach_Queue = ["audio/sounds/Days Like These.mp3", "audio/sounds/beach_dayz.mp3"]
    $ renpy.music.play(EP15_Beach_Queue, fadeout=1, fadein=1)
    play ambient beach_ambience
    scene 45-5 beach 1 with Dissolve(0.5)
    st2 "Bro! My biceps are way fuller than yours."
    st2 "I mean, just look at them."
    st2 "That's because I take creatine."
    scene 45-5 beach 2 with Dissolve(0.5)
    do1 "Good for you. As long as you're ok with losing hair."
    st2 "Bro that's bull, research doesn't support it."
    do1 "Sure, but yo dad got that bald had already."
    st2 "So? Nothing bad with being bald."
    a "{i}...Heh... Their banter...{/i}"
    scene 45-5 beach 3 with Dissolve(0.5)
    do1 "Khe... Khem..."
    st2 "She's behind me, right?"
    st2 "I look like a dork."
    st2 "Shit..."
    a "Not at all. Dorks don't flex their muscles heh..."
    a "You look more like a jackass... Haha..."
    do1 "HAHA! Good one Anna!"
    scene 45-5 beach 4 with Dissolve(0.5)
    st2 "Fair enough. I don't have a comeback from that."
    do1 "Of course you don't. You spent all your money on weed instead of school books."
    scene 45-5 beach 5 with Dissolve(0.5)
    a "So. What's up? What you guys been doing?"
    a "Anything interesting planned for today?"
    do1 "We do, in fact."
    scene 45-5 beach 6 with Dissolve(0.5)
    do1 "We were hoping to play volleyball, but one of our friends couldn't make it."
    do1 "He had to see about a girl or whatever."
    do1 "Not like I'm judging, but bros before hoes, right?"
    st2 "Dude, that's his sister, she just had leg surgery."
    do1 "Whoops. In that case, I take it back."
    scene 45-5 beach 7 with Dissolve(0.5)
    do1 "Buut... Since you're here, we actually have four people. That's really good news."
    ro2 "Damn straight!"
    a "Volleyball, you say?"
    do1 "Yeah, you up for it?"
    scene 45-5 beach 8 with Dissolve(0.5)
    a "Heh... Why the hell not."
    a "It's been a while since I played but..."
    a "On such a good day, why not?"
    scene 45-5 beach 9 with Dissolve(0.5)
    a "I'll just go and change, ok?"
    st2 "Uh... Yeah, take your time."
    scene 45-5 beach 10 with Dissolve(0.5)
    st2 "BROOOOO..."
    st2 "We'll see her in a bikini or something!"
    do1 "OH... She's such a hot female..."
    st2 "DUUDE..."
    st2 "I wonder how old she is."
    do1 "Good question. She got that bustyness of a milf, but at the same time looks hella young."
    play sound door2
    scene 45-5 beach 11 with Dissolve(0.5)
    a "Hehe... I bet they are not ready for the outfit I'm about to wear..."
    scene black with Dissolve(0.5)
    play sound undress
    scene 45-5 beach 12 with Dissolve(0.5)
    do1 "Hey, could you hook us up with some cold beers?"
    do1 "We could use some refreshments."
    bb1 "Coming right up."
    scene black with Dissolve(0.5)
    pause 1
    scene 45-5 beach 13 with Dissolve(0.5)
    do1 "..."
    ro2 "..."
    st2 "..."
    st2 "GOD DAMN!!!!"
    st2 "Shit... sorry..."
    a "What?"
    a "Don't like it?"
    play sound whoosh
    scene 45-5 beach 14 with flash:
        yalign 1
        linear 8 yalign 0.0
    pause 8
    scene 45-5 beach 15 with Dissolve(0.5)
    ro2 "Uhh... No. I mean, yeah... it's all cool... We ain't even got an idea what you's talking about."
    ro2 "We good, we good."
    a "Hehe... Whatever you say."
    a "{i}...They are definitely smitten...{/i}"
    scene 45-5 beach 16 with Dissolve(0.5)
    a "So... You guys ready to play some volleyball or what?"
    st2 "Hell Yeah!"
    do1 "Damn straight we are."
    a "Alright let's choose teams."
    scene 45-5 beach 17 with Dissolve(0.5)
    a "I choose, Rocco."
    ro2 "YEAH!"
    ro2 "That's whats up!"
    scene 45-5 beach 18 with Dissolve(0.5)
    st2 "But... Why?"
    st2 "I'm a way better player than Rocco."
    ro2 "Haha... Bro, you're just jelly."
    st2 "I ain't jealous... pff..."
    scene 45-5 beach 19 with Dissolve(0.5)
    a "Don't worry about it, I will try to not be too harsh on your amateurs."
    st2 "WHAAAA?"
    a "HAHA... How about we make the game a bit more fun."
    a "Each time a team loses 3 points, that team has to lose some clothing."
    do1 "WHooaaa?"
    a "What? Scared?"
    do1 "We ain't!"
    a "Alright, it's a deal."
    scene 45-5 beach 20 with Dissolve(0.5)
    "They all took their positions."
    "And preapred."
    scene 45-5 beach 21 with Dissolve(0.5)
    ro2 "We'll beat them, easy."
    a "Of course."
    scene 45-5 beach 22 with Dissolve(0.5)
    a "Come on. Show me what you got, boys."
    a "I won't be an easy target."
    play sound whoosh_1
    scene 45-5 beach 23 with Dissolve(0.5)
    do1 "Huahh!"
    play sound sound_volleyball_hit_1
    scene 45-5 beach 24 with Dissolve(0.5)
    a "I got it!"
    ro2 "OK!"
    play sound sound_volleyball_hit_2
    scene 45-5 beach 25 with vpunch
    pause 1
    a "Passing to you!"
    scene 45-5 beach 26 with Dissolve(0.5)
    ro2 "Alright!!!"
    ro2 "I'm setting for you, Anna."
    a "I'm ready!"
    play sound sound_volleyball_hit_1
    scene 45-5 beach 27 with vpunch
    a "Haaaah!"
    scene 45-5 beach 28 with Dissolve(0.5)
    st2 "I got it, bro!"
    do1 "No, I got it!"
    do1 "DUUDE!"
    play sound surprise2
    scene 45-5 beach 29 with Dissolve(0.5)
    do1 "Niaah!"
    st2 "Haauh..."
    play sound lighthit
    scene 45-5 beach 30 with vpunch
    do1 "Fuck!"
    st2 "ASSHOLE!!!"
    scene 45-5 beach 31 with Dissolve(0.5)
    st2 "BRO!"
    st2 "I had it!"
    do1 "Bro, I said first!"
    scene 45-5 beach 32 with Dissolve(0.5)
    a "Aawww... So cute..."
    a "Maybe get it over with and kiss?"
    a "HAHA."
    scene 45-5 beach 33 with Dissolve(0.5)
    do1 "Next time, keep your ears open."
    st2 "And you do the same."
    st2 "We can own them, just gotta keep our heads into the game."
    scene 45-5 beach 34 with Dissolve(0.5)
    a "Come on, you guys are dragging the game. Scared to lose or what?"
    st2 "We ain't scared."
    do1 "No way!"
    scene 45-5 beach 35 with Dissolve(0.5)
    a "Alright, My serve. You ready?"
    ro2 "Yes, Anna."
    ro2 "Ready when you are."
    play sound sound_volleyball_hit_2
    scene 45-5 beach 36 with Dissolve(0.5)
    a "Huaah!"
    play sound sound_volleyball_hit_1
    scene 45-5 beach 37 with vpunch
    st2 "I got it!"
    do1 "All yours, Steve!"
    scene 45-5 beach 38 with Dissolve(0.5)
    do1 "Aight, Ahh!"
    play sound sound_volleyball_hit_2
    scene 45-5 beach 39 with Dissolve(0.5)
    a "On me again!"
    ro2 "Yup!"
    scene 45-5 beach 40 with Dissolve(0.5)
    pause 1
    scene 45-5 beach 41 with Dissolve(0.5)
    ro2 "You got it!"
    play sound sound_volleyball_hit_2
    scene 45-5 beach 42 with Dissolve(0.5)
    a "HYAAAH!"
    scene 45-5 beach 43 with Dissolve(0.5)
    st2 "Whoooaaaaa..."
    scene 45-5 beach 44 with Dissolve(0.5)
    "Steve was mesmerized... Could barely believe his eyes..."
    scene 45-5 beach 45 with Dissolve(0.5)
    do1 "COME OOONNN STEEEEVEEE YOU GOT THIIIIS!!!"
    "But Steve did, in fact, not have it... His eyes were completely locked on Anna's pussy hair."
    play sound lighthit
    scene 45-5 beach 46 with vpunch
    do1 "NOOoooo!"
    st2 "AAHHHH!"
    scene 45-5 beach 47 with Dissolve(0.5)
    a "Oh! Are you ok?"
    st2 "Ouch..."
    st2 "That was not... What I had in mind..."
    do1 "Haha... Bro, you took the ball like a champ."
    ro2 "Word... Haha... You good, bro?"
    st2 "Yeah... Yeah... I just got distracted..."
    scene 45-5 beach 48 with Dissolve(0.5)
    st2 "Alright... Alright... I'm good. Let's just play, I got this..."
    st2 "Ultra focus mode on."
    st2 "I'll show you guys how a real pro plays this game."
    scene 45-5 beach 49 with Dissolve(0.5)
    st2 "Come on, hit me with your best shot."
    a "Hehe... Alright..."
    st2 "I'm ready for anything..."
    play sound sound_volleyball_hit_1
    scene 45-5 beach 50 with vpunch
    a "Hyah!"
    st2 "Come onnn.... I got this!"
    play sound sound_volleyball_hit_1
    scene 45-5 beach 51 with vpunch
    st2 "Hah!"
    scene 45-5 beach 52 with Dissolve(0.5)
    st2 "Set for me!"
    do1 "Yup, yup!"
    play sound whoosh_1
    scene 45-5 beach 53 with Dissolve(0.5)
    st2 "TAKE THAT! HAAAAA!"
    play sound sound_volleyball_hit_2
    scene 45-5 beach 54 with vpunch
    pause 1
    play sound whoosh_1
    scene 45-5 beach 55 with Dissolve(0.5)
    ro2 "Shit!"
    play sound lighthit
    scene 45-5 beach 56 with Dissolve(0.5)
    ro2 "Sorry, Anna... I missed that."
    a "It's ok..."
    st2 "HAHAAAA! Take it! YEAH!"
    scene 45-5 beach 57 with Dissolve(0.5)
    ro2 "Piss off bro, you just got lucky. We're already two points in the lead."
    st2 "Not for long you ain't!"
    scene 45-5 beach 58 with Dissolve(0.5)
    a "Hehe... The stakes are rising."
    a "Come on. Let's play!"
    scene 45-5 beach 59 with Dissolve(0.5)
    ro2 "Ok, your ball, guys."
    ro2 "Please miss, I wanna see you embarrass yourselves."
    scene 45-5 beach 60 with Dissolve(0.5)
    st2 "Ain't gonna happen, biiitch."
    st2 "We are pros."
    st2 "And we'll leave you in the dust."
    play sound whoosh_1
    scene 45-5 beach 61-1 with Dissolve(0.5)
    st2 "Huuuh!"
    play sound sound_volleyball_hit_1
    scene 45-5 beach 61 with vpunch
    pause 1
    scene 45-5 beach 62 with Dissolve(0.5)
    ro2 "{i}...Damn... It barely covers anything...{/i}"
    ro2 "{i}...Shit... gotta keep my head in the game...{/i}"
    play sound sound_volleyball_hit_1
    scene 45-5 beach 63 with Dissolve(0.5)
    ro2 "HAH! Got it!"
    a "NICE!"
    play sound sound_volleyball_hit_2
    scene 45-5 beach 64 with Dissolve(0.5)
    a "Here, I got a perfect setup for you!"
    ro2 "NIIIICE!!!"
    play sound sound_volleyball_hit_2
    scene 45-5 beach 65 with vpunch
    ro2 "HUUUUAAAAAAH!!!"
    play sound sound_volleyball_hit_2
    scene 45-5 beach 66 with vpunch
    pause 0.5
    play sound whoosh_1
    scene 45-5 beach 67 with vpunch
    pause 0.5
    scene 45-5 beach 68 with Dissolve(0.5)
    do1 "FUCK!"
    st2 "DAMMMNNNN... BROOO... That was nasty..."
    st2 "Gotta admit."
    scene 45-5 beach 69 with Dissolve(0.5)
    st2 "Fuck... We lost the 3rd point..."
    do1 "Damn... I don't wanna do it..."
    scene 45-5 beach 70 with Dissolve(0.5)
    a "Good job, Rocco... Hehe..."
    ro2 "Thanks, Anna. You did amazing, too."
    scene 45-5 beach 71 with Dissolve(0.5)
    a "Alright, boys."
    a "We won fair and square... Time for you to lose them shorts."
    do1 "Shit..."
    do1 "We really have to?"
    a "What? You scared?"
    do1 "Noo..."
    scene 45-5 beach 72 with Dissolve(0.5)
    st2 "Of course he is, look at him heh..."
    st2 "A pussyyyy..."
    do1 "I am what I eat..."
    st2 "You wish."
    st2 "I ain't scared."
    play sound undress
    scene 45-5 beach 73 with Dissolve(0.5)
    st2 "There... I got a nice cock, and I ain't afraid to show it!"
    a "Oh... Hehe..."
    scene 45-5 beach 74 with Dissolve(0.5)
    st2 "See... I'm a man of my word."
    a "You are indeed... Hehe..."
    a "Now your turn, Donny."
    do1 "Shit..."
    scene 45-5 beach 75 with Dissolve(0.5)
    ro2 "Come on, don't disappoint Anna."
    do1 "Uhh..."
    do1 "Fine..."
    play sound undress
    scene 45-5 beach 76 with Dissolve(0.5)
    pause 1
    scene 45-5 beach 77 with Dissolve(0.5)
    do1 "There, happy?"
    a "Hehe... Well, well..."
    a "I see no reason why you'd be so shy."
    do1 "Heh..."
    scene 45-5 beach 78 with Dissolve(0.5)
    do1 "Thanks... Uhh... Anyway, Can I put them back on now?"
    a "Nope... We will continue playing, heh..."
    do1 "Fine..."
    scene 45-5 beach 79 with Dissolve(0.5)
    beachgirl1 "What the fuck..."
    beachgirl2 "Mmm... They are kinda hot..."
    beachgirl1 "They already got a girl with them... She's gorgeous..."
    beachgirl2 "I'm getting turned on by seeing those cocks..."
    beachgirl1 "Stop it, Lana... You got a boyfriend..."
    scene 45-5 beach 80 with Dissolve(0.5)
    a "Alright... You boys ready?"
    st2 "Fuck YEAH!!!"
    play sound sound_volleyball_hit_1
    scene 45-5 beach 81 with vpunch
    a "HUAHH!"
    scene 45-5 beach 82 with Dissolve(0.5)
    do1 "I got it!"
    play sound sound_volleyball_hit_1
    scene 45-5 beach 83 with vpunch
    pause 0.5
    scene 45-5 beach 84 with Dissolve(0.5)
    ro2 "Haha... Nice cock, Steve..."
    st2 "Shut it, dude. You gonna lose!!"
    scene 45-5 beach 85 with Dissolve(0.5)
    ro2 "Fuck..."
    scene 45-5 beach 86 with Dissolve(0.5)
    ro2 "Eh..."
    scene 45-5 beach 87 with Dissolve(0.5)
    st2 "Hehe... Not so good, are ya?"
    st2 "Our shorts were holding us back, Now we unleashed OUR ULTIMATE POWER!!!"
    scene 45-5 beach 88 with Dissolve(0.5)
    a "Well, well... Did I choose the wrong person for my team?"
    ro2 "Uhh... No, Anna... I promise."
    a "Mhmm... I think you're trying to lose on purpose..."
    ro2 "No, Anna... I promise!"
    scene 45-5 beach 89 with Dissolve(0.5)
    beachguy1 "Bro... Some weird shit goin' on..."
    beachguy2 "Those dudes are lucky... Playing with such a hot chick..."
    beachguy1 "Perhaps we should just take her from them... Surely our company is way better."
    beachguy2 "Uh... Last time you tried something like that, you got a restraining order..."
    scene 45-5 beach 90 with Dissolve(0.5)
    do1 "Alright... My serve."
    do1 "You ready to lose?"
    a "The only ones that will lose are you, boys!"
    play sound sound_volleyball_hit_2
    scene 45-5 beach 91 with Dissolve(0.5)
    do1 "Haaah!"
    scene 45-5 beach 92 with Dissolve(0.5)
    a "{i}...I got this heh... They won't beat me...{/i}"
    play sound sound_volleyball_hit_1
    scene 45-5 beach 93 with Dissolve(0.5)
    a "There. Set me up!"
    play sound sound_volleyball_hit_2
    scene 45-5 beach 94 with Dissolve(0.5)
    ro2 "Take it!"
    play sound sound_volleyball_hit_1
    scene 45-5 beach 95 with Dissolve(0.5)
    a "Hyyaaaah!"
    play sound sound_volleyball_hit_2
    scene 45-5 beach 96 with Dissolve(0.5)
    st2 "Huah... Hah! Got it!"
    st2 "Let's show them what we got!"
    scene 45-5 beach 97 with Dissolve(0.5)
    do1 "Yeah. All you bro!"
    scene 45-5 beach 98 with Dissolve(0.5)
    st2 "I got the POWERRRR!!!!!"
    scene 45-5 beach 99 with Dissolve(0.5)
    a "{i}...Uhhm... The cock...{/i}"
    "Anna lost concentration for just a moment, but it was enough to lose..."
    play sound sound_volleyball_hit_1
    scene 45-5 beach 100 with vpunch
    pause 1
    scene 45-5 beach 101 with vpunch
    pause 1
    play sound whoosh_1
    scene 45-5 beach 102 with Dissolve(0.5)
    ro2 "Shiiit..."
    a "Oh..."
    play sound lighthit
    scene 45-5 beach 103 with vpunch
    a "Ah..."
    ro2 "You ok?"
    a "Fuck... We lost..."
    scene 45-5 beach 104 with Dissolve(0.5)
    st2 "HUHH!! WHAT'S UP, WE GOT YOU!"
    do1 "Yeah!!! We are the GOATS!"
    scene 45-5 beach 105 with Dissolve(0.5)
    a "Huh..."
    scene 45-5 beach 106 with Dissolve(0.5)
    ro2 "I'm sorry Anna, I tried my best..."
    a "Hehe... Sure you did..."
    ro2 "For real."
    scene 45-5 beach 107 with Dissolve(0.5)
    a "Well, Our best wasn't good enough..."
    a "I suppose..."
    ro2 "I suppose we gotta keep up our end of the deal."
    menu:
        "Fine...":
            pass
        "Sorry... Heh. It was just a joke.":
            do1 "HAHA!! We knew it!"
            st2 "chickeeen!"
            a "Uh. Heh. sorry, but I'll get going, see you next time!"
            a "I got other things to take care of."
            ro3 "Oh... Really?"
            a "Yeah. Gotta run."
            a "Sorry to break it up like this, but yeah, later!"
            scene black with Dissolve(0.5)
            play sound undress
            pause 1
            scene 45-5 beach 184 with Dissolve(0.5)
            bb1 "Had fun?"
            a "Yeah, but now I gotta go."
            a "Any day at the beach is a good day, though. Hah."
            bb1 "You bet!"
            stop ambient
            scene black with Dissolve(0.5)
            pause 1
            jump EP15_FBI
    a "Heh... Yeah..."
    play sound undress
    scene 45-5 beach 108 with Dissolve(0.5)
    pause 1
    scene 45-5 beach 109 with Dissolve(0.5)
    ro2 "See, I ain't scared."
    a "Wow..."
    ro2 "What's that?"
    a "Nothing..."
    scene 45-5 beach 110 with Dissolve(0.5)
    ro2 "So... Uh..."
    a "I'm... I'm a bit embarrassed to do it..."
    a "But... A deal's a deal..."
    scene 45-5 beach 111 with Dissolve(0.5)
    a "Here goes..."
    play sound undress
    scene 45-5 beach 112 with Dissolve(0.5)
    ro2 "Whooaaa..."
    a "Don't lose your heads..."
    play sound jacketcloth
    scene 45-5 beach 114 with Dissolve(0.5)
    a "There... Happy?"
    ro2 "Uhh... Um..."
    scene 45-5 beach 115 with Dissolve(0.5)
    "The dudes were dumbfounded... Actually not believing she'd take off her tiny bra."
    a "Alright, alright... Have you never seen boobs? Staring like that?"
    st2 "Uh... Niice..."
    a "Hehe..."
    scene 45-5 beach 116 with Dissolve(0.5)
    beachguy1 "She actually also took something off..."
    beachguy1 "What a day..."
    beachguy2 "I know right?"
    beachguy2 "Those dudes are all kinds of lucky..."
    scene 45-5 beach 117 with Dissolve(0.5)
    a "Alright enough gawking you three... I will go and get us all the beers."
    ro2 "That's very generous of you."
    a "Well, you gave me some weed the other day."
    do1 "Fair enough."
    scene 45-5 beach 117-1 with Dissolve(0.5)
    beachguy1 "Goddamn she's hot."
    beachguy2 "Yeah..."
    scene 45-5 beach 118 with Dissolve(0.5)
    bb1 "So... Uh... Having a good time?"
    a "You could say that heh..."
    bb1 "Correct me if I'm wrong, but it looked a bit like you lost on purpose."
    a "Hehe... Can't exactly leave those boys hanging..."
    a "I'm pretty sure they've wanted to see these for a loong time..."
    scene 45-5 beach 119 with Dissolve(0.5)
    bb1 "Well. Aren't they lucky..."
    a "OK, so... Could I have four beers please?"
    bb1 "Sure thing."
    scene 45-5 beach 120 with Dissolve(0.5)
    do1 "Beer. Nice!"
    ro2 "Yeah!"
    st2 "And Anna... A perfect beach day!"
    scene 45-5 beach 121 with Dissolve(0.5)
    a "Hehe... It is truly a wonderful day outside..."
    a "Add to that a cold beer, heaven... And sunbathing... Even better..."
    scene 45-5 beach 122 with Dissolve(0.5)
    ro2 "So uhh... Are you ok with us being... You know... With our packages out?"
    a "Oh... Heh..."
    a "Not the first time I've seen a dick..."
    ro2 "Heh..."
    scene 45-5 beach 123 with Dissolve(0.5)
    a "I don't have a problem with it at all..."
    a "To be completely honest... I like to look at them... Just a little bit you know."
    a "I'm a curious girl by nature."
    scene 45-5 beach 124 with Dissolve(0.5)
    st2 "Heh... That's cool..."
    st2 "We know a couple of girls, all of them are really shy... They'd never be down for something like this."
    a "Well, They'll grow up a bit, then they'll see... Besides..."
    a "I'm different... I don't care as much. Heh."
    st2 "You're definitely different, in a good way."
    do1 "{i}...Damn... Her panties aren't covering her vagina...{/i}"
    scene 45-5 beach 125 with Dissolve(0.5)
    do1 "{i}...Dammnn...{/i}"
    do1 "{i}...She's so hot... And slutty...{/i}"
    do1 "{i}...I wonder if she'd let us touch her...{/i}"
    do1 "{i}...Maybe she's just teasing us...{/i}"
    scene 45-5 beach 126 with Dissolve(0.5)
    do1 "{i}...Fuck... I'm getting harder...{/i}"
    play sound drinkingBeverage
    scene 45-5 beach 127 with Dissolve(0.5)
    pause 1
    scene 45-5 beach 128 with Dissolve(0.5)
    a "You know, Staying in the sun too long is not good for the skin..."
    a "Could you grab some sunscreen? It's in the changing rooms."
    scene 45-5 beach 129 with Dissolve(0.5)
    st2 "You mean me?"
    a "Yes, silly, heh..."
    a "I really need some sunscreen."
    scene 45-5 beach 130 with Dissolve(0.5)
    st2 "You bet. I'll be right back."
    a "Thanks a lot!"
    st2 "Think nothing of it!"
    scene 45-5 beach 131 with Dissolve(0.5)
    a "Can't wait for someone to massage my back..."
    a "My job can get really stressful sometimes."
    do1 "What do you do exactly?"
    a "I work at a law firm, of sorts. They provide many different services from legal advice to financial supervisory, audit, accounting, and more..."
    if dianaGoodRelations == True:
        a "I'm a partner in one of the daughter companies. Got a lot to take care of..."
        a "So a good massage really helps to take the edge off."
    else:
        a "I'm the Head of a department in one of the daughter companies."
        a "Got plenty of responsibilities."
    do1 "Wow... Impressive."
    scene 45-5 beach 132 with Dissolve(0.5)
    st2 "{i}...Hehe... This is awesommmmeeee!!!...{/i}"
    scene 45-5 beach 133 with Dissolve(0.5)
    st2 "I got the sunscreen."
    a "Nice... Could you put it on me, please?"
    st2 "For real?"
    a "Yeah. I can't reach my back."
    st2 "Absolutely! Hah."
    $ persistent.scene_46 = True
    label EP15_Beach_Sex_Label:
    $ EP15_Beach_Queue = ["audio/sounds/Days Like These.mp3", "audio/sounds/beach_dayz.mp3"]
    $ renpy.music.play(EP15_Beach_Queue, if_changed=True)
    scene 45-5 beach 134 with Dissolve(0.5)
    st2 "Like the whole back?"
    a "Yeah. Rub it in real nice."
    st2 "You got it..."
    ro2 "{i}...Lucky bastard...{/i}"
    scene 45-5 beach 135 with Dissolve(0.5)
    a "Nervous?"
    st2 "Me. Naah... I'm super confident..."
    a "Hehe... Way to go."
    play sound jerk loop
    scene 45-5 beach 136 with Dissolve(0.5)
    st2 "How does that feel?"
    a "You could work on your technique, heh..."
    a "But you're doing great."
    scene 45-5 beach 137 with Dissolve(0.5)
    do1 "Heh, lucky bastard."
    a "Don't worry, You'll have your chance."
    scene 45-5 beach 138 with Dissolve(0.5)
    st2 "{i}...Whoa... That's... So hot...{/i}"
    st2 "{i}...I really wanna fuck that pussy...{/i}"
    scene 45-5 beach 139 with Dissolve(0.5)
    "The dudes were getting increasingly horny..."
    "Anna was of course also getting aroused."
    "The constant attention and also seeing their naked cocks react to her body was enough to make her fantasize."
    scene 45-5 beach 140 with Dissolve(0.5)
    a "Heh... You like what you see, don't you?"
    st2 "Uh... Yeah... Heh..."
    a "Don't be shy... You can touch more."
    $ different_choice_menu = True
    $ EP15_Anim_Option = 1
    $ EP15_Anim_Speed = 1
    scene black
    show EP15_Beach_Anim_1 with Dissolve(0.5)
    label EP15_Beach_Anim_Menu_1_Label:
    st2 "Such a nice sensation..."
    st2 "Rubbing an ass like that."
    a "I knew you'd like it, heh."
    menu EP15_Beach_Anim_Menu:
        "View 1":
            hide EP15_Beach_Anim_1
            hide EP15_Beach_Anim_1_Faster
            $ EP15_Anim_Option = 1
            if EP15_Anim_Speed == 1:
                show EP15_Beach_Anim_1 with Dissolve(0.5)
            jump EP15_Beach_Anim_Menu
        "Slower":
            hide EP15_Beach_Anim_1
            hide EP15_Beach_Anim_1_Faster
            $ EP15_Anim_Speed = 1
            if EP15_Anim_Option == 1:
                show EP15_Beach_Anim_1 with Dissolve(0.5)
            jump EP15_Beach_Anim_Menu
        "Faster":
            hide EP15_Beach_Anim_1
            hide EP15_Beach_Anim_1_Faster
            $ EP15_Anim_Speed = 2
            if EP15_Anim_Option == 1:
                show EP15_Beach_Anim_1_Faster with Dissolve(0.5)
            jump EP15_Beach_Anim_Menu
        "Continue":
            $ different_choice_menu = False
            pass
    scene 45-5 beach 141 with Dissolve(0.5)
    st2 "Yes, ma'am..."
    st2 "Whoooaaa..."
    a "I see that you're enjoying yourself, Steve."
    st2 "Oh... Yeah..."
    scene 45-5 beach 142 with Dissolve(0.5)
    st2 "You're so hot..."
    a "I know."
    a "I bet I'm the hottest girl you've seen."
    st2 "Truest statement of the century."
    scene 45-5 beach 143 with Dissolve(0.5)
    do1 "Bro, don't bust by just looking at her, lol..."
    st2 "Fuck off, dude."
    scene 45-5 beach 145 with Dissolve(0.5)
    a "Looks like you can barely handle it yourself."
    do1 "Uhh... Yeah..."
    scene 45-5 beach 146 with Dissolve(0.5)
    a "Don't worry, I know just the thing to help you unwind."
    scene 45-5 beach 147 with Dissolve(0.5)
    a "And you too, Rocco. Even if we lost the game."
    a "We're all winners here, hehe..."
    scene 45-5 beach 148 with Dissolve(0.5)
    ro2 "That's so cool..."
    a "It's nice to be young dudes in college, eh?"
    st2 "Damn straight!"
    scene 45-5 beach 149 with Dissolve(0.5)
    a "So... What are you waiting for?"
    a "Get on top."
    st2 "Whaaaa?"
    scene 45-5 beach 150 with Dissolve(0.5)
    st2 "You sure?"
    a "Yeah... Give me a ride, Steve."
    a "I see that cock of yours is quite a bit excited to do something."
    st2 "Ok..."
    scene 45-5 beach 151 with Dissolve(0.5)
    st2 "Damn your butt is amazing..."
    a "I know."
    st2 "I'm so lucky!"
    a "Hehe."
    scene 45-5 beach 152 with Dissolve(0.5)
    a "Mh... Yeah, touch my ass with your cock..."
    st2 "Fuckk..."
    a "I like it when someone slides a cock between my cheeks."
    scene 45-5 beach 153 with Dissolve(0.5)
    a "Don't you like sliding your cock between my cheeks?"
    st2 "OHh... Yes, I do!"
    a "That's better..."
    a "Come on, enjoy yourself!"
    play sound jerk2
    scene 45-5 beach 154 with Dissolve(0.5)
    st2 "Shiiiet..."
    st2 "Your ass feels so good."
    a "Oh."
    scene 45-5 beach 155 with Dissolve(0.5)
    do1 "Damn! You, girl, are crazy!"
    a "But you love it, don't you?"
    do1 "Heh... YEAH!"
    scene 45-5 beach 156-1 with Dissolve(0.5)
    pause 1
    play sound femgasp_1
    scene 45-5 beach 156 with Dissolve(0.5)
    st2 "Niiiice..."
    a "Oh..."
    a "I love the feeling!"
    a "It's making me wet."
    $ different_choice_menu = True
    $ EP15_Anim_Option = 1
    $ EP15_Anim_Speed = 1
    scene black
    show EP15_Beach_Anim_2 with Dissolve(0.5)
    label EP15_Beach_Anim_Menu_2_Label:
    st2 "Oh... My cock between those cheeks."
    st2 "Heaven, if I ever knew one."
    a "Yeah? I'm glad you like it."
    menu EP15_Beach_Anim_Menu_2:
        "View 1":
            hide EP15_Beach_Anim_2
            hide EP15_Beach_Anim_2_Faster
            hide EP15_Beach_Anim_3
            hide EP15_Beach_Anim_3_Faster
            $ EP15_Anim_Option = 1
            if EP15_Anim_Speed == 1:
                show EP15_Beach_Anim_2 with Dissolve(0.5)
            elif EP15_Anim_Speed == 2:
                show EP15_Beach_Anim_2_Faster with Dissolve(0.5)
            jump EP15_Beach_Anim_Menu_2
        "View 2":
            hide EP15_Beach_Anim_2
            hide EP15_Beach_Anim_2_Faster
            hide EP15_Beach_Anim_3
            hide EP15_Beach_Anim_3_Faster
            $ EP15_Anim_Option = 2
            if EP15_Anim_Speed == 1:
                show EP15_Beach_Anim_3 with Dissolve(0.5)
            elif EP15_Anim_Speed == 2:
                show EP15_Beach_Anim_3_Faster with Dissolve(0.5)
            jump EP15_Beach_Anim_Menu_2
        "Slower":
            hide EP15_Beach_Anim_2
            hide EP15_Beach_Anim_2_Faster
            hide EP15_Beach_Anim_3
            hide EP15_Beach_Anim_3_Faster
            $ EP15_Anim_Speed = 1
            if EP15_Anim_Option == 1:
                show EP15_Beach_Anim_2 with Dissolve(0.5)
            elif EP15_Anim_Option == 2:
                show EP15_Beach_Anim_3 with Dissolve(0.5)
            jump EP15_Beach_Anim_Menu_2
        "Faster":
            hide EP15_Beach_Anim_2
            hide EP15_Beach_Anim_2_Faster
            hide EP15_Beach_Anim_3
            hide EP15_Beach_Anim_3_Faster
            $ EP15_Anim_Speed = 2
            if EP15_Anim_Option == 1:
                show EP15_Beach_Anim_2_Faster with Dissolve(0.5)
            elif EP15_Anim_Option == 2:
                show EP15_Beach_Anim_3_Faster with Dissolve(0.5)
            jump EP15_Beach_Anim_Menu_2
        "Continue":
            $ different_choice_menu = False
            st2 "Shit... I'm... Getting close..."
            st2 "Mmm..."
            pass
    scene 45-5 beach 157 with Dissolve(0.5)
    a "Ah... I feel your cock getting ready..."
    st2 "Aahh..."
    scene 45-5 beach 158 with Dissolve(0.5)
    st2 "Fuuck!"
    st2 "Your ass!"
    play sound cum_sound
    scene 45-5 beach 159 with flash_vpunch
    with flash
    st2 "AAHH!"
    with flash
    st2 "Fuck!"
    scene 45-5 beach 161 with Dissolve(0.5)
    a "Mmm... I feel that thick cum on my back."
    a "I know you liked covering me with it."
    st2 "I... ah... Fuckin hell... That was nasty good."
    a "Hehe..."
    scene 45-5 beach 162 with Dissolve(0.5)
    a "Soo... You guys look a bit lonely."
    scene 45-5 beach 163 with Dissolve(0.5)
    a "I think I know just the thing to help out."
    a "Wouldn't you say?"
    do1 "Uhh... Yeah, I would be down for some help."
    scene 45-5 beach 164 with Dissolve(0.5)
    a "Well, it's your lucky day."
    a "Cause I'm feeling in a generous mood."
    scene 45-5 beach 165 with Dissolve(0.5)
    "Anna crept closer to the other guys, her back covered..."
    "She felt very slutty, right in her element."
    scene 45-5 beach 166 with Dissolve(0.5)
    a "Come, let me alleviate your hardness."
    a "All that built up excitement."
    a "It has to go somewhere, don't you think?"
    do1 "Absolutely!"
    scene 45-5 beach 167 with Dissolve(0.5)
    do1 "Aahhh..."
    a "Mmm... A nice hard cock."
    a "Just the way I like it."
    scene 45-5 beach 168 with Dissolve(0.5)
    pause 1
    scene 45-5 beach 169 with Dissolve(0.5)
    a "Mmm..."
    do1 "Your hands... are so nice... Ah..."
    a "So is your cock... I feel it asking for more."
    $ different_choice_menu = True
    $ EP15_Anim_Option = 1
    $ EP15_Anim_Speed = 1
    scene black
    show EP15_Beach_Anim_6 with Dissolve(0.5)
    label EP15_Beach_Anim_Menu_3_Label:
    do1 "Oh... Anna... Those hands..."
    a "Hehe."
    a "I bet you'd want them touching you every day."
    do1 "OooooHhhh..."
    menu EP15_Beach_Anim_Menu_3:
        "View 1":
            hide EP15_Beach_Anim_6
            hide EP15_Beach_Anim_6_Faster
            $ EP15_Anim_Option = 1
            if EP15_Anim_Speed == 1:
                show EP15_Beach_Anim_6 with Dissolve(0.5)
            elif EP15_Anim_Speed == 2:
                show EP15_Beach_Anim_6_Faster with Dissolve(0.5)
            jump EP15_Beach_Anim_Menu_3
        "Slower":
            hide EP15_Beach_Anim_6
            hide EP15_Beach_Anim_6_Faster
            $ EP15_Anim_Speed = 1
            if EP15_Anim_Option == 1:
                show EP15_Beach_Anim_6 with Dissolve(0.5)
            jump EP15_Beach_Anim_Menu_3
        "Faster":
            hide EP15_Beach_Anim_6
            hide EP15_Beach_Anim_6_Faster
            $ EP15_Anim_Speed = 2
            if EP15_Anim_Option == 1:
                show EP15_Beach_Anim_6_Faster with Dissolve(0.5)
            jump EP15_Beach_Anim_Menu_3
        "Continue":
            $ different_choice_menu = False
            pass
    scene 45-5 beach 170 with Dissolve(0.5)
    ro2 "What about me?"
    a "Hehe... I thought you'd never ask."
    scene 45-5 beach 171 with Dissolve(0.5)
    a "Don't worry, I won't leave you... Hanging... Mhmm..."
    ro2 "Ahh... Nice!"
    scene 45-5 beach 172 with Dissolve(0.5)
    ro2 "That's... Perfect!"
    ro2 "You got some hands, Anna..."
    a "I'm experienced... I like what I do. Hehe..."
    $ different_choice_menu = True
    $ EP15_Anim_Option = 1
    $ EP15_Anim_Speed = 1
    scene black
    show EP15_Beach_Anim_7 with Dissolve(0.5)
    label EP15_Beach_Anim_Menu_4_Label:
    ro3 "Sweeet!"
    ro3 "Anna... So good."
    a "Mhmmm... I enjoy it too, you know?"
    menu EP15_Beach_Anim_Menu_4:
        "View 1":
            hide EP15_Beach_Anim_7
            hide EP15_Beach_Anim_7_Faster
            hide EP15_Beach_Anim_5
            hide EP15_Beach_Anim_5_Faster
            hide EP15_Beach_Anim_4
            hide EP15_Beach_Anim_4_Faster
            $ EP15_Anim_Option = 1
            if EP15_Anim_Speed == 1:
                show EP15_Beach_Anim_7 with Dissolve(0.5)
            elif EP15_Anim_Speed == 2:
                show EP15_Beach_Anim_7_Faster with Dissolve(0.5)
            jump EP15_Beach_Anim_Menu_4
        "View 2":
            hide EP15_Beach_Anim_7
            hide EP15_Beach_Anim_7_Faster
            hide EP15_Beach_Anim_5
            hide EP15_Beach_Anim_5_Faster
            hide EP15_Beach_Anim_4
            hide EP15_Beach_Anim_4_Faster
            $ EP15_Anim_Option = 2
            if EP15_Anim_Speed == 1:
                show EP15_Beach_Anim_5 with Dissolve(0.5)
            elif EP15_Anim_Speed == 2:
                show EP15_Beach_Anim_5_Faster with Dissolve(0.5)
            jump EP15_Beach_Anim_Menu_4
        "View 3":
            hide EP15_Beach_Anim_7
            hide EP15_Beach_Anim_7_Faster
            hide EP15_Beach_Anim_5
            hide EP15_Beach_Anim_5_Faster
            hide EP15_Beach_Anim_4
            hide EP15_Beach_Anim_4_Faster
            $ EP15_Anim_Option = 3
            if EP15_Anim_Speed == 1:
                show EP15_Beach_Anim_4 with Dissolve(0.5)
            elif EP15_Anim_Speed == 2:
                show EP15_Beach_Anim_4_Faster with Dissolve(0.5)
            jump EP15_Beach_Anim_Menu_4
        "Slower":
            hide EP15_Beach_Anim_7
            hide EP15_Beach_Anim_7_Faster
            hide EP15_Beach_Anim_5
            hide EP15_Beach_Anim_5_Faster
            hide EP15_Beach_Anim_4
            hide EP15_Beach_Anim_4_Faster
            $ EP15_Anim_Speed = 1
            if EP15_Anim_Option == 1:
                show EP15_Beach_Anim_7 with Dissolve(0.5)
            elif EP15_Anim_Option == 2:
                show EP15_Beach_Anim_5 with Dissolve(0.5)
            elif EP15_Anim_Option == 3:
                show EP15_Beach_Anim_4 with Dissolve(0.5)
            jump EP15_Beach_Anim_Menu_4
        "Faster":
            hide EP15_Beach_Anim_7
            hide EP15_Beach_Anim_7_Faster
            hide EP15_Beach_Anim_5
            hide EP15_Beach_Anim_5_Faster
            hide EP15_Beach_Anim_4
            hide EP15_Beach_Anim_4_Faster
            $ EP15_Anim_Speed = 2
            if EP15_Anim_Option == 1:
                show EP15_Beach_Anim_7_Faster with Dissolve(0.5)
            elif EP15_Anim_Option == 2:
                show EP15_Beach_Anim_5_Faster with Dissolve(0.5)
            elif EP15_Anim_Option == 3:
                show EP15_Beach_Anim_4_Faster with Dissolve(0.5)
            jump EP15_Beach_Anim_Menu_4
        "Continue":
            $ different_choice_menu = False
            ro3 "Oh... My cock..."
            do1 "Anna! Ahh!"
            pass
    scene 45-5 beach 173 with Dissolve(0.5)
    st2 "{i}...One-of-a-kind girl... So hot...{/i}"
    scene 45-5 beach 174 with Dissolve(0.5)
    a "Getting close are we?"
    a "I can feel it in your boner."
    do1 "Ohh... Yeah... Your hands are too good..."
    a "Hehe, good..."
    do1 "Fuck... Ahhh..."
    with vpunch
    play sound cum_sound
    scene 45-5 beach 175 with flash_vpunch
    do1 "AAHHH!!"
    a "Yeahhh..."
    with flash
    with flash
    do1 "Shittttt..."
    $ renpy.end_replay()
    scene 45-5 beach 172-1 with Dissolve(0.5)
    beachguy1 "What the hell is going on there?"
    beachguy2 "I think... That she's pleasuring them..."
    beachguy1 "Bro, whaaat... We gotta find out who that chick is..."
    beachguy1 "Maybe we could get some too..."
    beachguy2 "Fuck... I'm kinda horny right now for a good bitch."
    scene 45-5 beach 176 with Dissolve(0.5)
    a "Sounds like you enjoyed it..."
    scene 45-5 beach 177 with Dissolve(0.5)
    a "Oh... And you too, Rocco?"
    ro2 "Sorry, couldn't hold it in... You're too hot..."
    scene 45-5 beach 178 with Dissolve(0.5)
    a "Hehe... Well, looks like all of you have released the tension."
    a "Wouldn't you say?"
    scene 45-5 beach 179 with Dissolve(0.5)
    st2 "Uh... Yeah... I'm spent..."
    st2 "That was quite something..."
    ro2 "Damn straight."
    a "Well, I'm glad you enjoyed it... I certainly did..."
    a "But I gotta go now. Got some stuff to take care of."
    scene 45-5 beach 181 with Dissolve(0.5)
    ro2 "You can visit us again sometime, at your place."
    a "I probably will... Some weed and relaxation..."
    a "And maybe something else... Hehe..."
    do1 "Daaamn... It was awesome, thanks for spending time with us."
    a "You bet."
    a "See you around."
    scene 45-5 beach 182 with Dissolve(0.5)
    do1 "Bro... What an interesting day..."
    st2 "I feel weird that all of us got our cocks out..."
    ro2 "That's like whatever, one of the hottest chicks ever just gave us handjobs and shit."
    st2 "I hope she comes around some time again..."
    scene 45-5 beach 183 with Dissolve(0.5)
    a "Heh..."
    a "{i}...Those looked a bit flabbergasted... But thoroughly enjoyed it...{/i}"
    a "{i}...I like giving pleasure to others...{/i}"
    scene 45-5 beach 183-1 with Dissolve(0.5)
    a "This was rather fun, heh."
    a "Will see what we do next time when we meet..."
    scene black with Dissolve(0.5)
    play sound undress
    pause 1
    scene 45-5 beach 184 with Dissolve(0.5)
    bb1 "Had fun?"
    a "You could say that."
    a "See you around, hehe..."
    bb1 "You too, Anna."
    scene black with Dissolve(0.5)
    pause 1
    stop ambient
    jump EP15_FBI
label EP15_Office:
    $ EP15_var_11 = True
    scene generic office 1 with Dissolve(0.5)
    "Anna sat down at her desk and typed away..."
    "Looking through several spreadsheets and documents."
    "The work day was relatively uneventful..."
    "Just some maintenance work or emails..."
    scene black with Dissolve(0.5)
    pause 1
    scene generic office 3 with Dissolve(0.5)
    "Anna spent more time looking through the documentation, updating stuff in their work instructions..."
    scene black with Dissolve(0.5)
    "Several hours passed..."
    scene generic office 6 with Dissolve(0.5)
    a "{i}...Alright... That's it for today...{/i}"
    if dianaGoodRelations == False:
        play sound vibratorsound
        scene generic office 4 with Dissolve(0.5)
        "Suddenly Anna's vibrating summoning device went off..."
        "Jeremy was calling for her."
        a "Oh..."
        "A short burst of pleasure went through her."
    if DilanPornContent == True:
        play sound phonecall
        scene generic office 5 with Dissolve(0.5)
        a "Hello?"
        j2 "Hey... Anna... I was wondering if you'd like to meet up."
        a "Jeff? Hey!"
        a "What do you mean?"
        a "Like, regarding a shoot?"
        j2 "No. Just, two adults, meeting. Talking and such."
        a "Oh. Ok, sure. We can do that."
    scene black with Dissolve(0.5)
    pause 1
    if dianaGoodRelations == False:
        jump EP15_Mayor
    else:
        if DilanPornContent == True:
            jump EP15_Jeff
        else:
            jump EP15_Beach
label EP15_Mayor:
    $ EP15_var_6 = True
    play music PPMTimePassing
    scene 45-6 mayor 1 with Dissolve(0.5)
    a "You wanted to see me, Jeremy?"
    scene 45-6 mayor 2 with Dissolve(0.5)
    a "Oh, hello, Mayor Dalahan, sir."
    md_1 "Hello, Hello, Anna."
    scene 45-6 mayor 3 with Dissolve(0.5)
    j1 "So, let's get down to it."
    j1 "The Mayor and I are in the works on a contract with the city council."
    j1 "Mr. Dalahan has been looking at how he could 'invest' into local businesses, such as our own."
    j1 "And so we are potentially looking at a very valuable prospect if we can come to terms."
    j1 "So I decided to bring in the best, you. I told him about the basement..."
    scene 45-6 mayor 4 with Dissolve(0.5)
    a "Whaaa..."
    j1 "And he seems very, very interested..."
    j1 "I want you to give him a tour."
    scene 45-6 mayor 4-1 with Dissolve(0.5)
    a "Are you sure I should do it?"
    a "Maybe Diane is better suited for it?"
    j1 "Nonsense. You are very skilled and talented."
    scene 45-6 mayor 5 with Dissolve(0.5)
    md_1 "Hehe... I'm looking forward to the showcase, indeed, indeed. Yes."
    scene 45-6 mayor 6 with Dissolve(0.5)
    md_1 "We've talked all the details already, Jeremy. Now I'd like to see the basement."
    j1 "Of course. Anna will show you."
    a "Emmm..."
    a "Ok..."
    j1 "Wonderful!"
    scene 45-6 mayor 7 with Dissolve(0.5)
    md_1 "I hope you can be as persuasive as Jeremy says."
    md_1 "It would be very lucrative for everyone involved, hehe..."
    a "Eh... Perhaps..."
    scene 45-6 mayor 8 with Dissolve(0.5)
    if jeremySexContent == True:
        j1 "{i}...I don't like to share... But... I love the money that we'd be getting...{/i}"
        j1 "{i}...And the power of having the mayor of the city in my pocket...{/i}"
        j1 "{i}...It's a worthy sacrifice...{/i}"
    else:
        j1 "{i}...I hope I didn't put too much on Anna's shoulders...{/i}"
        j1 "{i}...She's always been clear on her stance when it comes to using her body...{/i}"
        j1 "{i}...At least with me... But if I keep being respectable and nice... Perhaps she'd want to be with me...{/i}"
    scene black with Dissolve(0.5)
    pause 1
    play sound door2
    scene 45-6 mayor 9 with Dissolve(0.5)
    a "So... Uh... This is the place..."
    md_1 "Wonderful... Wonderful!"
    scene 45-6 mayor 10 with Dissolve(0.5)
    md_1 "Plenty of contraptions, indeed."
    md_1 "Just as I imagined."
    md_1 "Hehe... Looks like Jeremy has had fun here in the past..."
    scene 45-6 mayor 11 with Dissolve(0.5)
    if jeremySexContent == True:
        a "Yeah... He has..."
    else:
        a "I wouldn't know... He's my boss, but he respects me enough to keep me out of it."
        a "I don't really question what he does with whom in here..."
    scene 45-6 mayor 12 with Dissolve(0.5)
    a "Anyway... This is the place..."
    a "I'm not sure what more he'd want me to show you..."
    md_1 "That is an excellent question."
    scene 45-6 mayor 13 with Dissolve(0.5)
    md_1 "Many tools... Well, well... He's got a bigger selection than even I did in the 80ies."
    md_1 "Gotta give it to the man, he works hard, but also plays hard."
    scene 45-6 mayor 14 with Dissolve(0.5)
    md_1 "Hehe... This one... A classic."
    md_1 "You know, he mentioned that you wouldn't only show me this place..."
    md_1 "But also showcase yourself..."
    md_1 "This is the time where your 'persuasion' comes in."
    a "{i}...Here it goes... Eh...{/i}"
    menu:
        "Uh... Jeremy asked me to showcase myself? Ok...":
            label EP15_Mayor_Sex_Label:
            $ renpy.music.play("audio/sounds/PPMTimePassing.mp3", if_changed=True)
            $ persistent.scene_45 = True
            scene 45-6 mayor 15 with Dissolve(0.5)
            a "I... I can show you something..."
            a "Will it earn the company and... Jeremy more money?"
            md_1 "Well, of course!"
            scene 45-6 mayor 16 with Dissolve(0.5)
            md_1 "And for you as well..."
            md_1 "Besides that, you'll also gain a powerful ally."
            md_1 "As long as you do my bidding."
            a "{i}...It would be good to have the Mayor as an ally...{/i}"
            scene 45-6 mayor 17 with Dissolve(0.5)
            a "Ok..."
            a "What would you like to see?"
            md_1 "How about we start slow... And then let's see."
            a "Alright."
            scene 45-6 mayor 18 with Dissolve(0.5)
            a "Soo... If I start with something like this..."
            play sound undress
            scene 45-6 mayor 19 with Dissolve(0.5)
            md_1 "Hmm... Yes... Indeed... Heh..."
            md_1 "Very good..."
            a "You like this?"
            md_1 "Turn around."
            scene 45-6 mayor 20 with Dissolve(0.5)
            a "Like this?"
            md_1 "Yes... Yes..."
            md_1 "You are a very good-looking woman indeed... Hehe..."
            md_1 "Take that off..."
            a "Really?"
            md_1 "Yes, yes!"
            play sound jacketcloth
            scene 45-6 mayor 21 with Dissolve(0.5)
            md_1 "Very nice."
            scene 45-6 mayor 23 with Dissolve(0.5)
            md_1 "Now... Turn around."
            md_1 "I want to see your... Talent..."
            scene 45-6 mayor 22 with Dissolve(0.5)
            a "Umm... Ok..."
            a "{i}...This will be lucrative... I can do it...{/i}"
            scene 45-6 mayor 24 with Dissolve(0.5)
            md_1 "Well, well..."
            md_1 "You are very gifted. Hehe..."
            a "You like what you see?"
            md_1 "I do, very much."
            scene 45-6 mayor 25 with Dissolve(0.5)
            a "Is that all?"
            md_1 "Most definitely not."
            md_1 "I want to see more."
            a "Everyone always does..."
            md_1 "Of course!"
            scene 45-6 mayor 26 with Dissolve(0.5)
            md_1 "Take off that skirt, I think it would look better on the floor."
            a "Umm... Surely I don't have to?"
            md_1 "Unless you want to earn good on the deal, you will."
            play sound undress
            scene 45-6 mayor 27 with Dissolve(0.5)
            pause 1
            scene 45-6 mayor 28 with Dissolve(0.5)
            a "Well... Satisfied?"
            md_1 "Almost. Heh..."
            scene 45-6 mayor 29 with Dissolve(0.5)
            md_1 "I think you should lose the panties."
            md_1 "I want to take a closer look at what's hiding behind them."
            scene 45-6 mayor 30 with Dissolve(0.5)
            a "I don't think we should..."
            a "It's a bit too much."
            md_1 "Do you really want to leave me and Jeremy dissatisfied?"
            a "Uh... I don't know..."
            scene 45-6 mayor 31 with Dissolve(0.5)
            md_1 "The correct answer is no. You want to stay on my good side."
            md_1 "Now. Go ahead and give me what I want."
            md_1 "And remember, you'll get what you want."
            play sound cloth_sound1
            scene 45-6 mayor 32 with Dissolve(0.5)
            a "Ok..."
            "Anna decided to play along more..."
            "Not much to lose anymore..."
            a "You like my ass?"
            md_1 "Oh, YEAH!"
            scene 45-6 mayor 33 with Dissolve(0.5)
            a "Well... The panties are off..."
            a "I'm all naked. Just like you wanted."
            md_1 "I love when I get what I want."
            scene 45-6 mayor 34 with Dissolve(0.5)
            md_1 "Hold on... There's..."
            scene 45-6 mayor 35 with Dissolve(0.5)
            md_1 "Well, well... What do we have here."
            md_1 "Forgot to pull it out?"
            a "Huh?"
            md_1 "Yes... Hehe..."
            scene 45-6 mayor 36 with Dissolve(0.5)
            md_1 "You've got something inside your ass..."
            md_1 "I didn't expect that, but I'm pleasantly surprised."
            scene 45-6 mayor 37 with Dissolve(0.5)
            md_1 "Spread those cheeks, please."
            md_1 "I'd like to examine the thing a bit more."
            a "Ok..."
            scene 45-6 mayor 38 with Dissolve(0.5)
            a "Like this?"
            scene 45-6 mayor 39 with Dissolve(0.5)
            md_1 "YES! Perfect!"
            md_1 "Hehe... I'd like to know, who put it there?"
            a "Uh..."
            md_1 "Certainly it was Jeremy, right?"
            a "Yes..."
            scene 45-6 mayor 40 with Dissolve(0.5)
            md_1 "Color me impressed. He's quite the master..."
            md_1 "And you, his puppet."
            md_1 "What exactly is it for?"
            a "So he'd be able to contact me more easily."
            md_1 "Hehe... Ingenius..."
            scene 45-6 mayor 41 with Dissolve(0.5)
            md_1 "Hmm... I wonder..."
            md_1 "How long has it been sitting in there?"
            md_1 "All day, yes?"
            a "Yes, sir."
            play sound jerk
            scene 45-6 mayor 42 with Dissolve(0.5)
            md_1 "Alright... Let us..."
            a "Ah..."
            md_1 "Like that, don't you?"
            a "Mhm..."
            md_1 "A slut indeed... I love sluts."
            scene 45-6 mayor 43 with Dissolve(0.5)
            md_1 "Out it comes."
            scene 45-6 mayor 45 with Dissolve(0.5)
            a "Ah..."
            scene 45-6 mayor 45 with Dissolve(0.5)
            md_1 "Very impressive."
            md_1 "You put that in every day at work?"
            a "Yes..."
            md_1 "Haha... I will try this on my assistant, too."
            scene 45-6 mayor 46 with Dissolve(0.5)
            md_1 "I wonder..."
            md_1 "How do you feel when he 'summons' you?"
            a "I... I feel good... I feel pleasure..."
            md_1 "Hehe."
            scene 45-6 mayor 47 with Dissolve(0.5)
            md_1 "How about we stick it somewhere, where it hasn't been."
            md_1 "What do you say?"
            a "I don't know what you mean."
            md_1 "No matter."
            play sound surprise
            scene 45-6 mayor 48 with Dissolve(0.5)
            a "Mmm..."
            md_1 "Yes... It looks good in your mouth, too."
            md_1 "Perhaps Jeremy should put something in your mouth as a means of summoning you?"
            md_1 "Like a ball gag... Haha..."
            $ different_choice_menu = True
            $ EP15_Anim_Option = 1
            $ EP15_Anim_Speed = 1
            scene black
            show EP15_Mayor_Anim_1 with Dissolve(0.5)
            label EP15_Mayor_Anim_Menu_1_Label:
            md_1 "Taste that buttplug... I bet you like it."
            a "Hmmph..."
            menu EP15_Mayor_Anim_Menu:
                "View 1":
                    hide EP15_Mayor_Anim_1
                    hide EP15_Mayor_Anim_4
                    hide EP15_Mayor_Anim_1_Faster
                    hide EP15_Mayor_Anim_4_Faster
                    $ EP15_Anim_Option = 1
                    if EP15_Anim_Speed == 1:
                        show EP15_Mayor_Anim_1 with Dissolve(0.5)
                    if EP15_Anim_Speed == 2:
                        show EP15_Mayor_Anim_1_Faster with Dissolve(0.5)
                    jump EP15_Mayor_Anim_Menu
                "View 2":
                    hide EP15_Mayor_Anim_1
                    hide EP15_Mayor_Anim_4
                    hide EP15_Mayor_Anim_1_Faster
                    hide EP15_Mayor_Anim_4_Faster
                    $ EP15_Anim_Option = 2
                    if EP15_Anim_Speed == 1:
                        show EP15_Mayor_Anim_4 with Dissolve(0.5)
                    elif EP15_Anim_Speed == 2:
                        show EP15_Mayor_Anim_4_Faster with Dissolve(0.5)
                    jump EP15_Mayor_Anim_Menu
                "Slower":
                    hide EP15_Mayor_Anim_1
                    hide EP15_Mayor_Anim_4
                    hide EP15_Mayor_Anim_1_Faster
                    hide EP15_Mayor_Anim_4_Faster
                    $ EP15_Anim_Speed = 1
                    if EP15_Anim_Option == 1:
                        show EP15_Mayor_Anim_1 with Dissolve(0.5)
                    elif EP15_Anim_Option == 2:
                        show EP15_Mayor_Anim_4 with Dissolve(0.5)
                    jump EP15_Mayor_Anim_Menu
                "Faster":
                    hide EP15_Mayor_Anim_1
                    hide EP15_Mayor_Anim_4
                    hide EP15_Mayor_Anim_1_Faster
                    hide EP15_Mayor_Anim_4_Faster
                    $ EP15_Anim_Speed = 2
                    if EP15_Anim_Option == 1:
                        show EP15_Mayor_Anim_1_Faster with Dissolve(0.5)
                    elif EP15_Anim_Option == 2:
                        show EP15_Mayor_Anim_4_Faster with Dissolve(0.5)
                    jump EP15_Mayor_Anim_Menu
                "Continue":
                    $ different_choice_menu = False
                    pass
            scene 45-6 mayor 49 with Dissolve(0.5)
            md_1 "You like that, yes?"
            a "Mm..."
            "Anna felt degraded... But something she had gotten used to... And had started to like, somewhat..."
            scene 45-6 mayor 50 with Dissolve(0.5)
            md_1 "Yes... You are so hot. Heh..."
            a "Mhmm..."
            scene 45-6 mayor 51 with Dissolve(0.5)
            md_1 "Alright, that's enough."
            a "Ahh..."
            md_1 "I think it's time for it to return to its rightful place."
            scene 45-6 mayor 52 with Dissolve(0.5)
            md_1 "Bend over, please."
            scene 45-6 mayor 53 with Dissolve(0.5)
            a "Uhh..."
            md_1 "Remember what's at stake."
            a "Ok..."
            scene 45-6 mayor 54 with Dissolve(0.5)
            a "Like this?"
            md_1 "Yes. Better."
            scene 45-6 mayor 55 with Dissolve(0.5)
            md_1 "Your ass is very, very beautiful."
            md_1 "I can't wait what we'll get up to in the future, Hehe..."
            scene 45-6 mayor 55-1 with Dissolve(0.5)
            md_1 "Mm... The fingers slide in so easily."
            play sound femmoan_2
            $ different_choice_menu = True
            $ EP15_Anim_Option = 1
            $ EP15_Anim_Speed = 1
            $ EP15_Mayor_Anim_Menu_Var_1 = False
            $ EP15_Mayor_Anim_Menu_Var_2 = False
            scene black
            play sound jerk loop
            show EP15_Mayor_Anim_2 with Dissolve(0.5)
            label EP15_Mayor_Anim_Menu_2_Label:
            a "Oh..."
            md_1 "Yess... That's a good asshole."
            a "Mh..."
            menu EP15_Mayor_Anim_Menu_1:
                "View 1":
                    hide EP15_Mayor_Anim_2
                    hide EP15_Mayor_Anim_2_Faster
                    hide EP15_Mayor_Anim_3
                    hide EP15_Mayor_Anim_3_Faster
                    $ EP15_Anim_Option = 1
                    if EP15_Anim_Speed == 1:
                        show EP15_Mayor_Anim_2 with Dissolve(0.5)
                    elif EP15_Anim_Speed == 2:
                        show EP15_Mayor_Anim_2_Faster with Dissolve(0.5)
                    jump EP15_Mayor_Anim_Menu_1
                "View 2":
                    hide EP15_Mayor_Anim_2
                    hide EP15_Mayor_Anim_2_Faster
                    hide EP15_Mayor_Anim_3
                    hide EP15_Mayor_Anim_3_Faster
                    $ EP15_Anim_Option = 2
                    if EP15_Anim_Speed == 1:
                        show EP15_Mayor_Anim_3 with Dissolve(0.5)
                    elif EP15_Anim_Speed == 2:
                        show EP15_Mayor_Anim_3_Faster with Dissolve(0.5)
                    jump EP15_Mayor_Anim_Menu_1
                "Slower":
                    hide EP15_Mayor_Anim_2
                    hide EP15_Mayor_Anim_2_Faster
                    hide EP15_Mayor_Anim_3
                    hide EP15_Mayor_Anim_3_Faster
                    $ EP15_Anim_Speed = 1
                    if EP15_Anim_Option == 1:
                        show EP15_Mayor_Anim_2 with Dissolve(0.5)
                    elif EP15_Anim_Option == 2:
                        show EP15_Mayor_Anim_3 with Dissolve(0.5)
                    jump EP15_Mayor_Anim_Menu_1
                "Faster":
                    hide EP15_Mayor_Anim_2
                    hide EP15_Mayor_Anim_2_Faster
                    hide EP15_Mayor_Anim_3
                    hide EP15_Mayor_Anim_3_Faster
                    $ EP15_Anim_Speed = 2
                    if EP15_Anim_Option == 1:
                        show EP15_Mayor_Anim_2_Faster with Dissolve(0.5)
                    elif EP15_Anim_Option == 2:
                        show EP15_Mayor_Anim_3_Faster with Dissolve(0.5)
                    jump EP15_Mayor_Anim_Menu_1
                "Continue":
                    $ different_choice_menu = False
                    pass
            stop sound
            scene 45-6 mayor 55-2 with Dissolve(0.5)
            a "Ah..."
            md_1 "Oh... Looks like you're enjoying it."
            a "Mh..."
            scene 45-6 mayor 55-3 with Dissolve(0.5)
            md_1 "Jeremy struck a gold mine with you."
            md_1 "I'm glad he decided to share..."
            md_1 "And not be a greedy bastard."
            scene 45-6 mayor 55-4 with Dissolve(0.5)
            md_1 "Yes. Yes..."
            scene 45-6 mayor 56 with Dissolve(0.5)
            md_1 "Alright... Time to put this back where it belongs."
            a "Ok..."
            md_1 "You've been good and submissive so far."
            md_1 "I think I'll sign the contract, yes. Hehe..."
            play sound jerk
            scene 45-6 mayor 57 with Dissolve(0.5)
            a "Ah..."
            md_1 "Very nice."
            scene 45-6 mayor 58 with Dissolve(0.5)
            a "Ohh..."
            a "Mh..."
            $ renpy.end_replay()
            scene black with Dissolve(0.5)
            pause
            scene 45-6 mayor 64-1 with Dissolve(0.5)
            md_1 "Well... That was very invigorating."
            md_1 "I can't wait to try those things on you. Hehe..."
            a "Ok... Yes, sir."
            md_1 "Trust me. If you submit, We'll get along nicely. And you'll get your rewards."
            a "Ok..."
            scene 45-6 mayor 65 with Dissolve(0.5)
            md_1 "Alright... It's time I got going."
            scene black with Dissolve(0.5)
            pause 1
            play sound door2
            scene 45-6 mayor 66 with Dissolve(0.5)
            md_1 "That was a good showcase indeed."
            md_1 "I'm glad Jeremy chose you."
            md_1 "No one would've done it better."
            scene 45-6 mayor 67 with Dissolve(0.5)
            md_1 "I will get going. Good to meet you."
            md_1 "I look forward to what the next time we meet will bring."
            a "Thank you, sir... Me too..."
            "Anna saw this as an opportunity... As a depraving one, but the Mayor promised rewards for her submissiveness."
            scene 45-6 mayor 68 with Dissolve(0.5)
            m1 "So... How did the meeting with the mayor go?"
            m1 "He looked pleased."
            a "Yeah..."
            scene 45-6 mayor 69 with Dissolve(0.5)
            a "Yeah, he was."
            a "I hope it helps us. As much as it helps him."
            m1 "An increased paycheck definitely wouldn't hurt."
            a "Yeah, alright. I'll get going."
            a "See you around, Madison."
            scene black with Dissolve(0.5)
            pause 1
        "I don't think it's such a good idea." if jeremySexContent == True:
            scene 45-6 mayor 15 with Dissolve(0.5)
            md_1 "How do you figure?"
            a "Well, if I know anything about Jeremy he's resourceful..."
            a "Since you're the mayor he'd want to get any dirt on you, that he could."
            a "He probably got cameras hidden here..."
            md_1 "Blackmail? Me?"
            md_1 "That's crazy..."
            a "Like I said, he's got pretty creative ideas... I know I've been caught in them a few times..."
            md_1 "Well, well... I see, I'll go and have a talk with him about this..."
            md_1 "He might've cost himself a pretty penny..."
            a "..."
            scene 45-6 mayor 65 with Dissolve(0.5)
            md_1 "Thanks for pointing it out."
            md_1 "He'll regret losing me as an ally."
            a "Uh... No problem."
            scene black with Dissolve(0.5)
            pause 1
        "I don't know what he promised you, but it ain't gonna happen..." if jeremySexContent == False:
            md_1 "What do you mean?"
            a "He never asks me to do such things..."
            a "And so I assume that I have the option to choose not to."
            a "If it costs us, so be it..."
            md_1 "Heh... That's rather unfortunate..."
            md_1 "But not totally unexpected..."
            md_1 "Alright... The basement is enough. But trust me, if you'd played ball, you'd get a bigger cut from the contract."
            scene 45-6 mayor 65 with Dissolve(0.5)
            md_1 "I will have to find other ways of enjoying this basement then."
            md_1 "Perhaps with other employees here."
            md_1 "Like Diane."
            a "Ehh... Ok."
            scene black with Dissolve(0.5)
            pause 1
    if DilanPornContent == True:
        jump EP15_Jeff
    else:
        jump EP15_Beach
label EP15_AfterWork_LogicGate:
    if EP15_var_6 == True and EP15_var_10 == True:
        $ EP15_var_12 = True
        $ log.addquest("Go to the Beach and meet up with the dudes.")
    return
label EP15_FBI:
    play music tranquility
    $ EP15_var_9 = True
    scene 45-7 home 1 with Dissolve(0.5)
    a "{i}...A shower would be good, after the beach...{/i}"
    scene 45-7 home 2 with Dissolve(0.5)
    pause 1
    play sound undress
    scene black with Dissolve(0.5)
    pause 1
    play sound shower_sound
    scene 45-7 home 3 with Dissolve(0.5)
    a "Ahh... That's good..."
    if timothySexContent == True:
        a "I should probably slowly get ready for the cosplay event with Timothy."
    else:
        a "I wonder what other adventures I'll get up to..."
    scene 45-7 home 4 with Dissolve(0.5)
    "Anna took her time, appreciating the warm water..."
    "Staying present... In the moment."
    scene 45-7 home 5 with Dissolve(0.5)
    pause 1
    scene 45-7 home 6 with Dissolve(0.5)
    a "Alright..."
    a "{i}...A shower always helps...{/i}"
    a "{i}...But the beach... Never get's old... Just sunbathing, just enjoying the moment...{/i}"
    play sound undress
    scene 45-7 home 7 with Dissolve(0.5)
    pause 1.5
    play sound chime1
    scene 45-7 home 8 with Dissolve(0.5)
    a "Huh?"
    scene black with Dissolve(0.5)
    pause 0.5
    play sound door2
    scene 45-7 home 9 with Dissolve(0.5)
    a "..."
    play sound door2
    play music tense2
    scene 45-7 home 10 with Dissolve(0.5)
    fbi1 "Hello, I'm sorry to intrude..."
    fbi1 "But If I'm not mistaken, you're Anna. Yes?"
    a "Yes?"
    scene 45-7 home 13 with Dissolve(0.5)
    fbi1 "I'm Special Agent Joseph Silva, FBI."
    a "What?"
    "Anna inspected the badge..."
    "Not like she knew if it was fake or not..."
    scene 45-7 home 12 with Dissolve(0.5)
    fbi1 "Once more, apologies for such a random visit..."
    fbi1 "Do you have a minute?"
    a "Uhh... Before I continue, I think I should contact my lawyer..."
    scene 45-7 home 11 with Dissolve(0.5)
    fbi1 "No need at all, you're not under investigation or anything like that..."
    fbi1 "Besides, we are the FBI, we don't solve small time crimes, we are after bigger fish."
    a "I really think I need a lawyer..."
    scene 45-7 home 14 with Dissolve(0.5)
    fbi1 "Do you really think we don't already have all the info we can get on you?"
    fbi1 "Trust me, if it was our goal to put you behind bars, a lawyer wouldn't help."
    fbi1 "No, I can promise that you are not a suspect, more so a person of interest in a case."
    a "Do tell?"
    scene 45-7 home 15 with Dissolve(0.5)
    fbi1 "Alright, for a while now, we've been tracking a sizeable and notorious crime ring that spans several cities."
    fbi1 "They've got their hands into multiple 'enterprises'. From drug trafficking and racket to murder and the worst, tax fraud."
    a "That's the worst?"
    fbi1 "That's a joke. You know how everyone's scared of the IRS? Well, those guys don't mess around. I'm here on behalf of a joint operation between the FBI, DEA, and the IRS."
    scene 45-7 home 14 with Dissolve(0.5)
    fbi1 "So. Are you familiar with one Sergey 'The Mad Bear'?"
    a "Uhh..."
    fbi1 "You are, that was rhetorical."
    fbi1 "Well, I will have you know that he's not the head of a small-scale operation, but rather a 'manager' of sorts in regards to one part of the operation."
    fbi1 "You see, he answers to others, he isn't the leader of the crime ring. It goes deeper than that."
    if EarlHelp == True:
        fbi1 "Now, he's behind bars, but the problem is to make him talk... He doesn't care at all about any threats we'd put on him."
        fbi1 "He's very loyal..."
    else:
        fbi1 "Now, he's missing, in connection to the murder of Detective Earl Mendoza."
        fbi1 "And currently, we've been unable to track him..."
    fbi1 "That's where you come in. I have it on good authority that you have access to his personal computer, correct?"
    scene 45-7 home 16 with Dissolve(0.5)
    a "I... Don't know... Perhaps?"
    fbi1 "That's good enough for me, you see, we'd do the leg work ourselves, but the moment the crime elements notice us snooping, they'll go underground."
    fbi1 "You are our ticket in. And since you've got access, you could get us the info required."
    fbi1 "Now, there is an additional aspect to all of this."
    fbi1 "We believe, that since Sergey's unavailable, the leadership is looking for a replacement."
    fbi1 "And someone to take responsibility. You are currently the only link, and we think that they are coming today, to the warehouse."
    a "Why don't you just arrest them, when they show up?"
    fbi1 "Like I said, those are not the main culprits. If we arrest the liaison, we'll lose any leverage that we have on the situation."
    scene 45-7 home 15 with Dissolve(0.5)
    fbi1 "As it stands, you're our leverage, you're our in, so to speak. And with a little bit of luck, we might land some valuable intel."
    fbi1 "I came here as a courtesy, rather than a choice. I'd say you don't have much."
    fbi1 "But if you cooperate willingly, you will be well rewarded."
    fbi1 "So, What I'd ask of you is, to head to the hideout and expect their arrival."
    fbi1 "Make a deal with them, become involved with them, whatever."
    fbi1 "Trust me, you'll be saving lives if you side with us."
    scene 45-7 home 16 with Dissolve(0.5)
    a "I..."
    scene 45-7 home 17 with Dissolve(0.5)
    fbi1 "That's all, consider your position carefully and please do what's right."
    fbi1 "Good luck. I will be in touch."
    play sound door2
    scene 45-7 home 18 with Dissolve(0.5)
    a "{i}...Well, that was unexpected...{/i}"
    a "{i}...He emphasized that I don't have much choice...{/i}"
    a "{i}...Like I ever do...{/i}"
    a "{i}...Alright, I should get ready...{/i}"
    play sound undress
    scene 45-7 home 20 with Dissolve(0.5)
    a "{i}...Damn..{/i}"
    a "{i}...I'd better not mess around with the FBI...{/i}"
    a "{i}...Should go to the warehouse... See what info I can dig up...{/i}"
    a "{i}...And wait for someone to come... That's a bit ominous...{/i}"
    a "{i}...The FBI agent knew a lot... Why wouldn't they just ambush them...{/i}"
    a "{i}...Whatever... Will see what's going on...{/i}"
    scene black with Dissolve(0.5)
    pause 1
    jump EP15_Mafia
label EP15_Mafia:
    play music tense2
    $ EP15_var_8 = True
    play ambient citytraffic
    scene 45-9 warehouse 1 with Dissolve(0.5)
    "As soon as Anna entered the rear entrance area she saw cars."
    "They were here already."
    a "{i}...Shit...{/i}"
    scene 45-9 warehouse 2 with Dissolve(0.5)
    a "{i}...Alright, gotta keep it cool...{/i}"
    a "{i}...At least Tyler's here... A friendly face... Sort of...{/i}"
    scene 45-9 warehouse 3 with Dissolve(0.5)
    wg1 "Hey, Anna..."
    wg1 "Uhh... We got some serious people here."
    wg1 "I don't know much, but I know that Sergey's involved with them."
    wg1 "They are inside, waiting on you, I suppose."
    scene 45-9 warehouse 4 with Dissolve(0.5)
    a "Don't worry. I got it all under control. I'll talk to them."
    wg1 "Sure, sure."
    wg1 "Sergey never told me about anything like this."
    a "It's uhh... Complicated, don't worry, you're all good."
    stop ambient fadeout 1
    scene black with Dissolve(0.5)
    pause 1
    play sound door2
    scene 45-9 warehouse 5 with Dissolve(0.5)
    gr1 "Ah. And Anna is also here."
    gr1 "Good."
    gr1 "A bit of a surprise, but no matter."
    scene 45-9 warehouse 6 with Dissolve(0.5)
    a "I just came here to keep tabs on the business and everything, since Sergey is unavailable."
    gr1 "Yes. I see. Well, the thing is."
    gr1 "We are aware of the situation."
    scene 45-9 warehouse 7 with Dissolve(0.5)
    gr1 "And that's why I'm here. to put things in their place."
    scene 45-9 warehouse 8 with Dissolve(0.5)
    gr1 "Come sit down. We got some stuff to discuss."
    a "Ok."
    play sound undress
    scene 45-9 warehouse 9 with Dissolve(0.5)
    gr1 "So. I know the details of Sergey's current predicament."
    if EarlHelp == True:
        gr1 "He's behind bars. locked up by one Detective Earl Mendoza."
        gr1 "And if he knows what's best for him, he'll keep his mouth shut."
        a "What do you mean?"
        gr1 "As of right now, Earl thinks he's caught the main guy."
        gr1 "If Sergey talks, he'll be dealt with in the prison."
    else:
        gr1 "He's got a lot of heat on him right now. Since he killed the Detective."
        gr1 "So he'll be out of the picture for a while."
        gr1 "Not involved in this city's activities anymore."
        a "Will I see him again?"
        gr1 "I don't know, depends on how fast the situation resolves."
    scene 45-9 warehouse 10 with Dissolve(0.5)
    a "Ok, But what does all of this have to do with me?"
    gr1 "I've been informed that you've got plenty of experience with administrative work."
    gr1 "Since you've been involved with them previously, I'd like for you to take over for now."
    a "Me? Really?"
    a "Do you trust me that much?"
    scene 45-9 warehouse 11 with Dissolve(0.5)
    gr1 "Trust you?"
    gr1 "Not at all."
    gr1 "Simply a bandaid, for now."
    gr1 "You'll also help us deal with another problem."
    a "Oh?"
    scene 45-9 warehouse 12 with Dissolve(0.5)
    gr1 "I don't know if you checked the numbers, but someone has been stealing from us."
    gr1 "Some motherfucker has been taking a cut, that he's not supposed to take."
    a "What?"
    a "How do you figure?"
    scene 45-9 warehouse 13 with Dissolve(0.5)
    crime1 "They've unloaded the cargo."
    gr1 "A MINUTE GODDAMN!"
    gr1 "I KNOW!"
    scene 45-9 warehouse 14 with Dissolve(0.5)
    gr1 "Anyway. We know this because we also got accountants, we also check the numbers."
    gr1 "And who ever thought that they could screw us, was very wrong."
    gr1 "It will be your responsiblity to find out who it was."
    gr1 "God help you, if you're involved in that in anyway."
    a "I'm... I'm not, I promise!"
    scene 45-9 warehouse 15 with Dissolve(0.5)
    gr1 "Good. It would be a shame to dispose of someone so..."
    gr1 "Precious."
    gr1 "One more thing."
    play sound jacketcloth
    scene 45-9 warehouse 16 with Dissolve(0.5)
    gr1 "Due to all these recent events, our operation has been slowed down here."
    gr1 "We've delivered a fair bit of cargo that you'll help distribute."
    gr1 "You'll have to call up some contacts, and get things going."
    gr1 "If you do all of these things, you'll have a bright future ahead of you."
    play sound cloth_sound1
    scene 45-9 warehouse 17 with Dissolve(0.5)
    a "I... Uh..."
    gr1 "Welcome to the family."
    a "Thanks?"
    gr1 "Hmph... I may be going easy on you because you're a woman, but don't cross us."
    scene 45-9 warehouse 18 with Dissolve(0.5)
    gr1 "I will be going. You do remember what we want from you, yes?"
    a "Take care of the administrative work... Find out who was stealing from you... Distribute the latest cargo."
    a "Sounds about right?"
    gr1 "Yes. Good."
    scene 45-9 warehouse 19 with Dissolve(0.5)
    gr1 "Good luck..."
    play sound door2
    scene 45-9 warehouse 20 with Dissolve(0.5)
    a "{i}...Fuck me...{/i}"
    a "{i}...How do I get myself in to these situations...{/i}"
    play sound door2
    scene 45-9 warehouse 21 with Dissolve(0.5)
    wg1 "Anna. Are you ok?"
    wg1 "Those guys, who were they? What did they want?"
    a "Oh boy..."
    a "A lot..."
    scene 45-9 warehouse 22 with Dissolve(0.5)
    a "Since Sergey's gone, things have stagnated..."
    a "Now they want to get things back the way they were."
    a "And they've put me in charge."
    wg1 "Alright, you're the new boss?"
    a "I guess..."
    scene 45-9 warehouse 23 with Dissolve(0.5)
    wg1 "Uhh... Ok. But I don't think I'll be able to handle things alone."
    a "No problem, I'll talk to Michael as well."
    wg1 "Oh... Ok."
    a "Anyway. I gotta go now... I'll be back sometime soon."
    wg1 "Got it."
    wg1 "I will await your arrival."
    scene black with Dissolve(0.5)
    if timothySexContent == True:
        jump EP15_Timothy_2
    else:
        jump EP15_Ending
    pause 1
label EP15_Timothy_2:
    $ EP15_var_7 = True
    play music chill_song_4
    play sound door2
    scene 45-8 timothy 1 with Dissolve(0.5)
    a "Hey, Timothy!"
    t "Anna! Good to see you!"
    a "You too!"
    play sound undress
    scene 45-8 timothy 2 with Dissolve(0.5)
    a "How are you doing?"
    scene 45-8 timothy 3 with Dissolve(0.5)
    t "Great! Looking forward to the event."
    t "And you?"
    a "I'm good. Kind of excited, heh."
    t "That's good. I'm glad you're here."
    scene 45-8 timothy 4 with Dissolve(0.5)
    a "So... How is it going with my outfit?"
    t "Uh... Yeah about that..."
    t "The company that I ordered from has sent me the wrong outfit."
    t "I received it today... No way we can get a new one before the event..."
    a "What do you mean?"
    t "It's totally not what I had in mind, this one's ALOT... um... Skimpier."
    scene 45-8 timothy 5 with Dissolve(0.5)
    a "Come on, Timothy. Don't worry..."
    a "Let's just check it out, maybe it's not that bad."
    t "Alright, It's just that I don't want to put you in an uncomfortable position."
    a "Don't worry, you won't."
    scene 45-8 timothy 6 with Dissolve(0.5)
    t "Ok... This way."
    scene 45-8 timothy 7 with Dissolve(0.5)
    t "So, Yeah. Like I said."
    t "It's pretty skimpy, the wrong version."
    a "Don't worry, let's try it on first. Then we'll see."
    scene 45-8 timothy 8 with Dissolve(0.5)
    t "Ok... You can change in my room."
    t "If you need some privacy."
    scene 45-8 timothy 9 with Dissolve(0.5)
    a "Don't worry, I got nothing to hide from you, heh."
    t "Oh... Hehe..."
    t "No problem."
    play sound undress
    scene black with Dissolve(0.5)
    pause 1
    scene 45-8 timothy 10 with Dissolve(0.5)
    a "So... Give me the costume."
    t "{b}*Gulp*{/b}"
    a "Hehe... You look very distracted. You ok?"
    "Anna knew what she was doing to Timothy, she liked to tease him."
    t "Yeah, yeah."
    t "Here's the outfit."
    play sound undress
    scene black with Dissolve(0.5)
    pause 1
    play sound jacketcloth
    scene 45-8 timothy 11 with Dissolve(0.5)
    t "Damn..."
    t "That is quite something..."
    t "It looks even better on you than on the model."
    a "Thank you, Timothy."
    t "So... What do you think?"
    a "I think it's pretty skimpy..."
    a "But I can wear it to the event, no problem."
    scene 45-8 timothy 12 with Dissolve(0.5)
    t "Really?"
    a "Yeah. Why not?"
    t "Uh... Just thought you'd be uncomfortable."
    a "Nonsense. You like it, right?"
    t "Yeah."
    a "Then I'll wear it."
    t "Niiice."
    a "Now your turn."
    scene 45-8 timothy 13 with Dissolve(0.5)
    t "Alright, I'll go to my room, and change real quick."
    t "Won't be long."
    scene 45-8 timothy 14 with Dissolve(0.5)
    a "No need. You can change here, like I did."
    t "Uhh..."
    t "Ok."
    play sound undress
    scene 45-8 timothy 15 with Dissolve(0.5)
    pause 1
    scene 45-8 timothy 16 with Dissolve(0.5)
    a "Don't be shy. I know what you're hiding there, heh."
    t "Heh... Thanks."
    scene 45-8 timothy 17 with Dissolve(0.5)
    a "Definitely would get checked out in the airport..."
    a "For carrying such a weapon."
    t "Oh. Hah. Thanks, Anna."
    t "You are very nice."
    scene 45-8 timothy 18 with Dissolve(0.5)
    t "Alright..."
    a "So, who are you supposed to be?"
    t "I'm a powerful Ancient Roman warrior Sulustus from the game series Chaos of Ancient Gods."
    a "Never heard."
    t "It's alright."
    scene 45-8 timothy 19 with Dissolve(0.5)
    t "How do I look?"
    a "Like an ancient warrior."
    a "Hehe... Who wins his battles with something in his pants."
    t "Haha..."
    a "By the way, who am I?"
    scene 45-8 timothy 20 with Dissolve(0.5)
    t "You are an ancient goddess called Acolyxa from another game series called Breaking Ascension."
    t "The main antagonist is trying to sever an Aether link that binds the worldly plane to the deity plane and stop anyone from ascending."
    t "Acolyxa and the main protagonist try to stop him."
    t "Quite interesting, actually."
    a "Wow. Nice."
    play sound undress
    scene 45-8 timothy 21 with Dissolve(0.5)
    a "I'll take the face mask off for now."
    t "Sure."
    t "Anyway, We're ready. Let's take a cab?"
    a "Alright."
    a "I'm kind of excited."
    t "Me too, heh."
    play sound door2
    scene black with Dissolve(0.5)
    pause 1
    stop music fadeout 1.5
    play sound car_sound1
    pause 3
    play ambient club_ambience_1
    scene 45-8 timothy 22 with Dissolve(0.5)
    a "Well, well."
    a "This place is quite packed."
    a "It doesn't look like a regular cosplay event."
    a "I mean, what I've seen on the internet."
    scene 45-8 timothy 23 with Dissolve(0.5)
    t "You're right, it's not. More like an underground kind of a thing."
    t "A lot of diehard fans of all kinds of games, comics, etc come here."
    t "To mingle, get drunk and stuff. heh."
    t "There's usually also some sort of an event or activity going on."
    scene 45-8 timothy 24 with Dissolve(0.5)
    a "Sounds like we've got something coming up heh."
    t "What do you mean?"
    a "The event."
    t "Yeah, I don't know what it is..."
    a "That's exciting!"
    scene 45-8 timothy 25 with Dissolve(0.5)
    ro3 "Timothy?"
    ro3 "Bro! What's up?!"
    scene 45-8 timothy 26 with Dissolve(0.5)
    t "Hey, Rob!"
    t "How you doing?"
    ro3 "Great, great!"
    ro3 "I'm keeping track if you've missed any cosplay events this year."
    t "I think I haven't, except the last time this event happened. Haha!"
    ro3 "Nice!"
    scene 45-8 timothy 27 with Dissolve(0.5)
    ro3 "Hello, Anna."
    a "Hey, Robert."
    ro3 "Great to see you. You doing good?"
    a "I am. you?"
    ro3 "Same, same! Life's great, haha!"
    ro3 "I didn't expect to see you here."
    scene 45-8 timothy 28 with Dissolve(0.5)
    a "Oh, you know. Timothy invited me. Thought it'd be fun."
    ro3 "Damn straight."
    ro3 "Good on him, right?"
    a "Brave. This place is pretty wild."
    ro3 "Oh you thought us Geeks don't like to party?"
    a "Well, maybe."
    scene 45-8 timothy 29 with Dissolve(0.5)
    ro3 "No worries. You'll see, this is one of those 'underground' cosplay events."
    ro3 "Real diehards come here to let off some steam."
    ro3 "Timothy and I come here as much as possible."
    ro3 "Guys! Let's get some drinks, Wohooo!!!"
    a "Alright, good idea."
    scene 45-8 timothy 30 with Dissolve(0.5)
    t "So. How's the crowd here today?"
    ro3 "Compared to last time? Wild, last time everyone was busy, a lot of people didn't make it."
    ro3 "Including you."
    t "Yeah... I was busy with some stuff."
    ro3 "No worries, good that you're here today."
    fe1 "Timothy?"
    scene 45-8 timothy 31 with Dissolve(0.5)
    t "Felicia? HEYYY!"
    t "Good to see you here!"
    play sound undress
    scene 45-8 timothy 32 with Dissolve(0.5)
    t "I thought you didn't come to these events."
    fe1 "You mean, Underground Sunicon?"
    fe1 "Usually don't, decided to swing by this time!"
    scene 45-8 timothy 33 with Dissolve(0.5)
    a "So... How do you two know each other?"
    a "Timothy's never told me about you."
    scene 45-8 timothy 34 with Dissolve(0.5)
    fe1 "Oh we usually attend these kinds of events."
    fe1 "Our friend groups aligned so that's how we met."
    fe1 "Actually through a friend of Roberts."
    fe1 "She isn't here today."
    scene 45-8 timothy 35 with Dissolve(0.5)
    fe1 "What about you?"
    fe1 "How do you two know each other?"
    scene 45-8 timothy 36 with Dissolve(0.5)
    a "Oh, we are colleagues from work."
    a "Been through a lot!"
    a "He invited me to this. I thought I'd join, try out something different."
    fe1 "Colleagues? Nice!"
    a "Well, maybe a bit more like colleagues with benefits, hehe..."
    fe1 "Sorry I didn't catch that."
    scene 45-8 timothy 37 with Dissolve(0.5)
    a "Nevermind, Hah."
    scene 45-8 timothy 38 with Dissolve(0.5)
    t "Uh.. Heh."
    scene 45-8 timothy 35 with Dissolve(0.5)
    fe1 "Well, it's great that you're trying out something like this."
    fe1 "It's a bit weird to outsiders, but we don't care."
    fe1 "It's our jam!"
    scene 45-8 timothy 37 with Dissolve(0.5)
    a "That's great, I don't judge. I actually like it, you kind of become a different character for an evening."
    fe1 "Exactly!"
    fe1 "Anyway, I'll go, I will greet some of my friends, we could get some drinks a bit later!"
    a "Definitely!"
    scene 45-8 timothy 39 with Dissolve(0.5)
    fe1 "See you around!"
    fe1 "Later, Timothy!"
    t "Bye!"
    scene 45-8 timothy 40 with Dissolve(0.5)
    a "Well, well. Timothy."
    a "I didn't know there was a girl..."
    t "What do you mean, nothing going on."
    a "Oh, heh... I saw how you embraced her."
    t "Uhh..."
    a "It's awesome!"
    t "I... I mean, we're just friends, she doesn't see me like anything more."
    scene 45-8 timothy 41 with Dissolve(0.5)
    ro3 "Total nonsense. I think she's just kind of reluctant..."
    ro3 "If Timothy was more straightforward and confident, she'd be all over him."
    a "Interesting... Well, the night ain't over yet."
    a "Let's see what we can do about it, eh?"
    scene 45-8 timothy 42 with Dissolve(0.5)
    t "Right... We were about to get some drinks, shall we?"
    t "I need something strong... All this is getting me a bit tensed up, haha!"
    a "Alright! Drinks! Woohoo!!"
    ro3 "Hell yeah!"
    scene black with Dissolve(0.5)
    "All three of them chug some shots and get on the dance floor."
    play ambient bar_ambience_1
    play music Party_Song_2
    scene 45-8 timothy 43 with Dissolve(0.5)
    a "Yeah!"
    a "This music is pretty good!"
    t "Come on, we can also hit some pretty dope tunes."
    a "Right, right!"
    ro3 "You gotta admit, this is pretty awesome!"
    a "Yeah, I didn't expect it to be!"
    scene 45-8 timothy 44 with Dissolve(0.5)
    ro3 "Anyway, How does it feel, Acolyxa?!"
    ro3 "The Goddess of Ascension!"
    a "Wha?"
    ro3 "I know the outfit! I know the game series!"
    ro3 "I played the shit out of it!"
    a "Haha! Well, being a goddess is pretty nice."
    scene 45-8 timothy 45 with Dissolve(0.5)
    t "Well, you're a goddess in and out of that costume!"
    a "Now, now. Don't get me too excited, Timothy. The evening has just begun!"
    t "Sorry!"
    a "Don't be! this is awesome!"
    scene 45-8 timothy 46 with Dissolve(0.5)
    "The girl, Felicia. She was pretty sure in her stance regarding Timothy... Up until now."
    "Seeing him with such a perfect woman as Anna..."
    "It made her rethink her choices..."
    "How could Timothy get such a girl to come with him to an event such as this..."
    "Perhaps there was more than meets the eye..."
    scene 45-8 timothy 47 with Dissolve(0.5)
    "Anna noticed her look... And she knew..."
    "She knew that Felicia had some thoughts, she recognized that look."
    "A look of jealousy and curiosity..."
    "A person questioning their own thoughts..."
    a "{i}...Hehe... I think she's interested...{/i}"
    scene 45-8 timothy 48 with Dissolve(0.5)
    a "I love how this outfit feels actually."
    t "It wasn't cheap, I'll tell you that much..."
    t "The quality should be good."
    scene 45-8 timothy 49 with Dissolve(0.5)
    a "Do you think you'll make a move on Felicia?"
    t "Uhh... I don't know..."
    a "But you seem interested in her."
    t "I... I just don't think she'd want to."
    a "Hehe... We might be able to change that."
    scene 45-8 timothy 50 with Dissolve(0.5)
    a "I feel the shots kicking in a bit hehe..."
    ro3 "Yeah... The alcohol here is pretty good."
    t "This is actually our go-to place, when we finally decide to go out and party."
    scene 45-8 timothy 51 with Dissolve(0.5)
    dj1 "WHAT! IS! UP PARTY PEOPLE!!!!!"
    dj1 "Your favorite DJ, DJ Gravity in DA HOUUUSEEEE!!!!"
    dj1 "MAKE SOME NOOISE!"
    dj1 "Well, begin the outfit showcase real SOOOON!"
    dj1 "Get them poses ready!!!"
    scene 45-8 timothy 52 with Dissolve(0.5)
    a "An outfit showcase?"
    t "It's one of the activities, they rotate them."
    t "I never participate in showcases."
    a "Why not?"
    t "I don't think anyone wants to see someone like me on the stage."
    a "Naah... We'll show them."
    scene 45-8 timothy 53 with Dissolve(0.5)
    ro3 "Come on, Timothy."
    ro3 "You and Anna can win this thing!"
    t "Heh... Alright, alright. I'll try!"
    stop ambient fadeout 1
    stop music fadeout 2
    pause 1
    play ambient club_ambience_1 fadein 1
    scene 45-8 timothy 54 with Dissolve(0.5)
    dj1 "Alright, so!"
    dj1 "You know the drill!"
    dj1 "Anyone who wants can come up and showcase their outfit!"
    dj1 "Best one will win a prize!"
    scene 45-8 timothy 55 with Dissolve(0.5)
    dj1 "Remember!"
    dj1 "It's not just the outfit, but also the poses! The grace and the confidence!"
    dj1 "So! Who'll be first?!"
    scene 45-8 timothy 56 with Dissolve(0.5)
    ro3 "The girl in front of me... She's so hot... Damn..."
    ro3 "I wanna do her so bad."
    a "Hehe... You're a horny one, eh?"
    ro3 "I always notice her here..."
    scene 45-8 timothy 57 with Dissolve(0.5)
    a "Have you talked to her before?"
    ro3 "No..."
    a "Well, then... Do as I and Timothy will. Take a chance!"
    dj1 "So! Who'll come here and show us their awesome outfit?!"
    scene 45-8 timothy 58 with Dissolve(0.5)
    ol1 "Me! ME!"
    dj1 "Alright, we got our first outfit!"
    dj1 "A brave girl we've all seen here time and time again."
    dj1 "OLIVIAAAAAAAAA!!!!!"
    scene 45-8 timothy 59 with Dissolve(0.5)
    dj1 "OH YEAH!"
    dj1 "Awesome outfit!"
    dj1 "I LOVEEEE ITTT!!!!!"
    dj1 "If I recall correctly, this is an outfit from a comic named Exorcism Falls!"
    dj1 "Make some noiiiisee for OLIVIAAAAAA!!!!"
    scene 45-8 timothy 60 with Dissolve(0.5)
    cr12 "WOHOOOO!!!!!"
    dj1 "That's riiight!"
    scene 45-8 timothy 61 with Dissolve(0.5)
    a "She's pretty. Nice outfit. Those shoes are beautiful."
    t "Yeah. People pay a pretty penny for such outfits."
    a "How much do I owe you?"
    t "Don't even mention it, heh."
    scene 45-8 timothy 62 with Dissolve(0.5)
    dj1 "Alriiight!"
    dj1 "Who's up next?"
    dj1 "We got a couple who are veterans here!"
    dj1 "LET'S GOOOO!!!!!"
    scene 45-8 timothy 63 with Dissolve(0.5)
    ro3 "That outfit is awesome!"
    ro3 "I've seen you around here many times."
    ol1 "Heh... Thanks."
    ro3 "I'm Robert."
    scene 45-8 timothy 64 with Dissolve(0.5)
    ol1 "I'm Olivia."
    ro3 "Very nice to make your acquaintance, Olivia."
    ro3 "Your outfits are always awesome. They are always from great comics or games."
    scene 45-8 timothy 65 with Dissolve(0.5)
    dj1 "Oh, YEAH!"
    dj1 "We got some moves with this couple!"
    dj1 "CRAZYYY PEOPLE!!!!!"
    dj1 "YEAHHH!"
    scene 45-8 timothy 66 with Dissolve(0.5)
    dj1 "YEEEEAAAHH!"
    dj1 "Crazy UP IN HERE!!!"
    scene 45-8 timothy 67 with Dissolve(0.5)
    t "So, These guys are veterans. They attend every single event they can."
    t "They even drive to other cities."
    t "Pretty hardcore, if you ask me."
    scene 45-8 timothy 68 with Dissolve(0.5)
    a "Oh really?"
    a "How about we go next?"
    t "Uhh..."
    t "Wha?"
    scene 45-8 timothy 69 with Dissolve(0.5)
    dj1 "Just don't go too crazy!"
    dj1 "This is a 'family' friendly event. HAHAAA!!!!"
    dj1 "LOVING THE MOOVES!"
    scene 45-8 timothy 70 with Dissolve(0.5)
    a1 "So. What are we doing here?"
    a1 "Everyone looks dressed up, besides us."
    ash "Yeah... Kind of missed that part."
    ash "I'm just pulling my friend out of the house, you know?"
    scene 45-8 timothy 71 with Dissolve(0.5)
    "Anna looked over and noticed Ashley with Andrew."
    a "{i}...What... They're here...{/i}"
    scene 45-8 timothy 72 with Dissolve(0.5)
    a "{i}...Andrew can't see me like this...{/i}"
    a "{i}...Shit...{/i}"
    scene 45-8 timothy 72-1 with Dissolve(0.5)
    ash "Let's get some drinks?"
    a1 "Sure. I'm parched."
    ash "Alright!"
    scene 45-8 timothy 73 with Dissolve(0.5)
    a "So. How about it?"
    t "What do you mean?"
    a "Let's go and give them a show?"
    t "Now??"
    a "Yes, now! hehe."
    play sound undress
    scene 45-8 timothy 74 with Dissolve(0.5)
    a "I'll put this on, for a full outfit."
    t "Ok."
    a "Ready?"
    t "Uhh... Sure!"
    t "Don't worry, we got this!"
    scene 45-8 timothy 75 with Dissolve(0.5)
    dj1 "Alrighty!"
    dj1 "WHO IS NEXT???!!!"
    t "WE!"
    dj1 "COME ON UP ON THE STAGE! SHOW US WHAT YOU GOOOOOOTTT!!!"
    scene 45-8 timothy 76 with Dissolve(0.5)
    a "Come on. Let's Go!"
    t "I'm coming, I'm coming, heh."
    scene 45-8 timothy 77 with Dissolve(0.5)
    dj1 "So... These outfits... Awesome!"
    dj1 "Especially the girl!"
    dj1 "Also, I've seen you around here but you've never come up on the stage."
    dj1 "FIRST TIME! LET'S GOOO!!!!!!"
    scene 45-8 timothy 78 with Dissolve(0.5)
    dj1 "I mean, god damn we've got a competitor this time."
    dj1 "You've brought out the big guns, eh?!"
    dj1 "AWESOME EVENIIINNGG!!!"
    dj1 "ALRIGHT GIVE US A SHOW!"
    scene 45-8 timothy 79 with Dissolve(0.5)
    dj1 "MAKE SOME NOISE FOR THIS SHOWCAAAAAASEEE!!!"
    a "Alright, what do we do?"
    t "Oh... Uh... We just pose some."
    a "I can do that. Heh."
    scene 45-8 timothy 80 with Dissolve(0.5)
    a1 "Hmm... That girl looks very similar to Anna, but it couldn't be, right?"
    "Ashley already knew it was Anna..."
    ash "Nope... That's definitely not her. Don't worry."
    scene 45-8 timothy 82 with Dissolve(0.5)
    a "{i}...I really hope he doesn't realize it's me...{/i}"
    a "{i}...That would be very awkward...{/i}"
    scene 45-8 timothy 83 with Dissolve(0.5)
    dj1 "OH YEAHHH!!!"
    dj1 "If I recall correctly, The girl's outfit is that of the goddess Acolyxa from Breaking Ascension!"
    dj1 "And the dude's outfit is that of the Ancient Roman super Warrior Sulustus!"
    dj1 "AWESOME CHOICEEEEES! YEAHH!!!"
    scene 45-8 timothy 84 with Dissolve(0.5)
    dj1 "YEAH!"
    dj1 "SHOW US THEM GUNS!"
    scene 45-8 timothy 85 with Dissolve(0.5)
    t "WOHOOO!!!"
    dj1 "MAKES SOME NOISSEEE FOR THESE TWO!"
    scene 45-8 timothy 86 with Dissolve(0.5)
    "Both Anna and Timothy were having a lot of fun."
    "Anna loved that Timothy was letting go and just enjoying the moment."
    scene 45-8 timothy 87 with Dissolve(0.5)
    ro3 "YEAH!"
    scene 45-8 timothy 88 with Dissolve(0.5)
    a "Come on, let's show them some more."
    t "What you got in mind?"
    a "Just follow my lead, heh."
    scene 45-8 timothy 89 with Dissolve(0.5)
    dj1 "OH DAAAMN!"
    dj1 "It's getting HOT UP IN HEEEREEE!"
    dj1 "THESE TWO ARE ON FIRE!"
    scene 45-8 timothy 90 with Dissolve(0.5)
    a "HAHA!"
    a "Take off my cape, let's spice things up!"
    t "Ok! Heh."
    play sound undress
    scene 45-8 timothy 91 with Dissolve(0.5)
    a "YEAH THAT'S GOOD!"
    scene 45-8 timothy 92 with Dissolve(0.5)
    a "AND NOW LIKE THIS!"
    t "YEAH! HAHA!!!"
    scene 45-8 timothy 93 with Dissolve(0.5)
    dj1 "OH WOW! THESE TWO ARE IN HEAT!"
    dj1 "DON'T GET TOO CRAZY!!!"
    scene 45-8 timothy 94 with Dissolve(0.5)
    t "THIS. IS. AWESOME!"
    a "I know. Hehe... I'm glad you like it!"
    scene 45-8 timothy 96 with Dissolve(0.5)
    t "WOW!"
    a "Like this!"
    dj1 "NIIIICE!"
    scene 45-8 timothy 97 with Dissolve(0.5)
    dj1 "THESE GUYS ARE VERY CONVINCING!"
    scene 45-8 timothy 97-2 with Dissolve(0.5)
    t "WHA?"
    scene 45-8 timothy 97-3 with Dissolve(0.5)
    a "You like the view, Timothy?"
    t "Heh... I really do!"
    scene 45-8 timothy 97-4 with Dissolve(0.5)
    dj1 "ALRIGHT, ALRIGHT!"
    dj1 "YOU GOT US CONVINCED!!!"
    dj1 "YOU WIIN. GETTING TOO CRAZY IN HERE!"
    dj1 "DAAAMN!"
    scene 45-8 timothy 97-5 with Dissolve(0.5)
    dj1 "WE GOT WINNERS!!!"
    dj1 "CONGRATULATIONS!"
    a "WOHOOO!!!"
    play sound surprise
    scene 45-8 timothy 98 with Dissolve(0.5)
    "Anna jumped on Timothy when she heard they'd won."
    a "NIIICE!"
    scene 45-8 timothy 99 with Dissolve(0.5)
    a1 "Some crazy people..."
    ash "Indeed... Heh..."
    scene 45-8 timothy 101 with Dissolve(0.5)
    t "Alright, Maybe jump off..."
    t "I'm starting to get a boner... Heh..."
    a "Oh... Sorry..."
    t "No problem... I just don't want everyone to see my cock..."
    a "I'd love to see it."
    scene 45-8 timothy 102 with Dissolve(0.5)
    dj1 "Congrats on winning tonight's outfit showcase!"
    dj1 "You'll get your award afterward!"
    a "Thank you!"
    scene 45-8 timothy 103 with Dissolve(0.5)
    t "Thanks for doing this with me."
    a "I wouldn't have it any other way."
    a "Let's go. I need to calm down a bit, Heh."
    scene 45-8 timothy 104 with Dissolve(0.5)
    ol1 "Congrats on the win!"
    ol1 "You're a first-timer, but I've never seen someone look so good in an outfit."
    scene 45-8 timothy 105 with Dissolve(0.5)
    a "Thanks! But you also look great!"
    ol1 "Thank you, Hah."
    scene 45-8 timothy 106 with Dissolve(0.5)
    ro3 "That was quite the show you put on there."
    a "Yeah. I think it was great."
    scene 45-8 timothy 107 with Dissolve(0.5)
    t "It was AWESOME!"
    t "The moves Anna had. I barely kept up."
    ro3 "Haha... You two are crazy people, awesome!"
    t "By the way, I gotta run to the toilet. Been keeping it in for a while."
    a "Alright, see you soon."
    scene 45-8 timothy 108 with Dissolve(0.5)
    ol1 "Hey, how about we go dance?"
    ol1 "Now that the activity is over, I really wanna enjoy the beats."
    scene 45-8 timothy 109 with Dissolve(0.5)
    ro3 "I'm game!"
    a "Yeah, let's do it!"
    scene 45-8 timothy 110 with Dissolve(0.5)
    fe1 "Anna. Wait..."
    fe1 "I wanted to talk to you."
    scene 45-8 timothy 111 with Dissolve(0.5)
    a "Hey, Felicia. Good to see you."
    a "Yeah, what's up?"
    a "You guys go ahead, I'll join you shortly."
    scene 45-8 timothy 112 with Dissolve(0.5)
    fe1 "So, Congrats on winning the showcase."
    fe1 "You both really worked it on the stage..."
    fe1 "I was just uh... Wondering. Are you both just coworkers?"
    scene 45-8 timothy 113 with Dissolve(0.5)
    a "What do you mean?"
    fe1 "Well... Are you both, like... Seeing each other?"
    a "Like a couple?"
    fe1 "Yeah."
    scene 45-8 timothy 114 with Dissolve(0.5)
    a "No... I wouldn't say that Heh..."
    a "But we do some stuff together."
    fe1 "Eh... What kind of stuff?"
    scene 45-8 timothy 115 with Dissolve(0.5)
    fe1 "What I mean, is... Are you like exclusive?"
    a "Haha... Looks like you like him afterall."
    fe1 "Well... Yeah... But like..."
    scene 45-8 timothy 116 with Dissolve(0.5)
    "Anna noticed Andrews's eyes wandering..."
    "He was still unsure if it was or wasn't her."
    "So he was trying to figure it out."
    scene 45-8 timothy 117 with Dissolve(0.5)
    a "{i}...Shit...{/i}"
    a "Listen... How about we talk somewhere... More private, eh?"
    scene 45-8 timothy 118 with Dissolve(0.5)
    a "Come with me... Heh."
    fe1 "What?"
    fe1 "Where are we going? Haha... You are fun."
    scene 45-8 timothy 119 with Dissolve(0.5)
    a "Don't worry about it. Just come with me."
    a "I'll answer all your questions about Timothy."
    a "Trust me... He's got a BIIIIG personality. If you know what I mean."
    fe1 "Wow, Really?"
    a "just come."
    $ renpy.music.set_volume (0.2, 1, "ambient")
    scene black with Dissolve(0.5)
    pause 1
    play sound door2
    scene 45-8 timothy 121 with Dissolve(0.5)
    fe1 "What are we doing here?"
    a "Oh Timothyyy."
    a "Where are you?"
    scene 45-8 timothy 122 with Dissolve(0.5)
    t "{i}...Huh?... Anna?...{/i}"
    t "Who is it?"
    scene 45-8 timothy 123 with Dissolve(0.5)
    a "Just two girls who are a bit lost. In need of your guidance."
    scene 45-8 timothy 124 with Dissolve(0.5)
    a "Could you help us out?"
    t "Uhh..."
    play sound door2
    scene 45-8 timothy 125 with Dissolve(0.5)
    t "Yeah? What's up?"
    a "There is a problem we both need help with."
    scene 45-8 timothy 126 with Dissolve(0.5)
    a "You see, Felicia here... She's curious about something."
    scene 45-8 timothy 127 with Dissolve(0.5)
    t "Whaaa?"
    a "And I thought I'd help her out with her curiosity."
    fe1 "Wha? No... I mean..."
    a "Don't worry too much, heh."
    a "May we come in?"
    fe1 "I don't... Think it's appropriate..."
    fe1 "I mean... Maybe some place else?"
    play sound surprise2
    scene 45-8 timothy 128 with Dissolve(0.5)
    a "Oh. Someone's coming... Let's get in fast."
    fe1 "OH!"
    play sound surprise
    scene 45-8 timothy 129 with Dissolve(0.5)
    fe1 "Waiittt... hah..."
    a "No time! wouldn't want to be seen in the men's toilets."
    play sound door2
    scene 45-8 timothy 130 with Dissolve(0.5)
    t "So... Uh... What now?"
    stop ambient fadeout 2
    scene black with Dissolve(2)
    pause 2
label EP15_Ending:
    jump EP16_Begin
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
