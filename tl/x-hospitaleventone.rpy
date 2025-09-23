label hospitalandrewroom_1:
    $ isActivePlace = 0
    play sound door2
    scene 29-14 hospital 30 with Dissolve(1)
    "Anna entered Andrew's room once more before leaving for home. She was much more confused than previously."
    "She felt all kinds of emotions, grief, regret but also curiosity and a lot of questions."
    a "Oh boy, this whole situation got really interesting, really fast. Maybe if you were okay, Andrew, you could help me."
    a "{i}...Or maybe not. All of this is really your doing, directly or not. Still, Rebecca was right about a lot of stuff..."
    a "{i}...And honestly, I'm really close to tipping over. I'm so confused, distressed and I have no idea how to deal with all this bullshit."
    a "{i}...Sergey, Fitzgerald... The whole situation to get money for your surgery..."
    a "{i}...Fuck..."
    a "Regardless, I came in to check up on you once more and say goodbye for now."
    play sound "audio/sounds/door2.ogg"
    cop1 "Excuse me, Are you Anna?"
    scene 29-14 hospital 31 with Dissolve(1)
    play sound "audio/sounds/jump2.ogg"
    a "Oh, You startled me. Yes... That's me."
    cop1 "My apologies ma'am. I didn't mean to intrude."
    cop1 "However I'm in need of your assistance. As I'm aware you know what I'm most likely talking about correct?"
    a "Hehe. I'm not that dumb to incriminate myself, by saying that I know what you are talking about."
    cop1 "Good, then I will also let you know that we have witness statements that put a woman of your description at the scene of a shooting."
    cop1 "Therefore I would ask you to cooperate and things will go along more smoothly."
    a "Right, you got me there."
    cop1 "Don't worry, from the gathered accounts, we do not think that you are a suspect."
    cop1 "However to fortify an ironclad defense and create a crime profile, we would like for you to come down to the precinct and give an official statement."
    scene 29-14 hospital 32 with Dissolve(1)
    cop1 "It's a formality that would ensure that the correct criminal is charged with first-degree murder as far as we know."
    cop1 "Also your statement would prove that you are not an accessory to murder."
    a "Accessory to murder? I'm this man's girlfriend. How would I be in any position to commit such a crime?"
    cop1 "You see, crimes of passion are not as rare as you'd think. We merely want to catch the criminal, that's all."
    a "I see. Well, what would I have to do?"
    cop1 "{i}...If I could justify it, I would ask you to strip for me back at the precinct... Oh, that would be the day..."
    scene 29-14 hospital 33 with Dissolve(1)
    cop1 "Right now I would just like to write down a few personal details. like your name, address, phone number. also a simple chain of events of the crime that was committed."
    cop1 "All of these are necessary to ensure both your credibility and that you arrive at the precinct. I hope you understand ma'am."
    a "Yeah, yeah sure."
    a "My name is Anna. I live on 150A Baker street. My phone number is +981 2020 4222"
    cop1 "Sorry I didn't get the entire number +981 2020 and..."
    a "It was 4222 at the end."
    cop1 "Right. So can you maybe tell me a simple recollection of the events that occurred and how things went down?"
    a "Well, Andrew and I had planned a date. But when I got there, everything was fucked up."
    a "Andrew was laying on the ground. I immediately approached him and then I saw a gunshot wound in his chest."
    a "{i}*sob*{/i} I called 911 as soon as I could, I was in shock, but I managed to get the call through."
    scene 29-14 hospital 34 with Dissolve(1)
    cop1 "It's okay ma'am. But I have to ask, why did you go to such a dangerous part of town for a date?"
    a "Well, we wanted to make things a bit more interesting and spice it up a little. {i}*sob*{/i}"
    a "I didn't think it would be that dangerous there, had I know, we wouldn't have planned to go there."
    cop1 "Okay, that is enough, it's okay ma'am. I won't ask any more of you now."
    cop1 "But like I said It would be great if you could come down to the precinct tomorrow and give a formal statement about all of this."
    a "Okay, I will. Thank you."
    scene 29-14 hospital 35 with Dissolve(1)
    cop1 "Alright, maybe I can take you home? It is quite late right now, that would be safer. What do you think?"
    a "Okay officer, thank you. We can go now."
    scene black with Dissolve(1)
