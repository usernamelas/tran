label preGenericEventOne:
    if dianaGoodRelations == True:
        jump GenericEventOneGoodDiane
    else:
        jump GenericEventOneBadDiane
label GenericEventOneGoodDiane:
    play sound walk
    scene black with Dissolve(2)
    scene 30-2 annas reception secretary with Dissolve(1)
    "Anna arrived at work."
    play sound surprise
    scene 32-5 office 2 with Dissolve(1)
    "Anna was heading to her office and noticed Diane talking to the colleagues."
    "She couldn't hear them, but she was intrigued."
    b10 "I'd so be down to have a party at some point, but well. Nada..."
    b10 "Last time was when Anna and Emily joined us."
    j10 "Yeah, that was dope..."
    d "Oh? I didn't know you were that acquainted. Haha."
    b10 "It was a cool party, though."
    if dianaPartyQuest == True:
        d "In that case, I'd think it would be cool if we all got together before the main thing you know?."
        d "Like a pre-game?"
        j10 "Huh, That would be awesome I think."
        b10 "Definitely, I'm super down to warm up. Haven't had this pre-games for some time now."
    else:

        d "Alright, anyway..."
        d "The papers are in order for you both, I will send them up to accounting soon."
        j10 "Thanks, Diane. We owe you one."
        d "Well... Don't mention it, haha..."
        b10 "Seriously, you've helped us out a lot."
        d "Sure, sure. That's my job. Just don't skip the annual meeting again, deal?"
        j10 "You got a deal, but that time we were 'busy'... Hehe..."
    scene 32-5 office 3 with Dissolve(1)
    a "{i}...What are they talking about..."
    if dianaPartyQuest == True:
        d "So... The party would be at my place on Saturday 3 hours before the corporate event."
        b10 "I should be able to make it no problem."
        j10 "Yeah, me too, I'm free all day."
        d "Great. Thank you, guys."
        b10 "This will be fun... Hehe..."
        b10 "Hey, There's Anna!"
    else:
        d "Oh? I'm intrigued. Would you share the details with me?"
        b10 "Well, we were just having 'fun' with one of the new intern girls from accounting."
        d "Jesus, Brandon! You disgust me."
        b10 "Hey, she wanted it and so did I. You asked for the details."
        d "Yeah, I shouldn't have asked..."
        b10 "Unluckily for the intern, she got fired because she was also not present in the meeting..."
        b10 "I still have her number just in case."
        j10 "Hey there's Anna!"
    scene 32-5 office 4-1 with Dissolve(1)
    d "Oh Hey, Anna. How are you doing?"
    a "Hello, Diane. I'm fine, just got to prep for contracts."
    b10 "Yeah, I heard you are working with East Oil Conglomerate?"
    a "That's one of the contracts, yes."
    j10 "Sheesh, I heard that they are pretty tough with their rules and regulations."
    j10 "Unless you wave a bunch of money in their face or... Something else... Hehe..."
    a "I will act as if I didn't hear that."
    scene 32-5 office 5-1 with Dissolve(1)
    a "Anyway, what you guys talking about?"
    if dianaPartyQuest == True:
        d "We were just discussing the pre-game party."
        a "Right, You told me something a couple of days ago."
        d "And I thought that I'd start organizing something. We would just warm up at my place."
        a "Warm up?"
        d "Nothing too big, just some drinks, choose an outfit, stuff like that."
        a "That sounds perfect, actually."
    else:
        "We were just discussing some personal matters."
        j10 "Nothing, personal about that intern, right Brandon?"
        b10 "Shush, Justin. No need to make us in such big assholes..."
        d "We already know you are assholes. But at least you are nice to us."
        b10 "How could we not be? You are awesome colleagues."
    scene 32-5 office 6-1 with Dissolve(1)
    d "By the way, I didn't know that you have had a party with Justin and Bradon."
    a "Oh, Haha... That was cool, I'm sorry I didn't invite you, it wasn't up to me."
    d "Oh, don't worry about it. It's alright."
    d "Anyway, I have to run now. Guys, take care..."
    scene 32-5 office 7-1 with Dissolve(1)
    "Diane rushed away..."
    j10 "Have you already picked a dress for the corporate party?"
    a "What corporate party? Am I missing something?"
    b10 "Yeah. Ethan is organizing the whole thing. And he gave some of us tasks."
    b10 "Justin is supposed to find a place, I hope he has, and also take care of the food."
    j10 "Diane sent out notification some time ago already. Ethan himself is looking for the entertainment."
    j10 "We were just talking with you about the pre-game."
    a "Whow. I've somehow missed this entire thing. A lot is going on in my life right now."
    b10 "No worries, just read the email that Diane sent to everyone and you're good. Ok?"
    a "Yeah, thanks a lot Brandon. And now I have to find a dress..."
    a "I have to go, guys, take care."
    j10 "You too, and good luck with the contracts."
    scene black with Dissolve(1)
    play sound door2
    "Anna went into her office."
    $ DayFourDianeTalk = True
    jump WorkDayFour
