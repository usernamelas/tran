transform custom_fade_in:
    alpha 0
    linear 0.5 alpha 1
init python:
    def EP9_Check_Scene_Number():
        global EP9_5_PoolBoyScene_Parameter
        if EP9_5_PoolBoyScene_Parameter >= 4:
            EP9_5_PoolBoyScene_Parameter = 1
        elif EP9_5_PoolBoyScene_Parameter <= 0:
            EP9_5_PoolBoyScene_Parameter = 3
screen PoolBoyScene():
    zorder 301
    frame ('background', None):

        xfill True
        yfill True
        has vbox
        spacing 10
        xalign 1.0
        yalign 1.0
        imagebutton:
            idle im.Scale("images/other/Episode_9.5/PoolBoy/37-9 pool 56.jpg", 200, 113)
            hover im.MatrixColor(im.Scale("images/other/Episode_9.5/PoolBoy/37-9 pool 56.jpg", 200, 113), im.matrix.brightness(0.2))
            focus_mask True
            action [Hide("EP9_5_PoolBoy_DoggyStyle_Screen"), Jump("EP9_5_PoolBoyScene_Missionary")]
        imagebutton:
            idle im.Scale("images/other/Episode_9.5/PoolBoy/37-9 pool 58.jpg", 200, 113)
            hover im.MatrixColor(im.Scale("images/other/Episode_9.5/PoolBoy/37-9 pool 58.jpg", 200, 113), im.matrix.brightness(0.2))
            focus_mask True
            action [Hide("EP9_5_PoolBoy_Missionary_Screen"), Jump("EP9_5_PoolBoyScene_DoggyStyle")]

        button:
            text "Slower" xalign 0.5 yalign 0.5
            idle_background "#000000CC"
            hover_background "#676767CC"
            xsize 200
            ysize 50
            action SetVariable("EP9_5_PoolBoyScene_Speed", 1)
        button:
            text "Faster" xalign 0.5 yalign 0.5
            idle_background "#000000CC"
            hover_background "#676767CC"
            xsize 200
            ysize 50
            action SetVariable("EP9_5_PoolBoyScene_Speed", 2)
        button:
            text "Change View" xalign 0.5 yalign 0.5
            idle_background "#000000CC"
            hover_background "#676767CC"
            xsize 200
            ysize 50
            action [SetVariable("EP9_5_PoolBoyScene_Parameter", EP9_5_PoolBoyScene_Parameter+1),
                EP9_Check_Scene_Number]
        button:
            text "Finish" xalign 0.5
            xsize 200
            idle_background "#000000CC"
            hover_background "#676767CC"
            ysize 50
            action Jump("EP9_5_PoolBoy_2")
screen EP9_5_PoolBoy_Missionary_Screen():
    zorder 300
    if EP9_5_PoolBoyScene_Parameter == 1:
        if EP9_5_PoolBoyScene_Speed == 1:
            add "EP9_5_PoolAnim_3" at custom_fade_in
        if EP9_5_PoolBoyScene_Speed == 2:
            add "EP9_5_PoolAnim_4" at custom_fade_in
    if EP9_5_PoolBoyScene_Parameter == 2:
        if EP9_5_PoolBoyScene_Speed == 1:
            add "EP9_5_PoolAnim_5" at custom_fade_in
        if EP9_5_PoolBoyScene_Speed == 2:
            add "EP9_5_PoolAnim_6" at custom_fade_in
    if EP9_5_PoolBoyScene_Parameter == 3:
        if EP9_5_PoolBoyScene_Speed == 1:
            add "EP9_5_PoolAnim_7" at custom_fade_in
        if EP9_5_PoolBoyScene_Speed == 2:
            add "EP9_5_PoolAnim_8" at custom_fade_in
screen EP9_5_PoolBoy_DoggyStyle_Screen():
    zorder 300
    if EP9_5_PoolBoyScene_Parameter == 1:
        if EP9_5_PoolBoyScene_Speed == 1:
            add "EP9_5_PoolAnim_10" at custom_fade_in
        if EP9_5_PoolBoyScene_Speed == 2:
            add "EP9_5_PoolAnim_9" at custom_fade_in
    if EP9_5_PoolBoyScene_Parameter == 2:
        if EP9_5_PoolBoyScene_Speed == 1:
            add "EP9_5_PoolAnim_11" at custom_fade_in
        if EP9_5_PoolBoyScene_Speed == 2:
            add "EP9_5_PoolAnim_12" at custom_fade_in
    if EP9_5_PoolBoyScene_Parameter == 3:
        if EP9_5_PoolBoyScene_Speed == 1:
            add "EP9_5_PoolAnim_13" at custom_fade_in
        if EP9_5_PoolBoyScene_Speed == 2:
            add "EP9_5_PoolAnim_14" at custom_fade_in
