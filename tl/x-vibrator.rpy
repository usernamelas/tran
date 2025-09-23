label VibratorFirstTime:
    play sound undress
    scene black with Dissolve(1)
    scene 32-8 vib 1 with Dissolve(1)
    "Anna looked at the bed and the cupboard where a special item was waiting for her."
    "She thought about all the days events and figured that this was a good time to unwind."
    a "{i}...What a day so far... I need to relax a bit..."
    scene 32-8 vib 2 with Dissolve(1)
    if DilanPornShootQuestDone == False:
        "Anna had become rather horny from what she saw in the gym's showers earlier."
    else:
        "Anna was still a bit horny from the day's adventures, so a bit more would be enough."
    "She decided that it was a good time to get some light release."
    "She had stored away a vibrator for such occasions."
    "Well, a dildo/vibrator..."
    a "{i}...Ah... Their session got quite steamy, even made me a bit jealous..."
    scene 32-8 vib 3 with Dissolve(1)
    a "{i}...Haven't used this one in a while... Mmm... I want it..."
    "Anna was getting hot just by looking at it."
    "The anticipation of putting it in was strong."
    if DilanPornShootQuestDone == False:
        "But was the dildo enough to release her tension? Or did she need more?"
    scene 32-8 vib 4 with Dissolve(1)
    "Anna started to lightly slide the tip up and down her vagina."
    "It was so moist down there, her juices were dripping down her ass crack on perfectly clean sheets."
    "But Anna couldn't care about that, she had no one to go to, so she had to resort to this toy."
    a "{i}...Ah, how I want a dick right now..."
    if johnBeenNaked == True:
        a "{i}...I wonder where John is... Haven't seen him..."
    scene 32-8 vib 5 with Dissolve(1)
    if johnBeenNaked == True:
        a "{i}...John... Ahh..."
    elif SergeySexContent == True and johnBeenNaked == False:
        a "{i}...Ah... Sergey..."
    "Anna pushed the tip into her pussy with ease."
    "The sensation was light but very, very pleasurable."
    "her moist vaginal lips were welcoming the dildo in without any resistance."
    a "{i}...Ah... I need some dick..."
    play sound jerk2
    scene 32-8 vib 6 with Dissolve(1)
    "The deeper she pushed it the more pleasure she felt."
    "But she felt that it wouldn't be enough..."
    "Anna started to thrust the dildo in and out at a fast pace."
    a "{i}...Fuck... Ahh..."
    "Her mind was filling with all kinds of fantasies."
    show AnnaVibOne with Dissolve(1)
    "Increasing pace she was thinking about..."
    if johnBeenNaked == True and SergeySexContent == False:
        a "{i}...John... Fuck me!..."
    elif SergeySexContent == True and johnBeenNaked == False:
        a "{i}...Sergey... Penetrate me harder!!!..."
    elif AlfredRelationship == True and johnBeenNaked == False and SergeySexContent == False:
        a "{i}...Oh, Alfred... Your experienced hands need to be all over me..."
    elif CarlSexContent == True and AlfredRelationship == False and johnBeenNaked == False and SergeySexContent == False:
        a "{i}...I need that dick inside of me, Carl... Oh..."
    elif CarlSexContent == False and AlfredRelationship == False and johnBeenNaked == False and SergeySexContent == False and jeremySexContent == False and TaxmanFootjob == False and DilanPornContent == False:
        a "{i}...Andrew... Even after all of our troubles... Please... Fuck me!..."
    elif CarlSexContent == True and AlfredRelationship == True and johnBeenNaked == True and SergeySexContent == True and jeremySexContent == True and TaxmanFootjob == True and DilanPornContent == True:
        a "{i}...Somebody just fuck me... I need some dick..."
    a "Ahh... this feels good..."
    "Anna was starting to feel tingling all over her body."
    play sound moaningtwo
    show AnnaVibTwo with Dissolve(1)
    hide AnnaVibOne
    a "I'm getting close... ah..."
    a "I need it..."
    a "{i}...This feels good, but some dick would be better..."
    "Anna started too feel the sensation build-up to the peak."
    a "I'm... I'm... Mmmm..."
    a "Ah... My pussy!!"
    "Anna started to climax in a explosive manner... Shivering and shaking..."
    with flash
    a "AAHH!!"
    with flash
    a "Mff..."
    play sound jerk
    scene 32-8 vib 7 with flash
    a "Oh... That's... Goood...."
    with vpunch
    "She was cumming for a good while and it felt pleasurable."
    "But not enough for her... Perhaps she was missing some additional stimulation..."
    "Or excitement..."
    if AnnaCorruption > 40:
        "Or maybe someone to do it infront of. Perhaps even multiple someones, like a camshow..."
    scene 32-8 vib 8 with Dissolve(1)
    hide AnnaVibTwo
    "Anna dropped down..."
    "She felt exhausted and was all sweaty..."
    if DilanPornShootQuestDone == False:
        "But something was off..."
        "Anna was wondering about everything and it felt like it wasn't enough."
        "The session was a mere passing of time and didn't help her that much to get rid of her arousal."
        a "{i}...Ah... Should I go again? I need more..."
        a "{i}...No... I have other things to do..."
        a "{i}...Perhaps I should go look for other adventures?..."
    else:
        "Anna felt like it was enough and decided to get dressed."
        a "{i}...Ah that was good..."
    scene black with Dissolve(1)
    play sound undress
    jump JohnEventThree
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
