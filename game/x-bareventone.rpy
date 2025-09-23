label BarEventOne:
    play audio door2
    play audio walk
    play music barsong
    scene black with Dissolve(1)
    scene 33-7 bar 1 with Dissolve(1)
    "When she entered, Anna noticed that the bar was very lively."
    "It was a Friday night, so everyone was out, partying. But for Anna, this evening had been eventful."
    "Full with all kinds of interesting situations. And it wasn't over."
    a "{i}...I should go to Jim..."
    play sound surprise
    scene 33-7 bar 2 with Dissolve(1)
    "Anna approached The bar and immediately was met with David and Jim."
    j3 "Oh, hello, Anna. Haven't seen you for a while."
    a "Hey, Jim. I've been busy, hehe..."
    a "{i}...If only he knew..."
    j3 "That's good to hear. We should all strive to fulfill ourselves."
    scene 33-7 bar 3 with Dissolve(1)
    a "Looks like you're busy today."
    j3 "Oh, yes. a lot of activity today."
    j3 "Keeps me on my toes, luckily you're here now. Should make it easier."
    j3 "You're always so good with customers. If you know what I mean?"
    a "Hehe... I guess..."
    "Anna was a bit uncomfortable with the fact, but there was nothing she could do."
    scene 33-7 bar 4 with Dissolve(1)
    da "How is my favorite bartender doing? I heard from Ethan that you've been promoted?"
    if dianaGoodRelations == False:
        a "Yeah, I've been promoted to head of department. More responsibilities, but also more perks."
    else:
        a "Yeah, I've become the new partner. I have a lot of experience, so they choose me as a reasonable candidate."
    da "I suppose congratulations are in order. I always knew you'd make it."
    scene 33-7 bar 5 with Dissolve(1)
    da "How about a drink on me? We should celebrate a bit, eh?"
    a "Oh. That sounds nice, but you know, my shift's about to start."
    da "I know, but one drink wouldn't hurt, would it?"
    a "It wouldn't..."
    a "God knows I could use one."
    scene 33-7 bar 6 with Dissolve(1)
    j3 "Sorry, David. Duty calls. There are some things I have to discuss with Anna."
    da "The party pooper. I won't tip you next time, Jim."
    j3 "Like you ever do, old fool. Haha..."
    a "Guys, no need to fight over me. There's plenty of that going around."
    j3 "Alright, let's go. You can buy her a drink after her shift."
    scene 33-7 bar 7 with Dissolve(1)
    j3 "Hey, Gabe. Can you hold the fort for a while? Gonna go to the back for a bit."
    ga "Will do, sir."
    a "Hey, Gabe."
    ga "Hey, Anna."
    play music jazzmusic
    scene 33-7 bar 8 with Dissolve(1)
    j3 "So. Now that we are away from prying eyes and ears. I wanted to discuss something."
    j3 "I will get straight to the point."
    j3 "I know you don't like Patrick, and he treats you poorly. How about we do something about it?"
    a "What? I mean yeah but what could we do."
    a "Not like going to the police or something would do any good, if we exposed his dirty secrets, he would do the same for us."
    scene 33-7 bar 9 with Dissolve(1)
    j3 "Well, I haven't figured out that part yet, but I know that you want to change something."
    j3 "Plus, I also don't like Patrick. He used to be different but has changed, for the worse."
    j3 "If we could somehow... Remove him and change leadership. I think we could make this place into something much better."
    a "Well... When you put it that way... Perhaps, yeah."
    scene 33-7 bar 10 with Dissolve(1)
    a "But I still have no idea what. I mean. I don't hate him, but he is pretty vile."
    j3 "What if I can present you with some options?"
    j3 "Since we would take over, we would make decisions 50/50 and split the income like that, too."
    a "That sounds good. What do you have in mind?"
    play sound surprise
    scene 33-7 bar 11 with Dissolve(1)
    lu "What is going on? What are you plotting, eh?"
    lu "You both should be working! Get back to it."
    j3 "Shut it, slime ball, you're still wet behind the ears. Don't give me orders."
    lu "I will tell my daddy how you speak to me."
    scene 33-7 bar 12 with Dissolve(1)
    lu "Unless you let me see what Anna looks like underneath, again."
    a "Beat it, kid, we are discussing business."
    lu "I'm very versed in business. I pay attention to what my dad does, ok?"
    a "But this isn't regarding that we need some privacy."
    scene 33-7 bar 13 with Dissolve(1)
    lu "Cmon, let me in on the secret, I promise, I can help..."
    a "No, What don't you understand."
    lu "Not even touching your breasts? Hehe..."
    with vpunch
    a "Are you daft? I said NO!"
    scene 33-7 bar 14 with vpunch
    j3 "Lucas! I will tell you once more, get out of here, or I will tell Patrick that you steal liquor from behind the bar."
    lu "But I don't do that..."
    j3 "Yeah, right. But he doesn't know that, and who do you think he's gonna believe?"
    lu "Fine, sorry... I was just trying to help..."
    scene 33-7 bar 15 with Dissolve(1)
    lu "I will have my revenge someday..."
    j3 "Don't speak like that. you have to earn your place..."
    lu "Yeah, right..."
    scene 33-7 bar 16 with Dissolve(1)
    j3 "That kid has become so much more annoying..."
    a "I think we were a little too harsh to him..."
    j3 "Maybe, but he has to realize that just because his daddy is the owner doesn't give him free rein."
    j3 "He is not the king yet, so to speak..."
    j3 "Speaking of kings... How about we continue with the plan to take down Patrick?"
    j3 "But somewhere apparently more private..."
    play sound door2
    scene 33-7 bar 17 with Dissolve(1)
    j3 "Ok, so. I want your final answer, are you in or out? Because you are an important part of my plan."
    "Jim put Anna in a peculiar situation."
    menu:
        "Anna has had fun with clients previously and has become comfortable with it.":
            a "I'm sorry, Jim, but I can't do anything to Patrick. He has given me work. I will find another way..."
            j3 "Seriously? After everything he has done to you?"
            a "I know... Still..."
            j3 "Your call, but just know, if we continue like this, you will simply become his toy..."
            a "Don't talk like that..."
            $ bar_var_1 = True
            $ bar_var_2 = True
            $ corruption_func("Anna Corruption +3")
            $ AnnaCorruption += 3
            jump JimAnnaDressingRoom
        "Anna has never been a willing subject and has had enough.":
            a "Of course, fuck Patrick. I'm in."
            a "I wanted to leave anyway. I couldn't take it anymore."
            j3 "Ok, so first things first."
            j3 "Put on the new outfit. I'm sorry, it's what Patrick chose, but remember, it's for the greater good."
            $ bar_var_1 = False
            $ bar_var_2 = True
            $ corruption_func("Anna Corruption +1")
            $ AnnaCorruption += 1
            jump JimAnnaDressingRoom
label JimAnnaDressingRoom:
    if bar_var_1 == True:
        play sound undress
        scene 33-7 bar 18 with Dissolve(1)
        j3 "Alright, that's your choice."
        j3 "Remember that we didn't talk about it. Or there will be a problem."
        a "I got it..."
        j3 "Anyway, I got an outfit for you, Patrick's orders. This will be a crazy night."
        play sound undress
        scene 33-7 bar 19 with Dissolve(1)
        a "Ok, I will wear it. I just need the money..."
        a "Just don't look, ok?"
        j3 "I'm not. Don't worry, although, since you're our employee, we have to examine you."
        a "I don't think I will work naked here."
        j3 "You never know."
        play sound undress
        scene 33-7 bar 20-1 with Dissolve(1)
        j3 "Wow. I got to admit, you look very good."
        j3 "Very sexy in this..."
        a "It is pretty revealing. I don't know how I feel about it..."
        j3 "Well, it will make your job much easier, I suppose."
        scene 33-7 bar 21 with Dissolve(1)
        j3 "Patrick made a good decision, for once."
        a "It's really skimpy..."
        j3 "You could say that..."
        a "Alright, I'm ready."
        scene 33-7 bar 22 with Dissolve(1)
        j3 "Well, not yet. I wanted to 'examine' everything first."
        a "What? I don't think it's necessary."
        j3 "I believe it is. I have to go to Patrick later and tell him if the outfit felt good."
        j3 "He always asks me about that."
        play sound undress
        scene 33-7 bar 26 with Dissolve(1)
        j3 "Anyway, I think it's high time for you to get to work. I still have to work out some details."
        j3 "Be ready any moment, ok?"
        a "Will do. Any specific requests from anyone?"
        j3 "Before you go, quickly go to Patrick. he summoned you."
    else:
        play sound undress
        scene 33-7 bar 18 with Dissolve(1)
        j3 "So. I would need you to be on top of your game today, be willing to do whatever is necessary."
        a "Yeah, I got that. What exactly do you need?"
        j3 "You know those two drunks that come here often? The bald guy and the other one? I know they are bad and pretty dumb."
        a "What makes you so sure they will be here today?"
        j3 "They never miss a Friday."
        j3 "So, I want you to make them really drunk and convince them to take money from a safe in Patrick's office."
        a "Why would they do it?"
        j3 "They are criminals, they will be drunk, and they will want their money back after spending it on expensive drinks."
        a "I see. Ok. What are you gonna do?"
        play sound undress
        scene 33-7 bar 19 with Dissolve(1)
        j3 "To be honest, I would rather not tell you. The less you know, the better. Ok?"
        a "Ok, sounds bad."
        j3 "Don't worry about it too much."
        j3 "You will know when the time is right. Right now, it would just put too much pressure on you."
        j3 "Also, when you convince them, just tell them that there is something in the fire extinguisher box."
        a "I guess I can try."
        play sound undress
        scene 33-7 bar 20-1 with Dissolve(1)
        j3 "Wow. I got to admit, you look very good."
        j3 "Very sexy in this..."
        a "It is pretty revealing. I don't know how I feel about it..."
        j3 "Well, it will make your job much easier, I suppose."
        scene 33-7 bar 21 with Dissolve(1)
        j3 "Sorry, it is what Patrick chose, like I said before."
        a "It's fine. I guess I won't have to wear this after the plan goes through?"
        j3 "You could say that..."
        a "Alright, I'm ready."
        scene 33-7 bar 22 with Dissolve(1)
        j3 "Well, not yet. I wanted to 'examine' everything first."
        a "What? I don't think it's necessary."
        j3 "I believe it is. I have to go to Patrick later and tell him if the outfit felt good."
        j3 "He always asks me about that."
        play sound undress
        scene 33-7 bar 26 with Dissolve(1)
        j3 "Anyway, I think it's high time for you to get to work. I still have to work out some details."
        j3 "Be ready any moment, ok?"
        a "Will do. Any specific requests from anyone?"
        j3 "Before you go, quickly go to Patrick. He summoned you."
        j3 "Also ask him about how long he will stay in the office. It's important to our plan."
    play sound door2
    jump PatrickOfficeScene
