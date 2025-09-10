label mroom_menu:
    if Hour >=1 and Hour <12:
        if Hour ==11 and day ==7:
            $ Hour += 1
            jump mroomdiscuss
        elif Hour == 10 and elaineshowsup ==1 and day ==6:
            scene door with fade
            b "{i} (pintu terkunci) {/i}"
            if windowfound ==1:
                b "{i} (mungkin saya bisa memeriksa tangga) {/i}"
                scene mstairs with fade
                "..."
                scene estairs with fade
                b "{i} (dia tidur, tidak ada yang bisa saya lakukan) {/i}"
                b "{i} (i \ 'll kembali ke dalam) {/i}"
                scene hall_d with fade
                "..."
                call screen gnav

        elif Hour == 10 and elaineshowsup ==1 and day ==6:
            scene door with fade
            b "{i} (pintu terkunci) {/i}"
            if windowfound ==1:
                b "{i} (mungkin saya bisa memeriksa tangga) {/i}"
                scene mstairs with fade
                "..."
                scene estairs with fade
                b "{i} (dia tidur, tidak ada yang bisa saya lakukan) {/i}"
                b "{i} (i \ 'll kembali ke dalam) {/i}"
                scene hall_d with fade
                "..."
                call screen gnav
            else:

                scene door with fade
                b "{i} (pintu terkunci) {/i}"
                call screen gnav
        else:

            pass
        scene door with fade
        b "{i} (pintu terkunci) {/i}"
        call screen gnav


    elif Hour ==12:
        if workrequest ==3 and day !=7:
            scene door with fade
            b "{i} (dia tidak ada di sini dan pintunya terkunci) {/i}"
            call screen gnav
        else:
            pass
        $ Hour += 1
        scene door with fade
        b "{i} (sepertinya pintu terbuka) {/i}"
        menu:
            "Memasuki":
                scene mroom_av with hpunch
                m "[bname]! Apa?"
                b "Maaf! Saya ingin menanyakan sesuatu"
                scene mroom_av1 with dissolve
                m "Apa itu?"
                scene mroom_av2 with dissolve
                b "Eh itu ..."
                scene mroom_av3 with dissolve
                m "Bertanya!"
                b "Apakah ada yang bisa saya lakukan untuk membantu?"
                m "Nothing now"
                b "Ok"
                m "Jangan lupa melakukan studi online Anda"
                b "Sure"
                pass
            "Ketukan":

                play sound "sounds/knock.ogg"
                m "Siapa itu?"
                b "It's me"
                m "Enter"
                stop sound
                if mnightie == 2:
                    scene mroom_av8 with fade
                    m "Apa yang salah [bname]?"
                    b "Saya ingin bertanya apakah ada yang bisa saya bantu"
                    m "No"
                    m "Nothing now"
                    b "Ok"
                    b "Aku melihatmu mengenakan gaun ini"
                    b "Saya pikir Anda tidak menyukainya"
                    scene mroom_av9 with dissolve
                    m "Oh tentu saja saya melakukannya"
                    m "Terima kasih"
                    m "Jangan lupa melakukan studi online Anda"
                    b "Sure"
                    pass

                elif mnightie == 1:
                    $ mnightie = 2
                    scene mroom_av4 with fade
                    m "Apa yang salah [bname]?"
                    b "Aku punya sesuatu untukmu"
                    m "Apa itu?"
                    b "Ini, cobalah"
                    m "Ok tolong tunggu di pintu"
                    scene door with fade
                    b "{i} (...) {/i}"
                    m "Anda bisa masuk"
                    scene mroom_av10 with fade
                    m "Jadi?"
                    b "Bagus, tapi saya tidak tahu"
                    b "Apakah kamu menyukainya?"
                    scene mroom_av11 with dissolve
                    show screen mrelup
                    $ mrel += 5
                    m "Ya saya menyukainya"
                    hide screen mrelup
                    m "Tapi aku tidak bisa memakainya"
                    m "Itu menunjukkan dari samping"
                    b "Sisi mana?"
                    scene mroom_av12 with dissolve
                    m "Maksud saya ini sedikit terbuka"
                    b "Ah ok"
                    b "Saya tidak tahu tentang fashion perempuan"
                    scene mroom_av13 with dissolve
                    "..."
                    scene mroom_av12 with fade
                    m "Terima kasih [bname]"
                    b "Ok saya akan pergi sekarang"
                    scene door with fade
                    b "{i} (...) {/i}"
                    call screen gnav
                else:

                    pass
                scene mroom_av4 with fade
                show screen mrelup
                m "Apa yang salah [bname]?"
                $ mrel += 2
                hide screen mrelup
                b "Saya ingin bertanya apakah ada yang bisa saya bantu"
                m "No"
                m "Nothing now"
                b "Ok"
                m "Jangan lupa melakukan studi online Anda"
                b "Sure"
                pass

        scene door with fade
        b "{i} (...) {/i}"
        call screen gnav

    elif Hour >12 and Hour <16:
        scene door with fade
        b "{i} (pintu terkunci) {/i}"
        call screen gnav

    elif Hour ==16:
        if workrequest ==3 and day !=7:
            scene door with fade
            b "{i} (dia tidak ada di sini dan pintunya terkunci) {/i}"
            call screen gnav
        else:
            pass
        $ Hour += 1
        scene door with fade
        b "{i} (sepertinya pintu terbuka) {/i}"
        menu:
            "Memasuki":
                if mrpmt <= 1:
                    scene mroom_pm with hpunch
                    m "[bname]! Apa?"
                    b "Maaf! Saya ingin menanyakan sesuatu"
                    scene mroom_pm1 with dissolve
                    m "Apa itu?"
                    $ mrpmt += 1
                    b "Eh itu ..."
                    m "Bertanya!"
                    b "Apakah ada yang bisa saya lakukan untuk membantu?"
                    m "Nothing now"
                    b "Ok"
                    m "Tolong keluar!"
                    b "Sure"
                    pass
                else:

                    scene door with vpunch
                    b "{i} (fuck it \ 's locked) {/i}"
                    m "APA!"
                    $ findwindow += 1
                    b "Tidak ada, saya ingin ..."
                    m "Please leave"
                    b "{i} (apa -apaan!) {/i}"
                    b "{i} (mungkin saya harus mencoba menaiki tangga?) {/i}"
                    if findwindow ==3:
                        b "{i} (Saya berharap ada cara untuk memeriksa apa yang sedang terjadi) {/i}"
                        b "{i} (i \ 'll periksa tangga) {/i}"
                        scene mstairs with fade
                        b "Aha!"
                        $ windowfound = 1
                        b "{i} (sama seperti yang saya kira) {/i}"
                        b "{i} (sekarang di mana flat kami) {/i}"
                        scene mstairs1 with fade
                        b "Dingin!"
                        b "{i} (aha! Apakah dia tidur?) {/i}"
                        b "{i} (Saya pikir lebih baik untuk pergi) {/i}"
                        pass
                    else:

                        if windowfound ==1:
                            menu:
                                "Periksa dari jendela":
                                    scene mstairs with fade
                                    "..."
                                    scene mstairs1 with fade
                                    b "{i} (tidur lagi) {/i}"
                                    "..."
                                    if wk >=2 and day == 2:
                                        scene mstairs2 with fade
                                        b "Hmmm"
                                        "Hei kamu!"
                                        scene mstairs3 with vpunch
                                        "Saya akan menelepon polisi"
                                        b "Sial, bukan apa yang Anda pikirkan!"
                                        "Saya menelepon polisi sekarang!"
                                        b "Damn"
                                        b "{i} (saya harus pergi) {/i}"
                                        b "Saya pikir saya harus pergi menemuinya"
                                        b "Kami tidak membutuhkan skandal apa pun"
                                        menu:
                                            "Pergi menemuinya":
                                                jump neighb
                                            "Tidak perlu":
                                                pass



                                    elif wk >=2 and mrel >=12:
                                        scene mstairs4 with fade
                                        b "Hmmm"
                                        b "{i} (dia berbalik) {/i}"
                                        b "{i} (apakah dia mencari cara saya!) {/i}"
                                        if mrel >=20:
                                            if day ==1:
                                                scene mstairs5 with fade
                                                b "{i} (wow!) {/i}"
                                                pass
                                            elif day ==4:
                                                scene mstairs5 with fade
                                                b "{i} (wow!) {/i}"
                                                pass

                                            elif day ==6:
                                                scene mstairs5 with fade
                                                b "{i} (wow!) {/i}"
                                                pass
                                            else:

                                                scene mstairs6 with fade
                                                b "{i} (wow!) {/i}"
                                                scene mstairs7 with dissolve
                                                "..."
                                                scene mstairs8 with dissolve
                                                b "{i} (oh fuck !! apakah dia melepasnya?) {/i}"
                                                if workrequest ==3:
                                                    scene mstairs9 with dissolve
                                                    m "{i} (Saya harus mulai menjaga diri saya sendiri) {/i}"
                                                    scene mstairs10 with dissolve
                                                    m "{i} (masalahnya adalah uang) {/i}"
                                                    if mbikini ==2:
                                                        scene mstairs11 with dissolve
                                                        m "{i} (bikini ini berkualitas baik) {/i}"
                                                        m "{i} (Saya ingin tahu apakah saya memiliki keberanian untuk memakainya di depan umum) {/i}"
                                                        m "{i} (i \ 'll tunjukkan ke [sname]) {/i}"
                                                        m "{i} (Saya yakin itu akan membuat saya merasa lebih percaya diri) {/i}"
                                                        scene mstairs12 with dissolve
                                                        m "{i} (Tidak Tidak Tidak, Gadis Ini Begitu Hidup) {/i}"
                                                        m "{i} (dia akan mulai mengajukan pertanyaan) {/i}"
                                                        m "{i}(Endlessly){/i}"
                                                        m "{i} (lebih baik tidak menunjukkan apa pun padanya) {/i}"
                                                        m "{i} (tidak saat ini) {/i}"
                                                        m "{i} (atau mungkin?) {/i}"
                                                        menu:
                                                            "Dia akan menunjukkannya kepada [sname]" if mrel >=200 and elaine_convince ==4:
                                                                m "{i} (let 's memiliki pendapatnya) {/i}"
                                                                b "{i} (apa yang dia pikirkan?) {/i}"
                                                                scene mstairs13 with dissolve
                                                                "..."
                                                                scene mstairs14 with dissolve
                                                                m "Jadi apa pendapat Anda tentang itu?"
                                                                s "Wow! Bagus"
                                                                s "Darimana kamu mendapatkannya?"
                                                                m "Saya hanya menelepon Anda untuk melihat apakah itu bagus atau tidak"
                                                                s "Ya itu, tunjukkan apa yang Anda miliki"
                                                                s "Ayo, kami tidak pernah terikat sejak kami pindah ke sini"
                                                                scene mstairs15 with dissolve
                                                                m "{i} (ok mungkin aku akan menunjukkan padanya nightie) {/i}"
                                                                m "{i} (Saya kira lebih baik dari [bname] untuk kepercayaan diri) {/i}"
                                                                scene mstairs16 with dissolve
                                                                "..."
                                                                scene mstairs17 with dissolve
                                                                s "..."
                                                                scene mstairs18 with dissolve
                                                                "..."
                                                                scene mstairs19 with fade
                                                                b "{i}(Wow){/i}"
                                                                b "{i} (apa yang terjadi) {/i}"
                                                                s "Oh cute"
                                                                s "Tapi di mana Anda berencana untuk memakai ini"
                                                                m "Saya tidak akan memakainya"
                                                                m "Hanya ... untuk menunjukkan kepada Anda"
                                                                s "Ini sangat seksi"
                                                                s "Tunjukkan lebih banyak tentang apa yang Anda dapatkan"
                                                                m "Ok"
                                                                scene mstairs16 with dissolve
                                                                "..."
                                                                scene mstairs17 with dissolve
                                                                s "{i}(Hmmm){/i}"
                                                                scene mstairs18 with dissolve
                                                                "..."
                                                                scene mstairs20 with dissolve
                                                                s "Wow!"
                                                                b "{i} (wow apa yang terjadi?) {/i}"
                                                                m "Apakah Anda pikir itu bagus?"
                                                                s "Of course"
                                                                pass



                                                            "{s} dia akan menunjukkannya ke [sname] {/s}" if mrel <200 and elaine_convince !=4:
                                                                "Anda tidak memiliki poin hubungan yang cukup dengan [mname]"
                                                                "Dan [mname] belum memulai pekerjaan klub"
                                                                m "{i} (tidak perlu) {/i}"
                                                                pass
                                                            "Dia menang":

                                                                m "{i} (tidak perlu) {/i}"
                                                                pass
                                                    else:

                                                        pass
                                                else:

                                                    pass
                                        else:

                                            pass
                                        "Hei kamu!"
                                        scene mstairs3 with vpunch
                                        "Saya akan menelepon polisi"
                                        b "Sial, bukan apa yang Anda pikirkan!"
                                        "Saya menelepon polisi sekarang!"
                                        b "Damn"
                                        b "{i} (saya harus pergi) {/i}"
                                        b "Saya pikir saya harus pergi menemuinya"
                                        b "Kami tidak membutuhkan skandal apa pun"
                                        menu:
                                            "Pergi menemuinya":
                                                jump neighb
                                            "Tidak perlu":
                                                pass
                                    else:

                                        b "{i}(I'll leave){/i}"
                                        pass
                                "Meninggalkan":





                                    pass
                        else:

                            b "{i} (tidak sekarang, saya akan menunggu beberapa hari) {/i}"
                            pass
            "Ketukan":




                if mrpmt <= 1:
                    play sound "sounds/knock.ogg"
                    m "Siapa itu?"
                    b "It's me"
                    m "Enter"
                    stop sound
                    scene mroom_av4 with fade
                    show screen mrelup
                    m "Apa yang salah [bname]?"
                    $ mrel += 5
                    hide screen mrelup
                    b "Saya ingin bertanya apakah ada yang bisa saya bantu"
                    m "No"
                    m "Nothing now"
                    b "Ok"
                    m "Jangan lupa melakukan studi online Anda"
                    b "Sure"
                    pass
                else:

                    if windowfound ==1 and mburnt == 0:
                        scene door with dissolve
                        play sound "sounds/knock.ogg"
                        m "APA!"
                        b "Tidak ada, saya ingin ..."
                        m "Please leave"
                        stop sound
                        if cselaine0 == 10:
                            b "Tapi aku punya sesuatu untuk memberitahumu"
                            m "Apa itu?"
                            b "Saya ... bolehkah saya masuk?"
                            scene mroom_av4 with fade
                            $ cselaine0 = 11
                            m "Apa itu [bname]?"
                            b "Saya punya 2 tiket bioskop gratis"
                            scene mroom_av6 with dissolve
                            m "Tiket bioskop?"
                            b "Ya saya pikir itu bagus untuk Anda dan [sname]"
                            b "Anda tahu ... mengubah suasana hati"
                            b "Tolong ambillah"
                            b "Mereka untuk pertunjukan pada pukul 17:00"
                            b "Anda masih punya waktu"
                            scene mroom_av7 with dissolve
                            m "Mhmm"
                            scene mroom_av4 with dissolve
                            m "Terima kasih [bname]"
                            m "Saya akan pergi memberi tahu [sname] untuk bersiap -siap"
                            m "Tapi bagaimana denganmu?"
                            b "Err ... aku akan pergi bersamamu dan kemudian, mungkin aku akan mengembara di kota"
                            b "Mungkin saya bisa mencari pekerjaan"
                            m "Kedengarannya bagus"
                            b "Keren, sampai jumpa"
                            scene door with fade
                            b "{i} (hebat) {/i}"
                            call screen gnav
                        else:
                            b "Ok"
                            pass
                    else:
                        play sound "sounds/knock.ogg"
                        m "Siapa itu?"
                        b "It's me"
                        m "Enter"
                        stop sound
                        if mburnt == 1 and day ==7:
                            scene mroom_av_b with fade
                            b "Hi"
                            m "Yes hi"
                            b "{i} (tidak sepertinya dia baik -baik saja) {/i}"
                            b "{i} (apa yang harus dikatakan padanya?) {/i}"
                            menu:
                                "Saya tidak enak badan":
                                    scene mroom_av_b1 with dissolve
                                    m "Apa itu sayang?"
                                    b "Mungkin demam, saya tidak tahu"
                                    m "Ya Tuhan, duduk"
                                    m "Saya akan mendapatkan termometer"
                                    scene mroom_av_b2 with fade
                                    m "Tempatkan ini di bawah lidah Anda"
                                    scene mroom_av_b3 with dissolve
                                    "..."
                                    b "Hmmm"
                                    scene mroom_av_b3p with dissolve
                                    b "{i}(Dammit){/i}"
                                    scene mroom_av_b2 with dissolve
                                    "..."
                                    scene mroom_av_b4 with dissolve
                                    m "Suhu Anda terlihat baik -baik saja"
                                    b "Saya tidak tahu, saya tidak merasa baik -baik saja"
                                    scene mroom_av_b5 with dissolve
                                    m "Kemarilah"
                                    scene mroom_av_b6 with dissolve
                                    m "Anda akan baik -baik saja sayang"
                                    scene mroom_av_b7 with dissolve
                                    menu:
                                        "Saya kira tidak demikian":
                                            if elaine_convince == 4:
                                                jump mroom_practice_b
                                            else:
                                                pass
                                        "Tidak mengatakan apa -apa":

                                            pass
                                    m "Pergi tidur siang, Anda akan merasa lebih baik"
                                    scene mroom_av_b8 with dissolve
                                    b "Saya kira begitu"
                                    b "{i} (hmmm, tidak buruk) {/i}"
                                    scene door with fade
                                    "..."
                                    call screen gnav
                                "Kamu tidak apa apa?":

                                    m "Ya saya"
                                    m "Tapi saya ingin tetap sendiri"
                                    m "Please"
                                    if persistent.patch_enabled:
                                        b "Ini tentang ayah tidak"
                                        pass
                                    else:
                                        b "Ini tentang Stewart bukanlah itu"
                                        pass

                                    b "Bajingan, dia melupakan semua tentang kita"
                                    scene mroom_av_b9 with dissolve
                                    m "..."
                                    scene mroom_av_b10 with dissolve
                                    b "{i} (menangis, keren, itu waktu) {/i}"
                                    menu:
                                        "Mengintip":
                                            scene mroom_av_b11 with dissolve
                                            b "Hmm"
                                            m "[bname]"
                                            m "Saya ingin tetap sendirian, silakan pergi"
                                            scene mroom_av_b9 with fade
                                            b "Errm ok"
                                            scene door with fade
                                            "Itu semua di sini"
                                            call screen gnav
                                        "Beri dia pelukan":

                                            b "Oh, jangan menangis"
                                            b "Ayo beri aku pelukan"
                                            scene mroom_av_b12 with dissolve
                                            "Dia terisak"
                                            show screen mrelup
                                            $ mrel += 2
                                            b "Tolong santai saja"
                                            hide screen mrelup
                                            scene mroom_av_b13 with dissolve
                                            b "{i}(Wow){/i}"
                                            m "Terima kasih atas dukungannya [bname]"
                                            b "Ya ya, tidak apa -apa"
                                            b "Aku akan pergi sekarang"
                                            scene door with fade
                                            "Itu semua di sini"
                                            call screen gnav
                        else:


                            pass
                        scene mroom_av4 with fade
                        show screen mrelup
                        m "Apa yang salah [bname]?"
                        $ mrel += 1
                        hide screen mrelup
                        b "Saya ingin bertanya apakah ada yang bisa saya bantu"
                        m "No"
                        m "Nothing now"
                        if elaine_convince == 4:
                            m "Atau ... saya katakan apa"
                            b "..."
                            jump mroom_practice
                        else:
                            pass
                        b "Ok"
                        m "Jangan lupa melakukan studi online Anda"
                        b "Sure"
                        if smoneym == 1:
                            b "Oh ngomong -ngomong"
                            b "Mengapa [sname] terus menceritakan tentang telepon"
                            b "Sementara dia tahu kita hidup dengan anggaran terbatas?"
                            scene mroom_av5 with dissolve
                            m "Pff saya tahu ya"
                            b "Saya harap saya bisa membantu"
                            m "Jangan khawatir tentang itu ..."
                            m "Saya akan mencari tahu"
                            pass
                        else:
                            pass


            "Mengetuk untuk memberinya tiket bioskop" if cselaine0 == 10:
                play sound "sounds/knock.ogg"
                m "Siapa itu?"
                b "It's me"
                m "Please leave"
                stop sound
                b "Tapi aku punya sesuatu untuk memberitahumu"
                m "Apa itu?"
                b "Saya ... bolehkah saya masuk?"
                scene mroom_pm1 with fade
                $ cselaine0 = 11
                m "Apa itu [bname]?"
                b "Saya punya 2 tiket bioskop gratis"
                scene mroom_pm2 with dissolve
                m "Tiket bioskop?!"
                b "Ya saya pikir itu bagus untuk Anda dan [sname]"
                b "Anda tahu ... mengubah suasana hati"
                b "Tolong ambillah"
                b "Mereka untuk pertunjukan pada pukul 17:00"
                b "Anda masih punya waktu"
                scene mroom_pm3 with dissolve
                m "Mhmm"
                scene mroom_pm4 with dissolve
                m "Terima kasih [bname]"
                m "Saya akan pergi memberi tahu [sname] untuk bersiap -siap"
                m "Tapi bagaimana denganmu?"
                b "Err ... aku akan pergi bersamamu dan kemudian, mungkin aku akan mengembara di kota"
                b "Mungkin saya bisa mencari pekerjaan"
                m "Kedengarannya bagus"
                b "Keren, sampai jumpa"
                scene door with fade
                b "{i} (hebat) {/i}"
                call screen gnav


        scene door with fade
        b "{i} (...) {/i}"
        call screen gnav

    elif Hour >16 and Hour <18:
        scene door with fade
        b "{i} (pintu terkunci) {/i}"
        call screen gnav

    elif Hour ==18:
        $ Hour += 1
        scene door with fade
        b "{i} (pintu terkunci) {/i}"
        call screen gnav

    elif Hour ==21:
        scene door with fade
        b "{i} (pintu terkunci) {/i}"
        call screen gnav


    elif Hour >21:
        scene door with fade
        b "{i} (pintu terkunci) {/i}"
        b "{i} (Saya harus tidur) {/i}"
        jump newdays
    else:

        scene door with fade
        b "{i} (pintu terkunci) {/i}"
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
