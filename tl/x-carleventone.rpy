label CarlEventOne:
    scene 32-1 earl 67 with Dissolve(1)
    "Anna picks up the phone and immediately calls Carl."
    c1 "Ye... Yeah? Anna? Why are you calling me this late in the night?"
    a "I can't say much, but... I need your help... I'm in the precinct right now."
    a "I didn't know anyone else, who I could call. I'm sorry to be putting you in danger like this."
    a "I need you to come and help me get out. I know you know things about the law."
    scene 32-1 earl 68 with Dissolve(1)
    c1 "Ah, Anna what were you thinking... Ah... Don't worry..."
    c1 "What's happened? Did the investigator Earl arrest you?"
    a "Yeah..."
    c1 "That's what I was afraid of..."
    c1 "Earl is unpredictable..."
    a "I'm sorry, I need your help."
    c1 "Yeah, it's fine. I'm on my way... I will be there in no time. Sit tight."
    scene 32-1 earl 69 with Dissolve(1)
    a "There. I'm not helping you! You've got no right to keep me here any longer."
    earl "Hehe... You are tough, I will give you that."
    earl "And that loyalty. I'm impressed. I rarely see it."
    earl "But it will come back to bite you in the ass. No honor amongst thieves and all that."
    earl "You've made a terrible enemy, Anna!"
    a "I don't care. You are a terrible man!"
    earl "Keep telling yourself that!"
    scene black with Dissolve(1)
    "After a little while Carl arrives at the precinct."
    scene 32-1 earl 70 with Dissolve(1)
    c1 "Hello, I've received a call from a distressed citizen from the precinct!"
    c1 "She is being held here against her will!"
    c1 "The person in question is named Anna."
    c1 "Under the state law she cannot be arrested without probable cause and legible proof! Even when under suspicion!"
    cop1 "Ah... I knew this will happen."
    c1 "You bet! If you do not release her I will write a legal statement to the city council to investigate this abuse of power."
    scene 32-1 earl 71 with Dissolve(1)
    cop1 "Alright, alright. I was not on board with this anyway. I've been cut out of this investigation, too."
    c1 "I've no idea what investigation you are talking about, however, I demand that you release her!"
    cop1 "Listen, pal... You don't make the demands here, but in any case, I have to comply..."
    cop1 "Because I agree with you."
    cop1 "What's your name again?"
    c1 "I'm not obligated to reveal my identity as a privacy concern. I was called here by the victim."
    c1 "But, you, on the other hand, are supposed to give me your name and police id in case I want to file a complaint."
    cop1 "You are smart, I will give you that. Alright, My name is Desmond and my police id is A55-B4ND1T."
    c1 "Thank you. Now, I will kindly ask you to release the person in question."
    play sound door2
    scene 32-1 earl 72 with Dissolve(1)
    cop1 "Earl! You son of a bitch. You have to release her. Anna's representative knows his stuff."
    cop1 "If we do not, You risk jeopardizing both of our careers and our freedoms even, maybe."
    earl "Sure, whatever. I'm done here anyway. I will find another way to catch the bad guy."
    earl "I will, however, escort Anna."
    cop1 "Sure... Sure..."
    play audio door2
    play audio surprise
    scene 32-1 earl 73 with Dissolve(1)
    "They exited the interrogation room and Earl wanted to look at the person Anna had contacted."
    "He wanted to imprint his face in his mind."
    c1 "Thank you for complying with the rules. If I find that this person has sustained any emotional trauma..."
    c1 "I will file the complaint with the city council and police head of department."
    earl "Cut the crap, bullshit, legal talk. I know this."
    earl "And I know how someone as educated as you would bend the rules to benefit themselves."
    c1 "I have no reason to comment or state an argument regarding this."
    earl "Whatever, get the hell out of here. I will be watching you both!"
    scene 32-1 earl 74 with Dissolve(1)
    c1 "Anna. Are you alright? Did he hurt you?"
    earl "You are both in my mind right now. I will get to the bottom of this."
    $ relationship_func_decrease("Earl Relationship -2")
    a "Yeah... Yeah... I'm fine. Let's get the hell out of here."
    c1 "Alright."
    play sound carsound
    scene 32-1 earl 75 with Dissolve(1)
    "Anna felt a slight release of tension..."
    a "I can't believe all this, Carl. He is dangerous. He knows stuff..."
    c1 "Yeah, I know... It was a big risk I took showing my face there..."
    c1 "Luckily I know how to keep myself 'legit' and out of trouble... Mostly..."
    scene 32-2 carl 3 with Dissolve(1)
    c1 "Are you alright, Anna? How are you feeling?"
    a "I'm a bit shaken, but much better now. It's so good to see you."
    c1 "Alright, I will take you home. Or maybe you would like to come to our place?"
    a "Hmm... That might be even better, Sure, Carl. Thanks."
    a "I'm happy that there are people I can rely on."
    c1 "Well, you've helped me in the past."
    c1 "Not even talking about the fact that you are Rebecca's sister."
    c1 "But regardless. Now is not the time and place to discuss all of this."
    c1 "Come on, let's go home."
    scene black with Dissolve(1)
    "After a short ride they arrived at Carl's place."
    play sound door2
    scene 32-2 carl 4 with Dissolve(1)
    $ renpy.music.play("audio/sounds/Purple Planet Music Chill Factor 80bpm.mp3", channel = 'music', if_changed = True)
    "They parked and quickly got inside."
    a "Ah... This place. Always nice to come back here."
    c1 "Yeah. Please, make yourself comfortable."
    c1 "Need anything? Coffee? Tea?"
    a "This late at night? You jest."
    c1 "Simply being courteous, that's all, Anna. Hehe..."
    a "Thank you again for your help. I know you took a big risk coming to the station."
    c1 "Yeah. But don't fret about it."
    scene 32-2 carl 5 with Dissolve(1)
    a "Regardless... I don't know... Perhaps I could have called someone else?"
    c1 "I don't know, but that doesn't matter now."
    c1 "I knew you were in trouble and I knew how to get you out of it."
    c1 "That's what matters. That you are safe. Rebecca would never forgive me if I didn't help... Neither would I."
    a "Thank you, Carl."
    a "Is it ok if I take a shower and cool off? Rebecca's sleeping though."
    c1 "Oh, don't worry about it, you can take a shower, no problem."
    scene 32-2 carl 6 with Dissolve(1)
    "They both go upstairs."
    c1 "I was just catching up to some late reading at night. She's been out for a couple of hours already."
    c1 "I didn't want to worry her, so I just let her sleep."
    a "Yeah, you and I both know how she can get when her sleep gets disturbed."
    c1 "Hehe... All over the place. She'd probably end up coming with me and beating up the cop."
    a "That would be a sight to see..."
    scene 32-2 carl 7 with Dissolve(1)
    a "Look at her. So beautiful... And sleeping like a puppy."
    a "I rarely got to watch her sleep, she was the one, usually, taking care of me."
    a "Keeping my spirits up. Tucking me in..."
    c1 "Huh, I never knew that."
    a "Well, I don't really talk to anyone about it. Never a reason to bring it up."
    a "I'm so grateful for her, though... Which is why I'm scared of what might happen."
    c1 "Don't mention it right now. Let's talk about it some other time."
    scene 32-2 carl 8 with Dissolve(1)
    c1 "Well, I'll probably nap on the couch and you can sleep with your sister."
    a "Ah, are you sure? Ok. It's been a trying day..."
    c1 "Absolutely. That might make you feel safer."
    a "Sure. Thanks, Carl."
    c1 "Don't mention it."
    play sound shower2
    scene 32-2 carl 9 with Dissolve(1)
    "Anna undressed and went under the warm water."
    "The day had been very colorful... And worrying."
    "Anna couldn't stop thinking about what the detective said."
    "She looked at her sister and wondered if she had made the right choice."
    "If not helping the detective was the correct thing to do..."
    a "{i}...I hope I don't get Rebecca in trouble with this. I can't lose her like this..."
    scene 32-2 carl 10 with Dissolve(1)
    "The shower did little to help Anna relax and forget about the events of the day."
    "But she tried her best to not think..."
    a "{i}...No way going back now. Only forwards..."
    a "{i}...I have to explain the situation to them as soon as possible..."
    scene 32-2 carl 11 with Dissolve(1)
    "As anna touched herself all around she felt extra sensitive down there."
    "Was it from all the stress..."
    if SergeySexContent == True:
        "Or was it from the intense session with Sergey..."
    "Anna wasn't sure, but she was certain about the fact that she was getting hot by just touching it."
    a "{i}...All this drama is creating a rush in my head... Even if I'm scared for some reason this time I'm also excited..."
    a "{i}...Living dangerous, the bad Anna... leader of the criminal underground in Suncity..."
    with vpunch
    a "{i}...What am I thinking??..."
    "Crazy thoughts were flooding Anna's mind and that made her feel extra aroused."
    play sound surprise2
    scene 32-2 carl 12 with Dissolve(1)
    "After she'd finished with the shower, Carl was standing there."
    a "Oh... I didn't see you there... How long have you been standing here?"
    c1 "Oh, I just got here... Don't worry, I wasn't peaking."
    c1 "I just remembered that there is no towel here."
    a "I'm not worried about that..."
    c1 "Great... I mean, all good then."
    play sound undress
    scene 32-2 carl 13 with Dissolve(1)
    "As anna started to dry herself she notices Carl still standing there..."
    a "Sorry, did you forget something? Why are you still standing here?"
    c1 "Well... I just got lost in thought for a second..."
    a "About what?"
    c1 "I... Um... About you..."
    "NOTE! This choice will impact the further relationship with Carl."
    scene 32-2 carl 14 with Dissolve(1)
    menu:
        "Anna remembers her previous 'naughty' involvement with Carl.":
            $ CarlSexContent = True
            $ relationship_func("Carl Relationship +2, Anna Corruption +2")
            $ AnnaCorruption += 2
            $ CarlRelationship += 2
            a "Oh... Carl... I don't know if this is a good idea."
            c1 "Oh, don't worry much... You know that Rebecca is a heavy sleeper."
            a "Well... Yeah, but still..."
            c1 "Just a little taste. She wouldn't mind."
            a "I guess your right..."
            jump CarlEventOneSex
        "Anna objects to Carl's approach.":
            $ CarlSexContent = False
            a "What? I don't think this is appropriate, Carl."
            a "Your my sister's boyfriend, it would be so wrong..."
            c1 "I... I'm sorry, You just kind of remind me of her a bit."
            a "It's okay... Just leave now..."
            jump RebeccaBed
