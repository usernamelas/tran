label EP13_Begin:
    $ EP13_var_1 = True
    scene black
    stop music
    show text "{size=+20}Press Space{/size}"
    pause

label EP13_JohnMorning:
    play music chill_song_3
    $ EP13_var_2 = True
    play sound interface_sound
    show text "Saturday morning..."
    scene 41-1 john 1 with Dissolve(1)
    a "Ah... Already morning?"
    a "{i}...I wonder what today will bring..."
    play sound doorknock
    scene 41-1 john 2 with Dissolve(1)
    a "Huh..."
    play sound surprise2
    scene 41-1 john 4 with Dissolve(1)
    j4 "Hey..."
    "John rushed in without even asking for permission."
    menu:
        "Turn around!!!":
            a "JOHN!! What are you doing? I'm naked!"
            j4 "Shit... Sorry..."
            a "Come on, I just woke up..."
            scene 41-1 john 7 with Dissolve(1)
            j4 "Umm... It's Andrew... He's awake."
            a "What?"
            j4 "Yeah, yeah... Just get ready and meet me in the living room."
            j4 "It's kind of a big deal."
            a "You don't say."
            pass
        "Say nothing.":
            a "That's straightforward."
            a "Come on, I just woke up..."
            j4 "Sorry... I've got news."
            j4 "Kind of a big deal."
            j4 "It's about Andrew."
            scene 41-1 john 5 with Dissolve(1)
            a "Really?"
            a "What about him??"
            "John's voice was rushed, excited, and happy. And worried..."
            j4 "He's awake."
            scene 41-1 john 6 with Dissolve(1)
            j4 "Well... Just get dressed."
            j4 "I'll tell you all about it."
            a "Sure... Give me a minute."
            play audio door2
            pass
    play sound undress
    scene 41-1 john 8 with Dissolve(1)
    a "Andrew? Awake?"
    scene 41-1 john 9 with Dissolve(1)
    "Anna looked her body up and down... Marveling at herself for a moment."
    "Thinking about Andrew..."
    a "Mhm... I wonder, what I could wear to the hospital..."
    scene black with Dissolve(1)
    play sound undress
    scene 41-1 john 10 with Dissolve(1)
    a "There... This should do nicely, a change of style."
    a "This one's nice. I like it. Heh."
    play sound door2
    scene 41-1 john 11 with Dissolve(1)
    j4 "Hey. You look different."
    a "Yeah, I decided to change. Something new, something different."
    j4 "Sure. I like whatever you wear, won't hear any protest from me."
    a "So, Andrew?"
    scene 41-1 john 12 with Dissolve(1)
    j4 "Yeah, I just got a call from the hospital. He's awoken from the surgery."
    j4 "They said that he is ready to be released."
    a "Really?"
    a "Why didn't you tell me straight away?"
    j4 "Well, I am telling you now!"
    j4 "Anyway, thought, that we could go get him together."
    scene 41-1 john 13 with Dissolve(1)
    a "Sure!"
    a "That's good news!"
    j4 "Yeah."
    j4 "I'm glad he's ok."
    a "So what are we waiting for?"
    a "Let's go, eh?"
    scene 41-1 john 14 with Dissolve(1)
    j4 "Yeah... I'm a bit nervous."
    if johnBeenNaked == True:
        j4 "What if he knows about us..."
        a "Come on. No need to think about that."
        a "He was in a coma..."
        a "He won't."
        j4 "Sure, you're right."
        j4 "Still, I feel bad about it..."
    else:
        j4 "Haven't seen the kid for a while."
        a "Of course, he's your son, after all."
    a "So..."
    scene 41-1 john 15 with Dissolve(1)
    a "Don't worry."
    a "Let's go get him."
    j4 "Yeah. Lemme just bring the car around..."
    play sound door2
    scene black with Dissolve(1)
    $ EP13_Black_Outfit = True
    pause
    play sound car_sound1
    jump EP13_Andrew
label EP13_Andrew:
    $ EP13_var_3 = True
    scene 41-2 andrew 1 with Dissolve(1)
    j4 "Hey... Um... We are here for Andrew?"
    nursereception "Certainly, you are the father, correct?"
    j4 "Yes. How, how is he?"
    nursereception "Andrew is doing well, he is awake, and also ready to be released from the hospital."
    scene 41-2 andrew 2 with Dissolve(1)
    j4 "Hah... That's great news."
    nursereception "Congratulations."
    j4 "Thank you... That's good!"
    a "Yeah, haha!"
    scene 41-2 andrew 3 with Dissolve(1)
    nursereception "He is ready to see you now."
    j4 "Yeah, alright."
    a "Shall we?"
    j4 "Yeah...."
    if johnBeenNaked == True:
        "They felt conflicted."
        "Happy... But uneasy, what if he knows something..."
        "About them..."
    play sound door2
    scene 41-2 andrew 4 with Dissolve(1)
    a1 "Guys..."
    a1 "Damn... This feels weird..."
    a1 "Anna... as beautiful, as ever."
    scene 41-2 andrew 5 with Dissolve(1)
    a "Hey... Don't get up... You are still recovering."
    a1 "Heh... I know..."
    a1 "Damn, it's good to see you."
    a "You, too, Andrew... you, too."
    scene 41-2 andrew 6 with Dissolve(1)
    a "How are you feeling?"
    a1 "Hella confused. It seems like I saw you just yesterday."
    a1 "Like it was all a dream."
    a "Well... You were in a coma."
    a1 "Don't tell me it's been six years."
    a "Haha... No."
    scene 41-2 andrew 7 with Dissolve(1)
    a1 "You are so beautiful, even more than I remember."
    a1 "How do you always do it?"
    a "Heh... Just the way I am..."
    a1 "Magnificent."
    scene 41-2 andrew 8 with Dissolve(1)
    j4 "Hey, buddy."
    j4 "You good?"
    a1 "Yeah, body hurts like hell, but... I'm fine. Memories are somewhat foggy."
    a1 "Did... Did I get shot?"
    if GoodBadDoctorChoice == 1:
        play sound door2
        scene 41-2 andrew 9 with Dissolve(1)
        d2 "Hello, everybody."
        d2 "How is my patient doing?"
        a1 "Alive and well doc!"
        d2 "That's good to hear."
        scene 41-2 andrew 10 with Dissolve(1)
        d2 "The hospital has provided a wheelchair for our patient."
        a1 "Great..."
        d2 "How are you guys holding up?"
        scene 41-2 andrew 11 with Dissolve(1)
        a "This a great day... Andrew is finally getting better."
        d2 "Indeed he is."
        d2 "His vitals look green across the board."
        play sound buttonsound
        scene 41-2 andrew 12 with Dissolve(1)
        d2 "Lemme just..."
        "The doctor turned off the system."
        d2 "There we go."
        d2 "You are almost out of this, heh."
        scene 41-2 andrew 13 with Dissolve(1)
        a1 "Finally. I wanna get up and walk around!"
        d2 "Not so fast."
        d2 "You are on bed duty for the next couple of days still..."
        scene 41-2 andrew 14 with Dissolve(1)
        a1 "But... Doc?"
        d2 "No, no, you'll have to rest for a little while still."
        a1 "Ok..."
        scene 41-2 andrew 15 with Dissolve(1)
        d2 "Andrew is still healing, almost healed, but he has to limit movement for the next couple of days."
        a "Ok, shouldn't be a problem. I know how to keep him in bed."
        play sound surprise
        d2 "Oh?"
        a1 "Wha??"
        "It took a moment for Anna to understand."
        scene 41-2 andrew 16 with Dissolve(1)
        a "I... I mean, Hah... I will make sure he rests."
        d2 "Good."
        d2 "In that case, we're ready."
        scene 41-2 andrew 17 with Dissolve(1)
        a "Come, let's get you out of there."
        a1 "Gladly."
        a1 "It feels odd. I feel like I just got here, but also that I've been here for a good while."
        a1 "Can't wait to get out."
        d2 "Indeed."
        play sound undress
        scene 41-2 andrew 18 with Dissolve(1)
        j4 "Come here... Lemme help you out, big boy."
        a1 "Yeah... Ah."
        play sound cloth_sound1
        scene 41-2 andrew 19 with Dissolve(1)
        a1 "Thanks, dad."
        j4 "No problem, buddy."
        a "Alright."
        scene 41-2 andrew 20 with Dissolve(1)
        j4 "Thank you for everything, doc."
        d2 "Don't mention it. It's my pleasure."
        a1 "Thanks, Cary."
        scene 41-2 andrew 21 with Dissolve(1)
        a "So. That's it?"
        d2 "Pretty much. Like I said, he will still have to rest in bed for a couple of days."
        d2 "And he also needs to take some medicine to numb the pain. Do note that it will make him somewhat high."
        d2 "I've written a prescription and also he will have to come in for an MRI in a couple of days."
        a "Ok."
        if CaryGoOut == True:
            j4 "We'll go to the reception and sign the papers, we'll wait for you there."
            play sound door2
            scene 41-2 andrew 22 with Dissolve(1)
            d2 "Anyway... I wanted to talk to you."
            scene 41-2 andrew 23 with Dissolve(1)
            d2 "I've been wondering if you'd like to... still maybe meet up sometime."
            a "Oh?"
            d2 "I've been thinking about you a lot."
            a "I..."
            d2 "Perhaps you'd be down for some fun later on."
            d2 "candle lit dinner perhaps?"
            a "Hehe... I'll... think about it."
            scene 41-2 andrew 24 with Dissolve(1)
            d2 "That's all I ask."
            d2 "I know you want to..."
            d2 "And you know that I want to..."
            play sound door2
            scene 41-2 andrew 25 with Dissolve(1)
            j4 "Oh... Umm..."
            j4 "I think someone forgot their phone here."
            d2 "Yeah, Andrew was on it for sometime after waking up."
            scene 41-2 andrew 26 with Dissolve(1)
            "John saw both women embracing each other..."
            "That made him excited in an instant."
            "He started to fantasize."
            j4 "I'll just... Um, get the phone."
            scene 41-2 andrew 27 with Dissolve(1)
            j4 "There it is."
            j4 "Anna you coming?"
            a "Yeah... Let's go."
            scene 41-2 andrew 28 with Dissolve(1)
            d2 "Take care..."
            d2 "And think about what I said."
            a "Hehe... Alright, alright."
        else:
            a "Thank you for everything, Doctor."
            d2 "It was my pleasure."
    else:
        scene 41-2 andrew 9-1 with Dissolve(1)
        d1 "Ah, hello. Looks like I've arrived just in time."
        j4 "Hello. Yeah."
        d1 "Great, great."
        d1 "I believe congratulations are in order?"
        scene 41-2 andrew 10-1 with Dissolve(1)
        j4 "Indeed."
        d1 "How is our patient doing?"
        d1 "Ready to be released?"
        a1 "Absolutely, sir."
        scene 41-2 andrew 11-1 with Dissolve(1)
        a "We are glad that he has made a good recovery."
        d1 "He seems good enough."
        d1 "You are free to take him home."
        play sound undress
        scene 41-2 andrew 18-1 with Dissolve(1)
        j4 "Come on, buddy."
        a1 "Ah... Thanks, still hurts, though."
        a "No need to check him, doctor?"
        d1 "Nono, his... uh... Fine."
        "The doctor didn't seem interested in the patient."
        play sound cloth_sound1
        scene 41-2 andrew 19-1 with Dissolve(1)
        j4 "There."
        a1 "Thanks, dad."
        scene 41-2 andrew 20-1 with Dissolve(1)
        j4 "Alright, we'll get going."
        d1 "Yeah, Anna, wait a moment, we've got something to discuss."
        a "Ok..."
        scene 41-2 andrew 21-1 with Dissolve(1)
        a1 "Thanks, doc. For everything."
        d1 "Yeah, yeah."
        d1 "Good uh, luck..."
        scene 41-2 andrew 22-1 with Dissolve(1)
        d1 "So. He umm, should stay home for a couple of days."
        d1 "I've also written a prescription of pain killers."
        a "Sure, thanks."
        d1 "Also, you'll have to come in with him."
        d1 "For a... Checkup..."
        d1 "For both of you. You do remember we still have some tests to do on you."
        scene 41-2 andrew 23-1 with Dissolve(1)
        a "What?"
        d1 "Indeed. I've made some discoveries regarding your... Condition."
        a "Tell me all about it, doc."
        d1 "Well, all in due time. I will contact you when it is time for you both to come in."
        scene 41-2 andrew 24-1 with Dissolve(1)
        a "I don't know if I want to continue... It wasn't exactly the best thing."
        d1 "On the contrary, you are making strides."
        d1 "We are on the cusp of a new discovery. If you help me, I will help you."
        a "How exactly would you help me?"
        d1 "For one, I could pay you, when I receive the stipend for this research."
        d1 "Or I could cure you."
        d1 "Just think about it. I know you'll come around."
        scene 41-2 andrew 25-1 with Dissolve(1)
        a "{i}...The doctor is relentless...{/i}"
        "Dr. Schmidt kept scheming and scheming."
        "Whatever he could come up with to become more successful."
        "Even if at others expense."
    play sound door2
    scene 41-2 andrew 30 with Dissolve(1)
    a1 "Damn, can't wait to get home."
    a1 "In a comfy bed."
    a1 "And some good food..."
    a1 "I feel hungryyyy."
    scene 41-2 andrew 31 with Dissolve(1)
    j4 "We'll serve you up the best food you've eaten in weeks."
    a1 "Haha... Most definitely, All I know is, I was fed stuff through a tube..."
    a1 "That's yucky."
    play sound door2
    play ambience city_traffic
    scene 41-2 andrew 32 with Dissolve(1)
    a "Ok, I'll get in the back."
    a1 "Thanks."
    play sound car_sound1
    scene 41-2 andrew 33 with Dissolve(1)
    j4 "So, how are you feeling in general, bud?"
    a1 "Like... Like something ain't right."
    j4 "Oh?"
    j4 "Care to elaborate?"
    a1 "I... Still need to get my thoughts in order..."
    j4 "Ok..."
    scene 41-2 andrew 34 with Dissolve(1)
    a1 "Other than that, it's good to finally be out."
    a1 "I think I'll also put the previous life behind me, getting shot really is an eye opener."
    a1 "And what you guys have been up to?"
    a "Oh, I will tell you all about it later."
    a1 "Ok, can't wait."
    play sound car_sound1
    stop ambience
    scene black with Dissolve(1)
    pause 1
    play sound door2
    play music chill_song_3
    scene 41-2 andrew 35 with Dissolve(1)
    a1 "Damn, hurts like a bitch."
    a "Don't worry, Doc gave me a prescription for the pain."
    a1 "Good..."
    a "I think it's a strong one. Might make you a bit high."
    j4 "Haha... Enjoy!"
    scene 41-2 andrew 36 with Dissolve(1)
    a1 "Thanks, guys."
    a1 "Damn, things seem woozy."
    a1 "I feel like I'm remembering things."
    a "What exactly?"
    play sound undress
    scene 41-2 andrew 37 with Dissolve(1)
    a1 "I don't know... Like, things. From the shooting..."
    a1 "And also, even though I was asleep, feels like I heard people..."
    a1 "I know you were there, definitely know I felt your presence there, guys."
    a1 "Also, I think someone was having... Umm... Sex somewhere, maybe in the other room or something... Weird."
    if johnBeenNaked == True:
        play sound surprise
        scene 41-2 andrew 38 with Dissolve(1)
        pause 1
        scene 41-2 andrew 39 with Dissolve(1)
        a "Umm..."
        "They both felt a cold hand go down their backs."
        "Did Andrew know?"
    scene 41-2 andrew 40 with Dissolve(1)
    a "Don't think about it too much now, You need rest."
    a1 "Yeah, I suppose so."
    a "We'll take care of you, you don't have to worry."
    scene 41-2 andrew 41 with Dissolve(1)
    a "Is there anything you want?"
    a1 "Not really, just to relax. Some food maybe, but John said he'll take care of that."
    a "OK, I will help you get undressed and then I'll get the medicine."
    a1 "Thanks, babe."
    play sound undress
    scene 41-2 andrew 42 with Dissolve(1)
    pause 1
    play sound jacketcloth
    scene 41-2 andrew 43 with Dissolve(1)
    if AnnaCorruption >= 40:
        "Anna looked at his penis and realized how unfulfilling it used to be."
        "How she'd want a proper cock to penetrate her."
    a "Well... Looks like you ain't that excited to see me."
    a1 "I am... Trust me, but the pain keeps my mind elsewhere."
    a "Ah, I see."
    scene 41-2 andrew 44 with Dissolve(1)
    "She looked at it..."
    a "{i}...It's been quite some time since we've done something...{/i}"
    a "{i}...Perhaps he'd want to...{/i}"
    scene 41-2 andrew 45 with Dissolve(1)
    "While Anna was pondering about things... She noticed that Andrew had fallen asleep."
    a "Oh, there he goes."
    play sound undress
    scene 41-2 andrew 46 with Dissolve(1)
    "She tucked him in."
    a "Alright, the medicine, Should take care of that."
    if AnnaCorruption <= 10:
        "Anna felt excitement in her body, Andrew was back, and she was happy to see him."
        "A lot has happened since his accident, she wants to tell him all about it."
    elif AnnaCorruption > 11 and AnnaCorruption< 30:
        "Anna felt pity towards Andrew."
        "The things she'd done, was there any penance for her?"
    elif AnnaCorruption >= 31:
        "Anna felt almost indifferent about Andrew."
        "She questioned every moment, why she was still with him."
        "Perhaps she still cared about him in some weird, twisted way."
    play sound door2
    scene 41-2 andrew 47 with Dissolve(1)
    j4 "How is he?"
    a "Fell asleep."
    if johnBeenNaked == True:
        j4 "We should talk about the elephant in the room."
        a "you think he knows something?"
        j4 "I do. Or... Maybe he's not entirely sure and is questioning himself still."
        scene 41-2 andrew 48 with Dissolve(1)
        a "Perhaps... We can always deny it."
        j4 "I suppose so."
        j4 "Damn, this is utterly fucked. he's my son."
        a "..."
    a "I'll go grab the medicine. Then I'll be back."
    j4 "Sure, meanwhile, I will find something for him to eat. Maybe I'll order something nice."
    a "Yeah, do that."