label GenericEventOneBadDiane:
    play sound walk
    scene black with Dissolve(2)
    scene 30-2 annas reception secretary with Dissolve(1)
    "Anna arrived at work."
    play sound surprise
    scene 32-5 office 2 with Dissolve(1)
    "Anna was heading to her office and noticed Diane gossiping with some of the colleagues."
    d "I couldn't believe it myself, haha... But you know, sometimes you strike gold."
    b10 "Damn, those pictures look hot."
    d "You guys are absolutely perverted... I love it, haha..."
    j10 "Look who's talking..."
    d "Oh, stop it."
    scene 32-5 office 3 with Dissolve(1)
    if emilyScene1 == True:
        a "{i}...What are they talking about? Pictures?..."
        a "{i}...I hope she's not talking about the ones she took in the dressing room..."
        "Anna was a bit nervous... This wouldn't be a good time for something to go wrong."
    d "Well, yeah... You can have one, on the house, I will send it to your phone."
    b10 "Thanks, Diane. Much appreciated."
    j10 "Diane! Send it to me, too."
    a "I'm sorry, What?"
    scene 32-5 office 4 with Dissolve(1)
    d "Oh, here's the department head... Let me guess, you got the promotion with your... head?"
    j10 "Who can blame them for letting her..."
    d "Ready to put your ass to work again?"
    menu:
        "Listen, I don't have to take shit from you!":
            a "You are the snake, alright? I just tried to make a living."
            a "And you are always bothering me, like a fucking whore!"
            b10 "Oh, damn."
            d "Haha... You're one to talk, sucking cock left and right!"
            $ relationship_func_decrease("Diane Relationship -1")
            $ DianeBadRelationship += 1
            jump MenuOptionTwo
        "Whatever I don't have time for this.":
            d "Perhaps you should find some time? We have plenty of insults."
            a "Well, I don't really care."
            b10 "We? Come on Diane, we know your beef's with Anna and we are not going to involve ourselves."
            j10 "Right. You girls just go on ahead and vent."
            jump MenuOptionOne
        "Diane, I'm sorry for what has happened to you in the past. We don't have to be enemies. (If Jeremy Relationship > 0)" if jeremySexContent == False:
            a "I don't even know why you're mad at me in the first place."
            a "And I'm sorry if I have done anything to hurt you..."
            a "Can we just talk? I truly wish that we could resolve our issues."
            d "I... I... umm... I don't think it can be fixed so easily..."
            $ relationship_func("Diane Relationship +1")
            $ DianeBadRelationship -= 1
            jump MenuOptionThree
label MenuOptionOne:
    scene 32-5 office 5 with Dissolve(1)
    a "I will just act as if I don't hear you... I have work to do."
    d "I've no need to vent, I'm simply stating a fact. Anna is the office whore along with Emily, from the looks of it."
    if emilyScene1 == True:
        d "And I'm simply fortunate enough to have content of them."
        a "Ridiculous... You know that I can sue you for this?"
        d "I know. But not before your reputation is destroyed..."
    a "You are evil..."
    a "And hurtful..."
    scene 32-5 office 6 with Dissolve(1)
    a "And cruel..."
    d "Yeah. I am, and you are just the office slut!"
    a "Diane, stop!"
    a "This is so wrong. How can you do this?"
    d "Because I can, and because I want to! Your slut behavior is hurting me, too!"
    a "What are you talking about?"
    d "I'm not going to explain myself to you..."
    if emilyScene1 == True:
        d "Anyway, see you around, bitch. We'll see how the office reacts to your photos..."
    "Diane stormed away full of pride in how she has treated Anna..."
    scene 32-5 office 7 with Dissolve(1)
    b10 "That was intense... Anyway..."
    j10 "Yeah, I think I'm going to get back to work... Enough drama for today..."
    j10 "By the way, Anna? Are you ok?"
    a "I... I'm fine... What do you want?"
    j10 "I just wanted to ask you if you've already chosen a dress for the corporate party?"
    a "What corporate party?"
    j10 "Diane sent out a notification regarding the event."
    a "Yeah and she probably took me out of the recipient list..."
    a "{i}...Now I have to figure out what to wear, too..."
    j10 "Maybe, anyway... See you around..."
    $ DayFourDianeTalk = True
    jump WorkDayFour
