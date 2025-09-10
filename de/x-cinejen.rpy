image bmwall:
    "bmwa00.jpg"
    pause 0.03
    "bmwa01.jpg"
    pause 0.03
    "bmwa02.jpg"
    pause 0.03
    "bmwa03.jpg"
    pause 0.03
    "bmwa04.jpg"
    pause 0.03
    "bmwa05.jpg"
    pause 0.03
    "bmwa06.jpg"
    pause 0.03
    "bmwa07.jpg"
    pause 0.03
    "bmwa08.jpg"
    pause 0.03
    "bmwa09.jpg"
    pause 0.03
    "bmwa10.jpg"
    pause 0.03
    "bmwa11.jpg"
    pause 0.03
    "bmwa12.jpg"
    pause 0.03
    "bmwa13.jpg"
    pause 0.03
    "bmwa14.jpg"
    pause 0.03
    "bmwa15.jpg"
    pause 0.03
    "bmwa16.jpg"
    pause 0.03
    "bmwa17.jpg"
    pause 0.03
    repeat

label cinejen:
    scene cinejen1 with fade
    b "Saya akan mendapatkan tiketnya"
    m "Tunggu, kita perlu memutuskan apa yang harus ditonton"
    scene cinejen2 with dissolve
    b "Mari kita coba malam yang dicuri?"
    m "Ya kenapa tidak"
    scene cinejen3 with dissolve
    b "2 tiket"
    m "Saya akan membayar untuk ini [bname]"
    scene cinejen4 with fade
    $ persistent.unlock_36 = True
    b "Saya berharap ini bagus"
    m "SHH, mulai"
    b "Ok"
    b "Haruskah saya memberi kita minuman dan popcorn?"
    m "Tolong minum saja"
    scene cinejen5 with fade
    "..."
    scene cinejen6 with dissolve
    m "Apakah ada alkohol dalam milkshake ini?"
    b "No"
    m "Weird"
    scene cinejen5 with fade
    m "Itu adalah film yang bagus"
    m "Let's go"
    menu:
        "Terima kasih":
            scene cinejen5a with dissolve
            m "Huh"
            b "SAYA.."
            b "Terima kasih untuk waktunya"
            show screen mrelup
            $ mrel += 5
            m "Terima kasih juga [bname]"
            hide screen mrelup
            pass
        "Melanjutkan":

            pass

    scene cinejen7 with fade
    m "Sepertinya [sname] tidak kembali"
    b "Mungkin dia di kamarnya"
    m "Panggil dia dan lihat di mana dia berada"
    m "Saya akan berubah"
    b "Ok"
    scene black
    "..."
    if mrel >=400:
        scene cinejen9 with fade
        m "Hah!"
        scene cinejen10 with dissolve
        b "Sorry"
        b "[sname] masih di Rowena"
        b "Dia bilang dia akan kembali terlambat"
        m "Ok"
        m "Pergi sekarang, aku akan sampai jumpa nanti"
        scene cinejen11 with fade
        b "{i} (wow!) {/i}"
        m "Apa yang sedang kamu lakukan?"
        b "Watching TV"
        m "Buat jalan, aku akan menonton denganmu"
        menu:
            "Ubah saluran":
                scene cinejen13 with dissolve
                m "Apa yang kamu tonton?"
                b "Saya baru saja mencari ..."
                pass
            "Jangan":
                scene cinejen14 with dissolve
                m "Hah!"
                scene cinejen15 with dissolve
                m "Astaga!"
                m "Anda tidak akan tumbuh dewasa"
                if mfuckedsober >= 1:
                    m "Dimana [sname]?"
                    b "Dia kembali terlambat katanya"
                    m "Apakah Anda memiliki kondom?"
                    b "Huh"
                    b "Mengapa"
                    m "Pergi mendapatkannya"
                    scene cinejen67 with fade
                    b "Wow"
                    m "Memakai kondom"
                    scene cinejen68 with fade
                    m "Saya akan mengajari Anda bagaimana menjadi baik"
                    m "Lakukan dengan lambat"
                    scene cjena
                    play sound "sounds/mpant.wav"
                    m "Ah"
                    "..."
                    "..."
                    m "Lambat"
                    "..."
                    stop sound
                    scene cinejen69 with dissolve
                    m "Hah! Apakah itu pintunya?"
                    m "Cepat pergi ke kamar saya"
                    scene cinejen70 with fade
                    s "Hi"
                    s "Mengapa meja ada?"
                    m "Jam berapa sekarang?"
                    s "Tapi saya katakan [bname] untuk memberi tahu Anda"
                    m "Pergi ke kamar Anda"
                    $ snupset += 1
                    "[sname] menjadi lebih kesal"
                    scene cinejen71 with dissolve
                    s "{i} (idiot itu dimana dia?!) {/i}"
                    scene door with fade
                    s "{i} (dia tidak ada di kamarnya, di mana dia bisa) {/i}"
                    s "{i} (i \ 'll periksa tangga) {/i}"
                    scene cinejen72 with dissolve
                    s "{i} (apa -apaan) {/i}"
                    scene cinejen73 with dissolve
                    s "..."
                    scene cinejen74 with dissolve
                    s "Astaga"
                    s "Saya harus pergi"
                    jump waitings1
                else:
                    pass
                $ mcorr += 1
                show screen mcorr
                b "Sorry"
                hide screen mcorr
                pass

        m "Dapatkan aku minuman"
        scene cinejen16 with fade
        m "Itu lebih baik sekarang"
        m "Saatnya melakukan kakiku"
        scene cinejen17 with dissolve
        b "Dengan senang hati"
        menu:
            "Mengintip":
                scene cinejen17c with dissolve
                b "{i} (sialan, kapan dia memakai ini!) {/i}"
                b "{i} (aku bersumpah ini bukan ada menit yang lalu) {/i}"
                pass
            "Jangan":
                pass
        "..."
        if springstring == 1:
            b "Ngomong -ngomong, aku punya sesuatu untukmu"
            scene cinejen17a with dissolve
            m "Apa itu?"
            m "Beri aku, aku akan mencobanya"
            scene cinejen17b with fade
            m "Anda tidak mengharapkan saya memakai ini ke pantai!"
            $ springstring = 2
            b "Saya tidak tahu, terserah Anda"
            scene cinejen18 with fade
            m "Continue"
            b "Sure"
            "..."
            scene cinejen19 with dissolve
            m "Saya pikir itu cukup"
            m "Aku akan tidur"
            scene cinejen20 with dissolve
            m "Hubungi [sname] dan periksa kapan dia kembali"
            b "Ok"
            scene cinejen21 with dissolve
            b "Hei, kapan kamu kembali?"
            s "{i} masih lebih awal mengapa? {/i}"
            if persistent.patch_enabled:
                b "Tidak ada, saya hanya ingin memberi tahu Anda"
                b "Ibu pergi tidur, kamu bisa meluangkan waktu"
                s "{i} ok keren, saya akan kembali dalam 2 jam {/i}"
                b "No worries"
                b "Dia bilang kamu bisa menginap malam"
                pass
            else:

                b "Tidak ada, saya hanya ingin memberi tahu Anda"
                b "[mname] pergi tidur, Anda bisa meluangkan waktu"
                s "{i} ok keren, saya akan kembali dalam 2 jam {/i}"
                b "No worries"
                b "Dia bilang kamu bisa menginap malam"
                pass

        if springstring == 2:
            b "Ngomong -ngomong, apakah Anda suka bikini itu?"
            scene cinejen17a with dissolve
            m "Yang mana?"
            b "Mesh hitam"
            m "Ah ya tidak buruk, tapi saya tidak akan memakainya"
            b "Mengapa tidak?"
            m "Hmm aku akan memberitahumu mengapa"
            m "Aku akan kembali"
            scene cinejen17b with fade
            m "Anda tidak mengharapkan saya memakai ini ke pantai!"
            $ springstring = 2
            b "Saya tidak tahu, terserah Anda"
            scene cinejen18 with fade
            m "Continue"
            b "Sure"
            "..."
            scene cinejen19 with dissolve
            m "Saya pikir itu cukup"
            m "Aku akan tidur"
            scene cinejen20 with dissolve
            m "Hubungi [sname] dan periksa kapan dia kembali"
            b "Ok"
            scene cinejen21 with dissolve
            b "Hei, kapan kamu kembali?"
            s "{i} masih lebih awal mengapa? {/i}"
            if persistent.patch_enabled:
                b "Tidak ada, saya hanya ingin memberi tahu Anda"
                b "Ibu pergi tidur, kamu bisa meluangkan waktu"
                s "{i} ok keren, saya akan kembali dalam 2 jam {/i}"
                b "No worries"
                b "Dia bilang kamu bisa menginap malam"
                pass
            else:

                b "Tidak ada, saya hanya ingin memberi tahu Anda"
                b "[mname] pergi tidur, Anda bisa meluangkan waktu"
                s "{i} ok keren, saya akan kembali dalam 2 jam {/i}"
                b "No worries"
                b "Dia bilang kamu bisa menginap malam"
                pass
        else:


            scene cinejen17a with dissolve
            m "Anda menjadi lebih baik"
            scene cinejen17 with dissolve
            m "Saya pikir itu cukup"
            m "Aku akan tidur"
            scene cinejenone with fade
            m "Hubungi [sname] dan periksa kapan dia kembali"
            b "Ok"
            scene cinejen21 with dissolve
            b "Hei, kapan kamu kembali?"
            s "{i} masih lebih awal mengapa? {/i}"
            if persistent.patch_enabled:
                b "Tidak ada, saya hanya ingin memberi tahu Anda"
                b "Ibu pergi tidur, kamu bisa meluangkan waktu"
                s "{i} ok keren, saya akan kembali dalam 2 jam {/i}"
                b "No worries"
                b "Dia bilang kamu bisa menginap malam"
                pass
            else:

                b "Tidak ada, saya hanya ingin memberi tahu Anda"
                b "[mname] pergi tidur, Anda bisa meluangkan waktu"
                s "{i} ok keren, saya akan kembali dalam 2 jam {/i}"
                b "No worries"
                b "Dia bilang kamu bisa menginap malam"
                pass

        scene cinejen22 with fade
        m "Ya!"
        b "Dia bilang dia akan tidur di sana"
        m "Weird"
        scene cinejen23 with dissolve
        m "Apa kamu yakin?"
        b "Yes"
        m "Aku akan meneleponnya"
        b "Hehe aku hanya bercanda, katanya dua jam"
        m "Tetap saja, saya harus berbicara dengannya"
        scene cinejen24 with dissolve
        m "Benarkah Anda akan tidur di sana?"
        scene cinejen25 with fade
        s "Apa? Siapa yang memberitahumu itu?"
        s "Saya akan datang dalam beberapa jam"
        "..."
        s "Masih 10 tahun, ayo!"
        scene cinejen24 with dissolve
        m "Ok jangan terlambat"
        scene cinejen22 with dissolve
        m "Selamat malam sayang"
        b "{i} (apa -apaan!) {/i}"
        menu:
            "Tunggu [sname]":
                jump waitings
            "Tonton beberapa porno berharap [sname] akan segera hadir":

                pass

        b "{i} (Saya pikir saya akan menunggu [sname]) {/i}"
        scene cinejen26 with fade
        b "{i} (Let \ 's Watch TV sampai dia datang) {/i}"
        scene black
        "Setelah beberapa waktu menonton film porno"
        scene cinejen11 with fade
        m "Dia belum kembali"
        b "Hah!"
        b "TIDAK!"
        scene cinejen27 with dissolve
        m "Astaga"
        m "Sekali lagi Anda menonton film porno"
        b "Err"
        scene cinejen15 with dissolve
        m "Bagaimana Anda mendapatkan semua saluran"
        b "It's DVD"
        scene cinejen28 with dissolve
        m "Ya Tuhan!"
        scene cinejen29 with dissolve
        b "Apa!"
        m "..."
        m "Apa yang Anda sebut ini?"
        scene cinejen30 with dissolve
        b "Ah yang ini hehehe"
        b "It's just"
        scene cinejen31 with dissolve
        b "It's bisexual"
        scene cinejen15 with dissolve
        m "Lihat [bname] Saya tidak menentang pilihan seksual yang Anda buat"
        scene cinejen32 with dissolve
        m "Tapi saya perlu tahu sekarang!"
        scene cinejen31 with dissolve
        m "{i} (apakah dia menggertak, karena saya perhatikan bagaimana dia memandang perempuan ...) {/i}"
        m "{i} (... dan pada saya) {/i}"
        m "{i} (ada cara untuk mengetahui jika dia menggertak) {/i}"
        m "Dapatkan aku minuman"
        scene cinejen16 with fade
        m "Thanks"
        m "Dapatkan minuman untuk Anda"
        m "Dan mari kita menonton TV"
        scene cinejen13 with dissolve
        b "Cheers"
        m "Tolong beri aku satu"
        b "Oh kamu sudah menyelesaikannya"
        m "Yes"
        scene cinejen34 with fade
        m "Cheers"
        b "Cheers"
        m "Stay here"
        b "Hah!"
        scene cinejen35 with dissolve
        m "{i} (i \ 'll sedikit menggodanya) {/i}"
        scene cinejen36 with dissolve
        m "Ayo Dance With Me"
        scene cinejen37 with dissolve
        "..."
        scene cinejen38 with dissolve
        m "Saya pikir itu cukup"
        scene cinejen39 with dissolve
        m "Hmmm"
        scene cinejen40 with dissolve
        m "Selamat malam"
        b "{i}(Damn){/i}"
        b "{i} (Saya perlu melakukan sesuatu) {/i}"
        menu:
            "Apakah Anda ingin minuman lain?":
                b "Yang terakhir saya janji"
                if mrel >=420 and mcorr>= 50:
                    m "Ok cepat"
                    m "Dapatkan saya tembakan"
                    scene cinejen42 with fade
                    "..."
                    menu:
                        "Saya perlu melakukan sesuatu sekarang":
                            m "Itu saja"
                            m "Selamat malam"
                            scene cinejen43 with dissolve
                            b "Wait"
                            m "Apa"
                            scene cinejen44 with dissolve
                            m "Apa yang sedang kamu lakukan"
                            "..."
                            m "Stewart"
                            b "Aku ingin menciummu"
                            scene cinejen45 with dissolve
                            m "Lalu lakukan"
                            scene cinejen46 with dissolve
                            "..."
                            scene cinejen47 with dissolve
                            "..."
                            menu:
                                "Bawa dia ke dinding" if mrel >=450:
                                    scene cinejen48 with dissolve
                                    "..."
                                    scene bmwall
                                    "..."
                                    m "Ahh Stewart"
                                    b "..."
                                    "..."
                                    menu:
                                        "Cum di dalam":
                                            scene cinejen49 with vpunch
                                            m "Ahhh!"
                                            scene cinejen51 with fade
                                            b "Selamat malam"
                                            scene cinejen52 with dissolve
                                            "..."
                                            pass
                                        "Keluar":
                                            scene cinejen50 with vpunch
                                            b "Ahhh"
                                            scene cinejen51 with fade
                                            b "Selamat malam"
                                            scene cinejen52 with dissolve
                                            "..."
                                            pass

                                "Bawa dia ke lantai" if mrel >=500:
                                    scene cinejen63 with fade
                                    "..."
                                    scene frgm
                                    "..."
                                    b "..."
                                    m "Eh!"
                                    b "..."
                                    m "Berikan padaku"
                                    scene cinejen64 with fade
                                    b "Argh"
                                    scene cinejen65 with dissolve
                                    "..."
                                    b "Saya cukup selesai"
                                    m "Wait"
                                    scene cinejen66
                                    "..."
                                    scene cinejen41 with fade
                                    "..."
                                    jump waitings
                                "Selamat malam":



                                    pass
                        "Tidak perlu":
                            m "Selamat malam"
                            pass
                else:

                    m "Tidak, saya ingin tidur"
                    pass
            "Melanjutkan":
                pass
        scene cinejen41 with fade
        "..."
        jump waitings
    else:

        scene cinejen8 with fade
        b "Dia masih di Rowena"
        b "Dia bilang dia akan kembali terlambat"
        m "Ok"
        m "Pergi sekarang, aku akan sampai jumpa nanti"
        scene cinejen12 with fade
        m "Selamat malam [bname]"
        m "Aku akan tidur sekarang"
        b "Selamat malam"
        "..."
        b "{i} (Saya pikir saya akan menunggu [sname]) {/i}"
        jump waitings






