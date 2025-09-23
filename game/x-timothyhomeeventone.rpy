label TimothyHomeEventOne:
    $ config.menu_include_disabled = False
    play music tranquility fadein 0.5
    play sound chime1
    scene black with Dissolve(2)
    a "Hey, Timothy it's me, Anna."
    t "Anna! Give me a second I will buzz you in."
    play sound door2
    scene 33-11 tim 1 with Dissolve(1)
    "Anna came by Timothy's place as they had agreed before."
    "Timothy was immediately happy to see Anna."
    a "Hey, Tim. How are you doing? Are you already done with work? It's still the middle of the day."
    t "Hey, Anna! I'm good, yeah. I persuaded the boss to let me leave earlier since I was done with everything..."
    t "So I could prepare for your arrival."
    a "That's thoughtful, Timothy."
    scene 32-11 tim 2 with Dissolve(1)
    t "Sorry, where are my manners..."
    t "Come, sit... How have you been?"
    a "I've been ok. I have some thing's on my mind, you know?"
    t "Got you. I can relate, I guess."
    a "Perhaps you can."
    scene 32-11 tim 3 with Dissolve(1)
    t "Want to share any of the things on your mind?"
    a "I don't want to bother you with my problems."
    t "You wouldn't ever do that, Anna."
    t "I'm genuinely curious."
    a "Well, in that case, another time I will tell you all about it. Right now, I want to spend time with you."
    t "Ok, I got it."
    t "Anyway, you still up for some good food?"
    a "That's always a way to a girl's heart."
    scene 32-11 tim 4 with Dissolve(1)
    "Timothy went to the kitchen and Anna thought about him."
    a "{i}...Timothy's kind and caring, I like that..."
    a "{i}...Not to mention that he's become braver as well..."
    a "{i}...The way he handled the guy in the coffee shop... That was very hot..."
    play sound surprise
    scene 32-11 tim 5 with Dissolve(1)
    a "Oh... Pizza?"
    t "Not just any pizza... I made it myself."
    a "So that was the preparation? How very thoughtful of you."
    t "All the best to you, Anna."
    t "Well, anyway... Let's dig in?"
    a "Won't have to tell me twice, Hehe..."
    scene 32-11 tim 6 with Dissolve(1)
    "Anna took the piece and it looked well done and very classical."
    "She took a bite, and it tasted so flavourful and sophisticated."
    t "I learned this recipe from my mom. A very good cook. Used to work in an Italian pizza place."
    a "Wow..."
    "She was chewing it like crazy. The texture, flavor, dough... Everything was done to perfection."
    scene 32-11 tim 7 with Dissolve(1)
    a "This is the best pizza I've ever eaten... I'm stunned... How did you make it so good? Haha."
    t "I've been practicing for a long time."
    t "I had a lot of time since I didn't go out of the house much... I had difficulty making friends..."
    a "Oh... You told me about it a bit back at the coffee shop. What exactly was going on?"
    t "Well, as I said before, I was bullied a lot... Didn't do much for my self-esteem."
    scene 32-11 tim 6 with Dissolve(1)
    t "The kids picked on me for my size... That lead to all kinds of insecurities about myself and about my body."
    t "I was in a bad place for some time... I almost even had a near-death situation. But my family was supportive of me."
    t "I don't think I want to talk much about that specific moment in my life."
    a "You don't have to, dear."
    t "Anyway..."
    t "Took me many years to really get over it but I've been getting better."
    t "I've started to work out, too. Has helped a lot."
    t "Ever since I met you, I've started to believe that I am worth it and all that... Haha..."
    scene 32-11 tim 7 with Dissolve(1)
    a "Oh, thank you, Timothy. That means a lot to me..."
    a "I'm sorry about your past but lately, I've seen that you have grown a lot."
    a "And you're becoming more confident and all that."
    a "I'm proud of you."
    t "Thanks, Anna... Couldn't do it without you."
    default TimothyHomeQuestionOne = False
    default TimothyHomeQuestionTwo = False
    default TimothyHomeQuestionThree = False
    menu TimothyQuestions1:
        "Do you keep in contact with your family?" if TimothyHomeQuestionOne == False:
            t "Yeah... Occasionally, they insist on keeping an eye on me."
            t "Because they are worried that I will do something bad."
            t "But I don't have the urges anymore."
            a "You have different 'urges' now, hehe..."
            t "Yeah... Haha..."
            t "Anyway, they live in this city so I occasionally visit them and they visit me."
            t "We have a very normal relationship. Nothing special to be honest."
            $ TimothyHomeQuestionOne = True
            jump TimothyQuestions1
        "How did you deal with your problems when you were younger?" if TimothyHomeQuestionTwo == False:
            t "I spent a lot of my time just playing games or watching my mother cook."
            t "She taught me a lot of basics of cooking, like how to cut, slice, all that."
            t "The rest of the time I spent in front of my computer playing games."
            a "I've always liked a good video game."
            t "Yeah, I prepped some for us."
            $ TimothyHomeQuestionTwo = True
            jump TimothyQuestions1
        "Do you talk to any other girls?" if TimothyHomeQuestionThree == False:
            t "Umm... Well... I wouldn't say that."
            t "Back in the day no. Zero..."
            t "But lately I've been trying, you know?"
            a "Oh? That's awesome. And admirable."
            t "Yeah... I've actually gotten some positive reactions, Hehe. So I'm hopeful."
            a "Of course, Timothy! Who wouldn't want a man who can cook such great pizza."
            a "Amongst other {b}GREAT{/b} things... hehe..."
            t "Stop it, Anna... Hah..."
            $ TimothyHomeQuestionThree = True
            jump TimothyQuestions1
        "That's all":
            pass

    t "How about we play some games?"
    a "Sure. What do you have?"
    t "I've got Mortal Kombat 11. Mario Kart 8 Deluxe..."
    play sound surprise
    with vpunch
    a "Mortal Kombat! I am a professional at that game, haha."
    t "Alright, tough talk, eh? Let's see what you got."
    scene black with Dissolve(2)
    play sound lighthit
    "..."
    play sound lighthit
    scene 32-11 tim 8 with Dissolve(1)
    play sound lighthit
    a "Oh... That was a tough punch... But you got nothing on Sub-Zero!"
    t "Trash talk much? Mileena will beat your ass haha!"
    with vpunch
    play sound lighthit
    a "Oh... Oh... I got it, Almoooost!"
    t "NOT YET! I won't give up that easy."
    t "Take That!"
    play audio surprise
    play audio lighthit
    a "I knew you will use that combo! You walked right into my trap!"
    t "What?! Noooo!"
    with flash
    with vpunch
    scene 32-11 tim 9 with Dissolve(1)
    a "YES! I WON!!!!"
    t "Haha... Nice job! But I just let you win, haha..."
    a "Oh, who's a sore loser?"
    t "No but for real, good moves, great game! You are the better player... This time..."
    a "Thanks, Timothy. You are very good, too. It was a pretty difficult fight."
    scene 32-11 tim 10 with Dissolve(1)
    default TimothyHomeQuestionFour = False
    default TimothyHomeQuestionFive = False
    menu TimothyQuestions2:
        "So. Where did you learn to play Mortal Kombat so well?" if TimothyHomeQuestionFour == False:
            t "Well, I have an older sister."
            t "She was the one that paid most attention to me during school."
            t "Always took care of me when I was feeling down. She helped me the most throughout my bad times."
            a "Wow. I never knew you had a sister."
            t "Yeah, she's a great person. I only wish she still lived in the city."
            t "We would conquer the world, but she decided to move out when she got a scholarship outside of the state."
            a "I see."
            t "But I support her fully, I was getting better by that time anyway."
            $ TimothyHomeQuestionFour = True
            jump TimothyQuestions2
        "Do you have big game collection?" if TimothyHomeQuestionFive == False:
            t "Oh, Yeah... Do you want to see it? I've got like 30 games in physical form and like 40 more in digital form."
            a "Wow. That's a lot. Seem like quite the game enthusiast."
            t "Not that much anymore, I spend more time outside now doing some activities."
            a "That's wonderful to hear."
            $ TimothyHomeQuestionFive = True
            jump TimothyQuestions2
        "That's all.":
            pass
    scene 32-11 tim 11 with Dissolve(1)
    "They got up and cleaned the dishes."
    a "Well, this was wonderful. I really enjoyed our time, Timothy."
    t "Yeah me too."
    a "Let's do this again some time. And maybe next time you will teach me how to make the pizza?"
    t "I wouldn't have it any other way."
    "Anna wondered for a moment."
    a "{i}...Should I kiss him?..."
    menu:
        "Yes.":
            play sound surprise
            scene 32-11 tim 12 with Dissolve(1)
            "She quickly leaned in and kissed Timothy."
            "Timothy was surprised, but welcomed it."
            "Not like they hadn't had sex before... But he always was star-struck when anything like this happened."
            "The kiss felt as if time had stopped for a while. There was no sound or any distractions."
            "Just both of them enjoying the simplicity of the moment and the feeling it was giving them."
            scene 32-11 tim 13 with Dissolve(1)
            t "Wow... Anna... Thank you."
            a "No, thank you. I really enjoy your company."
            a "You still don't completely realize how cool you are."
            t "I'm getting there, thanks to you, Anna."
            a "Give yourself credit, as well."
            $ relationship_func("Timothy Relationship +1")
            t "Yes. I will."
            if TimothyHomeQuestionOne == True and TimothyHomeQuestionTwo == True and TimothyHomeQuestionThree == True and TimothyHomeQuestionFour == True and TimothyHomeQuestionFive == True:
                $ TimothyRelationship += 1
        "No.":
            pass
    scene 32-11 tim 14 with Dissolve(1)
    a "Anyway, This was great. I thoroughly enjoyed this. Let's come up with another plan in the near future, alright?"
    t "Yeah. I know where to find you."
    a "Me too."
    a "Take care, Timothy."
    t "Cheers."
    scene black with Dissolve(2)
    play sound door2
    if dianaGoodRelations == False:
        jump JeremyHomeEventOne
    else:
        if BenjaminContent == True:
            a "{i}...I think I shoud visit Benjamin, since I promised him."
            jump BenjaminEventOne
        else:
            a "{i}...I think it's time to head home..."
            jump HomeEventTwo
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
