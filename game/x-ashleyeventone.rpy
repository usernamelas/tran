label PreAshleyEventOne:
    play music tranquility
    scene black with Dissolve(2)
    scene 30-14 home 32 with Dissolve(2)
    a "I should get some sleep, I've been pretty busy."
    if bar_var_1 == True:
        a "The bar fun was crazy..."
    else:
        a "Things got very heated at the bar..."
        a "I hope I won't be in any trouble..."
        a "What exactly happened there? Did all of them get shot? Patrick too?"
        a "I didn't think anyone would get shot..."
        "Anna had alot to think about."
        scene black with Dissolve(2)
        pause 2
    jump AshleyEventOne
label AshleyEventOne:
    scene black with Dissolve(1)
    scene 34-0 morning 1 with Dissolve(1)
    "Anna wakes up after a good night's rest. The previous night had been exhausting."
    "Various different things happened..."
    a "{i}...Another day, another chance..."
    scene 34-0 morning 2 with Dissolve(1)
    a "Damn, I think I slept really hard tonight."
    a "Well, it's understandable. Last night was crazy..."
    a "Feeling a little under the weather... I got kinda drunk last night while working..."
    a "I think all I need is a good coffee and just wake up properly."
label AshleyEventOneContinue:
    scene black with Dissolve(1)
    $ ashley_var_1 = True
    play sound door2
    scene 34-0 morning 3 with Dissolve(1)
    "Anna went out of her room. The morning was beautiful."
    "Everything was ok this morning, no bad dreams, no interruptions. Just peace and quiet."
    a "{i}...I wonder what will happen today..."
    play sound pourwater
    scene 34-0 morning 4 with Dissolve(1)
    "Anna went to the coffee machine and set the setting to her regular."
    a "This is just what I need."
    a "One sugar, black coffee..."
    a "This will definitely give me the good morning wake-up I want and need."
    play sound drinkingBeverage
    scene 34-0 morning 5 with Dissolve(1)
    "She had made the coffee and sat down on the sofa."
    a "{i}...Mmm, So good..."
    a "{i}...I should start every morning like this."
    "She took a big sip of her coffee."
    play sound phonecall
    scene 34-0 morning 6 with Dissolve(1)
    "Suddenly, her phone rang, and her tranquil morning was interrupted."
    "But that sip of coffee was enough to give her energy to answer."
    "It was Ashley."
    a "What? I wonder what he wants..."
    scene 34-0 morning 7 with Dissolve(1)
    a "Hello? Ashley?"
    ash "Hey, Anna. How are you? Doing good?"
    a "Umm, Yeah. What's this about? You don't ever call to just check up on me."
    ash "True, I'm gonna cut to the chase. I have a proposal for you."
    scene 34-0 morning 8 with Dissolve(1)
    menu:
        "Anna feels experimental and goes for it. She has done a lot of things with Ashley in the past.":
            a "Ok. I suppose we can see what you have to offer."
            ash "So. I've got some fans that have become very interested in you, Anna."
            ash "So I made an auction where you were the prize. Or, rather, meeting with you was the prize."
            a "WHAT? You didn't ask me and just did that?"
            ash "Whoa. You haven't heard all of it yet."
            ash "They are willing to pay good money for your time."
            ash "Let's switch to talking through the computer."
            $ ashley_var_2 = True
            $ relationship_func("Ashley Relationship +2, Anna Corruption +3")
            $ AshleyRelationship += 2
            $ AnnaCorruption += 3
            jump AshleyEventOneAccept
        "Anna despises Ashley and doesn't want any part of this.":
            a "Seriously? You are still trying to do some shit?"
            a "NO! Don't call me again!"
            "Anna quickly hangs up the phone..."
            jump AshleyEventOneRefuse

