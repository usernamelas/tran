label hospitalEilhartOne:
    play sound door2
    scene black with Dissolve(1)
    scene 30-10 hospital 1 with Dissolve(1)
    "Anna knocked on the door and stepped into Cary's office and looked around for a moment."
    play sound surprise
    "Dr. Eilhart was waiting for Anna with anticipation."
    d2 "Oh, Hello, Anna. I've been waiting for you."
    d2 "How are you doing today? How are you holding up, sweety?"
    a "Hey, Doctor. I'm okay. I'm trying to keep myself preoccupied to not think about everything that has occurred."
    d2 "That is understandable."
    a "Anyway. I've made up my mind about helping you, and I'd rather not get involved with that man."
    d2 "That is a good choice, Anna. He has done some bad things in the past, therefore I wish to rid this place of him."
    scene 30-10 hospital 2 with Dissolve(1)
    a "Right, that's why I'm here."
    d2 "Ok, like I explained yesterday..."
    d2 "You have to find the documents pertaining to his illegal activities within the hospital, more specifically..."
    d2 "He has been smuggling some drugs out of the hospital and has been reselling them to drug dealers."
    d2 "A drug called buprenorphine which essentially mitigates some of the withdrawal symptoms that one might get after using opiates."
    d2 "It doesn't completely negate the effects, but it does 'help' with the withdrawal."
    d2 "It is a drug that can be prescribed only in certain circumstances, and it isn't that easy to obtain."
    scene 30-10 hospital 3 with Dissolve(1)
    d2 "The second thing is regarding the memory card for a camera."
    d2 "It holds certain pictures and videos that I wish to erase from existence."
    d2 "They are being used to blackmail me and keep me quiet. Therefore I cannot do those things myself."
    a "Oh, okay, Doctor."
    a "Might you tell me what pictures and videos does it hold?"
    d2 "I think you can already guess."
    a "Oh...I see..."
    a "I'm sorry, Doctor."
    d2 "It's okay. I really appreciate that you are helping."
    scene 30-10 hospital 4 with Dissolve(1)
    d2 "So yeah, it's really important that you don't get caught because the doctor will pull you in with his charlatan ways."
    d2 "I don't really know how you will get in, but I figure you are resourceful."
    d2 "Time is also of the essence. The sooner we get this over with, the sooner we can calm down and get the surgery on the way for Andrew."
    d2 "I would appreciate it if you didn't tell anyone about what the memory card contains."
    d2 "It's embarrassing as it is for me."
    a "Okay, doc. I will get going. The sooner we get this over with, the better."
    d2 "Yes and, Anna? Thank you..."
    a "Thank you too, Cary."
    $ GoodBadDoctorChoice = 1
    jump hospitalEilhartOneTwo
    return
label hospitalEilhartOneTwo:
    scene black with Dissolve(1)
    scene 30-10 hospital 5 with Dissolve(1)
    "Anna approached Dr. Schmidt's cabinet... Looked around."
    "She was a bit hesitant. It was illegal, but then again, hadn't she done a bunch of illegal things before?"
    "This was for the greater good."
    a "{i}...Ok, no one is looking... You got this, Anna..."
    "Anna breathed in a deep breath, thought about it for a couple of seconds, and went for it."
    scene 30-10 hospital 6 with Dissolve(1)
    with hpunch
    "The door, however, was locked..."
    "As Anna had suspected."
    a "{i}...Eh... I knew it. It was worth the try, though."
    "Anna let out a small sigh. It would have been too easy."
    scene 30-10 hospital 7 with Dissolve(1)
    stranger "The doctor is not in. He has been away for some time."
    stranger "I've been waiting here for, like, two days for him to give me some documents."
    a "That's unfortunate."
    stranger "Yeah, I'm starting to think, I will just break in and take what I need."
    a "I don't know. how will you do it?"
    stranger "I know how to pick locks..."
    a "Why are you telling me this? Aren't you worried I will report you?"
    stranger "I've been waiting for so long, I don't care anymore."
    stranger "And I'm ready to bet, that you also need something from there."
label StrangerMenu:
    menu:
        "Yeah, I think I will pass":
            $ HospitalQuestOne = 3
            stranger "Well, if you change your mind, I will be right here."
            jump hospitalEilhartOneThree
        "You know what, let's do it.":
            $ HospitalQuestOne = 5
            jump strangerBreakIn
label hospitalEilhartOneThree:
    scene 29-14 hospital corridor anna pink dress new hair with Dissolve(1)
    a "{i}...Maybe I should ask someone else or just go back to the guy..."
    menu:
        "Ask Harold for his help." if not HospitalQuestOne == 4:
            jump HaroldEventOneTwoOne
        "Go back to the stanger.":
            jump StrangerMenu
