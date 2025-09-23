
label EP10_Alfred_Shop:
    play sound door2
    play music PPMEtheralEternity
    scene 38-6 cloth 1 with Dissolve(1)
    a2 "And so, we've reached a pivotal point."
    a2 "I will get in contact with my agent."
    a2 "This should be a great opportunity for us all!"
    play sound surprise
    scene 38-6 cloth 2 with Dissolve(1)
    a2 "Ah. Anna."
    a2 "Good to see you."
    a2 "How you've been?"
    a "You know, same old same old."
    a "How's the garden?"
    a2 "Flourishing!"
    play sound whoosh_1
    scene 38-6 cloth 3 with Dissolve(1)
    a "Hiii, Patricia!"
    p2 "Hello!"
    p2 "How are you, Anna?"
    a "Good, good. You?"
    p2 "Even better, now, haha."
    scene 38-6 cloth 4 with Dissolve(1)
    a "So. What's up?"
    a2 "I've got good news."
    a2 "I'm going to a big fashion show..."
    a "Niiice! Congratulations!"
    a2 "And... I've been given a chance to show off a lingerie set."
    a2 "For that I need a very beautiful and confident woman."
    a "Oh? Have you found her?"
    a2 "If you agree, then yes."
    $ EP10_Alfred_menu_1_var_1 = False
    $ EP10_Alfred_menu_1_var_2 = False
    menu EP10_Alfred_menu_1:
        "Is it a big show?" if EP10_Alfred_menu_1_var_1 == False:
            a2 "It is, indeed. A lot of high profile fashion icons will attend."
            a2 "And the lingerie is of a set that is highly sought-after."
            a2 "I just need the right model for it. People will be falling over each other to see it."
            $ EP10_Alfred_menu_1_var_1 = True
            jump EP10_Alfred_menu_1
        "How revealing is the lingerie?" if EP10_Alfred_menu_1_var_2 == False:
            a2 "Well, none of the sensitive areas are uncovered, but it is rather promiscuous."
            a2 "I'm rather sure that you will like it."
            a2 "It's truly amazing."
            a "I see."
            $ EP10_Alfred_menu_1_var_2 = True
            jump EP10_Alfred_menu_1
        "Let's do it!":
            a2 "WONDERFUL!"
            pass
    scene black with Dissolve(1)
    scene 38-6 cloth 5 with Dissolve(1)
    a2 "Alright, I will get it for you."
    a "I'm excited, actually."
    a2 "That is very good indeed."
    scene 38-6 cloth 6 with Dissolve(1)
    a2 "You can go in there. I will be with you in a second."
    if AlfredRelationship == True:
        play sound undress
        scene black with Dissolve(1)
        play audio surprise2
        scene 38-6 cloth 7 with Dissolve(1)
        a2 "Oh... Um..."
        a2 "I didn't think you'd be undressed already."
        a "Nothing to worry about."
        a2 "Very nice view..."
        scene 38-6 cloth 8 with Dissolve(1)
        a2 "Here. The outfit."
        a "Thank you, let's see what you've got..."
        a2 "You are as lovely as always."
    play sound cloth_sound1
    scene black with Dissolve(1)
    play sound jacketcloth
    "Minutes later..."
    play sound surprise
    scene 38-6 cloth 9 with Dissolve(1)
    a2 "I... I'm... I've not one word in my mouth..."
    a "Oh, stop it..."
    a2 "Truly, magnificent."
    a "You really think so?"
    scene 38-6 cloth 10 with Dissolve(1)
    a2 "Anna... This is the extremly-rare 'Envisage Ambrosia' set."
    a2 "It's truly... I've been keeping it a secret. It's as rare as diamonds, I could say."
    a2 "Sought after by the richest of men."
    a2 "Only five were ever made. Each given to 5 royal families by Klaus Koppenham himself."
    a2 "It was his way of expressing that none, even the highest of people are out of reach of seduction and lust."
    a2 "They say it was woven from silk made by black widows..."
    a "WHAT?"
    a2 "Crazy stories, I know."
    a2 "PATRICIAAA!!!!"
    a2 "COME AT ONCE!"
    play sound surprise
    scene 38-6 cloth 11 with Dissolve(1)
    a2 "Just look at this..."
    p2 "Oh. my..."
    p2 "Stunning..."
    scene 38-6 cloth 12 with Dissolve(1)
    p2 "We definitely found our model."
    a "Really think so?"
    p2 "It's like the designer made it for you."
    play sound jacketcloth
    scene black with Dissolve(1)
    scene 38-6 cloth 13 with Dissolve(1)
    a2 "So, how about it?"
    a2 "You willing to participate?"
    a "Yeah... Definitely..."
    a2 "YES!"
    a2 "You are a lifesaver, Anna."
    scene 38-6 cloth 14 with Dissolve(1)
    a "When's the show?"
    a2 "Very soon. In a couple of days."
    a "Oh?"
    scene 38-6 cloth 15 with Dissolve(1)
    a2 "Yeah, you've alleviated my worries now."
    a2 "I'm so excited..."
    a2 "Don't worry. You will also be handsomely rewarded."
    a "That's the last thing on my mind."
    scene 38-6 cloth 16 with Dissolve(1)
    "Thank you for this opportunity."
    a2 "No... Anna, thank you."
    p2 "Thank you from me, too."
    scene 38-6 cloth 14 with Dissolve(1)
    p2 "The old man was driving me crazy from worries. Haha."
    a2 "Sorry, my dear."
    p2 "Don't worry, I can handle you."
    a "Alright, guys. I will be running. Got other things to take care of."
    scene 38-6 cloth 15 with Dissolve(1)
    a2 "Of course. Good luck. And see you soon."
    $ EP10_var_8 = True
    if DilanPornShoot == True:
        jump EP10_Dilan_Tablet
    else:
        jump EP10_Bath
label EP10_Dilan_Tablet:
    pause 0.5
    scene black
    scene 37-3 dilan 1 with Dissolve(1)
    a "Hey!"
    d3 "Hey, Anna."
    d3 "Good to see you again."
    d3 "I just wanted to let you know that you can come to the second pornshoot today."
    scene 37-3 dilan 2 with Dissolve(1)
    a "Is that so?"
    d3 "Yeah. We can shoot it right away. Everything is ready."
    a "Nice!"
    $ EP9_5_porn_1 = True
    $ EP10_var_2 = True
    if EP9_5_var_5 == False:
        jump EP9_5_PoolBoy_1
    else:
        jump EP10_HarshTreatment
label EP10_HarshTreatment:
    play sound carsound3
    pause 1
    play music closuresong
    scene black
    scene 37-10 harsh 1 with Dissolve(1)
    "Anna and Dilan arrived at the location before everyone else."
    d3 "I'm glad you decided to choose Harsh Treatment today with me."
    scene 37-10 harsh 2 with Dissolve(1)
    d3 "I will let you know that, as the name implies, it's a harsher type of a scene."
    a "I understand."
    d3 "Don't worry, though. It's not going to be anything too extreme."
    d3 "Still, If you feel like it's too much, just let me know. We can stop at any time."
    d3 "Alright, I've notified you, that's all I can do."
    d3 "So this will be our filming location."
    a "This seems like a nice place to live."
    scene 37-10 harsh 3 with Dissolve(1)
    d3 "Well, I think it's for sale. Now that you're getting these higher grade jobs."
    d3 "Trust me. You will only get more and more money from each new opportunity."
    d3 "Anyway. I've got a simple yet cool outfit in the other room, you can go change there."
    play sound door2
    scene 37-10 harsh 4 with Dissolve(1)
    "Anna entered the room."
    d3 "{i}...I hope she is ready for this scene..."
    d3 "{i}...It's a little more intense..."
    scene black with Dissolve(1)
    "Some time later..."
    play sound door2
    scene 37-10 harsh 5 with Dissolve(1)
    a "How do I look?"
    d3 "Exactly as a clothes shop owner would."
    d3 "I think you are familiar with the premise of this shoot?"
    a "Yeah, I read the description."
    d3 "Turn around for me?"
    scene 37-10 harsh 6 with Dissolve(1)
    a "How is it?"
    d3 "What do you think?"
    d3 "It's as good as always."
    d3 "Anna, You never disappoint with your looks."
    scene 37-10 harsh 7 with Dissolve(1)
    $ EP10_menu_1_var_1 = False
    $ EP10_menu_1_var_2 = False
    $ EP10_menu_1_var_3 = False
    menu EP10_menu_1:
        "So... Who are the other actors?" if EP10_menu_1_var_1 == False:
            scene 37-10 harsh 8 with Dissolve(1)
            d3 "You've never met them."
            d3 "But they are from the agency I work with."
            d3 "Dan and Terry."
            d3 "They are usually involved in these 'harsher' movies."
            d3 "So they know what they are doing."
            a "I see."
            $ EP10_menu_1_var_1 = True
            jump EP10_menu_1
        "Do you have any other ideas coming up?" if EP10_menu_1_var_2 == False:
            scene 37-10 harsh 8 with Dissolve(1)
            d3 "I do, actually."
            d3 "I've got two more scenes getting prepped by the agency and they are already looking for models."
            d3 "I put your name forward as the first on the list."
            d3 "So there will be more jobs coming soon."
            d3 "And one of them is paying very, very well."
            scene 37-10 harsh 9 with Dissolve(1)
            a "That is great to hear. I will be waiting for you call."
            scene 37-10 harsh 8 with Dissolve(1)
            d3 "Count on it."
            $ EP10_menu_1_var_2 = True
            jump EP10_menu_1
        "That's all.":
            pass
    play sound door2
    scene 37-10 harsh 10 with Dissolve(1)
    d3 "Here they are."
    d3 "Hello!"
    porn1 "Hello to you, too, Dilan."
    porn2 "Hey, everyone!"
    scene 37-10 harsh 11 with Dissolve(1)
    d3 "So. This is Anna. you will be working together today."
    porn1 "Well, well."
    scene 37-10 harsh 12 with Dissolve(1)
    porn1 "I'm profoundly honored to meet you, Anna."
    porn1 "I've heard many, many great things about you."
    porn1 "It's a pleasure. I'm Dan."
    a "Oh, Hah. Hello, Dan. The feeling's mutual."
    scene 37-10 harsh 13-1 with Dissolve(1)
    porn2 "{i}...The tits..."
    scene 37-10 harsh 13-2 with Dissolve(1)
    porn2 "{i}...The ass..."
    porn2 "{i}...She is a vision..."
    scene 37-10 harsh 14 with Dissolve(1)
    d3 "Are you ready?"
    a "As ready as I will ever be."
    scene 37-10 harsh 15 with Dissolve(1)
    d3 "Alright, guys."
    d3 "Let's get started. How about you both just get settled in and prepare."
    d3 "Anna and I will start the scene outside."
    porn1 "Sure, we will check out the place and be ready when you need us."
    d3 "Great."
    play sound door2
    scene 37-10 harsh 17 with Dissolve(1)
    scene black with Dissolve(1)
    scene 37-10 harsh 18 with Dissolve(1)
    d3 "So, we will start the scene here. You've been called over to discuss the details of your deal with the loansharks."
    a "Alright, should be easy enough."
    d3 "Say some stuff about it out loud as keep moving, alright?"
    a "Got it!"
    d3 "AAAND... ACTION!"
    play music SexyTimeSong5
    scene 37-10 harsh 19 with flash
    a "I still don't have all the money for them..."
    a "I hope they will just give me another payment plan that I could pay off..."
    a "The business hasn't been doing as good as I hoped..."
    scene 37-10 harsh 20 with Dissolve(1)
    a "Well, here goes. I hope they are in a good a mood."
    scene 37-10 harsh 21 with Dissolve(1)
    d3 "Good. Great. Let's move towards the door, you will knock on the door, and Dan will open it."
    a "Got it."
    play sound doorknock
    scene 37-10 harsh 22 with Dissolve(1)
    porn1 "Coming!"
    porn1 "The girl is here, Terry. We got 'business' to attend to, heh."
    scene 37-10 harsh 23 with Dissolve(1)
    a "Hello, there. Dan."
    scene 37-10 harsh 24 with Dissolve(1)
    porn1 "OH, Anna. Hello. I'm glad you're here..."
    a "May I come in?"
    porn1 "Of course, we called you over, didn't we?"
    scene 37-10 harsh 25 with Dissolve(1)
    porn1 "Come in, then. And let's get down to business."
    scene 37-10 harsh 26 with Dissolve(1)
    porn1 "Get comfortable, we have to discuss the details of this business..."
    a "Alright..."
    "Anna was feeling a bit uneasy. Like she had just walked into the lion's den."
    scene 37-10 harsh 27 with Dissolve(1)
    porn2 "Ah, Hello, Anna."
    porn2 "It's been a while."
    porn2 "I remember when we made the deal. You came to me desperate..."
    porn2 "Well... Not really."
    porn2 "More like, very eager. Wanting to open your own clothing shop and clothing line."
    porn2 "How is it going?"
    a "Not, well..."
    scene 37-10 harsh 28 with Dissolve(1)
    porn2 "I see. Well, sorry to hear that, but do you have the money that I loaned you?"
    a "..."
    porn2 "Do you?"
    a "No..."
    porn2 "Do you remember what was our deal if you couldn't pay back on time?"
    a "Yes..."
    porn2 "For each missed deadline, you will come here and get punished..."
    a "Well. If you would give me a bit more time..."
    porn2 "Punished... Sexually..."
    scene 37-10 harsh 29 with Dissolve(1)
    porn1 "And you signed it so fast, so eagerly..."
    porn2 "If I remember correctly, you were so sure that it would work out that you said that you're not even worried."
    a "Umm..."
    porn1 "Well, then. Come on..."
    scene 37-10 harsh 30 with Dissolve(1)
    a "I... But... I need a bit more time."
    porn1 "You will have a new deadline after today."
    porn1 "But for now, Let's take off that jacket."
    play sound jacketcloth
    scene 37-10 harsh 31 with Dissolve(1)
    a "Oh..."
    porn1 "Yeah! That's what I'm talking about!"
    a "Is there no other way we can reason?"
    porn2 "You agreed to the deal, didn't you?"
    a "Yeah..."
    porn2 "Made a rash decision, now you pay the price."
    scene 37-10 harsh 32 with Dissolve(1)
    a "But, sir. I beg of you, give me a couple of weeks. That's all I'm asking."
    porn2 "We haven't gotten this far in the business by being soft."
    porn2 "You've got to understand that. Otherwise everyone would be walking all over us."
    a "Well, I understand that."
    scene 37-10 harsh 33 with Dissolve(1)
    porn2 "Therefore, It's time to 'pay up', If you know what I mean."
    a "{i}...Shiet, I've gotten in deep this time..."
    "Our poor Anna had made a bad judgment call... When she agreed to it, she knew the risksc..."
    "But it seemed so unrealistic. Her plan seemed so foolproof..."
    scene 37-10 harsh 34 with Dissolve(1)
    porn1 "Now you get punished!"
    a "Wha..."
    play sound surprise2
    stop music
    scene 37-10 harsh 35 with vpunch
    porn2 "You think we weren't serious when we made that a part of the deal?"
    a "I... I thought it was just a joke..."
    porn2 "We wouldn't joke about such things with such a hot lady."
    a "Ahh..."
    scene 37-10 harsh 36 with Dissolve(1)
    porn2 "Now then."
    a "Ok... I will comply..."
    porn2 "First, we will have some fun here. See the 'goods'"
    play music SexyTimeSong3
    play sound undress
    scene 37-10 harsh 37 with Dissolve(1)
    a "Was... Ah..."
    a "Was touch me in inapporporiate places also part of the agreement?"
    porn2 "Of course."
    porn2 "Shouldn't have agreed to our terms."
    a "I..."
    "Anna had consented to that..."
    "But it didn't go her way..."
    play sound woman_surprise
    scene 37-10 harsh 38 with Dissolve(1)
    a "Uaah..."
    porn2 "You are the sexiest woman that has ever come to get a loan from us."
    "Their reactions were genuine cause they hadn't seen her naked in real life, yet."
    scene 37-10 harsh 39 with Dissolve(1)
    "Anna was a bit worried..."
    "But something in all of this was also causing her to get excited..."
    "She thought to herself..."
    a "{i}...Why did I sign it so rashly..."
    a "{i}...I wonder, how harshly will they punish me..."
    "She was a bit curious..."
    play sound surprise
    scene 37-10 harsh 40 with Dissolve(1)
    pause 1
    play sound jacketcloth
    scene 37-10 harsh 41 with Dissolve(1)
    a "Oh..."
    "She was starting to feel a rush of excitement..."
    "Perhaps her decision was not so rash at all..."
    "Perhaps a part of her wanted to know, what would happen..."
    "She hadn't taken risks in her life, and a part of her wanted to discover something different..."
    porn2 "Come on. Lick it!"
    play sound jerk
    show EP10_Harsh_Treatment_Anim_9 with Dissolve(1)
    porn2 "Fuck..."
    pause 1
    show EP10_Harsh_Treatment_Anim_8 with Dissolve(0.7)
    $ check_scene_numbers_amount = 2
    $ scene_animation_speed = 1
    show screen Scene_Animation_Controller("EP10_HarshTreatment_1",
    ["images/other/Episode_10/Harsh_Treatment/37-10 harsh 41.jpg",
    "images/other/Episode_10/Harsh_Treatment/37-10 harsh 45.jpg"],
    ["Lick", "Suck"], [1, 2])
