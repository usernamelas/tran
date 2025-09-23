label JeremyEventTwo:
    play sound carsound
    play music PPMCasualReception fadein 0.5
    scene black with Dissolve(1)
    scene 30-2 office annas reception office outfit with Dissolve(1)
    "Anna arrived at work."
    scene 30-6 ethan 8 with Dissolve(1)
    "Anna sat down at her desk and started to sift through the tasks that Jeremy had prepared."
    "She cleaned up the mailbox."
    "And calculated some spreadsheets."
    a "{i}...If I take this cell and use the pie chart, I will be able to show a much better visible representation of the data."
    "She also read the new assistant's dossier."
    "And prepared some tutorial documents for the newcomer."
    a "{i}...I should be prepared for the upcoming teaching session with the newcomer."
    scene 30-6 ethan 9 with Dissolve(1)
    "Anna did some of the tasks and took a quick breather and thought about the new assistant that will be joining them today."
    play audio surprise
    scene 31-2 office 1 with Dissolve(1)
    play audio vibratorsound
    with vpunch
    "Suddenly, Anna started to feel a sensation in her vagina."
    "It was Jeremy's remote vibrator."
    "She instantly started to get flustered and hot."
    "The sensation took her by surprise."
    "Anna was overtaken by pleasure in a short amount of time."
    with vpunch
    scene 31-2 office 2 with Dissolve(1)
    play audio vibratorsound
    a "Umff..."
    "Anna moaned silently. She tried to suppress her feelings."
    a "{i}...Fuck Jeremy... Uhh. But it feels so good."
    "Anna was enjoying the feeling."
    "Even if it was not exactly the way she wanted."
    scene 31-2 office 3 with vpunch
    "Then suddenly it stopped."
    a "Ahh..."
    a "{i}...He stopped... Umf..."
    "Anna was flustered and sweating. It was already enough to make her enjoy herself too much."
    "It only meant one thing though. Jeremy was summoning Anna."
    a "I should go to Jeremy's office and see what he wants from me."
    jump JeremyEventTwoOne
    return

label JeremyEventTwoOne:
    play music tense2
    scene black with Dissolve(1)
    play sound door2
    scene 31-3 jeremy 1 with Dissolve(1)
    "Anna entered Jeremy's office."
    "In Jeremy's office, there was also another girl and Anna was curious as to who it was..."
    a "{i}...Must be the new assistant."
    j1 "Hello, Anna! Looks like the new summoning system is working."
    "Anna was embarrassed by the comment..."
    a "Yes, Jeremy. It works fine."
    j1 "Great, I will be using it every time I will need your assistance."
    scene 31-3 jeremy 2 with Dissolve(1)
    m1 "Hello, it's Anna right?"
    a "Yes, I'm Anna."
    m1 "Nice to meet you, I'm Madison."
    "Anna seemed to like Madison straight away."
    "She was also beautiful, so that would make working with her easier."
    m1 "Madison Carter new assistant to partner Jeremy."
    a "I thought it will be a new guy."
    j1 "There was a change of plans, I believe Ms. Carter is much more experienced and capable."
    a "Right..."
    play sound surprise
    scene 31-3 jeremy 3 with Dissolve(1)
    "Madison leaned in for a friendly kiss."
    "Anna was a bit confused for a moment but didn't really mind Madison's approach."
    a "Nice to meet you too, Madison."
    m1 "I guess you will be the one to teach me today, yes?"
    a "That's right. I will just show you the basics tasks to start you off. Afterward, we will go from there."
    m1 "Great, Thank you."
    scene 31-3 jeremy 4 with Dissolve(1)
    j1 "Anyway, enough with the formalities, ladies."
    j1 "You have both greeted each other. Now it's time to get to your duties."
    m1 "Absolutely, sir."
    a "Yes, Jeremy."
    j1 "I believe both of you know what you have to do. And Anna?"
    a "Yes, what do you want?"
    j1 "When you are done with the basic teaching for Ms. Carter, I will give you hard-copies of the upcoming contracts."
    a "Okay."
    j1 "That is all, go on."
    scene black with Dissolve(1)
    play sound door2
    scene 31-3 jeremy 5 with Dissolve(1)
    $ renpy.music.play("audio/sounds/Purple Planet Music Rendezvous.mp3", channel = 'music', if_changed = True)
    m1 "I'm eager to begin. I believe you will be a good teacher, Anna."
    a "Thanks, sweety."
    a "Anyway..."
    a "Can you tell me more about yourself?"
    m1 "Sure, what do you want to know?"
    default MadisonMenuOne1 = False
    default MadisonMenuOne2 = False
    menu madisonmenu:
        "How did you end up getting this job?" if MadisonMenuOne1 == False:
            m1 "Well, I was looking to get out of my previous workplace."
            m1 "It was not what I was looking for."
            m1 "Plus there was workplace harassment."
            a "Oh. I'm sorry about that."
            m1 "Well, I'm not weak, but I know that I don't have to take a beating."
            a "That's true."
            m1 "Anyway, this seemed promising, has a good salary and nice benefits on top of that."
            a "Oh, Yeah. I can't argue with that."
            a "{i}...If only she knew about Jeremy..."
            a "{i}...I can't tell her, though."
            m1 "Anyway, That's how it went."
            $ MadisonMenuOne1 = True
            jump madisonmenu
        "Tell me a bit more about yourself." if MadisonMenuOne2 == False:
            m1 "Well. I'm originally from here, The Sun city."
            m1 "I've been living here my entire life, traveled a lot, though."
            m1 "Went through school, like the usual lot."
            m1 "Finished studies at Suncity Business and Economics college."
            m1 "Decided not to go for an MBA and just try to climb the corporate ladder on my own."
            a "And how has it been so far?"
            m1 "Well, this is a bit of step down, but I see great opportunity here."
            a "I see, anything exciting like hobbies?"
            m1 "Well, I like to play chess in my free time. I'm a part of the local chess club."
            m1 "I also like to play visual novels in my free time. They are sometimes very intriguing."
            a "Really? I could never get myself in those. Perhaps I should try?"
            m1 "Yes, They are fun. You can also find some more erotic ones if you wish."
            m1 "There is this one about this girl who moves to a new city..."
            a "Right, Perhaps let's continue this some other time. Haha..."
            a "Don't want any colleague to hear us."
            m1 "Hehe... Sure."
            $ MadisonRelationship += 1
            $ relationship_func("Madison Relationship +1")
            $ MadisonMenuOne2 = True
            jump madisonmenu
        "That's all.":
            jump JeremyEventTwoTwo
    return
