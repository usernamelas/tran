label elainebusiness:
    $ cselaine0 = 8
    $ Hour += 1
    scene ebiz with fade
    b "Mungkinkah dia tiba dan pergi?!"
    "..."
    play sound "sounds/knock.ogg"
    b "Dingin"
    stop sound
    if e_showsupagain == 2:
        $ e_showsupagain = 0
        $ ebizcheck += 3

        jump elainebusinessspecial
    else:

        $ ebizcheck += 1
        pass
    $ elbs = renpy.random.randint (1,4)
    if elbs >2:
        jump elainebusinessalt
    else:
        pass
    scene ebiz1 with dissolve
    e "Hi [bname]"
    if bworkstarted ==1:
        e "Dimana kamarmu?"
        b "Itu ada di sana, di sebelah kiri"
        e "Ok"
        e "Anda mungkin pergi sekarang, saya akan tetap membuka pintu utama"
        b "Errm ... uang?"
        e "Nanti [bname] Saya akan memberi Anda sesuatu yang lebih baik dari uang"
        b "{i} (apa -apaan!) {/i}"
        pass
    else:

        e "Ini uangmu"
        $ mny += 70
        $ renpy.notify (_("She gave you 70 $"))
        $ renpy.pause ( 5, 0)
        b "{i} (70 !! Apa -apaan!) {/i}"
        b "Thanks"
        e "Dimana kamarmu?"
        b "Itu ada di sana, di sebelah kiri"
        e "Ok"
        e "Anda mungkin pergi sekarang, saya akan tetap membuka pintu utama"
        pass
    scene ebiz with fade
    if camerafixing ==2:
        $ camerarecording = 1
    else:
        pass
    b "Hmmm"
    menu:
        "Periksa tangga" if windowfound ==1:
            b "{i} (mari kita lihat) {/i}"
            scene ebizstairs0 with fade
            $ ebizaldoneonce = 1
            "..."
            scene ebizstairs with fade
            b "Wow!"
            b "{i} (fuck, aku tidak bisa mengangkat kepalaku, mereka akan melihatku) {/i}"
            scene ebizstairs1 with dissolve
            b "..."
            $ elfk = renpy.random.randint (1,4)
            if elfk >2:
                scene ebizstairs2 with fade
                e "Aghhh"
                scene ebizstairs4 with dissolve
                e "Hmmm"
                scene ebizstairs5 with dissolve
                "..."
                scene ebizstairs6 with dissolve
                b "{i} (wow!) {/i}"
                e "Saya tidak bisa lagi"
                scene ebizstairs11 with fade
                "..."
                e "Tolong $ 2000"
                scene ebizstairs12 with dissolve
                b "{i} (waktu untuk kembali ke dalam) {/i}"
                scene black
                "..."
                scene ebizstairs13 with fade
                r "Kemana saja kamu?"
                e "Merampok! Ayo ayolah!"
                r "Jawab aku!"
                e "Saya pergi menemui [mname]!"
                e "Tolong, saya terlambat untuk bekerja"
                scene ebizstairs14 with dissolve
                r "..."
                scene black
                "..."
                scene ebizstairs15 with fade
                b "{i} (ini adalah uang mudah!) {/i}"
                scene ebizstairs16 with fade

                "$ 2000"
                b "Terima kasih"
                scene ebizstairs15 with fade
                b "Hmmm"
                b "{i} (mungkin suatu hari) {/i}"
                scene broom_night with fade
                "..."
                call screen gnav
            else:

                scene ebizstairs3 with fade
                e "Hmmm"
                scene ebizstairs7 with hpunch
                e "Ahhh"
                scene ebizstairs8 with dissolve
                e "Ahhh fuck!"
                e "More"
                scene ebizstairs7 with dissolve
                "..."
                scene ebizstairs9 with fade
                e "Ahhh"
                scene ebizstairs10 with dissolve
                e "Saya tidak bisa lagi"
                scene ebizstairs11 with fade
                "..."
                e "Tolong $ 2000"
                scene ebizstairs12 with dissolve
                b "{i} (mereka pergi) {/i}"
                scene black
                "..."
                scene ebizstairs13 with fade
                r "Kemana saja kamu?"
                e "Merampok! Ayo ayolah!"
                r "Jawab aku!"
                e "Saya pergi menemui [mname]!"
                e "Tolong, saya terlambat untuk bekerja"
                scene ebizstairs14 with dissolve
                r "..."
                scene black
                "..."
                scene ebizstairs15 with fade
                b "{i} (ini adalah uang mudah!) {/i}"
                scene ebizstairs16 with fade
                "$ 2000"
                b "Terima kasih"
                scene ebizstairs15 with fade
                b "Hmmm"
                b "{i} (mungkin suatu hari) {/i}"
                scene broom_night with fade
                "..."
                call screen gnav
        "Cobalah untuk melihat dari pintu":


            scene door with hpunch
            b "{i} (hebat dia menguncinya) {/i}"
            e "Hai!! Pergilah!"
            b "Maaf!"
            e "Tolong tinggalkan rumah, kembali lagi nanti"
            b "Ok Ok"
            scene black
            "..."
            scene hall_n with fade
            "..."
            scene ebizstairs15 with fade
            b "Sepertinya mereka selesai"
            scene broom_night with fade
            "..."
            call screen gnav
        "Duduk dan tunggu dia":

            scene ebizwait with fade
            b "{i} (i \ 'll tunggu dia) {/i}"
            "..."
            e "Hey there"
            scene ebizdone with dissolve
            e "Apa yang ada"
            if camexpose == 1:
                b "Saya ingin berbicara dengan Anda"
                e "Tentang apa?"
                menu:
                    "Ceritakan tentang kamera":
                        b "Nah, saya butuh bantuan Anda dengan [mname]"
                        e "Bantuan macam apa"
                        b "Aku mendengarmu beberapa hari yang lalu berbicara dengannya tentang"
                        b "Tentang pekerjaan"
                        e "Dan?"
                        b "Saya ingin Anda meyakinkannya untuk mengubah pekerjaannya"
                        scene ebizdone1 with dissolve
                        e "..."
                        e "Anda bermaksud bekerja dengan saya?"
                        b "Tidak perlu dengan Anda"
                        b "Tapi sepertimu"
                        e "[bname] Anda menyadari bahwa saya tidak memiliki kendali atas moralnya, kan?"
                        e "Anda mengenalnya"
                        b "Baik Anda lebih baik melakukannya"
                        e "Apa maksudmu?"
                        b "Anda tahu persis apa yang saya maksud"
                        e "Apa yang kamu bicarakan?"
                        b "Lihat apa yang saya miliki"
                        scene camscenes5 with fade
                        e "Uh huh"
                        e "Dan Anda berencana untuk menunjukkan ini kepada Rob, saya kira"
                        b "Tidak, saya belum mengatakan ini"
                        scene ebizdone2 with dissolve
                        e "Listen [bname]"
                        $ elaine_convince = 1
                        e "Mari kita luruskan"
                        e "Saya akan mencoba membantu Anda, bukan karena foto ini, tetapi karena saya membutuhkan kamar Anda"
                        e "Saya tidak bisa menyewa"
                        e "Saya akan melakukan yang terbaik"
                        b "Ok cukup adil"
                        e "Sampai jumpa"
                        b "Bye"
                        scene broom_night with fade
                        b "{i} (Mari kita lihat apa yang akan dia lakukan) {/i}"
                        call screen gnav
                    "Tidak ada":

                        pass
            else:
                pass

            b "Tidak ada, hanya menunggu Anda selesai"
            e "Benar, terima kasih, sampai jumpa lain kali"
            b "Ok bye"
            scene broom_night with fade
            "..."
            call screen gnav



