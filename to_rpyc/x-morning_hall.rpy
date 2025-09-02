label morning_hall:
    if wrokmelindrp >=5 and mrob ==0:
        $ Hour += 2
        scene callelaine0 with fade
        play sound "sounds/mobilering.wav"
        b "{i} huh! Apa yang dia inginkan? {/i}"
        scene callelaine with dissolve
        c "Hi [bname]"
        b "Hi"
        c "Kemana saja kamu selama ini?"
        b "Seperti biasa, di rumah"
        c "Saya mendengar bahwa Anda melihat Melinda"
        b "Yes sometimes"
        c "Bisakah kamu datang hari ini?"
        b "Hari ini?"
        c "Ya saya perlu melihat Anda"
        c "Datang dan sarapan dengan saya, saya tidak akan membuat Anda terlambat"
        b "Hmm, oke"
        scene vch00 with fade
        "..."
        scene vch0 with dissolve
        m "..."
        scene vch1 with dissolve
        "..."
        scene vch with fade
        play sound "sounds/doorbell1.wav"
        c "Masuk, di sini di dapur"
        stop sound
        scene vch2 with fade
        c "Senang bertemu denganmu"
        b "{i}(Yeah right){/i}"
        b "Kamu juga"
        scene vch3 with dissolve
        c "Jadi bagaimana pekerjaan dengan Melinda?"
        b "Ini baik -baik saja, saya jarang pergi"
        c "Ayo [bname] Saya tahu segalanya"
        scene black
        "SEMENTARA ITU"
        scene vch4 with fade
        $ persistent.unlock_71 = True
        m "Saya membutuhkan bantuan Anda Elaine"
        e "Apa yang salah begitu awal?"
        m "Dimana Rob?"
        e "Di sini kenapa?"
        m "Bolehkah saya meminta bantuannya?"
        e "Rob, tolong datang"
        scene vch5 with dissolve
        r "Apa itu?"
        scene vch6 with dissolve
        m "Saya ingin Anda pergi ke alamat ini"
        r "Untuk apa?"
        m "Saya curiga tentang sesuatu dan saya perlu mengkonfirmasi keraguan saya"
        m "Bisakah Anda melakukannya untuk saya?"
        r "Sekarang?"
        m "Ya jika Anda tidak keberatan"
        scene vch7 with dissolve
        e "[mname] Katakan padaku apa masalahnya"
        e "Saat Rob bersiap"
        scene black
        "SEMENTARA ITU"
        scene dach
        "..."
        c "Ahh"
        scene vch9 with dissolve
        c "Ahh"
        scene dach
        "..."
        c "Ah yes"
        scene dach
        "..."
        scene vch8 with dissolve
        r "Hah!"
        r "{i} (intuisi wanita tidak pernah salah) {/i}"
        $ mrob = 1
        scene black
        "..."
        scene vch10 with fade
        r "Dimana [mname]?"
        e "Dia berangkat kerja"
        e "Apa yang Anda temukan?"
        scene vch11 with fade
        c "Terima kasih telah mengunjungi saya [bname]"
        b "Sampai jumpa"
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav


    elif workrequest ==3 and Hour==9 and day !=7:
        jump jenmorning
    else:
        pass
    scene hall_d with fade
    b "{i} (...) {/i}"
    if ticketrequested == 4 and Hour>=10 and elainefuck == 1:
        jump snamecon_efuck
    else:
        pass
    b "{i} (mungkin saya bisa ...) {/i}"
    menu:
        "Tonton TV" if tvwatched <1:
            "..."
            $ tvwatched += 1
            $ Hour += 1
            if day ==7:
                scene b_tv_d with fade
                "..."
                if workrequest ==3 and mrel >=200 and elaine_convince == 4:
                    scene b_tv_d2wa with dissolve
                    m "Selamat pagi sayang"
                    m "Bisakah Anda membantu saya dengan wajan ini?"
                    b "Hah!"
                    scene b_tv_d3wa with dissolve
                    b "Anda membuat saya takut"
                    b "Yeah sure"
                    scene b_tv_d4 with dissolve
                    b "Done"
                    scene b_tv_d5wa with fade
                    show screen mrelup
                    b "{i} (dia berbau mabuk) {/i}"
                    $ mrel += 2
                    hide screen mrelup
                    scene b_tv_d6wa with dissolve
                    menu:
                        "Meninggalkan":
                            b "Errm aku akan pergi sekarang"
                            scene b_tv_d5wa with dissolve
                            "..."
                            scene b_tv_d7wa with dissolve
                            m "Terima kasih"
                            pass
                        "Cium dia":
                            scene b_tv_d5wa with dissolve
                            "..."
                            scene b_tv_d6w with dissolve
                            m "Apa?"
                            scene b_tv_d7w with dissolve
                            m "..."
                            scene b_tv_d8w with dissolve
                            "..."
                            scene b_tv_d7wa with dissolve
                            m "Terima kasih"
                            b "{i} (mungkin saya bisa mencoba) {/i}"
                            menu:
                                "Lakukan itu":
                                    scene b_tv_d9w with dissolve
                                    m "..."
                                    scene b_tv_d10w with dissolve
                                    m "Apa yang sedang kamu lakukan?"
                                    b "..."
                                    m "Dapatkan aku minuman"
                                    scene b_tv_d11w with fade
                                    m "Mengapa Anda tidak memilikinya?"
                                    b "Too early"
                                    m "Ayo!"
                                    scene b_tv_d12w with dissolve
                                    m "Saya tahu apa yang akan membuat Anda minum"
                                    menu:
                                        "Saya tidak akan minum" if mmorningrepeat >=1 and mrel >=300:
                                            scene b_tv_d15w with fade
                                            b "Oh wow"
                                            scene b_tv_d16w with dissolve
                                            "..."
                                            scene b_tv_d17w with fade
                                            m "Akhirnya Anda diterima untuk minum"
                                            b "Ya masih lebih awal tapi saya melakukannya karena Anda memakai ini"
                                            m "Hmm"
                                            scene b_tv_d18w with dissolve
                                            m "Anda menyukainya?"
                                            b "A lot"
                                            scene b_tv_d19w with dissolve
                                            m "Lalu ikut denganku"
                                            m "Aku akan menunjukkan lebih banyak"
                                            jump mmorningsex

                                        "Saya tidak akan minum" if mrel >=350:
                                            scene b_tv_d15w with fade
                                            b "Oh wow"
                                            scene b_tv_d16w with dissolve
                                            "..."
                                            scene b_tv_d17w with fade
                                            m "Akhirnya Anda diterima untuk minum"
                                            b "Ya masih lebih awal tapi saya melakukannya karena Anda memakai ini"
                                            m "Hmm"
                                            scene b_tv_d18w with dissolve
                                            m "Anda menyukainya?"
                                            b "A lot"
                                            scene b_tv_d19w with dissolve
                                            m "Lalu ikut denganku"
                                            m "Aku akan menunjukkan lebih banyak"
                                            jump mmorningsex
                                        "Tidak mengatakan apa -apa":

                                            scene b_tv_d13w with fade
                                            b "Huh"
                                            $ mmorningrepeat += 1
                                            scene b_tv_d14w with fade
                                            m "Anda masih ingin minum?"
                                            b "No"
                                            m "Cheers"
                                            m "Saya tidak peduli"
                                            m "Aku akan sampai jumpa nanti"
                                            scene hall_d with fade
                                            b "{i} (...) {/i}"
                                            call screen gnav
                                "Jangan":
                                    pass



                elif workrequest ==3:
                    scene b_tv_d2w with dissolve
                    m "Selamat pagi sayang"
                    m "Bisakah Anda membantu saya dengan wajan ini?"
                    b "Hah!"
                    scene b_tv_d3w with dissolve
                    b "Anda membuat saya takut"
                    b "Yeah sure"
                    scene b_tv_d4 with dissolve
                    b "Done"
                    scene b_tv_d5w with fade
                    show screen mrelup
                    m "Terima kasih"
                    $ mrel += 2
                    hide screen mrelup

                    b "Errm aku akan pergi sekarang"
                    pass
                else:

                    scene b_tv_d3 with dissolve
                    m "[bname] Bisakah Anda membantu saya?"
                    b "Dengan apa?"
                    scene b_tv_d2 with dissolve
                    m "Dengan panci?"
                    b "Yeah sure"
                    scene b_tv_d4 with dissolve
                    b "Done"
                    scene b_tv_d5 with dissolve
                    show screen mrelup
                    m "Terima kasih"
                    $ mrel += 2
                    hide screen mrelup
                    b "Errm aku akan pergi sekarang"
                    pass

            elif day ==2:
                if workrequest ==3 and Hour>=10:
                    jump halltv_morning
                else:
                    pass
                scene b_tv_d with fade
                "..."
                scene b_tv_d6 with dissolve
                m "[bname] Bisakah Anda mendapatkan saya susu?"
                b "Yes sure"
                scene b_tv_d7 with dissolve
                menu:
                    "Lakukan beberapa gerakan juggling dengan botol":
                        scene b_tv_d9 with hpunch
                        b "Tada!"
                        m "[bname] Apa yang kamu lakukan? !!"
                        scene b_tv_d10 with dissolve
                        b "Ohh F ...!"
                        scene b_tv_d11 with hpunch
                        m "Keluar!"
                        b "Ok Ok"
                        scene b_tv_d11pov with dissolve
                        m "{i} (dia tidak akan pernah tumbuh dewasa) {/i}"
                        pass
                    "Letakkan di atas meja":


                        b "Ini dia"
                        m "Letakkan saja di sana"
                        scene b_tv_d8 with dissolve
                        "..."
                        pass

            elif day ==4:
                if workrequest ==3 and Hour>=10:
                    jump halltv_morning
                else:
                    pass
                scene b_tv_d with fade
                "..."
                scene b_tv_d6 with dissolve
                m "[bname] Bisakah Anda mendapatkan saya susu?"
                b "Yes sure"
                scene b_tv_d7 with dissolve
                menu:
                    "Lakukan beberapa gerakan juggling dengan botol":
                        scene b_tv_d9 with hpunch
                        b "Tada!"
                        m "[bname] Apa yang kamu lakukan? !!"
                        scene b_tv_d10 with dissolve
                        b "Ohh F ...!"
                        scene b_tv_d12 with hpunch
                        m "Keluar!"
                        pass
                    "Letakkan di atas meja":


                        b "Ini dia"
                        m "Letakkan saja di sana"
                        scene b_tv_d8 with dissolve
                        "..."
                        pass

            elif day==6:
                if workrequest ==3 and Hour>=10:
                    jump halltv_morning
                else:
                    pass
                scene b_tv_d with fade
                "..."
                scene b_tv_d3 with dissolve
                m "[bname] Bisakah Anda membantu saya?"
                b "Dengan apa?"
                scene b_tv_d2 with dissolve
                m "Dengan panci?"
                b "Yeah sure"
                scene b_tv_d4 with dissolve
                b "Done"
                if mrel >=36:
                    scene b_tv_d5a with dissolve
                    m "Anda pantas mendapatkan pelukan"
                    b "..."
                    menu:
                        "Cobalah bergerak":
                            scene b_tv_d8a with dissolve
                            m "Hah!"
                            scene b_tv_d9a with dissolve
                            m "{i} (dia tidak tahu apa yang baru saja dia lakukan) {/i}"
                            m "{i} (masih naif seperti biasa) {/i}"
                            if mrel >=50:
                                scene b_tv_d6a with dissolve
                                m "Anda perlu berolahraga lebih banyak [bname]"
                                b "Hah!"
                                b "Saya melakukannya"
                                m "Lihatlah perut Anda!"
                                scene b_tv_d7a with dissolve
                                b "Ini tidak besar"
                                scene b_tv_d10a with dissolve
                                m "Dan apa bola ini di sini"
                                b "{i} (apakah Anda harus menyebutkan bola sambil menyentuh perut saya) {/i}"
                                b "{i} (Saya harap dia tidak memperhatikan tonjolan) {/i}"
                                pass
                            else:
                                scene b_tv_d6a with dissolve
                                m "Anda perlu berolahraga lebih banyak [bname]"
                                b "Hah!"
                                b "Saya melakukannya"
                                m "Lihatlah perut Anda!"
                                scene b_tv_d7a with dissolve
                                b "Yeah"
                                scene b_tv_d5a with dissolve
                                pass
                        "Jangan":

                            scene b_tv_d6a with dissolve
                            m "Anda perlu berolahraga lebih banyak [bname]"
                            b "Hah!"
                            b "Saya melakukannya"
                            m "Lihatlah perut Anda!"
                            scene b_tv_d7a with dissolve
                            b "Yeah"
                            scene b_tv_d5a with dissolve
                            pass
                else:

                    scene b_tv_d5 with dissolve
                    pass

                show screen mrelup
                m "Pokoknya terima kasih telah membantu saya"
                $ mrel += 1
                hide screen mrelup
                b "Aku akan pergi sekarang"
                pass

            elif day ==3:
                if workrequest ==3 and Hour>=10:
                    jump halltv_morning
                else:
                    pass
                scene b_tv_d with fade
                "..."
                scene b_tv_d3 with dissolve
                m "[bname] Bisakah Anda membantu saya?"
                b "Dengan apa?"
                scene b_tv_d2 with dissolve
                m "Dengan panci?"
                b "Yeah sure"
                scene b_tv_d4 with dissolve
                b "Done"
                scene b_tv_d5 with dissolve
                show screen mrelup
                m "Terima kasih"
                $ mrel += 1
                hide screen mrelup
                b "Errm aku akan pergi sekarang"
                pass
            else:

                if workrequest ==3 and Hour==9:
                    jump jenmorning
                else:
                    if workrequest ==3 and Hour>=10:
                        jump halltv_morning
                    else:
                        pass
                scene b_tv_d with fade
                "..."
                scene b_tv_d1 with dissolve
                b "{i}(Boring){/i}"
                b "{i} (i \ 'd cuti lebih baik) {/i}"
                pass
        "Santai":




            $ Hour += 1
            scene b_relax_d with fade
            if day ==7:
                if beachalone == 3:
                    m "[bname] !!"
                    scene b_relax_d1 with hpunch
                    m "Apakah Anda menyelesaikan pekerjaan rumah Anda?"
                    b "Ini hari Minggu!"
                    m "Saya tidak ingin orang malas di rumah saya"
                    m "Bangunlah anak muda !!"
                    b "Yeah whatever"
                    b "Mari kita pergi ke pantai"
                    scene b_relax_d2a with dissolve
                    m "Panggil [sname]"
                    if mvisitnudebeach >=4:
                        b "Hmm"
                        menu:
                            "Panggil [sname]":
                                jump beachevent
                            "Jangan":
                                pass
                    b "Dia tidak datang"
                    b "Dia keluar dengan Rowena"
                    m "Apa?"
                    b "Ya mereka pergi ke mal"
                    scene b_relax_d3a with dissolve
                    m "Oke, siaplah diri Anda"
                    if mvisitnudebeach >=2:
                        e "Hey guys"
                        m "Hah!"
                        scene b_relax_d4a with dissolve
                        e "Selamat pagi, apa rencananya untuk hari ini?"
                        b "{i} (keren! Elaine dapat membantu) {/i}"
                        b "Kami pergi ke pantai"
                        m "Tapi sekarang setelah Anda di sini kami tidak akan melakukannya"
                        b "Oh kenapa?!"
                        scene b_relax_d5a with dissolve
                        m "Karena saya tidak ingin pergi ke tempat itu"
                        m "Apalagi dengan Elaine"
                        scene b_relax_d3a with dissolve
                        e "Kenapa, apa hubungannya denganku?"
                        b "Karena itu pantai telanjang itu"
                        e "Ahh"
                        e "Ayo [mname] Aku akan berperilaku aku janji"
                        m "Yeah right"
                        scene b_relax_d6a with dissolve
                        e "Itu ya, pergi bersiap -siap [bname]"
                        $ beachalone = 1
                        jump nudebeach_jenelaine
                    else:
                        $ beachalone = 1
                        jump nudebeach_jenny
                else:
                    pass
                "..."
                m "[bname] !!"
                scene b_relax_d1 with hpunch
                b "Ya!"
                m "Apakah Anda menyelesaikan pekerjaan rumah Anda?"
                scene b_relax_d2 with dissolve
                b "Ini hari Minggu!"
                m "Saya tidak ingin orang malas di rumah saya"
                m "Bangunlah anak muda !!"
                b "Yeah whatever"
                if beachdone == 0:
                    pass
                else:
                    jump sundayrelax

                scene b_relax_d3 with dissolve
                s "Bisakah kita pergi ke pantai?"
                if mny >=500:
                    pass
                else:
                    pass
                m "Kami tidak punya uang untuk itu"
                if wk >= 1:
                    menu:
                        "Mengapa tidak?":
                            b "Maksud saya, kita bisa berjalan -jalan"
                            b "Tidak perlu uang"
                            if mrel >20:
                                scene b_relax_d5 with dissolve
                                m "Hmmmm ok, bersiaplah"
                                $ beachdone = 1
                                scene b_relax_d6 with dissolve
                                s "Keren, bisakah saya meletakkan bikini saya?"
                                m "Ya kita bisa berenang, kenapa tidak"
                                if beach ==0:
                                    scene b_relax_d7 with fade
                                    $ beach += 1
                                    s "Tempat yang bagus"
                                    scene b_relax_d8 with dissolve
                                    b "Indeed"
                                    scene b_relax_d9 with dissolve
                                    "..."
                                    scene black with fade
                                    "..."
                                    scene b_relax_d10 with fade
                                    m "Saya kira itu cukup untuk hari ini"
                                    m "Let's go"
                                    scene b_relax_d11 with fade
                                    "..."
                                    scene hall_d with fade
                                    b "{i} (...) {/i}"
                                    call screen gnav

                                elif beach >=1 and cellshop == 1:
                                    if workrequest ==3:
                                        menu:
                                            "Mungkin kita bisa mengundang Elaine dengan kita?" if beachelainedone == 0:
                                                scene b_relax_d5 with dissolve
                                                m "Hmm"
                                                $ beachelainedone = 1
                                                jump beachevent_elaine

                                            "Mungkin kita bisa mengundang Rowena?" if rdf == 1 and beachrowenadone == 0:
                                                scene b_relax_d5 with dissolve
                                                m "Hmm"
                                                $ beachrowenadone = 1
                                                jump beachevent_rowena

                                            "*Mungkin saya harus mencoba pergi dengan [mname] sendiri kali ini*" if startnework ==1 and beachalone ==0 and mrel >=150:
                                                $ beachalone = 1
                                                b "{i} (sialan, [sname] tidak akan menerima i \ 'm yakin) {/i}"
                                                b "{i} (Saya perlu memikirkan cara untuk membuatnya tetap di sini) {/i}"
                                                b "{i} (Saya mengerti, mungkin voucher belanja ?!) {/i}"
                                                jump beachevent

                                            "[mname] memutuskan untuk membawa seseorang" if mbvisit >= 1:
                                                jump beach_withcoworker
                                            "Tidak mengatakan apa -apa":


                                                jump beachevent
                                    else:
                                        pass

                                    scene b_relax_d7 with fade
                                    "..."
                                    scene b_relax_d8 with dissolve
                                    "..."
                                    scene b_relax_d9 with dissolve
                                    "..."
                                    scene b_relax_d12 with dissolve
                                    s "Saya sangat perlu kecokelatan"
                                    scene black with fade
                                    "..."
                                    scene b_relax_d13 with fade
                                    m "Saya kira itu cukup untuk hari ini"
                                    m "Let's go"
                                    scene b_relax_d11 with fade
                                    "Halo"
                                    b "Hi"
                                    scene b_relax_d14 with dissolve
                                    b "Apa kabarmu?"
                                    if beach == 1:
                                        $ beach += 1
                                    "Terima kasih"
                                    "..."
                                    scene b_relax_d15 with fade
                                    m "Bagaimana Anda mengenalnya [bname]?"
                                    b "Dia adalah pemilik toko telepon"
                                    m "Eh huh!"
                                    "..."
                                    scene hall_d with fade
                                    b "{i} (...) {/i}"
                                    call screen gnav
                                else:

                                    if workrequest ==3:
                                        menu:
                                            "Mungkin kita bisa mengundang Elaine dengan kita?" if beachelainedone == 0:
                                                scene b_relax_d5 with dissolve
                                                m "Hmm"
                                                $ beachelainedone = 1
                                                jump beachevent_elaine

                                            "Mungkin kita bisa mengundang Rowena?" if rdf == 1 and beachrowenadone == 0:
                                                scene b_relax_d5 with dissolve
                                                m "Hmm"
                                                $ beachrowenadone = 1
                                                jump beachevent_rowena


                                            "*Mungkin saya harus mencoba pergi dengan [mname] sendiri kali ini*" if startnework ==1 and beachalone ==0 and mrel >=150:
                                                $ beachalone = 1
                                                b "{i} (sialan, [sname] tidak akan menerima i \ 'm yakin) {/i}"
                                                b "{i} (Saya perlu memikirkan cara untuk membuatnya tetap di sini) {/i}"
                                                b "{i} (mungkin membeli kartu belanja?) {/i}"
                                                jump beachevent
                                            "Tidak mengatakan apa -apa":


                                                jump beachevent
                                    else:

                                        pass
                                    scene b_relax_d8 with dissolve
                                    "..."
                                    scene b_relax_d9 with dissolve
                                    "..."
                                    scene b_relax_d12 with dissolve
                                    s "Saya sangat perlu kecokelatan"
                                    scene black with fade
                                    "..."
                                    scene b_relax_d13 with fade
                                    m "Saya kira itu cukup untuk hari ini"
                                    m "Let's go"
                                    scene b_relax_d11 with fade
                                    "..."
                                    scene hall_d with fade
                                    b "{i} (...) {/i}"
                                    call screen gnav
                            else:

                                scene b_relax_d5r with dissolve
                                m "TIDAK!"
                                b "{i} (oh sialan!) {/i}"
                                scene black
                                "Anda membutuhkan 20 [mname] poin"
                                pass
                        "Diam":


                            scene b_relax_d5r with dissolve
                            m "TIDAK!"
                            b "{i} (oh sialan!) {/i}"
                            b "Aku akan kembali tidur"
                            jump sundayrelax
                else:

                    "..."
                    pass

            elif day ==3:
                if workrequest ==3:
                    jump hallrelax
                else:
                    pass
                "..."
                m "[bname] !!"
                scene b_relax_d1 with hpunch
                b "Ya!"
                m "Apakah Anda menyelesaikan pekerjaan rumah Anda?"
                scene b_relax_d2 with dissolve
                b "Ini hari Minggu!"
                m "Even though"
                m "Saya tidak ingin orang malas di rumah saya"
                m "Bangunlah anak muda !!"
                b "Yeah whatever"
                scene b_relax_d3 with dissolve
                s "Bisakah kita pergi ke pantai?"
                if mny >=500:
                    pass
                else:
                    pass
                m "Kami tidak punya uang untuk itu"
                if wk >= 1:
                    menu:
                        "Mengapa tidak?":
                            b "Maksud saya, kita bisa berjalan -jalan"
                            b "Tidak perlu uang"
                            if mrel >19:
                                scene b_relax_d5 with dissolve
                                m "Hmmmm ok, bersiaplah"
                                scene b_relax_d6 with dissolve
                                s "Keren, bisakah saya meletakkan bikini saya?"
                                m "Ya kita bisa berenang, kenapa tidak"
                                scene black
                                "..."
                                scene b_relax_d7 with fade
                                if beach ==0:
                                    $ beach += 1
                                    s "Tempat yang bagus"
                                    scene b_relax_d8 with dissolve
                                    b "Indeed"
                                    scene b_relax_d9 with dissolve
                                    "..."
                                    scene black with fade
                                    "..."
                                    scene b_relax_d10 with fade
                                    m "Saya kira itu cukup untuk hari ini"
                                    m "Let's go"
                                    scene b_relax_d11 with fade
                                    "..."
                                    scene hall_d with fade
                                    b "{i} (...) {/i}"
                                    call screen gnav

                                elif beach ==1 and cellshop == 1:
                                    "..."
                                    scene b_relax_d8 with dissolve
                                    "..."
                                    scene b_relax_d9 with dissolve
                                    "..."
                                    scene b_relax_d12 with dissolve
                                    s "Saya sangat perlu kecokelatan"
                                    scene black with fade
                                    "..."
                                    scene b_relax_d13 with fade
                                    m "Saya kira itu cukup untuk hari ini"
                                    m "Let's go"
                                    scene b_relax_d11 with fade
                                    "Halo"
                                    b "Hi"
                                    scene b_relax_d14 with dissolve
                                    b "Apa kabarmu?"
                                    $ beach += 1
                                    "Terima kasih"
                                    "..."
                                    scene b_relax_d15 with fade
                                    m "Bagaimana Anda mengenalnya [bname]?"
                                    b "Dia adalah pemilik toko telepon"
                                    m "Eh huh!"
                                    "..."
                                    scene hall_d with fade
                                    b "{i} (...) {/i}"
                                    call screen gnav
                                else:

                                    scene b_relax_d8 with dissolve
                                    "..."
                                    scene b_relax_d9 with dissolve
                                    "..."
                                    scene b_relax_d12 with dissolve
                                    s "Saya sangat perlu kecokelatan"
                                    scene black with fade
                                    "..."
                                    scene b_relax_d13 with fade
                                    m "Saya kira itu cukup untuk hari ini"
                                    m "Let's go"
                                    scene b_relax_d11 with fade
                                    "..."
                                    scene hall_d with fade
                                    b "{i} (...) {/i}"
                                    call screen gnav
                            else:

                                scene b_relax_d5r with dissolve
                                m "TIDAK!"
                                b "{i} (oh sialan!) {/i}"
                                scene black
                                "Anda membutuhkan 20 [mname] poin"
                                pass
                        "Diam":


                            pass
                else:

                    "..."
                    pass






            elif day ==5:
                if workrequest ==3:
                    jump hallrelax
                else:
                    pass
                "..."
                m "[bname] !!"
                scene b_relax_d1 with hpunch
                b "Ya!"
                m "Apakah Anda menyelesaikan pekerjaan rumah Anda?"
                scene b_relax_d2 with dissolve
                b "Ini hari Minggu!"
                m "Even though"
                m "Saya tidak ingin orang malas di rumah saya"
                m "Bangunlah anak muda !!"
                b "Yeah whatever"
                scene b_relax_d3 with dissolve
                s "Bisakah kita pergi ke pantai?"
                if mny >=500:
                    pass
                else:
                    pass
                m "Kami tidak punya uang untuk itu"
                if wk >= 1:
                    menu:
                        "Mengapa tidak?":
                            b "Maksud saya, kita bisa berjalan -jalan"
                            b "Tidak perlu uang"
                            if mrel >20:
                                scene b_relax_d5 with dissolve
                                m "Hmmmm ok, bersiaplah"
                                scene b_relax_d6 with dissolve
                                s "Keren, bisakah saya meletakkan bikini saya?"
                                m "Ya kita bisa berenang, kenapa tidak"
                                scene black
                                "..."
                                scene b_relax_d7 with fade
                                if beach ==0:
                                    $ beach += 1
                                    s "Tempat yang bagus"
                                    scene b_relax_d8 with dissolve
                                    b "Indeed"
                                    scene b_relax_d9 with dissolve
                                    "..."
                                    scene black with fade
                                    "..."
                                    scene b_relax_d10 with fade
                                    m "Saya kira itu cukup untuk hari ini"
                                    m "Let's go"
                                    scene b_relax_d11 with fade
                                    "..."
                                    scene hall_d with fade
                                    b "{i} (...) {/i}"
                                    call screen gnav

                                elif beach ==1 and cellshop == 1:
                                    "..."
                                    scene b_relax_d8 with dissolve
                                    "..."
                                    scene b_relax_d9 with dissolve
                                    "..."
                                    scene b_relax_d12 with dissolve
                                    s "Saya sangat perlu kecokelatan"
                                    scene black with fade
                                    "..."
                                    scene b_relax_d13 with fade
                                    m "Saya kira itu cukup untuk hari ini"
                                    m "Let's go"
                                    scene b_relax_d11 with fade
                                    "Halo"
                                    b "Hi"
                                    scene b_relax_d14 with dissolve
                                    b "Apa kabarmu?"
                                    $ beach += 1
                                    "Terima kasih"
                                    "..."
                                    scene b_relax_d15 with fade
                                    m "Bagaimana Anda mengenalnya [bname]?"
                                    b "Dia adalah pemilik toko telepon"
                                    m "Eh huh!"
                                    "..."
                                    scene hall_d with fade
                                    b "{i} (...) {/i}"
                                    call screen gnav
                                else:

                                    scene b_relax_d8 with dissolve
                                    "..."
                                    scene b_relax_d9 with dissolve
                                    "..."
                                    scene b_relax_d12 with dissolve
                                    s "Saya sangat perlu kecokelatan"
                                    scene black with fade
                                    "..."
                                    scene b_relax_d13 with fade
                                    m "Saya kira itu cukup untuk hari ini"
                                    m "Let's go"
                                    scene b_relax_d11 with fade
                                    "..."
                                    scene hall_d with fade
                                    b "{i} (...) {/i}"
                                    call screen gnav
                            else:

                                scene b_relax_d5r with dissolve
                                m "TIDAK!"
                                b "{i} (oh sialan!) {/i}"
                                scene black
                                "Anda membutuhkan 20 [mname] poin"
                                pass
                        "Diam":


                            pass
                else:

                    "..."
                    pass
            else:






                if workrequest ==3:
                    jump hallrelax
                else:


                    "..."
                    pass



    scene hall_d with fade
    b "{i} (...) {/i}"
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc