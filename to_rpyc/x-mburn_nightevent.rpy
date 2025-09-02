label mburn_nightevent:
    scene etv_aw_b with fade
    b "Hah!"
    b "Hello"
    scene etv_aw2_b with dissolve
    m "Hi [bname]"
    b "Apa yang salah?"
    if day == 7:
        m "Tidak ada, hanya lelah"
        pass
    else:
        m "Tidak ada, hanya lelah karena pekerjaan"
        pass
    b "Ah begitu"
    b "Bisakah saya menonton TV?"
    m "Ya tentu, mari kita menonton sesuatu"
    scene etv_aw3_b with fade
    m "Pilih apa yang harus ditonton"
    m "Saya akan mendapatkan segelas anggur"
    menu:
        "Bisakah saya memilikinya juga?":
            if day ==7:
                $ drinkforbname = 1
                m "Only one"
                pass
            else:

                m "TIDAK!"
                b "..."
                pass
        "Jangan tanya":

            pass
    scene etv_aw4_b with fade
    "..."
    scene etv_aw5 with dissolve
    b "Hmmm"
    m "Maaf [bname] Saya tahu saya mengatakan tidak ada kaki di atas meja"
    m "Tapi kakiku sakit"
    b "It's ok"
    scene etv_aw4_b with dissolve
    b "Jika Anda mau, saya bisa memberi Anda gosok kaki"
    scene etv_aw6_b with dissolve
    if mrel >=70:
        scene etv_aw7_b with dissolve
        m "Itu akan sangat indah"
        scene etv_aw8_b with dissolve
        m "Mari kita lihat apa yang bisa Anda lakukan"
        scene etv_aw9_b with dissolve
        b "Bagaimana rasanya?"
        if mrel >=85:
            scene etv_aw10 with dissolve
            "..."
            scene etv_aw11 with dissolve
            "..."
            scene etv_aw10 with dissolve
            "..."
            scene etv_aw11 with dissolve
            m "Ahhh"
            scene etv_aw12_b with dissolve
            m "Yess"
            m "Tidak buruk"
            b "{i} (Sekarang waktunya, mengintip tidak ada sakit) {/i}"
            scene etv_aw13_b with dissolve
            b "{i}(No luck){/i}"
            scene etv_aw12_b with dissolve
            m "Ahhh"
            menu:
                "Sebutkan sengatan matahari":
                    b "Saya melihat Anda memiliki sinar matahari"
                    scene etv_aw15_b with dissolve
                    m "Jangan ingatkan saya tentang hal itu"
                    b "Jika Anda mau, saya bisa menerapkan lotion di punggung Anda"
                    if mrel >=100:
                        m "Hmm"
                        m "Saya akan mendapatkan lotion"
                        m "Dapatkan aku segelas anggur lagi"
                        if drinkforbname ==1:
                            b "Bisakah saya mendapatkan satu lagi juga?"
                            m "Tidak, cukup untukmu"
                            m "Anda sudah mabuk"
                            b "Tetapi..."
                            pass
                        else:
                            pass
                        scene etv_aw7_b with fade
                        m "Ini lotionnya"
                        m "Tahukah Anda bagaimana melakukannya?"
                        b "Sure"
                        scene etv_aw16_b with fade
                        m "..."
                        scene etv_aw17_b with dissolve
                        menu:
                            "Saya pikir lebih baik melonggarkan ini":
                                if drinkforbname ==1:
                                    scene etv_aw17_c with dissolve
                                    m "{i} (dia tidak tahu apa yang dia bicarakan) {/i}"
                                    m "{i} (Kurasa minuman itu terlalu banyak untuknya) {/i}"
                                    if elaine_convince ==4 and mrel >=150:
                                        m "Ya tidak apa -apa"
                                        m "Lakukan apa yang Anda inginkan"
                                        scene etv_aw17_r with dissolve
                                        m "..."
                                        m "Terima kasih [bname], sekarang Anda bisa kembali ke pijat kaki"
                                        m "Saya membutuhkan lebih dari itu"
                                        b "Saya senang bisa membantu"
                                        scene etv_aw18_r with fade
                                        m "Anda melakukan pekerjaan dengan baik"
                                        scene etv_aw18_cr with dissolve
                                        m "Ahhh"
                                        m "Yes"
                                        m "Don't stop"
                                        scene etv_aw10 with dissolve
                                        "..."
                                        scene etv_aw11 with dissolve
                                        "..."
                                        scene etv_aw10 with dissolve
                                        "..."
                                        scene etv_aw11 with dissolve
                                        "..."
                                        scene etv_aw18_r with dissolve
                                        m "Hmmm"
                                        scene etv_aw19_r with dissolve
                                        b "Huh, gelasnya !!"
                                        scene etv_aw20_r with dissolve
                                        b "{i}(WOW){/i}"
                                        scene etv_aw21_r with dissolve
                                        b "Hmmm"
                                        menu:
                                            "Semakin dekat":
                                                scene etv_aw20_cr with dissolve
                                                "..."
                                                menu:
                                                    "Pindahkan celana dalam":
                                                        scene etv_aw20_dr with dissolve
                                                        b "{i} (keren, sedikit lebih) {/i}"
                                                        s "[bname] Kamu dimana?"
                                                        b "{i} (keren, sedikit lebih) {/i}"
                                                        s "[bname] Kamu dimana?"
                                                        scene etv_aw20_er with hpunch
                                                        b "{i} (oh fuck!) {/i}"
                                                        b "{i} (run!) {/i}"
                                                        scene etv_aw20_f with dissolve
                                                        b "{i} (sialan aku lupa di mana kamarku) {/i}"
                                                        scene bporn with fade
                                                        b "Itu menakutkan"
                                                        b "{i} (hmm let \ 's lihat) {/i}"
                                                        b "{i} (apa yang harus dicari ...) {/i}"
                                                        menu:
                                                            "18+ remaja":
                                                                b "Mari kita lihat apa yang mereka miliki"
                                                                menu:
                                                                    "Hapus celana Anda":
                                                                        if scorr >= 30:
                                                                            jump s_watching
                                                                        else:
                                                                            scene bporn_s5 with dissolve
                                                                            s "Ohhh myyyy tuhan!"
                                                                            scene bporn_s6 with hpunch
                                                                            b "Hah!"
                                                                            b "Apa?"
                                                                            scene bporn_s7 with dissolve
                                                                            s "Serius [bname]!"
                                                                            b "Apa?"
                                                                            s "Tumbuh dewasa!"
                                                                            scene bporn_s8 with dissolve
                                                                            s "Dan lain kali Anda melihat saya, tolong tutupi mie kecil Anda"
                                                                            show screen scorr
                                                                            b "Apa -apaan"
                                                                            hide screen scorr
                                                                            $ scorr += 1
                                                                            scene bporn with fade
                                                                            b "{i} (sialan, aku tidak lagi dalam mood) {/i}"
                                                                            b "{i} (i \ 'll pergi tidur) {/i}"
                                                                            scene broom_night with fade
                                                                            "Naikkan korupsi Anda menjadi 30 untuk melihat adegan yang berbeda"
                                                                            jump newdays
                                                                    "Melanjutkan":

                                                                        pass
                                                                s "Apa yang Anda cari?"
                                                                scene bporn_s with hpunch
                                                                b "Hah!"
                                                                b "Nothing"
                                                                scene bporn_s1 with dissolve
                                                                s "Ayo! Tunjukkan padaku!"
                                                                menu:
                                                                    "Tunjukkan padanya":
                                                                        scene bporn_s2 with dissolve
                                                                        "..."
                                                                        scene bporn_s1 with dissolve
                                                                        "..."
                                                                        scene bporn_s3 with dissolve
                                                                        "..."
                                                                        scene bporn_s4 with dissolve
                                                                        s "Dengan serius!"
                                                                        s "Saya katakan lebih baik Anda mendapatkan pacar sejati"
                                                                        s "Sungguh pecundang"
                                                                        scene bporn with fade
                                                                        b "{i} (bagus yang dia tinggalkan) {/i}"
                                                                        b "{i} (sialan, aku tidak lagi dalam mood) {/i}"
                                                                        b "{i} (i \ 'll pergi tidur) {/i}"
                                                                        scene broom_night with fade
                                                                        "..."
                                                                        jump newdays
                                                                    "Menendang dia keluar":

                                                                        b "Tolong tinggalkan saja"
                                                                        scene bporn_s3 with dissolve
                                                                        s "Hmmm"
                                                                        scene bporn with fade
                                                                        b "{i} (bagus yang dia tinggalkan) {/i}"
                                                                        b "{i} (sialan, aku tidak lagi dalam mood) {/i}"
                                                                        b "{i} (i \ 'll pergi tidur) {/i}"
                                                                        scene broom_night with fade
                                                                        "..."
                                                                        jump newdays
                                                    "Jangan":

                                                        b "{i} (i \ 'D lebih baik tidak) {/i}"
                                                        pass
                                            "Lanjutkan dan gosok satu":


                                                scene etv_aw22_br with dissolve
                                                "..."
                                                scene etv_aw23_br with dissolve
                                                b "Hmmm"
                                                b "{i} (ini berbahaya) {/i}"
                                                b "{i} (tapi saya tidak peduli) {/i}"
                                                scene etv_aw26_br with hpunch
                                                b "Huh"
                                                b "{i} (dia bangun) {/i}"
                                                scene etv_aw23_br with dissolve
                                                b "Apakah Anda ingin gelas lain?"
                                                m "Yes"
                                                scene etv_aw27_br with dissolve
                                                "..."
                                                scene etv_aw28_br with dissolve
                                                jump mbun_extended




                                        scene etv_aw22_br with dissolve
                                        "..."
                                        scene etv_aw23_br with dissolve
                                        b "Hmmm"
                                        b "{i} (ini berbahaya) {/i}"
                                        s "[bname] Kamu dimana?"
                                        scene etv_aw21_r with hpunch
                                        b "{i} (oh fuck, aku akan pergi ke kamarku) {/i}"
                                        scene broom_night with fade
                                        b "{i} (lebih baik saya pergi tidur) {/i}"
                                        jump newdays
                                    else:




                                        pass
                                    m "Hanya sedikit"
                                    scene etv_aw17_b with dissolve
                                    b "Ok"
                                    scene etv_aw17_d with dissolve
                                    b "{i} (sekarang adalah waktunya) {/i}"
                                    pass
                                else:


                                    m "TIDAK!!"
                                    m "Err .. Maksudku"
                                    pass
                            "Tidak mengatakan apa -apa":

                                pass
                        m "Terima kasih [bname], sekarang Anda bisa kembali ke pijat kaki"
                        m "Saya membutuhkan lebih dari itu"
                        b "Saya senang bisa membantu"
                        scene etv_aw18_b with fade
                        m "Anda melakukan pekerjaan dengan baik"
                        scene etv_aw18_c with dissolve
                        m "Ahhh"
                        m "Yes"
                        m "Don't stop"
                        scene etv_aw10 with dissolve
                        "..."
                        scene etv_aw11 with dissolve
                        "..."
                        scene etv_aw10 with dissolve
                        "..."
                        scene etv_aw11 with dissolve
                        "..."
                        scene etv_aw18_b with dissolve
                        m "Hmmm"
                        scene etv_aw19_b with dissolve
                        b "Huh, gelasnya !!"
                        scene etv_aw20_b with dissolve
                        b "{i}(WOW){/i}"
                        scene etv_aw21_b with dissolve
                        b "Hmmm"
                        menu:
                            "Semakin dekat":
                                scene etv_aw20_b with dissolve
                                b "Hmm"
                                scene etv_aw20_c with dissolve
                                "..."
                                menu:
                                    "Pindahkan celana dalam":
                                        scene etv_aw20_d with dissolve
                                        b "{i} (keren, sedikit lebih) {/i}"
                                        s "[bname] Kamu dimana?"
                                        scene etv_aw20_e with hpunch
                                        b "{i} (oh fuck!) {/i}"
                                        b "{i} (run!) {/i}"
                                        scene etv_aw20_f with dissolve
                                        b "{i} (sialan aku lupa di mana kamarku) {/i}"
                                        scene bporn with fade
                                        b "Scary"
                                        b "{i} (hmm let \ 's lihat) {/i}"
                                        b "{i} (apa yang harus dicari ...) {/i}"
                                        menu:
                                            "18+ remaja":
                                                b "Mari kita lihat apa yang mereka miliki"
                                                menu:
                                                    "Hapus celana Anda":
                                                        if scorr >= 30:
                                                            jump s_watching
                                                        else:
                                                            scene bporn_s5 with dissolve
                                                            s "Ohhh myyyy tuhan!"
                                                            scene bporn_s6 with hpunch
                                                            b "Hah!"
                                                            b "Apa?"
                                                            scene bporn_s7 with dissolve
                                                            s "Serius [bname]!"
                                                            b "Apa?"
                                                            s "Tumbuh dewasa!"
                                                            scene bporn_s8 with dissolve
                                                            s "Dan lain kali Anda melihat saya, tolong tutupi mie kecil Anda"
                                                            show screen scorr
                                                            b "Apa -apaan"
                                                            hide screen scorr
                                                            $ scorr += 1
                                                            scene bporn with fade
                                                            b "{i} (sialan, aku tidak lagi dalam mood) {/i}"
                                                            b "{i} (i \ 'll pergi tidur) {/i}"
                                                            scene broom_night with fade
                                                            "Naikkan korupsi Anda menjadi 30 untuk melihat adegan yang berbeda"
                                                            jump newdays
                                                    "Melanjutkan":

                                                        pass
                                                s "Apa yang Anda cari?"
                                                scene bporn_s with hpunch
                                                b "Hah!"
                                                b "Nothing"
                                                scene bporn_s1 with dissolve
                                                s "Ayo! Tunjukkan padaku!"
                                                menu:
                                                    "Tunjukkan padanya":
                                                        scene bporn_s2 with dissolve
                                                        "..."
                                                        scene bporn_s1 with dissolve
                                                        "..."
                                                        scene bporn_s3 with dissolve
                                                        "..."
                                                        scene bporn_s4 with dissolve
                                                        s "Dengan serius!"
                                                        s "Saya katakan lebih baik Anda mendapatkan pacar sejati"
                                                        s "Sungguh pecundang"
                                                        scene bporn with fade
                                                        b "{i} (bagus yang dia tinggalkan) {/i}"
                                                        b "{i} (sialan, aku tidak lagi dalam mood) {/i}"
                                                        b "{i} (i \ 'll pergi tidur) {/i}"
                                                        scene broom_night with fade
                                                        "..."
                                                        jump newdays
                                                    "Menendang dia keluar":

                                                        b "Tolong tinggalkan saja"
                                                        scene bporn_s3 with dissolve
                                                        s "Hmmm"
                                                        scene bporn with fade
                                                        b "{i} (bagus yang dia tinggalkan) {/i}"
                                                        b "{i} (sialan, aku tidak lagi dalam mood) {/i}"
                                                        b "{i} (i \ 'll pergi tidur) {/i}"
                                                        scene broom_night with fade
                                                        "..."
                                                        jump newdays
                                    "Jangan":

                                        b "{i} (i \ 'D lebih baik tidak) {/i}"
                                        pass
                            "Lanjutkan dan gosok satu":
                                pass
                        scene etv_aw22_b with dissolve
                        "..."
                        scene etv_aw23_b with dissolve
                        b "Hmmm"
                        b "{i} (ini berbahaya) {/i}"
                        scene etv_aw21_b with dissolve
                        b "{i} (lebih baik saya melanjutkan ke toilet atau kamar saya) {/i}"
                        if srel >=80:
                            scene bporn with fade
                            b "{i} (hmm let \ 's lihat) {/i}"
                            b "{i} (apa yang harus dicari ...) {/i}"
                            menu:
                                "18+ remaja":
                                    b "Mari kita lihat apa yang mereka miliki"
                                    s "Apa yang Anda cari?"
                                    scene bporn_s with hpunch
                                    b "Hah!"
                                    b "Nothing"
                                    scene bporn_s1 with dissolve
                                    s "Ayo! Tunjukkan padaku!"
                                    menu:
                                        "Tunjukkan padanya":
                                            scene bporn_s2 with dissolve
                                            "..."
                                            scene bporn_s1 with dissolve
                                            "..."
                                            scene bporn_s3 with dissolve
                                            "..."
                                            scene bporn_s4 with dissolve
                                            s "Dengan serius!"
                                            s "Saya katakan lebih baik Anda mendapatkan pacar sejati"
                                            s "Sungguh pecundang"
                                            scene bporn with fade
                                            b "{i} (bagus yang dia tinggalkan) {/i}"
                                            b "{i} (sialan, aku tidak lagi dalam mood) {/i}"
                                            b "{i} (i \ 'll pergi tidur) {/i}"
                                            scene broom_night with fade
                                            "Itu semua di sini"
                                            jump newdays
                                        "Menendang dia keluar":

                                            b "Tolong tinggalkan saja"
                                            scene bporn_s3 with dissolve
                                            s "Hmmm"
                                            scene bporn with fade
                                            b "{i} (bagus yang dia tinggalkan) {/i}"
                                            b "{i} (sialan, aku tidak lagi dalam mood) {/i}"
                                            b "{i} (i \ 'll pergi tidur) {/i}"
                                            scene broom_night with fade
                                            "..."
                                            jump newdays
                                "Milfs":

                                    b "Mari kita lihat apa yang mereka miliki"
                                    s "Apa yang Anda cari?"
                                    scene bporn_s with hpunch
                                    b "Hah!"
                                    b "Nothing"
                                    scene bporn_s1 with dissolve
                                    s "Ayo! Tunjukkan padaku!"
                                    menu:
                                        "Tunjukkan padanya":
                                            scene bporn_s2milf with dissolve
                                            "..."
                                            scene bporn_s1 with dissolve
                                            "..."
                                            scene bporn_s3 with dissolve
                                            "..."
                                            scene bporn_s4 with dissolve
                                            s "Dengan serius!"
                                            s "Saya katakan lebih baik Anda mendapatkan pacar sejati"
                                            s "Dan dari usia Anda!"
                                            s "Sungguh pecundang"
                                            scene bporn with fade
                                            b "{i} (bagus yang dia tinggalkan) {/i}"
                                            b "{i} (sialan, aku tidak lagi dalam mood) {/i}"
                                            b "{i} (i \ 'll pergi tidur) {/i}"
                                            scene broom_night with fade
                                            "Itu semua di sini"
                                            jump newdays
                                        "Menendang dia keluar":

                                            b "Tolong tinggalkan saja"
                                            scene bporn_s3 with dissolve
                                            s "Hmmm"
                                            scene bporn with fade
                                            b "{i} (bagus yang dia tinggalkan) {/i}"
                                            b "{i} (sialan, aku tidak lagi dalam mood) {/i}"
                                            b "{i} (i \ 'll pergi tidur) {/i}"
                                            scene broom_night with fade
                                            "..."
                                            jump newdays
                        else:

                            scene broom_night with fade
                            b "{i} (lebih baik saya pergi tidur) {/i}"
                            "Naikkan [sname] poin Anda menjadi 80"
                            jump newdays
                    else:
                        m "Hmm"
                        m "Tidak, saya kira saya akan tidur"
                        m "Saya lelah"
                        scene hall_m_n16_b with fade
                        m "Terima kasih dan selamat malam sayang"
                        b "Selamat malam"
                        scene etv_aw14 with dissolve
                        b "{i} (...) {/i}"
                        scene hall_n with fade
                        b "{i} (i \ 'D lebih baik tidur) {/i}"
                        jump newdays
                "Tidak mengatakan apa -apa":

                    scene etv_aw9_b with dissolve
                    m "Itu bagus [bname]"
                    m "Saya pikir itu cukup untuk hari ini"
                    scene hall_m_n16_b with fade
                    m "Selamat malam sayang"
                    b "Selamat malam"
                    scene etv_aw14 with dissolve
                    b "{i} (...) {/i}"
                    scene hall_n with fade
                    b "{i} (i \ 'D lebih baik tidur) {/i}"
                    scene black
                    "Itu semua di sini"
                    jump newdays
        else:


            m "Tidak buruk, tapi itu cukup untuk hari ini"
            b "Ok"
            scene hall_m_n16_b with fade
            m "Selamat malam!"
            m "Pergi ke kamar Anda!"
            scene hall_n with fade
            b "{i} (sialan!) {/i}"
            b "{i} (Saya harus mengerjakan poin hubungan saya, 85) {/i}"
            b "{i} (kurasa aku akan tidur juga) {/i}"
            jump newdays
    else:

        scene etv_aw_no_b with dissolve
        m "Terima kasih, saya baik -baik saja"
        scene etv_aw4_b with fade
        "Anda terus menonton"
        scene hall_m_n16_b with fade
        m "Selamat malam!"
        m "Pergi ke kamar Anda!"
        scene hall_n with fade
        b "{i} (sialan!) {/i}"
        b "{i} (Saya harus mengerjakan poin hubungan saya, 70) {/i}"
        b "{i} (kurasa aku akan tidur juga) {/i}"
        jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc