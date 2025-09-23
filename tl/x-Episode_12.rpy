screen EP12_Emails(received, label_name, email_who, content_message, signature):
    zorder 250
    sensitive (not renpy.get_screen("say"))
    add "images/office/office_imagemap/email_background.jpg"
    frame:
        background None
        xsize 500
        ysize 100
        xalign 0.1
        yalign 0.1
        if received == True:
            text "From: " + email_who size 25 color "#000"
        else:
            text "To: " + email_who size 25 color "#000"
    frame:
        background None
        xsize 1400
        ysize 400
        xalign 0.1
        yalign 0.3
        has vbox
        text content_message color "#000"
        text signature color "#000"
    if received == True:
        imagebutton auto "images/office/office_imagemap/reply_%s.png":
            focus_mask True
            action [Hide("EP11_Emails", transition=Dissolve(1)), Jump(label_name)]
label EP12_Begin:
    $ EP12_var_1 = True
    scene black
    stop music
    show text "{size=+20}Press Space{/size}"
    pause
    if EarlHelp == False:
        $ EP11_var_10 = True
        jump EP12_Sleep_1
    else:
        stop music fadeout 3
        scene black with Dissolve(3)

        play sound interface_sound
        show text "Friday Morning..." with Dissolve(1)
        pause
        jump EP12_Rebecca
label EP12_Sleep_1:
    scene 33-0 morning 0 with Dissolve(1)
    a "Ah... Time to get some sleep."
    "..."
    scene black with Dissolve(1)
    stop music
    play sound interface_sound
    show text "Friday Morning..." with Dissolve(1)
    pause
    scene 33-0 morning 1 with Dissolve(1)
    a "Time to get up..."
    jump EP12_Rebecca
label EP12_Rebecca:
    $ EP12_var_3 = True
    show text "Meanwhile..." with Dissolve(1)
    pause
    play music bythepool
    play sound whoosh_1
    scene 40-2 becca 2 with flash
    if EarlHelp == True:
        m2 "What are we gonna do about the Carl situation?"
        m2 "You know my loyalties lie with Sergey. I've gotta get them out!"
        scene 40-2 becca 3 with Dissolve(1)
        r1 "Are you nuts? You're lucky enough they aren't coming for you."
        r1 "We will have to be smart about this..."
        m2 "Smart?"
        m2 "The only smart ones are in jail."
        r1 "Exactly, all we can do is sit back and hope..."
        m2 "I ain't too good at sitting back."
        r1 "You aren't healed enough yet..."
        r1 "Be patient..."
        scene 40-2 becca 4 with Dissolve(1)
        r1 "Anyway, I've got to run. Gotta keep ourselves afloat now..."
        m2 "Going to Dilan?"
        r1 "Yeah, he's kind of our lifeline..."
        r1 "Later..."
    else:
        m2 "Damn, so they really out of town?"
        r1 "Seems so."
        r1 "Best we keep a low profile, too."
        m2 "What about Anna?"
        scene 40-2 becca 3 with Dissolve(1)
        r1 "Sergey assured me that she's fine, I will talk to her later anyway."
        m2 "Good."
        r1 "You should also stay put."
        m2 "I know, I know. Sergey sent me a message. To rest..."
        m2 "But I ain't that good at sitting still."
        r1 "Hehe... I know..."
        scene 40-2 becca 4 with Dissolve(1)
        r1 "Anyway, I've gotta run. Got myself another opportunity with Dilan."
        m2 "Good, remind him to keep his hands to himself."
        r1 "Hehe..."
        r1 "Later..."
    scene black with Dissolve(1)
    play sound takephoto
    play audio whoosh_1
    scene 40-2 becca 5 with Dissolve(1)
    d3 "Yeah! Just like that!"
    d3 "That's wonderful!"
    play sound takephoto
    scene 40-2 becca 6 with flash
    d3 "You're really good at this!"
    d3 "Wonderful shots!"
    r1 "{i}...I kind of wanna do something more...{/i}"
    scene 40-2 becca 7 with Dissolve(1)
    d3 "Oh, yeah."
    d3 "You are killing it!"
    d3 "Lovely!"
    r1 "You like what you see big boy?"
    d3 "I LOVE IT!!!"
    scene 40-2 becca 7-1 with Dissolve(1)
    d3 "Get on all fours for me please..."
    d3 "I wanna see more cougar-ish seduction!"
    scene 40-2 becca 8 with Dissolve(1)
    r1 "{i}...Hehe... I bet you'd like to bed this cougar...{/i}"
    d3 "So hot!"
    play sound takephoto
    with flash
    d3 "MORE!"
    scene 40-2 becca 9 with Dissolve(1)
    r1 "{i}...I want more action... I wonder if he has any jobs available...{/i}"
    d3 "Just like that!"
    d3 "Lose the top!"
    play sound takephoto
    scene 40-2 becca 10 with flash
    d3 "The clients will love these 'extra' photos!"
    play sound takephoto
    with flash
    scene 40-2 becca 11 with Dissolve(1)
    d3 "Aaannd..."
    d3 "DONE!"
    d3 "We've got a lot."
    scene 40-2 becca 12 with Dissolve(1)
    d3 "I will have plenty to work with. You're good in front of the camera."
    d3 "Always have been."
    scene 40-2 becca 13 with Dissolve(1)
    r1 "Well... speaking of which."
    r1 "I've been meaning to ask you if you've got any jobs?"
    d3 "I do, our regulars."
    r1 "No... I mean, something that pays more?"
    scene 40-2 becca 13-1 with Dissolve(1)
    r1 "Like a..."
    r1 "Porno?"
    d3 "Truly?"
    d3 "Has the time come?!"
    r1 "I think so."
    d3 "I'm so glad to hear it."
    scene 40-2 becca 14 with Dissolve(1)
    d3 "Let me think..."
    d3 "Well, I don't have any solo scenes to offer..."
    d3 "But..."
    scene 40-2 becca 14-1 with Dissolve(1)
    d3 "YES!"
    d3 "There is a scene."
    d3 "Before we continue. What are you willing to do?"
    scene 40-2 becca 15 with Dissolve(1)
    r1 "Well... I'm down for a lot of things, nothing too disgusting."
    d3 "I see. That's fine. I don't do some more... niche fetishes anyway. If you change your mind, though. I have contacts."
    r1 "No, no. I'm good with what you've got."
    scene 40-2 becca 16 with Dissolve(1)
    d3 "Yes... Yes..."
    d3 "Well, like I said, I have a scene available. But it requires a second female."
    d3 "And I haven't found one yet."
    scene 40-2 becca 17 with Dissolve(1)
    d3 "I have a girl coming for a shoot right after you."
    d3 "Do you think you could convince her?"
    r1 "Oh... I don't know..."
    scene 40-2 becca 18 with Dissolve(1)
    r1 "Maybe... I will try my best."
    d3 "That's good to hear."
    scene 40-2 becca 19 with Dissolve(1)
    d3 "Speak of the devil."
    pg1 "Hey, Dilan!"
    d3 "So good to see you, Tanya!"
    d3 "How are you?"
    scene 40-2 becca 20 with Dissolve(1)
    pg1 "Hello, Rebecca!"
    r1 "Hey!"
    pg1 "So, we ready?"
    scene 40-2 becca 21-1 with Dissolve(1)
    d3 "Yeah, I just finished up with Rebecca."
    d3 "Good work!"
    d3 "Tanya? Get ready, you sexy woman!"
    pg1 "You got it!"
    scene 40-2 becca 21 with Dissolve(1)
    r1 "I wanna talk to you about something."
    pg1 "I'm intrigued. Hehe."
    scene 40-2 becca 22 with Dissolve(1)
    pg1 "We can talk about it while dressing. time's money."
    r1 "Sure!"
    scene 40-2 becca 23 with Dissolve(1)
    d3 "Thank you for today, Rebecca. Good luck!"
    r1 "Thanks, see you soon then."
    d3 "Yes, ma'am."
    scene 40-2 becca 24 with Dissolve(1)
    play sound undress
    pg1 "So. Tell me your secret plans."
    r1 "Hehe. Well, not so secret."
    r1 "But... Dilan and I conversed about this scene."
    pg1 "Oh?"
    scene 40-2 becca 25 with Dissolve(1)
    r1 "Well, I don't know how involved you are with the industry..."
    r1 "And how willing you are, but based on your looks... Well..."
    scene 40-2 becca 25-1 with Dissolve(1)
    r1 "Lemme say it straight, you look fucking hot and would you like to do a porn shoot with me?"
    pg1 "Well, well... That's very forward. We barely know each other. I like it, heh."
    r1 "I just know that people would love to see two hot, curvy 'milfs'."
    pg1 "I see."
    play sound undress
    scene 40-2 becca 26 with Dissolve(1)
    pg1 "To answer your previous question. No, I haven't done any porn shoots before."
    pg1 "I really hadn't ever thought about it."
    pg1 "And... I don't think I'm willing."
    pg1 "Regardless of the pay. You see, I've got a husband, I don't want that to get between us."
    scene 40-2 becca 27 with Dissolve(1)
    "Rebecca felt a bit awkward for asking."
    r1 "Emm, it's... It's ok."
    "She quickly tried to figure out who else would be willing..."
    r1 "Well, thanks for letting me know."
    pg1 "Thank you for asking me, if anything changes in the future... We can discuss it."
    r1 "Sure!"
    scene 40-2 becca 28 with Dissolve(1)
    r1 "{i}...Who else...{/i}"
    r1 "{i}...Oh! I know just the person...{/i}"
    play sound whoosh_1
    scene black with flash
label EP12_Work_1:
    $ EP12_var_4 = True
    scene 40-5 work 1 with Dissolve(1)
    "Anna sat down for yet another work day."
    "Anticipating some news with Tombale and BBD mining corporation."
    a "Let's see what we're working with..."
    scene 40-5 work 2 with Dissolve(1)
    a "Ah... I've got an email from Tombale."
    a "Hopefully, they are willing to work with us."
    menu EP12_Work_1_Emails:
        "Email form Tombale.":
            show screen disableClick
            show screen EP11_Emails(True, "EP12_Work_1_Emails_Reply","Tombale@BBDInc.org", "Greetings, Anna. I am profoundly honored that you've reached out to us. The land and the sky will always provide to those who are in need. We would be happy to discuss things. However you will have to go through a sacred ritual before acceptance. Let us know when you have prepared documents and are ready to participate in the ritual.", "Tombale Kanu.")
            pause
            label EP12_Work_1_Emails_Reply:
                hide screen disableClick
                show screen EP11_Emails(False, "None", "aTombale@BBDInc.org", "I'm glad to be hearing from you. I will prepare the documentation and also prepare for the ritual and then we can move on with our business.", "Anna")
                pause
                hide screen EP11_Emails with Dissolve(1)
    a "I wonder what he meant by the ritual... I've got to figure that out..."
    a "Madison could help..."
    scene 40-5 work 3 with Dissolve(1)
    a "Hey, Madison. Could you come up to my office for a second?"
    a "We have some work to do."
    scene 40-5 work 4 with Dissolve(1)
    m1 "Is that regarding a new client?"
    a "Yeah, I could use your help."
    m1 "Understood. Will be there shortly."
    scene 40-5 work 5 with Dissolve(1)
    a "Ritual..."
    a "Huh..."
    a "Alright, well. Gotta keep my eyes and ears open."
    play sound doorknock
    scene 40-5 work 6 with Dissolve(1)
    m1 "Hey. You wanted me?"
    a "Yeah. I've got... Um... I received an email from Tombale."
    m1 "BBD Inc?"
    a "Yeah. We need to find some documentation and legal papers for international mining corporations, more specifically African ones."
    scene 40-5 work 7 with Dissolve(1)
    a "Also... Tombale mentioned a ritual."
    m1 "Oh?"
    a "Yeah, I'm starting to think that they are very traditional and not as technically advanced."
    scene 40-5 work 6 with Dissolve(1)
    m1 "Do we want to touch that even?"
    a "Why not?"
    a "It's not a big deal."
    a "Anyway, legal documentation... I think we can get that with Ethan."
    scene 40-5 work 7 with Dissolve(1)
    m1 "And... Regarding the rituals. Perhaps the city library?"
    a "Yeah! That would work... Alright, let's get to it."
    a "First Ethan, then library."
label EP12_Work_2:
    $ EP12_var_5 = True
    play music PPMWatersideHarmony
    scene 40-5 work 8 with Dissolve(1)
    e1 "Anna."
    e1 "Madison."
    e1 "Good to see you!"
    e1 "How may I be of service?"
    scene 40-5 work 9 with Dissolve(1)
    a "Well. I need some guidance."
    a "I got in contact with BBD Inc."
    a "They are in fact very traditional and not technologically advanced."
    scene 40-5 work 10 with Dissolve(1)
    a "I'm not sure what laws we gotta consider."
    a "I wanted to ask if you could provide us with some cases you have?"
    a "Maybe some pointers?"
    e1 "Hmm..."
    e1 "I think... I can."
    scene 40-5 work 11 with Dissolve(1)
    e1 "Hold on... I think I've got some old paperwork I can give you to check out."
    e1 "Ok... Annd... Also. You'd need the Dunner-Terrence Law Reference Handbook."
    e1 "I'm not sure where I put that, I will send it to Madison, once I find it."
    scene 40-5 work 12 with Dissolve(1)
    e1 "Here. These are some cases from the past that have been collecting dust."
    e1 "There are some things to consider before you jump the rope."
    e1 "Natural conservation laws, the Mid-African treaties and such."
    e1 "I don't remember the details, but these should give you the heads up."
    e1 "We have tried to make dealings with certain 'entities' in the past, but with very little success."
    e1 "As you know, it's often not well regulated. So you got your hands full."
    e1 "Those laws are more for us, to not get sued by governmental bodies."
    scene 40-5 work 13 with Dissolve(1)
    a "Ethan, thank you so much!"
    e1 "Couple that with the Handbook, and you should be able to prepare the documentation with no problem."
    a "I see. The guy I talked to through email also mentioned a ritual."
    e1 "A ritual? Interesting."
    e1 "Well... I know nothing about rituals, but it might be a good idea to drop by the library."
    scene 40-5 work 14 with Dissolve(1)
    a "That's what we were thinking."
    a "Thanks again, Ethan. You are a lifesaver."
    e1 "Oh, think nothing of it."
    e1 "I'm glad to help!"
    jump EP12_Work_3
label EP12_Work_3:
    play music PPMWelcomeToThePlaza
    scene 40-6 library 1 with Dissolve(1)
    "They arrive at the city library."
    a "Hello."
    scene 40-6 library 2 with Dissolve(1)
    li_1 "Greetings, how may I be of service?"
    scene 40-6 library 3 with Dissolve(1)
    a "We are looking for certain books."
    a "Historical ones..."
    a "Umm... Regarding African rituals?"
    scene 40-6 library 4 with Dissolve(1)
    li_1 "Hmm... I think you can find them in the history section."
    li_1 "I remember a book about central African tribe rituals."
    a "Alright, thank you."
    scene 40-6 library 6 with Dissolve(1)
    a "That sounds promising."
    m1 "Sure does."
    a "I'm pretty intrigued, actually. I wonder what kind of ritual it is..."
    m1 "Well, probably some tea ceremony or something like that?"
    scene 40-6 library 7 with Dissolve(1)
    a "Alright. This is it."
    a "Let's get to it."
    a "You take that side, I'll take this side."
    m1 "Gotcha."
    scene 40-6 library 8 with Dissolve(1)
    a "I remember you said you spend your free time reading novels."
    m1 "Yeah. I spend some time in the library looking for something interesting."
    m1 "But... Sometimes I can't find stuff here so I opt for looking on the internet."
    a "Anything intriguing of late?"
    scene 40-6 library 9 with Dissolve(1)
    m1 "Nope, I'm still on the same old novel. They keep coming out with new chapters for it."
    m1 "I'm pretty into it right now."
    a "That's nice, maybe I should read it, too?"
    m1 "Oh. I mean, sure. It gets pretty steamy."
    scene 40-6 library 10 with Dissolve(1)
    a "Hold on..."
    a "Afri..."
    a "Central African Cultures and Rituals Compendium."
    play sound surprise
    scene 40-6 library 11 with Dissolve(1)
    a "Found it."
    m1 "Nice!"
    scene 40-6 library 12 with Dissolve(1)
    a "Let's see. What do we have here."
    a "Alright, I'm pretty sure this has what we need."
    play sound book_open_1
    scene 40-6 library 13 with Dissolve(1)
    a "Letter Z...."
    a "Z... Alright, Zamaru tribe. That's the one."
    a "So... The Greeting of Safu."
    a "It's an ancient ritual performed by the Zamaru tribe when they greet a trader or a traveler from far away lands."
    scene 40-6 library 14 with Dissolve(1)
    a "It is performed as follows:"
    a "1. Safu's Totem. The elders gather with the traveler and kneel before the Safu's Totem."
    a "2. Rising Spirits. The traveler provides the Elders with a gift. Usually, a small pot filled with foreign treats."
    a "3. Safu's embrace. The traveler takes a bath in waters mixed with multiple herbs and spices, and flowers. Then puts on tribal wear provided by elders."
    a "4. Grand Sitting. The elders and the traveler all sit in the main building in silence for several minutes and smell the aromatic air while one of the elders chants songs of the old."
    scene 40-6 library 15 with Dissolve(1)
    m1 "Doesn't sound too bad."
    a "Yeah, I guess We should get a pot and fill it with some treats from here."
    m1 "Yeah, I can do that. I certainly know some very tasty treats."
    scene 40-6 library 16 with Dissolve(1)
    a "Good, that works."
    m1 "You will be the one going, right?"
    a "Yeah, as usual."
    m1 "Sounds like a nice experience. A bath? With petals, herbs, and such?"
    a "Yeah, that could be a different kind of experience..."
    m1 "Did we miss anything?"
    scene 40-6 library 17 with Dissolve(1)
    a "Nope, I don't think so."
    m1 "Awesome, they will be pleased if you come prepared."
    a "Yeah."
    scene 40-6 library 18 with Dissolve(1)
    a "I suppose that's all."
    a "We can get back to the office."
    m1 "Alright, I will head out after work to get the pot and everything."
    scene 40-6 library 19 with Dissolve(1)
    a "Come on. It's work-related. You can do it during work hours."
    m1 "Oh, Anna. You're precious..."
    a "Perhaps you'd like to come with me to the meeting with them?"
    m1 "Oh? I think that would be great!"
    a "Alright, let's get back."
    scene 40-6 library 20 with Dissolve(1)
    a "Thank you for the help. We found exactly what we needed."
    a "The Greeting of Safu."
    a "All 4 steps seemed straight forward and pretty relaxing, in fact."
    li_1 "Glad you found what you needed."
    scene 40-6 library 21 with Dissolve(1)
    "Anna and Madison left..."
    li_1 "All four... Wait... There is a fifth..."
    li_1 "The most interesting one..."
    scene black with Dissolve(1)