label carcop:
    play sound "audio/sounds/car.ogg"
    scene 29-16 cop 1 with Dissolve(1)
    cop1 "So, how are you holding up ma'am? I mean in general?"
    a "Well, as good as someone in my position could. A person close to me was shot. God, people these days are relentless."
    a "Mugging left and right. I guess that's what we get for staying on the wrong side of town."
    cop1 "{i}...I feel like she is holding some info back... Well, it could be just me."
    cop1 "{i}...But when she comes down to the precinct we will have a more {b}deeper{/b} investigation hehe..."
    cop1 "I see. Hey, sometimes those things just happen, you know? At least he is alive."
    a "Yeah, but it's still complicated, he requires further surgery and it is quite costly."
    scene 29-16 cop 2 with Dissolve(1)
    cop1 "Yeah, I had a cousin who was also a police officer, and he was injured on the job. Heavily."
    a "Oh, that's terrible, is he ok?"
    cop1 "I mean, yeah, that was long ago, but what I was saying is that he got shot and now is disabled."
    cop1 "If we had known that we could save him, our family would have."
    a "Oh my. I'm so sorry, but how did you receive the news when you found out."
    cop1 "Well, the thing is, in our line of work, those things are a part of the job. It comes with the territory, so to speak."
    cop1 "I was, of course, hurt and shocked and angry but as I said, it's what we do. And it's what happens to some of us."
    a "Well, I guess you've given me more motivation to figure out how to help my boyfriend."
    cop1 "Say, I've been trying to figure this out all evening. You look familiar."
    cop1 "I wonder if I have seen you somewhere before?"
    scene 29-16 cop 3 with Dissolve(1)
    "Anna tried to figure it out."
    a "{i}...Wait, Do I know this man?..."
    menu:
        "Yeah, I saw him when taxman took me home.":
            $ taxmandrive = True
            $ relationship_func("Police and Taxman Relationship +1")
            $ DesmondRelationship += 1
            $ TaxmanRelationship += 1
            scene 29-16 cop 4 with Dissolve(1)
            a "I'm not really sure, but I might have seen you too."
            a "Maybe it was you who pulled me and the taxman over at the bar before?"
        "No, I don't know this man, first time I've seen him.":
            $ taxmandrive = False
            scene 29-16 cop 2 with Dissolve(1)
            a "I'm sorry, I don't recall you. Maybe you've mistaken me for someone else."
    if taxmandrive == True:
        cop1 "Well, yeah, I knew it. I recognized you from somewhere."
        cop1 "{i}...Excellent, This should improve my odds even more..."
    else:
        cop1 "{i}...Oh, well. It doesn't hurt to try. I swear I knew her. I guess not..."
        cop1 "{i}...Perhaps she would still be interested in some of the things I've got on my mind..."
    cop1 "Anyway. We are not far. Do you need anything, maybe some water or anything like that?"
    a "Thank you officer, I will be fine."
    cop1 "No problem, have to ask since you've been under such stress lately, you have to forget about things for a while and relax."
    a "I agree, crazy things have happened. Luckily Andrew is alive at least, so that's a relief."
    cop1 "Good to hear that, ma'am."
    play sound "audio/sounds/car.ogg"
    scene black with Dissolve(1)
    scene 29-16 cop 1 with Dissolve(1)
    cop1 "Well, it looks like we are here."
    a "Yes officer, this is the place. Thank you for taking me home."
    cop1 "Just doing my sworn duty, that's all ma'am. Take care."
    a "Thank you, officer, you too."
    play sound walk
    scene black with Dissolve(3)
    jump livingroom1sttime
    return
label hospitaltwo_1:
    $ isActivePlace = 100
    hide screen disableClick
    hide screen hospitalmap
    scene hospitalmap
    a "{i}... I already had the discussion with that sleazy doctor..."
    jump hospitalreception
    return