label MenuOptionTwo:
    scene 32-5 office 5 with Dissolve(1)
    if emilyScene1 == True:
        a "Oh, but you've been doing it way before anyone. You may have some 'evidence' about me, however..."
    a "Everyone in the office knows that you take the cake. You are the office slut."
    a "And always have been. If you just had a speck of humanity in you, you would just stop."
    a "But because your life is fucking miserable you put that shit out on me."
    d "I... I don't! I just know how you earned your place, always the favorite!"
    a "So that's what this is about? Professional jealousy?"
    a "Listen, We are not on the same level. Do You get it? You don't even compare to me!"
    scene 32-5 office 6 with Dissolve(1)
    a "And if you knew what's best for you, you would just fucking stop before someone breaks your fingers."
    d "So you're threatening me now?"
    a "And what if I am? What are you going to do about it? Nothing, cause you are an obedient office slut!"
    "Diane was completely shocked, Anna had rarely shown such anger."
    "She quickly stormed away without saying a word."
    scene 32-5 office 7 with Dissolve(1)
    a "And what are you two looking at? Also want to get scolded?"
    b10 "We... Umm... No... We're sorry, Let's just leave this behind us, ok?"
    a "You better..."
    j10 "Anyway, to lighten up the mood... Have you chosen a dress for the corporate party, Anna?"
    a "Corporate party? Wait... I don't know anything about that..."
    b10 "Diane sent out notifications...."
    a "Sure, sure. She probably left me out of the list of recipients... Thanks for reminding me."
    a "{i}...Now I have to figure out what to wear, too..."
    a "Anyway, I'm going to get to work. Bye."
    $ DayFourDianeTalk = True
    jump WorkDayFour
label MenuOptionThree:
    scene 32-5 office 5 with Dissolve(1)
    a "Why? We could just talk it out. Perhaps if I've done things in the past that upset you..."
    a "I would like to try and fix it... We don't have to agree on everything but we also don't have to hurt each other."
    d "You... You are just not a good person towards me, Anna..."
    d "Your actions have hurt me in the past... And you neglect how I feel about it."
    a "I don't know what I've done, but we should talk about it. Burry the hatchet, so to speak."
    scene 32-5 office 6 with Dissolve(1)
    d "Maybe... Maybe we could do that..."
    a "And then we could perhaps even improve our relationship..."
    d "I don't think it will be that simple. We have some serious issues..."
    a "Yeah... We do... Haha..."
    d "I... I have to go and think about everything..."
    "Diane slowly walked away, full of thoughts..."
    scene 32-5 office 7 with Dissolve(1)
    j10 "I did not expect it to go so smoothly, usually there is always some drama..."
    b10 "I know right? Kudos to Anna about not escalating things..."
    a "Well... We all have our issues, why not try and fix them..."
    b10 "Right... Anyway, You already picked a dress for the corporate party?"
    a "What party? I didn't know..."
    j10 "Well, a notification was sent out, but I guess it didn't reach you."
    a "Yeah... Thanks for the reminder. I have to go... Catch you later."
    a "{i}...Now I have to figure out what to wear, too..."
    $ DayFourDianeTalk = True
    jump WorkDayFour
label WorkDayFour:
    scene generic office 1 with Dissolve(1)
    "Anna sat down at her desk and started to work."
    "She paid heavy focus to the contracts and was starting to finish up with some of the complicated parts."
    scene black with Dissolve(1)
    "Some time past..."
    scene generic office 3 with Dissolve(1)
    a "{i}...It looks like they have a solid case, but if I apply the regulation in a different context..."
    a "{i}...Perhaps we can change the terms..."
    "Anna was working without any brakes as she wanted to go through her contracts at a good pace and very effectively."
    $ ContractProgress +=30
    "Contract analysis progress: [ContractProgress]%%"
    if TaxmanHelps == True or EarlHelp == True:
        "Suddenly Anna got a phone call. It was from Rebecca."
        play sound phonecall
        scene generic office 5 with Dissolve(1)
        r1 "Hey, Anna. How are you doing? I want to meet with you, I miss you."
        r1 "We haven't had a chance to talk properly and just be together..."
        a "What do you have in mind?"
        r1 "I just thought that we could go to the gym. We've been planning on it but haven't had the chance..."
        a "I don't know, Rebecca... I kind of have a lot on my plate right now."
        r1 "Come on sweety, the workout will help you. I know it."
        a "Ok, alright. How could I say no to my sweet sister."
    if GoodBadDoctorChoice == 2:
        jump SchmidtEventThree
    else:
        jump RebeccaEventOne
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
