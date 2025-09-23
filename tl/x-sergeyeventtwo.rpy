label SergeyEventTwo:
    play music blues
    play sound walk
    scene black with Dissolve(1)
    scene 33-3 serg 2 with Dissolve(1)
    "Anna entered the Warehouse. Unsure what was to follow, but she trusted Sergey and his judgment."
    "Sergey and Michael were already there. Discussing something."
    s1 "So, I trust that you've got it handled, yes?"
    m2 "I got it, boss. I was the first to arrive so I could assess everything and do my thing."
    s1 "Great. I have something else planned for today, but you won't be leading it... Anna will."
    scene 33-3 serg 3 with Dissolve(1)
    s1 "Speaking of Anna."
    s1 "Greetings. How are you holding up?"
    a "I'm doing fine. I've had plenty of things to do to keep my mind off of all the events."
    s1 "Understandable."
    m2 "Hey, Anna. How are you doing?"
    a "Hey, Michael. I'm ok. Thanks."
    scene 33-3 serg 4 with Dissolve(1)
    "Anna leaned in for a kiss. It had been a couple of days since she felt Sergey's strong presence."
    "She felt relief when she saw him."
    s1 "It's good to see that you're ok."
    s1 "I hope the detective didn't give you too much trouble."
    scene 33-3 serg 5 with Dissolve(1)
    "Anna also leaned in to kiss Michael."
    "Michael seemed surprised but welcomed it."
    scene 33-3 serg 6 with Dissolve(1)
    s1 "{i}...Uh... I don't like that..."
    "Sergey seemed to dislike that Anna was kissing somebody else, other than him."
    "Was he starting to develop some sort of feelings for her?"
    scene 33-3 serg 7 with Dissolve(1)
    s1 "Khem... Anyway. We have a lead on a potential person of interest."
    if benjamin_var_four == True:
        play sound surprise
        a "I will stop you right there because I also have a lead."
        a "Sorry. But basically, I got some information that he might've been involved with a drug dealer."
        a "But the drug dealer is dead now, under mysterious circumstances."
        s1 "Oh? That is very interesting..."
        a "Yeah and I heard that I could find a girl who is now a hooker at the 'Black Cat' brothel in the red light district."
        s1 "Huh. You've done some research, I see. Well done, Anna."
        s1 "Well, you will have to follow up on that lead, though."
        a "Why is that?"
        s1 "We are well known around the underground. If we tried to talk with people about some dead drug dealer, everyone would just run and hide."
    else:
        s1 "Basically, you'd have to go to the red light district and talk to some of the people, ask around."
        s1 "I've heard stories that Earl might've been involved in the killing of someone. I'm not sure who, but you have to find out."
        a "Ok. But why me?"
        s1 "Well, as you know, we are into some dealings, and people know about us, whoever might know something, will go into hiding fast."
        a "I see."
    scene 33-3 serg 8 with Dissolve(1)
    s1 "Ok, Michael, go ahead and deliver the stash we talked about."
    s1 "I will explain some details to Anna real quick."
    m2 "Rog, Boss. It was a pleasure to meet you, Anna."
    a "Bye, Michael."
    scene 33-2 serg 9 with Dissolve(1)
    s1 "Like I was saying..."
    s1 "They are all assholes, but money makes them talk almost always, so use it."
    s1 "I will cover whatever you pay them."
    s1 "We will also be available on call at any moment, so you don't have to worry about any issues."
    s1 "If you think something suspicious is going on. Call us straight away."
    scene 33-2 serg 10 with Dissolve(1)
    a "Ok, I got it."
    a "I will be back as soon as I have something."
    s1 "Thank you for this, Anna. We might obtain some info that would help us get rid of Detective Mendoza."
    stop music fadeout 2
    jump RedDistrictQuestionOne
    return
label RedDistrictQuestionOne:
    play sound walk
    play music PPMEtheralEternity
    scene black with Dissolve(1)
    "She went to the Red Light District..."
    scene 33-4 red 3 with Dissolve(1)
    "Anna approached a girl who was waiting on the corner."
    ho1 "Hey, sweety. Would you like to have some one-on-one lesbian action?"
    ho1 "I could eat you out like a pot of honey..."
    a "Umm, no thanks. I'm here on business."
    ho1 "Oh, you work here? I've never seen you here. Are you the new girl?"
    scene 33-4 red 4 with Dissolve(1)
    menu:
        "Anna plays it deceptively.":
            a "Yeah, I'm one of the new girls. Just started. I was wondering if you could give me some pointers."
            a " Are there any people I should be aware of? I've heard some stories about a cop..."
            ho1 "Oh... You're talking about that... Well, I shouldn't tell you, but since you are one of us..."
            ho1 "Some cop had killed a drug dealer some time back, later one of the girls joined us and told us that she used to be together with a drug dealer."
            ho1 "And that she would avenge his death one day. I think she is just some crackhead..."
            ho1 "I'm sorry, that's all I can tell you. If you want to know more, you have to find the girl."
            ho1 "Just be careful of cops in general..."
            a "Thanks, hon. I really appreciate your help!"
            $ sergey_var_three = True
            pass
        "Anna is honest.":
            a "I'm sorry, I'm not. I just thought that you could help me with some questions."
            ho1 "No. No way. You will get me in trouble. Please go away..."
            pass
    scene black with Dissolve(1)
    jump RedDistrictQuestionTwo
    return