screen EP10_HarshTreatment_Blowjob():
    zorder 300
    if scene_animation_parameter == 0:
        add "EP10_Harsh_Treatment_Anim_9"
    if scene_animation_parameter == 1:
        if scene_animation_position == 1:
            if scene_animation_speed == 1:
                add "EP10_Harsh_Treatment_Anim_1"
            if scene_animation_speed == 2:
                add "EP10_Harsh_Treatment_Anim_1_Faster"
        if scene_animation_position == 2:
            if scene_animation_speed == 1:
                add "EP10_Harsh_Treatment_Anim_2"
            if scene_animation_speed == 2:
                add "EP10_Harsh_Treatment_Anim_2_Faster"
label EP10_HarshTreatment_Blowjob:
    show screen EP10_HarshTreatment_Blowjob with Dissolve(0.3)
    hide EP10_Harsh_Treatment_Anim_9
    hide EP10_Harsh_Treatment_Anim_8
    porn2 "Take my good cock!"
    porn2 "Good stuff... Shit!"
    pause
label EP10_HarshTreatment_1:
    scene 37-10 harsh 43
    hide screen EP10_HarshTreatment_Blowjob with Dissolve(0.5)
    hide screen Scene_Animation_Controller with Dissolve(0.5)
    play sound surprise2
    a "Mmmh..."
    "Anna's face was pushed onto Terry's cock..."
    "She had barely any control..."
    "But her resistance was futile... Or did she barely try to resist at all..."
    "It seemed as if she wanted them to take advantage of her."
    scene 37-10 harsh 44 with Dissolve(1)
    porn1 "Yeah! Take that cock in your mouth!"
    porn1 "This is your punishment..."
    a "Mmmm..."
    porn1 "She is barely resisting..."
    porn2 "Either she is enjoying it, or is very compliant with our deal."
    porn2 "Fuck it, who cares... Ah!"
    scene 37-10 harsh 45 with Dissolve(1)
    a "Mmm..."
    "Anna's head was being pushed on the cock."
    "She wasn't given even a second of rest."
    play sound undress
    scene 37-10 harsh 46 with Dissolve(1)
    pause 1
    play sound jacketcloth
    scene 37-10 harsh 47 with Dissolve(1)
    "He tore off Anna's panties."
    "Pulled her face off of his cock."
    porn2 "Now... Time to get even more involved with your 'punishment', Anna."
    a "Oh..."
    play sound surprise
    scene 37-10 harsh 48 with Dissolve(1)
    play sound lighthit
    scene 37-10 harsh 49 with Dissolve(1)
    "Anna was thrown on the sofa."
    scene black with Dissolve(1)
    pause 0.5
    scene 37-10 harsh 50 with Dissolve(1)
    porn1 "Let's get to it."
    a "Oh..."
    a "{i}...These dicks are truly making me feel things..."
    "She thought to herself... Crazy how the punishment was getting her riled up."
    scene 37-10 harsh 51 with Dissolve(1)
    porn2 "This is where the fun begins."
    a "Please, be gentle, mister..."
    porn2 "Oh... I will, hehe."
    play sound cloth_sound1
    scene 37-10 harsh 52 with Dissolve(1)
    "Anna was flipped over once again."
    "On all fours."
    "And without hesitation..."
    play sound surprise2
    scene 37-10 harsh 53 with vpunch
    "The man pushed his erect penis in Anna's face."
    "Immediately deepthroating her."
    play sound jerk3 loop
    show EP10_Harsh_Treatment_Anim_3 with Dissolve(1)
    pause
    a "MMM...!!!"
    porn1 "That's right..."
    porn1 "Perfect!"
    play audio female_moan_5
    show EP10_Harsh_Treatment_Anim_4 with Dissolve(1)
    hide EP10_Harsh_Treatment_Anim_3
    pause
    pause
    stop sound

    scene 37-10 harsh 54 with Dissolve(1)
    hide EP10_Harsh_Treatment_Anim_4
    a "Gulp..."
    play sound jerk2
    scene 37-10 harsh 55 with Dissolve(1)
    a "MMmmm..."
    "She was chocking hard on it."
    "Small breaths... Just enough not to pass out."
    play sound female_cough_1
    scene 37-10 harsh 56 with Dissolve(1)
    "He suddenly released her mouth."
    a "Bhaaa..."
    a "Khe... Khem..."
    "Anna was coughing and breathing heavily."
    porn1 "Your mouth... It's like it was meant to be fucked."
    a "Is that enough?"
    porn2 "Nowhere near, girl."
    scene 37-10 harsh 59 with Dissolve(1)
    porn2 "How about I have some fun with your backside, huh?"
    a "Ok..."
    "Anna wouldn't admit it, but she was actually enjoying it."
    "At least a part of her was."
    "Some new exciting elements to her life."
    scene 37-10 harsh 60 with Dissolve(1)
    porn2 "Great fucking ass."
    porn1 "Tell me about it."
    porn1 "Feels like this is destiny. For us to fuck this chick."
    porn2 "You could miss a couple more deadlines and become our fuck whore."
    scene 37-10 harsh 61 with Dissolve(1)
    play audio spank3
    show screen delayedplay(0.2, "audio/sounds/female_moan_3.mp3")
    scene 37-10 harsh 62 with vpunch
    a "AH!"
    porn2 "Yeah. Scream for us!"
    scene 37-10 harsh 63 with Dissolve(1)
    porn2 "Now. Where was I..."
    porn2 "Oh yeah. About to fuck this amazing piece of ass."
    "The man didn't want to hesitate."
    play sound jerk2
    $ EP10_HarshTreatment_CrackFuck_var_1 = False
    $ EP10_HarshTreatment_PussyFuck_var_1 = False
    $ EP10_HarshTreatment_Spitroast_var_1 = False
    menu:
        "Give her a nice Crack fuck...":
            scene black
            if EP10_HarshTreatment_CrackFuck_var_1 == False:
                scene 37-10 harsh 60 with Dissolve(1)
                $ EP10_HarshTreatment_CrackFuck_var_1 = True
                porn2 "I think I want to enjoy your ass crack a bit..."
                a "Okey, sir. I will do as you say..."
                $ scene_animation_parameter = 0
        "Put that dick inside of her.":
            scene black
            if EP10_HarshTreatment_PussyFuck_var_1 == False:
                $ EP10_HarshTreatment_PussyFuck_var_1 = True
                porn2 "Fuck it, I wanna get inside of that pussy."
                $ scene_animation_parameter = 1
label EP10_HarshTreatment_Spitroast:
    play sound MoaningNine loop
    play audio jerk
    show screen Scene_Animation_Controller("EP10_HarshTreatment_2",
    ["images/other/Episode_10/Harsh_Treatment/37-10 harsh 63.jpg",
    "images/other/Episode_10/Harsh_Treatment/37-10 harsh 64.jpg"],
    ["Crack Fuck", "Solo"], [2, 1])
    screen EP10_Sex_Scene_HT():
        zorder 300
        if scene_animation_parameter == 0:
            if scene_animation_position == 1:
                add "EP10_Harsh_Treatment_Anim_10"
            if scene_animation_position == 2:
                add "EP10_Harsh_Treatment_Anim_11"
        if scene_animation_parameter == 1:
            if scene_animation_position == 1:
                add "EP10_Harsh_Treatment_Anim_12"
            if scene_animation_position == 2:
                add "EP10_Harsh_Treatment_Anim_12_Faster"
        if scene_animation_parameter == 2:
            if scene_animation_position == 1:
                add "EP10_Harsh_Treatment_Anim_5"
            if scene_animation_position == 2:
                add "EP10_Harsh_Treatment_Anim_6"
            if scene_animation_position == 3:
                add "EP10_Harsh_Treatment_Anim_7"
            if scene_animation_position == 4:
                add "EP10_Harsh_Treatment_Anim_13"
    show screen EP10_Sex_Scene_HT with Dissolve(1)
    pause
    porn2 "Oh... Fuck..."
    a "Ah..."
    porn2 "That's what I AM TALKING ABOUTTTT!!!"
    pause
label EP10_HarshTreatment_2:
    scene 37-10 harsh 64
    hide screen EP10_Sex_Scene_HT with Dissolve(0.5)
    hide screen Scene_Animation_Controller with Dissolve(0.5)
    a "AAhHOOHH..."
    scene 37-10 harsh 65 with Dissolve(1)
    "She felt ecstasy-like feelings take her body."
    a "Ah..."
    a "Just..."
    a "Just be gentle."
    porn2 "Gentle? I'm already fucking you good! Haha!"
    scene 37-10 harsh 66 with Dissolve(1)
    "Out of nowhere, Dan pushed Anna's mouth on his dick yet again."
    a "Mmhh."
    "Now she had become almost airtight."
    "Getting pounded in sync by the two loansharks."
    $ scene_animation_parameter = 2
    $ check_scene_numbers_amount = 4
    play sound moaningfive
    play audio jerk
    show screen Scene_Animation_Controller("EP10_HarshTreatment_3",
    ["images/other/Episode_10/Harsh_Treatment/37-10 harsh 63.jpg",
    "images/other/Episode_10/Harsh_Treatment/37-10 harsh 64.jpg",
    "images/other/Episode_10/Harsh_Treatment/37-10 harsh 65.jpg"],
    ["Crack Fuck", "Solo", "Spitroast"], [2, 1, 4])
    show screen EP10_Sex_Scene_HT with Dissolve(0.5)
    pause
    a "KHaaa."
    a "AHHHH..."
    "Anna's mouth was filled with cock."
    "The men were using her as their personal fuck toy."
    pause
label EP10_HarshTreatment_3:
    hide screen Scene_Animation_Controller
    hide screen EP10_Sex_Scene_HT
    play sound moaningtwo
    scene 37-10 harsh 67 with Dissolve(1)
    pause
    scene 37-10 harsh 68 with Dissolve(1)
    pause 1
    "They pushed off of her."
    porn2 "Get on the ground. On your knees."
    play sound lighthit
    scene 37-10 harsh 69 with Dissolve(1)
    "Anna got on all fours."
    a "Yes... Ah..."
    "She was still breathing heavily from the fucking she just got."
    "Her holes were sore..."
    "But it was not ending yet..."
    porn2 "MOVE!"
    scene 37-10 harsh 70 with Dissolve(1)
    a "Yes, sir..."
    pause 2
    scene 37-10 harsh 71 with Dissolve(1)
    "She crawled as the two men looked at her body."
    "Her holes on display for both of them."
    "She started to enjoy the deprecating actions the two of them were taking against her."
    scene 37-10 harsh 72 with Dissolve(1)
    "She enjoyed being their toy..."
    "A new-found passion of hers."
    "To be someone's sex slave."
    porn2 "Go on, up the stairs. MOVE!"
    scene 37-10 harsh 73 with Dissolve(1)
    pause 3
    play sound surprise
    scene 37-10 harsh 74 with Dissolve(1)
    a "{i}...Whoa..."
    "She hadn't expected something like that."
    scene 37-10 harsh 75 with Dissolve(1)
    porn2 "Prepare to get fucked hard, slut!"
    scene 37-10 harsh 76 with Dissolve(1)
    porn1 "Get in the contraption."
    a "Now?"
    porn1 "YES!"
    porn1 "You still owe us. Remember?"
    play sound handcuffs
    scene 37-10 harsh 77 with Dissolve(1)
    porn2 "Yes... Yes... This is great."
    porn2 "Now you will know to remember to pay us in time..."
    a "Umm... Yes... Sir..."
    porn2 "I can't quite tell if you are enjoying yourself or not..."
    a "I..."
    porn2 "Don't talk! It doesn't really matter."
    play sound handcuffs
    scene 37-10 harsh 78 with Dissolve(1)
    pause
    scene 37-10 harsh 79 with Dissolve(1)
    porn1 "There we go."
    porn1 "This looks perfect."
    a "What are you doing back there?"
    porn1 "Nothing you need to worry about!"
    play sound whoosh
    scene 37-10 harsh 80 with Dissolve(1)
    pause 0.5
    play audio spank1
    show screen delayedplay(0.2, "audio/sounds/femgasp.mp3")
    scene 37-10 harsh 81 with vpunch
    a "AAH!!"
    play sound whoosh
    scene 37-10 harsh 80 with Dissolve(1)
    pause 0.5
    play sound spank3
    scene 37-10 harsh 81 with vpunch
    a "SHIT!!"
    play sound whoosh
    scene 37-10 harsh 80 with Dissolve(1)
    pause 0.5
    play audio spank3
    show screen delayedplay(0.2, "audio/sounds/femgasp.mp3")
    scene 37-10 harsh 81 with vpunch
    a "PLEASE!! Be Gentle..."
    play sound jerk
    scene 37-10 harsh 82 with Dissolve(1)
    porn1 "I told you, this is your punishment..."
    a "Yes, master..."
    scene 37-10 harsh 83 with Dissolve(1)
    "Anna's ass was red from their spanking."
    porn1 "Yeah..."
    porn1 "I love this... Best investment we've made."
    porn2 "Can't argue there."
    "He teased the pussy with his cock a little bit and then..."
    play sound moaningfour
    scene 37-10 harsh 84 with Dissolve(1)
    "Pressed it inside of her."
    a "OH..."
    a "MF..."
    scene 37-10 harsh 85 with Dissolve(1)
    "She was getting engulfed with pleasure."
    porn2 "Damn, I'm pretty sure she actually signed it with the hopes of becoming our fuckslut."
    porn2 "She is enjoying it thoroughly."
    porn2 "Ain't ya."
    a "Fuck..."
    a "AHH!"
    porn2 "Lemme just..."
    scene 37-10 harsh 86 with Dissolve(1)
    porn2 "FUCK YEAH!"
    porn2 "TAKE IT!"
    "Anna was once again airtight."
    "Being fucked from both sides by the sleazy loansharks."
screen EP10_Sex_Scene():
    zorder 300
    if scene_animation_parameter == 0:
        if scene_animation_position == 1:
            if scene_animation_speed == 1:
                add "EP10_Harsh_Treatment_Anim_17"
            if scene_animation_speed == 2:
                add "EP10_Harsh_Treatment_Anim_17_Faster"
        if scene_animation_position == 2:
            if scene_animation_speed == 1:
                add "EP10_Harsh_Treatment_Anim_18"
            if scene_animation_speed == 2:
                add "EP10_Harsh_Treatment_Anim_18_Faster"
    if scene_animation_parameter == 1:
        if scene_animation_position == 1:
            if scene_animation_speed == 1:
                add "EP10_Harsh_Treatment_Anim_14"
            if scene_animation_speed == 2:
                add "EP10_Harsh_Treatment_Anim_14_Faster"
        if scene_animation_position == 2:
            if scene_animation_speed == 1:
                add "EP10_Harsh_Treatment_Anim_15"
            if scene_animation_speed == 2:
                add "EP10_Harsh_Treatment_Anim_15_Faster"
        if scene_animation_position == 3:
            if scene_animation_speed == 1:
                add "EP10_Harsh_Treatment_Anim_16"
            if scene_animation_speed == 2:
                add "EP10_Harsh_Treatment_Anim_16_Faster"
    if scene_animation_parameter == 2:
        if scene_animation_position == 1:
            if scene_animation_speed == 1:
                add "EP10_Harsh_Treatment_Anim_19"
            if scene_animation_speed == 2:
                add "EP10_Harsh_Treatment_Anim_19_Faster"
        if scene_animation_position == 2:
            if scene_animation_speed == 1:
                add "EP10_Harsh_Treatment_Anim_20"
            if scene_animation_speed == 2:
                add "EP10_Harsh_Treatment_Anim_20_Faster"
label EP10_HarshTreatment_Bondage:
    $ scene_animation_parameter = 1
    $ check_scene_numbers_amount = 3
    play audio jerk
    queue sound(female_moan_1, female_moan_2, femmoan_3, female_moan_5, femgasp_1, MoaningNine, femmoan_4, female_moan_4) loop
    show screen Scene_Animation_Controller("EP10_HarshTreatment_End",
    ["images/other/Episode_10/Harsh_Treatment/37-10 harsh 86.jpg",
    "images/other/Episode_10/Harsh_Treatment/37-10 harsh 83.jpg",
    "images/other/Episode_10/Harsh_Treatment/37-10 harsh 96.jpg"],
    ["Front", "Back", "Anal"], [2, 3, 2])
    show screen EP10_Sex_Scene with Dissolve(0.5)
    pause
    porn1 "YEAH. OH Fuck..."
    a "AAHH!"
    play sound female_moan_4
    a "AHH!!"
    pause
    "Anna holes were being used over and over."
    "Stretching the limits of her pleasure."
    "All three of them completely overtaken by pleasure..."
    "Just fucking in front of the camera... Might as well not have it there at all..."
    "They would do it for free... Just for the enjoyment..."
