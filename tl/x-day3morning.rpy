label dayThreeMorning:
    $ renpy.music.play("audio/sounds/Purple Planet Music Rendezvous.mp3", channel = 'music', if_changed = True)
    $ GlossaryUnlockAlfred = True
    scene 31-1 morning 1 with vpunch
    play sound phonecall
    "Anna was woken by a sudden phone call."
    "It was morning already. Felt like sleep was instant."
    "No dreams, nothing..."
    play sound surprise
    "She was surprised. The call was from Sergey."
    "She had been deep in sleep."
    play sound phonecall
    scene 31-1 morning 2 with Dissolve(1)
    "Anna quickly picked it up."
    a "He... Hello?"
    s1 "Good morning, Anna."
    a "Hi, Sergey. How are you?"
    s1 "I'm fine. How are you doing, though?"
    a "As well as I could."
    s1 "Understandable. Hey, listen. We should meet. Ok?"
    a "Umm. Sure."
    s1 "I would like you to come to my place around evening. Could you do that?"
    a "Your place?"
    s1 "The place where we met before all the events."
    a "Oh I get it, Sergey. I will be there."
    s1 "Alright, great. Make sure no one follows you. Ok?"
    a "Ok, I will be extra cautious."
    $ GlossaryUnlockSergey = True
    scene 31-1 morning 3 with Dissolve(1)
    "Sergey hung up. Anna was a bit surprised and a bit nervous."
    a "{i}...Now that was a quick talk..."
    a "{i}...I hope it's nothing serious. Like Sergey tieing up loose ends or something..."
    a "{i}...Probably not. I'm just overthinking it..."
    a "{i}...I haven't done anything wrong, have I?..."
    if AlfredRelationship == True:
        if AlfredLeaves == False:
            "Anna saw that Alfred had already got up and got dressed."
            "She heard someone doing something in the kitchen. Perhaps it's Alfred."
            "Anna put down the phone and decided to go to the kitchen."
            jump dayThreeMorningOne
        else:
            "Anna put down the phone and decided to get dressed."
            jump dayThreeMorningNone
    else:
        "Anna put down the phone and decided to get dressed."
        jump dayThreeMorningNone

label dayThreeMorningOne:
    scene black with Dissolve(1)
    play sound door2
    scene 31-1 morning 4 with Dissolve(1)
    play sound surprise
    play music jazzmusic
    "Anna was greeted with breakfast, that Alfred had made."
    "She was surprised. But also very glad."
    a "{i}...I can't believe it. Alfred is always so nice..."
    a2 "Good morning, Anna. I made us both a little breakfast."
    a "Hello Alfred, I'm surprised. Thank you for this."
    scene 31-1 morning 5 with Dissolve(1)
    a "But you didn't have to."
    a2 "I believe the opposite, Anna. You deserve it."
    a2 "Plus, I think you should taste my famous eggs with bacon."
    a2 "It's my hidden recipe."
    a "Really? I'm curious now."
    a2 "I'm joking, Anna. Hehe. I get lucky if I don't burn them, usually."
    a "Oh... Haha.."
    a2 "Please, take a seat, let's have some breakfast."
    scene 31-1 morning 6 with Dissolve(1)
    a2 "And then I have to get going. Gotta go to the clothing shop."
    a2 "Check out the collections and prepare them."
    a2 "I really hope you can come down to the clothing shop in the following days."
    a "I can't do it today, but I will go as soon as possible."
    a2 "Thank you, Anna. I really hope you will enjoy what we have received now."
    a2 "So how are you feeling today?"
    a "Oh, I have some things to do but yesterday made me feel so much better."
    a "Thank you, Alfred. You really helped me take the edge off."
    scene 31-1 morning 7 with Dissolve(1)
    a2 "Think nothing of it. I have to help if I can."
    a "That's sweet."
    a2 "I try to be."
    a "We should do this a bit more often. It really helps. Plus, you could watch the new series with me."
    a2 "Well... That's a proposal that I can't really say no to, And I will try to pay attention to the series. hehe."
    a2 "Perhaps I will even look into the comics again. It might bring back my youthful excitement."
    a "Definitely, never too old to try anything."
    a2 "But almost too old to carry around drunk Anna."
    a "Haha. I'm sorry Alfred, I didn't mean to."
    a2 "Don't worry, Anna. I'm just joking. Carrying you made me feel young again."
    scene black with Dissolve(1)
    "They finished their breakfast."
    scene 31-1 morning 8 with Dissolve(1)
    a "Well, your legendary eggs with bacon lived up to the expectations."
    a2 "Oh, Anna. No need to completely destroy my hopes of becoming a chef someday."
    a "Haha... That wasn't sarcasm, Alfred."
    a "You might just make it if you don't burn the food. Like this time, it was cooked to perfection."
    a2 "Thank you, Anna. It gives me hope. Hehe."
    a2 "Anyway, I should get going, have to prepare and all that."
    a "Ok, Alfred."
    a2 "But if we don't meet during the next days, please drop by when you have the time. I would appreciate it tremendously."
    a "I will be sure to drop by when I can."
    scene 31-1 morning 9 with Dissolve(1)
    "Anna leaned close to Alfred. Hugged him."
    "She felt warmth again like she had felt the previous evening."
    "Alfred was happy as well. Anna gave him feelings of youth. the excitement that hadn't been there for some time."
    a "Alfred, Thank you again for everything. I'm grateful for all that you've done."
    a2 "Thank you too, Anna. I'm also in your debt. You've helped me a lot too."
    a2 "From helping with the clothing shop to making me feel excitement and feelings I've been lacking for a long time."
    "Anna Looked Alfred in the eyes..."
    play sound jerk
    scene 31-1 morning 10 with Dissolve(1)
    "...And kissed him..."
    "It was a kiss of gratefulness and sympathy."
    "Alfred was feeling nervous throughout his body."
    "He felt tingly in the head as though he had felt when he was first with a girl back in the old days."
    "Anna was enjoying the moment too. It felt like nothing could hurt her. Safety and passion grasped her."
    "They didn't move for a good moment and relished each other's company a little longer."
    scene 31-1 morning 9 with Dissolve(1)
    a2 "Oh, Anna. Your lips are as soft as the bloom of a lily petal."
    a "Alfred... It's always so special with you. Such compliments are rare these days."
    a2 "Thank you, Anna."
    a2 "It's time for me to go, though."
    a "Okay, Alfred."
    scene black with Dissolve(1)
    "As they were approaching the door it opened."
    play audio door2
    scene 31-1 morning 11 with Dissolve(1)
    play audio surprise
    "It was John."
    a2 "Good morning."
    j "What the... Hello?"
    j "Who are you?"
    a2 "I'm Anna's neighbor."
    a "It's Alfred from the next door apartment."
    j "Right..."
    a2 "Goodbye, Anna."
    play sound door2
    scene 31-1 morning 12 with Dissolve(1)
    j "Who was that?"
    a "It was my neighbor Alfred."
    j "I see. What was he doing here, if I may ask?"
    a "Oh, nothing. We just had breakfast together, talked some neighborly things through."
    a "He owns a clothing shop. He was just telling me about it."
    j "Really. That's great I guess."
    scene 31-1 morning 13 with Dissolve(1)
    "There was a bit of tension in the air."
    "John was not entirely buying Anna's story."
    if johnBeenNaked == True:
        j "I hope you aren't doing anything like that with him."
        a "Is that any of your business?"
        a "Since you've been hanging around with that girl Janine."
        scene 31-1 morning 14 with Dissolve(1)
        j "It's nothing like that, Anna."
        a "Yeah, well... Where were you tonight?"
        j "Taking care of some business."
        a "Right."
        a "Listen, I don't have time to talk about this right now. Ok?"
        j "I don't know what's up with you, Anna but you have to figure it out."
        a "So do you. I'm not your pet or anything."
        a "Perhaps what we did was just a fluke and we should forget about it."
        a "Anyway, I don't have time for this. I have to go prepare for work."
        j "Fine, Can we at least talk about this later?"
        a "We'll see."
    else:
        j "Well, whatever you are doing. It isn't really my business."
        a "Where were you last night, though?"
        j "I took out Janine. We had a nice evening."
        scene 31-1 morning 14 with Dissolve(1)
        a "Have you had any chance to check if you can help with the surgery costs?"
        j "Yes, but not much. I could spare like 10,000 or 15,000 But no more."
        a "Only? That is not enough."
        j "I'm sorry, Anna, but that's the best I can do right now."
        a "Fine, that's better than nothing, at least."
        j "Yes, it is."
        j "I'm sure you will manage the rest. Then after all this is over, we can figure out something."
        a "Anyway, I have to go prepare for work."
        j "Ok, I won't keep you."

    scene black with Dissolve(1)
    play sound door2
    scene 31-1 morning 15 with Dissolve(1)
    "Anna entered her room."
    "She thought about things for a moment."
    if johnBeenNaked == True:
        a "{i}...I can't handle him right now. He hangs around with skanks and expects me to understand."
        a "{i}...After what we've had... Ugh..."
        a "{i}...Anyway..."
    a "{i}...At least Alfred was here to relax and calm me."
    a "{i}...I should get to work..."
    if GoodBadDoctorChoice == 1:
        a "{i}...I should also visit Dr. Eilhart and check her progress in the afternoon."
        $ HospitalDayThreeEilhart = True
    else:
        a "{i}...I should also go to Dr. Schmidt later in the afternoon, he wants to continue the study... I don't know how I feel about it, though."
        $ HospitalDayThreeSchmidt = True
    play sound undress
    scene black with Dissolve(1)
    if dianaGoodRelations == False:
        if jeremySexContent == True:
            jump JeremyEventTwo
        else:
            jump JeremyEventTwoNoSex
    else:
        jump EthanEventTwo


label dayThreeMorningNone:
    a "{i}...I should get to work..."
    if GoodBadDoctorChoice == 1:
        a "{i}...I should also visit Dr. Eilhart and check her progress in the afternoon."
        $ HospitalDayThreeEilhart = True
    else:
        a "{i}...I should also go to Dr. Schmidt later in the afternoon, he wants to continue the study... I don't know how I feel about it, though."
        $ HospitalDayThreeSchmidt = True
    play sound undress
    scene black with Dissolve(1)
    "Anna changed."
    if dianaGoodRelations == False:
        if jeremySexContent == True:
            jump JeremyEventTwo
        else:
            jump JeremyEventTwoNoSex
    else:
        jump EthanEventTwo
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