label PatrickOfficeScene:
    play sound door2
    scene black with Dissolve(1)
    if bar_var_1 == True:
        scene 33-7 bar 27 with Dissolve(1)
        a "Hello, Patrick. You wanted to see me?"
        pa "Greetings, Anna. Long time no see, eh? I just wanted to see the outfit for myself. How it looks on you..."
        pa "And I got to admit, it's very sexual, and I love it. I love sexualizing your body. It's so perfect for it."
        a "Is that all?"
        pa "Yes. I have high hopes for you today."
        scene 33-7 bar 28 with Dissolve(1)
        pa "As I see, you've added your own panties. They were not with the set."
        pa "I asked for no panties..."
        a "It will give me more room to play."
        pa "Good, good, smart girl. But if a patron is willing to pay enough, you better take them off."
        scene 33-7 bar 29 with Dissolve(1)
        a "I know."
        pa "So the usual thing today. Be the usual slut and get the tips. I will give you good money for that."
        a "Yes sir..."
        play sound takephoto
        scene 33-7 bar 30 with flash
        "While Anna and Patrick were talking, Lucas took a quick photo of Anna."
        a "Excuse me? What are you doing?"
        lu "Nothing you have to worry about, just gonna send my schoolmates some pictures."
        lu "They will be so jealous."
        a "You are a little pervert, Lucas. Ugh."
        lu "But you are just a little slut, Anna."
        scene 33-7 bar 31 with Dissolve(1)
        a "Don't be like that..."
        lu "I wanna touch your breasts, Anna."
        pa "Lucas, enough!"
        scene 33-7 bar 32 with Dissolve(1)
        pa "Get back to your damn homework."
        pa "You will have enough times to touch titties..."
        pa "And you. Get to work. Tonight is pretty active."
        a "Sure..."
    elif bar_var_1 == False:
        scene 33-7 bar 27 with Dissolve(1)
        a "Hello, Patrick. You wanted to see me?"
        pa "Greetings, Anna. Long time no see, eh? I just wanted to see the outfit for myself. How it looks on you..."
        pa "And I got to admit, it's very sexual, and I love it. I love sexualizing your body. It's so perfect for it."
        a "Is that all?"
        pa "Yes. I have high hopes for you today."
        scene 33-7 bar 28 with Dissolve(1)
        pa "As I see, you've added your own panties. They were not with the set."
        pa "I saw it as an upside. I wanted you to show your assets off completely, earn us more money."
        a "No, it's a bit too much."
        pa "In that case, 75%% of the tips your earn this evening will come to me as tribute."
        scene 33-7 bar 29 with Dissolve(1)
        a "But, that's not fair..."
        pa "The world ain't fair, honey. Just gotta deal with it."
        a "This is ridiculous. Without me, this place wouldn't earn as much."
        pa "Without me, you wouldn't be here in the first place. Probably would be some common street whore."
        a "This is inappropriate..."
        play sound takephoto
        scene 33-7 bar 30 with flash
        "While Anna and Patrick were arguing, Lucas took a quick photo of Anna."
        a "Excuse me? What are you doing?"
        lu "Nothing you have to worry about, just gonna send my schoolmates some pictures."
        lu "They will be so jealous."
        a "You are a little pervert, Lucas. Ugh."
        lu "But you are just a little slut, Anna."
        scene 33-7 bar 31 with Dissolve(1)
        a "Shut up, you little rat!"
        lu "DAD. She called me a rat!"
        lu "Put her in her place!"
        a "Yeah, cry to your daddy, little asshole!"
        scene 33-7 bar 32 with Dissolve(1)
        pa "That's enough!"
        pa "Anna, you will come here later and give me 75%% of the tips you get, got it?"
        "Anna remembered to ask Patrick about how long he will be here."
        a "Umm, How long will you be here? Just so I know, when I could bring the tips at the latest?"
        pa "I will be here all night. Sitting back and gazing upon my empire."
        a "I'll get to work then..."
    $ bar_var_3 = True
    play sound door2
    jump BarEventOneJim
label BarEventOneJim:
    play music barsong
    scene black with Dissolve(1)
    if bar_var_1 == True:
        scene 33-7 bar 33 with Dissolve(1)
        "Anna entered the bar area, and she could feel eyes on her, lustful eyes."
        "Everyone was checking her out. She was so sexy, so succulent. Anna could either embrace it or act awkward."
        "That was up to her."
        play sound surprise
        a "Oh, Emily. Didn't expect to see you here."
        e "I didn't have anything to do at home on Friday night. Plus, David is always good company. Nice outfit, by the way."
        a "I just had to change into this for tonight... It's ridiculous..."
        e "It is pretty sexy, not gonna lie. I like it."
        a "You like all of the things I wear, Emily. Haha."
        scene 33-7 bar 35 with Dissolve(1)
        e "How about you buy me a drink, David?"
        da "How could I say no to you."
        da "Give us your best bourbon, Jim!"
        j3 "Coming right up!"
        scene 33-7 bar 36 with Dissolve(1)
        j3 "Just gotta say, this light makes you look even hotter. Sorry."
        a "Oh, it's ok. Quickly went to Patrick. He seemed satisfied."
        j3 "That will make things easier, I suppose."
        a "No doubt."
        scene 33-7 bar 37 with Dissolve(1)
        j3 "I already poured the drinks for the couple that usually come here."
        j3 "Just take it to them. They also asked for you to approach them."
        j3 "Seemed interested and very chatty. Perhaps you can strike up a conversation. Get them to buy more. You know?"
        a "Ok, I get it. I Will try."
    else:
        scene 33-7 bar 33 with Dissolve(1)
        "Anna entered the bar area, and she could feel eyes on her, lustful eyes."
        "Everyone was checking her out. She was so sexy, so succulent. Anna could either embrace it or act awkward."
        "That was up to her."
        play sound surprise
        a "Oh, Emily. Didn't expect to see you here."
        e "I didn't have anything to do at home on Friday night. Plus, David is always good company. Nice outfit, by the way."
        a "I just had to change into this for tonight... It's ridiculous..."
        e "It is pretty sexy, not gonna lie. I like it."
        a "You like all of the things I wear, Emily. Haha."
        scene 33-7 bar 35 with Dissolve(1)
        e "How about you buy me a drink, David?"
        da "How could I say no to you."
        da "Give us your best bourbon, Jim!"
        j3 "Coming right up!"
        scene 33-7 bar 36 with Dissolve(1)
        j3 "Just gotta say, this light makes you look even hotter. Sorry."
        a "Oh, it's ok. Had a fight with Patrick and his stupid little kid."
        j3 "That will make things easier, I suppose."
        j3 "Did you get the time until he leaves?"
        a "He's staying here all night."
        j3 "Ok, so I have plenty of time to get things done."
        scene 33-7 bar 37 with Dissolve(1)
        j3 "I already poured the drinks for the couple. Just take it to them. They also asked for you to approach them."
        j3 "Seemed interested and very chatty. Perhaps you can strike up a conversation. Get them to buy more. You know?"
        a "Ok, I get it. I Will try."
        j3 "You are amazing, Anna. You and I will change this place into something amazing later on."
        a "I will count on that, hehe."
    $ bar_var_5 = True
    jump BarEventOneCouple
label BarEventOneCouple:
    scene black with Dissolve(1)
    play sound surprise
    scene 33-7 bar 39 with Dissolve(1)
    a "Hello again, One bottle of our finest white, dry wine. Is there perhaps something else you would like?"
    pa1 "We are fine now, that you are here..."
    a "Are you sure you want this very, very expensive drink. Perhaps we could get you something a bit cheaper?"
    pa1 "Definitely not. We want to enjoy something very nice, with someone very nice. Hehe..."
    scene 33-7 bar 40 with Dissolve(1)
    pa1 "I think you would be a perfect candidate."
    pa1 "Don't you think so, honey?"
    pa2 "I absolutely do."
    pa1 "See, we are both interested for you to have a chat with us."
    scene 33-7 bar 41 with Dissolve(1)
    pa2 "Why don't you sit down with us? Enjoy the drink and just chat?"
    a "I don't know, I think I should get back to work."
    a "It's not that I don't want to, but I don't know if I should. What if the boss gets upset?"
    pa1 "You are very loyal, it seems and do what's told of you?"
    a "I suppose so..."
    scene 33-7 bar 42 with Dissolve(1)
    pa2 "So, come on, sit with us, and let's vibe a bit?"
    pa2 "You can afford to take a little break. Right?"
    a "Well. I guess I could enjoy your company for a bit longer."
    a "But..."
    scene 33-7 bar 43 with Dissolve(1)
    "Anna looked at Jim as though asking him for permission."
    "Jim, of course, nodded and allowed Anna to service her customers with any request they had."
    a "Alright, I suppose I can sit down."
    pa2 "Wonderful, that's what I like to hear. Have a drink on us."
    scene 33-7 bar 44 with Dissolve(1)
    a "So, I think I've noticed you in this bar several times, actually."
    pa2 "Yeah, we are just here to have fun and see where life takes us."
    pa2 "We've been in a relationship for so long and are trying to expand our horizon more."
    pa2 "These kinds of places are the perfect opportunity."
    scene 33-7 bar 45 with Dissolve(1)
    pa1 "Relationships can become somewhat... Stale after some time."
    pa1 "So my dear husband and I are both just exploring new things... New people."
    a "Don't you get upset with each other?"
    pa1 "We don't. Absolutely not, because we do it together."
    pa1 "And it's a fun experience."
    scene 33-7 bar 46 with Dissolve(1)
    pa1 "And you know, you look like a very fun experience, too."
    a "I know, I like to enjoy people."
    a "But, you could take the first step..."
    pa1 "Really? Like what?"
    a "Well, you could start with touching my leg."
    play sound undress
    scene 33-7 bar 47 with Dissolve(1)
    pa1 "I think it would be just as enjoyable for you as it would be for us."
    a "I definitely have to agree with that."
    a "You like how my leg feels through this soft fishnet?"
    pa1 "I do..."
    a "How much have you drunk already? Haha."
    pa1 "Not much, about the same as this bottle."
    scene 33-7 bar 48 with Dissolve(1)
    "As the woman was touching Anna, she could feel some excitement building up between her thighs."
    a "You see? It's not that hard. But I know you like it."
    pa1 "Oh... Yes..."
    pa1 "We've been talking about you and fantasizing about you. You've got no idea about the dirty thoughts we've had..."
    a "Well... Tell me..."
    scene 33-7 bar 49 with Dissolve(1)
    pa1 "Can't reveal all our cards at the beginning, now can we?"
    pa1 "I suppose you will just have to wait and see."
    a "Mysterious? Now you have my attention, sweety."
    "Anna was feeling light warmth going through her entire body as Mrs. Malory continued to touch her."
    "Mr. Malory was also getting pretty into it, fantasizing about fucking his wife and Anna..."
    play sound surprise
    scene 33-7 bar 50 with Dissolve(1)
    e "Looks like they are getting it on, damn."
    e "Anna, you horny little girl. I love you..."
    da "Emily, you are the same, one perverted, fun, open girl."
    e "And you definitely enjoy that, every time, don't you?"
    da "Without a doubt."
    scene 33-7 bar 51 with Dissolve(1)
    j3 "Hey, Can you go and call Anna over? I wouldn't mind her staying there, but we have some other patrons."
    j3 "They need attention. So just ask her to get back here."
    e "You definitely know how to ruin a party, Jim."
    j3 "She's working. Plus, we have to cater to some other people."
    e "Fine, fine..."
    play sound surprise
    scene 33-7 bar 52 with Dissolve(1)
    e "Sorry to break your party up, but Anna is needed at the bar."
    a "Oh... That's a shame. I was having fun here..."
    pa1 "Indeed, but no worries, there are plenty of other times."
    pa2 "We will come here often. You are worth the wait."
    scene 33-7 bar 53 with Dissolve(1)
    e "That's sweet. I would even want to join you guys."
    e "Sounds like the party is right here."
    pa1 "Haha... It might as well be later on."
    e "I will be sure to keep an eye on you two."
    pa1 "I hope you like what you see, then..."
    play sound undress
    scene 33-7 bar 54 with Dissolve(1)
    a "This was very... Interesting, I hope we can continue where we left off, later on..."
    pa1 "You and me both..."
    a "I will take the plate, if you don't mind, ok?"
    pa1 "Be my guest, darling."
    scene 33-7 bar 55 with Dissolve(1)
    e "It looks like you were having fun, Anna."
    e "A shame that Jim is a party pooper. Haha."
    a "Haha. Right? I will be alright. I can probably find some other times to talk with them more."
    e "As if talking is what they want..."
    a "Hey, they are just very nice people."
    scene 33-7 bar 56 with Dissolve(1)
    j3 "Seems like you had fun there, didn't you?"
    j3 "That little interaction there gives me an idea. But for now, I will not tell you about it."
    a "Sure, so what do you want me to do?"
    j3 "Right now, nothing much. Just go and ask the guy in the red flannel if he wants something."
    a "Ok, I will do so."
    scene 33-7 bar 57 with Dissolve(1)
    e "What are you two plotting there?"
    e "Trying to take over the bar or something?"
    a "What? Absolutely not, Emily."
    j3 "We are just looking who else needs services."
    da "I wouldn't mind some services from someone smoking hot."
    da "Speaking of that, Emily, would you like to go out for a cigarette?"
    e "Oh, look who's a smooth talker now. Sure, let's go."
    $ bar_var_6 = True
    jump BarEventOneRedFlannel