label elainebusinessalt:
    scene ebiz1a with dissolve
    e "Hi [bname]"
    if bworkstarted ==1:
        e "Anda mungkin pergi sekarang, saya akan tetap membuka pintu utama"
        b "Errm ... uang?"
        e "Later [bname]"
        e "Saya akan memberi Anda sesuatu yang lebih baik dari uang"
        b "{i} (apa -apaan!) {/i}"
        pass
    else:

        e "Ini uangmu"
        $ mny += 70
        $ renpy.notify (_("She gave you 70 $"))
        $ renpy.pause ( 5, 0)
        b "{i} (70 !! Apa -apaan!) {/i}"
        b "Thanks"
        e "Dimana kamarmu?"
        b "Itu ada di sana, di sebelah kiri"
        e "Ok"
        e "Anda mungkin pergi sekarang, saya akan tetap membuka pintu utama"
        pass

    scene ebiz with fade
    if camerafixing ==2:
        $ camerarecording1 = 1
    else:
        pass
    b "Hmmm"
    menu:
        "Periksa tangga" if windowfound ==1:
            b "{i} (mari kita lihat) {/i}"
            scene ebizstairs0 with fade
            $ ebizaldoneonce = 1
            "..."
            scene ebizstairsa with fade
            b "Ohh wow!"
            b "{i} (fuck, aku tidak bisa mengangkat kepalaku, mereka akan melihatku) {/i}"
            scene ebizstairs1a with fade
            b "..."
            scene ebizstairs2a with dissolve
            "Yesss sayang"
            scene ebizstairs3a with dissolve
            e "Hmmm"
            scene ebizstairs2a with dissolve
            "Yess lebih"
            scene ebizstairs4a with dissolve
            "Saya datang"
            e "Lakukan sayang! Lakukan itu"
            scene ebizstairs5a with vpunch
            "Ahhh"
            b "{i} (wow!) {/i}"
            e "Hmmm sangat hangat"
            scene ebizstairs6a with fade
            "..."
            scene ebizstairs7a with dissolve
            "..."
            scene ebizstairs8a with fade
            b "{i} (Saya pikir mereka sudah selesai) {/i}"
            e "Aku mencintaimu"
            scene ebizstairs9a with dissolve
            "..."
            scene ebizstairs12 with dissolve
            b "{i} (waktu untuk kembali ke dalam) {/i}"
            scene black
            "..."
            scene ebizstairs13 with fade
            r "Kemana saja kamu?"
            e "Merampok! Ayo ayolah!"
            r "Jawab aku!"
            e "Saya pergi menemui [mname]!"
            e "Tolong, saya terlambat untuk bekerja"
            scene ebizstairs14 with dissolve
            r "..."
            scene black
            "..."
            scene ebizstairs15 with fade
            b "{i} (...) {/i}"
            scene broom_night with fade
            "..."
            call screen gnav
        "Cobalah untuk melihat dari pintu":




            scene door with hpunch
            b "{i} (hebat dia menguncinya) {/i}"
            e "Hai!! Pergilah!"
            b "Maaf!"
            e "Tolong tinggalkan rumah, kembali setelah 2 jam"
            b "Ok Ok"
            scene black
            "..."
            scene hall_n with fade
            "..."
            scene ebizstairs15 with fade
            b "Sepertinya mereka selesai"
            scene broom_night with fade
            "..."
            call screen gnav
        "Duduk dan tunggu dia":

            scene ebizwait with fade
            b "{i} (i \ 'll tunggu dia) {/i}"
            "..."
            e "Hey there"
            scene ebizdone with dissolve
            e "Apa yang ada"
            if camexpose == 1:
                b "Saya ingin berbicara dengan Anda"
                e "Tentang apa?"
                menu:
                    "Ceritakan tentang kamera":
                        b "Nah, saya butuh bantuan Anda dengan [mname]"
                        e "Bantuan macam apa"
                        b "Aku mendengarmu beberapa hari yang lalu berbicara dengannya tentang"
                        b "Tentang pekerjaan"
                        e "Dan?"
                        b "Saya ingin Anda meyakinkannya untuk mengubah pekerjaannya"
                        scene ebizdone1 with dissolve
                        e "..."
                        e "Anda bermaksud bekerja dengan saya?"
                        b "Tidak perlu dengan Anda"
                        b "Tapi sepertimu"
                        e "[bname] Anda menyadari bahwa saya tidak memiliki kendali atas moralnya, kan?"
                        e "Anda mengenalnya"
                        b "Baik Anda lebih baik melakukannya"
                        e "Apa maksudmu?"
                        b "Anda tahu persis apa yang saya maksud"
                        e "Apa yang kamu bicarakan?"
                        b "Lihat apa yang saya miliki"
                        scene camscenes5 with fade
                        e "Uh huh"
                        e "Dan Anda berencana untuk menunjukkan ini kepada Rob, saya kira"
                        b "Tidak, saya belum mengatakan ini"
                        scene ebizdone2 with dissolve
                        e "Listen [bname]"
                        $ elaine_convince = 1
                        e "Mari kita luruskan"
                        e "Saya akan mencoba membantu Anda, bukan karena foto ini, tetapi karena saya membutuhkan kamar Anda"
                        e "Saya tidak bisa menyewa"
                        e "Saya akan melakukan yang terbaik"
                        b "Ok cukup adil"
                        e "Sampai jumpa"
                        b "Bye"
                        scene broom_night with fade
                        b "{i} (Mari kita lihat apa yang akan dia lakukan) {/i}"
                        call screen gnav
                    "Tidak ada":

                        pass
            else:
                pass

            b "Tidak ada, hanya menunggu Anda selesai"
            e "Benar, terima kasih, sampai jumpa lain kali"
            b "Ok bye"
            scene broom_night with fade
            "..."
            call screen gnav


