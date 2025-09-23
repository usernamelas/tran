label AlfredEventTwo:
    $ scene_music_tracks_one = ["audio/sounds/PPM - Waterside Harmony.mp3", "audio/sounds/Tranquility.mp3"]
    $ renpy.random.shuffle(scene_music_tracks_one)
    $ renpy.music.play(scene_music_tracks_one, channel="music", fadein = 1, fadeout = 1)
    scene black with Dissolve(1)
    "Anna went into the corridor of her building."
    scene 33-2 alfred 1 with Dissolve(1)
    "Anna enters the house corridor and wonders about the news Alfred has for her..."
    a "{i}..Curious. What is Alfred up to..."
    scene 33-2 alfred 2 with Dissolve(1)
    "Anna notices a package at the door."
    a "{i}...This can be no coincidence..."
    a "{i}...I wonder what's inside the bag..."
    scene 33-2 alfred 3 with Dissolve(1)
    "She picked up the bag..."
    "And didn't look inside. Perhaps, it was supposed to be personal."
    a "{i}...Alright..."
    "Anna didn't know what to expect. The bag was big enough to hold an outfit."
    "But it could hold something else, as well..."
    play sound doorknock
    scene 33-2 alfred 4 with Dissolve(1)
    "Anna knocked on the door."
    "No one was answering as of yet."
    "Anna became a little bit anxious."
    a "{i}...What if something happened to Alfred... He may need my help..."
    play sound door2
    scene 33-2 alfred 5 with Dissolve(1)
    "Suddenly, Alfred came out."
    a "Alfred, are you ok?"
    a2 "Hey, Anna. Yes, yes."
    a2 "I'm quite alright. I've been busy, running around the house and stuff."
    a2 "I've got some news to share, and I've been unable to sit down..."
    scene 33-2 alfred 6 with Dissolve(1)
    "Alfred noticed Anna's outfit only now."
    a2 "What is this? A different outfit? It's rather revealing..."
    a "I don't suppose you could give me some pointers on how to arrange my clothing better?"
    a2 "I can if you are looking to embellish your curves and such."
    scene 33-2 alfred 7 with Dissolve(1)
    a "Does this 'embellish my curves?"
    a2 "It absolutely does, but we could always make it better."
    a "What do you mean by that?"
    a2 "Well, we could make the butt cheeks stand out more, add some extra elements to it."
    a "I see. I will make sure to visit you at the shop as soon as I can."
    a2 "Whenever you can, you know we like when you visit."
    scene 33-2 alfred 8 with Dissolve(1)
    a2 "Anyway, I will put the bag down in my living room and then, maybe, you'd like to go for a walk?"
    a2 "At the park. I have somethings to tell you."
    a2 "And the news has made me really excited, I can barely contain myself... Hehe..."
    a "Whoa, Alfred. Take a second and calm down. Hah... You will exhaust yourself too much."
    a2 "No such thing, Anna. You will understand when I explain."
    play sound door2
    scene 33-2 alfred 9 with Dissolve(1)
    "Alfred quickly ran into his house."
    "Anna was left wondering about what's going on with him."
    "She was happy to see him so positive and full of energy."
    "Anna even wondered how that would translate to other things..."
    a "{i}...I like him like this... He's so... Funny and extra."
    play sound door2
    scene 33-2 alfred 10 with Dissolve(1)
    "Alfred exited the house and locked it."
    a2 "So. I'm ready to head out, are you?"
    a "I am, Alfred."
    a2 "I was thinking... The park? It's a very tranquil place, compared to the rest of the city."
    a "Sure, I haven't been to the park in some time. It would do me some good."
    $ renpy.sound.play("audio/sounds/city_traffic.mp3", fadein=1)
    scene 33-2 alfred 11 with Dissolve(1)
    a2 "So, how have you been?"
    a2 "Anything exciting, new?"
    if dianaGoodRelations == False:
        a "I was promoted at work, and I took the lead on a contract closing deal."
    else:
        a "I've become a partner at the firm I work at, and I lead a contract closing deal."
    a2 "That doesn't surprise me. You are such a smart girl."
    a "I suppose it comes with its perks."
    scene 33-2 alfred 12 with Dissolve(1)
    a "Other than that, I've been exploring myself a bit."
    a2 "Oh, do tell."
    a "Perhaps, in a more private place... hehe..."
    a2 "Oh, Anna. You know how to keep people interested."
    a2 "Anyway, I've been wanting to tell you something."
    a "Go ahead, I'm all ears."
    a2 "You remember how you encouraged me to do something about my relationship with my daughter?"
    a2 "I did, I started to reach out and search for her, and I've found the city she lives in."
    play sound surprise
    scene 33-2 alfred 13 with Dissolve(1)
    a "Really? That sounds like good news!"
    a2 "It is. I also contacted some friends who live there and asked them to send me a map and a phone book."
    a2 "Those were the things in the bag that you picked up at the door."
    a "Isn't that a bit of an old-fashioned way of finding someone?"
    a2 "Well, first of all, I'm old. Hehe. And second of all, I don't know how all those computer, GPS things work."
    a2 "I'd stick to tested methods."
    scene 33-2 alfred 14 with Dissolve(1)
    a2 "So the next step is to find last names that match mine and call them up."
    a "That will take a long time. I could try to help you. I know my way around computers."
    a2 "Well, if you can, I would be very grateful, but even so, I'm enjoying this challenge."
    a2 "I've never felt so good in my life, finally doing something about my relationship with my daughter."
    a2 "And all that thanks to you, Anna..."
    scene 33-2 alfred 15 with Dissolve(1)
    "He started to hold Anna's hand gratefully."
    a2 "You've helped me out so much during the time we know each other."
    a "Oh, Alfred... You are sweetheart, I could never turn you away..."
    a2 "I'm again getting those sensations of youthly strength and vigor."
    scene 33-2 alfred 16 with Dissolve(1)
    a2 "As if I could... I could climb Mount Everest!"
    a "Haha..."
    a "That is very admirable, honestly."
    a "I can only hope that I will be so lively at your age."
    a2 "It's all about the mindset. Trust me."
    a2 "Life doesn't stop when you hit, say, 60 years. You still want to live and enjoy."
    scene black with Dissolve(1)
    stop sound fadeout 1
    play sound BirdsInPark
    scene 33-2 alfred 16-1 with Dissolve(1)
    "They arrived at the park. Such a calm and relaxing place."
    a2 "I've always wanted to walk around in the park with you."
    a "Yeah, it helps me unwind a bit. I should've come here more often."
    a2 "A picnic here would be a great idea, what do you think about that?"
    a "Yeah, why not. Hehe..."
    scene 33-2 alfred 17 with Dissolve(1)
    "They had walked through the park for a while and decided to sit down."
    "Not far from them sat two 'gentlemen' talking about their problems."
    st3 "Bro, I'm telling you, this is a foolproof plan if we invest our money with this guy..."
    st3 "We will get back five-fold. I'm telling you."
    st4 "Bro, stop. I don't believe you anymore. You already lost your money by buying those coins."
    st4 "It's Hella stupid that you still fall for that shit..."
    st3 "Don't be like that... Fine, Imma make money, and you are gonna be left in the dust..."
    play sound surprise
    scene 33-2 alfred 18 with Dissolve(1)
    st3 "Whoa. Who is that bombshell..."
    st4 "I think... Wait... That's that girl, bro."
    st3 "What? You serious? She's got a very... revealing outfit and an old sugar daddy with her."
    st4 "Damn. Lucky bastard."
    scene 33-2 alfred 19 with Dissolve(1)
    a2 "So, yeah. I'm going to start looking for my daughter. Hopefully, I find her..."
    a "If you don't find her with your method then I can talk to some of my contacts and perhaps get some info."
    a2 "Oh, Anna. Ever so helpful..."
    a2 "You are a very amazing woman, you know that? When you offer your help, you remind me of my wife."
    scene 33-2 alfred 20 with Dissolve(1)
    a2 "It's weird, sometimes you remind me of my daughter, sometimes of my wife..."
    a "Thank you, Alfred. That means a lot to me."
    a2 "It means a lot to me, too, that you are always helping me out, you know?"
    a2 "It's nice to have young and good people in this world."
    a "Thanks, but I don't think I'm a good person... I try to be, but it often doesn't go that way..."
    scene 33-2 alfred 21 with Dissolve(1)
    a2 "You already said the keyword, you try to be."
    a2 "We don't have to always succeed, but as long as we are willing and learning."
    a2 "We will come out on top."
    a "You right, You always know the right words to get me, haha..."
    "Anna was inspired by the youthful and energetic Alfred, and he is persistent to find his daughter..."
    scene 33-2 alfred 22 with Dissolve(1)
    "Anna's nipple was peaking out, but none of them had noticed. They just kept talking and talking."
    "Anna was also feeling some interesting sensations..."
    "She also, yet again, felt safe. Like before, when Alfred was at her place."
    a "You are a very respectable man, Alfred. I really like you."
    menu:
        "Anna thought that she could get a bit naughty with Alfred.":
            jump AlfredEventTwoSexIntro
        "Anna decided that she wants to stop and not take it further.":
            pass