label AshleyEventOneAccept:
    scene 34-0 morning 10 with Dissolve(1)
    ash "Hey. So apologies if I did it on such short notice."
    a "Well, you better have a good reason for me to agree with this."
    ash "Oh, trust me. You're gonna like it."
    a "I will believe it when I see."
    scene 34-0 morning 11 with Dissolve(1)
    ash "I will set up everything, and you will be thrown into a live show with your fans."
    ash "I have made a betting system where people can bet money, and the highest bidder will get a meeting with you."
    a "And what would I have to do."
    ash "Well, I can't say for sure, but probably what he asks of you."
    a "Not a lot of room for choice, from me."
    ash "When you see the amount, you won't want to choose differently."
    a "What do I do?"
    ash "Just read the comments, respond and be sexy about it."
    ash "Act as natural as possible."
    a "Umm... Ok..."
    ash "So you will be live in 3... 2... 1..."
    play music LICityOfAngels
    scene 34-0 morning 12 with Dissolve(1)
    "Anna felt excitement rush through her body."
    "She felt nervous but didn't show it. Hoping that what Ashley said was true."
    "He hadn't been the most trustworthy person, but perhaps she could use it to her advantage now."
    a "Hello... Guys. I'm Anna. Your favorite girl."
    "She had no idea what she was saying or doing, but from the experience of what she had seen on the internet, she imitated other 'cam-girls"
    scene 34-0 morning 13 with Dissolve(1)
    "The chat was going wild. Everyone was so excited to talk with the great, famous Anna."
    "She hadn't expected that many people on the site."
    a "Looks like there a lot of people here. Horny people hehe..."
    a "Well, then tell me what you want from me..."
    scene 34-0 morning 14 with Dissolve(1)
    "Requests poured in:"
    "Show tits, spread your legs, put a dildo in your ass."
    "The depraved and horny men and women of the internet depths were just going crazy with their ideas."
    "Some were decent, some were very, very specific..."
    a "Well, I forgot to mention, like all things in the world, time is money. So whoever bids the highest will get a chance to meet me."
    a "In-person..."
    play sound notificationsound
    scene 34-0 morning 15 with Dissolve(1)
    "Suddenly, a bid came in, and Anna was left in shock."
    "She hadn't expected that much to be on the table already."
    "Previous Anna's shows had helped her become quite famous in these circles."
    a "Well, well. Looks like there is already a decent bid."
    scene 34-0 morning 16 with Dissolve(1)
    "She tried to keep her composure."
    a "Looks like there is a bid for 2000 dollars from carnal_cock115."
    "She decided to push the limits."
    a "We can go higher, can't we? Who wants to see me do whatever they want?"
    a "Come on... Hihi..."
    a "I will give you a bit of incentive."
    play sound undress
    scene 34-0 morning 17 with Dissolve(1)
    "She pulled her shirt a bit to the side and revealed one of her nipples."
    a "Does this make you want to see me do more?"
    a "Do you want to see all of me? Just for you? Your dirty bastards..."
    "The chat was going crazy. Everyone was ecstatic to talk to Anna. Everyone wanted a piece."
    play sound notificationsound
    scene 34-0 morning 19 with Dissolve(1)
    "Then, another bid came in."
    "This time for 3000 dollars."
    a "Oh, we have another excited one on the field."
    a "3000 dollar bid from hard_penetrator54."
    a "You guys definitely want me, don't you?"
    scene 34-0 morning 20 with Dissolve(1)
    "Anna saw the easy potential in getting them to bid more."
    "She decided to spread her legs a bit. It was so easy to gain their confidence and increase bids."
    a "{i}...I can't believe this is working..."
    a "Perhaps you'd like to see more, guys..."
    a "In that case, you know what to do, hehe..."
    play sound notificationsound
    scene 34-0 morning 21 with Dissolve(1)
    "And yet another bid came in."
    "Anna was still surprised about the amounts that people were willing to invest just to get to see her in real life."
    a "Hey, hey. We have another high score here... I like your style, guys."
    "The chatroom was going wild with less fortunate people cursing and blasting the richer men and women who could bet."
    play sound notificationsound
    scene 34-0 morning 23 with Dissolve(1)
    "The latest bid had come in from a user called Futt_bucker4."
    "It was 5000 dollars."
    "Again, Anna was in disbelief, but she didn't choke. She seized the opportunity. Used it to her advantage."
    "If she could earn such easy money without much effort, she could really quickly become able to do whatever she wants."
    a "Whow, there is yet another. Thank you, Futt_bucker. Maybe you will be the lucky one."
    scene 34-0 morning 24 with Dissolve(1)
    a "Or perhaps there is some hidden, yet unreleased potential still in this chatroom."
    "Anna started to lift her legs gradually. She was slightly nervous and embarrassed but also excited about this."
    "Revealing herself to many, many people on the internet."
    a "Perhaps I could give you one last bit of incentive to bid higher to see me."
    play sound jerk
    scene 34-0 morning 25 with Dissolve(1)
    "She spread her legs apart and put her hand in front of her vaginal opening."
    a "Ah... If you bid more, perhaps you will see what's hiding behind door number one... hehe..."
    a "You will see all of me, and maybe even, you will be able to enjoy some of it."
    "She wasn't sure what she was saying, and even if she was willing to do anything when this all comes to pass..."
    "But there was no time to think about that now."
    play sound jerk2
    scene 34-0 morning 27-1 with Dissolve(1)
    "Her pussy was not directly in the camera, her erogenous zone was a bit less covered in light, and her hand was hiding it."
    "Giving the cam room clients the run for their money. They were going wild in the chat."
    "Anna was very effective at getting them riled up. Not showing everything all at once."
    "She had put her fingers in her pussy, and started to thrust lightly."
    scene 34-0 morning 27 with Dissolve(1)
    a "AHH... I wonder who will pay more... Ahh..."
    a "I'm starting to get wet down there..."
    "People in the chat were spamming, asking her to show her pussy, get naked."
    "And that was exactly what she needed to do. Get them so excited..."
    a "Oh... You want to see my pussy?"
    a "But I can't... It's reserved for one special one who bids the highest."
    scene 34-0 morning 28 with Dissolve(1)
    a "I wonder what my pussy tastes like. Would you want to taste my pussy juices?"
    "The chat went even crazier. everyone wanted to get some action with Anna."
    a "Maybe I should put fingers in my mouth, taste what it's like..."
    "Anna was getting pretty excited at this point, too."
    scene 34-0 morning 29 with Dissolve(1)
    a "Aaahh..."
    "She started to suck on her fingers."
    a "Oh... I wonder who will pay more to see me do all of this in real life with them."
    a "And soo much more..."
    a "I'm so wet just thinking about it... Come on... Aahhh, give it to me..."
    play sound notificationsound
    scene 34-0 morning 31 with Dissolve(1)
    "And then..."
    "Someone dropped an entire 10000 dollar bid on the chat. And everything went silent for a moment."
    a "So did Anna. Unable to fully comprehend what just happened."
    "The bid was made by an anonymous client. Who only wrote in the chat:"
    "'I hope our meeting will be pleasant...'"
    "He left, and the chat went Absolutely shitstorm. Everyone was spamming."
    scene 34-0 morning 32 with Dissolve(1)
    ash "Ok, guys. I think we have a winner. That's it for today's bids. Don't forget to come again. When I announce it."
    "Then, Ashley cut the feed."
    a "What the hell was that..."
    a "This is pretty crazy. 10 thousand dollars. I can't believe it..."
    a "I hope it's not going to be anything crazy..."
    scene 34-0 morning 33 with Dissolve(1)
    ash "So. We reached the peak for the first time, I'd say. As soon as I saw the 10k I knew that this was a good time to exit."
    ash "I have the bid locked in and the person's number. This system is made in a way that only when he approves the 10 thousand..."
    ash "Then they will come in. Right now there in escrow. But, I suppose I should call him up and tell him the deets."
    a "Wait. Wait. Are you actually serious? I will have to meet up with him?"
    ash "Yes. That's the deal. But don't worry. He or she probably won't kill you."
    a "Yeah, that's a good vibe setter there, Ash."
    if dianaGoodRelations == False:
        scene 34-0 morning 34 with Dissolve(1)
        ash "Anyway, I will contact you with everything else when I have set up all the other elements of this arrangement."
        ash "Ok?"
        a "I hope you know what you're doing. And I hope I will get paid good money for this shit."
        ash "Trust me, you will. And this is just the beginning if you decide to do it more."
        a "I have to go now. I'm getting a call from my boss."
        if jeremySexContent == True:
            ash "Ah... The Jeremy asshole guy?"
        a "How do you know him?"
        ash "Remember, Anna. I'm pretty good with cameras, info, and what not."
        a "Plus, once I just looked up your firm."
        scene 34-0 morning 35 with Dissolve(1)
        "Anna hesitated to answer the phone."
        "It was, no doubt, about the contract. She was ready to go, just didn't like the answering Jeremy."
        if jeremySexContent == True:
            a "{i}...Him again... Ugh..."
        else:
            a "Ok. Better hear what he has to say."
        scene 34-0 morning 8 with Dissolve(1)
        a "Yes, Jeremy?"
        if jeremySexContent == True:
            j1 "Hello, Anna. I need you to be ready as soon as possible."
            j1 "Don't dawdle around. Prepare and come to the office."
            j1 "We have a contract to finally close today. Understood?"
            a "Yes, Jeremy. Loud and clear."
            j1 "When you get here, get your work documents in order, and the limo will be waiting."
        else:
            j1 "Good morning, are you ready to continue today?"
            a "Yes, I'm good to go."
            j1 "Ok, prepare and come to the office as soon as possible."
            j1 "When you get here, get all your documents in order, and the limo will be waiting."
            a "Ok, I got it."
        "Jeremy hung up."
    else:
        a "Anyway, I have to get going. I have important things to do today."
        ash "I won't hold you, just be ready when the time comes."
        jump AshleyEventOneShower
label AshleyEventOneRefuse:
    if dianaGoodRelations == False:
        play sound phonecall
        scene 34-0 morning 35 with Dissolve(1)
        "Anna hesitated to answer the phone."
        "It was, no doubt, about the contract. She was ready to go, just didn't like the answering Jeremy."
        if jeremySexContent == True:
            a "{i}...Him again... Ugh..."
        else:
            a "Ok. Better hear what he has to say."
        scene 34-0 morning 8 with Dissolve(1)
        a "Yes, Jeremy?"
        if jeremySexContent == True:
            j1 "Hello, Anna. I need you to be ready as soon as possible."
            j1 "Don't dawdle around. Prepare and come to the office."
            j1 "We have a contract to finally close today. Understood?"
            a "Yes, Jeremy. Loud and clear."
            j1 "When you get here, get your work documents in order, and the limo will be waiting."
        else:
            j1 "Good morning, are you ready to continue today?"
            a "Yes, I'm good to go."
            j1 "Ok, prepare and come to the office as soon as possible."
            j1 "When you get here, get all your documents in order, and the limo will be waiting."
            a "Ok, I got it."
        "Jeremy hung up."
    else:
        a "Anyway, I have to get going. I have important things to do today."
        ash "Alright..."
        jump AshleyEventOneShower
