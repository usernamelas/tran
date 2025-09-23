label madisonEthanOne:
    play sound walk
    scene black with Dissolve(1)
    scene 31-3 jeremy 11 with Dissolve(1)
    a "Hey, Madison, we didn't have much time to get acquainted. Do you have a moment now?"
    m1 "Absolutely, Ethan showed me everything, and we already finished up."
    a "That fast? I'm impressed."
    m1 "Perhaps my previous work experience is rubbing off. Hehe..."
    a "Hehe... Perhaps."
    a "Anyway. I wanted to know more about you..."
    m1 "Sure, ask away."
    default MadisonMenuThree1 = False
    default MadisonMenuThree2 = False
    menu madisonmenu3:
        "How did you end up getting this job?" if MadisonMenuThree1 == False:
            m1 "Well, I was looking to get out of my previous workplace."
            m1 "It was not what I was looking for."
            m1 "Plus there was workplace harassment."
            a "Oh. I'm sorry about that."
            m1 "Well, I'm not weak, but I know that I don't have to take a beating."
            a "That's true."
            m1 "Anyway, this seemed promising, has a good salary and nice benefits on top of that."
            a "Oh, Yeah. I can't argue with that."
            a "Plus we have also kind of solved the workplace harassement. We used to have an issue with that."
            m1 "Is it something to do with that Jeremy, that Ethan mentioned?"
            a "Well, yeah. But I won't get into the details now."
            m1 "Ok, sure."
            m1 "Anyway, That's how it went."
            $ MadisonMenuThree1 = True
            jump madisonmenu3
        "Tell me a bit more about yourself." if MadisonMenuThree2 == False:
            m1 "Well. I'm originally from here, The Suncity."
            m1 "I've been living here my entire life, traveled a lot."
            m1 "Went through school, like the usual lot."
            m1 "Finished studies at Suncity Business and Economics college."
            m1 "Decided not to go for an MBA and just try to climb the corporate ladder on my own."
            a "Have you succeeded?"
            m1 "Well, a little, But I've since changed job's a couple of times during the years."
            a "I see, anything exciting like hobbies?"
            m1 "Well, I like to play chess in my free time. I'm a part of the local chess club."
            m1 "I also like to play visual novels in my free time. They are sometimes very intriguing."
            a "Really? I could never get myself in those. Perhaps I should try?"
            m1 "Yes, They are fun. You can also find some more erotic ones if you wish."
            m1 "There is this one about this girl who moves to a new city..."
            a "Right, Perhaps let's continue this some other time. Haha..."
            a "Don't want any colleague to hear us."
            m1 "Hehe... Sure."
            $ relationship_func("Madison Relationship +1")
            $ MadisonRelationship += 1
            $ MadisonMenuThree2 = True
            jump madisonmenu3
        "That's all.":
            jump madisonEthanOneTwo
    return
label madisonEthanOneTwo:
    scene 31-3 jeremy 18 with Dissolve(1)
    a "Anyway, it was nice talking with you."
    m1 "Likewise, Anna."
    a "I was going to go for lunch now and thought that maybe you want to join me?"
    m1 "Oh, Sorry, Anna. It would be my pleasure, but not today. I want to set up all my shortcuts and get some work done. I still have to get used to your systems."
    a "Oh... Well, alright, no problem. Just next time you HAVE to come to lunch with me... Hehe..."
    m1 "Sure, Anna."
    "Anna decided to invite Timothy to lunch."
    $ GlossaryUnlockMadison = True
    jump timothyEventTwo
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