label EP12_Work_4:
    $ EP12_var_6 = True
    scene 40-7 work 1 with Dissolve(1)
    a "Alright, that's all finished up."
    a "I will cross-reference the documents that Ethan provided and then draft up the first contract."
    m1 "Alright, sounds good."
    scene 40-7 work 2 with Dissolve(1)
    a "Meanwhile, you can go and prepare those two pots since we both will be going."
    m1 "Will do, Anna."
    a "This is great. I like working with you like this!"
    m1 "Me too. We make a great team."
    scene 40-7 work 3 with Dissolve(1)
    m1 "Do you want me to double-check everything afterward?"
    a "Yeah, I will send you the draft and everything, then you proofread. And then you can send them an email with attachments."
    m1 "That's a plan, then."
    a "Yeah, also notify them that we might be going there during the weekend if they are available."
    m1 "Ok!"
    play sound door2
    scene 40-7 work 4 with Dissolve(1)
    a "Alright... Let's make the draft..."
    scene black with Dissolve(1)
    "Anna spends a couple of hours making the contract..."
    scene 40-7 work 4 with Dissolve(1)
    a "Annd... Sent to Madison for double check... Now I should get on with my day..."
    scene black with Dissolve(1)
    if dianaGoodRelations == False:
        a "I should go to Jeremy..."
        jump EP12_Jeremy_1
    else:
        $ EP12_var_7 = True
        jump EP12_Rebecca_Yoga


label EP12_Jeremy_1:
    $ EP12_var_7 = True
    scene 40-10 jeremy 1 with Dissolve(1)
    a "Hello, sir..."
    a "Wanted to see me?"
    j1 "Yes."
    j1 "We have several things to discuss..."
    a "Where were you during the quarterly?"
    scene 40-10 jeremy 2 with Dissolve(1)
    j1 "Heh... Well... I was preoccupied."
    play audio whoosh_1
    play sound clappingcheeks loop
    scene 40-10 jeremy 4 with flash
    play audio femmoan
    sl_1 "Aahhh!!!"
    j1 "Yeah! Take it!"
    j1 "I'm fucking cumming!!!"
    with flash
    play sound cum_sound
    scene 40-10 jeremy 5 with Dissolve(1)
    with flash
    j1 "AAH!"
    j1 "I'm filling up your nasty holes!"
    sl_1 "AAhh... Fill me up, Daddy!"
    j1 "FUUUCK!"
    scene 40-10 jeremy 6 with Dissolve(1)
    scene black with Dissolve(1)
    scene 40-10 jeremy 7 with Dissolve(1)
    porn1 "So... When are you bringing your girl here?"
    if jeremySexContent == True:
        j1 "Don't you worry about it."
        j1 "I will eventually."
        j1 "Just get me what I need and we're settled. Understood?"
    else:
        j1 "I thought I made it clear that she won't take it."
        j1 "Thus I've changed my strategy. Perhaps someday."
        j1 "Just keep patient, we have other ones..."
    porn1 "Sure..."
    scene 40-10 jeremy 8 with flash
    a "Care to elaborate? I had to completely prepare the quarterly by myself..."
    if jeremySexContent == True:
        j1 "Non of your business. I knew you would have it under wraps."
    else:
        "I can't disclose that, sorry. I knew you'd manage."
    a "I almost missed it."
    j1 "But you didn't... It was a success!"
    j1 "Anyway."
    j1 "We have a meeting with the mayor today."
    j1 "You're coming with me."
    a "Oh?"
    j1 "Yeah... Limo's waiting."
    scene black with Dissolve(1)
    scene 40-10 jeremy 9 with Dissolve(1)
    a "So... Why are we meeting with him?"
    j1 "Well. I have business with him."
    j1 "You are still my direct subordinate, thus I'm taking you with me."
    a "Even if I am, I often feel out of the loop."
    scene 40-10 jeremy 10 with Dissolve(1)
    j1 "I don't pay you for being in the loop, I pay you for appearances."
    j1 "As you should already know."
    a "What is that supposed to mean."
    if jeremySexContent == True:
        j1 "You are eyecandy."
        j1 "Know your place!"
    else:
        j1 "As much as don't like using that, people find you visually appealing."
        j1 "Thus you will help with my business dealings."
    scene 40-10 jeremy 11 with Dissolve(1)
    a "I see..."
    j1 "Yes, and if all goes well, we'll get more business, more money, more power."
    a "That's what you're after?"
    j1 "Aren't we all?"
    scene black with Dissolve(1)
    play sound door2
    play music tense2
    scene 40-10 jeremy 12 with Dissolve(1)
    j1 "Richard!"
    md_1 "Jeremy!"
    md_1 "You lousy ass. Come in!"
    j1 "Good to see you. Keeping in shape I see?"
    scene 40-10 jeremy 13 with Dissolve(1)
    j1 "This is Anna. The company's upcoming talent."
    md_1 "Aahh... I See."
    md_1 "Are you here to discuss business, both of you?"
    a "Yes, sir."
    scene 40-10 jeremy 14 with Dissolve(1)
    md_1 "Well, I'm glad to see you, Anna."
    md_1 "How you've been?"
    a "I'm ok. Keeping busy."
    md_1 "Ahhh... No doubt, Jeremy usually has a lot of work for his employees."
    a "I suppose."
    scene 40-10 jeremy 15 with Dissolve(1)
    "There was a slight nuance in the air. As if Anna was unsure of what exactly were those two talking about."
    "But, she wasn't dumb anymore. She had a bad feeling about this."
    "Was it yet another of Jeremy's schemes?"
    md_1 "Sorry, where are my manners, sit... Sit."
    play sound undress
    scene 40-10 jeremy 16 with Dissolve(1)
    md_1 "That's better."
    md_1 "So... Jeremy. What's the play."
    j1 "Well, as we discussed prior, I have prepped the documents and they are ready to be sent over."
    j1 "Before that you wanted some guarantees."
    j1 "Here we are."
    scene 40-10 jeremy 17 with Dissolve(1)
    md_1 "Here you are, indeed."
    md_1 "I think we'll do very good business."
    play sound jacketcloth
    scene 40-10 jeremy 18 with Dissolve(1)
    j1 "You should know by now, I always come through."
    md_1 "You are right. I will be awaiting the documents."
    j1 "Good."
    md_1 "So, Anna."
    scene 40-10 jeremy 19 with Dissolve(1)
    md_1 "I see a prosperous future upon us."
    md_1 "How long have you been working with Jeremy."
    a "Uh... For some time..."
    "Anna felt uneasy as Mayor's hands touched her..."
    scene 40-10 jeremy 20 with Dissolve(1)
    "She looked at Jeremy with some disbelief."
    "But she understood that Jeremy was always scheming. This was just the latest in a long line."
    if jeremySexContent == True:
        "Anna realized that where she had gotten was not because of no choice, but because she actually enjoyed it."
        "Some part of her... Liked the idea of being used..."
        "A part she fought adamantly, yet it was futile nonetheless..."
    play sound surprise
    scene 40-10 jeremy 21 with Dissolve(1)
    md_1 "Yes..."
    md_1 "Wonderful, wonderful..."
    a "{i}...He is definitely talking about me...{/i}"
    md_1 "Contract signings are always my favorite."
    j1 "Well, I know how to pick them."
    scene 40-10 jeremy 22 with Dissolve(1)
    md_1 "Aint that the truth."
    md_1 "This might be the best one yet."
    a "I..."
    md_1 "Don't... Ruin the moment."
    md_1 "I dislike when women talk."
    scene 40-10 jeremy 23 with Dissolve(1)
    md_1 "Well then."
    md_1 "I believe we both have some work to do, I have seen what I need to see."
    j1 "Good. What do you think?"
    md_1 "If I wasn't clear already, this one will do perfectly."
    if jeremySexContent == True:
        a "{i}...I... I think I like being used like this...{/i}"
    scene 40-10 jeremy 24 with Dissolve(1)
    j1 "Anyway, here is the first part..."
    j1 "I will send the second part as soon as I get home."
    md_1 "Seems fair."
    md_1 "Don't keep me waiting!"
    j1 "Yes, sir."
    scene 40-10 jeremy 25 with Dissolve(1)
    md_1 "I can't wait for the signing..."
    a "The signing?"
    j1 "Yes, that will be quite an endeavor at our place..."
    md_1 "I think we are done here, for now, I've got a meeting with a young ambitious journalist."
    md_1 "Let's see how ambitious she is, hehe."
    j1 "Good one. Haha."
    scene black with Dissolve(1)
    play sound carsound2
    scene 40-10 jeremy 9 with Dissolve(1)
    if jeremySexContent == True:
        a "I hope I did what was needed?"
        j1 "Yes..."
        "Anna wasn't even reluctant any more, she accepted her part in the play and moved on."
        "Perhaps that was the best way..."
    else:
        a "What the hell was that?"
        a "I thought I'd made it very clear that this won't work."
        j1 "I'm sorry, Anna... But this is for the betterment of the company."
        j1 "We will figure something out, but I had to keep up appearances."
        a "Don't make me regret this."
    scene 40-10 jeremy 10 with Dissolve(1)
    if jeremySexContent == False:
        j1 "As I said, we'll figure it out. I'm sorry he groped you, but I hope we won't have to take it further."
        a "What exactly is the contract?"
        j1 "I can't say... Not yet."
        a "If you let me in on the secret, I might be able to help."
        j1 "I'll think about it."
    else:
        j1 "All I will say is this. There will be a contract signing."
        j1 "You will be part of it..."
        a "..."
    scene black with Dissolve(1)
    jump EP12_Rebecca_Yoga
