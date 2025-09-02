define rb = Character("Larry")
define rm = Character("Helena")

label rowenavisit:
    $ Hour += 1
    $ rvisit = 1
    scene row_visit with fade
    "..."
    scene row_visit1 with dissolve
    s "Dimana kita bisa berubah?"
    a "Follow me"
    scene row_visit2 with dissolve
    s "Kami akan kembali"
    b "Ok"
    scene black
    "..."
    scene row_visit3 with fade
    a "Sepertinya seseorang sedang mengawasi kami"
    s "Siapa?"
    a "Jangan lihat, hanya ada [bname] di sini"
    scene row_visit4 with dissolve
    s "Ya ampun!"
    if stalkb_rowena >= 1:
        s "Sudah kubilang dia terobsesi denganmu"
        if bikini3 == 2:
            s "Dia membeli ini untuk pemotretan saya"
            s "Cobalah"
            scene row_visit19 with fade
            b "{i}(Oh yeah){/i}"
            s "Wow amazing"
            s "{i} (Saya ingin tahu apa yang terjadi dengan [bname] sekarang hahaha) {/i}"
            pass
        else:
            pass
    else:
        pass
    s "Biarkan berubah di dalam"
    a "Ok"
    a "Menurut Anda mana yang harus saya pakai?"
    scene row_visit5 with dissolve
    b "{i} (oh sialan mereka masuk) {/i}"
    scene row_visit6 with fade
    b "Hmmm"
    if srel <=150:
        scene row_visit7 with dissolve
        a "Bikini yang bagus [sname]"
        scene row_visit8 with dissolve
        s "Thanks"
        b "Oh hi there"
        b "Biarkan berenang?"
        s "Yeah"
        a "Bukan untuk saya, maaf"
        s "Mengapa?"
        a "Tidak pandai dalam hal itu"
        a "Silakan, jangan keberatan saya, saya akan kecokelatan"
        scene row_visit9 with fade
        b "Aha!"
        scene row_visit10 with dissolve
        b "Anda pikir Anda cepat, hahaha"
        scene row_visit11 with dissolve
        s "Bllllehhh"
        b "Tangkap saya jika Anda bisa"
        scene row_visit12 with dissolve
        "..."
        scene row_visit13 with dissolve
        b "Huh"
        scene row_visit14 with fade
        a "Saya melakukan laser, setiap 2 minggu sekali"
        a "Anda?"
        s "Saya baru saja mencukur hari ini"
        b "Hai perempuan, apa yang kamu bicarakan"
        scene row_visit15 with dissolve
        s "Gadis berbicara, bukan urusanmu"
        a "Let \'s Go Change [sname]"
        scene row_visit16 with dissolve
        b "Apa ..."
        scene row_visit17 with fade
        b "Berengsek..."
        "..."
        s "Let \'s Go [bname]"
        scene row_visit18 with dissolve
        b "Huh, ya tentu"
        scene broom_day with fade
        "..."
        call screen gnav

    elif srel >150 and bikini1 ==2:
        jump rowenapoolfix


    elif srel >150:
        jump rowenapoolfix
    else:

        scene row_visit7 with dissolve
        a "Bikini yang bagus [sname]"
        scene row_visit8 with dissolve
        s "Thanks"
        b "Oh hai disana"
        b "Biarkan berenang?"
        s "Yeah"
        a "Bukan untuk saya, maaf"
        s "Mengapa?"
        a "Tidak pandai dalam hal itu"
        a "Silakan, jangan keberatan saya, saya akan kecokelatan"
        scene row_visit9 with fade
        b "Aha!"
        scene row_visit10 with dissolve
        b "Anda pikir Anda cepat, hahaha"
        scene row_visit11 with dissolve
        s "Bllllehhh"
        b "Tangkap saya jika Anda bisa"
        scene row_visit12 with dissolve
        "..."
        scene row_visit13 with dissolve
        b "Huh"
        scene row_visit14 with fade
        a "Saya melakukan laser, setiap 2 minggu sekali"
        a "Anda?"
        s "Saya baru saja mencukur hari ini"
        b "Hai perempuan, apa yang kamu bicarakan"
        scene row_visit15 with dissolve
        s "Gadis berbicara, bukan urusanmu"
        a "Let \'s Go Change [sname]"
        scene row_visit16 with dissolve
        b "Apa ..."
        scene row_visit17 with fade
        b "Berengsek..."
        "..."
        s "Let \'s Go [bname]"
        scene row_visit18 with dissolve
        b "Huh, ya tentu"
        scene broom_day with fade
        "..."
        call screen gnav