label EP13_Shop:
    $ EP13_var_4 = True
    scene 41-4 shop 2 with Dissolve(1)
    a "Hello, I've got a prescription for painkillers?"
    sk "Hi, certainly."
    sk "Let's see."
    if BenjaminContent == True:
        a "Also, I was wondering about... Uhm, Benjamin?"
        sk "Oh?"
        a "Did he get the job here?"
        scene 41-4 shop 3 with Dissolve(1)
        sk "Heh, indeed he did."
        sk "He will start in a couple of days as a janitor."
        scene 41-4 shop 4 with Dissolve(1)
        a "That's wonderful!"
        a "I'm glad he's moving up in the world."
        a "Not on the streets anymore."
        sk "Yeah, it's nice to help out someone like that."
        sk "When we talked, he was also pretty interesting."
        scene 41-4 shop 5 with Dissolve(1)
        sk "Here is the medicine."
        a "Thank you."
        sk "You're always welcome."
        play sound undress
        scene 41-4 shop 6 with Dissolve(1)
        pause 1
        scene 41-4 shop 7 with Dissolve(1)
        a "Thank you also for giving Benjamin the chance."
        sk "No problem. He came in and cleaned up the place for free a couple of times, just to prove himself."
        a "Really?"
        sk "Yeah, that was a nice gesture."
        a "Great, Take care."
        sk "Bye."
    else:
        scene 41-4 shop 5 with Dissolve(1)
        sk "Here is the medicine."
        a "Thank you."
        sk "You're always welcome."
        play sound undress
        scene 41-4 shop 6 with Dissolve(1)
        pause 1
        scene 41-4 shop 7 with Dissolve(1)
        a "Thank you, take care."
        sk "Bye."
    scene black with Dissolve(1)
    if BenjaminContent == True:
        jump EP13_Benjamin
    else:
        jump EP13_Andrew_2
label EP13_Benjamin:
    $ EP13_var_5 = True
    play music Funny_Song2
    play ambience city_traffic
    scene 41-3 ben 1-1 with Dissolve(1)
    "As Anna was walking back home..."
    "She heard a commotion."
    scene 41-3 ben 2-1 with Dissolve(1)
    b1 "Shiiiet."
    b1 "{i}...It's Anna!!! She could help me...{/i}"
    play sound surprise
    scene 41-3 ben 3-1 with Dissolve(1)
    b1 "Anna! I need... Ah... I need your help."
    a "Benjamin?"
    b1 "No time to explain right now!"
    scene 41-3 ben 4-1 with Dissolve(1)
    b1 "Just... Take this... I need you to take it..."
    a "Wha?"
    b1 "I will explain everything later!"
    a "Ok, Ok."
    b1 "I have to run... And FAAAST!"
    scene 41-3 ben 5-1 with Dissolve(1)
    a "Hold on, what's going on?"
    b1 "Can't tell you, I gotta run!"
    play sound jacketcloth
    scene 41-3 ben 6-1 with Dissolve(1)
    b1 "Here."
    scene 41-3 ben 7-1 with Dissolve(1)
    b1 "SHiieeet!"
    b1 "Imma bail now... AAAAHHH"
    cp1 "STOP!!!!"
    cp1 "STOP THE THIEF!"
    scene 41-3 ben 8-1 with Dissolve(1)
    b1 "Stall him, pleeeaasseee!"
    scene 41-3 ben 9-1 with Dissolve(1)
    cp1 "Stop right there you criminal scum!!"
    cp1 "You've violated the LAW!"
    a "What, the fuck."
    scene 41-3 ben 10-1 with Dissolve(1)
    cp1 "Excuse me miss... Did he do anything to you?"
    cp1 "Are you alright?"
    a "Uh... I'm fine... Yeah."
    a "Well..."
    "Anna figures she should stall him a bit..."
    cp1 "Ok, I will catch him in that case."
    scene 41-3 ben 11-1 with Dissolve(1)
    a "Well, Actually... He grabbed me..."
    with vpunch
    a "By the BOOBS!"
    cp1 "What?"
    a "Yeah... It's... I feel so dirty now..."
    cp1 "I really have to go... I have to catch him."
    a "But... Sir, He... I feel so not good."
    cp1 "You'll be fine."
    cp1 "I... Ok... I get it, I have to run ma'am."
    scene 41-3 ben 12-1 with Dissolve(1)
    cp1 "STOOOOP!!!!"
    cp1 "Where the fuck did he..."
    scene 41-3 ben 13-1 with Dissolve(1)
    a "What the hell was that?"
    a "I thought Benjamin was getting his act together."
    a "But this... He has some explaining to do..."
    scene black with Dissolve(1)
    stop ambience
    jump EP13_Andrew_2
label EP13_Andrew_2:
    play music chill_song_4
    $ EP13_var_6 = True
    scene 41-5 home 1 with Dissolve(1)
    a "Well, I'm back."
    j4 "Good, good... I've been here sitting, thinking."
    a "Well, did you order him something to eat?"
    j4 "Oh... No, not yet."
    a "Get on with it then."
    a "I'll bring him the medicine."
    play sound pourwater
    scene 41-5 home 2 with Dissolve(1)
    a "There. I wonder, the doctor said he'll be high from these."
    a "Well, at least he'll be able to enjoy himself a bit heh."
    scene 41-5 home 3 with Dissolve(1)
    a "Has he said or done anything?"
    j4 "No, I think he groaned a bit and said your name once but that's about it."
    j4 "He's been sleeping."
    a "I see."
    a "Ok."
    play sound door2
    scene 41-5 home 4 with Dissolve(1)
    a "Hello, sleepyhead."
    a "I've brought you the medicine."
    a1 "Anna... Anna... Mmmm..."
    play sound drinkingBeverage
    scene 41-5 home 5 with Dissolve(1)
    a1 "Yeah... Ok."
    a "Bottoms up."
    scene 41-5 home 6 with Dissolve(1)
    a "That should make you feel better, ye?"
    a1 "Yeah, thanks... I appreciate it."
    scene 41-5 home 7 with Dissolve(1)
    a "You'll be fine in no time."
    a1 "Well, A couple of days max. I wanna get on with life."
    a "Hehe, understandable."
    a1 "Listen, I've got something very serious to tell you."
    a1 "While I'm still not completely drugged out of it with the medicine."
    a "What is it?"
    "Anna felt anxious..."
    stop music
    a1 "Carl... He's behind it."
    a "What?"
    a1 "He was behind the shooting... HE Was the one who was screwing everyone over."
    play sound surprise2
    play music tense2
    scene 41-5 home 8 with vpunch
    a "WHATTT???!!!!"
    a "I'm Sorry.... WHAT!??!!"
    a1 "It's the truth..."
    a "That's about the dumbest shit I've heard."
    scene 41-5 home 9 with Dissolve(1)
    a1 "Anna, you've got to believe me."
    a1 "He was in with it with Fitzgerald."
    a1 "He was stealing and probably is still stealing from Sergey, from YOU and REBECCA!"
    scene 41-5 home 10 with Dissolve(1)
    a "The fuck you are telling me?"
    a "That our most trusted man, Rebecca's boyfriend... My... Friend."
    a "Has been behind all this mess?"
    a1 "YES!"
    scene 41-5 home 11 with Dissolve(1)
    a1 "I'm... Sorry, I feel, lightheaded."
    a1 "Just... Trust me, this once. I've got proof..."
    a1 "It's... In Sergey's warehouse, in the office..."
    a1 "Behind... the..."
    scene 41-5 home 12 with Dissolve(1)
    "He fell asleep again."
    a "What the fuck..."
    scene 41-5 home 13 with Dissolve(1)
    a "I... I don't believe it..."
    a "But... What if..."
    a "Could've he been?"
    "Anna tried to recall any details she could about Carl, about everything that happened."
    a "The shooting in the basement... It was... He got knocked out..."
    a "Right? By two tied-up men? Right?"
    play sound whoosh_1
    scene 36-9 base 4 with flash
    "Fitzgerald had a cloth around his eyes..."
    "Carl was knocked out..."
    "But... Fitzgerald and Mr. Smith were tied up... Carl is strong, and had a gun..."
    scene 41-5 home 14 with flash
    a "Holy Shit..."
    a "This... It can't be..."
    a "I... Have to check out the warehouse."
    scene black with Dissolve(1)
    jump EP13_Warehouse
label EP13_Warehouse:
    $ EP13_var_7 = True
    play music SecretAgent
    scene 41-7 warehouse 1 with Dissolve(1)
    wg1 "Oh, Hello, Anna."
    a "Hey, Tyler."
    a "How are you... doing?"
    wg1 "Well, as good as we can expect."
    wg1 "With all this shit going on."
    a "Yeah..."
    scene 41-7 warehouse 2 with Dissolve(1)
    a "Listen, I've got to take a look at some stuff in the warehouse. Do you mind?"
    if EarlHelp == True:
        wg1 "No problem, since Sergey's locked up, I'm trying to keep a low profile, I'd assume you know more about it all."
        wg1 "I haven't gotten any news from him either."
    else:
        wg1 "No problem at all, I've been informed by Sergey to let you carry out stuff here."
        wg1 "I'm just trying to keep a low profile, is all."
    a "Alright, thanks."
    scene 41-7 warehouse 3 with Dissolve(1)
    wg1 "How are you doing?"
    a "Well, same as you, as good as can be expected."
    a "I've got a plethora of other things to worry about."
    wg1 "Understandable. Hey, keep your head up though, we gon get through this."
    scene 41-7 warehouse 4 with Dissolve(1)
    a "No other choice."
    wg1 "True."
    wg1 "Well, don't let me keep you."
    play sound door2
    scene 41-7 warehouse 5 with Dissolve(1)
    a "So, lemme see."
    a "{i}...Seeing Tyler gave me quite a scare...{/i}"
    a "{i}...I still don't believe Andrew...{/i}"
    scene 41-7 warehouse 6 with Dissolve(1)
    a "He said behind the... But didn't finish before falling asleep."
    a "I wonder where could it be."
    scene 41-7 warehouse 7 with Dissolve(1)
    a "Well, it's Andrew, the place where he hid it, won't be very elaborate, that's for sure."
    a "Maybe behind this shelf..."
    "Anna felt a sense of uncertainty looming over her."
    "Were things about to turn upside down for all of them?"
    play sound give_box
    scene 41-7 warehouse 8 with Dissolve(1)
    a "Not here..."
    a "Hmm..."
    "Anna continued her search, as she was committed to finding the item."
    "A part of her believed or wanted to believe Andrew..."
    "A part of her felt like this was a betrayal by him, snooping around, trying to rattle the hornet's nest."
    play sound jacketcloth
    scene 41-7 warehouse 9 with Dissolve(1)
    "But what if it was true?"
    "What if Carl was the architect of this foul plan?"
    "What if Anna, Rebecca, and everyone else was an insignificant pawn in Carl's plot."
    "One way to find out."
    play sound undress
    scene 41-7 warehouse 10 with Dissolve(1)
    a "Maybe here."
    "As she continued her search, she tried to recall more things."
    "Connect the dots... Things were becoming clearer."
    a "Was it all a part of Carl's plot? Letting Fitzgerald KIDNAP Rebecca???"
    scene 41-7 warehouse 11 with Dissolve(1)
    a "Ah... There is something there."
    a "I still don't believe Andrew."
    play sound cloth_sound1
    scene 41-7 warehouse 12 with Dissolve(1)
    pause 1
    scene 41-7 warehouse 13 with Dissolve(1)
    a "A notebook."
    "As she was about to open it, she felt a wave of anxiety wash over her."
    play sound pageflip
    scene 41-7 warehouse 14 with Dissolve(1)
    a "..."
    a "No... No... No..."
    a "It can't be."
    "The notebook was filled with lists, dates, numbers, plan points."
    "Lists of things to do, and that have been done."
    "Dates of arrivals, Fitzgerald, Mr. Smith, dates when Sergey was unavailable."
    "Multiple entries of the weighted amounts of drugs that Carl has stolen."
    "Multiple entries of cash that Carl had written off the books."
    "Some notes on his plan..."
    $ hidden_note = False
    menu Note_Menu:
        "Note Entry #1":
            c1 "I knew Rebecca had a sister..."
            c1 "I didn't know she was THAT hot..."
            c1 "No matter, I can't let her get in the way of my plan..."
            jump Note_Menu
        "Note Entry #2":
            c1 "I've finally got in contact with a rival of Sergey..."
            c1 "He will surely be able to help me orchestrate all of this."
            c1 "He knows very little of my actual intentions... All he cares about is money and power..."
            jump Note_Menu
        "Note Entry #3":
            c1 "That damn boy, Andrew, he is messing with this entire thing..."
            c1 "Perhaps he can help me 'kidnap' Rebecca and I can convince him that it will help Anna and him."
            c1 "I should probably make Fitzgerald do that."
            c1 "Andrew will jump at the chance to make sure he can support Anna..."
            jump Note_Menu
        "Note Entry #4":
            c1 "It was all fucked up... Fitz and his bodyguard didn't take out Sergey..."
            c1 "And now we've got a dead body on our hands..."
            c1 "Andrew is out of the picture, at least…"
            c1 "He could've told on me..."
            c1 "I will have to come up with another plan."
            jump Note_Menu
        "Note Entry #5":
            c1 "Luckily for me, Fitz has popped up again and now he's with his brother."
            c1 "Now I can help them make a move against Sergey, once more."
            c1 "Gotta tie up the other loose ends and then... I can disappear..."
            $ hidden_note = True
            jump Note_Menu
        "Note Entry #6" if hidden_note == True:
            c1 "I have to disappear... Otherwise, the big boss will have my head..."
            c1 "Sergey doesn't even know how much I’ve stolen from everyone..."
            jump Note_Menu
        "That's all.":
            pass
    a "So that's how he planned it... So he wanted to take out Sergey AND Fitzgerald and his brother..."
    a "And in the end, I fucked up his plan by saving Sergey... And... Killing Mr. Smith..."
    "The notes mentioned where he was stashing money and some other items."
    scene 41-7 warehouse 15-1 with Dissolve(1)
    a "And a key?"
    a "It probably unlocks the stash..."
    scene 41-7 warehouse 15 with Dissolve(1)
    a "That... Fucking... Bastard..."
    a "He was fucking over everyone."
    "Anna was in shock, but she was also very angry."
    scene 41-7 warehouse 16 with Dissolve(1)
    a "I have to go to Rebecca for this. This might just be some fake notebook."
    a "The final piece of the puzzle will be at her place, Carl's place..."
    a "She might not like what I will have to say, but she's my sister. She deserves to know the truth."
    play sound door2
    scene 41-7 warehouse 17 with Dissolve(1)
    wg1 "All good in there?"
    a "Yeah, I just checked some stuff. Might help us, Sergey, you, me. Everyone."
    wg1 "That's great, thanks. Take care for now."
    a "You, too."
    scene black with Dissolve(1)
    jump EP13_Rebecca
label EP13_Rebecca:
    play music tranquility
    $ EP13_var_8 = True
    scene 41-8 rebecca 1 with Dissolve(1)
    r1 "Anna. What a lovely surprise!"
    a "Good to see you, sis."
    a "How are you doing?"
    scene 41-8 rebecca 2 with Dissolve(1)
    r1 "I'm ok. Michael is keeping the spirits up."
    r1 "We went to this fancy diner the other night."
    a "You think that's the best thing to do right now?"
    r1 "It helps keep our minds off of things, you know?"
    a "Fair point."
    scene 41-8 rebecca 3 with Dissolve(1)
    a "You home alone now."
    r1 "Naah... Michaels here, too."
    scene 41-8 rebecca 4 with Dissolve(1)
    r1 "In the shower right now..."
    r1 "Mm... That bod... Heh..."
    a "How is he?"
    r1 "Recovered, doing well..."
    scene 41-8 rebecca 5 with Dissolve(1)
    a "Good for him."
    r1 "And me of course, heh."
    r1 "What would I do without him."
    r1 "He gave us quite the scare, you know?"
    scene 41-8 rebecca 6 with Dissolve(1)
    a "Listen... No easy way to say this... But..."
    r1 "Huh?"
    a "Umm... It's about Carl..."
    scene 41-8 rebecca 7 with Dissolve(1)
    r1 "What about him?"
    if EarlHelp == True:
        r1 "Any news from the police?"
        a "Not quite..."
    else:
        r1 "Have they been in contact with you from their hideout?"
        a "Not exactly..."
    a "It's... Hard to tell..."
    scene 41-8 rebecca 8 with Dissolve(1)
    a "Ok..."
    a "I think he's been lying to us, he's been screwing us... All of us."
    play music tense2
    r1 "Wha?"
    r1 "Is this some twisted joke?"
    a "NO... I found a notebook in the warehouse... It has notes by Carl about what his plan was..."
    a "I think he might've released Fitzgerald... I think he was actually behind your kidnapping..."
    scene 41-8 rebecca 9 with Dissolve(1)
    r1 "WHAT!?"
    r1 "No! Anna, don't lie to me, not at a time like this!"
    a "I'm... I'm not, I wish I was, truly."
    a "I have proof... Andrew showed me."
    r1 "ANDREW? OF COURSE THAT LITTLE RUNT!"
    a "Stop... He might be right..."
    play sound book_open_1
    scene 41-8 rebecca 10 with Dissolve(1)
    r1 "..."
    r1 "I... I can't believe this..."
    r1 "He... He was going to leave me???"
    a "..."
    r1 "He was going to ditch us? Just like that?"
    scene 41-8 rebecca 11 with Dissolve(1)
    a "It gets worse, he was planning to tie up loose ends as well..."
    a "At the very least, we'd be in prison..."
    a "At worst... Well, you know..."
    scene 41-8 rebecca 12 with Dissolve(1)
    r1 "What kind of a psychopath does this?"
    r1 "The notes say that he keeps a small stash in this house..."
    a "That's why I came... To get more proof..."
    r1 "I... Ok."
    scene 41-8 rebecca 12-1 with Dissolve(1)
    a "He mentioned the cupboard."
    a "There was a key in the notes, too."
    scene 41-8 rebecca 13 with Dissolve(1)
    r1 "This one I think."
    r1 "He said he didn't use this cupboard because he lost the key. Said that nothing important in it anyway, let's just keep it like that."
    r1 "..."
    "Rebecca opened the cupboard."
    scene 41-8 rebecca 14 with Dissolve(1)
    r1 "Fuck..."
    r1 "I mean, he literally kept it all in plain sight..."
    r1 "Fucking liar. There are passports, money, all the shit, like in the movies."
    r1 "What the hell is going on?"
    scene 41-8 rebecca 15 with Dissolve(1)
    r1 "Why... Why would he do this?"
    a "I... I don't know."
    if EarlHelp == True:
        a "Perhaps I could find out more at the precinct. Somehow get some more evidence..."
        a "We might still be in danger..."
    else:
        a "Perhaps I should risk it and go meet with Sergey and Carl..."
    r1 "Yeah..."
    r1 "We've got to figure it out."
    scene 41-8 rebecca 16 with Dissolve(1)
    m2 "Heeyyy, Anna."
    m2 "Good to see you."
    m2 "Figure out what?"
    r1 "Uhm... Um..."
    scene 41-8 rebecca 17 with Dissolve(1)
    r1 "Figure out what we'll wear when we go out in a couple of days."
    "Rebecca, working her quick wits to steer the conversation in a different direction."
    m2 "Oh, some good ole sister time?"
    a "We've been thinking about it, yeah."
    "Anna played along."
    scene 41-8 rebecca 18 with Dissolve(1)
    "They didn't know if Michael should hear about this, just yet."
    m2 "You alright, Becca?"
    m2 "You seem a little rattled."
    r1 "Yeah, fine, I'm just a bit tired, you know?"
    m2 "I get you..."
    scene 41-8 rebecca 19 with Dissolve(1)
    m2 "How you doin', Anna?"
    a "I'm ok, I just came in to say hi, and drop off something for Rebecca."
    m2 "Sure, sure. no probs."
    a "I will be heading out now."
    m2 "Aight."
    scene 41-8 rebecca 20 with Dissolve(1)
    a "Take care, guys."
    m2 "Catch you later!"
    r1 "Bye, Anna..."
    scene black with Dissolve(1)
    jump EP13_Party
label EP13_Benjamin_2:
    play sound door2
    play music PPMSoftShoeShuffle
    $ EP13_var_9 = True
    scene 41-6 ben 1 with Dissolve(1)
    a "What the hell, Ben?"
    b1 "Huh?"
    b1 "Oh... I can explain!"
    b1 "It's not what you think, Anna. Truly."
    scene 41-6 ben 2 with Dissolve(1)
    a "Oh, come on. Cut the crap."
    a "You just can't help yourself, can you?"
    a "You got a job at the store, what happens when she finds out you are a thief?"
    b1 "I... Uh..."
    b1 "I know..."
    scene 41-6 ben 3 with Dissolve(1)
    b1 "I'm sorry."
    a "Sorry won't cut it, we have to return the watch."
    b1 "I... I can't exactly."
    a "Why?"
    b1 "It's... I'm on bad terms with some other hobos."
    a "I don't care, that doesn't excuse you stealing."
    scene 41-6 ben 4 with Dissolve(1)
    b1 "They said, if I don't steal that watch for them, they'll break into my place and mess it up."
    b1 "Then I would be thrown out of the apartment..."
    b1 "I've done so much to keep this place. It's a blessing."
    a "I... I didn't know."
    b1 "I'd do anything to not return to my old spot... It was... wet and stinky... And often some guy left his dog's poop there."
    b1 "Just to mess with me."
    scene 41-6 ben 5 with Dissolve(1)
    b1 "I have to bring it to them, sadly."
    b1 "Can I please have it?"
    a "Uh... No..."
    a "We will go there and fix it. They won't get away with it."
    b1 "But, Anna. What are you going to do?"
    a "I'll figure it out."
    play sound door2
    scene black with Dissolve(1)
    pause
    play ambience citytraffic
    play music PPMEtheralEternity
    scene 41-6 ben 8-1 with Dissolve(1)
    a "Yeah, this ain't no place I'd want to come often to."
    b1 "I know, right?"
    b1 "It only brings bad memories."
    scene 41-6 ben 9 with Dissolve(1)
    b1 "Those are the bastards..."
    a "I see... Ok. Let's just see what we can come up with."
    "Anna was worried, anxious about what they'd potentially do."
    scene 41-6 ben 10 with Dissolve(1)
    a "Ok, I figured it out."
    a "We'll go and talk to them. I will threaten them with my criminal connections."
    b1 "Ooooh? Really?"
    b1 "That's awesome."
    scene 41-6 ben 11 with Dissolve(1)
    a "Are those the same bastards that bothered you that one time?"
    a "When I first saw you?"
    b1 "Uh... Yeah..."
    a "We'll see about that."
    pause 1
    scene 41-6 ben 12 with Dissolve(1)
    a "Excuse me."
    a "Are you the guys that are pestering Benjamin?"
    bum1 "Heh... What is a pretty little thing like you doing in a place like this?"
    bum1 "And how does Benjamin know of you."
    bum2 "Waaiitt... I know you."
    scene 41-6 ben 13 with Dissolve(1)
    bum2 "You're Anna."
    a "How exactly do you know of me?"
    bum2 "I've seen you. In lots of places. The bar..."
    if DilanPornContent == True:
        bum2 "in magazines."
    a "Ok, so?"
    bum2 "Bill, she's the slut I tell you about all the time."
    bum1 "She's a fine dime, indeed."
    scene 41-6 ben 14 with Dissolve(1)
    bum1 "Ben. Do you have the watch?"
    bum1 "You know what'll happen if you don't provide us with it?"
    b1 "Uhh... I... I know."
    play sound undress
    scene 41-6 ben 15 with Dissolve(1)
    pause
    scene 41-6 ben 16 with Dissolve(1)
    pause 2
    if DilanPornContent == True:
        scene 41-6 ben 17 with Dissolve(1)
        bum1 "Oh shit. That is her."
        bum1 "This is magnificent."
        bum1 "The hair's a bit different, but not a problem."
        bum1 "I've been hoping to see you again."
        scene 41-6 ben 18 with Dissolve(1)
        bum2 "I mean, Ben. You've out done yourself!"
    bum2 "We asked for a watch, but you got us a jewel so much better than that."
    bum2 "We won't touch you anymore, hehe... For the time being."
    a "Damn straight you won't, You know Sergey? the criminal?"
    a "I am personally involved with him, if you as much as touch Benjamin or me, you will die."
    scene 41-6 ben 19 with Dissolve(1)
    bum2 "Hehe... Sergey?"
    if EarlHelp == True:
        bum2 "The one that's been jailed by that asshole detective?"
        bum2 "Yeah, sure... He ain't doing much through that jail cell..."
    else:
        bum2 "I heard they killed the detective and are on the run."
        bum2 "They ain't touchin’ us, more heat. That's for sure."
    bum2 "So... All is to say, you ain't getting help from him."
    a "{i}...Shit...{/i}"
    play sound surprise2
    scene 41-6 ben 20 with vpunch
    a "Back off!"
    scene 41-6 ben 21 with Dissolve(1)
    bum2 "Whoa, kitties got claws?"
    bum2 "Daddy likes. hehe..."
    a "You are nobody's daddy, you sad shit."
    scene 41-6 ben 22 with Dissolve(1)
    bum2 "Listen, we in the business like to say, you ain't got no leverage."
    bum2 "You want us to leave Ben alone, you gotta provide us with something valuable."
    scene 41-6 ben 23 with Dissolve(1)
    bum1 "Yeah, it's starting to sink in, eh?"
    bum1 "Was a mistake to come here. Well, we are fortunate, hehe."
    a "{i}...What do I do...{/i}"
    bum1 "Come now, don't be shy."
    scene 41-6 ben 24 with Dissolve(1)
    bum1 "We won't bite."
    bum2 "We just wanna feel a bit of warmth from that soft body of yours."
    a "Uh..."
    scene 41-6 ben 25 with Dissolve(1)
    bum2 "See a bit of skin. Oh yeah!"
    bum1 "So hot... I don't have to wank to your pics anymore, I can just touch you."
    scene 41-6 ben 26 with Dissolve(1)
    "Anna looked at Benjamin, he felt sorry for her..."
    "But he had no choice but to oblige their requests..."
    "She had a chance to make a split decision."
    menu:
        "Think quick and find something to hit them with.":
            play music suspensfulsong
            scene 41-6 ben 98 with Dissolve(1)
            "Anna looked around and noticed a bat."
            a "You won't touch neither me, nor Ben anymore!!!"
            scene 41-6 ben 99 with Dissolve(1)
            "She reached for the bat in a split second."
            bum1 "Wha?"
            bum2 "SHIT!"
            scene 41-6 ben 100 with Dissolve(1)
            a "You stupid pieces of shit!"
            a "I don't need Sergey or any other criminal!"
            a "I can fuck you up just as good you dumb fucks!"
            "Anna went complete amazonian mode, berserk."
            play sound baseball_hit
            scene 41-6 ben 101 with vpunch
            a "TAKE THAT!"
            bum2 "AAAHHHH."
            bum1 "NOOO!"
            scene 41-6 ben 102 with Dissolve(1)
            a "You fuckers. COME ON!"
            bum1 "NO. NO... Sorry, sorry!"
            bum2 "AAAAAH!!"
            scene 41-6 ben 103 with Dissolve(1)
            bum2 "WHY?"
            a "WHY?"
            a "You tried to fucking touch me you disgusting pig."
            a "That's why!"
            scene 41-6 ben 104 with Dissolve(1)
            with vpunch
            a "IF YOU EVER touch me or Ben EVER AGAIN... I... Will... Fucking kill you!"
            a "Did you get that?"
            a "Is that enough leverage for you?"
            "Ben was completely shocked by the anger Anna was exerting."
            "Did it all stem from other events that had happened?"
            bum1 "Ok... We're sorry. We won't touch either of you no more."
            scene 41-6 ben 105 with Dissolve(1)
            b1 "Anna... Wow..."
            a "You ok?"
            a "Yeah, yeah. I'm fine."
            a "Let's go."
            scene 41-6 ben 106 with Dissolve(1)
            "As they left the area, Ben was still shocked by Anna's actions."
            "He was inspired, even."
            b1 "That was brutal. I love it!"
            b1 "I never knew you could do that."
            a "Neither did I... Heh."
            scene 41-6 ben 107 with Dissolve(1)
            a "Well, now that that's settled. How about you take care of that watch?"
            b1 "Oh... Yeah, I will return it to the owner."
            b1 "Now that I don't have to worry about them blackmailing me anymore."
            a "Good..."
            scene 41-6 ben 108 with Dissolve(1)
            b1 "What will you do?"
            a "I got plenty of other things to attend to."
            a "See you around, Ben."
            b1 "Definitely. Perhaps you'd like to join me for dinner at my place sometime?"
            a "Sounds fun."
            b1 "I know how to make amazing quesadillas."
            a "Till then, Benjamin."
            scene black with Dissolve(1)
            stop ambience
            jump EP13_Evening
        "Allow the hobos to take advantage of Anna to save Ben.":
            jump EP13_Benjamin_2_Sex

label EP13_Benjamin_2_Sex:
    a "{b}*Sigh*{/b}"
    $ persistent.scene_38 = True
    scene 41-6 ben 27 with Dissolve(1)
    a "Fine... If you promise to leave Ben alone after this."
    bum1 "Hehe... We will definitely leave him alone, he's been nothing but a gem."
    a "In that case..."
    "Anna felt an overwhelming sense of regret take over her..."
    play sound cloth_sound1
    scene 41-6 ben 28 with Dissolve(1)
    "But she had to do something to save old Ben."
    bum1 "Huuaaaa... Them titters!"
    bum2 "You are truly a one of kind slut!"
    bum1 "RIGHT???"
    scene 41-6 ben 29 with Dissolve(1)
    pause 1.5
    scene 41-6 ben 30 with Dissolve(1)
    bum2 "And the other one?"
    play sound undress
    scene 41-6 ben 31 with Dissolve(1)
    a "Like that?"
    bum2 "Yeah... Just like that."
    scene 41-6 ben 32 with Dissolve(1)
    bum2 "I just love when women display their tits like that."
    bum2 "It's awe-inspiring. And coming from such a lady like you."
    scene 41-6 ben 33 with Dissolve(1)
    a "Uh... Men..."
    bum2 "Yess... Indeed."
    scene 41-6 ben 34 with Dissolve(1)
    "Ben wasn't going to miss a chance to look at Anna's knockers."
    bum2 "..."
    b1 "..."
    bum1 "..."
    a "Are we done?"
    scene 41-6 ben 35 with Dissolve(1)
    "Anna looked at Ben for a split second."
    a "Seriously?"
    scene 41-6 ben 36 with Dissolve(1)
    "He looked away immediately."
    "He felt awkward, bad, and all around responsible for what was happening."
    scene 41-6 ben 37 with Dissolve(1)
    "There were a couple of onlookers."
    "Locals of the alleyway."
    play audio femgasp
    scene 41-6 ben 38 with Dissolve(1)
    bum1 "Not quite. Ah..."
    bum1 "We still wanna enjoy the sensation of touching your perfect tits."
    a "Ahh..."
    "Anna felt their dirty, cold hands on her luscious breasts."
    "Bare as they laid in front of them..."
    scene 41-6 ben 39 with Dissolve(1)
    a "What..."
    "Anna wasn't exactly surprised by the forwardness of the bum."
    scene 41-6 ben 40 with Dissolve(1)
    bum2 "You gotta {b}Squeeze{/b} them properly, Bill."
    bum2 "Like so, eh?"
    a "Ah... be a bit more gentle."
    bum2 "Sure, sure... We will, hehe."
    scene 41-6 ben 41 with Dissolve(1)
    b1 "{i}...What have I done...{/i}"
    "Benjamin felt overwhelming guilt..."
    "Anna was so nice to him, always."
    "And now he'd put her in such a situation."
    scene 41-6 ben 42 with Dissolve(1)
    a "AaAH!"
    a "That hurts."
    bum2 "Don't lie, you like it."
    bum2 "How about we show you something..."
    a "Oh..."
    play sound cloth_sound1
    scene 41-6 ben 43 with Dissolve(1)
    pause 1
    scene 41-6 ben 44 with Dissolve(1)
    bum2 "Yeah... Hehe..."
    bum2 "I got a fine cock, don't I."
    scene 41-6 ben 45 with Dissolve(1)
    bum1 "I got one, too."
    bum1 "Take a look."
    bum1 "What do you think?"
    a "I... I... It's great."
    scene 41-6 ben 46 with Dissolve(1)
    bum1 "So, how about it?"
    a "What?"
    bum1 "How... About... You... Get on your knees."
    a "WHAT?"
    bum1 "We keep our promise if you keep yours."
    a "I..."
    a "Fine..."
    play sound jacketcloth
    scene 41-6 ben 47 with Dissolve(1)
    "Regretfully, Anna got on her knees..."
    "The things she did to help Ben..."
    "So selfless..."
    scene 41-6 ben 48 with Dissolve(1)
    bum2 "Well, what are you waiting for?"
    a "{i}...This is degrading...{/i}"
    a "{i}...I can't believe, I've gotten myself into yet another situation like this...{/i}"
    "It was a pattern with Anna."
    "Perhaps self-destructive behavior from an underlying condition."
    if AnnaCorruption >= 50:
        "No... It was her true, slutty nature..."
    scene 41-6 ben 49 with Dissolve(1)
    pause 1
    scene 41-6 ben 50 with Dissolve(1)
    a "Both your cocks..."
    bum1 "Yes, Yes!"
    scene 41-6 ben 51 with Dissolve(1)
    a "Mh..."
    "Anna caressed her breasts, as the men stroke themselves."
    "In anticipation to push their cocks deep down Anna's throat."
    scene 41-6 ben 52 with Dissolve(1)
    a "{i}...Their cocks smell so bad...{/i}"
    a "Ugh..."
    scene 41-6 ben 53 with Dissolve(1)
    bum1 "Come on, don't keep us waiting too long, girl."
    a "Yeah... Yeah..."
    bum1 "This is about to become the best evening of my life!"
    bum2 "PREACH, BROTHER!"
    play sound jerk loop
    scene 41-6 ben 56 with Dissolve(1)
    "Anna laid her hand on the bums cock. She felt the cock drawing her in."
    "She felt how the bum's body reacted as she touched it."
    scene EP13_Hobo_Anim_1 with Dissolve(1)
    bum1 "OH... Fuckers..."
    bum1 "Them hands, keep 'em going."
    pause
    scene 41-6 ben 57 with Dissolve(1)
    "And not a moment later she grabbed the other one, too."
    a "Like that?"
    bum2 "Fuck yeah."
    scene 41-6 ben 58 with Dissolve(1)
    "She kept stroking them slowly."
    "Building up to something more."
    scene EP13_Hobo_Anim_2 with Dissolve(1)
    "Not going too fast, not going too slow."
    "Just right."
    pause
    bum1 "Oooh... Fuck."
    scene 41-6 ben 59 with Dissolve(1)
    bum1 "Shiiet. I don't remember the last time some hot slut touched my dick like this."
    bum2 "Ahhh... How about you never had that happen before."
    bum2 "Luck finally smiles on us, man."
    scene 41-6 ben 60 with Dissolve(1)
    "Anna looked at Benjamin for a while."
    "Her face didn't explain much to him, did she enjoy it?"
    "Did she feel disgust or anger?"
    "Benjamin just felt embarrassed, but also turned on."
    "He enjoyed seeing Anna stroking bums. He was as depraved as any of them."
    scene 41-6 ben 61 with Dissolve(1)
    bum1 "How about you go a bit further, eh?"
    a "Fuck... But a deal's a deal, yes?"
    a "If I do it, you leave Ben alone."
    bum2 "Oh yes..."
    scene 41-6 ben 62 with Dissolve(1)
    "As she leaned closer, she smelled the unpleasant odors coming from their junk."
    "It repulsed her..."
    "But at the same time, she sank further into depravity..."
    "Her mind sank deeper into the thought of her being used as nothing but a hole for random bums to enjoy."
    play audio licking_1
    scene 41-6 ben 63 with Dissolve(1)
    "Anna recoiled as she touched the man's penis with her tongue."
    "The taste was unbearable."
    "But she pushed on... She was pleasuring a couple of bums to save another bum."
    "Anna had gotten herself into quite a predicament."
    scene 41-6 ben 64 with Dissolve(1)
    "She didn't want to taste it much more so she just went full in."
    "Push her mouth onto the cock as much as possible."
    "So deep it touched her uvula."
    a "AAHHHH."
    scene 41-6 ben 64-1 with Dissolve(1)
    a "MHh...."
    "And then again..."
    scene 41-6 ben 64 with Dissolve(1)
    a "MHHH."
    a "Khaaaaa..."
    play sound jerk3 loop
    scene EP13_Hobo_Anim_3 with Dissolve(1)
    pause
    a "MHhhh..."
    bum1 "Oooh... Yeah!"
    scene 41-6 ben 65 with Dissolve(1)
    bum1 "Ain't this grand..."
    bum1 "You've brought us a fuck toy, Ben."
    bum1 "I'd say, you've outdone yourself!"
    scene EP13_Hobo_Anim_7 with Dissolve(1)
    pause
    bum1 "Ahhh... FUCCKKK!"
    a "Mmhhh..."
    a "{i}...Anna's eyes watered a bit from the dick...{/i}"
    scene 41-6 ben 66 with Dissolve(1)
    "As the bum was enjoying Anna's mouth, he disregarded her entirely."
    "She was nothing but an object..."
    "They were, after all, completely and utterly void of any moral center."
    "As was Anna, since she allowed herself to be coerced into such actions."
    scene 41-6 ben 67 with Dissolve(1)
    b1 "Damn..."
    b1 "{i}...I wish she'd suck me off like that now...{/i}"
    b1 "{i}...But... She's helped me so much... How could I let this happen...{/i}"
    scene 41-6 ben 68 with Dissolve(1)
    bum1 "Fuck... Alright, alright... Go help out my friend over here."
    a "Ok..."
    scene 41-6 ben 69 with Dissolve(1)
    a "You'd like that, wouldn't you?"
    bum2 "Ohh... Yes. Go on, don't keep me waiting."
    bum2 "That mouth has to be enjoyed."
    scene 41-6 ben 70 with Dissolve(1)
    "Not a moment later Anna was already magnetized to the cock of the other man."
    a "mhh... That cock..."
    "The reality was starting to fade for her..."
    "As she fell deeper into the nothingness of her situation."
    scene 41-6 ben 71 with Dissolve(1)
    a "AAhhhh..."
    bum2 "OH... Shiiit!"
    bum2 "Fuck meee!!"
    scene 41-6 ben 72 with Dissolve(1)
    "She pushed even deeper this time around."
    "Her mind offline, body on autopilot..."
    a "mh... Ah..."
    "Doing the bidding of two homeless men."
    scene EP13_Hobo_Anim_4 with Dissolve(1)
    bum2 "Fuuck... I'm..."
    bum2 "I'm getting super close!"
    bum2 "This slut sucks good!"
    pause
    scene EP13_Hobo_Anim_8 with Dissolve(1)
    a "{i}...Come on... Finish faster...{/i}"
    a "{i}...This is so disgusting...{/i}"
    a "mmhhhhh!!!"
    pause
    bum2 "I'm coming!!! WHAT THE FUUUUUCKK AAH!!!!"
    with flash
    pause
    with flash
    menu:
        "Cum on her face.":
            scene 41-6 ben 73 with Dissolve(1)
            a "Oh!!"
            play sound cum_sound
            scene 41-6 ben 74 with Dissolve(1)
            bum2 "TAKE ITTT!!"
            bum1 "OHHAAAH!"
            scene 41-6 ben 75 with Dissolve(1)
            "Both men shot out streams of their thick sperm onto Anna's soft and silky face."
            "Covering it entirely in their juices."

            scene 41-6 ben 76 with Dissolve(1)
            bum1 "OH FUCK YEAH!"
            bum2 "This is what I'm talking about!!!"
            bum2 "A slut after my own taste!"
            scene 41-6 ben 78 with Dissolve(1)
            bum1 "Hehe... You look absolutely perfect like this."
            bum1 "You should come here more often, this would be a place for you."
        "Cum in her mouth.":
            scene 41-6 ben 79 with Dissolve(1)
            bum2 "TAKE ITTT!!"
            bum1 "OHHAAAH!"
            bum2 "FUCK MEEEEE!!!!!!"
            play sound cum_sound
            scene 41-6 ben 80 with Dissolve(1)
            "The bum pushed his cock so far down her throat, the cum was sent straight to her belly."
            a "HAAAAAA!!"
            play sound cum_sound
            scene 41-6 ben 81 with Dissolve(1)
            a "AHHHH."
            a "Kh..."
            scene 41-6 ben 82 with Dissolve(1)
            bum2 "Fuck!!!"
            scene 41-6 ben 83 with Dissolve(1)
            a "Ah..."
            "After getting her mouth filled to the brim by one bum..."
            scene 41-6 ben 85 with Dissolve(1)
            "She was immediately called by the other one."
            bum1 "Fuck... I can't hold it any longer!!"
            a "WHA?"
            scene 41-6 ben 86 with Dissolve(1)
            "He didn't hesitate and just push his cock as deep in her mouth as possible."
            "Giving her another dose of cum."
            scene 41-6 ben 87 with Dissolve(1)
            bum1 "AAHHHHH!!!!!"
            bum1 "DON'T WASTE A DROP!"
            a "MMMMMMMMMM!!!!!"
            scene 41-6 ben 88 with Dissolve(1)
            pause 2
            scene 41-6 ben 89 with Dissolve(1)
            a "Is... Is that all?"
            scene 41-6 ben 90 with Dissolve(1)
            bum1 "Fuck... Yeah... You've done your part."
    scene 41-6 ben 91 with Dissolve(1)
    "Anna got up and wiped herself... Some got on her chest..."
    a "As her mind returned, Anna inquired."
    a "What about our deal?"
    scene 41-6 ben 92 with Dissolve(1)
    bum1 "Oh... About Ben?"
    bum1 "Sure!"
    bum1 "For now..."
    a "What?"
    bum1 "You didn't think this would be a one-time thing, did you?"
    a "I better not have to come back here..."
    scene 41-6 ben 93 with Dissolve(1)
    "Anna looked at Ben..."
    "All she could see in his eyes was... embarrassment and arousal..."
    "Amongst other feelings."
    a "Come... let's get out of here..."
    scene 41-6 ben 94 with Dissolve(1)
    bum1 "Don't forget about us, sweet, sweet Anna!"
    bum2 "OOH SWEET ANNNA!!!!"
    scene 41-6 ben 95 with Dissolve(1)
    b1 "I'm... Sorry, you had to go through that."
    b1 "For me..."
    b1 "No one has ever done anything so selfless for me..."
    a "I... I don't want to talk about it right now..."
    scene 41-6 ben 96 with Dissolve(1)
    a "I... Hope this was worth it."
    a "It was quite... Uh... Depraving..."
    a "I hope you'll take the job and not steal anymore."
    scene 41-6 ben 97 with Dissolve(1)
    b1 "Anna... You have my word on that."
    b1 "I truly respect what you've done for me."
    b1 "I will show you that I can be good..."
    b1 "Perhaps you'd like to join me for dinner at my place sometime?"
    a "I will think about it..."
    b1 "I know how to make amazing quesadillas."
    a "Till then, Benjamin."
    b1 "Ok..."
    scene black with Dissolve(1)
    "Both were left with thoughts of this ordeal..."
    $ renpy.end_replay()
    pause 1
    stop ambience
    jump EP13_Evening
label EP13_Party:
    $ EP13_var_10 = True
    scene 41-9 party 1 with Dissolve(1)
    "Anna looked at the phone, it was Taxman, who was writing to her."
    t2 "I will pick you up later, wear something sexy, it will help to convince the guy, I'm sure of it."
    a "Ok... See you later..."
    du1 "Hey... Anna?"
    play sound surprise
    scene 41-9 party 2 with Dissolve(1)
    a "Oh."
    a "HEY!"
    scene 41-9 party 3 with Dissolve(1)
    du1 "Good to see you."
    du1 "Uhh... How are you?"
    a "I'm good, I'm good. And you?"
    du1 "Better now."
    scene 41-9 party 4 with Dissolve(1)
    du2 "We just wanted to ask... If you'd join the party?"
    a "OH, yeah. I was thinking about it."
    menu:
        "Agree to go to their party.":
            $ EP13_Party_Attend = True
            a "Sure. I will go. Hah!"
            a "But I have to go to a business dinner, so I will join you for a little while only. Ok?"
            du1 "Yeah, no problem, even a little bit is cool."
            du2 "AWESOME!!!"
            pass
        "Decide not to go.":
            $ EP13_Party_Attend = False
            a "Sorry guys, got a lot on my mind."
            a "Won't be going."
            du2 "OH... Umm, that's fine..."
            a "Take care."
            jump EP13_Alfred
    scene 41-9 party 5 with Dissolve(1)
    a "Don't get too excited, heh."
    du2 "Oh... Yeah, you're right. all good. I'm chill."
    du3 "Word, we all are."
    du2 "Our flat is on the 5th floor. Number 205."
    a "Got it."
    du3 "Heh."
    scene 41-9 party 6 with Dissolve(1)
    du3 "It's just cool that you'll join. I think you are the coolest neighbor in this building."
    du3 "Mostly it's old people. Man, we've got some complaints from them, you never had an issue."
    scene 41-9 party 7 with Dissolve(1)
    a "Trust me, I'm still partying, just like you."
    a "Won't hear any complaints from me."
    du3 "Niiice."
    a "Anyway, I will go home and change, and then I'll see you, eh?"
    du1 "Definitely!"
    a "{i}...I should go to Alfred and get a nice outfit for Taxman...{/i}"
    jump EP13_Alfred
label EP13_Alfred:
    $ EP13_var_11 = True
    scene 41-10 alfred 1 with Dissolve(1)
    a "Hey, Alfred!"
    a2 "Anna... Lovely to see you here."
    a2 "How are you doing?"
    scene 41-10 alfred 2 with Dissolve(1)
    a "I'm... Fine... Some new developments in life..."
    a "Andrew's home."
    a2 "Oh? That's nice!"
    a2 "How is he?"
    a "Still healing. Anyway."
    a "How are you?"
    a2 "I'm good, I'm very good indeed."
    a "Anything new since the fashion show?"
    scene 41-10 alfred 3 with Dissolve(1)
    a2 "Oh yes, I've been getting several offers for my outfit."
    a2 "Not only that, but also several investors would like to invest into my designs."
    a "Really?"
    a "That is wonderful!"
    a2 "Indeed."
    a2 "What brings to you me today?"
    a "I was wondering if you, as a person of fashion, could lend me an outfit?"
    a2 "Oh. Of course, I can."
    scene 41-10 alfred 4 with Dissolve(1)
    a2 "What is it that you'd like?"
    a "Well, it has to be seductive... Umm... A quite revealing... Expressive, perhaps?"
    a2 "Ah... I see."
    scene 41-10 alfred 5 with Dissolve(1)
    a2 "Give me a moment, I will look for something."
    a2 "I have something in mind."
    a "Alright, Thank you so much. I appreciate it a lot!"
    a2 "Think nothing of it."
    scene 41-10 alfred 6 with Dissolve(1)
    a2 "I'll be right back, you can sit down."
    a "Thanks."
    scene 41-10 alfred 7 with Dissolve(1)
    a "{i}...I bet he'll come up with some crazy outfit for me...{/i}"
    a "{i}...This night will be long...{/i}"
    scene 41-10 alfred 8 with Dissolve(1)
    a "{i}...I wonder how Andrew will feel about seeing me in such an outfit...{/i}"
    a "{i}...Well... He'll just have to deal with it for now...{/i}"
    scene 41-10 alfred 9 with Dissolve(1)
    a2 "Alright... One expressive, revealing outfit on the way."
    a2 "I hope it will satisfy your needs, Anna."
    a2 "The one you're wearing right now is pretty 'minimalistic'."
    if AlfredRelationship == True:
        play sound undress
        scene 41-10 alfred 10 with Dissolve(1)
        a "Well... Do you like it?"
        a2 "Whaa..."
        a "Hehe..."
        scene 41-10 alfred 11 with Dissolve(1)
        a "Anyway..."
        a "I'm confident this will be just what I need."
        scene 41-10 alfred 12 with Dissolve(1)
        a2 "KHem... Indeed!"
        a2 "Well... In that case, uhh... take care and enjoy yourself."
        scene 41-10 alfred 13 with Dissolve(1)
        a "I will, thanks a lot again."
        a "I will bring it back as soon as possible."
        a "Then we'll do something else together..."
        a2 "Oh... Hah... Absolutely."
        scene 41-10 alfred 14 with Dissolve(1)
        a2 "No rush, though."
        a2 "Take all the time you need, darling."
        scene 41-10 alfred 15 with Dissolve(1)
        a "See you around, Alfred."
        a2 "And you, Anna."
    else:
        a "I'm certain it will..."
        a "I will try to bring it back as soon as possible."
        scene 41-10 alfred 14 with Dissolve(1)
        a2 "No rush, though."
        a2 "Take all the time you need, darling."
        scene 41-10 alfred 15 with Dissolve(1)
        a "See you around, Alfred."
        a2 "And you, Anna."
    play sound door2
    jump EP13_Change_Outfit