label JeremyEventTwoTwo:
    scene black with Dissolve(1)
    scene 31-3 jeremy 6 with Dissolve(1)
    "Madison sat down, and Anna leaned in and started to explain things."
    "They were going over things as fast as Anna could show them."
    "Anna thought to herself..."
    a "{i}...Damn, she learns fast... I have to keep up myself..."
    a "You are really good at this."
    m1 "Well, I've done similar work before."
    m1 "I know Excel in and out pretty much."
    a "Of course you do. hehe..."
    a "This will go along smoothly."
    scene 31-3 jeremy 7 with Dissolve(1)
    "They were discussing how to make intricate if functions in excel and how to create complicated data sets."
    a "So if you take this cell and write an if function like this, you will be able to adapt the table to more specific parameters."
    m1 "Oh, I didn't really know that."
    m1 "Thank you."
    a "You are a quick learner, though."
    m1 "Oh, Stop it... You are a good teacher."
    scene 31-3 jeremy 8 with Dissolve(1)
    "From a distance, both Diane and Liam were discussing the new assistant."
    l1 "Look at the new-comer, Diane."
    l1 "Jeremy has, again, outdone himself."
    l1 "First Anna, now this. He somehow just keeps scoring."
    d "Yes, sir, he is very good at his job and gets the best for the job."
    l1 "Yeah, You bet. I wonder what else she is good at."
    l1 "I wonder if she is as good as you and Anna."
    d "It's not my place to judge."
    l1 "Well, I'm telling you, you are perfect, Diane."
    l1 "Perfect for all our 'interesting' times."
    d "Thank you, sir."
    play sound surprise
    scene 31-3 jeremy 9 with Dissolve(1)
    play music tense2
    l1 "Well, well... Welcome to the firm, Madison."
    l1 "Looks like another {i}...toy...{/i} Has been hired."
    m1 "Excuse me?"
    l1 "Nothing, I didn't say anything."
    m1 "And you are..."
    l1 "I'm Liam, one of the partners to the firm, next to Jeremy and Ethan."
    l1 "And you do well to remember that."
    m1 "I will try to do so."
    l1 "Good, if you do what you are told, then you will fit in here very well."
    l1 "By the way, Anna, nice picture."
    play sound surprise
    a "What???"
    l1 "You know what I'm talking about."
    a "*sigh*"
    l1 "Anyway, We are going."
    scene 31-3 jeremy 10 with Dissolve(1)
    "Liam and Diane both went to a meeting and left Anna and Madison confused."
    a "Yeah, well, speaking of harassment, not saying it's prevalent here, but some people are assholes."
    m1 "I guess you can't escape it anywhere."
    a "Yeah, true. Especially that girl, Diane. She is a piece of work."
    m1 "What picture was Liam talking about?"
    a "Don't mind it, it's nothing."
    $ GlossaryUnlockLiam = True
    scene 31-3 jeremy 11 with Dissolve(1)
    m1 "What was that all about anyway?"
    a "Liam thinks he is better than everyone and has a tendency to harass female co-workers."
    m1 "And he hasn't been fired yet?"
    a "Well, all things considered, he does his job well and brings in a good income."
    m1 "That doesn't excuse his actions."
    a "As I said, there are assholes everywhere."
    menu:
        "Tell Madison to do what they say and things will be fine.":
            a "Either way, I would advise you to be compliant."
            a "Even if it doesn't work your way, they will reward you well for doing things their way."
            m1 "I don't know. Anna, if you think it's for the best..."
            a "I do..."
            $ MadisonBrave = 0
            jump JeremyEventTwoThree
        "Tell Madison to be brave and stand against harassement.":
            a "But if you can't stand it, then just tell them, show your point of view."
            a "Don't let them do anything to you."
            m1 "Right, thanks, Anna."
            $ MadisonBrave = 1
            jump JeremyEventTwoThree