label hospitaltwo_2:
    $ isActivePlace = 100
    hide screen disableClick
    hide screen hospitalmap
    scene hospitalmap
    a "{i}... I should check up on Andrew once more before I leave..."
    jump hospitalreception
    return
label annaself1:
    $ isActivePlace = 100
    hide screen disableClick
    hide screen hospitalmap
    scene hospitalmap
    a "{i}...I need to see the Doctor right now..."
    jump hospitalreception
    return
label hospitalone:
    $ isActivePlace = 0
    play music "audio/sounds/tranquility.mp3"
    scene 29-14 hospital 2 with Dissolve(1)
    stop sound fadeout 1.0
    a "Oh my god...he looks so strange. I hope he's going to be ok."
    d1 "Yes, he's fine for now."
    a "For now?"
    d1 "Well, the bullet could be extracted without causing irreversible damage."
    d1 "We had to make multiple incisions in his chest because the bullet had penetrated the lungs and caused internal bleeding."
    d1 "The removal of the foreign object turned out successfully and no other organs were severely wounded in the process."
    d1 "However, due to the destructive nature of the bullet, the injury was quite extensive."
    a "What do you mean?"
    scene 29-14 hospital 3
    d1 "There was still some collateral damage that was situated around the chest cavity area and lungs. Also a couple of broken ribs."
    a "Oh my god...sounds bad..."
    a "Will he recover?"
    d1 "He's young and strong. With the proper treatment, he should be fine."
    d1 "When the bullet was extracted, we closed up the wound and gave him morphine and pentobarbital to induce a coma-like state."
    a "That's why he looks like he's just asleep."
    d1 "This was done to minimize the risk of body movements that could cause tears at the damaged area."
    d1 "Professional nurses will carry out a change of sleeping position in a careful manner as to not cause decubitus ulcers also known as bedsores."
    scene 29-14 hospital 4
    d1 "He will be kept in this state until his wounds are more healed."
    a "How long will he be like this?"
    d1 "Can't say exactly, depends on the person, but in this case a couple of days at the minimum."
    a "Jeez...for so long?"
    d1 "Well, that's not that long."
    scene 29-14 hospital 5
    d1 "By the way, it would be nice if you could join me in my office a moment later."
    d1 "There are some details that we have to discuss, Thank you."
    d1 "{i}...And then the real talking shall begin..."
    a "Yeah, no problem doc."
    a "{i}...What does he want to talk about?..."
    play sound door2
    scene 29-14 hospital 4
    "Doctor left the room."
    a "Jeez, Andrew, it's terrible, why did it have to happen to you... "
    r1 "He shouldn't have been there in the first place."
    a "Please, I can't even imagine what was going through his mind at that time."
    r1 "They say that during those situations the entire life flashes before the person's eyes."
    a "This gives me shivers, crazy how things went."
    scene 29-14 hospital 6
    a "I mean I've seen some things lately, but this..."
    a "I wonder if there is something that I could have done to prevent this."
    r1 "There is nothing you could've done, I hope you don't blame yourself."
    a "I still feel kind of guilty about all of this."
    scene 29-14 hospital 7
    play sound surprise
    r1 "You know what, that's bullshit! He turned his back on us, gave us up!"
    r1 "You owe him nothing, least of all any apologies. He brought this upon us and himself!"
    a "Don't be that harsh. People make mistakes."
    a "{i}...We all make mistakes... I know I've made some..."
    scene 29-14 hospital 8
    r1 "I don't really care, he put us in danger, I'm the forgiving type but this has sent me over the edge."
    r1 "People make mistakes, yes, like leaving the toilet seat up or forgetting to buy milk."
    r1 "But this is pure neglect and short-sighted approach to a damn dangerous situation."
    a "{i}...Rebecca seems really pissed this time..."
    r1 "As far as I'm concerned, I think you should dump Andrew..."
    scene 29-14 hospital 6
    a "I know he gave us up, but still, Andrew must have been confused... I think all he tried to do was save me."
    r1 "Save you? How, giving us up is saving you?"
    a "I don't know, maybe they threatened to kill me or something."
    a "This was a really heated situation, I don't know if I could have done anything differently if I were in his place."
    r1 "Right... I'm still furious and that doesn't change the fact!"
    r1 "He should have talked to Sergey in the first place!"
    scene 29-14 hospital 7
    a "You are right...he should have done that but he must have had his doubts."
    r1 "Like I said, short-sighted. I don't know what else to say."
    r1 "We will get more information when he wakes up. Whenever that will be."
    r1 "And when he does he will get an ass-whooping from me, when he is in a state for that."
    r1 "Anyway, enough about this entire parade of nonsense, enough dwelling right now."
    r1 "I hope you remember what to tell to the police?"
    a "Yeah...I hope they won't have any suspicions."
    scene 29-14 hospital 9
    r1 "Come here Anna, give your big sister a nice hug. We both need one."
    r1 "Are you ok? Will you be alright?"
    a "Yes, Rebecca. Thank you, I will be fine."

    r1 "Anyway. The most important thing to me is that you are safe."
    r1 "I'm gonna go now. Carl is waiting for me, and I can't stay until the police arrive. Take care, sis."
    a "See you later, Rebecca."
    scene 29-14 hospital 10
    play sound door2
    a "Oh Andrew, how did this all go so wrong so fast? How could you give us up like this?"
    a "What were you thinking? With the best of intentions maybe, but screwed up so hard this time."
    a "Some mistakes can cost lives... This is a lot, Andrew..."
    a "But I can't leave you now, not like this."
    a "Not after all the times you helped me before. Saving me from my drunk father."
    a "I don't know what would have happened if you hadn't been there for me."
    scene 29-14 hospital 11
    a "{i}...But Rebecca did say that I don't owe him anything, I don't know though..."
    a "{i}...I mean, what is it to wait a couple of days and think this through..."
    a "{i}...Not make rash decisions without knowing all the facts first... "
    a "We will talk when you get better, hope you recover soon."
    a "I'm gonna go to the doctor now, but I will come back a bit later to say goodbye."
    scene black with Dissolve(1)
    play sound "audio/sounds/door2.ogg"
