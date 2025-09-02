label toi_menu:
    if Hour >=9 and Hour <10:
        scene toi_d with fade
        b "{i} (tidak ada orang di sini) {/i}"
        b "{i} (dan saya tidak ingin menggunakan toilet sekarang) {/i}"
        call screen gnav

    elif Hour ==10:
        $ Hour += 1
        scene room3 with fade
        b "Hah!"
        b "Siapa \ 'yang masuk?"
        s "Itu aku!"
        s "Stay out"
        b "Duh! Itu terkunci"
        if toidoorscrew ==0 and workrequest ==3 and day !=7:
            $ toidoorscrew = 1
            b "{i} (Saya berharap saya dapat menemukan cara untuk membuka pintu ini) {/i}"
            pass

        elif toidoorscrew ==3 and workrequest ==3 and day !=7:
            scene room3 with dissolve
            b "{i} (mari coba dengan obeng) {/i}"
            "..."
            b "{i}(Cool){/i}"
            menu:
                "Memasuki":
                    jump toidoorscewed_morning
                "Tunggu":

                    pass
        else:


            pass
        scene toi_d_s with fade
        s "Oh, ya maksud saya tunggu!"
        b "OKE!!"
        b "Stop yelling"
        if sdom >=10:
            scene toi_d_s2 with dissolve
            s "Tunggu sebentar, hampir selesai"
            b "Saya tidak bisa menunggu saya pergi"
            scene toi_d with fade
            "..."
            call screen gnav
        else:
            scene toi_d with fade
            b "{i} (i \ 'll cuti, pasang!) {/i}"
            "Naikkan Poin Dominasi Anda"
            call screen gnav

    elif Hour ==11:
        $ Hour += 1
        scene toi_d with fade
        menu:
            "Gunakan toilet":
                scene toi_d_b with fade
                b "Ahhh"
                b "Nice"
                $ btoiuse += 1
                if btoiuse >=3 and sdom >=5:
                    scene toi_d_b6 with hpunch
                    s "Haa !!"
                    $ btoiuse += 1
                    b "Hai!"
                    if persistent.patch_enabled:
                        b "Saya akan memberi tahu ibu"
                        pass
                    else:
                        b "Saya akan memberi tahu [mname]"
                        pass
                    $ sdom += 1
                    scene toi_d_b7 with dissolve
                    s "..."
                    scene toi_d_b7a with dissolve
                    s "Dengan serius!"
                    s "Akulah yang akan memberitahunya!"
                    if btoiuse >= 6:
                        menu:
                            "Mendekati":
                                scene toi_d_b9 with fade
                                s "Kenapa kamu mendekatiku dengan benda itu!"
                                b "Hal apa?"
                                scene toi_d_b10 with dissolve
                                s "Itu!"
                                scene toi_d_b11 with dissolve
                                "..."
                                b "Benar-benar! Anda menerobos pintu tanpa memeriksa bahkan"
                                b "Dan Anda ceritakan tentang ini!"
                                b "Itu saja, aku sudah selesai denganmu"
                                b "Saya akan memberi tahu [mname]"
                                if workrequest ==3:
                                    scene toi_d_b12 with dissolve
                                    s "Oh jadi kamu mengubah tabel sekarang!?"
                                    b "Saya tidak mengubah apapun"
                                    b "Pikirkan sebelum Anda memberi tahu [mname]"
                                    b "Anda masuk, sementara Anda tahu saya ada di sini"
                                    s "Saya tidak tahu"
                                    b "Hmm"
                                    menu:
                                        "Beri aku handuk di sana" if sdom >=10:
                                            b "Dan biarkan masa lalu berlalu"
                                            scene toi_d_b13 with fade
                                            s "Here"
                                            scene toi_d_b14 with dissolve
                                            b "Thanks"
                                            show screen scorr
                                            b "Lihat ya!"
                                            hide screen scorr
                                            $ scorr += 1
                                            scene toi_d_b11a with dissolve
                                            "..."
                                            scene toi_d with fade
                                            "..."
                                            call screen gnav
                                        "Mari kita lupakan semuanya":


                                            b "Seolah -olah itu tidak pernah terjadi"
                                            s "Ok"
                                            s "Sorry anyway"
                                            b "Ok"
                                            pass
                                else:


                                    scene toi_d_b11a with dissolve
                                    b "Hah!"
                                    b "She left"
                                    pass
                            "Jangan":

                                pass
                    else:
                        pass
                    scene toi_d_b8 with dissolve
                    show screen sdomup
                    b "Hmmm"
                    hide screen sdomup
                    "..."
                    pass
                else:


                    pass
                scene toi_d with fade
                "..."
                call screen gnav
            "Kunci pintu dan gunakan toilet":

                scene toi_d_b with fade
                b "Ahhh"
                b "Nice"
                scene toi_d with dissolve
                "..."
                call screen gnav

    elif Hour >=12 and Hour <15:
        scene toi_d with fade
        b "{i} (tidak ada orang di sini) {/i}"
        b "{i} (dan saya tidak ingin menggunakan toilet sekarang) {/i}"
        call screen gnav

    elif Hour ==15:
        if workrequest ==3 and day ==7:
            $ Hour += 1
            scene toi_d with fade
            b "{i}(Hmm No one here){/i}"
            b "{i} (Let \ 'S Empty the Tank) {/i}"
            scene toi_d_b with fade
            "..."
            play sound "sounds/door_openc.wav"
            m "Oh"
            m "Sorry [bname]"
            m "Saya tidak mengenal Anda di sini"
            stop sound
            menu:
                "Berbelok":
                    scene toi_d_m with dissolve
                    b "Saya hampir selesai"
                    $ mcorr += 1
                    m "..."
                    m "Ini ... tidak apa -apa saya tidak ingin menggunakan toilet"
                    b "Oh"
                    b "Lalu apa yang ingin Anda lakukan?"
                    m "Saya ingin ..."
                    scene toi_d_m1 with dissolve
                    m "Bisakah Anda terlebih dahulu menarik celana pendek Anda?"
                    d "Oh sorry"
                    d "Lagipula aku akan pergi"
                    scene toi_d_m2 with dissolve
                    m "Ok"
                    scene room3 with fade
                    "..."
                    menu:
                        "Kembali":
                            scene toi_d_m11 with dissolve
                            b "Err"
                            if mrel >=150 and elaine_convince == 4:
                                scene toi_d_m13 with dissolve
                                m "[bname] Apa yang Anda inginkan?"
                                b "Err"
                                b "Saya lupa sesuatu"
                                m "Ok get It Please"
                                scene toi_d_m14 with dissolve
                                b "{i} (bercinta, apa yang harus diambil) {/i}"
                                b "{i} (gerakan itu tidak dihitung dengan baik) {/i}"
                                b "{i} (i \ 'll berpura -pura saya mengambil sesuatu) {/i}"
                                b "Done"
                                scene toi_d_m15 with dissolve
                                if mrel >=250:
                                    m "Tunggu sebentar"
                                    scene toi_d_m5 with fade
                                    "..."
                                    m "Tetap, saya ingin menunjukkan sesuatu"
                                    scene toi_d_m16 with fade
                                    m "Hanya sedetik"
                                    b "{i}(Wow){/i}"
                                    scene toi_d_m17 with dissolve
                                    m "Bagaimana menurutmu?"
                                    b "Hmm"
                                    menu:
                                        "Tampak hebat":
                                            m "Thank you"
                                            scene toi_d_m18 with dissolve
                                            m "Senang Anda menyukainya"
                                            m "Anda bisa pergi sekarang"
                                            b "Ok"
                                            scene room3 with fade
                                            "..."
                                            call screen gnav
                                        "Bagus tapi ... lebih baik tanpanya":


                                            m "Tapi apa?"
                                            b "Lebih baik tanpa itu"
                                            $ mrel -= 1
                                            show screen mreldw
                                            m "Please leave"
                                            hide screen mreldw
                                            b "Ok"
                                            scene room3 with fade
                                            b "{i} (sialan aku kacau) {/i}"
                                            call screen gnav
                                else:

                                    m "Anda bisa pergi sekarang"
                                    b "Ok sorry"
                                    scene room3 with fade
                                    "..."
                                    call screen gnav
                            else:
                                scene toi_d_m12 with dissolve
                                m "[bname] Apa yang Anda inginkan?"
                                b "Err"
                                b "Saya lupa sesuatu"
                                m "Keluar!"
                                b "Ok sorry"
                                m "Saya selalu mengunci pintu"
                                scene room3 with fade
                                "..."
                                call screen gnav
                        "Meninggalkan":

                            call screen gnav
                "Tidak apa-apa":

                    m "Saya akan kembali lagi nanti"
                    b "Saya hampir selesai"
                    scene toi_d_m3 with dissolve
                    b "I'll go"
                    if mpracticegift >=1 and mrel>= 120 and mcorr >= 3:
                        m "No stay"
                        m "Saya membutuhkan Anda untuk membantu saya dengan sesuatu"
                        b "Apa itu?"
                        m "Come here"
                        scene toi_d_m4 with dissolve
                        m "Beri aku satu menit"
                        m "Saya perlu menghapus jubahnya"
                        scene toi_d_m5 with dissolve
                        "..."
                        scene toi_d_m6 with dissolve
                        m "Saya ingin Anda membantu saya memilih sesuatu"
                        b "Ok"
                        scene toi_d_m7 with fade
                        m "Mereka meminta saya untuk memakai ini di tempat kerja"
                        m "Apa yang kamu katakan?"
                        b "Tentang apa?"
                        m "..."
                        scene toi_d_m8 with dissolve
                        m "{i} (oh my god, apa yang saya lakukan?) {/i}"
                        m "{i} (i \ 'D lebih baik ubah subjek) {/i}"
                        m "Apakah Anda suka warnanya?"
                        b "{i} (Saya harus bermain aman di sini) {/i}"
                        scene toi_d_m9 with dissolve
                        menu:
                            "Ya itu bagus":
                                b "Ya, bagus"
                                $ mrel += 1
                                m "Menurutmu begitu?"
                                show screen mrelup
                                b "Positive"
                                hide screen mrelup
                                m "Ok terima kasih, itu saja"
                                m "Anda bisa pergi sekarang, saya perlu melakukan kuku saya"
                                scene room3 with fade
                                "..."
                                call screen gnav
                            "Mungkin Anda harus bertanya [sname]":




                                b "{i} (...) {/i}"
                                b "Mungkin Anda harus bertanya [sname]"
                                $ mrel -= 1
                                b "Dia tahu lebih baik tentang hal -hal gadis ini"
                                scene toi_d_m10 with dissolve
                                show screen mreldw
                                m "..."
                                hide screen mreldw
                                m "Ok terima kasih, itu saja"
                                m "Anda bisa pergi sekarang, saya perlu melakukan kuku saya"
                                scene room3 with fade
                                "..."
                                call screen gnav
                    else:


                        pass
                    m "Tidak perlu saya pergi"
                    scene toi_d_b with fade
                    b "{i}(She left){/i}"
                    call screen gnav
        else:
            if instadone == 2 and rkiss >=1 and hidetoiletrowena ==0:
                $ Hour += 1
                scene toi_d with fade
                b "{i} (hmm tidak ada di sini) {/i}"
                b "{i} (Let \ 'S Empty the Tank) {/i}"
                scene toi_d_b with fade
                "..."
                play sound "sounds/door_openc.wav"
                a "Oops sorry"
                stop sound
                scene toi_rw with dissolve
                b "Oh Hi"
                a "Wow!"
                a "Anda berbalik begitu cepat"
                b "Hehe sorry"
                a "Pokoknya aku keluar"
                $ hidetoiletrowena = 1
                a "Saya ingin menggunakan toilet"
                b "Masuk, aku sudah selesai"
                a "Setidaknya tutupi diri Anda sendiri"
                scene toi_rw1 with dissolve
                "..."
                b "See you"
                scene room3 with fade
                show screen opnotif
                "..."
                hide screen opnotif
                "..."
                call screen gnav

            elif hidetoiletrowena ==1:
                $ Hour += 1
                scene toi_d with fade
                b "{i} (hmm ...) {/i}"
                menu:
                    "Sembunyikan dan Tunggu Rowena":
                        scene toi_rw2 with dissolve
                        b "{i} (itu adalah tempat yang bagus) {/i}"
                        scene toi_rw3 with fade
                        play sound "sounds/door_openc.wav"
                        b "{i} (ini dia datang) {/i}"
                        stop sound
                        b "{i} (i \ 'll tunggu sebentar lalu aku akan melompat dan menakut -nakuti dia) {/i}"
                        scene toi_rw4 with dissolve
                        b "{i} (huh!) {/i}"
                        scene toi_rw5 with dissolve
                        b "Hai! Apa yang sedang kamu lakukan?!"
                        scene toi_rw6 with vpunch
                        a "Berbuat salah! Tidak ada"
                        b "Tunjukkan apa yang ada di tanganmu"
                        a "..."
                        scene toi_rw7 with dissolve
                        b "Apa itu?"
                        scene toi_rw8 with dissolve
                        b "Apakah kamu serius?"
                        scene toi_rw6 with dissolve
                        b "Mencuri lipstik?"
                        a "Tolong jangan beri tahu [sname]"
                        b "Tapi kenapa? Maksud saya, Anda kaya dan segalanya"
                        a "Saya tidak bisa membantunya"
                        a "Tolong jangan beri tahu [sname]"
                        b "Saya akan mencoba untuk tidak melakukannya"
                        b "Pergi sekarang sebelum dia datang ke sini"
                        b "{i} (sialan kleptomane) {/i}"
                        $ rowenadp = 1
                        scene room3 with fade
                        "..."
                        call screen gnav
                    "Mengosongkan tangki":


                        b "{i} (Let \ 'S Empty the Tank) {/i}"
                        scene toi_d_b with fade
                        "..."
                        play sound "sounds/door_openc.wav"
                        a "Oops sorry"
                        stop sound
                        scene toi_rw with dissolve
                        b "Oh Hi"
                        a "Wow!"
                        a "Anda berbalik begitu cepat"
                        b "Hehe sorry"
                        if rowenacall >=2 and rowenamove >2:
                            jump rowenatoilet
                        else:
                            pass
                        a "Pokoknya aku keluar"
                        $ hidetoiletrowena = 1
                        a "Saya ingin menggunakan toilet"
                        b "Masuk, aku sudah selesai"
                        a "Setidaknya tutupi diri Anda sendiri"
                        scene toi_rw1 with dissolve
                        "..."
                        b "See you"
                        scene room3 with fade
                        "..."
                        call screen gnav
            else:


                pass
            scene toi_d with fade
            b "{i} (tidak ada orang di sini) {/i}"
            b "{i} (...) {/i}"
            call screen gnav




    elif Hour ==16:
        $ Hour += 1
        scene room3 with fade
        b "Hah!"
        b "Siapa \ 'yang masuk?"
        s "Itu aku!"
        b "Saya ingin mandi!"
        scene toi_d_s1 with fade
        s "Mengapa setiap kali saya menggunakan toilet!"
        b "Pfff!"
        s "Pergi, kembali setelah satu jam!"
        if cselaine0 == 10 and workrequest ==3 and day !=7:
            $ cselaine0 = 11
            b "Tapi ... aku punya sesuatu untukmu"
            s "Apa itu?"
            b "Aku akan memberimu nanti"
            s "Wait"
            scene toi_d_s3 with dissolve
            s "Saya akan membuka pintu"
            scene toi_d_s4 with fade
            s "Apa itu?"
            b "Saya memiliki tiket bioskop untuk Anda"
            scene toi_d_s5 with dissolve
            s "Ah Ok"
            b "Temui aku di ruang tamu pada pukul 17:00"
            s "Yes ok"
            scene toi_d with fade
            "..."
            call screen gnav
        else:

            if srel >=20:
                scene toi_d_s1a with dissolve
                s "..."
                s "{i} (cabul!) {/i}"
                if toidoorscrew ==0 and workrequest ==3 and day !=7:
                    scene room3 with dissolve
                    $ toidoorscrew = 1
                    b "{i} (Saya berharap saya dapat menemukan cara untuk membuka pintu ini) {/i}"
                    pass
                elif toidoorscrew ==3 and workrequest ==3 and day !=7:
                    scene room3 with dissolve
                    b "{i} (mari coba dengan obeng) {/i}"
                    "..."
                    b "{i}(Cool){/i}"
                    jump toidoorscewed
                else:

                    pass
            else:
                scene toi_d_s1a with dissolve
                s "..."
                pass

        b "..."
        scene room3 with fade
        b "{i} (i \ 'll pergi, persetan!) {/i}"
        call screen gnav

    elif Hour ==17:
        if elaineshowsup ==1 and day ==6:
            $ Hour += 1
            scene toi_d_e with fade
            e "Yes [bname]"
            b "Saya ingin menggunakan toilet"
            e "Lalu lakukan"
            b "Ok"
            scene toi_d_b with dissolve
            "..."
            s "Hah!"
            scene toi_d_b3 with dissolve
            s "..."
            scene toi_d_b12 with dissolve
            s "Apa ini [bname]!?"
            b "Ayo, aku hanya kencing"
            s "Dengan seseorang di kamar mandi?"
            e "Tidak apa -apa sayang"
            e "Tenang, itu normal"
            show screen sreldw
            $ srel -= 1
            scene toi_d_b11a with dissolve
            b "Hah!"
            hide screen sreldw
            e "Jangan khawatir tentang hal itu, dia akan baik -baik saja"
            scene toi_d with fade
            "..."
            call screen gnav

        elif elaineagain ==2 and day ==6:
            $ Hour += 1
            scene toi_d_e with fade
            e "Yes [bname]"
            b "Saya ingin menggunakan toilet"
            e "Lalu lakukan"
            b "Ok"
            scene toi_d_b with dissolve
            "..."
            s "Hah!"
            scene toi_d_b3 with dissolve
            s "..."
            scene toi_d_b12 with dissolve
            s "Apa ini [bname]!?"
            b "Ayo, aku hanya kencing"
            s "Dengan seseorang di kamar mandi?"
            e "Tidak apa -apa sayang"
            e "Tenang, itu normal"
            show screen sreldw
            $ srel -= 1
            scene toi_d_b11a with dissolve
            b "Hah!"
            hide screen sreldw
            e "Jangan khawatir tentang hal itu, dia akan baik -baik saja"
            scene toi_d with fade
            "..."
            call screen gnav
        else:


            pass
        scene toi_d with fade
        b "Hmm"
        menu:
            "Mandi dengan pintu tidak terkunci":
                $ Hour += 1
                scene toi_d_b1 with fade
                b "{i}(Nice){/i}"
                scene toi_d_b2 with fade
                "..."
                scene toi_d_b3 with hpunch
                s "Ups!"
                scene toi_d_b4 with dissolve
                b "Hai!"
                if persistent.patch_enabled:
                    b "Saya akan memberi tahu ibu"
                    pass
                else:
                    b "Saya akan memberi tahu [mname]"
                    pass
                if sdom >=20:
                    s "Please don't"
                    scene toi_d_b4a with dissolve
                    "..."
                    menu:
                        "Saya menang":
                            b "I won't"
                            s "Thank you"
                            s "I'm leaving"
                            $ sdom += 1
                            show screen sdomup
                            b "Hmmm"
                            hide screen sdomup
                            "..."
                            scene toi_d with fade
                            "..."
                            call screen gnav
                        "Dengan baik...":

                            b "Tolong berikan sikat gigi saya"
                            scene toi_d_b3a with dissolve
                            s "Ah.."
                            s "Yeah sure"
                            "Di mana Anda meletakkan sikat gigi"
                            menu:
                                "Ke atas":
                                    scene toi_d_b10a with dissolve
                                    "..."
                                    scene toi_d_b12a with dissolve
                                    b "Hmm"
                                    pass
                                "Turun":

                                    scene toi_d_b13a with fade
                                    "..."
                                    scene toi_d_b14a with dissolve
                                    b "Hmm"

                            scene toi_d_b5a with fade
                            "..."
                            b "Thanks"
                            s "Ok ... aku ..."
                            s "I'm leaving"
                            $ sdom += 1
                            show screen sdomup
                            b "Hmmm"
                            hide screen sdomup
                            "..."
                            menu:
                                "Terima kasih":
                                    $ srel += 1
                                    b "Thank you"
                                    pass
                                "Bisakah kamu...":

                                    b "Bisakah kamu..."
                                    s "Bisakah saya apa?"
                                    b "Bisakah Anda membantu saya dengan ini?"
                                    s "Dan bagaimana Anda ingin saya membantu?"
                                    b "Berlutut untuk starter"
                                    if srel >=500:
                                        scene toi_d_b6a with dissolve
                                        s "Hmm"
                                        s "Saya bisa [bname]"
                                        b "Ok tidak perlu berlutut"
                                        b "Bantuan akan dilakukan"
                                        s "Ok"
                                        scene toi_d_b8a with vpunch
                                        b "Aduh!"
                                        s "{i}(Hehehe){/i}"
                                        b "Tidak seperti itu"
                                        b "Berhenti! Cukup"
                                        $ shj = 1
                                        scene toi_d_b6ak with dissolve
                                        s "Mhmmm"
                                        scene toi_d_b9ak with dissolve
                                        b "..."
                                        scene toi_d_b6akc with dissolve
                                        b "Ahhh!"
                                        scene toi_d_b9a with fade
                                        s "Sorry"
                                        b "No probs"
                                        b "Terima kasih telah membantu"
                                        pass

                                    elif sbm ==1 and srel >=150:
                                        scene toi_d_b6a with dissolve
                                        s "Hmm"
                                        s "Saya bisa [bname]"
                                        b "Ok tidak perlu berlutut"
                                        b "Bantuan akan dilakukan"
                                        s "Ok"
                                        scene toi_d_b8a with vpunch
                                        b "Aduh!"
                                        s "{i}(Hehehe){/i}"
                                        b "Tidak seperti itu"
                                        b "Berhenti! Cukup"
                                        $ shj = 1
                                        scene toi_d_b6ak with dissolve
                                        s "Mhmmm"
                                        scene toi_d_b9ak with dissolve
                                        b "..."
                                        scene toi_d_b6akc with dissolve
                                        b "Ahhh!"
                                        scene toi_d_b9a with fade
                                        s "Sorry"
                                        b "No probs"
                                        b "Terima kasih telah membantu"
                                        pass

                                    elif sbm ==2:
                                        scene toi_d_b6a with dissolve
                                        s "Hmm"
                                        scene toi_d_b6b with dissolve
                                        s "Pergi bercinta diri sendiri"
                                        pass

                                    elif b_fightback == 2:
                                        scene toi_d_b6a with dissolve
                                        s "Hmm"
                                        s "Saya bisa [bname]"
                                        b "Ok tidak perlu berlutut"
                                        b "Bantuan akan dilakukan"
                                        s "Ok"
                                        scene toi_d_b8a with vpunch
                                        b "Aduh!"
                                        s "{i}(Hehehe){/i}"
                                        b "Tidak seperti itu"
                                        b "Berhenti! Cukup"
                                        s "Hehehe tidak!"
                                        b "Come here"
                                        scene toi_d_b15a with hpunch
                                        b "Beri aku ciuman!"
                                        scene toi_d_b16a with dissolve
                                        "..."
                                        $ shj = 1
                                        scene toi_d_b9a with fade
                                        s "Aku akan pergi sekarang"
                                        b "Terima kasih telah membantu"
                                        pass
                                    else:

                                        scene toi_d_b6a with dissolve
                                        s "Hmm"
                                        scene toi_d_b6b with dissolve
                                        s "Pergi bercinta diri sendiri"
                                        pass


                            scene toi_d with fade
                            "..."
                            call screen gnav
                else:

                    pass
                s "Maaf maaf, pintunya tidak terkunci"
                s "Aku keluar!"
                $ sdom += 1
                scene toi_d_b5 with dissolve
                show screen sdomup
                b "Hmmm"
                hide screen sdomup
                "..."
                scene toi_d with fade
                "..."
                call screen gnav
            "Mandi":

                "..."
                $ Hour += 1
                scene toi_d_b1 with fade
                b "{i}(Nice){/i}"
                scene toi_d_b2 with fade
                "..."
                scene toi_d with fade
                "..."
                call screen gnav

    elif Hour >=18 and Hour <20:
        scene toi_n with fade
        b "{i} (tidak ada orang di sini) {/i}"
        b "{i} (dan saya tidak ingin menggunakan toilet sekarang) {/i}"
        call screen gnav

    elif Hour ==20:
        "..."
        $ Hour += 1
        scene room3 with fade
        "..."
        scene room3 with vpunch
        m "Hai!"
        b "{i}(Shit){/i}"
        if mrel >=5 and mrel <=20:
            scene toi_m_n2 with dissolve
            m "Apakah Anda mencoba memecahkannya?"
            b "Maaf!"
            b "Saya tidak tahu"
            pass
        elif mrel >20:
            scene toi_m_n2a with dissolve
            m "Apakah Anda mencoba memecahkannya?"
            b "Maaf!"
            b "Saya tidak tahu"
            pass
        "..."
        menu:
            "Saya minta maaf tetapi saya benar -benar perlu menggunakan toilet":
                if mrel >=5 and mrel <=20:
                    m "Ok masuk!"
                    scene toi_m_n3 with fade
                    m "Tolong buat cepat"
                    b "Sure"
                    scene toi_m_n4 with dissolve
                    "..."
                    scene toi_m_n5 with fade
                    b "Done"
                    m "Terima kasih, sekarang tolong keluar"
                    b "Sure"
                    scene toi_m_n6 with fade
                    "..."
                    scene room3 with fade
                    "..."
                    call screen gnav

                elif mrel >20:
                    m "Ok masuk!"
                    scene toi_m_n3a with fade
                    m "Tolong buat cepat"
                    b "Sure"
                    scene toi_m_n4 with dissolve
                    "..."
                    scene toi_m_n5a with fade
                    b "Done"
                    m "Terima kasih, sekarang tolong keluar"
                    b "Sure"
                    scene toi_m_n6a with fade
                    "..."
                    if elaine_convince == 4 and mrel>= 50:
                        m "[bname]!"
                        m "Masih di sana?"
                        b "Yes"
                        b "Apa itu?"
                        m "Kembali"
                        scene toi_m_n7 with fade
                        m "Wait here"
                        m "Aku akan kembali"
                        jump mtoi_practice
                    else:

                        pass
                    scene room3 with fade
                    "..."
                    call screen gnav
                else:

                    m "TIDAK!"
                    m "Anda menunggu sampai saya selesai"
                    b "Ok"
                    scene room3 with fade
                    "Anda memiliki poin hubungan yang rendah"
                    call screen gnav
            "Meninggalkan":

                scene room3 with fade
                "..."
                call screen gnav

    elif Hour >=21:
        scene toi_n with fade
        b "{i} (tidak ada orang di sini) {/i}"
        b "{i} (Saya harus tidur) {/i}"
        jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc