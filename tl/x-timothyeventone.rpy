label timothySceneOne:
    scene black with Dissolve(1)
    scene 30-7 timothytalk 1 with Dissolve(1)
    "Anna went to Timothy's desk and pondered for a moment."
    "Anna was thinking about her relationship with Timothy."
    menu:
        "Oh, I really enjoyed all those fun times with Timothy, teasing, the game evenings and other things...":
            $ timothySexContent = True
            $ TimothyRelationship += 4
            $ AnnaCorruption +=3
            $ relationship_func("Timothy Relationship +4, Anna Corruption +3")
        "He is such a nice techie, but that's as far as it's gone so far.":
            $ timothySexContent = False
            $ relationship_func("Timothy Relationship +1")
            $ TimothyRelationship += 1

    scene 30-7 timothytalk 2 with Dissolve(1)
    if timothySexContent == True:
        a "Hey, Timothy... How are you doing?"
        t "Oh, Hey, Anna. I'm doing fine, adjusting to the new office area."
        a "Do you like it? Do you like what you see?"
        t "I...Uhm... Yes, I like the new space, if that's what you mean."
        t "Is that what you mean?"
        a "Of course, Timothy... What else would I mean?"
        t "I...Umm...Nothing Anna."
        scene 30-7 timothytalk 3 with Dissolve(1)
        a "I'm joking around Timothy, it's good to see you."
        t "You too, Anna."
        a "New things coming, Timothy."
        a "I'm looking forward to them... and you..."
        t "What was that, Anna?"
        a "Nothing...hehe."
        t "Okay, and what about you? Do you like the new work area?"
        a "Yes, I do."
    else:
        a "Hello, Timothy. How is it going?"
        t "Oh, Hello, Anna. I'm okay, just adjusting to the new office."
        a "Yeah, me too, I like it too."
        t "Yeah...{i}...I like you too{/i}..."
        a "Huh?"
        t "Ummm...Nothing, Anna."
    a "Anyway, I have some issues with my computer, could you help me out?"
    t "Yeah, I should be able to take a look, what is the problem?"
    a "Well, I tried to open the shared drives and they didn't work."
    t "Alright, let's go take a look."
    if timothySexContent == True:
        scene 30-7 timothytalk 4 with Dissolve(1)
        e "Hey, guys. Whatcha doing?"
        t "Uh, Hi, Emily."
        t "Anna has some problems with her computer."
        t "Will try to fix the issue."
        e "You go get them, tiger."
        t "What?"
        a "Hehe, Emily, give him a break."
        e "I'm just joking around, guys."
        e "See you later, dearies."
        scene 30-8 coffee 5 with Dissolve(1)
    a "Anyway, how have you been, Timothy?"
    t "Been fine, I...A lot of things have happened, you know?"
    if timothySexContent == True:
        a "Yes, a lot has happened."
        a "If you know what I mean...hehe..."
        t "Oh, Anna."
    else:
        a "Yeah, I know what you mean."
        a "Somethings in my life have also changed."

    a "Anyway, right this way, have to fix the computer so I can get to work."
    scene 30-8 coffee 6 with Dissolve(1)
    a "So, When I tried to open the drive, it gives me this error and closes the finder."
    a "I don't what else to tell you."
    t "Ah, I think I already see the problem, it will be a bit of software and hardware thing."
    t "First, I need to do some software things, a little system drive reset."
    scene 30-8 coffee 7 with Dissolve(1)
    t "Also I will rename the disk and reset the directory location on your computer."
    t "After that, I will check if your permissions have been updated, Ok?"
    a "Okay, Timothy. You know what to do."
    t "Anyway..."
    t "I will have to get under the table, I need to do some cable management as well if you don't mind."
    a "Oh, no problem at all, go ahead."
    scene 30-8 coffee 8 with Dissolve(1)
    t "{i}...Gotta be careful..."
    t "Right, some cables here have to be changed. It will just take a moment..."
    t "I should be able to do it without any other equipment."
    a "Good luck down there."
    t "Yeah, Thanks, Anna."
    scene 30-7 timothy 9 with Dissolve(1)
    "Timothy was fixing the wires and was super focused."
    "Some of the wires were mixed in the setup process."
    t "{i}...I didn't set this up... They should have called me. Amateurs...."
    t "{i}...At least non of the things are broken or too messed up."
    "Meanwhile, Anna had was thinking about something..."
    scene 30-7 timothy 10 with Dissolve(1)
    if timothySexContent == True:
        "Timothy was changing the wires and was sweating a bit because he was close to Anna's legs."
        "Meanwhile, Anna was enjoying the situation and was thinking if she should give Timothy a little reward for helping her."
        menu:
            "Maybe I should distract Timothy a bit have some fun with him...":
                $ AnnaCorruption += 1
                $ corruption_func("Anna Corruption +1")
                jump spreadLegsForTimothy
            "I should focus on the job right now. Any fun stuff could be left for later.":
                jump noSpreadLegsForTimothy
    else:

        jump alternateTimothy


    return
label spreadLegsForTimothy:
    a "How is it going down there Timothy?"
    t "It's a bit complicated to explain right now, but some of the wires have been incorrectly plugged."
    a "Oh, I see. Will you be able to fix it?"
    t "Should be no problem."
    a "That's good, Timothy, you're my hero."
    t "Oh, stop it, Anna. Just helping."
    a "No, Truly, Timothy."
    t "No problem, Anna."
    play sound surprise
    scene 30-7 timothy 11 with Dissolve(1)
    "Anna moved closer to the desk. To get into a better position."
    "Meanwhile, Timothy was still fixing the wires."
    "But for a moment, his gaze turned to Anna's legs, that had spread a bit."
    "Anna, of course, knew what she was doing."
    "Timothy started to stare. However, he had fixed the issue already."
    scene 30-7 timothy 12 with Dissolve(1)
    a "How is it going down there, Timothy?"
    t "I'm still fixing things, soon finished."
    a "Take your time... I want everything to work perfectly."
    t "Yes, ma'am... I mean, Anna."
    a "hehe...Timothy's right where I want him."
    scene 30-7 timothy 13 with Dissolve(1)
    "Timothy hadn't stopped starring for a straight minute."
    "He was engulfed by those thighs, and that sweet, sweet pussy."
    "Some good memories came back to him."
    t "{i}...Oh, That pussy...And those legs..."
    "Meanwhile, Anna thought to take it a bit further."
    "She just..."
    play sound undress
    scene 30-7 timothy 14 with Dissolve(1)
    "Just pulled the panties to the side, revealing her clit and pussy lips to Timothy."
    a "{i}...Let's see how you handle this, Timothy..."
    "Timothy was shocked, but also getting really turned on, really fast."
    t "{i}...Mmm...Those pussy lips, I would just go down on her so hard right now..."
    "Timothy was too focused on her pussy to notice he was still under the table, and when he was getting up, he hit his head against the desk."
    scene 30-7 timothy 14 with Dissolve(1)
    scene black
    play sound lighthit
    with vpunch
    scene 30-7 timothy 15 with Dissolve(1)
    t "Ouch..."
    a "Oh, Timothy, are you okay?"
    scene 30-7 timothy 16 with Dissolve(1)
    t "Ouch...Yes...I'm okay..."
    "And like that, it was over."
    t "{i}...I blew it, eh..."
    a "Are you sure you are okay, Timothy?"
    t "Yes, Anna. Thank you for caring."
    t "{i}...Well, next time will succeed maybe..."
    a "{i}...He is so cute and goofy....hehe..."
    scene 30-7 timothy 17 with Dissolve(1)
    "Timothy got up and checked the computer."
    t "Ouch...Still hurts!"
    a "Will you be alright, Timothy?"
    t "Yeah, I should be, I'm a strong guy."
    a "Of course you are, Timothy."
    a "{i}...Poor guy... Maybe I should give him a kiss?"
    scene 30-7 timothy 18 with Dissolve(1)
    "Timothy had fixed the computer and everything looked to be working."
    a "Oh, it looks like everything is working."
    a "Thank you so much, Timothy."
    t "No problem, Anna. I'm glad to help."
    t "{i}...Oh, that pussy...Mmmm...."
    t "Anyway, that is all, I will get going then."
    a "Wait, dear."
    scene 30-7 timothy 19 with Dissolve(1)
    with vpunch
    "Anna gave Timothy a sweet kiss for his hard work and hurt head."
    "Timothy was enjoying the kiss a lot."
    t "{i}...I wish we could do a bit more than that."
    a "{i}...Timothy, you little rascal..."
    "She kissed him for a good while..."
    scene 30-7 timothy 20 with Dissolve(1)
    a "Thank you again, Timothy."
    t "Thank you for the kiss, Anna. That makes it worth it, always."
    a "I know it does."
    a "Perhaps later, we could have something else as well?"
    "Timothy got a bit embarrassed and awkward."
    t "I...Umm...Yes, sure, Anna..."
    "Timothy almost tripped."
    "But he liked the sound of that."
    t "Anyway, I will get going, You probably have some work to do."
    a "Thank you again, Timothy."
    jump pornguycall

    return

label noSpreadLegsForTimothy:
    scene 30-7 timothy 17 with Dissolve(1)
    "Timothy got back from under the table."
    t "Alright, everything should be set up correctly now."
    t "Check if you can open the drive this time."
    a "Ok... Annnd...Yes!"
    a "It works now."
    a "Thank you so much, Timothy."
    t "No problem Anna, always for you."
    scene 30-7 timothy 18 with Dissolve(1)
    "Timothy had fixed the computer, and everything looked to be working."
    a "Thank you so much, Timothy."
    t "No problem, Anna. I'm glad to help."
    t "Anyway, that is all. I will get going then."
    a "Wait, dear."
    scene 30-7 timothy 19 with Dissolve(1)
    with vpunch
    "Anna gave Timothy a sweet kiss for his hard work and hurt head."
    "Timothy was enjoying the kiss a lot."
    t "I wish we could do a bit more than that."
    a "Timothy, you little rascal..."
    "She kissed him for a good while..."
    scene 30-7 timothy 20 with Dissolve(1)
    a "Thank you again, Timothy."
    t "Thank you for the kiss, Anna. That makes it worth it, always."
    a "I know it does."
    a "Perhaps later, we could have something else as well?"
    "Timothy got a bit embarrassed and awkward."
    t "I...Umm...Yes, sure, Anna..."
    "Timothy almost tripped."
    "But he liked the sound of that."
    t "Anyway, I will get going. You probably have some work to do."
    a "Thank you again, Timothy."
    jump pornguycall

    return

label alternateTimothy:
    scene 30-7 timothy 10 with Dissolve(1)
    a "How is it going down there, Timothy?"
    t "It's a bit complicated to explain right now, but some of the wires have been incorrectly plugged."
    a "Oh, I see. Will you be able to fix it?"
    t "Should be no problem."
    a "That's good, Timothy. Thank you very much."
    t "No problem, Anna."
    scene black
    with vpunch
    t "Ouch..."
    a "Oh, are you okay?"
    scene 30-7 timothy 16 with Dissolve(1)
    t "Ouch...Yes...I'm okay..."
    a "Are you certain you're okay?"
    t "Yes, Thank you, Anna."
    scene 30-7 timothy 17 with Dissolve(1)
    "Timothy got back from under the table."
    t "Alright, everything should be set up correctly now."
    t "Check if you can open the drive this time."
    a "Ok... Annnd...Yes!"
    a "It works now."
    scene 30-7 timothy 18 with Dissolve(1)
    a "Thank you so much, Timothy."
    t "No problem, Anna, always for you."
    t "Anyway, I will get going. If you have any other problems, let me know."
    a "Will do, Timothy. Thank you again."
    jump pornguycall
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
