
label jeremyEventOne:
    play sound door2
    play music tranquility
    scene black with Dissolve(1)
    scene 30-4 desk 1 with Dissolve(1)
    a "{i}...Alright. I should prepare all the things for work..."
    a "{i}...I hope the boss Jeremy doesn't droll all over the place when he sees me..."
    a "{i}...I should ask him about the promotion..."
    "Anna wondered for a moment about her relationship with Jeremy."
    "Note! This will impact future content with Jeremy."
    menu:
        "Luckily my boss didn't make me do anything that I didn't want to do!":
            $ jeremySexContent = False
            $ relationship_func("Jeremy Relationship +1")
            $ JeremyRelationship += 1
        "I had to do what I had to do, even if I regret it...":
            $ jeremySexContent = True
            $ relationship_func_decrease("Jeremy Relationship -5, Anna Corruption +10")
            $ JeremyBadRelationship += 5
            $ AnnaCorruption += 10
    scene 30-4 desk 2 with Dissolve(1)
    "Anna was working on the tasks that Jeremy had prepared."
    "The usual day-to-day monotone tasks."
    scene black with Dissolve(0.5)
    scene 30-4 desk 2 with Dissolve(0.5)
    a "{i}...So if I do this with the spreadsheet, then it will be more concise and easier to look at..."
    a "{i}...Then I should add this to it so that the overview includes all the charts..."
    scene black with Dissolve(0.5)
    scene 30-4 desk 2 with Dissolve(0.5)
    a "{i}...If I use if statements to accommodate data, then I will get more accurate results..."
    scene 30-4 desk 1 with Dissolve(1)
    a "{i}...Okay. Done with this task, should prep the other documents for Jeremy..."
    scene black with Dissolve(1)
    scene 30-4 desk 3 with Dissolve(1)
    "Anna had been working for a while now and felt a little bit thirsty."
    "Also, she thought that she could take a little break. Looking at the screen took its toll on her."
    a "{i}...I should take a break, stretch a little, get some water..."
    "Anna put aside her tasks for a moment and did a little stretch and went to get some water."
    scene 30-4 desk 4 with Dissolve(1)
    "Anna got up and was pouring water."
    play sound pourwater
    "She was thinking about her tasks as she was doing it."
    "The thought of the promotion also crossed her mind several times."
    if jeremySexContent == True:
        a "{i}...I wish I could get a promotion, then I would escape Jeremy's disgusting, sexual clutches."
    else:
        a "{i}...I wish I could get a promotion. I don't mind working for Jeremy but I can do better."
    scene 30-4 desk 5 with Dissolve(1)
    "She didn't notice that Jeremy had exited his office and had come to Anna."
    "Jeremy on the other hand was enjoying the subtle view."
    "He was also liking her new hair."
    j1 "{i}...Very nice view indeed... yes, yes... And the hair..."
    "Jeremy thought..."
    if jeremySexContent == True:
        j1 "{i}...The hair, oh... She has ways of making me want to enjoy her even more..."
    else:
        j1 "{i}...The hair, oh... I wonder if I could somehow get her though..."
    scene 30-4 desk 6 with Dissolve(1)
    with vpunch
    if jeremySexContent == True:
        a "Hello Jeremy...I didn't notice you, What do you want?"
        j1 "Very nice view Anna, I hope you don't mind if I stare a bit."
        a "{b}*Sigh*"
        a "It's fine, sir."
        j1 "Yes, yes. very nice."
        j1 "But you should pay a bit more attention to your surroundings."
        j1 "All kinds of things could have happened in this time frame, like someone looking at your computer."
        j1 "Seeing some sensitive data."
        a "Oh come on Jeremy, give me a break."
    else:
        a "Oh, Hello sir, I didn't notice you. My apologies."
        j1 "Yes. You should pay a bit more attention to your surroundings."
        j1 "All kinds of things could have happened in this time frame, like someone looking at your computer."
        j1 "Seeing some sensitive data."
        a "Don't be ridiculous."
    j1 "Well, now, now. I have to always be sure that no one is doing anything that could jeopardize our operation here."
    a "Sure, sir."
    scene 30-4 desk 9 with Dissolve(1)
    a "Anyway."
    a "I wanted to ask you about a couple of things If you have the time."
    if jeremySexContent == True:
        j1 "I always have time for you, hehe... if you know what I mean?"
        a "Yes, I do."
        a "But I wanted to ask you about the promotion."
        a "I hope that you haven't forgotten that?"
        j1 "How could I forget, you are my 'hardest' worker here, you know?"
        "Anna got a bit embarrassed."
        scene 30-4 desk 8 with Dissolve(1)
        a "I don't want to talk about it."
        "Jeremy's focus was elsewhere. He didn't even look at her."
        j1 "But I do..."
        j1 "Anyway, No I have not forgotten about your promotion, but we shall discuss this in my office."
        a "Another thing, Jeremy. I wish to know if there are any options for additional work."
        j1 "Ah, Yes. There is something, actually."
        j1 "But we shall discuss that in my office too. First, get me coffee, then we shall get to business, understand?"
        j1 "Oh and make it black and strong this time, yes?"
    else:
        j1 "I have a bit of time, be quick about it though, ok?"
        a "Ok, I wanted to ask you about the promotion, do you still remember?"
        j1 "Yes, I do remember. However, we shall discuss this in my office."
        scene 30-4 desk 7 with Dissolve(1)
        j1 "Anything else?"
        a "Yes, I wonder if you have any additional work that I could help with, any contracts, perhaps, that could use some oversight?"
        j1 "{i}Hmm...I wonder what I could give her...The things I WOULD give her..."
        j1 "Yes, there is something, actually."
        j1 "First bring me some coffee and then we shall discuss both topics, understand?"
        j1 "Oh and add more sugar to the coffee this time, please."
    a "Yes, sir. Absolutely."
    $ GlossaryUnlockJeremy = True
    jump jeremymakeCoffee
    return
