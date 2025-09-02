label nudebeach_jenny:
    $ Hour += 1
    if mvisitnudebeach ==0:
        scene nbm with fade
        m "Itu tempat yang bagus"
        $ mvisitnudebeach = 1
        b "Uh huh"
        b "{i} (tunggu sampai Anda tahu apa itu) {/i}"
        m "Kenapa ..."
        scene nbm1 with dissolve
        m "... Mengapa semua orang telanjang?"
        b "Err It \'s Nude Beach"
        scene nbm2 with dissolve
        m "Apa?"
        b "Yes"
        m "Apa yang sedang kamu lakukan?"
        b "Melakukan apa yang dilakukan semua orang di pantai telanjang"
        m "Anda tidak melakukan apapun, mari kita pergi"
        b "Oh ayolah!"
        b "Anda bisa tetap dengan pakaian Anda"
        m "Saya tidak menyukainya, ayo pergi"
        b "Please"
        if mrel >=200:
            scene nbm3 with fade
            "Anda meluangkan waktu dan pergi"
            scene nbmreturn with fade
            "..."
            scene hall_d with fade
            b "{i} (...) {/i}"
            call screen gnav
        else:

            m "Saya mengatakan tidak [bname]"
            b "Apa pun!"
            "Naikkan poin hubungan Anda menjadi 200"
            scene hall_d with fade
            b "{i} (...) {/i}"
            call screen gnav
    else:


        scene nbm with fade
        m "..."
        $ mvisitnudebeach += 1
        scene nbm2 with dissolve
        m "Apa yang sedang kamu lakukan?"
        b "Melakukan apa yang dilakukan semua orang di pantai telanjang"
        m "Anda tidak melakukan apapun"
        b "Oh ayolah!"
        b "Anda bisa tetap dengan pakaian Anda"
        b "Please"
        if mrel >=200:
            scene nbm4 with fade
            "..."
            if mcorr >=20:
                scene nbm5 with dissolve
                "..."
                scene nbm6 with dissolve
                "..."
                scene nbm7 with dissolve
                "..."
                b "Uhhm"
                b "Apakah Anda ingin saya menaruh minyak untuk Anda?"
                if mrel >=300:
                    m "..."
                    m "Ok"
                    scene nbm12 with fade
                    m "Di punggungku saja"
                    scene nbm13 with dissolve
                    "..."
                    if mvisitnudebeach >=2:
                        b "Apakah Anda ingin saya melepaskan puncak?"
                        m "No"
                        m "Aku hanya akan melonggarkannya"
                        scene nbm14 with dissolve
                        "..."
                        scene nbm15 with fade
                        m "Terima kasih [bname]"
                        m "Let's go"
                        scene nbmreturn with fade
                        "..."
                        scene nbmreturn1 with dissolve
                        m "{i} (alangkah baiknya jika saya bisa tan yang topless) {/i}"
                        m "{i} (hanya jika pantai ini terpencil) {/i}"
                        m "{i} (tidak [mname] Lupakan saja) {/i}"
                        scene hall_d with fade
                        b "{i} (...) {/i}"
                        call screen gnav
                    else:

                        m "Tidak, terima kasih, itu cukup"
                        "..."
                        m "Saatnya pergi"
                        scene nbmreturn with fade
                        "..."
                        scene hall_d with fade
                        b "{i} (...) {/i}"
                        call screen gnav
                else:


                    m "No thanks"
                    "Naikkan hubungan Anda menjadi 300"
                    scene nbm4 with fade
                    "..."
                    m "Saya kira sudah waktunya untuk pergi"
                    scene nbmreturn with fade
                    "..."
                    scene hall_d with fade
                    b "{i} (...) {/i}"
                    call screen gnav

                scene nbmreturn with fade
                "..."
                scene hall_d with fade
                b "{i} (...) {/i}"
                call screen gnav
            else:

                scene nbm8 with dissolve
                "..."
                scene nbm9 with dissolve
                m "Saya berjalan -jalan"
                scene nbm10 with dissolve
                "..."
                scene nbm11 with dissolve
                m "Hah!"
                m "{i} (orang itu di sana!) {/i}"
                m "{i} (lebih baik saya duduk dengan [bname]) {/i}"
                scene nbm4 with fade
                "Anda meluangkan waktu dan pergi"
                scene nbmreturn with fade
                "..."
                scene hall_d with fade
                b "{i} (...) {/i}"
                call screen gnav
        else:

            m "Saya mengatakan tidak [bname]"
            m "Let's go"
            b "Apa pun!"
            "Naikkan poin hubungan Anda menjadi 200"
            scene hall_d with fade
            b "{i} (...) {/i}"
            call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc