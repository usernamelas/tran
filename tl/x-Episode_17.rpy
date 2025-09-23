label EP17_Begin:
    $ EP17_var_1 = True
    stop music
    show text "{size=+20}Press Space{/size}"
    pause
label EP17_Home:
    $ EP17_var_2 = True
    $ renpy.music.play("audio/sounds/bensound-thelounge.ogg", channel = 'music', if_changed = True)
    $ EP17_var_2 = True
    scene 46-9 home 1 with Dissolve(0.5)
    a "{i}...Oh... What's going on here...{/i}"
    j "So... That's what happened to that old bike."
    a1 "Oh, wow. Didn't know."
    scene 46-9 home 2 with Dissolve(0.5)
    a "{i}...Spending some time together...{/i}"
    a "{i}...With all that's happened, it's nice...{/i}"
    scene 46-9 home 3 with Dissolve(0.5)
    j "Anna. Hey."
    a1 "Good to see you."
    a "You too, guys."
    scene 46-9 home 4 with Dissolve(0.5)
    a "What's up?"
    a "Smells great, by the way."
    a1 "We're just cooking dinner."
    a1 "I figured it would be nice for you to come home to a hot meal."
    a "So true."
    scene 46-9 home 5 with Dissolve(0.5)
    a "Oh. That's so thoughtful."
    a "I'll take a shower while it's cooking."
    a "Can't wait to eat something, heh."
    a1 "I bet."
    scene 46-9 home 6 with Dissolve(0.5)
    a1 "We're about done. So it will be ready when you finish with the shower."
    a "Nice!"
    scene 46-9 home 7 with Dissolve(0.5)
    j "Wait. we haven't even chopped the bell peppers, yet."
    a1 "Well, then let's get to it!"
    scene 46-9 home 8 with Dissolve(0.5)
    j "I've been steaming the rest of the veggies."
    j "Not like I've been sitting around and doing nothing."
    a "{i}...Heh... They're both putting in the work...{/i}"
    play sound door2
    scene black with Dissolve(0.5)
    pause 1
    scene 46-9 home 9 with Dissolve(0.5)
    a "Yet another eventful day..."
    a "Never a dull moment, that's for sure."
    a "Alright... A hot shower, just the thing I need..."
    play sound undress
    scene black with Dissolve(0.5)
    pause 0.5
    play sound shower_sound1
    scene 46-9 home 10 with Dissolve(0.5)
    if EP12_Rebecca_Accept_Offer == True:
        a "{i}...That scene with Dylan was quite something...{/i}"
        a "{i}...I bet Michael and Jeff both enjoyed it thoroughly...{/i}"
        a "{i}...I enjoy working with them... And with Rebecca...{/i}"
    scene 46-9 home 11 with Dissolve(0.5)
    a "{i}...I have to figure out what to do about the mess with the Grayden and the entire criminal organization...{/i}"
    a "{i}...I've got to continue delivering product as they mentioned...{/i}"
    scene 46-9 home 12 with Dissolve(0.5)
    a "Ah..."
    scene 46-9 home 13 with Dissolve(0.5)
    a "So good..."
    play sound cloth_sound1
    scene 46-9 home 14 with Dissolve(0.5)
    a "{i}...Now for some food...{/i}"
    a "{i}...Can't wait to see what they've cooked...{/i}"
    scene black with Dissolve(0.5)
    pause 0.5
    play sound door2
    play music tranquility
    scene 46-9 home 15 with Dissolve(0.5)
    j "Heh. I bet I can cook a better steak than you."
    a1 "Everything's a competition nowadays."
    j "Well, Yeah."
    j "That's how you know who's the best."
    scene 46-9 home 16 with Dissolve(0.5)
    a "Well, well."
    a "Looks like you two have been really working."
    a "Steak?"
    a "That's impressive."
    a1 "Only the best for you."
    scene 46-9 home 17 with Dissolve(0.5)
    j "We thought it would be nice to have a 'family' dinner together."
    a1 "Yeah. Once in a while, it never hurts."
    scene 46-9 home 18 with Dissolve(0.5)
    j "Please, sit."
    j "Everything is prepped."
    j "I picked the wine. It's my favorite."
    a "Wow. I didn't expect this."
    scene 46-9 home 19 with Dissolve(0.5)
    a1 "There you go."
    a "Thanks, Andrew."
    a1 "{i}...That fine ass... Fuck...{/i}"
    a1 "{i}...It's been such a long while since I had sex with her...{/i}"
    a1 "{i}...Can't wait when she finally gives it to me...{/i}"
    scene 46-9 home 20 with Dissolve(0.5)
    a "Mm..."
    a "Smells delicious!"
    scene 46-9 home 21 with Dissolve(0.5)
    a "So. What's the occasion?"
    a1 "Do we need one?"
    a "No but... Usually, that's how it goes."
    a1 "Well, I think I finally got a job."
    scene 46-9 home 22 with Dissolve(0.5)
    a "Really?"
    a "Where?"
    a1 "Well, I don't wanna say yet, cause I want to be 100%% sure, but it's pretty nice."
    a "Not even a hint?"
    a1 "Heh... I will tell you both once I get it."
    scene 46-9 home 23 with Dissolve(0.5)
    j "Finally, Andrew."
    j "You've been sitting on your ass for a while now."
    a1 "I was literally shot. What do you mean?"
    j "Nothing, nothing. Just saying that sounds like you finally did something right."
    scene 46-9 home 24 with Dissolve(0.5)
    a "Huh?"
    a "{i}...That's awfully mean...{/i}"
    scene 46-9 home 25 with Dissolve(0.5)
    a "I'm glad, for one, that you've been able to find something."
    a1 "Yeah. I'm pretty sure I got it, but I just wanna make sure."
    a1 "Tell you when I get there on my first day."
    a "Heh. Will keep you to it, Andrew."
    scene 46-9 home 26 with Dissolve(0.5)
    a "Cheers to you, Andrew!"
    play sound drinkingBeverage
    scene 46-9 home 27 with Dissolve(0.5)
    pause 1
    scene 46-9 home 28 with Dissolve(0.5)
    a "The steak looks so juicy and tasty."
    a1 "Trust me it is."
    a1 "If there's one thing I know how to do, it's cooking a good steak."
    scene 46-9 home 29 with Dissolve(0.5)
    a "This really is nice, you know."
    a "Who's idea was it?"
    a1 "Well..."
    a "It was yours, Andrew?"
    a1 "Yeah. Heh."
    scene 46-9 home 30 with Dissolve(0.5)
    a "That's so nice."
    a "You know, John. You don't give Andrew enough credit."
    a "He also helped me uncover a serious issue."
    a "Without his help, There would be dire consequences."
    a "So... Yeah."
    scene 46-9 home 31 with Dissolve(0.5)
    j "I mean... Yeah. It's all good, Andrew."
    j "Sorry for being so harsh."
    a1 "It's fine."
    scene black with Dissolve(0.5)
    "Some time later..."
    scene 46-9 home 32 with Dissolve(0.5)
    a "Wow... It was so tasty."
    a "I didn't expect it to be so good."
    a1 "Tried my best, heh."
    j "Can't argue there. It was really good."
    scene 46-9 home 33 with Dissolve(0.5)
    a1 "Mm..."
    a1 "{i}...Her nipple is almost showing...{/i}"
    a1 "{i}...I want her so bad... Damn...{/i}"
    scene 46-9 home 34 with Dissolve(0.5)
    j "{i}...I can almost see her nipple... So hot...{/i}"
    "Both Andrew and John were staring at them..."
    "Lusting for Anna."
    "It was almost a competition, who could get her..."
    menu:
        "Touch Johns crotch.":
            play sound undress
            scene 46-9 home 31-1 with Dissolve(0.5)
            j "Oh..."
            j "{i}...Ahhh... Hehe... She likes me...{/i}"
            scene 46-9 home 31-2 with Dissolve(0.5)
            j "Heh..."
            a "Hehe..."
            a1 "All good there?"
            j "Yeah."
        "Nevermind.":
            pass
    scene 46-9 home 35 with Dissolve(0.5)
    a1 "{i}...Huh...{/i}"
    a1 "{i}...Is he looking at her boobs, too?...{/i}"
    a1 "{i}...That's... Wrong...{/i}"
    scene 46-9 home 36 with Dissolve(0.5)
    j "{i}...Fuckk... I think he caught me staring...{/i}"
    j "{i}...What are you gonna do about it boy, eh?{/i}"
    j "{i}...I wanna be Anna's daddy...{/i}"
    "The two of them felt awkward tension..."
    "Both wanted a piece of that fine ass."
    scene 46-9 home 37 with Dissolve(0.5)
    a "Alright. I'm kind of tired. I'm going to sleep, you coming?"
    a1 "Oh. Umm. Yeah."
    a1 "I'm also tired. Have to get stuff done tomorrow."
    scene 46-9 home 38 with Dissolve(0.5)
    j "Guys?"
    j "Who's gonna clean it up?"
    a "You, John."
    a "He cooked such a good steak. You could clean up."
    j "Ok."
    scene 46-9 home 39 with Dissolve(0.5)
    a "When do you start work?"
    a1 "In a couple of days."
    a "Can't wait to see what you do, hehe."
    scene black with Dissolve(0.5)
    pause 0.5
    play sound door2
    scene 46-9 home 40 with Dissolve(0.5)
    a1 "Hey, Anna."
    a1 "It's been a while since we've done anything and..."
    a1 "You said that when I get better, then we'd..."
    a1 "You know?"
    a1 "Do something fun."
    scene 46-9 home 41 with Dissolve(0.5)
    a "Oh... Andrew... I'm sorry."
    a "I'm tired from today."
    a "I'd like to, but I'm just a bit too spent."
    play sound undress
    scene 46-9 home 42 with Dissolve(0.5)
    a "Perhaps you could wait a day or two?"
    a "When things are a bit more calm, you know?"
    a1 "Eh. Fine..."
    a "I promise the wait will be worth it."
    scene 46-9 home 43 with Dissolve(0.5)
    if EarlHelp == False:
        a "By the way. This is very important."
        a "I followed up on the lead you gave me and..."
        a "It's pretty serious."
        a "I need to let Sergey know, somehow."
        a1 "You sure it's a good idea?"
        a1 "I mean, it could be dangerous."
        a "You know me, I can find a way to avoid it."
        a "I have to do this. Otherwise, we will all be in jeopardy."
        a1 "I understand. Just be careful."
        a1 "What's the plan?"
        a "I will go meet with him and Sergey tomorrow... And try to figure out how I could tell him."
        a1 "Uh... I don't like it, but fine."
    else:
        a "So... I followed up on the lead you gave me..."
        a "The good news is that Carl is in the precinct, locked up already..."
        a "The bad news is that due to his behavior the leaders of the gang have stepped in..."
        a "They noticed that the operation has stopped and sent someone to find out what's wrong."
        a "I met with the guy. He told me that I have to resume distribution..."
        a "He also said that there is missing money and I will have to figure out how to get it back..."
        a "It's... Pretty shitty... But I think I can figure it out. As long as I can find where Carl might've hidden his stash."
        a1 "I think I should do all of this with you..."
        a "It's ok, Andrew."
        a "I'm in this, no need to pull you into it, too."
        a "You got shot... I don't want that to happen to you again."
        a1 "But I can help."
        a "No. It's better if I do this on my own..."
    a "Anyway... I'm tired..."
    scene 46-9 home 44 with Dissolve(0.5)
    a "Mmm..."
    stop music
    scene black with Dissolve(0.5)
    pause 0.5
    play sound interface_sound
    show text "Friday Morning..." with Dissolve(1.5)
    pause 0.5
    scene 47-1 morning 1 with Dissolve(0.5)
    a "Ahh..."
    a "Time to get up..."
    a "Got a lot of stuff to do..."
    scene 47-1 morning 2 with Dissolve(0.5)
    a "I'd just want a simple, uneventful day for once..."
    a "Is that too much to ask for..."
    a "always got some trouble I get into..."
    play sound cloth_sound1
    scene 47-1 morning 3 with Dissolve(0.5)
    a "First I've got work..."
    if EarlHelp == False:
        a "Then I should go to Rebecca. Get the car..."
        a "I need to somehow let Sergey know about Carl..."
    else:
        a "And I need to figure out some way to get more people to sell stuff so I can earn the money back faster..."
        a "Grayden didn't look like someone to mess around with."
        a "Perhaps I could try with the boys..."
    scene black with Dissolve(0.5)
    jump EP17_Office
    pause 1