label JeremyEventTwoThree:
    scene 31-3 jeremy 12 with Dissolve(1)
    "Anna was wondering if she had covered everything that was needed for Madison to start working."
    m1 "I assume that we might have covered everything?"
    a "Yeah, give me a second, I'm thinking right now."
    a "I think we have, actually."
    a "If I remember anything I will send you an email and necessary tools to do it and will come down to help."
    m1 "Alright Thanks, Anna,"
    play audio surprise
    play sound vibratorsound
    scene 31-3 jeremy 12-1 with vpunch
    "Suddenly, the vibrator went off again."
    "Anna was taken over by pleasure once again."
    "Pleasure she didn't necessarily wish to have but was enjoying nevertheless."
    a "Ah..."
    m1 "Are you okay, Anna?"
    stop sound
    scene 31-3 jeremy 13 with Dissolve(1)
    m1 "You seem kind of flustered."
    a "Ah... I'm... I'm ok."
    m1 "You sure?"
    a "Yeah."
    "The vibrator stopped, and Anna was relieved."
    play sound door2
    scene 31-3 jeremy 15 with Dissolve(1)
    "Jeremy exited his office and approached both ladies."
    j1 "Hello, I guess you two met Liam and Diane?"
    m1 "Yes, They seemed... Very nice..."
    j1 "Is that sarcasm I hear?"
    if MadisonBrave == 1:
        m1 "Yes, he was a bit rude."
        j1 "Excuse me?"
        m1 "That's all I'm saying, sir."
        j1 "Alright, we'll see."
        j1 "{i}...if she is a rowdy one, that will just make things more fun."
        j1 "{i}...I like it when they are harder to break in."
        jump JeremyEventTwoContract
    elif MadisonBrave == 0:
        m1 "No, He was ok, sir."
        j1 "That's right."
        jump JeremyEventTwoContract
label JeremyEventTwoNoSex:
    play sound carsound
    play music PPMCasualReception fadein 0.5
    scene black with Dissolve(1)
    scene 30-2 office annas reception office outfit with Dissolve(1)
    "Anna arrived at work."
    scene 30-6 ethan 8 with Dissolve(1)
    "Anna sat down at her desk and started to sift through the tasks that Jeremy had prepared."
    "She cleaned up the mailbox."
    "And calculated some spreadsheets."
    a "{i}...If I take this cell and use the pie chart, I will be able to show a much better visible representation of the data."
    "She also read the new assistant's dossier."
    "And prepared some tutorial documents for the newcomer."
    a "{i}...I should be prepared for the upcoming teaching session with the newcomer."
    scene 30-6 ethan 9 with Dissolve(1)
    "Anna did some of the tasks and took a quick breather and thought about the new assistant that will be joining them today."
    a "{i}...I hope he is a nice co-worker. Some of them here are not as nice."
    scene 30-6 ethan 8 with Dissolve(1)
    "Suddenly, Anna receive an email from Jeremy to go to his office and greet the new assistant."
    a "Alright, it's time to get going."
    "Anna prepared the rest of the documents and left her office."
    jump JeremyEventTwoNoSexTwo
    return
