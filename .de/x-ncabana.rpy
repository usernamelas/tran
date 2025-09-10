image nbcabanabrb:
    "nbrb00.jpg"
    pause 0.01
    "nbrb01.jpg"
    pause 0.01
    "nbrb02.jpg"
    pause 0.01
    "nbrb03.jpg"
    pause 0.01
    "nbrb04.jpg"
    pause 0.01
    "nbrb05.jpg"
    pause 0.01
    "nbrb06.jpg"
    pause 0.01
    "nbrb07.jpg"
    pause 0.01
    "nbrb08.jpg"
    pause 0.01
    "nbrb09.jpg"
    pause 0.01
    "nbrb10.jpg"
    pause 0.01
    "nbrb11.jpg"
    pause 0.01
    "nbrb12.jpg"
    pause 0.01
    "nbrb13.jpg"
    pause 0.01
    "nbrb14.jpg"
    pause 0.01
    "nbrb15.jpg"
    pause 0.01
    "nbrb16.jpg"
    pause 0.01
    "nbrb17.jpg"
    pause 0.01
    "nbrb18.jpg"
    pause 0.01
    "nbrb19.jpg"
    pause 0.01
    "nbrb20.jpg"
    pause 0.01
    "nbrb21.jpg"
    pause 0.01
    "nbrb22.jpg"
    pause 0.01
    "nbrb23.jpg"
    pause 0.01
    "nbrb24.jpg"
    pause 0.01
    "nbrb25.jpg"
    pause 0.01
    "nbrb26.jpg"
    pause 0.01
    "nbrb27.jpg"
    pause 0.01
    "nbrb28.jpg"
    pause 0.01
    "nbrb29.jpg"
    pause 0.01
    "nbrb30.jpg"
    pause 0.01
    "nbrb31.jpg"
    pause 0.01
    "nbrb32.jpg"
    pause 0.01
    "nbrb33.jpg"
    pause 0.01
    "nbrb34.jpg"
    pause 0.01
    "nbrb35.jpg"
    pause 0.01
    "nbrb36.jpg"
    pause 0.01
    "nbrb37.jpg"
    pause 0.01
    "nbrb38.jpg"
    pause 0.01
    "nbrb39.jpg"
    pause 0.01
    "nbrb40.jpg"
    pause 0.01
    "nbrb41.jpg"
    pause 0.01
    "nbrb42.jpg"
    pause 0.01
    "nbrb43.jpg"
    pause 0.01
    "nbrb44.jpg"
    pause 0.01
    "nbrb45.jpg"
    pause 0.01
    "nbrb46.jpg"
    pause 0.01
    "nbrb47.jpg"
    pause 0.01
    "nbrb48.jpg"
    pause 0.01
    "nbrb49.jpg"
    pause 0.01
    "nbrb50.jpg"
    pause 0.01
    "nbrb51.jpg"
    pause 0.01
    "nbrb52.jpg"
    pause 0.01
    "nbrb53.jpg"
    pause 0.01
    repeat


label ncabana:
    scene nbcabana_r_s with fade
    b "Mari kita menikmati waktu kita"
    b "Ini semua milik kita"
    s "Bagaimana Anda tahu tentang tempat ini [bname]"
    b "Aku tahu..."
    b "Apakah Anda mendapatkan ikan?"
    rb "Yes"
    b "Ayo lakukan"
    scene nbcabana_r_s1 with fade
    s "Dengan serius!"
    scene nbcabana_r_s2 with dissolve
    b "Apa yang salah?"
    s "Tolong berdandan"
    b "Ayo di pantai telanjang"
    s "Jadi apa? Anda tidak memasak setidaknya telanjang"
    rb "Ayo, Anda juga harus lepas landas"
    a "..."
    scene nbcabana_r_s3 with dissolve
    a "Mari kita lakukan [sname] \ 'baik -baik saja"
    s "..."
    scene nbcabana_r_s4 with fade
    rb "Let's eat"
    b "Yeah"
    scene nbcabana_r_s5 with fade
    b "Jadi apa yang kita lakukan sekarang?"
    a "Mari kita mendapatkan tan"
    rb "Ide bagus"
    scene nbr10 with fade
    a "Itu cukup saya kira"
    scene nbr11 with dissolve
    a "Hmm"
    a "Aku akan berbaring di tempat tidur di sana, sampai jumpa nanti"
    s "Ok"
    scene nbcabana_r_s6 with fade
    "..."
    scene nbcabana_r_s7 with dissolve
    s "Jadi apa yang Anda lakukan untuk hidup?"
    rb "Dengan baik..."
    b "{i}(Hmm){/i}"
    b "{i} (mungkin saya bisa mengikuti rowena!) {/i}"
    menu:
        "Ikuti dia":
            jump rowenaalonecabana
        "Tetap di sini":

            b "..."
            b "[sname]!"
            s "Ya?"
            b "Apakah Anda ingin berenang?"
            scene nbcabana_r_s18 with dissolve
            s "..."
            s "Ya ayo pergi"
            scene nbcabana_r_s19 with fade
            b "Hey [sname]"
            s "Apa?"
            b "Mari kita menggoda pria bodoh ini"
            s "Apa maksudmu?"
            b "Mari kita keluar di depannya"
            if scorr >= 30:
                s "Hmm, ya hahaha"
                scene nbcabana_r_s20 with dissolve
                rb "..."
                scene nbcabana_r_s21 with dissolve
                s "Huh [bname]!"
                s "Tolong hentikan"
                b "Diam!"
                b "Larry!"
                b "Bergabunglah dengan kami jika Anda suka"
                if sdom >=100:
                    scene nbcabana_r_s22 with dissolve
                    s "Tetapi..."
                    b "Saya bilang tutup mulut"
                    b "Ayo Larry"
                    scene nbcabana_r_s24 with fade
                    "..."
                    scene nbcabana_r_s25 with dissolve
                    "..."
                    scene nbcabanabrb
                    $ persistent.unlock_34 = True
                    s "Ahh"
                    "..."
                    s "Grrr"
                    "..."
                    scene nbcabana_r_s26 with hpunch
                    b "Ahhh"
                    scene nbcabana_r_s27 with fade
                    b "Cuci wajah Anda"
                    scene nbcabana_r_s28 with dissolve
                    "..."
                    "Rowena kembali, Anda meluangkan waktu dan pulang"
                    scene hall_d with fade
                    b "{i} (...) {/i}"
                    call screen gnav
                else:



                    scene nbcabana_r_s23 with dissolve
                    s "Hai! Hentikan"
                    s "Apa pendapat Anda tentang saya!"
                    "Naikkan dominasi Anda menjadi 100"
                    s "I'm leaving"
                    b "Wait wait"
                    scene nbr_return1 with fade
                    "Rowena kembali, Anda meluangkan waktu dan pulang"
                    scene hall_d with fade
                    b "{i} (sialan aku mengacaukannya) {/i}"
                    call screen gnav
            else:

                "Naikkan korupsi Anda menjadi 30"
                s "Tidak, saya tidak menyukainya"
                scene nbr_return1 with fade
                "Rowena kembali, Anda meluangkan waktu dan pulang"
                scene hall_d with fade
                b "{i} (...) {/i}"
                call screen gnav