label EP12_Lenny_Scene:
    $ EP12_var_9 = True
    "Anna changed into something nicer and went out to meet Lenny..."
    play ambience city_traffic
    play music chill_song_6
    scene 40-1 lenny 1-1 with Dissolve(1)
    a "Hey!"
    le1 "Anna! You actually came."
    le1 "I guess you liked our previous encounter after all..."
    "Anna thinks to herself:"
    menu:
        "{i}...I just liked the money...{/i}":
            pass
        "{i}...Yeah, he was pretty cute and wholesome...{/i}":
            pass
    scene 40-1 lenny 1 with Dissolve(1)
    le1 "You look stunning, to be honest!"
    a "Thanks, hehe..."
    scene 40-1 lenny 1-2 with Dissolve(1)
    le1 "How are you doing today?"
    "There was a bit of awkwardness in the air."
    a "I'm good, I'm good. just had work, that's about it."
    a "You?"
    scene 40-1 lenny 1-3 with Dissolve(1)
    le1 "Oh, I've been prepping all day. I can mostly work when I want to."
    a "Really?"
    le1 "Yeah, I'm pretty lucky in that sense."
    le1 "Well, lucky to have you here as well!"
    le1 "So, shall we?"
    scene black with Dissolve(1)
    stop ambience
    play sound door2
    scene 40-1 lenny 2 with Dissolve(1)
    le1 "I'll quickly say, though, my friends... They are a kind of jerks."
    le1 "Buut... They are the cool, rich people of the town. I get a lot of benefits from that."
    scene 40-1 lenny 2-1 with Dissolve(1)
    a "Don't worry, I'm on your side."
    a "Got your back."
    le1 "Wow... That's awesome, haha!"
    scene 40-1 lenny 3 with Dissolve(1)
    le1 "I'm a bit nervous... Fuck it. Introductions."
    scene 40-1 lenny 3-1 with Dissolve(1)
    le1 "Anna... These are my friends."
    le1 "Trina, Parker, Rico, Dustin."
    scene 40-1 lenny 4 with Dissolve(1)
    du4 "Well, well..."
    du4 "Look who turned up!"
    scene 40-1 lenny 5 with Dissolve(1)
    le1 "Hi, guys."
    le1 "This is Anna."
    a "Hi everybody."
    "Under his breath, Dustin commented to Rico."
    du4 "Look at that chick, wtf..."
    ri1 "Word. She's a straight 10."
    play sound jacketcloth
    scene 40-1 lenny 6 with Dissolve(1)
    a "Oh..."
    scene 40-1 lenny 7 with Dissolve(1)
    pr1 "Hello, Anna. I'm Parker."
    a "Hey."
    pr1 "Nice to meet you."
    "They seemed friendly enough."
    "But mostly everyone was nice to Anna..."
    scene 40-1 lenny 8 with Dissolve(1)
    pr1 "Come, sit."
    scene 40-1 lenny 9 with Dissolve(1)
    pr1 "So, you want anything, water, coffee?"
    a "Not in particular."
    le1 "Yeah, Me neither."
    pr1 "Right..."
    scene 40-1 lenny 10 with Dissolve(1)
    "Trina was eying Anna up and down."
    tr1 "{i}...Damn, she's so gorgeous. I wonder if that will make my position here unstable...{/i}"
    tr1 "{i}...I've been fucking these dudes for money for a while... Can't have them looking at another girl...{/i}"
    play music blues
    scene 40-1 lenny 11-1 with Dissolve(1)
    ri1 "So. How's life, Lenny."
    ri1 "Looks like you moving up in the world."
    ri1 "Got yourself a girlfriend and all."
    du4 "Come on. That ain't his girlfriend."
    du4 "Lenny could never pull a girl like that, right Anna?"
    scene 40-1 lenny 11 with Dissolve(1)
    menu:
        "No! I am here because I'm interested.":
            a "He's funny, and doesn't judge."
        "Well, Yeah... I suppose":
            a "But... I don't know..."
    du4 "I know I've seen you somewhere, that's what I'm saying. Imma find the place. Gimme a sec."
    le1 "Cut it out, Dustin!"
    scene 40-1 lenny 12-1 with Dissolve(1)
    tr1 "Don't mind him. He's an asshole, always has been."
    tr1 "Always trying to get under people's skins."
    du4 "Suure... I definitely got in somewhere, yesterday."
    scene 40-1 lenny 12 with Dissolve(1)
    a "It's ok. Haha."
    if DilanPornContent == True:
        scene 40-1 lenny 13 with Dissolve(1)
        du4 "Shiit. I found it. I knew I'd seen you somewhere."
        du4 "Take a look at this pic, Rico."
        scene 40-1 lenny 14 with Dissolve(1)
        du4 "Damn, I definitely fapped to this shit."
        du4 "How many pornos have you been in?"
        a "Oh, well..."
        scene 40-1 lenny 15 with Dissolve(1)
        du4 "Just look at that bod."
        ri1 "Dude, Right..."
        pr1 "Haha."
        scene 40-1 lenny 16 with Dissolve(1)
        a "It's just a... side thing..."
        a "I came here of my own interest."
        du4 "Riight, he probably bought you before, though."
        du4 "He told us about your first date."
        du4 "I know he couldn't land a girl like you."
    else:
        scene 40-1 lenny 16 with Dissolve(1)
        du4 "Well, I couldn't find it."
        du4 "Anyway..."
        du4 "What I'm trying to say is..."
        du4 "No way Lenny could land a girl like you."
    scene 40-1 lenny 16-1 with Dissolve(1)
    a "Nonsense."
    scene 40-1 lenny 17 with Dissolve(1)
    "Lenny became increasingly sad..."
    "He was very embarrassed..."
    "Thinking it was a mistake..."
    scene 40-1 lenny 17-1 with Dissolve(1)
    "He tried his best argument."
    le1 "You... You don't know that..."
    le1 "She's different..."
    scene 40-1 lenny 18 with Dissolve(1)
    le1 "Right?"
    scene 40-1 lenny 19 with Dissolve(1)
    "Anna was conflicted about it all..."
    a "I..."
    du4 "See, dude. she doesn't care..."
    scene 40-1 lenny 20 with Dissolve(1)
    pr1 "All we're asking is that you admit that you couldn't land this girl, Lenny."
    pr1 "Be real with yourself."
    scene 40-1 lenny 21 with Dissolve(1)
    tr1 "Come on guys, he's not that bad. He is pretty funny..."
    scene 40-1 lenny 22 with Dissolve(1)
    du4 "Yeah, funny to laugh about. Haha!"
    play sound surprise2
    scene 40-1 lenny 23 with vpunch
    le1 "You are... More evil than usual, Dustin... Why?"
    le1 "Why bother me like this?"
    scene 40-1 lenny 24 with Dissolve(1)
    du4 "Maaan... Cause you a pathetic ass, fat, ugly ass dude."
    le1 "..."
    scene 40-1 lenny 25 with Dissolve(1)
    le1 "Alright... I'm... I'm just going to get some air."
    du4 "You do that, the cool people will hang out!"
    scene 40-1 lenny 26 with Dissolve(1)
    a "Wait... Don't go..."
    pr1 "Just go, dude. Anna will be fine here with us."
    scene 40-1 lenny 27 with Dissolve(1)
    "Lenny could barely hold his emotions together."
    "The first hand humiliation he had to endure..."
    "Just to fit in..."
    scene 40-1 lenny 28 with Dissolve(1)
    a "Hold on, Lenny!"
    a "It's ok!"
    scene 40-1 lenny 29 with Dissolve(1)
    du4 "You're still trying to act all good?"
    du4 "Like, come on."
    du4 "We are all rich here. Why do you think he spends a bunch of money to fit in with us?"
    menu:
        "Anna decides to tighten with Lenny's friends a bit.":
            $ EP12_Choose_Lenny_Friends = True
            scene 40-1 lenny 30 with Dissolve(1)
            a "Well... I just like to have fun."
            du4 "Right, and who will have more fun, us? Or you with him?"
            du4 "Stick to your crowd, let the good times roll."
            du4 "I want a pic, you know. I'm a fan..."
            a "Alright..."
            scene 40-1 lenny 31 with Dissolve(1)
            play sound takephoto
            with flash
            du4 "Awesome!"
            scene 40-1 lenny 32 with Dissolve(1)
            "Dustin was holding Anna tightly, fantasizing about getting in her panties..."
            "And Anna was maybe even willing to..."
            scene 40-1 lenny 33 with Dissolve(1)
            du4 "How about I give you my number, we could all hang out sometime."
            du4 "Have some real fun."
            scene 40-1 lenny 33-1 with Dissolve(1)
            du4 "What do you say?"
            du4 "We know the best spots in the city."
            scene 40-1 lenny 34 with Dissolve(1)
            a "Sure... Why not."
            a "I will go check up on him anyway."
            du4 "Sure, sure. Just know who you'll have more fun with..."
        "Anna scolds his friends.":
            a "Even if it was something to do with money, you guys, are trash."
            a "I can't believe you would be so mean to someone like that."
            du4 "Damn... Chill out! I was just joking."
            a "Sure... Douche!"
    play sound high_heels_walking
    scene 40-1 lenny 36 with Dissolve(1)
    pause 0.5
    scene 40-1 lenny 37 with Dissolve(1)
    pause 0.5
    scene 40-1 lenny 38 with Dissolve(1)
    a "You ok?"
    le1 "Wha..."
    le1 "Lenny felt absolutely destroyed..."
    stop music fadeout 3
    scene 40-1 lenny 39 with Dissolve(1)
    "But then, Anna, a flicker of light in his world, turned up."
    "He saw her beautiful body... She was here, in front of him, not there with those guys..."
    play music chill_song_4
    scene 40-1 lenny 40 with Dissolve(1)
    le1 "Oh... Hey..."
    le1 "Sorry about that. We were just joking around..."
    le1 "We usually do that."
    scene 40-1 lenny 41 with Dissolve(1)
    a "Come on, don't lie. That was awful what they did."
    menu:
        "Tell me, why do you let them do that to you?":
            $ EP12_Help_Lenny = True
            play sound notificationsound
            $ renpy.notify("Lenny appreciates that.")
            a "And be honest."
            le1 "I mean..."
            scene 40-1 lenny 42 with Dissolve(1)
            le1 "They are pretty popular... They know the best clubs and stuff..."
            le1 "If I hang out with them, I get together with the crowd, which raises my chances of getting a hookup."
            le1 "Maybe even find a girl who's interested in me."
            scene 40-1 lenny 43 with Dissolve(1)
            a "Honestly, hanging out with these people, you will only find toxicity."
            le1 "I don't know..."
            a "Question. How many girls have you gotten since hanging out with them?"
            le1 "Well... None..."
            scene 40-1 lenny 44 with Dissolve(1)
            a "The thing is, they only use you. You give them free money, probably some other benefits."
            a "Someone to laugh at..."
            scene 40-1 lenny 45 with Dissolve(1)
            le1 "Yeah... Maybe you're right..."
            le1 "Maybe I should stop hanging out with them..."
            a "Yeah..."
            a "Anyway..."
        "But enough about that... Come here.":
            pass
    scene 40-1 lenny 46 with Dissolve(1)
    a "How about I sit here..."
    le1 "You mean... Uhh..."
    "Lenny was smitten. With such a woman in front of him..."
    scene 40-1 lenny 47 with Dissolve(1)
    le1 "Sure..."
    play sound cloth_sound1
    scene 40-1 lenny 48 with Dissolve(1)
    a "Let's forget about all that ordeal for a moment, alright?"
    le1 "Yeah... That's a good idea."
    le1 "I... I've never seen such a hot woman..."
    a "Heh... I'm one of a kind..."
    scene 40-1 lenny 49 with Dissolve(1)
    le1 "Yes... Yes, you are."
    a "It will be ok. You've got this, Lenny."
    le1 "Damn..."
    scene 40-1 lenny 50 with Dissolve(1)
    "Anna tried to make Lenny feel a bit better."
    "Unpredictable of Anna and how she feels in different situations."
    le1 "Such nice material..."
    "Anna allowed Lenny to grope her for a bit. To make him feel better..."
    scene 40-1 lenny 51 with Dissolve(1)
    pause 2
    scene 40-1 lenny 52 with Dissolve(1)
    a "You like that?"
    le1 "I... I do... Yeah. So much..."
    a "{i}...His hands seem so careful... Slow...{/i}"
    "Anna liked what he was doing..."
    play sound undress
    scene 40-1 lenny 53 with Dissolve(1)
    le1 "Wow..."
    scene 40-1 lenny 54 with Dissolve(1)
    a "Hey! That's a bit too far..."
    a "Can't go there..."
    scene 40-1 lenny 55 with Dissolve(1)
    le1 "What? I'm... I'm sorry..."
    le1 "But... You are so beautiful... So hot..."
    le1 "Surely I can..."
    scene 40-1 lenny 56 with Dissolve(1)
    a "{i}... I might've taken it too far...{/i}"
    "She felt reluctant to stop and just leave him like this. She felt sorry for him... But..."
    scene 40-1 lenny 57 with Dissolve(1)
    a "I..."
    scene 40-1 lenny 57-1 with Dissolve(1)
    le1 "Hey... I... I can pay you..."
    le1 "I will give you 1 thousand dollars if you let me grope you... 1 more if you do something with my..."
    le1 "You know, with the thingy down there..."
    a "{i}... He would give me 2k total if I just do some light stuff?...{/i}"
    a "{i}...It's not even full on sex...{/i}"
    "Anna couldn't understand what she wanted to do..."
    scene 40-1 lenny 58 with Dissolve(1)
    a "I... well..."
    menu:
        "Anna liked him, but she wasn't going to do it for free, yet.":
            $ Lenny_Relationship += 3
            a "Sure..."
            le1 "Yeah?"
            le1 "Awesome..."
            le1 "You are great..."
            pass
        "Anna realized that she didn't like him at all, but she definitely wanted the money.":
            $ Lenny_Relationship += 1
            a "Sure..."
            le1 "Yeah?"
            le1 "Awesome..."
            le1 "You are great..."
            pass
        "Anna refused to do those things...":
            $ EP12_Lenny_Refuse_Sex = True
            a "Nope... I'm sorry, but you can't buy me like that..."
            le1 "Well... Ok..."
            le1 "I won't press you."
            a "Good..."
            a "I... I will leave now..."
            le1 "Uhmm... Ok..."
            scene black with Dissolve(1)
            call EP12_Logic_Gate from _call_EP12_Logic_Gate
label EP12_Lenny_Sex_Scene:
    scene 40-1 lenny 59 with Dissolve(1)
    a "Well... I could give you something to enjoy..."
    le1 "Wonderful!"
    "Anna could see how his mood switched in an instant."
    play sound jacketcloth
    scene 40-1 lenny 60 with Dissolve(1)
    le1 "Ohh... So smooth."
    le1 "You are truly amazing, you know?"
    a "I know..."
    "Anna had heard this so many times at this point..."
    scene 40-1 lenny 61 with Dissolve(1)
    le1 "What do we have here?"
    scene 40-1 lenny 62 with Dissolve(1)
    le1 "Wow..."
    "Lenny had been hoping for a moment such as this..."
    le1 "Lemme just..."
    scene 40-1 lenny 63 with Dissolve(1)
    "His body was so excited, he could barely contain himself."
    "He could feel the vagina through the panties..."
    scene 40-1 lenny 64 with Dissolve(1)
    "That made him even crazier about her."
    le1 "It's... That pussy..."
    scene 40-1 lenny 65 with Dissolve(1)
    a "Ah..."
    a "{i}...He's... Inexperienced... Yet he's so into it..."
    "Lenny enjoyed Anna's emotions."
    play sound jacketcloth
    scene 40-1 lenny 66 with Dissolve(1)
    pause 0.5
    scene 40-1 lenny 67 with Dissolve(1)
    a "You like this?"
    scene 40-1 lenny 68 with Dissolve(1)
    le1 "I... I..."
    a "Hehe... Don't worry..."
    scene 40-1 lenny 69 with Dissolve(1)
    a "You can touch, if you'd like."
    "Lenny knew it was money well spent the moment he first met her..."
    scene 40-1 lenny 70 with Dissolve(1)
    a "{i}...Ohh... He seems hesitant... Awkward even...{/i}"
    a "{i}...But... He's made me a good offer...{/i}"
    a "{i}I kind of like that he's inexperienced...{/i}"
    scene 40-1 lenny 71 with Dissolve(1)
    le1 "Amazing..."
    le1 "Lemme just touches that nipple..."
    a "It's... sensitive, but... Sure. Be gentle."
    le1 "Yes, Anna."
    play sound femmoan
    scene 40-1 lenny 72 with Dissolve(1)
    le1 "You like that?"
    a "Oh..."
    "Lenny tried his best, but he was still a bit too rough."
    a "Ye... Yeah..."
    play sound femmoan_3
    scene EP12_Lenny_Anim_1 with Dissolve(0.5)
    le1 "Anna... Oh, Anna..."
    le1 "{i}...Even if I'm paying her...{/i}"
    le1 "{i}...It's worth it... Maybe she likes me, too...{/i}"
    scene 40-1 lenny 73 with Dissolve(1)
    le1 "No breasts like these..."
    scene 40-1 lenny 74 with Dissolve(1)
    le1 "Would you do something more for me?"
    a "I agreed to it, didn't I?"
    le1 "Well... Yeah..."
    play sound woman_hmm_1
    scene 40-1 lenny 75 with Dissolve(1)
    a "What is it that you'd like, Lenny?"
    le1 "I... My... Thing..."
    play sound undress
    scene 40-1 lenny 76 with Dissolve(1)
    le1 "It's been hard ever since you came on the balcony."
    a "Well, well..."
    scene 40-1 lenny 77 with Dissolve(1)
    le1 "Would you..."
    a "Heh... I sure can..."
    play sound cloth_sound1
    scene 40-1 lenny 78 with Dissolve(1)
    pause 0.5
    scene 40-1 lenny 79 with Dissolve(1)
    a "Just sit back... And relax..."
    le1 "Sure!"
    scene 40-1 lenny 83 with Dissolve(1)
    a "Could you remove those pants for me?"
    a "So I can see it fully?"
    le1 "Yes, Anna!"
    play sound undress
    scene 40-1 lenny 85 with Dissolve(1)
    a "It's... Really big..."
    le1 "Thank you..."
    a "The girls that reject you don't know what their missing out on."
    a "I bet they would wanna get fucked hard by this cock."
    scene 40-1 lenny 86 with Dissolve(1)
    a "You like the view?"
    play sound jerk2 loop
    scene EP12_Lenny_Anim_3 with Dissolve(0.5)
    le1 "I can barely believe it."
    le1 "Fuuck... Those hands..."
    a "{i}...He's been nothing but nice to me, too...{/i}"
    a "{i}...It makes it easier for me to do this...{/i}"
    a "{i}...Ah... His cock is really big, too...{/i}"
    scene 40-1 lenny 87 with Dissolve(1)
    le1 "{i}...I just wish she liked me back as I like her...{/i}"
    le1 "{i}I would marry the fuck out of her...{/i}"
    scene EP12_Lenny_Anim_2 with Dissolve(1)
    a "{i}...His face is full of pleasure...{/i}"
    a "{i}...I like it when somebody enjoys my handiwork...{/i}"
    a "Ah... You like this?"
    le1 "Mh... Yeah..."
    "Anna looked at his cock again..."
    scene 40-1 lenny 88 with Dissolve(1)
    a "It's... Enthralling..."
    le1 "Huh... Ah... Your hands do things to my cock, that I've never felt before..."
    scene 40-1 lenny 89 with Dissolve(1)
    a "How about something more?"
    "Anna tried to be a bit more direct... Take a lead as Lenny's personal 'escort'..."
    a "Perhaps I can enhance the view?"
    a "And give you something you will really remember?"
    le1 "I remember every moment I've spent with you."
    play audio undress
    scene 40-1 lenny 90 with vpunch
    le1 "WHOOAOAA!"
    a "Now... Where were we?"
    a "Oh, right..."
    a "You will like this."
    scene 40-1 lenny 91 with Dissolve(1)
    le1 "I... I... FUCK YEAH!"
    a "{i}...Hehe... I like it when people enjoy it this much...{/i}"
    scene 40-1 lenny 92 with Dissolve(1)
    "The view was amazing... Lenny just watched... Trying his best to keep his mind in the moment."
    "It was gonna pass eventually, but not before he had enjoyed it fully."
    play audio femmoan_4
    scene EP12_Lenny_Anim_5 with Dissolve(1)
    le1 "Oh... Yeah... Don't change anything... Continue like this..."
    le1 "{i}...Fuck she's good...{/i}"
    scene EP12_Lenny_Anim_4 with Dissolve(1)
    "Lenny tried his best not to lose focus and cum..."
    "But the titties were making it increasingly hard..."
    scene 40-1 lenny 93 with Dissolve(1)
    le1 "Ah... Them tits are so good."
    a "Have you had a titty job before?"
    le1 "Well... No..."
    a "Hehe..."
    a "I bet you love it."
    scene 40-1 lenny 94 with Dissolve(1)
    a "Want some more?"
    le1 "Yeah!"
    a "{i}... It's not even that bad to suck his cock...{/i}"
    a "{i}...It doesn't smell bad like some other's that I've sucked...{/i}"
    a "{i}...And he's nice about it...{/i}"
    scene 40-1 lenny 95 with Dissolve(1)
    a "Alright... Just lay back..."
    a "I'm 100 percent sure you'll love this..."
    a "My lips on your cock..."
    le1 "Really?!"
    a "Yeah..."
    scene 40-1 lenny 96 with Dissolve(1)
    "She looked at him for a moment."
    "Lenny couldn't handle the hotness she was exerting..."
    scene 40-1 lenny 97 with Dissolve(1)
    a "MMmm..."
    scene 40-1 lenny 97-1 with Dissolve(1)
    le1 "Ooohhh..."
    "Anna could see his cock twitching in front of her..."
    "Ready to be sucked..."
    "Waiting for it..."
    play sound jerk3 loop
    scene 40-1 lenny 98 with Dissolve(1)
    pause 1
    play audio sucking_1
    scene 40-1 lenny 99 with Dissolve(1)
    pause 1
    scene EP12_Lenny_Anim_8 with Dissolve(0.5)
    "Anna started off with just the tip..."
    le1 "mmhh... Those liips..."
    le1 "Just what I wanted..."
    "The man was completely under Anna's control..."
    pause
    scene EP12_Lenny_Anim_6 with Dissolve(0.5)
    le1 "Oh shit!"
    le1 "Ahh..."
    "Lenny immediately felt sensation rise by a factor of 10x."
    le1 "OOooh... That mouthh...."
    "Anna was inclined to help him out, since he was paying her handsomly."
    a "{i}...Mhmm... His cock filling up my mouth nice and full...{/i}"
    "Anna didn't mind being used as Lenny's personal cum-dumpster..."
    pause
    scene EP12_Lenny_Anim_6_Faster with Dissolve(0.5)
    le1 "Ooh...AAAHH!"
    le1 "Fuck you're good..."
    a "Mhm..."
    le1 "{i}...I should try and wife her up before anyone else does...{/i}"
    pause
    scene EP12_Lenny_Anim_7 with Dissolve(0.5)
    "Lenny could feel the sensation rising with every second..."
    "He was unable to hold for much longer..."
    "He didn't want to either..."
    pause
    scene EP12_Lenny_Anim_7_Faster with Dissolve(0.5)
    le1 "Oh fuck... I'm getting really close, Anna..."
    "Anna just kept sucking and sucking..."
    a "{i}...Hehe... I bet he can't hold it anymore...{/i}"
    le1 "Anna!"
    with flash
    a "Fuck!"
    with flash
    menu:
        "Cum in her mouth.":
            with flash
            le1 "Oh fuck!!!"
            with flash
            le1 "I can't hold it!"
            play sound cum_sound
            scene 40-1 lenny 100 with flash_vpunch
            a "MMMM!!"
            a "{i}...Ahh... He is filling my stomach full of his sperm!...{/i}"
            a "{i}...But I love it...{/i}"
            "Lenny didn't even give Anna a heads up..."
            "He just couldn't contain his semen."
            "Loaded her mouth right up!"
            scene 40-1 lenny 102 with Dissolve(1)
            a "Ahh..."
            "Anna tried to swallow most of it."
            scene 40-1 lenny 103 with Dissolve(1)
            pause 1
            scene 40-1 lenny 104 with Dissolve(1)
            a "Ah."
            scene 40-1 lenny 105 with Dissolve(1)
            a "How was that?"
            le1 "If I didn't need time to recover after cumming, I'd wanna go again!"
            a "Is that so?"
            le1 "Yeah..."
        "Cum on Anna's pretty face.":
            with flash
            le1 "Oh fuck!!!"
            with flash
            le1 "I can't hold it!"
            "Anna pulled off of it."
            "Just before the explosion!"
            stop audio
            play sound cum_sound
            scene 40-1 lenny 107 with flash_vpunch
            "She didn't have time to react..."
            "And all of it got on..."
            scene 40-1 lenny 108 with flash
            pause 0.5
            scene 40-1 lenny 109 with flash
            pause 0.5
            scene 40-1 lenny 111 with Dissolve(1)
            "Her face..."
            a "AH!!"
            a "{i}...I'm covered in his semen...{/i}"
            menu:
                "Anna liked to be covered in men's cum.":
                    a "That's so hot... Ah..."
                "Anna was disgusted...":
                    a "Ah... I have to wash it off..."
            a "Lemme just clean up..."

    scene 40-1 lenny 112 with Dissolve(1)
    le1 "Heh... Damn... I want more."
    a "I bet you do."
    le1 "Would you do it again in the future?"
    le1 "If I pay you?"
    scene 40-1 lenny 113 with Dissolve(1)
    a "Perhaps..."
    a "Depends on the amount."
    le1 "Hehe... Trust me, there's more where that came from."
    play sound jacketcloth
    scene 40-1 lenny 114 with Dissolve(1)
    a "Did you enjoy yourself?"
    le1 "Did I?"
    le1 "As far as my first time goes..."
    scene 40-1 lenny 115 with Dissolve(1)
    a "First time?"
    a "Can't call it that exactly, we haven't fucked."
    le1 "Well... A blowjob is great, too."
    scene 40-1 lenny 116 with Dissolve(1)
    le1 "This was so hot."
    le1 "Not even in my wildest dreams."
    a "I'm glad to hear."
    play sound cloth_sound1
    scene 40-1 lenny 117 with Dissolve(1)
    a "Well... I guess, we get back to the party?"
    le1 "Umm..."
    le1 "I think I'm good..."
    menu:
        "Anna recommended Lenny to be naughty.":
            a "You can tell your 'friends' what I did... They might get jealous."
            a "If you wanna brag to them later, by the way..."
            a "You can tell them..."
            le1 "Wha?"
            a "Tell them how this hot slut sucked you off."
            le1 "I... Yeah... Sure."
        "Anna recommended Lenny to be discreet.":
            a "Please don't tell them about any of this."
            a "If you wanna hang out with them, that's your business."
            a "I wouldn't do it if I were you."
            le1 "I'll think about it."
    le1 "I hope we can do this again in the future?"
    scene 40-1 lenny 118 with Dissolve(1)
    le1 "Please, please?"
    a "Hmm... Well..."
    a "I'll think about it."
    le1 "Awesome."
    le1 "Anyway."
    scene 40-1 lenny 119 with Dissolve(1)
    le1 "Here's what I promised."
    a "{i}...That's a lot of money...{/i}"
    $ renpy.end_replay()
    $ persistent.scene_35 = True
    play sound notificationsound
    $ MoneyVar += 2000
    $ renpy.notify("+2000$")
    a "Well... Thanks."
    le1 "It was a pleasure."
    a "I'm sure. hehe..."
    scene 40-1 lenny 120 with Dissolve(1)
    a "I appreciate it."
    le1 "Me too... This was one of a kind experience."
    le1 "Remember to keep me in mind, eh?"
    scene 40-1 lenny 121 with Dissolve(1)
    "Anna was a bit conflicted about just straight selling herself for money."
    "But was it that different from filming porn?"
    scene 40-1 lenny 122 with Dissolve(1)
    le1 "Shall we?"
    a "Yeah."
    play sound door2
    scene 40-1 lenny 123 with Dissolve(1)
    "They got back into the apartment..."
    le1 "Well... I don't know what to tell them."
    a "I will be heading out, you'll stay?"
    le1 "Naah."
    scene 40-1 lenny 124 with Dissolve(1)
    pr1 "Well, well... You got better?"
    pr1 "Did she talk you down?"
    pr1 "From being a big baby?"
    scene 40-1 lenny 125 with Dissolve(1)
    le1 "Yeah."
    le1 "Anyway. I will be going."
    le1 "It was a pleasure..."
    le1 "Not really..."
    a "Bye!"
    scene 40-1 lenny 126 with Dissolve(1)
    le1 "Wow... I might not talk to them anymore... Will see..."
    a "It won't be a big deal if you don't. They didn't really bring anything to the table."
    le1 "Fair enough."
    le1 "Thanks for today... I appreciate it."
    scene 40-1 lenny 127 with Dissolve(1)
    a "Sure, Lenny."
    a "I have to thank you, too..."
    a "You did give me quite a lot of... stuff..."
    le1 "More where that came from..."
    a "I'll keep that in mind."
    scene 40-1 lenny 128 with Dissolve(1)
    le1 "Well... This is me."
    le1 "See you around."
    a "Take care, for now, Lenny."
    menu:
        "Give me a call when you feel like spending some money on me, hehe...":
            le1 "Definitely!"
        "Give me a call when you feel like meeting up.":
            le1 "Will do."
    call EP12_Logic_Gate from _call_EP12_Logic_Gate_1
label EP12_Bar_1:
    play music PPMSoftShoeShuffle
    $ EP12_var_12 = True
    play sound surprise
    scene 40-3 patrick 1 with Dissolve(1)
    a "Hey guys!"
    da "Anna. Good to see you, Good to see you!"
    a "You ever leave this place?"
    da "Not if I can help it."
    scene 40-3 patrick 2 with Dissolve(1)
    j3 "Hey, Anna!"
    j3 "Good to see you."
    scene 40-3 patrick 3 with Dissolve(1)
    a "Yeah! So what's up?"
    a "Came in as soon as I could."
    scene 40-3 patrick 4 with Dissolve(1)
    j3 "Well, not much today... I think. Patrick wanted to discuss something, and asked me to call you in urgently."
    a "Ugh..."
    a "I don't like the sound of that."
    j3 "Naah. Don't worry. He seemed in a good mood today."
    a "Right..."
    scene 40-3 patrick 5 with Dissolve(1)
    da "I'm in a good mood."
    da "I will treat you good, Anna."
    a "haha... I know, David."
    a "How is Ethan?"
    scene 40-3 patrick 6 with Dissolve(1)
    da "Better than ever!"
    da "Keeps his pa off the streets."
    da "I mean. What more could I ask for?"
    a "Awesome."
    a "I'll get going."
    da "Don't let me keep you!"
    scene 40-3 patrick 7 with Dissolve(1)
    a "Later!"
    play sound door2
label EP12_Bar_2:
    play music tense2
    scene 40-3 patrick 8 with Dissolve(1)
    "Anna entered Patrick's office."
    a "{i}...I really hope he's in a good mood...{/i}"
    scene 40-3 patrick 9 with Dissolve(1)
    pa "Anna. Come in!"
    pa "My jackpot has come in."
    pa "Take it as a compliment."
    a "Sure, thanks."
    pa "How would you like to make more money?"
    scene 40-3 patrick 10 with Dissolve(1)
    a "Elaborate?"
    pa "Well... We could increase the stakes."
    pa "I've been planning and thinking a lot."
    pa "You are one of our best assets."
    a "I suppose."
    scene 40-3 patrick 11 with Dissolve(1)
    pa "I've been thinking of changing things around here."
    pa "We've already been on a natural course towards that."
    a "Ok?"
    pa "I would like you to trailblaze this idea."
    scene 40-3 patrick 12 with Dissolve(1)
    a "Well, what is it?"
    a "{i}...I don't like this...{/i}"
    pa "I would like to start selling sexual favors here."
    play sound surprise
    scene 40-3 patrick 13 with Dissolve(1)
    pa "And you could be the test bunny."
    a "What?"
    pa "I mean. you are the epicenter of all the nasty, naughty, depraved shit that keeps happening here..."
    pa "People've been asking."
    a "I..."
    scene 40-3 patrick 14 with Dissolve(1)
    pa "Just think about it."
    pa "The money."
    pa "Trust me. They would pay well..."
    pa "So... What do you say?"
    pa "I made a new menu and added some extra services to it..."
    menu:
        "I... Will do it...":
            $ EP12_Bar_Sexual_Services = True
            scene 40-3 patrick 15 with Dissolve(1)
            a "I suppose I don't have a choice..."
            pa "Well..."
            pa "If you wanna keep your job here..."
            a "I see..."
            scene 40-3 patrick 16 with Dissolve(1)
            pa "The thing is... You will do it."
            pa "And you will keep doing it."
            pa "Cause you're fucking addicted."
            scene 40-3 patrick 17 with Dissolve(1)
            pa "Keep that in mind."
            pa "Go get changed."
            a "Yes, sir."
            pass
        "I won't do it!":
            pa "That's a shame..."
            pa "Alright... Go get changed..."
            pass

    stop music fadeout 3
    scene 40-3 patrick 18 with Dissolve(1)
    a "{i}...Fuck... I keep getting myself into this...{/i}"
    scene 40-3 patrick 19 with Dissolve(1)
    a "{i}...Maybe I do enjoy it...{/i}"
    scene black with Dissolve(1)
    play sound door2
    play music chill_song_2
    scene 40-3 patrick 20 with Dissolve(1)
    a "Where is my outfit."
    a "Ah... Right..."
    scene 40-3 patrick 21 with Dissolve(1)
    a "There..."
    a "Same as previously."
    a "I hope it will be satisfactory..."
    scene black with Dissolve(1)
    play sound jacketcloth
    scene 40-3 patrick 22 with Dissolve(1)
    pause
    a "Well, I like how sexy I look in it."
    scene 40-3 patrick 23 with Dissolve(1)
    a "Alright... Time to get ready."
    play sound door2
    scene black with Dissolve(1)
    play ambience bar_ambience_1
    play music bar_song_1
    scene 40-3 patrick 24 with Dissolve(1)
    ga "Hey, Anna."
    ga "Heard you've got a big day ahead of you?"
    a "Heh... Yeah... I guess..."
    scene 40-3 patrick 25 with Dissolve(1)
    ga "Good luck to you."
    a "Thanks."
    ga "If you wanna get some extra, you know where to find me."
    a "Nice try, bozo."
    scene 40-3 patrick 26 with Dissolve(1)
    j3 "Anna!"
    a "Yeah?"
    j3 "Good to see you ready and able."
    a "Very funny."
    j3 "You do look good, though."
    scene 40-3 patrick 27 with Dissolve(1)
    j3 "So."
    j3 "Just walk around the bar."
    a "Get the orders."
    scene 40-3 patrick 28 with Dissolve(1)
    a "Right, the usual."
    j3 "Yep. Nothing more, nothing less..."
    scene 40-3 patrick 28-1 with Dissolve(1)
    if EP12_Bar_Sexual_Services == True:
        a "Riiight..."
        a "Patrick didn't tell you?"
        j3 "What?"
        a "He made a new menu with some 'extra' stuff..."
        j3 "Oh... He gave it to me, I didn't read it though..."
        a "Well... I agreed."
        j3 "You did?"
        scene 40-3 patrick 29 with Dissolve(1)
        j3 "Huh..."
        j3 "Makes sense. You've been our best asset so far."
        a "I guess."
        scene 40-3 patrick 30 with Dissolve(1)
        j3 "Well... Just do what you do best then."
        j3 "I'll be here if you need me."
        a "He didn't tell you?"
        j3 "Nope... Odd..."
    scene 40-3 patrick 31 with Dissolve(1)
    j3 "Anyway. You've got clients waiting. Get to work."
    j3 "Plenty of them."
    j3 "One seems pretty crazy for you."
    scene 40-3 patrick 33 with Dissolve(1)
    a "Huh?"
    j3 "Over my left shoulder."
    j3 "He's been sitting here anticipating you ever since arriving."
    play sound surprise2
    scene 40-3 patrick 32 with Dissolve(1)
    "The man looked stunned when seeing Anna."
    "Like a fan..."
    a "{i}...Jeez... He's absolutely wordless...{/i}"
    scene black with Dissolve(1)
label EP12_Bar_3:
    scene 40-3 patrick 34 with Dissolve(1)
    a "Hello, sir."
    a "What would you like to order today?"
    scene 40-3 patrick 35 with Dissolve(1)
    bc_1 "Oh, hey! You are one sexy bartender."
    bc_1 "And that outfit... Checks all the boxes for me."
    scene 40-3 patrick 36 with Dissolve(1)
    a "Thank you, heh."
    a "What can I say? I'm a full package."
    a "So, what'll it be?"
    scene 40-3 patrick 37 with Dissolve(1)
    bc_1 "I'll have a lager, please."
    a "Sure thing, hon."
    a "I will get it to you soon."
    bc_1 "Don't keep me waiting."
    scene black with Dissolve(1)
label EP12_Bar_4:
    scene 40-3 patrick 39 with Dissolve(1)
    a "Good evening, mister."
    bc_2 "Damn, the smoke show..."
    bc_2 "How do you do?"
    scene 40-3 patrick 40 with Dissolve(1)
    a "I'm wonderful, and you?"
    bc_2 "Even better now. Hah!"
    bc_2 "You'd make anyone's day better."
    a "{i}...They seem nice enough...{/i}"
    scene 40-3 patrick 40-1 with Dissolve(1)
    a "So what would you like?"
    a "We've got new cocktails, new arrival beers."
    scene 40-3 patrick 41 with Dissolve(1)
    bc_2 "I'll have a Lager... You guys got the best beer in town."
    a "Sure, sir."
    scene black with Dissolve(1)
label EP12_Bar_5:
    scene 40-3 patrick 42 with Dissolve(1)
    a "Greetings. How may I serve you."
    scene 40-3 patrick 43-1 with Dissolve(1)
    bc_3 "Oooh... Anna... I'm... I'm your biggest fan!"
    a "Really?"
    if DilanPornContent == True:
        bc_3 "I've watched all volumes of your... Um..."
        bc_3 "Adult films..."
        a "Oh?"
        bc_3 "Yeah... You are the best we've ever had. Like no one stands close."
        bc_3 "Not even Donna Mystique."
    else:
        bc_3 "Yeah, your work here is great!"
    a "Haha..."
    a "Thanks."
    scene 40-3 patrick 43 with Dissolve(1)
    bc_3 "Anyway. I'd... I'd like a cocktail."
    bc_3 "Sunset Dreams."
    a "Alright."
    scene 40-3 patrick 44 with Dissolve(1)
    a "I'll see what we can do, sir."
    bc_3 "Thaaankss!!!"
label EP12_Bar_6:
    scene 40-3 patrick 45-1 with Dissolve(1)
    a "So... We've got..."
    a "Um... Two lagers and Sunset Dreams cocktail."
    j3 "Alright... coming up."
    scene 40-3 patrick 45 with Dissolve(1)
    a "All of them seem nice."
    j3 "They are just enthralled by you, Anna."
    a "Wish Patrick was like that."
    j3 "Yeah."
    scene 40-3 patrick 46 with Dissolve(1)
    j3 "Can't have a perfect world, you know."
    a "True."
    a "Gotta do best with what we've got."
    j3 "Wise words."
    j3 "Ready."
    scene 40-3 patrick 47 with Dissolve(1)
    a "Alright... Keep up the good work."
    j3 "You too, Anna."
    scene 40-3 patrick 48 with Dissolve(1)
    j3 "{i}...That Ass!!!!...{/i}"
    scene 40-3 patrick 49 with Dissolve(1)
    pause 1
    play sound spank3
    scene 40-3 patrick 50 with vpunch
    pause 0.5
    scene 40-3 patrick 51 with Dissolve(1)
    a "Ouch!"
    a "Jim?!"
    scene 40-3 patrick 52 with Dissolve(1)
    j3 "I've got wise words for you. Seize every opportunity you get."
    a "Smartass..."
    j3 "Hehe..."
    scene black with Dissolve(1)