label AlfredEventTwoLeave:
    scene 33-2 alfred 21 with Dissolve(1)
    a "Oh, I received a message."
    a "I think we will have to leave it here because I have some things to attend to."
    scene 33-2 alfred 19 with Dissolve(1)
    a "Anyway, it was nice walking around with you and all that."
    a "We should do it again sometime."
    a2 "Ah. Ok, no problem, Anna. It was very nice to meet you."
    $ alfred_var_one = True
    $ alfred_var_three = True
    scene 33-2 alfred 81-1 with Dissolve(1)
    $ renpy.end_replay()
    $ persistent.thirteenthScene = True
    if EarlHelp == True:
        "Anna received a message to meet up with Earl."
        "She immediately got shivers and got nervous."
        jump EarlEventThree
    if CarlHelps == True or TaxmanHelps == True:
        "Anna received a message. It was from Sergey."
        "He asked for Anna to come to the warehouse."
        a "{i}...Oh... Now time to get down to business..."
        jump SergeyEventTwo
    return
label AlfredEventTwoSexIntro:
    play audio BirdsInPark
    scene 33-2 alfred 23 with Dissolve(1)
    a "Perhaps, you need a reward for all of your kind words."
    "Anna felt ripples go through her body. She was excited to try out this kind of an approach."
    a2 "What do you have in mind, dear Anna?"
    a "Just be patient, and you will find out, hehe..."
    scene 33-2 alfred 24 with Dissolve(1)
    st3 "Dude, she's going all out on that old man. I think I know him..."
    st4 "Yeah, it's her neighbor Alfred."
    st3 "How do you know that?"
    st4 "I just have eyes and ears, bro. I know stuff."
    st4 "This is getting intense. I wonder if they will fuck. That's kind of a lot."
    st3 "Yeah, I'd rather prefer if we could fuck her, not some old fool."
    scene 33-2 alfred 25 with Dissolve(1)
    a "Ah, what do we have here... hehe..."
    a2 "As you'd expect, my excitement translates to every aspect of my life..."
    a "I wouldn't have it any other way, Alfred."
    scene 33-2 alfred 26 with Dissolve(1)
    a "Do you wish to enjoy some alone time only between the two of us?"
    a2 "Oh, Anna. You always come up with these requests that I cannot deny."
    a2 "No man in his right mind would deny such great ideas."
    a "In that case, I will go to the toilet now, and you decide if you wish to join me in there..."
    a "Stay here and wait for a bit, then come and find me."
    scene 33-2 alfred 27 with Dissolve(1)
    "Anna got up and started walking towards the toilets."
    "piercing Alfred with a succulent gaze. He was so enchanted by her, he could barely contain himself."
    a2 "{i}...Oh, Anna... You will be the death of me..."
    a2 "{i}...But I want you so bad right now..."
    scene 33-2 alfred 28 with Dissolve(1)
    a "{i}...Alfred will get what's coming to him..."
    a "{i}...I will make him enjoy himself so much..."
    "Anna couldn't contain her own excitement."
    play sound undress
    scene 33-2 alfred 29 with Dissolve(1)
    "She entered the toilet and left the door halfway open."
    "So that Alfred would see what he's signing up for."
    "All of Anna with no strings attached..."
    "Alfred was convinced that he was already in heaven, and this was only a little glimpse of his paradise."
    scene 33-2 alfred 30 with Dissolve(1)
    "Anna looked back and waited..."
    "Showing even more skin, her ass crack peeking out, craving Alfred's attention."
    a2 "{i}...I can't believe... this girl... Ah..."
    "Alfred waited even longer, looking at what Anna will do next..."
    scene 33-2 alfred 31 with Dissolve(1)
    "Meanwhile, the two men also noticed Anna and were in complete awe..."
    st3 "What the fuck is going on... She is literally seducing him..."
    st4 "But why? I can't wrap my fingers around that idea..."
    st3 "Maybe to get something out of him."
    st4 "Perhaps... Or maybe the answer is much simpler..."
    st3 "Like what..."
    scene 33-2 alfred 32 with Dissolve(1)
    "Anna entered deeper into the toilets and hid behind the wall."
    "She laid in wait for Alfred to come in and take her for all she's worth..."
    "To make her feel safe, wanted, desired, cared for..."
    scene 33-2 alfred 33 with Dissolve(1)
    "Alfred got up in a quick motion..."
    "Started walking towards the bathroom stall in quick, small steps."
    st3 "He is actually going in!"
    st4 "Holy shit... Either she is really trying to get something out of him, or that man's got game..."
    st3 "Don't be ridiculous. She is just probably a nympho."
    scene 33-2 alfred 34 with Dissolve(1)
    "Alfred entered a pleasing view."
    "Anna was hiding behind the bathroom stall."
    "Both of their hearts beating faster in the excitement."
    "Both of them looking forward to the experience that was about to take them both..."
    scene 33-2 alfred 35 with Dissolve(1)
    "Anna knew it was Alfred. And she was not going to stop until she gets what she wants."
    "Slowly pushing her panties lower and lower. She knew what she wanted, and she knew she will get it."
    a2 "Anna... Wha... I..."
    a "Come closer, please... I have something to tell you..."
    scene 33-2 alfred 36 with Dissolve(1)
    "Alfred approached her... Trying to act all innocent."
    a2 "Are you ok, Anna? What do you wish? Do you need some help?"
    a "I need something indeed... But... Are you up for the task?"
    "Anna decided to not hesitate at all anymore."
    play audio door2
    play audio lighthit
    scene 33-2 alfred 37 with vpunch