label RedDistrictQuestionTwo:
    $ renpy.music.play("audio/sounds/City Of Angels.mp3", fadein=2)
    scene black with Dissolve(1)
    "Anna decided to approach another person in the Red Light District."
    scene 33-4 red 5 with Dissolve(1)
    play sound surprise
    a "Hello."
    ho2 "Heyyyy there, girl. You're looking dashingly fine."
    ho2 "I'm very, very interested in what you'd want with me... hehe..."
    scene 33-4 red 6 with Dissolve(1)
    ho2 "I mean... I rarely see such beauties here. They've definitely stepped up the game this time."
    ho2 "What you've got, how much you cost, honey?"
    a "I'm sorry? What?"
    ho2 "Yeah, time is money, I know. How much do you cost?"
    scene 33-4 red 7 with Dissolve(1)
    a "I'm not a hooker..."
    ho2 "Yeah, right. Funny joke..."
    a "I'm serious."
    ho2 "Then you must be out of your mind walking around here like that."
    scene 33-4 red 8 with Dissolve(1)
    ho2 "But I like crazy. It's my type, hehe..."
    ho2 "So, perhaps we could have a little bit of that crazy fun, eh?"
    a "I'm not sure I follow."
    ho2 "Oh, come on. You've got to want something if you came all the way here, dressed like that."
    a "Yeah, I wanna know about a drug dealer that was shot and killed. I know that his girlfriend works here now."
    ho2 "You are definitely crazy asking about this."
    play sound surprise
    scene 33-4 red 9 with Dissolve(1)
    ho2 "I know something about that..."
    ho2 "But damn girl, you've got some nice tits..."
    a "Wha? What are you doing?"
    a "Can you help me with some questions or not?"
    ho2 "Yes... Questions. I'd like to question your titties myself."
    scene 33-4 red 10 with Dissolve(1)
    a "Hey. You are very touchy. I don't think I like it."
    ho2 "Well, just tell me to stop, and I will think about it."
    ho2 "Can't pass up an opportunity like this."
    ho2 "You are a 10 out of 10. Rare beauty, god damn."
    scene 33-4 red 11 with Dissolve(1)
    a "Ok, dude. Stop!"
    a "I'm not some random hooker or some nympho."
    a "I'm not going to 'service' you."
    a "I just need some information, can you give it to me or not?"
    scene 33-4 red 12 with Dissolve(1)
    ho2 "In that case, I will be on my way."
    ho2 "You are just some dumb girl..."
    ho2 "Dressing like that, seeking attention but not willing to do anything. ridiculous."
    ho2 "You play a dangerous game, but what do I know. You don't give me anything. I won't tell you anything."
    play sound surprise
    scene 33-4 red 13 with Dissolve(1)
    a "What?"
    ho2 "I don't need dead weight. I'm leaving."
    "Anna realized that maybe she actually needs to make a deal with the man."
    "The information could be useful to her."
    play sound surprise
    scene 33-4 red 14 with Dissolve(1)
    $ config.menu_include_disabled = True
    a "Ok, ok. wait."
    a "Perhaps I was a bit overboard with the idea."
    a "Maybe we can make a deal?"
    ho2 "Oh, so now you wanna talk. Alright, I'll bite."
    ho2 "You either give me some tongue action or 500 bucks. and I will tell you whatever you wanna know."
    menu:
        "Anna chooses to give the man what he wants (If Corruption > 35)" if AnnaCorruption > 35:
            a "Fine, I will give you what you really want."
            ho2 "That's what I like to hear. Alright!"
            $ AnnaCorruption +=1
            $ corruption_func("Anna Corruption +1")
            jump RedDistrictSexOne
        "Anna decides to give him 500 $ of her own money for the info.":
            scene 33-4 red 15-1 with Dissolve(1)
            a "Ok, here. I will give you those 500 bucks, and you tell me what you know."
            ho2 "It wouldn't be my first choice, but alright. Money is money."
            ho2 "And you are still on the top of my list of girls I want."
            a "Good to know..."
            scene 33-4 red 17-1 with Dissolve(1)
            ho2 "There used to be this one girl I fucked all the time here, she loved to talk."
            ho2 "You didn't hear this from me, but there was a cop."
            ho2 "He killed some drug dealer. I think he was Russian or something."
            a "Wait, what?"
            ho2 "Yeah. related to some other Russian criminal."
            ho2 "The murder was never solved and the circumstances were shady. If someone did solve it, I bet you would get some dirt on the cop who killed the drug dealer."
            ho2 "The dead drug dealer's girlfriend used to work at the Black Cat, but now she hangs out at the Park at night."
            ho2 "She is a drug addict, so getting some info out of her will be hard unless you can get her a fix."
            ho2 "Her name is Gianna. If you meet her and convince her, she will know more."
            a "Thanks. That's helpful."
            a "I will get going now..."
            $ MoneyVar -=500
            $ sergey_var_four = True
            jump RedDistrictQuestionTwoEnding
label RedDistrictSexOne:
    scene 33-4 red 15 with Dissolve(1)
    ho2 "Well, well. I like where this is going."
    a "You better come through, afterward."
    ho2 "Oh, I shall, if you give me good head."
    ho2 "Come on, get on your knees and give some of them lips."
    scene 33-4 red 16 with Dissolve(1)
    "Anna went down low and wondered if this was the right choice."
    "But regardless, there was no turning back."
    a "{i}...I hope he can tell me what I want to know..."
    ho2 "{i}...This girl is nuts, but I like here... Crazy and sexy."
    scene 33-4 red 16-1 with Dissolve(1)
    ho1 "Damn, that girl is really going down to his dick."
    ho1 "That's kinda hot..."
    "The hooker wondered about who Anna was..."
    if sergey_var_three == True:
        ho1 "She said that she is one of the new girls. Looks like she is very good at her work."
    play sound undress
    scene 33-4 red 17 with Dissolve(1)
    "She pulled the man's flaccid penis out of his pants."
    ho2 "Oh, yeah... Stroke, it now."
    a "Alright, alright... I'll do what you want me to."
    ho2 "I love when women say that..."
    ho2 "Pull your breasts out more."
    play sound undress
    scene 33-4 red 18 with Dissolve(1)
    "Anna undressed her breasts and left them exposed."
    "The man was looking at them with lustful eyes. Couldn't keep them off of her tits."
    a "Like that?"
    ho2 "Damn. Your puppies are amazing. Fucking luscious."
    scene 33-4 red 19 with Dissolve(1)
    "During that time, the man's penis had become extremely erect, and it was looking Anna directly in her face."
    ho2 "Well, come on. It won't suck itself, now will it."
    a "{i}...I just have to do it if it helps get rid of that detective..."
    a "You want me to lick your penis?"
    ho2 "Yeah! Suck my cock!"
    play sound jerk2
    scene 33-4 red 20 with Dissolve(1)
    "Anna started to lick on his tip with slow and hesitant movements."
    ho2 "Take your time, I'm in no rush... Hehe..."
    ho2 "Better late than never, This slow teasing makes it just that much better."
    a "Mff... Mhm..."
    "Anna tried not to think about what she was doing right now."
    scene 33-4 red 21 with Dissolve(1)
    "The patron grabbed Anna by her head and started to thrust in and out at a slow pace."
    "Not even giving Anna a moment's rest. He kept increasing the speed."
    "Anna was at his mercy."
    a "{i}...Shit, he's going faster and faster."
    ho2 "Damn girl, your mouth, it's... Ahh... Really damn good..."
    play sound jerk
    scene 33-4 red 22 with Dissolve(1)
    "Anna couldn't talk. Her mouth was full of the man's dick."
    "He enjoyed the blowjob ..."
    ho2 "Damn, I would come here all the time if you worked here..."
    a "Mfff... Ahh... Mhh..."
    "The muffled moans could be heard down the street. The sound her mouth was making was echoing through the buildings."
    scene 33-4 red 23 with Dissolve(1)
    "He pushed his cock deep down Anna's throat. With no hesitation."
    "And Anna didn't protest. She just took that dick."
    ho2 "Damn. Almost my full length, that's impressive. Ahhhhh..."
    "Anna was struggling to get some air because the dick filled her oral cavity up entirely."
    play sound jerk3
    show RLDSexOne with Dissolve(1)
    "The patron was fucking Anna's face with no intention of stopping until he shoots his load."
    a "Mhh... {b}*Gulp*{/b}..."
    "Anna was choking on his hard cock. Barely able to keep herself from vomiting all over it."
    ho2 "Fuck... Take my dick!!"
    show RLDSexTwo with Dissolve(1)
    hide RLDSexOne
    "He was starting to go faster and faster approaching a climax."
    "Ready to explode in Anna's mouth with all his might."
    ho2 "Shiit... This is amazing! Fucking unbelievable. Your mouth is so good!"
    ho2 "Suck it... Ah... I'm about to come!!!"
    "Anna had no control of the situation. She was at his mercy."
    scene 33-4 red 24 with Dissolve(1)
    "He pushed his cock in Anna's face and felt that there was no turning back."
    "His cum was just waiting at the tip already."
    "Anticipating the perfect moment to receive his load, Anna started to lick his dick with her tongue while it was in her mouth."
    "Sending him over the edge..."
    play sound jerk3
    scene 33-4 red 25 with flash
    ho2 "Oh, Shit... Fuuck."
    with flash
    ho2 "Here I come!!! AAHHH!"
    with flash
    with flash
    ho2 "This is FANTASTIIICC!!!!"
    "YEEAAHH I'm shooting my load in yo mouth!! AhHH"
    with flash
    "The man was shooting streams of his ejaculate in her, already full, mouth."
    play sound jerk2
    scene 33-4 red 26 with Dissolve(1)
    a "AAhhh..."
    "Anna was gasping for breath. She almost blacked out from that interaction..."
    ho2 "Hot damn... I'm fucking drained. My balls are empty..."
    ho2 "You have to come here more often. I would pay you for a good fuck."
    a "Yeah, I don't know..."
    scene 33-4 red 27 with Dissolve(1)
    "Anna had swallowed most of the cum, but there was some still left on her lips and face."
    a "This is so much. My stomach is full of your cum..."
    ho2 "Well, I'm glad I could feed you."
    ho2 "I'm impressed. You are not even throwing up. You do this often?"
    a "What? NO! Definitely not..."
    ho2 "Riight."
    scene 33-4 red 28 with Dissolve(1)
    a "Well, Can you tell me anything about that drug dealer?"
    ho2 "Sure, sure. I'm pretty known around these parts."
    ho2 "Can never satiate my lust."
    ho2 "There used to be this one girl I fucked all the time here. She loved to talk."
    ho2 "You didn't hear this from me, but there was a cop."
    ho2 "He killed some drug dealer. I think he was Russian or something."
    a "Wait, what?"
    ho2 "Yeah. related to some other Russian criminal."
    ho2 "The murder was never solved, and the circumstances were shady. If someone did solve it, I bet you would get some dirt on the cop who killed the drug dealer."
    ho2 "The dead drug dealer's girlfriend used to work at the Black Cat, but now she hangs out at the Park at night."
    ho2 "She is a drug addict, so getting some info out of her will be hard unless you can get her a fix."
    ho2 "Her name is Gianna. If you meet her and convince her, she will know more."
    a "Thanks. That's helpful."
    a "I will get going now..."
    scene 33-4 red 29 with Dissolve(1)
    ho2 "I will be here usually if you want some more 'info' or just some fun. find me..."
    a "Yeah... Right..."
    a "{i}...You wish..."
    a "{i}...I still feel the cum filled feeling. Jeez..."
    a "{i}...Time to head back to Sergey's and tell him the news."
    $ sergey_var_four = True
    jump RedDistrictQuestionTwoEnding