label EP10_HarshTreatment_End:
    play sound jerk3
    menu:
        "Cum in Anna's mouth!":
            show EP10_Harsh_Treatment_Anim_17 with Dissolve(0.5)
            hide screen Scene_Animation_Controller
            hide screen EP10_Sex_Scene with Dissolve(0.5)
            porn2 "AH... FUCK!"
            porn2 "FUCK FUCK!!!"
            porn2 "TAKE MY CUMM!!!"
            with flash_vpunch
            pause 1
            scene 37-10 harsh 91 with Dissolve(1)
            with flash_vpunch
            play sound cum_sound
            a "MMMMMMM!!!MMHHH"
            play sound jerk
            scene 37-10 harsh 95 with Dissolve(1)
            porn1 "Damn, the mess I made..."
        "Cum on her face!":

            show EP10_Harsh_Treatment_Anim_17 with Dissolve(0.5)
            hide screen Scene_Animation_Controller
            hide screen EP10_Sex_Scene with Dissolve(0.5)
            with flash_vpunch
            scene 37-10 harsh 91 with Dissolve(1)
            porn2 "Oh, shit!"
            porn2 "LEMME JUST PAINT YOUR FAAAAACCCEEE!!!"
            scene 37-10 harsh 92 with Dissolve(1)
            porn2 "AH..."
            play audio cum_sound
            with flash_vpunch
            play audio cum_sound
            with flash_vpunch
            scene 37-10 harsh 93 with Dissolve(1)
    play sound moaninglong_1
    menu:
        "Finish inside of her pussy.":
            show EP10_Harsh_Treatment_Anim_14
            hide screen Scene_Animation_Controller
            hide screen EP10_Sex_Scene with Dissolve(0.5)
            with flash_vpunch
            porn1 "OH... OH AAHHH!!!"
            porn1 "I will fill you up so much!"
            play audio cum_sound
            with flash_vpunch
            scene 37-10 harsh 97 with Dissolve(1)
            play audio cum_sound
            with flash_vpunch
            pause 2
            scene 37-10 harsh 98 with flash_vpunch
            a "FUUCK, MY Pussy!"
        "Fill up her Anus!":
            show EP10_Harsh_Treatment_Anim_19
            hide screen Scene_Animation_Controller
            hide screen EP10_Sex_Scene with Dissolve(0.5)
            porn1 "SHIT!"
            porn1 "YOUR ASS IS SO FUCKING GREAT!!!"
            with flash_vpunch
            play audio cum_sound
            scene 37-10 harsh 90 with Dissolve(1)
            with flash_vpunch
            play audio cum_sound
            porn1 "AAHHHHHHH"
            scene 37-10 harsh 96 with Dissolve(1)
    stop sound fadeout 2
    $ renpy.end_replay()
    d3 "AAAND CUT!"
    scene black with Dissolve(3)
    "Anna Cleaned up..."
    play music tranquility fadein 2
    scene 37-10 harsh 100 with Dissolve(1)
    d3 "Well then."
    d3 "I think this shoot was rather amazing, don't you?"
    a "Umm. I never had an experience in this kind of a thing."
    d3 "GREAT, GREAT!!"
    d3 "This will be a banger, I know it!"
    porn1 "Glad we could help..."
    scene black with Dissolve(1)
    "Everyone gets dressed and cleaned up..."
    scene 37-10 harsh 101 with Dissolve(1)
    d3 "Well then, Thank you for today, everyone, You've been awesome."
    d3 "I really could feel the energy at the beginning of how you made Anna into a submissive girl."
    d3 "The acting was pretty decent for a porn film."
    porn2 "So perhaps I've still got a shot at making it big?"
    scene 37-10 harsh 102 with Dissolve(1)
    a "You've already made it big, Haha... I mean, just look at your package..."
    porn2 "Hehe... Fair point."
    porn1 "Alright, we'll be heading out, then."
    d3 "Sure! I will get in contact with you about the 'business' later today."
    porn2 "Got you!"
    play sound door2
    scene 37-10 harsh 103 with Dissolve(1)
    d3 "So, what did you think?"
    a "I've been really enjoying myself lately with these shoots."
    a "Like, all kinds of new things, machines and whatnot."
    d3 "I knew you'd like it!"
    scene 37-10 harsh 104 with Dissolve(1)
    d3 "Plus the cash... Heh."
    d3 "Speaking of..."
    d3 "You are special to me, so I will pay you now already."
    d3 "How does that sound?"
    a "I wouldn't mind, sure heh..."
    d3 "This has been a good gig. Will definitely turn some heads."
    d3 "Just come and check with my tablet from time to time and see if there are any new shoots. Eh?"
    a "Will do!"
    play sound moneysound
    $ renpy.notify("+ 8,500 $")
    d3 "Take care!"
    scene black with Dissolve(1)
    stop sound
    stop audio
    $ EP10_var_4 = True
    $ persistent.scene_29 = True
    if EP10_var_8 == False:
        jump EP10_Alfred_Shop
    else:
        jump EP10_Bath

label EP10_Bath:
    scene black with Dissolve(1)
    "Anna went home..."
    play sound shower_sound1
    scene 29-17 shower 2 with Dissolve(1)
    a "Ah..."
    a "A good bath after a long day is worth it..."
    a "It's been busy... Tomorrow I've got the closing..."
    scene 29-17 shower 3 with Dissolve(1)
    a "See what other things I will have to do..."
    scene 29-17 shower 6 with Dissolve(1)
    a "That's better..."
    $ EP10_var_9 = True
    play sound cloth_sound1
    scene black with Dissolve(1)
    scene 32-4 home 1 with Dissolve(1)
    a "Good night..."
    scene 29-18 bedroom 3 with Dissolve(1)
    stop music
    scene black with Dissolve(1)
    pause 1
    play sound interface_sound
    show text "Wednesday morning..." with Dissolve(1)
    pause 1
    scene 34-0 morning 1 with Dissolve(1)
    a "Ah..."
    scene 34-0 morning 2 with Dissolve(1)
    a "Alright... Time to get going, got plenty of things to do today..."
    a "Should check my messages, I think I heard the buzzer."
    play sound walk
    scene black with Dissolve(1)
    show text "At the Hospital."
    pause 4
    jump EP10_Hospital
label EP10_Hospital:
    play music tranquility
    if GoodBadDoctorChoice == 1:
        scene 35-2 cary 1 with Dissolve(1)
        d2 "Ah. Anna."
        d2 "Hello."
        d2 "I've got good news. Andrew will be making a full recovery."
        a "That's... Great to hear."
        scene 35-2 cary 2 with Dissolve(1)
        d2 "About payment..."
        a "Yeah, how much do you need?"
        d2 "I already contacted his father."
        d2 "He has paid 20 thousand dollars."
        d2 "So the reminder is around 30 thousand."
        a "I see. Well, I can pay that now."
        scene 35-2 cary 3 with Dissolve(1)
        play sound moneysound
        $ MoneyVar -= 30000
        $ renpy.notify("-30,000 $")
        a "That is indeed a lot of money."
        d2 "It was an important surgery if he was to regain full function."
        a "I see."
        a "I hope it's worth it."
        d2 "It should be."
        d2 "Would you like to see him?"
        a "Sure, why not."
    if GoodBadDoctorChoice == 2:
        scene 35-3 doc 1 with Dissolve(1)
        a "Hello. You wanted to see me?"
        d1 "I did, yes..."
        d1 "And I'd like to let you know that the surgery has been successful, and he is making a full recovery."
        d1 "On to the matter of money."
        d1 "Andrew's father, John has already put forward 20,000 $"
        d1 "That leaves 30,000 $ more. Since you've been so helpful with my study so far."
        scene 35-3 doc 3 with Dissolve(1)
        a "I don't have the money yet..."
        d1 "Well, well..."
        d1 "That sounds unfortunate for you..."
        a "Sir, can I please get an extension?"
        d1 "Yes, you may, but you within a couple of days, you will come in and I will do 'special' experiment on you."
        d1 "Is that understood?"
        a "Do I have a choice?"
        d1 "Well... Either that or you pay right now."
        a "..."
        a "Okey..."
        play sound moneysound
        $ renpy.notify("-30,000 $")
        a "I hope it's worth it..."
        d1 "His wellbeing is on the line... Of course it's..."
        d1 "Oh..."
        d1 "You see, that's why I like you."
        d1 "I know that you are a slut, actually..."
        d1 "And you don't really want him to get better, do you?"
        a "I... I do, but... Whatever. Call me when you have the next study appointment."
        d1 "Certainly..."
        scene 35-3 doc 2 with Dissolve(1)
        d1 "Do you wish to see him before you leave?"
        a "Alright, why not..."
    scene 38-8 andrew 1 with Dissolve(1)
    a "He looks just fine."
    a "No scars or anything at all..."
    if GoodBadDoctorChoice == 1:
        d2 "That's why the surgery was expensive. The doctor did a the functional surgery and the cosmetic one after the other."
        a "I see..."
        a "Thank you I suppose..."
        a1 "Anna..."
        a "Is he awake?"
        d2 "Maybe barely..."
        scene 38-8 andrew 2 with Dissolve(1)
        a "Andrew? Are you awake?"
        a1 "I'm..."
        a1 "Sorr...."
        a "I can't make out what he's saying."
        scene 38-8 andrew 3 with Dissolve(1)
        a1 "So beautif..."
        a1 "Don't... Trust..."
        scene 38-8 andrew 4 with Dissolve(1)
        a "What?"
        a "Hello?"
        scene 38-8 andrew 5 with Dissolve(1)
        a "He fell asleep again..."
        d2 "He will be going in and out of consciousness for a couple of days."
    else:
        d1 "What can I say, I work very well..."
        d1 "I did cosmetic surgery as well shortly after the main one."
        a "I see..."
        a "Thank you I suppose..."
        a1 "Anna..."
        a "Is he awake?"
        d1 "Maybe barely..."
        scene 38-8 andrew 2 with Dissolve(1)
        a "Andrew? Are you awake?"
        a1 "I'm..."
        a1 "Sorr...."
        a "I can't make out what he's saying."
        scene 38-8 andrew 3 with Dissolve(1)
        a1 "So beautif..."
        a1 "Don't... Trust..."
        scene 38-8 andrew 4 with Dissolve(1)
        a "What?"
        a "Hello?"
        scene 38-8 andrew 5 with Dissolve(1)
        a "He fell asleep again..."
        d1 "He will be going in and out of consciousness for a couple of days."
    a "Alright... I Will go... then..."
    $ EP10_var_10 = True
    jump EP10_Anna_Office_Work_1
screen EP10_Emails(received, label_name, email_who, content_message, signature):
    zorder 250
    sensitive (not renpy.get_screen("say"))
    add "images/office/office_imagemap/email_background.jpg"
    frame:
        background None
        xsize 500
        ysize 100
        xalign 0.1
        yalign 0.1
        if received == True:
            text "From: " + email_who size 25 color "#000"
        else:
            text "To: " + email_who size 25 color "#000"
    frame:
        background None
        xsize 1400
        ysize 400
        xalign 0.1
        yalign 0.3
        has vbox
        text content_message color "#000"
        text signature color "#000"
    if received == True:
        imagebutton auto "images/office/office_imagemap/reply_%s.png":
            focus_mask True
            action [Hide("EP10_Emails", transition=Dissolve(1)), Jump(label_name)]

label EP10_Anna_Office_Work_1:
    $ renpy.music.play("audio/sounds/bensound-thelounge.ogg", channel = 'music', if_changed = True)
    scene black with Dissolve(1)
    show text "Office"
    pause 2
    play sound jacketcloth
    scene 31-3 jeremy 20 with Dissolve(1)
    "Anna sat at her desk, thought for a second..."
    a "I've got to send the amended points in the main agreement to Madison."
    a "She should compile it all."
    scene 31-3 jeremy 19 with Dissolve(1)
    a "Alright... let's see..."
    a "Got everything done here."
    scene 36-4 work 2 with Dissolve(1)
    a "Gotta check emails..."
    $ EP10_Emails_1 = False
    $ EP10_Emails_2 = False
    $ EP10_Emails_3 = False
    if dianaGoodRelations == True:
        $ EP10_Emails_3 = True
    menu EP10_Emails_Menu:
        "Email Madison the amended documents." if EP10_Emails_1 == False:
            show screen EP10_Emails(False, "None", "madison.direct@jercomp.org", "Attached below are the rest of the amended documents. Please make sure to compile it all and prep them. Double check wording, too.", "Anna") with Dissolve(1)
            $ EP10_Emails_1 = True
            pause
            hide screen EP10_Emails with Dissolve(1)
            jump EP10_Emails_Menu
        "Email from Corporate" if EP10_Emails_2 == False:
            $ EP10_Emails_2 = True
            show screen EP10_Emails(True, "EP10_Corporate_Email", "ben.wallace@jercomp.org", "Hello, Anna. I wanted to wish you luck from us in the corporate. Got our fingers crossed that you close the deal. Do your best.", "Ben") with Dissolve(1)
            pause
            label EP10_Corporate_Email:
                show screen EP10_Emails(False, "None", "anna.direct@jercomp.org", "Thank's Ben! I will do my best indeed.", "Anna") with Dissolve(1)
                pause
                hide screen EP10_Emails with Dissolve(1)
            jump EP10_Emails_Menu
        "Email from Jeremy" if dianaGoodRelations == False and EP10_Emails_3 == False:
            $ EP10_Emails_3 = True
            show screen EP10_Emails(True, "EP10_Jeremy_Email", "jeremy.direct@jercomp.org", "Come to me as soon as you can.", "")
            pause
            label EP10_Jeremy_Email:
                show screen EP10_Emails("False", "None", "anna.direct@jercomp.org", "Will do.", "Anna")
                pause
                hide screen EP10_Emails with Dissolve(1)
            jump EP10_Emails_Menu
        "That's all" if EP10_Emails_1 == True and EP10_Emails_2 == True and EP10_Emails_3 == True:
            $ EP10_var_11 = True
            jump EP10_Madison_Convo
label EP10_Madison_Convo:
    $ EP10_var_12 = True
    scene 31-3 jeremy 7 with Dissolve(1)
    a "Hey, Madison."
    a "I just came to double-check that everything is in order."
    m1 "Yes, yes. I compiled everything and printed it once. Checked, printed again."
    m1 "So I've got two physical copies ready."
    a "Ok, great."
    scene 31-3 jeremy 6 with Dissolve(1)
    a "Did you double-check grammar and everything?"
    m1 "Yeah, used the automation to check everything."
    m1 "I mean, we should really give Timothy a raise, his programs work flawlessly."
    a "Yeah, I agree."
    if dianaGoodRelations == False:
        a "I still have to talk to Jeremy, so I will go to him..."
        jump EP10_Anna_Office_Work_2
    else:
        a "Let's go since everything is in order."
        m1 "Okay!"
        jump EP10_Plane
label EP10_Anna_Office_Work_2:
    scene black
    play sound door2
    scene 36-5 jeremy 1 with Dissolve(1)
    a "You wanted to see me?"
    j1 "Yeah. I trust that all documentation is prepared and checked for mistakes?"
    a "Yeah. So far, so good."
    a "Already checked with Madison, all should be good."
    j1 "Alright..."
    scene 36-5 jeremy 2 with Dissolve(1)
    j1 "I don't have to remind you that this is our biggest client."
    j1 "So you should undoubtedly make sure that everything is proper."
    a "I wonder, though. If it's the biggest client yet..."
    a "How have we been able to get all things sorted out so quickly?"
    scene 36-5 jeremy 3 with Dissolve(1)
    j1 "It was in process before you caught wind of it. I was taking care of certain things."
    j1 "You were the last important part..."
    a "I... I see."
    j1 "If everything is in order, let's head out."
    a "Alright."
    $ EP10_var_13 = True
    scene black with Dissolve(2)
    pause
    "Some time later..."
    jump EP10_Plane