label rowenaalonecabana:
    scene ralonecab with fade
    a "Hah!"
    b "Hmm bagus"
    scene ralonecab1 with hpunch
    a "Ah [bname]"
    scene ralonecab2 with dissolve
    a "..."
    scene ralonecab3 with dissolve
    a "Ahhh"
    if srel >=300:
        scene black
        "SEMENTARA ITU"
        scene nbcabana_r_s7a with fade
        s "{i} (Saya bertanya -tanya ke mana [bname] pergi ke) {/i}"
        s "{i} (saya akan pergi melihat apa yang dia lakukan) {/i}"
        scene nbcabana_r_s8 with fade
        s "{i}(Huh){/i}"
        menu:
            "Dia akan pergi bercinta pacar Rowena untuk mendapatkan genap":
                s "{i} (kami \ 'll lihat bajingan) {/i}"
                scene nbcabana_r_s10 with fade
                s "{i} (ini dia) {/i}"
                scene nbcabana_r_s11 with dissolve
                rb "Huh"
                rb "[sname]"
                s "Mudah, kami sendirian"
                rb "Apa!"
                s "[bname] Apakah sialan Rowena, apakah Anda ingin mendapatkan genap?"
                rb "Hell yeah"
                scene nbcabana_r_s12 with dissolve
                "..."
                scene nbcabana_r_s13 with dissolve
                s "Follow me"
                scene nbcabana_r_s14 with fade
                s "Ayo lakukan di sini"
                scene nbcabana_r_s15 with dissolve
                s "Ah"
                scene nbcabana_r_s16 with dissolve
                b "Hah!"
                b "Ayo Rowena biarkan menunggu mereka di sana"
                scene nbcabana_r_s17 with fade
                "..."
                scene nbr_return1 with fade
                b "Akhirnya Anda kembali, saya harap Anda menikmati"
                s "..."
                scene hall_d with fade
                b "{i} (sialan ...) {/i}"
                call screen gnav
            "Dia akan menamparnya":

                scene nbcabana_r_s9 with hpunch
                b "Aduh!"
                $ srel -= 5
                show screen sreldw
                s "Aku pulang"
                hide screen sreldw
                s "Asshole"
                scene hall_d with fade
                b "{i} (sialan itu kesalahan besar) {/i}"
                call screen gnav
    else:

        scene ralonecab4 with dissolve
        "..."
        menu:
            "Air mani":
                b "Uhhhh!"
                scene ralonecab5 with fade
                b "Let 's Go Dear"
                scene nbr_return1 with fade
                s "Akhirnya Anda kembali"
                s "Kemana saja kamu?"
                b "Toilet"
                s "Hmm"
                scene hall_d with fade
                b "{i} (...) {/i}"
                call screen gnav
            "Cum di mulutnya":


                scene ralonecab6 with fade
                b "{i} (kenapa dia terlihat marah) {/i}"
                b "{i} (apakah saya merasakan seburuk ini) {/i}"
                scene ralonecab5 with fade
                b "Let's go"
                scene nbr_return1 with fade
                s "Akhirnya Anda kembali"
                s "Kemana saja kamu?"
                b "Toilet"
                s "Hmm"
                scene hall_d with fade
                b "{i} (...) {/i}"
                call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