label EP9_5_Scene1_1:
    stop music
    scene 36-9 base16 with flash
    play sound gunsound3
    with vpunch
    pause 1
    scene 36-9 base 17 with Dissolve(1)
    "Anna quickly got up and shot Mr. Smith..."
    play music MovementSong_6
    "He fell to the ground in seconds, screaming out in pain..."
    f2 "AAHH!!!"
    play sound coughing
    f2 "AAAH!!!"
    play sound manpain
    "It was all happening so fast..."
    "But Anna had to react."
    scene 36-9 base 18 with Dissolve(1)
    "Mr. Smith let out one last gasp before succumbing to his wound."
    s1 "God damn, Anna. I didn't know you had it in you..."
    "Anna was frozen, unable to utter a word. Completely overtaken by the fact..."
    "She had just killed someone for the first time."
    s1 "Anna?"
    scene 36-9 base 19 with Dissolve(1):
        linear 50 zoom 1.5
    "She couldn't hear Sergey."
    "Monumental amount of emotions rushed her."
    "Confusion, anger, fear, dread... Instinct..."
    a "{i}...I... I just killed someone..."
    scene 36-9 base 20 with Dissolve(1)
    s1 "He's dead. Damn. If you hadn't intervened, Anna. I would've died..."
    s1 "Probably you and Carl, too. He was reaching for the gun..."
    a "I can't believe it..."
    a "A life gone, just like that..."
    s1 "Come on, you've seen shit like this before."
    a "But... I've..."
    a "I've never killed anyone..."
    a "Never even shot a gun before..."
    s1 "It was either him or you. It wasn't even a choice. You did the right thing."
    a "I... suppose..."
    if EarlHelp == True:
        play sound door2
        play audio surprise
        scene 36-9 base 21 with Dissolve(1)
        earl "Freeze!"
        a "huh?"
        scene 36-9 base 22 with Dissolve(1)
        earl "I got you all now!"
        earl "Drop the gun and move away, slowly."
        play sound item_falls
        scene 36-9 base 23 with Dissolve(1)
        a "I... I did what I had to."
        a "In self-defense!"
        earl "Yeah, yeah. Whatever."
        earl "I know what you criminals do anyway."
        s1 "Right, and you are the good cop, eh?"
        scene 36-9 base 24 with Dissolve(1)
        earl "No. I'm the guy holding the gun against your face."
        s1 "And that makes you the such a big man?"
        earl "Yes! Haha. I can do what I want."
        earl "Surely you don't want to get shot?"
        scene 36-9 base 25 with Dissolve(1)
        earl "Let's see here..."
        earl "Well, well."
        earl "Our departed is yet another scum. Like you."
        earl "Good riddance, I say. Great job, Anna..."
        "She felt the tension in the air. Earl ahead of them this time."
        scene 36-9 base 26 with Dissolve(1)
        s1 "You are just as bad, Earl! I know what you've done."
        s1 "Your actions will come to light."
        s1 "That I'm sure of."
        earl "I'm sure that we all get our due, but I've only done right."
        with vpunch
        earl "By THE BADGE!"
        scene 36-9 base 27 with Dissolve(1)
        earl "I can't say the same thing about you."
        s1 "The feeling's mutual."
        scene 36-9 base 28 with Dissolve(1)
        f1 "Hello?"
        f1 "Officer? I'm being held here against my own will!"
        f1 "These bastards kidnapped me!"
        earl "Oh, shut the fuck up! I know you tried to abduct Anna!"
        scene 36-9 base 27 with Dissolve(1)
        s1 "So that's your game?"
        s1 "Playing all righteous now?"
        s1 "I know what you've done to Anna and how treacherous you are."
        earl "You don't know the half of it, boy!"
        a "I need to check on Carl."
        play sound cloth_sound1
        scene 36-9 base 29 with Dissolve(1)
        a "Carl!"
        earl "Get him up!"
        earl "They will be coming with me."
        scene 36-9 base 30 with Dissolve(1)
        earl "My officers are already on their way."
        earl "We will take care of everything on this side."
        scene 36-9 base 31 with Dissolve(1)
        earl "Now!"
        earl "You and Carl over there are under arrest. You have the right to remain silent."
        earl "Anything you say can and will be held against you in the court of law!"
        earl "You have a right to an attourney, if you can't afford one, state will provide."
        earl "Yeah, yeah. We'll get there."
        scene 36-9 base 32 with Dissolve(1)
        s1 "I won't just give up."
        earl "You won't have a choice. I have enough evidence to put you away for a long time."
        s1 "I've got good lawyers, you will watch me walk, you sack."
        earl "Listen."
        scene 36-9 base 32 with vpunch
        earl "Fuck you!"
        earl "I've gone to big lengths to make sure you don't see the light of day without bars anymore."
        earl "So trust me when I say. Your days, like this, are over."
        with vpunch
        play sound undress
        scene 36-9 base 33 with Dissolve(1)
        earl "It's time to move."
        s1 "No."
        earl "What do you mean no?"
        scene 36-9 base 34 with Dissolve(1)
        earl "Are you hearing this?"
        scene 36-9 base 33 with Dissolve(1)
        earl "Did the dead guy hit you too hard?"
        earl "We can do this the easy way or the hard way."
        earl "Come on."
        scene 36-9 base 74 with Dissolve(1)
        s1 "I prefer the hard way."
        earl "Yeah, you're right. Officer!"
        earl "Clean up this trash!"
        play sound door2
        scene 36-9 base 75 with Dissolve(1)
        cop1 "Yes, sir!"
        s1 "I will find a way to make you pay."
        s1 "And when that day comes, it will come hard!"
        play sound handcuffs
        scene 36-9 base 76 with Dissolve(1)
        earl "Keep thinking."
        earl "I will be happy to see what you come up with."
        earl "You are not as powerful as you think!"
        scene 36-9 base 77 with Dissolve(1)
        "Sergey didn't react to Earl anymore..."
        s1 "Promise me that Anna will stay out of this. She didn't do any of it."
        earl "Sure, sure..."
        s1 "Be safe, Anna..."
        play sound door2
        scene 36-9 base 78 with Dissolve(1)
        earl "Well, well. You were a part of this."
        earl "To be honest. I'm thankful for your help..."
        a "What?"
        earl "Yeah, I couldn't have done it without you."
        a "I can believe my ears. Are you thanking me? After all the blackmail and abuse?"
        earl "Trust me, I had to lean on the weak link, no offense."
        play sound cloth_sound1
        scene 36-9 base 79 with Dissolve(1)
        a "Will you leave me and my sister alone now?"
        earl "You are free to go. I will not put you in the middle of it."
        earl "I will stay behind, collect evidence and clean it all up."
        a "Just like that?"
        earl "Yeah. I will, of course, contact you once more when this is over."
        a "What about Carl?"
        earl "Medics will take care of him."
        scene 36-9 base 80 with Dissolve(1)
        a "Ummm... Alright..."
        earl "Take care, Anna."
        a "..."
        a "Bye."
        $ EP9_var_12 = True
        scene black with Dissolve(1)
        jump EP9_5_Shower_1
    if CarlHelps == True or TaxmanHelps == True:
        scene 36-9 base 20-1 with Dissolve(1)
        "She looked at the gun in disbelief still."
        a "I... I can't."
        s1 "You ok?"
        play sound item_falls
        scene 36-9 base 20-2 with Dissolve(1)
        "Anna dropped the gun and tried to think of something else to focus on."
        a "Carl!"
        a "Is he ok?"
        play sound undress
        scene 36-9 base 29-1 with Dissolve(1)
        a "Carl!"
        a "He's knocked out cold."
        s1 "The man will be ok. He's tough."
        play sound police_arrest
        play audio door2
        scene 36-9 base 35 with Dissolve(1)
        earl "Freeze!"
        earl "You are all under arrest. You have the right to remain silent."
        earl "Anything you say can and will be held against you in the court of law!"
        earl "You have a right to an attorney. If you can't afford one, the state will provide."
        scene 36-9 base 36 with Dissolve(1)
        s1 "Oh. You feel powerful with that gun, eh?"
        s1 "How about you put it down, and we fight like real men."
        earl "Look at you. All bravado. I won't let my pride get in the way."
        earl "I know you would beat the living shit out of me."
        s1 "Oh yeah. I would. YOU KILLED MY BROTHER!"
        scene 36-9 base 35 with Dissolve(1)
        earl "What are you talking about?"
        earl "..."
        earl "Oh. The drug dealer? Alexei?"
        earl "He was a scumbag!"
        scene 36-9 base 36 with Dissolve(1)
        s1 "Don't you dare mention his name!"
        s1 "You destroyed a family that day..."
        scene 36-9 base 36-1 with Dissolve(1)
        a "{i}...Shit..."
        a "{i}...How did he find us..."
        "Anna was looking for a way how to help Sergey."
        s1 "I will have my revenge."
        scene 36-9 base 38 with Dissolve(1)
        a "Fuck it... If I've gone this far..."
        "Anna picked up the gun once more..."
        scene 36-9 base 38-1 with Dissolve(1)
        a "Sergey. Now!"
        earl "What?"
        stop music
        play sound gunsound3
        with vpunch
        pause 0.1
        scene 36-9 base 38-2 with Dissolve(0.2)
        pause 0.2
        play sound gunsound3
        with vpunch
        pause 0.3
        scene 36-9 base 39-1 with Dissolve(0.2)
        pause 0.5
        play sound cockgun
        scene 36-9 base 39-2 with Dissolve(0.2)
        "Earl leaned away to take cover from Anna's gunshots."
        play sound gunsound2
        with vpunch
        "And during that, Sergey shot as well."
        "All of the missed..."
        scene 36-9 base 40 with Dissolve(1)
        earl "Son of a bitch!"
        earl "I will kill you."
        play sound manpain
        play sound gunsound1
        scene 36-9 base 41 with vpunch
        s1 "Ah!"
        "Sergey dodged the bullet, and Earl made his escape."
        play sound door2
        scene 36-9 base 42 with Dissolve(1)
        s1 "Take care of Carl."
        s1 "I've got unfinished business with the asshole."
        a "Be careful!"
        show screen BlackBars
        play sound door2
        play music ChaseSong_1
        scene 36-9 base 43 with Dissolve(1)
        "Sergey knocked the door open."
        s1 "Run, you bastard!"
        scene 36-9 base 44 with Dissolve(1)
        "Sergey aimed the gun at the Detective and..."
        play sound gunsound3
        with vpunch
        scene 36-9 base 45 with Dissolve(1)
        play sound manpain
        earl "AHHHH!"
        "The bullet grazed Earl's shoulder."
        s1 "You won't get away, murderous pig!"
        "Earl was feeling the wrath of Sergey for the first time."
        "For the first time in a very long time, he felt fear..."
        "Like he wasn't in control of the situation."
        play sound carsound3
        scene 36-9 base 46 with Dissolve(1)
        "While stumbling and stuttering around, he quickly got in the car and drove off."
        s1 "Oh, you won't get away..."
        s1 "I WON'T LET YOU!"
        scene 36-9 base 47 with Dissolve(1)
        "Sergey unlocked the car, jumped in, and went straight after Earl."
        "The sirens were wailing. The wheels were squeaking."
        "But the detective could feel the inevitability."
        scene 36-9 base 48 with Dissolve(1)
        "Sergey pressed the pedal to the metal."
        "Rushing after him in his powerful jeep."
        s1 "I'm coming for you, bastard."
        scene 36-9 base 49 with Dissolve(1)
        earl "Fuck, fuck...."
        play sound manpain
        earl "My shoulder!"
        earl "I've got to get away."
        earl "I will get him some other day..."
        play ambient car_fast
        scene 36-9 base 50 with flash
        "A car chase ensued."
        "Both cars were speeding through the empty city streets."
        "But Earl just couldn't shake off Sergey."
        scene 36-9 base 51 with Dissolve(1)
        s1 "{i}...He will get what he deserves. That scumbag!"
        "Sergey felt adrenaline rushing through his body."
        "He could almost move mountains with the sheer power of his anger."
        scene 36-9 base 52 with Dissolve(1)
        earl "Son of a bitch!"
        earl "I won't get killed by some criminal low-life."
        "But it was in fact Earl who was the low-life."
        "His entire life praying on weak women, manipulating people, hurting them..."
        "His end was but inevitable."
        scene 36-9 base 53 with Dissolve(1)
        "Suddenly a transport car came on to the street."
        "The speed of the police vehicle was so fast that the driver had no time to react."
        scene 36-9 base 54 with Dissolve(1)
        "Earl, trying to evade the car and continue driving, made a cardinal error."
        "The speed was too fast, and his car lost traction with the road..."
        play sound car_break
        scene 36-9 base 55 with Dissolve(1)
        pause 2
        scene 36-9 base 56 with Dissolve(1)
        play sound man_scream
        earl "FUUUCKK!!"
        scene 36-9 base 57 with Dissolve(1)
        s1 "Oh fuck..."
        "Sergey slammed on the brakes and witnessed how the detective's car just rolled..."
        stop ambient
        stop music
        play sound car_break
        pause 2
        scene 36-9 base 57-1 with Dissolve(1)
        pause 0.5
        play sound car_crash
        scene black
        pause
        play music MovementSong_5
        play ambient idle_car
        pause 2
        scene 36-9 base 58 with Dissolve(4):
            ease 60 zoom 1.25
        "..."
        play audio coughing
        earl "Ah, shit... Shit..."
        "He was pinned between the ground, the car, and his terrible, terrible decisions..."
        play audio car_door
        play audio footsteps
        scene 36-9 base 59 with Dissolve(1):
            zoom 1.25
            linear 30 xalign 0.5
        "Sergey got out of the car and slowly walked towards the overturned police vehicle."
        "He knew he had won..."
        play ambient fire_burning
        scene 36-9 base 60 with Dissolve(1)
        "The detective's car had caught fire..."
        earl "Fuck... Get me out of here!"
        s1 "..."
        play sound jacketcloth
        scene 36-9 base 61 with Dissolve(1)
        "He leaned down to Earl... Looked him in the eye..."
        earl "You've got to help me..."
        earl "I am one of the good guys!"
        scene 36-9 base 62 with Dissolve(1)
        earl "Please. All I've done, it was to keep the streets safe."
        "Earl believed his conviction till the very end... Regardless of how misguided his actions were."
        s1 "No. The people you hurt, my brother, Anna. Who knows how many other people..."
        scene 36-9 base 63 with Dissolve(1)
        s1 "There is no salvation for you..."
        earl "The fuck you know!"
        earl "I did it all to protect regular folk!"
        scene 36-9 base 64 with Dissolve(1)
        "Sergey didn't say another word and just got up."
        earl "No! Don't!"
        earl "You son of a bitch!"
        earl "You know this isn't right!"
        scene 36-9 base 65 with Dissolve(1)
        earl "Who are you to judge!"
        earl "NOOO!"
        earl "You are no better than I am!"
        play sound manpain
        scene 36-9 base 66 with Dissolve(1)
        pause 2
        play sound car_door
        scene 36-9 base 67 with Dissolve(1)
        "Sergey got into his car and drove off..."
        "As the flames enveloped the car..."
        play sound carsound
        scene 36-9 base 68 with Dissolve(1)
        s1 "No, I'm worse..."
        scene black with Dissolve(4)
        stop ambient fadeout 4
        stop music fadeout 4
        hide screen BlackBars
        pause
        play sound door2
        play music tranquility
        scene 36-9 base 69 with Dissolve(1)
        s1 "Are you guys alright?"
        a "Yeah, we are fine."
        c1 "Except for a bad headache..."
        s1 "Well, it's done with, but now we have to devise a plan."
        scene 36-9 base 70 with Dissolve(1)
        c1 "What exactly happened?"
        s1 "Well, you see that Mr. Smith is dead... I killed detective Mendoza."
        s1 "Now we also have to get rid of Fitzgerald."
        play sound undress
        scene 36-9 base 71 with Dissolve(1)
        c1 "Yeah... This is kind of unfortunate..."
        c1 "Do you have any ideas?"
        f1 "I have an idea. Please release me."
        f1 "I've got money, loads of it, I can give it all to you..."
        scene 36-9 base 72 with Dissolve(1)
        c1 "Silence!"
        s1 "Well. I found out he's been trying to mess with the Albanians from the southside."
        s1 "We could just give him to them to strengthen ties."
        c1 "Albanians? It is prudent that you think this through."
        s1 "I have."
        s1 "Anna, you should go..."
        s1 "Go home, get some sleep. We will need you tomorrow."
        scene 36-9 base 73 with Dissolve(1)
        f1 "NO..."
        f1 "Please don't give me to the Albanians! Please!!!"
        f1 "I've got the money..."
    $ EP9_var_12 = True
    scene black with Dissolve(2)
    jump EP9_5_Shower_1
label EP9_5_Shower_1:
    play music MovementSong_6
    scene 36-10 shower 1 with Dissolve(1)
    a "A shower is what I need."
    play sound jacketcloth
    scene black with Dissolve(1)
    pause 1
    play ambient shower_sound1
    scene 36-10 shower 2 with Dissolve(1)
    a "Ah..."
    "The steaming hot water was washing away Anna's worries."
    scene 36-10 shower 7 with Dissolve(1)
    "But it was barely enough to make her forget the face of her victim."
    "Even though he deserved it..."
    "She still killed someone."
    "Was it for better or for worse..."
    "Anna will have to live with that now."
    scene 36-10 shower 4 with Dissolve(1)
    "Will she become more headstrong or crash even harder..."
    if EarlHelp == True:
        "And the turn of events with the detective..."
        "He thanked Anna. He was sincere..."
        "That was such a twist to her perception of him."
        "Perhaps he did it all just to catch the criminal..."
    stop ambient
    play sound cloth_sound1
    scene 36-10 shower 5 with Dissolve(1)
    a "Ah... I'm tired... I need some sleep."
    scene black with Dissolve(1)
    "Anna put on her clothes."
    $ EP9_5_var_1 = True
    $ EP9_5_var_2 = True
    scene black with Dissolve(1)
    scene 33-0 morning 0 with Dissolve(2)
    pause 0.5
    stop music
    scene black with Dissolve(1)
    pause 1
    play sound interface_sound
    show text "Tuesday morning..." with Dissolve(1)
    pause 1
    scene 37-1 morning 1 with Dissolve(1)
    "Anna was doing her best to keep her mind off of things."
    pause 1
    scene black with Dissolve(1)
    jump EP9_5_Conglomerate_1