label EP13_Change_Outfit:
    $ EP13_var_12 = True
    if EP13_Party_Attend == True:
        pass
    else:
        a "{i}...Taxman is outside...{/i}"
        scene black with Dissolve(1)
        jump EP13_Taxman
    scene 41-9 party 8 with Dissolve(1)
    a "{i}...Asleep...{/i}"
    a "{i}...Understandable... Getting shot is no small thing...{/i}"
    a "{i}...Still... He should've been upfront with me about Carl from the beginning before he got shot...{/i}"
    scene 41-9 party 9 with Dissolve(1)
    a "{i}...Alright, time to change...{/i}"
    scene black with Dissolve(1)
    play sound undress
    scene 41-9 party 10 with Dissolve(1)
    a "{i}...Well, well... Alfred's gone out of his way to fulfill his fantasies this time...{/i}"
    a "{i}...This is one skimpy dress...{/i}"
    scene 41-9 party 11 with Dissolve(1)
    a "{i}...It will do nicely for the restaurant owner, heh...{/i}"
    a1 "Damn... What is that dress?"
    a "Uh..."
    scene 41-9 party 12 with Dissolve(1)
    a "Oh, this?"
    menu:
        "It's for a working thing... I've got some stuff to do and, yeah...":
            scene 41-9 party 14 with Dissolve(1)
            a1 "Isn't it a bit too revealing?"
            a "What?"
            a "Noo... This is fine..."
            scene 41-9 party 13 with Dissolve(1)
            a1 "Well... Uhm... You look great in it."
            a "Thank you, Andrew."
        "I'm going out for drinks with Rebecca.":
            scene 41-9 party 13 with Dissolve(1)
            a1 "Is it a good idea to go partying dressed like that?"
            a1 "Won't it bring too much attention to you?"
            scene 41-9 party 14 with Dissolve(1)
            a "Naah... I ignore it anyway, I don't like creeps. You know me."
            a1 "Indeed I do."
        "I will use this dress to seduce a restaurant owner.":
            scene 41-9 party 13 with Dissolve(1)
            a1 "WHAT?"
            scene 41-9 party 14 with Dissolve(1)
            a "Haha... I'm just kidding."
            a "I'm going to meet with Emily, we've got a little photoshoot, it's to do with fashion."
            a1 "Oh... Haha... It's pretty revealing, but fashion is fashion."
            a "Indeed."
    scene 41-9 party 15 with Dissolve(1)
    a "So... You like this dress, huh?"
    a1 "Oh. Yeah..."
    a1 "It's very hot..."
    a "Hehe... That's nice to hear."
    scene 41-9 party 16 with Dissolve(1)
    a1 "It's so sexy... So seductive..."
    a1 "Provocative."
    a1 "I mean... It's fine, but I just feel a bit weird that you're dressed like this and other men see you like this."
    a "Oh?"
    a "It's fine, don't think on it too much."
    a1 "Eh..."
    play sound jacketcloth
    scene 41-9 party 17 with Dissolve(1)
    "Anna tried to avoid awkward conversation and changed subject."
    a "Would you want me to take it off for you?"
    a1 "Definitely..."
    a "{i}...Hehe... I like playing with him...{/i}"
    scene 41-9 party 18 with Dissolve(1)
    a1 "I'm getting hard already, only thinking about it."
    a "Well... I know how to push your buttons."
    a1 "Fuck me..."
    a1 "It's been a while since we, you know."
    a "Oh, yeah..."
    scene 41-9 party 19 with Dissolve(1)
    a "Perhaps when, you get a bit better, I will ride your rod like you want it."
    a1 "OOohhh..."
    play sound undress
    scene 41-9 party 20 with Dissolve(1)
    "Anna reached down to his crotch..."
    "Andrew was defenseless..."
    "He couldn't manage another second without Anna... It made him go crazy."
    scene 41-9 party 21 with Dissolve(1)
    a "Oh... Hehe... I touch something down there..."
    a1 "Aaahhhh..."
    a1 "Fuck... I wanna fuck you harder than I ever have."
    a "Patience, sweety..."
    a "Get better and then you'll get what you want."
    a "Remember what the doctor said?"
    a "You'll have to wait."
    scene 41-9 party 22 with Dissolve(1)
    a "For now..."
    a1 "Ahhh..."
    a "This will have to do..."
    a "At least it works, you know?"
    a1 "Fuck... Ok... I'm high as fuck from this medication..."
    a "Heh... Enjoy."
    scene 41-9 party 23 with Dissolve(1)
    a "Alright... Thats enough for now."
    a1 "Ah... Ok."
    scene 41-9 party 24 with Dissolve(1)
    a "Alright, Andrew... See you later, then..."
    a "You need the rest anyway."
    scene 41-9 party 25 with Dissolve(1)
    a1 "Yeah... Fuck..."
    a1 "So hot..."
    scene 41-9 party 26 with Dissolve(1)
    a "Alright, catch you later, hun."
    a1 "Bye!"
    if johnBeenNaked == True:
        play sound door2
        scene 41-9 party 27 with Dissolve(1)
        j4 "Damn... Who picked this out for you?"
        a "Uh... No one. Myself..."
        j4 "Where are you going dressed in this?"
        a "I've got some business to take care of."
        j4 "Huh..."
        a "What?"
        scene 41-9 party 28 with Dissolve(1)
        j4 "I swear I've heard this somewhere in a movie."
        j4 "A girl dresses into a skimpy outfit and goes and takes care of some 'business'"
        a "John! Stop iiit!"
        j4 "Alright, alright."
        j4 "You look ravishing, by the way."
        scene 41-9 party 29 with Dissolve(1)
        a "Thanks."
        j4 "So, where are you headed?"
        a "It's private, hehe..."
        j4 "Alright, alright..."
    play sound door2
    scene 41-9 party 30 with Dissolve(1)
    a "{i}...They said fifth floor, number 205...{/i}"
    a "Ok..."
    scene 41-9 party 31 with Dissolve(1)
    "Anna spent some time looking for the 205..."
    a "205... 205... Let’s see..."
    a "Ah... There it is..."
    play sound doorknock
    scene black with Dissolve(1)
    play sound door2
    play music SexyTimeSong6
    scene 41-9 party 32 with Dissolve(1)
    a "Heyyy..."
    du2 "You... You actually came?"
    a "I did, yeah..."
    scene 41-9 party 33 with Dissolve(1)
    du2 "And... whaaaaat the..."
    "Anna could feel how his youthful gaze pierced her."
    "He could barely believe what was in front of him."
    du2 "Uhh..."
    scene 41-9 party 34 with Dissolve(1)
    "The youthful exuberance was emanating from this man."
    "His hormones were shooting on all cylinders."
    a "Hello?"
    scene 41-9 party 35 with Dissolve(1)
    du2 "Uh... Sorry, sorry... Welcome to our place!"
    a "Thanks, haha!"
    scene 41-9 party 36 with Dissolve(1)
    gi_1 "Who's that?"
    du3 "Oh... Some girl we met at the beach..."
    du3 "Crazy, Ricky went up to her to ask for her number, and she actually decided to give it to him."
    du3 "Better yet, he invited her to the party and she came."
    du3 "Crazy world..."
    gi_1 "Wow... She has huge... Everything..."
    du3 "Riight?"
    scene 41-9 party 37 with Dissolve(1)
    du1 "ANNA!!!! HEY!!"
    du1 "Good stuff... Glad you came..."
    a "So, this is where you guys live?"
    du1 "Word... Pretty cool place ain't it?"
    du1 "We all chip in and pay for this place."
    scene 41-9 party 38 with Dissolve(1)
    a "Impressive."
    du1 "Yeah, we're all studying in university, so."
    du1 "Kinda busy, but you know, work hard, play hard."
    a "Hehe... Nice one."
    scene 41-9 party 39 with Dissolve(1)
    du3 "Hey!"
    a "Hey!"
    scene 41-9 party 40 with Dissolve(1)
    du1 "So. You're here for the first time. We gotta celebrate!"
    du1 "SHOTS!!!"
    a "HAHA, just like that?"
    du1 "I figure that life is but a moment so ain't no way to live if you don't live 100%%"
    scene 41-9 party 41 with Dissolve(1)
    a "What do you study? Philosophy?"
    du1 "EXACTLY! WOOOOOO!"
    a "Haha."
    scene 41-9 party 42 with Dissolve(1)
    du2 "Of course we will join you."
    a "Sure. Hehe..."
    scene 41-9 party 43 with Dissolve(1)
    du3 "Hold up duuudes! Gimme some o’ that too!"
    du1 "We got you, bro!"
    du1 "Come, come!"
    "When Anna entered the apartment, the other girl became almost invisible..."
    scene 41-9 party 44 with Dissolve(1)
    du3 "So... To what?"
    menu:
        "To youth!":
            du1 "Yup, yup!"
            du2 "Yup, yup!"
        "To great parties!":
            du3 "WORD!"
            du3 "Yup, yup!"
        "To getting drunk!!!":
            du3 "YEAAHHH, GIRL!"
            du1 "HAHA!!!"
    play sound drinkingBeverage
    scene 41-9 party 45 with Dissolve(1)
    "All of them chugged the huge shot."
    "Anna felt like it was her mission to show these young dudes how experienced people get shit done."
    "She chugged it along with them."
    scene 41-9 party 46 with Dissolve(1)
    du1 "Damn... You also finished all of it?"
    a "You think I'm some sorta pussy?"
    du3 "HAHA... OHH SNAAAAP!"
    du2 "OWNED, dude, OWNED!"
    scene 41-9 party 47 with Dissolve(1)
    du1 "Damn..."
    du2 "You know, we've got something else, if you'd wanna try?"
    a "Oh?"
    a "Sure..."
    "Anna had a lot on her mind... She needed to let go for a while..."
    "These dudes gave her a way of living in the moment."
    scene 41-9 party 48 with Dissolve(1)
    du1 "We've got something pretty awesome, you'll like it."
    du2 "{i}...Damn, That fucking ass...{/i}"
    a "Well, now I'm even more intrigued."
    scene 41-9 party 49 with Dissolve(1)
    du2 "Have you heard the story of Mary Jane?"
    a "Is that some girl?"
    du2 "Well... A lot of dudes are in love with her... Heh..."
    du1 "You'll like her, too."
    a "Oohh... Haha... Ok."
    play sound lighter
    scene 41-9 party 50 with Dissolve(1)
    du1 "That... is Mary Jane."
    du1 "In other words, weed."
    a "Haha... really?"
    menu:
        "I don't remember the last time I smoked weed...":
            du1 "Well, this will be a good refresher..."
            du1 "If you've ever smoked good weed, then you know."
            du1 "This shit we get, is the bomb..."
        "I... I've never smoked weed before...":
            du1 "Then this is the best way to start."
            du1 "This is about the best weed you can get in town."
            du1 "I mean, the high is so good..."
            du1 "Never gets anyone buzzed in the wrong way."
            a "Ok... Hehe..."
    scene 41-9 party 51 with Dissolve(1)
    "As the guy puffed, Anna felt her moment approach..."
    "She was nervous... Like everyone..."
    "But she'd do anything to get a moment of solace, of zero worries."
    scene 41-9 party 52 with Dissolve(1)
    du2 "Pfuuuu..."
    du2 "Damn... We rolled them good, bro..."
    du1 "Fuuck, yeah... Haha!"
    scene 41-9 party 53 with Dissolve(1)
    du2 "Try some..."
    du2 "Trust me, you won't regret it..."
    "Anna felt a bit anxious, but she just decided to go for it."
    a "Damn..."
    scene 41-9 party 54 with Dissolve(1)
    a "You're gonna give it to me, just like that?"
    du2 "Definitely... We invited you, get to enjoy our courtesy."
    a "Hehe... Alriiight."
    du2 "Reminder, inhale it in your lungs, not your mouth..."
    du2 "Keep it there for a second, then puff out..."
    du2 "It's gonna be awesome!"
    scene 41-9 party 55 with Dissolve(1)
    "Anna hesitated no longer..."
    "And went for it."
    "Taking a good inhale."
    scene 41-9 party 56 with Dissolve(1)
    du2 "Yuup... Hold it for a moment, let it get to you."
    a "Mhmmm...."
    du2 "Annd..."
    scene 41-9 party 57 with Dissolve(1)
    a "Ahhhhh."
    du2 "Juust like that."
    a "Haaa..."
    a "That was... cool..."
    du2 "Just let it work it's magic, let it make you relax."
    scene 41-9 party 58 with Dissolve(1)
    a "Khe..."
    du2 "It's alright, don't worry. Heh..."
    a "Hah... I'm good, I'm good..."
    du2 "That's awesome."
    scene 41-9 party 59 with Dissolve(1)
    a "Here..."
    du1 "Thank you."
    a "You're very welcome."
    du2 "Soo... You wanna tell us more about yourself?"
    a "Not right now, I wanna just enjoy this party..."
    du2 "Oh, that works, too."
    scene 41-9 party 60 with Dissolve(1)
    a "Instead, tell me about yourselves."
    du2 "Sure."
    du2 "Well, I study engineering at the University of Suncity."
    du1 "I study philosophy, like I mentioned before."
    du2 "We are just young wild dudes, trying to enjoy our youth."
    du2 "Tommy always keeps reminding us that this time of our lives is important as fuck."
    scene 41-9 party 61 with Dissolve(1)
    du1 "Haha... Yeah, and we should seize every moment we get."
    du1 "It's important to grab every opportunity you get."
    a "I agree completely."
    a "This is fun, guys... Haha..."
    "The weed was slowly starting to kick in."
    scene 41-9 party 62 with Dissolve(1)
    a "Haha... I think I'm starting to feel it."
    du2 "Yeah... Haha..."
    du2 "That's awesome."
    "Anna's boobs had decided to peak out a little bit and see what the party was like."
    "That of course caught the attention of one of the dudes."
    du2 "{i}...Daaamn...{/i}"
    scene 41-9 party 63 with Dissolve(1)
    a "Oh... Hold on."
    a "Ah... I think I will have to leave abruptly."
    du2 "Huh? Why?"
    a "It's uhh..."
    "Taxman had contacted Anna and said that he was down stairs."
    a "It's the work thing, gotta go."
    du2 "Ah, right... Ok..."
    scene 41-9 party 64 with Dissolve(1)
    a "Yeah... But it's alright... Now I know how fun it is with you guys..."
    a "Just hit me up when ever you can, deal?"
    du1 "Absolutely!"
    du2 "No doubt!"
    scene 41-9 party 67 with Dissolve(1)
    a "Alright... Damn... I'm kinda high... Haha..."
    a "I'm gonna enjoy it my 'work' situation, Haha!"
    du2 "definitely, I've smoked weed before school sometimes, too."
    du2 "Or before work, it's... hella interesting experience."
    a "Alright, I gotta run."
    scene 41-9 party 68 with Dissolve(1)
    du3 "Hey... It was nice you came by!"
    du3 "See you around?"
    a "Yeah... This is fun!"
    a "Haha!"
    a "Byeeee!"
    jump EP13_Taxman
