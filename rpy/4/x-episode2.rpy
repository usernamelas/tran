image ep2_104 = Movie(play="video/episode2/104.webm", loop=True)
image ep2_105 = Movie(play="video/episode2/105.webm", loop=True)
image ep2_106 = Movie(play="video/episode2/106.webm", loop=True)
image ep2_107 = Movie(play="video/episode2/107.webm", loop=True)
image ep2_204 = Movie(play="video/episode2/204.webm", loop=True)
image ep2_205 = Movie(play="video/episode2/205.webm", loop=True)
image ep2_206 = Movie(play="video/episode2/206.webm", loop=True)
image ep2_207 = Movie(play="video/episode2/207.webm", loop=True)
image ep2_303 = Movie(play="video/episode2/303.webm", image="images/episode2/303.webp", loop = False)

label episode2:
    stop music fadeout 4.0
    scene expression ("images/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(1, 2) with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_newEpisode

    show screen ui_message("Tuesday") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    call episode2_chooseJob from _call_episode2_chooseJob

    call episode2_pilates from _call_episode2_pilates

    call episode2_tvTris from _call_episode2_tvTris

    if toby_job == 0:
        call episode2_realEstate from _call_episode2_realEstate
    else:

        call episode2_club from _call_episode2_club

    call episode2_drinkMom from _call_episode2_drinkMom

    call episode2_trisNight from _call_episode2_trisNight

    return


label episode2_chooseJob:
    $ progress = 18


    scene expression ("images/episode2/001.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmmm. I wonder, what should I do. Who should I call?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}On one hand, calling Darlene would mean a more stable job, without so many complications.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}However working for Katrina might affect me in some way, but I'm sure that it would be fun.{/i}"

    "{color=#FDCA6E}Be careful. The decision you are about to make will have a big impact on the development of the character. Choose the life that suits you better.{/color}"

    menu:
        "{i}call Darlene for the Real Estate Job{/i}"(csq="Gallery Image"):
            $ toby_job = 0
            $ unlockImage(persistent.darlene_02)
            scene expression ("images/episode2/002.webp") with dissolve
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nHello?"
            toby "Good morning, ma'am. It's me [toby!c]. We met yesterday, and you told me to call you."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nOh, [toby!c]. I think I already told you to call me Darlene. I'm not that old yet!"
            toby "Sorry, Darlene."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nAnyway, I'm glad you called. Please tell me you didn't call just to say that you're going to work for my girlfriend."
            toby "No, I haven't. I called to tell you that I'm interested in working for you."
            scene expression ("images/episode2/003.webp") with dissolve
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nYou did the right thing."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nWhat are you doing this afternoon around 4PM?"
            toby "I haven't made any plans because you told me yesterday that we are going to sell an apartment."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nI told you that we are going to try and sell an apartment, but I like your enthusiasm."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nDo you have a car?"
            scene expression ("images/episode2/002.webp") with dissolve
            toby "Not really, but I think I can borrow my [mother]'s car."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nNo need!"
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nText me the address. I'll come to pick you up at 03:30PM."
            toby "Sure!"
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nOkay then. See you at 03:30PM."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nAnd [toby!c], make sure you're wearing something nice. We need to make a good impression on our clients!"
            toby "Of course."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nHave a good day, [toby!c]. See you later!"
            toby "Bye, bye!"
            scene expression ("images/episode2/004.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I better send her my address.{/i}"
            scene expression ("images/episode2/005.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I hope I made the right choice. Let's see how working for Darlene will play out.{/i}"
            pass
        "{i}call Katrina for shady business{/i}"(csq="Gallery Image"):

            $ toby_job = 1
            $ unlockImage(persistent.katrina_02)
            scene expression ("images/episode2/002.webp") with dissolve
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nYeah?"
            toby "Good morning ma'am. It's me [toby!c]. Yesterday you gave me a piece of paper with this number on it."
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nOh my, [toby!c]. I really thought my girlfriend stole you from me!"
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nSo? Are you ready to make some money and have fun at the same time?"
            toby "I guess so, but I'm not sure what I need to do."
            scene expression ("images/episode2/003.webp") with dissolve
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nLet's meet later at my office, and I'll tell you everything you need to know."
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nThe important part is that you please me!"
            toby "Uhm... Okay."
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nUhm...? Okay? What is that shit? You're working for me now! I don't want to hear you being unsure. I need men, not boys!"
            toby "Sorry ma'am!"
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nSorry? My men are never sorry. Tonight I'll be finding your lost balls. You do have balls, don't you?"
            menu:
                "{i}be arrogant{/i}":
                    toby "Wanna taste them?"
                    katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nI'm a lesbian, but I like your confidence, and if you're a good boy, I just might try them!"
                "{i}act normal{/i}":

                    toby "Yes ma'am, I have big balls!"
                    katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nThat's much better."
            scene expression ("images/episode2/002.webp") with dissolve
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nDo you have a car?"
            toby "No, not yet, we had to sell our cars."
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nThat sucks. I'll send one of my men to come to pick you up. Text me the address!"
            toby "You don't have to do that, I can take the bus."
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nBullshit! My men will not be seen taking the bus!"
            toby "Okay then. I'll text you my address!"
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nPerfect. See you later."
            toby "Bye, bye!"
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nAnd by the way..."
            toby "Yeah?"
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nI'm going to make a man out of you, just you wait!"
            toby "..."
            scene expression ("images/episode2/004.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I better send her my address.{/i}"
            scene expression ("images/episode2/005.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I hope I made the right choice. Katrina sounds a little bit shady, but at the same time, very intriguing.{/i}"
            pass


    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think I should tell [mom] how the phone call went. I'm sure she'd like to know.{/i}"

    return

label episode2_pilates:
    $ progress = 19


    scene expression ("images/episode2/006.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the hell is she doing?{/i}"
    scene expression ("images/episode2/007.webp") with dissolve
    toby "Morning, [mom]. What are you doing?"
    scene expression ("images/episode2/008.webp") with dissolve
    charlotte "Morning, sweetie. I'm doing Pilates."
    scene expression ("images/episode2/007.webp") with dissolve
    toby "I might be wrong, but shouldn't there be a ball instead of that chair for doing Pilates?"
    scene expression ("images/episode2/008.webp") with dissolve
    charlotte "Well, yes, but if you cannot find the ball because you just moved, it's safe to say that using a chair is the next best thing."
    scene expression ("images/episode2/009.webp") with dissolve
    toby "Sucks to be you!"
    charlotte "Oh really? That's how you wanna play this. So you think I shouldn't use the chair?"
    toby "I'm just saying. Maybe use something more comfortable."
    scene expression ("images/episode2/010.webp") with dissolve
    charlotte "I think I have just found the most comfortable thing to use as a replacement for my ball!"
    scene expression ("images/episode2/011.webp") with dissolve
    toby "I think the chair was a good replacement."
    charlotte "No. You were right, my back hurts a bit from it. So why don't you help your [mother] in need!"
    scene expression ("images/episode2/012.webp") with dissolve
    toby "I'm not [dad]. Your puppy eyes won't work on me."
    charlotte "No? Really? Not at all?"
    toby "Nope!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I gotta be honest, she's kinda cute though.{/i}"
    charlotte "Okay then. We'll play by different rules."
    scene expression ("images/episode2/013.webp") with dissolve
    charlotte "As long as you live in my house, you'll do what I say!"
    toby "Don't you think that's a bit unfair?"
    charlotte "I'm telling you what's unfair. Me not finding that ball."
    scene expression ("images/episode2/014.webp") with dissolve
    charlotte "Just keep your hands like this."
    toby "I'm gonna file a complaint with Child Protective Services. I feel used."
    scene expression ("images/episode2/015.webp") with dissolve
    charlotte "You're no longer a kid. You're a young adult. If you don't like how your [mother] treats you, you can always move!"
    toby "You're gonna miss me so much."
    charlotte "Of course I am, but it's not like you know how to cook, so I figure even if you move out, you'll still come back every morning to eat."
    toby "Does this pose actually do anything for you?"
    scene expression ("images/episode2/016.webp") with dissolve
    charlotte "How should I know? That's what my personal trainer told me to do. Just stay still like this with my hands on that ball!"
    toby "Let me get this straight, you've done Pilates for 5 years, and you still don't know why you're doing things like this?"
    scene expression ("images/episode2/017.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    charlotte "What do you think? Do I look okay for my age?"
    toby "Yes, but you always looked this good even before doing Pilates."
    charlotte "You have a point, but I'm not falling for it."
    scene expression ("images/episode2/018.webp") with dissolve
    toby "Falling for what?"
    label memory_03:
        if _in_replay:

            scene expression ("images/utils/black.png") with dissolve
            menu:
                "Choose your job"
                "Real Estate Agent":
                    $ toby_job == 0
                "Club Manager":
                    $ toby_job == 1
            scene expression ("images/episode2/018.webp") with dissolve

        charlotte "Just hold my feet."
        scene expression ("images/episode2/019.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}[mom!c]'s ass is huge!{/i}"
        scene expression ("images/episode2/020.webp") with dissolve
        charlotte "I know you want to me to stop Pilates today, not because you think it's useless, but because you don't want to help your sweet [mother] when she needs."
        toby "Now you're playing the victim here. You're not a victim, so stop acting like it!"
        scene expression ("images/episode2/021.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why am I staring at her ass.{/i}"
        if ep1_groping_charlotte == True:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Ever since yesterday I'm looking at [mom] in a different way and it feels so wrong.{/i}"
        charlotte "So did you call that lady about the job?"
        toby "Yes, I called her. I'm getting picked up at 3:30 this afternoon."
        scene expression ("images/episode2/022.webp") with dissolve
        charlotte "I hope you're talking about the real estate job."
        if toby_job == 0:
            scene expression ("images/episode2/023.webp") with dissolve
            toby "Of course. It was the smart thing to do!"
            charlotte "Glad to hear that my [son] is smart! So what will you be doing today?"
            toby "As far as I understood, we'll go sell an apartment...or at least try to."
            scene expression ("images/episode2/024.webp") with dissolve
            charlotte "I like how you said 'we' like you're going to do anything."
            toby "Who knows, maybe I will!"
            charlotte "And then you'll be rich and marry a good-looking girl, just like your [dad] did."
            scene expression ("images/episode2/025.webp") with dissolve
            toby "Did you marry [dad] because of his money?"
            charlotte "Of course not! I really loved him. Although, it was also nice getting all those gifts!"
        else:

            scene expression ("images/episode2/023.webp") with dissolve
            toby "Not quite. I feel like my life has been pretty boring up to this point, so working in a club might spice things up!"
            charlotte "I can't say I'm happy for you, because working in a club is fun when you're young, but what will happen in 10 years when you'll need a real job with a steady income for your family?"
            toby "Don't worry. Everything will be fine. We'll cross that bridge when we come to it!"
            scene expression ("images/episode2/024.webp") with dissolve
            charlotte "I'm going to hope you find someone rich someday and marry them, just like I did!"
            toby "You married [dad] for money?"
            charlotte "Of course not, but him buying me all those expensive things sure did help!"
            toby "You were such a gold digger!"
            scene expression ("images/episode2/025.webp") with dissolve
            charlotte "I was not. I really loved your [dad], but it was nice getting expensive gifts."

        scene expression ("images/episode2/026.webp") with dissolve
        toby "Loved? You're not in love with him anymore?"
        charlotte "Of course I still love him, but yeah, it's not like before."
        toby "That sounds like bullshit to me. When I get married I'll love my wife more with each day."
        scene expression ("images/episode2/027.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        charlotte "And she'll be one lucky lady."
        toby "Are we done with the Pilates?"
        charlotte "Only one pose left, but try not to let me fall, this one is a bit more complicated!"
        scene expression ("images/episode2/028.webp") with dissolve
        toby "Have you meet my friends? I can hold you any pose you want."
        charlotte "Oh my, if only I was a few years younger."
        scene expression ("images/episode2/029.webp") with dissolve
        charlotte "Don't let me fall!"
        toby "Of course [mom]. Don't worry. Just do your thing!"
        scene expression ("images/episode2/030.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}[mom!c] is heavier than I expected. How much did she eat this morning?{/i}"

        scene expression ("images/episode2/031.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck me. I can see her huge boobs. Dammit, I'm gonna get a boner.{/i}"
        scene expression ("images/episode2/032.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Her boobs are so big and it was like they are looking at me.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why am I so horny when I think about my [mom]?{/i}"
        scene expression ("images/episode2/033.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... Of course I'm getting a boner now. I mean why not?{/i}"
        scene expression ("images/episode2/034.webp") with dissolve
        charlotte "Is that a boner?"
        scene expression ("images/episode2/035.webp") with dissolve
        toby "No. It's not!"
        scene expression ("images/episode2/036.webp") with dissolve
        charlotte "Ouch!"
        charlotte "I told you not to let me fall."
        toby "Sorry, I didn't mean to, I just..."
        scene expression ("images/episode2/037.webp") with dissolve
        charlotte "I can't remember the last time someone got a boner by looking at me."
        scene expression ("images/episode2/038.webp") with dissolve
        toby "What?"
        charlotte "I can't remember the last time I saw a boner."
        menu:
            "{i}say nothing{/i}" if not _in_replay:
                toby "Uhm..."
            "{i}[JGR]give her a compliment{/i}"(csq="Charlotte +1 & Gallery Image"):
                $ charlotte_rel += 1
                $ unlockImage(persistent.charlotte_04)
                toby "I'm sorry for that, it's just that you look really, really good, and it happens."

        scene expression ("images/episode2/039.webp") with dissolve
        charlotte "Go take a cold shower. You kinda need it but don't take too long. I also need a shower."
        toby ".{w}.{w}."
        charlotte "Thank you for your help."
        toby "Anytime?"
        scene expression ("images/episode2/040.webp") with dissolve
        charlotte "My pleasure."

        $ unlockMemory(persistent.memory_03)
        $ renpy.end_replay()


    scene expression ("images/episode2/041.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why did I listen to [mom] when she told me to take a cold shower. I'm freezing to death.{/i}"
    scene expression ("images/episode2/042.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Well, at least I'm not so horny anymore.{/i}"
    if charlotte_rel >= 3:
        scene expression ("images/episode2/043.webp") with dissolve
        charlotte "[toby!c], are you done honey?"
        toby "In a second [mom], I just need to get dressed."
        charlotte "You're dressed already? Okay then."
        scene expression ("images/episode2/044.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n{i}I said, I need to get dressed.{/i}"
        scene expression ("images/episode2/045.webp") with dissolve
        charlotte "Sorry honey. I thought you said you were dressed already."
        charlotte "It's not like I haven't seen everything before since you were a kid."
        toby "It's a bit different now."
        charlotte "It's only slightly bigger, but it's the same thing."
        scene expression ("images/episode2/046.webp") with dissolve
        toby "It's a lot bigger."
        charlotte "Not really. You were quite gifted even when you were young. I have no idea who you took after, because your [dad] is not that big."
        scene expression ("images/episode2/047.webp") with dissolve
        toby "Okay. I'm leaving."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I don't know what's up with her, but since we moved here she's been acting very strange.{/i}"

    return

label episode2_tvTris:
    $ progress = 20


    show screen ui_message("Later that day") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode2/048.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This city is so boring. I was excited when we moved here because I thought I would get to meet new people, but in reality, I'm just staying inside all day watching TV.{/i}"
    scene expression ("images/episode2/049.webp") with dissolve
    patricia "Hi [toby!c]."
    toby "Morning."
    scene expression ("images/episode2/050.webp") with dissolve
    patricia "Morning was about 6 hours ago. It's already afternoon."
    toby "Oh really? I didn't realize."
    scene expression ("images/episode2/051.webp") with dissolve
    patricia "What are you watching?"
    toby "Not sure. Something on the History channel."
    patricia "Boring."
    toby "How was school?"
    scene expression ("images/episode2/052.webp") with dissolve
    patricia "Awful. I just had my first English class with the principal of the school. At first I didn't understand why everybody called her Mrs. WyWHORE."
    toby "And why is that?"
    patricia "Because she's such a bitch! She's crazy. My pen broke, so I asked a classmate to let me borrow a pen."
    patricia "When she saw us talking she was like \"{i}I don't know how your previous school was, but here when a teacher speaks everybody listens{/i}\". I hate her already."
    scene expression ("images/episode2/053.webp") with dissolve
    patricia "It's not funny!"
    toby "Fine, fine. It's not."
    scene expression ("images/episode2/054.webp") with dissolve
    toby "And besides English, what other classes did you have?"
    patricia "Well, all of those were boring, except for PE."
    toby "Since when do you like sports?"
    patricia "I don't, but I just heard a rumor."
    toby "Do tell!"
    patricia "There's a rumor that the PE teacher used to be a stripper!"
    toby "Can't be true. I mean, she's a teacher, after all. I'm sure the principal would check her background before hiring her."
    patricia "You mean the principal who is now in prison for who knows what?"
    toby "I see your point."
    scene expression ("images/episode2/055.webp") with dissolve
    patricia "Do you know how to give hand massages?"
    toby "Even if I do, why do you think I'd give you one?"
    scene expression ("images/episode2/056.webp") with dissolve
    patricia "Because I'm your little [sister] and my hand hurts from too much writing."
    menu:
        "{i}[JGR]give her a hand massage{/i}"(csq="Tris +1 & Gallery Image"):
            $ patricia_rel += 1
            $ unlockImage(persistent.patricia_04)
            scene expression ("images/episode2/057.webp") with dissolve
            patricia "Thank you! You're the best big [brother] I could have ever asked for."
            toby "Is that all you got?"
            patricia "And I love you?"
            toby "I'll take it."
            scene expression ("images/episode2/058.webp") with long_dissolve
        "{i}refuse to give her a hand massage{/i}":

            scene expression ("images/episode2/059.webp") with dissolve
            toby "Not a chance."
            patricia "You're the worst [brother]."
            toby "Yeah, yeah!"
            scene expression ("images/episode2/060.webp") with dissolve
            patricia "But I'm still using your shoulder as a pillow."
            toby "Whatever."
            scene expression ("images/episode2/061.webp") with long_dissolve

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She must be really tired if she fell asleep that fast.{/i}"
    scene expression ("images/episode2/062.webp") with shake
    toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n{i}Ouch!{/i}"
    scene expression ("images/episode2/063.webp") with dissolve
    patricia "Sorry! Sorry! Sorry! I felt like I was falling and ..."
    patricia "Does it hurt?"
    toby "{size=12}{color=#FDCA6E}* in a low voice *{/color}{/size}\n{i}Maybe.{/i}"
    if patricia_rel >= 3:
        scene expression ("images/episode2/064.webp") with dissolve
        patricia "Do you want me to kiss your booboo?"
        toby "I think I'll manage, but next time I won't forgive you that easily."
        scene expression ("images/episode2/065.webp") with dissolve
        patricia "You perv! You'd let your little [sister] kiss your penis?"
        toby "I didn't say that, you just misinterpret everything."
        scene expression ("images/episode2/066.webp") with dissolve
        toby "The only perv around is you!"
        patricia "Am not!"
    else:

        scene expression ("images/episode2/065.webp") with dissolve
        patricia "What's there to hurt. If it was big, I would have felt it."
        toby "Wanna bet?"
        patricia "You perv! You would show your penis to your [sister]?"
        patricia "Ewww. Pervert! You really need a new girlfriend here in town because lately, you've been kinda horny!"
        scene expression ("images/episode2/066.webp") with dissolve
        toby "You touched my penis, and somehow I'm the perv."
        patricia "It was an accident!"

    scene expression ("images/episode2/067.webp") with dissolve
    toby "I would stay longer to argue with a perv like you, but I need to get ready for work."
    patricia "Really? You're starting already?"
    scene expression ("images/episode2/068.webp") with dissolve
    if toby_job == 0:
        toby "Yup! I need to be ready at 3:30 because my boss is coming to pick me up."
        patricia "Cool! So which job did you end up taking?"
        toby "The real estate job. I'm going to be the biggest real estate agent in town!"
        patricia "Boring."
        scene expression ("images/episode2/069.webp") with dissolve
        toby "Don't come to me begging for money when you want a new dress!"
        patricia "You're going to buy it yourself and surprise me? How thoughtful of you!"
        toby "Bye!"
    else:

        toby "Yup! I need to be ready at 3:30 because someone is coming to pick me up!"
        patricia "Cool! So which job did you end up taking?"
        toby "Do I look like a boring guy to you? Of course I picked the club."
        patricia "Now that you mention it, You do kinda look a bit dull. I don't see what that woman saw in you!"
        scene expression ("images/episode2/069.webp") with dissolve
        toby "Don't come to me begging for money when you want a new dress!"
        patricia "You're going to buy it yourself and surprise me? How thoughtful of you!"
        toby "Bye!"

    return

label episode2_realEstate:
    $ progress = 21


    scene expression ("images/episode2/070.webp") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/071.webp") with dissolve
    darlene "Hi there [toby!c]. Are you ready for your first sale?"
    toby "As ready as I'll ever be!"
    darlene "Perfect! Let's go to the apartment and I'll explain everything there."
    scene expression ("images/episode2/072.webp") with dissolve
    darlene "So. This is it!"
    darlene "This is the apartment we're going to sell."
    darlene "Before I give you a tour of the place, let me explain everything."
    darlene "So we're going to meet here with two ladies. I don't know both of their names, but the one who is actually looking to buy this apartment is Lisa. Our focus is Lisa."
    scene expression ("images/episode2/073.webp") with dissolve
    darlene "We don't care too much about the other one. Lisa is the one with the money."
    darlene "The listing price for the apartment is $110,000, and the lowest we can take is $100,000."
    darlene "If we go below 100k, we'll start losing money, and we don't want that."
    scene expression ("images/episode2/074.webp") with dissolve
    darlene "The apartment has one bedroom, a bathroom, and this open space which can be used as a kitchen, dining room, and living room."
    toby "Quick question, are there any parking spaces with this apartment."
    darlene "Great question. This apartment does come with one parking space, but if the client asks, we can sell a second spot for $5,000 because we own the whole building."
    scene expression ("images/episode2/075.webp") with dissolve
    "Knock, knock."
    scene expression ("images/episode2/076.webp") with dissolve
    darlene "They have arrived. So remember, no lower than $100,000."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why does she keep telling me that? I'm here just to watch!{/i}"

    scene expression ("images/episode2/077.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    woman "Hi. We spoke on the phone about the apartment."
    scene expression ("images/episode2/078.webp") with dissolve
    darlene "You must be Lisa, right?"
    lisa "Yes."
    darlene "And this gorgeous lady is?"
    lauren "Lauren."
    scene expression ("images/episode2/079.webp") with dissolve
    darlene "So this is [toby!c]. He's our best agent. He'll be the one to show you the apartment. Unfortunately, I have something pressing that needs my attention."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Say what? I'm her best agent my ass. It's my first day!{/i}"
    scene expression ("images/episode2/080.webp") with dissolve
    darlene "He's the kind of guy who can take care of everything."
    scene expression ("images/episode2/081.webp") with dissolve
    darlene "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I let him take care of everything and I'm always satisfied, so you're in good hands.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the fuck is she talking about? I thought the crazy one was Kat, not her!{/i}"
    menu:
        "{i}try to act normal{/i}":
            scene expression ("images/episode2/082.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I said... Act normal. Does this look normal to you?{/i}"
        "{i}[JGR]play along{/i}"(csq="Darlene +1 & Gallery Image"):

            $ darlene_rel += 1
            $ ep2_spankDarlene = True
            $ unlockImage(persistent.darlene_03)
            scene expression ("images/episode2/083.webp") with dissolve
            toby "I'll take care of everything from here."
            scene expression ("images/episode2/084.webp") with dissolve
            toby "I'll call you once the apartment is sold!"
            pass

    scene expression ("images/episode2/085.webp") with dissolve
    darlene "Okay then. I'll leave you to it!"
    scene expression ("images/episode2/086.webp") with dissolve
    toby "Sorry for that!"
    toby "So let me show you around the apartment."
    lisa "No worries."
    scene expression ("images/episode2/087.webp") with dissolve
    lauren "So how good in bed are you?"
    toby "Excuse me?"
    lisa "Shut up, Lauren."
    scene expression ("images/episode2/088.webp") with dissolve
    lauren "Oh please. Look at him. He's no older than us, yet he fucks his boss who is 20 years older than he is. He must be a great lay."
    toby "Uhum yes. As I was saying, let me show you around the apartment."
    scene expression ("images/episode2/089.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Will all the sales be this awkward?{/i}"

    show screen ui_message("A short time later") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/090.webp") with long_dissolve
    hide screen ui_message
    $ progress = 22
    toby "So? What do you think?"
    lisa "I like it very much. This is exactly what I was looking for. So what was the asking price again?"
    toby "Well, the apartment is worth $120,000, but for someone as smart and beautiful as you, I can go down to $110,000. What do you say?"

    scene expression ("images/episode2/091.webp") with dissolve
    lisa "Really? You'd do that for us?"
    lisa "Thank you!"
    toby "Just please don't tell my boss the reason I've dropped 10k."
    scene expression ("images/episode2/092.webp") with dissolve
    lauren "Not so fast. Since you could drop 10k just like that, I'm sure you can do better!"
    toby "Not really."
    scene expression ("images/episode2/093.webp") with dissolve
    lauren "You're negotiating with me now."
    toby "Uhm..."
    scene expression ("images/episode2/094.webp") with dissolve
    lauren "So what do you say. How does 109k sound?"
    scene expression ("images/episode2/095.webp") with dissolve
    lisa "Please tell me you're not going to suck him off."
    scene expression ("images/episode2/096.webp") with dissolve
    lauren "Why not? He's good-looking, and besides, I'm curious how big his cock is since his boss likes it so much!"

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is she really going to blow me in front of her friend? This chick is crazy.{/i}"
    scene expression ("images/episode2/097.webp") with dissolve
    lauren "So what do you say, \"Mr. employee of the month\", can I proceed with the negotiations?"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I cannot negotiate with both of them. What should I do?{/i}"
    scene expression ("images/episode2/097_lisa.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}If I am going to win Lisa over I'll need to reject her friend. She looks like she's had enough of her silly antics.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's more mature and by the looks of things, she's more into charming nice guys, not someone who's willing to get blown by any girl who offers.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I need to be polite and flirt in a classy, respectful way.{/i}"
    scene expression ("images/episode2/097_lauren.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}On the other hand, her friend is already on her knees, ready to suck my cock.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She must come from a poor family and since she can't compete with Lisa on the money side, she tries to balance it by doing stupid shit like this.{/i}"
    menu:
        "{i}let Lauren do her thing{/i} [JLA]"(csq="Lauren +1 & Gallery Image"):
            label memory_04:
                $ unlockImage(persistent.lauren_01)

                $ lauren_path = True
                $ ep2_laurenBlowjob = True
                $ lauren_rel += 1
                if _in_replay:
                    scene expression ("images/episode2/097_lauren.webp") with dissolve
                toby "So it's 109k at the moment."
                scene expression ("images/episode2/098.webp") with dissolve
                lauren "Good enough for me!"
                scene expression ("images/episode2/099.webp") with dissolve
                lauren "108k."
                scene expression ("images/episode2/100.webp") with dissolve
                lauren "107k."
                toby "Aren't you going a little bit too fast with the money?"
                scene expression ("images/episode2/101.webp") with dissolve
                lauren "I know how much my mouth is worth. You just enjoy, Mr."
                scene expression ("images/episode2/102.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode2/103.webp") with dissolve
                lauren "106k!"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}If she's keeps going like this, I might end up paying her to buy this apartment.{/i}"
                scene expression ("images/episode2/104.webp")
                show ep2_104
                lauren "Do you like handjobs, Mr. [toby!c]?"
                toby "Who doesn't?"
                lauren "Cool! It's 105K then."
                scene expression ("images/episode2/105.webp")
                hide ep2_104
                show ep2_105
                toby "Let me guess. 104k?"
                lauren "You're right!"
                scene expression ("images/episode2/106.webp")
                hide ep2_105
                show ep2_106
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck me, this is the best blowjob ever.{/i}"
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode2/107.webp")
                hide ep2_106
                show ep2_107
                toby "I'm gonna cum soon!"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She looks like she's going to let me cum in her mouth. Which will probably cost another grand.{/i}"
                scene expression ("images/episode2/108.webp") with dissolve
                with flash
                with flash
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode2/109.webp") with dissolve
                lauren "That will be another 2k."
                lauren "Should I swallow?"
                toby "I feel like I'm the worse negotiator ever, but yes!"
                scene expression ("images/episode2/110.webp") with dissolve
                lauren "You might be, because that just cost another 1k."
                toby "So the final price is 101k?"
                scene expression ("images/episode2/111.webp") with dissolve
                lauren "That's right my dear."

                $ unlockMemory(persistent.memory_04)
                $ renpy.end_replay()

            scene expression ("images/episode2/112.webp") with dissolve
            lisa "I could kiss you right now, but I think I'm gonna wait till you wash that dirty mouth of yours."
        "{i}focus on Lisa{/i} [JLI]"(csq="Lisa +1 & Gallery Image"):

            $ unlockImage(persistent.lisa_01)
            $ lisa_path = True
            $ lisa_rel += 1

            scene expression ("images/episode2/114.webp") with dissolve
            toby "I'm sorry miss, but I'd rather negotiate with your friend. I try not to mix sex with business."
            scene expression ("images/episode2/115.webp") with dissolve
            lisa "Oh my God! You are the best. She's not used to being turned down."
            scene expression ("images/episode2/116.webp") with dissolve
            lauren "I understand, you'd rather let Lisa suck your cock. She's very skilled at it, I'm sure!"
            scene expression ("images/episode2/117.webp") with dissolve
            lisa "LAUREN!!!"
            scene expression ("images/episode2/118.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This is getting really, really awkward.{/i}"
            toby "Let's just say that she can give me a kiss on the cheek and the price will be 100k."
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Stupid, stupid, stupid. You idiot! This is how you negotiate?{/i}"
            scene expression ("images/episode2/119.webp") with dissolve
            lisa "Umm... Okay!"
            scene expression ("images/episode2/120.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode2/121.webp") with dissolve
            toby "Pleasure doing business with you."
            lisa "Me too!"
            scene expression ("images/episode2/122.webp") with dissolve
            lauren "Oh, come on! The dude just gave you a $20,000 discount! The least you can do is kiss him. It's obvious that's what he wants."
            scene expression ("images/episode2/121.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}You really don't have to do that. It's fine.{/i}"
            scene expression ("images/episode2/123_1.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode2/123.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Well, this was unexpected!{/i}"
            scene expression ("images/episode2/124.webp") with dissolve
            lisa "So, do you think you can sell me the apartment for $101k instead of $100k? I feel a bit guilty for taking advantage of you!"
            toby "Of course. If that's what you want."
            scene expression ("images/episode2/125.webp") with dissolve
            lauren "You two are made for each other."

    scene expression ("images/episode2/113.webp") with dissolve
    $ progress = 23
    lisa "So we have a deal then. $101,000 for the apartment?"
    toby "That's right."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}If Darlene finds out what happened here she'll fire me!{/i}"
    scene expression ("images/episode2/126.webp") with dissolve
    toby "Okay then. I'll need to talk to my boss about the papers, but you can come by our office tomorrow, and we'll finalize everything for you then."
    lisa "Thank you, sir!"
    toby "Just call me [toby!c]."
    lisa "Thank you [toby!c]."
    toby "No problem. It was my pleasure."
    scene expression ("images/episode2/127.webp") with dissolve
    lauren "Bye sexy! See you tomorrow."
    lisa "See you tomorrow, [toby!c]!"
    toby "Bye!"

    scene expression ("images/episode2/128.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Now how am I going to explain this to Darlene?{/i}"
    if ep2_spankDarlene == True:
        scene expression ("images/episode2/129.webp") with dissolve
        darlene "If you ever touch my ass ever again, I'm gonna cut your cock off and feed it to the dogs."
        toby "Sorry ma'am. I was just trying to..."
        darlene "I don't care. I'm your boss, and you're not allowed to touch my ass!"
        toby "Sorry ma'am!"
    scene expression ("images/episode2/130.webp") with dissolve
    darlene "So let me guess. You failed to sell the apartment?"
    toby "No! I did. It's just that it's not the price I was hoping for!"
    darlene "How much lower did you go?"
    scene expression ("images/episode2/131.webp") with dissolve
    toby "$101,000."
    darlene "And you're disappointed with that?"
    toby "Shouldn't I be?"
    darlene "The price for this apartment was really $80,000. The fact that you managed to sell it for $100,000 is a huge profit."
    darlene "I bought this apartment for $60,000, and since then the market went up, but it hadn't reached $100,000 yet."
    darlene "So for me, that's a profit of $40,000."
    scene expression ("images/episode2/132.webp") with dissolve
    toby "You mean $41,000!"
    darlene "Nope. That's your cut!"
    toby "But I thought you said my cut is 20%% of the profit."
    scene expression ("images/episode2/133.webp") with dissolve
    darlene "What can I say. I'm really bad with math today!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Should I be upset that she screwed me? Or should I be happy that I just made a grand in 30 minutes?{/i}"
    scene expression ("images/episode2/134.webp") with dissolve
    darlene "What do you think you're doing?"
    toby "Sorry ma'am. I thought you were going to take me home."
    darlene "No, I'm not. You're going to drive yourself home."
    toby "But I don't have a car."
    scene expression ("images/episode2/135.webp") with dissolve
    darlene "But you have a bike."
    scene expression ("images/episode2/136.webp") with dissolve
    toby "Are you serious?!"
    darlene "I hope you know how to ride one of those. And if you really want a luxury car like mine, you'll have to get better."
    menu:
        "{i}[JGR]flirt{/i}"(csq="Darlene +1"):
            scene expression ("images/episode2/137.webp") with dissolve
            $ darlene_rel += 1
            toby "You mean both in selling and in bed?"
            darlene "Don't push your luck!"
        "{i}don't flirt{/i}":

            pass
    scene expression ("images/episode2/138.webp") with dissolve
    toby "Thank you for the bike!"
    darlene "Thank you for the sale."
    toby "My pleasure!"
    darlene "Oh, and by the way, come to the office tomorrow so we can get your employment papers in order and I can teach you more about the job."
    toby "Okay!"
    return


label episode2_club:

    $ progress = 21
    scene expression ("images/episode2/070.webp") with long_dissolve


    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/139.webp") with dissolve
    toby "Excuse me sir, did Mrs. Katrina send you?"
    neal "Yes. I'm Neal. Hop in."
    neal "And don't slam the door!"
    scene expression ("images/episode2/140.webp") with dissolve
    neal "Mrs. Katrina told me you're new to the city."
    toby "Yeah. I just moved here a few days ago."
    neal "And? How do you like it so far?"
    toby "Can't say I had the time to see much. It looks interesting. The only place I've been so far is the beach."
    neal "Tell me you went there on a weekend."
    toby "No, it was yesterday."
    scene expression ("images/episode2/141.webp") with dissolve
    neal "You should definitely go on a Saturday. The girls there are the best."
    neal "You are into girls, right?"
    toby "Uhum, yes!"
    neal "Good."
    neal "By the way, we need to make a quick stop before going to Mrs. Katrina."
    toby "Yeah, sure. No problem."
    scene expression ("images/episode2/142.webp") with dissolve
    neal "Give me the piece from the glove compartment."
    toby "Piece?"
    scene expression ("images/episode2/143.webp") with dissolve
    neal "You've never held a gun before?"
    toby "No, I have. It's just that..."
    neal "Try not to hurt yourself with it."
    scene expression ("images/episode2/144.webp") with dissolve
    neal "I'll be right back. Don't go anywhere."
    scene expression ("images/episode2/145.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the fuck is going on? What have I gotten myself into?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is this going to be my new normal from now on? \"Pass me the gun.\" \"Here, hold this kilo of coke.\"{/i}"

    show screen ui_message("Five minutes later") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode2/146.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}The hell!? Why does he have a wad of cash in his hand? Did he fucking rob the place?{/i}"
    scene expression ("images/episode2/147.webp") with dissolve
    neal "Count this for me!"
    toby "Uhum... Sure!"
    scene expression ("images/episode2/148.webp") with dissolve
    toby "It's $1,000. Where should I put it?"
    neal "Hide it good and give it to Katrina when you see her."
    toby "Are you sure this is the right thing to do?"
    neal "Of course. If someone catches us, you have the money. It's the right thing to do!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yeah, for you!{/i}"
    scene expression ("images/episode2/149.webp") with long_dissolve
    toby "Hi ma'am. May I enter?"


    scene expression ("images/episode2/150.webp") with dissolve
    katrina "[toby!c]. Come, here my boy! So glad you've decided to join us."
    scene expression ("images/episode2/151.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What The hell? She's going to kiss me, just like that?{/i}"
    scene expression ("images/episode2/152.webp") with dissolve
    katrina "How was your trip!"
    menu:
        "{i}[JGR]look at her ass{/i}"(csq="Katrina +1 & Gallery Image"):
            $ katrina_rel += 1
            $ unlockImage(persistent.katrina_03)
            scene expression ("images/episode2/153.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What an ass... This woman's gonna be the death of me.{/i}"
            katrina "So?"
            scene expression ("images/episode2/154.webp") with dissolve
            katrina "Eyes up!"
            toby "Sorry, I..."
            katrina "I said, how was the trip? Did Neal behave?"
        "{i}be a good boy{/i}":
            pass
    toby "Uhum. Yeah, everything was fine. He asked me to give you this."
    scene expression ("images/episode2/155.webp") with dissolve
    katrina "Give me what?"
    toby "Umm... He asked me to give you a grand, but I can't find it! It must have fallen in the car!"
    toby "I'll be right back!"
    scene expression ("images/episode2/156.webp") with dissolve
    katrina "Looking for something?"
    toby "How did y...?"
    katrina "You need to have more control when someone is kissing you!"
    scene expression ("images/episode2/157.webp") with dissolve
    katrina "Please take a seat and let me explain your job here."
    toby "Sorry ma'am. I don't wanna be rude, but I'm not sure this is the right job for me."
    katrina "I told you to call me Katrina and let me spell it out for you!"
    scene expression ("images/episode2/158.webp") with dissolve
    katrina "Good boy!"
    katrina "So! Which word would you prefer, test or prank?"
    toby "Meaning?"
    katrina "Okay, the gun Neal asked you to give him was a fake. I just wanted to make sure you aren't going to call the police whenever you see something shady."
    katrina "We have a club, and here shady things are going to happen, but we want to keep them in our house. We want to let our own security handle things because if the cops get involved, we lose money. And do we want to lose money?"
    scene expression ("images/episode2/159.webp") with dissolve
    toby "No, we don't!"
    scene expression ("images/episode2/160.webp") with dissolve
    katrina "Exactly! We don't. Then the money... I just wanted to make sure I can trust you with money. I wanted to see how you would react if you'd knew that you'd have to give me a grand and you couldn't find it. Are you man enough to admit your mistakes?"
    katrina "And I liked how you handled it. You knew the risks of losing my money since you saw a gun just a few minutes ago!"
    katrina "Then I wanted to see how good you are with the girls, and you clearly lack concentration. If a girl kisses you, you lose focus, which is not good!"
    katrina "But we'll work on that."
    scene expression ("images/episode2/161.webp") with dissolve
    toby "So everything was just a test?"
    katrina "Exactly! And you passed!"
    katrina "Now, let's talk about your job."
    katrina "We need good looking guys to act like fake clients. Your job is to walk around the club and invite girls inside. Make them feel special and wanted."
    toby "So I don't get to join in the fun in the club?"
    katrina "Not really. Because sometimes there are girls in small groups that have more friends still at home, so your job is to flirt with those girls and get them to invite their friends next time."
    toby "I understand!"
    scene expression ("images/episode2/162.webp") with dissolve
    toby "And you want to have ladies in the club because if there are beautiful girls in the club, then a lot of men will come, and they are willing to buy lots of expensive drinks just to impress them."
    katrina "Exactly! I knew you were a smart guy."
    katrina "Also, you'll have to make sure that girls don't leave because of idiot guys. You'll be their knight in shining armor."
    toby "And what if to make a girl feel special I'll have to buy her drinks?"
    katrina "I'll introduce you to the staff, and they will give you whatever you need. Clothes, alcohol, drugs, whatever the girls need."
    scene expression ("images/episode2/163.webp") with dissolve
    toby "I really don't wanna get involved with drugs. I'm clean and don't want to get back into drugs again."
    katrina "You don't have to, but some people like to consume when they want to party."
    toby "But isn't it illegal to sell drugs in a club? You could lose your license!"
    scene expression ("images/episode2/164.webp") with dissolve
    katrina "Of course it is, but you're no drug dealer. You're not selling them. You'll give them away for free, but only to the ladies."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This is pretty fucked up!{/i}"
    scene expression ("images/episode2/165.webp") with dissolve
    katrina "Let me show you around and see if there are any girls in the club."
    toby "It's a Tuesday night. How many girls could be in the club on a Tuesday?"
    katrina "Usually there are a few people that come to drink, smoke, and chat on a weekday, but on the weekends, that's another story!"

    show screen ui_message("A short time later") with dissolve
    $ ui.saybehavior()
    $ ui.interact()


    scene expression ("images/episode2/166.webp") with long_dissolve
    hide screen ui_message
    $ progress = 22
    katrina "So? What do you think? You like the place?"
    toby "Uhum, yeah! It's nice, but there is one thing I need to ask you."
    katrina "Let me guess, the money?"
    toby "Yes."
    katrina "I'll be watching you and see how many girls you have talked to, fucked, or how many have sucked your cock under the table."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She sounds like a pervert!{/i}"
    scene expression ("images/episode2/167.webp") with long_dissolve
    katrina "I'm joking. You'll get a percentage of the sales. Don't worry, it will be fine, now let's see how good you are with the ladies."
    katrina "Do you have a girlfriend?"
    toby "Yes, but she's back home."
    katrina "You live with your girlfriend, and she's fine with you working in a club as a wingman? Nice! I like her."
    toby "No... I mean, she lives back in Rictown, but yeah, she doesn't know I'll be working here. I haven't had the chance to tell her."
    scene expression ("images/episode2/168.webp") with dissolve
    katrina "Interesting. Don't tell her. She doesn't need to know!"
    katrina "Show me a picture."
    toby "Is that really necessary?"
    katrina "Yes! I want to see your type."
    scene expression ("images/episode2/169.webp") with dissolve
    katrina "Too bad you're into blondes. I really thought we had something."
    katrina "Well, it is what it is!"
    scene expression ("images/episode2/170.webp") with dissolve
    katrina "Behind you, two girls just walked in. One of them is a blonde, just like you like them. Go talk to them and get her number."
    scene expression ("images/episode2/171.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    katrina "Actually, Nah. You don't have a chance with her. Get the friend's phone number."
    toby "I'll bet you that grand you stole from my pocket that I can get her number."
    katrina "Go get 'em, tiger. You've got yourself a deal!"
    scene expression ("images/episode2/172.webp") with dissolve
    toby "Hey, I'll give you 50 bucks if you go talk to the ladies over there."
    guy "Why would I do that?"
    scene expression ("images/episode2/173.webp") with dissolve
    toby "Because otherwise, the owner will ask to have a word with you!"
    scene expression ("images/episode2/174.webp") with dissolve
    guy "Do you know Mrs. Katrina?"
    toby "What do you think? Of course!"
    guy "Ok, I'll go. What should I say to them?"
    toby "Give them your cheesiest pick up line!"
    scene expression ("images/episode2/175.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Poor guy. He doesn't know what's about to happen to him.{/i}"
    scene expression ("images/episode2/176.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Time for [toby!c] to shine!{/i}"
    scene expression ("images/episode2/177.webp") with dissolve
    toby "Sorry I'm late, ladies. I just had to finish some business!"
    scene expression ("images/episode2/178.webp") with dissolve
    toby "Here's fifty bucks, go buy yourself something nice, maybe a book of better pickup lines!"
    guy "Fuck you!"
    scene expression ("images/episode2/179.webp") with long_dissolve
    girl "Wow, that was so cool!"
    girl "Now, who's going to get rid of you?"
    scene expression ("images/episode2/180.webp") with dissolve
    toby "Don't you worry, beautiful, I'll leave as soon as that guy is 50 feet away. I have no intention of wasting your time!"
    scene expression ("images/episode2/181.webp") with dissolve
    toby "No offense. But I'm sure you're fun!"
    scene expression ("images/episode2/182.webp") with dissolve
    lauren "I'm Lauren, and I am entertaining if you really want to know."
    scene expression ("images/episode2/183_1.webp") with dissolve
    toby "And I'm [toby!c]. At your service."
    scene expression ("images/episode2/183_2.webp") with dissolve
    lisa "And I'm Lisa. Now can you leave us alone, please?"
    scene expression ("images/episode2/184.webp") with dissolve
    toby "If the lady wants... See you around, beautiful!"
    lauren "But what if the other lady wants you to stay?"
    scene expression ("images/episode2/185.webp") with dissolve
    toby "Then I'll stay a bit longer."
    toby "So, tell me, Lauren! What makes you so fun?"
    lauren "Let's just say I'm fantastic in bed."
    scene expression ("images/episode2/186.webp") with dissolve
    toby "And? You're not?"
    lisa "I might be, but unlike my friend over there, I don't blow every guy I meet."
    scene expression ("images/episode2/187.webp") with dissolve
    toby "Ewww... You must be nasty!"
    lauren "You have no idea!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I can't flirt with both of them. I need to focus only on one.{/i}"
    scene expression ("images/episode2/188.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Judging by her attitude, she must be rich and she's had loads of guys trying to hit on her.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She must be tired of the shallow, horny approach. If I'm going to make a move on her, I should be a gentleman.{/i}"
    scene expression ("images/episode2/189.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She likes to be the center of attention. She'd do anything for a little bit of fun. I think she's very insecure about everything.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She cannot compete with her friend on so many levels, so she's trying make up for it by being more outgoing.{/i}"
    menu:
        "{i}focus on Lisa{/i} [JLI]"(csq="Lisa +1 & Gallery Image"):
            $ lisa_rel += 1
            $ lisa_path = True
            $ unlockImage(persistent.lisa_02)

            scene expression ("images/episode2/190.webp") with dissolve
            toby "Sorry beautiful, but I'm not the kind of guy who takes a girl in the bathroom and fucks her after knowing her for only 10 minutes. I'm the kind of guy who likes to go on dates and fall in love."
            scene expression ("images/episode2/191.webp") with dissolve
            toby "But for that, I'm going to need your number so I can ask you out!"
            scene expression ("images/episode2/192.webp") with dissolve

            lauren "You're such a pig! This is the most beautiful and hurtful rejection I have ever received."
            scene expression ("images/episode2/193.webp") with dissolve
            lisa "If you let her slap you once more, I'm even willing to give you a kiss on the cheek."
            toby "I can take anything you can throw at me."
            scene expression ("images/episode2/194.webp") with dissolve
            lauren "I'm gonna slap you if you're not going to kiss this gentleman on his lips!"
            scene expression ("images/episode2/195_1.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}A kiss on the cheek will be just fine.{/i}"
            scene expression ("images/episode2/195_2.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode2/195_3.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is she going for the lips?{/i}"
            scene expression ("images/episode2/196.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wasn't expecting that!{/i}"
            scene expression ("images/episode2/197.webp") with dissolve
            lisa "Call me!"
            scene expression ("images/episode2/198.webp") with dissolve
            toby "Oh, I will!"
            toby "I let you two enjoy the rest of your evening. It was nice meeting you!"
            lisa "Bye [toby!c]."
            lauren "Bye, handsome pig!"
        "{i}focus on Lauren{/i} [JLA]"(csq="Lauren +1 & Gallery Image"):

            $ unlockImage(persistent.lauren_02)
            $ lauren_rel += 1
            $ lauren_path = True
            $ ep2_laurenBlowjob = True
            scene expression ("images/episode2/199.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I'll be waiting for you in the bathroom.{/i}"
            scene expression ("images/episode2/200.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I hope I didn't make a fool out of myself. What if she doesn't come!{/i}"

            label memory_05:
                scene expression ("images/episode2/201.webp") with dissolve

                lauren "Miss me?"
                scene expression ("images/episode2/201_1.webp") with dissolve
                toby "You have no idea!"
                scene expression ("images/episode2/201_2.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode2/202.webp") with dissolve:
                    yalign 1.0
                    linear 10.0 yalign 0.0

                $ ui.pausebehavior(9.3)
                $ ui.saybehavior()
                $ ui.interact()
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This girl is crazy!{/i}"
                scene expression ("images/episode2/203.webp") with dissolve
                lauren "Fuck... It's so big!"
                scene expression ("images/episode2/204.webp")
                show ep2_204
                toby "You're crazy! You know that, right?"
                lauren "You just met me. You'll see just how crazy I can be."
                scene expression ("images/episode2/205.webp")
                hide ep2_204
                show ep2_205
                toby "If I'm going to see more like this, I cannot wait!"
                scene expression ("images/episode2/206.webp")
                hide ep2_205
                show ep2_206
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... This is so good!{/i}"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I never had a blowjob like this.{/i}"
                scene expression ("images/episode2/207.webp")
                hide ep2_206
                show ep2_207
                toby "I'm going to cum!"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Of course she's not stopping. Why would she!{/i}"
                scene expression ("images/episode2/208.webp") with dissolve
                hide ep2_207
                with flash
                with flash
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Damn... This was so, so good!{/i}"
                scene expression ("images/episode2/209.webp") with dissolve
                lauren "If you want me to swallow, you'll have to promise to call me."
                toby "As long as you give me your number!"
                scene expression ("images/episode2/210.webp") with dissolve
                lauren "Deal!"
                scene expression ("images/episode2/211.webp") with dissolve
                lauren "Here, I'll be waiting for your call!"
                toby "Gladly!"
                scene expression ("images/episode2/212.webp") with dissolve
                lauren "See you later, handsome."
                toby "See you later, sexy."

                $ unlockMemory(persistent.memory_05)
                $ renpy.end_replay()

    $ progress = 23
    scene expression ("images/episode2/213.webp") with dissolve

    katrina "So? How did it go?"
    if lisa_rel == 1:
        scene expression ("images/episode2/214.webp") with dissolve
        toby "What do you think? Of course, I managed to get her number!"
        katrina "You got her number? She fucking kissed you, too. That's pretty good, to be honest. No one else has managed to do that on their first day."
    else:
        toby "Not quite. I managed to get her friend's number."
        katrina "What did you do in the bathroom?"
        toby "She blew me."
        katrina "Not bad at all. No one else has managed to do that on their first day."

    scene expression ("images/episode2/213.webp") with dissolve
    toby "Really? Are there any other so-called wingmen working for you?"
    katrina "Not anymore. There was one, but he was totally useless!"
    toby "So, did I win the bet?"

    if lisa_rel == 1:
        scene expression ("images/episode2/215.webp") with dissolve
        katrina "Here... You earned it!"
    else:

        scene expression ("images/episode2/215.webp") with dissolve
        katrina "You lost the bet, but you still deserve the money."

    toby "Thank you, ma'am."
    toby "I mean, Katrina."
    katrina "Just call me Kat. You're my favorite guy now!"
    toby "Cool!"
    scene expression ("images/episode2/216.webp") with dissolve
    katrina "You're free to go home now."
    katrina "There is a motorcycle waiting for you. The key is in the ignition. It belongs to you now."
    toby "Are you shitting me?"
    katrina "Calm down. It's not like I'm giving you some supercar."
    toby "Yeah, but it's still something!"
    katrina "You could say that!"
    toby "Pleasure doing business with you!"
    katrina "Wait for my call. I'll be in touch when I need you here!"
    menu:
        "{i}[JGR]flirt{/i}"(csq="Katrina +1"):
            $ katrina_rel += 1
            toby "Can't wait for your call. I love hearing your voice."
            katrina "Don't push your luck, boy!"
        "{i}don't flirt{/i}":

            toby "Sure!"
    scene expression ("images/episode2/217.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/218.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This must be it!{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This must be my new bike!{/i}"
    return


label episode2_drinkMom:
    $ progress = 24

    scene expression ("images/episode2/219.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Finally home. I really missed riding a bike.{/i}"
    scene expression ("images/episode2/220.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm beat. Can't wait to get some sleep.{/i}"
    scene expression ("images/episode2/221.webp") with long_dissolve
    toby "Hey [mom], you're not sleeping yet?"

    scene expression ("images/episode2/222.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I gotta give it to her. [mom!c] looks amazing for her age.{/i}"

    charlotte "And miss when my [son] comes home from his first day of work?"
    charlotte "I couldn't do that, and besides, I just popped open a bottle of wine, and don't wanna drink it alone. It's getting depressing."
    scene expression ("images/episode2/223.webp") with dissolve
    toby "Aren't you drinking too much lately?"
    charlotte "Not at all. Let's sit down and tell me how your first day of work went."
    scene expression ("images/episode2/224.webp") with dissolve
    toby "Sure thing. Let me just turn on the lights."
    charlotte "You like the light on? You don't want to miss anything."
    scene expression ("images/episode2/225.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Was that a sexual joke?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Nah... It can't be! She's my [mom].{/i}"
    scene expression ("images/episode2/226.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But seeing that bottle half empty I think it may have been.{/i}"
    scene expression ("images/episode2/227.webp") with dissolve
    toby "You just opened the bottle? How much have you had?"
    charlotte "Only one full glass."
    scene expression ("images/episode2/228.webp") with dissolve
    charlotte "And maybe a few more half empty."
    scene expression ("images/episode2/229.webp") with dissolve
    charlotte "I promise I haven't had anything to drink for the past two weeks, but today is special."
    scene expression ("images/episode2/230.webp") with dissolve
    toby "Special how?"
    scene expression ("images/episode2/231.webp") with dissolve
    charlotte "My boy is a man now. He has a job and is becoming a responsible adult."
    charlotte "Actually, I think you've been a man for a while already. Now you're just more responsible."
    scene expression ("images/episode2/232.webp") with dissolve
    toby "[mom!c]! Can we not talk about my sex life?"
    scene expression ("images/episode2/233.webp") with dissolve
    charlotte "{size=12}{color=#FDCA6E}* mumbling *{/color}{/size}\n{i}At least you have one.{/i}"
    scene expression ("images/episode2/230.webp") with dissolve
    toby "What was that?"
    scene expression ("images/episode2/234.webp") with dissolve
    charlotte "At least you have one. I can't remember the last time me and your [father] had a romantic moment. Even just a passionate kiss."
    scene expression ("images/episode2/235.webp") with dissolve
    toby "I'm sure he still loves you. It's just with all that happened recently, it's hard to focus on different things. He's just trying his best."
    scene expression ("images/episode2/233.webp") with dissolve
    charlotte "{size=12}{color=#FDCA6E}* mumbling *{/color}{/size}\n{i}Yeah. He can't even remember our anniversary.{/i}"
    scene expression ("images/episode2/236.webp") with dissolve
    toby "Today was your anniversary?"
    scene expression ("images/episode2/234.webp") with dissolve
    charlotte "Yes. Today we would have celebrated 21 years of marriage."
    scene expression ("images/episode2/235.webp") with dissolve
    toby "I'm sure he didn't forget. He's just busy with work, but when he gets back home, I'm sure he'll bring you some flowers or something."
    scene expression ("images/episode2/237.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I need to call him right away to make sure he didn't forget.{/i}"
    scene expression ("images/episode2/238.webp") with dissolve
    charlotte "Not going to happen."
    scene expression ("images/episode2/235.webp") with dissolve
    toby "Give him a chance at least."
    scene expression ("images/episode2/238.webp") with dissolve
    charlotte "He's already in bed, sleeping."
    scene expression ("images/episode2/234.webp") with dissolve
    charlotte "I prepared dinner and this wine, besides that, I dressed sexy for him. Do you want to know what he told me?"
    scene expression ("images/episode2/239.webp") with dissolve
    charlotte "He said that we should keep this wine for special occasions. It's too expensive. So I'm going to drink it alone. I don't need a man to help me."
    charlotte "So if you're going to judge me for drinking, then why don't you go sleep next to your [father]."
    scene expression ("images/episode2/237.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's in a really bad place, I think I'd better try to cheer her up.{/i}"
    scene expression ("images/episode2/240.webp") with dissolve
    toby "Then sweet lady, let me tell you something. Do you know why back in high school I was always getting the lead roles in every play?"
    charlotte "Because you were rich and popular?"
    scene expression ("images/episode2/241.webp") with dissolve
    $ progress = 25
    toby "Maybe, but really because I'm a good actor, so let me to cheer you up. Tonight I'll be your husband. Why don't we celebrate 21 years of a happy marriage."
    charlotte "Where's my gift?"
    scene expression ("images/episode2/242.webp") with dissolve
    toby "Haven't I've done enough for you? I mean, I gave you two beautiful [children] and besides, one of them just made his first grand in one day."
    charlotte "That's wonderful, honey. Congratulations!"
    toby "Why are you congratulating me? I just told you that my [son] was the one who earned $1,000 in one day."
    charlotte "You're right, but I couldn't have had him without you. Actually, I think he got his brains from his [mother]."
    charlotte "So I guess there is no gift after all."
    scene expression ("images/episode2/243.webp") with dissolve
    toby "That was not the real gift. I have prepared more."
    charlotte "Then where is the rest?"
    scene expression ("images/episode2/244.webp") with dissolve
    toby "You need to be rewarded for having such a wonderful [son]."
    scene expression ("images/episode2/245.webp") with dissolve
    charlotte "After 21 years of marriage, you're still a pervert?"
    scene expression ("images/episode2/246.webp") with dissolve
    toby "I was not talking about anything dirty. The only pervert in this house is you."
    charlotte "Are you going to give me a phone that I actually paid for?"
    toby "No, I'm going to put on some music, and then we'll dance!"
    scene expression ("images/episode2/247.webp") with dissolve

    toby "Because I know how much you love to dance, so why don't you dance with me?"
    charlotte "How can I say no to such a handsome young man."
    toby "Don't be fooled by my looks. I'm actually in my fifties."
    scene expression ("images/episode2/248.webp") with dissolve
    charlotte "And you're still attracted to such an old-looking lady like me?"
    toby "I don't believe you're old until I see some ID. You look better than most girls my age. I mean my [son]'s age."
    scene expression ("images/episode2/249.webp") with dissolve
    charlotte "I have to admit. I look excellent given the fact that I have two [children]."
    charlotte "So, Mr. Charming. Why don't you show me your moves."
    scene expression ("images/episode2/250.webp") with long_dissolve
    toby "So what do you say my dear, is this gift good enough for you?"
    charlotte "Honest answer or do you want me to lie?"
    menu:
        "[JGR]Honest":
            pass
        "Lie":
            pass
    scene expression ("images/episode2/251.webp") with dissolve
    charlotte "I like the intention, but you don't know how to dance."
    toby "Was that the honest answer or the lie, cuz I can't tell."
    charlotte "I'm serious, you need to improve your moves."
    scene expression ("images/episode2/252.webp") with dissolve
    toby "What can I say? I haven't danced with my wife in 5 years."
    charlotte "You misunderstood. We haven't had sex in 5 years. The dancing is more recent."
    scene expression ("images/episode2/253.webp") with dissolve
    toby "My bad, I'll try to remember that next time."
    scene expression ("images/episode2/254.webp") with dissolve
    charlotte "Instead of remembering it, why don't you fix it?"
    $ unlockImage(persistent.charlotte_05)
    toby "Uhm..."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think she's had one too many drinks tonight.{/i}"
    scene expression ("images/episode2/255.webp") with dissolve
    charlotte "Sorry, sweetie. That sounded really inappropriate. It's just that I haven't had a good time like this in years, and for a split second, I was caught up in the moment."
    scene expression ("images/episode2/256.webp") with dissolve
    toby "Don't worry [mom]. Forget about it. I'm sorry you're having a rough time. Wanna talk more about it?"
    charlotte "That would be great."
    $ progress = 26
    scene expression ("images/episode2/257.webp") with dissolve
    charlotte "Our marriage is failing. I have done everything to save it. I supported him in every decision. I agreed to move. I agreed to help him with work."
    charlotte "I know we're going through rough times, so I tried my best to put on a smile for him. I did everything by the book."
    charlotte "And my reward is \"{i}That wine is for special ocassions{/i}\"."
    scene expression ("images/episode2/258.webp") with dissolve
    charlotte "Do I really deserve this? I understand that he has to work, it's normal, but I don't give a fuck about the money."
    charlotte "I don't care if we live in a huge mansion or a small apartment as long as we're happy, but we're not."
    charlotte "He's not happy. The only thing he thinks about is making money."
    scene expression ("images/episode2/259.webp") with dissolve
    charlotte "Please, just please don't ever be like him. You should make money, not the other way around."
    toby "I'm sorry you're going through this. I don't know if it helps, but I love you, and I'm sure Tris does too."
    scene expression ("images/episode2/260.webp") with dissolve
    charlotte "You two are the best thing that's ever happened to me. I'm so grateful for you guys."
    scene expression ("images/episode2/261.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I don't think there is a more heartbreaking moment than seeing your [mother] crying.{/i}"
    charlotte "I love you too, honey!"

    show screen ui_message("20 minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode2/262.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It looks like she fell asleep. I should take her to her room.{/i}"
    scene expression ("images/episode2/263.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe bringing her to the same bed as [dad] is not the best idea at the moment, but I'm sure she would hate Tris finding out what's going on here.{/i}"
    scene expression ("images/episode2/264.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Sorry [mom]. I'm going to fix up the attic and let you sleep there with me whenever you feel like it.{/i}"
    scene expression ("images/episode2/265.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Good night [mom].{/i}"

    return


label episode2_trisNight:
    $ progress = 27

    scene expression ("images/episode2/266.webp") with dissolve
    toby "Hi Tris. Why aren't you sleeping?"
    scene expression ("images/episode2/267.webp") with dissolve
    patricia "Because I hate this school!"
    patricia "I feel so stupid. I can't even do stupid math homework!"
    scene expression ("images/episode2/268.webp") with dissolve
    toby "Why don't you get a tutor then?"
    scene expression ("images/episode2/269.webp") with dissolve
    patricia "You really have to ask me that?"
    patricia "Because we're poor and [dad] said we can't afford a tutor, so I'll just have to do my best to learn it on my own."
    toby "We're poor?"
    patricia "Yes, we are. Have you forgotten why we have to share a room?"
    scene expression ("images/episode2/270.webp") with dissolve
    toby "Maybe you are. I am not!"
    scene expression ("images/episode2/271.webp") with dissolve
    patricia "Did you rob a bank or something?"
    toby "I'm just a hard working guy."
    scene expression ("images/episode2/272.webp") with dissolve
    patricia "Wow... You made $100. You're rich. I think we have different opinions about what rich means."
    scene expression ("images/episode2/273.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Do you really think I would give you all the money I made today? That's just the tip of the iceberg.{/i}"
    patricia "Do you have more?"
    toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Let's just say that I can pay for a tutor if you really need, and it won't even feel like I'm giving you money.{/i}"
    scene expression ("images/episode2/274.webp") with dissolve
    patricia "What's the catch?"
    toby "No catch. I'm just happy to help!"
    scene expression ("images/episode2/275.webp") with dissolve
    patricia "I have a better idea."
    scene expression ("images/episode2/276.webp") with dissolve
    toby "Do tell!"
    scene expression ("images/episode2/275.webp") with dissolve
    patricia "I'll keep the money, and instead of paying someone to tutor me, you can help me with my homework!"
    scene expression ("images/episode2/277.webp") with dissolve
    toby "This must be the worst deal of all time. Besides the fact that I lose money, I also lose time. So what's in for me?"
    scene expression ("images/episode2/278.webp") with dissolve
    patricia "Let me put it this way. You give me money that I spend on cute clothes, and when we're doing homework, I get to be dressed nicely. Maybe even sexy."
    scene expression ("images/episode2/279.webp") with dissolve
    toby "And why would this make me feel any better?"
    scene expression ("images/episode2/280.webp") with dissolve
    patricia "You'll be so impressed by my clothes, and then you'll give me even more money!"
    scene expression ("images/episode2/279.webp") with dissolve
    toby "It might be me, but I really feel that I'm losing here."
    scene expression ("images/episode2/280.webp") with dissolve
    patricia "No way... It's a win-win situation here."
    scene expression ("images/episode2/279.webp") with dissolve
    toby "Is it though?"
    scene expression ("images/episode2/281.webp") with dissolve
    patricia "Pretty please?"
    scene expression ("images/episode2/282.webp") with dissolve
    toby "Fine... What's the problem."
    patricia "Let me show you!"
    $ unlockImage(persistent.patricia_05)
    show screen ui_message("A short time later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    $ progress = 28
    scene expression ("images/episode2/283.webp") with dissolve
    hide screen ui_message
    toby "This should be everything. Anything else?"
    scene expression ("images/episode2/284.webp") with dissolve
    patricia "Yeah. Don't ever negotiate. You're really bad at it."
    toby "I meant, is there anything else in the homework you don't understand?"
    scene expression ("images/episode2/285.webp") with dissolve
    patricia "Thank you. I knew I could count on you."
    scene expression ("images/episode2/286.webp") with dissolve
    patricia "And take your money. I can't take it. You earned it."
    toby "I am serious. You can have it, go buy yourself something nice. I earned a lot today."
    scene expression ("images/episode2/287.webp") with dissolve
    patricia "Really? Was the first day of work that profitable?"
    toby "Yeah, no need to worry. It was awesome. Besides the money I made, I also got a bike."
    scene expression ("images/episode2/288.webp") with dissolve
    patricia "As I was saying, you really need to learn how to negotiate better. I think a cheap car would have been better than a bicycle, but yeah, you do you!"
    scene expression ("images/episode2/289.webp") with dissolve
    toby "Oh, silly girl. I said bike. Not bicycle."
    scene expression ("images/episode2/290.webp") with dissolve
    toby "Come, take a look at my so-called \"bicycle\"!"
    scene expression ("images/episode2/291.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/292.webp") with dissolve
    patricia "So? Are you going to leave and let me get dressed, or do you want to take me for a ride on your bike dressed like this?"
    scene expression ("images/episode2/293.webp") with dissolve
    toby "I must be getting old. I don't remember when I told you I'm taking you for a ride."
    patricia "I'm so sorry for you. So young and yet losing his memory already."
    toby "Is there a scenario where I get to win here?"
    scene expression ("images/episode2/294.webp") with dissolve
    patricia "Not a single one!"
    toby "I'll be waiting for you outside, but try to be quiet. I don't want [dad] to hear that I took you on my bike. He'll freak out!"
    scene expression ("images/episode2/295.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What is taking her so long?{/i}"
    $ progress = 29

    scene expression ("images/episode2/296.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    toby "What's with the outfit?"
    scene expression ("images/episode2/297.webp") with dissolve
    patricia "You don't like my biker outfit?"
    toby "I feel like a noob dressed like this when I see you like that."
    scene expression ("images/episode2/298.webp") with dissolve
    patricia "You do look like a noob if I'm being honest!"
    toby "That's it, I'm going solo."
    scene expression ("images/episode2/299.webp") with dissolve
    patricia "Too late now!"
    patricia "By the way, where is the helmet?"
    toby "I need to buy a couple. I got the bike without a helmet."
    patricia "Try not to have an accident then."
    scene expression ("images/episode2/300.webp") with dissolve
    toby "So where to?"
    patricia "Surprise me."

    scene expression ("images/episode2/301.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.00

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode2/302.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    show ep2_303 with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/303.webp") with dissolve
    hide ep2_303

    scene expression ("images/episode2/304.webp") with dissolve
    patricia "Let's go to the park."
    toby "I don't think it's legal to enter the park on the bike."
    patricia "Don't be such a pussy! We'll stop at a bench."
    scene expression ("images/episode2/305.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/306.webp") with dissolve
    toby "Do you like this one?"
    scene expression ("images/episode2/307.webp") with dissolve
    patricia "It's perfect."

    scene expression ("images/episode2/308.webp") with dissolve
    toby "So? What do you think about my bicycle."
    patricia "Meh..."
    scene expression ("images/episode2/309.webp") with dissolve
    toby "Really!? I hope you know how to get back because I'm leaving you here."
    patricia "Fine... It's awesome. I really needed to relax like this."
    scene expression ("images/episode2/310.webp") with dissolve
    toby "I feel you. I also needed to clear my head. I think it's nice for a change to not think about anything and just enjoy the ride."
    scene expression ("images/episode2/311.webp") with dissolve
    patricia "Did something happen?"
    scene expression ("images/episode2/312.webp") with dissolve
    toby "No, it's nothing. It's just something that happened at work."
    scene expression ("images/episode2/313.webp") with dissolve
    patricia "Speaking of... How was your first day of work?"
    $ progress = 30
    if toby_job == 0:
        scene expression ("images/episode2/310.webp") with dissolve
        toby "It was actually really nice. My boss is really impressed with me. We went to an apartment and she showed me around. When the clients got there, she just left me with them."
        scene expression ("images/episode2/314.webp") with dissolve
        patricia "Just like that? No prep talk, no nothing? Just \"Sell this apartment for me?\""
        scene expression ("images/episode2/315.webp") with dissolve
        toby "Yes. She told me that I should not go lower than 100k and told me to negotiate with one of the girls because she's the one that has the money!"
        scene expression ("images/episode2/314.webp") with dissolve
        patricia "You even negotiated the price for the apartment on your first day?"
        scene expression ("images/episode2/315.webp") with dissolve
        toby "Yeah. I was surprised too. I couldn't believe that she left me in charge. I think it was more like a test to see if I can sell the apartment."
        scene expression ("images/episode2/313.webp") with dissolve
        patricia "And did you?"
        scene expression ("images/episode2/316.webp") with dissolve
        toby "What do you think? Of course. I even got a higher price than she asked!"
        scene expression ("images/episode2/314.webp") with dissolve
        patricia "How much?"
        scene expression ("images/episode2/317.webp") with dissolve
        toby "101k."
        scene expression ("images/episode2/318.webp") with dissolve
        patricia "{size=12}{color=#FDCA6E}* laughing *{/color}{/size}\n{i}She's so lucky to have you. She told you not to go lower than 100k, and you sold it for 101k.{/i}"
        patricia "As I was telling you. Never negotiate."
        scene expression ("images/episode2/319.webp") with dissolve
        patricia "And how were the girls?"

    elif toby_job == 1:
        scene expression ("images/episode2/310.webp") with dissolve
        toby "It's a bit strange, my boss tested me to see if she can trust me."
        scene expression ("images/episode2/320.webp") with dissolve
        patricia "Tested to see if she can trust you? Why would she do that and how?"
        scene expression ("images/episode2/315.webp") with dissolve
        toby "Well, at first, her driver took me on this shady street and asked me to give him a gun from the glove compartment."
        scene expression ("images/episode2/317.webp") with dissolve
        toby "I almost shit myself when I saw the gun."
        scene expression ("images/episode2/314.webp") with dissolve
        patricia "Was it a real gun?"
        scene expression ("images/episode2/310.webp") with dissolve
        toby "It looked real, but from what miss Katrina told me, it was just a prank to see how would I react."
        toby "So I gave him the gun, and after a few minutes, he came back with a stack of money and asked me to count it and then give it to Katrina."
        scene expression ("images/episode2/313.webp") with dissolve
        patricia "And then?"
        scene expression ("images/episode2/315.webp") with dissolve
        toby "Then I went to miss Katrina's office, and she came to me, gave me a k... hug, and stole the money from my pocket."
        toby "I was so scared when I couldn't find the money, and then she started to make fun of me."
        scene expression ("images/episode2/318.webp") with dissolve
        patricia "I can't imagine how you felt. But still, why the tests?"
        scene expression ("images/episode2/310.webp") with dissolve
        toby "As far as I understood, there are a lot of shady things that happen in the club, and they don't want the police involved. They prefer to take care of things themselves."
        scene expression ("images/episode2/320.webp") with dissolve
        patricia "But what exactly is your job there?"
        scene expression ("images/episode2/317.webp") with dissolve
        toby "I need to pick up girls in the street and invite them inside because where there are beautiful ladies, there will be horny men willing to leave piles of cash to impress them."
        scene expression ("images/episode2/318.webp") with dissolve
        patricia "Men are so simple."
        scene expression ("images/episode2/310.webp") with dissolve
        toby "Very funny!"
        scene expression ("images/episode2/318.webp") with dissolve
        patricia "And why did she think you would be good with the girls?"
        scene expression ("images/episode2/316.webp") with dissolve
        toby "Actually, I'm really good at it. I actually managed to pick up two."
        scene expression ("images/episode2/319.webp") with dissolve
        patricia "Really? And how were the girls?"

    scene expression ("images/episode2/321.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}How were the girls? Hot. Really hot. Hot enough that I cheated on Emma. I'm so stupid.{/i}"
    toby "You know... Normal girls."
    patricia "What's with that look on your face?"
    scene expression ("images/episode2/322.webp") with dissolve
    toby "What look? It's nothing. You must be imagining things."
    scene expression ("images/episode2/323.webp") with dissolve
    patricia "Did something happen between you and one of the girls?"
    toby "I cheated on Emma."
    scene expression ("images/episode2/324.webp") with dissolve
    patricia "What do you mean you cheated on Emma?"
    toby "I really don't want to talk about it."
    scene expression ("images/episode2/325.webp") with dissolve
    patricia "You moron! How can you cheat on her?"
    toby "I thought you didn't like her."
    patricia "I don't. But no girl deserves to be cheated on!"
    scene expression ("images/episode2/326.webp") with dissolve
    toby "Oh please, don't tell me you never cheated!"
    scene expression ("images/episode2/327.webp") with dissolve
    patricia "Cheat on who? I've never had a boyfriend."
    toby "What do you mean you never had a boyfriend?"
    scene expression ("images/episode2/328.webp") with dissolve
    toby "You are so pretty. How come you haven't had a boyfriend?"
    patricia "I don't want to talk about it."
    toby "No, no... We are!"
    scene expression ("images/episode2/329.webp") with dissolve
    patricia "You didn't tell me what you did to cheat on Emma."
    if ep2_laurenBlowjob == True:
        toby "One of them gave me a blowjob!"
    else:
        toby "I kissed one of them!"
    scene expression ("images/episode2/330.webp") with dissolve
    patricia "So when are you going to introduce her to us. I hope this one isn't a gold digger like Emma!"
    toby "She is no gold digger, and right now we're talking about why you never had a boyfriend. I know plenty of boys in our High School that would have loved to date you."
    scene expression ("images/episode2/331.webp") with dissolve
    patricia "I kept comparing them to you. I saw how you treat women. You're such a gentleman. "
    scene expression ("images/episode2/332.webp") with dissolve
    patricia "You're smart, mature, funny, cool, handsome, caring, and none of those clowns could ever compare to you!"
    scene expression ("images/episode2/333.webp") with dissolve
    patricia "Until now. You lowered the bar really low with this."
    patricia "I think it's going to be easier to find a boyfriend now. I'm sure can find a man who isn't a cheater!"
    scene expression ("images/episode2/334.webp") with dissolve
    toby "Then I think you can find your way home on foot and look for a boyfriend."
    scene expression ("images/episode2/335.webp") with dissolve
    patricia "What do you think you're doing?"
    scene expression ("images/episode2/336.webp") with dissolve
    toby "See you home!"
    scene expression ("images/episode2/337.webp") with dissolve
    patricia "Don't you even dare!"
    scene expression ("images/episode2/338.webp") with dissolve
    toby "Next time, I won't be so nice!"
    scene expression ("images/episode2/339.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/340.webp") with long_dissolve
    patricia "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Idiot!{/i}"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