label EP9_5_Benjamin_Scene_1:
    stop music
    scene black
    play ambient citytraffic
    scene 36-10 ben 0 with Dissolve(1)
    "Benjamin is on the ground scouring some papers."
    b1 "Bollocks. Where did it go..."
    b1 "I can't find it, ugh..."
    a "Benjamin?"
    scene 36-10 ben 0-1 with Dissolve(1)
    a "Hey!"
    a "What are you doing here?"
    b1 "Tis naught but an old pickle in my jar."
    a "What?"
    b1 "I'm just picking up some of my old stuff from here."
    scene 36-10 ben 0-2 with Dissolve(1)
    b1 "Say, would you be so kind and lend me your beautiful, helping hand?"
    a "Why not. Gotta do my part for the people, right?"
    b1 "Precisely!"
    b1 "Now. On to the matter at hand."
    b1 "Need your help with some boxes."
    play sound give_box
    scene 36-10 ben 0-3 with Dissolve(1)
    b1 "This holds my collection of stamps."
    a "Really?"
    a "I didn't take you for a collector."
    b1 "Just kidding. My porn collection."
    a "Oh."
    scene 36-10 ben 0-4 with Dissolve(1)
    a "Where to now?"
    b1 "Follow my lead, it's not far. We will take the bus to my place. Not far from the shop we met at."
    a "On our way then..."
    a "I really should get a car."
    play sound car_sound1
    scene black with Dissolve(1)
    stop ambient fadeout 2
    pause 2
    play sound door2
    pause 1
    play sound give_box
    play music tranquility
    scene 36-10 ben 1 with Dissolve(1)
    b1 "Well. This is my home."
    a "I'm... Actually impressed."
    a "This is nicer than I thought it would be."
    a "Do you have this place all to yourself?"
    scene 36-10 ben 2 with Dissolve(1)
    b1 "For now. But I will have some roommates."
    b1 "I hope decent folk. I'm trying to get better, move away from the begging and all that."
    b1 "Find a job. I've had situations when those beggars trash the place, and we all get thrown out."
    b1 "So now I'm more careful."
    b1 "Anyway, This is my flat for now."
    scene 36-10 ben 3 with Dissolve(1)
    b1 "Feel at home, the fridge is there if you want anything."
    b1 "Do you want water? soda?"
    a "Soda would be nice."
    scene 36-10 ben 4 with Dissolve(1)
    b1 "Alright. Take a seat on the sofa. I will be with you in a minute."
    b1 "I will also have a drink."
    a "Sure, thanks, Ben."
    play sound jacketcloth
    scene 36-10 ben 5 with Dissolve(1)
    a "{i}...This is better than I expected..."
    a "{i}...He has made an upgrade. I hope it works out for him."
    "Anna was looking around and enjoying the decent flat."
    scene 36-10 ben 6 with Dissolve(1)
    "Her eyes locked on Ben for a while."
    "He was rummaging through the fridge, looking for drinks."
    "She had a certain liking towards him. Besides the smell, he was funny, smart, and thoughtful."
    "Benjamin had been lost in life for a good while, but things could change."
    scene 36-10 ben 7 with Dissolve(1)
    "He had become a man who could yet make a good life for himself."
    scene 36-10 ben 8 with Dissolve(1)
    b1 "Alright. As ordered. A soda."
    b1 "For both of us."
    a "Thank you."
    b1 "I bought them today, in hopes to have some visitors."
    b1 "You are the best outcome!"
    a "Heh."
    play sound jacketcloth
    scene 36-10 ben 9 with Dissolve(1)
    a "How have you settled in?"
    b1 "Exquisitely. I have made strides in cleaning this place up, actually."
    b1 "Went all around the town to find some thrown-away art, some decorum."
    b1 "Even found two unbroken lamps."
    play sound drinkingBeverage
    scene 36-10 ben 10 with Dissolve(1)
    b1 "Besides that, this place was decent enough already."
    a "How much do you pay for this flat?"
    b1 "I've found a good samaritan, the woman gave me a good discount. I only pay 300 dollars for this flat."
    b1 "I had been saving that money for half a year. was rummaging through trash like crazy and trying to find things to sell."
    a "Well, well. That is impressive."
    b1 "Thank you, now I need a decent job, and I will only go up."
    scene 36-10 ben 11 with Dissolve(1)
    a "I think if you go to the shop again, you will get a job as a janitor. That should be enough to cover the cost of this and get you some money for food."
    b1 "I figured that, will go tomorrow."
    b1 "Besides, I'm quite good at finding this, so if I need an extra buck, I can just scavange for things and sell em."
    a "Right."
    $ EP9_5_ben_menu_1 = False
    $ EP9_5_ben_menu_2 = False
    menu EP9_5_Ben_Menu:
        "How did you find out about this place?" if EP9_5_ben_menu_1 == False:
            scene 36-10 ben 12 with Dissolve(1)
            b1 "I was walking by the apartment building and heard an argument."
            b1 "There I am, listening. The landlady tells the tenant that she'd rather choose some bum."
            b1 "Instead of that guy to live in her apartment."
            b1 "So I didn't waste time and went right to her."
            scene 36-10 ben 11 with Dissolve(1)
            a "What she say?"
            b1 "Well..."
            scene 36-10 ben 12 with Dissolve(1)
            b1 "I saw the regret in her face."
            b1 "But she seemed stubborn enough to pick me."
            b1 "It all happened in front of the previous tenant."
            a "Haha!"
            b1 "I promised her, though, that I am getting my act together and I will be a good tenant."
            a "I hope so."
            $ EP9_5_ben_menu_1 = True
            jump EP9_5_Ben_Menu
        "Do you already have any roomates in mind?" if EP9_5_ben_menu_2 == False:
            b1 "Some. But I don't trust any of them to actually consider it."
            b1 "I will have to come up with something."
            b1 "But I think I could manage with a salary from the shop."
            scene 36-10 ben 11 with Dissolve(1)
            a "Indeed. I put in a good word for you."
            a "So if you show up cleaned up and motivated."
            b1 "I know, I know. I will get the job."
            $ EP9_5_ben_menu_2 = True
            jump EP9_5_Ben_Menu
        "That's all.":
            pass
    scene 36-10 ben 12 with Dissolve(1)
    a "I'm actually proud of you, Ben."
    a "I didn't have my hopes up, but this is very nice."
    b1 "Well, you've helped me out plenty. And been good company in the past."
    b1 "You've inspired me to become better."
    scene 36-10 ben 13 with Dissolve(1)
    b1 "A BIGGER personality, if you will."
    a "That's always good."
    scene 36-10 ben 14 with Dissolve(1)
    b1 "Indeed..."
    "Anna had noticed that Benjamin's mind had wandered..."
    "She was alright with letting him stare for a bit."
    play sound surprise
    scene 36-10 ben 15 with Dissolve(1)
    b1 "Anyway..."
    b1 "Where were we."
    a "The weather."
    b1 "Ah, yes. It's quite alright outside today. I spent a good portion of the morning scavanging."
    b1 "Man I love it. You never know what kind of goodies you will find out there in the world."
    scene 36-10 ben 16 with Dissolve(1)
    b1 "Oh! That reminds me!"
    b1 "I found a spare lightbulb. I need to change it, you mind helping me out?"
    a "Sure."
    play music Funny_Song2
    scene 36-10 ben 17 with Dissolve(1)
    a "Is this it?"
    b1 "Precisely. I found the exact lightbulb, like this."
    scene 36-10 ben 18 with Dissolve(1)
    "I wanna change it."
    b1 "Back when I used to live in Balkans... We used to fix everything as soon as we could..."
    a "Uh. You will be able to get up there?"
    b1 "That's what I need your help with."
    b1 "Can you give me a little push?"
    a "Let's do it."
    play sound undress
    scene 36-10 ben 19 with Dissolve(1)
    b1 "Eh. Uh..."
    b1 "Almost..."
    b1 "A bit mooooore...."
    play sound jacketcloth
    scene 36-10 ben 20 with Dissolve(1)
    b1 "There."
    a "You good up there?"
    b1 "Better than ever."
    b1 "This lightbulb has been flickering for three days. Now I will finally have peace."
    a "Heh."
    scene 36-10 ben 21 with Dissolve(1)
    b1 "Can you just hold me?"
    a "Sure."
    b1 "I will be fine, but just in case."
    scene 36-10 ben 22 with Dissolve(1)
    b1 "Alright. Just need to unscrew this and change that."
    b1 "Should only take a minute, don't you worry."
    scene 36-10 ben 23 with Dissolve(1)
    "While Benjamin was focused on the lightbulb..."
    "Anna started to feel something moving in his pants."
    a "Huh?"
    play sound surprise2
    scene 36-10 ben 24 with Dissolve(1)
    b1 "Ah. I'm falling!"
    a "Hold on!"
    play sound jacketcloth
    scene 36-10 ben 25 with Dissolve(1)
    pause 0.5
    play sound woman_surprise
    scene 36-10 ben 26 with Dissolve(1)
    a "Whoops!"
    a "Your pants. They just fell down..."
    scene 36-10 ben 27 with Dissolve(1)
    b1 "Ah shiet. I knew that wearing the wrong size will bite me in the ass..."
    b1 "Umm..."
    a "It's... It's ok. Just finish up."
    b1 "Yeah, I'm about done screwing..."
    b1 "I mean fixing the lightbulb."
    scene 36-10 ben 28 with Dissolve(1)
    "And like always, Anna felt a shift in her attention."
    "She was overcome with an urge to touch Benjamin's cock."
    "Like cocaine, it was calling her."
    play sound surprise
    scene 36-10 ben 29 with Dissolve(1)
    benp "Touch me, Anna... Toouuuuchhh me..."
    "It said..."
    "Anna couldn't handle it. She needs to touch it."
    b1 "Fnh..."
    "Anna started to caress the cock. Benjamin already felt excited."
    scene 36-10 ben 30 with Dissolve(1)
    b1 "Daamn..."
    b1 "{i}...This woman... Is... Is... Ahhh..."
    b1 "{i}...Crazyyyy... Ah... My cock... Her hands..."
    scene 36-10 ben 32 with Dissolve(1)
    b1 "Almost... Almost..."
    b1 "Annnd..."
    play sound ovenbell
    scene 36-10 ben 33 with Dissolve(1)
    b1 "La voila."
    a "NIIICE!"
    scene 36-10 ben 33-1 with Dissolve(1)
    b1 "Wonderful!"
    scene 36-10 ben 34 with Dissolve(1)
    a "Umm... Your cock..."
    a "Well... It also lit up."
    b1 "Sorry, sorry. I will get down in a sec and dress up."