label CarlEventOneSex:
    $ renpy.music.play("audio/sounds/Purple Planet Music Chill Factor 80bpm.mp3", channel = 'music', if_changed = True)
    scene 32-2 carl 15 with Dissolve(1)
    "Carl touched Anna's soft bosom. It was clean and shiny from the wash."
    "He felt an immediate rush of excitement..."
    "... And so did Anna..."
    a "Oh, Carl... I don't..."
    c1 "You have such a nice ass, Anna."
    c1 "So thick and juicy..."
    a "I... Ah... Th... Thanks..."
    a "I still think that we... shouldn't..."
    scene 32-2 carl 16 with Dissolve(1)
    c1 "Come here, don't think of anything..."
    c1 "You've been through a lot, you deserve to let go for a bit."
    c1 "Rebecca wouldn't mind, you know."
    a "I don't know, Carl... Wouldn't she?"
    c1 "No... She would want you to be at ease and relaxed."
    c1 "Whatever it takes..."
    scene 32-2 carl 17 with Dissolve(1)
    "As Carl's soothing voice made Anna believe him and she even forgot about the towel..."
    "As it dropped to the floor, Carl made sure to touch Anna softly to bring her to an elevated state."
    "She was excited but couldn't control her feelings..."
    c1 "You've got such a beautiful body, Anna."
    c1 "I still remember you laying naked on my desk, in front of me..."
    a "Oh, Carl... It was such spontaneous thing..."
    a "I hope Rebecca doesn't know about our little secret..."
    scene 32-2 carl 18 with Dissolve(1)
    "Anna noticed Rebecca sleeping there, her eyes closed but her face was towards them."
    "The rush of being caught overtook Anna, it felt so wrong, but so right..."
    a "Oh... We have to be careful... Even if she's within deep sleep's grasp..."
    c1 "Sure, let me do all of the work..."
    c1 "You deserve a little release, Anna."
    play sound jerk
    scene 32-2 carl 19 with Dissolve(1)
    "Carl's hand reached down to Anna's sensitive area and she felt immediate pulses of light tingles in her head."
    a "Oh..."
    c1 "You like that? When I touch your vagina lightly?"
    a "I... I don't know..."
    a "{i}...I don't want to say... It feels good..."
    "Anna had trouble admitting that she enjoyed it."
    "But the fact that it felt wrong, doing it with her sister's boyfriend, made her enjoy it that much more..."
    scene 32-2 carl 20 with Dissolve(1)
    a "Oh... This... I can't..."
    c1 "What's that?"
    a "I... Carl... It..."
    c1 "Don't worry, you don't have to say anything..."
    c1 "Your face reveals all I need to know."
    c1 "I'm doing everything correctly, and you are enjoying it..."
    scene 32-2 carl 21 with Dissolve(1)
    "Carl quickly leaned in and started to kiss Anna's neck..."
    "Anna started to feel more and more sensation."
    a "{i}...Oh... Dammmnn..."
    a "Carl..."
    "Anna was exerting increasing amounts of lubricant."
    "She was getting very moist down there..."
    "Carl's kisses and fingers were doing magic on her."
    scene 32-2 carl 22 with Dissolve(1)
    c1 "I want to have a little taste... I think it will be godly."
    a "I... I don't know..."
    a "What are you doing... I don't want Rebecca to catch us..."
    "Even though she loved her sister dearly, she couldn't deny herself such pleasure..."
    c1 "Don't worry too much, I got this... She wouldn't mind that you get pleasure."
    play sound jerk2
    scene 32-2 carl 23 with Dissolve(1)
    "Carl started to give her some of his amazing mouth skills."
    "Anna leaned against the cold bathroom glass and that made her get goosebumps all over her body."
    "Add to that the sensation she was getting from Carl's mouth... She had blissfully forgotten her worries."
    with vpunch
    a "Oh... Ah..."
    a "{i}...I have to keep it down..."
    a "It feels sooo good..."
    scene 32-2 carl 24 with Dissolve(1)
    "Anna was starting to let her inhibitions go and being shy of these feelings."
    "Carl's expertise was more than enough for Anna."
    a "Ahh... Mff..."
    c1 "You like it, don't you? I can hear it. You are so loud..."
    a "I... I'm sorry... Ah..."
    scene 32-2 carl 25 with Dissolve(1)
    "Carl was penetrating her pussy opening with his tongue."
    "Giving her a proper tongue attacks, whilst maintaining his attention on her clitoris and other important parts."
    "Anna's emotions were mingled between excitement and feeling so wrong."
    "All of that made it feel that much better. It made her feel strong sensations all over her body..."
    a "I... Carl... Ahh..."
    scene 32-2 carl 26 with Dissolve(1)
    "For all intents and purposes Rebecca was supposed to be sleeping hard, but as a twist of fate tonight she was having difficulty sleeping."
    "And she stood witness to exciting and hot action that was happening in the bathroom."
    "Was she angry, sad or, perhaps, even enjoying it..."
    r1 "{i}...I... Anna seems to be really enjoying herself..."
    r1 "{i}...I haven't ever seen her enjoying herself this much..."
    scene 32-2 carl 27 with Dissolve(1)
    "Anna was truly taken by the moment, everything seemed fine again..."
    "And Carl was probably enjoying the opportunity as much as Anna."
    a "{i}...I have to keep it down, I don't want to wake up Rebecca..."
    a "Ah... Fffu..."
    "As Anna was trying to keep her composure, Carl seemed to work harder to give her pleasure."
    "Leaving her wanting more but trying not to moan loudly at the same time."
    scene 32-2 carl 28 with Dissolve(1)
    "Meanwhile, it turned out that Rebecca was having fun watching this unfold."
    "She was oddly aroused from what she saw."
    "Enjoying herself lightly while Anna and Carl were in the bathroom."
    "Feeling a weird excitement rush through her body..."
    "While touching herself, she could hear Anna moan in the distance."
    a "Ah... Carl..."
    a "It feels good..."
    scene 32-2 carl 29 with Dissolve(1)
    "Rebecca was enjoying it. Even if it felt weird for her..."
    "She had suspicions about Anna's previous involvement with Carl..."
    "But it wasn't like Rebecca herself was clean, she had done some dirty things in the past, too..."
    r1 "Ah... Anna, you naughty slut... hehe..."
    scene 32-2 carl 30-1 with Dissolve(1)
    "While Rebecca was enjoying the view and Anna was enjoying the pleasure, Carl was digging in deeper."
    "Shoving his entire face between Anna's legs, trying to go deeper with his tongue..."
    "Anna's pussy tasted so good, Carl was spaced out on her, like a drug..."
    c1 "You like that? You like when your sister's boyfriend is eating you out?"
    a "Ah... Don't say... Don't say that..."
    c1 "Do you like it?"
    a "Yeah... I like it a lot... Ah..."
    scene 32-2 carl 31 with Dissolve(1)
    c1 "I can stop right now if you wish..."
    a "N... No... I mean, continue... Please..."
    c1 "Are you sure, I can stop if you feel like it's wrong..."
    a "I... don't say that I just want you to continue..."
    c1 "You asked for it..."
    a "I'm getting close, please continue..."
    scene 32-2 carl 33 with Dissolve(1)
    "Anna gripped Carl by his head and was pushing on him harder, starting to ride his face..."
    "Like her personal toy, it was out of pure instinct to gain more pleasure..."
    "Carl was almost starting to gasp for air, but he did his best to give Anna what she wanted..."
    a "Ah..."
    "Anna started to exhale harder and moaned louder..."
    scene 32-2 carl 32 with Dissolve(1)
    "Doing a very interesting motion with his mouth, It was enough to make Anna go crazy."
    a "Ah... I'm barely holding my moans... I don't want to wake up my sis..."
    a "Ah... Wha..."
    a "Fuuck..."
    "It didn't take long until Anna couldn't hold anymore..."
    "She started to ride Carl's face hard and moving involuntarily."
    with flash
    a "Ah... My pussyy... Ahh..."
    with flash
    "Mff..."
    "Fuuuck... So good..."
    with flash
    "Carl felt how Anna's juices were coming out..."
    scene 32-2 carl 34 with Dissolve(1)
    "She came down from the climax breathing heavily."
    a "Ah... I can't believe it... It felt so good..."
    c1 "Anna... I'm so glad I was able to help you..."
    a "I still can't believe it, but I can't deny it either..."
    c1 "Just admit that you liked it."
    scene 32-2 carl 35 with Dissolve(1)
    a "I like it, but we should keep it a bit lowkey..."
    c1 "Whatever you say, Anna."
    a "This was pretty amazing, I can just imagine what it would be in a different setting."
    c1 "Not as good as this? I mean, this is more exciting, isn't it?"
    a "But... But she's my sister..."
    c1 "Fair point."
    a "If we are to do this, I think we need to take it slower..."
    c1 "We've already done it, what do you mean?"
    a "That was different, I was overtaken..."
    scene 32-2 carl 36 with Dissolve(1)
    "They cleaned up and Anna went to the bed."
    c1 "I will let you sleep with Rebecca then and hit the couch myself, That will make you feel more at ease."
    a "Thank you, Carl, I really appreciated everything..."
    c1 "Don't mention it, It's what family's for..."
    c1 "Anyway, if you need anything, you can come and ask me. I will probably still be up for some time."
    c1 "I want to finish that book. Some very good insights."
    a "Alright, thanks."
    $ renpy.end_replay()
    $ persistent.eightScene = True
