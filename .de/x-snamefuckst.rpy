label snamefuckst:
    scene stst27 with fade
    if persistent.patch_enabled:
        s "Ayah!"
        pass
    else:
        s "Seh!"
        pass
    d "Senang bertemu denganmu lagi [sname]"
    scene stst28 with dissolve
    s "Dimana dia?"
    d "Dimana siapa?"
    s "Di mana Anda menyembunyikannya saat ini?"
    d "Siapa?"
    s "Ayo!"
    d "[sname] Saya tidak menyukai nada ini"
    s "Yeah"
    if sgoestost >2:
        scene stst28a with hpunch
        s "Dan apa yang akan Anda lakukan tentang itu"
        scene stst28b with fade
        d "Saya akan menunjukkan apa yang akan saya lakukan"
        scene stst28c with dissolve
        s "..."
        d "Ambillah"
        scene ddt
        $ persistent.unlock_60 = True
        s "..."
        d "Yeah"
        s "..."
        scene stst28d with dissolve
        "..."
        pass
    else:
        pass
    scene stst29 with fade
    s "Saya tidur di sini"
    d "Ok"
    scene stst33 with dissolve
    d "Tapi apakah [mname] OK dengan itu?"
    s "Jangan khawatir tentang dia"
    scene black
    "..."
    if jenopen >=2:
        scene black
        "SEMENTARA ITU"
        scene eljen with fade
        m "Lebih baik kita menunggu Elaine"
        $ jenopen += 1
        m "Jika Anda tidak keberatan"
        "Oke"
        "Saya akan memberi kami beberapa minuman"
        m "Ya terima kasih"
        scene eljen1 with fade
        m "Ah, ini dia"
        e "Maaf sudah terlambat, mari kita mulai"
        scene eljen2 with fade
        e "Jadi dengan siapa Anda ingin memulai?"
        "Keduanya untuk saat ini"
        "Sampai teman saya datang"
        scene eljen3 with dissolve

        "..."
        scene ejbj with fade
        m "..."
        scene ejbj1 with dissolve
        "..."
        e "..."
        scene eljen4 with dissolve
        "Hai teman -teman saya di sini"
        scene eljen5 with fade
        e "Jadi siapa yang mau siapa?"
        menu:
            "Mereka berdua menginginkan [mname]":
                scene eljen3 with dissolve
                e "Oh sungguh, jadi tidak ada yang menginginkanku sekarang"
                scene eljen5 with dissolve
                "Ayo Elaine, Anda tahu kami selalu menginginkan Anda"
                "Tapi kami melihat Anda hampir setiap hari, kami ingin mengubah rasa"
                e "Saya tidak berpikir dia akan menerima, apa [mname]"
                m "No"
                "Kami akan membayarnya sebanyak yang dia inginkan"
                e "$ 5000"
                "Kesepakatan"
                e "Tapi Anda harus santai saja padanya, dia baru dalam hal ini"
                "Oke"
                scene eljen6 with fade
                m "Please slowly"
                "Jangan khawatir"
                scene mdblp
                play sound "sounds/mdbl.wav"
                "..."
                m "Ahhh"
                "..."
                m "Ah"
                "..."
                stop sound
                scene eljen7 with fade
                "..."
                e "[mname] Anda luar biasa"
                e "Biarkan saya memijatnya untuk Anda"
                scene emjen
                "..."
                "..."
                pass
            "Pria kulit hitam itu menginginkan [mname]":

                scene eljen8 with fade
                $ persistent.unlock_61 = True
                m "Huh"
                scene eljen9 with dissolve
                m "{i} (apa ini menyentuh kaki saya) {/i}"
                scene eljen10 with hpunch
                m "Ah"
                scene eljen11 with dissolve
                m "Wha!"
                scene eljen12 with dissolve
                m "Ah"
                m "Enough please"
                scene eljen12a with fade
                "..."
                scene eljen12b with dissolve
                "..."
                pass
            "Pria di tempat tidur menginginkan [mname]":
                scene eljen13 with fade
                m "..."
                scene eljen14 with dissolve
                m "Ah"
                pass
    else:
        pass
    scene stst35 with fade
    s "Hey"
    s "Apa yang sedang kamu lakukan?"
    scene stst36 with dissolve
    d "Akan tidur"
    d "Sudah terlambat dan saya punya pekerjaan"
    s "Ok"
    scene stst56 with fade
    s "Apa yang kamu tidur secepat ini?"
    d "Saya lelah [sname] Saya mengadakan pertemuan di pagi hari"
    s "Mari kita lihat tentang itu"
    scene stlove
    d "Oh God"
    d "Stop"
    d "Ini salah"
    s "TIDAK..."
    s "It's not"
    if persistent.patch_enabled:
        s "Please daddy"
        pass
    else:
        s "Silakan!"
        pass
        scene stst63 with dissolve
        "..."
        d "Apa sekarang?"
        s "Saya menginginkannya"
    menu:
        "Dia akan mengizinkannya":
            scene fmd
            "..."
            s "Grrr"
            "..."
            s "..."
            s "Ahh"
            scene fmd271 with dissolve
            "..."
            scene stst64 with dissolve
            s "Finish inside"
            d "No"
            pass
        "TIDAK":
            d "No way"
            scene stst43 with dissolve
            s "Membosankan!"
            d "Pergi tidur sekarang"
            s "Selamat malam"
            "SEMENTARA ITU"
            scene jopen10 with fade
            m "[bname]!"
            m "Mengapa Anda tidur di sini, dan seperti ini?"
            scene jopen11 with dissolve
            b "Oh sorry"
            m "It's fine"
            m "Dimana [sname]?"
            b "Dia bilang dia akan melihat Rowena"
            if melsw >=9:
                pass
            elif msfkd >=1:
                pass
            else:
                m "Ok selamat malam"
                scene hall_n with fade
                "..."
                call screen gnav

            m "Saya akan minum"
            scene jopen12 with fade
            if jenopen ==1 and bnomn == 0:
                m "Saya ingin menanyakan pendapat Anda"
                b "Tentang apa?"
                m "Apa pendapat Anda tentang pekerjaan yang saya lakukan?"
                b "Maksudmu bekerja di klub?"
                m "Yes"
                b "Ini pekerjaan yang normal, sama seperti pekerjaan lain"
                m "Jadi maksud Anda, tidak apa -apa untuk Anda apa yang saya lakukan?"
                "Pastikan apa yang harus dipilih karena ini akan memengaruhi perilakunya"
                "Jika Anda ingin menjelajahi lebih banyak opsi, simpan di sini"
                menu:
                    "Tentu saja":
                        b "Tentu saja OK (NTR)"
                        $ jenopen += 1
                        m "Jadi begitu"
                        pass
                    "Baik itu tergantung pada apa yang Anda lakukan (tidak ada NTR)":

                        $ bnomn = 1
                        m "Jadi maksud Anda ada hal -hal yang tidak Anda terima"
                        b "Maksud saya bukan hanya saya"
                        b "Ada hal -hal yang tidak dapat diterima secara umum"
                        m "Jadi begitu"
                        pass
            else:
                pass
            scene jopen14 with dissolve
            b "Huh"
            m "Saya ingin pijat kaki"
            b "Sure"
            scene jopen15 with fade
            b "Bisakah saya melakukan punggung Anda setelah itu?"
            m "No"
            b "Lalu aku akan melakukan sesuatu yang lain"
            m "Tapi matikan lampu"
            m "Mungkin [sname] akan segera kembali"
            b "Dia menang"
            scene slm with dissolve
            m "Ah"
            scene slm1 with dissolve
            m "Yes"
            scene slm2 with dissolve
            m "Mhhmm"
            scene slm3 with dissolve
            m "Ahhh"
            m "Tunggu, giliranku"
            scene ssm
            $ persistent.unlock_57 = True
            b "Oh God"
            b "Mmm"
            "..."
            b "Ah"
            scene jopen16 with dissolve
            m "Ugh"
            scene jopen17 with fade
            b "Sampai jumpa lagi"
            scene hall_n with fade
            "..."
            jump newdays

    "..."
    menu:
        "Dia akan menciumnya":
            scene stst57 with dissolve
            "..."
            scene stst58 with dissolve
            s "Mmm"
            scene stst59 with dissolve
            s "Ahhh"
            scene stst60 with dissolve
            "..."
            scene stst61 with dissolve
            "..."
            scene stst62 with dissolve
            d "Hmm"
            scene stst56 with fade
            if persistent.patch_enabled:
                s "Selamat malam Ayah"
                pass
            else:
                s "Selamat malam"
                pass
            d "Selamat malam, saya harus tidur"
            d "Saya memiliki pekerjaan awal besok"
            d "Saya akan menyimpan uang untuk Anda di atas meja"
            s "Terima kasih"
            scene black
            "SEMENTARA ITU"
            scene jopen10 with fade
            m "[bname]!"
            m "Mengapa Anda tidur di sini, dan seperti ini?"
            scene jopen11 with dissolve
            b "Oh sorry"
            m "It's fine"
            m "Dimana [sname]?"
            b "Dia bilang dia akan melihat Rowena"
            if melsw >=9:
                pass
            elif msfkd >=1:
                pass
            else:
                m "Ok selamat malam"
                scene hall_n with fade
                "..."
                call screen gnav

            m "Saya akan minum"
            scene jopen12 with fade
            if jenopen ==1 and bnomn == 0:
                m "Saya ingin menanyakan pendapat Anda"
                b "Tentang apa?"
                m "Apa pendapat Anda tentang pekerjaan yang saya lakukan?"
                b "Maksudmu bekerja di klub?"
                m "Yes"
                b "Ini pekerjaan yang normal, sama seperti pekerjaan lain"
                m "Jadi maksud Anda, tidak apa -apa untuk Anda apa yang saya lakukan?"
                "Pastikan apa yang harus dipilih karena ini akan memengaruhi perilakunya"
                "Jika Anda ingin menjelajahi lebih banyak opsi, simpan di sini"
                menu:
                    "Tentu saja":
                        b "Tentu saja OK (NTR)"
                        $ jenopen += 1
                        m "Jadi begitu"
                        pass
                    "Baik itu tergantung pada apa yang Anda lakukan (tidak ada NTR)":

                        $ bnomn = 1
                        m "Jadi maksud Anda ada hal -hal yang tidak Anda terima"
                        b "Maksud saya bukan hanya saya"
                        b "Ada hal -hal yang tidak dapat diterima secara umum"
                        m "Jadi begitu"
                        pass
            else:
                pass
            scene jopen14 with dissolve
            b "Huh"
            m "Saya ingin pijat kaki"
            b "Sure"
            scene jopen15 with fade
            b "Bisakah saya melakukan punggung Anda setelah itu?"
            m "No"
            b "Lalu aku akan melakukan sesuatu yang lain"
            m "Tapi matikan lampu"
            m "Mungkin [sname] akan segera kembali"
            b "Dia menang"
            scene slm with dissolve
            m "Ah"
            scene slm1 with dissolve
            m "Yes"
            scene slm2 with dissolve
            m "Mhhmm"
            scene slm3 with dissolve
            m "Ahhh"
            m "Tunggu, giliranku"
            scene ssm
            $ persistent.unlock_57 = True
            b "Oh God"
            b "Mmm"
            "..."
            b "Ah"
            scene jopen16 with dissolve
            m "Ugh"
            scene jopen17 with fade
            b "Sampai jumpa lagi"
            scene hall_n with fade
            "..."
            jump newdays
        "Dia akan membiarkan dia melakukan apa yang dia inginkan":

            pass

    scene dste
    "..."
    d "Ahh"
    "..."
    s "..."
    scene stst53a with vpunch
    d "Kemarilah"
    scene stst53 with fade
    "..."
    scene stst54 with dissolve
    s "Apa rasanya seperti itu?"
    d "Apakah ini pertama kali Anda merasakan ini?"
    s "Yes"
    scene stst55 with dissolve
    d "Swallow, kamu akan baik -baik saja"
    s "..."
    s "Bisakah kamu meniduriku di lain waktu"
    d "[sname] !!"
    d "No"
    scene stst56 with fade
    if persistent.patch_enabled:
        s "Selamat malam Ayah"
        pass
    else:
        s "Selamat malam"
        pass
    d "Selamat malam, saya harus tidur"
    d "Saya memiliki pekerjaan awal besok"
    d "Saya akan menyimpan uang untuk Anda di atas meja"
    s "Terima kasih"
    scene black
    "SEMENTARA ITU"
    scene jopen10 with fade
    m "[bname]!"
    m "Mengapa Anda tidur di sini, dan seperti ini?"
    scene jopen11 with dissolve
    b "Oh sorry"
    m "It's fine"
    m "Dimana [sname]?"
    b "Dia bilang dia akan melihat Rowena"
    if melsw >=9:
        pass
    elif msfkd >=1:
        pass
    else:
        m "Ok selamat malam"
        scene hall_n with fade
        "..."
        call screen gnav

    m "Saya akan minum"
    scene jopen12 with fade
    if jenopen ==1 and bnomn == 0:
        m "Saya ingin menanyakan pendapat Anda"
        b "Tentang apa?"
        m "Apa pendapat Anda tentang pekerjaan yang saya lakukan?"
        b "Maksudmu bekerja di klub?"
        m "Yes"
        b "Ini pekerjaan yang normal, sama seperti pekerjaan lain"
        m "Jadi maksud Anda, tidak apa -apa untuk Anda apa yang saya lakukan?"
        "Pastikan apa yang harus dipilih karena ini akan memengaruhi perilakunya"
        "Jika Anda ingin menjelajahi lebih banyak opsi, simpan di sini"
        menu:
            "Tentu saja":
                b "Tentu saja OK (NTR)"
                $ jenopen += 1
                m "Jadi begitu"
                pass
            "Baik itu tergantung pada apa yang Anda lakukan (tidak ada NTR)":

                $ bnomn = 1
                m "Jadi maksud Anda ada hal -hal yang tidak Anda terima"
                b "Maksud saya bukan hanya saya"
                b "Ada hal -hal yang tidak dapat diterima secara umum"
                m "Jadi begitu"
                pass
    else:
        pass
    scene jopen14 with dissolve
    b "Huh"
    m "Saya ingin pijat kaki"
    b "Sure"
    scene jopen15 with fade
    b "Bisakah saya melakukan punggung Anda setelah itu?"
    m "No"
    b "Lalu aku akan melakukan sesuatu yang lain"
    m "Tapi matikan lampu"
    m "Mungkin [sname] akan segera kembali"
    b "Dia menang"
    scene slm with dissolve
    m "Ah"
    scene slm1 with dissolve
    m "Yes"
    scene slm2 with dissolve
    m "Mhhmm"
    scene slm3 with dissolve
    m "Ahhh"
    m "Tunggu, giliranku"
    scene ssm
    $ persistent.unlock_57 = True
    b "Oh God"
    b "Mmm"
    "..."
    b "Ah"
    scene jopen16 with dissolve
    m "Ugh"
    scene jopen17 with fade
    b "Sampai jumpa lagi"
    scene hall_n with fade
    "..."
    jump newdays