label EP9_5_Benjamin_Scene_Replay:
    play music SexyTimeSong4 fadein 2 fadeout 2
    show EP9_5_Ben_1 with Dissolve(1)
    b1 "AH..."
    show EP9_5_Ben_2 with Dissolve(1)
    hide EP9_5_Ben_1
    pause
    scene 36-10 ben 34 with Dissolve(1)
    pause 1
    hide EP9_5_Ben_2
    play sound lighthit
    scene 36-10 ben 35-1 with vpunch
    a "Ah!"
    b1 "Oof!"
    scene 36-10 ben 35 with Dissolve(1)
    b1 "Sorry, terribly sorry, Anna."
    a "It's ok... I guess, Hah."
    a "Well... Perhaps it's even better."
    play sound surprise
    scene 36-10 ben 36 with Dissolve(1)
    b1 "Huh?"
    b1 "This girl..."
    a "You seem to enjoy yourself."
    a "Your penis doesn't lie."
    scene 36-10 ben 37 with Dissolve(1)
    a "Does it?"
    b1 "No. I don't think so..."
    a "How about I make sure..."
    play sound licking_1
    scene 36-10 ben 38 with Dissolve(1)
    b1 "Hjuuuuhhh...."
    b1 "My oh my..."
    b1 "Woman, you make my feathers unfurl like a peacock!"
    a "Mhmmm."
    play sound jerk2
    scene 36-10 ben 39 with Dissolve(1)
    a "MMmm..."
    "Anna was enjoying the cock more and more."
    "It wasn't even smelly this time."
    a "Mmm..."
    b1 "Tis crazy how I get myself into these situations!"
    play sound licking_2
    scene 36-10 ben 40 with Dissolve(1)
    b1 "Oooaahh..."
    "Anna went deeper..."
    scene 36-10 ben 41 with Dissolve(1)
    play sound jerk3
    show EP9_5_Ben_3 with Dissolve(1)
    pause
    show EP9_5_Ben_4 with Dissolve(1)
    hide EP9_5_Ben_3
    pause
    scene 36-10 ben 42 with Dissolve(1)
    b1 "Hoooaaah!"
    a "Mmmm."
    "She enjoyed the taste of the clean bums dick."
    "And the clean bum loved the things Anna's mouth was doing to him."
    play sound jerk2
    scene 36-10 ben 43 with Dissolve(1)
    a "Mmmh."
    play sound femmoan_4
    a "Ah..."
    "Anna tried to contain her excitement to suck on some cock."
    "But to no avail."
    scene 36-10 ben 44 with Dissolve(1)
    b1 "Sheesh. Your head is miles ahead of anything else."
    b1 "How about we change it up?"
    play sound sucking_1
    scene 36-10 ben 45 with Dissolve(1)
    a "What do you have in mind?"
    "Anna was already too excited to worry about anything else."
    "She didn't see the man. She only saw his cock."
    play sound jacketcloth
    scene 36-10 ben 46 with Dissolve(1)
    b1 "I will lead you. Just let me take control, ok?"
    a "Ok..."
    "Anna liked that ole' Benny was giving her orders."
    b1 "Turn around for me, will ya?"
    scene 36-10 ben 47 with Dissolve(1)
    "She did as he told her."
    "Wondering what he would do next made her more and more excited..."
    play sound surprise
    play audio undress
    scene 36-10 ben 48 with Dissolve(1)
    a "Oh... Heh... Benjamin... What did you lose there?"
    b1 "Hehe... Oh, just something very tasty and sweet."
    b1 "Some cake..."
    play sound woman_surprise
    scene 36-10 ben 49 with Dissolve(1)
    pause 0.5
    play sound undress
    play audio jerk2
    scene 36-10 ben 50 with Dissolve(1)
    b1 "Yes. Tis better than snorting coke out of a hooker's ass!"
    a "Well, Hah. I'm glad you approve."
    b1 "Woman, you have no idea!"
    play sound jacketcloth
    scene 36-10 ben 51 with Dissolve(1)
    b1 "Lemme help you with that, too."
    a "Oh, ok."
    a "Do what you want with me..."
    a "Just, please... Give me that... Thing!"
    play sound cloth_sound1
    scene 36-10 ben 52 with Dissolve(1)
    b1 "Oh, no doubt about that..."
    "Benjamin whispered while fondling Anna's salacious melons."
    b1 "Yes... Wonderful indeed..."
    play sound move_whoosh
    scene 36-10 ben 53 with Dissolve(1)
    "He pushed her back downward revealing her pussy lips to him."
    b1 "Sweet fucks... I didn't think I would get to bang you."
    b1 "Like a dream come true."
    a "Come on, Benny. Don't waste any time, please..."
    a "Give me what I deserve!"
    play sound jerk
    scene 36-10 ben 54 with Dissolve(1)
    "Benjamin moved the tip around Anna's orifice, letting their juices lubricate the entrance."
    "The rock-hard shaft flicking up and down Anna's hole made her body vibrate in lust."
    a "Oh booyyy..."
    b1 "I could say the same thing... Damn..."
    play sound femmoan_1
    scene 36-10 ben 55 with Dissolve(1)
    a "Don't waste any time, Benny."
    b1 "Hyooo!"
    play sound jerk
    scene 36-10 ben 56 with Dissolve(1)
    a "Uuuhhh.. Ohh..."
    "Benjamin swayed back annd..."
    play sound move_whoosh
    scene 36-10 ben 57 with Dissolve(1)
    play sound femmoan_4
    "Thrust into Anna's not-so-tight vagina."
    a "Agh!"
    scene 36-10 ben 58 with Dissolve(1)
    b1 "Lord. Have mercy!"
    b1 "Vagina so good I would give my porn collection away!"
    play sound clappingcheeks
    scene 36-10 ben 59 with Dissolve(1)
    a "Mf. Continue like that."


    play sound femmoan_2
    play audio clappingcheeks
    show EP9_5_Ben_5 with Dissolve(1)
    a "Ahhh..."
    pause
    scene 36-10 ben 60 with Dissolve(1)
    hide EP9_5_Ben_5
    b1 "This is amazing..."
    b1 "The view, the moves. You are one of a kind... What the fuck..."
    a "Ah... Fuck me harder, please!"
    play sound move_whoosh
    scene 36-10 ben 61 with Dissolve(1)
    b1 "You like that, don't you!"
    a "YES! YES!"
    b1 "As Benjamin was fucking her with all his might, Anna felt the cock throbbing in her pussy."
    "She felt the sheer force of his thrust send pleasure throughout her body."
    play sound surprise
    scene 36-10 ben 62 with Dissolve(1)
    "Suddenly Benjamin flipped her on the table."
    b1 "I wanna look at your face when fucking you..."
    a "Ok..."
    a "Anna was too preoccupied with the pleasure to be bothered with the details."
    play sound moaninglong_1
    play audio jerk2
    scene 36-10 ben 63 with Dissolve(1)
    "Waiting not a second longer, Benjamin got right back to it."
    "He pushed his shaft inside of Anna and moved his hips with the same speed he had previously."
    "And Lustful Anna loved every second of it."
    a "This is even better! I love this cock!"
    a "AAHHH!"
    b1 "It feels like your pussy has taken my penis hostage!"
    b1 "It feels like it's sucking it. FUUCCKKK!"
    scene 36-10 ben 64 with Dissolve(1)
    "As if gained strength out of nowhere, Benjamin was fucking like a young dude."
    "With power like non before."
    "Holding her leg up, thrusting, almost, like an animal."
    scene 36-10 ben 65 with Dissolve(1)
    b1 "Ah.. Ah.. Ah.."
    a "I feel my pussy tingle so hard on your thing!!!"
    play sound clappingcheeks
    play audio jerk2
    show EP9_5_Ben_6 with Dissolve(1)
    pause
    play sound moaningfive
    show EP9_5_Ben_7 with Dissolve(1)
    hide EP9_5_Ben_6
    pause
    "Benjamin felt a strong sensation in his penis. A flush of serotonin released in his body..."
    "A surge of pleasure slowly started to build up to an inevitable peak."
    b1 "Ohh... Shiieett... I'm... I can't control it!!!"
    $ AnnaCorruption += 2
    $ corruption_func("Anna Corruption +2")
    menu:
        "Cum inside of Anna's tight pussy.":
            play sound femmoan_3
            scene 36-10 ben 70 with flash
            a "Cum iiinnnn. AHHH!!!"
            b1 "I'm explooodiiiingnggg!!"
            with flash
            play sound licking_1
            scene 36-10 ben 71 with flash
            b1 "Uhh.."
            with flash
            play sound jerk
            scene 36-10 ben 72 with Dissolve(1)
            "Benjamin pulled out after a moment."
            "Anna's pussy was leaking cum."
            scene 36-10 ben 73 with Dissolve(1)
            b1 "Fuck. I'm spent."
            b1 "I need to lie down for a second."
            scene black with Dissolve(1)
            play sound jacketcloth
            pause 1.5
            play sound undress
            pause 1
        "Splash her entire body with your sperm.":
            scene 36-10 ben 66 with flash
            with vpunch
            b1 "Fuuuuuckkkk."
            with flash
            play audio jerk
            "His shaft unloaded a powerful stream of cum all over Anna."
            scene 36-10 ben 66 with flash
            play sound woman_surprise
            a "Ah..."
            scene 36-10 ben 67 with flash
            b1 "Oh... I'm terribly sorry, Anna."
            a "Umm... It's. Alright."
            scene 36-10 ben 68 with Dissolve(1)
            a "I will just go and clean up then."
            b1 "Definitely, I have some wet towels in the bathroom."
            scene black with Dissolve(1)
            play sound jacketcloth
            pause 1.5
            play sound undress
            pause 1
    $ renpy.end_replay()
    scene 36-10 ben 76 with Dissolve(1)
    b1 "I'm left without words."
    a "Umm. Me, too. I don't know why I do these things..."
    b1 "Perhaps you just like it?"
    b1 "Nothing wrong with enjoying yourself. Especially with an older, more experienced gentlemen."
    a "Right..."
    b1 "Anyway. Maybe you would like to come by in the future again?"
    a "Perhaps."
    scene 36-10 ben 77 with Dissolve(1)
    a "If you behave, heh."
    b1 "From here on out, I'm going to be a model citizen."
    b1 "Stop by whenever."
    $ EP9_5_var_4 = True
    $ persistent.scene_27 = True
    scene black with Dissolve(1)
    if DilanPornShootQuestDone == True:
        jump EP9_5_Dilan_1
    else:
        jump EP9_5_Michael_1
label EP9_5_Dilan_1:
    stop music
    play music Chill_Song_1
    play sound door2
    play audio surprise
    scene 37-3 dilan 1 with Dissolve(1)
    d3 "Ah. Anna!"
    d3 "Welcome, welcome. Make yourself at home."
    scene 37-3 dilan 2 with Dissolve(1)
    d3 "Can I get you anything?"
    a "No, no. Thanks."
    d3 "Well, on to business, then."
    d3 "Let's sit."
    play sound cloth_sound1
    scene 37-3 dilan 3 with Dissolve(1)
    d3 "How you've been?"
    a "I'm alright. Plenty of crazy stuff happening in life right now."
    d3 "I can imagine."
    d3 "Did I tell you about that one time when I was filming a porno in a mansion..."
    d3 "And the owners came home... I mean, I thought the young guy who rented it out to us was the owner."
    d3 "They threatened to call the police, so we just bailed."
    d3 "The porn-star girl forgot her clothes, so we ended up shooting a public exposure porno."
    d3 "Great times... Hah..."
    $ EP9_5_dilan_menu_1 = False
    $ EP9_5_dilan_menu_2 = False
    $ EP9_5_dilan_menu_3 = False
    menu EP9_5_Dilan_Menu:
        "How is the porn industry treating you?" if EP9_5_dilan_menu_1 == False:
            scene 37-3 dilan 6 with Dissolve(1)
            d3 "There are some ups and downs."
            d3 "But, generally, the requests keep flooding in."
            d3 "And the more I establish my name in the industry, the more opportunities I get."
            d3 "People seem to like my content. No doubt you have something to do with it, too."
            scene 37-3 dilan 3 with Dissolve(1)
            a "Thank you. Heh."
            $ EP9_5_dilan_menu_1 = True
            jump EP9_5_Dilan_Menu
        "How did you end up becoming a porn filmmaker?" if EP9_5_dilan_menu_2 == False:
            scene 37-3 dilan 6 with Dissolve(1)
            d3 "Well, it all started when I was studying to become a carpenter."
            d3 "Lemme tell you, not what I wanted to do, but my parents were old-fashioned."
            d3 "Didn't approve of anything else other than getting a profession like that."
            scene 37-3 dilan 3 with Dissolve(1)
            a "What changed?"
            d3 "One day, I was walking through my campus and overheard some sex noises."
            d3 "In one of the second-floor dorm rooms."
            scene 37-3 dilan 6 with Dissolve(1)
            d3 "Went to investigate. Saw a young stud fucking a young girl. Something like 18."
            d3 "One of the cameramen got sick suddenly and had to run to the bathroom."
            d3 "He kicked the door open, ran out, and the director noticed me, and because the dude was about to nut..."
            d3 "In the heat of the moment he just took me and told me to film."
            d3 "Girl, I was natural!"
            scene 37-3 dilan 3 with Dissolve(1)
            a "Wow..."
            d3 "The rest is history. around 15 years of that."
            d3 "Then I decided to do something more regular and started my photography studio."
            d3 "Nowadays, I only accept special porn requests, and you are a special one, for sure."
            a "Don't make me blush... Heh."
            $ EP9_5_dilan_menu_2 = True
            jump EP9_5_Dilan_Menu
        "What you do in your free time?" if EP9_5_dilan_menu_3 == False:
            scene 37-3 dilan 6 with Dissolve(1)
            d3 "Free time?"
            d3 "Don't know the meaning of the word."
            d3 "After I finish film and photo shoots, I edit them."
            d3 "After a long day of work, I usually sit back and chill, get a beer."
            d3 "This work is pretty much my life."
            d3 "I'm just so fascinated by getting the next perfect picture or video."
            scene 37-3 dilan 3 with Dissolve(1)
            a "Really nothing outside of work?"
            d3 "Wel,l I occasionally go, and play pool at the local bar."
            scene 37-3 dilan 6 with Dissolve(1)
            d3 "Remember, we shot a threesome porno there."
            a "Riight..."
            $ EP9_5_dilan_menu_3 = True
            jump EP9_5_Dilan_Menu
        "That's all.":
            pass
    d3 "On to business then?"
    scene 37-3 dilan 4 with Dissolve(1)
    if escort_industry_var == True:
        play sound notification
        $ renpy.notify("+10,000 $")
        $ MoneyVar += 10000
        d3 "Here is your 10,000 $ cut."
        d3 "Glad to do business with you."
    if porn_industry_var == True:
        play sound notification
        $ renpy.notify("+5,000 $")
        $ MoneyVar += 5000
        d3 "Here is your 5,000 $ cut."
        d3 "Glad to do business with you."
    scene 37-3 dilan 5 with Dissolve(1)
    a "Oh. Haha."
    a "Thank you kindly."
    d3 "No. Thank you, Anna."
    d3 "You bring in this. All you, truly."
    d3 "And that brings me to my next point."
    scene 37-3 dilan 6 with Dissolve(1)
    d3 "Question. Do you wanna continue this arrangement?"
    d3 "Cause I have some very eager clients."
    menu:
        "Yes, Anna wants to do porn but also is interested in escort work.":
            scene 37-3 dilan 7 with Dissolve(1)
            a "I would like to participate in both escorts and porn videos."
            d3 "I thought you might say that. I cannot give you money for both as we discussed after the shoot."
            d3 "But I can still get you in contact with interested parties."
            a "That sounds great."
            $ AnnaCorruption += 2
            $ corruption_func("Anna Corruption +2")
            $ escort_industry_var = True
            $ porn_industry_var = True
            jump EP9_5_Dilan_1_Both
        "Yes, Anna wishes to have fun and earn money.":
            scene 37-3 dilan 7 with Dissolve(1)
            a "I think so. This is really decent money..."
            a "Plus, I kind of like what I do..."
            d3 "That's my girl. I'm glad to hear it."
            $ AnnaCorruption += 2
            $ corruption_func("Anna Corruption +2")
        "No, Anna doesn't want to participate anymore.":
            scene 37-3 dilan 7 with Dissolve(1)
            a "Ah. No. I've had my 'fun' I think I need to stop doing this."
            d3 "Oh, well. You know where to find me. If that's your final answer."
            a "I think so..."
            jump EP9_5_Dilan_2
    d3 "Alright, then."
    if escort_industry_var == True:
        d3 "I have a client. He's very, very influential."
        d3 "He received the raw version of our shoot and has also seen your previous work."
        d3 "That would be an escort job for you."
        scene 37-3 dilan 8 with Dissolve(1)
        a "Oh. If I recall correctly, that was my choice before, I see."
        d3 "Would you be interested?"
        a "Yeah. I'm down to see what this man has in mind."
        d3 "Great, I will make the call."
        scene black with Dissolve(1)
        "Some time later..."
        scene 37-3 dilan 7 with Dissolve(1)
        d3 "Wonderful news. He's available and waiting."
        a "Ok, should I prepare some outfit and go to him?"
        d3 "No. No. You will be picked up by a personal driver outside of my place."
        a "Wow. Ok, good to know."
        d3 "I will contact you with further details, unless you guys make a deal of your own..."
        a "Bye for now."
        scene black with Dissolve(1)
        jump EP9_5_Escort_1
    if porn_industry_var == True:
        d3 "So, your porn film got kind of popular."
        d3 "I would almost say, that you should make a social media presence so that people get to know you."
        a "I will keep that in mind."
        d3 "Anyway, I've got a lot of good feedback and have come up with two ideas for brand new films."
        scene 37-3 dilan 8 with Dissolve(1)
        a "Oh?"
        d3 "Yeah. One is more vanilla, more established, and the other one is more fetishized and experimental. But it's your choice which one to make."
        d3 "There isn't much difference in pay, so it's up to your preference."
        a "I see."
        play sound jacketcloth
        scene 37-3 dilan 9 with Dissolve(1)
        d3 "I've made first covers for the films."
        d3 "One is a BDSM and domination-focused film. It will have a bit different tact compared to your previous films."
        d3 "And the other is a simple, good old-fashioned interracial film. Jeff will star in it, so the chemistry will definitely be there."
        a "I see."
        scene 37-3 dilan 11 with Dissolve(1)
        pause 1
        scene 37-3 dilan 12 with Dissolve(1)
        pause 0.5
        menu:
            "Old Pool Boy Jeff.":
                $ EP9_5_porn_2 = True
                jump EP9_5_Dilan_2
            "Harsh Treatment.":
                $ EP9_5_porn_1 = True
                jump EP9_5_Dilan_2
        pause