label EP17_Rebecca:
    $ EP17_var_4 = True
    $ renpy.music.play("audio/sounds/bensound-thejazzpiano.ogg", channel = 'music', if_changed = True)
    scene 47-3 rebecca 1 with Dissolve(0.5)
    r1 "Anna! Hey!"
    r1 "Good to see you."
    scene 47-3 rebecca 2 with Dissolve(0.5)
    r1 "What brings you here?"
    a "I wanted to ask if I could get the car again?"
    if EarlHelp == False:
        a "I've got a plan, and I need to go back to Carl's hideout again..."
        r1 "What? Why?"
    else:
        r1 "Oh?"
        a "Yeah."
        a "You know our current situation, I've things to do and the car would make it easier."
        a "{i}...I have to find some more distributors for the drugs... The car will make things go a lot faster...{/i}"
    scene 47-3 rebecca 3 with Dissolve(0.5)
    if EarlHelp == False:
        a "Last time I was there, I only met Carl..."
        a "I need to meet Sergey, I need to let him know about this whole situation, somehow."
        a "I'd rather he did something about this whole situation, instead of us."
        a "At least sort it out with Carl..."
    else:
        a "Unless you had other plans for it."
        r1 "Umm. Nope."
        r1 "Yeah, why not."
    scene 47-3 rebecca 4 with Dissolve(0.5)
    if EarlHelp == False:
        r1 "Oh... Yeah, sure."
    r1 "I've got the key here."
    scene 47-3 rebecca 5 with Dissolve(0.5)
    r1 "You can just keep the car, to be honest..."
    r1 "I don't have a driver's license anyway."
    r1 "No use to me."
    a "Are you sure?"
    r1 "Yeah... What else would I do with it?"
    a "I don't know... Sell it?"
    r1 "Sounds to me like giving it to you could be more useful."
    a "Ok..."
    scene 47-3 rebecca 6 with Dissolve(0.5)
    r1 "Be very careful, Anna."
    if EarlHelp == False:
        r1 "We don't know what Carl is planning..."
    else:
        r1 "We don't want to mess with these people..."
    r1 "Ok?"
    a "Ok, sis. I'll do my best."
    scene 47-3 rebecca 7 with Dissolve(0.5)
    r1 "I don't want to lose you..."
    if EP12_Rebecca_Accept_Offer == True:
        r1 "Now that we've filmed a scene together..."
        r1 "I wish we could've been a bit closer during the filming, you know?"
        a "Oh... Heh... Yeah..."
    else:
        r1 "You're very dear to me."
        r1 "Can't have anything happen to you..."
    scene 47-3 rebecca 8 with Dissolve(0.5)
    if EarlHelp == False:
        r1 "So just, get what you need and get out of there, ok?"
        a "Ok."
        a "I will only stick around if Sergey's there."
        a "That should make it safer."
        r1 "Ok."
    else:
        r1 "Whatever you're doing..."
        r1 "I believe that you will succeed."
        a "Thanks, Rebecca."
        r1 "I just wish I could do more."
        a "One step at a time."
    scene 47-3 rebecca 9 with Dissolve(0.5)
    r1 "Take care, Anna."
    a "I will. Thanks for the car."
    r1 "It's all yours now, heh..."
    play sound door2
    scene black with Dissolve(0.5)
    pause 0.5
    if EarlHelp == True:
        jump EP17_Boys_1
    play ambient city_traffic
    scene 47-4 carl 1 with Dissolve(0.5)
    a "This car is now mine... Heh..."
    a "Unlikely for long, though..."
    a "Since it's probably acquired with illegal funds..."
    a "But one can hope."
    play sound car_door_close
    scene 47-4 carl 2 with Dissolve(0.5)
    a "Nice..."
    a "This ride is so smooth..."
    scene 47-4 carl 3 with Dissolve(0.5)
    a "{i}...Alright... I should just go to the hideout again...{/i}"
    a "{i}...If Sergey's there... I'll go in...{/i}"
    a "{i}...If not, I'll make up some excuse as to why I cannot...{/i}"
    stop ambient
    play sound car_sound1
    scene black with Dissolve(0.5)
    pause 0.5
    play music tense2
    scene 47-4 carl 4 with Dissolve(0.5)
    a "Alright..."
    a "Best of luck to me."
    scene 47-4 carl 5 with Dissolve(0.5)
    a "It looks like Sergey's here."
    a "His car is here."
    a "That's a good sign."
    play sound car_door_close
    scene 47-4 carl 6 with Dissolve(0.5)
    pause 1
    scene 47-4 carl 7 with Dissolve(0.5)
    "Anna went onward."
    a "How could I let Sergey know of Carl's real intentions..."
    a "Perhaps I could act as if it's a personal visit to Sergey..."
    if CarlSexContent == True:
        a "That would make Carl jealous... Heh..."
        a "A bit of revenge on my part for what he's done."
    scene 47-4 carl 8 with Dissolve(0.5)
    pause 1
    play sound doorknock
    scene 47-4 carl 9 with Dissolve(0.5)
    pause 1
    scene 47-4 carl 10 with Dissolve(0.5)
    s1 "Anna?"
    s1 "What are you doing here?"
    a "I..."
    a "I've got some important info..."
    a "Since you put me in charge at the warehouse..."
    a "There have been some developments."
    scene 47-4 carl 11 with Dissolve(0.5)
    s1 "Alright, alright."
    s1 "Let's talk more inside, come."
    scene 47-4 carl 12 with Dissolve(0.5)
    a "Oh. Carl, Hey."
    a "You're also here."
    a "How are you doing?"
    scene 47-4 carl 13 with Dissolve(0.5)
    c1 "Hey, Anna. All good?"
    c1 "You're acting a bit strange."
    c1 "I overheard you say that there's some development at the warehouse?"
    scene 47-4 carl 14 with Dissolve(0.5)
    a "Well... Yeah... But..."
    a "I sort of came here because... I..."
    scene 47-4 carl 15 with Dissolve(0.5)
    a "Missed someone."
    s1 "Huh?"
    c1 "Really?"
    s1 "Really?"
    scene 47-4 carl 16 with Dissolve(0.5)
    a "Y... Yeah."
    a "I wanted to see Sergey..."
    s1 "Oh... Ummm..."
    s1 "Well..."
    scene 47-4 carl 17 with Dissolve(0.5)
    if CarlSexContent == True:
        c1 "{i}...Seriously...{/i}"
        c1 "In front of me, after all that we've done together..."
    c1 "Umm... I'll just go out and..."
    c1 "Will grab a bite. There's a good food joint nearby."
    a "Thanks, Carl..."
    scene 47-4 carl 18 with Dissolve(0.5)
    c1 "I'll be uhh..."
    c1 "Not far."
    scene 47-4 carl 19 with Dissolve(0.5)
    if SergeySexContent == True:
        s1 "It's been a while since we've done something..."
        s1 "Really couldn't hold out any longer, heh."
        a "Sorry... I really want to, but not this time..."
        s1 "Huh?"
    else:
        s1 "Alright, you and I both know that you turned me down cold."
        s1 "What's changed?"
        a "It was a ruse."
        s1 "Huh?"
    scene 47-4 carl 20 with Dissolve(0.5)
    a "I'm actually here to warn you, Sergey."
    s1 "What about?"
    a "Grayden came to the warehouse."
    a "And... They are not happy with the halted operations."
    a "He and his superiors want to resume things and I'm the only one who's got the power to do it..."
    a "That's a part of the reason I'm here."
    a "It also turns out that..."
    scene 47-4 carl 21 with Dissolve(0.5)
    a "Carl's betrayed you..."
    a "Betrayed all of us."
    s1 "What are you talking about?"
    c1 "{i}...She was acting really strange...{/i}"
    c1 "{i}...Same as the previous time she came here...{/i}"
    c1 "{i}...Does she know...{/i}"
    scene 47-4 carl 22 with Dissolve(0.5)
    s1 "Explain..."
    a "Andrew has woken up..."
    a "And he had some really interesting things to say about Carl."
    a "He was 'investigating' him."
    a "He found out that Carl had been stealing cocaine and money from the operation..."
    scene 47-4 carl 23 with Dissolve(0.5)
    a "He had also been working with Fitzgerald..."
    a "It was all a setup to get you killed..."
    a "It was a lucky twist of fate that Andrew was shot and couldn't tell anyone anything..."
    a "Ever since then Carl has been looking for a good way to disappear."
    a "I found his diary... It's in the warehouse..."
    a "But... Everything I'm telling you is true."
    scene 47-4 carl 24 with Dissolve(0.5)
    s1 "And... Andrew helped you with that?"
    s1 "The same incompetent Andrew?"
    a "If you wanna put it that way, yeah."
    s1 "..."
    s1 "..."
    scene 47-4 carl 25 with Dissolve(0.5)
    s1 "He was... Stealing from us..."
    s1 "He arranged Rebecca's kidnapping..."
    a "As far as I understand it was a setup to get you, but it didn't work out..."
    s1 "He wanted to kill me?"
    scene 47-4 carl 26 with Dissolve(0.5)
    a "I... I think so..."
    a "I'm not sure abut his motivations..."
    a "Perhaps he just wanted to escape..."
    a "I... I don't know..."
    scene 47-4 carl 27 with Dissolve(0.5)
    s1 "FUUCK!"
    s1 "CARL IS BEHIND IT ALL?"
    s1 "BEHIND THE ENTIRE FUCKING SITUATION?!"
    a "He was guarding Fitzgerald and Smith that night..."
    scene 47-4 carl 28 with Dissolve(0.5)
    a "He didn't expect that you'd bring me and I'd kill Smith..."
    s1 "And... Now I've been sleeping in the same room with a guy that was trying to kill me..."
    s1 "It doesn't make sense..."
    a "Perhaps he wanted to pin it on Fitzgerald?"
    s1 "That would be my bet."
    s1 "Here it would be just too obvious..."
    scene 47-4 carl 29 with Dissolve(0.5)
    a "What are we gonna do?"
    a "We need to restart the operation..."
    s1 "We need to get rid of Carl..."
    a "But we owe a lot of money to the organization..."
    a "Grayden was very clear what would happen if we didn't get the money..."
    scene 47-4 carl 30 with Dissolve(0.5)
    s1 "Carl must've stashed it somewhere..."
    s1 "We will get him, I will BEAT HIM TO A PULP!"
    s1 "He'll tell me exactly where the money is."
    a "But..."
    scene 47-4 carl 31 with Dissolve(0.5)
    s1 "Fuuuuckk..."
    s1 "I had a feeling something is up..."
    s1 "You can never relax in this fucking 'career'..."
    s1 "I WILL GET THE INFO AND THEN FUCKING SPLIT HIM IN HALF!"
    a "Sergey..."
    scene 47-4 carl 32 with Dissolve(0.5)
    s1 "What?"
    a "It's... Ok..."
    a "I also felt betrayed..."
    scene 47-4 carl 33 with Dissolve(0.5)
    a "But... It's ok..."
    "Anna laid her soft hand on Sergey..."
    "It immediately seemed to calm him down..."
    s1 "Anna..."
    scene 47-4 carl 34 with Dissolve(0.5)
    s1 "You somehow make me calmer..."
    s1 "You're right."
    s1 "This is no time to lose our heads..."
    scene 47-4 carl 35 with Dissolve(0.5)
    s1 "We have to come up with a plan..."
    s1 "Do you know how much money he had stolen?"
    a "A lot... We definitely need to figure out where he hid the stash..."
    s1 "You're right."
    s1 "Regardless, while we try to find the stash..."
    s1 "We need to move product."
    s1 "But we only have Michael. And we need to do things faster..."
    a "Well... I might have a few people in mind."
    s1 "Is that so?"
    s1 "Alright, you'll tell me all about it later on..."
    scene 47-4 carl 36 with Dissolve(0.5)
    s1 "For now we need to act as if everything is alright."
    s1 "When he comes back, I will ambush him."
    s1 "You will have to help me tie him up and make sure that he cannot get free, ok?"
    s1 "I think it's time we returned to the city..."
    a "Are you sure it's safe?"
    scene 47-4 carl 37 with Dissolve(0.5)
    s1 "If we don't solve this issue, nowhere will be safe."
    s1 "it's a risk I have to take."
    a "Ok..."
    scene 47-4 carl 38 with Dissolve(0.5)
    s1 "Hold on..."
    play sound car_sound1
    scene 47-4 carl 39 with Dissolve(0.5)
    s1 "MY CAR!"
    s1 "He's driving away in my CAR!"
    s1 "UROD!"
    s1 "FUCK!"
    scene 47-4 carl 40 with Dissolve(0.5)
    s1 "He knicked the goddamn keys right before our eyes!"
    s1 "FUCK!"
    scene 47-4 carl 41 with Dissolve(0.5)
    s1 "Anna, we can't lose him now!"
    s1 "He will disappear... God knows he's resourceful."
    s1 "We have to get after him!"
    play sound door2
    play music ChaseSong_1
    scene 47-4 carl 42 with vpunch
    s1 "FUCK!"
    s1 "SRANAJA SUKA!!!"
    a "{i}...He must be furious to swear in Russian.{/i}"
    a "We can take my car!"
    play sound car_break
    scene 47-4 carl 43 with Dissolve(0.5)
    c1 "I KNEW IT!"
    c1 "They're on to me."
    c1 "I have to get out of here, become a ghost."
    scene 47-4 carl 44 with Dissolve(0.5)
    s1 "FUCK!"
    s1 "Your tire is flat."
    s1 "No doubt his work..."
    stop music fadeout 3
    scene 47-4 carl 45 with Dissolve(0.5)
    a "What will we do?"
    s1 "There's got to be a spare in the car."
    a "Will you be able to fix it in time?"
    play music blues
    s1 "No... It doesn't matter now."
    s1 "Let's just get back to the warehouse."
    scene 47-4 carl 46 with Dissolve(0.5)
    s1 "He will PAY for this betrayal."
    s1 "I had my suspicions... But I never thought he'd actually do it..."
    s1 "He was loyal for all these years..."
    scene 47-4 carl 47 with Dissolve(0.5)
    s1 "How did I not see it coming..."
    "Wherever Anna went, trouble followed."
    "Her presence made men fall over for her, fight for her..."
    "Wage wars for her..."
    scene black with Dissolve(0.5)
    "After a little while..."
    scene 47-4 carl 48 with Dissolve(0.5)
    s1 "Ugh..."
    s1 "There..."
    if SergeySexContent == True:
        a "{i}...He's so hot working like this... Oh...{/i}"
    scene 47-4 carl 49 with Dissolve(0.5)
    s1 "That should do it."
    a "All done?"
    s1 "Yeah. Let's just hope he didn't do anything else to the car."
    scene 47-4 carl 50 with Dissolve(0.5)
    a "What now?"
    s1 "Let's go to the warehouse."
    a "Will you be safe back in the city?"
    s1 "Yeah."
    s1 "I will be fine."
    s1 "Just have to lay low... Somewhat."
    play sound undress
    scene 47-4 carl 51 with Dissolve(0.5)
    pause 1
    scene 47-4 carl 52 with Dissolve(0.5)
    s1 "Give me the key. I'll drive."
    a "Ok..."
    s1 "Sorry, I just... Need to do something right now."
    a "Sure, I understand."
    play sound car_door_close
    scene 47-4 carl 53 with Dissolve(0.5)
    s1 "I'll go to the warehouse..."
    s1 "I need to see the current state of things."
    a "I mostly didn't touch anything."
    a "Tyler has been spending time there as you requested originally."
    s1 "Good."
    scene 47-4 carl 54 with Dissolve(0.5)
    s1 "Honestly, can't wait to get back."
    s1 "The only other person I'd trust is you, now that Carl has screwed me over."
    s1 "But dealing with Grayden is beyond you."
    s1 "I'm not putting you in that situation again."
    play sound carsound
    scene black with Dissolve(0.5)
    pause 1
    play music SecretAgent
    scene 47-4 carl 55 with Dissolve(0.5)
    "Guard Tyler awaits their arrival."
    scene 47-4 carl 56 with Dissolve(0.5)
    s1 "There he is."
    s1 "Did he keep you in the loop about everything?"
    a "Yeah."
    s1 "Good, he's a good man."
    scene 47-4 carl 57 with Dissolve(0.5)
    s1 "Hey."
    s1 "You good, Tyler?"
    scene 47-4 carl 58 with Dissolve(0.5)
    wg1 "I'm fine. I'm just surprised you're back, sir."
    wg1 "Thought you'd phone ahead."
    scene 47-4 carl 57 with Dissolve(0.5)
    s1 "There was no time."
    s1 "Came here as soon as I heard."
    s1 "There have been some unfortunate developments."
    s1 "I assume you were here when Grayden came?"
    wg1 "I was, sir."
    s1 "Good... I assume you've unloaded the product?"
    wg1 "As usual."
    s1 "Ok, we will need to prep it for distribution."
    s1 "There are some serious problems and we need to move as much of it as possible."
    wg1 "Understood."
    scene 47-4 carl 59 with Dissolve(0.5)
    s1 "As for you, Anna."
    s1 "I need you to follow up on that lead you told me about."
    s1 "Regarding more people to help with the product."
    s1 "I trust that you can make it happen."
    scene 47-4 carl 60 with Dissolve(0.5)
    s1 "As of now, you're one of the very few people I really trust."
    s1 "Can I rely on you to do this?"
    a "You can... Sergey..."
    s1 "Thanks... I have a lot of work to do. We'll talk this through later, ok?"
    a "Ok."
    play sound car_door_close
    scene 47-4 carl 61 with Dissolve(0.5)
    pause 1
    scene 47-4 carl 62 with Dissolve(0.5)
    a "I should probably contact the dudes..."
    a "See what they're up to..."
    scene black with Dissolve(0.5)
    pause 0.5
label EP17_Boys_1:
    $ EP17_var_5 = True
    play music VibingCity volume 0.7
    scene 47-5 boys 1 with Dissolve(0.5)
    a "Ok... I'm really doing this..."
    a "Trying to persuade a couple of dudes to sell drugs for the operation."
    a "But... I cannot do it without them..."
    a "Let's just see how it goes."
    play sound doorknock
    scene 47-5 boys 2 with Dissolve(0.5)
    pause 1
    scene 47-5 boys 3 with Dissolve(0.5)
    st2 "Anna?"
    st2 "Hey! What brings you here?"
    a "Oh... Just came by, to see how you guys are doing."
    st2 "We're doing great!"
    scene 47-5 boys 4 with Dissolve(0.5)
    do1 "Anna! HEY!"
    a "Hey, guys!"
    do1 "Good to see you here."
    ro2 "Yeah!"
    scene 47-5 boys 5 with Dissolve(0.5)
    a "I didn't interrupt anything, did I?"
    do1 "Not at all!"
    do1 "We were just getting ready go to to the movies."
    a "Movies?"
    a "You mean the cinema?"
    st2 "Yeah!"
    scene 47-5 boys 6 with Dissolve(0.5)
    a "Hmm... Would you mind if I joined you guys?"
    do1 "Really? You'd wanna come with us?"
    a "Why not?"
    do1 "That would be great!"
    ro2 "We got a dope movie in mind, you'll love it."
    a "When are you going?"
    do1 "We were about to leave."
    a "Ok."
    scene 47-5 boys 7 with Dissolve(0.5)
    a "I'll go change real quick, meet me in the hallway?"
    do1 "Sounds like a plan!"
    play sound door2
    scene black with Dissolve(0.5)
    pause 0.5
    scene 47-5 boys 8 with Dissolve(0.5)
    a "What could I wear."
    a "Perhaps something youtful..."
    a "It is a nice day outside, after all."
    scene black with Dissolve(0.5)
    pause 0.5
    play sound undress
    scene 47-5 boys 9 with Dissolve(0.5)
    a "Perfect. Heh."
    scene black with Dissolve(0.5)
    pause 0.5
    play sound door2
    scene 47-5 boys 10 with Dissolve(0.5)
    do1 "How much have we sold?"
    st2 "Like 15 g in the last month."
    ro2 "Nice, we're slowly getting there."
    a "{i}...Huh... Are they selling something as well...{/i}"
    scene 47-5 boys 11 with Dissolve(0.5)
    ro2 "Alright, enough business talk."
    st2 "Heh. Wow... She's stunning..."
    scene 47-5 boys 12 with Dissolve(0.5)
    ro2 "Let me be the first to say it: You look amazing!"
    a "Thanks, Rocco. Heh."
    st2 "Rocco's just a kissup, Haha."
    do1 "Yeah. Always trying to kiss ass!"
    ro2 "Shut up, guys!"
    scene 47-5 boys 13 with Dissolve(0.5)
    a "Now, now, boys."
    a "I just thought I'd pick out something more appropriate."
    scene 47-5 boys 14 with Dissolve(0.5)
    a "Looks like I succeeded."
    do1 "Definitely."
    scene 47-5 boys 15 with Dissolve(0.5)
    a "Right, Steve?"
    st2 "Uhh..."
    scene 47-5 boys 16 with Dissolve(0.5)
    a "Don't you like it?"
    st2 "I... Uhh..."
    scene 47-5 boys 17 with Dissolve(0.5)
    st2 "{b}*Gulp*{/b}"
    st2 "Yeah. It looks great!"
    a "Hehe. I knew you'd like it."
    scene 47-5 boys 18 with Dissolve(0.5)
    st2 "So. We were thinking of taking the bus or something."
    st2 "We won't make it in time on foot."
    a "How about a car?"
    st2 "Neither of us have one..."
    a "I do."
    st2 "Really?"
    st2 "In this economy?"
    st2 "Must be rich, then..."
    a "Heh, let's go."
    scene black with Dissolve(0.5)
    pause 0.5
    scene 47-5 boys 19 with Dissolve(0.5)
    do1 "Whoa... You're telling me THIS is your car?"
    do1 "Seriously?"
    st2 "Goddamn!"
    ro2 "No waaayyyyy!"
    scene 47-5 boys 20 with Dissolve(0.5)
    a "What? You don't like it?"
    a "Feel free to take the tram, haha."
    do1 "Nonono."
    scene 47-5 boys 21 with Dissolve(0.5)
    do1 "This car is SUPER dope!"
    st2 "Yeah, we didn't expect you to have such a car."
    ro2 "Yeah. How can you afford it?"
    a "Hehe..."
    a "Alright, let's get in."
    play sound car_door_close
    scene 47-5 boys 22 with Dissolve(0.5)
    st2 "Wow. The interior is super high quality."
    st2 "Can't believe it."
    do1 "It feels almost illegal to sit in a beauty like this."
    scene 47-5 boys 23 with Dissolve(0.5)
    ro2 "Just get in the car, dude."
    ro2 "Lucky bastard got the front seat!"
    do1 "Haha."
    do1 "I am the leader of the three of us."
    ro2 "YOU WISH. Haha!"
    play sound car_door_close
    scene 47-5 boys 24 with Dissolve(0.5)
    do1 "How can you afford such a car?"
    a "I've got my ways."
    do1 "I literally want a car like this..."
    a "Some day you will."
    do1 "I know... I will be rich and have a car like this... A yacht... Oh man..."
    scene 47-5 boys 25 with Dissolve(0.5)
    st2 "Wake up from your daydream sucker."
    st2 "Haha."
    do1 "Hey! Can't a man dream?"
    st2 "Suuure."
    scene 47-5 boys 26 with Dissolve(0.5)
    a "Soo. To the Cinema. How much time have we got?"
    do1 "Plenty since we're going by car."
    a "Alright."
    scene 47-5 boys 27 with Dissolve(0.5)
    st2 "Never has a girl driven me around like this."
    st2 "Pretty cool, to be honest."
    a "Haha. Now you know what girls experience."
    scene 47-5 boys 28 with Dissolve(0.5)
    st2 "Yeah. It's nice."
    scene 47-5 boys 29 with Dissolve(0.5)
    a "Here we are."
    do1 "Nice. Been wanting to see that film for a while now."
    st2 "Yeah."
    scene 47-5 boys 30 with Dissolve(0.5)
    a "I'll park the car around the corner. Wait for me?"
    do1 "Yeah."
    scene black with Dissolve(0.5)
    pause 0.5
    scene 47-5 boys 32 with Dissolve(0.5)
    do1 "The movie starts in 10 mins."
    ro2 "Just in time, then."
    st2 "{i}...Fuuuck...{/i}"
    scene 47-5 boys 33 with Dissolve(0.5)
    a "Been a while since I came to the cinema."
    ro2 "Hehe. Glad you joined us."
    scene 47-5 boys 34 with Dissolve(0.5)
    do1 "Alright. I'll get the tickets, got a discount for them."
    do1 "You guys get the snacks, sounds good?"
    ro2 "Yeah."
    scene 47-5 boys 35 with Dissolve(0.5)
    do1 "Don't get lost without me, hehe..."
    st2 "Shut up dude!"
    do1 "By the way, get me the diet coke, please."
    ro2 "We know, we know dude."
    scene 47-5 boys 36 with Dissolve(0.5)
    a "Let me take care of this, ok?"
    st2 "You sure?"
    a "Absolutely."
    a "Student life isn't easy, I know that."
    st2 "We can pay. We got money."
    a "I insist, this time."
    st2 "Alright..."
    scene 47-5 boys 37 with Dissolve(0.5)
    cashier1 "Hello, How may I help."
    a "Hey, we'd like 3 regular cokes and 1 diet coke please."
    a "Also two buckets of popcorn."
    scene 47-5 boys 38 with Dissolve(0.5)
    a "That's all."
    cashier1 "Alright, coming up."
    scene 47-5 boys 39 with Dissolve(0.5)
    ro2 "You sure you wanna pay?"
    a "Yeah, It's ok, Rocco."
    scene 47-5 boys 40 with Dissolve(0.5)
    cashier1 "There you go."
    cashier1 "That will be 25 dollars."
    a "No problem."
    scene 47-5 boys 41 with Dissolve(0.5)
    st3 "Hmm?"
    st3 "{i}...Wait... I think I know that girl...{/i}"
    scene 47-5 boys 42 with Dissolve(0.5)
    st3 "Hey, Don't I know you from somewhere?"
    st3 "Yeah, I think I've seen you in an adult film..."
    scene 47-5 boys 43 with Dissolve(0.5)
    a "Huh?"
    st3 "YEAH!"
    st3 "I'm like 95%% sure I've seen you sucking on a cock somewhere."
    a "WHAT?"
    st3 "Such a hot fucking body."
    scene 47-5 boys 44 with Dissolve(0.5)
    st2 "What did you say?"
    st3 "Hm?"
    scene 47-5 boys 45 with Dissolve(0.5)
    st2 "Bitch, I asked you a question."
    st2 "Or are you too big of a bitch to repeat it."
    st3 "I..."
    scene 47-5 boys 46 with Dissolve(0.5)
    st3 "I know that girl from somewhere. She sucks cock."
    st2 "You dumb idiot!"
    play sound spank3
    scene 47-5 boys 47 with vpunch
    st2 "Pussy ass bitch."
    st2 "Let's take it outside, I'll fuck you up!"
    st3 "AHH!"
    scene 47-5 boys 48 with Dissolve(0.5)
    st3 "No, please. I'm leaving."
    st2 "That's right bitch."
    st2 "You can only talk to women like that. Weak ass cretin."
    scene 47-5 boys 49 with Dissolve(0.5)
    a "Whoa."
    a "{i}...They don't mess around... Hehe...{/i}"
    a "{i}...They might be exactly what I'm looking for...{/i}"
    scene 47-5 boys 50 with Dissolve(0.5)
    st2 "What?"
    st2 "I wasn't gonna allow that POS disrespect my friend."
    a "I can see, hah."
    scene 47-5 boys 51 with Dissolve(0.5)
    a "That was brave."
    st2 "That was a no-brainer. Beyond disrespectful."
    st2 "Perhaps he'll think twice before saying some dumb shit again."
    a "Thanks, Steve."
    scene 47-5 boys 52 with Dissolve(0.5)
    cashier1 "He's harassed women here before."
    cashier1 "Looks like your friends put him in his place."
    st2 "Damn straight."
    st2 "If I see him here again..."
    scene 47-5 boys 53 with Dissolve(0.5)
    do1 "What's all this fuss about?"
    ro2 "Haha. You missed a good-ass moment."
    ro2 "Some dumbass said some sexual comments about Anna."
    ro2 "Steve put him in his place."
    scene 47-5 boys 54 with Dissolve(0.5)
    do1 "What? Where the fuck is that asshole."
    do1 "I'm going to beat his face blue."
    ro2 "He left already."
    scene 47-5 boys 55 with Dissolve(0.5)
    a "It's alright, Donny."
    a "Thanks."
    a "I appreciate you having my back."
    scene 47-5 boys 56 with Dissolve(0.5)
    ro2 "You should've seen the guy's face. Haha."
    ro2 "Steve slapped him. No bigger disrespect than that."
    ro2 "The guy almost ran out crying. Haha!"
    scene 47-5 boys 57 with Dissolve(0.5)
    a "Thanks again, Steve."
    scene 47-5 boys 58 with Dissolve(0.5)
    st2 "Anytime, Anna."
    st2 "We got your back."
    a "Hehe."
    do1 "It's about to start... I'm so excited!"
    do1 "Heh. Good, not a lot of people."
    scene 47-5 boys 60 with Dissolve(0.5)
    pause 0.5
    scene 47-5 boys 62 with Dissolve(0.5)
    ro2 "Which row?"
    do1 "Closer to the top."
    scene 47-5 boys 63 with Dissolve(0.5)
    do1 "Row 20, I think."
    ro2 "Heh. Good, we won't be bothered there."
    scene 47-5 boys 64 with Dissolve(0.5)
    pause 0.5
    scene 47-5 boys 65 with Dissolve(0.5)
    pause 0.5
    scene 47-5 boys 66 with Dissolve(0.5)
    do1 "Did you get my diet coke?"
    a "Yeah. As ordered."
    st2 "Dude, only pussies drink diet coke."
    do1 "What the fuck are you talking about."
    ro2 "Gotta agree, it tastes like ass."
    do1 "Whatever. I'm working out. Don't need the extra calories."
    scene 47-5 boys 67 with Dissolve(0.5)
    a "Here's your coke."
    do1 "Thanks, Anna. How much I owe you?"
    a "Zero."
    do1 "UH... I don't like owing people, even if they don't ask for it back."
    a "It's final, Donny. Zero."
    do1 "Ok, ok."
    scene 47-5 boys 67-1 with Dissolve(0.5)
    st2 "..."
    st2 "{i}...THAT ASS!! OMG!!!{/i}"
    play sound cloth_sound1
    scene 47-5 boys 68 with Dissolve(0.5)
    st2 "The first part was pretty good."
    st2 "Let's see if second one holds up."
    scene 47-5 boys 69 with Dissolve(0.5)
    do1 "I heard it's even better."
    st2 "Alright."
    do1 "Bro... I'm LOCKED IN!"
    ro2 "Haha."
    scene 47-5 boys 70 with Dissolve(0.5)
    do1 "Have you seen the first one?"
    a "I don't think so."
    do1 "Well... You might miss some details, but it's ok."
    a "Heh. I'll be fine."
    play music MovementSong_6
    scene 47-5 boys 71 with Dissolve(0.5)
    do1 "OH... YEAH!!!!"
    do1 "LOOKS SO FUCKING GOOD!"
    scene 47-5 boys 72 with Dissolve(0.5)
    pause 2
    scene 47-5 boys 73 with Dissolve(0.5)
    pause 0.5
    scene 47-5 boys 74 with Dissolve(0.5)
    a "Whoa? What are you doing, Donny?"
    a "This is our bucket. Mine and Steve's."
    a "Take from the other one. Heh."
    scene 47-5 boys 75 with Dissolve(0.5)
    do1 "Oh. Shiet. Sorry."
    a "He said while looking at me and still eating my popcorn."
    do1 "Hehe... Sorry, sorry. I just already grabbed it..."
    scene 47-5 boys 76 with Dissolve(0.5)
    st2 "Hey, can I have some?"
    a "Of course. This is our bucket."
    scene 47-5 boys 77 with Dissolve(0.5)
    st2 "Thanks."
    st2 "How do you like the movie, so far?"
    a "It's quite cinematic."
    st2 "Oh, yeah."
    scene 47-5 boys 78 with Dissolve(0.5)
    do1 "You got the stuff, right?"
    ro2 "Always bro."
    do1 "Pass to me after you're done?"
    ro2 "Ye."
    scene 47-5 boys 79 with Dissolve(0.5)
    a "Huh?"
    st2 "Thanks for joining us, you're pretty cool."
    scene 47-5 boys 80 with Dissolve(0.5)
    pause 0.5
    scene 47-5 boys 81 with Dissolve(0.5)
    st2 "Oh... Shit..."
    st2 "I'm... So sorry, Anna."
    st2 "I didn't mean to."
    scene 47-5 boys 82 with Dissolve(0.5)
    a "Heh... It's ok."
    a "I'll forgive you this time."
    scene 47-5 boys 83 with Dissolve(0.5)
    a "Huh?"
    st2 "Those dudes are already smoking, Haha."
    scene 47-5 boys 84 with Dissolve(0.5)
    do1 "Sheesh."
    do1 "That was a good pull, oh yeah."
    scene 47-5 boys 85 with Dissolve(0.5)
    do1 "Oh, hey. Heh..."
    do1 "Just a little extra fun, while watching my favorite franchise!"
    a "You sure it's ok?"
    do1 "Done a thousand times, haha."
    ro2 "Don't wooorrrrry. Heh."
    scene 47-5 boys 86 with Dissolve(0.5)
    do1 "You want some?"
    menu:
        "Sure, some weed never hurt anybody.":
            scene 47-5 boys 87 with Dissolve(0.5)
            a "Why not."
            do1 "That's my girl, haha."
            scene 47-5 boys 88 with Dissolve(0.5)
            a "Last time was pretty fun, hehe."
            scene 47-5 boys 89 with Dissolve(0.5)
            pause 0.5
            scene 47-5 boys 90 with Dissolve(0.5)
            a "Mmm."
            do1 "Yeah!"
            st2 "A proper pull, that's what's up."
            scene 47-5 boys 91 with Dissolve(0.5)
            pause 0.5
            scene 47-5 boys 92 with Dissolve(0.5)
            a "Whew."
            do1 "Nice smoke, Anna!"
            do1 "Hehe."
            scene 47-5 boys 93 with Dissolve(0.5)
            st2 "You're a beast, Anna."
            a "Hehe... Thanks."
            a "It's pretty fun."
        "I'll pass, thanks.":
            do1 "Alright, give it to Steve then."
            pass
    scene 47-5 boys 94 with Dissolve(0.5)
    st2 "We got the best stuff, that's for sure."
    do1 "Word."
    scene 47-5 boys 95 with Dissolve(0.5)
    do1 "This is such a dope moment."
    do1 "Whoooaaa."
    a "Yeah! He's crazy but brave."
    do1 "Haha!"
    a "Awesome!"
    scene 47-5 boys 96 with Dissolve(0.5)
    a "Soo... Uh..."
    a "I got a question."
    a "I think I overheard you in the hallway before."
    a "You sold some stuff. What was it?"
    scene 47-5 boys 97 with Dissolve(0.5)
    st2 "Oh. Yeah. We, umm, sell some of this stuff on the side."
    a "Really?"
    a "No judgment there, just curious."
    scene 47-5 boys 98 with Dissolve(0.5)
    do1 "Oh, yeah. We make a good buck."
    a "How much you said you sold?"
    do1 "Like... 15Gs last month."
    do1 "Not a lot but we're slowly growing."
    do1 "Good little side hustle."
    scene 47-5 boys 99 with Dissolve(0.5)
    a "What if I gave you an opportunity to earn more?"
    do1 "What do you mean?"
    a "Sell some other stuff..."
    a "Earn way more?"
    scene 47-5 boys 100 with Dissolve(0.5)
    a "Would you be interested?"
    scene 47-5 boys 101 with Dissolve(0.5)
    do1 "Heh... I'd have to see the stuff first."
    do1 "Perhaps we could, yeah."
    scene 47-5 boys 102 with Dissolve(0.5)
    ro2 "Easily."
    ro2 "Donny's not the businessminded."
    ro2 "We'd definitely be willing to sell some more stuff, heh."
    ro2 "But gotta see it first. Let's talk more about it after the movie."
    scene black with Dissolve(0.5)
    "Several epic scenes later..."
    scene 47-5 boys 103 with Dissolve(0.5)
    do1 "WHOAAA!!"
    do1 "EPIC SCENE!"
    scene 47-5 boys 104 with Dissolve(0.5)
    pause 1
    stop music
    scene black with Dissolve(0.5)
    pause 1
    play music Chill_Song_1
    scene 47-5 boys 105 with Dissolve(0.5)
    st2 "So, did you enjoy the movie?"
    a "I absolutely did."
    st2 "Being high made it even better, heh."
    scene 47-5 boys 106 with Dissolve(0.5)
    do1 "Alright, let's go."
    scene 47-5 boys 107 with Dissolve(0.5)
    a "Soo... Would you be willing to consider my offer?"
    do1 "Yeah, we're down."
    do1 "When you've got time, come to our place."
    do1 "Show us what you've got."
    a "Ok..."
    scene black with Dissolve(0.5)
    pause 0.5
    scene 47-5 boys 108 with Dissolve(0.5)
    do1 "Those cinematic shots... Fuck me..."
    do1 "That was so epic... I can't believe it!"
    st2 "So true!"
    ro2 "They will be making a third installment, I think."
    do1 "YUP! Can't wait already."
    scene black with Dissolve(0.5)
    pause 0.5
    play sound car_door_close
    scene 47-5 boys 109 with Dissolve(0.5)
    a "Alright... I'll drop you off, grab the stuff, and meet you at your place a bit later."
    do1 "Sure!"
    st2 "Pretty intrigued by what you've got in mind, heh."
    scene black with Dissolve(0.5)
    pause 0.5
    scene 47-5 boys 110 with Dissolve(0.5)
    do1 "Thanks for the right, Anna."
    do1 "We'll see you soon, then."
    a "Yeah!"
    a "Bye!"
    scene 47-5 boys 111 with Dissolve(0.5)
    a "{i}...Alright...{/i}"
    a "{i}...I should get the stuff... I hope they are willing to sell...{/i}"
    a "{i}...That would make my life much easier...{/i}"
    play sound car_sound1
    scene black with Dissolve(0.5)
    pause 0.5