label EP13_Taxman:
    $ EP13_var_13 = True
    play music chill_song_2
    if EP13_Party_Attend == False:
        scene 41-9 party 8 with Dissolve(1)
        a "{i}...Asleep...{/i}"
        a "{i}...Understandable... Getting shot is no small thing...{/i}"
        a "{i}...Still... He should've been upfront with me about Carl from the beginning before he got shot...{/i}"
        scene 41-9 party 9 with Dissolve(1)
        a "{i}...Alright, time to change...{/i}"
        scene black with Dissolve(1)
        play sound undress
        scene 41-9 party 10 with Dissolve(1)
        a "{i}...Well, well... Alfred's gone out of his way to fulfill his fantasies this time...{/i}"
        a "{i}...This is one skimpy dress...{/i}"
        scene 41-9 party 11 with Dissolve(1)
        a "{i}...It will do nicely for the restaurant owner, heh...{/i}"
        a1 "Damn... What is that dress?"
        a "Uh..."
        scene 41-9 party 12 with Dissolve(1)
        a "Oh, this?"
        menu:
            "It's for a working thing... I've got some stuff to do and, yeah...":
                scene 41-9 party 14 with Dissolve(1)
                a1 "Isn't it a bit too revealing?"
                a "What?"
                a "Noo... This is fine..."
                scene 41-9 party 13 with Dissolve(1)
                a1 "Well... Uhm... You look great in it."
                a "Thank you, Andrew."
            "I'm going out for drinks with Rebecca.":
                scene 41-9 party 13 with Dissolve(1)
                a1 "Is it a good idea to go partying dressed like that?"
                a1 "Won't it bring too much attention to you?"
                scene 41-9 party 14 with Dissolve(1)
                a "Naah... I ignore it anyway, I don't like creeps. You know me."
                a1 "Indeed I do."
            "I will use this dress to seduce a restaurant owner.":
                scene 41-9 party 13 with Dissolve(1)
                a1 "WHAT?"
                scene 41-9 party 14 with Dissolve(1)
                a "Haha... I'm just kidding."
                a "I'm going to meet with Emily, we've got a little photoshoot, it's to do with fashion."
                a1 "Oh... Haha... It's pretty revealing, but fashion is fashion."
                a "Indeed."
        scene 41-9 party 15 with Dissolve(1)
        a "So... You like this dress, huh?"
        a1 "Oh. Yeah..."
        a1 "It's very hot..."
        a "Hehe... That's nice to hear."
        scene 41-9 party 16 with Dissolve(1)
        a1 "It's so sexy... So seductive..."
        a1 "Provocative."
        a1 "I mean... It's fine, but I just feel a bit weird that you're dressed like this and other men see you like this."
        a "Oh?"
        a "It's fine, don't think on it too much."
        a1 "Eh..."
        play sound jacketcloth
        scene 41-9 party 17 with Dissolve(1)
        "Anna tried to avoid awkward conversation and changed subject."
        a "Would you want me to take it off for you?"
        a1 "Definitely..."
        a "{i}...Hehe... I like playing with him...{/i}"
        scene 41-9 party 18 with Dissolve(1)
        a1 "I'm getting hard already, only thinking about it."
        a "Well... I know how to push your buttons."
        a1 "Fuck me..."
        a1 "It's been a while since we, you know."
        a "Oh, yeah..."
        scene 41-9 party 19 with Dissolve(1)
        a "Perhaps when, you get a bit better, I will ride your rod like you want it."
        a1 "OOohhh..."
        play sound undress
        scene 41-9 party 20 with Dissolve(1)
        "Anna reached down to his crotch..."
        "Andrew was defenseless..."
        "He couldn't manage another second without Anna... It made him go crazy."
        scene 41-9 party 21 with Dissolve(1)
        a "Oh... Hehe... I touch something down there..."
        a1 "Aaahhhh..."
        a1 "Fuck... I wanna fuck you harder than I ever have."
        a "Patience, sweety..."
        a "Get better and then you'll get what you want."
        a "Remember what the doctor said?"
        a "You'll have to wait."
        scene 41-9 party 22 with Dissolve(1)
        a "For now..."
        a1 "Ahhh..."
        a "This will have to do..."
        a "At least it works, you know?"
        a1 "Fuck... Ok... I'm high as fuck from this medication..."
        a "Heh... Enjoy."
        scene 41-9 party 23 with Dissolve(1)
        a "Alright... Thats enough for now."
        a1 "Ah... Ok."
        scene 41-9 party 24 with Dissolve(1)
        a "Alright, Andrew... See you later, then..."
        a "You need the rest anyway."
        scene 41-9 party 25 with Dissolve(1)
        a1 "Yeah... Fuck..."
        a1 "So hot..."
        scene 41-9 party 26 with Dissolve(1)
        a "Alright, catch you later, hun."
        a1 "Bye!"
        if johnBeenNaked == True:
            play sound door2
            scene 41-9 party 27 with Dissolve(1)
            j4 "Damn... Who picked this out for you?"
            a "Uh... No one. Myself..."
            j4 "Where are you going dressed in this?"
            a "I've got some business to take care of."
            j4 "Huh..."
            a "What?"
            scene 41-9 party 28 with Dissolve(1)
            j4 "I swear I've heard this somewhere in a movie."
            j4 "A girl dresses into a skimpy outfit and goes and takes care of some 'business'"
            a "John! Stop iiit!"
            j4 "Alright, alright."
            j4 "You look ravishing, by the way."
            scene 41-9 party 29 with Dissolve(1)
            a "Thanks."
            j4 "So, where are you headed?"
            a "It's private, hehe..."
            j4 "Alright, alright..."
    play sound door2
    scene 41-11 taxman 1 with Dissolve(1)
    "Taxman was waiting for Anna."
    "And Anna was ready to do her part."
    if EP13_Party_Attend==True:
        "Anna was high from the weed... But she was enjoying herself."
    scene 41-11 taxman 2 with Dissolve(1)
    pause 1
    scene 41-11 taxman 3 with Dissolve(1)
    a "Hey, there..."
    a "Are you waiting for me?"
    t2 "Sure am."
    a "What do you think of the outfit? Will this suffice?"
    scene 41-11 taxman 4 with Dissolve(1)
    t2 "Most definitely."
    t2 "You've come prepared. The guy won't know what hit him."
    t2 "Metaphorically, of course."
    t2 "Alright, get in, let’s do this."
    play sound car_sound1
    scene 41-11 taxman 5 with Dissolve(1)
    a "So. Where are we going?"
    t2 "I made a reservation at La Doria."
    a "Wow... That is one of the most expensive restaurants."
    t2 "Indeed. Appearances are important."
    a "I've been there, it's nice."
    scene 41-11 taxman 6 with Dissolve(1)
    t2 "Are you ready?"
    a "As ready as I will ever be."
    t2 "Don't worry too much. You won't be leading the 'talks' anyway."
    t2 "Like I mentioned before, you are eye candy."
    t2 "That's about it."
    if EP13_Party_Attend == True:
        scene 41-11 taxman 7 with Dissolve(1)
        a "Haha... I'm definitely tasty."
        t2 "Huh?"
        t2 "Wait, are you high?"
        a "Haha... A lil bit. Maybe not a lil bit... Maybe a BIG bit..."
        t2 "Well, that will make things interesting."
    scene 41-11 taxman 9 with Dissolve(1)
    t2 "Alright, we're here."
    a "Fancy, fancy."
    t2 "We'll be here first, The owner will arrive a bit later."
    scene 41-11 taxman 10 with Dissolve(1)
    t2 "I've got it all planned out."
    t2 "Just follow my lead, ok?"
    a "Understood."
    scene 41-11 taxman 11 with Dissolve(1)
    t2 "After you."
    "Taxman didn't speak it out loud, but the moment he noticed Anna..."
    "He craved her..."
    "He wanted her..."
    scene 41-11 taxman 12 with Dissolve(1)
    a "Thank you."
    scene 41-11 taxman 13 with Dissolve(1)
    pause 1
    play sound door2
    play music chill_song_6
    scene 41-11 taxman 14 with Dissolve(1)
    a "Hello."
    t2 "Hello."
    scene 41-11 taxman 15 with Dissolve(1)
    lw_1 "Good evening, sir."
    lw_1 "As always, your table is ready."
    t2 "Yes... Great."
    scene 41-11 taxman 16 with Dissolve(1)
    lw_1 "I hope you are both having a wonderful evening."
    a "Indeed we are, heh."
    lw_1 "That's great to hear."
    scene 41-11 taxman 17 with Dissolve(1)
    t2 "Heh."
    t2 "No matter, business takes precedence, right?"
    a "Oh, yes."
    scene 41-11 taxman 18 with Dissolve(1)
    lw_1 "Right this way, sir and madam."
    play sound undress
    scene 41-11 taxman 19 with Dissolve(1)
    t2 "So, to go over everything once more."
    t2 "You are mostly eye candy."
    t2 "I will lead the talks. We should be able to sway him."
    t2 "I'll make him an offer that will benefit everyone."
    scene 41-11 taxman 20 with Dissolve(1)
    a "Wasn't he worried about the moral implication?"
    a "That it wasn't a good thing to have an illegal thing such as that under his roof?"
    t2 "Haha... Morals."
    t2 "He's a business man, morals will drive him into the ground..."
    t2 "I do respect the notion, though. Have to give him credit for trying, at least."
    scene 41-11 taxman 21 with Dissolve(1)
    sh_c "Greetings. I believe I'm at the right place?"
    t2 "Indeed you are, sir."
    scene 41-11 taxman 22 with Dissolve(1)
    a "Come sit, we've been waiting just for you."
    sh_c "Lucky me. Heh."
    play sound cloth_sound1
    scene 41-11 taxman 23 with Dissolve(1)
    a "I hope you're evening has been pleasant so far?"
    sh_c "It's been... Alright."
    sh_c "Better now, though."
    "Anna already knew that she had some influence over him."
    scene 41-11 taxman 24 with Dissolve(1)
    sh_c "All things considered, of course."
    t2 "Come now. We are all friends here."
    t2 "Or at the very least, lucrative business partners."
    scene 41-11 taxman 25 with Dissolve(1)
    t2 "Say, how about a bottle of wine?"
    t2 "Calisto Red?"
    sh_c "Hah... You know my favourite wine?"
    sh_c "Is that supposed to impress me?"
    t2 "Not at all."
    scene 41-11 taxman 26 with Dissolve(1)
    lw_1 "One Calisto Red?"
    t2 "Thank you."
    t2 "Could you please pour us a glass?"
    lw_1 "Certainly."
    scene 41-11 taxman 27 with Dissolve(1)
    lw_1 "Will you all be ready to order?"
    sh_c "Yes, I'm starving."
    play sound pourwater
    scene 41-11 taxman 28 with Dissolve(1)
    lw_1 "Here you go."
    t2 "I'm going to have the steak and salad, please."
    play sound pourwater
    scene 41-11 taxman 29 with Dissolve(1)
    sh_c "Thank you, ma'am."
    sh_c "I will also have the steak and salad. Make mine rare, please."
    play sound pourwater
    scene 41-11 taxman 30 with Dissolve(1)
    "The waitress leaned in and whispered to Anna."
    lw_1 "Good to see you here, Anna."
    a "Heyyyy..."
    scene 41-11 taxman 31 with Dissolve(1)
    lw_1 "So... Taxman?"
    lw_1 "Looks like you're moving up in the world, eh?"
    a "Hehe... Perhaps."
    lw_1 "So you juggling both of these gentlemen?"
    scene 41-11 taxman 32 with Dissolve(1)
    a "Maybe..."
    a "Heh."
    lw_1 "Oh, you naughty girl..."
    a "I like to keep it spicy, you know?"
    scene 41-11 taxman 33 with Dissolve(1)
    lw_1 "Well, I hope you all enjoy your evening."
    lw_1 "Your food will be made as priority."
    scene 41-11 taxman 34 with Dissolve(1)
    t2 "So. Cheers to future prospects?"
    sh_c "All this is smoke and mirrors, Taxman."
    sh_c "What you want me to do is not something I consider good for me."
    t2 "Come now, we can certainly come to some agreement?"
    scene 41-11 taxman 35 with Dissolve(1)
    sh_c "I doubt that. I will enjoy the wine, though."
    t2 "Of course. That's why I brought you here, I won't stoop to pettiness over business deals."
    t2 "It is, after all, the way the world works."
    sh_c "I know you. Nothing is as simple as it seems."
    sh_c "So, tell me, why do you want to 'infest' my restaurant with illegal gambling so badly?"
    scene 41-11 taxman 35-1 with Dissolve(1)
    t2 "Simply, profits. Nothing else."
    t2 "That place is of strategic value to me, and trust me, you stand to gain significant equity if you play ball."
    sh_c "I don't think any amount of money will convince me of this idea."
    sh_c "What bothers me, is, how open you are about that illegal den."
    sh_c "What if I go to the cops?"
    t2 "I'm certain you'll refrain from that."
    scene 41-11 taxman 36 with Dissolve(1)
    a "{i}...This conversation is getting heated...{/i}"
    a "{i}...Perhaps I should intervene and do something about it?{/i}"
    play sound drinkingBeverage
    scene 41-11 taxman 37 with Dissolve(1)
    pause 1
    scene 41-11 taxman 38 with Dissolve(1)
    t2 "It wouldn't go well for anyone if you did."
    sh_c "Are you threatening me?"
    t2 "No... I'm merely remarking upon the factual significance of the choice of going to the cops."
    t2 "Why did you come here at all then?"
    sh_c "To see what kind of an offer you'd make... I know you and your reputation."
    sh_c "And I don't like it."
    menu:
        "Anna should intervene and work her charms on the man.":
            $ EP13_Anna_Convince_Owner = True
            play music SexyTimeSong5
            scene 41-11 taxman 39 with Dissolve(1)
            a "Ok, ok... Perhaps we could approach it from a different angle."
            sh_c "What other angles are there?"
            sh_c "Taxman only talks money. Not the language I'd use."
            a "I'm not Taxman, as you are aware."
            sh_c "Indeed."
            scene 41-11 taxman 40 with Dissolve(1)
            a "I've come a long way in life, and I can be very persuasive."
            sh_c "What can you possibly offer me, that Taxman can't?"
            a "Hehe... There are plenty of things."
            scene 41-11 taxman 41 with Dissolve(1)
            "Taxman quickly caught on. He kept a cool head and understood that he was losing control of the conversation."
            "Now Anna had brought the balance back... He allowed her to continue."
            scene 41-11 taxman 42 with Dissolve(1)
            sh_c "Uh... Hm..."
            a "Trust me, I can do a lot of different things."
            a "I'm very talented."
            sh_c "Surely."
            scene 41-11 taxman 43 with Dissolve(1)
            a "Would you like it if I gave you a demonstration?"
            sh_c "Hmh... I... Perhaps..."
            a "That is what I like to hear."
            a "Say it."
            a "Say that you want me to give you a demonstration."
            scene 41-11 taxman 44 with Dissolve(1)
            sh_c "I... I... Uhh..."
            sh_c "I want you to give me a demonstration..."
            a "Hehe... Good."
            scene 41-11 taxman 45 with Dissolve(1)
            a "Alright, then."
            a "How about I..."
            play sound zipper_1
            scene 41-11 taxman 46 with Dissolve(1)
            a "Oh... Hehe..."
            a "Looks like you've been waiting for something like this?"
            sh_c "Not... Not until this moment..."
            a "Well then. Looks like I've already shown you a bit of what I can do."
            a "Would you like me to continue?"
            sh_c "I... Would..."
            scene 41-11 taxman 47 with Dissolve(1)
            a "Mmmmhhmmm..."
            a "It's so big in my hand."
            a "You are very well endowed, mister."
            sh_c "Ah.... Thanks..."
            scene 41-11 taxman 48 with Dissolve(1)
            sh_c "You are... Very, very talented..."
            a "I know... So... How about we do something about the deal?"
            a "We could surely come to some arrangement?"
            sh_c "Ahh... Fuck..."
            scene 41-11 taxman 49 with Dissolve(1)
            sh_c "You... Make a good point..."
            a "We would be very generous with the money as well..."
            a "You wouldn't even have to participate in the day-to-day…"
            sh_c "That's... True..."
            a "And your restaurant would be able to flourish."
            scene 41-11 taxman 50 with Dissolve(1)
            t2 "{i}...Holy shit...{/i}"
            t2 "{i}...She's actually convincing him, what the hell...{/i}"
            "Taxman was in disbelief how well Anna was handling the situation."
            play sound jerk loop
            scene 41-11 taxman 51 with Dissolve(1)
            sh_c "Ahh... Keep going..."
            sh_c "Fuuckkk... Those hands... Yeah... Sure..."
            sh_c "Just don't stop..."
            a "Of course..."
            scene 41-11 taxman 52 with Dissolve(1)
            a "{i}...It's so easy to manipulate people with my body...{/i}"
            a "{i}...I could become the president if I really wanted to...{/i}"
            "Anna felt the man's cock pulsating in her hands... Ready to shoot any second."
            scene EP13_Taxman_Anim_5 with Dissolve(1)
            pause
            sh_c "Ah..."
            a "Mmm..."
            pause
            scene EP13_Taxman_Anim_5_Faster with Dissolve(1)
            pause
            sh_c "Fuck... I'm... Getting close..."
            scene 41-11 taxman 52-1 with Dissolve(1)
            "The waitress noticed Anna doing something under the table with the man..."
            lw_1 "Oh... Such perversion..."
            lw_1 "I love it..."
            scene 41-11 taxman 53 with Dissolve(1)
            sh_c "Fuck... I'm about to cum..."
            scene EP13_Taxman_Anim_6 with Dissolve(1)
            a "Then cum... I want all your sperm..."
            a "Do it... You pervert."
            a "Cum in my hand."
            scene EP13_Taxman_Anim_6_Faster with Dissolve(1)
            sh_c "Fhhh..."
            sh_c "Ahh... Ahhh!"
            a "Yeah... Just like that."
            play sound cum_sound
            scene 41-11 taxman 54 with flash
            pause 1
            scene 41-11 taxman 55 with flash
            sh_c "Shiit..."
            sh_c "Ahh..."
            play sound licking_1
            scene 41-11 taxman 56 with Dissolve(1)
            sh_c "Damn..."
            sh_c "You are crazy... And I love it."
            a "Mmmm..."
            "Anna had done her part to convince the man..."
            scene 41-11 taxman 57 with Dissolve(1)
            "Taxman was still a bit in shock..."
            "But nothing he couldn't take advantage of."
            scene 41-11 taxman 58 with Dissolve(1)
            a "So... I think, perhaps, that we could come to an arrangement."
            a "I as an intermediary think that the deal is not bad at all, right Taxman?"
            scene 41-11 taxman 59 with Dissolve(1)
            t2 "Uhh... Indeed. I'm very generous, and like Anna mentioned, you wouldn't have to be a part of the day to day."
            t2 "I'm merely trying to make a unified front."
            sh_c "Shiit..."
            sh_c "Anna does make a good point."
            t2 "And... If you do, this won't be the last time you'd be able to enjoy some 'benefits'."
            scene 41-11 taxman 60 with Dissolve(1)
            sh_c "Heh... Well..."
            sh_c "I can see that working to my advantage."
            sh_c "Fuck... Fine... I will allow you to make the gambling den in my restaurant."
            t2 "Great."
            t2 "Trust me, we all will earn a fair amount of money from this venture."
            scene 41-11 taxman 62 with Dissolve(1)
            lw_1 "Here you are..."
            lw_1 "I hope you enjoy your meal."
            t2 "Thank you."
            scene 41-11 taxman 63 with Dissolve(1)
            lw_1 "Here you go."
            a "Thank you."
            scene 41-11 taxman 65 with Dissolve(1)
            lw_1 "I hope you all enjoy your meal."
            scene 41-11 taxman 66 with Dissolve(1)
            t2 "Alright, let's dig in and discuss some of the finer details of the deal."
            sh_c "I'm all ears..."
            scene black with Dissolve(1)
            "Some time later..."
            scene 41-11 taxman 67 with Dissolve(1)
            a "That was some fine steak."
            t2 "Couldn't agree more. This is, after all, one of the best places in town."
            sh_c "I still think I make better food at my restaurant."
            t2 "And now, with the funds, you'll be able to expand."
            sh_c "Huh... Fair enough..."
            scene 41-11 taxman 68 with Dissolve(1)
            lw_1 "So, how was your meal?"
            t2 "It was pristine, the steak was perfectly cooked."
            lw_1 "I'm happy to hear that."
            t2 "Please put this on my tab, the owner has my account, he can withdraw the funds."
            t2 "And give yourself a generous tip."
            lw_1 "I will relay the info to the owner..."
            lw_1 "Thank you for dining at La Doria."
            scene black with Dissolve(1)
            play sound door2
            scene 41-11 taxman 69 with Dissolve(1)
            t2 "So, I can safely assume that you will be ready within the next couple of days for the second phase?"
            sh_c "Sure... Yeah..."
            sh_c "When do I get to meet Anna?"
            t2 "She might come to the restaurant during the second phase. Together with me."
            sh_c "Great... I will keep that in mind."
            scene 41-11 taxman 70 with Dissolve(1)
            a "Pleasure doing business with you."
            sh_c "Likewise... Heh..."
            sh_c "I hope we get to meet again."
            a "You can count on that."
            a "Take care..."
            play sound car_sound1
            scene 41-11 taxman 71 with Dissolve(1)
            t2 "Well... I gotta say."
            t2 "That was not what I expected..."
            a "I know, you wanted me to not step in."
            a "But from my perspective, you both were starting to become increasingly agitated."
            a "Like you were about to blow."
            t2 "No, no... Don't get me wrong, I'm impressed. I'm glad you took control of the sitaution."
            scene 41-11 taxman 73 with Dissolve(1)
            t2 "I didn't even consider that at first."
            t2 "But when I saw you doing it and how the man changed his demeanor."
            t2 "I know you had him by the balls, literally... Haha."
            scene 41-11 taxman 72 with Dissolve(1)
            t2 "And that... makes me wonder..."
            t2 "What else are you good at?"
            if TaxmanFootjob == True:
                t2 "I mean, I know that your feet are magnificent..."
            menu:
                "Would you like to find out?":
                    $ EP13_Anna_Sex_Taxman = True
                    play music sideroad
                    scene 41-11 taxman 73 with Dissolve(1)
                    t2 "Hehe... I would."
                    a "Well, then... There's a quiet parking near my place."
                    t2 "Excellent."
                    play sound car_sound1
                    jump EP13_Taxman_Sex
                "Nothing, I think you can take me home now.":
                    t2 "Huh... Fine... A job well done..."
                    a "Yeah, I will be heading out."
                    t2 "Alright... You sure?"
                    a "Yeah."
                    scene 41-11 taxman 77 with Dissolve(1)
                    t2 "Well... It was a pleasure."
                    a "Likewise."
                    t2 "If you ever decide that you would like some more work, contact me."
                    a "I will think about it."
                    scene black with Dissolve(1)
                    pause 1
                    play sound door2
                    scene 41-12 home 1 with Dissolve(1)
                    a "He's asleep..."
                    if BenjaminContent == True:
                        a "I should go check up on Benjamin, ask him about the stolen item."
                        jump EP13_Benjamin_2
                    else:
                        jump EP13_Evening
        "Anna should refrain from interrupting.":
            $ EP13_Anna_Convince_Owner = False
            scene 41-11 taxman 40-1 with Dissolve(1)
            sh_c "I know I'm putting my life in jeopardy by refusing you, but let me tell you, I won't go quietly."
            "the conversation was getting ever so aggressive."
            sh_c "I think this has 'meeting' has been going on for too long."
            play sound jacketcloth
            scene 41-11 taxman 41-1 with Dissolve(1)
            sh_c "You are not a good man."
            sh_c "I will not be doing business with you."
            t2 "{i}...Damn... This mothefucker...{/i}"
            scene 41-11 taxman 42-1 with Dissolve(1)
            sh_c "You should be careful around him..."
            sh_c "Or you might actually be his slut..."
            sh_c "Did he bring you here as eyecandy?"
            sh_c "Hah..."
            sh_c "Pathetic..."
            sh_c "Go to hell, both of you."
            scene 41-11 taxman 43-1 with Dissolve(1)
            "The man left. Both Anna and Taxman were speechless for a moment."
            t2 "Well... That went worse than I expected..."
            t2 "I think it's time for us to leave."
            a "Ok..."
            scene 41-11 taxman 71 with Dissolve(1)
            a "So, you gonna take me home?"
            t2 "Yeah... Our business is concluded..."
            t2 "I will have to approach this differently."
            a "I don't think I want to know."
            t2 "It's best if you don't."
            scene 41-11 taxman 72 with Dissolve(1)
            t2 "This all has me annoyed."
            a "Me too... He was pretty angry."
            t2 "That doesn't matter... But the fact that I can't get the restaurant like this..."
            t2 "I need to let off some steam..."
            if TaxmanFootjob == True:
                t2 "I know that your feet are magnificent..."
                t2 "That could take the edge off."
            scene 41-11 taxman 73 with Dissolve(1)
            menu:
                "Perhaps I can help you?":
                    $ EP13_Anna_Sex_Taxman = True
                    play music sideroad
                    scene 41-11 taxman 73 with Dissolve(1)
                    t2 "Perhaps..."
                    a "We are near my house... There's a quiet parking there."
                    t2 "Lovely..."
                    jump EP13_Taxman_Sex
                "Well, good luck with that.":
                    t2 "Huh... Fine... Thank you for your 'help'..."
                    a "Yeah, I will be heading out."
                    t2 "Alright..."
                    a "Yeah."
                    scene 41-11 taxman 77 with Dissolve(1)
                    t2 "Well... Things could've gone better, but... It is what it is..."
                    a "Yeah... Sorry..."
                    scene black with Dissolve(1)
                    pause 1
                    play sound door2
                    scene 41-12 home 1 with Dissolve(1)
                    a "He's asleep..."
                    if BenjaminContent == True:
                        a "I should go check up on Benjamin, ask him about the stolen item."
                        jump EP13_Benjamin_2
                    else:
                        jump EP13_Evening
            pass