label waitings:
    scene cinejen26 with fade
    b "{i} (Let \ 's Watch TV sampai dia datang) {/i}"
    scene bwaits with dissolve
    s "Hey"
    b "Hai!"
    s "Apakah dia marah?"
    menu:
        "Aku menyelamatkanmu":
            scene bwaits1 with dissolve
            b "Tidak khawatir, saya telah melindungi Anda"
            if srel >=350:
                s "Terima kasih!!"
                scene bwaits3 with fade
                s "Di mana?"
                s "Apakah kamu membawaku ..."
                b "Anda akan melihat"
                scene bporn_shot_kiss4 with fade
                "..."
                scene bwaits4 with dissolve
                "..."
                scene bwaits5 with dissolve
                s "[bname] Saya mabuk"
                scene bwaits6 with hpunch
                b "Ya itu intinya"
                scene bwaits7 with fade
                $ persistent.unlock_39 = True
                "..."
                scene bwaits8 with dissolve
                "..."
                scene bwaits9 with dissolve
                s "..."
                scene bwaits10 with dissolve
                s "Ahhh"
                menu:
                    "Menyelesaikan":
                        scene bwaits11 with dissolve
                        b "Selamat malam"
                        jump newdays
                    "Selesaikan kasar":

                        scene bwaits12 with vpunch
                        s "Ahhh"
                        scene bwaits13 with fade
                        $ sdom += 1
                        show screen sdomup
                        b "Selamat malam"
                        hide screen sdomup
                        s "..."
                        jump newdays
            else:

                s "Terima kasih, saya akan tidur"
                s "Selamat malam"
                b "{i} (apa -apaan) {/i}"
                b "{i} (Saya kira sudah waktunya tidur) {/i}"
                "Naikkan poin hubungannya menjadi 350"
                jump newdays
        "Sedikit":

            s "Oh"
            s "Saya akan berbicara dengannya besok"
            s "Selamat malam"
            b "{i} (apa -apaan) {/i}"
            b "{i} (Saya kira sudah waktunya tidur) {/i}"
            jump newdays