label EP12_Bar_7:
    scene 40-3 patrick 53 with Dissolve(1)
    a "Alright... Here is your Lager, sir."
    bc_1 "Awesome!"
    bc_1 "Bring it here!"
    scene 40-3 patrick 54 with Dissolve(1)
    bc_1 "Say, I heard that this place is getting a rebranding."
    a "Oh?"
    bc_1 "Something about additional 'services'?"
    a "I see..."
    menu:
        "Service the client: + 150$":
            a "Alright, sir."
            a "You've got yourself a deal..."
            bc_1 "Really?"
            bc_1 "That's awesome!"
            scene 40-3 patrick 55 with Dissolve(1)
            a "{i}...I hope no one notices...{/i}"
            a "{i}...Probably will be fine...{/i}"
            play sound jacketcloth
            scene 40-3 patrick 56 with Dissolve(1)
            a "Alright... What would you like."
            a "We provide... 'lite' version for now."
            bc_1 "Great!"
            scene 40-3 patrick 57 with Dissolve(1)
            bc_1 "I'd like some hand services."
            scene 40-3 patrick 58 with Dissolve(1)
            bc_1 "If you don't mind?"
            a "I... That's what I'm here for."
            play sound undress
            scene 40-3 patrick 59 with Dissolve(1)
            bc_1 "Good."
            "The man hesitates only for a second, before pulling it out."
            play sound surprise
            scene 40-3 patrick 60 with Dissolve(1)
            a "Well, well..."
            a "Looks like you're ready."
            bc_1 "Been like this for a while."
            bc_1 "Ever since you showed up, in fact."
            scene 40-3 patrick 61 with Dissolve(1)
            "Anna looked around for a second more."
            a "{i}...Alright... Time to earn the money...{/i}"
            scene 40-3 patrick 62 with Dissolve(1)
            bc_1 "Damn..."
            "Anna got her hand right on his cock."
            "She tried to contain herself..."
            "Multiple emotions overtook her."
            "But as always... She tried to justify it."
            play sound jerk loop
            scene 40-3 patrick 63 with Dissolve(1)
            bc_1 "Magical..."
            bc_1 "Ahh..."
            scene 40-3 patrick 63-1 with Dissolve(1)
            bc_1 "Ah!"
            a "Shush... Keep it down mister..."
            a "{i}...I hope no one sees us...{/i}"
            bc_1 "Hehe... Sorry..."
            scene EP12_Bar_Anim_1 with Dissolve(1)
            bc_1 "Hooh..."
            bc_1 "That's the good shit..."
            a "{i}...I can feel his cock twitching in my hand...{/i}"
            scene EP12_Bar_Anim_2 with Dissolve(1)
            pause
            bc_1 "Just like that..."
            bc_1 "Oh, fuck... I'm getting real close..."
            bc_1 "Do it faster."
            scene EP12_Bar_Anim_2_Faster with Dissolve(1)
            pause
            bc_1 "Fuuuuuuuck... This is so good..."
            bc_1 "Best money I've spent here..."
            bc_1 "OH... I can't hold it anymore!"
            pause
            scene 40-3 patrick 64 with Dissolve(1)
            "The man got close, really fast..."
            with flash
            bc_1 "Shit..."
            with flash
            with flash
            play sound cum_sound
            scene 40-3 patrick 65 with flash_vpunch
            bc_1 "Fuckk... Aa..."
            bc_1 "Damn..."
            scene 40-3 patrick 66 with Dissolve(1)
            a "{i}...That's so hot...{/i}"
            a "{i}...What am I thinking...{/i}"
            scene 40-3 patrick 67 with Dissolve(1)
            pause 1
            scene 40-3 patrick 68 with Dissolve(1)
            bc_1 "Holy fuck..."
            a "{i}...I bet he likes this dirty stuff...{/i}"
            a "Mmm..."
            scene 40-3 patrick 69 with Dissolve(1)
            a "Well...I hope you had fun..."
            bc_1 "I... Damn..."
            bc_1 "Gotta take a chill moment..."
            bc_1 "Best hands I've ever had!"
            scene 40-3 patrick 70 with Dissolve(1)
            a "Enjoy your drink, sir."
            scene black with Dissolve(1)
        "Don't service him.":
            a "Nope, that's not on the menu today."
            pass
label EP12_Bar_8:
    scene 40-3 patrick 71-1 with Dissolve(1)
    bc_2 "Sexy girls AND good service?"
    bc_2 "This place keeps getting better and better."
    a "Thank you, sir."
    scene 40-3 patrick 71 with Dissolve(1)
    bc_2 "I hope the evening treats you well?"
    a "I'm doing alright, sure."
    bc_2 "Good to hear."
    scene 40-3 patrick 72_0 with Dissolve(1)
    a "Anyway... Here's your drink."
    bc_2 "Say... I found out somewhere, that you give extra service from now on?"
    bc_2 "The bar, I mean."
    scene 40-3 patrick 72-1 with Dissolve(1)
    a "We've had some changes, yeah."
    a "Mostly, I provide additional 'benefits' to our dear patrons."
    bc_2 "Good, good..."
    bc_2 "So? Would you be willing?"
    menu:
        "Service The client: +100$":
            scene 40-3 patrick 72 with Dissolve(1)
            a "Sure... We can do something."
            a "What do you have in mind?"
            scene 40-3 patrick 73 with Dissolve(1)
            bc_2 "Well... I've been looking at you all evening."
            bc_2 "Wondering..."
            scene 40-3 patrick 74 with Dissolve(1)
            bc_2 "Do you need those panties?"
            bc_2 "I think you'd look better without them."
            a "Is that so?"
            bc_2 "Indeed it is."
            scene 40-3 patrick 75 with Dissolve(1)
            a "Off they go, mister."
            bc_2 "Ha. That is priceless."
            scene 40-3 patrick 76 with Dissolve(1)
            a "Your patronage is deeply appreciated."
            a "Now, where were we?"
            a "Ah. Right."
            scene 40-3 patrick 78 with Dissolve(1)
            bc_2 "Hah. This is one of a kind chance."
            bc_2 "I... I want you to sit on my face."
            a "Face riding coming right up!"
            a "{i}...I'm so slutty... Hehe...{/i}"
            scene 40-3 patrick 79 with Dissolve(1)
            pause 1
            scene 40-3 patrick 80 with Dissolve(1)
            "The other bar members were catching on."
            da "The fuck..."
            j3 "Emm... You've seen more depraved shit here before."
            da "True."
            j3 "Patrick's rebranding."
            da "I see..."
            scene 40-3 patrick 81 with Dissolve(1)
            a "So, mister."
            a "You'd like to enjoy my pussy?"
            scene 40-3 patrick 82 with Dissolve(1)
            bc_2 "Yes, ma'am."
            bc_2 "I wanna suck on that clitoris."
            a "I'm obliged to help you with that."
            scene 40-3 patrick 83 with Dissolve(1)
            a "{i}...This is getting crazy...{/i}"
            a "{i}...Fuck it...{/i}"
            bc_2 "Fuck me. This is so hot."
            bc_2 "My wife would never do that."
            scene 40-3 patrick 84 with Dissolve(1)
            a "Well, then. Enjoy it hehe..."
            bc_2 "Oh, yes!"
            scene 40-3 patrick 85 with Dissolve(1)
            a "{i}...His tongue...{/i}"
            a "Mh..."
            bc_2 "Mhmmm..."
            play sound jerk2 loop
            scene 40-3 patrick 86 with Dissolve(1)
            pause 1
            play sound female_moan_5
            scene 40-3 patrick 87 with Dissolve(1)
            a "Mfff..."
            "Anna was starting to enjoy herself a lot more."
            scene 40-3 patrick 88 with Dissolve(1)
            j3 "She'll earn us some good bucks with this."
            j3 "Patrick is quite smart..."
            a "Ah!"
            "Anna could barely contain her moans..."
            "The pussy was getting rather sensitive."
            scene 40-3 patrick 89 with Dissolve(1)
            pause
            play audio female_moan_1
            scene 40-3 patrick 90 with Dissolve(1)
            a "{i}...So good...{/i}"
            "The man was enjoying the pussy sucking thoroughly..."
            a "Keep doing it just like that..."
            scene 40-3 patrick 91 with Dissolve(1)
            "Anna grabbed the man by his head and started to ride his face even more."
            play audio femmoan_3
            a "{i}...He's pressing all the right buttons...{/i}"
            a "Mhaa..."
            scene 40-3 patrick 92 with Dissolve(1)
            a "{i}...This is so hot... Others are probably looking at us...{/i}"
            a "{i}...This is so naughty...{/i}"
            play audio female_moan_4
            a "Yeah... Just... Like... That..."
            scene EP12_Bar_Anim_3 with Dissolve(0.5)
            pause
            play audio female_moan_2
            a "OOH!"
            "Anna was feeling the build-up of pleasure reach a peak."
            scene EP12_Bar_Anim_4 with Dissolve(1)
            pause
            "An explosion was imminent..."
            scene EP12_Bar_Anim_4_Faster with Dissolve(1)
            a "OOHHH."
            a "You like licking this pussy?"
            bc_2 "MHmmm...."
            a "{i}...So Good...{/i}"
            play audio female_moan_3
            "Anna was becoming very harsh with the man's face..."
            "But he loved it."
            "Her body arched in reflex..."
            scene 40-3 patrick 93 with flash
            play audio femmoan_4
            a "Oohh..."
            with flash
            a "Mhh..."
            play audio femmoan_3
            a "AAHHHH...!"
            scene 40-3 patrick 94 with flash
            pause 1
            a "AAHHH!!"
            pause 2
            stop sound
            scene 40-3 patrick 95 with Dissolve(1)
            bc_2 "Mhaa..."
            bc_2 "Yeah!"
            bc_2 "You like that?"
            a "Hehe... Sure did."
            scene 40-3 patrick 96 with Dissolve(1)
            a "Did you?"
            bc_2 "Absolutely..."
            bc_2 "I wanna do it again soon!"
            a "You bet, mister."
            "Anna was starting to garner an audience."
            scene 40-3 patrick 97 with Dissolve(1)
            a "Well, enjoy your drink, mister."
            a "I hope you come here again."
            scene 40-3 patrick 98 with Dissolve(1)
            bc_2 "No doubt about it."
            bc_2 "Next time something more, hehe."
            scene 40-3 patrick 99 with Dissolve(1)
            a "I will keep that in mind."
            bc_2 "Fuck yeah!"
            scene black with Dissolve(1)
        "Dont service.":
            a "I'm sorry, That's not happening."
            pass
label EP12_Bar_9:
    scene 40-3 patrick 100 with Dissolve(1)
    a "Hello again. The drink should be with you shortly."
    bc_3 "Ye, ye. No problem."
    scene 40-3 patrick 101 with Dissolve(1)
    a "How are you enjoying your evening so far?"
    bc_3 "There are the telltale signs of a successful one."
    bc_3 "Pretty girls, Good music, Probably good drinks too."
    a "Haha. We definitely have all of those."
    scene 40-3 patrick 102 with Dissolve(1)
    j3 "One Sunset Dreams?"
    bc_3 "Yes, Jim. Thank you!"
    bc_3 "Let's see if you make them as good as the competition."
    play sound drinkingBeverage
    scene 40-3 patrick 104 with Dissolve(1)
    bc_3 "Bottoms up!"
    scene 40-3 patrick 105 with Dissolve(1)
    a "How is it, sir?"
    a "I hope we tick off all the boxes you'd like in a bar?"
    play sound surprise2
    scene 40-3 patrick 107 with Dissolve(1)
    bc_3 "Well... There is one that I haven't checked just yet."
    a "Huh?"
    scene 40-3 patrick 108 with Dissolve(1)
    a "Oh!"
    a "Sir... I..."
    bc_3 "Heard you've got some extra perks to your patrons?"
    a "Well..."
    menu:
        "Suck off the man: +200$":
            a "Yeah... We do in fact."
            bc_3 "Hehe... That's what I like to hear."
            scene 40-3 patrick 110 with Dissolve(1)
            a "How about you sit back... And let me show you our specialty."
            bc_3 "Damn straight."
            scene 40-3 patrick 111 with Dissolve(1)
            a "Looks like you're already ready, eh?"
            bc_3 "Yes, ma'am. Been ready since I saw you enter."
            a "Hehe..."
            play sound surprise
            scene 40-3 patrick 112 with Dissolve(1)
            bc_3 "Ahh..."
            bc_3 "I've seen all your films... I never believed that I'd get the chance."
            scene 40-3 patrick 113 with Dissolve(1)
            a "Well, here I am."
            bc_3 "Here you are..."
            a "{i}...He looks so excited...{/i}"
            a "{i}...Kind of hot... Meeting my fan...{/i}"
            scene 40-3 patrick 114 with Dissolve(1)
            "Anna got on her knees in seconds."
            a "Alright... Sir..."
            bc_3 "Oh snap... Damn, damn..."
            bc_3 "This is really happening!!"

            scene 40-3 patrick 115 with Dissolve(1)
            bc_3 "Ooff..."
            bc_3 "Them hands!"
            scene 40-3 patrick 116 with Dissolve(1)
            a "Mhh...."
            bc_3 "Aah!!!"
            bc_3 "You crazy gal!"
            bc_3 "I'm going to be coming here regularly!"
            scene 40-3 patrick 117 with Dissolve(1)
            a "{i}...Mmm... His dick has a nice taste...{/i}"
            a "{i}...Never tasted anyone using some sort of product...{/i}"
            bc_3 "Before coming here, I used a special cream, so that it tastes better. Heh."
            a "Mhmmm..."
            play sound jerk3 loop
            scene 40-3 patrick 118 with Dissolve(1)
            pause
            scene 40-3 patrick 119 with Dissolve(1)
            bc_3 "Ahh..."
            a "{i}...So hot... I actually like being the bar slut...{/i}"
            play audio femmoan_2
            a "{i}...I'm starting to know my place...{/i}"
            scene 40-3 patrick 120 with Dissolve(1)
            pause 1
            scene EP12_Bar_Anim_5 with Dissolve(0.5)
            pause
            play audio femmoan_3
            if DilanPornContent == True:
                bc_3 "Finally meeting my favorite actress!"
                bc_3 "AND getting a blowjob from her???"
            else:
                bc_3 "My favorite waitress!"
                bc_3 "Is giving me a blowjob? Ain't life good?"
            pause
            scene EP12_Bar_Anim_6 with Dissolve(0.5)
            pause
            bc_3 "OH shitt..."
            bc_3 "You startin' to suck on it real tight!"
            bc_3 "Like a vacuum... Fuck meeeeee...."
            a "{i}...His cock filling my mouth up...{/i}"
            pause
            scene EP12_Bar_Anim_6_Faster with Dissolve(0.5)
            pause
            bc_3 "I'm... DAAMN!"
            a "Mmm... KHa..."
            pause
            scene 40-3 patrick 121 with Dissolve(1)
            bc_3 "Yeah, just like that..."
            "The man grabbed her head and..."
            scene 40-3 patrick 122 with Dissolve(1)
            "Pressed his cock even deeper."
            bc_3 "Ahhhh...."
            play audio female_cough_1
            a "{i}...Ah... I'm chocking on his cock...{/i}"
            bc_3 "Damn, you're hot!"
            scene 40-3 patrick 123 with Dissolve(1)
            "Anna gurgled on the client's cock."
            "Her eyes watering from the deep throat."
            a "MmmMM!!!!"
            bc_3 "Yeah. Take it!!!"
            bc_3 "This is great!"
            scene 40-3 patrick 124 with Dissolve(1)
            bc_3 "Best day of my life!"
            "The man wasn't stopping. In fact, he was increasing the pace."
            "Pushing the cock deeper and deeper."
            with flash
            scene 40-3 patrick 125 with Dissolve(1)
            bc_3 "Fuuuckkk!!!"
            with flash
            bc_3 "AHHH!!"
            "He pushed as much cum out as possible from his shaft."
            with flash
            with flash
            stop sound
            play sound cum_sound
            scene 40-3 patrick 126 with flash_vpunch
            bc_3 "AAAAAAAA"
            a "MmmmMMMM!!!!!!"
            a "{i}...So much cum...{/i}"
            a "{i}...My throat is completely filled...{/i}"
            scene 40-3 patrick 127 with Dissolve(1)
            "The cum was dripping. Her mouth had overflown from the amount of cum."
            scene 40-3 patrick 128 with Dissolve(1)
            bc_3 "Sheesh..."
            scene 40-3 patrick 129 with Dissolve(1)
            a "That's... A lot..."
            bc_3 "Yeah... Heh..."
            bc_3 "I had been saving up."
            bc_3 "That... that was amazing."
            bc_3 "I liked this sampling. Patrick knows how to get clients."
            a "Yeah..."
            scene 40-3 patrick 130 with Dissolve(1)
            bc_3 "You are one of a kind. Damn..."
            bc_3 "I sure hope you've got more where that came from, in the future."
            a "Perhaps..."
            scene 40-3 patrick 131 with Dissolve(1)
            a "Lemme just clean up."
            bc_3 "Uh... Sure... Take your time!"
            play sound jacketcloth
        "Don't provide any extra services.":
            a "I don't do any of that... Sorry..."
            bc_3 "Ah... A shame..."
    scene 40-3 patrick 132 with Dissolve(1)
    a "I hope you enjoyed our services and the drink."
    a "Please come again."
    bc_3 "Hehe... Without a doubt!"
    scene black with Dissolve(1)
