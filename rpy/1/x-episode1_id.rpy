image ep1_004 = Movie(play="video/episode1/004.webm", loop=True)
image ep1_005 = Movie(play="video/episode1/005.webm", loop=True)
image ep1_011 = Movie(play="Video/Episode1/011.Webm", loop=True)
image ep1_012 = Movie(play="Video/Episode1/012.Webm", loop=True)
image ep1_013 = Movie(play="Video/Episode1/013.Webm", loop=True)
image ep1_014 = Movie(play="Video/Episode1/014.Webm", loop=True)
image ep1_015 = Movie(play="Video/Episode1/015.Webm", loop=True)
image ep1_016 = Movie(play="Video/Episode1/016.Webm", loop=True)
image ep1_137 = Movie(play="video/episode1/137.webm", image="images/episode1/137.webp", loop = False)

label episode1:
    $ persistent.mc = toby
    $ persistent.memories_fixed = True

    stop music fadeout 1.0
    scene expression ("gambar/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(1, 1) with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_newEpisode

    $ progress = 1
    scene expression ("gambar/episode1/001.webp") with dissolve

    toby "{4} {3} * Thinking * {1} {5}
{2} Hidup jauh lebih rapuh daripada yang kita pikirkan. {6}"
    toby "{4} {3} * Thinking * {1} {5}
{2} seberapa cepat hal -hal dapat berubah selamanya. {6}"
    toby "{4} {3} * Thinking * {1} {5}
{2} Suatu hari Anda bangun dan hari berikutnya Anda turun. {6}"
    scene expression ("gambar/episode1/002.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5}
{2} Saya tidak percaya bahwa perusahaan saya [13] bangkrut dan sekarang kami harus pindah. {6}"
    toby "{4} {3} * Thinking * {1} {5}
{2} Saya sudah terbiasa memiliki semua yang saya inginkan dan sekarang tiba -tiba semuanya hilang. {6}"
    toby "{4} {3} * Thinking * {1} {5}
{2} Kami baru saja kehilangan rumah kami, yang memiliki kolam renang, sauna, 10 kamar, bioskop dalam ruangan, 8 kamar mandi dan ... sial, sangat sulit untuk mengucapkan selamat tinggal pada semua ini. {6}"
    toby "{4} {3} * Thinking * {1} {5}
{2} Saya masih berharap ini hanya mimpi yang buruk dan di pagi hari ketika saya bangun, saya masih akan memiliki mobil sport saya di depan, yang saya dapatkan untuk ulang tahun ke -18 saya. {6}"
    scene expression ("gambar/episode1/003.webp") with dissolve
    toby ""When you reached the top of the mountain you should take a break and look down for a bit.\"{6}"

    label memory_01:
        scene expression ("gambar/episode1/004.webp") with dissolve
        show ep1_004 with dissolve


        toby "{4} {3} * Thinking * {1} {5}
{2} berbicara tentang turun. Itu Emma. Dia pacarku. Kami baru saja terhubung beberapa bulan yang lalu. {6}"
        toby "{4} {3} * Thinking * {1} {5}
{2} Saya dulu berada di kelas yang sama dengan dia [9], Cindy. Begitulah cara kami bertemu. {6}"
        toby "{4} {3} * Thinking * {1} {5}
{2} Saya membayar Cindy untuk membantu saya dengan pekerjaan rumah saya. Dengan bantuan, maksud saya dia melakukan semuanya untuk saya. {6}"
        toby "{4} {3} * Thinking * {1} {5}
{2} Saya pikir saya sedikit terlalu manja. {6}"
        scene expression ("gambar/episode1/005.webp") with dissolve
        show ep1_005
        hide ep1_004
        toby "{4} {3} * Thinking * {1} {5}
{2} mengatakan pria yang tersedot oleh bayi pirang yang cantik. Saya masih manja. {6}"
        toby "{4} {3} * Thinking * {1} {5}
{2} setidaknya sampai dia mengetahui bahwa perusahaan saya [13] bangkrut dan itulah alasan sebenarnya mengapa kita pergi. {6}"
        scene expression ("gambar/episode1/006.webp") with dissolve
        emma "Sayang, apakah semuanya baik -baik saja? Anda tampak sedikit libur hari ini."
        toby "Jangan khawatir, sayang. Saya baik-baik saja. Hanya saja besok adalah hari kita meninggalkan kota dan siapa yang tahu kapan kita akan bertemu satu sama lain."
        emma "Awww. Kamu sangat manis. Anda tidak ingin meninggalkan saya?"
        toby "Tentu saja tidak. Anda adalah hal terbaik yang pernah terjadi pada saya."
        scene expression ("gambar/episode1/007.webp") with dissolve
        emma "Anda selalu dapat mengunjungi saya, atau lebih baik lagi, saya bisa mengunjungi Anda. Saya yakin ada banyak hotel bintang 5 di kota itu, dan kami dapat menghabiskan beberapa malam seperti ini."
        toby "Ya ... kamu benar!"
        emma "Tentu saja saya. Tidak ada yang bisa membuat kita terpisah."
        menu:
            "{2} [14] Cium dia {6}"(csq="Emma +1"):
                scene expression ("gambar/episode1/008.webp") with dissolve
                $ emma_rel += 1
                toby "{4} {3} * Thinking * {1} {5}
{2} 5 hotel bintang pantatku. Saya harus memberitahunya cepat atau lambat bahwa saya bangkrut. {6}"
                scene expression ("gambar/episode1/007.webp") with dissolve
            "{2} Jangan menciumnya {6}":
                toby "{4} {3} * Thinking * {1} {5}
{2} 5 hotel bintang pantatku. Saya harus memberitahunya cepat atau lambat bahwa saya bangkrut. {6}"
        emma "Jadi, apa yang kamu katakan? Ingin bercinta denganku seperti ini adalah hari terakhirmu di bumi?"
        toby "Apakah itu pertanyaan?"
        scene expression ("gambar/episode1/009.webp") with dissolve
        emma "Sama sekali tidak."
        toby "Sial, kamu sudah sangat basah."
        scene expression ("gambar/episode1/010.webp") with dissolve
        emma "Dengan pacar sepertimu, aku selalu basah."
        emma "Dan Anda selalu sulit."
        menu:
            "{2} [14] Dirty Talk {6}"(csq="Emma +1 & Galeri Gambar"):
                $ unlockImage(persistent.emma_01)
                $ ep1_emma_dirtyTalk = True
                $ emma_rel += 1
                toby "Diam dan mengendarai saya seperti pelacur Anda. Aku akan mengisimu dengan buruk."
                emma "Saya suka saat Anda berbicara kotor dengan saya."
            "{2} Clean Talk {6}"(csq="Emma +1"):
                $ emma_rel += 1
                toby "Apa yang telah saya lakukan untuk pantas mendapatkan seorang gadis seperti Anda?"
                emma "Anda membuat saya tersenyum ketika saya turun, jadi saya hanya membayar Anda untuk bulan -bulan terbaik dalam hidup saya."
        scene expression ("gambar/episode1/011.webp") with dissolve
        show ep1_011
        emma "Ya, ya, ya. Berikan padaku sayang."
        if ep1_emma_dirtyTalk == True:
            toby "Itu saja. Naik penisku kamu jalang kotor."
        else:
            toby "Aku sangat mencintaimu!"
            emma "{4} {3} * moaning * {1} {5}
Saya juga!"
        scene expression ("gambar/episode1/012.webp") with dissolve
        show ep1_012
        hide ep1_011
        if ep1_emma_dirtyTalk == True:
            toby "Anda suka berteriak?"
            emma "{4} {3} * Panting * {1} {5}
Ya, Yessss saya lakukan."
            toby "Kemudian berteriak bahwa Anda pelacur."
            emma "{4} {3} * Loud * {1} {5}
Saya pelacur."
            toby "Siapa pelacur kamu?"
            emma "{4} {3} * moaning * {1} {5}
Saya youUr!"
        else:
            toby "Anda sangat sempurna."
            emma "{4} {3} * Loud * {1} {5}
Ya, ya, Yessss."
            emma "{4} {3} * terengah -engah * {1} {5}
Jangan berhenti."
        scene expression ("gambar/episode1/013.webp") with dissolve
        show ep1_013
        hide ep1_012
        emma "{4} {3} * Panting * {1} {5}
Dick Anda sangat besar, saya tidak akan pernah terbiasa dengan itu."
        if ep1_emma_dirtyTalk == True:
            toby "Anda suka penis besar, Anda jalang lapar?"
            emma "{4} {3} * moaning * {1} {5}
Saya hanya menyukai penis besar Anda."
            toby "Kamu bermimpi tentang penisku?"
            emma "{4} {3} * Loud * {1} {5}
Ya, saya bersedia!"
        else:
            toby "Apakah aku menyakitimu?"
            emma "{4} {3} * moaning * {1} {5}
Tidak, penismu sempurna. Aku sangat merindukannya!"
            toby "Aku akan merindukan payudaramu yang indah."
        scene expression ("gambar/episode1/014.webp") with dissolve
        show ep1_014
        hide ep1_013
        emma "{4} {3} * Loud * {1} {5}
Ya, ya, yesss ... bercinta denganku keras, sayang."
        toby "Mari kita ubah posisi."
        scene expression ("gambar/episode1/015.webp") with dissolve
        show ep1_015
        hide ep1_014
        if ep1_emma_dirtyTalk == True:
            emma "{4} {3} * moaning * {1} {5}
Ya, ya. Persetan aku dari belakang seperti kamu bercinta pelacur kotor."
            toby "Apakah Anda pelacur kotor?"
            emma "{4} {3} * Loud * {1} {5}
Ya saya."
        else:
            emma "{4} {3} * terengah -engah * {1} {5}
Aku akan segera cum. Saya selalu melakukannya saat Anda meniduri saya dari belakang."
            toby "Saya juga sangat dekat."
        scene expression ("gambar/episode1/016.webp") with dissolve
        show ep1_016
        hide ep1_015
        emma "{4} {3} * Panting * {1} {5}
Ya, ya. Di sana!"
        emma "{4} {3} * terengah -engah * {1} {5}
Jangan berhenti!"
        toby "Saya akan cum!"
        if ep1_emma_dirtyTalk == True:
            emma "Saya sedang minum pil! Isi aku!"
        else:
            emma "Jangan khawatir, saya sedang minum pil!"
        scene expression ("gambar/episode1/017.webp") with dissolve
        hide ep1_016
        with flash
        with flash
        emma "{4} {3} * Panting * {1} {5}
Astaga, ini sangat bagus!"
        toby "Sial ... sangat bagus."
        scene expression ("gambar/episode1/018.webp") with dissolve
        emma "Aku sangat mencintaimu."
        toby "Saya juga!"

        $ unlockMemory(persistent.memory_01)
        $ renpy.end_replay()

    emma "Aku tidak tahu apa yang akan aku lakukan tanpamu di sini."
    toby "Anda masih memiliki [9] Anda."
    emma "Cindy?"
    emma "Dia tidak pernah di rumah, sejak dia terhubung dengan pria itu."
    scene expression ("gambar/episode1/019.webp") with dissolve
    toby "Nah, seperti yang Anda katakan, saya bisa datang mengunjungi Anda dari waktu ke waktu."
    emma "{4} {3} * Whispering * {1} {5}
Dan saya akan mengirimi Anda telanjang sehingga Anda tidak akan melupakan saya."
    toby "Bagaimana saya bisa melupakan gadis cantik seperti Anda."
    emma "Anda memanjakan saya."
    toby "Anda pantas mendapatkan yang terbaik. Benar?"
    scene expression ("gambar/episode1/020.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("gambar/episode1/021.webp") with dissolve
    emma "Jika Anda mengatakannya, saya percaya Anda."


    show screen ui_message("Minggu") with long_dissolve
    $ progress = 2
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("gambar/episode1/022.webp") with dissolve
    hide screen ui_message
    toby "{4} {3} * Thinking * {1} {5}
{2} Saya tidur seperti log. Tadi malam itu gila. {6}"
    scene expression ("gambar/episode1/023.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5}
{2} Dia sangat cantik saat dia tidur. Aku akan merindukan menghabiskan waktu bersamanya. {6}"
    toby "{4} {3} * Thinking * {1} {5}
{2} menghabiskan waktu? Siapa saya bercanda? Aku akan merindukannya. {6}"
    toby "{4} {3} * Thinking * {1} {5}
{2} Saya harus mandi. {6}"
    scene expression ("gambar/episode1/024.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5}
{2} Saya harus memberi tahu Emma alasan sebenarnya mengapa kita pergi. {6}"
    toby "{4} {3} * Thinking * {1} {5}
{2} Tapi bagaimana jika dia benar -benar menyukai [9] saya mengatakan? {6}"
    scene expression ("gambar/episode1/025.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5}
{2} Bagaimana jika dia benar -benar bersamaku hanya untuk uang. Maksudku, aku bukan pria terbaik. {6}"
    toby "{4} {3} * Thinking * {1} {5}
{2} Seksnya bagus, tapi saya merasa harus bisa membicarakan segalanya dengan pacar saya. {6}"
    scene expression ("gambar/episode1/026.webp") with dissolve
    emma "Pagi seksi."
    toby "Selamat pagi cantik."
    scene expression ("gambar/episode1/027.webp") with dissolve
    emma "Seseorang senang melihat saya."
    toby "Dia selalu senang melihatmu."
    scene expression ("gambar/episode1/028.webp") with dissolve
    $ unlockImage(persistent.emma_02)
    emma "Tidak hari ini, sayang. Kami bersenang -senang tadi malam, dan kami akan bersenang -senang ketika ayah Anda datang mengunjungi saya. Oke?"
    toby "{4} {3} * Thinking * {1} {5}
{2} dia sangat gila dan menyenangkan ketika dia berbicara dengan penisku! {6}"
    emma "Di sini ... biarkan aku memberimu ciuman malam yang baik!"
    emma "Tapi sebaiknya Anda tidur sesudahnya."
    scene expression ("gambar/episode1/029.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("gambar/episode1/030.webp") with dissolve
    emma "Saya menyuruhnya tidur!"
    toby "Saya melihat."
    emma "Aku mencintaimu."
    toby "Aku pun mencintaimu!"
    scene expression ("gambar/episode1/031.webp") with dissolve
    emma "Bisakah Anda mencuci punggung saya?"
    toby "Tentu."


    scene expression ("gambar/episode1/032.webp") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("gambar/episode1/033.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()


    $ progress = 3
    scene expression ("gambar/episode1/034.webp") with long_dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Ini dia. Setelah menghabiskan seluruh hidup saya di satu kota, saya akhirnya pindah ke kota yang berbeda. {6}"
    scene expression ("gambar/episode1/035.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    "*Notification Sound*"
    scene expression ("gambar/episode1/034.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Saya tidak bisa mengatakan bahwa saya ingin tinggal di sana selamanya, tetapi saya selalu membayangkan diri saya pindah sendiri pada usia ini, tidak seperti ini. {6}"
    scene expression ("gambar/episode1/035.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    "*Notification Sound*"
    scene expression ("gambar/episode1/034.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Saya sudah 20 tahun. Hidupku tidak menuju ke mana -mana. Saya selalu berencana untuk mendapatkan perusahaan [8] saya suatu hari, tetapi setelah apa yang terjadi, sekarang saya tidak tahu apa yang harus dilakukan dengan hidup saya. {6}"
    scene expression ("gambar/episode1/035.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    "*Notification Sound*"
    scene expression ("gambar/episode1/034.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Kami bangkrut. Kami kehilangan segalanya dan sekarang kami pindah ke kota di mana mitra [8] saya berada. Seorang temannya akan membiarkan kami tinggal di sana, tetapi siapa yang tahu berapa lama. {6}"
    scene expression ("gambar/episode1/035.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    "*Notification Sound*"
    scene expression ("gambar/episode1/036.webp") with dissolve
    toby "Apakah Anda keberatan? Cukup letakkan ponsel Anda diam."
    scene expression ("gambar/episode1/037.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Itu Patricia, atau Tris seperti orang memanggilnya. Dia adalah yang lebih muda [9]. Selalu bertingkah seolah dia pantas mendapatkan segalanya. Sama seperti sekarang. 
Saya berbicara, dan dia bahkan tidak repot -repot menjawab saya. {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Kami dulu rukun, tetapi selama beberapa bulan terakhir seperti dia menjadi gila. Saya tidak tahu apa yang terjadi padanya, tetapi saya bahkan tidak bisa melakukan percakapan normal dengannya. {6}"
    scene expression ("gambar/episode1/036.webp") with dissolve
    toby "Saya berbicara dengan Anda, idiot. Letakkan ponsel Anda diam!"
    scene expression ("gambar/episode1/038.webp") with dissolve
    patricia "Anda selesai?"
    toby "Saya belum selesai! Kataku, letakkan ponselmu diam seperti orang normal!"
    patricia "Tahan pikiran itu."
    scene expression ("gambar/episode1/039.webp") with dissolve
    toby "Benar-benar?"
    toby "Singkirkan kakimu dari pangkuanku!"
    scene expression ("gambar/episode1/040.webp") with dissolve
    patricia "Umm ... nah! 
Saya nyaman."
    scene expression ("gambar/episode1/041.webp") with dissolve
    toby "Aku bilang pindahkan kakimu!"
    scene expression ("gambar/episode1/042.webp") with dissolve
    erwin "Hentikan, kalian berdua! Anda berdua dewasa muda. Bertindak seperti itu!"
    toby "{4} {3} * Thinking * {1} {5} {2}
Itu [13] saya. Pria yang kehilangan segalanya. Dia mengatakan bahwa kita adalah orang dewasa muda, tetapi dia tidak pernah memberi tahu kami bagaimana dia berhasil kehilangan segalanya. {6}"
    toby ""Kids, we're bankrupt and we have to move!\". Tidak ada penjelasan, tidak ada apa -apa. Dia tidak menghormati kita dan tidak pernah memilikinya, tetapi sekarang dia mengharapkan kita untuk berperilaku seperti orang dewasa muda! {6}"
    scene expression ("gambar/episode1/043.webp") with dissolve
    charlotte "Biarkan anak -anak menjadi. Mereka baru saja bosan. Ini perjalanan panjang. Anda tidak dapat mengharapkan mereka tetap diam!"
    toby "{4} {3} * Thinking * {1} {5} {2}
Dan itu [2] saya. Dia satu -satunya orang normal dalam hal ini [10]. Dia dulunya adalah gadis desa yang sederhana, tapi kemudian dia menikah [13], dan dia agak memberinya semua yang dia inginkan. {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Jadi dia mungkin sedikit manja, tetapi meskipun demikian dia mengambil seluruh kebangkrutan dengan cukup baik. Saya kira fakta bahwa dia tidak selalu kaya membuatnya sedikit lebih kuat, tidak seperti [13] dan [3], mungkin bahkan diri saya sendiri. {6}"
    scene expression ("gambar/episode1/044.webp") with dissolve
    erwin "Mereka hanya anak -anak. Hanya itu yang bisa Anda katakan. Itu alasan Anda untuk memelihara dua anak nakal manja."
    charlotte "Anda tidak hanya mengatakan itu tentang [7] kami. Saya membesarkannya dengan baik. Andalah yang mengacaukan dan ingin menemukan seseorang untuk disalahkan!"
    erwin "Oh, tapi saya harus disalahkan seseorang atas situasi ini."
    charlotte "Jangan coba -coba!"
    scene expression ("gambar/episode1/045.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("gambar/episode1/046.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Kami sudah datang. {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Akhir -akhir ini [2] dan [13] banyak berdebat. Saya pikir seluruh situasi ini berdampak pada hubungan mereka. {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Sekarang saya merasa tidak enak karena menyebabkan situasi ini. Saya seharusnya hanya meninggalkan Tris sendirian. {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Aku benci ketika keduanya berdebat. Rasanya seperti selamanya sejak kita bahagia. Saya tidak percaya bagaimana pecah dapat merusak A [10]. {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Saya hanya berharap mereka tidak akan bercerai. Aku benci itu, tapi tahu [13] dia akan melakukan segala yang dia bisa untuk tidak kalah [2] dan mendapatkan kembali perusahaannya. {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Dia selalu seperti itu dan dia terus -menerus mencoba membuat saya menjadi seperti dia. Terima kasih padanya, saya juga tidak quitter. {6}"


    $ progress = 4

    scene expression ("gambar/episode1/047.webp") with long_dissolve
    erwin "Di sinilah kita. Rumah manis rumah."
    patricia "Terlihat sangat ramai dan kecil!"
    erwin "Biasakan itu untuk saat ini. Anda bukan lagi seorang putri!"
    charlotte "Hentikan, tolong!"
    charlotte "Lihat, sayang, memang lebih kecil dari rumah kami sebelumnya, tetapi selama kami senang, sudah cukup!"
    scene expression ("gambar/episode1/048.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Untung kami senang. {6}"
    scene expression ("gambar/episode1/049.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Punggung saya sakit sudah hanya memikirkan berapa banyak kotak yang harus kita bawa ke dalam. {6}"
    scene expression ("gambar/episode1/050.webp") with dissolve
    charlotte "Ayo sayang. Mari kita lihat kamar Anda! Anak laki -laki dapat menangani kotak!"
    patricia "Apakah saya bisa memilih kamar saya?"
    charlotte "Tentu! Ayo masuk ke dalam."
    scene expression ("gambar/episode1/051.webp") with dissolve
    erwin "Pilih kamarnya sendiri. Lelucon yang luar biasa. Hanya ada dua kamar. Dia sangat manja."
    toby "Lihat [13]. Saya mengerti Anda kesal karena kehilangan segalanya, tetapi berhenti mengeluarkan masalah Anda, terutama pada [2]."
    toby "Jika Anda ingin melepaskan sedikit uap, kami dapat pergi ke gym dan menabrak setiap pukulan yang ada, tetapi [2] dan [3] tidak pantas mendapatkan ini."
    scene expression ("gambar/episode1/052.webp") with dissolve
    erwin "..."
    toby "{4} {3} * Thinking * {1} {5} {2}
Itulah yang saya pikirkan. Dia tidak pernah suka mendengarkan siapa pun! {6}"
    erwin "Apakah Anda akan membantu saya dengan kotak -kotak ini, atau Anda hanya akan berdiri di sana marah tentang apa yang telah saya lakukan salah?"
    toby "Saya datang karena saya tidak mencari seseorang untuk meletakkan masalah saya!"
    erwin "Baik, Anda benar, saya diliputi."
    scene expression ("gambar/episode1/053.webp") with dissolve
    toby "Dan Anda minta maaf?"
    erwin "Tidak menyesal seperti Anda setelah kami selesai dengan semua kotak!"
    scene expression ("gambar/episode1/054.webp") with dissolve
    erwin "Di sini ... mari kita lihat apakah saya telah membuang -buang uang saya untuk membayar keanggotaan gym Anda selama ini!"
    toby "Haha, sangat lucu!"
    scene expression ("gambar/episode1/055.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("gambar/episode1/056.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("gambar/episode1/055.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("gambar/episode1/056.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()


    $ progress = 5

    show screen ui_message("Beberapa jam kemudian") with fade
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("gambar/episode1/057.webp") with dissolve
    hide screen ui_message
    patricia "Pizza ada di sini!"
    toby "Akhirnya, saya kelaparan!"
    scene expression ("gambar/episode1/058.webp") with dissolve
    erwin "Saya bertanya apakah Anda ingin saya berhenti di restoran, dan Anda semua bilang tidak."
    charlotte "Itu 7 jam yang lalu."
    scene expression ("gambar/episode1/059.webp") with dissolve
    erwin "Berbicara tentang 7 jam yang lalu ..."
    erwin "Seseorang di ruangan ini memberi tahu saya bahwa saya bertindak seperti keledai dengan Anda. Saya tidak akan mengatakan siapa, tapi dia benar!"
    erwin "Maaf Charlotte, karena berteriak pada Anda dan Tris. Maaf kami berada dalam situasi ini!"
    erwin "Anda masih favorit saya [11]."
    scene expression ("gambar/episode1/060.webp") with dissolve
    toby "*batuk*
Hanya [11]!"
    scene expression ("gambar/episode1/059.webp") with dissolve
    erwin "Terserah, Anda berdua [15] saya, dan Anda pantas mendapatkan yang terbaik. Itulah alasan saya bekerja sangat keras."
    erwin "Untukmu dan untuk istriku yang cantik."
    erwin "Saya minta maaf karena kalian berdua harus berbagi kamar. Setelah kami memiliki lebih banyak uang, saya akan mempekerjakan seseorang untuk memperbaiki loteng untuk [16]!"
    toby "Mengapa saya harus pindah ke loteng?"
    erwin "Karena Anda sangat bijak dan membuka mata saya untuk kesalahan saya, mungkin dari atas sana Anda akan memiliki lebih banyak wahyu seperti itu."
    scene expression ("gambar/episode1/061.webp") with dissolve
    patricia "Jadi dia harus tidur di lantai agar terlihat seperti peningkatan ketika dia pindah dari kamar saya ke loteng?"
    charlotte "Itu gadisku! Saya suka cara Anda berpikir!"
    scene expression ("gambar/episode1/062.webp") with dissolve
    toby "Maaf, tapi saya akan makan. Saya tidak mendengar dengan baik saat saya lapar. Saya baru saja mendengar sesuatu seperti loteng dan tidur di lantai!"
    charlotte "Bon appétit."
    scene expression ("gambar/episode1/063.webp") with long_dissolve
    toby "Entah pizza ini sangat enak, atau kami kelaparan!"
    scene expression ("gambar/episode1/066.webp") with dissolve
    charlotte "Pizza itu sangat enak! Saya mendengar banyak hal baik tentang makanan di kota ini!"
    scene expression ("gambar/episode1/067.webp") with dissolve
    patricia "Saya mendengar bahwa mereka memiliki pantai yang indah!"
    scene expression ("gambar/episode1/064.webp") with dissolve
    erwin "Pada perjalanan bisnis terakhir saya di sini, saya tinggal di sebuah hotel dekat pantai. Saya pergi ke sana setiap pagi untuk jogging, dan saya bisa mengatakan, itu cantik!"
    scene expression ("gambar/episode1/065.webp") with dissolve
    toby "Kita harus pergi ke sana besok."
    scene expression ("gambar/episode1/068.webp") with dissolve
    patricia "Saya tidak bisa. Saya harus mendaftar di sekolah menengah setempat!"
    scene expression ("gambar/episode1/065.webp") with dissolve
    toby "Sucks to Be You!"
    scene expression ("gambar/episode1/068.webp") with dissolve
    patricia "Setidaknya sekali saya menyelesaikan sekolah menengah, saya akan kuliah, tidak seperti orang lain di meja ini."
    scene expression ("gambar/episode1/065.webp") with dissolve
    toby "Saya ingin lebih fokus menghasilkan uang daripada belajar."
    scene expression ("gambar/episode1/066.webp") with dissolve
    charlotte "Dan bagaimana kabarmu?"
    scene expression ("gambar/episode1/064.webp") with dissolve
    erwin "Jika dia seperti [8], dia akan baik -baik saja!"
    scene expression ("gambar/episode1/069.webp") with dissolve
    erwin "Sebenarnya, saya tidak berpikir saya adalah contoh terbaik saat ini, tetapi jika dia seperti saya beberapa tahun yang lalu, dia akan baik -baik saja!"
    scene expression ("gambar/episode1/070.webp") with dissolve
    patricia "Saya lelah. Aku akan mandi."
    patricia "Ngomong -ngomong [16], cobalah untuk tidak terlalu nyaman di tempat tidur saya!"
    toby "Ya, ya!"


    $ progress = 6

    scene expression ("gambar/episode1/071.webp") with long_dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Saya harus memberi tahu Emma bahwa kami telah menetap dan melihat apa yang dia lakukan. {6}"

    scene expression ("gambar/episode1/072_texting.webp") with dissolve
    call sms_sent ("Emma", "Hey seksi. Saya telah tiba di rumah baru saya.
Apa kabarmu?") from _call_sms_sent_4
    call sms_incoming ("Emma", "Hai seksi!
 Saya baru saja keluar dari kamar mandi. Bagaimana tempat baru?") from _call_sms_incoming_5
    call sms_sent ("Emma", "Tidak sebesar yang lain, tapi tidak apa -apa.") from _call_sms_sent_5
    call sms_incoming ("Emma", "Berbicara tentang besar. Apakah itu saya atau apakah payudara saya menjadi sedikit lebih besar?", img_icon="gambar/episode1/077_icon.webp", img="gambar/episode1/077.webp") from _call_sms_incoming_6
    call sms_sent ("Emma", "Saya membutuhkan gambar dengan pantat dan payudara Anda sehingga saya dapat membandingkannya.") from _call_sms_sent_6
    call sms_incoming ("Emma", "Anda Hog Kotor.") from _call_sms_incoming_7
    call sms_incoming ("Emma", "Jadi? Bagaimana menurutmu?", img_icon="gambar/episode1/081_icon.webp", img="gambar/episode1/081.webp") from _call_sms_incoming_8
    toby "{4} {3} * Thinking * {1} {5} {2}
Dia sangat seksi! Saya tidak percaya dia pacar saya. {6}"
    window hide
    $ unlockImage(persistent.emma_03)
    call sms_sent ("Emma", "Ya, Anda benar, payudara Anda menjadi sedikit lebih besar.") from _call_sms_sent_7
    call sms_incoming ("Emma", "Seberapa besar? Saya butuh foto kontol, jadi saya bisa membandingkan.") from _call_sms_incoming_9
    hide screen message


    scene expression ("gambar/episode1/084.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("gambar/episode1/085.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Jika wanita itu menginginkan, wanita itu menginginkannya. Anda tidak dapat berdebat dengan itu. {6}"
    scene expression ("gambar/episode1/086.webp") with dissolve
    toby "Kotoran!"
    patricia "Astaga! Anda Perv. Anda mengambil foto kontol di tempat tidur saya?"
    toby "TIDAK?"
    scene expression ("gambar/episode1/087.webp") with dissolve
    patricia "Pergi saja, tolong mandi air dingin."
    toby "Maaf Anda harus melihat itu!"
    patricia "Anda menjijikkan, dan pastikan untuk mencuci tangan kotor Anda!"
    scene expression ("gambar/episode1/088.webp") with dissolve
    toby "Umm ... ya. Sampai jumpa lagi!"
    scene expression ("gambar/episode1/089.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("gambar/episode1/090.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Ini sangat bagus. Sangat menyenangkan untuk melepaskan beberapa stres setelah hari seperti itu. {6}"
    scene expression ("gambar/episode1/091.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Saya harus mandi sekarang. {6}"
    scene expression ("gambar/episode1/092.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Umm. Di mana saya harus meletakkan selimut saya? Kamar ini sangat kecil. {6}"
    scene expression ("gambar/episode1/093.webp") with dissolve
    patricia "Anda dapat tidur di tempat tidur, tetapi pastikan Anda menjaga tangan Anda sendiri, Anda sudah!"
    toby "Saya bukan orang cabul. Saya hanya merindukan pacar saya."
    patricia "Maka Anda bisa tidur di lantai!"
    scene expression ("gambar/episode1/094.webp") with dissolve
    toby "Jangan seperti itu, dia tidak seburuk itu!"
    scene expression ("gambar/episode1/095.webp") with dissolve
    patricia "Dia seorang penggali emas!"
    toby "Dia tidak! Lihatlah kami, kami tidak punya uang yang tersisa, dan dia masih mencintaiku!"
    patricia "Apakah dia tahu bahwa kita bangkrut?"
    toby "Umm ..."
    toby "Mungkin?"
    patricia "Ya, benar! Anda melakukannya, tetapi jangan datang kepada saya menangis ketika dia meninggalkan Anda."
    toby "Jangan khawatir tentang saya! Saya akan baik -baik saja."
    scene expression ("gambar/episode1/096.webp") with dissolve
    patricia "Apa pun!"


    $ progress = 7
    show screen ui_message("Senin") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("gambar/episode1/097.webp") with dissolve
    hide screen ui_message
    toby "{4} {3} * Thinking * {1} {5} {2}
Sobat, saya tidur seperti log. Saya ingin tahu jam berapa sekarang. {6}"
    scene expression ("gambar/episode1/098.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Sial, Tris bersiap -siap untuk sekolah. Apa yang harus saya lakukan? {6}"
    menu:
        "{2} [14] Ambil mengintip {6}"(csq="Tris +1 & Galeri Gambar"):
            $ ep1_peek_on_patricia = True
            $ patricia_rel += 1
            $ unlockImage(persistent.patricia_01)
            scene expression ("gambar/episode1/099.webp") with dissolve
            toby "{4} {3} * Thinking * {1} {5} {2}
Aku akan terkutuk. Lihatlah payudara yang ceria itu. Dia terlihat sangat bagus! {6}"
            scene expression ("gambar/episode1/100.webp") with dissolve
            toby "{4} {3} * Thinking * {1} {5} {2}
Sayang sekali saya punya pacar. {6}"
            scene expression ("gambar/episode1/101.webp") with dissolve
            toby "{4} {3} * Thinking * {1} {5} {2}
Sialan [16]. Dia [9] Anda, bodoh. Anda tidak dapat melihat [9] Anda seperti itu. {6}"
            scene expression ("gambar/episode1/102.webp") with dissolve
            toby "{4} {3} * Thinking * {1} {5} {2}
Meskipun dia panas sekali. {6}"
        "{2} menjadi baik [4] {6}":
            scene expression ("gambar/episode1/101.webp") with dissolve
            toby "{4} {3} * Thinking * {1} {5} {2}
Tidak. Tidak hari ini. Hari ini saya baik [4]. {6}"
    scene expression ("gambar/episode1/103.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Hari Baru, Kota Baru. Saya merasa harus membantu [13] dengan uang, tetapi saya tidak yakin apa yang bisa saya lakukan untuk mendapatkannya. {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Saya selalu bisa pergi berburu pekerjaan, tetapi satu -satunya pekerjaan yang pernah saya miliki adalah di perusahaan [13] saya dan jujur saja, saya agak manja. {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Tidak ada yang benar -benar mengharapkan saya untuk melakukan apa pun, jadi itu benar -benar masih seperti saya tidak pernah bekerja sehari dalam seluruh hidup saya. {6}"
    scene expression ("gambar/episode1/104.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Bagaimanapun, saya kelaparan. Mari kita lihat apa yang kita miliki di lemari es, jika ada. {6}"
    scene expression ("gambar/episode1/105.webp") with dissolve
    toby "Pagi [2]!"
    scene expression ("gambar/episode1/106.webp") with dissolve
    charlotte "Sayang pagi. Bagaimana Anda tidur?"
    scene expression ("gambar/episode1/107.webp") with dissolve
    toby "Sangat buruk. Lantainya cukup keras."
    charlotte "Bayi yang malang. Apakah itu benar -benar sulit?"
    toby "Ya. [9] saya sangat buruk. Saya memintanya seperti seribu kali untuk membiarkan saya tidur di tempat tidurnya, tetapi dia tidak akan membiarkan saya."
    scene expression ("gambar/episode1/108.webp") with dissolve
    charlotte "Oh, sayang. Datang ke [17]. Biarkan dia memberimu ciuman!"
    menu:
        "{2} [14] Biarkan dia menciummu {6}"(csq="Charlotte +1 & Galeri Gambar"):
            $ unlockImage(persistent.charlotte_01)
            $ charlotte_rel += 1
            scene expression ("gambar/episode1/109.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("gambar/episode1/110.webp") with dissolve
            charlotte "Lebih baik?"
            toby "Jauh lebih baik!"
            charlotte "Anda tahu apa yang menurut saya lucu?"
            toby "Tidak. Apa?"
            charlotte "Tris hanya memberi tahu saya bahwa dia membiarkan Anda tidur di tempat tidur, dan di atas itu, saya datang tadi malam untuk mengucapkan selamat malam, dan melihatnya dengan mata sendiri."
            toby "Oh. Mungkin aku berbohong hanya untuk mendapatkan ciuman?"
            charlotte "Tentu saja. Lain kali ketika Anda ingin [17] mencium Anda, tanyakan saja!"
            toby "Akan lakukan!"
        "{2} Katakan padanya bahwa Anda berbohong {6}":
            scene expression ("gambar/episode1/110.webp") with dissolve
            toby "Saya bercanda. Dia membiarkan saya tidur di tempat tidur tadi malam."
            charlotte "Aku tahu. Dia membual tentang itu pagi ini, di atas itu, saya datang tadi malam untuk mengucapkan selamat malam, dan Anda berdua tidur seperti bayi."
            toby "Oh, jadi semua akting ini tidak ada gunanya?"
            charlotte "Agak!"
    scene expression ("gambar/episode1/111.webp") with dissolve
    toby "Ngomong -ngomong, apakah kita punya sesuatu untuk dimakan?"
    charlotte "Saya belum punya waktu untuk pergi ke toko dulu, jadi kami hanya memiliki susu dan sereal untuk saat ini."
    toby "Cukup bagus!"
    scene expression ("gambar/episode1/112.webp") with dissolve
    toby "Apa yang kamu lihat?"
    charlotte "Tidak banyak, hanya beberapa pekerjaan di sekitar kota."
    toby "Untuk?"
    charlotte "Bagi saya, jelas. Kami benar -benar membutuhkan uang."
    scene expression ("gambar/episode1/113.webp") with dissolve
    toby "Ada yang menarik bagi saya?"
    charlotte "Anda tidak harus bekerja, sayang!"
    toby "Tapi saya lakukan. Saya berusia 20 tahun sekarang dan tidak pernah bekerja sehari dalam hidup saya."
    toby "Saya merasa terlalu manja. Saya perlu melakukan sesuatu dengan hidup saya!"
    charlotte "Nah pekerjaan paling menarik yang saya temukan sejauh ini adalah ini untuk agen real estat."
    toby "Biarkan saya melihat!"
    scene expression ("gambar/episode1/114.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Belahan belah [1] sangat besar! {6}"
    menu:
        "{2} [14] Lihat lebih baik {6}"(csq="Charlotte +1 & Galeri Gambar"):
            $ charlotte_rel += 1
            $ unlockImage(persistent.charlotte_02)
            scene expression ("gambar/episode1/115.webp") with dissolve
            toby "{4} {3} * Thinking * {1} {5} {2}
Saya tidak percaya betapa baiknya dia mencari wanita seusianya. {6}"
            scene expression ("gambar/episode1/116.webp") with dissolve
            charlotte "Jadi? Bagaimana menurutmu?"
            scene expression ("gambar/episode1/117.webp") with dissolve
            toby "Umm ..."
            scene expression ("gambar/episode1/118.webp") with dissolve
        "{2} Saya seharusnya tidak mengambil risiko {6}":
            scene expression ("gambar/episode1/118.webp") with dissolve
            charlotte "Jadi? Bagaimana menurutmu?"
    toby "Ya. Maksud saya, pekerjaan itu terlihat menarik, dan di atas itu, saya cukup pandai meyakinkan orang, jadi saya bisa mencobanya."
    charlotte "Apakah Anda yakin ingin bekerja begitu cepat?"
    toby "Ini tidak seperti saya menjadi lebih muda. Cepat atau lambat, saya harus mulai bekerja. Sekarang lebih baik."
    scene expression ("gambar/episode1/119.webp") with dissolve
    charlotte "Tapi apa yang akan terjadi saat Anda kuliah? Atau apakah Anda masih berpikir itu tidak ada gunanya?"
    toby "Saya masih berpikir untuk kuliah. Saya tahu bahwa ada perguruan tinggi yang bagus di sini. Emma mengatakan bahwa akan menyenangkan untuk bergabung tahun depan bersamanya karena dia juga akan datang ke sini."
    charlotte "Oh. Jadi begitu. Aku senang untukmu."
    charlotte "Ngomong -ngomong, bagaimana dia mengambil semua ini? Langkah Anda, fakta bahwa Anda tidak akan dapat membeli anting -anting berliannya dan sebagainya?"
    scene expression ("gambar/episode1/120.webp") with dissolve
    toby "Uhm ... Bagus, kurasa!"
    charlotte "Anda belum memberi tahu dia alasan sebenarnya mengapa kami harus pergi, bukan?"
    toby "Tidak, dia tahu, kurang lebih!"
    scene expression ("gambar/episode1/119.webp") with dissolve
    charlotte "Anda harus berbicara dengannya. Saya yakin dia akan memahami situasinya."
    toby "Bagaimana jika dia meninggalkan saya ketika dia tahu bahwa saya bangkrut?"
    charlotte "Dia tidak akan, karena apa pun yang dipikirkan orang lain, dia benar -benar menyukai Anda, dan jika Anda dibuang, yah, maka dia bukan yang tepat untuk Anda."
    toby "Saya tahu, tapi ..."
    scene expression ("gambar/episode1/121.webp") with dissolve
    charlotte "Ya, saya tahu. Dia memiliki pantat besar, payudara besar untuk usianya, wajahnya cantik, dan dia mungkin sangat baik di tempat tidur, tapi itu tidak semua yang penting dalam suatu hubungan!"
    toby "Itu sangat spesifik."
    charlotte "Ini tidak seperti Anda berusia 16 tahun. Anda orang dewasa. Saya tahu Anda bukan perawan lagi!"
    toby "[12]!"
    scene expression ("gambar/episode1/119.webp") with dissolve
    charlotte "Bagaimanapun. Seperti yang saya katakan, lebih baik memberi tahu dia apa yang terjadi daripada membiarkan dia berpikir bahwa Anda tidak mencintainya lagi. Dan itulah mengapa hadiah menjadi lebih murah."
    toby "Anda pikir begitu?"
    charlotte "Tentu saja!"
    toby "Atau saya bisa bekerja keras dan terus membeli barang -barang mahal, dan dia tidak akan tahu!"
    charlotte "Saya menyukai gagasan melatih pantat Anda, tetapi bagian yang mahal dan kebohongan tidak terlalu banyak. Bukan itu cara Anda dibesarkan."
    scene expression ("gambar/episode1/121.webp") with dissolve
    toby "Ya, Anda mungkin benar!"
    scene expression ("gambar/episode1/122.webp") with dissolve
    charlotte "Bagaimanapun. Saya harus berpakaian dan mendapatkan bahan makanan. Nomor telepon untuk pekerjaan itu ada di laptop saya jika Anda benar -benar menginginkannya."
    toby "Terima kasih, [2]."
    charlotte "Tidak, terima kasih telah menjadi yang baik [5]."
    charlotte "Sampai jumpa lagi!"
    scene expression ("gambar/episode1/123.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
[1] benar. Saya harus berbicara dengan Emma tentang apa yang sebenarnya terjadi. Mungkin saat dia datang mengunjungi saya, saya akan mengatakan yang sebenarnya. {6}"
    scene expression ("gambar/episode1/124.webp") with long_dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Mari kita lihat ada apa dengan pekerjaan ini? {6}"
    scene expression ("gambar/episode1/125.webp") with dissolve
    toby "Selamat pagi. Saya melihat iklan tentang pekerjaan sebagai agen real estat. Saya bertanya -tanya apakah pekerjaan itu masih tersedia?"
    $ progress = 8
    woman "{4} {3} * di telepon * {1} {5}
Selamat pagi. Ya, pekerjaan itu masih tersedia. 
Pernahkah Anda bekerja sebagai agen real estat sebelumnya?"
    toby "Tidak. Sebenarnya, ini akan menjadi pekerjaan pertama saya."
    woman "{4} {3} * di telepon * {1} {5}
Berapa usiamu?"
    toby "Saya berumur 20 tahun. Saya baru saja pindah ke kota dan sedang mencari pekerjaan."
    woman "{4} {3} * di telepon * {1} {5}
Saya mengerti. Apakah Anda tersedia hari ini jam 11 pagi untuk wawancara?"
    toby "Tentu saja!"
    woman "{4} {3} * di telepon * {1} {5}
Saya senang mendengarnya. Saya akan mengirimi Anda detailnya."
    toby "Terima kasih banyak!"
    woman "{4} {3} * di telepon * {1} {5}
Siapa namamu?"
    toby "Maaf, saya lupa memperkenalkan diri."
    toby "Nama saya [16]."
    woman "{4} {3} * di telepon * {1} {5}
Oke [16]. Sampai jumpa lagi!"
    toby "Ya, tentu!"
    woman "{4} {3} * di telepon * {1} {5}
Semoga harimu menyenangkan!"
    toby "Semoga harimu menyenangkan!"
    scene expression ("gambar/episode1/126.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Nah, itu mudah. Saya tidak pernah tahu semudah ini untuk mendapatkan pekerjaan! {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Atau mungkin saya hanya pria yang beruntung. {6}"
    scene expression ("gambar/episode1/127.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Mari kita lihat apa yang ada di TV. {6}"
    show screen ui_message("Beberapa saat kemudian") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("gambar/episode1/128.webp") with dissolve
    hide screen ui_message
    charlotte "Sayang, bisakah kamu datang dan bantu aku dengan tas?"
    toby "Tentu [2]."
    scene expression ("gambar/episode1/129.webp") with dissolve
    toby "Di mana Anda menginginkannya?"
    charlotte "Di sana. Saya akan menyelesaikannya!"
    scene expression ("gambar/episode1/130.webp") with dissolve
    charlotte "Apakah Anda menelepon agen real estat?"
    toby "Ya, dan saya memiliki wawancara pada pukul 11:00."
    charlotte "Hari ini?"
    toby "Ya! Saya harus segera bersiap -siap."
    charlotte "Itu cepat. Mereka pasti benar -benar membutuhkan orang."
    toby "Atau saya hanya pria yang beruntung?"
    charlotte "Anda hanya beruntung!"
    scene expression ("gambar/episode1/131.webp") with dissolve
    charlotte "Maksud saya, lihat [2] Anda, Anda harus benar -benar beruntung memiliki [2] seperti saya!"
    toby "Sekarang saya tahu siapa yang dilakukan Tris."
    charlotte "Anda lucu!"
    scene expression ("gambar/episode1/132.webp") with dissolve
    toby "Saya akan berubah untuk wawancara."
    scene expression ("gambar/episode1/133.webp") with long_dissolve
    charlotte "Ya ampun ... siapa pria tampan itu?"
    charlotte "Jika Anda berpakaian seperti itu, mereka akan mempekerjakan Anda di tempat!"
    toby "Saya hanya bisa berharap begitu!"
    scene expression ("gambar/episode1/134.webp") with dissolve
    charlotte "Di sini ... biarkan aku memperbaikinya!"
    toby "Terima kasih [2]."
    charlotte "Anda dapat mengambil mobil saya dan mengambil Patricia dari sekolah setelah selesai."
    toby "Tentu. Saya akan melakukan itu, maka saya akan datang menjemput Anda, dan kita semua akan pergi ke pantai!"
    charlotte "Jika itu yang Anda inginkan, bagaimana saya bisa mengatakan tidak kepada Anda!"
    scene expression ("gambar/episode1/135.webp") with dissolve
    charlotte "Semoga Sukses Sayang."
    toby "Terima kasih [2]!"


    $ progress = 9

    scene expression ("gambar/episode1/136.webp") with long_dissolve
    toby "Halo, saya di sini untuk wawancara kerja."
    window hide
    show ep1_137 with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("gambar/episode1/137.webp") with dissolve
    hide ep1_137
    woman "Anda harus [16], kan?"
    toby "Ya Bu."
    katrina "Anda bisa memanggil saya Katrina."
    scene expression ("gambar/episode1/138.webp") with dissolve
    katrina "Tolong duduklah."
    toby "Terima kasih, Bu."
    toby "Maksudku, Katrina."
    scene expression ("gambar/episode1/139.webp") with dissolve
    katrina "Jadi? Siapa [16]? Ceritakan lebih banyak tentang diri Anda!"
    scene expression ("gambar/episode1/140.webp") with dissolve
    toby "Nah, saya berumur 20 tahun. Saya baru saja pindah ke kota ini, dan saya pikir saya harus mendapatkan pekerjaan untuk membantu [10] saya."
    scene expression ("gambar/episode1/139.webp") with dissolve
    katrina "Di mana Anda tinggal sebelum pindah ke sini?"
    scene expression ("gambar/episode1/140.webp") with dissolve
    toby "Uhm, Rictown."
    scene expression ("gambar/episode1/139.webp") with dissolve
    katrina "Oh, menarik. Saya juga dulu tinggal di sana. Di bagian kota mana Anda tinggal?"
    scene expression ("gambar/episode1/140.webp") with dissolve
    toby "Saya lebih suka tidak mengatakan, jika tidak apa -apa?"
    scene expression ("gambar/episode1/141.webp") with dissolve
    katrina "Tidak, nak. Tidak apa -apa. Saya bertanya, Anda menjawab!"
    toby "Uhm. Saya tinggal di bagian atas."
    katrina "Maksudmu bagian yang kaya?"
    toby "Ya."
    scene expression ("gambar/episode1/139.webp") with dissolve
    katrina "[6] Anda bekerja untuk beberapa keledai kaya di sana?"
    scene expression ("gambar/episode1/140.webp") with dissolve
    toby "Uhm, tidak juga."
    scene expression ("gambar/episode1/142.webp") with dissolve
    katrina "Menarik ... jadi Anda berasal dari orang kaya [10]."
    scene expression ("gambar/episode1/143.webp") with dissolve
    katrina "Dan kenapa Anda ingin bekerja di sini jika Anda berasal dari orang kaya [10]?"
    toby "Mengapa ada yang menginginkan pekerjaan?"
    katrina "Saya mengerti. Anda bangkrut."
    scene expression ("gambar/episode1/144.webp") with dissolve
    katrina "Jadi, apakah Anda pikir Anda memiliki apa yang diperlukan untuk memuaskan saya?"
    toby "{4} {3} * Thinking * {1} {5} {2}
Wanita ini gila. {6}"
    menu:
        "Uhm, memuaskanmu?":
            katrina "Ya sayang, untuk bekerja keras sampai saya puas."
            katrina "Apa lagi?"
            toby "Tidak ada apa-apa. Ya, saya benar -benar berpikir saya bisa bekerja sampai Anda puas."
            scene expression ("gambar/episode1/145.webp") with dissolve
            katrina "Tidak, saya tidak suka bagaimana kedengarannya. Saya akan mengatakannya lagi."
            katrina "Apakah Anda pikir Anda dapat memuaskan saya?"
        "[14] Saya dapat memuaskan wanita mana pun, jadi mengapa Anda berbeda?"(csq="Katrina +1 & Gambar Galeri"):
            $ katrina_rel += 1
            $ unlockImage(persistent.katrina_01)
            katrina "Berani! Saya menyukainya, tetapi saya lebih berpikir seperti, dapatkah Anda bekerja sampai saya puas?"
            toby "Oh, ya. Saya benar -benar berpikir saya bisa bekerja sampai Anda puas."
            scene expression ("gambar/episode1/145.webp") with dissolve
            katrina "Sebenarnya, saya lebih menyukai jawaban pertama Anda."
            katrina "Apakah Anda pikir Anda dapat memuaskan saya?"

    scene expression ("gambar/episode1/146.webp") with dissolve
    toby "Ya, Bu. Aku bisa memuaskanmu!"
    scene expression ("gambar/episode1/147.webp") with dissolve
    katrina "Jadi, jika Anda benar -benar ingin mendapatkan uang, mengapa Anda tidak menjual narkoba seperti orang normal? Anda benar -benar ingin memasuki sistem yang rusak seperti ini, di mana ikan besar mengambil segalanya, dan Anda hanya mendapatkan apa yang mereka berikan kepada Anda?"
    katrina "Mengapa menjadi budak saat Anda bisa menjadi raja?"
    scene expression ("gambar/episode1/148.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Apakah dia benar -benar menanyakan ini padaku? Wawancara macam apa ini? {6}"
    scene expression ("gambar/episode1/149.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    $ progress = 10
    woman "Uhum, uhum. Permisi!"
    scene expression ("gambar/episode1/150.webp") with dissolve
    katrina "Halo, Sayang. Saya menguji karyawan masa depan Anda."
    woman "Saya yakin."
    scene expression ("gambar/episode1/151.webp") with dissolve
    woman "Anda harus [16] kan?"
    toby "Ya, Bu."
    scene expression ("gambar/episode1/152.webp") with dissolve
    darlene "Nama saya Darlene. Kami berbicara pagi ini di telepon."
    toby "Senang berkenalan dengan Anda!"
    scene expression ("gambar/episode1/153.webp") with dissolve
    darlene "Maaf, saya terlambat. Saya memiliki beberapa bisnis yang belum selesai dengan beberapa apartemen."
    scene expression ("gambar/episode1/154.webp") with dissolve
    toby "Tidak masalah."
    darlene "Saya berharap pacar saya tidak memberi Anda terlalu banyak masalah."
    toby "{4} {3} * Thinking * {1} {5} {2}
Pacar perempuan? Bos masa depan saya adalah seorang lesbian? Wow! {6}"
    toby "Sama sekali tidak."
    darlene "Saya senang mendengarnya."
    scene expression ("gambar/episode1/155.webp") with dissolve
    darlene "Sayang, bisakah kamu meninggalkan kami? Saya ingin mengenal [16] sedikit lebih baik!"
    katrina "Tentu saja, cintaku."
    scene expression ("gambar/episode1/156.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("gambar/episode1/157.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("gambar/episode1/158.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Oke ... itu sangat mencurigakan. {6}"
    scene expression ("gambar/episode1/159.webp") with dissolve
    darlene "Jadi, di telepon Anda menyebutkan bahwa Anda baru saja pindah ke kota dan Anda sudah mencari pekerjaan. Saya suka ini pada seseorang."
    darlene "Itu berarti mereka bekerja keras. Namun, Anda juga menyebutkan bahwa ini akan menjadi pekerjaan pertama Anda. Kenapa begitu?"
    toby "Nah, ini akan menjadi pekerjaan nyata pertama saya. Saya sering membantu di perusahaan [13] saya, tetapi segalanya tidak berjalan dengan baik bagi kami, dan sekarang kami telah pindah ke sini."
    darlene "Apakah Anda tahu sesuatu tentang rumah?"
    toby "Saya tahu sedikit bagian struktural rumah, dan saya sangat pandai membaca orang, jadi saya dapat membujuk mereka untuk membeli atau menyewa rumah."
    scene expression ("gambar/episode1/160.webp") with dissolve
    darlene "Begitu? Lalu mari kita dengarkan apa yang harus Anda katakan tentang saya?"
    toby "Uhm? Itu tidak sesuai."
    darlene "Anda dapat membuatnya terdengar sesuai atau hanya mengatakan apa pun yang Anda inginkan, dan kami akan memutuskan apa yang harus dilakukan dengan informasi itu."
    scene expression ("gambar/episode1/161.webp") with dissolve
    $ progress = 11
    menu:
        "{2} [14] Go Personal {6}"(csq="Darlene +1 & Galeri Gambar"):
            $ darlene_rel += 1
            $ unlockImage(persistent.darlene_01)
            scene expression ("gambar/episode1/162.webp") with dissolve
            toby "Anda sedang menjalin hubungan dengan wanita lain meskipun Anda tidak 100 %% yakin Anda seorang lesbian. Kemungkinan besar Anda memiliki beberapa hubungan yang gagal dan hati Anda sangat hancur, sehingga Anda kehilangan kepercayaan pada pria."
            toby "Meskipun Anda adalah bos perusahaan Anda sendiri dan Anda terbiasa dihormati, Anda bosan."
            toby "Anda suka ketika orang lain yang bertanggung jawab, itu sebabnya pacar Anda sangat suka memerintah karena Anda menyukainya, dan Anda menyukai gagasan untuk menjadi tunduk di luar pekerjaan."
            toby "Ketika Anda meminta saya untuk mengatakan sesuatu tentang Anda, Anda mengharapkan sesuatu yang lebih seperti, Anda adalah tipe wanita yang bekerja keras untuk mencapai tempat Anda sekarang."
            toby "Itu karena saya menjadi orang yang diwawancarai seharusnya tidak mendapatkan pribadi ini. Tetapi fakta bahwa saya sedang berbicara dengan Anda meskipun Anda bisa menjadi bos masa depan saya membuat Anda sangat bersemangat."
            toby "Karena jauh di lubuk hati, itulah yang benar -benar Anda inginkan."
            scene expression ("gambar/episode1/163.webp") with dissolve
            darlene "Uhm ... ya, jadi."
            scene expression ("gambar/episode1/164.webp") with dissolve
            darlene "Maaf, saya tidak mengharapkan itu, jadi saya tidak yakin harus berkata apa."
            toby "Saya harap saya tidak berlebihan."
            darlene "Mungkin sedikit, tapi yang mengejutkan itu tidak mengganggu saya."
        "{2} tetap aman {6}":

            scene expression ("gambar/episode1/162.webp") with dissolve
            toby "Anda adalah tipe wanita yang bekerja sangat keras untuk berada di tempat dia sekarang, dan perusahaan ini seperti bayi Anda."
            toby "Dengan ukuran kantor, saya dapat mengatakan bahwa tidak ada banyak orang yang bekerja di sini karena Anda ingin dapat mengetahui semua yang terjadi."
            toby "Anda suka memegang kendali sehingga jika terjadi kesalahan, Anda tidak dapat menyalahkan orang lain selain diri Anda sendiri."
            toby "Ketika Anda mendengar bahwa saya berusia 20 tahun, Anda mengatakan pada diri sendiri bahwa Anda dapat mengajari saya semua yang Anda ketahui karena Anda agak lelah bekerja dengan orang lain."
            toby "Jadi Anda memutuskan untuk mempekerjakan seseorang yang muda bahwa Anda akan dapat merawat dan akhirnya percaya."
            scene expression ("gambar/episode1/163.webp") with dissolve
            darlene "Ini sebenarnya benar -benar bagus!"
            darlene "Saya suka kemana perginya."

    scene expression ("gambar/episode1/165.webp") with dissolve
    darlene "Aku akan jujur padamu. Aku menyukaimu, mungkin kamu sedikit berani, tapi aku suka itu."
    darlene "Saya yakin Kat memberi Anda nomor teleponnya untuk meneleponnya karena dia suka mempekerjakan pria tampan di klubnya untuk menarik wanita muda."
    darlene "Dan jika di klub ada wanita muda, akan ada juga pria untuk membayar banyak uang untuk mengesankan mereka, jadi semua orang mendapat untung dari itu."
    darlene "Saya tidak dapat menawarkan kepada Anda pesta dan kesenangan yang dia bisa, tetapi saya dapat menawarkan Anda penghasilan yang sangat stabil dan kehidupan yang baik."
    darlene "Besok saya bertemu dengan klien untuk apartemen. Anda akan bergabung dengan saya, dan saya akan membiarkan Anda melakukan pekerjaan Anda."
    darlene "Saya ingin melihat apakah Anda benar -benar dapat membaca orang sebaik yang Anda katakan dan meyakinkan mereka untuk membeli."
    darlene "Saya biasanya tidak melakukan hal -hal seperti ini, tetapi saya sangat, sangat menyukai Anda."
    darlene "Jadi saya akan memberi Anda kesempatan. Jika Anda berhasil menjual apartemen, Anda mendapatkan 20 %% dari laba."
    scene expression ("gambar/episode1/166.webp") with dissolve
    toby "Saya tidak tahu harus berkata apa. Saya tidak mengharapkan ini."
    scene expression ("gambar/episode1/167.webp") with dissolve
    darlene "Anda tidak perlu mengatakan apa -apa sekarang, pikirkan saja siapa yang akan Anda hubungi besok. Saya atau Kat."
    toby "Terima kasih atas kesempatannya. Saya akan tidur di atasnya dan memanggil Anda hal pertama di pagi hari."
    scene expression ("gambar/episode1/168.webp") with dissolve
    darlene "Saya harap Anda akan membuat pilihan yang tepat."
    toby "Terima kasih untuk ini!"
    scene expression ("gambar/episode1/169.webp") with dissolve
    darlene "Tidak terima kasih! Saya sangat menikmati wawancara ini."
    toby "Semoga harimu menyenangkan, Bu."
    darlene "Tolong hubungi saya Darlene!"
    toby "Bye Darlene."
    darlene "Bye [16]."


    $ progress = 12

    scene expression ("gambar/episode1/170.webp") with long_dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Wawancara itu benar -benar sesuatu. Itu bukan yang saya harapkan, tetapi baik Darlene dan Katrina adalah wanita yang sangat menarik. {6}"
    toby "{4}{3}* thinking *{1}{5}{2}\nI wonder who I should call. On one hand working as a real estate agent would be stable income and a safe job.{6}"
    scene expression ("images/episode1/171.webp") with dissolve
    toby "{4}{3}* thinking *{1}{5}{2}\nOn the other hand Katrina's life sounds interesting. I'm not so sure about the drugs thing, but from what Darlene said it does sound interesting.{6}"
    toby "{4}{3}* thinking *{1}{5}{2}\nI don't know what to do. I'll have to think more about it.{6}"
    toby "{4}{3}* thinking *{1}{5}{2}\nAnyway, let's go pick up Tris from school.{6}"
    scene expression ("images/episode1/172.webp") with dissolve
    toby ""
    scene expression ("") with dissolve
    toby ""
    scene expression ("") with dissolve
    toby ""
    patricia ""
    toby ""
    patricia ""
    toby ""
    patricia ""
    scene expression ("") with dissolve
    toby ""
    patricia ""
    patricia "Ngomong -ngomong, kenapa kamu begitu berpakaian?"
    toby "Saya memiliki wawancara kerja."
    patricia "Anda? Bekerja?"
    scene expression ("gambar/episode1/176.webp") with dissolve
    toby "Ya. Apa yang aneh tentang itu?"
    patricia "Anda tidak pernah bekerja sehari pun dalam hidup Anda."
    toby "Saya membantu [13] di perusahaannya."
    patricia "Ya. Seperti yang saya katakan, Anda tidak pernah bekerja sehari pun dalam hidup Anda."
    patricia "Tapi bagaimanapun juga. Bagaimana wawancara berjalan?"
    toby "Saya akan memberi tahu Anda nanti setelah kami mengambil [2]. Saya benar -benar tidak ingin menceritakan kisah yang sama dua kali."
    scene expression ("gambar/episode1/177.webp") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("gambar/episode1/178.webp") with dissolve
    toby "Mengapa terburu -buru?"
    patricia "Apakah Anda bercanda? Saya belum melihat pantai dalam hampir 7 bulan."
    scene expression ("gambar/episode1/179.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Baik [2] dan Tris membutuhkan waktu lama untuk bersiap -siap. {6}"
    scene expression ("gambar/episode1/180.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    toby "{4} {3} * Thinking * {1} {5} {2}
Wow. [2] terlihat cantik. {6}"
    charlotte "Apakah Tris siap?"
    toby "Belum."
    patricia "Saya! Aku akan turun sekarang!"
    scene expression ("gambar/episode1/181.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    toby "{4} {3} * Thinking * {1} {5} {2}
Seperti [18], seperti [11]. {6}"
    scene expression ("gambar/episode1/182.webp") with dissolve
    toby "Ayo pergi!"


    $ progress = 13

    scene expression ("gambar/episode1/183.webp") with long_dissolve
    patricia "Pantai ini terlihat sangat keren. Tidak sabar untuk berenang."
    charlotte "Saya tidak sabar untuk tidur di lounger itu. Mereka terlihat nyaman!"
    toby "Banyak lelah?"
    scene expression ("gambar/episode1/184.webp") with dissolve
    charlotte "Sedikit. Bergerak adalah masalah yang cukup besar."
    scene expression ("gambar/episode1/185.webp") with dissolve
    patricia "Wow ... mereka memiliki jaring bola voli. Kami benar -benar harus bermain [16]."
    toby "Apakah kita?"
    scene expression ("gambar/episode1/186.webp") with dissolve
    patricia "Yesss!"
    toby "Bagus!"
    scene expression ("gambar/episode1/187.webp") with dissolve
    charlotte "Jadi? Bagaimana wawancara?"
    toby "Sebenarnya sangat baik. Ada dua wanita yang menawari saya pekerjaan."
    patricia "Anda belum pernah bekerja dalam hidup Anda dalam hidup Anda dan mendapat dua tawaran pekerjaan dari satu wawancara?"
    toby "Ya, itu aneh."
    scene expression ("gambar/episode1/188.webp") with dissolve
    toby "Jadi ada wanita ini bernama Darlene. Dialah yang saya ajak bicara di telepon pagi ini."
    toby "Dan pacarnya, Katrina. Dia adalah pemilik klub sejauh yang saya mengerti."
    toby "Ketika saya pergi ke sana, Katrina ada di kantornya, dan dia mengolok -olok saya sedikit!"
    scene expression ("gambar/episode1/189.webp") with dissolve
    patricia "Nah, wajah Anda memohon untuk diolok -olok!"
    scene expression ("gambar/episode1/190.webp") with dissolve
    charlotte "Jangan bersikap kasar kepada [4] Anda."
    scene expression ("gambar/episode1/188.webp") with dissolve
    toby "Ngomong -ngomong, jadi dia agak menawari saya pekerjaan di klubnya, tapi saya belum yakin apa, karena saat itulah Darlene masuk."
    scene expression ("gambar/episode1/191.webp") with dissolve
    charlotte "Jadi pada dasarnya dia mencuri karyawan pacarnya?"
    toby "Anda bisa mengatakan mereka sedang memperebutkan saya."
    scene expression ("gambar/episode1/192.webp") with dissolve
    patricia "Itu akan menjadi yang pertama dan terakhir kali dua gadis akan memperebutkan Anda."
    scene expression ("gambar/episode1/193.webp") with dissolve
    toby "Sangat lucu."
    scene expression ("gambar/episode1/188.webp") with dissolve
    toby "Ngomong -ngomong, Darlene tahu apa yang Katrina lakukan, jadi dia mengatakan bahwa aku punya sampai besok untuk memutuskan untuk siapa bekerja."
    toby "Besok saya akan menelepon Darlene atau Katrina."
    scene expression ("gambar/episode1/194.webp") with dissolve
    charlotte ""
    scene expression ("") with dissolve
    patricia "Saya tidak setuju dengan [2]. Saya pikir bekerja di klub bisa lebih menarik dan di atas itu, siapa tahu. Mungkin Anda akan bertemu dengan pacar baru."
    toby "Saya punya pacar."
    scene expression ("gambar/episode1/196.webp") with dissolve
    patricia "Mungkin, tapi dia menyebalkan."
    charlotte "Perhatikan lidah Anda, wanita muda. Dia bukan wanita jalang, dan selama mereka saling mencintai, hanya itu yang penting."
    scene expression ("gambar/episode1/197.webp") with dissolve
    patricia "Dia bahkan tidak memberitahunya mengapa kami harus pergi."
    charlotte "Itu bisnis mereka, bukan milikmu."
    patricia "Dia seorang penggali emas!"
    scene expression ("gambar/episode1/198.webp") with dissolve
    toby "Apa pun!
Saya akan mengambil sesuatu untuk diminum dari bar. Ingin apapun?"
    patricia "Saya ingin limun."
    toby "Saya akan membelikan Anda satu jika Anda mengambil kembali apa yang Anda katakan tentang Emma."
    scene expression ("gambar/episode1/199.webp") with dissolve
    patricia "Lalu aku akan membeli sendiri."
    scene expression ("gambar/episode1/200.webp") with dissolve
    charlotte "Jangan menganggapnya secara pribadi. Saya tidak tahu di mana saya salah dengannya."
    toby "Jangan khawatir [2]. Jadi? Apa yang bisa saya dapatkan dari Anda?"
    charlotte "Kejutkan aku!"
    scene expression ("gambar/episode1/201.webp") with dissolve
    toby "Saya akan!"
    scene expression ("gambar/episode1/202.webp") with dissolve
    toby "{4}{3}* thinking *{1}{5}{2}\nI hate the idea that maybe Tris is right, but it hurts when she talks like that about my girlfriend.{6}"
    scene expression ("images/episode1/203.webp") with dissolve
    patricia "Bagaimana rasanya?"
    toby "Merasa apa?"
    patricia "Rasa sakit ketika Anda menyadari bahwa [9] Anda selalu benar?"
    toby "Persetan!"
    scene expression ("") with dissolve
    barman ""
    $ progress = 14
    menu:
        ""(csq=""):
            $ patricia_rel += 1
            $ unlockImage(persistent.patricia_02)
            scene expression ("images/episode1/205.webp") with dissolve
            toby ""
            scene expression ("") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("") with dissolve
            patricia ""
            toby ""
            scene expression ("") with dissolve
            toby ""
            toby ""
            scene expression ("") with dissolve
            barman ""
            toby "Maaf?"
        "{2} dia tidak pantas mendapatkannya {6}":
            scene expression ("gambar/episode1/210.webp") with dissolve
            patricia "Apakah Anda tidak malu membiarkan seorang wanita membayar minumannya sendiri?"
            toby "Biarkan saya memikirkannya sebentar."
            scene expression ("") with dissolve
            toby ""
            scene expression ("") with dissolve
    barman ""
    toby ""
    barman ""
    scene expression ("") with dissolve
    toby ""
    barman ""
    toby ""
    barman ""
    barman ""
    toby ""
    toby ""
    scene expression ("") with dissolve
    barman ""
    scene expression ("") with dissolve
    toby "Terima kasih kawan!"
    scene expression ("gambar/episode1/214.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Mana yang harus saya berikan [2]? {6}"
    menu:
        "{2} [14] Yang dengan alkohol di dalamnya {6}"(csq="Charlotte +1"):
            $ charlotte_rel += 1
            $ ep1_get_charlotte_drunk = True
        "{2} yang tanpa alkohol di dalamnya {6}":
            pass
    scene expression ("gambar/episode1/215.webp") with dissolve
    toby "Ini dia [2]."
    charlotte "Terima kasih, Sayang."
    scene expression ("gambar/episode1/216.webp") with long_dissolve
    patricia "Saya punya ide!"
    toby "Membuatku takjub!"
    patricia "Jika Anda berhasil mengalahkan saya di bola voli, saya akan minta maaf atas semua yang saya katakan tentang Emma!"
    scene expression ("gambar/episode1/217.webp") with dissolve
    toby "Dan Anda juga tidak akan mengatakan hal buruk tentang dia di masa depan?"
    toby "Kesepakatan."
    scene expression ("gambar/episode1/218.webp") with dissolve
    patricia "Mari kita lihat Anda mencoba dulu."
    scene expression ("gambar/episode1/219.webp") with dissolve
    toby "Anda memintanya!"
    scene expression ("gambar/episode1/220.webp") with long_dissolve
    $ progress = 15
    menu:
        "{2} [14] Biarkan dia menang {6}"(csq="Tris +1 & Galeri Gambar & Penting untuk Jalur Tris '"):
            $ patricia_rel += 1
            $ ep1_let_patricia_win = True
            $ unlockImage(persistent.patricia_03)
            scene expression ("gambar/episode1/221.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("gambar/episode1/222.webp") with dissolve
            patricia "Memperdaya!"
            toby "Aku membiarkanmu menang!"
            scene expression ("gambar/episode1/223.webp") with dissolve
            patricia "Saya yakin ... Anda ayam!"
            toby "Itu saja!"
        "{2} Cobalah menang {6}":
            scene expression ("gambar/episode1/221.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("gambar/episode1/224.webp") with dissolve
            patricia "Aku membiarkanmu menang. Saya bosan berbicara tentang pacar Anda!"
            toby "Ya, benar!"
            scene expression ("gambar/episode1/225.webp") with dissolve
            patricia "Maksudku, aku bosan membicarakan pelacurmu!"
            toby "Itu saja ... Anda akan mendapatkannya untuk itu!"

    scene expression ("gambar/episode1/226.webp") with dissolve
    patricia "Membantu!"
    toby "Tidak ada orang di sini kecuali kami!"
    patricia "Dia mencoba memperkosa saya!"
    scene expression ("gambar/episode1/227_1.webp") with dissolve
    toby "Apakah kamu gila!? Bagaimana jika seseorang mendengar Anda?"
    scene expression ("gambar/episode1/227_2.webp") with dissolve
    patricia "Saya pikir Anda mengatakan bahwa tidak ada orang di sini!"
    scene expression ("gambar/episode1/228.webp") with dissolve
    toby "Banyak ayam?"
    scene expression ("gambar/episode1/229.webp") with dissolve
    patricia "Aaaa!"
    scene expression ("gambar/episode1/230.webp") with dissolve
    toby "Jadi? Mari kita dengar. Apakah ada sesuatu yang ingin Anda katakan?"
    scene expression ("gambar/episode1/231.webp") with dissolve
    patricia "Apa yang akan kamu lakukan padaku sekarang?"
    scene expression ("gambar/episode1/232.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Sial cara dia menatapku membuatku sangat terangsang dan sekarang aku punya kesalahan! {6}"
    scene expression ("gambar/episode1/233.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Dia memperhatikan. Sial, bercinta, persetan dengan hidupku. {6}"
    if patricia_rel == 3:
        scene expression ("gambar/episode1/234.webp") with dissolve
        patricia "Apakah Anda tertarik kepada saya bahwa Anda mendapat boner hanya dari saya bertingkah tak berdaya?"
        toby "TIDAK!"
        scene expression ("gambar/episode1/235.webp") with dissolve
        patricia "Ya Tuhan ... ini sangat lucu! Haha, pengisap!"
        scene expression ("gambar/episode1/237.webp") with dissolve
        patricia "Malam ini, Anda sedang tidur di lantai, Anda tanduk anjing!"
    else:
        scene expression ("gambar/episode1/236.webp") with dissolve
        patricia "Ewww. Ada apa denganmu? Saya [9] Anda!"
        toby "Maaf, itu bukan karena Anda!"
        patricia "Saya tidak peduli, lepas dari saya!"
        scene expression ("gambar/episode1/238.webp") with dissolve
        patricia "Malam ini Anda sedang tidur di lantai."
    scene expression ("gambar/episode1/239.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Benar-benar? Apakah Anda akan melakukan saya seperti itu? {6}"
    scene expression ("gambar/episode1/240.webp") with long_dissolve
    toby "Apakah Anda membutuhkan bantuan dengan itu?"
    $ progress = 16
    if charlotte_rel < 2:
        charlotte "Jangan khawatir. Saya bisa melakukannya sendiri!"
        toby "Mau mu!"
        pass
    else:

        scene expression ("gambar/episode1/241.webp") with dissolve
        charlotte "Bagaimana saya bisa mengatakan tidak kepada Anda?"
        scene expression ("gambar/episode1/242.webp") with dissolve
        toby "Ingin beberapa juga setelahnya?"
        scene expression ("gambar/episode1/243.webp") with dissolve
        patricia "{4} {3} * Whispering * {1} {5} {2}
Anda terlalu terangsang sekarang. Mungkin di waktu lain. {6}"
        scene expression ("images/episode1/244.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("gambar/episode1/245.webp") with dissolve
        charlotte "Apa yang dia katakan?"
        toby "Sesuatu seperti dia tidak pantas mendapatkan tabir surya karena dia kalah di bola voli!"
        scene expression ("gambar/episode1/246.webp") with dissolve
        if ep1_let_patricia_win == True:
            patricia "Idiot."
        else:
            patricia "Saya mengatakan bahwa saya bahkan tidak pantas pulang dengan Anda dengan mobil yang sama."
            toby "Jangan khawatir, saya akan menutup mata kali ini!"

        label memory_02:

            if _in_replay:

                $ ep1_get_charlotte_drunk=True

            scene expression ("gambar/episode1/247.webp") with dissolve
            charlotte "Jika tak satu pun dari kedua wanita itu mempekerjakan Anda, saya pikir Anda akan melakukannya dengan cukup baik sebagai tukang pijat."
            toby "Dan saya hanya menerapkan tabir surya. Bayangkan jika saya benar -benar memberi Anda pijatan."
            scene expression ("gambar/episode1/248.webp") with dissolve
            charlotte "Nah, karena kami bangkrut, saya pikir saya akan membiarkan Anda memijat saya suatu hari nanti."
            toby "Apakah punggung Anda masih sakit?"
            charlotte "Terkadang, setelah berdiri terlalu banyak."
            if ep1_get_charlotte_drunk == False:
                scene expression ("gambar/episode1/249.webp") with dissolve
                charlotte "Terima kasih atas tabir surya!"
                toby "Tidak ada masalah [2]."
            else:
                scene expression ("gambar/episode1/250.webp") with dissolve
                toby "{4} {3} * Thinking * {1} {5} {2}
Apa yang [2] lakukan? {6}"
                charlotte "Saya tidak ingin garis tan!"
                scene expression ("gambar/episode1/251.webp") with dissolve
                toby "Ya, tentu saja [2]!"
                scene expression ("gambar/episode1/252.webp") with dissolve
                charlotte "{4} {3} * Whispering * {1} {5} {2}
Pastikan Anda tidak ketinggalan tempat! {6}"
                scene expression ("gambar/episode1/253.webp") with dissolve
                toby "{4} {3} * Thinking * {1} {5} {2}
Apakah dia serius sekarang? {6}"
                toby "{4} {3} * Thinking * {1} {5} {2}
Pantatnya sangat besar! {6}"
                scene expression ("gambar/episode1/254.webp") with dissolve
                charlotte "{4} {3} * Whispering * {1} {5} {2}
Anak baik. {6}"
                toby "{4} {3} * Thinking * {1} {5} {2}
Saya tidak yakin apa yang ada di dalam koktail itu, tapi saya pikir sangat kuat. {6}"
                scene expression ("gambar/episode1/255.webp") with dissolve
                toby "{4} {3} * Thinking * {1} {5} {2}
Saya merasa agak kotor dan terangsang pada saat yang sama. Saya menyentuh pantat perusahaan saya [2]. {6}"
                toby "{4} {3} * Thinking * {1} {5} {2}
Ini bukan yang saya pikir akan terjadi di pantai. {6}"
                menu:
                    "{2} [14] maju {6}"(csq="Charlotte +1 & Galeri Gambar"):
                        $ charlotte_rel += 1
                        $ ep1_groping_charlotte = True
                        $ unlockImage(persistent.charlotte_03)
                        scene expression ("gambar/episode1/256.webp") with dissolve
                        toby "{4} {3} * Thinking * {1} {5} {2}
Apa -apaan ... Anda hanya hidup sekali. {6}"
                        scene expression ("gambar/episode1/257.webp") with dissolve
                        toby "{4} {3} * Thinking * {1} {5} {2}
Saya menyentuh payudara [2] saya! {6}"
                        toby "{4} {3} * Thinking * {1} {5} {2}
Dan sepertinya dia tidak terganggu oleh itu. {6}"
                        scene expression ("gambar/episode1/258.webp") with dissolve
                        toby "{4} {3} * Thinking * {1} {5} {2}
Oke ... saya tahu kemana perginya. {6}"
                        scene expression ("gambar/episode1/259.webp") with dissolve
                        toby "{4} {3} * Thinking * {1} {5} {2}
Saya tidak percaya seberapa besar dan lunak payudaranya. {6}"
                        charlotte "{4} {3} * mengerang sedikit * {1} {5}
{2} mhmmm. {6}"
                        scene expression ("gambar/episode1/260.webp") with dissolve
                        toby "{4} {3} * Thinking * {1} {5} {2}
Saya harus berhenti sebelum Tris berbalik. {6}"
                    "{2} stop {6}" if not _in_replay:
                        pass
                scene expression ("gambar/episode1/261.webp") with dissolve
                charlotte "Terima kasih sayang!"
                toby "Tidak ada masalah [2]."
                $ unlockMemory(persistent.memory_02)

            $ renpy.end_replay()

    scene expression ("gambar/episode1/262.webp") with dissolve
    toby "{4} {3} * Thinking * {1} {5} {2}
Hari yang luar biasa. Saya merasa kota ini memiliki dampak besar pada saya. {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Ngomong -ngomong, saya bertanya -tanya pekerjaan mana yang harus saya pilih besok. {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Di satu sisi memiliki penghasilan yang lebih stabil akan menjadi hebat dan di atas itu saya akan memiliki karier. {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Tapi kata -kata Katrina terus muncul di kepalaku. Dia berjanji kepada saya banyak uang. Tapi berapa biayanya? {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Maksudku, lihat [13], ketika bisnisnya baik dia berperilaku berbeda dari sekarang. Jadi aman untuk mengatakan bahwa pekerjaan saya akan berdampak pada attiude saya. {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Bagaimana jika setelah menghabiskan begitu banyak waktu di klub, dengan pelacur dan wanita mabuk saya akan mulai memperlakukan gadis -gadis di rumah dengan cara yang sama atau bahkan Emma. {6}"
    toby "{4} {3} * Thinking * {1} {5} {2}
Saya tidak yakin apa yang harus dipilih. Maksud saya, kedua pekerjaan itu terlihat cukup menjanjikan. Saya akan mengetahuinya besok. {6}"
    $ progress = 17
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
