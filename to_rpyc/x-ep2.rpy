label ep2:

    scene 234 with fade
    play music city fadein 1.5 volume 0.5
    v "Saya suka kota ini, toko -toko, bangunan, semuanya."
    v "Saya sudah lama ingin datang ke butik ini."
    scene 231
    mc "Saya tahu, Anda terus memberi tahu saya, haha."
    mc "Saya berjanji kepada Anda bahwa dalam satu atau dua tahun kita akan tinggal di kota ini."
    scene 232
    v "Aku akan memelukmu."
    mc "Saya tahu Anda akan melakukannya."
    scene 230
    mc "Jadi ... tempat ini pasti memiliki pakaian luar biasa untuk Anda terus mengganggu saya untuk membawa Anda ke sini selama ini."
    v "Semua teman saya mengatakan mereka memiliki pakaian terbaik di kota dan saya mempercayai mereka."
    mc "Ya pasti ..."
    scene 231
    mc "Saya yakin mereka juga memiliki harga tertinggi di kota."
    v "Haha, mungkin."
    v "Untung suamiku yang tercinta membayar untukku."
    mc "Oh, apakah saya?"
    v "Tentu saja Anda. Saya tahu betapa Anda ingin melihat saya cantik."
    scene 232
    mc "Anda selalu terlihat cantik, sayang."
    v "Miliknya, itu lucu."
    v "Anda masih membayar tho."
    scene 233
    mc "HMPT ..."
    mc "Baiklah."
    scene 232
    mc "Karena itu masalahnya, saya pikir saya harus memilih pakaian Anda saat itu."
    v "Cukup adil. Ayo masuk ke dalam."
    scene blackscreen
    stop music fadeout 1.0
    pause 1.0
    scene 235
    play music boutiquemusic fadein 1.0 volume 0.1
    play sound publicbathroom loop volume 0.1
    mct "Saya kira itu bukan ide terbaik ..."
    mct "[violet] mengambil selamanya di sana."
    scene 236
    mc "Hei sayang, apakah kamu akan berada di sana sepanjang hari?"
    mc "Saya bosan sekali di sini."
    scene 237
    v "Maaf sayang. Ada terlalu banyak yang bagus, saya tidak tahu mana yang harus dipilih."
    scene 236
    mc "Semua yang Anda coba sejauh ini bagus, cukup pilih salah satu dari mereka."
    scene 237
    v "Bukan itu cara kerjanya."
    v "Saya masih ingin mencoba lebih banyak pakaian."
    v "Dan Anda bilang Anda akan membantu saya memilih."
    scene 235
    mc "Bagus..."
    play audio curtainopen volume 0.2 fadeout 1.0
    scene 239
    play sound publicbathroom loop volume 0.1
    v "Hei, saya yakin Anda akan menyukai yang berikutnya."
    mc "Saya yakin saya akan ..."
    v "Saya akan mencoba pakaian dalam."
    scene 240
    mc "Baiklah! Sekarang kita sedang berbicara!"
    mc "Luangkan semua waktu yang Anda butuhkan!"
    scene 241
    v "Anda sangat mudah diprediksi."
    scene 242
    mc "Apa yang bisa saya katakan, saya pria sederhana."
    scene 246
    mct "Bersenandung? Dia lupa menutup tirai sepenuhnya."
    mct "Saya pikir saya harus menutupnya ..."
    scene 238
    mct "Sebenarnya, tidak ada orang lain di sini."
    scene 244
    mct "Dan saya tidak keberatan dengan pandangan."
    scene 242
    mct "Bung, aku pria paling beruntung yang hidup!"
    mct "[violet] sempurna!"
    mct "Tahun pernikahan pertama ini adalah yang terbaik dalam hidup saya."
    mct "Aku sangat mencintainya."
    scene 244
    mct "Cermin itu ditempatkan dengan sempurna."
    mct "Mungkin dia melakukannya dengan sengaja untuk menggodaku."
    mct "Siapa tahu ..."
    scene 248
    play audio disco volume 0.3
    stop music
    mct "HM?"
    scene 247
    play music heartbeatslow volume 0.5
    mct "Apa!? Seseorang akan datang!"
    mct "Jika saya tidak melakukan apa pun, dia pasti akan melihatnya menanggalkan pakaiannya."
    scene 248
    menu:
        "Tutup tirai":
            $ close_the_curtain = "1"
            $ dont_move = "2"
            scene 249
            stop music
            play music tense fadein 2.0 volume 0.2
            mct "Saya perlu menutup ini!"
            mct "Tidak mungkin saya membiarkan pria ini menonton istri saya membuka pakaian."
            play audio curtainopen volume 0.2 fadeout 1.0
            scene 250
            stranger "Pria apa, kenapa kamu melompat di depanku? Saya akan menggunakan yang ini."
            mc "Maaf tapi yang ini sudah ditempati, istri saya ada di sana."
            stranger "Sial, oke ... saya hanya akan menggunakan yang berikutnya."
            scene 251
            mc "Ya, bagus."
            mct "Itu sudah dekat!"
            mct "Saya harus berhati -hati jika saya ingin pindah ke kota ini dengan [Violet] suatu hari nanti."
            mct "Saya tidak bisa melakukan hal -hal semacam itu dan berisiko mengeksposnya seperti itu."
            mct "Saya tidak akan pernah membiarkan ini terjadi lagi."
            if dont_let_him_pee == "1":
                stop music
                stop sound
                play sound endupdate fadein 1.0 volume 0.3
                scene blackscreen with fade
                centered "__Tag_0____tag_1____present day__tag_2____tag_3__"
                pause 0.8
                jump kitchendinner
            if ted_shower == "1":
                stop music
                stop sound
                jump backtoshower
            else:
                stop music
                stop sound
                jump bathroomdoor
        "Jangan bergerak":


            $ dont_move = "1"
            $ close_the_curtain = "2"
            scene 247
            stop music
            stop sound
            play music tense fadein 2.0 volume 0.2
            mct "Saya ... Saya tidak bisa bergerak."
            mct "Apa yang terjadi padaku?"
            mct "[Violet] benar -benar terbuka dan saya tidak bergerak untuk menutup tirai itu."
            scene 252
            mct "Dia pasti akan melihatnya setengah telanjang."
            mct "Saya tidak bisa hanya duduk di sini."
            scene 253
            mct "Mengapa saya tidak bergerak untuk menghentikan ini?"
            mct "Apakah saya benar -benar ingin dia melihatnya seperti ini?"
            mct "Saya tidak bisa berpikir jernih."
            scene 254
            mct "Kotoran! Sudah terlambat sekarang."
            mct "Dia benar -benar bisa melihat refleksinya."
            mct "Dan dia tidak mengerti tentang hal itu."
            scene 255
            mct "Sepertinya dia bahkan tidak melihat saya di sini."
            mct "Dia hanya hipnotyzed olehnya."
            scene 256
            mct "Saya tidak bisa menyalahkannya."
            mct "Dia mengadakan pertunjukan tanpa menyadarinya."
            scene 257
            mct "Dia akan kesal padaku jika dia melihat apa yang terjadi."
            scene 258
            mct "Fakta bahwa saya tidak menghentikan orang ini dari memandangnya saat dia membuka pakaian."
            mct "Atau fakta bahwa saya membiarkan ini masih berlangsung."
            mct "Apakah dia benar -benar tidak melihat tirai terbuka?"
            scene 260
            mct "Bung ini memiliki pandangan hidupnya."
            scene 259
            mct "Saya merasa aneh ... ini membuat saya cemburu."
            mct "Tapi pada saat yang sama merasa terburu -buru ..."
            mct "Campuran antara kecemburuan dan kegembiraan."
            scene 261
            mct "Saya sangat bingung sekarang."
            scene 263
            mct "Sebagian dari diriku hanya ingin bangun dan meninju wajahnya karena melihat istriku."
            scene 261
            mct "Tapi hanya itu, dia hanya melihat. Apa yang dapat saya lakukan untuk menghentikannya?"
            scene 262
            mct "Sekarang saya sedang memikirkannya ..."
            mct "Ini sebenarnya cukup lucu."
            mct "Saya yakin dia berharap dia bisa berbuat lebih banyak, tetapi dia hanya bisa melihat."
            scene 265
            mct "Dia hanya duduk di sana, ngiler di atas tubuhnya."
            mct "Dan hanya itu yang bisa dia lakukan."
            scene 264
            mct "Nikmati selagi Anda bisa saudara."
            mct "Hanya itu yang akan Anda dapatkan."
            scene 266
            mct "Ini tidak jauh berbeda dari bikini."
            mct "Ini seperti semua orang di pantai."
            mct "Hanya membayangkan apa yang ada di bawahnya."
            mct "Tapi mereka hanya bisa membayangkan."
            scene 262
            mct "Saya satu -satunya yang dapat melihat apa yang ada di bawahnya."
            scene 267
            mct "HM?"
            scene 268
            mct "Apa??"
            mct "Apakah dia akan melepas celana dalamnya juga!?"
            scene 269
            mct "Sungguh! Saya ingat sekarang ..."
            mct "Dia bilang dia akan mencoba pakaian dalam."
            scene 270
            mct "Tapi dia ... dia akan melihatnya telanjang."
            mct "Melihatnya dalam bra dan celana dalam adalah satu hal ..."
            scene 271
            mct "Tapi ini ..."
            mct "Ini sudah terlalu jauh."
            menu:
                "Tutup sekarang!":
                    $ close_it_now = "1"
                    $ let_him_keep_looking = "2"
                    play audio curtainopen volume 0.2 fadeout 1.0
                    scene 279
                    mct "Cukup!"
                "Biarkan dia terus mencari":
                    $ let_him_keep_looking = "1"
                    $ close_it_now = "2"
                    scene 272
                    mct "Saya tidak tahu siapa yang lebih terkejut."
                    mct "Melihat wajahnya ..."
                    scene 273
                    mct "Istri saya telanjang di depannya dan saya tidak bergerak untuk menghentikan ini."
                    scene 261
                    mct "Sial, saya pikir saya bahkan bersemangat dengan itu."
                    mct "Saya sakit apa?"
                    scene 274
                    mct "Dia melepas bra sekarang."
                    mct "Mengapa saya tidak bisa pindah?"
                    scene 275
                    mct "Ini terlalu banyak."
                    mct "Saya tidak bisa membiarkan ini berlanjut."
                    mct "Jika [Violet] menyadari apa yang terjadi, dia akan membunuhku."
                    scene 277
                    mct "Saya perlu melakukan sesuatu!"
                    mct "Saya perlu pindah!"
                    scene 276
                    mct "SEKARANG!"
                    scene 275
                    ""
                    scene 278
                    mct "Toooo!"
                    mct "Cukup!"
            play audio curtainopen volume 0.2 fadeout 1.0
            scene 279
            mct "Sial, kuharap dia tidak terlalu banyak melihat."
            scene 280
            stranger "Bung! Mengapa Anda melakukan itu?"
            mc "Itulah istriku, kau mencoba mengintip, kau cabul!"
            stranger "Saya tidak mengintip! Aku bersumpah!"
            stranger "Saya hanya duduk di sini menunggu pacar saya."
            scene 281
            mc "Ya, benar."
            mc "Jangan mencoba menyangkalnya, saya melihat Anda mencari."
            stranger "Ok bung, maaf, saya tidak tahu!"
            stranger "Tapi, bisakah kamu menyalahkanku laki -laki? Istri Anda terlalu panas untuk tidak terlihat."
            scene 282
            mct "Sial, mendengarnya mengatakan itu ... dia benar, aku hanya berpikir aku tidak bisa menyalahkannya sebentar yang lalu ..."
            mct "Saya bahkan tidak bisa memahami perasaan saya sekarang."
            mct "Saya marah, tetapi pada saat yang sama itu adalah pilihan saya, untuk memulai."
            mct "Saya bisa menghentikan ini beberapa waktu yang lalu, tetapi saya tidak melakukannya."
            scene 283
            v "Sayang, apa yang terjadi?"
            v "Apakah semuanya baik -baik saja?"
            scene 284
            mc "Ya sayang, jangan khawatir."
            mc "Saya hanya berbicara dengan teman lama saya ..."
            scene 286
            vt "Oh, itu berarti kita tidak sendirian lagi."
            vt "Kira saya tidak akan mencoba pakaian dalam yang baru."
            vt "Lebih baik aku berpakaian."
            scene 284
            mc "Katakan padaku ketika kamu selesai, oke?"
            scene 283
            v "Oke sayang, aku hampir selesai di sini. Saya berpakaian sekarang."
            scene 284
            mc "Luangkan waktu Anda, saya akan berbicara dengan ... teman saya sementara saya menunggu Anda."
            scene 285
            stranger "Teman?"
            stranger "Well, since I'm your \"old friend\", Saya kira kita keren, kan?"
            scene 281
            mc "Tentu saja tidak, Anda idiot. Aku hanya tidak ingin dia tahu beberapa orang cabul mengintipnya karena dia mungkin akan membunuhmu lebih cepat dariku."
            mc "Sekarang keluarkan dari sini sebelum aku menendang wajahmu."
            stranger "Baiklah pria, dinginkan. Saya akan pergi."
            scene blackscreen
            pause 1.5
            scene 251
            mct "Oke, itu sudah dekat!"
            mct "Saya harus berhati -hati jika saya ingin pindah ke kota ini dengan [Violet] suatu hari nanti."
            mct "Saya tidak bisa melakukan hal -hal semacam itu dan berisiko mengeksposnya seperti itu."
            mct "Saya tidak akan pernah membiarkan ini terjadi lagi."
            if dont_let_him_pee == "1":
                stop music
                stop sound
                play sound endupdate fadein 1.0 volume 0.3
                scene blackscreen with fade
                centered "__Tag_0____tag_1____present day__tag_2____tag_3__"
                pause 0.8
                jump kitchendinner
            if ted_shower == "1":
                stop music
                stop sound
                jump backtoshower
            else:
                stop music
                stop sound
                jump bathroomdoor


    label backtoshower:
        play sound endupdate fadein 1.0 volume 0.3
        scene blackscreen with fade
        centered "__Tag_0____tag_1____present day__tag_2____tag_3__"
        pause 0.8
        play music showerinside fadein 0.5
        scene 149 with fade
        if dont_move == "1":
            mct "Cara saya merasakan ketika semua itu terjadi ..."
            mct "Saya tidak mengerti mengapa saya merasa seperti itu."
        mct "Kami terus mengalami situasi aneh sejak pertama kali kami datang ke kota ini."
        mct "Itu tidak bisa menjadi kebetulan ..."
        mct "Ini seperti ada sesuatu di sini yang membuat kita mendapat masalah."
        mct "Baiklah ... biarkan aku keluar dari sini."
        mct "Amelia dan Jeff akan berada di sini kapan saja sekarang."
        scene blackscreen
        narrador "[mcname] berpakaian dan setelah menyapa semua orang, mereka semua makan malam."
        stop sound
        jump kitchendinner


    label bathroomdoor:
        play sound endupdate fadein 1.0 volume 0.3
        scene blackscreen with fade
        centered "__Tag_0____tag_1____present day__tag_2____tag_3__"
        pause 0.8
        scene 229
        play music showeroutside fadein 3.0 volume 0.1
        if dont_move == "1":
            mct "Itu saja! Di situlah saya memiliki perasaan ini untuk pertama kalinya."
            mct "Tapi saya masih tidak mengerti mengapa saya merasa seperti ini."
        mct "Kami terus mengalami situasi seperti ini sejak pertama kali kami datang ke kota ini."
        mct "Itu tidak bisa menjadi kebetulan ..."
        mct "Ini seperti ada sesuatu di sini yang membuat kita mendapat masalah."
        mct "Saya bilang saya tidak pernah membiarkan Thigs seperti itu terjadi lagi tapi sepertinya saya tidak bisa mengendalikannya ..."
        if dont_move == "1":
            mct "Ini seperti sesuatu di dalam diri saya ingin hal -hal ini terjadi ..."
        mct "Saya harus memikirkannya nanti, saat ini saya memiliki masalah yang lebih besar."
        stop sound
        mct "[Violet] ada di sana di kamar mandi dan saya melihat Jeff masuk."
        mct "Apa yang harus saya lakukan sekarang?"
        menu:
            "Buka pintu":
                $ open_the_door = "1"
                $ get_back_to_the_kitchen = "2"
                mct "Saya harus melihat apa yang terjadi."
                scene 287
                mct "Mungkin aku salah dan dia bahkan tidak ada di sana."
                scene 288
                mct "Mungkin dia di luar ..."
                scene 289
                play sound chockmale volume 0.5
                mct "Tidak, tidak mungkin!"
                mct "Dia masih di sana."
                mct "Tapi Jeff ... aku melihatnya ... berjalan masuk."
                scene 290
                mct "Itu dia, aku tidak akan gila."
                mct "Setidaknya belum ..."
                scene 291
                mct "Dan dia ada di sana, telanjang."
                mct "Mencoba menutupi sebanyak yang dia bisa."
                scene 292
                mct "Tidak terlalu berhasil ..."
                mct "Saya tahu dia menutupi matanya tapi tetap saja, ini tidak normal."
                mct "Apa yang terjadi padanya?"
                mct "Belum lama ini, jika hal seperti ini terjadi, [Violet] akan benar -benar malu."
                mct "Jadi bagaimana dia bisa membiarkan Jeff masuk sementara dia benar -benar telanjang di kamar mandi?"
                scene 290
                mct "Dan kenapa dia di sini?"
                scene 292
                vt "Ini aneh, mengapa saya menyetujui ini?"
                vt "Saya hanya berharap dia pergi dengan cepat."
                v "Baiklah Jeff, lakukan saja apa yang harus Anda lakukan dan keluar, oke?"
                v "Dan jangan lihat di sini."
                scene 293
                jeff "Oh, jangan khawatir, aku menutupi mataku, aku tidak bisa melihat apa pun."
                jefft "Hahaha, dia sangat naif."
                scene 294
                jefft "Saya masih tidak percaya betapa beruntungnya saya sekarang."
                jefft "Lihatlah tubuh itu! [Violet] adalah sesuatu yang lain."
                jefft "Saya hampir bisa melihat putingnya."
                jefft "Dan dia tidak melakukan pekerjaan dengan baik dalam meliput vagina yang indah itu."
                scene 296
                mct "Apakah dia membiarkannya masuk karena dia perlu buang air kecil?"
                mct "Tidak bisakah dia menunggu sampai dia pergi?"
                scene 293
                mct "Siapa yang saya bodohi, saya tahu jawabannya dengan sangat baik."
                mct "Dia mungkin bahkan tidak perlu buang air kecil."
                scene 294
                mct "Dia meluangkan waktu untuk menikmati pemandangan sebanyak yang dia bisa."
                scene 296
                play sound heartbeatslow volume 0.5 loop
                mct "Sobat, situasi ini. Bagaimana ini bisa terjadi?"
                if let_him_keep_looking == "1":
                    mct "Di sini saya menonton ketika pria lain melihat istri saya saat dia telanjang ... lagi."
                mct "Dan saya pikir saya menikmatinya."
                mct "Saya selalu senang memamerkannya kepada pria lain, tetapi ini sangat berbeda."
                mct "Saya akan dihidupkan oleh itu."
                mct "Saya pikir saya suka ketika pria lain bernafsu setelah istri saya."
                mct "Itu gila."
                mct "Apa yang akan [Violet] pikirkan tentang ini? Saya bahkan tidak tahu harus berpikir apa."
                mct "Dan bagaimana dia baik -baik saja dengan ini?"
                stop sound
                scene 300
                vt "Jeff sudah ada di sini untuk sementara waktu."
                vt "Aku sangat malu aku bahkan tidak bisa melihat arahnya."
                vt "Tapi dia terlalu lama."
                vt "Saya harus melihatnya ..."
                scene 302
                vt "Dia masih di sana ..."
                vt "Berapa lama waktu yang dibutuhkan untuk buang air kecil?"
                scene 303
                vt "HM? Tunggu, apakah itu ..."
                scene 304
                play audio zipper
                vt "YA AMPUN! Saya bisa melihat penisnya."
                scene 300
                vt "Berengsek! Mengapa saya harus melihat?"
                scene 313
                v "Jeff, sudah selesai?"
                v "Kenapa kamu butuh waktu lama?"
                scene 312
                jeff "Oh, maafkan aku tapi aku punya sedikit masalah di sini ... hehe."
                scene 305
                vt "\"Little problem\"katanya."
                vt "Tidak terlihat sedikit dari sini."
                scene 302
                vt "Apa yang saya katakan!"
                vt "Dia adalah suami baru ibuku."
                scene 312
                jeff "Saya mencoba, saya bersumpah. Tetapi..."
                jeff "Agak sulit untuk buang air kecil dengan penisku seperti ini."
                scene 306
                v "Apa?"
                scene 305
                vt "Tunggu, apakah dia mengalami ereksi?"
                scene 313
                v "APA -APAAN, JEFF !!"
                v "Mengapa Anda mengalami ereksi sekarang ??"
                scene 312
                jeff "Maaf oke, saya tidak bisa mengendalikannya."
                jeff "Cukup sulit untuk tidak menjadi keras sambil melihat gadis seksi seperti Anda."
                scene 306
                v "Apa?? Apakah Anda mengatakan bahwa Anda seperti ini karena saya?"
                scene 312
                jeff "Sial ya. Anda super panas [Violet]."
                jeff "Dan juga ... Anda tidak melakukan pekerjaan dengan baik dalam meliput bagian Anda, jika Anda tahu apa yang saya maksud."
                scene 306
                vt "Apa?"
                scene 307
                vt "YA AMPUN! Dia benar."
                vt "Saya nyaris tidak menutupi vagina saya."
                scene 300
                vt "Saya tahu itu bukan ide yang baik untuk membiarkannya masuk."
                vt "Mengapa saya menempatkan diri saya dalam situasi ini?"
                scene 312
                jeff "Jadi, saya punya ide ... jika Anda membiarkan saya sedikit menyentaknya, saya akan bisa buang air kecil."
                scene 306
                vt "WTF! Apakah dia serius sekarang?"
                vt "Dia tidak bisa meminta ini."
                scene 313
                v "Anda tidak bisa serius sekarang."
                v "Tidakkah menurut Anda ini tidak pantas?"
                scene 312
                jeff "Yah, saya tidak bisa kembali ke Amelia dengan penis saya seperti ini."
                jeff "Dia akan mulai mengajukan pertanyaan."
                jeff "Belum lagi [McName] ... apa yang akan dia katakan tentang itu?"
                scene 306
                vt "Ya Tuhan, dia benar. Saya tidak ingin [McName] berpikir saya melakukan sesuatu yang salah."
                vt "Apa yang harus saya lakukan?"
                vt "Apakah dia benar -benar hanya akan melakukannya di depan saya?"
                vt "Apakah saya benar -benar akan mengizinkan ini?"
                menu:
                    "Katakan padanya untuk keluar!":
                        $ tell_him_to_get_out = "1"
                        $ allow_him_to_jerk_off = "2"
                        scene 313
                        v "APAKAH KAMU GILA? KELUAR DARI SINI SEKARANG!"
                        scene 312
                        jeff "Oke oke, maaf, itu hanya lelucon."
                        jeff "Anda tidak perlu berteriak, saya sudah pergi."
                        scene 297
                        mct "Wow! [Violet] menjadi sangat marah."
                        mct "Sial, aku seharusnya melakukan sesuatu ..."
                        scene 296
                        mct "Baiklah, izinkan saya keluar dari sini sebelum mereka melihat saya."
                        scene blackscreen
                        narrador "[McName] kembali ke dapur dan setelah beberapa saat Jeff dan [Violet] bergabung dengan mereka sehingga mereka semua bisa makan."
                        pause 0.5
                        jump kitchendinner
                    "Biarkan dia tersentak":


                        $ allow_him_to_jerk_off = "1"
                        $ tell_him_to_get_out = "2"
                        vt "Maksudku, dia benar."
                        vt "Entah itu atau kirim dia kembali ke sana dengan penisnya dengan keras ..."
                        vt "Dan akan sulit untuk menjelaskan jika seseorang bertanya ..."
                        vt "Kira saya akan membiarkan dia melakukannya. Ini juga tidak seperti aku melakukannya untuknya ..."
                        vt "Saya harap saya tidak menyesali ini nanti."
                scene 303
                v "Oke Jeff, Anda bisa melakukannya ..."
                scene 313
                v "Tapi lakukan dengan cepat dan jangan berani melihat saya."
                scene 312
                jeff "Oke, baiklah."
                jeff "Ini dia saat itu."
                scene 300
                play sound fap fadein 0.5 loop volume 3.0
                vt "Ini aneh, saya bisa mendengarnya melakukannya."
                vt "Persetan ... suaranya tidak membantu."
                vt "Saya sakit apa?"
                vt "Apakah saya benar -benar terangsang oleh ini?"
                scene 302
                vt "Jeff ada di sana masturbasi sementara aku telanjang di ruangan yang sama."
                if park_photos == "1":
                    vt "Saya masih sangat terangsang setelah adegan di taman."
                    vt "Di sini saya terpapar, sama seperti ketika pria itu memata -matai kami sementara [McName] dan saya mengambil gambar nakal di sebelah patung itu."
                vt "Saya perlu melakukan sesuatu tentang itu."
                vt "Saya kira tidak ada yang salah dengan ..."
                scene 307
                vt "Saya hanya perlu ..."
                scene 308
                vt "Sentuh diri saya sedikit."
                scene touchingherself1
                vt "Itu saja!"
                vt "Sama seperti itu."
                vt "Bagaimanapun, itulah kamar mandi saya."
                vt "Saya juga bisa melakukan masturbasi jika saya mau."
                scene 297
                mct "Wow! Dia mulai masturbasi."
                scene 296
                mct "Dan Jeff melakukan hal yang sama."
                scene touchingherself2
                ""
                scene touchingherself3
                vt "Saya harus mengakui, Jeff memiliki ayam yang bagus."
                if help_him == "1":
                    vt "Ini adalah yang kedua yang saya lihat hari ini selain suami saya."
                    vt "Itu gila!"
                vt "Saya tidak pernah berpikir dia akan memiliki yang sebesar itu."
                vt "Itu sangat tebal."
                vt "Bagaimana ibuku bisa mengambilnya di dalam dirinya ..."
                scene touchingherself2
                vt "Maksud saya..."
                vt "Itu pasti sangat menyakitkan."
                vt "Saya tidak berpikir itu bisa menyenangkan sama sekali."
                play audio moan1
                vt "Aaahh ..."
                scene 307
                vt "YA AMPUN! Apakah saya baru saja mengerang?"
                stop sound
                scene 312
                jefft "Wow, apakah itu erangan?"
                scene 297
                mct "APAKAH ITU ERANGAN ??"
                scene 300
                vt "Kotoran! Itu pasti erangan."
                vt "Saya hanya berharap dia tidak mendengarnya."
                scene 312
                jefft "Apakah dia masturbasi sekarang?"
                jefft "Ini lebih baik dari yang saya harapkan, mungkin dia tidak begitu pemalu."
                scene 300
                vt "Apa yang saya lakukan?"
                vt "Apa yang akan [McName] katakan jika dia melihat ini?"
                if embrace_feelings == "1":
                    vt "Mungkin dia bahkan akan menyukainya karena peristiwa baru -baru ini."
                    vt "Tapi meskipun begitu, ini sepertinya tidak benar."
                scene 301
                vt "Maksud saya..."
                scene 295
                vt "APA?! [McName]?!"
                scene 297
                mct "Oh sial! Dia melihatku."
                scene 295
                vt "YA AMPUN! [McName] ada di sana!"
                vt "Apa yang dia lakukan di sana? Sudah berapa lama dia di sana?"
                vt "Apa yang dia pikirkan?"
                scene 298
                play sound heartbeatslow loop
                mct "Sial, aku perlu melakukan sesuatu."
                mct "Jika saya tidak melakukan apa pun [Violet] akan panik."
                mct "Saya perlu menunjukkan kepadanya jika saya baik -baik saja dengan ini atau tidak."
                scene 295
                mct "Saya menikmati diri saya sendiri dan dia jelas menikmati dirinya sendiri."
                mct "Lihat saja wajahnya, dia terkejut melihatku di sini, tetapi pada saat yang sama matanya tidak bisa menyembunyikan betapa terangsangnya dia."
                scene 298
                mct "Tapi saya masih tidak yakin apakah saya harus menempuh jalan ini, saya tidak yakin apakah saya harus menyerah pada perasaan ini."
                mct "Ini adalah kesempatan terakhir saya untuk mundur."
                mct "Saya perlu membuat keputusan."
                menu:
                    "Kembali":
                        stop sound
                        $ back_out = "1"
                        $ show_you_are_okay = "2"
                        scene 301
                        vt "Sial, ini memalukan, [McName] hanya berdiri di sana. Saya perlu melakukan sesuatu."
                        scene 302
                        v "Jeff, ini tidak akan berhasil, bisakah kamu keluar?"
                        scene 312
                        jeff "Hanya sesaat, itu tidak akan memakan waktu lama."
                        scene 313
                        v "WHICH PART OF \"GET OUT\"APAKAH KAMU TIDAK MENDENGAR? KELUAR DARI SINI SEKARANG!"
                        scene 312
                        jeff "Oke oke, maaf."
                        jeff "Anda tidak perlu berteriak, saya sudah pergi."
                        scene 297
                        mct "Wow! [Violet] menjadi sangat marah."
                        mct "Sial, aku seharusnya melakukan sesuatu ..."
                        mct "Sepertinya dia terkendali ini."
                        scene 296
                        mct "Baiklah, biarkan aku keluar dari sini sebelum dia melihatku."
                        scene blackscreen
                        narrador "[McName] kembali ke dapur dan setelah beberapa saat Jeff dan [Violet] bergabung dengan mereka sehingga mereka semua bisa makan."
                        pause 0.5
                        jump kitchendinner
                    "Tunjukkan padanya kamu baik -baik saja":


                        stop sound
                        $ show_you_are_okay = "1"
                        $ back_out = "2"
                        scene 299
                        mct "Itu saja."
                scene 299
                mct "Saya tidak akan mundur sekarang."
                scene 314
                mc "* Berbisik* Lanjutkan!"
                scene 295
                vt "Apa? Apa yang dia katakan?"
                vt "Apakah dia benar -benar baik -baik saja dengan ini?"
                scene 315
                ""
                scene 314
                ""
                scene 295
                vt "Wow! Saya kira dia sudah ada di sana untuk sementara waktu."
                vt "Sepertinya dia tahu semua yang terjadi di sini."
                vt "Dan dia tidak marah. Dia ingin aku melanjutkan."
                vt "Kira dia tidak berbohong ketika dia mengatakan dia memiliki fantasi dengan saya terpapar di sekitar orang."
                scene 303
                vt "Nah, jika itu masalahnya, saya tidak akan berbohong ... Saya pasti menikmati diri saya sendiri."
                scene 304
                vt "Adegan ini membuatku lebih basah dan lebih basah."
                scene 314
                vt "Dan sekarang saya tahu [McName] ada di sana dan dia juga menikmatinya, itu membuat ini sepuluh kali lebih panas."
                scene touchingherself3
                play sound fap fadein 0.5 loop volume 3.0
                vt "Saya perlu melepaskan ketegangan yang saya rasakan."
                vt "Ya! Itu saja!"
                vt "Saya suka perasaan ini."
                vt "Hanya sedikit lebih lama dan aku akan cum."
                vt "Saya gelisah."
                vt "Ya Tuhan!"
                play audio moan1 volume 2.0
                vt "Aahh ... hampir sampai ..."
                scene 312
                play sound disco volume 0.5
                jeff "Hei [Violet], kamu baik -baik saja?"
                scene 306
                v "HM? Apa?"
                scene 316
                v "Oh tidak, aku J-Just ..."
                v "... Saya ingin tahu apakah Anda sudah selesai?"
                scene 312
                jeff "Baik, saya pikir saya mendengar Anda kesakitan atau sesuatu ..."
                scene 316
                v "Tidak, saya hanya S-Stubbed toe saya, itu saja."
                scene 312
                jeff "Jika Anda berkata begitu ..."
                jeff "Tapi, menjawab pertanyaan Anda, ini membutuhkan waktu lebih lama dari yang saya kira."
                jeff "Saya mungkin perlu sedikit lebih banyak stimulasi untuk menyelesaikannya."
                scene 306
                v "Lebih banyak stimulasi? Apa maksudmu?"
                scene 317
                jeff "Maksud saya, sulit bagi saya untuk melakukan masturbasi tanpa memiliki sesuatu yang seksi untuk dilihat, Anda tahu?"
                jeff "Jika Anda benar -benar ingin mempercepat ini, Anda bisa membiarkan saya melihat payudara Anda."
                scene 306
                v "APA? Apakah kamu gila? Sudah cukup buruk fakta bahwa saya membiarkan Anda melakukan masturbasi di sini, sekarang Anda ingin melihat payudaraku?"
                scene 317
                jeff "Saya hanya mengatakan jika Anda ingin saya cum lebih cepat ini akan banyak membantu."
                scene 302
                v "Banyak membantu, ya?"
                v "Saya yakin ..."
                scene 317
                jeff "Maksud saya, ini tidak seperti Anda banyak bersembunyi, selain itu ... Anda sudah melihat penis saya, hanya adil saya melihat payudara Anda sekarang."
                scene 316
                vt "Sial, dia melihatku melihat."
                scene 300
                vt "Dia agak ada benarnya."
                vt "Dia sudah banyak terlihat, sepasang payudara bukanlah apa -apa."
                vt "Tunggu, apakah saya benar -benar mempertimbangkan ini?"
                vt "Apakah saya benar -benar bersedia menunjukkan kepadanya payudara saya sehingga dia bisa cum lebih cepat?"
                scene 300
                vt "Saya tidak tahu apakah saya harus ..."
                scene 301
                vt "Apakah [McName] akan menyukainya jika saya melakukan itu?"
                scene 297
                ""
                scene 298
                ""
                scene 299
                mc "* Berbisik* lakukan!"
                play sound transition
                scene blackscreen
                pause 2.0
                scene blackscreen
                narrador "Pada saat yang sama..."
                scene 319
                ameliat "Yah, yah ... sepertinya semua orang memutuskan untuk pergi ke tempat lain dan meninggalkan saya di sini sendirian."
                ameliat "Itu tidak terlalu bagus."
                ameliat "Saya tidak akan berdiri di sini dan mempersiapkan semuanya sendirian jika itu yang mereka inginkan."
                scene 318
                ameliat "Selain itu ... tidak jarang saya mendapat kesempatan untuk menghabiskan waktu sendirian dengan [McName]."
                ameliat "Saya ingin sekali menggoda anak laki -laki itu lagi."
                ameliat "Aku masih tidak percaya dia memeras pantatku sebelumnya."
                ameliat "Dan dia bahkan mendapatkan penisnya keras haha."
                scene 319
                ameliat "Tapi mari kita pikirkan tentang itu lain kali."
                ameliat "Aku akan mencari mereka sekarang!"
                play sound transition
                scene blackscreen
                ""
                scene 299
                mc "* Berbisik* lakukan!"
                scene 295
                vt "Wow! Saya tidak mengharapkan itu."
                scene 299
                mc "* Berbisik* Biarkan dia melihat payudara Anda."
                scene 316
                vt "YA AMPUN! Apakah dia benar -benar menginginkan ini?"
                scene 295
                vt "Raut wajahnya ..."
                scene 299
                vt "Tampilan itu tidak berbohong."
                vt "Dia menginginkan ini sama seperti saya."
                vt "Mungkin bahkan lebih dari yang saya lakukan."
                scene 320
                vt "Oke, saya kira itu jawaban saya."
                vt "Dia sepertinya benar -benar ingin saya melakukan ini."
                vt "Saya harus lebih percaya diri tentang ini."
                vt "Dia tahu aku juga menikmatinya."
                vt "Nah, jika [McName] sangat menyukainya, maka saya melakukan ini untuknya."
                scene 321
                v "Baik Jeff, aku akan membiarkanmu melihat."
                scene 321
                v "Tetapi Anda hanya bisa melihat, jika Anda mencoba apa pun, saya akan segera keluar dari sini."
                v "Selesaikan saja dan keluar sebelum seseorang datang ke sini mencari kami ..."
                scene 320
                v "Kami tidak ingin itu terjadi, bukan?"
                scene 314
                mct "Haha, sayang yang sangat halus."
                mct "Sobat, saya suka ketika dia bermain -main seperti itu!"
                scene 321
                v "Apakah kita mengerti?"
                scene 317
                jeff "Oh ya, baiklah denganku."
                scene 321
                v "Oke, ini dia ..."
                scene 322
                ""
                v "Apakah kamu bahagia sekarang?"
                vt "Saya benar -benar melakukannya. Tidak ada jalan untuk kembali sekarang."
                scene 323
                jeff "Wow! [Violet] Payudara Anda sempurna!"
                jeff "Saya sangat bahagia!"
                jeff "Saya perlu lebih nyaman untuk ini."
                scene 324
                jeff "Aku hanya akan melepas jaket ini dan menurunkan celanaku, jangan khawatir."
                scene 322
                v "Baik, tapi cepatlah."
                vt "Ini sangat panas. Saya masih tidak percaya kami melakukan ini."
                scene 338
                jeff "Baiklah, saya siap!"
                jeff "Tunjukkan payudaramu yang indah, sayang."
                scene jeffjerkingoff3
                play sound fap fadein 0.5 loop volume 3.0
                jeff "Itu saja, saya menyukainya."
                scene 335
                mct "Itu terjadi ... itu benar -benar terjadi."
                mct "Dia membiarkannya tersentak tepat di depannya, dengan payudaranya dipajang."
                scene jeffjerkingoff1
                mct "Dan saya membiarkan ini terjadi."
                mct "Saya menikmati pemandangan ini."
                if let_him_keep_looking == "1":
                    mct "Sama seperti di ruang pas."
                    mct "Saya berbohong kepada diri saya sendiri saat itu dan tidak pernah memikirkannya sejak itu."
                    mct "Tapi sekarang ..."
                mct "Saya harus berhenti berbohong kepada diri saya sendiri dan mengakuinya."
                scene 299
                mct "Saya sangat menikmati ini!"
                scene jeffjerkingoff3
                mct "Dan saya tahu dia juga."
                mct "Dia tidak bisa mengalihkan pandangan dari penisnya."
                scene 322
                vt "Sungguh! Itu tidak adil. Ini penyiksaan!"
                vt "Saya ingin masturbasi juga, tetapi saya tidak bisa memberi tahu dia bahwa saya menikmati ini."
                scene jeffjerkingoff4
                vt "Dia benar -benar melakukannya."
                vt "Ini membuatku sangat basah, dan bukan karena kamar mandi."
                vt "Saya berharap dia sudah dekat."
                scene jeffjerkingoff1
                jeff "[violet] anda sangat seksi!"
                scene jeffjerkingoff4
                jeff "Saya bisa melihat payudara Anda sepanjang hari."
                jeff "Apa yang akan saya berikan untuk menjilat mereka."
                v "Bahkan tidak memikirkannya."
                v "Saya bilang Anda hanya bisa melihat."
                scene jeffjerkingoff1
                mct "Dia juga menikmati dirinya sendiri."
                if park_photos == "1":
                    mct "Setelah hari ini di taman, saya yakin dia memiliki semacam ketegaran eksibisionis padanya."
                    mct "Dia suka menunjukkan tubuhnya."
                    mct "Dan saya senang melihatnya melakukannya."
                scene 299
                mct "Itu pasangan yang sempurna."
                mct "Saya hanya berharap kami ..."
                amelia "[mcname]!"
                scene 327
                mct "HM?"
                stop sound
                scene 331
                amelia "[McName]! Kamu ada di mana?"
                scene 327
                play sound chockmale volume 0.2
                mct "Hah!"
                play sound fap fadein 0.5 loop volume 3.0
                scene jeffjerkingoff2
                mct "Saya benar -benar lupa tentang Amelia."
                mct "Jika dia datang ke sini, kita akan memiliki banyak hal untuk dijelaskan."
                scene 327
                mct "Saya harus pergi!"
                play sound doorclose volume 0.3
                scene 328
                ""
                scene 339
                jeff "HM?"
                scene blackscreen
                pause 1.0
                scene 329
                mct "Kotoran! Apa yang saya pikirkan?"
                mct "Amelia hampir menangkap saya di sini."
                scene 332
                amelia "Hei [McName], dari mana saja kamu?"
                amelia "Dan apa yang kamu lakukan berdiri di sana?"
                scene 330
                amelia "Anda sudah pergi sebentar sekarang dan Anda tidak memberi tahu saya ke mana Anda pergi ..."
                amelia "Dan Jeff juga ..."
                scene 333
                amelia "Jangan bilang kalian berdua lakukan dengan sengaja untuk meninggalkanku sendirian di dapur."
                amelia "Karena jika Anda berpikir bahwa saya akan mempersiapkan semuanya sendirian, Anda semua gila."
                scene 334
                mc "Tenang. Saya baru saja memeriksa untuk melihat apakah [Violet] akan memakan waktu lebih lama di kamar mandi ..."
                scene 345
                mc "Tentu saja saya akan membantu Anda."
                mc "Saya hanya akan kembali ke sana."
                mc "Tapi aku tidak bisa menyalahkanmu karena sudah merindukanku, haha."
                scene 347
                amelia "Dari apa yang bisa saya lihat, sepertinya Anda adalah orang yang hilang __tag_0__me__tag_1__!"
                scene 348
                mc "Apa?"
                scene 347
                amelia "Lihat saja ke bawah, sayang."
                scene 349
                mct "Apa yang dia bicarakan ..."
                scene 350
                mct "OH SIAL!"
                mct "Penisku masih sulit."
                mct "Permainan dengan [Violet] ini benar -benar berpengaruh pada saya."
                scene 351
                mc "Saya sangat menyesal Amelia ..."
                mc "Itu J-Just ..."
                scene 347
                amelia "Jangan khawatir, sayang."
                amelia "Saya tahu Anda seperti ini dari melihat istri Anda di kamar mandi, tentu saja."
                amelia "Aku hanya menggodamu."
                scene 351
                mc "Huh ... ya itu saja."
                mc "Tapi saya masih malu menjadi seperti ini di depan Anda."
                scene 344
                amelia "Serius, jangan khawatir tentang itu."
                amelia "Sekarang ... [Violet] harus dilakukan sebentar lagi."
                amelia "Ayo siapkan semuanya sebelum dia keluar, oke?"
                scene 345
                mc "Ya, tentu! Ayo pergi."
                scene 351
                mc "Saya hanya berharap [Violet] baik -baik saja. Aku benci membiarkannya sendirian di sana bersama Jeff, tapi aku harus pergi dengan Amelia sekarang ..."
                scene blackscreen
                pause 1.0
                scene 339
                jeff "Apa itu?"
                jeff "Apakah Anda mendengar suara itu, [Violet]?"
                scene 340
                v "Saya ... Saya tidak tahu, mungkin mereka ditransmisikan sesuatu di dapur ..."
                scene 339
                jeff "Hm, oke. Biarkan saya kembali ke sana."
                scene 341
                vt "[mcname] baru saja pergi ... ibuku pasti memanggilnya atau semacamnya."
                vt "Sekarang saya di sini sendirian dengan Jeff lagi ..."
                play sound fap fadein 0.5 loop volume 3.0
                scene jeffjerkingoffdoorclosed
                vt "Dan dia masih membelai penisnya."
                vt "Saya yakin dia bahkan belum dekat dengan Cumming."
                scene 316
                vt "Itu menyenangkan dan menyenangkan ketika [McName] sedang menonton, tetapi sekarang saya tidak tahu apakah saya harus melanjutkan tanpanya di sini."
                vt "Meskipun saya juga menyukainya, saya melakukan ini untuknya, untuk menggodanya."
                vt "Saya tahu saya setuju untuk membiarkan Jeff masturbasi sambil melihat payudara saya, tetapi haruskah saya membiarkannya selesai sekarang bahwa [McName] hilang?"
                menu:
                    "Jangan biarkan dia selesai.":
                        $ dont_let_him_finish = "1"
                        $ let_him_finish = "2"
                        stop sound
                        scene 341
                        v "Saya G-Guess lebih baik jika Anda pergi sekarang, Jeff."
                        v "Kami di sini terlalu lama."
                        scene 342
                        jeff "Apa?? Tidak, Anda tidak bisa melakukan ini untuk saya, saya belum selesai!"
                        scene 343
                        v "Yah, itu bukan masalah saya."
                        v "Anda memiliki kesempatan dan Anda terlalu lama."
                        v "Ayo sekarang, berhentilah menatapku dan keluar."
                        scene 324
                        jeff "Oke, baiklah!"
                        jeff "Aku pergi."
                        jefft "Lain kali saya harus lebih tegas."
                        scene blackscreen
                        narrador "Jeff kembali ke dapur dan setelah beberapa saat [Violet] bergabung dengan mereka sehingga mereka semua bisa makan."
                        pause 0.5
                        jump kitchendinner
                    "Biarkan dia selesai":


                        $ let_him_finish = "1"
                        $ dont_let_him_finish = "2"
                        scene 322
                        vt "Saya kira tidak ada yang salah dalam membiarkannya selesai."
                        vt "Aku bilang aku akan membiarkan dia melakukannya, tidak akan kembali sekarang."
                        vt "Dan saya tidak akan berbohong ... Saya semakin terangsang dengan semua ini."
                        vt "Saya yakin [McName] ingin saya melanjutkan juga."
                        vt "Baiklah. Aku akan membiarkannya selesai, tapi dia perlu melakukannya lebih cepat."
                        scene jeffjerkingoff3
                        v "Jeff, katakan padaku ... apakah kamu akan butuh waktu lama?"
                        v "Kita harus keluar, kita di sini terlalu lama sekarang."
                        scene jeffjerkingoffdoorclosed
                        jeff "Saya melakukan yang terbaik yang saya bisa sayang, tetapi Anda tidak banyak membantu saya di sini."
                        scene 352
                        stop sound
                        v "Apa? Apakah Anda benar -benar mengatakan itu?"
                        v "Saya membiarkan Anda melihat payudara saya telanjang sepenuhnya dan Anda mengatakan saya tidak membantu?"
                        v "Apa lagi yang Anda ingin saya lakukan?"
                        scene 338
                        jeff "Jangan salah paham, Anda seksi seperti bercinta dan saya suka payudara Anda dan semua kecuali ..."
                        scene 352
                        jeff "Terasa seperti aku tersentak pada patung."
                        jeff "Jangan terlalu dingin."
                        scene 338
                        jeff "Anda setidaknya bisa melakukan beberapa pose yang lebih seksi dan berhenti menutupi vagina Anda."
                        jeff "Saya jamin itu akan membantu dan saya akan cum dalam waktu singkat."
                        scene 354
                        vt "Apa? Dingin? Berani -beraninya dia memanggilku seperti itu."
                        vt "Bajingan sialan ..."
                        scene 353
                        vt "Tapi ... dia agak benar."
                        vt "Saya tidak berusaha banyak sekarang karena [McName] tidak menonton."
                        vt "Kira aku masih tidak nyaman melakukan ini tanpa dia ..."
                        vt "Bahkan dengan dia menunjukkan bahwa dia sangat menyukai ini."
                        scene 338
                        jeff "Ayo, apakah Anda ingin [McName] datang ke sini mencari kami?"
                        scene 320
                        vt "Hehehe."
                        vt "Kalau saja dia tahu ..."
                        vt "Oke, saya melakukan ini."
                        vt "Saya hanya akan mengikuti arus."
                        scene 355
                        v "Baiklah Jeff, Anda menang."
                        v "Saya akan melakukannya. Tolong cum lebih cepat."
                        scene 338
                        jeff "WOW! Itulah yang saya bicarakan!"
                        scene 355
                        play sound fap fadein 0.5 loop volume 3.0
                        jeff "Itu vagina bagus yang Anda miliki di sana."
                        jeff "[mcname] sangat beruntung untuk bercinta dengan vagina slutty ini setiap hari!"
                        vt "Ya Tuhan! Saya harus tersinggung oleh itu, jadi mengapa saya semakin terangsang oleh kata -kata ini."
                        scene jeffjerkingoffdoorclosed
                        jeff "Ayo, berbalik untukku sekarang."
                        jeff "Saya sudah dekat."
                        scene 355
                        v "Hm ... O-Oke."
                        scene jeffjerkingoffdoorclosed2
                        v "Seperti ini?"
                        jeff "Itu sempurna, pelacur!"
                        jeff "Pantat yang hebat!"
                        jeff "Saya sudah lama tidak cum."
                        jeff "Pemandangan ini akan membuatku gila!"
                        scene jeffjerkingoffdoorclosed3
                        jeff "Aahhah ..."
                        jeff "Sungguh! Aku akan cum, pelacur!"
                        jeff "Ambil!"
                        scene 359
                        play audio guycum fadein 0.5 volume 3.0
                        jeff "Ohawaahh ..."
                        scene 360
                        play audio cum1 volume 3.0
                        ""
                        scene 361
                        stop sound
                        play audio cum1 volume 3.0
                        v "Ahhh!"
                        scene 362
                        v "ASTAGA!"
                        scene 363
                        v "WTF ITU?!"
                        scene 362
                        v "KAKIKU!"
                        scene 364
                        v "ANDA DATANG DI KAKI SAYA, ANDA BAJINGAN!"
                        scene 365
                        jeff "Maaf sayang, saya tidak bisa menahannya."
                        jeff "Sudah lama sejak saya datang begitu banyak."
                        jeff "Anda harus bangga pada diri sendiri karena membuat saya cum seperti itu!"
                        scene 364
                        v "DAN ANDA HARUS KELUAR SEKARANG SEBELUM SAYA MENENDANG PANTAT ANDA!"
                        scene 365
                        jeff "Tunggu, aku belum buang air kecil."
                        scene 364
                        v "AKU TIDAK PEDULI! KELUAR SEKARANG!"
                        scene 324
                        play sound dress volume 0.5
                        jeff "Jeez! Oke, baiklah."
                        jeff "Aku pergi."
                        jeff "Biarkan saya berpakaian lebih dulu ... akan sulit untuk menjelaskan mengapa saya keluar dari sini tanpa celana saya, hehe."
                        stop sound
                        scene 316
                        vt "Sungguh brengsek!"
                        vt "Kotoran! Sekarang saya perlu mencuci diri lagi ..."
                        vt "Saya harus bergegas, mereka menunggu saya."
                        scene blackscreen
                        narrador "Jeff kembali ke dapur dan setelah beberapa saat, [Violet] bergabung dengan mereka sehingga mereka semua bisa makan."


                scene blackscreen
                pause 0.5
                jump kitchendinner
            "Kembali ke dapur. __Tag_0 __ (dapat menyebabkan jalur curang) __ tag_1__":


                $ get_back_to_the_kitchen = "1"
                $ open_the_door = "2"
                mct "Mungkin saya terlalu banyak berpikir."
                mct "Dia mungkin bahkan tidak ada di dalam."
                mct "Saya akan kembali ke dapur dan menunggu semua orang ..."
                scene blackscreen
                narrador "[McName] kembali ke dapur dan setelah beberapa saat Jeff dan [Violet] bergabung dengan mereka sehingga mereka semua bisa makan."
                pause 0.5


        jump kitchendinner


    label kitchendinner:
        stop sound
        stop music
        play music neighborhood fadein 1.5 volume 0.5
        scene 366
        amelia "Akhirnya kita semua di sini!"
        amelia "Aku merasa lapar menunggumu."
        if ted_shower == "1":
            scene 369
            mc "Maaf saya butuh waktu lama di kamar mandi."
            mc "Semoga saya tidak membuat Anda kelaparan sampai mati, haha."
            scene 368
            amelia "Oh, percayalah, aku mengeluarkan air liur sekarang dan itu semua salahmu ..."
            scene 373
            mct "Apakah saya gila atau apakah itu terdengar lebih seksual daripada yang seharusnya?"
            mc "Hm ... A-Lagi, saya sangat menyesal."
            scene 368
            amelia "Haha, aku hanya bercanda sayang."
            amelia "Jangan khawatir tentang itu."
            scene 366
            amelia "Saya senang kita semua bisa makan sekarang."
            scene 372
            amelia "Jadi katakan padaku, sayang."
            amelia "Apa rencana Anda setelah Anda sepenuhnya diselesaikan?"
            scene 375
            v "Yah, saya pikir saya akan mencari pekerjaan sesegera mungkin."
            v "[McName], dalam mengurus semuanya sekarang, tetapi saya ingin membantu."
            scene 384
            mc "Saya mengatakan kepadanya untuk tidak khawatir tentang itu, tetapi dia bersikeras."
            mc "Jika dia benar -benar ingin mencari pekerjaan, maka saya tidak menentangnya."
            mc "Saya hanya ingin menjadikannya wanita paling bahagia hidup."
            scene 385
            v "Sendiri, aku sudah menjadi wanita paling bahagia yang hidup berkatmu, sayang."
            v "Saya mencintaimu karena mendukung saya dalam setiap keputusan yang saya buat. Bahkan jika itu bukan yang terbaik, haha."
            v "Saya hanya tidak ingin menjadi ibu rumah tangga standar dan tinggal di rumah sepanjang hari tidak melakukan apa -apa."
        else:


            scene 370
            v "Ya, saya minta maaf karena terlalu lama di kamar mandi."
            scene 371
            jeff "Jangan khawatir, sayang."
            if get_back_to_the_kitchen == "1":
                jeff "Kira kamu benar -benar kotor saat itu, hehe."
                scene 374
                vt "Astaga. Saya tidak percaya dia mengatakan itu."
                vt "Tepat di depan semua orang."
                vt "Apa yang dia pikirkan?"
                vt "Apakah dia mencoba membuatku malu?"
                scene 376
                mct "Hm, apa yang dia katakan padanya?"
                mct "[violet] tampaknya sangat malu."
                scene 377
                mct "Mungkin itu bukan ide yang baik untuk membiarkannya sendirian di sana bersama Jeff."
            if open_the_door and allow_him_to_jerk_off == "1":
                jeff "Kira kamu benar -benar kotor saat itu, hehe."
                scene 374
                vt "Astaga. Saya tidak percaya dia mengatakan itu."
                vt "Tepat di depan semua orang."
                vt "Apa yang dia pikirkan?"
                vt "Apakah dia mencoba membuatku malu?"
                scene 376
                mct "Hm, apa yang dia katakan padanya?"
                mct "[violet] tampaknya sangat malu."
                scene 377
                mct "Mungkin itu bukan ide yang baik untuk membiarkannya sendirian di sana bersama Jeff."
                mct "Saya hanya berharap saya tidak mendorongnya terlalu jauh dengan permainan saya."
                scene 378
                amelia "Dimana sopan santun Anda, Jeff?"
                amelia "Apakah Anda pikir lelucon semacam ini sesuai?"
                scene 379
                jeff "Ohh, ayolah itu hanya lelucon, sayang."
                amelia "Ya, oke."
                amelia "Dan bagaimana denganmu? Anda menghilang untuk waktu yang baik."
                amelia "Apa yang kamu lakukan?"
                jeff "Saya baru saja berkeliaran di sekitar rumah, Anda tahu."
                scene 367
                jeff "Maksud saya, [McName] Anda sangat diberkati."
                jeff "Anda memiliki rumah yang indah."
                scene 371
                jeff "Ini memiliki salah satu pandangan terbaik yang pernah saya lihat dalam hidup saya."
                scene 369
                mc "Oh ya, percayalah, saya tahu."
                mct "Motherfucker melakukannya lagi."
                mct "Saya yakin dia tidak berbicara tentang rumah itu."
                scene 376
                mct "Dia hanya mencoba menggoda [Violet]."
                scene 367
                jeff "Ini memiliki banyak ruang juga."
                jeff "Ini cantik __tag_0__big one__tag_1__, tidakkah Anda berpikir [violet]?"
                scene 371
                ""
                scene 374
                v "Hm, w-apa? Apa yang kamu katakan? Maaf, saya sedikit terganggu."
                scene 371
                jeff "Saya hanya bertanya bagaimana menurut Anda?"
                jeff "Tidakkah Anda pikir itu __tag_0__big one__tag_1__?"
                scene 370
                vt "Itu dia lagi mencoba untuk mendapatkan reaksi dari saya."
                vt "Mengapa saya membiarkan ini membuat saya malu?"
                vt "Apa yang terjadi dengan semua kepercayaan yang saya miliki beberapa saat yang lalu?"
                vt "Saya tidak bisa membiarkan dia sampai ke saya."
                scene 380
                vt "Itu saja."
                vt "Saya tidak akan membiarkan dia menggodaku seperti ini."
                vt "Akulah yang melakukan menggoda."
                scene 381
                v "Sejujurnya, Jeff ..."
                v "Saya telah melihat __tag_0__bigger__tag_1__."
                scene 383
                mct "Wow, dia tidak terlihat begitu pemalu lagi!"
                mct "Itulah kepercayaan diri yang saya harapkan darinya."
                scene 382
                mct "Lihat wajahnya, hahaha."
                mct "Dia menempatkannya di tempatnya."
                scene 372
                amelia "Yah, itu terlihat cukup besar bagi saya, tapi oke."
                scene 385
                play sound girlsmirk 
                mcandv "* Berbisik* hehehe."
        scene 372
        amelia "Bagaimanapun ... Katakan padaku, sayang."
        amelia "Apa rencana Anda setelah Anda sepenuhnya diselesaikan?"
        scene 375
        v "Yah, saya belum tahu."
        v "Saya pikir saya akan mencari pekerjaan sesegera mungkin."
        v "[McName] sedang mengurus semuanya sekarang, tetapi saya benar -benar ingin bekerja."
        scene 384
        mc "Saya mengatakan kepadanya untuk tidak khawatir tentang itu, tetapi dia bersikeras."
        mc "Jika dia benar -benar ingin mencari pekerjaan, maka saya tidak menentangnya."
        scene 385
        mc "Saya hanya ingin menjadikannya wanita paling bahagia hidup."
        v "Sendiri, aku sudah menjadi wanita paling bahagia yang hidup berkatmu, sayang."
        v "Saya mencintaimu karena mendukung saya dalam setiap keputusan yang saya buat, bahkan jika kadang -kadang itu bukan yang terbaik, haha."
        v "Saya hanya tidak ingin menjadi ibu rumah tangga standar dan tinggal di rumah sepanjang hari tidak melakukan apa -apa."
        scene 372
        amelia "Oh, aku benar -benar mendapatkanmu, sayang."
        scene 378
        amelia "Anda melihat bagaimana Anda seharusnya memperlakukan seorang wanita?"
        jeff "Ya, tentu. Anda dapat bekerja juga jika Anda mau."
        amelia "Saya tidak membicarakan hal itu, Anda bodoh."
        scene 379
        jeff "Lalu apa itu?"
        amelia "Saya berbicara tentang bagaimana mereka berbicara satu sama lain."
        amelia "Uhmph ... Nevermind."
        amelia "Kami akan berbicara di rumah ..."
        scene 386
        jefft "Sial, apa yang saya lakukan?"
        jefft "Maksudku ... aku melakukan beberapa hal, tapi kurasa dia tidak tahu ..."
        scene 387
        play sound phonevibrating volume 1.5
        ""
        scene 386
        if let_him_finish == "1":
            jefft "Terima kasih Tuhan, diselamatkan oleh bel."
            scene 367
            jeff "Oh, sepertinya [McName] sedang sibuk sekarang."
            jeff "Saya pikir sudah waktunya bagi kita untuk pergi, sayang."
            scene 369
            mc "Jangan konyol. Saya bisa menjawab nanti, tidak masalah."
            mc "Dan Anda bahkan tidak menyelesaikan piring Anda."
            scene 367
            jeff "Ya, tapi percayalah ..."
            scene 371
            jeff "Saya sudah sepenuhnya puas!"
            scene 380
            vt "Saya melihat dia tidak akan berhenti."
            vt "Oke, jika itu yang dia inginkan ... dua bisa memainkan game itu."
            scene 381
            v "Nah, Jeff. Mungkin Anda hanya punya terlalu banyak makanan di piring Anda dan Anda tidak bisa mengambilnya."
            scene 388
            jeff "Huh, jika Anda mengatakannya, mungkin lain kali saya tidak akan membiarkan apa pun menjadi sia -sia ..."
            scene 383
            mct "Menyerah, Jeff. Anda tidak akan membuatnya tidak nyaman lagi."
            scene 378
            amelia "Baiklah, sayang. Jika Anda ingin pergi, ayo pergi."
        else:
            jefft "Terima kasih Tuhan, diselamatkan oleh bel."
            scene 367
            jeff "Oh, sepertinya [McName] sedang sibuk sekarang."
            jeff "Saya pikir sudah waktunya bagi kita untuk pergi, sayang."
            scene 369
            mc "Jangan konyol. Saya bisa menjawab nanti, tidak masalah."
            mc "Dan Anda bahkan tidak menyelesaikan piring Anda."
            scene 367
            jeff "Ya tapi, saya sudah kenyang."
            scene 378
            amelia "Baiklah, sayang. Jika Anda ingin pergi, ayo pergi."

        scene 368
        amelia "Terima kasih telah memiliki kami di rumah Anda."
        amelia "Makan malamnya enak. Tentu saja saya melakukan sebagian besar, tapi tetap saja."
        scene 372
        amelia "Dan saya harap Anda menemukan pekerjaan yang hebat di sini, sayang."
        amelia "Saya sangat senang untuk kalian!"
        scene 384
        mc "Terima kasih. Kami sangat senang tinggal dekat dengan Anda sekarang."
        mc "Anda bisa datang kapan saja Anda membutuhkan."
        scene 385
        mc "Dan saya yakin kita akan bersenang -senang di sini."
        v "Saya setuju!"
        scene blackscreen
        pause 1.0
        scene 392
        jeff "Selamat malam untuk kalian!"
        amelia "Selamat tinggal, sayang."
        play sound carlocking
        v "Sampai jumpa, sampai jumpa!"
        v "Berkendara aman."
        play sound cardoorclose
        mc "Hati-hati di jalan!"
        v "Itu dia."
        v "Senang melihat ibuku lagi setelah begitu banyak waktu."
        mc "Ya, kalian berdua akan punya banyak waktu untuk mengejar ketinggalan sekarang kita hidup dekat satu sama lain."
        v "Saya suka itu!"
        v "Sekarang..."
        scene 393
        v "Aku akan membutuhkanmu untuk melakukan sesuatu untukku."
        mc "Ya? Apa yang kamu butuhkan?"
        v "Semua yang menggoda dan bermain membuatku begitu basah, sayang."
        v "Aku membutuhkanmu di tempat tidur sekarang jadi aku bisa mengendaraimu seperti tidak ada hari esok."
        mc "Wow, begitu saja, ya?"
        v "Sama seperti itu."
        mc "Anda bahkan tidak perlu bertanya kepada saya dua kali."
        mc "Pimpin! Aku tepat di belakangmu."
        scene blackscreen
        stop music
        pause 1.0
        play music sexmusic3 fadein 0.5 volume 0.5
        scene 397
        v "Apakah kamu siap, sayang?"
        scene 396
        mc "Oh ya! Sooo Siap!"
        v "Aku akan mengendarai ayam itu sekarang. Jangan berani -berani bergerak!"
        mc "Aku milikmu."
        v "Itulah yang ingin saya dengar."
        play sound fucking4 loop
        scene ridingnewroom1
        ""
        v "Ohh yess, sial sayang."
        v "Anda tidak tahu betapa saya membutuhkan ini."
        mc "Oh, aku bisa melihat betapa basahnya kamu dengan cara penisku tergelincir ke dalam dirimu dengan mudah."
        scene ridingnewroom2
        v "Ya, saya sangat basah."
        v "Saya seperti ini sejak saya meninggalkan kamar mandi."
        if get_back_to_the_kitchen == "1":
            mct "Sial, aku masih tidak tahu apa yang terjadi di sana ..."
        scene ridingnewroom3
        v "Tidak, saya seperti ini sejak pagi ini ketika kami tidak selesai."
        v "Peristiwa baru -baru ini membuat saya lebih basah dan lebih basah."
        scene ridingnewroom1
        v "Saya tidak tahu apa yang terjadi dengan kami, yang saya tahu bahwa saya tidak ingin berhenti."
        v "Saya belum pernah basah sebelumnya."
        scene ridingnewroom2
        v "Ini adalah seks terbaik yang pernah kami miliki!"
        if get_back_to_the_kitchen == "1":
            mct "Apa yang dia maksud dengan itu?"
        else:
            mc "Saya setuju! Ayamku sangat keras sekarang, sayang."
        scene ridingnewroom3
        v "Ya, persetan dengan ayam yang keras itu!"
        v "Persetan denganku lebih cepat, sayang! Berikan padaku!"
        mc "Oke! Anda memintanya!"
        play sound fuckingfast fadein 2.0 loop
        scene ridingnewroom1fast
        play audio orgasm1 volume 1.5
        v "Ahhhhhmmmmm. Ya Tuhan, aku baru saja datang pada kemaluanmu, sayang!"
        mc "Itu yang Anda inginkan, bukan?"
        scene ridingnewroom2fast
        v "Itulah yang saya inginkan !!"
        v "Tolong, jangan berhenti!"
        v "Aku ingin cum di kemaluanmu lagi!"
        scene ridingnewroom3fast
        mc "Oh sayang, saya ingin cum juga!"
        v "Jangan berhenti, jangan berhenti!"
        scene ridingnewroom1fast
        v "Cum di dalam diriku!"
        v "Saya ingin merasakannya di dalam diri saya."
        scene ridingnewroom2fast
        mc "Apakah kamu yakin, sayang?"
        v "YA, LAKUKANLAH!"
        scene ridingnewroom3fast
        v "AKU AKAN CUM LAGI !!"
        mc "Oh ya? Oke sayang, mari kita bersama."
        mc "AKU CUMMING DI DALAM DIRIMU !!"
        stop sound 
        play sound guycum2
        play audio orgasm1 volume 1.5
        scene 400
        pause 0.3
        scene 401
        pause 0.3
        scene 400
        pause 0.3
        scene 401
        pause 0.3
        scene 400
        pause 0.4
        scene 401
        pause 0.4
        scene 402
        play audio cumbody
        pause 0.3
        play audio cumbody
        play sound relieve
        scene 394
        play audio ohmygod volume 2.5
        ""
        v "Sial, sayang. Itu sangat banyak cum."
        stop music
        play sound girlsmirknaughty
        scene 397
        play music bedroomsound
        v "Anda memenuhi saya dengan baik."
        scene 396
        mc "Nah, saya memegangnya sejak pagi ini, ingat?"
        scene 397
        v "Ya, saya ingat, tapi tahu saya harus mandi lagi, haha."
        mc "Silakan, saya akan menunggumu di sini."
        v "Oke, segera kembali!"
        scene 426
        v "Cobalah untuk tidak terlalu merindukanku."
        mc "Saya akan mencoba, haha."
        scene 389
        mct "Sobat, aku pria paling beruntung yang masih hidup!"
        mct "[Violet] sangat seksi, saya harus mengambil foto itu."
        scene 426
        show 429
        show phonephoto
        ""
        show phoneflash with Dissolve(0.1)
        play sound photoshootcellphone
        hide phoneflash
        hide phonephoto
        scene blackscreen
        show 429
        mct "Sangat bagus!"
        scene 428
        mct "Oh benar, itu mengingatkan saya bahwa saya harus memeriksa pesan dari sebelumnya."
        scene 427
        mct "Mari kita lihat."
        unknown_nvl "Hey [mcname], what's up man? How you doing?{image=emoji/wave.png}"
        mc_nvl "Hm ... aku baik -baik saja."
        mc_nvl "Bagaimana denganmu, Tuan ...?"
        unknown_nvl "Oh maaf, ini aku, Lee."
        unknown_nvl "Saya telah mengubah nomor saya."
        mc_nvl "Lee ?? Wow, sudah lama, bung."
        mc_nvl "Tunggu, izinkan saya menyimpan nomor Anda."
        nvl_narrator "Menambahkan Lee ke Kontak"
        mc_nvl "Selesai."
        mc_nvl "Jadi katakan padaku bung, ada apa? Aku belum melihatmu sejak kuliah"
        lee_nvl "Aku tahu. Anda ingat saya sudah pindah ke Jepang untuk bekerja?"
        mc_nvl "Ya, tentu. Bagaimana kabarmu?"
        lee_nvl "Pekerjaan itu, saya benci. Tempatnya, luar biasa!"
        lee_nvl "Itulah mengapa saya mengirimi Anda pesan, bung."
        lee_nvl "Saya kembali."
        lee_nvl "Dan dengarkan ini."
        lee_nvl "Anda tidak akan mempercayai saya, tetapi saya tidak akan datang sendiri ..."
        lee_nvl "... Saya menemukan pacar!"
        mc_nvl "What? You're right, I don't believe you {image=emoji/laugh.png}."
        lee_nvl "itu benar, bung!"
        mc_nvl "Nah, maaf karena meragukanmu tapi ..."
        mc_nvl "Kembali ke perguruan tinggi, Anda selalu mengatakan Anda menemukan pacar setiap bulan atau lebih."
        mc_nvl "Dan setiap kali Anda berbaring karena Anda malu menjadi satu -satunya perawan dalam kelompok."
        mc_nvl "Saya selalu mengatakan kepada Anda untuk tidak mengkhawatirkannya."
        mc_nvl "Tidak ada yang salah untuk menjadi perawan di perguruan tinggi."
        mc_nvl "Kebanyakan pria juga."
        lee_nvl "Ya, saya tahu ... saya tahu."
        lee_nvl "Anda tidak perlu mengingatkan saya tentang itu ..."
        lee_nvl "Tapi kali ini saya mengatakan yang benar, percayalah."
        mc_nvl "Oke, biarkan aku melihat fotonya kalau begitu."
        lee_nvl "Gambar? ..."
        lee_nvl "Hm ... Saya tidak tahu apakah saya bisa."
        mc_nvl "Yeah, for sure you can't, cuz she doesn't exist! {image=emoji/laugh.png}."
        lee_nvl "Ayo pria, bukan itu."
        lee_nvl "Hanya saja ... saya hanya punya satu fotonya yang dia kirimkan kepada saya."
        mc_nvl "Yah, saya tidak melihat masalahnya."
        mc_nvl "Kirimkan kepada saya kalau begitu."
        mc_nvl "Kecuali..."
        lee_nvl "Bagus!"
        lee_nvl "Ini dia ..."
        lee_nvl "__tag_0__"
        show 430
        nvl_narrator ""
        hide 430
        scene 431
        mct "WTF ??"
        mct "Dia gila!"
        mct "Saya tidak percaya dia mengirimi saya telanjang pacarnya."
        mct "Sial, aku tidak percaya dia benar -benar __tag_0__have__tag_1__ seorang pacar."
        show 430
        mct "Dan itu ... dia seksi!"
        mct "Sangat seksi!"
        mct "Lihat saja payudaranya."
        hide 430
        mc_nvl "Sial, kawan!"
        mc_nvl "Tidak percaya Anda mengirimi saya ini!"
        lee_nvl "Nah, apakah kamu percaya padaku sekarang?"
        mc_nvl "Sial, saya lakukan."
        mc_nvl "Anda benar -benar punya pacar saat ini."
        mc_nvl "Dan yang panas, jangan tersinggung."
        lee_nvl "Jangan khawatir, saya tidak."
        lee_nvl "Dia memang seksi seperti bercinta!"
        lee_nvl "Saya masih tidak tahu bagaimana saya mendapatkannya."
        lee_nvl "Kami adalah kebalikan satu sama lain."
        lee_nvl "As you can see, she's not shy at all. {image=emoji/sweat.png}"
        lee_nvl "Dia terus mendorong saya untuk melakukan banyak hal gila yang belum pernah saya lakukan sebelum bertemu dengannya."
        mc_nvl "Barang gila?"
        mc_nvl "Seperti apa?"
        lee_nvl "Seperti ... mengirimi Anda telanjang."
        mc_nvl "Apa??"
        lee_nvl "Ya, saya bertanya apakah saya harus mengirimkannya kepada Anda dan dia menyuruh saya melakukannya."
        lee_nvl "Dia sedikit eksibisionis."
        lee_nvl "Saya tidak berharap Anda mengerti tapi ... saya agak menyukainya."
        $ ones_count = sum([1 for choice in [keep_fucking_violet, dont_move, embrace_feelings, park_photos, let_him_keep_looking, open_the_door, show_you_are_okay] if choice == "1"])
        if ones_count >= 2:
            scene 434
            mct "Hmm, saya agak ..."
            mct "Siapa saya untuk menghakiminya."
        else:
            scene 432
            mct "Hmm, ya, saya tidak ..."
        scene 427
        lee_nvl "Omong-omong..."
        lee_nvl "Bagaimana denganmu?"
        lee_nvl "Apakah Anda masih berkencan dengan gadis itu, hm ... siapa namanya? Vicky? Valerie?"
        mc_nvl "Namanya [Violet]."
        mc_nvl "Dan tidak, aku tidak lagi berkencan dengannya ..."
        mc_nvl "... Saya benar -benar menikahinya."
        lee_nvl "Whaaaaat? You're married?? {image=emoji/fear.png}"
        lee_nvl "Bung, kenapa kamu melakukan itu?"
        lee_nvl "Anda masih terlalu muda untuk itu."
        lee_nvl "Dan Anda bahkan tidak mengundang saya ke pernikahan?"
        lee_nvl "Lebih buruk lagi, Anda tidak mengundang saya ke pesta bujangan!"
        mc_nvl "Apakah Anda bercanda?"
        mc_nvl "Tentu saja saya mencoba mengundang Anda."
        mc_nvl "Saya ingin Anda menjadi pria terbaik saya."
        mc_nvl "Aku memanggilmu seratus kali. (Sekarang saya tahu Anda tidak memiliki nomor itu lagi)."
        mc_nvl "Jadi secara teknis salah Anda."
        mc_nvl "Dan saya bahkan tidak mengadakan pesta bujangan, bung."
        lee_nvl "Sialan!"
        lee_nvl "Anda agak benar, tho."
        lee_nvl "Jadi hei? Ini [Violet] ... apakah dia seksi?"
        lee_nvl "Kirimkan saya fotonya. Saya belum pernah melihatnya ... bagaimana saya tahu dia bukan penemuan Anda."
        mc_nvl "WTF Bung!"
        lee_nvl "Apa? Itu adil. Saya mengirimi Anda foto pacar saya."
        lee_nvl "Dan itu telanjang!"
        mc_nvl "Sial, oke ... oke."
        mc_nvl "Saya akan mengirimkan fotonya."
        mc_nvl "Tunggu sebentar."
        scene 434
        mct "Oke, gambar mana yang harus saya kirimkan padanya?"
        menu:
            "Gambar normal":
                $ normal_picture = "1"
                $ return_the_favor = "2"
                scene 427
                mct "Saya akan mengirimkan yang ini."
                mc_nvl "__tag_0__"
                show 173
                nvl_narrator ""
                hide 173
                lee_nvl "Bagus, bung. Dia sangat imut."
                lee_nvl "Anda pria yang beruntung."
                lee_nvl "Tidak sabar untuk bertemu dengannya!"
            "Membalas budi":


                $ return_the_favor = "1"
                $ normal_picture = "2"
                mct "Maksudku, dia mengirimi aku yang cukup bagus, kira aku harus membalas budi."
                mct "Tapi itu langkah yang cukup besar bagi saya. Saya harus memikirkan hal ini."
                mct "Saya akan memberi tahu seseorang yang saya kenal untuk waktu yang lama, sahabat saya, melihat istri saya sama sekali."
                mct "Tidak ada jalan kembali dari sana."
                mct "Tapi bercinta, penisku menjadi keras hanya dengan memikirkannya."
                scene 427
                mct "Anda tahu apa, persetan! Aku akan melakukannya!"
                scene 433
                mct "Dan saya tahu persis mana yang harus dipilih."
                mct "Mari kita lihat bagaimana dia bereaksi."
                mc_nvl "Oke bung, kamu pantas mendapatkannya."
                mc_nvl "Saya akan mengirimkan foto yang baru saja saya ambil darinya."
                mc_nvl "Anda akan menyukainya ..."
                mc "Ini dia."


    jump ep3
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