label EP12_Bar_10:
    scene 40-3 patrick 133 with Dissolve(1)
    j3 "Well... Clients keeping you busy?"
    a "They sure are."
    j3 "As much as I enjoy your company, your shift has ended."
    scene 40-3 patrick 134 with Dissolve(1)
    a "Ok."
    j3 "Yeah."
    j3 "Take the money to Patrick."
    a "Sure..."
    scene 40-3 patrick 136 with Dissolve(1)
    ga "Good day, eh?"
    a "I suppose..."
    play sound door2
    scene black with Dissolve(1)
    play music chill_song_4
    stop ambience
    scene 40-3 patrick 137 with Dissolve(1)
    pa "Then subtract the expenses from the revenue and you get profit."
    pa "Never forget that revenue is the income you've earned, not the final profit."
    pa "Make all your calculations around that."
    scene 40-3 patrick 138 with Dissolve(1)
    lu "Dad..."
    lu "She's here."
    pa "Ah."
    scene 40-3 patrick 139 with Dissolve(1)
    pa "Just in time."
    pa "I've been keeping an eye on how you've been doing."
    pa "And..."
    pa "I have to say... Good job."
    pa "Now, then."
    pa "I have something else to discuss with you."
    scene 40-3 patrick 140 with Dissolve(1)
    a "Not another of your sexual schemes."
    pa "Hehe... You are quite right, Anna."
    pa "How about those earnings?"
    scene 40-3 patrick 141 with Dissolve(1)
    a "Here..."
    pa "You see, you give me a cut from all the earnings you get here."
    a "Seriously?"
    pa "Of course. All the marketing, all the setup I do so that you can earn here."
    pa "It doesn't come cheap."
    pa "Now, 50%% sounds good."
    scene 40-3 patrick 142 with Dissolve(1)
    a "Fine. Choke on it."
    pa "Now, now. We can, of course, strike another deal."
    pa "Remember, if you make good with me now, in the future you will be earning the big bucks."
    pa "Cause I will take care of everything else."
    scene 40-3 patrick 143 with Dissolve(1)
    pa "Here is your half..."
    scene 40-3 patrick 144 with Dissolve(1)
    pa "And about our deal."
    pa "You see. My son... He needs some... Practice."
    a "Wha?"
    scene 40-3 patrick 145 with Dissolve(1)
    pa "He's young. Inexperienced."
    pa "If you do him some of the honors."
    scene 40-3 patrick 146 with Dissolve(1)
    pa "I could throw something more your way."
    a "I..."
    pa "I will decrease my share to a tiny 20%% for the future and this transaction."
    pa "What do you say?"
    pa "And remember in the future, the profits will only go up."
    pa "Trust me."
    scene 40-3 patrick 147 with Dissolve(1)
    menu:
        "Ok... I could use the money.":
            label EP12_Bar_Lucas_Sex:
                "But did Anna really need the money? She was earning plenty at the office already..."
            "Perhaps it was something else..."
            pa "Haha. Great!"
            pa "Well then..."
            pa "Get on with it."
            scene 40-3 patrick 148 with Dissolve(1)
            pa "I will leave you to it."
            a "Sure..."
            play sound door2
            scene 40-3 patrick 149 with Dissolve(1)
            a "{i}...Alright... Let's get this over with...{/i}"
            a "{i}...He's a cheeky little kid... Annoying as they come...{/i}"
            a "{i}...But if it helps me...{/i}"
            scene 40-3 patrick 150 with Dissolve(1)
            a "So..."
            lu "Ah... the slut."
            a "{b}*Sigh*{/b}"
            a "I've been thinking..."
            a "Looks like you're slowly learning the ropes of the business, to take after your father?"
            lu "Of course, no one else is competent enough here, Not Jim... Certainly not you."
            scene 40-3 patrick 151 with Dissolve(1)
            a "Heh... That's..."
            "Anna was just suppressing her anger."
            a "True..."
            a "Listen... If that's the case, that you're taking over slowly..."
            a "You oughta know the rest of the 'perks' of this place, eh?"
            scene 40-3 patrick 152 with Dissolve(1)
            lu "Meaning?"
            lu "{i}...Is Anna going to...{/i}"
            scene 40-3 patrick 153 with Dissolve(1)
            a "Well... Something intimate."
            lu "Whoa..."
            "Lucas suddenly lost all his bravado..."
            a "Something to remember."
            scene 40-3 patrick 154 with Dissolve(1)
            a "What do you say?"
            lu "I... I..."
            lu "Yeaahhh..."
            "Anna could feel his awkwardness."
            a "Don't be shy, touch..."
            scene 40-3 patrick 155 with Dissolve(1)
            lu "Ahh..."
            a "Yeah... Like that."
            scene 40-3 patrick 156 with Dissolve(1)
            lu "Whe... Where is this coming from?"
            a "Like I said. Benefits of an upcoming Bar owner."
            a "Are you not enjoying this?"
            lu "I mean, I am."
            scene 40-3 patrick 157 with Dissolve(1)
            a "Relax. It's fine."
            a "{i}...All bravado until a woman gets naked in front of him...{/i}"
            a "{i}...Hehe... This is fun...{/i}"
            scene 40-3 patrick 158 with Dissolve(1)
            a "You wanna go further?"
            lu "Uhh... Y... Yeah.?"
            scene 40-3 patrick 159 with Dissolve(1)
            a "Take em off."
            lu "{b}*Gulp*{/b}"
            play sound undress
            scene 40-3 patrick 160 with Dissolve(1)
            a "Yeah... You like them titties?"
            lu "{i}...Fuck me... Always look good...{/i}"
            lu "Yes... ma'am..."
            a "Ma'am?"
            lu "Uhh..."
            scene 40-3 patrick 161 with Dissolve(1)
            pause 1
            play sound cloth_sound1
            scene 40-3 patrick 162 with Dissolve(1)
            a "How does it look from down there?"
            lu "Hot... Hot as fuck."
            a "Hehe..."
            a "{i}...He's so out of his element...{/i}"
            scene 40-3 patrick 163 with Dissolve(1)
            a "Come on. Are you just gonna stare?"
            lu "Emm... No."
            a "That's right."
            scene 40-3 patrick 164 with Dissolve(1)
            "When the time to do something sexual, Lucas becomes completely dormant."
            "Not Arrogant or mean anymore."
            "Just awkward and shy..."
            a "Lick it..."
            play sound jerk
            scene 40-3 patrick 165 with Dissolve(1)
            a "Mhm..."
            "Anna felt the stimulation right away..."
            "How the tongue slides across the nipple..."
            "Slowly becoming harder..."
            scene 40-3 patrick 166 with Dissolve(1)
            a "Just... Ah... Like that..."
            lu "Mhm..."
            a "You're doing good, boy."
            scene 40-3 patrick 167 with Dissolve(1)
            a "Yeah!"
            lu "Mmmmm..."
            a "{i}...Damn... They are sensitive... Feels ecstatic...{/i}"
            play sound jerk2
            scene EP12_Lucas_Anim_1 with Dissolve(0.5)
            a "{i}...Don't stop...{/i}"
            a "{i}...At least he can suck a nipple...{/i}"
            pause
            play audio female_moan_2
            scene 40-3 patrick 168 with Dissolve(1)
            pause 1
            scene 40-3 patrick 169 with Dissolve(1)
            "She pulled his head off of the nipple."
            a "Alright..."
            a "Time for something else."
            lu "Ok, Anna..."
            play sound jacketcloth
            scene 40-3 patrick 170 with Dissolve(1)
            a "How about we lose the panties?"
            lu "The what?"
            a "You thought we'd finished?"
            scene 40-3 patrick 171 with Dissolve(1)
            lu "{i}...I can't believe it... Will I get...{/i}"
            lu "{i}... To fuck her? She's hot...{/i}"
            lu "{i}...I'm so lucky... Damn...{/i}"
            "Lucas was in fact very excited..."
            "The facade he put on was a byproduct of his youth..."
            "He always tried to get Anna's attention the simple way he knew..."
            "With being rude or mean... Like his father..."
            scene 40-3 patrick 172 with Dissolve(1)
            a "Hehe..."
            a "Take em off, Lucas."
            lu "Yes... Anna..."
            play sound undress
            scene 40-3 patrick 173 with Dissolve(1)
            pause 1
            play sound whoosh_1
            scene 40-3 patrick 174 with Dissolve(1)
            pause 1
            scene 40-3 patrick 175 with Dissolve(1)
            "She immediately spread her legs in front of the inexperience little prick."
            "Perhaps it was Annas' fate to be a toy for the assholes..."
            a "You like this?"
            lu "Yes... Anna..."
            play sound surprise2
            scene 40-3 patrick 176 with Dissolve(1)
            lu "Fuuck me..."
            lu "This is..."
            a "Don't tell me you've never had a woman spread her legs like this for you..."
            lu "N... No..."
            a "Hehe... This will be fun..."
            scene 40-3 patrick 177 with Dissolve(1)
            "Lucas took a moment to admire her sexy fuck-hole."
            pause 1
            scene 40-3 patrick 178 with Dissolve(1)
            a "Don't hesitate..."
            a "Get that cock out."
            lu "What?"
            scene 40-3 patrick 179 with Dissolve(1)
            lu "Really?"
            a "Yes, silly..."
            a "Don't make me wait!"
            play sound undress
            scene 40-3 patrick 180 with Dissolve(1)
            a "That's right... Show that thing to me."
            a "Yeah... That's good."
            scene 40-3 patrick 181 with Dissolve(1)
            a "Well, let's get on with it..."
            a "Take your clothes off."
            scene 40-3 patrick 182 with Dissolve(1)
            a "You shy?"
            lu "Umm... No..."
            a "{i}...Of course, he is... Hehe...{/i}"
            a "{i}...This little prick will not forget our little fun experience...{/i}"
            play sound undress
            scene 40-3 patrick 183 with Dissolve(1)
            lu "Aah..."
            a "{i}...Heh... His cock is twitching in my hand like crazy...{/i}"
            "Anna could see the excitement and worry on Lucas' face."
            "He was looking forward to this, but also worried about not satisfying Anna."
            scene 40-3 patrick 184 with Dissolve(1)
            a "You like my hand wrapped around your cock?"
            lu "Yes... Anna... This is so hot..."
            scene EP12_Lucas_Anim_2 with Dissolve(0.5)
            pause
            lu "I... Hope I can give you what you want."
            a "Oh really?"
            pause
            a "Come on. Push it in..."
            scene 40-3 patrick 185 with Dissolve(1)
            pause 1
            play sound jerk loop
            scene 40-3 patrick 186 with Dissolve(1)
            a "Ah..."
            lu "mhh..."
            "He maneuvered his tip inside of Anna."
            "And felt the sensation as goosebumps covered his body..."
            play audio female_moan_2
            scene 40-3 patrick 187 with Dissolve(1)
            a "Ah..."
            a "You... You like that?"
            "Anna went along with the plan at first..."
            "But now... Like always, her senses were being overtaken..."
            scene 40-3 patrick 188 with Dissolve(1)
            lu "Yyeeaahh..."
            "Lucas took her and started to fuck harder..."
            scene 40-3 patrick 189 with Dissolve(1)
            "Barely any rhythm..."
            "Inexperienced... Yet Anna felt great..."
            scene 40-3 patrick 190 with Dissolve(1)
            a "{i}...Ah... This feels interesting...{/i}"
            a "{i}...Getting fucked by this asshole...{/i}"
            scene EP12_Lucas_Anim_3 with Dissolve(0.5)
            pause
            lu "Uhh..."
            pause
            lu "So good..."
            scene EP12_Lucas_Anim_3_Faster with Dissolve(0.5)
            pause
            play audio femmoan
            a "Mmhhh..."
            scene 40-3 patrick 192 with Dissolve(1)
            a "Ah!"
            lu "You... You like it..."
            scene EP12_Lucas_Anim_4 with Dissolve(0.5)
            a "Mhm... Shut up and fuck me..."
            pause
            play audio female_moan_5
            a "Continue like this..."
            scene EP12_Lucas_Anim_4_Faster with Dissolve(0.5)
            pause
            play audio female_moan_1
            scene 40-3 patrick 193 with Dissolve(1)
            pause 1
            scene 40-3 patrick 194 with Dissolve(1)
            a "{i}...He's so naive and shy...{/i}"
            a "{i}...I like teaching inexperienced young fuckers, hehe...{/i}"
            play audio femmoan_2
            a "MH!!"
            lu "I've... I've never fucked a pussy..."
            lu "This is unbelievable..."
            scene 40-3 patrick 195 with Dissolve(1)
            a "Lemme just get comfy..."
            lu "Yes... Anna... Do as you like!"
            play audio femmoan_2
            a "How about you focus on giving me some good dick?"
            lu "Yes... Ah!!"
            scene 40-3 patrick 196 with Dissolve(1)
            lu "{i}...How is this possible...{/i}"
            lu "{i}...Suddenly she's giving me some sex...{/i}"
            scene EP12_Lucas_Anim_5 with Dissolve(0.5)
            pause
            lu "{i}...Perhaps if I start treating her better she'll give me more?{/i}"
            pause
            scene EP12_Lucas_Anim_5_Faster with Dissolve(0.5)
            pause
            play audio female_moan_1
            lu "{i}...Or maybe because I treat her like a whore?...{/i}"
            lu "This shit feels soo goood..."
            pause
            scene 40-3 patrick 197 with Dissolve(1)
            lu "Ah... I... I'm getting close..."
            a "Me too..."
            play audio female_moan_2
            "But this time Anna was lying... She was faking it..."
            scene EP12_Lucas_Anim_6 with Dissolve(0.5)
            pause
            a "{i}...Gotta teach this kid how to work his hips more...{/i}"
            a "{i}...If I'm to turn him into a better fucker...{/i}"
            scene 40-3 patrick 198 with Dissolve(1)
            a "Aah..."
            lu "Oh fuck..."
            scene EP12_Lucas_Anim_6_Faster with Dissolve(0.5)
            lu "{i}...I might actually make her cum?!...{/i}"
            play audio MoaningTen
            menu:
                "Cum inside of Anna's pussy.":
                    with flash
                    scene 40-3 patrick 199 with Dissolve(1)
                    a "AHH!!!"
                    lu "FUUUCK!"
                    with flash
                    "Anna moaned loudly to give Lucas confidence in his 'abilities'"
                    lu "Ah..."
                    with flash
                    play sound cum_sound
                    scene 40-3 patrick 200 with flash_vpunch
                    pause 1
                    scene 40-3 patrick 201 with Dissolve(1)
                    lu "Fuck me... I filled you up good..."
                    a "Ah... You did indeed..."
                    scene 40-3 patrick 202 with Dissolve(1)
                    a "Hehe... Did you enjoy yourself?"
                    lu "I can't believe it still..."
                    a "If you act nice, you might get more..."
                "Cum on Anna's hot body.":
                    with flash
                    scene 40-3 patrick 199 with Dissolve(1)
                    lu "Shit!"
                    lu "AAHH... I'm... So..."
                    with flash
                    scene 40-3 patrick 203 with flash
                    lu "My cock!!!"
                    lu "SO GOOD!"
                    lu "AAHHHH!"
                    play sound cum_sound
                    scene 40-3 patrick 204 with flash_vpunch
                    a "AHH!"
                    lu "SHIITT!!!"
                    scene 40-3 patrick 205 with Dissolve(1)
                    a "Hehe... Did you enjoy yourself?"
                    lu "I can't believe it still..."
                    a "If you act nice, you might get more..."
            scene black with Dissolve(1)
            pause 0.5
            scene 40-3 patrick 207 with Dissolve(1)
            a "Hehe... How did you like that?"
            lu "I've never... Never had a girl..."
            lu "I'm... Wow..."
            a "Nice."
            scene 40-3 patrick 208 with Dissolve(1)
            "Lucas was bamboozled still."
            "Confused as to how did things get here."
            a "Well, I'm heading out... Take care."
            scene 40-3 patrick 209 with Dissolve(1)
            a "Be nice. Alright?"
            lu "I... Ok..."
            scene black with Dissolve(1)
            $ renpy.end_replay()
            play sound door2
            scene 40-3 patrick 210 with Dissolve(1)
            a "Well... That was interesting..."
            a "I hope now I get more money..."
            "Anna was becoming so gullible... Not learning anything from her previous encounters with Patrick."
            "Rather... She was becoming his personal sex worker... And was just in denial about the fact she loved it..."
            scene black with Dissolve(1)
            play sound jacketcloth
            scene 40-3 patrick 211 with Dissolve(1)
            a "Alright... My shift is over..."
            a "It was a bit odd... Just the 3 patrons and David... Was it all a setup?"
            $ persistent.scene_36 = True
            scene black with Dissolve(1)
        "Fuck. THAT!":
            a "I don't know why I let you use me like this. I don't need this. I'm out."
            pa "Don't be so dumb."
            pa "You need this."
            a "I don't. I got other opportunities!"
            pa "You know you'll regret this?"
            a "Naah. I won't."
            scene black with Dissolve(1)
            "Anna stormed out."
            play sound door2
            scene 40-3 patrick 210 with Dissolve(1)
            a "That'll show him..."
            "Although if Anna was smart enough, she'd leave this establishment permanently..."
            "The depravities would continue, otherwise."
            scene 40-3 patrick 211 with Dissolve(1)
            a "Alright... My shift is over..."
            scene black with Dissolve(1)
    jump EP12_Taxman
label EP12_DeadPatrickBar_1:
    $ EP12_var_12 = True
    play music jazzmusic
    scene 40-8 nopatrick 1 with Dissolve(1)
    a "Hey. I came as soon as I could."
    j3 "Great. Well, since we've got it all set up..."
    j3 "I was thinking it was time to open the bar again?"
    a "Yeah."
    scene 40-8 nopatrick 2 with Dissolve(1)
    a "Sounds like a plan."
    j3 "You are of course now the new 'boss'"
    a "Why did we decide to do it, again?"
    j3 "I mean, I'm not good with numbers, to be honest, I better leave it to someone smarter."
    a "Ah, right."
    a "So... We've got a couple of things to take care of."
    scene 40-8 nopatrick 3 with Dissolve(1)
    j3 "Yeah."
    j3 "We are running low on some alcohol and ingredients."
    a "Ok, so I will check what we need and order."
    j3 "Also, Gabe's waiting for you, he got released, wants his job back, and promises to take better care of this place."
    a "Ok..."
    scene 40-8 nopatrick 4 with Dissolve(1)
    j3 "That's about it. Some other organizing elements, but leave them to me."
    a "Sounds good."
    a "Will also take a look at our finances. Perhaps we can do something with those."
    j3 "Sure. That would be a good idea."
    scene black with Dissolve(1)
    play sound door2
    scene 40-8 nopatrick 5 with Dissolve(1)
    ga "Hey... Hey, Anna."
    a "Hello, Gabe..."
    ga "I was hoping you got a minute?"
    a "I sure do."
    scene 40-8 nopatrick 7 with Dissolve(1)
    a "Come on in."
    ga "Alright..."
    scene 40-8 nopatrick 8 with Dissolve(1)
    a "So... You doing ok?"
    ga "Yeah... I'm still a bit fucked up about what happened, but I'm good."
    ga "Listen, I wanted to ask if I could get my old job back?"
    a "Well..."
    a "Will you try and defend me harder than you did Patrick?"
    scene 40-8 nopatrick 9 with Dissolve(1)
    ga "Uh... Yeah! I will try even more. No one will be able to touch you!"
    a "Hehe... That's good to hear."
    scene 40-8 nopatrick 10 with Dissolve(1)
    a "If you try as {b}Hard{/b} as you can..."
    a "We will get along just fine."
    ga "Yes, Anna!"
    scene 40-8 nopatrick 11 with Dissolve(1)
    a "You are rehired, then."
    a "I'm glad to not have to look for someone new."
    ga "I'm glad I don't have to look for another job..."
    a "Trust me, this place will become much more profitable now..."
    a "As... Sad as it is that Patrick is gone..."
    scene 40-8 nopatrick 12 with Dissolve(1)
    a "You just keep doing what you do best, and we won't have any problems."
    a "You'll get paid good money..."
    ga "Yes, Anna... You can consider me... Your personal bodyguard."
    a "Is that so?"
    ga "Yes, ma'am!"
    a "Alright... hehe..."
    a "Dismissed!"
    scene 40-8 nopatrick 13 with Dissolve(1)
    pause 1
    play sound door2
    scene 40-8 nopatrick 14 with Dissolve(1)
    a "{i}...Personal bodyguard...{/i}"
    a "{i}...Interesting...{/i}"
    a "I should check the numbers..."
    play sound mouse_click_1
    scene 40-8 nopatrick 19 with Dissolve(1)
    a "Alright..."
    a "This accounting has layers..."
    a "I will have to bring in someone to make sense of this, I am not that good..."
    scene 40-8 nopatrick 20 with Dissolve(1)
    a "But it looks like Patrick was stealing from the bar..."
    a "Underpaying Jim and Gabe... And me..."
    a "That is just so fucking disgusting!"
    a "Well... No worries about that now..."
    a "Perhaps Emily could help with the accounting..."
    a "Alright, I should check our supplies."
    scene black with Dissolve(1)
    play sound door2
    scene 40-8 nopatrick 15 with Dissolve(1)
    a "So..."
    a "Jim said we are low on some stuff..."
    a "Probably the beers. They run out very quickly."
    play sound put_sound_1
    scene 40-8 nopatrick 16 with Dissolve(1)
    a "Alright..."
    a "Yeah, this is almost empty..."
    a "Thunderbolt Stout... One of the favorites, I believe."
    scene 40-8 nopatrick 17 with Dissolve(1)
    a "Hmm... I probably need some extra alcohol of every kind."
    a "A large quantity."
    a "Thunderbolt Stout definitely as a priority, but a bit of everything..."
    scene 40-8 nopatrick 18 with Dissolve(1)
    a "A lot of boxes are empty... Seems like there hasn't been much maintenance on this building in some time."
    a "Will need to fix a lot of things around here..."
    a "That requires money..."
    a "Where would I get investments now..."
    a "Better get back and order those things."
    scene black with Dissolve(1)
    play sound jacketcloth
    scene 40-8 nopatrick 19 with Dissolve(1)
    a "Alright..."
    a "10 boxes of Thunderbolt Stout..."
    a "2 boxes of Grand Canyon Whiskey..."
    a "3 boxes Pandora Gin."
    a "2 FrostFire Vodka... That name, though... Someone tried very hard..."
    scene 40-8 nopatrick 20 with Dissolve(1)
    a "That should be all. Some garnishes. a box of frozen lemons, a box of lime."
    a "Uh... Will have to do a big inventory very soon."
    a "Damn, this is a lot of info..."
    a "Plus this place needs fixing..."
    scene 40-8 nopatrick 21 with Dissolve(1)
    a "Alright... For now, this is fine..."
    a "Should get back to Jim and tell him that all is in order..."
    scene 40-8 nopatrick 22 with Dissolve(1)
    j3 "I don't know, man! We were trying to sue him, but he just disappeared."
    j3 "No idea how that happened... I mean, whatever..."
    da "Hehe... Crazy stuff..."
    da "Did you ever find him?"
    j3 "No. Haven't seen him since then... Like gone, nada... Poof..."
    j3 "Gone..."
    scene 40-8 nopatrick 23 with Dissolve(1)
    a "Hey, boys. Working hard?"
    da "Not me! I'm relaxin'!"
    a "Good to hear, David."
    scene 40-8 nopatrick 24 with Dissolve(1)
    j3 "So. All good?"
    a "Well, this place is in need of some repairs, I found out something not so good... We'll talk about it later on."
    a "Bottom line, this place requires some money."
    j3 "Huh... That bad?"
    a "It would be better if we did."
    scene 40-8 nopatrick 25 with Dissolve(1)
    j3 "Anyway... Those two are back."
    j3 "They've been wanting to talk to you."
    a "Huh..."
    a "Alright, will get to them."
    j3 "If I recall. you had some interesting 'business' with them?"
    a "Not quite, but will see..."
    scene 40-8 nopatrick 26 with Dissolve(1)
    pa1 "Anna!"
    pa1 "So good to see you!"
    pa2 "Hey!"
    a "Greetings. Welcome back to our bar!"
    scene 40-8 nopatrick 27 with Dissolve(1)
    a "How may I assist you today?"
    pa1 "Word on the street is, you've taken over?"
    a "Well... Since Patrick's accident... Someone had to, right?"
    pa1 "Oh, yeah..."
    a "So, here I am..."
    scene 40-8 nopatrick 28 with Dissolve(1)
    pa2 "Well... Good luck to you, Anna!"
    pa2 "Cheers!"
    a "Thanks! Haha."
    pa2 "Anyway... We've been wanting to discuss something... Since the news about you becoming the new boss."
    pa2 "More specifically... My wife wishes to talk with you."
    scene 40-8 nopatrick 29 with Dissolve(1)
    a "Oh?"
    a "I'm intrigued."
    scene 40-8 nopatrick 30 with Dissolve(1)
    pa1 "Yeah... We are... Looking for ummm..."
    pa1 "Business partners..."
    a "Are you now?"
    pa1 "Yeah. And, well... You seem capable..."
    a "How about we discuss this in my... office... hehe..."
    scene 40-8 nopatrick 31 with Dissolve(1)
    a "Jim? Hold the fort, I've got some business to attend to."
    j3 "Sure thing, Anna."
    j3 "Good luck."
    j3 "{i}...Business... Hehe... I know what she meant by that...{/i}"
    scene 40-8 nopatrick 32 with Dissolve(1)
    a "Welcome."
    a "This is where the 'magic' happens."
    a "Heh..."
    pa1 "Alriight..."
    scene 40-8 nopatrick 33 with Dissolve(1)
    a "You may sit down..."
    a "Would you like anything?"
    a "Water, whiskey?"
    pa1 "We'll be fine... For now..."
    scene 40-8 nopatrick 34 with Dissolve(1)
    a "So... Tell me, what do you have in mind?"
    pa1 "Well... I don't know if you know, but we are investors..."
    pa1 "And we've been trying to expand..."
    pa1 "By the looks of this place, it could use a good touch."
    pa1 "We believe, that you are a better fit than Patrick ever was."
    pa1 "And thus, we may consider investing..."
    a "{i}...This place really needs some money...{/i}"
    scene 40-8 nopatrick 35 with Dissolve(1)
    a "Yeah... I just did a little check of the place, It sure could use some work."
    pa1 "Right... The thing is, we are torn between this Bar and a restaurant downtown called Abeleque."
    pa1 "It's this fine seafood place... But we can't make up our mind..."
    a "I see..."
    play music SexyTimeSong1
    scene 40-8 nopatrick 36 with Dissolve(1)
    pa1 "If you were... To persuade us... We'd be happy to invest in this place..."
    a "Oh..."
    menu:
        "I think I might have something you'd want...":
            label EP12_DeadPatrickBar_1_Sex:
            scene 40-8 nopatrick 37 with Dissolve(1)
            pa1 "What do you think, husband?"
            pa1 "Does she have what we want?"
            pa2 "How about we find out, hehe."
            scene 40-8 nopatrick 38 with Dissolve(1)
            a "I remember our previous meeting."
            a "How about we continue where we left off?"
            scene 40-8 nopatrick 39 with Dissolve(1)
            a "I have a special set of skills..."
            pa1 "I can imagine, heh."
            pa2 "{i}...Damn... My wife together with Anna... That's hot as fuck...{/i}"
            scene 40-8 nopatrick 40 with Dissolve(1)
            a "You look so precious..."
            scene 40-8 nopatrick 41 with Dissolve(1)
            a "I undoubtedly know something you'll like..."
            pa1 "Oh..."
            scene 40-8 nopatrick 42 with Dissolve(1)
            pause 2
            scene 40-8 nopatrick 43 with Dissolve(1)
            a "Would you like... If..."
            "Anna felt drawn to Mrs. Malory's lips..."
            scene 40-8 nopatrick 44 with Dissolve(1)
            a "Mm..."
            pa1 "Mhm..."
            "Mrs. Malory didn't protest."
            "She just let Anna have her way."
            scene 40-8 nopatrick 45 with Dissolve(1)
            pa2 "Damn..."
            pa2 "{i}...I could watch this all day...{/i}"
            "The man was getting harder with every passing second."
            "Watching his wife make out with another girl sent his rocket flying."
            scene 40-8 nopatrick 46 with Dissolve(1)
            pause 1
            scene 40-8 nopatrick 47 with Dissolve(1)
            a "How about you turn around... I'm just getting started."
            pa1 "Heh... Ok."
            play sound jacketcloth
            scene 40-8 nopatrick 48 with Dissolve(1)
            scene black with Dissolve(1)
            play sound undress
            scene 40-8 nopatrick 49 with Dissolve(1)
            pa2 "Fuck me... This is hot!"
            pa1 "You think so, husband?"
            scene 40-8 nopatrick 50 with Dissolve(1)
            pa2 "Yeah!"
            pa2 "You girls are hotter than I can even describe."
            a "{i}...Looks like both of them are enjoying this... Hehe...{/i}"
            scene 40-8 nopatrick 51 with Dissolve(1)
            a "Come... I want something..."
            play sound undress
            scene 40-8 nopatrick 52 with Dissolve(1)
            "Things were getting more intense with every moment."
            a "{i}...Oh... I'm getting very turned on...{/i}"
            a "{i}...I bet she'd want to go down there...{/i}"
            play sound cloth_sound1
            scene 40-8 nopatrick 53 with Dissolve(1)
            pause 1
            scene 40-8 nopatrick 54 with Dissolve(1)
            pa2 "Hey... Um... You know, I could also use a touch..."
            pa1 "Heh... You wish..."
            pa1 "Don't even think about it, just sit back and watch..."
            pa1 "This time..."
            scene 40-8 nopatrick 55 with Dissolve(1)
            pa1 "The girls wanna have some fun now."
            a "Hehe... Oh, yeah."
            scene 40-8 nopatrick 56 with Dissolve(1)
            pa1 "I wonder what's hiding here..."
            a "You are welcome to find out."
            pa1 "I bet something wet..."
            play sound undress
            scene 40-8 nopatrick 57 with Dissolve(1)
            pause 1.5
            scene 40-8 nopatrick 58 with Dissolve(1)
            a "Well... Come on then..."
            a "I know you want to."
            pa1 "Do you allow me, Anna?"
            a "Yes."
            scene 40-8 nopatrick 59 with Dissolve(1)
            "Mr. Malory had pulled out his cock while the ladies were enjoying each other."
            pa2 "Fuck yeah!"
            pa2 "Come on, hun. Give it to her!"
            scene 40-8 nopatrick 60 with Dissolve(1)
            pa1 "Such a hot pussy..."
            pa1 "I bet everyone wants to have a piece of this."
            a "You're right..."
            a "But you are special."
            scene 40-8 nopatrick 61 with Dissolve(1)
            a "{i}...Mm... This is so naughty...{/i}"
            a "{i}...She just can't take her eyes off of it...{/i}"
            pa1 "I've been waiting for this moment for a long time..."
            play sound licking_2
            scene 40-8 nopatrick 62 with Dissolve(1)
            pa1 "Mmm..."
            play sound femmoan_1
            a "Ah!"
            a "Yeah..."
            play audio jerk3 loop
            scene 40-8 nopatrick 63 with Dissolve(1)
            a "Ah..."
            a "Just like that..."
            a "{i}...Her tongue is magical...{/i}"
            play sound femmoan
            a "{i}...She eats it like a pro...{/i}"
            scene 40-8 nopatrick 64 with Dissolve(1)
            a "Hehe..."
            a "{i}...Look at him... He's so hard...{/i}"
            play sound femmoan
            a "{i}...I bet he'd want to fuck her from the back while I look at him...{/i}"
            a "{i}...This is so hot...{/i}"
            scene 40-8 nopatrick 65 with Dissolve(1)
            pa2 "Ho, Fuck..."
            pa2 "You bitches are so hot..."
            play sound female_moan_2
            pa2 "My wife just licking some stranger's pussy..."
            pa2 "Keep doing it hon... I'm here hard as a rock!"
            scene 40-8 nopatrick 66 with Dissolve(1)
            pa1 "Mmm..."
            play sound female_moan_1
            a "OH..."
            scene 40-8 nopatrick 67 with Dissolve(1)
            play sound female_moan_3
            a "So good..."
            a "You do it like a pro..."
            pa1 "Mhmmm..."
            scene EP12_Malory_Anim_1 with Dissolve(0.5)
            pause
            a "Oh... Do this..."
            a "Yeah..."

            scene 40-8 nopatrick 68 with Dissolve(1)
            play sound female_moan_4
            a "Fuck!"
            a "I'm getting close!!"
            a "So good!!!"
            scene EP12_Malory_Anim_2 with Dissolve(0.5)
            pause
            "The intense stimulation was rushing through Anna's body."
            "She didn't need much to cum... And she loved it."
            a "OH!!"
            scene EP12_Malory_Anim_3 with Dissolve(0.5)
            pause
            a "OOh... Pleeassseee... Don't stop!!!!"
            a "AH. AH. AH."
            scene 40-8 nopatrick 69 with flash_vpunch
            a "Fuck!"
            play audio female_moan_5
            with flash
            a "MMMM!!"
            with flash
            with flash
            a "AAAAAAAHHHHH"
            with flash
            with flash
            pause 3
            scene 40-8 nopatrick 70 with Dissolve(1)
            pa1 "Hehe... You liked that?"
            a "Oh... I'm sweaty now."
            pa1 "I'm glad you enjoyed yourself."
            scene 40-8 nopatrick 71 with Dissolve(1)
            pa1 "I think you've persuaded us."
            a "Well then..."
            a "I'm glad we can do business."
            pa1 "But... We will need more negotiations."
            a "I can do that."
            scene 40-8 nopatrick 72 with Dissolve(1)
            pa2 "Yeah. Me, too!"
            a "Hehe."
            pa1 "Ha."
            scene black with Dissolve(1)
            play sound undress
            scene 40-8 nopatrick 73 with Dissolve(1)
            pa1 "I'd say, our business talks went really well."
            pa2 "They did, indeed."
            a "Well, then to a prosperous future!"
            scene 40-8 nopatrick 74 with Dissolve(1)
            pa1 "We should meet up and discuss this further soon."
            a "Sure."
            pa1 "I will give you a call."
            pa2 "Damn, honey... I'm so turned on now!"
            pa1 "But now we gotta run."
            pa1 "More business to attend to."
            a "Is it any similar to this?"
            pa1 "Oh... Only you, Anna."
            play sound door2
            scene 40-8 nopatrick 75 with Dissolve(1)
            pa1 "Take care!"
            pa1 "See you soon!"
            a "Bye!"
            $ renpy.end_replay()
            scene 40-8 nopatrick 76 with Dissolve(1)
            j3 "So... What happened back there?"
            a "{i}...If only he knew...{/i}"
            a "We got business partners."
            scene 40-8 nopatrick 77 with Dissolve(1)
            j3 "Really?"
            a "Yeah. They investors. Might be willing to invest."
            j3 "That's good to hear."
            j3 "When can we expect this?"
            scene 40-8 nopatrick 78 with Dissolve(1)
            a "I will meet up with them again in the near future and close the deal."
            a "But probably as soon as possible."
            j3 "Good job, Anna!"
            j3 "This place will become more profitable now."
            a "I'm confident it will."
            a "Anyway. I will get going, other things to do."
            scene 40-8 nopatrick 79 with Dissolve(1)
            j3 "Catch you later. Will you come in tomorrow?"
            a "I will. Since I'm the new 'boss' and all."
            j3 "Damn straight!"
            a "Later, boys!"
            $ persistent.scene_37 = True
            pass
        "I can give better profits, this place gets pretty busy.":
            $ EP12_Bar_Couple_Refuse = True
            pa1 "But I still think it won't match what the restaurant brings in."
            a "Well... I don't know then..."
            pa1 "Huh... I thought you'd have a better pitch."
            a "Nope..."
            a "Sorry..."
            pa1 "In that case, we'll take our leave then..."
            scene 40-8 nopatrick 76 with Dissolve(1)
            j3 "So... What happened back there?"
            a "We tried to negotiate, but didn't get anywhere."
            scene 40-8 nopatrick 77 with Dissolve(1)
            j3 "Oh... Well... It is what it is."
            j3 "We could really use some new distribution networks."
            a "Yeah, based on the spreadsheet, the current ones are asking too much..."
            a "Will have to come up with something else."
            scene 40-8 nopatrick 78 with Dissolve(1)
            a "I will put my mind to it a bit later."
            a "We still floating above the water."
            j3 "Thanks."
            j3 "Let's act fast, though."
            a "Anyway. I will get going, other things to do."
            scene 40-8 nopatrick 79 with Dissolve(1)
            j3 "Catch you later. Will you come in tomorrow?"
            a "I will. Since I'm the new 'boss' and all."
            j3 "Damn straight!"
            a "Later, boys!"
            pass
    jump EP12_Taxman
