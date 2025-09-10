label sundayrelax:
    scene b_relax_d with dissolve
    "..."
    m "[bname]"
    scene b_relax_d2 with dissolve
    b "Apa?"
    m "Bangun, kita harus melakukan pembersihan yang mendalam"
    b "Aku!"
    b "Saya seorang pria"
    b "Anda memiliki [sname] untuk jenis pekerjaan ini"
    m "Bangun!!"
    m "[sname] akan membantu juga"
    b "{i}(Damn){/i}"
    scene b_relax_d3 with dissolve
    m "Anda membersihkan kamar tidur Anda"
    m "[bname] Dan saya akan melakukan dapur, toilet, dan kamar saya"
    s "OK"
    m "[bname] Ikuti saya"
    scene sdayclea with fade
    if mrel>=100:
        m "Saya akan berubah, lanjutkan dengan kuas"
        b "Ok"
        m "Dan tolong putar"
        scene sdayclea1 with fade
        "..."
        scene sdayclea1a with dissolve
        "..."
        pass
    else:

        m "Saya perlu berubah"
        m "Tunggu di pintu"
        scene door with fade
        "..."
        m "Anda mungkin masuk"
        pass
    scene sdayclea2 with fade
    m "Jangan lagi datang ke bagian ini"
    m "Anda sudah melakukannya sudah pergi ke dekat jendela"
    menu:
        "Melihat lebih dekat":
            scene sdayclea3 with dissolve
            b "Hmmm"
            if mrel >= 450:
                scene sdclea77a with dissolve
                m "..."
                pass
            elif mfuckedsober >=1:
                scene sdclea77a with dissolve
                m "..."
                pass
            else:
                scene sdclea77 with dissolve
                m "Hai!"
                pass
        "OKE":
            pass
    scene sdayclea4 with fade
    b "I'm done"
    m "Oke, periksa [sname]"
    m "Temui aku di dapur nanti"
    m "Saya akan menyelesaikan mopping terlebih dahulu"
    if mnightie == 1:
        $ mnightie = 2
        b "Aku punya sesuatu untukmu"
        m "Letakkan di tempat tidur, dan keluar dari sini"
        scene sdayclea5 with dissolve
        "..."
        scene sdayclea6 with vpunch
        m "Oh [bname]"
        b "Ups ember!"
        m "..."
        b "Saya harap Anda menyukainya"
        show screen mrelup
        $ mrel += 2
        m "Ya saya menyukainya"
        hide screen mrelup
        b "Aku akan sampai jumpa di dapur"
        pass
    else:
        pass
    scene black with fade
    "..."
    scene sdayclea7 with fade
    b "Ia!"
    s "Apa yang kamu inginkan?"
    b "Saya datang untuk memeriksa Anda"
    scene sdayclea8 with dissolve
    s "Periksa saya?!"
    b "Yes"
    if persistent.patch_enabled:
        b "Ibu menyuruhku untuk memeriksa apakah kamu membersihkan dengan benar"
        pass
    else:
        b "[mname] Memberitahu saya untuk memeriksa apakah Anda membersihkan dengan benar"
        pass
    s "Hmm"
    scene sdayclea9 with dissolve
    if sbm ==2:
        s "Baik Anda lebih baik mengambil ini dan mulai membersihkan"
        s "Here"
        b "Apa?"
        s "Ambillah, atau saya akan menunjukkan video masturbasi Anda kepadanya"
        b "{i} (fuck!) {/i}"
        b "OK"
        scene sdayclea10 with fade
        "..."
        b "Saya hampir selesai"
        s "Lakukan dengan baik, saya akan memeriksa pekerjaan Anda"
        b "Apa ..."
        scene sdayclea11 with dissolve
        s "{i}(Hehe){/i}"
        "..."
        scene sdayclea10 with fade
        s "Anda mungkin pergi sekarang"
        s "Saya akan memeriksanya nanti"
        pass
    else:
        s "Pergi bercinta diri sendiri"
        b "Hehehe"
        pass
    scene sdayclea66 with dissolve
    b "Bagaimana jika saya tidak?"
    s "Pergilah!"
    scene sdayclea67 with vpunch
    if srel >=200 and sdom >=100:
        s "Tolong hentikan [bname]"
        b "Hmm"
        scene sdayclea68 with hpunch
        s "Huh"
        scene sdayclea69 with dissolve
        b "Lepaskan kemeja ini"
        scene sds
        s "Ahh"
        b "Mmm"
        "..."
        s "Ah"
        m "[bname]!"
        scene sdayclea70 with hpunch
        s "Hah!"
        s "Cepat, sembunyikan"
        scene sdayclea71 with fade
        m "Dimana [bname]?"
        s "Aku tidak tahu"
        m "Hmm"
        m "Saya mengatakan kepadanya untuk datang dan membantu Anda"
        s "Ya dia ada di sini, tapi dia pergi"
        m "Jadi begitu"
        menu:
            "[mname] akan membersihkan dapur **":
                pass
            "[mname] akan mengikutinya ke toilet":

                scene room3 with fade
                m "Ah kamu di sini?"
                b "Ermm yes"
                if mfuckedsober >= 1 and mrel >=300:
                    m "Apa?"
                    m "Apakah itu lagi?"
                    scene sdayclea73 with dissolve
                    b "Er no aku \ 'm ok"
                    scene sdayclea74 with dissolve
                    m "Sepertinya Anda senang Anda selalu mengalami masalah ini"
                    b "Masalah mana"
                    scene sdayclea75 with dissolve
                    m "Duduklah di sisi bak mandi"
                    scene sdayclea76 with dissolve
                    m "Hmm"
                    b "Apa?"
                    scene sdm
                    "..."
                    scene sdmend with fade
                    m "Anda datang cepat kali ini"
                    m "Anda bisa pergi sekarang"
                    scene hall_d with fade
                    b "{i} (...) {/i}"
                    call screen gnav
                else:

                    m "Apakah Anda mandi?"
                    b "Yes"
                    m "Apakah Anda menyelesaikan pembersihan"
                    b "Of course"
                    m "Baiklah, sampai jumpa nanti"
                    scene hall_d with fade
                    b "{i} (...) {/i}"
                    call screen gnav
    else:

        s "Hai!"
        s "Keluar!"
        b "Ok ok, santai saja!"
        "Naikkan hubungan Anda menjadi 200 dan dominasi menjadi 100"
        pass

    scene black with fade
    "..."
    scene sdayclea12 with fade
    "..."
    m "Saya kira itu cukup"
    b "Ya tempat itu bersinar"
    scene sdayclea13 with fade
    m "Terima kasih sayang"
    menu:
        "Mencuri ciuman":
            scene sdayclea13k with dissolve
            m "..."
            if mrel >350:
                scene sdayclea13k1 with dissolve
                m "{i} (apa itu ...) {/i}"
                scene sdayclea13k2 with dissolve
                $ mcorr += 1
                show screen mcorr
                m "{i} (dia lakukan!) {/i}"
                hide screen mcorr
                menu:
                    "Sentuh payudara":
                        scene sdayclea13tb with dissolve
                        m "{i} (huh!) {/i}"
                        $ mcorr += 1
                        pass
                    "Jangan":
                        pass
            else:


                scene sdayclea13kr with hpunch
                m "Hai!"
                b "Sorry"
                b "Mistake"
                pass
        "Jangan":



            pass
    "..."
    if mrel >=100:
        m "Mari ikut saya"
        m "Aku punya sesuatu untukmu"
        scene sdayclea14 with fade
        m "Pakai"
        b "..."
        m "Ayo coba, izinkan saya melihat apakah itu cocok"
        b "Di Sini?"
        m "Ya, lepaskan pakaian Anda"
        scene sdayclea15 with dissolve
        "..."
        menu:
            "Berbelok":
                scene sdayclea19 with dissolve
                m "Mengapa Anda berbalik?"
                b "I'm shy"
                m "Ayo"
                m "Tidak ada yang belum pernah saya lihat sebelumnya"
                scene sdayclea20 with dissolve
                $ mcorr += 1
                if mfuckedsober >= 1:
                    m "Apakah itu? Masih seperti terakhir kali"
                    b "Tidak, tidak apa -apa sekarang"
                    scene sdayclea21 with dissolve
                    show screen mcorr
                    m "Apa kamu yakin"
                    hide screen mcorr
                    b "Yes"
                    b "Kadang -kadang sedikit lebih sulit dari biasanya"
                    scene sdayclea22 with dissolve
                    "..."
                    scene sdaycleaanal_bw with fade
                    m "{i} (ada sesuatu yang mencurigakan tentang ini) {/i}"
                    pass
                else:
                    pass
                m "Baik jika ada sesuatu yang harus Anda malu"
                scene sdayclea21 with dissolve
                show screen mcorr
                m "Ini perut ini"
                hide screen mcorr
                if mfuckedsober >= 1:
                    m "Mhm"
                    scene sdayclea22 with dissolve
                    m "{i} (tenang [mname]) {/i}"
                    scene sdayclea18 with fade
                    m "Tampak bagus untukmu"
                    b "Yes thanks"
                    s "Pakaian yang bagus"
                    scene sdclea78 with dissolve
                    m "Hi [sname]"
                    s "Cleaning finished"
                    m "Terima kasih"
                    m "Oke, saya ingin tidur siang"
                    m "Terima kasih"
                    b "Ok"
                    scene sdclea79 with fade
                    b "Hey wait"
                    s "Apa?"
                    b "Mengapa Anda tidak mengunjungi Rowena baru -baru ini?"
                    s "Saya, kenapa?"
                    s "Apakah Anda ingin melihatnya?"
                    b "Tidak, tidak, tapi ..."
                    b "Saya punya dua tiket untuk bioskop"
                    b "Jika Anda ingin mengundangnya?"
                    s "Hmm"
                    s "Baiklah, beri aku"
                    if mny >=100:
                        b "Di sini 00 sebagai gantinya"
                        s "Thanks"
                        b "Berhati -hatilah, nikmati"
                        scene sdclea80 with dissolve
                        s "{i}(Hmm){/i}"
                        jump msundaysex
                    else:
                        pass
                    b "Saya tidak ingat di mana tiketnya jujur"
                    s "Ok kemudian berhenti mengganggu saya"
                    scene hall_d with fade
                    b "{i} (...) {/i}"
                    call screen gnav

                elif melsw >=9:
                    m "Mhm"
                    scene sdayclea22 with dissolve
                    m "{i} (tenang [mname]) {/i}"
                    scene sdayclea18 with fade
                    m "Tampak bagus untukmu"
                    b "Yes thanks"
                    s "Pakaian yang bagus"
                    scene sdclea78 with dissolve
                    m "Hi [sname]"
                    s "Cleaning finished"
                    m "Terima kasih"
                    m "Oke, saya ingin tidur siang"
                    m "Terima kasih"
                    b "Ok"
                    scene sdclea79 with fade
                    b "Hey wait"
                    s "Apa?"
                    b "Mengapa Anda tidak mengunjungi Rowena baru -baru ini?"
                    s "Saya, kenapa?"
                    s "Apakah Anda ingin melihatnya?"
                    b "Tidak, tidak, tapi ..."
                    b "Saya punya dua tiket untuk bioskop"
                    b "Jika Anda ingin mengundangnya?"
                    s "Hmm"
                    s "Baiklah, beri aku"
                    if mny >=100:
                        b "Di sini 00 sebagai gantinya"
                        s "Thanks"
                        b "Berhati -hatilah, nikmati"
                        scene sdclea80 with dissolve
                        s "{i}(Hmm){/i}"
                        jump msundaysex
                    else:
                        pass
                    b "Saya tidak ingat di mana tiketnya jujur"
                    s "Ok kemudian berhenti mengganggu saya"
                    scene hall_d with fade
                    b "{i} (...) {/i}"
                    call screen gnav

                elif msfkd >= 1:
                    m "Mhm"
                    scene sdayclea22 with dissolve
                    m "{i} (tenang [mname]) {/i}"
                    scene sdayclea18 with fade
                    m "Tampak bagus untukmu"
                    b "Yes thanks"
                    s "Pakaian yang bagus"
                    scene sdclea78 with dissolve
                    m "Hi [sname]"
                    s "Cleaning finished"
                    m "Terima kasih"
                    m "Oke, saya ingin tidur siang"
                    m "Terima kasih"
                    b "Ok"
                    scene sdclea79 with fade
                    b "Hey wait"
                    s "Apa?"
                    b "Mengapa Anda tidak mengunjungi Rowena baru -baru ini?"
                    s "Saya, kenapa?"
                    s "Apakah Anda ingin melihatnya?"
                    b "Tidak, tidak, tapi ..."
                    b "Saya punya dua tiket untuk bioskop"
                    b "Jika Anda ingin mengundangnya?"
                    s "Hmm"
                    s "Baiklah, beri aku"
                    if mny >=100:
                        b "Di sini 00 sebagai gantinya"
                        s "Thanks"
                        b "Berhati -hatilah, nikmati"
                        scene sdclea80 with dissolve
                        s "{i}(Hmm){/i}"
                        jump msundaysex
                    else:
                        pass
                    b "Saya tidak ingat di mana tiketnya jujur"
                    s "Ok kemudian berhenti mengganggu saya"
                    scene hall_d with fade
                    b "{i} (...) {/i}"
                    call screen gnav
                else:

                    m "{i} (apakah penisnya brengsek) {/i}"
                    scene sdayclea22 with dissolve
                    m "{i} (oh my, itu langkah yang salah) {/i}"
                    pass
                    if mcorr >=40:
                        m "{i} (Saya perlu memeriksa ulang) {/i}"
                        scene sdayclea21 with dissolve
                        "..."
                        scene sdayclea22 with dissolve
                        m "{i} (sepertinya dia naif) {/i}"
                        m "{i} (ayolah [mname]) {/i}"
                        scene sdayclea22a with dissolve
                        m "{i} (itu adalah refleks alami) {/i}"
                        pass
                    else:

                        "Naikkan poin korupsi Anda menjadi 40"
                        pass
                scene sdayclea18 with fade
                m "Tampak bagus untukmu"
                pass
            "Jangan giliran":

                scene sdayclea16 with dissolve
                "..."
                scene sdayclea17 with dissolve
                b "Dimana itu?"
                m "Dimana apa?"
                b "Hal yang Anda ingin saya pakai"
                scene sdayclea16 with dissolve
                m "Ah di sini, ambillah"
                scene sdayclea18 with dissolve
                m "Tampak sempurna"
                pass

        b "Terima kasih untuk itu"
        scene sdayclea23 with fade
        b "Terima kasih"
        m "Anda menyambut sayang"
        if mcorr >=20:
            m "Saya akan tidur siang sekarang"
            menu:
                "Melanjutkan":
                    scene sdayclea24 with fade
                    "..."
                    scene sdayclea31 with dissolve
                    "..."
                    if elaine_convince >= 4 and mrel>=300:
                        scene sdayclea33 with dissolve
                        m "[bname]"
                        m "Anda masih di sini?"
                        b "Ya maaf saya melepas ini"
                        scene sdayclea35 with dissolve
                        b "Apa?"
                        m "Lanjutkan, jangan keberatan"
                        scene sdayclea36 with dissolve
                        "..."
                        scene sdayclea37 with dissolve
                        m "Katakan padaku apakah kamu tinggal di sini untuk melihat aku menanggalkan pakaian?"
                        b "..."
                        b "Tidak, tentu saja tidak"
                        scene sdayclea38 with dissolve
                        m "Ok saya lihat"
                        menu:
                            "Selesai dan Pergi":
                                b "I'm done"
                                pass
                            "Lihat pantatnya":

                                scene sdayclea39 with dissolve
                                b "{i}(Gorgeous){/i}"
                                scene sdayclea40 with dissolve
                                $ mcorr += 1
                                show screen mcorr
                                m "Hmmm"
                                hide screen mcorr
                                scene sdayclea41 with dissolve
                                if mcorr >=35:
                                    m "{i} (hmm apakah dia ...?) {/i}"
                                    m "{i} (mari kita lihat) {/i}"
                                    scene sdayclea42 with dissolve
                                    m "Ups saya menjatuhkan ponsel saya"
                                    b "Ughhh"
                                    scene sdayclea43 with dissolve
                                    b "{i} (fuck!) {/i}"
                                    b "SAYA..."
                                    b "Saya harus pergi"
                                    b "Bye"
                                    if mboobstalk ==1 and mrel<450:
                                        scene sdayclea38 with dissolve
                                        m "Tunggu!"
                                        b "Saya tidak bisa pergi"
                                        m "Aku bilang tunggu!"
                                        scene sdayclea45 with dissolve
                                        m "Apa yang salah?"
                                        m "Anda tidak terlihat baik -baik saja"
                                        b "Ya saya harus pergi"
                                        scene sdayclea46 with dissolve
                                        m "Tidak, tunggu"
                                        scene sdayclea47 with dissolve
                                        m "Jadi katakan padaku"
                                        b "Tentang apa?"
                                        m "Tentang apa yang ditanyakan Elaine terakhir kali di pantai"
                                        m "Dan Anda suka menonton payudara Elaine"
                                        m "Jadi beri tahu saya?"
                                        scene sdayclea57 with dissolve
                                        b "{i} (huh!) {/i}"
                                        scene sdayclea58 with dissolve
                                        m "Mana yang lebih baik?"
                                        scene sdayclea59 with dissolve
                                        b "{i} (oh fuck!) {/i}"
                                        b "{i} (Saya harus keluar dari sini sebelum saya menyemprot ...) {/i}"
                                        scene sdayclea60 with dissolve
                                        m "Jadi mana yang lebih baik?"
                                        scene sdayclea61 with dissolve
                                        b "Y ..."
                                        scene sdayclea62 with dissolve
                                        b "Milikmu..."
                                        scene sdayclea63 with fade
                                        b "{i} (apa yang saya lakukan ...) {/i}"
                                        scene hall_d with fade
                                        b "{i} (...) {/i}"
                                        call screen gnav

                                    elif mrel>=450:
                                        scene sdayclea38 with dissolve
                                        m "Tunggu!"
                                        b "Saya tidak bisa pergi"
                                        m "Aku bilang tunggu!"
                                        scene sdayclea45 with dissolve
                                        m "Apa yang salah?"
                                        m "Anda tidak terlihat baik -baik saja"
                                        b "Ya saya harus pergi"
                                        scene sdayclea46 with dissolve
                                        m "Tidak, tunggu"
                                        scene sdayclea47 with dissolve
                                        m "Anda bisa memberi tahu saya sayang"
                                        m "Apa yang salah?"
                                        b "{i} (duh!) {/i}"
                                        b "Nothing"
                                        m "{i} (Saya perlu mengajarinya pelajaran) {/i}"
                                        if mfuckedsober >= 1:
                                            m "{i} (kecuali itu priapisme lagi) {/i}"
                                            scene sdayclea47worried with dissolve
                                            m "{i} (Mungkinkah itu saya alasan priapismenya!) {/i}"
                                            pass
                                        else:
                                            pass
                                        scene sdayclea48 with dissolve
                                        m "{i} (hmm!) {/i}"
                                        scene sdayclea47 with dissolve
                                        m "Tapi kamu terlihat sedih dan khawatir"
                                        m "Atau mungkin lelah?"
                                        m "Aku tahu bagaimana menghiburmu"
                                        m "Kenakan pakaianmu dan ikut aku"
                                        scene sdayclea49 with fade
                                        m "Izinkan saya memberi Anda cepat mencuci"
                                        scene sdayclea50 with dissolve
                                        m "Anda akan merasa lebih baik setelah ini"
                                        scene sdayclea51 with dissolve
                                        m "Berdiri biarkan aku mencuci perut dan paha"
                                        scene sdayclea52 with dissolve
                                        m "Stand still"
                                        scene sdayclea53 with dissolve
                                        "..."
                                        scene sdayclea52 with dissolve
                                        "..."
                                        b "{i}(Focus [bname]){/i}"
                                        scene sdayclea54 with dissolve
                                        b "{i} (Saya tidak peduli lagi) {/i}"
                                        b "{i} (dia melakukan itu dengan sengaja) {/i}"
                                        scene sdayclea55 with dissolve
                                        b "Ahhh!"
                                        scene sdayclea56 with dissolve
                                        m "{i} (oh Tuhan apa yang baru saja saya lakukan!) {/i}"
                                        m "{i} (apakah saya sangat kekurangan!) {/i}"
                                        m "{i} (sejauh saya hampir memberikan handjob ...) {/i}"
                                        if mfuckedsober >= 1:
                                            m "{i} (tapi setidaknya dia merasa lebih baik sekarang) {/i}"
                                            m "{i}(Hopefully){/i}"
                                            "..."
                                            m "{i} (Saya harus memverifikasi jika dia baik -baik saja) {/i}"
                                            scene sdayclea64 with dissolve
                                            m "Tetap?"
                                            b "Tetap apa?"
                                            m "Apakah kamu yakin ini oke?"
                                            b "Sedikit rasa sakit, tapi akan baik -baik saja"
                                            m "Bagus"
                                            m "Saya akan pergi sekarang"
                                            m "Bersihkan dan Pergi"
                                            scene sdayclea65 with dissolve
                                            b "{i} (i \ 'm mulai menyukai ini) {/i}"
                                            scene hall_d with fade
                                            b "{i} (...) {/i}"
                                            call screen gnav
                                        else:

                                            m "Saya akan pergi sekarang"
                                            m "Bersihkan dan Pergi"
                                            scene hall_d with fade
                                            b "{i} (...) {/i}"
                                            call screen gnav
                                    else:

                                        pass
                                    scene sdayclea44 with fade
                                    m "Hmm"
                                    scene hall_d with fade
                                    b "{i} (...) {/i}"
                                    call screen gnav
                                else:

                                    "Korupsi 35 poin diperlukan"
                                    pass

                                m "Anda bisa pergi sekarang [bname]"
                                scene sdayclea34 with dissolve
                                b "Bye"
                                scene hall_d with fade
                                b "{i} (...) {/i}"
                                call screen gnav

                        m "Oke, silakan pergi"
                        scene sdayclea34 with dissolve
                        b "Bye"
                        scene hall_d with fade
                        b "{i} (...) {/i}"
                        call screen gnav


                    elif mrel >=300:
                        scene sdayclea33 with dissolve
                        m "[bname] Anda masih di sini?"
                        b "Ya maaf saya melepas ini"
                        m "Oke, silakan pergi"
                        scene sdayclea34 with dissolve
                        b "Bye"
                        scene hall_d with fade
                        b "{i} (...) {/i}"
                        call screen gnav
                    else:

                        scene sdayclea32 with dissolve
                        m "Kenapa kamu masih di sini?"
                        m "Keluar!"
                        b "Sorry"
                        scene hall_d with fade
                        b "{i} (...) {/i}"
                        call screen gnav

                "Dapatkah saya melihat hal yang ingin Anda tunjukkan ketika Anda memiliki malam perempuan dengan Elaine?" if jenteaselingerie ==1 and  mrel >=150:
                    m "Hmm Ok"
                    m "Duduk, aku akan kembali"
                    jump jenteasebik

                "Apakah Anda membeli sesuatu yang baru?" if mrel >=250:
                    m "Apa maksudmu?"
                    b "Maksud saya jika Anda menginginkan pendapat saya"
                    m "Hmm Ok"
                    m "Duduk, aku akan kembali"
                    jump jenteasebik

                "Dapatkah saya melihat apakah gaun tidur yang saya berikan pada Anda?" if mnightie == 2 and  mrel >=200:
                    m "Saya pikir saya telah menunjukkannya kepada Anda, bukan?!"
                    m "Pokoknya ya, saya sudah mencobanya sebelumnya"
                    b "Ah Ok"
                    m "Pokoknya duduk, aku akan memakainya"
                    scene sdayclea24 with fade
                    if mcorr >=35:
                        "..."
                        scene sdayclea30 with dissolve
                        "..."
                        scene sdayclea31 with dissolve
                        pass
                    else:

                        m "Jangan lihat sisi ini"
                        "Naikkan poin korupsi Anda menjadi 35"
                        pass

                    scene sdayclea25 with fade
                    m "Senang sekarang"
                    b "Ya bagus"
                    scene sdayclea26 with fade
                    m "Sampai jumpa lagi"
                    m "Saya akan tidur siang sekarang"
                    scene hall_d with fade
                    b "{i} (...) {/i}"
                    scene black
                    "SEMENTARA ITU"
                    scene sdayclea27 with fade
                    m "{i} (dia mulai terlihat sangat mirip dengan Stewart dalam setelan ini) {/i}"
                    if mcorr >=40:
                        scene sdayclea27a with dissolve
                        "..."
                        pass
                    else:
                        pass

                    m "{i} (i \ \ 'll mengambil tidur singkat) {/i}"
                    scene sdayclea28 with fade
                    m "{i} (bagaimana saya melewatkan bajingan ini) {/i}"
                    scene sdayclea29 with dissolve
                    m "{i} (don \ 't [mname]!) {/i}"
                    m "{i} (Saya harus mengajarinya pelajaran) {/i}"
                    if mcorr >=40:
                        scene sdayclea21bw with dissolve
                        "..."
                        scene sdayclea30bw with dissolve
                        "..."
                        scene sdayclea28 with dissolve
                        m "{i} (hentikan [mname]) {/i}"
                        pass
                    else:
                        m "{i} (Saya tidak akan menerima sesuatu yang kurang dari dia memohon lututnya) {/i}"
                        pass
                    scene hall_d with fade
                    "..."
                    call screen gnav



                "{s} Bisakah saya melihat apakah nightie yang saya berikan pada Anda? {/s}" if mnightie == 2 and mrel <200:
                    m "Saya pikir saya telah menunjukkannya kepada Anda, bukan?!"
                    m "Pokoknya ya, saya sudah mencobanya sebelumnya"
                    b "Ah Ok"
                    m "Sampai jumpa lagi"
                    m "Saya akan tidur siang sekarang"
                    pass
        else:
            m "Saya akan tidur siang sekarang"
            "Naikkan poin korupsi Anda untuk melihat lebih banyak"
            pass
    else:


        pass
    scene hall_d with fade
    b "{i} (...) {/i}"
    call screen gnav


label jenteasebik:
    scene jenbik with fade
    b "Yang bagus"
    b "Mengapa Anda tidak memakainya ke pantai?"
    scene jenbik1 with dissolve
    m "..."
    scene jenbik2 with dissolve
    m "{i} (Saya harap ini membuatnya mengerti mengapa) {/i}"
    scene jenbik with dissolve
    if mboobstalk ==1:
        m "Jadi Anda benar -benar berpikir saya harus memakainya ke pantai?"
        b "Yes"
        m "Tapi kadang -kadang kita pergi ke pantai telanjang"
        m "Dan saya tahu Anda menyukainya"
        scene jenbik3 with dissolve
        m "Dan Anda suka menonton payudara Elaine"
        scene jenbik4 with dissolve
        b "Apa! TIDAK"
        scene jenbik5 with dissolve
        m "Jadi siapa yang memiliki payudara yang lebih baik?"
        menu:
            "Anda":
                "Anda"
                m "Hmm"
                pass
            "Apakah mereka nyata?" if mrel >=300:
                scene jenbik6 with vpunch
                m "Permisi!!!"
                m "Kemarilah"
                m "Rasakan mereka"
                b "Errr"
                scene jenbik7 with dissolve
                m "Jadi? Bagaimana menurutmu?"
                scene jenbik8 with dissolve
                b "Mereka merasa sangat baik dan tegas"
                m "Terima kasih"
                "Itu semua di sini"
                pass
    else:

        pass
    m "Baiklah, sampai jumpa nanti"
    scene hall_d with fade
    b "{i} (...) {/i}"
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