label EP10_Plane:
    play sound carsound2
    scene black with Dissolve(1)
    pause 2
    play music SexyTimeSong5
    if dianaGoodRelations == True:
        scene 38-3 plane 1 with Dissolve(1)
        m1 "Wow. I can't believe we actually have our own plane."
        a "Yeah. I've been on it a couple of times."
        m1 "You know you've made it when you can fly around in a private jet."
        a "Well. We can't really go where we want."
        scene 38-3 plane 2 with Dissolve(1)
        m1 "I suppose so..."
        m1 "But no more boring and tedious business trips."
        a "Right?"
        m1 "I almost feel like you're my sugar momma."
        a "Haha. Maybe I am..."
        scene 38-3 plane 3 with Dissolve(1)
        m1 "Well, well..."
        m1 "This is all to us?"
        a "Yeah. Surprisingly."
        m1 "Damn the company must be rich to give the entire plane only to us."
        a "This is a very big client."
        a "If I remember correctly, it's the biggest one we've had!"
        m1 "Right. I read the files, too."
        scene 38-3 plane 5 with Dissolve(1)
        a "Alright, let's get settled in. We've got some time before take off."
        a "Also got some work to do before we touch down in Dubai."
        m1 "Dubai... Crazy..."
        a "As far as I know, we will be taken to a private residence outside of the city."
        play sound cloth_sound1
        scene 38-3 plane 6 with Dissolve(1)
        m1 "So what's on the agenda?"
        a "I will get to it in a bit."
        a "Some last-minute paperwork."
        scene 38-3 plane 7 with Dissolve(1)
        m1 "Alright, meanwhile..."
        m1 "Would you like anything?"
        m1 "I am your assistant, after all."
        a "Yeah, Madison. Can you bring some refreshments and snacks for both of us?"
        m1 "Right away."
        play sound walk
        scene 38-3 plane 8 with Dissolve(1)
        pause 3
        scene 38-3 plane 11 with Dissolve(1)
        a "{i}...Crazy how far we've come..."
        a "{i}...If I land this deal, I will get a huge commission probably."
        a "{i}...As well as the respect from my peers."
        scene black with Dissolve(1)
        scene 38-3 plane 12 with Dissolve(1)
        m1 "Alright."
        m1 "Brought some coffe, croisants."
        m1 "Some whiskey, too."
        a "Great, that should help us along."
        a "Come, sit. Let's have a little chat. The plane is about to take off."
        scene black with Dissolve(1)
        scene 38-3 plane 13 with Dissolve(1)
        m1 "Now that we're in the air..."
        m1 "What's the plan?"
        scene 38-3 plane 14 with Dissolve(1)
        a "Well, I will be meeting with them, you will have the rest of the day for yourself."
        a "You can walk around town, see the sights."
        a "I don't think anyone will notice if you grab the corporate card."
        a "Buy yourself something nice."
        m1 "That's awesome!"
        play sound drinkingBeverage
        scene 38-3 plane 15 with Dissolve(1)
        a "Indeed."
        a "Just try not to spend too much, alright?"
        a "I've also got some paperwork to go through, so if you could give me a minute."
        m1 "You're the boss. I do what you tell me..."
        scene 38-3 plane 16 with Dissolve(1)
        a "You'd do anything?"
        m1 "Well, I'm bound by my contract..."
        a "Hehe... Good to know..."
        scene black with Dissolve(1)
        "Some time later..."
        scene 38-3 plane 17 with Dissolve(1)
        a "Now. Time for a break, wouldn't you agree?"
        m1 "Oh, I wasn't even working."
        menu:
            "Anna becomes more dominant...":
                label EP10_Plane_Lesbian_Label:
                    pass
                a "I need you to help me relax."
                scene 38-3 plane 18 with Dissolve(1)
                m1 "I... I can do that."
                a "Good."
                a "Come with me, now."
                $ dom_var += 1
                scene 38-3 plane 19 with Dissolve(1)
                m1 "Huh?"
                a "This way..."
                "Madison was curious."
                "But Anna wasn't even really hiding her intentions."
                scene 38-3 plane 20 with Dissolve(1)
                a "This is a relaxation room."
                a "We can sit down here, and you can do something for me."
                m1 "Alright, Anna."
                scene 38-3 plane 21 with Dissolve(1)
                a "Now... I want you to do whatever I ask of you."
                m1 "Okey."
                play sound surprise
                scene 38-3 plane 22 with Dissolve(1)
                a "I want you to take off your shirt."
                a "I want to see those naked tits in front of me."
                m1 "WHAT?"
                a "DO IT..."
                scene 38-3 plane 23 with Dissolve(1)
                "Anna was commanding Madison to fulfill all her needs."
                a "Yes..."
                a "Your beautiful, beautiful tits..."
                play sound jacketcloth
                scene 38-3 plane 24 with Dissolve(1)
                a "Lemme get rid of mine, too."
                a "Come here."
                play sound jerk3
                scene 38-3 plane 25 with Dissolve(1)
                "Anna started to lick her mouth."
                "Kiss it all over."
                m1 "Mmm..."
                play sound smooch
                scene 38-3 plane 26 with Dissolve(1)
                pause
                a "Mf..."
                scene 38-3 plane 27 with Dissolve(1)
                "She moved her hands down to her skirt."
                "Indicating to take them off..."
                play sound undress
                scene 38-3 plane 28 with Dissolve(1)
                "Madison was unsure if she liked that Anna was bossing her around."
                "But she had to do it."
                "It was a part of her job."
                a "You are going to be a good girl and do whatever I ask of you."
                a "Then we will get along nicely."
                a "And I will pay you well."
                m1 "Ok..."
                a "Get naked!"
                scene 38-3 plane 29 with Dissolve(1)
                a "That's better..."
                a "Come here, lick my nipples..."
                a "I want you here right now..."
                play sound kisspeck
                scene 38-3 plane 30 with Dissolve(1)
                "Madison slowly licked Anna's nipples."
                "Filling her with pleasure..."
                a "Ahh..."
                scene 38-3 plane 31 with Dissolve(1)
                "Soon after, Anna moved her head down to her pussy."
                a "LICK IT!"
                "Pressing Madison's head against her crotch."
                a "AAHHH!!"
                "She was using Madison's face as her personal sex toy."
                m1 "MMHH... MHHHH"
                "Madison could barely breathe. Anna was pushing her face hard."
                scene 38-3 plane 32 with Dissolve(1)
                "But she tried her best to please Anna."
                "Otherwise who knows what would happen."
                "Anna was in power now..."
                "And it felt good!"
                play sound kisspeck
                scene 38-3 plane 33 with Dissolve(1)
                a "Mmm..."
                a "Ahh!"
                play sound lighthit
                scene 38-3 plane 34 with Dissolve(1)
                a "Use your fingers now."
                m1 "Yes, ma'am."
                scene 38-3 plane 35 with Dissolve(1)
                a "Ahh..."
                a "That's it..."
                a "Don't stop now!"
                $ EP10_Plane_Lesbian_var_1 = 1
                $ EP10_Plane_Lesbian_var_2 = 1
                $ EP10_Plane_Lesbian_var_3 = False
                play sound moaningfour
                label EP10_Plane_Lesbian_4:
                    $ config.menu_include_disabled = True
                    $ different_choice_menu = True
                    scene black
                    hide EP10_Plane_Anim_6
                    hide EP10_Plane_Anim_6_Faster
                    hide EP10_Plane_Anim_7
                    hide EP10_Plane_Anim_7_Faster
                    if EP10_Plane_Lesbian_var_1 == 1:
                        if EP10_Plane_Lesbian_var_2 == 1:
                            show EP10_Plane_Anim_6 with Dissolve(1)
                        if EP10_Plane_Lesbian_var_2 == 2:
                            show EP10_Plane_Anim_6_Faster with Dissolve(1)
                    if EP10_Plane_Lesbian_var_1 == 2:
                        if EP10_Plane_Lesbian_var_2 == 1:
                            show EP10_Plane_Anim_7 with Dissolve(1)
                        if EP10_Plane_Lesbian_var_2 == 2:
                            show EP10_Plane_Anim_7_Faster with Dissolve(1)
                    menu:
                        "Slower":
                            $ EP10_Plane_Lesbian_var_2 = 1
                            jump EP10_Plane_Lesbian_4
                        "Faster":
                            $ EP10_Plane_Lesbian_var_2 = 2
                            $ EP10_Plane_Lesbian_var_3 = True
                            jump EP10_Plane_Lesbian_4
                        "View 1":
                            $ EP10_Plane_Lesbian_var_1 = 1
                            jump EP10_Plane_Lesbian_4
                        "View 2" if EP10_Plane_Lesbian_var_3 == True:
                            $ EP10_Plane_Lesbian_var_1 = 2
                            jump EP10_Plane_Lesbian_4
                        "Continue":
                            hide EP10_Plane_Anim_6
                            hide EP10_Plane_Anim_6_Faster
                            hide EP10_Plane_Anim_7
                            hide EP10_Plane_Anim_7_Faster
                            $ different_choice_menu = False
                            pass
                scene 38-3 plane 36 with Dissolve(1)
                "Madison was about make Anna moan from pleasure."
                a "Put them in me..."
                m1 "Yes, Anna..."
                $ EP10_Plane_Lesbian_var_1 = 1
                $ EP10_Plane_Lesbian_var_2 = 1
                $ EP10_Plane_Lesbian_var_3 = False
                label EP10_Plane_Lesbian_5:
                    $ config.menu_include_disabled = True
                    $ different_choice_menu = True
                    scene black
                    hide EP10_Plane_Anim_8
                    hide EP10_Plane_Anim_8_Faster
                    hide EP10_Plane_Anim_9
                    if EP10_Plane_Lesbian_var_1 == 1:
                        if EP10_Plane_Lesbian_var_2 == 1:
                            show EP10_Plane_Anim_8 with Dissolve(1)
                        if EP10_Plane_Lesbian_var_2 == 2:
                            show EP10_Plane_Anim_8_Faster with Dissolve(1)
                    if EP10_Plane_Lesbian_var_1 == 2:
                        if EP10_Plane_Lesbian_var_2 == 1:
                            show EP10_Plane_Anim_9 with Dissolve(1)
                        if EP10_Plane_Lesbian_var_2 == 2:
                            show EP10_Plane_Anim_9 with Dissolve(1)
                    menu:
                        "Slower":
                            $ EP10_Plane_Lesbian_var_2 = 1
                            jump EP10_Plane_Lesbian_5
                        "Faster":
                            $ EP10_Plane_Lesbian_var_2 = 2
                            jump EP10_Plane_Lesbian_5
                        "View 1":
                            $ EP10_Plane_Lesbian_var_1 = 1
                            jump EP10_Plane_Lesbian_5
                        "View 2":
                            $ EP10_Plane_Lesbian_var_1 = 2
                            jump EP10_Plane_Lesbian_5
                        "Continue":
                            hide EP10_Plane_Anim_8
                            hide EP10_Plane_Anim_8_Faster
                            hide EP10_Plane_Anim_9
                            $ different_choice_menu = False
                            pass
                scene 38-3 plane 37 with Dissolve(1)
                "Then Madison was already hot for Anna."
                "She got comfy and started to scissor Anna's pussy."
                a "AAHH."
                m1 "YEAH... You're pussy rubs just perfectly against me..."
                play sound jerk
                $ EP10_Plane_Lesbian_var_1 = 1
                $ EP10_Plane_Lesbian_var_2 = 1
                $ EP10_Plane_Lesbian_var_3 = False
                label EP10_Plane_Lesbian_6:
                    $ config.menu_include_disabled = True
                    $ different_choice_menu = True
                    scene black
                    hide EP10_Plane_Anim_10
                    hide EP10_Plane_Anim_11
                    if EP10_Plane_Lesbian_var_1 == 1:
                        if EP10_Plane_Lesbian_var_2 == 1:
                            show EP10_Plane_Anim_10 with Dissolve(1)
                    if EP10_Plane_Lesbian_var_1 == 2:
                        if EP10_Plane_Lesbian_var_2 == 1:
                            show EP10_Plane_Anim_11 with Dissolve(1)
                    menu:
                        "View 1":
                            $ EP10_Plane_Lesbian_var_1 = 1
                            jump EP10_Plane_Lesbian_6
                        "View 2":
                            $ EP10_Plane_Lesbian_var_1 = 2
                            jump EP10_Plane_Lesbian_6
                        "Continue":
                            hide EP10_Plane_Anim_10
                            hide EP10_Plane_Anim_11
                            $ different_choice_menu = False
                            pass
                scene 38-3 plane 38 with Dissolve(1)
                a "AAAHHH!!!"
                with flash_vpunch
                m1 "OH... OH..."
                scene 38-3 plane 39 with flash_vpunch
                "Both of them twitched from the pleasure."
                with flash_vpunch
                "Both cumming in one motion, at the same time."
                a "OHAAHH"
                with flash_vpunch
                m1 "FFFFUUCK!"
                scene 38-3 plane 40 with Dissolve(1)
                a "You are a good little worker, aren't you?"
                m1 "Yes, Ma'am..."
                scene 38-3 plane 41 with Dissolve(1)
                a "I enjoyed you very much, Madison."
                m1 "I... I did, too..."
                "But Madison was conflicted, she agreed to Anna's demands, but didn't think it was the right choice..."
                scene black with Dissolve(1)
                "They got dressed."
                $ persistent.scene_30 = True
                $ renpy.end_replay()
                pass
            "Anna plays it cool.":
                a "I just thought, you know. We could get to know each other a bit more."
                scene 38-3 plane 18 with Dissolve(1)
                m1 "I'm always up for a chat."
                a "That's good to hear."
                a "How about you follow me."
                scene 38-3 plane 19 with Dissolve(1)
                m1 "Huh?"
                a "This way..."
                "Madison was curious."
                "But Anna wasn't even really hiding her intentions."
                scene 38-3 plane 20 with Dissolve(1)
                a "This is a relaxation room."
                a "We can sit down here, get a bit more... intimate..."
                m1 "You mean..."
                m1 "You mean like sexually?"
                a "Yes..."
                a "Don't you want to?"
                scene 38-3 plane 21 with Dissolve(1)
                m1 "I... I'm not sure..."
                a "But what we shared after the party? With Diane?"
                m1 "I was drunk..."
                m1 "Hot women in power are my weakness..."
                a "Is that so?"
                m1 "But I shouldn't... Not now..."
                m1 "Sorry..."
                pass
            "Anna decides not to pursue Madison's panties...":
                scene black with Dissolve(1)
                "Sometime later..."
                scene 38-3 plane 43 with Dissolve(1)
                a "And so, that's how I became a partner..."
                m1 "Impressive, Anna."
                m1 "I'm glad to see another woman up there."
                a "It has its perks... Such as this plane..."
                pass
        scene 38-3 plane 42 with Dissolve(1)
        a "Alright, now on to some more business..."
        m1 "I will go through some documents, and re-check them."
        a "Good."
        scene black with Dissolve(1)
        "They landed."
        scene 38-3 plane 44 with Dissolve(1)
        a "Ok, I think we're here..."
        a "Time to get going."
        play sound walk
        scene 38-3 plane 45 with Dissolve(1)
        a "We've got to go through the security and a limo will await us."
        a "But I received a message, you will have to come with me, actually."
        a "No time for sightseeing..."
        m1 "That's no problem..."
        scene black
        jump EP10_Conglomerate_Meeting
    else:
        scene 38-3 plane 1-1 with Dissolve(1)
        j1 "Alright, then."
        j1 "Let's get on."
        a "Do we have all the paperwork?"
        j1 "Yes. But you know, I would consider it your job."
        a "I mean, yeah. just double checking."
        scene 38-3 plane 2-1 with Dissolve(1)
        j1 "That's nice!"
        "Jeremy was eyeing Madison's backside."
        "Already plotting his next perverted move."
        m1 "I'm excited. I've never flown a private jet."
        j1 "Hehe... Good to know. I might take you on more trips."
        scene 38-3 plane 3-1 with Dissolve(1)
        j1 "Alright, get settled in."
        m1 "We've got it all to ourselves?"
        j1 "Yes."
        j1 "Anyway, let's move. The plan will take off soon."
        scene 38-3 plane 5-1 with Dissolve(1)
        a "Do you like it?"
        m1 "Do I?"
        m1 "This is pretty awesome."
        a "Yeah, if you hang out with us, you will get more trips like this."
        j1 "Oh yes... That is preferable, two sexy ladies on my plane."
        play sound jacketcloth
        scene 38-3 plane 6-1 with Dissolve(1)
        j1 "Bring us some snacks and refreshments."
        m1 "Alright, I will check what's available."
        a "Thanks, Madison."
        scene 38-3 plane 7-1 with Dissolve(1)
        j1 "Be quick about it, I want a good drink!"
        m1 "Right away..."
        play sound walk
        scene 38-3 plane 8-1 with Dissolve(1)
        pause 2.5
        scene 38-3 plane 9-1 with Dissolve(1)
        j1 "You still have some paperwork to finish up."
        j1 "I will just sit back and relax."
        j1 "I will have plenty of work when I land."
        j1 "And need I remind you that this is our biggest client."
        j1 "You better not botch it."
        scene 38-3 plane 10-1 with Dissolve(1)
        a "I will do my best, sir."
        a "Unless you pull something like the previous time."
        j1 "Beg you pardon?"
        a "When you change the deal at the very end and almost cost us the deal?"
        if jeremySexContent == True:
            j1 "Don't talk to me like that! Plus they were morons anyway."
            j1 "You do well to remember not to talk to me like that."
            j1 "I'm sure you know what happens if you disobey me?"
            a "I know..."
        else:
            j1 "Ah. Well... I was hoping. That was a bit of unfortunate business..."
            j1 "Still, you landed the deal. Great, great success."
        scene 38-3 plane 9-1 with Dissolve(1)

        if jeremySexContent == True:
            j1 "Also, I want you to seduce Madison, in front of me."
        else:
            j1 "I'm probably gonna regret this, but I sometimes wished you did something with Madison."

        scene 38-3 plane 10-1 with Dissolve(1)
        if jeremySexContent == True:
            a "You can't be serious?"
            j1 "I am. And you will do it."
            a "..."
        else:
            a "That is indeed not a good thing to say."
            j1 "Well, yeah. Sorry..."
        scene 38-3 plane 12-1 with Dissolve(1)
        m1 "Alright, refreshments. Drinks, croissants."
        j1 "Good, good!"
        j1 "Whiskey, that's exactly what I need."
        if jeremySexContent == True:
            j1 "With all these blabbering women around..."
            a "Hmph..."
        scene 38-3 plane 13-1 with Dissolve(1)
        "They looked at each other in understanding."
        "They didn't like Jeremy..."
        "But he was their boss..."
        m1 "So... What do you want from me next?"
        scene 38-3 plane 14-1 with Dissolve(1)
        a "Oh me?"
        a "I think we've got it from here, you can just sit and relax."
        a "I understand that you prepped all the legal documents and everything else before we headed out?"
        m1 "Yes, Anna."
        scene 38-3 plane 15-1 with Dissolve(1)
        if jeremySexContent == True:
            "Out of nowhere, Jeremy insisted on some perversions..."
            j1 "Since we are on this here plane, as rich people..."
            j1 "I want you two to be my entertainment."
            a "What?"
            j1 "Yes. Well, Anna? Will you do what I asked?"
            a "That's..."
        else:
            j1 "You know, I don't wanna sound out of line, but you girls are great."
            j1 "In all kinds of ways..."
            j1 "Also very attractive."
            m1 "Thank you, sir."
            j1 "I wish you did some sexy stuff..."
        menu:
            "Okey..." if jeremySexContent == True:
                label EP10_Plane_Jeremy_Sex:
                    pass
                scene 38-3 plane 16-1 with Dissolve(1)
                "Anna got up from her seat and moved towards Madison..."
                j1 "Yes... Yes..."
                m1 "Umm... Do we have to do it?"
                a "Yes... We have to do what he asks of us."
                "Was Anna truly scared of Jeremy? Seemed like she was secretly enjoying this."
                play sound jacketcloth
                scene 38-3 plane 17-1 with Dissolve(1)
                m1 "Anna..."
                m1 "It's not right..."
                a "I... I'm sorry."
                "Neither of them really resisted."
                play sound jacketcloth
                scene 38-3 plane 18-1 with Dissolve(1)
                j1 "Mhmmmm..."
                play sound undress
                scene 38-3 plane 19-1 with Dissolve(1)
                j1 "Very nice..."
                "Jeremy enjoyed the show..."
                scene 38-3 plane 20-1 with Dissolve(1)
                m1 "Ah..."
                "Anna touched Madison all around, while Jeremy was looking."
                "They both felt uneasy."
                "But not agreeing with Jeremy would be worse..."
                scene 38-3 plane 21-1 with Dissolve(1)
                j1 "Wonderful..."
                pause
                scene 38-3 plane 22-1 with Dissolve(1)
                j1 "How about you, Madison, help Anna with some undressing?"
                scene 38-3 plane 23-1 with Dissolve(1)
                a "{i}...Oh no... He probably wants more..."
                a "{i}...But... It's okay... Maybe..."
                a "{i}...This is my place after all... Right?..."
                scene 38-3 plane 24-1 with Dissolve(1)
                m1 "Are you ok with that?"
                j1 "YES SHE IS!"
                a "Yeah..."
                "And Anna started to accept that even more."
                scene 38-3 plane 25-1 with Dissolve(1)
                "She moved her hands onto Anna, Caressing her."
                "Those soft, warm hands made me feel a bit better."
                play sound cloth_sound1
                scene 38-3 plane 26-1 with Dissolve(1)
                "Then she slowly started to take off her skirt..."
                play sound jacketcloth
                scene 38-3 plane 27-1 with Dissolve(1)
                j1 "Now sit down on the table..."
                j1 "And you, Madison, 'help' Anna relax down there.."
                play sound surprise2
                scene 38-3 plane 28-1 with Dissolve(1)
                m1 "Excuse me?"
                j1 "I think we talked about this already..."
                m1 "Yeah..."
                play sound cloth_sound1
                scene 38-3 plane 29-1 with Dissolve(1)
                pause
                scene 38-3 plane 30-1 with Dissolve(1)
                pause 2
                scene 38-3 plane 31-1 with Dissolve(1)
                "She got on her knees in front of Anna."
                "She felt at Anna's mercy..."
                "Looking like a peasant at a queen."
                scene 38-3 plane 32-1 with Dissolve(1)
                "Who was about to pleasure her..."
                "Anna was a queen, after all..."
                "A nasty, perverted, and lustful queen."
                play sound undress
                scene 38-3 plane 33-1 with Dissolve(1)
                pause
                scene 38-3 plane 34-1 with Dissolve(1)
                j1 "Now. Use your mouth on her!"
                m1 "Y... Yes, sir."
                scene 38-3 plane 35-1 with Dissolve(1)
                m1 "I will try to make it as pleasurable as possible."
                a "Don't worry..."
                scene 38-3 plane 36-1 with Dissolve(1)
                "She looked at Anna's exposed pussy lips."
                "At the amazingly sexy pubes."
                scene 38-3 plane 37-1 with Dissolve(1)
                "Touching her..."
                "Feeling her..."
                scene 38-3 plane 38-1 with Dissolve(1)
                "Anna just couldn't handle the arousal that Maidson was giving her."
                "She looked at Jeremy... And something inside of her went even wilder..."
                "She seemed to be enjoying being Jeremy's toy."
                scene 38-3 plane 39-1 with Dissolve(1)
                pause 1.5
                play sound licking_1
                scene 38-3 plane 40-1 with Dissolve(1)
                a "Oh..."
                "Anna moaned lightly..."
                play sound licking_2
                show EP10_Plane_Anim_1 with Dissolve(1)















                pause
                play sound female_moan_4
                a "{i}...Shit... Her tongue is so good..."
                a "{i}...I'm Already feeling something amazing..."
                "Anna's body had barely started to receive stimulation but it was enveloping her."
                pause
                show EP10_Plane_Anim_2 with Dissolve(1)
                hide EP10_Plane_Anim_1
                pause
                pause
                scene 38-3 plane 41-1 with Dissolve(1)
                hide EP10_Plane_Anim_2
                a "Mhh..."
                scene 38-3 plane 42-1 with Dissolve(1)
                "Anna spread her legs to give Madison more room to do her magic."
                a "Yeah... Keep doing it like that..."
                scene 38-3 plane 43-1 with Dissolve(1)
                "Looking at each other."
                "Getting ever more aroused."
                scene 38-3 plane 44-1 with Dissolve(1)
                "None of them had even noticed that Jeremy was naked."
                a "WHAT?"
                j1 "Hehe..."
                play sound surprise2
                scene 38-3 plane 45-1 with Dissolve(1)
                m1 "Oh My!"
                j1 "Now then, ladies."
                scene 38-3 plane 46-1 with Dissolve(1)
                j1 "I want some of the action, too."
                "Anna was too arroused to care at this point..."
                "But Madison... She felt extremely uncomfortable..."
                "But Jeremy had already found ways to convince her."
                scene 38-3 plane 47-1 with Dissolve(1)
                m1 "Okey, sir... I will please you..."
                j1 "I love hearing it from you!"
                scene 38-3 plane 48-1 with Dissolve(1)
                pause 2
                scene 38-3 plane 49-1 with Dissolve(1)
                "She put the tip in."
                "She could smell his cock. The precum."
                "I didn't make her feel any better."
                "But she had to do it."
                play sound licking_1
                show EP10_Plane_Anim_Blow with Dissolve(1)
                pause
                j1 "YEAH!"
                play sound jerk
                j1 "Shit your mouth's good."
                pause
                scene 38-3 plane 50-1 with Dissolve(1)
                j1 "Yeah... This looks great. In your rightful place."
                j1 "On your knees in front of me."
                "Madison just took it..."
                scene 38-3 plane 51-1 with Dissolve(1)
                j1 "How about the 'main course' eh?"
                j1 "You're next, Anna."
                a "Huh?"
                scene 38-3 plane 52-1 with Dissolve(1)
                j1 "Hehe..."
                a "{i}...I just have to accept it..."
                j1 "Let the fun begin... I've been waiting to fuck you on the plane."
                j1 "it's been too long..."
                play sound jerk
                scene 38-3 plane 53-1 with Dissolve(1)
                a "Mh..."
                "As Jeremy started to rub his tip against her, she shook lightly."
                play sound jerk2
                play audio femgasp_1
                scene 38-3 plane 54-1 with Dissolve(1)
                a "Ahh..."
                "Slowly pushing it in..."
                a "OHHH AAHH!"
                scene 38-3 plane 55-1 with Dissolve(1)
                a "You're so... Big..."
                j1 "I know... You like my big cock, don't you..."
                a "I uh..."
                queue sound (female_moan_1, female_moan_2)
                $ EP10_Plane_Sex_1_var_1 = 1
                $ EP10_Plane_Sex_1_var_2 = 1
                label EP10_Plane_Sex_1:
                    scene black
                    hide EP10_Plane_Anim_3
                    hide EP10_Plane_Anim_4
                    hide EP10_Plane_Anim_5
                    hide EP10_Plane_Anim_3_Faster
                    hide EP10_Plane_Anim_4_Faster
                    $ different_choice_menu = True
                    if EP10_Plane_Sex_1_var_1 == 1:
                        if EP10_Plane_Sex_1_var_2 == 1:
                            show EP10_Plane_Anim_3 with Dissolve(1)
                        if EP10_Plane_Sex_1_var_2 == 2:
                            show EP10_Plane_Anim_3_Faster with Dissolve(1)
                    elif EP10_Plane_Sex_1_var_1 == 2:
                        if EP10_Plane_Sex_1_var_2 == 1:
                            show EP10_Plane_Anim_4 with Dissolve(1)
                        if EP10_Plane_Sex_1_var_2 == 2:
                            show EP10_Plane_Anim_4_Faster with Dissolve(1)
                    elif EP10_Plane_Sex_1_var_1 == 3:
                        show EP10_Plane_Anim_5 with Dissolve(1)
                    menu:
                        "Faster":
                            $ EP10_Plane_Sex_1_var_2 = 2
                            jump EP10_Plane_Sex_1
                        "Slower":
                            $ EP10_Plane_Sex_1_var_2 = 1
                            jump EP10_Plane_Sex_1
                        "View 1":
                            $ EP10_Plane_Sex_1_var_1 = 1
                            jump EP10_Plane_Sex_1
                        "View 2":
                            $ EP10_Plane_Sex_1_var_1 = 2
                            jump EP10_Plane_Sex_1
                        "View 3":
                            $ EP10_Plane_Sex_1_var_1 = 3
                            jump EP10_Plane_Sex_1
                        "Continue":
                            pass
                    $ different_choice_menu = False
                menu:
                    "Anna admitted to loving it!":
                        a "YES! OHH..."
                        "Jeremy had, essentially, turned Anna into his sex toy."
                        "And she didn't want it any other way."
                    "Refrained from saying anything...":
                        a "MMmm..."
                        j1 "Your face says enough."
                j1 "Oh fuck... I'm close..."
                j1 "Ahh... Shit..."
                a "Already?"
                j1 "Shit..."
                with flash_vpunch
                j1 "Oh!"
                menu:
                    "Cum on her stomach.":
                        j1 "AAAHHH"
                        with flash_vpunch
                        play sound cum_sound
                        scene 38-3 plane 60-1 with flash
                        j1 "SHIITT!!!!"
                        scene 38-3 plane 61-1 with Dissolve(1)
                    "Cum in Anna's pussy!":
                        j1 "TAKE MY CUM!"
                        with flash_vpunch
                        with flash_vpunch
                        play sound cum_sound
                        scene 38-3 plane 54-1 with Dissolve(1)
                        j1 "AHHH..."
                        j1 "HJAAA!"
                        scene 38-3 plane 59-1 with Dissolve(1)
                        j1 "WHOA!"
                        a "You came already?"
                        j1 "Fuck, you're good..."
                    "Cum in Madison's mouth.":
                        j1 "OPEN YOUR MOUTH REDHEADED SLUT!"
                        m1 "HUH?..."
                        scene 38-3 plane 62-1 with Dissolve(1)
                        with flash_vpunch
                        play sound cum_sound
                        scene 38-3 plane 63-1 with Dissolve(1)
                        j1 "HHHHAA!!"
                        j1 "HMMMF."
                        "Jeremy filled her mouth with his vile seed."
                        play sound cum_sound
                        scene 38-3 plane 64-1 with Dissolve(1)
                        pause 2
                        scene 38-3 plane 65-1 with Dissolve(1)
                        m1 "Are... Are you done, sir?"
                        j1 "Yeah..."
                        scene 38-3 plane 66-1 with Dissolve(1)
                hide EP10_Plane_Anim_3
                hide EP10_Plane_Anim_4
                hide EP10_Plane_Anim_5
                hide EP10_Plane_Anim_3_Faster
                hide EP10_Plane_Anim_4_Faster
                j1 "Well done, girls..."
                j1 "You've earned a break."
                scene black with Dissolve(1)
                "Sometime later."
                scene 38-3 plane 67-1 with Dissolve(1)
                a "I didn't even cum this time..."
                j1 "Hehe!"
                j1 "You've finally accepted your place as my slut?"
                j1 "What was I supposed to do? You two are so hot..."
                j1 "Now sit down. I still got some work to do."
                $ persistent.scene_31 = True
                $ renpy.end_replay()
                pass
            "That is not appropriate Jeremy. I won't!":
                if jeremySexContent == True:
                    j1 "Don't disrespect my word!"
                    a "Sir, I won't sexually pleasure you. That is wrong!"
                    a "You can't force me!"
                    j1 "Fuck... Yes, I can."
                    a "If you do, I will go to the authorities!"
                    j1 "They... They won't believe you."
                    a "Fuck yeah they will, try my, lard ass!"
                if jeremySexContent == False:
                    j1 "Uh... I... I'm sorry girls... I just sometimes get ahead of myself..."
                    a "It's... Okey..."
                    if AnnaCorruption >= 30:
                        "For a second, Anna even thought about giving him pity sex."
                        "But that was beyond reason."
                    j1 "Anyway, let's get back to work."
            "Anna decides to take charge and only enjoy Madison (Dom Anna)." if dom_var>=1:
                $ dom_var += 1
                a "Well, how about I give you nothing, and Madison and I have some fun?"
                j1 "Uh... I..."
                j1 "{b}{i}*GULP*"
                play sound cloth_sound1
                scene 38-3 plane 19-2 with Dissolve(1)
                j1 "Whaaa..."
                "Our nice guy Jeremy was gonna get cucked by two ladies."
                "While he will be working, the two hottest office workers ever will fuck in the other room."
                a "I need you to help me relax."
                m1 "Huh?"
                a "This way..."
                "Madison was curious."
                "But Anna wasn't even really hiding her intentions."
                scene 38-3 plane 20 with Dissolve(1)
                a "This is a relaxation room."
                a "We can sit down here, and you can do something for me."
                m1 "Alright, Anna."
                scene 38-3 plane 21 with Dissolve(1)
                a "Now... I want you to do whatever I ask of you."
                m1 "Okey."
                play sound surprise
                scene 38-3 plane 22 with Dissolve(1)
                a "I want you to take off your shirt."
                a "I want to see those naked tits in front of me."
                m1 "WHAT?"
                a "DO IT..."
                scene 38-3 plane 23 with Dissolve(1)
                "Anna was commanding Madison to fulfill all her needs."
                a "Yes..."
                a "Your beautiful, beautiful tits..."
                play sound jacketcloth
                scene 38-3 plane 24 with Dissolve(1)
                a "Lemme get rid of mine, too."
                a "Come here."
                play sound jerk3
                scene 38-3 plane 25 with Dissolve(1)
                "Anna started to lick her mouth."
                "Kiss it all over."
                m1 "Mmm..."
                play sound smooch
                scene 38-3 plane 26 with Dissolve(1)
                pause
                a "Mf..."
                scene 38-3 plane 27 with Dissolve(1)
                "She moved her hands down to her skirt."
                "Indicating to take them off..."
                play sound undress
                scene 38-3 plane 28 with Dissolve(1)
                a "You are going to be a good girl and do whatever I ask of you."
                a "Then we will get along nicely."
                a "And I will pay you well."
                m1 "Ok..."
                with vpunch
                a "Get naked!"
                scene 38-3 plane 29 with Dissolve(1)
                a "That's better..."
                a "Come here, lick my nipples..."
                a "I want you here right now..."
                play sound kisspeck
                scene 38-3 plane 30 with Dissolve(1)
                "Madison slowly licked Anna's nipples."
                "Filling her with pleasure..."
                a "Ahh..."
                scene 38-3 plane 31 with Dissolve(1)
                "Soon after, Anna moved her head down to her pussy."
                a "LICK IT!"
                "Pressing Madison's head against her crotch."
                a "AAHHH!!"
                "She was using Madison's face as her personal sex toy."
                m1 "MMHH... MHHHH"
                "Madison could barely breathe. Anna was pushing her face hard."
                scene 38-3 plane 31-2 with Dissolve(1)
                "And as they were going at it, Jeremy decided to look a little."
                scene 38-3 plane 32 with Dissolve(1)
                "But she tried her best to please Anna."
                play sound kisspeck
                scene 38-3 plane 33 with Dissolve(1)
                a "Mmm..."
                a "Ahh!"
                play sound lighthit
                scene 38-3 plane 34 with Dissolve(1)
                a "Use your fingers now."
                m1 "Yes, ma'am."
                scene 38-3 plane 35-2 with Dissolve(1)
                "Anna noticed Jeremy peeking."
                "It strangely turned her on."
                scene 38-3 plane 35 with Dissolve(1)
                a "Ahh..."
                a "That's it..."
                a "Don't stop now!"
                $ EP10_Plane_Lesbian_var_1 = 1
                $ EP10_Plane_Lesbian_var_2 = 1
                $ EP10_Plane_Lesbian_var_3 = False
                play sound moaningfour
                label EP10_Plane_Lesbian:
                    $ config.menu_include_disabled = True
                    $ different_choice_menu = True
                    scene black
                    hide EP10_Plane_Anim_6
                    hide EP10_Plane_Anim_6_Faster
                    hide EP10_Plane_Anim_7
                    hide EP10_Plane_Anim_7_Faster
                    if EP10_Plane_Lesbian_var_1 == 1:
                        if EP10_Plane_Lesbian_var_2 == 1:
                            show EP10_Plane_Anim_6 with Dissolve(1)
                        if EP10_Plane_Lesbian_var_2 == 2:
                            show EP10_Plane_Anim_6_Faster with Dissolve(1)
                    if EP10_Plane_Lesbian_var_1 == 2:
                        if EP10_Plane_Lesbian_var_2 == 1:
                            show EP10_Plane_Anim_7 with Dissolve(1)
                        if EP10_Plane_Lesbian_var_2 == 2:
                            show EP10_Plane_Anim_7_Faster with Dissolve(1)
                    menu:
                        "Slower":
                            $ EP10_Plane_Lesbian_var_2 = 1
                            jump EP10_Plane_Lesbian
                        "Faster":
                            $ EP10_Plane_Lesbian_var_2 = 2
                            $ EP10_Plane_Lesbian_var_3 = True
                            jump EP10_Plane_Lesbian
                        "View 1":
                            $ EP10_Plane_Lesbian_var_1 = 1
                            jump EP10_Plane_Lesbian
                        "View 2" if EP10_Plane_Lesbian_var_3 == True:
                            $ EP10_Plane_Lesbian_var_1 = 2
                            jump EP10_Plane_Lesbian
                        "Continue":
                            hide EP10_Plane_Anim_6
                            hide EP10_Plane_Anim_6_Faster
                            hide EP10_Plane_Anim_7
                            hide EP10_Plane_Anim_7_Faster
                            $ different_choice_menu = False
                            pass
                scene 38-3 plane 36 with Dissolve(1)
                "Madison was about make Anna moan from pleasure."
                a "Put them in me..."
                m1 "Yes, Anna..."
                $ EP10_Plane_Lesbian_var_1 = 1
                $ EP10_Plane_Lesbian_var_2 = 1
                $ EP10_Plane_Lesbian_var_3 = False
                label EP10_Plane_Lesbian_2:
                    $ config.menu_include_disabled = True
                    $ different_choice_menu = True
                    scene black
                    hide EP10_Plane_Anim_8
                    hide EP10_Plane_Anim_8_Faster
                    hide EP10_Plane_Anim_9
                    if EP10_Plane_Lesbian_var_1 == 1:
                        if EP10_Plane_Lesbian_var_2 == 1:
                            show EP10_Plane_Anim_8 with Dissolve(1)
                        if EP10_Plane_Lesbian_var_2 == 2:
                            show EP10_Plane_Anim_8_Faster with Dissolve(1)
                    if EP10_Plane_Lesbian_var_1 == 2:
                        if EP10_Plane_Lesbian_var_2 == 1:
                            show EP10_Plane_Anim_9 with Dissolve(1)
                        if EP10_Plane_Lesbian_var_2 == 2:
                            show EP10_Plane_Anim_9 with Dissolve(1)
                    menu:
                        "Slower":
                            $ EP10_Plane_Lesbian_var_2 = 1
                            jump EP10_Plane_Lesbian_2
                        "Faster":
                            $ EP10_Plane_Lesbian_var_2 = 2
                            $ EP10_Plane_Lesbian_var_3 = True
                            jump EP10_Plane_Lesbian_2
                        "View 1":
                            $ EP10_Plane_Lesbian_var_1 = 1
                            jump EP10_Plane_Lesbian_2
                        "View 2" if EP10_Plane_Lesbian_var_3 == True:
                            $ EP10_Plane_Lesbian_var_1 = 2
                            jump EP10_Plane_Lesbian_2
                        "Continue":
                            hide EP10_Plane_Anim_8
                            hide EP10_Plane_Anim_8_Faster
                            hide EP10_Plane_Anim_9
                            $ different_choice_menu = False
                            pass
                scene 38-3 plane 37 with Dissolve(1)
                "Then Madison was already hot for Anna."
                "She got comfy and started to scissor Anna's pussy."
                a "AAHH."
                m1 "YEAH... You're pussy rubs just perfectly against me..."
                $ EP10_Plane_Lesbian_var_1 = 1
                $ EP10_Plane_Lesbian_var_2 = 1
                $ EP10_Plane_Lesbian_var_3 = False
                label EP10_Plane_Lesbian_3:
                    $ config.menu_include_disabled = True
                    $ different_choice_menu = True
                    scene black
                    hide EP10_Plane_Anim_10
                    hide EP10_Plane_Anim_11
                    if EP10_Plane_Lesbian_var_1 == 1:
                        if EP10_Plane_Lesbian_var_2 == 1:
                            show EP10_Plane_Anim_10 with Dissolve(1)
                    if EP10_Plane_Lesbian_var_1 == 2:
                        if EP10_Plane_Lesbian_var_2 == 1:
                            show EP10_Plane_Anim_11 with Dissolve(1)
                    menu:
                        "View 1":
                            $ EP10_Plane_Lesbian_var_1 = 1
                            jump EP10_Plane_Lesbian_3
                        "View 2":
                            $ EP10_Plane_Lesbian_var_1 = 2
                            jump EP10_Plane_Lesbian_3
                        "Continue":
                            hide EP10_Plane_Anim_10
                            hide EP10_Plane_Anim_11
                            $ different_choice_menu = False
                            pass
                scene 38-3 plane 38 with Dissolve(1)
                a "AAAHHH!!!"
                m1 "OH... OH..."
                scene 38-3 plane 38-2 with Dissolve(1)
                "The dirty voyeur look at both girls coming..."
                "He liked that she denied him this pleasure..."
                "He wanted Anna to do more bad things to him..."
                scene 38-3 plane 39 with Dissolve(1)
                "Both of them twitched from the pleasure."
                "Both cumming in one motion, at the same time."
                a "OHAAHH"
                m1 "FFFFUUCK!"
                scene 38-3 plane 40 with Dissolve(1)
                a "You are a good little worker, aren't you?"
                m1 "Yes, Ma'am..."
                scene 38-3 plane 41 with Dissolve(1)
                a "I enjoyed you very much, Madison."
                m1 "I... I did, too..."
                scene black with Dissolve(1)
                "They got dressed."
                $ persistent.scene_30 = True
                $ renpy.end_replay()
                pass
        play sound cloth_sound1
        scene 38-3 plane 68-1 with Dissolve(1)
        if jeremySexContent == True:
            "Awkward silence loomed as they awaited their landing."
        else:
            "They chatted some and awaited their landing."
        scene black with Dissolve(1)
        "After a couple of hours, they landed..."
        if dianaGoodRelations == False:
            scene 38-3 plane 46 with Dissolve(1)
            j1 "Put on your happy faces. We've arrived."
            j1 "Let's get to work. Anna, you know what you've got to do."
            a "Yes... sir..."
            j1 "I will take another limo to meet some other people."
        else:
            scene 38-3 plane 45 with Dissolve(1)
            a "Alright, it's our time to shine. Let's make the company proud."
            m1 "Yes, Anna!"
        jump EP10_Conglomerate_Meeting

