label SexShopEventOne:
    play music tranquility
    $ renpy.sound.play("audio/sounds/city_traffic.mp3", fadein=1)
    scene black with Dissolve(1)
    play audio surprise
    scene 32-13 adult 1 with Dissolve(1)
    e "There is my favorite girl!"
    a "Hey... Hehe..."
    a "What made you decide to come looking for this kind of a place?"
    e "Well, I've been a bit 'lonely' if you know what I mean. Thought that I could get something to skip the time."
    a "Ah... I see haha..."
    scene 32-13 adult 1-1 with Dissolve(1)
    e "Hey! This is no laughing matter. Serious business. Haha."
    a "Right. Well, since I'm here, I might go in, as well."
    e "Sure. Hopefully, it won't be some creepy sex dungeon or something."
    a "It isn't. I've been there."
    e "Well, aren't you a fun one?"
    stop sound fadeout 1
    play audio door2
    scene 32-13 adult 2 with Dissolve(1)
    e "Soo, where is everybody?"
    a "Usually there is a girl at the main desk. I don't know where she is now."
    play sound lighthit
    e "Wait, did you hear that?"
    a "I did. Must be coming from one of the rooms."
    e "Remember what I told you about the sex dungeon?"
    a "It's not. Haha... I think..."
    scene 32-13 adult 3 with Dissolve(1)
    e "Well... Perhaps they're just sorting stuff..."
    e "Meanwhile, look at all the choices. It's amazing how many variations there often are."
    a "Yeah... Crazy."
    a "But I don't know if I'm going to get anything. I don't need any."
    e "Yeah. Right. I know why, girl. Haha..."
    play audio door2
    play audio surprise
    scene 32-13 adult 4 with Dissolve(1)
    r2 "I have customers! Just do it yourself."
    r2 "Put them according to colors together!"
    e "Oh. There's someone."
    a "That's Ruby."
    scene 32-13 adult 5 with Dissolve(1)
    r2 "Hello, Anna! I'm sorry for keeping you waiting."
    r2 "And I see that you've brought a friend this time?"
    r2 "A new collection of assortment of toys and other 'accessories' has arrived."
    r2 "Now, what can I do you for?"
    e "So, It's my first time here and I was wondering what you could offer me?"
    r2 "First timer, eh? You never forget your first, haha."
    scene 32-13 adult 6 with Dissolve(1)
    r2 "Well. From MY extensive experience, it's good to dive in depending on what makes you comfortable."
    r2 "At first. It's to test out the waters. Then as you become more seasoned at penetrating that pussy... Well..."
    r2 "Then you can move onto bigger and more fun things. Haha..."
    r2 "My colleague in the other room sorting our stuff is... A man of acquired tastes."
    r2 "And he advises our more 'freaky' clients. So, when you get to that level, I will introduce you to him."
    scene 32-13 adult 7 with Dissolve(1)
    e "What did I say about the sex dungeon. Haha..."
    r2 "Oh... Have you already been here?"
    e "No. I was just joking with Anna in hopes that this isn't one."
    a "I've never known that there was one, though."
    r2 "No problem, it's for our higher echelon of patrons, so to speak."
    r2 "If you are ever interested, I can get you in contact with our owner. He manages that part of our business."
    play sound surprise
    scene 32-13 adult 8 with Dissolve(1)
    r2 "Anyway, this is the collection that I advise for our up-and-coming clients."
    e "Wow, a nice collection. And... that's a double penetration dildo..."
    menu:
        "Anna remembers about her experience with Ruby.":
            $ ruby_sex_content = True
            $ AnnaCorruption +=1
            $ corruption_func("Anna Corruption +1")
            r2 "Anna, you remember our fun times, don't you?"
            a "Umm... Haha... Let's move on."
        "Anna seems to have no prior experience with this.":
            $ ruby_sex_content = False
            a "Alright...."
    r2 "You said... That you are an amateur. I pulled this out just for the sake of presentation."
    r2 "Buuut... It seems that you already know your stuff."
    scene 32-13 adult 9 with Dissolve(1)
    e "I will take it."
    r2 "Oh? I like your style, girl. This one is very flexible and very, very natural."
    r2 "I've used this product before on occasion. It's very good when you have two girls one on top of another and..."
    a "OK. That's enough stories. Haha..."
    scene 32-13 adult 10 with Dissolve(1)
    e "Sure, I will take this. I've been meaning to experiment a bit."
    a "Emily. I didn't know you had it in you."
    e "What? Girls just wanna have fun. No?"
    a "No judgment from me."
    r2 "Great, will you take anything else?"
    scene 32-13 adult 11 with Dissolve(1)
    e "I will also take this vibrator. It's a simple one and my old one broke after a... Freak accident."
    r2 "Ah, yes. I've got plenty of those, if you ever wish to expand your theory!"
    e "Thanks for now, Haha..."
    r2 "Great, That will be all?"
    e "Yes."
    play sound undress
    scene 32-13 adult 12 with Dissolve(1)
    r2 "That will be $56.99."
    r2 "And I hope to see you, two gorgeous ladies, here again soon."
    r2 "You would be such a great addition to our group of 'friends'."
    a "Yeah. I don't know about that one. But thanks."
    e "I will reserve my judgment for now, though."
    e "Thank you and have a good one."
    play audio door2
    $ renpy.sound.play("audio/sounds/city_traffic.mp3", fadein=1)
    scene 32-13 adult 13 with Dissolve(1)
    e "Wow. That was... An interesting chick."
    a "Yeah, she is very... Open about her sexuality."
    e "Maybe you could learn a thing or two from her."
    a "Oh, you would know. Haha..."
    e "Anyway, I have to run now. Will see you at work soon honey. And... I think we should celebrate soon."
    a "Celebrate what?"
    e "Oh nothing... My aunt's, son's, wives', cat's birthday. Do we need a reason?"
    a "I guess not. Haha... See you!"
    stop sound fadeout 1
    jump VibratorFirstTime
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
