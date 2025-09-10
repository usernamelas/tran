label eveningtv_afterwork:
    if mburnt == 1:
        $ mburnt = 0
        jump mburn_nightevent
    else:
        pass
    scene etv_aw with fade
    b "Hah!"
    scene etv_aw1 with dissolve
    b "Hello"
    scene etv_aw2 with dissolve
    m "Hi [bname]"
    b "Apa yang salah?"
    if day == 7:
        m "Tidak ada, hanya lelah"
        pass
    elif startnework ==1 and day ==2:
        m "Tidak ada, hanya lelah"
        jump eveningtv_elaine

    elif startnework ==1 and day ==5 and elaineshowsup ==0 and etvelaine ==1:
        m "Tidak ada, hanya lelah"
        jump elainefirstcoming

    elif elaineagain == 1 and day ==5:
        jump elainesecondcoming

    elif mbtv == 1 and day ==3:
        b "Dimana Adam?"
        m "Mencuci tangannya"
        m "Silakan selesaikan studi Anda!"
        b "Hmm"
        b "Ok"
        jump mbtvnight

    elif gnight >=2 and day ==4:
        jump eveningtv_elaine

    elif melsw >=9 and day ==5:
        jump eveningtv_elaine
    else:

        m "Tidak ada, hanya lelah karena pekerjaan"
        pass

    b "Ah begitu"
    b "Bisakah saya menonton TV?"
    m "Ya tentu, mari kita menonton sesuatu"
    scene etv_aw3 with fade
    m "Pilih apa yang harus ditonton"
    m "Saya akan mendapatkan segelas anggur"
    menu:
        "Bisakah saya memilikinya juga?":
            if day !=7:
                m "No"
                pass
            else:
                $ drinkforbname = 1
                m "Only one"
                pass


    scene etv_aw4 with fade
    "..."
    scene etv_aw5 with dissolve
    b "Hmmm"
    m "Maaf [bname] Saya tahu saya mengatakan tidak ada kaki di atas meja"
    m "Tapi kakiku sakit"
    b "It's ok"
    menu:
        "Tonton TV":
            scene hall_m_n12 with dissolve
            b "Saya tidak suka blues"
            m "Just watch"
            if pornchanel == 1:
                scene hall_m_n17 with dissolve
                m "Saya tidak mencoba saluran baru"
                m "Dan saluran yang memalukan itu sudah berubah"
                b "Ya..."
                b "Apa yang Anda ubah?"
                m "Movies"
                b "Bisakah kita menontonnya"
                scene hall_m_n12 with dissolve
                m "Ya, mari kita lihat apa yang mereka miliki"
                scene hall_m_n37 with dissolve
                m "Hah!"
                b "Err"
                scene hall_m_n15 with dissolve
                m "Siapa yang mengembalikan saluran ini?"
                b "Aku tidak tahu"
                b "Tapi mengapa mereka melakukan ini?"
                m "Errrm"
                scene hall_m_n38 with dissolve
                if elaine_convince == 4:
                    m "{i} (baik jika dia naif seperti yang dikatakan Elaine, saya bisa menggunakannya untuk melakukan beberapa latihan) {/i}"
                    jump jenpractice
                else:
                    m "{i} (apakah dia naif atau hanya membodohi saya) {/i}"
                    pass
                m "Anda tahu apa, mari kita melihat beberapa film dokumenter"
                m "Anda tidak menyukai ini?"
                b "Ya kenapa tidak"
                scene hall_m_n19 with dissolve
                b "Ya ini lebih baik"
                m "Ok"
                scene black
                "..."
                scene hall_m_n12 with fade
                b "Tidak buruk kan?"
                m "Yeah"
                m "Selamat malam"
                scene hall_m_n16 with fade
                m "Selamat malam!"
                scene hall_n with fade
                b "{i} (Saya kira saya akan tidur juga) {/i}"
                jump newdays
            else:

                pass
            scene hall_m_n11 with dissolve
            "..."
            scene hall_m_n10 with fade
            m "Itu bagus"
            b "Ya, membosankan"
            if elaine_convince == 4:
                jump jenpractice
            else:
                pass
            scene hall_m_n16 with fade
            m "Selamat malam!"
            scene hall_n with fade
            b "{i} (Saya kira saya akan tidur juga) {/i}"
            jump newdays
        "Tawarkan gosok":

            pass

    scene etv_aw4 with dissolve
    b "Jika Anda mau, saya bisa memberi Anda gosok kaki"
    scene etv_aw6 with dissolve
    if mrel >=30:
        scene etv_aw7 with dissolve
        m "Itu akan sangat indah"
        scene etv_aw8 with dissolve
        m "Mari kita lihat apa yang bisa Anda lakukan"
        scene etv_aw9 with dissolve
        b "Bagaimana rasanya?"
        if mrel >=100:
            scene etv_aw10 with dissolve
            "..."
            scene etv_aw11 with dissolve
            "..."
            scene etv_aw10 with dissolve
            "..."
            scene etv_aw11 with dissolve
            m "Ahhh"
            menu:
                "Apakah Anda ingin saya menggunakan krim kaki?":
                    scene etv_aw12 with dissolve
                    m "No dear"
                    m "Mungkin gosok punggung, setelah ini"
                    m "Tolong lanjutkan saja"
                    b "{i} (Sekarang waktunya, mengintip tidak ada sakit) {/i}"
                    scene etv_aw13 with dissolve
                    b "{i}(No luck){/i}"
                    scene etv_aw12 with dissolve
                    m "Ahhh"
                    scene etv_aw12pov with dissolve
                    m "{i} (tangannya sangat kuat, seperti Stewart) {/i}"
                    scene etv_aw9 with dissolve
                    m "Itu bagus [bname]"
                    if mrel >=110:
                        m "Biarkan saya mendapatkan segelas anggur lagi"
                        m "Tetap di tempat kami berhenti"
                        scene etv_aw20 with fade
                        m "Let's continue"
                        scene etv_aw21 with dissolve
                        m "Ohh ya!"
                        m "Itu luar biasa"
                        b "Huh, gelasnya !!"
                        scene etv_aw22 with dissolve
                        b "{i} (bercinta kaca, mari kita mengintip di sini) {/i}"
                        menu:
                            "Mengintip":
                                scene etv_aw23 with dissolve
                                b "{i}(Slowly [bname]){/i}"
                                scene etv_aw24 with dissolve
                                m "Oh [bname] jangan berhenti"
                                scene etv_aw24 with hpunch
                                b "{i}(Fuck){/i}"
                                scene etv_aw22 with dissolve
                                b "{i}(One rub){/i}"
                                scene etv_aw25 with dissolve
                                b "{i}(One move){/i}"
                                scene etv_aw26 with dissolve
                                b "{i}(Yeah){/i}"
                                b "{i} (ini sepertinya belum digunakan untuk sementara) {/i}"
                                b "{i} (hang on dec, bagaimana bisa dicukur) {/i}"
                                b "{i} (Saya pikir dia melihat seseorang?) {/i}"
                                b "{i} (Saya perlu menyentuh ini, saya tidak akan bercinta sekarang) {/i}"
                                s "[bname] Kamu dimana?"
                                scene etv_aw27 with hpunch
                                b "Oh fuck!"
                                if elaine_convince == 4:
                                    menu:
                                        "Perbaiki hal -hal dan shoo dia pergi":
                                            scene etv_ss with fade
                                            s "Apa yang sedang kamu lakukan?"
                                            b "Tidak ada, [mname] tertidur"
                                            b "Dan saya sedang menonton TV"
                                            b "Janganlah membangunkannya"
                                            b "Just go"
                                            scene etv_ss1 with fade
                                            b "{i} (keren dia pergi) {/i}"
                                            scene etv_ss2 with fade
                                            m "Apa yang telah terjadi?"
                                            b "Tidak ada, Anda tertidur selama beberapa waktu"
                                            jump jenpractice
                                        "Berlari":

                                            pass
                                else:

                                    pass
                                b "{i} (run!) {/i}"
                                scene etv_aw20_f with dissolve
                                b "{i} (sialan aku lupa di mana kamarku) {/i}"
                                scene bporn with fade
                                b "Scary"
                                b "{i} (Saya perlu menggosoknya) {/i}"
                                b "{i} (hmm let \ 's lihat) {/i}"
                                menu:
                                    "Hapus celana Anda":
                                        if scorr >= 30:
                                            jump s_watching_m
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
                                    "Jangan":
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



                                m "Itu cukup sayang"
                                b "Ok"
                                if elaine_convince == 4:
                                    jump jenpractice
                                else:
                                    pass
                                scene etv_aw17 with fade
                                m "Terima kasih"
                                if drinkforbname == 1:
                                    menu:
                                        "Lakukan sesuatu, Anda benar -benar mabuk?":
                                            scene etv_aw17a with dissolve
                                            m "..."
                                            m "[bname] Saya harus pergi"
                                            b "..."
                                            pass
                                        "TIDAK":
                                            pass
                                else:
                                    pass
                                scene hall_m_n16 with fade
                                m "Selamat malam sayang"
                                b "Selamat malam"
                                scene etv_aw14 with dissolve
                                b "{i} (...) {/i}"
                                scene hall_n with fade
                                b "{i} (i \ 'D lebih baik tidur) {/i}"
                                jump newdays
                    else:



                        pass
                    m "Biarkan saya mendapatkan segelas anggur lagi dan Anda memberi saya gosok punggung"
                    scene etv_aw15 with fade
                    m "Anda baik -baik saja"
                    menu:
                        "Mengintip":
                            scene etv_aw16 with dissolve
                            "..."
                            m "{i} (kenapa dia berhenti?) {/i}"
                            m "{i} (mungkin lelah) {/i}"
                            m "Itu cukup sayang"
                            b "Ok"
                            if elaine_convince == 4:
                                jump jenpractice
                            else:
                                pass
                            scene etv_aw17 with fade
                            m "Terima kasih"
                            "Dapatkan poin Anda ke lebih tinggi dari 110 untuk melihat adegan yang berbeda"
                            pass
                        "Jangan":

                            m "Itu cukup sayang"
                            b "Ok"
                            if elaine_convince == 4:
                                jump jenpractice
                            else:
                                pass
                            scene etv_aw17 with fade
                            m "Terima kasih"
                            pass

                    scene hall_m_n16 with fade
                    m "Selamat malam sayang"
                    b "Selamat malam"
                    scene etv_aw14 with dissolve
                    b "{i} (...) {/i}"
                    scene hall_n with fade
                    b "{i} (i \ 'D lebih baik tidur) {/i}"
                    jump newdays
                "Tidak mengatakan apa -apa":

                    scene etv_aw12 with dissolve
                    m "Yess"
                    m "Tidak buruk"
                    b "{i} (Sekarang waktunya, mengintip tidak ada sakit) {/i}"
                    scene etv_aw13 with dissolve
                    b "{i}(No luck){/i}"
                    scene etv_aw12 with dissolve
                    m "Ahhh"
                    scene etv_aw12pov with dissolve
                    m "{i} (tangannya sangat kuat, seperti Stewart) {/i}"
                    scene etv_aw9 with dissolve
                    m "Itu bagus [bname]"
                    m "Saya pikir itu cukup untuk hari ini"
                    if elaine_convince == 4:
                        jump jenpractice
                    else:
                        pass
                    scene hall_m_n16 with fade
                    m "Selamat malam sayang"
                    b "Selamat malam"
                    scene etv_aw14 with dissolve
                    b "{i} (...) {/i}"
                    scene hall_n with fade
                    b "{i} (i \ 'D lebih baik tidur) {/i}"
                    jump newdays
        else:


            m "Tidak buruk, tapi itu cukup untuk hari ini"
            b "Ok"
            if elaine_convince == 4:
                jump jenpractice
            else:
                pass

            scene hall_m_n16 with fade
            show screen mrelup
            $ mrel += 1
            m "Selamat malam!"
            hide screen mrelup
            m "Pergi ke kamar Anda!"
            scene hall_n with fade
            b "{i} (sialan!) {/i}"
            b "{i} (Saya harus mengerjakan poin hubungan saya, 100) {/i}"
            b "{i} (Saya kira saya akan tidur juga) {/i}"
            jump newdays
    else:

        scene etv_aw_no with dissolve
        m "Terima kasih, saya baik -baik saja"
        scene etv_aw4 with fade
        "Anda terus menonton"
        if elaine_convince == 4:
            jump jenpractice
        else:
            pass
        scene hall_m_n16 with fade
        m "Selamat malam!"
        m "Pergi ke kamar Anda!"
        scene hall_n with fade
        b "{i} (sialan!) {/i}"
        b "{i} (Saya harus mengerjakan poin hubungan saya, 30) {/i}"
        b "{i} (Saya kira saya akan tidur juga) {/i}"
        jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
