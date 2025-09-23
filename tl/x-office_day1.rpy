label officeDianeOne:
    $ renpy.music.play("audio/sounds/bensound-thelounge.ogg", channel = 'music', if_changed = True)
    if firstTimeDiane == False:
        scene 30-2 office 1 with Dissolve(1)
        "Anna enters the office reception, where she sees Diane."
        "As she approaches Diane, she starts to think about something..."
        "She ponders about her relationship with Jeremy and Diane."
        "Note: This choice will have a greater impact on future relationships."
        $ firstTimeDiane = True
        $ GlossaryUnlockDiane = True
        menu:
            "There's Diane, I'm glad we were able to become friends now that Jeremy is gone. (Jeremy Dead)":
                $ relationship_func("Diane Relationship +3, Anna Corruption +4")
                $ dianaGoodRelations = True
                $ DianeRelationship += 3
                $ AnnaCorruption += 4
                jump goodDiane
            "Ugh, Diane. I don't like her she feels like a blight in this office along with Jeremy. (Jeremy Alive)":
                $ dianaGoodRelations = False
                $ relationship_func_decrease("Diane Relationship -2, Anna Corruption +4")
                $ DianeBadRelationship += 2
                $ AnnaCorruption += 4
                jump badDiane
    elif (firstTimeDiane == True) and (dianaGoodRelations == True):
        scene 30-2 office reception without anna
        d "Hello Anna, hope you are doing well, I'm a bit busy right now."
        jump officeone
    elif (firstTimeDiane == True) and (dianaGoodRelations == False):
        scene 30-2 office reception without anna
        d "Hello, I'm busy right now!"
        jump officeone
    return
label badDiane:
    scene 30-2 office 2-2 with Dissolve(1)
    d "Oh, it's you, Anna. Yes, What does the 'Hardest worker' wish?"
    a "Cmon Diane, we don't have to be enemies."
    d "We don't have to be friends either, now do we?"
    a "Whatever your beef with me is, it will have to wait, I've come here to work."
    a "Not create drama."
    d "Oh so you are implying that I come here to create drama?"
    a "No, it's not what I meant... You know what? Forget about it."
    scene 30-2 office 3 with Dissolve(1)
    d "Right, I know what you always 'mean', You mean to suck up to everyone in the office."
    d "{b}Literally...{/b}"
    a "I'm sorry What did you say?"
    d "Oh... you know what? Forget about it."
    a "Fine, whatever."
    a "See you later...{i}bitch...{/i}"
    jump EmilyChangingRoomEvent
    return
label goodDiane:
    scene 30-2 office 2-2 with Dissolve(1)
    a "Hello, Diane."
    d "Hi, Anna. How are you doing?"
    a "I'm okay, some crazy things have happened, but I'm okay."
    d "Do you want to talk about it?"
    a "Not right now, sorry."
    d "It's okay, I understand."
    d "Congratulations on becoming a partner, by the way. I'm glad that you got that position."
    d "You deserve it, Anna, truly."
    d "Thank you, dear."
    a "Anyway..."
    define dianaMenuOption1 = False
    define dianaMenuOption2 = False
    menu dianaMenu:
        "How have you been these past couple of days?" if dianaMenuOption1 == False:
            scene 30-2 office 3 with Dissolve(1)
            d "Oh, I'm okay. Visited my grandparents last weekend. They are doing quite okay for their age."
            d "Went out with one guy... I mean, I could tell you all the details, but I have to be a bit mysterious, you know?"
            a "Sure, maybe some other time you could tell me, dear."
            d "Perhaps..."
            d "Anyway, I also did a general cleaning at my place, perhaps we could have a party with our colleagues there next weekend..."
            a "Why not, will have to talk about it a bit later."
            d "Sure."
            $ dianaPartyQuest = True
            $ dianaMenuOption1 = True
            jump dianaMenu
        "How is the workload this week, anything I should know?" if dianaMenuOption2 == False:
            d "Ah, yes. Becoming a partner has its benefits but also some additional responsibilities."
            d "I have already sent you some emails in regards to this position, also a schedule and appointments."
            d "I will send additional paperwork your way once it comes through."
            scene 30-2 office 4 with Dissolve(1)
            d "Also, Ethan wishes to speak with you. I've put it on the agenda for you."
            d "I believe Ethan wishes to discuss things regarding this partner business."
            d "That is all for now."
            a "Thank you very much for this info, Diane."
            $ dianaMenuOption2 = True
            jump dianaMenu
        "That's all":
            jump EmilyChangingRoomEvent
    return


label EmilyChangingRoomEvent:
    scene black
    play music jazzmusic
    play sound surprise
    scene 30-3 emily 1 with Dissolve(1)
    a "Oh sorry to barge in Emily."
    e "Hey Anna, good to see you. Don't worry, I do not mind..."
    if dianaGoodRelations == True:
        e "Congratulations on becoming a partner."
        e "I know you could beat the competition and come out on top."
        a "Aww, thanks Emily I appreciate this."
        e "And now since that scumbag, Jeremy is out of the way, I feel like you can make things much better around here."
        a "Hope I can live up to the expectations."
    e "Anyway, What's up, you look a little stressed out."
    a "Well, I have to tell you something, it's pretty serious."
    a "I don't know if I should tell you this, but I have to get it off my chest."
    e "Sure, if you are not ready, I won't ask you to explain."
    scene 30-3 emily 2 with Dissolve(1)
    a "I know it's okay, I think it's better if I tell you."
    a "You are a really nice person, Emily, you know that already, though."
    e "Thank you, Anna, I won't forget this."
    a "Ok, Well basically..."
    a "Andrew...Has been shot..."
    stop music
    with vpunch
    scene 30-3 emily 3 with Dissolve(1)
    e "What?!"
    play music blues
    e "Oh my god, honey, are you okay??"
    e "I mean...Is he okay??"
    a "Well, it's complicated, but for the time being he is okay."
    e "What do you mean time being?"
    a "Basically, the doctor said, that he needs extra surgery if he is to live without any complications."
    a "The catch is that the surgery is really expensive, so I have to come up with money and pretty soon."
    e "Oh, no. How exactly did it happen?"
    a "I don't want to say the details, It's really complicated."
    scene 30-3 emily 4 with Dissolve(1)
    e "Okay Anna, I won't push. How are you holding up?"
    a "Well, as good as I can, I witnessed all of those things happen. I was in the middle of it."
    a "Andrew kind of saved my life, but the whole situation we got in was actually his fault."
    a "If he hadn't mixed with the wrong crowd, we would be fine."
    e "Oh, I'm so sorry, Poor Andrew though, kind of paid for his mistake and almost with his life."
    a "Yeah, well it is what it is...At least he is alive."
    e "Come here Anna, give me a hug, you need one, I can comfort you a bit."
    scene 30-3 emily 5 with Dissolve(1)
    a "Oh, you're a bit touchy today, Emily."
    e "Anything I can do to make you feel better, and I mean anything."
    e "You've been through so much lately."
    a "Thanks, Emily, I appreciate it."
    e "Maybe you need someone to caress you a bit, sweetie."
label EmilyScene1:
    scene 30-3 emily 5
    define emilyScene1 = False
    menu EmilyScene1Menu:
        "Oh, Emily, we have been quite close lately.":
            $ emilyScene1 = True
            $ corruption_func("Anna Corruption +1")
            $ AnnaCorruption += 1
            $ persistent.secondScene = True
        "I think that we shouldn't cross the line.":
            e "Oh, Okay... just a hug then Anna..."
            e "You will be okay, I will try to help however I can."
            jump emilyChangingRoomNext
    if emilyScene1 == True:
        play music closuresong fadein 1.0
        "Anna was a bit shocked, but she liked what Emily was doing, it might help her forget all the worries."
        "Emily had a way of making Anna relax and calm down. Emily's approach was a bit straightforward, not too much but enough to be assertive."
        "Anna was getting a bit hot."
        scene 30-3 emily 6 with Dissolve(1)
        e "I have a surprise for you, Anna, but I have to take off your dress."
        a "I don't know if we should do this here, Emily!"
        e "Why, love? Are you nervous that someone might see us?"
        a "Yeah, that wouldn't be good."
        e "That just adds to the excitement, doesn't it?"
        e "Let me just slip this thing down a bit, you look like you're hot in this dress."
        a "Oh, You are moving forward fast Emily..."
        e "If I want something, I get it you know what I mean?"
        scene 30-3 emily 7 with Dissolve(1)
        play sound equipsound
        "Emily almost tears off Anna's dress, exposing her breasts and half-naked body."
        "As soon as she does that, she sees Anna's ass and is amazed by it."
        e "Oh Anna, Your ass is just amazing."
        a "You really think so, Emily?"
        a "Well... I...Uhmm... We should get moving Emily."
        e "Not so fast, Anna dear."
        e "I want to touch it... I really do."
        a "Okay, Emily..."
        scene 30-3 emily 8 with Dissolve(1)
        "Emily comes closer to Anna and caresses her bottocks."
        "That already makes Anna excited."
        "Anna enjoyed Emily's slight dominance. It wasn't too much but it was there, subtle enough to notice, but not too heavy."
        "She needs to be drawn in a bit more. Emily has to be careful as to not set her off..."
        a "Emily, it feels good."
        scene 30-3 emily 9 with Dissolve(1)
        e "I know it does, I'm getting hotter by the second, and looks like you are too."
        a "I...I... Yes, Emily, you are not giving me a choice."
        e "Even if you had a choice, you would choose this, I know it for a fact."
        a "Maybe..."
        a "{i}...Wow, Emily knows what she is doing, Well, she has always known, but now it's even more effective."
        scene 30-3 emily 11 with Dissolve(1)
        "As Anna was in her thoughts about Emily's dominance, she didn't even notice how Emily had closed the distance again."
        "Emily had gripped Anna a bit tighter this time, Feeling her chest and caressing her hair."
        "She had a goal in mind and she was not going to stop until she gets what she wants."
        "Anna is a bit lost in Emily's grip and her eyes, overtaken by the sensation."
        a "Oh Emily, you are so beautiful..."
        e "No, I'm fucking hot, and you are just out of this world, Anna."
        a "Thanks...Emily..."
        e "The things I want to do to you..."
        with flash
        a "Tell me..."
        e "No... Let me just show you..."
        a "Okay, Emily."
        scene 30-3 emily 12 with Dissolve(1)
        "Emily gripped Anna even tighter this time and put her palm on Anna's scalp caressing it and bring her even closer."
        "Anna was looking deep into Emily's eyes, mesmerized... Almost petrified by them..."
        "Emily was in control and all Anna could do was just let it happen..."
        "All she could do was let Emily control her, kiss her, caress her..."
        "Emily was leaning in for a kiss and Anna wasn't going to stop her."
        scene black with Dissolve(0.5)
        scene 30-3 emily 13 with Dissolve(1)
        "The kiss was almost magical, Anna was lost in the moment..."
        "Emily was lost too... Just lusting for Anna's soft, plushy lips..."
        "Both of them intertwined in an encounter unparalleled..."
        "Both getting hotter and hotter."
        "..."
        "But Emily was not going to stop there, No..."
        "She wants to go all the way... And so she will, Cause she wants it, Anna needs it, both of them lust for it..."
        scene 30-3 emily 14 with Dissolve(1)
        play sound jerk
        "Anna is just not here, all her worries, all her stress, Andrew, Sergey, the money, all of it non-existent..."
        "Emily was not there either, just blank mind for a moment that feels like it lasts forever..."
        "Her senses were coming back, and Anna was in for a surprise..."
        "Emily licked Anna's lips once more and..."
        scene 30-3 emily 15 with Dissolve(1)
        "...And pulled away immediately and changed her focus to Anna's hard nipples, She just felt Anna, she knew what she wanted..."
        "And so without a single sign of protest, Anna just let it happen, looking at Emily as she takes even more control of Anna."
        a "Oh...Emily...That feels amazing, You are just whoa..."
        a "I'm a bit lightheaded... But that's a good thing..."
        a "Keep doing what you are doing and don't stop..."
        scene black with Dissolve(1)

        show nippleLickOne with Dissolve(1)
        play sound jerk2
        a "Please don't stop... It feels so fucking amazing, Emily..."
        "Emily, of course, had no intention of stopping..."
        "She liked the position they were in."
        "And Anna, well, she was just enjoying every bit of the moment."
        "Anna was borderline in pure ecstasy."
        show nippleLickTwo with Dissolve(1)
        play sound jerk
        "She liked the view, Emily licking on her hard, pointy nipple..."
        "That was an amazing sight, Emily always had a way of doing things to Anna..."
        scene 30-3 emily 16 with Dissolve(1)
        "Anna was getting hotter by the moment, starting to drip down there, in the nether regions..."
        "Emily was just going to town on Anna...Not giving her a break, making her sweat for it..."
        "Both of them were getting really nice and hot..."
        "Both of them getting wet and ready..."
        a "Emily, You are amazing at this, Right what I need..."
        "Emily started to multitask... Her hand reaching..."
        play sound heartbeat
        scene 30-3 emily 17 with Dissolve(1)
        play sound jerk
        "...Down in between Anna's legs..."
        "That sent Anna over the edge...Literally, Emily's simple touch made Anna gasp and moan..."
        "She was feeling pleasure that outpaced her conscious mind..."
        "Emily had this technique with her fingers, she just knew how to press Anna's buttons in the right order..."
        "Or was it due to Anna's lowered inhibitions? Was it the trauma that caused her to exhibit more sexuality?"
        "Either way, Anna was in self-induced ecstacy..."
        a "{i}...Emily...Always on top of the game... Ah..."
        a "Ah...Emily... Mfhh..."
        e "Yeah, you like that you dirty slut?"
        a "Yes, Emily...Yes!"
        a "Keep going and don't stop...I'm so close..."
        scene 30-3 emily 18 with Dissolve(1)
        "Anna was taken by pleasure...She moaned loudly as she released her burden..."
        "Emily felt Anna flooding all over her hand..."
        "She felt her orgasming."
        with flash
        a "Ah..."
        play sound jerk
        with vpunch
        a "Oh...my...god..."
        with vpunch
        with flash
        "..."
        a "Mphf...Ah.."
        with vpunch
        scene black with Dissolve(1)
        scene 30-3 emily 19 with Dissolve(1)
        a "Oh, wow... Thank you, Emily, this really released the tension..."
        stop music fadeout 2.0
        e "Whatever I can do for my favorite girl, you know?"
        $ renpy.end_replay()
        play music jazzmusic
        if dianaGoodRelations == False:
            play audio takephoto
            play audio surprise2
            scene 30-3 emily 20-2
            with vpunch
            d "Oh I knew you both were sluts..."
            d "Let me take a photo for the entire office to see...That's enough to end your possibilities of becoming anything else..."
            d "Anything else other than office sluts... Everyone will be pointing fingers at this..."
            d "How is that for the 'hardest' worker, Anna?"
            a "Oh... stupid bitch! Delete it right now, or you will be sorry!"
            d "Dream on, I'm not deleting this jewel!"
            e "Anna, don't...Just let it go... She is not worth it..."
            scene 30-3 emily 21-2 with Dissolve(1)
            d "Yeah, let it go!"
            e "You know we could report you to the police for this?"
            d "Right, have I anything to lose?"
            d "Atleast I will see you fail as well."
            d "I will be sure to make up my mind what to do with this content a bit later."
            scene 30-3 emily 22-2 with Dissolve(1)
            d "Someone around here actually has to do some work!"
            d "Not like you two!"
            d "See you later, office sluts!"
        else:
            scene 30-3 emily 20 with Dissolve(1)
            play sound surprise2
            with vpunch
            "As Anna and Emily were coming down from the hot session..."
            "Diane entered the changing room and saw them both..."
            d "Oh... What's going on in here..."
            scene 30-3 emily 21 with Dissolve(1)
            d "I didn't mean to bother... Sorry to disturb you, ladies..."
            d "Looking good, though."
            e "Diane! Some privacy, please!"
            "Meanwhile, Anna was remembering something about Diane..."
            menu:
                "Oh, I loved that session at my office...":
                    $ dianaSexyTimeOne = True
                    d "Sorry to barge in..."
                    scene 30-3 emily 22 with Dissolve(1)
                    a "Diane! Wait!"
                    d "Huh?"
                    a "It's all right, Diane...Not like you haven't seen my breasts before or anything."
                    d "Right, well, sorry anyway."
                    d "But if the circumstances were a bit different I would even want to join in."
                    a "I know you would."
                    a "I still remember that time when we enjoyed each other's company... I loved it..."
                    scene 30-3 emily 23 with Dissolve(1)
                    d "Really? Thank you, Anna... I enjoyed it too."
                    d "Anyway... You look gorgeous, luscious breasts and amazing curves, as always..."
                    a "Thank you...It's the same with you..."
                    d "Ah, Thanks, Anna."
                    d "Anyway, sorry for keeping you like this..."
                    d "I will get going, Got stuff to do."
                    d "Next time I plan on entering faster, so I don't miss the action.."
                    a "Okh Diane. You sly fox..."
                    e "See you later, Diane."
                    $ relationship_func("Diane Relationship +1, Anna Corruption +1")
                    $ DianeRelationship += 1
                    $ AnnaCorruption += 1
                    jump emilyChangingRoomNext
                "Unfortunate that Diane and I didn't develop a deeper connection":
                    d "Sorry for entering like this."
                    d "I will get going, Sorry again."
                    a "It's okay Diane."
                    d "See you two later."
                    $ dianaSexyTimeOne = False
                    jump emilyChangingRoomNext
label emilyChangingRoomNext:
    if emilyScene1 == False:
        scene 30-3 emily 10 with Dissolve(1)
        if dianaGoodRelations == True:
            e "Since Jeremy is now out of the picture, here is a new outfit for you Anna."
            a "Oh Emily, for me? Thank you so much..."
            a "I can't believe that that's over."
            e "Yeah, neither can I."
            jump emilyChangingRoomThree
        else:
            a "Thank you for the hug, Emily."
            e "No problem. By the way, since you've paid back the money to Jeremy, here is a new outfit for you."
            a "Wow, Thank you, Emily."
            e "Always for you, Anna."
            jump emilyChangingRoomThree
    if emilyScene1 == True:
        scene 30-3 emily 24 with Dissolve(1)
        if dianaGoodRelations == False:
            e "I can't stand that bitch..."
            e "She is always just being so hurtful and mean."
            a "Yeah, it's pretty bad, with her, maybe something can be changed..."
            a "Maybe things would be different if she didn't have to endure Jeremy and others."
            e "I don't think so, it's her choice to be such a bitch to us!"
            a "I guess so."
            a "Hopefully she will get rid of that picture."
            e "If she doesn't there will be hell to pay. For her of course."
        else:
            if dianaSexyTimeOne == True:
                e "Oh, you two looked cute together...hehe..."
                a "Stop it, Emily..."
                e "What? It's not like I just gave you pleasure."
                e "Can't imaging why couldn't she. You know? back at your office? Remember?"
                a "Yeah, I do Emily, no need to shout it out loud..."
            a "I'm glad we were able to put our differences aside and become friends."
    e "Anyway, that was a bit awkward. But stuff happens, you know?"
    a "It's fine, you did an amazing job of releasing the tension, Thank you, Emily."
    scene 30-3 emily 25 with Dissolve(1)
    if dianaGoodRelations == True:
        e "No problem, Anna. And since Jeremy is now out of the picture, here is a new outfit for you Anna."
        a "Oh Emily, for me? Thank you so much..."
        a "I can't believe that that's over."
        e "Yeah, neither can I."
    else:
        e "No problem, by the way, since you've paid back the money to Jeremy, here is a new outfit for you."
        a "Wow, Thank you, Emily."
        e "Always for you, Anna."
    jump emilyChangingRoomThree
    return
label emilyChangingRoomThree:
    scene black with Dissolve(1)
    play music lounge
    play sound equipsound
    pause 2.0
    scene 30-3 emily 26 with Dissolve(1)
    a "Wow, this outfit is very nice... It's a bit sexy, but not too much."
    a "Thank you, Emily. I appreciate it a lot!"
    e "I knew you would like it."
    a "I don't like it, I love it, Emily."
    e "Hehe, well I'm glad that you do."
    scene 30-3 emily 27 with Dissolve(1)
    e "Anyway, I've been thinking, would you maybe want me to redo your hair?"
    a "I don't know, what do you have in mind?"
    e "Let me just do it, I know you will love it, trust me, Anna."
    a "Okay, Emily, I will trust you."
    e "Let me just take a look real quick."
    e "..."
    e "Okay, if I do... If I do that and then that..."
    e "Okay, Anna, sit back, let me do my other type of magic if you know what I mean."
    a "Sure, Emily, hehe."
    scene black with Dissolve(1)
    play sound equipsound
    pause 1.0
    play sound equipsound
    pause 1.0
    scene 30-3 emily 28 with Dissolve(1)
    e "Annnd... There. I'm done, Anna."
    a "Well, I need a mirror, I want to see how it looks. dying of anticipation."
    e "Give me a sec just stand up first."
    a "Okay, Emily...I hope you didn't screw up my hair, hehe..."
    e "I would never..."
    a "I'm just joking, dear."
    e "Oh, I see, hehe."
    scene 30-3 emily 29 with Dissolve(1)
    e "Well... Wow. It looks amazing, Anna."
    a "Really?"
    e "I mean you are talking to a professional."
    a "Sure, Emily...hehe..."
    e "Ok, let's check it out in the mirror."
    a "Alright."
    a "I'm actually nervous."
    e "It's amazing, Anna."
    scene 30-3 emily 30 with Dissolve(1)
    with flash
    play sound surprise2
    with vpunch
    a "Whoa...Emily, the hair is amazing!"
    e "Yeah?"
    a "YES!! I LOVE IT!"
    a "It's absolutely amazing!"
    e "I'm really glad you like it."
    e "Anyway, time for me to get ready for work too."
    scene 30-3 emily 31 with Dissolve(1)
    if emilyScene1 == True:
        a "Well, you kind of did some work on me already, honey."
        e "Hehe, that I did, but that was an enjoyable work."
        e "The rest pays the bills you know?"
        e "Maybe I should start asking you to pay me for doing you, hehe..."
        e "Just kidding, Anna."
    else:
        a "Right, I should also go."
        e "Thanks for sharing the details about Andrew with me, Anna."
        e "I appreciate your honesty and being open with me."
    e "Anyway, Anna, catch you later... good luck with work."
    a "Thanks, dear, you too."
    scene 30-3 emily 32 with Dissolve(1)
    "After Emily left the changing room. Anna was stuck in thought for a moment..."
    "Anna pondered..."
    if emilyScene1 == True and dianaGoodRelations == True and dianaSexyTimeOne == False:
        a "{i}...I hope Diane won't think anything bad of me after seeing what she did..."
        a "{i}...Like I'm some slut. I mean she has seen some stuff but we are in this together..."
    elif emilyScene1 == True and dianaGoodRelations == True and dianaSexyTimeOne == True:
        a "{i}...I wonder if Diane liked what she saw..."
        a "{i}...Perhaps she would be willing to do something more since we had that fun in my office..."
        a "{i}...She is a thoughtful person... And I like her quite a bit..."
    elif emilyScene1 == True and dianaGoodRelations == False:
        a "{i}...I hope Diane deletes those photos. Otherwise, I'm going to be in trouble..."
        a "{i}...That will just add to the list of things that give me a headache..."
    if dianaGoodRelations == True:
        a "{i}...I should probably go to the partners office and understand how things will be from now on..."
    else:
        a "{i}...I should get to my desk and prepare for the workday, Jeremy has probably left some tasks..."
    $ GlossaryUnlockEmily = True
    $ changingRoomDone = True
label officethree:
    if dianaGoodRelations == True:
        jump ethanintroduction
    else:
        jump jeremyEventOne
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