label elainebusinessspecial:
    scene ebiz1b with dissolve
    e "Hi [bname]"
    if bworkstarted ==1:
        e "Anda mungkin pergi sekarang, saya akan tetap membuka pintu utama"
        b "Errm ... uang?"
        e "Nanti [bname] Saya akan memberi Anda sesuatu yang lebih baik dari uang"
        b "{i} (apa -apaan!) {/i}"
        pass
    else:

        e "Ini uangmu"
        $ mny += 80
        $ renpy.notify (_("She gave you 80 $"))
        $ renpy.pause ( 5, 0)
        b "{i} (80 !! apa -apaan!) {/i}"
        b "Thanks"
        e "Anda mungkin pergi sekarang, saya akan tetap membuka pintu utama"
        pass
    scene ebiz with fade
    if camerafixing ==2:
        $ camerarecording2 = 1
    else:
        pass
    b "Hmmm"
    b "Hmmm"
    menu:
        "Periksa tangga" if windowfound ==1:
            b "{i} (mari kita lihat) {/i}"
            scene ebizstairs0 with fade
            $ ebizaldoneonce = 1
            "..."
            scene ebizstairsb with fade
            b "Ohh wow!"
            b "{i} (fuck, aku tidak bisa mengangkat kepalaku, mereka akan melihatku) {/i}"
            scene ebizstairs1b with fade
            e "Ayo Linara, jangan takut"
            "Saya tahu istri saya, dia malu, dia membutuhkan lebih dari sekadar kata -kata"
            scene ebizstairs2b with dissolve
            "Mulailah dengan membuatnya cemburu"
            scene ebizstairs3b with dissolve
            e "Hmmm"
            scene ebizstairs4b with dissolve
            "Bergabunglah dengan Linara -nya"
            scene ebizstairs5b with dissolve
            e "Ahhh"
            b "{i} (wow!) {/i}"
            scene ebizstairs6b with fade
            e "Ahh yes"
            scene ebizstairs7b with dissolve
            e "Ohhh"
            scene ebizstairs6b with fade
            e "Berikan padanya di mulutnya"
            scene ebizstairs8b with fade
            b "{i} (wow pantat ke mulut, tidak bisa dipercaya) {/i}"
            scene ebizstairs9b with dissolve
            "Ahhhh"
            scene ebizstairs12 with fade
            b "{i} (Saya pikir mereka sudah selesai) {/i}"
            scene black
            "..."
            scene ebizstairs13 with fade
            r "Kemana saja kamu?"
            e "Merampok! Ayo ayolah!"
            r "Jawab aku!"
            e "Saya pergi menemui [mname]!"
            e "Tolong, saya terlambat untuk bekerja"
            scene ebizstairs14 with dissolve
            r "..."
            scene black
            "..."
            scene ebizstairs15 with fade
            b "{i} (...) {/i}"
            scene broom_night with fade
            "..."
            call screen gnav
        "Cobalah untuk melihat dari pintu":




            scene door with hpunch
            b "{i} (hebat dia menguncinya) {/i}"
            e "Hai!! Pergilah!"
            b "Maaf!"
            e "Tolong tinggalkan rumah, kembali setelah 2 jam"
            b "Ok Ok"
            scene black
            "..."
            scene hall_n with fade
            "..."
            scene ebizstairs15 with fade
            b "Sepertinya mereka selesai"
            scene broom_night with fade
            "..."
            call screen gnav
        "Duduk dan tunggu dia":


            scene ebizwait with fade
            b "{i} (i \ 'll tunggu dia) {/i}"
            "..."
            e "Hey there"
            scene ebizdone with dissolve
            e "Apa yang ada"
            if camexpose == 1:
                b "Saya ingin berbicara dengan Anda"
                e "Tentang apa?"
                menu:
                    "Ceritakan tentang kamera":
                        b "Nah, saya butuh bantuan Anda dengan [mname]"
                        e "Bantuan macam apa"
                        b "Aku mendengarmu beberapa hari yang lalu berbicara dengannya tentang"
                        b "Tentang pekerjaan"
                        e "Dan?"
                        b "Saya ingin Anda meyakinkannya untuk mengubah pekerjaannya"
                        scene ebizdone1 with dissolve
                        e "..."
                        e "Anda bermaksud bekerja dengan saya?"
                        b "Tidak perlu dengan Anda"
                        b "Tapi sepertimu"
                        e "[bname] Anda menyadari bahwa saya tidak memiliki kendali atas moralnya, kan?"
                        e "Anda mengenalnya"
                        b "Baik Anda lebih baik melakukannya"
                        e "Apa maksudmu?"
                        b "Anda tahu persis apa yang saya maksud ..."
                        e "Apa yang kamu bicarakan?"
                        b "Lihat apa yang saya miliki"
                        scene camscenes5 with fade
                        e "Uh huh"
                        e "Dan Anda berencana untuk menunjukkan ini kepada Rob, saya kira"
                        b "Tidak, saya belum mengatakan ini"
                        scene ebizdone2 with dissolve
                        e "Listen [bname]"
                        $ elaine_convince = 1
                        e "Mari kita luruskan"
                        e "Saya akan mencoba membantu Anda, bukan karena foto ini, tetapi karena saya membutuhkan kamar Anda"
                        e "Saya tidak bisa menyewa"
                        e "Saya akan melakukan yang terbaik"
                        b "Ok cukup adil"
                        e "Sampai jumpa"
                        b "Bye"
                        scene broom_night with fade
                        b "{i} (Mari kita lihat apa yang akan dia lakukan) {/i}"
                        call screen gnav
                    "Tidak ada":

                        pass
            else:
                pass

            b "Tidak ada, hanya menunggu Anda selesai"
            e "Benar, terima kasih, sampai jumpa lain kali"
            b "Ok bye"
            scene broom_night with fade
            "..."
            call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