label EP13_Taxman_Sex:
    $ persistent.scene_39 = True
    scene 41-11 taxman 74 with Dissolve(1)
    t2 "I think this will work perfectly."
    a "Away from prying eyes."
    t2 "That's what I was going for... But I don't care, personally."
    scene 41-11 taxman 75 with Dissolve(1)
    t2 "When I look at you, uhh..."
    t2 "Something changes in me..."
    a "Hehe... I have that effect on people."
    a "So... About my part in the 'business'..."
    t2 "Well, this was a one time thing..."
    a "Well... Then we have nothing to talk about..."
    scene 41-11 taxman 76 with Dissolve(1)
    "Anna got out of the car..."
    t2 "Huh? Wait!"
    scene 41-11 taxman 77 with Dissolve(1)
    t2 "Fine... You'll get 5%%."
    a "Seriously, that cheap?"
    t2 "10%%?"
    a "That's better."
    scene 41-11 taxman 78 with Dissolve(1)
    a "I knew we could come to some arrangement."
    t2 "Hehe... You're slick, I'll give you that."
    if TaxmanFootjob == True:
        t2 "I remember what your feet were like..."
        t2 "That was but a taste..."
        t2 "Now I want more."
    else:
        a "I know just the thing you'd like."
    "The night was darkening."
    "The city was alive on a Saturday night..."
    scene 41-11 taxman 80 with Dissolve(1)
    a "How about something like this?"
    play sound cloth_sound1
    scene 41-11 taxman 81 with Dissolve(1)
    t2 "Hehe..."
    t2 "That's what I'm talking about."
    t2 "Those tits are priceless."
    a "Why thank you."
    t2 "I can't wait any longer... I CRAVE you."
    play sound kisspeck
    scene 41-11 taxman 82 with Dissolve(1)
    "Taxman suddenly got very close and started to touch and kiss Anna all over."
    a "AHH..."
    t2 "Mmmm...."
    a "Oh..."
    "Anna liked that Taxman was kissing her neck... It sent goosebumps down her body."
    scene 41-11 taxman 83 with Dissolve(1)
    a "Ah..."
    "Quiet moans could be heard from Anna."
    "Taxman was kissing her body with such passion... With such grace."
    "Anna rarely felt a man take that route."
    "Anna got more turned on with every kiss..."
    scene 41-11 taxman 83-1 with Dissolve(1)
    a "Lemme show you what I got..."
    t2 "Go ahead... ahh..."
    scene 41-11 taxman 84 with Dissolve(1)
    a "Hehe..."
    a "How about I..."
    scene 41-11 taxman 85 with Dissolve(1)
    a "Help you with something down there?"
    a "I know it gets hard... And it needs attention."
    t2 "Fuck... You aren't wrong."
    scene 41-11 taxman 86 with Dissolve(1)
    t2 "Mmm... So hot..."
    a "You like them?"
    t2 "Oh yes... Oh fuck yes."
    play sound undress
    scene 41-11 taxman 87 with Dissolve(1)
    a "Well then... wanna see what I can do with them?"
    t2 "Ohhh... Yes..."
    t2 "Anna... you are so hot... So FUCKING hot..."
    play sound cloth_sound1
    scene 41-11 taxman 88 with Dissolve(1)
    t2 "Aahhhh..."
    "As soon as Anna touched his dick, Taxman felt a surge of excitement rush his body."
    "Like a drug..."
    a "{i}...Hehe... I bet he'll like this...{/i}"
    a "{i}...Pervert... Heh...{/i}"
    scene 41-11 taxman 89 with Dissolve(1)
    a "Oh... It feels so nice..."
    a "You like how my feet massage your cock?"
    t2 "I... Ahhh..."
    t2 "Better than any I ever have had."
    scene 41-11 taxman 90 with Dissolve(1)
    a "Hmm..."
    a "How about we lose the jacket?"
    t2 "Sure... I don't need it anyway."
    scene 41-11 taxman 91 with Dissolve(1)
    pause 0.5
    play audio undress
    play sound jerk2 loop
    scene EP13_Taxman_Anim_9 with Dissolve(1)
    pause
    t2 "Ooh..."
    t2 "Keep it up..."
    pause

    a "oh..."
    a "{i}...He seems to be enjoying himself a lot...{/i}"
    pause
    scene 41-11 taxman 92 with Dissolve(1)
    a "You like that?"
    a "When I stroke your cock with my feet?"
    t2 "Oh... Yeahh..."
    play sound jerk loop
    scene 41-11 taxman 93 with Dissolve(1)
    t2 "Keep going..."
    t2 "Fuck, you're hot..."
    "Anna slightly increased the pace."
    "As she rubbed her feet against his cock, Taxman moaned a little bit..."
    scene EP13_Taxman_Anim_10 with Dissolve(1)
    t2 "Mhh..."
    pause
    a "Mhm..."
    t2 "Ooh yeah..."
    scene EP13_Taxman_Anim_10_1 with Dissolve(1)
    pause
    a "{i}...Oh... He's enjoying it a lot, hehe...{/i}"
    pause
    t2 "Fuuckk..."
    t2 "Mhm... Ah."
    scene 41-11 taxman 94 with Dissolve(1)
    t2 "Oh... Ahh..."
    a "Does this satisfy you?"
    t2 "Ohh... Ahh..."
    "Anna changed motion now and then to keep Taxman interested..."
    "He of course was into anything Anna was doing."
    stop sound
    scene 41-11 taxman 95 with Dissolve(1)
    t2 "Alright... Before I get too excited..."
    t2 "Let me enjoy something else."
    a "Oh... Hehe... You want to go all the way?"
    t2 "I want to enjoy every part of you, Anna."
    scene 41-11 taxman 96 with Dissolve(1)
    a "Come here, big boy."
    play sound jacketcloth
    scene 41-11 taxman 97 with Dissolve(1)
    t2 "Oh... That pussy..."
    "It wouldn't be an understatement to say, that Anna's pussy was one of the most sought-after in the city."
    "She was slowly garnering influence among the city´s elite."
    "One of whom was the Taxman."
    play sound undress
    scene 41-11 taxman 98 with Dissolve(1)
    a "just like that."
    t2 "Show them to me... I wanna see all of you."
    "With every moment, getting closer to what they truly wanted..."
    scene 41-11 taxman 99 with Dissolve(1)
    "Anna looked around a bit if there was anyone who could see them..."
    "Even though the city was alive and well... No one was disturbing them..."
    "Perhaps some onlookers from apartment building windows."
    play sound undress
    scene 41-11 taxman 100 with Dissolve(1)
    t2 "Oh. Yeah..."
    t2 "You are one magnificent sight."
    a "Well, what are you waiting for?"
    scene 41-11 taxman 101 with Dissolve(1)
    a "That's right..."
    a "Come closer."
    scene 41-11 taxman 102 with Dissolve(1)
    a "Mhhmm..."
    "The hood of the car was warm... It made it easy for Anna to get into a comfortable position..."
    "To be penetrated by Taxman..."
    "It was a looong time coming..."
    t2 "I've been waiting for this..."
    play audio surprise
    play audio female_moan_5
    play sound jerk2 loop
    scene 41-11 taxman 103 with vpunch
    pause 0.5
    play audio female_moan_2
    scene 41-11 taxman 104 with vpunch
    a "AHHH!"
    "Not a moment later, Taxman had already made his way into Anna's pussy hole."
    a "Nhhh..."
    t2 "OOooo Fuuuuuuckkk..."
    t2 "That's just... Wow..."
    scene 41-11 taxman 105 with Dissolve(1)
    a "Oh..."
    a "Taxman..."
    t2 "Anna... That pussy is... Fucking glorious..."
    scene EP13_Taxman_Anim_12 with Dissolve(1)
    play audio femmoan_2
    a "Ahh..."
    play audio femmoan_4
    a "MMmmmhhh..."
    play audio female_moan_3

    scene 41-11 taxman 106 with Dissolve(1)
    "Their moans could be heard lightly echoing off the buildings..."
    play audio female_moan_4
    "They might've even gained some attention from the regular folks..."
    "But it mattered not to them. They were in their own pleasure world."
    scene 41-11 taxman 107 with Dissolve(1)
    a "Ahh..."
    a "Faster..."
    a "AH... FASTER!"
    scene EP13_Taxman_Anim_11 with Dissolve(1)
    play audio moaningthree
    a "OoHHHHH!!"
    pause
    "Anna's mind was filled with pleasure..."
    "She craved penetration..."
    "From powerful men."

    scene 41-11 taxman 108 with Dissolve(1)
    "The car was shaking from Taxman's penetration."
    "He fucked hard."
    "And that's what Anna liked."
    scene EP13_Taxman_Anim_13 with Dissolve(1)
    play audio femgasp
    pause
    a "Fuck me like you mean it... AAHHH!!"
    a "Ahh..."
    a "AHHHHH!!!"
    t2 "Fuck... Ah..."
    scene 41-11 taxman 110 with Dissolve(1)
    t2 "Fuck... I'm going to fucking cum soon..."
    t2 "That pussy ain't a joke!"
    play audio femmoan_2
    scene EP13_Taxman_Anim_14 with Dissolve(1)
    a "AHH!"
    t2 "FUCK!"
    t2 "MY COCK!"
    "Their screams were getting louder and louder..."
    t2 "I'm about to bust"
    scene EP13_Taxman_Anim_15 with Dissolve(1)
    play audio moaning_1
    t2 "I'm.. Fuck... Ah!"
    t2 "Oh... Shit... SHIIIT!!"
    pause
    scene EP13_Taxman_Anim_15_Faster with Dissolve(1)
    t2 "AHHHH."
    t2 "FUUUUUUUUUUUCCCKKK!!"
    with flash
    pause
    with flash
    menu:
        "Cum in Anna's pussy.":
            play sound cum_sound
            scene 41-11 taxman 111 with Dissolve(1)
            with flash
            t2 "Ahhh."
            with flash
            t2 "Ahhh..."
            t2 "...."
            with flash
            t2 "AAHHHHHH...."
            scene 41-11 taxman 112 with Dissolve(1)
            t2 "Shit..."
            scene 41-11 taxman 113 with Dissolve(1)
            "Anna's pussy was leaking cum..."
            "Taxman didn't mind giving her all of his load."
            scene 41-11 taxman 114 with Dissolve(1)
            t2 "Damn."
            t2 "That was hot."
            t2 "We gotta do this more often."
            scene 41-11 taxman 115 with Dissolve(1)
        "Cum on her body.":
            play sound cum_sound
            scene 41-11 taxman 116 with Dissolve(1)
            t2 "AAHHHH!!!!!"
            with flash
            with flash
            t2 "AAHH."
            a "Cum all over me, please!"
            with flash
            t2 "YEAH!"
            scene 41-11 taxman 117 with Dissolve(1)
            a "Mmhmmm..."
            t2 "Oh fuck."
            t2 "You might the best fuck I've ever had..."
            a "Really?"
            t2 "Possibly..."
            scene 41-11 taxman 118 with Dissolve(1)
            t2 "I mean just look at this."
            t2 "You fucking know how to rock somebody’s world."
            scene 41-11 taxman 119 with Dissolve(1)
            t2 "Damn... Covered in my cum..."
            a "I knew you'd like that, hehe..."
            t2 "Indeed..."

    a "{i}...This is so exciting...{/i}"
    a "{i}...Doing it outside, while someone could see us...{/i}"
    a "Hehe... I can see you enjoyed yourself."
    play sound undress
    scene black with Dissolve(1)
    "Anna cleaned up..."
    scene 41-11 taxman 120 with Dissolve(1)
    a "So... Does that conclude our dealings?"
    t2 "Well... Sure, but if you'd like to continue..."
    t2 "I have other jobs I can offer you."
    a "Oh?"
    scene 41-11 taxman 121 with Dissolve(1)
    t2 "Yeah."
    t2 "There is plenty to do in the city, trust me."
    t2 "Just think about it, ok?"
    a "I will..."
    scene 41-11 taxman 122 with Dissolve(1)
    "Anna finished her 'meeting' with Taxman and left."
    scene black with Dissolve(1)
    "A couple of moments before..."
    play sound femgasp_1_wet
    scene 41-11 taxman 123 with flash
    a1 "Huh..."
    "Andrew was woken up by some loud moaning..."
    a1 "What... Fuck... I'm high..."
    scene 41-11 taxman 124 with Dissolve(1)
    "He got up and walked to the window to check the commotion."
    "He could not focus his eyes on the people outside..."
    "The drugs made him very sedated."
    a1 "Damn... Somebody's having fun..."
    a1 "Eh... I want some too. damn..."
    scene 41-11 taxman 125 with Dissolve(1)
    a1 "Gotta get healthy, could maybe enjoy Anna a bit..."
    play audio femmoan_3
    scene black with Dissolve(1)
    pause 1
    play sound door2
    scene 41-12 home 1 with Dissolve(1)
    a "He's asleep..."
    $ renpy.end_replay()
    if BenjaminContent == True:
        a "I should go check up on Benjamin, ask him about the stolen item."
        jump EP13_Benjamin_2
    else:
        jump EP13_Evening
