label EP18_Begin:
    stop music
    show text "{size=+20}Press Space{/size}"
    pause
    play music chill_song_2
    play sound undress
    $ EP18_var_1 = True
    if bar_var_1 == True:
        scene 47-9 barscene 254 with Dissolve(0.5)
        a "Who knows..."
        a "He can be a little unpredictable, that's for sure."
        e "I don't know him well enough."
        a "One thing's for sure, it will be something rather exciting..."
        scene 47-9 barscene 255 with Dissolve(0.5)
        e "Besides him taking a cut."
        e "We do all the work."
        a "True, but without him, we wouldn't have a platform."
        e "Meaning?"
        a "Without Patrick, our other option would be working the corner."
        a "And we both know we wouldn't be doing that."
        e "Haha. True."
        a "Let's go."
    else:
        scene 47-9 barscene 254 with Dissolve(0.5)
        a "It's mostly Jim."
        a "I don't have time for planning."
        a "But I certainly find the job intriguing."
        e "So do I. Heh. I wonder how much money we made tonight, though."
        a "That's a good question."
        a "We'll get back to it tomorrow."
        e "Ok."
        scene 47-9 barscene 255 with Dissolve(0.5)
        e "I wouldn't say no to a side hustle like this."
        e "Get paid for having fun?"
        e "What's not to like?"
        a "True, haha."
    play sound door2
    scene 47-9 barscene 255_0 with Dissolve(0.5)
    ga "Hey, girls!"
    ga "Productive night, eh?"
    a "Hah, you bet!"
    ga "I'm sure we earned a pretty penny."
    a "Indeed we did."
    scene 47-9 barscene 256 with Dissolve(0.5)
    a "We couldn't do our job properly without a guard."
    a "Making sure nobody gets too handsy or rough."
    ga "My main priority, girls."
    ga "Won't let anything happen to you on my watch."
    scene 47-9 barscene 257 with Dissolve(0.5)
    j3 "Good job, girls."
    if bar_var_1 == True:
        j3 "Patrick will count the money and tell us tomorrow."
    else:
        j3 "I'll get to counting money later, will give you the numbers tomorrow."
    a "Better not skimp on anything."
    j3 "You'll get your dues, that I'm sure of."
    scene 47-9 barscene 258 with Dissolve(0.5)
    e "So what now?"
    e "We going partying?"
    a "This late?"
    e "Why not?"
    a "I'm spent, Emily."
    a "I want to get some sleep asap."
    e "Fiiine. I'll just do the same."
    scene black with Dissolve(0.5)
    pause 1
label EP18_Morning:
    $ EP18_var_2 = True
    stop music
    play sound interface_sound
    show text "Saturday Morning..." with Dissolve(0.5)
    pause 2
    play music tranquility
    scene 48-1 morning 1 with Dissolve(0.5)
    if bar_var_1 == True:
        a "{i}...I wonder what Patrick has planned for today...{/i}"
        a "{i}...Things keep heating up at the bar...{/i}"
    else:
        a "{i}...I wonder how we could pump up the action more...{/i}"
        a "{i}...Making that business more lucrative is not a bad thing...{/i}"
        a "{i}...Perhaps I could even involve more and more girls...{/i}"
    scene 48-1 morning 2 with Dissolve(0.5)
    a1 "Hey... Anna."
    a1 "A dream come true for a man. Seeing such a beautiful woman as I wake up..."
    a1 "Wow."
    scene 48-1 morning 3 with Dissolve(0.5)
    a "Heh. You're making me blush, Andrew."
    a1 "Everything for you, Anna."
    a "Everything?"
    a1 "Whatever you say, goes."
    scene 48-1 morning 4 with Dissolve(0.5)
    a1 "You sleep well?"
    a "Yeah."
    a "Can't complain."
    scene 48-1 morning 5 with Dissolve(0.5)
    a1 "It's finally weekend."
    a1 "And you're free."
    a1 "I thought that, perhaps, we could do some things together today?"
    a1 "It's been a while since we've done something, just the two of us."
    scene 48-1 morning 6 with Dissolve(0.5)
    a "Oh?"
    a "Got anything particular in mind?"
    a1 "Eh. No. Hadn't gotten that far. Haha."
    play sound undress
    scene 48-1 morning 7 with Dissolve(0.5)
    a "Hmm..."
    a1 "Well, I haven't been to the beach for a while."
    a1 "Or the pool or something, we could do that?"
    a "I like the idea."
    scene 48-1 morning 8 with Dissolve(0.5)
    a1 "Nice!"
    a1 "It's settled then."
    a "Alright, heh."
    scene 48-1 morning 9 with Dissolve(0.5)
    a "But I'd first like to eat some breakfast."
    a "Didn't eat anything yesterday in the evening..."
    scene 48-1 morning 10 with Dissolve(0.5)
    a1 "I agree. Pretty hungry."
    a1 "How about we eat outside?"
    a1 "Find a nice cafe and indulge a little?"
    a "Great idea, Andrew!"
    a "Let's go."
    scene black with Dissolve(0.5)
    pause 1
    play sound door2
    scene 48-1 morning 12 with Dissolve(0.5)
    a1 "Got any ideas where we could go?"
    a "Not really."
    a1 "Hmm... I think I might know a place."
    a "Nice."
    scene 48-1 morning 13 with Dissolve(0.5)
    j4 "Morning, sleepyheads."
    a1 "Hey, dad."
    a "Morning, John."
    j4 "I'm cooking some food."
    scene 48-1 morning 14 with Dissolve(0.5)
    j4 "Want some?"
    j4 "Making enchiladas."
    j4 "And a bit of whiskey, hehe."
    a1 "We're good. Thanks."
    scene 48-1 morning 15 with Dissolve(0.5)
    a1 "Why you gotta be half naked, though?"
    a "Heh. It's alright..."
    scene 48-1 morning 16 with Dissolve(0.5)
    j4 "What, jealous of my physique?"
    a1 "Yeah. Right..."
    a "We'll head out, eat at a cafe or something."
    j4 "Your loss."
    j4 "Where you going?"
    a "To the cafe first, then to the beach."
    j4 "Can I join you later?"
    a1 "Sorry. No. We want to spend some time together, just the two of us."
    j4 "Oh... Ok..."
    scene 48-1 morning 17 with Dissolve(0.5)
    a1 "For some reason, he continues to be an asshole."
    a1 "Hate it."
    a "Don't worry about it."
    a1 "Whatever..."
    j4 "{i}...Perhaps I can still join Anna later...{/i}"
    play sound door2
    scene black with Dissolve(0.5)
    pause 1
    play ambient citytraffic
    scene 48-1 morning 18 with Dissolve(0.5)
    a1 "The place isn't far."
    a1 "I think I've been there a few times."
    a "Anything good?"
    a1 "Well. Cheesecake is good."
    a "Oh, yummy."
    scene 48-1 morning 19 with Dissolve(0.5)
    a1 "Not as yummy as you, Anna."
    a "Oh, Andrew."
    a "Hehe."
    a1 "I mean it. so beautiful."
    scene black with Dissolve(0.5)
    pause 1
    play sound door2
    scene 48-1 morning 20 with Dissolve(0.5)
    a "Hmm. I've been here, too."
    a1 "Really?"
    a1 "And?"
    a "It's a nice place, indeed."
    a "A cute waitress. You'd like her."
    scene 48-1 morning 21 with Dissolve(0.5)
    a1 "Hi."
    a1 "What's your breakfast offer?"
    barista "Cheese sandwiches and coffee."
    barista "Will that do?"
    scene 48-1 morning 22 with Dissolve(0.5)
    a1 "Um. Sure."
    a1 "No cheesecake?"
    barista "Unfortunately, no."
    barista "They could't deliver it today..."
    barista "Sorry."
    a1 "It's ok."
    scene 48-1 morning 23 with Dissolve(0.5)
    a1 "We'll manage, right Anna?"
    a "Heh. Yeah. It's ok."
    a "Lovely day, isn't it?"
    barista "Couldn't agree more."
    a "Perfect for a trip to the beach."
    barista "Yeah..."
    a "{i}...Hehe, should tease Andrew a bit...{/i}"
    a "Care to join?"
    barista "Umm... That sounds fun, but I have to see if I can make it..."
    barista "If I can, I'll surely go."
    a "We'll keep our eyes and ears open."
    barista "Ok, heh."
    scene 48-1 morning 24 with Dissolve(0.5)
    barista "Alright. Here are the sandwiches."
    barista "And the coffee."
    a "Mmm... The coffee smells so good."
    barista "Only the best at our cafe."
    scene 48-1 morning 25 with Dissolve(0.5)
    barista "That will be 8.50$."
    a1 "Here. Let me pay for it."
    scene 48-1 morning 26 with Dissolve(0.5)
    barista "Thank you. Enjoy your meal!"
    a1 "Thanks!"
    scene 48-1 morning 27 with Dissolve(0.5)
    a "So. what did you think about the waitress?"
    a "Wasn't she attractive?"
    scene 48-1 morning 28 with Dissolve(0.5)
    a1 "Oh? This feels like a trap."
    a "It isn't, so don't worry. I'm not that jealous type of a girlfriend."
    a1 "Well. Yeah. She was cute."
    a "Heh, indeed."
    scene 48-1 morning 29 with Dissolve(0.5)
    a1 "But. I'd never choose her over you."
    a "Are you sure?"
    a1 "Yeah. You're perfection."
    scene 48-1 morning 30 with Dissolve(0.5)
    a "Ah so tasty..."
    a "I do wonder."
    a1 "What about?"
    scene 48-1 morning 31 with Dissolve(0.5)
    a "If she joined us at the beach."
    a "Hypothetically, of course..."
    a "It would be funny if we, the three of us, did some stuff."
    a "You know?"
    a1 "Meaning?"
    a "You know. menage a troi."
    a1 "Like the three of us?"
    a "Hehe... It would be interesting."
    scene 48-1 morning 29 with Dissolve(0.5)
    a1 "I... Um... I mean. Yeah."
    a1 "Heh... Only if it was ok with you."
    a "It would be heh."
    a "I bet you'd like it."
    scene 48-1 morning 31 with Dissolve(0.5)
    a "Even if you find only me perfect."
    a1 "I uhh..."
    a "Haha. I'm just messing around, Andrew."
    a1 "Right. heh."
    a "Anyway. I'm all done. Let's go?"
    a1 "Yeah."
    scene 48-1 morning 32 with Dissolve(0.5)
    a "Thank you for the coffee and sandwiches."
    a "They never fail us."
    scene 48-1 morning 33 with Dissolve(0.5)
    barista "You're welcome!"
    a "See you later then, maybe?"
    barista "Maybe..."
    scene 48-1 morning 34 with Dissolve(0.5)
    a1 "So. The beach now?"
    a "Oh yes!"
    a "Can't wait. I want that sun on my skin!"
    a1 "I want a cold beer!"
    a "Same."
    scene black with Dissolve(0.5)
    pause 1
