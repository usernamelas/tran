label eveningtv_elaine:
    play sound "sounds/doorbell.wav"
    m "Hmm siapa itu saat ini?"
    stop sound
    if mrob == 3 and gnight >=4 and day ==2:
        scene etv_er with fade
        m "Oh hai elaine"
        m "Hi Rob"
        e "Rob bertanya apakah dia bisa datang, itu hari liburnya"
        e "Saya harap kami tidak mengganggu Anda"
        e "Mungkin Anda akan tidur"
        m "Tidak, tidak sama sekali, kami biasanya menonton TV saat ini"
        e "Bagus"
        m "Saya akan segera kembali"
        e "Tidak perlu berubah"
        m "Saya tidak bisa tetap seperti itu"
        scene etv_e2r with fade
        e "Bagaimana kabarmu [bname]?"
        b "Aku baik-baik saja"
        scene etv_e3r with dissolve
        m "Apa yang ingin Anda minum Elaine?"
        e "Sama seperti Anda"
        m "Dan Rob?"
        r "Apapun yang Anda minum"
        scene etv_e8r with fade
        e "Anda terlihat bagus [bname]"
        b "Thanks"
        b "Kamu juga"
        scene etv_e4r with dissolve
        m "Cheers"
        b "{i} (hmm orang ini melihat payudaranya) {/i}"
        scene etv_e5r with dissolve
        e "Jadi bagaimana pergeseran Anda?"
        scene etv_e6r with dissolve
        m "Tidak buruk kecuali orang mabuk yang biasa"
        e "Ya selalu seperti itu"
        scene etv_e5r with dissolve
        e "Dan apakah mereka menyebutkan kepada Anda tentang gaun kelinci baru itu"
        m "Jangan ingatkan saya tentang hal itu"
        e "Saya pikir Anda tidak akan menyukainya"
        m "Saya mengumpulkannya dan menyimpannya di laci"
        m "Tidak akan memakainya"
        e "Oh kamu memilikinya di sini?"
        m "Yes"
        e "Bisakah saya mencobanya?"
        m "Ya, mari kita pergi ke kamar saya"
        scene etv_e7r with fade
        "..."
        menu:
            "[bname] akan mencoba menjual [mname] (NTR)":
                b "{i} (mungkin saya bisa menghasilkan uang) {/i}"
                b "Lihat, aku melihatmu menonton payudaranya"
                r "Apa yang kamu bicarakan?"
                b "Saya tahu bahwa Anda menyukainya ..."
                b "Dan saya bisa membuatnya mudah untuk Anda"
                r "..."
                b "Untuk harga yang tepat tentu saja"
                r "{i} (apakah idiot ini mencoba mengatur saya) {/i}"
                r "{i} (jika dia melakukan itu, dia memberatkan dirinya sendiri) {/i}"
                r "Katakanlah saya menerima"
                r "Berapa harganya?"
                b "$ 2000"
                r "Oke, dan bagaimana Anda akan membuatnya?"
                b "Tinggalkan untukku"
                r "Dan di mana kita melakukannya?"
                b "Di sini hanya bersantai, dan dia akan menjadi milikmu, aku akan membaliknya"
                r "Dan bagaimana dengan Elaine?"
                b "Aku akan membawanya pergi"
                r "Ok deal"
                b "Uang dulu"
                r "Anda harus bercanda"
                b "50 persen sekarang 50 persen pengiriman"
                e "We're back"
                scene etv_e9r with dissolve
                e "Aku melihatmu dan Rob bersantai"
                b "Ya dia keren"
                b "Bisakah saya minum sendiri?"
                m "Ya dan tuang lagi untuk kita"
                if strongdrinksforgirlnight ==3:
                    $ robmvisit += 1
                    scene girlnight3a with dissolve
                    b "{i} (i \ 'll Gunakan minuman keras khusus ini untuknya dan elaine) {/i}"
                    b "{i} (Saya perlu memastikan untuk memasukkan minuman normal untuk saya dan merampok kacamata yang sama) {/i}"
                    scene etv_e10r with fade
                    m "Mengapa ini berbeda [bname]?"
                    b "Ini baru saya pikir membiarkan Anda mencobanya"
                    scene black
                    "Setelah beberapa waktu"
                    scene etv_e11r with fade
                    e "Hahaha ini lucu"
                    e "Ya Tuhan ..."
                    scene etv_e12r with dissolve
                    e "Saya perlu menggunakan kamar mandi"
                    scene etv_e13r with dissolve
                    b "Dia milikmu, aku akan terus mengunci Elaine"
                    scene etv_e14r with dissolve
                    b "{i} (sialan aku lupa tentang [sname]) {/i}"
                    scene etv_e15r with dissolve
                    m "Mhhm"
                    scene etv_e16r with dissolve
                    m "..."
                    scene etv_e17r with dissolve
                    m "Wow"
                    scene etv_e18r with dissolve
                    "..."
                    scene etv_e19r with dissolve
                    "..."
                    scene black
                    "SEMENTARA ITU"
                    scene etv_e20r with fade
                    b "Apa yang sedang kamu lakukan?"
                    s "Bagaimana menurutmu?"
                    s "Mencoba tidur"
                    b "Mari kita lakukan pemotretan untuk Anda dan Elaine"
                    s "Tidak mood"
                    b "Ayo!"
                    s "[bname] Sudah kubilang aku tidak mau"
                    menu:
                        "Menerima":
                            b "{i} (Saya perlu mengambil elaine) {/i}"
                            b "{i} (mungkin ke toilet) {/i}"
                            scene black
                            "..."
                            scene bel
                            e "..."
                            "..."
                            e "Ahh"
                            e "[bname] yes"
                            pass
                        "Bayar dia":

                            b "Aku akan membayarmu untuk itu"
                            s "Berapa harganya?"
                            b "500"
                            $ mny -= 500
                            s "Ok"
                            s "Let's start"
                            b "Lepaskan pakaian Anda"
                            scene etv_e21r with dissolve
                            b "Aku serius, ayo"
                            b "Elaine Lepaskan gaun Anda"
                            scene etv_e22r with fade
                            b "Berlutut Elaine"
                            scene etv_e23r with dissolve
                            "..."
                            scene etv_e24r with dissolve
                            b "Wow"
                            s "Ah"
                            scene etv_e25r with dissolve
                            b "Yeah more"
                            pass
                    scene black
                    "SEMENTARA ITU"
                    scene etv_e26r with fade
                    m "Ahh"
                    scene robm with dissolve
                    $ persistent.unlock_73 = True
                    m "Oh"
                    "..."
                    m "God"
                    "..."
                    m "Ahhh"
                    "..."
                    scene etv_e27r with fade
                    e "Ok saya akan pergi sekarang"
                    b "No wait"
                    b "[sname] Bisakah Anda menjaganya selama satu menit, saya akan kembali"
                    scene etv_e28r with dissolve
                    s "Hmm"
                    scene etv_e29r with fade
                    b "Cepat, Anda harus menyelesaikannya"
                    scene etv_e30r with dissolve
                    b "Selesai saya perlu membawanya pergi"
                    r "Ok"
                    scene etv_e31r with dissolve
                    s "Huh"
                    scene etv_e32r with fade
                    b "Let's go"
                    scene etv_e33r with dissolve
                    e "Dimana [mname]?"
                    r "Saya pikir dia bersamamu"
                    r "Let \'s Go?"
                    $ mny += 2000
                    $ renpy.notify (_("You received 2000 $"))
                    $ renpy.pause ( 5, 0)
                    scene etv_e34r with dissolve
                    s "Anda tercela"
                    b "Apa?"
                    b "Mengapa?"
                    s "..."
                    b "{i} (persetan, aku akan tidur) {/i}"
                    jump newdays
                else:





                    b "{i} (sialan, bagaimana jika dia tidak mabuk) {/i}"
                    b "{i} (Saya harus mendapatkan minuman keras untuk waktu berikutnya) {/i}"
                    scene etv_e4r with fade
                    m "Cheers"
                    scene etv_e35r with dissolve
                    "..."
                    b "{i} (tampaknya mereka tidak akan mabuk) {/i}"
                    scene etv_e36r with dissolve
                    b "{i} (i \ 'll go lihat apa [sname] terserah) {/i}"
                    scene etv_e37r with fade
                    b "Apa yang sedang kamu lakukan?"
                    s "Apa yang kamu lihat?"
                    b "Mari bersenang -senang"
                    s "Apa?"
                    b "Mari kita melakukan sesuatu yang saya maksud"
                    s "Tinggalkan aku sendiri [bname]"
                    b "Apa -apaan, kenapa kamu menyebalkan?"
                    s "Pergi!"
                    b "Fuck it"
                    scene etv_e38r with fade
                    b "Mereka pergi?"
                    m "Yes"
                    b "Apakah Anda ingin saya memberikan pijatan?"
                    m "Tidak, terima kasih, saya akan tidur"
                    b "{i} (sialan, tidak ada yang mau menghibur saya hari ini) {/i}"
                    b "{i} (Saya kira saya akan tidur) {/i}"
                    jump newdays
            "[bname] akan diam":


                "..."
                e "We're back"
                scene etv_e9r with dissolve
                e "Aku melihatmu dan Rob bersantai"
                b "Ya dia keren"
                scene etv_e35r with dissolve
                "..."
                b "{i}(Boring){/i}"
                scene etv_e36r with dissolve
                b "{i} (i \ 'll go lihat apa [sname] terserah) {/i}"
                scene etv_e37r with fade
                b "Apa yang sedang kamu lakukan?"
                s "Apa yang kamu lihat?"
                b "Mari bersenang -senang"
                s "Apa?"
                b "Mari kita melakukan sesuatu yang saya maksud"
                s "Tinggalkan aku sendiri [bname]"
                b "Apa -apaan, kenapa kamu menyebalkan?"
                s "Pergi!"
                b "Fuck it"
                scene etv_e38r with fade
                b "Mereka pergi?"
                m "Yes"
                b "Apakah Anda ingin saya memberikan pijatan?"
                m "Tidak, terima kasih, saya akan tidur"
                b "{i} (sialan, tidak ada yang mau menghibur saya hari ini) {/i}"
                b "{i} (Saya kira saya akan tidur) {/i}"
                jump newdays
    else:

        pass
    scene etv_e with fade
    m "Oh hai elaine"
    e "Hi [mname]"
    e "Saya telah datang mengunjungi Anda"
    e "Apakah Anda keberatan jika saya menghabiskan waktu?"
    m "Oh tidak tentu saja tidak"
    scene etv_e1 with dissolve
    e "Saya harap saya tidak mengganggu Anda"
    e "Mungkin Anda akan tidur"
    m "Tidak, tidak sama sekali, kami biasanya menonton TV saat ini"
    e "Bagus"
    m "Saya akan segera kembali"
    scene etv_e2 with fade
    e "Bagaimana kabarmu [bname]?"
    b "Saya baik -baik saja, dan Anda?"
    scene etv_e3 with dissolve
    m "Apa yang ingin Anda minum Elaine?"
    e "Sama seperti Anda"
    if elaineagain >= 3:
        jump girlsnight


        jump girlsnight
    else:
        pass
    menu:
        "Tetap bersama mereka":
            pass
        "Tinggalkan mereka sendiri":
            jump sname_elainetv

    scene etv_e4 with fade
    e "Jadi? Bagaimana perasaan Anda di tempat kerja?"
    m "It's OK"
    e "Apa maksudmu oke?"
    e "Apakah Anda terbiasa?"
    m "Not so"
    e "Tapi saya melihat sebaliknya"
    scene etv_e5 with dissolve
    m "Apa maksudmu?"
    e "Saya dapat melihat Anda berjalan -jalan dengan piyama dan dalih Anda"
    e "Berlatih lebih sedikit pakaian?"
    b "{i}(Haha){/i}"
    scene etv_e6 with dissolve
    "..."
    scene etv_e5 with dissolve
    m "Saya selalu memakai ini?"
    e "Lalu itu bagus"
    e "Anda telah menyingkirkan kompleks Anda"
    m "..."
    scene etv_e7 with dissolve
    e "Bisakah saya mendapatkan segelas anggur lagi?"
    scene etv_e8 with dissolve
    "..."
    scene etv_e4 with fade
    e "Cheers for Your Complex"
    m "Cheers"
    e "Saya sangat senang Anda menjadi lebih baik"
    e "Saya berharap ini akan hilang sepenuhnya"
    m "Mari kita menonton TV"
    e "Saya datang untuk melihat Anda, bukan menonton TV"
    m "Dan saya tidak ingin melanjutkan topik ini"
    scene etv_e9 with dissolve
    e "Apa hal yang membosankan ini?"
    b "Yeah"
    e "Berikan padaku, izinkan saya menemukan sesuatu yang lebih baik"
    scene etv_e11 with dissolve
    e "Ini jauh lebih baik"
    scene etv_e10 with dissolve
    m "Elaine !!"
    scene etv_e5 with dissolve
    m "Tolong matikan"
    e "Ok mari kita kembali ke topik kita"
    m "..."
    e "Seberapa jauh Anda melangkah dengan dorongan kepercayaan diri Anda?"
    scene etv_e6 with dissolve
    "..."
    scene etv_e5 with dissolve
    m "Apakah kita harus melakukan ini sekarang?"
    e "Saya tidak tahu mengapa tidak?"
    scene etv_e6 with dissolve
    if mrel >=100:
        "..."
        m "[bname] Bisakah Anda meninggalkan kami sendiri"
        b "Err"
        b "Saya ingin menonton TV jika Anda tidak keberatan"
        m "Mhmm"
        m "OK"
        e "Jadi?"
        scene etv_e5 with dissolve
        m "Saya tidak tahu apakah saya bisa mengatasi ini"
        m "Saya tidak bisa memakai hal -hal seperti itu di tempat kerja, itu adalah skandal jika seseorang melihat saya di sana"
        if etvelaine ==0:
            scene etv_e4 with fade
            e "Jangan khawatir tentang itu"
            e "Ini akan menjadi lebih baik seiring waktu"
            e "Bersorak untuk itu"
            $ etvelaine = 1
            m "Cheers"
            "..."
            e "Mungkin ini saat yang tepat untuk berlatih"
            m "Ayo Elaine!"
            e "Mengapa tidak?"
            e "Pergi memakai sesuatu"
            e "Dan lakukan beberapa gerakan tarian, peasy mudah"
            e "Anda hampir tidak mengenakan apa -apa"
            scene etv_e6 with dissolve
            m "No"
            e "Saya akan melakukannya"
            scene etv_e21 with dissolve
            m "Anda keluar dari pikiran Anda"
            scene etv_e22 with dissolve
            e "Tadaa!"
            m "Apa!!"
            scene etv_e23 with dissolve
            m "ELAINE! Apa ini?"
            e "Apa? Saya selalu melakukan latihan jenis ini dengan Rob"
            m "Jangan lupakan apa itu Rob dan apa itu [bname] bagi saya"
            m "Kembalikan gaun Anda"
            e "Sungguh karen!"
            scene etv_e4 with fade
            "..."
            "Setelah beberapa waktu"
            scene etv_e18 with fade
            e "Selamat malam"
            m "Selamat malam Elaine"
            scene etv_e20 with dissolve
            m "Aku akan tidur"
            m "Selamat malam sayang"
            b "Selamat malam"
            b "{i} (Saya kira saya akan tidur juga) {/i}"
            jump newdays

        elif etvelaine ==1:
            e "Saya punya ide"
            "Dia berbisik"
            m "..."
            e "Mengapa Anda tidak menempatkan ini dan menunjukkan kepada kami"
            scene etv_e14 with dissolve
            "..."
            scene etv_e5 with dissolve
            m "Sekarang?"
            e "Ya coba itu"
            e "Pertama, itu membuat Anda merasa lebih baik tentang diri sendiri dan membantu Anda mengatasi masalah Anda ini"
            m "Aku tidak tahu..."
            e "Anda sudah memakai ini"
            e "Periksa apa yang baru saja saya berikan kepada Anda, itu tidak jauh berbeda"
            scene etv_e12 with dissolve
            e "Lihat dan kemudian putuskan"
            "..."
            scene etv_e13 with dissolve
            m "Ok saya akan kembali"
            scene etv_e15 with fade
            e "Hmm bagus"
            e "Biarkan saya melihat bagaimana tampilannya dari belakang?"
            scene etv_e16 with dissolve
            "..."
            b "{i}(Hmmm){/i}"
            e "Bagus"
            e "Tapi tidak sebagus pertunjukan saya"
            e "Tolong beri kami lebih banyak anggur"
            scene etv_e17 with fade
            e "Cheers"
            "..."
            e "Tidak, giliran saya untuk menunjukkan kepada Anda"
            scene etv_e24 with fade
            "..."
            scene etv_e25 with dissolve
            e "Tadaa!"
            m "Hai!"
            scene etv_e26 with dissolve
            m "ELAINE! Apa ini?"
            m "Kembalikan gaun Anda"
            e "Ayo! Jangan menjadi Karen bergabung dengan saya untuk beberapa latihan"
            scene etv_e27 with dissolve
            e "Apa yang kamu katakan?"
            b "Err"
            m "Meninggalkan Steve dari ini"
            scene etv_e28 with dissolve
            b "{i} (huh steve! Siapa steve?) {/i}"
            e "Apa pun!"
            m "Pakai pakaian Anda"
            e "Dapatkan kami minuman terlebih dahulu"
            scene etv_e17 with fade
            "..."
            scene black
            "Setelah beberapa waktu"
            scene etv_e18 with fade
            e "Selamat malam"
            m "Selamat malam Elaine"
            m "Bagaimana dengan gaun itu?"
            e "Keep it"
            scene etv_e19 with dissolve
            m "Aku akan tidur"
            m "Selamat malam sayang"
            b "Selamat malam"
            b "{i} (...) {/i}"
            scene etv_e29 with dissolve
            e "[bname] Bawa dia ke kamarnya"
            e "Aku akan di sini untuk memastikan dia baik -baik saja"
            b "Aha! OKE"
            scene etv_e30 with fade
            m "Tidur di sini Stewart"
            b "Hehehe"
            b "Saya tidak bisa ..."
            menu:
                "Pergi ke Elaine":
                    m "Ayo Stewart"
                    m "I miss Steve"
                    b "{i} (sialan!) {/i}"
                    b "Aku ... aku lelah"
                    b "Aku akan kembali"
                    scene etv_e39 with fade
                    b "Fiuh!"
                    e "Anda menidurkannya?"
                    b "Not fully"
                    e "Jadi ... aku ... ingin bertanya padamu"
                    e "Tentang kemajuan Anda?"
                    b "Tidak begitu bagus, tapi mari kita bicara di kamarku"
                    b "It's safer"
                    b "Saya takut [mname] akan mengikuti saya"
                    scene etv_e40 with fade
                    "..."
                    b "Bukan kemajuan yang bagus"
                    b "Dia benar -benar pemalu"
                    b "Saya butuh lebih banyak bantuan"
                    e "I'll try"
                    e "Selamat malam untuk saat ini"
                    b "Err wait"
                    e "Apa?"
                    b "Mungkin Anda juga bisa memberi saya kepercayaan diri"
                    e "Keyakinan macam apa?"
                    b "Mungkin membantu dengan berciuman?"
                    e "Saya tidak bisa melakukan itu [bname]"
                    b "Please"
                    e "Hanya yang cepat"
                    b "Ok saya janji"
                    scene etv_e41 with dissolve
                    "..."
                    b "Bisakah Anda melepas gaun itu?"
                    scene etv_e42 with dissolve
                    e "..."
                    e "Saya tidak menanggalkan pakaian gratis"
                    b "Tapi Anda baru saja melakukannya sebelumnya"
                    e "Itu hanya untuk meningkatkan kepercayaan [mname]"
                    b "Ok berapa harganya?"
                    e "0 Diskon untuk Anda"
                    b "Hmm"
                    if mny >=50:
                        b "Di Sini..."
                        $ mny -= 50
                        scene etv_e43 with fade
                        b "Mmmm"
                        scene etv_e44 with dissolve
                        "..."
                        scene etv_e45 with dissolve
                        if sbm ==2 and bcaught_s == 0:
                            scene etv_c0 with fade
                            s "{i} (huh! Suara apa itu berasal dari kamar [bname] \!?) {/i}"
                            scene etv_c with dissolve
                            s "{i} (aha!) {/i}"
                            $ bcaught_s = 1
                            s "{i} (di mana ponsel saya) {/i}"
                            scene etv_cbw with dissolve
                            s "{i} (yess !!) {/i}"
                            scene etv_e45 with dissolve
                            e "[bname]"
                            scene etv_e46 with dissolve
                            e "Cukup, saya harus pergi"
                            b "..."
                            e "Saya akan terlambat"
                            scene etv_e40 with fade
                            e "Tidak aman melakukan ini di sini"
                            e "Selamat malam"
                            b "Ok selamat malam"
                            e "Selamat malam [bname]"
                            scene broom_night with fade
                            b "{i} (i \ 'll pergi tidur) {/i}"
                            "Itu semua dalam opsi ini"
                            "Tunggu [sname] untuk melawan kekuatan di kamarnya @11: 00 dan saat mengambil beberapa foto"
                            jump newdays
                        else:

                            e "[bname]"
                            e "Cukup, saya harus pergi"
                            b "..."
                            e "Saya akan terlambat"
                            scene etv_e40 with fade
                            e "Tidak aman melakukan ini di sini"
                            e "Selamat malam"
                            b "Ok selamat malam"
                            e "Selamat malam [bname]"
                            scene broom_night with fade
                            b "{i} (i \ 'll pergi tidur) {/i}"
                            "..."
                            jump newdays
                    else:

                        b "Sial, aku tidak punya"
                        e "Selamat malam [bname]"
                        scene broom_night with fade
                        b "{i} (persetan, aku akan tidur) {/i}"
                        jump newdays


                "Tetap di sini" if mrel>=100:
                    scene etv_e31 with dissolve
                    m "Ayo Stewart"
                    m "Saya merindukan Steve"
                    b "{i} (sialan!) {/i}"
                    scene etv_e32 with dissolve
                    "..."
                    m "Masukkan ke dalam"
                    b "Letakkan apa?"
                    scene etv_e33 with dissolve
                    m "Steve"
                    b "Tentu saja sayang"
                    b "{i} (hehe dia memanggil penisnya steve) {/i}"
                    b "{i} (akhirnya aku bisa merasakan vagina itu) {/i}"
                    m "Ayo, bawakan aku hamil Stewart"
                    b "{i} (bercinta hamil, saya belum memikirkannya) {/i}"
                    b "{i} (Pikirkan alasan [bname] ...) {/i}"
                    menu:
                        "Mengizinkan":
                            b "Saya tidak bisa ..."
                            b "... Aku lelah"
                            pass
                        "Makan dia":

                            b "Hmmm"
                            scene etv_e65 with dissolve
                            m "Huh"
                            scene etv_e66 with dissolve
                            m "Ahhh"
                            scene etv_e67 with dissolve
                            "..."
                            scene etv_e68 with dissolve
                            m "Ahhh Steve!"
                            m "Fuck me"
                            b "Saya tidak bisa ..."
                            b "... Aku lelah"
                            pass

                    scene etv_e34 with hpunch
                    m "Mari kita lihat apakah Anda"
                    scene etv_e35 with dissolve
                    b "Ahhh!"
                    if mrel>=200:
                        scene etv_e35a with dissolve
                        b "Ughh"
                        scene etv_e35b with dissolve
                        b "{i}(Focus [bname]){/i}"
                        if mrel>=300:
                            scene etv_e34 with dissolve
                            m "Siap memberikannya padaku?"
                            scene etv_e69 with fade
                            m "..."
                            scene etv_e70 with dissolve
                            m "Ya akhirnya penis yang bagus"
                            scene etv_e71 with dissolve
                            m "Ahhh"
                            scene etv_e72 with dissolve
                            m "..."
                            scene etv_e73 with dissolve
                            m "Yess baby"
                            scene etv_e74 with dissolve
                            b "{i} (dia sangat basah, apakah dia cum!?) {/i}"
                            scene etv_e75 with dissolve
                            "..."
                            m "Apakah Anda selesai?"
                            b "TIDAK..."
                            scene etv_e76 with fade
                            b "{i} (oh elaine sial, saya lupa tentang dia) {/i}"
                            scene etv_e77 with fade
                            m "Seh! Di mana?"
                            b "Harus pergi"
                            m "Di mana?"
                            b "Aku akan kembali"
                            b "{i} (semoga dia tidak mengikuti saya) {/i}"
                            scene hall_n with fade
                            b "Persetan!"
                            b "Dia pergi"
                            b "Aku lebih baik tidur"
                            b "Atau mungkin saya bisa melihat apa dengan [mname]"
                            call screen etvnav
                        else:

                            pass
                    else:

                        pass
                    scene etv_e36 with vpunch
                    "..."
                    b "Sungguh!"
                    scene etv_e37 with dissolve
                    b "{i} (oh elaine sial, saya lupa tentang dia) {/i}"
                    scene etv_e38 with fade
                    m "Seh! Di mana?"
                    b "Harus pergi"
                    m "Di mana?"
                    b "Aku akan kembali"
                    b "{i} (semoga dia tidak mengikuti saya) {/i}"
                    scene hall_n with fade
                    b "Persetan!"
                    b "Dia pergi"
                    b "Aku lebih baik tidur"
                    b "Atau mungkin saya bisa melihat apa dengan [mname]"
                    call screen etvnav
    else:


        "..."
        m "[bname] Bisakah Anda meninggalkan kami sendiri"
        b "Err"
        b "Saya ingin menonton TV jika Anda tidak keberatan"
        m "Saya meminta Anda untuk pergi"
        m "Jadi ... tolong lakukan"
        b "Ok baik -baik saja"
        b "{i} (sialan saya perlu meningkatkan poin hubungan saya ke 100) {/i}"
        b "{i} (kurasa aku akan tidur sekarang) {/i}"
        jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc