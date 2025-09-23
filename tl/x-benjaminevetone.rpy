label BenjaminEventOne:
    scene black
    scene 32-15 shop 1 with Dissolve(1)
    "Anna enters the shop, it's already late, and the shop is about to close."
    sk "Hey hon, how may I help you?"
    a "Hey, I would like to get some strong alcohol..."
    a "Perhaps a good but inexpensive whiskey?"
    sk "I think I've got what you need."
    scene 32-15 shop 2 with Dissolve(1)
    sk "A little party never hurt anybody, right?"
    a "Yeah... Haha..."
    a "Just need some to unwind..."
    sk "Buying for yourself or for someone else, too?"
    menu:
        "A friend, a good person.":
            sk "Oh... Those are important, indeed."
            a "He seems so."
        "Oh, just returning the favor.":
            sk "Oh, That's nice."
            a "Yeah, He kind of deserves it."
            sk "Huh..."
    scene 32-15 shop 3 with Dissolve(1)
    sk "Alright, that will be 29.99$"
    a "Here you go."
    sk "Thank you. Have a nice evening..."
    a "Thank you."
    scene black with Dissolve(1)
    jump BenjaminEventOneTwo
label BenjaminEventOneTwo:
    $ renpy.music.play("audio/sounds/Purple Planet Music Rendezvous.mp3", fadein = 0.5, loop=True)
    play sound walk
    scene black with Dissolve(1)
    scene 32-16 hob 1-1 with Dissolve(1)
    "Anna enters the alleyway, a bit concerned as to what she might expect..."
    "Hopefully, just good ole' Ben."
    "She was reluctant to continue on, but she had promised Benjamin to visit him."
    "And she could get some useful intel out of him about Earl..."
    a "{i}...I hope I won't regret buying this whiskey bottle."
    scene 32-16 hob 2 with Dissolve(1)
    "Anna moved further into the smelly, dirty path."
    a "{i}...Ben seems nice enough of a bum. I don't know how I feel about consorting with such people..."
    a "{i}...But, then again, what makes me any better... Just circumstances... Right?"
    "Anna pondered about her life's choices for a moment..."
    play sound surprise
    scene 32-16 hob 3 with Dissolve(1)
    "There he was..."
    "Sitting in the dimly lit area of the famous bar."
    "Smoking a cigarette, that he would convince you, he didn't find in a dumpster or ask a stranger."
    b1 "I suppose... I could just make a racket in front of the bar. Maybe they will get me something to drink."
    "Murmuring to himself, he hadn't noticed Anna just yet. He seemed a bit drunk already..."
    play sound surprise
    scene 32-16 hob 4 with Dissolve(1)
    a "Benjamin?"
    with vpunch
    b1 "Anna?! Wha... I didn't expect you here."
    a "I, ummm... Well, we had a deal, remember?"
    b1 "Of course, I just didn't expect you to follow through."
    scene 32-16 hob 5 with Dissolve(1)
    b1 "I see, you've brought some goodies, eh?"
    a "Yeah... I... I thought this would be a good thank you gift for at least trying to help me."
    b1 "It's perfect!"
    b1 "Used to drink just regular old beer or whatnot."
    b1 "But this, this seems great."
    b1 "Excuse me! Where are my manners... Come, come sit down. There's plenty of room."
    scene 32-16 hob 6 with Dissolve(1)
    b1 "I've been on a 12-day long streak of no hard liquor, and now it's time to break it."
    a "Soo... Um..."
    "There was awkwardness in the air. Anna didn't exactly know what she was doing here..."
    a "How are... You doing? Doing good? Got food?"
    b1 "There's plenty of food around. Old Jimmy just hit the road and left me his stove. Plus, I still have what you brought me, so I'm eating hearty!"
    scene 32-16 hob 7 with Dissolve(1)
    a "That sounds... Um... Great..."
    b1 "Right? It was high time that old fart moved out... Bringing his crackheads here..."
    b1 "I've always said one thing, Give me a beer, give me whiskey, but don't ever try to feed me any of that crack rock shit."
    b1 "Tried it once. Ended up naked, on a highway, next to a dead antelope. I've no idea how it got there or, for that matter... How I got there..."
    a "Wow... That's a hell of a story..."
    b1 "Girl... You ain't heard nothing yet..."
    b1 "Now... How about you crack open that bottle, pun intended... Haha..."
    scene 32-16 hob 8 with Dissolve(1)
    "Anna got to opening it..."
    b1 "You know, in Russia, they have a saying, if you can count the cracks of opening a bottle, you will have very good luck."
    a "Really?"
    b1 "Yeah... And you know what?!"
    play sound surprise
    with vpunch
    b1 "It WORKS! HAHA!"
    b1 "I've been getting luckier and luckier in the past few weeks."
    b1 "Anyway, Drink up. We have a tradition that whoever opens up the. drinks first."
    b1 "It was mostly so that the person would get some because usually, it disappears very quickly."
    play sound drinkingBeverage
    scene 32-16 hob 9 with Dissolve(1)
    "Anna played friendly and took the first sip. Still questioning her decisions..."
    "But she knew that Benjamin might know some things about Earl... So it was a sacrifice she could make..."
    "Drinking in an alleyway with a homeless guy, who might even be crazy..."
    "She thought that taking a big chug would make it easier to handle..."
    scene 32-16 hob 10 with Dissolve(1)
    b1 "Impressive. Chugging like a proper Free spirit!"
    a "Free spirit?"
    b1 "We here don't judge. We aren't a part of the culturally impoverished and disconnected society. That seems oxymoronic in its view of idiosyncrasy."
    b1 "Which stems from lack of self-awareness on an ideological level thus bringing huge polarization and discord amongst the societies different class norms."
    b1 "That ultimately leads to presumptions, judgmental and ignorant look towards us - Free Spirits."
    b1 "And as the world continues to plunge deeper into individualism, it seems to lose the very core and essence of itself due to the huge variety of opinion."
    b1 "Everyone and no one are right at the same time..."
    a "What?..."
    b1 "Yeah... Anyway, give me the bottle. I need a chug, too... Hehe..."
    play sound drinkingBeverage
    scene 32-16 hob 11 with Dissolve(1)
    "Benjamin took the bottle and went bottoms up. He gulped the bottle with ease."
    a "Slow down, Benjamin. You will pass out at this rate."
    "Benjamin seemed to ignore Anna's concerns and continued to empty the bottle."
    scene 32-16 hob 12 with Dissolve(1)
    b1 "Ahh... That was good!"
    a "Yeah, you drank like one-third of the bottle."
    b1 "I do what I enjoy, hehe..."
    a "Ok... I mean, your business."
    b1 "Don't worry, I'm used to drinking like this with my pals."
    scene 32-16 hob 13 with Dissolve(1)
    b1 "And the brand makes it even easier. I rarely get these labels. Usually, something watered down..."
    b1 "But this beauty is such a breeze to drink. Don't you think?"
    a "I... I don't think so. I already got dizzy from that first mouthful."
    b1 "Come on. Don't be like that, here. Enjoy some more of the bottle."
    play sound drinkingBeverage
    scene 32-16 hob 14 with Dissolve(1)
    "Anna decided to play along and took the bottle."
    b1 "Thatta girl. I love a woman who holds her liquor."
    "She took a smaller chug from the bottle with quick motion this time."
    b1 "Nice, nice!"
    a "{i}...At this rate, I will be so drunk I won't understand what's happening. I have to slow down..."
    b1 "Don't be so shy. Let me help you."
    play sound surprise
    scene 32-16 hob 15 with Dissolve(1)
    "Suddenly, Benjamin took the bottle and pushed it higher."
    b1 "Yeah, some more won't hurt you, I promise. This is some good stuff."
    a "MMhh..."
    "Anna didn't expect that from Benjamin. Perhaps, he just needed a drinking buddy."
    a "Stop!.... Mh...."
    play sound surprise2
    scene 32-16 hob 16 with vpunch
    "Anna pushed the bottle away, and it dropped out of their hands."
    b1 "NOOOOO..."
    a "Oh, shit..."
    b1 "THE BOTTLE...."
    scene 32-16 hob 17 with Dissolve(1)
    "Benjamin didn't hesitate to run after the bottle and check if it's ok."
    b1 "My dear whiskey... Are you ok?"
    a "It's just some alcohol, no need to go crazy about it... Haha..."
    a "Oh, I feel rather drunk already... I hope I don't fall over like that bottle."
    scene 32-16 hob 18-1 with Dissolve(1)
    b1 "It's fine, and we still have plenty of alcohol left in there."
    a "Great, It's about damn time that you took another 'sip'... Come on, Ben, sip, sip."
    b1 "You seem to be enjoying this mood very much, hehe..."
    a "Nothing wrong with a Free Spirit enjoy herself, eh?"
    "Anna was starting to babble drunk talk, and Benjamin was enjoying every moment of it."
    "Anna saw an opportunity to ask him about Earl."
    a "Hey, Benjamin, why don't you tell me a bit more about Detective Earl?"
    b1 "Why such a sudden change of topic?"
    play sound drinkingBeverage
    scene 32-16 hob 19 with Dissolve(1)
    a "I don't know, seemed like it was appropriate."
    b1 "Well, there isn't that much to tell... He's a cop, a good one, but he's very vicious."
    b1 "All criminals fear him because he can't really be bought, plays by his own rules."
    b1 "Beats up thugs to get information if needed. That sort of thing..."
    scene 32-16 hob 20 with Dissolve(1)
    a "Do you have any dirt on him? I mean, any leads that I could follow?"
    b1 "Well, there is something... But, I'm not sure I should tell you."
    a "Why not? It would really help me..."
    b1 "It's just very sensitive information, and if it was to leak, I could get into a lot of trouble..."
    scene 32-16 hob 21 with Dissolve(1)
    "Benjamin had started touching Anna's leg lightly..."
    b1 "And you know, I'm not sure I'm willing to risk it... hehe..."
    "Anna understood right away what it could be about..."
    a "Well, I've helped you in the past, can't you help a lady out?"
    "Anna tried to convince him."
    play sound undress
    scene 32-16 hob 22 with Dissolve(1)
    a "Oh, poor Benjamin..."
    "Anna felt like she had the upper hand in the situation. She could manipulate him to do anything for her..."
    b1 "Anna, you are a goddess amongst men... We should all bow down for you."
    a "Then help me out, and you might gain my favor."
    jump BenjaminEventOneSex