label AlfredSexReplayOne:
    "Anna pushed Alfred against the wall..."
    "Her intentions were clear. And Alfred was not going to stop her..."
    a2 "Oh... Anna... You are... very vigorous..."
    a "Just like you are today... Can you handle all of me, Alfred?"
    a2 "I can. And I want to!"
    play sound undress
    scene 33-2 alfred 38 with Dissolve(1)
    a "Do you like what you see?"
    a2 "I do... And the view is amazing..."
    a "Don't worry about anything... You are an amazing man, Alfred..."
    a "And you deserve everything good in the world."
    scene 33-2 alfred 39 with Dissolve(1)
    a2 "Anna... Ah... Are you sure this is the right place?"
    a "Don't you like a bit of excitement? A bit of thrill?"
    a2 "Yes... I definitely do."
    a "Exactly, You'd like if someone saw a young girl pleasuring you..."
    a2 "I... Oh, Anna."
    a2 "I can barely handle you."
    play sound undress
    scene 33-2 alfred 40 with Dissolve(1)
    a2 "Ahh..."
    "Anna put her hands on Alfred's dick, and he immediately felt strong sensations from her hands."
    a2 "Ahh... Your touch..."
    a "And I'm going to give you everything you desire..."
    scene 33-2 alfred 43 with Dissolve(1)
    "Anna's strokes were slow and concentrated on the erect penis."
    "Alfred was full of desire that he was trying to not show to Anna."
    "He wanted to seem kind and gentle, but, oh, how he wanted to ravage her..."
    play sound jerk
    scene 33-2 alfred 44 with Dissolve(1)
    "As she was stroking Alfred, she leaned in for a kiss."
    "She was greeted with a very eager response from Alfred, who quickly closed the gap..."
    "He was still trying to contain himself as Anna's hands rubbed his cock with seductive strokes."
    a "Mhfff.."
    a2 "Ah...Mf.."
    scene 33-2 alfred 45 with Dissolve(1)
    "Their kiss had become deep, and they both were enveloped by it."
    "Licking each other's tongues and getting their saliva everywhere."
    "Some of it was dripping down on the ground, and some of it got on Alfred's stick."
    a2 "{i}...Fuck me... Anna is so hot... I'm so hard right now..."
    a2 "{i}...Let me just take off those panties..."
    play sound undress
    scene 33-2 alfred 46 with Dissolve(1)
    "Alfred moved his hands and started to push the skirt down lower."
    "He did it slowly and sensually, and as he did it, Anna was shaking a bit."
    "Warm sensation was taking over her body as she was pleasuring Alfred."
    a "{i}...Damn, I'm... I'm getting kind of hot right now..."
    a "{i}...How does Alfred do this..."
    play sound undress
    scene 33-2 alfred 47 with Dissolve(1)
    "The piece of clothing hit the ground, and Anna was left with her ass exposed..."
    a2 "Whoops, sorry, Anna..."
    a "Oh, you dirty old perv, hehe..."
    scene 33-2 alfred 48 with Dissolve(1)
    "Anna looked Alfred in the eyes. Both of them fired up, ready to go."
    "Alfred was full of lust, passion, and vigor. Ready to penetrate Anna at a moment's notice."
    a "I think you will like what I have in mind next... hehe..."
    "Alfred had no idea what to expect..."
    scene 33-2 alfred 49 with Dissolve(1)
    "She braced against Alfred, lifted her leg, and started to rub her pussy lips against his erect length."
    "Alfred was just so... surprised. But he welcomed the opportunity."
    a2 "Oh, Anna... So beautiful, so radiant... As always..."
    a "Ah... Your dick rubbing against my entrance is already making me go crazy."
    scene 33-2 alfred 55 with Dissolve(1)
    st3 "Bro, what do you think they're doing in there?"
    st4 "That's a good question. But I have a pretty good idea."
    st3 "Exactly, my guy. I was thinking, maybe we go take a look?"
    st4 "Fuck it, what are they gonna do? Beat us up? Haha..."
    play sound door2
    scene 33-2 alfred 56 with Dissolve(1)
    "Both of the men quickly enter the toilets. Trying to make as little noise as possible."
    st3 "Try to stay quiet. We don't want to startle them. Maybe we could get some good material."
    st4 "Yeah. We could show her what we've got..."
    st3 "Precisely. See, my ideas can work out sometimes."
    st4 "Gotta admit this is one of your better ideas."
    scene 33-2 alfred 57 with Dissolve(1)
    "They whispered kinky things amongst each other."
    st3 "Holy shit, look at the legs, they're going at it, looks like."
    st4 "You can hear the kissing sounds, or is he already dicking her down?"
    st3 "I've got no clue. Let's take a look, shall we?"
    st4 "Be my guest, man."
    scene 33-2 alfred 58 with Dissolve(1)
    "Alfred was rubbing his dick against Anna's snatch, and both of them had become very hot..."
    a2 "Ah... Anna... You are torturing me..."
    a "Hehe... I know, I like to do that..."
    a2 "Oh, you devilish minx..."
    scene 33-2 alfred 59 with Dissolve(1)
    "Suddenly, Anna noticed that there was a phone from under the stall."
    menu:
        "Anna decided to go through with it and get filmed...":
            "Someone was filming them... And that turned Anna on even more."
            a "{i}...Oh... This is... Very interesting, someone wants to see how I get fucked by an old man..."
            $ AnnaCorruption +=1
            $ corruption_func("Anna Corruption +1")
            jump AlfredEventTwoSexContinue
        "Anna realized that it's against her better judgment.":
            scene 33-2 alfred 60-1 with Dissolve(1)
            a "{i}...No, I have to stop... I can't."
            a "I'm sorry, Alfred, we have to stop here. This place isn't a good idea."
            a2 "Oh, That's is of no problem, we can find some other place and some other time."
            a "Exactly."
            $ renpy.end_replay()
            jump AlfredEventTwoSexNoContinue