label EP18_Beach_1:
    $ EP18_var_3 = True
    play music Chill_Song_1
    stop ambient
    scene 48-2 beach 1 with Dissolve(0.5)
    a1 "Wow."
    a "Yeah."
    a1 "To be honest. I've never been here."
    a "Really?"
    a "Make a wish, hehe."
    a1 "It alread came true."
    a1 "Being here with you."
    scene 48-2 beach 2 with Dissolve(0.5)
    a1 "Let's go grab a drink then?"
    a1 "I really want that beer."
    scene 48-2 beach 3 with Dissolve(0.5)
    a "First, Let's go get changed."
    a "I want to get into my bikini as soon as possible."
    a "And I'm pretty sure you'll like it hehe."
    a1 "Interesting..."
    scene 48-2 beach 4 with Dissolve(0.5)
    a1 "You come here often?"
    a "Not often, but I do."
    a "Usually a lot of people here."
    scene 48-2 beach 5 with Dissolve(0.5)
    a "Sometimes I've been here with Rebecca."
    a1 "Oh."
    a "No better place to be on a sunny day."
    scene 48-2 beach 6 with Dissolve(0.5)
    a "I'll 'accidentaly' leave the door open."
    a1 "In public?"
    a "Got a problem with that?"
    a "And not like I'm walking nude in the city center."
    scene 48-2 beach 7 with Dissolve(0.5)
    a1 "Fair point."
    a "Besides, I thought you liked seeing me."
    a1 "I do indeed."
    a "Then, shush and enjoy."
    play sound jacketcloth
    scene 48-2 beach 8 with Dissolve(0.5)
    a "Mm..."
    a "You like my curves?"
    a1 "Whaaaa..."
    scene 48-2 beach 9 with Dissolve(0.5)
    a1 "DAMN!"
    a1 "So hot, Anna!"
    scene 48-2 beach 10 with Dissolve(0.5)
    a "What's that?"
    a "I can't hear you behind that huge ass. Hehe."
    a1 "Haha."
    scene 48-2 beach 11 with Dissolve(0.5)
    a1 "A queen if I ever saw one."
    a "That's right!"
    a "And you better not forget it."
    a1 "I wont!"
    play sound undress
    scene 48-2 beach 12 with Dissolve(0.5)
    a1 "What?"
    a1 "Whoa."
    a "Hm?"
    scene 48-2 beach 13 with Dissolve(0.5)
    a1 "Wooow."
    a1 "Umm..."
    a1 "That's... Like. Not a lot of coverage."
    scene 48-2 beach 14 with Dissolve(0.5)
    a "What?"
    a "Everyone at the beach wears minimal clothing."
    a1 "There's minimal and then there's this."
    a1 "You sure this is what you want to wear?"
    a "Yeah, why not? Don't like it?"
    play sound whoosh
    scene 48-2 beach 15-1 with flash:
        yalign 1
        linear 8 yalign 0.0
    pause 8
    scene 48-2 beach 15 with Dissolve(0.5)
    a1 "I do, but... It just barely covers anything..."
    a "Oh c'mon, Andrew. It's just the beach."
    a "Not like I'm walking down main street in this."
    scene 48-2 beach 16-1 with Dissolve(0.5)
    a1 "Holy..."
    a1 "Such a hot body."
    scene 48-2 beach 16 with Dissolve(0.5)
    a "Go get changed."
    a "I really want to get some nice tan today."
    a1 "Uhh... Sure."
    scene 48-2 beach 17 with Dissolve(0.5)
    a1 "I just hope everyone won't stare at you."
    a "And even if they will, so what?"
    a "You know they can't get me."
    a "They'll just get jealous. But you'll be the one taking me home."
    a1 "Heh. True."
    scene 48-2 beach 18 with Dissolve(0.5)
    a "Hurry up."
    scene 48-2 beach 19 with Dissolve(0.5)
    a1 "All done."
    a1 "Let's go."
    a "Yes, yes, yes. Hehe."
    scene black with Dissolve(0.5)
    pause 1
    scene 48-2 beach 20 with Dissolve(0.5)
    a "Hey!"
    barten "Hello, Anna!"
    barten "Back again, I see."
    a "Of course. Whenever I got some free time, I come here."
    scene 48-2 beach 21 with Dissolve(0.5)
    barten "I've noticed."
    a "Not a lot of people I see."
    barten "Still early morning."
    barten "People will show up."
    a "True."
    scene 48-2 beach 22 with Dissolve(0.5)
    barten "Remember last time you were here."
    barten "Had a great volleybal game, ye?"
    a "Oh the best. Hehe."
    barten "Indeed."
    scene 48-2 beach 23 with Dissolve(0.5)
    a "The stakes were high."
    barten "Oh I saw."
    scene 48-2 beach 24 with Dissolve(0.5)
    a1 "{i}...He's staring at her...{/i}"
    a1 "{i}...I knew I was right... But... Anna insists...{/i}"
    a1 "{i}...I suppose she's right, though... People stare but only I take her home...{/i}"
    scene 48-2 beach 25 with Dissolve(0.5)
    barten "So where's Rebecca?"
    a "Oh. She's pretty busy with... Stuff."
    barten "Aren't we all."
    barten "Alright, what'll you have today?"
    a "Just two beers, thanks."
    barten "Coming right up."
    scene 48-2 beach 26 with Dissolve(0.5)
    barten "Anyway, hope you've enjoy your day here today."
    a "I certainly will."
    a "Finaly here with my boyfriend."
    barten "Great!"
    scene 48-2 beach 27 with Dissolve(0.5)
    a1 "I was right, people are staring..."
    a "So?"
    a "It's not that big of a deal, Andrew."
    a "Quit making it so."
    a1 "Alright, alright."
    scene 48-2 beach 28 with Dissolve(0.5)
    a1 "Perfect, two chairs for us. No one has taken them."
    a "Yeah. Looks like luck is on our side."
    a1 "Hah."
    scene 48-2 beach 29 with Dissolve(0.5)
    pause 1
    scene 48-2 beach 30 with Dissolve(0.5)
    beachguy1 "Damn..."
    beachguy1 "It's that girl."
    beachguy2 "Yeah,the same one from some days ago."
    scene 48-2 beach 31 with Dissolve(0.5)
    beachguy2 "She's such a badie. Look at those tits."
    beachguy1 "Her outfit barely covers anything at all..."
    beachguy2 "What I wouldn't do... Damn..."
    scene 48-2 beach 32-1 with Dissolve(0.5)
    beachguy2 "Def would tap that ass more than once."
    beachguy1 "We'd double team her, hehe."
    beachguy2 "Call in the rest of the guys, and give her a good one."
    scene 48-2 beach 32-2 with Dissolve(0.5)
    a "{i}...Very vulgar comments...{/i}"
    a "{i}...I wonder what Andrew thinks about those comments...{/i}"
    scene 48-2 beach 32 with Dissolve(0.5)
    a1 "{i}...Fuckers talking like that about Anna...{/i}"
    a1 "{i}...But I don't want a fight...{/i}"
    a1 "{i}...But... They are right... She is kinda slutty in this outfit...{/i}"
    scene 48-2 beach 33 with Dissolve(0.5)
    a1 "Alright."
    a1 "I kinda wanna lay down and enjoy the sun, too."
    a "Hehe. Good to hear."
    scene 48-2 beach 34 with Dissolve(0.5)
    a1 "But I gotta say, I heard the way the talked..."
    a1 "I'm not sure how to feel."
    a "What, you gonna take what everyone says serious?"
    a "They don't matter."
    a1 "Eh, sure."
    scene 48-2 beach 35 with Dissolve(0.5)
    a "Besides, you men look at every girl that has curves."
    a "What am I supposed to do? Just not exist?"
    a1 "You're right, Anna. You're always right."
    play sound drinkingBeverage
    scene 48-2 beach 36 with Dissolve(0.5)
    a1 "Mmm!"
    a1 "So fucking good."
    play sound drinkingBeverage
    scene 48-2 beach 37 with Dissolve(0.5)
    a "Oh."
    a "You're right!"
    scene 48-2 beach 38 with Dissolve(0.5)
    a1 "So. How's work, and everything else?"
    a1 "You know... The Carl situation?"
    a "Oh that..."
    a "Well, there have been developements."
    a "It's complicated."
    a "I don't really want to talk about it."
    a "I'd rather lay down and rest."
    scene 48-2 beach 39 with Dissolve(0.5)
    a "Ahh.."
    a "Soo goood."
    a1 "Overheard the bartender talk about volleyball."
    a "Oh, yeah."
    a1 "What's that all about?"
    scene 48-2 beach 40 with Dissolve(0.5)
    a "Oh. You know."
    a "Some friends and I came here to play volleyball."
    a "That's all."
    a1 "I know them?"
    a "People from work."
    a1 "I see."
    a "Hey, you mind if I uncover my breasts?"
    scene 48-2 beach 41 with Dissolve(0.5)
    a1 "There's not much covering them to begin with, but..."
    a1 "Still. What if someone sees?"
    a "C'mon, Andrew."
    scene 48-2 beach 42 with Dissolve(0.5)
    a "No one will see. We're facing away from people."
    a "Besides, I need to tan my breasts."
    a "I want to look good for you."
    scene 48-2 beach 43 with Dissolve(0.5)
    a1 "Eh. Sure."
    a1 "Not like I can do much to stop you."
    a "You can, just say no."
    a "But I know you wont."
    a "You wanna see my luscious breasts, Andrew."
    play sound undress
    scene 48-2 beach 44 with Dissolve(0.5)
    a "See."
    a "It's all good."
    a "The world didn't collapse just because I revealed my breasts."
    a1 "Oh I don't know... Anything can happen."
    scene 48-2 beach 45 with Dissolve(0.5)
    a1 "But I cannot deny how sexy you are, Anna."
    a "You're definitely a lucky, Andrew."
    a1 "Oh yeah! I tell myself that everyday."
    a "Hehe."
    scene 48-2 beach 46 with Dissolve(0.5)
    a "Ah. This is nice."
    a "Perhaps I should get a beach side property so I could do this everyday after I get home."
    a "Just imagine a house with a view of the sea."
    a "Wow..."
    scene 48-2 beach 47 with Dissolve(0.5)
    a1 "Hah, yeah."
    a1 "I'll be realistic. I don't see myself being able to afford it."
    a1 "At least not in the forseeable future."
    a "You never know."
    scene 48-2 beach 48 with Dissolve(0.5)
    a1 "Jeez."
    a1 "I feel kinda dizzy..."
    a1 "And... sleepy..."
    a1 "Fuck, maybe the medicine and the alcohol don't mix..."
    a "Andrew? You ok?"
    a1 "AAahhh... Yeah. Just..."
    scene 48-2 beach 49 with Dissolve(0.5)
    a1 "I'll... Take a little nap. Ok?"
    a "Sure, just relax."
    a "No rush today."
    a1 "Ah..."
    scene 48-2 beach 50 with Dissolve(0.5)
    a "That's unexpected."
    a "Didn't know the medicine would do that."
    a "Well... I'll just relax in silence."
    a "Nothing wrong with that."
    scene 48-2 beach 51 with Dissolve(0.5)
    a "I'm out of beer, though..."
    a "And Andrew's asleep."
    a "Perhaps I should..."
    scene 48-2 beach 52 with Dissolve(0.5)
    a "Yoohoo?"
    a "Come over here?"
    beachguy1 "Wait, what?"
    scene 48-2 beach 53 with Dissolve(0.5)
    beachguy2 "She's calling us over, let's go dude."
    beachguy1 "For real?"
    beachguy2 "Haha, that's interesting. Let's go check it out."
    scene 48-2 beach 54 with Dissolve(0.5)
    a "I'll just ask them."
    a "Don't want to pester Andrew. He still needs his rest."
    scene 48-2 beach 55 with Dissolve(0.5)
    pause 1
    scene 48-2 beach 57 with Dissolve(0.5)
    beachguy1 "Yes?"
    beachguy1 "{i}...Holy fuck... Her tits are bare...{/i}"
    beachguy1 "What does such a wonderful lady like you want?"
    scene 48-2 beach 56 with Dissolve(0.5)
    a "Oh. heh. Hey. I just drank all of my beer..."
    a "And I need a new one."
    a "Heh. I really went through it fast."
    scene 48-2 beach 58 with Dissolve(0.5)
    a "As you can see, my boyfriend is asleep..."
    a "And I don't want to wake him."
    a "I don't want to walk around half naked like this and a bit too lazy to do it myself."
    a "Soo..."
    a "Perhaps I could ask you guys?"
    scene 48-2 beach 59 with Dissolve(0.5)
    beachguy2 "Sure. That can be arranged."
    a "Oh you're so nice. Thank you."
    beachguy2 "I'll be right back."
    scene 48-2 beach 60 with Dissolve(0.5)
    a "Thank you!"
    scene 48-2 beach 61 with Dissolve(0.5)
    a "Oh, that reminds me."
    a "I really need someone to wipe some sunscreen on me."
    a "My boyfriend would do it..."
    a "But as you can see, he's not exactly capable."
    a "Would you mind?"
    scene 48-2 beach 62 with Dissolve(0.5)
    beachguy1 "Oh I don't mind at all."
    beachguy1 "What ever you need."
    a "Good, hehe."
    scene 48-2 beach 63 with Dissolve(0.5)
    beachguy1 "You're the volleyball girl right?"
    a "What do you mean?"
    beachguy1 "I saw you playing volleyball with some young dudes here before."
    a "Oh, hehe... Yes."
    beachguy1 "Things got pretty interesting towards the end."
    a "They sure did."
    scene 48-2 beach 64 with Dissolve(0.5)
    beachguy1 "You sure your boyfriend doesn't mind?"
    a "Well, he's asleep. I don't see a problem with someone else helping out meanwhile."
    a "You know?"
    beachguy1 "Hehe. Sure."
    scene 48-2 beach 65 with Dissolve(0.5)
    a "I mean, we aren't exactly doing anything bad, are we?"
    beachguy1 "Absolutely not."
    a "You're just a nice man helping out someone in need."
    a "That's all."
    beachguy1 "True."
    scene 48-2 beach 66 with Dissolve(0.5)
    a1 "Ahh... Wha."
    a1 "{i}...What the... Is this a dream...{/i}"
    a1 "{i}...I'm so confused right now...{/i}"
    scene 48-2 beach 67 with Dissolve(0.5)
    a1 "{i}...Some dude massaging Anna...{/i}"
    a1 "{i}...Damn, that medicine and alcohol definitely doesn't mix...{/i}"
    a1 "{i}...I'm... Whoa... So confused...{/i}"
    scene 48-2 beach 68 with Dissolve(0.5)
    a1 "{i}...That's... Weird... I don't think some random should touch Anna like that...{/i}"
    a1 "{i}..C'mon Andrew... Don't complicate it... It's not that big of a deal...{/i}"
    a1 "{i}...He's just... Doing something to her... Putting on sunscreen...{/i}"
    a1 "{i}...Perhaps I'm just seeing things...{/i}"
    scene 48-2 beach 69 with Dissolve(0.5)
    beachguy2 "Well. I'm back."
    beachguy2 "Got the beer, as requested."
    a "Hehe, great!"
    a1 "Thank you!"
    scene 48-2 beach 70 with Dissolve(0.5)
    beachguy2 "You're very welcome."
    a "I'm Anna."
    beachguy2 "Awesome."
    scene 48-2 beach 71 with Dissolve(0.5)
    beachguy2 "You know..."
    beachguy2 "I think I deserve a little 'reward' for bringing you beer."
    beachguy2 "Don't you think?"
    a "Oh. hehe... Well you've both been rather helpful."
    scene 48-2 beach 72 with Dissolve(0.5)
    a "Would be callous of me not to say thanks in some way, now would it."
    beachguy1 "Correct, hehe."
    scene 48-2 beach 73 with Dissolve(0.5)
    a1 "{i}... Whaaat?{/i}"
    a1 "{i}...I definitely must be dreaming...{/i}"
    a1 "{i}...Anna isn't that naughty... Is she?...{/i}"
    scene 48-2 beach 74 with Dissolve(0.5)
    a "How about you help me take off this micro bikini."
    a "I was going to lose it anyway."
    beachguy1 "Hehe. Of course!"
    play sound undress
    scene 48-2 beach 75 with Dissolve(0.5)
    pause 1
    scene 48-2 beach 76 with Dissolve(0.5)
    beachguy1 "There."
    beachguy1 "That should make it easier for you to get a good tan."
    a "You're absolutely right."
    beachguy2 "Wow!"
    beachguy1 "Yeah!"
    scene 48-2 beach 77 with Dissolve(0.5)
    a1 "{i}...Wait... I'm... Not dreaming...{/i}"
    a1 "{i}...She's actually being undressed by some strangers...{/i}"
    a1 "{i}...There must be a good reason for that, totally...{/i}"
    scene 48-2 beach 78 with Dissolve(0.5)
    a1 "{i}...You can almost see her pussy...{/i}"
    a1 "{i}...That's... Is that a good thing to do...{/i}"
    a1 "{i}...It's Anna, she knows what she's doing, though...{/i}"
    scene 48-2 beach 79 with Dissolve(0.5)
    a "How's that for a reward?"
    beachguy2 "Absolutely perfect!"
    a "I knew you'd like it, hehe."
    scene 48-2 beach 80 with Dissolve(0.5)
    a "Thank you for the help!"
    beachguy2 "No problem at all."
    beachguy2 "Any time you need some help."
    beachguy2 "If we're here. We'll help!"
    a "Thanks!"
    scene 48-2 beach 81 with Dissolve(0.5)
    a1 "What's going on?"
    scene 48-2 beach 82 with Dissolve(0.5)
    a "Oh, you're awake. heh."
    a1 "What you all doing?"
    scene 48-2 beach 83 with Dissolve(0.5)
    beachguy1 "Uhh... Nothing much."
    beachguy1 "You just fell asleep."
    beachguy1 "Anna here needed some help with some stuff."
    beachguy1 "We just helped out, that's all."
    scene 48-2 beach 84 with Dissolve(0.5)
    a "Thank you again, heh."
    beachguy1 "We'll leave you to it."
    a "Heh."
    scene 48-2 beach 85 with Dissolve(0.5)
    beachguy2 "See you around."
    a "Cheers!"
    scene 48-2 beach 86 with Dissolve(0.5)
    a1 "Anna?"
    a1 "What was that all about?"
    a1 "They saw you naked?"
    a "Oh, Andrew."
    a "Not like people haven't seen titties before."
    a1 "I'm not even talking about that. Your pussy."
    a "C'mon. They didn't see it. It was all behind my big ass."
    $ persistent.scene_54 = True
    label EP18_Andrew_Sex_Scene_Label_Gallery:
    $ renpy.music.play("audio/sounds/Chill_Song_1.mp3", channel = 'music', if_changed = True)
    scene 48-2 beach 87 with Dissolve(0.5)
    a1 "But..."
    a "What. Lost your tongue?"
    a1 "Whaa..."
    a "You like what you're seeing?"
    scene 48-2 beach 88 with Dissolve(0.5)
    a1 "Yeah..."
    a1 "But."
    a "But what?"
    a "Want me to cover up now?"
    a1 "I... No..."
    a "Hehe."
    scene 48-2 beach 89 with Dissolve(0.5)
    beachguy2 "Dude, that girl's a freak!"
    beachguy1 "Right?"
    beachguy1 "Let's hope she comes here again."
    beachguy1 "We could def talk her into some freaky shit."
    scene 48-2 beach 90 with Dissolve(0.5)
    a "Just say the word and I'll cover up."
    a1 "I..."
    a "I know you won't cause you like seeing my sexy body."
    scene 48-2 beach 91 with Dissolve(0.5)
    a "Oh..."
    a "You like when touch myself like this?"
    a1 "Ummm..."
    a1 "It's..."
    scene 48-2 beach 92 with Dissolve(0.5)
    a1 "I just think..."
    a1 "It's inappropriate to do it..."
    a1 "Um..."
    a1 "I forgot what I was saying."
    scene 48-2 beach 93 with Dissolve(0.5)
    a "Exactly. Cause it's not important."
    a1 "WOOOW!"
    a "You know you like what you saw. Now and before, right?"
    a1 "I... I don't think so..."
    a "You sure?"
    a1 "Yeah..."
    scene 48-2 beach 94 with Dissolve(0.5)
    a "Then why is your cock hard?"
    a "You have to admit, maybe just a little part of you liked what you saw before."
    a "Someone massaging my body."
    scene 48-2 beach 95 with Dissolve(0.5)
    a1 "Umm..."
    a1 "I'm not sure..."
    a "Hehe..."
    a "That's ok..."
    play sound undress
    scene 48-2 beach 96 with Dissolve(0.5)
    a "I can help you with your 'problem.'"
    a1 "oooOOOHHHH."
    a "Yeah?"
    a1 "OH, Anna!"
    show EP18_Andrew_Anim_1 with Dissolve(0.5)
    pause
    a1 "Ah..."
    pause
    show EP18_Andrew_Anim_2 with Dissolve(0.5)
    hide EP18_Andrew_Anim_1
    pause
    a "Yeah. You like this stroking?"
    a1 "Yeah... Fuck..."
    a "Ah."
    scene 48-2 beach 97 with Dissolve(0.5)
    hide EP18_Andrew_Anim_2
    a1 "This is... Not... A good idea."
    a "What?"
    a "Are you seriously saying you don't want me to touch you like this?"
    a1 "I..."
    a "Now or never."
    a1 "Fuuckk..."
    scene 48-2 beach 98 with Dissolve(0.5)
    a "MMm... This whole ordeal is making me wet!"
    a1 "WHAAA?!"
    a1 "WOW!"
    a "Yeah... I bet you want that cock inside me."
    scene 48-2 beach 99 with Dissolve(0.5)
    a "Ohh... So hot..."
    a "Don't you agree?"
    a "{i}...When people look at me like this...{/i}"
    scene 48-2 beach 99-1 with Dissolve(0.5)
    beachguy1 "Dammnn..."
    beachguy2 "I don't think I've ever seen something like this at the beach."
    beachguy1 "Yeah. Crazy!"
    show EP18_Andrew_Anim_3 with Dissolve(0.5)
    a "Mmm..."
    a "{i}...So hot...{/i}"
    a "{i}...They're just staring at me...{/i}"
    a "{i}...Dirty men... Hehe...{/i}"
    scene 48-2 beach 100 with Dissolve(0.5)
    hide EP18_Andrew_Anim_3
    a1 "Oh... Anna..."
    a1 "Your hands are so soft on my cock."
    a1 "Like silk."
    a "Hehe... Hold on just a moment."
    a1 "I can barely do it..."
    play sound cloth_sound1
    scene 48-2 beach 101 with Dissolve(0.5)
    a1 "OOHOHHH!"
    a "You like that, yeah?"
    a1 "YES!"
    a1 "SO HOT!"
    $ different_choice_menu = True
    $ EP18_Anim_Option = 1
    $ EP18_Anim_Speed = 1
    scene black
    play sound jerk loop
    show EP18_Andrew_Anim_4 with Dissolve(0.5)
    label EP18_Andrew_Sex_Label_1:
    a1 "OH shit!"
    a1 "Your tits are so hot!"
    a "Hmmph..."
    menu EP18_Andrew_Anim_Menu_1:
        "View 1":
            hide EP18_Andrew_Anim_4
            hide EP18_Andrew_Anim_5
            hide EP18_Andrew_Anim_6
            hide EP18_Andrew_Anim_7
            $ EP18_Anim_Option = 1
            if EP18_Anim_Speed == 1:
                show EP18_Andrew_Anim_4 with Dissolve(0.5)
            if EP18_Anim_Speed == 2:
                show EP18_Andrew_Anim_5 with Dissolve(0.5)
            jump EP18_Andrew_Anim_Menu_1
        "View 2":
            hide EP18_Andrew_Anim_4
            hide EP18_Andrew_Anim_5
            hide EP18_Andrew_Anim_6
            hide EP18_Andrew_Anim_7
            $ EP18_Anim_Option = 2
            if EP18_Anim_Speed == 1:
                show EP18_Andrew_Anim_6 with Dissolve(0.5)
            elif EP18_Anim_Speed == 2:
                show EP18_Andrew_Anim_7 with Dissolve(0.5)
            jump EP18_Andrew_Anim_Menu_1
        "Slower":
            hide EP18_Andrew_Anim_4
            hide EP18_Andrew_Anim_5
            hide EP18_Andrew_Anim_6
            hide EP18_Andrew_Anim_7
            $ EP18_Anim_Speed = 1
            if EP18_Anim_Option == 1:
                show EP18_Andrew_Anim_4 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Andrew_Anim_6 with Dissolve(0.5)
            jump EP18_Andrew_Anim_Menu_1
        "Faster":
            hide EP18_Andrew_Anim_4
            hide EP18_Andrew_Anim_5
            hide EP18_Andrew_Anim_6
            hide EP18_Andrew_Anim_7
            $ EP18_Anim_Speed = 2
            if EP18_Anim_Option == 1:
                show EP18_Andrew_Anim_5 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Andrew_Anim_7 with Dissolve(0.5)
            jump EP18_Andrew_Anim_Menu_1
        "Continue":
            hide EP18_Andrew_Anim_4
            hide EP18_Andrew_Anim_5
            hide EP18_Andrew_Anim_6
            hide EP18_Andrew_Anim_7
            $ different_choice_menu = False
            pass
    scene 48-2 beach 102 with Dissolve(0.5)
    a1 "FUCK FUCK FUCK..."
    a1 "I'm... Cumming!"
    a1 "FUUCK!"
    play sound cum_sound
    scene 48-2 beach 103 with flash_vpunch
    a1 "AHHH!!"
    a "OH!"
    a1 "FUUCK!"
    scene 48-2 beach 104 with Dissolve(0.5)
    a "Oh... How awkward..."
    a1 "I'm... Sorry..."
    a1 "I didn't expect that..."
    a "Neither did I."
    a1 "You have to understand. I've not done anything."
    a "Not even masturbated?"
    a1 "No...I wanted to keep all that semen for you."
    a1 "And now it's wasted."
    $ renpy.end_replay()
    scene 48-2 beach 105 with Dissolve(0.5)
    a "Not all of it."
    a "I can still manage to 'reclaim' some."
    a1 "Serious?"
    a "Totaly."
    play sound licking_1
    scene 48-2 beach 106 with Dissolve(0.5)
    a1 "Oh shit!"
    a1 "That's good!"
    a "You like it?"
    a1 "YEAH!"
    show EP18_Andrew_Anim_8 with Dissolve(0.5)
    pause
    a1 "Ah!"
    a1 "AH!"
    a1 "It's a bit sensitive."
    a "Hehe."
    scene 48-2 beach 107 with Dissolve(0.5)
    hide EP18_Andrew_Anim_8
    a1 "Oh, Anna. Sweet Anna!"
    a1 "Such a good girlfriend!"
    if AnnaCorruption >=30:
        a "{i}...If only he knew...{/i}"
    play sound licking_2
    scene 48-2 beach 108 with Dissolve(0.5)
    a1 "You're really sucking it all up..."
    a1 "Damn!"
    a "Hehe..."
    scene 48-2 beach 109 with Dissolve(0.5)
    a "You sure you came so fast because you hadn't done it for a while?"
    a "Or maybe it was because of something else?"
    a1 "What do you mean?"
    a "Maybe you liked what you saw with the guys, and that really turned you on."
    scene 48-2 beach 110 with Dissolve(0.5)
    a1 "I don't know, Anna..."
    a1 "It's all confusing..."
    a "Hehe..."
    a1 "Please forgive me for cumming so fast."
    a1 "I know I left you wanting."
    scene 48-2 beach 111 with Dissolve(0.5)
    a "Eh. It's ok."
    a "There will be other times..."
    if AnnaCorruption >= 40:
        a "{i}...And other men...{/i}"
    scene 48-2 beach 112 with Dissolve(0.5)
    a1 "Yeah. I don't know what came over me."
    a1 "Cumming so fast..."
    a "{i}...Even for him, that was fast...{/i}"
    a "{i}...Perhaps he did actually like what he saw, and that sent him over the edge...{/i}"
    scene 48-2 beach 113 with Dissolve(0.5)
    a "There are still reasons to consider..."
    a1 "Maybe..."
    scene 48-2 beach 114 with Dissolve(0.5)
    a "I mean. It's normal for other guys to find me hot."
    a "That just means you've got a trophy at home. A grand prize that you own."
    a1 "Well..."
    scene 48-2 beach 115 with Dissolve(0.5)
    a "You sure you don't find it hot when other men crave me?"
    a1 "I..."
    a "It just means you've got something everyone wants..."
    a1 "When you put it that way... It makes sense..."
    scene 48-2 beach 116 with Dissolve(0.5)
    a "Hehe... Exactly..."
    a "Anyway. I think it's time to get going."
    a1 "Yeah. I feel a bit weird because of the... Alcohol and medicine mixing."
    a "Ok."
    play sound undress
    scene 48-2 beach 117 with Dissolve(0.5)
    pause 1
    scene 48-2 beach 118 with Dissolve(0.5)
    a1 "I still think this outfit is too minimal."
    a1 "Buut... I suppose it's all ok."
    a "Heh."
    scene 48-2 beach 119 with Dissolve(0.5)
    a "I knew you'd warm up to it."
    a "I know you like seeing it anyway. My body half covered."
    a "For all to see."
    a1 "Umm... I suppose..."
    a1 "{i}...Not sure how I feel about all of this...{/i}"
    scene black with Dissolve(0.5)
    pause 1
    scene 48-2 beach 120 with Dissolve(0.5)
    a1 "I mean... All in all, a nice day at the beach."
    a "Indeed."
    scene black with Dissolve(0.5)
    pause 1
    play music chill_song_2
    play ambient citytraffic
    scene 48-2 beach 121 with Dissolve(0.5)
    a "What are you planning to do next?"
    a1 "Not sure."
    a1 "Will lay down at home at first."
    a1 "Then figure it out."
    if BenjaminContent == True:
        b1 "{i}...That's Anna!{/i}"
        scene 48-2 beach 122 with Dissolve(0.5)
        b1 "{i}...As beautiful as ever...{/i}"
        b1 "{i}...I should talk to her...{/i}"
        scene 48-2 beach 123 with Dissolve(0.5)
        b1 "Anna! Hey!"
        a1 "Go away, dude!"
        a1 "Stop pestering us!"
        scene 48-2 beach 124 with Dissolve(0.5)
        a "Wait. No."
        a "I know him?"
        a1 "You know this bum?"
        a "Well... I'll have you know, he is not a bum anymore."
        b1 "That's right!"
        b1 "Now I'm a citizen with rights!"
        scene 48-2 beach 125 with Dissolve(0.5)
        b1 "How are you doing?"
        a "I'm good! Went to the beach."
        a "I'm more curious about you?"
        a "You settled in at work?"
        b1 "Hehe... I am!"
        b1 "As you can see, I've got a bunch of groceries bought."
        scene 48-2 beach 126 with Dissolve(0.5)
        a "Indeed."
        a "You should also get some new clothing."
        a "These old rags don't let you shine."
        b1 "Oh. Heh... You're right, but I just don't know where."
        a "I know a place where we could get something for you."
        a "At a discount."
        b1 "That sounds like a great idea!"
        a1 "{i}...How does Anna know him... Hmmm...{/i}"
        scene 48-2 beach 127 with Dissolve(0.5)
        b1 "Wait a minute..."
        scene 48-2 beach 128 with Dissolve(0.5)
        b1 "Sorry to cut it short... But... That's a great idea!"
        b1 "I forgot to turn the stove off, I gotta run!"
        a "Let's meet again today, a bit later, regarding clothes, ok?"
        a "There's the clothing shop in the shopping district. Alfred's clothing."
        b1 "Hmm... I'll find it."
        scene 48-2 beach 129 with Dissolve(0.5)
        b1 "Bye!"
        b1 "See you later!"
        a1 "Who was that guy?"
        a "Oh, Benjamin?"
        a "Just someone I've been helping out."
        a1 "You've been helping out a homeless guy?"
        a "Yeah, what of it?"
        scene 48-2 beach 130 with Dissolve(0.5)
        a1 "Nothing... That sounds very nice."
        b1 "{i}...Hehe, if only he knew what 'nice' things she has done for me...{/i}"
        b1 "{i}...With her mouth... with her nether regions... hehe...{/i}"
    scene 48-2 beach 131 with Dissolve(0.5)
    a1 "Oh, just remembered. Have to meet Ashley later."
    a1 "What are you going to do?"
    scene 48-2 beach 131-1 with Dissolve(0.5)
    a "Got some things to do."
    a "Will see."
    if BenjaminContent == True:
        a "Like you just heard, will meet Benjamin and help him with some clothing."
        a "I know the store owner, and he'd help out me and Benjamin."
        a1 "That's cool."
    else:
        a "Got some things to do... But one thing at a time, I'll also get home and rest a little..."
    scene black with Dissolve(0.5)
    pause 1
    stop ambient
    if BenjaminContent == True:
        scene 48-2 beach 132 with Dissolve(0.5)
        a "{i}...What we did at the beach was interesting...{/i}"
        a "{i}...Andrew looked conflicted, but not completely against the idea...{/i}"
        a "{i}...Perhaps he'd actually like it, with some encouragement...{/i}"
        a "{i}...Will see...{/i}"
        a "{i}...I guess I'll change back into my regular outfit...{/i}"
    else:
        jump EP18_John_1
    play sound undress
    scene black with Dissolve(0.5)
    pause 1
    if BenjaminContent == True:
        jump EP18_Benjamin_1
    else:
        jump EP18_John_1
label EP18_Benjamin_1:
    $ EP18_var_4 = True
    play ambient citytraffic
    play music chill_song_3
    scene 48-3 ben 1 with Dissolve(0.5)
    b1 "Anna!"
    b1 "So good to see you again!"
    a "Benjamin, hello."
    a "Managed to get home in time?"
    b1 "Yeah, all good. Heh."
    scene 48-3 ben 2 with Dissolve(0.5)
    b1 "You know. It's been a looong time since I've bought clothes at a normal shop..."
    b1 "Have to cherish this moment."
    a "Heh indeed."
    a "I'm glad you're getting back on track."
    b1 "You have no idea how happy I am about all this."
    play sound door2
    scene 48-3 ben 3 with Dissolve(0.5)
    a "So I know the owner of the shop as well as the assistant."
    a "Patricia. She's a wonderful girl. I bet she'll help us with some outfits for you."
    b1 "That's nice to hear."
    stop ambient
    scene 48-3 ben 4 with Dissolve(0.5)
    a "There she is."
    b1 "Oh she's beautiful."
    scene 48-3 ben 5 with Dissolve(0.5)
    a "Hello, Patricia!"
    p2 "Anna?"
    p2 "It's been a while since I've seen you!"
    p2 "I mean, don't get me wrong. I'm happy to see you!"
    scene 48-3 ben 6 with Dissolve(0.5)
    a "Oh... Sorry, I've been pretty busy lately."
    a "There's always something going on in my life, hehe."
    p2 "So. Who have you brought me today?"
    a "Oh. This is Benjamin. A friend of mine."
    a "I met him at the bar, and we're just picking out some new clothes for him."
    a "I also need something for an occasion."
    scene 48-3 ben 7 with Dissolve(0.5)
    b1 "Hello. Heh."
    b1 "Haven't been in a shop like this for quite some time."
    b1 "So I apologize for looking like this..."
    p2 "Not to worry, any friend of Anna's is a friend of mine."
    scene 48-3 ben 8 with Dissolve(0.5)
    p2 "Follow me to the changing cabin, and we'll pick out something for you."
    b1 "Sounds great!"
    scene 48-3 ben 9 with Dissolve(0.5)
    p2 "So. I'd like you to undress."
    b1 "Wha?"
    p2 "Meanwhile, I will choose something for you."
    a "She's good at finding nice-looking fits. Trust me."
    scene 48-3 ben 10 with Dissolve(0.5)
    p2 "Well, I didn't go to design school for no reason, hehe."
    p2 "So. Yeah. My specialty is giving people outfits that match their style, persona, and overall aesthetic."
    b1 "Wow. I'm impressed."
    p2 "Alright, Anna and I will pick something out."
    scene 48-3 ben 11 with Dissolve(0.5)
    p2 "So. Tough day, I see?"
    a "What do you mean?"
    scene 48-3 ben 12 with Dissolve(0.5)
    p2 "C'mon, Anna."
    p2 "It's obvious that man is a homeless guy or something."
    a "Technically not anymore. He has a place of his own."
    p2 "Why exactly are you helping him?"
    p2 "He's probably just some drunk that's gonna leech off you."
    scene 48-3 ben 13 with Dissolve(0.5)
    a "Don't say that."
    a "He's a lot better of a person than you'd think."
    a "Besides. I remember my grandpa. This man is also of older age and..."
    a "I just have a soft spot for older men in need."
    a "I can't help it. Won't let that nice man suffer on the street."
    scene 48-3 ben 14 with Dissolve(0.5)
    p2 "Oh, Anna."
    p2 "You with your kind heart."
    p2 "One of these days, someone will take advantage..."
    p2 "But if they do, I will tear their hair out, hehe."
    a "Haha. Patricia, always such a loyal friend."
    p2 "I've got something for him, let's go."
    scene 48-3 ben 15 with Dissolve(0.5)
    p2 "Alright, we're back!"
    p2 "You can open the door!"
    b1 "Umm... I'm a bit shy. I don't think we should do this."
    p2 "You mean you'll just stand there without new clothing?"
    b1 "Umm... I didn't think it through."
    p2 "Just open up."
    scene 48-3 ben 16 with Dissolve(0.5)
    p2 "Heh, a bit shy."
    a "See, I told you."
    a "He's just a kind old man who doesn't want to burden anyone..."
    a "But deserves things like these."
    b1 "Alright. I'll open it so you can give me clothes."
    scene 48-3 ben 17 with Dissolve(0.5)
    a "Oh."
    scene 48-3 ben 18 with Dissolve(0.5)
    p2 "WHAAA?"
    p2 "That's a..."
    p2 "{i}...Biig cock... Fucking hell...{/i}"
    p2 "Wait..."
    p2 "Why are you naked?"
    scene 48-3 ben 19 with Dissolve(0.5)
    b1 "You asked me to undress?!"
    p2 "Yeah, but obviously to leave underpants on or something."
    b1 "Shiet."
    scene 48-3 ben 20 with Dissolve(0.5)
    b1 "I didn't have anyone to begin with."
    b1 "I'm sorry for this..."
    b1 "I didn't mean to be this unprofessional."
    scene 48-3 ben 21 with Dissolve(0.5)
    p2 "It's umm... Ok."
    p2 "Here. Take the clothes."
    play sound cloth_sound1
    scene 48-3 ben 22 with Dissolve(0.5)
    b1 "Thanks. I'll get changed real quick."
    p2 "Umm... Yeah. Ok."
    a "Hehe..."
    scene 48-3 ben 23 with Dissolve(0.5)
    p2 "Oh my god..."
    p2 "That was the largest penis I've ever seen. What the..."
    p2 "Have you seen it before?"
    p2 "You didn't look as surprised."
    scene 48-3 ben 24 with Dissolve(0.5)
    a "Between you and I."
    a "I have..."
    p2 "What?"
    a "There was an accident once..."
    a "And I saw it, right up in my face..."
    p2 "Jeez."
    scene 48-3 ben 25 with Dissolve(0.5)
    b1 "Hmm..."
    b1 "What if I asked Anna for help, heh."
    b1 "I want to see her touch me..."
    scene 48-3 ben 26 with Dissolve(0.5)
    b1 "Hey, Anna?!"
    b1 "Anna?"
    a "Yes, Benjamin?"
    b1 "I've got this problem!"
    b1 "I can't bend down to put on the pants."
    b1 "It's my back... Been slowly giving out for a while now."
    b1 "Could you come in here and help out?"
    scene 48-3 ben 27 with Dissolve(0.5)
    p2 "Oh my... Heh..."
    a "Oh... That's... Since he doesn't have underpants..."
    p2 "Well, not to sound jealous, but you will see that big cock once more..."
    p2 "That's the upside, at least."
    a "Don't be so vulgar, Patricia."
    scene 48-3 ben 28 with Dissolve(0.5)
    p2 "What?"
    p2 "Just stating the obvious."
    p2 "Regardless if he's a homeless man, a girl can still appreciate a nice cock when she sees one."
    a "True."
    scene 48-3 ben 29 with Dissolve(0.5)
    p2 "I'll be right back, ok?"
    p2 "Will look for an outfit for you, too."
    a "Alright, I'll help the poor man, hehe."
    scene 48-3 ben 30 with Dissolve(0.5)
    a "Um..."
    a "Just... Let's get this over quickly, okay?"
    scene 48-3 ben 31 with Dissolve(0.5)
    b1 "Oh, absolutely. I just need a bit of help."
    a "Sure, sure."
    b1 "Come on in."
    b1 "You know, this cabin is larger than some of the places I used to live in..."
    a "What?"
    b1 "Crazy, I know."
    scene 48-3 ben 32 with Dissolve(0.5)
    a "Heh... This is a bit awkward."
    b1 "Yeah... I'm... Sorry..."
    b1 "{i}...Hehe... No, I'm not... I want her to check out my cock...{/i}"
    scene 48-3 ben 33 with Dissolve(0.5)
    a "Umm... Wait."
    a "You haven't even put on the top or anything."
    b1 "I always start with the pants."
    a "Alright, alright."
    scene 48-3 ben 34 with Dissolve(0.5)
    b1 "Juicy..."
    a "What?"
    b1 "Nothing, nothing. Heh."
    play sound jacketcloth
    scene 48-3 ben 35 with Dissolve(0.5)
    b1 "{i}...Yes... YES!... Hehe...{/i}"
    b1 "{i}..Hot Anna in front of me...{/i}"
    b1 "{i}...Again!... Hehe...{/i}"
    scene 48-3 ben 36 with Dissolve(0.5)
    a "{i}...It's so big...{/i}"
    a "{i}...Fuck...{/i}"
    a "{i}...Again, I'm starting to feel drawn to it...{/i}"
    play sound undress
    scene 48-3 ben 37 with Dissolve(0.5)
    a "Almost there."
    a "{i}...Such a nice cock...{/i}"
    a "{i}...Almost like it needs to be sucked...{/i}"
    scene 48-3 ben 38 with Dissolve(0.5)
    a "Your cock is in the way..."
    b1 "I can't help it, Anna..."
    b1 "It's just that big, and I have to deal with it."
    play sound jacketcloth
    scene 48-3 ben 39 with Dissolve(0.5)
    a "Oh..."
    b1 "Niice..."
    a "What?"
    b1 "Nothing... Nothing..."
    scene 48-3 ben 40 with Dissolve(0.5)
    pause 1
    play sound undress
    scene 48-3 ben 44 with Dissolve(0.5)
    b1 "Ahh..."
    b1 "Yeah."
    scene 48-3 ben 45 with Dissolve(0.5)
    b1 "You know..."
    b1 "You can get it whenever you want. Hehe..."
    a "What?"
    scene 48-3 ben 46 with Dissolve(0.5)
    a "Stop fooling around, Ben."
    a "We can't do some naughty stuff in here."
    b1 "Why not?"
    b1 "Worried someone will hear?"
    a "Umm..."
    a "No..."
    a "Just. Not appropriate."
    b1 "Heh. I've seen that look on your face before."
    play sound undress
    scene 48-3 ben 47 with Dissolve(0.5)
    b1 "Ok, All done."
    b1 "Gotta say, I feel nice in a new set of clothes."
    a "You also look outstanding."
    b1 "Thank you..."
    scene 48-3 ben 48 with Dissolve(0.5)
    a "Patricia!"
    scene 48-3 ben 49 with Dissolve(0.5)
    p2 "Yes?"
    a "We're all done here."
    a "And I gotta say, you've picked out something really nice for him."
    p2 "Thank you. My aim is to please."
    scene 48-3 ben 50 with Dissolve(0.5)
    b1 "I feel so good in this. Thank you!"
    b1 "I mean, it looks good, feels good, smells good."
    p2 "I'm glad I could put a smile on your face."
    b1 "Looking this fresh, I guess I'm going to have to invite Anna to dinner, hehe."
    p2 "Interesting."
    scene 48-3 ben 51 with Dissolve(0.5)
    p2 "So. All done here?"
    a "I think so."
    p2 "Let's go and finalize this thing."
    b1 "Alright!"
    scene 48-3 ben 53 with Dissolve(0.5)
    b1 "So how much will that set me back?"
    a "Oh, don't worry about this."
    a "I'll cover it."
    scene 48-3 ben 54 with Dissolve(0.5)
    p2 "Don't forget, I also picked out something for you."
    a "Oh. hehe. Thanks."
    a "I wonder what it is."
    p2 "Trust me, you won't be disappointed."
    a "I'll keep you to it, Patricia. Haha."
    scene 48-3 ben 55 with Dissolve(0.5)
    p2 "I'll also give you a generous discount since you're a regular here."
    p2 "And knowing Alfred, he wouldn't mind."
    p2 "In fact, sales have been up since that fashion show."
    b1 "Thank you once more."
    b1 "Let me carry that for you."
    scene 48-3 ben 56 with Dissolve(0.5)
    a "Thanks."
    b1 "You sure you can pay?"
    a "Easily."
    b1 "I will repay you 10 fold."
    a "Hehe. I'll keep you to it."
    scene 48-3 ben 57 with Dissolve(0.5)
    p2 "Thanks for shopping with us!"
    p2 "Nice to see you, Benjamin."
    p2 "See you around, Anna!"
    b1 "Bye, lovely Patricia!"
    scene 48-3 ben 58 with Dissolve(0.5)
    p2 "Take care!"
    a "Bye!"
    play sound door2
    scene 48-3 ben 60 with Dissolve(0.5)
    b1 "That was great."
    b1 "I will certainly try to keep this outfit in good condition."
    b1 "It's excellent."
    b1 "Thank you so much."
    b1 "Anyway. You up for that dinner?"
    a "At your place?"
    b1 "Yeah. To celebrate the occasion. Besides, you bought this outfit for me. The least I can do is cook you something nice."
    b1 "I do know how to cook some nice dishes. And I promise, they will contain good ingredients."
    scene 48-3 ben 59 with Dissolve(0.5)
    a "Hehe. Alright. You convinced me."
    a "This evening then?"
    b1 "Absolutely!"
    a "I'd be glad to have dinner at your place, Benjamin."
    b1 "Oh, Yes!"
    b1 "I'll cook something very nice."
    a "I will. See you in the evening."
    b1 "Bye, Anna!"
    scene black with Dissolve(0.5)
    pause 1
    jump EP18_John_1
