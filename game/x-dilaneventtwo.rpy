label DilanEventTwo:
    play music tranquility fadein 0.5
    play sound carsound
    scene black with Dissolve(2)
    scene 32-10 dilan 1 with Dissolve(1)
    a "{i}...Oh... Dilan's with someone..."
    play sound surprise
    a "{i}...Wait... That's Rebecca? What?..."
    "Anna was surprised as to who she saw here."
    a "{i}...Well, that wasn't completely unexpected..."
    scene 32-10 dilan 2 with Dissolve(1)
    a "{i}...You naughty girl... Hehe..."
    "Both Dilan and Rebecca seemed to be very enjoying the shoot."
    d3 "Perfect shots, you are stunning, Rebecca!"
    r1 "Let me pose like this and take another one."
    d3 "Absolutely, anything you wish, dear."
    play sound surprise
    scene 32-10 dilan 3 with Dissolve(1)
    d3 "Oh, Anna. You're here? What's the time?"
    a "It's middle of the day right now."
    d3 "It seems that I've carried away, hehe..."
    r1 "If I was you, I would get carried away as well..."
    a "What are you even doing here?"
    scene 32-10 dilan 4 with Dissolve(1)
    r1 "I just need some pictures from Dilan, that's all."
    r1 "Wait, what are YOU doing here?"
    a "I... Um... Have some business with Dilan."
    r1 "Right. You don't have to tell me if you don't want to."
    scene 32-10 dilan 5 with Dissolve(1)
    menu:
        "Tell Rebecca about the porn shoot.":
            a "Well, I... I'm going to be participating in a 'video'."
            $ relationship_func("Rebecca will remember that.")
            play sound surprise
            r1 "What? Wow... Now I'm surprised."
            r1 "Where is this coming from?"
            a "Well. Dilan provided the opportunity and I need the money right now."
            r1 "Ah... Right..."
            $ rebecca_pornshoot_question = True
        "Don't Tell Rebecca.":
            a "I will tell you some other time, perhaps."
            a "Just some photoshoot business..."
            r1 "Ok..."
    play sound undress
    scene 32-10 dilan 6 with Dissolve(1)
    d3 "Anyway, We are done here. I have all the shots we needed."
    r1 "Sure, hon. In that case I will get changed."
    r1 "By what time could the pictures be ready?"
    d3 "Well, I'm rather busy during the next couple of days but I will have them ready by the beginning of next week."
    r1 "Sounds great!"
    scene 32-10 dilan 7 with Dissolve(1)
    d3 "Sorry, Anna. I got a bit carried away."
    a "It's totally fine, Dilan. We all have work to do."
    d3 "Anyway, Are we still on? You haven't changed your mind yet, have you?"
    menu:
        "Anna agrees to continue.":
            a "I'm good, we can get ready for the shoot."
            pass
        "Anna changes her mind.":
            a "I've had some time to think about it and I don't want to participate in that."
            a "It's a bit too much. Even if the money's good."
            play sound surprise2
            d3 "Oh... Well... It's not very good to bail at the last moment."
            d3 "I'm disappointed..."
            d3 "But in any case, I have someone else in mind luckily."
            a "Sorry, Dilan, but I cannot do it."
            d3 "But would you still be willing to do some more 'softcore' content in the future?"
            a "Perhaps, I will have to think about. You can contact me with any idea's you have."
            d3 "You've kind of limited me. But I will think of something. Because you're still perfect for a lot of content."
            $ DilanPornShootQuestDone = True
            $ DayFourCompletion +=1
            if timothySexContent == True:
                jump TimothyHomeEventOne
            else:
                jump JeremyHomeEventOne
            return
    scene 32-10 dilan 8 with Dissolve(1)
    d3 "That's great, I will wrap up here with Rebecca and then we can get going."
    d3 "I would also like to mention that we have a skeleton crew."
    d3 "Only I will be filming, I've set up the place, the lights, and other cameras."
    a "Oh, really? That already makes me more comfortable. Thank you, Dilan."
    scene black with Dissolve(1)
    play sound undress
    scene 32-10 dilan 9 with Dissolve(1)
    r1 "Alright, I'm done here so I will get going, someone has to actually work."
    r1 "And not have fun all the time... Haha."
    a "I think I do more work in a day than you do in a week. Hah."
    r1 "Probably true."
    if rebecca_pornshoot_question == False:
        r1 "Good luck on what ever you are going to do."
    else:
        r1 "Good luck in your shoot. I'm still surprised, but you do you. Not that I'm judging, hehe..."
    scene 32-10 dilan 10 with Dissolve(1)
    r1 "By the way, I want to discuss some stuff with you when you're free."
    r1 "Some 'fun' stuff..."
    a "Now I'm intrigued, I will go to your place when I have the time."
    r1 "I would be happy."
    r1 "Have fun and don't make uncle Dilan sad."
    play sound door2
    scene 32-10 dilan 11 with Dissolve(1)
    a "Sorry about that. She's very... creative... in ways of how to embarrass me. Haha."
    d3 "Don't mind me, You have a very beautiful and friendly sister. It's a privilege working with you both."
    a "Hah... Well, she truly is. Has always cared for those close to her."
    d3 "That is very honorable, Anna. Alright, let's get to work?"
    scene 32-10 dilan 12 with Dissolve(1)
    d3 "Now... Where are our beloved co-stars..."
    d3 "I got carried away and was late, but they are also a bit behind the clock."
    a "Oh, you know. probably prepping for the shot in their own way."
    d3 "Don't wanna know how they do it, though. Haha..."
    play sound door2
    scene 32-10 dilan 13 with Dissolve(1)
    "A moment later both Jeff and King entered the studio."
    d3 "Great... How are you guys?"
    j2 "We're good. Let's get to work."
    k1 "Hey, Anna... How was the gym session?"
    a "Umm... It was exhilarating, I'm glad that I went, I think of making it a habit."
    k1 "I like the sound of that."
    d3 "Great, so. We will take my car and go to the set. I've already prepared everything."
    scene 32-10 dilan 14 with Dissolve(1)
    d3 "I will tell you the plot once more during our drive over there."
    d3 "It's rather simple so no big script to read is necessary."
    k1 "Also, that sister of yours is lovely. And my intuition tells me that you are, too."
    d3 "Guys, guys... Focus. We want to be professional about it."
    k1 "Sure... Let's move out then."
    play audio carsound2
    scene black with Dissolve(1)
    scene 32-10 dilan 15 with Dissolve(1)
    "They all got in the car and everyone felt a bit nervous, especially Anna."
    "This shoot was potentially going to change things for her a lot."
    a "I won't deny, I'm a bit nervous about this."
    d3 "Oh, we all are, but don't think on it too much, right Jeff?"
    j2 "Sure, sure haha... Anna take it easy, I'm here to make you all laugh."
    scene 32-10 dilan 16 with Dissolve(1)
    "While Dilan and Jeff were discussing some things in the front, King and Anna had a talk of their own."
    a "So, you visit that gym often?"
    k1 "Yeah, working out helps me unwind, takes my mind off of things."
    k1 "I'm more interested in you, though, do you go there regularly yourself?"
    a "Not really, but I've plans to start to do it. I'm pretty sure it will only help me."
    k1 "The truth."
    scene 32-10 dilan 17 with Dissolve(1)
    k1 "When I was 'massaging' your sister's leg I wondered."
    k1 "Whether or not your legs felt as soft and silky."
    k1 "I'm sorry if it's too forward but they do, Anna. Your's are astonishing."
    a "Thank you, King."
    menu:
        "Anna told King what she saw in the showers.":
            a "But I know of your little 'adventure' with Rebecca."
            k1 "You do... Huh... Well, I hope it doesn't make you uncomfortable."
            a "The opposite actually, she got to you first... Made me a bit jealous, I don't know why..."
            k1 "Hehe... Understandable."
            $ king_shower_lie = False
        "Anna decided to keep up the ruse.":
            a "I hope you fixed her issue."
            k1 "Yeah, she went out of there well and good."
            a "Thank you for that."
            $ king_shower_lie = True
    scene 32-10 dilan 18 with Dissolve(1)
    a "Regardless, your hands feel very nice on my thighs... It feels relaxing."
    k1 "I will try my best to make you feel comfortable, Anna. It's very important to me as your co-star."
    k1 "I feel that you are getting hot there... Have you been waiting for this?"
    a "I... I don't know what to say..."
    k1 "Don't. Nothing has to be said."
    scene 32-10 dilan 19 with Dissolve(1)
    d3 "And so the guy pulled out his penis the second our team started filming."
    d3 "He looked around and got stage fright. Haha... He was just there holding... No... Strangling his dick and was completely frozen."
    j2 "Haha... Even I managed to hold myself together at the first shoot."
    d3 "Yeah... Haha... He was just looking at us, not understanding anything. So, the girl started to improvise."
    d3 "Luckily we had a very good pornstar on our hands - Ruby Love."
    with vpunch
    play sound surprise
    j2 "Wait, WHAT? THE RUBY LOVE??!!"
    d3 "Yeah... She was... Very good..."
    j2 "All my career and I didn't manage to get her..."
    d3 "Ok, we are almost here!"
    play sound carsound
    scene black with Dissolve(2)
    play audio door2
    pause 0.5
    play audio door2
    scene 32-12 shoot 4 with Dissolve(1)
    d3 "Alright, sorry, I forgot to explain the script to Anna."
    d3 "Let's go over it real quick."
    d3 "So, The basic plot is that you are a girl who's decided to go out with her hubby. A rich but very faithful husband."
    d3 "Fortunately for him you had always been faithful, too... Until now..."
    d3 "He picked out an amazing dress for you and all that, but for some odd reason he's late and isn't picking up his phone."
    d3 "So you just wait and decide to play by yourself meanwhile."
    d3 "There will be two other men: These two distinguished gentlemen."
    j2 "Oh, please, Dilan. No need to be rude haha..."
    d3 "Hehe... They will be playing and of course, they will notice you."
    d3 "You won't know how to play. They will see that and propose to help you out."
    scene 32-12 shoot 3 with Dissolve(1)
    d3 "We have everything set up so I'm pretty much ready when you are."
    d3 "There will be several pool tables, just pick the closest ones."
    d3 "I've picked out an outfit for you already."
    a "Oh... This is also in such an open spot..."
    d3 "I've picked a venue that is a lot less public. So I'm certain we will be fine and no one will peek."
    d3 "So that will be pretty much it. Any questions?"
    a "I think I got everything. I'm still a bit nervous, but..."
    a "I suppose I will be fine."
    d3 "Anna, don't worry. I know you are comfortable with Jeff and King will grow on you in no time."
    d3 "We are pretty private here, and of course, I'm just here for the shots."
    a "Ok, no reason to mess around. Let's do this."
    d3 "Great. You can go over there by the pool table and change, the outfit is there as well."
    scene 32-12 shoot 5 with Dissolve(1)
    a "{i}...I guess there is no turning back now..."
    a "{i}...Still, I have my reservations but the money is nice and this might be fun..."
    "Anna was a bit reluctant and unsure but she was already on set."
    a "{i}...Alright, where is the outfit?..."
    play sound undress
    scene 32-12 shoot 6 with Dissolve(1)
    "As Anna removed the clothing. She got light shivers, but not from the room..."
    "From the excitement and being nervous about the entire ordeal."
    "The place was warm and comfortable, however, it was large and not really cozy."
    "The windows gave a lot of light to the entire room and also a lot of exposure from the outside."
    "There was nothing that would block vision if someone was to look inside..."
    scene 32-12 shoot 7 with Dissolve(1)
    "As Anna looked over, she noticed that her co-stars were indeed very professional."
    "They didn't even peek creepily but discussed details of their part."
    a "{i}...I like how serious they are about their work, but at the same time enjoying it..."
    a "{i}...Especially Jeff with his jokes, always makes me laugh and makes me comfortable..."
    scene 32-12 shoot 8 with Dissolve(1)
    d3 "So I believe you both got your parts as well?"
    j2 "Got it."
    k1 "Yep!"
    j2 "Even after all my experience, I still feel excited towards Anna and this scene."
    d3 "She is natural, just sometimes needs someone to ease her in and feel good."
    d3 "So you make her feel comfortable and good."
    k1 "She is definitely a snack. Let's do this."
    play sound undress
    scene 32-12 shoot 9 with flash
    with vpunch
    "The outfit was..."
    "Very endearing. Very seductive and even perverted."
    "Just enough to get the minds of the viewers to go crazy."
    a "{i}...Wow... It's so... Expressive..."
    a "{i}...But also comfortable..."
    scene 32-12 shoot 10 with Dissolve(1)
    a "{i}...My butt feels good in this and it also looks amazing..."
    "Anna was admiring the outfit. She felt as if it really revealed her..."
    "But then again, that was the point, wasn't it..."
    a "{i}...It does show off my assets in a very, very colorful way..."
    play sound surprise
    scene 32-12 shoot 11 with Dissolve(1)
    a "So... How do I look?"
    k1 "Wow! That looks... Hot damn!"
    j2 "You just beat the competition by a mile, Anna..."
    j2 "Pure perfection. Like Aphrodite herself."
    a "Oh, Haha..."
    d3 "I got to give it to myself... I've nailed the choice this time..."
    a "You always do, Dilan..."
    scene 32-12 shoot 12 with Dissolve(1)
    "Even when they tried to keep their composure, they all stared at her with lust..."
    d3 "Ummm... Anyway... I'm ready to get started... It's a bit hard to keep my eyes off of Anna, though."
    j2 "Have to agree... Anna, you will have no trouble to 'convince' me to help you with pool."
    "Meanwhile, King was... Even with all of his experience, mesmerized by Anna..."
    "It was his first time working with her."
    scene 32-12 shoot 13 with Dissolve(1)
    d3 "Alright, enough drooling, hehe..."
    d3 "Sorry, Anna..."
    menu:
        "(SUB) It's... Alright...":
            $ sub_var +=1
            a "I... I will just do whatever you ask of me."
            d3 "That's my girl."
        "(DOM) Anna doesn't mind.":
            $ dom_var +=1
            a "Well, I don't mind, I like when men are under my control."
            d3 "Oh? That's worth exploring."
    d3 "So guys, get into positions, I need Anna for a second."
    scene 32-12 shoot 14 with Dissolve(1)
    d3 "I guess there is no going back now."
    a "If I came this far, I might as well commit to it fully."
    d3 "That's what I like to hear. So, you got your part, yes?"
    a "I did, I will try my best to fit in, shouldn't be that hard."
    d3 "You are a natural. Hope you're feeling comfortable?"
    a "I'm a bit nervous but also excited about this opportunity."
    scene 32-12 shoot 15 with Dissolve(2)
    "The co-stars were in position and Anna got into character."
    "They all were trying to focus as much as possible."
    "But Anna... She was out there, almost entirely on display..."
    d3 "Alright, guys... I'm about to film. cut the chatter."
    d3 "AAAAND... ACTION!"