label JeremyEventTwoNoSexTwo:
    scene black with Dissolve(1)
    play sound door2
    scene 31-3 jeremy 1 with Dissolve(1)
    "Anna entered Jeremy's office."
    "In Jeremy's office, there was Jeremy himself and another lady."
    a "{i}...Must be the new assistant."
    j1 "Hello, Anna. Hope you are getting comfortable in your new place."
    a "Yes, sir. I am."
    j1 "Good to hear."
    scene 31-3 jeremy 2 with Dissolve(1)
    m1 "Hello, It's Anna, right?"
    a "Yes, I'm Anna."
    m1 "Nice to meet you. I'm Madison."
    "Anna seemed to like Madison straight away."
    "She was also beautiful, so that would make working with her easier."
    m1 "Madison Carter new assistant to partner Jeremy."
    a "I thought it will be a new guy."
    j1 "There was a change of plans. I believe Ms. Carter is much more experienced and capable."
    a "Right..."
    scene 31-3 jeremy 3 with Dissolve(1)
    "Madison leaned in for a friendly kiss."
    "Anna was a bit confused for a moment but didn't really mind Madison's approach."
    a "Nice to meet you too, Madison."
    m1 "I guess you will be the one to teach me today, yes?"
    a "That's right. I will just show you the basics tasks to start you off. Afterward, we will go from there."
    m1 "Great, Thank you."
    scene 31-3 jeremy 4 with Dissolve(1)
    j1 "Anyway, enough with the formalities, ladies."
    j1 "You have both greeted each other. Now it's time to get to your duties."
    m1 "Absolutely, sir."
    a "Yes, Jeremy."
    j1 "I believe both of you know what you have to do. And Anna?"
    a "Yes, sir?"
    j1 "When you are done with the basic teaching for Ms. Carter, I will give you hard-copies of the upcoming contracts."
    a "Okay."
    j1 "That is all, go on."
    scene black with Dissolve(1)
    play sound door2
    scene 31-3 jeremy 5 with Dissolve(1)
    m1 "I'm eager to begin. I believe you will be a good teacher, Anna."
    a "Thanks, sweety."
    a "Anyway..."
    a "Can you tell me more about yourself?"
    m1 "Sure, what do you want to know?"
    default MadisonMenuTwo1 = False
    default MadisonMenuTwo2 = False
    menu madisonmenu1:
        "How did you end up getting this job?" if MadisonMenuTwo1 == False:
            m1 "Well, I was looking to get out of my previous workplace."
            m1 "It was not what I was looking for."
            m1 "Plus there was workplace harassment."
            a "Oh. I'm sorry about that."
            m1 "Well, I'm not weak, but I know that I don't have to take a beating."
            a "That's true."
            m1 "Anyway, this seemed promising, has a good salary and nice benefits on top of that."
            a "Oh, Yeah. I can't argue with that."
            m1 "Anyway, That's how it went."
            $ MadisonMenuTwo1 = True
            jump madisonmenu1
        "Tell me a bit more about yourself." if MadisonMenuTwo2 == False:
            m1 "Well. I'm originally from here, The Suncity."
            m1 "I've been living here my entire life, traveled a lot."
            m1 "Went through school, like the usual lot."
            m1 "Finished studies at Suncity Business and Economics college."
            m1 "Decided not to go for an MBA and just try to climb the corporate ladder on my own."
            a "Have you succeeded?"
            m1 "Well, a little, But I've since changed job's a couple of times during the years."
            a "I see, anything exciting like hobbies?"
            m1 "Well, I like to play chess in my free time. I'm a part of the local chess club."
            m1 "I also like to play visual novels in my free time. They are sometimes very intriguing."
            a "Really? I could never get myself in those. Perhaps I should try?"
            m1 "Yes, They are fun. You can also find some more erotic ones if you wish."
            m1 "There is this one about this girl who moves to a new city..."
            a "Right, Perhaps let's continue this some other time. Haha..."
            a "Don't want any colleague to hear us."
            m1 "Hehe... Sure."
            $ MadisonRelationship += 1
            $ relationship_func("Madison Relationship +1")
            $ MadisonMenuTwo2 = True
            jump madisonmenu1
        "That's all.":
            jump JeremyEventTwoNoSexThree