label EP18_Benjamin_2:
    $ EP18_var_8 = True
    stop ambient
    play music chill_song_6
    scene 48-5 ben 1 with Dissolve(0.5)
    b1 "Anna! You're finally here."
    a "MMm... Smells great!"
    b1 "I've been cooking since we last spoke, hehe."
    a "Impressive. You've been a busy bee."
    scene 48-5 ben 2 with Dissolve(0.5)
    b1 "Indeed."
    b1 "But only the best for you, Anna."
    b1 "I've been out of practice for a bit, but that's why I've been cooking non-stop since then."
    a "I'm sure it's going to be lovely."
    scene 48-5 ben 3 with Dissolve(0.5)
    a "{i}...Mmm... Smells really good...{/i}"
    a "{i}...Last time I was here...{/i}"
    a "{i}...Benny penetrated me on that table...{/i}"
    scene 48-5 ben 4 with Dissolve(0.5)
    a "I hope you don't mind. I'll go to the toilet real quick."
    a "{i}...And change into the outfit that Patricia gave me...{/i}"
    a "{i}...Surprise Benny...{/i}"
    b1 "Absolutely!"
    b1 "Do whatever you'd like. Toilet, bath, TV."
    a "Thanks, heh."
    scene 48-5 ben 6 with Dissolve(0.5)
    a "I'll be back soon, ok?"
    b1 "No rush."
    scene 48-5 ben 7 with Dissolve(0.5)
    pause 1
    scene 48-5 ben 8 with Dissolve(0.5)
    a "Alright."
    a "Let's see what kind of an outfit Patricia picked out for me."
    play sound undress
    scene 48-5 ben 9 with Dissolve(0.5)
    pause 1
    play sound cloth_sound1
    scene black with Dissolve(0.5)
    pause 1
    play sound jacketcloth
    scene 48-5 ben 10 with Dissolve(0.5)
    a "The front is nice, but..."
    scene 48-5 ben 11 with Dissolve(0.5)
    a "Whaat?"
    a "There's absolutely nothing covering my back..."
    a "Oh Patricia, you naughty, naughty girl."
    a "Didn't expect anything less from that minx."
    a "Let's see what Benjamin thinks."
    scene 48-5 ben 12 with Dissolve(0.5)
    pause 1
    scene 48-5 ben 13 with Dissolve(0.5)
    pause 1
    scene 48-5 ben 14 with Dissolve(0.5)
    b1 "That's a nice outfit, Anna."
    b1 "Proper and beautiful."
    a "{i}...He hasn't noticed the back yet, heh...{/i}"
    a "{i}...He's in for a nice surprise...{/i}"
    scene 48-5 ben 15 with Dissolve(0.5)
    b1 "I like it."
    a "Me too."
    a "It also has a little surprise."
    b1 "Oh?"
    scene 48-5 ben 16 with Dissolve(0.5)
    b1 "I wonder what the surprise is."
    a "You'll see soon."
    b1 "Can't wait, hehe."
    scene 48-5 ben 17 with Dissolve(0.5)
    b1 "Could you help me out with the dishes?"
    a "Sure."
    b1 "Just put everything on the table."
    b1 "The food is almost ready."
    scene 48-5 ben 18 with Dissolve(0.5)
    b1 "I'm sure you will love what I've prepared for the both of us."
    a "Hehe. I trust you."
    scene 48-5 ben 19 with Dissolve(0.5)
    pause 1
    play sound surprise2
    scene 48-5 ben 20 with Dissolve(0.5)
    b1 "{i}....OoooOOOoooOOAAAAA!!!...{/i}"
    b1 "{i}..SHIEEEETT!!...{/i}"
    b1 "{i}...She got nothing covering that... WHAA?{/i}"
    scene 48-5 ben 21 with Dissolve(0.5)
    b1 "{i}...She nastyyyy!!!...{/i}"
    b1 "Just the way I like it!"
    a "What's that?"
    b1 "Ummm... Nothing, did I say that out loud?"
    a "Yeah..."
    scene 48-5 ben 22 with Dissolve(0.5)
    a "Hold on. those dishes are a bit lower."
    a "Just... Have to reach down there."
    b1 "{i}..AaaaaaaAAAAAaAAAAAHHHOOOO!...{/i}"
    b1 "{i}...THAT ASSSS!!!{/i}"
    scene 48-5 ben 23 with Dissolve(0.5)
    a "{i}...Hehe...{/i}"
    a "{i}...I can feel his gaze on my luscious butt...{/i}"
    scene 48-5 ben 24 with Dissolve(0.5)
    a "That's all?"
    b1 "Yeah, these will do."
    b1 "Khem."
    scene 48-5 ben 25 with Dissolve(0.5)
    b1 "Just put them on the counter."
    b1 "I'll do the rest."
    a "Ok."
    scene 48-5 ben 26 with Dissolve(0.5)
    pause 1
    scene 48-5 ben 27 with Dissolve(0.5)
    b1 "{i}...I feel like I'm going to get LUCKYYYY...{/i}"
    b1 "You can just sit at the table. Be right with ya."
    a "Can't wait. It smells amazing!"
    b1 "Trust me, it is."
    scene 48-5 ben 28 with Dissolve(0.5)
    a "I know what you saw back there."
    a "When I leaned over."
    a "We will manage to finish our food, right?"
    a "I'm hungry."
    scene 48-5 ben 29 with Dissolve(0.5)
    b1 "As you command, Anna."
    b1 "I shall keep my composure."
    b1 "Besides, you have to taste this soup. It's exquisite."
    scene 48-5 ben 30 with Dissolve(0.5)
    b1 "You know..."
    b1 "I used to be a chef."
    b1 "And Ramen soup was one of my specialties."
    a "Really?"
    a "I never knew."
    scene 48-5 ben 31 with Dissolve(0.5)
    b1 "Eh. That time has long since passed."
    b1 "Now I'm a degenerate with good taste, that be all."
    a "You are not a degenerate."
    b1 "Heh, you know what I mean."
    scene 48-5 ben 32 with Dissolve(0.5)
    b1 "Here."
    b1 "Best I can offer."
    a "I'm sure it will exceed expectations."
    b1 "I'll let you be the judge of that."
    scene 48-5 ben 33 with Dissolve(0.5)
    a "Thank you, Benjamin."
    b1 "Only the best for you."
    play sound jacketcloth
    scene 48-5 ben 34 with Dissolve(0.5)
    b1 "Let's dig in. I'm starving."
    a "Me too."
    scene 48-5 ben 35 with Dissolve(0.5)
    a "I can't remember the last time I had food from Asian cuisine."
    b1 "Indeed, I am in the same situation."
    b1 "Now that I get a paycheck, I can finally afford to eat proper food again."
    b1 "Before it was scraps, leftovers... Eh..."
    a "But not anymore, Benjamin."
    scene 48-5 ben 36 with Dissolve(0.5)
    a "Alright, let's see what you've cooked up."
    scene 48-5 ben 37 with Dissolve(0.5)
    b1 "Classic ramen soup recipe."
    scene 48-5 ben 38 with Dissolve(0.5)
    a "MMMmmmmm!"
    a "It's so GOOD!"
    b1 "Really?"
    a "Oh yeah!"
    a "Wow!"
    a "So much flavor."
    b1 "Heh..."
    scene black with Dissolve(0.5)
    pause 1
    scene 48-5 ben 39 with Dissolve(0.5)
    a "Wow. I can't believe I finished it all so fast."
    b1 "That's how the ramen soup is."
    b1 "It gets ya."
    a "And a bit spicy."
    scene 48-5 ben 40 with Dissolve(0.5)
    b1 "Wouldn't have it any other way."
    a "I'm not against it. It's great!"
    a "Wow, I'm still in disbelief."
    a "I didn't know you cooked such great food."
    b1 "I really tried my best."
    scene 48-5 ben 41 with Dissolve(0.5)
    b1 "Alright, that's that."
    b1 "Heh."
    b1 "I'll just clean up."
    scene 48-5 ben 42 with Dissolve(0.5)
    a "You know. I'll help out."
    b1 "You don't have to."
    a "It's the least I can do to help out."
    a "The meal was worth it."
    scene 48-5 ben 43 with Dissolve(0.5)
    b1 "Thanks, Anna."
    a "Thank you for the tasty, tasty food."
    scene 48-5 ben 44 with Dissolve(0.5)
    a "Lemme just."
    b1 "Ok..."
    b1 "{i}...Wha...{/i}"
    b1 "{i}...Fucking amazing ass... FUCK!{/i}"
    scene 48-5 ben 45 with Dissolve(0.5)
    a "You all good there, Benjamin?"
    b1 "I... Umm..."
    b1 "I think."
    scene 48-5 ben 46 with Dissolve(0.5)
    b1 "{i}..OH MY GOD!!!!!...{/i}"
    b1 "{i}...I WANNA SNIFF HER ASS SO BAD!...{/i}"
    a "You mentioned you were a chef before."
    a "Perhaps in the near future, it's worth trying to find a job somewhere in that field."
    scene 48-5 ben 47 with Dissolve(0.5)
    a "You know?"
    a "Benjamin?"
    b1 "MMMMMMM."
    scene 48-5 ben 48 with Dissolve(0.5)
    a "Oh..."
    b1 "Soo... Soft..."
    scene 48-5 ben 49 with Dissolve(0.5)
    a "Oh... Ah..."
    b1 "Yes, yes, yes."
    scene 48-5 ben 50 with Dissolve(0.5)
    a "Haha... Benjamin."
    a "It's... A bit inappropriate, don't you think?"
    b1 "I... Think it's fine, hehe."
    scene 48-5 ben 51 with Dissolve(0.5)
    b1 "Let me know if you'd like me to stop. Heh."
    a "Um..."
    $ persistent.scene_52 = True
    label EP18_Benjamin_Sex_1:
    $ renpy.music.play("audio/sounds/chill_song_6.mp3", channel = 'music', if_changed = True)
    scene 48-5 ben 52 with Dissolve(0.5)
    a "Ok..."
    b1 "Should I stop?"
    a "N... No..."
    scene 48-5 ben 53 with Dissolve(0.5)
    b1 "Good, heh."
    b1 "I thought as much."
    scene 48-5 ben 54 with Dissolve(0.5)
    b1 "{b}*Sniff*{/b}"
    b1 "AAHHH!"
    b1 "YEAH!"
    play audio female_moan_1
    scene 48-5 ben 55 with Dissolve(0.5)
    a "Ooh... Benny."
    b1 "MHMM!"
    scene 48-5 ben 56 with Dissolve(0.5)
    a "Sniff that asshole!"
    a "And lick that pussy!"
    a "Oh... Benny!"
    play sound jerk3 loop
    scene 48-5 ben 57 with Dissolve(0.5)
    b1 "Barely got in there, and that pussy's already moist."
    b1 "Now ain't that peculiar."
    play audio female_moan_2
    a "I... I would agree..."
    scene 48-5 ben 58 with Dissolve(0.5)
    b1 "MM!"
    b1 "That crack is full of your sweat and juices."
    b1 "I fucking love a sweaty woman!"
    stop sound
    scene 48-5 ben 59 with Dissolve(0.5)
    b1 "Come here!"
    scene 48-5 ben 60 with Dissolve(0.5)
    b1 "How about you lose that beautiful, beautiful dress for me."
    b1 "The only thing that looks better on you is nothing."
    b1 "When absolutely nothing covers you. THAT looks just so amazing!"
    play sound undress
    scene 48-5 ben 61 with Dissolve(0.5)
    pause 1
    scene 48-5 ben 62 with Dissolve(0.5)
    b1 "You are such a pleasing woman."
    b1 "Anna, oh Anna."
    b1 "What fortunes favor me to see such a woman naked."
    play sound cloth_sound1
    scene 48-5 ben 63 with Dissolve(0.5)
    a "Hehe."
    a "Perhaps you'd like it if I touched you. That would make things even better, wouldn't it?"
    b1 "OH YES, YES!"
    scene 48-5 ben 64 with Dissolve(0.5)
    b1 "YES!"
    b1 "OH..."
    b1 "Never get used to the sensation your hands bring."
    scene 48-5 ben 65 with Dissolve(0.5)
    a "Come with me."
    b1 "Oh... Hah."
    b1 "Lead the way."
    b1 "You control my body now anyway."
    scene 48-5 ben 66 with Dissolve(0.5)
    a "You're telling me that if I wanted, I could rob a bank with your body?"
    b1 "Anything for you, Anna!"
    a "Hehe."
    play audio surprise
    play sound jacketcloth
    scene 48-5 ben 67 with Dissolve(0.5)
    b1 "OH."
    b1 "Hah."
    a "Now. Where were we?"
    scene 48-5 ben 68 with Dissolve(0.5)
    a "Perhaps a little..."
    a "Mouth would make you feel a bit better?"
    b1 "Oh, please, please!"
    b1 "Anna, YES!"
    play sound undress
    scene 48-5 ben 69 with Dissolve(0.5)
    a "There we go."
    scene 48-5 ben 70 with Dissolve(0.5)
    b1 "YOUR HANDS!"
    b1 "Soo... Nice..."
    a "I know, Benny."
    a "I know."
    scene 48-5 ben 71 with Dissolve(0.5)
    b1 "I'm the luckiest son of a bitch to walk this earthly plane."
    a "Hehe."
    a "You always had a way with words."
    $ different_choice_menu = True
    $ EP18_Anim_Option = 1
    $ EP18_Anim_Speed = 1
    scene black
    play sound jerk loop
    show EP18_Benny_Anim_1 with Dissolve(0.5)
    label EP18_Benny_Sex_Label_1:
    b1 "OH shit!"
    b1 "Them HANDS! THEM HANNNDS!"
    b1 "OHHAAA!"
    menu EP18_Benny_Anim_Menu_1:
        "View 1":
            hide EP18_Benny_Anim_1
            hide EP18_Benny_Anim_2
            hide EP18_Benny_Anim_3
            hide EP18_Benny_Anim_4
            $ EP18_Anim_Option = 1
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_1 with Dissolve(0.5)
            if EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_2 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_1
        "View 2":
            hide EP18_Benny_Anim_1
            hide EP18_Benny_Anim_2
            hide EP18_Benny_Anim_3
            hide EP18_Benny_Anim_4
            $ EP18_Anim_Option = 2
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_3 with Dissolve(0.5)
            elif EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_4 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_1
        "Slower":
            hide EP18_Benny_Anim_1
            hide EP18_Benny_Anim_2
            hide EP18_Benny_Anim_3
            hide EP18_Benny_Anim_4
            $ EP18_Anim_Speed = 1
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_1 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_3 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_1
        "Faster":
            hide EP18_Benny_Anim_1
            hide EP18_Benny_Anim_2
            hide EP18_Benny_Anim_3
            hide EP18_Benny_Anim_4
            $ EP18_Anim_Speed = 2
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_2 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_4 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_1
        "Continue":
            hide EP18_Benny_Anim_1
            hide EP18_Benny_Anim_2
            hide EP18_Benny_Anim_3
            hide EP18_Benny_Anim_4
            $ different_choice_menu = False
            pass
    scene 48-5 ben 72 with Dissolve(0.5)
    a "Looks so good up close."
    b1 "I took good care of it for you."
    a "Hehe."
    scene 48-5 ben 73 with Dissolve(0.5)
    a "Mmm..."
    a "MMMM!"
    b1 "OH, YES!"
    scene 48-5 ben 74 with Dissolve(0.5)
    b1 "AAHHHH!"
    a "KHA. KHA!"
    $ different_choice_menu = True
    $ EP18_Anim_Option = 1
    $ EP18_Anim_Speed = 1
    scene black
    play sound jerk loop
    show EP18_Benny_Anim_5 with Dissolve(0.5)
    label EP18_Benny_Sex_Label_2:
    b1 "FUUUUUUUUUUUUUU..."
    a "AH. KHAA!"
    menu EP18_Benny_Anim_Menu_2:
        "View 1":
            hide EP18_Benny_Anim_5
            hide EP18_Benny_Anim_6
            hide EP18_Benny_Anim_7
            hide EP18_Benny_Anim_8
            $ EP18_Anim_Option = 1
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_5 with Dissolve(0.5)
            if EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_6 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_2
        "View 2":
            hide EP18_Benny_Anim_5
            hide EP18_Benny_Anim_6
            hide EP18_Benny_Anim_7
            hide EP18_Benny_Anim_8
            $ EP18_Anim_Option = 2
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_7 with Dissolve(0.5)
            elif EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_8 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_2
        "Slower":
            hide EP18_Benny_Anim_5
            hide EP18_Benny_Anim_6
            hide EP18_Benny_Anim_7
            hide EP18_Benny_Anim_8
            $ EP18_Anim_Speed = 1
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_5 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_7 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_2
        "Faster":
            hide EP18_Benny_Anim_5
            hide EP18_Benny_Anim_6
            hide EP18_Benny_Anim_7
            hide EP18_Benny_Anim_8
            $ EP18_Anim_Speed = 2
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_6 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_8 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_2
        "Continue":
            hide EP18_Benny_Anim_5
            hide EP18_Benny_Anim_6
            hide EP18_Benny_Anim_7
            hide EP18_Benny_Anim_8
            $ different_choice_menu = False
            pass
    $ different_choice_menu = True
    $ EP18_Anim_Option = 1
    $ EP18_Anim_Speed = 1
    scene black
    play sound jerk loop
    show EP18_Benny_Anim_9 with Dissolve(0.5)
    label EP18_Benny_Sex_Label_3:
    b1 "FUUUUUUUUUUUUUU..."
    a "AH. KHAA!"
    menu EP18_Benny_Anim_Menu_3:
        "View 1":
            hide EP18_Benny_Anim_9
            hide EP18_Benny_Anim_10
            hide EP18_Benny_Anim_11
            hide EP18_Benny_Anim_12
            hide EP18_Benny_Anim_13
            hide EP18_Benny_Anim_14
            $ EP18_Anim_Option = 1
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_9 with Dissolve(0.5)
            if EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_10 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_3
        "View 2":
            hide EP18_Benny_Anim_9
            hide EP18_Benny_Anim_10
            hide EP18_Benny_Anim_11
            hide EP18_Benny_Anim_12
            hide EP18_Benny_Anim_13
            hide EP18_Benny_Anim_14
            $ EP18_Anim_Option = 2
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_11 with Dissolve(0.5)
            elif EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_12 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_3
        "View 3":
            hide EP18_Benny_Anim_9
            hide EP18_Benny_Anim_10
            hide EP18_Benny_Anim_11
            hide EP18_Benny_Anim_12
            hide EP18_Benny_Anim_13
            hide EP18_Benny_Anim_14
            $ EP18_Anim_Option = 3
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_13 with Dissolve(0.5)
            elif EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_14 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_3
        "Slower":
            hide EP18_Benny_Anim_9
            hide EP18_Benny_Anim_10
            hide EP18_Benny_Anim_11
            hide EP18_Benny_Anim_12
            hide EP18_Benny_Anim_13
            hide EP18_Benny_Anim_14
            $ EP18_Anim_Speed = 1
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_5 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_7 with Dissolve(0.5)
            elif EP18_Anim_Option == 3:
                show EP18_Benny_Anim_13 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_3
        "Faster":
            hide EP18_Benny_Anim_9
            hide EP18_Benny_Anim_10
            hide EP18_Benny_Anim_11
            hide EP18_Benny_Anim_12
            hide EP18_Benny_Anim_13
            hide EP18_Benny_Anim_14
            $ EP18_Anim_Speed = 2
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_6 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_8 with Dissolve(0.5)
            elif EP18_Anim_Option == 3:
                show EP18_Benny_Anim_14 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_3
        "Continue":
            hide EP18_Benny_Anim_9
            hide EP18_Benny_Anim_10
            hide EP18_Benny_Anim_11
            hide EP18_Benny_Anim_12
            hide EP18_Benny_Anim_13
            hide EP18_Benny_Anim_14
            $ different_choice_menu = False
            pass
    scene 48-5 ben 75 with Dissolve(0.5)
    a "I bet you liked that."
    b1 "Liked that?"
    b1 "I fuckity LOVED that!"
    scene 48-5 ben 76 with Dissolve(0.5)
    a "Hehe..."
    a "I'm glad to hear that."
    b1 "Can't wait what else you've got in mind."
    a "Well... I... Pretty wet down there."
    a "I have to bring down the excitement levels."
    a "For the both of us..."
    scene 48-5 ben 77 with Dissolve(0.5)
    b1 "OOh... Heh."
    b1 "You know how to intrigue an old homeless man."
    a "Now, now. You aren't homeless anymore."
    b1 "Heh. You're right!"
    scene 48-5 ben 78 with Dissolve(0.5)
    a "Let me just get comfortable."
    b1 "Oh... Take all the time you need."
    play sound undress
    scene 48-5 ben 79 with Dissolve(0.5)
    pause 1
    scene 48-5 ben 80 with Dissolve(0.5)
    a "You ready?"
    b1 "Never been more ready."
    play sound femmoan_1
    scene 48-5 ben 81 with Dissolve(0.5)
    a "AHH!"
    b1 "Oh, jolly good!"
    b1 "OH SO GOOOD!"
    play sound femmoan_2
    a "Benny!"
    b1 "Anna!"
    scene 48-5 ben 82 with Dissolve(0.5)
    a "Let me give you a nice ride, ok?"
    b1 "Be my guest!"
    play sound femmoan_3
    b1 "I want all of that!"
    scene 48-5 ben 83 with Dissolve(0.5)
    a "So do I..."
    a "Oh... That dick..."
    a "Patricia also saw it... She also fucking enjoyed seeing that huge cock of yours."
    scene 48-5 ben 84 with Dissolve(0.5)
    b1 "You're just... Saying that to be nice."
    b1 "Ahhh..."
    play sound femmoan_3
    a "Only the truth for you."
    scene 48-5 ben 85 with Dissolve(0.5)
    a "FUCK!"
    a "It hits so deep!"
    b1 "I know!"
    play audio female_moan_2
    b1 "I feel like I'm almost hitting your cervix!"
    a "Almost?"
    a "You're already there!"
    play audio female_moan_4
    a "AHHH!"
    $ different_choice_menu = True
    $ EP18_Anim_Option = 1
    $ EP18_Anim_Speed = 1
    scene black
    play sound jerk loop
    show EP18_Benny_Anim_15 with Dissolve(0.5)
    label EP18_Benny_Sex_Label_4:
    b1 "OH GIRL!"
    a "AH. BENNY!"
    play audio female_moan_3
    a "YOU'RE SO HUGE!"
    menu EP18_Benny_Anim_Menu_4:
        "View 1":
            hide EP18_Benny_Anim_15
            hide EP18_Benny_Anim_16
            hide EP18_Benny_Anim_17
            hide EP18_Benny_Anim_18
            $ EP18_Anim_Option = 1
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_15 with Dissolve(0.5)
            if EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_16 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_4
        "View 2":
            hide EP18_Benny_Anim_15
            hide EP18_Benny_Anim_16
            hide EP18_Benny_Anim_17
            hide EP18_Benny_Anim_18
            $ EP18_Anim_Option = 2
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_17 with Dissolve(0.5)
            elif EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_18 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_4
        "Slower":
            hide EP18_Benny_Anim_15
            hide EP18_Benny_Anim_16
            hide EP18_Benny_Anim_17
            hide EP18_Benny_Anim_18
            $ EP18_Anim_Speed = 1
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_15 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_17 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_4
        "Faster":
            hide EP18_Benny_Anim_15
            hide EP18_Benny_Anim_16
            hide EP18_Benny_Anim_17
            hide EP18_Benny_Anim_18
            $ EP18_Anim_Speed = 2
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_16 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_18 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_4
        "Continue":
            hide EP18_Benny_Anim_15
            hide EP18_Benny_Anim_16
            hide EP18_Benny_Anim_17
            hide EP18_Benny_Anim_18
            $ different_choice_menu = False
            pass
    scene 48-5 ben 86 with Dissolve(0.5)
    a "AAHHHH!!"
    b1 "ANNNAAA!"
    a "FUCK YES!"
    b1 "You like that cock, eh?"
    b1 "You like how I fuck your hot, hot pussy with it?"
    a "MHMMM!!!"
    $ different_choice_menu = True
    $ EP18_Anim_Option = 1
    $ EP18_Anim_Speed = 1
    scene black
    play sound jerk loop
    show EP18_Benny_Anim_19 with Dissolve(0.5)
    label EP18_Benny_Sex_Label_5:
    a "OH... SO GOOOD!!!"
    play sound femmoan_3
    b1 "BABYYY!"
    menu EP18_Benny_Anim_Menu_5:
        "View 1":
            hide EP18_Benny_Anim_19
            hide EP18_Benny_Anim_20
            hide EP18_Benny_Anim_21
            hide EP18_Benny_Anim_22
            hide EP18_Benny_Anim_39
            hide EP18_Benny_Anim_40
            $ EP18_Anim_Option = 1
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_19 with Dissolve(0.5)
            if EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_20 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_5
        "View 2":
            hide EP18_Benny_Anim_19
            hide EP18_Benny_Anim_20
            hide EP18_Benny_Anim_21
            hide EP18_Benny_Anim_22
            hide EP18_Benny_Anim_39
            hide EP18_Benny_Anim_40
            $ EP18_Anim_Option = 2
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_21 with Dissolve(0.5)
            elif EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_22 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_5
        "View 3":
            hide EP18_Benny_Anim_19
            hide EP18_Benny_Anim_20
            hide EP18_Benny_Anim_21
            hide EP18_Benny_Anim_22
            hide EP18_Benny_Anim_39
            hide EP18_Benny_Anim_40
            $ EP18_Anim_Option = 3
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_39 with Dissolve(0.5)
            elif EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_40 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_5
        "Slower":
            hide EP18_Benny_Anim_19
            hide EP18_Benny_Anim_20
            hide EP18_Benny_Anim_21
            hide EP18_Benny_Anim_22
            hide EP18_Benny_Anim_39
            hide EP18_Benny_Anim_40
            $ EP18_Anim_Speed = 1
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_19 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_21 with Dissolve(0.5)
            elif EP18_Anim_Option == 3:
                show EP18_Benny_Anim_39 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_5
        "Faster":
            hide EP18_Benny_Anim_19
            hide EP18_Benny_Anim_20
            hide EP18_Benny_Anim_21
            hide EP18_Benny_Anim_22
            hide EP18_Benny_Anim_39
            hide EP18_Benny_Anim_40
            $ EP18_Anim_Speed = 2
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_20 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_22 with Dissolve(0.5)
            elif EP18_Anim_Option == 3:
                show EP18_Benny_Anim_40 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_5
        "Continue":
            hide EP18_Benny_Anim_19
            hide EP18_Benny_Anim_20
            hide EP18_Benny_Anim_21
            hide EP18_Benny_Anim_22
            hide EP18_Benny_Anim_39
            hide EP18_Benny_Anim_40
            $ different_choice_menu = False
            pass
    $ different_choice_menu = True
    $ EP18_Anim_Option = 1
    $ EP18_Anim_Speed = 1
    scene black
    play sound jerk loop
    show EP18_Benny_Anim_23 with Dissolve(0.5)
    label EP18_Benny_Sex_Label_6:
    play audio female_moan_3
    a "This is perfect!"
    menu EP18_Benny_Anim_Menu_6:
        "View 1":
            hide EP18_Benny_Anim_23
            hide EP18_Benny_Anim_24
            hide EP18_Benny_Anim_25
            hide EP18_Benny_Anim_26
            $ EP18_Anim_Option = 1
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_23 with Dissolve(0.5)
            if EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_24 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_6
        "View 2":
            hide EP18_Benny_Anim_23
            hide EP18_Benny_Anim_24
            hide EP18_Benny_Anim_25
            hide EP18_Benny_Anim_26
            $ EP18_Anim_Option = 2
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_25 with Dissolve(0.5)
            elif EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_26 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_6
        "Slower":
            hide EP18_Benny_Anim_23
            hide EP18_Benny_Anim_24
            hide EP18_Benny_Anim_25
            hide EP18_Benny_Anim_26
            $ EP18_Anim_Speed = 1
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_23 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_25 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_6
        "Faster":
            hide EP18_Benny_Anim_23
            hide EP18_Benny_Anim_24
            hide EP18_Benny_Anim_25
            hide EP18_Benny_Anim_26
            $ EP18_Anim_Speed = 2
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_24 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_26 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_6
        "Continue":
            hide EP18_Benny_Anim_23
            hide EP18_Benny_Anim_24
            hide EP18_Benny_Anim_25
            hide EP18_Benny_Anim_26
            $ different_choice_menu = False
            pass
    scene 48-5 ben 87 with Dissolve(0.5)
    a "So fucking good..."
    play sound cloth_sound1
    scene 48-5 ben 88 with Dissolve(0.5)
    a "Come. Penetrate me with that rod."
    b1 "Just the pose I wanted!"
    b1 "You know how to make a man happy!"
    a "And you know how to make a woman happy!"
    scene 48-5 ben 89 with Dissolve(0.5)
    b1 "Such a sweet, sweet thing."
    a "C'mon."
    a "Give me what I want."
    b1 "Hehe... As you command!"
    scene 48-5 ben 90 with Dissolve(0.5)
    a "Fuck..."
    scene 48-5 ben 91 with Dissolve(0.5)
    a "AHHH!"
    b1 "YEAH!"
    b1 "That pussy just gets better and better!"
    a "And so does your cock!"
    $ different_choice_menu = True
    $ EP18_Anim_Option = 1
    $ EP18_Anim_Speed = 1
    scene black
    play sound jerk loop
    show EP18_Benny_Anim_27 with Dissolve(0.5)
    label EP18_Benny_Sex_Label_7:
    b1 "The... Hottest... Woman... Ever..."
    b1 "YEEEHAAAWW!"
    menu EP18_Benny_Anim_Menu_7:
        "View 1":
            hide EP18_Benny_Anim_27
            hide EP18_Benny_Anim_28
            hide EP18_Benny_Anim_29
            hide EP18_Benny_Anim_30
            $ EP18_Anim_Option = 1
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_27 with Dissolve(0.5)
            if EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_28 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_7
        "View 2":
            hide EP18_Benny_Anim_27
            hide EP18_Benny_Anim_28
            hide EP18_Benny_Anim_29
            hide EP18_Benny_Anim_30
            $ EP18_Anim_Option = 2
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_29 with Dissolve(0.5)
            elif EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_30 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_7
        "Slower":
            hide EP18_Benny_Anim_27
            hide EP18_Benny_Anim_28
            hide EP18_Benny_Anim_29
            hide EP18_Benny_Anim_30
            $ EP18_Anim_Speed = 1
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_27 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_29 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_7
        "Faster":
            hide EP18_Benny_Anim_27
            hide EP18_Benny_Anim_28
            hide EP18_Benny_Anim_29
            hide EP18_Benny_Anim_30
            $ EP18_Anim_Speed = 2
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_28 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_30 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_7
        "Continue":
            hide EP18_Benny_Anim_27
            hide EP18_Benny_Anim_28
            hide EP18_Benny_Anim_29
            hide EP18_Benny_Anim_30
            $ different_choice_menu = False
            pass
    scene 48-5 ben 92 with Dissolve(0.5)
    a "OHHH!!!"
    b1 "YEEEHAAW!"
    scene 48-5 ben 93 with Dissolve(0.5)
    a "OH... FUCk... Yes... Yesss....!"
    a "FUCK... FUCKK!!!!"
    b1 "Looks like you're brain is getting fried from my cock?!"
    scene 48-5 ben 94 with Dissolve(0.5)
    b1 "YEAH!"
    b1 "You dirty girl!"
    b1 "You like when a homeless man fucks your brains out?"
    a "OHHH... Yes!"
    menu:
        "I'll stick to fucking her pussy!":
            pass
            $ different_choice_menu = True
            $ EP18_Anim_Option = 1
            $ EP18_Anim_Speed = 1
            scene black
            play sound jerk loop
            show EP18_Benny_Anim_35 with Dissolve(0.5)
            label EP18_Benny_Sex_Label_8:
            $ different_choice_menu = True
            a "SO big... So big... So big..."
            play audio female_moan_5
            a "FFFFFUUCK!"
            menu EP18_Benny_Anim_Menu_8:
                "View 1":
                    hide EP18_Benny_Anim_35
                    hide EP18_Benny_Anim_36
                    hide EP18_Benny_Anim_37
                    hide EP18_Benny_Anim_38
                    $ EP18_Anim_Option = 1
                    if EP18_Anim_Speed == 1:
                        show EP18_Benny_Anim_35 with Dissolve(0.5)
                    if EP18_Anim_Speed == 2:
                        show EP18_Benny_Anim_36 with Dissolve(0.5)
                    jump EP18_Benny_Anim_Menu_8
                "View 2":
                    hide EP18_Benny_Anim_35
                    hide EP18_Benny_Anim_36
                    hide EP18_Benny_Anim_37
                    hide EP18_Benny_Anim_38
                    $ EP18_Anim_Option = 2
                    if EP18_Anim_Speed == 1:
                        show EP18_Benny_Anim_37 with Dissolve(0.5)
                    elif EP18_Anim_Speed == 2:
                        show EP18_Benny_Anim_38 with Dissolve(0.5)
                    jump EP18_Benny_Anim_Menu_8
                "Slower":
                    hide EP18_Benny_Anim_35
                    hide EP18_Benny_Anim_36
                    hide EP18_Benny_Anim_37
                    hide EP18_Benny_Anim_38
                    $ EP18_Anim_Speed = 1
                    if EP18_Anim_Option == 1:
                        show EP18_Benny_Anim_35 with Dissolve(0.5)
                    elif EP18_Anim_Option == 2:
                        show EP18_Benny_Anim_37 with Dissolve(0.5)
                    jump EP18_Benny_Anim_Menu_8
                "Faster":
                    hide EP18_Benny_Anim_35
                    hide EP18_Benny_Anim_36
                    hide EP18_Benny_Anim_37
                    hide EP18_Benny_Anim_38
                    $ EP18_Anim_Speed = 2
                    if EP18_Anim_Option == 1:
                        show EP18_Benny_Anim_36 with Dissolve(0.5)
                    elif EP18_Anim_Option == 2:
                        show EP18_Benny_Anim_38 with Dissolve(0.5)
                    jump EP18_Benny_Anim_Menu_8
                "Continue":
                    hide EP18_Benny_Anim_35
                    hide EP18_Benny_Anim_36
                    hide EP18_Benny_Anim_37
                    hide EP18_Benny_Anim_38
                    $ different_choice_menu = False
                    pass
            show EP18_Benny_Anim_38 with Dissolve(0.5)
        "Put it in Anna's asshole!":
            scene 48-5 ben 95 with Dissolve(0.5)
            a "Put it in my ass."
            b1 "What?"
            a "PUT. IT. In MY FUCKING ASSHOLE!"
            a "I NEED IT!"
            scene 48-5 ben 96 with Dissolve(0.5)
            b1 "You're the nastiest piece of ass I know."
            b1 "I will do as you wish!"
            scene 48-5 ben 97 with Dissolve(0.5)
            a "Good... Ahh..."
            scene 48-5 ben 98 with Dissolve(0.5)
            pause 1
            scene 48-5 ben 99 with Dissolve(0.5)
            pause 1
            scene 48-5 ben 100 with Dissolve(0.5)
            a "AAHHH!"
            b1 "DAMN!"
            b1 "SO TIGHT!"
            b1 "Almost need some vaseline!"
            b1 "But all the juices from your ass are making it all moist down there too!"
            $ different_choice_menu = True
            $ EP18_Anim_Option = 1
            $ EP18_Anim_Speed = 1
            scene black
            play sound jerk loop
            show EP18_Benny_Anim_31 with Dissolve(0.5)
            label EP18_Benny_Sex_Label_9:
            a "SO big... So big... So big..."
            play audio female_moan_5
            a "FFFFFUUCK!"
            menu EP18_Benny_Anim_Menu_9:
                "View 1":
                    hide EP18_Benny_Anim_31
                    hide EP18_Benny_Anim_32
                    hide EP18_Benny_Anim_33
                    hide EP18_Benny_Anim_34
                    $ EP18_Anim_Option = 1
                    if EP18_Anim_Speed == 1:
                        show EP18_Benny_Anim_31 with Dissolve(0.5)
                    if EP18_Anim_Speed == 2:
                        show EP18_Benny_Anim_32 with Dissolve(0.5)
                    jump EP18_Benny_Anim_Menu_9
                "View 2":
                    hide EP18_Benny_Anim_31
                    hide EP18_Benny_Anim_32
                    hide EP18_Benny_Anim_33
                    hide EP18_Benny_Anim_34
                    $ EP18_Anim_Option = 2
                    if EP18_Anim_Speed == 1:
                        show EP18_Benny_Anim_33 with Dissolve(0.5)
                    elif EP18_Anim_Speed == 2:
                        show EP18_Benny_Anim_34 with Dissolve(0.5)
                    jump EP18_Benny_Anim_Menu_9
                "Slower":
                    hide EP18_Benny_Anim_31
                    hide EP18_Benny_Anim_32
                    hide EP18_Benny_Anim_33
                    hide EP18_Benny_Anim_34
                    $ EP18_Anim_Speed = 1
                    if EP18_Anim_Option == 1:
                        show EP18_Benny_Anim_31 with Dissolve(0.5)
                    elif EP18_Anim_Option == 2:
                        show EP18_Benny_Anim_33 with Dissolve(0.5)
                    jump EP18_Benny_Anim_Menu_9
                "Faster":
                    hide EP18_Benny_Anim_31
                    hide EP18_Benny_Anim_32
                    hide EP18_Benny_Anim_33
                    hide EP18_Benny_Anim_34
                    $ EP18_Anim_Speed = 2
                    if EP18_Anim_Option == 1:
                        show EP18_Benny_Anim_32 with Dissolve(0.5)
                    elif EP18_Anim_Option == 2:
                        show EP18_Benny_Anim_34 with Dissolve(0.5)
                    jump EP18_Benny_Anim_Menu_9
                "Continue":
                    hide EP18_Benny_Anim_31
                    hide EP18_Benny_Anim_32
                    hide EP18_Benny_Anim_33
                    hide EP18_Benny_Anim_34
                    $ different_choice_menu = False
                    pass
            scene 48-5 ben 101 with Dissolve(0.5)
            a "Keep fucking me..."
            a "Keep fucking me, you dirty, dirty man!"
            b1 "HEHE... YES!"
            b1 "You like getting your ass filled up, don't you?"
            a "MHM!!!"
            scene 48-5 ben 102 with Dissolve(0.5)
            a "OH... GOD!"
            b1 "YES, YES!"
            scene 48-5 ben 103 with Dissolve(0.5)
            b1 "Perfect!"
            b1 "AHH!"
            a "OOHH!!!"
            show EP18_Benny_Anim_34 with Dissolve(0.5)
            menu:
                "Put it back into Anna's pussy?":
                    show EP18_Benny_Anim_38 with Dissolve(0.5)
                    hide EP18_Benny_Anim_34
                    jump EP18_Benny_Sex_Label_8
                "CUMMM!!!":
                    pass
    menu:
        "Cum on Anna's belly!":
            b1 "I'm ABOUT TO BUUUST!"
            a "COME ON!"
            play audio moaninglong_1
            a "SHOOT IT ALL OVER MY BODY!"
            b1 "YES, bitch!"
            a "That's right... Paint your bitch!"
            b1 "AHAHHAAA!!!!"
            with flash
            play sound cum_sound
            scene 48-5 ben 114 with flash_vpunch
            b1 "HAAA!"
            with flash_vpunch
            b1 "YAAAHHAAA!"
            with flash_vpunch
            b1 "HUUAAAAAHHAAA!"
            scene 48-5 ben 115 with Dissolve(0.5)
            b1 "SHAIZE!"
            b1 "FUCK!"
            scene 48-5 ben 116 with Dissolve(0.5)
            a "OH wow..."
            a "You're still hard?"
            b1 "I am... Not for long... But..."
        "Fill that vagina up!":
            b1 "FUCK!"
            b1 "ANNA!"
            play audio moaninglong_1
            b1 "I'm closing in!!!!"
            a "THEN DON'T STOP!"
            a "CUM!"
            with flash
            a "GIVE IT ALL TO ME!"
            play sound cum_sound
            scene 48-5 ben 111 with flash_vpunch
            b1 "AAAaaaaaAAAAAAaaaaAAAHHHAaaaaAA!!!"
            play sound cum_sound
            with flash
            with flash
            b1 "YAAEEAEAAHHH!!!!"
            b1 "FUCKING DAAAAM!"
            with flash
            scene 48-5 ben 112 with Dissolve(0.5)
            b1 "All in the cum drain!"
            a "YES!"
            scene 48-5 ben 113 with Dissolve(0.5)
            b1 "Fucking DAMN!"
            a "I can feel it all inside me!"
            scene 48-5 ben 116 with Dissolve(0.5)
            a "OH wow..."
            a "You're still hard?"
            b1 "I am... Not for long... But..."
        "Give her asshole all that cum!":
            scene 48-5 ben 104 with Dissolve(0.5)
            b1 "FUCK!"
            play audio moaninglong_1
            b1 "I'm... GETTING CLOSE!"
            b1 "FUCKK!"
            b1 "HERE I!"
            scene 48-5 ben 105 with Dissolve(0.5)
            b1 "COMMEEEE!!!!"
            b1 "AAAHHHHAAAA!!!"
            play sound cum_sound
            scene 48-5 ben 106 with flash_vpunch
            a "AOHHH!"
            play sound cum_sound
            with vpunch
            b1 "YAH!"
            play sound cum_sound
            with flash
            with flash
            b1 "YAH!"
            b1 "YOOAAHHHHAAA!"
            with flash
            pause
            scene 48-5 ben 107 with Dissolve(0.5)
            b1 "FUCKING DAMN!"
            b1 "THAT ASSHOLE ROCKS!"
            scene 48-5 ben 108 with Dissolve(0.5)
            a "OH wow..."
            a "You're still hard?"
            b1 "I am... Not for long... But..."
    $ different_choice_menu = True
    $ EP18_Anim_Option = 1
    $ EP18_Anim_Speed = 1
    scene 48-5 ben 117 with Dissolve(0.5)
    b1 "Oh... Boy..."
    b1 "I'm lightheaded."
    a "Hehe. You did really work me out."
    scene 48-5 ben 118 with Dissolve(0.5)
    a "And even kept fucking my hole after finishing."
    b1 "I do whatever you command of me, Anna."
    b1 "Hehe."
    b1 "Good!"
    b1 "I feel like I could almost go for more..."
    scene 48-5 ben 119 with Dissolve(0.5)
    a "I don't know if I can take it."
    b1 "Come on. At least while I'm still hard!"
    scene 48-4 ben 129 with Dissolve(0.5)
    b1 "Just for a bit more. Eh?"
    a "Oh... Heh. Fine."
    play sound undress
    scene 48-4 ben 130 with Dissolve(0.5)
    b1 "Oh YEAH!"
    b1 "Girl you got me GOING AGAIN!"
    scene black
    play sound jerk loop
    show EP18_Benny_Anim_41 with Dissolve(0.5)
    label EP18_Benny_Sex_Label_10:
    a "SO big... So big... So big..."
    play audio female_moan_5
    a "FFFFFUUCK!"
    menu EP18_Benny_Anim_Menu_10:
        "View 1":
            hide EP18_Benny_Anim_41
            hide EP18_Benny_Anim_42
            hide EP18_Benny_Anim_43
            hide EP18_Benny_Anim_44
            $ EP18_Anim_Option = 1
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_41 with Dissolve(0.5)
            if EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_42 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_10
        "View 2":
            hide EP18_Benny_Anim_41
            hide EP18_Benny_Anim_42
            hide EP18_Benny_Anim_43
            hide EP18_Benny_Anim_44
            $ EP18_Anim_Option = 2
            if EP18_Anim_Speed == 1:
                show EP18_Benny_Anim_43 with Dissolve(0.5)
            elif EP18_Anim_Speed == 2:
                show EP18_Benny_Anim_44 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_10
        "Slower":
            hide EP18_Benny_Anim_41
            hide EP18_Benny_Anim_42
            hide EP18_Benny_Anim_43
            hide EP18_Benny_Anim_44
            $ EP18_Anim_Speed = 1
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_41 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_43 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_10
        "Faster":
            hide EP18_Benny_Anim_41
            hide EP18_Benny_Anim_42
            hide EP18_Benny_Anim_43
            hide EP18_Benny_Anim_44
            $ EP18_Anim_Speed = 2
            if EP18_Anim_Option == 1:
                show EP18_Benny_Anim_42 with Dissolve(0.5)
            elif EP18_Anim_Option == 2:
                show EP18_Benny_Anim_44 with Dissolve(0.5)
            jump EP18_Benny_Anim_Menu_10
        "Continue":
            hide EP18_Benny_Anim_41
            hide EP18_Benny_Anim_42
            hide EP18_Benny_Anim_43
            hide EP18_Benny_Anim_44
            $ different_choice_menu = False
            pass
    show EP18_Benny_Anim_44 with Dissolve(0.5)
    b1 "AHHH!"
    b1 "AHHHHOHOHO!!!"
    b1 "FUCKING GOOD!"
    a "You coming?"
    b1 "YESS YES!"
    with flash
    with flash
    play sound cum_sound
    scene 48-4 ben 133 with flash_vpunch
    b1 "AAHHHH!!"
    with flash
    with vpunch
    b1 "FUCK.... YEEAAAAAAAAAHHHH!!"
    with flash
    pause 1
    scene 48-4 ben 134 with Dissolve(0.5)
    b1 "Wow..."
    b1 "Another proper load..."
    b1 "You wake a monster in me."
    scene 48-4 ben 135 with Dissolve(0.5)
    a "Wow... My pussy's so sore right now."
    a "I'm still surprised you could go again."
    scene 48-4 ben 136 with Dissolve(0.5)
    b1 "Girl... So am I!"
    scene 48-5 ben 119 with Dissolve(0.5)
    a "Ah."
    a "This was fun."
    b1 "Wow... It was quite something if you ask me."
    a "Indeed, Benjamin."
    a "I will go clean up, ok?"
    scene 48-5 ben 120 with Dissolve(0.5)
    a "Can you stand up?"
    b1 "I don't have the power."
    b1 "I'll probably have the best night's sleep tonight."
    play sound door2
    scene 48-5 ben 121 with Dissolve(0.5)
    a "{i}...He was a beast...{/i}"
    a "{i}...How can such an old man still fuck so hard...{/i}"
    a "{i}...Considering the size of his body in relation to his huge cock...{/i}"
    a "{i}...Wow...{/i}"
    scene black with Dissolve(0.5)
    play sound undress
    pause 1
    scene 48-5 ben 122 with Dissolve(0.5)
    b1 "Hehe... You look great!"
    a "Thanks."
    $ renpy.end_replay()
    scene 48-5 ben 123 with Dissolve(0.5)
    a "Well, well..."
    a "I spy with my little eye a naughty magazine."
    a "With me as the cover girl."
    scene 48-5 ben 124 with Dissolve(0.5)
    a "What is that doing there?"
    b1 "Oh... Heh."
    b1 "Just something to kill the time on long evenings."
    scene 48-5 ben 125 with Dissolve(0.5)
    b1 "You have to understand."
    b1 "I'm your biggest fan!"
    b1 "And... To be able to fuck you!"
    b1 "It's like I live in a fantasy world!"
    a "Hehe."
    scene 48-5 ben 126 with Dissolve(0.5)
    a "Anyway. I'll get going."
    a "I've got other things to do."
    a "Just as important."
    a "Will you be ok?"
    b1 "Oh, yes!"
    b1 "Better than ok!"
    b1 "Everything feels more vibrant, the colors, the sounds."
    b1 "It's like I just had surgery to enhance all my senses."
    scene 48-5 ben 127 with Dissolve(0.5)
    a "Perhaps I'm just a very special doctor. Who helps people get better."
    b1 "Indeed. Hehe..."
    a "See you later, Benny."
    b1 "Goodbye, Anna!"
    scene black with Dissolve(0.5)
    pause 1
    jump EP18_Ruby_1