label AshleyEventOneShower:
    play sound door2
    play music lounge
    scene 34-1 shower 1 with Dissolve(1)
    "Anna went to the bathroom and decided to take a quick shower."
    "It was a good idea after yesterday's ordeal. A lot had happened."
    if bar_var_1 == True:
        a "{i}...The entire sex scene that everyone saw. I still don't know how I feel about it..."
        a "{i}...I loved it, but... I didn't come. I felt like I should just be used by them and let them cum..."
    else:
        a "{i}...The shooting was very, very sinister..."
        a "{i}...I'm still getting shivers..."
        a "{i}...Was that Jim's plan all along? How could he do something like this..."
        a "{i}...Maybe I should report this?.."
        a "{i}...No... No, I'm already in a lot of trouble as it is..."
    play sound shower2
    scene 34-1 shower 2 with Dissolve(1)
    "Anna got in and washed."
    play sound shower3
    scene 34-1 shower 2-1 with Dissolve(1)
    "The shower was exactly what she needed to wash away all that had happened yesterday."
    "Crazy how everything turned out."
    play sound shower2
    scene 34-1 shower 2 with Dissolve(1)
    a "{i}...Ah... This feels so good..."
    a "{i}...I've got to get ready and head to the office. On a Saturday. Crazy!"
    if bar_var_1 == True:
        scene 34-1 shower 3-1 with Dissolve(1)
        "Anna touched her asshole lightly..."
        "It was still sore from yesterday's fucking with the clients."
        "But she felt good about it..."
        a "{i}...Ah... Easy there, little buddy..."
    play sound shower2
    scene 34-1 shower 3 with Dissolve(1)
    a "{i}...I wonder how the contract closing will go..."
    a "{i}...I hope those men will agree..."
    a "{i}...I wonder what will they ask of me..."
    "Anna's thoughts wondered in the shower."
    "She spent, what felt like, half an hour just thinking about everything."
    scene 34-1 shower 6 with Dissolve(1)
    a "{i}...Ah, such a fresh feeling. I feel much better already..."
    if office_var_two == False:
        a "{i}...I have to prepare and head out. Gotta close that contract..."
        a "{i}...No matter the cost... I've already come this far, might as well go all the way..."
    else:
        a "{i}...I think I got a message from Ethan to meet with the Limo driver and go ask him to take me somewhere..."
    play sound undress
    scene 33 new outfit with Dissolve(1)
    "Anna put on her regular outfit."
    $ ashley_var_3 = True
    if office_var_two == False:
        $ contract_event_1 = True
        jump PreContractEventTwo
    else:
        jump BasemenetEvent
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