label EP9_5_Dilan_1_Both:
    if escort_industry_var == True and porn_industry_var == True:
        d3 "I have a client. He's very, very influential."
        d3 "He received the raw version of our shoot and has also seen your previous work."
        d3 "That would be an escort job for you."
        scene 37-3 dilan 8 with Dissolve(1)
        a "Oh. I see."
        d3 "Would you be interested?"
        a "Yeah. I'm down to see what this man has in mind."
        d3 "Great, I will make the call."
        scene black with Dissolve(1)
        "Some time later..."
        scene 37-3 dilan 7 with Dissolve(1)
        d3 "Wonderful news. He's available and waiting."
        a "Ok, should I prepare some outfit and go to him?"
        d3 "No. No. You will be picked up by a personal driver outside of my place."
        a "Wow. Ok, good to know."
        d3 "Also, ask him to drop you off back at my place after your meeting."
        d3 "We will continue with the porn shoot after that, alright?"
        a "Yeah, got it."
        jump EP9_5_Escort_1
label EP9_5_Dilan_1_Both_2:
    stop ambient
    play sound walk
    scene black with Dissolve(1)
    pause 2
    play sound door2
    scene 37-3 dilan 7 with Dissolve(1)
    d3 "Alright, you're back!"
    d3 "On to our other 'business'"
    d3 "So, your porn film got kind of popular."
    d3 "I would almost say that you should make a social media presence so that people get to know you."
    a "I will keep that in mind."
    d3 "Anyway, I've got a lot of good feedback and have come up with two ideas for brand new films."
    scene 37-3 dilan 8 with Dissolve(1)
    a "Oh?"
    d3 "Yeah. One is more vanilla, more established, and the other one is more fetishized and experimental. But it's your choice which one to make."
    d3 "There isn't much difference in pay, so it's up to your preference."
    a "I see."
    play sound jacketcloth
    scene 37-3 dilan 9 with Dissolve(1)
    d3 "I've made first covers for the films."
    d3 "One is a BDSM and domination-focused film. It will have a bit different tact compared to your previous films."
    d3 "And the other is a simple, good old-fashioned interracial film. Jeff will star in it, so the chemistry will definitely be there."
    a "I see."
    scene 37-3 dilan 11 with Dissolve(1)
    pause 1
    scene 37-3 dilan 12 with Dissolve(1)
    pause 0.5
    menu:
        "Old Pool Boy Jeff.":
            $ EP9_5_porn_2 = True
            jump EP9_5_Dilan_2
        "Harsh Treatment.":
            $ EP9_5_porn_1 = True
            jump EP9_5_Dilan_2
    pause
label EP9_5_Dilan_2:
    if EP9_5_porn_1 == True:
        scene 37-3 dilan 12 with Dissolve(1)
        a "Harsh Treatment..."
        d3 "Great choice, indeed."
        scene 37-3 dilan 13-1 with Dissolve(1)
        d3 "Let's do it!"
        scene black with Dissolve(1)
        jump EP10_HarshTreatment
    if EP9_5_porn_2 == True:
        scene 37-3 dilan 11 with Dissolve(1)
        a "Old Pool Boy Jeff."
        d3 "Wonderful choice!"
        scene 37-3 dilan 13 with Dissolve(1)
        d3 "Alright then. We can begin when ever you are ready!"
        a "I'm ready."
        d3 "Then let's go to the shooting set."
        jump EP9_5_PoolBoy_1
    play sound move_whoosh
    scene 37-3 dilan 14 with Dissolve(1)
    a "Thanks for your help, Dilan."
    d3 "No problem. Take care!"
    $ EP9_5_var_5 = True
    scene black with Dissolve(2)
    play sound walk
    jump EP9_5_Michael_1
label EP9_5_PoolBoy_1:
    play sound carsound3
    scene black with Dissolve(1)
    pause 1
    define PoolBoy_Scene_Music = ["audio/sounds/SexyTimeSong4.mp3", "audio/sounds/By The Pool.mp3", "audio/sounds/SexyTimeSong3.mp3"]
    $ renpy.random.shuffle(PoolBoy_Scene_Music)
    play music PoolBoy_Scene_Music
    scene 37-8 pool 1 with Dissolve(1)
    a "Whoa."
    a "This place seems so nice."
    d3 "I couldn't agree more."
    d3 "I looked for a good place."
    play ambient pool_ambient
    scene 37-8 pool 2 with Dissolve(1)
    a "How much did it cost to rent out?"
    d3 "Oh, that isn't important..."
    d3 "What is crucial, is that you get to enjoy yourself in a good work environment."
    scene 37-8 pool 3 with Dissolve(1)
    a "Dilan, you are such a sweetheart."
    d3 "No need to fret. It's all my pleasure."
    a "But still, this is so nice."
    d3 "If we continue working together, you will get to see some crazy mansions and condos."
    scene 37-8 pool 4 with Dissolve(1)
    d3 "Perhaps even find some 'love' with the owners, hah."
    a "Maybe, I'm not getting my hopes up."
    a "Even though I like the money and the sex, someone who loves me for who I am, not what my ass looks like..."
    a "That would be nice."
    d3 "Of course, tomorrow. But for today, we focus on your juicy cheeks!"
    a "Yes, sir! Haha."
    play sound move_whoosh
    scene 37-8 pool 5 with Dissolve(1)
    j2 "Did someone say juicy cheeks?"
    a "Jeff!"
    d3 "There you are."
    scene 37-8 pool 6 with Dissolve(1)
    j2 "How are you two doing on this fine day."
    a "Even better now! Hah."
    d3 "Great, great. Glad that Anna joined us."
    j2 "You can say that again."
    play sound kisspeck
    scene 37-8 pool 7 with Dissolve(1)
    d3 "Oh. Wow."
    a "Mm..."
    j2 "Mhm..."
    play sound licking_1
    scene 37-8 pool 8 with Dissolve(1)
    pause 2
    play audio smooch
    scene 37-8 pool 9 with Dissolve(1)
    d3 "Alright, alright."
    d3 "That's enough, you dirty pervs!"
    d3 "Let's get to work, shall we?"
    d3 "The dressing room is that way. I've got outfits picked out already."
    scene 37-8 pool 10 with Dissolve(1)
    j2 "Nice place. I'm impressed."
    a "Yeah. Dilan seems to up the game every time we do this."
    j2 "No doubt about it."
    j2 "When he's working with the best, meaning you and me..."
    j2 "You know the rest."
    play sound jacketcloth
    scene 37-8 pool 11 with Dissolve(1)
    a "Well..."
    a "Get naked, mister."
    play sound undress
    scene 37-8 pool 12 with Dissolve(1)
    "He didn't hesitate one bit."
    a "Well, well."
    a "Some views never get old."
    j2 "Let me tell you."
    j2 "The day you get bored of it is the day I quit my career."
    a "Soo... Never? Hah..."
    play sound undress
    scene 37-8 pool 13 with flash:
        zoom 1.25
        easein 30 xalign 0.5
    pause 5
    scene 37-8 pool 14 with Dissolve(1):
        xalign 0.5
        zoom 1.25
        easein 30 xalign 0.0
    a "Oh, no. We're both naked..."
    a "I wonder what two naked adults could do for fun?"
    j2 "Let's find out?"
    scene 37-8 pool 15 with Dissolve(1)
    a "Hehe... Well, not yet!"
    j2 "You tease... I love it... This will be awesome!"
    play sound jacketcloth
    scene 37-8 pool 16 with Dissolve(1)
    a "You look, usually dashing."
    scene 37-9 pool 17 with Dissolve(1)
    j2 "Khem... Thanks."
    j2 "You are... Well... Who am I kidding!"
    j2 "You're fucking hot. Ha!"
    j2 "Anyway, let's get to it?"
    a "Let's do it, Sweety."
    scene 37-9 pool 18 with Dissolve(1)
    d3 "You guys took your damn time."
    d3 "Alright, you look really good in that."
    d3 "Perfectly fitting my imagination!"
    play sound move_whoosh
    scene 37-9 pool 19 with Dissolve(1)
    d3 "Well. Even better."
    d3 "But enough about that!"
    scene 37-9 pool 20 with Dissolve(1)
    d3 "Could you just get on that chair for me, please?"
    d3 "Don't think about any emotions right now, just enjoy the sun."
    a "Ok. Thanks."
    play sound cloth_sound1
    scene 37-9 pool 21 with Dissolve(1)
    d3 "Perfect."
    a "This is so nice."
    a "I could chill here all day!"
    d3 "I bet."
    scene 37-9 pool 22 with Dissolve(1)
    d3 "Alriight."
    d3 "Keep looking good for me."
    play sound takephoto
    with flash
    d3 "Just like that!"
    scene 37-9 pool 23 with Dissolve(1)
    play sound takephoto
    with flash
    d3 "Very niiice."
    a "Is all ok?"
    d3 "It's perfect!"
    d3 "Just relax. Enjoy the sun."
    scene 37-9 pool 24 with Dissolve(1)
    d3 "A couple more..."
    d3 "I'm starting to film now..."
    d3 "Alright."
    scene 37-9 pool 25 with Dissolve(1)
    d3 "Jeff!"
    d3 "You ready?"
    j2 "As I will ever be!"
    d3 "Good!"
    scene 37-9 pool 26 with Dissolve(1)
    "Dilan aimed the camera, leveled the frame."
    d3 "Alright. Great. Come."
    scene 37-9 pool 27 with Dissolve(1)
    "Anna, our gorgeous Miss World 2010-2015 who is married to a rich oil magnate, lays down for a good sunbathing session..."
    "But it is interrupted by a timely arrival of our trusty cleaner Jeff."
    "At first, she's surprised and unhappy..."
    "Her session would be ruined by some cleaner guy..."
    scene 37-9 pool 28 with Dissolve(1)
    "But the man seemed nice."
    j2 "Hello, miss."
    j2 "Sorry for the intrusion. Your husband asked if I could clean the pool today."
    j2 "You are having guests over later this evening?"
    a "Oh. Yes. Thank you, mister."
    scene 37-9 pool 29 with Dissolve(1)
    a "{i}...He seems alright... Well..."
    a "{i}...And... I haven't had any in a couple of days..."
    a "{i}...My hubby seems to not care about my needs..."
    scene 37-9 pool 31 with Dissolve(1)
    j2 "Say... Aren't you the girl that won the Miss World title five years in a row?"
    a "That's right. After that, I retired because my dear hubby proposed to me."
    j2 "Nice... Nice..."
    play sound surprise
    scene 37-9 pool 32 with Dissolve(1)
    a "Indeed..."
    "Jeff looked at Anna. She had spread her legs a bit."
    "Teasing the poor man."
    scene 37-9 pool 33 with Dissolve(1)
    j2 "Smoking fire."
    j2 "I mean, I should get back to it."
    a "I hope it's ok if I take my top off. I wanted to get a bit of a tan today."
    j2 "Umm... Yeah... Huhhg."
    scene black with Dissolve(0.5)
    play sound jacketcloth
    scene 37-9 pool 34 with Dissolve(0.5)
    "Jeff continued to work. Humming a familiar song."
    a "You know, that song reminds me of good ole days?"
    j2 "You mean the one I was humming?"
    a "Yeah."
    play sound surprise2
    scene 37-9 pool 35 with Dissolve(1)
    j2 "Goddamn!"
    a "You seem surprised."
    a "Never seen female breasts?"
    j2 "You joke, but you are literally the most beautiful female in the world, professionally."
    j2 "I'm just... Surprised you'd take it off with strangers around."
    scene 37-9 pool 37 with Dissolve(1)
    a "Even though I look beautiful... And perhaps even innocent..."
    a "I'm anything but..."
    j2 "{b}*Gulp*{/b}"
    a "You like what you see?"
    play sound move_whoosh
    scene 37-9 pool 38 with Dissolve(1)
    j2 "I do indeed."
    j2 "Are they real?"
    a "Yes... They are. Hehe."
    j2 "Damn..."
    a "How about you massage my legs a bit?"
    j2 "I'm a simple cleaner, but it's never too late to change professions."
    a "That's right, honey!"
    play sound femgasp
    scene 37-9 pool 39 with Dissolve(1)
    a "Oh. That's so nice. Your hands feel very pleasurable on my skin..."
    a "I have to say. I get very 'excited' when I haven't had attention in some time..."
    j2 "Uuhh... Heheh...."
    "Jeff was nervous and excited..."
    "This girl. This absolute stunner, 10/10 model was bare tits in front of him."
    "Could life get any better..."
    scene 37-9 pool 40 with Dissolve(1)
    "Moving his hands up Anna's succulent body. Jeff was still in disbelief of what was unfolding."
    a "Mmm... Your hands feel so perfect touching my skin."
    a "Do you do this often?"
    j2 "I wish I did it more, with you..."
    play sound jacketcloth
    scene 37-9 pool 41 with Dissolve(1)
    j2 "Oh... Would you look at that..."
    a "Do you like when young girls reveal themselves to you?"
    j2 "Absolutely... Do you... Like older men?"
    a "Definitely..."
    scene 37-9 pool 42 with Dissolve(1)
    "She was showing off more and more of her inviting hole."
    "The trophy wife wanted sex, and she would get it."
    "Pool boy Jeff would make sure of it."
    scene 37-9 pool 43 with Dissolve(1)
    "He slid his fingers across her thighs and right around the pussy entrance, feeling the moist, excited opening."
    "He did not touch it, though. Just slid his fingers around it."
    "That made the naughty wife go wild."
    play sound jerk2
    scene 37-9 pool 44 with Dissolve(1)
    pause 1.5
    play sound femgasp
    scene 37-9 pool 45 with Dissolve(1)
    pause 1.5
    a "Oh..."
    j2 "Looks like you're enjoying yourself..."
    play sound femmoan_2
    scene 37-9 pool 46 with Dissolve(1)
    a "Mmm..."
    pause 1
    scene 37-9 pool 47 with Dissolve(1)
    a "Well, well."
    a "That bulge is giving me ideas."
    a "Get rid of those pants!"
    play sound undress
    scene 37-9 pool 48 with Dissolve(1)
    pause 1
    scene 37-9 pool 49 with Dissolve(1)
    a "Wow. It's so biig..."
    a "Well now I'm glad I came out here to sunbathe..."
    j2 "Hah. Trust me, size isn't the only thing I've got."
    scene 37-9 pool 50 with Dissolve(1)
    a "Really?"
    a "I got some tricks up my sleeve, too."
    a "Wanna see?"
    j2 "If ever said no... Shoot me."
    play sound licking_1
    scene 37-9 pool 51 with Dissolve(1)
    "Keeping direct eye contact with Jeff, Anna started to suck him off."
    "Slowly at first, then increasing the pace more and more."
    play sound jerk2
    show EP9_5_PoolAnim_1 with Dissolve(1)
    j2 "Ah..."
    pause
    play sound smooch
    show EP9_5_PoolAnim_2 with Dissolve(1)
    hide EP9_5_PoolAnim_1
    a "Mhmmm..."
    "Anna always enjoyed a hard cock in her mouth."
    play sound kisspeck
    scene 37-9 pool 52 with Dissolve(1)
    hide EP9_5_PoolAnim_2
    a "How about you give your employer's wife a good fucking?"
    j2 "Don't mind if I do. Hah!"
    play sound undress
    scene 37-9 pool 54 with Dissolve(1)
    a "I can't wait..."
    j2 "That crazy for some cock, huh?"
    a "Yeah..."
    $ EP9_5_menu_item_1 = False
    $ EP9_5_menu_item_2 = False
    $ EP9_5_position_var = 0
    menu:
        "Give Anna some love in classic missionary.":
            jump EP9_5_PoolBoyScene_Missionary
        "Flip her on all fours and doggystyle that Asshole!":
            jump EP9_5_PoolBoyScene_DoggyStyle