label EP18_John_1:
    $ EP18_var_5 = True
    play music Chill_Song_1
    if BenjaminContent == False:
        scene 48-4 john 1 with Dissolve(0.5)
        j4 "Anna!"
        j4 "Hey."
        a "Hey, John."
        j4 "How are you doing?"
        scene 48-4 john 2 with Dissolve(0.5)
        a "Pretty good."
        j4 "How was the beach?"
        a "Oh. It was lovely."
        scene 48-4 john 3 with Dissolve(0.5)
        j4 "Wish I could've joined."
        a "Don't take it the wrong way, but I'm glad you didn't."
        a "It was a moment Andrew and I could finally spend together..."
        a "Just the two of us."
        j4 "Oh. OK, OK."
        j4 "Sorry."
        a "It's OK. What you up to?"
        scene 48-4 john 1 with Dissolve(0.5)
        j4 "Just gonna go ride my motorcycle around."
        j4 "Meet with some biker buddies of mine."
        j4 "You wanna join?"
        scene 48-4 john 4 with Dissolve(0.5)
        a "Oh. I'm good, thanks. Kind of tired."
        j4 "Right. Well, your loss, honey."
        scene 48-4 john 5 with Dissolve(0.5)
        a "{i}...Hmm... He mentioned the bikers...{/i}"
        a "{i}...I do need to expand the distribution to sell the 'product' faster...{/i}"
        scene 48-4 john 6 with Dissolve(0.5)
        a "Hold on!"
        a "Sorry, you said ride the motorcycle?"
        j4 "Yeah?"
        a "I misheard you before."
        a "I'd actually like to join you."
        scene 48-4 john 7 with Dissolve(0.5)
        j4 "Sure. you gonna come like this?"
        a "Umm... No."
        a "I'm just quickly going to change."
        scene 48-4 john 8 with Dissolve(0.5)
        a "Something..."
        a "More appropriate. Heh."
        j4 "Can't wait, heh."
        scene black with Dissolve(0.5)
        pause 1
        play sound door2
        scene 48-4 john 9 with Dissolve(0.5)
    else:
        scene 48-4 john 2-1 with Dissolve(0.5)
        j4 "Anna!"
        j4 "Hey."
        a "Hey, John."
        j4 "How are you doing?"
        scene 48-4 john 3-1 with Dissolve(0.5)
        a "Pretty good."
        j4 "What you've been up to?"
        j4 "How was the beach?"
        a "Oh. It was lovely."
        a "I just helped out a friend."
        j4 "Wish I could've joined."
        a "Don't take it the wrong way, but I'm glad you didn't."
        a "It was a moment Andrew and I could finally spend together..."
        a "Just the two of us."
        j4 "Oh. OK, OK."
        j4 "Sorry."
        a "It's OK. What you up to?"
        scene 48-4 john 4-1 with Dissolve(0.5)
        j4 "Just gonna go ride my motorcycle around."
        j4 "Meet with some biker buddies of mine."
        j4 "You wanna join?"
        a "Oh. I'm good, thanks. Kind of tired."
        j4 "Right. Well, your loss, honey."
        scene 48-4 john 5-1 with Dissolve(0.5)
        a "{i}...Hmm... He mentioned the bikers...{/i}"
        a "{i}...I do need to expand the distribution to sell the 'product' faster...{/i}"
        scene 48-4 john 6-1 with Dissolve(0.5)
        a "Hold on!"
        a "Sorry, you said ride the motorcycle?"
        j4 "Yeah?"
        a "I misheard you before."
        a "I'd actually like to join you."
        scene 48-4 john 7-1 with Dissolve(0.5)
        j4 "Sure. you gonna come like this?"
        a "Umm... No."
        a "I'm just quickly going to change."
        scene 48-4 john 8-1 with Dissolve(0.5)
        a "Something..."
        a "More appropriate. Heh."
        j4 "Can't wait, heh."
        scene black with Dissolve(0.5)
        pause 1
        play sound door2
    a "Hmm..."
    a "What would be 'more appropriate'..."
    scene black with Dissolve(0.5)
    pause 1
    play sound undress
    scene 48-4 john 10 with Dissolve(0.5)
    a "Perfect."
    a "This will be very, very persuasive."
    scene 48-4 john 11 with Dissolve(0.5)
    a "And the hair."
    a "A little innocence in the mix."
    scene 48-4 john 12 with Dissolve(0.5)
    a "What do you think?"
    a "This is better?"
    j4 "Huh?"
    scene 48-4 john 13 with Dissolve(0.5)
    j4 "Heh. That's..."
    j4 "You sure?"
    j4 "Quite revealing."
    a "Revealing?"
    a "I thought all biker girls dressed similar to this."
    a "You don't like it? I can change."
    scene 48-4 john 14 with Dissolve(0.5)
    j4 "No, no."
    j4 "It's fine. No need to change, heh."
    a "That's what I thought."
    play sound door2
    scene black with Dissolve(0.5)
    pause 1
    play ambient citytraffic
    scene 48-4 john 15 with Dissolve(0.5)
    a "Wow!"
    a "That's yours?"
    j4 "It is."
    j4 "My baby."
    j4 "Have you been on one before?"
    a "Many years ago."
    scene 48-4 john 16 with Dissolve(0.5)
    a "It's beautiful."
    j4 "Thanks."
    j4 "The love of my life."
    a "The only one?"
    j4 "Heh. Perhaps not..."
    scene 48-4 john 17 with Dissolve(0.5)
    j4 "Hop on."
    a "Just like that?"
    scene 48-4 john 18 with Dissolve(0.5)
    j4 "What of it?"
    a "What about helmets?"
    j4 "Will be fine, not a long ride anyway."
    scene 48-4 john 19 with Dissolve(0.5)
    a "You sure?"
    j4 "Definitely, I've learned to control this beauty well."
    a "Hmm. OK."
    scene 48-4 john 20 with Dissolve(0.5)
    j4 "Just hold on tight!"
    a "OK! Hah!"
    scene black with Dissolve(0.5)
    pause 1
    play sound motorcycle_sound_1
    scene 48-4 john 21 with Dissolve(0.5)
    pause 1
    scene 48-4 john 22 with Dissolve(0.5)
    pause 1
    a "HAHA!"
    a "This is fun!"
    j4 "FUCK YEAH!"
    play sound motorcycle_sound_1
    scene 48-4 john 23 with Dissolve(0.5)
    j4 "Wanna go faster?"
    a "You sure we should?"
    j4 "Oh yeah!"
    scene 48-4 john 24 with Dissolve(0.5)
    a "AAHHH!!"
    j4 "Haha! Don't worry!"
    scene black with Dissolve(0.5)
    pause 1
    scene 48-4 john 25 with Dissolve(0.5)
    j4 "Alright. We're here."
    scene 48-4 john 26 with Dissolve(0.5)
    j4 "This is the bar where we usually meet."
    a "You and the bikers?"
    j4 "Yeah."
    j4 "Our hang-out spot."
    scene 48-4 john 27 with Dissolve(0.5)
    j4 "You sure you're gonna be OK?"
    a "What do you mean?"
    j4 "The outfit."
    j4 "They can be a rowdy bunch."
    a "Heh, yeah. I will be fine."
    scene 48-4 john 28 with Dissolve(0.5)
    a "{i}...I think I've been here before, though.{/i}"
    j4 "C'mon. Let's go."
    scene black with Dissolve(0.5)
    pause 1
    stop ambient
    play sound door2
    play music barsong
    scene 48-4 john 29 with Dissolve(0.5)
    a "Hmm..."
    scene 48-4 john 30 with Dissolve(0.5)
    j4 "You good?"
    a "Uh. what?"
    a "Yeah, yeah."

    scene 48-4 john 31 with Dissolve(0.5)
    a "Never better. hehe."
    j4 "You seem a bit lost in thought."
    a "Oh. Heh. Maybe a little."
    scene 48-4 john 32 with Dissolve(0.5)
    j4 "Guys."
    bi1 "John."
    bi2 "What's up, wood."
    j4 "You doing well?"
    scene 48-4 john 33 with Dissolve(0.5)
    bi2 "Pretty alright, all things considered."
    bi2 "Going for round two."
    j4 "That's my boy, haha!"
    scene 48-4 john 34 with Dissolve(0.5)
    menu:
        "Anna has had previous 'engagements' with these two.":
            $ EP18_Bikers_History = True
            a "Hello there."
            bi2 "Well, well. Heh."
            bi2 "Been a while since I've seen you around, Anna."
            j4 "Huh?"
            scene 48-4 john 35 with Dissolve(0.5)
            j4 "You know her?"
            bi2 "We know of each other, yeah."
            j4 "Interesting. Heh."
            scene 48-4 john 36 with Dissolve(0.5)
            j4 "Didn't know you were a regular in these parts."
            a "Not a local, no."
            a "Just had an occasion here."
            j4 "Alright, alright."
        "Anna is not involved with them.":
            a "Hello there."
            bi2 "Heh, hey, back to you."
            bi2 "Who's this?"
            scene 48-4 john 35 with Dissolve(0.5)
            j4 "A friend. heh."
            bi2 "A beautiful one."
            j4 "Alright, alright."
            pass
    scene 48-4 john 37 with Dissolve(0.5)
    bi2 "We were about to get our third round."
    bi2 "You guys in or out?"
    a "At this time of the day?"
    bi2 "It's weekend."
    j4 "We'll join you, of course!"
    scene 48-4 john 38 with Dissolve(0.5)
    j4 "Hey, Jill."
    barji1 "John! Good to see you here."
    barji1 "You doing good?"
    barji1 "Heard you guys got pretty rowdy yesterday."
    j4 "Always, haha."
    scene 48-4 john 39 with Dissolve(0.5)
    barji1 "What can I get you two?"
    j4 "Give us two Venebera IPAs."
    barji1 "Coming right up!"
    scene 48-4 john 40 with Dissolve(0.5)
    a "You sure we should?"
    a "How will you ride the bike?"
    j4 "C'mon. One drink won't do any harm."
    j4 "Trust me."
    j4 "We drive better with one beer inside."
    scene 48-4 john 41 with Dissolve(0.5)
    barji1 "There you go."
    j4 "Thanks, Jill."
    j4 "Say hi to Monica from me."
    barji1 "Will do, hehe."
    scene 48-4 john 42 with Dissolve(0.5)
    j4 "Mmm... I can almost feel the taste..."
    scene 48-4 john 43 with Dissolve(0.5)
    j4 "You know, we have a saying around here."
    a "What do you mean?"
    j4 "When we drink."
    j4 "The rest of the bikers are not around, but it's sort of our motto."
    scene 48-4 john 44 with Dissolve(0.5)
    j4 "Ride or die, and when you die, you'll ride forever!"
    j4 "It's a life we choose, cheers!"
    a "Hehe. Cheers!"
    j4 "One more thing. Bottoms up."
    play sound drinkingBeverage
    scene 48-4 john 45 with Dissolve(0.5)
    pause 1
    scene 48-4 john 46 with Dissolve(0.5)
    bi1 "It's good, isn't it hehe?"
    a "It's... Umm... Whoa... Hehe."
    bi2 "A bit too fast. We got a lightweight here, Haha."
    bi1 "C'mon, give her a break man."
    scene 48-4 john 47 with Dissolve(0.5)
    bi2 "We're gonna go outside for a smoke."
    bi2 "You guys coming?"
    scene 48-4 john 48 with Dissolve(0.5)
    a "Why not."
    scene black with Dissolve(0.5)
    pause 1
    scene 48-4 john 49 with Dissolve(0.5)
    bi1 "You smoke?"
    a "Uhh..."
    a "I don't."
    bi1 "Suit yourself."
    bi2 "By the way, John."
    bi2 "We got that package for you."
    bi2 "Our boy retrieved it from the stolen vehicle."
    scene 48-4 john 50 with Dissolve(0.5)
    j4 "Uh... Heh."
    j4 "He's joking around."
    j4 "No stolen vehicles here."
    scene 48-4 john 51 with Dissolve(0.5)
    bi2 "Hehe..."
    bi2 "Oh, Johnny boy."
    bi2 "If only you knew."
    scene 48-4 john 52 with Dissolve(0.5)
    j4 "What are you talking about?"
    scene 48-4 john 53 with Dissolve(0.5)
    if EP18_Bikers_History == True:
        bi1 "We've met this girl before."
        bi1 "We know some stuff about her."
        j4 "Meaning?"
        bi1 "She's not exactly an angel either."
        bi1 "Into some shady shit, just as we are."
        bi1 "So no point in playing saint."
    else:
        bi1 "We may not have met her before..."
        bi1 "But our contacts have."
        j4 "What do you mean?"
        bi1 "She's not exactly an angel either."
        bi1 "Into some shady shit, just as we are."
        bi1 "So no point in playing saint."
    scene 48-4 john 54 with Dissolve(0.5)
    j4 "Anna?"
    a "Oh..."
    bi1 "Oh, yeah, dude."
    bi1 "She's into some criminal shit, same as us."
    play music tense2
    scene 48-4 john 55 with Dissolve(0.5)
    j4 "Seriously?"
    j4 "Are they joking?"
    bi1 "Just tell her, Anna."
    a "I... Well..."
    a "I'm... I've done some shady stuff, yeah."
    scene 48-4 john 56 with Dissolve(0.5)
    j4 "Wow."
    j4 "I didn't expect that at all."
    j4 "I thought she was just an office lady."
    bi2 "Been living under a rock, John."
    scene 48-4 john 57 with Dissolve(0.5)
    bi2 "She's been seen doing work Sergey for 'The Bear.'"
    j4 "WHAT?"
    j4 "Wait."
    scene 48-4 john 58 with Dissolve(0.5)
    j4 "Why did you come here?"
    j4 "Was it on 'business'?"
    a "Well..."
    j4 "Wow."
    j4 "Alright, the less I know, the better."
    scene 48-4 john 59 with Dissolve(0.5)
    a "I did come with some proposals... I won't hide it anymore."
    a "But It's between them and me..."
    j4 "Damn... I'm perplexed, to be honest."
    j4 "You know what?"
    scene 48-4 john 60 with Dissolve(0.5)
    j4 "I really don't want to be a part of this whole ordeal. I'll just go recover the package."
    j4 "Meanwhile, you can deal with your business."
    scene 48-4 john 61 with Dissolve(0.5)
    if EP18_Bikers_History == True:
        bi2 "I still remember our previous 'encounter.'"
        bi1 "Hah. Yeah."
        bi2 "It was pretty 'interesting.'"
        scene 48-4 john 62 with Dissolve(0.5)
        a "Oh c'mon. That was a while ago."
        a "Besides, it wasn't a big deal."
        bi2 "Oh really?"
        scene 48-4 john 63 with Dissolve(0.5)
        bi2 "Still fresh in my mind."
        bi2 "Kind of seemed like a big deal."
        bi1 "He's right, you've got a big deal in the back."
        a "Anyway. snap back."
    a "I'm here to discuss business."
    a "I know what you guys do and..."
    a "I've got some product."
    scene 48-4 john 62 with Dissolve(0.5)
    a "I'm looking for new distribution."
    bi2 "And you've come to us..."
    bi2 "What makes you think we'd deal with you."
    bi2 "We're doing just fine without new involvements."
    scene 48-4 john 64 with Dissolve(0.5)
    a "Fine..."
    a "I hadn't even gotten to the best bit..."
    a "But if you'll shut me down before I've shown you how good the product is..."
    a "Then I'm out."
    scene 48-4 john 65 with Dissolve(0.5)
    bi2 "Wait, wait."
    bi2 "Alright."
    bi2 "I'm just joking around."
    scene 48-4 john 66 with Dissolve(0.5)
    bi2 "We can hear you out."
    bi2 "Since you used to work for Sergey."
    a "Oh, now you want to play ball?"
    bi2 "Yeah. show us the product."
    scene 48-4 john 67 with Dissolve(0.5)
    bi2 "Who are you calling?"
    a "C'mon."
    a "I worked for Sergey. You think I'd just walk around with a pound of cocaine?"
    a "I got my contacts, my safe locations."
    a "Not my first rodeo."
    bi2 "Damn."
    "..."
    a "Hey!"
    a "You on the spot?"
    m2 "Yeah. What's up?"
    scene 48-4 john 68 with Dissolve(0.5)
    a "Meet me near your house. I need some product."
    m2 "Alright, girl."
    m2 "Got some ready to go."
    bi1 "She's for real, sounds like."
    a "I'll be there in five."
    m2 "Got it."
    scene 48-4 john 69 with Dissolve(0.5)
    a "See. I'm not some amateur."
    a "Trust me when I say that this could be very beneficial."
    bi1 "Sure, sure. Obviously, we'll want to test it out."
    a "Why do you think I'm going to meet my contact now?"
    scene 48-4 john 70 with Dissolve(0.5)
    a "I'll be back in a while. Don't go anywhere."
    bi2 "You got some balls, girl."
    bi2 "Respect."
    a "Hehe..."
    scene 48-4 john 71 with Dissolve(0.5)
    bi1 "Among other things..."
    scene black with Dissolve(0.5)
    pause 1
    scene 48-4 john 72 with Dissolve(0.5)
    m2 "Anna."
    m2 "What's up?"
    m2 "Looking good!"
    scene 48-4 john 73 with Dissolve(0.5)
    m2 "What do you need the product for?"
    a "I'm out working, getting distribution contacts. Need a package of your finest."
    m2 "Already ready."
    scene 48-4 john 74 with Dissolve(0.5)
    m2 "Gotta say."
    m2 "You've been really putting in work."
    a "Eh. You don't know the half of it."
    if EarlHelp == False:
        m2 "Well. Sergey hasn't really explained everything to me."
        a "Yeah, he's a lot more cautious."
        m2 "All I know is I gotta hustle double now."
        m2 "And keep my eyes peeled for Carl."
        a "Yeah..."
    else:
        m2 "I don't really know a lot."
        m2 "Just some bits that you've told me."
        m2 "All I know is I gotta hustle double now."
        m2 "And keep my eyes peeled for Carl."
        a "Yeah..."
        a "Things will get more clear in the future."
        m2 "I'm trusting you on this one, Anna."
    scene 48-4 john 75 with Dissolve(0.5)
    a "Anyway."
    scene 48-4 john 76 with Dissolve(0.5)
    m2 "Here's the stuff, as asked."
    a "A whole package?"
    m2 "Exactly."
    scene 48-4 john 77 with Dissolve(0.5)
    a "Thanks, Michael."
    a "You're awesome."
    a "If I can land this deal, that should really speed things up for us."
    m2 "But you owe me some answers."
    m2 "OK?"
    scene 48-4 john 78 with Dissolve(0.5)
    a "You got it."
    a "I'll tell you everything."
    m2 "Good luck, girl."
    scene black with Dissolve(0.5)
    pause 1
    scene 48-4 john 79 with Dissolve(0.5)
    bi2 "Well, well."
    a "You doubted me?"
    bi2 "Not for a second, hehe."
    scene 48-4 john 80 with Dissolve(0.5)
    a "I've got the stuff."
    a "If you want to test it out."
    a "Trust me, this shit is good."
    a "Not some diluted off-brand bullshit a lot of other places are selling."
    scene 48-4 john 81 with Dissolve(0.5)
    bi2 "Hmm."
    bi2 "I'll be the judge of that."
    a "Go right ahead."
    scene 48-4 john 82 with Dissolve(0.5)
    bi2 "That's a big tester."
    a "I know. We've got plenty more where that came from."
    a "Consider this an 'onboarding' gift."
    scene 48-4 john 83 with Dissolve(0.5)
    bi2 "Spoken like a true 'office lady.'"
    bi2 "As John put it."
    a "I have my moments, hehe."
    bi2 "Alright, be back in a sec."
    scene 48-4 john 84 with Dissolve(0.5)
    bi1 "You're not scared he'll just disappear with the stuff."
    a "He may. But then we'll just blacklist your entire organization."
    a "And that's the last of our cocaine he and anyone he's affiliated with will see."
    bi1 "Impressive."
    scene 48-4 john 85 with Dissolve(0.5)
    bi1 "Don't take it as a threat, but you should be more careful."
    a "From what?"
    bi1 "Big hulking dudes."
    a "You'll harm me?"
    a "You do know what happens to you if you harm a negotiator."
    bi1 "You talk big, but can you back it up?"
    a "I used to work for Sergey. Guess who He worked for..."
    bi1 "I always thought he was the big dog."
    a "Trust me, he is simply a pawn. And if that crazy man was the pawn, imagine who's at the top."
    scene 48-4 john 86 with Dissolve(0.5)
    bi1 "Khem..."
    bi1 "Um... Nice outfit."
    a "Hehe... Thought you'd come to your senses."
    a "And thank you."
    a "I picked it out specifically for this occasion."
    bi1 "We so special?"
    scene 48-4 john 87 with Dissolve(0.5)
    a "If you help me distribute this product, you will be very... Very special."
    bi1 "Hehe..."
    bi1 "They definitely found a good negotiator."
    a "I'm pretty good at convincing people. Stick around, and you'll find out why."
    scene 48-4 john 88 with Dissolve(0.5)
    bi2 "{b}*Sniff*{/b}"
    scene 48-4 john 90 with Dissolve(0.5)
    bi2 "{b}*Sniff*{/b}"
    bi2 "{b}*Sniff*{/b}"
    bi2 "Damn."
    scene 48-4 john 91 with Dissolve(0.5)
    bi2 "She's fucking right."
    bi2 "This shit is like gold dust."
    bi2 "Haven't had a hit like this since our party in Fort Bailey Glade."
    bi1 "That good?"
    bi2 "Oh yeah. It's fucking POWERFUL!"
    scene 48-4 john 92 with Dissolve(0.5)
    a "I'm a woman of my word."
    bi2 "You weren't lying... Damn..."
    scene 48-4 john 93 with Dissolve(0.5)
    bi2 "Alright. You win."
    bi2 "We'll sell this stuff."
    bi2 "But... There's the question of percentages."
    a "80:20"
    bi2 "60:40"
    a "Hmm..."
    scene 48-4 john 94 with Dissolve(0.5)
    menu:
        "65:35, and I'll let you touch me and show you something.":
            play music SexyTimeSong7
            bi2 "Oh... What you've got in mind?"
            scene 48-4 john 95 with Dissolve(0.5)
            a "Well... I know everyone likes my melons."
            if EP18_Bikers_History == True:
                a "And I bet you'd want to see them again."
            else:
                a "And I bet you'd LOVE to see them."
            scene 48-4 john 96 with Dissolve(0.5)
            bi1 "For 5%%. Why not. Not a big deal."
            a "Hehe..."
            a "Good."
            scene 48-4 john 97 with Dissolve(0.5)
            bi2 "I'm starting to see why you're the negotiator."
            a "Indeed. I do have a particular set of skills. Don't I?"
            bi2 "Oh yeah."
            scene 48-4 john 98 with Dissolve(0.5)
            bi2 "These are fucking nice."
            a "C'mon."
            a "You can do more."
            scene 48-4 john 99 with Dissolve(0.5)
            a "{i}...Men... Show them boobs, and they forget about percentages...{/i}"
            a "{i}...What if I pushed for more...{/i}"
            play sound undress
            scene 48-4 john 100 with Dissolve(0.5)
            bi2 "Whoa..."
            bi2 "That's quite something."
            a "I told you."
            scene 48-4 john 101 with Dissolve(0.5)
            a "..."
            menu:
                "75:25, and You can go all the way.":
                    $ persistent.scene_53 = True
                    label EP18_Bikers_Sex_Scene_Label_Gallery:
                    $ renpy.music.play("audio/sounds/ikoliks - Need You Tonight.mp3", channel = 'music', if_changed = True)
                    $ EP18_Bikers_75_Percent = True
                    a "Trust me. I'm part of the benefits... If you go this direction."
                    a "A reoccurring privilege..."
                    bi2 "Really?"
                    bi2 "Well..."
                    bi2 "Heh..."
                    scene 48-4 john 102 with Dissolve(0.5)
                    bi2 "You've got a deal, babe."
                    a "I knew I could persuade you."
                    a "Trust me, you won't be disappointed."
                    scene 48-4 john 103 with Dissolve(0.5)
                    bi1 "This will be fucking good."
                    a "Oh, you can count on that, big boy."
                    scene 48-4 john 104 with Dissolve(0.5)
                    pause 1
                    play sound undress
                    scene 48-4 john 105 with Dissolve(0.5)
                    pause 1
                    scene 48-4 john 106 with Dissolve(0.5)
                    a "C'mon."
                    a "Go ahead."
                    a "I know you want to."
                    scene 48-4 john 107 with Dissolve(0.5)
                    pause 1
                    scene 48-4 john 108 with Dissolve(0.5)
                    bi1 "Nice!"
                    bi1 "That's what I like to see."
                    a "You are allowed to do more than just look."
                    bi1 "OH YEAH!"
                    scene 48-4 john 109 with Dissolve(0.5)
                    a "AAH!"
                    a "Oh..."
                    scene 48-4 john 110 with Dissolve(0.5)
                    bi1 "Looks like you're enjoying those fingers."
                    bi1 "Moist already."
                    a "Always ready to negotiate... Hehe."
                    bi1 "That's apparent, indeed."
                    scene 48-4 john 111 with Dissolve(0.5)
                    a "Oh."
                    play sound ripcloth
                    scene 48-4 john 112 with Dissolve(0.5)
                    pause
                    scene 48-4 john 113 with Dissolve(0.5)
                    bi1 "Nice!"
                    a "Mhm."
                    a "Keep doing that!"
                    scene 48-4 john 114 with Dissolve(0.5)
                    a "Aah... I believe that 75:25 is a good deal, considering other 'benefits' you are getting."
                    bi2 "You sound more and more convincing every second."
                    scene 48-4 john 115 with Dissolve(0.5)
                    bi2 "C'mon."
                    bi2 "Time to earn your keep!"
                    a "I could tell you the same thing."
                    a "If you fail to give me a good fucking..."
                    a "I might have to look elsewhere."
                    scene 48-4 john 116 with Dissolve(0.5)
                    bi2 "Oh Heh."
                    bi2 "You'll enjoy this, I promise!"
                    a "I better!"
                    bi2 "You are a good slut, you know that?"
                    a "Mhmmm."
                    scene 48-4 john 117 with Dissolve(0.5)
                    a "OH!"
                    a "C'mon. Give me what I want!"
                    bi2 "Fuck you are so good!"
                    play sound female_moan_3
                    scene 48-4 john 118 with Dissolve(0.5)
                    a "AAHHHAA!!!"
                    bi2 "OOHHH YEAH!!!"
                    play sound female_moan_1
                    bi2 "THAT PUSSY FUCKING SLAPS!"
                    bi2 "You're so FUCKING WET!"
                    $ different_choice_menu = True
                    $ EP18_Anim_Option = 1
                    $ EP18_Anim_Speed = 1
                    scene black
                    play sound jerk loop
                    show EP18_Biker_Anim_1 with Dissolve(0.5)
                    label EP18_Biker_Sex_Label_1:
                    bi2 "OH shit!"
                    bi2 "THIS SHIT IS GOOD AS FUCK!"
                    play audio female_moan_5
                    a "MHMMM..."
                    menu EP18_Biker_Anim_Menu_1:
                        "View 1":
                            hide EP18_Biker_Anim_1
                            hide EP18_Biker_Anim_2
                            hide EP18_Biker_Anim_3
                            hide EP18_Biker_Anim_4
                            $ EP18_Anim_Option = 1
                            if EP18_Anim_Speed == 1:
                                show EP18_Biker_Anim_1 with Dissolve(0.5)
                            if EP18_Anim_Speed == 2:
                                show EP18_Biker_Anim_2 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_1
                        "View 2":
                            hide EP18_Biker_Anim_1
                            hide EP18_Biker_Anim_2
                            hide EP18_Biker_Anim_3
                            hide EP18_Biker_Anim_4
                            $ EP18_Anim_Option = 2
                            if EP18_Anim_Speed == 1:
                                show EP18_Biker_Anim_3 with Dissolve(0.5)
                            elif EP18_Anim_Speed == 2:
                                show EP18_Biker_Anim_4 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_1
                        "Slower":
                            hide EP18_Biker_Anim_1
                            hide EP18_Biker_Anim_2
                            hide EP18_Biker_Anim_3
                            hide EP18_Biker_Anim_4
                            $ EP18_Anim_Speed = 1
                            if EP18_Anim_Option == 1:
                                show EP18_Biker_Anim_1 with Dissolve(0.5)
                            elif EP18_Anim_Option == 2:
                                show EP18_Biker_Anim_3 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_1
                        "Faster":
                            hide EP18_Biker_Anim_1
                            hide EP18_Biker_Anim_2
                            hide EP18_Biker_Anim_3
                            hide EP18_Biker_Anim_4
                            $ EP18_Anim_Speed = 2
                            if EP18_Anim_Option == 1:
                                show EP18_Biker_Anim_2 with Dissolve(0.5)
                            elif EP18_Anim_Option == 2:
                                show EP18_Biker_Anim_4 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_1
                        "Continue":
                            hide EP18_Biker_Anim_1
                            hide EP18_Biker_Anim_2
                            hide EP18_Biker_Anim_3
                            hide EP18_Biker_Anim_4
                            $ different_choice_menu = False
                            pass
                    scene 48-4 john 119 with Dissolve(0.5)
                    a "AH!"
                    a "OOHHAAAA!"
                    play sound female_moan_2
                    a "AHHHH!!!!"
                    bi1 "I feel like that mouth oughta do some work."
                    scene 48-4 john 122 with Dissolve(0.5)
                    bi1 "Oh yeah!"
                    play audio femmoan_3
                    a "Mmm..."
                    play sound licking_2
                    bi1 "Wish every negotiation went like this."
                    bi2 "Haha. damn straight."
                    scene 48-4 john 123 with Dissolve(0.5)
                    a "KHHAAAA!"
                    bi1 "OH YEAH!"
                    bi1 "Such a good mouth."
                    $ different_choice_menu = True
                    $ EP18_Anim_Option = 1
                    $ EP18_Anim_Speed = 1
                    scene black
                    play sound jerk loop
                    show EP18_Biker_Anim_5 with Dissolve(0.5)
                    label EP18_Biker_Sex_Label_2:
                    bi1 "That mouth WORKING!"
                    a "Hmmph..."
                    menu EP18_Biker_Anim_Menu_2:
                        "View 1":
                            hide EP18_Biker_Anim_5
                            hide EP18_Biker_Anim_6
                            hide EP18_Biker_Anim_17
                            hide EP18_Biker_Anim_18
                            $ EP18_Anim_Option = 1
                            if EP18_Anim_Speed == 1:
                                show EP18_Biker_Anim_5 with Dissolve(0.5)
                            if EP18_Anim_Speed == 2:
                                show EP18_Biker_Anim_6 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_2
                        "View 2":
                            hide EP18_Biker_Anim_5
                            hide EP18_Biker_Anim_6
                            hide EP18_Biker_Anim_17
                            hide EP18_Biker_Anim_18
                            $ EP18_Anim_Option = 2
                            if EP18_Anim_Speed == 1:
                                show EP18_Biker_Anim_17 with Dissolve(0.5)
                            elif EP18_Anim_Speed == 2:
                                show EP18_Biker_Anim_18 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_2
                        "Slower":
                            hide EP18_Biker_Anim_5
                            hide EP18_Biker_Anim_6
                            hide EP18_Biker_Anim_17
                            hide EP18_Biker_Anim_18
                            $ EP18_Anim_Speed = 1
                            if EP18_Anim_Option == 1:
                                show EP18_Biker_Anim_5 with Dissolve(0.5)
                            elif EP18_Anim_Option == 2:
                                show EP18_Biker_Anim_17 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_2
                        "Faster":
                            hide EP18_Biker_Anim_5
                            hide EP18_Biker_Anim_6
                            hide EP18_Biker_Anim_17
                            hide EP18_Biker_Anim_18
                            $ EP18_Anim_Speed = 2
                            if EP18_Anim_Option == 1:
                                show EP18_Biker_Anim_6 with Dissolve(0.5)
                            elif EP18_Anim_Option == 2:
                                show EP18_Biker_Anim_18 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_2
                        "Continue":
                            hide EP18_Biker_Anim_5
                            hide EP18_Biker_Anim_6
                            hide EP18_Biker_Anim_17
                            hide EP18_Biker_Anim_18
                            $ different_choice_menu = False
                            pass
                    scene 48-4 john 124 with Dissolve(0.5)
                    a "Mmmm.!"
                    bi1 "Fuck!"
                    scene 48-4 john 125 with Dissolve(0.5)
                    bi1 "AAHHH!"
                    bi1 "Take my entire cock!"
                    scene 48-4 john 126 with Dissolve(0.5)
                    bi1 "C'mon girl."
                    bi1 "I gotta test that pussy out."
                    a "OK."
                    scene 48-4 john 127 with Dissolve(0.5)
                    bi1 "Come here."
                    bi1 "Fuuck."
                    bi1 "I can't wait a moment longer."
                    a "Then we have a deal?"
                    bi1 "Yeah, yeah."
                    bi1 "Just ride me, girl."
                    scene 48-4 john 128 with Dissolve(0.5)
                    pause 1
                    scene 48-4 john 129 with Dissolve(0.5)
                    bi1 "WOOW!"
                    bi1 "That looks fucking fantastic!"
                    a "You like it, yeah?"
                    bi1 "Better than anything I've seen before."
                    scene 48-4 john 130 with Dissolve(0.5)
                    a "Hehe."
                    a "Let me give you an enjoyable ride then."
                    bi1 "Fuck YEAH!"
                    play audio femmoan_4
                    scene 48-4 john 131 with Dissolve(0.5)
                    a "AAHHh!"
                    play audio female_moan_2
                    bi1 "FUUUUCK!"
                    play audio femmoan_1
                    scene 48-4 john 132 with Dissolve(0.5)
                    a "OooAAAHHH!"
                    bi1 "SHIIIT!"
                    bi1 "THAT PUSSY DOING GOOD WORK!"
                    scene 48-4 john 133 with Dissolve(0.5)
                    a "FUCK!"
                    a "{i}...So hot... Getting fucked by two random bikers...{/i}"
                    a "{i}...I can't hold my excitement fuck...{/i}"
                    $ different_choice_menu = True
                    $ EP18_Anim_Option = 1
                    $ EP18_Anim_Speed = 1
                    scene black
                    play sound jerk loop
                    show EP18_Biker_Anim_7 with Dissolve(0.5)
                    label EP18_Biker_Sex_Label_3:
                    play audio femmoan_3
                    a "AHHH!"
                    menu EP18_Biker_Anim_Menu_3:
                        "View 1":
                            hide EP18_Biker_Anim_7
                            hide EP18_Biker_Anim_8
                            hide EP18_Biker_Anim_9
                            hide EP18_Biker_Anim_10
                            $ EP18_Anim_Option = 1
                            if EP18_Anim_Speed == 1:
                                show EP18_Biker_Anim_7 with Dissolve(0.5)
                            if EP18_Anim_Speed == 2:
                                show EP18_Biker_Anim_8 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_3
                        "View 2":
                            hide EP18_Biker_Anim_7
                            hide EP18_Biker_Anim_8
                            hide EP18_Biker_Anim_9
                            hide EP18_Biker_Anim_10
                            $ EP18_Anim_Option = 2
                            if EP18_Anim_Speed == 1:
                                show EP18_Biker_Anim_9 with Dissolve(0.5)
                            elif EP18_Anim_Speed == 2:
                                show EP18_Biker_Anim_10 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_3
                        "Slower":
                            hide EP18_Biker_Anim_7
                            hide EP18_Biker_Anim_8
                            hide EP18_Biker_Anim_9
                            hide EP18_Biker_Anim_10
                            $ EP18_Anim_Speed = 1
                            if EP18_Anim_Option == 1:
                                show EP18_Biker_Anim_7 with Dissolve(0.5)
                            elif EP18_Anim_Option == 2:
                                show EP18_Biker_Anim_9 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_3
                        "Faster":
                            hide EP18_Biker_Anim_7
                            hide EP18_Biker_Anim_8
                            hide EP18_Biker_Anim_9
                            hide EP18_Biker_Anim_10
                            $ EP18_Anim_Speed = 2
                            if EP18_Anim_Option == 1:
                                show EP18_Biker_Anim_8 with Dissolve(0.5)
                            elif EP18_Anim_Option == 2:
                                show EP18_Biker_Anim_10 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_3
                        "Continue":
                            hide EP18_Biker_Anim_7
                            hide EP18_Biker_Anim_8
                            hide EP18_Biker_Anim_9
                            hide EP18_Biker_Anim_10
                            $ different_choice_menu = False
                            pass
                    play sound femgasp_1
                    scene 48-4 john 134 with Dissolve(0.5)
                    a "AAHHHAAA!"
                    bi1 "OHH SHIT!"
                    bi1 "FUCK FUCK!"
                    a "MHMM!"
                    scene 48-4 john 135 with Dissolve(0.5)
                    bi2 "C'mon girl. I'm ready to shoot a load."
                    bi2 "Get up against that wall."
                    a "Hehe. OK."
                    scene 48-4 john 136 with Dissolve(0.5)
                    bi2 "You're the hottest bitch in town for sure."
                    bi2 "And the best negotiator I've met."
                    a "Oh I bet."
                    a "Now give me some more of that cock!"
                    scene 48-4 john 137 with Dissolve(0.5)
                    pause 1
                    scene 48-4 john 138 with Dissolve(0.5)
                    a "AAAAAAAA!"
                    a "Yeah!"
                    a "COCK... SO... Good..."
                    scene 48-4 john 139 with Dissolve(0.5)
                    bi2 "I'm going to power fuck you!"
                    bi2 "Give you all that spunk!"
                    bi2 "Fill you up so much!"
                    a "YES PLEASE!"
                    $ different_choice_menu = True
                    $ EP18_Anim_Option = 1
                    $ EP18_Anim_Speed = 1
                    scene black
                    play sound jerk loop
                    show EP18_Biker_Anim_11 with Dissolve(0.5)
                    label EP18_Biker_Sex_Label_4:
                    play audio femmoan_3
                    a "AHHH!"
                    a "YEAH!"
                    bi2 "FUCK THIS SHIT IS GETTING ME GOINNNG!!!"
                    menu EP18_Biker_Anim_Menu_4:
                        "View 1":
                            hide EP18_Biker_Anim_11
                            hide EP18_Biker_Anim_12
                            hide EP18_Biker_Anim_13
                            hide EP18_Biker_Anim_14
                            $ EP18_Anim_Option = 1
                            if EP18_Anim_Speed == 1:
                                show EP18_Biker_Anim_11 with Dissolve(0.5)
                            if EP18_Anim_Speed == 2:
                                show EP18_Biker_Anim_12 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_4
                        "View 2":
                            hide EP18_Biker_Anim_11
                            hide EP18_Biker_Anim_12
                            hide EP18_Biker_Anim_13
                            hide EP18_Biker_Anim_14
                            $ EP18_Anim_Option = 2
                            if EP18_Anim_Speed == 1:
                                show EP18_Biker_Anim_13 with Dissolve(0.5)
                            elif EP18_Anim_Speed == 2:
                                show EP18_Biker_Anim_14 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_4
                        "Slower":
                            hide EP18_Biker_Anim_11
                            hide EP18_Biker_Anim_12
                            hide EP18_Biker_Anim_13
                            hide EP18_Biker_Anim_14
                            $ EP18_Anim_Speed = 1
                            if EP18_Anim_Option == 1:
                                show EP18_Biker_Anim_11 with Dissolve(0.5)
                            elif EP18_Anim_Option == 2:
                                show EP18_Biker_Anim_13 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_4
                        "Faster":
                            hide EP18_Biker_Anim_11
                            hide EP18_Biker_Anim_12
                            hide EP18_Biker_Anim_13
                            hide EP18_Biker_Anim_14
                            $ EP18_Anim_Speed = 2
                            if EP18_Anim_Option == 1:
                                show EP18_Biker_Anim_12 with Dissolve(0.5)
                            elif EP18_Anim_Option == 2:
                                show EP18_Biker_Anim_14 with Dissolve(0.5)
                            jump EP18_Biker_Anim_Menu_4
                        "Continue":
                            hide EP18_Biker_Anim_11
                            hide EP18_Biker_Anim_12
                            hide EP18_Biker_Anim_13
                            hide EP18_Biker_Anim_14
                            $ different_choice_menu = False
                            pass
                    scene 48-4 john 140 with Dissolve(0.5)
                    "Moans could be heard throughout the entire alley."
                    "Echoing off the walls and into the windows of the buildings."
                    "Hot depravities were taking place..."
                    scene 48-4 john 141 with Dissolve(0.5)
                    bi2 "FUUCK!"
                    bi2 "GETTING CLOSE!"
                    scene 48-4 john 142 with Dissolve(0.5)
                    a "Fill... Me... UP!"
                    scene 48-4 john 143 with Dissolve(0.5)
                    bi2 "FUUCK!"
                    bi2 "YEAAHHH!"
                    show EP18_Biker_Anim_14 with Dissolve(0.5)
                    play audio moaningfive
                    with flash
                    pause 2
                    with flash
                    play sound cum_sound
                    pause
                    play sound cum_sound
                    scene 48-4 john 144 with flash_vpunch
                    hide EP18_Biker_Anim_14
                    bi1 "AAAAHHHA!"
                    with flash
                    a "OHHH!"
                    with vpunch
                    scene 48-4 john 145 with Dissolve(0.5)
                    bi2 "That's a good one!"
                    a "Got it all out?"
                    bi2 "Yeah... Wheew."
                    scene 48-4 john 146 with Dissolve(0.5)
                    a "C'mon."
                    a "I ain't done yet."
                    a "And I'm sure you aren't either."
                    scene 48-4 john 147 with Dissolve(0.5)
                    bi1 "Hehe. I bet there's some room left there."
                    a "There is... Besides, that cum is already leaking out. Leaving new room."
                    scene 48-4 john 148 with Dissolve(0.5)
                    a "Give me your load too."
                    a "Enjoy the benefits of working with us!"
                    bi1 "FUCK YEAH!"
                    scene 48-4 john 149 with Dissolve(0.5)
                    bi1 "FUCK!"
                    bi1 "YEAHHHH!"
                    scene 48-4 john 150 with Dissolve(0.5)
                    pause 1
                    scene 48-4 john 151 with Dissolve(0.5)
                    a "OHH!"
                    a "That's right!"
                    a "Give me that cock!"
                    a "And don't stop until you cum!"
                    $ different_choice_menu = True
                    $ EP18_Anim_Option = 1
                    $ EP18_Anim_Speed = 1
                    scene black
                    play sound jerk loop
                    show EP18_Biker_Anim_15 with Dissolve(0.5)
                    label EP18_Biker_Sex_Label_5:
                    play audio femmoan_3
                    a "AHHH!"
                    a "YEAH!"
                    bi1 "I'm about to bust a fat one too!"
                    menu EP18_Biker_Anim_Menu_5:
                        "Slower":
                            hide EP18_Biker_Anim_15
                            hide EP18_Biker_Anim_16
                            show EP18_Biker_Anim_15 with Dissolve(0.5)
                            $ EP18_Anim_Speed = 1
                            jump EP18_Biker_Anim_Menu_5
                        "Faster":
                            hide EP18_Biker_Anim_15
                            hide EP18_Biker_Anim_16
                            show EP18_Biker_Anim_16 with Dissolve(0.5)
                            $ EP18_Anim_Speed = 2
                            jump EP18_Biker_Anim_Menu_5
                        "Continue":
                            hide EP18_Biker_Anim_15
                            hide EP18_Biker_Anim_16
                            $ different_choice_menu = False
                            pass
                    scene 48-4 john 152 with Dissolve(0.5)
                    bi1 "You're one nasty bitch, you know that?"
                    a "Hehe, I do."
                    a "And you love it."
                    bi1 "Oh yeah!"
                    scene 48-4 john 153 with Dissolve(0.5)
                    a "AHHH!!!"
                    with flash
                    play sound cum_sound
                    play sound moaninglong_1
                    scene 48-4 john 154 with Dissolve(0.5)
                    a "FUCK FUCK FUCK!"
                    show EP18_Biker_Anim_16 with Dissolve(0.5)
                    bi1 "I'm GETTING CLOSE!!!!"
                    play audio cum_sound
                    with flash
                    bi1 "YEAHHH!"
                    bi1 "TAKE MY LOAD TOO!"
                    with flash
                    with flash
                    scene 48-4 john 155 with Dissolve(0.5)
                    hide EP18_Biker_Anim_16
                    bi1 "Wow."
                    bi1 "I'm fucking empty."
                    stop sound
                    scene 48-4 john 156 with Dissolve(0.5)
                    a "Good!"
                    bi1 "Yeah."
                    scene 48-4 john 157 with Dissolve(0.5)
                    a "There's so much."
                    a "I can feel it dripping down my leg."
                    scene 48-4 john 158 with Dissolve(0.5)
                    a "Didn't know you two would have that much ready to shoot."
                    bi1 "You are one of a kind."
                    bi2 "Yeah, I also didn't know I'd cum so much."
                    bi2 "Instincts. When you see a woman like that, you shoot as much as you can."
                    bi1 "Hehe."
                    scene 48-4 john 159 with Dissolve(0.5)
                    a "SO?"
                    bi1 "Yes. We'll deal your product."
                    bi1 "75:25, as discussed."
                    a "Good."
                    scene black with Dissolve(0.5)
                    pause 1
                    play sound undress
                    scene 48-4 john 160 with Dissolve(0.5)
                    a "If you do good work... You'll receive those extra benefits again."
                    bi1 "Hehe."
                    bi1 "Glad to hear it."
                "That's all.":

                    $ EP18_Bikers_65_Percent = True
                    pass
        "Deal.":
            $ EP18_Bikers_60_Percent = True
    scene 48-4 john 161 with Dissolve(0.5)
    a "Just don't mess around and try to rip us off."
    a "My superiors won't take that well."
    a "I will be fine, but those who mess with us... Those will have problems."
    bi1 "You got it, girl."
    bi1 "You'll have no problems with us."
    $ renpy.end_replay()
    scene 48-4 john 162 with Dissolve(0.5)
    j4 "So umm..."
    j4 "You all done?"
    scene 48-4 john 163 with Dissolve(0.5)
    a "Just finished."
    bi1 "Listen, we'll have a new bit of business to take care of."
    j4 "I assume that's what you three discussed?"
    bi1 "Yeah."
    bi1 "We'll probably have to expand."
    scene 48-4 john 164 with Dissolve(0.5)
    bi1 "Anyway, we'll get moving."
    a "I will stay in contact."
    bi1 "Got it."
    scene 48-4 john 165 with Dissolve(0.5)
    j4 "What was that 'business' that you talked about?"
    a "Well..."
    a "I'll tell you some other time."
    j4 "I. I think it's important if you do it now."
    scene 48-4 john 166 with Dissolve(0.5)
    a "..."
    a "I'm involved in some 'business,' and I've been assigned to find new ways to distribute our product."
    j4 "Mhm..."
    j4 "That product being cocaine or something, right?"
    a "Well..."
    j4 "You never cease to surprise... I'm not sure how I feel about this..."
    a "Me?"
    a "I also just found out you're involved in some dealings. Illegal ones, I might add."
    j4 "Fine, fine..."
    scene 48-4 john 167 with Dissolve(0.5)
    j4 "I'm kind of tired. You wanna head home?"
    a "Sure."
    j4 "We should talk about this some more."
    j4 "OK?"
    a "We'll see..."
    scene 48-4 john 168 with Dissolve(0.5)
    j4 "Regardless of what you're into..."
    j4 "You're still one amazing woman, Anna."
    j4 "That much I can tell you..."
    j4 "I still admire you."
    scene 48-4 john 169 with Dissolve(0.5)
    a "I wouldn't have it any other way, hehe."
    j4 "Heh."
    scene black with Dissolve(0.5)
    pause 1
    play sound door2
    play music tranquility
    scene 48-4 john 170 with Dissolve(0.5)
    j4 "I'll take it easy the rest of the day."
    j4 "Wanna just hang around?"
    a "Uh... I can't. I've got other things to attend to."
    scene 48-4 john 171 with Dissolve(0.5)
    j4 "Heh. You always do."
    j4 "Alright. Your loss."
    scene 48-4 john 172 with Dissolve(0.5)
    a "I wouldn't be so sure, John."
    a "It's usually everyone else who wants my attention."
    j4 "Touche, hehe."
    play sound door2
    scene 48-4 john 173 with Dissolve(0.5)
    if BenjaminContent == True:
        a "Should get prepped and go meet Benjamin at his place."
    else:
        a "Just going to get changed..."
        a "See what's what."
    play sound undress
    scene 48-4 john 174 with Dissolve(0.5)
    a "There. That's better."
    if BenjaminContent == True:
        jump EP18_Benjamin_2
    scene black with Dissolve(0.5)
    pause 1
    jump EP18_Ruby_1