label jeremymakeCoffee:
    scene black with Dissolve(1)
    scene 30-4 coffee 1 with Dissolve(1)
    "Anna went to the main office area, it was still early, and only a few people had arrived."
    "Emily was working on her morning routines. Timothy was nowhere to be seen."
    "Everyone else was either in a meeting or absent, for other reasons."
    scene 30-4 coffee 2 with Dissolve(1)
    if jeremySexContent == True:
        a "{i}...He wanted the coffee black and strong this time, better not screw it up..."
        a "{i}...Or maybe I should, maybe even spit in it...No...Better not..."
    else:
        a "{i}...He wanted it with more sugar this time. No problem..."
    scene 30-4 coffee 3 with Dissolve(1)
    play sound pourwater
    a "{i}...Okay, Make it like this..."
    "Anna made the coffee as Jeremy had requested."
    "She thought about making herself one, but rather not make the boss wait on her."
    "Anna thought that..."
    a "{i}...I should try to be on my best behavior to get the promotion that I want..."
    "When the coffee was ready, Anna was ready to take it to Jeremy."
    jump JeremyEventOneTwo
    return
label JeremyEventOneTwo:
    play sound door2
    scene black with Dissolve(1)
    scene 30-5 jeremy 1 with Dissolve(1)
    play music blues fadein 1.0
    "Anna entered Jeremy's office and put the coffee on his table."
    a "Here you go sir, I hope it lives up to the expectations."
    if jeremySexContent == True:
        j1 "It better be. For me, it's really important to get my morning coffee right."
        scene 30-5 jeremy 2 with Dissolve(1)
        j1 "Anna, I think you know not to disappoint me."
        a "Yes, sir."
        j1 "{i}...I need just any reason to have some fun with her..."
        j1 "I'm merely looking for the things that best benefit me, the company, and the partners."
        j1 "Do you understand?"
        a "Perfectly, sir."
        j1 "Anyway, we came here to discuss a couple of topics, not the intricacies of making a good coffee."
        j1 "You said you wanted to get a promotion, yes?"
        a "That's correct, sir."
        j1 "Well, good news, Anna. I will give you the promotion however, That will not come without its strings attached."
        a "Of course, never that easy, is it..."
        scene 30-5 jeremy 4 with Dissolve(1)
        j1 "No! It's not easy!"
        j1 "You understand, that I control all the cards, that I'm in charge?"
        j1 "Do you not?"
        a "I do understand that, sir."
        j1 "Perfect, Well then let me explain how this will go."
        scene 30-5 jeremy 5 with Dissolve(1)
        play sound surprise
        j1 "Since I am in control, I have to keep staying in control."
        j1 "I have to keep my eye on my peers and my inferiors."
        j1 "One of them being you."
        a "What do you mean, keep an eye on me?"
        j1 "Well, I'm glad you asked..."
        j1 "See, I'm not always available to be on the phone or to call you to come to me."
        j1 "I have to keep my eye on you in some...More...Experimental ways..."
        j1 "If you know what I mean."
        a "No, I absolutely don't, sir."
        play sound undress
        scene 30-5 jeremy 6-1
        with vpunch
        j1 "Let me just demonstrate!"
        j1 "I will have to insert a special device in you that will vibrate."
        j1 "When I need you to respond or when you know that you are being summoned."
        j1 "Do you understand?"
        a "No, sir, I don't."
        j1 "You don't seem that bright right now, Anna!"
        a "Cause you are so vague, and from what I have endured from you before, I have no idea what to expect!"
        j1 "Perfect. Then this will come as a surprise."
        play sound surprise
        scene 30-5 jeremy 6
        play music tense2
        with vpunch
        a "What are you doing??!"
        j1 "I'm merely doing what needs to be done to keep my control!"
        j1 "And you will listen and you will obey, because you want that promotion AND you want that additional job opportunity, no?"
        a "Y...Yes...Sir..."
        j1 "Exactly, therefore, I hold all the cards, and I'm also holding this specific device, that I will insert one special place."
        j1 "You will grow to like it as time passes."
        a "I don't... I won't...."
        j1 "Anna, we both know that resistance is futile."
        a "This is not right!"
        j1 "Whatever is best for the company, remember that!"
        play audio surprise2
        play audio jerk
        scene 30-5 jeremy 7
        with vpunch
        "Anna was struggling a bit, but she knew what she had to do to get to the top, even if it was to degrade herself."
        "A small part of her perhaps even enjoyed it?... Her inhibitions are, after all, lowered."
        "Jeremy inserted a remote vibrator in Anna's pussy."
        "Luckily sexual arousal was one of the side effects of Anna's condition. She was moist down there, and the device was easily inserted."
        with vpunch
        j1 "Well, well...Look who is expecting something."
        a "It's not what you think!"
        with flash
        j1 "Looks like it is exactly what I think, Anna."
        j1 "You are dripping all over the floor."
        a "{i}...Keep your composure, Anna..."
        scene 30-5 jeremy 8 with Dissolve(1)
        a "I can't believe you did this."
        j1 "Like I said, it's to summon you when needed."
        a "This is so degrading..."
        j1 "We all have a price to pay if we are to get what we want!"
        j1 "And, yes. You are getting the promotion to team leader."
        j1 "And about the job opportunity, I will send you the necessary information once you get set up at your new place in the main office."
        a "Ok...Sir..."
        a "{i}...Fucking pig..."
        scene 30-5 jeremy 9 with Dissolve(1)
        a "I hope this will be worth my while."
        j1 "If you do as you are asked and do what is necessary, then yes."
        j1 "That includes all kinds of things, hehe."
        j1 "Everything and anything for the best of the company."
        j1 "{i}...We will have fun with this later, hehe."
        j1 "Okay, now go on, set up in your new place."
    else:
        j1 "Let's hope so. We wouldn't want anything to stand in the way of your promotion..."
        j1 "Now would we?"
        a "No, but I don't understand how making a coffee would impact my candidacy for team leaders position?"
        j1 "Well, sometimes the smallest things can have the biggest impact down the road. It's called the butterfly effect."
        scene 30-5 jeremy 2 with Dissolve(1)
        j1 "Anna, I know that you don't much like me, I don't much care either."
        j1 "However, I'm not stupid, and I merely want what's best for me, the company, and its partners."
        j1 "Do you understand the precedent that I'm setting?"
        a "Yes sir, absolutely."
        j1 "Right, therefore I must look for the options that best fit."
        j1 "I'm not saying you don't fit, I'm just saying that you should know what fits."
        scene 30-5 jeremy 3 with Dissolve(1)
        j1 "Anyway, we came here to discuss a couple of topics, not the intricacies of making a good coffee."
        a "Yes, sir. I just wanted to ask whether or not you will give me the promotion that I wish to get?"
        j1 "Right... The promotion. Well, Anna, I have good news for you. I will give you the promotion, no strings attached. I have to admit that you have been a good worker."
        a "Really, sir? Thank you so much!"
        play sound surprise
        scene 30-5 jeremy 10 with Dissolve(1)
        "To her own surprise, she hugged him, even though she didn't like him much."
        j1 "{i}...Wow, I didn't know it meant that much to her. This might increase my chances even more..."
        j1 "{i}...Perhaps I can somehow win her over with good graces..."
        j1 "{i}...She feels so soft and nice... Keep your composure..."
        j1 "All in a day's work, Anna."
        j1 "But know that it won't be easy, things will become harder."
        scene 30-5 jeremy 11 with Dissolve(1)
        j1 "{i}...I hope she warms up to me more, maybe I could take my chances at some point..."
        a "Absolutely sir, I won't fail you or the company."
        j1 "Alright, enough about that. You also asked me about more specialized work?"
        j1 "Yes, I have something that requires special attention, I will send you his dossier and contract, you will look through it."
        a "His?"
        j1 "Yes, since you are not my secretary anymore, I need someone else for the job."
        a "Okay, sir. I will take a look at it at the next possibility."
        j1 "This will be an important first step. You will have to teach him as well, do note that you will only have to do it for the first couple of days."
        j1 "Anyway, that's all, I'll leave you to it. Go to your new work place in the main office."
    j1 "I have some work to do."
    jump officeAnnaOne
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