label AlfredEventTwoSexNoContinue:
    play sound door2
    scene 33-2 alfred 80 with Dissolve(1)
    a "I'm sorry, we were in the mood, but something ruined it."
    a2 "Oh, I'm sorry if I overstepped."
    a "It wasn't you, Alfred. Definitely not you."
    a "But we will have to continue this some other time."
    a "I have some important things to attend to right now..."
    a "I'm sorry again, I promise I will make it up to you."
    scene 33-2 alfred 81-1 with Dissolve(1)
    $ renpy.end_replay()
    $ persistent.thirteenthScene = True
    if EarlHelp == True:
        "Anna received a message to meet up with Earl."
        "She immediately got shivers and got nervous."
        jump EarlEventThree
    if CarlHelps == True or TaxmanHelps == True:
        "Anna received a message. It was from Sergey."
        "He asked for Anna to come to the warehouse."
        a "{i}...Oh... Now time to get down to business..."
        jump SergeyEventTwo
    return
    return
label AlfredEventTwoSexContinue:
    play music closure
    scene 33-2 alfred 60 with Dissolve(1)
    a "Alfred... I want you to do something for me..."
    a2 "What is it, Anna?"
    a "I want you to... To stick that dick inside of my wet pussy..."
    a2 "Sweet mercy... I have to do that, indeed."
    scene 33-2 alfred 61 with Dissolve(1)
    "Alfred put the tip against Anna's entrance and rubbed around for a moment."
    "That coupled with the fact that Anna knew she was being filmed sent her over the edge..."
    a "{i}...This is so hot... I can't even think straight..."
    a2 "Oh, dear... Here I come..."
    "Anna's pussy was dripping. The entry inside would take no effort."
    play sound jerk
    scene 33-2 alfred 62 with Dissolve(1)
    with vpunch
    a "Ah... Fuck."
    "Alfred pushed his dick inside of Anna in one motion."
    "He went balls deep into Anna at a moment's notice."
    a "Fuuckk... Ah..."
    "Anna was already enjoying herself a lot. The tingling sensation was taking over her head..."
    a2 "Fuuckk... Your pussy..."
    scene 33-2 alfred 63 with Dissolve(1)
    "They both seemed in ecstasy. Out of their minds..."
    a "{i}...Fuck... This dick... It hits different..."
    "Alfred continued his motion and set a steady pace to give Anna the dicking she needed."
    a "Fuck me, Alfred... Fuck me!"
    a "Ahhh...."
    play sound jerk2
    scene 33-2 alfred 64 with Dissolve(1)
    "Alfred pushed Anna against the wall with his dick and continued to fuck her with his extra erect penis."
    a2 "{i}...Anna is so amazing... She's always making me enjoy the world so much more..."
    a "{i}...Alfred knows how to fuck a woman..."
    a "Ahhh... Your fucking me so good..."
    play sound moaningfour
    show AlfredSexOne with Dissolve(1)
    "They both transitioned to explicit moaning and sex-filled moment."
    "Both of them were right where they wanted to be, doing exactly what they wanted to do."
    a "Dick me down... Alfred!"
    a2 "Yes... Ahh..."
    show AlfredSexTwo with Dissolve(1)
    hide AlfredSexOne
    "He was penetrating her inner walls deeply. So deeply that she could feel it within her stomach, almost."
    "She felt every little detail of his penis."
    "And Alfred was just ecstatic about the sensations that Anna's pussy was putting on him."
    "He could feel how she was just trying to grip his cock with her lips even more."
    play sound moaningfive
    show AlfredSexThree with Dissolve(1)
    hide AlfredSexTwo
    "Meanwhile, the two voyeurs were filming the ongoing 'exchange'"
    "They both were getting exactly what they wanted... And Anna..."
    "She was fulfilling fantasies that she had buried deep within."
    "She was slowly unleashing her inner desires and sluttiness."
    scene 33-2 alfred 65 with Dissolve(1)
    hide AlfredSexThree
    a "This is so good, Alfred. You can't even imagine..."
    a "Ahh..."
    a "Fuck me like you meant it. Fuck me harde,r Alfred... Ahh..."
    "Alfred was as vigorous as ever. The idea of stopping didn't even cross his mind."
    "He was fucking her like a bull."
    play sound moaningfour
    scene 33-2 alfred 66 with Dissolve(1)
    "He lifted up her leg and started to go even harder."
    a "Go as deep as you can..."
    a2 "You read my mind completely, Anna..."
    "They were fucking with temptation that couldn't be matched."
    scene 33-2 alfred 67 with Dissolve(1)
    "Anna looked directly into the camera and showed her face of pleasure."
    "She couldn't understand why it turned her on, but it did..."
    a "{i}...What is happening to me. Why is the camera turning me on even more..."
    a2 "Fuuck... Your pussy. As good as a fresh shower after a hot day. My entire body is full of sensation..."
    a "Aahh... Alfred... Oh... Fuck..."
    play sound moaningfive
    scene 33-2 alfred 68 with Dissolve(1)
    "But that was not the end of it."
    "Alfred knew he wanted to go further. He wanted to fuck Anna like sex possessed demon."
    "To penetrate that pussy harder and deeper than he had ever done before, or at least try."
    "He picked up Anna with both of his arms. Using all the strength and power, he could muster..."
    "So that he could go as deep as he possibly can..."
    play sound moaningfour
    show AlfredSexFour with Dissolve(1)
    "And so he went in even deeper. The tip of his penis was so erect he filled Anna's pussy completely full."
    a "My pussy!!!! AAHHH"
    "The moans were getting louder and louder as Anna was unable to contain herself anymore."
    show AlfredSexFive with Dissolve(1)
    hide AlfredSexFour
    a "{i}...So amazing... So great... Ahh..."
    a2 "Anna is just... ahh... I wish to do this to her every day..."
    a2 "That makes me so happy... She is so amazing..."
    "Both of them just enjoying the moment to the fullest."
    a "Harder, Alfred... Harder!!!"
    scene 33-2 alfred 69 with Dissolve(1)
    hide AlfredSexFive
    a "Alfred... You know how to handle me..."
    "Anna's tits were looking right at Alfred. He loved the view of Anna's face and her luscious breasts."
    a2 "You are so beautiful, and your chest is just... Amazing..."
    a2 "Ahhh..."
    "Alfred was ravaging Anna's pussy, and she loved every moment of it."
    scene 33-2 alfred 70 with Dissolve(1)
    "Anna's ass cheek clapping and their moans were so loud, they could be heard from outside the toilet."
    a "It's so deep..."
    a "Aahhhhh...."
    play sound moaningfive
    show AlfredSexSix with Dissolve(1)
    "Alfred was clapping her hard. Reachin the penultimate pleasure."
    "The climax was about the erupt harder than Yellowstone national park would in the movie 2012..."
    "He was about to give her loads large than sperm whales release in their whole lifetime."
    "It was all or nothing for Alfred!"
    a "Ahhh... Alfred!!!"
    a2 "ANNAAAA!!!!"
    with flash
    with flash
    a2 "FUUUCK HERE I COME!!!!"
    with flash
    play sound moaningfive
    a "FILL ME UP COMPLETELY!!!"
    a "Fill my womb with your cum!!!"
    with flash
    a "AAAHHH."
    a2 "I'm CUMMINGG!!! AHHH"
    scene 33-2 alfred 71 with Dissolve(1)
    hide AlfredSexSix
    "She was reaching pleasure so deep, her body started to tremble and shake. Her legs were shaking from the climactic sensation."
    "The sensation was so strong her eyes rolled back into her head involuntarily..."
    a "Aah... Fuck... Ahh... Mh..."
    scene 33-2 alfred 72 with Dissolve(1)
    "Alfred came deep into her pussy... His balls were getting drained of all the possible semen."
    "He was filling Anna's pussy so much it was spilling out while his dick was still inside."
    "Completely covering the entire inner pussy of Anna."
    a2 "AAAHHHHH."
    play sound jerk2
    scene 33-2 alfred 73 with Dissolve(1)
    "As he was pulling out, a large blob of cum just instantly came guzzling out."
    "dripping all over the floor."
    "Large streams continued to exit Anna's pussy. It had been a total eruption of Alfred's cock."
    scene 33-2 alfred 74 with Dissolve(1)
    a2 "I... I'm so amazed... So drained and exhausted, but feeling so fucking amazing..."
    a2 "Anna... You're celestial... Dear, sweet Anna."
    a "Alfred... You are so good... I can't explain with words, even..."
    "Both of them were exhausted, but even more so, Anna. She had completely blacked out for a second from the explosive climax."
    a2 "Come here..."
    play sound jerk
    scene 33-2 alfred 75 with Dissolve(1)
    "Alfred kissed Anna passionately."
    "Their lips were almost glued together."
    a "Mff... Mh."
    "Alfred was not only a good fucker, but also a good kisser..."
    "He kept amazing Anna. It could be said that with age comes experience..."
    scene 33-2 alfred 76 with Dissolve(1)
    "Meanwhile, our dear voyeurs had gotten all the content they needed."
    "They decided that it was good time to bolt."
    st3 "Let's get out of here, bro."
    st4 "Yeah, before we get made."
    st4 "I don't want any misconduct. My slate is clean so far."
    scene 33-2 alfred 77 with Dissolve(1)
    "Anna sat down to push out the rest of the semen and clean herself up."
    a2 "How are you feeling, Anna?"
    a2 "Are you ok?"
    a "I'm better than ok. I've been awaiting this kind of an opportunity..."
    a "It was so good that I'm still coming down from the sensation..."
    a "It was very... intense..."
    scene 33-2 alfred 78 with Dissolve(1)
    a "This was truly wonderful, Alfred."
    a2 "Well... I'm glad I was able to satisfy you, Anna."
    a2 "It's all I've ever wanted to do, to help you."
    a2 "But I can't believe that we did it in a public toilet..."
    a "That is what makes it fun."
    a "Anyway, it was all so nice. I hope you succeed at looking for your daughter."
    a "We should do this sometime again..."
    a2 "Absolutely, I wouldn't say no to that, Anna."
    play sound door2
    play audio BirdsInPark
    play music tranquility
    scene 33-2 alfred 79 with Dissolve(1)
    "As they exited, the two strangers were looking at their filmed material..."
    "Anna noticed them..."
    a2 "That was other-worldly. But I have to go now. Will you be ok?"
    a "Yeah, I still have some stuff to do around town."
    a "{i}...Oh... Now I don't know if it was such a good idea..."
    a "{i}...I hope they don't do anything with that material..."
    a "Ok, Alfred. Take care. I will see you soon."
    a2 "You too, Anna. Goodbye."
    scene 33-2 alfred 80 with Dissolve(1)
    "They saw that Anna was staring..."
    st3 "Oh, shit. I wonder if she will come over and say anything..."
    st4 "I don't think so... I hope not. Remember, she was pretty slutty in the train..."
    st3 "Yeah, your right, bro."
    scene 33-2 alfred 81-1 with Dissolve(1)
    $ renpy.end_replay()
    $ persistent.thirteenthScene = True
    if EarlHelp == True:
        "Anna received a message to meet up with Earl."
        "She immediately got shivers and got nervous."
        jump EarlEventThree
    if CarlHelps == True or TaxmanHelps == True:
        "Anna received a message. It was from Sergey."
        "He asked for Anna to come to the warehouse."
        a "{i}...Oh... Now time to get down to business..."
        jump SergeyEventTwo
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