label snamefuckst1:
    scene stst27 with fade
    if persistent.patch_enabled:
        s "Ayah!"
        pass
    else:
        s "Seh!"
        pass
    d "Senang bertemu denganmu lagi [sname]"
    scene stst28 with dissolve
    s "Dimana dia?"
    d "Dimana siapa?"
    s "Di mana Anda menyembunyikannya saat ini?"
    d "Siapa?"
    s "Ayo!"
    d "[sname] Saya tidak menyukai nada ini"
    s "Yeah"
    if sgoestost >2:
        scene stst28a with hpunch
        s "Dan apa yang akan Anda lakukan tentang itu"
        scene stst28b with fade
        d "Saya akan menunjukkan apa yang akan saya lakukan"
        scene stst28c with dissolve
        s "..."
        d "Ambillah"
        scene ddt
        $ persistent.unlock_60 = True
        s "..."
        d "Yeah"
        s "..."
        scene stst28d with dissolve
        "..."
        pass
    else:
        pass
    scene stst29 with fade
    s "Saya tidur di sini"
    d "Ok"
    scene stst33 with dissolve
    d "Tapi apakah [mname] OK dengan itu?"
    s "Jangan khawatir tentang dia"
    scene black
    "..."
    scene stst35 with fade
    s "Hey"
    s "Apa yang sedang kamu lakukan?"
    scene stst36 with dissolve
    d "Akan tidur"
    d "Sudah terlambat dan saya punya pekerjaan"
    s "Ok"
    scene stst56 with fade
    s "Apa yang kamu tidur secepat ini?"
    d "Saya lelah [sname] Saya mengadakan pertemuan di pagi hari"
    s "Mari kita lihat tentang itu"
    scene stlove
    d "Oh God"
    d "Stop"
    d "Ini salah"
    s "TIDAK..."
    s "It's not"
    if persistent.patch_enabled:
        s "Please daddy"
        pass
    else:
        s "Silakan!"
        pass
        scene stst63 with dissolve
        "..."
        d "Apa sekarang?"
        s "Saya menginginkannya"
    menu:
        "Dia akan mengizinkannya":
            scene fmd
            "..."
            s "Grrr"
            "..."
            s "..."
            s "Ahh"
            scene fmd271 with dissolve
            "..."
            scene stst64 with dissolve
            s "Finish inside"
            d "No"
            pass
        "TIDAK":
            d "No way"
            scene stst43 with dissolve
            s "Membosankan!"
            d "Pergi tidur sekarang"
            s "Selamat malam"
            jump newdays

    "..."
    menu:
        "Dia akan menciumnya":
            scene stst57 with dissolve
            "..."
            scene stst58 with dissolve
            s "Mmm"
            scene stst59 with dissolve
            s "Ahhh"
            scene stst60 with dissolve
            "..."
            scene stst61 with dissolve
            "..."
            scene stst62 with dissolve
            d "Hmm"
            scene stst56 with fade
            if persistent.patch_enabled:
                s "Selamat malam Ayah"
                pass
            else:
                s "Selamat malam"
                pass
            d "Selamat malam, saya harus tidur"
            d "Saya memiliki pekerjaan awal besok"
            d "Saya akan menyimpan uang untuk Anda di atas meja"
            s "Terima kasih"
            jump newdays
        "Dia akan membiarkan dia melakukan apa yang dia inginkan":

            pass

    scene dste
    "..."
    d "Ahh"
    "..."
    s "..."
    scene stst53a with vpunch
    d "Kemarilah"
    scene stst53 with fade
    "..."
    scene stst54 with dissolve
    s "Apa rasanya seperti itu?"
    d "Apakah ini pertama kali Anda merasakan ini?"
    s "Yes"
    scene stst55 with dissolve
    d "Swallow, kamu akan baik -baik saja"
    s "..."
    s "Bisakah kamu meniduriku di lain waktu"
    d "[sname] !!"
    d "No"
    scene stst56 with fade
    if persistent.patch_enabled:
        s "Selamat malam Ayah"
        pass
    else:
        s "Selamat malam"
        pass
    d "Selamat malam, saya harus tidur"
    d "Saya memiliki pekerjaan awal besok"
    d "Saya akan menyimpan uang untuk Anda di atas meja"
    s "Terima kasih"
    jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