label EP10_Conglomerate_Meeting:
    play music tranquility
    play sound walk
    scene 38-4 oil 2 with Dissolve(1)
    pause 1.5
    scene 38-4 oil 3 with Dissolve(1)
    Chauffeur "Ladies! Welcome, welcome!"
    Chauffeur "I'm your chauffeur, I will take you to the compound of my superiors."
    a "Hello. Thank you."
    play sound carsound3
    scene black with Dissolve(1)
    scene 38-4 oil 4 with Dissolve(1)
    Chauffeur "Well, we're here, I wish you a great stay."
    Chauffeur "The CEO is a humble, pleasant person and his concierge is as well. I bid you farewell!"
    Chauffeur "He will be waiting for you in the main open roof area."
    a "Thank you, mister."
    scene 38-4 oil 5 with Dissolve(1)
    m1 "So, what now?"

    menu:
        "Anna decides to 'convince' the client in a more enjoyable way.(More commission)":
            a "Now, it's show time!"
            pass
        "Anna decides to just go sign the agreement as intended.(Less commission)":
            scene 38-4 oil 6 with Dissolve(1)
            a "We'll just go and sign the documents."
            a "Then leave."
            m1 "I see. Shouldn't be that hard."
            a "Nope."
            m1 "We got a private plane just to sign an agreement?"
            a "Physical signature is important."
            a "Let's go..."
            play sound walk
            scene 38-4 oil 12-2 with Dissolve(1)
            pause 1
            scene 38-4 oil 14-2 with Dissolve(1)
            ea2 "There they come."
            ea1 "Indeed."
            scene 38-4 oil 16-2 with Dissolve(1)
            a "Hello. I'm Anna, partner of Jercomp."
            a "This is Madison."
            scene 38-4 oil 18-2 with Dissolve(1)
            ea1 "Hello, Anna. You are as radiant as the sun."
            a "Oh. Haha... Thank you sir."
            scene 38-4 oil 20-2 with Dissolve(1)
            ea2 "I'm Secretary Sareem, and this is Emir Ahsan, the CEO."
            a "Nice to meet you both."
            a "We are glad that you've decided to do business with us."
            a "I believe you've had the time go over the deal?"
            scene 38-4 oil 19-2 with Dissolve(1)
            ea2 "Yes, we have. It seemed appropriate."
            a "I'm glad to hear that, sir."
            scene 38-4 oil 21-2 with Dissolve(1)
            ea1 "We've gathered here today to sign an agreement."
            ea1 "A relationship between two companies, I could say."
            ea1 "In times of hardship, never be afraid to ask for help."
            ea1 "And so, we've come to you for help."
            ea1 "And we thank you for your pledge to be our guiding hand."
            scene 38-4 oil 35-2 with Dissolve(1)
            ea1 "My signature here, ladies."
            ea1 "I'm pleased to announce that we are, as of now, sharing a common goal and a fruitful future!"
            scene 38-4 oil 36-2 with Dissolve(1)
            ea1 "I'm very glad to be a part of this journey with you."
            ea1 "I hope that you are as happy as I am."
            a "I'm truly happy, Emir Ahsan. Thank you."
            ea1 "Thanks be up on you, too."
            scene 38-4 oil 37-2 with Dissolve(1)
            ea1 "If you ever have more time, please. Visit us."
            ea1 "We will be waiting for you as guests in our homes whenever you wish."
            a "Thank you, kind sir. I will consider it."
            ea1 "Peace be upon you."
            scene black with Dissolve(1)
            scene 38-4 oil 6 with Dissolve(1)
            m1 "That was fast."
            a "Yeah..."
            a "Let's go home."
            scene black with Dissolve(1)
            stop sound
            stop audio
            scene black
            show text "Many hours later..."
            pause 3
            $ EP10_var_14 = True
            if bar_var_1 == False:
                jump EP10_Patricks_Kid
            elif EarlHelp == False:
                jump EP10_Sergey_Warehouse
            jump EP10_Variable_Check

    scene 38-4 oil 6 with Dissolve(1)
    a "I've prepared something nice for the client."
    a "Gimme a sec."
    play sound cloth_sound1
    scene black with Dissolve(1)
    scene 38-4 oil 7 with Dissolve(1)
    play sound jacketcloth
    scene black with Dissolve(1)
    scene 38-4 oil 9 with Dissolve(1)
    a "La Voila!"
    m1 "Whoa... Umm... Is it appropriate to wear something like this?"
    m1 "I mean, it's very revealing for a business meeting."
    a "Hehe... You are new to my methods."
    a "If you know what I mean."
    m1 "Wait... Oh..."
    m1 "Won't that get you in trouble?"
    scene 38-4 oil 10 with Dissolve(1)
    a "Hasn't so far."
    m1 "Well... If it gets us what we want, then... I suppose."
    m1 "It's just, not that ethical, I think..."
    a "Well... I believe in doing whatever needs to be done to achieve our goals."
    scene 38-4 oil 11 with Dissolve(1)
    a "Anyway. How do I look?"
    m1 "Astonishing... Profoundly astonishing..."
    m1 "I truly think this one of the best outfits I've ever seen put a on womans body, if we talk in a sexual context."
    a "Ok. Let's get to work!"
    play sound walk
    scene 38-4 oil 12-1 with Dissolve(1)
    pause 2.5
    scene 38-4 oil 13 with Dissolve(1)
    "As she entered, Emir Ahsan and Secretary Sameer both looked in awe."
    "A woman of beauty unmatched..."
    scene 38-4 oil 14-1 with Dissolve(1)
    pause 2.5
    scene 38-4 oil 16-1 with Dissolve(1)
    a "Hello, gentlemen."
    scene 38-4 oil 15 with Dissolve(1)
    ea1 "What the..."
    ea2 "Welcome to our compound. We've been awaiting your arrival."
    ea1 "I... I..."
    ea2 "I believe we are here for business today."
    scene 38-4 oil 17-1 with Dissolve(1)
    "While Secretary Sameer was making the introduction."
    "Ahsan was enchanted by Anna already."
    "He was looking Anna up and down."
    scene 38-4 oil 18 with Dissolve(1)
    "Astounded he was."
    ea1 "Amazing..."
    scene 38-4 oil 19 with Dissolve(1)
    ea2 "I'm Secretary Sameer and this is Emir Ahsan."
    ea2 "We are representatives regarding overseas business."
    ea2 "A pleasure to meet you."
    scene 38-4 oil 20 with Dissolve(1)
    a "Thank you, Secretary."
    a "I'm Anna, one of the partners of the Jercomp."
    scene 38-4 oil 21 with Dissolve(1)
    ea1 "Nice to meet you, Anna."
    scene 38-4 oil 22 with Dissolve(1)
    a "This is my assistant, Madison."
    scene 38-4 oil 23 with Dissolve(1)
    ea2 "A pleasure. As I planned. You will talk the details through with Emir Ahsan."
    ea2 "And I will prepare the documentation with Madison."
    ea2 "But the signing of the agreement will be left to you two."
    a "That sounds like a plan."
    ea2 "Alright, to a fruitful future together."
    "Anna will convince Emir Ahsan."
    "Secretary Sameer was doing everything behind the scenes, Emir Ahsan simply inherited everything."
    "And he was reluctant to deal with Anna's company, however, she was here to convince him, as Secretary Sameer had planned."
    scene 38-4 oil 24 with Dissolve(1)
    ea2 "This way, please."
    ea2 "I will get us something to eat, are you hungry?"
    m1 "Famished, actually..."
    label EP10_Conglomerate_Sex_Label:
        pass
    play music SexyTimeSong7
    scene 38-4 oil 25 with Dissolve(1)
    a "Well, now that they're gone. Let's get down to 'business'?"
    ea1 "Absolutely, Anna."
    ea1 "I'm all ears."
    scene 38-4 oil 28 with Dissolve(1)
    a "Do you like what you see?"
    scene 38-4 oil 29 with Dissolve(1)
    ea1 "Ma'am, I can't..."
    ea1 "Describe..."
    ea1 "IN WORDS!"
    ea1 "Absolutely fantastic!"
    scene black with Dissolve(0.5)
    play sound undress
    scene 38-4 oil 30 with Dissolve(1)
    ea1 "What tha fuuuck..."
    "She was moving seductively, mesmerizing Ahsan."
    scene 38-4 oil 31 with Dissolve(1)
    pause 2.5
    scene 38-4 oil 32 with Dissolve(1)
    a "You can touch if you wish..."
    ea1 "YES! YES!!!"
    scene 38-4 oil 33 with Dissolve(1)
    ea1 "Oh... Such smooth skin..."
    ea1 "So hot..."
    scene 38-4 oil 34 with Dissolve(1)
    a "Before we continue..."
    a "Are you willing to do business with us?"
    a "If you are, I will let you have more..."
    scene 38-4 oil 35 with Dissolve(1)
    ea1 "YES, OF COURSE!"
    ea1 "Anything you want!"
    "He added his signature to the end deal."
    "A manipulative, yet effective tactic by Anna..."
    "She was truly becoming a vicious force in the business world..."
    scene 38-4 oil 36 with Dissolve(1)
    a "Do you want more?"
    ea1 "YES!"
    scene 38-4 oil 37 with Dissolve(1)
    a "I will give you something you've not experienced ever..."
    a "How about you get undressed, sir."
    play sound jacketcloth
    scene 38-4 oil 38 with Dissolve(1)
    a "Well then. Do you want to enjoy me?"
    a "All of my body?"
    ea1 "Fuck yeah, I've been waiting since I first saw you in our meeting."
    scene 38-4 oil 39 with Dissolve(1)
    a "You liked what you saw, didn't you?"
    ea1 "OH... Yeah..."
    pause
    scene 38-4 oil 40 with Dissolve(1)
    pause 2.5
    play sound jacketcloth
    scene 38-4 oil 41 with Dissolve(1)
    "She lowered herself to his pelvis..."
    a "Let's see what you've got, big boy."
    ea1 "Yes, ma'am."
    play sound jerk
    scene 38-4 oil 42 with Dissolve(1)
    ea1 "Ah... Ffff..."
    ea1 "Your hands..."
    a "You like that?"
    ea1 "Heck yeah!"
    scene 38-4 oil 43 with Dissolve(1)
    a "You have a very nice cock, sir."
    ea1 "AAhh... Thank you..."
    ea1 "I love your hands!!!"
    a "How about I turn around and..."
    play sound whoosh_1
    scene 38-4 oil 44 with Dissolve(1)
    a "And show you some more?"
    ea1 "WOMAN... YOU ARE AMAZING!"
    ea1 "COME TO PAPA!!!"
    a "You sure like me a lot, hehe..."
    ea1 "You are a goddess!!"
    play sound jerk2
    scene 38-4 oil 45 with Dissolve(1)
    a "Oh... You're fingers feel so..."
    a "Your fingers are doing magic on my pussy lips..."
    ea1 "I guess I'm a natural."
    scene 38-4 oil 46 with Dissolve(1)
    "He didn't wait a moment longer and put his tip to Anna's hole."
    a "Ah..."
    play sound jerk
    scene 38-4 oil 47 with Dissolve(1)
    ea1 "Oh... Shiit..."
    "Slowly..."
    "Anna was pushing on his cock mildly... take her sweet time..."
    $ EP10_Conglomerate_Sex_Var_1 = 1
    $ EP10_Conglomerate_Sex_Var_2 = 1
    $ EP10_Conglomerate_Sex_Var_3 = False
    queue sound(female_moan_1, female_moan_2, femmoan_3, female_moan_5, femgasp_1, MoaningNine, femmoan_4, female_moan_4) loop
