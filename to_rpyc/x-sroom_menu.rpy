

label sroom_menu:
    if Hour >=1 and Hour <11:
        scene door with fade
        b "{i} ([sname] pintu terkunci) {/i}"
        b "{i} (Saya ingin tahu apa yang dia lakukan?) {/i}"
        call screen gnav

    elif Hour ==11:
        $ Hour += 1
        scene door with fade
        b "{i} (sepertinya pintunya terbuka) {/i}"
        menu:
            "Ketukan":
                play sound "sounds/knock.ogg"
                s "Siapa itu?"
                b "It's me"
                $ srel += 10
                s "Masuk, itu terbuka"
                if sblowjobdone == 1 and day !=7:
                    scene sroom_ava with fade
                    b "Hi [sname]"
                    "..."
                    b "[sname]!?"
                    scene sroom_av1a with dissolve
                    s "Huh [bname] Maaf"
                    s "Saya sedang belajar"
                    s "Bisakah Anda membantu saya?"
                    b "Of course"
                    s "Saya tidak bisa melakukan persamaan ini"
                    b "Biarkan saya melihat"
                    scene sroom_av2a with dissolve
                    s "Yang ini"
                    scene sroom_av3a with dissolve
                    "..."
                    scene sroom_av4a with dissolve
                    b "Hmmm"
                    b "Yeah"
                    s "Ya apa?"
                    s "Aku akan melakukannya untukmu"
                    scene sroom_av2 with dissolve
                    b "Beginilah cara Anda melakukannya?"
                    scene sroom_av5a with dissolve
                    show screen srelup
                    s "Terima kasih"
                    hide screen srelup
                    b "Terima kasih kembali"
                    s "Sekarang izinkan saya menyelesaikan ini"
                    b "Sure"
                    if bcaught_s == 1 and b_fightback == 0:
                        s "Tunggu sebentar"
                        $ b_fightback = 1
                        b "Apa?"
                        scene sroom_av_sbm with fade
                        s "Saya butuh uang"
                        b "Untuk apa?"
                        s "Tidak ada, saya hanya butuh $ 100"
                        b "Ha!"
                        b "Yeah right"
                        scene sroom_av_sbm1 with dissolve
                        s "Ok pergi, tidak perlu"
                        s "Tetapi"
                        s "Ada sesuatu yang ingin saya tunjukkan kepada Anda untuk Anda berhati -hati lain kali"
                        s "Seseorang mungkin melihatmu"
                        b "Hah! Apa itu?"
                        scene etv_cbw with dissolve
                        s "Ini"
                        b "Hah!"
                        scene sroom_av_sbm2 with dissolve
                        s "Anda tahu [bname] Saya bagus"
                        if persistent.patch_enabled:
                            s "Dan Anda tahu bahwa saya tidak akan menunjukkan ini kepada ibu"
                            pass
                        else:
                            s "Dan Anda tahu bahwa saya tidak akan menunjukkan ini kepada [mname]"
                            pass
                        s "Tetapi Anda juga harus baik kepada saya sebagai balasannya"
                        menu:
                            "Beri dia uang":
                                b "Biarkan saya melihat apa yang saya miliki"
                                if mny >=100:
                                    $ go_counter -= 2
                                    b "Di sini ambillah"
                                    s "Terima kasih !!"
                                    pass
                                else:
                                    b "Saya tidak memilikinya sekarang"
                                    b "Aku akan memberimu nanti"
                                    $ go_counter += 1
                                    s "Oke, lihat yah!"
                                    pass
                            "Lakukan apapun yang Anda inginkan":

                                $ go_counter += 2
                                s "Oke, baiklah"
                                s "Kami akan melihat"
                                pass


                    elif b_fightback == 1:
                        scene sroom_av_sbm2 with dissolve
                        s "Jangan lupa uang atau hadiah saya jika Anda mau"
                        menu:
                            "Beri dia uang":
                                b "Biarkan saya melihat apa yang saya miliki"
                                if mny >=100:
                                    $ go_counter -= 2
                                    b "Di sini ambillah"
                                    s "Terima kasih !!"
                                    pass
                                else:
                                    b "Saya tidak memilikinya sekarang"
                                    b "Aku akan memberimu nanti"
                                    $ go_counter += 1
                                    s "Ok"
                                    pass
                            "Saya tidak punya uang":

                                $ go_counter += 2
                                pass


                    elif b_fightback == 2:
                        scene sroom_av_sbm2 with dissolve
                        s "Jangan lupakan uang saya"
                        b "Tidak Ada Lagi Uang Sayang"
                        s "Hehe, ok baik"
                        b "Saya juga punya foto"
                        scene nbr_k3_bw with dissolve

                        "..."
                        scene sroom_av_dwy with dissolve
                        s "Errr"
                        b "Bye dear"
                        scene sroom_av_sbm3 with dissolve
                        "..."
                        pass
                    else:

                        pass
                else:

                    scene sroom_av with fade
                    b "Hai [sname], apa yang salah?"
                    scene sroom_av1 with dissolve
                    s "Saya tidak tahu bagaimana melakukan persamaan ini"
                    b "Mari kita lihat"
                    scene sroom_av2 with dissolve
                    b "Hmmm"
                    scene sroom_av3 with dissolve
                    b "Done"
                    show screen srelup
                    s "Thank youuuu"
                    hide screen srelup
                    scene sroom_av4 with fade
                    s "Sekarang izinkan saya menyelesaikan ini"
                    b "Sure"
                    pass
            "Memasuki":

                if laptoprequested == 1 and sscall ==0:
                    $ sscall = 1
                    scene sroom_scall5 with fade
                    if persistent.patch_enabled:
                        s "Yes dad"
                        pass
                    else:
                        s "Yes stewart"
                        pass
                    "..."
                    s "Tidak sebanyak itu ..."
                    scene sroom_scall6 with dissolve
                    s "Oke, terima kasih"
                    s "Kamu juga, bye"
                    b "Hmm"
                    scene sroom_scall7 with dissolve
                    s "Ya?"
                    b "Dengan siapa kamu berbicara?"
                    if persistent.patch_enabled:
                        s "Dad"
                    else:
                        s "Stewart"
                        pass

                    b "Hmm tidak, kamu tahu bahwa kita tidak diizinkan meneleponnya?"
                    s "Saya tidak meneleponnya"
                    b "Ah masa? Bagaimana dia mendapatkan nomor Anda?"
                    b "Nomor Anda baru kan? Dia tidak tahu bahwa kamu sudah mendapatkannya"
                    scene sroom_scall8 with dissolve
                    s "Apa masalah Anda [bname]!?"
                    s "Apakah saya menelepon atau tidak?!"
                    if persistent.patch_enabled:
                        b "Tidak ada ... aku akan memberitahu ibu"
                        pass
                    else:
                        b "Tidak ada ... aku akan memberi tahu [mname]"
                        pass
                    s "Berlangsung! Katakan padanya"
                    b "Kami akan melihat"
                    scene sroom_scall7 with dissolve
                    s "Sebelum Anda memberitahunya ..."
                    s "Bolehkah saya tahu apa yang saya lakukan salah?"
                    b "Anda tahu bahwa [mname] tidak ingin kami menghubungi dia dengan benar?"
                    s "Ya tapi kadang -kadang dia meneleponmu"
                    b "Ini berbeda, saya tidak pernah memanggilnya"
                    s "Oh ... saya tidak tahu"
                    b "Jangan khawatir kita semua membuat kesalahan"
                    scene sroom_scall9 with dissolve
                    s "Terima kasih [bname]"
                    b "Baiklah, lihat yah"
                    scene door with fade
                    b "{i} (Saya harus memberi tahu [mname] tentang ini) {/i}"
                    call screen gnav
                else:
                    pass
                scene sroom_av5 with hpunch
                s "[bname] !! Apa yang salah denganmu?"
                b "Hai [sname], apa yang kamu lakukan?"
                scene sroom_av6 with dissolve
                s "Dengan serius!"
                b "Apa?"
                s "Anda masuk dan bertanya apa yang saya lakukan?"
                b "Jadi apa?"
                scene sroom_av7 with dissolve
                b "Saya melihat Anda membutuhkan bantuan untuk ini"
                s "Tidak, saya bisa mengelola"
                b "Oke, sesuai keinginan Anda"
                pass

        if spiercings == 3:
            s "Err"
            s "Anda bisa kembali setelah 5 menit saya ingin menunjukkan sesuatu kepada Anda"
            b "Keren ok"
            jump sroom_morningpiercings
        else:
            pass
        scene door with fade
        b "{i} (...) {/i}"
        call screen gnav

    elif Hour >12 and Hour <13:
        scene door with fade
        b "{i} (pintu terkunci) {/i}"
        call screen gnav

    elif Hour ==13:
        $ Hour += 1
        scene door with fade
        b "{i} (sepertinya pintunya terbuka) {/i}"
        scene sroom_av8 with fade
        b "Hey there"
        b "Apa yang sedang kamu lakukan?"
        scene sroom_av9 with dissolve
        s "[bname]! Tidak bisakah Anda melihat saya membaca"
        s "Please"
        b "Ok Sorry"
        if wk >= 1:
            "..."
            scene sroom_av10 with dissolve
            s "Berhentilah menjengkelkan"
            scene sroom_av11 with dissolve
            s "Please [bname]"
            s "Please leave"
            menu:
                "Saya akan pergi dengan satu kondisi*":
                    s "Apa itu?"
                    scene sroom_av15 with dissolve
                    "..."
                    if kissrepeat >4:
                        b "Ayo, kami sudah melakukannya berkali -kali"
                        s "Saya tidak sedang dalam mood sekarang"
                        b "Itu hanya satu ciuman"
                        scene sroom_av16 with dissolve
                        s "Anda cabul"
                        scene sroom_av17 with dissolve
                        "..."
                        if srel >= 80:
                            b "{i}(Hmm){/i}"
                            b "{i} (mungkin ...) {/i}"
                            scene sroom_av18 with dissolve
                            b "{i} (keren, tidak ada reaksi) {/i}"
                            menu:
                                "Tarik":
                                    scene sroom_av24 with dissolve
                                    "..."
                                    if sphotos_progress >1 and srel >= 100:
                                        jump sroom13

                                    elif srel >= 120:
                                        jump sroom13
                                    else:

                                        scene sroom_av25 with hpunch
                                        b "Aduh!"
                                        s "Keluar"
                                        scene door with fade
                                        b "{i} (...) {/i}"
                                        "..."
                                        call screen gnav
                                "Tidak melakukan apa -apa":

                                    pass
                            scene sroom_av19 with dissolve
                            s "Senang"
                            b "Hehehe"
                            s "Sekarang izinkan saya membaca"
                            b "Ya keren"
                            scene door with fade
                            b "{i} (...) {/i}"
                            "..."
                            call screen gnav
                        else:
                            scene sroom_av19 with dissolve
                            s "Sekarang izinkan saya membaca"
                            b "Ya keren"
                            scene door with fade
                            b "{i} (...) {/i}"
                            "..."
                            call screen gnav
                    else:
                        s "Keluar!"
                        if kissrepeat ==0:
                            "Mungkin Anda harus belajar berciuman dengan dia terlebih dahulu?!"
                            pass

                        elif kissrepeat ==4:
                            s "Cukup berciuman untukmu"
                            s "Sekarang tinggalkan aku sendiri"
                            "Berlatih lebih banyak ciuman"
                            pass

                        elif kissrepeat >0 and kissrepeat <4:
                            "Berlatih lebih banyak ciuman"
                            pass

                    b "Ok fine"
                    scene sroom_av12 with dissolve
                    s "Apa sekarang!"
                    scene sroom_av13a with dissolve
                    b "..."
                    scene sroom_av14a with hpunch
                    hide screen sreldw
                    s "Tuhanku [bname]"
                    s "Please go"
                    if persistent.patch_enabled:
                        s "Atau saya akan menelepon ibu"
                        pass
                    else:
                        s "Atau saya akan menelepon [mname]"
                        pass

                    menu:
                        "Tertawa":
                            b "Hahahah"
                            scene sroom_av15a with vpunch
                            s "KELUAR!!"
                            b "I'm leaving"
                            scene door with fade
                            b "{i} (...) {/i}"
                            "..."
                            call screen gnav
                "Menggodanya":


                    b "{i}(Hmm){/i}"
                    scene sroom_av12 with dissolve
                    s "Apa sekarang [bname]?"
                    b "Aku akan ..."
                    menu:
                        "Menggelitik kakinya":
                            scene sroom_av13 with dissolve
                            b "..."
                            show screen sreldw
                            $ srel -= 1
                            scene sroom_av14 with hpunch
                            hide screen sreldw
                            s "Tuhanku [bname]"
                            s "Please go"
                            if persistent.patch_enabled:
                                s "Atau saya akan menelepon ibu"
                                pass
                            else:
                                s "Atau saya akan menelepon [mname]"
                                pass

                            b "Hahahah"
                            menu:
                                "Panggil dia" if workrequest ==3:
                                    jump sroom13tease
                                "Melanjutkan":
                                    pass
                            b "I'm going"
                            pass
                        "Tarik pantatnya ke bawah*":

                            if pullsb_repeat >2 and sblowjobdone ==1:
                                if pullsb_repeat >=5 and naivetalk == 0 and day ==7:
                                    scene sroom_av20 with hpunch
                                    b "Hahaha"
                                    scene sroom_av15b with vpunch
                                    s "KELUAR!!"
                                    b "Uh oh!"
                                    scene sroom_av23 with dissolve
                                    m "[bname]!"
                                    m "Let's talk"
                                    b "Ok"
                                    m "Ikuti saya ke kamar saya"
                                    jump m_b_naivetalk
                                else:
                                    scene sroom_av22 with hpunch
                                    b "Wow"
                                    $ pullsb_repeat += 1
                                    if srel >=200 and workrequest ==3 and day !=7:
                                        jump bottomsdown
                                    else:
                                        "Naikkan Poin Hubungan Anda, 200 Dibutuhkan"
                                        pass
                                    scene sroom_av15a with vpunch
                                    s "KELUAR!!"
                                    b "I'm leaving"
                                    scene door with fade
                                    b "{i} (...) {/i}"
                                    "..."
                                    call screen gnav


                            elif pullsb_repeat >2 and scorr >= 20:
                                scene sroom_av21 with hpunch
                                b "Hmmm"
                                $ pullsb_repeat += 1
                                scene sroom_av15a with vpunch
                                s "KELUAR!!"
                                b "Siapa yang memakai celana dalam di bawah celana dalam?"
                                b "Hahahaha"
                                s "Aku berkata!"
                                b "I'm leaving"
                                scene door with fade
                                b "{i} (...) {/i}"
                                "..."
                                call screen gnav
                            else:


                                scene sroom_av20 with hpunch
                                b "Hahaha"
                                $ pullsb_repeat += 1
                                scene sroom_av15a with vpunch
                                s "KELUAR!!"
                                b "Apakah kamu serius? Siapa yang memakai celana dalam di bawah celana dalam"
                                b "Hahahaha"
                                s "Aku berkata!"
                                b "I'm leaving"
                                scene door with fade
                                b "{i} (...) {/i}"
                                "..."
                                call screen gnav
                "Meninggalkan":


                    b "I'm going"
                    pass
        else:

            pass
        scene door with fade
        b "{i} (...) {/i}"
        call screen gnav

    elif Hour >13 and Hour <18:
        if sroom13underss >= 4 and srel >300 and sroomride == 0:
            scene door with fade
            b "{i} (sepertinya pintunya terbuka) {/i}"
            $ sroomride = 1
            jump returnsroom14
        else:
            pass
        scene door with fade
        b "{i} (pintu terkunci) {/i}"
        if windowfound ==1 and swindowchecked == 0:
            $ Hour += 1
            b "{i} (mungkin saya dapat memeriksa windows) {/i}"
            menu:
                "Periksa jendela":
                    $ swindowchecked = 1
                    scene mstairs with fade
                    "..."
                    if sroom13underss >= 4 and srel >300:
                        jump stairssroom14
                    else:
                        pass
                    scene sstairs with fade
                    b "{i}(Hmm){/i}"
                    "..."
                    if srel >=20:
                        scene sstairs1 with fade
                        b "{i} (...) {/i}"
                        scene sstairs2 with dissolve
                        b "{i}(Oh){/i}"
                        if instadone == 2:
                            if srel >=30 and bikini3 == 2 and day ==1:
                                scene sstairs4 with dissolve
                                s "{i} (Saya tidak bisa memakainya di mana saja, [mname] akan membunuh saya) {/i}"
                                scene sstairs5 with dissolve
                                b "{i}(Oh shit){/i}"
                                pass

                            elif srel >=30 and bikini3 == 2 and day ==4:
                                scene sstairs4 with dissolve
                                s "{i} (Saya tidak bisa memakainya di mana saja, [mname] akan membunuh saya) {/i}"
                                scene sstairs5 with dissolve
                                b "{i}(Oh shit){/i}"
                                pass

                            elif srel >=40 and sstrip == 1 and day ==3:
                                scene sstairs6 with dissolve
                                b "{i}(Yeah){/i}"
                                scene sstairs7 with dissolve
                                s "..."
                                b "{i} (apakah dia berbicara pada dirinya sendiri?) {/i}"
                                pass

                            elif srel >=50 and sstrip == 1 and day ==5:
                                scene sstairs6 with dissolve
                                b "{i}(Yeah){/i}"
                                scene sstairs8 with dissolve
                                s "..."
                                scene sstairs9 with dissolve
                                s "..."
                                b "{i} (saya yakin dia mengatakan sesuatu) {/i}"
                                pass

                            elif sbm ==2:
                                scene sstairs10 with fade
                                b "{i} (apa ini?) {/i}"
                                scene sstairs11 with dissolve
                                b "..."
                                scene sstairs12 with dissolve
                                s "Ahhh"
                                pass
                            else:

                                scene sstairs3 with dissolve
                                s "Woohoo !!"
                                scene sstairs3a with dissolve
                                b "{i}(Oh wow){/i}"
                                "RAISE YOUR POINTS AND/OR TRY ON DIFFERENT DAYS"
                                "Setidaknya 50 poin yang dibutuhkan"
                                pass

                            "Hei kamu!"
                            b "{i} (persetan!) {/i}"
                            scene mstairs3 with vpunch
                            "Saya akan menelepon polisi"
                            b "Sial, bukan apa yang Anda pikirkan!"
                            b "{i} (itu yang Anda pikirkan) {/i}"
                            "Saya menelepon polisi sekarang!"
                            b "Damn"
                            b "{i} (saya harus pergi) {/i}"
                            scene door with fade
                            b "{i} (...) {/i}"
                            b "Saya pikir saya harus pergi menemuinya"
                            b "Kami tidak membutuhkan skandal apa pun"
                            menu:
                                "Pergi menemuinya":
                                    jump neighb
                                "Tidak perlu":
                                    call screen gnav
                        else:

                            "Hei kamu!"
                            b "{i} (persetan!) {/i}"
                            scene mstairs3 with vpunch
                            "Saya akan menelepon polisi"
                            b "Sial, bukan apa yang Anda pikirkan!"
                            b "{i} (itu yang Anda pikirkan) {/i}"
                            "Saya menelepon polisi sekarang!"
                            b "Damn"
                            b "{i} (saya harus pergi) {/i}"
                            scene door with fade
                            b "{i} (...) {/i}"
                            b "Saya pikir saya harus pergi menemuinya"
                            b "Kami tidak membutuhkan skandal apa pun"
                            menu:
                                "Pergi menemuinya":
                                    jump neighb
                                "Tidak perlu":
                                    call screen gnav
                    else:
                        "Hei kamu!"
                        scene mstairs3 with vpunch
                        "Saya akan menelepon polisi"
                        b "Sial, bukan apa yang Anda pikirkan!"
                        "Saya menelepon polisi sekarang!"
                        b "Damn"
                        b "{i} (saya harus pergi) {/i}"
                        scene door with fade
                        b "{i} (...) {/i}"
                        b "Saya pikir saya harus pergi menemuinya"
                        b "Kami tidak membutuhkan skandal apa pun"
                        menu:
                            "Pergi menemuinya":
                                jump neighb
                            "Tidak perlu":
                                call screen gnav
        else:
            call screen gnav

    elif Hour ==18:
        $ Hour += 1
        scene door with fade
        b "{i} (sepertinya pintunya terbuka) {/i}"
        menu:
            "Ketukan":
                play sound "sounds/knock.ogg"
                s "Siapa itu?"
                b "It's me"
                s "Masuk, itu terbuka"
                if sburnt ==1:
                    jump sburn_study
                else:
                    pass
                scene sroom_st with fade
                b "Hai [sname], apa yang salah?"
                scene sroom_st1 with dissolve
                s "Saya mencoba belajar duh!"
                menu:
                    "Berlatih berciuman" if skiss >=1:
                        b "Bisakah Anda membantu saya"
                        s "Dengan apa?"
                        b "Meningkatkan ciuman saya"
                        if srel >=80:
                            s "Siapa Anda menggunakan ciuman ini?"
                            menu:
                                "Hanya kamu":
                                    $ srel += 5
                                    show screen srelup
                                    s "Hehe"
                                    hide screen srelup
                                    pass
                                "Tidak ada":
                                    b "No one"
                                    pass
                            s "Kemarilah"
                            scene sroom_st_kiss with dissolve
                            $ kissrepeat += 1
                            "Pengalaman ciuman Anda telah meningkat"
                            s "Tolong pergi sekarang"
                            menu:
                                "Saya tidak menginginkannya":
                                    scene sroom_st_kiss1 with dissolve
                                    s "Apa maksudmu?"
                                    b "Saya ingin ciuman yang berbeda ..."
                                    scene sroom_st_kiss2 with dissolve
                                    b "Seperti ini"
                                    if srel >=200:
                                        s "Tunggu..."
                                        b "Apa?"
                                        s "[mname] ada di sini"
                                        b "Jadi apa? Kita bisa mengunci pintu"
                                        s "Ok"
                                        scene sroom_st_kiss3 with fade
                                        s "..."
                                        scene sroom_st_kiss4 with dissolve
                                        s "Ahhh [bname]"
                                        s "I'm"
                                        scene sroom_st_kiss5 with dissolve
                                        s "Ahhhh"
                                        if srel >=350:
                                            b "Apakah kamu cum?"
                                            s "Tidak, kamu konyol"
                                            b "Lalu apa!"
                                            scene sroom_st_kiss6 with dissolve
                                            s "It's"
                                            scene sroom_st_kiss2 with dissolve
                                            b "Ini kencing!"
                                            s "Hehehe!"
                                            menu:
                                                "Saya menyukainya":
                                                    b "Mmm saya suka itu"
                                                    scene sroom_st_kiss3 with dissolve
                                                    s "Ahh kamu kotor"
                                                    scene sroom_st_kiss7 with vpunch
                                                    s "Ahhh"
                                                    scene sroom_st_kiss8 with dissolve
                                                    s "Oh!"
                                                    "..."
                                                    b "Datang..."
                                                    scene sroom_st_kiss9 with fade
                                                    "..."
                                                    scene sroom_st_kiss10 with dissolve
                                                    "..."
                                                    scene sroom_st_kiss11 with dissolve
                                                    s "..."
                                                    scene sroom_st_kiss12 with dissolve
                                                    b "Yeah"
                                                    scene sroom_st_kiss13 with dissolve
                                                    "..."
                                                    scene sroom_st_kiss14 with dissolve
                                                    s "Ahhh"
                                                    scene sroom_st_kiss15 with hpunch
                                                    "..."
                                                    scene sroom_st_kiss15a with dissolve
                                                    s "..."
                                                    scene sroom_st_kiss16 with fade
                                                    b "I'll go"
                                                    s "Ok"
                                                    scene door with fade
                                                    b "{i} (...) {/i}"
                                                    call screen gnav
                                                "Saya tidak suka":

                                                    scene sroom_st_kiss6 with fade
                                                    s "Anda bisa pergi"
                                                    scene door with fade
                                                    b "{i} (...) {/i}"
                                                    call screen gnav
                                        else:

                                            scene sroom_st_kiss6 with fade
                                            s "Anda bisa pergi sekarang"
                                            scene door with fade
                                            b "{i} (...) {/i}"
                                            call screen gnav
                                    else:
                                        s "No [bname]"
                                        b "Ok"
                                        "Naikkan hubungan Anda menjadi 200"
                                        pass
                                "Melanjutkan":

                                    b "Ok"
                                    pass
                        else:
                            s "Tidak, tolong pergi"
                            b "Ok"
                            "Naikkan hubungan Anda menjadi 80 poin"
                            pass
                    "Menawarkan bantuan":

                        b "Ingin bantuan saya?"
                        if badgrds == 1:
                            scene sroom_st1s with dissolve
                            s "Ya tolong, maukah kamu?"
                            menu:
                                "Dengan satu kondisi":
                                    jump study_event
                                "Tentu saja":

                                    pass
                        else:

                            pass
                        s "Yes"
                        scene sroom_st2 with dissolve
                        b "Hmmm"
                        $ srel += 2
                        scene sroom_st3 with dissolve
                        b "Done"
                        show screen srelup
                        s "Thank youuuu"
                        hide screen srelup
                        scene sroom_st4 with fade
                        s "Sekarang izinkan saya menyelesaikan ini"
                        b "Sure"
                        pass
                    "Tinggalkan dia sendiri":

                        b "Lihat yah!"
                        pass
                    "Menggelitiknya":

                        scene sroom_st10 with hpunch
                        b "Huuu!"
                        scene sroom_st11 with hpunch
                        s "Hai!!"
                        b "Hahaha, santai!"
                        if srel >=25:
                            s "Berhentilah tertawa !!"
                            scene sroom_st13 with dissolve
                            b "Ahahahaha"
                            scene sroom_st14 with dissolve
                            "..."
                            b "Hahahaha"
                            scene sroom_st15 with dissolve
                            s "Sungguh idiot!"
                            menu:
                                "{s} peluk {/s}":
                                    "Belum tersedia"
                                    pass
                                "Meninggalkan":

                                    pass

                            scene sroom_st16 with dissolve
                            s "..."
                            pass
                        else:

                            s "Keluar!"
                            scene sroom_st12 with dissolve
                            b "Lihat ya!"
                            pass


                    "Apakah Anda ingin berlatih pemotretan untuk halaman Anda?" if instadone == 2:
                        s "Ya, tapi apakah Anda mendapatkan kamera?"
                        b "Kami dapat mencoba dengan ponsel saya"
                        s "Hmm, oke"
                        scene sroom_inst_photos with fade
                        b "Anda tidak berencana mengambil foto dengan itu"
                        s "Apa!?"
                        b "Ayo, ubah menjadi sesuatu yang lebih menyenangkan"
                        s "Seperti apa?"
                        b "Aku tidak tahu..."
                        menu:
                            "Mungkin rok?":
                                s "Ok"
                                s "Wait outside"
                                scene black
                                "..."
                                s "Anda bisa masuk"
                                scene sroom_inst_photos1 with fade
                                b "Mengapa tidak rok?"
                                s "Saya tidak suka"
                                b "OK"
                                b "Cobalah pose yang berbeda"
                                b "Saya akan memakai lebih banyak lampu"
                                scene sroom_inst_photos2 with fade
                                b "Bagus!"
                                scene sroom_inst_photos3 with dissolve
                                s "Saya pikir itu cukup untuk hari ini"
                                b "Mau mu"
                                if srel <12:
                                    scene black
                                    "Satu opsi lagi tersedia jika Anda memiliki poin lebih tinggi dari 11"
                                    pass
                                else:

                                    pass


                            "Aku punya sesuatu untukmu" if bikini1 ==1:
                                s "Apa itu?"
                                b "Di sini, pakai"
                                scene sroom_inst_photos_happy with dissolve
                                s "Waaah!"
                                $ bikini1 = 2
                                s "Tolong tunggu di luar"
                                scene door with dissolve
                                "..."
                                s "Anda bisa masuk!"
                                scene sroom_inst_photos14 with fade
                                s "Bagaimana menurutmu?"
                                b "Ayo, jangan malu, itu indah"
                                scene sroom_inst_photos15 with dissolve
                                s "Menurutmu begitu?"
                                b "Yeah"
                                b "Mari kita ambil beberapa foto"
                                s "Hanya satu"
                                b "Ya ampun!"
                                b "Ok"
                                scene sroom_inst_photos16 with dissolve
                                s "Bagaimana?"
                                b "Besar"
                                s "Cukup untuk hari ini"
                                b "Hmm Ok"
                                pass

                            "Saya memiliki sesuatu yang baru untuk Anda" if bikini3 ==1:
                                s "Apa itu?"
                                b "Di sini, pakai"
                                scene sroom_inst_photos_happy with dissolve
                                s "Waaah!"
                                $ bikini3 = 2
                                s "Tolong tunggu di luar"
                                scene door with dissolve
                                "..."
                                "..."
                                b "Siap!"
                                s "[bname] Anda menjadi cabul!"
                                b "Apa? Apa yang salah?"
                                scene sroom_inst_photos21 with dissolve
                                s "Dengan serius!!"
                                b "Serius Apa? Bisakah saya masuk!"
                                s "Tinggal!"
                                b "Jangankah kamu menyukainya?"
                                s "Tidak, saya tidak \ 't"
                                b "Ok, berikan padaku aku akan mengembalikannya"
                                scene sroom_inst_photos22 with dissolve
                                s "Tidak, saya akan menyimpannya, tetapi Anda tidak akan pernah melihatnya"
                                s "Atau ambil foto saya di dalamnya"
                                b "Wow"
                                s "Pergi saja!"
                                scene door with dissolve
                                b "Ok ok pergi"
                                scene sroom_inst_photos23 with fade
                                s "Orang cabul!!"
                                scene door with fade
                                "..."
                                call screen gnav


                            "Saya memiliki monokini untuk Anda" if bikini2 ==1:
                                s "Apa itu?"
                                b "Di sini, pakai"
                                scene sroom_inst_photos_happy with dissolve
                                s "Waaah!"
                                $ bikini2 = 2
                                s "Tolong tunggu di luar"
                                scene door with dissolve
                                "..."
                                s "Anda bisa masuk!"
                                scene sroom_inst_photos24 with fade
                                s "Bagaimana menurutmu?"
                                b "Itu indah"
                                b "Coba beberapa pose"
                                s "Only one"
                                b "Ya ampun!"
                                b "Ok"
                                scene sroom_inst_photos25 with dissolve
                                s "Bagaimana?"
                                b "Besar"
                                s "Cukup untuk hari ini"
                                b "Hmm Ok"
                                pass

                            "Saya memiliki pakaian rok untuk Anda" if microskirt1 ==1:
                                s "Apa itu?"
                                b "Di sini, pakai"
                                scene sroom_inst_photos_happy with dissolve
                                s "Waaah!"
                                $ microskirt1 = 2
                                s "Tolong tunggu di luar"
                                scene door with dissolve
                                "..."
                                s "Anda bisa masuk!"
                                scene sroom_inst_photos31 with fade
                                s "Bagaimana menurutmu?"
                                b "Itu indah"
                                b "Coba beberapa pose"
                                s "Only one"
                                b "Ya ampun!"
                                b "Ok"
                                scene sroom_inst_photos32 with dissolve
                                s "Bagaimana?"
                                b "Besar"
                                s "Cukup untuk hari ini"
                                b "Hmm Ok"
                                pass

                            "Rok mini" if microskirt1 ==2:
                                s "Tolong tunggu di luar"
                                scene door with dissolve
                                "..."
                                s "Anda bisa masuk!"
                                scene sroom_inst_photos31 with fade
                                s "Jadi apa yang kita lakukan?"
                                b "Beri aku beberapa pose"
                                scene sroom_inst_photos32 with dissolve
                                "..."
                                b "Ok kita sudah selesai dengan yang satu ini"
                                s "Apa selanjutnya?"
                                b "Coba beberapa pose keren"
                                if srel >=36:
                                    scene sroom_inst_photos33 with dissolve
                                    s "Sesuatu seperti itu!"
                                    b "Luar biasa!"
                                    b "Pergi ke dinding itu"
                                    if sdom >=20:
                                        s "Apa! Mengapa?"
                                        b "Itu akan terlihat lebih baik di dinding"
                                        s "Di mana?"
                                        b "Go there"
                                        b "Hanya satu foto dinding sisi"
                                        scene sroom_inst_photos34 with fade
                                        b "Looks stunning"
                                        b "More"
                                        if srel >=45:
                                            scene sroom_inst_photos35 with fade
                                            b "Besar"
                                            s "Bisakah kita berhenti hari ini?"
                                            b "Tentu..."
                                            b "Sampai jumpa lagi"
                                            pass
                                        else:

                                            s "Bisakah kita berhenti hari ini?"
                                            b "Tentu..."
                                            b "Sampai jumpa lagi"
                                            pass
                                    else:

                                        s "Tidak [bname] itu cukup"
                                        b "Hmm Ok"
                                        scene black
                                        "Anda membutuhkan poin dominasi yang lebih tinggi (20)"
                                        pass
                                else:

                                    scene sroom_inst_photos31 with dissolve
                                    s "No [bname]"
                                    s "Cukup untuk hari ini"
                                    b "Hmm Ok"
                                    scene black
                                    "Anda membutuhkan poin hubungan yang lebih tinggi (36)"
                                    pass




                            "Monokini" if bikini2 ==2:
                                s "Tolong tunggu di luar"
                                scene door with dissolve
                                "..."
                                s "Anda bisa masuk!"
                                scene sroom_inst_photos26 with fade
                                s "Jadi apa yang kita lakukan?"
                                b "Beri aku beberapa pose"
                                scene sroom_inst_photos27 with dissolve
                                "..."
                                b "Ok kita sudah selesai dengan yang satu ini"
                                s "Apa selanjutnya?"
                                b "Cobalah untuk berbalik"
                                if srel >=36:
                                    scene sroom_inst_photos28 with dissolve
                                    s "Sesuatu seperti itu!"
                                    b "Luar biasa!"
                                    b "Pergi ke dinding itu"
                                    if sdom >=20:
                                        s "Apa! Mengapa?"
                                        b "Itu akan terlihat lebih baik di dinding"
                                        s "Di mana?"
                                        b "Go there"
                                        b "Hanya satu foto dinding sisi"
                                        scene sroom_inst_photos29 with fade
                                        b "Looks stunning"
                                        b "More"
                                        if srel >=45:
                                            scene sroom_inst_photos30 with fade
                                            b "Besar"
                                            s "Bisakah kita berhenti hari ini?"
                                            b "Tentu..."
                                            b "Sampai jumpa lagi"
                                            pass
                                        else:

                                            s "Bisakah kita berhenti hari ini?"
                                            b "Tentu..."
                                            b "Sampai jumpa lagi"
                                            pass
                                    else:

                                        s "Tidak [bname] itu cukup"
                                        b "Hmm Ok"
                                        scene black
                                        "Anda membutuhkan poin dominasi yang lebih tinggi (20)"
                                        pass
                                else:

                                    scene sroom_inst_photos26 with dissolve
                                    s "No [bname]"
                                    s "Cukup untuk hari ini"
                                    b "Hmm Ok"
                                    scene black
                                    "Anda membutuhkan poin hubungan yang lebih tinggi (36)"
                                    pass


                            "Bikini" if bikini1 ==2:
                                s "Tolong tunggu di luar"
                                scene door with dissolve
                                "..."
                                s "Anda bisa masuk!"
                                scene sroom_inst_photos14 with fade
                                b "Ayo! Berhenti melakukan ini setiap saat"
                                scene sroom_inst_photos15 with dissolve
                                s "Jadi apa yang kita lakukan?"
                                b "Beri aku beberapa pose"
                                scene sroom_inst_photos16 with dissolve
                                "..."
                                b "Ok kita sudah selesai dengan yang satu ini"
                                scene sroom_inst_photos17 with dissolve
                                s "Apa selanjutnya?"
                                scene sroom_inst_photos16 with dissolve
                                b "Cobalah untuk berbalik"
                                if srel >=36:
                                    scene sroom_inst_photos19 with dissolve
                                    s "Sesuatu seperti itu!"
                                    b "Luar biasa!"
                                    b "Pergi ke dinding itu"
                                    if sdom >=20:
                                        s "Apa! Mengapa?"
                                        b "Itu akan terlihat lebih baik di dinding"
                                        s "Di mana?"
                                        b "Go there"
                                        b "Hanya satu foto dinding sisi"
                                        scene sroom_inst_photos20 with fade
                                        b "Looks stunning"
                                        s "Bisakah kita berhenti hari ini?"
                                        b "Tentu..."
                                        b "Sampai jumpa lagi"
                                        pass
                                    else:

                                        s "Tidak [bname] itu cukup"
                                        b "Hmm Ok"
                                        scene black
                                        "Anda membutuhkan poin dominasi yang lebih tinggi (20)"
                                        pass
                                else:

                                    scene sroom_inst_photos18 with dissolve
                                    s "No [bname]"
                                    s "Cukup untuk hari ini"
                                    b "Hmm Ok"
                                    scene black
                                    "Anda membutuhkan poin hubungan yang lebih tinggi (36)"
                                    pass

                            "Kejutan saya" if srel >=12:
                                scene sroom_inst_photos4 with fade
                                b "Hmm, tidak buruk"
                                b "Coba pose lain"
                                scene sroom_inst_photos5 with dissolve
                                s "Sesuatu seperti ini?"
                                b "Cantik ya!"
                                scene sroom_inst_photos6 with dissolve
                                s "Oh [bname] Ayo!"
                                b "Aku bersumpah, melanjutkan!"
                                if srel >=17 and srel <=20:
                                    scene sroom_inst_photos7 with dissolve
                                    s "Bagaimana dengan ini?"
                                    b "Super cute"
                                    b "Lebih banyak lagi ..."
                                    s "No"
                                    pass
                                elif srel >=21:
                                    scene sroom_inst_photos7 with dissolve
                                    s "Bagaimana dengan ini?"
                                    b "Super cute"
                                    b "Lebih banyak lagi ..."
                                    s "Hmm"
                                    scene sroom_inst_photos9 with dissolve
                                    b "Bagus!"
                                    menu:
                                        "{s} Minta dia melakukan sesuatu yang sugestif {/s}":
                                            scene sroom_inst_photos9as with dissolve
                                            b "Wow"
                                            b "More"
                                            b "No"
                                            pass
                                        "Lagi?":
                                            if srel >=25 and srel <=35:
                                                s "Ok"
                                                s "Only one"
                                                scene sroom_inst_photos10 with dissolve
                                                b "Dingin"
                                                pass

                                            elif srel >35:
                                                s "Ok"
                                                s "Only one"
                                                scene sroom_inst_photos10 with dissolve
                                                b "Dingin"
                                                b "Ayo, satu lagi"
                                                scene sroom_inst_photos11 with dissolve
                                                s "Mhhmm"
                                                s "Ok"
                                                scene sroom_inst_photos12 with fade
                                                b "..."
                                                b "Oke cukup"
                                                scene sroom_inst_photos13 with dissolve
                                                s "Terima kasih"
                                                pass
                                            else:

                                                s "No"
                                                pass
                                else:


                                    pass

                                scene sroom_inst_photos8 with dissolve
                                s "Cukup untuk hari ini"
                                b "Hmm Ok"
                                pass

                    "Kami membutuhkan foto baru untuk halaman*" if instauploads == 1:
                        s "Bagaimana dengan foto yang Anda ambil sebelumnya?"
                        b "Saya sudah mempostingnya"
                        s "Kualitas rendah?"
                        b "Ayo, kualitas kamera telepon sangat bagus saat ini"
                        s "Hmm, oke"
                        scene sroom_inst_photos with fade
                        b "Berubah menjadi sesuatu yang menyenangkan"
                        s "Seperti apa?"
                        b "Aku tidak tahu..."
                        menu:
                            "Mari kita coba sesuatu yang baru":
                                if srel >=50:
                                    jump realinstaphotos
                                else:
                                    pass
                                s "Ok tunggu di luar"
                                scene door with fade
                                "Dapatkan hubungannya lebih tinggi dari 50 poin"
                                "..."
                                s "Datang"
                                scene sroom_inst_photos4 with fade
                                b "Hmm, tidak buruk"
                                b "Coba pose lain"
                                scene sroom_inst_photos5 with dissolve
                                s "Sesuatu seperti ini?"
                                b "Cantik ya!"
                                scene sroom_inst_photos6 with dissolve
                                s "Oh [bname] Ayo!"
                                b "Aku bersumpah, melanjutkan!"
                                if srel >=17 and srel <=20:
                                    scene sroom_inst_photos7 with dissolve
                                    s "Bagaimana dengan ini?"
                                    b "Super cute"
                                    b "Lebih banyak lagi ..."
                                    s "No"
                                    pass
                                elif srel >=21:
                                    scene sroom_inst_photos7 with dissolve
                                    s "Bagaimana dengan ini?"
                                    b "Super cute"
                                    b "Lebih banyak lagi ..."
                                    s "Hmm"
                                    scene sroom_inst_photos9 with dissolve
                                    b "Bagus!"
                                    menu:
                                        "Minta dia untuk melakukan sesuatu yang sugestif":
                                            scene sroom_inst_photos_suggestive with dissolve
                                            s "Seperti apa?"
                                            b "Kami membutuhkan pengikut"
                                            b "Anda tahu seperti apa pria"
                                            s "Hmmm"
                                            scene sroom_inst_photos_suggestive1 with dissolve
                                            s "Seperti ini"
                                            b "Jangan begitu naif [sname]"
                                            b "Apakah Anda pikir foto seperti itu akan membuat Anda pengikut?"
                                            s "Duh! Saya tahu, tetapi saya punya satu jawaban untuk Anda"
                                            b "Apa?"
                                            scene sroom_inst_photos_suggestive2 with dissolve
                                            s "Dalam mimpimu"
                                            b "Ok apapun, tapi ubah saja sesuatu dalam pose Anda"
                                            b "Dengar, kenapa kamu tidak bersandar di meja itu di sana"
                                            s "Oke, tapi tidak ada game yang lucu"
                                            s "Anda mengambil foto dari samping"
                                            b "Ok"
                                            scene sroom_inst_photos_suggestive3 with fade
                                            b "Keren, sekarang lihat kamera"
                                            scene sroom_inst_photos_suggestive4 with dissolve
                                            b "Bagus, bisakah Anda mengangkat roknya sedikit?"
                                            b "Maksud saya pegang dengan tangan Anda yang lain"
                                            s "Tidak [bname], cukup untuk hari ini"
                                            s "Tolong pergi sekarang"
                                            scene door with fade
                                            b "{i} (...) {/i}"
                                            call screen gnav
                                        "Lagi?":

                                            if srel >=25 and srel <=35:
                                                s "Ok"
                                                s "Only one"
                                                scene sroom_inst_photos10 with dissolve
                                                b "Dingin"
                                                pass

                                            elif srel >35:
                                                s "Ok"
                                                s "Only one"
                                                scene sroom_inst_photos10 with dissolve
                                                b "Dingin"
                                                b "Ayo, satu lagi"
                                                scene sroom_inst_photos11 with dissolve
                                                s "Mhhmm"
                                                s "Ok"
                                                scene sroom_inst_photos12 with fade
                                                b "..."
                                                scene sroom_inst_photos13 with dissolve
                                                s "Bagus?"
                                                b "Yeah"
                                                scene sroom_inst_photos36 with dissolve
                                                b "Besar"
                                                b "Bisakah Anda berbalik dan meletakkan tangan di pinggul?"
                                                if srel >40:
                                                    scene sroom_inst_photos37 with dissolve
                                                    s "Seperti ini?"
                                                    b "Yeaaah, pegang di sana"
                                                    b "Biarkan saya mengambil pasangan"
                                                    scene sroom_inst_photos38 with dissolve
                                                    b "Hmmm"
                                                    pass
                                                else:
                                                    s "No"
                                                    pass
                                            else:

                                                s "No"
                                                pass
                                else:


                                    pass

                                scene sroom_inst_photos8 with dissolve
                                s "Cukup untuk hari ini"
                                b "Hmm Ok"
                                pass
            "Memasuki":


                if sburnt ==1:
                    jump sburn_study_enter
                else:
                    pass
                scene sroom_st5 with hpunch
                s "[bname] !! Apa yang salah denganmu?"
                b "Hai [sname], apa yang kamu lakukan?"
                s "Dengan serius!"
                b "Apa?"
                s "Anda masuk dan bertanya apa yang saya lakukan?"
                b "Jadi apa?"
                scene sroom_st7 with dissolve
                b "Saya melihat Anda membutuhkan bantuan untuk ini"
                s "Tidak, saya bisa mengelola"
                b "Oke, sesuai keinginan Anda"
                pass

        scene door with fade
        b "{i} (...) {/i}"
        call screen gnav

    elif Hour >=19 and Hour <20:
        $ Hour += 1
        scene door with fade
        b "{i} (sepertinya pintunya terbuka) {/i}"
        menu:
            "Ketukan":
                play sound "sounds/knock.ogg"
                if laptoprequested == 1 and sscall ==0:
                    b "Hmm"
                    b "{i}(I'll enter){/i}"
                    $ sscall = 1
                    scene sroom_scall with fade
                    if persistent.patch_enabled:
                        s "Yes dad"
                        pass
                    else:
                        s "Yes stewart"
                        pass
                    "..."
                    s "Tidak sebanyak itu ..."
                    scene sroom_scall1 with dissolve
                    s "Oke, terima kasih"
                    s "Kamu juga, bye"
                    b "Hmm"
                    scene sroom_scall2 with dissolve
                    s "Ya?"
                    b "Dengan siapa kamu berbicara?"
                    if persistent.patch_enabled:
                        s "Dad"
                    else:
                        s "Stewart"
                        pass

                    b "Hmm tidak, kamu tahu bahwa kita tidak diizinkan meneleponnya?"
                    s "Saya tidak meneleponnya"
                    b "Ah masa? Bagaimana dia tahu nomor Anda?"
                    b "Nomor Anda baru kan? Dia tidak tahu bahwa kamu sudah mendapatkannya"
                    scene sroom_scall3 with dissolve
                    s "Apa masalah Anda [bname]!?"
                    s "Apakah saya menelepon atau tidak?!"
                    if persistent.patch_enabled:
                        b "Tidak ada ... aku akan memberitahu ibu"
                        pass
                    else:
                        b "Tidak ada ... aku akan memberi tahu [mname]"
                        pass
                    s "Berlangsung! Katakan padanya"
                    b "Kami akan melihat"
                    scene sroom_scall2 with dissolve
                    s "Sebelum Anda memberitahunya ..."
                    s "Bolehkah saya tahu apa yang saya lakukan salah?"
                    b "Anda tahu bahwa [mname] tidak ingin kami menghubungi dia dengan benar?"
                    s "Ya tapi kadang -kadang dia meneleponmu"
                    b "Ini berbeda, saya tidak pernah memanggilnya"
                    s "Oh ... saya tidak tahu"
                    b "Jangan khawatir kita semua membuat kesalahan"
                    scene sroom_scall4 with dissolve
                    s "Terima kasih [bname]"
                    b "Baiklah, lihat yah"
                    scene door with fade
                    b "{i} (...) {/i}"
                    scene pdinner_m1 with fade
                    "..."
                    b "Saya pikir ada sesuatu yang harus Anda ketahui"
                    scene pdinner_m2 with dissolve
                    m "Apa maksudmu?"
                    b "[sname] sedang berbicara dengan Stewart"
                    m "Dan?"
                    b "Dia meminta uang kepadanya dan memberi tahu dia tentang situasi kami"
                    scene pdinner_m3 with dissolve
                    m "Apa!!"
                    b "Yeah"
                    scene pdinner_m4 with hpunch
                    "..."
                    scene pdinner_m5 with fade
                    "..."
                    m "Apakah kamu mengerti !!!"
                    "..."
                    s "Ya, saya minta maaf"
                    s "I'm sorry"
                    m "Lain kali saya akan mengambil telepon ini dan menghancurkannya!"
                    $ sbm = 1
                    b "Hmm"
                    b "Saatnya pergi"
                    scene door with fade
                    b "{i} (...) {/i}"
                    call screen gnav
                else:
                    pass
                s "Siapa itu?"
                b "It's me"
                s "Masuk, itu terbuka"
                scene sroom_st with fade
                b "Masih belajar?"
                scene sroom_st1 with dissolve
                s "Tidak, saya sudah selesai"
                if srel >=10:
                    scene sroom_st8 with dissolve
                    s "Saya akan pergi makan malam"
                    s "Sampai jumpa"
                    menu:
                        "Oke":
                            b "Ok"
                            scene door with fade
                            b "{i} (...) {/i}"
                            call screen gnav

                        "Beri dia tindikan" if spiercings == 2:
                            b "Aku punya sesuatu untukmu"
                            s "Apa itu?"
                            b "Piercings"
                            scene sroomst_gift1 with dissolve
                            s "Benar-benar!!"
                            b "Ya, silakan coba"
                            scene sroomst_gift1_1 with fade
                            s "Bagus?"
                            b "Yeah awesome"
                            scene sroomst_gift1_2 with hpunch
                            show screen srelup
                            $ spiercings = 3
                            $ srel += 2
                            s "Terima kasih [bname]"
                            hide screen srelup
                            b "Terima kasih kembali"
                            b "Aku akan melihatmu untuk makan malam"
                            scene door with fade
                            b "{i} (...) {/i}"
                            call screen gnav


                        "Tiket konser apa ini" if ticketrequested == 1:
                            b "Jadi untuk siapa konser itu?"
                            s "Taylor Shift"
                            b "Aha"
                            b "Apakah dia datang ke kota?"
                            s "Ya, segera"
                            $ ticketrequested = 2
                            b "Ok baik -baik saja"
                            b "Sampai jumpa"
                            scene door with fade
                            b "{i} (...) {/i}"
                            call screen gnav

                        "Apakah Anda ingin mengambil foto panas?" if elaine_convince == 4 and saction >=2 and srel>=100 and addedchoicerepeat <=3:
                            s "[bname] Saya tidak berminat sekarang"
                            $ addedchoicerepeat += 1
                            b "Anda akan berminat saat kami mendapatkan 1000 pengikut"
                            b "Oh ayolah!"
                            jump snameaddedchoice
                else:

                    s "Saya akan pergi makan malam"
                    s "Sampai jumpa"
                    menu:
                        "Oke":
                            b "Ok"
                            scene door with fade
                            b "{i} (...) {/i}"
                            call screen gnav

                        "Tiket konser apa ini" if ticketrequested == 1:
                            b "Jadi untuk siapa konser itu?"
                            s "Taylor Shift"
                            b "Aha"
                            b "Apakah dia datang ke kota?"
                            $ ticketrequested = 2
                            s "Ya, segera"
                            b "Ok baik -baik saja"
                            b "Sampai jumpa"
                            scene door with fade
                            b "{i} (...) {/i}"
                            call screen gnav
            "Memasuki":

                if laptoprequested == 1 and sscall ==0:
                    $ sscall = 1
                    scene sroom_scall with fade
                    if persistent.patch_enabled:
                        s "Yes dad"
                        pass
                    else:
                        s "Yes stewart"
                        pass
                    "..."
                    s "Tidak sebanyak itu ..."
                    scene sroom_scall1 with dissolve
                    s "Oke, terima kasih"
                    s "Kamu juga, bye"
                    b "Hmm"
                    scene sroom_scall2 with dissolve
                    s "Ya?"
                    b "Dengan siapa kamu berbicara?"
                    if persistent.patch_enabled:
                        s "Dad"
                    else:
                        s "Stewart"
                        pass

                    b "Hmm tidak, kamu tahu bahwa kita tidak diizinkan meneleponnya?"
                    s "Saya tidak meneleponnya"
                    b "Ah masa? Bagaimana dia mendapatkan nomor Anda?"
                    b "Nomor Anda baru kan? Dia tidak tahu bahwa kamu sudah mendapatkannya"
                    scene sroom_scall3 with dissolve
                    s "Apa masalah Anda [bname]!?"
                    s "Apakah saya menelepon atau tidak?!"
                    if persistent.patch_enabled:
                        b "Tidak ada ... aku akan memberitahu ibu"
                        pass
                    else:
                        b "Tidak ada ... aku akan memberi tahu [mname]"
                        pass
                    s "Berlangsung! Katakan padanya"
                    b "Kami akan melihat"
                    scene sroom_scall2 with dissolve
                    s "Sebelum Anda memberitahunya ..."
                    s "Bolehkah saya tahu apa yang saya lakukan salah?"
                    b "Anda tahu bahwa [mname] tidak ingin kami menghubungi dia dengan benar?"
                    s "Ya tapi kadang -kadang dia meneleponmu"
                    b "Ini berbeda, saya tidak pernah memanggilnya"
                    s "Oh ... saya tidak tahu"
                    b "Jangan khawatir kita semua membuat kesalahan"
                    scene sroom_scall4 with dissolve
                    s "Terima kasih [bname]"
                    b "Baiklah, lihat yah"
                    scene door with fade
                    b "{i} (...) {/i}"
                    scene pdinner_m1 with fade
                    "..."
                    b "Saya pikir ada sesuatu yang harus Anda ketahui"
                    scene pdinner_m2 with dissolve
                    m "Apa maksudmu?"
                    b "[sname] sedang berbicara dengan Stewart"
                    m "Dan?"
                    b "Dia meminta uang kepadanya dan memberi tahu dia tentang situasi kami"
                    scene pdinner_m3 with dissolve
                    m "Apa!!"
                    b "Yeah"
                    scene pdinner_m4 with hpunch
                    "..."
                    scene pdinner_m5 with fade
                    "..."
                    m "Apakah kamu mengerti !!!"
                    "..."
                    s "Ya, saya minta maaf"
                    s "I'm sorry"
                    m "Lain kali saya akan mengambil telepon ini dan menghancurkannya!"
                    $ sbm = 1
                    b "Hmm"
                    b "Saatnya pergi"
                    scene door with fade
                    b "{i} (...) {/i}"
                    call screen gnav
                else:

                    pass
                scene sroom_st5 with hpunch
                b "Masih belajar?"
                s "Apa yang salah denganmu?"
                b "Hanya memeriksa Anda"
                s "Dengan serius!"
                b "Apa?"
                s "Anda masuk dan mengatakan bahwa Anda sedang memeriksa saya!?"
                b "Jadi apa?"
                if srel >=10:
                    scene sroom_st9 with dissolve
                    s "Please go"
                    menu:
                        "Oke":
                            b "Ok"
                            scene door with fade
                            b "{i} (...) {/i}"
                            call screen gnav

                        "Tiket konser apa ini" if ticketrequested == 1:
                            b "Jadi untuk siapa konser itu?"
                            s "Taylor Shift"
                            b "Aha"
                            b "Apakah dia datang ke kota?"
                            $ ticketrequested = 2
                            s "Ya, segera"
                            b "Ok baik -baik saja"
                            b "Sampai jumpa"
                            scene door with fade
                            b "{i} (...) {/i}"
                            call screen gnav
                else:

                    s "Keluar saja"
                    s "Please"
                    menu:
                        "Oke":
                            b "Ok"
                            scene door with fade
                            b "{i} (...) {/i}"
                            call screen gnav

                        "Tiket konser apa ini" if ticketrequested == 1:
                            b "Jadi untuk siapa konser itu?"
                            s "Taylor Shift"
                            b "Aha"
                            b "Apakah dia datang ke kota?"
                            $ ticketrequested = 2
                            s "Ya, segera"
                            b "Ok baik -baik saja"
                            b "Sampai jumpa"
                            scene door with fade
                            b "{i} (...) {/i}"
                            call screen gnav


    elif Hour >=21:
        scene door with fade
        b "{i}(It's locked){/i}"
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