label waitings1:
    scene cinejen26 with fade
    b "{i} (Let \ 's Watch TV sampai dia datang) {/i}"
    s "Hey"
    scene bwaitsa with dissolve
    b "Aha!"
    b "Anda di sini"
    s "Hmm"
    menu:
        "Aku menyelamatkanmu":
            s "Ya!"
            if srel >=350:
                s "Terima kasih!!"
                scene bwaitsa3 with fade
                s "Di mana?"
                s "Apakah kamu membawaku ..."
                b "Anda akan melihat"
                s "TIDAK!"
                scene bporn_shot_kiss4 with fade
                s "{i} (pada dasarnya saya mencium vaginanya sekarang) {/i}"
                scene bwaits4 with dissolve
                "..."
                scene bwaits5 with dissolve
                s "[bname] Saya mabuk"
                scene bwaits6 with hpunch
                b "Ya itu intinya"
                scene bwaits7 with fade
                $ persistent.unlock_39 = True
                "..."
                scene bwaits8 with dissolve
                "..."
                scene bwaits9 with dissolve
                s "..."
                scene bwaits10 with dissolve
                s "Ahhh"
                menu:
                    "Finish":
                        scene bwaits11 with dissolve
                        b "Selamat malam"
                        jump newdays
                    "Finish rough":

                        scene bwaits12 with vpunch
                        s "Ahhh"
                        scene bwaits13 with fade
                        $ sdom += 1
                        show screen sdomup
                        b "Selamat malam"
                        hide screen sdomup
                        s "..."
                        jump newdays
            else:

                s "Terima kasih, saya akan tidur"
                s "Selamat malam"
                b "{i} (apa -apaan) {/i}"
                b "{i} (Saya kira sudah waktunya tidur) {/i}"
                "Naikkan poin hubungannya menjadi 350"
                jump newdays
        "Selamat malam":

            s "Selamat malam"
            b "{i} (apa -apaan) {/i}"
            b "{i} (Saya kira sudah waktunya tidur) {/i}"
            jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