label EP9_5_PoolBoyScene_Missionary:
    scene black
    $ EP9_5_position_var = 1
    if EP9_5_menu_item_2 == False:
        play sound cloth_sound1
        scene 37-9 pool 55 with Dissolve(1)
        j2 "Allow me to slip right in, then."
        j2 "You made it all good and slipper with your mouth."
        a "That was the idea. Plus, I like cock in my mouth..."
        j2 "You freak, I love it."
        play sound move_whoosh
        scene 37-9 pool 56 with Dissolve(1)
        pause 1.5
        play sound femmoan_4
        scene 37-9 pool 57 with Dissolve(1)
        "Jeff waited a bit and slowly started to slide it in."
        "Anna felt the pussy stretching..."
    $ EP9_5_menu_item_2 = True
    play ambient moaninglong_1
    play audio jerk2
    scene black with Dissolve(0.5)
    show screen PoolBoyScene
    show screen EP9_5_PoolBoy_Missionary_Screen with Dissolve(0.5)
    a "AH!"
    a "Keep fucking that tight pussy!"
    j2 "Yeah? You love to fuck dudes behind your hubby's back?"
    a "AH. Yeah!"
    j2 "Stroke my cock with your vagina!"
    "Anna was entering blissful numbness. Nothing else was around her, only the cock fucking her sensitive pussy."
    pause
    pause
    jump EP9_5_PoolBoy_2
label EP9_5_PoolBoyScene_DoggyStyle:
    scene black
    $ EP9_5_position_var = 2
    if EP9_5_menu_item_1 == False:
        stop ambient
        play sound move_whoosh
        scene 37-9 pool 58 with Dissolve(1)
        a "Oh. Haha."
        j2 "I wanna give your backside some lovin."
        a "Oh... My god!"
        a "I love it!"
        scene 37-9 pool 59 with Dissolve(1)
        a "Please, please don't make me wait!"
        j2 "I won't. Just enjoying the view for a second."
        play sound cloth_sound1
        scene 37-9 pool 60 with Dissolve(1)
        pause 1.5
        play audio jerk2
        play sound femmoan_3
        scene 37-9 pool 61 with Dissolve(1)
        pause 2
        $ EP9_5_PoolBoyScene_Parameter = 1
    $ EP9_5_menu_item_1 = True
    play ambient moaninglong_1
    scene black with Dissolve(0.5)
    show screen PoolBoyScene
    show screen EP9_5_PoolBoy_DoggyStyle_Screen with Dissolve(0.5)
    a "Aahh... That dick..."
    j2 "Yeah? It feels good in your ass, doesn't it?"
    a "YES!"
    a "Give it to me, aaah!"
    "Clapping cheeks and moaning could be heard throughout the room."
    pause
    pause
label EP9_5_PoolBoy_2:
    play ambient moaning_1
    if EP9_5_position_var == 1:
        menu:
            "Cum in Anna's vagina.":
                play sound jerk3
                scene black
                with flash_vpunch
                pause 0.5
                with flash_vpunch
                a "OHHHH!! HMMFFFF!!"
                hide screen PoolBoyScene
                hide screen EP9_5_PoolBoy_Missionary_Screen
                scene 37-9 pool 57-1 with Dissolve(1)
                pause 1
                scene 37-9 pool 57-2 with flash_vpunch
                a "AAAHHHH!!!!"
                j2 "FUCK!"
                scene 37-9 pool 57-3 with Dissolve(1)
                stop ambient
            "Cum on her beautiful body.":
                play sound jerk3
                scene black
                with flash_vpunch
                pause 0.5
                with flash_vpunch
                a "OHHHH!! HMMFFFF!!"
                hide screen PoolBoyScene
                hide screen EP9_5_PoolBoy_Missionary_Screen
                scene 37-9 pool 57-1 with Dissolve(1)
                pause 1
                scene 37-9 pool 57-2 with Dissolve(1)
                a "Cum all over me!"
                j2 "FUCK!"
                scene 37-9 pool 57-4 with flash_vpunch
                j2 "AAAHHH!!"
                scene 37-9 pool 57-5 with Dissolve(1)
                pause 5
                stop ambient
    if EP9_5_position_var == 2:
        menu:
            "Fill up all of Anna's tight asshole.":
                play sound jerk3
                scene black
                with flash
                j2 "I'm spunk you up!"
                a "Ah. Fill meee!"
                hide screen PoolBoyScene
                hide screen EP9_5_PoolBoy_DoggyStyle_Screen
                scene 37-9 pool 63 with Dissolve(1)
                pause 1
                scene 37-9 pool 64 with Dissolve(1)
                j2 "Oh. Shiet!"
                with flash
                scene 37-9 pool 65 with flash_vpunch
                j2 "AHH!"
                a "OHAA!"
                play sound jerk2
                stop ambient
                scene 37-9 pool 66-1 with Dissolve(1)
                "Anna touched her backside and felt gushes of cum escaping the now-stretched, hole."
                j2 "Damn. That ass is tight. Does your hubby use it?"
                scene 37-9 pool 66 with Dissolve(1)
                a "No. Not at all..."
                a "I've been wanting to do it..."
            "Cover her back with Jeff sperm!":
                play sound jerk3
                play audio woman_surprise
                hide screen PoolBoyScene
                hide screen EP9_5_PoolBoy_DoggyStyle_Screen
                scene 37-9 pool 63-1 with flash_vpunch
                j2 "SHIET!"
                a "OH!"
                stop ambient
                scene 37-9 pool 64-1 with Dissolve(1)
                j2 "All covered!"
                a "Nice..."
    $ persistent.scene_28 = True
    $ renpy.end_replay()
label EP9_5_PoolBoy_3:
    scene 37-9 pool 67 with Dissolve(1)
    a "Well. My hubby doesn't please my pussy as good as you..."
    j2 "I'm glad to hear it."
    a "This could be our little secret. What do you say?"
    j2 "Yes, ma'am."
    scene 37-9 pool 68 with Dissolve(1)
    a "I would like to enjoy your company in the future, again..."
    j2 "Likewise..."
    d3 "AAANND CUT!"
    scene 37-9 pool 69 with flash
    d3 "Great work, both of you!"
    d3 "I'm as satisfied as you both! Hah."
    d3 "You did well. I love the excitement and the pleasure."
    scene black with Dissolve(1)
    "Anna cleaned up..."
    scene 37-9 pool 70 with Dissolve(1)
    d3 "Alright you guys. I can literally pay you right now."
    d3 "This was a client request from a bigger porn company."
    d3 "They've been outsourcing the work to me for some while now and the budget gets paid upfront."
    a "That's good to know."
    j2 "Indeed."
    scene 37-9 pool 71 with Dissolve(1)
    d3 "So, here is your pay."
    play sound notification
    $ renpy.notify("+8,500 $")
    $ MoneyVar += 8500
    a "Thanks."
    d3 "Also, both of you, keep an eye out for jobs."
    d3 "I will have more work for you soon."
    d3 "I'm also thinking of setting up a little computer, and you can just come by my place and check it for new jobs."
    d3 "It's not ready yet, but basically you will be able to check on the computer for new films and choose from a list."
    a "Great to know! Keep me posted."
    $ EP9_5_var_5 = True
    play sound walk
    scene 37-9 pool 72 with Dissolve(1)
    a "{i}...I liked the acting..."
    a "{i}...I almost felt like I was the girl in the story... It's kind of exciting..."
    "Anna was left with something to think about."
    pause 1.5
    scene black with Dissolve(1)
    if EP10_var_8 == False:
        jump EP9_5_Michael_1
    else:
        jump EP10_Bath