label BenjaminEventOneNoSex:
    scene 32-16 hob 50 with Dissolve(1)
    a "I'm sorry, I shouldn't have come here..."
    b1 "Don't go, please..."
    a "I will... Bye, it was, um... Nice to meet you..."
    scene black with Dissolve(1)
    jump HomeEventTwo
label BenjaminEventOneSex:
    scene 32-16 hob 23 with Dissolve(1)
    a "Oh... You senile man..."
    "Anna decided to play along. He could be her informant..."
    b1 "You are such an amazing woman, Anna..."
    a "I like these kind words from you... You know how to compliment a woman."
    a "Come on, get up."
    "As she helped him stand up, he slipped..."
    with vpunch
    scene 32-16 hob 24 with Dissolve(1)
    "Benjamin was very drunk and barely could stand, and he tipped over..."
    a "Benjamin!"
    b1 "Oh no..."
    play sound lighthit
    scene 32-16 hob 25 with vpunch
    "He fell to the ground and hit his back..."
    b1 "Ouch!"
    a "Are you okay?"
    b1 "Ah shit, Fuck..."
    scene 32-16 hob 26 with Dissolve(1)
    a "Are you hurt?"
    b1 "Ah... A bit... My hip... It's my old injury..."
    a "You fell hard, looks like it."
    b1 "Oh... I'm getting old, so I gotta be more careful."
    a "Where does it hurt?"
    scene 32-16 hob 27 with Dissolve(1)
    b1 "Right here... Around my pelvis..."
    "Anna was surprised and hesitated but offered her help."
    a "I think I can massage it a little bit to make it feel better."
    b1 "Yeah. that would be amazing..."
    "Anna saw that he was in pain."
    scene 32-16 hob 28 with Dissolve(1)
    "She started to caress his leg with soft touches. And that already aroused Benjamin."
    a "Right here? Like this?"
    b1 "Yeah... That's very good. I feel better already..."
    b1 "Keep massaging it..."
    scene 32-16 hob 29 with Dissolve(1)
    "Benjamin was getting hot. it was difficult for him to contain himself..."
    b1 "You're doing great. It's already starting to feel better..."
    scene 32-16 hob 30 with Dissolve(1)
    "Benjamin got so excited, and yet again, his penis peaked out of his pants."
    "Anna noticed it and wondered if she should say anything..."
    b1 "Your hands are so magical on my hip... I wonder if they are magical on anything else, too."
    a "Dream on."
    scene 32-16 hob 31 with Dissolve(1)
    "Anna continued massaging his hip and saw his penis grow ever larger."
    "Benjamin was hoping for Anna to take her hand and touch his dick..."
    "He had been wanting to experience that ever since he first met her..."
    b1 "I've never met a girl like you... Just so... Perfect..."
    scene 32-16 hob 32 with Dissolve(1)
    b1 "Something else needs attention, though..."
    b1 "And if you help me out, I will tell you about Earl."
    menu:
        "Anna decides to agree with Benjamin's offer.":
            "He took her hand and traversed it towards his crotch."
            a "What are you doing, Benjamin?"
            b1 "Just what a man of my position would always do..."
            b1 "And you did want to know more about the detective."
        "Anna was repulsed by the idea.":
            a "Absolutely not! I'm not willing to do that. Sorry..."
            b1 "But... But, Anna..."
            a "It's not me... Sorry..."
            jump BenjaminEventOneNoSex
    scene 32-16 hob 33 with Dissolve(1)
    "He pushed Anna's hand on his crotch and massaged around the area."
    "Anna could feel the tip of his dick touching her fingers..."
    "The state she was in made it easier to bear... Or maybe the fact that she was becoming more slutty than ever..."
    scene 32-16 hob 34 with Dissolve(1)
    "Benjamin's dick was escaping the pants more and more... They were slowly sliding off as Anna continued to rub him."
    a "{i}...What am I doing... And why do I feel a bit hot..."
    b1 "{i}...She is actually touching my dick... What I wouldn't do for this woman, holy shit..."
    "Benjamin was silently enjoying the slowly increasing lust, but Anna was unsure of what she was feeling."
    play sound surprise
    scene 32-16 hob 35 with Dissolve(1)
    "At this point, Benjamin's dick had expressed itself to the maximum, bulging out of his pants..."
    a "Damn... What am I doing?"
    b1 "I bet you've seen enough of these... hehe..."
    a "Stop talking, or I walk."
    b1 "Ok... Sorry, sorry..."
    scene 32-16 hob 36 with Dissolve(1)
    "Anna was touching his cock more and more with every second. Building up Benjamin's excitement."
    b1 "This feels good... So good... Better than any alcohol could ever do..."
    a "You like that? Will you help me then?"
    b1 "Ah... I think I will. Just keep going..."
    "Anna kept pushing him for answers..."
    play sound jerk
    scene 32-16 hob 37 with Dissolve(1)
    "Suddenly, she grabbed Benjamin's dick, and it sent him over the edge."
    b1 "Fuck... Nice soft hands on my cock... Just the way I like it."
    a "I bet you do, you dirty old pervert..."
    a "{i}...Fine, I will do it. At least I will get some good out of it."
    b1 "Yeah, I am... And you like it... Ahh..."
    scene 32-16 hob 38 with Dissolve(1)
    "His dick had reached its peak size, and Anna had gripped it fully in her hands."
    a "Do you like the motion I'm making, huh? Do you like how I touch it?"
    b1 "Yes. I want you to go faster... Do as I order, and I will tell you anything."
    a "Ok... I will do as you tell me to..."
    scene 32-16 hob 39 with Dissolve(1)
    b1 "Ah... Those hands are... Fuck..."
    "Anna increased her pace as she rubbed his dick, and she could see pure enjoyment in Benjamin's face."
    b1 "Keep stroking my cock... I want you to go faster!"
    a "I will do as you say... Benjamin..."
    scene 32-16 hob 39-1 with Dissolve(1)
    "Anna notices a magazine behind him."
    a "You still have that magazine, Benjamin?"
    b1 "Ah... Yeah, two sexy ladies... My favorite wank material... Oh..."
    "Anna was increasing the pace with every moment, driving Benjamin crazy."
    play sound jerk
    show HoboHandOne with Dissolve(1)
    "Anna was rubbing his cock with her moist hands."
    "Millions of thoughts were rushing her head..."
    "She tried to justify doing this..."
    a "{i}...I... I should just stop thinking right now."
    show HoboHandTwo with Dissolve(1)
    "And so Anna continued, with blank mind... Like a sex toy for some hobo to enjoy..."
    "Hoping that it would end as soon as possible and that some good would come out of it..."
    b1 "Your hands... They are amazing... I love em... I LOVE THEM!"
    b1 "Buuut... AH..."
    scene 32-16 hob 40 with Dissolve(1)
    b1 "Could you perhaps... Give me some more?"
    b1 "Like, maybe, give me some lickety lick?"
    a "What? I'm not touching your smelly dick with anything but my hands."
    b1 "But you will help out a hopeless man AND get the information you wanted..."
    a "You already promised, though!"
    b1 "Come on, you know what's on the line here..."
    a "You old prick!"
    menu:
        "Anna realizes that the info could be detrimental to her...":
            a "Fine, you dirty old pervert... But fuck you for this..."
            b1 "That's my girl! Hehe..."
            a "I need some more alcohol for this..."
            $ AnnaCorruption +=1
            $ corruption_func("Anna Corruption +1")
            jump BenjaminEventOneBlowjob
        "Anna doesn't want to go that far...":
            a "No! I don't want to put my mouth on your stinky dick!"
            b1 "Don't be so rude! I don't have all the amenities available..."
            jump BenjaminEventOneNoSex