label EP12_Taxman:
    $ EP12_var_13 = True
    play sound phonecall
    play music PPMEtheralEternity
    scene 40-4 taxman 1-1 with Dissolve(1)
    a "Huh... It's Taxman..."
    scene 40-4 taxman 1-2 with Dissolve(1)
    t2 "Hello, Anna..."
    t2 "We have to meet..."
    a "Do I have much choice?"
    t2 "Well... I'm already here..."
    play sound surprise
    scene 40-4 taxman 1-3 with Dissolve(1)
    a "..."
    scene 40-4 taxman 1 with Dissolve(1)
    "Anna enters Taxman's car, expecting something ominous..."
    t2 "Anna... It's been quite some time."
    scene 40-4 taxman 2 with Dissolve(1)
    a "Yeah..."
    a "So, what did you contact me about?"
    scene 40-4 taxman 3 with Dissolve(1)
    "Taxman looked Anna up and down... fantasizing..."
    if TaxmanHelps == True:
        t2 "We still have some unfinished business."
        t2 "I got you out of jail, didn't I?"
    else:

        t2 "Long time no see, eh?"
        a "Hello... It's been some time, indeed..."
        t2 "Remember Paul?"
        a "Of course I do, I just thought we put it behind us."
        t2 "It was quite an expensive decision for me."
        t2 "I need to equalize that, and you I think you could help me..."
    scene 40-4 taxman 4 with Dissolve(1)
    if TaxmanHelps == True:
        a "You did..."
        t2 "And I told you you'd owe me a favor, didn't I?"
        t2 "Now I've come to collect."
    else:
        a "Since most of what you do is illegal... What can I help you with?"
        a "And why are you coming to me like this?"
        t2 "Who else? You've been busy..."
    scene 40-4 taxman 5 with Dissolve(1)
    if TaxmanHelps == True:
        t2 "Don't worry, I won't ask much of you right now, since you already let me enjoy a little bit."
        t2 "It didn't, however, settle our debts completely, thus I'm here."
    else:
        if EarlHelp == True:
            t2 "Took down Sergey's empire..."
            t2 "Impressive work, by the way."
        if CarlHelps == True:
            t2 "You've helped make Sergey's empire stronger and now it's unopposed, Mendoza's dead."
            t2 "Very impressive, that helps my plans along as well."
    scene 40-4 taxman 6 with Dissolve(1)
    a "Alright, what do you have in mind?"
    t2 "Glad we're on the same boat."
    scene 40-4 taxman 7 with Dissolve(1)
    t2 "Simple, really. We are at a local restaurant."
    t2 "A decent establishment."
    t2 "But my operation cannot ignore it any longer."
    scene 40-4 taxman 8 with Dissolve(1)
    t2 "You see, the man inside is struggling with his business, but my attempts to persuade him have failed."
    t2 "He's as stubborn as he's righteous."
    t2 "But I've got a new weapon."
    scene 40-4 taxman 9 with Dissolve(1)
    a "Me?"
    t2 "Correct."
    t2 "My last shot before using more violent means of obtaining his business."
    a "Seriously?"
    t2 "He would earn a lot of money if he played ball."
    a "So what exactly do you want?"
    scene 40-4 taxman 10 with Dissolve(1)
    t2 "I want you to persuade him to meet with me... And you, for a dinner tomorrow to discuss business."
    t2 "I want to establish an illegal gambling den within his business."
    if TaxmanHelps == True:
        a "And then my debt will be settled?"
        t2 "First, persuade him, then we'll talk about it."
        a "Ok..."
    else:
        a "So I will get paid for this?"
        t2 "If you succeed..."
        t2 "Remember, you will only get paid if you persuade him and we get the final meeting with him."
    a "Here goes nothing."
    play sound door2
    scene 40-4 taxman 11 with Dissolve(1)
    "The cafe was empty..."
    "Like Taxman had said... It was struggling with clientele."
    scene 40-4 taxman 12 with Dissolve(1)
    t2 "That's a sweet piece of ass..."
    t2 "She's got this, I'm sure I got the right woman for the job."
    scene 40-4 taxman 13 with Dissolve(1)
    pause 1
    scene 40-4 taxman 14 with Dissolve(1)
    a "{i}...Alright, let's do it...{/i}"
    "Anna walked up to him with confidence, at first."
    scene 40-4 taxman 15 with Dissolve(1)
    sh_1 "We are about to close... Sorry..."
    a "Umm... yeah..."
    a "I'm not here about that..."
    scene 40-4 taxman 16 with Dissolve(1)
    sh_1 "She who does not know what she seeks is bound to wander forever."
    a "I... I mean I'm here for something else."
    sh_1 "Oh?"
    scene 40-4 taxman 17 with Dissolve(1)
    a "I've heard your business is struggling."
    sh_1 "From who?"
    a "That's the word on the street."
    sh_1 "That bad, huh?"
    scene 40-4 taxman 18 with Dissolve(1)
    sh_1 "What exactly, do you wish to do about it?"
    a "Well..."
    a "You need help, outside help."
    sh_1 "No one is willing to invest in this place..."
    scene 40-4 taxman 19 with Dissolve(1)
    a "Are you absolutely sure?"
    sh_1 "Well... Not anyone decent..."
    sh_1 "I've been approached by 'Taxman' or whatever they call him."
    a "Perhaps you'd be willing to reconsider?"
    scene 40-4 taxman 20 with Dissolve(1)
    sh_1 "What?"
    sh_1 "That man is a scoundrel, a criminal."
    a "Well... All he wants to do is have a meeting with you."
    sh_1 "And then what? Turn my restaurant into a den of crime, sin, and depravity?"
    scene 40-4 taxman 21 with Dissolve(1)
    a "You'd earn good money, and you'd be able to continue to support your business."
    a "All we ask for is a dinner meeting."
    scene 40-4 taxman 22 with Dissolve(1)
    a "And if you are not convinced by then, we'd walk away."
    sh_1 "Just like that?"
    sh_1 "Taxman doesn't just walk away..."
    scene 40-4 taxman 23 with Dissolve(1)
    sh_1 "I don't think this will happen."
    scene 40-4 taxman 24 with Dissolve(1)
    a "Please, reconsider..."
    a "I would be attending this dinner meeting, too..."
    a "As his assistant..."
    a "You being there would make me very happy..."
    scene 40-4 taxman 24-1 with Dissolve(1)
    sh_1 "Happy... Eh?"
    a "Yeah..."
    scene 40-4 taxman 25 with Dissolve(1)
    a "Taxman has your best interest at heart..."
    a "And he's willing to make compromises..."
    sh_1 "You think so?"
    scene 40-4 taxman 26 with Dissolve(1)
    a "Yeah..."
    a "And remember, your business would still be able to survive."
    a "We will all come out on top, actually."
    scene 40-4 taxman 27 with Dissolve(1)
    "Anna was tightening the grip on his mind..."
    sh_1 "..."
    a "{i}...Come on, please accept...{/i}"
    sh_1 "Well..."
    sh_1 "There'd have to be safe guards..."
    sh_1 "{i}...But this girl... Ugh, she's hot... I can barely hold my cold shoulder...{/i}"
    scene 40-4 taxman 28 with Dissolve(1)
    sh_1 "And he'd be willing to adapt?"
    a "Sure... like I said. Compromises."
    sh_1 "Hmm... alright..."
    scene 40-4 taxman 29 with Dissolve(1)
    a "Really?"
    sh_1 "Yeah... If you'll be there..."
    a "Of course, sir... That's a promise."
    scene 40-4 taxman 30 with Dissolve(1)
    a "If we come to an agreement, this place could be reinvented."
    a "Just imagine it."
    a "And I will help you along the way."
    scene 40-4 taxman 31 with Dissolve(1)
    sh_1 "You will, huh?"
    a "Of course. I will also be sure to make your meeting with us as worthwhile as possible."
    sh_1 "Hehe... I will keep that in mind..."
    sh_1 "Alright, I will meet with you guys. Tomorrow."
    a "That is great to hear."
    a "Taxman will send the details to you."
    scene 40-4 taxman 32 with Dissolve(1)
    a "Take care for now."
    sh_1 "Hold on, I didn't catch your name?"
    a "It's Anna."
    sh_1 "Nice to meet you, Anna."
    a "Nice to meet you, too."
    scene 40-4 taxman 33 with Dissolve(1)
    sh_1 "{i}...Damn...{/i}"
    scene black with Dissolve(1)
    play sound door2
    scene 40-4 taxman 34 with Dissolve(1)
    t2 "How'd it go?"
    a "Well, I got us a meeting."
    t2 "Haha... Great."
    a "We've got a meeting for tomorrow."
    a "He wants me to be there, too."
    a "Well, I kind of promised."
    scene 40-4 taxman 35 with Dissolve(1)
    t2 "Oh, Anna..."
    t2 "Well, now you gotta be there."
    a "I see..."
    a "But then we're done?"
    t2 "If you choose to."
    scene 40-4 taxman 37 with Dissolve(1)
    if TaxmanHelps == True:
        t2 "Don't think I've forgotten our previous encounter..."
        t2 "I hope you're discreet about it?"
        a "I have been, yes..."
    else:
        t2 "Trust me, if you want friends in high places, you'll continue our partnership."
    scene 40-4 taxman 38 with Dissolve(1)
    "Anna felt a bit uncomfortable."
    "But she saw the opportunity in this."
    scene 40-4 taxman 39 with Dissolve(1)
    a "Alright, are we done here?"
    t2 "Yes, we are."
    t2 "Come, I'll take you home."
    play sound carsound2
    scene black with Dissolve(1)
    jump EP12_Episode_End
label EP12_Rebecca_Yoga:
    $ EP12_var_10 = True
    play music chill_song_3
    scene 40-9 yoga 1 with Dissolve(1)
    r1 "Hey! Good that you decided to meet up."
    r1 "Crazy times, huh?"
    a "Yeah..."
    scene 40-9 yoga 2 with Dissolve(1)
    a "How are you holding up?"
    r1 "Seeing you makes my day better."
    if EarlHelp == True:
        r1 "{i}...Gotta show Anna that I'm strong...{/i}"
    r1 "But, yeah... How's your yoga?"
    a "Rusty?"
    r1 "Hehe... We'll get you going in no time."
    scene 40-9 yoga 3 with Dissolve(1)
    r1 "Hey... I'm Rebecca, we had an appointment today."
    n1 "Welcome, Rebecca. Good to see that brought a friend."
    r1 "That's my sister."
    n1 "Even better."
    n1 "You can go get changed. I will be with you shortly."
    scene 40-9 yoga 4 with Dissolve(1)
    a "You come here often?"
    r1 "Occasionally."
    r1 "When I need to do some mind and body type of stuff."
    a "Ah, I see."
    scene black with Dissolve(1)
    play sound undress
    scene 40-9 yoga 5 with Dissolve(1)
    a "There we go."
    a "So... You said you wanted to talk about something?"
    r1 "Yeah... Well... Heh."
    r1 "You know how I do stuff with Dilan, too?"
    scene 40-9 yoga 6 with Dissolve(1)
    a "Modeling, right?"
    r1 "Sure."
    r1 "Well... I've been thinking... Perhaps I need to..."
    r1 "Expand my horizons."
    scene 40-9 yoga 7 with Dissolve(1)
    a "You mean like..."
    r1 "Porno..."
    a "Oh. Well... I ain't surprised..."
    a "I thought you'd already be doing something like that."
    play sound jacketcloth
    scene 40-9 yoga 8 with Dissolve(1)
    r1 "Huh... You really think of me like that?"
    a "No, I just know you. Hehe..."
    r1 "Fair enough."
    scene 40-9 yoga 9 with Dissolve(1)
    a "So, was that what you wanted to talk about?"
    r1 "Umm... I wanted to ask..."
    scene 40-9 yoga 10 with Dissolve(1)
    n1 "Hello and Welcome."
    n1 "Today's keyword is mindfulness."
    n1 "We all need mindfulness in our lives."
    n1 "So we will practice some mindfulness techniques and poses today."
    n1 "I would like you all to get on all fours."
    scene 40-9 yoga 11 with Dissolve(1)
    n1 "Yeah... Just like that."
    a "{i}...I don't remember the last time I did some yoga...{/i}"
    n1 "You are doing wonderful."
    n1 "So the first pose we will do is frog pose."
    scene 40-9 yoga 12 with Dissolve(1)
    r1 "Anyway... Would you want to join me for a... scene..."
    play sound surprise
    a "Huh?"
    r1 "Yeah... Umm... It's like a foursome scene, but... I can't find the second girl..."
    a "Wow..."
    scene 40-9 yoga 13 with Dissolve(1)
    a "You think that's a good idea?"
    r1 "Why not?"
    a "I don't know..."
    r1 "As far as I know, we wouldn't be doing anything like that..."
    r1 "We'd just be in the same room and well... Having some fun..."
    a "Naughty, naughty."
    scene 40-9 yoga 14 with Dissolve(1)
    n1 "Yes, like that."
    n1 "You guys are doing great."
    n1 "Now, breath in..."
    n1 "Breath out... Be mindful of yourself, how you breathe... Your wellbeing."
    scene 40-9 yoga 15 with Dissolve(1)
    r1 "So... Would you be willing to do it?"
    a "Um... I don't know..."
    a "Quite a leap..."
    r1 "Well, the money's nice."
    if EarlHelp == True:
        r1 "I'm in desperate need."
    else:
        r1 "With the boys out of town... And Michael on my shoulders..."
    scene 40-9 yoga 16 with Dissolve(1)
    a "I suppose..."
    menu:
        "Anna agrees to participate.":
            $ EP12_Rebecca_Accept_Offer = True
            a "We can do it."
            r1 "Really?"
            r1 "That's awesome..."
            a "But... you know..."
            r1 "Yeah, yeah... I know, it's fine!"
        "Anna doesn't want to participate.":
            a "I don't want to..."
            a "Doesn't seem right."
            r1 "Huh... That's a bummer..."
            a "I'm sorry, sis."
            r1 "No, No worries."
    scene 40-9 yoga 17 with Dissolve(1)
    n1 "Breath in..."
    n1 "Breath out..."
    a "How is Michael?"
    r1 "He is healing surprisingly fast..."
    scene 40-9 yoga 18 with Dissolve(1)
    r1 "I guess the bullet grazed him?"
    a "Or maybe he is superhuman?"
    r1 "Hehe... I wouldn't put that behind him..."
    r1 "Definitely superhuman in bed..."
    a "Rebecca!"
    scene 40-9 yoga 19 with Dissolve(1)
    a "What about Carl?"
    r1 "Oh... Umm... He doesn't mind..."
    a "You sure about that?"
    r1 "Maybe."
    scene 40-9 yoga 20 with Dissolve(1)
    n1 "Alright, girls."
    n1 "That will be all for our mindfulness class today."
    a "That went by fast."
    n1 "Time flies when you're having fun."
    scene 40-9 yoga 21 with Dissolve(1)
    if EP12_Rebecca_Accept_Offer == True:
        r1 "So, will you join me for the shoot with Dilan?"
        a "Yeah, when is it?"
        r1 "Not sure, will give him a call a bit later."
        r1 "Thank you, you're kind of saving my hide."
        if EarlHelp == True:
            r1 "Now that we are in this shitty situation, I have to take care of myself and Michael..."
            a "Yeah... that is unfortunate..."
        else:
            r1 "While Carl is in hiding... I gotta find a way to take care of stuff..."
            a "Yeah... Makes sense."
    else:
        r1 "Sad that you won't be joining me at the shoot."
        a "Eh... I'm sorry... That's a bit too much for me."
        r1 "I will manage."
    scene black with Dissolve(1)
    play sound undress
    scene 40-9 yoga 22 with Dissolve(1)
    r1 "Well, time to get going."
    r1 "Thanks for joining me today."
    r1 "It was a nice change of pace."
    a "Sure was!"
    scene 40-9 yoga 23 with Dissolve(1)
    a "Come here."
    a "Everything will be fine."
    r1 "Your embrace helps me... Thanks, Anna."
    a "Anytime, dear."
    scene black with Dissolve(1)
    if ashley_var_2 == False:
        $ EP12_var_9 = True
        jump EP12_Logic_Gate
    else:
        jump EP12_Lenny_Scene
label EP12_Logic_Gate:
    if bar_var_1 == False:
        jump EP12_DeadPatrickBar_1
    else:
        jump EP12_Bar_1
    return

label EP12_Episode_End:
    scene black with Dissolve(1)
    jump EP13_Begin
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