label EP9_5_Escort_1:
    play ambient citytraffic
    scene 37-4 escort 1 with Dissolve(1)
    "When Anna exited the building, the chauffeur was already waiting."
    di "Anna?"
    a "Alex?"
    di "The world's small, eh?"
    scene 37-4 escort 2 with Dissolve(1)
    a "Ain't that the truth."
    a "I thought you only worked for our company."
    di "Well, no. I work for a company that handles it."
    di "But I'm also privately employed by Mr. Burnsfield."
    a "Well, well."
    scene 37-4 escort 3 with Dissolve(1)
    a "Thanks."
    stop ambient
    play sound carsound3
    scene black with Dissolve(1)
    pause 2.5
    scene 37-4 escort 4 with Dissolve(1)
    a "Damn. This house looks huge."
    a "I wonder if the man is old or not..."
    scene 37-4 escort 5 with Dissolve(1)
    di "Alright, this is your stop."
    a "Thank you, Alex."
    scene 37-4 escort 6 with Dissolve(1)
    di "Take care!"
    di "Whatever your business is with him..."
    di "Be professional. He is a bit old-fashioned."
    a "Will do."
    play sound door2
    play sound surprise
    play music SexyTimeSong4
    scene 37-4 escort 7-1 with Dissolve(1)
    "Anna saw a good-looking man with a great posture and a fire in his eyes..."
    "She immediately took a liking to him. He seemed sincere and genuine."
    "But if he was pure... He wouldn't require escort services."
    mb1 "Welcome, Anna."
    a "Hello."
    mb1 "I hope you're doing well?"
    scene 37-4 escort 8-1 with Dissolve(1)
    a "I am doing alright."
    mb1 "It's great to finally meet you in person."
    mb1 "I've seen your work before."
    a "Umm..."
    mb1 "With Shingzhou? And other companies. Your help was key to securing those deals, right?"
    a "Oh. That, haha. Yeah, thank you."
    scene 37-4 escort 9-1 with Dissolve(1)
    mb1 "Where are my manners? Come in, please."
    a "Alright."
    scene black with Dissolve(1)
    "They immediately went to his home office."
    play sound door2
    scene 37-4 escort 10-1 with Dissolve(1)
    mb1 "I will show you around the mansion more in the future."
    a "Take your time. I'm patient."
    mb1 "Indeed."
    scene 37-4 escort 11-1 with Dissolve(1)
    mb1 "Anyway, it has come to my attention that you are also good at other 'things'"
    mb1 "And so I got in contact with some of our cities talent outreach."
    mb1 "That lead me to you."
    mb1 "You see, I have certain 'tastes' and you could help me with that."
    a "I hope I can."
    scene 37-4 escort 12 with Dissolve(1)
    mb1 "We shall see..."
    scene 37-4 escort 13 with Dissolve(1)
    mb1 "By the looks of it, we will get along just nicely."
    mb1 "But it's not only about the looks, but it's about the actions and passion as well."
    a "I know what you mean."
    scene 37-4 escort 14 with Dissolve(1)
    mb1 "We will have sort of a... Test."
    mb1 "I will evaluate if you fit my criteria."
    a "Oh..."
    "Anna had never been a part of such a 'professional' arrangement."
    scene 37-4 escort 15 with Dissolve(1)
    a "I will do my best to fulfill your expectations."
    mb1 "I hope so, too."
    scene 37-4 escort 16 with Dissolve(1)
    mb1 "I've prepared an outfit for you if you wish to see it."
    a "An outfit?"
    mb1 "Yes. Had my butler pick it up from Bella's Secret the other day."
    a "Wow..."
    "Bella's Secret was one of most renowned female lingerie lines."
    "Their outfits cost on average 50,000 - 70,000 $."
    scene 37-4 escort 17 with Dissolve(1)
    a "I don't know what to say."
    mb1 "No need to say anything. Try it on and see how it feels."
    scene 37-4 escort 18 with Dissolve(1)
    mb1 "I will go get something to drink while you change."
    a "Alright."
    play sound door2
    scene 37-4 escort 19 with Dissolve(1)
    "Anna seemed to be lost in thought."
    "This man wasn't at all what he seemed."
    "Very sophisticated, well-mannered."
    a "Let's get to it."
    scene 37-4 escort 20 with Dissolve(1)
    a "I wonder if he has other girls like this..."
    a "But an outfit from Bella's Secret..."
    a "That is just nuts. They are expensive as hell."
    play sound jacketcloth
    scene 37-4 escort 21 with Dissolve(1)
    pause 1
    play sound give_box
    scene 37-4 escort 22 with Dissolve(1)
    a "What do we have here."
    a "Damn..."
    play sound undress
    scene black with Dissolve(1)
    pause 1.5
    play sound cloth_sound1
    scene 37-4 escort 23 with Dissolve(1)
    a "It fits like a glow."
    a "I wonder if Dilan told him my measurements."
    a "The cloth seems so fine and comfy."
    a "But 50k for this?"
    a "Seems like an overkill..."
    a "Who am I to judge, though..."
    scene 37-4 escort 25 with Dissolve(1)
    mb1 "Very nice indeed..."
    play sound surprise
    scene 37-4 escort 24 with vpunch
    a "I didn't know you were here."
    mb1 "Well, to be honest, I sneaked in, hah."
    a "It's ok."
    mb1 "I've got to say, It looks like I imagined. I have vivid fantasies. It's pretty simple."
    mb1 "And I like it! A lot."
    scene 37-4 escort 26 with Dissolve(1)
    a "So what would you like me to do?"
    mb1 "It's not all finely cut as you'd think. I will require some effort on your part."
    a "What do you mean?"
    play sound cloth_sound1
    scene 37-4 escort 27 with Dissolve(1)
    mb1 "It's a maids outfit, so... We'll start there."
    scene 37-4 escort 28 with Dissolve(1)
    a "Oh. No problem."
    scene 37-4 escort 27 with Dissolve(1)
    mb1 "Great. I have some things to do anyway."
    a "I will get to it then."
    play sound cleaning_sound1
    scene 37-4 escort 29 with Dissolve(1)
    "Anna got to it."
    "Dusting the surfaces all the while Mr. Burnsfield was looking at her."
    a "Hm... Hm... Mhm..."
    "Anna was humming to herself as she was cleaning."
    scene 37-4 escort 30 with Dissolve(1)
    "The view was exquisite."
    mb1 "Very nice..."
    "Mr. Bursnfield was enjoying the view and working parallel."
    play sound cloth_sound1
    scene 37-4 escort 31 with Dissolve(1)
    "The room was quiet. Anna thought that she could easily be a personal maid for someone as powerful..."
    "And if he wanted to take advantage of her... She wouldn't mind."
    scene 37-4 escort 32 with Dissolve(1)
    "She looked with a sexily at the man."
    scene 37-4 escort 33 with Dissolve(1)
    "Her butt cheeks exposed just like that."
    a "Is this good, Mr. Bursnfield?"
    mb1 "Very, just keep going."
    play sound move_whoosh
    scene 37-4 escort 34 with Dissolve(1)
    "She was slowly closing the gap between her and the man."
    "Trying to leave a good impression. It would be good to have friends in high places."
    play sound cleaning_sound1
    scene 37-4 escort 35 with Dissolve(1)
    a "{i}...I could move closer to him. Tease him a little..."
    a "{i}...I wonder if he'd enjoy it..."
    scene 37-4 escort 36 with Dissolve(1)
    a "Excuse me, I think I should also clean your table..."
    mb1 "By all means."
    mb1 "Don't let me stop you."
    scene 37-4 escort 37 with Dissolve(1)
    a "Thanks, could you move a bit?"
    mb1 "Of course."
    scene 37-4 escort 37-1 with Dissolve(1)
    mb1 "Is this far enough?"
    a "Yeah. I think I have enough room."
    mb1 "Alright. I will sit back and wait a moment."
    a "I will be quick."
    scene 37-4 escort 37-2 with Dissolve(1)
    mb1 "Not too quick, I hope."
    mb1 "The view is marvelous."
    a "Thank you, Mr."
    scene 37-4 escort 38 with Dissolve(1)
    a "I would also like to clean under the table if you don't mind."
    mb1 "Go right ahead. The cleaner, the better."
    a "You read my mind."
    play sound cloth_sound1
    scene 37-4 escort 39 with Dissolve(1)
    "Anna got on all fours and seductively moved under the table."
    a "I will be down there just a second."
    a "I'm really good with my hands and on all fours."
    mb1 "I can only imagine. Hah."
    scene 37-4 escort 40 with Dissolve(1)
    "As Anna was slowly sliding deeper under the table..."
    "Mr. Burnsfield was holding his composure."
    "He was getting a tingling sensation. Excitement was building up."
    "But he liked to tease himself. Not get it at first."
    scene 37-4 escort 41 with Dissolve(1)
    a "Am I doing ok, sir?"
    mb1 "You are doing perfectly."
    a "Thank you."
    scene 37-4 escort 42 with Dissolve(1)
    mb1 "Uh..."
    mb1 "Alright..."
    mb1 "I think it's all clean now, isn't it?"
    a "Yeah, I believe so."
    play sound move_whoosh
    scene 37-4 escort 43 with Dissolve(1)
    mb1 "Well, Anna."
    mb1 "After this, you will have to come again."
    mb1 "I need such an effective maid as yourself."
    a "So did I do well?"
    scene black with Dissolve(1)
    play sound undress
    pause 1
    scene 37-4 escort 44 with Dissolve(1)
    mb1 "I would be lying if I said it was anything other than perfect."
    a "Thank you, sir."
    mb1 "I will get your contact info and call you."
    scene 37-4 escort 45 with Dissolve(1)
    mb1 "We will set up a schedule for our... Arrangement."
    mb1 "You will be free to come by whenever and clean, and we can go further."
    a "I'm glad to hear it."
    mb1 "Also, I've got a little bonus for you."
    play sound notification
    $ renpy.notify("+3,000 $")
    $ MoneyVar += 3000
    pause 1.5
    play sound door2
    scene 37-4 escort 46 with Dissolve(1)
    mb1 "I'm glad I got to meet you."
    a "Me too."
    mb1 "I anticipate our further dealings a lot now."
    mb1 "I have some interesting things to show you."
    a "I've got something up my sleeve as well."
    scene 37-4 escort 47 with Dissolve(1)
    mb1 "now you've got me even more interested."
    a "Good. Heh."
    mb1 "..."
    mb1 "I like you."
    mb1 "Anyway. I will contact you with further details soon."
    a "Alright."
    scene 37-4 escort 48 with Dissolve(1)
    mb1 "It was very nice to meet you."
    mb1 "I look forward to seeing you soon."
    a "Likewise, Mr. Burnsfield. Take care."
    mb1 "You too, Anna. You too."
    play sound carsound3
    scene 37-4 escort 49 with Dissolve(1)
    di "Well, How did it go?"
    a "I got the job!"
    di "Nice. Congratulations!"
    a "Thank you, Alex."
    di "Where to?"
    a "Just drop me off in the center."
    play ambient citytraffic
    play sound carsound2
    scene 37-4 escort 50 with Dissolve(1)
    di "Well, this is you."
    a "Thank you."
    di "Have a good day, ma'am."
    a "Thank you, bye!"
    if escort_industry_var == True and porn_industry_var == True:
        jump EP9_5_Dilan_1_Both_2
    $ EP9_5_var_5 = True
    jump EP9_5_Michael_1
label EP9_5_Conglomerate_1:
    play music SpeedBumpsSong
    scene generic office 1 with Dissolve(1)
    "Anna sat down at the computer and prepared for the online meeting."
    a "Alright... All the documents are ready."
    a "I should make the call."
    play sound phonecall
    scene black with Dissolve(1)
    scene 37-5 annacall 4 with Dissolve(1)
    a "Oh. Hello!"
    cr10 "Salam, Anna!"
    cr11 "Hello!"
    a "So, today's call is to go over anything that you would still like to discuss regarding the contract."
    a "Before we I fly over to you, and we have the signing."
    scene 37-5 annacall 1 with Dissolve(1)
    cr10 "Wonderful, I like this."
    scene 37-5 annacall 6 with Dissolve(1)
    cr10 "So. Yeah. We looked over the documents your assistant sent to us, and it's mostly good."
    cr10 "We have an issue with the fact that the contract doesn't seem to cover logistics services."
    scene 37-5 annacall 3 with Dissolve(1)
    a "I see. It's all perfectly reasonable. We have a good list of companies that can secure fast and effective service."
    a "I didn't included on the assumption that you might have your own logistics coverage."
    cr10 "No problem at all! We would like to use local services as they are more likely to have greater experience."
    a "Alright. That's settled, then. I will make the amendment, send the new documents and then we can move on to the next phase."
    cr10 "By the way. This might sound unprofessional, but you are the most beautiful representative that we've ever seen."
    play sound surprise
    scene 37-5 annacall 7 with Dissolve(1)
    a "Oh. Haha. Thanks!"
    a "I always like to hear a nice compliment."
    cr10 "As you should. You should be showered in compliments."
    scene 37-5 annacall 8 with Dissolve(1)
    cr11 "She is so hot... Dammnn..."
    cr10 "Stay calm, my friend."
    cr10 "All is well."
    cr10 "We look forward to meeting you, Anna."
    scene 37-5 annacall 10 with Dissolve(1)
    "Anna had a thought..."
    "She looked around the office."
    a "Well..."
    menu:
        "Show them something...":
            $ AnnaCorruption += 1
            $ corruption_func("Anna Corruption +1")
            play sound undress
            scene 37-5 annacall 11 with Dissolve(1)
            a "Here is a something little bit fun for you guys."
            a "I'm getting a bit hot in my office."
            cr10 "Whaaaa."
            scene 37-5 annacall 12 with Dissolve(1)
            cr10 "Amaziiing."
            cr11 "Wow!"
            play sound jacketcloth
            scene 37-5 annacall 14 with Dissolve(1)
            pause 1.5
            play sound cloth_sound1
            scene 37-5 annacall 15 with Dissolve(1)
            pause 2
            a "Do you like it?"
            a "Perhaps I should get even closer..."
            scene 37-5 annacall 16 with Dissolve(1)
            pause
            play sound surprise
            scene 37-5 annacall 18 with Dissolve(1)
            pause
            scene 37-5 annacall 17 with Dissolve(1)
            cr10 "Damn!"
            cr11 "You crazy woman!"
            play sound surprise
            scene 37-5 annacall 19 with Dissolve(1)
            a "Whoops, sorry. Someone is coming. I have to cover up..."
            a "I hope you liked a little bit of my 'presentation'"
            cr10 "Wooow. Yes."
            cr11 "We look forward to meeting you in real life..."
            a "It will be great, I promise."
            pass
        "Do not get carried away.":
            pass
    scene 37-5 annacall 20 with Dissolve(1)
    a "Well, that's all from me. Then I have a green light to come and visit you?"
    cr10 "Yes!"
    cr10 "We will be waiting for you with anticipation!"
    a "Alright, then, take care. My assistant will send you the amended documents."
    a "Bye!"
    scene 37-5 annacall 21 with Dissolve(1)
    cr10 "Bye, miss!"
    pause 1
    scene 37-5 annacall 22 with Dissolve(1)
    cr10 "YEAH!"
    cr11 "She is one crazy woman. I love it when the western girls do this!"
    cr10 "This will be so much fun, my friend."
    scene 37-5 annacall 25 with Dissolve(1)
    a "Alright, I should go to Madison and discuss this."
    scene black with Dissolve(1)
    "Anna spends some time working and wraps up some additional tasks..."
    $ EP9_5_var_6 = True
    jump EP9_5_Conglomerate_2
label EP9_5_Conglomerate_2:
    scene 31-3 jeremy 11 with Dissolve(1)
    a "Hey Madison!"
    m1 "Anna. So good to see you!"
    m1 "How did the meeting with EOC go?"
    a "It was pretty smooth actually."
    a "However, they want to include Logistics planning and services in the contract."
    a "They will outsource that, too."
    scene 31-3 jeremy 6 with Dissolve(1)
    m1 "Alright. I've got some papers already prepped for that."
    a "Well done."
    a "So yeah. go in the contract and redo that part. The proof read the entire page again."
    m1 "Will do, boss!"
    scene 31-3 jeremy 11 with Dissolve(1)
    a "Right."
    $ EP9_5_conglomerate_menu_var_1 = False
    $ EP9_5_conglomerate_menu_var_2 = False
    menu EP9_5_conglomerate_menu:
        "How have you been doing with work in general?" if EP9_5_conglomerate_menu_var_1 == False:
            m1 "It's been doable."
            m1 "Still picking up new things."
            m1 "Been trying to get to know my colleagues a bit more."
            m1 "Had a coffee sit down with Timothy the other day."
            if jeremySexContent == True:
                m1 "Jeremy is a... Pain in the ass."
                a "Tell me about it."
            m1 "Other than that, pretty solid."
            $ EP9_5_conglomerate_menu_var_1 = True
            jump EP9_5_conglomerate_menu
        "What about you free time? Still playing those novels?" if EP9_5_conglomerate_menu_var_2 == False:
            m1 "Yeah!"
            m1 "That game I told you about before?"
            m1 "It's getting spicier and spicier, some drama going down..."
            a "{i}...Almost sounds like my life..."
            m1 "Been digging at some other ones, too, but nothing quite hits like that one."
            a "Nice. Maybe you should show it to me some day?"
            m1 "Why not."
            $ EP9_5_conglomerate_menu_var_2 = True
            jump EP9_5_conglomerate_menu
        "That's all.":
            pass
    scene 31-3 jeremy 12 with Dissolve(1)
    a "Alright. I think that's all."
    a "I will leave you to it."
    m1 "Alright, Anna. Take care!"
    a "Catch ya later."
    $ EP9_5_var_8 = True
    if BenjaminContent == True:
        jump EP9_5_Benjamin_Scene_1
    else:
        if DilanPornShootQuestDone == True:
            jump EP9_5_Dilan_1
        else:
            jump EP9_5_Michael_1
label EP9_5_Michael_1:
    play music tranquility
    play sound door2
    scene 37-2 michael 1 with Dissolve(1)
    "There he was. Sleeping..."
    "Michael was alive, fortunately. But the wound was heavy, and recovery would take a while."
    a "Hey..."
    scene 37-2 michael 2 with Dissolve(1)
    r1 "Hey, Anna."
    r1 "I didn't expect to see you here."
    a "Well, I had to check up on Michael."
    r1 "Of course."
    scene 37-2 michael 3 with Dissolve(1)
    a "How is he?"
    r1 "He's strong. Their doctor comes around every day to check up on him and administer some drugs."
    r1 "He says the wound is serious, but he should get through it with enough care and attention."
    r1 "So that's what I'm doing mostly right now."
    a "I see."
    scene 37-2 michael 4 with Dissolve(1)
    a "I hope he recovers soon."
    r1 "Me, too."
    a "He is strong. I believe it."
    scene 37-2 michael 5 with Dissolve(1)
    r1 "That's for sure."
    r1 "But enough dwelling on that."
    r1 "How about we talk about something else?"
    r1 "This has been keeping me up all the time."
    play sound surprise
    scene 37-2 michael 6 with Dissolve(1)
    m2 "Huh."
    play sound coughing
    m2 "Shit."
    play sound move_whoosh
    scene 37-2 michael 7 with Dissolve(1)
    pause 2
    scene 37-2 michael 8 with Dissolve(1)
    m2 "Anna, what are you doing here?"
    a "Came to check up on you."
    m2 "Thanks. I appreciate."
    m2 "How are things?"
    if EarlHelp == True:
        a "We will talk about it later, ok?"
        a "Some things went down..."
        m2 "You've got to tell me?"
        a "I will when you get better."
    if TaxmanHelps == True or CarlHelps == True:
        a "Um... Mr. Smith is dead..."
        a "..."
        a "And the detective is dead too."
        m2 "Good riddance, I say! We're back on track."
        a "The guys decided to lay low for a moment."
        a "I will probably have to take a more active part in the business."
        m2 "That's good to hear."
    scene 37-2 michael 9 with Dissolve(1)
    a "Enough about that."
    a "How about we focus on you getting better."
    m2 "Yeah, yeah."
    scene 37-2 michael 10 with Dissolve(1)
    "He felt Anna's hand on his lap..."
    "It made wonders happen, as always."
    m2 "Huh..."
    scene 37-2 michael 11 with Dissolve(1)
    a "How are you feeling in general?"
    m2 "The doctor keeps giving me pain medication, so I don't feel much when I'm doing a minimum amount of movement."
    m2 "When I try to get up or something, it hurts like a bitch."
    a "I can only imagine..."
    play sound surprise
    scene 37-2 michael 13 with Dissolve(1)
    "Anna's hands had risen another fallen soldier."
    m2 "Umm..."
    r1 "Hey, there..."
    scene 37-2 michael 14 with Dissolve(1)
    a "Eh. Looks like someone got excited. Hehe."
    m2 "I think I'm good. Hah."
    scene 37-2 michael 15 with Dissolve(1)
    r1 "You will be better..."
    r1 "This will be as good as the medicine your doctor gives you."
    m2 "Damn, Rebecca."
    m2 "I'm barely alive, and you're givin me a handy."
    m2 "Now that's what's up!"
    play sound jerk
    show EP9_5_MichaelAnim_1 with Dissolve(1)
    pause
    show EP9_5_MichaelAnim_2 with Dissolve(1)
    hide EP9_5_MichaelAnim_1
    pause
    m2 "Mmm..."
    m2 "Nice..."
    scene 37-2 michael 16 with Dissolve(1)
    hide EP9_5_MichaelAnim_2
    r1 "You deserve the best care in the world."
    r1 "You've helped in times of need..."
    scene 37-2 michael 17 with Dissolve(1)
    menu:
        "Anna felt it necessary to please Michael":
            $ AnnaCorruption +=1
            $ corruption_func("Anna Corruption +1")
            a "Yes. So, just sit back and relax..."
            a "We will do the rest..."
            r1 "Oh, Anna. You freaky girl."
            play sound jerk2
            scene 37-2 michael 18 with Dissolve(1)
            m2 "Nice..."
            "Slow strokes that Anna did felt magical to Michael."
            "Both of the girls were massaging his long shaft."
            "Thing's couldn't get better."
            scene 37-2 michael 19 with Dissolve(1)
            a "You like when we stroke your cock like this?"
            a "Double the attention?"
            m2 "Yes... Yeah!"
            play sound jerk2
            show EP9_5_MichaelAnim_3 with Dissolve(1)
            pause
            m2 "Shit..."
            m2 "This feels unreal!"
            a "I bet it does, big boy!"
            show EP9_5_MichaelAnim_4 with Dissolve(1)
            hide EP9_5_MichaelAnim_3
            pause
            m2 "Damn... I'm getting close with you two massaging my entire length."
            a "Come when ever you want, baby."
            a "It will relieve the pain."
            scene 37-2 michael 20 with Dissolve(1)
            m2 "Ah."
            m2 "Daamn."
            play sound licking_1
            scene 37-2 michael 21 with Dissolve(1)
            r1 "I want some of that good cream."
            m2 "What the fuck! Damn!"
            m2 "You girls are freaks! I love it!"
            r1 "Come here."
            play sound jerk3
            scene 37-2 michael 22 with Dissolve(1)
            with flash_vpunch
            m2 "AAH!"
            m2 "My dick is about to explode!"
            scene 37-2 michael 23 with flash_vpunch
            m2 "AAHHHH!"
            r1 "Mmmm..."
            m2 "Damn. Finish in your mouth had never felt so good."
            $ config.menu_include_disabled = True
            scene 37-2 michael 24 with Dissolve(1)
            menu:
                "Kiss Rebecca on the her cum filled mouth. (IF Corruption > 35)" if AnnaCorruption > 35:
                    $ AnnaCorruption += 1
                    $ corruption_func("Anna Corruption +1")
                    scene 37-2 michael 25 with Dissolve(1)
                    "Anna slowly leaned in..."
                    "And..."
                    play sound smooch
                    scene 37-2 michael 26 with Dissolve(1)
                    "Kissed her..."
                    "While Michael was watching."
                    "In disbelief of these two freaky women."
                    m2 "DAAAAAAAAMN!"
                    play sound licking_2
                    scene 37-2 michael 27 with Dissolve(1)
                    a "Mm..."
                    m2 "You girls!"
                    m2 "Are the best."
                    scene black with Dissolve(1)
                    pause 0.5
                    scene 37-2 michael 28 with Dissolve(1)
                    "Rebecca cleaned up."
                    a "Well..."
                    a "I will get going then..."
                    scene 37-2 michael 29 with Dissolve(1)
                    a "It was... Good to see you guys..."
                    "Anna was in a bit of shock at what she had just done."
                    a "See you guys around."
                    m2 "Take care Anna."
                    r1 "Bye, sweety."
                    scene 37-2 michael 30 with Dissolve(1)
                    a "What..."
                    a "Uh..."
                    scene black with Dissolve(1)
                "Don't kiss her on her lips":
                    scene 37-2 michael 28 with Dissolve(1)
                    "Rebecca cleaned up."
                    scene 37-2 michael 11 with Dissolve(1)
                    a "I hope you get better soon, Michael..."
                    m2 "Thanks, Anna. I appreciate you coming to check up on me."
                    a "Take care, guys!"
                    r1 "By sweety, be careful in these crazy times."
        "Well I think it's time to get going.":
            scene 37-2 michael 11 with Dissolve(1)
            a "I hope you get better soon, Michael..."
            m2 "Thanks, Anna. I appreciate you coming to check up on me."
            a "Take care, guys!"
            r1 "By sweety, be careful in these crazy times."
    $ EP9_5_var_7 = True
    jump EP9_5_Version_End
label EP9_5_Version_End:
    scene black with Dissolve(1)
    jump EP10_Alfred_Shop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