label JeremyEventTwoNoSexThree:
    scene black with Dissolve(1)
    scene 31-3 jeremy 6 with Dissolve(1)
    "Madison sat, and Anna leaned in and started to explain things."
    "They were going over things as fast as Anna could show them."
    "Anna thought to herself..."
    a "{i}...Damn, she learns fast... I have to keep up myself."
    a "You are really good at this."
    m1 "Well, I've working similar things before."
    m1 "I know Excel in and out pretty much."
    a "Of course you do. hehe..."
    a "This will go along smoothly."
    scene 31-3 jeremy 7 with Dissolve(1)
    "They were discussing how to make intricate if functions in excel and how to create complicated data sets."
    a "So if you take this cell and write an if function like this, you will be able to adapt the table to more specific parameters."
    m1 "Oh, I didn't really know that."
    m1 "Thank you."
    a "You are a quick learner, though."
    m1 "Oh, Stop it... You are a good teacher."
    scene 31-3 jeremy 8 with Dissolve(1)
    "From a distance, both Diane and Liam were discussing the new assistant."
    l1 "Look at the new-comer, Diane."
    l1 "Jeremy has, again, outdone himself."
    l1 "First Anna, now this. He somehow just keeps scoring."
    d "Yes, sir, he is very good at his job and gets the best for the job."
    l1 "Yeah, You bet. I wonder what else she is good at."
    l1 "I wonder if she is as good as you and Anna."
    d "It's not my place to judge."
    l1 "Well, I'm telling you, you are perfect, Diane."
    l1 "Perfect for all our 'interesting' times."
    d "Thank you, sir."
    scene 31-3 jeremy 9 with Dissolve(1)
    l1 "Well, well... Welcome to the firm, Madison."
    l1 "Looks like another {i}...Fuck toy whore. {/i} has been hired."
    m1 "Hello, Excuse me?"
    l1 "Nothing, I didn't say anything."
    m1 "You are..."
    l1 "I'm Liam, one of the partners to the firm, next to Jeremy and Ethan."
    l1 "And you do well to remember that."
    m1 "I will try to do so."
    l1 "Good, if you do what you are told, then you will fit in here very well."
    l1 "By the way, Anna, nice picture."
    a "What???"
    l1 "You know what I'm talking about."
    a "*sigh*"
    l1 "Anyway, We are going."
    scene 31-3 jeremy 10 with Dissolve(1)
    "Liam and Diane both went to a meeting and left Anna and Madison confused."
    a "Yeah, well, speaking of harassment, not saying it prevalent here, but some people are assholes."
    m1 "I guess you can't escape it anywhere."
    a "Yeah, true. Especially that girl Diane. She is a piece of work."
    m1 "What picture was Liam talking about?"
    a "Don't mind it, it's nothing."
    scene 31-3 jeremy 11 with Dissolve(1)
    m1 "What was that all about anyway?"
    a "Liam thinks he is better than everyone and has a tendency to harass female co-workers."
    m1 "And he hasn't been fired yet?"
    a "Well, all things considered, he does his job well and brings in good income."
    m1 "That doesn't excuse his actions."
    a "Like I said, there are assholes everywhere."
    menu:
        "Tell Madison to be brave and stand against harassement.":
            a "But if you can't stand it then just tell them, show your point of view."
            a "Don't let them do anything to you."
            m1 "Right, thanks, Anna."
            $ MadisonBrave = 1
            jump JeremyEventTwoNoSexFour
        "Tell Madison to do what they say and things will be fine.":
            a "Either way, I would advise you to be compliant."
            a "Even if it doesn't work your way, they will reward you well for doing things their way."
            m1 "I don't know Anna if you think it's for the best..."
            a "I do..."
            $ MadisonBrave = 0
            jump JeremyEventTwoNoSexFour
    return