label RebeccaBed:
    scene 32-2 carl 37 with Dissolve(1)
    if CarlSexContent == True:
        "After the entire ordeal Anna got into the bed and her mind was flooded with different thoughts."
    else:
        "After she dried up and Carl had left, she got into bed with Rebecca and her mind flooded with different thoughts."
    "The day had been a very colorful one. With its fair share of amazing things but also full of stress."
    "The detective won't take lightly to her choice, he has put Carl in danger..."
    "But she also feels more powerful than ever. Able to resist breaking and also feeling a certain draw to the being badder."
    "Anna, the criminal underground boss..."
    a "{i}...That would be something, me as the bad mob-boss Anna. hehe... That would be something..."
    scene 32-2 carl 38 with Dissolve(1)
    if CarlSexContent == True:
        "While Anna was thinking about her day, Rebecca was still processing what she just saw."
        "And how she felt about it all..."
        r1 "{i}...Oh, Anna... You naughty girl, hehe..."
        r1 "{i}...Just when I thought I knew all about you, you surprise me..."
        "Rebecca seemed to accept it and enjoy it, as a matter of fact."
    else:
        "While Anna was thinking about her day, Rebecca had woken up lightly."
        "She wasn't sure what had happened, but she immediately felt that Anna was with her."
        a "I'd better get some sleep..."

    scene 32-2 carl 39 with Dissolve(1)
    "Rebecca suddenly turned towards Anna and hugged her."
    "And in a silent voice whispered to her..."
    r1 "Hey, Anna... I'm surprised you are here... I hope everything's fine."
    if CarlSexContent == True:
        "Anna was shocked immediately and started to wonder if Rebecca had seen everything."
        "But she was too tired to worry about it..."
    a "Hey... Shh... Sleep tight sis, let's talk in the morning."
    $ GlossaryUnlockCarl = True
    $ GlossaryUnlockTaxman = True
    scene black with Dissolve(4)
    "In the morning..."
    play sound surprise
    scene 33-1 rebecca 1 with Dissolve(1)
    $ renpy.music.play("audio/sounds/Purple Planet Music Rendezvous.mp3", channel = 'music', if_changed = True)
    r1 "Hey, sweety. It's time to wake up. How was your sleep?"
    a "Oh, Hey Rebecca... I, I slept well, no dreams again... Just fell asleep."
    r1 "Ah, you must've been tired, huh?"
    a "I was... a lot happened yesterday..."
    r1 "Carl gave me a little rundown of everything... I think you did the right thing."
    scene 33-1 rebecca 2 with Dissolve(1)
    a "What do you mean?"
    r1 "Well, the police precinct and everything..."
    r1 "I got scared but he assured me that everything was ok."
    r1 "Still, I'm worried about you. Did anyone do anything to you there?"
    a "N... No, the detective was being an asshole again, but that's nothing new."
    r1 "We should report him for sexual harassment!"
    a "Yeah, I don't think that would work... Plus I think we should keep a low-profile."
    play sound undress
    scene 33-1 rebecca 3 with Dissolve(1)
    r1 "I guess, but still, now they know of Carl, too..."
    a "Yeah, that was the biggest risk. I'm sorry that I had to call him..."
    r1 "Oh, don't worry I understand and so does Carl. He always has our back, though."
    r1 "I really appreciate that in him."
    a "Yeah, he saved me back there. I didn't know he was so fluent in law."
    r1 "It's a long story, but he has to know a lot to be able to go around it, you know?"
    a "I understand."
    r1 "Anyway, get dressed I will make us some coffee."
    scene black with Dissolve(1)
    play sound undress
    scene 33-1 rebecca 4 with Dissolve(1)
    "Anna dressed up and went down to the kitchen, and Rebecca had finished making them coffee."
    a "Thank you, Rebecca."
    r1 "Anytime, sis. So... How was yesterday evening? Did Carl accommodate you well?"
    a "I, I... Yeah. He helped me with everything. Thanks."
    if CarlSexContent == True:
        r1 "Anything and everything?"
        a "Umm... Yeah..."
    r1 "He is always so helpful, you know for the simple 'necessities' that we all crave for. hehe."
    scene 33-1 rebecca 5 with Dissolve(1)
    if CarlSexContent == True:
        r1 "So how did you enjoy our place? Was there anything to be excited about?"
        a "I... Like your place, Rebecca. I've always liked it."
    else:
        a "You know I've always liked your place."
    r1 "Hehe... I wonder why... Well, you're always welcome here, feel like home."
    if CarlSexContent == True:
        r1 "And, use anything and everyone for whatever you wish..."
        a "Everyone?"
        r1 "Oh... Don't mind me... Hehe..."
    else:
        r1 "And use anything you need."
        a "Ok, I will, thanks, sweety."
    scene 33-1 rebecca 6 with Dissolve(1)
    if CarlSexContent == True:
        "Anna couldn't understand what Rebecca meant by these comments but she was a bit uneasy..."
        "Did Rebecca know?"
    a "Thanks, the coffee tastes really good."
    if CarlSexContent == True:
        r1 "Yeah, Carl usually also likes the {b}taste{/b} Of some things, if you know what I mean?"
        a "I... I don't know..."
        r1 "Well, nevermind, Anna. I'm just playing around."
    else:
        r1 "Yeah, Carl taught me this recipe, there is a little secret that I won't tell you, hehe."
    r1 "Anyway, I'm going to be heading out soon. Have some errands to run. Will you manage?"
    a "Ah, Yeah. Sure. I will also head out. I also have important business at the office today."
    scene 33-1 rebecca 7 with Dissolve(1)
    r1 "Come here, sweety. I've missed you, and I've been worried. But you always seem to figure things out on your own."
    r1 "I'm proud of that."
    a "Thanks, Rebecca. You taught me good things when we were younger."
    r1 "Oh, you've always been smart, I can't take all the credit."
    r1 "Anyway, time to get going. I'm going to miss you. Let's meet soon again, ok?"
    a "Ok, Rebecca... It was nice to see you again."
    r1 "Oh, I almost forgot... Remember that we planned to go to the gym together?"
    r1 "I was wondering if you'd like to go with me today after work?"
    a "I don't know if it's the right time with everything what's happening."
    r1 "It's the best time! It might help you take your mind off of things."
    a "I guess you're probably right."
    r1 "Great, that's settled then, I will be waiting for you in the gym after work."
    scene black with Dissolve(1)
    jump preGenericEventOne
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
