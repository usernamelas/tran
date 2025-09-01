image ep2_104 = Movie(play="video/episode2/104.webm", loop=True)
image ep2_105 = Movie(play="video/episode2/105.webm", loop=True)
image ep2_106 = Movie(play="video/episode2/106.webm", loop=True)
image ep2_107 = Movie(play="video/episode2/107.webm", loop=True)
image ep2_204 = Movie(play="video/episode2/204.webm", loop=True)
image ep2_205 = Movie(play="video/episode2/205.webm", loop=True)
image ep2_206 = Movie(play="video/episode2/206.webm", loop=True)
image ep2_207 = Movie(play="video/episode2/207.webm", loop=True)
image ep2_303 = Movie(play="video/episode2/303.webm", image="images/episode2/303.webp", loop = False)

label episode2:
    stop music fadeout 4.0
    scene expression ("images/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(1, 2) with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_newEpisode

    show screen ui_message("Tuesday") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    call episode2_chooseJob from _call_episode2_chooseJob

    call episode2_pilates from _call_episode2_pilates

    call episode2_tvTris from _call_episode2_tvTris

    if toby_job == 0:
        call episode2_realEstate from _call_episode2_realEstate
    else:

        call episode2_club from _call_episode2_club

    call episode2_drinkMom from _call_episode2_drinkMom

    call episode2_trisNight from _call_episode2_trisNight

    return


label episode2_chooseJob:
    $ progress = 18


    scene expression ("images/episode2/001.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmmm. I wonder, what should I do. Who should I call?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}On one hand, calling Darlene would mean a more stable job, without so many complications.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}However working for Katrina might affect me in some way, but I'm sure that it would be fun.{/i}"

    "{color=#FDCA6E} Hati -hati. Keputusan yang akan Anda buat akan memiliki dampak besar pada pengembangan karakter. Pilih kehidupan yang lebih cocok untuk Anda. {/color}"

    menu:
        "{i} Hubungi Darlene untuk pekerjaan real estat {/i}"(csq="Gambar galeri"):
            $ toby_job = 0
            $ unlockImage(persistent.darlene_02)
            scene expression ("images/episode2/002.webp") with dissolve
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nHello?"
            toby "Selamat pagi, ma \ 'am. Itu aku [toby!c]. Kami bertemu kemarin, dan Anda menyuruh saya menelepon Anda."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nOh, [toby!c]. I think I already told you to call me Darlene. I'm not that old yet!"
            toby "Maaf, Darlene."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nAnyway, I'm glad you called. Please tell me you didn't call just to say that you're going to work for my girlfriend."
            toby "Tidak, saya belum. Saya menelepon untuk memberi tahu Anda bahwa saya tertarik untuk bekerja untuk Anda."
            scene expression ("images/episode2/003.webp") with dissolve
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nYou did the right thing."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nWhat are you doing this afternoon around 4PM?"
            toby "Saya belum membuat rencana karena Anda memberi tahu saya kemarin bahwa kami akan menjual apartemen."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nI told you that we are going to try and sell an apartment, but I like your enthusiasm."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nDo you have a car?"
            scene expression ("images/episode2/002.webp") with dissolve
            toby "Tidak juga, tapi saya pikir saya bisa meminjam mobil saya [mother]."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nNo need!"
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nText me the address. I'll come to pick you up at 03:30PM."
            toby "Tentu!"
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nOkay then. See you at 03:30PM."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nAnd [toby!c], make sure you're wearing something nice. We need to make a good impression on our clients!"
            toby "Tentu saja."
            darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nHave a good day, [toby!c]. See you later!"
            toby "Sampai jumpa!"
            scene expression ("images/episode2/004.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I better send her my address.{/i}"
            scene expression ("images/episode2/005.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I hope I made the right choice. Let's see how working for Darlene will play out.{/i}"
            pass
        "{i} hubungi Katrina untuk bisnis teduh {/i}"(csq="Gambar galeri"):

            $ toby_job = 1
            $ unlockImage(persistent.katrina_02)
            scene expression ("images/episode2/002.webp") with dissolve
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nYeah?"
            toby "Selamat pagi ma \ 'am. Itu aku [toby!c]. Kemarin Anda memberi saya selembar kertas dengan nomor ini di atasnya."
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nOh my, [toby!c]. I really thought my girlfriend stole you from me!"
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nSo? Are you ready to make some money and have fun at the same time?"
            toby "Saya kira begitu, tapi saya tidak yakin apa yang perlu saya lakukan."
            scene expression ("images/episode2/003.webp") with dissolve
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nLet's meet later at my office, and I'll tell you everything you need to know."
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nThe important part is that you please me!"
            toby "Uhm ... oke."
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nUhm...? Okay? What is that shit? You're working for me now! I don't want to hear you being unsure. I need men, not boys!"
            toby "Maaf ma \ 'am!"
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nSorry? My men are never sorry. Tonight I'll be finding your lost balls. You do have balls, don't you?"
            menu:
                "{i} menjadi arogan {/i}":
                    toby "Ingin merasakannya?"
                    katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nI'm a lesbian, but I like your confidence, and if you're a good boy, I just might try them!"
                "{i} bertindak normal {/i}":

                    toby "Ya, saya punya bola besar!"
                    katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nThat's much better."
            scene expression ("images/episode2/002.webp") with dissolve
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nDo you have a car?"
            toby "Tidak, belum, kami harus menjual mobil kami."
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nThat sucks. I'll send one of my men to come to pick you up. Text me the address!"
            toby "Anda tidak harus melakukan itu, saya bisa naik bus."
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nBullshit! My men will not be seen taking the bus!"
            toby "Oke kalau begitu. Saya akan mengirimi Anda alamat saya!"
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nPerfect. See you later."
            toby "Sampai jumpa!"
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nAnd by the way..."
            toby "Ya?"
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nI'm going to make a man out of you, just you wait!"
            toby "..."
            scene expression ("images/episode2/004.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I better send her my address.{/i}"
            scene expression ("images/episode2/005.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I hope I made the right choice. Katrina sounds a little bit shady, but at the same time, very intriguing.{/i}"
            pass


    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think I should tell [mom] how the phone call went. I'm sure she'd like to know.{/i}"

    return

label episode2_pilates:
    $ progress = 19


    scene expression ("images/episode2/006.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the hell is she doing?{/i}"
    scene expression ("images/episode2/007.webp") with dissolve
    toby "Pagi, [mom]. Apa yang sedang kamu lakukan?"
    scene expression ("images/episode2/008.webp") with dissolve
    charlotte "Pagi, sayang. Saya melakukan Pilates."
    scene expression ("images/episode2/007.webp") with dissolve
    toby "Saya mungkin salah, tetapi seharusnya tidak ada bola, bukan kursi itu untuk melakukan pilates?"
    scene expression ("images/episode2/008.webp") with dissolve
    charlotte "Ya, tetapi jika Anda tidak dapat menemukan bola karena Anda baru saja pindah, aman untuk mengatakan bahwa menggunakan kursi adalah hal terbaik berikutnya."
    scene expression ("images/episode2/009.webp") with dissolve
    toby "Sucks to Be You!"
    charlotte "Ah, benarkah? Begitulah cara Anda ingin memainkan ini. Jadi Anda pikir saya tidak boleh menggunakan kursi?"
    toby "Saya hanya mengatakan. Mungkin menggunakan sesuatu yang lebih nyaman."
    scene expression ("images/episode2/010.webp") with dissolve
    charlotte "Saya pikir saya baru saja menemukan hal yang paling nyaman untuk digunakan sebagai pengganti bola saya!"
    scene expression ("images/episode2/011.webp") with dissolve
    toby "Saya pikir kursi itu pengganti yang baik."
    charlotte "Tidak. Anda benar, punggung saya sedikit sakit karena itu. Jadi mengapa Anda tidak membantu [mother] Anda membutuhkan!"
    scene expression ("images/episode2/012.webp") with dissolve
    toby "Saya tidak [dad]. Mata anak anjing Anda tidak akan bekerja pada saya."
    charlotte "TIDAK? Benar-benar? Sama sekali tidak?"
    toby "Tidak!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I gotta be honest, she's kinda cute though.{/i}"
    charlotte "Oke kalau begitu. Kami akan bermain dengan aturan yang berbeda."
    scene expression ("images/episode2/013.webp") with dissolve
    charlotte "Selama Anda tinggal di rumah saya, Anda akan melakukan apa yang saya katakan!"
    toby "Tidakkah menurutmu itu agak tidak adil?"
    charlotte "Saya memberi tahu Anda apa yang tidak adil. Saya tidak menemukan bola itu."
    scene expression ("images/episode2/014.webp") with dissolve
    charlotte "Jaga saja tangan Anda seperti ini."
    toby "Saya akan mengajukan keluhan dengan layanan perlindungan anak. Saya merasa bekas."
    scene expression ("images/episode2/015.webp") with dissolve
    charlotte "Anda tidak lagi seorang anak. Anda adalah orang dewasa muda. Jika Anda tidak menyukai bagaimana [mother] Anda memperlakukan Anda, Anda selalu dapat bergerak!"
    toby "Anda akan sangat merindukan saya."
    charlotte "Tentu saja saya, tetapi tidak seperti Anda tahu cara memasak, jadi saya pikir bahkan jika Anda pindah, Anda masih akan kembali setiap pagi untuk makan."
    toby "Apakah pose ini benar -benar melakukan sesuatu untuk Anda?"
    scene expression ("images/episode2/016.webp") with dissolve
    charlotte "Bagaimana saya harus tahu? Itulah yang disuruh pelatih pribadi saya untuk saya lakukan. Tetap diam seperti ini dengan tangan saya di bola itu!"
    toby "Biarkan saya meluruskan ini, Anda sudah selesai Pilates selama 5 tahun, dan Anda masih tidak tahu mengapa Anda melakukan hal -hal seperti ini?"
    scene expression ("images/episode2/017.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    charlotte "Bagaimana menurutmu? Apakah saya terlihat baik -baik saja untuk usia saya?"
    toby "Ya, tetapi Anda selalu terlihat bagus bahkan sebelum melakukan Pilates."
    charlotte "Anda ada benarnya, tetapi saya tidak jatuh cinta padanya."
    scene expression ("images/episode2/018.webp") with dissolve
    toby "Jatuh untuk apa?"
    label memory_03:
        if _in_replay:

            scene expression ("images/utils/black.png") with dissolve
            menu:
                "Pilih pekerjaan Anda"
                "Agen real estat":
                    $ toby_job == 0
                "Manajer klub":
                    $ toby_job == 1
            scene expression ("images/episode2/018.webp") with dissolve

        charlotte "Pegang kakiku saja."
        scene expression ("images/episode2/019.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}[mom!c]'s ass is huge!{/i}"
        scene expression ("images/episode2/020.webp") with dissolve
        charlotte "Saya tahu Anda ingin saya menghentikan Pilates hari ini, bukan karena Anda pikir itu tidak berguna, tetapi karena Anda tidak ingin membantu Anda yang manis [mother] saat dia membutuhkannya."
        toby "Sekarang Anda bermain sebagai korban di sini. Anda bukan korban, jadi berhentilah bertingkah seperti itu!"
        scene expression ("images/episode2/021.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why am I staring at her ass.{/i}"
        if ep1_groping_charlotte == True:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Ever since yesterday I'm looking at [mom] in a different way and it feels so wrong.{/i}"
        charlotte "Jadi, apakah Anda memanggil wanita itu tentang pekerjaan itu?"
        toby "Ya, saya meneleponnya. Saya dijemput pada pukul 3:30 sore ini."
        scene expression ("images/episode2/022.webp") with dissolve
        charlotte "Saya harap Anda berbicara tentang pekerjaan real estat."
        if toby_job == 0:
            scene expression ("images/episode2/023.webp") with dissolve
            toby "Tentu saja. Itu adalah hal yang cerdas untuk dilakukan!"
            charlotte "Senang mendengar [son] saya pintar! Jadi apa yang akan kamu lakukan hari ini?"
            toby "Sejauh yang saya mengerti, kami akan menjual apartemen ... atau setidaknya mencoba."
            scene expression ("images/episode2/024.webp") with dissolve
            charlotte "Saya suka bagaimana Anda mengatakan \ 'kami \' seperti Anda akan melakukan apa pun."
            toby "Siapa tahu, mungkin saya akan!"
            charlotte "Dan kemudian Anda akan menjadi kaya dan menikahi seorang gadis yang tampan, seperti halnya [dad] Anda."
            scene expression ("images/episode2/025.webp") with dissolve
            toby "Apakah Anda menikah [dad] karena uangnya?"
            charlotte "Tentu saja tidak! Saya sangat mencintainya. Meskipun, itu juga menyenangkan mendapatkan semua hadiah itu!"
        else:

            scene expression ("images/episode2/023.webp") with dissolve
            toby "Tidak cukup. Saya merasa hidup saya sangat membosankan hingga saat ini, jadi bekerja di klub mungkin membumbui segalanya!"
            charlotte "Saya tidak bisa mengatakan bahwa saya bahagia untuk Anda, karena bekerja di klub itu menyenangkan ketika Anda masih muda, tetapi apa yang akan terjadi dalam 10 tahun ketika Anda akan membutuhkan pekerjaan nyata dengan penghasilan tetap untuk keluarga Anda?"
            toby "Jangan khawatir. Semuanya akan baik -baik saja. Kami akan menyeberangi jembatan itu ketika kami datang ke sana!"
            scene expression ("images/episode2/024.webp") with dissolve
            charlotte "Saya akan berharap Anda menemukan seseorang yang kaya suatu hari nanti dan menikahi mereka, sama seperti yang saya lakukan!"
            toby "Anda menikah [dad] untuk mendapatkan uang?"
            charlotte "Tentu saja tidak, tetapi dia membelikan saya semua hal mahal itu pasti membantu!"
            toby "Anda adalah penggali emas!"
            scene expression ("images/episode2/025.webp") with dissolve
            charlotte "Saya tidak. Saya sangat menyukai [dad] Anda, tapi senang mendapatkan hadiah mahal."

        scene expression ("images/episode2/026.webp") with dissolve
        toby "Dicintai? Anda tidak lagi jatuh cinta padanya?"
        charlotte "Tentu saja aku masih mencintainya, tapi ya, itu tidak seperti sebelumnya."
        toby "Kedengarannya seperti omong kosong bagi saya. Ketika saya menikah, saya akan lebih mencintai istri saya setiap hari."
        scene expression ("images/episode2/027.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        charlotte "Dan dia akan menjadi seorang wanita yang beruntung."
        toby "Apakah kita sudah selesai dengan Pilates?"
        charlotte "Hanya satu pose yang tersisa, tetapi cobalah untuk tidak membiarkan saya jatuh, yang ini sedikit lebih rumit!"
        scene expression ("images/episode2/028.webp") with dissolve
        toby "Sudahkah Anda bertemu teman -teman saya? Saya dapat memegang pose apa pun yang Anda inginkan."
        charlotte "Ya ampun, kalau saja saya beberapa tahun lebih muda."
        scene expression ("images/episode2/029.webp") with dissolve
        charlotte "Jangan biarkan aku jatuh!"
        toby "Tentu saja [mom]. Jangan khawatir. Lakukan saja hal Anda!"
        scene expression ("images/episode2/030.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}[mom!c] is heavier than I expected. How much did she eat this morning?{/i}"

        scene expression ("images/episode2/031.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck me. I can see her huge boobs. Dammit, I'm gonna get a boner.{/i}"
        scene expression ("images/episode2/032.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Her boobs are so big and it was like they are looking at me.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why am I so horny when I think about my [mom]?{/i}"
        scene expression ("images/episode2/033.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... Of course I'm getting a boner now. I mean why not?{/i}"
        scene expression ("images/episode2/034.webp") with dissolve
        charlotte "Apakah itu boner?"
        scene expression ("images/episode2/035.webp") with dissolve
        toby "Tidak. Tidak!"
        scene expression ("images/episode2/036.webp") with dissolve
        charlotte "Aduh!"
        charlotte "Sudah kubilang jangan biarkan aku jatuh."
        toby "Maaf, saya tidak bermaksud, saya hanya ..."
        scene expression ("images/episode2/037.webp") with dissolve
        charlotte "Saya tidak dapat mengingat kapan terakhir kali seseorang mendapat kesalahan pada melihat saya."
        scene expression ("images/episode2/038.webp") with dissolve
        toby "Apa?"
        charlotte "Saya tidak dapat mengingat kapan terakhir kali saya melihat boner."
        menu:
            "{i} tidak mengatakan apa -apa {/i}" if not _in_replay:
                toby "Uhm ..."
            "{i} [JGR] Beri dia pujian {/i}"(csq="Charlotte +1 & Galeri Gambar"):
                $ charlotte_rel += 1
                $ unlockImage(persistent.charlotte_04)
                toby "Saya minta maaf untuk itu, hanya saja Anda terlihat sangat, sangat bagus, dan itu terjadi."

        scene expression ("images/episode2/039.webp") with dissolve
        charlotte "Pergi mandi air dingin. Anda agak membutuhkannya tetapi tidak terlalu lama. Saya juga butuh mandi."
        toby ". {w}. {w}."
        charlotte "Terima kasih atas bantuannya."
        toby "Kapan pun?"
        scene expression ("images/episode2/040.webp") with dissolve
        charlotte "Dengan senang hati."

        $ unlockMemory(persistent.memory_03)
        $ renpy.end_replay()


    scene expression ("images/episode2/041.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why did I listen to [mom] when she told me to take a cold shower. I'm freezing to death.{/i}"
    scene expression ("images/episode2/042.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Well, at least I'm not so horny anymore.{/i}"
    if charlotte_rel >= 3:
        scene expression ("images/episode2/043.webp") with dissolve
        charlotte "[toby!c], apakah kamu sudah selesai sayang?"
        toby "Dalam sedetik [mom], saya hanya perlu berpakaian."
        charlotte "Anda sudah berpakaian? Oke kalau begitu."
        scene expression ("images/episode2/044.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n{i}I said, I need to get dressed.{/i}"
        scene expression ("images/episode2/045.webp") with dissolve
        charlotte "Maaf sayang. Saya pikir Anda bilang sudah berpakaian."
        charlotte "Ini tidak seperti saya belum pernah melihat segalanya sebelumnya sejak Anda masih kecil."
        toby "Ini sedikit berbeda sekarang."
        charlotte "Ini hanya sedikit lebih besar, tapi itu hal yang sama."
        scene expression ("images/episode2/046.webp") with dissolve
        toby "Ini jauh lebih besar."
        charlotte "Tidak terlalu. Anda cukup berbakat bahkan ketika Anda masih muda. Saya tidak tahu siapa yang Anda ambil setelahnya, karena [dad] Anda tidak sebesar itu."
        scene expression ("images/episode2/047.webp") with dissolve
        toby "Oke. Saya pergi."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I don't know what's up with her, but since we moved here she's been acting very strange.{/i}"

    return

label episode2_tvTris:
    $ progress = 20


    show screen ui_message("Later that day") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode2/048.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This city is so boring. I was excited when we moved here because I thought I would get to meet new people, but in reality, I'm just staying inside all day watching TV.{/i}"
    scene expression ("images/episode2/049.webp") with dissolve
    patricia "Hai [toby!c]."
    toby "Pagi."
    scene expression ("images/episode2/050.webp") with dissolve
    patricia "Pagi sekitar 6 jam yang lalu. Ini sudah sore."
    toby "Ah, benarkah? Saya tidak menyadari."
    scene expression ("images/episode2/051.webp") with dissolve
    patricia "Apa yang kamu tonton?"
    toby "Tidak yakin. Sesuatu di saluran sejarah."
    patricia "Membosankan."
    toby "Bagaimana sekolah?"
    scene expression ("images/episode2/052.webp") with dissolve
    patricia "Buruk sekali. Saya baru saja mengikuti kelas bahasa Inggris pertama saya dengan kepala sekolah. Awalnya saya tidak mengerti mengapa semua orang memanggilnya Ny. Wywhore."
    toby "Dan mengapa begitu?"
    patricia "Karena dia menyebalkan! Dia gila. Pena saya pecah, jadi saya meminta teman sekelas untuk membiarkan saya meminjam pena."
    patricia "When she saw us talking she was like \"{i}I don't know how your previous school was, but here when a teacher speaks everybody listens{/i}\". Aku sudah membencinya."
    scene expression ("images/episode2/053.webp") with dissolve
    patricia "Itu tidak lucu!"
    toby "Baik, baiklah. Itu tidak."
    scene expression ("images/episode2/054.webp") with dissolve
    toby "Dan selain bahasa Inggris, kelas apa lagi yang Anda miliki?"
    patricia "Nah, semuanya membosankan, kecuali PE."
    toby "Sejak kapan Anda suka olahraga?"
    patricia "Saya tidak, tapi saya baru saja mendengar rumor."
    toby "Katakan!"
    patricia "Ada desas -desus bahwa guru PE dulu menjadi penari telanjang!"
    toby "Tidak bisa benar. Maksudku, dia seorang guru, bagaimanapun juga. Saya yakin kepala sekolah akan memeriksa latar belakangnya sebelum mempekerjakannya."
    patricia "Maksud Anda kepala sekolah yang sekarang berada di penjara karena siapa yang tahu apa?"
    toby "Saya mengerti maksud Anda."
    scene expression ("images/episode2/055.webp") with dissolve
    patricia "Apakah Anda tahu cara memberikan pijat tangan?"
    toby "Bahkan jika saya melakukannya, mengapa menurut Anda saya akan memberi Anda satu?"
    scene expression ("images/episode2/056.webp") with dissolve
    patricia "Karena aku kecil [sister] dan tanganku sakit karena terlalu banyak tulisan."
    menu:
        "{i} [JGR] Beri dia pijat tangan {/i}"(csq="Tris +1 & Galeri Gambar"):
            $ patricia_rel += 1
            $ unlockImage(persistent.patricia_04)
            scene expression ("images/episode2/057.webp") with dissolve
            patricia "Terima kasih! Anda adalah yang terbaik [brother] yang bisa saya minta."
            toby "Apakah hanya itu yang kamu punya?"
            patricia "Dan aku mencintaimu?"
            toby "Saya akan mengambilnya."
            scene expression ("images/episode2/058.webp") with long_dissolve
        "{i} menolak untuk memberinya pijat tangan {/i}":

            scene expression ("images/episode2/059.webp") with dissolve
            toby "Bukan kesempatan."
            patricia "Anda yang terburuk [brother]."
            toby "Ya, ya!"
            scene expression ("images/episode2/060.webp") with dissolve
            patricia "Tapi saya masih menggunakan bahu Anda sebagai bantal."
            toby "Apa pun."
            scene expression ("images/episode2/061.webp") with long_dissolve

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She must be really tired if she fell asleep that fast.{/i}"
    scene expression ("images/episode2/062.webp") with shake
    toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n{i}Ouch!{/i}"
    scene expression ("images/episode2/063.webp") with dissolve
    patricia "Maaf! Maaf! Maaf! Saya merasa seperti jatuh dan ..."
    patricia "Apakah itu sakit?"
    toby "{size=12}{color=#FDCA6E}* in a low voice *{/color}{/size}\n{i}Maybe.{/i}"
    if patricia_rel >= 3:
        scene expression ("images/episode2/064.webp") with dissolve
        patricia "Apakah Anda ingin saya mencium booboo Anda?"
        toby "Saya pikir saya akan mengelola, tetapi lain kali saya tidak akan memaafkan Anda dengan mudah."
        scene expression ("images/episode2/065.webp") with dissolve
        patricia "Kamu rv! Anda akan membiarkan [sister] Anda mencium penis Anda?"
        toby "Saya tidak mengatakan itu, Anda hanya salah menafsirkan semuanya."
        scene expression ("images/episode2/066.webp") with dissolve
        toby "Satu -satunya di sekitar adalah Anda!"
        patricia "Saya tidak!"
    else:

        scene expression ("images/episode2/065.webp") with dissolve
        patricia "Apa yang ada di sana untuk menyakiti. Jika itu besar, saya akan merasakannya."
        toby "Ingin bertaruh?"
        patricia "Kamu rv! Anda akan menunjukkan penis Anda ke [sister] Anda?"
        patricia "Ewww. Orang cabul! Anda benar -benar membutuhkan pacar baru di sini di kota karena akhir -akhir ini, Anda sudah agak terangsang!"
        scene expression ("images/episode2/066.webp") with dissolve
        toby "Anda menyentuh penis saya, dan entah bagaimana saya adalah Perv."
        patricia "Itu kecelakaan!"

    scene expression ("images/episode2/067.webp") with dissolve
    toby "Saya akan tinggal lebih lama untuk berdebat dengan pervas seperti Anda, tetapi saya harus bersiap -siap untuk bekerja."
    patricia "Benar-benar? Anda sudah memulai?"
    scene expression ("images/episode2/068.webp") with dissolve
    if toby_job == 0:
        toby "Ho! Saya harus siap pada pukul 3:30 karena bos saya datang untuk menjemput saya."
        patricia "Dingin! Jadi pekerjaan mana yang akhirnya Anda ambil?"
        toby "Pekerjaan real estat. Saya akan menjadi agen real estat terbesar di kota!"
        patricia "Membosankan."
        scene expression ("images/episode2/069.webp") with dissolve
        toby "Jangan datang kepada saya meminta uang saat Anda menginginkan gaun baru!"
        patricia "Anda akan membelinya sendiri dan mengejutkan saya? Betapa bijaksana tentang Anda!"
        toby "Selamat tinggal!"
    else:

        toby "Ho! Saya harus siap pada pukul 3:30 karena seseorang datang untuk menjemput saya!"
        patricia "Dingin! Jadi pekerjaan mana yang akhirnya Anda ambil?"
        toby "Apakah saya terlihat seperti pria yang membosankan bagi Anda? Tentu saja saya memilih klub."
        patricia "Sekarang setelah Anda menyebutkannya, Anda terlihat agak membosankan. Aku tidak melihat apa yang dilihat wanita itu di dalam dirimu!"
        scene expression ("images/episode2/069.webp") with dissolve
        toby "Jangan datang kepada saya meminta uang saat Anda menginginkan gaun baru!"
        patricia "Anda akan membelinya sendiri dan mengejutkan saya? Betapa bijaksana tentang Anda!"
        toby "Selamat tinggal!"

    return

label episode2_realEstate:
    $ progress = 21


    scene expression ("images/episode2/070.webp") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/071.webp") with dissolve
    darlene "Hai [toby!c]. Apakah Anda siap untuk penjualan pertama Anda?"
    toby "Siap seperti yang pernah saya lakukan!"
    darlene "Sempurna! Mari kita pergi ke apartemen dan saya akan menjelaskan semuanya di sana."
    scene expression ("images/episode2/072.webp") with dissolve
    darlene "Jadi. Ini dia!"
    darlene "Ini adalah apartemen yang akan kami jual."
    darlene "Sebelum saya memberi Anda tur tempat itu, izinkan saya menjelaskan semuanya."
    darlene "Jadi kami akan bertemu di sini dengan dua wanita. Saya tidak tahu kedua nama mereka, tetapi orang yang sebenarnya ingin membeli apartemen ini adalah Lisa. Fokus kami adalah Lisa."
    scene expression ("images/episode2/073.webp") with dissolve
    darlene "Kami tidak terlalu peduli dengan yang lain. Lisa adalah orang dengan uang."
    darlene "Harga daftar untuk apartemen adalah 10.000, dan terendah yang dapat kami ambil adalah 00.000."
    darlene "Jika kita pergi di bawah 100k, kita akan mulai kehilangan uang, dan kita tidak menginginkannya."
    scene expression ("images/episode2/074.webp") with dissolve
    darlene "Apartemen ini memiliki satu kamar tidur, kamar mandi, dan ruang terbuka yang dapat digunakan sebagai dapur, ruang makan, dan ruang tamu."
    toby "Pertanyaan cepat, apakah ada ruang parkir dengan apartemen ini."
    darlene "Pertanyaan bagus. Apartemen ini memang datang dengan satu tempat parkir, tetapi jika klien bertanya, kami dapat menjual tempat kedua seharga, 000 karena kami memiliki seluruh bangunan."
    scene expression ("images/episode2/075.webp") with dissolve
    "Knock, ketukan."
    scene expression ("images/episode2/076.webp") with dissolve
    darlene "Mereka telah tiba. Jadi ingat, tidak lebih rendah dari 00.000."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why does she keep telling me that? I'm here just to watch!{/i}"

    scene expression ("images/episode2/077.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    woman "Hai. Kami berbicara di telepon tentang apartemen."
    scene expression ("images/episode2/078.webp") with dissolve
    darlene "Anda pasti Lisa, kan?"
    lisa "Ya."
    darlene "Dan wanita cantik ini?"
    lauren "Lauren."
    scene expression ("images/episode2/079.webp") with dissolve
    darlene "Sayangnya, saya memiliki sesuatu yang mendesak yang membutuhkan perhatian saya.Jadi ini [toby!c]. Dia agen terbaik kami. Dia akan menjadi orang yang menunjukkan apartemennya."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Say what? I'm her best agent my ass. It's my first day!{/i}"
    scene expression ("images/episode2/080.webp") with dissolve
    darlene "Dia tipe pria yang bisa mengurus semuanya."
    scene expression ("images/episode2/081.webp") with dissolve
    darlene "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I let him take care of everything and I'm always satisfied, so you're in good hands.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the fuck is she talking about? I thought the crazy one was Kat, not her!{/i}"
    menu:
        "{i} Cobalah untuk bertindak normal {/i}":
            scene expression ("images/episode2/082.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I said... Act normal. Does this look normal to you?{/i}"
        "{i} [JGR] Mainkan {/i}"(csq="Darlene +1 & Galeri Gambar"):

            $ darlene_rel += 1
            $ ep2_spankDarlene = True
            $ unlockImage(persistent.darlene_03)
            scene expression ("images/episode2/083.webp") with dissolve
            toby "Saya akan mengurus semuanya dari sini."
            scene expression ("images/episode2/084.webp") with dissolve
            toby "Aku akan meneleponmu begitu apartemen dijual!"
            pass

    scene expression ("images/episode2/085.webp") with dissolve
    darlene "Oke kalau begitu. Aku akan meninggalkanmu!"
    scene expression ("images/episode2/086.webp") with dissolve
    toby "Maaf untuk itu!"
    toby "Jadi izinkan saya menunjukkan Anda di sekitar apartemen."
    lisa "Jangan khawatir."
    scene expression ("images/episode2/087.webp") with dissolve
    lauren "Jadi seberapa bagus di tempat tidur Anda?"
    toby "Permisi?"
    lisa "Diam, Lauren."
    scene expression ("images/episode2/088.webp") with dissolve
    lauren "Bisa aja. Lihat dia. Dia tidak lebih tua dari kita, namun dia meniduri bosnya yang 20 tahun lebih tua dari dia. Dia pasti awam yang hebat."
    toby "Uhum ya. Seperti yang saya katakan, izinkan saya menunjukkan kepada Anda di sekitar apartemen."
    scene expression ("images/episode2/089.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Will all the sales be this awkward?{/i}"

    show screen ui_message("A short time later") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/090.webp") with long_dissolve
    hide screen ui_message
    $ progress = 22
    toby "Jadi? Bagaimana menurutmu?"
    lisa "Saya sangat menyukainya. Inilah yang saya cari. Jadi berapa harga yang diminta lagi?"
    toby "Nah, apartemen ini bernilai 20.000, tetapi untuk seseorang yang pintar dan cantik seperti Anda, saya bisa turun menjadi 10.000. Apa yang kamu katakan?"

    scene expression ("images/episode2/091.webp") with dissolve
    lisa "Benar-benar? Anda melakukan itu untuk kami?"
    lisa "Terima kasih!"
    toby "Tolong jangan beri tahu bos saya alasan saya turun 10k."
    scene expression ("images/episode2/092.webp") with dissolve
    lauren "Tidak begitu cepat. Karena Anda bisa turun 10k begitu saja, saya yakin Anda bisa melakukan yang lebih baik!"
    toby "Tidak terlalu."
    scene expression ("images/episode2/093.webp") with dissolve
    lauren "Anda sedang bernegosiasi dengan saya sekarang."
    toby "Uhm ..."
    scene expression ("images/episode2/094.webp") with dissolve
    lauren "Jadi apa yang Anda katakan. Bagaimana suara 109k?"
    scene expression ("images/episode2/095.webp") with dissolve
    lisa "Tolong beritahu saya bahwa Anda tidak akan menghisapnya."
    scene expression ("images/episode2/096.webp") with dissolve
    lauren "Mengapa tidak? Dia tampan, dan selain itu, saya ingin tahu seberapa besar kemaluannya karena bosnya sangat menyukainya!"

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is she really going to blow me in front of her friend? This chick is crazy.{/i}"
    scene expression ("images/episode2/097.webp") with dissolve
    lauren "So what do you say, \"Mr. employee of the month\", bisakah saya melanjutkan dengan negosiasi?"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I cannot negotiate with both of them. What should I do?{/i}"
    scene expression ("images/episode2/097_lisa.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}If I am going to win Lisa over I'll need to reject her friend. She looks like she's had enough of her silly antics.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's more mature and by the looks of things, she's more into charming nice guys, not someone who's willing to get blown by any girl who offers.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I need to be polite and flirt in a classy, respectful way.{/i}"
    scene expression ("images/episode2/097_lauren.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}On the other hand, her friend is already on her knees, ready to suck my cock.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She must come from a poor family and since she can't compete with Lisa on the money side, she tries to balance it by doing stupid shit like this.{/i}"
    menu:
        "{i} Biarkan Lauren melakukan pekerjaannya {/i} [JLA]"(csq="Lauren +1 & Galeri Gambar"):
            label memory_04:
                $ unlockImage(persistent.lauren_01)

                $ lauren_path = True
                $ ep2_laurenBlowjob = True
                $ lauren_rel += 1
                if _in_replay:
                    scene expression ("images/episode2/097_lauren.webp") with dissolve
                toby "Jadi itu 109k saat ini."
                scene expression ("images/episode2/098.webp") with dissolve
                lauren "Cukup bagus untukku!"
                scene expression ("images/episode2/099.webp") with dissolve
                lauren "108k."
                scene expression ("images/episode2/100.webp") with dissolve
                lauren "107k."
                toby "Apakah Anda tidak terlalu cepat dengan uang?"
                scene expression ("images/episode2/101.webp") with dissolve
                lauren "Saya tahu betapa bernilai mulut saya. Anda menikmati, Tn."
                scene expression ("images/episode2/102.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode2/103.webp") with dissolve
                lauren "106k!"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}If she's keeps going like this, I might end up paying her to buy this apartment.{/i}"
                scene expression ("images/episode2/104.webp")
                show ep2_104
                lauren "Apakah Anda suka handjobs, Tn. [toby!c]?"
                toby "Siapa yang tidak?"
                lauren "Dingin! Kalau begitu, itu 105k."
                scene expression ("images/episode2/105.webp")
                hide ep2_104
                show ep2_105
                toby "Biarkan saya menebak. 104k?"
                lauren "Anda benar!"
                scene expression ("images/episode2/106.webp")
                hide ep2_105
                show ep2_106
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck me, this is the best blowjob ever.{/i}"
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode2/107.webp")
                hide ep2_106
                show ep2_107
                toby "Aku akan segera cum!"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She looks like she's going to let me cum in her mouth. Which will probably cost another grand.{/i}"
                scene expression ("images/episode2/108.webp") with dissolve
                with flash
                with flash
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode2/109.webp") with dissolve
                lauren "Itu akan menjadi 2K lagi."
                lauren "Haruskah saya menelan?"
                toby "Saya merasa seperti negosiator terburuk yang pernah ada, tapi ya!"
                scene expression ("images/episode2/110.webp") with dissolve
                lauren "Anda mungkin, karena itu hanya biaya 1k lagi."
                toby "Jadi harga akhir 101k?"
                scene expression ("images/episode2/111.webp") with dissolve
                lauren "Itu benar sayangku."

                $ unlockMemory(persistent.memory_04)
                $ renpy.end_replay()

            scene expression ("images/episode2/112.webp") with dissolve
            lisa "Aku bisa menciummu sekarang, tapi kurasa aku akan menunggu sampai kamu mencuci mulut kotor itu."
        "{i} fokus pada lisa {/i} [JLI]"(csq="Lisa +1 & Galeri Gambar"):

            $ unlockImage(persistent.lisa_01)
            $ lisa_path = True
            $ lisa_rel += 1

            scene expression ("images/episode2/114.webp") with dissolve
            toby "Saya maafkan maaf, tapi saya lebih suka bernegosiasi dengan teman Anda. Saya mencoba untuk tidak mencampur seks dengan bisnis."
            scene expression ("images/episode2/115.webp") with dissolve
            lisa "Astaga! Anda adalah yang terbaik. Dia tidak terbiasa ditolak."
            scene expression ("images/episode2/116.webp") with dissolve
            lauren "Saya mengerti, Anda lebih suka membiarkan Lisa mengisap penis Anda. Dia sangat terampil dalam hal itu, saya yakin!"
            scene expression ("images/episode2/117.webp") with dissolve
            lisa "Lauren !!!"
            scene expression ("images/episode2/118.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This is getting really, really awkward.{/i}"
            toby "Mari kita katakan bahwa dia bisa memberi saya ciuman di pipi dan harganya akan 100k."
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Stupid, stupid, stupid. You idiot! This is how you negotiate?{/i}"
            scene expression ("images/episode2/119.webp") with dissolve
            lisa "Umm ... oke!"
            scene expression ("images/episode2/120.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode2/121.webp") with dissolve
            toby "Senang berbisnis dengan Anda."
            lisa "Saya juga!"
            scene expression ("images/episode2/122.webp") with dissolve
            lauren "Oh, ayolah! Bung saja memberi Anda diskon 0.000! Paling tidak yang bisa Anda lakukan adalah menciumnya. Jelaslah bahwa apa yang diinginkannya."
            scene expression ("images/episode2/121.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}You really don't have to do that. It's fine.{/i}"
            scene expression ("images/episode2/123_1.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode2/123.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Well, this was unexpected!{/i}"
            scene expression ("images/episode2/124.webp") with dissolve
            lisa "Jadi, apakah Anda pikir Anda bisa menjual apartemen kepada saya seharga 01k, bukan 00k? Saya merasa sedikit bersalah karena memanfaatkan Anda!"
            toby "Tentu saja. Jika itu yang Anda inginkan."
            scene expression ("images/episode2/125.webp") with dissolve
            lauren "Kalian berdua dibuat untuk satu sama lain."

    scene expression ("images/episode2/113.webp") with dissolve
    $ progress = 23
    lisa "Jadi kami punya kesepakatan. 01.000 untuk apartemen?"
    toby "Itu benar."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}If Darlene finds out what happened here she'll fire me!{/i}"
    scene expression ("images/episode2/126.webp") with dissolve
    toby "Oke kalau begitu. Saya perlu berbicara dengan bos saya tentang surat -surat, tetapi Anda dapat datang ke kantor kami besok, dan kami akan menyelesaikan semuanya untuk Anda."
    lisa "Terima kasih, Pak!"
    toby "Panggil saja aku [toby!c]."
    lisa "Terima kasih [toby!c]."
    toby "Tidak masalah. Dengan senang hati."
    scene expression ("images/episode2/127.webp") with dissolve
    lauren "Bye Sexy! Sampai besok."
    lisa "Sampai jumpa besok, [toby!c]!"
    toby "Selamat tinggal!"

    scene expression ("images/episode2/128.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Now how am I going to explain this to Darlene?{/i}"
    if ep2_spankDarlene == True:
        scene expression ("images/episode2/129.webp") with dissolve
        darlene "Jika Anda pernah menyentuh pantat saya lagi, saya akan memotong ayam Anda dan memberi makan untuk anjing."
        toby "Maaf ma \ 'am. Saya hanya mencoba untuk ..."
        darlene "Saya tidak peduli. Saya bos Anda, dan Anda tidak diizinkan menyentuh pantat saya!"
        toby "Maaf ma \ 'am!"
    scene expression ("images/episode2/130.webp") with dissolve
    darlene "Jadi izinkan saya menebak. Anda gagal menjual apartemen?"
    toby "TIDAK! Ya. Hanya saja itu bukan harga yang saya harapkan!"
    darlene "Seberapa jauh Anda pergi?"
    scene expression ("images/episode2/131.webp") with dissolve
    toby "01.000."
    darlene "Dan Anda kecewa dengan itu?"
    toby "Haruskah aku?"
    darlene "Harga untuk apartemen ini benar -benar 0.000. Fakta bahwa Anda berhasil menjualnya seharga 00.000 adalah keuntungan besar."
    darlene "Saya membeli apartemen ini seharga 0,000, dan sejak itu pasar naik, tetapi belum mencapai 00.000."
    darlene "Jadi bagi saya, itu adalah untung sebesar 0.000."
    scene expression ("images/episode2/132.webp") with dissolve
    toby "Maksudmu 1.000!"
    darlene "Tidak. Itu potongan Anda!"
    toby "Tapi saya pikir Anda mengatakan pemotongan saya adalah 20 %% dari laba."
    scene expression ("images/episode2/133.webp") with dissolve
    darlene "Apa yang bisa saya katakan. Saya sangat buruk dengan matematika hari ini!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Should I be upset that she screwed me? Or should I be happy that I just made a grand in 30 minutes?{/i}"
    scene expression ("images/episode2/134.webp") with dissolve
    darlene "Menurut Anda apa yang Anda lakukan?"
    toby "Maaf ma \ 'am. Saya pikir Anda akan membawa saya pulang."
    darlene "Tidak, saya tidak. Anda akan pulang ke rumah."
    toby "Tapi saya tidak punya mobil."
    scene expression ("images/episode2/135.webp") with dissolve
    darlene "Tapi Anda memiliki sepeda."
    scene expression ("images/episode2/136.webp") with dissolve
    toby "Apakah kamu serius?!"
    darlene "Saya harap Anda tahu cara mengendarai salah satunya. Dan jika Anda benar -benar menginginkan mobil mewah seperti milik saya, Anda harus menjadi lebih baik."
    menu:
        "{i} [JGR] Flirt {/i}"(csq="Darlene +1"):
            scene expression ("images/episode2/137.webp") with dissolve
            $ darlene_rel += 1
            toby "Maksudmu baik dalam menjual maupun di tempat tidur?"
            darlene "Jangan dorong keberuntungan Anda!"
        "{i} don \ 't flirt {/i}":

            pass
    scene expression ("images/episode2/138.webp") with dissolve
    toby "Terima kasih untuk sepeda!"
    darlene "Terima kasih atas penjualannya."
    toby "Dengan senang hati!"
    darlene "Oh, dan omong -omong, datanglah ke kantor besok sehingga kami bisa mendapatkan surat ketenagakerjaan Anda dan saya bisa mengajari Anda lebih banyak tentang pekerjaan itu."
    toby "Oke!"
    return


label episode2_club:

    $ progress = 21
    scene expression ("images/episode2/070.webp") with long_dissolve


    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/139.webp") with dissolve
    toby "Permisi Pak, apakah Nyonya Katrina mengirimmu?"
    neal "Ya. I \ 'M Neal. Melompat."
    neal "Dan jangan membanting pintu!"
    scene expression ("images/episode2/140.webp") with dissolve
    neal "Nyonya Katrina memberi tahu saya bahwa Anda baru di kota."
    toby "Ya. Saya baru saja pindah ke sini beberapa hari yang lalu."
    neal "Dan? Bagaimana Anda menyukainya sejauh ini?"
    toby "Tidak bisakah saya bilang saya punya waktu untuk melihat banyak. Itu terlihat menarik. Satu -satunya tempat yang sejauh ini adalah pantai."
    neal "Katakan padaku kamu pergi ke sana pada akhir pekan."
    toby "Tidak, itu kemarin."
    scene expression ("images/episode2/141.webp") with dissolve
    neal "Anda harus pergi pada hari Sabtu. Gadis -gadis di sana adalah yang terbaik."
    neal "Kamu menjadi perempuan, kan?"
    toby "Uhum, ya!"
    neal "Bagus."
    neal "Ngomong -ngomong, kita perlu berhenti sebentar sebelum pergi ke Nyonya Katrina."
    toby "Ya, tentu. Tidak masalah."
    scene expression ("images/episode2/142.webp") with dissolve
    neal "Beri aku bagian dari kompartemen sarung tangan."
    toby "Bagian?"
    scene expression ("images/episode2/143.webp") with dissolve
    neal "Anda tidak pernah memegang senjata sebelumnya?"
    toby "Tidak, saya punya. Itu hanya itu ..."
    neal "Cobalah untuk tidak melukai diri sendiri dengan itu."
    scene expression ("images/episode2/144.webp") with dissolve
    neal "Saya akan segera kembali. Jangan pergi ke mana pun."
    scene expression ("images/episode2/145.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the fuck is going on? What have I gotten myself into?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is this going to be my new normal from now on? \"Pass me the gun.\" \"Here, hold this kilo of coke.\"{/i}"

    show screen ui_message("Five minutes later") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode2/146.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}The hell!? Why does he have a wad of cash in his hand? Did he fucking rob the place?{/i}"
    scene expression ("images/episode2/147.webp") with dissolve
    neal "Hitung ini untukku!"
    toby "Uhum ... Tentu!"
    scene expression ("images/episode2/148.webp") with dissolve
    toby "Ini, 000. Di mana saya harus meletakkannya?"
    neal "Sembunyikan itu baik dan berikan kepada Katrina saat Anda melihatnya."
    toby "Apakah Anda yakin ini adalah hal yang benar untuk dilakukan?"
    neal "Tentu saja. Jika seseorang menangkap kami, Anda punya uang. Ini hal yang benar untuk dilakukan!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yeah, for you!{/i}"
    scene expression ("images/episode2/149.webp") with long_dissolve
    toby "Hai ma \ 'am. Bolehkah saya masuk?"


    scene expression ("images/episode2/150.webp") with dissolve
    katrina "[toby!c]. Datang, ini anakku! Senang sekali Anda memutuskan untuk bergabung dengan kami."
    scene expression ("images/episode2/151.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What The hell? She's going to kiss me, just like that?{/i}"
    scene expression ("images/episode2/152.webp") with dissolve
    katrina "Bagaimana perjalanan Anda!"
    menu:
        "{i} [JGR] Lihat pantatnya {/i}"(csq="Katrina +1 & Gambar Galeri"):
            $ katrina_rel += 1
            $ unlockImage(persistent.katrina_03)
            scene expression ("images/episode2/153.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What an ass... This woman's gonna be the death of me.{/i}"
            katrina "Jadi?"
            scene expression ("images/episode2/154.webp") with dissolve
            katrina "Mata!"
            toby "Maaf aku..."
            katrina "Saya berkata, bagaimana perjalanannya? Apakah Neal berperilaku?"
        "{i} menjadi anak yang baik {/i}":
            pass
    toby "Uhum. Ya, semuanya baik -baik saja. Dia memintaku untuk memberimu ini."
    scene expression ("images/episode2/155.webp") with dissolve
    katrina "Beri aku apa?"
    toby "Umm ... dia memintaku untuk memberimu genggam, tapi aku tidak bisa menemukannya! Pasti jatuh di dalam mobil!"
    toby "Aku akan segera kembali!"
    scene expression ("images/episode2/156.webp") with dissolve
    katrina "Mencari sesuatu?"
    toby "Bagaimana kamu ...?"
    katrina "Anda harus memiliki kontrol lebih besar saat seseorang mencium Anda!"
    scene expression ("images/episode2/157.webp") with dissolve
    katrina "Tolong duduklah dan izinkan saya menjelaskan pekerjaan Anda di sini."
    toby "Maaf ma \ 'am. Saya tidak ingin bersikap kasar, tetapi saya tidak yakin ini adalah pekerjaan yang tepat untuk saya."
    katrina "Saya mengatakan kepada Anda untuk memanggil saya Katrina dan membiarkan saya mengejanya untuk Anda!"
    scene expression ("images/episode2/158.webp") with dissolve
    katrina "Baik!"
    katrina "Jadi! Kata mana yang lebih Anda sukai, tes, atau lelucon?"
    toby "Arti?"
    katrina "Oke, pistol Neal memintamu untuk memberinya palsu. Saya hanya ingin memastikan Anda tidak akan menelepon polisi setiap kali Anda melihat sesuatu yang teduh."
    katrina "Kami memiliki klub, dan di sini hal -hal yang teduh akan terjadi, tetapi kami ingin menyimpannya di rumah kami. Kami ingin membiarkan keamanan kami sendiri menangani berbagai hal karena jika polisi terlibat, kami kehilangan uang. Dan apakah kita ingin kehilangan uang?"
    scene expression ("images/episode2/159.webp") with dissolve
    toby "Tidak, kami tidak!"
    scene expression ("images/episode2/160.webp") with dissolve
    katrina "Saya ingin melihat bagaimana Anda akan bereaksi jika Anda tahu bahwa Anda harus memberi saya genggam dan Anda tidak dapat menemukannya. Apakah Anda cukup pria untuk mengakui kesalahan Anda?Tepat! Kami tidak. Lalu uangnya ... Saya hanya ingin memastikan saya bisa mempercayai Anda dengan uang."
    katrina "Dan saya suka bagaimana Anda menanganinya. Anda tahu risiko kehilangan uang saya karena Anda melihat senjata hanya beberapa menit yang lalu!"
    katrina "Kemudian saya ingin melihat seberapa baik Anda dengan gadis -gadis itu, dan Anda jelas kurang konsentrasi. Jika seorang gadis mencium Anda, Anda kehilangan fokus, yang tidak bagus!"
    katrina "Tapi kami akan mengerjakannya."
    scene expression ("images/episode2/161.webp") with dissolve
    toby "Jadi semuanya hanya tes?"
    katrina "Tepat! Dan kamu lulus!"
    katrina "Sekarang, mari kita bicara tentang pekerjaan Anda."
    katrina "Kami membutuhkan pria tampan untuk bertindak seperti klien palsu. Tugas Anda adalah berjalan di sekitar klub dan mengundang gadis -gadis ke dalam. Membuat mereka merasa istimewa dan diinginkan."
    toby "Jadi saya tidak bisa bergabung dalam kesenangan di klub?"
    katrina "Tidak terlalu. Karena kadang -kadang ada gadis -gadis dalam kelompok kecil yang masih memiliki lebih banyak teman di rumah, jadi pekerjaan Anda adalah menggoda gadis -gadis itu dan membuat mereka mengundang teman -teman mereka di lain waktu."
    toby "Saya mengerti!"
    scene expression ("images/episode2/162.webp") with dissolve
    toby "Dan Anda ingin memiliki wanita di klub karena jika ada gadis -gadis cantik di klub, maka banyak pria akan datang, dan mereka bersedia membeli banyak minuman mahal hanya untuk mengesankan mereka."
    katrina "Tepat! Saya tahu Anda adalah pria yang cerdas."
    katrina "Juga, Anda harus memastikan bahwa gadis -gadis tidak pergi karena idiot cowok. Anda akan menjadi ksatria mereka dalam baju besi yang bersinar."
    toby "Dan bagaimana jika membuat seorang gadis merasa istimewa, saya harus membeli minumannya?"
    katrina "Saya akan memperkenalkan Anda kepada staf, dan mereka akan memberi Anda apa pun yang Anda butuhkan. Pakaian, alkohol, narkoba, apa pun yang dibutuhkan gadis -gadis itu."
    scene expression ("images/episode2/163.webp") with dissolve
    toby "Saya benar -benar tidak ingin terlibat dengan narkoba. Saya bersih dan tidak ingin kembali ke narkoba lagi."
    katrina "Anda tidak harus melakukannya, tetapi beberapa orang suka mengkonsumsi ketika mereka ingin berpesta."
    toby "Tetapi bukankah ilegal menjual narkoba di klub? Anda bisa kehilangan lisensi Anda!"
    scene expression ("images/episode2/164.webp") with dissolve
    katrina "Tentu saja itu, tetapi Anda tidak melakukan pengedar narkoba. Anda tidak menjualnya. Anda akan memberikannya secara gratis, tetapi hanya untuk para wanita."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This is pretty fucked up!{/i}"
    scene expression ("images/episode2/165.webp") with dissolve
    katrina "Izinkan saya menunjukkan Anda dan melihat apakah ada gadis di klub."
    toby "Ini adalah Selasa malam. Berapa banyak gadis yang bisa berada di klub pada hari Selasa?"
    katrina "Biasanya ada beberapa orang yang datang untuk minum, merokok, dan mengobrol pada hari kerja, tetapi pada akhir pekan, itu cerita lain!"

    show screen ui_message("A short time later") with dissolve
    $ ui.saybehavior()
    $ ui.interact()


    scene expression ("images/episode2/166.webp") with long_dissolve
    hide screen ui_message
    $ progress = 22
    katrina "Jadi? Bagaimana menurutmu? Anda menyukai tempat ini?"
    toby "Uhum, ya! Ini bagus, tapi ada satu hal yang perlu saya tanyakan kepada Anda."
    katrina "Biarkan saya menebak, uangnya?"
    toby "Ya."
    katrina "Saya akan mengawasi Anda dan melihat berapa banyak gadis yang telah Anda ajak bicara, kacau, atau berapa banyak yang mengisap ayam Anda di bawah meja."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She sounds like a pervert!{/i}"
    scene expression ("images/episode2/167.webp") with long_dissolve
    katrina "Saya bercanda. Anda akan mendapatkan persentase dari penjualan. Jangan khawatir, itu akan baik -baik saja, sekarang mari kita lihat seberapa baik Anda dengan para wanita."
    katrina "Apakah Anda punya pacar?"
    toby "Ya, tapi dia kembali ke rumah."
    katrina "Anda tinggal dengan pacar Anda, dan dia baik -baik saja dengan Anda bekerja di klub sebagai wingman? Bagus! Saya menyukainya."
    toby "Tidak ... Maksudku, dia tinggal di Rictown, tapi ya, dia tidak tahu aku akan bekerja di sini. Saya tidak punya kesempatan untuk memberitahunya."
    scene expression ("images/episode2/168.webp") with dissolve
    katrina "Menarik. Jangan memberitahunya. Dia tidak perlu tahu!"
    katrina "Tunjukkan gambar."
    toby "Apakah itu benar -benar perlu?"
    katrina "Ya! Saya ingin melihat tipe Anda."
    scene expression ("images/episode2/169.webp") with dissolve
    katrina "Sayang sekali kamu menjadi pirang. Saya benar -benar berpikir kami memiliki sesuatu."
    katrina "Nah, begitulah adanya!"
    scene expression ("images/episode2/170.webp") with dissolve
    katrina "Di belakang Anda, dua gadis baru saja masuk. Salah satunya adalah seorang pirang, sama seperti Anda seperti mereka. Bicaralah dengan mereka dan dapatkan nomornya."
    scene expression ("images/episode2/171.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    katrina "Sebenarnya, nah. Anda tidak punya kesempatan dengannya. Dapatkan nomor telepon teman."
    toby "Saya berani bertaruh Anda bahwa memberi Anda mencuri dari saku saya bahwa saya bisa mendapatkan nomornya."
    katrina "Pergi \ mereka, Tiger. Anda telah mendapatkan kesepakatan!"
    scene expression ("images/episode2/172.webp") with dissolve
    toby "Hei, saya akan memberi Anda 50 dolar jika Anda berbicara dengan para wanita di sana."
    guy "Mengapa saya melakukan itu?"
    scene expression ("images/episode2/173.webp") with dissolve
    toby "Karena jika tidak, pemilik akan meminta untuk berbicara dengan Anda!"
    scene expression ("images/episode2/174.webp") with dissolve
    guy "Apakah Anda kenal Ny. Katrina?"
    toby "Bagaimana menurutmu? Tentu saja!"
    guy "Oke, saya akan pergi. Apa yang harus saya katakan kepada mereka?"
    toby "Beri mereka garis penjemputan Anda yang paling aneh!"
    scene expression ("images/episode2/175.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Poor guy. He doesn't know what's about to happen to him.{/i}"
    scene expression ("images/episode2/176.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Time for [toby!c] to shine!{/i}"
    scene expression ("images/episode2/177.webp") with dissolve
    toby "Maaf saya terlambat, nona. Saya hanya harus menyelesaikan beberapa bisnis!"
    scene expression ("images/episode2/178.webp") with dissolve
    toby "Di sini lima puluh dolar, belilah diri Anda sesuatu yang bagus, mungkin buku dari jalur pickup yang lebih baik!"
    guy "Persetan denganmu!"
    scene expression ("images/episode2/179.webp") with long_dissolve
    girl "Wow, itu sangat keren!"
    girl "Sekarang, siapa yang akan menyingkirkanmu?"
    scene expression ("images/episode2/180.webp") with dissolve
    toby "Jangan khawatir, cantik, aku akan pergi segera setelah pria itu berjarak 50 kaki. Saya tidak punya niat untuk membuang -buang waktu Anda!"
    scene expression ("images/episode2/181.webp") with dissolve
    toby "Tidak bermaksud menyinggung. Tapi saya yakin Anda menyenangkan!"
    scene expression ("images/episode2/182.webp") with dissolve
    lauren "Saya Lauren, dan saya menghibur jika Anda benar -benar ingin tahu."
    scene expression ("images/episode2/183_1.webp") with dissolve
    toby "Dan saya [toby!c]. Di layanan Anda."
    scene expression ("images/episode2/183_2.webp") with dissolve
    lisa "Dan aku lisa. Sekarang bisakah Anda meninggalkan kami sendirian?"
    scene expression ("images/episode2/184.webp") with dissolve
    toby "Jika wanita itu ingin ... sampai jumpa, cantik!"
    lauren "Tapi bagaimana jika wanita lain ingin Anda tinggal?"
    scene expression ("images/episode2/185.webp") with dissolve
    toby "Lalu aku akan tinggal sedikit lebih lama."
    toby "Jadi, katakan padaku, Lauren! Apa yang membuatmu sangat menyenangkan?"
    lauren "Katakan saja aku fantastis di tempat tidur."
    scene expression ("images/episode2/186.webp") with dissolve
    toby "Dan? Anda tidak?"
    lisa "Saya mungkin, tetapi tidak seperti teman saya di sana, saya tidak meniup setiap pria yang saya temui."
    scene expression ("images/episode2/187.webp") with dissolve
    toby "Ewww ... kamu pasti jahat!"
    lauren "Anda tidak tahu!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I can't flirt with both of them. I need to focus only on one.{/i}"
    scene expression ("images/episode2/188.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Judging by her attitude, she must be rich and she's had loads of guys trying to hit on her.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She must be tired of the shallow, horny approach. If I'm going to make a move on her, I should be a gentleman.{/i}"
    scene expression ("images/episode2/189.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She likes to be the center of attention. She'd do anything for a little bit of fun. I think she's very insecure about everything.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She cannot compete with her friend on so many levels, so she's trying make up for it by being more outgoing.{/i}"
    menu:
        "{i} fokus pada lisa {/i} [JLI]"(csq="Lisa +1 & Galeri Gambar"):
            $ lisa_rel += 1
            $ lisa_path = True
            $ unlockImage(persistent.lisa_02)

            scene expression ("images/episode2/190.webp") with dissolve
            toby "Maaf cantik, tapi saya bukan tipe pria yang membawa seorang gadis di kamar mandi dan menidurinya setelah mengenalnya hanya 10 menit. Saya tipe pria yang suka pergi berkencan dan jatuh cinta."
            scene expression ("images/episode2/191.webp") with dissolve
            toby "Tetapi untuk itu, saya akan membutuhkan nomor Anda sehingga saya dapat mengajak Anda keluar!"
            scene expression ("images/episode2/192.webp") with dissolve

            lauren "Anda adalah babi seperti itu! Ini adalah penolakan terindah dan menyakitkan yang pernah saya terima."
            scene expression ("images/episode2/193.webp") with dissolve
            lisa "Jika Anda membiarkannya menampar Anda sekali lagi, saya bahkan bersedia memberi Anda ciuman di pipi."
            toby "Saya bisa mengambil apa pun yang bisa Anda lempar ke saya."
            scene expression ("images/episode2/194.webp") with dissolve
            lauren "Aku akan menamparmu jika kamu tidak akan mencium pria ini di bibirnya!"
            scene expression ("images/episode2/195_1.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}A kiss on the cheek will be just fine.{/i}"
            scene expression ("images/episode2/195_2.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode2/195_3.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is she going for the lips?{/i}"
            scene expression ("images/episode2/196.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wasn't expecting that!{/i}"
            scene expression ("images/episode2/197.webp") with dissolve
            lisa "Telepon saya!"
            scene expression ("images/episode2/198.webp") with dissolve
            toby "Oh, saya akan!"
            toby "Saya membiarkan kalian berdua menikmati sisa malam Anda. Senang bertemu denganmu!"
            lisa "Bye [toby!c]."
            lauren "Sampai jumpa, babi tampan!"
        "{i} fokus pada lauren {/i} [JLA]"(csq="Lauren +1 & Galeri Gambar"):

            $ unlockImage(persistent.lauren_02)
            $ lauren_rel += 1
            $ lauren_path = True
            $ ep2_laurenBlowjob = True
            scene expression ("images/episode2/199.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I'll be waiting for you in the bathroom.{/i}"
            scene expression ("images/episode2/200.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I hope I didn't make a fool out of myself. What if she doesn't come!{/i}"

            label memory_05:
                scene expression ("images/episode2/201.webp") with dissolve

                lauren "Merindukanku?"
                scene expression ("images/episode2/201_1.webp") with dissolve
                toby "Anda tidak tahu!"
                scene expression ("images/episode2/201_2.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode2/202.webp") with dissolve:
                    yalign 1.0
                    linear 10.0 yalign 0.0

                $ ui.pausebehavior(9.3)
                $ ui.saybehavior()
                $ ui.interact()
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This girl is crazy!{/i}"
                scene expression ("images/episode2/203.webp") with dissolve
                lauren "Sial ... itu sangat besar!"
                scene expression ("images/episode2/204.webp")
                show ep2_204
                toby "Anda gila! Anda tahu itu, kan?"
                lauren "Anda baru saja bertemu saya. Anda akan melihat betapa gilanya saya."
                scene expression ("images/episode2/205.webp")
                hide ep2_204
                show ep2_205
                toby "Jika saya akan melihat lebih banyak seperti ini, saya tidak bisa menunggu!"
                scene expression ("images/episode2/206.webp")
                hide ep2_205
                show ep2_206
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... This is so good!{/i}"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I never had a blowjob like this.{/i}"
                scene expression ("images/episode2/207.webp")
                hide ep2_206
                show ep2_207
                toby "Saya akan pergi ke cum!"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Of course she's not stopping. Why would she!{/i}"
                scene expression ("images/episode2/208.webp") with dissolve
                hide ep2_207
                with flash
                with flash
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Damn... This was so, so good!{/i}"
                scene expression ("images/episode2/209.webp") with dissolve
                lauren "Jika Anda ingin saya menelan, Anda harus berjanji untuk menelepon saya."
                toby "Selama Anda memberi saya nomor Anda!"
                scene expression ("images/episode2/210.webp") with dissolve
                lauren "Kesepakatan!"
                scene expression ("images/episode2/211.webp") with dissolve
                lauren "Di sini, saya akan menunggu panggilan Anda!"
                toby "Dengan senang hati!"
                scene expression ("images/episode2/212.webp") with dissolve
                lauren "Sampai jumpa nanti, tampan."
                toby "Sampai jumpa nanti, seksi."

                $ unlockMemory(persistent.memory_05)
                $ renpy.end_replay()

    $ progress = 23
    scene expression ("images/episode2/213.webp") with dissolve

    katrina "Jadi? Bagaimana hasilnya?"
    if lisa_rel == 1:
        scene expression ("images/episode2/214.webp") with dissolve
        toby "Bagaimana menurutmu? Tentu saja, saya berhasil mendapatkan nomornya!"
        katrina "Anda mendapatkan nomornya? Dia juga menciummu. Sejujurnya, jujur saja. Tidak ada orang lain yang berhasil melakukannya pada hari pertama mereka."
    else:
        toby "Tidak cukup. Saya berhasil mendapatkan nomor temannya."
        katrina "Apa yang Anda lakukan di kamar mandi?"
        toby "Dia mengejutkanku."
        katrina "Tidak buruk sama sekali. Tidak ada orang lain yang berhasil melakukannya pada hari pertama mereka."

    scene expression ("images/episode2/213.webp") with dissolve
    toby "Benar-benar? Apakah ada yang disebut Wingmen lain yang bekerja untuk Anda?"
    katrina "Tidak lagi. Ada satu, tapi dia sama sekali tidak berguna!"
    toby "Jadi, apakah saya memenangkan taruhan?"

    if lisa_rel == 1:
        scene expression ("images/episode2/215.webp") with dissolve
        katrina "Di sini ... Anda mendapatkannya!"
    else:

        scene expression ("images/episode2/215.webp") with dissolve
        katrina "Anda kehilangan taruhan, tetapi Anda masih pantas mendapatkan uang."

    toby "Terima kasih, ma \ 'am."
    toby "Maksudku, Katrina."
    katrina "Panggil saja aku Kat. Anda adalah pria favorit saya sekarang!"
    toby "Dingin!"
    scene expression ("images/episode2/216.webp") with dissolve
    katrina "Anda bebas untuk pulang sekarang."
    katrina "Ada sepeda motor yang menunggumu. Kuncinya adalah dalam kunci kontak. Itu milikmu sekarang."
    toby "Apakah Anda buang air besar?"
    katrina "Tenang. Ini tidak seperti saya memberi Anda supercar."
    toby "Ya, tapi itu masih sesuatu!"
    katrina "Anda bisa mengatakan itu!"
    toby "Senang berbisnis dengan Anda!"
    katrina "Tunggu panggilan saya. Aku akan menghubungi saat aku membutuhkanmu di sini!"
    menu:
        "{i} [JGR] Flirt {/i}"(csq="Katrina +1"):
            $ katrina_rel += 1
            toby "Tidak bisa menunggu panggilan Anda. Saya suka mendengar suara Anda."
            katrina "Jangan dorong keberuntunganmu, nak!"
        "{i} don \ 't flirt {/i}":

            toby "Tentu!"
    scene expression ("images/episode2/217.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/218.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This must be it!{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This must be my new bike!{/i}"
    return


label episode2_drinkMom:
    $ progress = 24

    scene expression ("images/episode2/219.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Finally home. I really missed riding a bike.{/i}"
    scene expression ("images/episode2/220.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm beat. Can't wait to get some sleep.{/i}"
    scene expression ("images/episode2/221.webp") with long_dissolve
    toby "Hei [mom], kamu belum tidur?"

    scene expression ("images/episode2/222.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I gotta give it to her. [mom!c] looks amazing for her age.{/i}"

    charlotte "Dan rindu saat [son] saya pulang dari hari pertama kerja?"
    charlotte "Saya tidak bisa melakukan itu, dan selain itu, saya baru saja membuka sebotol anggur, dan tidak ingin meminumnya sendiri. Itu semakin menyedihkan."
    scene expression ("images/episode2/223.webp") with dissolve
    toby "Apakah Anda terlalu banyak minum akhir -akhir ini?"
    charlotte "Sama sekali tidak. Mari kita duduk dan beri tahu saya bagaimana hari kerja pertama Anda berjalan."
    scene expression ("images/episode2/224.webp") with dissolve
    toby "Pasti. Biarkan saya menyalakan lampu."
    charlotte "Anda suka lampu menyala? Anda tidak ingin melewatkan apa pun."
    scene expression ("images/episode2/225.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Was that a sexual joke?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Nah... It can't be! She's my [mom].{/i}"
    scene expression ("images/episode2/226.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But seeing that bottle half empty I think it may have been.{/i}"
    scene expression ("images/episode2/227.webp") with dissolve
    toby "Anda baru saja membuka botolnya? Berapa banyak yang Anda miliki?"
    charlotte "Hanya satu gelas penuh."
    scene expression ("images/episode2/228.webp") with dissolve
    charlotte "Dan mungkin beberapa setengah kosong."
    scene expression ("images/episode2/229.webp") with dissolve
    charlotte "Saya berjanji saya belum minum apa pun selama dua minggu terakhir, tetapi hari ini istimewa."
    scene expression ("images/episode2/230.webp") with dissolve
    toby "Spesial bagaimana?"
    scene expression ("images/episode2/231.webp") with dissolve
    charlotte "Anak laki -laki saya sekarang. Dia memiliki pekerjaan dan menjadi orang dewasa yang bertanggung jawab."
    charlotte "Sebenarnya, saya pikir Anda sudah menjadi pria untuk sementara waktu. Sekarang Anda hanya lebih bertanggung jawab."
    scene expression ("images/episode2/232.webp") with dissolve
    toby "[mom!c]! Bisakah kita tidak membicarakan kehidupan seks saya?"
    scene expression ("images/episode2/233.webp") with dissolve
    charlotte "{size=12}{color=#FDCA6E}* mumbling *{/color}{/size}\n{i}At least you have one.{/i}"
    scene expression ("images/episode2/230.webp") with dissolve
    toby "Apa itu?"
    scene expression ("images/episode2/234.webp") with dissolve
    charlotte "Setidaknya Anda punya satu. Saya tidak dapat mengingat terakhir kali saya dan [father] Anda memiliki momen romantis. Bahkan hanya ciuman yang penuh gairah."
    scene expression ("images/episode2/235.webp") with dissolve
    toby "Aku yakin dia masih mencintaimu. Hanya dengan semua yang terjadi baru -baru ini, sulit untuk fokus pada hal -hal yang berbeda. Dia hanya mencoba yang terbaik."
    scene expression ("images/episode2/233.webp") with dissolve
    charlotte "{size=12}{color=#FDCA6E}* mumbling *{/color}{/size}\n{i}Yeah. He can't even remember our anniversary.{/i}"
    scene expression ("images/episode2/236.webp") with dissolve
    toby "Hari ini adalah hari jadi Anda?"
    scene expression ("images/episode2/234.webp") with dissolve
    charlotte "Ya. Hari ini kita akan merayakan 21 tahun pernikahan."
    scene expression ("images/episode2/235.webp") with dissolve
    toby "Saya yakin dia tidak lupa. Dia hanya sibuk dengan pekerjaan, tetapi ketika dia kembali ke rumah, aku yakin dia akan membawakanmu beberapa bunga atau semacamnya."
    scene expression ("images/episode2/237.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I need to call him right away to make sure he didn't forget.{/i}"
    scene expression ("images/episode2/238.webp") with dissolve
    charlotte "Tidak akan terjadi."
    scene expression ("images/episode2/235.webp") with dissolve
    toby "Beri dia kesempatan setidaknya."
    scene expression ("images/episode2/238.webp") with dissolve
    charlotte "Dia sudah di tempat tidur, tidur."
    scene expression ("images/episode2/234.webp") with dissolve
    charlotte "Saya menyiapkan makan malam dan anggur ini, selain itu, saya berpakaian seksi untuknya. Apakah Anda ingin tahu apa yang dia katakan padaku?"
    scene expression ("images/episode2/239.webp") with dissolve
    charlotte "Saya tidak membutuhkan pria untuk membantu saya.Dia mengatakan bahwa kita harus menyimpan anggur ini untuk acara -acara khusus. Itu terlalu mahal. Jadi saya akan meminumnya sendiri."
    charlotte "Jadi, jika Anda akan menghakimi saya karena minum, lalu mengapa Anda tidak tidur di sebelah [father] Anda."
    scene expression ("images/episode2/237.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's in a really bad place, I think I'd better try to cheer her up.{/i}"
    scene expression ("images/episode2/240.webp") with dissolve
    toby "Lalu wanita manis, biarkan aku memberitahumu sesuatu. Tahukah Anda mengapa di sekolah menengah saya selalu mendapatkan peran utama dalam setiap permainan?"
    charlotte "Karena kamu kaya dan populer?"
    scene expression ("images/episode2/241.webp") with dissolve
    $ progress = 25
    toby "Mungkin, tapi sungguh karena aku adalah aktor yang baik, jadi biarkan aku menghiburmu. Malam ini aku akan menjadi suamimu. Mengapa kita tidak merayakan 21 tahun pernikahan yang bahagia."
    charlotte "Di mana hadiah saya?"
    scene expression ("images/episode2/242.webp") with dissolve
    toby "Haven \ 't i \' telah cukup untuk Anda? Maksudku, aku memberimu dua [children] yang indah dan selain itu, salah satunya baru saja membuat grand pertamanya dalam satu hari."
    charlotte "Itu luar biasa, sayang. Selamat!"
    toby "Mengapa Anda memberi selamat kepada saya? Saya baru saja memberi tahu Anda bahwa [son] saya adalah orang yang mendapatkan, 000 dalam satu hari."
    charlotte "Anda benar, tetapi saya tidak bisa memilikinya tanpa Anda. Sebenarnya, saya pikir dia mendapatkan otaknya dari [mother]."
    charlotte "Jadi saya kira tidak ada hadiah."
    scene expression ("images/episode2/243.webp") with dissolve
    toby "Itu bukan hadiah yang sebenarnya. Saya telah mempersiapkan lebih banyak."
    charlotte "Lalu dimana sisanya?"
    scene expression ("images/episode2/244.webp") with dissolve
    toby "Anda harus dihargai karena memiliki [son] yang luar biasa."
    scene expression ("images/episode2/245.webp") with dissolve
    charlotte "Setelah 21 tahun menikah, Anda masih cabul?"
    scene expression ("images/episode2/246.webp") with dissolve
    toby "Saya tidak membicarakan sesuatu yang kotor. Satu -satunya cabul di rumah ini adalah Anda."
    charlotte "Apakah Anda akan memberi saya telepon yang sebenarnya saya bayar?"
    toby "Tidak, saya akan memakai musik, dan kemudian kita akan menari!"
    scene expression ("images/episode2/247.webp") with dissolve

    toby "Karena saya tahu betapa Anda suka menari, jadi mengapa Anda tidak menari dengan saya?"
    charlotte "Bagaimana saya bisa mengatakan tidak kepada pemuda yang tampan."
    toby "Jangan tertipu oleh penampilan saya. Saya sebenarnya berusia lima puluhan."
    scene expression ("images/episode2/248.webp") with dissolve
    charlotte "Dan Anda masih tertarik pada wanita tua yang tampak seperti saya?"
    toby "Saya tidak percaya Anda sudah tua sampai saya melihat beberapa id. Anda terlihat lebih baik dari kebanyakan gadis seusia saya. Maksud saya usia [son] saya."
    scene expression ("images/episode2/249.webp") with dissolve
    charlotte "Saya harus mengakui. Saya terlihat sangat baik mengingat fakta bahwa saya memiliki dua [children]."
    charlotte "Jadi, Tuan Charming. Mengapa Anda tidak menunjukkan gerakan Anda."
    scene expression ("images/episode2/250.webp") with long_dissolve
    toby "Jadi apa yang Anda katakan sayangku, apakah hadiah ini cukup baik untuk Anda?"
    charlotte "Jawaban yang jujur atau apakah Anda ingin saya berbohong?"
    menu:
        "[JGR] Jujur":
            pass
        "Berbohong":
            pass
    scene expression ("images/episode2/251.webp") with dissolve
    charlotte "Saya suka niatnya, tetapi Anda tidak tahu cara menari."
    toby "Adalah jawaban yang jujur atau kebohongan, karena saya tidak bisa memberi tahu."
    charlotte "Saya serius, Anda perlu meningkatkan gerakan Anda."
    scene expression ("images/episode2/252.webp") with dissolve
    toby "Apa yang bisa saya katakan? Saya belum menari dengan istri saya dalam 5 tahun."
    charlotte "Anda salah paham. Kami belum berhubungan seks dalam 5 tahun. Menari lebih baru."
    scene expression ("images/episode2/253.webp") with dissolve
    toby "Buruk saya, saya akan mencoba mengingatnya lain kali."
    scene expression ("images/episode2/254.webp") with dissolve
    charlotte "Alih -alih mengingatnya, mengapa Anda tidak memperbaikinya?"
    $ unlockImage(persistent.charlotte_05)
    toby "Uhm ..."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think she's had one too many drinks tonight.{/i}"
    scene expression ("images/episode2/255.webp") with dissolve
    charlotte "Maaf, sayang. Kedengarannya sangat tidak pantas. Hanya saja saya belum bersenang -senang seperti ini selama bertahun -tahun, dan selama beberapa detik, saya terjebak pada saat itu."
    scene expression ("images/episode2/256.webp") with dissolve
    toby "Jangan khawatir [mom]. Lupakan itu. Saya \ m maafkan Anda memiliki waktu yang sulit. Ingin berbicara lebih banyak tentang itu?"
    charlotte "Itu akan sangat bagus."
    $ progress = 26
    scene expression ("images/episode2/257.webp") with dissolve
    charlotte "Saya setuju untuk pindah. Saya setuju untuk membantunya bekerja.Pernikahan kami gagal. Saya telah melakukan segalanya untuk menyimpannya. Saya mendukungnya dalam setiap keputusan."
    charlotte "Saya tahu kami sedang menjalani masa -masa sulit, jadi saya mencoba yang terbaik untuk tersenyum padanya. Saya melakukan semuanya dengan buku itu."
    charlotte "And my reward is \"{i}That wine is for special ocassions{/i}\"."
    scene expression ("images/episode2/258.webp") with dissolve
    charlotte "Apakah saya benar -benar pantas mendapatkan ini? Saya mengerti bahwa dia harus bekerja, itu normal, tetapi saya tidak peduli tentang uang itu."
    charlotte "Saya tidak peduli jika kita tinggal di rumah besar atau apartemen kecil selama kita bahagia, tapi kita tidak."
    charlotte "Dia tidak senang. Satu -satunya hal yang dia pikirkan adalah menghasilkan uang."
    scene expression ("images/episode2/259.webp") with dissolve
    charlotte "Tolong, tolong jangan pernah seperti dia. Anda harus menghasilkan uang, bukan sebaliknya."
    toby "Saya \ m maafkan Anda sedang melalui ini. Aku tidak tahu apakah itu membantu, tapi aku mencintaimu, dan aku yakin Tris juga melakukannya."
    scene expression ("images/episode2/260.webp") with dissolve
    charlotte "Kalian berdua adalah hal terbaik yang pernah terjadi padaku. Aku sangat bersyukur untuk kalian."
    scene expression ("images/episode2/261.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I don't think there is a more heartbreaking moment than seeing your [mother] crying.{/i}"
    charlotte "Aku juga mencintaimu, sayang!"

    show screen ui_message("20 minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode2/262.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It looks like she fell asleep. I should take her to her room.{/i}"
    scene expression ("images/episode2/263.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe bringing her to the same bed as [dad] is not the best idea at the moment, but I'm sure she would hate Tris finding out what's going on here.{/i}"
    scene expression ("images/episode2/264.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Sorry [mom]. I'm going to fix up the attic and let you sleep there with me whenever you feel like it.{/i}"
    scene expression ("images/episode2/265.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Good night [mom].{/i}"

    return


label episode2_trisNight:
    $ progress = 27

    scene expression ("images/episode2/266.webp") with dissolve
    toby "Hai Tris. Kenapa kamu tidak tidur?"
    scene expression ("images/episode2/267.webp") with dissolve
    patricia "Karena aku benci sekolah ini!"
    patricia "Saya merasa sangat bodoh. Saya tidak bisa mengerjakan pekerjaan rumah matematika yang bodoh!"
    scene expression ("images/episode2/268.webp") with dissolve
    toby "Mengapa Anda tidak mendapatkan tutor?"
    scene expression ("images/episode2/269.webp") with dissolve
    patricia "Anda benar -benar harus menanyakan hal itu kepada saya?"
    patricia "Karena kami miskin dan [dad] mengatakan kami tidak dapat membeli tutor, jadi saya hanya harus melakukan yang terbaik untuk mempelajarinya sendiri."
    toby "Kami miskin?"
    patricia "Ya, kami. Apakah Anda lupa mengapa kami harus berbagi kamar?"
    scene expression ("images/episode2/270.webp") with dissolve
    toby "Mungkin kamu. Saya tidak!"
    scene expression ("images/episode2/271.webp") with dissolve
    patricia "Apakah Anda merampok bank atau sesuatu?"
    toby "Saya hanya seorang pria yang bekerja keras."
    scene expression ("images/episode2/272.webp") with dissolve
    patricia "Wow ... Anda membuat 00. Anda kaya. Saya pikir kami memiliki pendapat berbeda tentang apa arti kaya."
    scene expression ("images/episode2/273.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Do you really think I would give you all the money I made today? That's just the tip of the iceberg.{/i}"
    patricia "Apakah Anda memiliki lebih banyak?"
    toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Let's just say that I can pay for a tutor if you really need, and it won't even feel like I'm giving you money.{/i}"
    scene expression ("images/episode2/274.webp") with dissolve
    patricia "Apa tangkapannya?"
    toby "Tidak ada tangkapan. Saya hanya senang membantu!"
    scene expression ("images/episode2/275.webp") with dissolve
    patricia "Saya memiliki ide yang lebih baik."
    scene expression ("images/episode2/276.webp") with dissolve
    toby "Katakan!"
    scene expression ("images/episode2/275.webp") with dissolve
    patricia "Saya akan menyimpan uang itu, dan alih -alih membayar seseorang untuk mengajari saya, Anda dapat membantu saya dengan pekerjaan rumah saya!"
    scene expression ("images/episode2/277.webp") with dissolve
    toby "Ini pasti kesepakatan terburuk sepanjang masa. Selain fakta bahwa saya kehilangan uang, saya juga kehilangan waktu. Jadi apa yang bagi saya?"
    scene expression ("images/episode2/278.webp") with dissolve
    patricia "Biarkan saya begini. Anda memberi saya uang yang saya habiskan untuk pakaian lucu, dan ketika kami melakukan pekerjaan rumah, saya bisa berpakaian bagus. Mungkin bahkan seksi."
    scene expression ("images/episode2/279.webp") with dissolve
    toby "Dan mengapa ini membuat saya merasa lebih baik?"
    scene expression ("images/episode2/280.webp") with dissolve
    patricia "Anda akan sangat terkesan dengan pakaian saya, dan kemudian Anda akan memberi saya lebih banyak uang!"
    scene expression ("images/episode2/279.webp") with dissolve
    toby "Mungkin aku, tapi aku benar -benar merasa kalah di sini."
    scene expression ("images/episode2/280.webp") with dissolve
    patricia "Tidak mungkin ... itu adalah situasi win-win di sini."
    scene expression ("images/episode2/279.webp") with dissolve
    toby "Apakah itu?"
    scene expression ("images/episode2/281.webp") with dissolve
    patricia "Please Please?"
    scene expression ("images/episode2/282.webp") with dissolve
    toby "Baik ... apa masalahnya."
    patricia "Biarkan saya menunjukkan kepada Anda!"
    $ unlockImage(persistent.patricia_05)
    show screen ui_message("A short time later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    $ progress = 28
    scene expression ("images/episode2/283.webp") with dissolve
    hide screen ui_message
    toby "Ini harus menjadi segalanya. Ada lagi?"
    scene expression ("images/episode2/284.webp") with dissolve
    patricia "Ya. Jangan pernah bernegosiasi. Anda sangat buruk dalam hal itu."
    toby "Maksud saya, apakah ada hal lain dalam pekerjaan rumah yang Anda tidak mengerti?"
    scene expression ("images/episode2/285.webp") with dissolve
    patricia "Terima kasih. Saya tahu saya bisa mengandalkan Anda."
    scene expression ("images/episode2/286.webp") with dissolve
    patricia "Dan ambil uang Anda. Saya tidak bisa mengambilnya. Anda mendapatkannya."
    toby "Saya serius. Anda dapat memilikinya, belilah diri Anda sesuatu yang menyenangkan. Saya mendapatkan banyak hal hari ini."
    scene expression ("images/episode2/287.webp") with dissolve
    patricia "Benar-benar? Apakah hari pertama pekerjaan yang menguntungkan?"
    toby "Ya, tidak perlu khawatir. Itu luar biasa. Selain uang yang saya hasilkan, saya juga mendapat sepeda."
    scene expression ("images/episode2/288.webp") with dissolve
    patricia "Seperti yang saya katakan, Anda benar -benar perlu belajar bagaimana bernegosiasi dengan lebih baik. Saya pikir mobil murah akan lebih baik daripada sepeda, tapi ya, Anda melakukannya!"
    scene expression ("images/episode2/289.webp") with dissolve
    toby "Oh, gadis konyol. Saya mengatakan sepeda. Bukan sepeda."
    scene expression ("images/episode2/290.webp") with dissolve
    toby "Come, take a look at my so-called \"bicycle\"Lai"
    scene expression ("images/episode2/291.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/292.webp") with dissolve
    patricia "Jadi? Apakah Anda akan pergi dan membiarkan saya berpakaian, atau Anda ingin membawa saya untuk naik sepeda berpakaian seperti ini?"
    scene expression ("images/episode2/293.webp") with dissolve
    toby "Saya pasti sudah tua. Aku tidak ingat ketika aku memberitahumu bahwa aku akan mengajakmu berkendara."
    patricia "Aku sangat menyesal untukmu. Begitu muda namun sudah kehilangan ingatannya."
    toby "Apakah ada skenario di mana saya bisa menang di sini?"
    scene expression ("images/episode2/294.webp") with dissolve
    patricia "Bukan satu pun!"
    toby "Aku akan menunggumu di luar, tapi cobalah untuk diam. Saya tidak ingin [dad] mendengar bahwa saya membawa Anda ke sepeda saya. Dia akan panik!"
    scene expression ("images/episode2/295.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What is taking her so long?{/i}"
    $ progress = 29

    scene expression ("images/episode2/296.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    toby "Apa dengan pakaiannya?"
    scene expression ("images/episode2/297.webp") with dissolve
    patricia "Anda tidak menyukai pakaian biker saya?"
    toby "Saya merasa seperti noob yang berpakaian seperti ini ketika saya melihat Anda seperti itu."
    scene expression ("images/episode2/298.webp") with dissolve
    patricia "Anda memang terlihat seperti noob jika saya jujur!"
    toby "Itu saja, saya akan solo."
    scene expression ("images/episode2/299.webp") with dissolve
    patricia "Terlambat sekarang!"
    patricia "Ngomong -ngomong, di mana helmnya?"
    toby "Saya perlu membeli pasangan. Saya mendapatkan sepeda tanpa helm."
    patricia "Cobalah untuk tidak mengalami kecelakaan."
    scene expression ("images/episode2/300.webp") with dissolve
    toby "Jadi kemana saja?"
    patricia "Kejutan saya."

    scene expression ("images/episode2/301.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.00

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode2/302.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    show ep2_303 with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/303.webp") with dissolve
    hide ep2_303

    scene expression ("images/episode2/304.webp") with dissolve
    patricia "Mari kita pergi ke taman."
    toby "Saya tidak berpikir itu sah untuk memasuki taman di atas sepeda."
    patricia "Jangan menjadi vagina seperti itu! Kami akan berhenti di bangku."
    scene expression ("images/episode2/305.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/306.webp") with dissolve
    toby "Apakah Anda suka yang ini?"
    scene expression ("images/episode2/307.webp") with dissolve
    patricia "Itu sempurna."

    scene expression ("images/episode2/308.webp") with dissolve
    toby "Jadi? Apa pendapat Anda tentang sepeda saya."
    patricia "Meh ..."
    scene expression ("images/episode2/309.webp") with dissolve
    toby "Benar-benar!? Saya harap Anda tahu cara kembali karena saya meninggalkan Anda di sini."
    patricia "Baik ... itu luar biasa. Saya sangat perlu bersantai seperti ini."
    scene expression ("images/episode2/310.webp") with dissolve
    toby "Aku merasakanmu. Saya juga perlu menjernihkan kepala saya. Saya pikir itu bagus untuk perubahan untuk tidak memikirkan apa pun dan hanya menikmati perjalanannya."
    scene expression ("images/episode2/311.webp") with dissolve
    patricia "Apakah sesuatu terjadi?"
    scene expression ("images/episode2/312.webp") with dissolve
    toby "Tidak, tidak ada apa -apa. Itu hanya sesuatu yang terjadi di tempat kerja."
    scene expression ("images/episode2/313.webp") with dissolve
    patricia "Berbicara tentang ... bagaimana hari kerja pertama Anda?"
    $ progress = 30
    if toby_job == 0:
        scene expression ("images/episode2/310.webp") with dissolve
        toby "Sebenarnya sangat bagus. Bos saya sangat terkesan dengan saya. Kami pergi ke sebuah apartemen dan dia menunjukkan kepada saya. Ketika klien sampai di sana, dia hanya meninggalkan saya bersama mereka."
        scene expression ("images/episode2/314.webp") with dissolve
        patricia "Just like that? No prep talk, no nothing? Just \"Sell this apartment for me?\"
        scene expression ("images/episode2/315.webp") with dissolve
        toby "Ya. Dia mengatakan kepada saya bahwa saya tidak boleh lebih rendah dari 100 ribu dan menyuruh saya bernegosiasi dengan salah satu gadis karena dia yang memiliki uang!"
        scene expression ("images/episode2/314.webp") with dissolve
        patricia "Anda bahkan menegosiasikan harga untuk apartemen pada hari pertama Anda?"
        scene expression ("images/episode2/315.webp") with dissolve
        toby "Saya pikir itu lebih seperti tes untuk melihat apakah saya bisa menjual apartemen.Ya. Saya juga terkejut. Saya tidak percaya bahwa dia meninggalkan saya yang bertanggung jawab."
        scene expression ("images/episode2/313.webp") with dissolve
        patricia "Dan apakah kamu?"
        scene expression ("images/episode2/316.webp") with dissolve
        toby "Bagaimana menurutmu? Tentu saja. Saya bahkan mendapat harga yang lebih tinggi daripada yang dia tanyakan!"
        scene expression ("images/episode2/314.webp") with dissolve
        patricia "Berapa harganya?"
        scene expression ("images/episode2/317.webp") with dissolve
        toby "101k."
        scene expression ("images/episode2/318.webp") with dissolve
        patricia "{size=12}{color=#FDCA6E}* laughing *{/color}{/size}\n{i}She's so lucky to have you. She told you not to go lower than 100k, and you sold it for 101k.{/i}"
        patricia "Seperti yang saya katakan. Tidak pernah bernegosiasi."
        scene expression ("images/episode2/319.webp") with dissolve
        patricia "Dan bagaimana gadis -gadis itu?"

    elif toby_job == 1:
        scene expression ("images/episode2/310.webp") with dissolve
        toby "Agak aneh, bos saya menguji saya untuk melihat apakah dia bisa mempercayai saya."
        scene expression ("images/episode2/320.webp") with dissolve
        patricia "Diuji untuk melihat apakah dia bisa mempercayai Anda? Mengapa dia melakukan itu dan bagaimana caranya?"
        scene expression ("images/episode2/315.webp") with dissolve
        toby "Nah, pada awalnya, sopirnya membawaku di jalan yang teduh ini dan memintaku untuk memberinya pistol dari kompartemen sarung tangan."
        scene expression ("images/episode2/317.webp") with dissolve
        toby "Aku hampir buang air besar ketika aku melihat pistolnya."
        scene expression ("images/episode2/314.webp") with dissolve
        patricia "Apakah itu senjata sungguhan?"
        scene expression ("images/episode2/310.webp") with dissolve
        toby "Itu tampak nyata, tetapi dari apa yang dikatakan Nona Katrina, itu hanya lelucon untuk melihat bagaimana saya akan bereaksi."
        toby "Jadi saya memberinya pistol, dan setelah beberapa menit, dia kembali dengan setumpuk uang dan meminta saya untuk menghitungnya dan kemudian memberikannya kepada Katrina."
        scene expression ("images/episode2/313.webp") with dissolve
        patricia "Kemudian?"
        scene expression ("images/episode2/315.webp") with dissolve
        toby "Lalu aku pergi ke kantor Nona Katrina, dan dia datang kepadaku, memberiku ... pelukan, dan mencuri uang dari sakuku."
        toby "Saya sangat takut ketika saya tidak bisa menemukan uang itu, dan kemudian dia mulai mengolok -olok saya."
        scene expression ("images/episode2/318.webp") with dissolve
        patricia "Saya tidak bisa membayangkan bagaimana perasaan Anda. Tapi tetap saja, mengapa tesnya?"
        scene expression ("images/episode2/310.webp") with dissolve
        toby "Sejauh yang saya mengerti, ada banyak hal teduh yang terjadi di klub, dan mereka tidak ingin polisi terlibat. Mereka lebih suka mengurus hal -hal itu sendiri."
        scene expression ("images/episode2/320.webp") with dissolve
        patricia "Tapi apa sebenarnya pekerjaan Anda di sana?"
        scene expression ("images/episode2/317.webp") with dissolve
        toby "Saya perlu menjemput gadis -gadis di jalan dan mengundang mereka ke dalam karena di mana ada wanita cantik, akan ada pria terangsang yang bersedia meninggalkan tumpukan uang tunai untuk mengesankan mereka."
        scene expression ("images/episode2/318.webp") with dissolve
        patricia "Pria sangat sederhana."
        scene expression ("images/episode2/310.webp") with dissolve
        toby "Sangat lucu!"
        scene expression ("images/episode2/318.webp") with dissolve
        patricia "Dan mengapa dia pikir kamu akan baik dengan gadis -gadis itu?"
        scene expression ("images/episode2/316.webp") with dissolve
        toby "Sebenarnya, saya sangat pandai dalam hal itu. Saya benar -benar berhasil mengambil dua."
        scene expression ("images/episode2/319.webp") with dissolve
        patricia "Benar-benar? Dan bagaimana gadis -gadis itu?"

    scene expression ("images/episode2/321.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}How were the girls? Hot. Really hot. Hot enough that I cheated on Emma. I'm so stupid.{/i}"
    toby "Anda tahu ... gadis normal."
    patricia "Apa dengan raut wajah Anda?"
    scene expression ("images/episode2/322.webp") with dissolve
    toby "Tampilan apa? Ini bukan apa -apa. Anda harus membayangkan sesuatu."
    scene expression ("images/episode2/323.webp") with dissolve
    patricia "Apakah sesuatu terjadi antara Anda dan salah satu gadis?"
    toby "Saya selingkuh di Emma."
    scene expression ("images/episode2/324.webp") with dissolve
    patricia "Apa maksudmu kamu berselingkuh di Emma?"
    toby "Saya benar -benar tidak ingin membicarakannya."
    scene expression ("images/episode2/325.webp") with dissolve
    patricia "Kamu tolol! Bagaimana Anda bisa menipu dia?"
    toby "Saya pikir Anda tidak menyukainya."
    patricia "Saya tidak. Tapi tidak ada gadis yang pantas ditipu!"
    scene expression ("images/episode2/326.webp") with dissolve
    toby "Oh tolong, jangan katakan padaku kamu tidak pernah curang!"
    scene expression ("images/episode2/327.webp") with dissolve
    patricia "Menipu siapa? Saya tidak pernah punya pacar."
    toby "Apa maksudmu kamu tidak pernah punya pacar?"
    scene expression ("images/episode2/328.webp") with dissolve
    toby "Kamu sangat cantik. Kenapa kamu belum punya pacar?"
    patricia "Saya tidak ingin membicarakannya."
    toby "Tidak, tidak ... kami!"
    scene expression ("images/episode2/329.webp") with dissolve
    patricia "Anda tidak memberi tahu saya apa yang Anda lakukan untuk menipu Emma."
    if ep2_laurenBlowjob == True:
        toby "Salah satu dari mereka memberi saya blowjob!"
    else:
        toby "Saya mencium salah satu dari mereka!"
    scene expression ("images/episode2/330.webp") with dissolve
    patricia "Jadi kapan Anda akan memperkenalkannya kepada kami. Saya harap yang ini bukan penggali emas seperti Emma!"
    toby "Dia bukan penggali emas, dan saat ini kita berbicara tentang mengapa kamu tidak pernah punya pacar. Saya tahu banyak anak laki -laki di sekolah menengah kami yang akan senang berkencan dengan Anda."
    scene expression ("images/episode2/331.webp") with dissolve
    patricia "Saya terus membandingkannya dengan Anda. Saya melihat bagaimana Anda memperlakukan wanita. Anda benar -benar pria."
    scene expression ("images/episode2/332.webp") with dissolve
    patricia "Anda pintar, dewasa, lucu, keren, tampan, peduli, dan tidak ada badut yang bisa dibandingkan dengan Anda!"
    scene expression ("images/episode2/333.webp") with dissolve
    patricia "Sampai sekarang. Anda menurunkan bilah sangat rendah dengan ini."
    patricia "Saya pikir itu akan lebih mudah untuk menemukan pacar sekarang. Saya yakin dapat menemukan seorang pria yang bukan penipu!"
    scene expression ("images/episode2/334.webp") with dissolve
    toby "Lalu saya pikir Anda dapat menemukan jalan pulang dengan berjalan kaki dan mencari pacar."
    scene expression ("images/episode2/335.webp") with dissolve
    patricia "Menurut Anda apa yang Anda lakukan?"
    scene expression ("images/episode2/336.webp") with dissolve
    toby "Sampai jumpa!"
    scene expression ("images/episode2/337.webp") with dissolve
    patricia "Jangan berani -berani!"
    scene expression ("images/episode2/338.webp") with dissolve
    toby "Lain kali, saya tidak akan begitu baik!"
    scene expression ("images/episode2/339.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode2/340.webp") with long_dissolve
    patricia "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Idiot!{/i}"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