label DilanEventTwoReplay:
    $ scene_music_tracks = ["audio/sideroad.mp3", "audio/sounds/City Of Angels.mp3", "audio/sounds/Overjoyed.mp3"]
    $ renpy.random.shuffle(scene_music_tracks)
    $ renpy.music.play(scene_music_tracks, channel="music", fadein = 1, fadeout = 1)
    scene black with flash
    scene black
    "The scene: A quiet, private billiards bar where people go to take care of business."
    "Two guys are just playing pool and sunddely a complete bombshell enters the place."
    play sound surprise
    scene 32-12 shoot 16 with Dissolve(1)
    "They notice her immediately as she walks by... Their jaws dropping, heartbeat pausing for a second."
    "They can immediately feel the atmosphere shift..."
    "Both of the men go completely silent in awe of the sexiness laid in front of them."
    "The girl can feel their eyes on her and she can't stop to think that she actually likes it."
    "Why would her husband pick out such an outfit for her..."
    scene 32-12 shoot 17 with Dissolve(1)
    "Anna goes to her table and waits..."
    "Both men exchanges comments in a silent fashion."
    j2 "Whoa... Who's that? I've never seen her here..."
    k1 "I've got no idea, man..."
    k1 "I wanna go talk to her... She looks a bit confused."
    j2 "Yeah, you can see that from the back of her head?"
    play sound surprise
    scene 32-12 shoot 18 with Dissolve(1)
    "The men decide to approach the woman and inquire."
    j2 "Hey, We've never seen you here before."
    a "Oh... Hello... It's my first time..."
    k1 "Awesome, we love when people, such as yourself come and indulge."
    scene 32-12 shoot 19 with Dissolve(1)
    j2 "And... You've come here all on your own?"
    a "No, I was supposed to meet my dear hubby here some time ago..."
    a "But he's late... That's not very like him."
    j2 "I'm sure he will be here at some point, but meantime... Have you ever played pool?"
    a "I haven't I was excited to come and play."
    k1 "Why don't we 'teach' you while you wait for your dear hubby?"
    scene 32-12 shoot 20-1 with Dissolve(1)
    a "I... I don't know, my hubby told me not to talk to strangers in this bar."
    j2 "Don't worry about it, we are just friendly guys trying to help you with pool."
    a "Well, If you put it that way... I guess..."
    "As Jeff and Anna were talking, King inspected the goods with lustful eyes."
    scene 32-12 shoot 20 with Dissolve(1)
    d3 "Alright Annnnd... CUT!"
    d3 "Just wanted to say that you guys are doing great."
    d3 "Continue on with teaching her to play."
    d3 "One side note to King: Be a bit more proactive, You seem a bit off."
    k1 "I got you, will do."
    "King was having difficulty handling Anna, he hadn't seen her full sexiness before."
    d3 "Aaaand... ACTION!"
    scene 32-12 shoot 21 with flash
    j2 "So, get a comfortable pose and try to rest the cue on your fingers for stability."
    j2 "Use your hips and lean in a bit, to give more control."
    a "Like... This?"
    j2 "Yes, you got it, girl!"
    j2 "And aim for the middle of the white ball."
    scene 32-12 shoot 22 with Dissolve(1)
    a "Oh, what are you doing?"
    j2 "Don't worry, I'm just leading you a bit, is it ok?"
    a "It... It's fine."
    "The girl was naive but she didn't mind the attention... Something she hadn't experienced before."
    j2 "Yeah, just like that..."
    scene 32-12 shoot 22-1 with Dissolve(1)
    "Jeff could see her ass crack, and was wondering how someone would let such a girl walk around like this."
    "Perhaps the husband had 'business' to deal with and this was his trophy wife..."
    "He didn't care much... That asshole was late and these guys were sure as hell going to take advantage of it."
    k1 "Yeah, girl... You are in the position. Now hit the ball."
    play sound pool_cue
    scene 32-12 shoot 23 with Dissolve(1)
    a "NO!"
    j2 "Ah... Sometimes it doesn't go as planned."
    k1 "Yeah, but that was a good first shot."
    j2 "By the way, what's your name?"
    a "I'm Anna..."
    scene 32-12 shoot 24 with Dissolve(1)
    k1 "Such a beautiful name. As beautiful as you..."
    a "I... Thank you..."
    k1 "We can improve the shot, though. Would you like to?"
    a "Yes! It's fun, haha..."
    "And now the tables had turned, Jeff was 'inspecting' the goods."
    k1 "Do the same thing as before, but I will 'help' you this time."
    scene 32-12 shoot 25 with Dissolve(1)
    a "Oh... Alright..."
    "The girl was getting a bit lightheaded as the man's hands touch her body..."
    "She felt some feelings she hadn't felt before. As if something was right but also wrong..."
    "Anna did nothing to stop it, though... She was determined to learn to play pool with her hubby."
    "And these men would teach her..."
    k1 "Spread your legs a bit, to get a more stable stance."
    a "Oh... I'm trying, but my dress is in the way."
    play sound undress
    scene 32-12 shoot 26 with Dissolve(1)
    k1 "Let me help you with that."
    play sound surprise
    a "Oh... I didn't know you would do that..."
    a "Thank you again... You are very kind gentlemen."
    j2 "We aim to please as they say."
    scene 32-12 shoot 27 with Dissolve(1)
    k1 "Now you are in a position to get the shot. Be nice and slow with it."
    j2 "Take your time with lining it up, no rush is needed."
    k1 "Yeah, we like to enjoy ourselves whenever we play. Just like now."
    a "Yeah... I like playing."
    k1 "AAaannndd."
    play sound pool_cue
    scene 32-12 shoot 28 with Dissolve(1)
    a "Oh... Darn!"
    k1 "Damn, that's so close... Don't worry, we've all had these shots."
    j2 "Yeah, it was lined up perfectly, but just not enough power..."
    "They were are very comfortable and Dilan was enjoying the chemistry."
    "All of them started to feel natural and relaxed."
    scene 32-12 shoot 29 with Dissolve(1)
    a "Is there something wrong with sticks or the balls?"
    a "It's really far in the corner. What now?"
    j2 "Well, you try again."
    k1 "Yeah, nothing else to add, just need some practice to get better."
    a "I really hope so, I wouldn't want to disappoint my hubby."
    j2 "No way you could do that, girl."
    scene 32-12 shoot 30 with flash
    d3 "AAAND CUT!"
    d3 "Great job, guys. Nothing to add. You are all perfect."
    d3 "Just keep doing what you are doing!"
    d3 "AAAND ACTION!"
    scene 32-12 shoot 31 with flash
    a "This is pretty fun guys."
    a "I've already understood the basics."
    j2 "Yeah, well the company is great, you know?"
    a "Yeah, you guys are pretty cool."
    scene 32-12 shoot 32 with Dissolve(1)
    k1 "We are a lot cooler than you can imagine."
    a "Oh?"
    j2 "Yeah, we can show you a lot more than just pool skills..."
    k1 "Yeah, we got a good package 'deal' if you are interested hehe..."
    a "Hmm... That's interesting, what do you have in mind?"
    scene 32-12 shoot 33 with Dissolve(1)
    j2 "Well... We have 'BIG' pool cues of our own. And you have a 'BIG' personality, from what we've seen."
    a "Haha... You are funny!"
    k1 "But we are not lying."
    a "What are you doing?"
    j2 "Oh you know, just getting to know you better."
    scene 32-12 shoot 34 with Dissolve(1)
    "The girl was getting hot and very, very intrigued about what the men were talking about."
    "Her husband was never so mysterious and interesting..."
    "She felt new feelings, perhaps because this was her first time in such a situation..."
    a "I don't mind that..."
    play sound undress
    scene 32-12 shoot 35 with Dissolve(1)
    k1 "Do you mind if we, help you show us more of your personality?"
    a "I... I don't know if I should, though... I'm not sure my husband would approve."
    j2 "He's not here, and we think that he wouldn't want you to get bored, right?"
    a "I suppose you're right..."
    k1 "And this is fun, isn't it?"
    a "I... I don't know... I think it is... I'm getting new feelings, and they intrigue me..."
    j2 "Perhaps we should explore them?"
    play sound surprise
    scene 32-12 shoot 36 with Dissolve(1)
    a "Nope! Not yet! I need to get the ball into the hole... hehe..."
    j2 "Oh you cheeky girl, I like that!"
    k1 "Such a tease."
    a "I need to get at least one ball in the hole, then I will have succeeded."
    j2 "We can help you with that..."
    a "I got this, I will show you that I can."
    play sound surprise
    scene 32-12 shoot 37 with Dissolve(1)
    j2 "Hot Damn!"
    "Both men exchanged whispers..."
    k1 "Is she doing this on purpose?"
    j2 "Even if she is, I don't care... best 10 bucks I've spent at this place..."
    k1 "Fuck yeah, my guy!"
    "They were just so drawn to the girl... And she was just having fun..."
    scene 32-12 shoot 38 with Dissolve(1)
    "The view for both of the gentlemen was absolutely stunning."
    "The girl had no panties on... And all they could do was just stand like statues..."
    "Completely spellbound by the succulent and lustful female in front of them."
    a "Ok, guys. I got this! I will get it in this time..."
    j2 "Yeaah... You will..."
    k1 "Cmon, you can do it, girl!"
    play sound pool_cue
    scene 32-12 shoot 39 with Dissolve(1)
    a "YES! I got it in!"
    j2 "YOU DID! Awesome job, Anna."
    a "Did you like that, guys?"
    k1 "Yes. We absolutely did."
    j2 "Every single second of it..."
    play sound surprise
    scene 32-12 shoot 40 with Dissolve(1)
    a "Oh..."
    a "Mmm... That's a nice feeling..."
    k1 "I like it, too... You're very moist there..."
    a "I get like that, sometimes when I'm around men... And women..."
    j2 "Hell yeah..."
    scene 32-12 shoot 41 with Dissolve(1)
    a "Mmff... I like it, keep doing that..."
    a "This isn't wrong, is it?"
    a "I'm just having some fun..."
    k1 "Absolutely not, girl... This is just good people helping each other out..."
    a "Yeah... That's what it is..."
    a "You are both such gentlemen..."
    scene 32-12 shoot 42 with Dissolve(1)
    "The air in the room was starting to get hot from their talking and their breathing."
    "The husband was nowhere to be found, late... But the girl didn't mind..."
    "She was getting good company from the men at the bar..."
    j2 "Perhaps, you are ready for a reward for getting the ball in the hole?"
    a "I wonder what it is..."
    k1 "It's the package we were talking about..."
    play sound surprise2
    scene 32-12 shoot 43 with Dissolve(1)
    a "OH... MY..."
    a "That is a big package..."
    k1 "Yeah... It has a mind of its own, too..."
    a "Would you like me to... you know?"
    k1 "Yes, we would both like that... The package needs some care..."
    play sound surprise2
    scene 32-12 shoot 44 with Dissolve(1)
    a "Oh, and here comes the other one, hehe."
    "The girl was very intrigued what these men had in mind. She had only done anything like this with her hubby."
    "But they seemed so nice and helpful, and fun..."
    a "Well... I think..."
    j2 "Come and try out these sticks, as well, girl."
    "Even though she was into her role she enjoyed her predicament."
    play sound undress
    scene 32-12 shoot 45 with Dissolve(1)
    "She leaned down and inspected the schlongs closer."
    a "{i}...Damn, I feel like that girl, but I can't deny what I'm actually feeling..."
    "Both men could see that there was a fire burning in her eyes... Intrigue that she could barely control..."
    a "They are even bigger up close. I don't know if I can handle both of them..."
    j2 "Why don't we find out, eh?"
    play sound undress
    scene 32-12 shoot 46 with Dissolve(1)
    "Anna got down from the pool table with excitement..."
    "And grabbed them by their cocks."
    j2 "We will keep you good company while you wait for your husband."
    a "I hope he won't mind... I don't think we should do it... But... I need to repay you for helping me."
    a "{i}...Damn, that's so cheesy, but I like it..."
    k1 "Of course he wouldn't mind. You are just having fun, he will be fine..."
    scene 32-12 shoot 47 with Dissolve(1)
    a "Like this?"
    "Anna put her lips to the engorge cock before her."
    a "This is such a big package... I don't know..."
    j2 "Just try sweet Anna. You will manage."
    a "I am excited, though. I will try my best."
    play sound jerk
    scene 32-12 shoot 48 with Dissolve(1)
    "Slowly swallowing and moisturising the cock she pushed it deeper in her mouth."
    j2 "Oh... That's it... Slowly but surely."
    "The girl had never taken such big cock in her mouth before... But she was natural at it."
    a "Mmm... Mff..."
    "Jeff was feeling Anna's lips and her throat taking up his length."
    play sound jerk2
    scene 32-12 shoot 49 with Dissolve(1)
    "And she pushed it deeper and deeper. Without stopping..."
    j2 "Oh, shit... This bitch good..."
    "And the girl liked being called that, she couldn't explain why, but she liked it."
    j2 "Yeah, take my cock deeper... Are you enjoying this?"
    a "Mhm... Ah..."
    scene 32-12 shoot 50 with Dissolve(1)
    a "Ah... I like this activity. It's new and interesting to me."
    "Anna knew that everything she was saying was cheesy, but this was a porn movie, after all."
    k1 "Well, then. try out mine now. It also needs some attention."
    a "Yes, mister. If it needs it then it gets it."
    "Anna had completely forgotten about her husband."
    "He was late but that didn't mean she couldn't enjoy herself in the meantime."
    play sound jerk
    scene 32-12 shoot 51 with Dissolve(1)
    "The moment she started licking King's cock, he felt pulses through his body."
    "Like something clicked... It had been a long time since he felt a sensation like this."
    k1 "Oh, shit... That already feels good. Where did you learn this?"
    a "I... Mmm... I've never done this before..."
    j2 "Fuck. Then you are definitely a natural."
    scene 32-12 shoot 52 with Dissolve(1)
    "Not a moment passed and Anna took King's shaft deeper."
    k1 "Fuck... This is good... I'm impressed..."
    "Anna started to increase her pace and she was getting hot herself."
    "This whole thing, at the beginning it felt like acting, but now she felt like she was the girl in real life."
    "That made her enjoy this in a right and also in a wrong way."
    play sound jerk3
    show DilanShootOne with Dissolve(1)
    "The pace increased as their fun increased."
    "All of them were indulging in the moment. Even if this was work, there was no rule they couldn't enjoy it."
    k1 "Ah... Yeah... This is great!"
    k1 "Keep sucking... Ahh..."
    "And so Anna did, imagining herself as the wife awaiting her hubby's arrival."
    play sound jerk3
    show DilanShootTwo with Dissolve(1)
    hide DilanShootOne
    "Anna kept sucking on King's cock more and more."
    "And there was no way she was going to stop."
    a "Mff... Ahh..."
    "She enjoyed the new thrills of having a cock in her mouth."
    show DilanShootThree with Dissolve(1)
    hide DilanShootTwo
    k1 "Yeah... You got it... Ah... This is too good."
    j2 "Suck on that dick, polish it."
    a "Ahh... Mff... Ohhh..."
    "King was enjoying himself too much and he felt a sudden build-up that he barely managed to control."
    "Anna was doing magic down there..."
    scene 32-12 shoot 53 with Dissolve(1)
    hide DilanShootThree
    "King pulled her head off his cock, almost with a bit of force. She didn't want to let go."
    a "Was that not good enough, mister? I'm sorry if I failed."
    k1 "No. It's amazing, but I want to enjoy the moment for a bit."
    k1 "You are damn amazing. Get up."
    scene 32-12 shoot 54 with Dissolve(1)
    "He stood her up and looked at her."
    "King was feeling different kinds of feelings in this situation..."
    k1 "This is amazing, where are you getting this from?"
    a "I... I don't know... Do you like it, boys?"
    j2 "We fucking LOVE IT!"
    k1 "Let us help you out of that dress."
    play sound undress
    scene 32-12 shoot 55 with Dissolve(1)
    "They were all getting lustful. All craving that experience."
    "The girl was overtaken by the enjoyment and experience she was getting from this."
    a "Oh, your hands are making me tingle, guys... I can't believe I hadn't discovered this sooner."
    k1 "Yeah, all good things come to those who wait."
    "Both men gripped the dress and stripped it off Anna in one fell swoop."
    play sound undress
    scene 32-12 shoot 56 with Dissolve(1)
    "She was completely exposed and Dilan was getting perfect shots from this."
    "The actors had completely indulged themselves in their characters."
    d3 "{i}...This shit is perfect... They gotta pay us the bonuses, too."
    a "Hehe... I'm a bit embarrassed."
    j2 "You've got nothing to be worried about, Anna. You are so sexy, so tempting and exquisite."
    scene black with Dissolve(1)
    play audio undress
    play sound jerk2
    scene 32-12 shoot 57 with Dissolve(1)
    "Both Jeff and King quickly tore off their clothes in anticipation of pleasure."
    "They both covered Anna in hands. Licking and touching her everywhere and she was absolutely enjoying it."
    a "Ah... This feels great..."
    j2 "I know... We always try to do the best we can to new visitors like you..."
    a "You are so kind and generous... Ah..."
    play sound jerk
    scene 32-12 shoot 58 with Dissolve(1)
    "Anna was flooding with sensation."
    "She was enjoying this situation very much."
    a "Mmm..."
    k1 "Fuck, your titties are amazing."
    k1 "Gentille fille..."
    "King whispered in disbelief as he sucked on her breasts."
    play sound jerk2
    scene 32-12 shoot 59 with Dissolve(1)
    a "Oh... Ahh..."
    "Jeff didn't become such a long-lasting pornstar without knowing his stuff..."
    "He multitasked as he brought Anna wondrous pleasure."
    j2 "Yeah, you like that? You've got the moistest pussy ever..."
    j2 "Does your husband pleasure you like we do?"
    a "Ahh... I... No..."
    scene 32-12 shoot 60 with Dissolve(1)
    "They stepped back and Jeff pushed Anna against the pool table."
    a "Oh... This feels exciting... What do you have in mind?"
    j2 "Something you've never felt before..."
    "Anna waited in anticipation, she could barely hold anymore."
    scene 32-12 shoot 61 with Dissolve(1)
    "Jeff's tip started to sift around Anna's vaginal entrance."
    "She could feel it and she was going crazy..."
    a "Ah... This feels... Enticing..."
    "The temptation to put it in Anna's vagina was extreme, but Jeff wanted to enjoy the moment a bit."
    j2 "Are you ready?"
    a "Ahh... I... I think so..."
    play audio moaningthree
    scene 32-12 shoot 62 with Dissolve(1)
    "Jeff started to push his rock-hard dick into Anna's wet hole..."
    "And Anna... She just melted..."
    a "AAAH... I've not felt this... Oh..."
    j2 "Yeah? This is just the beginning..."
    a "It's amazing... MFFF..."
    play audio jerk2
    scene 32-12 shoot 64 with Dissolve(1)
    "Jeff gripped Anna more tightly and increased the pace."
    "Anna's body was shivering in pleasure. Her eyes had rolled into her head."
    a "OH... FUCK..."
    j2 "You've got such an amazing pussy, too, miss..."
    play audio moaningfive
    scene 32-12 shoot 65 with vpunch
    a "AAAHHH... SO DEEEP..."
    j2 "AAH... SO TIGHT!"
    "They were both enjoying the deep penetration with so much passion."
    a "This is thrilling... I can't believe I hadn't done this before..."
    a "My hubby will have to let me do this more..."
    scene 32-12 shoot 66 with Dissolve(1)
    "Dilan was catching everything and was ecstatic about the material."
    d3 "{i}...I would be so down to fuck her right now..."
    d3 "{i}...She is so amazing... Such beauty, such curves."
    "The fucking was becoming steamy and King wanted a piece of that."
    scene 32-12 shoot 67 with Dissolve(1)
    k1 "Pull off, this beautiful girl needs some of my cock, too..."
    a "Ah... Please, don't keep me waiting..."
    k1 "As you say. We shall give you such a good time to remember..."
    k1 "So much so, you will become a regular visitor here afterward."
    scene 32-12 shoot 68 with Dissolve(1)
    j2 "Jeff stepped back and allowed King to finally have some of that."
    k1 "And you will most definitely enjoy this."
    a "{i}...I wonder, who will make him feel better. Me or Rebecca..."
    k1 "{i}...Let's see which one of the sisters is better..."
    play sound surprise
    scene 32-12 shoot 69 with Dissolve(1)
    "King flipped Anna over and left her surprised..."
    a "Ah. What are you planning, mister?"
    k1 "To pleasure you more, girl. You deserve this."
    a "I like it, I want more... come on... Ahh..."
    play audio assclapping
    play audio moaningthree
    scene 32-12 shoot 70 with Dissolve(1)
    "King basically pushed his cock deep into Anna's vagina. Balls deep."
    "Without hesitation..."
    a "AAHHHH... FUUCK..."
    a "It's... so BIG..."
    k1 "Yeah... You like it deep in your pussy?"
    a "Oh... Yes... UGH... AHH..."
    play sound moaningfour
    show DilanShootFour with Dissolve(1)
    "King was fucking Anna in a very rhythmic, almost tribal pace."
    "And she was losing her mind... It was an absolute pleasure."
    "Her entire body was vibrating with waves of euphoria."
    "And so was King's... He was intensely enjoying Anna's entire being."
    k1 "Fuck... This is too good... I'm in disbelief..."
    a "Why? Ahh... I thought that you liked this..."
    k1 "Ahh..."
    play sound jerk2
    show DilanShootFive with Dissolve(1)
    hide DilanShootFour
    k1 "I fucking love it! It's just almost impossible..."
    k1 "Ahh... Yeah... Bitch..."
    "They were both entwined in the atmospheric sexual moment."
    k1 "Ahh... Prends ma bite, putain!"
    a "Mm...."
    play sound jerk
    scene 32-12 shoot 71 with Dissolve(1)
    "What felt like it lasted for a good while of fucking. They didn't even notice the time pass."
    k1 "This is the most mesmerizing experience ever..."
    k1 "I'm barely holding together... Ahh."
    a "Mm... This is so good..."
    "Anna tried to keep to her character as much as possible."
    play sound assclapping
    scene 32-12 shoot 72 with Dissolve(1)
    "King felt that he was getting too excited... He needed a breather..."
    "Anna didn't want to stop. So lustful and full of energy."
    "Ready to go all in..."
    k1 "Ahh... This is almost too much... Fuck."
    a "Oh, you need a quick pause, but I'm having so much fun..."
    play sound surprise
    scene 32-12 shoot 73 with Dissolve(1)
    "She pulled off of King after taking his stamina into consideration."
    "It was hard to do because the pleasure was so amazing."
    a "Ok, ok. boys... Perhaps we could 'play' on this table?"
    k1 "Oh... Shit... Ahh..."
    j2 "I would absolutely love to, Anna."
    scene 32-12 shoot 74 with Dissolve(1)
    a "Come here, I don't have enough balls on this table. I need some more."
    j2 "You don't have to ask me twice. This is the best experience ever!"
    j2 "I will come to this place all the time if you are here, too."
    a "I will consider it... hehe..."
    play sound surprise
    scene 32-12 shoot 75 with Dissolve(1)
    "Jeff didn't waste any time to get on top of Anna."
    "He gripped her as well as he could and prepped to penetrate her with all he had."
    j2 "You ready for the best time of your life?"
    a "I would hope so. You are such nice gentlemen, both of you..."
    play sound jerk
    scene 32-12 shoot 76 with Dissolve(1)
    a "AAHH... So good..."
    "Jeff barely entered her and she was already shivering from the pleasure."
    "It was too much for her to handle."
    j2 "Yeah... This is so good..."
    "Both of them were breathing heavily from the beginning."
    "But neither of them was going to stop."
    scene 32-12 shoot 77 with Dissolve(1)
    "Anna noticed that King had gotten on the table only when his cock was shoved in her face."
    a "Oh... Mff... So you want some help, too?"
    k1 "If you would... Your lips are amazing on this cock."
    a "Yeesss... Ahh..."
    play sound assclapping
    scene 32-12 shoot 78 with Dissolve(1)
    "At this point, they were all indulging deeply. Lustfully enjoying the freedom of sex."
    "The penetration was deep and satisfying for both of them, and King's dick was making its way to Anna's face."
    j2 "Fuck mee... This is so amazing... Aaah..."
    a "Fuck me harder! Ahh..."
    play sound surprise
    scene 32-12 shoot 79 with Dissolve(1)
    "Jeff decided to give Anna a surprise of his own."
    a "Oh, Aah... What are you doing?"
    j2 "I believe you might enjoy this..."
    a "No one has ever used that hole..."
    j2 "Then let me be the first to try, hehe..."
    play sound jerk
    scene 32-12 shoot 80 with Dissolve(1)
    "Anna's hole was as tight as the dress she had worn earlier."
    "Jeff had difficulty entering without heavy pleasure."
    "This was a test for him, which he was sure to pass but at a cost to his stamina."
    j2 "OH, shiet... That's tight... Your husband should use this hole some time..."
    a "Ok... Aahhh... He was always against it, but I will tell him..."
    play audio surprise2
    play sound jerk2
    scene 32-12 shoot 81 with Dissolve(1)
    "Slowly but surely the pussy juice, dick lube covered, cock was sliding into Anna's rear entrance."
    "Anna wasn't sure what she felt, it was definitely pleasurable."
    a "AAAHH... It's so big in my asshole... Fuck..."
    j2 "This is fucking amazing... Ah... I love the tightness..."
    play sound jerk
    scene 32-12 shoot 82 with Dissolve(1)
    "Anna's recently fucked pussy hole was still gaping from the cock, as if it was asking to be filled again."
    "But she was also feeling stimulation through her asshole."
    "More so it was heavenly for Jeff, who was barely keeping his composure."
    a "Oh... Aa... Fuck... It's stretching me wide."
    play audio assclapping
    play sound moaningfour
    scene 32-12 shoot 83 with Dissolve(1)
    "Anna's anus had finally and entirely swallowed Jeff's rod as he pushed her legs wide apart."
    "Anna touched her pussy with her hand to give her extra stimulation, waiting to get her mouth filled with King's cock."
    "It was ecstasy for all, King was just enjoying this moment for a while. His first experience with Anna..."
    "Even if it was a threesome, he didn't care... He started to like her."
    scene 32-12 shoot 84 with Dissolve(1)
    "Jeff suddenly grabbed Anna's hand."
    a "Oh... What are you doing now, dear mister?"
    j2 "I have a plan and I think you might like it."
    a "You keep intriguing me all the time... Ahh..."
    play sound surprise
    scene 32-12 shoot 85 with Dissolve(1)
    "He pulled Anna on top with all his might."
    j2 "I think you might enjoy what I have in mind..."
    j2 "King, come help me... Let's give her double deluxe!"
    k1 "I got you, my man. This lady's gonna get the full package."
    j2 "Come here, Anna."
    scene 32-12 shoot 86 with Dissolve(1)
    "As Jeff was changing holes, he also kissed Anna with eager passion."
    "Anna was prepared to be penetrated and satisfied..."
    a "Mm... You kiss so well."
    j2 "Cause I like you a lot..."
    play sound jerk2
    scene 32-12 shoot 91 with Dissolve(1)
    "Jeff pushed his cock into Anna's pussy with a quick thrust."
    a "AHHHH... Fuck... That feels so good..."
    j2 "Yeah, I know you like it when we fill you up."
    k1 "You are about to feel even better, Anna."
    play sound jerk
    scene 32-12 shoot 88 with Dissolve(1)
    a "AAh... Aaahhh... FUUUCkkkk..."
    "King didn't waste time to fill up her other hole..."
    "Anna experienced deep penetration in both holes and now it clicked."
    "She felt high pleasure, she didn't know she ever could get."
    play sound moaningfive
    scene 32-12 shoot 89 with Dissolve(1)
    "She had become weak in her knees for a moment after the pleasure overtook her."
    "Her entire body was feeling ripples of ecstatic euphoria."
    "Now it had finally reached its peak, they were all fucking in a hot, sweaty, and passionate manner."
    "The girl was full of excitement, intrigue, and playful pleasure."
    play audio assclapping
    scene 32-12 shoot 90 with Dissolve(1)
    j2 "You... like when... Ah... two men fill up your holes?"
    a "Fuuckk... Ahh... Is it wrong... if I say yes?"
    j2 "No... Mf... You are just having fun... Ohh..."
    a "Yes!... I love it! Ahh..."
    play sound moaningfour
    show DilanShootSix with Dissolve(1)
    "And so they all were entering a trinity of perpetual pleasure."
    "gratifying each other with vigor and slowly draining stamina."
    a "Ahhh... Both of my holes filled... Fuck..."
    j2 "Yeah, take it... Looks like you are enjoying it a lot!"
    a "Yes... Ahh..."
    play audio jerk
    show DilanShootEight with Dissolve(1)
    hide DilanShootSix
    "Jeff had an amazing look from the bottom."
    "Anna's tits jiggling with extreme range, her facial expression indicating that she was completely enveloped in euphoria."
    "Her moans filling the entire room."
    j2 "Holy shieeet... This is... Ahh..."
    "They were copulating at an ever-increasing pace."
    play audio moaningthree
    play audio jerk2
    show DilanShootSeven with Dissolve(1)
    hide DilanShootEight
    "Jeff's face was completely covered with Anna's tits."
    "Meanwhile King was whispering dirty and devious thing's into Anna's ear in French."
    k1 "Tu aimes quand nos bites te remplissent, salope?"
    "Anna couldn't understand any of it, but she loved it."
    a "FUUCk... AAHHH... Oh..."
    k1 "Shit... This is too good... Mff..."
    "They all felt that the climax was closing in with speed."
    play sound jerk
    scene 32-12 shoot 91 with Dissolve(1)
    hide DilanShootSeven
    "Anna was almost passing out. She was being held up by the sheer force of their cocks."
    "Filled up to the brim with engorged fuck sticks, she couldn't respond to anything else."
    a "I'm... So close... Don't stop!"
    "And the men didn't stop, they kept the same pace as Anna was closing up, and so were they..."
    "They were all getting so close..."
    play audio jerk2
    play sound moaningthree
    show DilanShootSeven with Dissolve(1)
    a "AAAHH.... FUCK...."
    with vpunch
    k1 "Here I come!!!!.... AAHHHH"
    with flash
    j2 "Fuck... I'm exploding! OH Shit!"
    with flash
    with flash
    with vpunch
    scene 32-12 shoot 92 with Dissolve(1)
    hide DilanShootSeven
    "They were all cumming with exorbitant force."
    "All of them moaning in a unison."
    "The entire room was echoing in screams and moans..."
    a "AAAAHHH."
    scene 32-12 shoot 94 with flash
    a "FAAAA... Fuck..."
    k1 "AAAHHH!"
    j2 "Goddamn, my dick hurts from coming this hard..."
    "Anna was completely filled in both of her holes. It was leaking everywhere..."
    "She felt so exhausted... Barely any energy left in her."
    scene 32-12 shoot 93 with Dissolve(1)
    "They all just laid there for a moment trying to catch a breath..."
    "No talking, just three people gasping and exhaling."
    "It took them a good while to recuperate..."
    a "I... Can't believe it... I didn't know that this was so fun and enjoyable."
    scene 32-12 shoot 95 with Dissolve(1)
    a "Holy shit. You've filled me up so much."
    j2 "That's what we do, Haha..."
    k1 "Man's gotta do what man's gotta do."
    a "I should come and play pool here more often."
    j2 "Sure. Do that. We would enjoy your company here. Hehe..."
    k1 "Yeah, You are good and fun... I very much enjoyed myself."
    "They had come back down from the long and extensive activity."
    a "This was... I've no words..."
    d3 "AAAAND CUT!"
    $ renpy.end_replay()
    scene 32-12 shoot 96 with flash
    d3 "SPLENDID WORK! I'm in absolute awe of the sexual prowess and passion that just took place."
    d3 "I've got all the shots, and I'm delighted with the results already. Everyone was perfectly doing their part."
    d3 "I have nothing else to add. Pure perfect content. I'm very, very satisfied... hehe..."
    a "Really?"
    d3 "Yes, Anna. You were the epitome of sexual engagement."
    play sound undress
    scene 32-12 shoot 97 with Dissolve(1)
    j2 "Well, That's a wrap then."
    k1 "This was great!"
    a "I think I did alright."
    d3 "You were perfect, Anna. I can't tell you enough how amazing this shoot was."
    d3 "I only wish you would join us more often."
    a "I will think about it."
    d3 "Alright, we are done here guys, get dressed and clean up."
    play sound undress
    if king_shower_lie == False:
        scene 32-12 shoot 98 with Dissolve(2)
        a "So. Since I know that you had an 'experience' with Rebecca in the showers..."
        a "I would like to know your thoughts about our time?"
        k1 "Damn... you gotta lay it on me now? Haha... It's really hard to tell, Anna."
        k1 "Honestly. I don't know. You are both absolutely amazing..."
        a "I will let you off easy this time, but next time, if it happens, I will want a straight answer. hehe."
        k1 "You got it, Anna."
    scene 32-12 dilan 98-1 with Dissolve(1)
    d3 "So. It will take me some time to cut and edit the film."
    d3 "And you will get the payments as soon as it's done. Should be within the next couple of days."
    d3 "However, since it's Anna's first time in a threesome and her second film..."
    d3 "I wanted to extend an offer, this might be a bit sleazy towards my current distributor, but..."
    d3 "I have another one who would want this movie and he would distribute it to a different crowd."
    d3 "One of them is for the general porn industry, which will pay less, but will give you more clout and popularity."
    d3 "Meaning that you will get more movies to star in, in the future."
    d3 "The other one is to high-end people. Rich men and women, some young but mostly old, they will pay more, but less clout."
    d3 "However another upside might be that you could potentially give escort services for great money to the high-end crowd."
    menu:
        "5,000 $, more clout, more porn movie job offers":
            a "I don't know yet, but perhaps this would be the better option if I want to continue in the future."
            a "I think I would settle for less money but with a future upside of more offers."
            $ porn_industry_var = True
        "10,000 $, less clout, escort job offers":
            a "I haven't made up my mind if I wanna continue down this path, but..."
            a "I need the money now, and if I decided that I want to do things like this more, I'd rather do it off the camera."
            $ escort_industry_var = True
    scene 32-12 shoot 100 with Dissolve(1)
    d3 "Alright, that wraps it up then. It was my pleasure to work with you."
    d3 "Take care, I will get in contact with you in the following days regarding the payment and other details."
    a "Alright, Thank you, Dilan. It was amazing guys."
    j2 "The feeling's mutual, Anna."
    k1 "You are awesome. Have a good one and see you at the gym."
    stop sound
    $ persistent.twelfthScene = True
    $ AnnaCorruption += 3
    $ corruption_func("Anna Corruption +3")
    if timothySexContent == True:
        jump TimothyHomeEventOne
    else:
        jump JeremyHomeEventOne
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