label EP10_Conglomerate_Sex_1:
    $ config.menu_include_disabled = True
    $ different_choice_menu = True
    scene black
    hide EP10_Conglomerate_Anim_1
    hide EP10_Conglomerate_Anim_1_Faster
    hide EP10_Conglomerate_Anim_2
    hide EP10_Conglomerate_Anim_2_Faster
    if EP10_Conglomerate_Sex_Var_1 == 1:
        if EP10_Conglomerate_Sex_Var_2 == 1:
            show EP10_Conglomerate_Anim_1 with Dissolve(1)
        if EP10_Conglomerate_Sex_Var_2 == 2:
            show EP10_Conglomerate_Anim_1_Faster with Dissolve(1)
    if EP10_Conglomerate_Sex_Var_1 == 2:
        if EP10_Conglomerate_Sex_Var_2 == 1:
            show EP10_Conglomerate_Anim_2 with Dissolve(1)
        if EP10_Conglomerate_Sex_Var_2 == 2:
            show EP10_Conglomerate_Anim_2_Faster with Dissolve(1)
    menu:
        "Slower":
            $ EP10_Conglomerate_Sex_Var_2 = 1
            jump EP10_Conglomerate_Sex_1
        "Faster":
            $ EP10_Conglomerate_Sex_Var_2 = 2
            jump EP10_Conglomerate_Sex_1
        "View 1":
            $ EP10_Conglomerate_Sex_Var_1 = 1
            jump EP10_Conglomerate_Sex_1
        "View 2":
            $ EP10_Conglomerate_Sex_Var_1 = 2
            jump EP10_Conglomerate_Sex_1
        "Continue":
            $ different_choice_menu = False
            hide EP10_Conglomerate_Anim_1
            hide EP10_Conglomerate_Anim_1_Faster
            hide EP10_Conglomerate_Anim_2
            hide EP10_Conglomerate_Anim_2_Faster
            pass
    $ EP10_Conglomerate_Sex_Var_1 = 1
    $ EP10_Conglomerate_Sex_Var_2 = 1
    $ EP10_Conglomerate_Sex_Var_3 = False
    play audio jerk3