label BenjaminEventOneBlowjob:
    play audio drinkingBeverage
    scene 32-16 hob 41 with Dissolve(1)
    "Anna took the bottle and chugged it more..."
    b1 "Oh, yeah... This is amazing... Keep going, girl..."
    "Anna took an exaggerated sip... She wasn't even sure if this all was worth it, but she had gone this far..."
    "Might as well finish it."
    scene 32-16 hob 42 with Dissolve(1)
    "Anna didn't want to do it, but... Perhaps it would pay off later on..."
    a "Are you ready?"
    b1 "Am I ever? I've been waiting for this since the day I met you..."
    a "Alright... here we go... The smell it's... Strong..."
    play sound jerk2
    show HoboBlowOne with Dissolve(1)
    a "{i}...I better get this over with quickly..."
    "She started to go up and down along Benjamin's shaft in a slow manner..."
    "The alcohol had kicked in, and it was easier for her to contain herself..."
    "The stench seemed a bit less strong..."
    b1 "Fuuck... My pals won't believe me..."
    b1 "Ah..."
    play sound jerk3
    show HoboBlowTwo with Dissolve(1)
    "Anna's pace increased as she wanted to get it over with..."
    a "Mff... Mh..."
    a "{i}...Fuck this guy, for sure..."
    b1 "Keep licking! I'm ahh..."
    menu:
        "Cum in Anna's mouth":
            scene 32-16 hob 45-1 with Dissolve(1)
            "He grabbed her head and started to thrust into her mouth..."
            "Like an animal, lead by instinct..."
            a "Ah... Mfff..."
            "Anna's mouth was full with Benjamin's dick..."
            a "{i}...What the hell... I can't escape his clutches..."
            "She could barely keep herself from vomiting all over it."
            play sound jerk
            scene 32-16 hob 46-1 with Dissolve(1)
            b1 "Fuuuck..."
            with flash
            b1 "I'm coming iiin..."
            b1 "In yo mouth... AAHHH."
            with flash
            b1 "My dick in your mouth... Hella goood!!!!"
            "Benjamin's cum was gushing into Anna's mouth."
            "His ejaculate was filling her oral cavity to the brim."
            with flash
            scene 32-16 hob 48-1 with Dissolve(1)
            a "{b}*Gulp*{/b}"
            "Anna swallowed his thick semen..."
            a "Fuck... There was so much..."
            b1 "Girl... You don't even know..."
            a "Why did you do that???"
            b1 "I couldn't help myself..."
            $ benjamin_var_three = True
        "Cum on Anna's lovely face.":
            with vpunch
            with flash
            scene 32-16 hob 46 with Dissolve(1)
            with flash
            "BOOM!!!"
            "Benjamin's ejaculate was exploding all over Anna's silky soft face."
            b1 "MY DIIICKK... YEHAW!!!"
            with flash
            b1 "It's all coming out... RECEIVE IT!!!!"
            a "FUUUCKK AAHHHH...."
            scene 32-16 hob 48 with Dissolve(1)
            a "There is so much... I hope non of it got on my dress... Ah."
            b1 "You betcha... I've been patiently waiting to explode my load on you for a while..."
            a "Damn... Such a mess..."