label rowenapoolfix:
    if day ==3:
        jump rowenapool35
    elif day == 5:
        jump rowenapool35

    elif day ==1 and rowena_mom >=1:
        jump rowenapool35

    elif stalkb_rowena ==3:
        scene row_visit7b with dissolve
        s "Bikini yang bagus"
        scene row_visit8b with dissolve
        a "Thank youuu"
        b "Oh hai disana"
        b "Biarkan berenang?"
        s "Yeah"
        a "Bukan untuk saya, maaf"
        s "Mengapa?"
        a "Tidak pandai dalam hal itu"
        a "Silakan, jangan keberatan saya, saya akan kecokelatan"
        scene row_visit10b with fade
        if rowenaslap ==0:
            s "Hei, coba sekarang"
            b "Coba apa?"
            s "Duh! Bicaralah dengannya lagi"
            b "Tetapi..."
            $ rowenaslap = 1
            s "Dengarkan dia menaruh bikini baru ini untukmu"
            b "Menurutmu begitu?"
            s "Percayalah, saya seorang gadis, saya tahu"
            b "Ok"
            scene row_visit11b with dissolve
            s "..."
            scene row_visit11bg with hpunch
            s "Hah!"
            scene row_visit12b with dissolve
            s "{i} (apa yang terjadi) {/i}"
            s "{i} (sudah waktunya untuk mengganggu) {/i}"
            scene row_visit14b with fade
            s "Jadi Rowena bagaimana pelajaranmu?"
            a "Semua baik"
            s "Bagus"
            s "Saya pikir sudah waktunya berubah, kami tidak ingin terlambat"
            a "Ok"
            scene row_visit16b with dissolve
            "..."
            scene row_visit17 with fade
            b "{i} (sialan itu satu tamparan) {/i}"
            "..."
            scene row_visit18 with fade
            s "Let \'s Go [bname]"
            b "Huh, ya tentu"
            scene broom_day with fade
            "..."
            call screen gnav
        else:


            b "Anda pikir Anda cepat, hahaha"
            scene row_visit11a with dissolve
            s "Bllllehhh"
            b "Tangkap saya jika Anda bisa"
            scene row_visit12 with dissolve
            "..."
            scene row_visit13c with dissolve
            b "Huh"
            scene row_visit14c with fade
            a "Saya melakukan laser, setiap 2 minggu sekali"
            a "Anda?"
            s "Saya baru saja mencukur hari ini"
            b "Hai perempuan, apa yang kamu bicarakan"
            scene row_visit15b with dissolve
            s "Gadis berbicara, bukan urusanmu"
            if skiss_asked == 1:
                if rdf ==0:
                    scene row_visit17b with dissolve
                    "Hai sayang"
                    a "Huh"
                    $ rdf = 1
                    a "Sayang kamu di sini"
                    scene row_visit18b with dissolve
                    "..."
                    scene row_visit19b with dissolve
                    a "Teman -teman, temui Larry pacarku"
                    a "Larry, ini [sname]"
                    rb "Hi"
                    s "Hi Larry"
                    scene row_visit20b with dissolve
                    rb "Dan siapa kamu?"
                    b "[bname]"
                    b "Saya \ m [sname] pacar"
                    scene row_visit21b with dissolve
                    s "..."
                    rb "Keren kalau begitu, biarkan berenang"
                    a "Ya..."
                    s "Tidak ada Rowena, kita harus pergi"
                    s "Lain kali pasti"
                    a "Ok sampai jumpa"
                    s "Let \'s Go [bname]"
                    scene broom_day with fade
                    "..."
                    call screen gnav
                else:

                    scene row_visit17b with dissolve
                    "Hai sayang"
                    a "Sayang kamu di sini"
                    scene row_visit18b with dissolve
                    "..."
                    scene row_visit20b with fade
                    rb "Jadi, kali ini kita berenang?"
                    a "Ya, mereka tidak akan mengatakan tidak"
                    scene row_visit22b with dissolve
                    "..."
                    scene row_visit23b with fade
                    "..."
                    scene row_visit24b with dissolve
                    rb "Hei [bname] Bisakah Anda melakukan hal yang sama?"
                    if rbkisscounter <=1:
                        b "Berbuat salah..."
                        $ rbkisscounter += 1
                        s "Saya pikir sudah saatnya kita pergi"
                        a "Ok sampai jumpa"
                        s "Let \'s Go [bname]"
                        scene black
                        "Coba lebih banyak"
                        scene broom_day with fade
                        "..."
                        call screen gnav
                    else:

                        pass
                    b "..."
                    scene row_visit25b with dissolve
                    s "Huh"
                    scene row_visit26b with dissolve
                    "..."
                    $ skiss = 1
                    scene row_visit27b with fade
                    b "Bagaimana itu?"
                    rb "Hmm"
                    s "[bname] Turunkan aku, saatnya kita pergi"
                    rb "Tunggu teman -teman, mengapa kita tidak melanjutkan ini di pantai"
                    s "Oh sudah terlambat sekarang"
                    a "Let \'s Go, itu di dekatnya, kami tidak akan terlambat"
                    menu:
                        "Meyakinkannya untuk pergi":
                            b "Ini kedengarannya ide yang bagus"
                            b "Ayo [sname]"
                            s "Aku tidak tahu"
                            b "Ok rowena, kami pergi"
                            if rowena_mom >=1:
                                scene row_visit79b with dissolve
                                rm "Hai teman -teman! Pergi ke pantai?"
                                a "Yes"
                                menu:
                                    "Dia akan ikut denganmu":
                                        rm "Aku akan ikut denganmu, aku tidak ada hubungannya"
                                        jump nudebeach_rowenamom
                                    "Dia menang":

                                        rm "Ok enjoy"
                                        jump nudebeach_rowena
                            else:


                                jump nudebeach_rowena
                        "Melanjutkan":

                            pass

                    scene broom_day with fade
                    "..."
                    call screen gnav
            else:
                pass
            a "Let \'s Go Change [sname]"
            scene row_visit16b with dissolve
            "..."
            scene row_visit17 with fade
            "..."
            scene row_visit18 with fade
            s "Let \'s Go [bname]"
            b "Huh, ya tentu"
            scene broom_day with fade
            "..."
            call screen gnav
    else:

        pass


    scene row_visit7a with dissolve
    a "Bikini yang bagus [sname]"
    scene row_visit8a with dissolve
    s "Thanks"
    b "Oh hai disana"
    b "Biarkan berenang?"
    s "Yeah"
    a "Bukan untuk saya, maaf"
    s "Mengapa?"
    a "Tidak pandai dalam hal itu"
    a "Silakan, jangan keberatan saya, saya akan kecokelatan"
    scene row_visit9a with fade
    b "Aha!"
    scene row_visit10a with dissolve
    b "Anda pikir Anda cepat, hahaha"
    scene row_visit11a with dissolve
    s "Bllllehhh"
    b "Tangkap saya jika Anda bisa"
    scene row_visit10a with dissolve
    s "Tunggu!"
    s "Mengapa Anda tidak berbicara dengannya"
    b "Hah!"
    b "Anda pikir begitu?"
    s "Ya lakukan itu"
    menu:
        "Lakukan itu":
            $ stalkb_rowena = 3
            scene row_visit11c with fade
            s "{i} (keren) {/i}"
            s "{i} (atau ...) {/i}"
            s "{i} (.. mungkin saya harus membantunya) {/i}"
            scene row_visit14d with fade
            s "Halo, apa yang kamu bicarakan?"
            a "Tidak ada, hanya barang normal"
            "..."
            "Anda mengobrol untuk sedikit lebih banyak dan gadis -gadis itu memutuskan saatnya untuk berubah"
            scene row_visit16a with dissolve
            b "..."
            scene row_visit17 with fade
            b "Berengsek..."
            "..."
            s "Let \'s Go [bname]"
            scene row_visit18 with dissolve
            b "Huh, ya tentu"
            scene broom_day with fade
            "..."
            call screen gnav
        "Berpura -pura malu":

            b "Tidak, saya tidak bisa ..."
            s "Hmmm"
            s "Mau mu"
            pass

    scene row_visit12 with dissolve
    "..."
    scene row_visit13a with dissolve
    b "Huh"
    scene row_visit14a with fade
    a "Saya melakukan laser, setiap 2 minggu sekali"
    a "Anda?"
    s "Saya baru saja mencukur hari ini"
    b "Hai perempuan, apa yang kamu bicarakan"
    scene row_visit15a with dissolve
    s "Gadis berbicara, bukan urusanmu"
    a "Let \'s Go Change [sname]"
    scene row_visit16a with dissolve
    b "Apa ..."
    scene row_visit17 with fade
    b "Berengsek..."
    "..."
    s "Let \'s Go [bname]"
    scene row_visit18 with dissolve
    b "Huh, ya tentu"
    scene broom_day with fade
    "..."
    call screen gnav

