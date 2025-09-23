label JeremyHomeEventOne:
    $ renpy.music.play("audio/sounds/Purple Planet Music Chill Factor 80bpm.mp3", fadein=0.5, loop=True)
    play sound walk
    scene black with Dissolve(1)
    scene 32-14 jeremy 17 with Dissolve(1)
    "Anna had arrived at Jeremy's apartment."
    play sound door2
    scene 32-14 jeremy 1 with Dissolve(1)
    "Anna hesitantly entered the premise. She was unsure what request lay in wait for her at Jeremy's place."
    "She was immediately met with Jeremy's presence."
    j1 "Hello, Anna."
    a "He... Hey... Why have you asked for me to come?"
    if jeremySexContent == False:
        j1 "Don't worry, all in good time."
    else:
        j1 "Wait for a second! Be patient. I will tell you."
    play sound surprise
    scene 32-14 jeremy 2 with Dissolve(1)
    "Suddenly, Madison came out of nowhere."
    j1 "As I recall, you both met in my office."
    a "Yes."
    a "What are you doing here, Madison?"
    j1 "She's just... helping me with something."
    a "{i}...Why don't I like the way it sounds..."
    scene 32-14 jeremy 3 with Dissolve(1)
    m1 "I've done all that you asked of me, Jeremy."
    if jeremySexContent == False:
        j1 "That's good, very good."
    else:
        j1 "Excellent. I trust that you will have done it to the best of your abilities?"
        j1 "Otherwise, there will be some form of... Punishment..."
        m1 "I hope you will be pleased."
    j1 "Alright, then. I think it's time for you to be on your way."
    m1 "Yes, sir..."
    j1 "I need to take something from my room. Will be back in a moment."
    play sound door2
    scene 32-14 jeremy 4 with Dissolve(1)
    a "What are you doing here, Madison?"
    m1 "I... I'm helping with something..."
    a "Oh... What is it?"
    if jeremySexContent == True:
        m1 "I don't want to talk about it."
        m1 "It's... Well... No, never mind."
        menu:
            "Exactly, just do whatever he tells you to do.":
                a "Then everything will be fine."
                m1 "Oh, Really? I will make sure to do so."
                pass
            "Be careful with him. He tends to push the limits.":
                m1 "Thanks, Anna. I appreciate it."
                a "I got you, girl."
                $ MadisonBrave +=1
    else:
        m1 "Since I'm his new assistant, I have to keep track of all kinds of things."
        m1 "Including newly upcoming contract. That you both will present."
        m1 "Jeremy had an evening call with the clients, and he needed someone to bring him the documents from the office."
        a "Ahh... I see..."
    m1 "I will get going. Take care, Anna."
    a "By, Madi."
    scene 32-14 jeremy 5 with Dissolve(1)
    if jeremySexContent == True:
        "Anna could feel something off about Madison's behavior."
        "She seemed disconnected."
        "Anna wondered for a moment."
        a "{i}...I hope Jeremy didn't do anything to her..."
    else:
        "Anna could feel that Madison was tired."
        "It had been a long day for her, for sure..."
        a "{i}...Madison seemed exhausted. She will have a simple day tomorrow, though..."
        a "{i}...Since we have the contract closing..."
    play audio door2
    play audio surprise
    scene 32-14 jeremy 6 with Dissolve(1)
    "As Anna turned back, Jeremy was there... with a dress..."
    a "What's this?"
    j1 "It's a little gift. You can keep it, but there is a catch."
    j1 "You have to wear this for tomorrow's contract closing."
    a "Umm... What is the point of this?"
    scene 32-14 jeremy 7 with Dissolve(1)
    if jeremySexContent == True:
        j1 "Do not ask such futile questions."
        j1 "You will simply do as asked, and that's that."
        a "I don't think I understand..."
        j1 "And you don't have to. You are still my subordinate."
        j1 "So do as I say, and there will be no problems. I want to take advantage of your... disposition."
    else:
        j1 "Oh... Well... I don't want to sound pervy, but you look amazing."
        j1 "And I believe this would only help more with the looks."
        j1 "My plan is to take the attention of our clients away from the contract more."
        j1 "You see... They are pretty reluctant. As I've come to realize."
        j1 "Therefore, it would be good we could take advantage of your... disposition."
    scene 32-14 jeremy 8 with Dissolve(1)
    if jeremySexContent == True:
        a "But... Sir... I..."
        j1 "It's for the contract closing... You will pose as eye candy."
        j1 "That's all you need to know."
        a "Am I just some tool to you?"
        j1 "Precisely. If you cause any more ruckus, I will have to punish you. Believe me, it would be much more fun."
        j1 "However, I think you will agree that it would benefit everyone if we could guarantee the closing."
        a "I suppose..."
    else:
        a "Do I have any say in this? It almost feels like you are using me as a tool."
        j1 "Yeah, it doesn't sound good when you put it that way."
        j1 "But I have no bad intentions. I'm merely trying to play on your pluses."
        j1 "It would go a long way if you would do this for us."
        j1 "I'm certain that this would increase our chances of closing the deal."
        a "I... I guess that is a good point..."
    a "Alright, I will try it on... At least..."
    if jeremySexContent == True:
        j1 "Yes, you will..."
    else:
        a "Can you at least turn around?"
        j1 "Oh... No problem."
    play sound undress
    if jeremySexContent == True:
        scene 32-14 jeremy 9 with Dissolve(1)
        "As Anna was taking off her silky dress, Jeremy was eyeballing her."
        "She could feel the searing heat of his lust on her skin."
        "As if it was burning through."
        "The awkward tension was palpable, and so were Jeremy's intentions."
        a "I don't like when you stare."
        j1 "You will just have to deal with it. I have to examine how it looks."
    else:
        scene 32-14 jeremy 9-1 with Dissolve(1)
        "Anna felt awkward, but it wasn't as bad when she weighed the pros and cons."
        "Jeremy was also respecting her boundaries, as much as he could."
        "Anna motivated herself with the simple reason of contract closing."
        "If she could close it, she could get enough funds together to fix up Andrew."
        "And then they could resolve their issues, one way or another."
    play sound undress
    if jeremySexContent == True:
        scene 32-14 jeremy 10 with Dissolve(1)
        j1 "Wonderful body... I'm always impressed..."
        "Anna could barely keep her composure, but at least Jeremy wasn't as mean as usual."
        "Perhaps it was to do with Madison and why she was here earlier."
        a "Can you not stare, please?"
        j1 "How else would I inspect the goods."
        a "...{b}*sigh*...{/b}"
        j1 "Sorry, what?"
        a "Nothing..."
        j1 "Nothing....?"
        menu:
            "(SUB) Nothing, Master.":
                $ sub_var +=1
                a "Nothing, Master..."
                j1 "That's better, Anna."
            "(DOM) I will not say it...":
                $ dom_var +=1
                j1 "Fiesty, I like it."
    else:
        scene 32-14 jeremy 10-1 with Dissolve(1)
        "Jeremy was barely keeping himself together. He wanted to look at Anna so bad."
        j1 "I hope I don't cause you too much discomfort. But I would like you to know that you are absolutely amazing for doing this."
        a "Oh... Well... It's for the greater good, right?"
        "Anna was surprised how Jeremy was acting lately, much more tolerable."
        j1 "Right, if we close this deal, we will greatly increase our income streams."
        j1 "And you will get a nice commission for assisting the case."
    if jeremySexContent == True:
        if sub_var >= 1:
            scene 32-14 jeremy 11 with Dissolve(1)
            "Anna could feel Jeremy's presence ever-growing on her..."
            a "What are you doing?"
            j1 "It's been a while since we had fun..."
            a "Wait... This isn't right... You can't do it."
            j1 "I'm your master, I can do whatever..."
            j1 "Do you wish to get the closing bonus or not?"
            a "{i}...I need the money..."
            scene 32-14 jeremy 12 with Dissolve(1)
            a "Ok... Ok..."
            j1 "Yes... Your skin is as smooth as ever..."
            j1 "I just love groping and touching you."
            a "{i}... I feel embarrassed... But what can I do..."
            j1 "This is such a great experience for me."
            j1 "You are very hot, Anna..."
            j1 "Alright, change into the dress..."
    scene black with Dissolve(1)
    play sound undress
    scene 32-14 jeremy 13 with Dissolve(1)
    "Jeremy was impressed."
    "And so was Anna, the dress was revealing... very revealing in some areas, but it was comfortable..."
    "A little adjustments here and there, and it would a be very casual yet classy and sexy dress."
    j1 "Well, well... I rarely manage to get the right size and everything, but I've nailed it this time..."
    a "I... I don't know what to say..."
    if jeremySexContent == True:
        j1 "Say nothing... Just let me inspect this..."
        j1 "Yes... This will do nicely..."
        a "It's revealing my breasts..."
        j1 "Don't you worry your little head about it..."
        j1 "We will definitely be doing good..."
        j1 "Turn around and let me see that juicy ass of yours."
    else:
        j1 "Don't worry, it looks great on you... Will you be alright with this dress?"
        a "I... I think so. It's a bit revealing..."
        j1 "Oh... Don't worry, it's the light... When closing the contract, I don't think they will notice."
        j1 "But I think it will have the effect that I want it to have."
    scene 32-14 jeremy 14 with Dissolve(1)
    if jeremySexContent == True:
        j1 "It looks priceless, I would ask for some enjoyment of you, but I need you fresh tomorrow."
        a "{i}...I can't believe what he's putting me through..."
        a "{i}...Do I have to take it?..."
        j1 "But after that, everything's fair game. I have some big plans for you for in the future."
        a "Do I even want to know what you have in mind?"
        j1 "You don't have to want to know. You will do it if you wish to keep this excellent position."
    else:
        j1 "My apologies if I stare a bit too much."
        j1 "But you are simply exquisite..."
        a "Th... Thanks?"
        j1 "Oh, don't mind me. I'm merely remarking upon your astonishing appearance."
        a "It makes me a bit uncomfortable."
        j1 "I'm sorry."
        menu:
            "But... Thanks for being nice...":
                j1 "Oh... Don't think about it."
            "Yeah... Let's keep it professional.":
                "Anna was being a bit mean towards Jeremy."
        j1 "Anyway, You can change back into your clothes. I hope this will do fine."
    if jeremySexContent == True:
        scene 32-14 jeremy 15 with Dissolve(1)
        "Jeremy approaches Anna even closer and makes her feel his presence even more."
        j1 "Perfect fit. You, Anna, are an exquisite additional tool for our contract closing."
        a "But... How can you..."
        j1 "Don't ask such questions. Keep to your own thoughts."
        a "{i}...I don't have to take this... But I still need the cash..."
        a "{i}...Is Andrew worth the suffering?... But then again, I kind of pulled him into all of this..."
        "Anna was fighting a difficult battle in her mind whether or not being Andrew's savior was reasonable."
    play sound undress
    scene black with Dissolve(1)
    scene 32-14 jeremy 16 with Dissolve(2)
    if jeremySexContent == True:
        "Anna was rather uncomfortable but still felt some semblance and reason for taking this abuse..."
        "She needed to help Andrews surgery and resolve their issues. Her mind was slowly figuring out what to tell Andrew."
        "Meanwhile, Jeremy was, yet again, grinning in the pleasure of his success at manipulating Anna."
        a "Are we done here?"
        j1 "We are done when I say we are, but... Yes. I have what I need. You are free to go."
    else:
        "Anna didn't seem that uncomfortable since Jeremy was respecting boundaries."
        "She felt like she was being used, but she needed the money, and perhaps in the future, she could take the lead on the contract closings."
        a "So. This will do fine, right?"
        j1 "I can't even explain how perfect it is. Thank you."
        a "Are we all done here?"
        j1 "Yes, thank you, Anna. We shall meet tomorrow, be at your best."
        j1 "Take care."
        a "Bye."
    scene 32-14 jeremy 16 with Dissolve(2)
    "Anna went out of his apartment and wondered about what she's going to do next."
    if BenjaminContent == True:
        a "{i}...I think I shoud visit Benjamin, since I promised him."
        jump BenjaminEventOne
    else:
        a "{i}...I think it's time to head home..."
        jump HomeEventTwo
    scene black with Dissolve(1)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