label EP10_Conglomerate_Sex_2:
    $ config.menu_include_disabled = True
    $ different_choice_menu = True
    scene black
    hide EP10_Conglomerate_Anim_3
    hide EP10_Conglomerate_Anim_4
    if EP10_Conglomerate_Sex_Var_1 == 1:
        if EP10_Conglomerate_Sex_Var_2 == 1:
            show EP10_Conglomerate_Anim_3 with Dissolve(1)
    if EP10_Conglomerate_Sex_Var_1 == 2:
        if EP10_Conglomerate_Sex_Var_2 == 1:
            show EP10_Conglomerate_Anim_4 with Dissolve(1)
    menu:
        "View 1":
            $ EP10_Conglomerate_Sex_Var_1 = 1
            jump EP10_Conglomerate_Sex_2
        "View 2":
            $ EP10_Conglomerate_Sex_Var_1 = 2
            jump EP10_Conglomerate_Sex_2
        "Continue":
            $ different_choice_menu = False
            pass
    stop sound
    a "Oh... Your cock is absolutely perfect.."
    ea1 "Same about your pussy..."
    ea1 "Oh... Shit..."
    ea1 "I can't even..."
    scene 38-4 oil 49 with Dissolve(1)
    a "Yeah?"
    a "You like it? Ahh..."
    ea1 "I love it..."
    scene 38-4 oil 50 with Dissolve(1)
    ea1 "Lemme just..."
    a "Ah... Hehe..."
    a "My other hole... You want it?"
    a "Take it..."
    ea1 "MAAAAAAAAAANNN!!"
    ea1 "YEAHHH!!"
    play audio jerk
    scene 38-4 oil 51 with Dissolve(1)
    hide EP10_Conglomerate_Anim_1
    hide EP10_Conglomerate_Anim_1_Faster
    hide EP10_Conglomerate_Anim_2
    hide EP10_Conglomerate_Anim_2_Faster
    queue sound(female_moan_1, female_moan_2, femmoan_3, female_moan_5, femgasp_1, MoaningNine, femmoan_4, female_moan_4) loop
    $ EP10_Conglomerate_Sex_Var_1 = 1
    $ EP10_Conglomerate_Sex_Var_2 = 1
    $ EP10_Conglomerate_Sex_Var_3 = False
    play audio jerk3
label EP10_Conglomerate_Sex_3:
    $ config.menu_include_disabled = True
    $ different_choice_menu = True
    scene black
    hide EP10_Conglomerate_Anim_5
    hide EP10_Conglomerate_Anim_5_Faster
    hide EP10_Conglomerate_Anim_6
    hide EP10_Conglomerate_Anim_6_Faster
    if EP10_Conglomerate_Sex_Var_1 == 1:
        if EP10_Conglomerate_Sex_Var_2 == 1:
            show EP10_Conglomerate_Anim_5 with Dissolve(1)
        if EP10_Conglomerate_Sex_Var_2 == 2:
            show EP10_Conglomerate_Anim_5_Faster with Dissolve(1)
    if EP10_Conglomerate_Sex_Var_1 == 2:
        if EP10_Conglomerate_Sex_Var_2 == 1:
            show EP10_Conglomerate_Anim_6 with Dissolve(1)
        if EP10_Conglomerate_Sex_Var_2 == 2:
            show EP10_Conglomerate_Anim_6_Faster with Dissolve(1)
    menu:
        "Slower":
            $ EP10_Conglomerate_Sex_Var_2 = 1
            jump EP10_Conglomerate_Sex_3
        "Faster":
            $ EP10_Conglomerate_Sex_Var_2 = 2
            jump EP10_Conglomerate_Sex_3
        "View 1":
            $ EP10_Conglomerate_Sex_Var_1 = 1
            jump EP10_Conglomerate_Sex_3
        "View 2":
            $ EP10_Conglomerate_Sex_Var_1 = 2
            jump EP10_Conglomerate_Sex_3
        "Continue":
            $ different_choice_menu = False
            hide EP10_Conglomerate_Anim_5
            hide EP10_Conglomerate_Anim_5_Faster
            hide EP10_Conglomerate_Anim_6
            hide EP10_Conglomerate_Anim_6_Faster
            pass
    scene 38-4 oil 52 with Dissolve(1)
    ea1 "I want to fuck you at my speed..."
    ea1 "Get on the couch..."
    "Anna pulled off of his cock..."
    a "Yes, sir."
    scene 38-4 oil 54 with Dissolve(1)
    "Waiting a not a moment longer he inserted it back into Anna..."
    a "OHhh... AAH!!!"
    ea1 "YEAHAAAH... ARGhh... FUCK!"
    $ EP10_Conglomerate_Sex_Var_1 = 1
    $ EP10_Conglomerate_Sex_Var_2 = 1
    $ EP10_Conglomerate_Sex_Var_3 = False
    play audio jerk3
label EP10_Conglomerate_Sex_4:
    $ config.menu_include_disabled = True
    $ different_choice_menu = True
    scene black
    hide EP10_Conglomerate_Anim_8
    hide EP10_Conglomerate_Anim_8_Faster
    hide EP10_Conglomerate_Anim_9
    hide EP10_Conglomerate_Anim_9_Faster
    hide EP10_Conglomerate_Anim_10
    hide EP10_Conglomerate_Anim_10_Faster
    hide EP10_Conglomerate_Anim_11
    hide EP10_Conglomerate_Anim_11_Faster
    if EP10_Conglomerate_Sex_Var_1 == 1:
        if EP10_Conglomerate_Sex_Var_2 == 1:
            show EP10_Conglomerate_Anim_8 with Dissolve(1)
        if EP10_Conglomerate_Sex_Var_2 == 2:
            show EP10_Conglomerate_Anim_8_Faster with Dissolve(1)
    if EP10_Conglomerate_Sex_Var_1 == 2:
        if EP10_Conglomerate_Sex_Var_2 == 1:
            show EP10_Conglomerate_Anim_9 with Dissolve(1)
        if EP10_Conglomerate_Sex_Var_2 == 2:
            show EP10_Conglomerate_Anim_9_Faster with Dissolve(1)
    if EP10_Conglomerate_Sex_Var_1 == 3:
        if EP10_Conglomerate_Sex_Var_2 == 1:
            show EP10_Conglomerate_Anim_10 with Dissolve(1)
        if EP10_Conglomerate_Sex_Var_2 == 2:
            show EP10_Conglomerate_Anim_10_Faster with Dissolve(1)
    if EP10_Conglomerate_Sex_Var_1 == 4:
        if EP10_Conglomerate_Sex_Var_2 == 1:
            show EP10_Conglomerate_Anim_11 with Dissolve(1)
        if EP10_Conglomerate_Sex_Var_2 == 2:
            show EP10_Conglomerate_Anim_11_Faster with Dissolve(1)
    menu:
        "Slower":
            $ EP10_Conglomerate_Sex_Var_2 = 1
            jump EP10_Conglomerate_Sex_4
        "Faster":
            $ EP10_Conglomerate_Sex_Var_2 = 2
            jump EP10_Conglomerate_Sex_4
        "View 1":
            $ EP10_Conglomerate_Sex_Var_1 = 1
            jump EP10_Conglomerate_Sex_4
        "View 2":
            $ EP10_Conglomerate_Sex_Var_1 = 2
            jump EP10_Conglomerate_Sex_4
        "View 3":
            $ EP10_Conglomerate_Sex_Var_1 = 3
            jump EP10_Conglomerate_Sex_4
        "View 4":
            $ EP10_Conglomerate_Sex_Var_1 = 4
            jump EP10_Conglomerate_Sex_4
        "Continue":
            $ different_choice_menu = False
            pass
    a "FUCK ME just like that!!!"
    a "OH... Fuck..."
label EP10_Conglomerate_Sex_5:
    $ config.menu_include_disabled = True
    $ different_choice_menu = True
    scene black
    hide EP10_Conglomerate_Anim_8
    hide EP10_Conglomerate_Anim_8_Faster
    hide EP10_Conglomerate_Anim_9
    hide EP10_Conglomerate_Anim_9_Faster
    hide EP10_Conglomerate_Anim_10
    hide EP10_Conglomerate_Anim_10_Faster
    hide EP10_Conglomerate_Anim_11
    hide EP10_Conglomerate_Anim_11_Faster
    if EP10_Conglomerate_Sex_Var_1 == 1:
        if EP10_Conglomerate_Sex_Var_2 == 1:
            show EP10_Conglomerate_Anim_8 with Dissolve(1)
        if EP10_Conglomerate_Sex_Var_2 == 2:
            show EP10_Conglomerate_Anim_8_Faster with Dissolve(1)
    if EP10_Conglomerate_Sex_Var_1 == 2:
        if EP10_Conglomerate_Sex_Var_2 == 1:
            show EP10_Conglomerate_Anim_9 with Dissolve(1)
        if EP10_Conglomerate_Sex_Var_2 == 2:
            show EP10_Conglomerate_Anim_9_Faster with Dissolve(1)
    if EP10_Conglomerate_Sex_Var_1 == 3:
        if EP10_Conglomerate_Sex_Var_2 == 1:
            show EP10_Conglomerate_Anim_10 with Dissolve(1)
        if EP10_Conglomerate_Sex_Var_2 == 2:
            show EP10_Conglomerate_Anim_10_Faster with Dissolve(1)
    if EP10_Conglomerate_Sex_Var_1 == 4:
        if EP10_Conglomerate_Sex_Var_2 == 1:
            show EP10_Conglomerate_Anim_11 with Dissolve(1)
        if EP10_Conglomerate_Sex_Var_2 == 2:
            show EP10_Conglomerate_Anim_11_Faster with Dissolve(1)
    menu:
        "Slower":
            $ EP10_Conglomerate_Sex_Var_2 = 1
            jump EP10_Conglomerate_Sex_5
        "Faster":
            $ EP10_Conglomerate_Sex_Var_2 = 2
            jump EP10_Conglomerate_Sex_5
        "View 1":
            $ EP10_Conglomerate_Sex_Var_1 = 1
            jump EP10_Conglomerate_Sex_5
        "View 2":
            $ EP10_Conglomerate_Sex_Var_1 = 2
            jump EP10_Conglomerate_Sex_5
        "View 3":
            $ EP10_Conglomerate_Sex_Var_1 = 3
            jump EP10_Conglomerate_Sex_5
        "View 4":
            $ EP10_Conglomerate_Sex_Var_1 = 4
            jump EP10_Conglomerate_Sex_5
        "Continue":
            $ different_choice_menu = False
            pass
    play audio jerk3
    play sound moaninglong_1
    a "Oh... Fuck... I'm getting close... AGHGHH."
    ea1 "YEAH. ME TOOO!!!"
    ea1 "AAHHH AAHHHHH OHHH"
    a "OOH FUUUCKKKK!"
    menu:
        "Cum in her mouth...":
            ea1 "Aahhh!!!!"
            a "MMMM!!!!!!"
            play audio cum_sound
            scene 38-4 oil 58 with flash_vpunch
            ea1 "AARRHHHHHH!!!!"
            scene 38-4 oil 59 with flash_vpunch
            pause
            with flash_vpunch
            scene 38-4 oil 60 with Dissolve(1)
            pause
        "Cum on her beautiful body...":
            ea1 "Ah... Ahh!!"
            a "CUM ALL OVER ME!!!"
            play audio cum_sound
            with flash_vpunch
            scene 38-4 oil 56 with flash_vpunch
            ea1 "mhh... Fuck..."
            scene 38-4 oil 57 with Dissolve(1)
            pause
    play music tranquility
    scene black with Dissolve(1)
    "After taking a breath..."
    scene 38-4 oil 61 with Dissolve(1)
    a "Well... How did you enjoy me?"
    ea1 "I'm at a loss for words, to be honest..."
    ea1 "I've never had such a woman..."
    scene 38-4 oil 62 with Dissolve(1)
    a "Hehe... I hope you are pleased."
    ea1 "Pleased is not even enough to praise you!"
    ea1 "More like fulfilled my life!"
    a "I enjoyed myself a lot as well..."
    scene black with Dissolve(1)
    play sound cloth_sound1
    $ persistent.scene_32 = True
    $ renpy.end_replay()
    scene 38-4 oil 63 with Dissolve(1)
    a "Well... That was something..."
    ea1 "Indeed!"
    scene 38-4 oil 64 with Dissolve(1)
    a "Ah, you're back!"
    ea2 "And everything is as should be, I assume?"
    scene 38-4 oil 65 with Dissolve(1)
    a "Yeah. We came to an agreement."
    ea1 "Yeah... We came indeed... Heh."
    ea2 "I'm glad to hear."
    ea2 "Madison and I also finished all 'dealings'."
    scene 38-4 oil 67 with Dissolve(1)
    a "We'd like to open a champagne, but plane's waiting."
    ea2 "Of course, never rest. We also have business to attend to. Other, deals to make heh."
    scene 38-4 oil 68 with Dissolve(1)
    a "It was very nice to meet you, Ahsan."
    ea1 "The pleasure was all mine. Come back soon, my lady."
    scene black with Dissolve(1)
    play sound walk
    scene 38-4 oil 69 with Dissolve(1)
    a "Well... we've got a deal!"
    scene 38-4 oil 70 with Dissolve(1)
    m1 "Went well?"
    a "Better than I expected."
    a "We will have another happy client."
    scene 38-4 oil 71 with Dissolve(1)
    if dianaGoodRelations == False:
        a "Anyway, Jeremy's probably waiting. Let's get back. Shall we?"
        m1 "Right away!"
    else:
        a "Alright, time to go. Short but a successful stay."
        m1 "We should come here on a vacation."
        a "Perhaps..."
    scene black with Dissolve(1)
    "After many hours..."
    stop sound
    stop audio
    $ EP10_var_14 = True
    if bar_var_1 == False:
        jump EP10_Patricks_Kid
    elif EarlHelp == False:
        jump EP10_Sergey_Warehouse
    jump EP10_Variable_Check
