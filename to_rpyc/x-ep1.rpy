label start:
    stop music fadeout 3.0
    menu:
        "Ya, saya berusia 18 tahun atau lebih.":
            narrador "Nikmati ceritanya!"
        "Tidak, saya di bawah 18.":

            return



    $ mcname = renpy.input("Enter your name (Default \"Ted\")")

    $ mcname = mcname.strip()

    if mcname == "":
        $ mcname = "Ted"

    $ violet = renpy.input("Enter your Wife's name (Default \"Violet\")")

    $ violet = violet.strip()

    if violet == "":
        $ violet = "Ungu"

    centered "__Tag_0____tag_1__ untuk pengalaman yang lebih baik mainkan game ini dengan suara dihidupkan .__ tag_2____tag_3__"
    scene 2
    play music romanticmusic fadein 2.0 volume 0.2
    mct "Di sini saya dengan istri tercinta saya [Violet] mencari rumah baru."
    mct "Kami telah menikah selama 3 tahun tinggal di apartemen dan menabung."
    mct "Dan sekarang, akhirnya kami dapat membeli rumah impian kami di lingkungan yang baik."
    scene 1a
    mct "Setelah melihat -lihat banyak rumah, kami akhirnya menemukan yang sempurna untuk kami."
    mct "Itu bagus sekali!"
    scene 1
    mct "Dan lingkungannya terlihat bagus."
    mct "Lingkungan yang cukup tenang dan dingin."
    mct "Kami belum bertemu tetangga mana pun, tapi saya yakin mereka akan mencintai kami!"
    scene 3
    mct "Kami bahkan memiliki kolam renang!"
    mct "Siapa yang tidak suka itu?"
    scene 11
    mct "Dilihat dari penampilan mereka, mereka tampak seperti pasangan yang baik."
    mct "Setelah kami ditampung di dalam, kami bisa bertemu mereka."
    scene 12
    mct "Saya menantikannya."
    mct "Tetangga tua kami semuanya tua dan pemarah."
    mct "Harus menyenangkan memiliki tetangga pada kelompok usia yang sama dengan kita."
    mct "Tidak sabar untuk memulai cerita kami di sini!"
    stop music fadeout 2.0
    scene blackscreen
    pause 0.5
    scene 4
    play music neighborhood fadein 1.5 volume 0.5
    vt "Ini sangat besar, betapa beruntungnya kami!"
    vt "Rumah itu pasti mahal ..."
    vt "Saya berharap dia tidak menghabiskan terlalu banyak."
    v "Ya Tuhan sayang, aku suka di sini."
    v "Ibuku akan menyukai ini, kami memiliki kolam renang!"
    v "Kami tidak membutuhkan rumah yang begitu besar, Anda tahu saya senang tinggal di apartemen lama."
    v "Tapi saya sangat senang kami pindah ke sini."
    v "Kami akan sangat bahagia hidup di sini, saya merasakannya!"
    v "Rumah kami sempurna! Aku sangat mencintaimu!"
    scene 5
    mc "Aku juga mencintaimu sayang"
    mc "Saya sangat senang kami ada di sini sekarang"
    mc "Jangan terlalu khawatir, saya hanya ingin memberikan hal terbaik untuk Anda!"
    mc "Saya tidak sabar untuk menunjukkan kepada Anda setiap kamar!"
    scene 6
    v "Oh ya? Anda ingin menunjukkan kepada saya?"
    v "Mengapa Anda tidak menunjukkan kepada saya betapa Anda mencintaiku sementara kami menguji kamar tidur kami sebelum kami bertemu tetangga?"


    menu:
        "Tentu saja saya akan menunjukkan kepada Anda!":
            $ show_her = "1"
            scene 5
            mc "Aku akan menunjukkan lebih dari sekadar sayang itu."
            mc "Mari saya antar."
            stop music
            scene 17
            play sound dooropen1 volume 0.3
            v "Wow!"
            play sound dress volume 0.3
            v "Saya belum pernah melihat Anda menanggalkan pakaian begitu cepat."
            mc "Aku tidak sabar untuk bercinta denganmu!"
            mc "Ayo. Ayo masuk ke dalam."
            stop sound
            scene 14
            play music sexmusic fadein 3.0 volume 0.1
            v "Sepertinya seseorang siap untuk pergi."
            mc "Kamu sangat seksi sayang sehingga tidak mungkin untuk tidak segera menjadi keras!"
            mc "Lompat di tempat tidur. Lihat apakah Anda menyukainya."
            scene 15
            v "Hummm. Comfy!"
            v "Aku menyukainya!"
            mc "Dari sudut ini, ia juga terlihat mengundang."
            scene 7
            v "Apakah ini cukup mengundang untuk Anda?"
            mc "Sial, aku tidak berpikir aku bisa menjadi lebih sulit."
            v "Aku sangat terangsang sekarang!"
            v "Ayo. Jangan membuatku menunggu."
            v "Saya sudah basah."
            scene 8
            mc "Anda menginginkan ini, ya?"
            v "Jangan menggodaku!"
            v "Tolong, masukkan."
            mc "Katakan padaku betapa kamu menginginkan penisku di dalam dirimu sekarang."
            v "Oh, kamu tidak tahu. Aku membutuhkan penismu di dalam diriku sekarang atau aku akan gila."
            mc "Ya? Ini dia!"
            scene 9
            play sound moan1
            v "ASTAGA!"
            v "Hmmmmm ... itu saja."
            scene 18
            play sound fucking1 loop
            mc "Kamu sangat kencang sayang."
            v "Persetan denganku!"
            v "Sama seperti itu."
            scene 27
            v "Ya! Persetan denganku!"
            scene dogstyle1
            pause 9.0
            v "Kamu bercinta denganku sangat bagus."
            v "Saya di surga sekarang."
            mc "Anda seperti itu, jangan Anda, Anda minx kecil."
            stop sound
            scene 10
            v "Ohh ya, izinkan saya menunjukkan apa yang bisa dilakukan minx kecil ini."
            v "Biarkan saya menjadi yang teratas."
            scene 13
            v "Sekarang berbaring saja dan nikmati."
            v "Aku akan keluar darimu!"
            scene 16
            mc "WOW!"
            v "Menikmati!"
            scene riding1
            play sound fucking1 loop
            pause 9.0
            mc "Sial, apa yang kamu lakukan padaku?"
            v "Saya menunjukkan apa yang bisa saya lakukan."
            mc "Oh ya! Anda pasti dapat melakukan banyak hal!"
            mc "Jika Anda mempertahankan ini, saya akan cum dalam waktu singkat."
            stop sound fadeout 1.5
            scene 16
            mc "Tunggu. Biarkan saya menjadi lebih nyaman."
            scene 19
            mc "Baiklah, beri aku semua yang kamu punya!"
            v "Apakah Anda cukup nyaman sekarang?"
            mc "Oh ya pasti."
            scene 20
            mct "Bersenandung? Apa itu di jendela?"
            mct "Apakah seseorang disana?"
            scene 21
            play sound disco volume 0.3
            stop music
            mct "WTF!"
            mct "Ada creep tua yang menonton kami berhubungan seks!"
            scene 22
            ht "Apakah ini pasangan yang akan pindah ke rumah itu?"
            ht "Sungguh keren. Pria itu beruntung seperti bercinta!"
            scene 23
            ht "Saya kira saya juga cukup beruntung."
            ht "Saya bisa melihat acara ini dari sini."
            ht "Gadis itu liar! Lihatlah dia memantul pada penis itu."
            play sound heartbeatslow volume 0.5 loop
            scene 24
            mct "Apa yang harus saya lakukan sekarang?"


            menu:
                "Terus [Violet]":
                    $ keep_fucking_violet = "1"
                    $ stop_this_right_now = "2"
                    stop sound
                    scene 25
                    play music sexmusic fadein 3.0 volume 0.1
                    mct "Biarkan dia melihat semua yang dia inginkan."
                    mct "Dia hanya seorang pria tua!"
                    scene 26
                    mct "Ya Tuhan, itu sangat panas!"
                    mct "Saya yakin dia cemburu sekarang."
                    mct "Ingin berada di tempat saya."
                    play sound fucking1 loop
                    scene riding2
                    pause 9.0
                    mct "Tidak percaya saya melakukan ini!"
                    mct "Saya pasti sakit."
                    mct "Tapi pemandangan yang indah."
                    v "Itu dia sayang!"
                    v "Pertahankan ini dan aku akan cum!"
                    v "ASTAGA"
                    show riding2 with flash
                    $ renpy.pause(0.3)
                    v "SAYA CUMMIIIIINGGG !!"
                    show riding2 with flash
                    $ renpy.pause(0.3)
                    stop sound
                    play sound moan2
                    show a3_2 with flash
                    $ renpy.pause(0.1)
                    show riding2
                    pause 0.1
                    show a3_2 with flash
                    $ renpy.pause(0.3)
                    v "YEEEEES!"
                    v "Itu sempurna!"
                    scene 28
                    v "Saya datang sangat keras!"
                    v "Kamu bercinta denganku sangat baik sayang."
                    scene 29
                    v "Itu saja!"
                    v "Membuat saya cum lagi."
                    scene 30
                    vt "Bersenandung?"
                    vt "Apa itu ..."
                    scene 31
                    stop music
                    play sound chockfemale volume 0.3
                    v "[McName] Berhenti!"
                    v "Ada orang cabul yang menatap kami melalui jendela!"


                    menu:
                        "Cobalah menenangkannya":
                            scene 32
                            mc "Santai sayang, itu adil dan orang tua."
                            v "Apakah kamu gila ??"
                            v "Kamu sakit!"
                            v "Biarkan aku pergi!"
                            v "Aku keluar!"
                            play music sadmusic
                            scene blackscreen
                            mct "Setelah itu, [Violet] mengambil barang -barangnya dan pergi ke rumah ibunya."
                            mct "Jika mungkin saya mengambil hal -hal yang sedikit lebih lambat dengannya, bayangkan kehidupan yang bisa kita jalani."
                            narrador "Cobalah untuk kembali dan mengambil hal -hal lebih lambat."
                            stop music
                            scene 31
                            menu:
                                "BANGUN DAN LAKUKAN SESUATU!":
                                    scene 33
                                    play music tense fadein 3.0 volume 0.2
                                    mct "Kira aku harus berpura -pura marah."
                                    mc "Persetan!"
                                    v "Kami lupa menutup tirai."
                                    scene 34
                                    v "TUTUP DENGAN CEPAT!"
                                    mc "Aku di atasnya!"
                                    mc "Selamat tinggal creep."
                                    scene 35
                                    ht "Sial, mereka melihatku!"
                                    ht "Baiklah, tebak pertunjukannya sudah berakhir."
                                    ht "Pria itu sepertinya tahu aku sedang mencari jauh sebelum mereka berhenti."
                                    ht "Atau mungkin saya hanya melihat sesuatu."
                                    ht "Apa pun."
                                    ht "Saya kira saya harus menemukan alasan ketika mereka menghadapi saya ..."
                                    scene 36
                                    mc "Betapa anehnya kuno."
                                    mc "Aku akan mengajarinya pelajaran saat kita melihatnya."
                                    v "Aku tidak percaya dia melihatku telanjang."
                                    v "Saya masih terkejut!"
                                    stop music fadeout 1.5
                                    scene 37
                                    mc "Ya. Jadi ... dimana kita?"
                                    v "Apa? Bagaimana Anda masih sulit setelah semua ini?"
                                    v "Maaf tapi saya tidak bisa sekarang."
                                    v "Ayo berpakaian dan keluar."
                                    scene 38
                                    play sound disappointed volume 0.5
                                    mct "Sungguh!"
                                    scene 39
                                    mct "Kotoran!"
                                    scene 40
                                    mc "Oke..."
                                    mc "Ayo pergi."
                                    stop sound
                                    scene blackscreen
                                    pause 0.5
                                    scene time
                                    narrador "Setelah beberapa menit ..."
                        "Bangun dan Lakukan Sesuatu":
                            scene 33
                            play music tense fadein 3.0 volume 0.2
                            mct "Kira aku harus berpura -pura marah."
                            mc "Persetan!"
                            v "Kami lupa menutup tirai."
                            scene 34
                            v "TUTUP DENGAN CEPAT!"
                            mc "Aku di atasnya!"
                            mc "Selamat tinggal creep."
                            scene 35
                            ht "Sial, mereka melihatku!"
                            ht "Baiklah, tebak pertunjukannya sudah berakhir."
                            ht "Pria itu sepertinya tahu aku sedang mencari jauh sebelum mereka berhenti."
                            ht "Atau mungkin saya hanya melihat sesuatu."
                            ht "Apa pun."
                            ht "Saya kira saya harus menemukan alasan ketika mereka menghadapi saya ..."
                            scene 36
                            mc "Betapa anehnya kuno."
                            mc "Aku akan mengajarinya pelajaran saat kita melihatnya."
                            v "Aku tidak percaya dia melihatku telanjang."
                            v "Saya masih terkejut!"
                            stop music fadeout 1.5
                            scene 37
                            mc "Ya. Jadi ... dimana kita?"
                            v "Apa? Bagaimana Anda masih sulit setelah semua ini?"
                            v "Maaf tapi saya tidak bisa sekarang."
                            v "Ayo berpakaian dan keluar."
                            scene 38
                            play sound disappointed volume 0.5
                            mct "Sungguh!"
                            scene 39
                            mct "Kotoran!"
                            scene 40
                            mc "Oke..."
                            mc "Ayo pergi."
                            stop sound
                            scene blackscreen
                            pause 0.5
                            scene time
                            narrador "Setelah beberapa menit ..."
                "Hentikan ini sekarang!":


                    $ stop_this_right_now = "1"
                    $ keep_fucking_violet = "2"
                    stop sound
                    scene 33
                    play music tense fadein 3.0 volume 0.2
                    mc "Ada orang cabul yang menatap kami melalui jendela!"
                    mc "Persetan!"
                    v "Kami lupa menutup tirai."
                    scene 34
                    v "TUTUP DENGAN CEPAT!"
                    mc "Aku di atasnya!"
                    mc "Selamat tinggal creep."
                    scene 35
                    ht "Sial, mereka melihatku!"
                    ht "Baiklah, tebak pertunjukannya sudah berakhir."
                    ht "Saya kira saya harus menemukan alasan ketika mereka menghadapi saya ..."
                    scene 36
                    mc "Betapa anehnya kuno."
                    mc "Aku akan mengajarinya pelajaran saat kita melihatnya."
                    v "Aku tidak percaya dia melihatku telanjang."
                    v "Saya masih terkejut!"
                    stop music fadeout 1.5
                    scene 37
                    mc "Ya. Jadi ... dimana kita?"
                    v "Apa? Bagaimana Anda masih sulit setelah semua ini?"
                    v "Maaf tapi saya tidak bisa sekarang."
                    v "Ayo berpakaian dan keluar."
                    scene 38
                    play sound disappointed volume 0.5
                    mct "Sungguh!"
                    scene 39
                    mct "Kotoran!"
                    scene 40
                    mc "Oke..."
                    mc "Ayo pergi."
                    stop sound
                    scene blackscreen
                    pause 0.5
                    scene time
                    narrador "Setelah beberapa menit ..."
        "Mengapa saya masih berpikir? Pergi bersamanya!":


            $ show_her = "1"
            scene 5
            mc "Aku akan menunjukkan lebih dari sekadar sayang itu."
            mc "Mari saya antar."
            stop music
            scene 17
            play sound dooropen1 volume 0.3
            v "Wow!"
            play sound dress volume 0.3
            v "Saya belum pernah melihat Anda menanggalkan pakaian begitu cepat."
            mc "Aku tidak sabar untuk bercinta denganmu!"
            mc "Ayo. Ayo masuk ke dalam."
            stop sound
            scene 14
            play music sexmusic fadein 3.0 volume 0.1
            v "Sepertinya seseorang siap untuk pergi."
            mc "Kamu sangat seksi sayang sehingga tidak mungkin untuk tidak segera menjadi keras!"
            mc "Lompat di tempat tidur. Lihat apakah Anda menyukainya."
            scene 15
            v "Hummm. Comfy!"
            v "Aku menyukainya!"
            mc "Dari sudut ini, ia juga terlihat mengundang."
            scene 7
            v "Apakah ini cukup mengundang untuk Anda?"
            mc "Sial, aku tidak berpikir aku bisa menjadi lebih sulit."
            v "Aku sangat terangsang sekarang!"
            v "Ayo. Jangan membuatku menunggu."
            v "Saya sudah basah."
            scene 8
            mc "Anda menginginkan ini, ya?"
            v "Jangan menggodaku!"
            v "Tolong, masukkan."
            mc "Katakan padaku betapa kamu menginginkan penisku di dalam dirimu sekarang."
            v "Oh, kamu tidak tahu. Aku membutuhkan penismu di dalam diriku sekarang atau aku akan gila."
            mc "Ya? Ini dia!"
            scene 9
            play sound moan1
            v "ASTAGA!"
            v "Hmmmmm ... itu saja."
            scene 18
            play sound fucking1 loop
            mc "Kamu sangat kencang sayang."
            v "Persetan denganku!"
            v "Sama seperti itu."
            scene 27
            v "Ya! Persetan denganku!"
            scene dogstyle1
            pause 9.0
            v "Kamu bercinta denganku sangat bagus."
            v "Saya di surga sekarang."
            mc "Anda seperti itu, jangan Anda, Anda minx kecil."
            stop sound
            scene 10
            v "Ohh ya, izinkan saya menunjukkan apa yang bisa dilakukan minx kecil ini."
            v "Biarkan saya menjadi yang teratas."
            scene 13
            v "Sekarang berbaring saja dan nikmati."
            v "Aku akan keluar darimu!"
            scene 16
            mc "WOW!"
            v "Menikmati!"
            scene riding1
            play sound fucking1 loop
            pause 9.0
            mc "Sial, apa yang kamu lakukan padaku?"
            v "Saya menunjukkan apa yang bisa saya lakukan."
            mc "Oh ya! Anda pasti dapat melakukan banyak hal!"
            mc "Jika Anda mempertahankan ini, saya akan cum dalam waktu singkat."
            stop sound fadeout 1.5
            scene 16
            mc "Tunggu. Biarkan saya menjadi lebih nyaman."
            scene 19
            mc "Baiklah, beri aku semua yang kamu punya!"
            v "Apakah Anda cukup nyaman sekarang?"
            mc "Oh ya pasti."
            scene 20
            mct "Bersenandung? Apa itu di jendela?"
            mct "Apakah seseorang disana?"
            scene 21
            play sound disco volume 0.3
            stop music
            mct "WTF!"
            mct "Ada creep tua yang menonton kami berhubungan seks!"
            scene 22
            ht "Apakah ini pasangan yang akan pindah ke rumah itu?"
            ht "Sungguh keren. That guy is lucky as fuck!"
            scene 23
            ht "Saya kira saya juga cukup beruntung."
            ht "Saya bisa melihat acara ini dari sini."
            ht "Gadis itu liar! Lihatlah dia memantul pada penis itu."
            play sound heartbeatslow volume 0.5 loop
            scene 24
            mct "Apa yang harus saya lakukan sekarang?"


            menu:
                "Terus [Violet]":
                    $ keep_fucking_violet = "1"
                    $ stop_this_right_now = "2"
                    stop sound
                    scene 25
                    play music sexmusic fadein 3.0 volume 0.1
                    mct "Biarkan dia melihat semua yang dia inginkan."
                    mct "Dia hanya seorang pria tua!"
                    scene 26
                    mct "Ya Tuhan, itu sangat panas!"
                    mct "Saya yakin dia cemburu sekarang."
                    mct "Ingin berada di tempat saya."
                    play sound fucking1 loop
                    scene riding2
                    pause 9.0
                    mct "Tidak percaya saya melakukan ini!"
                    mct "Saya pasti sakit."
                    mct "Tapi pemandangan yang indah."
                    v "Itu dia sayang!"
                    v "Pertahankan ini dan aku akan cum!"
                    v "ASTAGA"
                    show riding2 with flash
                    $ renpy.pause(0.3)
                    v "SAYA CUMMIIIIINGGG !!"
                    show riding2 with flash
                    $ renpy.pause(0.3)
                    stop sound
                    play sound moan2
                    show a3_2 with flash
                    $ renpy.pause(0.1)
                    show riding2
                    pause 0.1
                    show a3_2 with flash
                    $ renpy.pause(0.3)
                    v "YEEEEES!"
                    v "Itu sempurna!"
                    scene 28
                    v "Saya datang sangat keras!"
                    v "Kamu bercinta denganku sangat baik sayang."
                    scene 29
                    v "Itu saja!"
                    v "Membuat saya cum lagi."
                    scene 30
                    vt "Bersenandung?"
                    vt "Apa itu ..."
                    scene 31
                    stop music
                    play sound chockfemale volume 0.3
                    v "[McName] Berhenti!"
                    v "Ada orang cabul yang menatap kami melalui jendela!"


                    menu:
                        "Cobalah menenangkannya":
                            scene 32
                            mc "Santai sayang, itu adil dan orang tua."
                            v "Apakah kamu gila ??"
                            v "Kamu sakit!"
                            v "Biarkan aku pergi!"
                            v "Aku keluar!"
                            play music sadmusic
                            scene blackscreen
                            mct "Setelah itu, [Violet] mengambil barang -barangnya dan pergi ke rumah ibunya."
                            mct "Jika mungkin saya mengambil hal -hal yang sedikit lebih lambat dengannya, bayangkan kehidupan yang bisa kita jalani."
                            narrador "Cobalah untuk kembali dan mengambil hal -hal lebih lambat."
                            stop music
                            scene 31
                            menu:
                                "BANGUN DAN LAKUKAN SESUATU!":
                                    scene 33
                                    play music tense fadein 3.0 volume 0.2
                                    mct "Kira aku harus berpura -pura marah."
                                    mc "Persetan!"
                                    v "Kami lupa menutup tirai."
                                    scene 34
                                    v "TUTUP DENGAN CEPAT!"
                                    mc "Aku di atasnya!"
                                    mc "Selamat tinggal creep."
                                    scene 35
                                    ht "Sial, mereka melihatku!"
                                    ht "Baiklah, tebak pertunjukannya sudah berakhir."
                                    ht "Pria itu sepertinya tahu aku sedang mencari jauh sebelum mereka berhenti."
                                    ht "Atau mungkin saya hanya melihat sesuatu."
                                    ht "Apa pun."
                                    ht "Saya kira saya harus menemukan alasan ketika mereka menghadapi saya ..."
                                    scene 36
                                    mc "Betapa anehnya kuno."
                                    mc "Aku akan mengajarinya pelajaran saat kita melihatnya."
                                    v "Aku tidak percaya dia melihatku telanjang."
                                    v "Saya masih terkejut!"
                                    stop music fadeout 1.5
                                    scene 37
                                    mc "Ya. Jadi ... dimana kita?"
                                    v "Apa? Bagaimana Anda masih sulit setelah semua ini?"
                                    v "Maaf tapi saya tidak bisa sekarang."
                                    v "Ayo berpakaian dan keluar."
                                    scene 38
                                    play sound disappointed volume 0.5
                                    mct "Sungguh!"
                                    scene 39
                                    mct "Kotoran!"
                                    scene 40
                                    mc "Oke..."
                                    mc "Ayo pergi."
                                    stop sound
                                    scene blackscreen
                                    pause 0.5
                                    scene time
                                    narrador "Setelah beberapa menit ..."
                        "Bangun dan Lakukan Sesuatu":
                            scene 33
                            play music tense fadein 3.0 volume 0.2
                            mct "Kira aku harus berpura -pura marah."
                            mc "Persetan!"
                            v "Kami lupa menutup tirai."
                            scene 34
                            v "TUTUP DENGAN CEPAT!"
                            mc "Aku di atasnya!"
                            mc "Selamat tinggal creep."
                            scene 35
                            ht "Sial, mereka melihatku!"
                            ht "Baiklah, tebak pertunjukannya sudah berakhir."
                            ht "Pria itu sepertinya tahu aku sedang mencari jauh sebelum mereka berhenti."
                            ht "Atau mungkin saya hanya melihat sesuatu."
                            ht "Apa pun."
                            ht "Saya kira saya harus menemukan alasan ketika mereka menghadapi saya ..."
                            scene 36
                            mc "Betapa anehnya kuno."
                            mc "Aku akan mengajarinya pelajaran saat kita melihatnya."
                            v "Aku tidak percaya dia melihatku telanjang."
                            v "Saya masih terkejut!"
                            stop music fadeout 1.5
                            scene 37
                            mc "Ya. Jadi ... dimana kita?"
                            v "Apa? Bagaimana Anda masih sulit setelah semua ini?"
                            v "Maaf tapi saya tidak bisa sekarang."
                            v "Ayo berpakaian dan keluar."
                            scene 38
                            play sound disappointed volume 0.5
                            mct "Sungguh!"
                            scene 39
                            mct "Kotoran!"
                            scene 40
                            mc "Oke..."
                            mc "Ayo pergi."
                            stop sound
                            scene blackscreen
                            pause 0.5
                            scene time
                            narrador "Setelah beberapa menit ..."
                "Hentikan ini sekarang!":


                    $ stop_this_right_now = "1"
                    $ keep_fucking_violet = "2"
                    stop sound
                    scene 33
                    play music tense fadein 3.0 volume 0.2
                    mc "Ada orang cabul yang menatap kami melalui jendela!"
                    mc "Persetan!"
                    v "Kami lupa menutup tirai."
                    scene 34
                    v "TUTUP DENGAN CEPAT!"
                    mc "Aku di atasnya!"
                    mc "Selamat tinggal creep."
                    scene 35
                    ht "Sial, mereka melihatku!"
                    ht "Baiklah, tebak pertunjukannya sudah berakhir."
                    ht "Saya kira saya harus menemukan alasan ketika mereka menghadapi saya ..."
                    scene 36
                    mc "Betapa anehnya kuno."
                    mc "Aku akan mengajarinya pelajaran saat kita melihatnya."
                    v "Aku tidak percaya dia melihatku telanjang."
                    v "Saya masih terkejut!"
                    stop music fadeout 1.5
                    scene 37
                    mc "Ya. Jadi ... dimana kita?"
                    v "Apa? Bagaimana Anda masih sulit setelah semua ini?"
                    v "Maaf tapi saya tidak bisa sekarang."
                    v "Ayo berpakaian dan keluar."
                    scene 38
                    play sound disappointed volume 0.5
                    mct "Sungguh!"
                    scene 39
                    mct "Kotoran!"
                    scene 40
                    mc "Oke..."
                    mc "Ayo pergi."
                    stop sound
                    scene blackscreen
                    pause 0.5
                    scene time
                    narrador "Setelah beberapa menit ..."

    scene 42
    play music neighborhood fadein 1.5 volume 0.5
    v "Oke, kami siap bertemu semua orang sekarang."
    v "Dan jangan lupa ibuku akan datang dengan suaminya yang baru untuk melihat rumah baru kita malam ini!"
    mc "Saya tidak akan."
    mc "Ayo pergi."
    scene blackscreen
    pause 0.5
    scene 43
    v "Halo, apa kabar?"
    v "Saya [Violet] dan ini adalah suami saya [McName]."
    v "Kami baru saja pindah ke rumah di sebelahmu."
    v "Kami adalah tetangga sekarang."
    scene 44
    mel "Oh hai! Senang berkenalan dengan Anda."
    mel "Pasangan yang cantik."
    mel "Saya Melanie, tetapi Anda bisa memanggil saya Mel."
    mike "Dan saya Michael, tetapi Anda dapat memanggil saya apa pun yang Anda inginkan."
    scene 45
    mel "Anda tidak mungkin!"
    mel "Horndog seperti itu."
    mike "Aku hanya bercanda dengan santai madu."
    mike "Kalian bisa memanggilku Mike."
    mike "Anda memiliki istri yang sangat cantik [McName]."
    scene 46
    mc "Terima kasih, dia benar -benar. Saya pria yang beruntung."
    mc "Tapi saya melihat Anda juga beruntung, istrimu juga cantik."
    mc "Senang bertemu kalian, senang memiliki tetangga dengan kelompok usia yang sama dengan kita."
    scene 47
    mike "Jangan bilang, lingkungan ini terlihat seperti panti jompo."
    mike "Kebanyakan dari mereka sudah tua dan sakit."
    mike "Ada seorang lelaki tua yang tinggal di rumah di sebelah kanan Anda."
    mike "Dia aneh dan membosankan. Sepertinya dia keluar dari film horor."
    mel "Jangan seperti itu madu."
    mel "Kalian ingin masuk?"
    scene 48
    mc "Tidak hari ini terima kasih."
    mc "Kami sebenarnya akan berbicara dengan orang tua itu sekarang."
    mc "Ayo pergi sayang, aku ingin bertemu dengannya."
    v "Apa kamu yakin?"
    mc "Ya tentu saja, ayolah."
    mc "Selamat tinggal, senang bertemu kalian."
    scene 49
    mel "Sampai jumpa, jika kalian membutuhkan sesuatu, jangan takut untuk bertanya kepada kami, oke?"
    mike "Bersenang -senang sekarat akibat kebosanan."
    scene 50
    ht "Sial, mereka datang."
    ht "Saatnya menjalankan rencana saya."
    scene blackscreen
    narrador "..."
    scene 51
    v "Anda tidak perlu terlalu agresif tetapi jangan mudah padanya!"
    v "Dia perlu belajar tidak memata -matai orang di saat -saat paling intim mereka."
    mc "Santai, aku hanya akan sedikit menakut -nakuti dia. Saya tidak akan pernah memukul orang tua."
    mc "Saya bisa melihat dia sudah membuka pintu."
    mc "Bagus, itu menghemat waktu."
    stop music
    scene 52
    play music fightmusic fadein 2.0 volume 0.2
    mc "HEI BRENGSEK."
    mc "ANDA PIKIR KAMI TIDAK MELIHAT APA YANG ANDA LAKUKAN DI SANA?"
    mc "Aku akan merobek matamu sehingga kamu tidak pernah menggunakannya untuk melihat orang berhubungan seks bahkan di interrr ..."
    scene 53
    stop music
    play sound disco volume 0.3
    mc "...bersih."
    stop sound
    scene 54
    play sound chockmale volume 0.5
    mct "Tidak ada jalan sialan!"
    scene 55
    mct "Kami akan langsung ke neraka."
    mct "Saya hanya menghina orang buta."
    scene 56
    ht "Saatnya memenangkan Oscar."
    play music neighborhood fadein 1.5 volume 0.5
    h "Apa yang terjadi? Kebisingan apa itu?"
    h "Apakah seseorang di sana berteriak padaku?"
    scene 57
    mc "Maaf, tidak ... itu orang gila di jalanan."
    mc "Dia pasti bingung ..."
    scene 56
    ht "Hehehe itu berhasil!"
    h "Oh ok, saya mengerti."
    h "Dan siapa kamu?"
    scene 58
    mc "Kami baru saja pindah."
    mc "Saya [McName] dan ini [Violet] istri saya."
    mc "Kami adalah tetangga baru Anda."
    h "Oh, itu bagus, aku herold."
    mc "Saya tahu Anda tidak bisa melihat tetapi saya meraih lengan saya untuk menyambut Anda."
    h "Ah oke."
    scene 59
    h "Di Sini."
    play sound chockfemale
    v "Uhhh."
    scene 60
    h "Anda memiliki tangan yang lembut."
    ht "Itu langkah yang berani, tapi saya perlu mengambil payudara itu."
    scene 61
    v "WTF YANG KAMU LAKUKAN?!"
    v "LEPASKAN AKU!"
    scene 62
    v "ORANG CABUL!"
    scene 63
    v "MENGAMBIL"
    scene 64
    play sound slap volume 0.8
    v "INI!"
    scene 65
    h "ADUH."
    scene 66
    h "AHHH."
    scene 67
    play sound fall1 volume 0.8
    h "UGHH."
    scene 68
    play sound fall2 volume 0.3
    h "Kotoran."
    scene 69
    mc "Sial [Violet], Anda hampir membunuhnya!"
    stop sound
    mct "Sepertinya dia melihat tamparan itu datang."
    v "Saya sangat menyesal saya tidak bermaksud."
    v "Dia meraih ..."
    v "Saya lupa dia buta."
    mc "Bagaimana?!"
    v "Saya tidak berpikir!"
    scene 68
    h "Ahhh, saya pikir lengan saya patah."
    h "Saya tidak bisa memindahkannya."
    scene 70
    v "Astaga!"
    v "Itu bukan niat saya, saya sangat menyesal!"
    mc "Ayo, mari kita bawa dia ke rumah sakit."
    v "Tentu. Anda benar. Ayo pergi!"
    scene blackscreen
    stop music fadeout 1.5
    pause 0.1
    narrador "..."
    scene 71
    play music hospital fadein 1.5 volume 0.3
    v "Saya merasa sangat buruk."
    v "Semoga tidak ada yang terlalu serius."
    mc "Ini akan baik -baik saja sayang, itu hanya jatuh."
    scene 72
    play sound dooropen2 volume 0.6
    nurse "Dia baik -baik saja, hanya sedikit pusing dan dia mematahkan lengan kiri."
    nurse "Kalian bisa masuk sekarang."
    nurse "Saya akan pulang sekarang ini adalah akhir dari shift saya, tetapi perawat lain harus sampai di sini beberapa menit kemudian."
    mc "Tidak masalah, mari kita masuk ke dalam madu."
    stop sound
    scene 73
    mc "Lihat sayang, dia baik -baik saja."
    mc "Anda terlalu khawatir."
    v "Apakah dia tidur?"
    mc "Aku tidak tahu. Mari kita lihat."
    mc "Halo herold, apakah kamu bangun? Bagaimana perasaanmu?"
    scene 74
    h "Humm?"
    h "Siapa di sana? Perawat?"
    mc "Tidak, ini saya [McName] dan istri saya."
    mc "Kami di sini untuk melihat apakah Anda baik -baik saja."
    h "Oh, saya baik -baik saja, terima kasih, baru saja patah lengan."
    v "Aku benar -benar menyesal dia, itu semua salahku."
    h "Tidak apa -apa sayang, itu kecelakaan. Saya tidak menyimpan dendam."
    h "Bisakah Anda membantu saya?"
    vt "Apakah itu miliknya ... tidak, itu tidak mungkin."
    h "Apakah kamu masih di sana?"
    scene 75
    v "Saya di sini. Tentu saja saya bisa membantu Anda, apa saja."
    v "Apa yang kamu inginkan?"
    h "Bisakah Anda menelepon perawat kembali? Saya perlu buang air kecil dan dia membantu saya."
    scene 74
    v "Maaf tapi dia baru saja meninggalkan rumah dan perawat lainnya belum tiba."
    h "Sial, tapi aku benar -benar perlu buang air kecil. Itu menyakitkan."
    scene 76
    vt "Apa yang harus saya lakukan?"
    mct "Sial, karena aku melihatnya memata -matai kita berhubungan seks, aku merasakan kebutuhan aneh untuk terus mendorong penyimpangan ini."
    mct "Apa yang harus saya lakukan?"


    menu:
        "Sarankan dia membantunya":
            $ help_him = "1"
            $ wait_for_the_nurse = "2"
            scene 76
            mct "Aku agak merasa tidak enak untuknya, dan sebagian besar kesalahan kita dia terluka di sini sekarang."
            mct "Dan juga, ini sangat menarik bagi saya."
            scene 77
            mc "* Berbisik* sayang saya pikir Anda harus membantunya."
            v "* Berbisik* apa? Apa yang kamu katakan?"
            mc "* Berbisik* Ayo, tidak ada orang lain di sini, perawat akan membutuhkan waktu terlalu lama untuk sampai di sini. Itu yang paling tidak bisa kita lakukan untuknya."
            v "* Berbisik* Tapi aku akan melihat ..."
            scene 78
            mc "* Berbisik* bersantai. Itu hanya bagian tubuh. Ini bukan masalah besar."
            mc "* Berbisik* itu akan baik -baik saja. Ingat ketika kami mengatakan kami ingin mencoba hal -hal baru dan menarik?"
            mc "* Berbisik* Ini bisa menyenangkan."
            mc "* Berbisik* Dan itu akan memberi kita cerita yang hebat setelahnya."
            vt "Hmm, aku tidak tahu ... aneh dia ingin aku melakukan ini ..."
            vt "Tapi saya kira dia benar, itu hanya bagian tubuh."
            vt "Saya masih tidak begitu yakin tentang hal itu tetapi [McName] telah saya maksudkan, itu yang paling tidak bisa kita lakukan untuknya karena ini salah saya dia ada di sini."
            scene 79
            v "Oke, saya akan membantunya."
            v "Anda meyakinkan saya."
            mc "Itu dia, itu gadisku."
            mc "* Berbisik* Hei, saat Anda sampai di sana."
            mc "* Berbisik* Biarkan pintu kamar mandi sedikit terbuka sehingga saya dapat membantu Anda jika terjadi kesalahan."
            v "* Berbisik* oh baiklah."
            scene 80
            h "Anda tidak perlu melakukan ini manis."
            h "Itu bukan salahmu."
            scene 75
            v "Tidak apa -apa, saya ingin."
            v "Itu yang paling bisa saya lakukan."
            scene 81
            h "Terima kasih! Kamu cantik!"
            ht "Hehe ini menjadi lebih baik dari yang saya harapkan."
            ht "Sepertinya saya memukul emas dengan yang satu ini."
            scene 82
            v "Baiklah, mari kita lepaskan selimut ini dari Anda sekarang."
            scene 83
            play sound dress volume 0.5
            v "Di sini kita ... wtf?!"
            play sound chockfemale 
            v "Kenapa kamu telanjang?"
            h "Saya tidak suka pakaian rumah sakit itu."
            h "Mereka membiarkan pantat saya terbuka, jadi jika itu masalahnya saya lebih suka membiarkan tubuh saya bebas."
            h "Apa masalahnya? Anda harus melihatnya ketika Anda membantu saya kencing."
            scene 84
            v "Saya kira Anda benar ..."
            vt "Saya hanya tidak berpikir itu akan sebesar ini."
            mct "Saya tidak percaya istri saya melihat penis pria tua tepat di depan saya."
            mct "Dan saya akan dihidupkan oleh WTF itu."
            mct "Saya sakit apa?"
            scene 85
            v "Ok Herold, pegang saya, saya akan membimbing Anda ke kamar mandi."
            h "Terima kasih sayang."
            vt "Saya sangat berharap [McName] baik -baik saja dengan ini."
            vt "Aku akan melakukan apa yang dia katakan dan biarkan pintu sedikit terbuka."
            scene blackscreen
            pause 0.5
            narrador "[violet] membawanya ke kamar mandi sementara [mcname] mengikuti tepat di belakang ..."
            stop music fadeout 1.0
            scene 86 with Dissolve(0.3)
            play music publicbathroom fadein 1.5 volume 0.2
            mct "Sial. Dia benar -benar melakukannya."
            mct "Istri saya membantu seorang pria telanjang kencing sementara dia menggendongnya."
            mct "Mengapa saya begitu terangsang oleh situasi ini?"
            scene 87
            v "Kami sudah ada di sini dia."
            v "Anda bisa mulai kencing sekarang."
            h "Apa maksudmu aku bisa memulai?"
            h "Anda harus mengarahkannya untuk saya, saya tidak bisa menggunakan lengan saya."
            v "Bertujuan?"
            scene 88
            vt "Ya Tuhan, dia benar."
            vt "Dia harus berpegang pada saya dengan lengan kanannya dan lengan kirinya rusak."
            scene 89
            vt "Tapi saya tidak berpikir saya bisa melakukan itu."
            vt "Dia ingin aku memegang penisnya."
            vt "Apa yang harus saya lakukan? Jika saya tidak memegangnya, dia akan buang air kecil di lantai."
            scene 90
            vt "Biarkan saya melihat apa yang [McName] pikirkan."
            vt "* Berbisik* Apa yang Anda ingin saya lakukan?"
            scene 91
            play sound heartbeatslow volume 0.5 loop
            mct "Sial, dia menatapku menungguku untuk memutuskan."
            mct "Saya harus menghentikan ini, ini terlalu jauh."
            mct "Tapi saya tidak bisa tidak merasakan hati saya berdebar kencang hanya dengan memikirkan istri saya meraih ayam pria lain."
            mct "Saya tidak tahu harus berbuat apa."


            menu:
                "Merangkul perasaan ini.":
                    $ embrace_feelings = "1"
                    $ nod_her_to_stop = "2"
                    scene 92
                    stop sound
                    mct "Saya ingin ini."
                    scene 93
                    mc "* Berbisik* lakukan."
                    scene 94
                    vt "Tidak mungkin dia ingin saya melakukan ini."
                    vt "Saya harus mengakui bahwa situasi ini agak menyenangkan."
                    vt "Tapi ini terlalu banyak."
                    vt "Raut wajahnya ..."
                    scene 95
                    v "Oke dia, aku akan melakukannya!"
                    h "Bagus! Cepatlah, saya berada di batas saya di sini."
                    scene 96
                    vt "Oke, saya kira itu bukan masalah besar."
                    vt "Saya hanya membantunya dengan kebutuhannya. Perawat melakukan ini sepanjang waktu."
                    vt "Saya harus mengatakan dia memiliki ayam yang cukup bagus untuk pria tua."
                    vt "Apakah saya benar -benar membangkitkan ini?"
                    scene 93
                    mct "Persetan, aku sulit seperti batu sekarang."
                    mct "Dia akan melakukannya."
                    scene 99
                    ht "Ha ha ha. Itu terlalu mudah!"
                    ht "Pria ini gila membiarkan istrinya melakukan hal ini."
                    ht "Dia melihat kita berpikir aku buta dan aku tidak bisa melihatnya di sana hahaha."
                    ht "Sepertinya dia memiliki fetish jahat ini atau semacamnya."
                    scene 96
                    vt "Saya akan mengambil penis seorang lelaki tua sementara suami saya mengawasi semuanya."
                    play sound heartbeatfast volume 0.5 loop
                    vt "Ini gila!"
                    vt "Jantungku berdegup kencang sekarang."
                    vt "Oke, saya bisa melakukannya!"
                    scene 97 with Dissolve(0.3)
                    pause 0.9 
                    scene 98 with Dissolve(0.3)
                    pause 0.3
                    stop sound
                    play sound doorknock volume 0.8
                    scene 100
                    nurse "Halo saya di sini!"
                    play sound lockeddoor
                    nurse "Mengapa pintunya terkunci?"
                    scene 101
                    mc "Kotoran! Perawat tiba!"
                    mct "Untung saya mengunci pintu sebelumnya, jika perawat masuk sekarang dan melihat saya di sini akan sulit untuk dijelaskan ..."
                    v "Cepat, mari kita kembali tidur!"
                    scene blackscreen
                    pause 0.5
                    play sound doorlock volume 0.3
                    stop music
                    play music hospital fadein 1.5 volume 0.3
                    narrador "[violet] dengan cepat membawanya kembali ke tempat tidur dan [mcname] membuka kunci pintu sehingga perawat bisa masuk."
                "Mengangguk untuk berhenti.":


                    $ nod_her_to_stop = "1"
                    $ embrace_feelings = "2"
                    stop sound
                    scene 90
                    mc "* Berbisik* Ini sudah terlalu jauh."
                    v "* Berbisik* oh oke, mari kita hentikan ini."
                    v "Maaf dia tapi ini terlalu banyak."
                    v "Mari kita kembali dan tunggu perawat."
                    scene blackscreen
                    pause 0.5
                    stop music
                    play music hospital fadein 1.5 volume 0.3
                    narrador "[violet] membawanya kembali ke tempat tidur dan [mcname] membuka kunci pintu sehingga perawat dapat masuk."
        "Tunggu perawat tiba":


            $ wait_for_the_nurse = "1"
            $ help_him = "2"
            scene 74
            v "Maaf tapi perawat mungkin tidak akan lama."
            v "Kita harus menunggunya."
            scene blackscreen
            pause 0.5
            narrador "Setelah beberapa menit ..."


    scene 80
    h "Sial, bagaimana dengan situasi saya sekarang?"
    h "Saya masih perlu buang air kecil!"
    scene 76
    v "Tidak apa -apa dia."
    v "Perawat dapat membantu Anda sekarang."
    scene 80
    ht "Fuuuck itu sangat dekat."
    ht "Perawat bodoh. Aku bahkan tidak perlu buang air kecil."
    scene 76
    mc "Saya kira kita harus pergi sekarang sayang, mereka bisa mengurus sisanya."
    mc "Semoga Anda segera sembuh Herold, sampai jumpa."
    v "Bye Herold, maaf saya tidak bisa membantu."
    scene blackscreen
    pause 0.2
    stop music fadeout 1.0
    narrador "Setelah itu, mereka keluar dan mulai berjalan pulang."
    if help_him == "1" and embrace_feelings == "1":
        play music parkday volume 0.1
        scene 106
        v "Pagi yang gila."
        v "Bisakah Anda membayangkan bahwa pada hari pertama hidup adalah rumah baru saya akan menampar wajah tetangga tua kami dan membawanya ke rumah sakit di mana saya harus melihatnya telanjang ..."
        mc "Ya, saat Anda mengatakannya seperti itu ..."
        mc "Kedengarannya gila."
        mc "Kira kita harus berbicara tentang apa yang terjadi di sana kan?"
        scene 107
        v "Tentu, tapi kita bisa menunggu sampai kita pulang untuk itu."
        v "Mari kita nikmati taman yang indah ini sekarang."
        v "Tidak jarang kita bisa berjalan -jalan seperti ini."
        scene 106
        mc "Ya, Anda benar, ini sangat dingin."
        mc "Aku menyukainya!"
    if wait_for_the_nurse == "1":
        play music parkday volume 0.1
        scene 107
        v "Taman yang indah!"
        v "Tidak jarang kita bisa berjalan -jalan seperti ini."
        scene 106
        mc "Ya, Anda benar, ini sangat dingin."
        mc "Aku menyukainya!"
    if help_him == "1" and embrace_feelings == "2":
        play music parkday volume 0.1
        scene 106
        v "Pagi yang gila."
        v "Bisakah Anda membayangkan bahwa pada hari pertama hidup adalah rumah baru saya akan menampar wajah tetangga tua kami dan membawanya ke rumah sakit di mana saya harus melihatnya telanjang ..."
        mc "Ya, saat Anda mengatakannya seperti itu ..."
        mc "Kedengarannya gila."
        mc "Kira kita harus berbicara tentang apa yang terjadi di sana kan?"
        scene 107
        v "Tentu, tapi kita bisa menunggu sampai kita pulang untuk itu."
        v "Mari kita nikmati taman yang indah ini sekarang."
        v "Tidak jarang kita bisa berjalan -jalan seperti ini."
        scene 106
        mc "Ya, Anda benar, ini sangat dingin."
        mc "Aku menyukainya!"
    scene 107
    v "Hei, kenapa kita tidak mengambil beberapa foto?"
    scene 119
    mc "HM? Anda ingin saya memotret Anda di sini?"
    scene 107
    v "Tentu, kenapa tidak? Taman itu terlihat kosong."
    scene 119
    mc "Benar-benar?"
    scene 118
    mc "Anda benar."
    mc "Tidak ada satu jiwa pun di sini."
    scene 171
    mc "Selain patung aneh itu tentu saja hahah."
    mc "Dan itu bahkan memegang kamera."
    scene 106
    mc "Oke, mari kita lakukan."
    mc "Itu latar belakang yang sempurna."
    scene 172
    mc "Oke, tetap dekat dengan patung dan buat beberapa pose untuk saya."
    scene blackscreen
    show 173
    show phonephoto
    v "Seperti ini?"
    mc "Sangat bagus!"
    mc "Say \"cheese\"."
    show phoneflash with Dissolve(0.1)
    play sound photoshootcellphone
    hide phoneflash
    hide phonephoto
    ""
    scene 172
    mc "Bagus! Mari kita lakukan pasangan lagi."
    scene blackscreen
    narrador "Pada saat yang sama..."
    scene 200
    trevor "Dimana bajingan ini?"
    scene 201
    trevor "Dia bilang dia akan berada di sini jam 5 sore."
    trevort "Justin selalu terlambat."
    trevort "Saya tidak percaya ini. Taman ini benar -benar kosong."
    mc "Say \"cheese\"."
    scene 203
    trevort "HM?"
    trevort "Apakah itu suara Justin? Saya tidak tahu dari sini."
    scene 202
    trevort "Itu datang dari sana."
    trevort "Taman ini lebih besar dari yang saya kira."
    scene 204
    trevort "Itu bukan Justin. Hanya pasangan yang memotret."
    trevort "Saya kira taman itu tidak begitu kosong."
    trevort "Biarkan saya melihat apa yang mereka lakukan."
    scene 195
    mc "Ini bagus. Cobalah membuat beberapa pose seksi sekarang."
    scene blackscreen
    show 174
    show phonephoto
    v "Cukup seksi?"
    mc "Cantik!"
    show phoneflash with Dissolve(0.1)
    play sound photoshootcellphone
    hide phoneflash
    hide phonephoto
    ""
    scene 197
    trevort "Bung, cewek itu sangat panas!"
    trevort "Ayo, tunjukkan tubuh seksi itu!"
    scene blackscreen
    show 175
    show phonephoto
    v "Bagaimana dengan ini?"
    mc "Saya menyukainya!"
    show phoneflash with Dissolve(0.1)
    play sound photoshootcellphone
    hide phoneflash
    hide phonephoto
    ""
    scene 176
    mct "Sepertinya dia bersenang -senang."
    mct "Mungkin ini adalah kesempatan saya untuk membuatnya lebih terbuka."



    menu:
        mct "Haruskah saya melakukannya?"
        "Minta lebih banyak gambar yang berani.":
            $ park_photos = "1"
            $ no_park_photos = "2"
            scene 195
            mc "Hei sayang. Ini sangat seksi tapi apa yang Anda katakan kami membawa ini ke level berikutnya?"
            scene 178
            v "Level berikutnya? Bagaimana apanya?"
            scene 195
            mc "Saya tidak tahu, maksud saya ... mungkin Anda bisa melepas top Anda."
            scene 178
            v "Anda tidak bisa serius, kami di depan umum, bagaimana jika seseorang datang?"
            scene 195
            mc "Kemudian, mereka akan melihat kehidupan mereka."
            scene 179
            v "Jadi Anda menyukai gagasan seseorang yang melihat istri telanjang Anda di taman umum ..."
            scene 195
            mct "Dia bahkan bercanda dengan ide itu."
            if keep_fucking_violet == "1":
                mct "Setelah hari ini, ketika saya pikir Herold sedang menatap kami, saya benar -benar mulai menyukai gagasan memamerkannya lebih banyak."
                mct "Saya pasti ingin menjelajahi ini lebih banyak."
                mct "Aku belum bisa memberitahunya."
            else:
                mct "Saya kira saya sangat menyukai ide ini, tetapi saya belum bisa memberitahunya."
            mc "Ayo saya pikir Anda mengatakan Anda ingin mencoba hal -hal menarik ... untuk menjadi lebih berani ..."
            scene 178
            vt "Dia benar, aku harus lebih berani."
            vt "Selain itu, kita sendirian di sini. Saya belum melihat saya jiwa di taman ini."
            scene 179
            v "Oke, siapkan kamera. Saya akan melakukannya."
            scene blackscreen
            show 180
            show phonephoto
            v "Saya akan menunjukkan betapa berani saya."
            mc "Ya!"
            show phoneflash with Dissolve(0.1)
            play sound photoshootcellphone
            hide phoneflash
            hide phonephoto
            ""
            scene 199
            trevort "Dia benar -benar melakukannya!"
            trevort "Ya! Biarkan saya melihat payudaranya."
            scene blackscreen
            show 181
            show phonephoto
            mc "Sungguh! Itu saja."
            show phoneflash with Dissolve(0.1)
            play sound photoshootcellphone
            hide phoneflash
            hide phonephoto
            ""
            scene 196
            trevort "Mustahil! Saya sangat beruntung!"
            trevort "Pertunjukan yang luar biasa!"
            scene 182
            v "Itu dia, atasan tidak aktif. Apa yang Anda ingin saya lakukan sekarang?"
            scene 195
            mc "Saya tidak tahu ... lebih dekat dengan patung itu, jadilah kreatif."
            scene 182
            v "Hummm ..."
            v "Oke saya pikir saya punya ide."
            scene blackscreen
            show 183
            show phonephoto
            v "Saya pikir Tn. Patung di sini berhasil. Dia memiliki pantat yang cukup kuat haha."
            mc "Itu lucu."
            show phoneflash with Dissolve(0.1)
            play sound photoshootcellphone
            hide phoneflash
            hide phonephoto
            ""
            scene blackscreen
            show 184
            show phonephoto
            v "Dan saya yakin penisnya sangat keras sekarang."
            mc "Ya Tuhan, Anda telah menunggu untuk melemparkan yang itu, kan?"
            v "Ha ha ha."
            show phoneflash with Dissolve(0.1)
            play sound photoshootcellphone
            hide phoneflash
            hide phonephoto
            ""
            scene 185
            vt "Saya harus mengakui, ini cukup menarik."
            vt "Saya merasa sangat bebas memiliki payudara saya seperti ini."
            scene 186
            vt "HM?"
            scene 187
            vt "YA AMPUN! Kami tidak sendirian!"
            scene 196
            trevort "Sial, dia melihatku!"
            scene 190
            mc "Apa yang terjadi sayang? Sepertinya Anda telah melihat hantu."
            scene 187
            v "Dia..."
            v "SAYA..."
            scene 188
            vt "Tunggu, apa yang saya lakukan?"
            vt "Itulah arti [McName]. Saya harus lebih berani."
            vt "Kami bersenang -senang dan melakukan sesuatu yang baru dan menarik untuk perubahan."
            vt "Saya tidak bisa merusak ini karena beberapa Perv ingin melihatnya."
            vt "..."
            scene 189
            vt "Persetan! Saya tidak peduli lagi."
            if keep_fucking_violet == "1" and embrace_feelings == "1":
                vt "Selain itu, [McName] sangat suka memamerkan saya kepada pria lain, dia suka melihat wajah cemburu mereka."
                vt "Saya kira dia akan menyukainya ketika saya mengatakan kepadanya bahwa kami tidak sendirian di sini."
                vt "Dan menilai dari bagaimana dia bereaksi hari ini di rumah sakit, menyuruh saya melakukan semua itu dengan Herold, saya pikir dia bersemangat dengan ide itu."
            vt "Ayo lakukan ini!"
            v "Bukan bukan bayi, mari kita terus berjalan."
            scene 186
            vt "Lihat semua yang Anda inginkan sedikit."
            scene 197
            trevort "Wow, dia tahu aku di sini dan dia masih terjadi."
            trevort "Saya pasti bermimpi."
            scene blackscreen
            show 194
            show phonephoto
            mc "Itu terlihat bagus!"
            mc "Kamu benar -benar madu."
            show phoneflash with Dissolve(0.1)
            play sound photoshootcellphone
            hide phoneflash
            hide phonephoto
            ""
            vt "Saya tidak percaya saya melakukan ini. Saya sangat berharap [McName] tidak akan marah tentang hal itu nanti."
            vt "Saya melakukan ini untuknya. Meskipun saya tidak akan berbohong, saya mulai lebih menyukai ini."
            scene blackscreen
            show 193
            show phonephoto
            mc "Dick saya sangat keras sayang, Anda sangat seksi!"
            vt "Saya tidak tahu apakah A harus bersemangat dengan pikiran seseorang yang melihat payudara saya sementara suami saya sulit."
            vt "Tapi sebenarnya aku ... pasti!"
            show phoneflash with Dissolve(0.1)
            play sound photoshootcellphone
            hide phoneflash
            hide phonephoto
            ""
            scene 196
            trevort "Sobat, betapa aku ingin memiliki payudara itu di tanganku sekarang."
            trevort "Saya harus mencari tahu siapa dia."
            scene blackscreen
            show 192
            vt "Jika pria itu ingin datang ke sini, saya tidak akan tahu harus berkata apa kepada [McName]."
            scene blackscreen
            show 192
            show phonephoto
            mc "Saya senang melihat Anda seperti ini."
            show phoneflash with Dissolve(0.1)
            play sound photoshootcellphone
            hide phoneflash
            hide phonephoto
            ""
            vt "Saya sangat basah sekarang."
            vt "Jika kita terus mempertahankan ini, saya akan mulai melakukan masturbasi di sini di taman."
            vt "Saya pikir kita lebih baik berhenti sebelum saya melangkah terlalu jauh."
            scene 198
            v "Oke sayang itu cukup untuk hari ini, mari kita pergi."
            scene 195
            mc "Oh tidak, benarkah? Biarkan saya mengambil beberapa lagi."
            scene 198
            v "Tidak mungkin, kita harus pergi sekarang."
            v "Saya pikir saya mendengar seseorang datang."
            scene 199
            trevort "Kotoran! Itu isyarat saya untuk pergi."
            scene 177
            mc "Oke, oke. Kita bisa melakukan ini lagi hari lain."
            scene 179
            v "Kau anggap aku apa? Anda pikir saya akan melepas di depan umum setiap hari sekarang?"
            scene 177
            mc "Itu akan luar biasa!"
            scene 179
            v "Anda tidak dapat diperbaiki, Anda tahu itu?"
            v "Ayo pergi sebelum Anda membuat saya telanjang lagi."
            scene 191
            mc "Oke!"
            mct "Itu pasti beberapa kemajuan!"
            mct "Saya hanya perlu memastikan saya tidak mendorongnya ke jauh dan kami dapat bersenang -senang di masa depan."
            mc "Ayo pergi."
            scene blackscreen
            pause 1.0
            scene 106
            mct "Wow, kita tidak sendirian di sini lagi, bayangkan jika kita tidak berhenti."
            mct "Sobat yang sulit, tidak ada payudara untuk Anda hari ini."
        "Jangan minta lebih.":

            $ no_park_photos = "1"
            $ park_photos = "2"
            scene 191
            mct "Nah, mari kita terus berjalan pulang."
            mc "Hei sayang, itu cukup foto, ayo pergi."
            scene 178
            v "Segera, Benarkah?"
            scene 191
            mc "Ya, sudah terlambat dan kami harus pulang."
            scene 178
            v "Baiklah. Itu menyenangkan. Mari kita lakukan ini lebih sering."
            mc "Tentu sayang."
            scene blackscreen
            pause 0.5
            scene 106
            mct "Untung saya berhenti, kami tidak sendirian di taman lagi."


    scene 109
    justint "Bersenandung?"
    justint "Oh halo ..."
    scene 110
    justint "WOW!"
    justint "Nah, itulah yang saya sebut bakat besar!"
    scene 111
    justint "Sepertinya mereka baru di sekitar sini."
    justint "Saya tidak bisa melewatkan kesempatan ini!"
    scene 112
    justin "Halo pasangan cantik!"
    justin "Bisakah saya berbicara dengan Anda sebentar?"
    mc "Bersenandung?"
    scene 113
    mc "Oh halo!"
    mc "Tentu, kita bisa bicara."
    mc "Apa yang telah terjadi?"
    scene 114
    justin "Jadi, nama saya Justin dan saya seorang fotografer."
    justin "Saya duduk di sana terganggu ketika saya melihat Anda berdua lewat."
    scene 116
    justin "Bolehkah saya meminta nama Anda?"
    scene 113
    mc "Saya [McName] dan ini adalah istri saya [Violet]."
    v "Senang berkenalan dengan Anda."
    justin "Sangat bagus, memang."
    scene 116
    justin "Katakan [Violet], apakah Anda pernah melakukan pemodelan?"
    justin "Anda terlihat seperti dari industri ini."
    scene 117
    v "Oh tidak, tidak pernah. Saya dulu bekerja sebagai sekretaris."
    v "Saya tidak bekerja lagi sekarang. Kami baru saja pindah."
    scene 116
    justin "Saya melihat ... selamat datang, semoga Anda menyukainya di sini."
    justin "Saya mungkin memiliki tawaran untuk Anda."
    scene 115
    justin "Dengan segala hormat [McName], istri Anda terlihat seperti model besar."
    justin "Saya memiliki studio di dekat dan saya ingin tahu apakah Anda mau membiarkan saya mengambil beberapa fotonya."
    scene 119
    mct "Apa? Bung ini ingin mengambil foto istri saya?"
    mct "Saya bertanya -tanya gambar macam apa."
    scene 118
    mc "Saya tidak tahu pria, kami bahkan tidak mengenal Anda ..."
    mc "Bagaimana saya bisa membiarkan istri saya pergi ke studio dengan beberapa pria acak yang bahkan saya tidak tahu benar -benar seorang fotografer."
    scene 120
    justin "Ayo pria, kenapa aku berbohong padamu?"
    justin "Dan tentu saja Anda akan berada di sana juga."
    justin "Saya tidak memintanya untuk datang sendirian dengan saya."
    justin "Tapi saya melihat Anda membutuhkan bukti."
    scene 121
    justin "Di sini, bawa kartu saya."
    justin "Situs web saya ada di sana."
    justin "Anda dapat mencarinya dan melihat sesi foto saya sebelumnya di sana."
    scene 122
    mct "Hum ... sepertinya sangat profesional."
    mct "Saya kira dia mengatakan yang sebenarnya."
    scene 123
    mc "Bagaimana menurutmu sayang?"
    mc "Apakah Anda menyukai itu?"
    scene 124
    v "Hmm ... saya tidak tahu."
    v "Saya selalu bermimpi menjadi model super."
    v "Tapi saya belum tahu."
    v "Mari kita lihat gambar dari situs web terlebih dahulu."
    v "Jika kita suka mereka, kita akan lihat ..."
    scene 125
    mc "Ini dia. Kami akan menghubungi jika kami menyukai pekerjaan Anda."
    mc "Kita harus pergi sekarang. Jaga pria."
    scene 126
    justin "Tentu, Anda adalah bosnya!"
    justin "Sampai jumpa, selamat malam!"
    justin "Sampai berjumpa lagi."
    scene 127
    justint "Saya sangat berharap mengatakan ya."
    justint "Lihat dia pergi."
    scene 128
    justint "Tidak sabar untuk bekerja dengan pantat itu."
    justint "Sempurna ..."
    scene blackscreen
    pause 0.3
    narrador "Nanti di rumah ..."
    stop music fadeout 1.5
    if help_him == "1" and embrace_feelings == "1":
        scene 102
        play music sadmusic fadein 2.0 volume 0.5
        v "Apakah kamu baik -baik saja sayang?"
        v "Kamu terlihat sedih. Apa yang telah terjadi?"
        mc "Aku baik -baik saja ... hanya saja aku seharusnya tidak menyuruhmu melakukan semua itu di rumah sakit."
        mc "Maaf saya overdid, saya hanya ingin kami bersenang -senang dalam situasi itu."
        mc "Saya takut jika saya terus melakukan hal -hal itu, saya mungkin akan kehilangan Anda."
        v "Ayo sayang, jangan pernah mengatakan itu!"
        v "Anda tidak akan kehilangan saya, apa pun yang terjadi."
    if show_her == "1" and keep_fucking_violet == "1" and wait_for_the_nurse == "1":
        scene 102
        play music sadmusic fadein 2.0 volume 0.5
        v "Apakah kamu baik -baik saja sayang?"
        v "Kamu terlihat sedih. Apa yang telah terjadi?"
        mc "Aku baik -baik saja ... hanya aku ..."
    if show_her == "1" and keep_fucking_violet == "1" and wait_for_the_nurse == "2" and nod_her_to_stop == "1":
        scene 102
        play music sadmusic fadein 2.0 volume 0.5
        v "Apakah kamu baik -baik saja sayang?"
        v "Kamu terlihat sedih. Apa yang telah terjadi?"
        mc "Aku baik -baik saja ... hanya aku ..."
    if show_her == "1" and keep_fucking_violet == "1":
        scene 103
        play music sadmusic fadein 2.0 volume 0.5
        mc "Saya hanya memiliki perasaan ini dalam diri saya, saya tidak tahu bagaimana menjelaskannya."
        mc "Hari ini ketika kami berhubungan seks di kamar tidur saya melihatnya jauh sebelum Anda melakukannya."
        mc "Aku seharusnya memberitahumu, tetapi sebaliknya aku terus berjalan."
        mc "Dan saya tidak tahu dia buta. Bagi saya dia pasti memata -matai kami."
        mc "Ketika saya melihat Anda cum untuk saya saat seseorang melihat itu membuat saya menjadi gila!"
        mc "Saya tidak tahu mengapa, tetapi melihat Anda terbuka seperti itu mengacaukan kepala saya."
        mc "Saya khawatir saya akan melangkah terlalu jauh dalam fantasi itu dan saya akhirnya menyakiti Anda."
        scene 104
        stop music fadeout 1.5
        play music romanticmusic fadein 3.0 volume 0.1
        v "Hei, datang ke sini. Saya tahu Anda tidak akan pernah melakukan apa pun yang bisa menyakiti saya."
        v "Jika Anda memiliki fantasi ini, saya terbuka untuk membicarakannya dengan mereka."
        v "Dan jika Anda suka, selama itu adalah sesuatu yang kami berdua setuju maka saya tidak melihat masalah."
        v "Aku sangat mencintaimu dan aku berjanji ini tidak akan mengubah kita."
        v "Di samping itu..."
        scene 105
        v "Saya tahu Anda suka memamerkan saya kepada orang -orang dan jika Anda meniduri saya sebagus itu setelah Anda melihatnya melihat tubuh telanjang saya sepenuhnya terpapar ..."
        v "Saya tidak ingin Anda menghentikannya dalam waktu dekat."
        v "Saya akan berbohong jika saya mengatakan saya tidak menikmati. Anda telah melihat bagaimana A datang pada ayam Anda."
    if show_her == "1" and stop_this_right_now == "1":
        scene 104
        v "Senang berada di rumah, tapi aku masih merasa tidak enak untuknya, dia buta dan karena aku patah lengan."
        mc "Saya merasa tidak enak juga, saya siap bertarung dengannya. Bagi saya dia pasti orang cabul."
        v "Hari yang sangat gila, saya tidak percaya kami harus membawanya ke rumah sakit setelah kami pikir dia memata -matai kami."
        v "Saya senang Anda melihatnya di sana, saya tahu dia ternyata buta setelah semua, tetapi tetap saja, saya cukup terkejut di sana."
        scene 105
        v "Lucunya ..."
        v "Ketika saya mulai memikirkan semua situasi itu, itu membuat saya ingin tertawa."
        mc "Anda benar, itu benar -benar lucu."
        v "Benar? Bagus, Anda juga berpikir seperti itu."
    scene 105
    if park_photos == "1":
        v "Dan saya sangat menyukainya di taman."
        v "Awalnya saya takut tetapi saya sangat menikmatinya."
        mc "Saya juga menyukainya, kita harus lebih sering melakukannya."
        v "Dan Anda tahu apa? Saya tidak memberi tahu Anda di sana, tetapi kami tidak sendirian pada saat itu."
        mc "Ah, benarkah?"
        v "Ada sedikit cabul tepat di belakang sudut menatap kami ... menatapku."
        v "Saya melihatnya setelah saya mengambil top saya dan berpikir akan menyenangkan untuk menggoda pria malang itu."
        v "Saya tidak banyak berpikir pada saat itu tetapi sekarang saya melihat saya membuat pilihan yang tepat karena suami saya memiliki fantasi tentang saya yang terpapar, haha."
        mc "Anda pasti melakukannya. Dan terima kasih sudah memberitahuku."
        mc "Yang paling penting adalah kami saling memberi tahu segalanya. Sisanya kita bisa mengetahuinya dengan waktu."
        v "Benar!"
    v "Sekarang, mari kita mandi, ibuku seharusnya ada di sini dalam waktu dekat."
    v "Saya tidak ingin dia datang ke sini sementara kami berbau seperti rumah sakit."
    mc "Kesepakatan! Ayo pergi."
    stop music fadeout 1.5
    scene blackscreen
    pause 0.5
    scene 129
    play music showerinside fadein 0.5
    mc "Jadi, apa pendapat Anda tentang kamar mandi?"
    mc "Apakah kamu menyukainya?"
    v "Saya pikir itu bagus. Banyak ruang, bak mandi ..."
    v "Kami bahkan tidak bisa mandi bersama di kamar mandi lama."
    v "Saya suka cahaya di sini. Satu -satunya hal adalah ..."
    scene 130
    v "Tidakkah menurut Anda aneh bahwa kita sepenuhnya terbuka ke halaman belakang?"
    v "Maksudku, siapa pun bisa melihat ke dalam jika kita memiliki barbekyu di sana atau sesuatu."
    mc "Ya, saya mengerti maksud Anda."
    mc "Tapi saya cukup yakin itu adalah gelas satu sisi."
    mc "Kita bisa melihat halaman belakang dari sini tetapi dari sana itu sepenuhnya buram."
    scene 131
    v "Wow! Benar-benar?"
    mc "Ya sayang, tentu saja haha."
    mc "Ini desain modern."
    v "Baiklah, tuan pria modern."
    scene 131b
    mct "Hm airnya bagus."
    mct "Tapi Amelia dan Jeff akan berada di sini kapan saja sekarang."
    mct "Haruskah saya keluar?"


    menu:
        "Tetap sedikit lebih lama":
            $ ted_shower = "1"
            $ violet_shower = "2"
            scene 132
            v "Saya akan keluar, cobalah untuk tidak terlalu lama."
            play sound doorbell volume 0.5
            v "Ibuku akan segera ke sini ..."
            scene 133
            v "Saya kira itu dia."
            mc "Waktu yang tepat!"
            v "Ha ha ha."
            v "Ayo. Serius aku menunggumu di sana. Jangan butuh waktu lama."
            mc "Hei, saya pria besar, saya perlu lebih banyak waktu untuk membersihkan tubuh saya daripada Anda."
            v "Kamu beruntung aku mencintaimu, pria besarku!"
            mc "Saya tahu saya. Dan aku juga mencintaimu!"
            stop sound
            stop music fadeout 3.0
            scene blackscreen
            pause 0.5
            play music neighborhood fadein 2.5 volume 0.2
            scene 134
            play sound doorbell volume 0.5
            amelia "Halo, apakah ada yang di rumah?"
            v "Aku datang !!"
            stop sound
            play sound dooropen1 volume 0.5
            scene 135
            amelia "Selamat malam, saya mencari seorang berambut merah panas yang memiliki ibu yang lebih panas."
            amelia "Apakah Anda tahu jika dia tinggal di sini?"
            scene 136
            v "Saya pikir saya mungkin pernah melihatnya."
            v "Tidak begitu yakin tentang ibu yang lebih panas."
            scene 135
            amelia "Haha pantat pintar."
            amelia "Ayo, beri pelukan besar pada ibumu."
            stop sound
            scene 137
            v "Aku sangat merindukanmu."
            amelia "Aku juga bayi perempuan."
            amelia "Sekarang setelah Anda tinggal di dekatnya, kami dapat menghabiskan lebih banyak waktu bersama."
            v "Saya ingin ibu itu!"
            scene 138
            amelia "Dan lihat rumahmu!"
            amelia "Sangat indah. Anda dan [McName] diberkati."
            amelia "Saya berharap ayah Anda bisa berada di sini untuk melihat berapa banyak yang telah Anda tanam."
            amelia "Aku yakin dia akan bangga padamu."
            v "Terima kasih Ibu. Saya tahu dia akan melakukannya."
            v "Ayo masuk ke dalam sekarang."
            play sound doorclose volume 0.5
            scene 139
            v "Karena kami membahas masalah ini, bagaimana Jeff memperlakukan Anda setelah satu tahun menikah?"
            amelia "Oh, dia benar -benar madu. Kami saling mencintai setiap hari."
            v "Itu bagus untuk didengar."
            v "Kenapa dia tidak ikut denganmu?"
            amelia "Dia terjebak di tempat kerja. Tapi dia berjanji akan segera mengunjungimu."
            v "Oke. Tidak masalah."
            amelia "Berbicara tentang suami yang hebat ... dimana [mcname]?"
            v "Saya pikir dia masih di kamar mandi, Anda tahu bagaimana keadaannya."
            amelia "Ya, saya tahu hehe."
            stop sound
            scene 140
            v "Nah, saya akan membuat makan malam, jika saya membutuhkan bantuan Anda, saya akan menelepon Anda."
            v "Untuk saat ini Anda dapat melakukan tur di rumah, sesuai dengan diri Anda."
            v "Mi Casa es Su Casa!"
            amelia "Terima kasih."
            amelia "Or should I say, \"Gracias\"hahah."
            scene 141
            ameliat "Hmm, jadi [McName] sedang mandi sekarang."
            ameliat "Menarik..."
            ameliat "Ini bisa menjadi kesempatan sempurna untuk menghentikan rasa ingin tahu saya ..."
            scene blackscreen
            pause 0.6
            stop music fadeout 1.5
            scene 142
            play music showeroutside fadein 3.0 volume 0.1
            ameliat "Sepertinya mereka lupa pintu terbuka."
            ameliat "Mari kita lihat apa yang kita miliki di sini ..."
            scene 143
            ameliat "Ohh my!"
            ameliat "Lihat itu!"
            scene 144
            ameliat "[violet] tidak bisa mengeluh, itu sudah pasti."
            ameliat "[McName] sedang mengemas penis yang cukup bagus yang harus saya katakan."
            ameliat "Dan dia bahkan tidak tegak."
            scene 143
            ameliat "Saya tahu saya seharusnya tidak melihat ..."
            ameliat "Tapi saya benar -benar basah menonton ini."
            ameliat "Ada apa denganku?"
            ameliat "Dia adalah suami putriku."
            scene 144
            ameliat "Tapi itu ayam yang bagus."
            ameliat "Sulit untuk tidak melihat."
            scene 145
            ameliat "Dia tidak tahu bahwa saya di sini."
            ameliat "Saya bisa masuk dan mengatakan saya tidak tahu dia ada di sana ..."
            scene 146
            ameliat "Saya ingin melihat raut wajahnya."
            ameliat "Dia selalu malu di sekitarku."
            ameliat "Ini akan menyenangkan. Aku akan masuk ..."
            v "MAMA!"
            play sound doorbell volume 0.5
            scene 147
            v "Jeff ada di sini, saya tidak bisa mendapatkan pintu sekarang."
            v "Bisakah Anda membantu saya di sini?"
            stop sound
            scene 148
            ameliat "Kotoran! Saya kehilangan jejak waktu."
            amelia "Tidak masalah sayang aku datang."
            stop music
            play music showerinside fadein 0.5
            scene 149
            mct "Bersenandung?"
            mct "Apakah seseorang menelepon saya?"
            mct "Saya pikir saya mendengar suara Amelia."
            scene 150
            mct "Sungguh! Pintunya terbuka."
            mct "Apakah dia melihat saya?"
            scene 149
            mct "Ya Tuhan, itu akan menjadi percakapan yang aneh nanti ..."
            mct "Ini ... situasi ini."
            mct "Itu membuatku ingat hari itu ..."
            stop music fadeout 2.0
            play sound endupdate fadein 2.0 volume 0.5
            scene blackscreen with fade
            pause 0.5
            centered "__Tag_0____tag_1__pisode 2__tag_2____tag_3__"
            centered "__Tag_0____tag_1__2 tahun yang lalu__tag_2____tag_3__"
            stop sound
        "Keluar dulu":


            $ violet_shower = "1"
            $ ted_shower = "2"
            scene 151
            mc "Saya akan keluar, cobalah untuk tidak terlalu lama."
            play sound doorbell volume 0.5
            mc "Ibumu akan segera berada di sini ..."
            scene 152
            mc "Saya kira itu dia."
            v "Waktu yang tepat!"
            mc "Ayo. Serius, aku menunggumu di sana. Jangan butuh waktu lama."
            v "Santai, saya keluar sebentar lagi."
            mc "Kamu beruntung aku mencintaimu!"
            v "Saya tahu saya. Aku pun mencintaimu!"
            stop sound
            stop music fadeout 3.0
            scene blackscreen
            pause 0.5
            play music neighborhood fadein 2.5 volume 0.2
            scene 153
            play sound doorbell volume 0.5
            amelia "Halo, apakah ada yang di rumah?"
            mc "Aku datang !!"
            stop sound
            play sound dooropen1 volume 0.5
            scene 154
            amelia "Halo, saya datang untuk mengunjungi putri saya dan suaminya."
            amelia "Dia berambut merah panas seperti saya. Apakah Anda melihatnya?"
            scene 155
            mc "Ah, benarkah? Seorang berambut merah panas?"
            mc "Saya pikir saya benar -benar melihatnya sekarang. Heheh"
            scene 154
            amelia "Hahaha, mulut manis yang bagus."
            amelia "Ayo, biarkan aku memelukmu."
            stop sound
            scene 156
            amelia "Kemarilah!"
            mct "Apa?"
            amelia "Aku sangat merindukan kalian."
            scene 157
            mc "Hmm ... aku juga Amelia."
            amelia "Sekarang kalian tinggal di dekatnya, kita bisa menghabiskan lebih banyak waktu bersama."
            mc "Ya, aku-aku akan menyukainya!"
            scene 159
            mct "Sial, aku meraih pantatnya secara tidak sengaja."
            mct "Dia melompat pada saya, itu bukan salah saya."
            scene 160
            ameliat "Astaga! Saraf orang ini."
            ameliat "He's squeezing my ass and pretending nothing happened."
            ameliat "Aku juga bisa berpura -pura, pria besar."
            scene 157
            amelia "Dan lihat rumahmu!"
            amelia "Sangat indah. Anda dan [Violet] diberkati."
            amelia "Saya berharap ayahnya bisa berada di sini untuk melihat seberapa banyak dia tumbuh."
            amelia "Saya yakin dia akan bangga padanya."
            scene 158
            mc "Ya tentu ... saya tahu dia akan melakukannya."
            mct "Bukankah dia marah karena tanganku ada di pantatnya?"
            mct "Mungkin dia tidak menyadarinya."
            mct "Kira saya harus berpura -pura saya juga tidak menyadarinya."
            scene 160
            ameliat "Dia semakin berani di sekitarku sekarang."
            ameliat "Dia sangat pemalu sebelumnya."
            ameliat "Jika ini terjadi tidak lama sebelum dia sudah meminta maaf seperti orang gila."
            scene 159
            mct "Oh sial! Aku semakin keras, dia menekan penisku."
            mct "Dia pasti akan merasakannya sekarang."
            scene 160
            ameliat "Apa itu? Apakah itu penis yang saya rasakan di antara kedua kaki saya?"
            ameliat "Dia menjadi bersemangat anak malang itu."
            ameliat "Saya harus berhenti sebelum dia terlalu bersemangat."
            scene 157
            amelia "[mcname], anda bisa menurunkan saya sekarang ..."
            mc "Hmm ... ya benar, mari masuk ke dalam sekarang. Semakin gelap di luar."
            amelia "Tentu."
            play sound doorclose volume 0.5
            scene 161
            mc "Jadi, bagaimana Jeff memperlakukan Anda setelah satu tahun menikah?"
            amelia "Oh, dia benar -benar madu. Kami saling mencintai setiap hari."
            mc "Itu bagus untuk didengar."
            mc "Kenapa dia tidak ikut denganmu?"
            amelia "Dia terjebak di tempat kerja. Tapi dia pasti akan segera sampai di sini."
            mc "Jadi begitu."
            stop sound
            play sound doorknock volume 0.4
            scene 162
            amelia "Bicaralah tentang iblis."
            jeff "Di sinilah saya, maaf atas keterlambatannya."
            mc "Biarkan aku membuka pintu untukmu."
            stop sound
            play sound dooropen1 volume 0.5
            scene 163
            jeff "Halo nak, senang bertemu denganmu lagi."
            jeff "Itu rumah yang indah yang kalian miliki di sini."
            stop sound
            scene 164
            mc "Terima kasih Jeff, setelah tiga tahun kami akhirnya bisa membeli rumah impian kami."
            mc "[violet] menyukainya!"
            scene 163
            jeff "Saya yakin dia melakukannya."
            jeff "Dimana dia?"
            scene 165
            amelia "Ya. Dimana putriku?"
            mc "Saya pikir dia masih di kamar mandi, Anda tahu bagaimana keadaannya."
            amelia "Ya, saya tahu hehe."
            scene 166
            mc "Ayo di Jeff, rasakan di rumah."
            mc "Aku akan mulai membuat makan malam sambil menunggunya."
            scene 165
            amelia "Aku akan membantumu sayang."
            mc "Terima kasih, tapi Anda tidak perlu melakukannya. Anda adalah tamu kami."
            amelia "Saya ingin, tidak berdebat oke?"
            mc "Baik, kamu menang."
            scene 166
            mc "Anda bisa menyesuaikan diri dengan Jeff."
            mc "Mi Casa es Su Casa!"
            jeff "Terima kasih."
            scene blackscreen
            pause 0.6
            scene 167
            jefft "Hmm ... jadi, hot kecil [Violet] sedang mandi sekarang saat [McName] dan Amelia sibuk makan malam."
            jefft "Menarik..."
            jefft "Ini bisa jadi bagus."
            stop music fadeout 1.5
            scene 168
            play music showeroutside fadein 3.0 volume 0.2
            jefft "Pintunya terbuka."
            jefft "Ini pasti hari keberuntunganku!"
            jefft "Saya harus melihat ini!"
            scene 169
            jefft "Sial, lihat pantat itu !!"
            jefft "Saya tidak menyadari bahwa dia sangat seksi ketika saya menikah dengan ibunya."
            jefft "Sepertinya apel tidak jatuh jauh dari pohon."
            jefft "[mcname] adalah pria yang beruntung!"
            jefft "Apa yang tidak akan saya berikan untuk menidurinya setiap hari."
            stop music fadeout 1.5
            scene 170
            play music showerinside
            jefft "Saya perlu melihatnya dari dekat."
            scene 206
            play sound dooropen2 volume 2.0
            jefft "Ini dia."
            scene 207
            jefft "Sungguh! Pintu itu sangat keras!"
            scene 208
            v "Sayang, berhentilah terburu -buru."
            scene 209
            v "Sudah kubilang aku keluar dalam waktu sebentar ..."
            stop sound
            scene 211
            play sound chockfemale fadein 0.1
            v "ASTAGA!!"
            scene 212
            v "Apa yang kamu lakukan di sini ???"
            scene 213
            jeff "Tenang, tenang! Silakan."
            jeff "Saya bisa menjelaskan."
            scene 214
            jeff "Tolong jangan berteriak."
            jeff "Apakah Anda ingin mereka mendengar kami?"
            scene 212
            v "Apakah Anda tidak tahu Anda harus mengetuk sebelum Anda membuka pintu ??"
            scene 215
            jeff "Saya tahu, maaf ..."
            jeff "Saya hanya tidak tahu Anda ada di sini. Saya hanya mencoba menemukan kamar mandi."
            jeff "Amelia membantu [McName] dengan makan malam dan dia bilang aku bisa bertanya -tanya di sekitar rumah."
            jeff "Saya benar -benar perlu buang air kecil!"
            scene 217
            v "Tetap! Anda bisa mengetuk dulu!"
            scene 216
            jeff "Anda benar, itu hanya ... Saya perlu buang air kecil, saya tidak berpikir."
            scene 217
            v "Dan mengapa Anda masih berdiri di sana?! Tidak bisakah kamu melihat aku malu?"
            scene 218
            jeff "Oh, benar, maafkan aku ..."
            jeff "Lihat, saya tidak melihat."
            scene 219
            jeff "Saya bahkan akan berbalik."
            scene 220
            v "Aku masih lebih suka kamu keluar ..."
            v "Saya hampir selesai. Lima menit lagi dan saya akan keluar."
            v "Anda dapat menggunakan toilet setelah saya pergi."
            scene 221
            jeff "Ahh ayolah! Saya tidak bisa menahannya selama lima menit lagi."
            jeff "Tidak bisakah kau membiarkan aku masuk sebentar?"
            jeff "Anda bisa menyelesaikannya saat kencing. Dengan begitu mereka tidak akan menunggu kita terlalu lama."
            scene 223
            v "Apa? Anda tidak bisa serius."
            scene 221
            jeff "Aku bersumpah aku tidak akan melihatmu."
            jeff "Ayo. Ini akan lebih cepat dengan cara ini. Mereka menunggu kami di dapur ..."
            scene 222
            vt "Kotoran. Dia benar, [McName] mungkin bertanya -tanya mengapa saya mengambil Soo lama."
            vt "Tapi apakah ini terlalu banyak?"


            menu:
                "Jangan biarkan dia kencing":
                    $ dont_let_him_pee = "1"
                    $ let_him_pee = "2"
                    scene 223
                    v "Maaf Jeff, tapi kamu harus menunggu."
                    v "Ini terlalu banyak."
                    scene 221
                    jeff "Oke tidak masalah..."
                    jefft "Sungguh! Lain kali saya harus lebih tegas."
                    stop music fadeout 2.0
                    play sound endupdate fadein 2.0 volume 0.5
                    scene blackscreen
                    pause 0.5
                    centered "__Tag_0____tag_1__pisode 2__tag_2____tag_3__"
                    centered "__Tag_0____tag_1__2 tahun yang lalu__tag_2____tag_3__"
                    stop sound
                "Biarkan dia kencing":


                    $ let_him_pee = "1"
                    $ dont_let_him_pee = "2"
                    vt "Dia hanya akan kencing dan keluar."
                    vt "Saya kira tidak apa -apa."
                    scene 223
                    v "Baiklah Jeff, kamu bisa masuk. Tapi jangan lihat aku."
                    v "Dan tolong, cepatlah."
                    scene 224
                    jeff "Tentu, saya akan."
                    jefft "Tidak percaya dia membiarkan saya masuk. Itu sempurna!"
                    stop music
                    play music neighborhood fadein 2.5 volume 0.2
                    scene blackscreen
                    narrador "Pada saat yang sama..."
                    scene 205
                    mct "[violet] terlalu lama di kamar mandi ..."
                    mct "Aku akan membawanya keluar dari sana."
                    mct "Jeff pergi untuk beberapa waktu sekarang juga."
                    mct "Tunggu ... apakah saya menutup pintu setelah saya keluar dari kamar mandi?"
                    scene 210
                    play sound heartbeatslow volume 0.5 loop
                    mct "Kotoran! Tidak mungkin."
                    mct "Saya perlu memeriksanya sekarang!"
                    scene 225
                    mct "Apa? Jeff pergi di kamar mandi."
                    mct "[violet] pasti sudah keluar dari sana, kan?"
                    scene 226
                    play sound dooropen1 volume 0.3
                    mc "Sayang, apakah kamu disana?"
                    scene 227
                    play sound heartbeatfast volume 0.5 loop
                    mct "Kotoran!"
                    mct "Dia tidak ada di sini!"
                    mct "Itu artinya ..."
                    scene 228
                    mct "[ungu]!"
                    scene 229
                    mct "Mustahil! Dia menutup pintu."
                    mct "Sungguh! Apa yang harus saya lakukan?"
                    mct "Saya tidak mengerti apa yang saya rasakan saat ini."
                    mct "Saya tidak bisa berpikir jernih."
                    mct "Ini ... perasaan ini."
                    mct "Saya merasa seperti ini sebelumnya."
                    mct "Pertama kali kami datang ke kota ini ..."
                    stop sound
                    stop music fadeout 2.0
                    play sound endupdate fadein 2.0 volume 0.5
                    scene blackscreen with fade
                    pause 0.5
                    centered "__Tag_0____tag_1__pisode 2__tag_2____tag_3__"
                    centered "__Tag_0____tag_1__2 tahun yang lalu__tag_2____tag_3__"
                    stop sound


    jump ep2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