label BenjaminEventOneFinish:
    b1 "I can't believe it... I came so much..."
    b1 "I'm sorry for that... Anna, oh no..."
    b1 "Are you ok?"
    "Benjamin didn't really care, he was actually enjoying the artwork he had created on her face."
    if benjamin_var_three == True:
        scene 32-16 hob 50-2 with Dissolve(1)
        a "I hope the intel will be as good as the pleasure I just gave you."
        b1 "You bet it will..."
        a "Let me just clean up real quick."
        "Anna took a napkin and wiped her face."
    else:
        scene 32-16 hob 50-1 with Dissolve(1)
        a "I hope the intel will be as good as the pleasure I just gave you."
        b1 "You bet it will..."
        a "Let me just clean up real quick."
        "Anna took a napkin and wiped her face."
    scene 32-16 hob 50 with Dissolve(1)
    b1 "Alright, let me get up real quick."
    a "Will you be ok, with your leg and all?"
    b1 "Yeah, yeah... Your 'massage' gave me some comfort and pain relief. Thank you."
    "Anna was ready to get some good news for a change."
    scene 32-16 hob 52 with Dissolve(1)
    "She looked down, and his cock was still hard as a rock."
    a "Umm, will you put that away?"
    b1 "No, I'm fine... Thanks... heh..."
    a "Alright... Anyway... What can you tell me?"
    scene 32-16 hob 51 with Dissolve(1)
    b1 "Well, you didn't hear it from me, but... Earl has actually been involved in some shady business..."
    a "Oh?... I like the sound of that..."
    b1 "Yeah... I don't know everything, but I do know that he was involved with some drug dealer guy."
    b1 "I knew the drug dealer, but he is dead... Under mysterious circumstances, I might add. And it is pretty fishy."
    b1 "He had a girlfriend... You can find her at the 'Black Cat' brothel. It's in deeper into the industrial district."
    b1 "But beware, it is visited by all kinds of shady characters. Be on your toes if you wish to pick at the thread."
    a "Ok... That is awfully vague... But it will have to do..."
    scene 32-16 hob 53 with Dissolve(1)
    b1 "I'm sorry, but that's the best I can do, and now you have an inside man."
    b1 "I can feed you more information. As long as we can strike a good deal. hehe..."
    a "I knew it wouldn't be that easy... But ok, I will think about it."
    a "Thanks for the help... I will get going now... I have other things to do."
    b1 "Be sure to visit me again. I might have some more information."
    scene black with Dissolve(1)
    jump HomeEventTwo
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