label EP17_Warehouse_1:
    $ EP17_var_6 = True
    play music SecretAgentTwo
    scene 47-6 warehouse 2 with Dissolve(0.5)
    wg1 "Anna. Hello."
    a "Hey, Tyler."
    wg1 "What brings you here?"
    a "On some business, so to speak."
    if EarlHelp == False:
        a "Know where Sergey is?"
        scene 47-6 warehouse 3 with Dissolve(0.5)
        wg1 "He's out."
        wg1 "Will be pretty busy, said as much."
        a "When will he be back?"
        wg1 "No idea."
    scene 47-6 warehouse 4 with Dissolve(0.5)
    a "Ok. I need to do something. Can you help me out?"
    wg1 "What is it?"
    a "I need a sample of the 'product'."
    wg1 "What for?"
    a "Sergey and I discussed that we need to expand the operation to cover the losses..."
    scene 47-6 warehouse 5 with Dissolve(0.5)
    wg1 "I don't know..."
    wg1 "He didn't tell me anything."
    a "It's true."
    a "You know that I was the one that talked to Grayden."
    a "If we don't come up with money soon, there will be big problems."
    if EarlHelp == False:
        a "Not just for me or Sergey, but for you too."
    else:
        a "Not just for me or Michael, but for you as well."
    scene 47-6 warehouse 6 with Dissolve(0.5)
    wg1 "Alright, alright."
    wg1 "You're right. Sorry that I didn't believe you."
    a "It's alright."
    wg1 "I'll be right back."
    scene 47-6 warehouse 7 with Dissolve(0.5)
    a "The air feels tense here..."
    a "Understandably so..."
    scene 47-6 warehouse 8 with Dissolve(0.5)
    a "Hopefully I'll manage to convince the boys."
    a "It would make things a lot easier."
    if EarlHelp == False:
        a "I could probably delegate them to Sergey afterwards."
    scene 47-6 warehouse 9 with Dissolve(0.5)
    wg1 "Alright. Here's the stuff."
    scene 47-6 warehouse 10 with Dissolve(0.5)
    a "How much is in there?"
    wg1 "I think around 100 grams."
    a "I see. Thanks. That should do the trick."
    play sound jacketcloth
    scene 47-6 warehouse 11 with Dissolve(0.5)
    wg1 "I'm trusting you here, ok?"
    a "What do you mean?"
    if EarlHelp == False:
        wg1 "Sergey didn't tell me anything... So..."
        a "He's probably busy with stuff. Like I said, Sergey and I talked about it."
        a "And you can probably agree that we need to sell product faster and the best way to do it is to bring on more people."
    else:
        wg1 "I haven't exactly been made aware of what is going on."
        wg1 "I'm just doing my job of securing this place."
        a "I know, I understand your doubts but you have to realize that we need to sell more products..."
        a "To catch up for lost time and the best way to do it is by getting more people to work for us."
        wg1 "Sure."
    scene 47-6 warehouse 12 with Dissolve(0.5)
    a "Thanks, Tyler."
    wg1 "No problem."
    scene black with Dissolve(0.5)
    "Some time later..."