label RedDistrictQuestionTwoEnding:
    hide screen disableClick
    play music PPMAwakening
    scene 33-4 red 30 with Dissolve(1)
    "Anna had gotten the intel and was heading back to Sergey's."
    a "{i}...Something doesn't add up... The drug dealer was Russian and was related to some other Russian?"
    a "{i}...Could it be Sergey..."
    a "{i}...That would turn things around heavily..."
    scene 33-4 red 31 with Dissolve(1)
    "Anna was going back to Sergey's and typing him a message about the news."
    "It would really move things forward, but..."
    "She was looking at her phone and didn't even notice two men were standing in front of her."
    f1 "Hey, beauty... Wanna have some fun?"
    a "Sorry, I'm not working here."
    f1 "Come on, Anna..."
    play sound surprise2
    play music tense
    scene 33-4 red 32 with Dissolve(1)
    f1 "Long time no see, eh?"
    a "What??? How... Why..."
    f1 "Are you surprised? It was clear I escaped. Haha..."
    f1 "Don't tell me you thought that we wouldn't come after you..."
    a "I... I..."
    play sound lighthit
    scene 33-4 red 33 with vpunch
    f1 "Enough bullshitting..."
    f1 "We've been looking for you. Visited your 'boyfriend' at the hospital. Oh, he will want to know what you've been up to."
    f1 "Anyway... We have something important to discuss... So..."
    f1 "Let's talk..."
    play sound deepimpact
    scene black
    $ config.menu_include_disabled = False
    jump FitzEventOne
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