label rowenapool35:
    scene row_visit7b with dissolve
    s "Bikini yang bagus"
    scene row_visit8b with dissolve
    a "Thank youuu"
    b "Oh hai disana"
    b "Biarkan berenang?"
    s "Yeah"
    a "Mari kita mendapatkan cokelat terlebih dahulu"
    a "Lalu kami menyegarkan dengan berenang"
    if rdf ==0:
        scene row_visit17b with dissolve
        "Hai sayang"
        a "Huh"
        $ rdf = 1
        a "Sayang kamu di sini"
        scene row_visit18b with dissolve
        "..."
        scene row_visit19b with dissolve
        a "Teman -teman, temui Larry pacarku"
        a "Larry, ini [sname]"
        rb "Hi"
        s "Hi Larry"
        scene row_visit20b with dissolve
        rb "Dan siapa kamu?"
        b "[bname]"
        b "Saya \ m [sname] pacar"
        scene row_visit21b with dissolve
        s "..."
        rb "Keren kalau begitu, biarkan berenang"
        a "Ya..."
        s "Tidak ada Rowena, kita harus pergi"
        s "Lain kali pasti"
        a "Ok sampai jumpa"
        s "Let \'s Go [bname]"
        scene broom_day with fade
        "..."
        call screen gnav
    else:
        scene row_visit17b with dissolve
        "Hai sayang"
        a "Sayang kamu di sini"
        if rowenamove >=1:
            b "{i} (Saya pikir dia bertengkar dengannya) {/i}"
        else:
            pass
        scene row_visit18b with dissolve
        "..."
        scene row_visit20b with fade
        rb "Jadi, kali ini kita berenang?"
        a "Ya, mereka tidak akan mengatakan tidak"
        scene row_visit22b with dissolve
        "..."
        scene row_visit23b with fade
        "..."
        scene row_visit24b with dissolve
        rb "Hei [bname] Bisakah Anda melakukan hal yang sama?"
        if srel <350:
            b "Berbuat salah..."
            $ rbkisscounter += 1
            s "Saya pikir sudah saatnya kita pergi"
            a "Ok sampai jumpa"
            s "Let \'s Go [bname]"
            scene black
            "Dapatkan hubungan [sname] lebih tinggi dari 350"
            scene broom_day with fade
            "..."
            call screen gnav
        else:

            pass
        b "..."
        scene row_visit25b with dissolve
        s "Huh"
        scene row_visit26b with dissolve
        "..."
        $ skiss = 1
        scene row_visit27b with fade
        b "Bagaimana itu?"
        rb "Hmm"
        s "[bname] Turunkan aku, saatnya kita pergi"
        rb "Tunggu teman -teman, mengapa kita tidak melanjutkan ini di pantai"
        s "Oh sudah terlambat sekarang"
        a "Let \'s Go, itu di dekatnya, kami tidak akan terlambat"
        menu:
            "Meyakinkannya untuk pergi":
                b "Ini kedengarannya ide yang bagus"
                b "Ayo [sname]"
                s "Aku tidak tahu"
                b "Ok rowena, kami pergi"
                if rowena_mom >=1:
                    scene row_visit79b with dissolve
                    rm "Hai teman -teman! Pergi ke pantai?"
                    a "Yes"
                    menu:
                        "Dia akan ikut denganmu":
                            rm "Aku akan ikut denganmu, aku tidak ada hubungannya"
                            jump nudebeach_rowenamom
                        "Dia menang":

                            rm "Ok enjoy"
                            jump nudebeach_rowena
                else:


                    jump nudebeach_rowena
            "Mari kita tinggal di sini":


                pass

        scene row_visit28b with fade
        b "{i} (wow keduanya ...) {/i}"
        scene row_visit29b with dissolve
        b "{i} (kelinci terangsang) {/i}"
        $ rowenabffuck = 1
        scene row_visit30b with dissolve
        "..."
        scene row_visit31b with dissolve
        s "..."
        scene row_visit32b with dissolve
        a "Ahhh"
        scene row_visit33b with dissolve
        a "Jangan keberatan kami, lakukan sesuatu"
        scene row_visit34b with dissolve
        s "Apa yang kita lakukan?"
        menu:
            "Biarkan berenang":
                s "Ok"
                scene row_visit12b with fade
                a "Ahhhh"
                s "Wow, mereka seperti kelinci terangsang"
                b "Apa yang mereka lakukan?"
                s "Dia mengendarainya"
                b "Mungkin dia menidurinya di pantat"
                scene row_visit35b with dissolve
                s "Wow"
                b "Lihat saya katakan"
                s "Bagaimana Anda tahu?"
                scene row_visit36b with dissolve
                a "Persetan dengan penis besar Anda"
                scene row_visit37b with dissolve
                s "..."
                if scorr >=100:
                    s "Mari ikut saya"
                    scene row_visit38b with dissolve
                    b "Apa?"
                    scene row_visit39b with dissolve
                    s "Persetan denganku sekarang"
                    scene row_visit40b with dissolve
                    s "Yess"
                    scene row_visit41b with dissolve
                    s "Beri aku yang besar itu"
                    scene row_visit42b with dissolve
                    s "Ahh"
                    scene row_visit43b with dissolve
                    s "..."
                    if day == 5 and srel >=450:
                        scene row_visit44b with dissolve
                        s "Lagi!"
                        scene row_visit45b with dissolve
                        s "Ah"
                        s "More"
                        scene row_visit46b with dissolve
                        s "Yesss!"
                        "Baiklah dengan baik"
                        scene row_visit47b with dissolve
                        $ rowena_mom = 1
                        "Pesta di rumah saya"
                        menu:
                            "Berlari":
                                b "{i}(Fuck){/i}"
                                s "Let \'s Go [bname]"
                                scene broom_day with fade
                                "..."
                                call screen gnav
                            "Melanjutkan":

                                b "{i}(Fuck){/i}"
                                s "Let \'s Go [bname]"
                                scene row_visit52b with dissolve
                                rm "Berhenti!"
                                scene row_visit53b with dissolve
                                rm "Ikut dengan saya, saya akan memberi tahu orang tuamu tentang ini"
                                scene row_visit54b with fade
                                rm "Wait here"
                                scene row_visit55b with dissolve
                                b "..."
                                scene row_visit56b with fade
                                rm "Hmm"
                                scene row_visit57b with dissolve
                                rm "Berlantai"
                                scene row_visit58b with vpunch
                                b "Huh"
                                rm "Saya bilang naik lantai"
                                rm "Tidak ada yang meniduri di tempat saya!"
                                scene row_visit59b with dissolve
                                rm "Except me"
                                scene row_visit60b with dissolve
                                b "Ah!"
                                scene row_visit61b with dissolve
                                rm "{i} (anak baik! Saya perlu menemukan cara untuk membuatnya tetap ada) {/i}"
                                scene row_visit62b with dissolve
                                rm "Hmmm"
                                scene row_visit63b with dissolve
                                rm "Yes"
                                scene row_visit64b with dissolve
                                rm "Ya, jilat"
                                scene row_visit65b with fade
                                s "{i} (Aku ingin tahu ke mana dia membawanya) {/i}"
                                scene row_visit66b with fade
                                rm "Siap mengambilnya"
                                scene row_visit67b with dissolve
                                b "Ahh!"
                                rm "Giliran saya sekarang"
                                scene row_visit68b with dissolve
                                "..."
                                scene row_visit69b with dissolve
                                "..."
                                scene row_visit70b with fade
                                b "Ughh"
                                scene row_visit71b with dissolve
                                b "..."
                                scene row_visit72b with dissolve
                                $ persistent.unlock_24 = True
                                rm "Lakukan dengan benar"
                                b "Yes"
                                scene row_visit73b with hpunch
                                b "Saya akan melakukannya dengan benar"
                                scene row_visit74b with dissolve
                                rm "Ahh"
                                scene row_visit75b with fade
                                b "Fuck"
                                scene row_visit76b with dissolve
                                "..."
                                scene row_visit77b with dissolve
                                "..."
                                scene row_visit78b with fade
                                s "Kemana saja kamu?"
                                b "Apa yang salah?"
                                s "Apa yang terjadi dengannya?"
                                b "Dia memberi kuliah, dan mengancam dia akan memberi tahu orang tua saya"
                                b "Dimana Rowena?"
                                s "Mereka melarikan diri sejak dia muncul"
                                b "Ayo biarkan pulang"
                                scene broom_day with fade
                                "..."
                                call screen gnav
                    else:
                        scene row_visit48b with dissolve
                        b "Yess"
                        s "Berbaring, berikan padaku"
                        scene row_visit49b with dissolve
                        b "Saya akan meledak"
                        scene row_visit50b with dissolve
                        "..."
                        scene row_visit51b with dissolve
                        b "Ahhh"
                        s "Mari pulang"
                        b "Yes"
                        scene broom_day with fade
                        "..."
                        call screen gnav
                else:

                    s "Let \'s Go [bname]"
                    b "{i}(Fuck){/i}"
                    "Meningkatkan korupsi menjadi 100"
                    pass
            "Mari kita melakukan hal yang sama":

                s "TIDAK!"
                b "Mau mu"
                s "Mari pulang"
                pass
        scene broom_day with fade
        "..."
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc