image ep10_035 = Movie(play="video/episode10/035.webm", image="images/episode10/035.webp", loop = False)
image ep10_043 = Movie(play="video/episode10/043.webm", loop = True)
image ep10_044 = Movie(play="video/episode10/044.webm", loop = True)
image ep10_045 = Movie(play="video/episode10/045.webm", loop = True)
image ep10_049 = Movie(play="video/episode10/049.webm", loop = True)
image ep10_050 = Movie(play="video/episode10/050.webm", loop = True)
image ep10_051 = Movie(play="video/episode10/051.webm", loop = True)
image ep10_052 = Movie(play="video/episode10/052.webm", loop = True)
image ep10_053 = Movie(play="video/episode10/053.webm", loop = True)
image ep10_054 = Movie(play="video/episode10/054.webm", loop = True)
image ep10_109 = Movie(play="video/episode10/109.webm", image="images/episode10/109.webp", loop = False)
image ep10_117 = Movie(play="video/episode10/117.webm", loop = True)
image ep10_118 = Movie(play="video/episode10/118.webm", loop = True)
image ep10_119 = Movie(play="video/episode10/119.webm", loop = True)
image ep10_120 = Movie(play="video/episode10/120.webm", image="images/episode10/120.webp", loop = False)
image ep10_124 = Movie(play="video/episode10/124.webm", loop = True)
image ep10_125 = Movie(play="video/episode10/125.webm", loop = True)
image ep10_126 = Movie(play="video/episode10/126.webm", loop = True)
image ep10_127 = Movie(play="video/episode10/127.webm", loop = True)
image ep10_128 = Movie(play="video/episode10/128.webm", loop = True)
image ep10_129 = Movie(play="video/episode10/129.webm", loop = True)
image ep10_158 = Movie(play="video/episode10/158.webm", image="images/episode10/158.webp", loop = False)
image ep10_220 = Movie(play="video/episode10/220.webm", image="images/episode10/220.webp", loop = False)
image ep10_284 = Movie(play="video/episode10/284.webm", image="images/episode10/284.webp", loop = False)
image ep10_285 = Movie(play="video/episode10/285.webm", image="images/episode10/285.webp", loop = False)
image ep10_286 = Movie(play="video/episode10/286.webm", image="images/episode10/286.webp", loop = False)