label BarEventOneRedFlannel:
    if bar_var_6 == True:
        scene black with Dissolve(1)
        scene 33-7 bar 58 with Dissolve(1)
        "While Anna was servicing the guy in the flannel. Two idiots walked into the bar."
        ro "Oh, look who we got here. David already got a girl on your hands."
        da "Yeah, well. It was nice to talk to you. Now move."
        ro "Very courteous, as always."
        da "If you two weren't such asses, maybe there would be better times."
        ro "Don't say something you'll regret..."
        scene 33-7 bar 59 with Dissolve(1)
        ro "But, I ain't here for that today anyway."
        da "I know why you're here, to get shitfaced as usual and then harass the girls."
        le "It ain't harassin'. We are simply mingling. Having fun."
        da "At the expense of others, of course."
        ro "Whatever. You just talk bullshit all the time, anyway."
        ro "Get out of my way. I want to have a drink."
        scene 33-7 bar 60 with Dissolve(1)
        ro "Damn, jackpot today."
        le "Who is that. Seems similar to Anna but not the hair."
        ro "Yeah, can't see her face."
        ro "But look at that outfit though, maybe we are in luck today..."
        jump BarEventOneDrunks
label BarEventOneDrunks:
    if bar_var_1 == True:
        play sound surprise
        scene 33-7 bar 61 with Dissolve(1)
        ro "Hey, Jim. Who's that. Is it Anna?"
        j3 "Who else could it be? Anyway, how can I be of service?"
        ro "We want to get fucked up, so give us your best!"
        ro "And then later... Maybe a bit of private time with Anna."
        j3 "She isn't a hooker or an escort."
        ro "We'll ask her about that."
        scene 33-7 bar 62 with Dissolve(1)
        le "Hello, Anna. Lookin' As hot as always."
        le "Wanna have fun?"
        a "Come on, guys, it doesn't work that way."
        ro "Riight. You'll come around."
        scene 33-7 bar 63 with Dissolve(1)
        "As soon as Anna went behind the bar, Jim leaned in."
        j3 "It's showtime. Let's see how wild it gets tonight."
        j3 "Let's get some money out of these fools."
        a "Yeah, I got this."
        j3 "Good to know."
        scene 33-7 bar 64 with Dissolve(1)
        a "Well, you're in luck tonight, boys. We've got a special evening tonight."
        ro "Fuck yeah! Bring it on."
        le "Yeeah. Let's get drunk."
        j3 "We've got some special drinks prepared for tonight."
        scene 33-7 bar 65 with Dissolve(1)
        le "Everything special we need is this hot bitch, Anna."
        "Anna didn't like hearing this but she was going with it."
        a "Hehe... You know it. Who knows where the night might go."
        le "Hopefully to all the 'wrong' places. Haha..."
        le "Now get us some drinks. I'm ready to get fucked uuuuppp!!!"
        play sound pourwater
        scene 33-7 bar 66 with Dissolve(1)
        j3 "Our finest whiskey, bourbon coming right up."
        j3 "These are on the house. Considering that you've been such good clients of ours."
        ro "Now, this is what I call bottle service."
        a "This night is all about you. And I mean everything."
        ro "You never cease to amaze."
        scene 33-7 bar 67 with Dissolve(1)
        ro "But goddamn, can't take my eyes off of you, girl."
        ro "Tell me that you are a part of tonight's fun?"
        a "Let's see where it goes, huh?"
        ro "Alriiight."
        scene 33-7 bar 68 with Dissolve(1)
        ro "Bottoms up."
        "Leslie didn't hesitate and took shots like he was bulletproof."
        "Immediately regretted taking it so fast."
        j3 "Drink up, my friends. This is going to be a fun night."
        scene 33-7 bar 69 with Dissolve(1)
        le "That is some good whiskey, not gonna lie."
        j3 "Only the top shelf for you guys."
        ro "Alcohol is all the same to me. All the same, all I care about is getting fucked up!"
        ro "And getting rowdy. Let me tell you. We are in some good stuff right now."
        ro "Extorted some businesses, but since you guys are the cool ones, we won't do it here."
        scene 33-7 bar 70 with Dissolve(1)
        j3 "That's good to hear. how about some cocktails, huh?"
        ro "You read my mind."
        j3 "I call this cocktail the: 'The Ex-Wife'"
        ro "That sounds like one hell of a drink."
        ro "Sign me up for two! Haha!"
        "Both men, especially Ron, were getting pretty noisy."
        scene 33-7 bar 71 with Dissolve(1)
        j3 "I hope you are ready for this one."
        ro "Damn right I am."
        "Jim started mixing the cocktails for both 'gentlemen'"
        le "Alright, I'm feeling good and want to dance with some hot bitches."
        ro "You and me both, but first we gotta get hammered, then we find some whores to fuck."
        label BarSexScene:
            $ renpy.music.play("audio/sounds/BarSong.mp3", channel = 'music', if_changed = True)
        scene 33-7 bar 72 with Dissolve(1)
        j3 "Here are the cocktails. Enjoy them. That will be 300$ each. But you will get a bonus with it. If you know what I mean?"
        ro "What? That's more expensive than previously!"
        ro "I feel like it's too expensive..."
        le "Yeah. I feel like you have to convince us."
        play sound surprise
        scene 33-7 bar 73-1 with Dissolve(1)
        "Anna hopped on the bar and approached Ron."
        a "Oh come on, if you buy them, I will let you take remove something from my outfit."
        ro "You are absolutely wild tonight. I like that!"
        ro "Well, in that case, I'm fucking in!"
        scene 33-7 bar 74-1 with Dissolve(1)
        "Both of the men started to chug the cocktails. The drinks were interesting in taste but gave a good kick."
        a "Yeah, just like that. Drink up. I want you to drink it all up for me."
        "Jim was enjoying the view too. Just gazing as Anna worked her magic on those two idiots."
        j3 "{i}...Damn, she's hot as fuck... Maybe when all of this is over, I could get with her..."
        scene 33-7 bar 75 with Dissolve(1)
        ro "That was... Too... Easy... Agh..."
        le "You think? I'm barely able to hold it. That drink was so fucking hardcore..."
        ro "You're just a pussy, Leslie!"
        le "Am not. Anyway, how about you keep up with your part of the deal. We finished our drink, no problem."
        a "Fine, fine. you win..."
        scene 33-7 bar 76 with Dissolve(1)
        le "Your titties are so nice. And big, and round."
        a "Thank you... Don't be shy. Take off the covers."
        "Anna knew what was at stake, so she rolled with it."
        le "I wouldn't have it any other way."
        "The sexual tension was rising in the bar area."
        "Some of the patrons were looking on and enjoying the view."
        scene 33-7 bar 77 with Dissolve(1)
        "Both of them started touching Anna's tits. enjoying the feel. groping her."
        a "Ah..."
        "She was a little bit stimulated. the entire vibe was so experimental."
        ro "Yeah, you like that, don't you..."
        le "Of course she does. Just look at her face."
        play sound undress
        scene 33-7 bar 78 with Dissolve(1)
        ro "And they are off. Damn girl..."
        "They had unraveled the nipple covers and saw Anna's beautiful breasts unleash their full potential."
        le "They are so fucking good. I wanna just drown in those boobs."
        ro "Wait your turn, Les."
        scene 33-7 bar 79 with Dissolve(1)
        "The couple looked from afar and enjoyed the show."
        pa1 "Those lucky bastards, eh?"
        pa2 "Don't worry, we will have our turn at some point."
        pa2 "For now, let's just enjoy the show, honey."
        pa1 "She is so beautiful. I want you to ram that cock into her pussy and then mine."
        pa2 "You and me both. That would be so hot."
        pa2 "But I also have this idea. Maybe we should also do the opposite. Two cocks penetrating you?"
        pa1 "Oh, husband. You know how to trigger my weaknesses..."
        play music activesong
        scene 33-7 bar 80-1 with Dissolve(1)
        "Emily had returned from smoking and was met with an amazing sight."
        e "{i}...My girl seems to be having a lot of fun without me..."
        e "I should help her a bit, loosen her up."
        e "Damn, I want a drink. Who's ready for shots?!"
        scene 33-7 bar 81-1 with Dissolve(1)
        e "Anna, what are you doing? Haha?"
        a "Oh, just entertaining the guests. And also enjoying myself."
        a "Where did David go?"
        e "He had to leave. Looks like I will have to find some other company for tonight."
        a "You wanna join?"
        e "Oh, you take the spotlight this time, honey."
        scene 33-7 bar 82 with Dissolve(1)
        "Jim had prepared the next set of cocktails for the two idiots."
        j3 "Here, more drinks for you, and if you chug those, this might all go even further."
        le "Damn, I don't know, kind of dizzy right now."
        ro "I told you guys, he's a pussy."
        le "Bro, I just don't wanna pass out before the real fun begins."
        scene 33-7 bar 83-1 with Dissolve(1)
        a "If you guys drink these, I will go further..."
        a "Show you a bit more of what I have to offer."
        ro "See, Leslie? We can't say no to a woman."
        le "Fuck. I got no choice in this one, hehe..."
        scene 33-7 bar 84-1 with Dissolve(1)
        a "Emily, you will have to join me."
        e "Oh? What do you have in mind?"
        a "I won't tell you just yet, first they chug. Then we improvise."
        e "I couldn't say no to you, Anna..."
        a "I know, hun. And you love it."
        scene 33-7 bar 85 with Dissolve(1)
        "Both men took the drinks and started to chug them in a fast manner."
        a "That's right. Keep doing that, and you will get me all in no time."
        le "Bottoms up... Fuuuck... I'm going to be trashed after this."
        ro "Maybe you, then I will have Anna all to myself. Fuck yeah."
        scene 33-7 bar 86 with Dissolve(1)
        "Without any hesitation, both gullible schmuks swallowed the entire drink in seconds."
        "Even if it meant them passing out, they knew they had to try and get that piece of ass, Anna."
        a "Damn, you boys are very, very rigorous drinkers."
        ro "What can I say. I'm a fucking BEAST! Now, show us what you got, slut."
        le "Yeah, we want more. Come on."
        scene 33-7 bar 87 with Dissolve(1)
        "Anna leaned down and arched her back. Taking up an inviting pose."
        a "Emily, sweety, would you help me with these panties?"
        e "Oh. Hehe... Would I. Come here, let me help you."
        ro "WHAAAT? Double girl action? Am I dreaming? Am I in heaven?"
        scene 33-7 bar 88 with Dissolve(1)
        "Emily approached Anna and caressed her a bit before starting to slowly slide off the panties."
        ro "Daamn. This is better than I could've ever imagined."
        le "Broo. These chicks are crazy. I love it."
        ro "If only I could get this kind of service every time I came here."
        play sound undress
        scene 33-7 bar 89-1 with Dissolve(1)
        a "Thank you, Emily. Now I will ask you to join me on this bar."
        e "Anna, this is crazy. Haha... Even I don't think I have it in me."
        a "Trust me, babe, you do. I will ask Jim to prepare a shot for us."
        e "I don't know..."
        scene 33-7 bar 90-1 with Dissolve(1)
        a "It's all or nothing. You just have to get up here."
        "Trust me, it's going to be fun."
        e "You naughty, naughty girl..."
        e "Ok, Fuck it. Let's do this."
        play sound undress
        scene 33-7 bar 91-1 with Dissolve(1)
        "Anna reached out with her hand. Emily was still a bit hesitant. She was just not drunk enough to reach her peak sluttiness."
        e "This is crazyyy."
        a "You know it, girl. And you love it."
        ro "This is fucking amazing. I'm going to fuck you both so hard you will pass out from pleasure."
        scene 33-7 bar 92-1 with Dissolve(1)
        e "Well, here I am. On the bar. Fuuck."
        e "I need that shot, Anna. Can you hook me up?"
        a "Of course. Come here. This is our strongest liquor."
        a "Are you ready for this?"
        play sound drinkingBeverage
        scene 33-7 bar 96-1 with Dissolve(1)
        "They both took the shot glasses and emptied them."
        "Emily was a bit drunk, but the cigarette coupled with the shot made her excited."
        e "Ah. This is stroong..."
        ro "Yeaah. That's what I like to see. Chicks enjoying themselves."
        le "Ron, stop with the... {b}*Gulp*{/b}... overacting, man."
        scene 33-7 bar 96 with Dissolve(1)
        a "Now on to some more interesting things, eh Emily?"
        e "What do you have in mind, you sexy girl."
        a "Whatever we want. Let's have it."
        ro "YEEAHHH. Let's goooo!"
        scene 33-7 bar 97 with Dissolve(1)
        a "Oh, Emily. We are barely drunk, and you are already enjoying me?"
        a "What's gotten into you?"
        e "I'm always like this, just need a little push..."
        ro "Come on then, show us your kinky side, girl. I can't wait to see."
        scene 33-7 bar 97-1 with Dissolve(1)
        "Anna started to slowly undress her friend's cleavage."
        "The titties were just waiting for an opportunity to be unleashed. No bra, nothing else to hide them if they were to come out."
        a "Oh, what do we have here. Some fun stuff, eh?"
        e "You know me, Anna. Always ready for a party. The less I wear, the easier it is..."
        scene 33-7 bar 98 with Dissolve(1)
        "From afar, some patrons were looking on and checking out the scene that was unfolding."
        "Both girls were getting pretty riled up, hot and naughty."
        stranger "Damn. I would like to include myself in that. Seems like an open event."
        stranger "Maybe I can get some touchy time..."
        play sound lighthit
        scene 33-7 bar 99 with Dissolve(1)
        "Emily pushed Anna down against the bar with a bit of power."
        a "Oh, Emily. What's gotten into you? You seem to be taking my power over, now."
        e "Girls just want to have fun, so here I am, taking what I want."
        a "Naughty, naughty girl. Come here..."
        scene 33-7 bar 100 with Dissolve(1)
        e "I'm going to enjoy you more than anyone ever has."
        e "You know I have a way with my hands and my mouth... And my pussy."
        e "I just know how to take you for all your worth."
        a "Fuck. Emily, give it to me."
        "Anna was getting wet and ready to be enjoyed."
        scene 33-7 bar 101 with Dissolve(1)
        "She pushed herself onto Anna, and their chests touched."
        a "Ah... You sexy beast..."
        ro "Yeeaaah... Let's gooo!"
        le "This is the best shit I've ever seen."
        play sound jerk
        scene 33-7 bar 102 with Dissolve(1)
        "Immediately, they started kissing each other passionately."
        "The drinks were strong and had finally worked their magic."
        "Anna was overtaken by sensation. Being seen by strangers, kissing with Emily."
        "She was on fire, she wanted more... And so did Emily..."
        scene 33-7 bar 103 with Dissolve(1)
        ro "Yeah. Give it to her. Show us what you got."
        "Meanwhile, Leslie started caressing Emily's leg. She didn't even feel it at first."
        le "You girls are so hot, I want to see more..."
        "Emily's legs were so soft and warm."
        le "{i}...Damn, what a fine woman... I want to penetrate her so bad..."
        scene 33-7 bar 104 with Dissolve(1)
        "Leslie's hand was going higher, towards her asscrack. Towards her panties."
        le "Let me just enjoy a little bit of this sexy piece of ass."
        ro "What you trying to do, Les? You dirty dog, haha..."
        le "Oh, just helping girls get rid of things that are in their way."
        ro "Such a gentleman..."
        scene 33-7 bar 105 with Dissolve(1)
        e "What are you doing there, you naughty boy?"
        le "Well, since Anna doesn't have panties, I'm just helping you with that."
        e "I guess we'll be matching, hehe..."
        le "That was the idea, yeah. You are both so sexy. I just can't wait to see more. This is amazing..."
        play sound undress
        scene 33-7 bar 106 with Dissolve(1)
        "Leslie slowly slid her panties down her thighs."
        "Emily felt small spasms through her body, as she felt that her and Anna's pussies were touching."
        a "Oh, you like that, don't you. I can feel it."
        e "You just shush and let me make YOU feel good."
        play sound jerk2
        scene 33-7 bar 107 with Dissolve(1)
        "Before Emily could do anything, Les slid his finger into her pussy ever so slightly."
        "Just enough to make her crave a cock. Just enough to open her, already wet, pussy walls."
        "Prepare them for penetration, for fucking..."
        e "Ah... I see your friend is enjoying me, too."
        a "I wouldn't have it any other way."
        scene 33-7 bar 108 with Dissolve(1)
        e "Well, I'm not going to let anyone have the upper hand on me this time..."
        e "How about you sit back and relax. I will just let you feel something that you absolutely love."
        a "And what would that be?"
        e "You will see..."
        play sound jerk
        scene 33-7 bar 108-1 with Dissolve(1)
        "Emily moved down to Anna's pussy hole. And started to lick it lightly. Just enough to stimulate Anna."
        a "Aah... I like... It..."
        "She was already feeling sensations. Emily always knew how to trigger her."
        j3 "{i}...Things are getting crazy here. Patron's are starting to look..."
        j3 "{i}...I hope it doesn't get out of hand..."
        play sound jerk3
        scene 33-7 bar 108-2 with Dissolve(1)
        "Anna looked down to Emily, and the sight made her get even steamier."
        "She was starting to sweat from the entire ordeal. People were watching. Emily was licking her pussy with such success."
        a "Ahh... Damn, Emily, you are very good... Oh..."
        e "Mhm... Mmm..."
        "Emily was enjoying this as much as Anna. She loved the taste of Anna's sweet, sweet pussy."
        "And the view of Anna's pleasured face was just as sexy..."
        play sound jerk2
        scene 33-7 bar 108-3 with Dissolve(1)
        a "Ahh... That's right. Just like that!"
        "Everyone was enjoying the sexual intercourse that was unfolding on the bar surface."
        "What seemed to be a regular Friday night had slowly started to turn into a sex-crazed depravity."
        "Onlookers were fantasizing about boning Anna or licking her up and down, or her sucking their dicks."
        scene 33-7 bar 109 with Dissolve(1)
        "Emily hastily changed her position so that their wet pussies would align."
        e "I want my pussy to feel your pussy, girl. Fuck!"
        a "Ahh... You are a fucking animal, Emily. I want you to take me..."
        ro "Damn, you girls are fucking crazy. I LOVE IT!"
        le "YEAH. Give it to her, Emily."
        play sound moaningfour
        scene 33-7 bar 110 with Dissolve(1)
        "Both men started to touch the girls. Feeling their luscious breasts swing in the air."
        "Emily was moving perfectly against Anna's lips. Rubbing each other and feeling the ecstasy building."
        "The air in the building was becoming hot and sweaty from the dancing, drinking, and well... The perverted sex that was going on."
        e "Aahh... Yeah. That's right..."
        a "Emily... AAhh... I'm so horny..."
        scene 33-7 bar 111 with Dissolve(1)
        pa1 "They are taking it further and further. Holy shit..."
        pa1 "They are actually scissoring already... That is so hot... I never believed I would see this happen in this bar."
        pa1 "It's so hot. I'm getting pretty fucking wet."
        pa2 "Yeah, it's a sight behold. I'm pretty hard myself, right now."
        play sound moaningfive
        scene 33-7 bar 112 with Dissolve(1)
        pa2 "If you want, you could go and join them..."
        pa1 "Even if we are exploring our sexualities... I don't think that I'm ready for that yet."
        pa1 "But I'm still so hella horny..."
        pa2 "Perhaps we should go home and do it?"
        pa1 "No, let's not wait, I want you to take me right now, in the bar toilets... Please... Ah..."
        pa2 "Ask no more..."
        scene 33-7 bar 113 with Dissolve(1)
        "Anna's back was arching in pleasure. She was in a world of satisfaction right now."
        "She was being stimulated by Emily and some strangers touching her tits."
        "She was getting more turned on with every second."
        "Being at their mercy. Being touched everywhere, scandalous, really."
        "People all around the bar were watching. Some left, some enjoyed the show."
        play sound jerk2
        play audio surprise2
        scene 33-7 bar 115 with Dissolve(1)
        "Out of nowhere, Ron pulled out his hard cock, and it immediately caught Anna's attention."
        a "What do we have here, huh?"
        ro "Oh, just a fun little experience."
        a "How about you give it to me, then?"
        "Anna was starting to lose all her inhibitions at this point."
        scene 33-7 bar 116 with Dissolve(1)
        j3 "This is getting pretty out of hand."
        j3 "Don't cum on the bar, or I will throw you out."
        "While Jim was talking, Emily, Anna, and the two guys were getting shitfaced, horny, and ready to fuck hard."
        "His words were passing their ears..."
        scene 33-7 bar 117 with Dissolve(1)
        "Les had also pulled out his cock. And Emily was in heat, wanted to suck on something."
        "As she was grinding on Anna's pussy, she was getting more and more turned on."
        "Didn't even care whose dick it was..."
        e "Fuck, I want something hard right now..."
        scene 33-7 bar 118 with Dissolve(1)
        "Anna instinctively took Ron's hard cock in her hand and started to stroke it."
        a "Yeah... That's one big, attractive cock right there."
        ro "Fuck, You are one crazy bitch. I love it."
        ro "Your hands on my cock, that's the best shit ever."
        play sound jerk
        scene 33-7 bar 119 with Dissolve(1)
        "At the same time, Emily had also started to caress Leslies dick."
        "So turned on, she didn't even notice the other people in the bar."
        "Looking at that dick. Her eyes locked on it. Fantasizing about it."
        e "You like it when I touch your dickhead?"
        le "Girl, I'm fucking crazy about it."
        scene 33-7 bar 120 with Dissolve(1)
        "Ron's dick was getting closer and closer to Anna's mouth."
        "She was opening it, preparing to receive the tip of his dick in her mouth."
        "Ron was in disbelief about it, but he wanted it so bad."
        "For Anna to suck on his stick, deepthroat it."
        scene 33-7 bar 121 with Dissolve(1)
        "She opened her mouth and took his member in slowly, but surely."
        ro "OH, YEAH! The best night of my life!!!"
        "Ron was so turned on, started to shout, other patrons around the bar were looking and didn't believe what they saw."
        "Anna was slowly starting to become a simple slut in the bar."
        "Eventually, maybe some cum dump for everyone to enjoy."
        scene 33-7 bar 122 with Dissolve(1)
        "Her mouth was completely wide open as Ron continued to push it deeper and deeper in her throat."
        "From one, side it was Emily grinding on her pussy lips. From the other side, it was Ron entering her mouth."
        ro "Your mouth is amazeballs. I love it when bitches suck my dick. Keep going, girl."
        ro "I want you to take it all the way... ALL THE WAY!! WOOOO."
        play sound jerk2
        show BarSexOne with Dissolve(1)
        "Ron started face-fuck Anna with his hard, big rod."
        a "Aah... {b}*GULP*{/b}"
        "Anna was choking on it. But loving it."
        ro "Take my dick. Yeah. I know you love it, you slut..."
        "And Anna did love it. Something hard and big in her mouth."
        show BarSexTwo with Dissolve(1)
        hide BarSexOne
        "She was taking the entire Ron's length..."
        "So masterfully, so elegantly."
        "Anna was a trained champ in sucking cock."
        "And onlookers, as well as Ron, were impressed."
        scene 33-7 bar 123 with Dissolve(1)
        "As for Emily, she was mesmerized by the big, long erect penis in front of her."
        "She wanted nothing more than to just enjoy it fully."
        e "I want it right now. Fuck I want it right fucking now!"
        le "I won't stop you, girl. Come here, suck on it."
        play sound jerk3
        scene 33-7 bar 124 with Dissolve(1)
        "She pulled off Anna and immediately went for the treasure in front of her."
        "Still on the bar with her ass in the air, she started to suck on Leslie's dong without hesitation."
        "Other patrons of the bar could see Emily's exposed pussy in doggy style."
        "Oh, if someone had the balls to just go for it and push his dick inside Emily..."
        "Then this bar night would turn into a full-fledged fuck fest."
        scene 33-7 bar 125 with Dissolve(1)
        "As the four perverts went further into the depravity of their sex-crazed fantasies, other people around them were cheering on."
        "Some left to find their sex adventures. Some started to go in the darker corners of the bar and make out. Or even act out on their fantasies."
        e "Mhh... Fuck, So good."
        le "FUUUUCK. This is some fine dick sucking. You are amazing."
        scene 33-7 bar 126 with Dissolve(1)
        "Now, the four horsemen of lust were in full-on blowbang."
        "All of them enjoying the moment, not caring about anyone else."
        e "MMfff... Ahh..."
        a "Ahm... KHaa..."
        "Both girls, choking on hard dicks, thinking about nothing more."
        scene 33-7 bar 126-1 with Dissolve(1)
        "As Ron was getting his dick deepthroated, he went for Anna's wet, plump pussy."
        ro "You are so moist there. I think you are ready for some dick fuck."
        a "Mhm..."
        "Anna couldn't talk, but she definitely did want a hard cock in her pussy."
        "Forgetting about everyone she cared about, all she wanted right now was to get fucked hard."
        play sound jerk3
        scene 33-7 bar 126-2 with Dissolve(1)
        "Ron pushed his fingers into her pussy."
        "And as he did that, Anna shivered in pleasure."
        "Unable to contain herself..."
        ro "I want to fuck your tight hole, Anna."
        play sound jerk2
        scene 33-7 bar 127 with Dissolve(1)
        ro "But first, I have to take a photo for memories and my boys."
        ro "How this bitch is sucking my dick. Fuck yeah."
        "Anna was unable to control herself. She wanted it all."
        ro "Ahh... Fuck yeah. This is the best sex party ever!!!"
        scene 33-7 bar 131 with Dissolve(1)
        ro "I want you to..."
        a "To fuck my tight pussy. I know. Please... Do it."
        ro "You won't have to ask me twice, girl."
        scene 33-7 bar 133 with Dissolve(1)
        "Both Anna and Emily got up."
        e "Fuck, I want some dick bad. Being in the middle of the bar makes it even better."
        e "I haven't been this turned on in a while."
        a "I'm so wet, right now..."
        scene 33-7 bar 134 with Dissolve(1)
        a "Come on, show me what you got, big boy."
        ro "Oh, I'm about to fuck you good, slut..."
        a "You better."
        "They were so in heat, they could barely talk about anything."
        scene 33-7 bar 135 with Dissolve(1)
        "Leslie was undressing Emily. So eager, so impatient. He was fantasizing about Emily passionately."
        "He noticed her the moment they entered the bar, and now she sucked his dick and was about to bounce on his rock solid cock."
        le "This is just so unbelievable. I wanna stick it in you so baaaad...."
        e "Give it to me. Please. I crave it."
        play sound undress
        scene 33-7 bar 136 with Dissolve(1)
        "Both men's long schlongs were sliding across girl's asses. Preparing to go as deep and as hard as possible."
        "To make them climax from the sheer built-up anticipation."
        "Anna was already breathing heavily while waiting for the entrance."
        "Emily had been completely disarmed from her clothes. Entirely naked in the middle of the bar."
        play sound jerk2
        scene 33-7 bar 137 with Dissolve(1)
        "Our guy Ron was starting to push it in slowly. Not rushing anywhere, enjoying every inch, every centimeter."
        "And so was Anna..."
        a "Aah... It's fucking big... Fuck. AAh... I..."
        ro "Yeah... Do you like that? You love it, don't you..."
        a "AAhh..."
        "Anna couldn't really talk. She was so depraved, so dirty. Barely in control of her body and emotions."
        "Was this really the beginning of the end of decent Anna? A girl that was soon going to be reduced to nothing but a simple fuck hole?"
        play sound jerk2
        play audio moaningfour
        show BarSexThree with Dissolve(1)
        a "{i}...Fuck, that dick... What's wrong with me..."
        a "{i}...I can't control myself..."
        a "Ahh..."
        scene 33-7 bar 138 with Dissolve(1)
        hide BarSexThree
        a "AAAAAAHH... Push it in more pleasee... I want..."
        ro "What? Say it!"
        a "I want your hard cock to fuck me deeper!"
        "Emily was enjoying how vulnerable and pleasured Anna looked."
        play sound jerk
        play audio moaningfive
        show BarSexFour with Dissolve(1)
        "The bar was bouncing..."
        "The room was filling with hot air and moans that were barely drowned out by the loud music."
        play sound jerk2
        scene 33-7 bar 138-2 with Dissolve(1)
        hide BarSexFour
        "Ron's penetration was sending Anna over the edge."
        "Her eyes rolled into her head from the pleasure. As the man's rock solid penis was annihilating Anna's sweet, sweet pussy."
        a "Ahh... This is... Fucking amazing..."
        "Both of them were fucking perfectly in unison."
        play sound moaningtwo
        scene 33-7 bar 139 with Dissolve(1)
        "Ron had pushed it in almost as deep as he could go, leaving just a little bit out."
        "Just in case he needed a bit more to satisfy this nympho."
        "He was surprised how Anna could take his entire length."
        ro "You're one freaky girl. I like it. Getting fucked in the middle of the bar."
        ro "When people are watching..."
        play audio jerk
        play sound moaningone
        scene 33-7 bar 140-2 with Dissolve(1)
        "On the other side, Emily was getting penetrated by Les. Slowly but surely."
        le "You are tight as fuck... Aahh..."
        e "Fuck... It's going innn... Feels like the biggest one I've had..."
        le "Yeah, you like it?"
        e "Aahh... It's so big inside of me... Keep pushing..."
        scene 33-7 bar 140 with Dissolve(1)
        e "That's it. Yeah... Aahh... FUUCK."
        le "Biitch... Your pussy is extra, extra fucking good."
        e "Yeah? You like fucking my tight cunt?"
        le "Aahh... It's the only thing I want to do..."
        play sound jerk2
        play audio moaningthree
        scene 33-7 bar 140-1 with Dissolve(1)
        e "ah... OOH... AAAHHHHHHH."
        "With a slow pace, Leslie had finally pushed his enormous fuck-stick into Emily's twat."
        "She was barely able to process how such a large cock could go into her."
        "She was also very proud of herself, besides the incomprehensible new pleasures."
        e "This is... A first for me... Fuck..."
        scene 33-7 bar 141 with Dissolve(1)
        "As they both were getting fucked hard..."
        "They looked at each other... Both of their faces filled with pleasure."
        "And seeing each other in ecstasy, they enjoyed the entire ordeal even more."
        e "Fuck... Mh... You are so sexy when you look like this..."
        a "AAh.."
        a "Ahh... You, too... Emily, you are fucking hot..."
        play audio moaningfour
        play audio moaningthree
        scene 33-7 bar 142 with Dissolve(1)
        "Both men were enjoying the pleasures of the girl's pussies."
        "The bar had loud music and other noises, but you could hear the female moans in the background a bit."
        "They were looking at each other and not thinking about anything else."
        "Just the moment they were in, getting fucked by some random men."
        "What was Anna turning into..."
        play sound jerk2
        scene 33-7 bar 143 with Dissolve(1)
        "As if they had planned this before, both Ron and Leslie decided to pull out their dicks of the girl's holes..."
        "And switch to the other opening... The Asshole..."
        "The girls didn't know what to expect."
        "They were still coming down from the pleasurable pussy fuck they just received..."
        play sound jerk2
        scene 33-7 bar 144 with Dissolve(1)
        "No hesitation, no slow entry. Ron Just pushed it in without any pause."
        "Almost the entire length. Pushed it in raw. His cock was still covered in Anna's pussy juices, so lubrication was there."
        "He immediately started to thrust in and out of her anal hole. Ramming it."
        a "My ass... It's so big in my ass!!"
        play sound moaningfive
        show BarSexFive with Dissolve(1)
        "The penetration was ecstatic. The vigor was strong."
        "Pushing the limits of what it means to have anal sex with a big hard-on."
        "Ron could barely handle the pleasure coming from Anna's ass."
        scene 33-7 bar 145 with Dissolve(1)
        hide BarSexFive
        "Emily was in the same situation. But for her, it was even crazier."
        "She had never had such huge cock inside her anal cavity."
        e "AAHHHHH... I... Can't... So big..."
        "She was barely able to maintain her composure. almost on the edge of passing out from the sheer size and power of Leslie's dick."
        play sound jerk2
        scene 33-7 bar 146 with Dissolve(1)
        "Both of the girls were unable to talk or interact."
        "In their own minds... Enjoying all the pleasures..."
        "And so, too, were the guys."
        ro "This is the best night of my life... Fuck yeah!"
        le "I know... This is amazing."
        play sound moaningone
        scene 33-7 bar 147 with Dissolve(1)
        "Ron's dick was completely enveloped by Anna's hole."
        "It was sucking it in."
        "Not letting out any little part of it."
        play sound jerk
        scene 33-7 bar 148 with Dissolve(1)
        ro "AAh.. DAaang... TOO MUCH!!!"
        with flash
        ro "YEEAAAAH!!!"
        "Ron was exploding inside of Anna."
        with flash
        ro "MY COOOCK."
        a "Ahhh... Yeah..."
        ro "Take my seed, you slut!"
        with flash
        play sound jerk2
        scene 33-7 bar 149 with Dissolve(1)
        "Lumps of semen were coming out of Anna's ass."
        "Ron was entirely drained. His balls were empty..."
        ro "I'm fucked... I'm completely out..."
        "For the first time in a long while, Anna was feeling a bit different."
        scene 33-7 bar 150 with Dissolve(1)
        "Both Emily and Anna had been filled to the brim with sperm."
        "Now all that is left for them is to be used by the other clients and live their lives as nothing more."
        e "Anna... You dirty girl, that's a lot of cum. How can you handle that?"
        a "Oh... I have to ask you the same thing, Emily. I didn't know you had it in you."
        scene 33-7 bar 151 with Dissolve(1)
        "Emily was in no better situation. completely exhausted, filled with cum and naked in a bar full of strangers."
        "Almost the epitome of depravity for both of the girls present."
        e "Leslie. I have to say, you fuck me good."
        le "Girl... You are a different breed..."
        scene 33-7 bar 152 with Dissolve(1)
        j3 "Goddamn, The entire bar is looking at you."
        a "I... I don't know what overtook me..."
        e "Just being young, wild and free..."
        j3 "Crazy girls..."
        scene 33-7 bar 153 with Dissolve(1)
        a "I need a time out... We can go and get changed. I will show you where Emily."
        e "Yeah... I'm... Pretty drunk and exhausted. Lead the way."
        ro "Damn, I need a breather, too. I'm gonna take the next taxi home..."
        le "I think I'm about to puke from those drinks... Fuuck."
        play sound undress
        scene 33-7 bar 155 with Dissolve(1)
        "Emily quickly put on her dress. She had become a little embarrassed to be naked in front of all these strangers."
        ro "You girl is one hell of a slut. I'll tell you that."
        le "If you wanna, we could hang out more. Maybe try some drugs or something?"
        a "I don't know about that right now. I'm pretty tired to think about it..."
        e "I will get back to you on that one, Les..."
        "The girls didn't seem to want any further contact with them besides what they had tonight..."
        "Girls just wanna have fun..."
        scene 33-7 bar 156 with Dissolve(1)
        j3 "Well, you definitely brought a lot of attention and money to this bar tonight. Clients were coming up to the bar and ordering drinks and tipping for the show."
        a "I suppose that's good, right?"
        j3 "Oh, it's perfect. Patrick will be very satisfied."
        e "Will I get any of that?"
        j3 "Well, you'll have to ask Anna. What I can do, personally, is give you a bit of a discount."
        e "That will do, Jim. That will do."
        scene 33-7 bar 157 with Dissolve(1)
        e "Anyway, what did you think about tonight?"
        j3 "Other than that, I regret that I'm working and not able to join the fun. I loved the show. You two are wild."
        j3 "If things work out, we could get more work, like this, for you. If you want it."
        j3 "Well, that might be up to Patrick..."
        a "I guess..."
        "Anna was conflicted, but she enjoyed the ordeal a lot. Loved to be used as a toy for other's pleasure..."
        a "Ok, my shift is over, guys. See you later."
        j3 "I will show you where you can clean up, Emily."
        play music tense2
        play sound door2
        scene 33-7 bar 158 with Dissolve(1)
        "She exited the bar area and was going to the change room."
        "But he was already there. Waiting. Satisfied, happy..."
        pa "Well, well. You've outdone yourself this time."
        pa "I could hire you as a full-time slut. You brought in a lot of money tonight."
        play sound surprise
        scene 33-7 bar 159 with Dissolve(1)
        a "I didn't notice you."
        pa "Should be more aware of your surroundings. Wouldn't want anything to happen with my best income."
        a "Thanks..."
        pa "Anyway, you've been working pretty well tonight. I will count the cash and set aside your share."
        a "Thank you..."
        scene 33-7 bar 160 with Dissolve(1)
        pa "Anyway, you will get your regular salary for a night as well."
        a "How much of the tips will I get?"
        pa "Well, you know our system. You will get 50%% of the tips."
        pa "If you do good work, you will get paid well. Understand?"
        a "Yes..."
        pa "Now move along. I have things to do."
        play sound door2
        scene 33-7 bar 161 with Dissolve(1)
        "Anna entered the dressing room and thought about the events of the night."
        a "{i}...This was fun all around... But for some reason, I didn't cum... Why..."
        a "{i}...I loved that everyone saw me, and I was being used... And it felt so much more fascinating to be just a toy..."
        a "{i}...This is crazy. What am I thinking..."
        "Anna was starting to come to terms with her situation, and maybe it was better for her to just do what Patrick says."
        play sound undress
        scene 33-7 bar 162 with Dissolve(1)
        a "{i}...I just have to deal with it, I guess. If I put in good work, I will get good money..."
        a "{i}...And more of that feeling..."
        "She had changed and was ready to leave..."
        "The night's events had given Anna a lot of things to think about."
        $ bar_var_4 = True
        $ persistent.eighteenthScene = True
        $ renpy.end_replay()
    else:

        scene 33-7 bar 61 with Dissolve(1)
        ro "Hey, Jim. Who's that. Is it Anna?"
        j3 "Yeah. What do you want?"
        ro "We want to get fucked up so gives us your best!"
        ro "And then later... Maybe a bit of private time with Anna."
        j3 "She isn't a hooker or an escort."
        ro "We'll ask her about that."
        scene 33-7 bar 62 with Dissolve(1)
        le "Hello, Anna. Lookin' As hot as always."
        le "Wanna have fun?"
        a "I'm working, but we can arrange something, later..."
        ro "Now THAT's what I like to hear!"
        scene 33-7 bar 63 with Dissolve(1)
        "As soon as Anna went behind the bar, Jim leaned in."
        j3 "It's show time. Remember what I told you about doing what's necessary?"
        a "Yeah, I got this. Trust me, I'm motivated."
        j3 "Good to know."
        scene 33-7 bar 64 with Dissolve(1)
        a "Well, you're in luck tonight, boys. We've got a special evening tonight."
        ro "Fuck yeah! Bring it on."
        le "Yeeah. Let's get drunk."
        j3 "We've got some special drinks prepared for tonight."
        scene 33-7 bar 65 with Dissolve(1)
        le "Everything special we need is this hot bitch, Anna."
        "Anna didn't like hearing this but she was going with it."
        a "Hehe... You know it. Who knows where the night might go."
        le "Hopefully to all the 'wrong' places. Haha..."
        le "Now get us some drinks. I'm ready to get fucked uuuuppp!!!"
        play sound pourwater
        scene 33-7 bar 66 with Dissolve(1)
        j3 "Our finest whiskey, bourbon coming right up."
        j3 "These are on the house. Considering that you've been such good clients of ours."
        ro "Now, this is what I call bottle service."
        a "This night is all about you. And I mean everything."
        ro "You never cease to amaze."
        scene 33-7 bar 67 with Dissolve(1)
        ro "But goddamn, can't take my eyes off of you, girl."
        ro "Tell me that you are a part of tonight's fun?"
        a "Let's see where it goes, huh?"
        ro "Alriiight."
        scene 33-7 bar 68 with Dissolve(1)
        ro "Bottoms up."
        "Leslie didn't hesitate and took shots like he was bulletproof."
        "Immediately regretted taking it so fast."
        j3 "Drink up, my friends. This is going to be a fun night."
        scene 33-7 bar 69 with Dissolve(1)
        le "That is some good whiskey, not gonna lie."
        j3 "Only the top shelf for you guys."
        ro "Alcohol is all the same to me. All the same, all I care about is getting fucked up!"
        ro "And getting rowdy. Let me tell you. We are in some good stuff right now."
        ro "Extorted some businesses, but since you guys are the cool ones, we won't do it here."
        scene 33-7 bar 70 with Dissolve(1)
        j3 "That's good to hear. how about some cocktails, huh?"
        ro "You read my mind."
        j3 "I call this cocktail the: 'The Ex-Wife'"
        ro "That sounds like one hell of a drink."
        ro "Sign me up for two! Haha!"
        "Both men, especially Ron, were getting pretty noisy."
        scene 33-7 bar 71 with Dissolve(1)
        j3 "I hope you are ready for this one."
        ro "Damn right I am."
        "Jim started mixing the cocktails for both 'gentlemen'"
        le "Alright, I'm feeling good and want to dance with some hot bitches."
        ro "You and me both, but first we gotta get hammered, then we find some whores to fuck."
        scene 33-7 bar 72 with Dissolve(1)
        j3 "Here are the cocktails. Enjoy them. That will be 300$ each. But you will get a bonus with it. If you know what I mean?"
        ro "What? That's more expensive than previously!"
        ro "I feel like it's too expensive..."
        le "Yeah. I feel like you have to convince us."
        play sound surprise
        scene 33-7 bar 73-1 with Dissolve(1)
        "Anna hopped on the bar and approached Ron."
        a "Oh come on, if you buy them, I will let you take remove something from my outfit."
        ro "You are absolutely wild tonight. I like that!"
        ro "Well, in that case, I'm fucking in!"
        scene 33-7 bar 74-1 with Dissolve(1)
        "Both of the men started to chug the cocktails. The drinks were interesting in taste but gave a good kick."
        a "Yeah, just like that. Drink up. I want you to drink it all up for me."
        "Jim was enjoying the view too. Just gazing as Anna worked her magic on those two idiots."
        j3 "{i}...Damn, she's hot as fuck... Maybe when all of this is over, I could get with her..."
        scene 33-7 bar 75 with Dissolve(1)
        ro "That was... Too... Easy... Agh..."
        le "You think? I'm barely able to hold it. That drink was so fucking hardcore..."
        ro "You're just a pussy, Leslie!"
        le "Am not. Anyway, how about you keep up with your part of the deal. We finished our drink, no problem."
        a "Fine, fine. you win..."
        scene 33-7 bar 76 with Dissolve(1)
        le "Your titties are so nice. And big, and round."
        a "Thank you... Don't be shy. Take off the covers."
        "Anna knew what was at stake, so she rolled with it."
        le "I wouldn't have it any other way."
        "The sexual tension was rising in the bar area."
        "Some of the patrons were looking on and enjoying the view."
        scene 33-7 bar 77 with Dissolve(1)
        "Both of them started touching Anna's tits. enjoying the feel. groping her."
        a "Ah..."
        "She was a little bit stimulated. the entire vibe was so experimental."
        ro "Yeah, you like that, don't you..."
        le "Of course she does. Just look at her face."
        play sound undress
        scene 33-7 bar 78 with Dissolve(1)
        ro "And they are off. Damn girl..."
        "They had unraveled the nipple covers and saw Anna's beautiful breasts unleash their full potential."
        le "They are so fucking good. I wanna just drown in those boobs."
        ro "Wait your turn, Les."
        scene 33-7 bar 79 with Dissolve(1)
        "The couple looked from afar and enjoyed the show."
        pa1 "Those lucky bastards, eh?"
        pa2 "Don't worry, we will have our turn at some point."
        pa2 "For now, let's just enjoy the show, honey."
        pa1 "She is so beautiful. I want you to ram that cock into her pussy and then mine."
        pa2 "You and me both. That would be so hot."
        pa2 "But I also have this idea. Maybe we should also do the opposite. Two cocks penetrating you?"
        pa1 "Oh, husband. You know how to trigger my weaknesses..."
        play music activesong
        scene 33-7 bar 80-1 with Dissolve(1)
        "Emily had returned from smoking and was met with an amazing sight."
        e "{i}...My girl seems to be having a lot of fun without me..."
        e "I should help her a bit, loosen her up."
        e "Damn, I want a drink. Who's ready for shots?!"
        scene 33-7 bar 81-1 with Dissolve(1)
        e "Anna, what are you doing? Haha?"
        a "Oh, just entertaining the guests. And also enjoying myself."
        a "Where did David go?"
        e "He had to leave. Looks like I will have to find some other company for tonight."
        a "You wanna join?"
        e "Oh, you take the spotlight this time, honey."
        scene 33-7 bar 82 with Dissolve(1)
        "Jim had prepared the next set of cocktails for the two idiots."
        j3 "Here, more drinks for you, and if you chug those, this might all go even further."
        le "Damn, I don't know, kind of dizzy right now."
        ro "I told you guys, he's a pussy."
        le "Bro, I just don't wanna pass out before the real fun begins."
        scene 33-7 bar 83-1 with Dissolve(1)
        a "If you guys drink these, I will go further..."
        a "Show you a bit more of what I have to offer."
        ro "See, Leslie? We can't say no to a woman."
        le "Fuck. I got no choice in this one, hehe..."
        scene 33-7 bar 84-1 with Dissolve(1)
        a "Emily, you will have to join me."
        e "Oh? What do you have in mind?"
        a "I won't tell you just yet, first they chug. Then we improvise."
        e "I couldn't say no to you, Anna..."
        a "I know, hun. And you love it."
        scene 33-7 bar 85 with Dissolve(1)
        "Both men took the drinks and started to chug them in a fast manner."
        a "That's right. Keep doing that, and you will get me all in no time."
        le "Bottoms up... Fuuuck... I'm going to be trashed after this."
        ro "Maybe you, then I will have Anna all to myself. Fuck yeah."
        scene 33-7 bar 86 with Dissolve(1)
        "Without any hesitation, both gullible schmuks swallowed the entire drink in seconds."
        "Even if it meant them passing out, they knew they had to try and get that piece of ass, Anna."
        a "Damn, you boys are very, very rigorous drinkers."
        ro "What can I say. I'm a fucking BEAST! Now, show us what you got, slut."
        le "Yeah, we want more. Come on."
        scene 33-7 bar 87 with Dissolve(1)
        "Anna leaned down and arched her back. Taking up an inviting pose."
        a "Emily, sweety, would you help me with these panties?"
        e "Oh. Hehe... Would I. Come here, let me help you."
        ro "WHAAAT? Double girl action? Am I dreaming? Am I in heaven?"
        scene 33-7 bar 88 with Dissolve(1)
        "Emily approached Anna and caressed her a bit before starting to slowly slide off the panties."
        ro "Daamn. This is better than I could've ever imagined."
        le "Broo. These chicks are crazy. I love it."
        ro "If only I could get this kind of service every time I came here."
        play sound undress
        scene 33-7 bar 89-1 with Dissolve(1)
        a "Thank you, Emily. Now I will ask you to join me on this bar."
        e "Anna, this is crazy. Haha... Even I don't think I have it in me."
        a "Trust me, babe, you do. I will ask Jim to prepare a shot for us."
        e "I don't know..."
        scene 33-7 bar 90-1 with Dissolve(1)
        a "It's all or nothing. You just have to get up here."
        "Trust me, it's going to be fun."
        e "You naughty, naughty girl..."
        e "Ok, Fuck it. Let's do this."
        play sound undress
        scene 33-7 bar 91-1 with Dissolve(1)
        "Anna reached out with her hand. Emily was still a bit hesitant. She was just not drunk enough to reach her peak sluttiness."
        e "This is crazyyy."
        a "You know it, girl. And you love it."
        ro "This is fucking amazing. I'm going to fuck you both so hard you will pass out from pleasure."
        scene 33-7 bar 92-1 with Dissolve(1)
        e "Well, here I am. On the bar. Fuuck."
        e "I need that shot, Anna. Can you hook me up?"
        a "Of course. Come here. This is our strongest liquor."
        a "Are you ready for this?"
        play sound drinkingBeverage
        scene 33-7 bar 96-1 with Dissolve(1)
        "They both took the shot glasses and emptied them."
        "Emily was a bit drunk, but the cigarette coupled with the shot made her excited."
        e "Ah. This is stroong..."
        ro "Yeaah. That's what I like to see. Chicks enjoying themselves."
        le "Ron, stop with the... {b}*Gulp*{/b}... overacting, man."
        scene 33-7 bar 96 with Dissolve(1)
        a "Now on to some more interesting things, eh Emily?"
        e "What do you have in mind, you sexy girl."
        a "Whatever we want. Let's have it."
        ro "YEEAHHH. Let's goooo!"
        scene 33-7 bar 97 with Dissolve(1)
        a "Oh, Emily. We are barely drunk, and you are already enjoying me?"
        a "What's gotten into you?"
        e "I'm always like this, just need a little push..."
        ro "Come on then, show us your kinky side, girl. I can't wait to see."
        scene 33-7 bar 97-1 with Dissolve(1)
        "Anna started to slowly undress her friend's cleavage."
        "The titties were just waiting for an opportunity to be unleashed. No bra, nothing else to hide them if they were to come out."
        a "Oh, what do we have here. Some fun stuff, eh?"
        e "You know me, Anna. Always ready for a party. The less I wear, the easier it is..."
        scene 33-7 bar 98 with Dissolve(1)
        "From afar, some patrons were looking on and checking out the scene that was unfolding."
        "Both girls were getting pretty riled up, hot and naughty."
        stranger "Damn. I would like to include myself in that. Seems like an open event."
        stranger "Maybe I can get some touchy time..."
        play sound lighthit
        scene 33-7 bar 99 with Dissolve(1)
        "Emily pushed Anna down against the bar with a bit of power."
        a "Oh, Emily. What's gotten into you? You seem to be taking my power over, now."
        e "Girls just want to have fun, so here I am, taking what I want."
        a "Naughty, naughty girl. Come here..."
        scene 33-7 bar 100 with Dissolve(1)
        e "I'm going to enjoy you more than anyone ever has."
        e "You know I have a way with my hands and my mouth... And my pussy."
        e "I just know how to take you for all your worth."
        a "Fuck. Emily, give it to me."
        "Anna was getting wet and ready to be enjoyed."
        scene 33-7 bar 101 with Dissolve(1)
        "She pushed herself onto Anna, and their chests touched."
        a "Ah... You sexy beast..."
        ro "Yeeaaah... Let's gooo!"
        le "This is the best shit I've ever seen."
        play sound jerk
        scene 33-7 bar 102 with Dissolve(1)
        "Immediately, they started kissing each other passionately."
        "The drinks were strong and had finally worked their magic."
        "Anna was overtaken by sensation. Being seen by strangers, kissing with Emily."
        "She was on fire, she wanted more... And so did Emily..."
        scene 33-7 bar 103 with Dissolve(1)
        ro "Yeah. Give it to her. Show us what you got."
        "Meanwhile, Leslie started caressing Emily's leg. She didn't even feel it at first."
        le "You girls are so hot, I want to see more..."
        "Emily's legs were so soft and warm."
        le "{i}...Damn, what a fine woman... I want to penetrate her so bad..."
        scene 33-7 bar 104 with Dissolve(1)
        "Leslie's hand was going higher, towards her asscrack. Towards her panties."
        le "Let me just enjoy a little bit of this sexy piece of ass."
        ro "What you trying to do, Les? You dirty dog, haha..."
        le "Oh, just helping girls get rid of things that are in their way."
        ro "Such a gentleman..."
        scene 33-7 bar 105 with Dissolve(1)
        e "What are you doing there, you naughty boy?"
        le "Well, since Anna doesn't have panties, I'm just helping you with that."
        e "I guess we'll be matching, hehe..."
        le "That was the idea, yeah. You are both so sexy. I just can't wait to see more. This is amazing..."
        play sound undress
        scene 33-7 bar 106 with Dissolve(1)
        "Leslie slowly slid her panties down her thighs."
        "Emily felt small spasms through her body, as she felt that her and Anna's pussies were touching."
        a "Oh, you like that, don't you. I can feel it."
        e "You just shush and let me make YOU feel good."
        play sound jerk2
        scene 33-7 bar 107 with Dissolve(1)
        "Before Emily could do anything, Les slid his finger into her pussy ever so slightly."
        "Just enough to make her crave a cock. Just enough to open her, already wet, pussy walls."
        "Prepare them for penetration, for fucking..."
        e "Ah... I see your friend is enjoying me, too."
        a "I wouldn't have it any other way."
        scene 33-7 bar 108 with Dissolve(1)
        e "Well, I'm not going to let anyone have the upper hand on me this time..."
        e "How about you sit back and relax. I will just let you feel something that you absolutely love."
        a "And what would that be?"
        e "You will see..."
        play sound jerk
        scene 33-7 bar 108-1 with Dissolve(1)
        "Emily moved down to Anna's pussy hole. And started to lick it lightly. Just enough to stimulate Anna."
        a "Aah... I like... It..."
        "She was already feeling sensations. Emily always knew how to trigger her."
        j3 "{i}...Things are getting crazy here. Patron's are starting to look..."
        j3 "{i}...I hope it doesn't get out of hand..."
        play sound jerk3
        scene 33-7 bar 108-2 with Dissolve(1)
        "Anna looked down to Emily, and the sight made her get even steamier."
        "She was starting to sweat from the entire ordeal. People were watching. Emily was licking her pussy with such success."
        a "Ahh... Damn, Emily, you are very good... Oh..."
        e "Mhm... Mmm..."
        "Emily was enjoying this as much as Anna. She loved the taste of Anna's sweet, sweet pussy."
        "And the view of Anna's pleasured face was just as sexy..."
        play sound jerk2
        scene 33-7 bar 108-3 with Dissolve(1)
        a "Ahh... That's right. Just like that!"
        "Everyone was enjoying the sexual intercourse that was unfolding on the bar surface."
        "What seemed to be a regular Friday night had slowly started to turn into a sex-crazed depravity."
        "Onlookers were fantasizing about boning Anna or licking her up and down, or her sucking their dicks."
        scene 33-7 bar 109 with Dissolve(1)
        "Emily hastily changed her position so that their wet pussies would align."
        e "I want my pussy to feel your pussy, girl. Fuck!"
        a "Ahh... You are a fucking animal, Emily. I want you to take me..."
        ro "Damn, you girls are fucking crazy. I LOVE IT!"
        le "YEAH. Give it to her, Emily."
        play sound moaningfour
        scene 33-7 bar 110 with Dissolve(1)
        "Both men started to touch the girls. Feeling their luscious breasts swing in the air."
        "Emily was moving perfectly against Anna's lips. Rubbing each other and feeling the ecstasy building."
        "The air in the building was becoming hot and sweaty from the dancing, drinking, and well... The perverted sex that was going on."
        e "Aahh... Yeah. That's right..."
        a "Emily... AAhh... I'm so horny..."
        scene 33-7 bar 111 with Dissolve(1)
        pa1 "They are taking it further and further. Holy shit..."
        pa1 "They are actually scissoring already... That is so hot... I never believed I would see this happen in this bar."
        pa1 "It's so hot. I'm getting pretty fucking wet."
        pa2 "Yeah, it's a sight behold. I'm pretty hard myself, right now."
        play sound moaningfive
        scene 33-7 bar 112 with Dissolve(1)
        pa2 "If you want, you could go and join them..."
        pa1 "Even if we are exploring our sexualities... I don't think that I'm ready for that yet."
        pa1 "But I'm still so hella horny..."
        pa2 "Perhaps we should go home and do it?"
        pa1 "No, let's not wait, I want you to take me right now, in the bar toilets... Please... Ah..."
        pa2 "Ask no more..."
        scene 33-7 bar 113 with Dissolve(1)
        "Anna's back was arching in pleasure. She was in a world of satisfaction right now."
        "She was being stimulated by Emily and some strangers touching her tits."
        "She was getting more turned on with every second."
        "Being at their mercy. Being touched everywhere, scandalous, really."
        "People all around the bar were watching. Some left, some enjoyed the show."
        scene 33-7 bar 115 with Dissolve(1)
        "Out of nowhere, Ron pulled out his hard cock, and it immediately caught Anna's attention."
        a "What do we have here, huh?"
        ro "Oh, just a fun little experience."
        scene 33-7 bar 115-1 with Dissolve(1)
        "Anna realized that this was a good time to move on with the plan."
        a "I think this is a bit too wild."
        ro "You don't want my cock?"
        a "I... I do, but maybe somewhere a bit more private?"
        ro "I like the sound of that."
        play sound undress
        scene 33-7 bar 115-2 with Dissolve(1)
        e "What do you have in mind, Anna?"
        a "Don't worry about it. Just follow my lead and play along."
        e "Uu... Mysterious, I like that."
        a "I will owe you one for this, sweety."
        e "I will remeber that, hehe..."
        play sound door2
        play music blues
        scene 33-7 bar 163 with Dissolve(1)
        "All of the perverts went into the toilet expecting something big, but Anna was committed to her goal."
        a "Soo, I was wondering if you could do something for me, guys..."
        ro "Anything to get some of that pussy, girl..."
        a "Well, there is this thing I want you to do... It's..."
        le "Come on, come on. Tell us."
        a "Could you go into my boss Patrick's office and take something from his safe?"
        play sound surprise
        ro "Oh shiiit. That's pretty serious. I mean. I do plenty of bad work, but..."
        play sound surprise
        scene 33-7 bar 164 with Dissolve(1)
        a "It would mean a lot to me..."
        a "There is some money in it for you as well as something special from me if you do it..."
        ro "Fuck. You are one crazy girl..."
        ro "I don't know what to say, the money is nice, and a night with you would be fucking amazing..."
        scene 33-7 bar 165 with Dissolve(1)
        a "I really need your help on this one, Ron. Sweety."
        a "It would mean the world to me if you did this..."
        ro "I... I want you..."
        a "If you do it, I will give you all you want."
        a "I will let you ravage me like a savage. Do anything you want to me..."
        a "Ahh... I'm getting wet even thinking about it..."
        scene 33-7 bar 166 with Dissolve(1)
        le "Wait, wait. This is not a good idea."
        le "You are not seriously considering it, are you, Ron?"
        ro "Shut up, I'm thinking..."
        "Emily didn't exactly know what to do, but Anna had asked her to play along."
        play audio surprise
        play sound undress
        scene 33-7 bar 167 with Dissolve(1)
        e "Oh, Leslie. If you do this, you can have all of me... My body, my tits, and ass would be yours."
        le "Holy shit... You girls are fucking crazy..."
        e "I'm even crazier about you... I want your hard cock to penetrate me. But you have to help my friend Anna."
        le "Fuck..."
        le "{i}...What do I do, what do I do..."
        "Both men were completely enchanted by the girls..."
        scene 33-7 bar 168 with Dissolve(1)
        ro "You bitches are crazy. This is so hot..."
        ro "I want to destroy your pussy, Anna..."
        ro "Destroy it with my hard cock."
        a "You can have it all if you do it..."
        a "Won't you help two ladies in need?"
        scene 33-7 bar 169 with Dissolve(1)
        le "Dude. I... I don't know what to think. They are two smoking hot bitches. I wanna fuck them so bad."
        le "But, I don't think it's a good idea..."
        ro "Shut up, dude. We do this daily. You ain't a pussy, are you?"
        ro "Plus, we will get our money back. Those drinks were bloody expensive."
        ro "We gotta help these girls. They need it."
        le "Ahh. Shieeet..."
        scene 33-7 bar 170 with Dissolve(1)
        ro "Fine. We'll do it."
        a "Oh, Ron. You are such a good guy."
        le "Fuuuck. This is nooot... I... Fuck it."
        a "You will get all of this when you do what I need."
        a "There are some things in the fire hydrant box if it turns out you need them."
        play sound door2
        scene 33-7 bar 171 with Dissolve(1)
        le "Dude, what the fuck are we doing?"
        ro "Bro, chill, it's gonna be fine. I'm drunk, I don't care, and there are bitches waiting for us."
        le "Ahh... This is crazy."
        ro "It's simple, we go in, grab what we need, and get out. simple."
        play sound surprise
        scene 33-7 bar 172 with Dissolve(1)
        le "What the fuuuck. That's a gun. Fuck. This is too crazy..."
        ro "Shut up, and don't be a little bitch. We've come this far. Let's do this."
        le "I have a bad feeling about this..."
        ro "Dude, we've done this before, we got this."
        "The two idiots were so taken by the girls, they would do anything."
        "Smoothly done by Anna..."
        play sound undress
        scene 33-7 bar 172-1 with Dissolve(1)
        "They put on the masks and prepared."
        le "I can't see shit in this thing."
        ro "I'm so fucking drunk I can't understand shit."
        ro "Let's just go in and do our thing, man."
        ro "It's easy. Done it a million times."
        play music tense2
        scene 33-7 bar 173 with Dissolve(1)
        "Both men had committed fully. Not knowing what to expect."
        "Both drunk enough to care little about the situation."
        "Only driven by their lust for the girls..."
        ro "Alright, in here."
        le "I'm behind you."
        play sound surprise
        scene 33-7 bar 174 with Dissolve(1)
        pa "Hey, Who are you?"
        pa "And what the fuck are you doing in my office?"
        ro "Shut up, you old fool, or I will pop your cork."
        le "Ye. Sit silent, asshole."
        scene 33-7 bar 175 with Dissolve(1)
        ro "Now that we are acquainted, you will show me the safe."
        pa "What safe? I don't know what you are talking about, you idiots."
        pa "Do you know how much trouble you are going to get in now?"
        pa "You won't see the light of the day anymore, you fucks."
        scene 33-7 bar 176 with Dissolve(1)
        le "That's the safe, and it's open. We should grab everything."
        ro "Good idea. And you, motherfuck, stay still. One wrong move and I will fill you with lead."
        ro "You are the idiot if you left the safe open for us. Haha..."
        ro "This is way too easy."
        scene 33-7 bar 177 with Dissolve(1)
        le "Don't move, bitch."
        le "We will take all the money. Just for fun."
        ro "Hurry up, Les. Don't bitch around."
        le "Fine, fine."
        play music tense
        scene 33-7 bar 178 with Dissolve(1)
        "Meanwhile, Patrick had been slowly opening the cupboard and pulling out his own gun."
        "Waiting for the best moment to reveal it."
        pa "You've got to be the dumbest criminals ever. Do you even know who you're messing with?"
        ro "Shut your damn mouth, fool. Before I bust a cap in your face!"
        play sound surprise2
        scene 33-7 bar 179 with Dissolve(1)
        pa "Oh, I don't think so, you fucks!"
        pa "Stay right there... Les."
        pa "You are going to stay there. While I call my guard, and we call the cops on you."
        le "Don't... Don't shoot!"
        pa "Shut your mouth bitch ass, I will let my mobsters do it."
        play sound surprise2
        scene 33-7 bar 180 with Dissolve(1)
        ro "You are bluffing. You ain't got no mobsters. You are just a lil bitch who happens to own a bar."
        pa "HAHAHA... You are the dumbest piece of shit I've ever seen."
        pa "Shut up before I shoot you both for attempted robbery!"
        ro "I will shoot you before you can do anything!"
        scene 33-7 bar 181 with Dissolve(1)
        pa "Try me. You FUCK!"
        "While Patrick and Ron were arguing, Leslie was leaning in to try and take away the gun from Patrick."
        "But..."
        play sound gunsound1
        scene 33-7 bar 182 with vpunch
        with flash
        play sound gunsound2
        "BOOM."
        play sound gunsound1
        "Patrick fired his weapon the moment he noticed what Leslie was trying to do."
        "The bullet went through his chest."
        "And Leslie was falling down."
        play sound lighthit
        scene 33-7 bar 183 with Dissolve(1)
        pa "Your turn, scum!"
        ro "NO! LES!"
        ro "Motherfucker I will kill you and bury you with the roaches."
        play sound gunsound1
        ro "AAAHHHHHHH."
        scene 33-7 bar 184 with flash
        play sound gunsound2
        with vpunch
        "BOOM."
        play sound gunsound2
        with flash
        "BOOM."
        play sound gunsound1
        with flash
        "Ron fired multiple shots at Patrick, with hatred in his eyes."
        "Leslie was bleeding out on the floor, but Patrick was shot dead immediately."
        scene 33-7 bar 185 with Dissolve(1)
        ro "MOTHERFUUCKEERRR!!! FUUUCK"
        ro "THIS IS FUUUUCKED!"
        "Ron was in a state of confusion and rage. He didn't know what to do."
        ro "What to do? What to do? LESLIE!"
        scene 33-7 bar 186 with Dissolve(1)
        "Ron checked on Leslie... He wasn't responding."
        ro "Les. Fuck. This is fucked up... Nooooo."
        "Ron was distressed about his friend Leslie."
        "He didn't know what to do, so he just thought about what he does best..."
        scene 33-7 bar 187 with Dissolve(1)
        "Stealing."
        "He looked at the safe..."
        ro "I will just take whatever is in there. I know Leslie wouldn't want me to waste it and leave it."
        ro "This is all their fault. THOSE BITCHES! FUUCK."
        with vpunch
        ro "I will kill them!!!"
        scene 33-7 bar 188 with Dissolve(1)
        "He approached the opened safe. Feeling sick, twisted, scared, and full of rage."
        "The entire room was just dead quiet, besides the muffled noises from the bar."
        "Ron was going to take the money and then avenge his fallen friend."
        ro "Money! Money! I will take it all, and then I will shoot them. I will avenge you, LES!"
        scene 33-7 bar 189 with Dissolve(1)
        "Gabe had heard the shots and immediately ran to his locker for the gun."
        "He was too late... Noticed the terrible sight in front of him."
        ga "Stop right there, asshole. Don't move. If you do, you're dead."
        "Gabe was ready to fire any moment..."
        scene 33-7 bar 190 with Dissolve(1)
        ro "Oh, you think you could kill me? Haha...."
        ro "HAHAHA... I'm invincible. I've killed plenty of people!!"
        ro "I don't care if I live or die. HAHA... You won't see another day."
        "Ron was losing it. Becoming enveloped by a deep state of confusion. Add to that the fact that he was very drunk..."
        "And you had a completely unreasonable person on your hands."
        scene 33-7 bar 191 with Dissolve(1)
        ro "Hyaaaa!!!!!"
        "Ron turned around and tried to fire off his weapon, but Gabe was prepared."
        "Everything was happening in a split second."
        play sound gunsound2
        scene 33-7 bar 192 with flash
        play sound gunsound1
        with vpunch
        "BOOM!"
        play sound gunsound1
        with flash
        "POW!!"
        play sound gunsound2
        with flash
        play sound gunsound2
        "Gabe fired multiple shots at Ron. Enough bullets penetrated Ron."
        ro "AAAHHH... FUCK YOOOUUU."
        "Ron screamed out in last act of defiance before his ultimate demise."
        play sound lighthit
        scene 33-7 bar 193 with Dissolve(1)
        "Lifeless Ron hit the ground in seconds."
        "Gabe was overtaken by a dreading feeling. He had just killed a man."
        "No training prepared him for this. For feeling how feels now..."
        ga "Fuck, fuck... Patrick... Dead..."
        play sound surprise2
        scene 33-7 bar 194 with Dissolve(1)
        "All three of the masterminds were talking, chilling. Acting like they didn't know."
        "The truth is that non of them knew exactly what was going on, least of all Emily."
        a "What was that? Sounded like..."
        e "Like gunshots. What the fuck?"
        e "Is this to do with, Ummm..."
        scene 33-7 bar 195 with Dissolve(1)
        j3 "I have no idea what you are talking about."
        a "Yeah, we don't know anything, and neither do you, Emily."
        e "Right...I hope this doesn't turn back on us..."
        "All of them were a bit nervous as to what had happened, but none of them wanted to go investigate."
        play sound surprise
        play sound door2
        scene 33-7 bar 196 with Dissolve(1)
        cop1 "I got a call about two very intoxicated and inappropriate men?"
        j3 "Umm, Yeah. that was me. I think something bad has happened."
        j3 "The two men were here and then they weren't."
        cop1 "Explain the situa..."
        play sound gunsound1
        scene 33-7 bar 198 with vpunch
        play sound gunsound2
        "They all heard a couple more gunshots."
        cop1 "Shit. That sounded like weapon fire."
        a "Please do something!"
        "The cop didn't waste any time and ran straight into the danger."
        play sound surprise2
        scene 33-7 bar 199 with Dissolve(1)
        cop1 "FREEZE. DO NOT MOVE!"
        cop1 "DROP THE GUN AND PUT YOUR HANDS BEHIND YOUR BACK."
        ga "Yeah. I'm complying, sir. Don't shoot. I didn't do this. I'm a guard in this bar."
        cop1 "We will verify that later. Now put your hands behind your back and do not move."
        ga "Yes, sir."
        scene 33-7 bar 200 with Dissolve(1)
        "Gabe knew that he shouldn't do anything stupid."
        "But he has very distressed..."
        cop1 "I will take you to the police station, and then we will see."
        ga "I understand."
        cop1 "You have the right to remain silent. Anything you say can and will be used against you in a court of law."
        cop1 "You have the right to an attorney. If you cannot afford an attorney, one will be provided for you by the state."
        scene 33-7 bar 201 with Dissolve(1)
        cop1 "Shit... Three people are dead. What the hell happened here..."
        ga "I came in here after I heard gunfire, and I saw my boss, in the chair, dead."
        ga "And... And one of the guys is dead. The guy in the white shirt tried to steal stuff, and as soon as he noticed me..."
        ga "He tried to shoot at me. I got the shot off first."
        cop1 "We will verify this and everything else back and the police station, with camera footage that will be provided."
        play sound door2
        scene 33-7 bar 202 with Dissolve(1)
        a "What happened in there?"
        cop1 "I'm not at liberty to provide any details as of now. More officers will arrive at the scene in a moment."
        cop1 "DO NOT enter the area. It's cordoned off."
        cop1 "Is that clear?"
        scene 33-7 bar 203 with Dissolve(1)
        j3 "Yes, officer. I will oversee all the papers and footage and all the guests that had arrived tonight..."
        cop1 "Your cooperation will be appreciated a lot."
        cop1 "Now, stay here. When officers arrive, give your testimony and head home, nowhere else."
        cop1 "Understood?"
        scene 33-7 bar 204 with Dissolve(1)
        a "Yes, officer."
        cop1 "Why are you here, Anna? This is highly suspicious."
        a "Umm. I just work here..."
        "She could feel the pressure from Desmond's question and his suspicion."
        e "What are you talking about?"
        cop1 "That is non of your concern, miss."
        play sound door2
        scene black with Dissolve(2)
        "After some time, additional officers arrived on the scene."
        scene 33-7 bar 210 with Dissolve(1)
        "Officer Bella had arrived on the scene, and additional policemen had gone to examine the room."
        b2 "Hello. I would just like to ask you a few questions, is that ok?"
        a "Yeah, sure..."
        b2 "Where were you during the shooting?"
        a "Both of us were here."
        b2 "Did you notice anything suspicious regarding the men?"
        a "They were just aggressive and shouted, but that was not unusual."
        b2 "Do you have any personal connection to these men?"
        a "We do not. I've only seen them as clients here."
        scene 33-7 bar 211 with Dissolve(1)
        b2 "Hmm. I see. Well, I will take the rest of the questions to the bartender."
        a "Yeah. I'm sorry I couldn't help more."
        b2 "It's ok. It's good that no one else was shot."
        a "Yeah. Are we free to go?"
        b2 "Yes, I have your information. If we have any additional questions, we will contact you."
        b2 "It's just strange that you're also involved in this, Anna."
        play sound surprise
        a "You know my name?"
        b2 "I've read through the file. Just be careful."
        scene black with Dissolve(2)
        "Anna went to change and left the bar."
        $ bar_var_4 = True
    jump PreAshleyEventOne
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