label doctorconvo:
    scene hospitalmap
    a "{i}...Wait, That's Harold. I should go and talk to him, ask about the doctor..."
    scene 29-15 corridor 1
    play sound surprise
    a "Hey Harold, long time no see. How've you been?"
    h "Anna? What are you doing here? What has happened?"
    h "{i}...Dammn... She looks so fine, as good as I remember..."
    "Harold lightly smacks his lips, he is overtaken by Anna's looks. He can't take his eyes off of her."
    scene 29-15 corridor 2
    h "Was the guy in the ER someone you know?"
    a "Yeah, it's my boyfriend Andrew. He was shot in the chest."
    h "Oh, That's terrible, What is his condition?"
    h "{i}Even though I like Anna, I hope Andrew's condition improves. I am, after all, a doctor..."
    a "He is in an induced coma right now, and the damage was extensive, he will be out for some time."
    h "I hope he gets better soon, we will keep a keen eye on his condition, don't you worry."
    scene 29-15 corridor 3
    h "{i}...Damn, that dress... They must have something going on there..."
    h "{i}...Concentrate Harold, concentrate, don't blow your composure and say or do something dumb..."
    scene 29-15 corridor 2
    h "Anyway, do you mind sharing any details of how Andrew ended up with a gunshot in his {i}pleural cavity{i}?"
    a "I don't even know what that means. if you mean his lungs, then... it's a long story."
    h "{i}...Of course, I said something stupid, who cares what it's called in Latin. Well, besides me..."
    h "I mean... yeah lungs, sorry, I sometimes get carried away with my studies here."
    scene 29-15 corridor 4
    h "How did it happen?"
    a "I'm sorry, but I don't want to talk about it now."
    h "Sure, I won't bother, if you do decide to speak to someone about it, let me know."
    a "Anyway. An intern, huh? And at this respectable hospital?"
    h "Yeah, well, I worked my ass off to get here, but yeah, it's crazy how I got here, maybe sometime we can talk about it more to a cup of coffee or such."
    a "Perhaps. But for now, I have to get going. I have a meeting with the doctor."
    if doctortalkhappen == False:
        scene 29-15 corridor 5
        a "Excuse me, could you tell me where the doctor's office is?"
        nursereception "Dr. Schmidt is down the hall, opposite room 210. Your friend Andrew's room that is."
        nursereception "That is room 203. He is waiting for you inside."
        a "Thank you kindly. Catch you later Harold."
    else:
        a "Bye Harold!"