label EP18_Ruby_1:
    $ EP18_var_6 = True
    play music PPMEtheralEternity
    if BenjaminContent == True:
        scene 48-6 shop 1-1 with Dissolve(0.5)
        a "Oh... What's this..."
        if bar_var_1 == True:
            a "It's Patrick..."
            scene 48-6 shop 2-1 with Dissolve(0.5)
            a "Hello?"
            pa "Hello, Anna."
            pa "You know that we're working today, yes?"
            a "Yeah, I'm aware."
            scene 48-6 shop 3-2 with Dissolve(0.5)
            pa "I need you to run an errand before you come."
            a "What is it?"
            pa "Go to the local sex shop."
            pa "We need to buy some... Toys..."
            a "Oh... Ok."
            pa "Good. When you're done with that, come straight to the bar."
        else:
            a "It's Jim... Ok..."
            scene 48-6 shop 2-2 with Dissolve(0.5)
            a "Hello?"
            j3 "Hey, Anna. You good?"
            a "I'm ok, yeah."
            j3 "Listen. I was wondering, what could we do today at the bar?"
            j3 "Got any ideas?"
            scene 48-6 shop 3-3 with Dissolve(0.5)
            a "Hmm... Not really."
            a "You?"
            j3 "Well, I do... But will you like it?"
            a "Just tell me."
            j3 "We'd need some sex toys."
            a "Oh. Heh. Intriguing."
            j3 "Could you go get them at a local sex shop before coming in?"
            a "Sure, I'll get to it."
            j3 "I'll reimburse you after."
    else:
        scene 48-6 shop 1 with Dissolve(0.5)
        a "Oh... What's this..."
        if bar_var_1 == True:
            a "It's Patrick..."
            scene 48-6 shop 2 with Dissolve(0.5)
            a "Hello?"
            pa "Hello, Anna."
            pa "You know that we're working today, yes?"
            a "Yeah, I'm aware."
            scene 48-6 shop 3 with Dissolve(0.5)
            pa "I need you to run an errand before you come."
            a "What is it?"
            pa "Go to the local sex shop."
            pa "We need to buy some... Toys..."
            a "Oh... Ok."
            pa "Good. When you're done with that, come straight to the bar."
        else:
            a "It's Jim... Ok..."
            scene 48-6 shop 2 with Dissolve(0.5)
            a "Hello?"
            j3 "Hey, Anna. You good?"
            a "I'm ok, yeah."
            j3 "Listen. I was wondering, what could we do today at the bar?"
            j3 "Got any ideas?"
            scene 48-6 shop 3-1 with Dissolve(0.5)
            a "Hmm... Not really."
            a "You?"
            j3 "Well, I do... But will you like it?"
            a "Just tell me."
            j3 "We'd need some sex toys."
            a "Oh. Heh. Intriguing."
            j3 "Could you go get them at a local sex shop before coming in?"
            a "Sure, I'll get to it."
            j3 "I'll reimburse you after."
    jump EP18_Ruby_2
label EP18_Ruby_2:
    $ EP18_var_7 = True
    scene 48-6 shop 4 with Dissolve(0.5)
    r2 "Anna!"
    r2 "Hey!"
    r2 "Haven't seen you in a while."
    a "Hey, Ruby."
    scene 48-6 shop 6 with Dissolve(0.5)
    a "Been pretty busy."
    r2 "So. What brings you to me?"
    if bar_var_1 == True:
        a "Patrick sent me to pick up some items for the bar."
        r2 "Oh. Right!"
    else:
        a "I came to pick up some stuff for the bar. Jim might've called ahead?"
        r2 "Yeah, he did."
    scene 48-6 shop 5 with Dissolve(0.5)
    r2 "Got them already prepped."
    r2 "Give me a sec?"
    a "Sure."
    scene 48-6 shop 7 with Dissolve(0.5)
    r2 "Your old toys still keeping you satisfied?"
    a "Heh. I don't have much time to use them... Pretty busy."
    r2 "That's a pity."
    scene 48-6 shop 8 with Dissolve(0.5)
    r2 "Let me see..."
    r2 "Ok... Ok..."
    r2 "Alright."
    scene 48-6 shop 9 with Dissolve(0.5)
    r2 "This is the order for the bar."
    scene 48-6 shop 10 with Dissolve(0.5)
    a "Oh wow..."
    a "An interesting selection."
    scene 48-6 shop 11 with Dissolve(0.5)
    r2 "Since you're a very special customer."
    r2 "I'll pack something extra in this bag."
    r2 "As a surprise for you."
    a "Thank you, Ruby."
    scene 48-6 shop 12 with Dissolve(0.5)
    r2 "I hope you enjoy these."
    a "Heh... Thanks."
    a "{i}...I wonder what is the surprise for me...{/i}"
    if bar_var_1 == True:
        scene 48-6 shop 13-1 with Dissolve(0.5)
        a "{i}...I wonder what Patrick has planned...{/i}"
        a "{i}...If I know him at all... He's got some depravities planned...{/i}"
    else:
        a "{i}...I wonder what Jim had in mind... I'm the leader, but he ends up planning everything...{/i}"
        a "It could be fun."
    scene black with Dissolve(3)
    pause 1
label EP18_Ending:
    jump EP19_Begin
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