label EP10_Sergey_Warehouse:
    $ EP10_var_16 = True
    play music tense2
    scene 38-7 wa 1 with Dissolve(1)
    s1 "We are getting out of here!"
    s1 "We've got to leave the city for a while."
    c1 "I understand and agree, but wouldn't it be prudent for us to first examine the situation?"
    c1 "We have to take care of Anna, Rebecca and Michael."
    s1 "Michael is fine. he will lay low at Rebecca's. We are the two main faces now. Certainly me."
    s1 "Anna will be fine, too. She is a big girl. She proved that she can take care of herself. plus no one else knows about her inolvement."
    a "Guys?"
    scene 38-7 wa 2 with Dissolve(1)
    s1 "Ah. Anna. We've been waiting..."
    s1 "Excuse me."
    scene 38-7 wa 3 with Dissolve(1)
    s1 "How is everything?"
    s1 "How are you holding up?"
    a "Surprisingly well. I've got things to keep my mind occupied."
    s1 "That's good."
    a "So, what's up?"
    scene 38-7 wa 4 with Dissolve(1)
    s1 "We are planning to leave the town to lay low, but no one can take care of the warehouse and our 'business' while we are gone."
    s1 "Our contact at the police told us that they are looking for suspects."
    s1 "We don't know what the police know so we'd better get out of here for a while."
    s1 "Carl is reluctant to leave Rebecca and you and Michael unattended."
    s1 "He is too cautious. I'm not trying to be the coward here, but facts show that no one else knows about you or Rebecca."
    s1 "This is the one time when Carl isn't thinking with his head."
    scene 38-7 wa 5 with Dissolve(1)
    c1 "I'm... Sorry..."
    s1 "Don't be sorry, I understand, we just can't dwell here."
    c1 "I will go pack our stuff."
    s1 "Sure."
    scene 38-7 wa 6 with Dissolve(1)
    a "What if I helped with the warehouse?"
    s1 "You?"
    s1 "I would never ask, that is a lot of risk..."
    a "I overheard you saying that I'm a big girl and can take care of myself."
    a "I know plenty about your warehouse, plus I know some accounting from my office job."
    a "Let me show you."
    scene 38-7 wa 7 with Dissolve(1)
    a "See. I've got experience. I can track all records, I know how to clear funds through the proper channels."
    a "Plus everything you do here is through aliases anyway. No one will know that anything has changed."
    "Sergey was surprised."
    s1 "Huh..."
    s1 "Perhaps..."
    scene 38-7 wa 8 with Dissolve(1)
    a "I understand the shell company concept aswell, the shipping company is the front."
    a "And logistics of this warehouse aren't too complicated as I see."
    a "Will take some time to get used to, but I will manage."
    a "Plus, Carl has made a pretty clear cut system for the accounting, as I see."
    s1 "You've learned all of that from your work with us and in the office?"
    a "Well... Yeah, I suppose. I will have to do some manuvering with the money, set up some new accounts if needed."
    a "I understand the general principles of clearing the funds through. The placement, The layering, the integration."
    a "As I understand, you've got spreadsheets and flowcharts to visualize the scheme?"
    s1 "We do."
    scene 38-7 wa 9 with Dissolve(1)
    a "Then I should be easily able to draw clear lines through which funds get funneled."
    a "Obviously you've got offshore accounts in the Cayman Islands, and some in the Bahamas."
    a "Got a list of your accounts somewhere?"
    s1 "Yes, I keep everything in hard copies in the safe, hidden."
    a "Plus, the criminal activities, I've had my fair share with you guys."
    a "I should be able to handle some minor ones. You've got a way of tracking that as well?"
    s1 "Yes."
    scene 38-7 wa 10 with Dissolve(1)
    play music SexyTimeSong8
    s1 "To be honest..."
    s1 "I'm impressed."
    s1 "How did I never think of you?"
    scene 38-7 wa 9 with Dissolve(1)
    a "Cause you are careful with putting me in danger?"
    s1 "Oh, right... Well, if you can guarantee that you won't be putting your head out there and just making sure everything runs smoothly..."
    if SergeySexContent == True:
        play sound surprise
        scene 38-7 wa 11 with Dissolve(1)
        a "Now why would I do that?"
        a "I'm a careful lady."
        s1 "You are an 'everything' lady. intelligent, beautiful..."
        a "You are saying that just to make me blush..."
        s1 "I'm telling the truth."
        play sound cloth_sound1
        scene 38-7 wa 12 with Dissolve(1)
        a "Oh..."
        play sound kisspeck
        scene 38-7 wa 13 with Dissolve(1)
        a "Mm..."
        "She was enveloped by Sergey's manly arms..."
        "Anna craved his attention..."
        "His touch... His cock..."
        scene 38-7 wa 14 with Dissolve(1)
        c1 "Sergey..."
        c1 "If we are going, let's go now..."
        "Looking at them made him feel... Jealous?"
        "Or something else maybe..."
        scene 38-7 wa 15 with Dissolve(1)
        a "He's right. The sooner you are away from here... The better..."
        s1 "Yeah... I know..."
        s1 "Take care..."
    else:
        play sound surprise
        scene 38-7 wa 11 with Dissolve(1)
        a "Now, why would I do that?"
        a "I'm a careful lady."
        s1 "You are an 'everything' lady. intelligent, beautiful..."
        a "You are saying that just to make me blush..."
        s1 "I'm telling the truth."
        play sound cloth_sound1
        scene 38-7 wa 14 with Dissolve(1)
        c1 "Sergey..."
        c1 "If we are going, let's go now..."
        "Looking at them made him feel... Jealous?"
        "Or something else, maybe..."
        scene 38-7 wa 15 with Dissolve(1)
        a "He's right. The sooner you are away from here... The better..."
        s1 "Yeah... I know..."
        s1 "Take care..."
    scene 38-7 wa 16 with Dissolve(1)
    c1 "So... Anna will be taking over for now?"
    s1 "How did you figure?"
    c1 "Only logical conclusion..."
    c1 "Farewell, Anna."
    s1 "The key to the safe is one of the cupboards of the table."
    scene 38-7 wa 17 with Dissolve(3)
    a "Alright... Damn... I've taken a lot of responsibility..."
    a "Let's see what I'm working with..."
    a "I'm sure I can manage..."
    scene 38-7 wa 18 with Dissolve(1)
    a "I've got all the info..."
    a "This could become so much bigger..."
    a "Make changes, expand..."
    scene 38-7 wa 20 with Dissolve(1):
        zoom 0.5 xalign 0.5 yalign 0.5
        linear 10 zoom 0.6 xalign 0.5 yalign 0.5
    a "All that control..."
    pause 0.5
    scene 38-7 wa 21 with Dissolve(1):
        zoom 0.6 xalign 0.5 yalign 0.5
    a "Am I building an Empire here?"
    scene black
    jump EP10_Variable_Check
label EP10_Patricks_Kid:
    $ EP10_var_15 = True
    play music distantsong
    scene 35-5 barscene 1 with Dissolve(1)
    a "{i}...Alright, now to the office..."
    scene 35-5 barscene 2 with Dissolve(1)
    a "Still closed..."
    pause
    scene black with Dissolve(1)
    play sound door2
    scene 35-5 barscene 8 with Dissolve(1)
    a "Hey, Jim..."
    a "I kind of expected you to be here."
    j3 "Haven't really left."
    j3 "Been moving some money around, some witnesses or whatever. So that we are safe."
    scene 35-5 barscene 9 with Dissolve(1)
    pause 1.5
    scene 35-5 barscene 12 with Dissolve(1)
    j3 "Also, I called Lucas over... Tried to appeal to him."
    j3 "He is the only one who knows the password."
    a "Right..."
    j3 "What will you do if he asks something naughty of you in exchange for the password?"
    a "Nothing, shout at him. The whole reason why we did this is to escape Patrick's tyranny."
    j3 "True..."
    j3 "I will go do some cleanup, he should be here soon."
    a "Thanks."
    scene black with Dissolve(1)
    scene 38-5 lucas 1-2 with Dissolve(1)
    play sound doorknock
    pause 2
    play sound door2
    scene 38-5 lucas 1 with Dissolve(1)
    lu "Well. I'm here... What do you want?"
    a "Hi. Lucas..."
    scene 38-5 lucas 2 with Dissolve(1)
    a "Let me just start by saying, I'm very sorry about your loss..."
    a "I wish there was more I could've done..."
    scene 38-5 lucas 3 with Dissolve(1)
    lu "Bullshit..."
    lu "I don't believe you one bit..."
    lu "I'm sure you had something to do with it."
    scene 38-5 lucas 4 with Dissolve(1)
    a "Me?"
    lu "Yeah... I know you didn't like him..."
    lu "He was... harsh to you."
    scene 38-5 lucas 5 with Dissolve(1)
    lu "Probably cause you are an annoying, dumb slut."
    a "How can you say that?"
    a "You don't even know me."
    lu "I know enough."
    scene 38-5 lucas 6 with Dissolve(1)
    a "Listen. I will say it once."
    a "I did not kill your father, never intended to."
    a "I'm sorry about your loss."
    a "I understand why you are an asshole right now."
    with vpunch
    a "BUT GET A FUCKING GRIP!"
    scene 38-5 lucas 7 with Dissolve(1)
    lu "Umm..."
    lu "I..."
    lu "I don't have a way to get money anymore..."
    lu "He helped me with it..."
    scene 38-5 lucas 8 with Dissolve(1)
    a "Listen. Sorry."
    a "I'm trying to continue his legacy."
    a "But to do that, I need the password."
    scene 38-5 lucas 9 with Dissolve(1)
    menu:
        "Tell me the password. Then you might get some money...":
            $ EP10_Give_Lucas_Money = False
            lu "Alriight..."
            scene 38-5 lucas 15 with Dissolve(1)
            lu "qwertyshort_novel2023."
            a "Interesting."
            scene 38-5 lucas 13 with Dissolve(1)
            a "Alriiight..."
            a "Annnd..."
            play sound notifsound
            scene 38-5 lucas 14 with Dissolve(1)
            a "Great... Thank you."
            scene 38-5 lucas 15 with Dissolve(1)
            lu "So... How about the money?"
            scene 38-5 lucas 16 with Dissolve(1)
            a "You won't get any."
            lu "WHAT?"
            a "You are a little, annoying, unthankful brat."
            a "Go get a job."
            scene 38-5 lucas 17 with Dissolve(1)
            lu "You lied to me!"
            a "If you had been a nice person to me, maybe I would be nicer to you..."
            lu "Bullshit. You are an whore!"
            scene 38-5 lucas 18 with Dissolve(1)
            lu "This isn't over, bitch!"
            scene 38-5 lucas 19 with Dissolve(1)
            a "That's right. Leave, and don't come back."
            scene black with Dissolve(1)
            scene 35-5 barscene 16 with Dissolve(1)
            j3 "So. How did it go?"
            a "I got the password!"
            scene 38-5 lucas 17 with Dissolve(1)
            a "We are in. Now we can do everything."
            j3 "That is great. I will get right on it. I will probably need you to come back here again soon."
            j3 "We are setting up the biz!!!"
            j3 "How did you persuade him?"
            a "I promised to give him some money, but didn't."
            scene 35-5 barscene 16 with Dissolve(1)
            j3 "You tricked him?"
            j3 "I hope it doesn't come back to bite us in the ass..."
            a "It won't. he is a little rat."
        "If you give the password, I will pay some money up front.":
            $ EP10_Give_Lucas_Money = True
            a "What do you think?"
            lu "Sure... That sounds nice."
            lu "I need money now for school, since Patrick... Is... Is..."
            scene 38-5 lucas 10 with Dissolve(1)
            a "It's okey... You'll be fine."
            "Anna was in control of the broken, young man infront of her..."
            "Was it evil? Or was it survival instict?"
            scene 38-5 lucas 11 with Dissolve(1)
            a "So?"
            lu "Lemme think..."
            scene 38-5 lucas 12 with Dissolve(1)
            lu "qwertyshort_novel2023."
            a "Alright, interesting password."
            a "But as passwords go, not the worst."
            play sound notifsound
            scene 38-5 lucas 13 with Dissolve(1)
            a "Yes... Got it!"
            a "Thank you, Lucas."
            lu "So. What about the money?"
            scene 38-5 lucas 14 with Dissolve(1)
            a "Oh, yeah. gimme a sec."
            lu "OK."
            a "I won't give you a lot because we still need it for the bar..."
            scene 38-5 lucas 20-1 with Dissolve(1)
            a "How about..."
            a "10 grand?"
            lu "WHAAT?"
            a "Should cover you, right?"
            a "{i}...That will be enough for him to leave us alone..."
            scene 38-5 lucas 20 with Dissolve(1)
            a "Alright..."
            play sound whoosh_1
            scene 38-5 lucas 21 with Dissolve(1)
            a "Here you go. I hope you will keep this all a secret?"
            lu "Yes!"
            a "If you behave well, you will get more."
            "Lucas was completely oblivious to the nefarious plot he was a part of..."
            "The 10,000 $ clouded his mind."
            scene 38-5 lucas 22 with Dissolve(1)
            "Greedy... Like father, like son..."
            "But that was the best course of action for Anna. If she was to survive the world..."
            "If she allowed Patrick to degrade her... She would become nothing but a cum-dumpster."
            "She wouldn't allow it."
            scene black with Dissolve(1)
            play sound door2
            scene 35-5 barscene 16 with Dissolve(1)
            j3 "So. How did it go?"
            a "I got the password!"
            scene 35-5 barscene 17 with Dissolve(1)
            a "We are in. Now we can do everything."
            j3 "That is great. I will get right on it. I will probably need you to come back here again soon."
            j3 "We are setting up the biz!!!"
            j3 "How did you persuade him?"
            a "Gave him some money."
            scene 35-5 barscene 16 with Dissolve(1)
            j3 "How much?"
            scene 35-5 barscene 17 with Dissolve(1)
            a "10k..."
            j3 "Well, that's a small price to pay for an entire business."
            a "I agree."
    a "Alright, then. I will get going."
    a "Call me when you have something."
    j3 "Yes, ma'am."
    scene black with Dissolve(1)
    if EarlHelp == False:
        jump EP10_Sergey_Warehouse
    else:
        jump EP10_Variable_Check
label EP10_Variable_Check:
    scene black with Dissolve(1)
    jump EP11_Begin
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