label episode10:
    $ progress = 130
    stop music fadeout 4.0
    scene expression ("images/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(2, 4) with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_newEpisode


    if charlotte_path:
        $ unlockImage(persistent.charlotte_17)

    call episode10_denise from _call_episode10_denise

    if charlotte_path:
        call episode10_book from _call_episode10_book

    if toby_job == 0:
        call episode10_realEstate from _call_episode10_realEstate
    else:
        call episode10_club from _call_episode10_club

    scene expression ("images/episode8/199.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/200.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if patricia_path:
        call episode10_trisChores from _call_episode10_trisChores
    else:
        call episode10_shower from _call_episode10_shower

    call episode10_sheila from _call_episode10_sheila

    call episode10_fight from _call_episode10_fight

    if charlotte_path:
        call episode10_nightCharlotte from _call_episode10_nightCharlotte
    else:
        call episode10_nightAlone from _call_episode10_nightAlone

    call episode10_end from _call_episode10_end

    return

label episode10_denise:
    $ progress = 131
    show screen ui_message("Friday") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message

    scene expression ("images/episode10/001.webp") with dissolve
    denise "Are you sure you can't take me to the train station? Your [mom]'s driving skills are... Well... You know what I mean. She has no skills whatsoever."
    toby "She's not that bad. After all, she drove me back and forth to school for years and I still have both arms and legs."
    scene expression ("images/episode10/002.webp") with dissolve
    if denise_path:
        denise "Maybe, but that doesn't mean you're completely healthy."
        denise "There is something wrong with your head, dear. Why else would you buy your [aunt] sexy lingerie and flirt with her?"
        toby "Do you really think [mom]'s driving is at fault here?"
        if emma_break == False:
            denise "Of course. What else? I mean we both know you're not lacking for pussy."
        else:
            denise "Either that or maybe you're not getting enough pussy."

        scene expression ("images/episode10/003_laugh.webp") with dissolve
        toby "If [mom] hears you talking like that she won't let you stay with us next week."
    else:

        denise "Well, that's a relief. But you still need to have your head examined."
        scene expression ("images/episode10/003_normal.webp") with dissolve
        toby "If I have mental issues it's because [mom] and [dad] argue nearly every day, not because of her driving skills."
        scene expression ("images/episode10/004_laugh.webp") with dissolve
        denise "You mean lack of driving skills."
        scene expression ("images/episode10/003_laugh.webp") with dissolve
        toby "Careful, she might hear you and then she won't let you stay with us next week."

    if emma_break == False:
        scene expression ("images/episode10/004_flirty.webp") with dissolve
        denise "The walls in your house are really thin, so if she lets you live under the same roof after what you did last night, I'm sure she'll let me stay here next week too."
        scene expression ("images/episode10/003_surprised.webp") with dissolve
        toby "Shit! You're messing with me right?"
        scene expression ("images/episode10/004_laugh.webp") with dissolve
        denise "Maybe...Maybe not, but I'm pretty sure your girlfriend won't be able to sit properly for a few days."
        scene expression ("images/episode10/003_ashamed.webp") with dissolve
        toby "Fuck... Do you think [mom] heard us?"
        if patricia_path:
            scene expression ("images/episode10/004_smile.webp") with dissolve
            denise "Don't worry. She didn't, but someone else might have. I only heard because I went to the bathroom to check up on Tris because she was gone for like 10 minutes."
            scene expression ("images/episode10/003_surprised.webp") with dissolve
            toby "Shit! She heard us?"
            scene expression ("images/episode10/004_laugh.webp") with dissolve
            denise "Who knows? Maybe she did, maybe she didn't."
    else:

        scene expression ("images/episode10/004_laugh.webp") with dissolve
        denise "I'm sure she loves having me here."
        scene expression ("images/episode10/003_laugh.webp") with dissolve
        toby "Except for when you make fun of her weight."
        scene expression ("images/episode10/004_smile.webp") with dissolve
        denise "So what? She needed a little push, she's gotten lazy."

    scene expression ("images/episode10/004_curious.webp") with dissolve
    denise "So I don't suppose I can convince you to come with us to the train station?"
    scene expression ("images/episode10/003_laugh.webp") with dissolve
    toby "Sadly, no. Unfortunately, someone has to work in this house."
    scene expression ("images/episode10/004_smile.webp") with dissolve
    denise "I like your [family]. It's very traditional. The men go to work to provide for the [family] while the women stay home getting bored."
    if patricia_path and charlotte_path:
        scene expression ("images/episode10/003_flirty.webp") with dissolve
        toby "And buying expensive stuff. The women in this [family] have expensive tastes."
    elif patricia_path:
        scene expression ("images/episode10/003_flirty.webp") with dissolve
        toby "Tris has expensive tastes and [dad] doesn't give her spending money."
        scene expression ("images/episode10/004_laugh.webp") with dissolve
        denise "Yet she cleans your room for that money."
        scene expression ("images/episode10/003_laugh.webp") with dissolve
        toby "She needs to learn the value of money."
    elif charlotte_path:
        scene expression ("images/episode10/003_flirty.webp") with dissolve
        toby "Someone needs to take care of [mom] since [dad] isn't doing so well."
    else:
        scene expression ("images/episode10/003_laugh.webp") with dissolve
        toby "Yeah. I was raised to treat women right."

    if denise_path:
        scene expression ("images/episode10/004_flirty.webp") with dissolve
        denise "And how can I join the [family] with all these rights? I've never had a sugar daddy."
        scene expression ("images/episode10/003_laugh.webp") with dissolve
        toby "Or sugar [nephew]."
        scene expression ("images/episode10/004_laugh.webp") with dissolve
        $ unlockImage(persistent.denise_04)
        denise "You make it sound so dirty. I'm way past needing a sugar daddy, but joining your [family] to at least get some of your attention could be fun."
    else:
        scene expression ("images/episode10/004_laugh.webp") with dissolve
        denise "Where do I sign up?"
    scene expression ("images/episode10/003_smile.webp") with dissolve
    toby "Well... For starters you need to stick around more than just a couple days."
    scene expression ("images/episode10/004_curious.webp") with dissolve
    denise "Wouldn't you get tired of me?"
    scene expression ("images/episode10/003_laugh.webp") with dissolve
    toby "How could I? You're the coolest [aunt] ever."
    scene expression ("images/episode10/004_cool.webp") with dissolve
    denise "It's not like I have any competition."
    scene expression ("images/episode10/003_smile.webp") with dissolve
    toby "You know [dad] has a [sister] too, right?"
    scene expression ("images/episode10/004_laugh.webp") with dissolve
    denise "That old hag couldn't compete with me in a Cool Contest."
    scene expression ("images/episode10/003_smile.webp") with dissolve
    toby "So that means next week you'll stay longer?"
    scene expression ("images/episode10/004_laugh.webp") with dissolve
    denise "I'll have to run it by your [mother] first."
    scene expression ("images/episode10/005.webp") with dissolve
    charlotte "Run what by me?"
    scene expression ("images/episode10/006.webp") with dissolve
    toby "If she can stay with us more than two days next week."
    scene expression ("images/episode10/005.webp") with dissolve
    charlotte "Only if she stops making fun of my belly."
    scene expression ("images/episode10/007.webp") with dissolve
    denise "Belly? What belly? You have the body of a Greek goddess."
    scene expression ("images/episode10/008.webp") with dissolve
    charlotte "You can stay with as long as you like."
    scene expression ("images/episode10/009.webp") with dissolve
    denise "I guess I'll be sticking around a little longer next week."
    scene expression ("images/episode10/010.webp") with dissolve
    charlotte "OK, it's time. Let's go."
    scene expression ("images/episode10/011.webp") with dissolve
    denise "Let me at least say goodbye to my favorite [nephew]."
    if denise_path:
        scene expression ("images/episode10/010.webp") with dissolve
        charlotte "You're only saying that so he'll buy you more clothes."
        scene expression ("images/episode10/011.webp") with dissolve
        denise "Be a good girl and wait for me in the car."
        scene expression ("images/episode10/012.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        if ep8_denise_lingerie:
            denise "Thank you for everything, especially that sexy lingerie."
            toby "It was my pleasure."
            denise "Oh, I'm sure of that."
        else:
            denise "Thank you for everything, dear."
            toby "No problem."
    else:
        scene expression ("images/episode10/013.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        denise "Take care of your [mom] and [sister]."
        toby "You know I will."

    scene expression ("images/episode10/014.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/015.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    return

label episode10_book:
    $ progress = 132
    scene expression ("images/episode10/309.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/310.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/311.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}No... I shouldn't. I shouldn't read her book. After all it's her only way of expressing her frustrations.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It's just like a journal or diary. It's her way of expressing what she feels. It's just a novel. It's not real.{/i}"
    scene expression ("images/episode10/312.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Ugh! Damn it.... I need to know. I hope [mom] won't be pissed at me for reading it.{/i}"
    scene expression ("images/episode10/313.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What she doesn't know can't hurt her.{/i}"
    scene expression ("images/episode10/314.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}OK, where did we leave off... If I remember correctly it was just after [aunt] Denise, or Esined or whatever she calls her gave the waiter [mom]'s phone number.{/i}"
    scene expression ("images/episode10/315.webp") with dissolve

    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Alone. Again. Looks like my husband has already left for work.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I understand that he has to work. I don't mean to don't sound ungrateful. But a woman needs more than just money.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Anyway. I think I'll go for a morning jog. Hopefully it'll help me forget about my frustrations.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wonder what time it is. It looks early.{/i}"
    scene expression ("images/episode10/316.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Two new messages. From unknown number.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Could that be him? The sexy waiter?{/i}"
    scene expression ("images/episode10/317_texting.webp") with dissolve
    call sms_incoming ("unknown", "Good morning, beautiful. I hope you have a wonderful day because you deserve it, and don't you dare let anyone ruin it for you.") from _call_sms_incoming_169
    call sms_incoming ("unknown", "Just so you know, before you get pissed at me, I knew it was safe to text you because I saw him this morning. I was jogging while he was going to work. I think we live in the same neighborhood.") from _call_sms_incoming_170
    scene expression ("images/episode10/318.webp") with dissolve
    hide screen message
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What should I do? I can't reply, can I?{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But I want to. It feels so nice to be appreciated and his message was sweet.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... Why does this have to be so hard.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}OK, I'll just thank him for his text and wish him a good day also. There's nothing wrong with that.{/i}"
    scene expression ("images/episode10/317_texting.webp") with dissolve
    call sms_sent ("unknown", "Good morning, to you too. I hope you have a great day, hopefully as good as mine.") from _call_sms_sent_132
    hide screen message
    scene expression ("images/episode10/319.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why does this feel so wrong? Am I a bad wife?{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What's wrong with me? I love my husband.{/i}"
    scene expression ("images/episode10/320.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think.{/i}"
    scene expression ("images/episode10/317_texting.webp") with dissolve
    call sms_incoming ("unknown", "It will be now.") from _call_sms_incoming_171
    call sms_sent ("unknown", "Should I be flattered?") from _call_sms_sent_133
    call sms_incoming ("unknown", "I don't know. Did you make the coffee that put this smile on my face? Because that is the reason my day got better.", img_icon="images/episode10/321_icon.webp", img="images/episode10/321.webp") from _call_sms_incoming_172
    call sms_sent ("unknown", "How could I make you a coffee and be pissed at you at the same time.") from _call_sms_sent_134
    call sms_incoming ("unknown", "I don't believe you. You're way too cool to be pissed at me.") from _call_sms_incoming_173
    call sms_sent ("unknown", "Do I not look pissed?", img_icon="images/episode10/322_icon.webp", img="images/episode10/322.webp") from _call_sms_sent_135
    call sms_incoming ("unknown", "Now my day is all of a sudden really, really great. I don't think it could get any better than this.") from _call_sms_incoming_174
    call sms_sent ("unknown", "Let me guess. You bought yourself a croissant.") from _call_sms_sent_136
    call sms_incoming ("unknown", "Well, yes. But no, I'm talking about your gorgeous eyes.") from _call_sms_incoming_175
    call sms_sent ("unknown", "I would say \"Thank you\", but I'm still mad at you.") from _call_sms_sent_137
    call sms_incoming ("unknown", "Are you coming to the restaurant later today?") from _call_sms_incoming_176
    call sms_sent ("unknown", "I don't know. Why?") from _call_sms_sent_138
    call sms_incoming ("unknown", "So I can apologize for being an ass.") from _call_sms_incoming_177
    call sms_sent ("unknown", "On your knees?") from _call_sms_sent_139
    call sms_incoming ("unknown", "I'm not going to propose to you. I'll just be asking for forgiveness.") from _call_sms_incoming_178
    call sms_sent ("unknown", "I'll think about it.") from _call_sms_sent_140
    call sms_incoming ("unknown", "That's all I ask.") from _call_sms_incoming_179
    call sms_incoming ("unknown", "That and when do you think you'll be coming?") from _call_sms_incoming_180
    call sms_sent ("unknown", "I'm not saying. It'll be a surprise.") from _call_sms_sent_141
    call sms_incoming ("unknown", "I was wrong. My day can get better.") from _call_sms_incoming_181
    call sms_incoming ("unknown", "See you later.") from _call_sms_incoming_182
    call sms_sent ("unknown", "Bye!") from _call_sms_sent_142
    call sms_incoming ("unknown", "Hmmm...No emojis. You must be really pissed.") from _call_sms_incoming_183

    scene expression ("images/episode10/319.webp") with dissolve
    hide screen message
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What am I doing? Why did I say I'd go? I can't go. That's foolish.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should call Esined.{/i}"
    scene expression ("images/episode10/323.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Come on... Pick up.{/i}"
    scene expression ("images/episode10/324.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Hey, [sis]. I need your help.{/i}"
    denise_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Something wrong?{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Everything is wrong. I'm going to kill you.{/i}"
    denise_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Let me guess. He called you?{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Nope. We're texting now.{/i}"
    denise_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Look at you, high school girl. Texting!{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I'm going to kill you.{/i}"
    denise_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}So, what's wrong? You're just texting. Nothing's happening. It's not like you're going to see him.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Yeah... About that.{/i}"
    denise_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}No way...{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Yes way. And you're coming with me.{/i}"
    denise_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Look. I love you, but I don't think I'm ready for a threesome.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Ha ha. You're coming with me to make sure I don't do anything stupid.{/i}"
    denise_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Are you that desperate that you actually trust me?{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Yes... I don't want to be alone with him. Maybe with you around he'll be too afraid to flirt. I don't know.{/i}"
    denise_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}If you don't want him to flirt with you, bring your husband.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Bitch.{/i}"
    denise_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Fine... Meet you there at eight?{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Okay. And don't you dare be late.{/i}"
    denise_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Okay, okay... Don't worry. I'll be there.{/i}"

    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message

    scene expression ("images/episode10/325.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit, shit, shit... She's still not here and he's over there looking at me so smiley.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'll just tell him that this is wrong. We can't do this and then leave. I'll ask him to delete my number and that will be the end of it.{/i}"
    scene expression ("images/episode10/326.webp") with dissolve
    waiter "Wow... You look great."
    charlotte_ "You don't look so bad either."
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}No, no, no... That was NOT what I was supposed to say.{/i}"
    scene expression ("images/episode10/327.webp") with dissolve
    $ toby_ = reverse_name(toby)
    toby_ "I'm [toby_!c], by the way."
    scene expression ("images/episode10/332.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Wait, what?!?! That's my name. Is this fantasy really about me? Does my [mom] have a fantasy about me?{/i}"
    scene expression ("images/episode10/328_1.webp") with dissolve
    charlotte_ "Nice to meet you. Ettola Rahc."
    scene expression ("images/episode10/328_2.webp") with dissolve
    toby_ "You have a beautiful name."
    scene expression ("images/episode10/329.webp") with dissolve
    charlotte_ "And you must have a great boss for letting you do nothing but wait for married women to come by the restaurant."
    toby_ "He doesn't have a say in what I do on my day off."
    scene expression ("images/episode10/330_1.webp") with dissolve
    charlotte_ "Oh. Your day off? And how did you know when I would be here?"
    scene expression ("images/episode10/330_2.webp") with dissolve
    toby_ "I didn't. I came here right after we texted. I didn't want to miss my chance to talk to you."
    scene expression ("images/episode10/330_1.webp") with dissolve
    charlotte_ "But that was nearly 12 hours ago."
    scene expression ("images/episode10/330_2.webp") with dissolve
    toby_ "I would say it was worth the wait."
    scene expression ("images/episode10/331.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}God. He's so sweet. Nobody has ever been this good to me.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I want to kiss him so badly. He's just perfect.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Look at those eyes, that nose. God, those lips.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wanna kiss his lips.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What's wrong with me? Why do I want to kiss him so badly?{/i}"

    scene expression ("images/episode10/332.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Wait, what? That's it? Looks like that's as far as she's gotten so far.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hold on. There's something scribbled at the bottom like a footnote.{/i}"
    toby "{size=12}{color=#FDCA6E}* reading *{/color}{/size}\n{i}\"God. Why is he so perfect. Why is he so good to me? He's so sweet and caring. He's my [son]! I can't think about him like this, but he makes me feel so loved and wanted.\"{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Wow... I don't know what to say...{/i}"
    if toby_job == 0:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit. I'm going to be late for work.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck. I'm going to be late for work.{/i}"
    scene expression ("images/episode10/333.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}There is no denying it now. [mom!c] is writing a fantasy novel about me. What am I going to do?{/i}"

    return

label episode10_realEstate:
    $ progress = 133
    scene expression ("images/episode10/016.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/017.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/018.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()


    scene expression ("images/episode10/019.webp") with dissolve
    toby "Hey, boss! What's with the serious face?"
    darlene "Before I answer, I just want to let you know that I think you're a great asset to the company and if you need help with anything in the future, all you have to do is ask."
    scene expression ("images/episode10/020_curious.webp") with dissolve
    toby "What are you talking about? What's going on?"
    scene expression ("images/episode10/021_normal.webp") with dissolve
    darlene "On the table is a paper you have to sign and in the envelope are the profits you'd make for your apartments once we sell them."
    scene expression ("images/episode10/020_normal.webp") with dissolve
    toby "You're firing me?"
    if darlene_path:
        scene expression ("images/episode10/021_sad.webp") with dissolve
        darlene "Look, [toby!c]. It's not like I want to, but after what happened here the other day, I have no choice."
        scene expression ("images/episode10/021_normal.webp") with dissolve
        darlene "All I'm asking is that you sign that piece of paper and forget about what happened. In return you get 15k."
        scene expression ("images/episode10/020_sad.webp") with dissolve
        toby "You think I need money to keep quiet about that?"
        scene expression ("images/episode10/021_normal.webp") with dissolve
        darlene "I've known you for two months now and to be honest, I don't think you're the kind of guy who'd ruin my reputation for money. But in my experience, money always wins."
        scene expression ("images/episode10/021_sad.webp") with dissolve
        darlene "That's why I'm being more than fair here. If you want to continue to work in this industry I will absolutely put a good word for you."
        scene expression ("images/episode10/020_normal.webp") with dissolve
        toby "I don't want that and I don't need your money. I don't want anything in exchange for my silence. If you want me to sign something that I won't ruin your reputation or try to extort you for money, I'll gladly sign it."
        scene expression ("images/episode10/021_surprised.webp") with dissolve
        darlene "Umm..."
        scene expression ("images/episode10/020_normal.webp") with dissolve
        toby "But I don't want to leave. I like this job and I like working for you. I have so much more to learn from you."
        scene expression ("images/episode10/021_angry.webp") with dissolve
        darlene "For fuck sake, [toby!c]! Why do you have to make this complicated? Just take the money and forget about all of it!"
        scene expression ("images/episode10/020_angry.webp") with dissolve
        toby "I don't want your money."
        scene expression ("images/episode10/020_signing.webp") with dissolve
        toby "There, I signed it."
        scene expression ("images/episode10/020_normal.webp") with dissolve
        toby "Now I can't tell anyone about whatever the hell it was that happened. If you want to fire me, then fire me. But don't you dare try to buy my silence with money."
        scene expression ("images/episode10/021_sad.webp") with dissolve
        darlene "Why are you so stubborn about this? You're going to need money till you find a new job."
        scene expression ("images/episode10/020_normal.webp") with dissolve
        toby "You taught me that patience is the most important part of this industry. And that sometimes you work, work, work and the reward is still out there, but you have to wait."
        scene expression ("images/episode10/020_smile.webp") with dissolve
        toby "Well in this case, the apartments I'm working are still on the market, so we have to wait."
        scene expression ("images/episode10/021_normal.webp") with dissolve
        darlene "Now you're just being stupid! I'm going to fire you and you'll have nothing."
        scene expression ("images/episode10/022.webp") with dissolve
        toby "Then all I can say is that it was a pleasure working for you."
        scene expression ("images/episode10/023.webp") with dissolve
        darlene "Wait, don't leave. At least let me explain why I have to let you go."
        scene expression ("images/episode10/024.webp") with dissolve
        darlene "What we did the other day was wrong. I have never cheated on Kat ever. But from now on every time I see you, I will remember that I cheated on her. I feel guilty."
        darlene "And the scary part isn't the fact that I gave you a blowjob, but the fact that I wanted to, because that's how those things work."
        scene expression ("images/episode10/025_normal.webp") with dissolve
        toby "You keep explaining to me how those drugs work, but if you knew so much, why did you offer them to me in the first place?"
        scene expression ("images/episode10/026_guilty.webp") with dissolve
        darlene "I know about the drugs because sometimes me and Kat use them to spice things in the bedroom, but I never knew that they made a chocolate version."
        scene expression ("images/episode10/025_normal.webp") with dissolve
        toby "I see."
        scene expression ("images/episode10/026_normal.webp") with dissolve
        darlene "Anyway, like I was saying, I have to let you go because I don't want to ever cheat on Katrina again."
        scene expression ("images/episode10/025_curious.webp") with dissolve
        toby "I thought you had to let me go because I remind you of what we did?"
        scene expression ("images/episode10/026_guilty.webp") with dissolve
        darlene "That too."
        scene expression ("images/episode10/026_normal.webp") with dissolve
        darlene "Look, it's complicated."
        scene expression ("images/episode10/026_angry.webp") with dissolve
        darlene "Why the hell didn't you just take the money and leave? Why do you had to stick around and play the nice guy card?"
        scene expression ("images/episode10/025_laugh.webp") with dissolve
        toby "Because, believe it or not. I am a nice guy."
        scene expression ("images/episode10/026_smile.webp") with dissolve
        darlene "You are, that's why I don't want to let you go."
        scene expression ("images/episode10/025_normal.webp") with dissolve
        toby "Then don't."
        scene expression ("images/episode10/026_normal.webp") with dissolve
        darlene "If you promise me that what happened the other day will never happen again."
        scene expression ("images/episode10/025_laugh.webp") with dissolve
        toby "As long as you don't drug me or jerk me off, I'll be a good lad."
        scene expression ("images/episode10/026_laugh.webp") with dissolve
        darlene "Yeah, I need to explain about that one too."
        scene expression ("images/episode10/025_smile.webp") with dissolve
        toby "Yeah I think it would be nice."
        scene expression ("images/episode10/026_smile.webp") with dissolve
        darlene "You remember how I told you that sometimes me and Kat use that to spice things up in the bedroom? Well, not only in the bedroom."
        scene expression ("images/episode10/025_flirty.webp") with dissolve
        toby "Someone is being naughty in the office?"
        scene expression ("images/episode10/026_laugh.webp") with dissolve
        darlene "Don't make it sound so dirty, but yeah. I pay the rent for this office so I can do whatever I want."
        scene expression ("images/episode10/025_laugh.webp") with dissolve
        toby "Sounds fair."
        scene expression ("images/episode10/026_normal.webp") with dissolve
        darlene "Anyway, the thing is you came up minutes after she left and I was pretty much under the influence, but I promise you I will be more careful from now on."
        scene expression ("images/episode10/026_sad.webp") with dissolve
        darlene "And if I do something like this one more time, you take your money and leave."
        scene expression ("images/episode10/027.webp") with dissolve
        toby "Deal."
        label memory_33:


            scene expression ("images/episode10/028.webp") with dissolve

            toby "God, you're beautiful!"
            scene expression ("images/episode10/029.webp") with dissolve
            darlene "You really think so?"
            toby "Yes."
            scene expression ("images/episode10/030.webp") with dissolve
            darlene "What are you doing to me, [toby!c]?"
            toby "I'm not doing anything."
            scene expression ("images/episode10/031.webp") with dissolve
            darlene "So... Before we get to work we need to make some ground rules here."
            scene expression ("images/episode10/032.webp") with dissolve
            darlene "You and I will not be a thing. I am your boss, and you'll never look at me in a funny way."
            scene expression ("images/episode10/033.webp") with dissolve
            toby "And you'll never drug me so you can suck my cock."
            scene expression ("images/episode10/034.webp") with dissolve
            darlene "You mean this cock? I wouldn't even touch it."
            show ep10_035
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode10/035.webp") with dissolve
            hide ep10_035
            toby "And we will never kiss each other like this ever again."
            scene expression ("images/episode10/036.webp") with dissolve
            darlene "And I will never try to undress you."
            scene expression ("images/episode10/037.webp") with dissolve
            toby "Me neither."
            scene expression ("images/episode10/038.webp") with dissolve
            toby "And I will never, I mean never, unhook your bra so I can see your beautiful small breasts."
            scene expression ("images/episode10/039.webp") with dissolve
            darlene "And even if the bra is unhooked I will never take it down, like this."
            scene expression ("images/episode10/040.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode10/041.webp") with dissolve:
                yalign 0.0
                linear 10.0 yalign 1.0

            darlene "I want you so bad!"
            toby "I feel you!"
            scene expression ("images/episode10/042.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            darlene "This is the last time I'm sucking your cock!"

            scene expression ("images/episode10/043.webp") with dissolve
            show ep10_043
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck... This feels so good.{/i}"
            $ ui.saybehavior()
            $ ui.interact()
            hide ep10_043

            scene expression ("images/episode10/044.webp") with dissolve
            show ep10_044
            $ ui.saybehavior()
            $ ui.interact()
            hide ep10_044

            scene expression ("images/episode10/045.webp") with dissolve
            show ep10_045
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I want to fuck her so bad right now.{/i}"
            $ ui.saybehavior()
            $ ui.interact()
            hide ep10_045

            scene expression ("images/episode10/046.webp") with dissolve:
                yalign 0.0
                linear 10.0 yalign 1.0
            toby "God... I want more than just a blowjob. I want to fuck you."

            scene expression ("images/episode10/047.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            darlene "Take me here on the table."

            scene expression ("images/episode10/048.webp") with dissolve:
                xalign 1.0
                linear 10.0 xalign 0.0

            toby "Oh, believe me I will."

            scene expression ("images/episode10/049.webp") with dissolve
            show ep10_049
            darlene "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nGod! You're so big."
            $ ui.saybehavior()
            $ ui.interact()
            darlene "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYour cock feels so good inside me. I forgot how good a real cock feels."
            hide ep10_049

            scene expression ("images/episode10/050.webp") with dissolve
            show ep10_050
            $ ui.saybehavior()
            $ ui.interact()
            darlene "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nYes, yes, yes! Don't stop."
            hide ep10_050

            scene expression ("images/episode10/051.webp") with dissolve
            show ep10_051
            darlene "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck me, [toby!c]. Give it to me. Fuck me hard."
            $ ui.saybehavior()
            $ ui.interact()
            darlene "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes... Yes... YES!"
            darlene "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nTake me from behind."
            hide ep10_051

            scene expression ("images/episode10/052.webp") with dissolve
            show ep10_052
            darlene "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck I feel so dirty. I love your cock."
            $ ui.saybehavior()
            $ ui.interact()
            hide ep10_052

            scene expression ("images/episode10/053.webp") with dissolve
            show ep10_053
            darlene "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes, yes... Right there. Don't stop."
            darlene "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nGod! You're big!"
            $ ui.saybehavior()
            $ ui.interact()
            hide ep10_053

            scene expression ("images/episode10/054.webp") with dissolve
            show ep10_054
            darlene "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes, yes, yes..."
            darlene "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI'm going to cum. Don't stop."
            toby "I'm going to cum too."
            darlene "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nPlease don't stop."
            toby "I can't hold it anymore."
            darlene "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nDon't stop."
            toby "I'm going to cum inside you."
            darlene "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck... Cum inside then, but don't you dare stop."
            hide ep10_054

            scene expression ("images/episode10/055.webp") with dissolve:
                yalign 0.0
                linear 10.0 yalign 1.0

            toby "I'm cumming."
            with flash
            with flash
            darlene "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes... Me too!"

            $ unlockImage(persistent.darlene_07)
            scene expression ("images/episode10/055_1.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode10/056.webp") with dissolve
            darlene "God, that felt so good."
            toby "Please tell me you're not under the influence of that stuff?"
            darlene "Don't worry. I don't need any drugs to know that I needed you to fuck my brains out."
            scene expression ("images/episode10/057.webp") with dissolve
            darlene "This was a one time thing. Okay?"
            toby "Are you sure?"
            darlene "We have work to do. We can't have sex in the office like two animals. We have responsibilities."
            toby "Okay then. Next time I'll ask you out first and then we'll see what happens."
            scene expression ("images/episode10/058.webp") with dissolve
            darlene "Get dressed and get back to work."
            $ unlockMemory(persistent.memory_33)
            $ renpy.end_replay()
    else:

        scene expression ("images/episode10/021_sad.webp") with dissolve
        darlene "Look [toby!c]. It's not that I want to, but I feel so strange to be around you, after I asked to give you a blowjob."
        scene expression ("images/episode10/021_normal.webp") with dissolve
        darlene "All I'm asking of you is to sign that piece of paper and forget about that and in return you get 15k."
        scene expression ("images/episode10/020_curious.webp") with dissolve
        toby "You're basically paying me to stay silent, not to ruin your reputation."
        scene expression ("images/episode10/021_sad.webp") with dissolve
        darlene "Maybe."
        scene expression ("images/episode10/020_normal.webp") with dissolve
        toby "Look. I don't need your money to stay silent. You've done so much for me. I don't need anything in exchange."
        scene expression ("images/episode10/020_signing.webp") with dissolve
        toby "Here. I'm signing this and I don't need your money. You thought me so much and I think you're the best boss I could have."
        scene expression ("images/episode10/020_smile.webp") with dissolve
        toby "I have grown to care for you, so I would never do anything to ruin your reputation."
        scene expression ("images/episode10/021_surprised.webp") with dissolve
        darlene "But I tried to..."
        scene expression ("images/episode10/020_normal.webp") with dissolve
        toby "But nothing... Nothing happened and nothing will. I understand you were drugged and it's not your fault, so I don't see a need for to you have to pay for anything."
        scene expression ("images/episode10/021_sad.webp") with dissolve
        darlene "Thank you [toby!c]."
        scene expression ("images/episode10/020_smile.webp") with dissolve
        toby "No worries. So? What do I have to do today?"
        scene expression ("images/episode10/021_smile.webp") with dissolve
        darlene "Are you sure? 15k is a lot of money."
        scene expression ("images/episode10/020_normal.webp") with dissolve
        toby "I haven't earned it yet. I will make so much more."
        scene expression ("images/episode10/021_laugh.webp") with dissolve
        darlene "In that case, what are you still doing here? Get back to work."

    scene expression ("images/episode10/059.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    show screen ui_message("Some time later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message

    scene expression ("images/episode10/060.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/061.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    play sound "audio/fx/notification_5.mp3"
    scene expression ("images/episode10/062.webp") with dissolve
    if sheila_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}A message from Sheila. I completely forgot about our date.{/i}"
        scene expression ("images/episode10/062_texting.webp") with dissolve
        call sms_incoming ("sheila", "Hey sexy. Ready for tonight?", img_icon="images/episode10/063_icon.webp", img="images/episode10/063.webp") from _call_sms_incoming_184
        call sms_sent ("sheila", "Hey sexy. Of course. I just need to wrap up some things at work, take a quick shower and I'll come pick you up.") from _call_sms_sent_143
        call sms_incoming ("sheila", "Cool. I'm waiting.") from _call_sms_incoming_185
        call sms_incoming ("sheila", "By the way, don't forget about the thing.") from _call_sms_incoming_186
        call sms_sent ("sheila", "Fine. I won't.") from _call_sms_sent_144
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Sheila? I wonder what she wants.{/i}"
        scene expression ("images/episode10/062_texting.webp") with dissolve
        call sms_incoming ("sheila", "Hi there. What's up?") from _call_sms_incoming_187
        call sms_sent ("sheila", "Nothing much, just wrapping up some work things.") from _call_sms_sent_145
        call sms_incoming ("sheila", "Cool.") from _call_sms_incoming_188
        call sms_incoming ("sheila", "About what we discussed yesterday, were you able to come through?") from _call_sms_incoming_189
        call sms_sent ("sheila", "Not yet, but I'm working on it.") from _call_sms_sent_146
        call sms_incoming ("sheila", "Thanks, man. By the way, I just finished with my last client, do you think you can come to my place with the stuff if you get it?") from _call_sms_incoming_190
        call sms_sent ("sheila", "Sure.") from _call_sms_sent_147
        call sms_incoming ("sheila", "Cool. Thanks!") from _call_sms_incoming_191
        call sms_sent ("sheila", "See you later") from _call_sms_sent_148

    hide screen message
    scene expression ("images/episode10/064.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I need to ask Darlene if she has any chocolates left.{/i}"
    scene expression ("images/episode10/065.webp") with dissolve
    if darlene_path:
        toby "Umm... I have a strange question."
        scene expression ("images/episode10/066.webp") with dissolve
        darlene "Okay?"
        scene expression ("images/episode10/065_2.webp") with dissolve
        toby "Do you happen to have more chocolates?"
        scene expression ("images/episode10/067.webp") with dissolve
        darlene "I told you dear. That was a one time thing."
        scene expression ("images/episode10/065_2.webp") with dissolve
        toby "A girl told me that she wants to try this drug called \"The Hooker\", which by her description sounds like the chocolate we had the other day and I told her I'll try to get her some."
        scene expression ("images/episode10/067.webp") with dissolve
        darlene "What a stallion. Am I not enough for you?"
        scene expression ("images/episode10/068.webp") with dissolve
        toby "You said it yourself. That was a one time thing, so..."
        scene expression ("images/episode10/066.webp") with dissolve
        darlene "Let me call Kat!"
    else:
        toby "Sorry to bother you ma'am, but I have a strange question."
        scene expression ("images/episode10/066.webp") with dissolve
        darlene "Is everything all right?"
        scene expression ("images/episode10/065_2.webp") with dissolve
        toby "A friend of mine told me about this drug called \"The Hooker\", which seems very similar to the one you told me about and I was wondering if you have any left?"
        scene expression ("images/episode10/066.webp") with dissolve
        darlene "Sorry dear, but I threw out the box, but if you want I can call Kat."
        scene expression ("images/episode10/065_2.webp") with dissolve
        toby "If it's not too much."
    $ progress = 134
    scene expression ("images/episode10/069.webp") with dissolve
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Hi dear. How's work?{/i}"
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Yeah. It's a busy day.{/i}"
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}By the way, someone dear to us wants to have fun with his girlfriend and wants to spice things up in the bedroom.{/i}"
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Yeah... Or living room. Who knows with kids these days.{/i}"
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Put it on my tab.{/i}"
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Yeah, yeah. See you tonight.{/i}"
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    scene expression ("images/episode10/070.webp") with dissolve
    darlene "She's waiting for you in her club. I'll send you the address."
    scene expression ("images/episode10/071.webp") with dissolve
    toby "Do you know how much it is for a box?"
    scene expression ("images/episode10/070.webp") with dissolve
    darlene "Yes I do, but for you it's on the house."
    scene expression ("images/episode10/071.webp") with dissolve
    toby "You didn't have to."
    scene expression ("images/episode10/070.webp") with dissolve
    darlene "Don't worry. It's fine."
    darlene "By the way, if she asks you how you know about the chocolates you tell her that I was eating her present and was telling you about how cool this chocolate is."
    darlene "Whatever you do, don't tell her about us."
    scene expression ("images/episode10/071.webp") with dissolve
    toby "Okay. Thank you very much."
    scene expression ("images/episode10/072.webp") with dissolve
    darlene "No worries and have fun tonight."
    scene expression ("images/episode10/073.webp") with dissolve
    toby "I will."
    scene expression ("images/episode10/074.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()


    scene expression ("images/episode10/075.webp") with dissolve
    bodyguard "Where the fuck do you think you're going? The club is closed."
    toby "I have to pick something up from Katrina."
    bodyguard "It's Mrs. Katrina and she didn't tell me anything about it. So beat it."
    toby "Look man, just ask your boss."
    bodyguard "Fuck off... I have my orders not to disturb her."
    toby "My boss just talked to her a few minutes ago and told me to come here and pick something up."
    bodyguard "The couriers don't use the front door."
    bodyguard "I'll take you to Mrs. Katrina, but if you're lying to me, then I'll have your balls on a stick."
    scene expression ("images/episode10/076.webp") with dissolve
    toby "What are you doing, man?"
    bodyguard "Making sure you don't have any weapons. I don't trust you."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I knew that Katrina was crazy, but she might be crazier than I thought.{/i}"
    scene expression ("images/episode10/077.webp") with fade
    bodyguard "Sorry ma'am. This guy says you were expecting him."
    scene expression ("images/episode10/078.webp") with dissolve
    katrina "[toby!c]. How I've missed you! Sorry I forgot to tell Neal that you were coming."
    katrina "You can leave us now."
    scene expression ("images/episode10/079.webp") with dissolve
    neal "Yes ma'am."
    scene expression ("images/episode10/080.webp") with dissolve
    katrina "So? You wanna have fun tonight?"
    toby "Umm... Yeah."
    scene expression ("images/episode10/081.webp") with dissolve
    katrina "How the fuck do you know what my product does? Did you and Darlene have fun?"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}\"My product\"? Is she the one that developed this drug?{/i}"
    katrina "Careful. My hand is on your dick, so if you're lying to me I'm going to crush your little nuts."
    toby "No ma'am. I didn't touch the chocolate. She ate it alone and started telling me how you two like to spice things up in the bedroom, so I wanted to give it a try."
    katrina "Is that your final answer?"
    toby "Yes."
    scene expression ("images/episode10/082.webp") with dissolve
    katrina "If you lied to me, have fun tonight, because that's the last time you'll use that cock of yours."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the hell have I gotten myself into?{/i}"
    scene expression ("images/episode10/083.webp") with dissolve
    katrina "Here. You don't know where you got it from. Understood?"
    toby "Yes ma'am."
    katrina "And if I were you, I'd let your partner eat more. It's cooler to see how desperate she is for your cock."
    toby "Ummm... Thank you."

    scene expression ("images/episode10/084.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    return

label episode10_club:
    $ progress = 133
    scene expression ("images/episode10/016.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/085.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/086.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}That's strange. Katrina told me she's waiting for me in the office, but she's not here.{/i}"

    scene expression ("images/episode10/087.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I guess I'll have to wait for her.{/i}"


    scene expression ("images/episode10/088.webp") with dissolve
    if sheila_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}A message from Sheila.{/i}"
        scene expression ("images/episode10/088_texting.webp") with dissolve
        call sms_incoming ("sheila", "Hey sexy. I hope you didn't forget about tonight.") from _call_sms_incoming_192
        call sms_sent ("sheila", "Tonight? What happens tonight?") from _call_sms_sent_149
        call sms_incoming ("sheila", "Why do you always have to act so tough.") from _call_sms_incoming_193
        call sms_sent ("sheila", "Don't worry, sexy. I didn't forget about our date.") from _call_sms_sent_150
        call sms_sent ("sheila", "Nor the gift.") from _call_sms_sent_151
        call sms_incoming ("sheila", "That's what I wanted to hear.") from _call_sms_incoming_194
        call sms_incoming ("sheila", "See you tonight, then.", img_icon="images/episode10/089_icon.webp", img="images/episode10/089.webp") from _call_sms_incoming_195
    else:

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}A message from Sheila. I wonder what she wants.{/i}"
        scene expression ("images/episode10/088_texting.webp") with dissolve
        call sms_incoming ("sheila", "Hi man. What's up?") from _call_sms_incoming_196
        call sms_sent ("sheila", "Hi Sheila. Nothing much. I just got to work.") from _call_sms_sent_152
        call sms_incoming ("sheila", "Just now? You have a pretty damn easy job, if you ask me.") from _call_sms_incoming_197
        call sms_sent ("sheila", "Then I won't!") from _call_sms_sent_153
        call sms_incoming ("sheila", "Lol. By the way, did you get it?") from _call_sms_incoming_198
        call sms_sent ("sheila", "Not yet, but I'm working on it.") from _call_sms_sent_154
        call sms_incoming ("sheila", "Cool. I'm finishing work a bit early today, do you think you can drop it off after work? I'll be home.") from _call_sms_incoming_199
        call sms_sent ("sheila", "Just send me the address and I'll swing by.") from _call_sms_sent_155
        call sms_incoming ("sheila", "Cool. Thanks, man!") from _call_sms_incoming_200

    hide screen message

    scene expression ("images/episode10/090.webp") with dissolve
    katrina "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nI'M GOING TO KILL THAT SON OF A BITCH."
    scene expression ("images/episode10/091.webp") with dissolve
    $ renpy.music.set_volume(0.5, channel="music")
    $ renpy.music.set_volume(1.5, channel="sound")
    play sound "audio/fx/gunshot.mp3"
    katrina "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nWHO THE FUCK DOES HE THINK HE IS."
    scene expression ("images/episode10/092.webp") with dissolve
    play sound "audio/fx/gunshot.mp3"
    katrina "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nHE THINKS HE CAN TALK TO ME LIKE THAT AND NOTHING WILL HAPPEN."
    scene expression ("images/episode10/093.webp") with dissolve
    play sound "audio/fx/gunshot.mp3"
    katrina "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nI FUCKING HATE RICH FAT FUCKERS."
    scene expression ("images/episode10/094.webp") with dissolve
    play sound "audio/fx/gunshot.mp3"
    katrina "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nI'M GOING TO KILL THAT PIECE OF SHIT WHILE HE JERKS HIMSELF OFF THINKING ABOUT SOME RANDOM BOY."
    scene expression ("images/episode10/095.webp") with dissolve
    play sound "audio/fx/gunshot.mp3"
    katrina "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nOR GIRL, OR WHATEVER HE'S INTO. I DON'T GIVE A FUCK!"
    scene expression ("images/episode10/096.webp") with dissolve
    play sound "audio/fx/gun_snaps.mp3"
    $ renpy.music.set_volume(1.0, channel="music")
    $ renpy.music.set_volume(1.0, channel="sound")
    katrina "Stupid piece of shit!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This is bad. I never saw Katrina this mad. Lucky for me she's out of bullets.{/i}"
    scene expression ("images/episode10/097.webp") with dissolve
    katrina "When did you get here?"
    toby "A few minutes ago."
    katrina "And why didn't you say anything."
    toby "I didn't want to end up switching places with that wall."
    scene expression ("images/episode10/098.webp") with dissolve
    katrina "You're smarter than you look."
    if katrina_path:
        label memory_34:


            scene expression ("images/episode10/099.webp") with dissolve
            katrina "So? You're here to apologize?"
            toby "Not really. I came because you asked me to."
            scene expression ("images/episode10/100.webp") with dissolve
            katrina "Is that your final answer?"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fucking hell, the gun is so hot. She's going to burn my skin.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}At least she doesn't have any bullets left.{/i}"
            toby "Yes. I'm not going to apologize for something that isn't my fault. So you asked me to come and I came. What's going on?"
            scene expression ("images/episode10/101.webp") with dissolve
            katrina "I asked you to come here, because I need someone to lick my asshole and I figured you might want to, since you liked my pussy so much."
            katrina "It's inches away. Basically is the same pose."
            scene expression ("images/episode10/102.webp") with dissolve
            toby "Sorry, but if you really want to feel my saliva on your arse, all I can do is spit on this fucking gun and then you can shove it up your ass."
            scene expression ("images/episode10/103.webp") with dissolve
            katrina "Open your fucking mouth."
            scene expression ("images/episode10/104.webp") with dissolve
            katrina "You were saying?"
            toby "I said shove your gun in your ass."
            katrina "Careful motherfucker. I'm very close to shooting your brains out."
            toby "Then fucking shoot!"
            scene expression ("images/episode10/105.webp") with dissolve
            toby "You just pull this thing and it's done."
            katrina "You're on thin ice here boy, don't make me, because I will shoot you."
            scene expression ("images/episode10/106.webp") with dissolve
            toby "What's wrong scaredy cat?"
            toby "You don't want to shoot me? You like me that much?"
            katrina "You have no idea what I want."
            toby "Believe me, I do."
            scene expression ("images/episode10/107.webp") with dissolve
            katrina "What do I want?"
            toby "You want me to take control of you!"
            scene expression ("images/episode10/108.webp") with dissolve
            katrina "Kiddo. This is real life, not those stupid porn games you're playing."

            show ep10_109
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode10/109.webp") with dissolve
            hide ep10_109
            toby "What's wrong darling? I thought you didn't want this."
            scene expression ("images/episode10/110.webp") with dissolve
            katrina "What I want is for you to apologize."
            toby "What a coincidence. I'm also waiting for you to apologize and maybe blow me."
            toby "You know? Just to even things up."
            scene expression ("images/episode10/111.webp") with dissolve
            katrina "Before or after I shoot your cock?"
            toby "How about both."
            scene expression ("images/episode10/112.webp") with dissolve
            katrina "Drop your pants."
            toby "I knew you couldn't resist me."
            scene expression ("images/episode10/113.webp") with dissolve
            katrina "I don't want to miss your tiny cock."
            toby "Tiny cock? I doubt you could fit it in your mouth."
            katrina "Believe me I can!"
            scene expression ("images/episode10/114.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0
            toby "Then fucking prove it."

            scene expression ("images/episode10/115.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode10/116.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()
            toby "That's it baby. Be a good slut and suck that cock."

            scene expression ("images/episode10/117.webp") with dissolve
            show ep10_117
            $ ui.saybehavior()
            $ ui.interact()
            toby "If I didn't know any better, I'd say you suck cock for a living."
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\n{i}MmmOTHERmmmFUCKmmmER!{/i}"
            hide ep10_117

            show ep10_120
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode10/120.webp") with dissolve
            hide ep10_120
            toby "Don't you know it's not polite to speak with your mouth full?"
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\n{i}You're so gonna pay for this.{/i}"

            scene expression ("images/episode10/118.webp") with dissolve
            show ep10_118
            toby "I know, I know. I already pay. Seeing how much you like to suck cock, I'd say I'm doing you a favor."
            $ ui.saybehavior()
            $ ui.interact()
            hide ep10_118

            scene expression ("images/episode10/119.webp") with dissolve
            show ep10_119
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fucking hell... This is so good.{/i}"
            $ ui.saybehavior()
            $ ui.interact()
            hide ep10_119

            scene expression ("images/episode10/121.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0
            toby "Come here you little slut. I want to fill your pussy."

            scene expression ("images/episode10/122_1.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0
            katrina "Fuck me, [toby!c]."

            scene expression ("images/episode10/122_2.webp") with dissolve:
                xalign 0.0
                yalign 0.0
                linear 10.0 yalign 0.8 xalign 1.0
            toby "Turn around. I'm fucking you from behind like the little slut that you are."

            scene expression ("images/episode10/123.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0
            katrina "Am I a slut?"

            scene expression ("images/episode10/124.webp") with dissolve
            show ep10_124
            toby "You're the biggest slut!"
            katrina "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes... Yes. I'm a slut."
            toby "Are you my slut?"
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYES!"
            hide ep10_124

            scene expression ("images/episode10/125.webp") with dissolve
            show ep10_125
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck... Your cock feels so good."
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nGive it to me. Hard."
            katrina "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nHarder!"
            hide ep10_125

            scene expression ("images/episode10/126.webp") with dissolve
            show ep10_126
            katrina "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes. Yes... YES!"
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nLike that. Fuck me in my cunt."
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI want it harder!"
            hide ep10_126

            scene expression ("images/episode10/127.webp") with dissolve
            show ep10_127
            katrina "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes! YES! YESSS."
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nJust like that. Don't stop."
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nDon't stop."
            katrina "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nFuck me."
            hide ep10_127

            scene expression ("images/episode10/128.webp") with dissolve
            show ep10_128
            katrina "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nFuck, fuck, FUCK! You're so big for my little cunt."
            toby "You like my cock slut?"
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYES. I love it."
            toby "Is it better than any toy you use?"
            katrina "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nFuck yes."
            hide ep10_128

            scene expression ("images/episode10/129.webp") with dissolve
            show ep10_129
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI'm going to cum."
            toby "I'm close too."
            katrina "Don't you dare cum inside me. I promise I will kill you."
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's seems serious. I think this is a good time to listen to her.{/i}"
            katrina "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nYES... YES... YESSS."
            hide ep10_129

            scene expression ("images/episode10/130.webp") with dissolve
            play sound "audio/fx/Knocking-on-door-five-knocks-www.fesliyanstudios.com.mp3"
            "{i}*knock, knock*{/i}"
            neal "Sorry ma'am, but Mr. Wood is here. He says it's something urgent."
            scene expression ("images/episode10/131.webp") with dissolve
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nDo not come inside."
            scene expression ("images/episode10/130.webp") with dissolve
            neal "What? You said to come inside?"
            scene expression ("images/episode10/132.webp") with dissolve
            neal "Okay."
            scene expression ("images/episode10/133.webp") with dissolve
            $ unlockImage(persistent.katrina_07)
            play sound "audio/fx/gunshot.mp3"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, I'm coming.{/i}"
            with flash
            with flash
            katrina "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nI SAID \"DON'T FUCKING COME INSIDE\"."
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}How the fuck was she able to fire that gun? I didn't think she had any bullets left.{/i}"

            scene expression ("images/episode10/134.webp") with dissolve
            katrina "Fucking hell you came inside?"
            $ unlockMemory(persistent.memory_34)
            $ renpy.end_replay()

        scene expression ("images/episode10/135.webp") with dissolve
        katrina "Get out of here, before I kill you."
        toby "Should I go home?"
        scene expression ("images/episode10/136.webp") with dissolve
        katrina "No... Wait for me in the club, we still have business to discuss."
    else:

        scene expression ("images/episode10/099.webp") with dissolve
        katrina "So? How is my favorite employee?"
        katrina "Did you change your mind and come to lick my pussy?"
        toby "Nope."
        scene expression ("images/episode10/100.webp") with dissolve
        katrina "Are you sure?"
        toby "Yes ma'am."
        katrina "Fuck, you're so boring."
        scene expression ("images/episode10/130.webp") with dissolve
        "{i}Knock, knock.{/i}"
        play sound "audio/fx/Knocking-on-door-five-knocks-www.fesliyanstudios.com.mp3"
        neal "Sorry ma'am, but Mr. Wood is here. He says it's something urgent."
        scene expression ("images/episode10/100.webp") with dissolve
        katrina "You go wait for me in the club. I've got some business to take care of."
        toby "Yes ma'am."

    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message

    $ progress = 134
    scene expression ("images/episode10/137.webp")
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What is taking her so long?{/i}"
    scene expression ("images/episode10/138.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    katrina "Here you are."
    if katrina_path:
        scene expression ("images/episode10/139.webp") with dissolve
        katrina "Business first, so take this to Kayla."
        scene expression ("images/episode10/140.webp") with dissolve
        katrina "Now that your hands are busy. Why the fuck do I still feel your cum inside my pussy."
        scene expression ("images/episode10/141.webp") with dissolve
        toby "Because you didn't clean yourself yet?"
        scene expression ("images/episode10/140_2.webp") with dissolve
        katrina "You got one more chance and then I'll shoot. This time I really don't care, I'll just have to take the package myself. So?"
        scene expression ("images/episode10/142.webp") with dissolve
        toby "Because you fucking scared me when you shot. I didn't expect you to actually shoot."
        scene expression ("images/episode10/140_2.webp") with dissolve
        katrina "Why wouldn't you expect for me to shoot when I'm pointing a gun?"
        scene expression ("images/episode10/142.webp") with dissolve
        toby "Because you were supposed to be out of bullets."
        scene expression ("images/episode10/143.webp") with dissolve
        katrina "Fucking hell... You thought I was out of bullets? That's why you were so tough back there? Because you were sure I wouldn't kill you?"
        katrina "This gun sometimes misfires. It's pretty much broken, but it has sentimental value. It was my first pistol."
        scene expression ("images/episode10/144.webp") with dissolve
        katrina "So next time you're being smart, try to be smarter, because you were this close from being history."
        scene expression ("images/episode10/145.webp") with dissolve
        katrina "Lucky for you, the sex was good, but that was a one time thing, from now on you only get to lick my pussy or my ass. You choose."
        scene expression ("images/episode10/146_1.webp") with dissolve
        katrina "Now, chop, chop. Kayla is waiting for this package."
        scene expression ("images/episode10/146_2.webp") with dissolve
        toby "Umm... I kinda have one request. Do you think it's possible for me to get one box of chocolate for recreational purposes?"
        scene expression ("images/episode10/146_3.webp") with dissolve
        katrina "Help yourself from the box."
        scene expression ("images/episode10/146_2.webp") with dissolve
        toby "Thank you, ma'am."
    else:
        scene expression ("images/episode10/139.webp") with dissolve
        katrina "Take this box to Kayla. She's waiting for you."
        toby "Okay ma'am."
        scene expression ("images/episode10/146_2.webp") with dissolve
        toby "I've got one question. Do you think it's possible for me to get a box of chocolate for recreational purposes?"
        scene expression ("images/episode10/146_3.webp") with dissolve
        katrina "Help yourself from the box."
        scene expression ("images/episode10/146_2.webp") with dissolve
        toby "Thank you, ma'am."

    scene expression ("images/episode10/148.webp") with dissolve
    katrina "See you around."

    scene expression ("images/episode10/149.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/150.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    return


label episode10_trisChores:
    $ progress = 135

    scene expression ("images/episode10/153.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()


    scene expression ("images/episode10/154.webp") with dissolve
    if toby_job == 0:
        toby "What are you doing, [sis]?"
    else:
        toby "What the hell are you doing? This is how you're cleaning my room?"
    scene expression ("images/episode10/155.webp") with dissolve
    patricia "Do you really believe what this book says?"
    toby "You don't agree with it?"
    patricia "Nope. It's full of crap."
    scene expression ("images/episode10/156_curious.webp") with dissolve
    toby "What makes you say that?"
    scene expression ("images/episode10/157_reading.webp") with dissolve
    patricia "\"Of course, if she’s stroking your knee, no need for further questions. But if she’s stroking hers, this may be a subconscious desire to stroke yours.\""
    scene expression ("images/episode10/157_curious.webp") with dissolve
    patricia "Really? Has any girl you dated ever stroked your knee?"
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "Not really, but I don't know. Maybe she was touching her knee."
    scene expression ("images/episode10/157_laugh.webp") with dissolve
    if emma_break:
        patricia "We both know you only dated bitches, so if they were touching their knees, it was probably because they were hurting from showing you too much affection."
    else:
        patricia "If you're talking about Emma, if she was touching her knees, it was probably because they were hurting from showing you too much affection."
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "You're being a bitch right now. You know that, right?"
    scene expression ("images/episode10/157_laugh.webp") with dissolve
    patricia "Yet I don't feel the need to scratch my knees."
    scene expression ("images/episode10/157_normal.webp") with dissolve
    patricia "So whoever sold you this book, he screwed you."
    scene expression ("images/episode10/156_book.webp") with dissolve
    toby "Give me the book."
    scene expression ("images/episode10/157_laugh.webp") with dissolve
    patricia "Let me read you one more."
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "I know. I already read that part."
    scene expression ("images/episode10/157_reading.webp") with dissolve
    patricia "Then let's read something from the end. I will spoil the book for you."
    patricia "\"When a woman suddenly blinks faster, you may have increased her level of sexual excitement\"."
    patricia "\"You might notice a sudden rapid eye blink when you tell an amazing story of you being a cool/exciting/funny guy. This is a subliminal way of saying, “You’ve captured my interest.”\"."
    scene expression ("images/episode10/156_book.webp") with dissolve
    toby "Give me the book."
    scene expression ("images/episode10/158.webp") with dissolve
    patricia "But... I still want to read it, big [brother]. Can't you see how interested I am in your book."
    show ep10_158
    toby "I see what you're trying to do, but it's not working."
    hide ep10_158
    scene expression ("images/episode10/157_cool.webp") with dissolve
    patricia "My point exactly. This book is full of crap. If you want to know what girls think, you can ask me. I've been a girl for all my life, so I think I know more about how women think than this Dr. Love who wrote this book."
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "And why would you help me?"
    scene expression ("images/episode10/157_smile.webp") with dissolve
    patricia "Because I'm your [sister] and I want the best for you. This way I also get to filter your bimbos. If I don't like a girl I'll give you crappy advice, like \"If she's touching her hair, she actually wants you to touch it\"."
    scene expression ("images/episode10/156_laugh.webp") with dissolve
    toby "And what's in for you?"
    scene expression ("images/episode10/157_smile.webp") with dissolve
    patricia "What do you mean, what's in for me? I don't need anything. What type of person do you think I am?"
    scene expression ("images/episode10/157_laugh.webp") with dissolve
    patricia "I just told you, I'm doing this because I love you, but if you'd be willing to buy me gifts or give me money, who am I to say no to that?"
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "I'm already paying you clean my room and by the looks of it, you're not doing a very good job, because instead of making my bed you're messing it up by sitting in it."
    scene expression ("images/episode10/157_cool.webp") with dissolve
    patricia "You call that payment? Have you seen how your room looks in the morning after you leave?"
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "Oh please. It's not that bad."
    scene expression ("images/episode10/157_laugh.webp") with dissolve
    patricia "It's not good either, so I think $50 is a bit cheap for all the work I do."
    scene expression ("images/episode10/156_flirty.webp") with dissolve
    toby "If you want more, you know what to do."
    scene expression ("images/episode10/157_normal.webp") with dissolve
    patricia "I actually need some money. I'm going out with Bea tonight and I could really use some."
    scene expression ("images/episode10/156_laugh.webp") with dissolve
    toby "You know what to do?"
    scene expression ("images/episode10/157_pouty.webp") with dissolve
    patricia "Can't you be a good [brother] for once?"
    scene expression ("images/episode10/156_smile.webp") with dissolve
    toby "Fine. I'll adjust the prices."
    scene expression ("images/episode10/157_surprised.webp") with dissolve
    patricia "Really?"
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "Of course. What won't I do for my little [sister]?"
    scene expression ("images/episode10/156_laugh.webp") with dissolve
    toby "So, $26 if your cleaning my room in your clothes, $51 if you're doing it in this dress, $101 in your underwear and $202 if you do it naked."
    scene expression ("images/episode10/157_meh.webp") with dissolve
    patricia "You just added $1 to each."
    scene expression ("images/episode10/156_laugh.webp") with dissolve
    toby "Not true. I added 2$ on the last tier."
    scene expression ("images/episode10/157_laugh.webp") with dissolve
    patricia "Stupid me. I almost forgot how much you can do with 2$."
    scene expression ("images/episode10/156_smile.webp") with dissolve
    toby "There are countries where you can buy a house with 2$."
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "Or a tent."
    scene expression ("images/episode10/157_smile.webp") with dissolve
    patricia "So 101$ if I clean your room in my underwear?"
    scene expression ("images/episode10/156_flirty.webp") with dissolve
    toby "You're considering it?"
    scene expression ("images/episode10/157_laugh.webp") with dissolve
    patricia "Nope. But I like the face you make when you think things are going your way."
    scene expression ("images/episode10/159.webp") with dissolve
    if sheila_path:
        toby "Well, I'd like to stay and chit chat, but I gotta prepare for a date tonight, because believe it or not, that book is doing wonders."
        scene expression ("images/episode10/160.webp") with dissolve
        patricia "I'm sure it's just another bimbo."
        scene expression ("images/episode10/159.webp") with dissolve
        toby "Bimbo or not, tonight I'm having sex, while you go out with Bea talking about bad boys like me."
        scene expression ("images/episode10/162.webp") with dissolve
        patricia "Or maybe we will have sex too. Maybe I'm lesbian now."
        scene expression ("images/episode10/163.webp") with dissolve
        toby "Let me know how that goes."
    else:
        toby "Well, I'd like to stay and chit chat, but I gotta take a shower, because I need to meet up with a girl."
        scene expression ("images/episode10/161.webp") with dissolve
        patricia "Don't tell me this book actually works."
        scene expression ("images/episode10/159.webp") with dissolve
        toby "Maybe it does, but I'm not dating her. I just have to give her something."
        scene expression ("images/episode10/161.webp") with dissolve
        patricia "I told you, this book is full of crap."
        scene expression ("images/episode10/163.webp") with dissolve
        toby "Well, since I paid for it, I plan on finishing it."

    scene expression ("images/episode10/164.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/165.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/166.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/167.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/168.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/169.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/170.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/171.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    $ progress = 136
    scene expression ("images/episode10/172.webp") with dissolve
    toby "What are you still doing here?"
    scene expression ("images/episode10/173.webp") with dissolve
    patricia "Waiting for my payment."
    scene expression ("images/episode10/172.webp") with dissolve
    toby "Oh, right."
    scene expression ("images/episode10/174.webp") with dissolve
    toby "Here's you $50."
    scene expression ("images/episode10/175.webp") with dissolve
    patricia "You're missing some."
    scene expression ("images/episode10/176.webp") with dissolve
    toby "Oh, right. My bad. Here one more."
    scene expression ("images/episode10/175_1.webp") with dissolve
    patricia "Umm... Have you checked your phone in a while?"
    toby "No. Why?"
    patricia "Well, I'm actually $151 short."
    scene expression ("images/episode10/177.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Looks like she sent me some messages.{/i}"
    scene expression ("images/episode10/177_texting.webp") with dissolve
    call sms_incoming ("tris", "Are you ready to be broke, because I think I'm about to get a whole lot richer.") from _call_sms_incoming_201
    call sms_incoming ("tris", "Since I don't wear a bra, I thought I could keep the apron and still count as lingerie.", img_icon="images/episode10/178_icon.webp", img="images/episode10/178.webp") from _call_sms_incoming_202
    $ unlockImage(persistent.patricia_18)
    scene expression ("images/episode10/177.webp") with dissolve
    hide screen message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck. She's hot. I wish I could see this in person.{/i}"
    scene expression ("images/episode10/179.webp") with dissolve
    patricia "So? What do you think? Am I short or not?"
    toby "Maybe, but only $50, not $151 like you said."
    patricia "Oh... Maybe there is more."
    toby "There's more?"
    patricia "Maybe."
    scene expression ("images/episode10/177_texting.webp") with dissolve
    call sms_incoming ("tris", "Ummm. Changed my mind. Since you're still in bathroom and won't be able to see me like this.", img_icon="images/episode10/180_icon.webp", img="images/episode10/180.webp") from _call_sms_incoming_203
    scene expression ("images/episode10/177.webp") with dissolve
    hide screen message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Damn. Tris is messing with me. I need to change the rules of this game. She won't be allowed to clean my room when I'm not around.{/i}"
    scene expression ("images/episode10/179.webp") with dissolve
    patricia "By the look on your face, I'd say you agree that I'm $151 short."
    toby "We need to talk about this. From now on you're not allowed to clean my room unless I'm present."
    scene expression ("images/episode10/181.webp") with dissolve
    patricia "We'll talk about that later. Right now I'm going to need that $151, because I plan on having fun tonight."
    scene expression ("images/episode10/182.webp") with dissolve
    toby "Here's the money, but from now on I need to see you cleaning my room in person"
    patricia "I knew you'd say that, that's why I sent you a photo, silly."
    scene expression ("images/episode10/183.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode10/184.webp") with dissolve
    patricia "{size=12}{color=#FDCA6E}* softly speaking *{/color}{/size}\n{i}Pleasure doing business with you.{/i}"
    scene expression ("images/episode10/185.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode10/186.webp") with dissolve
    patricia "Oopsies. You dropped your towel."
    scene expression ("images/episode10/187.webp") with dissolve
    patricia "You're sick [bro]. You got a boner from watching your little [sister] doing chores naked."
    scene expression ("images/episode10/188.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}The fuck was that? I know that we have our games, but this... this was something else.{/i}"
    scene expression ("images/episode10/189.webp") with dissolve:
        xalign 0.5
        yalign 0.5
        zoom 0.5
        linear 120.0 zoom 1.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}For some reason, this time it didn't feel like a game, more like she was actually flirting with me.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It can't be. She's my little [sister].{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Or? Was she really flirting with me?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I don't know how to feel about this. I do love my [sister] and she's beautiful, smart, gorgeous and hot.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Am I really attracted to her? I must be. Why else would I get a boner every time she shows me her boobs or I see her pics.{/i}"
    if toby_job == 0:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Whatever it is, we need to have a talk.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Whatever is happening she's gonna pay for playing with me.{/i}"

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Anyway. I should get changed.{/i}"

    return

label episode10_shower:
    scene expression ("images/episode10/164.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/165.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/167.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/168.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/169.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    return

label episode10_sheila:
    $ progress = 137

    scene expression ("images/episode10/190.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/191.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/192.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/193.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if sheila_path:
        scene expression ("images/episode10/194.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode10/195.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        toby "God, you're beautiful."
        sheila "Thank you!"
        sheila "Shall we?"
        toby "Yes, we shall."

        scene expression ("images/episode10/196.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode10/197.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode10/198.webp") with dissolve
        sheila "So you're telling me that if you'd won one million dollars you wouldn't spend a dime for a week?"
        toby "Yes. That's exactly what I'm saying."
        scene expression ("images/episode10/199_curious.webp") with dissolve
        sheila "But why?"
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "Well. One million dollars might seem like a lot at first, but once you start spending it, it doesn't seem so much."
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "But it's still one million dollars."
        scene expression ("images/episode10/200_smile.webp") with dissolve
        toby "Yes, but you won that money. You didn't earn it, so even though you know the value of money now, when you win it you'll think you can get more millions just like that, so you tend to spend it on stupid things."
        scene expression ("images/episode10/199_normal.webp") with dissolve
        sheila "That's an interesting way of thinking, but I still don't get why wait on week and then spend them?"
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "Because after a week, you've had enough time to think about what you really need, because if I won one million dollars right in this moment, and I wouldn't be careful, and by morning I'd have less than 100k left."
        scene expression ("images/episode10/199_laugh.webp") with dissolve
        sheila "Now we're getting somewhere. Let's say you win one million dollars right now and you have till morning to spend it all. If you do you'll win another million which you can do whatever you want with. If you want to wait a week, that's it."
        scene expression ("images/episode10/200_flirty.webp") with dissolve
        toby "Well, in that case, I'd buy you a diamond necklace, earrings and a bracelet."
        scene expression ("images/episode10/199_flirty.webp") with dissolve
        sheila "So you're telling me that the first thing you'd do is buy me something nice?"
        scene expression ("images/episode10/200_smile.webp") with dissolve
        toby "Sure. Why not? After all, I still want to have fun tonight."
        scene expression ("images/episode10/199_laugh.webp") with dissolve
        sheila "You think I would have sex with you tonight if you wouldn't buy me nice things? Do I look like a gold digger to you?"
        scene expression ("images/episode10/200_normal.webp") with dissolve
        toby "What am I saying and what she is hearing. I just told you that the first thing I'd do is buy you nice things. Not buy me that Rolls-Royce Phantom that I dream about."
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "So you'd buy me 15k of jewelry while you get yourself a 500k car?"
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "I'm the one who won the money after all. I don't remember hearing you telling me that you'd buy me something nice if you'd won one million dollars."
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "Hey. That's not how the game works. I'm the victim here."
        scene expression ("images/episode10/200_smile.webp") with dissolve
        toby "Let's switch places for now."
        scene expression ("images/episode10/200_curious.webp") with dissolve
        toby "What would you do if you won one million dollars."
        scene expression ("images/episode10/199_curious.webp") with dissolve
        sheila "Hmm... I'd split it in 3. With one third of money I'd take you shopping."
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "That's bullshit. I don't believe you'd buy me 330k worth of gifts."
        scene expression ("images/episode10/199_laugh.webp") with dissolve
        sheila "Who said anything about me buying you things? I need someone to help me with the bags. I'm buying designer clothes."
        scene expression ("images/episode10/200_normal.webp") with dissolve
        toby "And you complained about me."
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "You're a guy. In our society, you're supposed to buy me things, not the other way around."
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "That's a double standard."
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "Double or not, I still expect you to buy me something even if I win one million dollars."
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "Yeah... And I'm the bad guy here."
        scene expression ("images/episode10/199_laugh.webp") with dissolve
        sheila "Wait. You didn't hear what I would do with the rest."
        scene expression ("images/episode10/200_curious.webp") with dissolve
        toby "Surprise me."
        scene expression ("images/episode10/199_thinking.webp") with dissolve
        sheila "Well, with another third of the money I'd buy a nice house in the suburbs, because I hate the city."
        scene expression ("images/episode10/200_normal.webp") with dissolve
        toby "Why do you hate it?"
        scene expression ("images/episode10/199_normal.webp") with dissolve
        sheila "Because it's not safe. Maybe you don't notice because you're a guy, but for a girl it's not a safe place. The crime rate is huge."
        if toby_job == 0:
            scene expression ("images/episode10/200_sad.webp") with dissolve
            toby "I never thought about it. I got so used to it."
            scene expression ("images/episode10/199_sad.webp") with dissolve
            sheila "Yeah. It's not a nice place."
        else:
            scene expression ("images/episode10/200_normal.webp") with dissolve
            toby "It can't be that bad."
            scene expression ("images/episode10/199_normal.webp") with dissolve
            sheila "That's because you work in a mad place and got used to the crazy. I'm sure that if I'd pull a gun out of my purse right now you wouldn't even flinch."
            scene expression ("images/episode10/200_curious.webp") with dissolve
            toby "You have a gun on you?"
            scene expression ("images/episode10/199_laugh.webp") with dissolve
            sheila "I don't even have a purse, where would I keep my gun?"
            scene expression ("images/episode10/200_normal.webp") with dissolve
            toby "My gun? You have one?"
            scene expression ("images/episode10/199_awkward.webp") with dissolve
            sheila "Umm... No. Why would I have one?"


        scene expression ("images/episode10/199_normal.webp") with dissolve
        sheila "Anyway, with the last part of money I'd buy a Lambo."
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "That's an ugly car."
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "Maybe you think so, because you're an old soul and your dream car is a Rolls-Royce."
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "I'm not an old soul."
        scene expression ("images/episode10/199_impersonate.webp") with dissolve
        sheila "{size=12}{color=#FDCA6E}* mocking *{/color}{/size}\n{i}\"If I'd win one million dollars, I wouldn't touch it for a week.\"{/i}"
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "I don't sound like that."
        scene expression ("images/episode10/199_normal.webp") with dissolve
        sheila "Except that you are."
        scene expression ("images/episode10/200_normal.webp") with dissolve
        toby "That doesn't make me an old soul, but penny wise, unlike you, a big spender."
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "I'm not a big spender."
        scene expression ("images/episode10/200_impersonate.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* mocking *{/color}{/size}\n{i}\"I'm going to buy designer clothes and a Lambo. A pink one with fuzzy seats.\"{/i}"
        scene expression ("images/episode10/199_laugh.webp") with dissolve
        sheila "Ewww... Pink Lambo. No..."
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "Black with fuzzy seats?"
        scene expression ("images/episode10/199_normal.webp") with dissolve
        sheila "No fuzzy seats."
        scene expression ("images/episode10/201.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode10/199_normal.webp") with dissolve
        sheila "Actually I'd spend all the money to find and save my [sister]."
        scene expression ("images/episode10/200_curious.webp") with dissolve
        toby "Umm... What happened to her."
        scene expression ("images/episode10/199_sad.webp") with dissolve
        sheila "Nothing. Sorry, I don't want to ruin the night."
        scene expression ("images/episode10/200_normal.webp") with dissolve
        toby "You're not ruining anything. What happened to your [sister]?"
        scene expression ("images/episode10/199_angry.webp") with dissolve
        sheila "Nothing. I don't want to talk about it."
        scene expression ("images/episode10/200_sad.webp") with dissolve
        toby "Sorry if I said something. Are you okay?"
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "Don't worry. I'm fine."
        scene expression ("images/episode10/199_flirty.webp") with dissolve
        sheila "Did you get the chocolate?"
        scene expression ("images/episode10/200_normal.webp") with dissolve
        toby "Yes. But are you sure this is what you need right now?"
        scene expression ("images/episode10/199_normal.webp") with dissolve
        sheila "Yeah. This is the only thing I want right now. Let's go back to my place."
        scene expression ("images/episode10/200_normal.webp") with dissolve
        toby "..."

        scene expression ("images/episode10/202.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode10/203.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode10/204.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode10/205.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ unlockImage(persistent.sheila_08)
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode10/206.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()


        scene expression ("images/episode10/207.webp") with dissolve
        sheila "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Fuck... I can't do this to you.{/i}"
        toby "What's wrong, Sheila?"
        scene expression ("images/episode10/208.webp") with dissolve
        sheila "What is this? This isn't the chocolate we talked about."
        toby "Ummm..."
        scene expression ("images/episode10/209.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What's going on? Why is she acting so strange suddenly?{/i}"
        scene expression ("images/episode10/210.webp") with dissolve
        sheila "Look, I'm not in the mood anymore. Let me just put something on and I'll see you out."
    else:

        scene expression ("images/episode10/211.webp") with dissolve
        toby "Hey Sheila, look what I got for you."
        scene expression ("images/episode10/212.webp") with dissolve
        sheila "You got some?"
        scene expression ("images/episode10/211.webp") with dissolve
        toby "Well, it wasn't easy, but since you're always so nice to me, I thought it would be nice to do something for you."
        scene expression ("images/episode10/212.webp") with dissolve
        sheila "Well, thank y..."

        scene expression ("images/episode10/213_1.webp") with dissolve
        sheila "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Fuck... I can't do this to you.{/i}"
        scene expression ("images/episode10/213_2.webp") with dissolve
        sheila "This isn't the chocolate I've been telling you about."
        scene expression ("images/episode10/214.webp") with dissolve
        toby "Are you sure? Because I'm almost ..."
        scene expression ("images/episode10/215.webp") with dissolve
        sheila "No it's not. Anyway, let me see you out."

    $ progress = 138
    scene expression ("images/episode10/216.webp") with fade
    toby "What is going on, Sheila?"
    sheila "First of all you should know that I'm really sorry for everything."
    scene expression ("images/episode10/217_normal.webp") with dissolve
    sheila "I'm not a personal trainer. I'm actually an undercover agent, and I'm investigating Katrina and Darlene."
    scene expression ("images/episode10/218_surprised.webp") with dissolve
    toby "You're messing with me, right?"
    toby "I understand Katrina, but Darlene?"
    scene expression ("images/episode10/217_normal.webp") with dissolve
    sheila "You're right. The investigation is mainly on Katrina, but Darlene isn't completely innocent either."
    sheila "Together the couple runs a secret BDSM club and they are being investigated for drugs, prostitution, human trafficking and who knows what other horrors are going on there."
    scene expression ("images/episode10/218_curious.webp") with dissolve
    toby "And what does that have to do with me? I'm not involved in any of that."
    scene expression ("images/episode10/217_sad.webp") with dissolve
    sheila "You appeared on our radar when you took the job, so we had to keep tabs on you from the beginning. That way you wouldn't suspect me later."
    sheila "That was my job, to get close to you and then use you for information and maybe access."
    if sheila_path:
        scene expression ("images/episode10/218_angry.webp") with dissolve
        toby "So the sex was just part of the job."
        scene expression ("images/episode10/217_sad.webp") with dissolve
        sheila "Don't be like that, please. I had my orders."
        scene expression ("images/episode10/218_normal.webp") with dissolve
        toby "So it's okay for you to have sex with me, because your boss orders you to, but if Katrina does it, then it's pimping and prostitution."
        scene expression ("images/episode10/217_normal.webp") with dissolve
        sheila "It's not like that."
        scene expression ("images/episode10/218_angry.webp") with dissolve
        toby "Then how it is? Why aren't you sucking my cock then? Isn't that your job."
        scene expression ("images/episode10/219.webp") with dissolve
        sheila "You're an asshole!"
        scene expression ("images/episode10/217_angry.webp") with dissolve
        sheila "Look. I'm making a big sacrifice here."
        scene expression ("images/episode10/218_normal.webp") with dissolve
        toby "What are you sacrificing? You won't have a \"booty call boy\" when you feel like having sex?"
        scene expression ("images/episode10/217_angry.webp") with dissolve
        sheila "Why do you think we didn't have sex yesterday? I hate using you. You don't deserve this."
        scene expression ("images/episode10/218_angry.webp") with dissolve
        toby "Still... I don't see what are you sacrificing, by not fucking me."
        scene expression ("images/episode10/217_angry.webp") with dissolve
        sheila "I'm sacrificing my [sister], you asshole."
    else:
        scene expression ("images/episode10/218_curious.webp") with dissolve
        toby "So, why are you telling me this now?"
        scene expression ("images/episode10/217_sad.webp") with dissolve
        sheila "Because you're actually a nice guy who is getting way too close to the fire."
        scene expression ("images/episode10/218_normal.webp") with dissolve
        toby "Wasn't that the whole idea? Wait for me to get into the organization and then use me, so you can bring them down?"
        toby "Except that I probably would have gone down too."
        scene expression ("images/episode10/218_angry.webp") with dissolve
        toby "So you didn't care that you let someone ruin his life as long as you got the job done."
        toby "That's nice."
        scene expression ("images/episode10/217_normal.webp") with dissolve
        sheila "It's not like that."
        scene expression ("images/episode10/218_curious.webp") with dissolve
        toby "Then enlighten me. How it is then. Wasn't that the whole idea? Hoping that I would get deeper into their world so you could use me for info?"
        scene expression ("images/episode10/217_angry.webp") with dissolve
        sheila "Look. I'm making a big sacrifice here."
        scene expression ("images/episode10/218_normal.webp") with dissolve
        toby "Don't get me wrong. I appreciate you telling me this, but that doesn't change the fact that you people would have let me ruin my life."
        scene expression ("images/episode10/218_angry.webp") with dissolve
        sheila "Well, I would have ruined anyone's life to save my [sister]."

    scene expression ("images/episode10/218_curious.webp") with dissolve
    toby "Your [sister]? What are you talking about?"
    scene expression ("images/episode10/217_normal.webp") with dissolve
    sheila "I'm almost sure that Katrina has her."
    scene expression ("images/episode10/218_normal.webp") with dissolve
    toby "You mean like, she kidnapped her?"
    scene expression ("images/episode10/217_cry.webp") with dissolve
    sheila "I don't know. I don't know anything about her anymore."
    scene expression ("images/episode10/218_normal.webp") with dissolve
    toby "I'm sorry. I didn't know, but what happened exactly?"
    scene expression ("images/episode10/217_normal.webp") with dissolve
    sheila "Well, our [mother] died when we were little, so we only had our [father], but he died in the line of duty when I was 19. She was 17 at the time."
    scene expression ("images/episode10/217_sad.webp") with dissolve
    sheila "His death affected us very differently. I decided to become a cop and continue his legacy. Finish what he couldn't."
    scene expression ("images/episode10/218_curious.webp") with dissolve
    toby "And your [sister]?"
    scene expression ("images/episode10/217_sad.webp") with dissolve
    sheila "Well, she chose a different path. She was so pissed that he died, that she rebelled against anything my [father] believed in."
    scene expression ("images/episode10/217_angry.webp") with dissolve
    sheila "He was against smoking, so she started smoking."
    scene expression ("images/episode10/217_sad.webp") with dissolve
    sheila "He was against drugs, so she started using."
    sheila "He was against us going to clubs, so guess what she did."
    scene expression ("images/episode10/218_normal.webp") with dissolve
    toby "Let me guess. She went clubbing?"
    scene expression ("images/episode10/217_normal.webp") with dissolve
    sheila "Every night."
    scene expression ("images/episode10/217_sad.webp") with dissolve
    sheila "And not only was she was pissed at him, she got pissed at me too, because I became a cop and she thought I would die just like him."
    scene expression ("images/episode10/217_cry.webp") with dissolve
    sheila "Since our [father] died, I became a little bit overprotective and we had a huge fight."
    sheila "That's the last time I saw her. I remember her dressing up for the club and telling me to fuck off."
    sheila "Those where her last words to me."
    scene expression ("images/episode10/218_normal.webp") with dissolve
    toby "And let me guess. It was Katrina's club?"
    scene expression ("images/episode10/217_sad.webp") with dissolve
    sheila "Exactly, so the fact that I'm telling you this, might cost me the mission, but I already lost someone dear to me, so I'm not losing you too."
    scene expression ("images/episode10/218_curious.webp") with dissolve
    toby "But why would you risk losing your [sister] for some stranger?"
    scene expression ("images/episode10/217_cryLaugh.webp") with dissolve
    sheila "Beats me if I know."
    if sheila_path:
        scene expression ("images/episode10/217_normal.webp") with dissolve
        sheila "But I'm starting to like you, very much, so I can't let you ruin your life."
        scene expression ("images/episode10/217_normal.webp") with dissolve
        sheila "You're the first guy who actually respects me and likes me genuinely, or at least that's what I believe."
        menu:
            "{i}[JGR]kiss her{/i}":
                show ep10_220 with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode10/220.webp")
                hide ep10_220
                toby "I really do."
                sheila "I know, [toby!c]."
                scene expression ("images/episode10/221.webp") with dissolve
                sheila "What was that for?"
                toby "I don't know, it felt like you could use a little love."
            "{i}hug her{/i} [JWRN2]"(csq="Closes Sheila's path."):

                $ sheila_closed = True
                $ sheila_path = False
                $ renpy.notify("Sheila's path has been closed!")
                pass
    else:
        scene expression ("images/episode10/217_normal.webp") with dissolve
        sheila "But it was the first time someone did anything nice for me without expecting something in return."
        scene expression ("images/episode10/217_laugh.webp") with dissolve
        sheila "You showed up with that big stupid grin, because you managed to get me that box of chocolates and you never expected anything in return. That's very special nowadays."
    if sheila_path == False:
        scene expression ("images/episode10/222.webp") with dissolve
        toby "Come here."
        scene expression ("images/episode10/223.webp") with dissolve

    sheila "Thank you for not being pissed at me."
    toby "I am pissed, but I understand your reasons. I would probably do anything for my [sister] too."
    sheila "I'm sure of that."

    scene expression ("images/episode10/224.webp") with dissolve
    toby "By the way. Why are we in the hallway?"
    sheila "My apartment is bugged."
    if sheila_path:
        toby "And what would have happened if we had sex? Would your boss hear you scream my name?"
        sheila "Now that you put it like that, it does sound dirty."
    else:
        toby "Shit... I'm never going in your apartment."
    sheila "Anyway. What are you going to do now?"
    scene expression ("images/episode10/225.webp") with dissolve
    toby "What else can I do? I'm going to help you with your [sister]."
    sheila "Are you serious?"
    toby "Of course, but I'm going to need your help not to let me go down with everybody."
    sheila "I'll do my best, but please try not to do anything illegal."
    if toby_job == 0:
        toby "I will."
        sheila "And I'll talk to my superiors and try to convince them to give you immunity, but you'll have to help me expose the couple."
        toby "I still don't buy that Darlene has any part of it, but I'll do my best to prove that Katrina is guilty."
        sheila "Don't put too much trust in her."
    else:
        toby "Like delivering drugs?"
        sheila "Yes..."
        toby "Then, that's going to be a problem."
        sheila "Shit... Don't worry, I'll talk to my superiors and convince them to give you immunity. After all, you didn't do anything, but that would mean you help us expose the couple, not only help me."
        toby "I don't owe them anything, but if that's what I've got to do, I'll do my best."

    scene expression ("images/episode10/226.webp") with dissolve
    toby "Anyway, I guess I should leave, before your boss suspects anything."
    sheila "Yeah, you're right."
    sheila "Thank you for everything and please be careful."
    toby "Don't worry. I'll be fine."

    scene expression ("images/episode10/227.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What have I gotten myself into?{/i}"

    scene expression ("images/episode10/228.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Are Katrina and Darlene really that bad? I mean I could see Katrina doing all that, but Darlene? No way.{/i}"

    scene expression ("images/episode10/229.webp") with dissolve:
        zoom 1.0
        linear 10.0 zoom 1.5 xalign 0.5

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/230.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    return

label episode10_fight:
    $ progress = 139

    scene expression ("images/episode10/231.webp") with dissolve:
        xalign 0.0
        yalign 0.0
        linear 10.0 yalign 1.0 xalign 1.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the hell is all the noise?{/i}"

    scene expression ("images/episode10/232.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/233.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think [mom] and [dad] are fighting. Again.{/i}"

    scene expression ("images/episode10/234.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'll go check up on Tris to make sure she's ok. She hates it when they fight.{/i}"

    scene expression ("images/episode10/235.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Good. At least she's not home.{/i}"

    scene expression ("images/episode10/236.webp") with dissolve:
        xalign 0.5
        yalign 0.5
        zoom 0.8
        linear 10.0 zoom 1.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Now... How on Earth am I going to stop them for fighting.{/i}"

    scene expression ("images/episode10/237.webp") with dissolve
    erwin "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nDo you think I don't know what's going on? Do you think I'm that stupid?!"
    charlotte "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nHow dare you accuse me of this. All I've done was be there for you!"
    erwin "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nSo then what the fuck is this?!"
    scene expression ("images/episode10/238.webp") with dissolve
    erwin "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nSince you didn't show it to me, what else could it be?!"
    scene expression ("images/episode10/239.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nAre you two out of your minds? What the hell is going on?!"
    erwin "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nYou go to your room. This doesn't concern you!"
    toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nIt does concern me, because whether you like it or not, I'm still your [son] and you're my [parents]!"
    scene expression ("images/episode10/240.webp") with dissolve
    charlotte "Please, [toby!c]. Get out. This has nothing to do with you."
    scene expression ("images/episode10/241.webp") with dissolve
    erwin "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nYes, [son]. This is between me and your [mother]!"
    scene expression ("images/episode10/242.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nWell if you wanted to keep it between you, then you should've thought about that before yelling so loud the whole neighborhood can hear you!"

    scene expression ("images/episode10/243.webp") with dissolve
    erwin "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nI said, get out of my room!"
    scene expression ("images/episode10/242.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nIf you think I'm going to let you fight, then you're getting senile, old man. I won't stand here and let you two yell!"
    toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nWhat if Tris came back home first and heard you two yelling like that? You both know how she is!"
    toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nAre you really that desperate to emotionally break the only angel in this fucking hell?!"
    scene expression ("images/episode10/243.webp") with dissolve
    erwin "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nAt least she would have found what a cheating whore her [mother] is!"
    scene expression ("images/episode10/244.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode10/245.webp") with dissolve
    if toby_job == 0:
        toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nYou have no right to talk about [mom] like that!"
    else:
        toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nIf you ever say that about [mom] again I don't give a fuck if you're my [father] or not. I'm going to kill you!"

    scene expression ("images/episode10/245_1.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nHow the fuck can she cheat on you if she never leaves the house?!"
    toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nWhy the fuck would she cheat on you? Did you hit your head? I can't even convince her to divorce you!"
    scene expression ("images/episode10/246.webp") with dissolve
    erwin "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nBecause she needs me for money!"
    scene expression ("images/episode10/247.webp") with dissolve
    charlotte "What fucking money? You never gave me a dime since we moved. I never asked you anything. I just need for you to love me."
    scene expression ("images/episode10/248.webp") with dissolve
    toby "Come here, [mom]. You're sleeping in my room tonight."
    scene expression ("images/episode10/249.webp") with dissolve
    erwin "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nIf she's not cheating me, then explain why I found this sexy lingerie. I for one haven't seen her in it."
    scene expression ("images/episode10/250.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nHow the fuck would you want to see her dressed like that since when you're home all you do is sleep?"
    toby "The problem was never [mom]. You know she would never cheat on you, but you're too fucking drunk to admit it and way too proud to talk about the real problem."
    scene expression ("images/episode10/251.webp") with dissolve
    toby "Let's go, [mom]."
    scene expression ("images/episode10/252.webp") with fade
    charlotte "Thank you for standing up for me. I could never ask for a better [son]."
    toby "You know I'll always be here for you."
    charlotte "I know."
    scene expression ("images/episode10/255.webp") with dissolve
    charlotte "..."
    scene expression ("images/episode10/253_curious.webp") with dissolve
    charlotte "Do you think I should do it?"
    scene expression ("images/episode10/254_normal.webp") with dissolve
    toby "Do what?"
    scene expression ("images/episode10/253_sad.webp") with dissolve
    charlotte "Divorce him?"
    scene expression ("images/episode10/254_sad.webp") with dissolve
    toby "Look [mom]. I can't tell you what to do. That's your decision. But just know that you don't have to worry about me or Tris."
    scene expression ("images/episode10/254_normal.webp") with dissolve
    toby "We're both old enough to understand. So make this decision for you, not for us."
    scene expression ("images/episode10/253_sad.webp") with dissolve
    charlotte "Thank you dear."
    scene expression ("images/episode10/253_normal.webp") with dissolve
    charlotte "What would you do in my situation?"
    scene expression ("images/episode10/254_sad.webp") with dissolve
    toby "I would say that divorce is the way, but I haven't had a 20 years relationship. I never lived with anyone. I never shared the good or the bad with someone, so I don't know what you're going through."
    scene expression ("images/episode10/253_smile.webp") with dissolve
    charlotte "You're a wise kid."
    scene expression ("images/episode10/254_smile.webp") with dissolve
    toby "I clearly took after you."
    scene expression ("images/episode10/254_normal.webp") with dissolve
    toby "Just know that whatever you choose, I will always be by your side."
    scene expression ("images/episode10/256.webp") with dissolve
    charlotte "I love you, [toby!c]."
    toby "I love you too, [mom]."
    scene expression ("images/episode10/257.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    return

label episode10_nightCharlotte:
    $ progress = 140
    label memory_35:

        scene expression ("images/episode10/258.webp") with dissolve
        toby "Do you want me to let you sleep?"
        scene expression ("images/episode10/259_1.webp") with dissolve
        charlotte "What about you?"
        scene expression ("images/episode10/259_2.webp") with dissolve
        toby "Don't worry about me. I'll sleep on the couch. That's the least I could do."
        scene expression ("images/episode10/259_1.webp") with dissolve
        charlotte "The least you could do is sleep here with me."
        scene expression ("images/episode10/264.webp") with dissolve
        toby "Are you sure this is a good idea?"
        charlotte "You mean given what's going on between us?"
        toby "Exactly?"
        scene expression ("images/episode10/265.webp") with dissolve
        charlotte "I have no idea. I don't even know what's going on between us. All I know is that I don't want to be alone tonight."
        scene expression ("images/episode10/266.webp") with dissolve
        toby "Yeah. And all I know is that whenever I'm with you my heart beats faster."
        toby "When I look at you, all I can think about is how gorgeous you are. How caring, how intelligent you are. I don't have words to describe what I'm feeling when I'm with you."
        toby "When I look in your eyes, I get lost in the thought, it's very similar to when you fall in love."
        scene expression ("images/episode10/267.webp") with dissolve
        charlotte "But... I am your [mother]."
        toby "I know. That's what makes things so complicated, because what I feel right now for you is a little bit of everything."
        scene expression ("images/episode10/268.webp") with dissolve
        charlotte "You mean you love me like a [son], but also you love me like a man loves a woman?"
        toby "Exactly. It's a feeling so strong, I can't even put my finger on it."
        charlotte "I know exactly what you feel, because it's the same for me."
        scene expression ("images/episode10/269.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0
        charlotte "You are my [son]. The boy who I taught how to walk."

        scene expression ("images/episode10/270.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0
        toby "And you are my [mother], the woman who taught me how to ride a bike."

        scene expression ("images/episode10/271.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        charlotte "That was a bit difficult at first."

        scene expression ("images/episode10/272.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        toby "But you were always there for me."

        scene expression ("images/episode10/273.webp") with dissolve:
            xalign 0.0
            yalign 0.0
            linear 10.0 xalign 1.0 yalign 1.0
        charlotte "And I will always be. No matter what. Bad moments."

        scene expression ("images/episode10/274.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        charlotte "But also good moments, like when you went to prom. I was so proud of you."

        scene expression ("images/episode10/275.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0
        toby "Yeah... We remember my prom a little differently."
        charlotte "I was still proud of you. My boy was a man."

        scene expression ("images/episode10/276.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        charlotte "So yeah. It's that love."
        toby "But it's more than that."

        if ep1_groping_charlotte or _in_replay:
            scene expression ("images/episode10/277.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0

            charlotte "I still remember the first time you touched my breasts. I felt so excited, but I always blamed the alcohol."

            scene expression ("images/episode10/278.webp") with dissolve:
                xalign 1.0
                linear 10.0 xalign 0.0

            toby "You do have amazing breasts to be honest."
            charlotte "When did you look at them?"
            toby "Don't you remember when your t-shirt got pulled up during your work out?"
        else:

            scene expression ("images/episode10/278.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0
            toby "I can't stop thinking the time when I saw your bare breasts, during your work out."

        charlotte "I was so ashamed at that, but the fact that you got a boner made me so..."
        toby "Horny?"
        charlotte "I would say excited, but horny could work too."
        charlotte "That's when I figured it out that it felt good teasing you. I felt wanted. For the first time in many years."

        scene expression ("images/episode10/279.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        toby "And you do like to tease me."

        scene expression ("images/episode10/280.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0
        charlotte "It does make me feel good, but that's not all."
        charlotte "At first I thought it's merely the lack of attention, but that's not it."

        scene expression ("images/episode10/281.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        charlotte "Do you remember that after our first date, we were standing in front of the house, joking about kisses on the first date."
        toby "Yeah... All I wanted to do was kiss your gorgeous lips."
        charlotte "You have no idea how much I wanted that too and then just blame it on the alcohol and all."
        toby "That was really different than everything before."

        scene expression ("images/episode10/282.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0
        charlotte "It was never just [mother]ly love."
        toby "It was more than that."

        scene expression ("images/episode10/283.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.25
        charlotte "It is so much more."
        toby "I love you [mom]."
        charlotte "I love you too."

        show ep10_284 with dissolve
        $ unlockImage(persistent.charlotte_18)
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode10/284.webp")
        hide ep10_284

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Umm... I just kissed my [mother].{/i}"
        scene expression ("images/episode10/285.webp") with dissolve
        show ep10_285
        charlotte "Ummm... That was... Was so good."
        toby "It just felt so..."
        charlotte "Right and wrong at the same time?"
        toby "Yes!"
        show ep10_286 with dissolve
        hide ep10_285
        charlotte "Not so fast, cowboy. That was a one time thing. I'm still trying to process what's going on."
        toby "What is there to process? We both liked it."
        charlotte "That doesn't mean you're no longer my [son]."
        charlotte "Let's try and get some sleep. I can't think straight at the moment."
        scene expression ("images/episode10/286.webp")
        hide ep10_286
        scene expression ("images/episode10/287.webp") with dissolve:
            xalign 0.9
        charlotte "Do you have a t-shirt I can borrow?"
        scene expression ("images/episode10/287.webp") with dissolve:
            xalign 0.2
        toby "You could wear the lingerie."
        scene expression ("images/episode10/287.webp") with dissolve:
            xalign 0.9
        charlotte "You really want to see what Denise made me buy?"
        scene expression ("images/episode10/287.webp") with dissolve:
            xalign 0.2
        toby "Maybe?"
        scene expression ("images/episode10/287.webp") with dissolve:
            xalign 0.9
        charlotte "You naughty boy."

        scene expression ("images/episode10/288_1.webp") with dissolve:
            yalign 0.9
            linear 6.0 yalign 0.2

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode10/288_2.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode10/289.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode10/290_1.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode10/291.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode10/292.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode10/293.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode10/294.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        $ unlockMemory(persistent.memory_35)
        $ renpy.end_replay()

    return

label episode10_nightAlone:
    $ progress = 140
    scene expression ("images/episode10/258.webp") with dissolve
    toby "Do you want me to let you sleep?"
    scene expression ("images/episode10/259_1.webp") with dissolve
    charlotte "What about you?"
    scene expression ("images/episode10/259_2.webp") with dissolve
    toby "Don't worry. I'll sleep on the chouch."
    scene expression ("images/episode10/259_1.webp") with dissolve
    charlotte "I feel bad making you sleep on the couch."
    scene expression ("images/episode10/260.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode10/261.webp") with dissolve
    toby "It's the least I could do for you."
    scene expression ("images/episode10/262.webp") with dissolve
    charlotte "Thank you dear."
    scene expression ("images/episode10/263.webp") with fade
    $ ui.saybehavior()
    $ ui.interact()

    return

label episode10_end:
    $ progress = 141

    show screen ui_message("Meanwhile") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message

    scene expression ("images/episode10/295.webp"):
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/296.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/297.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/298.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/299.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/300.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/301.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/302.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/303.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode10/304.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if patricia_path:
        if charlotte_path:
            scene expression ("images/episode10/306.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode10/307.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()
        else:

            scene expression ("images/episode10/305.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()
    else:
        scene expression ("images/episode10/306.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode10/308.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