label hospitalEilhartTwo:
    play music jazzmusic
    scene black with Dissolve(1)
    "Anna had returned with both the memory card and the documents."
    scene 30-10 hospital 10 with Dissolve(1)
    play sound surprise
    with vpunch
    "To Anna's surprise, Cary was half-naked, changing into everyday clothes to leave the hospital."
    "Anna wanted to wait for a bit, let her change... Not to scare her as well."
    a "{i}...I kind of like her stockings and that back is very nice."
    a "{i}...I wonder, does she work out..."
    a "Dr. Eilhart?"
    scene 30-10 hospital 11 with Dissolve(1)
    play sound surprise2
    with vpunch
    d2 "Oh... Anna, you startled me a little bit."
    a "I'm sorry. You didn't seem to notice that I entered."
    d2 "I have a tendency of getting lost in thought sometimes. I think really hard about work and forget to pay attention to other things."
    d2 "It's a funny story, actually. I was once thinking about a patient and an upcoming surgery..."
    d2 "And I didn't pay attention to what I was doing..."
    d2 "I was at this one food place just having a snack... I had finished eating..."
    d2 "And I didn't notice that I was trying to cut the air with my fork and knife..."
    d2 "Hehe... That was an embarrassing moment... Someone heard the screeching of utensils against porcelain and kind of pointed out that I don't have anything on my plate."
    d2 "I quickly got up and left..."
    a "Haha... That's interesting..."
    d2 "Yeah, I try not to think about work much when I'm not at the hospital since I've had a couple of situations like that."
    scene 30-10 hospital 12 with Dissolve(1)
    d2 "Anyway... What do you have for me."
    a "Ok, so I got into the office, I don't think anyone noticed me..."
    d2 "That's good."
    a "The thing is I didn't really know what I was looking for, but I found a key that unlocked a cupboard."
    a "Inside I found a camera."
    d2 "Not a memory card?"
    a "No..."
    if AnnaCheckedCamera == True:
        a "But I... I couldn't help and turn on the camera and check what was inside..."
        d2 "What?"
        with vpunch
        d2 "You saw me... didn't you..."
        a "Yes, Doctor..."
        d2 "Why?.. It's embarrassing as it is for me..."
        scene 30-10 hospital 13 with Dissolve(1)
        a "I'm sorry, I just wanted to be sure it was you and I was too curious not to look."
        d2 "Well... What did you think?"
        a "I give you credit. You have some moves, girl... heh."
        d2 "Thanks."
        d2 "The issue is that it was back in the day, I won't deny that I partially enjoyed what I was doing and I knew it will help me with my career, but after some time I wanted out."
        d2 "Unfortunately the doctor didn't mention that he will be using a camera to record any of what we did."
        d2 "So then afterward he used that as blackmail material to get what he wants, be it sexual pleasures or just to get his way with anything else."
        a "I'm sorry, Cary."
        d2 "It's fine. After today, I won't have to endure this anymore."
    else:
        a "And I resisted the urge to turn it on and check what contents were inside."
        d2 "Really? Wow, thank you, Anna. I really respect that."
        scene 30-10 hospital 13 with Dissolve(1)
        a "You want to tell me what is inside?"
        d2 "Back in the day, I tried to be a much bigger career person. I was more about getting higher on the career ladder."
        d2 "Therefore, I employed all kinds of methods I wanted."
        d2 "The doctor gave me what I wanted, and in return, I gave him what he wanted."
        d2 "I won't deny that at the beginning, I also did enjoy it, but after some time, I wanted out."
        d2 "Unfortunately, the doctor didn't mention that he will be using a camera to record any of what we did."
        d2 "So then afterward he used that as blackmail material to get what he wants, be it sexual pleasures or just to get his way with anything else."
        a "I'm sorry, Cary."
        d2 "It's fine. After today, I won't have to endure this anymore."

    scene 30-10 hospital 14 with Dissolve(1)
    a "And the documents I found were just prescriptions."
    d2 "That is perfect, Anna. I wasn't sure what you should look for at the beginning, but now that you did, we have hit the jackpot."
    d2 "I will look at the prescriptions and check against the system."
    d2 "I'm pretty sure he is using old aliases and names to write off the drugs."
    d2 "He knows the system pretty well."
    d2 "If it all pans out, we will be able to incriminate him for this."
    scene 30-10 hospital 15 with Dissolve(1)
    d2 "It will not only put him behind bars for some time because he is essentially drug dealing."
    d2 "But it will also tarnish his reputation and career here. And about that, he cares much, much more."
    a "Isn't that a bit harsh?"
    d2 "Frankly, no... He has done some terrible, terrible things."
    d2 "I mean, my aspirations pale in comparison to his."
    d2 "I might have done some naughty things, but he has done some very bad things."
    a "How do you know all this?"
    d2 "I used to be his assistant back in the day."
    d2 "I knew what he did, but I could never prove it, and I couldn't have him investigated either because he had material on me that would ruin my career."
    d2 "Anyway..."
    d2 "Come here, Anna."
    scene 30-10 hospital 16 with Dissolve(1)
    d2 "I'm really, really thankful for what you've done here."
    d2 "You kind of put your neck on the line."
    a "Thank you, Cary."
    d2 "You didn't only do it for your own gain, I'm glad you helped me like this."
    a "No problem."
    a "I think it's better this way."
    d2 "It most definitely is."
    d2 "Anyway, I'm gonna get going, Let's put these in a safe place and If you don't mind, I will take the memory card."
    a "Absolutely. How long until we could see some results?"
    d2 "With clear proof that he is doing criminal activities, we will have him out of the office within the next days."
    d2 "And since I'm next in command, I will take over as acting lead until they find a replacement."
    a "I see. Well, good luck to us both then."
    d2 "Perhaps, after we get the verdict and this is all over, we could go out and have a little celebration?"
    a "I would like that, Cary."
    a "And see you, Cary."
    d2 "Thanks again, Anna... Bye."
    $ relationship_func("Dr. Eilhart Relationship +2")
    scene 30-10 hospital 17 with Dissolve(1)
    "Anna exited Cary's office and thought about everything for a moment."
    a "{i}...Ah this was quite exciting, I'm glad It went off without a hitch..."
    a "{i}...Now I should only worry about half of the money and no more doctor Badman..."
    a "{i}...Although, now I won't have any way of finding out what issues I have from that trauma..."
    a "{i}...Perhaps now that Cary will be the leading doctor, she might be able to study this condition..."
    a "{i}...I wonder where this could lead...I like her though, I should go out with her..."
    $ EilhartRelationship += 2
    jump alfredeventOne
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
