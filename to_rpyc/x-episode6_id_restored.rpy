image ep6_005 = Movie(play="video/episode6/005.webm", image="images/episode6/005.webp", loop = False)
image ep6_022 = Movie(play="video/episode6/022.webm", loop = True)
image ep6_023 = Movie(play="video/episode6/023.webm", loop = True)
image ep6_025 = Movie(play="video/episode6/025.webm", loop = True)
image ep6_026 = Movie(play="video/episode6/026.webm", loop = True)
image ep6_033 = Movie(play="video/episode6/033.webm", loop = True)
image ep6_034 = Movie(play="video/episode6/034.webm", loop = True)
image ep6_035 = Movie(play="video/episode6/035.webm", loop = True)
image ep6_036 = Movie(play="video/episode6/036.webm", loop = True)
image ep6_037 = Movie(play="video/episode6/037.webm", loop = True)

label episode6:
    $ progress = 83
    stop music fadeout 4.0
    scene expression ("images/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(1, 6) with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    show screen ui_message("Tuesday") with long_dissolve
    hide screen ui_newEpisode
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message

    if toby_job == 0:
        $ katrina_path = False
    else:
        $ darlene_path = False

    if emma_break == False:
        call episode6_date_emma from _call_episode6_date_emma

    if toby_job == 0:
        call episode6_realEstate from _call_episode6_realEstate
    else:

        call episode6_club from _call_episode6_club

    call episode6_dinnerPreparations from _call_episode6_dinnerPreparations

    call episode6_dinner from _call_episode6_dinner

    call episode6_backHome from _call_episode6_backHome

    call episode6_charlotte from _call_episode6_charlotte

    if ep6_caughtJerking:
        call episode6_nightTris from _call_episode6_nightTris



    call episode6_weeks from _call_episode6_weeks

    return

label episode6_date_emma:

    scene expression ("images/episode6/001.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/002.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/003.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/004.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    show ep6_005 with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode6/005.webp") with dissolve
    hide ep6_005

    emma "Aku sangat merindukanmu, cintaku."
    toby "Aku juga merindukanmu."
    toby "Kamu terlihat sangat baik."

    scene expression ("images/episode6/006.webp") with dissolve
    emma "Saya mencoba yang terbaik."
    emma "Ketika pria Anda merawat dirinya sendiri, saya juga harus melakukannya. Saya perlu terlihat terbaik untuk Anda."
    scene expression ("images/episode6/007.webp") with dissolve
    toby "Ya ... apa yang bisa saya katakan. Saya mandi pagi ini."
    scene expression ("images/episode6/008.webp") with dissolve
    emma "Berbicara tentang hujan. Saya benar -benar perlu mengambilnya juga. Saya bau setelah perjalanan."
    scene expression ("images/episode6/007.webp") with dissolve
    toby "Omong kosong! Anda berbau seperti bunga."
    scene expression ("images/episode6/008.webp") with dissolve
    emma "Mungkin seperti bunga mati."
    scene expression ("images/episode6/009.webp") with dissolve
    toby "Baik ... lepaskan. Saya memesan kami kamar hotel untuk malam ini."
    emma "Ah, benarkah?"
    toby "Nah, apartemen kami agak kecil dan kamar masa depan saya perlu masih membutuhkan cinta, jadi ya."
    emma "Apakah itu berarti saya tidak akan melihat [mom] Anda?"
    scene expression ("images/episode6/010.webp") with dissolve
    toby "Oh kamu akan ... dia membuatku berjanji untuk membawamu. Dia rindu mengolok -olok saya dengan Anda di sekitar."
    emma "Dia yang termanis."
    toby "Dan selain itu saya meninggalkan sepeda pulang, karena saya tidak tahu berapa banyak bagasi yang Anda miliki sehingga kami perlu mendapatkannya setelah Anda mandi."
    scene expression ("images/episode6/011.webp") with dissolve
    toby "Dan berhubungan seks."
    emma "Dua kali."
    toby "Hemat energi untuk malam ini."
    emma "Anda tidak tahu berapa banyak energi yang saya hemat selama tiga minggu terakhir ini."
    scene expression ("images/episode6/012.webp") with dissolve
    toby "Aku sangat merindukanmu."
    emma "Aku juga sayang. Tidak bisa menunggu untuk pindah ke sini."

    scene expression ("images/episode6/013.webp") with fade
    emma "Astaga. Tempat ini terlihat luar biasa. Ini pasti harganya harganya."
    toby "Jangan khawatir tentang uang itu. Ini adalah yang paling tidak bisa saya lakukan untuk Anda."
    scene expression ("images/episode6/014.webp") with dissolve
    emma "Anda benar -benar tidak boleh memilikinya. Maksudku, aku bisa dengan mudah tidur di pantai, selama aku bersamamu."
    toby "Mari kita katakan bahwa saya memesan hotel ini jadi saya tidak harus tidur di pasir."
    scene expression ("images/episode6/015_1.webp") with fade
    toby "Nah, ini dia!"
    scene expression ("images/episode6/015_2.webp") with dissolve
    emma "Kamar ini sangat besar. Ini lebih besar dari apartemen saya."
    scene expression ("images/episode6/016.webp") with dissolve
    emma "Aku akan mandi. Ketika saya kembali, saya berharap Anda tidak mengenakan apa -apa."
    emma "Bahkan bukan kondom."
    scene expression ("images/episode6/017.webp") with dissolve
    toby "Jangan terlalu lama."
    scene expression ("images/episode6/018.webp") with dissolve
    emma "Kembali!"
    stop music fadeout 2.0

    show screen ui_message("2 minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    label memory_20:
        scene expression ("images/episode6/019.webp") with dissolve
        hide screen ui_message
        $ progress = 84


        toby "Jika Anda benar -benar berpikir saya bisa menunggu lagi, Anda keluar dari pikiran Anda."
        scene expression ("images/episode6/020.webp") with dissolve
        emma "Saya berharap Anda bergabung, tetapi saya berharap setidaknya punya waktu untuk dibersihkan."
        scene expression ("images/episode6/021.webp") with dissolve
        toby "Jadi mengapa Anda tidak mengatakan apa -apa?"
        emma "Karena saya ingin melihat apakah Anda benar -benar menginginkan saya sebanyak yang saya inginkan."
        menu:
            "{i} [JGR] Dirty Talk {/i}"(csq="Emma +1 & Galeri Gambar"):
                $ ep6_emma_dirtyTalk = True
                $ emma_rel += 1
                $ unlockImage(persistent.emma_06)
                toby "Anda menguji saya, pelacur?"
                toby "Mengapa Anda tidak mengambil penis saya di mulut Anda dan melihat apakah itu siap untuk Anda!"
            "{i} Clean Talk {/i}":
                toby "Oh, aku menginginkanmu!"
                emma "Saya bisa melihat itu."

        scene expression ("images/episode6/022.webp")
        show ep6_022
        $ ui.saybehavior()
        $ ui.interact()
        if ep6_emma_dirtyTalk == True:
            toby "Itu pelacur itu! Menghisapnya. Anda menyukai rasa penis saya?"
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nMhmmm..."
            toby "Tentu saja Anda melakukannya!"
        else:
            toby "Persetan denganku ... ini sangat bagus. Aku sangat mencintaimu."
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nMhmmm..."

        scene expression ("images/episode6/023.webp")
        hide ep6_022

        show ep6_023
        if ep6_emma_dirtyTalk == True:
            toby "Ayamku merindukan bibirmu. Bibir slutty Anda."
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nMmmm..."
            toby "Kami akan melakukan sesuatu yang Anda nikmati."
        else:
            $ ui.saybehavior()
            $ ui.interact()

        scene expression ("images/episode6/024.webp") with dissolve
        hide ep6_023

        if ep6_emma_dirtyTalk == True:
            emma "Apakah Anda akan bercinta dengan mulut saya?"
            toby "Anda menginginkannya dengan benar?"
            emma "Tentu saja."
        else:
            emma "Saya punya ide. Ingat saat Anda kacau mulut saya?"
            toby "Apa kamu yakin?"
            emma "Ya."

        scene expression ("images/episode6/025.webp")
        show ep6_025
        if ep6_emma_dirtyTalk == True:
            toby "Anda suka ini, pelacur? Anda menyukai saya bercinta dengan mulut Anda?"
            emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nMhmmm..."
            toby "Anda suka digunakan?"
            emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nMhmmm..."
        else:
            toby "Beri tahu saya jika saya terlalu kasar."
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nMhmmm..."

        scene expression ("images/episode6/026.webp")
        hide ep6_025

        show ep6_026
        $ ui.saybehavior()
        $ ui.interact()
        if ep6_emma_dirtyTalk == True:
            toby "Saya akan mengisi mulut slutty Anda dengan air mani saya."
            emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nMhmm..."
        else:
            toby "Saya akan pergi ke cum."
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nMhmm..."
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's not stopping. She wants me to cum in her mouth. I love her.{/i}"

        scene expression ("images/episode6/027.webp") with dissolve
        hide ep6_026

        with flash
        with flash
        $ ui.saybehavior()
        $ ui.interact()
        if ep6_emma_dirtyTalk == True:
            toby "Anak yang baik!"

        scene expression ("images/episode6/028.webp") with dissolve
        emma "Itu sangat bagus. Saya sangat merindukan rasa cum Anda."
        toby "Anda seorang gadis yang kotor!"
        scene expression ("images/episode6/029.webp") with dissolve
        emma "Saya akan membersihkan sekarang dan kemudian kita dapat pindah ke putaran kedua ketika saya selesai."
        scene expression ("images/episode6/030.webp") with dissolve
        if ep6_emma_dirtyTalk == True:
            toby "Apakah penisku terlihat sudah cukup?"
            scene expression ("images/episode6/031.webp") with dissolve
            emma "Seseorang sangat merindukanku."
            scene expression ("images/episode6/032.webp") with dissolve
            toby "Anda tidak tahu."
        else:
            toby "Itu bukan rencana paling cerdas. Jika Anda mandi maka saya bercinta dengan Anda, Anda hanya perlu mandi lagi."
            scene expression ("images/episode6/031.webp") with dissolve
            emma "Dan apa yang Anda usulkan?"
            toby "Nah, saya tidak bisa membiarkan Anda tetap seperti itu. Aku juga perlu menjagamu."
            scene expression ("images/episode6/032.webp") with dissolve
            emma "Aku sangat terangsang sekarang!"

        scene expression ("images/episode6/033.webp")
        show ep6_033

        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck you're so big. I missed you being inside me."
        if ep6_emma_dirtyTalk == True:
            toby "Anda adalah pelacur yang lapar. Anda tahu itu benar?"
            emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nI'm your dirty slut, so then it's perfect."
        else:
            toby "Anda sangat ketat."
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes, yes... Right there."

        scene expression ("images/episode6/034.webp")
        hide ep6_033
        show ep6_034

        if ep6_emma_dirtyTalk == True:
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck me [toby!c]. Fuck me, my love!"
        else:
            emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nI love you so much!"
            toby "Aku juga mencintaimu sayang!"

        scene expression ("images/episode6/035.webp")
        hide ep6_034
        show ep6_035

        if ep6_emma_dirtyTalk == True:
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nDon't stop. {w} Don't stop. {w}Right there."
            toby "Anda suka penis saya, pelacur?"
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI fucking love it!"
        else:
            emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes, yes... Just like that."
            emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYou're perfect."

        scene expression ("images/episode6/036.webp")
        hide ep6_035
        show ep6_036
        if ep6_emma_dirtyTalk == True:
            toby "Vagina Anda terasa sangat enak di penisku."
            emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nIt was made for it."
        else:
            $ ui.saybehavior()
            $ ui.interact()

        scene expression ("images/episode6/037.webp")
        hide ep6_036
        show ep6_037
        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI'm going to cum."
        toby "Saya juga."
        if ep6_emma_dirtyTalk:
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nCum inside. Cum inside your slut. Fill me up."
        else:
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nCum inside me. Fill me up."

        with flash
        scene expression ("images/episode6/038.webp")
        hide ep6_037
        with flash
        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nOh my... that was so good."
        toby "Itu bagus."
        emma "Aku mencintaimu sayang."
        toby "Aku juga mencintaimu sayang."
        scene expression ("images/episode6/039.webp") with dissolve
        toby "Aku akan membiarkanmu mandi sekarang."
        emma "Terima kasih!"
        scene expression ("images/episode6/040.webp") with dissolve
        toby "Dengan senang hati!"

        $ unlockMemory(persistent.memory_20)
        $ renpy.end_replay()

    show screen ui_message("20 minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode6/041.webp")
    hide screen ui_message

    toby "Sudah selesai?"
    toby "Jadi? Haruskah kita mengambil sepeda saya dan kemudian pergi ke restoran, atau apakah Anda lebih suka makan dulu?"
    scene expression ("images/episode6/042_1.webp") with dissolve
    emma "Apa pun yang Anda inginkan, itu akan bagus. Aku tidak terlalu lapar."
    scene expression ("images/episode6/042_2.webp") with dissolve
    "*menggeram perut*"
    scene expression ("images/episode6/043_1.webp") with dissolve
    toby "Tidak ... Anda tidak lapar sama sekali."
    scene expression ("images/episode6/044.webp") with dissolve
    emma "Bagus. Mungkin sedikit."
    scene expression ("images/episode6/043_2.webp") with dissolve
    toby "Kami akan makan sesuatu terlebih dahulu. Untuk apa Anda ingin?"
    toby "Saya tahu restoran yang bagus yang melakukan steak yang bagus. Saya pergi ke sana dengan [mom] beberapa hari yang lalu."
    scene expression ("images/episode6/045.webp") with dissolve
    emma "Kamu tahu bahwa aku mencintaimu kan?"
    toby "Ya?"
    emma "Mari kita tetap santai. Anda tidak harus membuat saya terkesan, mari kita mendapatkan burger dan kentang goreng."
    toby "Anda yakin?"
    emma "Positif!"
    scene expression ("images/episode6/046.webp") with dissolve
    emma "Lagi pula, ini tidak seperti saya seorang penggali emas. Benar?"
    toby "Berapa lama lagi Anda akan menggosoknya?"
    emma "Saya akan memikirkannya dan memberi tahu Anda."
    scene expression ("images/episode6/047.webp") with dissolve
    toby "Bagus. Saya pantas mendapatkannya!"

    scene expression ("images/episode6/048.webp") with fade
    clerk "Selamat siang. Apa yang bisa saya dapatkan dari Anda?"
    scene expression ("images/episode6/049.webp") with dissolve
    toby "Saya akan mengambil makanan cheeseburger sedang dengan kentang goreng dan coke."
    scene expression ("images/episode6/050.webp") with dissolve
    toby "Dan makanan ganda cheeseburger ganda untuk wanita itu. Sebenarnya, buatlah dua ganda besar. Keduanya dengan kentang goreng."
    scene expression ("images/episode6/051.webp") with dissolve
    toby "Dia agak lapar."
    scene expression ("images/episode6/052.webp") with dissolve
    emma "Tolong jangan dengarkan dia. Saya akan memiliki hal yang sama. Satu media dengan kentang goreng dan kokas."
    scene expression ("images/episode6/050.webp") with dissolve
    toby "Anda yakin?"
    scene expression ("images/episode6/053.webp") with dissolve
    emma "Saya positif."
    scene expression ("images/episode6/048.webp") with dissolve
    clerk "Oke kalau begitu. Dua makanan cheeseburger sedang dengan kentang goreng dan kokas, muncul segera."

    scene expression ("images/episode6/054.webp") with dissolve
    emma "Terlihat madu. Saya tahu Anda mencoba membuat saya terkesan dengan fakta bahwa Anda punya uang dan Anda mampu membeli dua kali makan, tetapi seperti yang saya katakan, saya sudah."
    toby "Anda sangat bodoh."
    emma "Aku mencintaimu!"
    toby "Ya ... aku juga!"

    scene expression ("images/episode6/055.webp") with dissolve
    emma "Oke, saya tidak bisa melihat makanan ini lagi. Biarkan makan!"
    toby "Bon Appétit!"

    show screen ui_message("10 minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode6/056_0.webp") with dissolve

    hide screen ui_message

    toby "Ummm ... Sayang. Ini adalah pertama kalinya Anda sudah selesai makan sebelum saya."
    scene expression ("images/episode6/057.webp") with dissolve
    emma "Nah, saya belum makan apa pun sejak kemarin!"
    scene expression ("images/episode6/056.webp") with dissolve
    toby "Kalau begitu aku akan memberimu makanan lagi."
    scene expression ("images/episode6/057.webp") with dissolve
    emma "Berhentilah bersikap konyol. Ayo pergi saja. Saya tidak sabar untuk bersenang -senang dengan [mom] Anda."
    scene expression ("images/episode6/056.webp") with dissolve
    toby "Tidak. Saya hanya mengambil kunci saya dan kami keluar dari sana!"
    scene expression ("images/episode6/058.webp") with dissolve
    emma "Silakan? Setidaknya sepuluh menit."
    scene expression ("images/episode6/056.webp") with dissolve
    toby "Lima!"
    scene expression ("images/episode6/058.webp") with dissolve
    emma "Delapan."
    scene expression ("images/episode6/056.webp") with dissolve
    toby "Tujuh."
    scene expression ("images/episode6/058.webp") with dissolve
    emma "Tujuh setengah?"
    scene expression ("images/episode6/059.webp") with dissolve
    toby "Bagus."
    scene expression ("images/episode6/060.webp") with dissolve
    emma "Sempurna! Biarkan saja!"

    $ progress = 85
    scene expression ("images/episode6/061.webp") with fade
    emma "Biarkan saya menebak ... bocah nakal ini milikmu?"
    toby "Sebenarnya dia seorang wanita. Wanita buruk."
    emma "Haruskah saya cemburu?"
    scene expression ("images/episode6/062.webp") with dissolve
    toby "Mungkin kamu harus. Saya sudah sering mengendarainya belakangan ini."
    emma "Ya, tapi kamu berpakaian."
    toby "Mungkin. Bisakah kamu yakin?"
    scene expression ("images/episode6/063.webp") with fade
    toby "Hei [mom]. Lihat apa yang diseret kucing itu."
    scene expression ("images/episode6/064.webp") with dissolve
    charlotte "Saya suka kucing ini. Dia menyeret hal -hal terbaik."
    charlotte "Hai sayang! Selamat datang."
    scene expression ("images/episode6/065.webp") with dissolve
    emma "Hai ma \ 'am."
    charlotte "Bisa aja. Itu baik [mom] atau Charlotte."
    emma "Hai Charlotte! Apa kabarmu?"
    scene expression ("images/episode6/066.webp") with dissolve
    charlotte "Lihatmu. Anda sangat menggemaskan. Sudahkah Anda melakukan sesuatu dengan rambut Anda?"
    emma "Umm ... oh yeah ... beberapa minggu yang lalu, tapi kami tidak bertemu satu sama lain sejak saya melakukannya."
    scene expression ("images/episode6/067_1.webp") with dissolve
    charlotte "Dan apakah [son] saya memperhatikan perubahan itu?"
    scene expression ("images/episode6/067_2.webp") with dissolve
    emma "Tidak terlalu."
    scene expression ("images/episode6/067_1.webp") with dissolve
    charlotte "PFF ... Men!"
    scene expression ("images/episode6/068_1.webp") with dissolve
    toby "Enam menit tersisa!"
    scene expression ("images/episode6/069.webp") with dissolve
    emma "Dia memberi saya hanya tujuh setengah menit untuk berbicara dengan Anda. Sesuatu tentang kita mengolok -oloknya."
    charlotte "Ya, dia sensitif seperti itu."
    scene expression ("images/episode6/068_2.webp") with dissolve
    toby "Aku tidak sensitif dan aku bisa mendengarmu!"
    scene expression ("images/episode6/067_1.webp") with dissolve
    charlotte "Bayar dia tidak keberatan ... Anda terlalu cantik untuk mendengarkan omong kosongnya."
    scene expression ("images/episode6/067_2.webp") with dissolve
    emma "Jadi saya harus mengabaikan aturan 7 menit?"
    scene expression ("images/episode6/070.webp") with dissolve
    charlotte "Tentu saja tidak! Biarkan saya memberi tahu Anda sebuah rahasia."
    scene expression ("images/episode6/071.webp") with dissolve
    charlotte "Anda menunggu di sana. Anda tidak diizinkan mendengar rahasianya."
    toby "Bukan kesempatan, saya tidak membiarkan Anda mengajarkan hal -hal bodohnya."
    scene expression ("images/episode6/072.webp") with dissolve
    charlotte "Anda pintar, cantik, memiliki payudara yang bagus, payudara.Jadi sayang. Lihatmu. Anda memiliki semua yang bisa diimpikan oleh pria."
    scene expression ("images/episode6/073.webp") with dissolve
    toby "[mom!c]!"
    scene expression ("images/episode6/074.webp") with dissolve
    charlotte "Kamu, silam. Sudah kubilang jangan datang ke sini."
    scene expression ("images/episode6/072.webp") with dissolve
    charlotte "Jadi seperti yang saya katakan, Anda memiliki semua yang diinginkan dan dibutuhkan pria. Jika dia tidak membiarkan Anda melakukan sesuatu, Anda hanya memotong sesuatu yang dia suka."
    charlotte "Jika dia suka ketika Anda mencium lobus telinganya, Anda berhenti melakukan itu ketika dia membuat Anda kesal."
    charlotte "Jika dia membuatmu semakin kesal, kamu bisa dengan mudah mengatakan \"Sayang, kepalaku sakit."
    scene expression ("images/episode6/075.webp") with dissolve
    emma "Sama seperti itu?"
    scene expression ("images/episode6/072.webp") with dissolve
    charlotte "Tentu saja."
    scene expression ("images/episode6/076.webp") with dissolve
    emma "Sayang, kami akan tinggal lebih dari tujuh setengah menit."
    emma "Kami akan tinggal sepuluh menit."
    scene expression ("images/episode6/077.webp") with dissolve
    toby "Apa pun. Aku seharusnya tidak membawamu ke sini sama sekali."
    scene expression ("images/episode6/072.webp") with dissolve
    charlotte "Langkah kecil.Itu sempurna. Anda harus mengambil langkah kecil. Jika Anda mengatakan sekitar 30 menit, dia akan terlalu gugup."

    show screen ui_message("1 hour later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode6/078.webp") with dissolve
    hide screen ui_message


    charlotte "Terima kasih telah mengunjungi saya sayang."
    emma "Selalu menyenangkan."
    charlotte "Jangan menjadi orang asing. Pintu saya selalu terbuka untuk Anda."
    toby "Ya, ya. Biarkan sekarang!"
    charlotte "Dia masih pemarah, tapi aku yakin dia akan melupakannya hanya dengan ciuman."
    emma "Saya bisa mengurusnya."
    scene expression ("images/episode6/079.webp") with dissolve
    emma "Bye Mrs. Charlotte."
    charlotte "Itu hanya Charlotte."
    emma "Bye Charlotte."
    charlotte "Bye Honey!"
    toby "Sampai jumpa besok [mom]."
    charlotte "Jaga permata ini dengan baik."

    $ progress = 86

    scene expression ("images/episode6/080.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/081.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    emma "Saya harap itu tidak mengganggu Anda sehingga saya rukun dengan [mom] Anda. Dia sangat manis."
    toby "Jangan khawatir, saya hanya bertindak kesal. Sungguh luar biasa bahwa kalian berdua benar -benar rukun."
    emma "Masalahnya, saya tidak pernah tahu seperti apa rasanya memiliki seorang ibu. Dan mengobrol dengan [mom] Anda, saya bisa membayangkan seperti apa nantinya."

    scene expression ("images/episode6/082.webp") with dissolve
    toby "Saya mengerti, saya minta maaf untuk itu. Karena Anda mengangkatnya, Anda tidak pernah memberi tahu saya apa yang terjadi. Saya hanya tahu bahwa ibumu meninggal melahirkan Anda dan bahwa Anda tidak memiliki hubungan yang baik dengan ayah Anda."
    emma "Mari kita duduk."

    scene expression ("images/episode6/083.webp") with dissolve
    emma "Saya sangat kesal ketika Anda tidak mengatakan yang sebenarnya tentang mengapa Anda pindah, tetapi untuk bersikap adil saya tidak pernah berbicara dengan Anda tentang keluarga saya juga."
    toby "Anda selalu menghindari subjek sehingga saya tidak pernah mendorongnya."

    scene expression ("images/episode6/084_sad.webp") with dissolve
    emma "Dan untuk alasan yang bagus."
    emma "Bukannya aku tidak mempercayaimu, hanya saja keluargaku sangat hancur."
    emma "Ketika ibuku meninggal, itu merobek ayahku."
    scene expression ("images/episode6/084_sad2.webp") with dissolve
    emma "Para dokter mengatakan kepadanya bahwa akan lebih baik untuk membatalkan saya, karena pengiriman mungkin membunuhnya. Tapi dia tidak peduli. Dia merasa dia cukup kuat untuk bertarung melewatinya."
    emma "Dia bilang dia cukup kuat untuk melahirkanku dan hidup untuk membesarkanku."
    scene expression ("images/episode6/084_sad.webp") with dissolve
    emma "Ayah mencoba meyakinkannya untuk melakukan aborsi, tetapi dia terlalu keras kepala."
    scene expression ("images/episode6/084_sadSmile.webp") with dissolve
    emma "Saya mendapatkan sifat yang sama dari ibu saya."
    scene expression ("images/episode6/084_sad2.webp") with dissolve
    emma "Ngomong -ngomong, ayah saya mencoba meyakinkannya untuk menjalani aborsi, tetapi dia menolak, dia terlalu mencintaiku, meskipun dia belum bertemu dengan saya."
    emma "Hal yang aneh, cinta keibuan."
    scene expression ("images/episode6/084_sad.webp") with dissolve
    emma "Bulan -bulan berlalu dan saya akan dilahirkan dan ketakutan dokter menjadi kenyataan. Mereka tidak bisa menyelamatkannya."
    emma "Dan ya ... ayah saya telah membenci saya sepanjang hidup saya. Dia menatapku seperti aku membunuh istrinya."
    scene expression ("images/episode6/085_sad.webp") with dissolve
    toby "Itu adalah hal paling bodoh yang pernah ada. Pertama -tama, itu bukan pilihan Anda dan kedua bagaimana Anda bisa membenci anak Anda sendiri?"
    scene expression ("images/episode6/084_sadSmile.webp") with dissolve
    emma "Setidaknya saya punya cindy saya!"
    scene expression ("images/episode6/085_normal.webp") with dissolve
    toby "Adikmu?"
    scene expression ("images/episode6/084_sadSmile.webp") with dissolve
    emma "Yup. Itu lucu karena dia selalu merawat saya, tetapi dia hanya seperti satu tahun lebih tua dari saya."
    emma "Maksudku, dia dan bibiku. Dia pindah untuk membantu ayah saya bersama kami."
    scene expression ("images/episode6/085_curious.webp") with dissolve
    toby "Bibi di sisi ibumu?"
    scene expression ("images/episode6/084_normal.webp") with dissolve
    emma "Tidak. Adik ayahku. Tapi dia tidak seperti dia."
    emma "Dia merawat saya sampai dia menikah 6 tahun kemudian. Dia ingin membawa kami bersamanya, tetapi ayah saya tidak pernah setuju."
    scene expression ("images/episode6/085_normal.webp") with dissolve
    toby "Yah, mungkin dia menyadari bahwa itu bukan salahmu bahwa ibumu meninggal."
    scene expression ("images/episode6/084_sad2.webp") with dissolve
    emma "Ya, saya berharap."
    scene expression ("images/episode6/085_normal.webp") with dissolve
    toby "Apa yang dia lakukan?"
    scene expression ("images/episode6/084_sad2.webp") with dissolve
    emma "Tidak ada apa-apa. Mari kita katakan bahwa saya terlihat persis seperti ibu dan ayah saya terlalu merindukannya."
    scene expression ("images/episode6/085_surprised.webp") with dissolve
    toby "Tolong beritahu saya ini tidak akan terjadi di mana saya pikir itu akan terjadi."
    scene expression ("images/episode6/084_sad.webp") with dissolve
    emma "Seperti yang saya katakan, saya memiliki saudara perempuan yang sangat baik yang merawat saya."
    emma "Ketika dia mengetahui apa yang dikatakan ayah saya setiap kali dia mabuk, kami memutuskan untuk melarikan diri."
    scene expression ("images/episode6/085_curious.webp") with dissolve
    toby "Sudahkah Anda berbicara dengan ayah Anda sejak itu?"
    scene expression ("images/episode6/084_sadSmile.webp") with dissolve
    emma "Tidak dan saya tidak bermaksud."
    scene expression ("images/episode6/085_normal.webp") with dissolve
    toby "Kemarilah sayang."

    scene expression ("images/episode6/086.webp") with dissolve
    toby "Saya sangat menyesal tentang semua itu. Saya tidak pernah tahu."
    emma "Jangan khawatir. Tidak ada yang tahu kecuali Anda. Anda adalah orang pertama yang saya katakan semua itu."
    toby "Aku akan merawatmu dengan baik."
    emma "Aku mencintaimu!"
    scene expression ("images/episode6/087.webp") with dissolve
    emma "Ya, jadi ini aku. Seorang gadis yang hancur. Itu sebabnya saya sedikit lekat, karena Anda adalah alasan saya tersenyum."
    toby "..."
    scene expression ("images/episode6/088.webp") with dissolve
    emma "Maaf jika saya menghancurkan hari itu. Aku tidak akan memberitahumu, tapi rasanya seperti waktu yang tepat."
    toby "Anda tidak merusak apapun."
    scene expression ("images/episode6/089.webp") with dissolve
    emma "Mungkin hanya dorongan seks?"
    toby "Nah, malam ini mungkin saya merasa seperti memeluk alih -alih berhubungan seks."
    toby "Saya merasa perlu melindungi Anda yang dibungkus dengan lengan saya."
    scene expression ("images/episode6/088.webp") with dissolve
    emma "Aku sangat mencintaimu."
    toby "Saya juga!"

    scene expression ("images/episode6/090.webp") with long_dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/091.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/092.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/093.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/094.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    return


label episode6_realEstate:
    $ progress = 87

    scene expression ("images/episode6/095.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode6/096.webp") with dissolve
    darlene "Jadi Kat memberitahuku kalian berdua bertemu di gym."
    scene expression ("images/episode6/097.webp") with dissolve
    toby "Oh ya. Saya tidak tahu kalian pergi ke gym yang sama?"
    scene expression ("images/episode6/098.webp") with dissolve
    darlene "Ya. Ini tidak terlalu ramai karena kebijakan ruang ganti bersama. Kat menyukainya."
    scene expression ("images/episode6/099.webp") with dissolve
    darlene "Ngomong -ngomong, apa yang kamu lakukan nanti malam?"
    scene expression ("images/episode6/097.webp") with dissolve
    toby "Saya tidak punya rencana, mengapa?"
    scene expression ("images/episode6/099.webp") with dissolve
    darlene "Bukankah dia memberitahumu? Saya ingin mengundang Anda untuk makan malam."
    scene expression ("images/episode6/097.webp") with dissolve
    toby "Dia menyebutkan sesuatu, tetapi dia tidak mengatakan kapan."
    scene expression ("images/episode6/099.webp") with dissolve
    darlene "Jadi? Apa yang kamu katakan?"
    scene expression ("images/episode6/097.webp") with dissolve
    toby "Saya ingin sekali."
    scene expression ("images/episode6/098.webp") with dissolve
    darlene "Besar. Jika Anda memiliki plus, Anda juga bisa membawanya."
    if emma_break == False:
        scene expression ("images/episode6/097.webp") with dissolve
        toby "Nah, pacar saya baru saja kembali ke rumah pagi ini."
        scene expression ("images/episode6/099.webp") with dissolve
        darlene "Ah, benarkah? Menembak! Saya seharusnya mengundang Anda kemarin."
        scene expression ("images/episode6/100.webp") with dissolve
        darlene "Bagaimanapun, Anda bisa pulang sekarang dan bersiap -siap. Saya akan mengirimi Anda alamatnya."
    else:
        scene expression ("images/episode6/097.webp") with dissolve
        toby "Aku akan datang sendiri."
        scene expression ("images/episode6/100.webp") with dissolve
        darlene "Nah dalam hal ini, mengapa Anda tidak pulang dan bersiap -siap? Saya akan mengirimi Anda alamatnya."

    scene expression ("images/episode6/101.webp") with dissolve
    toby "Saya hanya ingin menyelesaikan ini dan kemudian saya akan pergi."
    darlene "Sempurna. Saya tahu Anda adalah orang yang tepat untuk pekerjaan itu."
    scene expression ("images/episode6/102.webp") with dissolve
    darlene "Aku akan meninggalkanmu."

    return


label episode6_club:
    $ progress = 87

    scene expression ("images/episode6/103.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode6/104.webp") with dissolve
    katrina "Bagus [toby!c]. Anda di sini!"
    scene expression ("images/episode6/105.webp") with dissolve
    katrina "Jadi, apakah kamu datang malam ini?"
    scene expression ("images/episode6/106.webp") with dissolve
    toby "Datang dimana?"
    scene expression ("images/episode6/105.webp") with dissolve
    katrina "Apakah Darlene tidak memberitahumu?"
    scene expression ("images/episode6/106.webp") with dissolve
    toby "Maaf ma \ 'am, tapi saya tidak tahu apa yang Anda bicarakan."
    scene expression ("images/episode6/107.webp") with dissolve
    katrina "Apakah kalian berdua tidak bertemu di gym dan dia mengundang Anda untuk makan malam?"
    scene expression ("images/episode6/106.webp") with dissolve
    toby "Dia memang menyebutkan sesuatu, tetapi dia tidak mengatakan kapan."
    scene expression ("images/episode6/107.webp") with dissolve
    katrina "Saya akan mengirimkan alamatnya. Pulanglah, mandi dan kenakan sesuatu yang lebih nyaman."
    scene expression ("images/episode6/108.webp") with dissolve
    toby "Umm ... tentu. Sampai jumpa lagi?"
    scene expression ("images/episode6/109.webp") with dissolve
    katrina "Dan, Anda dapat membawa plus jika Anda suka."
    scene expression ("images/episode6/108.webp") with dissolve
    if emma_break:
        toby "Saya akan datang sendiri malam ini, saya agak putus dengan pacar saya dan selain itu, dia tidak tinggal di kota."
    else:
        toby "Yah dia baru saja pergi pagi ini. Dia datang mengunjungi saya untuk hari itu, jadi saya akan sendirian."
    scene expression ("images/episode6/109.webp") with dissolve
    katrina "Bawa gadis lain kemudian."
    scene expression ("images/episode6/108.webp") with dissolve
    toby "Saya pikir lebih baik jika saya datang sendiri malam ini."
    scene expression ("images/episode6/109.webp") with dissolve
    katrina "Mau mu."
    katrina "Sampai jumpa nanti malam."
    scene expression ("images/episode6/110.webp") with dissolve
    toby "Nanti!"

    return

label episode6_dinnerPreparations:
    $ progress = 88
    scene expression ("images/episode6/111.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It's nice of them to invite me over for dinner.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm curious what their house looks like.{/i}"
    scene expression ("images/episode6/112.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm guessing there are a lot of nice fancy things that Darlene bought right alongside handcuffs, metal things, whips and who knows what other nasty stuff Katrina uses for decorations.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe even dildos.{/i}"

    stop music fadeout 1.0
    play sound "audio/fx/Knocking-on-door-five-knocks-www.fesliyanstudios.com.mp3"
    scene expression ("images/episode6/113.webp") with dissolve
    patricia "[toby!c], bisakah saya masuk? Saya harus bersiap -siap untuk malam ini."
    scene expression ("images/episode6/114.webp") with dissolve
    toby "Saya akan keluar dalam 10 menit!"
    scene expression ("images/episode6/113.webp") with dissolve
    patricia "Terlalu lama. Saya harus pergi saat itu."
    scene expression ("images/episode6/114.webp") with dissolve
    toby "Kemana kamu pergi?"
    scene expression ("images/episode6/113.webp") with dissolve
    patricia "Saya akan menjelaskan begitu saya di dalam, berbalik atau menutupi diri Anda sendiri!"
    scene expression ("images/episode6/115.webp") with dissolve
    toby "Jangan masuk!"

    scene expression ("images/episode6/116.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    patricia "Saya benar -benar terburu -buru."

    scene expression ("images/episode6/117.webp") with dissolve
    toby "Di mana Anda akan berpakaian seperti itu?"
    scene expression ("images/episode6/118.webp") with dissolve
    patricia "Anda tidak menyukainya?"
    scene expression ("images/episode6/117.webp") with dissolve
    toby "Tidak, Anda terlihat hebat, tapi apa kesempatan itu?"
    scene expression ("images/episode6/119.webp") with dissolve
    patricia "Cobalah menebak ..."
    scene expression ("images/episode6/120.webp") with dissolve
    toby "Anda sedang berkencan."
    scene expression ("images/episode6/119.webp") with dissolve
    patricia "Ya, saya berharap."
    scene expression ("images/episode6/120.webp") with dissolve
    toby "Clubbing?"
    scene expression ("images/episode6/119.webp") with dissolve
    patricia "Klub apa yang buka hari ini? Dan selain itu, saya menari seperti bebek!"
    scene expression ("images/episode6/121.webp") with dissolve
    toby "Menarik. Saya akan memberi Anda 10 dolar jika Anda menunjukkan gerakan Anda."
    scene expression ("images/episode6/122.webp") with dissolve
    patricia "Tidak ... terus bermimpi."
    scene expression ("images/episode6/121.webp") with dissolve
    toby "Ayo. Aku akan memberimu 0 jika kamu menari untukku."
    scene expression ("images/episode6/122.webp") with dissolve
    patricia "Anda menyadari bagaimana kedengarannya, bukan?"
    scene expression ("images/episode6/121.webp") with dissolve
    toby "Bisa aja. Anda yang memiliki pikiran yang kotor."
    scene expression ("images/episode6/123.webp") with dissolve
    patricia "Yeah, right. Sorry my bad, because \"I'll give you $50 to dance for me\" doesn't sound strange at all, right?"
    scene expression ("images/episode6/121.webp") with dissolve
    toby "Tepat. Seperti yang saya katakan, Anda memiliki pikiran kotor."
    scene expression ("images/episode6/123.webp") with dissolve
    patricia "Buatlah 00 dan saya akan memikirkannya."
    scene expression ("images/episode6/120.webp") with dissolve
    toby "00!? Itu adalah biaya tarian pribadi dengan akhir yang bahagia."
    scene expression ("images/episode6/123.webp") with dissolve
    patricia "Ya ... dan saya satu -satunya perv di sini."
    scene expression ("images/episode6/121.webp") with dissolve
    toby "Yup ... Maksudku, kamu meledak saat aku di sini telanjang."
    scene expression ("images/episode6/124.webp") with dissolve
    patricia "Tidak ada yang belum pernah saya lihat."
    scene expression ("images/episode6/121.webp") with dissolve
    toby "Tepatnya, jadi itu hanya adil bahwa untuk 00 Anda menyamakan kedudukan."
    scene expression ("images/episode6/124.webp") with dissolve
    patricia "Bagaimana tepatnya kita mencapai titik ini dalam percakapan?"
    scene expression ("images/episode6/120.webp") with dissolve
    toby "Nah, Anda sedang berkencan dan karena Anda tidak ingin saya mengganggu Anda dengan pertanyaan, Anda mengubah topik pembicaraan menjadi sesuatu yang kotor, karena Anda tahu ini adalah bagaimana saya kehilangan fokus pada hal -hal penting."
    scene expression ("images/episode6/124.webp") with dissolve
    patricia "Yup ... Aku adalah penjahat dalam cerita ini!"
    scene expression ("images/episode6/125.webp") with dissolve
    toby "Tentu saja Anda. Anda mencoba merobek saya."
    scene expression ("images/episode6/124.webp") with dissolve
    patricia "Baik, Anda memberi saya 0 dan saya akan memberi Anda senyum lebar."
    scene expression ("images/episode6/125.webp") with dissolve
    toby "Ummm... What happened to \"dance for me\"?"
    scene expression ("images/episode6/126.webp") with dissolve
    patricia "Nah, Anda menjadi serakah dan sekarang penawaran itu keluar dari meja."
    scene expression ("images/episode6/121.webp") with dissolve
    toby "Aku yang serakah? Anda bertanya kepada saya 0 hanya untuk melihat Anda tersenyum?"
    scene expression ("images/episode6/124.webp") with dissolve
    patricia "Anda harus jujur. Saya memiliki senyuman yang bagus. Jika aku jadi kamu, aku akan mengambil kesepakatan itu."
    scene expression ("images/episode6/120.webp") with dissolve
    toby "Oke, Anda masih menghindari pertanyaan. Jadi? Kemana kamu pergi?"
    scene expression ("images/episode6/123.webp") with dissolve
    patricia "Bea mendapat dua tiket ke balet sebagai hadiah dari orang tuanya. Dan mengingat fakta bahwa Joe membenci balet dan juga brengsek, dia memberi saya tiket lainnya."
    scene expression ("images/episode6/127.webp") with dissolve
    toby "Sekarang saya memiliki lebih banyak pertanyaan daripada sebelumnya."
    toby "Siapa Joe?"
    toby "Kenapa dia brengsek?"
    toby "Dan kapan Anda menjadi prima balerina?"
    scene expression ("images/episode6/128.webp") with dissolve
    patricia "Apakah Anda sedikit terlalu penasaran dengan Bea?"
    scene expression ("images/episode6/127.webp") with dissolve
    toby "Anda adalah orang yang menjatuhkan bom tentang dia menjadi brengsek. Anda tidak bisa menyalahkan saya karena ingin tahu."
    scene expression ("images/episode6/128.webp") with dissolve
    if beatrice_path:
        patricia "Tapi kamu menyukainya, kan?"
        scene expression ("images/episode6/127.webp") with dissolve
        toby "Jadi? Kenapa dia brengsek?"
    else:
        pass

    scene expression ("images/episode6/128.webp") with dissolve
    patricia "Jika saya memberi tahu Anda maka saya harus membunuh Anda."
    scene expression ("images/episode6/127.webp") with dissolve
    toby "Bagus. Jangan beri tahu saya."
    scene expression ("images/episode6/129.webp") with dissolve
    patricia "Oke kamu menang!"
    patricia "Joe adalah seorang pria di kelas lain. Selama tiga minggu terakhir dia telah mengirim sms padanya hampir setiap hari, tetapi dia masih belum mengajaknya kencan."
    patricia "Dan dia tidak pernah berbicara dengan tatap muka. Dia hanya mengirim sms padanya."
    scene expression ("images/episode6/130.webp") with dissolve
    toby "Pertama -tama, Anda buruk dalam menjaga rahasia. Ingatkan saya untuk tidak mempercayai Anda dengan apa pun."
    scene expression ("images/episode6/127.webp") with dissolve
    toby "Kedua, saya tidak melihat ada yang salah dengan dia pemalu."
    scene expression ("images/episode6/128.webp") with dissolve
    patricia "Dia tidak malu. Dia hanya malu berbicara dengannya. Maksud saya itu hanya tebakan, tapi ya."
    patricia "Karena dia bukan salah satu dari anak -anak yang keren."
    scene expression ("images/episode6/131.webp") with dissolve
    toby "Terlalu banyak drama untukku."
    toby "Jadi? Apa yang Anda ketahui tentang balet?"
    scene expression ("images/episode6/132.webp") with dissolve
    patricia "Tidak ada, tapi saya akan belajar."
    scene expression ("images/episode6/133.webp") with dissolve
    toby "Semoga berhasil dengan itu."
    scene expression ("images/episode6/134.webp") with dissolve
    patricia "Jadi? Bagaimana menurutmu?"
    scene expression ("images/episode6/135.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    toby "Wow [sis] ... Anda terlihat ... cantik!"
    scene expression ("images/episode6/136.webp") with dissolve
    patricia "Terima kasih."
    patricia "Ngomong -ngomong ... menurutmu aku terlalu banyak menunjukkan kulit?"
    scene expression ("images/episode6/133.webp") with dissolve
    toby "Tidak terlalu. Gaun itu terlihat bagus. Satu -satunya hal adalah mencoba untuk tidak membungkuk atau sesuatu karena gaun itu mungkin tergelincir."
    scene expression ("images/episode6/137.webp") with dissolve
    patricia "Lihat!Tolong ... ini bukan pakaian murah. Itu tidak akan slip. Bahkan tidak jika saya membungkuk."
    scene expression ("images/episode6/138.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode6/139.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode6/140.webp") with dissolve
    patricia "Kotoran!"
    toby "Sekarang Anda menunjukkan sedikit terlalu banyak kulit, tetapi selain itu baik -baik saja."
    scene expression ("images/episode6/137.webp") with dissolve
    patricia "Saya kira saya tidak akan membungkuk saat itu."
    scene expression ("images/episode6/141.webp") with dissolve
    patricia "Setidaknya tidak saat ada Perv di sekitar."
    scene expression ("images/episode6/142.webp") with dissolve
    toby "Oh sial!"
    scene expression ("images/episode6/143.webp") with dissolve
    toby "Ya, lebih baik tidak membungkuk."
    scene expression ("images/episode6/144.webp") with dissolve
    patricia "Ngomong -ngomong, apakah menurutmu kamu bisa tidur di sofa malam ini? Saya ingin mengundang Bea."
    toby "Tapi sofa sangat tidak nyaman."
    scene expression ("images/episode6/145_1.webp") with dissolve
    patricia "Cantik!"
    patricia "Anda tahu saya tidak pandai berteman. Saya akhirnya membuatnya dan akan menyenangkan memiliki malam perempuan!"
    scene expression ("images/episode6/145_2.webp") with dissolve
    toby "Bisakah Anda menunggu sampai saya selesai merenovasi loteng?"
    scene expression ("images/episode6/146_1.webp") with dissolve
    patricia "Tidak!"
    patricia "Terima kasih untuk ini. Anda yang terbaik!"
    scene expression ("images/episode6/146_2.webp") with dissolve
    toby "Saya tidak pernah mengatakan saya akan melakukannya."
    scene expression ("images/episode6/147.webp") with dissolve
    patricia "Saya tahu Anda lebih baik dari yang Anda kenal sendiri. Saya tahu Anda akan mengatakan ya!"
    toby "Tapi saya tidak pernah mengatakannya!"
    patricia "Saya akan mencium Anda untuk menunjukkan penghargaan saya, tetapi mengingat fakta bahwa teman kecil Anda bangun setelah melihat sedikit kulit, saya tidak bisa membayangkan apa yang akan terjadi jika saya memberi Anda ciuman!"
    scene expression ("images/episode6/148.webp") with dissolve
    toby "Tidak ada yang akan terjadi."
    patricia "Masih bisa mengambil risiko!"
    scene expression ("images/episode6/149.webp") with dissolve
    patricia "Sampai jumpa!"
    toby "Bye Bitch!"
    patricia "Mencintaimu juga!"
    scene expression ("images/episode6/150.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What am I going to do with you? Really? You woke up when you saw Tris? She's our [sister], dude.{/i}"
    menu:
        "{i} [JGR] Jerk Off {/i}"(csq="Acara Malam dengan Tris & Galeri Gambar & Penting untuk Tris \ 'Path"):
            $ ep6_caughtJerking = True
            scene expression ("images/episode6/151.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I can't believe how hot Tris is.{/i}"
            scene expression ("images/episode6/152.webp") with dissolve
            $ unlockImage(persistent.patricia_12)
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}That's it [sis]. You have gorgeous tits. Flash them one more time.{/i}"
            scene expression ("images/episode6/151.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wanna cum on your beautiful tits.{/i}"
            scene expression ("images/episode6/153.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode6/154.webp") with dissolve
            patricia "Omong-omong! Maaf untuk..."
            scene expression ("images/episode6/155.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode6/156.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck!!!{/i}"
            scene expression ("images/episode6/157.webp") with dissolve
            patricia "Maaf! Saya baru saja pergi."
            scene expression ("images/episode6/158.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Well, that was awkward.{/i}"
            pass
        "{i} Ini akan hilang. Saya seharusnya tidak terlambat makan malam. {/i}":


            pass

    return


label episode6_dinner:
    $ progress = 89
    stop music fadeout 1.0
    scene expression ("images/episode6/159.webp") with fade
    play sound "audio/fx/Knocking-on-door-five-knocks-www.fesliyanstudios.com.mp3"
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode6/160.webp") with dissolve

    darlene "Oh, [toby!c] ... Selamat datang. Silakan masuk!"
    scene expression ("images/episode6/161.webp") with dissolve
    toby "Ini untukmu. Saya harap Anda menyukai mereka."
    scene expression ("images/episode6/162.webp") with dissolve
    darlene "Mereka luar biasa. Anda benar -benar tidak boleh memilikinya."
    darlene "Biarkan saya memasukkannya ke dalam air. Jadikan diri Anda nyaman. Katrina harus keluar sebentar lagi. Dia mandi."
    scene expression ("images/episode6/163.webp") with dissolve
    toby "Anda memiliki apartemen yang sangat bagus!"
    scene expression ("images/episode6/164.webp") with dissolve
    darlene "Anda sangat manis. Ini adalah apartemen pertama yang saya jual sebagai agen real estat baru."
    darlene "Empat tahun yang lalu saya menemukan itu di belakang pasar dan memutuskan bahwa saya harus memilikinya sendiri. Saya merasa cukup terikat pada apartemen ini."
    scene expression ("images/episode6/165.webp") with dissolve
    toby "Oh, jadi itu lebih merupakan hal yang sentimental?"
    scene expression ("images/episode6/166.webp") with dissolve
    darlene "Ya. Sesuatu seperti itu. Saya berusia 22 tahun saat itu dan 4 tahun kemudian saya memutuskan untuk memulai bisnis saya sendiri."
    toby "Anda mulai muda."
    if toby_job == 0:
        darlene "Begitu juga Anda. Ketika saya melihat Anda, saya melihat diri saya sendiri."
    else:
        darlene "Ya, saya lakukan, tetapi kadang -kadang saya berharap saya lebih banyak berpesta pada usia itu. Saya sangat fokus pada pekerjaan dan barang -barang dan kehilangan banyak hal untuk bersenang -senang."

    scene expression ("images/episode6/167.webp") with dissolve
    katrina "Beri tahu saya kapan [toby!c] tiba di sini."
    scene expression ("images/episode6/168.webp") with dissolve
    toby "Selamat malam!"
    katrina "Oh ... kamu sudah di sini."
    scene expression ("images/episode6/169.webp") with dissolve
    katrina "Aku akan berpakaian. Kembali!"
    scene expression ("images/episode6/170.webp") with dissolve
    darlene "Saya minta maaf untuk itu. Dia tidak punya masalah dengan ketelanjangan!"
    toby "Jangan khawatir."
    if darlene_path:
        scene expression ("images/episode6/171.webp") with dissolve
        darlene "Saya bertaruh. Anda suka melihat pacar saya, [toby!c]? Aku tidak cukup untukmu?"
        toby "Apakah ini benar -benar yang ingin Anda bicarakan saat pacar Anda ada di ruangan lain?"
        darlene "Ya, Anda mungkin benar!"
    else:
        pass

    scene expression ("images/episode6/170.webp") with dissolve
    if emma_break:
        if toby_job == 0:
            darlene "Ngomong -ngomong ... berbicara tentang pacar, apa yang terjadi dengan milikmu?"
        else:
            darlene "Ngomong -ngomong ... berbicara tentang pacar, Kat memberitahuku bahwa kamu putus dengan milikmu."

        toby "Ya, ya. Hubungan jarak jauh sedikit lebih sulit dari yang saya harapkan."
        darlene "Ya dan selain itu, Anda masih muda. Ini adalah waktu ketika Anda harus bersenang -senang, tidak diikat ke hubungan jarak jauh."
    else:

        if toby_job == 0:
            darlene "Pokoknya ... berbicara tentang pacar. Anda menyebutkan sesuatu tentang dia berada di kota."
        else:
            darlene "Pokoknya ... berbicara tentang pacar. Kat memberitahuku pacarmu di kota kemarin."

        toby "Ya. Dia merindukanku dan memutuskan untuk mengambil cuti dari sekolah untuk datang berkunjung."
        darlene "Kaum muda."

    scene expression ("images/episode6/172.webp") with dissolve

    katrina "Tinggalkan anak laki -laki itu sendirian, kau hag tua. Anda seperti wanita tua usil yang perlu tahu segalanya."
    scene expression ("images/episode6/173.webp") with dissolve
    darlene "Anda akan berbicara! Anda mencoba bertindak keren sekarang, tetapi itu adalah ide Anda untuk mengundangnya sehingga Anda dapat bersenang -senang dengannya."
    scene expression ("images/episode6/172.webp") with dissolve
    katrina "Ngomong -ngomong, [toby!c]. Dengan \ 'Fun' dia bermaksud berbicara tentang kehidupan cinta Anda dan menggoda Anda, tidak bersenang -senang seperti apa yang Anda dan saya pikirkan tentang kesenangan!"
    if katrina_path or darlene_path:
        scene expression ("images/episode6/174.webp") with dissolve
        toby "Menembak! Itu memalukan."
    else:
        scene expression ("images/episode6/175.webp") with dissolve
        toby "Sebenarnya saya tidak memikirkan apa pun."
        scene expression ("images/episode6/172.webp") with dissolve
        katrina "Saya mengerti mengapa dia menyukai Anda."

    scene expression ("images/episode6/176.webp") with dissolve
    darlene "Ayo, biarkan makan. Lagi pula, itulah mengapa kami mengundang Anda."
    scene expression ("images/episode6/177.webp") with dissolve
    katrina "Asal tahu saja, Darlene adalah juru masak rumah. Jika saya memasak makanan Anda, Anda akan mengambil hidup Anda ke tangan Anda sendiri."
    scene expression ("images/episode6/178.webp") with dissolve
    toby "Anda tidak bisa seburuk itu."
    scene expression ("images/episode6/179.webp") with dissolve
    darlene "Percayalah kepadaku. Memasak bukanlah salah satu bakatnya."
    scene expression ("images/episode6/180.webp") with dissolve
    darlene "OKE! Gali!"
    toby "Bon Appétit!"
    katrina "..."
    scene expression ("images/episode6/181_happy_2.webp") with long_dissolve
    $ progress = 90
    toby "Terima kasih untuk makan malam. Itu bagus."
    scene expression ("images/episode6/182_smile_1.webp") with dissolve
    katrina "Ya, dia adalah juru masak terbaik."
    scene expression ("images/episode6/182_smile_2.webp") with dissolve
    katrina "Sebenarnya sekarang saya mengatakan itu, saya pikir Anda yang terbaik di hampir semua hal yang Anda lakukan!"
    scene expression ("images/episode6/183_laugh_3.webp") with dissolve
    darlene "Terkadang dia bisa sangat manis. Saat -saat itu sangat jarang, tetapi itu bisa terjadi."
    scene expression ("images/episode6/182_smile_2.webp") with dissolve
    katrina "Dengan begitu Anda menghargainya ketika saya mengatakan hal -hal manis tentang Anda."
    scene expression ("images/episode6/181_laugh_3.webp") with dissolve
    toby "Momen -momen ini seperti gerhana matahari. Jarang, tapi luar biasa saat itu terjadi."
    scene expression ("images/episode6/182_laugh_1.webp") with dissolve
    katrina "Tepat. Aku tahu kamu mengerti."
    scene expression ("images/episode6/182_laugh_2.webp") with dissolve
    if toby_job == 0:
        katrina "Anda benar untuk menyukainya. Dia pintar, yang ini."
    else:
        katrina "Melihat? Sudah kubilang dia bukan hanya wajah yang cantik."
    scene expression ("images/episode6/183_normal_1.webp") with dissolve
    darlene "Asal tahu saja, dia dulu benar -benar peduli dan manis. Akhir -akhir ini dia menyebalkan, tapi kembali ketika kami bertemu dia benar -benar baik."
    scene expression ("images/episode6/181_curious_2.webp") with dissolve
    toby "Saya harap Anda tidak keberatan dengan permintaan saya, tetapi bagaimana kalian berdua bertemu?"
    scene expression ("images/episode6/182_arogant_1.webp") with dissolve
    katrina "Let's just say I was her \"savior\"."
    scene expression ("images/episode6/181_curious_3.webp") with dissolve
    toby "Sekarang Anda membuat saya penasaran."
    scene expression ("images/episode6/183_laugh_1.webp") with dissolve
    darlene "Dia suka membual."
    scene expression ("images/episode6/183_normal_1.webp") with dissolve
    darlene "Berapa banyak waktu yang Anda miliki?"
    scene expression ("images/episode6/182_laugh_2.webp") with dissolve
    katrina "Jangan bosan dengan pria malang itu dengan cerita panjang Anda."
    scene expression ("images/episode6/181_happy_3.webp") with dissolve
    toby "Tidak, sungguh. Sekarang saya perlu tahu."
    scene expression ("images/episode6/183_smile_3.webp") with dissolve
    darlene "Melihat? Seseorang ingin mendengarkan kisah romantis saya."
    scene expression ("images/episode6/183_smile_1.webp") with dissolve
    darlene "Jadi seperti yang saya katakan, 15 tahun yang lalu saya memulai perusahaan saya. Awalnya kecil, tapi kemudian segalanya benar -benar mulai mengambil."
    darlene "Kami berhasil membeli banyak properti dan semuanya berjalan sangat hebat."
    scene expression ("images/episode6/183_normal_1.webp") with dissolve
    darlene "Namun, meskipun bisnisnya berjalan dengan baik, saya masih muda dan naif, dan saya jatuh cinta dengan seorang pria yang juga bekerja untuk saya."
    darlene "Tidak lama setelah bisnis saya mulai benar -benar lepas landas, kami menikah."
    darlene "Tapi cinta memudar dan enam tahun kemudian kami akhirnya bercerai."
    scene expression ("images/episode6/182_normal_1.webp") with dissolve
    katrina "Saya terus mengatakan kepadanya bahwa dia hanya mengejar uangnya."
    scene expression ("images/episode6/183_sad_1.webp") with dissolve
    darlene "Mungkin dia benar. Masalahnya adalah ketika hal -hal akhirnya mulai berjalan dengan baik, krisis ekonomi melanda. Kami tidak hanya kehilangan banyak properti, yang saya tinggalkan saya harus berpisah antara saya dan mantan suami saya."
    scene expression ("images/episode6/181_normal_2.webp") with dissolve
    toby "Menyesal mendengarnya."
    scene expression ("images/episode6/183_normal_1.webp") with dissolve
    darlene "Itu adalah waktu yang mengerikan. Tapi titik terang dari cerita ini ada di sini tempat saya bertemu Kat."
    darlene "Saya ditinggalkan dengan klub dan hanya 10 apartemen."
    scene expression ("images/episode6/182_laugh_1.webp") with dissolve
    katrina "Di situlah saya masuk. Saya adalah penyelamatnya."
    katrina "Dia bertanya apakah saya bisa membayar sewa 6 bulan ke depan."
    scene expression ("images/episode6/182_smile_1.webp") with dissolve
    katrina "Saya bukan wanita bisnis yang cerdas dengan cara apa pun, tetapi saya tahu seperti apa aroma pemerasan."
    scene expression ("images/episode6/183_laugh_3.webp") with dissolve
    darlene "Pemerasan pantat saya. Saya bahkan akan menurunkan sewa bulanan."
    scene expression ("images/episode6/182_smile_1.webp") with dissolve
    katrina "Apa pun. Saya tidak menerima. Saya punya uang, tetapi saya tidak akan menjadi semacam amal."
    scene expression ("images/episode6/182_arogant_1.webp") with dissolve
    katrina "Jadi saya bertanya apakah dia memiliki apartemen yang tersedia untuk disewa."
    katrina "Dan untungnya baginya dia melakukannya. Ternyata semuanya. Jadi saya menyewa semua 10 untuk gadis -gadis saya dan saya menyelamatkan pantat kecilnya yang lucu."
    scene expression ("images/episode6/183_laugh_1.webp") with dissolve
    darlene "Disimpan adalah kata yang kuat."
    scene expression ("images/episode6/181_curious_3.webp") with dissolve
    toby "You mentioned something about \"your girls\". Saya tidak tahu Anda punya anak."
    scene expression ("images/episode6/182_laugh_1.webp") with dissolve
    katrina "Tidak, saya tidak. Saya mengatakan karyawan. Anda harus memiliki misheard dan selain itu saya tidak pernah memiliki anak dan tidak memiliki keinginan untuk apa pun."
    scene expression ("images/episode6/181_normal_3.webp") with dissolve
    toby "Ya ... mungkin saya salah lagi."
    scene expression ("images/episode6/183_awkward_1.webp") with dissolve
    darlene "Ngomong -ngomong, dia menyewa semua apartemen yang saya miliki untuk karyawannya dan secara mengejutkan dia cukup tepat dengan sewa."
    scene expression ("images/episode6/181_thinking.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm sure she said girls. I wonder why are they trying to change the subject.{/i}"
    scene expression ("images/episode6/182_arogant_1.webp") with dissolve
    katrina "Kami sudah bersama selama 7 tahun dan saya masih harus membayar sewa."
    scene expression ("images/episode6/183_normal_1.webp") with dissolve
    darlene "Bisnis adalah bisnis dan seks adalah seks."
    scene expression ("images/episode6/181_curious_2.webp") with dissolve
    toby "Dan kapan Anda menyadari bahwa Anda gay?"
    scene expression ("images/episode6/183_laugh_1.webp") with dissolve
    darlene "Mari kita katakan saja saya memiliki bagian saya dari pria dan memutuskan saya lebih menyukai wanita."
    scene expression ("images/episode6/183_normal_1.webp") with dissolve
    darlene "Itu aneh bagi kami berdua. Tak satu pun dari kami yang tahu kami menyukai wanita. Kami mulai nongkrong dan ya."
    scene expression ("images/episode6/181_smile_2.webp") with dissolve
    toby "Itu bagus."
    scene expression ("images/episode6/182_normal_1.webp") with dissolve
    katrina "Tidak juga, karena pertama -tama kita harus melalui bagian kita yang adil dari pria bodoh."
    scene expression ("images/episode6/181_laugh_3.webp") with dissolve
    toby "Aku sakit."
    scene expression ("images/episode6/182_smile_1.webp") with dissolve
    katrina "Cukup aman untuk mengatakan bahwa Anda tidak menyerang kami berdua sebagai brengsek."
    scene expression ("images/episode6/181_curious_3.webp") with dissolve
    toby "Anda juga mengalami perceraian yang buruk?"
    scene expression ("images/episode6/182_laugh_1.webp") with dissolve
    katrina "Neraka tidak. Saya menyelamatkan keluar dari rumah asuh saat saya berusia 18 tahun. Untuk bertahan hidup, saya harus melakukan banyak hal yang saya sesali."
    katrina "Saya melakukan semua hal buruk yang bisa Anda harapkan harus dilakukan seorang anak untuk bertahan, tetapi hal terburuk adalah seks untuk uang."
    scene expression ("images/episode6/183_thinking.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Darlene seems a little bit uncomfortable. Maybe I touched a nerve.{/i}"
    scene expression ("images/episode6/182_normal_1.webp") with dissolve
    katrina "Itu ketika saya memutuskan saya suka wanita."
    scene expression ("images/episode6/183_awkward_3.webp") with dissolve
    darlene "Ya ... Lagi pula."
    scene expression ("images/episode6/182_laugh_2.webp") with dissolve
    katrina "Oh, berhenti. Saya tahu Anda tidak menyukai bagian itu tentang masa lalu saya dan ingin merahasiakannya, tetapi itu tidak seperti [toby!c] akan berkeliling memberi tahu semua orang bahwa pacar Anda biasa bercinta dengan uang."
    scene expression ("images/episode6/182_arogant_1.webp") with dissolve
    katrina "Benar, [toby!c]?"
    scene expression ("images/episode6/181_awkward_3.webp") with dissolve
    toby "Uhh ... ya, tentu saja tidak!"
    scene expression ("images/episode6/181_thinking.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think it's time for me to go, before they get in a fight.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But Katrina seems like an interesting woman with interesting past.{/i}"
    scene expression ("images/episode6/184.webp") with dissolve
    toby "Terima kasih banyak atas undangan dan makan malam wanita, tapi saya takut sudah saatnya saya kembali ke rumah. Ini terlambat."
    scene expression ("images/episode6/185.webp") with dissolve
    darlene "Saya senang Anda menerima dan Anda selalu dipersilakan untuk datang lagi."
    scene expression ("images/episode6/186.webp") with dissolve
    katrina "Lain kali, ini akan menjadi giliran Anda untuk menceritakan kisah Anda kepada kami."
    scene expression ("images/episode6/184.webp") with dissolve
    toby "Pasti."
    if toby_job == 0:
        scene expression ("images/episode6/187.webp") with dissolve
        darlene "Sebelum Anda pergi, saya hanya ingin memberi tahu Anda bahwa saya menyukai Anda dan saya akan mengajari Anda semua yang saya tahu."
        if darlene_path:
            toby "Di tingkat profesional?"
            scene expression ("images/episode6/188.webp") with dissolve
            darlene "Siapa tahu, mungkin tidak hanya pada tingkat profesional."
            $ unlockImage(persistent.darlene_05)
        scene expression ("images/episode6/187.webp") with dissolve
        darlene "Mari kita katakan Anda akan menjadi agen real estat terbaik di sekitar ketika saya selesai dengan Anda!"
        toby "Saya menantikannya!"
    else:
        scene expression ("images/episode6/189.webp") with dissolve
        katrina "Aku menyukaimu [toby!c]. Saya akan menjadikan Anda orang yang sangat kuat."
        toby "Saya sangat menyukainya."
        if katrina_path:
            scene expression ("images/episode6/190.webp") with dissolve
            katrina "Dan mungkin saya akan mengajari Anda cara mengendalikan wanita yang kuat juga."
            toby "Saya pikir saya sudah cukup baik dalam hal itu."
            katrina "Saya akan mengajari Anda cara mengendalikan wanita yang kuat tanpa tertembak."
            toby "Saya tidak pernah membayangkan saya perlu belajar keterampilan itu. Saya melihat sekarang di mana itu bisa berguna."
            $ unlockImage(persistent.katrina_05)
        scene expression ("images/episode6/189.webp") with dissolve
        katrina "Jadi, sampai jumpa besok di klub?"
        toby "Anda bertaruh!"

    scene expression ("images/episode6/191.webp") with dissolve
    toby "Terima kasih untuk malam ini. Itu sangat bagus dan sekali lagi terima kasih atas undangannya."

    return


label episode6_backHome:
    $ progress = 91

    scene expression ("images/episode6/192.webp") with dissolve
    if toby_job == 0:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Dinner was nice actually. It was interesting to see how Darlene is at home when she's not at work.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And Katrina... Well, she's so different than what I imagined, but I'm really curious about her teenage years.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It was so strange to see Katrina so relaxed and all. I think her relationship with Darlene is doing her good.{/i}"
    scene expression ("images/episode6/193.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Anyway, I'm ready to get some sleep. I'm so tired.{/i}"
    scene expression ("images/episode6/194_2.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/194_1.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit, I forgot Bea was coming over. Now I need to find an excuse so I don't blow Tris' cover. She would hate it if Bea found out she still shares a bed with her [brother].{/i}"
    patricia "Anda lupa mengetuk!"
    beatrice "Hai [toby!c]."
    scene expression ("images/episode6/195.webp") with dissolve
    toby "Sangat menyesal nona. Saya pikir Anda masih di balet dan sepertinya saya tidak bisa menemukan ..."
    toby "... Kunci saya untuk sepeda saya dan saya pikir Anda mencuri mereka lagi."
    scene expression ("images/episode6/196.webp") with dissolve
    patricia "Terkadang saya mencuri kuncinya. Saya sangat suka melakukannya setiap kali dia terburu -buru sehingga dia harus mencari mereka."
    scene expression ("images/episode6/197.webp") with dissolve
    beatrice "Anda sangat buruk ..."
    scene expression ("images/episode6/199.webp") with dissolve
    toby "Itu hanya alasannya. Sebenarnya, dia takut aku akan terluka atau sesuatu sehingga dia menyembunyikan kunci saya berharap saya akan naik bus."
    toby "Dia terlalu peduli tentang saya, tetapi dia benci mengakuinya."
    scene expression ("images/episode6/197.webp") with dissolve
    beatrice "Aww ... sangat manis."
    scene expression ("images/episode6/198.webp") with dissolve
    patricia "Anda berharap."
    scene expression ("images/episode6/197.webp") with dissolve
    beatrice "Saya suka hubungan Anda. Saya berharap saya bisa rukun juga dengan [brother] saya juga."
    scene expression ("images/episode6/196.webp") with dissolve
    patricia "Nah ... kami hanya menampilkan pertunjukan untuk Anda. Kami tidak benar -benar bergaul dengan baik."
    scene expression ("images/episode6/199.webp") with dissolve
    toby "Ya ... terutama saat dia mencuri kunci saya. Jadi? Apakah Anda tahu di mana mereka berada?"
    scene expression ("images/episode6/198.webp") with dissolve
    patricia "Aku tidak tahu. Saya hanya tahu bahwa mereka tidak ada di ruangan ini."
    scene expression ("images/episode6/199.webp") with dissolve
    toby "Aku membencimu. Anda tahu itu benar?"
    scene expression ("images/episode6/198.webp") with dissolve
    patricia "Mencintaimu juga."
    scene expression ("images/episode6/199.webp") with dissolve
    toby "Saya tahu Anda melakukannya."
    scene expression ("images/episode6/200.webp") with dissolve
    toby "Ngomong -ngomong, selamat malam, perempuan!"
    scene expression ("images/episode6/201.webp") with dissolve
    beatrice "Selamat malam, [toby!c]."
    patricia "Selamat malam dan semoga sukses dengan kunci Anda."

    scene expression ("images/episode6/202.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Really, [toby!c]? That's the best you could come up with? She steals your keys?{/i}"
    play sound "audio/fx/notification_5.mp3"
    scene expression ("images/episode6/203.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I've got a message from Tris.{/i}"
    scene expression ("images/episode6/204_texting.webp") with dissolve

    call sms_incoming ("tris", "Thanks for covering for me, but really?") from _call_sms_incoming_68
    call sms_incoming ("tris", "What am I?") from _call_sms_incoming_69
    call sms_incoming ("tris", "12?") from _call_sms_incoming_70
    call sms_sent ("tris", "It worked. Didn't it?") from _call_sms_sent_37
    call sms_incoming ("tris", "Yeah, actually it did, but you really need to work on your lies.") from _call_sms_incoming_71
    call sms_sent ("tris", "I'm sleeping on the couch and you're bitching about that?") from _call_sms_sent_48
    call sms_incoming ("tris", "By the way. I left your pajamas in [mom]'s bedroom.") from _call_sms_incoming_72
    call sms_sent ("tris", "Cheers!") from _call_sms_sent_49
    call sms_incoming ("tris", "Good night and sleep well on the couch!") from _call_sms_incoming_73
    call sms_sent ("tris", "Yeah, yeah. I know. I'm the best [brother] ever.") from _call_sms_sent_50
    call sms_incoming ("tris", "You wish!") from _call_sms_incoming_74
    hide screen message

    scene expression ("images/episode6/205.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}At least she left my shorts in [mom]'s bedroom.{/i}"

    return

label episode6_charlotte:
    $ progress = 92
    scene expression ("images/episode6/206.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}The hell is this? {/i}"
    scene expression ("images/episode6/207_texting.webp") with dissolve
    call sms_sent ("tris", "The hell are these?", img="images/episode6/208.webp", img_icon="images/episode6/208_icon.webp") from _call_sms_sent_51
    call sms_incoming ("tris", "Those are your pajamas, silly!") from _call_sms_incoming_75
    call sms_sent ("tris", "I sleep in shorts.") from _call_sms_sent_52
    call sms_incoming ("tris", "Those are not shorts. Those are more like underwear. You don't want Bea to see you in your underwear.") from _call_sms_incoming_76
    call sms_incoming ("tris", "And besides these are much nicer. You'll look just like [dad].") from _call_sms_incoming_77
    call sms_incoming ("tris", "I'm sure [mom] would appreciate it if you finally wore them. She bought them for you, remember?") from _call_sms_incoming_78
    call sms_sent ("tris", "She bought the same thing for [dad]. Whatever. You'll pay for this.") from _call_sms_sent_53
    call sms_incoming ("tris", "Oh, please. Grow up, already!") from _call_sms_incoming_79
    call sms_sent ("tris", "Just you wait!") from _call_sms_sent_54
    hide screen message

    scene expression ("images/episode6/209.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hell nah, I'm not going to wear that shirt. It's like a thousand degrees outside.{/i}"

    scene expression ("images/episode6/210.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Well, well, well. Look at that. [mom!c] left her laptop here. Maybe I could take a peek at her new book.{/i}"
    scene expression ("images/episode6/211.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see. Tris' birthday.{/i}"
    toby "{size=12}{color=#FDCA6E}* reading *{/color}{/size}\n{i}\"Wrong password!\"{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Her anniversary, maybe?{/i}"
    toby "{size=12}{color=#FDCA6E}* reading *{/color}{/size}\n{i}\"Wrong password!\"{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}My birthday?{/i}"
    toby "{size=12}{color=#FDCA6E}* reading *{/color}{/size}\n{i}\"Wrong password!\"{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm hurt [mom]. Maybe her birthday?{/i}"
    toby "{size=12}{color=#FDCA6E}* reading *{/color}{/size}\n{i}\"Wrong password!\"{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit. Let's try 'tris'.{/i}"
    toby "{size=12}{color=#FDCA6E}* reading *{/color}{/size}\n{i}\"Wrong password!\"{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmm... I'll give you more chance to show me you love me. Let's try '[toby!c]'.{/i}"
    scene expression ("images/episode6/212.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And we're in. [mom!c], I'm glad that my name is your password, but you really need to step up your game.{/i}"
    scene expression ("images/episode6/213.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see if I can find her story.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmm... I think this is the one.{/i}"
    toby "{size=12}{color=#FDCA6E}* reading *{/color}{/size}\n{i}\"My name is Ettola Rahc and I have a confession to make.\"{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What kind of name is this? Oh shit! It's almost her name read backwards. Ettola Rahc -> CharAlotte.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's keep reading.{/i}"
    scene expression ("images/episode6/214.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I can't take my eyes off of him. He's right there in front of me, but why am I staring at him? He's not my husband.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}He's just a waiter. Yes, he's good looking, but I'm a married woman.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I love my husband, I can't look at other guys.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But God, he's so gorgeous. What I would give to be 20 again.{/i}"
    scene expression ("images/episode6/215.webp") with dissolve
    erwin "Apakah semuanya baik -baik saja?"
    scene expression ("images/episode6/216.webp") with dissolve
    charlotte_ "Maaf sayang, saya sedang bermimpi."
    scene expression ("images/episode6/215.webp") with dissolve
    erwin "Hari yang panjang?"
    scene expression ("images/episode6/216.webp") with dissolve
    charlotte_ "Ya. Saya sangat sibuk dengan pekerjaan belakangan ini."
    scene expression ("images/episode6/215.webp") with dissolve
    erwin "Anda sekarang istri saya. Aku akan menjagamu.Saya masih tidak mengerti mengapa Anda bekerja. Saya katakan bahwa saya dapat memberikan semua yang Anda butuhkan. Anda tidak harus bekerja."
    scene expression ("images/episode6/217.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yup. This is my husband. We've been married for quite a while now, but we got so used to this that we forgot how to be romantic.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe that's why I'm looking over at that young man, hoping he'll notice me and give me a smile. I just want to feel wanted.{/i}"
    scene expression ("images/episode6/214.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I mean. Look at him.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Tall, lean figure with just enough muscle, dark hair, gorgeous dark brown eyes. And that smile. God, that smile.{/i}"
    $ unlockImage(persistent.charlotte_12)
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm getting so horny just looking at him. I'm such a bad housewife.{/i}"
    scene expression ("images/episode6/213.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmm... Maybe I'm wrong, but me and this waiter seem to have a lot in common.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Or maybe this was just her type back then. I mean, a lot of people say that I look a lot like [dad] when he was young.{/i}"
    scene expression ("images/episode6/218.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode6/219.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think I hear someone coming upstairs. I'd better put this back.{/i}"
    scene expression ("images/episode6/220.webp") with dissolve
    $ progress = 93
    charlotte "Oh, sayang. Anda sudah kembali?"
    scene expression ("images/episode6/221.webp") with dissolve
    toby "Ya. Saya baru saja datang untuk berpakaian. Tris meninggalkan piyama saya di sini."
    scene expression ("images/episode6/223.webp") with dissolve
    charlotte "Lihatlah Anda, makhluk cantik, atau makhluk yang indah?"
    scene expression ("images/episode6/222.webp") with dissolve
    toby "Just go with what you feel is right. Anything works as long as you add the \"creature\"setelah itu."
    scene expression ("images/episode6/224_smile.webp") with dissolve
    charlotte "Saya senang Anda akhirnya memutuskan untuk mengenakan piyama yang saya beli."
    scene expression ("images/episode6/225_laugh.webp") with dissolve
    toby "Terima kasih Tris. Dia alasan saya tidak memiliki celana pendek di sini."
    scene expression ("images/episode6/224_laugh.webp") with dissolve
    charlotte "Dia sangat manis, wanita muda itu."
    scene expression ("images/episode6/225_meh.webp") with dissolve
    toby "Ya ... Anda memberi tahu saya. Tebak siapa yang akan tidur di sofa malam ini."
    if ep4_nightWithCharlotte:
        scene expression ("images/episode6/224_flirty.webp") with dissolve
        charlotte "Saya dapat bergabung dengan Anda jika Anda mau."
        scene expression ("images/episode6/225_laugh.webp") with dissolve
        toby "Anda suka tidur di sofa dengan saya?"
        scene expression ("images/episode6/224_laugh.webp") with dissolve
        charlotte "Jangan bisa maju sendiri. Saya suka tidak mendengar dengkol [father] Anda."
        scene expression ("images/episode6/225_normal.webp") with dissolve
        toby "Dan di sini saya berpikir Anda senang menghabiskan waktu dengan saya."
        scene expression ("images/episode6/224_pouty.webp") with dissolve
        charlotte "Malang kamu. Tentu saja aku suka menghabiskan waktu bersamamu, sayang."
        scene expression ("images/episode6/224_curious.webp") with dissolve
        charlotte "Ngomong -ngomong, bagaimana makan malam di bosmu?"
    else:
        scene expression ("images/episode6/224_smile.webp") with dissolve
        charlotte "Setidaknya Anda akan tidur dengan perut penuh dengan makanan enak."
        scene expression ("images/episode6/224_curious.webp") with dissolve
        charlotte "Sebenarnya apakah kamu? Bagaimana makan malam di bos Anda \ '?"
    scene expression ("images/episode6/225_smile.webp") with dissolve
    toby "Itu sebenarnya bagus. Makanannya sangat enak dan selain itu, bos saya dan pacarnya sangat enak."
    scene expression ("images/episode6/224_smile.webp") with dissolve
    charlotte "Saya senang mendengarnya. Setidaknya salah satu dari kami memiliki malam yang baik."
    scene expression ("images/episode6/225_curious.webp") with dissolve
    toby "Apa maksudmu? Apakah sesuatu terjadi?"
    scene expression ("images/episode6/225_normal.webp") with dissolve
    toby "Tolong beritahu saya [dad] tidak melakukan sesuatu yang bodoh lagi."
    scene expression ("images/episode6/224_laugh.webp") with dissolve
    charlotte "Tidak, sayang. Jangan khawatir tentang dia. Ini tidak ada hubungannya dengan [father] Anda."
    scene expression ("images/episode6/224_smile.webp") with dissolve
    charlotte "Saya hanya melupakan usia saya. Saya lupa saya tidak lagi berusia 20 tahun dan ingin membantu Anda dengan renovasi."
    scene expression ("images/episode6/225_laugh.webp") with dissolve
    toby "Saya katakan bahwa saya akan mengurusnya."
    scene expression ("images/episode6/224_smile.webp") with dissolve
    charlotte "Saya tahu, tetapi ada banyak kotak dan hal -hal di loteng dan karena Anda bekerja sekarang, saya pikir itu adil untuk membantu Anda."
    scene expression ("images/episode6/225_smile.webp") with dissolve
    toby "Apa yang bisa saya katakan sekarang. Terima kasih!"
    scene expression ("images/episode6/224_awkward.webp") with dissolve
    charlotte "Anda bisa berterima kasih kepada punggung saya, karena dia melakukan semuanya."
    scene expression ("images/episode6/225_normal.webp") with dissolve
    toby "Tolong beritahu saya bahwa Anda tidak mengambil kotak berat."
    scene expression ("images/episode6/224_smile.webp") with dissolve
    charlotte "Saya mencoba setidaknya."
    scene expression ("images/episode6/225_curious.webp") with dissolve
    toby "Dan sekarang Anda memiliki masalah punggung lagi?"
    scene expression ("images/episode6/224_awkward.webp") with dissolve
    charlotte "Mungkin?"
    scene expression ("images/episode6/225_normal.webp") with dissolve
    toby "[mom!c] !!! Anda baru saja menyingkirkannya. Anda ingin mereka kembali?"
    scene expression ("images/episode6/224_sad.webp") with dissolve
    charlotte "Saya tidak bisa duduk dan tidak melakukan apa pun."
    scene expression ("images/episode6/225_laugh.webp") with dissolve
    toby "Anda dapat menulis buku Anda."
    scene expression ("images/episode6/224_laugh.webp") with dissolve
    charlotte "Bagus. Saya akan menulis buku saya. Pesta Pooper!"
    label memory_21:


        scene expression ("images/episode6/225_curious.webp") with dissolve
        toby "Bagaimana punggung Anda?"
        scene expression ("images/episode6/224_awkward.webp") with dissolve
        charlotte "Dalam banyak rasa sakit."
        scene expression ("images/episode6/225_normal.webp") with dissolve
        toby "Meletakkan. Aku akan memberimu pijatan."
        scene expression ("images/episode6/224_smile.webp") with dissolve
        charlotte "Anda tidak harus, sayang. Aku baik -baik saja, sungguh."
        scene expression ("images/episode6/225_normal.webp") with dissolve
        toby "Dengarkan saja saya sekali."
        scene expression ("images/episode6/224_laugh.webp") with dissolve
        charlotte "Baik ... tapi Anda harus berbalik sehingga saya bisa mengenakan beberapa celana dalam."
        scene expression ("images/episode6/226.webp") with dissolve
        charlotte "Tidak mengintip."
        scene expression ("images/episode6/227.webp") with dissolve
        toby "Saya menang."

        scene expression ("images/episode6/228.webp") with dissolve
        charlotte "Oke, saya siap untuk tangan ajaib Anda."

        scene expression ("images/episode6/229.webp") with dissolve
        toby "Katakan saja di mana itu menyakitkan."
        charlotte "Saya pikir Anda memberi saya pijatan penuh, bukan hanya di mana itu menyakitkan."
        scene expression ("images/episode6/230.webp") with dissolve
        toby "Saya akan memijat seluruh punggung Anda, tetapi saya perlu tahu di mana itu menyakitkan sehingga saya bisa lebih fokus di sana."
        charlotte "Apakah kamu manis."
        scene expression ("images/episode6/231.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode6/232.webp") with dissolve
        charlotte "Itulah tempatnya."
        scene expression ("images/episode6/233.webp") with dissolve
        toby "Saya bisa merasakan simpulnya. Anda benar -benar melakukan angka saat ini."
        toby "Itu saja, Anda tidak diizinkan naik ke atas sampai saya mengeluarkannya."
        scene expression ("images/episode6/234.webp") with dissolve
        charlotte "Sejak kapan Anda membuat aturan di rumah saya?"
        scene expression ("images/episode6/233.webp") with dissolve
        toby "Karena Anda sangat keras kepala dan sekarang saya harus menjagamu."
        scene expression ("images/episode6/234.webp") with dissolve
        charlotte "Tetapi begitu loteng selesai, apakah saya akan diizinkan untuk mengunjungi Anda?"
        scene expression ("images/episode6/233.webp") with dissolve
        toby "Sesering yang Anda inginkan."
        scene expression ("images/episode6/235.webp") with dissolve
        charlotte "Dan bagaimana dengan tidur di sana?"
        scene expression ("images/episode6/233.webp") with dissolve
        toby "Saya akan memikirkannya. Maksud saya, Anda mengajari saya bahwa tidak ada dalam hidup yang gratis."
        scene expression ("images/episode6/235.webp") with dissolve
        charlotte "Jadi itu artinya saya harus membayar pijatan ini?"
        scene expression ("images/episode6/236.webp") with dissolve
        toby "Mari kita katakan bahwa sesi pertama gratis."
        scene expression ("images/episode6/237.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Although, looking this ass so close is a pretty good payment.{/i}"
        scene expression ("images/episode6/238.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's my [mom]. I can't look at her ass.{/i}"
        scene expression ("images/episode6/239.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode6/240.webp") with dissolve
        charlotte "Anda bisa sedikit lebih rendah."
        scene expression ("images/episode6/241.webp") with dissolve
        toby "Di Sini?"
        scene expression ("images/episode6/240.webp") with dissolve
        charlotte "Ya ... di sekitar area itu."
        menu:
            "{i} pijat di sana {/i}" if not _in_replay:
                scene expression ("images/episode6/239.webp") with dissolve
                charlotte "Terima kasih sayang. Itu sempurna."
                scene expression ("images/episode6/233.webp") with dissolve
                toby "Tidak masalah. Dan mulai sekarang Anda meninggalkan kotak berat untuk saya."
                stop music fadeout 1.0
                scene expression ("images/episode6/251_1.webp") with dissolve
                erwin "Apa yang terjadi di sini?"
                scene expression ("images/episode6/252_1.webp") with dissolve
                charlotte "Saya mengambil kotak besar dari loteng dan saya menyakiti punggung saya, jadi saya meminta [toby!c] untuk memberi saya pijatan."
            "{i} [JGR] Bahkan lebih rendah {/i}"(csq="Charlotte +1 & Galeri Gambar & Penting untuk Path Charlotte \ '"):

                $ charlotte_rel += 1
                $ ep6_dirtyMassage = True

                scene expression ("images/episode6/242.webp") with dissolve
                toby "Saya akan pindah ke sini sehingga saya dapat memijat area itu dengan lebih baik."
                scene expression ("images/episode6/243.webp") with dissolve
                charlotte "Anda adalah spesialis."
                scene expression ("images/episode6/244.webp") with dissolve
                toby "Ya ... Maksud saya, saya telah menonton tepat satu video pijat hampir sampai akhir."
                scene expression ("images/episode6/245.webp") with dissolve
                charlotte "Saya tahu saya berada di tangan yang baik."
                scene expression ("images/episode6/246.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode6/247.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode6/248.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode6/249.webp") with dissolve
                charlotte "[toby!c], apakah ini masih pijatan?"
                toby "Apakah Anda tidak mengatakan bahwa saya adalah pro di sini?"
                $ unlockImage(persistent.charlotte_13)
                scene expression ("images/episode6/250.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                $ unlockMemory(persistent.memory_21)
                $ renpy.end_replay()

                stop music fadeout 1.0
                scene expression ("images/episode6/251.webp") with dissolve
                erwin "Apa yang terjadi di sini?"
                scene expression ("images/episode6/252.webp") with dissolve
                charlotte "Saya mengambil kotak besar dari loteng dan saya menyakiti punggung saya, jadi saya meminta [toby!c] untuk memberi saya pijatan."


    if ep6_dirtyMassage:
        scene expression ("images/episode6/251.webp") with dissolve
        erwin "Dan kenapa dia di atasmu?"
        scene expression ("images/episode6/252.webp") with dissolve
        charlotte "Jadi dia bisa melakukan pekerjaannya. Ini tidak seperti kita memiliki meja pijat hanya berbaring di sekitar rumah."
        scene expression ("images/episode6/253.webp") with dissolve
        charlotte "Jangan beri tahu saya bahwa Anda cemburu dari [son] Anda."
        scene expression ("images/episode6/254.webp") with dissolve
        erwin "Tentu saja tidak. Apakah Anda merasa lebih baik sekarang?"
        scene expression ("images/episode6/255.webp") with dissolve
        charlotte "Ya. Dia sangat terampil dengan tangannya."
    else:
        scene expression ("images/episode6/254.webp") with dissolve
        erwin "Saya mengerti. Dan apakah Anda merasa lebih baik sekarang?"
        scene expression ("images/episode6/252_1.webp") with dissolve
        charlotte "Ya. Dia sangat terampil dengan tangannya."

    scene expression ("images/episode6/256.webp") with dissolve
    toby "Bagaimanapun. Aku akan membiarkan kalian berdua berbicara. Saya akan menyiapkan sofa saya."
    scene expression ("images/episode6/257.webp") with dissolve
    erwin "Apakah Tris menendang Anda keluar dari kamarnya?"
    scene expression ("images/episode6/256.webp") with dissolve
    toby "Tidak, dia punya teman dan meminta saya untuk tidur di sofa malam ini."
    scene expression ("images/episode6/257.webp") with dissolve
    erwin "Anda baik -baik saja."
    scene expression ("images/episode6/258.webp") with dissolve
    toby "Selamat malam."
    scene expression ("images/episode6/259.webp") with dissolve
    charlotte "Selamat malam, sayang!"

    scene expression ("images/episode6/260.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should get some sleep.{/i}"

    return

label episode6_nightTris:
    $ progress = 94

    show screen ui_message("Two hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/261.webp") with dissolve
    hide screen ui_message
    play sound "audio/fx/notification_5.mp3"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Who's texting me at this hour?{/i}"
    scene expression ("images/episode6/262_texting.webp") with dissolve
    call sms_incoming ("tris", "Hey [bro]. You sleeping?") from _call_sms_incoming_80
    call sms_sent ("tris", "I would be, but this couch is not the most comfortable place to sleep.") from _call_sms_sent_55
    call sms_incoming ("tris", "Sucks to be you.") from _call_sms_incoming_81
    call sms_sent ("tris", "How come you're not sleeping?") from _call_sms_sent_56
    call sms_sent ("tris", "Is Bea snoring louder than me?") from _call_sms_sent_57
    call sms_incoming ("tris", "No. She's an angel. I can't sleep, I keep thinking about something and wanted to ask you about it.") from _call_sms_incoming_82
    call sms_sent ("tris", "Shoot!") from _call_sms_sent_58
    call sms_incoming ("tris", "I'm coming downstairs. If you're jerking off, make sure you put your penis back in your pants.") from _call_sms_incoming_83
    call sms_sent ("tris", "Very funny!") from _call_sms_sent_59
    hide screen message

    scene expression ("images/episode6/263.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode6/264.webp") with dissolve
    toby "Biarkan saya menebak, Anda sangat merindukan saya sehingga Anda tidak bisa tidur?"
    scene expression ("images/episode6/265.webp") with dissolve
    patricia "Tidak. Saya hanya ingin tahu tentang sesuatu."
    scene expression ("images/episode6/266.webp") with dissolve
    toby "Mari kita dengar."
    scene expression ("images/episode6/265.webp") with dissolve
    patricia "Mengapa Anda menyentak tadi malam?"
    scene expression ("images/episode6/267.webp") with dissolve
    toby "Benar-benar? Inilah mengapa Anda tidak bisa tidur? Anda bertanya -tanya mengapa saya kadang -kadang seorang pria dan tersentak?"
    scene expression ("images/episode6/268.webp") with dissolve
    patricia "Saya tahu bahwa kalian brengsek setiap hari, tetapi saya bertanya -tanya mengapa Anda melakukannya saat itu."
    scene expression ("images/episode6/266.webp") with dissolve
    toby "Saya tidak melihat ke mana Anda pergi dengan ini."
    scene expression ("images/episode6/268.webp") with dissolve
    patricia "Mengapa Anda menyentak setelah Anda melihat puting saya?"
    scene expression ("images/episode6/267.webp") with dissolve
    toby "Aku menyentak tidak ada hubungannya dengan putingmu, [sis]."
    scene expression ("images/episode6/269.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}At least one of us needs to believe that, because I'm sure as hell that it had everything to do with her nipple.{/i}"
    scene expression ("images/episode6/270.webp") with dissolve
    patricia "Anda menyadari bahwa saya mengenal Anda lebih baik daripada yang Anda kenal sendiri, bukan?"
    scene expression ("images/episode6/271.webp") with dissolve
    patricia "Bagus. Mari kita katakan secara hipotesis Anda menyentak karena Anda melihat puting saya. Apakah Anda masih memikirkannya saat Anda tersentak?"
    menu:
        "[JGR] Mungkin."(csq="Tris +1 & Galeri Gambar"):
            scene expression ("images/episode6/272.webp") with dissolve
            patricia "Tapi aku [sister], kamu tidak berpikir itu aneh?"
            scene expression ("images/episode6/266.webp") with dissolve
            toby "Mungkin sedikit, tapi bagaimanapun, Anda masih seorang wanita sebelum menjadi [sister] saya dan sejujurnya, Anda terlihat baik."
            scene expression ("images/episode6/268.webp") with dissolve
            patricia "Kamu benar -benar berpikir begitu?"
            scene expression ("images/episode6/273.webp") with dissolve
            toby "Nah, kita masih dalam cerita hipotetis kan?"
            scene expression ("images/episode6/270.webp") with dissolve
            patricia "Yup."
            scene expression ("images/episode6/273.webp") with dissolve
            toby "Dalam hal ini, ya. Kamu terlihat sangat baik. Terkadang saya bertanya -tanya mengapa Anda tidak pernah punya pacar, Anda benar -benar sempurna."
            scene expression ("images/episode6/268.webp") with dissolve
            patricia "Wow. Terima kasih."
            scene expression ("images/episode6/272.webp") with dissolve
            patricia "Jadi mengapa Anda harus segera tersentak? Apakah akan menyakiti Anda jika Anda memiliki boner terlalu lama?"
            scene expression ("images/episode6/273.webp") with dissolve
            toby "Bukankah kita sudah membahas hal ini selama permainan rock, kertas, gunting?"
            scene expression ("images/episode6/271.webp") with dissolve
            patricia "Ya atau tidak!"
            scene expression ("images/episode6/273.webp") with dissolve
            toby "Tidak, itu tidak menyakitkan, tapi bola biru bukanlah sesuatu yang menyenangkan untuk dimiliki."
            scene expression ("images/episode6/272.webp") with dissolve
            patricia "Bola Biru?"
            scene expression ("images/episode6/267.webp") with dissolve
            toby "Bagaimana saya berakhir dalam situasi ini."
            scene expression ("images/episode6/273.webp") with dissolve
            toby "Blue Balls adalah istilah yang digunakan oleh kita laki -laki ketika kita menjadi terangsang tetapi tidak mendapatkan rilis apa pun. Semua ketegangan itu menumpuk."
            scene expression ("images/episode6/274.webp") with dissolve
            patricia "Jadi secara hipotesis jika saya menarik top ke atas, Anda akan mendapatkan bola biru?"
            scene expression ("images/episode6/275.webp") with dissolve
            toby "Ummm ..."
            scene expression ("images/episode6/276.webp") with dissolve
            $ unlockImage(persistent.patricia_13)
            patricia "Nikmati bola biru Anda!"
            scene expression ("images/episode6/277.webp") with dissolve
            patricia "Selamat malam [toby!c]."
            scene expression ("images/episode6/278.webp") with dissolve
            toby "Umm ... selamat malam?"
            scene expression ("images/episode6/279.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the hell was that?{/i}"
        "Tentu saja tidak.":


            scene expression ("images/episode6/277.webp") with dissolve
            patricia "Oh ... oke!"
            scene expression ("images/episode6/278.webp") with dissolve
            toby "Umm ... selamat malam?"

    return

label episode6_weeks:
    show screen ui_message("During the next 7 weeks") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/280.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    hide screen ui_message
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/281.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/282.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/283.webp") with dissolve:
        yalign 1.0
        xalign 1.0
        linear 10.0 yalign 0.0 xalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/284.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if emma_break == False:
        scene expression ("images/episode6/285.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    if toby_job == 0:
        scene expression ("images/episode6/286.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    if toby_job == 1:
        scene expression ("images/episode6/287.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    scene expression ("images/episode6/288.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if lisa_path == True:
        scene expression ("images/episode6/289.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    if lauren_path == True:
        scene expression ("images/episode6/290.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    scene expression ("images/episode6/291.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if sheila_path == True:
        scene expression ("images/episode6/292.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    scene expression ("images/episode6/293.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/294.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/295.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if beatrice_path == True:
        scene expression ("images/episode6/296.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    if darlene_path == True:
        scene expression ("images/episode6/297.webp") with dissolve:
            yalign 1.0
            xalign 1.0
            linear 10.0 yalign 0.0 xalign 0.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    if katrina_path == True:
        scene expression ("images/episode6/298.webp") with dissolve:
            yalign 1.0
            xalign 1.0
            linear 10.0 yalign 0.0 xalign 0.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    if ep6_caughtJerking:
        scene expression ("images/episode6/299.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode6/300.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    scene expression ("images/episode6/301.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode6/302.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if emma_break == False:
        scene expression ("images/episode6/303.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    scene expression ("images/episode6/304.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if lisa_path == True:
        scene expression ("images/episode6/305.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    if lauren_path == True:
        scene expression ("images/episode6/306.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    scene expression ("images/episode6/307.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    stop music fadeout 7.0
    scene expression ("images/utils/black.png") with Dissolve (8)
    $ ui.pausebehavior(9.3)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