label EP17_Boys_2:
    $ EP17_var_7 = True
    scene 47-8 boys 1 with Dissolve(0.5)
    a "Alright. Here goes."
    a "Fingers crossed."
    play music bythepool
    play sound doorknock
    scene 47-8 boys 2 with Dissolve(0.5)
    st2 "Anna. Hey. That was fast."
    a "Yeah, I just went got the stuff. Rushed straight back."
    st2 "I see."
    st2 "Come in."
    scene 47-8 boys 3 with Dissolve(0.5)
    do1 "So, you got the stuff, yeah?"
    a "Yeah."
    st2 "Hah. Let's see if it's actually flour or something."
    scene 47-8 boys 4 with Dissolve(0.5)
    a "This is the package."
    st2 "Wow. That's big."
    do1 "Um..."
    do1 "Didn't actually think you'd have it."
    scene 47-8 boys 5 with Dissolve(0.5)
    do1 "I don't know..."
    do1 "This is pretty serious stuff."
    ro2 "Don't tell me you're bitching out, dude."
    do1 "Umm..."
    scene 47-8 boys 6 with Dissolve(0.5)
    st2 "I ain't a pussy like Donny. You can give it to me."
    a "Ok."
    st2 "If it's the real deal, I'm in."
    scene 47-8 boys 7 with Dissolve(0.5)
    st2 "How much is in the package?"
    a "I think 100 grams."
    st2 "What?"
    st2 "That's a lot. Damn."
    st2 "We could earn a hefty sum."
    scene 47-8 boys 8 with Dissolve(0.5)
    st2 "You mind if I try it out?"
    a "Why not."
    st2 "Hehe, Awesome!"
    play sound undress
    scene 47-8 boys 10 with Dissolve(0.5)
    st2 "Alright."
    do1 "You sure about this?"
    st2 "If we sell this, we'd earn a lot more than we do by selling weed."
    scene 47-8 boys 11 with Dissolve(0.5)
    st2 "Let's see."
    scene 47-8 boys 12 with Dissolve(0.5)
    ro2 "Steve is right."
    ro2 "We could earn a pretty penny, even after Anna takes her cut."
    do1 "Maybe..."
    do1 "I'm not sure about this."
    ro2 "We've got contacts. We could sell it fast too."
    ro2 "Bro, half our class wants to get high off of it."
    scene 47-8 boys 13 with Dissolve(0.5)
    a "You'd be doing me a service."
    do1 "Well..."
    st2 "I'm pretty much sold, just... Wanna taste it."
    scene 47-8 boys 14 with Dissolve(0.5)
    st2 "{b}*Sniff*{/b}"
    scene 47-8 boys 15 with Dissolve(0.5)
    st2 "AAHHHHHH!"
    st2 "HAHA!"
    scene 47-8 boys 16 with Dissolve(0.5)
    st2 "WHOA!"
    st2 "OK!!!"
    st2 "WOWOWOWOW!"
    st2 "VERY GOOD! HAHA!"
    scene 47-8 boys 17 with Dissolve(0.5)
    st2 "That really hits the spot!"
    st2 "Gotta admit. This shit is FUCKING GOOD!"
    scene 47-8 boys 18 with Dissolve(0.5)
    a "Heh. I knew it."
    do1 "Alright, alright. Give me that shit."
    st2 "Hehe. Word."
    scene 47-8 boys 19 with Dissolve(0.5)
    st2 "There."
    do1 "Oh boy."
    do1 "Been a while since I got some."
    scene 47-8 boys 20 with Dissolve(0.5)
    do1 "{b}*Sniff*{/b}"
    do1 "AHHHH."
    scene 47-8 boys 21 with Dissolve(0.5)
    do1 "Hoho WHEEEE!"
    do1 "Alright"
    do1 "Hit me like a fucking train!"
    do1 "Wide awake!"
    scene 47-8 boys 22 with Dissolve(0.5)
    do1 "You brought the good good."
    do1 "WOW. So much energy."
    do1 "Le't fucking gooooO!!!"
    scene 47-8 boys 23 with Dissolve(0.5)
    a "So? You'd be willing to help me out?"
    do1 "I'd be willing to do so much more..."
    do1 "So hot..."
    scene 47-8 boys 24 with Dissolve(0.5)
    do1 "Lemme just. Give those sexy lips a kiss."
    a "Oh. Heh."
    play sound kisspeck
    scene 47-8 boys 25 with Dissolve(0.5)
    a "Mmm..."
    do1 "Mmm..."
    scene 47-8 boys 26 with Dissolve(0.5)
    st2 "Haha!"
    st2 "Ma man's going wild!"
    scene 47-8 boys 27 with Dissolve(0.5)
    ro2 "Well, what about you?"
    ro2 "You gonna join us for a funzy one?"
    a "Well..."
    menu:
        "Of course. I'd like to have some fun with the boys.":
            $ EP17_Boys_Lower_Cut = True
            scene 47-8 boys 28 with Dissolve(0.5)
            a "Who do you take me for, a pussy?"
            ro2 "Haha! That's what I'm talking about!"
            scene 47-8 boys 29 with Dissolve(0.5)
            a "Scoot over and let me sit down!"
            st2 "Alright, alright!"
            scene 47-8 boys 30 with Dissolve(0.5)
            st2 "Didn't know you had it in you."
            a "I'm not a pushover, hehe."
            scene 47-8 boys 31 with Dissolve(0.5)
            do1 "This little fucker is the fun stuff, the nose candy, the blow, the Florida snow... Hehe."
            do1 "Quite an amazing piece of invention by humankind."
            scene 47-8 boys 32 with Dissolve(0.5)
            a "{b}*Sniff*{/b}"
            a "AHHHH!!!"
            scene 47-8 boys 33 with Dissolve(0.5)
            a "Whoaaa..."
            a "WOOOOW!"
            a "That's amazing!!!"
            do1 "Right?"
            scene 47-8 boys 34 with Dissolve(0.5)
            st2 "I feel invincible!"
            st2 "So much energy!"
            a "SAME!"
            a "This shit is goood!"
            scene 47-8 boys 35 with Dissolve(0.5)
            do1 "While...we are on topic!"
            do1 "Wanted to ask about our cut."
            do1 "What can we expect?"
            scene 47-8 boys 36 with Dissolve(0.5)
            do1 "You gonna pay us decently right?"
            do1 "We'd wanna earn some, we'd be down to earn some. Like nice percentage."
            do1 "You know what I mean? Just a nice percentage, like... I don't know."
            do1 "HEHE!"
        "I don't use my own supply.":
            scene 47-8 boys 28 with Dissolve(0.5)
            a "Just the way it is."
            ro2 "Whoa."
            ro2 "Fair enough."
            ro2 "Living by a code."
            st2 "Haha. Your loss but ok."
            do1 "Anyway, what about our cut?"
    do1 "We'd want like... 30%%. That's reasonable I think..."
    menu:
        "Well. How about 15%% and Anna lets Rocco sniff it out of her ass.":
            label EP17_Boys_Sex_Scene:
            $ persistent.scene_50 = True
            play music GratitudeSong
            ro2 "WHOA. WHAT?"
            st2 "Umm... Well... HAHA!"
            st2 "If you throw in some extra. I'm down!"
            ro2 "DUDE. OF COURSE, we're in."
            scene 47-8 boys 38 with Dissolve(0.5)
            a "So we got a deal?"
            ro2 "Oh yeah!"
            scene 47-8 boys 39 with Dissolve(0.5)
            a "Well then. Let me just take this off and get comfy."
            ro2 "DAAAAMN!"
            play sound undress
            scene 47-8 boys 40 with Dissolve(0.5)
            pause 0.5
            scene 47-8 boys 41 with Dissolve(0.5)
            do1 "Fuckin... Wow..."
            scene 47-8 boys 42 with Dissolve(0.5)
            a "Hehe..."
            a "I bet you can barely contain yourselves."
            scene 47-8 boys 43 with Dissolve(0.5)
            a "Well, get some on me."
            a "Don't have all day."
            do1 "Ain't that the truth!"
            scene 47-8 boys 44 with Dissolve(0.5)
            pause 0.5
            scene 47-8 boys 45 with Dissolve(0.5)
            do1 "There."
            a "Heh. I like your hands on my buttcheeks."
            do1 "Hehe..."
            scene 47-8 boys 46 with Dissolve(0.5)
            do1 "Cmon dude..."
            do1 "Lucky bastard!"
            a "The party ain't over yet, hehe."
            scene 47-8 boys 47 with Dissolve(0.5)
            ro2 "That ass is just... FUCKING MAGNIFICENT!"
            a "Hehe. I know."
            a "So... 15%% are yours, guys."
            scene 47-8 boys 48 with Dissolve(0.5)
            ro2 "Hehe..."
            scene 47-8 boys 49 with Dissolve(0.5)
            ro2 "{b}*Sniff*{/b}"
            ro2 "OHHH!"
            scene 47-8 boys 50 with Dissolve(0.5)
            ro2 "OH YEAHH!"
            ro2 "YOU GUYS WERE RIGHT!"
            ro2 "Fuck this is some good stuff!"
            scene 47-8 boys 51 with Dissolve(0.5)
            a "AAhhh..."
            a "You can sniff down there a bit more if you'd like hehe."
            scene 47-8 boys 52 with Dissolve(0.5)
            ro2 "FUCK YEAH!"
            scene 47-8 boys 53 with Dissolve(0.5)
            ro2 "A literal dream come true!"
            ro2 "FUUCKING HELL!!! SO GOOD!"
            scene 47-8 boys 54 with Dissolve(0.5)
            a "Ahhh... Oh..."
            a "Looks like you're enjoying it hehe..."
            do1 "WHOA!"
            do1 "I want some too."
            st2 "YEAH!"
            play sound licking_1
            scene 47-8 boys 55 with Dissolve(0.5)
            ro2 "Mmmm..."
            ro2 "Ahhha..."
            scene 47-8 boys 56 with Dissolve(0.5)
            a "Your mouth is pretty good, to be honest."
            a "Got a lot of practice it seems, hehe."
            a "Ahh..."
            $ different_choice_menu = True
            $ EP16_Anim_Option = 1
            $ EP16_Anim_Speed = 1
            scene black
            show EP17_Boys_Anim_1 with Dissolve(0.5)
            a "OOhh... Woww..."
            a "Rocco..."
            play sound jerk2 loop
            menu EP17_Boys_Menu_1:
                "View 1":
                    hide EP17_Boys_Anim_1
                    hide EP17_Boys_Anim_2
                    show EP17_Boys_Anim_1 with Dissolve(0.5)
                    jump EP17_Boys_Menu_1
                "View 2":
                    hide EP17_Boys_Anim_1
                    hide EP17_Boys_Anim_2
                    show EP17_Boys_Anim_2 with Dissolve(0.5)
                    jump EP17_Boys_Menu_1
                "Continue":
                    hide EP17_Boys_Anim_1
                    hide EP17_Boys_Anim_2
                    $ different_choice_menu = False
                    stop sound
                    pass
            scene 47-8 boys 57 with Dissolve(0.5)
            do1 "Dude."
            do1 "We want some of that too."
            scene 47-8 boys 58 with Dissolve(0.5)
            a "Then why are you still clothed?"
            a "My front is free."
            do1 "Oh... Wow..."
            do1 "Umm..."
            scene 47-8 boys 59 with Dissolve(0.5)
            do1 "You... Sure?"
            a "Would I let some dude sniff and lick my backside if I wasn't sure?"
            do1 "Heh."
            scene 47-8 boys 60 with Dissolve(0.5)
            pause 0.5
            play sound undress
            scene 47-8 boys 61 with Dissolve(0.5)
            pause 0.5
            scene 47-8 boys 62 with Dissolve(0.5)
            a "Well, well."
            a "Aren't you full of surprises."
            do1 "Thanks."
            scene 47-8 boys 63 with Dissolve(0.5)
            a "I bet you like the way I touch that cock?"
            do1 "Ah... Yeah."
            a "It's so stiff..."
            a "So hard..."
            scene 47-8 boys 64 with Dissolve(0.5)
            a "I know you like that."
            a "Yeah?"
            a "You enjoyyyy when I touch that rod?"
            do1 "Fuuck..."
            $ different_choice_menu = True
            $ EP16_Anim_Option = 1
            $ EP16_Anim_Speed = 1
            scene black
            show EP17_Boys_Anim_3 with Dissolve(0.5)
            ro2 "MMmmmmmmMMM."
            do1 "Aahh!"
            play sound jerk2 loop
            menu EP17_Boys_Menu_2:
                "View 1":
                    hide EP17_Boys_Anim_3
                    hide EP17_Boys_Anim_4
                    show EP17_Boys_Anim_3 with Dissolve(0.5)
                    jump EP17_Boys_Menu_2
                "View 2":
                    hide EP17_Boys_Anim_3
                    hide EP17_Boys_Anim_4
                    show EP17_Boys_Anim_4 with Dissolve(0.5)
                    jump EP17_Boys_Menu_2
                "Continue":
                    hide EP17_Boys_Anim_3
                    hide EP17_Boys_Anim_4
                    $ different_choice_menu = False
                    stop sound
                    pass
            scene 47-8 boys 65 with Dissolve(0.5)
            st2 "I can't just stand there like a dumbass..."
            a "What are you waiting for?"
            a "Get naked and join in!"
            play sound undress
            scene 47-8 boys 66 with Dissolve(0.5)
            st2 "You down to switch?"
            st2 "You already got some action."
            ro2 "Fine, fine."
            scene 47-8 boys 67 with Dissolve(0.5)
            st2 "That ass."
            ro2 "Impeccable, I know. Heh."
            st2 "Yeah..."
            st2 "I can't believe she's in our flat like this."
            a "What are you doing back there?"
            scene 47-8 boys 68 with Dissolve(0.5)
            a "Ohh..."
            a "Mmm..."
            st2 "Fuuckk..."
            scene 47-8 boys 69 with Dissolve(0.5)
            a "You like that big ass, Steve?"
            st2 "I LOVE IT!"
            show EP17_Boys_Anim_5 with Dissolve(0.5)
            pause
            st2 "Ohh.. Yeahhh!"
            st2 "That's just fucking right."
            a "Aren't my cheeks fucking amazing?"
            st2 "Out of this world!"
            scene 47-8 boys 70 with Dissolve(0.5)
            hide EP17_Boys_Anim_5
            st2 "I barely know what to do with all that ass..."
            a "Whatever you'd like, baby."
            a "It's all yours."
            play sound femgasp_1
            stop music fadeout 3
            scene 47-8 boys 71 with Dissolve(0.5)
            a "Ahh..."
            a "Ohh...FF..."
            st2 "Yeahh... That's it... That hole is good..."
            play music closuresong
            scene 47-8 boys 72 with Dissolve(0.5)
            a "AAHHHAAH!"
            a "Go deeper..."
            a "Oh... Steve!"
            do1 "Damn she's horny."
            do1 "And so fucking hot!"
            scene 47-8 boys 73 with Dissolve(0.5)
            ro2 "Time for me to join in, too!"
            a "Yeah!"
            a "Ahh..."
            scene 47-8 boys 74 with Dissolve(0.5)
            a "Two big, nice cocks in front of me."
            a "Can't choose!"
            a "Ahh..."
            a "I'll just have em both!"
            scene 47-8 boys 75 with Dissolve(0.5)
            a "Don't you think so?"
            ro2 "Oh, yeah!"
            ro2 "You're the hottest chick ever!"
            scene 47-8 boys 76 with Dissolve(0.5)
            a "Do you like when the hottest chick ever masturbates your cock like this?"
            ro2 "Girl, you don't even know..."
            ro2 "Heaven!"
            ro2 "MHMM!!!"
            do1 "OH YEAH!"
            scene 47-8 boys 77 with Dissolve(0.5)
            a "Hehe..."
            a "Aah... I like being like this."
            a "So fun... Mhmm..."
            $ different_choice_menu = True
            $ EP16_Anim_Option = 1
            $ EP16_Anim_Speed = 1
            scene black
            play sound jerk loop
            show EP17_Boys_Anim_6 with Dissolve(0.5)
            ro2 "MMmmmmmmMMM."
            do1 "Aahh!"
            menu EP17_Boys_Menu_3:
                "Slower":
                    hide EP17_Boys_Anim_6
                    hide EP17_Boys_Anim_7
                    show EP17_Boys_Anim_6 with Dissolve(0.5)
                    jump EP17_Boys_Menu_3
                "Faster":
                    hide EP17_Boys_Anim_6
                    hide EP17_Boys_Anim_7
                    show EP17_Boys_Anim_7 with Dissolve(0.5)
                    jump EP17_Boys_Menu_3
                "Continue":
                    hide EP17_Boys_Anim_6
                    hide EP17_Boys_Anim_7
                    $ different_choice_menu = False
                    stop sound
                    pass
            scene 47-8 boys 78 with Dissolve(0.5)
            do1 "I wanna use your mouth, Anna..."
            do1 "It needs to be used."
            a "Oh, I like you taking initiative."
            scene 47-8 boys 79 with Dissolve(0.5)
            do1 "I cannot contain myself."
            do1 "SO FUCKING AMAZING!"
            play sound jerk3 loop
            scene 47-8 boys 80 with Dissolve(0.5)
            pause 1
            scene 47-8 boys 81 with Dissolve(0.5)
            a "MMMmm..."
            do1 "AHH FUCK!"
            scene 47-8 boys 82 with Dissolve(0.5)
            a "MMMMM!!!"
            a "KHA!"
            "Anna was finally locked in."
            "Pinned between two horny dudes."
            "And She loved every second of it."
            scene 47-8 boys 83 with Dissolve(0.5)
            st2 "Fuck me..."
            st2 "That pussy is S tier."
            st2 "I can barely keep up!"
            a "AHH."
            st2 "FUCK!"
            $ different_choice_menu = True
            $ EP17_Anim_Option = 1
            $ EP17_Anim_Speed = 1
            scene black
            play sound jerk loop
            show EP17_Boys_Anim_8 with Dissolve(0.5)
            a "Ohh... Boys... I'm so turned on..."
            a "Love being filled by your cocks."
            st2 "Daaamn, Anna!"
            menu EP17_Boys_Menu_4:
                "View 1":
                    scene black with Dissolve(0.25)
                    hide EP17_Boys_Anim_8
                    hide EP17_Boys_Anim_9
                    hide EP17_Boys_Anim_10
                    hide EP17_Boys_Anim_11
                    if EP17_Anim_Speed == 1:
                        show EP17_Boys_Anim_8 with Dissolve(0.5)
                    if EP17_Anim_Speed == 2:
                        show EP17_Boys_Anim_9 with Dissolve(0.5)
                    $ EP17_Anim_Option = 1
                    jump EP17_Boys_Menu_4
                "View 2":
                    scene black with Dissolve(0.25)
                    hide EP17_Boys_Anim_8
                    hide EP17_Boys_Anim_9
                    hide EP17_Boys_Anim_10
                    hide EP17_Boys_Anim_11
                    if EP17_Anim_Speed == 1:
                        show EP17_Boys_Anim_10 with Dissolve(0.5)
                    if EP17_Anim_Speed == 2:
                        show EP17_Boys_Anim_11 with Dissolve(0.5)
                    $ EP17_Anim_Option = 2
                    jump EP17_Boys_Menu_4
                "Slower":
                    scene black with Dissolve(0.25)
                    hide EP17_Boys_Anim_8
                    hide EP17_Boys_Anim_9
                    hide EP17_Boys_Anim_10
                    hide EP17_Boys_Anim_11
                    if EP17_Anim_Option == 1:
                        show EP17_Boys_Anim_8 with Dissolve(0.5)
                    if EP17_Anim_Option == 2:
                        show EP17_Boys_Anim_10 with Dissolve(0.5)
                    $ EP17_Anim_Speed = 1
                    jump EP17_Boys_Menu_4
                "Faster":
                    scene black with Dissolve(0.25)
                    hide EP17_Boys_Anim_8
                    hide EP17_Boys_Anim_9
                    hide EP17_Boys_Anim_10
                    hide EP17_Boys_Anim_11
                    if EP17_Anim_Option == 1:
                        show EP17_Boys_Anim_9 with Dissolve(0.5)
                    if EP17_Anim_Option == 2:
                        show EP17_Boys_Anim_11 with Dissolve(0.5)
                    $ EP17_Anim_Speed = 2
                    jump EP17_Boys_Menu_4
                "Continue":
                    hide EP17_Boys_Anim_8
                    hide EP17_Boys_Anim_9
                    hide EP17_Boys_Anim_10
                    hide EP17_Boys_Anim_11
                    $ different_choice_menu = False
                    stop sound
                    pass
            scene 47-8 boys 84 with Dissolve(0.5)
            st2 "SHIIETT!"
            st2 "I'm barely able hold on..."
            scene 47-8 boys 85 with Dissolve(0.5)
            st2 "I'm... Getting real close, Anna."
            st2 "I wanna cum inside..."
            a "MHmmm."
            st2 "Fuck yeah!"
            scene 47-8 boys 86 with Dissolve(0.5)
            st2 "SHIIIIT!"
            st2 "THAT'S SO GOOOD!"
            a "MMMMM!"
            st2 "AHHH."
            st2 "AH!!!"
            play sound cum_sound
            scene 47-8 boys 87 with flash
            pause 1
            scene 47-8 boys 88 with Dissolve(0.5)
            st2 "That's a proper load. Fuck!"
            scene 47-8 boys 89 with Dissolve(0.5)
            a "Hehe..."
            a "I knew you'd like my pussy."
            a "I'd say a good bargain, eh?"
            st2 "OH yeah!"
            scene 47-8 boys 90 with Dissolve(0.5)
            a "Well."
            scene 47-8 boys 91 with Dissolve(0.5)
            a "Who'd like to go next?"
            a "I got plenty of room left in there. Hehe..."
            do1 "Fuck. I wanna do your pussy!"
            scene 47-8 boys 92 with Dissolve(0.5)
            pause 0.5
            scene 47-8 boys 93 with Dissolve(0.5)
            do1 "This is such a hot view."
            do1 "Your tits are so beautiful..."
            do1 "So plump."
            scene 47-8 boys 94 with Dissolve(0.5)
            do1 "I just can't wait any longer..."
            do1 "Anna... Fuck..."
            a "Get in there, Donny."
            a "Don't keep me waiting."
            scene 47-8 boys 95 with Dissolve(0.5)
            do1 "Aahhh!"
            do1 "Oh..."
            a "Yeah, Donny. Keep going deeper!"
            play sound female_moan_3
            scene 47-8 boys 96 with Dissolve(0.5)
            a "AHH!"
            scene 47-8 boys 97 with Dissolve(0.5)
            a "That's right."
            a "Now rail me!"
            do1 "I... I will do you so good!"
            do1 "SO FUCKING GOOD!"
            do1 "YOU'RE A GODDESS!"
            scene 47-8 boys 98 with Dissolve(0.5)
            a "AAHHH!!"
            a "KEEP SAYING THOSE HOT THINGS TO ME!"
            a "AHH!"
            scene 47-8 boys 99 with Dissolve(0.5)
            ro2 "I can't believe we're fucking this divine vision!"
            ro2 "A sex deity!"
            a "OHH!"
            $ different_choice_menu = True
            $ EP17_Anim_Option = 1
            $ EP17_Anim_Speed = 1
            scene black
            play sound jerk loop
            show EP17_Boys_Anim_14 with Dissolve(0.5)
            a "FUck... FUCK FUCK!"
            do1 "GODDAMN!"
            do1 "AHH! AAAHH!!!"
            ro2 "MMHH!!!"
            play audio moaningthree
            menu EP17_Boys_Menu_5:
                "View 1":
                    scene black with Dissolve(0.25)
                    hide EP17_Boys_Anim_12
                    hide EP17_Boys_Anim_13
                    hide EP17_Boys_Anim_14
                    hide EP17_Boys_Anim_15
                    if EP17_Anim_Speed == 1:
                        show EP17_Boys_Anim_14 with Dissolve(0.5)
                    if EP17_Anim_Speed == 2:
                        show EP17_Boys_Anim_15 with Dissolve(0.5)
                    $ EP17_Anim_Option = 1
                    jump EP17_Boys_Menu_5
                "View 2":
                    scene black with Dissolve(0.25)
                    hide EP17_Boys_Anim_12
                    hide EP17_Boys_Anim_13
                    hide EP17_Boys_Anim_14
                    hide EP17_Boys_Anim_15
                    if EP17_Anim_Speed == 1:
                        show EP17_Boys_Anim_12 with Dissolve(0.5)
                    if EP17_Anim_Speed == 2:
                        show EP17_Boys_Anim_13 with Dissolve(0.5)
                    $ EP17_Anim_Option = 2
                    jump EP17_Boys_Menu_5
                "Slower":
                    scene black with Dissolve(0.25)
                    hide EP17_Boys_Anim_12
                    hide EP17_Boys_Anim_13
                    hide EP17_Boys_Anim_14
                    hide EP17_Boys_Anim_15
                    if EP17_Anim_Option == 1:
                        show EP17_Boys_Anim_14 with Dissolve(0.5)
                    if EP17_Anim_Option == 2:
                        show EP17_Boys_Anim_12 with Dissolve(0.5)
                    $ EP17_Anim_Speed = 1
                    jump EP17_Boys_Menu_5
                "Faster":
                    scene black with Dissolve(0.25)
                    hide EP17_Boys_Anim_12
                    hide EP17_Boys_Anim_13
                    hide EP17_Boys_Anim_14
                    hide EP17_Boys_Anim_15
                    if EP17_Anim_Option == 1:
                        show EP17_Boys_Anim_15 with Dissolve(0.5)
                    if EP17_Anim_Option == 2:
                        show EP17_Boys_Anim_13 with Dissolve(0.5)
                    $ EP17_Anim_Speed = 2
                    jump EP17_Boys_Menu_5
                "Continue":
                    hide EP17_Boys_Anim_12
                    hide EP17_Boys_Anim_13
                    hide EP17_Boys_Anim_14
                    hide EP17_Boys_Anim_15
                    $ different_choice_menu = False
                    stop sound
                    pass
            play audio female_moan_1
            scene 47-8 boys 100 with Dissolve(0.5)
            "Anna was overtaken by powerful pleasure."
            "She liked to be used like this."
            "She enjoyed the intense pleasure so much so that she lost sense of reality, yet again."
            scene 47-8 boys 101 with Dissolve(0.5)
            a "Come onnnn!!"
            a "COME ONNN!!!"
            a "FILL ME UP!"
            do1 "AHHH!"
            do1 "AHHHAAAAA!"
            do1 "FUUUCKK!"
            play sound cum_sound
            scene 47-8 boys 102 with flash
            pause 2
            scene 47-8 boys 103 with Dissolve(0.5)
            a "Another load in heh."
            a "I'm pretty good at convincing, aren't I?"
            do1 "Oh... Yeah!"
            scene 47-8 boys 104 with Dissolve(0.5)
            do1 "You definitely are..."
            do1 "And so fucking hot!"
            a "Hehe..."
            scene 47-8 boys 105 with Dissolve(0.5)
            a "And what about you?"
            a "Also want some fun stuff?"
            ro2 "You read my mind!"
            ro2 "I want to put it in you so bad!"
            scene 47-8 boys 106 with Dissolve(0.5)
            a "I'm all yours."
            ro2 "I want you to get up."
            ro2 "I want to hold you in the air as I fuck you."
            scene 47-8 boys 107 with Dissolve(0.5)
            pause 1
            play sound undress
            scene 47-8 boys 108 with Dissolve(0.5)
            a "Oh!"
            a "Hehe."
            ro2 "There we go."
            ro2 "You like that?"
            a "Oh, yes!"
            scene 47-8 boys 109 with Dissolve(0.5)
            a "AHHH!"
            ro2 "YEAH!"
            ro2 "That pussy's perfect!"
            a "OHHH!!"
            scene 47-8 boys 110 with Dissolve(0.5)
            a "Yeah! Just keep fucking me like that."
            a "Don't stop now! MHHFF!"
            ro2 "No intention. AHH!"
            scene 47-8 boys 111 with Dissolve(0.5)
            a "FUUCKK!!"
            ro2 "FUUUCKKK!!"
            ro2 "YES! YES! YES!"
            a "ROCCO!!"
            $ different_choice_menu = True
            $ EP17_Anim_Option = 1
            $ EP17_Anim_Speed = 1
            scene black
            play sound jerk loop
            show EP17_Boys_Anim_18 with Dissolve(0.5)
            a "DEEPER ROCCO!"
            a "DEEPER!"
            ro2 "AAHH."
            ro2 "AHHH!!!"
            play audio moaningone
            menu EP17_Boys_Menu_6:
                "View 1":
                    scene black with Dissolve(0.25)
                    hide EP17_Boys_Anim_16
                    hide EP17_Boys_Anim_17
                    hide EP17_Boys_Anim_18
                    hide EP17_Boys_Anim_19
                    if EP17_Anim_Speed == 1:
                        show EP17_Boys_Anim_18 with Dissolve(0.5)
                    if EP17_Anim_Speed == 2:
                        show EP17_Boys_Anim_19 with Dissolve(0.5)
                    $ EP17_Anim_Option = 1
                    jump EP17_Boys_Menu_6
                "View 2":
                    scene black with Dissolve(0.25)
                    hide EP17_Boys_Anim_16
                    hide EP17_Boys_Anim_17
                    hide EP17_Boys_Anim_18
                    hide EP17_Boys_Anim_19
                    if EP17_Anim_Speed == 1:
                        show EP17_Boys_Anim_16 with Dissolve(0.5)
                    if EP17_Anim_Speed == 2:
                        show EP17_Boys_Anim_17 with Dissolve(0.5)
                    $ EP17_Anim_Option = 2
                    jump EP17_Boys_Menu_6
                "Slower":
                    scene black with Dissolve(0.25)
                    hide EP17_Boys_Anim_16
                    hide EP17_Boys_Anim_17
                    hide EP17_Boys_Anim_18
                    hide EP17_Boys_Anim_19
                    if EP17_Anim_Option == 1:
                        show EP17_Boys_Anim_18 with Dissolve(0.5)
                    if EP17_Anim_Option == 2:
                        show EP17_Boys_Anim_16 with Dissolve(0.5)
                    $ EP17_Anim_Speed = 1
                    jump EP17_Boys_Menu_6
                "Faster":
                    scene black with Dissolve(0.25)
                    hide EP17_Boys_Anim_16
                    hide EP17_Boys_Anim_17
                    hide EP17_Boys_Anim_18
                    hide EP17_Boys_Anim_19
                    if EP17_Anim_Option == 1:
                        show EP17_Boys_Anim_19 with Dissolve(0.5)
                    if EP17_Anim_Option == 2:
                        show EP17_Boys_Anim_17 with Dissolve(0.5)
                    $ EP17_Anim_Speed = 2
                    jump EP17_Boys_Menu_6
                "Continue":
                    hide EP17_Boys_Anim_16
                    hide EP17_Boys_Anim_17
                    hide EP17_Boys_Anim_18
                    hide EP17_Boys_Anim_19
                    $ different_choice_menu = False
                    stop sound
                    pass
            scene 47-8 boys 112 with Dissolve(0.5)
            st2 "DAMN!"
            st2 "All this cocaine got me ready for another round!"
            a "AH!"
            st2 "Yeah! Anna is too hot to not fuck again!"
            scene 47-8 boys 113 with Dissolve(0.5)
            a "Come and... Ahh.. Get it!! AH!!"
            a "FUCK. AH!"
            a "I got my backside ready!"
            a "AH!"
            scene 47-8 boys 114 with Dissolve(0.5)
            pause 1
            scene 47-8 boys 115 with Dissolve(0.5)
            st2 "OH yeah."
            "Steve slid his tip across Anna's asshole."
            "The hole was loosening in anticipation."
            scene 47-8 boys 116 with Dissolve(0.5)
            a "OH FUUCK!"
            st2 "YEAH!"
            ro2 "YEEAH!!!"
            ro2 "YOU LIKE THAT?"
            a "OOHH... YESSS!!"
            $ different_choice_menu = True
            $ EP16_Anim_Option = 1
            $ EP16_Anim_Speed = 1
            scene black
            play sound jerk loop
            show EP17_Boys_Anim_20 with Dissolve(0.5)
            ro2 "MMmmmmmmMMM."
            st2 "FUCK!"
            st2 "AH!"
            a "FILL ME UP BOYS!!!"
            menu EP17_Boys_Menu_7:
                "Slower":
                    hide EP17_Boys_Anim_20
                    hide EP17_Boys_Anim_21
                    show EP17_Boys_Anim_20 with Dissolve(0.5)
                    jump EP17_Boys_Menu_7
                "Faster":
                    hide EP17_Boys_Anim_20
                    hide EP17_Boys_Anim_21
                    show EP17_Boys_Anim_21 with Dissolve(0.5)
                    jump EP17_Boys_Menu_7
                "Continue":
                    hide EP17_Boys_Anim_20
                    hide EP17_Boys_Anim_21
                    $ different_choice_menu = False
                    stop sound
                    pass
            scene 47-8 boys 117 with Dissolve(0.5)
            a "OAAAAHHAA!"
            ro2 "AHHH!!!"
            st2 "MHAAAA!"
            "All three of them were moaning so loud it could be heard in the hallway."
            scene 47-8 boys 118 with Dissolve(0.5)
            ro2 "I'm getting super close!"
            st2 "YEAH!"
            a "THEN FILL ME UP EVEN MORE!"
            scene 47-8 boys 119 with Dissolve(0.5)
            a "AHHH!"
            play audio moaninglong_1
            show EP17_Boys_Anim_21 with Dissolve(0.5)
            a "AAHHHH!!!!"
            with flash
            with flash
            ro2 "AAH!!!"
            ro2 "FUUCKKK!"
            with flash
            st2 "OHHHHAAAA!!!"
            with flash
            scene 47-8 boys 120 with flash
            pause 1
            play sound cum_sound
            scene 47-8 boys 121 with flash
            pause
            scene 47-8 boys 122 with Dissolve(0.5)
            pause 0.5
            scene 47-8 boys 123 with Dissolve(0.5)
            pause 1
            scene 47-8 boys 124 with Dissolve(0.5)
            a "Well, looks like you've all been 'convinced' hehe."
            st2 "Thoroughly, in fact!"
            scene 47-8 boys 125 with Dissolve(0.5)
            do1 "Yeah, yeah."
            do1 "I could've also gone another round, probably."
            st2 "SUUURE DUDE!"
            a "Well. If you behave. I might be willing to do it again sometime."
            scene 47-8 boys 126 with Dissolve(0.5)
            a "Ah."
            a "That was amazing."
            a "I really had a lot of fun."
            a "So... We got a deal?"
            scene 47-8 boys 127 with Dissolve(0.5)
            st2 "Fuck yeah."
            st2 "We're gonna sell your stuff and then some."
            a "I'm glad to hear it."
            scene black with Dissolve(0.5)
            pause 1
            scene 47-8 boys 128 with Dissolve(0.5)
            do1 "So... How soon do you need this sold?"
            a "As soon as possible."
            a "I'm not going to divulge a lot but, the funds are urgently needed."
            scene 47-8 boys 129 with Dissolve(0.5)
            a "Can I count on your discretion and quick results?"
            do1 "Yeah. There are some parties happening soon, so we'll get shit done fast."
            a "Good."
            scene 47-8 boys 130 with Dissolve(0.5)
            a "We'll do this a couple of times and after the urgent issue is resolved..."
            a "Perhaps you'll be willing to sell more."
            a "Think about it."
            do1 "We will."
            scene 47-8 boys 131 with Dissolve(0.5)
            a "See you around boys. This was FUN!"
            do1 "Hehe."
            ro2 "It really was!"
            st2 "Cya! We won't let you down!"
            scene black with Dissolve(0.5)
            pause 1
            $ renpy.end_replay()
            scene 47-8 boys 132 with Dissolve(0.5)
            a "Well, that's done with."
            a "I hope neither of us gets in trouble."
            a "They seem loyal, though."
            scene 47-8 boys 133 with Dissolve(0.5)
            a "What else do I have left to do..."
            a "Have to head to the bar."
        "Alright, 30%% it is.":
            scene 47-8 boys 28 with Dissolve(0.5)
            a "Does that sound fair?"
            st2 "Yeah. We think that works."
            st2 "Guys?"
            ro2 "We're in."
            do1 "Yeah. That's good money, heh."
            play sound undress
            scene black with Dissolve(0.5)
            pause 1
            scene 47-8 boys 129 with Dissolve(0.5)
            a "Can I count on your discretion and quick results?"
            do1 "Yeah. There are some parties happening soon, so we'll get shit done fast."
            a "Good."
            scene 47-8 boys 130 with Dissolve(0.5)
            a "We'll do this a couple of times and after the urgent issue is resolved..."
            a "Perhaps you'll be willing to sell more."
            a "Think about it."
            do1 "We will."
            scene 47-8 boys 131 with Dissolve(0.5)
            a "See you around boys. Good luck with the product, try not to spend all the money in one place."
            do1 "Hehe."
            st2 "Cya! We won't let you down!"
            scene black with Dissolve(0.5)
            pause 1
            scene 47-8 boys 132 with Dissolve(0.5)
            a "Well, that's done with."
            a "I hope neither of us gets in trouble."
            a "They seem loyal, though."
            scene 47-8 boys 133 with Dissolve(0.5)
            a "What else do I have left to do..."
            a "Have to head to the bar."
    play sound jacketcloth
    scene black with Dissolve(0.5)
    pause 1
    jump EP17_Agent