label JeremyEventTwoNoSexFour:
    scene 31-3 jeremy 12 with Dissolve(1)
    "Anna was wondering if she had covered everything that was needed for Madison to start working."
    m1 "I assume that we might have covered everything?"
    a "Yeah, give me a second, I'm thinking right now."
    a "I think we have actually."
    a "If I remember anything, I will send you an email and necessary tools to do it and will come down to help."
    m1 "Alright Thanks, Anna,"
    play sound door2
    scene 31-3 jeremy 15 with Dissolve(1)
    "Jeremy exited his office and approached both ladies."
    j1 "Hello, I guess you two met Liam and Diane?"
    m1 "Yes, They seemed... Very nice..."
    j1 "Is that sarcasm I hear?"
    if MadisonBrave == 1:
        m1 "Yes, he was a bit rude."
        j1 "Excuse me?"
        m1 "That's all I'm saying, sir."
        j1 "Alright, we'll see."
        jump JeremyEventTwoContract
    elif MadisonBrave == 0:
        m1 "No, He was ok, sir."
        j1 "That's right."
        jump JeremyEventTwoContract
    return
label JeremyEventTwoContract:
    scene 31-3 jeremy 16 with Dissolve(1)
    j1 "Anyway, I hope you've both been busy and have covered everything for Madison to get to work?"
    a "As far as I remember, yes."
    a "If I come up with anything else, I will send it her way via email."
    j1 "Alright. Because I need Anna right now."
    j1 "We have to discuss certain details regarding contracts."
    j1 "She is now the head of the department, and things go through her."
    j1 "I will also send the contracts your way, Madison. You will have to learn to proofread them as well."
    j1 "Anna will do the work, and when she has checked them, she will send the analysis your way, and you will check and learn from it."
    a "Yes, and if you have any questions, let me know."
    m1 "Will do, Anna. Thank you."
    scene 31-3 jeremy 17 with Dissolve(1)
    j1 "Anyway, here. take a look at these and go through them."
    j1 "The contracts are less beneficial for the counterparty, so I would like you to hide any details regarding the downsides."
    a "Well... I will try to do my best..."
    j1 "I want them on my desk by Friday."
    j1 "We have a lot of work ahead of us."
    a "Will do, sir."
    j1 "If we close these deals properly, we will be in the money, so to speak."
    if jeremySexContent == True:
        j1 "And we will be able to enjoy it. hehe..."
        j1 "And you..."
        a "Right..."
        j1 "And if you do well, you will get a nice cut of the profits."
        a "Thank you, sir."
    else:
        j1 "And then you will be able to get a nice cut of the profits."
        a "Thank you, sir."
    play sound door2
    scene 31-3 jeremy 18 with Dissolve(1)
    "Jeremy left."
    "Anna was thinking about the contracts for a moment."
    a "{i}...Time to get back to work..."
    a "Anyway, Madison, it was nice meeting you. I think we should also go for a little lunch today."
    a "What do you think?"
    m1 "Thanks, Anna, but I still have a bunch of things to set up, my shortcuts and stuff like that. I will skip lunch today."
    a "Alright, then next time we definitely have to go."
    a "And if you need anything, just call me or write me an email. I will try to help as much as I can."
    m1 "Will make sure to do that if I need to."
    a "See you later, sweety."
    m1 "Bye."
    $ GlossaryUnlockMadison = True
    jump JeremyEventTwoAnnaOffice
    return

label JeremyEventTwoAnnaOffice:
    play music PPMCasualReception fadein 0.5
    scene black with Dissolve(1)
    scene 31-3 jeremy 19 with Dissolve(1)
    "Anna sat down at her table and started to read the contracts."
    "She was very focused and went at it for a couple of hours straight."
    scene black with Dissolve(1)
    scene 31-3 jeremy 19 with Dissolve(1)
    "She was very motivated to get the money, so she was looking for any mistake and tried perfect the contracts to the specifications."
    a "{i}...I have the three contracts..."
    a "{i}...One is for Shingzhou corp..."
    a "{i}...One is East Oil Conglomerate..."
    a "{i}...And the last one is for the BBD Mining Inc..."
    a "{i}...Gotta make sure they are all in order..."
    scene 31-3 jeremy 20 with Dissolve(1)
    "She went at it for an hour more and had finally gone through the basics."
    "Anna knew that there was more work to do, but she had made good progress."
    $ ContractProgress = 20
    "Contract Analysis progress: [ContractProgress]%%"
    "Anna decided that it was a good time to go for lunch and invite someone."
    "Anna wondered who she could invite."
    a "{i}...Madison decided to skip today..."
    "Anna decided to invite Timothy."
    play sound undress
    jump timothyEventTwo
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
