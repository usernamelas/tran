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
    denise "Apakah Anda yakin tidak dapat membawa saya ke stasiun kereta? Keterampilan mengemudi [mom] Anda adalah ... yah ... Anda tahu apa yang saya maksud. Dia tidak memiliki keterampilan apa pun."
    toby "Dia tidak seburuk itu. Lagipula, dia mengantarku bolak -balik ke sekolah selama bertahun -tahun dan aku masih memiliki lengan dan kaki."
    scene expression ("images/episode10/002.webp") with dissolve
    if denise_path:
        denise "Mungkin, tapi itu tidak berarti Anda benar -benar sehat."
        denise "Ada yang salah dengan kepalamu, sayang. Kenapa lagi kamu membeli pakaian dalam [aunt] seksi dan menggoda dia?"
        toby "Apakah Anda benar -benar berpikir mengemudi [mom] akan salah?"
        if emma_break == False:
            denise "Tentu saja. Apa lagi? Maksud saya, kami berdua tahu Anda tidak kekurangan vagina."
        else:
            denise "Entah itu atau mungkin Anda tidak mendapatkan cukup vagina."

        scene expression ("images/episode10/003_laugh.webp") with dissolve
        toby "Jika [mom] mendengar Anda berbicara seperti itu dia tidak akan membiarkan Anda tinggal bersama kami minggu depan."
    else:

        denise "Nah, itu melegakan. Tetapi Anda masih perlu memeriksa kepala."
        scene expression ("images/episode10/003_normal.webp") with dissolve
        toby "Jika saya memiliki masalah mental, itu karena [mom] dan [dad] berdebat hampir setiap hari, bukan karena keterampilan mengemudi."
        scene expression ("images/episode10/004_laugh.webp") with dissolve
        denise "Maksud Anda kurangnya keterampilan mengemudi."
        scene expression ("images/episode10/003_laugh.webp") with dissolve
        toby "Hati -hati, dia mungkin mendengarmu dan kemudian dia akan membiarkanmu tinggal bersama kami minggu depan."

    if emma_break == False:
        scene expression ("images/episode10/004_flirty.webp") with dissolve
        denise "Dinding di rumah Anda sangat tipis, jadi jika dia membiarkan Anda tinggal di bawah atap yang sama setelah apa yang Anda lakukan tadi malam, saya yakin dia akan membiarkan saya tinggal di sini minggu depan juga."
        scene expression ("images/episode10/003_surprised.webp") with dissolve
        toby "Kotoran! Anda berantakan dengan saya kan?"
        scene expression ("images/episode10/004_laugh.webp") with dissolve
        denise "Mungkin ... mungkin tidak, tapi saya cukup yakin pacar Anda tidak bisa duduk dengan benar selama beberapa hari."
        scene expression ("images/episode10/003_ashamed.webp") with dissolve
        toby "Persetan ... menurutmu [mom] mendengar kita?"
        if patricia_path:
            scene expression ("images/episode10/004_smile.webp") with dissolve
            denise "Jangan khawatir. Dia tidak, tetapi orang lain mungkin memilikinya. Saya hanya mendengar karena saya pergi ke kamar mandi untuk memeriksa Tris karena dia pergi selama 10 menit."
            scene expression ("images/episode10/003_surprised.webp") with dissolve
            toby "Kotoran! Dia mendengar kami?"
            scene expression ("images/episode10/004_laugh.webp") with dissolve
            denise "Siapa yang tahu? Mungkin dia melakukannya, mungkin dia tidak."
    else:

        scene expression ("images/episode10/004_laugh.webp") with dissolve
        denise "Saya yakin dia suka memiliki saya di sini."
        scene expression ("images/episode10/003_laugh.webp") with dissolve
        toby "Kecuali saat Anda mengolok -olok berat badannya."
        scene expression ("images/episode10/004_smile.webp") with dissolve
        denise "Jadi apa? Dia membutuhkan sedikit dorongan, dia menjadi malas."

    scene expression ("images/episode10/004_curious.webp") with dissolve
    denise "Jadi saya tidak mengira saya bisa meyakinkan Anda untuk ikut dengan kami ke stasiun kereta?"
    scene expression ("images/episode10/003_laugh.webp") with dissolve
    toby "Sayangnya, tidak. Sayangnya, seseorang harus bekerja di rumah ini."
    scene expression ("images/episode10/004_smile.webp") with dissolve
    denise "Saya suka [family] Anda. Ini sangat tradisional. Para pria pergi bekerja untuk menyediakan [family] sementara para wanita tinggal di rumah bosan."
    if patricia_path and charlotte_path:
        scene expression ("images/episode10/003_flirty.webp") with dissolve
        toby "Dan membeli barang -barang mahal. Para wanita di [family] ini memiliki selera yang mahal."
    elif patricia_path:
        scene expression ("images/episode10/003_flirty.webp") with dissolve
        toby "Tris memiliki selera yang mahal dan [dad] tidak memberinya uang pengeluaran."
        scene expression ("images/episode10/004_laugh.webp") with dissolve
        denise "Namun dia membersihkan kamar Anda untuk uang itu."
        scene expression ("images/episode10/003_laugh.webp") with dissolve
        toby "Dia perlu mempelajari nilai uang."
    elif charlotte_path:
        scene expression ("images/episode10/003_flirty.webp") with dissolve
        toby "Seseorang perlu mengurus [mom] karena [dad] tidak melakukannya dengan baik."
    else:
        scene expression ("images/episode10/003_laugh.webp") with dissolve
        toby "Ya. Saya dibesarkan untuk memperlakukan wanita dengan benar."

    if denise_path:
        scene expression ("images/episode10/004_flirty.webp") with dissolve
        denise "Dan bagaimana saya bisa bergabung dengan [family] dengan semua hak ini? Saya tidak pernah memiliki ayah gula."
        scene expression ("images/episode10/003_laugh.webp") with dissolve
        toby "Atau gula [nephew]."
        scene expression ("images/episode10/004_laugh.webp") with dissolve
        $ unlockImage(persistent.denise_04)
        denise "Anda membuatnya terdengar sangat kotor. Saya sangat membutuhkan ayah gula, tetapi bergabung dengan [family] Anda untuk setidaknya mendapatkan beberapa perhatian Anda bisa menyenangkan."
    else:
        scene expression ("images/episode10/004_laugh.webp") with dissolve
        denise "Dimana saya harus mendaftar?"
    scene expression ("images/episode10/003_smile.webp") with dissolve
    toby "Nah ... sebagai permulaan Anda harus bertahan lebih dari beberapa hari."
    scene expression ("images/episode10/004_curious.webp") with dissolve
    denise "Tidakkah kamu akan bosan denganku?"
    scene expression ("images/episode10/003_laugh.webp") with dissolve
    toby "Bagaimana saya bisa? Anda yang paling keren [aunt] yang pernah ada."
    scene expression ("images/episode10/004_cool.webp") with dissolve
    denise "Ini tidak seperti saya memiliki kompetisi."
    scene expression ("images/episode10/003_smile.webp") with dissolve
    toby "Anda tahu [dad] memiliki [sister] juga, kan?"
    scene expression ("images/episode10/004_laugh.webp") with dissolve
    denise "Hag tua itu tidak bisa bersaing dengan saya dalam kontes yang keren."
    scene expression ("images/episode10/003_smile.webp") with dissolve
    toby "Jadi itu berarti minggu depan Anda akan tinggal lebih lama?"
    scene expression ("images/episode10/004_laugh.webp") with dissolve
    denise "Saya harus menjalankannya dengan [mother] Anda terlebih dahulu."
    scene expression ("images/episode10/005.webp") with dissolve
    charlotte "Jalankan apa dengan saya?"
    scene expression ("images/episode10/006.webp") with dissolve
    toby "Jika dia bisa tinggal bersama kami lebih dari dua hari minggu depan."
    scene expression ("images/episode10/005.webp") with dissolve
    charlotte "Hanya jika dia berhenti mengolok -olok perutku."
    scene expression ("images/episode10/007.webp") with dissolve
    denise "Perut? Perut apa? Anda memiliki tubuh dewi Yunani."
    scene expression ("images/episode10/008.webp") with dissolve
    charlotte "Anda bisa tinggal selama yang Anda suka."
    scene expression ("images/episode10/009.webp") with dissolve
    denise "Saya kira saya akan bertahan sedikit lebih lama minggu depan."
    scene expression ("images/episode10/010.webp") with dissolve
    charlotte "Oke, sudah waktunya. Ayo pergi."
    scene expression ("images/episode10/011.webp") with dissolve
    denise "Izinkan saya setidaknya mengucapkan selamat tinggal pada favorit saya [nephew]."
    if denise_path:
        scene expression ("images/episode10/010.webp") with dissolve
        charlotte "Anda hanya mengatakan itu sehingga dia akan membelikan Anda lebih banyak pakaian."
        scene expression ("images/episode10/011.webp") with dissolve
        denise "Jadilah gadis yang baik dan tunggu saya di dalam mobil."
        scene expression ("images/episode10/012.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        if ep8_denise_lingerie:
            denise "Terima kasih atas segalanya, terutama pakaian dalam yang seksi itu."
            toby "Dengan senang hati."
            denise "Oh, saya yakin akan hal itu."
        else:
            denise "Terima kasih atas segalanya, sayang."
            toby "Tidak masalah."
    else:
        scene expression ("images/episode10/013.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        denise "Jaga [mom] dan [sister] Anda."
        toby "Anda tahu saya akan."

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
    waiter "Wow ... kamu terlihat hebat."
    charlotte_ "Anda juga tidak terlihat sangat buruk."
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}No, no, no... That was NOT what I was supposed to say.{/i}"
    scene expression ("images/episode10/327.webp") with dissolve
    $ toby_ = reverse_name(toby)
    toby_ "Ngomong -ngomong, saya [toby_!c],."
    scene expression ("images/episode10/332.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Wait, what?!?! That's my name. Is this fantasy really about me? Does my [mom] have a fantasy about me?{/i}"
    scene expression ("images/episode10/328_1.webp") with dissolve
    charlotte_ "Senang berkenalan dengan Anda. Ettola Rahc."
    scene expression ("images/episode10/328_2.webp") with dissolve
    toby_ "Anda memiliki nama yang indah."
    scene expression ("images/episode10/329.webp") with dissolve
    charlotte_ "Dan Anda harus memiliki bos yang hebat untuk membiarkan Anda tidak melakukan apa pun selain menunggu wanita yang sudah menikah datang ke restoran."
    toby_ "Dia tidak memiliki suara dalam apa yang saya lakukan pada hari libur saya."
    scene expression ("images/episode10/330_1.webp") with dissolve
    charlotte_ "Oh. Hari liburmu? Dan bagaimana Anda tahu kapan saya akan berada di sini?"
    scene expression ("images/episode10/330_2.webp") with dissolve
    toby_ "Saya tidak. Saya datang ke sini tepat setelah kami mengirim sms. Saya tidak ingin melewatkan kesempatan saya untuk berbicara dengan Anda."
    scene expression ("images/episode10/330_1.webp") with dissolve
    charlotte_ "Tapi itu hampir 12 jam yang lalu."
    scene expression ("images/episode10/330_2.webp") with dissolve
    toby_ "Saya akan mengatakan itu layak untuk ditunggu."
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
    toby "Hei, bos! Apa dengan wajah serius?"
    darlene "Sebelum saya menjawab, saya hanya ingin memberi tahu Anda bahwa saya pikir Anda adalah aset besar bagi perusahaan dan jika Anda membutuhkan bantuan dengan apa pun di masa depan, yang harus Anda lakukan adalah bertanya."
    scene expression ("images/episode10/020_curious.webp") with dissolve
    toby "Apa yang kamu bicarakan? Apa yang terjadi?"
    scene expression ("images/episode10/021_normal.webp") with dissolve
    darlene "Di atas meja ada kertas yang harus Anda tanda tangani dan di dalam amplop adalah keuntungan yang Anda hasilkan untuk apartemen Anda setelah kami menjualnya."
    scene expression ("images/episode10/020_normal.webp") with dissolve
    toby "Anda memecat saya?"
    if darlene_path:
        scene expression ("images/episode10/021_sad.webp") with dissolve
        darlene "Lihat, [toby!c]. Ini tidak seperti yang saya inginkan, tetapi setelah apa yang terjadi di sini tempo hari, saya tidak punya pilihan."
        scene expression ("images/episode10/021_normal.webp") with dissolve
        darlene "Yang saya minta hanyalah Anda menandatangani selembar kertas itu dan lupa tentang apa yang terjadi. Sebagai imbalannya Anda mendapatkan 15k."
        scene expression ("images/episode10/020_sad.webp") with dissolve
        toby "Anda pikir saya butuh uang untuk diam tentang itu?"
        scene expression ("images/episode10/021_normal.webp") with dissolve
        darlene "Aku sudah mengenalmu selama dua bulan sekarang dan sejujurnya, aku tidak berpikir kamu tipe pria yang merusak reputasi uangku. Tetapi dalam pengalaman saya, uang selalu menang."
        scene expression ("images/episode10/021_sad.webp") with dissolve
        darlene "Itulah mengapa saya lebih dari adil di sini. Jika Anda ingin terus bekerja di industri ini, saya benar -benar akan memberikan kata yang baik untuk Anda."
        scene expression ("images/episode10/020_normal.webp") with dissolve
        toby "Saya tidak menginginkannya dan saya tidak butuh uang Anda. Saya tidak menginginkan apa pun sebagai imbalan atas keheningan saya. Jika Anda ingin saya menandatangani sesuatu yang saya tidak akan merusak reputasi Anda atau mencoba memeras Anda demi uang, saya dengan senang hati akan menandatanganinya."
        scene expression ("images/episode10/021_surprised.webp") with dissolve
        darlene "Umm ..."
        scene expression ("images/episode10/020_normal.webp") with dissolve
        toby "Tapi saya tidak mau pergi. Saya suka pekerjaan ini dan saya suka bekerja untuk Anda. Saya memiliki lebih banyak lagi untuk dipelajari dari Anda."
        scene expression ("images/episode10/021_angry.webp") with dissolve
        darlene "Demi bercinta, [toby!c]! Mengapa Anda harus membuat ini rumit? Ambil saja uangnya dan lupakan semua itu!"
        scene expression ("images/episode10/020_angry.webp") with dissolve
        toby "Saya tidak menginginkan uang Anda."
        scene expression ("images/episode10/020_signing.webp") with dissolve
        toby "Di sana, saya menandatanganinya."
        scene expression ("images/episode10/020_normal.webp") with dissolve
        toby "Sekarang saya tidak bisa memberi tahu siapa pun tentang apa pun yang terjadi. Jika Anda ingin memecat saya, maka tembak saya. Tapi jangan berani -berani mencoba membeli keheningan saya dengan uang."
        scene expression ("images/episode10/021_sad.webp") with dissolve
        darlene "Mengapa Anda begitu keras kepala tentang ini? Anda akan membutuhkan uang sampai Anda menemukan pekerjaan baru."
        scene expression ("images/episode10/020_normal.webp") with dissolve
        toby "Anda mengajari saya bahwa kesabaran adalah bagian terpenting dari industri ini. Dan kadang -kadang Anda bekerja, bekerja, bekerja, dan hadiahnya masih di luar sana, tetapi Anda harus menunggu."
        scene expression ("images/episode10/020_smile.webp") with dissolve
        toby "Nah dalam hal ini, apartemen yang saya kerjakan masih ada di pasaran, jadi kami harus menunggu."
        scene expression ("images/episode10/021_normal.webp") with dissolve
        darlene "Sekarang Anda hanya bodoh! Aku akan memecatmu dan kamu tidak punya apa -apa."
        scene expression ("images/episode10/022.webp") with dissolve
        toby "Maka yang bisa saya katakan adalah bahwa itu menyenangkan bekerja untuk Anda."
        scene expression ("images/episode10/023.webp") with dissolve
        darlene "Tunggu, jangan pergi. Setidaknya izinkan saya menjelaskan mengapa saya harus membiarkan Anda pergi."
        scene expression ("images/episode10/024.webp") with dissolve
        darlene "Apa yang kami lakukan beberapa hari yang lain salah. Saya tidak pernah menipu Kat. Tetapi mulai sekarang setiap kali saya melihat Anda, saya akan ingat bahwa saya berselingkuh. Saya merasa bersalah."
        darlene "Dan bagian yang menakutkan bukanlah fakta bahwa saya memberi Anda blowjob, tetapi fakta yang saya inginkan, karena itulah cara kerja hal -hal itu."
        scene expression ("images/episode10/025_normal.webp") with dissolve
        toby "Anda terus menjelaskan kepada saya bagaimana obat -obatan itu bekerja, tetapi jika Anda tahu banyak, mengapa Anda menawarkannya kepada saya?"
        scene expression ("images/episode10/026_guilty.webp") with dissolve
        darlene "Saya tahu tentang obat -obatan karena kadang -kadang saya dan Kat menggunakannya untuk membumbui barang -barang di kamar tidur, tetapi saya tidak pernah tahu bahwa mereka membuat versi cokelat."
        scene expression ("images/episode10/025_normal.webp") with dissolve
        toby "Jadi begitu."
        scene expression ("images/episode10/026_normal.webp") with dissolve
        darlene "Ngomong -ngomong, seperti yang saya katakan, saya harus membiarkan Anda pergi karena saya tidak ingin menipu Katrina lagi."
        scene expression ("images/episode10/025_curious.webp") with dissolve
        toby "Saya pikir Anda harus membiarkan saya pergi karena saya mengingatkan Anda tentang apa yang kami lakukan?"
        scene expression ("images/episode10/026_guilty.webp") with dissolve
        darlene "Itu juga."
        scene expression ("images/episode10/026_normal.webp") with dissolve
        darlene "Lihat, itu rumit."
        scene expression ("images/episode10/026_angry.webp") with dissolve
        darlene "Kenapa kamu tidak hanya mengambil uang dan pergi? Mengapa Anda harus bertahan dan memainkan kartu pria yang baik?"
        scene expression ("images/episode10/025_laugh.webp") with dissolve
        toby "Karena, percaya atau tidak. Saya pria yang baik."
        scene expression ("images/episode10/026_smile.webp") with dissolve
        darlene "Anda, itu sebabnya saya tidak ingin membiarkan Anda pergi."
        scene expression ("images/episode10/025_normal.webp") with dissolve
        toby "Lalu jangan t."
        scene expression ("images/episode10/026_normal.webp") with dissolve
        darlene "Jika Anda berjanji kepada saya bahwa apa yang terjadi di hari lain tidak akan pernah terjadi lagi."
        scene expression ("images/episode10/025_laugh.webp") with dissolve
        toby "Selama Anda tidak menggunakan obat saya atau menyentak saya, saya akan menjadi anak yang baik."
        scene expression ("images/episode10/026_laugh.webp") with dissolve
        darlene "Ya, saya perlu menjelaskan tentang itu juga."
        scene expression ("images/episode10/025_smile.webp") with dissolve
        toby "Ya saya pikir itu akan menyenangkan."
        scene expression ("images/episode10/026_smile.webp") with dissolve
        darlene "Anda ingat bagaimana saya memberi tahu Anda bahwa kadang -kadang saya dan Kat menggunakannya untuk membumbui semuanya di kamar tidur? Yah, tidak hanya di kamar tidur."
        scene expression ("images/episode10/025_flirty.webp") with dissolve
        toby "Seseorang sedang nakal di kantor?"
        scene expression ("images/episode10/026_laugh.webp") with dissolve
        darlene "Jangan membuatnya terdengar sangat kotor, tapi ya. Saya membayar sewa untuk kantor ini sehingga saya dapat melakukan apa pun yang saya inginkan."
        scene expression ("images/episode10/025_laugh.webp") with dissolve
        toby "Kedengarannya adil."
        scene expression ("images/episode10/026_normal.webp") with dissolve
        darlene "Ngomong -ngomong, masalahnya adalah Anda muncul beberapa menit setelah dia pergi dan saya cukup banyak di bawah pengaruh, tetapi saya berjanji kepada Anda bahwa saya akan lebih berhati -hati mulai sekarang."
        scene expression ("images/episode10/026_sad.webp") with dissolve
        darlene "Dan jika saya melakukan hal seperti ini sekali lagi, Anda mengambil uang dan pergi."
        scene expression ("images/episode10/027.webp") with dissolve
        toby "Kesepakatan."
        label memory_33:


            scene expression ("images/episode10/028.webp") with dissolve

            toby "Ya Tuhan, kamu cantik!"
            scene expression ("images/episode10/029.webp") with dissolve
            darlene "Kamu benar -benar berpikir begitu?"
            toby "Ya."
            scene expression ("images/episode10/030.webp") with dissolve
            darlene "Apa yang kamu lakukan padaku, [toby!c]?"
            toby "Saya tidak melakukan apa -apa."
            scene expression ("images/episode10/031.webp") with dissolve
            darlene "Jadi ... sebelum kita mulai bekerja, kita perlu membuat beberapa aturan dasar di sini."
            scene expression ("images/episode10/032.webp") with dissolve
            darlene "Anda dan saya tidak akan menjadi apa -apa. Saya bos Anda, dan Anda tidak akan pernah melihat saya dengan cara yang lucu."
            scene expression ("images/episode10/033.webp") with dissolve
            toby "Dan Anda tidak akan pernah membuat saya obat sehingga Anda bisa mengisap penisku."
            scene expression ("images/episode10/034.webp") with dissolve
            darlene "Maksudmu ayam ini? Saya bahkan tidak akan menyentuhnya."
            show ep10_035
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode10/035.webp") with dissolve
            hide ep10_035
            toby "Dan kami tidak akan pernah mencium satu sama lain seperti ini lagi."
            scene expression ("images/episode10/036.webp") with dissolve
            darlene "Dan saya tidak akan pernah mencoba membuka pakaian Anda."
            scene expression ("images/episode10/037.webp") with dissolve
            toby "Saya juga."
            scene expression ("images/episode10/038.webp") with dissolve
            toby "Dan aku tidak akan pernah, maksudku tidak pernah, melepaskan bramu sehingga aku bisa melihat payudara kecilmu yang indah."
            scene expression ("images/episode10/039.webp") with dissolve
            darlene "Dan bahkan jika bra tidak terpasang, saya tidak akan pernah menurunkannya, seperti ini."
            scene expression ("images/episode10/040.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode10/041.webp") with dissolve:
                yalign 0.0
                linear 10.0 yalign 1.0

            darlene "Aku sangat menginginkanmu!"
            toby "Aku merasakanmu!"
            scene expression ("images/episode10/042.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            darlene "Ini adalah terakhir kali aku mengisap penismu!"

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
            toby "Tuhan ... Saya ingin lebih dari sekadar blowjob. Aku ingin bercinta denganmu."

            scene expression ("images/episode10/047.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            darlene "Bawa aku ke sini di atas meja."

            scene expression ("images/episode10/048.webp") with dissolve:
                xalign 1.0
                linear 10.0 xalign 0.0

            toby "Oh, percayalah, aku akan melakukannya."

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
            toby "Aku juga akan cum."
            darlene "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nPlease don't stop."
            toby "Saya tidak bisa menahannya lagi."
            darlene "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nDon't stop."
            toby "Saya akan cum di dalam diri Anda."
            darlene "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck... Cum inside then, but don't you dare stop."
            hide ep10_054

            scene expression ("images/episode10/055.webp") with dissolve:
                yalign 0.0
                linear 10.0 yalign 1.0

            toby "Saya cumming."
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
            darlene "Ya Tuhan, itu terasa sangat baik."
            toby "Tolong beritahu saya bahwa Anda tidak di bawah pengaruh barang itu?"
            darlene "Jangan khawatir. Saya tidak perlu obat apa pun untuk mengetahui bahwa saya membutuhkan Anda untuk mengacaukan otak saya."
            scene expression ("images/episode10/057.webp") with dissolve
            darlene "Ini adalah satu kali. Oke?"
            toby "Apa kamu yakin?"
            darlene "Kami memiliki pekerjaan yang harus dilakukan. Kita tidak bisa berhubungan seks di kantor seperti dua hewan. Kami memiliki tanggung jawab."
            toby "Oke kalau begitu. Lain kali saya akan mengajak Anda keluar terlebih dahulu dan kemudian kami akan melihat apa yang terjadi."
            scene expression ("images/episode10/058.webp") with dissolve
            darlene "Berpakaian dan kembali bekerja."
            $ unlockMemory(persistent.memory_33)
            $ renpy.end_replay()
    else:

        scene expression ("images/episode10/021_sad.webp") with dissolve
        darlene "Lihat [toby!c]. Bukannya aku mau, tapi aku merasa sangat aneh berada di sekitarmu, setelah aku meminta untuk memberimu blowjob."
        scene expression ("images/episode10/021_normal.webp") with dissolve
        darlene "Yang saya minta dari Anda hanyalah menandatangani selembar kertas itu dan lupa tentang itu dan sebagai imbalan Anda mendapatkan 15k."
        scene expression ("images/episode10/020_curious.webp") with dissolve
        toby "Anda pada dasarnya membayar saya untuk tetap diam, bukan untuk merusak reputasi Anda."
        scene expression ("images/episode10/021_sad.webp") with dissolve
        darlene "Mungkin."
        scene expression ("images/episode10/020_normal.webp") with dissolve
        toby "Lihat. Saya tidak butuh uang Anda untuk tetap diam. Anda telah melakukan banyak hal untuk saya. Saya tidak membutuhkan apa pun sebagai gantinya."
        scene expression ("images/episode10/020_signing.webp") with dissolve
        toby "Di Sini. Saya menandatangani ini dan saya tidak butuh uang Anda. Anda sangat memikirkan saya dan saya pikir Anda adalah bos terbaik yang bisa saya miliki."
        scene expression ("images/episode10/020_smile.webp") with dissolve
        toby "Saya telah tumbuh untuk merawat Anda, jadi saya tidak akan pernah melakukan apa pun untuk merusak reputasi Anda."
        scene expression ("images/episode10/021_surprised.webp") with dissolve
        darlene "Tapi saya mencoba ..."
        scene expression ("images/episode10/020_normal.webp") with dissolve
        toby "Tapi tidak ada ... tidak ada yang terjadi dan tidak ada yang mau. Saya mengerti Anda dibius dan itu bukan salah Anda, jadi saya tidak melihat kebutuhan untuk Anda harus membayar apa pun."
        scene expression ("images/episode10/021_sad.webp") with dissolve
        darlene "Terima kasih [toby!c]."
        scene expression ("images/episode10/020_smile.webp") with dissolve
        toby "Jangan khawatir. Jadi? Apa yang harus saya lakukan hari ini?"
        scene expression ("images/episode10/021_smile.webp") with dissolve
        darlene "Apa kamu yakin? 15K adalah banyak uang."
        scene expression ("images/episode10/020_normal.webp") with dissolve
        toby "Saya belum mendapatkannya. Saya akan menghasilkan lebih banyak lagi."
        scene expression ("images/episode10/021_laugh.webp") with dissolve
        darlene "Dalam hal ini, apa yang masih Anda lakukan di sini? Kembali bekerja."

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
        toby "Umm ... Saya punya pertanyaan aneh."
        scene expression ("images/episode10/066.webp") with dissolve
        darlene "Oke?"
        scene expression ("images/episode10/065_2.webp") with dissolve
        toby "Apakah Anda kebetulan memiliki lebih banyak cokelat?"
        scene expression ("images/episode10/067.webp") with dissolve
        darlene "Sudah kubilang sayang. Itu adalah satu kali."
        scene expression ("images/episode10/065_2.webp") with dissolve
        toby "A girl told me that she wants to try this drug called \"The Hooker\", yang menurut deskripsinya terdengar seperti cokelat yang kami miliki beberapa hari yang lalu dan saya mengatakan kepadanya bahwa saya akan mencoba mendapatkannya."
        scene expression ("images/episode10/067.webp") with dissolve
        darlene "Sungguh kuda betina. Apakah saya tidak cukup untuk Anda?"
        scene expression ("images/episode10/068.webp") with dissolve
        toby "Anda mengatakannya sendiri. Itu adalah satu kali, jadi ..."
        scene expression ("images/episode10/066.webp") with dissolve
        darlene "Biarkan saya menelepon Kat!"
    else:
        toby "Maaf mengganggu Anda, saya punya pertanyaan aneh."
        scene expression ("images/episode10/066.webp") with dissolve
        darlene "Apakah semuanya baik -baik saja?"
        scene expression ("images/episode10/065_2.webp") with dissolve
        toby "A friend of mine told me about this drug called \"The Hooker\", Mana yang sangat mirip dengan yang Anda ceritakan dan saya bertanya -tanya apakah ada yang tersisa?"
        scene expression ("images/episode10/066.webp") with dissolve
        darlene "Maaf sayang, tapi saya membuang kotak, tetapi jika Anda mau, saya bisa menelepon Kat."
        scene expression ("images/episode10/065_2.webp") with dissolve
        toby "Jika tidak terlalu banyak."
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
    darlene "Dia menunggumu di klubnya. Saya akan mengirimkan alamatnya."
    scene expression ("images/episode10/071.webp") with dissolve
    toby "Tahukah Anda berapa banyak untuk sebuah kotak?"
    scene expression ("images/episode10/070.webp") with dissolve
    darlene "Ya, saya lakukan, tetapi untuk Anda ada di rumah."
    scene expression ("images/episode10/071.webp") with dissolve
    toby "Anda tidak harus melakukannya."
    scene expression ("images/episode10/070.webp") with dissolve
    darlene "Jangan khawatir. Tidak apa -apa."
    darlene "Ngomong -ngomong, jika dia bertanya kepada Anda bagaimana Anda tahu tentang cokelat yang Anda katakan kepadanya bahwa saya sedang memakan hadiahnya dan memberi tahu Anda tentang betapa kerennya cokelat ini."
    darlene "Apa pun yang Anda lakukan, jangan memberi tahu dia tentang kami."
    scene expression ("images/episode10/071.webp") with dissolve
    toby "Oke. Terima kasih banyak."
    scene expression ("images/episode10/072.webp") with dissolve
    darlene "Jangan khawatir dan bersenang -senang malam ini."
    scene expression ("images/episode10/073.webp") with dissolve
    toby "Saya akan."
    scene expression ("images/episode10/074.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()


    scene expression ("images/episode10/075.webp") with dissolve
    bodyguard "Menurutmu kemana kamu pergi? Klub ditutup."
    toby "Saya harus mengambil sesuatu dari Katrina."
    bodyguard "Ini Mrs. Katrina dan dia tidak memberitahuku apa -apa tentang itu. Jadi kocok."
    toby "Lihatlah pria, tanyakan saja atasan Anda."
    bodyguard "Persetan ... saya punya perintah untuk tidak mengganggunya."
    toby "Bos saya baru saja berbicara dengannya beberapa menit yang lalu dan menyuruh saya datang ke sini dan mengambil sesuatu."
    bodyguard "Kurir tidak menggunakan pintu depan."
    bodyguard "Aku akan membawamu ke Mrs. Katrina, tetapi jika kamu berbohong padaku, maka aku akan memiliki bola di atas tongkat."
    scene expression ("images/episode10/076.webp") with dissolve
    toby "Apa yang kamu lakukan, kawan?"
    bodyguard "Memastikan Anda tidak punya senjata. Saya tidak mempercayai Anda."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I knew that Katrina was crazy, but she might be crazier than I thought.{/i}"
    scene expression ("images/episode10/077.webp") with fade
    bodyguard "Maaf ma \ 'am. Orang ini bilang kamu mengharapkannya."
    scene expression ("images/episode10/078.webp") with dissolve
    katrina "[toby!c]. Betapa aku merindukanmu! Maaf saya lupa memberi tahu Neal bahwa Anda akan datang."
    katrina "Anda bisa meninggalkan kami sekarang."
    scene expression ("images/episode10/079.webp") with dissolve
    neal "Ya ma \ 'am."
    scene expression ("images/episode10/080.webp") with dissolve
    katrina "Jadi? Kamu ingin bersenang -senang malam ini?"
    toby "Umm ... ya."
    scene expression ("images/episode10/081.webp") with dissolve
    katrina "Bagaimana Anda tahu apa yang dilakukan produk saya? Apakah Anda dan Darlene bersenang -senang?"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}\"My product\"? Apakah dia yang mengembangkan obat ini? {/i}"
    katrina "Hati-hati. Tanganku ada di penismu, jadi jika kamu berbohong padaku, aku akan menghancurkan kacang kecilmu."
    toby "Tidak ada ma \ 'am. Saya tidak menyentuh cokelat. Dia memakannya sendirian dan mulai memberi tahu saya bagaimana kalian berdua suka membumbui semuanya di kamar tidur, jadi saya ingin mencobanya."
    katrina "Apakah itu jawaban terakhir Anda?"
    toby "Ya."
    scene expression ("images/episode10/082.webp") with dissolve
    katrina "Jika Anda berbohong kepada saya, bersenang -senang malam ini, karena itu terakhir kali Anda akan menggunakan ayam Anda itu."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the hell have I gotten myself into?{/i}"
    scene expression ("images/episode10/083.webp") with dissolve
    katrina "Di Sini. Anda tidak tahu dari mana Anda mendapatkannya. Dipahami?"
    toby "Ya ma \ 'am."
    katrina "Dan jika saya jadi Anda, saya akan membiarkan pasangan Anda makan lebih banyak. Lebih keren untuk melihat seberapa putus asa dia untuk ayam Anda."
    toby "Ummm ... terima kasih."

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
    katrina "Burung bodoh!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This is bad. I never saw Katrina this mad. Lucky for me she's out of bullets.{/i}"
    scene expression ("images/episode10/097.webp") with dissolve
    katrina "Kapan kamu sampai di sini?"
    toby "Beberapa menit yang lalu."
    katrina "Dan mengapa Anda tidak mengatakan apa -apa."
    toby "Saya tidak ingin akhirnya beralih tempat dengan dinding itu."
    scene expression ("images/episode10/098.webp") with dissolve
    katrina "Anda lebih pintar dari yang Anda lihat."
    if katrina_path:
        label memory_34:


            scene expression ("images/episode10/099.webp") with dissolve
            katrina "Jadi? Anda di sini untuk meminta maaf?"
            toby "Tidak terlalu. Saya datang karena Anda meminta saya."
            scene expression ("images/episode10/100.webp") with dissolve
            katrina "Apakah itu jawaban terakhir Anda?"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fucking hell, the gun is so hot. She's going to burn my skin.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}At least she doesn't have any bullets left.{/i}"
            toby "Ya. Saya tidak akan meminta maaf atas sesuatu yang bukan salah saya. Jadi Anda meminta saya untuk datang dan saya datang. Apa yang terjadi?"
            scene expression ("images/episode10/101.webp") with dissolve
            katrina "Saya meminta Anda untuk datang ke sini, karena saya membutuhkan seseorang untuk menjilat bajingan saya dan saya pikir Anda mungkin ingin, karena Anda sangat menyukai vagina saya."
            katrina "Ini hanya beberapa inci. Pada dasarnya adalah pose yang sama."
            scene expression ("images/episode10/102.webp") with dissolve
            toby "Maaf, tetapi jika Anda benar -benar ingin merasakan air liur saya di pantat Anda, yang bisa saya lakukan hanyalah meludahkan pistol sialan ini dan kemudian Anda dapat mendorongnya ke atas pantat Anda."
            scene expression ("images/episode10/103.webp") with dissolve
            katrina "Buka mulutmu."
            scene expression ("images/episode10/104.webp") with dissolve
            katrina "Anda berkata?"
            toby "Saya bilang mendorong pistol Anda di pantat Anda."
            katrina "Motherfucker yang cermat. Saya sangat dekat dengan menembakkan otak Anda."
            toby "Lalu menembak!"
            scene expression ("images/episode10/105.webp") with dissolve
            toby "Anda hanya menarik hal ini dan selesai."
            katrina "Anda di atas es tipis di sini nak, jangan membuat saya, karena saya akan menembak Anda."
            scene expression ("images/episode10/106.webp") with dissolve
            toby "Kucing menakut -nakuti apa yang salah?"
            toby "Anda tidak ingin menembak saya? Kamu sangat menyukaiku?"
            katrina "Anda tidak tahu apa yang saya inginkan."
            toby "Percayalah, saya lakukan."
            scene expression ("images/episode10/107.webp") with dissolve
            katrina "Apa yang saya inginkan?"
            toby "Anda ingin saya mengendalikan Anda!"
            scene expression ("images/episode10/108.webp") with dissolve
            katrina "Kiddo. Ini adalah kehidupan nyata, bukan game porno bodoh yang Anda mainkan."

            show ep10_109
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode10/109.webp") with dissolve
            hide ep10_109
            toby "Sayang apa yang salah? Saya pikir Anda tidak menginginkan ini."
            scene expression ("images/episode10/110.webp") with dissolve
            katrina "Yang saya inginkan adalah untuk meminta maaf."
            toby "Sungguh kebetulan. Saya juga menunggu Anda untuk meminta maaf dan mungkin meledakkan saya."
            toby "Kamu tahu? Hanya untuk meremehkan hal -hal."
            scene expression ("images/episode10/111.webp") with dissolve
            katrina "Sebelum atau sesudah saya menembak ayam Anda?"
            toby "Bagaimana dengan keduanya."
            scene expression ("images/episode10/112.webp") with dissolve
            katrina "Jatuhkan celana Anda."
            toby "Saya tahu Anda tidak bisa menahan saya."
            scene expression ("images/episode10/113.webp") with dissolve
            katrina "Saya tidak ingin merindukan ayam kecil Anda."
            toby "Ayam kecil? Saya ragu Anda bisa memasukkannya ke dalam mulut Anda."
            katrina "Percayalah, aku bisa!"
            scene expression ("images/episode10/114.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0
            toby "Kemudian sialan membuktikannya."

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
            toby "Itu sayang. Jadilah pelacur yang baik dan payah ayam itu."

            scene expression ("images/episode10/117.webp") with dissolve
            show ep10_117
            $ ui.saybehavior()
            $ ui.interact()
            toby "Jika saya tidak tahu lebih baik, saya akan mengatakan Anda mengisap ayam untuk mencari nafkah."
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\n{i}MmmOTHERmmmFUCKmmmER!{/i}"
            hide ep10_117

            show ep10_120
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode10/120.webp") with dissolve
            hide ep10_120
            toby "Tidakkah Anda tahu tidak sopan untuk berbicara dengan mulut penuh?"
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\n{i}You're so gonna pay for this.{/i}"

            scene expression ("images/episode10/118.webp") with dissolve
            show ep10_118
            toby "Saya tahu, saya tahu. Saya sudah membayar. Melihat betapa Anda suka mengisap ayam, saya mengatakan saya ingin membantu Anda."
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
            toby "Kemarilah pelacur kecil. Saya ingin mengisi vagina Anda."

            scene expression ("images/episode10/122_1.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0
            katrina "Persetan denganku, [toby!c]."

            scene expression ("images/episode10/122_2.webp") with dissolve:
                xalign 0.0
                yalign 0.0
                linear 10.0 yalign 0.8 xalign 1.0
            toby "Berbalik. Aku menidurimu dari belakang seperti pelacur kecil itu."

            scene expression ("images/episode10/123.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0
            katrina "Apakah saya seorang pelacur?"

            scene expression ("images/episode10/124.webp") with dissolve
            show ep10_124
            toby "Anda adalah pelacur terbesar!"
            katrina "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes... Yes. I'm a slut."
            toby "Apakah Anda pelacur saya?"
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
            toby "Anda suka pelacur penis saya?"
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYES. I love it."
            toby "Apakah lebih baik dari mainan apa pun yang Anda gunakan?"
            katrina "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nFuck yes."
            hide ep10_128

            scene expression ("images/episode10/129.webp") with dissolve
            show ep10_129
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI'm going to cum."
            toby "Saya dekat."
            katrina "Jangan berani -berani dalam diri saya. Aku berjanji akan membunuhmu."
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's seems serious. I think this is a good time to listen to her.{/i}"
            katrina "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nYES... YES... YESSS."
            hide ep10_129

            scene expression ("images/episode10/130.webp") with dissolve
            play sound "audio/fx/Knocking-on-door-five-knocks-www.fesliyanstudios.com.mp3"
            "{i}*Knock, Knock*{/i}"
            neal "Maaf Ma, tapi Tuan Wood ada di sini. Dia mengatakan itu sesuatu yang mendesak."
            scene expression ("images/episode10/131.webp") with dissolve
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nDo not come inside."
            scene expression ("images/episode10/130.webp") with dissolve
            neal "Apa? Anda berkata untuk masuk?"
            scene expression ("images/episode10/132.webp") with dissolve
            neal "Oke."
            scene expression ("images/episode10/133.webp") with dissolve
            $ unlockImage(persistent.katrina_07)
            play sound "audio/fx/gunshot.mp3"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, I'm coming.{/i}"
            with flash
            with flash
            katrina "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nI SAID \"DON'T FUCKING COME INSIDE\"."
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}How the fuck was she able to fire that gun? I didn't think she had any bullets left.{/i}"

            scene expression ("images/episode10/134.webp") with dissolve
            katrina "Sialan kamu masuk ke dalam?"
            $ unlockMemory(persistent.memory_34)
            $ renpy.end_replay()

        scene expression ("images/episode10/135.webp") with dissolve
        katrina "Keluar dari sini, sebelum aku membunuhmu."
        toby "Haruskah saya pulang?"
        scene expression ("images/episode10/136.webp") with dissolve
        katrina "Tidak ... tunggu saya di klub, kami masih memiliki bisnis untuk didiskusikan."
    else:

        scene expression ("images/episode10/099.webp") with dissolve
        katrina "Jadi? Bagaimana karyawan favorit saya?"
        katrina "Apakah Anda berubah pikiran dan datang untuk menjilat vagina saya?"
        toby "Tidak."
        scene expression ("images/episode10/100.webp") with dissolve
        katrina "Apa kamu yakin?"
        toby "Ya ma \ 'am."
        katrina "Sial, kamu sangat membosankan."
        scene expression ("images/episode10/130.webp") with dissolve
        "{i} Knock, knock. {/i}"
        play sound "audio/fx/Knocking-on-door-five-knocks-www.fesliyanstudios.com.mp3"
        neal "Maaf Ma, tapi Tuan Wood ada di sini. Dia mengatakan itu sesuatu yang mendesak."
        scene expression ("images/episode10/100.webp") with dissolve
        katrina "Anda pergi menunggu saya di klub. Saya sudah mendapatkan beberapa bisnis untuk diurus."
        toby "Ya ma \ 'am."

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
    katrina "Ini dia."
    if katrina_path:
        scene expression ("images/episode10/139.webp") with dissolve
        katrina "Bisnis dulu, jadi bawa ini ke Kayla."
        scene expression ("images/episode10/140.webp") with dissolve
        katrina "Sekarang tangan Anda sibuk. Kenapa aku masih merasakan air mani di dalam vaginaku."
        scene expression ("images/episode10/141.webp") with dissolve
        toby "Karena Anda belum membersihkan diri sendiri?"
        scene expression ("images/episode10/140_2.webp") with dissolve
        katrina "Anda mendapat satu kesempatan lagi dan kemudian saya akan menembak. Kali ini saya benar -benar tidak peduli, saya hanya harus mengambil paket itu sendiri. Jadi?"
        scene expression ("images/episode10/142.webp") with dissolve
        toby "Karena kamu sangat membuatku takut saat menembak. Saya tidak mengharapkan Anda untuk benar -benar menembak."
        scene expression ("images/episode10/140_2.webp") with dissolve
        katrina "Mengapa Anda tidak berharap untuk saya menembak ketika saya menunjuk senjata?"
        scene expression ("images/episode10/142.webp") with dissolve
        toby "Karena Anda seharusnya kehabisan peluru."
        scene expression ("images/episode10/143.webp") with dissolve
        katrina "Sialan ... Anda pikir saya kehabisan peluru? Itu sebabnya Anda sangat tangguh di belakang sana? Karena kamu yakin aku tidak akan membunuhmu?"
        katrina "Pistol ini terkadang misfires. Ini cukup rusak, tetapi memiliki nilai sentimental. Itu adalah pistol pertama saya."
        scene expression ("images/episode10/144.webp") with dissolve
        katrina "Jadi lain kali Anda menjadi pintar, cobalah untuk menjadi lebih pintar, karena Anda sedekat ini dari menjadi sejarah."
        scene expression ("images/episode10/145.webp") with dissolve
        katrina "Beruntung bagi Anda, seks itu bagus, tapi itu satu kali, mulai sekarang Anda hanya bisa menjilat vagina atau pantat saya. Anda memilih."
        scene expression ("images/episode10/146_1.webp") with dissolve
        katrina "Sekarang, potong, potong. Kayla sedang menunggu paket ini."
        scene expression ("images/episode10/146_2.webp") with dissolve
        toby "Umm ... saya agak punya satu permintaan. Apakah Anda pikir mungkin bagi saya untuk mendapatkan satu kotak cokelat untuk tujuan rekreasi?"
        scene expression ("images/episode10/146_3.webp") with dissolve
        katrina "Bantu diri Anda dari kotak."
        scene expression ("images/episode10/146_2.webp") with dissolve
        toby "Terima kasih, ma \ 'am."
    else:
        scene expression ("images/episode10/139.webp") with dissolve
        katrina "Bawa kotak ini ke Kayla. Dia menunggumu."
        toby "Oke ma \ 'am."
        scene expression ("images/episode10/146_2.webp") with dissolve
        toby "Saya punya satu pertanyaan. Apakah Anda pikir mungkin bagi saya untuk mendapatkan sekotak cokelat untuk tujuan rekreasi?"
        scene expression ("images/episode10/146_3.webp") with dissolve
        katrina "Bantu diri Anda dari kotak."
        scene expression ("images/episode10/146_2.webp") with dissolve
        toby "Terima kasih, ma \ 'am."

    scene expression ("images/episode10/148.webp") with dissolve
    katrina "Sampai jumpa."

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
        toby "Apa yang kamu lakukan, [sis]?"
    else:
        toby "Apa yang kamu lakukan? Beginilah cara Anda membersihkan kamar saya?"
    scene expression ("images/episode10/155.webp") with dissolve
    patricia "Apakah Anda benar -benar percaya apa yang dikatakan buku ini?"
    toby "Anda tidak setuju dengan itu?"
    patricia "Tidak. Ini penuh omong kosong."
    scene expression ("images/episode10/156_curious.webp") with dissolve
    toby "Apa yang membuatmu mengatakan itu?"
    scene expression ("images/episode10/157_reading.webp") with dissolve
    patricia "\"Tentu saja, kalau dia mengelus lututmu, tak perlu bertanya lebih lanjut. Tapi kalau dia mengelus lututnya, mungkin ini keinginan bawah sadar untuk mengelus lututmu.\"
    scene expression ("images/episode10/157_curious.webp") with dissolve
    patricia "Benar-benar? Apakah ada gadis yang Anda kencani pernah membelai lutut Anda?"
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "Tidak juga, tapi saya tidak tahu. Mungkin dia menyentuh lututnya."
    scene expression ("images/episode10/157_laugh.webp") with dissolve
    if emma_break:
        patricia "Kami berdua tahu Anda hanya berkencan dengan pelacur, jadi jika mereka menyentuh lutut mereka, itu mungkin karena mereka sakit karena terlalu banyak menunjukkan kasih sayang."
    else:
        patricia "Jika Anda berbicara tentang Emma, jika dia menyentuh lututnya, itu mungkin karena mereka sakit karena terlalu banyak menunjukkan kasih sayang."
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "Anda sedang menyebalkan sekarang. Anda tahu itu, kan?"
    scene expression ("images/episode10/157_laugh.webp") with dissolve
    patricia "Namun saya tidak merasakan kebutuhan untuk menggaruk lutut saya."
    scene expression ("images/episode10/157_normal.webp") with dissolve
    patricia "Jadi siapa pun yang menjual buku ini kepada Anda, dia mengacaukan Anda."
    scene expression ("images/episode10/156_book.webp") with dissolve
    toby "Beri aku bukunya."
    scene expression ("images/episode10/157_laugh.webp") with dissolve
    patricia "Izinkan saya membacakan Anda satu lagi."
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "Aku tahu. Saya sudah membaca bagian itu."
    scene expression ("images/episode10/157_reading.webp") with dissolve
    patricia "Lalu mari kita membaca sesuatu dari akhir. Saya akan merusak buku untuk Anda."
    patricia "\"When a woman suddenly blinks faster, you may have increased her level of sexual excitement\"."
    patricia "\"You might notice a sudden rapid eye blink when you tell an amazing story of you being a cool/exciting/funny guy. This is a subliminal way of saying, “You’ve captured my interest.”\"."
    scene expression ("images/episode10/156_book.webp") with dissolve
    toby "Beri aku bukunya."
    scene expression ("images/episode10/158.webp") with dissolve
    patricia "Tapi ... saya masih ingin membacanya, besar [brother]. Tidak bisakah Anda melihat betapa tertariknya saya di buku Anda."
    show ep10_158
    toby "Saya melihat apa yang Anda coba lakukan, tetapi tidak berfungsi."
    hide ep10_158
    scene expression ("images/episode10/157_cool.webp") with dissolve
    patricia "Maksud saya persis. Buku ini penuh dengan omong kosong. Jika Anda ingin tahu apa yang dipikirkan gadis, Anda dapat bertanya kepada saya. Saya sudah menjadi gadis untuk seluruh hidup saya, jadi saya pikir saya tahu lebih banyak tentang bagaimana wanita berpikir daripada cinta Dr. yang menulis buku ini."
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "Dan mengapa Anda membantu saya?"
    scene expression ("images/episode10/157_smile.webp") with dissolve
    patricia "Because I'm your [sister] and I want the best for you. This way I also get to filter your bimbos. If I don't like a girl I'll give you crappy advice, like \"If she's touching her hair, she actually wants you to touch it\"."
    scene expression ("images/episode10/156_laugh.webp") with dissolve
    toby "Dan apa yang bisa Anda lakukan?"
    scene expression ("images/episode10/157_smile.webp") with dissolve
    patricia "Apa maksudmu, apa yang akanku lakukan? Saya tidak butuh apapun. Menurut Anda, seperti apa saya?"
    scene expression ("images/episode10/157_laugh.webp") with dissolve
    patricia "Aku baru saja memberitahumu, aku melakukan ini karena aku mencintaimu, tetapi jika kamu bersedia membelikanku hadiah atau memberiku uang, siapa aku untuk mengatakan tidak untuk itu?"
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "Saya sudah membayar Anda membersihkan kamar saya dan dengan kelihatannya, Anda tidak melakukan pekerjaan yang sangat baik, karena alih -alih membuat tempat tidur saya, Anda mengacaukannya dengan duduk di dalamnya."
    scene expression ("images/episode10/157_cool.webp") with dissolve
    patricia "Anda memanggil pembayaran itu? Pernahkah Anda melihat bagaimana kamar Anda terlihat di pagi hari setelah Anda pergi?"
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "Bisa aja. Ini tidak seburuk itu."
    scene expression ("images/episode10/157_laugh.webp") with dissolve
    patricia "Ini juga tidak bagus, jadi saya pikir 0 agak murah untuk semua pekerjaan yang saya lakukan."
    scene expression ("images/episode10/156_flirty.webp") with dissolve
    toby "Jika Anda menginginkan lebih, Anda tahu apa yang harus dilakukan."
    scene expression ("images/episode10/157_normal.webp") with dissolve
    patricia "Saya sebenarnya butuh uang. Aku keluar dengan Bea malam ini dan aku benar -benar bisa menggunakannya."
    scene expression ("images/episode10/156_laugh.webp") with dissolve
    toby "Anda tahu apa yang harus dilakukan?"
    scene expression ("images/episode10/157_pouty.webp") with dissolve
    patricia "Bisakah Anda menjadi baik [brother] untuk sekali?"
    scene expression ("images/episode10/156_smile.webp") with dissolve
    toby "Bagus. Saya akan menyesuaikan harga."
    scene expression ("images/episode10/157_surprised.webp") with dissolve
    patricia "Benar-benar?"
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "Tentu saja. Apa yang tidak akan saya lakukan untuk kecil [sister]?"
    scene expression ("images/episode10/156_laugh.webp") with dissolve
    toby "Jadi, 6 jika Anda membersihkan kamar saya di pakaian Anda, 1 jika Anda melakukannya dalam gaun ini, 01 di pakaian dalam dan 02 jika Anda melakukannya telanjang."
    scene expression ("images/episode10/157_meh.webp") with dissolve
    patricia "Anda baru saja menambahkan ke masing -masing."
    scene expression ("images/episode10/156_laugh.webp") with dissolve
    toby "Tidak benar. Saya menambahkan $ 2 di tingkat terakhir."
    scene expression ("images/episode10/157_laugh.webp") with dissolve
    patricia "Bodoh aku. Saya hampir lupa seberapa banyak yang dapat Anda lakukan dengan $ $."
    scene expression ("images/episode10/156_smile.webp") with dissolve
    toby "Ada negara -negara di mana Anda dapat membeli rumah dengan $ 2."
    scene expression ("images/episode10/156_normal.webp") with dissolve
    toby "Atau tenda."
    scene expression ("images/episode10/157_smile.webp") with dissolve
    patricia "Jadi $ 101 jika saya membersihkan kamar Anda di pakaian dalam saya?"
    scene expression ("images/episode10/156_flirty.webp") with dissolve
    toby "Anda sedang mempertimbangkannya?"
    scene expression ("images/episode10/157_laugh.webp") with dissolve
    patricia "Tidak. Tapi saya suka wajah yang Anda buat ketika Anda berpikir semuanya berjalan sesuai keinginan Anda."
    scene expression ("images/episode10/159.webp") with dissolve
    if sheila_path:
        toby "Yah, saya ingin tetap dan mengobrol, tapi saya harus bersiap untuk kencan malam ini, karena percaya atau tidak, buku itu melakukan keajaiban."
        scene expression ("images/episode10/160.webp") with dissolve
        patricia "Saya yakin itu hanyalah bimbo lain."
        scene expression ("images/episode10/159.webp") with dissolve
        toby "Bimbo atau tidak, malam ini aku berhubungan seks, sementara kamu pergi dengan Bea berbicara tentang anak nakal seperti aku."
        scene expression ("images/episode10/162.webp") with dissolve
        patricia "Atau mungkin kita akan berhubungan seks juga. Mungkin saya lesbian sekarang."
        scene expression ("images/episode10/163.webp") with dissolve
        toby "Beri tahu saya bagaimana kelanjutannya."
    else:
        toby "Yah, saya ingin tinggal dan mengobrol, tapi saya harus mandi, karena saya perlu bertemu dengan seorang gadis."
        scene expression ("images/episode10/161.webp") with dissolve
        patricia "Jangan beri tahu saya buku ini benar -benar berfungsi."
        scene expression ("images/episode10/159.webp") with dissolve
        toby "Mungkin itu terjadi, tapi aku tidak berkencan dengannya. Saya hanya harus memberinya sesuatu."
        scene expression ("images/episode10/161.webp") with dissolve
        patricia "Sudah kubilang, buku ini penuh dengan omong kosong."
        scene expression ("images/episode10/163.webp") with dissolve
        toby "Nah, karena saya membayarnya, saya berencana untuk menyelesaikannya."

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
    toby "Apa yang masih kamu lakukan di sini?"
    scene expression ("images/episode10/173.webp") with dissolve
    patricia "Menunggu pembayaran saya."
    scene expression ("images/episode10/172.webp") with dissolve
    toby "Oh, benar."
    scene expression ("images/episode10/174.webp") with dissolve
    toby "Di sini kamu 0."
    scene expression ("images/episode10/175.webp") with dissolve
    patricia "Anda kehilangan beberapa."
    scene expression ("images/episode10/176.webp") with dissolve
    toby "Oh, benar. Burukku. Di sini satu lagi."
    scene expression ("images/episode10/175_1.webp") with dissolve
    patricia "Umm ... sudahkah Anda memeriksa ponsel Anda?"
    toby "Tidak Memangnya kenapa?"
    patricia "Nah, saya sebenarnya 51 pendek."
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
    patricia "Jadi? Bagaimana menurutmu? Apakah saya pendek atau tidak?"
    toby "Mungkin, tapi hanya 0, bukan 51 seperti yang Anda katakan."
    patricia "Oh ... mungkin masih ada lagi."
    toby "Ada lagi?"
    patricia "Mungkin."
    scene expression ("images/episode10/177_texting.webp") with dissolve
    call sms_incoming ("tris", "Ummm. Changed my mind. Since you're still in bathroom and won't be able to see me like this.", img_icon="images/episode10/180_icon.webp", img="images/episode10/180.webp") from _call_sms_incoming_203
    scene expression ("images/episode10/177.webp") with dissolve
    hide screen message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Damn. Tris is messing with me. I need to change the rules of this game. She won't be allowed to clean my room when I'm not around.{/i}"
    scene expression ("images/episode10/179.webp") with dissolve
    patricia "Dengan raut wajah Anda, saya mengatakan Anda setuju bahwa saya pendek."
    toby "Kita perlu membicarakan hal ini. Mulai sekarang Anda tidak diizinkan membersihkan kamar saya kecuali saya hadir."
    scene expression ("images/episode10/181.webp") with dissolve
    patricia "Kami akan membicarakannya nanti. Saat ini saya akan membutuhkan 51 itu, karena saya berencana untuk bersenang -senang malam ini."
    scene expression ("images/episode10/182.webp") with dissolve
    toby "Ini uangnya, tetapi mulai sekarang saya perlu melihat Anda membersihkan kamar saya secara langsung"
    patricia "Saya tahu Anda mengatakan itu, itulah mengapa saya mengirimi Anda foto, konyol."
    scene expression ("images/episode10/183.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode10/184.webp") with dissolve
    patricia "{size=12}{color=#FDCA6E}* softly speaking *{/color}{/size}\n{i}Pleasure doing business with you.{/i}"
    scene expression ("images/episode10/185.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode10/186.webp") with dissolve
    patricia "Oopsies. Anda menjatuhkan handuk Anda."
    scene expression ("images/episode10/187.webp") with dissolve
    patricia "Anda sakit [bro]. Anda mendapat boner dari menonton [sister] Anda melakukan tugas telanjang."
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

        toby "Ya Tuhan, kamu cantik."
        sheila "Terima kasih!"
        sheila "Haruskah kita?"
        toby "Ya, kami akan."

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
        sheila "Jadi Anda mengatakan kepada saya bahwa jika Anda memenangkan satu juta dolar, Anda tidak akan menghabiskan uang receh selama seminggu?"
        toby "Ya. Persis seperti apa yang saya katakan."
        scene expression ("images/episode10/199_curious.webp") with dissolve
        sheila "Tapi kenapa?"
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "Dengan baik. Satu juta dolar mungkin tampak seperti banyak pada awalnya, tetapi begitu Anda mulai menghabiskannya, itu tidak terlihat begitu banyak."
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "Tapi itu masih satu juta dolar."
        scene expression ("images/episode10/200_smile.webp") with dissolve
        toby "Ya, tapi Anda memenangkan uang itu. Anda tidak mendapatkannya, jadi meskipun Anda tahu nilai uang sekarang, ketika Anda memenangkannya, Anda akan berpikir Anda bisa mendapatkan lebih banyak jutaan seperti itu, jadi Anda cenderung membelanjakannya untuk hal -hal bodoh."
        scene expression ("images/episode10/199_normal.webp") with dissolve
        sheila "Itu cara berpikir yang menarik, tapi saya masih tidak mendapatkan mengapa menunggu pada minggu dan kemudian menghabiskannya?"
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "Karena setelah seminggu, Anda punya cukup waktu untuk memikirkan apa yang sebenarnya Anda butuhkan, karena jika saya memenangkan satu juta dolar tepat pada saat ini, dan saya tidak akan berhati -hati, dan pada pagi hari saya memiliki kurang dari 100 ribu tersisa."
        scene expression ("images/episode10/199_laugh.webp") with dissolve
        sheila "Jika Anda ingin menunggu seminggu, itu.Sekarang kita akan mendapatkan suatu tempat. Katakanlah Anda menang satu juta dolar sekarang dan Anda memiliki sampai pagi untuk menghabiskan semuanya. Jika Anda melakukannya, Anda akan memenangkan satu juta lagi yang dapat Anda lakukan apa pun yang Anda inginkan."
        scene expression ("images/episode10/200_flirty.webp") with dissolve
        toby "Nah, dalam hal ini, saya akan membelikan Anda kalung berlian, anting -anting dan gelang."
        scene expression ("images/episode10/199_flirty.webp") with dissolve
        sheila "Jadi Anda mengatakan kepada saya bahwa hal pertama yang Anda lakukan adalah membelikan saya sesuatu yang baik?"
        scene expression ("images/episode10/200_smile.webp") with dissolve
        toby "Tentu. Mengapa tidak? Lagi pula, saya masih ingin bersenang -senang malam ini."
        scene expression ("images/episode10/199_laugh.webp") with dissolve
        sheila "Anda pikir saya akan berhubungan seks dengan Anda malam ini jika Anda tidak akan membelikan saya barang -barang bagus? Apakah saya terlihat seperti penggali emas bagi Anda?"
        scene expression ("images/episode10/200_normal.webp") with dissolve
        toby "Apa yang saya katakan dan apa yang dia dengar. Saya baru saja memberi tahu Anda bahwa hal pertama yang saya lakukan adalah membelikan Anda barang -barang bagus. Tidak membelikan saya yang rolls-royce phantom yang saya impikan."
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "Jadi Anda akan membelikan saya 15k perhiasan saat Anda mendapatkan mobil 500k?"
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "Lagipula aku yang memenangkan uang. Saya tidak ingat mendengar Anda mengatakan kepada saya bahwa Anda akan membelikan saya sesuatu yang baik jika Anda memenangkan satu juta dolar."
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "Hai. Bukan itu cara kerja permainan. Saya adalah korban di sini."
        scene expression ("images/episode10/200_smile.webp") with dissolve
        toby "Biarkan tempat beralih untuk saat ini."
        scene expression ("images/episode10/200_curious.webp") with dissolve
        toby "Apa yang akan Anda lakukan jika Anda memenangkan satu juta dolar."
        scene expression ("images/episode10/199_curious.webp") with dissolve
        sheila "Hmm ... aku membelahnya dalam 3. Dengan sepertiga uang aku akan membawamu berbelanja."
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "Itu omong kosong. Saya tidak percaya Anda akan membelikan saya hadiah senilai 330k."
        scene expression ("images/episode10/199_laugh.webp") with dissolve
        sheila "Siapa yang mengatakan sesuatu tentang saya membelikan Anda barang? Saya membutuhkan seseorang untuk membantu saya dengan tas. Saya membeli pakaian desainer."
        scene expression ("images/episode10/200_normal.webp") with dissolve
        toby "Dan Anda mengeluh tentang saya."
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "Anda seorang pria. Dalam masyarakat kita, Anda seharusnya membelikan saya barang -barang, bukan sebaliknya."
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "Itu standar ganda."
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "Ganda atau tidak, saya masih berharap Anda membelikan saya sesuatu bahkan jika saya menang satu juta dolar."
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "Ya ... dan saya orang jahat di sini."
        scene expression ("images/episode10/199_laugh.webp") with dissolve
        sheila "Tunggu. Anda tidak mendengar apa yang akan saya lakukan dengan yang lain."
        scene expression ("images/episode10/200_curious.webp") with dissolve
        toby "Kejutan saya."
        scene expression ("images/episode10/199_thinking.webp") with dissolve
        sheila "Nah, dengan sepertiga dari uang itu saya akan membeli rumah yang bagus di pinggiran kota, karena saya membenci kota."
        scene expression ("images/episode10/200_normal.webp") with dissolve
        toby "Mengapa Anda membencinya?"
        scene expression ("images/episode10/199_normal.webp") with dissolve
        sheila "Karena tidak aman. Mungkin Anda tidak memperhatikan karena Anda seorang pria, tetapi untuk seorang gadis itu bukan tempat yang aman. Tingkat kejahatan sangat besar."
        if toby_job == 0:
            scene expression ("images/episode10/200_sad.webp") with dissolve
            toby "Saya tidak pernah memikirkannya. Saya sudah terbiasa."
            scene expression ("images/episode10/199_sad.webp") with dissolve
            sheila "Ya. Ini bukan tempat yang bagus."
        else:
            scene expression ("images/episode10/200_normal.webp") with dissolve
            toby "Itu tidak bisa seburuk itu."
            scene expression ("images/episode10/199_normal.webp") with dissolve
            sheila "Itu karena Anda bekerja di tempat yang gila dan terbiasa dengan orang gila. Saya yakin bahwa jika saya akan mengeluarkan pistol dari dompet saya sekarang, Anda tidak akan tersentak."
            scene expression ("images/episode10/200_curious.webp") with dissolve
            toby "Anda memiliki senjata pada Anda?"
            scene expression ("images/episode10/199_laugh.webp") with dissolve
            sheila "Saya bahkan tidak punya dompet, di mana saya akan menyimpan pistol saya?"
            scene expression ("images/episode10/200_normal.webp") with dissolve
            toby "Pistol saya? Kamu punya satu?"
            scene expression ("images/episode10/199_awkward.webp") with dissolve
            sheila "Umm ... Tidak. Mengapa saya memilikinya?"


        scene expression ("images/episode10/199_normal.webp") with dissolve
        sheila "Bagaimanapun, dengan bagian terakhir dari uang saya akan membeli lambo."
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "Itu mobil yang jelek."
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "Mungkin Anda berpikir begitu, karena Anda adalah jiwa lama dan mobil impian Anda adalah Rolls-Royce."
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "Saya bukan jiwa tua."
        scene expression ("images/episode10/199_impersonate.webp") with dissolve
        sheila "{size=12}{color=#FDCA6E}* mocking *{/color}{/size}\n{i}\"If I'd win one million dollars, I wouldn't touch it for a week.\"{/i}"
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "Saya tidak terdengar seperti itu."
        scene expression ("images/episode10/199_normal.webp") with dissolve
        sheila "Kecuali kamu."
        scene expression ("images/episode10/200_normal.webp") with dissolve
        toby "Itu tidak membuat saya menjadi jiwa lama, tetapi Penny bijak, tidak seperti Anda, pemboros besar."
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "Saya bukan pemboros besar."
        scene expression ("images/episode10/200_impersonate.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* mocking *{/color}{/size}\n{i}\"I'm going to buy designer clothes and a Lambo. A pink one with fuzzy seats.\"{/i}"
        scene expression ("images/episode10/199_laugh.webp") with dissolve
        sheila "Ewww ... Pink Lambo. TIDAK..."
        scene expression ("images/episode10/200_laugh.webp") with dissolve
        toby "Hitam dengan kursi kabur?"
        scene expression ("images/episode10/199_normal.webp") with dissolve
        sheila "Tidak ada kursi fuzzy."
        scene expression ("images/episode10/201.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode10/199_normal.webp") with dissolve
        sheila "Sebenarnya saya akan menghabiskan semua uang untuk menemukan dan menyimpan [sister] saya."
        scene expression ("images/episode10/200_curious.webp") with dissolve
        toby "Umm ... apa yang terjadi padanya."
        scene expression ("images/episode10/199_sad.webp") with dissolve
        sheila "Tidak ada apa-apa. Maaf, saya tidak ingin merusak malam."
        scene expression ("images/episode10/200_normal.webp") with dissolve
        toby "Anda tidak merusak apapun. Apa yang terjadi dengan [sister] Anda?"
        scene expression ("images/episode10/199_angry.webp") with dissolve
        sheila "Tidak ada apa-apa. Saya tidak ingin membicarakannya."
        scene expression ("images/episode10/200_sad.webp") with dissolve
        toby "Maaf jika saya mengatakan sesuatu. Apakah kamu baik -baik saja?"
        scene expression ("images/episode10/199_smile.webp") with dissolve
        sheila "Jangan khawatir. Saya baik-baik saja."
        scene expression ("images/episode10/199_flirty.webp") with dissolve
        sheila "Apakah Anda mendapatkan cokelatnya?"
        scene expression ("images/episode10/200_normal.webp") with dissolve
        toby "Ya. Tapi apakah Anda yakin ini yang Anda butuhkan sekarang?"
        scene expression ("images/episode10/199_normal.webp") with dissolve
        sheila "Ya. Ini adalah satu -satunya hal yang saya inginkan sekarang. Mari kita kembali ke tempat saya."
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
        toby "Apa yang salah, Sheila?"
        scene expression ("images/episode10/208.webp") with dissolve
        sheila "Apa ini? Ini bukan cokelat yang kita bicarakan."
        toby "Ummm ..."
        scene expression ("images/episode10/209.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What's going on? Why is she acting so strange suddenly?{/i}"
        scene expression ("images/episode10/210.webp") with dissolve
        sheila "Lihat, aku tidak ingin lagi. Biarkan saya mengenakan sesuatu dan saya akan melihat Anda keluar."
    else:

        scene expression ("images/episode10/211.webp") with dissolve
        toby "Hei Sheila, lihat apa yang saya dapatkan untuk Anda."
        scene expression ("images/episode10/212.webp") with dissolve
        sheila "Kamu punya beberapa?"
        scene expression ("images/episode10/211.webp") with dissolve
        toby "Yah, itu tidak mudah, tetapi karena Anda selalu sangat baik kepada saya, saya pikir akan menyenangkan untuk melakukan sesuatu untuk Anda."
        scene expression ("images/episode10/212.webp") with dissolve
        sheila "Baiklah, terima kasih ..."

        scene expression ("images/episode10/213_1.webp") with dissolve
        sheila "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Fuck... I can't do this to you.{/i}"
        scene expression ("images/episode10/213_2.webp") with dissolve
        sheila "Ini bukan cokelat yang telah saya ceritakan."
        scene expression ("images/episode10/214.webp") with dissolve
        toby "Apa kamu yakin? Karena aku hampir ..."
        scene expression ("images/episode10/215.webp") with dissolve
        sheila "Tidak, itu tidak. Ngomong -ngomong, biarkan aku melihatmu keluar."

    $ progress = 138
    scene expression ("images/episode10/216.webp") with fade
    toby "Apa yang terjadi, Sheila?"
    sheila "Pertama -tama Anda harus tahu bahwa saya sangat menyesal atas segalanya."
    scene expression ("images/episode10/217_normal.webp") with dissolve
    sheila "Saya bukan pelatih pribadi. Saya sebenarnya seorang agen yang menyamar, dan saya sedang menyelidiki Katrina dan Darlene."
    scene expression ("images/episode10/218_surprised.webp") with dissolve
    toby "Anda berantakan dengan saya, kan?"
    toby "Saya mengerti Katrina, tapi Darlene?"
    scene expression ("images/episode10/217_normal.webp") with dissolve
    sheila "Anda benar. Investigasi terutama pada Katrina, tetapi Darlene juga tidak bersalah."
    sheila "Bersama -sama pasangan ini menjalankan klub BDSM rahasia dan mereka sedang diselidiki untuk narkoba, pelacuran, perdagangan manusia dan siapa yang tahu kengerian apa yang terjadi di sana."
    scene expression ("images/episode10/218_curious.webp") with dissolve
    toby "Dan apa hubungannya dengan saya? Saya tidak terlibat dalam hal itu."
    scene expression ("images/episode10/217_sad.webp") with dissolve
    sheila "Anda muncul di radar kami ketika Anda mengambil pekerjaan itu, jadi kami harus mengawasi Anda sejak awal. Dengan begitu Anda tidak akan mencurigai saya nanti."
    sheila "Itu adalah pekerjaan saya, untuk mendekati Anda dan kemudian menggunakan Anda untuk informasi dan mungkin akses."
    if sheila_path:
        scene expression ("images/episode10/218_angry.webp") with dissolve
        toby "Jadi seks itu hanya bagian dari pekerjaan itu."
        scene expression ("images/episode10/217_sad.webp") with dissolve
        sheila "Tolong, jangan seperti itu. Saya mendapat perintah saya."
        scene expression ("images/episode10/218_normal.webp") with dissolve
        toby "Jadi tidak apa -apa bagi Anda untuk berhubungan seks dengan saya, karena bos Anda memerintahkan Anda, tetapi jika Katrina melakukannya, maka itu adalah mucikari dan pelacuran."
        scene expression ("images/episode10/217_normal.webp") with dissolve
        sheila "Tidak seperti itu."
        scene expression ("images/episode10/218_angry.webp") with dissolve
        toby "Lalu bagaimana itu? Kenapa kamu tidak mengisap penisku? Bukankah itu pekerjaanmu."
        scene expression ("images/episode10/219.webp") with dissolve
        sheila "Anda seorang bajingan!"
        scene expression ("images/episode10/217_angry.webp") with dissolve
        sheila "Lihat. Saya membuat pengorbanan besar di sini."
        scene expression ("images/episode10/218_normal.webp") with dissolve
        toby "What are you sacrificing? You won't have a \"booty call boy\"Saat Anda ingin berhubungan seks?"
        scene expression ("images/episode10/217_angry.webp") with dissolve
        sheila "Menurut Anda mengapa kami tidak berhubungan seks kemarin? Aku benci menggunakanmu. Anda tidak pantas mendapatkan ini."
        scene expression ("images/episode10/218_angry.webp") with dissolve
        toby "Tetap saja ... Aku tidak melihat apa yang kamu korbankan, dengan tidak meniduriku."
        scene expression ("images/episode10/217_angry.webp") with dissolve
        sheila "Saya mengorbankan [sister] saya, Anda bajingan."
    else:
        scene expression ("images/episode10/218_curious.webp") with dissolve
        toby "Jadi, mengapa Anda mengatakan ini sekarang?"
        scene expression ("images/episode10/217_sad.webp") with dissolve
        sheila "Karena Anda benar -benar pria baik yang terlalu dekat dengan api."
        scene expression ("images/episode10/218_normal.webp") with dissolve
        toby "Bukankah itu seluruh idenya? Tunggu saya masuk ke organisasi dan kemudian gunakan saya, sehingga Anda dapat menjatuhkannya?"
        toby "Kecuali bahwa saya mungkin akan turun juga."
        scene expression ("images/episode10/218_angry.webp") with dissolve
        toby "Jadi Anda tidak peduli bahwa Anda membiarkan seseorang merusak hidupnya selama Anda menyelesaikan pekerjaan."
        toby "Itu bagus."
        scene expression ("images/episode10/217_normal.webp") with dissolve
        sheila "Tidak seperti itu."
        scene expression ("images/episode10/218_curious.webp") with dissolve
        toby "Berharap bahwa saya akan masuk lebih dalam ke dunia mereka sehingga Anda bisa menggunakan saya untuk info?Lalu mencerahkan saya. Bagaimana itu. Bukankah itu seluruh idenya?"
        scene expression ("images/episode10/217_angry.webp") with dissolve
        sheila "Lihat. Saya membuat pengorbanan besar di sini."
        scene expression ("images/episode10/218_normal.webp") with dissolve
        toby "Jangan salah paham. Saya menghargai Anda mengatakan ini kepada saya, tetapi itu tidak mengubah fakta bahwa kalian akan membiarkan saya merusak hidup saya."
        scene expression ("images/episode10/218_angry.webp") with dissolve
        sheila "Yah, saya akan menghancurkan hidup siapa pun untuk menyelamatkan [sister] saya."

    scene expression ("images/episode10/218_curious.webp") with dissolve
    toby "Anda [sister]? Apa yang kamu bicarakan?"
    scene expression ("images/episode10/217_normal.webp") with dissolve
    sheila "Aku hampir yakin Katrina memilikinya."
    scene expression ("images/episode10/218_normal.webp") with dissolve
    toby "Maksudmu seperti, dia menculiknya?"
    scene expression ("images/episode10/217_cry.webp") with dissolve
    sheila "Aku tidak tahu. Saya tidak tahu apa -apa lagi tentang dia."
    scene expression ("images/episode10/218_normal.webp") with dissolve
    toby "Saya minta maaf. Saya tidak tahu, tapi apa yang sebenarnya terjadi?"
    scene expression ("images/episode10/217_normal.webp") with dissolve
    sheila "Nah, [mother] kami meninggal ketika kami masih kecil, jadi kami hanya memiliki [father], tetapi ia meninggal dalam menjalankan tugas ketika saya berusia 19 tahun. Dia berusia 17 tahun saat itu."
    scene expression ("images/episode10/217_sad.webp") with dissolve
    sheila "Kematiannya mempengaruhi kita dengan sangat berbeda. Saya memutuskan untuk menjadi polisi dan melanjutkan warisannya. Selesaikan apa yang dia tidak bisa."
    scene expression ("images/episode10/218_curious.webp") with dissolve
    toby "Dan [sister] Anda?"
    scene expression ("images/episode10/217_sad.webp") with dissolve
    sheila "Yah, dia memilih jalan yang berbeda. Dia sangat kesal sehingga dia meninggal, sehingga dia memberontak terhadap apa pun yang saya yakini [father]."
    scene expression ("images/episode10/217_angry.webp") with dissolve
    sheila "Dia menentang merokok, jadi dia mulai merokok."
    scene expression ("images/episode10/217_sad.webp") with dissolve
    sheila "Dia menentang narkoba, jadi dia mulai menggunakan."
    sheila "Dia menentang kami pergi ke klub, jadi tebak apa yang dia lakukan."
    scene expression ("images/episode10/218_normal.webp") with dissolve
    toby "Biarkan saya menebak. Dia pergi clubbing?"
    scene expression ("images/episode10/217_normal.webp") with dissolve
    sheila "Setiap malam."
    scene expression ("images/episode10/217_sad.webp") with dissolve
    sheila "Dan bukan saja dia kesal padanya, dia juga kesal pada saya, karena saya menjadi polisi dan dia pikir saya akan mati sama seperti dia."
    scene expression ("images/episode10/217_cry.webp") with dissolve
    sheila "Karena [father] kami meninggal, saya menjadi sedikit terlalu protektif dan kami bertengkar besar."
    sheila "Itu terakhir kali saya melihatnya. Saya ingat dia berdandan untuk klub dan menyuruh saya untuk bercinta."
    sheila "Itu di mana kata -kata terakhirnya untukku."
    scene expression ("images/episode10/218_normal.webp") with dissolve
    toby "Dan izinkan saya menebak. Itu klub Katrina?"
    scene expression ("images/episode10/217_sad.webp") with dissolve
    sheila "Tepatnya, jadi fakta bahwa saya mengatakan ini kepada Anda, mungkin membuat saya kehilangan misi, tetapi saya sudah kehilangan seseorang yang saya sayangi, jadi saya tidak kehilangan Anda juga."
    scene expression ("images/episode10/218_curious.webp") with dissolve
    toby "Tetapi mengapa Anda berisiko kehilangan [sister] Anda untuk beberapa orang asing?"
    scene expression ("images/episode10/217_cryLaugh.webp") with dissolve
    sheila "Mengalahkan saya jika saya tahu."
    if sheila_path:
        scene expression ("images/episode10/217_normal.webp") with dissolve
        sheila "Tapi aku mulai sangat menyukaimu, jadi aku tidak bisa membiarkanmu merusak hidupmu."
        scene expression ("images/episode10/217_normal.webp") with dissolve
        sheila "Anda adalah orang pertama yang benar -benar menghormati saya dan menyukai saya dengan tulus, atau setidaknya itulah yang saya yakini."
        menu:
            "{i} [JGR] Cium dia {/i}":
                show ep10_220 with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode10/220.webp")
                hide ep10_220
                toby "Saya sangat melakukannya."
                sheila "Saya tahu, [toby!c]."
                scene expression ("images/episode10/221.webp") with dissolve
                sheila "Untuk apa itu?"
                toby "Saya tidak tahu, rasanya Anda bisa menggunakan sedikit cinta."
            "{i} peluk {/i} [JWRN2]"(csq="Menutup jalan Sheila."):

                $ sheila_closed = True
                $ sheila_path = False
                $ renpy.notify("Sheila's path has been closed!")
                pass
    else:
        scene expression ("images/episode10/217_normal.webp") with dissolve
        sheila "Tapi itu adalah pertama kalinya seseorang melakukan sesuatu yang baik untuk saya tanpa mengharapkan imbalan sesuatu."
        scene expression ("images/episode10/217_laugh.webp") with dissolve
        sheila "Anda muncul dengan senyum bodoh yang besar itu, karena Anda berhasil memberi saya sekotak cokelat itu dan Anda tidak pernah mengharapkan imbalan apa pun. Itu sangat istimewa saat ini."
    if sheila_path == False:
        scene expression ("images/episode10/222.webp") with dissolve
        toby "Kemarilah."
        scene expression ("images/episode10/223.webp") with dissolve

    sheila "Terima kasih karena tidak kesal pada saya."
    toby "Saya kesal, tetapi saya mengerti alasan Anda. Saya mungkin akan melakukan apa saja untuk [sister] saya juga."
    sheila "Saya yakin akan hal itu."

    scene expression ("images/episode10/224.webp") with dissolve
    toby "Omong-omong. Mengapa kita berada di lorong?"
    sheila "Apartemen saya disadap."
    if sheila_path:
        toby "Dan apa yang akan terjadi jika kita berhubungan seks? Apakah bos Anda akan mendengar Anda berteriak nama saya?"
        sheila "Sekarang Anda katakan seperti itu, kedengarannya kotor."
    else:
        toby "Sial ... Aku tidak pernah pergi ke apartemenmu."
    sheila "Bagaimanapun. Apa yang akan kamu lakukan sekarang?"
    scene expression ("images/episode10/225.webp") with dissolve
    toby "Apa lagi yang bisa saya lakukan? Saya akan membantu Anda dengan [sister] Anda."
    sheila "Apakah kamu serius?"
    toby "Tentu saja, tetapi saya akan membutuhkan bantuan Anda untuk tidak membiarkan saya turun bersama semua orang."
    sheila "Saya akan melakukan yang terbaik, tapi tolong cobalah untuk tidak melakukan sesuatu yang ilegal."
    if toby_job == 0:
        toby "Saya akan."
        sheila "Dan saya akan berbicara dengan atasan saya dan mencoba meyakinkan mereka untuk memberi Anda kekebalan, tetapi Anda harus membantu saya mengekspos pasangan itu."
        toby "Saya masih tidak membeli bahwa Darlene memiliki bagian dari itu, tetapi saya akan melakukan yang terbaik untuk membuktikan bahwa Katrina bersalah."
        sheila "Jangan terlalu percaya padanya."
    else:
        toby "Suka memberikan obat -obatan?"
        sheila "Ya..."
        toby "Lalu, itu akan menjadi masalah."
        sheila "Sial ... jangan khawatir, saya akan berbicara dengan atasan saya dan meyakinkan mereka untuk memberi Anda kekebalan. Lagi pula, Anda tidak melakukan apa pun, tetapi itu berarti Anda membantu kami mengekspos pasangan itu, tidak hanya membantu saya."
        toby "Saya tidak berutang apa pun kepada mereka, tetapi jika itu yang harus saya lakukan, saya akan melakukan yang terbaik."

    scene expression ("images/episode10/226.webp") with dissolve
    toby "Bagaimanapun, saya kira saya harus pergi, sebelum bos Anda mencurigai apa pun."
    sheila "Ya, Anda benar."
    sheila "Terima kasih atas segalanya dan berhati -hatilah."
    toby "Jangan khawatir. Saya akan baik -baik saja."

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
    charlotte "Tolong, [toby!c]. Keluar. Ini tidak ada hubungannya dengan Anda."
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
    charlotte "Uang sialan apa? Anda tidak pernah memberi saya uang receh sejak kami pindah. Aku tidak pernah menanyakan apapun padamu. Aku hanya perlu kamu mencintaiku."
    scene expression ("images/episode10/248.webp") with dissolve
    toby "Kemarilah, [mom]. Anda tidur di kamar saya malam ini."
    scene expression ("images/episode10/249.webp") with dissolve
    erwin "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nIf she's not cheating me, then explain why I found this sexy lingerie. I for one haven't seen her in it."
    scene expression ("images/episode10/250.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nHow the fuck would you want to see her dressed like that since when you're home all you do is sleep?"
    toby "Masalahnya tidak pernah [mom]. Anda tahu dia tidak akan pernah menipu Anda, tetapi Anda terlalu mabuk untuk mengakuinya dan terlalu bangga untuk membicarakan masalah sebenarnya."
    scene expression ("images/episode10/251.webp") with dissolve
    toby "Let \'s Go, [mom]."
    scene expression ("images/episode10/252.webp") with fade
    charlotte "Terima kasih telah membela saya. Saya tidak pernah bisa meminta yang lebih baik [son]."
    toby "Anda tahu saya akan selalu ada di sini untuk Anda."
    charlotte "Aku tahu."
    scene expression ("images/episode10/255.webp") with dissolve
    charlotte "..."
    scene expression ("images/episode10/253_curious.webp") with dissolve
    charlotte "Apakah Anda pikir saya harus melakukannya?"
    scene expression ("images/episode10/254_normal.webp") with dissolve
    toby "Lakukan apa?"
    scene expression ("images/episode10/253_sad.webp") with dissolve
    charlotte "Menceraikannya?"
    scene expression ("images/episode10/254_sad.webp") with dissolve
    toby "Tetapi ketahuilah bahwa Anda tidak perlu khawatir tentang saya atau Tris.Lihat [mom]. Saya tidak bisa memberi tahu Anda apa yang harus dilakukan. Itu keputusan Anda."
    scene expression ("images/episode10/254_normal.webp") with dissolve
    toby "Kami keduanya cukup tua untuk dipahami. Jadi buat keputusan ini untuk Anda, bukan untuk kami."
    scene expression ("images/episode10/253_sad.webp") with dissolve
    charlotte "Terima kasih sayang."
    scene expression ("images/episode10/253_normal.webp") with dissolve
    charlotte "Apa yang akan Anda lakukan dalam situasi saya?"
    scene expression ("images/episode10/254_sad.webp") with dissolve
    toby "Saya akan mengatakan bahwa perceraian adalah jalannya, tetapi saya belum memiliki hubungan 20 tahun. Saya tidak pernah tinggal dengan siapa pun. Saya tidak pernah berbagi yang baik atau buruk dengan seseorang, jadi saya tidak tahu apa yang Anda alami."
    scene expression ("images/episode10/253_smile.webp") with dissolve
    charlotte "Anda adalah anak yang bijak."
    scene expression ("images/episode10/254_smile.webp") with dissolve
    toby "Saya jelas mengejar Anda."
    scene expression ("images/episode10/254_normal.webp") with dissolve
    toby "Ketahuilah bahwa apa pun yang Anda pilih, saya akan selalu berada di sisi Anda."
    scene expression ("images/episode10/256.webp") with dissolve
    charlotte "Aku mencintaimu, [toby!c]."
    toby "Aku juga mencintaimu, [mom]."
    scene expression ("images/episode10/257.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    return

label episode10_nightCharlotte:
    $ progress = 140
    label memory_35:

        scene expression ("images/episode10/258.webp") with dissolve
        toby "Apakah Anda ingin saya membiarkan Anda tidur?"
        scene expression ("images/episode10/259_1.webp") with dissolve
        charlotte "Bagaimana denganmu?"
        scene expression ("images/episode10/259_2.webp") with dissolve
        toby "Jangan khawatir tentang saya. Saya akan tidur di sofa. Itu yang paling tidak bisa saya lakukan."
        scene expression ("images/episode10/259_1.webp") with dissolve
        charlotte "Paling tidak yang bisa Anda lakukan adalah tidur di sini dengan saya."
        scene expression ("images/episode10/264.webp") with dissolve
        toby "Apakah Anda yakin ini ide yang bagus?"
        charlotte "Maksudmu diberikan apa yang terjadi di antara kita?"
        toby "Tepat?"
        scene expression ("images/episode10/265.webp") with dissolve
        charlotte "Saya tidak tahu. Aku bahkan tidak tahu apa yang terjadi di antara kita. Yang saya tahu adalah bahwa saya tidak ingin sendirian malam ini."
        scene expression ("images/episode10/266.webp") with dissolve
        toby "Ya. Dan yang saya tahu adalah bahwa setiap kali saya berdetak kencang."
        toby "Ketika saya melihat Anda, yang bisa saya pikirkan adalah betapa cantiknya Anda. Betapa peduli, betapa cerdasnya Anda. Aku tidak punya kata -kata untuk menggambarkan apa yang aku rasakan ketika aku bersamamu."
        toby "Ketika saya menatap mata Anda, saya tersesat dalam pikiran, itu sangat mirip dengan ketika Anda jatuh cinta."
        scene expression ("images/episode10/267.webp") with dissolve
        charlotte "Tapi ... aku [mother] kamu."
        toby "Aku tahu. Itulah yang membuat segalanya menjadi sangat rumit, karena apa yang saya rasakan saat ini untuk Anda adalah sedikit dari segalanya."
        scene expression ("images/episode10/268.webp") with dissolve
        charlotte "Maksudmu kamu mencintaiku seperti [son], tapi juga kamu mencintaiku seperti pria mencintai wanita?"
        toby "Tepat. Rasanya sangat kuat, saya bahkan tidak bisa meletakkan jari saya di atasnya."
        charlotte "Saya tahu persis apa yang Anda rasakan, karena itu sama untuk saya."
        scene expression ("images/episode10/269.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0
        charlotte "Anda adalah [son] saya. Bocah yang saya ajarkan cara berjalan."

        scene expression ("images/episode10/270.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0
        toby "Dan Anda adalah [mother] saya, wanita yang mengajari saya cara mengendarai sepeda."

        scene expression ("images/episode10/271.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        charlotte "Itu agak sulit pada awalnya."

        scene expression ("images/episode10/272.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        toby "Tapi kamu selalu ada untukku."

        scene expression ("images/episode10/273.webp") with dissolve:
            xalign 0.0
            yalign 0.0
            linear 10.0 xalign 1.0 yalign 1.0
        charlotte "Dan saya akan selalu begitu. Apa pun yang terjadi. Momen buruk."

        scene expression ("images/episode10/274.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        charlotte "Tapi juga saat -saat yang baik, seperti saat Anda pergi ke pesta prom. Aku sangat bangga padamu."

        scene expression ("images/episode10/275.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0
        toby "Ya ... kami ingat prom saya sedikit berbeda."
        charlotte "Aku masih bangga padamu. Anak laki -laki saya adalah seorang pria."

        scene expression ("images/episode10/276.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        charlotte "Jadi ya. Itu cinta itu."
        toby "Tapi itu lebih dari itu."

        if ep1_groping_charlotte or _in_replay:
            scene expression ("images/episode10/277.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0

            charlotte "Saya masih ingat saat pertama kali Anda menyentuh payudara saya. Saya merasa sangat bersemangat, tetapi saya selalu menyalahkan alkohol."

            scene expression ("images/episode10/278.webp") with dissolve:
                xalign 1.0
                linear 10.0 xalign 0.0

            toby "Sejujurnya Anda memiliki payudara yang luar biasa."
            charlotte "Kapan Anda melihat mereka?"
            toby "Tidakkah Anda ingat ketika T-shirt Anda ditarik selama berolahraga?"
        else:

            scene expression ("images/episode10/278.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0
            toby "Saya tidak bisa berhenti memikirkan waktu ketika saya melihat payudara Anda, selama berolahraga."

        charlotte "Saya sangat malu pada hal itu, tetapi fakta bahwa Anda mendapat boner membuat saya begitu ..."
        toby "Terangsang?"
        charlotte "Saya akan mengatakan bersemangat, tetapi terangsang bisa bekerja juga."
        charlotte "Itu ketika saya menemukannya bahwa rasanya enak menggoda Anda. Saya merasa diinginkan. Untuk pertama kalinya dalam bertahun -tahun."

        scene expression ("images/episode10/279.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        toby "Dan Anda suka menggodaku."

        scene expression ("images/episode10/280.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0
        charlotte "Itu memang membuatku merasa baik, tapi itu tidak semua."
        charlotte "Awalnya saya pikir itu hanya kurangnya perhatian, tetapi bukan itu."

        scene expression ("images/episode10/281.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        charlotte "Apakah Anda ingat bahwa setelah kencan pertama kami, kami berdiri di depan rumah, bercanda tentang ciuman di kencan pertama."
        toby "Ya ... yang ingin saya lakukan hanyalah mencium bibirmu yang indah."
        charlotte "Anda tidak tahu seberapa besar saya menginginkannya juga dan kemudian menyalahkan alkohol dan semuanya."
        toby "Itu sangat berbeda dari semuanya sebelumnya."

        scene expression ("images/episode10/282.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0
        charlotte "Itu tidak pernah hanya [mother] cinta."
        toby "Itu lebih dari itu."

        scene expression ("images/episode10/283.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.25
        charlotte "Itu jauh lebih banyak."
        toby "Aku mencintaimu [mom]."
        charlotte "Aku pun mencintaimu."

        show ep10_284 with dissolve
        $ unlockImage(persistent.charlotte_18)
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode10/284.webp")
        hide ep10_284

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Umm... I just kissed my [mother].{/i}"
        scene expression ("images/episode10/285.webp") with dissolve
        show ep10_285
        charlotte "Ummm ... itu ... sangat bagus."
        toby "Rasanya begitu ..."
        charlotte "Benar dan salah pada saat yang sama?"
        toby "Ya!"
        show ep10_286 with dissolve
        hide ep10_285
        charlotte "Tidak terlalu cepat, koboi. Itu adalah satu kali. Saya masih mencoba memproses apa yang terjadi."
        toby "Apa yang harus diproses? Kami berdua menyukainya."
        charlotte "Itu tidak berarti Anda tidak lagi saya [son]."
        charlotte "Mari kita coba dan tidur. Saya tidak bisa berpikir lurus saat ini."
        scene expression ("images/episode10/286.webp")
        hide ep10_286
        scene expression ("images/episode10/287.webp") with dissolve:
            xalign 0.9
        charlotte "Apakah Anda memiliki T-shirt yang bisa saya pinjam?"
        scene expression ("images/episode10/287.webp") with dissolve:
            xalign 0.2
        toby "Anda bisa memakai pakaian dalam."
        scene expression ("images/episode10/287.webp") with dissolve:
            xalign 0.9
        charlotte "Anda benar -benar ingin melihat apa yang Denise buat saya beli?"
        scene expression ("images/episode10/287.webp") with dissolve:
            xalign 0.2
        toby "Mungkin?"
        scene expression ("images/episode10/287.webp") with dissolve:
            xalign 0.9
        charlotte "Anda anak nakal."

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
    toby "Apakah Anda ingin saya membiarkan Anda tidur?"
    scene expression ("images/episode10/259_1.webp") with dissolve
    charlotte "Bagaimana denganmu?"
    scene expression ("images/episode10/259_2.webp") with dissolve
    toby "Jangan khawatir. Saya akan tidur di sofa."
    scene expression ("images/episode10/259_1.webp") with dissolve
    charlotte "Aku merasa tidak enak membuatmu tidur di sofa."
    scene expression ("images/episode10/260.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode10/261.webp") with dissolve
    toby "Ini yang paling tidak bisa saya lakukan untuk Anda."
    scene expression ("images/episode10/262.webp") with dissolve
    charlotte "Terima kasih sayang."
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
