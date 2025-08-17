

define ms = Character("Mila {size=25}(thoughts)", image="mila", color=u'#df0e8f', what_italic=True)
define m = Character("Mila", image="mila", color=u'#df0e8f')
define p = Character("Paul", image="paul", color=u'#1e7316')
define l = Character("Liz", color=u'#a8b9bf')
define ls = Character("Liz {size=25}(thoughts)", color=u'#a8b9bf')
define n = Character("")
define bob_unknown = Character("???")
define bob = Character("Bob", color=u'#0321a7')
define d = Character("Dick")
define Courier = Character("Courier")
define ps = Character("Paul (thoughts)", color=u'#1e7316')
define k = Character("Kira", image="kiki", color=u'#F5F5DC')

define l_translation1 = Character("Liz", color=u'#a8b9bf', what_textshader="reverse_typewriter", slow=True, what_slow_cps=translation_shader_korean_cps)
define l_translation2 = Character("", what_textshader="slow_typewriter", slow=True, what_slow_cps=translation_shader_cps)
define Kim_translation1 = Character("Kim", what_textshader="reverse_typewriter", slow=True, what_slow_cps=translation_shader_korean_cps)
define Kim_translation2 = Character("", what_textshader="slow_typewriter", slow=True, what_slow_cps=translation_shader_cps)
define nobody_translation1 = Character("???", what_textshader="reverse_typewriter", slow=True, what_slow_cps=translation_shader_korean_cps)
define nobody_translation2 = Character("", what_textshader="slow_typewriter", slow=True, what_slow_cps=translation_shader_cps)


define ma = Character("Mila", kind=nvl, image="mila", callback=Phone_SendSound)
define md = Character("Mila", kind=nvl, image="mila", callback=Phone_SendSound)
define pm = Character("Paul (husband)", kind=nvl, callback=Phone_ReceiveSound)
define dm = Character("Dick82", kind=nvl, callback=Phone_ReceiveSound)
define bob_message = Character("Bob", kind=nvl, callback=Phone_ReceiveSound)


define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)


default paul_took_initiative = False
default paul_touch_ass = False
default mila_was_in_the_room = False
default bday_sub = True
default bob_love = 0


default mila_dom = 0

default dom = 0

default bday_bobs_slut = False

label start:
scene bg restricted
"Special thanks to {a=https://f95zone.to/threads/experienced-proofreader-i-can-help-you-with-your-game.155643/}Saint Blackmoor{/a} for editing and proofreading this game"
menu:
    "If you are less than 18 years old, please close this game"
    "Let me in, I am 18+":
        jump start2
    "I am not 18+":

        jump end

label start2:
scene bg mila_first with dissolve

ms "How long ago did we meet? {w}Back in school, fifteen years ago."
ms "Remembering those times is so pleasant... {w}Everything was so exciting and vibrant back then."
ms "My life with Paul started like a fairytale that I always dreamed of living."
scene bg wedding with dissolve
ms "“They lived happily ever after” - a story I dreamed of as a child. {w}My prince on a white horse gave me happiness."
ms "My life was full of fun and joy. {w}And it seemed like everything was just perfect. {w}Paul really is a prince. {w}He's handsome, smart, and can take care of me."
ms "But something has changed recently. {w}Everything is so good and sweet that there's nothing to gossip about with my friends. {w}Everything is so good... {w}That is the only thought that remains in my head..."
scene wedding_bw with dissolve
ms "Happiness...{w} is boring."
ms "Not that I want any drama or trouble... {w}But this level of care and love that Paul gives me... {w}This trust he shows me... {w}Makes me want...{w} things..."
scene bathroom_start_worried_steam with fade
show hand_sprite at center:
    xpos 0.7
    easeout 0.5 xpos 0.166
pause 0.7
hide hand_sprite
scene bathroom_start_worried with dissolve
ms "Things that I don't want to say out loud."
ms "Things that I don't want to even think about."
ms "Maybe I don't deserve his faith and trust."
ms "Because faith{w} is a lie."
ms "And trust is pain that you allow others to inflict on you."
scene bathroom_start_worried_2 with dissolve
ms "And maybe that's what he wants?"
ms "Maybe it sounds selfish, but I want more. {w}I want more adventure, more passion, more freedom."
scene bathroom_start_sad with dissolve
ms "I love Paul, but sometimes it seems like he doesn't understand me. {w}He cares for me so much that I start to feel protected, like in a golden cage."
ms "And I don't know what to do. {w}Maybe I need to talk to him, but I'm afraid of his reaction."
ms "All of this sounds so silly. {w}I should be happy with what I have. {w}But I can't help myself. I want more. I want to feel alive."
scene bathroom_start_naughty with dissolve
ms "These thoughts consume me. {w}Especially when the routine becomes so boring that my mind starts hiding reality from me."
ms "It sends me into a world of fantasies. {w}A world where I don't have to be a good girl. {w}A world where I'm not a queen. Where I don't have to make any decisions."
scene bathroom_start_naughty_2 with dissolve
ms "I'm someone much worse. Someone... {w}different."
ms "Someone who never gets tired of talking right after greeting. {w}Someone who doesn't feel disgusted by attention, but instead craves it."
ms "Someone who knows how to enjoy life and strives for it."
scene bathroom_start_sad_2 with dissolve
ms "Someone who is not me."
stop music

play sound "vibro.mp3"
scene bg apartments with dissolve
show mila camisole_and_shorts_surprised at center:
    xpos 0.6
ms "I jumped, coming out of my thoughts."
pm "How are you, sunshine?"
ms "..."
show mila camisole_and_shorts_irritated
ms "Haaaa..."
show mila camisole_and_shorts_sad_looking_aside
ms "I don't want to answer. If I tell the truth, he'll start squawking and whining.{w} He'll probably suggest me to see a therapist."
ms "I don't want to solve my problems.{w} I don't want to solve anything at all."
ms "My interests are drifting further and further away from normal."
ms "At first, I read romance novels and imagined myself as the heroine, caught up in a whirlwind of events."
ms "But over time, the stories that interested me became more and more twisted and erotic."
show mila camisole_and_shorts_naughty
ms "Then I read a famous fanfic and tried to imagine myself as a submissive.{w} A slave."
ms "And this idea fascinated me so much that I registered on a dating site for like-minded people."
ms "It turned out there were many like me.{w} It was harder to find someone who could and knew how to dominate than those who wanted to submit."
play sound "vibro.mp3"
pm "Are you busy?"
show mila camisole_and_shorts_sad_looking_aside
ms "I never dared to tell Paul about this. Our sex life was sickly vanilla."
ms "He didn't want to experiment, and I was afraid to show him the wrong side of me, the one he married. Afraid of seeming perverted."
ms "How do I tell him about this?"
ms "Especially because he is always busy..."
play sound "vibro.mp3"
pm "I'll be working late today."
show mila camisole_and_shorts_irritated
m "*Sigh*"
show mila camisole_and_shorts_embarassed
ms "So that's why I opened up my true self \"there\". On a forum with pages, black just as my desires."
nvl clear
dm "Write your measurements and weight."
show mila camisole_and_shorts_irritated_2
ms "That was the first thing Dick wrote to me. No \"hello\", no \"what's your name\", no \"what are you looking for on this site\"."
ms "I don't know what made me answer this arrogant and impudent message. But something in his tone made me answer."
md "Why?"
dm "I want to know."
show mila camisole_and_shorts_smirk
md "And I want a million dollars and a helicopter."
dm "You won't get them on this site."
md "No?"
dm "No. And you came here not for that."
show mila camisole_and_shorts_naughty
ms "Something hit my heart. I stared at the screen and waited. Waited for him to say what I didn't want to hear."
dm "You came here because you want someone to see the real you."
show mila camisole_and_shorts_naughty_surprised
ms "My heart was pounding like crazy. A stranger on the other side of the screen knew more about me than my husband, who had known me for over ten years."
dm "I want to know. I want to see you. The real you. In all your beauty and ugliness, dirtiness and purity."
ms "..."
show mila camisole_and_shorts_thinking
ms "I hesitated for a few more minutes."
ms "For some reason, it seemed to me that he was waiting. Waiting for my answer with tension."
ms "The feelings were such that it felt like I was standing in front of him. And his gaze was devouring my body. Watching every muscle movement on my face."
show mila camisole_and_shorts_embarassed2
md "My weight is 54 kilograms..."
dm "Oh, great, what a cutie!"
show mila camisole_and_shorts_shy_smile
ms "I smiled."
dm "How old are you?"
md "I'm thirty-two."
dm "Married?"
show mila camisole_and_shorts_embarassed
ms "I didn't like that I hesitated before answering as if I wanted to say \"No\".{w} But after all, my fingers still tapped on the screen."
md "Yes."
dm "Haha. So you're cheating on him?"
show mila camisole_and_shorts_irritated_2
md "No!"
ms "His question made me angry. I never would!.."
dm "Haha. Just planning to? Got it, got it."
show mila camisole_and_shorts_angry
ms "How dare he?"
ms "I'm not planning anything!"
ms "I'm just experimenting."
show mila camisole_and_shorts_embarassed2
ms "A little bit..."
dm "What's your bra size?"
show mila camisole_and_shorts_sad_looking_aside
ms "Do I really have to answer that?"
ms "Why am I even talking to him?"
md "I'm an A+ cup."
show mila camisole_and_shorts_embarassed
ms "Aaaand {w}I answered."
dm "A+?"
dm "Is that a way of saying you have no boobs, but you're trying really hard to stuff them in a bra?"
show mila camisole_and_shorts_irritated_2
ms "Oh, shut up!"
dm "Send me a selfie."
show mila camisole_and_shorts_embarassed2
ms "My heart started pounding like crazy again.{w} This is dangerous."
ms "If I do this, there's no turning back.{w} If I do this, everyone might find out who I really am."
ms "They'll point fingers."
ms "Laugh behind my back."
ms "I'll never be able to wash it out of my life."
ms "..."
show mila camisole_and_shorts_biting_lips
ms "..."
ms "..."
show mila camisole_and_shorts_embarassed2
md "I don't wanna"
dm "How else will I know you're not fake?"
dm "Maybe you're a fat sweaty guy who likes to pretend he has a cheating wife?"
show mila camisole_and_shorts_angry
md "I'm not a guy."
dm "Prove it."
show mila camisole_and_shorts_naughty
ms "I lowered my hand and touched myself.{w} My pussy was wet.{w} The pressure and demand were turning me on.{w} I liked it, liked it more than anything else."


menu:
    "I should stop here ({color=#ad9546}\"Loyal\"{/color} / {color=#c57d43}\"Polyamorus (harem)\"{/color} routes)":
        jump Loyal
    "No harm if nobody knows... ({color=#d32020}Cheating{/color} / {color=#b0308d}Sharing{/color} routes)":

        jump NTR_Netorase


label NTR_Netorase:
show mila camisole_and_shorts_shy_smile
md "Do you promise not to post it anywhere?"
dm "Yes."
show mila camisole_and_shorts_embarassed
md "Wait."
ms "My heart was pounding in my temples. I took a long time to choose the angle. Redid the photo several times until I finally decided, putting on a mask on my face first."
play sound "shot.mp3"
show mila camisole_and_shorts_shy_smile
ms "..."
show dick_selfie1x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "{image=dick/Selfies/dick_selfie1.webp}"
hide dick_selfie1x
md "Here it is."
dm "Well, you are a cutie."
ms "Not that I was particularly happy with those compliments."
dm "And you have no boobs."
show mila camisole_and_shorts_angry
ms "?!"
ms "Just because I don't have huge bazongas doesn't mean I have no tits."
show mila camisole_and_shorts_naughty_surprised
dm "But I'd still like to grab them."
show mila camisole_and_shorts_shy_smile
ms "Asshole..."
dm "Don't cover your face anymore."
show mila camisole_and_shorts_embarassed
ms "Sure, keep dreaming."
ms "Why did you even think I would send you anything?"
dm "I like you. I want to play with you, girl."
show mila camisole_and_shorts_embarassed2
ms "What does he mean?"
dm "How's your day going?"
show mila camisole_and_shorts_sad_looking_aside
md "I wake up, do my things, and go to sleep."
dm "Wow, that's probably the most detailed description of a daily routine I've ever seen! 😂"
md "Sorry, I'm not really good with introductions. What do you want to know?"
dm "Is there anything in your life that brings you joy?"
show mila camisole_and_shorts_naughty_surprised
ms "I was lost for words and didn't know how to answer."
dm "Is there something you can get lost in and not notice the time passing? Something you can talk about endlessly if asked?"
show mila camisole_and_shorts_sad_looking_aside
md "I don't know."
md "I like sewing."
md "I guess..."
dm "Sewing?"
show mila camisole_and_shorts_shy_smile
md "Yeah."
md "I can spend hours choosing a pattern, drawing a design, looking for fabrics, and preparing patterns."
md "I have my own mannequin, a machine with an overlock, and even a Japanese semi-automatic knitting machine."
md "I dedicate all my free time to this."
show mila camisole_and_shorts_grin3
md "For example, I'm almost done with a blouse now."
md "I just need to resew the sleeves and sew on the buttons."
md "This fabric is not easy to work with, though. "
md "It's so thin that it tears if you sew with a too-small stitch, but if you use a larger one, it leaves puckers."
dm "I see"
show mila camisole_and_shorts_embarassed3
ms "I stopped myself. Phew, that was close. Who would be interested in listening to me talk about sewing?"
show mila camisole_and_shorts_embarassed2
ms "I'm such an idiot."
show mila camisole_and_shorts_sad_looking_aside
md "I'm Sorry"
dm "For what?"
show mila camisole_and_shorts_sad_looking_down
md "You're probably bored with me."
md "I talk too much, don't I?"
show mila camisole_and_shorts_worried
ms "Why isn't he responding?"
ms "I started typing a message and then erased it again because I wasn't sure what to say in this situation."
ms "And why do I even want to say anything?"
ms "..."
show mila camisole_and_shorts_irritated_2
ms "To hell with it"
ms "I tried to distract myself and do some cleaning, but my thoughts kept returning to this conversation."
ms "I wanted to put my phone away, but I opened the chat again and stared at my last message."
show mila camisole_and_shorts_shy
ms "My breathing quickened. I knew I hadn't done anything wrong, but..."
ms "I wanted to beg for forgiveness."
show mila camisole_and_shorts_embarassed
ms "I wanted to feel humiliated."
ms "I wanted someone to punish me for my stupid thoughts."
show mila camisole_and_shorts_sad_looking_aside
md "Did I do something wrong?"
ms "His status flashed, he read the message but didn't reply."
show mila camisole_and_shorts_embarassed2
ms "I swallowed. My face was burning with shame, and there was a hot, itchy lump in my stomach."
md "Can I somehow make up for my mistake?"
dm "Get on your knees and take a selfie if you want to apologize."
show mila camisole_and_shorts_angry
ms "Apologize?{w} Apologize for what?"
ms "I've done nothing wrong"
show mila camisole_and_shorts_shy
ms "But..."
ms "I suggested it myself, didn't I?"
ms "I slowly knelt down and started adjusting the angle."
show mila camisole_and_shorts_naughty
ms "He wanted a photo with my face...but is it worth it?"
ms "If someone finds out, I'll have problems."
show mila camisole_and_shorts_biting_lips
ms "The more I thought about it, the more I wanted to do it."
ms "And the more I wanted to do it, the more aroused I became."
play sound "shot.mp3"
ms "..."
show dick_selfie2x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "{image=dick/Selfies/dick_selfie2.webp}"
hide dick_selfie2x
show mila camisole_and_shorts_shy_smile
dm "Good girl."
dm "I was just busy, you didn't have to apologize."
show mila camisole_and_shorts_surprised
dm "But your actions show great potential."
ms "I fell onto the bed and pressed my face into the pillow."
show mila camisole_and_shorts_hiding_face
ms "AAAA"
ms "I am an idiot!"
play sound "vibro.mp3"
dm "Still..."
dm "If you cover your face with a mask one more time - it's over"
show mila camisole_and_shorts_embarassed2
ms "..."
dm "Understood?"
ms "..."
show mila camisole_and_shorts_biting_lips
ms "Am I actually considering this?..."
md "Yes"
"..."
show mila camisole_and_shorts_shy_smile
dm "Good"
"..."
dm "What don't you like about married life?"
show mila camisole_and_shorts_worried
md "I didn't say I don't like it."
dm "But you're here. There must be a reason for that."
show mila camisole_and_shorts_thinking
ms "I didn't know what to say."
dm "There's something in strangers that even the closest friends don't have - the ability to openly talk about anything."
show mila camisole_and_shorts_shy
dm "It's like talking to a therapist."
dm "Only better."
dm "It's free."
dm "He doesn't satisfy you sexually?"
show mila camisole_and_shorts_sad_looking_down
md "No"
md "Everything is good."
ms "I didn't like that I hesitated before typing it"
dm "But is he doing something wrong?"
show mila camisole_and_shorts_embarassed
ms "I blushed."
ms "Talking about it seemed shameful."
ms "Unpleasant."
ms "Wrong."
ms "Previous me would never say it out loud."
show mila camisole_and_shorts_shy_smile
ms "But now I felt like a different person."
show mila camisole_and_shorts_embarassed2
md "Yes..."
md "Maybe..."
dm "Don't you like his size?"
show mila camisole_and_shorts_naughty_surprised
md "What do you mean?"
show mila camisole_and_shorts_embarassed3
md "Oh..."
show mila camisole_and_shorts_embarassed
ms "I blushed"
md "I see..."
md "No, everything's fine."
show mila camisole_and_shorts_embarassed2
md "Maybe."
md "I don't know."
dm "Have you ever tried other penises?"
show mila camisole_and_shorts_angry
md "Of course not!"
dm "How about toys?"
show mila camisole_and_shorts_embarassed
ms "Um..."
md "Deodorant tube..."
dm "I would laugh if it wasn't so pitiful..."
dm "What do you fantasize about?"
show mila camisole_and_shorts_thinking
ms "Why he is changing themes so fast?"
show mila camisole_and_shorts_giggle
md "Oh, I'd love to visit France!"
md "Walk along the narrow streets of old Europe..."
md "Or go to fashionable boutiques and visit famous ateliers..."
dm "Very interesting."
dm "But I didn't mean that."
dm "I meant what do you think about when you masturbate."
show mila camisole_and_shorts_embarassed3
ms "Oh..."
show mila camisole_and_shorts_embarassed2
ms "I felt stupid."
ms "He wasn't interested in my dreams."
ms "And me as a person."
ms "He was only interested in my body..."
show mila camisole_and_shorts_biting_lips
ms "A bit my lip."
ms "I liked it."
ms "That's why I'm here."
ms "The arousal made it hard to think straight."
ms "I felt intoxicated with lust."
ms "I wanted to say something reckless."
ms "Something sexual and daring."
show mila camisole_and_shorts_grin
md "I imagine myself being fucked by multiple men."
md "To be used like a rubber doll."
md "As if just an object for satisfying their lust."
show mila camisole_and_shorts_naughty
ms "I breathed heavily."
ms "Blood rushed to my cheeks."
ms "I really imagined it."
ms "And I liked it."
dm "Do you imagine yourself as a whore?"
show mila camisole_and_shorts_biting_lips
ms "I swallowed."
md "Yes."
dm "So you like to submit and serve horny males?"
md "{image=emoji/sweat.webp}"
dm "Say it."
dm "Say it out loud."
show mila camisole_and_shorts_irritated_2
ms "What nonsense."
ms "He won't know if I said it or not anyway."
show mila camisole_and_shorts_biting_lips
ms "My lips tingled with excitement."
ms "My pussy was itching and craving attention.{w} I could feel how wet my panties were."
show mila camisole_and_shorts_embarassed
m "I..."
ms "My voice sounded rough and hoarse."
m "I... would like to be ogled by horny men."
show mila camisole_and_shorts_grin
ms "Hehe."
ms "That came out silly."
show mila camisole_and_shorts_embarassed2
m "I am a slut"
show mila camisole_and_shorts_grin2
m "Haha."
show mila camisole_and_shorts_embarassed3
m "I AM A SLUT!"
show mila camisole_and_shorts_grin3
ms "HAHAHA"
ms "Something burst out of me along with laughter."
ms "Joy."
ms "Pride."
ms "And a sense of liberation from a{w} very,{w} very,{w} VERY long imprisonment."
ms "As if invisible chains were pulling my soul whole my life."
ms "And those chains finally disappeared."
dm "Well?"
show mila camisole_and_shorts_embarassed
ms "He couldn't have heard me, could he?"
show mila camisole_and_shorts_embarassed2
ms "He couldn't, right?"
dm "Did you try it?"
show mila camisole_and_shorts_thinking
md "Yes."
dm "And you liked it."
show mila camisole_and_shorts_embarassed
md "Yes."
dm "Aha."
dm "You're a natural-born slut."
show mila camisole_and_shorts_shy_smile
dm "Well, now that we've got that sorted out..."
dm "Undress."
show mila camisole_and_shorts_surprised
ms "?!"
show mila camisole_and_shorts_angry
md "I'm sorry, what?"
dm "Undress."
dm "I want to see you naked."
ms "I threw the phone away as if it had become hot."
ms "His words first clouded my mind, and then sobered me up, as if dousing me with a bucket of ice water."
ms "And the proper, well-behaved girl inside me screamed - \"No!.{w} Don't do this!\"."
play sound "vibro.mp3"
show mila camisole_and_shorts_worried
ms "But then curiosity and arousal took over again."
play sound "vibro.mp3"
ms "I took the phone in my hand and hesitated to unlock the screen."
play sound "vibro.mp3"
ms "It kept buzzing in my hand."
ms "I was afraid to read Dick's messages."
ms "Afraid that the second me would take over and I wouldn't be able to resist."
show mila camisole_and_shorts_shy
ms "And do something shameful."
ms "And the worst part - not even regret doing it."
dm "Just imagine that you're in the spotlight."
dm "That me and other gentlemen are devouring your body with lustful glances."
show mila camisole_and_shorts_embarassed
dm "You feel the heat and itch, don't you?"
dm "Your skin becomes so sensitive that clothes feel rough and unnecessary."
show mila camisole_and_shorts_biting_lips
dm "You feel like you are not your true self"
dm "Tease us a bit."
dm "Show us your body."
dm "Like a good slave you are."
show mila camisole_and_shorts_dazed
ms "I felt hypnotized"
ms "My feet just went to the bathroom"
scene br
show mila2 camisole_and_shorts_dazed at left
ms "Dick said...{w} No more face covering..."
ms "I need to make a dirty selfie, without hiding my face..."
show mila camisole_and_shorts_angry at right with hpunch
ms "The remains of my consciousness fought with the \"new me\""
ms "And the \"new me\" was winning"
show mila camisole_and_shorts_worried at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
ms "Everyone will be able see me..."
ms "And Paul..."
show mila camisole_and_shorts_angry at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
ms "What would he do if he knew?"
show mila2 camisole_and_shorts_dazed at left:
    easein 0.7 xzoom 1.1 yzoom 1.1
    easein 0.3 xzoom 1 yzoom 1
ms "Those questions..."
show mila camisole_and_shorts_angry:
    easein 0.5 xzoom 0.9 yzoom 0.9 yalign 1.0
ms "Are too complicated..."
ms "..."
show mila camisole_and_shorts_angry at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5):
    easein 0.5 xzoom 0.8 yzoom 0.8 yalign 1.0
ms "My second self kept yelling at me"
show mila camisole_and_shorts_angry at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5):
    easein 0.5 xzoom 0.7 yzoom 0.7 yalign 1.0
ms "But her voice became quieter until I couldn't hear it at all."
hide mila with dissolve
"..."
ms "Dazzled by my own thoughts I approached the sink and wet my camisole with water"
play sound "shot.mp3"
show mila2 camisole_and_shorts_dazed at center:
    xpos 0.6
ms "..."
hide mila2
show dick_selfie3x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "{image=dick/Selfies/dick_selfie3.webp}"
hide dick_selfie3x
dm "Not bad."
dm "But..."
show mila camisole_and_shorts_scared_shy at center:
    xpos 0.6
md "I took off the mask!"
dm "I see"
dm "But you are still covering your face"
dm "Don't"
show mila camisole_and_shorts_sad_looking_aside
md "I am not sure that I can..."
md "I mean should..."
md "I mean..."
ms "..."
dm "Then pull your shirt up and show us your tits, slut."
show mila camisole_and_shorts_embarassed2
ms "I swallowed"
ms "More excited than embarrassed, I hesitate a little."
ms "That...{w} I can do...{w} I obediently lifted my shirt and took another photo."
ms "The feeling of freedom and arousal overwhelmed me..."
play sound "shot.mp3"
show mila camisole_and_shorts_shy_smile
ms "..."
show dick_selfie4x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "{image=dick/Selfies/dick_selfie4.webp}"
hide dick_selfie4x
dm "Take your shirt off."
show mila camisole_and_shorts_topless_biting_lips
ms "The shirt fell to my feet."
ms "I looked at my reflection in the mirror as if for the first time."
show mila camisole_and_shorts_topless_smug
ms "Another me was looking at me."
ms "Bold, impudent, and sexy."
ms "I looked at myself like that and got aroused."
ms "I really wanted to undress."
ms "I wanted to show myself."
show mila camisole_and_shorts_topless_caress
ms "Show every..."
ms "Part..."
ms "Of my body..."
play sound "shot.mp3"
ms "..."
show dick_selfie5x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "{image=dick/Selfies/dick_selfie5.webp}"
hide dick_selfie5x
play sound "shot.mp3"
show mila camisole_and_shorts_topless_biting_lips
ms "I didn't even care that I showed my face"
ms "My fingers untied the shorts string"
ms "My heart was beating like crazy"
play sound "shot.mp3"
ms "..."
show dick_selfie6x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "{image=dick/Selfies/dick_selfie6.webp}"
hide dick_selfie6x
show mila camisole_and_shorts_topless_smug
ms "And with each shot taken, the voice of the second me became louder and louder."
play sound "shot.mp3"
ms "..."
show dick_selfie7x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "{image=dick/Selfies/dick_selfie7.webp}"
hide dick_selfie7x
ms "It was telling my body what to do."
ms "And my body obeyed those commands eagerly."
show mila camisole_and_shorts_topless_biting_lips
ms "The panties stuck to my wet pussy with thin fabric."
ms "I had never felt so aroused before."
ms "The arousal engulfed me,{w} consumed me,{w} demanded more and more.{w}It was like a drug."
play sound "vibro.mp3"
dm "Take off your panties, turn around and spread your ass."
dm "That's how sluts invite their master."
show mila camisole_and_shorts_topless_smug
ms "I looked away from the screen and looked at my reflection."
ms "The spark in my eyes burned brighter and brighter."
ms "My head protested his attitude towards me and his words."
show mila camisole_and_shorts_topless_caress_licking_lips
ms "But my hands pulled down the panties..."
play sound "shot.mp3"
ms "..."
show dick_selfie8x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "{image=dick/Selfies/dick_selfie8.webp}"
hide dick_selfie8x


play sound "door-open-close.mp3"
show mila camisole_and_shorts_topless_surprised
ms "Damn!"
ms "I lost track of time..."
p "{size=-8}Honey!"
ms "My shirt is wet, if I go out like this..."
p "{size=-4}Sweetie, are you home?"
show mila oversized_shirt_shy
ms "I put on Paul's shirt"
ms "Is this ok?{w} Can I greet him like this?"
ms "..."
scene bg door with fade
scene bg mila_shirt_tug
m "H-hi."
p "Hello sweetheart"
ms "Paul didn't look up at first - he was looking at the screen of his phone"
ms "But after a couple of seconds..."
p "How was your..."
scene bg mila_shirt_tug2
p "Wow!"
"..."
p "This..."
p "This is..."
p "What is this?"
ms "His gaze roamed over my body."
scene bg mila_shirt_tug3
ms "Paul was looking at me with a completely different look."
ms "Not the usual paternal and condescending one."
ms "But a lustful one..."
ms "And it aroused me even more."
scene bg mila_shirt_tug4
m "I..."
ms "I want him to press me against the wall right here..."
m "I put everything in the washing machine... {w} So..."
ms "So push me down right here and fuck me like there's no tomorrow!!!"
p "I-I see..."
ms "Obviously Paul didn't do it..."
ms "I was embarrassed by my own thoughts."
ms "Paul, red as a lobster, walked into the living room, trying not to look at me."
"..."
scene bg mila_shirt_tug5
ms "Well... {w} What else did I expect?"
ms "He always tired after work."
ms "It's his usual behavior..."
ms "But why does it annoy me so much?"
scene bg mila_shirt_tug6
ms "... No, really, why does it annoy me so much?"
ms "Maybe..."
ms "Maybe I should talk to him about... {w}all this?"
ms "I feel, that with everything I do, I just sinking deeper"
ms "Maybe I need my knight after all..."

menu:
    "I should talk to Paul before I made more mistakes...({color=#b0308d}Sharing{/color} route)":
        jump Netorase
    "I do what I want, and no one will stop me ({color=#d32020}Cheating{/color} route)":

        jump NTR


label Netorase:

ms "I…"
ms "I have to tell him everything..."
ms "Before I do anything stupid..."
ms "This can't go on any longer."
"{w}..."
scene bg apartments
ms "I told Paul everything."
ms "He didn't want to believe what he heard"
ms "But as soon as I showed him the photos, his face changed"
ms "He finally realized"
ms "He finally believed"
ms "Shock turned to anger"
ms "I've never seen him like this"
ms "And I got scared"
ms "But besides fear, another feeling appeared in my heart..."
"{w}..."
scene bg talking_out1
m "Paul?"
ms "..."
m "I…"
scene bg talking_out2
p "Shut up."
ms "His voice sounded rough and low"
ms "It's like someone else was talking to me"
ms "Or something different"
ms "Something evil and aggressive"
ms "Something animalistic..."
ms "Fear squeezed my throat"
ms "But with it came excitement"
ms "An unprecedented sense of danger intoxicated me"
ms "I swallowed..."
scene bg talking_out3
ms "...{image=emoji/heart.png}"
ms "..."
scene bg talking_out4
p "All my life…"
ms "Paul's voice sounded so hoarse and low..."
ms "As if it wasn't his voice at all."
p "I tried to be a “good” guy"
p "When I was bullied at school, I endured it"
p "I was waiting."
p "When everyone was living they lives and going on dates at university, I was studying."
p "Because I believed that there would be someone..."
p "At least one person in this shitty world, who will understand me."
p "Who will appreciate... {w}my efforts. My {w}loyalty."
p "My dignity, {w}my honor."
p "But all the girls that I liked back then..."
p "Fell in love with some assholes"
p "And it made me angry."
p "It turned me inside out, {w}I was sick of their hypocrisy and stupidity"
p "But still... {w}hope continued to glimmer in my heart"
p "Hope, {w}that I will find..."
scene bg talking_out5
p "You."
"{w}..."
p "And you…"
scene bg talking_out6
m "Paul... I..."
scene bg talking_out7
p "Shut the fuck up!"
ms "The words stuck in my throat."
scene bg talking_out8
ms "But his scream and my fear did not make me want to run away."
ms "Quite the opposite."
ms "I flowed like the last whore."
scene bg talking_out9
ms "I bit my lip and lowered my head, trying not to give myself away."
p "You! {w}I did everything for you!"
p "Everything!"
p "Whatever you wanted, I did it."
p "All I ever wanted in return was confidence, {w}that you wouldn't stab me in the back."
p "All I'm asked for {w}was a little respect."
p "And at least a drop of fucking loyalty."
p "Is it that difficult?"
p "Am I asking too much?"
"{w}..."
scene bg talking_out10
p "Fucking why?"
ms "..."
p "Why? Why did you do this?"
ms "Paul clenched his fists and slapped me"
scene bg talking_out10 with hpunch
m "Ahhh..."
ms "I couldn't hold back my groan."
ms "He slapped me, but it was still Paul's slap"
ms "It didn't hurt me.{w} My perverted self wanted more of that"
ms "His emotions...{w} His pain...{w} His anger"
ms "I wanted to provoke him even more, so I didn't try to hard to disguise my moan as a groan of pain."
scene bg talking_out9
p "Is this what you wanted?"
p "To be exposed? {w}To become a whore?"
p "To be used like a thing?"
ms "I silently looked up at him"
ms "He didn't look like himself"
ms "Strong, menacing, scary"
ms "Like an angry beast"
ms "I looked at him and could hardly restrain the desire to put my hand into my panties..."
ms "Damn, how sexy he is now..."
p "Spread your legs"
ms "His commanding voice echoed in my head"
ms "His hands reached down and pulled down his pants."

label hscene_netorase_hatefuck:
scene bg talking_out11
ms "I raised my legs up and spread my pussy, feeling with my fingers how wet I was"
ms "Paul entered me sharply and quickly"
scene bg talking_out12 with dissolve
ms "Without asking, as usual, {w}if it hurts, {w}if I need to get used to it"
ms "He satisfied his urge with my body"
scene bg talking_out13 with dissolve
ms "Rough, with animalistic fury"
scene bg talking_out14 with dissolve
ms "His strong hands grabbed my buttocks and held my hips tightly"
scene bg talking_out15 with dissolve
m "Ahhh. ahhh... AHHHH!"
ms "I came almost immediately and, without trying to hide my orgasm, gave in to sweet convulsions"
m "Ahhhh!"
ms "When I opened my eyes I noticed that his rage gradually began to recede."
ms "In its place came lust and surprise"
scene bg talking_out15a with dissolve
ms "I looked at Paul and smiled"
m "Yes, my love...{w} This is exactly what I wanted..."
ms "Paul squeezed my hips even harder and after a few strokes began to pump his sperm into me"
scene bg talking_out16 with dissolve
ms "I enjoyed these sensations - the walls of my pussy felt every spasm of his penis"
ms "Paul let go of my hips and sat on the sofa with his head in his hands."
ms "I didn't know how to support him and how to show him that nothing bad happened"
scene bg talking_out17 with fade
ms "I silently knelt down and took his penis into my mouth, cleaning it of sperm."
ms "..."
ms "Paul raised his head and looked at me in surprise for a while."
p "What are you doing?"
scene bg talking_out18 with dissolve
ms "I licked another drop of sperm from his dick and answered"
ms "You yourself said that I am a whore, and I behave the way my husband wants me to."
ms "I showed him my tongue with the remnants of sperm then licked my lips and swallowed"
m "Mmm…"
"{w}..."
scene bg talking_out20 with dissolve
ms "..."
m "Do you... hate me now?"
ms "..."
ms "Paul looked away."
ms "I leaned my elbows on his lap and pressed my cheek against his dick."
scene bg talking_out21 with dissolve
m "Our life seemed boring to me, my love."
ms "..."
m "I..."
m "I wanted something new. So that you stop considering me \"yours\"."
ms "Paul looked at me in fear."
m "I'm not a thing, my love."
m "I am human."
m "I am a woman."
m "And I won't always do what you expect of me."
ms "..."
ms "Paul relaxed a little, but was still silent."
scene bg talking_out20 with dissolve
m "I love you, Paul."
ms "Paul shook as if struck."
ms "I ignored his reaction."
m "I will always love you."
m "And I know that you love me too."
ms "Paul hesitantly raised his hand and patted my head."
ms "I closed my eyes and smiled."
ms "..."
ms "..."
m "Well..."
m "So... Tell me honestly..."
scene bg talking_out21 with dissolve
m "Did you like it?"
ms "..."
ms "Paul's hand froze, but then he continued stroking my head."
ms "..."
p "Yes.."
ms "His voice sounded uncertain. As if he doubted his words and feelings."
ms "..."
m "And what exactly do you..."
p "I don't know."
ms "This time he answered faster and sharper."
ms "..."
ms "..."
m "You…"
m "Would you like to do something like that again?"
ms "..."
ms "..."
p "What exactly?"
ms "..."
m "Well…"
scene bg talking_out19 with dissolve
ms "I licked his penis"
m "I don't know… Yet..."
ms "..."
m "For example... Have you ever imagined me..."
ms "..."
m "In a slightly different... {w}role? Not just your plain princess-wife."
ms "..."
ms "..."
scene bg talking_out18 with dissolve
m "For example, if I were a fitness instructor and beefy men were hanging around me..."
ms "Paul tensed."
m "No?"
ms "..."
scene bg talking_out17 with dissolve
m "Well, or maybe some of your subordinates from work would come to us..."
m "You know the green one..."
ms "..."
p "I received a promotion not long ago, I don't really have any subordinates yet."
m "Which means no?"
ms "..."
p "No."
ms "..."
scene bg talking_out18 with dissolve
m "Maybe with someone older?"
ms "Paul's dick twitched and poked my cheek."
ms "I raised my eyes and looked at him."
ms "..."
ms "Paul said nothing."
m "With someone who is definitely not your equal."
ms "His penis began to fill with blood."
scene bg talking_out22 with dissolve
m "Imagine a fat older man in a Smoky the Bandit T-shirt holding me by the hair and fucks me from behind..."
ms "..."
ms "His penis became completely hard."
ms "Hehe..."
m "Someone here doesn't let you lie."
ms "Paul turned away embarrassed and did not answer."
ms "I ran my tongue along the shaft of his penis, just like I saw in a porno."
m "Imagine him sitting on the bed, and me on my knees in front of him..."
p "..."
m "How his thick and hairy penis penetrates my small mouth..."
ms "Paul tensed as if before an orgasm"
ms "Hehe..."
m "How he covers my face with his thick sperm..."
p "Ahhh..."
ms "Paul couldn't stand it and start cumming"
scene bg talking_out23 with dissolve
ms "I opened my mouth wider and let him ejaculate inside my wanting mouth"
ms "His sperm tasted sweet..."
ms "I easily swallowed it bit by bit"
scene bg talking_out24 with dissolve
ms "When his dick stopped twitching, I squeezed out the last drops of his cum"
ms "His penis became softer and smaller"
ms "I opened my mouth and showed Paul the remaining sperm"
scene bg talking_out25 with dissolve
m "Ahah…"
m "Is that what you like?"
p "..."
m "Understood"
m "..."
ms "Paul went limp and was breathing heavily."
p "Where did you learn that?"
ms "I collected the sperm from my cheek with my finger and licked it."
ms "Then I leaned towards his ear and answered."
m "I suck off the old janitor every day."
ms "..."
ms "Paul looked at me in disbelief."
m "Ahaha"
m "I'm kidding"
"{w}..."
if _in_replay:
    return


scene bg apartments
n "Several weeks have passed."
ms "Our sex life was filled with depraved fantasies"
show mila red_thinking at right:
    xzoom 0.8 yzoom 0.8
ms "We talked, we found out what each of us was hiding under the surface"
ms "Which we discussed and then made real"
show mila red_shy at right:
    xzoom 0.8 yzoom 0.8
ms "But, I'm afraid we've become a little noisier than before..."
ms "I hope we didn't disturb the neighbors too much..."
show mila red_naughty at right:
    xzoom 0.8 yzoom 0.8
ms "..."
ms "Thinking about last night made me kinda hot..."
ms "..."
ms "I should go to the grocery store to clear my mind..."
"{w}..."
scene bg grocery_store
show mila red_bags at right:
    xzoom 0.8 yzoom 0.8
ms "Damn, the bags are so heavy."
ms "How am I supposed to drag all of it home?"
"{w}..."
scene bg street
show mila red_sweat at right:
    xzoom 0.8 yzoom 0.8
m "Haah {w}haah"
ms "Ok..."
ms "This is my neighborhood"
ms "The main thing is to get to the entrance door... {w} Then elevator... {w} And then I'm almost home..."
ms "Why did I get so much meat anyway? {w}And why did I buy pineapples?"
ms "It's clear they were a good deal, maybe because I heard they sweeten men's sperm {w} *giggle*"
ms "But now I need to get them home somehow..."
ms "I'll just rest a bit, and then go further..."
ms "I tiredly put the bags down and sighed."
show mila red_rest at right:
    xzoom 0.8 yzoom 0.8
m "Ugh... My back."
ms "A plump and tall middle aged man appeared next to me as if out of nowhere."
ms "Despite being huge his steps were so silent, that I didn't hear them at all"
ms "And despite being so large, he slouched in an attempt to hide his presence, as if he didn't want people to pay attention to him"
show mila red_surprised at right:
    xzoom 0.8 yzoom 0.8
ms "When I heard his quiet voice, I even shuddered in surprise."
ms "The man smiled awkwardly."
show someone at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "Excuse me... Can I help you?"
ms "..."
ms "He leaned a bit towards me"
ms "I smelled a faint scent of sweat and cheap cologne."
ms "I swallowed and hurriedly waved my hands in front of me."

show mila red_waving_hands at right:
    xzoom 0.8 yzoom 0.8
m "No, no, it's okay"
ms "It seemed his face had not changed, but I felt that my refusal had upset him."

hide someone
show bob waving at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "Sorry... I didn't mean to scare you."
ms "..."

show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "You probably don't like being near me, so I'll take my leave..."

show mila red_sad at right:
    xzoom 0.8 yzoom 0.8
ms "My heart sank with sympathy."
ms "Without realizing it, I grabbed his hand."

show mila red_wait at right:
    xzoom 0.8 yzoom 0.8
m "Please, wait!"
m "In fact, it would be great if you could help me..."

show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "..."

show mila red_scratch at right:
    xzoom 0.8 yzoom 0.8
m "I don't know why I declined your offer. I can't imagine how I'll manage carrying these bags up the stairs."

show bob surprised at left:
    xzoom 0.9 yzoom 0.9
ms "The man raised his eyebrows in surprise, not believing his ears."
bob_unknown "Hmm...{w} Sure..."
bob_unknown "..."
m "..."

show mila red_awkward_smile at right:
    xzoom 0.8 yzoom 0.8


show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "..."
ms "He is kinda creepy..."

show mila red_wait at right:
    xzoom 0.8 yzoom 0.8
m "It's right around the corner,{w} that big apartment building, you know?"


show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "..."
bob_unknown "You mean 32/1 at 3rd st?"

show mila red_scratch at right:
    xzoom 0.8 yzoom 0.8

m "Yeah! You know the streets quite well, haha!"

show mila red_creep at right:
    xzoom 0.8 yzoom 0.8

ms "Creepy!"
ms "The man seemed a bit hurt of my awkward smile"

show bob sad2 at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "No, I don't know \"the streets\". I just live in this building"

show mila red_scratch at right:
    xzoom 0.8 yzoom 0.8

ms "Oh... Ok then..."

show mila red_sad at right:
    xzoom 0.8 yzoom 0.8

"He reached out his hand to me and I gave him the bags."

"We walked in awkward silence"
"{w}..."
"When we came to the building we found out that the elevator wasn't working"

show mila red_angry at right:
    xzoom 0.8 yzoom 0.8

m "Are you kidding me?!"
ms "The man laughed dryly"
ms "I looked at him and then at the bags"
ms "{w}..."
ms "Well... {w} It would be rude to ask him to carry them to the 14th floor right?"
ms "But the man just walked to the stairs"
scene bg stairs
show mila red_awkward_smile at right:
    xzoom 0.8 yzoom 0.8
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "You live in 1420R, right?"
show mila red_creep at right:
    xzoom 0.8 yzoom 0.8

ms "..."
ms "Creepy!"
show bob sad at left:
    xzoom 0.9 yzoom 0.9
ms "The man put on a sad smile again and looked to the side"
bob_unknown "I am your neighbor, that's why I know"


show mila red_sad at right:
    xzoom 0.8 yzoom 0.8

ms "Oh..."
ms "Wait if he is our neighbor, then he must have heard our... new games..."

show mila red_shy at right:
    xzoom 0.8 yzoom 0.8

ms "I tried to cover my embarrassment with a laugh"

show mila red_scratch at right:
    xzoom 0.8 yzoom 0.8
m "Ahah, sorry, I should have known"

show bob shy at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "Oh don't worry... {w}I only recently noticed... that I have neighbors"
ms "..."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "I mean, I am not very social..."
ms "I wanted to answer, but climbing the stairs knocked all desire to talk out of me"
"{w}..."

scene bg doors
show mila red_rest at right:
    xzoom 0.8 yzoom 0.8
m "Haaaa... {w}haaaa... {w}haaaa..."
ms "Fourteen floors, this is not a joke, right?"
ms "I leaned forward to catch a breath"
show cg leaning_red1 at center:
    xzoom 0.5 yzoom 0.5 ypos 1
    linear 1.0 ypos 0.75
ms "When I looked up, the man turned away sharply. {w}His face was bright red."

show bob shy at left:
    xzoom 0.9 yzoom 0.9
ms "I looked down and realized that bending over gave him an excellent view of my breasts."
ms "..."

show mila red_shy at right:
    xzoom 0.8 yzoom 0.8

ms "Oh gods... Was he staring at me?"
ms "..."
ms "Well, not that I am against it..."
ms "A small price to pay for helping me carry the bags."
ms "Maybe I should even cheer him up a little."
ms "I smiled and leaned forward even more"
m "Thank you very much, my friendly neighbor!"
show cg leaning_red2 at center:
    xzoom 0.5 yzoom 0.5 ypos 1
    linear 1.0 ypos 0.75
ms "This will give him a bit better view."

show bob surprised at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "..."
ms "Hehe"

show bob waving at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "No no, it's nothing!"
ms "He waved his hands."


show bob shy at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "It was my pleasure to help."
show mila red_giggle at right:
    xzoom 0.8 yzoom 0.8
ms "Hehe..."
ms "Of course it was a pleasure..."


hide cg leaning_red2
show mila red_smile at right:
    xzoom 0.8 yzoom 0.8
m "My name is Mila. We never introduced ourselves..."

bob_unknown "You have such a beautiful name!"
m "Thanks!"

show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "..."
m "..."

m ".{w}.{w}?"
show mila red_awkward_smile at right:
    xzoom 0.8 yzoom 0.8
m "And you?"


show bob surprised at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "Oh! {w}Sorry! {w}I am Bob..."
ms "That was awkward..."

show mila red_smile at right:
    xzoom 0.8 yzoom 0.8


m "Well, nice to meet you, Bob."
ms "..."

show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "Nice to meet you too, miss"
ms "..."
bob "..."

show mila red_awkward_smile at right:
    xzoom 0.8 yzoom 0.8

ms "The pause dragged on"


show bob sad at left:
    xzoom 0.9 yzoom 0.9
ms "He began to look somewhat sad and depressed again."
ms "I patted him on the shoulder and took my bags"

show mila red_bags at right:
    xzoom 0.8 yzoom 0.8

m "Okay, I won't waste your time anymore."
bob "Sure..."
ms "He pursed his lips and nodded."
ms "The big guy looked like he was about to cry."
ms "..."
ms "I looked at my packages."
ms "..."

show mila red_shy at right:
    xzoom 0.8 yzoom 0.8

m "Are you married, Bob?"
ms "..."

show bob sad2 at left:
    xzoom 0.9 yzoom 0.9
ms "He became even sadder."
bob "No."
ms "The answer sounded sharp, if not rude."
ms "..."

show mila red_waving_hands at right:
    xzoom 0.8 yzoom 0.8

m "Sorry, I didn't mean to offend you."
bob "..."

show mila red_smile at right:
    xzoom 0.8 yzoom 0.8

m "I just picked up a lot of meat and vegetables..."
m "Would you let me to treat you to my world famous stew?"
bob "..."

show bob surprised at left:
    xzoom 0.9 yzoom 0.9
ms "Bob looked at me in disbelief."
ms "..."

show mila red_awkward_smile at right:
    xzoom 0.8 yzoom 0.8

m "?..."
m "You don't like stew?"


show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "I DO! Yes! I want it, of course I want it!"
ms "He showed his bag which contained several packs of instant noodles."
bob "I don't know how to cook and therefore I don't eat very well..."

show mila red_nagging at right:
    xzoom 0.8 yzoom 0.8

ms "I put one hand on my hip and wagged a finger at him."
m "You can't do that, Bob! You'll give yourself an ulcer!"
ms "..."


show bob smile at left:
    xzoom 0.9 yzoom 0.9
ms "Bob smiled and scratched the back of his head."
bob "Sorry, miss."
ms "..."

show mila red_scratch at right:
    xzoom 0.8 yzoom 0.8

m "Actually {w}I'm Mrs."


show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "Oh... {w}Right... {w}Sure... {w}Obviously..."
ms "Bob became sad again."

show mila red_sad at right:
    xzoom 0.8 yzoom 0.8

ms "He looked like a lost puppy"
ms "I couldn't stand it"
ms "They say - sharing is caring..."
ms "..."

show mila red_shy at right:
    xzoom 0.8 yzoom 0.8

ms "..."
m "Are you busy now?"
"{w}..."

show bob surprised at left:
    xzoom 0.9 yzoom 0.9
bob "No... But why are you asking?"
ms "..."

show mila red_wait at right:
    xzoom 0.8 yzoom 0.8

m "Well, you could help me with cooking. And at the same time we could have dinner together..."
m "Paul will be home late today, so I'm afraid it'll be sad to spend my evening alone."
bob "..."

show bob smile at left:
    xzoom 0.9 yzoom 0.9
bob "I.. Yes! {w}Just let me take a shower."

show mila red_smile at right:
    xzoom 0.8 yzoom 0.8

m "Sure, sure..."
ms "..."

show mila red_shy at right:
    xzoom 0.8 yzoom 0.8

ms "I had the idea of teasing him again, so I pulled back my T-shirt and waved it, revealing a view of my chest."
show cg leaning_red3 at center:
    xzoom 0.5 yzoom 0.5 ypos 1
    linear 1.0 ypos 0.75
m "Yeah! I need to hit the shower too! {w}It's damn hot today, huh?"

show bob shy at left:
    xzoom 0.9 yzoom 0.9
bob "{w}... Yes... {w} it is very hot."
show mila red_smile at right:
    xzoom 0.8 yzoom 0.8

ms "..."
ms "..."
hide cg leaning_red3
show mila red_waving_hands at right:
    xzoom 0.8 yzoom 0.8
m "Well, see you later."
ms "I went into the apartment and closed the door."
play sound "door-open-close.mp3"
hide mila red_waving_hands
hide bob shy


"{w}..."
scene bg bedroom
ms "I took a shower and stood in front of the closet."
show mila nude_think at right
ms "Hmmm..."
ms "Bob is looking like a guy, who is begging to be teased..."
ms "But I mustn't overdo it - he might think that I am some kind of weirdo"
show mila oversized_shirt_posing at right
ms "Maybe something like this?"
ms "..."
ms "Nah... {w} It's too... {w}random... {w}Also it feels wrong for some reason..."
show mila casual_skeptic at right:
    xpos 0.9
    ypos 0.95
ms "{w}..."
ms "And that's kinda... {w}Plain..."
ms "Hmmm..."
show mila robe_puzzled at right
ms "..."
show mila robe_from_behind_looking at right
ms "..."
ms "That's it! {w} I think..."
ms "I wonder if it's too much?"
ms "Spinning in front of the mirror and fixing my makeup, I almost missed a cautious and quiet knock at the door."
"{w}..."
scene bg door
play sound "door-open-close.mp3"
show bob waving at left:
    xzoom 0.9 yzoom 0.9
bob "... {size=-10}H-hello?"
show mila robe_smile_open_mouth at right
m "Hi again! {w}You knocked so quietly that I thought it might be a draft, haha."
show bob shy at left:
    xzoom 0.9 yzoom 0.9
ms "Bob smiled sheepishly."
show mila robe_smile_grin at right
m "Come on in."
ms "Drops of water were visible on his skin."
show mila robe_curious at right
ms "Was he in such a hurry that he forgot to dry himself?"
ms "Even though he had obviously just come from the shower, he was dressed the same as before.."
show mila robe_blush_shy_looking_aside at right
ms "But most importantly, I couldn't help but notice the huge bulge in his pants."
show mila robe_blush_smirk at right
ms "Did he like my robe that much, huh?"
ms "I smiled at my thoughts and called him into the kitchen."
"{w}..."
scene bg kitchen
ms "..."
show mila robe_from_behind_not_looking at right
ms "While we were cooking, I noticed as Bob throw glances at my butt"
ms "I wanted to tease him more, but I didn't risk it and just pretended, that I didn't notice"
ms "I've already gone too far with the robe..."
ms "And it's just plain dangerous to provoke him more"
ms "It will be better if I just pretend to be naive and careless"
ms "And first of all I need to talk to Paul about..."
show mila robe_think at right
ms "About what?"
ms "I glanced at Bob."
show bob idle at left:
    xzoom 0.9 yzoom 0.9
ms "Upon closer inspection, he is probably already over fifty."
ms "His build is... {w}Well he is not well built to say the least."
show mila robe_blush_shy_looking_aside at right
ms "The only thing he can compete with Paul is the size of his dick, judging by the bulge in his pants..."
ms "But I don't think that will be a problem for Paul, knowing his kinks..."
hide mila robe_blush_shy_looking_aside
"{w}..."
ms "..."
ms "When the food was ready, Bob stood up and was about to leave."
show mila robe_puzzled at right
m "Where are you going?"
bob "..."
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "I... {w} I forgot to bring a food container, {w}so I wanted to go and get it..."
show mila robe_puzzled_frown at right
m "Container? {w}Why do you need that?"
"Bob looked at me in confusion."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "But you said that you wanted to treat me to stew..."
show mila robe_blush_smirk at right
ms "I couldn't help it, I wanted to tease him more... {w}His reactions are the kind that make you want to play him a little..."
m "Did I?"
show bob sad2 at left:
    xzoom 0.9 yzoom 0.9
ms "Bob put on an even sadder smile"
show mila robe_smile_grin at right
ms "I giggled and nodded towards the chair."
m "Sit down. {w}Let me take care of you."
show bob idle at left:
    xzoom 0.9 yzoom 0.9
ms "He sat down at the table embarrassedly."
show mila robe_from_behind_not_looking at right
ms "I turned to the sink and was about to grab a regular plate"
ms "Hmmm..."
show mila robe_from_behind_looking at right
ms "I guess Bob needs a larger portion"
ms "And... {w} It would be fun to tease him more."
show mila robe_from_behind_not_looking_reaching_tiptoes at right
ms "I stretched my back and stood on tiptoes, in attempt to reach for the large bowl on top"
ms "I almost immediately grabbed the edge, {w}but feeling his gaze on my ass, I stood up on tiptoes more and leaned over to give him a better view."
show cg robe_close_up_butt at center:
    xzoom 0.75 yzoom 0.75 ypos 1 xpos 0.5
    linear 1.0 ypos 0.75
ms "Hehe."
ms "This is so exciting!"
ms "..."
show bob shy at left:
    xzoom 0.9 yzoom 0.9
ms "Glancing over my shoulder, I noticed that Bob was having a hard time covering his boner."
ms "Hehehe."
ms "..."
ms "..."
ms "I set the table and sat down opposite him."
scene bg kitchen
"{w}..."
ms "We just ate in silence for a while."
show mila robe_curious at right
m "So... {w}is it good?"
show bob smile at left:
    xzoom 0.9 yzoom 0.9
bob "Yes, Mrs, everything is very tasty!"
show mila robe_smile_open_mouth at right
m "Just call me Mila, otherwise Mrs. sounds a bit too..."
ms "Bob smiled apologetically and nodded."
"{w}..."
"{w}..."
show mila robe_puzzled at right
ms "This silence makes it hard to breathe..."
ms "It looks like he wants to talk with me but was too afraid to start a conversation"
ms "I tried to break the ice again"
show mila robe_smile_open_mouth at right
m "So... {w} What do you do for a living?"
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "..."
bob "I am a kind of developer, {w}I guess..."
show mila robe_puzzled at right
ms "What kind of answer is that?"
show mila robe_smile_awkward_open_mouth at right
m "You mean in IT?"
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "Yeah..."
show mila robe_puzzled at right
"{w}..."
ms "Is he for real?"
ms "His communication skills are really top notch..."
show mila robe_smile_awkward_open_mouth at right
m "Do you have any hobbies? {w}What do you like to do in your free time?"
bob "..."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
ms "Bob stared at me for a while"
bob "I... {w}I like fishing, {w}I think."
ms "That's something"
show mila robe_smile_open_mouth_excited at right
m "Oh really? {w}What is the biggest fish you ever caught?"
show bob sad2 at left:
    xzoom 0.9 yzoom 0.9
bob "..."
ms "Somehow he became even more sad"
show mila robe_puzzled at right
ms "This guy is a walking landmine"
bob "Actually I don't like fishing, I'm sorry"
show mila robe_puzzled at right
m "..."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "I lied..."
ms "Uhuh"
ms "Now I understand nothing..."
show mila robe_smile_awkward_open_mouth at right
m "Erm... {w}Why?"
bob "..."
show mila robe_puzzled at right
ms "Bob hesitated {w} but I silently waited for his reply"
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "I... I don't know..."
bob "I thought that my hobbies may seem weird..."
show mila robe_puzzled at right
m "..."
show mila robe_puzzled_frown at right
ms "Please don't tell that you have a collection of dead people in chests or something..."
show mila robe_think at right
ms "I guess... {w}I need to encourage him somehow..."
show mila robe_smile_open_mouth at right
m "You know what my hobby is?"
bob "..."
ms "He looked at me with anticipation"
show mila robe_blush_shy_looking_aside at right
m "I {w}collect lonely socks"
bob "..."
m "..."
bob "..."
show mila robe_smile_open_mouth at right
m "You know, the ones that are left with on partner after the washing?"
m "Somehow, I can't throw them away, and sometimes, I go through them hoping to reunite its partner."
bob "..."
show mila robe_smile_grin at right
m "Dumb hobby, huh?"
show bob smile at left:
    xzoom 0.9 yzoom 0.9
bob "..."
bob "Heh"
show mila robe_smile_open_mouth at right
m "So don't be afraid to tell me about your hobby"
m "I doubt that your is dumber than mine..."
bob "..."
show mila robe_puzzled at right
m "..."
show bob shy at left:
    xzoom 0.9 yzoom 0.9
bob "..."
bob "Well... {w} I like anime and games..."
"{w}..."
show mila robe_smile_awkward_open_mouth at right
m "..."
m "You mean... {w}something extreme?"
bob "No no!"
bob "Just regular ones..."
show mila robe_smile_awkward_angry at right
ms "..."
ms "That's it?"
ms "Where is the punchline?"
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "It's just..."
bob "I always do everything at the wrong time of life..."
m "..."
show mila robe_curious at right
bob "Like... I am 52, and I like the things that are made for the teenagers."
bob "I've never been married or even in a relationship because I always thought that it was the thing for the future."
show mila robe_sad at right
bob "I am always late... My colleagues make fun of me..."
bob "I missed my promotion, my Mom's funeral, everything..."
show bob sad2 at left:
    xzoom 0.9 yzoom 0.9
show mila robe_sad_tears at right
bob "I missed my life..."
bob "And now... Now I am just a pathetic old wimp who is whining about his problems..."
ms "..."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "... {w}Sorry..."
bob "I ruined the mood... {w} I always do..."
"{w}..."
ms "That was... {w}tough to hear..."
ms "Bob looked at me and put on an empty and sad smile"
bob "So… Well..."
show bob smile at left:
    xzoom 0.9 yzoom 0.9
bob "Thank you for this evening."
ms "His smile looked the same... {w}But his voice seemed strange to me."
ms "It seemed distant... {w}Wavering... {w}Dying..."
show mila robe_sad_tears_open_mouth at right
m "Bob?"
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "I'll probably should go. Don't worry, I won't bother you anymore..."
ms "He stood up."
show mila robe_sad at right
ms "I felt a lump raising in my throat."
ms "As if… If I didn't do something right now, I would regret it for the rest of my life."
ms "Therefore, when he passed by, I grabbed his hand without thinking"
show mila robe_think at right
m "Wait."
show bob sad2 at left:
    xzoom 0.9 yzoom 0.9
ms "Bob looked at me blankly."
ms "There was so much sorrow in his eyes... {w}It was as if there was no person left inside. {w}Just an empty shell."
show mila robe_proud at right
m "Don't you want to catch up then?"
show bob surprised at left:
    xzoom 0.9 yzoom 0.9
bob "Catch up? What do you mean?"
show mila robe_grin_thumbs_up at right
m "Hah. Leave that to me!"
"{w}..."
show mila robe_puzzled at right
ms "I have no idea!!!"
show bob idle at left:
    xzoom 0.9 yzoom 0.9
ms "Bob just tilted his head to the side."
show mila robe_think at right
ms "I need to figure out how exactly \"he\" can \"catch up\"..."
ms "Although, if you think about it, it's not like I can help with much..."
ms "First of all, I need to fix his self-esteem..."
bob "..."
show mila robe_puzzled at right
ms "And probably his public image as well..."
ms "Money could help..."
show mila robe_puzzled_frown at right
ms "Pity I don't have that..."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "?..."
show mila robe_sad at right
ms "And I have no idea how a person can become rich fast"
ms "{w}..."
ms "To be honest I have no idea how a person can become rich at all"
ms "And even if I could - it won't solve the problem..."
show mila robe_think at right
ms "Hmmm{w}..."
ms "I caught a glimpse of my own reflection in the mirror"
show mila robe_smile_open_mouth_excited at right
m "Oh!"
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "?"
show mila robe_proud at right
m "You, my dear, will find a girlfriend!"
bob "..."
show bob sad2 at left:
    xzoom 0.9 yzoom 0.9
ms "Bob laughed sadly, if not evilly."
bob "Hah! Do you think I haven't tried?"
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "All women are attracted to cute faces! Or money. I have neither one nor the other!"
show mila robe_smile_awkward_angry at right
m "..."
bob "..."
m "..."
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "Well, ok, not every woman... {w}But almost everyone... {w}I mean no offense..."
show mila robe_puzzled at right
ms "I stopped him with a gesture."
m "You may be right to some extent. But we, PEOPLE, are all interested in what is already in demand."
bob "..."

show mila robe_smile_open_mouth at right
m "So, {w}what does that mean?"
m "..."
bob "..."
m "..."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
ms "Bob sighed"
bob "What does it mean?"
ms "Great, at least some reaction."

show mila robe_proud at right
m "It means the main thing is to show that you have worth. {w}That you are already... {w}in demand and {w}someone worth getting to know."
ms "Bob narrowed his eyes."

show mila robe_blush_smirk at right
m "Look."
ms "I grabbed his elbow and took a photo."
play sound "shot.mp3"
show cg selfie_with_bob at center:
    xzoom 0.8 yzoom 0.8 ypos 1
    linear 1.0 ypos 0.75

show mila robe_proud at right
m "See?"
show bob shy at left:
    xzoom 0.9 yzoom 0.9
bob "..."

show mila robe_blush_smirk at right
m "We look like a couple."
bob "..."

show mila robe_smile_open_mouth at right
m "I don't have your number, let me send you this photo..."
bob "Ah? Yes OK…"
ms "Bob didn't seem to believe what was happening."
ms "..."
hide cg selfie_with_bob
nvl clear
md "{image=bob/One use/selfie_with_Bob.webp}"
show bob idle at left:
    xzoom 0.9 yzoom 0.9
ms "Bob silently stared at the screen of his phone"
show mila robe_smile_grin at right
ms "I squeezed his hand and waited until he finally paid attention to me."
m "You're a great guy Bob."
m "Don't worry too much about stupid people."
m "Many girls like big guys"
m "Don't lump everyone into the same basket."
bob "..."
show bob shy at left:
    xzoom 0.9 yzoom 0.9
bob "Do you?"
show mila robe_puzzled at right
m "..."
m "M?"
ms "His question took me by surprise."
bob "Do {b}you{/b} {w}like big guys?"
show mila robe_blush_smirk at right
ms "..."
m "Yes, Bob. {w}I like big guys."
ms "For some reason it sounded erotic. {w}My tummy felt warm and I could hardly resist the urge to squeeze my legs."
show bob smile at left:
    xzoom 0.9 yzoom 0.9
bob "..."
show mila robe_smile_open_mouth at right
m "Post this photo on social networks. {w}I will create a new page and say that I have recently met the most wonderful man in my life."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
ms "Bob frowned."
bob "Why do you need another page?.."
m "..."
show mila robe_puzzled at right
ms "..."
m "The current one contains my wedding photos and pictures with Paul. It will be strange if someone sees them."
bob "Ah... Well, yes, that sounds reasonable."
ms "..."
ms "Bob posted a photo on his page."
ms "..."
show mila robe_think at right
ms "I feel that it's not enough..."
show mila robe_smile_open_mouth_excited at right
ms "Oh! {w}I came up with another idea."
show mila robe_blush_smirk at right
m "Come by tomorrow morning. {w}I'll give you something."
show bob surprised at left:
    xzoom 0.9 yzoom 0.9
bob "..."
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "Ok... {w} I will"
play sound "door-open-close.mp3"
show bob surprised at left:
    xzoom 0.9 yzoom 0.9
    linear 1.0 xpos 0.75
show mila robe_blush_smirk at right:
    linear 1.0 xpos 0.9
p "I'm home!"
show mila robe_smile_open_mouth at right:
    xpos 0.9
m "Oh, it's Paul. {w}Let me introduce you."
show paul suit_shock at left
ms "Paul froze when he saw such a big guy and slowly turned his gaze to me."
show paul suit_frown at left
ms "Noticing my outfit and embarrassed look, he frowned."
p "Is this... {w}Is this what I think it is?"
ms "..."
show mila robe_blush_smirk at right:
    xpos 0.9
m "No. {w}At least not yet."
show bob idle at left:
    xzoom 0.9 yzoom 0.9 xpos 0.75
ms "Bob looked from me to Paul with a silent question in his eyes."
show mila robe_smile_open_mouth at right:
    xpos 0.9
m "This is Bob."
ms "I briefly told Paul about how Bob helped me carry my bags and prepare dinner"
scene bg door
ms "Bob opened his mouth to add something, but I pulled him towards the exit."
show mila robe_smile_awkward_open_mouth at right
m "Okay, Bob, {w}thanks again for your help, {w}it was nice to meet you."
ms "And already at the door I added."
show mila robe_blush_smirk at right
m "Come by tomorrow morning before work. {w}Do not forget!"
show bob sad at left:
    xzoom 0.9 yzoom 0.9
ms "He nodded, still perplexed."
bob "Sure... {w}Good night..."
hide bob_sad
play sound "door-open-close.mp3"
ms "I rushed to the bedroom, to give Paul proper explanation"
ms "I don't want him to think I'm doing anything without his consent."


label hscene_netorase_hj_with_paul:
scene bg apartments
ms "Paul was waiting for me in the living room with crossed arms"
ms "I knelt before him and took off his pants."
show cg mila_paul_hj_smile with dissolve
ms "His rock hard dick popped out at my face"
ms "I took it in my hand and looked at Paul"
m "Before you ask any questions - nothing happened"
p "..."
m "I flashed my tits a bit for him, and let him look at my butt a little"
p "..."
m "It was... {w}exciting"
p "..."
m "..."
m "Is this what you wanted?"
p "..."
show cg mila_paul_hj_worried with dissolve
p "I'm not sure..."
p "..."
p "It's painful to imagine you... with someone else..."
m "..."
m "Do you want to stop?"
p "..."
p "..."
p "{size=-10}no..."
m "..."
show cg mila_paul_hj_idle with dissolve
p "Mmm..."
p "What are you planning to do next?"
m "..."
m "I want to boost his self esteem first..."
m "So I will pretend to be his girlfriend or something..."
ms "Paul made a grimace"
m "You don't like the idea?"
p "..."
p "It's just... {w}No... {w}I'm just jealous, I think..."
m "..."
m "Do you want to put some... {w}restrictions on my actions?"
p "..."
p "Don't fall in love with him..."
show cg mila_paul_hj_smile with dissolve
m "I won't. {w}I love you."
p "..."
p "I love you too, sweetheart..."
m "Darling?"
p "Yeah?"
m "What is your fantasy about... all of this?"
p "I... I'm afraid to dig deep into it..."
p "Afraid to admit that... That I like it when others are... With you..."
ms "He seemed so vulnerable... I wanted to support him somehow"
m "I love you"
p "I know..."
p "It's just... It's wrong... It's not what I want to want, but I do..."
p "Every time I have even one thought about it I hate myself for it..."
p "But... It's so exciting..."
m "Can you... Share one of these thoughts with me?"
p "..."
p "No... It's embarassing"
show cg mila_paul_hj_idle with dissolve
m "Pretty please?"
p "Sweetheart, no"
m "Pretty pretty please?"
p "..."
m "I'll owe one wish if you do"
p "..."
p "{size=-10}Fine..."
m "Hehe"
p "..."
m "So?"
m "I'm getting excited"
p "Remember the last time, when we were in the restaurant with my colleague?"
m "..."
m "{w}..."
show cg mila_paul_hj_smile with dissolve
m "Oh! I do! We ate steaks. Bad ones."
p "Yes. Also, you were sitting opposite me, and one of my colleagues was sitting next to you."
m "Right!"
p "..."
p "I... {w}Imagined... {w}Multiple times..."
p "That you were giving him a handjob that time under the table..."
m "{w}..."
show cg mila_paul_hj_worried with dissolve
m "How... {w}How did you know?"
p "...What?"
m "I thought we were being discreet..."
m "I covered my hand with a napkin"
m "Then, I unzipped his pants and took his penis in my hand"
m "Do you remember the moment he gasped in surprise?"
p "..."
m "Yeah. And then I started to move my hand"
show cg mila_paul_hj_smile with dissolve
m "Like this"
m "But I tried to do it slow to not get caught"
m "And then..."
show cg mila_paul_hj_open with dissolve
p "Urgh..."
p "Fuck!"
m "Ahaha!"
m "Mmm..."
m "Give me that sweet cum, honey..."
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
scene mila_paul_hj_cum_1 with flash
p "Ohhh yess..."
scene mila_paul_hj_cum_2 with dissolve
m "..."
scene mila_paul_hj_cum_3 with flash
p "Mmm..."
scene mila_paul_hj_cum_4 with dissolve
m "Hehehe..."
scene mila_paul_hj_cum_5 with dissolve
ms "Paul looked at me with a satisfied smile on his face"
ms "I smiled back"
m "..."
ms "I tenderly milked the last drops of his cum and sucked it"
p "Mmm..."
p "You are the best..."
m "hehe"
m "{w}..."
scene bg apartments with dissolve
ms "I stood up and was about to go to the bathroom"
p "Wait..."
m "?"
show mila robe_cum_idle at center
p "Was it real? {w}I mean... {w}Have you..."
m "{w}..."
show mila robe_cum_angry at center
m "Of course not, silly!"
m "I won't do something that could hurt you!"
m "Do you think I am capable of betrayal?"
p "..."
p "No..."
p "Also you look hot when you are angry and covered in cum"
show mila robe_cum_confused at center
m "{w}..."
show mila robe_cum_smirk at center
m "..."
m "You think?"
p "Yeah..."
m "Imagine then..."
m "That's it's not your sperm..."
show mila robe_cum_wink at center with dissolve
pause 0.5
show mila robe_cum_smirk at center
p "..."
p "Holy shit..."
m "Hehehe"
m "And also..."
show mila robe_cum_wink at center
ms "I leaned close to his ear and whispered"
m "{size=-15}If you ever want me to jerk off to someone else..."
m "{size=-15}Just ask"
p "!!!"
m "I owe you one, remember?"
p "..."
p "You are a little devil..."
show mila robe_cum_smirk at center
m "..."
m "Last time I checked, I was your angel..."
p "..."
p "I love you"
m "..."
p "I love you too"
if _in_replay:
    return
"{w}..."


label v122:
scene bg kitchen
"{w}..."
"..."
show mila robe_think at center
ms "The next day I got up early and cooked a lunch."
ms "I tried even harder than I did for Paul."
ms "In the end, my food is nothing more than a routine for him..."
ms "But for Bob... {w}It's something much more..."
ms "That's why I put a lot more effort in it"
show mila robe_blush_shy_looking_aside at center
ms "I kept remembering the thrill of his gaze"
ms "It resembled some forgotten feeling for me..."
ms "Something that I thought I wouldn't feel again..."
ms "And that's why... {w} I wanted even more..."
show mila robe_blush_smirk at center
ms "Something more thrilling... {w}Something more daring..."
ms "Something, that will make Bob more confident..."
ms "Something, that makes me feel different..."
ms "Something, that will shut up his \"compassionate\" colleagues..."
ms "..."
ms "..."
show mila robe_puzzled at center
ms "Hmmm..."
ms "..."
show mila robe_smile_open_mouth_excited at center
ms "Oh!"
show mila robe_think at center
ms "I put on thick lipstick and kissed the napkin."
ms "..."
show mila robe_blush_smirk at center
ms "Heh."
ms "Looks erotic."
ms "I put it on top."
show mila robe_think at center
ms "..."
ms "I would like to add something else..."
ms "..."
show mila robe_smile_grin at center
ms "I grinned at my thoughts, {w} pulled down my panties and put them on the bottom."
ms "There was a speck of my pussy juice in the middle."
ms "Hehe."
ms "Exactly what is needed."
ms "He should find them after lunch."
ms "..."
show mila robe_smile_awkward_open_mouth at center
ms "Carried away by my thoughts, I again almost missed the quiet knock on the door."
scene bg door
show mila robe_smile_awkward_open_mouth at center:
    linear 1.0 xpos 0.9
ms "I rushed to the door and opened it - I was afraid that Bob would quickly change his mind and leave."
ms "Seeing his puzzled face, I couldn't help but smile."
show mila robe_smile_open_mouth at right
m "Hello Bob."
show bob waving at left:
    xzoom 0.9 yzoom 0.9
bob "H-Hello..."
m "..."
bob "..."
show mila robe_smile_awkward_angry at right
m "..."
ms "I need to do something with this awkward atmosphere and pauses someday..."
show mila robe_smile_open_mouth_excited at right
m "Here you go."
ms "I handed him a bag of containers."
show bob surprised at left:
    xzoom 0.9 yzoom 0.9
bob "..."
ms "He looked at me in confusion."
bob "What is this?"
show mila robe_proud at right
m "This is your lunch."
bob "..."
m "Eat in the company of colleagues."
show mila robe_smile_grin at right
m "Make them envy you!"
bob "..."
show mila robe_puzzled_frown at right
m "..."
bob "..."
ms "Bob was silent for a while and then shouted:"
show bob waving at left:
    xzoom 0.9 yzoom 0.9
bob "No no no! I can't accept this!"
show mila robe_shhhh_finger at right
m "Shhh!"
ms "I put my finger to my lips."
show mila robe_smile_awkward_open_mouth at right
m "Be quiet!"
m "Or you will wake up the neighbors."
bob "..."
show mila robe_smile_open_mouth at right
m "You wanted to tease these idiots, right?"
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "..."
bob "Yes…"
m "Here you go. {w}Okay, I need to prepare lunch for Paul as well. {w}So have a nice day, and good luck to you."
show bob smile at left:
    xzoom 0.9 yzoom 0.9
bob "Thank you!"
ms "His smile was so sincere and good-natured that I couldn't stand it and turned away."
show mila robe_sad at right
ms "I felt like the bully..."
ms "Like I am the bad guy who is lying to the pure hearted kid..."
ms "I couldn't stand it and just closed the door."
play sound "door-open-close.mp3"
show mila robe_sad_tears at right
ms "Crap…"
ms "This is unfair…"
ms "I better not screw it up..."


"{w}..."
scene bg apartments
ms "I did my daily chores and lay down on the sofa to get some rest"
bob_message "Hello, Mila."
bob_message "I have a strange request..."
bob_message "Can I call?"
ms "I quickly checked my reflection in the mirror, made some adjustments and started the video call."
show cg videocall_smile at center:
    xzoom 0.8 yzoom 0.8
ms "When he answered the phone, I burst into a smile."
m "Hello, my bear! {w}How was your lunch today?"
show cg videocall_wink
m "I am not that confident in my cooking skills, but I am pretty sure that I'll get good with some practice"
show cg videocall_smile
bob "Bob's eyes darted from side to side."
bob "W-we... {w}Erm... {w}Everybody can hear you..."
show cg videocall_surprise
ms "I feigned surprise."
show cg videocall_closed_eyes_smile
m "Oh, sorry! Are you in the office? {w}If there is someone nearby - forgive me!"
bob "..."
show cg videocall_smile
m "..."
bob "..."
show cg videocall_smile_awkward
m "Hello? Connection was lost?"
show cg videocall_smile
bob "N-no... This... I just didn't know how to answer..."
ms "A man picked up the phone and stared at the camera."
ms "Next to him were several other people in suits."
show cg videocall_smile_awkward
ms "I put on a polite smile and waved at them."
ms "..."
ms "They looked at me for several long seconds."
ms "When I started to feel uneasy, one of them asked:"
bob_unknown "Are you seriously dating Bob?"
show cg videocall_shy_giggle
ms "I faked embarrassment."
m "H-he said that?"
ms "I pressed my hands to my cheeks and giggled."
m "W-we didn't say any vows, but if Bob says so... hehehe..."
bob_unknown "..."
bob "..."
hide cg videocall_shy_giggle
ms "Silence reigned again for some time, which then exploded with their shouts"
ms "I listened to them and tried my best not to yell at them back"
show mila robe_smile_awkward_angry at right
bob_unknown "Oh come on!"
bob_unknown "Why the hell is such a cutie with this shitfuck?!"
bob_unknown "Can't she find anyone better?"
bob_unknown "What a joke!"
bob_unknown "{size=-12}Our ugly Bob has a girlfriend and I don't? Life is unfair..."
bob_unknown "I don't believe it... I can't believe it..."
ms "For some reason, their reaction irritated me. Much more than I thought."
hide mila
show cg videocall_cold_smile at center:
    xzoom 0.8 yzoom 0.8
m "I'm sorry? Why do you talk about my Bob like that? It's rude!"
ms "The voices gradually died down."
bob_unknown "The man holding the phone answered."
bob_unknown "We just love Bob too much, you see?"
ms "Someone laughed behind him."
ms "I gritted my teeth but remained silent."
bob_unknown "We just don't want anyone to take advantage of his… “good side”"
show cg videocall_smile_awkward
ms "I put on a smile."
ms "Yeah, sure. {w}Tell me a story"
m "Oh really? {w}Thank you! {w}You all are so kind!"
bob "..."
bob_unknown "Would you mind joining our evening get-together tonight?"
show cg videocall_happy_smile_open_mouth
ms "I feigned joy."
m "Oh, with pleasure! Now can you pass the phone to Bob?"
hide mila robe_smile_awkward_angry
"{w}..."
hide cg videocall_happy_smile_open_mouth
ms "We chatted some more, but he was so embarrassed that he was talking nonsense."
ms "So I ended the conversation without even having a chance to tease him properly."
ms "The conversation left a nasty aftertaste."
ms "I felt anger and irritation that I hadn't felt in a long time."
ms "They don't believe that someone could date Bob purely out of desire? I'll show you, assholes."
bob_message "You don't have to do this..."
ms "Bob was writing something else, but didn't have time to send the message. I answered faster."
ma "I want to do this."
ma "So I'll come."
ms "I wanted to cheer him up, so I chose a better angle and took a selfie."
play sound "shot.mp3"
ms "..."
show bob_selfie1x at right:
    xzoom 0.75 yzoom 0.75
    ypos 0.9 xpos 0.95
md "{image=bob/One use/bob_selfie1.webp}"
hide bob_selfie1x
"..."
ms "I waited a couple of minutes, but Bob didn't answer"
show mila robe_curious
ms "I opened the closet and started choosing an outfit."
m "Hmmm..."
bob_message "You are very beautiful, Mila..."
show mila robe_proud
ms "..."
ms "Oh he is so sweet..."
show mila robe_smile_awkward_angry
ms "..."
ms "It's just made me even more angry at his so-called \"Friends\""
show mila robe_blush_smirk
ms "Alright"
ms "Operation \"make them jealous\" has officially started"
ms "My goal is to look sexy and modest at the same time"
show mila robe_curious
ms "..."
ms "Hmmm"
ms "How about this?"
show mila dress_front:
    xzoom 1.1 yzoom 1.1
ms "..."
ms "Well it's definitely sexy"
ms "But..."
show mila dress_back
ms "I look like a prostitute..."
ms "I think I need to try something else"
ms "..."
show mila summerdress_front:
    xzoom 1 yzoom 1
ms "..."
ms "This one looks nice"
ms "I like the color and the image overall"
show mila summerdress_back
ms "..."
ms "But... {w} With Bob I will look like a crazy person with daddy issues..."
ms "..."
ms "..."
show mila summerdress_front
ms "Am I a crazy person with daddy issues?"
"{w}..."
ms "No... {w} I think... {w} Anyway, lets try something else..."
ms "..."
show mila jeans_and_blouse_front:
    ypos 0.95
ms "..."
ms "..."
show mila jeans_and_blouse_back
ms "..."
ms "So?"
ms "..."
ms "I guess it's ok..."
ms "I don't have time to choose something different"
ms "Let's go with this"
"{w}..."


scene bg taxi
play sound "car_door.mp3"
"..."
ms "I got into a taxi and texted Bob that I would be there soon."
bob_message "You really want to come?"
bob_message "I am not sure that it's a good idea..."
ma "I already coming, Bob"
"..."
ms "Bob didn't answer"
"{w}..."
play sound "car_door.mp3"
"..."
show bg mila_and_car:
    ypos 1.0
    linear 4.0 ypos 2.65
ms "Getting out of the taxi, I almost tripped."
ms "I haven't worn heels for a long time..."
ms "I took a moment to gather my thoughts, and went into the cafe."
play sound "shop_door.mp3"
"..."
scene bg cafe
ms "There were lots of people inside"
ms "The loud noise of dozens of people talking, whispering, yelling and laughing - all at the same time, filled my ears"
show mila jeans_and_blouse_front
ms "I found Bob at the corner with a bottle of beer in his hand, he nervously looked at me"
ms "I wasn't sure what his face looked like - he looked like he was worried even more than usual and relieved at the same time"
show mila jeans_and_blouse_waving
ms "I smiled, waved at him and yelled"
m "Hi, my daddy bear!"
ms "For a moment all conversation fell silent."
ms "Dozens of eyes stared at me"
show mila jeans_and_blouse_run_smile
ms "I tried to ignore them and ran towards Bob."
bob_unknown "..."
bob_unknown "{size=-12}(whispers) I don't believe this is real..."
hide mila
show milaandbob lap_surprise at right:
    xpos 0.9
ms "I got near Bob, hugged him and sat on his lap."
ms "Several colleagues still looked at us in disbelief, so I pressed my cheek to Bob and kissed him."
"..."
bob_unknown "{size=-12}(whispers) Fuck this world..."
show milaandbob lap_blush
ms "..."
ms "Hehe."
ms "No, fuck {b}you{/b}, idiots."
ms "I felt something hard pressed against my thigh."
ms "..."
show milaandbob lap_blush2
ms "Something? {w}It's Bob's dick, Mila..."
ms "I suppressed my embarrassment"
ms "After all, this is a completely natural reaction."
ms "..."
show milaandbob lap_blush2_looking_aside
ms "Not to mention I enjoy his excitement."
show milaandbob lap_smirk_lookin_at_bob
ms "I looked at Bob and smiled slyly, letting him know that I had noticed."
show milaandbob lap_smirk_lookin_at_bob_looking_away
ms "He turned away embarrassed."
ms "Hehehe."
ms "..."
show milaandbob lap_blush2_looking_aside
ms "Bob's colleagues insisted that I drink with them, but I managed to refuse, citing poor alcohol tolerance."
bob_unknown "If you won't drink with us, at least tell us how you met Bob?"
ms "I tried to answer, but another man yelled:"
bob_unknown "Better tell us where can I \"meet\" with you too?"
ms "The crowd burst into laughter"
show milaandbob lap_smile
ms "I answered with a polite smile, like I didn't get \"the joke\"."
ms "Drunks always make shitty jokes"
ms "Still, sitting on Bob's lap was the right choice."
ms "This way I immediately made it clear who my man is."
ms "..."
show milaandbob lap_blush2_looking_aside
ms "The very thought made me shiver."
ms "My man is Paul, {w}not Bob...{w} Yet I'm sitting on his lap and rubbing my ass against his erect dick..."
ms "I again felt as his cock pressed against my ass, but this time its combat readiness caused me not tenderness, but desire."
ms "I feel like some kind of slut."
ms "..."
show milaandbob lap_blush_closed_eyes
ms "Mmm…"
ms "I suppressed my moan, but failed to suppress my desire to rub my slit against Bob's cock"
ms "Bob gently placed his hand on my waist and whispered:"
show milaandbob lap_blush_hand_on_waist_looking_at_eachother
bob "I need to go... To the restroom."
ms "His gentle touch and hot breath caused a new flock of goosebumps that jumped along my spine."
hide milaandbob lap_blush_hand_on_waist_looking_at_eachother
ms "As soon as Bob left, one of his fellow harassers moved closer and put his hand on my knee."
show cg hand_on_knee at center:
    xzoom 0.6 yzoom 0.6
    ypos 0.8
"..."
bob_unknown "Tell me honestly, how much does he pay you?"
ms "I was stunned by this question."
bob_unknown "I'll pay three times more than he pays you for a month just for one night."
bob_unknown "Do you do anal?"
hide cg hand_on_knee
ms "For a brief moment I couldn't believe what I just heard"
ms "But then..."
show mila jeans_and_blouse_angry_open at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
play sound "slap.mp3"
"SLAP!"
ms "I threw his hand off and slapped his face."
m "What do you think I am?!"
show mila jeans_and_blouse_angry_close
bob_unknown "..."
m "..."
ms "The whole cafe became quiet."
bob_unknown "..."
ms "I stood up and looked at everyone around me with contempt."
show mila jeans_and_blouse_angry_open
m "I seriously hoped that it was just my imagination."
m "That you really respect him and understand what a good person Bob is."
show mila jeans_and_blouse_angry_close
ms "I looked at the man who had just offered me money."
show mila jeans_and_blouse_angry_disgust_open
m "The only whore at this table is you."
m "I'm sure your friends will pay you triple to fuck you in the ass."
show mila jeans_and_blouse_angry_close
ms "I looked around and noticed that Bob had already returned from the toilet and was standing a couple of steps away from me with his mouth open."
show bob surprised at left:
    xzoom 0.8 yzoom 0.8
show mila jeans_and_blouse_angry_open
m "We're leaving Bob."
m "I urgently need to fuck someone."
ms "The arrogant man who was trying to buy me turned pale and fell silent."
ms "I glanced at him with contempt"
show mila jeans_and_blouse_angry_disgust_open
m "A real {b}MAN{/b}"
show mila jeans_and_blouse_angry_close:
    easein 0.5 xpos 0.25
    linear 0.4 xzoom -1.0
ms "I took Bob's hand and walked to the exit."
show mila jeans_and_blouse_angry_open:
    easein 1 xpos 0.8
show bob surprised at left:
    xzoom 0.8 yzoom 0.8
    easein 1 xpos 0.5
m "Have a shitty evening, dickheads"
bob_unknown "..."
"..."
play sound "shop_door.mp3"


scene bg night_city
ms "When we moved a considerable distance from the cafe and my anger evaporated, I felt ashamed of what I had done."
ms "I sighed."
show mila jeans_and_blouse_remorse at center
m "Sorry, Bob... I couldn't resist."
show bob smile at left:
    xzoom 0.8 yzoom 0.8
ms "He scratched the back of his head in embarrassment."
bob "No, you don't have to apologize... {w}It's me... {w} You know?.. {w}And no one before... {w} Like, in general..."
ms "Bob looked at me and smiled."
show bob idle
bob "Thank you."
show mila jeans_and_blouse_run_smile
m "Hah."
m "My pleasure."
show bob smile
bob "To be honest, I even liked it."
show mila jeans_and_blouse_proud_smile
ms "I returned his smile."
ms "Bob didn't take his eyes off me for a long time."
bob "You smile so beautifully..."
show bob sad
ms "..."
show mila jeans_and_blouse_blush_embarassed
ms "Stop... {w}Your embarrassing me..."
show mila jeans_and_blouse_blush_embarassed_twist_hair
m "T-thank you..."
show bob shy
bob "Sorry…"
show mila jeans_and_blouse_surprise
m "???"
ms "I looked at him in surprise."
m "For what?"
show bob sad
bob "I think I've fallen in love with you."
show mila jeans_and_blouse_shock
m "Everything suddenly slowed and then stopped."
ms "..."
m "What?"
show bob sad2
bob "I love you, Mila."
ms "Bob smiled sadly."
show mila jeans_and_blouse_panic at center with hpunch
m "..."
ms "Crap…"
ms "Crap!"
ms "Fuck fuck fuck!"
show mila jeans_and_blouse_sad_looking_aside
m "I…"
ms "Bob raised his hand in a stopping gesture."
show bob waving
bob "Don't sweat it... {w}Everything is fine."
bob "I already know your answer..."
show bob sad
ms "His eyes became dull and empty again."
show mila jeans_and_blouse_sad_looking_down
ms "Damn Mila! You can't play with people's feelings..."
ms "What am I doing?"
ms "I can't leave him to his fate now."
ms "We are responsible for those who fall in love with us!"
show mila jeans_and_blouse_sad_looking_up
m "..."
show mila jeans_and_blouse_sad_looking_up:
    easein 0.5 xpos 0.35
show bob sad
ms "Bob turned and was about to move on, but I grabbed his arm, forcing him to look at me."
m "Wait."
ms "Life returned to Bob's eyes for a moment, but almost immediately went out again."
show mila jeans_and_blouse_serious_open_mouth
m "I'm married Bob. And I love my husband."
show bob sad2
ms "Bob chuckled and nodded."
bob "I know."
m "But…"
ms "I closed my eyes."
show mila jeans_and_blouse_blush_looking_aside
m "I'll think about what... {w}we can do..."
show bob sad
ms "Bob frowned."
bob "What do you mean?"
"..."
"..."
show mila jeans_and_blouse_front
m "Lets go."
bob "..."
bob "Where to?"
show mila jeans_and_blouse_run_smile:
    easeout 1 xpos 0.65
show bob sad:
    easeout 1 xpos 0.25
m "To home, where else?"
ms "I pulled him along with me."
bob "Mila..."
ms "Bob protested hesitantly, but followed."
ms "I turned around and winked at him."
show mila jeans_and_blouse_smile_wink
m "Leave it to me!"
bob "..."
hide mila
hide bob
"{w}..."
scene bg doors
ms "I left Bob at the door to his apartment and told him to come by for his lunch tomorrow morning."
ms "He still looked at me in disbelief, but agreed."



"{w}..."
scene bg apartments
play sound "door-open-close.mp3"
show mila jeans_and_blouse_sad_looking_aside at center
ms "Entering the apartment, I could not stand it and burst into tears"
ms "Bob's feelings and his confession were so pure ... {w} so sincere"
ms "Something broke in me ..."
ms "On one hand, I was happy."
show mila jeans_and_blouse_sad_looking_up
ms "It is stupid to deny that I like Bob. {w} As a person. {w} As a friend. {w} As a man ..."
ms "I have never experienced this before ... {w} Never before have I had to refuse after confession."
ms "The only other person who had confessed to me was Paul..."
ms "It somehow happened that everyone around us knew that we were dating and that everything was fine in our relationship..."
ms "Maybe that's why no one tried to confess to me ..."
ms "But this feeling ... {w} devastation ... {w} betrayal ..."
ms "I can't describe it ..."
ms "It broke me from the inside. {w} I want to support Bob ... {w} to give him happiness ..."
ms "But I can't..."
show mila jeans_and_blouse_sad_looking_up:
    linear 1.0 xpos 0.75
show paul suit_shock at left
p "Babe?"
show mila jeans_and_blouse_sad_looking_aside
m "..."
p "What's happened?"
ms "I didn't know how to answer"
ms "I didn't know where to start"
ms "I was so confused, {w} my thoughts are intertwined with each other, {w}, and it gave rise to strange meanings and images"
ms "I silently let them out"
p "Sunshine?"
label first_nts_choice:
    show screen nts_stats_overlay

    menu:
        "Mila was lost in her thoughts. Paul should:"
        "Push her to answer (Mila's submissiveness + 1)":
            $ dom += 1
            jump push
        "Let her be, she will talk when she is ready (Mila's dominance + 1)":
            $ mila_dom += 1
            jump slide

label push:

show paul suit_frown:
    easeout 1.0 xpos 0.45
show mila jeans_and_blouse_sad_looking_up:
    linear 1.0 xpos 0.75
ms "Paul took my hands, which pulled me out of the whirlwind of emotions."
hide screen nts_stats_overlay
show mila jeans_and_blouse_run_smile
ms "I looked at him with gratitude and smiled"
p "What's happened?"
ms "His voice sounded stricter and tougher"
ms "This had a beneficial effect on me"
ms "Finally, my thoughts fell into place, and I was able to calm down."
jump lovetalk

label slide:

show mila jeans_and_blouse_sad_looking_down
ms "Subbed in my thoughts, I did not notice how a mug of hot chocolate appeared in my hands."
hide screen nts_stats_overlay
ms "I don't know how much time had passed, but I was able to calm down and put my thoughts in order."
ms "Paul was silently waiting."
show mila jeans_and_blouse_run_smile
ms "I smiled gratefully at him."

label lovetalk:

show mila jeans_and_blouse_serious_open_mouth
ms "I told Paul what happened."
ms "About Bob's colleagues. {w} About our meeting in a cafe. {w} and about his confession."
ms "Paul listened carefully to me. And at the moment, he only sighed."
show paul suit_frown
p "I knew this could happen..."
m "..."
p "..."
show mila jeans_and_blouse_sad_looking_aside
m "This sucks, huh?"
ms "My voice trembled. {w} I did not understand how I felt."
ms "But I understood that if Paul were to say something cruel now, I wouldn't be able to stand it and would do something..."
ms "And would regret it afterwards."
show paul suit_sad
p "..."
p "I'm afraid even to imagine myself in his place ..."
ms "..."
show mila jeans_and_blouse_surprise
ms "How could I think that he would say something harsh?"
ms "He is my husband after all... {w}For a reason."
ms "..."
show mila jeans_and_blouse_sad_looking_up
m "I... Me too ... {w} I don't know how to react to this ..."
p "..."
m "..."
p "..."
show mila jeans_and_blouse_serious_open_mouth
m "Listen ... {w} Do you ... {w} do you remember how it feels like? {w} To be in love?"
p "..."
show paul suit_frown
p "I am not sure what do you mean...{w} I love {b}you{/b}. {w} Not a bit less than I loved you ten years ago."
ms "A warm feeling spilled over my body"
show mila jeans_and_blouse_run_smile
m "I love you too."
p "..."
m "But I'm not talking about that. {w}I mean ..."
show mila jeans_and_blouse_sad_looking_down
m "Do you remember those feelings, when you fell in love?"
show mila jeans_and_blouse_sad_looking_up
m "Remember how often your heart beat faster at the thought?"
show mila jeans_and_blouse_sad_looking_aside
m "What happened during the day kept repeating in your memory over and over again."
show mila jeans_and_blouse_sad_looking_down
m "How desperately, even painfully, you wanted to touch, cuddle, hug and kiss?"
p "..."
show paul suit_shock
p "Certainly. {w}And I still feel it. {w}For me nothing has changed ..."
show mila jeans_and_blouse_angry_close
ms "I frowned."
m "No. {w} Something has changed."
show mila jeans_and_blouse_serious_open_mouth
m "Sometimes it seems to me that you are tired of me..."
m "That I am no longer the most beautiful and desired girl for you... {w} That I am just boring..."
show mila jeans_and_blouse_sad_looking_down
m "Everything you say and do for me is the same routine for you as going to work."
p "..."
show paul suit_frown
p "You are wrong..."
show mila jeans_and_blouse_run_smile
m "I know. {w} I mean... {w} Now I know."
show mila jeans_and_blouse_sad_looking_aside
m "But this feeling ... {w}This fatigue ..."
m "It is inside. {w} it is. {w} It has not disappeared."
show mila jeans_and_blouse_sad_looking_up
m "And Bob's words ... {w} They woke something in me."
show mila jeans_and_blouse_sad_looking_down
m "The thrill. {w} Forgotten thrill of love ..."
show screen nts_stats_overlay
menu:
    "Should Paul do something?"
    "Take the initiative, show her your love (Mila's submissiveness + 1)":
        $ dom += 1
        $ paul_took_initiative = True
        jump cafe
    "It's better to give her some space to let her figure out her feelings (Mila's dominance + 1)":

        $ mila_dom += 1
        jump chat

label cafe:
p "..."
show paul suit_open_mouth_neutral
p "You know. I have an idea."
hide screen nts_stats_overlay
show mila jeans_and_blouse_surprise
m "?"
p "Let's go."
m "What? {w}Where to?"
p "Let's go, I'll tell you along the way"
m "..."
n "{w}. {w}. {w}."
scene mall
show mila jeans_and_blouse_serious_open_mouth
m "And? {w} What are we doing here?"
show mila jeans_and_blouse_serious_open_mouth:
    linear 1.0 xpos 0.75
show paul suit_grin:
    xpos 0.25
ms "Paul only grinned in response and pulled me toward the clothing store."
"..."
show paul suit_frown
show mila jeans_and_blouse_run_smile
m "What are we looking for?"
ms "Paul sorted out different dresses and outfits with a dissatisfied face"
p "We are choosing a dress for you"
show mila jeans_and_blouse_front
ms "Paul pull out another dress, grimaced and put it back"
ms "I ran through the racks with my eyes"
ms "I already had a couple of dresses at home, which I never wore."
ms "All the same, we never go to places where wearing them would be appropriate..."
show mila jeans_and_blouse_serious_open_mouth
m "Dear, I have dresses. If you warned me beforehand, I would put one on for you."
ms "Paul looked at me thoughtfully"
ms "He seemed to pick up on my words because he could not formulate what he wanted to do."
show paul suit_open_mouth_neutral
p "I want to...{w} dress you up."
p "Somehow in a special way ..."
show paul suit_blush_looking_aside
p "And boast. {w}Kind of... {w}Like: {w}Everyone, look - {w}this girl is with me."
p "Something like that..."
m "..."
show mila jeans_and_blouse_run_smile
ms "I smiled"
m "Do you have something in mind?"
show paul suit_frown
ms "Paul returned to the shelves"
p "Not really... {w} I want something more... {w} {size=-10} frank."
show mila jeans_and_blouse_blush_embarassed
ms "My heart was beating quickly..."
ms "My body had become warm.{w} My clothes suddenly became prickly and stiff {w}and my skin has become too sensitive."
ms "I swallowed"
ms "These sensations..."
show mila jeans_and_blouse_blush_embarassed_twist_hair
ms "They were not like love"
ms "They were not similar to anything previously experienced"
ms "I wanted Paul to tell me what to do"
ms "I wanted him to praise me"
show mila jeans_and_blouse_blush_looking_aside
ms "So that he looks at me and only me"
ms "So he boasts of me"
ms "So he'd use me. {w} As a thing."
ms "So that other people desired me."
ms "So that Paul decides who will be worthy of me"
show mila jeans_and_blouse_run_smile
m "Maybe something like this?"
ms "I pointed to a red short dress with an open back"
ms "Excitement fogged my mind"
ms "Paul looked at me in surprise and at the dress I chosen"
show paul suit_open_mouth_neutral
p "Are you sure?"
m "..."
p "..."
show mila jeans_and_blouse_proud_smile
m "If my husband wishes, I can even go naked"
ms "I myself did not believe what I said"
ms "But if Paul really told me to undress"
show mila jeans_and_blouse_blush_looking_aside
ms "I would obey"
p "..."
m "..."
show paul suit_blush_looking_aside
p "Then... {w}Let's try it on"
p "And this"
ms "Paul handed me high-heels shoes"
show mila jeans_and_blouse_surprise
m "..."
m "I'm afraid I can't walk in them"
p "..."
show paul suit_open_mouth_neutral
p "Then I will carry you."
show mila jeans_and_blouse_blush_looking_aside
m "..."
m "Ok..."
scene changing room
ms "I went in the fitting room"
n "{w}. {w}. {w}."
show mila sly_dress_shy at right:
    xpos 0.75
m "..."
show paul suit_shock:
    xpos 0.3
p "..."
m "..."
m "Well?"
show paul suit_open_mouth_blush
p "You look amazing"
show mila sly_dress_shy_giggle
m "..."
m "Hehe"
p "And very sexy"
show mila sly_dress_shy
m "..."
show paul suit_open_mouth_neutral
p "Turn around"
show mila sly_dress_from_behind
m "..."
p "..."
show paul suit_open_mouth_blush
p "Your ... {w} {size=-10} ass {size=+10} looks awesome"
ms "Paul's voice became a little quieter. Apparently, it was still difficult for him to play the brutal macho."
ms "I hid a smile and curled my back to provide him with the best view"
show mila sly_dress_from_behind_arched_back
p "Ahem ... {w} we'll take it!"
show mila sly_dress_shy_giggle
m "..."
m "Well ... what's next?"
show paul suit_grin
ms "Paul grinned."
p "Now we go to the restaurant."
"{w}. {w}. {w}."
scene bg restaurant
show mila sly_dress_neutral:
    xpos 0.5 ypos 0.1
show paul suit_shock:
    xpos 0.15
"???" "Welcome!"
show mila sly_dress_shy:
    easeout 1 xpos 0.085
ms "As soon as we went inside, a young waiter met us"
ms "We both were to embarrassed to look at each other, so I instinctively hid behind Paul"
ms "He tried his best not to look at my neckline and focused on Paul alone"
"..."
ms "Music played quietly"
ms "There were not that many dinners in the restaurant"
show mila sly_dress_from_behind:
    xpos 0.5
hide paul
ms "While we were walking to the table, I tried to pull the dress down, because it was striving up, exposing my ass"
ms "I literally felt people gazes aimed at me"
show mila sly_dress_shy
ms "... {w}It's so embarassing"
ms "But {w}I like it"
ms "..."
hide mila
ms "Paul ordered a bottle of wine and insisted that I drink a couple of glasses."
ms "It's kinda cleared my head and fogged my thoughts at the same time."
show big mila_table_relaxed_from_left
ms "A smile appeared on my face, all the nervousness and today's events disappeared somewhere."
ms "Only excitement remains."
ms "Paul noticed a change in my mood."
show big paul_serious_open_mouth_from_right with wipeleft
p "I want you to do something for me."
show big mila_table_intrigued_from_left with wiperight
m "?"
ms "I leaned forward to be closer to him."
m "You have all my attention."
show big paul_serious_open_mouth_from_right with wipeleft
p "I want you to show your tits to someone in here."
show big mila_table_surptised_from_left with wiperight
ms "..."
ms "If not for wine, I would be scared and refuse."
show big mila_table_smirk_from_left
ms "But I just smiled and took a couple more sips."
m "To whom for example?"
show big paul_serious_open_mouth_from_right with wipeleft
p "How about that man near the toilet?"
show big mila_table_profile_looking_to_the_side_from_left with wiperight
ms "I looked where he pointed."
show big mila_table_smirk_from_left
m "Sure"
"{w}. {w}. {w}."
hide big
show mila sly_dress_from_behind_arched_back
ms "I got up and, cat walked towards the man"
ms "I no longer cared that the dress pulled up and opened a clear view on my ass"
ms "Quite the opposite. {w} I would like to show even more ..."
ms "I was still swaying in my heels a bit..."
ms "But apparently in order to confidently stand on them, you need only a little more confidence"
ms "And the wine did a great job with providing me with confidence"
ms "I straightened the strap so that it was easier for my chest to fall out."
ms "Approaching the man I pretended to be a little more drunk than I really was, and leaned over, pushing my tits together with my elbows"
show mila sly_dress_drunk_tits_out
m "I'm sorry"
"???" "..."
ms "The man looked at me and his gaze stopped at my chest."
show mila sly_dress_drunk_tits_out_pointing_finger
m "The door on the left is it a male or female toilet?"
ms "The man smiled unpleasantly, grabbed my hand tightly and pulled me towards the toilet."
"???" "To the right, let me help you out, girl."
scene bg toilet
play sound "door-open-close.mp3"
show mila sly_dress_scared
ms "I did not have time to come to my senses, he had already dragged me inside the booth."
ms "I was terribly scared, but couldn't scream; my throat was dry, and I could only mumble weakly."
show mila sly_dress_scared_open_mouth
m "W-wait ..."
show cg pinned_to_the_wall_scared_cry:
    xzoom 0.75 yzoom 0.75 ypos 1.0
    linear 1.0 ypos 0.025
show mila sly_dress_scared_open_mouth:
    linear 1.0 xpos 0.85
ms "But the man didn't listen to me"
ms "Before, when Paul was angry at me I felt fear"
ms "But that fear wasn't scary"
ms "It was that type of fear, that makes you horny"
ms "Like when you know, that this time sex will be rough"
ms "Rough, but... {w}safe."
ms "Because I knew Paul would never hurt me..."
ms "But now..."
ms "This fear wasn't exciting at all"
ms "This fear was ugly, {w}violent, {w}dangerous..."
ms "The only thing I wanted at that moment was to run away"
ms "..."
ms "The man pinned me to the toilet wall and reached for my tits"
ms "But luckily, he did not have time to do anything."
show cg pinned_to_the_wall_scared_cry_pleading_eyes:
    xzoom 0.75 yzoom 0.75 ypos 1.0
    linear 1.0 ypos 0.025
ms "The door swung open and Paul entered the toilet."
ms "The man looked at him displeasedly."
hide cg
"???" "I don't mind sharing, but I will be the first."
show paul suit_angry at left:
    xzoom -1
show mila sly_dress_scared
p "..."
p "..."
show paul suit_angry_open_mouth
p "It's not for you to decide"
show paul suit_angry_open_mouth:
    easeout 0.5 xpos 0.5
ms "Paul took my hand"
show paul suit_open_mouth_neutral
p "Come on, dear."
show paul suit_open_mouth_neutral:
    linear 0.5 xpos 0.25
show mila sly_dress_scared:
    linear 0.5 xpos 0.65
"???" "..."
show paul suit_open_mouth_neutral:
    linear 0.5 xpos 0.15
show mila sly_dress_scared:
    linear 0.5 xpos 0.35 xzoom -1
ms "The man did not interfere, and let us through."
ms "But he made a ugly grimace and spat on the floor."
"???" "Fucking cuckold."
m "..."
p "..."
play sound "door-open-close.mp3"
scene bg restaurant
show paul suit_sad at center
show mila sly_dress_scared at right:
    xpos 0.85
m "..."
p "..."
ms "The mood was spoiled."
ms "The wine fog instantly disappeared from my head."
ms "The playful mood was gone."
ms "We just called a taxi and returned home, not talking on the way back."
"{w}. {w}. {w}."
if _in_replay:
    return
jump lovetalk2

label chat:
scene bg apartments
show paul suit_frown at left
p "..."
show mila robe_think at right
ms "A tense silence fell on the room"
hide screen nts_stats_overlay
ms "Emotions and feelings overwhelmed me"
ms "Next to Paul, I always feel so protected and calm ..."
show mila robe_puzzled_frown
ms "But at the same time..."
ms "I wanted something else"
show mila robe_blush_shy_looking_aside
ms "And Paul also wants this, {w}I think ..."
ms "He is just too constrained by his principles to admit it"
ms "..."
show mila robe_sad
ms "Thoughts of Bob and his confession burst into my head"
ms "They mixed with the thoughts of my relationship with Paul, {w}about my grievances... {w}and about my actions."
show mila robe_puzzled_frown
ms "These feelings of trepidation... They are similar to what I felt when I texted with that guy from the app..."
ms "What was his name again?{w}... {w}Dick, I think?"
show mila robe_shhhh_finger
ms "..."
ms "Perhaps repeating that experience is worthwhile,{w} but this time, it should include Paul."
ms "It may help me to put my thoughts in order and understand if I am confusing excitement with love ..."
hide mila
scene bg mila_on_laps_smile
ms "I laid near Paul and took out my tablet."
ms "Paul silently pats my head."
ms "I snuggled to him to show that I liked it."
ms "..."
p "What's up?"
ms "..."
scene bg mila_on_laps_looking_up
m "Remember the site where I chatted with that man?"
p "..."
p "Yes."
ms "Paul's voice sounded a bit rude."
ms "Apparently he was not fully able to cope with his jealousy yet."
scene bg mila_on_laps_looking_up_open_mouth
m "I want us to chat there with someone."
scene bg mila_on_laps_looking_up
ms "Paul tensed."
scene bg mila_on_laps_looking_up_open_mouth
m "Together."
scene bg mila_on_laps_looking_up
p "..."
p "Together?"
scene bg mila_on_laps_smile
m "Yep. {w}Together."
ms "I looked at my husband."
scene bg mila_on_laps_looking_up_concerned
m "You don't like the idea?"
p "..."
m "..."
p "..."
scene bg mila_on_laps_smile
m "I'll take your silence as \"Yes\""
ms "After a couple of minutes of wandering on the site, I received a message from some guy."
ms "After banal representations, the conversation began to become more frank."
ms "..."
ms "Which is generally not surprising - knowing the subject of the site."
ms "..."
scene bg mila_on_laps_looking_up_open_mouth
m "He says that he would like to know my sexual preferences."
scene bg mila_on_laps_smile
p "..."
p "And what did you answer?"
scene bg mila_on_laps_looking_up_open_mouth
m "Nothing, yet"
scene bg mila_on_laps_smile
p "..."
m "I will write it like this: I love it when I am being used as an object."
scene bg mila_on_laps_looking_up_open_mouth
p "..."
scene bg mila_on_laps_smile
m "Kinda boring, don't you think?"
p "..."
m "How about: I love it when they punish me like I've been a bad girl."
scene bg mila_on_laps_looking_up_open_mouth
p "..."
p "Maybe it will be better to say: to fuck like a useless whore..."
m "..."
scene bg mila_on_laps_smirk
m "..."
scene bg mila_on_laps_smile
m "..."
m "He says that he fucks all his bitches like that."
p "..."
scene bg mila_on_laps_looking_up_open_mouth_giggle
m "I am pretty sure that those \"bitches\" are imaginary, though..."
p "..."
p "We all want to seem cooler than we are."
m "..."
scene bg mila_on_laps_looking_up_open_mouth
m "All except you."
scene bg mila_on_laps_smirk
m "You are already the coolest."
p "..."
scene bg mila_on_laps_smile
m "..."
m "He says that he wants to tie me up and fuck my head hole."
p "..."
p "Sounds hot..."
m "..."
scene bg mila_on_laps_looking_up_concerned
m "You think?"
m "..."
m "Then..."
scene bg mila_on_laps_shy
m "Would {b}you{/b} like to fuck my head hole?"
p "..."
p "Yeah, I think I do..."
m "..."
scene bg mila_on_laps_smirk
m "Do you want me to bring a rope?"
p "..."
p "You are so depraved ..."
scene bg mila_on_laps_looking_up_open_mouth_giggle
m "Hehehe"
p "..."
ms "The mood was too playful for my proposal to be turned into action"
ms "So I returned to the chat."
scene bg mila_on_laps_smile
m "..."
m "Oh! He asked to send a photo."
p "..."
p "This is dangerous, Mila."
m "I know."
p "..."
scene bg mila_on_laps_shy
m "..."
p "..."
p "Maybe if we take it without your face in it?"
m "..."
scene bg mila_on_laps_looking_up_open_mouth_giggle
m "{w}. {w}. {w}."
scene bg apartments
ms "I readily jumped out of bed and handed the phone to paul."
show mila robe_smile_grin at center
m "Tell me what to do."
p "..."
p "Untie the belt, {w}I think..."
ms "I obeyed without hesitation."
show mila robe_untied
ms "Goosebumps ran down the body."
ms "The black eye of the camera looked at me from Paul's hand."
ms "I felt like a rabbit before the snake."
ms "As if hypnotized, I expected my fate."
ms "I longed for this."
ms "The bathrobe flowed across my body, opening a view of the navel and pussy."
ms "I looked at the eye of the camera, and it looked at me."
p "..."
p "Show yourself"
show mila nude_think
m "I slowly threw off my bathrobe, exposing my body."
p "..."
p "Oh gods, you are so beautiful..."
show mila nude_blush
m "..."
ms "I had forgotten the last time Paul told of his feelings so openly."
ms "I hardly restrained myself, {w}I drove away the thoughts that I dream of being tied up."
show mila nude_blush_masturbate
ms "And wanted feel Paul's firm cock in my throat."
m "..."
p "..."
p "Ready."
show mila nude_surprised:
    pause 0.3
show mila nude_blush
ms "Paul's voice pulled me out of my thoughts."
ms "I took the phone and saw that he had already sent a couple of pictures to the guy."
show mila nude_blush_looking_aside
m "..."
ms "A tense-excited silence hung."
ms "To be honest, I no longer really wanted to continue texting with a stranger."
ms "But I decided that it was better to pump up Paul's excitement more"
show mila nude_reading_message_hand_on_hip
m "..."
m "He writes that I am very hot."
p "And I agree with him."
show mila nude_reading_message_hand_on_hip_grin
m "Hehe"
ms "I noticed that Paul's dick was swollen"
show mila nude_reading_message_hand_on_hip_biting_lips
ms "A little more and he will not be able to restrain himself..."
show mila nude_reading_message_hand_on_hip_annoyed
m "..."
m "He sent a dickpic"
p "..."
m "..."
p "..."
show mila nude_reading_message_hand_on_hip_annoyed_open_mouth
m "Who was the idiot who came up with the idea that there is someone who likes dick pics?"
show mila nude_reading_message_hand_on_hip_annoyed
p "..."
show mila nude_reading_message_hand_on_hip_annoyed_open_mouth
m "And now he wants to Facetime"
show mila nude_reading_message_hand_on_hip_annoyed
p "..."
show mila nude_reading_message_hand_on_hip_annoyed_open_mouth
m "Aaand now he's spamming with tons of messages."
m "Creepy..."
show mila nude_sad
ms "A moment and the mood was gone."
ms "The guy continued to make demands to take more photos, show my face and ask where I lived."
ms "Attempts to help him find at least a fraction of sanity did not lead to anything, so I just blocked him."
ms "..."
ms "..."
ms "The mood again became gloomy."
ms "And thoughts about the Bob's confession crawled into my head again."
"{w}. {w}. {w}."
if _in_replay:
    return

label lovetalk2:
scene bg apartments
ms "Feeling the tiredness from everything that happened, I decided to go take a shower"
scene 127_b-day_shower
ms "..."
ms "The jets of hot water helped me calm down and put my thoughts in order."
ms "But thoughts about Bob's confession still had not disappeared."
ms "They just stopped being so annoying."
ms "There was only a dull pain and resentment. {w} Towards life. {w} Towards fate. {w} Towards myself."
scene br
ms "When I left the bathroom and my eyes met Paul's, I realized that he was thinking similar thoughts."
scene bg apartments
show mila robe_puzzled_frown at right
show paul suit_sad at left
ms "We smiled sadly to each other."
m "..."
p "..."
p "Unpleasant feeling, right?"
show mila robe_smile_awkward_open_mouth
m "Yeah..."
p "..."
m "..."
show paul suit_open_mouth_neutral
p "What should we do?"
show paul suit_sad
show mila robe_curious
m "I don't know ... I'm not sure ..."
p "..."
m "..."
show paul suit_open_mouth_neutral
p "Listen ... {w} It seems to me that we both understand that our... {w}games ... {w}should not be thoughtless..."
p "This time we can say we were lucky. {w}But next time things could be much worse ..."
show paul suit_frown
ms "I just nodded in response"
m "..."
show paul suit_blush_looking_aside
p "That is why..."
ms "Paul hesitated, gathering his thoughts"
show mila robe_blush_shy_looking_aside
ms "He seemed to be fighting with himself, trying to choose the right words."
ms "I was waiting silently, trying not to interfere with the flow of his feeling and thoughts"
show paul suit_open_mouth_blush
p "I think we better not do this with some random strangers ..."
show mila robe_puzzled
ms "I only nodded in agreement. It is stupid to deny the obvious."
show paul suit_blush_looking_aside
p "It is better to do this with someone else... {w} with someone who is worthy... {w}of such attention..."
ms "It finally dawned on me what he meant."
show mila robe_blush_shy_looking_aside
ms "My body was again doused with heat."
ms "The experiences were replaced again by excitement"
ms "And this excitement prompted the solution to all problems at once."
show mila robe_blush_smirk
ms "I sat on Paul's lap and brought my face close to his."
ms "His dick had not yet managed to get swollen"
ms "Therefore, I began to slowly move my hips, rubbing my pussy of his cock."
scene bg mila_on_top_of_paul
m "You think?"
m "Where should I start?"
show screen nts_stats_overlay
menu:
    "What should Paul do?"
    "Tell his fantasy to Mila (Mila's submissiveness + 1)":
        $ dom += 1
        jump fantasy
    "Hesitate (Mila's dominance + 1)":

        $ mila_dom += 1
        jump mila_lead

label fantasy:
scene bg mila_on_top_of_paul
ms "Paul ran his hands along my hips and looked passionately at me."
p "I would like you to meet Bob naked."
hide screen nts_stats_overlay
ms "Hoo ... I did not expect him to be so straightforward."
m "..."
m "Do you think he can restrain himself and not attack me?"
p "Bob is not such a person."
p "I think he would be embarrassed and turn away."
scene bg mila_on_top_of_paul_giggle
m "Ahah, I think you're right."
ms "Paul's hands glided over my body and I felt growing excitement."
scene bg mila_on_top_of_paul
ms "My hips moved with a will of their own. My pussy simply demanded that I rub it on something."
ms "And conveniently, Paul's hardened penis was just in the right place."
p "Then you will give him his lunch ..."
m "..."
scene bg mila_on_top_of_paul_unsatisfied
m "And that's it?"
ms "I stopped for a moment."
ms "Paul smiled maliciously."
p "I knew that would not be enough for my whore-wife."
ms "His rude words made my nipples harden."
ms "I smiled embarrassedly."
m "Sorry..."
p "For what? I love you for who you are."
ms "Paul touched my pussy with his cockhead."
ms "I let it enter me and slowly pushed my hips down."
scene bg mila_on_top_of_paul_head_up
m "Ahhhh ..."
p "Good girl."
ms "I bit my lip and froze."
ms "Despite the fact that I unbearably wanted to feel every vein on his cock ..."
ms "I also wanted Paul to make me move ..."
p "Then you will kneel before him."
p "Take his cock in your hand..."
scene bg mila_on_top_of_paul
ms "I could not stand it and began to move my hips ..."
p "..."
p "And... {w}what will you do next?"
jump sex_paul

label mila_lead:
ms "Paul silently averted his eyes."
ms "It was still hard for him to admit his desires."
hide screen nts_stats_overlay
scene bg mila_on_top_of_paul_after_sex_kiss
ms "Therefore, I leaned closer kissed him and then whispered:"
m "I think we are ready to give a good... {w}tender... {w}handjob..."
ms "I moved my hand lower and stroked his rapidly hardening penis"
m "I think Bob has a fat and healthy cock."
ms "Paul closed his eyes and start to breathe rapidly"
ms "His dick was getting stronger and hotter in my hand."
ms "I began to stroke it slowly"
m "Tomorrow he will come to us"
m "And I will lower his pants..."
m "I'll kneel before him..."
ms "Paul's dick completely hardened."
ms "I guided it to my pussy that was already flooded with juices."
ms "Paul's hands were on my ass. He pulled me down."
ms "But I did not give in and only tease his cockhead with the wet lips of my pussy."
m "Imagine how surprised he will be..."
m "Most likely he will not be able to hold out for long and will want to cum on me ..."
m "But I will not let him end right away ..."
scene bg mila_on_top_of_paul_head_up
ms "I spread my lips with my second hand and lowered my hips, allowing his cock to get into me."
m "Mmm..."
ms "I could not hold back a moan."
p "Oh God..."
ms "I smiled"
scene bg mila_on_top_of_paul
m "Should I continue?"
p "Yes Yes! Baby you are the best!"
scene bg mila_on_top_of_paul_giggle
m "Ahah..."

label sex_paul:
scene bg mila_on_top_of_paul
m "Then I will open my mouth and look at Bob ..."
ms "It seemed to me that Paul's penis was much larger and hotter than usual..."
ms "Or maybe it was my pussy which was tightening more than usual."
ms "I moved slowly, plunging into my imagination"
scene bg mila_on_top_of_paul_head_up
m "Bob's heavy body hung over me"
m "His fat cock swayed in front of my nose ..."
m "I slowly lick his cockhead ..."
ms "I licked my lips they had suddenly became numb."
m "And then I take it in the mouth ..."
ms "Paul's penis touched the most pleasant places."
ms "And because of the slow movements it was possible to feel every millimeter of his dick..."
scene bg mila_on_top_of_paul
m "It does not fit in my mouth."
m "It is too thick and long for me."
m "I'm trying to swallow it deeper, but I can't ..."
ms "Paul's hands squeezed my buttocks."
scene bg mila_on_top_of_paul_head_up
ms "I felt an approaching orgasm ..."
ms "But I tried to stay on the verge, delay it ..."
ms "Although my consciousness slowly sailed in the realm of dreams ..."
ms "At the same time, I lost control of my actions."
ms "My hips began to move faster and faster ..."
m "Bob decides to help me ..."
m "He takes my hair ..."
m "AND..."
define flash = Fade(0.1, 0.0, 0.5, color="#FF0080")
scene bg mila_on_top_of_paul_head_up with flash
m "..."
scene bg mila_on_top_of_paul_after_sex_kiss with flash
p "..."
scene bg mila_on_top_of_paul_after_sex with flash
m "..."
m "Uf!"
m "..."
ms "I scratched Paul's back and pressed myself onto him."
ms "We came almost at the same time..."
ms "I did not understand this right away, but only a few seconds after I came myself."
ms "Paul's cock still pulsed a little and I gratefully squeezed my pussy to help him release the contents of his balls into me."
p "Haaaa ..."
ms "Paul's body finally relaxed."
scene bg mila_on_top_of_paul_after_sex_kiss
ms "I wrapped my arms around his head and kissed him passionately."
m "..."
p "..."
m "..."
p "..."
scene bg mila_on_top_of_paul_giggle
m "That was so damn cool ..."
p "..."
m "..."
p "You don't say..."
m "..."
p "..."
m "Paul..."
p "Yes?"
scene bg mila_on_top_of_paul_after_sex_kiss
m "..."
m "I love you."
scene bg mila_on_top_of_paul_giggle
ms "Paul hugged me tight"
p "..."
m "..."
p "..."
scene bg mila_on_top_of_paul_unsatisfied
m "So... {w}What should I... {w}I mean \"we\" do?"
p "..."
m "..."
p "..."
p "Let's... {w}Let's just not break his heart..."
scene bg mila_on_top_of_paul
m "..."
p "And then..."
p "Let's see what will happen."
m "..."
p "I think you will know what to do..."
p "Just do a right thing..."
p "I... {w}I trust your intentions."
scene bg mila_on_top_of_paul with fade
"{w}. {w}. {w}."




scene bg door
"..."
ms "The next day Bob knocked softly on the door."
show mila robe_shhhh_finger
ms "Greeting him with a smile, I handed him his lunch."
show bob surprised at left:
    xzoom 0.9 yzoom 0.9
ms "He looked at me in bewilderment."
m "Take it. {w}This is for you."
bob "..."
m "Take it already, my hand is about to fall off."
ms "Bob hesitantly accepted the bag of food."
show mila robe_puzzled_frown
m "So…"
bob "..."
show mila robe_puzzled
m "I thought about your words..."
show bob waving:
    xzoom 0.9 yzoom 0.9
bob "You did?"
ms "Bob made a fake laugh"
show bob smile:
    xzoom 0.9 yzoom 0.9
bob "Sorry, I shouldn't have said that..."
show mila robe_puzzled_frown
show bob sad2:
    xzoom 0.9 yzoom 0.9
bob "I mean... {w}I know your answer... {w}And I never wanted to make you... {w}uncomfortable..."
ms "Bob sighed"
show mila robe_sad
show bob sad:
    xzoom 0.9 yzoom 0.9
bob "I don't know why I said that..."
ms "He looked at me"
bob "You shouldn't be bothered with it... {w}I'm always like that..."
show mila robe_sad_tears
m "..."
m "His words made me sad, but somehow, I managed to pull myself together and smile."
show mila robe_smile_open_mouth
m "Don't worry, Bob. It's fine"
show bob idle:
    xzoom 0.9 yzoom 0.9
ms "He put on a fake smile"
bob "Sure. {w}If you say so..."
ms "I literally felt his desire to leave as soon as possible"
show mila robe_blush_shy_looking_aside
m "It's fine Bob, {w}because, {w}I will be your girlfriend"
bob "..."
m "..."
bob "..."
show mila robe_puzzled
m "..."
show bob smile:
    xzoom 0.9 yzoom 0.9
bob "Ahah! That's a funny joke!"
ms "His eyes told me that he wasn't finding it the least bit funny at all."
show mila robe_puzzled_frown
m "I'm not joking. {w}Well... {w}Maybe I am... {w}Kind of..."
show mila robe_smile_awkward_open_mouth
m "Anyway, {w}I mean, {w}I'll {b}pretend{/b} to be your girlfriend"
show bob sad2:
    xzoom 0.9 yzoom 0.9
bob "I don't like where this is going, so I should probably go"
ms "He frowned and turned to leave"
ms "I had to grab his sleeve to stop him"
show mila robe_worried_open_mouth_wait
m "Wait!"
bob "..."
show bob sad:
    xzoom 0.9 yzoom 0.9
ms "He looked at me with dull eyes"
ms "I didn't like that look"
ms "Judging. Uneasy. Even painful. For both of us"
ms "I sighed"
show mila robe_think
m "Bob. Listen to me."
ms "He didn't replied"
ms "But he didn't try to turn away from me neither"
m "..."
ms "Why is it so hard to gather my thoughts?"
m "..."
show mila robe_blush_shy_looking_aside
m "Do... {w}Do you like me, Bob?"
bob "..."
ms "Bob clenched his teeth and looked at me with pain in his eyes"
show bob frown_dull_eyes:
    xzoom 0.9 yzoom 0.9
bob "You... {w}know the answer"
show mila robe_smile_awkward_open_mouth
m "I don't want to hurt you, Bob"
m "I just..."
ms "I tried to find the right words... {w}But I failed..."
show mila robe_puzzled_frown
m "Just ask me out, Bob"
bob "..."
m "..."
show bob idle:
    xzoom 0.9 yzoom 0.9
ms "Bob sneered but put on a sad smile and nodded"
bob "Sure... {w}I will... {w}someday."
ms "No! {w}That's not what I meant, you silly"
show mila robe_curious
m "Ask me out."
show bob sad:
    xzoom 0.9 yzoom 0.9
ms "Bob frowned"
bob "Yeah, sure, {w}I will..."
show mila robe_smile_awkward_angry
m "Ask. {w}Me. {w}Out.{w}"
bob "..."
show bob sad2:
    xzoom 0.9 yzoom 0.9
ms "Bob sighed"
bob "But you are married..."
show mila robe_smile_awkward_open_mouth
m "Yes Bob, I am. That's why it's just a pretense"
bob "..."
show mila robe_smile_open_mouth
m "But it doesn't mean that it's pointless"
show mila robe_proud
m "Ask me out."
m "And see for yourself, that I won't turn you down"
bob "..."
show bob frown_dull_eyes:
    xzoom 0.9 yzoom 0.9
bob "This isn't right and I don't like it"
show mila robe_smile_awkward_angry
m "Do you? {w}You don't like to talk with me? {w}You don't want to go on a date with me?"
bob "..."
show mila robe_curious
m "Look. {w}You are nice guy. {w}And you are worth more then you think. {w}Much more"
m "And I'll prove it to you."
show mila robe_grin_thumbs_up
m "As long as you need - I will be your \"girlfriend\""
show mila robe_smile_grin
m "I'll cook for you, go on a dates with you, talk with you and stuff like that."
show mila robe_smile_open_mouth_excited
m "And I'll help you gain your self confidence"
bob "..."
show mila robe_proud
m "Ok?"
bob "Well..."
ms "Taking a closer look, I noticed that Bob was wearing a wrinkled t-shirt with a dirty collar that was turned inside out."
ms "I automatically tried to fix it, as I always do it for Paul, when he is in a hurry."
ms "Bob stood motionless."
bob "..."
scene bg door
show cg mila_and_bob_hands_on_sholders at center:
    xzoom 0.85 yzoom 0.85
    linear 1.0 ypos 0.85
ms "I looked at his face and, noticing his embarrassed look, looked away."
ms "He was so big... And he was so close... I felt so young and feminine"
ms "For a brief moment I remembered yesterday's fantasy..."
ms "And for a brief moment I wanted to make it real"
ms "I found my hands still lying on his wide shoulders and quickly step a bit back"
scene bg door
show bob shy:
    xzoom 0.9 yzoom 0.9
bob "..."
show mila robe_blush_shy_looking_aside
m "..."
ms "Woah..."
ms "What was that?"
show mila robe_puzzled
ms "Why is my heart beating so fast?"
ms "Somehow I managed to calm down, put on a brave smile and looked at him"
ms "I need to say something before it gets even more weird..."
show mila robe_smile_awkward_open_mouth
m "So?"
bob "..."
show bob surprised:
    xzoom 0.9 yzoom 0.9
bob "Ok... I guess..."
ms "I smiled at him and he smiled back"
show mila robe_blush_smirk
m "That's settled then"
show mila robe_holding_hand_open_mouth_blush
ms "I held out my empty hand"
m "Give me the key to your apartment, I'll clean it up and do your laundry."
m "I'm sure you haven't done that for a long time."
bob "..."
ms "Bob looked away and scratched the back of his head."
show bob doubting_scratching_head:
    xzoom 0.9 yzoom 0.9
bob "Erm..."
show mila robe_holding_hand_open_mouth_brow_up
m "What?"
bob "..."
m "..."
bob "..."
show mila robe_holding_hand_open_mouth_blush
m "Listen, you need to get used to the idea that someone wants to do something nice for you."
show mila robe_holding_hand_open_mouth_blush2
m "Just... {w}because."
bob "..."
m "..."
bob "I don't..."
ms "I felt like he would reject my proposal again, so I interrupted him right away."
show mila robe_holding_hand_open_mouth_frown
m "Just stop thinking that something bad might happen!"
m "I'm your girlfriend, remember?"
show mila robe_holding_hand_open_mouth_blush3_looking_aside
m "And I just want to... {w}{i}please{/i} you."
ms "..."
show mila robe_blush_smirk
ms "Wait... {w}That sounds kinda lewd..."
ms "..."
ms "Hehe"
bob "..."
show mila robe_holding_hand_open_mouth_blush2
ms "I patiently waited for his reaction"
ms "..."
show bob idle:
    xzoom 0.9 yzoom 0.9
ms "Bob still hesitated, but unfastened the key and put it in my hand."
show mila robe_smile_grin
ms "I smiled."
m "Get ready to be surprised - your apartment will be as clean as it has ever been!"
show bob smile:
    xzoom 0.9 yzoom 0.9
bob "Sure... {w}Hehe..."
bob "Erm…"
ms "Bob scratched his head again."
show bob shy:
    xzoom 0.9 yzoom 0.9
bob "Just don't clean my room... {w}Please"
bob "There... {w}I'll clean it myself..."
bob "..."
show mila robe_puzzled_frown
m "..."
show mila robe_bow_down
ms "After a short moment, I joined my palms and bowed down a bit"
m "As you wish..."
m "..."
m "...master"
show mila robe_blush_smirk
ms "Lewd!"
ms "Bob shyly smiled and left in a hurry"
show mila robe_smile_open_mouth_excited
ms "I waved at his back and closed the door"
"..."
show mila robe_smile_awkward_open_mouth
m "Well... {w}that went well, I think..."
"..."
show mila robe_curious
m "What's inside his room, I wonder?"
"{w}..."


scene bg apartments
ms "Having finished my chores before lunch, I finally went to clean Bob's flat"
ms "I expected it to be dirty, but it turned out to be not as bad as it could have been."
scene bg bobs_apartments_dirty
play sound "door-open-close.mp3"
ms "Rolling up my sleeves, I picked up the trash, gathered dirty clothes to wash later, and mopped the floors."
ms "Aparrently Bob doesn't have a washing machine..."
"..."
show mila casual_sad
ms "Wait a sec..."
ms "What is that?"
ms "Is it some kind of a suit?"
ms "Isn't it kind of small for Bob to wear?"
ms "Why does he need it?"
ms "I smelled it"
show mila casual_disgust_covered_nose
ms "Eugh... It stinks..."
ms "Needs washing then"
show mila casual_proud
ms "After a couple of hours the flat became much cleaner."
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
scene bg bobs_apartments_clean with flash
show mila casual_proud
"..."
ms "When the cleaning was finished, I couldn't resist and went to the door of bob's bedroom."
scene bg closed_door
show mila casual_skeptic at right:
    ypos 1.2
ms "..."
ms "He specifically asked me not to go inside..."
ms "Hmmm..."
show screen nts_stats_overlay
menu:
    "Should I open it anyway?"
    "It's easier to ask for forgiveness than asking for permission... (Mila's dominance + 1)":
        $ mila_dom += 1
        $ mila_was_in_the_room = True
        jump bob_door_opened
    "Some doors should stay closed...":

        jump bob_door_not_opened

label bob_door_opened:
show mila casual_worried
ms "I can't resist... I need to know"
hide screen nts_stats_overlay
play sound "creak.mp3"
scene bg bobs_room
ms "The door opened with a quiet creak"
ms "I knew there was no one in the room, {w}but for some reason I froze and looked around"
m "..."
show mila casual_relieved
m "Come on Mila..."
m "You aren't doing anything illegal..."
ms "I looked inside"
ms "The trash can next to the computer was filled with used napkins. {w}The stale air smelled faintly of sperm and sweat. {w}I covered my nose."
show mila casual_disgust_covered_nose
m "Ugh..."
ms "On the table was a switched off computer and a framed photo."
ms "I looked at it closer"
show cg selfie_in_a_frame at left:
    yzoom 0.7 xzoom 0.7
    linear 0.6 ypos 0.8
show mila casual_worried
m "He printed that selfie, hah..."
m "..."
m "..."
show mila casual_sad
ms "Somehow it was depressing..."
ms "I couldn't stand it and turned away"
play sound "creak.mp3"
scene bg closed_door
ms "..."
ms "..."
m "I guess I really shouldn't have opened the door..."
m "..."
show mila casual_interested_blush
m "But..."
m "He masturbates a lot..."
m "..."
m "What is he dreaming about, I wonder?"
m "..."
m "..."
m "Anyway... I'm done. {w}I should go home now."
jump maid1_continue

label bob_door_not_opened:
show mila casual_proud
m "No... {w}I shouldn't go there. He asked me not to..."
m "..."
hide screen nts_stats_overlay
show mila casual_worried
ms "But... {w}This restriction put me in a mood..."
ms "For a little mischief. .."
show mila casual_thinking
m "Hmmm..."
ms "What should I do?"
show mila casual_interested_blush
ms "Maybe tease him a little?"
ms "I stood in the middle of the tidy apartment and took a selfie."
play sound "shot.mp3"
"..."
show cg maid1_selfie_casual:
    yzoom 0.9 xzoom 0.9
m "Hmmm…"
ms "Something is missing…"
ms "I took off my bra and adjusted my T-shirt."
play sound "shot.mp3"
"..."
show cg maid1_selfie_casual_pokies_v_grin_blush:
    yzoom 0.9 xzoom 0.9
ms "Hehe."
ms "That's better."
ma "{image=bob/One use/cg maid1_selfie_casual_pokies_v_grin_blushx.webp}"
ms "I sent the photo to Bob and waited impatiently for his response."
show mila casual_hand_in_pants_heavy_breathing
ms "When I noticed that he had read my message, I couldn't resist and put my hands in my panties."
ms "My pussy was oozing juices"
m "Come on dear boyfriend..."
m "Say something..."
show mila casual_hand_in_pants_biting_lips
m "..."
bob_message "Thank you"
ms "..."
show mila casual_laugh
ms "Hehe."
ms "How dry."
m "..."
show mila casual_smile
ms "His answer kind of ruined the mood. I felt more joyful than horny"
ms "So I giggled and thought that it would be funny to tease him more"
ma "Have you changed your mind about your room? I can clean it too, you know?"
ms "The answer came almost instantly"
bob_message "No!"
show mila casual_laugh
ms "Ahah."
ma "Fine."
"..."
show mila casual_thinking
ms "Still, what's inside his room?"
ms "I looked at the closed door one last time and left Bob's apartment"
"..."




label maid1_continue:
scene bg apartments
"{w}..."
ms "The next day, Bob sheepishly thanked me for his lunch and cleaning."
ms "But with each passing day he became gloomier and gloomier."
ms "A week later he didn't come at all."
ms "I knocked on his door, but no one opened it."
scene bg bobs_apartments_clean
play sound "door-open-close.mp3"
ms "When I opened the door with the key, it turned out that he had already left."
show mila robe_puzzled_frown
m "..."
m "What the?.."
ms "I still kept my part of the deal - moped the floors and tidied the room."
show mila robe_puzzled
ms "Couple of times I took my phone and tried to text Bob a message"
ms "But couldn't chose the right words"
"..."
show mila robe_think
m "Haaa..."
ms "With a heavy soul I returned home"
scene bg apartments
play sound "door-open-close.mp3"
ms "In the evening, when I heard that Bob had returned home, I came to him."
scene bg doors
show mila robe_puzzled_frown
m "..."
show bob sad2:
    xzoom 0.9 yzoom 0.9
ms "Bob opened the door but didn't even look at me."
ms "..."
show mila robe_smile_awkward_open_mouth
m "..."
m "Bob?"
show bob sad:
    xzoom 0.9 yzoom 0.9
bob "..."
bob "Good evening…"
m "..."
show mila robe_worried_open_mouth_wait
m "Yeah, hi. What happened?"
show bob doubting_scratching_head:
    xzoom 0.9 yzoom 0.9
bob "..."
bob "..."
ms "Bob didn't answer."
ms "..."
show mila robe_sad
m "Bob? Did I hurt you somehow?"
bob "..."
ms "Bob shook his head and sighed."
show bob sad:
    xzoom 0.9 yzoom 0.9
bob "No... {w}I..."
bob "Well...{w} First of all, {w}thank you..."
show mila robe_sad_tears
ms "I nodded. Although he did not look at me and hardly notice the clean flat."
ms "For some reason I felt bad... {w} A disgusting bitter feeling of loss scratched me inside"
ms "I swallowed, trying to get rid of it"
ms "It didn't help"
show bob frown_dull_eyes:
    xzoom 0.9 yzoom 0.9
bob "..."
bob "I think it's time to stop..."
m "..."
m "..."
show mila robe_sad_tears_open_mouth
m "Why?"
show mila robe_sad_tears
ms "My voice cracked"
ms "Bob quickly looked at me but immediately turn away"
bob "..."
show bob sad:
    xzoom 0.9 yzoom 0.9
bob "This...{w} it's not real..."
bob "But...{w} it's exhausting..."
bob "..."
bob "And...{w} the longer it lasts..."
bob "The more painful it becomes..."
show mila robe_sad_tears_open_mouth
m "..."
m "Bob…"
show mila robe_sad_tears
show bob frown_dull_eyes:
    xzoom 0.9 yzoom 0.9
bob "..."
ms "He looked at me blankly..."
ms "I took his hand."
show mila robe_sad_tears_open_mouth
m "And what is real then?"
bob "..."
show mila robe_puzzled_frown
m "Can you feel my touch?"
ms "He didn't react."
ms "Something inside me cracked"
ms "I couldn't watch him suffer anymore"
ms "Following a sudden impulse I stood up on tiptoes, grab his neck and pressed my lips to his"
scene cg mila_kiss_bob with flash
ms "I felt the salty taste of my tears and a slight taste of tobacco"
ms "His lips were so soft and big..."
ms "He stood there, frozen, and I wasn't sure is he liked it or not..."
ms "After a couple of very long seconds I pulled away"
scene bg doors
show mila robe_blush_shy_looking_aside
show bob surprised:
    xzoom 0.9 yzoom 0.9
bob "..."
m "..."
bob "..."
m "..."
show mila robe_sad_tears_open_mouth
m "How about that?"
bob "..."
ms "Life appeared in his eyes again."
ms "He looked at me in surprise."
bob "..."
show mila robe_blush_shy_looking_aside
m "Is this not real either?"
bob "..."
show bob sad2:
    xzoom 0.9 yzoom 0.9
bob "I... {w}I don't know what to think... {w}And I didn't know how to answer."
ms "I stepped closer and looked into his eyes"
ms "He looked like a frightened deer"
show mila robe_smile_awkward_angry
ms "He still didn't believe me"
ms "He still wants to run away"
ms "..."
show mila robe_proud
ms "But I won't let you do that"
ms "I smiled and wiped my tears"
show mila robe_blush_smirk
m "I like you, Bob"
show bob surprised:
    xzoom 0.9 yzoom 0.9
bob "..."
show mila robe_smile_open_mouth
m "If I weren't married, you would have a great chance with me."
bob "..."
show mila robe_shhhh_finger
m "If only you could become more confident..."
m "Then you would most likely find yourself a worthy woman."
bob "..."
show bob sad:
    xzoom 0.9 yzoom 0.9
show mila robe_puzzled_frown
ms "Bob looked at me with pain."
bob "I... {w}I don't want anyone else anymore."
m "..."
bob "..."
show mila robe_smile_awkward_angry
ms "And how should I answer to that?"
ms "..."
ms "Fuck..."
ms "Fuck fuck fuck"
show mila robe_think
ms "Think, Mila... {w}Think"
m "..."
ms "The pause dragged along"
ms "Bob sighed and smiled sadly"
show bob frown_dull_eyes:
    xzoom 0.9 yzoom 0.9
bob "Can you {w}leave me alone?"
ms "I flinched"
show mila robe_puzzled_frown
bob "I…"
bob "I'm afraid that I will say something... {w}That I will regret saying later."
bob "..."
m "..."
show mila robe_curious
m "Haaa..."
ms "Suddenly I felt so tired of everything."
ms "The emotional distress can be exhausting too"
show mila robe_irritated_open_mouth
m "You know what?"
m "Fine. {w}I'll leave."
show bob sad:
    xzoom 0.9 yzoom 0.9
bob "..."
ms "Bob chuckled"
ms "I ignored his reaction"
m "But tomorrow you will pick me up after work"
m "And we will go on a date"
show bob surprised:
    xzoom 0.9 yzoom 0.9
bob "But..."
show mila robe_iritated_atatata
m "Atatata"
m "No buts."
show mila robe_irritated_open_mouth
m "I heard you. {w}I hurt you, {w}blah blah blah"
m "But. {w}You are also hurting me. {w}Like right now"
m "Why should I endure it?{w} I can run away too.{w} Pretend that I don't know you.{w} That I don't care."
m "But I won't."
m "Because I do care.{w} I do know you.{w} And I do like you."
m "Instead, {w}you know what I will do? {w}I'll deal with it"
m "There is no way to commit yourself to relationship and feel no pain at all"
m "You will hurt me.{w} I will hurt you.{w} But pain is not the only thing we may experience."
m "I'm not afraid of getting hurt. {w}It's better than feeling nothing at all, isn't it?"
show bob frown_dull_eyes:
    xzoom 0.9 yzoom 0.9
bob "..."
m "So get your shit together, and treat me to a nice meal.{w} Or something.{w} I don't care, actually; let's just have fun."
bob "..."
m "Ok?"
ms "Bob didn't answer. He stood there and looked at me like I was a ghost"
m "Ok. Tomorrow. Evening. Bye."
scene bg door
play sound "door-open-close.mp3"
show mila robe_sad_tears
ms "I closed the door, and only then did I feel that I had no power to stand and hold back my tears."
ms "Arguments have never been my strong suit, after all..."




scene bg apartments
hide mila
show cg mila_hugging_knees at center:
    xzoom 0.9 yzoom 0.9 ypos 0.9
ms "I did not have time to recover before Paul returned home."
ms "He found me sitting on the bed, hugging my knees."
p "..."
p "Sweetheart? What happened? Are you hurt?"
ms "I couldn't properly answer, and just burst into tears."
ms "Paul hugged me and gave me some time to gather my thoughts."

show cg mila_paul_hug at center:
    ypos 1.8
    linear 5.0 ypos 1.1
ms "His presence always has a calming effect on me."
ms "A few minutes later I was able to finally pull away and tell him what happened."
hide cg
show paul suit_open_mouth_neutral at left
m "..."
p "Do you feel better?"
show mila robe_blush_shy_looking_aside at right
ms "I nodded"
p "..."
m "..."
show paul suit_sad
p "..."
p "Can I be completely honest with you?"
show mila robe_puzzled_frown
ms "..."
ms "For some reason, his tone seemed to me frightening. I nodded diligently, trying not to imagine things."
m "Sure..."
p "..."
show paul suit_frown
p "I am very worried about Bob...{w} But as soon as you said you kissed him, I can't think about anything else..."
m "..."
m "..."
show mila robe_sad
ms "My palms instantly became sweaty."
ms "I swallowed nervously."
show mila robe_curious
m "You...{w} do you want to stop all this?"
p "..."
show mila robe_sad
ms "Paul was silent, immersed in his thoughts."
m "..."
ms "In a conversation with Bob, I succumbed to emotions."
ms "But now different thoughts swarmed my head."
ms "I regretted that I did it and tried to justified myself."
ms "I was angry at Paul and, at the same time, was struggling with a desire to start praying for forgiveness."
ms "I was sure of only one."
show mila robe_sad_tears
ms "I don't want my relationship with Paul to break."
ms "I realized that I could think about Bob and indulge myself only if everything was fine at home."
ms "If Paul is happy..."
m "..."
show mila robe_sad_tears_open_mouth
m "Paul?"
show mila robe_sad_tears
show paul suit_open_mouth_neutral
p "Ah? Sorry, what did you say?"
m "..."
show mila robe_sad_tears_open_mouth
m "I asked if you want to... Stop all of this?"
show mila robe_sad_tears
p "..."
show paul suit_shock
ms "Paul looked at me in surprise."
p "No, why do you ask?"
m "..."
show mila robe_sad_tears_open_mouth
m "I thought you were angry at me..."
show mila robe_sad_tears
p "..."
p "Oh..."
show paul suit_grin
p "Ahah.{w} No. Everything is fine!"
show paul suit_open_mouth_blush
p "I just...{w} I tried to imagine that kiss of yours..."
show paul suit_blush_looking_aside
show mila robe_smile_awkward_open_mouth:
    easein 1 xpos 0.8
m "..."
m "Oh...{w}Uhm...{w} And what do you think?"
p "..."
show paul suit_open_mouth_blush
p "That it had to be damn sexy..."
show paul suit_blush_looking_aside
ms "All my worries disappeared as if by the wave of a magic wand."
show mila robe_smile_grin
ms "I smiled."
m "You think?"
show paul suit_grin
p "Yeah...{w} but what's for sure - I am offended that I did not see it."
show mila robe_blush_smirk:
    easein 1 xpos 0.6
m "Heh...{w} Do you want me to take a photo next time?"
p "..."
show paul suit_sad
ms "Paul looked at me with a piercing look."
show mila robe_blush_shy_looking_aside
ms "I cringed, but did not look away."
p "..."
show paul suit_grin
p "Next time, huh?"
show mila robe_blush_smirk
m "..."
show paul suit_open_mouth_blush
p "Yes. I do want it"
show paul suit_blush_looking_aside
m "..."
p "..."
show mila robe_puzzled
m "Paul..."
show paul suit_open_mouth_neutral
p "?"
m "..."
show mila robe_puzzled_frown
m "You do not mind that we are going on a date?"
show paul suit_blush_looking_aside
p "..."
show paul suit_open_mouth_blush
p "I guess...{w} I still find it sexy."
show mila robe_shhhh_finger
p "I do not know why."
p "And I am pretty sure, that I don't want to know the reason."
show paul suit_blush_looking_aside
m "..."
p "..."
show paul suit_sad
p "Just...{w} Don't betray my trust..."
show mila robe_worried_open_mouth_wait
m "I would never!"
p "I know.{w} And still. Just...{w} don't."
show mila robe_puzzled_frown
m "..."
hide paul
show mila robe_puzzled_frown at center
ms "I looked at him and his gaze made me shiver."
ms "This tread of trust between us keeps stretching under the pressure of our actions."
ms "And we kept pulling it in attempts to tear it apart."
ms "But we always stop at the last moment. Which just made the tread stronger."
ms "I don't want to make Paul suffer."
ms "I want the proof.{w} The power.{w} I want his feelings.{w} All of them."
ms "I want to submit to him.{w} To show him, that whatever happens with us...{w} Whatever we do ourselves...{w} My heart is his property."
ms "And there is nothing,{w} literally nothing,{w} that could tear us apart."
m "..."
show mila robe_smile_awkward_open_mouth
m "Do you want to give any instructions?"
show screen nts_stats_overlay
menu:
    "What should Paul suggest?"
    "Let him touch your ass (Mila's submissiveness + 1)":
        $ dom += 1
        $ paul_touch_ass = True
        jump netorase1_choice1
    "Do what you think is right (Mila's dominance + 1)":
        $ mila_dom += 1
        jump netorase1_choice2

label netorase1_choice1:
show mila robe_blush_shy_looking_aside
ms "Blood rushed to my cheeks, and I felt my face become red."
m "..."
hide screen nts_stats_overlay
show mila robe_puzzled
m "You sure?"
show paul suit_open_mouth_neutral at left
p "Yep."
show paul suit_grin
ms "Paul smiled at me. He answered without hesitation."
m "..."
show mila robe_puzzled_frown
m "But you won't be able to watch..."
p "..."
p "That's why I want to hear all the juicy details afterwards."
m "..."
show mila robe_blush_smirk
m "..."
m "Fine. I'll see what I can do."
p "..."
show paul suit_smirk
ms "Paul smiled somehow cheekily."
p "That's my girl."
p "..."
ms "I won't lie. I liked his reaction."
"..."
jump netorase1_continue

label netorase1_choice2:
show paul suit_blush_looking_aside at left
show mila robe_puzzled_frown
ms "Paul kept silent.{w} So I thought it would be right to suggest something."
hide screen nts_stats_overlay
show mila robe_blush_smirk
m "..."
m "Nothing? I think I'll just suck him off then..."
show paul suit_extremely_shocked
p "!!!"
ms "Paul looked at me in disbelief."
show mila robe_shhhh_finger:
    easein 1 xpos 0.4
m "You don't like the idea?"
p "..."
show paul suit_blush_looking_aside
ms "Paul understood, that I was joking and became embarassed by his reaction."
ms "I couldn't help it.{w} I wanted to tease him more."
show mila robe_blush_smirk:
    easein 1 xpos 0.3
m "You seemed to like it before? What happened?"
p "..."
ms "Paul didn't answer."
show mila robe_shhhh_finger
m "Hehe.{w} Then...{w} maybe I should touch him?"
p "..."
ms "Paul smiled at me cautiously."
ms "I smiled back at him."
m "..."
show mila robe_proud
m "So? What do you think?"
p "..."
show paul suit_open_mouth_blush
p "I think you can rub it... {w}Through his clothes..."
show paul suit_blush_looking_aside
ms "I rubbed Paul's bulge."
show mila robe_blush_smirk
m "Like this?"
p "..."
show paul suit_open_mouth_blush
p "Yeah..."
show paul suit_blush_looking_aside
show mila robe_smile_grin
m "Hehe..."
m "Well..."
m "I see what I can do..."
p "..."

label netorase1_continue:
"{w}..."
scene bg bedroom
ms "I was afraid that I would not fall asleep because of my thoughts."
ms "But it turned out that I was so exhausted that I fell asleep almost immediately as soon as my head touched the pillow."





n "{w}. {w}. {w}."
scene bg apartments
ms "The day passed in excitement."
ms "I tried to get distracted by cleaning and cooking, but my thoughts about the upcoming date did not go away."
show mila robe_think
m "..."
m "I was just like a schoolgirl before her first date, what's the big deal?"
m "..."
show mila robe_smile_awkward_open_mouth
ms "When the time approached six, I began to prepare."
ms "At first I wanted to dress up... But in the end I decided to not to overdo it."
show mila robe_untied
ms "I did not want to make Bob even more nervous."
n "..."
show mila jeans_and_blouse_front
n "..."
ms "Bob came almost immediately after work."
ms "Although I heard him stomping at the door gathering strength. I decided not to rush him."
ms "Finally he knocked."
show mila jeans_and_blouse_waving at right
m "..."
show bob idle at left:
    xzoom 0.8 yzoom 0.8
bob "..."
show mila jeans_and_blouse_remorse
m "..."
m "Bob..."
bob "Hello..."
show mila jeans_and_blouse_angry_open
m "Yeah, Hi...{w} what is that you are wearing?"
show mila jeans_and_blouse_angry_close
show bob doubting_scratching_head
bob "..."
bob "..."
bob "My ordinary clothes!"
m "..."
show mila jeans_and_blouse_angry_open
m "Right."
show mila jeans_and_blouse_angry_close
show bob frown_dull_eyes
bob "..."
bob "I should have come in work clothes?"
show mila jeans_and_blouse_remorse
m "..."
m "Haaaa ..."
m "Let's go."
play sound "door-open-close.mp3"
scene bg doors
show bob doubting_scratching_head at left:
    xzoom 0.8 yzoom 0.8
bob "..."
bob "Oh, ok ..."
show bob idle
ms "Bob stepped back and followed me from behind."
show mila jeans_and_blouse_back
ms "At first, I wanted to pester him because he did not praise my looks and went on a date in his usual rags..."
ms "But then I remembered that this was his first date. I shouldn't expect too much from him."
m "Bob..."
show bob frown_dull_eyes
bob "Yes?"
m "..."
m "If you like the view from behind more, then I do not mind."
show bob surprised
bob "!"
m "But in general, the couple usually walks close on a date."
show bob frown_dull_eyes
bob "S-sorry ..."
m "Bob caught up with me in two steps and tried to keep the pace of our walking."
show mila jeans_and_blouse_run_smile
m "..."
n "{w}. {w}. {w}."
scene mall
ms "As we entered the mall, Bob began to lag behind again."
ms "I had to grab his arm to not lose sight of him."
show mila jeans_and_blouse_serious_open_mouth at center
m "..."
m "Why are you so afraid?"
show bob sad at left:
    xzoom 0.8 yzoom 0.8
ms "Bob frowned."
bob "I'm not afraid ... {w}It's just... {w}people find me unpleasant."
bob "Therefore, I try not to come across anyone ..."
show mila jeans_and_blouse_sad_looking_aside
ms "I did not know how to answer."
show bob frown_dull_eyes
bob "You have never experienced the unpleasant look of disgust."
bob "Therefore, I am not hiding myself for their pleasure... {w}I do it for myself."
bob "I do not look at them and keep a low profile, to avoid drawing attention."
bob "And in order not to feel worse than I already do..."
show mila jeans_and_blouse_sad_looking_up
m "..."
m "Sorry..."
show bob sad
ms "Bob smiled sadly."
bob "It's ok..."
m "..."
show mila jeans_and_blouse_sad_looking_down
m "What about me?"
show bob surprised
ms "Bob looked at me in surprise."
show mila jeans_and_blouse_sad_looking_up
m "Do I also look at you with disgust?"
bob "..."
show bob sad
bob "No..."
show mila jeans_and_blouse_serious_open_mouth
m "Then don't look at them.{w} Look at me."
bob "..."
show mila jeans_and_blouse_front
m "..."
bob "..."
show bob idle
ms "Bob smiled."
bob "Ok."
ms "I squeezed his hand slightly and smiled."
m "Good."
show mila jeans_and_blouse_waving
m "Now we will go to the store and look at some clothes for you..."
"..."
scene changing room
ms "Bob grumbled while I was picking clothes for him."
ms "After some time I answered him, but after a while I began to just ignore it."
ms "Bob frowned, but stopped grumbling."
"..."
"???" "Do you need help to make a choice?"
ms "A consultant girl approached me."
ms "I wanted to refuse at first, but then I realized that I had wandered around the store for half an hour and couldn't find what I wanted."
show mila jeans_and_blouse_run_smile
m "Yes, I think so. {w}Bob, come here, please."
show bob frown_dull_eyes at left:
    xzoom 0.8 yzoom 0.8
bob "..."
bob "Bob obediently came closer and stood next to me, trying not to meet the gaze of the saleswoman."
ms "The girl looked at him with a quick look and put on a polite smile, but I clearly felt what Bob spoke of."
ms "She radiated hostility, and I could literally feel it, even when she was hiding it behind a smile."
show mila jeans_and_blouse_remorse
m "..."
m "I wonder what he did to her? Bob was surrounded by some aura that forced others to despise him."
bob "..."
"???" "Are you trying to choose an outfit for your ... father? What's the occasion?"
show mila jeans_and_blouse_angry_close
ms "Her reaction for some reason knocked me out of the rut and angered me."
show mila jeans_and_blouse_angry_open
m "He is my boyfriend."
show mila jeans_and_blouse_angry_close
ms "For a moment, the seller's disgust leaked to her face. And this time it was turned to me."
ms "I met her gaze, ready to arrange a scandal if she behaves inappropriately."
m "..."
ms "But apparently she felt my determination and lowered her eyes."
"???" "I apologize, I did not mean to upset you."
m "..."
show mila jeans_and_blouse_proud
ms "I gazed at Bob and read gratitude in his eyes."
ms "Heh."
show mila jeans_and_blouse_smile_wink
ms "There we go."
"..."
"..."



ms "We spent more than an hour trying on different outfits. {w}Judging by Bob's face, he regretted agreeing to go with me on a date about 10 minutes later."
ms "But in the end, it was worth it."
show mila jeans_and_blouse_run_smile at center
"..."
"..."
show bob suit_sceptic at left:
    xzoom 0.8 yzoom 0.8
m "It seems to me this is our option."
show bob suit_happy
ms "Bob shone."
bob "It's done? Can we go now?"
show mila jeans_and_blouse_serious_open_mouth
ms "I rolled my eyes."
ms "It's good that Paul himself was engaged in his wardrobe ..."
"..."
scene mall
ms "We paid for the clothes and left the store."
ms "Bob, judging by his face, was dissatisfied with our pastime"
show mila jeans_and_blouse_run_smile
m "Well, what's next?"
show bob suit_sceptic at left:
    xzoom 0.8 yzoom 0.8
bob "..."
bob "Call it a day?"
show mila jeans_and_blouse_surprise
m "..."
m "Nope."
show bob suit_awkward_smile
ms "Bob sighed, but noticing my displeased gaze put on a smile."
show mila jeans_and_blouse_haaaa_tired_irritated
m "..."
m "Haaaa ..."
show mila jeans_and_blouse_angry_open
m "Bob, are you dissatisfied with something?"
show bob suit_sceptic
bob "..."
ms "Bob said nothing."
m "You are on a date with a girl who is twenty years younger than you."
m "I helped you to chose a suit and cooked for you"
show mila jeans_and_blouse_angry_disgust_open
m "I could relax at home or do something else now, but no - I spend my personal time with you."
m "So I am interested: are you dissatisfied with something?"
show mila jeans_and_blouse_angry_close
ms "Bob muttered at once."
show bob suit_frown_open_mouth
bob "I did not force you to come with me."
ms "The tone of his voice was more mean than resentful."
bob "I don't need your pity. {w}It was you in the first place who initiated all of this... {w}Farce."
show bob suit_sceptic
show mila jeans_and_blouse_remorse
m "..."
ms "I almost snapped at him, but restrained myself."
ms "I wanted to have fun, not a fight."
show mila jeans_and_blouse_surprise
m "..."
ms "But now it's clear why he does not have a girlfriend."
m "..."
ms "We must somehow help him to behave."
show mila jeans_and_blouse_serious_open_mouth
m "Farce, you say..."
ms "Feeling my irritation, Bob shrunk back and said nothing."
show mila jeans_and_blouse_angry_open
m "I see that you are dissatisfied. {w}You do not like that I helped you with clothes, {w}you did not like that I am cooking for you,{w} you did not like that I agreed to become your girlfriend."
m "How many layers of your armor will I need to overcome in order to finally get to the Bob, that is satisfied with at least one thing?"
m "All I get from you are your pouts and frowns."
show mila jeans_and_blouse_angry_close
show bob suit_frown_open_mouth
bob "..."
ms "Bob opened his mouth to say something, but after a second he closed it and turned away."
show bob suit_sceptic
show mila jeans_and_blouse_front
ms "I came a little closer and forced him to look at me."
show mila jeans_and_blouse_serious_open_mouth
m "What do you want?"
show mila jeans_and_blouse_surprise
bob "..."
show mila jeans_and_blouse_serious_open_mouth
m "Do you want to return home? {w}And forget it as soon as possible, a bad date where an annoying girl made you try on clothes?"
m "Do you want that?"
show mila jeans_and_blouse_surprise
show bob suit_frown
bob "..."
ms "Bob frowned, but continued to be silent."
show mila jeans_and_blouse_serious_open_mouth
m "I don't know how to read thoughts Bob. {w}What do you want?"
show mila jeans_and_blouse_surprise
bob "..."
ms "His eyes ran from side to side, like a teenager, caught in the theft of cookies."
ms "I took a step back to give him a little space."
bob "..."
show mila jeans_and_blouse_serious_open_mouth
m "I dragged you to the clothing store because it seemed to me that you didn't give a fuck about the date. {w}About me too."
m "Fortunately, I didn't dress up too much for the occasion."
m "Imagine how stupid would I look if i did?"
show mila jeans_and_blouse_remorse
bob "..."
show bob suit_frown_open_mouth
bob "We look stupid together anyway."
show mila jeans_and_blouse_frown
m "..."
show mila jeans_and_blouse_frown_open_mouth
m "Do you really think so?"
show bob suit_frown at left:
    xzoom 0.8 yzoom 0.8
ms "Bob looked away."
m "Bob?"
bob "..."
scene bg mila_incoming_hug
ms "I took him by the chin and made him look at me."
m "Do you really think so or are you just afraid to argue with others?"
bob "..."
scene bg mila_incoming_hug_looking_aside
m "Look."
ms "I turned to the mirrored surface of one of the windows."
scene bg mila_and_bob_mirror
m "Do we look stupid?"
bob "..."
scene bg mila_and_bob_mirror_hand_on_hip
m "We look hot together, if you ask me. {w}Like a girl with her Sugardaddy."
ms "Bob didn't answer, but his face cleared, and I even noticed a sort of smile."
ms "I slightly pushed him with my hip."
scene bg mila_and_bob_mirror_hand_on_hip_smile
m "Stop worrying about the opinion of others."
m "It's impossible for us to be liked by every single person."
m "They don't like you. {w}Well, fuck them. {w}If they don't want to look at you. {w}Well, let them turn away."
m "If you raise your head, you can see that not everyone is hating you."
m "There are some, who like you."
scene bg mila_and_bob_mirror_hand_on_hip_embarassed_pointing_at_self
m "Like {b}me{/b}, for example..."
bob "..."
m "..."
scene bg mila_and_bob_mirror_hand_on_hip_smile_shy
m "And now I want a drink."
m "It's getting hot in here..."
bob "..."
m "Are we going? Or do you want to run home?"
bob "..."
ms "Bob thought a few moments, but then finally smiled and nodded."
ms "I took him under the elbow."
scene mall
show mila jeans_and_blouse_run_smile
m "I will not force you to choose a place the first time."
m "I know one place where you can eat and dance deliciously."
m "But next time it's your turn to choose a place."
ms "Bob didn't answer."
show mila jeans_and_blouse_proud_smile
m "Well, that's settled then."
n "{w}. {w}. {w}."
scene bg restaurant

if paul_took_initiative:
    ms "I've been already to this restaurant with Paul."
    ms "And I wanted to rewrite our negative experience with something pleasant."
    jump continue_bob_restaurant
ms "We went to the nearby restaurant. Inside, it smelled pleasant and fresh, and warm, soft light flashed imposingly in space."
ms "A spot for dancing was in the center of the hall, which was currently empty."
label continue_bob_restaurant:
ms "The waiter led us to our table, took our orders and left."
ms "We chatted about work and drank a little wine."
scene bg mila_table_blouse_playful
ms "Warmth spilled over my body, I felt tipsy."
ms "The wine made us relax."
ms "I wanted to return to the playful mood and change the subject to something interesting and less depressing. {w}I had reached a point where I was tired of feeling like a girlfriend who only whines."
m "..."
m "Let's play a game."
ms "Wine spurred my playful nature. I wanted to talk on more frank topics."
ms "Bob frowned."
bob "Game?"
scene bg mila_table_blouse_seductive_gaze
m "Yeah. You ask a question, or make a statement about me, and if you are right - I'll drink."
bob "And if not?"
m "Then next is my turn to ask. And then your again."
bob "..."
m "Are we playing?"
ms "Bob did not want to agree, but either the wine played a role, or he himself was tired of his constant refusals."
bob "Fine."
scene bg mila_table_blouse_grin
m "Hah. I will begin."
scene bg mila_table_blouse_think
m "The last time you went on a date was at least five years ago."
scene bg mila_table_blouse_playful
ms "Bob took a moment to think."
bob "No. About two years ago, I met a woman. We went to the cinema. Once."
scene bg mila_table_blouse_surprise
ms "I could not restrain myself and raised my eyebrows in surprise."
m "Really? And what happened next?"
bob "Now it's not your turn to ask a question."
ms "Bob grinned."
scene bg mila_table_blouse_grin
m "That's true."
scene bg mila_table_blouse_playful
bob "..."
bob "You feel sorry for me and that's why you are doing all of this."
scene bg mila_table_blouse_think
ms "I thought for a moment, but then I shook my head."
m "\"Sorry\" not quite a suitable word. I like you and therefore I... worry about you. This is closer to the truth."
scene bg mila_table_blouse_seductive_gaze
m "There is another reason, but we are both not ready for it."
ms "All three of us are not ready for it, that would be more accurate."
bob "..."
bob "We both failed... This game is boring..."
scene bg mila_table_blouse_grin
m "Ahah."
m "Are you saying that we should raise the stakes? You are right!"
bob "That is not what I..."
ms "Bob tried to say something, but I didn't want to listen."
scene bg mila_table_blouse_seductive_gaze
m "You would like to kiss me now."
ms "Bob stopped speaking and stared at me."
ms "Then he slowly lifted the glass and took a sip."
scene bg mila_table_blouse_grin
ms "I smiled."
scene bg mila_table_blouse_think
m "Hmmm ... you think that you are doing something wrong by going on a date with a married woman."
ms "Bob took another sip."
scene bg mila_table_blouse_playful
m "It's not easy for me, too, to be honest.{w} I'm not sure what you think,{w}, but this is the first time I am on a date with someone other than Paul.."
bob "..."
ms "Bob looked confused."
ms "Good. Life is not as easy as you think. I bet you don't understand what I want and what I feel."
ms "But you will, eventually."
scene bg mila_table_blouse_think
m "Hmmm ... let's add some spice."
ms "Bob looked at me warily."
scene bg mila_table_blouse_playful
m "You masturbate imagining sex with me."
bob "!!!"
ms "Bob looked at me in a shock."
m "..."
scene bg mila_table_blouse_seductive_gaze
ms "I kept silent, and waited for his answer."
bob "..."
m "Well? Am I wrong?"
bob "..."
bob "..."
ms "Bob turned away and brought the glass to his lips."
scene bg mila_table_blouse_blush_naughty_whispering
ms "I could not resist, leaned forward slightly to be closer to him and whispered:"
m "Me too."
bob "!"
scene bg mila_table_blouse_playful
m "That's why, I will also take a sip."
bob "..."
"{w}..."
ms "At some moment, I don't know how it happened, there was no wine in the bottle."
ms "And suddenly, my thoughts began to swirl around in my head with great speed, and I couldn't catch them anymore."
ms "This is the moment. {w}The moment, when we should stop talking and take action."
scene bg mila_table_blouse_playful_drunk
m "We should dance! Can we dance?"
ms "Bob shook his head."
bob "No, thanks."
scene bg mila_table_blouse_pout_drunk
m "..."
bob "Is it my turn to ask a question?"
m "It was a request, not a question, Bob."
bob "Ah ... sorry ..."
scene bg mila_table_blouse_playful_drunk
m "Come oooon. {w}If you dance with me, I will fulfill one of your wishes."
bob "..."
scene bg restaurant
show mila jeans_and_blouse_drunk_hand_open at center
ms "I got up and held out my hand."
m "Come!"
ms "Hehe... Sounds lewd!"
ms "Bob resisted me a bit more, but when he understood I wouldn't back down, he stood up."
bob "I don't know how to dance."
scene bg mila_and_bob_dance
ms "I smiled and laid his hands on my waist."
m "There is nothing complicated. Just listen to the music."
ms "According to his trembling hands, it was clear he was worried."
ms "But the wine and the whole situation were so heady that his uncertainty only heightened my appetite."
if paul_touch_ass == False:
    jump mila_took_iniative

ms "I took a step forward and pressed my body to his."
ms "His hands remained hanging in the air."
ms "I took his wrists and met his eyes."
ms "He did not resist."
show cg mila_and_bob_dance_hands_on_ass at truecenter with dissolve
ms "I slowly lowered his hands to my back, and then pulled them down until his palms were on my ass."
ms "With my stomach, I felt as his cock became hard."
ms "I smiled, let go of his wrists and hugged his neck."
bob "..."
ms "We almost froze in this position."
ms "I slowly moved my hips to the music's rhythm, rubbing my entire body against his."
ms "Bob wanted to remove his hands, but I managed to intercept his wrist and pressed them to my ass."
m "..."
ms "If Paul didn't request that... {w}I am unsure which of us was more embarrassed in this situation - I or Bob. ..."
ms "But we continued to move slowly, {w}afraid to turn away from each other, {w}afraid to break the invisible balance and look at ourselves from the side."
jump continue_dance_bob

label mila_took_iniative:

ms "I thought that it would be easier for Bob if he couldn't see my eyes."
ms "So I turned my back to him and took a step back."
show cg mila_and_bob_dance_from_behind at center:
    ypos 1.8
    linear 5.0 ypos 1.1
ms "I felt with my back and booty his hardened penis."
ms "Recently, this one fact could turn me red."
ms "But now..."
ms "Now I wanted to snuggle up to him more and feel every millimeter of his cock."
ms "I turned around and our eyes met."
ms "He was embarassed, and I smiled at him."
ms "And his embarrassment woke up an even more slutty part of my consciousness."
m "You know they say that dance is like sex."
ms "I pressed him with my whole body and rubbed my butt against his penis."
m "And some say that dance is even better."
ms "Bob practically stopped moving. He looked like a frightened rabbit."
ms "And damn how I liked this power over him ..."
ms "I got up on tiptoe and pushed his cock with my ass."
ms "My weight would not be enough to drop him - after all he is much heavier than me."
ms "But Bob still slightly staggered and grabbed my hips."
show cg mila_and_bob_dance_from_behind_hands_on_hips:
    ypos 1.8
    linear 5.0 ypos 1.1
ms "I caught his gaze and smiled."
ms "Bob wanted to remove his hands, but I took him by the wrists and ran it along my body, along my waist, to my hips ..."
ms "On then my chest ..."
define flash = Fade(0.1, 0.0, 0.5, color="#FF0080")
show cg mila_and_bob_dance_from_behind_hands_on_tits with flash
ms "His palms were glued to my clothes, and the only thought in my head was:"
ms "I want to get naked..."

label continue_dance_bob:
scene bg restaurant
ms "But the music ended, and we found ourselves hugging in plain sight, and it became suddenly shameful."
show mila jeans_and_blouse_sad_looking_up
m "..."
show bob suit_awkward_smile:
    xzoom 0.8 yzoom 0.8
bob "..."
hide bob
hide mila
scene bg bob_table_happy_laugh
ms "We returned to our table."
ms "For a while we drank wine silently, which allowed us to relax a little. And then blabbed until closing."
ms "At long last, Bob smiled at me and spoke without the restrictions of his complexes."
ms "We returned home after midnight... Drunk and happy."
"..."
"..."
scene bg doors with fade
show mila jeans_and_blouse_front
m "Thanks Bob..."
m "I had a great time."
show bob suit_smile at left:
    xzoom 0.8 yzoom 0.8
ms "Bob smiled. {w} For real. {w}It wasn't his usual grimace. {w} It was a good, solid smile of joy."
show mila jeans_and_blouse_run_smile
ms "I smiled back."
bob "Thank you. I liked it too ..."
m "..."
show bob suit_frown
ms "In less than a second, his smile faded again, and sadness returned to his eyes."
bob "Okay, I'll go. {w}Have a good evening."
ms "Bob hastily turned, but I caught his sleeve with the usual movement."
show mila jeans_and_blouse_sad_looking_up
m "Wait..."
show bob suit_sceptic
ms "Bob froze and turned around."
hide mila
show cg mila_kiss_shy_looking_down at right:
    xzoom 0.85 yzoom 0.85
    ypos 0.9
ms "I played with the keys in my hand."
m "Do you know what it means if you bring a girl home after a date and she doesn't hide behind the door right away?"
show bob suit_frown
bob "..."
show bob suit_frown_open_mouth
bob "No? How should I know?"
show bob suit_frown
m "..."
show cg mila_kiss_shy_looking_up_biting_lip with dissolve
ms "I glanced at Bob and smiled in a suggestive manner."
ms "Bob did not understand the hint."
show cg mila_kiss_shy_looking_up_hair_hand with dissolve
ms "I removed my hair behind my ear and shot my eyes again."
ms "Bob looked at me thoughtfully."
show cg mila_kiss_haaaa with dissolve
ms "I sighed."
show cg mila_kiss_pout with dissolve
m "Kiss me already ..."
bob "I don't think..."
ms "I interrupted his excuses with a gesture."
m "Stop thinking. {w}Enough of your doubts. {w}I already showed enough initiative."
ms "I paused to give my next words more power."
show cg mila_kiss_love_smile with dissolve
m "It's your turn."
bob "..."
m "..."
ms "The silence became so tense and sharp that it seemed as if it could cut you."
ms "Bob swallowed and took a step towards me."
show cg mila_kiss_kiss:
    ypos 1
    linear 1 ypos 0.9
ms "I raised my chin and closed my eyes to make it easier for him to kiss me."
hide bob
m "..."
bob "..."
m "..."
show cg mila_and_bob_kiss_side at truecenter:
    xzoom 1 yzoom 1
bob "..."
m "..."
ms "The kiss was so light and gentle that I hardly even noticed it."
hide cg
show bob suit_awkward_smile at left:
    xzoom 0.8 yzoom 0.8
show mila jeans_and_blouse_blush_embarassed_twist_hair
ms "I opened my eyes and looked at Bob."
ms "He turned away, embarrassed."
m "..."
bob "..."
show mila jeans_and_blouse_blush_looking_aside
ms "We stood in awkward silence for a while."
m "Good night Bob. {w}Thanks for a wonderful evening."
ms "Bob smiled and opened his mouth to say something."
ms "But his eyes stopped at our door, and he became sad again."
show bob suit_frown_open_mouth
bob "And you... both of you..."
show bob suit_awkward_smile
ms "Bob smiled sadly."
show mila jeans_and_blouse_sad_looking_aside
bob "Good night."
ms "He turned away and went to his apartment."
m "..."
m "..."






"{w}. {w}. {w}."
scene bg door with fade
play sound "door-open-close.mp3"
label menu_paul_and_mila_first_dominance_challenge:
show screen nts_stats_overlay
menu:
    "Who is more dominant now?"

    "Paul (Requires 2+ Mila's submissiveness) (Mila's submissiveness + 1)" if dom >= 2:
        $ dom += 1
        jump netorase_stats_scene1_paul

    "Paul (Not enough Mila's submissiveness)" if dom < 2:
        "Paul hesitated, he wasn't sure, that Mila is ready to be dominated."
        "She needs at least 2 submissiveness."
        jump menu_paul_and_mila_first_dominance_challenge

    "Mila (Requires 2+ dominance) (Mila's dominance + 1)" if mila_dom >= 2:
        $ mila_dom += 1
        jump netorase_stats_scene1_mila

    "Mila (Not enough dominance)" if mila_dom < 2:
        "Mila hesitated. She still lacked the resolve to dominate."
        "She needs at least 2 dominance."
        jump menu_paul_and_mila_first_dominance_challenge


label netorase_stats_scene1_paul:
show bg paul_and_mila_kiss_shock
ms "As soon as I opened the door, Paul grabbed my hand and dragged me inside."
hide screen nts_stats_overlay
ms "The door slammed shut behind me, and I found myself pressed with my back to the door."
ms "Paul covered my lips with his and passionately kissed me before I managed to understand what was happening."
show bg paul_and_mila_kiss_closed_pleasure
ms "His hot hands glided over my body."
ms "I closed my eyes and surrendered to the sensations."
ms "After a few long moments, Paul leaned back and I was able to take my breath."
show bg paul_and_mila_face_to_face
m "..."
p "..."
m "Hey..."
m "What was that?"
p "I... {w}heard you when you left the elevator."
p "I looked through the peephole..."
show bg paul_and_mila_face_to_face_embarassed
ms "Previous events flashed through my head."
ms "Blood rushed to my face and suddenly it became even hotter in here than before."
show bg paul_and_mila_face_to_face_embarassed_cautious
ms "My back was covered with cold sweat. I met Paul's gaze, expecting to see anger, jealousy and resentment there."
ms "But it was just pure animalistic desire."
ms "I swallowed."
m "Do you want... {w}I mean...{w} Maybe we should go to the bedroom?"
p "No."
ms "In a low hoarse voice, provoked goosebumps that ran across my skin."
show bg paul_and_mila_face_to_face_embarassed_biting_lip
ms "His strong hands stroked my body and I melted under his touches."
p "Raise your shirt."
ms "The wine and desire ruled over my head."
ms "I wanted only one thing - to obey."
ms "Listen to his voice. Do what he wants."
show bg paul_and_mila_face_to_face_embarassed_pulled_by_self
m "..."
m "..."
p "Take it off."
show bg paul_and_mila_face_to_face_embarassed_bra
ms "I obeyed."
m "..."
ms "He kissed me again and ran a hand over my waist and hips."
ms "I felt his desire with my whole body."
ms "And I understood how hard it was for him to restrain himself."
ms "I did not understand {b}why{/b} he was holding back."
ms "He leaned back again."
p "Take off the bra."
show bg paul_and_mila_face_to_face_embarassed_topless
ms "I obeyed."
ms "The bra slipped along my elbows and fell to the floor."
ms "The room was hot but my skin of my chest was much more tender and sensitive."
ms "I felt hundreds of invisible needles dig into the skin."
ms "Paul devoured me with his eyes."
ms "He saw me naked hundreds of times."
ms "But now ... for some reason it felt like it was our first time."
show bg paul_and_mila_face_to_face_embarassed_topless_squeeze
ms "Paul rudely squeezed my hardened nipples."
m "Ouch!"
ms "Paul released my nipples almost immediately, but the pain did not want to disappear."
ms "I covered my chest with my hands."
show bg paul_and_mila_face_to_face_embarassed_topless_covering_breasts
m "That hurt..."
ms "Paul ignoring my words again dug his lips into my lips."
ms "He pressed me to the door and I felt locked in this narrow space."
ms "His aggression and desire felt as if he wanted to eat me."
show cg paul_and_mila_kiss_close_up
ms "I again felt a mixture of fear and excitement."
ms "Like I'm prey in his hands."
ms "But it wasn't scary."
ms "I knew that he would stop if I asked.{w} I saw his raw desire, and I liked the fact that I made him feel like that."
ms "I wanted to tame his animal nature. {w}And for this it was necessary to obey. {w}Adapt."
ms "So into my thoughts, I did not notice when Paul's hand unbuttoned my jeans."
ms "I felt his fingers spread my wet labia."
ms "His palm pressed against the clitoris and I moved my hips forward clinging to it stronger."
show cg paul_and_mila_jeans_shlick at truecenter:
    xzoom 0.7 yzoom 0.7
m "Mmm..."
p "You are so wet, whore ..."
m "..."
ms "Paul's rude words flew past my ears."
ms "I was too focused on sensations. {w}And I wanted to hear his voice too much."
m "Mmm..."
ms "I did not notice at what point he lowered my jeans. {w}They were in the way, so I completely removed them."
ms "Paul continued to caress my pussy while I was stripped."
ms "That's why it was hard to undress."
ms "But I did not want him to stop."
ms "I did not want these sensations to stop for a moment."
ms "And I didn't want to lose my mood..."
ms "Paul pressed me to the door and stopped his moving fingers."
show cg paul_and_mila_panties_shlick
ms "I could not restrain myself and began to move my hip myself, fucking myself with his fingers, like they were his dick."
ms "But Paul did not let me stimulate myself too much, holding me on the verge of orgasm."

if paul_touch_ass:
    p "Did you do what I asked?"
    ms "I moaned in response something unclear."
    show cg paul_and_mila_panties_shlick_wipe_hand:
        xzoom 1 yzoom 1
    ms "Paul pulled his fingers from my pussy and wiped them on my face."
    ms "Moisture, humiliation and stopped stimulation allowed me to slightly come to my senses."
    p "You did what I asked, whore?"
    show cg mila_dazed_with_paul
    m "..."
    ms "I did not immediately understand what he was demanding."
    ms "But then I realized that he was talking about his request."
    m "Yes... {w}we...{w} we danced..."
    ms "My thoughts were fogged.{w} I wanted to stop talking and finally feel his cock inside."
    ms "A lump stood in my throat."
    show cg mila_dazed_tears_with_paul
    ms "Paul's piercing gaze was filled with jealousy and desire.{w} I could not understand what he was thinking.{w} For some reason, I felt offended and tears came to my eyes."
    m "I put bob's hands on my ass ..."
    m "And I rubbed against him while we danced ..."
    jump netorase_stats_scene1_paul_continue

ms "I realized that Paul hardly held back, and I wanted to tease it even more."
show cg paul_and_mila_panties_shlick_smirk
m "You know when we were on that date ..."
ms "I did not recognize my voice. It sounded lower than usual."
ms "As if it wasn't me talking, but someone else."
m "We went out to dance ..."
ms "Paul pulled my panties.{w} The fabric painfully moved into a pussy,{w} but I was happy with any stimulation."
ms "And his jealousy mixed with desire excited me more."
ms "I slightly pushed forward my hips, not taking my eyes off the Paul."
m "I clung to him with my body ..."
m "I felt his cock rub my ass."
m "And you know what he did at that moment?"
p "..."
ms "Paul again inserted his fingers into my pussy and I groaned involuntarily."
m "Mmm..."
ms "Paul's movements were rough, fast, and a little awkward."
show cg paul_and_mila_panties_shlick_hand_in_pants
ms "This allowed me to come to my senses a little and put my hand in his pants."
ms "I felt his cock and wrapped my hand around it."
ms "Paul's movements became less strong, he was distracted by his sensations."
ms "I whispered in his ear."
m "When we danced his hands glided all over my body ..."
m "He caressed my hips..."
m "My tummy..."
m "My tits..."
show cg paul_and_mila_kiss_close_up:
    xzoom 1 yzoom 1
ms "Paul passionately kissed me and pressed me to the door ..."
m "Mmm..."
label netorase_stats_scene1_paul_continue:
ms "I heard the click of the lock."
hide screen nts_stats_overlay
ms "My heart pounded frantically in my chest."
scene bg mila_panties_shock_scared
m "Paul? Are you crazy?!"
p "Shhhh."
m "I am almost naked!"
p "Hush, I said."
ms "Paul opened the door and took my hand out of his pants."
ms "I looked around nervously, in a panic, expecting that one of our neighbors' doors would open ..."
ms "How would I look in their eyes if this happens?"
scene bg mila_panties_scared_blush
m "..."
ms "They will point fingers at me ..."
ms "Women will be contemptuously disgusted ..."
ms "And the men ... will devour me with their eyes ..."
scene bg mila_panties_blush_closed_biting
m "Mmm..."
"..."
scene bg mila_at_door_panties with fade
ms "I found myself standing opposite the door to the Bob's apartment."
ms "Paul forced me to bend my back."
ms "Cool air pricked the skin. But excitement did not allow me to freeze."
ms "Paul took my hair and inserted his fingers in my pussy."
scene bg mila_at_door_finger_fuck
m "Mmm..."
ms "I could not hold back a moan."
p "So, you danced and kissed another man, despite the fact that you are married?"
m "..."
ms "For a moment I was scared. But feeling Paul's fingers in my pussy and his touch, I realized that he was not angry."
ms "That this is just part of the game."
scene bg mila_at_door_finger_fuck_clenched_teeth
m "Yes..."
p "And you got excited from that?"
ms "I involuntarily squeezed my legs and pushed my hips towards his fingers, wanting to feel them deeper in me."
m "Yes...{w} very much..."
p "What would you call a girl who behaves like that?"
scene bg mila_at_door_finger_fuck_pressed_lips
m "..."
ms "I didn't want to say it out loud. Especially here, in a public place...{w} Right against the door to Bob's apartment..."
ms "But excitement took over."
m "{size=-10}Slut..."
p "That is, you admit that you are a nymphomaniac slut, who melts from the touch of another man?"
m "{size=-6}Yes..."
scene bg mila_at_door_finger_fuck_scream
m "{size=-4}Yes{w} {size=-2}Yes{w} {size=+6}Yes!"
p "Hush, don't shout ..."
ms "My thoughts were covered by a pink fog, I stood on the edge of the abyss, and hardly restrained my screams."
ms "Paul stopped his fingers."
scene bg mila_at_door_finger_fuck_pressed_lips
p "Don't you think that this it's not enough for you?"
ms "I was confused...{w} I did not understand what he was saying,{w} I just wanted to feel his cock inside..."
m "Huh?"
p "Do you want to cum, whore?"
scene bg mila_at_door_finger_fuck_begging
m "Yes, very much...{w} Please, fuck me ..."
ms "But Paul was in no hurry and continued to hold me on the verge."
m "Please..."
ms "Paul took me by the throat and brought his lips close to my ear."
scene bg mila_at_door_finger_fuck_holding_neck
p "You know, I think for such a pervert as you it's not enough."
ms "I swallowed. Even through a veil of excitement, I understood that something was wrong."
p "I think you want more. So?"
m "..."
ms "I said nothing."
scene bg mila_at_door_finger_fuck_bitting_lips
ms "Paul moved his fingers and I bit my lip so as not to groan."
ms "Drops of my juices flowed down my leg."
ms "I realized that I would do anything to cum."
scene bg mila_at_door_finger_fuck_begging
m "Paul ... please ..."
p "Quiet."
scene bg mila_at_door_finger_fuck_bitting_lips
ms "I bit my lip."
p "You are just ashamed to admit it, right?"
m "..."
p "But ask yourself. Who are you?"
m "..."
scene bg mila_at_door_finger_fuck_tears
ms "I swallowed."
ms "Say it."
m "I'm...{w} I'm a slut..."
p "Exactly."
p "Remember this when you doubt how to behave with Bob."
p "Understood?"
m "..."
m "Yes..."
p "Do you like being a slut?"
scene bg mila_at_door_finger_fuck_bitting_lips
ms "Paul's fingers continued to caress me. But this time I realized that he was pushing me closer to the edge."
m "Yes!"
p "Quiet."
p "Do you want to be seen?"
m "..."
scene bg mila_at_door_finger_fuck_hands_mouth
ms "I clasped my mouth with my hands and closed my eyes, concentrating on sensations."
p "Tomorrow you will behave like a slut with a bob."
ms "..."
ms "I hardly understood what he was saying. I surrendered to the flow of feelings and sensations."
p "Tomorrow you will give him pleasure."
p "Not as a whore who expects something in return."
p "You will please him like a real slut."
p "Understood?"
m "MGM ..."
ms "I continued to clamp my mouth and tried not to make any sounds."
ms "I heard the noise of the elevator, someone called it on one of the floors. But Paul did not pay attention to that."
ms "The fear of being caught, shame and excitement were mixed into a perverted cocktail."
ms "And Paul's fingers continued to press the insides of my pussy."
p "Do you want to cum?"
m "MGM!"
ms "I mumbled in the affirmative something slurred."
p "Will you behave like a slut from now on?"
m "MGM!"
ms "Yes, fuck it!{w} Just let me cum..."
scene bg mila_at_door_finger_fuck_hands_mouth_tight_hug
ms "Paul squeezed me in his arms and began to fuck me with his fingers."
scene bg mila_at_door_finger_fuck_hands_mouth_tight_hug_rolling_eyes with flash
m "..."
scene bg mila_at_door_finger_fuck_hands_mouth_tight_hug_rolling_eyes_legs with flash
m "!"
scene bg mila_at_door_finger_fuck_hands_mouth_tight_hug_rolling_eyes_legs_cum with flash
m "!!!"
ms "It seems to me for a second I lost consciousness."
ms "The muscles of my legs were involuntarily reduced."
ms "My breath stopped."
ms "It seems to me that my heart also stopped fighting."
ms "Or was beating so hard that I was deaf."
scene bg mila_at_door_finger_fuck_hands_mouth_tight_hug_leg_after_sex
ms "It seems to me I screamed, but Paul clamped my mouth with his hand."
ms "Through the veil of orgasm, I heard a bell of the elevator."
ms "Paul pulled me inside our flat and we disappeared behind the door a moment before the elevators opened."
scene bg paul_and_mila_face_to_face_tired
m "Haaa Haaa ..."
ms "I lay on the floor and breathed heavily from the recently experienced orgasm ..."
scene bg paul_and_mila_face_to_face_laugh
p "Ahah."
ms "Paul laughed and I laughed with him."
ms "I felt light and happiness..."
ms "My head was empty and free from thoughts."
scene bg paul_and_mila_lying_from_above
m "..."
p "..."
p "But if anything, it wasn't a joke."
scene bg paul_and_mila_lying_from_above_mila_confused
ms "I raised my head and looked at him in confusion."
p "I mean... tomorrow...{w} I want you...{w}to go even further ..."
ms "I swallowed."
m "Are you serious?"
p "..."
p "Yes."

if dom >= mila_dom:
    m "I ... I'm not sure that I can."
    scene bg paul_and_mila_lying_from_above_mila_confused_paul_looking
    p "You can.{w} Just remember how you felt today."
    p "Wake up your inner pervert."
    p "Although ... I doubt that she is sleeping ..."
    ms "I jokingly hit him on the shoulder."
    scene bg paul_and_mila_lying_from_above_mila_shy_love_paul_looking
    m "Hey!"
    p "Ahah..."
    m "..."
    p "..."
    scene bg paul_and_mila_lying_from_above_mila_smirk_paul_confused
    p "So?"
    p "Will you do it for me?"
    m "..."
    m "..."
    m "{size=-10}Fine..."
    ms "Suddenly I felt hot from shame or excitement."
    ms "I did not immediately realize what I agreed to."
    ms "The boundaries of acceptable things expanded, what once seemed unthinkable now became reality."
    scene bg paul_and_mila_lying_from_above_hug
    ms "I wanted to feel our connection, our intimacy and love, so I clung to him."
    ms "He stroked my back."
    ms "This simple gesture was enough for me to calm down."
    m "Fine..."
    ms "I repeated with more confidence."
    if _in_replay:
        return
    jump bob_first_hj
ms "Despite my recent orgasm, a playful mood took over me."
scene bg paul_and_mila_lying_from_above_mila_smirk
m "Is it true?"
p "..."
ms "My proactive reaction made Paul a bit confused."
show bg paul_and_mila_lying_from_above_mila_smirk_paul_confused
m "That is, you want your wife to behave like a whore?"
p "..."
ms "I climbed onto him and smiled."
show bg paul_and_mila_missionary_smirk
m "Do you want your precious girl to behave depraved not only with you, right?"
ms "But Paul did not look away this time and smiled at me."
ms "His hands stroked my hips."
p "Yeah baby. I want it."
m "Hehehe ..."
ms "I felt his hard dick rubbing my ass."
ms "My skin tinged with excitement."
ms "I felt like the boundaries of acceptable things had expanded, what once seemed unthinkable now became reality."
ms "And I liked this reality more and more ..."
m "Fine."
ms "I leaned over."
show bg paul_and_mila_lying_from_above_hug
m "But you better take responsibility and love me as I will become."
ms "Paul smiled."
p "Naturally."
p "You are the hottest woman in the world."
if _in_replay:
    return
jump bob_first_hj

label netorase_stats_scene1_mila:
scene bg door with fade
play sound "door-open-close.mp3"
show paul suit_open_mouth_blush at left
ms "When I came home, an excited Paul met me almost on the threshold."
ms "He froze a couple of steps from me and opened his mouth, but did not say anything."
show mila jeans_and_blouse_sad_looking_up at center
p "..."
m "..."
m "Hello..."
p "Hello..."
show paul suit_blush_looking_aside
ms "Paul looked away."
show mila jeans_and_blouse_front
ms "The kiss with Bob, the date, and the passive behavior of Paul put a sadistic nature in me."
ms "I unzipped the fly on my jeans and went towards him."
ms "My pressure forced him to take a few steps back until he bumped into the chair and sat down."
ms "I smiled and lowered my jeans."
scene bg mila_unzipped_lowered_jeans_smirk_tease
m "We had a great time together."
m "We walked a little, and then went to the restaurant."
scene bg mila_from_behind_pulloff_jeans
ms "I turned my back to Paul and bent over to pull off my jeans."
ms "Paul's penis swelled and protruded in his pants."
m "We drank a little and danced."
ms "I turned back and threw my leg on Paul's shoulder."
scene bg mila_leg_on_shoulder_wet_panties
ms "I brought my crotch closer to his face and felt his hot breath on my pussy."
m "We danced and his hands caressed my body..."
scene bg mila_leg_on_shoulder_panties_aside_juice
ms "I moved my panties aside and showed how wet I was."
m "Do you want to taste how much I liked it?"
ms "Paul did not hesitate long, he eagerly put his tongue in my pussy and began to lick my juices."
scene bg mila_leg_on_shoulder_panties_aside_juice_spread_pussy
m "Mmm... a good boy..."
m "..."
m "Mmmm..."
m "Yes..."
m "Like that..."
m "Ahhh..."
ms "Paul's tongue played with my clitoris and plunged deep into my pussy."
scene bg mila_leg_on_shoulder_panties_aside_head_grab
ms "I grabbed his hair and pressed him to my crotch."
m "Oh yeah..."
ms "I realized that it was hard for me to stand on my feet."
ms "But I did not want to go to bed and give myself to Paul's mercy."
ms "I wanted to tease him..."
ms "I leaned back and then took a step."
m "Undress and lie down."
ms "Paul doubted for some time, but then obeyed."
scene bg mila_panties_aside_pov_face_sitting
ms "I stood above his face."
ms "He looked so sweet and helpless from above..."
ms "I wonder how Bob would look from the same angle?"
m "..."
scene bg mila_panties_aside_pov_face_sitting_looking_aside_confused
m "!"
ms "What am I thinking about?"
m "..."
ms "Wait...{w} Why not?"
scene bg mila_panties_aside_pov_face_sitting_grin
ms "I grinned."
m "Do you want your wife to sit on your face?"
p "Yes!"
ms "Paul grabbed his penis and made several strokes."
scene bg mila_panties_aside_pov_face_sitting_threaten_finger
ms "I shook my finger."
m "Nope, stop!"
m "Hands off."
ms "Paul obeyed."
scene bg mila_panties_aside_pov_face_sitting
m "Good boy."
ms "I squatted down and pressed my pussy to his lips."
scene bg mila_panties_aside_face_sitting_from_side_hands_on_chest
ms "His nose entered my pussy. I bit my lip and made several movements to get comfortable."
m "Mmm..."
ms "Paul was breathing through his mouth, and feeling his breath, my clitoris became even more sensitive."
ms "Paul began to caress it gently with his tongue."
m "Mmm, yeah..."
m "Like that..."
p "..."
m "It seems to me that I become addicted to these sensations ..."
m "Mmm...."
ms "I rested my hands on Paul's chest and made several movements with my hips."
m "Haaa Haaa..."
m "Yeees..."
ms "Paul dick swayed in front of my face. He pulsed it slightly, as if trying to attract attention."
m "Do you want me to jerk you off?"
p "Yes! I beg you!"
m "Ahah..."
m "I will do whatever you want, but with one condition ..."
ms "Paul froze for a second, but then continued to caress my pussy with his tongue."
m "Tomorrow I will do the same for Bob."
ms "Paul froze again."
ms "I moved my hips and my fingertips ran along his stomach and hips."
m "What do you say?"
p "..."
ms "His cock pulsed in a beginning motion to get me to stroke it."
ms "But I wanted to hear Paul's voice."
ms "I wanted to feel that he is ready...{w} that we are both ready.{w} To the next step{w} into the abyss."
ms "That we are ready to go from words to action, from fantasies to reality."
ms "Paul hesitated and I realized that he is not ready. He would refuse."
ms "Therefore, I just began to enjoy the sensations."
ms "I closed my eyes and moved my hips, approaching orgasm."
m "Yes, dear...{w} like this ..."
m "More...{w} Right there, yes..."
m "Ahhh ahhh..."
m "I'm almost...{w} A bit less pressure..."
m "Ahhh..."
m "Mmm..."
ms "I felt as Paul took me by the wrist and pulled me down."
ms "At first I did not understand what he wanted."
ms "But when his cock poked into my palm, I was thrown into heat."
ms "For some reason, I imagined that in my hand is Bob's penis, not Paul's."
ms "I slowly ran down and up, trying to adapt to my own rhythm."
ms "It felt like I touched it for the first time."
ms "Paul started to move his hips."
ms "He was already at the edge."
m "Mmm...."
ms "His cock began to pulsate in my hand, and at that moment, I realized that I was not far from orgasm either."
ms "I wanted to feel sperm on my skin, so I leaned over and put my face closer."
p "Mhhmhm!"
ms "Paul fired onto my face with a tight stream of sperm."
ms "It was so hot that it felt like it burned me...{w} And this was the last straw for me."
scene bg mila_orgasm_close_up_split_from_side
ms "I felt the muscles of my legs began to ripple from my orgasm."
ms "The sensations were so bright and heavy that it seemed to me that I was dying."
ms "I almost did not feel how Paul was covering my face with sperm."
ms "That sensation was lost in a general squall of sensations."
ms "I dug my nails into Paul's hips and growled like a beast."
"..."
"{w}. {w}. {w}."
scene bg mila_in_sperm_on_pauls_chest
ms "When we finally calmed down, I realized that I could not move."
ms "But I somehow gathered my strength, rolled over and lay down next to Paul."
m "Fuuuh ..."
m "It was cool."
p "It really was ..."
m "..."
p "..."
scene bg mila_looking_at_paul_in_sperm_on_pauls_chest_paul_worried
p "Was that joke about ... about Bob?"
ms "I looked at him."
m "What will you say if I say \"No\"?"
p "..."
scene bg mila_looking_at_paul_in_sperm_on_pauls_chest_paul_frown
ms "Paul frowned."
ms "I was waiting for his answer and for some reason, I was worried."
p "..."
p "I don't know..."
scene bg mila_looking_at_paul_smile_in_sperm_on_pauls_chest_paul_frown
ms "I smiled. For some reason, I knew that he would answer that way."
m "Then no. It wasn't a joke."
p "..."
m "What do you say now?"
ms "Paul was silent even longer."
ms "But still after a while he quietly answered."
scene bg mila_looking_at_paul_smile_in_sperm_on_pauls_chest_paul_fine
p "{size=-6}Fine..."
ms "He seemed so vulnerable to me."
ms "I sighed."
p "Paul."
ms "He looked at me and immediately looked away."
scene bg mila_looking_at_paul_serious_in_sperm_on_pauls_chest_paul_giggle
p "Look at me."
ms "Paul looked up and smiled strangely."
m "?"
p "..."
p "You look very funny when you try to be serious covered with sperm."
ms "I licked my lips."
m "You think?"
ms "Paul blushed."
ms "The tension between us evaporated."
scene bg mila_looking_at_paul_serious_in_sperm_on_pauls_chest_paul_serious
m "Look. {w}I do what I do, because both of us like it, and only if it's true we will continue.{w} You do understand that, right?"
p "..."
p "Yes."
m "We can stop it at any time if we want.{w} Like right now, for example."
p "..."
m "Understand?"
p "..."
p "Yes."
m "..."
m "I'll ask you again, do you want to continue?"
ms "Paul met my gaze more confidently."
p "Yes. {w} Yes, I want it."
scene bg mila_looking_at_paul_smile_in_sperm_on_pauls_chest_paul_confident
ms "I smiled."
m "Ok."
m "I love you, Paul."
p "..."
p "I love you too..."
if _in_replay:
    return



label bob_first_hj:
"{w}..."
scene bg mila_woke_up_stretch
ms "I woke up early"
ms "Something changed in me..."
ms "It felt like I was still in a dream"
ms "And could do anything I hadn't even dreamed of before"
ms "I kissed Paul who was still sleeping and quietly went to the bathroom"
scene br with fade
show mila casual_worried at center
ms "..."
ms "Fingers trembled with excitement or nervousness"
ms "I wasn't sure was there more excitement or more nervousness..."
ms "I ran my hands over my thighs and chest"
ms "The skin covered in goosebumps in response to this touch."
ms "..."
show mila casual_thinking
ms "For some reason I couldn't decide..."
ms "I knew what I need to do... {w}What I want to do..."
ms "But fear got in my way; I felt defenseless and vulnerable."
ms "I wanted to do it... But at the same time I wanted to hide..."
show mila casual_interested_blush
ms "My gaze fell on the suit that I found in Bob's apartment and took to wash."
ms "..."
m "I wonder would it fit me?"
ms "..."
show mila dva_concerned
ms "..."
show mila dva_back
ms "..."
show mila dva_posing
ms "..."
m "Ahah..."
ms "The nervousness disappeared as if by hand."
show mila dva_think
ms "Hm..."
m "What if..."
ms "I looked at myself in the mirror"
ms "..."
ms "I think I've seen this character somewhere..."
show mila dva_serious
ms "Should she be serious?"
ms "..."
show mila dva_think
ms "No, something is wrong."
show mila dva_cheerful
ms "Maybe cheerful and bright?"
ms "..."
show mila dva_concerned
ms "Hehe. Looks cool."
ms "I was so different from myself that it gave me confidence"
ms "I put on my coat and carefully, trying not to make any noise, I went into Bob's apartment."
play sound "door-open-close.mp3"
scene bg bobs_apartments_clean with fade
ms "My heart was pounding in my chest"
play sound "heart.mp3"
ms "Palms covered with sweat"
show mila dva_concerned
ms "What am I doing?"
ms "What am I doing here?"
ms "Mila... Do you understand what will happen after?"
ms "..."
show mila dva_concerned_looking_aside_blush
ms "Yes, we agreed that I would behave...{w} different"
ms "But damn..."
scene bg closed_door
show mila dva_concerned:
    ypos 0.35
ms "I reached out my hand to the handle of the door to Bob's room and froze."
play sound "heart.mp3"
show mila dva_concerned_looking_aside_blush
ms "I... Do I really want to do this?"
ms "..."
show mila dva_scared
ms "After all, there will be no turning back."
ms "What if Paul thinks this isn't what he wants?"
ms "What if I don't like it?"
ms "What will I tell Bob in that case?"
ms "..."
ms "Shit shit shit"
ms "I swallowed."
ms "Thoughts rushed through my head chaotically. I couldn't keep track of them."
ms "My legs took a step back without my command."
ms "..."
show mila dva_concerned
ms "Maybe it's worth rethinking everything again?"
ms "We... {w}We could go to a bar together...{w} Or invite Bob over..."
ms "..."
scene bg bobs_apartments_clean
show mila dva_sad_smile
ms "Yes.{w} It's probably better to do that."
stop sound
ms "I somehow immediately calmed down, turned around and walked towards the exit."
ms "It will be better this way."
ms "..."
show mila dva_concerned
ms "Walking past the mirror, I glanced at myself and froze."
ms "..."
ms "Wait."
ms "Am I dressed up for nothing?"
ms "Maybe at least take a selfie?"
play sound "shot.mp3"
scene bg mila_bobs_apartment_dva_selfie_smile
ms "I smiled at my idea, took out my phone and pointed the camera at myself."
ms "..."
scene bg mila_bobs_apartment_dva_selfie_upset
ms "..."
ms "For some reason, my fear and eternal desire for half-measures irritated me."
scene bg mila_bobs_apartment_dva_selfie_agry
ms "How long it takes to accept myself?"
ms "Am I really a scaredy cat?"
ms "..."
ms "Fuck it"
ms "I'm going in"
scene bg closed_door
ms "..."
play sound "door-open-close.mp3"
scene bg bobs_room_bob_sleep
show mila dva_scared at truecenter:
    ypos 0.75 xpos 0.75
ms "..."
ms "After I came into the room, I immediately froze up"
ms "All of my courage evaporated"
ms "Bob was lying on the bed snoring."
if mila_was_in_the_room:
    ms "The room also smelled of sperm and sweat."
    ms "The smell seemed to get even stronger"
    jump dva_continue
ms "There was a heavy smell of sweat and sperm in the room."
ms "The air seemed sticky and dirty."
label dva_continue:
scene bg bobs_room_bob_sleep_mila_opens_window
ms "I tiptoed to the window and opened it."
ms "Fresh cool air instantly cleared the room of odor"
scene bg bobs_room_bob_sleep
ms "Bob's chest rose and fell slowly. {w}He slept peacefully with his limbs scattered on the bed."
show mila dva_concerned at truecenter:
    ypos 0.75 xpos 0.75
ms "..."
ms "So... So what's next?"
ms "..."
show mila dva_scared
ms "I swallowed."
ms "Then I slowly sat down on the edge of the bed and touched Bob's leg."
m "{size=-12}Bob!"
ms "..."
ms "He didn't react."
m "{size=-8}Bob!!"
ms "I called him a little louder, but he still didn't respond."
ms "..."
play sound "heart.mp3" loop
ms "My heart was pounding loudly in my chest."
ms "I grabbed the edge of the blanket and pulled it to the side"
ms "..."
ms "..."
ms "A second later it slid to the floor."
scene bg bob_on_bed_nude_flacid_sleep_mila_shock
ms "Oh. {w}My.{w} God."
ms "Bob's dick was thicker than Paul's even in this relaxed state."
scene bg bob_on_bed_nude_flacid_sleep_mila_blush
ms "I wanted to touch it, but I restrained myself, afraid of waking Bob."
ms "The skin on his penis had turned red - apparently he jerked off yesterday as if there was no tomorrow"
ms "..."
scene bg bob_on_bed_nude_flacid_sleep_mila_bitlip
ms "I wonder what he imagined?"
ms "..."
ms "As if hypnotized, I looked at his penis and imagined Bob masturbating."
ms "My hand reached down."
ms "The suit prevented me from touching my pussy, so I just rubbed it through my clothes."
m "{size=-4}Bob?"
ms "I called him again. My voice sounded hoarse and low."
ms "I swallowed."
ms "Bob didn't react."
ms "..."
ms "What should I do?.."
ms "..."
scene bg bob_on_bed_nude_flacid_sleep_mila_scared
ms "I stroked his leg."
ms "His breathing froze for a moment, and I froze along with him."
ms "I didn't know what I wanted more, for him to wake up or not."
ms "His skin was soft and hot. {w}I felt how heavy his body was just by touching him."
ms "My gaze was drawn to his cock. I didn't notice when I had got closer."
ms "My hand gently stroked his thigh, dangerously close to his huge balls."
scene bg closeup_hand_near_mila_aroused
ms "The heavy, unpleasant musky smell of penis filled my nose."
ms "I wanted to turn away from it, but at the same time this smell excited me."
m "{size=-8}Bob!?"
ms "For some reason my voice sounded quieter then the last time.{w} Now I was afraid to wake him up."
ms "I wanted this moment to last as long as possible."
ms "This smell.{w} This situation.{w} My clothes...{w} All this brought out something wild and animal in me."
ms "I licked my lips."
scene bg bob_on_bed_nude_flacid_sleep_mila_scared
ms "Bob moved, and I pulled my hand back in fear."
ms "..."
ms "But nothing happened."
scene bg bob_on_bed_nude_flacid_sleep_mila_angry
ms "Fear paralyzed me for a moment, but after a moment, I controlled myself and became angry."
stop sound
ms "I resolutely moved closer and grabbed Bob's penis."
scene bg flacid_handjob_mila_angry
ms "My fingers could hardly wrap around his thick cock."
bob "Mmm..."
ms "Bob muttered something in his sleep, but I couldn't understand what."
play sound ["loops/SexSlide5.wav", "<silence 1>", "loops/SexSlide6.wav", "<silence 1>", "loops/SexSlide7.wav", "<silence 1>", "loops/SexSlide8.wav", "<silence 1>", "loops/SexSlide9.wav", "<silence 1>", "loops/SexSlide10.wav", "<silence 1>", "loops/SexSlide11.wav", "<silence 1>", "loops/SexSlide13.wav", "<silence 1>", "loops/SexSlide14.wav", "<silence 1>", "loops/SexSlide15.wav", "<silence 1>", "loops/SexSlide16.wav", "<silence 1>", "loops/SexSlide17.wav", "<silence 1>", "loops/SexSlide18.wav", "<silence 1>", "loops/SexSlide19.wav", "<silence 1>", "loops/SexSlide20.wav", "<silence 1>"] loop
scene bg flacid_handjob_mila_excited_low
ms "I slowly stroked his cock, enjoying the way it hardened and throbbed in my hand."
ms "Oh my god, oh my god, oh my god!"
ms "I'm doing it!"
scene bg flacid_handjob_mila_excited
ms "I'm doing it!!!"
ms "I'm jerking off Bob!"
ms "His dick is in my hand!"
scene bg flacid_handjob_mila_excited_high
ms "AAAAA!!!"
ms "I'm such a slut!"
ms "..."
ms "Bob's dick swelled a little, but then stopped responding to my touch."
scene bg flacid_handjob_mila_offended
ms "For some reason I felt insulted by this."
ms "Am I not good enough for you?"
ms "..."
ms "I sat more comfortably and brought my face closer to the penis."
scene bg pov_handjob_eww
ms "The smell became even stronger."
ms "For a second I thought about using my mouth to help myself, but the smell took away all desire."
scene bg pov_handjob_neutral
ms "I grabbed his penis with both hands and began to gently massage it along its entire length."
bob "Hmmm..."
ms "Bob opened his eyes and looked at me in surprise."
scene bg pov_handjob_awkward
ms "I was confused, and didn't know what to do..."
ms "..."
ms "..."
ms "My hands continued to massage his penis by themselves."
ms "I smiled and spat on the cockhead, adding a little lubricant."
ms "Bob rubbed his eyes and looked at me without saying a word."
scene bg pov_handjob_bigger_cock_blush_bitlip
ms "His dick became completely hard in my hands, turning into a real giant."
ms "Oh Lord, how can it even fit inside me?"
ms "..."
ms "..."
ms "Who said that this may happen?"
scene bg pov_handjob_bigger_cock_shy_smile
ms "I smiled shyly at my thoughts."
ms "Bob was afraid to move and just looked at me silently."
ms "..."
ms "..."
ms "The pauses were still awkward and difficult."
ms "I just moved my arms and tried to focus on the movements."
ms "Bob stared at me and didn't even seem to breathe or blink."
scene bg pov_handjob_bigger_cock_looking_down_shy
ms "There was so much lust in his gaze... So much desire."
ms "I swallowed and lowered my eyes in embarrassment."
ms "Damn... I love it when he looks at me like that."
ms "Excitement clouded my mind."
ms "I wanted to do something even more depraved..."
show screen nts_stats_overlay
menu:
    "I'll just relax and try to please him (Mila's submissiveness + 1)":
        $ dom += 1
        jump mila_sub_hj_bob
    "I want to tease him (Mila's dominance + 1)":

        $ mila_dom += 1
        jump mila_dom_hj_bob

label mila_sub_hj_bob:
ms "I felt as if something was pressing on my shoulders dragging me towards his cock."
hide screen nts_stats_overlay
scene bg pov_handjob_bigger_cock_shy_smile
ms "I looked at Bob and met his gaze."
ms "He slowly and steadily followed my every movement."
play sound "heart.mp3" loop
ms "My lips were numb with excitement."
ms "My mouth filled with saliva."
ms "I slowly started to go lower"
ms "The smell of his dick became unbearable.{w} Unbearably exciting."
scene bg pov_handjob_bigger_cock_closer
ms "I leaned down closer to his penis."
ms "So close that I could see the pattern of his skin."
ms "A drop of pre-cum appeared on the cockhead."
scene bg pov_handjob_bigger_cock_closer_closed_eyes
ms "I closed my eyes..."
ms "Then leaned even closer."
ms "And kissed his cock."
play sound "kiss.mp3"
scene bg pov_handjob_bigger_cock_closed_eyes_kiss
bob "Mmm..."
ms "Bob shuddered and groaned."
ms "The cockhead was hot and wet from the salty precum."
ms "I opened my eyes and looked at him"
play sound "lick.wav"
scene bg pov_handjob_bigger_cock_open_eyes_lick
ms "I licked his penis gently without taking my eyes off Bob."
play sound "putin.wav"
scene bg pov_handjob_bigger_cock_open_eyes_deep_kiss
ms "I parted my lips and carefully let the head of his penis inside my mouth."
ms "I had to try hard to open my mouth enough to avoid hitting the dick with my teeth."
ms "And I still didn't succeed."
ms "God, what a huge dick he has."
ms "My second hand, against my will, went down and began to stroke my clitoris."
play sound "moan1.wav"
scene bg pov_handjob_bigger_cock_closed_eyes_deep_kiss
m "Mmm..."
ms "This time I moaned."
ms "I felt Bob move and felt a gentle touch on my hair."
scene bg pov_handjob_bigger_cock_open_eyes_hands_on_head_deep_kiss_surprised
ms "I opened my eyes and realized that Bob was holding my head."
ms "Passion and desire covered his eyes like a veil."
ms "..."
ms "I felt that he had little control over himself and tried to pull away."
ms "But he just pressed me closer to him."
play sound "gag1.mp3"
m "Mmm!"
ms "Bob slowly but steadily pushed his cock deeper inside my mouth"
play sound "moanprotest.wav"
scene bg pov_handjob_bigger_cock_open_eyes_hands_on_head_suck_scared_frown_mascara_tears
m "MMM!"
ms "I tried to resist..."
ms "But he was too strong and too willing"
play sound ["suck1/1.mp3", "suck1/2.mp3", "suck1/3.mp3", "suck1/4.wav", "suck1/5.mp3", "suck1/6.mp3", "suck1/7.mp3", "suck1/8.mp3", "suck1/9.wav", "suck1/10.mp3", "suck1/11.mp3", "suck1/12.mp3"] loop
scene bg pov_face_fuck_mascara_tears_saliva_scared
ms "Bob, not paying attention to my resistance, began to literally fuck my head"
ms "His cock was pounding its huge head into my throat."
ms "I somehow managed to breathe through my nose."
scene bg pov_face_fuck_mascara_tears_saliva_idle
m "Suck suck suck"
ms "..."
ms "..."
ms "Lights flashed before my eyes. It seemed like Bob's cock was knocking all thoughts out of my head."
ms "I realized that my hand was still frantically caressing my pussy."
ms "And damn... {w} I loved his brutal passion."
play sound ["suck2/1.wav", "suck2/2.wav", "suck2/3.wav", "suck2/4.wav", "suck2/5.wav", "suck2/6.wav", "suck2/7.wav", "suck2/8.wav", "suck2/9.wav", "suck2/10.wav", "suck2/11.wav"] loop
scene bg pov_face_fuck_mascara_tears_saliva_seductive_gaze
ms "And also despite the fact that he has poor self-control, he is still quite gentle and does not cross the line of cruelty."
ms "It allowed me to relax a little."
m "Suck suck suck."
ms "I realized that Bob would cum soon, and I began to caress his balls with my hand."
m "Suck suck suck."
ms "I felt like something is missing."
ms "Like I am afraid to go all in..."
ms "Afraid to let myself go... {w}And doing it half-assed"
ms "Like I don't want to please him for real..."
ms "And that made me angry"
play sound ["suck3/1.wav", "suck3/2.wav", "suck3/3.wav", "suck3/4.wav", "suck3/5.wav", "suck3/6.wav", "suck3/7.wav", "suck3/8.wav", "suck3/9.wav", "suck3/10.wav", "suck3/11.wav", "suck3/12.wav", "suck3/13.wav"] loop
play music ["moans/1.wav", "<silence 3>", "moans/2.wav","<silence 3>", "moans/3.wav", "<silence 3>"] loop
scene bg pov_face_fuck_mascara_tears_saliva_smile
ms "I began to move my tongue inside my mouth, licking his cockhead that was ramming my throat."
m "Mmm..."
ms "I realized that I could not hold back my moans, despite the rough treatment."
ms "I wanted him to continue using me."
ms "Like a sex toy. {w}Just like a cumdump."
ms "Like a slut."
m "Mmm..."
ms "Cum for me, big boy..."
m "Mmm..."
ms "..."
ms "Wait a sec..."
ms "Cum?"
ms "..."
ms "He'll cum soon..."
ms "..."
ms "Won't I choke on his..."
bob "Urgh!.."
stop music
stop sound
scene bg pov_face_fuck_mascara_tears_pressed_before_cum with hpunch
ms "Bob tensed and pressed my head into his crotch."
ms "Despite the desire to break free from his grip, I tried to relax and let his dick come deeper inside my mouth"
ms "It literally penetrated my throat"
ms "I felt his cockhead tightened even more, and in a moment shot a huge load of thick sperm into my throat."
play sound "SWFSlosh4.wav"
scene bg pov_face_fuck_mascara_tears_pressed_cum_full_mouth with hpunch
ms "It instantly filled my entire mouth."
ms "But that was only the beginning."
play sound ["SWFSlosh4.wav", "<silence 0>", "SDTGag14.wav"]
scene bg pov_face_fuck_mascara_tears_pressed_cum_full_mouth_let_out with hpunch
ms "The next load was no less than the first,{w} and from the pressure it splashed out and began to flow down the penis and balls in thick streams."
play sound ["SWFSlosh5.wav", "SDTGag2.wav", "SWFSlosh4.wav", "SWFSlosh4.wav", "SDTGag10.wav", "SWFSlosh5.wav", "SWFSlosh4.wav","SWFSlosh5.wav", "SDTGag6.wav"]
scene bg pov_face_fuck_mascara_tears_pressed_cum_full_mouth_let_out_cum_from_nose_choking with hpunch
ms "The third load out through my nose, making it impossible for me to breathe normally."
ms "Tears flowed from my eyes."
ms "I patted Bob's hands and he immediately let me go."
ms "I pulled away, swallowed and took a deep breath."
scene bg pov_leaned_back_facial_handjob_cum
ms "Bob's scent and remnants of his sperm were still in my mouth"
play sound "SWFSlosh4.wav"
ms "Bob continued to cum all over my hands."
play sound "SWFSlosh5.wav"
ms "Load after load. I've never seen so much sperm."
ms "It felt like a horse came on me."
jump mila_bob_handjob_continue

label mila_dom_hj_bob:
ms "The feeling of power over Bob awakened something perverted in me."
hide screen nts_stats_overlay
scene bg pov_handjob_bigger_cock_smug_dom
ms "Lately, I've started to feel like I can control Paul when I hold his dick."
ms "And the same feeling arose when I took Bob by the penis."
ms "A big, strong man lies in front of me and completely submits to my will."
ms "He is ready to do anything for me."
ms "He looked like a small animal"
ms "Scared. {w} And excited."
scene bg pov_handjob_bigger_cock_smug_smirk
ms "A smile crept onto my lips."
m "Put your hands behind your head."
ms "I was amazed at how low and powerful my voice sounded."
ms "I wasn't even surprised when Bob obeyed my command without question."
ms "I wanted to tease Bob.{w} Force him to bow before me."
scene bg pov_handjob_bigger_cock_open_mouth_saliva_flow
ms "I stuck out my tongue and showed the inside of my mouth."
ms "A stream of saliva flowed from the tongue and landed on the head of the penis."
ms "I rubbed it gently with my fingers."
scene bg pov_handjob_bigger_cock_smug_smirk_wet_cock
m "Do you want this tongue to touch your dick?"
bob "YES!"
ms "Bob practically shouted it."
scene bg pov_handjob_bigger_cock_giggle_laugh_wet_cock
m "Ahahaha"
scene bg pov_handjob_bigger_cock_smug_smirk_wet_cock
m "Good boy."
m "To do this, you need to listen to me, understand?"
ms "Bob nodded hastily."
m "Good boy."
m "Ask your mistress."
bob "P-please..."
m "Please what?"
bob "Blow me, mistress!"
scene bg pov_handjob_bigger_cock_frown_wet_cock
m "..."
m "I didn't say anything about giving you a blowjob."
m "I said this tongue will touch your dick."
bob "Sorry madam!"
ms "Bob extended his arms and waved them in front of him apologetically."
m "Hands behind head!"
ms "Bob hastily followed my command."
scene bg pov_handjob_bigger_cock_smug_smirk_wet_cock
m "Good boy"
ms "Crap.{w} I like this power."
m "Let's play a game."
bob "A game?"
m "Yes.{w} I'll start doing this."
stop sound
ms "I leaned lower.{w} The heavy musky smell of his cock filled my nose."
ms "But I was already excited enough to not pay attention to it."
scene bg from_side_licking_balls_handjob_closed_eyes
play sound "moans_suck.wav"
ms "I stuck out my tongue and licked his balls, salty from sweat while intensifying the movement with my hand."
bob "Oh God..."
scene bg from_side_handjob_open_eyes_giggle
play sound "chuckle.wav"
ms "I chuckled."
m "If you can hold it without cumming for a minute, then so be it. I'll blow you."
ms "Bob opened his eyes wide and looked at me in disbelief."
scene bg from_side_licking_balls_handjob_open_eyes
play sound "moans_suck.wav" loop
ms "I licked him again."
m "Let's start then."
scene bg from_side_sucking_balls_handjob_open_eyes
ms "I sucked his balls into my mouth and continued to jerk his penis, which seemed to become even bigger."
bob "Urgh..."
ms "Bob closed his eyes and bit his lip."
scene bg from_side_handjob_open_eyes_piercing_eyes
m "Open your eyes and look at me, Bob."
m "It's not fair to look away."
scene bg from_side_licking_shaft_open_eyes
ms "Feeling his gaze, I smiled and ran my wet tongue along the entire length of the shaft."
ms "I didn't even know if I wanted him to lose..."
ms "Or I want to lose myself..."
ms "I wonder what it's like...{w} To feel this huge bolt in your mouth."
ms "I tilted my head and wrapped my lips around the shaft of his penis."
bob "Mmm..."
ms "I felt that Bob was already on the verge."
ms "And soon he will cover me with his sperm."
ms "And I will never be able to wash myself of this."
ms "I can no longer stop being who I just became."
ms "I'm a slut."
ms "And sluts...{w} Sluts love sperm."
scene bg from_side_licking_shaft_open_eyes
ms "I ran my tongue along the entire shaft and,{w} feeling Bob's penis tense from my touches,{w} I slowly opened my mouth..."
scene bg pov_sucking_cockhead_piercing_eyes
play sound "moan_suck2.wav"
ms "And let his dick into my wet mouth."
bob "Oh God!"
ms "Bob started cumming almost immediately."
ms "I wanted to gently suck his sperm and release it out."
ms "That was my plan...{w} but..."
scene bg pov_sucking_cockhead_piercing_eyes_cum_first
play sound "SWFSlosh4.wav"
ms "There was so much sperm that it instantly filled my mouth and began to flow down to my hand and down to his balls."
play sound "SWFSlosh4.wav"
ms "And damn...{w} It was so hot..."
scene bg pov_sucking_cockhead_piercing_eyes_cum_second
play sound "SWFSlosh5.wav"
ms "Feeling hot streams of another man's sperm fill my mouth."
ms "To feel that he is in my power."
ms "That he's mine."
play sound "SWFSlosh4.wav"
scene bg pov_sucking_cockhead_piercing_eyes_cum_smile
ms "Without letting his dick out of my mouth, I looked at Bob and smiled."
ms "Good boy."
ms "Bob didn't stop cumming. He continued to pump my mouth with cum."
play sound "SWFSlosh5.wav"
scene bg pov_leaned_back_facial_handjob_cum_smile
ms "I released his dick from my mouth and leaned back, tired."

label mila_bob_handjob_continue:
ms "It covered my hands and slowly flowed down the shaft and to those hairy balls."
ms "After a few seconds, the spasms ended and everything became quiet."
ms "Bob covered his face with his hands and was silent."
bob "I...{w} I'm sorry."
scene bg pov_leaned_back_facial_handjob_cum_smile
ms "I milked the remaining sperm from his cock and asked interestedly."
m "For what?{w} For cumming all over me?"
ms "This recent event woke a real slut inside me. {w}And I didn't feel awkward at all. {w}Quite the opposite. {w}I felt proud and powerful"
bob "..."
bob "Yes…"
bob "At first...{w} I thought I was still dreaming... {w}And then... {w}I just couldn't stop"
bob "Sorry! I'm so sorry..."
scene pov_leaned_back_facial_handjob_cum_looking_aside_doubtful
m "..."
ms "I didn't want to accept his apology"
ms "I felt like if I accepted it, it meant that I agreed that he did something wrong."
ms "And he didn't."
scene bg pov_leaned_back_facial_handjob_cum_smile
m "It wasn't a dream bob.{w} For both of us.{w} Don't you want to see what it looks like?"
ms "Bob froze."
scene pov_leaned_back_facial_handjob_cum_smirk
m "Your thick sperm flows down my fingers.{w} I gently massage your huge dick until it gradually becomes softer..."
bob "..."
scene pov_leaned_back_facial_handjob_cum_looking_aside_doubtful
m "No?"
ms "Bob removed his hands from his face and looked at my face first, but his eyes still fell on to penis."
scene waving_hand_with_cum_facial_grin_teasing
ms "I waved at him with my fingers stained with his sperm."
ms "He looked at it silently, as if he was spellbound."
ms "..."
scene waving_hand_with_cum_facial_demanding
m "You know what?"
m "Take a picture of me."
bob "... {w}WHAT?!"
m "I said grab your phone{w} and make a picture of me."
bob "W-why? {w}A picture? It's dangerous!"
scene waving_hand_with_cum_facial_tilted_head_doubts
m "Is it?{w} Will you show it to your shitty colleagues?{w} Or post it somewhere?"
bob "..."
scene waving_hand_with_cum_facial_demanding
m "No. {w}You won't."
m "You are not that kind of person."
ms "I gently stroked his penis."
ms "..."
scene waving_hand_with_cum_facial_shy_looking_aside
m "That's why I can do... {w}risky stuff... {w}with you {w}and for you."
m "..."
bob "..."
scene waving_hand_with_cum_facial_shy
m "I am not a saint, you know? {w}Girls have some lewd thoughts too..."
m "It's just..."
scene waving_hand_with_cum_facial_shy_looking_aside
m "Most men are just horny monkeys... {w}If you give them even a little tease... {w} Well..."
m "..."
bob "..."
scene waving_hand_with_cum_facial_grin_teasing
m "Nevermind... {w}Come on, make a picture already,{w} go on"
play sound "shot.mp3"
ms "..."
bob "Thank you..."
m "Ahah.{w} My pleasure."
m "And guess what?"
ms "Bob looked at me questioningly."
m "Send me a copy too."
bob "..."
scene waving_hand_with_cum_facial_teasing
m "When I masturbate this evening, I will look at it."
bob "!!!"
m "Yes, girls do that too."
scene waving_hand_with_cum_facial_shy_looking_aside
m "And your schlong and this whole experience..."
scene waving_hand_with_cum_facial_shy
m "It was extremely sexy."
bob "..."
ms "Bob opened and closed his mouth, but did not answer."
scene waving_hand_with_cum_facial_demanding
m "Okay, I need to wash my hands."
m "Lunch is on the table."
m "And have a nice day at work."
ms "I blew him a kiss but forgot that my hand was covered in his cum."
scene mila_licking_cum_from_fingers
ms "I stopped for a moment, and then licked my palm right in front of him"
bob "..."
ms "His cock become hard again"
scene mila_licking_cum_from_fingers_smile
ms "Hehe.{w} I'll let you deal with that yourself"
ms "Damn, I'm such a slut..."
"..."
scene black
"..."
if _in_replay:
    return



scene bg paul_and_bob_at_bar with fade
play music "bar.mp3"
p "..."
bob "..."
p "..."
bob "..."
p "Hmm..."
ps "Bob picked up his beer and took a silent sip."
ps "We sat like this for several minutes.{w} I had managed to drink a glass of whiskey and was sipping a second one."
ps "Despite the fact that smoking was prohibited inside, there was a strong cigarette smell in the air."
ps "Behind us, several men were arguing about politics.{w} Their loud voices, clinking glasses and bottles and laughter enveloped us in a curtain of noise."
ps "Making our meeting weirdly intimate."
ps "But the conversation still could not begin."
p "..."
ps "Bob wrote to me this afternoon and asked to meet. I invited him to a bar near my house."
ps "But after the greeting, we just sipped our drinks in silence, too embarrassed to speak."
p "Haaaa..."
ps "I exhaled tiredly."
ps "It feels like if I don't start a conversation, Bob will just get drunk and fall asleep right at the bar"
p "So what did you want to talk about?"
ps "Bob shuddered and looked at me in fear."
ps "Sweat covered his forehead and his pupils darted from side to side."
ps "But even after a minute he still didn't answer."
ps "I decided to help him."
p "If it's about what happened this morning, then I already know."
p "Mila told me everything."
ps "Bob looked at me in surprise."
if dom >= mila_dom:
    p "In general, it would be more correct to say that I told her to do it."
if mila_dom > dom:
    p "I don't mind what she does. Quite the opposite."
bob "Erm..."
ps "Bob scratched the top of his head, puzzled."
ps "I exhaled and leaned my elbows on the table, twirling the glass of whiskey in my hands."
p "Hard to understand right?"
ps "Bob just nodded in response."
p "..."
p "You know..."
p "We've been together for so long, that..."
p "No, that's not what I want to say..."
ps "I twirled the glass in my hand and waited for the noise behind me to get louder."
ps "As if afraid that someone else would hear my words."
p "When you are in love, you want the object of your feelings to be perfect."
p "In everything."
p "And that's how you see her."
p "Ideal."
p "Gymnast,{w} strong-willed and beautiful,{w} smart and kind..."
p "Virgin..."
ps "Bob smiled sadly."
bob "The only thing that would be enough for me is that she loves me back."
ps "I nodded."
p "For me too."
p "But that's what makes you see her in a different light."
p "You deceive yourself because you want to be deceived."
p "But in reality she will be perfect, simply by the fact that she loves you"
p "And you love her."
bob "That's what I don't understand why..."
ps "I raised my hand in a stopping gesture."
p "Let me finish."
bob "..."
bob "Bob immediately fell silent."
p "At first I saw her as a timid and obedient girl."
p "And I liked it."
p "And knowing that she put this mask on herself."
p "Because that's what I was waiting for. What I and everyone around us want to see."
p "This is how a connection is formed.{w} Your loyalty to each other and determination to change yourself to meet your partner's expectations bind you."
p "But if you think about it...{w} You change. And what you like changes with you."
ps "I raised my glass and took a sip of whiskey and held the scalding liquid on my tongue."
ps "Swallowing and exhaling, I noticed a faint oak aroma."
p "When I was 20, I hated whiskey. I drank it only diluted with cola.{w} But with age... My tastes have changed."
bob "..."
p "And it's the same here.{w} I liked the fact that Mila is a timid and obedient girl.{w} My girl."
p "But I only liked it because I was insecure."
p "I wasn't sure about her."
p "But over time...{w} it becomes tediously boring."
bob "..."
p "Of course, we talked...{w} We tried different things."
p "But our intimate life becomes insipid."
p "And my fantasies...{w} Strife somewhere far away."
p "It's like...{w} You watch porn, jerk off to other women, depraved women."
p "And you even imagine yourself with them."
p "But your connection with your beloved one...{w} It loses tension."
p "It begins to dangle between you, like a chain that hinders your movements."
p "And somewhere at this moment your masks begin to crack."
p "And you wonder - do you love her, or her mask?"
p "You realize that you have a choice."
p "You can go fulfill your fantasies with someone else."
p "And you have to maintain the appearance of former feelings.{w} Lie to her.{w} And to yourself."
p "You get used to pretending."
p "And that will make your love platonic.{w} Just a pretense"
p "Or you will destroy your relationship."
p "But also you can try...{w} to do the same thing you did at the very beginning."
p "Talk.{w} Take off your masks, expose your weaknesses, appear vulnerable in front of each other."
p "To let yourself to be loved as is.{w} To love the real weak and ugly human inside.{w} To compare expectations."
p "We take off our masks to put on new ones."
p "Those that better suit the desires of the partner."
p "Those that suit the current situation in the best way."
ps "I looked at Bob."
p "And sometimes the Slut mask suits her best."
ps "Bob didn't take his eyes off his bottle, as if he was afraid to look at me."
bob "..."
bob "It's wrong..."
ps "I chuckled."
p "People make the rules."
p "Rules about what is wrong and what is right."
p "What you can and cannot do."
p "Rules about what is considered cheating."
p "Rules on what is considered betrayal."
bob "..."
p "I like these changes."
p "They breathed life into our relationship."
p "They gave me back the feeling...{w} of freshness...{w}and passion."
p "I wonder how far can we go?"
p "I'm jealous,{w} yes.{w} It hurts,{w} damn right."
p "But at the same time...{w} This new Mila turns me on like hell."
bob "..."
p "..."
bob "..."
bob "Your life is so perfect that I want to kill you and crawl into your skin."
p "..."
ps "I tried to understand what I heard for some time, not knowing how to react."
p "I... I'm not sure you can do that."
ps "Bob nodded and took a sip of his beer."
bob "I know."
bob "I'm too fat."
p "..."
p "This is not exactly what I meant..."
ps "I still didn't understand whether he was joking or being serious."
bob "..."
p "..."
ps "Bob cleared his throat."
bob "Hmm..."
bob "So it means... You don't mind that I... That we... That Mila..."
p "Yeah. I don't mind."
bob "..."
p "..."
bob "What else can I do to her?"
p "..."
ps "I frowned. I didn't like what he said."
p "What do you mean?"
p "She's human. She is not a thing that you can somehow \"use\"."
bob "I don't mean it that way..."
bob "I mean..."
bob "Is there a limit?"
p "..."
ps "I swallowed."
ps "A drop of cold sweat ran down my back."
ps "I was scared by my thoughts, but at the same time I felt relieved."
ps "It was as if the awareness of my desire freed me."
p "Anything she wants."
bob "..."
p "..."
ps "We sat for some time in almost silence."
ps "I finished my whiskey, patted him on the back goodbye, and went home."
ps "Bob just nodded in response and ordered himself another beer."
ps "..."
stop music




label a125:
scene bg apartments with fade
show mila robe_puzzled_frown at right
ms "..."
ms "..."
show mila robe_puzzled:
    xzoom -1
    easein 0.7 xpos 0.25
"tap tap tap"
ms "..."
ms "..."
show mila robe_puzzled_frown:
    easein 0.7 xpos 0.95
"tap tap tap"
ms "..."
ms "..."
show mila robe_irritated_open_mouth:
    easein 0.7 xpos 0.55
"tap tap"
m "Haaaaa..."
ms "..."
ms "After the blowjob, I took a shower. Then it finally hit me, what had actualy happened just now."
ms "Or more precisely, I felt it even earlier - the moment I took off the suit. {w}It was so tight, like a second skin."
ms "And as soon as I freed myself from it...{w} I became myself again."
show mila robe_blush_shy_looking_aside
ms "Mila. Paul's wife. The wife who sucked off her neighbor while her husband was getting ready for work..."
ms "The memories washed over me that where cold and heat simultaneously."
ms "Heat from the events flashing before my eyes, awakening lust with their perversity."
ms "Cold from fear of the consequences."
ms "What will Paul say?{w} I texted him, and told what I did..."
ms "But all he answered was “we'll talk in the evening”..."
ms "..."
show mila robe_irritated_open_mouth:
    easein 0.7 xpos 0.25
"tap tap tap"
ms "..."
show mila robe_iritated_atatata
ms "I hate it when he does that..."
ms "Is it that hard to say what you think right away?"
ms "Is it necessary to make me worry?"
ms "..."
show mila robe_irritated_open_mouth:
    easein 0.7 xpos 0.95
"tap tap tap"
ms "..."
show mila robe_irritated_open_mouth:
    easein 0.7 xpos 0.55
"tap tap tap"
ms "..."
show mila robe_puzzled
ms "Maybe I should meet him in some special way?"
show mila robe_blush_smirk
ms "To ease the tension...{w} Not because I want it myself..."
show screen nts_stats_overlay
menu:
    "How should I greet Paul when he comes home?"
    "With obedience (Mila's submissiveness + 1)":
        $ dom += 1
        jump netorase_greetings_mila_sub
    "Take control (Mila's dominance + 1)":
        $ mila_dom += 1
        jump netorase_greetings_mila_dom

label netorase_greetings_mila_sub:
show mila robe_shhhh_finger
ms "He will probably like it if I meet him as a slave..."
hide screen nts_stats_overlay
show mila robe_blush_smirk
ms "Slave whore..."
ms "..."
ms "Hehe"
ms "The door lock clicked."
ms "I hastily knelt down and assumed a humble pose."
scene mila_kneeling_robe
ms "Paul walked into the apartment and froze for a moment."
p "..."
ms "I was afraid to look up."
ms "Paul came closer and stood in front of me."
p "..."
m "..."
p "I like this greeting."
scene mila_kneeling_robe_light_smile
ms "My chest felt warm"
m "I'm glad..."
p "I was just having drinks with Bob by the way."
scene mila_kneeling_robe_surprised
ms "I raised my head in surprise."
p "He called me himself."
p "Could you..."
ms "Paul interrupt himself and lowered his voice"
p "Get up and pour me some tea. {w}We need to talk.{w} And also I think I drank too much."
jump netorase_greetings_continue
label netorase_greetings_mila_dom:
show mila robe_smile_awkward_angry
ms "An evil grin crept onto my face"
hide screen nts_stats_overlay
ms "Why should I bother?{w} He was the one who made me worry."
ms "Now it's his turn."
ms "The door lock clicked."
show mila robe_curious
ms "I crossed my arms over my chest and took a threatening pose"
ms "Paul noticed me and frowned"
show paul suit_open_mouth_neutral at left
p "Babe?"
p "Is there something wrong?"
m "..."
ms "I continued to silently glare at him."
ms "Paul's eyes darted."
show paul suit_sad
p "Em..."
p "Sorry for being late?.."
ms "He looked at me hopefully."
p "No, that's not the problem."
m "..."
ms "To be honest, even I don't know what the problem is.{w} But he should struggle a bit too.{w} I did after all"
ms "..."
ms "I just want to tease him."
show paul suit_open_mouth_blush
p "Hmm...{w} I met Bob...{w} We had a drink."
show mila robe_blush_shy_looking_aside
m "What?.."
ms "All my feigned self-confidence disappeared."
ms "I swallowed."
m "Come on, tell me."
ms "I pulled Paul into the kitchen."
label netorase_greetings_continue:
scene bg kitchen
ms "..."
ms "Paul told me about his conversation with Bob."
ms "We were both silent for some time."
ms "Paul drank a cup of tea and it sobered him up a bit"
m "..."
show mila robe_puzzled at center
m "So what do you think? How does he...{w} Feel about all this?"
ms "Paul looked at me and shrugged."
show paul suit_open_mouth_neutral at left
p "It's hard to say. It seems to me that he is puzzled, and he is trying to understand what is stronger - his conscience or lust."
ms "I nodded thoughtfully, but didn't know what to say."
ms "My head was filled with a strange cocktail of thoughts and desires."
ms "But one feeling stood out the most.{w} Anxiety."
ms "It's not like I didn't want to know about what Bob think..."
ms "I just wanted to know what Paul thought about what happened this morning more then anything else."
ms "I wanted to see his reaction. Feel our connection."
ms "And judging by his thoughtfully worried face, Paul was thinking the same thing."
show paul suit_blush_looking_aside
p "..."
p "Hmm..."
ms "Paul cleared his throat."
show paul suit_open_mouth_blush
p "So...{w} About what happened this morning..."
ms "I felt like a coiled-up spring."
ms "Paul and I's connection tightened again, painfully draining the confidence from me."
show mila robe_sad
ms "It seemed like I was starting to physically feel this tension.{w} And it made my body crave Paul's attention more than ever before."
ms "I wanted to snuggle up to him,{w} smell the orange-cinnamon scent of his cologne.{w} Feel the elasticity of his body.{w} And its warmth."
ms "I wanted to be sure... {w}That he still loved me.{w} Even after what I did.{w} Even knowing what I will do."
show paul suit_sad
p "I...{w} I think that this thing, that happened in the morning...{w} That's not what I want..."
show mila robe_sad_tears
ms "From Paul's first words and mood, I already knew what he wanted to say."
ms "That this is exactly what I was afraid of the most..."
ms "My hopes were shattered."
ms "My pride and confidence evaporated.{w} I was ready to do anything to win his affection back."
ms "It seemed like my whole life was flashing before my eyes.{w} My mind gave me hundreds of options of what I could say,{w} what I should say."
ms "But I didn't like any of them."
ms "Resentment and fear hurt me almost physically.{w} Tears gathered up in my eyes.{w} And no matter how hard I tried - I couldn't swallow a lump in my throat"
ms "With trembling hands, I took Paul's hand and touched it with my lips."
scene mila_kiss_pauls_hand
p "..."
ms "A moment later I felt a gentle touch on my head."
ms "I didn't immediately dare to raise my head, but when I finally did, I saw Paul looking at me in surprise."
scene bg kitchen
show paul suit_open_mouth_neutral at left
p "..."
show mila robe_sad_tears at center
p "What are you doing?"
ms "I couldn't say a word and just closed my eyes and shook my head."
ms "I hope he won't leave me..."
ms "I can't imagine my life without him..."
m "..."
p "..."
p "Well... What I meant was, that I don't like that things you do is hidden..."
ms "I felt his nervousness. Paul made a pause, trying to gather up his thoughts"
p "I mean...{w} I like when you tell me what you did...{w} But,{w} I want to see it too..."
if dom >= mila_dom:
    show paul suit_smirk
    p "I want to tell you what to do. I want to train and guide you on how to become the ideal slut for me..."
    ms "Paul looked at me confidently"
    ms "His voice sounded in this commanding manner that has been making me shiver lately."
    ms "I looked down and tried to calm my racing heart."
    show mila robe_worried_open_mouth_wait
    m "..."
    ms "I wanted to feel his power over me."
    ms "I wanted to feel his desire and passion."
    ms "When I submit to his perverted desires, I feel like I am plunging into the depths of his consciousness."
    ms "I am adjusting to his requirements, guessing what he wants."
    ms "I saw his vulnerable side.{w} I drawn to it.{w} I was absorbed by it."
    ms "And I can hurt him by reacting differently than he expected."
    ms "He can't force me to do anything.{w} I obey his orders only because I want to."
    ms "The possibility of refusal is threatening him.{w} And it gives me power."
    ms "So who is in charge?{w} The one who give orders?{w} Or the one who obeys?"
    m "..."
    m "What... {w}What do you want me to do?..{w} Master..."
    ms "It was so easy to say.{w} This word fit perfectly, as if it should be there."
    ms "Master...{w} Even thinking about it made me shiver."
    ms "Having said this, it was as if I had opened the door to the hidden corners of my mind."
    ms "The parts of me that I try control with all my might,{w} try to hold it and hide."
    ms "And what was locked inside began to overcome me.{w} It captured my consciousness."
    ms "It became a part of me.{w} Each next perverted step opened this door further."
    ms "And I was no longer sure that I would ever be able to close it."
    ms "Not to mention,{w} that I don't want to."
    show paul suit_grin
    p "..."
    ms "Paul liked how I called him and grinned."
    p "I think you should talk to Bob."
    m "..."
    show mila robe_puzzled_frown
    m "But... You said that you want to see..."
    show paul suit_smirk
    p "Yeah.{w} But I think Bob is not ready for this...{w} Experience."
    ms "I nodded."
    p "Therefore, your task is to lead him to this."
    m "..."
    show mila robe_blush_smirk
    m "Lead him, huh"
    m "But...{w} How can I do this?"
    ms "Paul shrugged."
    p "Don't know. Think of something. Offer something in return, for example."
    show mila robe_think
    m "..."
    m "..."
    show mila robe_shhhh_finger
    m "Fine..."
    p "..."
    ms "The muffled sound of a door opening was heard from behind the wall. Bob came home."
    ms "Paul and I looked at each other."
    m "..."
    p "..."
    show mila robe_worried_open_mouth_wait
    m "I should probably go and talk to him, right?"
    p "Yes."
    ms "I looked at myself and smoothed out the non-existent wrinkles on my robe."
    m "Do I look okay?"
    p "..."
    p "No.{w} You look hot."
    show mila robe_worried_open_mouth_wait
    m "..."
    m "Thank you."
    scene bg door
    ms "I walked hesitantly towards the exit."
    ms "Already at the door Paul called out to me."
    show mila robe_from_behind_looking
    ms "I turned around."
    p "When you return, a small surprise will await you."
    ms "The tone of his voice left no doubt about the nature of the surprise he was talking about."
    ms "I felt hot."
    ms "I wonder what he came up with?"
    show mila robe_from_behind_not_looking
    ms "I swallowed and walked out into the coolness of the corridor."
    jump netorase_talking_after_blowjob_continue

show paul suit_smirk
p "I want to look at you, when you are in your...{w} Naughty mode.{w} With someone else..."
ms "Paul fell silent, embarrassed."
ms "I waited a bit, giving him time to collect his thoughts."
ms "But with every passing moment I grew impatient"
ms "And the desire to tease him."
show mila robe_blush_smirk
m "So you would like to see how my little mouth is sucking another another man's dick?"
ms "Paul didn't answer."
ms "I approached him and lifted his face by the chin."
scene mila_dominant_face
ms "His embarrassed face awakened something in me."
ms "Something aggressive, but not evil."
ms "The desire to control...{w} To subjugate...{w} To tease..."
ms "I don't know how to describe this feeling."
ms "It's something elusive.{w} The desire to inflict pain for the sake of pleasure."
ms "The pain can vary.{w} Not necessarily physical."
ms "I want to feel his humility.{w} His desire to follow my whims."
ms "His enjoyment and admiration of my most disgusting sides."
m "What a bad boy..."
ms "The right words came out of nowhere.{w} I just knew what I should say.{w} Because I said everything I wanted. Without any restrain."
ms "Having said this, it was as if I had opened the door to the hidden corners of my mind."
ms "The parts that I try not to let out."
ms "And what was locked inside began to overcome me. Capture my consciousness."
ms "It became a part of me. Each next perverted step opened this door further."
ms "And I was no longer sure that I would ever be able to close it."
ms "Not to mention that I don't want to."
ms "I want to become different.{w} Become my true self. {w} Without ignoring, without denying those parts of me that are locked inside."
ms "Locked under the morality, education, traditions... Common sense."
ms "I want Paul to see this part of me.{w} I want him to love it.{w} I want him to love me no matter what."
ms "Despite the most disgusting things I will do.{w} To him.{w} To us."
m "..."
ms "The muffled sound of a door opening was heard from behind the wall. Bob came home."
ms "I wanted to play with Paul some more, but this sound gave me another idea"
scene bg kitchen with fade
show mila robe_blush_smirk
m "Take off your clothes and wait for me here. I need to go talk to my lover."
show paul suit_blush_looking_aside at left
ms "Paul turned red, either from embarrassment or anger."
ms "I just grinned at his reaction."
ms "But then his face brightened, as if he had remembered something."
ms "A playful grin crept onto his face."
show paul suit_smirk
p "Okay, mam..."
show mila robe_puzzled_frown
ms "I frowned."
m "Is there something wrong?"
p "No... I just remembered something. I'll show you when you get back."
m "..."
ms "I was bursting with curiosity, but I decided that a little surprise wouldn't make it worse."
ms "So I headed towards the door."
scene bg door
p "Have fun."
show mila robe_from_behind_not_looking
ms "I froze for a second, for some reason frightened by the mocking note in his voice."
ms "But not having figured out what to answer, I just thanked him and went out into the coolness of the corridor."

label netorase_talking_after_blowjob_continue:
scene bg bobs_apartments_clean with fade
ms "Even though I had a key, I felt it was right to knock rather than open the door myself."
ms "Bob opened it almost immediately."
ms "The persistent smell of alcohol hit my nose, and his huge erect penis caught my eye."
show bob nude_flaccid_drunk at right:
    ypos 1.05
ms "Bob was completely naked."
ms "He grabbed my hand and pulled me inside."
show mila robe_holding_hand_open_mouth_blush2 at left
m "W-what? W-wait!"
scene bob_kiss_mila_forced
ms "The door to the apartment slammed behind me. Bob pressed me to the door and forcefully kissed me."
ms "His hands began to greedily grope my body."
ms "His sudden pressure and impudent behavior angered me."
ms "I rested my elbows on the door and pushed him away from me with all my might."
ms "I'm not sure my efforts moved him even an inch."
ms "But, sensing my resistance, he pulled away in surprise and looked at me with a gaze clouded by alcohol."
scene bg bobs_apartments_clean
show mila robe_iritated_atatata at left
m "What the hell, Bob!"
show bob nude_flaccid_drunk at right:
    ypos 1.05
ms "He frowned and took a step back."
bob "Did I do something... Hic... wrong?"
m "...."
m "Did you do something wrong? What the heck?"
ms "For some reason his behavior scared me. I immediately lost control over what was happening."
ms "His tongue burst into my mouth so quickly and unexpectedly that I felt raped."
ms "My body became sensitive, but not in a vulgar sense.{w} Quite the opposite.{w} It seemed to me that everything was covered with needles."
ms "Any touch caused irritation... And fear."
show mila robe_irritated_open_mouth
m "..."
bob "P-Paul said...{w} Hic...{w} That I can do whatever...{w} Hic...{w} I want..."
show mila robe_smile_awkward_angry
m "Oooh, really?{w} That's so sweet!{w} But shouldn't you two, I don't know, ask me first?"
bob "..."
ms "Bob frowned."
show bob nude_flaccid_frown
bob "B-but... You're the one..."
ms "I interrupted his inarticulate muttering."
m "Yes. I started it myself. But that doesn't mean you can do whatever you want with me, just because \"Paul said it\""
ms "Bob hunched over and seemed to become smaller."
show bob nude_flaccid_sad
bob "I see...{w} Hic..."
ms "His voice sounded not even sad, but indifferent.{w} As if he knew this would happen.{w} He turned away from me and walked towards the bedroom."
show bob nude_from_behind
show mila robe_worried_open_mouth_wait
ms "His hunched figure evoked nothing but pity."
ms "The further he moved away, the calmer and safer I felt."
ms "And the more it became clear to me that I was too harsh."
m "Wait..."
show bob nude_from_behind_looking_back_sad
ms "Bob stopped and turned back.{w} His penis hung like a shapeless sausage between his legs.{w} And I had to put an effort not to look down."
bob "What?{w} Hic..."
ms "His voice sounded dry, almost harsh."
m "..."
ms "I tried to find words, but I still couldn't formulate what I wanted to say."
m "I... I feel sorry..."
show bob nude_flaccid_angry
ms "Bob didn't let me finish."
ms "His eyes flashed with anger."
bob "You are sorry? Don't pity me!"
ms "I was taken aback by his sudden aggression and wanted to step back, but I realized my back was still resting against the door."
bob "You are forever sorry.{w} You all always talk to me out of pity."
bob "It's like you're doing me a favor."
bob "I've never asked to be saved."
show mila robe_puzzled_frown
m "I don't..."
show bob nude_flaccid_sad
bob "Stop it already.{w}That's enough."
show mila robe_sad
m "..."
ms "I didn't know how to answer.{w} Anger surged in Bob so much that he stopped hiccuping and seemed to sober up."
bob "Why the hell is everyone around doing whatever they want and not giving a damn about my opinion?"
bob "Why do you always decide for me?"
bob "Why should I always think about what others want?"
bob "How about what I want?"
show mila robe_worried_open_mouth_wait
m "..."
ms "His voice hit my exposed nerves like a ringing hammer.{w} I lowered my head, fighting shame."
bob "You don't give me the right to leave,{w} you begin to manipulate me and push me in the direction that fits you."
bob "But you're just indulging your whims, right?"
bob "You don't give a fuck about me.{w} You don't give a fuck about my thoughts and feelings."
m "..."
ms "Resentment burned in my throat, my eyes watered and itched. I could hardly restrain myself from bursting into tears."
ms "Because I knew.{w} He was right."
m "..."
bob "Enough.{w} I'm done with it."
show mila robe_from_behind_not_looking
ms "I couldn't stand it anymore.{w} I turned my back to leave and grabbed the door handle."
ms "My guts demanded to quickly leave this room.{w} To run away."
ms "Nobody wants to be the bad guy.{w} And I already found hundreds of excuses for myself."
ms "That it was for Bob's benefit.{w} That he definitely enjoyed it.{w} That he could refuse it any time."
ms "But I knew it was all a lie."
ms "And that made me feel even more offended.{w} Even more hurt."
show mila robe_from_behind_looking
m "..."
ms "If I leave now, I will only prove to him that he is right."
ms "What will he do after this?"
m "..."
ms "What will I do and how will I feel afterwards? Can I pretend that nothing happened?"
ms "...{w} No.{w} Of course not."
m "..."
show mila robe_puzzled_frown
ms "I let go of the handle and turned back, to face Bob."
m "I... I'm sorry."
ms "My voice trembled and sounded quiet and weak."
ms "Bob sighed."
bob "I don't need your apology.{w} I want to be left alone."
m "..."
show mila robe_puzzled
m "It seemed to me that just recently you wanted something different..."
bob "Are you going to pretend that you care again?"
m "..."
show mila robe_smile_awkward_angry
m "..."
ms "Wait a minute... At what point did this become my tribunal?"
ms "I shouldn't feel guilty for being scared."
ms "Bob's words reflected his feelings.{w} Simple and honest, like a teenager's."
ms "He still saw the world in black and white.{w} And he refused to grow up."
ms "Refused to see anything less than perfect.{w} Something contradictory.{w} Something human like."
ms "There are no halftones in his world.{w} He protects this world, cherishes it.{w} Because it protects him from the disgusting reality."
ms "A reality in which everything is painted dark gray."
ms "I couldn't help myself.{w} I felt sorry for him.{w} Even though he didn't like it."
ms "But this is stupid.{w} You can't judge someone for their feelings.{w} We cannot choose what we feel.{w} We just feel."
ms "And all we do is trying to find a reasonable reason why."
show mila robe_worried_open_mouth_wait
m "Bob..."
show bob nude_flaccid_crossed_arms
ms "He crossed his arms over his chest and turned away."
ms "Like a child..."
show mila robe_irritated_open_mouth
m "I did not mean to offend you.{w} But you didn't see me as a person at all at that moment.{w} You wanted to use me like a thing."
ms "Not that I'm against it...{w} But this requires a different mood."
ms "I decided not to tell him this...{w} For now."
bob "But you..."
m "Yes."
ms "I interrupted him again."
m "Yes, I did what I wanted.{w} But I don't remember that at least once I forced you to do something."
ms "Bob looked away and winced.{w} He probably saw it differently."
ms "I sighed."
m "Listen, I'm not against displays of...{w} Tenderness from you."
show bob nude_bigger_penis_crossed_arms_shock
ms "Bob glared at me. His penis twitched and began to fill with blood."
ms "I could hardly restrain myself from staring at it."
m "Everything just has its place, time, and mood..."
bob "..."
show bob nude_bigger_penis_crossed_arms_frown
bob "You and only you will decide all of it, apparently?"
if mila_dom >= dom:
    show mila robe_blush_smirk
    m "And isn't that what you want?"
    bob "..."
    ms "Bob raised one eyebrow skeptically."
    m "..."
    ms "When did he become so cocky?"
    m "..."
    show mila robe_proud
    m "Okay, let's do it this way. We will exchange terms."
    jump netorase_talking_with_Bob_after_blowjob_continue

show mila robe_worried_open_mouth_wait
ms "I looked away."
ms "I didn't want to answer this question.{w} I didn't want to say it out loud."
ms "I was afraid that he would take my words incorrectly."
ms "I really don't want to decide anything.{w} I feel so comfortable when Paul tells me what to do."
ms "I don't want to be responsible for my choices."
ms "I don't want to be a good girl.{w} I want to be bad girl."
ms "Very bad girl."
ms "But at the same time, I don't want to feel like it's me..."
ms "I want to feel like I'm forced to do this...{w} That I'm controlled by someone else."
ms "But I can't say it out loud..."
m "..."
bob "I knew it."
ms "Bob sighed sadly."
m "No..."
ms "I somehow squeezed it out of myself.{w} I didn't want to talk about this topic.{w} I didn't want to admit it."
ms "But I'll have to."
ms "Because that's what Paul wants."
ms "The last thought gave me strength and confidence."
show mila robe_blush_smirk
ms "Yes.{w} Paul told me to talk to Bob.{w} This is his will.{w} I have to do it."
m "No Bob.{w} I won't be the only one who decides"
ms "I was finally able to say it more firmly.{w} Bob looked at me interestedly."
m "I want to offer you...{w} other conditions..."

label netorase_talking_with_Bob_after_blowjob_continue:
bob "Conditions?"
show mila robe_proud
m "Yes."
ms "Bob frowned in confusion."
m "Three conditions from me.{w} Three conditions from you."
bob "Conditions for what?"
ms "I swallowed the lump in my throat and tried to look as confident as I could."
m "Three conditions for doing it again."
bob "..."
m "..."
bob "Do it? Do what?"
ms "I pursed my lips in displeasure."
show mila robe_holding_hand_open_mouth_blush3_looking_aside
m "Don't make me say it out loud.{w} I'm uncomfortable too, damn it!{w} I've never done anything like this, what do you want from me?"
ms "Bob was somewhat taken aback by my rebuke and did not answer."
bob "..."
show mila robe_proud
m "Hmm..."
ms "I coughed into my fist, regaining my composure."
m "I want our... Relationship to have a positive impact on both of us."
m "Therefore, my first condition is that I want you to have some creative hobby."
ms "Bob immediately sank."
bob "What for?{w} I am a loser.{w} I tried drawing, sculpting, making games, writing songs - I'm terrible.{w} I will never become even decent."
ms "I just smiled warmly in response."
show mila robe_smile_open_mouth
m "Creativity is not about becoming better than others."
m "Creativity is about expressing yourself,{w} helping yourself and others understand what kind of person you are."
m "You can create things, even if no one will ever see it."
show bob nude_bigger_penis_crossed_arms_warm_smile
bob "..."
ms "Bob smiled for a second, but then frowned again."
show bob nude_bigger_penis_crossed_arms_frown
bob "Again!{w} You're doing it again!{w} I refused because I want to refuse.{w} I don't want to waste time on this."
show mila robe_curious
ms "I folded my arms over my chest."
m "First of all, you didn't refuse.{w} Secondly, this is my condition.{w} But you can put yours forward to make up for it.{w} Learn to negotiate, not refuse."
ms "Bob sighed."
bob "Why do you want me to have a hobby?"
ms "I shrugged and chuckled."
m "Just because.{w} This is what I want.{w} This is my whim.{w} You know, it is quite pleasant to want something and do something to achieve it."
ms "Bob lowered his eyes."
bob "Yes. It must be nice..."
ms "His voice sounded dull and lifeless."
m "..."
show mila robe_blush_smirk
m "So? What's your condition?"
bob "I don't have any. I don't want to think about it."
bob "Dreams are for those who are talented.{w} For people like me... It's hard to have dreams."
ms "Bob answered after a short pause.{w} But I didn't like his answer."
show mila robe_irritated_open_mouth
m "I didn't ask what you didn't want.{w} I asked what your condition would be?{w} What do you want, Bob?"
ms "Bob raised his hand and glared at me for a few seconds."
ms "I didn't look away and didn't even blink."
bob "I want you to take off your clothes."
ms "Out of the corner of my eye I noticed his huge penis swaying in the air"
ms "Hell, I don't mind taking my clothes off myself..."
ms "But I need to follow the rules.{w} Otherwise I'll lose control again.{w} And all this will turn into a disgusting experience where I will feel used and raped."
ms "I nodded slowly, keeping my eyes on Bob, as if afraid that if I lost sight of him for even a moment, he would rush at me."
m "Fine.{w} As soon as you fulfill my condition,{w} I will undress."
ms "Bob was surprised at first.{w} Then he brightened, and then frowned again."
bob "What do you mean? What do I need to do specifically?"
show mila robe_think
ms "His voice sounded intermittent, hoarse and low. He could hardly contain his excitement."
ms "And at the moment it was both frightening and exciting."
ms "I answered calmly, not showing my excitement, so as not to provoke him even more."
show mila robe_irritated_open_mouth
m "I will undress when you show me what you made with your own hands."
ms "Bob winced."
bob "No.{w} This won't work.{w} You can say I didn't put in enough effort or something like that.{w} How do I know if I've kept my side of the deal?"
ms "He said it clearly and firmly.{w} I realized that I was unlikely to be able to convince him and had already begun to come up with workarounds."
ms "But Bob beat me to it."
show bob nude_bigger_penis_crossed_arms_smirk
bob "I'll start drawing.{w} And you will pose for me.{w} Naked."
show mila robe_puzzled
ms "I swallowed."
ms "I felt like I couldn't refuse."
ms "So I nodded hesitantly."
m "Deal..."
bob "..."
bob "What's next?"
m "Erm..."
ms "I was somewhat taken aback by his pressure, but tried to pull myself together and look confident."
show mila robe_proud
m "Second condition..."
show mila robe_think
ms "It's a shame I didn't think about this in advance..."
ms "His dick was still swaying in the air, constantly attracting attention. I could clearly smell his musky scent."
ms "And it brought back memories of what happened this morning."
ms "My mouth filled with saliva. As if afraid that this monster would start ramming my throat again."
ms "I swallowed."
ms "I wonder... What would happen if he abstains for a while?"
ms "How much sperm will this giant produce when he cums?"
ms "My inner perverted self trembled with anticipation."
ms "She took control of my body and lips for a moment and passed off her desires as mine."
show mila robe_blush_smirk
m "I want you to abstain from masturbation for three days."
ms "Bob raised his eyebrows in surprise, but then frowned again."
bob "What the heck? Now I can't even jerk off?"
ms "I tried not to lose my confident appearance under his pressure."
show mila robe_proud
m "This is my second condition."
ms "Bob wanted to object, but stopped short, and then grinned."
bob "Hah.{w} Fine.{w} Then you will have to watch a few of my favorite porn movies and write a detailed review about them."
bob "And also..."
show mila robe_irritated_open_mouth
m "There is more?"
ms "Even that was pretty daring, and isn't that enough for him?"
bob "No. You also can't have an orgasm."
show mila robe_puzzled_frown
ms "I looked at Bob indignantly."
m "It sounds like more then one condition..."
ms "Bob chuckled."
bob "But this is it. This is my second condition"
show mila robe_irritated_open_mouth
m "Then I will add something to mine - you will have to leave detailed comments about things that I'll send you."
ms "A shadow of uncertainty fell on Bob's face."
bob "Erm... What will you send me?"
m "Heh."
show mila robe_proud
ms "I chuckled contentedly."
m "Something that will make compliance with my condition more difficult."
ms "Bob continued to frown, but nodded nonetheless."
bob "Deal."
m "..."
ms "Somehow we got heated in this dispute."
ms "But I liked that Bob started arguing with me.{w} And defended his position more firmly."
ms "He still seemed unsure of his words and actions.{w} And I tried to find the line of what was permitted."
ms "But he definitely stepped on the path of growth, not decline."
ms "And at this I cannot but rejoice."
m "..."
ms "I just need to push him a little further in the right direction."
m "And the third condition."
ms "Bob looked at me intently."
m "I want you to get a promotion at work."
show bob nude_bigger_penis_crossed_arms_frown
ms "Bob suddenly became limp and haggard."
ms "Not a trace remained of his former confidence."
ms "He even seemed to have shrunk in size.{w} Although I understand that that is impossible."
bob "Haaa...."
ms "He let out an irritated and tired sigh."
show mila robe_puzzled
bob "I knew that in the end you would ask me to get you a star from the sky or give you an island."
bob "Well, I'm sorry,{w} but that's impossible."
ms "His voice sounded angry, even mocking."
ms "But the edges of his sharp words was not directed at me.{w} Most of all, he hurt himself with it."
m "..."
ms "I knew it was hard to inspire him."
ms "But as practice shows, anger gives him enough energy to do something."
ms "So I carefully added."
show mila robe_worried_open_mouth_wait
m "Yes... And this is my third condition."
ms "Bob glared at me."
ms "Some strange fire flared up in his eyes."
ms "It was scary,{w} but attractive."
bob "Yeah?"
bob "Is that your condition?"
ms "I nodded slowly in response, not taking my eyes off him."
bob "Well, why not?{w} Why not do in a couple of days what I couldn't do in the last 30 years?"
bob "It's so simple after all!"
bob "All I have to do is just try, right?"
ms "I was silent.{w} He is not yet in a state to hear anything."
bob "And who cares that I already tried countless times.{w} I humiliated myself,{w} I did everything I could to change something."
bob "It's fucking pointless."
bob "It's enough to just believe in yourself! Just do it!{w} I'm sick of this crap."
bob "It does not work.{w} The world is unfair.{w} Life is a shitty game with lousy balance."
bob "If you were born a freak,{w} if you have no talents,{w} no one cares about you."
bob "Nobody cares what you want.{w} People just wipe their feet on you."
m "..."
ms "Bob fell silent. His anger began to subside."
ms "But I didn't want him to calm down.{w} I wanted to add fuel to this fire."
m "I'm not asking you to humiliate yourself.{w} I ask you to pump up your desire and self confidence.{w} To realize that you are worth it."
m "To understand, that people will begin to respect you only when you begin to respect yourself."
m "When you accept yourself, forgive yourself and love yourself.{w} Just the way you are."
m "It doesn't mean, that you should give up on trying to be better.{w} Quite the opposite."
m "Love yourself.{w} Hate your weakness.{w} Build a better version of yourself."
ms "Bob winced."
bob "I've had enough."
bob "I don't want to listen to this crap..."
m "..."
ms "I felt irritated."
show mila robe_iritated_atatata
m "Damn it Bob!"
ms "He even flinched in surprise."
m "This is my third condition Bob.{w} Last thing.{w} That's all you need."
m "You understand?"
m "This is not a star from the sky.{w} This is not a challenge from some ticktock crap.{w} It's a tiny step."
m "But a step up, not deeper into the quagmire.{w} This is what you can do.{w} And for fuck sakes, you can."
m "You won't try.{w} No need to try.{w} Put an effort to it.{w} And do it."
m "I'm not asking you to double your monthly salary.{w} Even if you raise your check on 1$ is enough."
m "Just get a fucking raise."
m "And you will get what you want from me."
bob "..."
m "Life is a climb.{w} Don't try to jump over a cliff.{w} Make one tiny step at a time."
m "We always have a choice - to shamefully run away from what we don't like."
m "Or accept ourselves and do what we want to do."
m "In the second case, you may encounter something you hate.{w} And more than once.{w} You can hurt yourself, lose, make mistakes.{w} For the sake of getting a chance."
m "And it doesn't matter whether you get it or not.{w} The important thing is that you keep trying all the way.{w} A person rots if he stops climbing."
m "And yes, if you run away, you will keep what you have.{w} You won't fall down. {w} But you will be left alone with your shame and disappointment."
m "Look around Bob."
m "Is this what you want?{w} What are you trying to save?"
ms "Bob narrowed his eyes."
ms "My words seemed to anger him even more."
bob "You have no idea what I've been through.{w} What I experienced and endured."
bob "How could you know? You are a housewife."
ms "His comment triggered me"
m "\"Just\" a house wife?"
m "First of all I was a professional gymnast.{w} And a good one.{w} I am retired now, and I chose to become housewife after that."
m "And the second thing - being housewife isn't easy.{w} It's a lot of work actualy."
ms "Bob looked like he was sorry for a moment, but then he frown again and continued his speech."
bob "It's just prove my point. "
bob "It's not for you to say all of this to me - you are talented.{w} You were born with a golden spoon in your mouth."
bob "And guess what?{w} I'll prove it to you."
ms "I swallowed again. There was so much strength and confidence in his words...{w} I caught myself thinking that I was admiring his anger."
ms "There was something deeply human in this emotion.{w} Something disgusting and beautiful at the same time.{w} Something repulsive and exciting."
ms "I felt the blood rush to my face."
bob "You think it's all about motivation, huh?"
bob "Then my third condition would be this."
show mila robe_excited_and_shy
bob "When I get promoted, I'll fuck you.{w} I'll put your little ass on this sofa,{w} grab your hair and fuck you until I empty my balls."
bob "I will fuck your throat and you will swallow my dick all the way to the balls.{w} You'll ride my cock like it's a wild rodeo."
bob "I will cover you with my cum from head to toe and you will thank me for it."
show bob nude_bigger_penis_crossed_arms_smirk
bob "How does that sound?{w} Is it ok for you? {w} Do you want my promotion that much?"
ms "Bob became more and more angry with every word. {w} And with every word he said, I became more and more excited."
if mila_dom >= dom:
    ms "I wanted to curb his energy. Subdue him."
    ms "And damn it, I imagined all this in colors."
    jump netorase_mila_and_bob_third_condition_continue

ms "Even though it seemed like the same energy as before,{w} I didn't feel threatened."
ms "I didn't feel used.{w} Quite the opposite.{w} Now I felt my power over him."
ms "He wanted it.{w} He voiced it.{w} And now it became my desire."
ms "To satisfy him.{w} To use my body for its intended purpose."
label netorase_mila_and_bob_third_condition_continue:
ms "Trying not to show my excitement, I nodded slowly."
m "Fine."
show bob nude_bigger_penis_crossed_arms_shock
bob "..."
bob "W-what?"
ms "Bob lost his confidence and blinked his eyes in surprise."
ms "Apparently, his anger broke through the barriers of his consciousness, and all these fantasies simply burst out."
show mila robe_blush_smirk
m "I said okay."
ms "Feeling in control of the situation gave me more confidence."
ms "So I was able to smile."
bob "W-what... {w}Hic...{w} do you mean?"
ms "Bob still couldn't believe it. It was so shocking for him that he started hiccuping again."
ms "A grin crept onto my lips."
m "If you get a promotion at work,{w} I will stand doggy style on this sofa and spread my ass."
m "I'll get on my knees, or whatever you want and gobble your big cock, even if I choke on it."
m "I'll climb on your lap, and ride you like there is no tomorrow"
m "And every time you cum, I'll squeeze every drop of your semen and ask for more."
ms "Bob opened and closed his mouth, unable to answer."
ms "I giggled."
m "How does it sound?{w} Is it ok for you?"
ms "My heart was pounding furiously in my chest."
ms "We put our fantasies into words, and suddenly all of it became real."
ms "Although nothing has happened yet, they have become so close."
ms "I opened the door and turned towards the corridor."
show mila robe_from_behind_looking
m "Good night, Bob."
bob "..."
m "And prepare things you need for tomorrow..."
m "I'll come by to pose for you."
ms "Bob silently followed me with his eyes, still in a state of shock."
play sound "door-open-close.mp3"
scene bg doors with fade
ms "As the door closed in my face, I felt the coolness of the night air."
ms "A gentle breeze crept under my clothes and stroked my sweat-covered skin."
ms "It suddenly became chilly."
m "..."
show mila robe_closed_eyes_kiss
m "Achoo!"
m "..."
m "I hope I don't get sick..."


scene bg a125_mila_puzzled with fade
ms "I walked into the house and put my back against the door. "
ms "In the silence of the corridor, I could clearly hear my heart beating."
ms "Something is changed in me...{w} And everywhere..."
ms "..."
ms "What just happened?"
ms "..."
ms "Did I, um. agreed to sleep with Bob?"
ms "..."
p "Baby!"
ms "Paul's voice came from the bedroom. "
ms "I took a deep breath, calming down. "
ms "..."
ms "I'll probably have to tell him about what happened..."
ms "But how?{w} Where do I start..."
ms "Hi Paul, you know Bob's going to fuck me soon.{w} You don't mind, do you?"
ms "..."
scene bg a125_mila_worried
ms "..."
ms "He doesn't mind, does he?"
ms "..."
ms "I sighed once more and went to the bedroom."
scene bg bedroom
ms "Paul was waiting for me with the same smirk on his face. "
ms "..."
show mila robe_curious at center
ms "I looked around, but I didn't see anything suspicious."
m "So...{w} Where's the surprise?"
ms "Paul hummed. "
p "Later. "
p "First, tell me how it went with Bob. "
ms "I told Paul what happened. "
ms "And when I got to Bob's third condition, I noticed a glint in Paul's eye. "
ms "He got really excited. "
show screen nts_stats_overlay
menu:
    "I should be careful with his feelings (Mila's submissiveness + 1)":
        $ dom += 1
        jump a125_mila_sub
    "Paul likes teasing (Mila's dominance + 1)":
        $ mila_dom += 1
        jump a125_mila_dom

label a125_mila_sub:
show mila robe_excited_and_shy at center
ms "I wonder how he'll react to my words..."
hide screen nts_stats_overlay
ms "What...{w} Will he tell me to do?"
ms "...{w}{image=emoji/heart.png}"
m "He said he'd bring me to my knees..."
show mila robe_blush_smirk
m "And fuck me.{w} Hard..."
ms "Paul swallowed."
p "Go on. "
ms "His eyes burned with lust. "
ms "I could feel his burning gaze in my skin. "
m "He...{w} He said he'd take me by the hair."
m "And put his cock down my throat. "
show mila robe_puzzled
m "And you know.{w} I'm afraid I'm gonna suffocate from it. "
m "When he fucked my face last time, I thought I was gonna die..."
ms "Paul licked his lips and smirked."
p "You lack practice."
show mila robe_puzzled_frown
m "Hmm?"
ms "I looked at him in surprise. "
ms "Paul pulled out a huge dildo from somewhere and walked over to me. "
show mila robe_worried_open_mouth_wait
p "You know, I had a thought..."
p "I listen to your stories,{w} I fantasize about what you do and how you do it."
p "But it's not enough. I can't see it"
p "So apparently you're doing it pretty badly."
ms "I frowned indignantly."
show mila robe_irritated_open_mouth
m "I don't..."
p "Silence. "
show mila robe_worried_open_mouth_wait
ms "Paul said it hard and loud. "
ms "His voice resonated in my chest, giving off an itchy tingle in my lower abdomen. "
ms "I instantly shut my mouth and averted my gaze."
ms "Oh, man. I love it when he acts like this..."
p "Every day I realise more and more how I want you to be."
m "..."
p "And you know what? I think it's time for your training. "
ms "I looked up at Paul in confusion. "
m "Training?"
ms "Paul waved the dildo in front of my face. "
p "Get your hair out of your face."
ms "I looked at him uncomprehendingly."
p "Move your hair to the back of your head. "
m "..."
ms "I still remained silent, Paul frowned."
p "What are you waiting for, do it!"
scene bg a125_mila_fix_hair
ms "I swallowed,{w} I pulled out a rubber band and gathered my hair into a ponytail. "
p "On your knees. "
scene bg a125_mila_from_above
ms "Bob's attack still hadn't faded from my memory. "
ms "That's why obeying Paul's orders was difficult."
p "Hands behind your back."
ms "But with each passing second, the excitement was crowding out the anxiety. "
ms "I wonder what Paul had come up with this time?"
ms "Paul brought the toy up to my face. "
p "Open your mouth. "
ms "The huge phallus in front of my face resembled Bob's cock.{w} Only it smelled of something artificial,{w} chemical,{w} not at all like Bob."
scene bg a125_mila_from_above_penis_cringe
ms "I cringed at the smell."
ms "Paul frowned. "
p "That's not good. "
p "You're thinking too much. "
p "There's only one emotion a whore like you should feel when you see a cock!"
p "It's happiness."
scene bg a125_mila_from_above_penis_cringe_look_up
ms "I wasn't horny enough to take his dirty talk positively."
ms "It seemed like a simple insult. "
p "Here we go again. "
ms "Paul took hold of my hair and pulled me down."
scene bg a125_mila_from_above_struggle
m "Ay yay yay!"
ms "I grabbed his arm trying to push him away. "
p "Hands behind your back!"
ms "I didn't listen. "
ms "Paul leaned right into my face. "
p "Why are you resisting?{w} Do you think I can't see the juices dripping between your thighs?{w} Your head is getting in the way of your pleasure."
p "You're a slut. You want to be fucked like a whore.{w} Your body wants to be treated like a whore."
p "But your bad head is too full of thoughts and illusions about who you are. "
m "..."
ms "Paul spat on my face. "
scene bg a125_mila_from_above_spit
ms "My throat burned with resentment. My eyes filled with tears. "
ms "Paul couldn't say that about me. He doesn't think that. It's all a game..."
ms "It's not real..."
scene bg a125_mila_from_above_spit_tears
ms "Paul smirked."
p "Open your mouth, whore, and stick your tongue out. "
ms "I pressed my lips together on principle. "
ms "Paul leaned back irritably. "
p "You don't want to admit it, do you?"
p "You want it all to stop."
p "You want to wake up tomorrow morning still the same perfect wife, don't you?"
m "..."
p "Okay then,{w} I'll talk to Bob.{w} I'll tell him you're not a whore at all,{w} but a faithful wife. "
p "And then you can keep doing the house chores.{w} Just like before. "
scene bg a125_mila_from_above_spit_looking_aside
ms "..."
ms "No..."
ms "I don't want that..."
ms "I don't want to die of boredom again..."
ms "Also..."
ms "Why does he say that?{w} Why is he so cruel to me?"
ms "..."
ms "Because...{w} because I like it. "
ms "I was finally able to swallow the lump in my throat."
scene bg a125_mila_from_above_spit_sucking
ms "I slowly loosened my lips and opened my mouth. "
ms "My inner voice was hysterically screaming at me. "
ms "That I should respect myself.{w} That this is not me.{w} That all this humiliation was unacceptable. "
ms "But Paul's contemptuous and commanding gaze drowned out that voice. "
ms "Smothering it with his overwhelming presence. "
ms "And I melted under that gaze. "
scene bg a125_mila_from_side_suck
p "That's it.{w} Good girl."
ms "Those words were like a warm balm to me. "
ms "I let go of his hand and slowly put my hands behind my back. "
p "Show me how you sucked Bob's dick, slut"
ms "My lust drowned out all other feelings and thoughts. "
ms "There was only one desire left.{w} To obey."
ms "I slowly took the toy into my mouth and began to suck on the head. "
ms "..."
m "Mmm."
m "..."
m "..."
ms "Paul watched me for a while, then exhaled irritably."
p "What a pathetic sight..."
scene bg a125_mila_from_above_pout
ms "I frowned and let the toy out of my mouth. "
p "I've been meaning to tell you for a long time..."
p "Keep sucking, why the fuck did you stop?"
m "..."
scene bg a125_mila_from_side_suck
ms "I reluctantly obeyed."
p "I've been meaning to tell you for a long time - you are terrible at sucking. "
scene bg a125_mila_from_side_suck_2
ms "Oh, I'm sorry!{w} If you don't like it, suck it yourself..."
ms "I almost cried with resentment. "
p "And this was exactly the reason why I kept silent - your reaction.{w} I was afraid that you would be insulted and cry."
scene bg a125_mila_from_side_suck_2_2
ms "I froze and looked at Paul. "
p "But now I know that you want to be a real slut. {w}So I properly train you to be one."
p "Suck it.{w} Deeper."
scene bg a125_mila_from_side_suck_2
m "..."
m "..."
m "..."
p "Yeah..."
m "... "
m "..."
p "All right, that's enough."
scene bg a125_mila_from_above_pout
ms "I leaned back and wiped my lips."
p "Firstly, you need to use more saliva, comprende?"
p "And not just a little more, you need to have so much of it running down the balls and your chin."
p "Got it?"
ms "I reluctantly nodded in response."
p "Answer, yes Master. "
m "..."
m "Yes... Master..."
p "Secondly, you must learn to relax your throat."
p "Your body must become a living onahole oozing love juices."
p "Keep that in mind - you're just a cumdump. "
p "Now, say it out loud. "
ms "What a nonsense..."
m "..."
p "Do it."
scene bg a125_mila_from_above_admit
m "I'm...{w} I'm just a cumdump..."
ms "Somehow it didn't sound as humiliation or an insult."
ms "It felt like a...{w} praise?"
ms "Paul pushed the dildo into my mouth until it was in my throat. "
scene bg a125_mila_from_side_suck_3_1
m "Mgmm!"
ms "The rubber head pressed into my throat, triggering the gag reflex. "
scene bg a125_mila_from_side_suck_3_3
p "You're still struggling."
scene bg a125_mila_from_side_suck_3_2
m "(cough)"
scene bg a125_mila_from_side_suck_3_3
p "I don't like it."
p "Repeat in your head - I'm just a cumdump."
ms "..."
scene bg a125_mila_from_side_suck_3_2
m "(cough)"
scene bg a125_mila_from_side_suck_3_3
ms "I'm just a cumdump..."
scene bg a125_mila_from_side_suck_3_2
m "(choking)"
scene bg a125_mila_from_side_suck_3_3
ms "I'm just a cumdump..."
p "Loosen your throat, whore."
p "I can't do it for you."
p "It's the privilege of true whores to learn to ignore their gag reflex to suck cock."
p "And you're going to be that whore. "
p "You must give up your selfish desire for pleasure."
p "You must let go of your selfish desire for pleasure."
scene bg a125_mila_from_side_suck_3_2
m "(cough)"
scene bg a125_mila_from_side_suck_3_4
p "You've got to realise that your purpose is to give pleasure"
p "And to do that, you must learn to enjoy pain, humiliation, suffocation."
scene bg a125_mila_from_side_suck_3_5
m "(cough)"
scene bg a125_mila_from_side_suck_3_4
p "Swallow."
ms "I can't..."
scene bg a125_mila_from_side_suck_3_5
m "(cough)"
scene bg a125_mila_from_side_suck_3_4
p "I said swallow. "
ms "It's impossible...{w} I just can't do it..."
ms "I took a deep breath through my nose.{w} Then I relaxed, despite feeling the pressure on my throat"
ms "And then...{w} I just swallowed."
scene bg a125_mila_from_side_suck_4
p "That's it. Good girl."
ms "I have no idea how something so thick got down my throat."
ms "But it did"
ms "My throat stretched and encompassed the head"
ms "My mouth filled with slippery saliva"
ms "Paul kept pushing, pushing the toy deeper"
scene bg a125_mila_from_side_suck_5
m "(cough)"
p "That's my girl "
p "Good girl"
p "That's it. "
ms "I felt like the toy had already sunk into my stomach. "
ms "My throat was intermittently contracting and trying to push the foreign object out."
scene bg a125_mila_from_side_suck_6
m "(choke)"
p "To the balls, baby. "
p "That's it. Good girl."
ms "Rubber balls were poking my chin."
ms "My mouth was filled with saliva"
ms "Tears filled my eyes."
ms "But I could see Paul's satisfaction, and it gave me strength."
ms "I tried to relax, but I wasn't very good at it. "
ms "The discomfort was too much..."
m "(cough)"
ms "Paul slowly pulled the toy out of my throat, and I could barely hold back the gagging from the sensation. "
m "..."
scene bg a125_mila_from_side_breather
ms "I breathed greedily and kept swallowing bitter saliva."
p "That's enough.{w} Open your mouth and stick out your tongue. "
ms "There were no thoughts left in my head."
scene bg a125_mila_from_side_suck_3_4
ms "I complied, despite the unpleasant sensations."
ms "The less I think about them, the better. "
ms "The phallus slipped into my mouth and into my throat."
ms "I closed my eyes and tried to relax."
scene bg a125_mila_from_side_suck_3_5
m "(cough)"
p "Come on.{w} Deeper, slut."
ms "I swallowed, and the cock entered my throat."
scene bg a125_mila_from_side_suck_4
m "(cough)"
scene bg a125_mila_from_side_suck_5
p "That's it. "
p "That's how you're supposed to suck Bob's cock. "
scene bg a125_mila_from_side_suck_6
ms "The rubber balls were back again, poking my chin."
p "Use your tongue too. {w} You're just a cumdump. {w} Use everything you have to please the man."
m "..."
scene bg a125_mila_from_side_suck_7
p "Good girl. {w} That's it."
p "Imagine what it would be like.{w} His huge belly and hairy pubes would be up against your nose."
p "You'd smell the sour odour of his sweat."
p "And his cock would be plunging down your throat"
p "That's how whores give blowjobs"
m "(cough)"
scene bg a125_mila_from_side_breather
ms "Paul pulled the toy out of my mouth again."
ms "I was trying to catch my breath at this point. "
ms "Paul waved the phallus in front of my face. "
p "Now prove that you know how to do it. "
p "Suck 'Bob' in a way that makes me believe you want his cum."
scene bg a125_mila_from_side_pulling_cock
ms "I hesitated for a moment, but then I took the cock in my hand and guided it into my mouth."
p "Hands off."
scene bg a125_mila_from_side_suck_2
ms "I plunged the head into my mouth and began to suck it diligently."
p "The fuck are you doing again?{w} Fuck.{w} Your.{w} Throat."
scene bg a125_mila_from_side_suck_5
ms "When I had to move my head on my own, my throat tensed up."
scene bg a125_mila_from_side_suck_4
m "(cough)"
scene bg a125_mila_from_side_suck_5
ms "And that made it harder for me to relax."
p "You're just a cumdump. "
scene bg a125_mila_from_side_suck_4
m "(cough)"
scene bg a125_mila_from_side_suck_5
p "You are thinking too much again"
p "Your job is to bring pleasure "
scene bg a125_mila_from_side_suck_4
m "(cough)"
scene bg a125_mila_from_side_suck_5
p "Do it"
ms "Man, that sounds so stupid..."
ms "..."
scene bg a125_mila_from_side_suck_4
m "(cough)"
scene bg a125_mila_from_side_suck_5
ms "Fuck it. "
ms "I'm just a cumdump..."
ms "I'm a perverted whore."
ms "I like to suck cock."
ms "I want to bathe in cum."
ms "I want to be gangbanged"
ms "I want to be used as a 'thing' "
scene bg a125_mila_from_side_suck_4
ms "I'm just a cumdump"
p "That's it.{w} Good girl."
scene bg a125_mila_from_side_suck_8
ms "I didn't notice as the cock began to sink quietly down my throat. "
ms "And this time, I didn't feel so uncomfortable. "
ms "I wanted it even deeper."
scene bg a125_mila_from_side_suck_9
ms "I pressed my face into the rubber balls."
ms "The phallus widened my throat so much I couldn't breathe. "
ms "But I tried to shove it in even deeper, like I was trying to swallow it whole."
scene bg a125_mila_from_side_suck_10
ms "I stuck out my tongue and tried to lick the balls on the dildo"
ms "And that's when I felt the hot drops on my face."
scene bg a125_mila_from_side_cum1
p "Yeah, slut!"
p "That's it.{w} Choke on that fat cock.{w} Oh, shit, you are perfect..."
scene bg a125_mila_from_side_cum2
p "Oh, fuck"
scene bg a125_mila_from_side_cum3
p "Yeah"
ms "Realizing that Paul was already cumming and I was running out of air, I finally pulled back and started gulping for air."
scene bg a125_after_fellatio
m "Haaaaah...{w} hahaha...{w} Haaaa..."
ms "A smile crept over my face.{w} I felt so happy that Paul came. "
ms "It was like I'd really fulfilled my purpose. "
p "Good girl"
p "I'd fuck you with that toy, but the problem is{w} you are forbidden to cum."
p "And judging by the puddle between your legs, you're not far from orgasm. "
p "So... {w}Tough luck, huh?"
scene bg a125_after_fellatio2
ms "..."
ms "What had just happened?"
ms "..."
ms "...{w}{image=emoji/heart.png}"
if _in_replay:
    return
jump a126

label a125_mila_dom:
show mila robe_blush_smirk at center
m "Do you know what he'll do to your wife?"
p "..."
hide screen nts_stats_overlay
m "He wants me to get on the couch and spread my ass."
ms "I turned my back to Paul."
scene bg a125_all_fours
m "Like this, maybe?"
m "He's gonna grab me by the hair and put his cock deep in my mouth, up to his balls."
p "..."
ms "Paul's cock was clearly protruding from his trousers. "
scene bg a125_all_fours_grin
m "And then, I'm gonna get down on my knees."
scene bg a125_fellatio_gesture
m "Open my mouth and let him fuck my face."
p "..."
m "Mmm? What is it?"
m "Wanna see? "
scene bg a125_smirk
m "Do you want to see your unfaithful wife suck another man's dick? "
m "How his balls are gonna slap my pussy? "
m "How he's gonna pour gallons of his cum all over my face?"
p "...{w} Yes..."
m "Uhuh..."
m "But I'm afraid you'll just have to live with your fantasy for now."
m "But if you want me to, I can return home covered in his cum next time."
m "Would you like to see that?"
scene bg a125_grin
p "Yes!"
p "Yes, hell yes! "
m "Mmm, I think someone got overexcited fantasizing..."
scene bg a125_smirk
m "But you see, Bob forbade me to cum."
m "So I can't help you with your problem."
ms "I nodded at his cock."
m "..."
m "Why are you looking at me like that?"
m "..."
scene bg a125_dildo
m "W-what is it?"
ms "Paul shoved a huge dildo in front of my face."
p "This is the surprise I told you about."
m "Hmmm..."
scene bg a125_dildo_smirk
m "And what do you want me to do with this...{w} surprise?"
p "..."
ms "Paul didn't answer.{w} You want me to tease you, huh?"
m "Wow...{w} It's so big!"
m "It looks like Bob's cock..."
m "You know.{w} I'm dying to try what it feels like.{w} To ride a giant like that. "
m "I threw off my robe"
ms "Shit,{w} I'm so excited... {w}But Bob forbade me to cum...{w} I shouldn't lie to him"
ms "So I need to seriously hold back"
scene bg a125_dildo_squating
m "..."
m "Oh god, it's huge!"
m "I don't think it's gonna fit inside me"
m "What do you think?"
m "Mmm."
m "You can jerk your cock off while this giant fucks your wife."
ms "Paul hurriedly pulled his cock out of his trousers and grabbed it like he wanted to rip it off."
m "Ahahhh..."
scene bg a125_dildo_squating2
m "Mmm...{w} Watch Bob's cock stretch my pussy."
m "Shhhh... {w} Ouch... {w} Oh, God, it's so big "
m "Aaahhhh..."
m "Mmm... "
m "Oh Bob, take your time, let me get used to it..."
m "I've never been fucked by such a huge dick..."
m "..."
m "Hehe... Do you like the show?"
p "Y-yes..."
m "Then I will try harder for you and try to sit lower..."
scene bg a125_dildo_squating3
m "Ahhh..."
m "Ohh fuck..."
m "Bob you will tear me apart...{w} Be careful..."
m "Mmm..."
m "Uff...{w} I think this is my limit, Bob..."
ms "The toy filled my pussy.{w} He was so huge that I felt more pain than pleasure."
m "I sat down as deep as I could.{w} And the dildo rested against my uterus, delivering painfully pleasant sensations."
m "..."
m "Mmm"
scene bg a125_dildo_squating4
m "Do you like it?"
p "Yes! Very!"
m "Ahah"
m "Do you want to cum?"
p "Yes!{w} I'm already close..."
m "You're not allowed to cum in my pussy, that's Bob's privilege."
m "He reserved it."
m "That's why you'll cum on my feet"
m "Be grateful"
m "..."
scene bg a125_dildo_squating_feet
ms "I had to hold myself up so as not to impale myself even deeper on Bob's dick...{w} I mean... {w} on the dildo, of course."
ms "I still put some weight on my crotch, and it pushed the dildo deeper making me frown in pain"
ms "Paul, feeling the touch of my legs, almost immediately began to cum."
scene bg a125_dildo_squating_feet_cum
m "Pfff...{w} Ahaha..."
m "Good boy."
m "Release everything onto my feet..."
m "..."
m "Good boy"
m "Are you happy?"
p "..."
m "Did you like how your wife was jumping on this huge dick?"
p "..."
scene bg a125_dildo_squating_feet_cum_pout
m "No?{w} Sorry then I will never do this again..."
p "...{w} {size=-12}I like it..."
m "Hmmm...{w} What was that?"
p "{size=-6} I said, I liked it..."
scene bg a125_dildo_squating_feet_cum
m "Oh you do?{w} I had no idea! {w} So do you want me to do it again?"
p "... {w}Yes."
m "Hehe"
m "It's a pity, that I can't cum, I would love to bring myself to orgasm too..."
ms "I carefully stood up from the dick and turned my back to Paul."
m "Look."
scene bg a125_after_sex_spread
ms "I deliberately did not tense my pussy muscles so that my pussy would look as stretched out as possible."
m "..."
p "... {w}wow."
m "Do you like it?"
p "Y-yes..."
m "I will be horny as fuck after couple of days without cumming"
m "And then Bob will fuck your wife in that needy pussy"
p "..."
m "Is that what you want, darling?"
ms "Paul swallowed."
m "I want you to say it"
p "... {w}I want you to get fucked by Bob... {w}And then I want to see you covered in his cum..."
scene bg a125_after_sex_spread_grin
m "Hehe...{w} If my husband desires it, I will do it"
if _in_replay:
    return


label a126:

ms "..."
scene 126_mila_sleeping with fade
ms "I slept terribly."
scene 126_nightmare_blink
ms "All night I was tormented by some sort of erotic nightmares..."
ms "Monsters chased me, caught me and raped me."
ms "Fear mixed with excitement, disgust with lust"
ms "I woke up later than usual, covered in cold sweat"
ms "..."
scene 126_mila_morning
m "Damn...{w} Not only did I not get enough sleep..."
m "But my pussy is itching..."
m "I'm not some nymphomaniac...{w} But the moment something is forbidden - you start to want it more and more"
scene 126_mila_morning_blush
ms "..."
ms "My head was filled with thoughts of what happened yesterday."
ms "About the conversation with Bob...{w} And what happened after."
ms "..."
scene 126_mila_morning_phone
ms "Hmmm..."
ms "There were a couple dozen unread messages from Bob on my phone."
ms "These were links to porn clips."
ms "Judging by the sending time, he spent the whole night gathering and sending them to me."
ms "..."
m "Maybe that's why I slept so poorly?"
scene 126_mila_morning_phone_smirk
ms "Maybe he was that horny monster, and it was his growing desire that I felt?"
ms "Damn... Now I want to punish Bob for this."
play sound "shot.mp3"
scene 126_mila_morning_selfie with flash_nightmare
ms "..."
ms "Looks good"
ms "But... {w} I think I need to cover my nipples...{w} I still feel kind of unsafe..."
ms "Yep. That's better"
ma "Good morning!"
ma "{image=bob/selfies/morning_1_126.webp}"
ms "Bob didn't have to wait long for an answer."
bob_message "!"
scene 126_mila_morning_phone_grin
ms "Ahah..."
ms "Now sit there and hide your sausage from your colleagues."
ms "hehe"
scene 126_mila_morning_phone_smirk
ma "One exclamation mark is not enough for a complete answer."
ms "I saw that the message status changed to “read”, but there was no response"
ma "Should I assume that our agreement is invalid?"
bob_message "No."
ms "Bob responded almost immediately"
bob_message "I don't know how to answer..."
bob_message "You are very beautiful."
ma "Thanks Bob."
scene 126_mila_morning_phone_grin
ms "hehe"
ms "Okay, it'll do the first time."
bob_message "Have you already watched the clips?"
scene 126_mila_morning_phone
ms "..."
m "When did he become so persistent?"
ma "No Bob, I just woke up."
bob_message "Good morning."
scene 126_mila_morning_phone_smirk
ms "This is what you should have said at the beginning."
ms "..."
ms "Okay, let's see what's there."
ms "After thinking a little, I decided to record a voice message while I watched the video."
ms "This will be easier than writing the text later."
ms "..."
scene 126_video_1 with fade
m "Hi Bob. I'm starting to watch your videos."
m "The title says \"A good stretch\"..."
m "The first one is about a girl in a gym?{w} Is it even considered porn? {w}Ok, let's see..."
ms "..."
scene 126_video_2
m "Oh, she's flexible.{w} I still can do something like that too, I think"
ms "..."
scene 126_video_3
m "And this is apparently the coach."
ms "..."
m "Yeah, he wants to help her with stretching."
m "She looks like a ballerina or gymnast. {w}Nice"
scene 126_video_4
ms "..."
m "Ah..."
m "Oooh..."
m "It's about that kind of stretching..."
scene 126_video_5
ms "..."
m "Holy fuck..."
m "He is huge"
m "Are you kidding me?{w} It's impossible..."
m "It won't fit."
m "Asses won't stretch that much."
scene 126_video_6
ms "..."
m "Ok, I take my words back."
m "..."
m "What do men find in anal anyway?"
m "This hole is not meant for sex."
scene 126_video_sex
ms "..."
m "I kind of get it..."
m "For some reason it looks hot"
ms "My hand went down to my pussy."
m "Mmm..."
ms "Damn, the main thing is not to cum."
m "Bob, can you hear those sounds?"
"shlick{w} shlick{w} shlick"
m "Don't worry...{w}mmm...{w} I'll keep my promise...{w}Ahhh...{w} And I'll stop on time..."
m "Mmm..."
"shlick{w} shlick{w} shlick"
m "Damn, but this will be hard."
scene 126_video_8
ms "..."
m "Wait, he wants her to suck him off?"
ms "..."
m "But his dick just was in her ass..."
scene 126_video_9
m "..."
m "Of course, he'll force her to do it..."
m "Um...{w} Do you like this?"
ms "..."
m "It's humiliating"
m "Although I won't hide it, there is something in this."
m "Something dirty.{w} In the literal sense of the word."
ms "..."
m "Also, I think your dick is bigger."
scene 126_video_cum
m "Oh, he is cumming on her face"
m "There's something particularly naughty about finishing on the face, right?"
m "That's it?"
m "Cool video, I liked it."
ms "I turned off the recording."
scene 126_mila_morning_phone with fade
ms "My pussy itched with desire."
m "I need some kind of distraction..."
ms "I want Bob to have a hard time concentrating too."
m "Hmmm..."
scene 126_mila_morning_phone_smirk
ms "..."
ms "Maybe I should stretch out a bit too?"
ms "I changed clothes and set up a camera"
ms "My pussy was so wet that my leggings were soaked with my juices."
play sound "shot.mp3"
scene 126_mila_stretching with flash_nightmare
ms "Hmmm..."
ms "Is it too much?"
ms "I'm basically showing my pussy to him..."
ms "...{w} So what?"
ms "He will fuck me soon anyway."
ms "..."
ms "Hehe"
ms "Let's see his reaction"
ma "I watched the first video"
ma "I liked it!"
ma "It got me thinking..."
ma "Do you want to help me stretch?"
ma "{image=bob/selfies/morning_2_126.webp}"
bob_message "Oh God..."
ms "hehe..."
ma "That's all what you got to say?"
ma "Do you think am I flexible?"
bob_message "Yes"
bob_message "Sorry, I haven't gotten over your audio message yet..."
ma "I bet it's hard for you there."
ms "hehe"
ma "But I still need a more detailed comment on my picture."
bob_message "I can help you... With stretching."
ma "Oh thanks! That is so nice of you."
ma "What do you imagine when you see me in this position?"
ms "Bob read my message again but did not respond."
ma "Bob"
ma "It's new to me, too."
ma "But I recorded a whole voicemail for you while I was watching porn."
ma "I bet you can say something naughty too..."
ma "I want it"
ms "Bob didn't answer"
ma "Pretty please?"
ms "It took him a while to answer"
ms "..."
ms "Come on, Bob, tell me something dirty..."
bob_message "I imagine taking off your leggings and fucking you in the ass."
ms "My ass?!"
ma "Why my ass?"
bob_message "I don't know. I like it"
ma "I'm afraid it's impossible, Bob"
ma "Have you seen your dick?"
bob_message "The anus can stretch up to 14 cm in diameter without any effort."
ms "Up to 14!.. I don't believe it."
bob_message "So don't worry about that."
ms "Wait a minute. What do you mean don't worry?"
ma "I don't plan on having anal sex, Bob."
bob_message "Oh..."
bob_message "OK..."
ms "I wanted to support him somehow, so I took another selfie."
ms "..."
play sound "shot.mp3"
scene 126_mila_selfie with flash_nightmare
ma "But I plan to do something else ;)"
ma "{image=bob/selfies/morning_3_126.webp}"
bob_message "Oh God..."
bob_message "Mila, if you don't stop sending me such pictures, I might cum in my pants just from rubbing against my fly."
ms "Pfft, hahahaha."
ms "These are the kind of comments I'm talking about!"
ma "Be careful out there."
ms "I watched a couple more videos from the collection and recorded audio messages."
ms "While I was doing this, I didn't notice that evening had come."
m "Damn, I haven't done anything useful today..."
ms "I feel like a freeloader now..."
ms "..."
ms "Well, okay, let's assume that today is my day off."


scene br with fade
ms "..."
scene 126_mila_after_shower
ms "Paul had not yet returned home when I heard Bob enter his apartment."
ms "I took a shower to freshen up a little."
ms "I wanted to put on my usual robe, but suddenly I felt like it's not fitting"
ms "My body changed along with my thoughts"
ms "I wanted to attract attention"
ms "I wanted men to want me"
ms "My men"
scene 126_mila_after_shower_naughty
m "Hehe..."
ms "The problem is that I didn't really hide my body before."
ms "But now I wanted to somehow highlight my goodies"
ms "..."
scene 126_mila_after_shower_top
ms "I came to the bedroom and rummaged through the clothes to find something that would fit \ ''the new me'' vibe better."
ms "I picked out a top without straps"
ms "I remember it kept falling off my chest, and I stopped wearing it."
ms "Now, this is not a problem.{w} Well, even if it falls, so what?"
ms "I'll please a couple of passers-by with my naked tits"
ms "I do not mind"
scene 126_mila_after_shower_from_behind
ms "I also found shorts that I bought a long time ago for going to the beach."
ms "I never dared to go outside in them."
ms "They looked too slutty for me"
ms "I twirled around in the mirror admiring my reflection."
ms "fufu...{w} I wonder what Bob will say..."
ms "Okay, time to go..."
scene 126_mila_hi
ms "..."
m "Hi Bob!{w} I came!"
ms "Bob was sitting on the living room couch in front of a small album of pencils."
ms "There was a camera in his hands."
bob "Hey,{w} take off your clothes."
bob "I want to take some pictures for reference."
scene 126_mila_surprised
ms "..."
ms "I recoiled slightly from his pressure."
ms "But Bob remained seated, so I was not afraid or uncomfortable from this pressure."
ms "I even felt a little offended that he didn't say anything about my appearance."
scene 126_mila_worried
m "W-wait. Let's move gradually."
ms "Bob frowned."
bob "Again?"
scene 126_mila_serious
m "I not going back on my words."
m "Simply using your own words - how can I guarantee you will fulfill your part of the deal?"
bob "..."
m "If I take off my clothes now, you'll take a few pictures, and then you won't draw anything."
bob "I wouldn't do that."
scene 126_mila_worried
m "Well, I would have kept my word too, but you didn't believe me."
m "Why should I believe you?"
bob "..."
bob "I don't like where this is going"
bob "What do you suggest?"
m "..."
scene 126_mila_serious
m "Let's do this..."
m "I will undress.{w} Piece by piece.{w} And you will draw me in every step.{w} How does that sound?"
bob "..."
bob "But I will need a lot of time for each sketch."
m "So?{w} Are we in a hurry?"
bob "..."
m "..."
scene 126_mila_smile
bob "Fine."
bob "But then, I want you to change into something."
scene 126_mila_serious
ms "I looked at myself."
ms "And why then did I choose this outfit?"
m "If it's not more revealing than what I'm already wearing, fine."
ms "Bob looked away embarrassed"
bob "No, it is...{w} On the contrary, mine is more prudent."
scene 126_mila_smile
bob "And by the way, you look great..."
ms "For some reason, his compliment made me smile contentedly."
ms "Bob went into the bedroom, rustled his clothes there for a while, and returned to the living room."
bob "Erm...{w} It's on the bed."
ms "I interestedly went into his bedroom and closed the door."
scene 126_bobs_room_uniform with fade
m "..."
if dom >= mila_dom:
    ms "Are you kidding me?"
    m "Bob are you serious?"
    bob "S-sorry...{w} I..."
    bob "This is...{w} This was my dream since school..."
    m "Haaa..."
    jump continue_126
ms "Hooo..."
ms "Bob is a dirty boy..."
ms "I would prefer a teacher outfit more, but this is ok, too"
ms "I can imagine how I will tease him in the furture"

label continue_126:
scene 126_bobs_room_mila_changed
ms "I took off my clothes and changed"
ms "It's better not to think about where he got this suit and what he did with it."
m "..."
scene 126_bobs_room_mila_smirk
ms "Although I can imagine how he jerked off on it...{w} It's more exciting than repulsive."
m "..."
ms "When did I become such a pervert?"
scene 126_bobs_room_mila_changed
ms "Or have I always been like this?.."
if dom >= mila_dom:
    scene 126_living_room_mila_shy with fade
    m "..."
    ms "I went to the center of the room."
    bob "..."
    m "..."
    bob "..."
    scene 126_living_room_mila_sad_smile
    m "Um...{w} Bob?"
    ms "Bob flinched"
    bob "S-Sorry.{w} That is simply gorgeous!{w} You are gorgeous!"
    scene 126_living_room_mila_giggle
    m "Hehe..."
    m "Thank you."
    scene 126_living_room_mila_teasing
    m "But seriously, Bob...{w} I already look like a teenager, but you still want to dress me up in a school uniform?"
    bob "S-sorry..."
    scene 126_living_room_mila_giggle
    m "It's okay.{w} But do notice, I won't call you daddy.{w} It's cringey..."
    bob "..."
    ms "Bob was speechless and just looked at me with his mouth open."
    jump continue_126_2
scene 126_living_room_mila_smug with fade
m "Good morning, Bob, can I borrow you homework?"
bob "..."
m "..."
scene 126_living_room_mila_teasing
m "Oh...{w} You want me to call you Sensei, right?"
m "Won't happen"
bob "..."
scene 126_living_room_mila_shy
m "Erm...{w} Bob?{w} Hello?"
ms "Bob flinched"
bob "S-sorry!{w} I was just...{w} I mean...{w} Wow..."
scene 126_living_room_mila_giggle
m "Ahah"
m "Do you like how I look?"
bob "God, yes!"
scene 126_living_room_mila_raised_eyebrow
m "So it's not enough for you that I already look like a teenager?"
m "You want to dress me up like one?"
bob "I'm sorry"
scene 126_living_room_mila_giggle
m "Don't be. I'm just messing with you."

label continue_126_2:
scene 126_living_room_mila_teasing
m "..."
m "Well, what's next?"
bob "Erm...{w} Could you sit on the table and cross your legs?"
scene 126_living_room_mila_sitting_crossed_legs
m "..."
m "Like that?"
bob "Yes."
ms "Bob took out pencils and began frantically scraping them on the paper."
m "..."
bob "..."
ms "I physically felt his gaze crawling over my body."
ms "I heard the rustling of the stylus on the canvas"
ms "The sound sent shivers through my body.{w} It was as if he was guiding it along my exposed nerves."
ms "I tried not to move, which made me feel more like an exhibit in a museum."
ms "A thing to be admired"
scene 126_living_room_mila_sitting_crossed_legs_nipples
ms "My skin became sensitive, and therefore, the clothes seemed prickly and scratchy"
ms "I wanted to throw them off"
ms "I let his gaze caress my body directly, without additional obstacles"
ms "And his silence only aggravated these feelings."
scene 126_living_room_mila_sitting_crossed_legs_nipples_open_mouth
m "Have you ever been in love?"
ms "I remembered his confession and immediately felt sorry"
scene 126_living_room_mila_sitting_crossed_legs_nipples_worried
m "I mean, before..."
ms "Bob froze for a moment"
scene 126_living_room_mila_sitting_crossed_legs_nipples
bob "Yes..."
m "..."
bob "First time was in school..."
bob "Her name was...{w} Anna."
scene 126_living_room_mila_sitting_crossed_legs_nipples_warm_smile
m "It's a beautiful name."
bob "Yes."
bob "She sat in front of me in middle school."
bob "I admired her... Her back."
scene 126_living_room_mila_sitting_crossed_legs_nipples_giggle_smirk
ms "I grinned."
m "Her {b}back{/b}?"
bob "Yes."
m "You meant her ass?"
bob "..."
m "..."
bob "..."
bob "Can you now untie your necktie, unbutton your shirt a little and lean forward?"
ms "His demanding voice made me shiver"
scene 126_living_room_mila_sitting_leaning_forward
m "..."
m "Like this?"
bob "Yes, perfect."
ms "The pencil began to crawl across the paper again."
scene 126_living_room_mila_sitting_leaning_forward_open_mouth
m "Did you confess to her?"
scene 126_living_room_mila_sitting_leaning_forward
bob "..."
bob "No."
ms "Before I could ask the next question, Bob continued."
bob "She started dating one of the bullies.{w} His name was Billie. Billie \"the truck\" they called him"
m "The truck?{w} Why so?"
bob "..."
bob "He somehow dragged two defenders on himself.{w} They start calling him like that afterwards."
m "Is this something from football or other?"
bob "Kind of.{w} Rugby."
bob "Well, in general - he was strong, popular, aggressive and stupid.{w} Classic."
bob "Why is every good girl is always attracted to some douchebag?"
scene 126_living_room_mila_sitting_leaning_forward_open_mouth_sceptical
ms "I shrugged."
m "Not everyone.{w} I've never liked show-offs, for example.{w} Paul was a nerd, by the way."
scene 126_living_room_mila_sitting_leaning_forward
ms "Bob shot his eyes at me, but did not comment on my words."
bob "Then her grades got worse."
bob "And then she actually started going on paid dates."
bob "According to rumors at least..."
scene 126_living_room_mila_sitting_leaning_forward_open_mouth
m "..."
m "Have you tried to talk to her?"
bob "Who would listen to me?"
scene 126_living_room_mila_sitting_leaning_forward_warm_smile
m "I would."
bob "..."
m "..."
bob "Can you sit with your back to me?"
scene 126_living_room_mila_sitting_from_behind
m "..."
m "Like this?"
bob "Yes."
m "..."
bob "And..."
bob "Can you also...{w} lift your skirt?"
ms "Blood rushed to my face."
scene 126_living_room_mila_sitting_from_behind_lift
ms "I obediently pulled up my skirt and showed my ass to Bob."
ms "He swallowed."
bob "{size=-12}Oh Lord, have mercy on me..."
m "..."
scene 126_living_room_mila_sitting_from_behind_lift_open_mouth
m "And what happened next?{w} To this girl, I mean"
ms "Talking helped me not to think too much about what I was doing right now"
bob "..."
bob "I don't know."
bob "I...{w} I was angry with her and stopped paying attention."
m "Hmm..."
bob "I think then I realized that all women think with their pussies."
scene 126_living_room_mila_sitting_from_behind_lift_sceptical
m "Wev do?"
m "And you?"
bob "What about me?"
m "Are you not thinking with your dick?"
bob "..."
m "Sex is the oldest human motivation source."
scene 126_living_room_mila_pants_pull
ms "I stood up, turned sideways to Bob, put my hands under my skirt and pulled my panties down."
m "Everything we do is either for sex or about sex."
m "And in this you are no different from that girl."
ms "My panties were hanging around my knees. Only my skirt covered my pussy."
ms "Bob was breathing heavily and stroking the bulge in his pants."
ms "His gaze became heavy... Predatory."
ms "I felt like prey again."
ms "I felt fear again.{w} And desire."
scene 126_living_room_mila_after
ms "I swallowed and stood up."
m "I think that's enough for today."
bob "But you're not naked!"
ms "Bob looked at me indignantly."
m "I'm afraid a little more, and you won't be able to hold back, and you will just attack me."
m "And this is not what you, and I agreed on."
ms "Bob grimaced."
bob "This is really not what we agreed on.{w} You promised to pose for me {b}naked{/b}"
ms "Bob frowned"
scene 126_mila_after_door
ms "Already at the door I stopped, turned around and looked at Bob."
m "I did promised you that"
m "And I will"
bob "..."
m "And so that you don't think that I don't keep my word."
scene 126_mila_after_skirt_lift
m "..."
bob "..."
m "Good night, Bob."
"..."


play sound "door-open-close.mp3"
scene bg door with fade
ms "..."
show mila schoolgirl_pout at center:
    xpos 0.6
ms "Even though I spent more than an hour with Bob, Paul has not returned yet."
ms "He's taking his time today"
show mila walk_achoo
m "Achoo!"
ms "..."
show mila walk_thoughtful
ms "Is it because of the dust?"
ms "I should clean up at least a little..."
scene bg apartments with fade
ms "Paul came home as soon, as I changed clothes."
show paul suit_open_mouth_blush at left
p "Honey I'm ho... Woah.{w} Wow!"
show mila slutty_smirk
m "How do you like my outfit?"
if dom >= mila_dom:
    show paul suit_smirk
    p "Gorgeous!"
    p "You look like a real whore"
    show mila slutty_embarassed
    m "I...{w} That was my intention..."
    p "Turn around.{w} Show me your ass"
    show mila slutty_from_behind
    p "..."
    p "Mmm...{w} Great shorts."
    show mila slutty_from_behind_smirk
    m "Thank you...{w} Master."
    jump walk_126_continue_1

show paul suit_blush_looking_aside
ms "Paul looked away and blushed"
ms "I ran my hand over my thighs."
m "Let me give you a hint - I look like a slut, right?"
ms "Paul shot his eyes at me."
ms "I turned my back to him."
show mila slutty_from_behind_ass_support
m "Look at this ass."
m "You really want to spank it, don't you?"
ms "Paul swallowed."
show mila slutty_from_behind_grin
m "Ahah.{w} Sorry, I didn't mean to tease you too much."
m "Do you like it?"
p "... Yes."
m "I'm glad."

label walk_126_continue_1:
show paul suit_open_mouth_neutral
p "By the way, I'm dying of hunger."
show mila slutty_awkward
m "Um..."
m "You know..."
m "The thing is...{w} I didn't cook anything today."
ms "Paul looked at me questioningly"
p "Something happened?"
m "Not really..."
show mila slutty_awkward_smile
m "I lay on my bed all day and watched porn"
show paul suit_smirk
p "..."
m "..."
p "Sounds... Tough..."
m "..."
p "..."
show mila slutty_giggle
show paul suit_grin
m "Pfff! hahaha!"
ms "..."
if dom >= mila_dom:
    show paul suit_smirk
    ms "A grin crept onto Paul's face."
    p "Shall we go for a walk?"
    show mila slutty_smirk
    m "With pleasure! Let me just change my clothes"
    p "No."
    show mila slutty_concerned
    m "?.."
    p "You will go in this. You didn't just dress up like that"
    p "I would even add something."
    scene 126_slutty_mila_before_walk
    m "..."
    jump walk_126_continue_2

show paul suit_open_mouth_neutral
p "Um... Maybe we can go eat somewhere?"
show mila slutty_smirk
m "Let's."
ms "Paul smiled contentedly."
ms "I headed towards the exit."
m "Let's go then?"
show paul suit_open_mouth_blush
p "..."
p "Erm..."
p "You won't go outside like that, right?"
show mila slutty_concerned
ms "I looked at myself"
m "Oh, right...{w} Sorry, give me a sec."
"..."
scene 126_slutty_mila_before_walk
m "..."
m "That's better?"
p "..."
p "You want to go like that?"
m "Yep"
p "..."
label walk_126_continue_2:
m "How do I look?"
p "..."
ms "Paul smiled."
p "Gorgeous, darling."
m "So?{w} Let's go then?"
ms "..."
scene bg park with fade
ms "The sun had not yet completely set below the horizon.{w} Its rays painted the park hundreds of tones of yellow."
ms "The warm wind ruffled my hair and caressed my bare skin with gentle touches."
ms "The sweet smell of flowers and the fresh smell of grass mixed with the smells of food prepared in the trays."
ms "I just now realized how much I want to eat."
ms "Paul's stomach growled loudly."
scene 126_walk_date_grin
ms "We looked at each other."
m "Ahah.{w} How about boiled corn?"
p "No, I want something more nourishing."
ms "I constantly caught the glances of passers-by while we were looking for somewhere to eat."
ms "Having chosen a small Mexican bench, we settled down on high chairs."
scene 126_walk_date_cafe
ms "..."
ms "Paul looked around nervously for a while."
ms "I was so hungry that I didn't immediately understand the reason for his concern."
ms "But as soon as I stuffed my tummy, I realized that the eyes of almost everyone around me were directed at me."
scene 126_walk_date_cafe_aroused
ms "I swallowed and felt almost naked."
m "..."
ms "Well... {w}I am practically naked."
ms "..."
scene 126_walk_date_cafe_aroused_biting_lip
ms "I leaned forward slightly"
m "Do you think they can see my ass well?"
if dom >= mila_dom:
    p "I think they would be happy to pull off your shorts and fuck you right on this chair."
    scene 126_walk_date_cafe_smirk
    m "Hmmm...{w} You think so?"
    m "Would you like to see that?"
    p "Very. Fucking. Much."
    jump walk_126_continue_3

ms "Paul looked down in embarrassment."
scene 126_walk_date_cafe_smirk
m "I could pull down my shorts now and take your hands."
m "And some dork would sit behind me and fuck me"
p "..."
m "Imagine my face at that moment."
scene 126_walk_date_cafe_pretend with dissolve
pause 0.5
scene 126_walk_date_cafe_smirk
ms "Paul swallowed."
m "hehe"
label walk_126_continue_3:
scene bg park with fade
ms "When we finished eating, Paul looked at me strangely and invited me to walk in the park."
ms "..."
show mila slutty_concerned at right
ms "Actually, it's strange - Paul doesn't really like to walk"
ms "I glanced at him suspiciously"
m "Are you up to something?"
show paul suit_smirk at center
ms "Paul just smiled and extended his hand to me."
m "..."
show mila slutty_idle:
    easein 0.7 xpos 0.8
ms "I still felt unsure on heels, so I grabbed onto Paul."
ms "Fortunately, we were walking slowly, so I kept my balance quite easily"
ms "And I literally felt how heels highlight my butt"
show mila slutty_from_behind_ass_support
ms "Almost every passersby gazed at my legs and ass"
ms "Women and elderly people frowned and grumbled something under their breath."
ms "One granny even quite clearly called me a whore"
show mila slutty_from_behind_grin
ms "I just smiled back"
ms "The men turned their heads and followed us with their gaze."
ms "I glanced at Paul. He was beaming with pride."
show mila slutty_proud
m "Heh."
ms "His reaction give me even more confidence, causing me to straighten my back and begin to rock my hips more."
show mila slutty_concerned
ms "Where are we actually going?"
ms "There were almost no people in this part of the park."
ms "I looked questioningly at Paul."
show paul suit_grin
ms "He just grinned."
m "..."
ms "Okay, let's see what he came up with."
m "..."
ms "We found a free bench and sat down."
show mila slutty_awkward
ms "I looked around.{w} It wasn't completely deserted, but there were passers-by at a certain distance."
ms "I hope Paul doesn't want to have sex here..."
ms "Someone will definitely call the police..."
show mila slutty_concerned
m "..."
ms "And is that only thing that bothers me?"
m "..."
show mila slutty_giggle
ms "Hah."
ms "..."





label hscene_netorase_park:
scene bg park
show mila slutty_giggle at right:
    xpos 0.8
show paul suit_grin at center
p "Do you see that guy?"
show mila slutty_idle
ms "I emerged from my thoughts."
m "Mmm? {w} Where?{w} That one with a backpack?{w} Yeah, what about him?"
p "He looks lonely."
show mila slutty_concerned
m "Erm...{w} Yeah...{w} He is.{w} Poor guy."
ms "I couldn't understand what was Paul's deal"
p "Reminds me a bit of Bob, doesn't he?"
show mila slutty_suspicious
m "..."
ms "What is he getting at?"
m "Maaay-be?"
show paul suit_smirk
p "I think he needs to be inspired somehow...{w} What do you say?"
m "Inspired?"
p "..."
show mila slutty_surprised
m "..."
m "Are you asking me to?.."
p "..."
show mila slutty_surprised2
m "You're not serious, right?"
p "..."
show mila slutty_serious
m "Are you serious?"
p "Yes."
m "..."
show mila slutty_concerned
m "And how can I \"inspire\" him?"
p "Hmmm...{w} Well, you know better than I..."
m "So it's up to me to decide?"
p "..."
p "Yes."
show mila slutty_awkward
m "..."
p "..."
m "I don't have a condom."
show paul suit_open_mouth_neutral
ms "Paul raised his eyebrows."
p "Wow. Are you planning to inspire him that much?"
show mila slutty_frown
m "Then what did you mean?"
show paul suit_open_mouth_blush
p "Erm...{w} I mean...{w} Yes, in principle that would be inspiring..."
show mila slutty_suspicious
m "Actually, I thought about giving him a blowjob.{w} With a condom."
p "Ah...{w} Ok..."
show mila slutty_frown
m "Ok?{w} Is it \"OK!\" type of ok,{w} or an \"I get it\" type of ok?"
p "It's \"OK\"..."
show mila slutty_surprised
ms "Ok?.."
show mila slutty_surprised2
ms "OK?!"
ms "I didn't have much time to process what Paul just said"
m "!"
m "Damn, he's leaving!"
scene 126_walk_date_lee_meeting_1
ms "Obeying a sudden impulse, I jumped up and ran"
ms "I didn't know what would I do when I catch up to him"
ms "And I don't know how I didn't kill myself while running in heels"
scene 126_walk_date_lee_meeting_2
m "Wait!"
m "Sorry!"
ms "The guy looked at me"
"???" "Um...{w} Are you talking to me?"
scene 126_walk_date_lee_meeting_3
m "Yes!"
m "Can you help me?"
"???" "...{w} Um...{w} Sorry, I don't have money..."
ms "The guy lowered his eyes."
scene 126_walk_date_lee_meeting_4
ms "Hah.{w} He really reminds me of Bob in some ways."
m "It's OK."
ms "The guy looked at me suspiciously and lowered his gaze again."
ms "So...{w} So what's next?"
ms "I can't just offer him a blow job, can I?"
scene 126_walk_date_lee_meeting_5
m "Erm..."
ms "I took a closer look at the guy."
ms "I've seen this badge somewhere..."
ms "It looks like it's from some kind of game..."
ms "Hmmm...{w} \"OverSee\" or something?"
ms "Right, it's a game Bob told me about"
scene 126_walk_date_lee_meeting_6
m "Erm,{w} listen,{w} are you a fan of \"OverSee\"?"
ms "The guy looked at me in surprise."
"???" "Um...{w} Well yes..."
m "Listen, I did a cosplay of one character..."
m "But I don't know much about it, can you take a look?"
scene 126_walk_date_lee_meeting_6
"???" "Well, OK."
ms "I showed him the photo."
"..."
ms "The guy launched into lengthy explanations about how my cosplay sucked, and what needed to be changed."
ms "I pretended to listen carefully and nodded."
ms "The guy, apparently sensing my pretense, frowned."
scene 126_walk_date_lee_meeting_8
"???" "Why do you want it? Are you getting ready for the comiket?"
m "Yes, I..."
ms "I started scrolling through the photos and \"accidentally\" showed several of my naked selfies"
scene 126_walk_date_lee_meeting_9
m "Oopsie."
m "Sorry."
ms "The guy blushed"
"???" "..."
m "..."
"???" "Are you doing it for onlyfans?"
scene 126_walk_date_lee_meeting_10
ms "Whaaa?.."
m "Um...{w} Onlychans?"
"???" "Don't play dumb."
"???" "You want to make a video of my reaction to your nudes, am I right?"
ms "Does he think this is some kind of adult prank?"
ms "I can use this, I think..."
scene 126_walk_date_lee_meeting_11
m "No, actually, I want to make some... different type of content..."
ms "The guy frowned."
m "..."
m "I want you to film me while I suck your dick"
scene 126_walk_date_lee_meeting_12
"???" "W-what?"
m "Well,{w} if you don't mind of course."
m "I'll suck you off, and you'll record it."
m "For my onlychance."
"???" "Onlyfans."
m "Right.{w} That's what I said."
ms "Whatever"
"???" "..."
"???" "O-ok..."
scene 126_walk_date_lee_meeting_13
m "Let's go then."
"???" "{size=-12}I hope I won't be killed there..."
ms "I quickly turned and winked at Paul, then took the guy by the hand and led him towards the public toilet."
"..."
scene 126_walk_date_lee_toilet_1 with fade
m "It's kinda cramped in here..."
m "I won't close the stall, ok?"
m "I hope we won't get caught"
m "Do you happen to have a condom?"
"???" "Yeah!"
scene 126_walk_date_lee_toilet_2
m "Sweet! Locked and loaded, huh? Ahah"
"???" "I have it for good luck."
m "And as you can see, you got lucky"
ms "He handed me a condom."
scene 126_walk_date_lee_toilet_3
m "Thank you."
m "Do you like blowjobs?"
"???" "I...{w} don't know...{w} I guess?"
ms "Is it his first time?"
ms "..."
scene 126_walk_date_lee_toilet_4
ms "Sweet"
m "Oh ok, it's no big deal."
m "Do you want me to take off your pants?"
"???" "N-no, I'll do it myself"
m "Sure."
ms "The guy hastily unbuttoned his jeans."
ms "It suddenly struck me what was happening"
ms "But for some reason I didn't feel bad at all"
ms "I felt in control of the situation"
ms "And that's why...{w} It was fun"
scene 126_walk_date_lee_toilet_3
m "Take your time, I'm not going anywhere."
ms "..."
"???" "W-why? I don't..."
ms "His dick remained soft"
"???" "Come on! Get it up!"
ms "He convulsively grabbed his flaccid penis and began to crush it"
scene 126_walk_date_lee_toilet_2
m "Be careful, you'll tear it off."
"???" "Well... why now!?"
ms "The guy was ready to burst into tears"
scene 126_walk_date_lee_toilet_4
m "You're just nervous. Look at me."
"???" "..."
m "Look at me."
ms "He looked up."
scene 126_walk_date_lee_toilet_5
m "Everything is alright, don't worry."
m "My name is Mila,{w} what's yours?"
"???" "..."
"???" "Lee..."
scene 126_walk_date_lee_toilet_6
m "Lee?"
m "That's an interesting name,{w} are your parents from China?"
"???" "No.{w} My parents are idiots."
scene 126_walk_date_lee_toilet_2
m "Ahah, sorry."
scene 126_walk_date_lee_toilet_1
m "Do you like me, Lee?"
"???" "...{w} Yeah, you are gorgeous..."
scene 126_walk_date_lee_toilet_2
m "Ahah.{w} Thank you."
scene 126_walk_date_lee_toilet_5
m "Do you want to touch my breasts, Lee?"
"???" "Can I?"
m "Sure!"
scene 126_walk_date_lee_toilet_7
ms "I put my hands behind my back."
ms "The guy grabbed my nipples and pinched them hard"
scene 126_walk_date_lee_toilet_8
m "Ouch!"
m "Not so rough"
"???" "S-sorry..."
m "It's nothing.{w} Just...{w} Be gentle, ok?"
"???" "..."
scene 126_walk_date_lee_toilet_9
m "Like?"
"???" "Yes, very much!"
scene 126_walk_date_lee_toilet_10
m "(heh)"
m "You can pull my top down.{w} You want to see them too, right?"
ms "The guy swallowed and pulled my top down"
scene 126_walk_date_lee_toilet_11
"???" "Wow..."
m "Do you like my titties?"
"???" "..."
m "I see you do"
ms "I pointed my finger at his penis."
m "Now, he's ready."
"???" "Y-yes..."
m "Here is my phone.{w} Can you sit down?{w} You can record me however you like."
m "Ready?"
"???" "..."
"???" "Yes."
scene 126_walk_date_lee_record_1 with fade
m "Hello everyone, today I met this wonderful guy in the park."
m "His name is Lee.{w} Say hi to everyone, Lee!"
ms "I instantly got into the role."
ms "To be honest, I enjoyed this situation."
"???" "H-hi everyone...{w} I'm Lee."
m "Lee couldn't resist groping me before the recording started."
scene 126_walk_date_lee_record_2
m "Look at my red nipples, it's because Lee grabbed them with all his might."
"???" "B-but you said..."
m "It's okay, I am joking."
scene 126_walk_date_lee_record_3
m "Well Lee here told me that he wanted a blowjob from me"
m "Is it true?"
"???" "Y-yes..."
m "I should get to it then."
m "Let me show you a little trick"
ms "I opened the condom and put it in my mouth."
scene 126_walk_date_lee_record_4
ms "I squatted down, took his penis, and directed it into my mouth, pulling the condom along its entire length."
scene 126_walk_date_lee_record_5
"..."
scene 126_walk_date_lee_record_6
"..."
scene 126_walk_date_lee_record_7
ms "His dick was smaller then Bob's, but it still pressed against my throat."
ms "So I had to help myself with my hand."
scene 126_walk_date_lee_record_8
"..."
m "And it's done"
if dom >= mila_dom:
    ms "Paul's lessons came to mind"
    scene 126_walk_date_lee_record_9
    "..."
    scene 126_walk_date_lee_record_10
    "..."
    scene 126_walk_date_lee_record_11
    ms "I collected as much saliva as possible and slowly began to lower my head until his dick hit my throat."
    scene 126_walk_date_lee_record_12
    ms "Then I tried to relax and swallowed"
    scene 126_walk_date_lee_record_13
    ms "The dick slid deeper"
    "???" "Ooohhhh fuck..."
    "???" "Oh my god..."
    scene 126_walk_date_lee_record_14
    ms "His dick smelled something sour"
    ms "Here he also resembled Bob."
    m "Mmm..."
    scene 126_slutty_blowjob
    m "..."
    m "*suck*{w}*suck*{w}*suck*{w}"
    m "..."
    ms "I tried to relax, took it as deep as I could, and stuck out my tongue to lick his balls"
    scene 126_walk_date_lee_record_16
    m "..."
    "???" "Ohhh wow..."
    ms "..."
    scene 126_walk_date_lee_record_17
    m "*cough*"
    scene 126_walk_date_lee_record_16
    m "..."
    scene 126_walk_date_lee_record_17
    m "*cough*"
    scene 126_walk_date_lee_record_18
    ms "..."
    scene 126_walk_date_lee_record_19
    ms "..."
    scene 126_walk_date_lee_record_20
    m "Haa...{w} Haaa...{w} Haaa..."
    "???" "Are you alright?"
    scene 126_walk_date_lee_record_21
    m "Sure"
    m "Do you like it?"
    "???" "Yes! It's awesome!"
    scene 126_walk_date_lee_record_22
    m "Ahah."
    m "I'm glad you like it"
    scene 126_walk_date_lee_record_23
    ms "I felt that I had already warmed up enough."
    ms "So I wanted something more."
    ms "I wanted to feel like... a thing again..."
    ms "I'm just a cum dump..."
    scene 126_walk_date_lee_record_24
    m "Do you want to...{w} Fuck my throat?"
    "???" "W-what?"
    m "Stand up"
    "..."
    scene 126_walk_date_facefucking_1 with fade
    ms "I put my hands behind my back."
    m "Fuck my mouth, Lee."
    ms "I opened my mouth and stuck out my tongue."
    "???" "Wow..."
    scene 126_walk_date_facefucking_2
    ms "Lee hesitantly put his hands on my head and tenderly pushed his cock inside my mouth."
    scene 126_walk_date_facefucking_3
    ms "I tried to smile with his dick in my mouth to encourage him"
    ms "Don't worry big boy, you wont break me"
    scene 126_slutty_irrumatio_slow
    m "..."
    ms "Lee was so carring, that it made me smile"
    ms "Well...{w} Not literally...{w} His cock was drilling my mouth, so I couldn't actualy smile"
    ms "But he never pushed it full force"
    ms "Maybe that's why I experienced almost no discomfort."
    ms "My pussy itched with desire."
    ms "Come on big boy, you can push it deeper..."
    ms "Use me..."
    ms "I should show him, that he can be a bit more rough"
    ms "I started adding pressure and speed"
    scene 126_slutty_irrumatio_fast
    ms "..."
    ms "Yes..."
    ms "Fuck me..."
    ms "Lee's movement became rougher.{w} Maybe he saw it in my eyes.{w} I wanted it"
    scene 126_walk_date_facefucking_4_1
    ms "He stopped for a moment to gather my ponytail for a better grip"
    ms "I didn't stop him"
    ms "And then he just started fucking my head."
    scene 126_slutty_irrumatio_fast_2
    ms "The pace became faster, and also he started to put more pressure"
    ms "That's when his cock finally slid down my throat"
    scene 126_walk_date_facefucking_6clean
    m "*gag*"
    ms "Lee paused"
    ms "I am not sure why... {w}Maybe he was enjoying the moment{w} or was just to scared to continue"
    scene 126_walk_date_facefucking_6
    ms "Despite the running tears, I tried to encourage him."
    ms "Use me like a slut big boy...{w} I don't mind it"
    ms "Lee pushed his cock even deeper"
    scene 126_walk_date_facefucking_7
    m "*Gag*"
    scene 126_walk_date_facefucking_8_cough
    m "*cough*"
    scene 126_walk_date_facefucking_8
    ms "I'm just a cum dump..."
    scene 126_walk_date_facefucking_8_cough
    m "*cough*"
    scene 126_walk_date_facefucking_8
    ms "I'm just a cum dump..."
    "???" "Oh fuck, I'm going to cum!"
    ms "The guy pressed his belly to my nose and pushed his dick deep into my throat"
    ms "I felt how his cock begin to pulsate inside"
    scene 126_walk_date_facefucking_7
    "???" "Yeees!!!"
    scene 126_walk_date_facefucking_8_cough
    "???" "Fuck..."
    scene 126_walk_date_facefucking_8a
    "???" "Yes"
    scene 126_walk_date_facefucking_8_cough
    "???" "Oooh..."
    scene 126_walk_date_facefucking_8aa
    ms "The condom stretched in my throat."
    ms "I felt the sperm accumulating in it."
    m "..."
    ms "Finally he leaned back and pulled his dick out of me."
    scene 126_walk_date_facefucking_9
    m "Haaa...{w} Haaaaa"
    "???" "Are you ok?"
    scene 126_walk_date_facefucking_10
    m "Ahaha.{w} Don't worry, I'm fine"
    "..."
    scene 126_walk_date_facefucking_10a
    ms "I carefully pulled the condom off his penis and tied it."
    ms "I'll give it to Paul later."
    ms "My face is probably a mess... I need to fresh up a little"
    jump walk_126_continue_4

scene 126_slutty_blowjob_lazy
ms "I started sucking his dick, helping myself with my hands"
m "..."
"???" "Ohh yeah..."
"???" "Oh god..."
ms "The itch in my pussy..."
ms "I wonder how Paul will react if I ride this boy now"
ms "Damn, this is unbearable..."
ms "I want to cum..."
ms "But I shouldn't..."
ms "..."
ms "Wait,{w} what would happen if I came?"
m "..."
ms "I would break Bob's trust."
ms "And he won't trust me anymore?"
ms "C'mon."
m "..."
scene 126_walk_date_lee_record_dom_1
ms "I didn't notice how my hand ended up in my shorts."
m "Mmm..."
ms "I want a dick, I want a dick, I want a dick."
ms "To hell with it!"
scene 126_walk_date_lee_record_dom_2
ms "I stood up and pulled off my shorts and took off my top"
ms "Lee swallowed"
scene 126_walk_date_lee_record_dom_3
ms "It felt exciting to be naked in public place...{w} And liberating"
m "Sorry, I got a little overexcited"
m "Would you mind if I change the type of service?"
"???" "Erm..."
scene 126_walk_date_lee_record_dom_4
m "I want your cock right here"
ms "The black eye of the camera traced every move"
ms "I imagined how Paul would watch the recording"
ms "Mmm... {w}I wanna tease him more..."
m "Lean back a bit"
scene 126_walk_date_lee_record_dom_5 with fade
ms "I took his dick and inserted it into my pussy"
m "Ohhh fffuck..."
ms "I was ready to cum at that very second"
ms "But I gave myself some time to get used to the sensations"
scene 126_walk_date_lee_record_dom_5a
m "Mmm..."
ms "It's also nice to keep yourself on the edge..."
ms "Maybe I should really try not to cum?"
scene 126_walk_date_lee_record_dom_6
ms "I started rubbing my pussy on his dick"
"???" "..."
ms "Lee looked at me like a little mouse"
scene 126_walk_date_lee_record_dom_7
ms "You are so funny."
scene 126_walk_date_lee_record_dom_7a
m "Do you like my pussy, Lee?"
scene 126_walk_date_lee_record_dom_7
"???" "Y-yes..."
scene 126_walk_date_lee_record_dom_7a
m "Mmm..."
scene 126_walk_date_lee_record_dom_7
m "Do you want me to sit lower?"
scene 126_walk_date_lee_record_dom_7a
"???" "Yes! Please!"
scene 126_walk_date_lee_record_dom_7aa
m "Ahah"
scene 126_walk_date_lee_record_dom_7a
m "Will you cum for me if I sit lower?"
scene 126_walk_date_lee_record_dom_7
"???" "I think so...{w} I'm on the edge, miss..."
ms "I am on edge myself...{w} If I start moving more I may cum too"
scene 126_walk_date_lee_record_dom_7a
m "Do you want to cum in my pussy? Or in my mouth?"
"???" "In the pussy!"
scene 126_walk_date_lee_record_dom_7aa
m "Ahah."
scene 126_walk_date_lee_record_dom_7a
m "Fine."
scene 126_walk_date_lee_record_dom_8
m "Cum for me Lee."
scene 126_walk_date_lee_record_dom_9
m "Cum in my pussy."
scene 126_walk_date_lee_record_dom_8
"???" "Ahhh"
scene 126_walk_date_lee_record_dom_9
"???" "Yes!!!"
scene 126_walk_date_lee_record_dom_10
ms "I felt Lee's cock begin to throb, pumping sperm into the condom."
ms "I found myself thinking that I would like him to come without a condom."
ms "The pussy stimulation almost brought me to orgasm, so I had to hold myself with all my might."
ms "Fuck!{w} Bob will have to fuck me really good to compensate for this..."
"???" "Haa... Haaa... Haaa..."
scene 126_walk_date_lee_record_dom_11
ms "After catching my breath a little, I pulled his dick out"
ms "Then I pulled off the condom and tied it."
ms "I'll give it to Paul as a trophy."

label walk_126_continue_4:
scene 126_walk_date_after_light_smile with fade
ms "I fixed my clothes and was waiting for Lee to dress up"
ms "My drenched pussy was itching, demanding some attention"
ms "That sensation drove all of my thoughts away"
ms "I didn't gave many thoughts about what just happened"
ms "I just wanted to have sex..."
scene 126_walk_date_after_worried
ms "I looked at Lee. He was sitting on the toilet, immersed in his thoughts"
ms "Lee was awfully quiet"
m "Is everything ok?"
ms "He flinched"
"???" "Yeah...{w} I just... {w}This is the best day of my life."
scene 126_walk_date_after_grin
m "Ah..."
m "I'm happy to hear that.{w} Thank you for your time, I liked it too"
ms "I took my phone from him and straightened my clothes."
scene 126_walk_date_after_light_smile
m "Okay, I'll go.{w} Thanks again."
"???" "W-wait!"
scene 126_walk_date_after_surprised
m "Mmm?"
ms "I turned around."
"???" "C-can I take your pic?"
"???" "A memory photo..."
scene 126_walk_date_after_worried
ms "I thought about it."
ms "On the one hand, I already shared my photos with a stranger."
ms "On the other hand... This is still very risky."
if mila_dom > dom:
    ms "I just fucked him."
else:
    ms "...{w}I just sucked him off..."
ms "What can be more risky than that?"
scene 126_walk_date_after_grin
m "If you want to show off...{w} It would be better to take a selfie together, don't you think?{w} Come closer"
scene 126_walk_date_after_selfie with fade
play sound "shot.mp3"
"..."
"???" "Thank you! Thank you!"
ms "Lee took his time before pulling his hands away"
ms "I literally had to break out of his arms"
ms "For a moment I had this disgusting feeling of lost control"
ms "But Lee finally let me out"
ms "And I rushed to the exit"
scene 126_walk_date_after_worried
m "Have a nice day, Lee."
m "Bye bye."
ms "..."
scene bg public_toilet with fade
show paul suit_sad at left
show mila slutty_serious at right
ms "Paul was waiting for me outside."
ms "I looked at him and all my worries just dissapeared"
show mila slutty_giggle:
    easein 1 xpos 0.5
ms "I greeted him with a smile."
m "You look like a pimp"
p "..."
show paul suit_smirk
p "Because you look like a whore."
show mila slutty_proud
m "Ahah, thank you.{w} I'll take it as a compliment."
p "Everything is fine?"
show mila slutty_proud_condom
ms "I showed him the condom."
m "I recorded an interesting video for you."
show paul suit_open_mouth_blush
p "Oh God..."
ms "I couldn't read expression on his face"
ms "But a moment after he smiled"
show paul suit_smirk
p "Can't wait to see it."
show mila slutty_smirk
m "I think you also want to see this"
scene 126_walk_date_after_condom_pour
m "..."
scene 126_walk_date_after_condom_close_mouth
m "..."
scene 126_walk_date_after_condom_close_mouth_2
m "..."
play sound "swallow.wav"
m "..."
scene 126_walk_date_after_condom_open_mouth
m "..."
p "..."
p "Holy fuck..."
scene 126_walk_date_after_condom_giggle
m "Ahah"
m "Do you like that?"
p "Fuck yes!"
scene 126_walk_date_after_condom_naughty
if _in_replay:
    return



label a127:
"..."
scene 127_mirror_disgust with fade
ms "Yikes..."
ms "I still had the taste of cum in my mouth even though I had brushed my teeth and washed my face."
scene 127_mirror_serious with dissolve
ms "My throat felt sore."
"..."
scene 127_in_bed_paul_alone with fade
ms "Paul was already in bed when I returned."
ms "He was so immersed in his thoughts that he didn't notice me entering the bedroom."
m "..."
scene 127_in_bed_mila_and_paul with dissolve
ms "I crawled under the blanket and lay down next to him without saying a word."
ms "After everything that happened, I felt a strange mixture of feelings."
ms "Fear...{w} Guilt...{w} Arousal..."
ms "I was so focused on my own feelings that I forgot about Paul's feelings"
scene 127_in_bed_worried with dissolve
m "Are you ok?"
m "..."
p "..."
m "Paul?"
p "?"
ms "Paul winced."
p "Oh sorry.{w} I was lost in thoughts."
p "What was the question?"
scene 127_in_bed_smile with dissolve
m "It's okay"
m "Is everything fine?"
p "..."
scene 127_in_bed_worried with dissolve
m "..."
p "..."
m "Paul?"
scene 127_in_bed_worried_2 with dissolve
p "*sigh*"
ms "Fear consumed me.{w} It was as if it grabbed my head with icy fingers and pulled my hair back."
ms "I swallowed."
scene 127_in_bed_worried with dissolve
p "I...{w} I can't understand my feelings."
m "..."
p "Everything that is happening... Turns me on wildly."
p "But I have a feeling that we are{w} drifting apart..."
scene 127_in_bed_hug with dissolve
ms "I pressed my whole body against him."
m "There is only one way to get even closer, but right now it is not available to us."
p "..."
scene 127_in_bed_hug_2 with dissolve
p "..."
p "Well, did you understand what I meant?"
m "Certainly."
p "..."
scene 127_in_bed_mila_and_paul with dissolve
m "You know..."
m "We had months when we didn't have sex..."
scene 127_in_bed_worried with dissolve
m "Do you remember?"
ms "Paul nodded."
p "It's not that I stopped loving you..."
ms "I shook my head."
scene 127_in_bed_mila_and_paul_2 with dissolve
m "I know.{w} I felt the same..."
m "Routine.{w} Habit.{w} Boredom."
m "Love and sex seemed to be separated."
m "And sex was no longer necessary."
scene 127_in_bed_shy with dissolve
m "I just...{w} masturbated sometimes...{w} And that was enough."
p "..."
m "But now..."
scene 127_in_bed_naughty with dissolve
m "It's only been three days, Paul, and I'm already going crazy."
m "In my head there is only sex, sex, and sex."
m "I just got out of the shower, but I can already feel my pussy is wet."
ms "Paul stroked my back and his touch caused a pleasant tingling throughout my body."
m "What I want to say is..."
m "Sometimes restrictions and fantasies add excitement."
m "New sensations."
p "..."
scene 127_in_bed_smug with dissolve
m "How about I forbid you from having sex with me until something is done?"
scene 127_in_bed_smug_frown with dissolve
p "..."
p "For example?"
m "For example, the next time you have sex will be only the way you want."
m "But it must be something new."
p "..."
scene 127_in_bed_naughty with dissolve
p "For example, what if I want to see you with someone else?"
m "Well, you can already, I sent you a video."
p "..."
p "Then, I want to fuck you while you're blowing someone else."
scene 127_in_bed_smirk with dissolve
m "Sounds hot."
m "Deal."
ms "Paul squeezed my ass."
scene 127_in_bed_pleasure with dissolve
m "Aahh..."
scene 127_in_bed_pout with dissolve
m "Stop teasing me, I can barely hold on anyway."
"..."
scene bg apartments with fade
show mila oversized_shirt_haaa at center:
    xpos 0.6
m "Haaa..."
show mila oversized_shirt_pout
ms "Okay,{w} I tried."
ms "But this is damn unbearable - no matter what I do, all my thoughts still slide towards sex."
ms "I looked at the clock."
show mila oversized_shirt_shock
m "It's only 11 p.m.?!"
show mila oversized_shirt_haaa
m "Haaa..."
show mila oversized_shirt_pout
show 127_bobs_sketch at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
bob_message "{image=bob/selfies/127_bobs_sketch_low.webp}"
hide 127_bobs_sketch
show mila oversized_shirt_surprised
ma "Wow!"
show mila oversized_shirt_happy
ma "Bob it's really good! You shouldn't say you are bad at it"
bob_message "Do you like it?"
ma "Yeah, you're great at drawing!"
bob_message "Thank you..."
show mila oversized_shirt_cheeky_grin
ma "And there is even something poking in my ass"
bob_message "Sorry..."
ma "Don't sweat it"
show mila oversized_shirt_shy_smile
ms "..."
ms "He is kinda obsessed with my ass"
show mila oversized_shirt_cheeky_grin
ms "Hehe"
bob_message "I posted some of my work on sinterest."
show mila oversized_shirt_shy_open_mouth
ms "It's not like someone can recognize me in his drawings, right?"
ms "It's just a picture..."
show mila oversized_shirt_shy_smile
ms "But it's kinda hot to imagine some anonymous people jerking off on my ass..."
bob_message "And received a lot of positive comments"
ma "I'm glad"
bob_message "It feels... unearned"
bob_message "I think it's more like your achievement, then mine..."
show mila oversized_shirt_haaa
ms "Haaa..."
ms "For fuck sakes, Bob..."
show mila oversized_shirt_pout
ms "I should support him somehow..."
show mila oversized_shirt_cheeky_grin
ms "\"Inspire\", huh?"
ms "Like Lee?"
show mila oversized_shirt_shy_smile
ms "..."
ms "I still have the schoolgirl outfit..."
show mila oversized_shirt_cheeky_grin
m "Huh."
play sound "shot.mp3"
scene 127_spread_selfie with flash
ma "Here's some inspiration for you"
ma "{image=bob/selfies/127_spread_selfie_low.webp}"
scene bg bedroom with fade
bob_message "Oh wow..."
bob_message "What an ass..."
show mila schoolgirl_cheeky_grin at center:
    xpos 0.6
ms "..."
ma "Wanna give it a good squeeze?"
bob_message "I want to spank it"
show mila schoolgirl_shy
ms "..."
ms "Our arousal made us rougher with words"
show mila schoolgirl_slight_smile
ms "But I would be lying if I say that I don't like it"
show mila schoolgirl_masturbating
ms "I put my hand under my skirt and squeezed my clitoris"
show mila schoolgirl_pain_pinch
m "Ouch..."
ms "The pain cleared my mind a little, but then left pleasant echoes"
show mila schoolgirl_shy
m "Damn, I want to fuck..."
ms "I feel like a schoolboy with spermotoxicosis"
show mila schoolgirl_slight_smile
ms "All of my thoughts are about sex..."
m "Okay, let's watch Bob's videos..."
scene 127_porn_1 with fade
ms "..."
m "Bob, it's time for the next chapter of \"Mila is watching your favorite porn\"."
ms "..."
m "I can't help but notice that all the girls in your videos are quite petite"
m "Cool outfit by the way"
ms "..."
scene 127_porn_2 with dissolve
m "Let me guess"
m "It will be anal again?"
m "I can't deny it - it certainly looks beautiful."
m "But what's the fun?"
scene 127_porn_3 with dissolve
ms "..."
m "Oh wow"
m "That a huge anal plug!"
scene 127_porn_4 with dissolve
m "..."
m "It looks so depraved when your ass is stretched out like that..."
m "She even trying to smile, poor soul..."
scene 127_porn_5 with dissolve
ms "..."
ms "For a split second I imagined myself in the girl's place"
ms "Paul's words couldn't escape his mind."
m "I would like to be fucked like that..."
scene 127_porn_6 with dissolve
show mila schoolgirl_surprised at center:
    xpos 0.6
m "!"
ms "Did I say that out loud?"
show mila schoolgirl_shy
m "..."
show mila schoolgirl_slight_smile
ms "So what?"
ms "Bob already knows that I'm a slut"
ms "..."
show mila schoolgirl_cheeky_grin
ms "Hehe"
scene 127_porn_7 with dissolve
m "Holly smokes..."
m "..."
m "Are you kidding me?"
m "Oh poor girl..."
m "I can't even imagine what it feels like to be so full"
ms "Despite the fact that what happened on the screen was brutal and rude"
ms "I lowered my hand down and began to caress myself"
m "*shlick shlick shlick*"
ms "Along with growing excitement, I watched the girl on video"
scene 127_porn_8 with dissolve
ms "Her expression changed..."
ms "And then she dug her nails into the back of one of the men and screamed"
ms "Her leg muscles tensed, she held her breath, and then convulsed."
ms "I stopped the video and sent Bob my comments."
scene bg bedroom with fade
show mila schoolgirl_surprised at center:
    xpos 0.6
m "Wow..."
show mila schoolgirl_biting_lips
ms "I've never seen such a strong orgasm"
ms "I couldn't get this orgasm scene out of my head."
m "Is it fake?{w} Or it is really possible to have an orgasm from ass fucking, I wonder?"
m "..."
show cg 127_anus_rub with moveintop
ms "I myself didn't notice how my fingers had already begun to stroke the anus ring."
hide cg with moveoutbottom
show mila schoolgirl_slight_smile
m "Heh"
m "If he is so obsessed with asses..."
m "I need to take another photo for Bob."
play sound "shot.mp3"
scene 127_fingering_selfie with flash
ms "..."
show mila schoolgirl_shy at center:
    xpos 0.6
ma "{image=bob/selfies/127_fingering_selfie_low.webp}"
ma "I don't know about 14cm, it's difficult to put even one finger in."
bob_message "Oh wow, Mila!"
bob_message "Love it!"
bob_message "That's an amazing picture!"
bob_message "I'm so horny right now, oh fuck..."
scene bg bedroom with fade
show mila schoolgirl_biting_lips at center:
    xpos 0.6
ms "He is so excited over this picture..."
ms "It's kinda cute..."
bob_message "Was it painful?"
show mila schoolgirl_slight_smile
ma "Not really"
ma "More like... unpleasant?"
show mila schoolgirl_pout
ma "To be honest, I don't get it, it's just uncomfortable..."
ma "I think that anal orgasm you see in porn is a myth."
ms "Bob didn't answer for a while"
bob_message "You are right and wrong at the same time..."
bob_message "There is no other orgasm other than the clitoral one."
bob_message "At least that's what doctors say."
bob_message "And yet anal sex can be extremely pleasant"
bob_message "Because it stimulates your pussy from a very unusual angle"
show mila schoolgirl_slight_smile
ms "We have an anal expert here..."
show mila schoolgirl_cheeky_grin
ms "Should I call you anal sensei from now on?"
ma "Somehow I doubt it"
bob_message "Wanna bet?"
show mila schoolgirl_shy
ms "..."
ms "I almost agreed."
ma "I'm afraid to imagine how exactly you will prove it...{image=emoji/sweat.webp}"
bob_message "I may not look like it, but all girls I've been with said that I am really good at anilingus"
show mila schoolgirl_embarassed
bob_message "I would love to introduce you to my tongue instead of your fingers and lick you from head to toe one day"
bob_message "This is a great photo, Mila, thank you."
ma "{image=emoji/shy.webp}"
ms "..."


label hscene_2nd_drawing_session:
scene evening with fade
pause 1
scene bg apartments with dissolve
bob_message "I'm home."
show mila schoolgirl_shy at center:
    xpos 0.6
ms "I know"
ms "I heard you come in"
ma "I'm coming"
ms "..."
show mila schoolgirl_slight_smile
ms "I think I've acquired some kind of superpowers."
ms "Before, I didn't pay attention to what was happening outside the apartment."
ms "And now I hear Bob getting ready for work and returning home."
ms "..."
ms "I looked at myself."
show mila schoolgirl_biting_lips
m "I'll probably go like this..."
m "At the same time, I can return this outfit."
show mila schoolgirl_thinking
ms "..."
m "Perhaps I should have washed it first?"
m "Although..."
show mila schoolgirl_slight_smile
m "I think he'll like it even more if I don't"
ms "..."
ms "Already at the door my eyes caught on the high-heels"
show mila schoolgirl_thinking
ms "Lately I've been feeling pretty confident in them."
m "Bob probably won't mind if I wear them, right?"
bob_message "Are you coming soon?"
show mila schoolgirl_haaaa
ms "Yeah, yeah, I'm coming"
show mila schoolgirl_biting_lips
ms "Bob is so persistent...{w}{image=emoji/heart.png}"
ms "I need to hurry"
play sound "door-open-close.mp3"
scene bg doors with fade
show mila schoolgirl_oops at center:
    xpos 0.6
ms "..."
ms "Oops"
ms "I forgot my keys."
ms "..."
play sound "knock.mp3"
scene 127_drawing_event_1 with fade
m "H-hello"
bob "..."
scene 127_drawing_event_2 with dissolve
m "I forgot my keys."
bob "..."
m "..."
scene 127_drawing_event_3 with dissolve
m "Erm..."
m "Can I come in?"
bob "Oh yeah, sorry."
bob "I got a little starstruck"
scene 127_drawing_event_4 with dissolve
m "Ahah"
m "I decided to get you back the outfit too, so I came in it."
bob "..."
m "Well, I'm coming in!"
"..."
scene 127_drawing_event_5 with fade
bob "What are you doing?"
scene 127_drawing_event_6 with dissolve
m "Hm?"
scene 127_drawing_event_7 with dissolve
m "Undressing?"
bob "..."
scene 127_drawing_event_8 with dissolve
m "By the way, I really liked your drawing."
scene 127_drawing_event_9 with dissolve
m "I don't know why you put yourself down so much"
scene 127_drawing_event_10 with dissolve
m "Should I take off the stockings?"
m "..."
scene 127_drawing_event_11 with dissolve
m "Bob?"
bob "..."
scene 127_drawing_event_12 with dissolve
m "Heeeeey"
bob "Sorry...{w} I didn't expect you to take off your clothes..."
scene 127_drawing_event_13 with dissolve
m "Oh..."
scene 127_drawing_event_12 with dissolve
m "Should I get dressed then?"
bob "No no!{w} Everything is fine"
scene 127_drawing_event_14 with dissolve
m "..."
scene 127_drawing_event_11 with dissolve
m "So what should I do?"
bob "I don't know..."
bob "Can you show me some cool gymnastics pose?"
scene 127_drawing_event_15 with dissolve
m "Hmmm..."
ms "It's good that I recently stretched."
scene 127_drawing_event_12 with dissolve
m "I don't want to fall, so I'll take off the heels, ok?"
scene 127_drawing_event_16 with fade
m "Let me try..."
scene 127_drawing_event_17 with dissolve
m "..."
bob "Holy shit..."
scene 127_drawing_event_18 with dissolve
m "Cool, huh?"
bob "Can I take a photo?"
m "PLease do, I'm already at my limit actually"
play sound "shot.mp3"
ms "I was possessed by some strange excitement"
ms "Bob's admiration and gaze made me want to show off."
ms "Lately I haven't had many opportunities to show what my body is capable of."
scene 127_drawing_event_19 with fade
m "..."
bob "Holy shit!"
play sound ["shot.mp3", "shot.mp3", "shot.mp3", "shot.mp3"]
"..."
ms "How many photos is he going to take?"
scene 127_drawing_event_20 with fade
ms "Suddenly it became hot in the room"
ms "All this exercising made me sweaty"
m "..."
m "How do you like my stretching?"
bob "Holy shit, I didn't think some of those poses were even possible"
scene 127_drawing_event_21 with dissolve
m "The human body is amazing, if you have the desire, anything can be stretched"
m "..."
scene 127_drawing_event_22 with dissolve
ms "The second meaning of the last phrase dawned on me"
ms "My ass clenched in fear in anticipation of a possible stretch"
scene 127_drawing_event_23 with dissolve
m "Hmm..."
scene 127_drawing_event_20 with dissolve
m "What's next?{w} I am kind of tired of heavy poses"
m "Let's do something less extreme"
ms "Bob turned red, breathing heavily."
scene 127_drawing_event_22 with dissolve
ms "I clearly saw the bulge in his pants"
ms "But my excitement and my last date with Paul gave me strength and courage"
ms "Bob devoured me with his eyes"
ms "And knowing his preferences, I wanted to tease him even more."
scene 127_drawing_event_24 with dissolve
m "I bet you want to look at my ass, right?"
bob "Bob swallowed"
m "Here you go"
scene 127_drawing_event_25 with fade
m "..."
m "Do you like my ass?"
bob "..."
m "Bob... don't be silent"
play sound "shot.mp3"
scene 127_drawing_event_26 with dissolve
m "I can stay in this position for a long time, you could just start drawing."
bob "I... Hmm"
ms "Bob's voice sounded hoarse and he cleared his throat."
bob "I was afraid of missing some details..."
m "Oh!{w} Details are very important!"
scene 127_drawing_event_26a with dissolve
ms "Arousal clouded my mind"
m "You can spread my ass to see \"the details\" better, if you want"
ms "Bob gulped"
ms "He came near me"
ms "Oh my gosh, he is so huge..."
ms "His pants were bursting from inside"
scene 127_drawing_event_27 with dissolve
ms "Bob tenderly put his hand on my ass cheek"
ms "I felt his finger almost touch my pussy"
ms "I barely managed to hold back a moan"
bob "You are so sexy, Mila..."
scene 127_drawing_event_28 with dissolve
ms "I am so horny right now...{w} If he lowers his pants and puts it inside..."
ms "His huge fat cock would tear my pussy apart..."
ms "I just need to push him a little more..."
ms "Come on...{w} Spread my cheeks..."
scene 127_drawing_event_29 with dissolve
m "So you can see the details better?"
ms "My voice cracked"
ms "Bob stared at my pussy and ass, breathing heavily "
ms "My pussy was leaking, and Bob could feel my wetness with his fingers"
scene 127_drawing_event_30 with dissolve
ms "I was like a bitch in heat..."
ms "Come on Bob, just fuck me already"
bob "Mila...{w} I think we should stop..."
bob "I'm barely holding..."
ms "He took his hands off me and leaned back"
scene 127_drawing_event_31 with dissolve
ms "..."
ms "His words brought me to my senses"
ms "What is happening with me?"
ms "I almost couldn't control myself just now..."
scene 127_drawing_event_32 with fade
ms "I still was aroused as hell"
ms "And embarassed"
ms "That's why I grabbed a pillow to hug.{w} As a shield..."
scene 127_drawing_event_33 with dissolve
m "Hmm...{w} Tomorrow is the last day, right?"
bob "...{w} Yes"
ms "Fuck, I wanna see how much he will cum..."
scene 127_drawing_event_34 with dissolve
m "Erm... If you want, I can come again and you can jerk off on my naked body"
ms "That sounds so lewd..."
bob "..."
ms "Bob was silent"
scene 127_drawing_event_35 with dissolve
m "You don't like the idea?"
ms "I felt insulted"
bob "I think...{w} I got a promotion"
scene 127_drawing_event_36 with dissolve
m "You did?{w} Already?!"
ms "I thought it would take him much longer..."
bob "I went to an interview with our competitors..."
bob "They pay more there.{w} Not much more, but still"
bob "I was somehow afraid to post my resume before..."
bob "I thought that if the boss found out, we would have an unpleasant conversation..."
bob "But to be honest, I don't care anymore..."
bob "Thanks to you, I guess..."
scene 127_drawing_event_33 with dissolve
ms "I noticed that Bob was now talking in a different manner"
ms "His voice changed.{w} He talks in shorter sentences and more confident..."
ms "My pussy clenched in anticipation."
ms "He got a promotion..."
scene 127_drawing_event_37 with dissolve
ms "Which means...{w} Tomorrow"
bob "In general, I wrote a statement, but it will officially come into force in a couple of weeks."
bob "True, I was called to talk to HR"
bob "I'll have to put up with their chatter for a bit."
bob "..."
bob "Does this count?"
scene 127_drawing_event_32 with dissolve
m "Hmmm..."
scene 127_drawing_event_33 with dissolve
m "What do you think?"
ms "Bob winced"
bob "*Sigh*"
bob "Well, of course not..."
m "..."
scene 127_drawing_event_36 with dissolve
m "Why not?"
m "I think it counts"
ms "Bob looked at me in surprise."
bob "What?"
scene 127_drawing_event_37 with dissolve
m "It is enough to bring a signed rental agreement as proof."
m "Or some other papers"
m "Or a bonus paycheck"
m "Or you can bring nothing, really."
m "Just your word is enough for me."
bob "I could lie, you know."
scene 127_drawing_event_38 with dissolve
m "You sure can"
m "But I believe you."
m "I believe in you, Bob."
ms "He smiled."
ms "A strange expression crept onto his face - a mixture of embarrassment and confusion."
bob "Um...{w} That means,{w} tomorrow..."
scene 127_drawing_event_37 with dissolve
m "Yeah."
m "Tomorrow I'm all yours."
bob "..."
m "Good night Bob"
bob "..."
if _in_replay:
    return


scene bg bedroom with fade
"..."
ms "When Paul returned home, I told him that Bob had fulfilled the third condition."
show mila slutty_serious at center:
    xpos 0.6
m "..."
show paul suit_blush_looking_aside at left
p "So, long story short, tomorrow you two will have sex"
show mila slutty_idle
m "...{w} Yes..."
show paul suit_sad
p "Hmm..."
show mila slutty_concerned
m "Paul, I'm not sure I can stop after this..."
m "Today I had trouble controlling myself"
m "It's like I'm possessed by some lustful entity"
show mila slutty_serious
m "If I continue to indulge it...{w}It may consume me"
m "I'm not sure I'll ever be able to get rid of it in the future..."
show paul suit_smirk
ms "Paul looked at me seriously"
p "And I don't want you to stop"
m "..."
show mila slutty_suspicious
m "Will...{w} Will your love stay the same afterwards?"
show paul suit_sad
p "..."
p "No."
show mila slutty_tearing_up
m "..."
show paul suit_grin
p "I will love you even more"
show mila slutty_tearing_up_smile
m "I love you too."
show paul suit_smirk
p "..."
m "Paul..."
m "Do you want to have kids?"
show paul suit_shock
p "Wow, jumping to another topic..."
show mila slutty_tearing_up_grin
m "I suddenly wanted to get pregnant"
show paul suit_open_mouth_neutral
p "Huh"
p "Not yet."
p "I thought about it.{w} Earlier"
show paul suit_blush_looking_aside
p "And now... I want something a little different..."
show paul suit_grin
p "Plus...{w} I got some ideas..."
show mila slutty_frown
m "Ideas?{w} What ideas?"
show paul suit_smirk
p "I will tell you later."
m "You know that I hate it when you do that"
p "But I still don't want to tell anything yet."
show paul suit_grin
p "All I can say is that I'm sure you'll like the idea."
show mila slutty_suspicious
m "OK, I guess..."
p "By the way, I watched yesterday's video"
show mila slutty_idle
m "You did?{w} And how...{w} How was it?"
show paul suit_smirk
p "Gorgeous."
show mila slutty_giggle
p "You are a real whore"
p "Best porn of my life"
show mila slutty_idle
m "Do you want more?"
show paul suit_blush_looking_aside
p "..."
p "Yes"
scene 127_mila_morning with fade
ms "I didn't sleep well again."
ms "This time it was me chasing monsters with big dicks"
ms "I caught them and fucked them. And I still couldn't cum"
scene bg bedroom with fade
show mila slutty_concerned at center:
    xpos 0.6
ms "I glanced at the clock"
play sound "ticking.mp3"
"*tic*{w}*tok*{w}*tic*{w}*tok*"
show mila slutty_haaaa
m "Haaaa"
show mila slutty_frown
ms "I shouldn't look at the clock, it makes time go slower..."
m "Why the hell do I do this every..."
show mila slutty_serious
ms "I looked at the clock"
m "Two minutes"
m "..."
show mila slutty_haaaa
m "Fuck."
m "I looked again."
show mila slutty_idle
m "..."
ma "How's it going?"
bob_message "Busy"
show mila slutty_haaaa
m "Haaaa..."
show mila slutty_frown
m "I hate waiting"
m "..."
show mila slutty_idle
m "I'll go freshen up in the shower"
"..."
scene 127_b-day_shower with fade
play sound "shower.mp3"
ms "Hot streams of water brought me back to my senses a little"
ms "For several minutes I just stood and enjoyed the sensations"
ms "I'm afraid to imagine what state Bob is in..."
jump a127_bday_branch

label after_the_bday:
    scene bg doors with fade
    play sound "door-open-close.mp3"
    ms "..."
    show mila nude_new_shy at right
    ms "I was so tired that I didn't even think to start worrying when I left the apartment completely naked."
    ms "Ultimately, it's three o'clock in the morning and there won't be anyone there anyway."
    ms "The cool night air felt scalding."
    scene bg door with fade
    play sound "door-open-close.mp3"
    show mila nude_new_shy at right
    ms "It seemed to me that I was all on fire."
    ms "My head was spinning from fatigue."
    scene 127_b-day_shower with fade
    play sound "shower.mp3"
    ms "With the last of my strength, I went into the shower and rinsed off."
    scene bg apartments with fade
    ms "When I finished and was leaving the bathroom I saw, that Paul was waiting for me in the living room"
    show mila robe_excited_and_shy at right
    ms "His excited and worried look put a smile on my face"
    m "I'm home..."
    ms "I really wanted to sleep.{w} The room swayed before my eyes."
    p "How are you?"
    m "I..."
    m "I think I overdid it a little."
    scene 129_faint with hpunch
    play sound "body-fall.mp3"
    ms "The room turned on its side and went dark."
    p "Sweetheart! Darling!"
    ms "I heard Paul's voice from afar and fell into sweet bliss."
    ms "Sleep...{w} I want to sleep so bad..."

label after_faint:
jump not_yet

label not_yet:
scene under_constr
play music anthem
"Sorry, this is the end of this path for this version :("
"But I am working my ass off to make more :)"
"Check out {a=https://subscribestar.adult/addont}my subscribe star page{/a} to know the latest news"
jump end


label end:
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
