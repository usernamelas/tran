image ep11_007_009 = Movie(play="video/episode11/007-009.webm", image="images/episode11/009.webp", loop = False)
image ep11_026_028 = Movie(play="video/episode11/026-028.webm", image="images/episode11/028.webp", loop = False)
image ep11_095 = Movie(play="video/episode11/095.webm", image="images/episode11/095.webp", loop = False)
image ep11_205 = Movie(play="video/episode11/205.webm", image="images/episode11/205.webp", loop = False)
image ep11_209 = Movie(play="video/episode11/209.webm", image="images/episode11/209.webp", loop = False)
image ep11_218 = Movie(play="video/episode11/218.webm", image="images/episode11/218.webp", loop = False)

label episode11:
    $ progress = 142
    scene expression ("images/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(2, 5) with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_newEpisode

    if patricia_path:
        stop music fadeout 10.0
        call episode11_nightTrisToby from _call_episode11_nightTrisToby
    else:
        call episode11_nightTrisRuns from _call_episode11_nightTrisRuns
    call episode11_nightBea from _call_episode11_nightBea

    call episode11_morning from _call_episode11_morning

    call episode11_jog from _call_episode11_jog

    if lisa_path or lauren_path:
        call episode11_beachGirls from _call_episode11_beachGirls
    else:
        call episode11_beaMessage from _call_episode11_beaMessage

    call episode11_beachTris from _call_episode11_beachTris

    if patricia_path:
        call episode11_dateTris from _call_episode11_dateTris

    return

label episode11_nightTrisToby:
    label memory_36:
        if _in_replay:
            scene expression ("images/utils/black.png") with dissolve
            menu:
                "[JGR] Kamar Tidur":
                    $ charlotte_path = True
                "ruang tamu":
                    $ charlotte_path = False

        if charlotte_path:

            scene expression ("images/episode11/001.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode11/002.webp") with dissolve:
                yalign 0.0
                linear 10.0 yalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode11/003.webp") with dissolve:
                xalign 0.0
                yalign 1.0
                linear 10.0 xalign 1.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode11/004.webp") with dissolve:
                yalign 0.0
                linear 10.0 yalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode11/005.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode11/006.webp") with dissolve:
                yalign 0.0
                linear 10.0 yalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            show ep11_007_009
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode11/009.webp") with dissolve
            hide ep11_007_009

            scene expression ("images/episode11/010.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What's going on? It feels like someone is giving me head.{/i}"

            scene expression ("images/episode11/011.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode11/012.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}What are you doing, [sis]?!{/i}"
            $ unlockImage(persistent.patricia_19)
            scene expression ("images/episode11/013.webp") with dissolve
            patricia "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I'm sucking your cock.{/i}"
            patricia "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}You like it?{/i}"
            scene expression ("images/episode11/014.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Good thing [mom] is sleeping so soundly.{/i}"
            scene expression ("images/episode11/015.webp") with dissolve
            patricia "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Oops... I didn't see her there.{/i}"
            scene expression ("images/episode11/016.webp") with dissolve
            patricia "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I'm going to continue now, so be quiet there or we're both in trouble.{/i}"
            scene expression ("images/episode11/017.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}What are you doing?{/i}"
            scene expression ("images/episode11/018.webp") with dissolve
            patricia "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}What do you mean? I'm going to suck your cock. I heard that men like it.{/i}"

            scene expression ("images/episode11/019.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}No you're not.{/i}"
            patricia "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Why not? You don't like it?{/i}"
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}You're drunk. Let's go outside.{/i}"
            patricia "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}You want me to suck your cock outside so [mom] doesn't hear us and wake up?{/i}"
            scene expression ("images/episode11/020.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}No! You're not sucking my cock. You're drunk. Let's go outside.{/i}"
            patricia "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I'm not good enough for you? I thought you liked little sluts.{/i}"
            scene expression ("images/episode11/021.webp") with dissolve
            toby "Ayo, di lantai bawah, sekarang!"
        else:

            scene expression ("images/episode11/022.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode11/023.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode11/024.webp") with dissolve:
                xalign 0.0
                yalign 0.0
                linear 10.0 xalign 1.0 yalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode11/025.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            show ep11_026_028
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode11/028.webp") with dissolve
            hide ep11_026_028


            scene expression ("images/episode11/029.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What's going on? It feels like someone's giving me head.{/i}"

            scene expression ("images/episode11/030.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode11/031.webp") with dissolve
            toby "Apa yang kamu lakukan, [sis]?!"
            $ unlockImage(persistent.patricia_19)
            scene expression ("images/episode11/032.webp") with dissolve
            patricia "Aku mengisap penismu."
            patricia "Anda menyukainya?"
            toby "Anda mabuk, [sis]!"
            scene expression ("images/episode11/033.webp") with dissolve
            patricia "Jadi apa? Anda masih bisa menikmatinya."

            scene expression ("images/episode11/034.webp") with dissolve
            toby "Hentikan. Aku tidak akan membiarkanmu mengisap penisku. Anda mabuk!"
            patricia "Aku tidak cukup baik untukmu? Saya pikir Anda menyukai pelacur kecil."

        $ unlockMemory(persistent.memory_36)
        $ renpy.end_replay()

    $ progress = 143
    scene expression ("images/episode11/035.webp") with dissolve
    toby "Lihat. Itu tidak ada hubungannya dengan apakah saya suka atau tidak, itu adalah fakta bahwa Anda mabuk."
    patricia "Tetapi ketika saya mencoba melakukan sesuatu yang baik untuk Anda, Anda menghentikan saya.Jadi apa? Anda selalu mengatakan bahwa Anda mencintaiku. Anda pikir saya cantik."
    scene expression ("images/episode11/036_sad.webp") with dissolve
    if emma_break == False:
        patricia "Mungkin alkoholnya adalah apa yang saya butuhkan. Saya bukan pelacur seperti pacar Anda."
    else:
        patricia "Mungkin alkoholnya adalah apa yang saya butuhkan. Saya bukan pelacur seperti mantan pacar Anda."
    scene expression ("images/episode11/036_normal.webp") with dissolve
    patricia "Aku hanya ingin mendapatkan cintamu."
    scene expression ("images/episode11/037_normal.webp") with dissolve
    toby "Tapi aku sangat mencintaimu. Anda tidak perlu melakukan apa pun untuk itu. Anda sedikit [sister] dan saya akan selalu mencintaimu."
    scene expression ("images/episode11/036_sad.webp") with dissolve
    if emma_break == False:
        patricia "Tapi Anda mencintai Emma lebih dari Anda mencintaiku, karena dia membiarkan Anda melakukan segala macam hal keriting padanya."
        scene expression ("images/episode11/037_sad.webp") with dissolve
        toby "Itu tidak benar. Emma tidak dapat dibandingkan dengan perasaan saya tentang Anda. Anda adalah [sister] saya."
    else:
        patricia "Tapi Anda akan menemukan orang lain dan melupakan saya."
        scene expression ("images/episode11/037_sad.webp") with dissolve
        toby "Lihat, Tris. Anda adalah [sister] saya dan saya akan selalu mencintaimu, tidak peduli siapa saya kencan."

    scene expression ("images/episode11/036_sad.webp") with dissolve
    patricia "Tapi aku ingin kamu ..."
    scene expression ("images/episode11/037_curious.webp") with dissolve
    toby "Anda ingin saya apa?"
    scene expression ("images/episode11/036_sad.webp") with dissolve
    patricia "Tidak ada apa-apa. Saya ingin tidur."
    scene expression ("images/episode11/037_normal.webp") with dissolve
    toby "Mari kita bicara di pagi hari, saat Anda sedikit lebih sadar."
    if charlotte_path:
        scene expression ("images/episode11/036_curious.webp") with dissolve
        patricia "Tunggu sebentar. Mengapa [mom] di tempat tidur Anda?"
        scene expression ("images/episode11/037_sad.webp") with dissolve
        toby "Dia dan [dad] bertengkar, jadi saya menawarkan untuk membiarkannya tidur di tempat tidur saya."
        scene expression ("images/episode11/036_normal.webp") with dissolve
        patricia "Dia memakai pakaian dalam seksi."
        scene expression ("images/episode11/038.webp") with dissolve
        patricia "Saya yakin Anda tidak akan berhenti [mom] jika dia mencoba memberi Anda blowjob."
    else:
        scene expression ("images/episode11/038.webp") with dissolve
        patricia "Apa pun."


    scene expression ("images/episode11/039.webp") with dissolve:
        xalign 0.5
        yalign 0.5
        zoom 0.8
        linear 20.0 zoom 1.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Well, there's no denying it now. That guy she was talking about with [aunt] Denise was actually me.{/i}"

    scene expression ("images/episode11/040.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}My little [sister] is in love with me, but maybe I'm in love with her too?{/i}"

    scene expression ("images/episode11/041.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}If I'm honest with myself, I've been looking at her differently for quite a while now. She's not the annoying spoiled brat she used to be.{/i}"

    scene expression ("images/episode11/042.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Ok, so she's still a little annoying. But she's a beautiful, smart woman, who I really like. I've been so hung up on the fact that she was [family].{/i}"

    scene expression ("images/episode11/043.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    if charlotte_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But so is [mom]. We're [family], which I think could make this even more special.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But I think this could be even better, because no matter what she'll always be there for me and I will for her.{/i}"

    scene expression ("images/episode11/044.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm going to tell her how I feel. I can't put it off any longer.{/i}"

    scene expression ("images/episode11/045.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I have to be honest with her. She's my [sister] and I love her too.{/i}"

    scene expression ("images/episode11/046.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Ummm... She's not here. Where the hell is she? Maybe she's in the back yard.{/i}"

    scene expression ("images/episode11/047.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... She's not here either. Maybe she went to talk to [mom].{/i}"

    scene expression ("images/episode11/048.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Nope... not here. Where could she be?{/i}"

    scene expression ("images/episode11/049.webp") with dissolve:
        xalign 0.0
        yalign 0.0
        linear 20.0 xalign 1.0 yalign 1.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Uhh... Where are my keys?{/i}"

    scene expression ("images/episode11/050.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Please, please, tell me you didn't take off on my bike.{/i}"

    scene expression ("images/episode11/051.webp") with dissolve:
        xalign 0.5
        yalign 0.5
        zoom 0.8
        linear 10.0 zoom 1.3 yalign 0.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck! She ran away.{/i}"

    scene expression ("images/episode11/052.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She ran away because of me. She must have felt ashamed that I stopped her. Why the fuck did I stop her?{/i}"

    scene expression ("images/episode11/053.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I really liked it. She wasn't the best, but she wasn't the worst, either. She did it out of love.{/i}"

    scene expression ("images/episode11/054.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Please, [sis]. Pick up the phone. Don't do anything stupid.{/i}"

    scene expression ("images/episode11/055.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck! I messed this up. Where could she be?{/i}"

    scene expression ("images/episode11/054.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Come on... Pick up the phone. Come on, [sis]!{/i}"

    scene expression ("images/episode11/055.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What am I going to do now?{/i}"

    scene expression ("images/episode11/056.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should probably wake [mom] up.{/i}"

    return

label episode11_nightTrisRuns:
    $ progress = 143
    scene expression ("images/episode11/057.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()


    scene expression ("images/episode11/041.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if charlotte_path:
        scene expression ("images/episode11/058.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Ummm... What just happened? What was Tris doing in my room? I should go check on her.{/i}"
    else:

        scene expression ("images/episode11/059.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Was that Tris? Let me check her room.{/i}"


    scene expression ("images/episode11/043.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if charlotte_path == False:
        scene expression ("images/episode11/044.webp") with dissolve:
            xalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()


    scene expression ("images/episode11/045.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/046.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's not here. Maybe she's in the back yard.{/i}"

    scene expression ("images/episode11/047.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Nope... She's not here either. Maybe she didn't get home yet. I should go back to sleep.{/i}"


    if charlotte_path:
        scene expression ("images/episode11/048.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Something feels off.{/i}"
    else:

        scene expression ("images/episode11/048.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I forgot [mom] was sleeping in my room.{/i}"

    scene expression ("images/episode11/049.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Wait... Where are my keys?{/i}"

    scene expression ("images/episode11/050.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Don't tell me she took off with my bike.{/i}"

    scene expression ("images/episode11/051.webp") with dissolve:
        xalign 0.5
        yalign 0.5
        zoom 0.8
        linear 10.0 zoom 1.3 yalign 0.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, fuck, fuck! She left with my bike!{/i}"

    scene expression ("images/episode11/052.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I hope she's ok... What happened? Where did she go?{/i}"

    scene expression ("images/episode11/053.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why did she run away?{/i}"

    scene expression ("images/episode11/054.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Come on, stupid. Answer your phone.{/i}"

    scene expression ("images/episode11/055.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What's gotten into her? I'll try again.{/i}"

    scene expression ("images/episode11/054.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Answer the fucking phone.{/i}"

    scene expression ("images/episode11/055.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit! I don't know what to do.{/i}"

    scene expression ("images/episode11/056.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should probably wake [mom] up.{/i}"

    return

label episode11_nightBea:
    $ progress = 144
    scene expression ("images/episode11/060.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I got a message from an unknown number. I wonder who it is.{/i}"
    scene expression ("images/episode11/061_texting.webp") with dissolve
    call sms_incoming ("unknown", "Hey, [toby!c]. This is Bea. Please don't freak out, but your [sister] stole your bike and came to my place. She's a little drunk, but she's fine.") from _call_sms_incoming_204
    call sms_incoming ("unknown", "I'm not sure what's going on, but she's crying. Please cover for her tonight. Tell your [mom] she told you she's spending the night at my place. I'll try to talk to her to see what's wrong.") from _call_sms_incoming_205
    if beatrice_path:
        call sms_sent ("unknown", "Hi Bea. I'll come to pick her up.") from _call_sms_sent_156
    else:
        call sms_sent ("unknown", "Hi Bea. Send me the address. I'll come to pick her up.") from _call_sms_sent_157
    if patricia_path:
        call sms_incoming ("unknown", "Don't come... Please! Let me talk to her. She seems like she's pissed at you. If you show up, she'll know that I told you and won't trust me again.") from _call_sms_incoming_206
    else:
        call sms_incoming ("unknown", "Don't come... Please! Let me talk to her. If you show up, she'll know that I told you where she was and she'll stop trusting me.") from _call_sms_incoming_207
    call sms_sent ("unknown", "Let me talk to her.") from _call_sms_sent_158
    call sms_incoming ("unknown", "Please, [toby!c].") from _call_sms_incoming_208
    if beatrice_path:
        call sms_sent ("unknown", "Bea! She's my little [sister], I'm worried about her.") from _call_sms_sent_159
        call sms_incoming ("unknown", "Please don't make a scene.") from _call_sms_incoming_209
    else:
        call sms_sent ("unknown", "Bea! She's my little [sister], I'm worried about her. Send me the address!") from _call_sms_sent_160
        call sms_incoming ("unknown", "Please don't make a scene.", img_icon="images/episode11/062_icon.webp") from _call_sms_incoming_210
    hide screen message


    scene expression ("images/episode11/060.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She lives pretty close. If I run I'm there in like 15 minutes.{/i}"

    scene expression ("images/episode11/063.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/064.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/065.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/066.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    if beatrice_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Oh boy...{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This looks to be the right place.{/i}"

    scene expression ("images/episode11/067_texting.webp") with dissolve
    call sms_sent ("unknown", "I'm downstairs. Tell Tris to come down.") from _call_sms_sent_161
    call sms_incoming ("unknown", "One second.") from _call_sms_incoming_211
    call sms_sent ("unknown", "Thank you, Bea!") from _call_sms_sent_162
    hide screen message

    scene expression ("images/episode11/068.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Tonight I'll be a good [brother] and talk to her about what's bothering her, but tomorrow I'm going to have a serious conversation about this incident.{/i}"
    beatrice "Hai [toby!c]."

    scene expression ("images/episode11/069.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    toby "Hai Bea. Di mana saya [sister] saya?"
    scene expression ("images/episode11/070.webp") with dissolve
    beatrice "Dia sudah pingsan. Tolong biarkan saya berbicara dengannya di pagi hari, karena dia tidak masuk akal."
    if patricia_path:
        scene expression ("images/episode11/071_normal.webp") with dissolve
        beatrice "Dia mengatakan dia kesal pada Anda, tetapi juga bahwa dia frustrasi pada seorang pria. Awalnya saya pikir dia berbicara tentang Anda, tetapi dia tidak masuk akal sehingga dia pasti berbicara tentang orang lain."
    scene expression ("images/episode11/071_sad.webp") with dissolve
    beatrice "Saya berjanji kepada Anda bahwa besok saya akan mendapatkannya pulang, tapi tolong tutupi dia dengan [mother] Anda."
    beatrice "Biarkan saya berbicara dengannya dulu. Dia benar -benar membutuhkan teman."
    scene expression ("images/episode11/072_normal.webp") with dissolve
    toby "Saya tidak tahu Bea. Dia melarikan diri dari rumah. Itu tidak bagus."
    scene expression ("images/episode11/071_laugh.webp") with dissolve
    beatrice "Saya bisa tahu dari bagaimana Anda datang ke sini dan begitu cepat sehingga Anda mengkhawatirkannya. Saya berharap saya memiliki [brother] seperti Anda, tetapi ini pertama kalinya melakukan sesuatu yang bodoh ini."
    scene expression ("images/episode11/072_laugh.webp") with dissolve
    toby "Anda benar. Dia tidak bodoh. Itu biasanya saya."
    scene expression ("images/episode11/071_curious.webp") with dissolve
    beatrice "Apa kabar?"
    scene expression ("images/episode11/072_normal.webp") with dissolve
    toby "Dia selalu ada untuknya.Saya khawatir Bea. Saya tidak tahu cara menangani ini. Saya tidak ingin memberi tahu [mom], tapi mungkin saya harus melakukannya karena mereka dulu adalah teman baik."
    scene expression ("images/episode11/071_normal.webp") with dissolve
    beatrice "Ada hal -hal yang tidak bisa dia katakan padanya [mother], meskipun mereka rukun."
    scene expression ("images/episode11/071_smile.webp") with dissolve
    beatrice "Biarkan saya berbicara dengannya dan meyakinkannya."
    if patricia_path:
        scene expression ("images/episode11/072_curious.webp") with dissolve
        toby "Apakah dia mengatakan sesuatu tentang apa yang terjadi di rumah?"
        scene expression ("images/episode11/071_smile.webp") with dissolve
        beatrice "Hanya saja Anda tidak menghargainya dan bahwa Anda idiot. Kemudian dia mulai berbicara tentang beberapa pria yang menolaknya. Saya tidak tahu siapa dia, tetapi pasti bodoh untuk menolak seorang gadis seperti Tris."
        scene expression ("images/episode11/072_normal.webp") with dissolve
        toby "Ya ... dia pasti sangat bodoh."
    scene expression ("images/episode11/073.webp") with dissolve
    beatrice "Ngomong -ngomong, inilah kunci untuk sepeda Anda. Sembunyikan lebih baik di lain waktu, karena [sister] Anda tidak tahu cara mengendarai sepeda. Saya terkejut dia berhasil sampai di sini dalam keadaan utuh."
    toby "Ya. Saya pikir sudah waktunya membeli helm juga."
    beatrice "Anda tidak punya satu? Saya pikir dia hanya melupakannya."
    toby "Ummm ... ya ..."
    if beatrice_path:
        scene expression ("images/episode11/074.webp") with dissolve
        toby "Bagaimanapun, terima kasih atas segalanya. Tolong beri tahu saya bagaimana keadaannya."
        scene expression ("images/episode11/075.webp") with dissolve
        beatrice "Tentu saja, [toby!c]."
        $ unlockImage(persistent.beatrice_03)
        scene expression ("images/episode11/076.webp") with dissolve
    else:
        scene expression ("images/episode11/076.webp") with dissolve
        toby "Bagaimanapun, terima kasih atas segalanya. Tolong beri tahu saya bagaimana keadaannya."
        beatrice "Tentu saja, [toby!c]."
    toby "Sampai jumpa lagi."
    beatrice "Hati-hati di jalan!"
    scene expression ("images/episode11/077.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode11/078.webp") with dissolve
    if charlotte_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'll sleep downstairs tonight. I don't want to wake [mom] up.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Ugh! What a night. I need to get some sleep.{/i}"
    scene expression ("images/episode11/079.webp") with dissolve
    if patricia_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I really need to talk to Tris. Tell her how I feel.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}God, I was stupid. I knew for so long, yet I did nothing.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wonder how much she drank to get the courage to go up there and put my dick in her mouth.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She clearly needs to be careful with her alcohol.{/i}"
    else:
        pass

    scene expression ("images/utils/black.png") with Fade(5.0, 0.0, 1.0)
    $ ui.saybehavior()
    $ ui.interact()

    return

label episode11_morning:
    $ progress = 145
    show screen ui_message("Saturday") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    hide screen ui_message
    scene expression ("images/episode11/080.webp") with dissolve
    charlotte "Sayang. Bangun!"
    scene expression ("images/episode11/081.webp") with dissolve
    toby "Ugggghhh ... biarkan aku tidur."
    charlotte "Sayang, apakah kamu tahu di mana Tris? Teleponnya dimatikan."
    scene expression ("images/episode11/082.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit!{/i}"
    toby "Pagi!"
    scene expression ("images/episode11/083.webp") with dissolve
    toby "Ya saya lakukan. Dia membangunkanku tadi malam untuk membawanya menjadi \ 'a. Dia pulang untuk mengambil beberapa pakaian dan kemudian aku membawanya."
    scene expression ("images/episode11/084.webp") with dissolve
    charlotte "Tapi teleponnya dimatikan."
    scene expression ("images/episode11/083.webp") with dissolve
    toby "Mungkin baterainya mati dan BEA memiliki jenis pengisi daya yang berbeda?"
    scene expression ("images/episode11/085.webp") with dissolve
    charlotte "Mungkin Anda benar!"
    if charlotte_path:
        scene expression ("images/episode11/086.webp") with dissolve
        toby "Kemarilah. Tidak perlu khawatir, semuanya baik -baik saja."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I hope!{/i}"

    scene expression ("images/episode11/087.webp") with dissolve
    erwin "Pagi."
    scene expression ("images/episode11/088.webp") with dissolve
    charlotte "..."
    scene expression ("images/episode11/089.webp") with dissolve
    erwin "Sayang, bisakah kita bicara? Silakan!"
    scene expression ("images/episode11/088.webp") with dissolve
    charlotte "Saya tidak punya apa -apa untuk dikatakan kepada Anda dan saya tidak tertarik pada apa pun yang ingin Anda katakan kepada saya."
    scene expression ("images/episode11/090.webp") with dissolve
    erwin "Saya pergi bekerja kalau begitu. Semoga harimu menyenangkan."
    scene expression ("images/episode11/091.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode11/092_1.webp") with dissolve
    toby "Kamu oke?"
    if charlotte_path:
        scene expression ("images/episode11/092_2.webp") with dissolve
        charlotte "Ya, saya baik -baik saja. Terima kasih, kepedulian saya [son]."
        scene expression ("images/episode11/093_smile.webp") with dissolve
        toby "Tadi malam adalah ..."
        scene expression ("images/episode11/094_smile.webp") with dissolve
        charlotte "Menarik?"
        scene expression ("images/episode11/093_normal.webp") with dissolve
        toby "Saya pergi untuk cantik."
        scene expression ("images/episode11/094_sad.webp") with dissolve
        charlotte "Itu sempurna, tetapi itu tidak mengubah fakta bahwa saya adalah [mother] dan saya juga menikah."
        scene expression ("images/episode11/093_normal.webp") with dissolve
        toby "Jadi?"
        scene expression ("images/episode11/094_smile.webp") with dissolve
        charlotte "Lihat, saya tidak ingin Anda berpikir bahwa saya mengambil satu langkah maju & dua langkah mundur. Apa yang kita miliki sangat istimewa. Saya tidak pernah merasakan hal seperti itu."
        scene expression ("images/episode11/094_cute.webp") with dissolve
        charlotte "Jantungku memompa keluar dari dadaku ketika aku menciummu. Merasa bibir Anda di bibir saya persis seperti yang saya butuhkan, tetapi seperti yang saya katakan, itu salah."
        scene expression ("images/episode11/093_curious.webp") with dissolve
        toby "Itu karena masyarakat kita berpikir itu salah dan kita telah dikondisikan untuk berpikir seperti ini. Dalam masyarakat kita, salah untuk mencium [mother], tetapi kami melakukannya dan rasanya luar biasa."
        scene expression ("images/episode11/094_sad.webp") with dissolve
        charlotte "Itu lebih dari hebat, tapi itu bukan satu -satunya masalah. Masalahnya adalah [father] Anda mengatakan saya adalah pelacur karena selingkuh dan meskipun itu tidak benar saat itu, sekarang."
        charlotte "Saya tidak pernah berselingkuh padanya.Aku menipu dia ... denganmu. Saya menipu [father] Anda dengan Anda. Saya merasa tidak enak."
        scene expression ("images/episode11/093_normal.webp") with dissolve
        toby "Tapi hubungan Anda sudah rusak dan itu hanya ciuman."
        scene expression ("images/episode11/094_normal.webp") with dissolve
        charlotte "Meskipun demikian. Itu tidak benar dan tidak, itu bukan hanya ciuman. Itu jauh lebih buruk daripada jika saya berhubungan seks dengan seseorang yang tidak saya cintai. Bagi saya itu lebih dari sekadar ciuman sederhana."
        scene expression ("images/episode11/094_cute.webp") with dissolve
        charlotte "Itu adalah ciuman paling emosional yang pernah ada. Saya tidak pernah merasakan hal seperti itu sebelumnya. Pada saat itu, saya lupa saya memiliki seorang suami, saya lupa tentang apa yang dipikirkan masyarakat kita tentang ini, dan yang saya inginkan hanyalah saat itu untuk tidak pernah berakhir."
        scene expression ("images/episode11/093_smile.webp") with dissolve
        toby "Aku mencintaimu, [mom]."
        scene expression ("images/episode11/094_smile.webp") with dissolve
        charlotte "Aku juga mencintaimu dan tidak ada yang tidak akan kulakukan untukmu, tapi aku bingung sekarang."
        scene expression ("images/episode11/093_smile.webp") with dissolve
        toby "Saya mengerti. Saya tidak bisa mengatakan saya sepenuhnya mengerti apa yang terjadi atau bagaimana menanganinya, tetapi yang saya tahu adalah bahwa saya tidak ingin ini berakhir."
        scene expression ("images/episode11/093_normal.webp") with dissolve
        toby "Apa yang kami miliki tadi malam itu sempurna. Saya tidak ingin kehilangan itu."
        scene expression ("images/episode11/094_sad.webp") with dissolve
        charlotte "Aku tidak sayang, tapi aku masih perlu memikirkan hal ini. Saya tidak pernah berpikir saya akan berada dalam situasi ini dan saya tidak tahu bagaimana menanganinya."
        scene expression ("images/episode11/094_normal.webp") with dissolve
        charlotte "Tolong jangan marah padaku, tapi aku benar -benar perlu waktu untuk mencerna semuanya dan sekarang aku tidak di tempat yang tepat. Saya hanya bertengkar besar dengan [father] Anda dan saya tidak ingin keputusan saya dipengaruhi oleh itu."
        scene expression ("images/episode11/094.webp") with dissolve
        toby "Bagaimana saya bisa marah pada Anda, [mom]? Aku mencintaimu!"
        charlotte "Aku pun mencintaimu."
        $ unlockImage(persistent.charlotte_19)
        show ep11_095
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode11/095.webp") with dissolve
        hide ep11_095
        charlotte "Anda akan menjadi kematian saya."
        toby "Saya mengatakan bahwa kita berada di kapal yang sama."
    else:
        scene expression ("images/episode11/092_2.webp") with dissolve
        charlotte "Ya, saya baik -baik saja."
        scene expression ("images/episode11/093_curious.webp") with dissolve
        toby "Ingin membicarakannya?"
        scene expression ("images/episode11/094_smile.webp") with dissolve
        charlotte "Anda manis sayang, tapi tidak. Saya baik-baik saja. Tidak ada yang perlu dibicarakan."
        scene expression ("images/episode11/094_sad.webp") with dissolve
        charlotte "Saya hanya perlu waktu untuk memproses segalanya dan memutuskan cara terbaik untuk menanganinya."
        scene expression ("images/episode11/093_normal.webp") with dissolve
        toby "Jika Anda perlu membicarakan apa pun, ketahuilah bahwa saya di sini untuk Anda."
        scene expression ("images/episode11/094_smile.webp") with dissolve
        charlotte "Terima kasih sayang. Saya tahu saya memiliki yang terbaik di dunia."
        scene expression ("images/episode11/096.webp") with dissolve
        charlotte "Aku mencintaimu sayang."
        toby "Saya juga [mom]."

    scene expression ("images/episode11/097.webp") with dissolve
    charlotte "Ngomong -ngomong, aku akan mandi."
    if charlotte_path:
        toby "Dan saya pikir saya akan jogging. Saya benar -benar perlu menjernihkan kepala saya, karena saya tidak ingin melakukan apa pun yang akan mendorong Anda menjauh dari saya."
        scene expression ("images/episode11/098.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And also to try to figure out what I'm going to do about Tris.{/i}"
    else:
        toby "Dan saya pikir saya akan jogging."
        scene expression ("images/episode11/098.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I really need to think about the whole Tris situation.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It would kill her to know that Tris ran away.{/i}"
    scene expression ("images/episode11/099.webp") with dissolve
    charlotte "Baiklah, sayang. Tidak usah buru-buru!"

    return

label episode11_jog:
    $ progress = 146

    scene expression ("images/episode11/100.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's do this. Hopefully it will help me clear my head.{/i}"
    scene expression ("images/episode11/101.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I can't believe my [sister] ran away from home, it's not like her.{/i}"
    if patricia_path:
        scene expression ("images/episode11/102.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I mean. I get it, she thinks I rejected her, but she was drunk. It would have been worse if I let her continue.{/i}"
        scene expression ("images/episode11/103.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But even so, she started to suck my cock. My cock was inside her mouth. What was she thinking?{/i}"
        scene expression ("images/episode11/104.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And she kept mentioning that I like sluts. I don't think I've only dated sluts. Yeah, so Emma didn't exactly have the best reputation in High School, but that's because she was popular. She wasn't a slut.{/i}"
        scene expression ("images/episode11/105.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And Tris really went all out trying suck my dick hoping to earn my love. I don't need that to love her. She should know better.{/i}"
    else:
        scene expression ("images/episode11/102.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I mean, what happened in the club yesterday? I really need to talk to Bea.{/i}"
        scene expression ("images/episode11/103.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But I also need to talk to Tris. What she did was dangerous. Getting on a bike after drinking, that could have been really bad.{/i}"
        scene expression ("images/episode11/104.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She wasn't thinking straight. Something's going on with her. She was never like this. She would have never have run away from home.{/i}"
        scene expression ("images/episode11/105.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I would have understood if she ran away with a guy because [mom] wouldn't let her date him, but that's not the issue. What could it be?{/i}"

    if charlotte_path:
        scene expression ("images/episode11/106.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And last night. What was that? Did I really kiss my [mother]? It was so passionate.{/i}"
        scene expression ("images/episode11/107.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It was full of emotion. We both wanted it, and I do understand that she needs some time to think it through. After all, she has always been against cheating.{/i}"
        scene expression ("images/episode11/108.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I remember when I first started dating Mia, my first girlfriend, all she ever said to me was stay faithful to her.{/i}"
        scene expression ("images/episode11/109.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But even so, we can't ignore what we felt when we kissed. It was so intense and pure and beautiful. It was just perfect.{/i}"
        scene expression ("images/episode11/110.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}How could I not want more of that.{/i}"
    else:
        scene expression ("images/episode11/106.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And then there is last night. The fight [mom] and [dad] had. How can someone be such an ass with his wife. I get that it's difficult to deal erectile dysfunction, but still. She's your fucking wife.{/i}"
        scene expression ("images/episode11/107.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}You married that woman because you loved her and because you wanted to spend your whole life together, not only to have sex for the rest of your life with one person. {/i}"
        scene expression ("images/episode11/108.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}If sex is what you're looking for then you don't get married, you go to a whorehouse and have as much as you want. That is your wife, the woman who you share both good and bad with. Unfortunately a lot of people forget why they got married in the first place.{/i}"
        scene expression ("images/episode11/109.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And even if they weren't married, a woman like [mom] needs to be respected. She was always there for you no matter what. Good or bad. I really don't get these people.{/i}"
        scene expression ("images/episode11/110.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}All I know is that I want all this to be over. I really don't care how, but it has to be over. It would be nice to be a happy [family] again, but I don't see that happening anytime soon.{/i}"

    return

label episode11_beachGirls:
    play sound "audio/fx/car-horn.mp3"
    $ progress = 147

    scene expression ("images/episode11/111.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/112.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/113.webp") with dissolve
    lauren "Hey seksi. Butuh tumpangan?"
    scene expression ("images/episode11/114.webp") with dissolve
    toby "Oh ... Hai Girls. Apa yang sedang kamu lakukan?"
    if lisa_path:
        scene expression ("images/episode11/115.webp") with dissolve
        lisa "Kami pergi ke pantai. Ingin datang?"
    else:
        scene expression ("images/episode11/113.webp") with dissolve
        lauren "Kami pergi ke pantai untuk berjemur. Ingin melihat?"
    scene expression ("images/episode11/117.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It could be a good thing to go to the beach and forget about everything for a bit. Just relax.{/i}"
    scene expression ("images/episode11/114.webp") with dissolve
    toby "Saya ingin, tetapi saya harus kembali ke rumah terlebih dahulu, mandi dan mendapatkan batang saya."
    toby "Sampai jumpa di sana?"
    scene expression ("images/episode11/116.webp") with dissolve
    lauren "Omong kosong. Anda bisa datang seperti itu. Anda bisa mandi di laut."
    scene expression ("images/episode11/114.webp") with dissolve
    toby "Anda lupa bagian batangnya."
    scene expression ("images/episode11/116.webp") with dissolve
    lauren "Itu tidak akan adil bagi kita karena kita telanjang jadi kita tidak mendapatkan garis tan."
    scene expression ("images/episode11/118.webp") with dissolve
    lauren "Benar? Anda tidak mengubah pikiran Anda."
    scene expression ("images/episode11/119.webp") with dissolve
    lisa "Ummm ..."
    lauren "Tentu saja tidak, setelah semua Anda kehilangan taruhan. Anda tidak dapat kembali sekarang."
    scene expression ("images/episode11/116.webp") with dissolve
    lauren "Jadi? Apa yang kamu katakan koboi? Peduli untuk bergabung dengan kami? Kami benar -benar dapat menggunakan pria yang kuat dengan kami untuk melindungi kami dari creep."
    scene expression ("images/episode11/114.webp") with dissolve
    toby "Ummm ... kamu berantakan denganku kan?"
    scene expression ("images/episode11/113.webp") with dissolve
    lauren "Tidak, kami tidak! Aku sangat membenci garis tan dan Lisa kehilangan taruhan, jadi dia tidak punya pilihan."
    scene expression ("images/episode11/120.webp") with dissolve
    toby "Persetan ... lepaskan."
    if lisa_path:
        scene expression ("images/episode11/121.webp") with dissolve
        lisa "Kamu kecil. Segera setelah Anda mendengar bahwa kami akan telanjang, Anda melompat ke dalam mobil."
    else:
        scene expression ("images/episode11/122.webp") with dissolve
        lauren "Sudah kubilang dia adalah Perved yang paling keren."
    scene expression ("images/episode11/123.webp") with dissolve
    toby "Dalam pembelaan saya, saya benar -benar perlu melepaskan pikiran saya, jadi pergi ke pantai benar -benar dapat membantu saya."
    scene expression ("images/episode11/124.webp") with dissolve
    lauren "Dan melihat dua keindahan telanjang bahkan lebih baik."
    if lisa_path:
        scene expression ("images/episode11/125.webp") with dissolve
        toby "Maaf sayang, tapi saya hanya tertarik pada satu kecantikan telanjang."
        scene expression ("images/episode11/127.webp") with dissolve
        lisa "Aduh ... itu pasti menyakiti ego Anda."
        scene expression ("images/episode11/128.webp") with dissolve
        lauren "Apa yang membuatmu berpikir dia membicarakanmu?"
        scene expression ("images/episode11/127.webp") with dissolve
        lisa "Jangan khawatir. Dia pintar dan tahu apa yang terbaik untuknya."
        scene expression ("images/episode11/129.webp") with dissolve
        lisa "Jadi [toby!c], saya tidak tahu Anda suka joging."
    else:
        scene expression ("images/episode11/126.webp") with dissolve
        toby "Apa yang bisa saya katakan. Saya seorang pria sederhana."
        scene expression ("images/episode11/127.webp") with dissolve
        lisa "Mhmmm ... mari kita bicara tentang hal lain, sebelum kalian berdua berakhir berhubungan seks di mobil saya."
        scene expression ("images/episode11/128.webp") with dissolve
        lauren "Anda ingin melihat itu, tidakkah Anda?"
        scene expression ("images/episode11/129.webp") with dissolve
        lisa "Jadi, [toby!c], apakah Anda sering jogging?"

    scene expression ("images/episode11/130.webp") with dissolve
    toby "Saya tidak. Hanya saja saya memiliki banyak hal di pikiran saya dan saya perlu menjernihkan kepala saya."
    scene expression ("images/episode11/131.webp") with dissolve
    lauren "Apakah semuanya baik -baik saja?"
    scene expression ("images/episode11/132.webp") with dissolve
    toby "Ya, jangan khawatir. Tidak apa -apa."

    scene expression ("images/episode11/133.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/134.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/135.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/136.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/137.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/138.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/139.webp") with dissolve
    lisa "Tolong berbalik sehingga kami bisa berubah."
    scene expression ("images/episode11/140.webp") with dissolve
    toby "Apa gunanya aku berbalik karena kita akan telanjang bersama?"
    scene expression ("images/episode11/141.webp") with dissolve
    lauren "Karena dia sedikit malu."
    scene expression ("images/episode11/139.webp") with dissolve
    lisa "Ya, maksud saya kita semua berbalik, telanjang dan kemudian pada hitungan tiga kita berbalik, jadi itu akan menjadi dampak yang sama untuk semua orang."
    scene expression ("images/episode11/142.webp") with dissolve
    lauren "Anda selalu sangat pemalu, tetapi jika itu aturannya."
    scene expression ("images/episode11/143.webp") with dissolve
    lauren "Beri tahu saya saat Anda semua berbalik."
    scene expression ("images/episode11/144.webp") with dissolve
    lisa "Saya siap. [toby!c], beri tahu kami saat Anda berbalik."
    scene expression ("images/episode11/145.webp") with dissolve
    toby "Ummm ... ini agak aneh tapi apa pun. Aku berbalik."
    scene expression ("images/episode11/146.webp") with dissolve
    lauren "Oke kalau begitu ... semua orang menjatuhkan celana dalammu."
    scene expression ("images/episode11/147.webp") with dissolve
    lisa "Saya tidak tahu apakah saya bisa melakukan ini."
    if lisa_path:
        scene expression ("images/episode11/148.webp") with dissolve
        lauren "Ayo. Dia melihatmu telanjang sebelumnya. Aku harus menjadi yang gugup, bukan kamu. Bagaimana jika dia menatapku dan mendapat kesalahan?"
    else:
        scene expression ("images/episode11/148.webp") with dissolve
        lauren "Saya berjanji dia bukan beberapa perv. Mungkin dia akan menatapmu sebentar, mendapatkan kesalahan dan itu ..."
    scene expression ("images/episode11/149.webp") with dissolve
    toby "Tidak ada yang akan mendapatkan kesalahan."
    scene expression ("images/episode11/150.webp") with dissolve
    lauren "Oke. Kami siap. Haruskah kita berbalik?"
    scene expression ("images/episode11/151.webp") with dissolve
    toby "Setiap kali Anda siap."
    scene expression ("images/episode11/152.webp") with dissolve
    lisa "Satu."
    scene expression ("images/episode11/153.webp") with dissolve
    lauren "Dua."
    scene expression ("images/episode11/154.webp") with dissolve
    toby "Tiga."
    scene expression ("images/episode11/155.webp") with dissolve
    lisa "Astaga. Dia benar -benar mempercayai kita."
    scene expression ("images/episode11/156.webp") with dissolve
    toby "Kalian berdua akan membayar untuk ini."
    if lisa_path:
        scene expression ("images/episode11/157.webp") with dissolve
        lisa "Ooooh ... aku sangat takut. Itulah mengapa saya tetap menggunakan celana dalam, sehingga Anda bisa melihat mereka gemetar."
        scene expression ("images/episode11/159.webp") with dissolve
        toby "Begitu? Biarkan saya menariknya ke bawah sehingga tidak akan begitu jelas."
        scene expression ("images/episode11/160.webp") with dissolve
        lisa "Anda tidak akan berani."
        scene expression ("images/episode11/161.webp") with dissolve
        toby "Sudah kubilang kamu akan membayar untuk ini."
        scene expression ("images/episode11/162.webp") with dissolve
        lisa "Maaf ... itu ide Lauren. Saya baru saja bermain."
        $ unlockImage(persistent.lisa_10)
        scene expression ("images/episode11/163.webp") with dissolve
        toby "Lauren adalah masalah Anda. Aku hanya di sini untuk berurusan denganmu."
        scene expression ("images/episode11/164.webp") with dissolve
        lauren "Jangan berani -berani membawaku ke dalam ini."
        scene expression ("images/episode11/165.webp") with dissolve
        lisa "Terlambat untuk itu."
        scene expression ("images/episode11/166.webp") with dissolve
        lauren "Kamu jalang!"
        scene expression ("images/episode11/167.webp") with dissolve
        lisa "Bagaimanapun, itu adalah ide Anda!"
        scene expression ("images/episode11/168.webp") with dissolve
        lauren "Aku akan mendorong dildo sebesar ini di pantatmu malam ini untuk ini."
        scene expression ("images/episode11/169.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}No, no, no...{/i}"
        scene expression ("images/episode11/170.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit.{/i}"
        $ unlockImage(persistent.lisa_lauren_01)
        scene expression ("images/episode11/171_1.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        lauren "Sepertinya pacar Anda menyukai ide itu."
        scene expression ("images/episode11/172.webp") with dissolve
        toby "Saya pikir kita harus berpakaian."
        scene expression ("images/episode11/173.webp") with dissolve
        lisa "Saya pikir Anda benar."
    else:


        scene expression ("images/episode11/158.webp") with dissolve
        lauren "Saya akan membayar, tetapi Anda bahkan tidak memiliki kesulitan."
        scene expression ("images/episode11/174.webp") with dissolve
        toby "Bagaimana saya bisa mendapatkan kesulitan jika Anda masih memiliki semua pakaian Anda?"
        scene expression ("images/episode11/175.webp") with dissolve
        lauren "Anda bahkan tidak memikirkannya."
        scene expression ("images/episode11/176.webp") with dissolve
        toby "Terlambat untuk itu. Saya sudah memikirkannya dan Tuhan saya menyukai idenya."
        scene expression ("images/episode11/177.webp") with dissolve
        lauren "Jika Anda tidak berhenti, saya tidak akan mengisap ayam Anda selama sebulan."
        scene expression ("images/episode11/178.webp") with dissolve
        toby "Itu bagus. Tidak ada foreplay selama sebulan, hanya seks yang kasar dan kotor."
        scene expression ("images/episode11/179.webp") with dissolve
        lisa "Ewww ... Saya tidak ingin mendengar detail itu."
        scene expression ("images/episode11/180.webp") with dissolve
        $ unlockImage(persistent.lauren_10)
        lauren "Anda masih memakai semua pakaian Anda juga?"
        scene expression ("images/episode11/181.webp") with dissolve
        lisa "Jangan berani -berani."
        scene expression ("images/episode11/182.webp") with dissolve
        lauren "Itu lebih lucu ketika saya adalah satu -satunya topless."
        scene expression ("images/episode11/183.webp") with dissolve
        lisa "Jangan berani menyentuh atasan saya."
        scene expression ("images/episode11/184.webp") with dissolve
        lauren "Kurasa aku harus puas dengan celana dalammu."
        scene expression ("images/episode11/185.webp") with dissolve
        lisa "Lauren! Aku akan pergi membunuhmu. Aku benar -benar akan mencekikmu sampai mati."
        scene expression ("images/episode11/169_2.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}No, no, no...{/i}"
        scene expression ("images/episode11/170_2.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit.{/i}"
        $ unlockImage(persistent.lisa_lauren_01)
        scene expression ("images/episode11/171_2.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        lauren "Saya tidak tahu Anda punya sesuatu untuk tersedak. Mungkin kita harus mencobanya di tempat tidur malam ini."
        scene expression ("images/episode11/172.webp") with dissolve
        toby "Mari kita berpakaian."
        scene expression ("images/episode11/173.webp") with dissolve
        lisa "Itu ide yang bagus."

    scene expression ("images/episode11/186.webp") with dissolve
    toby "Jadi? Bagaimana kuliah? Anda menyukainya sejauh ini?"
    lauren "Bahkan jangan aku mulai."
    lisa "Jangan dengarkan dia. Dia kesal karena dia harus mengambil matematika dan bahasa Inggris."
    scene expression ("images/episode11/187_curious_2.webp") with dissolve
    toby "Apa yang kamu harapkan?"
    scene expression ("images/episode11/189_smile_1.webp") with dissolve
    lauren "Saya tidak tahu, tapi saya benci matematika, jadi mengapa saya harus mengambilnya karena saya jurusan seni?"
    scene expression ("images/episode11/188_laugh_2.webp") with dissolve
    lisa "Karena Anda harus tahu cara menghitung langkah dansa Anda."
    scene expression ("images/episode11/189_pissed_3.webp") with dissolve
    lauren "Kapan Anda menjadi pelawak seperti itu?"
    scene expression ("images/episode11/188_thinking.webp") with dissolve
    lisa "Ummm ... biarkan aku berpikir. Saya pikir tadi malam."
    scene expression ("images/episode11/187_laugh_3.webp") with dissolve
    toby "Melihat bahwa Lauren begitu menentang sistem, saya akan bertanya kepada Anda. Apakah kamu menyukainya?"
    scene expression ("images/episode11/188_smile_1.webp") with dissolve
    lisa "Ya Tuhan, aku suka kuliah. Sangat menyenangkan, saya bisa belajar banyak hal tentang bagaimana saya bisa membantu anak -anak."
    scene expression ("images/episode11/188_excited_1.webp") with dissolve
    lisa "Saat ini kita sedang mempelajari dasar -dasarnya dan begitu kita selesai dengan bahwa kita harus memutuskan untuk fokus mengajar baik taman kanak -kanak atau sekolah dasar."
    scene expression ("images/episode11/187_curious_3.webp") with dissolve
    toby "Dan menurut Anda mana yang Anda sukai?"
    scene expression ("images/episode11/188_normal_1.webp") with dissolve
    lisa "Saya belum yakin. Keduanya terdengar seperti pilihan yang bagus, tapi saya pikir itu lebih sulit di taman kanak -kanak, karena Anda harus melakukan semua jenis proyek dan membuatnya memperhatikan. Sekolah dasar tampaknya sedikit lebih mudah."
    scene expression ("images/episode11/187_curious_3.webp") with dissolve
    toby "Benar-benar? Saya pikir itu akan lebih mudah dengan anak -anak kecil. Anda memberi mereka mainan dan kemudian itu."
    scene expression ("images/episode11/188_laugh_1.webp") with dissolve
    lisa "Nah, Anda mungkin akhirnya melakukan itu, tetapi Anda sebenarnya memiliki lebih banyak rencana pelajaran untuk muncul dan butuh lebih banyak waktu untuk mempersiapkan."
    scene expression ("images/episode11/189_normal_3.webp") with dissolve
    lauren "Sekarang mari kita bicara tentang milikku.Ya, ya. Kami mengerti. Kelas Anda sangat keren."
    scene expression ("images/episode11/187_smile_2.webp") with dissolve
    toby "Saya pikir Anda tidak ingin memulai."
    scene expression ("images/episode11/189_normal_1.webp") with dissolve
    lauren "Ya, tapi saya masih berpikir saya memiliki kursus yang lebih baik."
    scene expression ("images/episode11/188_laugh_2.webp") with dissolve
    lisa "Anda memanggil kursus -kursus itu?"
    scene expression ("images/episode11/189_normal_3.webp") with dissolve
    lauren "Hanya karena Anda sangat terbiasa dengan kursus bodoh tidak berarti semuanya membosankan."
    scene expression ("images/episode11/187_smile_2.webp") with dissolve
    toby "Sekarang saya sangat penasaran. Kelas apa yang kamu ambil?"
    scene expression ("images/episode11/189_cool_1.webp") with dissolve
    lauren "Nah, sebagai permulaan semester ini saya memiliki kelas dansa dan kelas teater."
    lauren "Juga kelas psikologi sehingga kita dapat belajar menafsirkan apa pun."

    $ progress = 148
    if lisa_path:
        play sound "audio/fx/Cell Phone Ring Sound Effect - Free Sound Effects.mp3"
        if lauren_sidePath:
            $ ep11_lisaLeaves = True

            scene expression ("images/episode11/190.webp") with dissolve
            lisa "Maaf teman -teman. Saya harus mengambil ini."
            scene expression ("images/episode11/191.webp") with dissolve
            lauren "Sekarang dia tidak akan mengganggu saya lagi, izinkan saya memberi tahu Anda betapa kerennya kursus saya."
            toby "Saya mendengarkan."
            lauren "Jadi, pertama -tama ..."
            scene expression ("images/episode11/192.webp") with dissolve
            lisa "Hai teman -teman, saya harus pergi ke mobil selama beberapa menit."
            toby "Apakah Anda ingin saya ikut dengan Anda?"
            scene expression ("images/episode11/193.webp") with dissolve
            lauren "Dia seorang wanita dewasa, dia bisa menangani dirinya sendiri. Anda tetap tinggal dan mendengarkan saya."
            scene expression ("images/episode11/192.webp") with dissolve
            lisa "Beruntung Anda. Saya akan segera kembali."
            scene expression ("images/episode11/194.webp") with dissolve
            lauren "Tidak usah buru-buru."

            scene expression ("images/episode11/200.webp") with dissolve
            toby "Jadi? Pertama?"
            lauren "Pertama -tama, maaf tentang bagian telanjang, senang melihat Anda telanjang."
            scene expression ("images/episode11/201_flirty.webp") with dissolve
            toby "Kesenangan itu milikku."
            scene expression ("images/episode11/202_laugh.webp") with dissolve
            lauren "Semua milikmu? Anda menikmati telanjang di pantai umum? Apakah Anda semacam nudist?"
            scene expression ("images/episode11/201_smile.webp") with dissolve
            toby "Biarkan saya mengulanginya. Kesenangan itu semua milikku pada akhirnya."
            scene expression ("images/episode11/202_flirty.webp") with dissolve
            lauren "Pacar Anda baru saja pergi dan Anda sudah menggoda dengan saya?"
            scene expression ("images/episode11/201_laugh.webp") with dissolve
            toby "Menggoda denganmu? Apa yang membuatmu berpikir begitu?"
            scene expression ("images/episode11/202_curious.webp") with dissolve
            lauren "Kesenangan itu milikmu pada akhirnya? Saat Anda melihat saya hampir telanjang."
            scene expression ("images/episode11/201_smile.webp") with dissolve
            toby "Saya sudah berbicara tentang Lisa. Saya tidak tahu apa yang Anda bicarakan."
            scene expression ("images/episode11/202_flirty.webp") with dissolve
            lauren "Jadi, apakah saya tidak cukup menarik bagi Anda?"
            scene expression ("images/episode11/201_flirty.webp") with dissolve
            toby "I didn't say that. I just said that I've been looking at Lisa. I was a good \"boyfriend\"."
            scene expression ("images/episode11/202_smile.webp") with dissolve
            lauren "Are you always a good \"boyfriend\"?"
            scene expression ("images/episode11/201_curious.webp") with dissolve
            toby "Tergantung pada situasinya."
            scene expression ("images/episode11/202_flirty.webp") with dissolve
            lauren "Jadi jika saya mengambil top saya, Anda tidak akan terlihat?"
            scene expression ("images/episode11/201_normal.webp") with dissolve
            toby "I said I'm a good \"boyfriend\", bukan yang bodoh."
            scene expression ("images/episode11/202_laugh.webp") with dissolve
            lauren "Jadi Anda tampilan tetapi tidak menyentuh, tipe pria?"
            scene expression ("images/episode11/201_smile.webp") with dissolve
            toby "Saya kira kita tidak akan pernah tahu."
            scene expression ("images/episode11/202_flirty.webp") with dissolve
            lauren "Apakah kamu yakin tentang itu?"
            scene expression ("images/episode11/201_laugh.webp") with dissolve
            toby "Ingin membuktikan saya salah?"
            scene expression ("images/episode11/202_smile.webp") with dissolve
            lauren "Mungkin saya lakukan."
            scene expression ("images/episode11/201_curious.webp") with dissolve
            toby "Dan bagaimana Anda berencana melakukan itu?"
            scene expression ("images/episode11/203.webp") with dissolve
            lauren "Jadi jika saya melakukan ini, Anda tidak merasakan keinginan untuk menyentuh payudara saya? Untuk memerasnya?"
            toby "Mungkin saya lebih kuat dari dorongan saya."
            scene expression ("images/episode11/204.webp") with dissolve
            lauren "Sentuh payudara saya, [toby!c]. Saya perlu tahu Anda menginginkan saya sebanyak yang saya inginkan!"
            menu:
                "{i} [JGR] Peras payudaranya {/i}":
                    show ep11_205
                    $ ui.saybehavior()
                    $ ui.interact()
                    scene expression ("images/episode11/205.webp") with dissolve
                    hide ep11_205
                    lauren "Mari kita temui besok."
                    toby "Apakah Anda yakin itu ide yang bagus? Bagaimana jika Lisa mengetahuinya?"
                    scene expression ("images/episode11/206.webp") with dissolve
                    lauren "Dia menang. Kami akan pergi ke suatu tempat yang jauh."
                    scene expression ("images/episode11/207.webp") with dissolve
                    toby "Persetan. Tentu!"
                    toby "Mari kita temui besok."
                "{i}be a good \"boyfriend\"{/i} [JLASPC]"(csq="Jalur samping Lauren ditutup"):

                    $ lauren_sidePath = False
                    $ renpy.notify("Lauren's side path has been closed!")
                    stop music fadeout 5.0
                    scene expression ("images/episode11/201_normal.webp") with dissolve
                    toby "Lihat, Anda cantik, tapi saya sangat suka Lisa. Saya tidak bisa melakukan ini padanya."
                    scene expression ("images/episode11/202_smile.webp") with dissolve
                    lauren "Saya menghormatinya. Saya minta maaf jika saya melewati batas."
                    scene expression ("images/episode11/201_normal.webp") with dissolve
                    toby "Ini baik -baik saja. Ini tidak seperti kamu gila. Saya agak mendorong Anda ke arah itu"
                    scene expression ("images/episode11/202_smile.webp") with dissolve
                    lauren "Ngomong -ngomong, aku senang Lisa menemukan seseorang sepertimu."

            scene expression ("images/episode11/210.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode11/226.webp") with dissolve
            lisa "Lauren, aku harus memberitahumu sesuatu."
        else:


            $ ep11_lisaLeaves = False
            scene expression ("images/episode11/195.webp") with dissolve
            lauren "Maaf teman -teman, tapi saya harus mengambil ini."
            scene expression ("images/episode11/196.webp") with dissolve
            lisa "Sekarang kita tidak harus mendengarkan kelas menari yang membosankan, saya akan melanjutkan ke tempat yang saya tinggalkan."
            toby "Jadi. Anda mengatakan sesuatu tentang bagaimana ini lebih sulit dengan anak -anak TK."
            scene expression ("images/episode11/197.webp") with dissolve
            lauren "Hai teman -teman, saya akan segera kembali, perlu bertemu dengan seorang teman."
            scene expression ("images/episode11/198.webp") with dissolve
            lisa "Akhirnya beberapa waktu sendirian."
            scene expression ("images/episode11/197.webp") with dissolve
            lauren "Saya mendengar itu, jalang!"
            scene expression ("images/episode11/199.webp") with dissolve
            lisa "Mencintaimu juga!"


            scene expression ("images/episode11/214.webp") with dissolve
            lisa "Jadi seperti yang saya katakan, menurut saya Anda memiliki lebih banyak pekerjaan yang harus dilakukan dengan taman kanak -kanak, karena Anda perlu menjelaskan banyak hal kepada mereka dengan cara yang dapat mereka pahami."
            lisa "Dan selain itu, saya terlalu menyukai anak -anak dan saya tidak akan bisa suka memerintah di sekitar labu kecil itu."
            toby "Anda lucu."
            scene expression ("images/episode11/215_shy.webp") with dissolve
            lisa "Diam. Anda membuat saya memerah."
            scene expression ("images/episode11/216_smile.webp") with dissolve
            toby "Setelah sekian lama Anda masih malu dengan saya ketika saya memberi Anda pujian?"
            scene expression ("images/episode11/215_laugh.webp") with dissolve
            lisa "Ini bukan salahku, aku tidak terbiasa menerima pujian."
            scene expression ("images/episode11/215_smile.webp") with dissolve
            lisa "You forget I have a brother and all the compliments he ever gave me were \"idiot\", \"stupid\", \"chubby\"."
            scene expression ("images/episode11/216_laugh.webp") with dissolve
            toby "Tembam? Apa yang gemuk tentang Anda."
            scene expression ("images/episode11/215_laugh.webp") with dissolve
            lisa "Saya sering makan banyak."
            scene expression ("images/episode11/216_normal.webp") with dissolve
            toby "Saya tidak bisa membayangkan Anda gemuk."
            scene expression ("images/episode11/215_smile.webp") with dissolve
            lisa "Oh, saya tidak pernah gemuk. Saya sudah kurus sejak saya ingat."
            scene expression ("images/episode11/216_curious.webp") with dissolve
            toby "Lalu mengapa dia memanggilmu gemuk?"
            scene expression ("images/episode11/215_laugh.webp") with dissolve
            lisa "Biasanya karena saya mencuri permennya."
            scene expression ("images/episode11/216_laugh.webp") with dissolve
            toby "Kamu sangat jahat!"
            scene expression ("images/episode11/215_shy.webp") with dissolve
            lisa "Mengapa? Saya adalah seorang gadis kecil yang menyukai permen."
            scene expression ("images/episode11/215_curious.webp") with dissolve
            lisa "Ingin mengatakan saya tidak pantas mendapatkannya?"
            scene expression ("images/episode11/216_laugh.webp") with dissolve
            toby "Bagaimana saya bisa mengatakan sesuatu seperti itu."
            scene expression ("images/episode11/215_smile.webp") with dissolve
            lisa "Melihat? Persis seperti apa yang telah saya bicarakan."
            scene expression ("images/episode11/216_smile.webp") with dissolve
            toby "Anda sangat cantik."
            scene expression ("images/episode11/215_shy.webp") with dissolve
            lisa "Hentikan!"
            scene expression ("images/episode11/216_laugh.webp") with dissolve
            toby "Atau?"
            scene expression ("images/episode11/215_smile.webp") with dissolve
            lisa "Atau aku tidak akan mencium bibirmu yang enak."
            scene expression ("images/episode11/216_normal.webp") with dissolve
            toby "Dalam hal ini Anda jelek, bodoh dan gemuk."
            scene expression ("images/episode11/217.webp") with dissolve
            lisa "Kemarilah kamu!"
            show ep11_218
            $ ui.pausebehavior(6.7)
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode11/219.webp") with dissolve
            hide ep11_218
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode11/220.webp") with dissolve
            toby "Apa yang harus saya hubungi untuk membuat Anda menjatuhkan celana dalam itu?"
            lisa "Hubungi saya besok dan mengajak saya keluar dan mungkin saya akan meninggalkan mereka di rumah."
            toby "Apa yang telah saya lakukan untuk Anda? Saya dulu menjadi cabul dalam hubungan kami."
            scene expression ("images/episode11/221.webp") with dissolve
            lauren "Anda berdua mesum."
            scene expression ("images/episode11/222.webp") with dissolve
            lisa "Umm ... kapan kamu kembali?"
            scene expression ("images/episode11/221.webp") with dissolve
            lauren "Tepat di sekitar waktu ketika [toby!c] meletakkan tangannya di celana dalam Anda."
            scene expression ("images/episode11/223.webp") with dissolve
            lisa "Ha! Gotcha! Dia tidak melakukan itu, jadi itu berarti Anda baru saja sampai di sini."
            scene expression ("images/episode11/221.webp") with dissolve
            lauren "Anda sangat membosankan!"
            scene expression ("images/episode11/224.webp") with dissolve
            lisa "Mhmm."
            scene expression ("images/episode11/225_1.webp") with dissolve
            toby "Kapan terakhir kali Anda mencium siapa pun?"
            scene expression ("images/episode11/229.webp") with dissolve
            lisa "Itu rendah!"
            scene expression ("images/episode11/230.webp") with dissolve
            lauren "Ya, ya. Saya sudah datang."
    else:


        play sound "audio/fx/Cell Phone Ring Sound Effect - Free Sound Effects.mp3"
        if lisa_sidePath:
            $ ep11_lisaLeaves = False

            scene expression ("images/episode11/195.webp") with dissolve
            lauren "Maaf teman -teman, tapi saya harus mengambil ini."
            scene expression ("images/episode11/196.webp") with dissolve
            lisa "Sekarang kita tidak harus mendengarkan kelas menari yang membosankan, saya akan melanjutkan ke tempat yang saya tinggalkan."
            toby "Jadi. Anda mengatakan sesuatu tentang bagaimana ini lebih sulit dengan anak -anak TK."
            scene expression ("images/episode11/197.webp") with dissolve
            lauren "Hai teman -teman, saya akan segera kembali, saya perlu bertemu dengan seorang teman."
            scene expression ("images/episode11/198.webp") with dissolve
            lisa "Akhirnya! Kita bisa berbicara tanpa terputus."
            scene expression ("images/episode11/197.webp") with dissolve
            lauren "Saya mendengar itu, jalang!"
            scene expression ("images/episode11/199.webp") with dissolve
            lisa "Mencintaimu juga!"


            scene expression ("images/episode11/214.webp") with dissolve
            lisa "Jadi seperti yang saya katakan, menurut saya Anda memiliki lebih banyak pekerjaan yang harus dilakukan dengan taman kanak -kanak, karena Anda perlu menjelaskan banyak hal kepada mereka dengan cara yang dapat mereka pahami."
            lisa "Dan selain itu, saya terlalu menyukai anak -anak sehingga saya tidak akan bisa suka memerintah di sekitar labu kecil itu."
            toby "Saya pikir Anda akan menjadi guru yang hebat."
            scene expression ("images/episode11/215_shy.webp") with dissolve
            lisa "Diam. Anda membuat saya memerah."
            scene expression ("images/episode11/216_smile.webp") with dissolve
            toby "Anda benar -benar tidak tahu cara menerima pujian."
            scene expression ("images/episode11/215_laugh.webp") with dissolve
            lisa "Ini bukan salahku, aku tidak terbiasa menerima pujian."
            scene expression ("images/episode11/215_smile.webp") with dissolve
            lisa "I have a brother and all the compliments he ever gave me were \"idiot\", \"stupid\", \"chubby\"."
            scene expression ("images/episode11/216_laugh.webp") with dissolve
            toby "Tembam? Apa yang gemuk tentang Anda."
            scene expression ("images/episode11/215_laugh.webp") with dissolve
            lisa "Saya sering makan banyak."
            scene expression ("images/episode11/216_normal.webp") with dissolve
            toby "Saya tidak bisa membayangkan Anda gemuk."
            scene expression ("images/episode11/215_smile.webp") with dissolve
            lisa "Oh, saya tidak pernah gemuk. Saya selalu kurus."
            scene expression ("images/episode11/216_curious.webp") with dissolve
            toby "Lalu mengapa dia memanggilmu gemuk?"
            scene expression ("images/episode11/215_laugh.webp") with dissolve
            lisa "Biasanya karena saya mencuri permennya."
            scene expression ("images/episode11/216_laugh.webp") with dissolve
            toby "Kamu sangat jahat!"
            scene expression ("images/episode11/215_shy.webp") with dissolve
            lisa "Mengapa? Saya adalah seorang gadis kecil yang menyukai permen."
            scene expression ("images/episode11/215_curious.webp") with dissolve
            lisa "Ingin mengatakan saya tidak pantas mendapatkannya?"
            scene expression ("images/episode11/216_laugh.webp") with dissolve
            toby "Bagaimana saya bisa mengatakan sesuatu seperti itu."
            scene expression ("images/episode11/215_smile.webp") with dissolve
            lisa "Melihat? Persis seperti apa yang telah saya bicarakan."
            scene expression ("images/episode11/216_smile.webp") with dissolve
            toby "Anda sangat senang bergaul."
            scene expression ("images/episode11/215_cute.webp") with dissolve
            lisa "Anda juga tidak terlalu buruk."
            scene expression ("images/episode11/216_arogant.webp") with dissolve
            toby "Saya tidak buruk? Sayang, saya menyenangkan untuk bergaul."
            scene expression ("images/episode11/215_laugh.webp") with dissolve
            lisa "Bayi?"
            scene expression ("images/episode11/216_laugh.webp") with dissolve
            toby "You like \"honey\"lebih baik?"
            scene expression ("images/episode11/215_laugh.webp") with dissolve
            lisa "Saya suka sayang."
            scene expression ("images/episode11/216_smile.webp") with dissolve
            toby "Sayang, aku menyenangkan untuk bergaul."
            scene expression ("images/episode11/215_smile.webp") with dissolve
            lisa "Setiap kali dia pulang dari kencan denganmu, dia tidak bisa berhenti berbicara tentang betapa menyenangkannya itu.Baik, Anda benar. Saya menikmati perusahaan Anda. Saya mengerti mengapa Lauren sangat berbicara tentang Anda."
            scene expression ("images/episode11/216_laugh.webp") with dissolve
            toby "Sekarang Anda membuat saya memerah."
            scene expression ("images/episode11/215_laugh.webp") with dissolve
            lisa "Anda tidak punya alasan untuk memerah. Ini tidak seperti saya percaya apapun yang dia ceritakan tentang Anda."
            scene expression ("images/episode11/216_normal.webp") with dissolve
            toby "Anda baru saja mengatakan bahwa Anda akhirnya mengerti mengapa Lauren menikmati kencannya dengan saya dan sekarang Anda mengatakan bahwa Anda tidak percaya apa yang dia katakan?"
            scene expression ("images/episode11/215_shy.webp") with dissolve
            lisa "Diam!"
            menu:
                "[JGR] mengajaknya kencan":
                    scene expression ("images/episode11/216_smile.webp") with dissolve
                    toby "Bagus. Lalu mari kita keluar besok dan Anda akan melihat sendiri jika apa yang dia katakan kepada Anda itu benar."
                    scene expression ("images/episode11/215_surprised.webp") with dissolve
                    lisa "Pertama -tama, saya tidak akan berkencan dengan pacar teman saya."
                    scene expression ("images/episode11/215_laugh.webp") with dissolve
                    lisa "Kedua, bahkan jika kita keluar, aku tidak akan menguji semua yang dia katakan untuk melihat apakah itu benar."
                    scene expression ("images/episode11/216_curious.webp") with dissolve
                    toby "Mengapa? Apa lagi yang dia katakan?"
                    scene expression ("images/episode11/215_shy.webp") with dissolve
                    lisa "Mari kita katakan dia memberi saya terlalu banyak informasi tentang apa yang kalian berdua lakukan. Dia bahkan memberi tahu saya bagaimana dia tahu tentang tempat ini."
                    scene expression ("images/episode11/216_awkward.webp") with dissolve
                    toby "Um ... ya ..."
                    scene expression ("images/episode11/215_smile.webp") with dissolve
                    lisa "Ya, jadi tidak, terima kasih! Aku bukan gadis seperti itu."
                    scene expression ("images/episode11/216_smile.webp") with dissolve
                    toby "Tidak ada yang mengatakan Anda. Kami berdua menikmati menghabiskan waktu bersama. Mari kita keluar, seperti teman. Bicara tentang sepak bola, mobil, perempuan."
                    scene expression ("images/episode11/215_laugh.webp") with dissolve
                    lisa "Oleh gadis -gadis yang Anda maksud, Lauren dan kepribadiannya yang lain?"
                    scene expression ("images/episode11/216_smile.webp") with dissolve
                    toby "Berapa banyak yang dia miliki?"
                    scene expression ("images/episode11/215_laugh.webp") with dissolve
                    lisa "Terlalu banyak."
                    scene expression ("images/episode11/221.webp") with dissolve
                    lauren "Anda yang akan berbicara?"
                    scene expression ("images/episode11/222.webp") with dissolve
                    lisa "Anda mendengarnya?"
                    scene expression ("images/episode11/221.webp") with dissolve
                    lauren "Tentu saja saya lakukan, Bitch!"
                    scene expression ("images/episode11/224.webp") with dissolve
                    lisa "Untuk menjawab pertanyaan Anda. Dia hanya memiliki dua."
                    lisa "Teman baik Lauren dengan dengan siapa Anda dapat berbicara dengan dan pelacur gila Lauren, yang hanya berpikir tentang mengisap sesuatu."
                    scene expression ("images/episode11/225_2.webp") with dissolve
                    lauren "Kedengarannya benar."
                "{i} Ubah subjek {/i} [JLISPC]"(csq="Sidepath Lisa ditutup"):

                    $ lisa_sidePath = False
                    $ renpy.notify("Lisa's sidepath has been closed!")
                    stop music fadeout 5.0
                    scene expression ("images/episode11/216_curious.webp") with dissolve
                    toby "Ngomong -ngomong, apakah Anda harus mengajar siswa di suatu tempat semester ini?"
                    scene expression ("images/episode11/215_smile.webp") with dissolve
                    lisa "Ya, sebenarnya saya lakukan. Saya tidak bisa menunggu."
                    scene expression ("images/episode11/221.webp") with dissolve
                    lauren "Tuhan kamu membosankan. Anda sudah berbicara tentang sekolah sejak saya pergi?"
                    scene expression ("images/episode11/222.webp") with dissolve
                    lisa "Apa yang kamu harapkan?"
                    scene expression ("images/episode11/221.webp") with dissolve
                    lauren "Aku tidak tahu. Saya berharap melihat Anda di atas [toby!c], mencoba mencuri pacar saya."
                    scene expression ("images/episode11/223.webp") with dissolve
                    lisa "Tidak akan terjadi."
        else:


            $ ep11_lisaLeaves = True
            scene expression ("images/episode11/190.webp") with dissolve
            lisa "Maaf teman -teman. Saya harus mengambil ini."
            scene expression ("images/episode11/191.webp") with dissolve
            lauren "Sekarang setelah dia tidak akan mengganggu saya lagi, izinkan saya memberi tahu Anda betapa kerennya kelas saya."
            toby "Saya mendengarkan."
            lauren "Jadi, pertama -tama ..."
            scene expression ("images/episode11/192.webp") with dissolve
            lisa "Hai teman -teman, saya harus pergi ke mobil selama beberapa menit."
            scene expression ("images/episode11/194.webp") with dissolve
            lauren "Tidak usah buru-buru."
            scene expression ("images/episode11/193.webp") with dissolve
            lauren "Segera setelah dia pergi, aku sampai di atasmu dan kami bercinta seperti orang gila. Oke?"
            scene expression ("images/episode11/192.webp") with dissolve
            lisa "Cobalah untuk tidak berteriak terlalu banyak."


            scene expression ("images/episode11/200.webp") with dissolve
            lauren "Saya suka menggodanya. Dia benar -benar pemalu."
            toby "Saya tidak yakin apakah dia benar -benar tidak bersalah."
            scene expression ("images/episode11/202_laugh.webp") with dissolve
            lauren "Nah, dia tidak bersalah, dia tahu banyak hal, tapi dia terlalu malu untuk mengakuinya."
            scene expression ("images/episode11/201_laugh.webp") with dissolve
            toby "Tidak semua orang adalah orang yang seperti Anda dan saya."
            scene expression ("images/episode11/202_flirty.webp") with dissolve
            lauren "Kita agak mesum kan?"
            scene expression ("images/episode11/201_smile.webp") with dissolve
            toby "Maksud saya, dibutuhkan seseorang untuk mengetahuinya, kan?"
            scene expression ("images/episode11/202_smile.webp") with dissolve
            lauren "Anda tidak tahu seberapa besar saya menginginkan Anda sekarang."
            scene expression ("images/episode11/201_smile.webp") with dissolve
            toby "Jadi bagaimana dengan begitu Lisa membuat Anda berada di atas saya dan kami bercinta seperti kelinci."
            scene expression ("images/episode11/202_flirty.webp") with dissolve
            lauren "Anda menginginkan itu, kan?"
            scene expression ("images/episode11/201_laugh.webp") with dissolve
            toby "Mungkin saya lakukan."
            scene expression ("images/episode11/202_sexy.webp") with dissolve
            lauren "Ya, saya juga, tapi saya tidak ingin Lisa menangkap kami. Selain itu, saya berjanji padanya hari ini saya akan berperilaku dan tinggal bersamanya."
            scene expression ("images/episode11/201_curious.webp") with dissolve
            toby "Dan aku menghancurkan hari gadismu?"
            scene expression ("images/episode11/202_smile.webp") with dissolve
            lauren "Lebih menyenangkan dengan Anda di sekitar dan selain itu dia menyukai Anda. Dia mengatakan kepada saya bahwa Anda baik untuk saya."
            scene expression ("images/episode11/201_smile.webp") with dissolve
            toby "Dan apakah Anda setuju?"
            scene expression ("images/episode11/208.webp") with dissolve
            lauren "Ummm ... mungkin?"
            toby "Mungkin?"
            lauren "Tentu saja saya lakukan. Anda sangat baik untuk saya dan Anda sangat keren dan ..."
            toby "Berhenti bicara!"
            show ep11_209
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode11/209.webp") with dissolve
            hide ep11_209
            scene expression ("images/episode11/210.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode11/211.webp") with dissolve
            lisa "Dapatkan kamar, kalian berdua."
            scene expression ("images/episode11/212.webp") with dissolve
            toby "Kami akan. Besok!"
            scene expression ("images/episode11/213.webp") with dissolve
            lauren "Kami akan?"
            toby "Yup."
            lauren "Tak sabar menunggu."



    if ep11_lisaLeaves:
        scene expression ("images/episode11/227.webp") with dissolve
        lisa "Tebak siapa yang baru saja saya lihat."
        scene expression ("images/episode11/230.webp") with dissolve
        lauren "Aku tidak tahu. Siapa?"
        scene expression ("images/episode11/231.webp") with dissolve
        lisa "Joe dan gadis es krim. Mereka berpegangan tangan."
        scene expression ("images/episode11/232.webp") with dissolve
        toby "Siapa Joe?"
    else:
        scene expression ("images/episode11/230.webp") with dissolve
        lauren "Tebak siapa yang saya lihat di pantai?"
        scene expression ("images/episode11/231.webp") with dissolve
        lisa "Mengalahkan saya."
        scene expression ("images/episode11/230.webp") with dissolve
        lauren "Joe dan gadis es krim. Mereka berpegangan tangan."
        scene expression ("images/episode11/233.webp") with dissolve
        toby "Siapa Joe?"

    scene expression ("images/episode11/234.webp") with dissolve
    lisa "Seorang pria Lauren bertemu di kelas menari. Dia ingin mengajak beberapa gadis keluar selama dua bulan dan tidak pernah memiliki nyali sampai Lauren di sini mengatakan kepadanya apa yang harus dilakukan. Dia semacam Dr. Love."
    scene expression ("images/episode11/235.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why does this sound so familiar.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Bea's wanna be boyfriend was called Joe.{/i}"
    if ep11_lisaLeaves:
        scene expression ("images/episode11/232.webp") with dissolve
    else:
        scene expression ("images/episode11/233.webp") with dissolve
    toby "Oleh gadis es krim yang Anda maksud, bea?"
    scene expression ("images/episode11/236.webp") with dissolve
    lauren "Anda tahu Bea?"
    scene expression ("images/episode11/237.webp") with dissolve
    toby "Ya ... dia berteman dengan sangat baik dengan [sister] saya."
    scene expression ("images/episode11/238.webp") with dissolve
    lisa "Tris?"
    scene expression ("images/episode11/239.webp") with dissolve
    toby "Ya. Kamu kenal dia?"
    scene expression ("images/episode11/234.webp") with dissolve
    lisa "Ya. Kami memiliki dua kursus bersama. Dia sangat manis dan cantik."
    if ep11_lisaLeaves:
        scene expression ("images/episode11/239.webp") with dissolve
        toby "Apakah dia di sini bersama mereka?"
        scene expression ("images/episode11/234.webp") with dissolve
        lisa "Ya ... dia ada di bar."
    else:
        scene expression ("images/episode11/237.webp") with dissolve
        toby "Apakah dia di sini bersama mereka?"
        scene expression ("images/episode11/240.webp") with dissolve
        lauren "Ya ... dia ada di bar."
    scene expression ("images/episode11/241.webp") with dissolve
    if patricia_path:
        toby "Maaf gadis, tapi saya harus pergi. Kami bertengkar tadi malam dan saya benar -benar perlu berbicara dengannya."
    else:
        toby "Maaf gadis, tapi aku benar -benar harus berbicara dengannya."
    scene expression ("images/episode11/242.webp") with dissolve
    lisa "Apakah semuanya baik -baik saja?"
    scene expression ("images/episode11/241.webp") with dissolve
    toby "Ya ... jangan khawatir. Semuanya akan baik -baik saja, tetapi saya benar -benar harus pergi."
    toby "Terima kasih untuk hari ini. Itu bagus."
    scene expression ("images/episode11/241.webp") with dissolve
    toby "Kita harus melakukan ini lebih sering."
    scene expression ("images/episode11/242.webp") with dissolve
    if lisa_path:
        lisa "Tentu..."
    else:
        lauren "Tentu."
    scene expression ("images/episode11/243.webp") with dissolve
    toby "Sampai jumpa."

    return

label episode11_beaMessage:
    play sound "audio/fx/notification_5.mp3"
    $ progress = 147
    scene expression ("images/episode11/244.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Looks like I got a message from Bea.{/i}"
    scene expression ("images/episode11/245_texting.webp") with dissolve
    call sms_incoming ("bea", "Hi [toby!c]. We're going to the beach. If you wanna talk to Tris head there, but don't let her know I told you.") from _call_sms_incoming_212
    if beatrice_path:
        call sms_sent ("bea", "Hi Bea. Thanks! You're the best") from _call_sms_sent_163
        call sms_incoming ("bea", "Yeah, I know!") from _call_sms_incoming_213
        call sms_sent ("bea", "See you there!") from _call_sms_sent_164
        call sms_incoming ("bea", "Sure thing") from _call_sms_incoming_214
    else:
        call sms_sent ("bea", "Hi Bea. Thank you very much!") from _call_sms_sent_165
        call sms_incoming ("bea", "No worries.") from _call_sms_incoming_215
    hide screen message
    scene expression ("images/episode11/246.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What should I do? How can I go there without her thinking Bea told me.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'll just pretend I was jogging on the beach.{/i}"
    scene expression ("images/episode11/247.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yeah. That could definitely work and this way, I don't have go inside and tell [mom] what's going on.{/i}"
    return


label episode11_beachTris:
    $ progress = 149
    if lisa_path or lauren_path:
        scene expression ("images/episode11/250.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She said Tris was at the bar. Let's see if she's still there.{/i}"


        scene expression ("images/episode11/251.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is that Tris? Is she smoking?{/i}"
    else:
        scene expression ("images/episode11/248.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wonder where Tris is.{/i}"


        scene expression ("images/episode11/249.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think I see her. What is she doing? Is she smoking?{/i}"


    scene expression ("images/episode11/252.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/253.webp") with dissolve
    toby "Apa yang kamu lakukan di sini, [sis]?"
    scene expression ("images/episode11/254.webp") with dissolve
    patricia "Hai! Kembalikan rokok saya."
    scene expression ("images/episode11/255.webp") with dissolve
    toby "Anda tidak akan merokok saat saya berkeliling."
    scene expression ("images/episode11/256_1.webp") with dissolve
    patricia "Lalu cuti."
    scene expression ("images/episode11/256_2.webp") with dissolve
    patricia "Bolehkah saya meminta rokok lagi?"
    scene expression ("images/episode11/256_3.webp") with dissolve
    toby "Tidak, dia tidak bisa memiliki yang lain."
    if toby_job == 0:
        scene expression ("images/episode11/257.webp") with dissolve
        if patricia_path:
            toby "Aku tidak akan meninggalkanmu seperti ini. Kita perlu bicara."
        else:
            toby "Saya tidak akan pergi. Anda akan memberi tahu saya apa yang terjadi dengan Anda."
    else:
        scene expression ("images/episode11/258.webp") with dissolve
        if patricia_path:
            toby "Aku tidak akan meninggalkanmu seperti ini. Kita perlu bicara."
        else:
            toby "Aku tidak akan pergi. Anda akan memberi tahu saya apa yang terjadi dengan Anda."

    scene expression ("images/episode11/372.webp") with dissolve
    barman "Ada masalah?"
    if toby_job == 0:
        scene expression ("images/episode11/373.webp") with dissolve
        toby "Tidak ada masalah di sini. Saya berbicara dengan [sister] saya, jadi mengapa Anda tidak membuat diri Anda berguna di tempat lain."
        scene expression ("images/episode11/372.webp") with dissolve
        barman "Saya tidak menyukai nada Anda, saya pikir sudah waktunya Anda pergi."
        scene expression ("images/episode11/373.webp") with dissolve
        toby "Lihatlah, dia tidak tertarik. Anda terlalu tua, jelek dan bodoh untuk [sister] saya, jadi kalahkan."
    else:
        scene expression ("images/episode11/373.webp") with dissolve
        toby "Tidak ada masalah di sini. Saya berbicara dengan [sister] saya, jadi mengapa Anda tidak membuat diri Anda berguna di tempat lain."
        scene expression ("images/episode11/372.webp") with dissolve
        barman "Saya tidak menyukai nada Anda. Saya pikir sudah waktunya Anda pergi."
        scene expression ("images/episode11/374.webp") with dissolve
        toby "Dan aku berkata, persetan."
        barman "Lepaskan tanganmu, atau yang lain."
        toby "Atau apa lagi?"
        scene expression ("images/episode11/375_1.webp") with dissolve
        toby "Tunggu, aku mengenalmu."
        scene expression ("images/episode11/375_2.webp") with dissolve
        barman "Bagaimana Anda mengenal saya?"
        scene expression ("images/episode11/375_1.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}If I ever see you anywhere near Climax, you'll be in big trouble, understood? {/i}"
        scene expression ("images/episode11/376.webp") with dissolve
        barman "Kotoran! Anda [toby!c]. Katrina ..."
        toby "Keluar dari sini."

    scene expression ("images/episode11/377.webp") with dissolve
    patricia "Hai! Saya sedang berbicara dengannya."
    scene expression ("images/episode11/378.webp") with dissolve
    if toby_job == 0:
        toby "Lihat dia, lalu lihatmu. Anda bisa melakukan yang lebih baik. Sekarang, mari kita bicara tentang sesuatu yang lebih penting."
    else:
        toby "Dan sekarang Anda berbicara dengan saya!"

    toby "Jadi apa yang terjadi?"

    $ progress = 150
    if patricia_path:
        scene expression ("images/episode11/259.webp") with dissolve
        patricia "Kami tidak punya apa -apa untuk dibicarakan. Sekarang maukah Anda meninggalkan saya sendiri. Saya tidak ingin berbicara dengan Anda."
        scene expression ("images/episode11/260.webp") with dissolve
        toby "Kita perlu berbicara tentang apa yang terjadi tadi malam."
        scene expression ("images/episode11/259.webp") with dissolve
        patricia "Saya mabuk. Itulah yang terjadi. Itu tidak akan terjadi lagi."
        scene expression ("images/episode11/260.webp") with dissolve
        toby "Aku mengkhawatirkanmu. Anda mengambil sepeda saya. Sesuatu bisa terjadi padamu."
        scene expression ("images/episode11/261.webp") with dissolve
        patricia "..."
        scene expression ("images/episode11/262.webp") with dissolve
        patricia "Tidak ada yang terjadi pada saya."
        patricia "Ada lagi yang ingin Anda bicarakan atau saya bisa menyalakan rokok lain?"
        scene expression ("images/episode11/263.webp") with dissolve
        toby "Kapan Anda mulai merokok?"
        scene expression ("images/episode11/264.webp") with dissolve
        patricia "Ummm ... biarkan aku berpikir! Itu yang sulit."
        patricia "Pagi ini."
        scene expression ("images/episode11/263.webp") with dissolve
        if toby_job == 0:
            toby "Saya tidak menginginkan apa pun selain yang terbaik untuk Anda. Biarkan saya membantu Anda."
            scene expression ("images/episode11/265.webp") with dissolve
            patricia "Selamat tinggal!"
            scene expression ("images/episode11/266.webp") with dissolve
            toby "Jangan seperti itu, [sis]. Ayo pergi ke suatu tempat untuk berbicara."
            scene expression ("images/episode11/266.webp") with dissolve
            patricia "Saya tidak punya apa -apa untuk Anda bicarakan."
            toby "Bagus. Kemudian Anda mendengarkan."
            scene expression ("images/episode11/267.webp") with dissolve
        else:
            toby "Anda mulai membuat saya kesal dengan nada Anda."
            scene expression ("images/episode11/265.webp") with dissolve
            patricia "Selamat tinggal!"
            scene expression ("images/episode11/266.webp") with dissolve
            toby "Persetan dengan omong kosong ini. Anda datang dengan saya. Kita perlu bicara."
            scene expression ("images/episode11/266.webp") with dissolve
            patricia "Saya tidak punya apa -apa untuk Anda bicarakan."
            toby "Kemudian Anda hanya duduk di sana dan mendengarkan."
            scene expression ("images/episode11/267.webp") with dissolve

        patricia "Baik ... bicara."
        scene expression ("images/episode11/268.webp") with dissolve
        toby "Mari kita pergi ke dermaga. Itu lebih tenang."
        patricia "Oke."
        scene expression ("images/episode11/269.webp") with dissolve
        patricia "Bagaimana Anda tahu saya ada di sini? Apakah Bea merata saya seperti yang dia lakukan dengan sepeda Anda?"
        if lisa_path or lauren_path:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I hate to lie to her, but if she finds out I'm here with two girls, she might not react well.{/i}"
        else:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I hate to lie her, but I really need Bea on my side if something happens again.{/i}"
        toby "Tidak. Aku jogging di pantai dan melihatmu."
        patricia "Anda pergi untuk jogging? Saya selalu harus menyeret pantat Anda dan tiba -tiba Anda ingin berlari?"
        scene expression ("images/episode11/270.webp") with dissolve
        toby "Tidak seperti Anda untuk melakukan sesuatu seperti itu. Biasanya semua orang tahu kapan Anda pergi ke suatu tempat dan Anda hanya bangun dan pergi di tengah malam.Saya memiliki banyak hal di pikiran saya. Saya perlu menjernihkan kepala saya. Pertama -tama, saya khawatir tentang Anda."
        patricia "Yah tidak seperti saya juga merokok, namun di sinilah saya."
        toby "Kemudian itu [mom]. Dia benar -benar takut ketika Anda tidak pulang ke rumah pagi ini dan Anda tidak menjawab telepon Anda."
        patricia "Baterai saya mati."
        scene expression ("images/episode11/271.webp") with dissolve
        toby "Itulah yang saya katakan kepadanya dan bahwa Anda berada di Bea, jadi dia tidak terlalu banyak. Dia sudah memiliki banyak hal di piringnya."
        if charlotte_path:
            patricia "Ya, saya ingat Anda menceritakan sesuatu tentang perkelahian."
        else:
            patricia "Apa yang telah terjadi?"
            toby "Dia dan [dad] bertengkar besar. Aku membiarkannya tidur di kamarku."
            patricia "Itulah mengapa Anda berada di sofa?"
            toby "Ya."


        scene expression ("images/episode11/272.webp") with dissolve
        toby "Bagaimanapun, bukan itu yang ingin saya bicarakan."
        patricia "Lihat. Aku pulang malam ini. Seperti yang saya katakan, saya hanya mabuk. Saya tidak tahu apa yang terjadi pada saya."
        toby "Saya senang mendengarnya, tetapi sebenarnya tepat setelah Anda naik ke atas, saya banyak memikirkan apa yang terjadi."
        scene expression ("images/episode11/273_ashamed.webp") with dissolve
        patricia "Bisakah kita tidak membicarakannya? Aku sudah malu. Itulah alasan utama saya pergi tadi malam."
        scene expression ("images/episode11/274_normal.webp") with dissolve
        toby "Saya tidak percaya itu. Saya tidak percaya bahwa Anda pergi karena Anda malu."
        scene expression ("images/episode11/273_normal.webp") with dissolve
        patricia "Saya tidak peduli dengan apa yang Anda yakini."
        scene expression ("images/episode11/274_smile.webp") with dissolve
        toby "Saya pikir Anda pergi karena Anda merasa ditolak."
        scene expression ("images/episode11/273_arogant.webp") with dissolve
        patricia "Anda adalah [brother] saya.Apakah kamu bodoh atau apa? Ditolak oleh siapa? Anda?"
        scene expression ("images/episode11/274_normal.webp") with dissolve
        toby "Jadi Anda ingin memberi tahu saya bahwa Anda tidak punya perasaan untuk saya?"
        scene expression ("images/episode11/273_normal.webp") with dissolve
        patricia "Aku memang punya perasaan untukmu. Saya peduli untuk Anda sebagai [brother]. Seperti yang saya katakan, apa yang terjadi kemarin, adalah karena alkohol."
        scene expression ("images/episode11/274_smile.webp") with dissolve
        toby "Jadi Anda tidak menemukan saya menarik sama sekali?"
        scene expression ("images/episode11/273_grosed.webp") with dissolve
        patricia "Ewww ... itu kotor."
        scene expression ("images/episode11/274_normal.webp") with dissolve
        toby "Saya tidak bisa mengendalikannya.Saya tidak berpikir itu kotor. Sebenarnya saya pikir itu bagus, karena saya merasakan hal yang sama. Saya tidak bisa mengatakan saya mengerti apa yang sedang terjadi, atau bagaimana saya bisa merasa tertarik pada [sister] saya, tetapi memang demikian."
        scene expression ("images/episode11/274_smile.webp") with dissolve
        toby "Saya pikir Anda adalah gadis tercantik yang pernah saya lihat. Mungkin aneh untuk tertarik pada [sister] saya sendiri, tetapi saya tidak bisa membantunya. Ini tidak seperti saya ingin ini terjadi, tetapi itu terjadi dan saya tidak dapat melakukan apa saja untuk mengubahnya."
        scene expression ("images/episode11/273_surprised.webp") with dissolve
        patricia "..."
        scene expression ("images/episode11/274_smile.webp") with dissolve
        toby "Alasan mengapa saya menghentikan Anda tadi malam, bukan karena saya tidak ingin Anda melanjutkan, tetapi karena saya tidak tahu bagaimana menangani situasi tersebut. Sepanjang hidup saya, saya tahu bahwa ini salah dan sulit bagi saya untuk mengubahnya."
        scene expression ("images/episode11/274_normal.webp") with dissolve
        toby "Selain itu, Anda mabuk."
        scene expression ("images/episode11/273_grosed.webp") with dissolve
        patricia "Berhenti bicara. Anda menjijikkan. Saya tidak percaya Anda memikirkan saya seperti itu. Anda butuh bantuan."
        scene expression ("images/episode11/274_normal.webp") with dissolve
        toby "Setidaknya aku jujur tentang perasaanku padamu."
        scene expression ("images/episode11/273_normal.webp") with dissolve
        patricia "Tidak ada yang ada di antara kita."
        scene expression ("images/episode11/274_normal.webp") with dissolve
        toby "Saya tidak meminta Anda menjadi pacar saya, tetapi saya memberi tahu Anda bagaimana perasaan saya. Saya ingin Anda tahu bahwa Anda tidak sendirian di kereta ini. Saya juga tidak tahu cara menangani situasi ini."
        scene expression ("images/episode11/274_smile.webp") with dissolve
        toby "Saya tidak mengatakan bahwa kita harus mengejar jalan ini, tetapi kita bisa mencari tahu bersama apa pun yang sedang terjadi.Anda adalah [sister] saya dan aku mencintaimu. Anda tahu bahwa saya akan melakukan apa saja untuk Anda. Aku tidak ingin kehilanganmu."
        scene expression ("images/episode11/273_curious.webp") with dissolve
        patricia "Atau apa yang salah dengan kita?"
        scene expression ("images/episode11/274_smile.webp") with dissolve
        toby "Jika itu yang ingin Anda sebut, tentu saja, tapi apa pun yang terjadi, jangan pernah tinggalkan seperti itu. Itu adalah malam terburuk yang pernah ada."
        scene expression ("images/episode11/274_sad.webp") with dissolve
        toby "Saya hampir tidak tidur."
        scene expression ("images/episode11/273_ashamed.webp") with dissolve
        patricia "Jadi Anda tidak marah padaku?"
        scene expression ("images/episode11/274_angry.webp") with dissolve
        toby "Oh, saya marah, tapi saya marah karena Anda melarikan diri tanpa memikirkan konsekuensinya. Aku marah karena sesuatu bisa terjadi padamu. Anda mabuk dengan sepeda."
        toby "Saya marah karena saya harus berbohong kepada [mom] mengatakan bahwa semuanya baik -baik saja ketika saya berantakan, mencoba mencari tahu apa yang harus dilakukan."
        toby "Saya marah karena Anda merokok. Anda merusak paru -paru Anda."
        scene expression ("images/episode11/273_sad.webp") with dissolve
        patricia "Maaf."
        scene expression ("images/episode11/274_angry.webp") with dissolve
        toby "Tapi kebanyakan aku marah pada diriku sendiri. Karena butuh waktu selama ini untuk menyadari bagaimana perasaan saya tentang Anda."
        scene expression ("images/episode11/273_smile.webp") with dissolve
        patricia "Jadi ... kamu sangat menyukaiku?"
        scene expression ("images/episode11/274_smile.webp") with dissolve
        toby "Lebih dari itu [sis]."
        scene expression ("images/episode11/273_normal.webp") with dissolve
        patricia "Jadi saya kira Anda harus belajar bagaimana hidup dengan perasaan itu."
        scene expression ("images/episode11/274_laugh.webp") with dissolve
        toby "Hanya saya?"
        scene expression ("images/episode11/273_laugh.webp") with dissolve
        patricia "Ya, karena tidak seperti Anda, saya tidak memiliki perasaan sakit seperti ini terhadap anggota [family], tetapi tidak apa -apa. Saya akan berada di sini untuk Anda jika Anda membutuhkan saya."
        scene expression ("images/episode11/274_smile.webp") with dissolve
        toby "Betapa baiknya Anda."
        scene expression ("images/episode11/273_laugh.webp") with dissolve
        patricia "Saya tahu, kan?"
        scene expression ("images/episode11/274_curious.webp") with dissolve
        toby "Jadi itu artinya Anda pulang?"
        scene expression ("images/episode11/273_smile.webp") with dissolve
        patricia "Ya."
        scene expression ("images/episode11/274_normal.webp") with dissolve
        toby "Kemarilah. Beri aku pelukan."
        scene expression ("images/episode11/273_smile.webp") with dissolve
        patricia "Cobalah untuk tidak jatuh terlalu banyak untuk saya."
        scene expression ("images/episode11/274_laugh.webp") with dissolve
        toby "Saya akan melakukan yang terbaik."
        scene expression ("images/episode11/275.webp") with dissolve
        if toby_job == 0:
            toby "Jika Anda pernah mencuri sepeda saya, saya akan menendang pantat Anda."
        else:
            toby "Jika Anda pernah mencuri sepeda saya, saya akan memukul Anda."
        $ unlockImage(persistent.patricia_20)
        scene expression ("images/episode11/276.webp") with dissolve
        patricia "Anda seorang idiot."
        scene expression ("images/episode11/277.webp") with dissolve
        toby "Jadi? Ingin pulang sekarang, atau ...?"
        patricia "I'm coming with you. Bea is with her \"wannabe\"pacar. Saya merasa seperti roda ketiga."
        scene expression ("images/episode11/278.webp") with dissolve
        toby "Keren, mari kita katakan selamat tinggal dan pulang."
        scene expression ("images/episode11/279.webp") with dissolve
        patricia "Bisakah kita pergi ke suatu tempat untuk makan? Ibu Bea tidak memiliki keterampilan memasak."
        scene expression ("images/episode11/280.webp") with dissolve
        toby "Baik, tapi aku akan mandi dulu. Saya berbau."
        patricia "Saya perhatikan."
        scene expression ("images/episode11/281.webp") with dissolve
        toby "Kata ketel ke pot."
        patricia "Saya tidak bau. Saya mandi pagi ini."
        toby "Anda lupa sikat gigi Anda. Saya dapat memberi tahu Anda berapa banyak bidikan tequila yang Anda miliki."
        scene expression ("images/episode11/282.webp") with dissolve
        patricia "..."
        patricia "Saya terburu -buru."


        patricia "Anyway, let's go say goodbye to Bea and her \"wannabe\"Pacar dan kemudian kita bisa mandi."
        if lisa_path or lauren_path:
            toby "Maksudmu Joe?"
            scene expression ("images/episode11/283.webp") with dissolve
            patricia "Bagaimana Anda tahu?"
            toby "Tidakkah kamu tahu aku psikis?"
            toby "What I don't get is, why \"wannabe\"? Siapa yang mau itu?"
        else:
            toby "\"Wannabe\"pacar?"
            patricia "Ya. Jangan tanya. Itu rumit."
            scene expression ("images/episode11/283.webp") with dissolve
            toby "Why \"wannabe\"? Siapa yang mau itu?"
    else:

        scene expression ("images/episode11/259.webp") with dissolve
        patricia "Tidak ada yang terjadi dengan saya. Saya baik-baik saja."
        scene expression ("images/episode11/260.webp") with dissolve
        toby "Anda pergi tanpa mengucapkan sepatah kata pun. Itu tidak seperti Anda."
        scene expression ("images/episode11/261.webp") with dissolve
        patricia "..."
        scene expression ("images/episode11/262.webp") with dissolve
        patricia "Seperti yang kamu kenal aku."
        scene expression ("images/episode11/260.webp") with dissolve
        toby "Ok, mari kita bicara. Katakan padaku apa yang kamu suka. Katakan padaku apa yang mengganggumu."
        scene expression ("images/episode11/264.webp") with dissolve
        patricia "Yang mengganggu saya adalah kenyataan bahwa saya tidak bisa merokok dengan damai."
        scene expression ("images/episode11/265.webp") with dissolve
        patricia "Selamat tinggal!"
        scene expression ("images/episode11/266.webp") with dissolve
        if toby_job == 0:
            toby "Anda tidak ke mana -mana sampai Anda memberi tahu saya apa yang terjadi."
        else:
            toby "Anda tidak pergi ke mana pun. Anda tinggal di sini dan memberi tahu saya apa yang salah."
        patricia "Anda benar -benar menyakiti saya idiot! Lepaskan lenganku."
        toby "Tidak sampai Anda memberi tahu saya apa yang terjadi dengan Anda. Saya peduli untuk Anda, Anda tahu?"
        scene expression ("images/episode11/267.webp") with dissolve
        patricia "Tidak ada yang salah dengan saya."
        toby "[mom!c] benar -benar takut pagi ini ketika dia tidak bisa mendapatkan Anda."
        patricia "Baterai saya mati."
        toby "Jangan khawatir, saya meliput untuk Anda, tetapi Anda harus memberi tahu saya apa yang terjadi."
        patricia "Baik ... mari kita berjalan -jalan."
        scene expression ("images/episode11/268.webp") with dissolve
        patricia "Aku benci aku tidak punya siapa -siapa untuk diajak bicara.Aku benci di sini. Aku benci segalanya tentang kota ini. Aku benci berpura -pura baik -baik saja."
        patricia "Aku benci pulang hanya untuk melihat bagaimana [mom] dan [dad] tidak berbicara satu sama lain."
        patricia "Kemarin saya berada di klub dan saya mabuk sehingga saya bisa melupakan segalanya. Saya hanya ingin bersenang -senang."
        scene expression ("images/episode11/269.webp") with dissolve
        patricia "Tapi coba tebak. Saya sampai di rumah dan saya ingat segalanya. Saya ingat fakta bahwa [mom] dan [dad] berada di ambang bercerai."
        patricia "Anda memiliki pekerjaan yang baik. Anda mendapatkan uang yang baik dan saya berharap Anda pergi setiap hari sekarang dan meninggalkan kami di sini dalam kesengsaraan kami. Pindah dengan seorang gadis cantik dan aku akan terjebak di sini merawat [mom]."
        toby "Saya tidak akan pernah meninggalkan kalian berdua. Anda adalah orang -orang terpenting dalam hidup saya."
        scene expression ("images/episode11/270.webp") with dissolve
        patricia "Anda mengatakan itu sekarang, tetapi Anda sudah tidak banyak berkeliaran. Anda selalu memiliki sesuatu yang menarik terjadi."
        toby "Anda baru saja mulai kuliah. Saya yakin itu akan menjadi lebih baik untuk Anda juga."
        patricia "Saya rusak, [toby!c]! Saya tidak bisa menemukan pria normal. Semua orang yang meminta saya hanya memiliki 3 neuron di kepala mereka dan mereka bermain hide \ 'n Seek!"
        scene expression ("images/episode11/271.webp") with dissolve
        toby "Itu tidak bisa seburuk itu."
        patricia "Percayalah. Memiliki Anda sebagai [brother] adalah bagian dari masalah. Saya telah melihat Anda berbicara dengan perempuan. Anda tampak keren dan seperti Anda tahu apa yang Anda lakukan."
        patricia "Tapi setiap pria yang mendekati saya bertindak sangat bodoh. Mereka sangat ingin mengesankan saya dengan garis penjemputan yang bodoh itu."
        scene expression ("images/episode11/272.webp") with dissolve
        patricia "Saya akan berakhir sendirian, atau dengan idiot sebagai pacar dan kemudian dalam 10 tahun, saya akan berada dalam situasi yang sama dengan [mom]."
        scene expression ("images/episode11/274_normal.webp") with dissolve
        toby "Anda bereaksi berlebihan. Anda akan menemukan seseorang yang tepat untuk Anda."
        scene expression ("images/episode11/273_normal.webp") with dissolve
        patricia "Apa pun, tapi itu masih tidak berarti bahwa [family] kami bukan pertunjukan."
        scene expression ("images/episode11/274_smile.webp") with dissolve
        toby "Kamu punya aqw."
        scene expression ("images/episode11/273_normal.webp") with dissolve
        patricia "Apa pun."
        scene expression ("images/episode11/274_curious.webp") with dissolve
        toby "Jadi itu sebabnya Anda mengambil sepeda tadi malam? Karena kamu benci berada di rumah?"
        scene expression ("images/episode11/273_sad.webp") with dissolve
        patricia "Ya dan karena saya melihat betapa baiknya Beatrice [family]. Mereka tidak pernah punya uang, namun mereka begitu ketat."
        scene expression ("images/episode11/273_smile.webp") with dissolve
        patricia "Ibunya membuat makanan terburuk yang pernah ada, namun ayahnya selalu menghargainya dan mengatakan kepadanya betapa enak makanannya."
        scene expression ("images/episode11/274_laugh.webp") with dissolve
        toby "Apakah itu buruk?"
        scene expression ("images/episode11/273_laugh.webp") with dissolve
        patricia "Saya tidak berpikir dia tahu di mana garam atau merica berada di rumah mereka. Makanannya tidak seperti rasa. Saya tidak tahu bagaimana es krimnya sangat bagus."
        scene expression ("images/episode11/273_sad.webp") with dissolve
        patricia "Saya ingin merasakan bagian dari [family] yang bahagia."
        scene expression ("images/episode11/274_sad.webp") with dissolve
        toby "Lihat. Saya tahu kami bukan yang sempurna [family], tetapi kami saling peduli."
        scene expression ("images/episode11/274_normal.webp") with dissolve
        toby "Aku benci bagaimana [dad] telah berperilaku akhir -akhir ini, tapi aku tahu dia mencintai kita, dengan caranya sendiri."
        scene expression ("images/episode11/273_normal.webp") with dissolve
        patricia "Ya ... semuanya kacau."
        scene expression ("images/episode11/274_sad.webp") with dissolve
        toby "Lihat, tidak peduli seberapa kacau kami sebagai [family], [mom] dan aku mencintaimu dan aku khawatir sakit tentangmu. Saya tidak akan pergi ke mana pun."
        scene expression ("images/episode11/274_laugh.webp") with dissolve
        toby "Dan jika saya pergi, saya akan membawa Anda."
        scene expression ("images/episode11/273_laugh.webp") with dissolve
        if emma_break:
            patricia "Hanya jika Anda tidak bergerak sendirian."
        else:
            patricia "Hanya jika Anda tidak bergerak dengan Emma."
        scene expression ("images/episode11/274_laugh.webp") with dissolve
        toby "Oke ... berurusan!"
        scene expression ("images/episode11/274_normal.webp") with dissolve
        toby "Apakah Anda akan pulang sekarang?"
        scene expression ("images/episode11/273_normal.webp") with dissolve
        patricia "Lagipula aku akan pulang, karena aku benci tinggal di orang lain, tidak peduli seberapa sempurna [family] mereka."
        scene expression ("images/episode11/274_smile.webp") with dissolve
        toby "Kemarilah kamu bodoh. Beri aku pelukan."
        scene expression ("images/episode11/275.webp") with dissolve
        toby "Jika Anda pernah mencuri sepeda saya lagi, saya akan menendang pantat Anda."
        patricia "Maaf!"


        scene expression ("images/episode11/278.webp") with dissolve
        toby "Ayo. Mari pulang."
        scene expression ("images/episode11/279.webp") with dissolve
        patricia "Let me say goodbye to Bea and her \"wannabe\"Pacar dulu."
        scene expression ("images/episode11/280.webp") with dissolve
        if lisa_path or lauren_path:
            toby "Maksudmu Joe?"
            patricia "Bagaimana Anda tahu?"
            scene expression ("images/episode11/283.webp") with dissolve
            toby "Tidakkah kamu tahu aku psikis?"
            toby "What I don't get is, why \"wannabe\"? Siapa yang mau itu?"
        else:
            toby "\"Wannabe\"pacar?"
            patricia "Ya. Jangan tanya. Itu rumit."
            scene expression ("images/episode11/283.webp") with dissolve
            toby "Why \"wannabe\"? Siapa yang mau itu?"

    patricia "Dia melakukannya. Dia telah mengajaknya keluar selama dua bulan."
    toby "Pria malang."
    scene expression ("images/episode11/284.webp") with dissolve
    patricia "Bagaimanapun. Itu ada."
    $ progress = 151
    scene expression ("images/episode11/285.webp") with dissolve
    patricia "Hai teman -teman, saya akan lepas landas."
    beatrice "Sudah?"
    patricia "Ya. Saya meminta [toby!c] untuk datang menjemput saya. Saya tidak benar -benar berminat untuk pantai."
    joe "Menyesal mendengarnya."

    if beatrice_path:
        scene expression ("images/episode11/286_1.webp") with dissolve
        joe "Omong-omong. Saya Joe!"
        scene expression ("images/episode11/287.webp") with dissolve
        menu:
            "{i} [JGR] Peras tangannya keras {/i}":
                toby "Senang bertemu denganmu, Joe!"
                scene expression ("images/episode11/288.webp") with dissolve
                joe "M-ME ... juga!"
                scene expression ("images/episode11/289.webp") with dissolve
                toby "Ngomong -ngomong, Bea, kamu terlihat sangat hebat hari ini."
                scene expression ("images/episode11/290.webp") with dissolve:
                    xalign 0.0
                    yalign 1.0
                    linear 10.0 yalign 0.0 xalign 0.8

                $ ui.pausebehavior(9.3)
                $ ui.saybehavior()
                $ ui.interact()
                beatrice "Terima kasih!"
            "{i} nice {/i} [JWRN6]"(csq="Jalur Beatrix ditutup"):

                $ beatrice_path = False
                $ renpy.notify("Beatrice's path has been closed!")
                toby "Senang bertemu denganmu Joe!"
    else:
        scene expression ("images/episode11/286_2.webp") with dissolve
        joe "Omong-omong. Saya Joe!"
        scene expression ("images/episode11/287.webp") with dissolve
        toby "Senang bertemu denganmu Joe!"

    scene expression ("images/episode11/291.webp") with dissolve
    toby "Haruskah kita?"
    patricia "Tentu!"
    scene expression ("images/episode11/292.webp") with dissolve
    toby "Ngomong -ngomong, kita berjalan kaki."
    patricia "Apa maksudmu, berjalan kaki?"
    toby "Maksud saya, saya datang ke sini untuk jogging, ingat?"
    scene expression ("images/episode11/293.webp") with dissolve
    patricia "Dan sekarang Anda memberi tahu saya? Jika saya tahu saya akan menunggu Bea membawa saya pulang dengan truk es krimnya."
    toby "Itulah yang Anda dapatkan untuk melarikan diri dari rumah."
    patricia "Ya, ya."

    return

label episode11_dateTris:
    scene expression ("images/episode11/294.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/295.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/296.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/297.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/298.webp") with dissolve:
        xalign 0.5
        yalign 0.5
        zoom 0.8
        linear 120.0 zoom 1.3 yalign 0.0

    patricia "Anda pergi mandi saat saya akan berbicara dengan [mom] sebentar."



    scene expression ("images/episode11/299.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/300.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/301.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    label memory_37:
        if _in_replay:

            scene expression ("images/utils/black.png") with dissolve
            menu:
                "Pilih pekerjaan Anda"
                "Agen real estat":
                    $ toby_job == 0
                "Manajer klub":
                    $ toby_job == 1
        scene expression ("images/episode11/302.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode11/303.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode11/304.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode11/305.webp") with dissolve
        if toby_job == 0:
            toby "Apa yang sedang kamu lakukan? Saya mandi di sini."
        else:
            toby "Apa yang kamu lakukan, [sis]? Saya mandi."
        scene expression ("images/episode11/306.webp") with dissolve
        patricia "Apa? Saya perlu menyikat gigi dan bersiap -siap."
        toby "Dan Anda tidak bisa menunggu sedikit lebih lama sampai saya selesai?"
        scene expression ("images/episode11/307.webp") with dissolve
        patricia "Jangan repot -repot menutupi diri Anda. Ini tidak seperti saya tertarik melihat weiner Anda. Anda yang sakit, bukan saya."
        scene expression ("images/episode11/308.webp") with dissolve
        toby "Jika itu masalahnya."
        scene expression ("images/episode11/309.webp") with dissolve
        patricia "Agak kecil jika Anda bertanya kepada saya."
        scene expression ("images/episode11/310.webp") with dissolve
        toby "Nah, aku tidak bertanya padamu!"
        scene expression ("images/episode11/311.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode11/312.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What is she doing now?{/i}"
        scene expression ("images/episode11/313.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode11/314.webp") with dissolve
        patricia "Saya tidak berpikir itu akan menjadi ide yang baik untuk terus mengenakan pakaian renang pada tanggal kami. Bagaimana menurutmu?"
        menu:
            "Saya tidak peduli" if not _in_replay:
                scene expression ("images/episode11/315.webp") with dissolve
                patricia "Sampai jumpa di luar."
            "[JGR] Ya ... mungkin tidak."(csq="Gambar galeri"):
                scene expression ("images/episode11/316.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                $ unlockImage(persistent.patricia_21)
                scene expression ("images/episode11/317.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode11/318.webp") with dissolve
                patricia "Ngomong -ngomong, sepertinya kamu punya situasi kecil di sana."
                toby "Keluar!"
                scene expression ("images/episode11/319.webp") with dissolve
                patricia "Asal kamu tahu. Aku benar -benar lapar. Kami tidak punya waktu bagi Anda untuk menyentak memikirkan siapa yang tahu apa."
                toby "Pastikan Anda mengenakan gaun yang bagus, karena kami pergi ke restoran mewah. Aku berjanji padamu."
                patricia "Anda ingat."
                toby "Sekarang keluar!"
                scene expression ("images/episode11/320.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What am I going to do with her? She likes to tease me so much. She's so gorgeous.{/i}"
                if charlotte_path:
                    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}How did I end up in this situation? I'm attracted to both my [mother] and my [sister].{/i}"
                else:
                    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}How did I up in this situation? I'm attracted to my [sister].{/i}"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This feels so fucked up, but I love it.{/i}"

        $ unlockMemory(persistent.memory_37)
        $ renpy.end_replay()

    scene expression ("images/episode11/321.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why am I feeling so anxious about this date. It's just Tris. We're just going to eat something, then come back. Nothing we haven't done before.{/i}"
    scene expression ("images/episode11/322.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But this is the first time we're going out after I told her how I feel, and I know she feels the same even though she's trying to act nonchalant.{/i}"
    $ progress = 152
    scene expression ("images/episode11/323.webp") with fade
    toby "Anda selesai?"
    scene expression ("images/episode11/324.webp") with dissolve
    patricia "Ya."
    scene expression ("images/episode11/325.webp") with dissolve
    patricia "Haruskah kita?"
    scene expression ("images/episode11/326.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    toby "Wow ... kamu terlihat bagus."
    patricia "Terima kasih! Anda mengatakan bahwa kami akan makan di restoran mewah, jadi saya melakukan yang terbaik."
    scene expression ("images/episode11/327.webp") with dissolve
    toby "Anda mungkin terlalu berpakaian! Ini tidak terlalu mewah."
    patricia "Terlambat sekarang. Saya suka berpakaian bagus!"

    stop music fadeout 5.0
    scene expression ("images/episode11/328.webp") with dissolve
    charlotte "Ya ampun. Di mana kalian berdua berpakaian sangat bagus?"
    scene expression ("images/episode11/329.webp") with dissolve
    toby "Saya berjanji pada Tris bahwa saya akan membawanya ke restoran mewah dengan gaji pertama saya seperti 100 tahun yang lalu dan dia mengingatkan saya setiap hari. Saatnya menandai janji saya."
    scene expression ("images/episode11/328.webp") with dissolve
    charlotte "Itu gadisku!"

    scene expression ("images/episode11/330.webp") with dissolve
    patricia "Haruskah kita?"
    toby "Tentu ... lepaskan."
    scene expression ("images/episode11/331.webp") with fade
    patricia "Anda mencoba membuat saya terkesan?"
    toby "Tentu saja. Aku berharap bisa membawamu pulang malam ini."
    scene expression ("images/episode11/332.webp") with dissolve
    patricia "Aku hampir yakin kamu akan membawaku pulang malam ini."
    toby "Saya sebagus itu?"
    patricia "Saya berbicara tentang fakta bahwa kita tinggal di rumah yang sama, tetapi tentu saja. Mengapa tidak! Anda baik -baik saja."
    scene expression ("images/episode11/333.webp") with dissolve
    patricia "Jadi? Dimana?"
    toby "Ada tempat makanan cepat saji baru di kota yang sangat dekat di sini."
    patricia "Tolong beritahu saya bahwa saya tidak akan berpakaian seperti ini ke rantai makanan cepat saji."
    scene expression ("images/episode11/334.webp") with dissolve
    toby "Kami dapat kembali berubah jika Anda mau."
    patricia "Jangan. Aku terlalu lapar dan selain itu aku tidak terlalu keberatan. Saya bisa pergi ke restoran dengan piyama atau gaun pengantin untuk pertandingan sepak bola. Saya benar -benar tidak peduli."
    toby "Dingin."
    scene expression ("images/episode11/335.webp") with dissolve
    patricia "Tapi akan menyenangkan bagi Anda untuk memberi tahu saya ke mana kami pergi."
    toby "Itu lucu."
    patricia "Anda tahu apa lagi yang lucu?"
    toby "Kejutan saya."
    scene expression ("images/episode11/336.webp") with dissolve
    patricia "Fakta bahwa saya akan membuat Anda kembali untuk ini dan saya akan memesan cukup makanan untuk 10 orang yang akan Anda bayar."
    toby "Anda sangat buruk."
    patricia "Anda tidak tahu."
    scene expression ("images/episode11/338.webp") with fade
    patricia "Tunggu, Anda menipu saya. Ini bukan makanan cepat saji."
    toby "Nah, aku memang menjanjikan sesuatu yang mewah, bukan?"
    patricia "Ya, tapi kalau begitu ..."
    scene expression ("images/episode11/339.webp") with dissolve
    patricia "Anda seorang idiot!"
    toby "Aku pun mencintaimu!"
    scene expression ("images/episode11/340.webp") with dissolve
    waitress "Selamat siang, apakah Anda memiliki reservasi?"
    toby "Tidak, kami tidak. Apakah Anda memiliki meja terbuka untuk dua orang?"
    waitress "Ya, ikuti saya."
    scene expression ("images/episode11/341.webp") with dissolve
    toby "Bisakah kita memiliki dua menu."
    waitress "Tentu ... segera kembali!"
    scene expression ("images/episode11/342.webp") with dissolve
    patricia "Anda mengingatkan saya pada [dad] ketika dia keren. Saya ingat betapa baiknya perasaan saya ketika kami pergi ke restoran bersamanya dan dia sangat yakin pada dirinya sendiri."
    toby "Pertama -tama, [dad] tidak pernah keren."
    toby "Kedua, tidak terlalu sulit untuk berbicara dengan seorang pelayan."
    toby "Ketiga, apakah menurut Anda saya keren?"
    scene expression ("images/episode11/343.webp") with dissolve
    patricia "Mungkin pada awalnya, tetapi kemudian Anda berubah pikiran ketika Anda mengatakan bahwa [dad] tidak pernah keren, yang juga berlaku untuk Anda."
    toby "Saya dan mulut besar saya."
    scene expression ("images/episode11/344.webp") with dissolve
    waitress "Ini dia."
    toby "Terima kasih!"
    scene expression ("images/episode11/345.webp") with dissolve
    patricia "Jadi? Menu apa yang Anda sarankan?"
    scene expression ("images/episode11/346.webp") with dissolve
    toby "Ini pertama kalinya saya di sini, jadi saya tidak tahu apa yang bagus, tetapi tempat itu memiliki banyak ulasan bagus di internet jadi saya ingin memeriksanya dan karena saya berjanji kepada Anda, saya akan membawa Anda ke tempat yang bagus ..."
    scene expression ("images/episode11/345.webp") with dissolve
    patricia "Jadi Anda belum membawa gadis lain ke sini?"
    scene expression ("images/episode11/346.webp") with dissolve
    toby "Tidak. Hanya kamu!"
    scene expression ("images/episode11/345.webp") with dissolve
    patricia "Saya merasa tersanjung."
    scene expression ("images/episode11/346.webp") with dissolve
    toby "Sebagaimana mestinya."
    scene expression ("images/episode11/347.webp") with dissolve
    toby "Jadi? Sudahkah Anda memutuskan apa yang ingin Anda makan?"
    patricia "Saya kira demikian. Saya pergi untuk Spaghetti Carbonara."
    toby "Itu hal termurah di menu. Anda bilang Anda lapar."
    scene expression ("images/episode11/348.webp") with dissolve
    patricia "Pernahkah Anda melihat harga di tempat ini?"
    toby "Jangan khawatir, [sis]. Tidak apa -apa."
    patricia "Saya merasa tidak enak. Mari kita pergi ke tempat lain."
    toby "Oke kalau begitu. Anda akan mendapatkan hal yang sama dengan saya."
    scene expression ("images/episode11/349.webp") with dissolve
    patricia "Apa itu?"
    toby "Sirloin panggang dengan anggur merah."
    patricia "Saya tidak berpikir anggur adalah ide yang sangat bagus, mengingat apa yang terjadi tadi malam."
    scene expression ("images/episode11/350.webp") with dissolve
    toby "Jangan khawatir, aku ada di sini untukmu. Tidak ada yang akan terjadi."
    patricia "Dan bagaimana jika Anda mabuk juga?"
    toby "Lalu kita berhubungan seks."
    scene expression ("images/episode11/351.webp") with dissolve
    patricia "[toby!u]!"
    toby "Dinginkan ... tidak ada yang akan terjadi. Saya tidak mabuk dari satu gelas anggur dan Anda juga tidak."
    scene expression ("images/episode11/352.webp") with dissolve
    toby "Jadi? Apa kabar hari ini?"
    patricia "Apakah ini jenis pembicaraan kecil yang biasanya Anda miliki saat berkencan?"
    if toby_job == 0:
        toby "No. Usually I start with \"God, you have a beautiful smile\"."
        scene expression ("images/episode11/353.webp") with dissolve
        patricia "Ummm ... terima kasih."
        toby "Dan kemudian aku menatap matamu yang indah selama beberapa detik bertanya -tanya apa yang aku lakukan begitu baik dalam kehidupan masa lalu untuk mendapatkan kencan dengan seorang gadis sepertimu."
        scene expression ("images/episode11/355.webp") with dissolve
        patricia "Oke, mari kita bicara tentang hari saya."
    else:
        toby "TIDAK! Biasanya saya bertanya apa warna pakaian dalamnya."
        scene expression ("images/episode11/354.webp") with dissolve
        patricia "Hitam!"
        toby "Renda?"
        patricia "Mungkin? Ingin mencari tahu?"
        toby "Tidak sekarang. Mungkin saat kita pulang."
        scene expression ("images/episode11/355.webp") with dissolve
        patricia "Mari kita bicara tentang hari saya."

    scene expression ("images/episode11/352.webp") with dissolve
    patricia "Jadi kami bangun sekitar jam 11, karena saudara laki -laki Bea sedang mengadakan konser rock di kamarnya dan dia membangunkan kami dengan gitar bodohnya."
    toby "Saya sudah menyukai pria ini."
    patricia "Idiot!"
    scene expression ("images/episode11/356.webp") with dissolve
    waitress "Permisi. Sudahkah Anda memutuskan untuk memesan apa?"
    toby "Ya kami punya. Kami seperti 2 dari sirloin spesial panggang dengan sebotol anggur merah terbaik Anda."
    waitress "Pilihan yang sangat baik. Datang segera."
    scene expression ("images/episode11/357.webp") with dissolve
    toby "Anda berkata?"
    patricia "Ya, jadi kami terbangun pada jam 11 \ 'dan Bea [mom] sedang memasak telur dan bacon, tetapi baunya sangat buruk, jadi saya berbohong dan mengatakan kepadanya bahwa saya biasanya tidak makan di pagi hari."
    toby "Bagaimana Anda bisa merusak telur dan bacon?"
    patricia "Anda tidak tahu."
    scene expression ("images/episode11/358.webp") with dissolve
    toby "Anda terlalu pilih -pilih!"
    patricia "Saya tidak! Tapi saya tidak ingin mengambil risiko lagi. Terakhir kali saya makan sesuatu yang dibuat oleh ibunya, saya merasa sakit sepanjang hari dan sepanjang malam."
    scene expression ("images/episode11/359.webp") with dissolve
    toby "Tinggalkan botolnya."
    waitress "Tentu saja!"
    scene expression ("images/episode11/360_laugh.webp") with dissolve
    patricia "\"You're not getting drunk from a glass of wine\". Five minutes later \"Leave the bottle\"."
    scene expression ("images/episode11/361_smile.webp") with dissolve
    if toby_job == 0:
        toby "Lihatlah warna itu. Akan menjadi dosa hanya minum satu gelas."
    else:
        toby "Saya biasanya minum wiski di tempat kerja tetapi ketika saya melihat warnanya, rasanya salah hanya minum satu gelas."
    scene expression ("images/episode11/360_smile.webp") with dissolve
    patricia "Oke, tapi saya membawa kami pulang."
    scene expression ("images/episode11/361_laugh.webp") with dissolve
    toby "Oh, neraka tidak! Drunk [toby!c] adalah pengemudi yang lebih baik daripada Sober Tris."
    scene expression ("images/episode11/360_surprised.webp") with dissolve
    patricia "Kapan terakhir kali Anda melihat saya mengemudi?"
    scene expression ("images/episode11/361_normal.webp") with dissolve
    toby "Saya melihat bagaimana Anda memarkir sepeda saya kemarin. Itu luar biasa itu tidak rusak."
    scene expression ("images/episode11/360_cool.webp") with dissolve
    patricia "Pertama -tama, saya mabuk kemarin dan kedua itu adalah sepeda bukan mobil."
    scene expression ("images/episode11/361_normal.webp") with dissolve
    toby "Saya akan memikirkannya."
    scene expression ("images/episode11/360_excited.webp") with dissolve
    patricia "Terima kasih! Anda yang terbaik."
    scene expression ("images/episode11/361_curious.webp") with dissolve
    toby "Saya pikir Anda tidak suka mengemudi."
    scene expression ("images/episode11/360_normal.webp") with dissolve
    patricia "Itu tidak benar. Saya suka mengemudi, tetapi biasanya ketika saya mengendarainya dengan [mom] atau [dad] di kursi penumpang dan mereka membuat saya gila."
    scene expression ("images/episode11/360_angry.webp") with dissolve
    patricia "\"Hati-hati. Itu persimpangan jalan.\", \"Warnanya merah!\", \"Rem, rem, rem, sialan!\", \"Jangan ngebut!\", \"Kamu tidak perlu secepat ini. Kita tidak terburu-buru.\""
    scene expression ("images/episode11/361_laugh.webp") with dissolve
    toby "Malang kamu!"
    scene expression ("images/episode11/360_meh.webp") with dissolve
    patricia "Saya tidak mendapatkannya. Mengapa mereka lebih mempercayai Anda daripada mempercayai saya?"
    scene expression ("images/episode11/361_smile.webp") with dissolve
    toby "Mungkin karena saya terlihat lebih dapat dipercaya dan lebih dewasa."
    scene expression ("images/episode11/360_cool.webp") with dissolve
    patricia "Ya, benar. Itu pasti! Mereka pasti seksis."
    scene expression ("images/episode11/361_laugh.webp") with dissolve
    toby "Ya terutama [mom]. Dia seorang seksis."
    scene expression ("images/episode11/360_normal.webp") with dissolve
    patricia "Mungkin bukan dia, tapi [dad]."
    scene expression ("images/episode11/361_smile.webp") with dissolve
    toby "Saya tidak berdebat."
    scene expression ("images/episode11/361_curious.webp") with dissolve
    toby "Ngomong -ngomong, Anda tidak memberi tahu saya bagaimana sisa hari Anda berjalan."
    scene expression ("images/episode11/360_meh.webp") with dissolve
    patricia "Saya menghindari menjawab dengan sengaja."
    scene expression ("images/episode11/361_curious.webp") with dissolve
    toby "Dan alasannya?"
    scene expression ("images/episode11/360_sad.webp") with dissolve
    patricia "Karena yang saya lakukan hanyalah memikirkan betapa pelacurnya saya. Dan bagaimana saya dulu menilai Emma, karena dia berpakaian sedikit minim dan saya memanggilnya pengisap ayam, dan begitu saya mabuk saya berakhir dengan penis di mulut saya."
    scene expression ("images/episode11/360_normal.webp") with dissolve
    patricia "Aku sangat palsu. Saya benci gadis -gadis yang tidur dengan pria pertama yang mereka temui dan bagaimana mereka lebih sering mengganti pria daripada kaus kaki mereka dan sekarang menatap saya."
    scene expression ("images/episode11/360_sad.webp") with dissolve
    patricia "You aren't my boyfriend, you didn't even flirt with me and what did I do? \"Put that cock in your mouth, Tris\"."
    scene expression ("images/episode11/361_sad.webp") with dissolve
    toby "Anda terlalu keras pada diri sendiri, Tris. Anda bukan pelacur. Tidak terjadi apa-apa. Anda baru saja minum terlalu banyak."
    scene expression ("images/episode11/360_normal.webp") with dissolve
    patricia "Apa pun!"
    scene expression ("images/episode11/361_smile.webp") with dissolve
    toby "Memberitahu apa. Anda memilih hari ketika Anda dan saya bisa pergi ke bar atau klub dan saya akan mengajari Anda cara minum secara bertanggung jawab."
    scene expression ("images/episode11/361_normal.webp") with dissolve
    toby "Anda tidak terbiasa dengan alkohol. Tapi seperti kebanyakan hal, ini bisa dilatih. Pertama, kami hanya akan minum sedikit, dan kemudian sedikit lebih dan lebih banyak lagi, sampai Anda dapat mengendalikan diri Anda bahkan jika Anda minum seperti orang Viking."
    scene expression ("images/episode11/360_pirate.webp") with dissolve
    patricia "Arrr ..."
    scene expression ("images/episode11/361_facepalm.webp") with dissolve
    toby "Saya bilang Viking, bukan bajak laut."
    scene expression ("images/episode11/360_shy.webp") with dissolve
    patricia "Burukku. Bagaimana suara Viking?"
    scene expression ("images/episode11/361_normal.webp") with dissolve
    toby "Mengingat fakta bahwa mereka adalah manusia seperti kita, saya akan mengatakan suara yang mereka buat adalah kata -kata."
    scene expression ("images/episode11/360_cool.webp") with dissolve
    patricia "Smartass."
    scene expression ("images/episode11/360_normal.webp") with dissolve
    patricia "Jadi, apakah saya harus memilih hari seperti hari Kamis misalnya, dan kemudian setiap hari Kamis Anda membawa saya ke bar, atau dapatkah saya mengatakan hari Minggu minggu ini dan minggu berikutnya memilih hari yang berbeda?"
    scene expression ("images/episode11/361_smile.webp") with dissolve
    toby "Saya fleksibel."
    scene expression ("images/episode11/360_laugh.webp") with dissolve
    patricia "Oke. Saya memilih hari Minggu."
    scene expression ("images/episode11/361_laugh.webp") with dissolve
    toby "Maksudmu besok?"
    scene expression ("images/episode11/360_smile.webp") with dissolve
    patricia "Ya."
    scene expression ("images/episode11/361_smile.webp") with dissolve
    toby "Baiklah kalau begitu. Besok malam saya akan mengajari Anda cara minum seperti orang dewasa."
    scene expression ("images/episode11/362.webp") with dissolve
    patricia "Anda telah mendapatkan kesepakatan."
    $ progress = 153
    scene expression ("images/episode11/363.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/364.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/365.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/366_1.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/366_2.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/367.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/368.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/369.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode11/370.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    $ unlockImage(persistent.patricia_22)
    scene expression ("images/episode11/371.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    patricia "Terima kasih untuk hari ini dan terima kasih telah ada untuk saya. Saya sangat membutuhkan ini."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