label EP17_Office:
    $ EP17_var_3 = True
    scene 47-2 office 1 with Dissolve(0.5)
    a "Hey, Emily."
    a "Doing good?"
    e "Anna!"
    scene 47-2 office 2 with Dissolve(0.5)
    e "I'm quite alright."
    e "Working... Maybe."
    a "By playing solitaire?"
    e "Well. a break after such a long morning. Heh."
    scene 47-2 office 3 with Dissolve(0.5)
    a "Soo. Are you ready for today?"
    e "You mean the bar?"
    a "Indeed."
    e "Already, wow. Umm..."
    a "Yeah, I need a helping hand you're just the person I'd trust with it."
    e "Alright. But. Will I get something thrown my way?"
    scene 47-2 office 4 with Dissolve(0.5)
    a "You sure will."
    a "If we do a good job, a lot, even."
    e "Heh. Good to hear."
    scene 47-2 office 5 with Dissolve(0.5)
    e "Should I wear something specific?"
    a "No. We'll have outfits there."
    e "Gotcha."
    a "See you later, dear."
    scene 47-2 office 6 with Dissolve(0.5)
    if bar_var_1 == False:
        a "{i}...I hope she will put up with everything Patrick has probably planned for us...{/i}"
        a "{i}...It's not a good idea to make him mad...{/i}"
    else:
        a "{i}...I hope she will be willing to do the things I've planned...{/i}"
        a "{i}...I could use the money...{/i}"
    scene black with Dissolve(0.5)
    pause 0.5
    scene 47-2 office 7 with Dissolve(0.5)
    a "Ok... An email."
    a "From Shingzhou."
    a "Interesting. I thought our dealings were done."
    a "Perhaps they need more of my services."
    scene 47-2 office 8 with Dissolve(0.5)
    a "Indeed."
    a "They want to have an online meeting and discuss things."
    a "Like more cooperation and they need my assistance."
    stop music fadeout 3
    a "Hehe... I'm really getting up in the world."
    a "Alright. I'll call them."
    play music PPMCasualReception
    play sound mouse_click_1
    scene black with Dissolve(0.5)
    pause 0.5
    scene 47-2 office 9 with Dissolve(0.5)
    c2 "Anna! So good to see you!"
    a "Hello, Mr. Chen!"
    a "How are you?"
    c2 "We are great, business is great."
    c2 "So much so that we are planning to incorporate several companies."
    scene 47-2 office 10 with Dissolve(0.5)
    a "I'm glad to hear it. You've also been one of our biggest clients."
    a "Thank you for your business!"
    c2 "Of course. The services provided are impeccable."
    scene 47-2 office 11 with Dissolve(0.5)
    a "Only the best for our clients."
    a "So. What brings you to me today?"
    scene 47-2 office 9 with Dissolve(0.5)
    c2 "Well. As I mentioned, we are expanding and we need an expert to help expedite the process."
    a "I see."
    c2 "We have potential businesses here in China that we want to have closer ties with."
    c2 "I understand it would be a long trip, but we really could use someone like you."
    scene 47-2 office 12 with Dissolve(0.5)
    c2 "Perhaps you could remind us of what we did last time we met?"
    c2 "It was wonderful. Maybe a little showcase would do it. Heh."
    menu:
        "Heh, ok. I can do that.":
            scene 47-2 office 13 with Dissolve(0.5)
            a "If you'd like I can... show you something, heh."
            c2 "We'd love that!"
            c2 "That would make things even better!"
            scene 47-2 office 14 with Dissolve(0.5)
            a "{i}...I should try to be discreet so that people wouldn't see me like this...{/i}"
            scene 47-2 office 15 with Dissolve(0.5)
            a "Heh. Alright."
            a "Are you ready?"
            scene 47-2 office 16 with Dissolve(0.5)
            c2 "Dying of anticipation."
            c2 "You are the epitome of beauty."
            if jeremySexContent == False:
                scene 47-2 office 17 with Dissolve(0.5)
                a "Heh."
                a "Like what you see?"
                c2 "Oh yes!"
                c2 "So good!"
                scene 47-2 office 18 with Dissolve(0.5)
                c2 "It truly brings back good memories, hah."
                c2 "It's perfect."
                a "Thank you, Mr. Chen."
            else:
                scene 47-2 office 17-2 with Dissolve(0.5)
                a "Heh."
                a "Like what you see?"
                c2 "Oh indeed!"
                c2 "You've got something inside there?"
                scene 47-2 office 18-2 with Dissolve(0.5)
                c2 "I have to ask."
                c2 "Why is it in there?"
                c2 "Are you a naughty, naughty girl by nature?"
                a "Maybe... But Jeremy asked me to put it in."
                a "It's a communication device."
                a "He calls me with it."
                c2 "Ingenious!"
            scene 47-2 office 19 with Dissolve(0.5)
            c2 "Could you open up your legs more?"
            c2 "A wonderful sight."
            c2 "Could look all day."
            z1 "Indeed."
            if jeremySexContent == False:
                scene 47-2 office 20 with Dissolve(0.5)
                c2 "WOOW!"
                c2 "So good!"
                c2 "Can't wait to see you again!"
            else:
                scene 47-2 office 20-2 with Dissolve(0.5)
                c2 "Wow. That pussy plug looks magnificent."
                c2 "Is it real gold?"
                a "I'm unsure..."
                c2 "Can't wait to see you again!"
            scene 47-2 office 21 with Dissolve(0.5)
            a "Alright. That should be enough for now."
            c2 "Fair enough."
            scene 47-2 office 22 with Dissolve(0.5)
            c2 "I'm glad we contacted you."
            c2 "Can't wait to meet you in person again."
            c2 "So you in?"
            a "Yes. Let's do it."
        "What? NO! Strictly professional here.":
            scene 47-2 office 9 with Dissolve(0.5)
            c2 "Really? What has changed?"
            a "Nothing. I just don't feel comfortable doing that."
            c2 "Interesting..."
            scene 47-2 office 22 with Dissolve(0.5)
            c2 "Fair enough..."
            c2 "But are you still willing to help us in our endeavors?"
            a "Yeah."
    scene 47-2 office 23 with Dissolve(0.5)
    a "So. What's the plan then?"
    c2 "Well, the business is back in China."
    c2 "We're here already and the first meeting is scheduled next week."
    scene 47-2 office 24 with Dissolve(0.5)
    c2 "Would you be willing to take your private jet and fly to us?"
    a "Whoa. That's a long way."
    a "But, yeah. I'd still expect our regular commissions."
    a "But this time also, since I'm not directly working through my company but also helping your business, there will be additional commission."
    c2 "Of course, whatever you need, Anna."
    c2 "We can discuss this through email and also when we meet."
    c2 "We will send you the documentation we're putting together."
    a "Ok. Sounds good."
    a "I will start prepping the paperwork."
    c2 "See you soon, Anna."
    a "Bye!"
    scene 47-2 office 25 with Dissolve(0.5)
    a "Alright. Will delegate some of this to Madison."
    a "Got other things to take care of."
    a "Like going to Rebecca."
    scene black with Dissolve(0.5)
    pause 1
    jump EP17_Rebecca
label EP17_Agent:
    $ EP17_var_8 = True
    play ambient city_traffic
    play music SecretAgent
    scene 47-10 agent 1 with Dissolve(0.5)
    fbi1 "Anna."
    fbi1 "Surprised to run into you."
    scene 47-10 agent 2 with Dissolve(0.5)
    fbi1 "On your way to somewhere?"
    a "I bet it's not surprising at all to meet me here."
    a "You probably know where I'm headed."
    fbi1 "True."
    fbi1 "Get in, I can take you there."
    scene 47-10 agent 3 with Dissolve(0.5)
    a "Should I be worried?"
    fbi1 "Absolutely not. I'd just like to talk."
    a "What about?"
    fbi1 "Just get in."
    play sound car_door_close
    scene 47-10 agent 4 with Dissolve(0.5)
    a "Soo... What do you want?"
    fbi1 "Grayden and his boss."
    a "Straightforward, at least."
    fbi1 "No point in beating around the bush."
    fbi1 "Your meeting with him was, eye-opening."
    fbi1 "We also got some good info from his computer."
    fbi1 "But our plan has changed a bit."
    fbi1 "Turns out that Sergey's even less important than we thought. There is barely any info that we could use in regards to the heads of the operation."
    scene 47-10 agent 5 with Dissolve(0.5)
    fbi1 "So... We figured that we'd focus on the new developments, like the money owed by Carl to the organization."
    fbi1 "That you are supposed to get for them. And what people you've been trying to convince to get it for you."
    a "Shit..."
    fbi1 "Don't worry, it's all part of the plan, besides..."
    fbi1 "We are not after some weed smokers."
    scene 47-10 agent 6 with Dissolve(0.5)
    fbi1 "We are after the big dogs."
    fbi1 "For now, I want you to continue with your plan of getting the funds."
    fbi1 "We will track you accordingly. See what happens."
    a "Why can't you just give me the funds, I'd try setting up a meeting."
    fbi1 "Too suspicious. It has to run a natural course."
    fbi1 "All you need to worry about is keeping up the ruse."
    scene 47-10 agent 7 with Dissolve(0.5)
    if EarlHelp == False:
        fbi1 "By the looks of it, you've become Sergey's right hand."
        fbi1 "That's our in."
        fbi1 "All you have to do is play your part."
    else:
        fbi1 "By the looks of it, you've been 'appointed' as the leader of the operation."
        fbi1 "That's our in."
        fbi1 "All you have to do is play your part."
    scene 47-10 agent 8 with Dissolve(0.5)
    a "Why are you so sure that I will get anywhere close to them."
    fbi1 "Looking at you. I'm very convinced that you will."
    fbi1 "I'm certain you can persuade them to come out."
    fbi1 "Then we'll lay on the pressure."
    scene 47-10 agent 7 with Dissolve(0.5)
    a "What about my safety?"
    a "What guarantees do I get?"
    fbi1 "That's covered."
    fbi1 "We are putting together a witness protection program that would assure your AND your sister's safety."
    scene 47-10 agent 8 with Dissolve(0.5)
    a "How can I trust you?"
    fbi1 "Cmon, we are the FBI."
    a "Mhm... That assures me how?"
    fbi1 "There are always bad apples in the government. But so far I've been forthcoming, haven't I?"
    fbi1 "I know about all your dealings, but I'm turning a blind eye cause you'd help us put away the real bad guys."
    fbi1 "That's why you can trust me."
    fbi1 "I will contact you again when things start to take shape."
    fbi1 "Then we'll discuss all of this further."
    scene 47-10 agent 10 with Dissolve(0.5)
    fbi1 "We're here."
    a "Thanks."
    scene 47-10 agent 11 with Dissolve(0.5)
    fbi1 "Anna."
    fbi1 "Can I trust your discretion?"
    fbi1 "Remember, if you help us with this, we can guarantee your safety."
    scene 47-10 agent 12 with Dissolve(0.5)
    a "Do I have a choice?"
    fbi1 "You do. But then I cannot promise leniency or your freedom."
    fbi1 "Besides, helping put away bad guys is never a bad thing."
    a "Alright..."
    scene 47-10 agent 13 with Dissolve(0.5)
    fbi1 "Good luck at the bar."
    fbi1 "I will be in contact."
    scene 47-10 agent 14 with Dissolve(0.5)
    a "Thanks..."
    a "I'll do what I can."
    fbi1 "Yes."
    scene black with Dissolve(0.5)
    pause 1
