image ep1_004 = Movie(play="video/episode1/004.webm", loop=True)
image ep1_005 = Movie(play="video/episode1/005.webm", loop=True)
image ep1_011 = Movie(play="video/episode1/011.webm", loop=True)
image ep1_012 = Movie(play="video/episode1/012.webm", loop=True)
image ep1_013 = Movie(play="video/episode1/013.webm", loop=True)
image ep1_014 = Movie(play="video/episode1/014.webm", loop=True)
image ep1_015 = Movie(play="video/episode1/015.webm", loop=True)
image ep1_016 = Movie(play="video/episode1/016.webm", loop=True)
image ep1_137 = Movie(play="video/episode1/137.webm", image="images/episode1/137.webp", loop = False)

label episode1:
    $ persistent.mc = toby
    $ persistent.memories_fixed = True

    stop music fadeout 1.0
    scene expression ("images/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(1, 1) with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_newEpisode

    $ progress = 1
    scene expression ("images/episode1/001.webp") with dissolve

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Life is a lot more fragile than we think.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}How quickly things can change forever.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}One day you're up and the next day you're down.{/i}"
    scene expression ("images/episode1/002.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I can't believe that my [dad]'s company went bankrupt and now we have to move.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I was so used to having everything I wanted and now all of a sudden everything is gone.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}We just lost our house, the one with a pool, a sauna, 10 rooms, an indoor cinema, 8 bathrooms and ... Shit, it's so hard to say goodbye to all this.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I still hope this is just a bad dream and in the morning when I wake up, I'll still have my sports car out front, the one I got for my 18th birthday.{/i}"
    scene expression ("images/episode1/003.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}My [father] had a saying, \"When you reached the top of the mountain you should take a break and look down for a bit.\"{/i}"

    label memory_01:
        scene expression ("images/episode1/004.webp") with dissolve
        show ep1_004 with dissolve


        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Speaking of down. That's Emma. She's my girlfriend. We just hooked up a few months ago.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I used to be in the same class as her [sister], Cindy. That's how we met.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I was paying Cindy to help me with my homework. By help, I mean she was doing it all for me.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think I was a little bit too spoiled.{/i}"
        scene expression ("images/episode1/005.webp") with dissolve
        show ep1_005
        hide ep1_004
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Says the guy who is getting sucked by a beautiful blond babe. I'm still spoiled.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}At least till she finds out that my [dad]'s company went bankrupt and that's the real reason why we're leaving.{/i}"
        scene expression ("images/episode1/006.webp") with dissolve
        emma "Dear, is everything all right? You seem a little bit off today."
        toby "Don't worry, sweetie. I'm fine. it's just that tomorrow is the day we leave the city and who knows when we'll see each other."
        emma "Awww. You're so sweet. You don't want to leave me?"
        toby "Of course not. You're the best thing that's ever happened to me."
        scene expression ("images/episode1/007.webp") with dissolve
        emma "You can always come visit me, or better yet, I can come visit you. I'm sure there are plenty of 5 star hotels in that city, and we can spend a few nights like this."
        toby "Yeah... You're right!"
        emma "Of course I am. Nothing can keep us apart."
        menu:
            "{i}[JGR]kiss her{/i}"(csq="Emma +1"):
                scene expression ("images/episode1/008.webp") with dissolve
                $ emma_rel += 1
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}5 star hotels my ass. I have to tell her sooner or later that I'm broke.{/i}"
                scene expression ("images/episode1/007.webp") with dissolve
            "{i}don't kiss her{/i}":
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}5 star hotels my ass. I have to tell her sooner or later that I'm broke.{/i}"
        emma "So, what do you say? Wanna fuck me like this is your last day on earth?"
        toby "Is that even a question?"
        scene expression ("images/episode1/009.webp") with dissolve
        emma "Not at all."
        toby "Shit, you're so wet already."
        scene expression ("images/episode1/010.webp") with dissolve
        emma "With a boyfriend like you, I'm always wet."
        emma "And you're always hard."
        menu:
            "{i}[JGR]dirty talk{/i}"(csq="Emma +1 & Gallery Image"):
                $ unlockImage(persistent.emma_01)
                $ ep1_emma_dirtyTalk = True
                $ emma_rel += 1
                toby "Shut up and ride me like the whore you are. I'm gonna fill you up bad."
                emma "I love it when you talk dirty to me."
            "{i}clean talk{/i}"(csq="Emma +1"):
                $ emma_rel += 1
                toby "What have I done to deserve a girl like you?"
                emma "You made me smile when I was down, so I'm just repaying you for the best months of my life."
        scene expression ("images/episode1/011.webp") with dissolve
        show ep1_011
        emma "Yes, yes, yes. Give it to me baby."
        if ep1_emma_dirtyTalk == True:
            toby "That's it. Ride my cock you dirty bitch."
        else:
            toby "I love you so much!"
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nMe too!"
        scene expression ("images/episode1/012.webp") with dissolve
        show ep1_012
        hide ep1_011
        if ep1_emma_dirtyTalk == True:
            toby "You like to scream?"
            emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes, yessss I do."
            toby "Then scream that you're a whore."
            emma "{size=12}{color=#FDCA6E}* loud *{/color}{/size}\nI'm a WHORE."
            toby "Who's whore are you?"
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI'm YOUUURS!"
        else:
            toby "You're so perfect."
            emma "{size=12}{color=#FDCA6E}* loud *{/color}{/size}\nYes, yes, YESSSS."
            emma "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nDon't stop."
        scene expression ("images/episode1/013.webp") with dissolve
        show ep1_013
        hide ep1_012
        emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYour dick is so big, I'll never get used to it."
        if ep1_emma_dirtyTalk == True:
            toby "You like big dicks, you hungry bitch?"
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI only love your big dick."
            toby "You dream about my dick?"
            emma "{size=12}{color=#FDCA6E}* loud *{/color}{/size}\nYes, I DO!"
        else:
            toby "Am I hurting you?"
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nNo, your dick is perfect. I'm so gonna miss it!"
            toby "I'll miss your beautiful breasts."
        scene expression ("images/episode1/014.webp") with dissolve
        show ep1_014
        hide ep1_013
        emma "{size=12}{color=#FDCA6E}* loud *{/color}{/size}\nYES, YES, yesss... Fuck me hard, baby."
        toby "Let's change positions."
        scene expression ("images/episode1/015.webp") with dissolve
        show ep1_015
        hide ep1_014
        if ep1_emma_dirtyTalk == True:
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes, yes. Fuck me from behind like you fuck a dirty whore."
            toby "Are you a dirty whore?"
            emma "{size=12}{color=#FDCA6E}* loud *{/color}{/size}\nYES I AM."
        else:
            emma "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nI'm gonna cum soon. I always do when you fuck me from behind."
            toby "I'm so close too."
        scene expression ("images/episode1/016.webp") with dissolve
        show ep1_016
        hide ep1_015
        emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes, yes. Right there!"
        emma "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nDon't stop!"
        toby "I'm about to cum!"
        if ep1_emma_dirtyTalk == True:
            emma "I'm on the pill! Fill me up!"
        else:
            emma "Don't worry, I'm on the pill!"
        scene expression ("images/episode1/017.webp") with dissolve
        hide ep1_016
        with flash
        with flash
        emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nGosh, this was so good!"
        toby "Shit... It was so, so good."
        scene expression ("images/episode1/018.webp") with dissolve
        emma "I love you so much."
        toby "Me too!"

        $ unlockMemory(persistent.memory_01)
        $ renpy.end_replay()

    emma "I don't know what I'll do without you here."
    toby "You still have your [sister]."
    emma "Cindy?"
    emma "She's never home, ever since she hooked up with that guy."
    scene expression ("images/episode1/019.webp") with dissolve
    toby "Well, as you said, I can come to visit you from time to time."
    emma "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\nAnd I'll send you nudes so that you won't forget me."
    toby "How could I forget a beautiful girl like you."
    emma "You're spoiling me."
    toby "You deserve the best. Right?"
    scene expression ("images/episode1/020.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/021.webp") with dissolve
    emma "If you say so, I believe you."


    show screen ui_message("Sunday") with long_dissolve
    $ progress = 2
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode1/022.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I slept like a log. Last night was crazy.{/i}"
    scene expression ("images/episode1/023.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's so beautiful when she's sleeping. I'm gonna miss spending time with her.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Spending time? Who am I kidding? I'm gonna miss fucking her.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should go take a shower.{/i}"
    scene expression ("images/episode1/024.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should tell Emma the real reason why we're leaving.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But what if she's really like my [sister] says?{/i}"
    scene expression ("images/episode1/025.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What if she's actually with me only for the money. I mean, I'm not the best looking guy.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}The sex is good, but I feel like I should be able to talk about everything with my girlfriend.{/i}"
    scene expression ("images/episode1/026.webp") with dissolve
    emma "Morning sexy."
    toby "Good morning, beautiful."
    scene expression ("images/episode1/027.webp") with dissolve
    emma "Somebody is happy to see me."
    toby "He's always happy to see you."
    scene expression ("images/episode1/028.webp") with dissolve
    $ unlockImage(persistent.emma_02)
    emma "Not today, dear. We had fun last night, and we'll have more fun when your daddy comes to visit me. Okay?"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's so crazy and fun when she talks to my dick!{/i}"
    emma "Here... Let me give you a good night kiss!"
    emma "But you better go to sleep afterward."
    scene expression ("images/episode1/029.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/030.webp") with dissolve
    emma "I told him to go to sleep!"
    toby "I saw."
    emma "I love you."
    toby "I love you too!"
    scene expression ("images/episode1/031.webp") with dissolve
    emma "Can you please wash my back?"
    toby "Sure."


    scene expression ("images/episode1/032.webp") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/033.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()


    $ progress = 3
    scene expression ("images/episode1/034.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nHere we go. After spending my whole life in one city I'm finally moving to a different one.{/i}"
    scene expression ("images/episode1/035.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    "*notification sound*"
    scene expression ("images/episode1/034.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI can't say that I wanted to stay there forever, but I always imagined myself moving out on my own at this age, not like this.{/i}"
    scene expression ("images/episode1/035.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    "*notification sound*"
    scene expression ("images/episode1/034.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI'm 20 already. My life is going nowhere. I always planned to get my [father]'s company one day, but after what happened, now I don't know what to do with my life.{/i}"
    scene expression ("images/episode1/035.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    "*notification sound*"
    scene expression ("images/episode1/034.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nWe went bankrupt. We lost everything and now we're moving to a city where my [father]'s partners are. A friend of his will let us stay there, but who knows for how long.{/i}"
    scene expression ("images/episode1/035.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    "*notification sound*"
    scene expression ("images/episode1/036.webp") with dissolve
    toby "Do you mind? Just put your phone on silent already."
    scene expression ("images/episode1/037.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nThat's Patricia, or Tris as people call her. She's my younger [sister]. Always acting like she deserves everything. Just like now. \nI'm talking, and she doesn't even bother answering me.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nWe used to get along quite well, but for the past few months it's like she went mad. I don't know what's gotten into her, but I can't even have a normal conversation with her.{/i}"
    scene expression ("images/episode1/036.webp") with dissolve
    toby "I'm talking to you, idiot. Put your phone on silent!"
    scene expression ("images/episode1/038.webp") with dissolve
    patricia "You done?"
    toby "I'm not done! I said, put your phone on silent like a normal person!"
    patricia "Hold that thought."
    scene expression ("images/episode1/039.webp") with dissolve
    toby "Really?"
    toby "Get your feet off my lap!"
    scene expression ("images/episode1/040.webp") with dissolve
    patricia "Umm... Nah! \nI'm comfortable."
    scene expression ("images/episode1/041.webp") with dissolve
    toby "I said MOVE YOUR LEGS!"
    scene expression ("images/episode1/042.webp") with dissolve
    erwin "Stop it, you two! You're both young adults. Act like it!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nThat's my [dad]. The guy who lost everything. He says that we're young adults, but he never told us how he managed to lose everything.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nIt was just \"Kids, we're bankrupt and we have to move!\". No explanation, no nothing. He doesn't respect us and never has, but now he expects us to behave like young adults!{/i}"
    scene expression ("images/episode1/043.webp") with dissolve
    charlotte "Let the kids be. They are just getting bored. It's a long drive. You can't expect them to stay still!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nAnd that's my [mom]. She's the only normal person in this [family]. She used to be a simple country girl, but then she married [dad], and he kinda gave her everything she wanted.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nSo she might be a bit spoiled, but even so she took the whole bankruptcy pretty well. I guess the fact that she was not always wealthy made her a bit stronger, unlike [dad] and [sis], maybe even myself.{/i}"
    scene expression ("images/episode1/044.webp") with dissolve
    erwin "They are just kids. That's all you can say. That's your excuse for raising two spoiled brats."
    charlotte "You did not just say that about our [kids]. I raised them well. It's you who screwed up and want to find someone to blame!"
    erwin "Oh, but I have someone to blame for this situation."
    charlotte "Don't even try!"
    scene expression ("images/episode1/045.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode1/046.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nWe had it coming.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nLately [mom] and [dad] argue a lot. I think this whole situation had an impact on their relationship.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nNow I feel bad for causing this situation. I should have just left Tris alone.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI hate it when these two argue. It feels like forever since we've been happy. I can't believe how going broke can ruin a [family].{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI just hope they won't get divorced. I'd hate that, but knowing [dad] he'll do everything he can to not lose [mom] and get his company back.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nHe was always like that and he constantly tried to make me be like him. Thanks to him, I'm no quitter either.{/i}"


    $ progress = 4

    scene expression ("images/episode1/047.webp") with long_dissolve
    erwin "Here we are. Home sweet home."
    patricia "It's looking very crowded and small!"
    erwin "Get used to it for now. You're no longer a princess!"
    charlotte "Stop it, please!"
    charlotte "Look, honey, it is indeed smaller than our previous house, but as long as we're happy, it's enough!"
    scene expression ("images/episode1/048.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nGood thing we're happy.{/i}"
    scene expression ("images/episode1/049.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nMy back hurts already just thinking about how many boxes we'll have to carry inside.{/i}"
    scene expression ("images/episode1/050.webp") with dissolve
    charlotte "Come on sweetie. Let's see your room! The boys can handle the boxes!"
    patricia "Do I get to choose my room?"
    charlotte "Sure! Let's go inside."
    scene expression ("images/episode1/051.webp") with dissolve
    erwin "Choose her own room. What a joke. There are only two rooms. She's so spoiled."
    toby "Look [dad]. I understand you're pissed about losing everything, but stop taking out your problems on them, especially on [mom]."
    toby "If you want to let off some steam, we can go to a gym and hit every punchbag there is, but [mom] and [sis] don't deserve this."
    scene expression ("images/episode1/052.webp") with dissolve
    erwin "..."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nThat's what I thought. He never liked listening to anybody!{/i}"
    erwin "Are you gonna help me with these boxes, or are you just going to stand there fuming about what I've done wrong?"
    toby "I'm coming because I'm not looking for someone to lay my problems on!"
    erwin "Fine, you're right, I overstepped."
    scene expression ("images/episode1/053.webp") with dissolve
    toby "And you're sorry?"
    erwin "Not as sorry as you'll be once we finish with all the boxes!"
    scene expression ("images/episode1/054.webp") with dissolve
    erwin "Here... Let's see if I've wasted my money paying for your gym membership all these years!"
    toby "Haha, very funny!"
    scene expression ("images/episode1/055.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/056.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/055.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/056.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()


    $ progress = 5

    show screen ui_message("A few hours later") with fade
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/057.webp") with dissolve
    hide screen ui_message
    patricia "Pizza is here!"
    toby "Finally, I'm starving!"
    scene expression ("images/episode1/058.webp") with dissolve
    erwin "I asked you if you wanted me to stop at a restaurant, and you all said no."
    charlotte "That was 7 hours ago."
    scene expression ("images/episode1/059.webp") with dissolve
    erwin "Speaking of 7 hours ago..."
    erwin "Someone in this room told me that I acted like an ass with you. I won't say who, but he's right!"
    erwin "I'm sorry Charlotte, for yelling at you and Tris. I'm sorry we're in this situation!"
    erwin "You're still my favorite [daughter]."
    scene expression ("images/episode1/060.webp") with dissolve
    toby "*cough*\nOnly [daughter]!"
    scene expression ("images/episode1/059.webp") with dissolve
    erwin "Whatever, you're both my [children], and you deserve the best. That's the reason I work so hard."
    erwin "For you and for my beautiful wife."
    erwin "I'm sorry that you two have to share a room. Once we have more money, I'll hire someone to fix up the attic for [toby!c]!"
    toby "Why do I have to move into the attic?"
    erwin "Because you're so wise and opened my eyes to my mistakes, maybe from up there you'll have more revelations like that."
    scene expression ("images/episode1/061.webp") with dissolve
    patricia "So he'll have to sleep on the floor to make it look like an upgrade when he moves from my room to the attic?"
    charlotte "That's my girl! I like the way you think!"
    scene expression ("images/episode1/062.webp") with dissolve
    toby "I'm sorry, but I'm gonna eat. I don't hear well when I'm hungry. I just heard something like the attic and sleep on the floor!"
    charlotte "Bon Appétit."
    scene expression ("images/episode1/063.webp") with long_dissolve
    toby "Either this pizza was really good, or we were starving!"
    scene expression ("images/episode1/066.webp") with dissolve
    charlotte "The pizza was really good! I heard a lot of good things about food in this city!"
    scene expression ("images/episode1/067.webp") with dissolve
    patricia "I heard that they have a beautiful beach!"
    scene expression ("images/episode1/064.webp") with dissolve
    erwin "On my last business trip here, I stayed in a hotel near the beach. I went there every morning for a jog, and I can say, it's gorgeous!"
    scene expression ("images/episode1/065.webp") with dissolve
    toby "We should go there tomorrow."
    scene expression ("images/episode1/068.webp") with dissolve
    patricia "I can't. I have to register at the local High School!"
    scene expression ("images/episode1/065.webp") with dissolve
    toby "Sucks to be you!"
    scene expression ("images/episode1/068.webp") with dissolve
    patricia "At least once I finish High School, I'll go to college, unlike someone else at this table."
    scene expression ("images/episode1/065.webp") with dissolve
    toby "I wanted to focus more on making money than studying."
    scene expression ("images/episode1/066.webp") with dissolve
    charlotte "And how is that going?"
    scene expression ("images/episode1/064.webp") with dissolve
    erwin "If he's anything like his [father], he'll be just fine!"
    scene expression ("images/episode1/069.webp") with dissolve
    erwin "Actually, I don't think I'm the best example at the moment, but if he's like I was a few years ago, he'll be just fine!"
    scene expression ("images/episode1/070.webp") with dissolve
    patricia "I'm tired. I'll go take a shower."
    patricia "By the way [toby!c], try not to get too comfortable in my bed!"
    toby "Yeah, yeah!"


    $ progress = 6

    scene expression ("images/episode1/071.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI should let Emma know that we have settled in and see what she's doing.{/i}"

    scene expression ("images/episode1/072_texting.webp") with dissolve
    call sms_sent ("emma", "Hey sexy. I have arrived at my new home.\nHow are you?") from _call_sms_sent_4
    call sms_incoming ("emma", "Hi sexy!\n I just got out of the shower. How is the new place?") from _call_sms_incoming_5
    call sms_sent ("emma", "Not as big as the other one, but it's fine.") from _call_sms_sent_5
    call sms_incoming ("emma", "Speaking of big. Is it me or did my boobs get a little bit bigger?", img_icon="images/episode1/077_icon.webp", img="images/episode1/077.webp") from _call_sms_incoming_6
    call sms_sent ("emma", "I need a picture with both your ass and boobs so I can compare them.") from _call_sms_sent_6
    call sms_incoming ("emma", "You dirty hog.") from _call_sms_incoming_7
    call sms_incoming ("emma", "So? What do you think?", img_icon="images/episode1/081_icon.webp", img="images/episode1/081.webp") from _call_sms_incoming_8
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nShe's so hot! I can't believe she's my girlfriend.{/i}"
    window hide
    $ unlockImage(persistent.emma_03)
    call sms_sent ("emma", "Yeah, you're right, your boobs got a little bit bigger.") from _call_sms_sent_7
    call sms_incoming ("emma", "How big? I need a dick pic, so I can compare.") from _call_sms_incoming_9
    hide screen message


    scene expression ("images/episode1/084.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/085.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nIf the lady wants, the lady wants. You can't argue with that.{/i}"
    scene expression ("images/episode1/086.webp") with dissolve
    toby "Shit!"
    patricia "Oh my God! You perv. You're taking dick pics in my bed?"
    toby "No?"
    scene expression ("images/episode1/087.webp") with dissolve
    patricia "Just go, please take a cold shower."
    toby "Sorry you had to see that!"
    patricia "You're gross, and make sure to wash your dirty hands!"
    scene expression ("images/episode1/088.webp") with dissolve
    toby "Umm... Yeah. See you later!"
    scene expression ("images/episode1/089.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/090.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nThis was so good. It's nice to release some stress after such a day.{/i}"
    scene expression ("images/episode1/091.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI should take a shower now.{/i}"
    scene expression ("images/episode1/092.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nUmm. Where should I put my blanket? This room is so small.{/i}"
    scene expression ("images/episode1/093.webp") with dissolve
    patricia "You can sleep in the bed, but make sure you keep your hands to yourself, you perv!"
    toby "I'm not a pervert. I just miss my girlfriend."
    patricia "Then you can sleep on the floor!"
    scene expression ("images/episode1/094.webp") with dissolve
    toby "Don't be like that, she's not that bad!"
    scene expression ("images/episode1/095.webp") with dissolve
    patricia "She's a gold digger!"
    toby "She's not! Look at us, we have no money left, and she still loves me!"
    patricia "Does she know that we're broke?"
    toby "Umm..."
    toby "Maybe?"
    patricia "Yeah, right! You do you, but don't come to me crying when she leaves you."
    toby "Don't worry about me! I'll be just fine."
    scene expression ("images/episode1/096.webp") with dissolve
    patricia "Whatever!"


    $ progress = 7
    show screen ui_message("Monday") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/097.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nMan, I slept like a log. I wonder what time it is.{/i}"
    scene expression ("images/episode1/098.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nShit, Tris is getting ready for school. What should I do?{/i}"
    menu:
        "{i}[JGR]take a peek{/i}"(csq="Tris +1 & Gallery Image"):
            $ ep1_peek_on_patricia = True
            $ patricia_rel += 1
            $ unlockImage(persistent.patricia_01)
            scene expression ("images/episode1/099.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI'll be damned. Look at those perky boobs. She looks so good!{/i}"
            scene expression ("images/episode1/100.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nToo bad I have a girlfriend.{/i}"
            scene expression ("images/episode1/101.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nDamn it [toby!c]. She's your [sister], stupid. You can't look at your [sister] like that.{/i}"
            scene expression ("images/episode1/102.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nEven though she's hot as hell.{/i}"
        "{i}be a good [brother]{/i}":
            scene expression ("images/episode1/101.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nNope. Not today. Today I'm a good [brother].{/i}"
    scene expression ("images/episode1/103.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nNew day, new city. I feel like I should help [dad] with money, but I'm not sure what I could do to earn it.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI could always go job hunting, but the only job I ever had was in my [dad]'s company and let's be honest, I was kinda spoiled.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nNobody really expected me to do anything anyway, so it's really still like I've never worked a day in my whole life.{/i}"
    scene expression ("images/episode1/104.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nAnyway, I'm starving. Let's see what we have in the fridge, if anything.{/i}"
    scene expression ("images/episode1/105.webp") with dissolve
    toby "Morning [mom]!"
    scene expression ("images/episode1/106.webp") with dissolve
    charlotte "Morning sweetie. How did you sleep?"
    scene expression ("images/episode1/107.webp") with dissolve
    toby "Very bad. The floor was quite hard."
    charlotte "Poor baby. Was it really, really hard?"
    toby "Yes. My [sister] is so bad. I asked her like a thousand times to let me sleep in her bed, but she wouldn't let me."
    scene expression ("images/episode1/108.webp") with dissolve
    charlotte "Oh, poor baby. Come to [mommy]. Let her give you a kiss!"
    menu:
        "{i}[JGR]let her kiss you{/i}"(csq="Charlotte +1 & Gallery Image"):
            $ unlockImage(persistent.charlotte_01)
            $ charlotte_rel += 1
            scene expression ("images/episode1/109.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode1/110.webp") with dissolve
            charlotte "Better?"
            toby "Much better!"
            charlotte "You know what I find funny?"
            toby "No. What?"
            charlotte "Tris just told me that she let you sleep in the bed, and on top of that, I came by last night to say good night, and saw it with my own eyes."
            toby "Oh. Maybe I lied just to get a kiss?"
            charlotte "Of course. Next time when you want [mommy] to kiss you, just ask!"
            toby "Will do!"
        "{i}tell her you lied{/i}":
            scene expression ("images/episode1/110.webp") with dissolve
            toby "I was joking. She let me sleep in the bed last night."
            charlotte "I know. She bragged about that this morning, on top of that, I came by last night to say good night, and you both were sleeping like babies."
            toby "Oh, so all this acting was pointless?"
            charlotte "Kind of!"
    scene expression ("images/episode1/111.webp") with dissolve
    toby "By the way, do we have anything to eat?"
    charlotte "I haven't had time to go to the store just yet, so we only have milk and cereal for now."
    toby "Good enough!"
    scene expression ("images/episode1/112.webp") with dissolve
    toby "What are you looking at?"
    charlotte "Nothing much, just some jobs around town."
    toby "For?"
    charlotte "For me, obviously. We really need the money."
    scene expression ("images/episode1/113.webp") with dissolve
    toby "Anything interesting for me?"
    charlotte "You don't have to work, honey!"
    toby "But I do. I'm 20 now and have never worked a day in my life."
    toby "I feel too spoiled. I need to do something with my life!"
    charlotte "Well the most interesting job I found so far is this one for a real estate agent."
    toby "Let me see!"
    scene expression ("images/episode1/114.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\n[mom!c]'s cleavage is huge!{/i}"
    menu:
        "{i}[JGR]take a better look{/i}"(csq="Charlotte +1 & Gallery Image"):
            $ charlotte_rel += 1
            $ unlockImage(persistent.charlotte_02)
            scene expression ("images/episode1/115.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI can't believe how good she looks for a woman her age.{/i}"
            scene expression ("images/episode1/116.webp") with dissolve
            charlotte "So? What do you think?"
            scene expression ("images/episode1/117.webp") with dissolve
            toby "Umm..."
            scene expression ("images/episode1/118.webp") with dissolve
        "{i}I shouldn't risk it{/i}":
            scene expression ("images/episode1/118.webp") with dissolve
            charlotte "So? What do you think?"
    toby "Yeah. I mean, the job looks interesting, and on top of that, I'm pretty good at convincing people, so I could give it a try."
    charlotte "Are you sure you want to work so soon?"
    toby "It's not like I'm getting any younger. Sooner or later, I'll need to start working. Now is better."
    scene expression ("images/episode1/119.webp") with dissolve
    charlotte "But what will happen when you go to college? Or do you still think it's pointless?"
    toby "I'm still thinking about going to college. I know that there is a good college here. Emma said that it would be nice to join next year with her because she also was going to come here."
    charlotte "Oh. I see. I'm happy for you then."
    charlotte "By the way, how is she taking all this? Your move, the fact that you won't be able to buy her diamond earrings and so on?"
    scene expression ("images/episode1/120.webp") with dissolve
    toby "Uhm... Good, I guess!"
    charlotte "You haven't told her the real reason why we had to leave, have you?"
    toby "No, she knows, more or less!"
    scene expression ("images/episode1/119.webp") with dissolve
    charlotte "You should talk to her. I'm sure she'll understand the situation."
    toby "What if she leaves me when she finds out that I'm broke?"
    charlotte "She won't, because no matter what others think, she really likes you, and if you do get dumped, well, then she was not the right one for you."
    toby "I know, but..."
    scene expression ("images/episode1/121.webp") with dissolve
    charlotte "Yeah, I know. She has a great ass, huge boobs for her age, her face is beautiful, and she's probably excellent in bed, but that's not all that matters in a relationship!"
    toby "That was very specific."
    charlotte "It's not like you're 16. You're a grown man. I know you're not a virgin anymore!"
    toby "[mom!u]!"
    scene expression ("images/episode1/119.webp") with dissolve
    charlotte "Anyway. Like I was saying, it's better to let her know what happened than letting her think that you don't love her anymore. And that's why the gifts are getting cheaper."
    toby "You think so?"
    charlotte "Of course!"
    toby "Or I could work my ass off and keep on buying her expensive things, and she won't know!"
    charlotte "I like the idea of working your ass off, but the expensive part and the lies not so much. That's not how you were raised."
    scene expression ("images/episode1/121.webp") with dissolve
    toby "Yeah, you're probably right!"
    scene expression ("images/episode1/122.webp") with dissolve
    charlotte "Anyway. I should get dressed and get the groceries. The phone number for that job is on my laptop if you really want it."
    toby "Thanks, [mom]."
    charlotte "No, thank you for being such a good [son]."
    charlotte "See you later!"
    scene expression ("images/episode1/123.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\n[mom!c] is right. I should talk to Emma about what really happened. Maybe when she comes to visit me I'll tell her the truth.{/i}"
    scene expression ("images/episode1/124.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nLet's see what's up with this job?{/i}"
    scene expression ("images/episode1/125.webp") with dissolve
    toby "Good morning. I saw an ad about a job as a real estate agent. I was wondering if the job is still available?"
    $ progress = 8
    woman "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nGood morning. Yes, the job is still available. \nHave you ever worked as a real estate agent before?"
    toby "No. Actually, this would be my first job."
    woman "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nHow old are you?"
    toby "I'm 20 years old. I just moved to town and am looking for a job."
    woman "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nI understand. Are you available today at 11 AM for an interview?"
    toby "Of course!"
    woman "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nI'm glad to hear it. I'll text you the details."
    toby "Thank you very much!"
    woman "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nWhat was your name?"
    toby "Sorry, I forgot to introduce myself."
    toby "My name is [toby!c]."
    woman "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nOkay [toby!c]. See you later!"
    toby "Yes, sure!"
    woman "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nHave a good day!"
    toby "Have a good day!"
    scene expression ("images/episode1/126.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nWell, that was easy. I never knew it was this easy to get a job!{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nOr maybe I'm just a lucky guy.{/i}"
    scene expression ("images/episode1/127.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nLet's see what's on TV.{/i}"
    show screen ui_message("A short time later") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/128.webp") with dissolve
    hide screen ui_message
    charlotte "Sweetie, can you please come and help me with the bags?"
    toby "Sure [mom]."
    scene expression ("images/episode1/129.webp") with dissolve
    toby "Where do you want them?"
    charlotte "Over there. I'll sort them out!"
    scene expression ("images/episode1/130.webp") with dissolve
    charlotte "Did you call the real estate agency?"
    toby "Yes, and I have an interview at 11:00."
    charlotte "Today?"
    toby "Yes! I should get ready soon."
    charlotte "That was fast. They must really need people."
    toby "Or I'm just a lucky guy?"
    charlotte "You're just lucky!"
    scene expression ("images/episode1/131.webp") with dissolve
    charlotte "I mean, look at your [mom], you have to be really lucky to have [mom] like me!"
    toby "Now I know who Tris takes after."
    charlotte "You're hilarious!"
    scene expression ("images/episode1/132.webp") with dissolve
    toby "I'm going to get changed for the interview."
    scene expression ("images/episode1/133.webp") with long_dissolve
    charlotte "Oh my... Who is that handsome guy?"
    charlotte "If you go dressed like that, they will hire you on the spot!"
    toby "I can only hope so!"
    scene expression ("images/episode1/134.webp") with dissolve
    charlotte "Here... Let me fix this!"
    toby "Thanks [mom]."
    charlotte "You can take my car and pick up Patricia from school when you're done."
    toby "Sure. I'll do that, then I'll come pick you up, and we'll all go to the beach!"
    charlotte "If that's what you want, how can I say no to you!"
    scene expression ("images/episode1/135.webp") with dissolve
    charlotte "Good luck sweetie."
    toby "Thanks [mom]!"


    $ progress = 9

    scene expression ("images/episode1/136.webp") with long_dissolve
    toby "Hello, I'm here for the job interview."
    window hide
    show ep1_137 with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/137.webp") with dissolve
    hide ep1_137
    woman "You must be [toby!c], right?"
    toby "Yes ma'am."
    katrina "You can call me Katrina."
    scene expression ("images/episode1/138.webp") with dissolve
    katrina "Take a seat please."
    toby "Thank you, ma'am."
    toby "I mean, Katrina."
    scene expression ("images/episode1/139.webp") with dissolve
    katrina "So? Who is [toby!c]? Tell me more about yourself!"
    scene expression ("images/episode1/140.webp") with dissolve
    toby "Well, I'm 20 years old. I just moved to this city, and I thought that I should get a job to help my [family]."
    scene expression ("images/episode1/139.webp") with dissolve
    katrina "Where did you live before moving here?"
    scene expression ("images/episode1/140.webp") with dissolve
    toby "Uhm, Rictown."
    scene expression ("images/episode1/139.webp") with dissolve
    katrina "Oh, interesting. I also used to live there. Which part of the city did you live in?"
    scene expression ("images/episode1/140.webp") with dissolve
    toby "I prefer not to say, if that's okay?"
    scene expression ("images/episode1/141.webp") with dissolve
    katrina "No, boy. It's not okay. I ask, you answer!"
    toby "Uhm. I lived in the upper part."
    katrina "You mean the rich part?"
    toby "Yes."
    scene expression ("images/episode1/139.webp") with dissolve
    katrina "Your [parents] worked for some rich ass there?"
    scene expression ("images/episode1/140.webp") with dissolve
    toby "Uhm, not really."
    scene expression ("images/episode1/142.webp") with dissolve
    katrina "Interesting... So you come from a wealthy [family]."
    scene expression ("images/episode1/143.webp") with dissolve
    katrina "And how come you want to work here if you come from a wealthy [family]?"
    toby "Why does anyone want a job?"
    katrina "I understand. You're broke."
    scene expression ("images/episode1/144.webp") with dissolve
    katrina "So, do you think you've got what it takes to satisfy me?"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nThis woman is crazy.{/i}"
    menu:
        "Uhm, satisfy you?":
            katrina "Yes sweetie, to work your ass off till I'm satisfied."
            katrina "What else?"
            toby "Nothing. Yes, I really do think I can work till you're satisfied."
            scene expression ("images/episode1/145.webp") with dissolve
            katrina "No, I don't like how that sounds. I'll say it again."
            katrina "Do you think you can satisfy me?"
        "[JGR]I can satisfy any woman, so why would you be any different?"(csq="Katrina +1 & Gallery Image"):
            $ katrina_rel += 1
            $ unlockImage(persistent.katrina_01)
            katrina "Bold! I like it, but I was thinking more like, can you work your ass off till I'm satisfied?"
            toby "Oh, yes. I really do think I can work till you're satisfied."
            scene expression ("images/episode1/145.webp") with dissolve
            katrina "Actually, I liked your first answer better."
            katrina "Do you think you can satisfy me?"

    scene expression ("images/episode1/146.webp") with dissolve
    toby "Yes, ma'am. I can satisfy you!"
    scene expression ("images/episode1/147.webp") with dissolve
    katrina "So if you really want to earn money why don't you sell drugs like a normal person? You really want to enter a broken system like this, where the big fish takes everything, and you get only what they give you?"
    katrina "Why be a slave when you can be a king?"
    scene expression ("images/episode1/148.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nIs she really asking me this? What kind of interview is this?{/i}"
    scene expression ("images/episode1/149.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    $ progress = 10
    woman "Uhum, uhum. Excuse me!"
    scene expression ("images/episode1/150.webp") with dissolve
    katrina "Hi there, darling. I was testing your future employee."
    woman "I'm sure."
    scene expression ("images/episode1/151.webp") with dissolve
    woman "You must be [toby!c] right?"
    toby "Yes, ma'am."
    scene expression ("images/episode1/152.webp") with dissolve
    darlene "My name is Darlene. We talked this morning on the phone."
    toby "Nice to meet you!"
    scene expression ("images/episode1/153.webp") with dissolve
    darlene "Sorry, I'm late. I had some unfinished business with a few apartments."
    scene expression ("images/episode1/154.webp") with dissolve
    toby "No problem."
    darlene "I hope my girlfriend didn't give you too much trouble."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nGirlfriend? My future boss is a lesbian? Wow!{/i}"
    toby "Not at all."
    darlene "I'm glad to hear it."
    scene expression ("images/episode1/155.webp") with dissolve
    darlene "Sweetheart, could you leave us, please? I want to get to know [toby!c] a little bit better!"
    katrina "Of course, my love."
    scene expression ("images/episode1/156.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/157.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/158.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nOkay... That was very suspicious.{/i}"
    scene expression ("images/episode1/159.webp") with dissolve
    darlene "So, on the phone you mentioned that you just moved to town and you're already looking for a job. I like this in a person."
    darlene "It means they are hard-working. However, you also mentioned that this would be your first job. Why is that?"
    toby "Well, this would be my first real job. I used to help out at my [dad]'s company a lot, but things didn't work out so well for us, and now we've moved here."
    darlene "Do you know anything about houses?"
    toby "I do know a bit of the structural parts of a house, and I'm very good at reading people, so I can persuade them to buy or rent a house."
    scene expression ("images/episode1/160.webp") with dissolve
    darlene "Is that so? Then let's hear what you have to say about me?"
    toby "Uhm? That would not be appropriate."
    darlene "You can make it sound appropriate or just say whatever you want, and we'll decide what to do with those pieces of information."
    scene expression ("images/episode1/161.webp") with dissolve
    $ progress = 11
    menu:
        "{i}[JGR]go personal{/i}"(csq="Darlene +1 & Gallery Image"):
            $ darlene_rel += 1
            $ unlockImage(persistent.darlene_01)
            scene expression ("images/episode1/162.webp") with dissolve
            toby "You're in a relationship with another woman even though you're not 100%% sure you're a lesbian. Most likely you had some failed relationships and your heart got broken so badly, that you lost trust in men."
            toby "Even though you're the boss of your own company and you're used to being respected, you're tired of it."
            toby "You like it when someone else is in charge, that's why your girlfriend is so bossy because you like it, and you love the idea of being submissive outside work."
            toby "When you asked me to say something about you, you were expecting something more like, you're the type of woman who worked hard to get where you are right now."
            toby "That's because me being the interviewee should have not gotten this personal. But the fact that I'm talking down to you even though you could be my future boss makes you very excited."
            toby "Because deep down that's what you really want."
            scene expression ("images/episode1/163.webp") with dissolve
            darlene "Uhm... Yes, so."
            scene expression ("images/episode1/164.webp") with dissolve
            darlene "Sorry, I was not expecting that, so I'm not sure what to say."
            toby "I hope I didn't go overboard."
            darlene "Maybe a bit, but surprisingly it didn't bother me."
        "{i}stay safe{/i}":

            scene expression ("images/episode1/162.webp") with dissolve
            toby "You're the kind of woman who worked very hard to be where she is right now, and this company is like your baby."
            toby "By the size of the office, I can say that there aren't many people working here because you want to be able to know everything that goes on."
            toby "You like to be in control so that if something goes wrong, you can't blame anyone else but yourself."
            toby "When you heard that I'm 20 years old, you told yourself that you could teach me everything you know because you're a bit tired of working with people."
            toby "So you decided to hire someone young that you'll be able to groom and eventually trust."
            scene expression ("images/episode1/163.webp") with dissolve
            darlene "This was really, really good actually!"
            darlene "I like where this is going."

    scene expression ("images/episode1/165.webp") with dissolve
    darlene "I'll be honest with you. I like you, perhaps you're a little bit bold, but I like that."
    darlene "I'm sure that Kat gave you her number to call her because she likes to hire good looking guys at her club to attract young women."
    darlene "And if in a club there are young ladies, there will also be men to pay lots of money to impress them, so everybody gets to profit from that."
    darlene "I can't offer you the parties and fun she can, but I can offer you a very stable income and good life."
    darlene "Tomorrow I'm meeting with a client for an apartment. You will join me, and I'll let you do your thing."
    darlene "I want to see if you're really able to read people as good as you say and convince them to buy."
    darlene "I don't normally do things like this, but I really, really like you."
    darlene "So I'll give you a chance. If you manage to sell the apartment, you get 20%% of the profit."
    scene expression ("images/episode1/166.webp") with dissolve
    toby "I don't know what to say. I was not expecting this."
    scene expression ("images/episode1/167.webp") with dissolve
    darlene "You don't have to say anything now, just think about who you're gonna call tomorrow. Me or Kat."
    toby "Thank you for the opportunity. I'll sleep on it and call you first thing in the morning."
    scene expression ("images/episode1/168.webp") with dissolve
    darlene "I hope you'll make the right choice."
    toby "Thank you for this!"
    scene expression ("images/episode1/169.webp") with dissolve
    darlene "No, thank you! I really enjoyed this interview."
    toby "Have a great day ma'am."
    darlene "Please call me Darlene!"
    toby "Bye Darlene."
    darlene "Bye [toby!c]."


    $ progress = 12

    scene expression ("images/episode1/170.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nThat interview was really something. It wasn't what I expected, but both Darlene and Katrina were really interesting women.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI wonder who I should call. On one hand working as a real estate agent would be stable income and a safe job.{/i}"
    scene expression ("images/episode1/171.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nOn the other hand Katrina's life sounds interesting. I'm not so sure about the drugs thing, but from what Darlene said it does sound interesting.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI don't know what to do. I'll have to think more about it.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nAnyway, let's go pick up Tris from school.{/i}"
    scene expression ("images/episode1/172.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI should text Tris that I'm here.{/i}"
    scene expression ("images/episode1/173.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nHere comes the school girl.{/i}"
    scene expression ("images/episode1/174.webp") with dissolve
    toby "So how is the new school?"
    patricia "The school looks boring, but the gossip is something else here."
    toby "How come?"
    patricia "Well, for starters, a few months ago, the principal of this school got arrested for crimes involving a drug dealer of some sort."
    toby "This city is a strange place!"
    patricia "You're telling me? But to be honest, I think we'll fit in really well here. It's not like we're too normal."
    scene expression ("images/episode1/175.webp") with dissolve
    toby "Anyway, we should leave. [mom!c] is waiting for us to go to the beach!"
    patricia "Yes! I've been waiting for this the whole day!"
    patricia "By the way, why are you so dressed up?"
    toby "I had a job interview."
    patricia "You? Working?"
    scene expression ("images/episode1/176.webp") with dissolve
    toby "Yes. What's so strange about that?"
    patricia "You've never worked a day in your life."
    toby "I helped [dad] at his company."
    patricia "Yeah. Like I said, you've never worked a day in your life."
    patricia "But anyway. How did the interview go?"
    toby "I'll tell you later after we pick [mom] up. I really don't want to tell the same story twice."
    scene expression ("images/episode1/177.webp") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/178.webp") with dissolve
    toby "Why the rush?"
    patricia "Are you kidding me? I haven't seen a beach in almost 7 months."
    scene expression ("images/episode1/179.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nBoth [mom] and Tris take a long time to get ready.{/i}"
    scene expression ("images/episode1/180.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nWow. [mom] looks gorgeous.{/i}"
    charlotte "Is Tris ready?"
    toby "Not yet."
    patricia "I am! I'm coming down now!"
    scene expression ("images/episode1/181.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nLike [mother], like [daughter].{/i}"
    scene expression ("images/episode1/182.webp") with dissolve
    toby "Let's go then!"


    $ progress = 13

    scene expression ("images/episode1/183.webp") with long_dissolve
    patricia "This beach looks so cool. Can't wait to swim."
    charlotte "I can't wait to sleep on those loungers. They look comfy!"
    toby "Tired much?"
    scene expression ("images/episode1/184.webp") with dissolve
    charlotte "A little bit. Moving was a pretty big deal."
    scene expression ("images/episode1/185.webp") with dissolve
    patricia "Wow... They have a volleyball net. We really have to play [toby!c]."
    toby "Do we?"
    scene expression ("images/episode1/186.webp") with dissolve
    patricia "Yesss!"
    toby "Fine!"
    scene expression ("images/episode1/187.webp") with dissolve
    charlotte "So? How was the interview?"
    toby "It was excellent actually. There were there two women who offered me a job."
    patricia "You haven't worked a single day in your life and got two job offers from one interview?"
    toby "Yeah, it was strange."
    scene expression ("images/episode1/188.webp") with dissolve
    toby "So there is this woman named Darlene. She's the one I talked to on the phone this morning."
    toby "And her girlfriend, Katrina. She's the owner of a club as far as I understood."
    toby "When I went there, Katrina was in her office, and she made fun of me a little bit!"
    scene expression ("images/episode1/189.webp") with dissolve
    patricia "Well, your face begs to be made fun of!"
    scene expression ("images/episode1/190.webp") with dissolve
    charlotte "Don't be rude to your [brother]."
    scene expression ("images/episode1/188.webp") with dissolve
    toby "Anyway, so she kinda offered me a job at her club, but I'm not sure what yet, because that's when Darlene entered."
    scene expression ("images/episode1/191.webp") with dissolve
    charlotte "So basically she was stealing her girlfriend's employee?"
    toby "You could say they were fighting over me."
    scene expression ("images/episode1/192.webp") with dissolve
    patricia "That will be the first and last time two girls will fight over you."
    scene expression ("images/episode1/193.webp") with dissolve
    toby "Very funny."
    scene expression ("images/episode1/188.webp") with dissolve
    toby "Anyway, Darlene knew what Katrina did, so she said that I have until tomorrow to decide who to work for."
    toby "Tomorrow I'll either call Darlene or Katrina."
    scene expression ("images/episode1/194.webp") with dissolve
    charlotte "I think working for Darlene would be the best. It's a good job. You don't even know what you'll have to do at the club."
    scene expression ("images/episode1/195.webp") with dissolve
    patricia "I disagree with [mom]. I think working in the club could be more interesting and on top of that, who knows. Maybe you'll meet a new girlfriend."
    toby "I have a girlfriend."
    scene expression ("images/episode1/196.webp") with dissolve
    patricia "Maybe, but she's a bitch."
    charlotte "Watch your tongue, young lady. She's not a bitch, and as long as they love each other, that's all that matters."
    scene expression ("images/episode1/197.webp") with dissolve
    patricia "He didn't even tell her why we had to leave."
    charlotte "That's their business, not yours."
    patricia "She's a gold digger!"
    scene expression ("images/episode1/198.webp") with dissolve
    toby "Whatever!\nI'll go grab something to drink from the bar. Want anything?"
    patricia "I want a lemonade."
    toby "I'll buy you one if you take back what you said about Emma."
    scene expression ("images/episode1/199.webp") with dissolve
    patricia "Then I'll just go buy one myself."
    scene expression ("images/episode1/200.webp") with dissolve
    charlotte "Don't take it personally. I don't know where I went wrong with her."
    toby "Don't worry [mom]. So? What can I get you?"
    charlotte "Surprise me!"
    scene expression ("images/episode1/201.webp") with dissolve
    toby "I will!"
    scene expression ("images/episode1/202.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI hate the idea that maybe Tris is right, but it hurts when she talks like that about my girlfriend.{/i}"
    scene expression ("images/episode1/203.webp") with dissolve
    patricia "How does it feel?"
    toby "Feel what?"
    patricia "The pain when you realize that your [sister] is always right?"
    toby "Fuck off!"
    scene expression ("images/episode1/204.webp") with dissolve
    barman "That will be $10.50."
    $ progress = 14
    menu:
        "{i}[JGR]pay for her drink{/i}"(csq="Tris +1 & Gallery Image"):
            $ patricia_rel += 1
            $ unlockImage(persistent.patricia_02)
            scene expression ("images/episode1/205.webp") with dissolve
            toby "Allow me!"
            scene expression ("images/episode1/206.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode1/207.webp") with dissolve
            patricia "I knew I could count on you!"
            toby "Yeah, yeah. Whatever!"
            scene expression ("images/episode1/208.webp") with dissolve
            toby "..."
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nDude... She's your [sister]. You can't look at her ass.{/i}"
            scene expression ("images/episode1/209.webp") with dissolve
            barman "Sir?"
            toby "Sorry?"
        "{i}she doesn't deserve it{/i}":
            scene expression ("images/episode1/210.webp") with dissolve
            patricia "Aren't you ashamed to let a lady pay for her own drink?"
            toby "Let me think about that for a bit."
            scene expression ("images/episode1/207.webp") with dissolve
            toby "No. Not at all!"
            scene expression ("images/episode1/209.webp") with dissolve
    barman "What can I get you, sir?"
    toby "Oh, right. Give me your best alcoholic cocktail and the best one with no alcohol in it."
    barman "Sure. Give me a second!"
    scene expression ("images/episode1/211.webp") with dissolve
    toby "Got to be honest. This place is really nice, too bad it's kinda empty. I suppose not a lot of people come to the beach on a Monday."
    barman "First time here?"
    toby "Yeah, I just moved to the city."
    barman "You'll like it here. There are plenty of things to do."
    barman "You should come back to the beach on the weekend. There are plenty of gorgeous ladies here."
    toby "Yeah... I should definitely come by!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI have a gorgeous lady at home, but he doesn't need to know that.{/i}"
    scene expression ("images/episode1/212.webp") with dissolve
    barman "Here you go sir. That will be $25"
    scene expression ("images/episode1/213.webp") with dissolve
    toby "Thanks man!"
    scene expression ("images/episode1/214.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nWhich one should I give [mom]?{/i}"
    menu:
        "{i}[JGR]the one with alcohol in it{/i}"(csq="Charlotte +1"):
            $ charlotte_rel += 1
            $ ep1_get_charlotte_drunk = True
        "{i}the one without alcohol in it{/i}":
            pass
    scene expression ("images/episode1/215.webp") with dissolve
    toby "Here you go [mom]."
    charlotte "Thank you, darling."
    scene expression ("images/episode1/216.webp") with long_dissolve
    patricia "I have an idea!"
    toby "Amaze me!"
    patricia "If you manage to beat me at volleyball, I'll apologize for everything I said about Emma!"
    scene expression ("images/episode1/217.webp") with dissolve
    toby "And you won't say anything bad about her in the future either?"
    toby "Deal."
    scene expression ("images/episode1/218.webp") with dissolve
    patricia "Let's see you try first."
    scene expression ("images/episode1/219.webp") with dissolve
    toby "You asked for it!"
    scene expression ("images/episode1/220.webp") with long_dissolve
    $ progress = 15
    menu:
        "{i}[JGR]let her win{/i}"(csq="Tris +1 & Gallery Image & Important for Tris' path"):
            $ patricia_rel += 1
            $ ep1_let_patricia_win = True
            $ unlockImage(persistent.patricia_03)
            scene expression ("images/episode1/221.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode1/222.webp") with dissolve
            patricia "Sucker!"
            toby "I let you win!"
            scene expression ("images/episode1/223.webp") with dissolve
            patricia "I'm sure... You chicken!"
            toby "That's it!"
        "{i}try to win{/i}":
            scene expression ("images/episode1/221.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode1/224.webp") with dissolve
            patricia "I let you win. I was getting tired of talking about your girlfriend!"
            toby "Yeah, right!"
            scene expression ("images/episode1/225.webp") with dissolve
            patricia "I meant, I was getting tired of talking about your bitch!"
            toby "That's it... You're gonna get it for that!"

    scene expression ("images/episode1/226.webp") with dissolve
    patricia "Help!"
    toby "No one's here except for us!"
    patricia "He's trying to rape me!"
    scene expression ("images/episode1/227_1.webp") with dissolve
    toby "Are you crazy!? What if someone hears you?"
    scene expression ("images/episode1/227_2.webp") with dissolve
    patricia "I thought you said that nobody is here!"
    scene expression ("images/episode1/228.webp") with dissolve
    toby "Chicken much?"
    scene expression ("images/episode1/229.webp") with dissolve
    patricia "Aaaa!"
    scene expression ("images/episode1/230.webp") with dissolve
    toby "So? Let's hear it. Was there something you wanted to say?"
    scene expression ("images/episode1/231.webp") with dissolve
    patricia "What are you going to do to me now?"
    scene expression ("images/episode1/232.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nShit the way she looks at me made me so horny and now I have a boner!{/i}"
    scene expression ("images/episode1/233.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nShe noticed. Fuck, fuck, fuck my life.{/i}"
    if patricia_rel == 3:
        scene expression ("images/episode1/234.webp") with dissolve
        patricia "Are you that attracted to me that you got a boner just from me acting helpless?"
        toby "No!"
        scene expression ("images/episode1/235.webp") with dissolve
        patricia "Oh my God... This is so funny! Haha, sucker!"
        scene expression ("images/episode1/237.webp") with dissolve
        patricia "Tonight, you're sleeping on the floor, you horn dog!"
    else:
        scene expression ("images/episode1/236.webp") with dissolve
        patricia "Ewww. What's wrong with you? I'm your [sister]!"
        toby "Sorry, it's not because of you!"
        patricia "I don't care, get off me!"
        scene expression ("images/episode1/238.webp") with dissolve
        patricia "Tonight you're sleeping on the floor."
    scene expression ("images/episode1/239.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nReally? Are you going to do me like that?{/i}"
    scene expression ("images/episode1/240.webp") with long_dissolve
    toby "Do you need help with that?"
    $ progress = 16
    if charlotte_rel < 2:
        charlotte "Don't worry. I can do it myself!"
        toby "As you wish!"
        pass
    else:

        scene expression ("images/episode1/241.webp") with dissolve
        charlotte "How can I say no to you?"
        scene expression ("images/episode1/242.webp") with dissolve
        toby "Want some too after?"
        scene expression ("images/episode1/243.webp") with dissolve
        patricia "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}{i}\nYou're too horny right now. Maybe some other time.{/i}"
        scene expression ("images/episode1/244.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode1/245.webp") with dissolve
        charlotte "What did she say?"
        toby "Something like she doesn't deserve any sunscreen because she lost at volleyball!"
        scene expression ("images/episode1/246.webp") with dissolve
        if ep1_let_patricia_win == True:
            patricia "Idiot."
        else:
            patricia "I said that I don't even deserve to go home with you in the same car."
            toby "Don't worry, I'll close an eye this time!"

        label memory_02:

            if _in_replay:

                $ ep1_get_charlotte_drunk=True

            scene expression ("images/episode1/247.webp") with dissolve
            charlotte "If neither of those two ladies hire you, I think you'd do pretty well as a masseur."
            toby "And I'm just applying sunscreen. Imagine if I was really giving you a massage."
            scene expression ("images/episode1/248.webp") with dissolve
            charlotte "Well, since we're broke, I think I'll let you massage my back one day."
            toby "Does your back still hurt?"
            charlotte "Sometimes, after standing too much."
            if ep1_get_charlotte_drunk == False:
                scene expression ("images/episode1/249.webp") with dissolve
                charlotte "Thank you for the sunscreen!"
                toby "No problem [mom]."
            else:
                scene expression ("images/episode1/250.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nWhat is [mom] doing?{/i}"
                charlotte "I don't want any tan lines!"
                scene expression ("images/episode1/251.webp") with dissolve
                toby "Yeah, sure [mom]!"
                scene expression ("images/episode1/252.webp") with dissolve
                charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}{i}\nMake sure you don't miss a spot!{/i}"
                scene expression ("images/episode1/253.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nIs she serious right now?{/i}"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nHer ass is huge!{/i}"
                scene expression ("images/episode1/254.webp") with dissolve
                charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}{i}\nGood boy.{/i}"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI'm not sure what was in that cocktail, but I think was really strong.{/i}"
                scene expression ("images/episode1/255.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI feel kinda dirty and aroused at the same time. I'm touching my [mom]'s firm ass.{/i}"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nThis is not what I was thought was going to happen at the beach.{/i}"
                menu:
                    "{i}[JGR]go forward{/i}"(csq="Charlotte +1 & Gallery Image"):
                        $ charlotte_rel += 1
                        $ ep1_groping_charlotte = True
                        $ unlockImage(persistent.charlotte_03)
                        scene expression ("images/episode1/256.webp") with dissolve
                        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nWhat the hell... You only live once.{/i}"
                        scene expression ("images/episode1/257.webp") with dissolve
                        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI'm touching my [mom]'s breast!{/i}"
                        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nAnd it doesn't seem like she's bothered by that.{/i}"
                        scene expression ("images/episode1/258.webp") with dissolve
                        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nOkay... I know where this is going.{/i}"
                        scene expression ("images/episode1/259.webp") with dissolve
                        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI can't believe how big and soft her boobs are.{/i}"
                        charlotte "{size=12}{color=#FDCA6E}* moaning slightly *{/color}{/size}\n{i}Mhmmm.{/i}"
                        scene expression ("images/episode1/260.webp") with dissolve
                        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI should stop before Tris turns over.{/i}"
                    "{i}stop{/i}" if not _in_replay:
                        pass
                scene expression ("images/episode1/261.webp") with dissolve
                charlotte "Thank you honey!"
                toby "No problem [mom]."
                $ unlockMemory(persistent.memory_02)

            $ renpy.end_replay()

    scene expression ("images/episode1/262.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nWhat a day. I feel like this city has had a big impact on me.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nAnyway, I wonder which job I should choose tomorrow.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nOn one hand having a more stable income would be great and on top of that I'll have a career.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nBut Katrina's words keep popping in my head. She did promise me plenty of money. But at what cost?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI mean, look at [dad], when his business was good he behaved differently than now. So it's safe to say that my job will have an impact on my attiude.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nWhat if after spending so much time in the club, with whores and drunk ladies I'll start to treat the girls at home the same way or even Emma.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}{i}\nI'm not sure what to choose. I mean, both jobs look promising enough. I'll figure it out tomorrow.{/i}"
    $ progress = 17
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