label hospitaltwo:
    $ isActivePlace = 0
    stop music
    play music "audio/sounds/bensound-funkysuspense.ogg"
    $ d1 = Character("Dr. Schmidt", color = "#90AEF9")
    hide screen disableClick
    play audio "audio/sounds/door2.ogg"
    scene 29-14 hospital 12
    play audio "audio/sounds/jump1.ogg"
    d1 "It's not your decision and don't even try to speak about it."
    "To Anna's surprise, Dr. Schmidt was not alone, there was another doctor with him."
    "Anna was not entirely sure what that meant."
    "Both of the doctors were arguing about something."
    a "{i}...Who is she?... I hope they won't ask me to disclose any details of the shooting..."
    a "{i}...I already got a lot on my plate..."
    a "{i}...What are they arguing about? Something to do with some costs?..."
    a "Hello, Dr. Schmidt? You said you wanted to see me?"
    a "Perhaps I came at the wrong time?"
    d1 "Ah, Anna. No, not at all. Please come in."
    d1 "We have a couple of things to discuss before you take your leave."
    scene 29-14 hospital 13
    d1 "Let's cut to the case so to speak. We have pressing matters on the agenda."
    d1 "We wish to get those out of the way as soon as possible and you might be able to help us."
    a "What could I help YOU with? I have no experience as a doctor or anything like that."
    "There was palpable angst in the air, from all parties currently present."
    a "{i}...I hope it's nothing serious..."
    d1 "Please, Anna, take a seat."
    play sound undress
    scene 29-14 hospital 14 with Dissolve(1)
    "Anna takes a seat."
    a "Okay, what is the problem?"
    d1 "You see, there is an issue with Andrew's condition, his injuries are quite bad..."
    a "But you told me that he's going to be fine."
    d1 "I know, he is for now, but he will require further surgery to ensure that his condition does not deteriorate."
    a "What do you mean by another surgery? I thought he is going to recover."
    d1 "He probably will, but there is also a high likelihood of him having severe complications if no other surgery is performed."
    a "Well, then go on!"
    d1 "The issue with this situation is that further surgery is quite costly."
    play sound surprise
    scene 29-14 hospital 18 with Dissolve(0.5)
    a "What? I thought that the hospital covered these kind of emergencies."
    d1 "They do, but this surgery was a means to keep him alive and he does not have insurance that covers the other parts."
    d1 "When he recovers and no other operations are performed..."
    d1 "...He might not..."
    "As Dr. Schmidt was explaining the details of the situation to Anna, his focus was somewhere else."
    "He was trying to remember if he had a previous encounter with Anna already."
    scene 29-14 hospital 14 with Dissolve(0.5)
    d1 "{i}...If I recall correctly..."
    "This choice will have an impact on the relationship with Dr. Schmidt."
    menu:
        "I did the first phase of manipulations on Anna previously.":
            $ doctormanipulations = True
            play sound surprise
            scene 29-14 hospital 14-1 with Dissolve(0.5)
            d1 "{i}Yes... As I remember... Her chest is a prime example of the pinnacle of human body's evolution..."
            d1 "{i}...I mean... This...is...a specimen...One of a kind..."
            d1 "{i}...I wonder if she would be willing to continue our studies..."
            d1 "{i}...Maybe she is gullible enough to be manipulated further..."
            scene 29-14 hospital 16 with Dissolve(0.5)
            d2 "...And like Dr. Schmidt said previously, if the surgeries I mentioned are not performed, he might come out with heavy complications."
            scene 29-14 hospital 14-1 with Dissolve(0.5)
            with vpunch
            d1 "Oh, what? Right. Yes, yes. Biiiig complications."
        "I wish she had allowed me to do my experiments.":
            $ doctormanipulations = False
            scene 29-14 hospital 16 with Dissolve(0.5)
            d2 "...And like I said previously, if the surgeries I mentioned are not performed, he might come out with heavy complications."
            d1 "Oh, what? Right. She is correct."
    scene 29-14 hospital 17 with Dissolve(0.5)
    d2 "But don't worry Anna, we can look for a solution together."
    d2 "However, since you are, as far as we know, next of kin to him, you must make that decision."
    a "I figured out as much, yeah. Thanks, but it doesn't make it any easier."
    d2 "No, it doesn't, I'm sorry."
    scene 29-14 hospital 18 with Dissolve(0.5)
    a "How can you put this pressure on me. I did not want any of this."
    d1 "I'm sorry Anna, it's merely the hospital policy."
    a "{i}...Honestly fuck this shit..."
    a "Alright, alright."
    scene 29-14 hospital 19 with Dissolve(0.5)
    a "This is a tought situation that you've put me in."
    d1 "Sorry, if anyone put you there it was Andrew, I'm fairly confident that there is some foul play."
    d2 "We cannot say that James. It's unclear what happened, might just be a mugging."
    d1 "Right. Regardless, this is the situation we are in."
    a "{i}...I need to get my head straight and figure this out..."
    scene 29-14 hospital 20 with Dissolve(0.5)
    d2 "Anyway, take your time Anna, we can still wait a bit before making the final decision."
    d2 "I will leave now, I have an appointment with a patient."
    d1 "Thank you doctor."
    d2 "Take care Anna, we will do the best that we can."
    scene 29-14 hospital 17 with Dissolve(0.5)
    a "Thank you Dr.... What is your name?"
    d2 "I'm Dr. Cary Eilhart."
    a "Thank you Dr. Eilhart. I know you will."
    scene 29-15 hospital 23 with Dissolve(0.5)
    a "She seems like a very capable and nice doctor."
    d1 "Yes she is. One of the best actually. I took her under my wing when she just joined us."
    d1 "{i}...And its not the only thing she is good at..."
    d1 "Anyway. The entire surgery would cost around the 100,000 dollar mark."
    scene 29-15 hospital 24 with Dissolve(0.5)

    play sound surprise2

    a "WHAT????"
    a "You must be joking. That is an entire year worth of salary in many cases."
    d1 "Yes, but I reckon that not in your case."
    a "What is that supposed to mean?"
    d1 "Nothing, forget about it."
    d1 "Anyway. Either one hundred thousand dollars full price or we can strike a deal."
    a "What kinda deal?"
    a "{i}...Why do I feel like it's something I won't like hearing?"
    d1 "The trauma you had some time ago, we didn't quite research it thoroughly!"
    a "I don't really wanna talk about it."
    if doctormanipulations == True:
        d1 "Sure, but if you let me study this condition further, I am willing to decrease the price to 60,000 dollars."
    else:
        d1 "Sure, but if you let me study this condition of yours, I am willing to decrease the price to 60,000 dollars."
    a "What's in it for you?"
    d1 "It's a very rare condition and I could become quite famous in medical society thank's to you."
    a "{i}...What a prick, just thinking about himself..."
    a "And what if I don't accept either offer?"
    d1 "Well, then you risk Andrew having permanent damage. Remember Anna, time is running short."
    scene 29-15 hospital 25 with Dissolve(0.5)
    if doctormanipulations == True:
        a "I don't know doctor, I will have to think about it."
        d1 "Sure, just know that you don't have much time, please make up your mind until the next appointment."
        d1 "{i}...Oh and then the fun will begin... We will study so many things about the nature of this girl..."
        d1 "{i}...Things are coming up aces... So to speak..."
        a "{i}...This scumbag, extorting people... 100,000 for a surgery... The gall on this creep..."
        a "{i}...But what other choice do I have? Perhaps I can look for Dr. Eilhart, maybe she has another option..."
        a "{i}...But then again If I let the doctor study my condition, perhaps I will also understand it better myself..."
    else:
        a "I don't know doctor, I don't think I'm willing to be exploited like that."
        d1 "Sure, just know that you don't have much time, please make up your mind until the next appointment."
        d1 "{i}...The reality is often disappointing...Oh well, I had to try...Perhaps she will change her mind..."
        a "{i}...This scumbag, extorting people... 100,000 for a surgery... The gall on this creep..."
        a "{i}...But what other choice do I have? Perhaps I can look for Dr. Eilhart, maybe she has another option..."
    $ doctortalkhappen = True
    scene black with Dissolve(1)
    jump hospitalthree
    return
label hospitalthree:
    $ isActivePlace = 0
    play music tranquility
    play sound "audio/sounds/door2.ogg"
    scene 29-15 hospital 26 with Dissolve (0.5)
    d2 "Hey Anna, I wished to speak with you without Dr. Schmidt's presence."
    d2 "I know what he is trying to do and I know how you feel. He is using this situation to his advantage."
    d2 "And I, in my good conscious mind, cannot really let this go. The surgery is not as expensive as he claims."
    d2 "{i}...Poor girl fell into James' fingers. I cannot allow her to go through with this..."
    a "Huh, I did figure that part out. Do you have any other options or suggestions?"
    scene 29-15 hospital 27 with Dissolve (0.5)
    d2 "Actually, yes I do. However I cannot do much in this situation without your help. You see, he makes the decisions here anyway."
    d2 "Due to that fact, my hands are tied. But if we found a way to incriminate him for his previous indiscretions, we might be able to get him out of the picture."
    a "More drama? Seems like my life is one giant loop of drama these days... heh."
    d2 "I understand you Anna, I really do. I have some history with this place and Dr. Schmidt, so I know how you feel."
    scene 29-14 hospital 28 with Dissolve (0.5)
    a "Alright. Sure. What would need to be done to get this incriminating evidence?"
    d2 "It's a bit more complicated than that. But simply put, you would have to sneak into his office and find clues as to where documents with sensitive information might be located."
    d2 "Also, I'm pretty sure there is a memory card from a camera stored somewhere, if you could find that, I would tremendously appreciate that."
    d2 "As far as I know, it contains some... Um... compromising photos and videos of me..."
    d2 "I won't tell you any further details about that right now though."
    d2 "I assume that finding it won't be easy, however, I do think that you are resourceful enough to succeed."
    d2 "Now, I will admit that I also have a personal gain from this."
    d2 "But I'm willing to take the chance if you are, I think it's for the best."
    a "{i}She seems quite motivated. I wonder what history she has with the doctor that is so complicated."
    "Anna was pondering about the reasons why the doctor would be so interested to set Dr. Schmidt up."
    scene 29-14 hospital 29 with Dissolve (0.5)
    d2 "I know that it is a lot to take in so you have some time to think about it, but don't take too long. Remember, that Andrew's well-being is on the line."
    a "Yeah, I know, I know. But it's just... Why things always have to be so complicated?"
    d2 "I don't know. I wish it was more simple. Some people are just like that, you know?"
    d2 "Anyhow, I will leave you to it. Perhaps you should say goodbye to Andrew once more and go home, think things through, get some rest."
    d2 "I think that you've been through quite a lot. Maybe, after this all is over, we could have a deeper conversation about all of these things."
    a "Maybe. You seem like a genuine person Cary. I will think this through and get back to you next time I'm here."
    d2 "Sounds like a plan."
    scene black with Dissolve(2)
    $ GlossaryUnlockDrSchmidt = True
    $ GlossaryUnlockDrCary = True
    jump hospitalandrewroom_1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
