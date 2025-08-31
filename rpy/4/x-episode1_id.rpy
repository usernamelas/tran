image ep1_004 = Movie(play="video/episode1/004.webm", loop=True)
image ep1_005 = Movie(play="video/episode1/005.webm", loop=True)
image ep1_011 = Movie(play="video/episode1/011.webm", loop=True)
image ep1_012 = Movie(play="video/episode1/012.webm", loop=True)
image ep1_013 = Movie(play="video/episode1/013.webm", loop=True)
image ep1_014 = Movie(play="video/episode1/014.webm", loop=True)
image ep1_015 = Movie(play="video/episode1/015.webm", loop=True)
image ep1_016 = Movie(play="video/episode1/016.webm", loop=True)
image ep1_137 = Movie(play="video/episode1/137.webm", image="images/episode1/137.webp", loop = False)

label episode1:
    $ persistent.mc = toby
    $ persistent.memories_fixed = True

    stop music fadeout 1.0
    scene expression ("images/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(1, 1) with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_newEpisode

    $ progress = 1
    scene expression ("images/episode1/001.webp") with dissolve

    toby "{2}{6}* thinking *{5}{1}\n{4}Life is a lot more fragile than we think.{3}"
    toby "{2}{6}* thinking *{5}{1}\n{4}How quickly things can change forever.{3}"
    toby "{2}{6}* thinking *{5}{1}\n{4}One day you're up and the next day you're down.{3}"
    scene expression ("images/episode1/002.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}\n{4}I can't believe that my [1]'s company went bankrupt and now we have to move.{3}"
    toby "{2}{6}* thinking *{5}{1}\n{4}I was so used to having everything I wanted and now all of a sudden everything is gone.{3}"
    toby "{2}{6}* thinking *{5}{1}\n{4}We just lost our house, the one with a pool, a sauna, 10 rooms, an indoor cinema, 8 bathrooms and ... Shit, it's so hard to say goodbye to all this.{3}"
    toby "{2}{6}* thinking *{5}{1}\n{4}I still hope this is just a bad dream and in the morning when I wake up, I'll still have my sports car out front, the one I got for my 18th birthday.{3}"
    scene expression ("images/episode1/003.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}\n{4}My [15] had a saying, \"When you reached the top of the mountain you should take a break and look down for a bit.\"{3}"

    label memory_01:
        scene expression ("images/episode1/004.webp") with dissolve
        show ep1_004 with dissolve


        toby "{2}{6}* thinking *{5}{1}\n{4}Speaking of down. That's Emma. She's my girlfriend. We just hooked up a few months ago.{3}"
        toby "{2}{6}* thinking *{5}{1}\n{4}I used to be in the same class as her [17], Cindy. That's how we met.{3}"
        toby "{2}{6}* thinking *{5}{1}\n{4}I was paying Cindy to help me with my homework. By help, I mean she was doing it all for me.{3}"
        toby "{2}{6}* thinking *{5}{1}\n{4}I think I was a little bit too spoiled.{3}"
        scene expression ("images/episode1/005.webp") with dissolve
        show ep1_005
        hide ep1_004
        toby "{2}{6}* thinking *{5}{1}\n{4}Says the guy who is getting sucked by a beautiful blond babe. I'm still spoiled.{3}"
        toby "{2}{6}* thinking *{5}{1}\n{4}At least till she finds out that my [1]'s company went bankrupt and that's the real reason why we're leaving.{3}"
        scene expression ("images/episode1/006.webp") with dissolve
        emma "Sayang, apakah semuanya baik -baik saja? Anda tampak sedikit libur hari ini."
        toby "Jangan khawatir, sayang. Saya baik-baik saja. Hanya saja besok adalah hari kita meninggalkan kota dan siapa yang tahu kapan kita akan bertemu satu sama lain."
        emma "Awww. Anda sangat manis. Anda tidak ingin meninggalkan saya?"
        toby "Tentu saja tidak. Anda adalah hal terbaik yang pernah terjadi pada saya."
        scene expression ("images/episode1/007.webp") with dissolve
        emma "Anda selalu dapat mengunjungi saya, atau lebih baik lagi, saya bisa mengunjungi Anda. Saya yakin ada banyak hotel bintang 5 di kota itu, dan kita bisa menghabiskan beberapa malam seperti ini."
        toby "Ya ... Anda benar!"
        emma "Tentu saja saya. Tidak ada yang bisa membuat kita terpisah."
        menu:
            "{4} [3] Cium dia {3}"(csq="Emma +1"):
                scene expression ("images/episode1/008.webp") with dissolve
                $ emma_rel += 1
                toby "{2}{6}* thinking *{5}{1}\n{4}5 star hotels my ass. I have to tell her sooner or later that I'm broke.{3}"
                scene expression ("images/episode1/007.webp") with dissolve
            "{4} don \ 'T cium dia {3}":
                toby "{2}{6}* thinking *{5}{1}\n{4}5 star hotels my ass. I have to tell her sooner or later that I'm broke.{3}"
        emma "Jadi, apa yang kamu katakan? Ingin bercinta denganku seperti ini adalah hari terakhirmu di bumi?"
        toby "Apakah itu pertanyaan?"
        scene expression ("images/episode1/009.webp") with dissolve
        emma "Sama sekali tidak."
        toby "Sial, kamu sudah sangat basah."
        scene expression ("images/episode1/010.webp") with dissolve
        emma "Dengan pacar sepertimu, aku selalu basah."
        emma "Dan Anda selalu sulit."
        menu:
            "{4} [3] Dirty Talk {3}"(csq="Emma +1 & Galeri Gambar"):
                $ unlockImage(persistent.emma_01)
                $ ep1_emma_dirtyTalk = True
                $ emma_rel += 1
                toby "Diam dan mengendarai saya seperti pelacur Anda. Aku akan mengisimu dengan buruk."
                emma "Saya suka saat Anda berbicara kotor dengan saya."
            "{4} Clean Talk {3}"(csq="Emma +1"):
                $ emma_rel += 1
                toby "Apa yang telah saya lakukan untuk pantas mendapatkan seorang gadis seperti Anda?"
                emma "Anda membuat saya tersenyum ketika saya turun, jadi saya hanya membayar Anda untuk bulan -bulan terbaik dalam hidup saya."
        scene expression ("images/episode1/011.webp") with dissolve
        show ep1_011
        emma "Ya, ya, ya. Berikan padaku sayang."
        if ep1_emma_dirtyTalk == True:
            toby "Itu saja. Naik penisku kamu jalang kotor."
        else:
            toby "Aku sangat mencintaimu!"
            emma "{2}{6}* moaning *{5}{1}\nMe too!"
        scene expression ("images/episode1/012.webp") with dissolve
        show ep1_012
        hide ep1_011
        if ep1_emma_dirtyTalk == True:
            toby "Anda suka berteriak?"
            emma "{2}{6}* panting *{5}{1}\nYes, yessss I do."
            toby "Kemudian berteriak bahwa Anda adalah pelacur."
            emma "{2}{6}* loud *{5}{1}\nI'm a WHORE."
            toby "Siapa pelacur Anda?"
            emma "{2}{6}* moaning *{5}{1}\nI'm YOUUURS!"
        else:
            toby "Anda sangat sempurna."
            emma "{2}{6}* loud *{5}{1}\nYes, yes, YESSSS."
            emma "{2}{6}* gasping *{5}{1}\nDon't stop."
        scene expression ("images/episode1/013.webp") with dissolve
        show ep1_013
        hide ep1_012
        emma "{2}{6}* panting *{5}{1}\nYour dick is so big, I'll never get used to it."
        if ep1_emma_dirtyTalk == True:
            toby "Anda suka penis besar, Anda jalang lapar?"
            emma "{2}{6}* moaning *{5}{1}\nI only love your big dick."
            toby "Kamu bermimpi tentang penisku?"
            emma "{2}{6}* loud *{5}{1}\nYes, I DO!"
        else:
            toby "Apakah aku menyakitimu?"
            emma "{2}{6}* moaning *{5}{1}\nNo, your dick is perfect. I'm so gonna miss it!"
            toby "Aku akan merindukan payudaramu yang indah."
        scene expression ("images/episode1/014.webp") with dissolve
        show ep1_014
        hide ep1_013
        emma "{2}{6}* loud *{5}{1}\nYES, YES, yesss... Fuck me hard, baby."
        toby "Biarkan posisi mengubah posisi."
        scene expression ("images/episode1/015.webp") with dissolve
        show ep1_015
        hide ep1_014
        if ep1_emma_dirtyTalk == True:
            emma "{2}{6}* moaning *{5}{1}\nYes, yes. Fuck me from behind like you fuck a dirty whore."
            toby "Apakah Anda pelacur kotor?"
            emma "{2}{6}* loud *{5}{1}\nYES I AM."
        else:
            emma "{2}{6}* gasping *{5}{1}\nI'm gonna cum soon. I always do when you fuck me from behind."
            toby "Saya sangat dekat dengan."
        scene expression ("images/episode1/016.webp") with dissolve
        show ep1_016
        hide ep1_015
        emma "{2}{6}* panting *{5}{1}\nYes, yes. Right there!"
        emma "{2}{6}* gasping *{5}{1}\nDon't stop!"
        toby "Saya akan cum!"
        if ep1_emma_dirtyTalk == True:
            emma "Saya sedang minum pil! Isi aku!"
        else:
            emma "Jangan khawatir, aku sedang minum pil!"
        scene expression ("images/episode1/017.webp") with dissolve
        hide ep1_016
        with flash
        with flash
        emma "{2}{6}* panting *{5}{1}\nGosh, this was so good!"
        toby "Sial ... sangat bagus."
        scene expression ("images/episode1/018.webp") with dissolve
        emma "Aku sangat mencintaimu."
        toby "Saya juga!"

        $ unlockMemory(persistent.memory_01)
        $ renpy.end_replay()

    emma "Aku tidak tahu apa yang aku lakukan tanpamu di sini."
    toby "Anda masih memiliki [17] Anda."
    emma "Cindy?"
    emma "Dia tidak pernah pulang, sejak dia terhubung dengan pria itu."
    scene expression ("images/episode1/019.webp") with dissolve
    toby "Nah, seperti yang Anda katakan, saya bisa datang mengunjungi Anda dari waktu ke waktu."
    emma "{2}{6}* whispering *{5}{1}\nAnd I'll send you nudes so that you won't forget me."
    toby "Bagaimana saya bisa melupakan gadis cantik seperti Anda."
    emma "Anda memanjakan saya."
    toby "Anda pantas mendapatkan yang terbaik. Benar?"
    scene expression ("images/episode1/020.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/021.webp") with dissolve
    emma "Jika Anda mengatakannya, saya percaya Anda."


    show screen ui_message("Sunday") with long_dissolve
    $ progress = 2
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode1/022.webp") with dissolve
    hide screen ui_message
    toby "{2}{6}* thinking *{5}{1}\n{4}I slept like a log. Last night was crazy.{3}"
    scene expression ("images/episode1/023.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}\n{4}She's so beautiful when she's sleeping. I'm gonna miss spending time with her.{3}"
    toby "{2}{6}* thinking *{5}{1}\n{4}Spending time? Who am I kidding? I'm gonna miss fucking her.{3}"
    toby "{2}{6}* thinking *{5}{1}\n{4}I should go take a shower.{3}"
    scene expression ("images/episode1/024.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}\n{4}I should tell Emma the real reason why we're leaving.{3}"
    toby "{2}{6}* thinking *{5}{1}\n{4}But what if she's really like my [17] says?{3}"
    scene expression ("images/episode1/025.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}\n{4}What if she's actually with me only for the money. I mean, I'm not the best looking guy.{3}"
    toby "{2}{6}* thinking *{5}{1}\n{4}The sex is good, but I feel like I should be able to talk about everything with my girlfriend.{3}"
    scene expression ("images/episode1/026.webp") with dissolve
    emma "Pagi seksi."
    toby "Selamat pagi cantik."
    scene expression ("images/episode1/027.webp") with dissolve
    emma "Seseorang senang melihat saya."
    toby "Dia selalu senang melihatmu."
    scene expression ("images/episode1/028.webp") with dissolve
    $ unlockImage(persistent.emma_02)
    emma "Tidak hari ini, sayang. Kami bersenang -senang tadi malam, dan kami akan bersenang -senang ketika ayah Anda datang mengunjungi saya. Oke?"
    toby "{2}{6}* thinking *{5}{1}\n{4}She's so crazy and fun when she talks to my dick!{3}"
    emma "Di sini ... biarkan aku memberimu ciuman malam yang baik!"
    emma "Tapi sebaiknya Anda tidur sesudahnya."
    scene expression ("images/episode1/029.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/030.webp") with dissolve
    emma "Saya menyuruhnya tidur!"
    toby "Saya melihat."
    emma "Aku mencintaimu."
    toby "Aku pun mencintaimu!"
    scene expression ("images/episode1/031.webp") with dissolve
    emma "Bisakah Anda mencuci punggung saya?"
    toby "Tentu."


    scene expression ("images/episode1/032.webp") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/033.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()


    $ progress = 3
    scene expression ("images/episode1/034.webp") with long_dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nHere we go. After spending my whole life in one city I'm finally moving to a different one.{3}"
    scene expression ("images/episode1/035.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    "*Notification Sound*"
    scene expression ("images/episode1/034.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nI can't say that I wanted to stay there forever, but I always imagined myself moving out on my own at this age, not like this.{3}"
    scene expression ("images/episode1/035.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    "*Notification Sound*"
    scene expression ("images/episode1/034.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nI'm 20 already. My life is going nowhere. I always planned to get my [15]'s company one day, but after what happened, now I don't know what to do with my life.{3}"
    scene expression ("images/episode1/035.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    "*Notification Sound*"
    scene expression ("images/episode1/034.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nWe went bankrupt. We lost everything and now we're moving to a city where my [15]'s partners are. A friend of his will let us stay there, but who knows for how long.{3}"
    scene expression ("images/episode1/035.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    "*Notification Sound*"
    scene expression ("images/episode1/036.webp") with dissolve
    toby "Apakah Anda keberatan? Cukup letakkan ponsel Anda diam."
    scene expression ("images/episode1/037.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nThat's Patricia, or Tris as people call her. She's my younger [17]. Always acting like she deserves everything. Just like now. \nI'm talking, and she doesn't even bother answering me.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nWe used to get along quite well, but for the past few months it's like she went mad. I don't know what's gotten into her, but I can't even have a normal conversation with her.{3}"
    scene expression ("images/episode1/036.webp") with dissolve
    toby "Aku berbicara denganmu, idiot. Letakkan ponsel Anda diam!"
    scene expression ("images/episode1/038.webp") with dissolve
    patricia "Anda selesai?"
    toby "Saya belum selesai! Kataku, letakkan ponselmu diam seperti orang normal!"
    patricia "Tahan pikiran itu."
    scene expression ("images/episode1/039.webp") with dissolve
    toby "Benar-benar?"
    toby "Singkirkan kakimu dari pangkuanku!"
    scene expression ("images/episode1/040.webp") with dissolve
    patricia "Umm... Nah! \nI'm comfortable."
    scene expression ("images/episode1/041.webp") with dissolve
    toby "Aku bilang pindahkan kakimu!"
    scene expression ("images/episode1/042.webp") with dissolve
    erwin "Hentikan, kalian berdua! Anda berdua dewasa muda. Bertindak seperti itu!"
    toby "{2}{6}* thinking *{5}{1}{4}\nThat's my [1]. The guy who lost everything. He says that we're young adults, but he never told us how he managed to lose everything.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nIt was just \"Kids, we're bankrupt and we have to move!\". Tidak ada penjelasan, tidak ada apa -apa. Dia tidak menghormati kita dan tidak pernah, tetapi sekarang dia mengharapkan kita untuk berperilaku seperti orang dewasa muda! {3}"
    scene expression ("images/episode1/043.webp") with dissolve
    charlotte "Biarkan anak -anak menjadi. Mereka baru saja bosan. Ini perjalanan panjang. Anda tidak dapat mengharapkan mereka tetap diam!"
    toby "{2}{6}* thinking *{5}{1}{4}\nAnd that's my [6]. She's the only normal person in this [16]. She used to be a simple country girl, but then she married [1], and he kinda gave her everything she wanted.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nSo she might be a bit spoiled, but even so she took the whole bankruptcy pretty well. I guess the fact that she was not always wealthy made her a bit stronger, unlike [1] and [10], maybe even myself.{3}"
    scene expression ("images/episode1/044.webp") with dissolve
    erwin "Mereka hanya anak -anak. Itu semua yang bisa Anda katakan. Itu alasan Anda untuk memelihara dua anak nakal manja."
    charlotte "Anda tidak hanya mengatakan itu tentang [18] kami. Saya membesarkannya dengan baik. Anda yang mengacau dan ingin menemukan seseorang untuk disalahkan!"
    erwin "Oh, tapi saya harus disalahkan seseorang atas situasi ini."
    charlotte "Bahkan jangan coba -coba!"
    scene expression ("images/episode1/045.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode1/046.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nWe had it coming.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nLately [6] and [1] argue a lot. I think this whole situation had an impact on their relationship.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nNow I feel bad for causing this situation. I should have just left Tris alone.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nI hate it when these two argue. It feels like forever since we've been happy. I can't believe how going broke can ruin a [16].{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nI just hope they won't get divorced. I'd hate that, but knowing [1] he'll do everything he can to not lose [6] and get his company back.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nHe was always like that and he constantly tried to make me be like him. Thanks to him, I'm no quitter either.{3}"


    $ progress = 4

    scene expression ("images/episode1/047.webp") with long_dissolve
    erwin "Di sinilah kita. Rumah manis rumah."
    patricia "Ini terlihat sangat ramai dan kecil!"
    erwin "Biasakan itu untuk saat ini. Anda tidak lagi seorang putri!"
    charlotte "Hentikan, tolong!"
    charlotte "Lihat, sayang, memang lebih kecil dari rumah kita sebelumnya, tapi selama kita senang, itu cukup!"
    scene expression ("images/episode1/048.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nGood thing we're happy.{3}"
    scene expression ("images/episode1/049.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nMy back hurts already just thinking about how many boxes we'll have to carry inside.{3}"
    scene expression ("images/episode1/050.webp") with dissolve
    charlotte "Ayo sayang. Mari kita lihat kamar Anda! Anak laki -laki dapat menangani kotak!"
    patricia "Apakah saya bisa memilih kamar saya?"
    charlotte "Tentu! Biarkan masuk ke dalam."
    scene expression ("images/episode1/051.webp") with dissolve
    erwin "Dia sangat manja.Pilih kamarnya sendiri. Lelucon yang luar biasa. Hanya ada dua kamar."
    toby "Lihat [1]. Saya mengerti Anda kesal karena kehilangan segalanya, tetapi berhenti mengeluarkan masalah Anda pada mereka, terutama pada [6]."
    toby "Jika Anda ingin melepaskan sedikit uap, kami dapat pergi ke gym dan menabrak setiap pukulan yang ada, tetapi [6] dan [10] tidak pantas mendapatkan ini."
    scene expression ("images/episode1/052.webp") with dissolve
    erwin "..."
    toby "{2}{6}* thinking *{5}{1}{4}\nThat's what I thought. He never liked listening to anybody!{3}"
    erwin "Apakah Anda akan membantu saya dengan kotak -kotak ini, atau Anda hanya akan berdiri di sana marah tentang apa yang saya lakukan salah?"
    toby "Saya datang karena saya tidak mencari seseorang untuk meletakkan masalah saya!"
    erwin "Baik, Anda benar, saya diliputi."
    scene expression ("images/episode1/053.webp") with dissolve
    toby "Dan Anda menyesal?"
    erwin "Tidak menyesal seperti Anda setelah kami selesai dengan semua kotak!"
    scene expression ("images/episode1/054.webp") with dissolve
    erwin "Di sini ... mari kita lihat apakah saya telah membuang -buang uang saya untuk membayar keanggotaan gym Anda selama ini!"
    toby "Haha, sangat lucu!"
    scene expression ("images/episode1/055.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/056.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/055.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/056.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()


    $ progress = 5

    show screen ui_message("A few hours later") with fade
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/057.webp") with dissolve
    hide screen ui_message
    patricia "Pizza ada di sini!"
    toby "Akhirnya, saya kelaparan!"
    scene expression ("images/episode1/058.webp") with dissolve
    erwin "Saya bertanya apakah Anda ingin saya berhenti di restoran, dan Anda semua bilang tidak."
    charlotte "Itu 7 jam yang lalu."
    scene expression ("images/episode1/059.webp") with dissolve
    erwin "Berbicara tentang 7 jam yang lalu ..."
    erwin "Seseorang di ruangan ini memberi tahu saya bahwa saya bertindak seperti keledai dengan Anda. Aku tidak akan mengatakan siapa, tapi dia benar!"
    erwin "Saya menyesal Charlotte, karena berteriak pada Anda dan Tris. Saya maafkan kami dalam situasi ini!"
    erwin "Anda tetap menjadi favorit saya [11]."
    scene expression ("images/episode1/060.webp") with dissolve
    toby "*cough*\nOnly [11]!"
    scene expression ("images/episode1/059.webp") with dissolve
    erwin "Terserah, Anda adalah [8] saya, dan Anda pantas mendapatkan yang terbaik. Itulah alasan saya bekerja sangat keras."
    erwin "Untukmu dan untuk istriku yang cantik."
    erwin "Saya minta maaf karena kalian berdua harus berbagi kamar. Setelah kami memiliki lebih banyak uang, saya akan mempekerjakan seseorang untuk memperbaiki loteng untuk [4]!"
    toby "Mengapa saya harus pindah ke loteng?"
    erwin "Karena Anda sangat bijak dan membuka mata saya untuk kesalahan saya, mungkin dari atas sana Anda akan memiliki lebih banyak wahyu seperti itu."
    scene expression ("images/episode1/061.webp") with dissolve
    patricia "Jadi dia harus tidur di lantai agar terlihat seperti peningkatan ketika dia pindah dari kamarku ke loteng?"
    charlotte "Itu gadisku! Saya suka cara Anda berpikir!"
    scene expression ("images/episode1/062.webp") with dissolve
    toby "Saya minta maaf, tapi saya akan makan. Saya tidak mendengar dengan baik ketika saya lapar. Saya baru saja mendengar sesuatu seperti loteng dan tidur di lantai!"
    charlotte "Bon appétit."
    scene expression ("images/episode1/063.webp") with long_dissolve
    toby "Entah pizza ini sangat enak, atau kami kelaparan!"
    scene expression ("images/episode1/066.webp") with dissolve
    charlotte "Pizza itu sangat enak! Saya mendengar banyak hal baik tentang makanan di kota ini!"
    scene expression ("images/episode1/067.webp") with dissolve
    patricia "Saya mendengar bahwa mereka memiliki pantai yang indah!"
    scene expression ("images/episode1/064.webp") with dissolve
    erwin "Pada perjalanan bisnis terakhir saya di sini, saya tinggal di sebuah hotel dekat pantai. Saya pergi ke sana setiap pagi untuk jogging, dan saya bisa mengatakan, itu cantik!"
    scene expression ("images/episode1/065.webp") with dissolve
    toby "Kita harus pergi ke sana besok."
    scene expression ("images/episode1/068.webp") with dissolve
    patricia "Saya bisa \ 't. Saya harus mendaftar di sekolah menengah setempat!"
    scene expression ("images/episode1/065.webp") with dissolve
    toby "Sucks to Be You!"
    scene expression ("images/episode1/068.webp") with dissolve
    patricia "Setidaknya sekali saya menyelesaikan sekolah menengah, saya akan kuliah, tidak seperti orang lain di meja ini."
    scene expression ("images/episode1/065.webp") with dissolve
    toby "Saya ingin lebih fokus menghasilkan uang daripada belajar."
    scene expression ("images/episode1/066.webp") with dissolve
    charlotte "Dan bagaimana kabarmu?"
    scene expression ("images/episode1/064.webp") with dissolve
    erwin "Jika dia seperti [15], dia akan baik -baik saja!"
    scene expression ("images/episode1/069.webp") with dissolve
    erwin "Sebenarnya, saya tidak berpikir saya adalah contoh terbaik saat ini, tetapi jika dia seperti saya beberapa tahun yang lalu, dia akan baik -baik saja!"
    scene expression ("images/episode1/070.webp") with dissolve
    patricia "Saya lelah. Aku akan mandi."
    patricia "Ngomong -ngomong [4], cobalah untuk tidak terlalu nyaman di tempat tidurku!"
    toby "Ya, ya!"


    $ progress = 6

    scene expression ("images/episode1/071.webp") with long_dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nI should let Emma know that we have settled in and see what she's doing.{3}"

    scene expression ("images/episode1/072_texting.webp") with dissolve
    call sms_sent ("emma", "Hey sexy. I have arrived at my new home.\nHow are you?") from _call_sms_sent_4
    call sms_incoming ("emma", "Hi sexy!\n I just got out of the shower. How is the new place?") from _call_sms_incoming_5
    call sms_sent ("emma", "Not as big as the other one, but it's fine.") from _call_sms_sent_5
    call sms_incoming ("emma", "Speaking of big. Is it me or did my boobs get a little bit bigger?", img_icon="images/episode1/077_icon.webp", img="images/episode1/077.webp") from _call_sms_incoming_6
    call sms_sent ("emma", "I need a picture with both your ass and boobs so I can compare them.") from _call_sms_sent_6
    call sms_incoming ("emma", "You dirty hog.") from _call_sms_incoming_7
    call sms_incoming ("emma", "So? What do you think?", img_icon="images/episode1/081_icon.webp", img="images/episode1/081.webp") from _call_sms_incoming_8
    toby "{2}{6}* thinking *{5}{1}{4}\nShe's so hot! I can't believe she's my girlfriend.{3}"
    window hide
    $ unlockImage(persistent.emma_03)
    call sms_sent ("emma", "Yeah, you're right, your boobs got a little bit bigger.") from _call_sms_sent_7
    call sms_incoming ("emma", "How big? I need a dick pic, so I can compare.") from _call_sms_incoming_9
    hide screen message


    scene expression ("images/episode1/084.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/085.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nIf the lady wants, the lady wants. You can't argue with that.{3}"
    scene expression ("images/episode1/086.webp") with dissolve
    toby "Kotoran!"
    patricia "Astaga! Anda Perv. Anda mengambil foto kontol di tempat tidur saya?"
    toby "TIDAK?"
    scene expression ("images/episode1/087.webp") with dissolve
    patricia "Pergi saja, tolong mandi air dingin."
    toby "Maaf Anda harus melihat itu!"
    patricia "Anda menjijikkan, dan pastikan untuk mencuci tangan kotor Anda!"
    scene expression ("images/episode1/088.webp") with dissolve
    toby "Umm ... ya. Sampai jumpa lagi!"
    scene expression ("images/episode1/089.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/090.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nThis was so good. It's nice to release some stress after such a day.{3}"
    scene expression ("images/episode1/091.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nI should take a shower now.{3}"
    scene expression ("images/episode1/092.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nUmm. Where should I put my blanket? This room is so small.{3}"
    scene expression ("images/episode1/093.webp") with dissolve
    patricia "Anda dapat tidur di tempat tidur, tetapi pastikan Anda menjaga tangan Anda sendiri, Anda sudah!"
    toby "Saya bukan orang cabul. Saya hanya merindukan pacar saya."
    patricia "Maka Anda bisa tidur di lantai!"
    scene expression ("images/episode1/094.webp") with dissolve
    toby "Jangan seperti itu, dia tidak seburuk itu!"
    scene expression ("images/episode1/095.webp") with dissolve
    patricia "Dia seorang penggali emas!"
    toby "Dia tidak! Lihatlah kami, kami tidak punya uang yang tersisa, dan dia masih mencintaiku!"
    patricia "Apakah dia tahu bahwa kita bangkrut?"
    toby "Umm ..."
    toby "Mungkin?"
    patricia "Ya, benar! Anda melakukannya, tetapi tidak datang kepada saya menangis ketika dia meninggalkan Anda."
    toby "Jangan khawatir tentang saya! Aku akan baik -baik saja."
    scene expression ("images/episode1/096.webp") with dissolve
    patricia "Apa pun!"


    $ progress = 7
    show screen ui_message("Monday") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/097.webp") with dissolve
    hide screen ui_message
    toby "{2}{6}* thinking *{5}{1}{4}\nMan, I slept like a log. I wonder what time it is.{3}"
    scene expression ("images/episode1/098.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nShit, Tris is getting ready for school. What should I do?{3}"
    menu:
        "{4} [3] Ambil mengintip {3}"(csq="Tris +1 & Galeri Gambar"):
            $ ep1_peek_on_patricia = True
            $ patricia_rel += 1
            $ unlockImage(persistent.patricia_01)
            scene expression ("images/episode1/099.webp") with dissolve
            toby "{2}{6}* thinking *{5}{1}{4}\nI'll be damned. Look at those perky boobs. She looks so good!{3}"
            scene expression ("images/episode1/100.webp") with dissolve
            toby "{2}{6}* thinking *{5}{1}{4}\nToo bad I have a girlfriend.{3}"
            scene expression ("images/episode1/101.webp") with dissolve
            toby "{2}{6}* thinking *{5}{1}{4}\nDamn it [4]. She's your [17], stupid. You can't look at your [17] like that.{3}"
            scene expression ("images/episode1/102.webp") with dissolve
            toby "{2}{6}* thinking *{5}{1}{4}\nEven though she's hot as hell.{3}"
        "{4} menjadi baik [5] {3}":
            scene expression ("images/episode1/101.webp") with dissolve
            toby "{2}{6}* thinking *{5}{1}{4}\nNope. Not today. Today I'm a good [5].{3}"
    scene expression ("images/episode1/103.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nNew day, new city. I feel like I should help [1] with money, but I'm not sure what I could do to earn it.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nI could always go job hunting, but the only job I ever had was in my [1]'s company and let's be honest, I was kinda spoiled.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nNobody really expected me to do anything anyway, so it's really still like I've never worked a day in my whole life.{3}"
    scene expression ("images/episode1/104.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nAnyway, I'm starving. Let's see what we have in the fridge, if anything.{3}"
    scene expression ("images/episode1/105.webp") with dissolve
    toby "Pagi [6]!"
    scene expression ("images/episode1/106.webp") with dissolve
    charlotte "Sayang pagi. Bagaimana Anda tidur?"
    scene expression ("images/episode1/107.webp") with dissolve
    toby "Sangat buruk. Lantainya cukup keras."
    charlotte "Bayi yang malang. Apakah itu benar -benar sulit?"
    toby "Ya. [17] saya sangat buruk. Saya memintanya seperti seribu kali untuk membiarkan saya tidur di tempat tidurnya, tetapi dia tidak akan membiarkan saya."
    scene expression ("images/episode1/108.webp") with dissolve
    charlotte "Oh, sayang. Datang ke [13]. Biarkan dia memberimu ciuman!"
    menu:
        "{4} [3] Biarkan dia menciummu {3}"(csq="Charlotte +1 & Galeri Gambar"):
            $ unlockImage(persistent.charlotte_01)
            $ charlotte_rel += 1
            scene expression ("images/episode1/109.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode1/110.webp") with dissolve
            charlotte "Lebih baik?"
            toby "Jauh lebih baik!"
            charlotte "Anda tahu apa yang menurut saya lucu?"
            toby "Tidak. Apa?"
            charlotte "Tris hanya memberi tahu saya bahwa dia membiarkan Anda tidur di tempat tidur, dan di atas itu, saya datang tadi malam untuk mengucapkan selamat malam, dan melihatnya dengan mata sendiri."
            toby "Oh. Mungkin aku berbohong hanya untuk mendapatkan ciuman?"
            charlotte "Tentu saja. Lain kali ketika Anda ingin [13] mencium Anda, tanyakan saja!"
            toby "Akan lakukan!"
        "{4} Katakan padanya bahwa Anda berbohong {3}":
            scene expression ("images/episode1/110.webp") with dissolve
            toby "Saya bercanda. Dia membiarkan saya tidur di tempat tidur tadi malam."
            charlotte "Aku tahu. Dia membual tentang itu pagi ini, di atas itu, saya datang tadi malam untuk mengucapkan selamat malam, dan Anda berdua tidur seperti bayi."
            toby "Oh, jadi semua akting ini tidak ada gunanya?"
            charlotte "Agak!"
    scene expression ("images/episode1/111.webp") with dissolve
    toby "Ngomong -ngomong, apakah kita punya sesuatu untuk dimakan?"
    charlotte "Saya belum punya waktu untuk pergi ke toko dulu, jadi kami hanya memiliki susu dan sereal untuk saat ini."
    toby "Cukup bagus!"
    scene expression ("images/episode1/112.webp") with dissolve
    toby "Apa yang kamu lihat?"
    charlotte "Tidak banyak, hanya beberapa pekerjaan di sekitar kota."
    toby "Untuk?"
    charlotte "Bagi saya, jelas. Kami benar -benar membutuhkan uang."
    scene expression ("images/episode1/113.webp") with dissolve
    toby "Ada yang menarik bagi saya?"
    charlotte "Anda tidak harus bekerja, sayang!"
    toby "Tapi saya lakukan. Sekarang saya 20 dan tidak pernah bekerja sehari pun dalam hidup saya."
    toby "Saya merasa terlalu manja. Saya perlu melakukan sesuatu dengan hidup saya!"
    charlotte "Nah pekerjaan paling menarik yang saya temukan sejauh ini adalah ini untuk agen real estat."
    toby "Biarkan saya melihat!"
    scene expression ("images/episode1/114.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\n[12]'s cleavage is huge!{3}"
    menu:
        "{4} [3] Perhatikan lebih baik {3}"(csq="Charlotte +1 & Galeri Gambar"):
            $ charlotte_rel += 1
            $ unlockImage(persistent.charlotte_02)
            scene expression ("images/episode1/115.webp") with dissolve
            toby "{2}{6}* thinking *{5}{1}{4}\nI can't believe how good she looks for a woman her age.{3}"
            scene expression ("images/episode1/116.webp") with dissolve
            charlotte "Jadi? Bagaimana menurutmu?"
            scene expression ("images/episode1/117.webp") with dissolve
            toby "Umm ..."
            scene expression ("images/episode1/118.webp") with dissolve
        "{4} saya seharusnya tidak mengambil risiko {3}":
            scene expression ("images/episode1/118.webp") with dissolve
            charlotte "Jadi? Bagaimana menurutmu?"
    toby "Ya. Maksudku, pekerjaan itu terlihat menarik, dan di atas itu, aku cukup pandai meyakinkan orang, jadi aku bisa mencobanya."
    charlotte "Apakah Anda yakin ingin bekerja begitu cepat?"
    toby "Ini tidak seperti saya menjadi lebih muda. Cepat atau lambat, saya harus mulai bekerja. Sekarang lebih baik."
    scene expression ("images/episode1/119.webp") with dissolve
    charlotte "Tapi apa yang akan terjadi saat Anda kuliah? Atau apakah Anda masih berpikir itu tidak ada gunanya?"
    toby "Saya masih berpikir untuk kuliah. Saya tahu bahwa ada perguruan tinggi yang bagus di sini. Emma mengatakan bahwa akan menyenangkan untuk bergabung tahun depan bersamanya karena dia juga akan datang ke sini."
    charlotte "Oh. Jadi begitu. Kalau begitu, aku bahagia."
    charlotte "Ngomong -ngomong, bagaimana dia mengambil semua ini? Langkah Anda, fakta bahwa Anda tidak akan dapat membeli anting -anting berliannya dan sebagainya?"
    scene expression ("images/episode1/120.webp") with dissolve
    toby "Uhm ... Bagus, kurasa!"
    charlotte "Anda belum memberi tahu dia alasan sebenarnya mengapa kami harus pergi, bukan?"
    toby "Tidak, dia tahu, kurang lebih!"
    scene expression ("images/episode1/119.webp") with dissolve
    charlotte "Anda harus berbicara dengannya. Saya yakin dia akan memahami situasinya."
    toby "Bagaimana jika dia meninggalkan saya ketika dia tahu bahwa saya bangkrut?"
    charlotte "Dia menang, karena apa pun yang dipikirkan orang lain, dia benar -benar menyukai Anda, dan jika Anda dibuang, yah, maka dia bukan orang yang tepat untuk Anda."
    toby "Saya tahu, tapi ..."
    scene expression ("images/episode1/121.webp") with dissolve
    charlotte "Ya, saya tahu. Dia memiliki pantat besar, payudara besar untuk usianya, wajahnya cantik, dan dia mungkin sangat baik di tempat tidur, tapi itu tidak semua yang penting dalam suatu hubungan!"
    toby "Itu sangat spesifik."
    charlotte "Ini tidak seperti Anda \ 're 16. Anda adalah orang dewasa. Aku tahu kamu bukan perawan lagi!"
    toby "[9]!"
    scene expression ("images/episode1/119.webp") with dissolve
    charlotte "Bagaimanapun. Seperti yang saya katakan, lebih baik agar dia tahu apa yang terjadi daripada membiarkannya berpikir bahwa Anda tidak mencintainya lagi. Dan itulah mengapa hadiah menjadi lebih murah."
    toby "Anda pikir begitu?"
    charlotte "Tentu saja!"
    toby "Atau saya bisa bekerja keras dan terus membeli barang -barang mahalnya, dan dia tidak akan tahu!"
    charlotte "Saya menyukai gagasan melatih pantat Anda, tetapi bagian yang mahal dan kebohongan tidak terlalu banyak. Bukan itu bagaimana Anda dibesarkan."
    scene expression ("images/episode1/121.webp") with dissolve
    toby "Ya, Anda mungkin benar!"
    scene expression ("images/episode1/122.webp") with dissolve
    charlotte "Bagaimanapun. Saya harus berpakaian dan mendapatkan bahan makanan. Nomor telepon untuk pekerjaan itu ada di laptop saya jika Anda benar -benar menginginkannya."
    toby "Terima kasih, [6]."
    charlotte "Tidak, terima kasih telah menjadi yang baik [7]."
    charlotte "Sampai jumpa lagi!"
    scene expression ("images/episode1/123.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\n[12] is right. I should talk to Emma about what really happened. Maybe when she comes to visit me I'll tell her the truth.{3}"
    scene expression ("images/episode1/124.webp") with long_dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nLet's see what's up with this job?{3}"
    scene expression ("images/episode1/125.webp") with dissolve
    toby "Selamat pagi. Saya melihat iklan tentang pekerjaan sebagai agen real estat. Saya bertanya -tanya apakah pekerjaan itu masih tersedia?"
    $ progress = 8
    woman "{2}{6}* on the phone *{5}{1}\nGood morning. Yes, the job is still available. \nHave you ever worked as a real estate agent before?"
    toby "Tidak. Sebenarnya, ini akan menjadi pekerjaan pertama saya."
    woman "{2}{6}* on the phone *{5}{1}\nHow old are you?"
    toby "Saya berumur 20 tahun. Saya baru saja pindah ke kota dan sedang mencari pekerjaan."
    woman "{2}{6}* on the phone *{5}{1}\nI understand. Are you available today at 11 AM for an interview?"
    toby "Tentu saja!"
    woman "{2}{6}* on the phone *{5}{1}\nI'm glad to hear it. I'll text you the details."
    toby "Terima kasih banyak!"
    woman "{2}{6}* on the phone *{5}{1}\nWhat was your name?"
    toby "Maaf, saya lupa memperkenalkan diri."
    toby "Nama saya [4]."
    woman "{2}{6}* on the phone *{5}{1}\nOkay [4]. See you later!"
    toby "Ya, tentu!"
    woman "{2}{6}* on the phone *{5}{1}\nHave a good day!"
    toby "Semoga harimu menyenangkan!"
    scene expression ("images/episode1/126.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nWell, that was easy. I never knew it was this easy to get a job!{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nOr maybe I'm just a lucky guy.{3}"
    scene expression ("images/episode1/127.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nLet's see what's on TV.{3}"
    show screen ui_message("A short time later") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/128.webp") with dissolve
    hide screen ui_message
    charlotte "Sayang, bisakah kamu datang dan bantu aku dengan tas?"
    toby "Tentu [6]."
    scene expression ("images/episode1/129.webp") with dissolve
    toby "Di mana Anda menginginkannya?"
    charlotte "Di sana. Saya akan menyelesaikannya!"
    scene expression ("images/episode1/130.webp") with dissolve
    charlotte "Apakah Anda menelepon agen real estat?"
    toby "Ya, dan saya memiliki wawancara pada pukul 11:00."
    charlotte "Hari ini?"
    toby "Ya! Saya harus segera bersiap -siap."
    charlotte "Itu cepat. Mereka pasti benar -benar membutuhkan orang."
    toby "Atau saya hanya pria yang beruntung?"
    charlotte "Anda hanya beruntung!"
    scene expression ("images/episode1/131.webp") with dissolve
    charlotte "Maksud saya, lihat [6] Anda, Anda harus benar -benar beruntung memiliki [6] seperti saya!"
    toby "Sekarang saya tahu siapa yang dilakukan Tris."
    charlotte "Anda sangat lucu!"
    scene expression ("images/episode1/132.webp") with dissolve
    toby "Saya akan berubah untuk wawancara."
    scene expression ("images/episode1/133.webp") with long_dissolve
    charlotte "Ya ampun ... siapa pria tampan itu?"
    charlotte "Jika Anda berpakaian seperti itu, mereka akan mempekerjakan Anda di tempat!"
    toby "Saya hanya bisa berharap begitu!"
    scene expression ("images/episode1/134.webp") with dissolve
    charlotte "Di sini ... biarkan aku memperbaikinya!"
    toby "Terima kasih [6]."
    charlotte "Anda dapat mengambil mobil saya dan mengambil Patricia dari sekolah saat Anda selesai."
    toby "Tentu. Aku akan melakukan itu, lalu aku akan datang menjemputmu, dan kita semua akan pergi ke pantai!"
    charlotte "Jika itu yang Anda inginkan, bagaimana saya bisa mengatakan tidak kepada Anda!"
    scene expression ("images/episode1/135.webp") with dissolve
    charlotte "Semoga Sukses Sayang."
    toby "Terima kasih [6]!"


    $ progress = 9

    scene expression ("images/episode1/136.webp") with long_dissolve
    toby "Halo, saya di sini untuk wawancara kerja."
    window hide
    show ep1_137 with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/137.webp") with dissolve
    hide ep1_137
    woman "Anda harus [4], kan?"
    toby "Ya ma \ 'am."
    katrina "Anda bisa memanggil saya Katrina."
    scene expression ("images/episode1/138.webp") with dissolve
    katrina "Tolong duduklah."
    toby "Terima kasih, ma \ 'am."
    toby "Maksudku, Katrina."
    scene expression ("images/episode1/139.webp") with dissolve
    katrina "Jadi? Siapa [4]? Ceritakan lebih banyak tentang diri Anda!"
    scene expression ("images/episode1/140.webp") with dissolve
    toby "Nah, saya berumur 20 tahun. Saya baru saja pindah ke kota ini, dan saya pikir saya harus mendapatkan pekerjaan untuk membantu [16]."
    scene expression ("images/episode1/139.webp") with dissolve
    katrina "Di mana Anda tinggal sebelum pindah ke sini?"
    scene expression ("images/episode1/140.webp") with dissolve
    toby "Uhm, Rictown."
    scene expression ("images/episode1/139.webp") with dissolve
    katrina "Oh, menarik. Saya juga dulu tinggal di sana. Di bagian kota mana Anda tinggal?"
    scene expression ("images/episode1/140.webp") with dissolve
    toby "Saya lebih suka tidak mengatakan, jika itu baik -baik saja?"
    scene expression ("images/episode1/141.webp") with dissolve
    katrina "Tidak, nak. Tidak apa -apa. Saya bertanya, Anda menjawab!"
    toby "Uhm. Saya tinggal di bagian atas."
    katrina "Maksudmu bagian yang kaya?"
    toby "Ya."
    scene expression ("images/episode1/139.webp") with dissolve
    katrina "[2] Anda bekerja untuk beberapa keledai kaya di sana?"
    scene expression ("images/episode1/140.webp") with dissolve
    toby "Uhm, tidak juga."
    scene expression ("images/episode1/142.webp") with dissolve
    katrina "Menarik ... jadi Anda berasal dari orang kaya [16]."
    scene expression ("images/episode1/143.webp") with dissolve
    katrina "Dan kenapa Anda ingin bekerja di sini jika Anda berasal dari orang kaya [16]?"
    toby "Mengapa ada yang menginginkan pekerjaan?"
    katrina "Saya mengerti. Anda bangkrut."
    scene expression ("images/episode1/144.webp") with dissolve
    katrina "Jadi, apakah Anda pikir Anda mendapatkan apa yang diperlukan untuk memuaskan saya?"
    toby "{2}{6}* thinking *{5}{1}{4}\nThis woman is crazy.{3}"
    menu:
        "Uhm, memuaskanmu?":
            katrina "Ya sayang, untuk bekerja keras sampai aku puas."
            katrina "Apa lagi?"
            toby "Tidak ada apa-apa. Ya, saya benar -benar berpikir saya bisa bekerja sampai Anda puas."
            scene expression ("images/episode1/145.webp") with dissolve
            katrina "Tidak, saya tidak suka bagaimana kedengarannya. Saya akan mengatakannya lagi."
            katrina "Apakah Anda pikir Anda dapat memuaskan saya?"
        "[3] Saya bisa memuaskan wanita mana pun, jadi mengapa Anda berbeda?"(csq="Katrina +1 & Gambar Galeri"):
            $ katrina_rel += 1
            $ unlockImage(persistent.katrina_01)
            katrina "Berani! Saya menyukainya, tetapi saya lebih berpikir seperti, dapatkah Anda bekerja sampai saya puas?"
            toby "Oh, ya. Saya benar -benar berpikir saya bisa bekerja sampai Anda puas."
            scene expression ("images/episode1/145.webp") with dissolve
            katrina "Sebenarnya, saya lebih menyukai jawaban pertama Anda."
            katrina "Apakah Anda pikir Anda dapat memuaskan saya?"

    scene expression ("images/episode1/146.webp") with dissolve
    toby "Ya, ma \ 'am. Aku bisa memuaskanmu!"
    scene expression ("images/episode1/147.webp") with dissolve
    katrina "Jadi jika Anda benar -benar ingin mendapatkan uang mengapa Anda tidak menjual obat seperti orang normal? Anda benar -benar ingin memasuki sistem yang rusak seperti ini, di mana ikan besar mengambil segalanya, dan Anda hanya mendapatkan apa yang mereka berikan kepada Anda?"
    katrina "Mengapa menjadi budak saat Anda bisa menjadi raja?"
    scene expression ("images/episode1/148.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nIs she really asking me this? What kind of interview is this?{3}"
    scene expression ("images/episode1/149.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    $ progress = 10
    woman "Uhum, uhum. Permisi!"
    scene expression ("images/episode1/150.webp") with dissolve
    katrina "Halo, Sayang. Saya menguji karyawan masa depan Anda."
    woman "Saya yakin."
    scene expression ("images/episode1/151.webp") with dissolve
    woman "Anda harus [4] kan?"
    toby "Ya, ma \ 'am."
    scene expression ("images/episode1/152.webp") with dissolve
    darlene "Nama saya Darlene. Kami berbicara pagi ini di telepon."
    toby "Senang berkenalan dengan Anda!"
    scene expression ("images/episode1/153.webp") with dissolve
    darlene "Maaf, saya terlambat. Saya memiliki beberapa bisnis yang belum selesai dengan beberapa apartemen."
    scene expression ("images/episode1/154.webp") with dissolve
    toby "Tidak masalah."
    darlene "Saya berharap pacar saya tidak memberi Anda terlalu banyak masalah."
    toby "{2}{6}* thinking *{5}{1}{4}\nGirlfriend? My future boss is a lesbian? Wow!{3}"
    toby "Sama sekali tidak."
    darlene "Saya senang mendengarnya."
    scene expression ("images/episode1/155.webp") with dissolve
    darlene "Sayang, bisakah kamu meninggalkan kami? Saya ingin mengenal [4] sedikit lebih baik!"
    katrina "Tentu saja, cintaku."
    scene expression ("images/episode1/156.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/157.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/158.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nOkay... That was very suspicious.{3}"
    scene expression ("images/episode1/159.webp") with dissolve
    darlene "Jadi, di telepon Anda menyebutkan bahwa Anda baru saja pindah ke kota dan Anda sudah mencari pekerjaan. Saya suka ini pada seseorang."
    darlene "Itu berarti mereka bekerja keras. Namun, Anda juga menyebutkan bahwa ini akan menjadi pekerjaan pertama Anda. Kenapa begitu?"
    toby "Nah, ini akan menjadi pekerjaan nyata pertama saya. Saya sering membantu di perusahaan [1] saya, tetapi segalanya tidak berjalan dengan baik bagi kami, dan sekarang kami telah pindah ke sini."
    darlene "Apakah Anda tahu sesuatu tentang rumah?"
    toby "Saya tahu sedikit bagian struktural rumah, dan saya sangat pandai membaca orang, jadi saya dapat membujuk mereka untuk membeli atau menyewa rumah."
    scene expression ("images/episode1/160.webp") with dissolve
    darlene "Begitu? Lalu mari kita dengar apa yang Anda katakan tentang saya?"
    toby "Uhm? Itu tidak sesuai."
    darlene "Anda dapat membuatnya terdengar sesuai atau hanya mengatakan apa pun yang Anda inginkan, dan kami akan memutuskan apa yang harus dilakukan dengan informasi tersebut."
    scene expression ("images/episode1/161.webp") with dissolve
    $ progress = 11
    menu:
        "{4} [3] Go Personal {3}"(csq="Darlene +1 & Galeri Gambar"):
            $ darlene_rel += 1
            $ unlockImage(persistent.darlene_01)
            scene expression ("images/episode1/162.webp") with dissolve
            toby "Anda menjalin hubungan dengan wanita lain meskipun Anda tidak 100 %% yakin Anda seorang lesbian. Kemungkinan besar Anda memiliki beberapa hubungan yang gagal dan hati Anda sangat hancur, sehingga Anda kehilangan kepercayaan pada pria."
            toby "Meskipun Anda adalah bos perusahaan Anda sendiri dan Anda terbiasa dihormati, Anda bosan dengan itu."
            toby "Anda suka ketika orang lain yang bertanggung jawab, itu sebabnya pacar Anda sangat suka memerintah karena Anda menyukainya, dan Anda menyukai gagasan untuk tunduk di luar pekerjaan."
            toby "Ketika Anda meminta saya untuk mengatakan sesuatu tentang Anda, Anda mengharapkan sesuatu yang lebih seperti, Anda adalah tipe wanita yang bekerja keras untuk mencapai tempat Anda sekarang."
            toby "Itu karena saya menjadi orang yang diwawancarai seharusnya tidak mendapatkan pribadi ini. Tetapi fakta bahwa saya berbicara kepada Anda meskipun Anda bisa menjadi bos masa depan saya membuat Anda sangat bersemangat."
            toby "Karena jauh di lubuk hati apa yang benar -benar Anda inginkan."
            scene expression ("images/episode1/163.webp") with dissolve
            darlene "Uhm ... ya, jadi."
            scene expression ("images/episode1/164.webp") with dissolve
            darlene "Maaf, saya tidak mengharapkan itu, jadi saya tidak yakin harus berkata apa."
            toby "Saya harap saya tidak berlebihan."
            darlene "Mungkin sedikit, tapi yang mengejutkan itu tidak mengganggu saya."
        "{4} tetap aman {3}":

            scene expression ("images/episode1/162.webp") with dissolve
            toby "Anda adalah tipe wanita yang bekerja sangat keras untuk berada di tempat dia sekarang, dan perusahaan ini seperti bayi Anda."
            toby "Dengan ukuran kantor, saya dapat mengatakan bahwa tidak ada banyak orang yang bekerja di sini karena Anda ingin dapat mengetahui semua yang terjadi."
            toby "Anda suka memegang kendali sehingga jika terjadi kesalahan, Anda tidak dapat menyalahkan orang lain selain diri Anda sendiri."
            toby "Ketika Anda mendengar bahwa saya berusia 20 tahun, Anda mengatakan pada diri sendiri bahwa Anda dapat mengajari saya semua yang Anda ketahui karena Anda sedikit lelah bekerja dengan orang lain."
            toby "Jadi Anda memutuskan untuk mempekerjakan seseorang yang muda yang bisa Anda persiapkan dan akhirnya percaya."
            scene expression ("images/episode1/163.webp") with dissolve
            darlene "Ini sebenarnya benar -benar bagus!"
            darlene "Saya suka kemana perginya."

    scene expression ("images/episode1/165.webp") with dissolve
    darlene "Aku akan jujur padamu. Aku menyukaimu, mungkin kamu sedikit berani, tapi aku suka itu."
    darlene "Saya yakin Kat memberi Anda nomornya untuk meneleponnya karena dia suka mempekerjakan pria tampan di klubnya untuk menarik wanita muda."
    darlene "Dan jika di klub ada wanita muda, akan ada juga pria untuk membayar banyak uang untuk mengesankan mereka, jadi semua orang mendapat untung dari itu."
    darlene "Saya tidak bisa menawarkan kepada Anda pesta dan kesenangan yang dia bisa, tetapi saya dapat menawarkan Anda penghasilan yang sangat stabil dan kehidupan yang baik."
    darlene "Besok saya bertemu dengan klien untuk sebuah apartemen. Anda akan bergabung dengan saya, dan saya akan membiarkan Anda melakukan pekerjaan Anda."
    darlene "Saya ingin melihat apakah Anda benar -benar dapat membaca orang sebaik yang Anda katakan dan meyakinkan mereka untuk membeli."
    darlene "Saya biasanya tidak melakukan hal -hal seperti ini, tetapi saya benar -benar menyukai Anda."
    darlene "Jadi saya akan memberi Anda kesempatan. Jika Anda berhasil menjual apartemen, Anda mendapatkan 20 %% dari laba."
    scene expression ("images/episode1/166.webp") with dissolve
    toby "Saya tidak tahu harus berkata apa. Saya tidak mengharapkan ini."
    scene expression ("images/episode1/167.webp") with dissolve
    darlene "Anda tidak perlu mengatakan apa -apa sekarang, pikirkan saja siapa yang akan Anda hubungi besok. Saya atau Kat."
    toby "Terima kasih atas kesempatannya. Saya akan tidur di atasnya dan memanggil Anda hal pertama di pagi hari."
    scene expression ("images/episode1/168.webp") with dissolve
    darlene "Saya harap Anda akan membuat pilihan yang tepat."
    toby "Terima kasih untuk ini!"
    scene expression ("images/episode1/169.webp") with dissolve
    darlene "Tidak terima kasih! Saya sangat menikmati wawancara ini."
    toby "Semoga harimu menyenangkan."
    darlene "Tolong hubungi saya Darlene!"
    toby "Bye Darlene."
    darlene "Bye [4]."


    $ progress = 12

    scene expression ("images/episode1/170.webp") with long_dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nThat interview was really something. It wasn't what I expected, but both Darlene and Katrina were really interesting women.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nI wonder who I should call. On one hand working as a real estate agent would be stable income and a safe job.{3}"
    scene expression ("images/episode1/171.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nOn the other hand Katrina's life sounds interesting. I'm not so sure about the drugs thing, but from what Darlene said it does sound interesting.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nI don't know what to do. I'll have to think more about it.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nAnyway, let's go pick up Tris from school.{3}"
    scene expression ("images/episode1/172.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nI should text Tris that I'm here.{3}"
    scene expression ("images/episode1/173.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nHere comes the school girl.{3}"
    scene expression ("images/episode1/174.webp") with dissolve
    toby "Jadi bagaimana sekolah baru?"
    patricia "Sekolah terlihat membosankan, tetapi gosip adalah sesuatu yang lain di sini."
    toby "Kenapa?"
    patricia "Sebagai permulaan, beberapa bulan yang lalu, kepala sekolah ini ditangkap karena kejahatan yang melibatkan semacam pengedar narkoba."
    toby "Kota ini adalah tempat yang aneh!"
    patricia "Anda memberi tahu saya? Tapi jujur saja, saya pikir kita akan sangat cocok di sini. Ini tidak seperti kita terlalu normal."
    scene expression ("images/episode1/175.webp") with dissolve
    toby "Bagaimanapun, kita harus pergi. [12] sedang menunggu kami pergi ke pantai!"
    patricia "Ya! Saya sudah menunggu ini sepanjang hari!"
    patricia "Ngomong -ngomong, kenapa kamu begitu berpakaian?"
    toby "Saya memiliki wawancara kerja."
    patricia "Anda? Bekerja?"
    scene expression ("images/episode1/176.webp") with dissolve
    toby "Ya. Apa yang begitu aneh tentang itu?"
    patricia "Anda tidak pernah bekerja sehari pun dalam hidup Anda."
    toby "Saya membantu [1] di perusahaannya."
    patricia "Ya. Seperti yang saya katakan, Anda tidak pernah bekerja sehari pun dalam hidup Anda."
    patricia "Tapi bagaimanapun juga. Bagaimana wawancara berjalan?"
    toby "Aku akan memberitahumu nanti setelah kita mengambil [6]. Saya benar -benar tidak ingin menceritakan kisah yang sama dua kali."
    scene expression ("images/episode1/177.webp") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode1/178.webp") with dissolve
    toby "Mengapa terburu -buru?"
    patricia "Apakah Anda bercanda? Saya belum melihat pantai dalam hampir 7 bulan."
    scene expression ("images/episode1/179.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nBoth [6] and Tris take a long time to get ready.{3}"
    scene expression ("images/episode1/180.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    toby "{2}{6}* thinking *{5}{1}{4}\nWow. [6] looks gorgeous.{3}"
    charlotte "Apakah Tris siap?"
    toby "Belum."
    patricia "Saya! Aku sedang turun sekarang!"
    scene expression ("images/episode1/181.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    toby "{2}{6}* thinking *{5}{1}{4}\nLike [14], like [11].{3}"
    scene expression ("images/episode1/182.webp") with dissolve
    toby "Biarkan saja pergi!"


    $ progress = 13

    scene expression ("images/episode1/183.webp") with long_dissolve
    patricia "Pantai ini terlihat sangat keren. Tidak bisa menunggu untuk berenang."
    charlotte "Saya tidak bisa menunggu untuk tidur di kursi -kursi itu. Mereka terlihat nyaman!"
    toby "Banyak lelah?"
    scene expression ("images/episode1/184.webp") with dissolve
    charlotte "Sedikit. Bergerak adalah masalah yang cukup besar."
    scene expression ("images/episode1/185.webp") with dissolve
    patricia "Wow ... mereka memiliki jaring bola voli. Kami benar -benar harus bermain [4]."
    toby "Apakah kita?"
    scene expression ("images/episode1/186.webp") with dissolve
    patricia "Yesss!"
    toby "Bagus!"
    scene expression ("images/episode1/187.webp") with dissolve
    charlotte "Jadi? Bagaimana wawancara?"
    toby "Sebenarnya sangat baik. Ada dua wanita yang menawari saya pekerjaan."
    patricia "Anda belum bekerja satu hari dalam hidup Anda dan mendapat dua tawaran pekerjaan dari satu wawancara?"
    toby "Ya, itu aneh."
    scene expression ("images/episode1/188.webp") with dissolve
    toby "Jadi ada wanita ini bernama Darlene. Dia yang saya ajak bicara di telepon pagi ini."
    toby "Dan pacarnya, Katrina. Dia adalah pemilik klub sejauh yang saya mengerti."
    toby "Ketika saya pergi ke sana, Katrina ada di kantornya, dan dia mengolok -olok saya sedikit!"
    scene expression ("images/episode1/189.webp") with dissolve
    patricia "Nah, wajah Anda memohon untuk diolok -olok!"
    scene expression ("images/episode1/190.webp") with dissolve
    charlotte "Jangan bersikap kasar kepada [5] Anda."
    scene expression ("images/episode1/188.webp") with dissolve
    toby "Ngomong -ngomong, jadi dia agak menawari saya pekerjaan di klubnya, tapi saya belum yakin apa, karena itu ketika Darlene masuk."
    scene expression ("images/episode1/191.webp") with dissolve
    charlotte "Jadi pada dasarnya dia mencuri karyawan pacarnya?"
    toby "Anda bisa mengatakan mereka sedang memperebutkan saya."
    scene expression ("images/episode1/192.webp") with dissolve
    patricia "Itu akan menjadi yang pertama dan terakhir kali dua gadis akan memperebutkan Anda."
    scene expression ("images/episode1/193.webp") with dissolve
    toby "Sangat lucu."
    scene expression ("images/episode1/188.webp") with dissolve
    toby "Ngomong -ngomong, Darlene tahu apa yang Katrina lakukan, jadi dia mengatakan bahwa aku punya sampai besok untuk memutuskan untuk siapa bekerja."
    toby "Besok saya akan menelepon Darlene atau Katrina."
    scene expression ("images/episode1/194.webp") with dissolve
    charlotte "Saya pikir bekerja untuk Darlene akan menjadi yang terbaik. Ini pekerjaan yang bagus. Anda bahkan tidak tahu apa yang harus Anda lakukan di klub."
    scene expression ("images/episode1/195.webp") with dissolve
    patricia "Saya tidak setuju dengan [6]. Saya pikir bekerja di klub bisa lebih menarik dan di atas itu, siapa tahu. Mungkin Anda akan bertemu pacar baru."
    toby "Saya punya pacar."
    scene expression ("images/episode1/196.webp") with dissolve
    patricia "Mungkin, tapi dia menyebalkan."
    charlotte "Perhatikan lidah Anda, wanita muda. Dia bukan wanita jalang, dan selama mereka saling mencintai, itu yang penting."
    scene expression ("images/episode1/197.webp") with dissolve
    patricia "Dia bahkan tidak memberitahunya mengapa kami harus pergi."
    charlotte "Itu bisnis mereka, bukan milikmu."
    patricia "Dia seorang penggali emas!"
    scene expression ("images/episode1/198.webp") with dissolve
    toby "Whatever!\nI'll go grab something to drink from the bar. Want anything?"
    patricia "Saya ingin limun."
    toby "Saya akan membelikan Anda satu jika Anda mengambil kembali apa yang Anda katakan tentang Emma."
    scene expression ("images/episode1/199.webp") with dissolve
    patricia "Lalu aku akan membeli sendiri."
    scene expression ("images/episode1/200.webp") with dissolve
    charlotte "Jangan mengambilnya secara pribadi. Saya tidak tahu di mana saya salah dengannya."
    toby "Jangan khawatir [6]. Jadi? Apa yang bisa saya dapatkan dari Anda?"
    charlotte "Kejutkan aku!"
    scene expression ("images/episode1/201.webp") with dissolve
    toby "Saya akan!"
    scene expression ("images/episode1/202.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nI hate the idea that maybe Tris is right, but it hurts when she talks like that about my girlfriend.{3}"
    scene expression ("images/episode1/203.webp") with dissolve
    patricia "Bagaimana rasanya?"
    toby "Merasa apa?"
    patricia "Rasa sakit ketika Anda menyadari bahwa [17] Anda selalu benar?"
    toby "Persetan!"
    scene expression ("images/episode1/204.webp") with dissolve
    barman "Itu akan menjadi 0,50."
    $ progress = 14
    menu:
        "{4} [3] Bayar minumannya {3}"(csq="Tris +1 & Galeri Gambar"):
            $ patricia_rel += 1
            $ unlockImage(persistent.patricia_02)
            scene expression ("images/episode1/205.webp") with dissolve
            toby "Izinkan saya!"
            scene expression ("images/episode1/206.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode1/207.webp") with dissolve
            patricia "Aku tahu aku bisa mengandalkanmu!"
            toby "Ya, ya. Apa pun!"
            scene expression ("images/episode1/208.webp") with dissolve
            toby "..."
            toby "{2}{6}* thinking *{5}{1}{4}\nDude... She's your [17]. You can't look at her ass.{3}"
            scene expression ("images/episode1/209.webp") with dissolve
            barman "Pak?"
            toby "Maaf?"
        "{4} dia tidak pantas mendapatkannya {3}":
            scene expression ("images/episode1/210.webp") with dissolve
            patricia "Apakah Anda malu membiarkan seorang wanita membayar minumannya sendiri?"
            toby "Biarkan saya memikirkannya sebentar."
            scene expression ("images/episode1/207.webp") with dissolve
            toby "Tidak. Tidak sama sekali!"
            scene expression ("images/episode1/209.webp") with dissolve
    barman "Apa yang bisa saya dapatkan dari Anda, Pak?"
    toby "Oh, benar. Beri saya koktail beralkohol terbaik Anda dan yang terbaik tanpa alkohol di dalamnya."
    barman "Tentu. Beri aku sesaat!"
    scene expression ("images/episode1/211.webp") with dissolve
    toby "Harus jujur. Tempat ini sangat bagus, terlalu buruk itu agak kosong. Saya kira tidak banyak orang datang ke pantai pada hari Senin."
    barman "Pertama kali di sini?"
    toby "Ya, saya baru saja pindah ke kota."
    barman "Anda akan suka di sini. Ada banyak hal yang harus dilakukan."
    barman "Anda harus kembali ke pantai pada akhir pekan. Ada banyak wanita cantik di sini."
    toby "Ya ... saya pasti harus datang!"
    toby "{2}{6}* thinking *{5}{1}{4}\nI have a gorgeous lady at home, but he doesn't need to know that.{3}"
    scene expression ("images/episode1/212.webp") with dissolve
    barman "Ini dia Pak. Itu akan menjadi 5"
    scene expression ("images/episode1/213.webp") with dissolve
    toby "Terima kasih kawan!"
    scene expression ("images/episode1/214.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nWhich one should I give [6]?{3}"
    menu:
        "{4} [3] Yang dengan alkohol di dalamnya {3}"(csq="Charlotte +1"):
            $ charlotte_rel += 1
            $ ep1_get_charlotte_drunk = True
        "{4} yang tanpa alkohol di dalamnya {3}":
            pass
    scene expression ("images/episode1/215.webp") with dissolve
    toby "Ini dia [6]."
    charlotte "Terima kasih, Sayang."
    scene expression ("images/episode1/216.webp") with long_dissolve
    patricia "Saya punya ide!"
    toby "Membuatku takjub!"
    patricia "Jika Anda berhasil mengalahkan saya di bola voli, saya akan meminta maaf atas semua yang saya katakan tentang Emma!"
    scene expression ("images/episode1/217.webp") with dissolve
    toby "Dan Anda juga tidak akan mengatakan hal buruk tentang dia di masa depan?"
    toby "Kesepakatan."
    scene expression ("images/episode1/218.webp") with dissolve
    patricia "Mari kita lihat Anda mencoba dulu."
    scene expression ("images/episode1/219.webp") with dissolve
    toby "Anda memintanya!"
    scene expression ("images/episode1/220.webp") with long_dissolve
    $ progress = 15
    menu:
        "{4} [3] Biarkan dia menang {3}"(csq="Tris +1 & Galeri Gambar & Penting untuk Tris \ 'Path"):
            $ patricia_rel += 1
            $ ep1_let_patricia_win = True
            $ unlockImage(persistent.patricia_03)
            scene expression ("images/episode1/221.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode1/222.webp") with dissolve
            patricia "Memperdaya!"
            toby "Aku membiarkanmu menang!"
            scene expression ("images/episode1/223.webp") with dissolve
            patricia "Saya yakin ... Anda ayam!"
            toby "Itu saja!"
        "{4} Cobalah menang {3}":
            scene expression ("images/episode1/221.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode1/224.webp") with dissolve
            patricia "Aku membiarkanmu menang. Saya bosan berbicara tentang pacar Anda!"
            toby "Ya, benar!"
            scene expression ("images/episode1/225.webp") with dissolve
            patricia "Maksudku, aku bosan membicarakan pelacurmu!"
            toby "Itu saja ... Anda akan mendapatkannya untuk itu!"

    scene expression ("images/episode1/226.webp") with dissolve
    patricia "Membantu!"
    toby "Tidak ada orang di sini kecuali kami!"
    patricia "Dia mencoba memperkosa saya!"
    scene expression ("images/episode1/227_1.webp") with dissolve
    toby "Apakah kamu gila!? Bagaimana jika seseorang mendengar Anda?"
    scene expression ("images/episode1/227_2.webp") with dissolve
    patricia "Saya pikir Anda mengatakan bahwa tidak ada orang di sini!"
    scene expression ("images/episode1/228.webp") with dissolve
    toby "Banyak ayam?"
    scene expression ("images/episode1/229.webp") with dissolve
    patricia "Aaaa!"
    scene expression ("images/episode1/230.webp") with dissolve
    toby "Jadi? Mari kita dengar. Apakah ada sesuatu yang ingin Anda katakan?"
    scene expression ("images/episode1/231.webp") with dissolve
    patricia "Apa yang akan kamu lakukan padaku sekarang?"
    scene expression ("images/episode1/232.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nShit the way she looks at me made me so horny and now I have a boner!{3}"
    scene expression ("images/episode1/233.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nShe noticed. Fuck, fuck, fuck my life.{3}"
    if patricia_rel == 3:
        scene expression ("images/episode1/234.webp") with dissolve
        patricia "Apakah Anda tertarik kepada saya bahwa Anda mendapat boner hanya dari saya bertingkah tak berdaya?"
        toby "TIDAK!"
        scene expression ("images/episode1/235.webp") with dissolve
        patricia "Ya Tuhan ... ini sangat lucu! Haha, pengisap!"
        scene expression ("images/episode1/237.webp") with dissolve
        patricia "Malam ini, kamu tidur di lantai, kau tanduk anjing!"
    else:
        scene expression ("images/episode1/236.webp") with dissolve
        patricia "Ewww. Apa yang salah denganmu? I \ 'M Anda [17]!"
        toby "Maaf, ini bukan karena Anda!"
        patricia "Saya tidak peduli, lepas dari saya!"
        scene expression ("images/episode1/238.webp") with dissolve
        patricia "Malam ini Anda sedang tidur di lantai."
    scene expression ("images/episode1/239.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nReally? Are you going to do me like that?{3}"
    scene expression ("images/episode1/240.webp") with long_dissolve
    toby "Apakah Anda membutuhkan bantuan dengan itu?"
    $ progress = 16
    if charlotte_rel < 2:
        charlotte "Jangan khawatir. Saya bisa melakukannya sendiri!"
        toby "Mau mu!"
        pass
    else:

        scene expression ("images/episode1/241.webp") with dissolve
        charlotte "Bagaimana saya bisa mengatakan tidak kepada Anda?"
        scene expression ("images/episode1/242.webp") with dissolve
        toby "Ingin beberapa juga setelahnya?"
        scene expression ("images/episode1/243.webp") with dissolve
        patricia "{2}{6}* whispering *{5}{1}{4}\nYou're too horny right now. Maybe some other time.{3}"
        scene expression ("images/episode1/244.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode1/245.webp") with dissolve
        charlotte "Apa yang dia katakan?"
        toby "Sesuatu seperti dia tidak pantas mendapatkan tabir surya karena dia kalah di bola voli!"
        scene expression ("images/episode1/246.webp") with dissolve
        if ep1_let_patricia_win == True:
            patricia "Idiot."
        else:
            patricia "Saya mengatakan bahwa saya bahkan tidak pantas pulang dengan Anda dengan mobil yang sama."
            toby "Jangan khawatir, aku akan menutup mata kali ini!"

        label memory_02:

            if _in_replay:

                $ ep1_get_charlotte_drunk=True

            scene expression ("images/episode1/247.webp") with dissolve
            charlotte "Jika tidak satu pun dari kedua wanita itu mempekerjakan Anda, saya pikir Anda akan melakukannya dengan cukup baik sebagai tukang pijat."
            toby "Dan saya hanya menerapkan tabir surya. Bayangkan jika saya benar -benar memberi Anda pijatan."
            scene expression ("images/episode1/248.webp") with dissolve
            charlotte "Karena kami bangkrut, saya pikir saya akan membiarkan Anda memijat saya suatu hari nanti."
            toby "Apakah punggung Anda masih sakit?"
            charlotte "Terkadang, setelah berdiri terlalu banyak."
            if ep1_get_charlotte_drunk == False:
                scene expression ("images/episode1/249.webp") with dissolve
                charlotte "Terima kasih atas tabir surya!"
                toby "Tidak ada masalah [6]."
            else:
                scene expression ("images/episode1/250.webp") with dissolve
                toby "{2}{6}* thinking *{5}{1}{4}\nWhat is [6] doing?{3}"
                charlotte "Saya tidak menginginkan garis tan!"
                scene expression ("images/episode1/251.webp") with dissolve
                toby "Ya, tentu [6]!"
                scene expression ("images/episode1/252.webp") with dissolve
                charlotte "{2}{6}* whispering *{5}{1}{4}\nMake sure you don't miss a spot!{3}"
                scene expression ("images/episode1/253.webp") with dissolve
                toby "{2}{6}* thinking *{5}{1}{4}\nIs she serious right now?{3}"
                toby "{2}{6}* thinking *{5}{1}{4}\nHer ass is huge!{3}"
                scene expression ("images/episode1/254.webp") with dissolve
                charlotte "{2}{6}* whispering *{5}{1}{4}\nGood boy.{3}"
                toby "{2}{6}* thinking *{5}{1}{4}\nI'm not sure what was in that cocktail, but I think was really strong.{3}"
                scene expression ("images/episode1/255.webp") with dissolve
                toby "{2}{6}* thinking *{5}{1}{4}\nI feel kinda dirty and aroused at the same time. I'm touching my [6]'s firm ass.{3}"
                toby "{2}{6}* thinking *{5}{1}{4}\nThis is not what I was thought was going to happen at the beach.{3}"
                menu:
                    "{4} [3] maju {3}"(csq="Charlotte +1 & Galeri Gambar"):
                        $ charlotte_rel += 1
                        $ ep1_groping_charlotte = True
                        $ unlockImage(persistent.charlotte_03)
                        scene expression ("images/episode1/256.webp") with dissolve
                        toby "{2}{6}* thinking *{5}{1}{4}\nWhat the hell... You only live once.{3}"
                        scene expression ("images/episode1/257.webp") with dissolve
                        toby "{2}{6}* thinking *{5}{1}{4}\nI'm touching my [6]'s breast!{3}"
                        toby "{2}{6}* thinking *{5}{1}{4}\nAnd it doesn't seem like she's bothered by that.{3}"
                        scene expression ("images/episode1/258.webp") with dissolve
                        toby "{2}{6}* thinking *{5}{1}{4}\nOkay... I know where this is going.{3}"
                        scene expression ("images/episode1/259.webp") with dissolve
                        toby "{2}{6}* thinking *{5}{1}{4}\nI can't believe how big and soft her boobs are.{3}"
                        charlotte "{2}{6}* moaning slightly *{5}{1}\n{4}Mhmmm.{3}"
                        scene expression ("images/episode1/260.webp") with dissolve
                        toby "{2}{6}* thinking *{5}{1}{4}\nI should stop before Tris turns over.{3}"
                    "{4} stop {3}" if not _in_replay:
                        pass
                scene expression ("images/episode1/261.webp") with dissolve
                charlotte "Terima kasih sayang!"
                toby "Tidak ada masalah [6]."
                $ unlockMemory(persistent.memory_02)

            $ renpy.end_replay()

    scene expression ("images/episode1/262.webp") with dissolve
    toby "{2}{6}* thinking *{5}{1}{4}\nWhat a day. I feel like this city has had a big impact on me.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nAnyway, I wonder which job I should choose tomorrow.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nOn one hand having a more stable income would be great and on top of that I'll have a career.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nBut Katrina's words keep popping in my head. She did promise me plenty of money. But at what cost?{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nI mean, look at [1], when his business was good he behaved differently than now. So it's safe to say that my job will have an impact on my attiude.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nWhat if after spending so much time in the club, with whores and drunk ladies I'll start to treat the girls at home the same way or even Emma.{3}"
    toby "{2}{6}* thinking *{5}{1}{4}\nI'm not sure what to choose. I mean, both jobs look promising enough. I'll figure it out tomorrow.{3}"
    $ progress = 17
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