label EP17_Bar:
    stop ambient
    $ EP17_var_9 = True
    play music barsong
    scene 47-9 barscene 1 with Dissolve(0.5)
    j3 "And that's how I ended up here."
    b10 "Cheers to that, haha."
    scene 47-9 barscene 2 with Dissolve(0.5)
    a "Emily! Hey."
    e "Anna!"
    a "Got here well?"
    e "Yeah. Look who's also here!"
    play sound surprise
    scene 47-9 barscene 3 with Dissolve(0.5)
    b10 "Hey, Anna."
    a "Brandon?"
    a "What brings you here?"
    b10 "Just going around clubs this evening, see what's what."
    scene 47-9 barscene 4 with Dissolve(0.5)
    da "Hey, Anna."
    a "David! Hah. I can always find you here."
    j3 "Whenever I'm in, he's also in."
    j3 "That means, always."
    scene 47-9 barscene 5 with Dissolve(0.5)
    da "Lovely to see you both here again."
    da "Never a dull moment with you two."
    scene 47-9 barscene 6 with Dissolve(0.5)
    a "So. You ready?"
    e "For?"
    a "Our 'shift'."
    e "Sure, a little side hustle doesn't hurt."
    if bar_var_1 == True:
        a "We should go get changed and the go to Patricks office."
    else:
        a "Come, I'll show you around."
        e "Oh, heh. VIP access."
        scene 47-9 barscene 7 with Dissolve(0.5)
        e "Soo... Since Patrick's demise, you've been in charge?"
        a "More or less."
        scene 47-9 barscene 8 with Dissolve(0.5)
        e "Really?"
        e "You're like everywhere."
        e "You high up at the office, in charge here."
        e "Some other things I probably don't know about."
        e "You're a busy bee, Anna."
        scene 47-9 barscene 9 with Dissolve(0.5)
        a "So. This is the place."
        e "Wow. Quite an office."
        e "Definitely has more of that I'm a sleazy bar owner vibe to it. Haha."
        a "Right?"
        scene 47-9 barscene 11 with Dissolve(0.5)
        e "Got big plans for the bar?"
        a "Not really. There's so much going on that I can barely keep up."
        a "Maybe will have to sit down and figure it out."
        e "Knowing you, you'd figure out something freaky. Hah."
        scene 47-9 barscene 12 with Dissolve(0.5)
        a "Hehe."
        a "I'll just focus on my job and take away a nice paycheck for now."
        a "I've got a lot to do in terms of business at the office."
        e "True."
        a "Let's go get changed."
    scene black with Dissolve(0.5)
    pause 0.5
    play sound door2
    scene 47-9 barscene 13 with Dissolve(0.5)
    e "So what kind of an outfit do you have for me?"
    e "And... What exactly are we going to do?"
    scene 47-9 barscene 14 with Dissolve(0.5)
    a "We'll cater to clients."
    a "Just do the regular and then see how things go."
    e "I remember the previous time."
    a "Oh... That heh."
    a "We'll see how it goes."
    scene 47-9 barscene 15 with Dissolve(0.5)
    a "I've got this for you."
    e "Oh."
    e "Thanks."
    scene 47-9 barscene 16 with Dissolve(0.5)
    e "Never worked in a bar before."
    a "You'll be natural at it."
    a "You're extroverted and all that."
    e "Heh, thanks."
    play sound undress
    scene 47-9 barscene 17 with Dissolve(0.5)
    e "Sure you don't need me like this?"
    e "We'll certainly earn the big bucks."
    a "Seriously?"
    e "No! Of course not."
    e "Too much, too much Anna."
    a "Haha."
    play sound jacketcloth
    scene 47-9 barscene 18 with Dissolve(0.5)
    a "Wow."
    a "Looks great on you."
    scene 47-9 barscene 19 with Dissolve(0.5)
    e "Really think so?"
    a "Yeah."
    e "I don't know... It's pretty skimpy."
    e "Revealing."
    scene 47-9 barscene 20 with Dissolve(0.5)
    e "You sure this is ok?"
    a "Yeah. You've seen how I dress here sometimes."
    a "It's definitely ok."
    e "Well... Ok."
    a "What? Shy all of a sudden?"
    scene 47-9 barscene 21 with Dissolve(0.5)
    e "I wonder what you've got prepared."
    a "You'll see. I don't know myself."
    a "I just come in here and pick whatever."
    if bar_var_1 == True:
        a "Unless Patrick specifically asks me."
    scene black with Dissolve(0.5)
    pause 0.5
    play sound undress
    scene 47-9 barscene 22 with Dissolve(0.5)
    e "Wowow."
    e "Anna, you're on fire!"
    e "I didn't expect such an outfit!"
    a "Yeah. Me neither."
    scene 47-9 barscene 23 with Dissolve(0.5)
    e "It's wow."
    e "So, what are we supposed to be?"
    a "Not sure."
    play sound surprise
    scene 47-9 barscene 24 with Dissolve(0.5)
    a "This whip makes me think I'm a dominatrix and you're my sweet innocent angel."
    e "Whip?"
    e "What the fuck! Haha."
    scene 47-9 barscene 25 with Dissolve(0.5)
    e "This is about to become a very interesting evening."
    a "Oh yeah."
    if bar_var_1 == True:
        a "We should go to Patrick before we go to the bar."
        e "Ok..."
        scene black with Dissolve(0.5)
        pause 1
        scene 47-9 barscene 26 with Dissolve(0.5)
        a "{i}...There he is... I better listen to what he wants...{/i}"
        a "Hello, sir."
        a "You wanted to see us before we go to the bar?"
        scene 47-9 barscene 28 with Dissolve(0.5)
        pa "Indeed."
        pa "And I see you've brought your friend like I asked."
        e "Hello, sir."
        pa "Good, good. She knows how to respond."
        e "What?"
        scene 47-9 barscene 29 with Dissolve(0.5)
        pa "Yeah, so. Today the theme, as you see is dominatrix and her innocent follower."
        pa "I picked the outfits myself."
        a "Thank you."
        e "Thank you."
        pa "Hehe. This will go well."
        scene 47-9 barscene 30 with Dissolve(0.5)
        pa "Oh, yes... Indeed..."
        pa "Perfect."
        scene 47-9 barscene 31 with Dissolve(0.5)
        a "What's this for?"
        pa "What do you think?"
        pa "That's for you to use out there."
        scene 47-9 barscene 32 with Dissolve(0.5)
        pa "Now go earn us some good money."
        pa "Good luck!"
        scene 47-9 barscene 33 with Dissolve(0.5)
        a "Ok, sir."
        pa "Hehe..."
        scene 47-9 barscene 34 with Dissolve(0.5)
        e "He's pretty creepy."
        a "What? No, he isn't."
        a "He just takes this work seriously."
        scene black with Dissolve(0.5)
    else:
        a "I suppose we can go to the bar, and talk to Jim."
        a "He's currently doing all the work and setup instead of me."
        e "By the looks of it, he's got some 'spicy' ideas."
        scene black with Dissolve(0.5)
    play sound door2
    pause 0.5
    scene 47-9 barscene 35 with Dissolve(0.5)
    j3 "Well, well."
    j3 "Don't you two look stunning."
    a "Hehe. We do indeed."
    a "And ready to lay punishment on those who disobey."
    j3 "Haha. Remind me to obey you at all times."
    a "Soo. What exactly do you want us to do?"
    scene 47-9 barscene 36 with Dissolve(0.5)
    if bar_var_1 == True:
        j3 "I don't know."
        j3 "Didn't Patrick tell you?"
        j3 "That's all his master plan."
        a "I guess he did."
        j3 "Just play along. Looks like you're a dominatrix."
    else:
        j3 "Well I suppose you're role is that of a dominatrix."
        a "Where did you find these?"
        j3 "Oh don't ask. That was quite a mission..."
        a "So what do you want from us?"
        j3 "Just the regular."
        a "Ok."
    scene 47-9 barscene 37 with Dissolve(0.5)
    da "Haha. I sign up to be the first to get spanked!"
    scene 47-9 barscene 38 with Dissolve(0.5)
    a "You better not joke around, David."
    a "Otherwise I just might do it."
    a "And you'll go home with a sore buttcheek."
    da "Haha."
    scene 47-9 barscene 39 with Dissolve(0.5)
    j3 "So yeah. We've got a lot of the regulars here again."
    j3 "Your biggest fans, Anna."
    scene 47-9 barscene 41 with Dissolve(0.5)
    a "I'll go talk to the couple and the guy at the bar."
    a "You go and serve the guys on the right."
    e "Sure."
    scene 47-9 barscene 40 with Dissolve(0.5)
    a "Thanks for helping me out once more."
    e "I mean no problem, but I didn't exactly come here to be a waitress. I came here to have fun."
    a "Oh, we'll have fun, that's certain."
    a "Not for long in that outfit, hehe."
    scene 47-9 barscene 42 with Dissolve(0.5)
    j3 "Yeah, knowing the crowd."
    j3 "Things could heat up quite a bit."
    scene 47-9 barscene 43 with Dissolve(0.5)
    e "Hello, sir."
    bc_1 "Well, well."
    bc_1 "A new waitress?"
    e "Maybe. Heh."
    scene 47-9 barscene 44 with Dissolve(0.5)
    e "What would you like?"
    bc_1 "You bent over and spanked Hehe..."
    e "That... Will come later perhaps."
    scene 47-9 barscene 45 with Dissolve(0.5)
    bc_1 "Nice! In that case, I want a regular beer."
    e "Coming right up."
    scene 47-9 barscene 46 with Dissolve(0.5)
    bc_1 "Dayum. That's a sweet ass."
    bc_1 "Hehe, this will be a fun evening."
    scene 47-9 barscene 47 with Dissolve(0.5)
    e "Hello. What would you like to order?"
    scene 47-9 barscene 48 with Dissolve(0.5)
    bc_2 "Just a beer for me."
    bc_2 "I'm more here for the show, hehe."
    e "Indeed."
    scene 47-9 barscene 49 with Dissolve(0.5)
    e "Alright. I'll be back with a beer soon enough."
    scene 47-9 barscene 50 with Dissolve(0.5)
    a "Well, hello there."
    a "It's always nice to see returning customers."
    pa1 "There's always something fun going on here."
    a "Indeed there is."
    scene 47-9 barscene 51 with Dissolve(0.5)
    a "I hope you're both enjoying yourselves."
    a "It's going to get only better."
    pa2 "Glad to hear it."
    scene 47-9 barscene 52 with Dissolve(0.5)
    a "Oh you can bet on that. I have this interesting tool today."
    pa1 "What?"
    pa2 "Damn, Haha."
    a "Fun activities await."
    if EP12_Bar_Couple_Refuse == False:
        a "Besides, if you remember our previous fun experience..."
        a "Things will only get more and more fun."
        pa1 "How could I forget?"
        pa2 "Agreed, that was very fun..."
    scene 47-9 barscene 53 with Dissolve(0.5)
    a "So what would you like to order?"
    pa2 "We'll have two of your today's specials."
    a "Very well."
    a "Be right back."
    scene 47-9 barscene 54 with Dissolve(0.5)
    a "Hello again."
    a "I always see you around here."
    bc_3 "I only come when you're around."
    bc_3 "You're an absolute queen!"
    bc_3 "I could watch you all day, Anna."
    scene 47-9 barscene 55 with Dissolve(0.5)
    a "Devoted indeed."
    a "Plays straight into today's theme."
    a "What would you like to order?"
    bc_3 "You guys got them new IPAs?"
    a "We sure do."
    bc_3 "Get me one of those, whichever."
    bc_3 "I know you will pick the right one."
    scene 47-9 barscene 56 with Dissolve(0.5)
    a "Alright. Will be back in a sec."
    scene 47-9 barscene 57 with Dissolve(0.5)
    e "Ok, so... Two beers."
    e "That's it."
    a "From my side two specials and and IPA."
    a "He doesn't care what kind."
    e "Well, I didn't expect them to also ask about extra 'services'."
    scene 47-9 barscene 58 with Dissolve(0.5)
    e "Didn't know that's how it went down. Heh."
    a "Well. Yeah..."
    a "That's where the big bucks come from now."
    e "I mean, not against it, just surprised. Hah."
    scene 47-9 barscene 59 with Dissolve(0.5)
    a "Hehe."
    a "But it's fun, isn't it?"
    e "Hehe. It's ramping up indeed."
    scene 47-9 barscene 60 with Dissolve(0.5)
    j3 "Alright, I'll make the drinks and you girls, do it like last time."
    e "I wasn't here last time."
    a "Last time I offered the extra services when giving out the drinks."
    e "Ooohhh."
    scene 47-9 barscene 61 with Dissolve(0.5)
    j3 "Just, keep it lowkey before the main 'event'."
    if bar_var_1 == False:
        j3 "I've got some ideas."
    else:
        j3 "Patrick told me some ideas."
    a "Ok, we'll try to refrain from doing too much."
    scene 47-9 barscene 62 with Dissolve(0.5)
    j3 "Haha."
    j3 "Just keep some juice for a bit later. Ok?"
    a "Heh. You can never know with us."
    j3 "True."
    scene 47-9 barscene 63 with Dissolve(0.5)
    a "Come on."
    scene 47-9 barscene 64 with Dissolve(0.5)
    a "One beer."
    bc_1 "Heh. Nice."
    scene 47-9 barscene 65 with Dissolve(0.5)
    bc_1 "You two are some fine sluts."
    e "Ok."
    bc_1 "Anyway, do you offer any services this time?"
    if bar_var_1 == True:
        bc_1 "Previously Anna gave me a blowy."
    scene 47-9 barscene 66 with Dissolve(0.5)
    e "Umm."
    scene 47-9 barscene 67 with Dissolve(0.5)
    a "Yeah. We do. But smaller ones."
    a "We'll have a bigger main 'event' a bit later."
    a "If you can keep it in your pants a bit longer hehe."
    scene 47-9 barscene 68 with Dissolve(0.5)
    e "Yeah. Soo. What would you like in that case?"
    bc_1 "Hmm..."
    scene 47-9 barscene 69 with Dissolve(0.5)
    bc_1 "Show me those nice titties."
    bc_1 "I bet they'd look better naked."
    e "Heh. Alright."
    play sound undress
    scene 47-9 barscene 70 with Dissolve(0.5)
    e "You like that?"
    bc_1 "Oh yeah!"
    bc_1 "I like this new arrival. Hehe..."
    bc_1 "You will fit in her perfectly."
    scene 47-9 barscene 71 with Dissolve(0.5)
    e "Here's the drink."
    scene 47-9 barscene 72 with Dissolve(0.5)
    bc_1 "Thanks."
    scene 47-9 barscene 73 with Dissolve(0.5)
    bc_1 "Can't wait to see what you guys got planned."
    a "It will be fun, trust me."
    scene 47-9 barscene 74 with Dissolve(0.5)
    e "Hello."
    e "You also ordered a regular beer, right?"
    bc_2 "Yeah."
    scene 47-9 barscene 75 with Dissolve(0.5)
    bc_2 "Nice, beautiful breasts, by the way."
    bc_2 "This bar definitely knows how to pick hot girls to work here."
    e "Thank you."
    bc_2 "I was wondering."
    bc_2 "Looks like you're giving some 'services' for the clients today."
    if bar_var_1 == True:
        bc_2 "Just like last time when Anna rode my face... Magnificent that was."
    a "Yeah, but smaller requests. To keep us in top shape for later."
    bc_2 "Very intriguing."
    bc_2 "Alright. I want you to unveil Anna's front for me."
    scene 47-9 barscene 76 with Dissolve(0.5)
    e "As you wish, sir."
    a "Go right ahead."
    a "I'm all yours, baby."
    scene 47-9 barscene 77 with Dissolve(0.5)
    pause 0.5
    play sound undress
    scene 47-9 barscene 78 with Dissolve(0.5)
    e "I never get tired of those sexy boobs."
    scene 47-9 barscene 79 with Dissolve(0.5)
    bc_2 "Oh..."
    bc_2 "Neither do I."
    scene 47-9 barscene 80 with Dissolve(0.5)
    e "Here's your drink, sir."
    scene 47-9 barscene 81 with Dissolve(0.5)
    bc_2 "Thank you."
    bc_2 "You're both so sexy."
    scene 47-9 barscene 82 with Dissolve(0.5)
    pa1 "I'm glad that the other girl is back."
    pa1 "She is very hot as well."
    pa2 "Well, she's all yours, hehe."
    pa1 "Don't think I'll leave you all by yourself."
    scene 47-9 barscene 83 with Dissolve(0.5)
    pa2 "Let's just see where the night goes, eh?"
    pa1 "I have a feeling that we're in for a good time."
    pa2 "Hehe."
    scene 47-9 barscene 84 with Dissolve(0.5)
    a "Soo. My favourite couple."
    a "Two specials for special people."
    pa1 "Hehe. Thank you."
    pa1 "We're glad that Emily is here again."
    scene 47-9 barscene 85 with Dissolve(0.5)
    a "Oh yeah. Heh."
    e "We go wayyy back."
    e "Since school."
    scene 47-9 barscene 86 with Dissolve(0.5)
    a "Indeed. And she's rather freaky. Just like me."
    a "Heh."
    a "This time she's helping out."
    a "In more ways than one, hehe."
    scene 47-9 barscene 87 with Dissolve(0.5)
    pa1 "Perfect."
    pa1 "We don't have any requests for now."
    scene 47-9 barscene 88 with Dissolve(0.5)
    a "You sure?"
    a "You've always been eyeing me."
    pa1 "We heard that there will be the main event a bit later."
    pa1 "We'll definitely want to join in then, hehe."
    scene 47-9 barscene 89 with Dissolve(0.5)
    pa2 "Oh, yeah. we're very curious."
    a "Hehe."
    a "You won't regret it. When you're done with the drinks, I hope you join in."
    scene 47-9 barscene 90 with Dissolve(0.5)
    a "That's all."
    scene 47-9 barscene 91 with Dissolve(0.5)
    a "Oh wait. I need to bring an IPA to the last guy."
    scene 47-9 barscene 92 with Dissolve(0.5)
    a "When I come back, I suppose it will be time for the event. Heh."
    e "I wonder what it is."
    a "Yeah, me too."
    scene 47-9 barscene 93 with Dissolve(0.5)
    b10 "Well, well."
    b10 "Lost that upper part really quickly."
    a "Not as quick as Emily, though."
    a "Heh."
    a "Besides, not like you haven't seen these before."
    scene 47-9 barscene 94 with Dissolve(0.5)
    b10 "Hah. True."
    b10 "No judgment there."
    b10 "I'll tell you this though..."
    b10 "Justin will regret not coming when he hears what is going on today. Hehe."
    a "Haha. Make sure to let him know."
    b10 "Oh I will."
    scene 47-9 barscene 95 with Dissolve(0.5)
    a "Sorry for the wait."
    a "Rather busy here today."
    bc_3 "It's alright, Anna."
    bc_3 "I'd wait for you as long as necessary."
    bc_3 "You're boobs are so beautiful."
    if bar_var_1 == True:
        bc_3 "By the way."
        scene 47-9 barscene 96 with Dissolve(0.5)
        bc_3 "I do have a small request as well."
        bc_3 "Could you take the first sip?"
        bc_3 "It's on me. I want you to drink from it... Mmm..."
        scene 47-9 barscene 97 with Dissolve(0.5)
        a "Oh. Ok. I can do that. And a little bit more. Heh."
        bc_3 "Please. You are the best thing that happened to this bar."
        play sound drinkingBeverage
        scene 47-9 barscene 96-1 with Dissolve(0.5)
        a "Mmm..."
        play sound licking_2
        scene 47-9 barscene 96-2 with Dissolve(0.5)
        bc_3 "Oh... Yeah... So hot..."
        bc_3 "Reminds me of when you sucked my cock."
    scene 47-9 barscene 98 with Dissolve(0.5)
    j3 "Alright. You did well."
    j3 "But now it's time to ramp it up a little bit."
    a "Ok. So what's the master plan?"
    scene 47-9 barscene 99 with Dissolve(0.5)
    j3 "Get up on the bar and let's invite the guests to request something."
    e "Well, well..."
    e "I wonder what they will come up with."
    play music bar_song_1
    scene 47-9 barscene 100 with Dissolve(0.5)
    j3 "Come, I'll help you up."
    scene 47-9 barscene 101 with Dissolve(0.5)
    pause 0.5
    scene 47-9 barscene 102 with Dissolve(0.5)
    a "Hehe."
    a "Such a gentleman."
    scene 47-9 barscene 103 with Dissolve(0.5)
    a "Not touching me inappropriately."
    j3 "Heh."
    j3 "gotta be respectful."
    a "I'm a dominatrix, you better be. Hehe."
    scene 47-9 barscene 104 with Dissolve(0.5)
    a "Alright."
    a "Emily?"
    scene 47-9 barscene 105 with Dissolve(0.5)
    a "Come up here."
    e "Riight... Like I'm the best for the innocent girl choice, heh."
    scene 47-9 barscene 106 with Dissolve(0.5)
    e "I'm a bit embarrassed though, hehe."
    a "That's what makes you perfect for the role."
    a "Just act on it."
    e "Of course. We're talking away a good pay day AND having loads of fun."
    scene 47-9 barscene 107 with Dissolve(0.5)
    bc_1 "Hmm. Looks like they are doing something interesting there."
    scene 47-9 barscene 108 with Dissolve(0.5)
    a "Alright, gather around!"
    a "We're going to do something fun now."
    a "And we want your help."
    scene 47-9 barscene 109 with Dissolve(0.5)
    a "Come closer."
    pa1 "That seems like the main 'course' Heh."
    pa2 "Let's see what's going on."
    scene 47-9 barscene 110 with Dissolve(0.5)
    a "So. We will take a request from someone."
    a "On what we should do. That will be added to your bill, though. So choose wisely... Heh."
    a "Whatever you'd like."
    scene 47-9 barscene 111 with Dissolve(0.5)
    bc_1 "YEAH! YEAH!"
    bc_1 "I got an idea!"
    scene 47-9 barscene 112 with Dissolve(0.5)
    bc_1 "I saw a small whip you had."
    bc_1 "I want you to spank her with it!"
    bc_2 "Yeah! That's so hot!"
    da "Hehe. I agree!"
    scene 47-9 barscene 113 with Dissolve(0.5)
    e "But... But... I didn't do anything wrong, master."
    a "Yes you did!"
    a "You deserve punishment, little slave!"
    scene 47-9 barscene 114 with Dissolve(0.5)
    a "Turn around and show me that ass."
    a "Don't keep me waiting!"
    scene 47-9 barscene 115 with Dissolve(0.5)
    a "You've been a bad girl, you know that, right?"
    e "I... I have been a bad girl..."
    a "And what does that mean?"
    e "You have to punish me."
    a "Indeed."
    scene 47-9 barscene 116 with Dissolve(0.5)
    a "Got anything to say for yourself?"
    e "I'm sorry for disobeying."
    e "Sorry for being a bad slave."
    a "That's right!"
    scene 47-9 barscene 117 with Dissolve(0.5)
    pause 1
    play sound spank1
    scene 47-9 barscene 118 with vpunch
    e "Oh."
    scene 47-9 barscene 119 with Dissolve(0.5)
    a "Take that!"
    e "Sorry!"
    scene 47-9 barscene 120 with Dissolve(0.5)
    bc_1 "NONONO!"
    bc_1 "That was too weak!"
    bc_1 "Stronger!"
    bc_1 "She deserves to be punished harder!"
    scene 47-9 barscene 121 with Dissolve(0.5)
    a "Well, well."
    a "If the crowd wishes so. Hehe."
    scene 47-9 barscene 122 with Dissolve(0.5)
    e "Do it."
    e "I can take it. Hehe."
    a "Exactly!"
    scene 47-9 barscene 123 with Dissolve(0.5)
    pause 1
    play sound spank2
    scene 47-9 barscene 124 with vpunch
    e "AHHH!"
    scene 47-9 barscene 125 with Dissolve(0.5)
    e "Ouch! That really hurt!"
    a "Hehe. That's your punishment for being a bad slave!"
    a "You will learn from this experience?"
    e "Yes, madam!"
    scene 47-9 barscene 126 with Dissolve(0.5)
    a "Good. Hehe."
    scene 47-9 barscene 127 with Dissolve(0.5)
    a "That mark on your ass will be a reminder not to do it again!"
    e "I understand."
    scene 47-9 barscene 129 with Dissolve(0.5)
    e "I will not disobey again."
    a "You better. Otherwise, we will make your punishment harder!"
    bc_1 "Yeah!"
    bc_2 "WOHOO!!"
    scene 47-9 barscene 131 with Dissolve(0.5)
    pa2 "I wonder if you'd like that to be done on you, too."
    pa2 "Getting spanked like that. Oh. Hehe."
    scene 47-9 barscene 132 with Dissolve(0.5)
    pa1 "You mean, get punished by you, spanked like she was?"
    scene 47-9 barscene 131 with Dissolve(0.5)
    pa2 "Well what if it was someone else?"
    pa1 "Heh. Maybe..."
    pa2 "Heh."
    if bar_var_1 == True:
        label EP17_Bar_Sex_Scene:
        $ renpy.music.play("audio/sounds/bar_song_1.mp3", channel = 'music', if_changed = True)
        $ persistent.scene_51 = True
        scene 47-9 barscene 133 with Dissolve(0.5)
        j3 "ALRIGHT!"
        j3 "Who's up for a little drinking game?"
        j3 "I'm letting someone, who wants to buy, a special whiskey."
        j3 "And more importantly a special way of drinking it."
        scene 47-9 barscene 134 with Dissolve(0.5)
        j3 "Using Anna's body!"
        j3 "Hahaaa!"
        scene 47-9 barscene 135 with Dissolve(0.5)
        a "What? Hehe."
        a "Interesting."
        scene 47-9 barscene 136 with Dissolve(0.5)
        bc_2 "ME! ME! ME!"
        bc_2 "I'll pay whatever!"
        bc_2 "I wanna do it!"
        scene 47-9 barscene 137 with Dissolve(0.5)
        j3 "Alright then!"
        bc_2 "YES!"
        bc_2 "HAHA!"
        scene 47-9 barscene 138 with Dissolve(0.5)
        bc_2 "Oh I cannot wait to do it."
        bc_2 "You're the hottest woman ever!"
        a "Thank you, hehe."
        scene 47-9 barscene 139 with Dissolve(0.5)
        j3 "Alright, Anna."
        j3 "Spread your legs and remove some clothing."
        j3 "Let's give this lucky bastard what he wants!"
        a "Oh. Ok. Haha."
        scene 47-9 barscene 140 with Dissolve(0.5)
        pause 1
        play sound jacketcloth
        scene 47-9 barscene 141 with Dissolve(0.5)
        bc_2 "Oh... My... I can taste it already... Wow..."
        a "You'd do anything for it?"
        bc_2 "Anything..."
        a "Throw in an extra few hundred."
        bc_2 "WORTH. EVERY. PENNY!"
        scene 47-9 barscene 142 with Dissolve(0.5)
        a "Emily, you can do the honors."
        e "Ok."
        scene 47-9 barscene 143 with Dissolve(0.5)
        e "Should I just pour it down your stomach?"
        a "Yeah."
        a "Let him have as much as he wants. Heh."
        scene 47-9 barscene 144 with Dissolve(0.5)
        a "Get down in front of me."
        a "I'm the dominatrix here."
        bc_2 "OH... YEAH!"
        scene 47-9 barscene 145 with Dissolve(0.5)
        a "I like how you look from up here."
        bc_2 "I love how you look from down here!"
        a "Perfect."
        a "Come closer."
        scene 47-9 barscene 146 with Dissolve(0.5)
        pause 1
        play sound pourwater
        scene 47-9 barscene 147 with Dissolve(0.5)
        bc_2 "Aahhhh."
        j3 "YEAH!"
        e "MORE!"
        scene 47-9 barscene 148 with Dissolve(0.5)
        a "AH."
        bc_1 "YEAAHH!"
        bc_2 "HAHAHAAAAAA!"
        a "Is that all you can take, huh?"
        a "Don't stop!"
        scene 47-9 barscene 149 with Dissolve(0.5)
        a "Ahhh..."
        bc_2 "Mmmmm..."
        a "Oh..."
        show EP17_Bar_Anim_17 with Dissolve(0.5)
        pause
        a "OoOHHH."
        bc_2 "MHM!!!"
        show EP17_Bar_Anim_18 with Dissolve(0.5)
        hide EP17_Bar_Anim_17
        pause
        a "Pleasure me!"
        a "Pleasure you dominatrix!"
        bc_2 "MHM!"
        scene 47-9 barscene 150 with Dissolve(0.5)
        hide EP17_Bar_Anim_18
        j3 "Alright!"
        j3 "That's a fun activity, isn't it?"
        j3 "Who's next?"
        scene 47-9 barscene 151 with Dissolve(0.5)
        bc_2 "I want more!"
        bc_2 "I will pay A LOT more!"
        scene 47-9 barscene 152 with Dissolve(0.5)
        a "Well. Ok, What you've got in mind?"
        bc_2 "I've seen the things you do here."
        bc_2 "I wanna give that pussy some good fucking."
        a "Oh?"
        scene 47-9 barscene 153 with Dissolve(0.5)
        bc_2 "I will pay double. I'll PAY TRIPLE!"
        bc_2 "Just... I wanna do it..."
        scene 47-9 barscene 154 with Dissolve(0.5)
        a "Heh. Alright, alright."
        a "You've got a deal."
        play sound undress
        scene 47-9 barscene 155 with Dissolve(0.5)
        a "I'm all yours."
        bc_2 "Oh yeah."
        bc_2 "Come down lower."
        scene 47-9 barscene 155-1 with Dissolve(0.5)
        a "Perhaps meanwhile you could turn to that side of the audience?"
        e "Good idea. Heh."
        scene 47-9 barscene 156 with Dissolve(0.5)
        a "Like this?"
        bc_2 "Perfect!"
        bc_2 "So hot. Those tits... Everything..."
        bc_2 "Fuck."
        scene 47-9 barscene 157 with Dissolve(0.5)
        e "Well. How about you guys?"
        e "Wanna join in on the fun?"
        b10 "Ladies first. Heh."
        scene 47-9 barscene 158 with Dissolve(0.5)
        e "He is not wrong."
        e "I can see that you wanna do something fun, eh?"
        scene 47-9 barscene 159 with Dissolve(0.5)
        pa1 "Well. Yeah... Heh. But."
        pa1 "Maybe not the drink."
        e "No problem. Perhaps something else?"
        scene 47-9 barscene 160 with Dissolve(0.5)
        e "I can give you whatever you want baby."
        pa1 "Oh yeah?"
        scene 47-9 barscene 161 with Dissolve(0.5)
        pa1 "How about you let me taste those lips?"
        e "They are all yours."
        play sound kisspeck
        scene 47-9 barscene 162 with Dissolve(0.5)
        e "Mmm."
        pa1 "Mhmm..."
        scene 47-9 barscene 163 with Dissolve(0.5)
        pause 1
        scene 47-9 barscene 164 with Dissolve(0.5)
        pa1 "And now... The other ones."
        e "Oh?"
        e "Alright."
        scene 47-9 barscene 165 with Dissolve(0.5)
        pa1 "Just lay down. Hehe."
        scene 47-9 barscene 166 with Dissolve(0.5)
        pa1 "You've got such a sexy body."
        e "You too, babe."
        e "We're both fine pieces of ass."
        scene 47-9 barscene 167 with Dissolve(0.5)
        pause 0.5
        play sound undress
        scene 47-9 barscene 168 with Dissolve(0.5)
        e "Well? What are you waiting for?"
        e "This innocent girl wants to have some fun."
        pa1 "Perfect."
        scene 47-9 barscene 169 with Dissolve(0.5)
        pa1 "I bet you will love this."
        play sound jerk2
        scene 47-9 barscene 170 with Dissolve(0.5)
        e "Oh... AAHHHH..."
        scene 47-9 barscene 171 with Dissolve(0.5)
        a "Nice..."
        scene 47-9 barscene 172 with Dissolve(0.5)
        a "Don't keep me waiting, ok?"
        bc_2 "No way. Haha."
        scene 47-9 barscene 173 with Dissolve(0.5)
        a "Ohh..."
        a "Keep going..."
        scene 47-9 barscene 174 with Dissolve(0.5)
        a "Yeesss..."
        a "Deeper..."
        scene 47-9 barscene 175 with Dissolve(0.5)
        bc_2 "So good..."
        bc_2 "That. Pussy IS SO GOOD!"
        bc_2 "FUCK!"
        $ different_choice_menu = True
        $ EP17_Anim_Option = 1
        $ EP17_Anim_Speed = 1
        scene black
        play sound jerk loop
        show EP17_Bar_Anim_1 with Dissolve(0.5)
        bc_2 "OHHHH YEAAEAHHH!"
        play sound femmoan_3
        a "Ahh... Keep fucking me, you slave!"
        bc_2 "YES!"
        menu EP17_Bar_Menu_1:
            "View 1":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_1
                hide EP17_Bar_Anim_2
                hide EP17_Bar_Anim_3
                hide EP17_Bar_Anim_4
                if EP17_Anim_Speed == 1:
                    show EP17_Bar_Anim_1 with Dissolve(0.5)
                if EP17_Anim_Speed == 2:
                    show EP17_Bar_Anim_2 with Dissolve(0.5)
                $ EP17_Anim_Option = 1
                jump EP17_Bar_Menu_1
            "View 2":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_1
                hide EP17_Bar_Anim_2
                hide EP17_Bar_Anim_3
                hide EP17_Bar_Anim_4
                if EP17_Anim_Speed == 1:
                    show EP17_Bar_Anim_3 with Dissolve(0.5)
                if EP17_Anim_Speed == 2:
                    show EP17_Bar_Anim_4 with Dissolve(0.5)
                $ EP17_Anim_Option = 2
                jump EP17_Bar_Menu_1
            "Slower":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_1
                hide EP17_Bar_Anim_2
                hide EP17_Bar_Anim_3
                hide EP17_Bar_Anim_4
                if EP17_Anim_Option == 1:
                    show EP17_Bar_Anim_1 with Dissolve(0.5)
                if EP17_Anim_Option == 2:
                    show EP17_Bar_Anim_3 with Dissolve(0.5)
                $ EP17_Anim_Speed = 1
                jump EP17_Bar_Menu_1
            "Faster":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_1
                hide EP17_Bar_Anim_2
                hide EP17_Bar_Anim_3
                hide EP17_Bar_Anim_4
                if EP17_Anim_Option == 1:
                    show EP17_Bar_Anim_2 with Dissolve(0.5)
                if EP17_Anim_Option == 2:
                    show EP17_Bar_Anim_4 with Dissolve(0.5)
                $ EP17_Anim_Speed = 2
                jump EP17_Bar_Menu_1
            "Continue":
                hide EP17_Bar_Anim_1
                hide EP17_Bar_Anim_2
                hide EP17_Bar_Anim_3
                hide EP17_Bar_Anim_4
                $ different_choice_menu = False
                stop sound
                pass
        scene 47-9 barscene 176 with Dissolve(0.5)
        b10 "Damn, she got a nice ass."
        play sound femmoan_2
        b10 "She probably won't mind if I touch her, hehe."
        scene 47-9 barscene 177 with Dissolve(0.5)
        pa2 "That's my wife, dude."
        b10 "Shit. Sorry man. She beautiful, though."
        scene 47-9 barscene 178 with Dissolve(0.5)
        pa1 "Ah... Let him do it, honey, cmon."
        pa2 "Eh. Alright."
        pa1 "You know you like it."
        play sound femmoan_1
        scene 47-9 barscene 179 with Dissolve(0.5)
        pause 1
        play sound undress
        scene 47-9 barscene 180 with Dissolve(0.5)
        b10 "Niice..."
        b10 "No panties. Heh."
        pa1 "My husband insisted."
        pa2 "Well. Of course."
        play sound female_moan_2
        scene 47-9 barscene 181 with Dissolve(0.5)
        b10 "So hot."
        b10 "Crazy things going on here, eh?"
        pa2 "You could say that."
        $ different_choice_menu = True
        $ EP17_Anim_Option = 1
        $ EP17_Anim_Speed = 1
        scene black
        play sound jerk loop
        show EP17_Bar_Anim_5 with Dissolve(0.5)
        bc_2 "Fuck. Fuck. FUuuuck."
        a "Don't stop! YEAH!"
        play sound female_moan_1
        bc_2 "FUCK YEAH! MY DREAM COME TRUE!!!!"
        menu EP17_Bar_Menu_2:
            "View 1":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_5
                hide EP17_Bar_Anim_6
                hide EP17_Bar_Anim_7
                hide EP17_Bar_Anim_8
                if EP17_Anim_Speed == 1:
                    show EP17_Bar_Anim_5 with Dissolve(0.5)
                if EP17_Anim_Speed == 2:
                    show EP17_Bar_Anim_6 with Dissolve(0.5)
                $ EP17_Anim_Option = 1
                jump EP17_Bar_Menu_2
            "View 2":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_5
                hide EP17_Bar_Anim_6
                hide EP17_Bar_Anim_7
                hide EP17_Bar_Anim_8
                if EP17_Anim_Speed == 1:
                    show EP17_Bar_Anim_7 with Dissolve(0.5)
                if EP17_Anim_Speed == 2:
                    show EP17_Bar_Anim_8 with Dissolve(0.5)
                $ EP17_Anim_Option = 2
                jump EP17_Bar_Menu_2
            "Slower":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_5
                hide EP17_Bar_Anim_6
                hide EP17_Bar_Anim_7
                hide EP17_Bar_Anim_8
                if EP17_Anim_Option == 1:
                    show EP17_Bar_Anim_5 with Dissolve(0.5)
                if EP17_Anim_Option == 2:
                    show EP17_Bar_Anim_7 with Dissolve(0.5)
                $ EP17_Anim_Speed = 1
                jump EP17_Bar_Menu_2
            "Faster":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_5
                hide EP17_Bar_Anim_6
                hide EP17_Bar_Anim_7
                hide EP17_Bar_Anim_8
                if EP17_Anim_Option == 1:
                    show EP17_Bar_Anim_6 with Dissolve(0.5)
                if EP17_Anim_Option == 2:
                    show EP17_Bar_Anim_8 with Dissolve(0.5)
                $ EP17_Anim_Speed = 2
                jump EP17_Bar_Menu_2
            "Continue":
                with flash
                bc_2 "Fuck!"
                play sound female_moan_4
                bc_2 "AHHH!"
                bc_2 "YEAAHHH!!!"
                a "Cover me ahhhh."
                bc_2 "Ahh!"
                play sound female_moan_5
                with flash
                bc_2 "OHH!"
                with flash
                scene 47-9 barscene 182 with flash
                play audio female_moan_1
                play sound cum_sound
                scene 47-9 barscene 183 with flash
                hide EP17_Bar_Anim_5
                hide EP17_Bar_Anim_6
                hide EP17_Bar_Anim_7
                hide EP17_Bar_Anim_8
                $ different_choice_menu = False
                stop sound
                pass
        pause 1
        scene 47-9 barscene 184 with Dissolve(0.5)
        a "That's a proper load."
        bc_2 "Weeks worth in there."
        bc_2 "Had been waiting for this."
        scene 47-9 barscene 185 with Dissolve(0.5)
        bc_2 "You are worth every single dollar I spend on you."
        a "Hehe. Of course, I am. I'm your dominatrix, after all."
        bc_2 "Oh, yes."
        bc_1 "Daaamn. Proper slut."
        scene 47-9 barscene 186 with Dissolve(0.5)
        bc_1 "Alright, my turn to fuck this bitch."
        bc_1 "I'll show you how to fuck women like this properly."
        scene 47-9 barscene 187 with Dissolve(0.5)
        bc_1 "Whores like these are only good for one thing."
        bc_1 "Getting fucked. That's exactly what I will do."
        scene 47-9 barscene 188 with Dissolve(0.5)
        a "Sorry, what?"
        scene 47-9 barscene 189 with Dissolve(0.5)
        da "Not happening, buddy."
        bc_1 "Bro what?"
        da "You don't talk about her like that."
        bc_1 "She is a fucking slut, dude."
        da "Shut up."
        bc_1 "Or what?"
        scene 47-9 barscene 190 with Dissolve(0.5)
        da "I maybe old than you, but I can promise you this."
        da "If you don't step off, I will beat you so hard, there will be bones in your stool."
        bc_1 "Damn, alright, alright."
        scene 47-9 barscene 191 with Dissolve(0.5)
        a "Where you going, you didn't pay?!"
        bc_1 "I ain't paying for the drink. Fuck this..."
        da "Get out of here. Asshole."
        scene 47-9 barscene 192 with Dissolve(0.5)
        da "Sorry about that, Anna."
        a "David? I didn't expect that, heh."
        da "No way I'm gonna let anyone mess with my favorite waitress."
        da "And don't worry. I will cover for the drink. A small price to pay to never see him again."
        scene 47-9 barscene 193 with Dissolve(0.5)
        a "Well. I think you've earned yourself a little gift."
        da "What do you mean?"
        scene 47-9 barscene 194 with Dissolve(0.5)
        a "Perhaps you'd like to spank me?"
        da "What?"
        a "A dominatrix also has needs. Hehe."
        da "Well."
        scene 47-9 barscene 195 with Dissolve(0.5)
        a "Come on."
        a "You know you want to."
        da "When you put it that way."
        scene 47-9 barscene 196 with Dissolve(0.5)
        pause 1
        play sound spank2
        scene 47-9 barscene 197 with vpunch
        a "AAHH!"
        scene 47-9 barscene 198 with Dissolve(0.5)
        a "Hehe. See?"
        a "You definitely enjoyed that."
        scene 47-9 barscene 199 with Dissolve(0.5)
        a "How about something more?"
        a "I bet your friend in the pants also wants something."
        scene 47-9 barscene 200 with Dissolve(0.5)
        da "I don't think we should."
        a "We have to!"
        a "You know it."
        a "Besides, you paid for the drink. That comes with extra services..."
        da "Well. Alright."
        play sound undress
        scene 47-9 barscene 201 with Dissolve(0.5)
        pause 1
        scene 47-9 barscene 202 with Dissolve(0.5)
        pause 1
        scene 47-9 barscene 203 with Dissolve(0.5)
        a "That's right."
        a "Come on."
        a "Give it to me."
        a "I've actually been waiting for this for a LOOOONG time..."
        scene 47-9 barscene 204 with Dissolve(0.5)
        da "Oh... Fuck... Me too..."
        da "FUUUCKK!"
        a "DAVID... AHHH!"
        scene 47-9 barscene 205 with Dissolve(0.5)
        da "I knew it would be good... But I didn't expect to be this good..."
        da "Fuuuck..."
        a "You never know... Ahh... Until you try... FFuck..."
        $ different_choice_menu = True
        $ EP17_Anim_Option = 1
        $ EP17_Anim_Speed = 1
        scene black
        play sound jerk loop
        show EP17_Bar_Anim_9 with Dissolve(0.5)
        da "FFFAAAAAAA!"
        play sound female_moan_5
        a "Oh... This hits different!"
        da "YES!"
        menu EP17_Bar_Menu_3:
            "View 1":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_9
                hide EP17_Bar_Anim_10
                hide EP17_Bar_Anim_11
                hide EP17_Bar_Anim_12
                if EP17_Anim_Speed == 1:
                    show EP17_Bar_Anim_9 with Dissolve(0.5)
                if EP17_Anim_Speed == 2:
                    show EP17_Bar_Anim_10 with Dissolve(0.5)
                $ EP17_Anim_Option = 1
                jump EP17_Bar_Menu_3
            "View 2":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_9
                hide EP17_Bar_Anim_10
                hide EP17_Bar_Anim_11
                hide EP17_Bar_Anim_12
                if EP17_Anim_Speed == 1:
                    show EP17_Bar_Anim_11 with Dissolve(0.5)
                if EP17_Anim_Speed == 2:
                    show EP17_Bar_Anim_12 with Dissolve(0.5)
                $ EP17_Anim_Option = 2
                jump EP17_Bar_Menu_3
            "Slower":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_9
                hide EP17_Bar_Anim_10
                hide EP17_Bar_Anim_11
                hide EP17_Bar_Anim_12
                if EP17_Anim_Option == 1:
                    show EP17_Bar_Anim_9 with Dissolve(0.5)
                if EP17_Anim_Option == 2:
                    show EP17_Bar_Anim_11 with Dissolve(0.5)
                $ EP17_Anim_Speed = 1
                jump EP17_Bar_Menu_3
            "Faster":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_9
                hide EP17_Bar_Anim_10
                hide EP17_Bar_Anim_11
                hide EP17_Bar_Anim_12
                if EP17_Anim_Option == 1:
                    show EP17_Bar_Anim_10 with Dissolve(0.5)
                if EP17_Anim_Option == 2:
                    show EP17_Bar_Anim_12 with Dissolve(0.5)
                $ EP17_Anim_Speed = 2
                jump EP17_Bar_Menu_3
            "Continue":
                hide EP17_Bar_Anim_9
                hide EP17_Bar_Anim_10
                hide EP17_Bar_Anim_11
                hide EP17_Bar_Anim_12
                $ different_choice_menu = False
                stop sound
                pass
        scene 47-9 barscene 206 with Dissolve(0.5)
        da "Ahh... You are amazing... Fuuuck..."
        da "How is it THAT good..."
        a "Your cock... I knew exactly how good it would be... Ahhh..."
        a "You didn't let down, David... Aahh... David!"
        scene 47-9 barscene 207 with Dissolve(0.5)
        pause 1
        play sound spank2
        scene 47-9 barscene 208 with Dissolve(0.5)
        a "AAhh!!"
        da "Yeah... You like it, I see. Hehe..."
        scene 47-9 barscene 209 with Dissolve(0.5)
        da "I think you need to get fucked harder..."
        a "Yes, please..."
        a "Aaaaaaaaa."
        scene 47-9 barscene 210 with Dissolve(0.5)
        a "Faster, David. Faster!"
        da "If you ask, I shall oblige!"
        da "You deserve a good fucking, eh?"
        a "OHhh... Yes!"
        scene 47-9 barscene 211 with Dissolve(0.5)
        a "Soo goooooodddd!! HHAAAA!"
        da "Fuck... MH!"
        a "OH."
        $ different_choice_menu = True
        $ EP17_Anim_Option = 1
        $ EP17_Anim_Speed = 1
        scene black
        play sound jerk loop
        show EP17_Bar_Anim_13 with Dissolve(0.5)
        da "I... I can't hold it long anymore... AHH!"
        play sound female_moan_5
        a "Whenever you wanna... Ahhh... Fill me UP, David!"
        da "OHHAAAA!!"
        menu EP17_Bar_Menu_4:
            "View 1":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_13
                hide EP17_Bar_Anim_14
                hide EP17_Bar_Anim_15
                hide EP17_Bar_Anim_16
                if EP17_Anim_Speed == 1:
                    show EP17_Bar_Anim_13 with Dissolve(0.5)
                if EP17_Anim_Speed == 2:
                    show EP17_Bar_Anim_14 with Dissolve(0.5)
                $ EP17_Anim_Option = 1
                jump EP17_Bar_Menu_4
            "View 2":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_13
                hide EP17_Bar_Anim_14
                hide EP17_Bar_Anim_15
                hide EP17_Bar_Anim_16
                if EP17_Anim_Speed == 1:
                    show EP17_Bar_Anim_15 with Dissolve(0.5)
                if EP17_Anim_Speed == 2:
                    show EP17_Bar_Anim_16 with Dissolve(0.5)
                $ EP17_Anim_Option = 2
                jump EP17_Bar_Menu_4
            "Slower":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_13
                hide EP17_Bar_Anim_14
                hide EP17_Bar_Anim_15
                hide EP17_Bar_Anim_16
                if EP17_Anim_Option == 1:
                    show EP17_Bar_Anim_13 with Dissolve(0.5)
                if EP17_Anim_Option == 2:
                    show EP17_Bar_Anim_15 with Dissolve(0.5)
                $ EP17_Anim_Speed = 1
                jump EP17_Bar_Menu_4
            "Faster":
                scene black with Dissolve(0.25)
                hide EP17_Bar_Anim_13
                hide EP17_Bar_Anim_14
                hide EP17_Bar_Anim_15
                hide EP17_Bar_Anim_16
                if EP17_Anim_Option == 1:
                    show EP17_Bar_Anim_14 with Dissolve(0.5)
                if EP17_Anim_Option == 2:
                    show EP17_Bar_Anim_16 with Dissolve(0.5)
                $ EP17_Anim_Speed = 2
                jump EP17_Bar_Menu_4
            "Continue":
                play audio moaning_1
                a "DAVIIDD!!"
                with flash
                a "I'm getting CLOSE!"
                a "AAHHH!"
                with flash
                a "ME TOOO!!!"
                with flash
                play sound cum_sound
                scene 47-9 barscene 213 with flash
                pause
                scene 47-9 barscene 215 with Dissolve(0.5)
                hide EP17_Bar_Anim_13
                hide EP17_Bar_Anim_14
                hide EP17_Bar_Anim_15
                hide EP17_Bar_Anim_16
                $ different_choice_menu = False
                stop sound
                pass
        da "Whoa..."
        da "Came so hard I feel lightheaded."
        a "That's what my pussy will do to you. hehe."
        scene 47-9 barscene 216 with Dissolve(0.5)
        a "They're still going at it."
        a "Always something going on."
        scene 47-9 barscene 217 with Dissolve(0.5)
        e "Ahhh... AHHH!!!"
        e "OHHHAAA!"
        with flash
        e "YES!!"
        with flash
        with flash
        scene 47-9 barscene 218 with Dissolve(0.5)
        e "Oaaaaahhhhh!!"
        e "SO GOOD!"
        scene 47-9 barscene 219 with Dissolve(0.5)
        e "You are VERY good with your mouth."
        e "Been a while since I came like that."
        e "Amazing night, hehe."
        e "A lot of new experiences."
        scene 47-9 barscene 220 with Dissolve(0.5)
        b10 "Your wife is awesome. hehe..."
        pa2 "Thanks."
        scene 47-9 barscene 221 with Dissolve(0.5)
        pa2 "I aim to please, hehe."
        e "You did just that, haha."
        scene 47-9 barscene 222 with Dissolve(0.5)
        da "I feel weird standing around naked, gotta get dressed."
        a "Haha... I'm used to it."
        da "I know. Heh."
        play sound jacketcloth
        scene 47-9 barscene 223 with Dissolve(0.5)
        pa1 "Alright guys... Umm... This was quite steamy."
        pa1 "We gotta run home. Stuff to do."
        a "I can guess what..."
        scene 47-9 barscene 224 with Dissolve(0.5)
        b10 "Perhaps I could join you?"
        pa1 "Maybe next time."
        pa1 "But keep that idea in mind..."
        pa2 "Maybe..."
        scene 47-9 barscene 225 with Dissolve(0.5)
        a "See, it was pretty fun."
        e "I never said it wouldn't be."
        e "Just haven't done anything like this before."
        a "Yes you have."
        e "Not for money, haha."
        play music chill_song_2
        $ renpy.end_replay()
        scene 47-9 barscene 226 with Dissolve(0.5)
        j3 "Well."
        j3 "I think Patrick will be very satisfied."
        a "I hope so."
        a "We did a lot."
        j3 "Indeed you did, I would be if I was him."
        scene 47-9 barscene 227 with Dissolve(0.5)
        j3 "Went mostly smooth, besides that asshole who didn't pay for the drink."
        a "David paid for it."
        a "I assume we won't expect him here again."
        j3 "Gabe won't let him in."
        scene black with Dissolve(1)
        pause 1
        scene 47-9 barscene 228 with Dissolve(0.5)
        a "So. What do you think?"
        a "Would do this again?"
        e "Hmm... Maybe..."
        play sound surprise2
        scene 47-9 barscene 229 with Dissolve(0.5)
        pa "Good, good. Did well enough."
        pa "Be prepared for tomorrow. Things will really get crazy then."
        pa "Got more work to be done."
        a "Ok, sir."
        e "Tomorrow as well?"
        scene 47-9 barscene 230 with Dissolve(0.5)
        pa "Of course."
        pa "Always work to be done here, money to be earned."
        pa "Unless you don't like money."
        e "We do..."
        scene 47-9 barscene 231 with Dissolve(0.5)
        pa "Good to hear it."
        e "When will we get paid?"
        pa "We'll talk tomorrow more. If you do a good job, I will pay you tomorrow."
        scene 47-9 barscene 232 with Dissolve(0.5)
        e "Is he always like this?"
        a "Like what?"
        e "Like this?"
        scene 47-9 barscene 233 with Dissolve(0.5)
        a "Yes. But he's alright... He pays..."
        e "Doesn't sound convincing."
        a "Let's just come tomorrow and see..."
        a "He said things will get crazier..."
        a "Wonder what he meant..."
        scene black with Dissolve(0.5)
    else:
        scene 47-9 barscene 157 with Dissolve(0.5)
        e "Well. How about you guys?"
        e "Wanna join in on the fun?"
        b10 "Ladies first. Heh."
        scene 47-9 barscene 158 with Dissolve(0.5)
        e "He is not wrong."
        e "I can see that you wanna do something fun, eh?"
        scene 47-9 barscene 159 with Dissolve(0.5)
        pa1 "Well. Yeah... Heh. But."
        pa1 "Maybe not the drink."
        e "No problem. Perhaps something else?"
        scene 47-9 barscene 160 with Dissolve(0.5)
        e "I can give you whatever you want baby."
        pa1 "Oh yeah?"
        scene 47-9 barscene 161 with Dissolve(0.5)
        pa1 "How about you let me taste those lips?"
        e "They are all yours."
        play sound kisspeck
        scene 47-9 barscene 162 with Dissolve(0.5)
        e "Mmm."
        pa1 "Mhmm..."
        scene 47-9 barscene 163 with Dissolve(0.5)
        pause 1
        scene 47-9 barscene 164 with Dissolve(0.5)
        pa1 "And now... The other ones."
        e "Oh?"
        e "Alright."
        scene 47-9 barscene 165 with Dissolve(0.5)
        pa1 "Just lay down. Hehe."
        scene 47-9 barscene 166 with Dissolve(0.5)
        pa1 "You've got such a sexy body."
        e "You too, babe."
        e "We're both fine pieces of ass."
        scene 47-9 barscene 167 with Dissolve(0.5)
        pause 0.5
        play sound undress
        scene 47-9 barscene 236 with Dissolve(0.5)
        e "Well. What are you waiting for?"
        e "This innocent girl wants to have some fun."
        pa1 "Perfect."
        scene 47-9 barscene 169 with Dissolve(0.5)
        pa1 "I bet you will love this."
        play sound jerk2
        scene 47-9 barscene 170 with Dissolve(0.5)
        e "Oh... AAHHHH..."
        scene 47-9 barscene 237 with Dissolve(0.5)
        a "Hehe... Looks like my innocent angel can't contain herself."
        a "Even after I just punished her!"
        scene 47-9 barscene 176 with Dissolve(0.5)
        b10 "Damn, she got a nice ass."
        play sound femmoan_2
        b10 "She probably won't mind if I touch her, hehe."
        scene 47-9 barscene 177 with Dissolve(0.5)
        pa2 "That's my wife, dude."
        b10 "Shit. Sorry man. She beautiful, though."
        scene 47-9 barscene 178 with Dissolve(0.5)
        pa1 "Ah... Let him do it, honey, cmon."
        pa2 "Eh. Alright."
        pa1 "You know you like it."
        play sound femmoan_1
        scene 47-9 barscene 238 with Dissolve(0.5)
        b10 "Niice..."
        b10 "No panties. Heh."
        pa1 "My husband insisted."
        pa2 "Well. Of course."
        play sound female_moan_2
        scene 47-9 barscene 181 with Dissolve(0.5)
        b10 "So hot."
        b10 "Crazy things going on here, eh?"
        pa2 "You could say that."
        scene 47-9 barscene 239 with Dissolve(0.5)
        e "Oh... Fuck..."
        e "This is so hot..."
        e "Keep going..."
        scene 47-9 barscene 241 with Dissolve(0.5)
        a "Heh. Perhaps I should spank you too, Mrs. Malory?"
        pa1 "Nom... Nom... Mhm..."
        scene 47-9 barscene 242 with Dissolve(0.5)
        pa1 "Do it..."
        pa1 "I've been just as bad of a girl as Emily."
        pa1 "Punish me!"
        scene 47-9 barscene 243 with Dissolve(0.5)
        a "You know it!"
        a "And no one can save you, not even your husband!"
        a "You're in my domain now!"
        scene 47-9 barscene 244 with Dissolve(0.5)
        a "HYAAAH!"
        play sound spank2
        scene 47-9 barscene 245 with vpunch
        pause 1
        scene 47-9 barscene 246 with Dissolve(0.5)
        pa1 "AAHH!"
        pa1 "Hurts so good!"
        a "Exactly!"
        scene 47-9 barscene 247 with Dissolve(0.5)
        pa2 "Ohh... my..."
        pa2 "So hot..."
        pa2 "I know my wife deserves more spanking."
        a "You are absolutely right!"
        scene 47-9 barscene 248 with Dissolve(0.5)
        pause 1
        play sound spank1
        scene 47-9 barscene 249 with vpunch
        pa1 "AHHHAA!"
        scene 47-9 barscene 250 with Dissolve(0.5)
        pa1 "OHHAAAH."
        pa1 "Mmmm..."
        scene 47-9 barscene 251 with Dissolve(0.5)
        e "OH... Mrs. Malory. I'm so close!"
        e "AHHH!"
        play sound moaningfive
        scene 47-9 barscene 217 with Dissolve(0.5)
        e "Ahhh... AHHH!!!"
        e "OHHHAAA!"
        with flash
        e "YES!!"
        with flash
        with flash
        scene 47-9 barscene 218 with Dissolve(0.5)
        e "Oaaaaahhhhh!!"
        e "SO GOOD!"
        scene 47-9 barscene 219 with Dissolve(0.5)
        e "You are VERY good with your mouth."
        e "Been a while since I came like that."
        e "Amazing night, hehe."
        e "A lot of new experiences."
        scene 47-9 barscene 252 with Dissolve(0.5)
        b10 "Your wife is awesome. hehe..."
        pa2 "Thanks."
        scene 47-9 barscene 253 with Dissolve(0.5)
        pa2 "I aim to please, hehe."
        e "You did just that, haha."
        scene 47-9 barscene 223 with Dissolve(0.5)
        pa1 "Alright guys... Umm... This was quite steamy."
        pa1 "We gotta run home. Stuff to do."
        a "I can guess what..."
        scene 47-9 barscene 224 with Dissolve(0.5)
        b10 "Perhaps I could join you?"
        pa1 "Maybe next time."
        pa1 "But keep that idea in mind..."
        pa2 "Maybe..."
        scene 47-9 barscene 225 with Dissolve(0.5)
        a "See, it was pretty fun."
        e "I never said it wouldn't be."
        e "Just haven't done anything like this before."
        a "Yes you have."
        e "Not for money, haha."
        play music chill_song_2
        scene 47-9 barscene 226 with Dissolve(0.5)
        j3 "Well."
        j3 "We brought in very decent money today."
        j3 "That couple is pretty rich, The mid-long-haired man as well."
        a "I hope so."
        a "We did a lot."
        j3 "Indeed you did. I would be if I was him."
        scene 47-9 barscene 227 with Dissolve(0.5)
        j3 "Went smooth."
        j3 "As expected. Things are kind of better when Patrick is not around."
        j3 "Assholes seem to avoid this place when an asshole isn't running it."
        j3 "Let's do some even crazier things tomorrow."
        scene black with Dissolve(1)
        pause 1
        scene 47-9 barscene 228 with Dissolve(0.5)
        a "So. What do you think?"
        e "Seriously? Easiest money ever."
        a "You coming tomorrow too?"
        play sound surprise2
        scene 47-9 barscene 232 with Dissolve(0.5)
        e "Of course I am. I got pleasured, got money, and drinks."
        e "You know me, Anna. I'm a party girl, this felt like just the place to be."
        a "Haha. Great!"
        scene 47-9 barscene 233 with Dissolve(0.5)
        a "Let's think about something for tomorrow."
        a "This could become a very lucrative endeavor with your help."
        e "Hehe. I'm looking forward to what you and Jim will come up with for tomorrow."
        a "Me too..."
        scene black with Dissolve(0.5)
label EP17_Ending:
    jump EP18_Begin
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