label EP13_Evening:
    $ EP13_var_14 = True
    scene 41-12 home 2 with Dissolve(1)
    a "{i}...What a day...{/i}"
    a "A lot has happened..."
    a "I should get some sleep..."
    scene 41-12 home 3 with Dissolve(1)
    a "{i}...Andrew is tight asleep...{/i}"
    a "{i}...Should keep it that way for the next couple of days...{/i}"
    if AnnaCorruption <= 20:
        a "{i}...He needs the rest...{/i}"
        a "{i}...We should figure things out... I haven't been the best...{/i}"
    scene black with Dissolve(1)
    stop music
    pause 1
    show text "Sunday Morning."
    play sound interface_sound
    scene 42-1 morning 1 with Dissolve(1)
    a "Ahh..."
    play music tranquility
    a "{i}Perhaps Sunday will be a bit less eventful...{/i}"
    if AnnaCorruption >=30:
        a "{i}...I wonder what things would be like if I wasn't so interested in other men...{/i}"
    if AnnaCorruption <= 10:
        a "{i}I can't wait to spend my entire life together with him...{/i}"
        a "{i}...I just have to sort out some stuff...{/i}"
    scene 42-1 morning 2 with Dissolve(1)
    a "{i}...Some coffee would be good...{/i}"
    a "{i}...What interesting things could I do today...{/i}"
    play sound phonecall
    scene 42-1 morning 3 with Dissolve(1)
    a "Hello?"
    m1 "Anna! Hey."
    m1 "I'm terribly sorry for contacting you at this hour on a Sunday."
    m1 "But I think you won't mind."
    m1 "It's to do with BBD Inc."
    m1 "They've invited us to come to the ritual today."
    a "Today already?"
    scene 42-1 morning 4 with Dissolve(1)
    m1 "Yeah, I don't know why on a Sunday, but I suppose they want to close the deal as soon as possible."
    a "Makes sense..."
    m1 "Yeah!"
    m1 "We have to leave soon if we want to reach them until the end of the day."
    m1 "I've already contacted our upper management, they've prepped the plane."
    a "Alright, I'll get ready and meet you at the airport."
    scene 42-1 morning 5 with Dissolve(1)
    a1 "Heyyy..."
    if AnnaCorruption <=20:
        a "Morning, sleeping head."
    else:
        a "Morning."
    a1 "You're up early. Out and about."
    a "Ah... Yeah... I've got some work stuff."
    scene 42-1 morning 6 with Dissolve(1)
    a "We've got a closing with one client and I've got to catch a flight."
    a1 "Damn... Anna, you've been keeping busy."
    a "Yeah."
    if EP13_Anna_Sex_Taxman == True:
        a1 "You won't believe it..."
        a1 "I saw some people fucking in the parking lot of the house..."
        play sound surprise
        scene 42-1 morning 7 with Dissolve(1)
        a "What?!"
        a1 "Yeah... Crazy people."
        scene 42-1 morning 8 with Dissolve(1)
        a "Umm... You didn't see who they were, right?"
        a1 "No... My vision is blurry from the pills."
        a "Oh... I... see."
        "Anna felt a boulder roll off her shoulders once more."
    a "Anyway... I will be heading out shortly."
    a1 "I see..."
    scene 42-1 morning 9 with Dissolve(1)
    a "But... when I come back..."
    a "We will have a nice talk about all that has happened."
    a1 "Sounds good."
    a "Meanwhile, you rest. Ok?"
    play sound kisspeck
    scene 42-1 morning 10 with Dissolve(1)
    pause 1
    scene 42-1 morning 11 with Dissolve(1)
    a "Take care for now."
    a1 "See you later, then."
    play sound door2
    scene 42-1 morning 12 with Dissolve(1)
    a "Hey."
    j4 "Morning."
    j4 "So. What you up to on a Sunday?"
    a "Work."
    j4 "Really? You're dedicated."
    scene 42-1 morning 13 with Dissolve(1)
    a "No other choice, the client wants to meet today."
    j4 "Understandable."
    j4 "How did yesterday go?"
    if EP13_Anna_Convince_Owner == True:
        a "Smoothly, managed to do what was intended."
    else:
        a "We failed to do what was necessary..."
    j4 "Will you tell me about what you did?"
    a "Some other time, anyway, I gotta run."
    if johnBeenNaked == True:
        j4 "Well, the outfit really was something."
        j4 "You looked amazing."
        j4 "Makes me wonder, what you did."
        a "Some other time, gotta run!"
    scene 42-1 morning 14 with Dissolve(1)
    a "Take care of Andrew while I'm gone, ok?"
    j4 "Sure, sure."
    a "Alright... See you later!"
    j4 "Bye!"
    scene black with Dissolve(1)
    play sound car_sound1
label EP13_BBDInc:
    play music chill_song_2
    scene 42-2 plane 1 with Dissolve(1)
    a "Hey!"
    m1 "Hello, Anna!"
    a "Wow... I like the outfit."
    m1 "Tombale mentioned to go casual, it's hot there."
    scene 42-2 plane 2 with Dissolve(1)
    m1 "I could say the same about you, although the black color will make you hotter."
    m1 "Both physically and metaphorically."
    a "Haha... Let's go, smartass."
    play sound plane_fly
    scene 42-2 plane 3 with Dissolve(1)
    a "So... What are we expecting."
    m1 "Well, I know as much as you."
    m1 "All I did was prepare the treats."
    a "Nice."
    a "What did you get?"
    scene 42-2 plane 4 with Dissolve(1)
    m1 "Well, I got some chocolate."
    m1 "There is this place that makes the best chocolate I've eaten."
    m1 "Then I also bought some jelly beans and such."
    m1 "And cheese cake."
    a "Uu... Tasty, tasty."
    m1 "Oh, before I forget. Could you go over the contract?"
    a "I can."
    play sound mouse_click_1
    scene 42-2 plane 5 with Dissolve(1)
    m1 "The thing is, they are relying on us to do all the 'heavy' lifting in this."
    m1 "Tombale has a lawyer, but we are the experts in this field, so he is kind of trusting us."
    m1 "I would love it if we didn't do anything to screw them over."
    a "Ah... Well, we will do our best."
    a "Could you go and ask the pilot how long it will take?"
    m1 "Alright."
    scene 42-2 plane 6 with Dissolve(1)
    a "Let's see..."
    a "Ok... That's fine, that's fine too..."
    a "{i}...I think they will be fine with the contract terms...{/i}"
    scene 42-2 plane 7 with Dissolve(1)
    m1 "Uh... It will take some time..."
    m1 "Several hours. Like 8 or something?"
    a "Damn. Ok..."
    scene 42-2 plane 8 with Dissolve(1)
    a "Perhaps I'll take a nap."
    m1 "Yeah, Me too. It will be a long flight."
    a "First gotta finish up with the documents and then..."
    a "You can rest for now."
    m1 "Sure."
    scene black with Dissolve(1)
    "Many hours later..."
    scene 42-2 plane 9 with Dissolve(1)
    a "I think we're landing."
    m1 "Yeah... Should get in our seats."
    a "Alright, see you on the ground."
    scene black with Dissolve(1)
    pause 1
    play music Songbirds
    scene 42-2 plane 10 with Dissolve(1)
    a "So... This is it."
    a "It's pretty hot here."
    m1 "Yeah. I came prepped."
    a "Good. Alright, let's get this show on the road."
    a "He's dressed minimally."
    m1 "Indeed."
    scene 42-2 plane 11 with Dissolve(1)
    tm_1 "Greetings, travelers."
    tm_1 "I'm Initiate Kabe."
    a "Nice to make your acquaintance."
    m1 "Hello, sir."
    scene 42-2 plane 12 with Dissolve(1)
    tm_1 "Do not be distracted by my outfit."
    tm_1 "This is all a part of the tradition."
    tm_1 "I come to greet the travelers."
    scene 42-2 plane 13 with Dissolve(1)
    tm_1 "And to be the chaperone that takes us to the Temple of Safu."
    a "Wow, interesting."
    tm_1 "Come, let's head out."
    a "Alright."
    play sound car_sound1
    scene 42-2 plane 14 with Dissolve(1)
    tm_1 "In the days of the old, the journey was full of turmoil and danger."
    tm_1 "Nowadays, we've adapted to a new approach."
    a "Lucky us, hehe."
    tm_1 "Part of the ritual used to make the journey on foot."
    a "Even more so."
    tm_1 "We will be there within 30 minutes."
    tm_1 "Meanwhile, you can relax and enjoy the safari."
    tm_1 "It's truly a magnificent sight, every morning I wake up."
    a "Indeed."
    tm_1 "I hope you've brought sun protection?"
    m1 "Oh, yes. I did. SPF 50."
    tm_1 "Should work."
    play sound carsound2
    scene black with Dissolve(1)
    scene 42-3 bbc 1 with Dissolve(1)
    tm_1 "We are far no longer, just around this mountain."
    a "Great."
    m1 "I can't wait. I always dreamed of coming to such a place."
    a "Really?"
    m1 "Yeah, it's a lifelong dream, and Anna you've helped me make it true."
    m1 "The safari, the ancient culture and traditions..."
    m1 "Amazing..."
    scene 42-3 bbc 2 with Dissolve(1)
    a "Huh. nice."
    a "Huts?"
    tm_1 "As previously mentioned, do not let appearances fool you."
    tm_1 "Acolyte Obi will explain further."
    scene 42-3 bbc 4 with Dissolve(1)
    tm_2 "Greetings and welcome to the humble village of Da'Anumen."
    tm_2 "As with all other travelers, the tradition states that you must first see the humble beginnings."
    tm_2 "This village, might not be much to the eye, but it holds hundreds if not thousands of years of sacred tradition."
    tm_2 "Where out fathers lived."
    tm_1 "And our fathers, fathers lived."
    tm_2 "Yes!"
    tm_1 "AND, our father, fathers, fathers, fathers lived."
    tm_2 "That's enough, Kabe."
    tm_2 "This specific village houses Acolytes and Initiates of the Temple of Safu."
    a "Very interesting."
    scene 42-3 bbc 5 with Dissolve(1)
    tm_2 "If you would please, I will now take you to the Temple of Safu. Where the rites shall begin."
    tm_2 "Are you ready?"
    a "Oh, yes."
    tm_2 "In that case, let us proceed."
    play music Savannah
    scene 42-3 bbc 6 with Dissolve(1)
    a "Whoa..."
    a "This temple is huge."
    tm_2 "Built by our ancestors."
    tm_2 "As a show of conviction and gratefulness for the gifts Safu has provided."
    tm_2 "One of which you are here today, to discuss."
    a "Ahh... I see..."
    scene 42-3 bbc 7 with Dissolve(1)
    m1 "This is so awesome."
    m1 "I've never been a part of such an experience."
    a "Neither have I, this is pretty cool."
    tm_2 "This way."
    scene 42-3 bbc 8 with Dissolve(1)
    a "Wow."
    m1 "Right?"
    a "The totem..."
    scene 42-3 bbc 9 with Dissolve(1)
    a "I hope the treats you brought will be tasty."
    m1 "Me too..."
    a "This is pretty serious."
    scene 42-3 bbc 10 with Dissolve(1)
    "They all came to the totem and Acolyte Obi with Initiate Kabe both kneeled."
    a "Should we also kneel?"
    m1 "I don't know, I think the book said so."
    scene 42-3 bbc 11 with Dissolve(1)
    tm_3 "Welcome to Temple of Safu."
    tm_3 "Allow me to extend my welcome."
    tm_3 "I am honored to meet you, far-travelers."
    scene 42-3 bbc 12 with Dissolve(1)
    a "Hello, sir. We are also deeply honored to be here."
    m1 "And we are humbled that you have allowed us to enter the Temple."
    a "Indeed."
    tm_3 "As tradition dictates, travellers should also kneel before the Totem of Safu."
    a "Yes, sir."
    scene 42-3 bbc 13 with Dissolve(1)
    "They both kneeled and looked upon the locals."
    scene 42-3 bbc 14 with Dissolve(1)
    tm_3 "All above as all below. The sky so blue, sand so course..."
    tm_3 "Safu, The god of destinies, past and future."
    tm_3 "Welcome these strangers, enjoy their gifts. and shed them of ignorance."
    tm_3 "With your blessing shall they continue!"
    scene 42-3 bbc 15 with Dissolve(1)
    a "Uh... This is a bit weird."
    m1 "Anna, come on. These rites are millennia old."
    a "Yeah... I know..."
    scene 42-3 bbc 16 with Dissolve(1)
    tm_3 "You may get up and present your gifts."
    a "Yes, sir."
    m1 "With pleasure."
    scene 42-3 bbc 17 with Dissolve(1)
    a "We have brought interesting tasty treats from our land."
    a "I hope you and Safu will enjoy them as much as we do."
    tm_3 "Wonderful gift, wonderful indeed."
    scene 42-3 bbc 18 with Dissolve(1)
    tm_3 "Thanks be upon these travelers for gifts given."
    tm_3 "A gift given is a gift that cannot be taken."
    tm_3 "As such, these travelers have shown gratitude and generosity."
    tm_3 "Proof of their conviction."
    scene 42-3 bbc 19 with Dissolve(1)
    tm_3 "You as the leader of your people, Anna, will be taken for the next part of the rites."
    tm_3 "Your friend will join us in a traditional sitting: A Grand Sitting."
    a "Alright, sounds good."
    tm_3 "This lady will lead you to our special baths. Follow her."
    a "Ok."
    scene 42-3 bbc 20 with Dissolve(1)
    m1 "Enjoy, heh."
    m1 "I wish I could have that experience."
    m1 "Getting washed and such... mmhh..."
    a "Madison. Hehe..."
    scene 42-3 bbc 21 with Dissolve(1)
    tm_4 "I'm very honored to be the conduit for Safu's Embrace ritual."
    a "Oh."
    a "It's the bath, right?"
    tm_4 "Indeed."
    play music Endless_Savannah
    scene 42-3 bbc 22 with Dissolve(1)
    tm_4 "Here we are."
    a "Oh, it smells wonderful in here."
    tm_4 "We use local herbs to give the water this wonderful aroma."
    scene 42-3 bbc 23 with Dissolve(1)
    tm_4 "Now, if you could please take off your clothes."
    a "Sorry?"
    tm_4 "I am to wash your body."
    tm_4 "It's a very sacred tradition, to rid you of the dirtiness of the world around."
    scene 42-3 bbc 24 with Dissolve(1)
    tm_4 "It's not only that, Safu provides the water, and embraces you with it, through me."
    tm_4 "A shield, from evil spirits, as well."
    a "Really?"
    tm_4 "Yes my part in this is important."
    a "Ok..."
    play sound undress
    scene 42-3 bbc 25 with Dissolve(1)
    tm_4 "Wonderful."
    tm_4 "You are a very beautiful traveler."
    tm_4 "Indeed might be one of the most beautiful ever."
    tm_4 "There is a legend of the 'Graceful Traveller'."
    a "Really?"
    tm_4 "Indeed, now, please get into the basin."
    scene 42-3 bbc 26 with Dissolve(1)
    a "Can you tell me about the legend?"
    tm_4 "It is not for me to tell."
    tm_4 "I am to wash you and prepare you."
    a "Prepare me?"
    play sound pourwater
    scene 42-3 bbc 27 with Dissolve(1)
    tm_4 "Please, enjoy the water and the aroma."
    tm_4 "Let the worries wash away."
    a "Mh... It does feel nice."
    scene 42-3 bbc 28 with Dissolve(1)
    a "The water also feels soft, and pleasantly refreshing."
    tm_4 "Safu, take the evil spirits away from the body of this traveler."
    tm_4 "Let us rejoice in your gift of water!"
    a "Oh..."
    scene 42-3 bbc 29 with Dissolve(1)
    "Anna deeply relished the ritual."
    "The air smelled wonderful, the water was pure and pleasurable on her body."
    scene 42-3 bbc 30 with Dissolve(1)
    "The soft touches from the lady were delightful..."
    scene 42-3 bbc 31 with Dissolve(1)
    "As the Acolyte said, this short ceremony washed Anna's problems away, even if for a little while."
    play sound pourwater
    scene 42-3 bbc 32 with Dissolve(1)
    a "You are very good at this."
    tm_4 "I've been doing this for as many years as I have been a part of the Temple of Safu."
    a "Oh?"
    a "How long."
    scene 42-3 bbc 33 with Dissolve(1)
    a "Mmmm..."
    "Anna didn't think much of it, but the ritual was supposed to be sensual."
    "And it was, it made her a bit horny..."
    a "Oh..."
    scene 42-3 bbc 34 with Dissolve(1)
    a "Ah..."
    a "Continue please."
    tm_4 "As you wish."
    scene 42-3 bbc 35 with Dissolve(1)
    a "{i}...She is very intimate with me...{/i}"
    a "{i}...Is it a part of the ritual?...{/i}"
    tm_4 "Do you like this?"
    a "Oh yes..."
    scene 42-3 bbc 36 with Dissolve(1)
    tm_4 "And this?"
    a "Yes... Mm..."
    tm_4 "Good..."
    "Anna didn't realize it at first, but the Acolyte was preparing her for something."
    scene 42-3 bbc 37 with Dissolve(1)
    a "Hehe... Is this a part of the ceremony, too?"
    tm_4 "Indeed."
    tm_4 "Of course, we are given some freedom to express. A little bit."
    a "I like your expression."
    scene 42-3 bbc 38 with Dissolve(1)
    tm_4 "I'm glad."
    tm_4 "Don't worry, I will be done soon."
    a "No rush, take your time."
    play sound femmoan_3
    scene 42-3 bbc 39 with Dissolve(1)
    a "Ah..."
    tm_4 "Oh... You seem to be enjoying this a lot."
    a "I... I am, yeah."
    play sound jerk
    scene 42-3 bbc 40 with Dissolve(1)
    tm_4 "Good..."
    a "Mhm..."
    scene 42-3 bbc 41 with Dissolve(1)
    a "Please, don't stop."
    tm_4 "I have to, for now..."
    a "Ah..."
    scene 42-3 bbc 42 with Dissolve(1)
    tm_4 "That is it for the cleansing."
    tm_4 "Now I have a special outfit to help you put on."
    a "Interesting."
    a "What kind of an outfit?"
    scene 42-3 bbc 43 with Dissolve(1)
    tm_4 "It's made of pure gold. It was made several hundred years ago, and has been cleaned and maintained regularly."
    a "Wow. That is impressive."
    tm_4 "Indeed. It's a devoted task throughout generations."
    play sound undress
    scene black with Dissolve(1)
    play sound chain_1
    scene 42-3 bbc 44 with Dissolve(1)
    pause 1.5
    play sound chain_2
    scene 42-3 bbc 45 with Dissolve(1)
    pause 1
    scene 42-3 bbc 46 with Dissolve(1)
    a "Whoa..."
    a "Umm... What exactly are you preparing for me?"
    tm_4 "Don't you know? The final part of the ritual."
    a "I thought there were 4 parts."
    scene 42-3 bbc 47 with Dissolve(1)
    tm_4 "Don't worry too much..."
    tm_4 "You will find out soon enough..."
    "Anna had a weird feeling about it."
    tm_4 "You are ready, please... Go through the door."
    play sound jacketcloth
    scene 42-3 bbc 49 with Dissolve(2)
    a "Huh..."
    scene 42-3 bbc 50 with Dissolve(2)
    tm_5 "Welcome to Copulation of Devotion ritual, traveler."
    scene 42-3 bbc 51 with Dissolve(2.5)
    a "Oh my..."
    play sound deepimpact
    stop music
    scene black
label EP13_Episode_End:
    jump EP14_Begin
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
