label RebeccaEventOne:
    play sound walk
    scene black with Dissolve(2)
    play music ["audio/blueboi.mp3", "audio/sideroad.mp3", "audio/closure.mp3"] fadeout 1.0 fadein 1.0
    scene 32-6 gym 1 with Dissolve(1)
    "Anna entered the gym and immediately felt motivated to have a very good workout."
    "Rebecca was already there with her succulent breasts heaving in the air."
    "Anna couldn't deny that Rebecca was a very beautiful big sister."
    a "{i}...Both of us seem to have inherited very curvacious bodies from our mom..."
    a "Hey, Rebecca. I'm sorry I'm a bit late..."
    r1 "Anna! I'm so glad to see you. Don't worry, I already started to change."
    scene 32-6 gym 2 with Dissolve(1)
    if CarlHelps == True:
        r1 "Even though it's been just a couple of hours, I've missed you."
        a "Oh, don't be like that, I'm always there when you need me and vice-versa."
        r1 "Always, dear Anna."
    r1 "How has your day been so far?"
    a "Oh... You know... It's has had its fair share of moments already."
    r1 "Care to share? I'm curious about your life. Always have been."
    a "Nothing too exciting, though. Just work and some other things..."
    if GoodBadDoctorChoice == 2:
        "Anna was reluctant to tell Rebecca about her 'interesting' examination at the doctor's office."
    scene 32-6 gym 3 with Dissolve(1)
    "Anna was wondering if she should talk about her day at the office."
    $ config.menu_include_disabled = False
    menu:
        "I had an argument with Diane again!" if dianaGoodRelations == False:
            a "She is so vile towards me and I don't even really know why..."
            r1 "Oh, well. She's just probably jealous of you. Going up in the world."
            a "I don't really want to talk about her."
            a "Also, there is a corporate party in the works... And I forgot to choose a dress!"
            r1 "Oh, Anna. I will have to take you shopping, then. You have to look irresistible."
            a "Rebecca... Stop it... Haha."
        "Had a nice chat with Diane and the colleagues." if dianaGoodRelations == True:
            a "Their planning to throw a party at Diane's place."
            a "Also, there is a corporate party in the works... And I forgot to choose a dress!"
            r1 "Oh, Anna. We will have to go shopping then. You have to look irresistible."
            a "Rebecca... Stop it... Haha."
        "Anna decided not to talk about her office drama.":
            a "Anyway. I'm just focusing on work right now, a lot of stuff to do."
    r1 "You got the promotion, right?"
    a "Yeah. I'm pretty excited as to how it will turn out. Hopefully I can earn more money."
    a "And take care of Andrew's condition."
    r1 "You're still on about him? Anna. Get your mind right about him..."
    r1 "He's cost us a lot of pain. And I, sure as hell, am not forgiving him..."
    play sound undress
    scene 32-6 gym 4 with Dissolve(1)
    a "I understand you... But still..."
    r1 "I'm not going to lecture you on what to do in your life, but a word of advice:"
    r1 "If you decide to help him with the surgery, do it, but after that just forget about him..."
    r1 "He's nothing but trouble. A guy who first needs to learn how to live his own life without screwing others over..."
    a "I guess there is some truth to those words."
    r1 "Yeah, I know."
    scene 32-6 gym 5 with Dissolve(1)
    r1 "But... Look at that outfit. Even I'm hardly able to resist, Anna."
    a "Oh, yeah, something that I had stored away for these situations."
    r1 "Well, all I can say is that you've got taste, honey."
    r1 "All the guys at the gym will have difficulty concentrating, I bet."
    a "Haha... Talk about difficulty concentrating, Rebecca. You are the definition of desirable."
    r1 "Now your just talking nonsense. Hehe..."
    a "I'm not. Haha."
    scene 32-6 gym 6 with Dissolve(1)
    "Both of them had finished the dressing room small talk and now it was time to get to work."
    r1 "So, do you have anything in mind for today? Any specific exercises?"
    a "Umm... I've been out of practice, lately. I'm still thinking."
    a "I could do some leg workouts today, you know? Squats and such."
    r1 "Read my mind."
    scene 32-6 gym 7 with Dissolve(1)
    r1 "Look at these guys go. Definitely strong, don't you think?"
    a "What? I'm sorry I wasn't listening."
    r1 "Oh, that proves my point exactly. Haha."
    a "I'm thinking since we've come here once, perhaps we should make this a regular thing?"
    r1 "That is an absolutely perfect idea. We won't get those gains if we don't do it consistently."
    a "Right."
    scene 32-6 gym 8 with Dissolve(1)
    "Rebecca was giving the guys seductive looks. But that was Rebecca's demeanor. She usually did those things."
    "But the guys had already caught on, seeing two absolutely irresistible women."
    "Walking around in such sexy, sporty outfits."
    gym1 "Damn, look at those two."
    gym1 "Absolute fucking knockouts, both of them..."
    scene 32-6 gym 9 with Dissolve(1)
    gym2 "Focus on my set dude, You're my spotter!"
    gym2 "I'm barely benching the last rep and... You're looking at some girls."
    gym1 "Oh, sorry. You looked like you got it all covered."
    gym2 "Just, help me out, will you?"
    scene 32-6 gym 10 with Dissolve(1)
    a "So, How are things back at home with Carl?"
    r1 "Oh, the usual. We are all good. But I'm curious about you."
    r1 "Are you doing alright, all things considered?"
    a "It's hard. I will be honest... But we women often have to deal with those things..."
    r1 "'Hard'... Hehe..."
    r1 "I'm sorry, Anna. Carry on."
    a "I'm just trying to be hopeful that all this blows over soon and we can get back to normal lives."
    a "I have plenty of things to worry about..."
    scene 32-6 gym 11 with Dissolve(1)
    "As they were stretching they were discussing the details of Anna's life."
    r1 "All of this could've been avoided if not for Andrew..."
    a "Yeah, I know. That is one of the things I have to deal with. But I have to do it on my own."
    r1 "I understand, Anna. Just know that I'm here for you..."
    a "Thanks, sis, I know that."
    if TaxmanHelps == True:
        a "After the evening with at Sergey's I was going home and I was arrested..."
        r1 "What??? By the investigator?"
        a "Yes... I won't go into heavy details right now, but I got a guy who got me out..."
        r1 "Maybe you should have called Carl?"
        a "I don't want to put you in danger..."
        r1 "I see, thanks, Anna. But who helped you out?"
        a "Just a friend who knows the law..."
        r1 "So you've made some good friends in the city, huh?"
        a "You could say that."
    scene 32-6 gym 12 with Dissolve(1)
    gym2 "Yeah, you were right about them. Total 10s. Don't often see these kinds of girls in this gym."
    gym1 "I know right? Maybe we should 'help' them with their workout?"
    gym2 "As if we are any professionals."
    gym1 "Perhaps we could get their numbers, you know?"
    gym2 "First I have to finish my benchpress."
    scene 32-6 gym 13 with Dissolve(1)
    a "And when I fix those recent issues, I will finally be able to focus on work properly and get things done."
    a "My new promotion comes with certain perks. I want to earn as much as possible, you know? Go on a vacation as well."
    r1 "Ah... Yes... Somewhere warm, preferably with palm trees. Haha..."
    a "Exactly, I just want to get away from all of this for some time..."
    if SergeySexContent == True:
        a "And perhaps go with Sergey..."

    r1 "You're still on about that? Perhaps you're just slutty, Anna... Haha..."
    r1 "Not that there is anything wrong with it, you know?"









    scene 32-6 gym 14 with Dissolve(1)
    r1 "That's enough stretching, let's get to work, huh?"
    a "Alright, but it looks like that rack is still taken."
    r1 "Don't worry. A little bit of me and they won't be able to resist. Haha..."
    a "Oh you devilish minx. You're always ready to get what you want by any means necessary."
    r1 "You know me well."
    play sound surprise
    scene 32-6 gym 15 with Dissolve(1)
    r1 "Hey guys, I was just wondering if you are still going to anything on this rack?"
    r1 "We just want to do some squats and I wondered if you would allow us, two beautiful ladies, to do them?"
    gym1 "I'm... Sure... We can do that, sure..."
    r1 "Thanks. I appreciate that."
    scene 32-6 gym 16 with Dissolve(1)
    gym1 "I was also wondering if you need a spotter, perhaps?"
    gym1 "You know, I could also give you some tips and stuff."
    gym2 "Right, like you, did when spotting me..."
    gym1 "Shut it, dude. Haha."
    gym1 "He's just joking."
    r1 "I think we will be alright, won't be lifting heavy."
    scene 32-6 gym 17 with Dissolve(1)
    gym1 "Sure, your loss, honey..."
    gym1 "Help me get those plates off, man!"
    gym2 "Yeah, got it."
    "Anna was not saying anything and just letting Rebecca take care of everything."
    "She was, meanwhile thinking about other things."
    if CarlSexContent == True:
        "She was thinking about her session with Carl and how that seemed rather wrong but felt so good..."
    if SergeySexContent == True:
        "Recalling the amazing evening with Sergey, even if it was ruined by the detective..."
    if TaxmanFootjob == True:
        "Remembering the interesting session with the taxman and his obsession with her legs and feet."
    r1 "Thanks a lot guys."
    gym1 "You bet."
    scene 32-6 gym 18 with Dissolve(1)
    r1 "Anyway, now that we have the floor, I guess we should do a warm-up set."
    a "Yeah, It's been a while, but I think I still remember the basics."
    r1 "Well, You were always the sportier one."
    a "It used to help me take my mind off of things."
    a "I will go first, alright?"
    r1 "Yeah, absolutely, Anna."
    scene 32-6 gym 20 with Dissolve(1)
    "Anna got into position, back straight, ass out."
    "It felt natural, and her mind stopped worrying immediately."
    a "{i}...Alright, I think I got the hang of this. Just warm up set..."
    scene 32-6 gym 21 with Dissolve(1)
    "Anna was putting in the effort, feeling strong and confident."
    a "{i}...Alright, a couple of more reps. This feels great..."
    "The guys were checking out Anna's form and ass, of course."
    gym1 "Damn, This girl got some nice curves... That ass..."
    "The guy was whispering to his friend."
    gym2 "I know... Amazing... It's always great to see girls squatting."
    scene 32-6 gym 22 with Dissolve(1)
    "Deep squats, getting the glutes and quads involved effectively."
    "The guys watching were as involved in her workout as was Anna."
    gym1 "{i}...Damn, I would so go to town on her..."
    gym1 "{i}...She has amazing form, too... I love it when girls workout..."
    gym1 "{i}...So fucking hot..."
    scene 32-6 gym 23 with Dissolve(1)
    "Anna finished her set and felt exhilarated."
    a "That was great. I feel so good already. Hehe..."
    r1 "I know! Let me go next. I need to get those glutes workin'..."
    a "Sure, the floor's yours, Rebecca."
    scene 32-6 gym 24 with Dissolve(1)
    r1 "Can't let my sister take all the spotlight, hehe..."
    a "I couldn't do that, even if I tried."
    r1 "Right... If you'd see how the guys were looking at you..."
    r1 "Tell me, is my form correct?"
    a "Yeah, it's good. Keep going."
    scene 32-6 gym 25 with Dissolve(1)
    r1 "Well? Is my ass bigger already?"
    a "Haha... You wish..."
    r1 "Well, my confidence is bigger, definitely."
    a "Couldn't agree more. I feel great."
    a "So... Let's add some weight now?"
    r1 "Are you sure that we should add weight already?"
    a "Yeah, won't put much."
    scene 32-6 gym 26 with Dissolve(1)
    "While Anna and Rebecca were prepping weights, King had arrived."
    k1 "Hey, guys. Slacking off in the gym again? Haha..."
    gym2 "Oh, cmon dude, give us a break. We won't look like you anyway."
    k1 "Well, perhaps not like me, but we can all always improve ourselves."
    k1 "Never compare yourself to others. That's an insult to you."
    gym1 "Wise words from an 'actor'... Haha..."
    k1 "Hey, listen. No need to be rude, got it? There is already unnecessary stigma around us."
    k1 "And most of which is untrue. Got it?"
    gym1 "Yeah... Alright..."
    scene 32-6 gym 27 with Dissolve(1)
    "Anna was doing her second set and was very focused and motivated."
    "Pushing herself with ever repetition."
    "King immediately noticed that it was Anna."
    k1 "{i}...Anna? I could recognize those thighs and ass anywhere..."
    play sound surprise
    scene 32-6 gym 28 with Dissolve(1)
    k1 "Hey, girls. Looking good."
    a "King? What are you doing here... Give me a second to finish..."
    k1 "Absolutely, workout comes first."
    r1 "King? Who's this handsome gentleman, Anna?"
    scene 32-6 gym 29 with Dissolve(1)
    a "Umm, This is a colleague from Dilan's shoots. I recently met him."
    a "What are you doing here? We haven't had much time to get acquainted."
    k1 "No worries, there's always time for that."
    if DilanPornShoot == True:
        k1 "We will, of course, get to know each other later on, if you know what I mean..."
        a "That would be nice, I like to know my co-workers."
    a "Anna? Introduce me?"
    scene 32-6 gym 30 with Dissolve(1)
    a "Oh, Sorry. This is my lovely sister Rebecca."
    k1 "Pleasure... Pleasure, indeed."
    k1 "{i}...Look at those curves..."
    if DilanPornShoot == True:
        k1 "{i}...Mmm... I wonder if I could score them both..."
    r1 "Definitely a gentleman, What's your name?"
    k1 "People just call me King."
    r1 "Very nice to meet you, King... Hehe..."
    k1 "Anyway, By the looks of it, you girls are doing squats today?"
    r1 "Yeah, it's my turn by the way..."
    k1 "Please, the floor's yours."
    scene 32-6 gym 31 with Dissolve(1)
    "Rebecca got into position and tried to be extra succulent because she seemed to like King."
    "She wanted to get his attention..."
    k1 "{i}...Damn... She's one fine lady..."
    k1 "You got great form, but we can always make it a bit better."
    k1 "If, I may?"
    r1 "Absolutely... I will take all the help I can get."
    scene 32-6 gym 32 with Dissolve(1)
    "King got closer to Rebecca and started to lead her."
    k1 "On the down movement tried to go slower. Eccentric movement requires slower momentum. Feel the muscle, squeeze it."
    k1 "And when you go up, try explosive strength, and exhale as you go up."
    k1 "It helps both mentally and physically."
    r1 "Oh, you know your stuff, huh?"
    "Anna also was paying attention, but it seemed that King was paying a lot of attention to Rebecca."
    scene 32-6 gym 33 with Dissolve(1)
    k1 "Excellent. As you come down, squeeze the muscle, feel the tension. And remember to go slow."
    r1 "Like this?"
    k1 "Yes, exactly. You've got great form. And great structure. It's good to work with people who pay attention."
    "It looked like Rebecca was enjoying herself a lot. King was doing his best to leave a good impression."
    "And he was succeeding..."
    a "{i}...Rebecca really seems into it now..."
    r1 "Damn it's getting a bit too heavy..."
    k1 "Just a little bit lower. I will help you."
    scene 32-6 gym 34 with Dissolve(1)
    "King pushed close to Rebecca with his crotch... And she didn't mind..."
    k1 "Let me just adjust your posture a bit. To get most effectiveness."
    k1 "With time you will become proficient and won't need anyone behind you."
    k1 "Do you feel it? Do you feel the squeeze?"
    r1 "Yeah... but it's tough..."
    k1 "Remember to push a bit. But don't overdo it, if it's your first training..."
    r1 "Ok..."
    "Anna was feeling a bit jealous, King wasn't giving her this kind of attention..."
    k1 "And now let's go up. I got you."
    scene 32-6 gym 35 with Dissolve(1)
    k1 "Yeah, just like that..."
    k1 "You are doing great..."
    r1 "{i}...Oh... This man knows what he's doing..."
    r1 "{i}...I'm already getting hot..."
    "King had started to touch Rebecca's breasts, but she didn't mind, in fact, she was enjoying it..."
    r1 "{i}...Keep going... Ah..."
    r1 "{i}...Maybe I should try something with him..."
    scene 32-6 gym 37 with Dissolve(1)
    r1 "Ouch... I think I hurt myself a bit..."
    k1 "Perhaps you overdid it..."
    k1 "Did you warm-up and stretch?"
    r1 "Yeah... I think I just got a bit carried away..."
    k1 "Ah...It's understandable. What's hurting?"
    r1 "I think I strained my hamstring a bit..."
    k1 "Ah... No worries, I can help with that as well..."
    k1 "I can massage it for you if you wish?"
    r1 "Really? Sure... That would help a lot..."
    scene 32-6 gym 38 with Dissolve(1)
    a "Will you be alright?"
    r1 "Absolutely. I trust that King will take good care of my hamstring..."
    k1 "Just to make sure, I'm a certified physician in my free time as well."
    r1 "Really? That's very interesting."
    k1 "Yeah, so I will do my best to ease your pain..."
    r1 "Alright, We will be going... Take care, Anna."
    if DilanPornShoot == True:
        k1 "See you at the set... Alright? We can talk more then."
        k1 "Don't worry, I will take good care of your sister."
    a "Sure guys, I'll just finish here and stretch a bit."
    scene 32-6 gym 39 with Dissolve(1)
    a "{i}...What just happened?..."
    a "{i}...He didn't help me with my sets... Bastard..."
    a "{i}...Well played, sister..."
    a "{i}...Well played..."
    r1 "{i}...I see that Anna is a bit jelly..."
    if CarlSexContent == True:
        r1 "{i}...Since she had some fun with Carl, I will do the same with her friend... hehe..."
    "Anna was dumbfounded... She could see that Rebecca was enjoying King's presence."
    if DilanPornShoot == True:
        "But she didn't know King well and this would have been a good time to get to know him."
        a "{i}...Oh well, I guess I will just have to find some time to talk to him at the set..."
    "Anna finished her workout and put the plates back in their place."
    scene 32-6 gym 40 with Dissolve(1)
    "Her workout was over as well, just to stretch out and warm down after the vigorous workout."
    a "{i}...I hope Rebecca will be alright... And since he is a physician she should be fine..."
    if DilanPornShoot == True:
        a "{i}...Just got to stretch out and get going... Will have to talk to him later..."
        a "{i}...It's today... So I have to be on my A-game..."
    scene 32-6 gym 41 with Dissolve(1)
    a "{i}...This was a very nice workout... Perhaps I should make it a regular thing..."
    a "{i}...Perhaps I could even meet King here again... He could give me some useful tips..."
    a "{i}...This has really helped me take my mind off of things..."
    a "{i}...And I've made some physical progress in the process..."
    scene 32-6 gym 42 with Dissolve(1)
    a "Alright, just a little bit more, and then I have to get going."
    a "{i}...I wonder if King will fix Rebecca's hamstring before I leave..."
    "Anna was doing the last stretching exercise to release the tension in the muscles. For better recovery."
    a "{i}...Ok, this is enough... I should get going..."
    scene 32-6 gym 43 with Dissolve(1)
    gym1 "Hey, You're done already?"
    a "It's enough for the first time."
    gym2 "We're glad that there are good-looking girls, such as yourself, coming to the gym."
    gym1 "I hope that you come here again some time."
    a "Well, I'm thinking of making it a habit, so perhaps. Hehe..."
    gym1 "Awesome... I mean, great... That's good for you..."
    a "I will get going. Bye."
    gym1 "Take care."
    play sound door2
    scene 32-6 gym 44 with Dissolve(1)
    "The workout had been very exhilarating and did well for Anna's thoughts."
    "She had some time to lay off all the problems but also get clear-headed as to what to do."
    a "{i}...Ah... Very nice, now for a good shower and then I have to get going..."
    a "{i}...Rebecca must be in the shower already..."
    play sound undress
    scene black with Dissolve(1)
    "Anna undressed and went to the showers."
label ShowerFuck:
    scene 32-6 gym 45 with Dissolve(1)
    "She was checking if they were empty, but..."
    "She heard some talking. A low voice and a female voice."
    a "{i}...I wonder what's that about..."
    "As she was entering the showers she saw..."
    play sound surprise
    scene 32-6 gym 46 with Dissolve(1)
    "Rebecca and it was clear that King was in there with her."
    "Anna couldn't get a good look yet, but she was surprised."
    a "{i}...Wait, is Rebecca with King?..."
    "Multiple questions filled Anna's mind."
    a "{i}...Is she up to no good?..."
    play sound shower3
    scene 32-6 gym 47 with Dissolve(1)
    k1 "You've got some amazing tits, Rebecca."
    r1 "Why, thank you... I can see that you like them... From down there..."
    k1 "I know... Would you like to touch it?"
    r1 "Would I? Yes!"
    scene 32-6 gym 48 with Dissolve(1)
    "Anna was witnessing all of this unfold..."
    if CarlSexContent == True:
        "But she couldn't be completely surprise because of what she had done herself..."
        "With Carl..."
    r1 "Oh, it feels so large in my hand... I'm getting hot..."
    k1 "Let me tell you, babe... You are already hot..."
    k1 "I just craved you the moment I saw you in the gym..."
    if DilanPornShoot == True:
        "Anna heard their conversation and was a bit jealous..."
        "She was supposed to work with him later on in the day..."
        a "{i}...Oh, you cheeky bastards... Alright, alright... hehe..."
        "Anna was plotting her revenge on King..."
        "She was going to torture him during the porn-shoot..."
    scene 32-6 gym 49 with Dissolve(1)
    r1 "Oh... You sexual monster... Haha..."
    r1 "And you are probably very good in bed... Knowing the fact that you're an actor..."
    k1 "Well... I was even before all of that... I'm a natural... Heh..."
    r1 "And very confident. I like that."
    scene 32-6 gym 50 with Dissolve(1)
    k1 "Come here. I want you... I want you hard, Rebecca..."
    r1 "Oh... Please... Don't keep me waiting... I want you, too."
    "The tension in the shower room was increasing. Rebecca was very aroused and ready."
    "King just wanted to fuck that perfect pussy..."
    play sound surprise
    scene 32-6 gym 51 with Dissolve(1)
    "He quickly turned Rebecca around."
    k1 "Are you ready? Do you want to be fucked by my hard cock?"
    "She felt his stiff tool pressing against her butt cheeks."
    r1 "Yes... Please, penetrate me..."
    "King went closer to her ear and whispered something to her."
    k1 "Ce sera une excellente baise..."
    r1 "Oh... You know French?"
    k1 "Yes... Je vais baiser ta chatte, salope."
    scene 32-6 gym 52 with Dissolve(1)
    "Without any more hesitation, King entered Rebecca's snatch."
    "And it welcomed his dick with open arms..."
    r1 "Oh... Fuck... That feels amazing..."
    k1 "Yeah... Your pussy is mesmerizing..."
    r1 "Go faster, please..."
    k1 "My thoughts exactly."
    play sound moaningone
    scene 32-6 gym 53 with Dissolve(1)
    "They had started to fuck vigorously."
    "Anna felt rather interesting. She was also a bit horny."
    "And their passionate fucking wasn't helping her."
    a "{i}...They are so loud as well... Rebecca..."
    a "{i}...What do I do now? Should I watch?..."
    scene 32-6 gym 54 with Dissolve(1)
    "Anna couldn't just look away. She was into it..."
    "She liked what she saw... It was so full of emotion..."
    a "{i}...They look so hot while fucking... Oh..."
    a "{i}...I'm starting to get horny as well..."
    play sound moaningtwo
    scene 32-6 gym 55 with Dissolve(1)
    "King grabbed Rebecca for more grip and control."
    "She was completely under his power."
    "And she liked it..."
    r1 "{i}...Oh... Fuck me... He is so good..."
    r1 "Fuck me... Yes... It's so good... Ah..."
    scene 32-6 gym 56 with Dissolve(1)
    "King was fucking like a bull. Without stopping..."
    "Pure thrusting in and out."
    "Rebecca was getting that dick hard. And she wanted nothing less..."
    "Completely spaced out in pleasure. She wanted to be rammed like this..."
    a "{i}...She is so into it... This is weird... What about Carl..."
    if CarlSexContent == True:
        a "{i}...But then again... Can't say that Carl is any better..."
        a "{i}...Or that I'm any better... Oh... This is very interesting..."
    scene 32-6 gym 57 with Dissolve(1)
    "The penetration was deep and satisfying for both of them."
    "King was surprised as to how well her pussy was taking his cock."
    k1 "{i}...This girl is so fucking hot... I'm having difficulty focusing..."
    "He felt that it was slowly closing in, but he wasn't about to let someone beat him."
    "For King it was about going longer, being better, doing it faster..."
    r1 "Ah... This is fucking amazing..."
    r1 "Your cock... It's so great... Ah..."
    scene 32-6 gym 58 with Dissolve(1)
    "King picked her leg up."
    k1 "Give me your tongue..."
    r1 "Call me your bitch, please..."
    k1 "I want to kiss you, slut..."
    r1 "Ah...."
    "They were kissing passionately."
    play sound [moaningtwo, moaningthree] fadein 0.5
    show RebeccaKingFuckOne
    "They're intercourse was full of sexual energy."
    "Rebecca was in ecstasy. Enjoying the full length of King's cock."
    r1 "Ah... I can't believe how good it is... ah..."
    r1 "Fuck me harder, King! Please..."
    "Anna was so hot from watching that, it was hard to look away."
    "The moans could be heard throughout the entire locker room and showers."
    scene 32-6 gym 59 with Dissolve(1)
    hide RebeccaKingFuckOne
    "Ohh my God... So good..."
    k1 "Tu aimes ça, salope?"
    r1 "Huh? Your french is so hot..."
    k1 "You like it, slut?"
    r1 "Yes!!! I love it..."
    k1 "Your so hot... I love your fucking curves, I would wanna fuck you so long..."
    play audio moaningtwo
    play audio jerk
    scene 32-6 gym 60 with Dissolve(1)
    "Anna could hear everything and had become really horny."
    "She had started to touch herself lightly... She hadn't even noticed. She was doing it involuntarily..."
    a "{i}...Oh... Rebecca... You dirty slut... I love it..."
    a "{i}...King is pretty hot too actually..."
    a "{i}...Whispering some dirty things in French. Who knows what he's saying..."
    "Anna was overtaken by all those thoughts..."
    play sound [moaningthree, moaningtwo] fadein 0.5
    show RebeccaKingFuckTwo with Dissolve(1)
    "The penetration was heavenly for Rebecca..."
    "It felt so hot for her. She had no idea the day will turn out like this..."
    r1 "Ah... Fuck me harder..."
    k1 "As you wish..."
    "King was penetrating her faster and deeper."
    scene 32-6 gym 61 with Dissolve(1)
    "Rebecca's and King's fucking had reached its peak... They were fucking with embellishing moans and heavy breaths."
    "Rebecca felt intertwined with King... In a sex-induced high."
    r1 "Fuck... My pussy... King... Oh..."
    k1 "Ah... Yeah... I love it..."
    r1 "Fuck me, fuck me, fuck me..."
    play audio jerk2
    play audio moaningthree
    show RebeccaKingFuckThree with Dissolve(1)
    hide RebeccaKingFuckTwo
    "The climax was starting to build up..."
    "King felt as if he was reaching his threshold..."
    "... And so was Rebecca..."
    "She couldn't hold herself any longer."
    r1 "Fuck... I'm getting so close... Oh my god..."
    r1 "King... Ah..."
    play sound moaningtwo
    k1 "Yeah... I'm getting close, too!!"
    k1 "Ahhh... You want my cum?"
    r1 "Yes!! Give it all to mee, I'm coming aahhh..."
    menu:
        "Cum inside her pussy.":
            r1 "Ahh... I'm CUMMIINGGG!!!"
            with flash
            k1 "Fuck me tooo!!! OHHH..."
            r1 "Flood me with your cum!!"
            with flash
            with flash
            k1 "FUUUUCKK."
            k1 "Prends ma putain de sperme!!"
            scene 32-6 gym 62 with flash
            k1 "Ah..."
            "King was filling up Rebecca's hole with his ejaculate."
            "It was leaking all over the place..."
        "Cum on her face.":
            play sound jerk
            r1 "Aah.. Fuck..."
            k1 " Get on your knees!"
            scene 32-6 gym 63 with flash
            r1 "Yess... rain on me!!!"
            r1 "Ahh.. Cum on me..."
            with flash
            k1 "Ahhh!!!"
            with vpunch
            with flash
            k1 "FUUUUCKK."
            scene 32-6 gym 64 with Dissolve(1)
            k1 "Oh shiiit..."
    "It took them a while to come down from the hot session."
    "They were both very drained, almost as if King had met his match."
    "The great actor was impressed by Rebecca's skill."
    scene black with Dissolve(1)
    play sound shower3
    "They both washed off."
    scene 32-6 gym 65 with Dissolve(1)
    r1 "I have to admit... That was absolutely amazing..."
    r1 "I'm still feeling sensation on my body."
    k1 "Yeah, I won't lie. You've got some amazing moves, Rebecca."
    r1 "Well, I can only say the same about you..."
    k1 "You are on par with some of my co-stars... Even better than them..."
    k1 "Haven't had such an amazing session in some time."
    k1 "Ok, I guess I should leave before somebody sees us here."
    scene 32-6 gym 66 with Dissolve(1)
    "Anna barely got herself together as King was walking out."
    "She acted as if she didn't know anything..."
    a "Oh... King? What are you doing in here?"
    k1 "I must have mixed up the showers, sorry. Haha..."
    a "Right..."
    if DilanPornShoot == True:
        k1 "Anyway, see you on set later today?"
        a "Umm... Yeah... Sure..."
        a "{i}...I feel so weird now that he fucked my sister..."
    else:
        k1 "Anyway, see you around?"
        a "Yeah... Sure, King..."
    play sound shower2
    scene 32-6 gym 67 with Dissolve(1)
    r1 "Sooo. How was the rest of your workout?"
    a "It was good. I stretched and was done..."
    a "How is your 'hamstring', Rebecca?"
    r1 "Umm... It's much better, King did me good..."
    a "Sorry, what did you say?"
    r1 "Oh, nothing, he helped me and fixed the problem, yeah..."
    a "Mhm... Hehe..."
    play sound shower2
    scene black with Dissolve(1)
    "Anna washed..."
    scene 32-6 gym 68 with Dissolve(1)
    "She came back and Rebecca was getting dressed, slowly..."
    r1 "So... What do you think about King?"
    a "He seems nice enough..."
    r1 "Yeah, he has a very nice 'personality'... Did you know he speaks French?"
    a "{i}...Yeah, I know... I heard everything, you naughty girl... Hehe..."
    a "No... Really? That's cool. Haha."
    play sound undress
    scene 32-6 gym 69 with Dissolve(1)
    r1 "Anyway, I will have to get going now. I've got a couple of things to do..."
    a "Yeah, likewise. I still have plenty to do today..."
    r1 "Well... Don't let me keep you..."
    r1 "But hey, we should come here again, what do you think?"
    a "I think that it's a great idea... And I would love to come here again and workout..."
    r1 "Yeah... Me too... Workout..."
    play sound walk
    scene black with Dissolve(2)
    play sound phonecall
    scene anna city walking with Dissolve(1)
    "As Anna was walking she got a call from Emily."
    e "Anna? Hey what are you doing?"
    a "Just heading home from a workout."
    e "Awesome. I was wondering if you could help me with something."
    a "Ok?"
    e "I'm looking for a sex shop. I thought that maybe you know a place?"
    a "Yeah. it's in the shopping district, I will send you the location."
    e "Haha... My girl. Would you also want to join me?"
    a "Sure. Why not."
    jump SexShopEventOne
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
