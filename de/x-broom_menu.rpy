



label broom_menu:
    if Hour >=9 and Hour <18:
        if startnework >= 1 and mbunknown >=1 and stewartcalled ==0:
            jump stewartcall

        elif bworkstarted == 1 and elaineagain >= 1 and melmilin ==0 and day ==1:
            $ melmilin = 1
            jump meldanbtalk

        elif bworkstarted == 1 and elaineagain >= 1 and melmilin ==0 and day ==2:
            $ melmilin = 1
            jump meldanbtalk

        elif bworkstarted == 1 and beachalone >= 1 and melmilin ==0 and day ==2:
            $ melmilin = 1
            jump meldanbtalk

        elif bworkstarted == 1 and elaineagain >= 1 and melmilin ==0 and day ==3:
            $ melmilin = 1
            jump meldanbtalk

        elif bworkstarted == 1 and elaineagain >= 1 and melmilin ==0 and day ==3:
            $ melmilin = 1
            jump meldanbtalk

        elif bworkstarted == 1 and beachalone >= 1 and melmilin ==0 and day ==3:
            $ melmilin = 1
            jump meldanbtalk

        elif bworkstarted == 1 and elaineagain >= 1 and melmilin ==0 and day ==4:
            $ melmilin = 1
            jump meldanbtalk

        elif bworkstarted == 1 and beachalone >= 1 and melmilin ==0 and day ==4:
            $ melmilin = 1
            jump meldanbtalk

        elif cherylintro ==1 and cherylintrodone ==0:
            $ cherylintrodone = 1
            scene black
            "SEMENTARA ITU"
            scene cherintro with fade
            c "..."
            d "Hi sis"
            scene cherintro1 with dissolve
            c "Hi Stewart"
            d "Saya butuh bantuan Anda"
            c "Apakah ini tentang [mname]"
            scene cherintro2 with dissolve
            d "Ya, bisakah Anda berbicara dengannya"
            scene cherintro3 with dissolve
            c "Oke, saya akan menelepon [bname] dan mencoba menemukannya"
            pass

        elif meldan == 3 and elaine_convince == 4 and day ==7:
            jump mdanlabel2
        else:

            if ebizcheck <= -3 and ebizaldoneonce >= 1 and e_showsupagain <2:
                scene callelaine0 with fade
                play sound "sounds/mobilering.wav"
                b "{i} huh! Elaine Calling {/i}"
                scene callelaine with dissolve
                stop sound
                e "Hi [bname]"
                b "Hi"
                $ e_showsupagain = 1
                e "Mengapa Anda tidak menelepon saya?"
                e "Tidakkah kamu ingin uang?"
                b "Sebenarnya, saya tidak bisa mengeluarkan mereka dari rumah baru -baru ini"
                b "{i} Saya tidak bisa memberitahunya bahwa tidak layak untuk uang yang saya dapatkan {/i}"
                e "Nah, Anda harus melakukannya"
                b "{i} atau mungkin saya harus {/i}"
                e "Saya memiliki sesuatu yang istimewa dan saya membutuhkan kamar secepatnya"
                b "Hmmm"
                b "Mari kita bicara saat Anda datang"
                e "Errm Ok"
                b "Sampai jumpa"
                menu:
                    "Persetan dia, aku tidak punya waktu untuknya sekarang":
                        "Jangan sering lakukan ini jika Anda ingin melanjutkan dengan [mname] cerita"
                        "Itu menunda Elaine meyakinkannya untuk mengubah pekerjaannya"
                        "Apakah Anda yakin ingin melanjutkan ini"
                        menu:
                            "Tidak, saya telah mengubah pikiran":
                                pass
                            "Ya lanjutkan, saya tidak ingin Elaine menelepon saya sekarang":
                                $ ebizcheck = 6
                                $ e_showsupagain = 2
                                pass
                    "Kenapa tidak, mungkin aku mendapatkan sesuatu dengannya":

                        pass
            else:


                pass

        "..."
        if bgmt ==1 and elfllowup ==0:
            scene melta with fade
            "SEMENTARA ITU"
            $ elfllowup = 1
            ml "Bagaimana [mname] Adam"
            mb "Semuanya terkendali saat Anda meminta ma \ 'am"
            ml "Apakah dia menerima?"
            mb "Belum, aku belum memberitahunya"
            ml "Apa yang kamu tunggu?"
            mb "Anda menyuruh saya untuk melakukannya dengan lambat dengannya, dia yang sulit"
            ml "Kami tidak bisa menahannya begitu lama untuk ini"
            ml "Jika Anda tidak bisa melakukannya, saya akan berbicara dengannya"
            mb "Saya bisa memberi saya beberapa hari"
            ml "All right"
            scene melta1 with dissolve
            dn "Jadi ada apa dengan [mname]?"
            ml "Nothing dear"
            ml "Apakah Anda ingin pergi ke pantai?"
            dn "Yes sure"
            scene melta2 with fade
            dn "Tempat yang bagus"
            scene black
            "..."
            pass

        elif elfllowup == 1:
            $ elfllowup = 2
            $ Hour += 1
            scene callelaine0 with fade
            play sound "sounds/mobilering.wav"
            b "{i} huh! Elaine Calling {/i}"
            scene callelaine with dissolve
            stop sound
            e "Hi [bname]"
            b "Hi"
            e "Apa yang terjadi denganmu?"
            b "Saya berbicara dengan Cheryl dan ..."
            e "Mari kita bertemu dan Anda memberi tahu saya segalanya"
            b "Ok saya akan datang"
            e "Bukan ke tempat saya, mari kita bertemu di pantai"
            b "Telanjang?"
            e "Yes whatever"
            b "Keren, sampai jumpa"
            jump elfup
        else:
            pass
        scene broom_day with fade
        b "Hmmm"
        b "Apa yang harus dilakukan sekarang?"
        menu:
            "Belajar" if bstudied <2:
                $ Hour += 1
                $ bstudy += 1
                $ bstudied += 1
                scene bcourse with fade
                b "Hmm bagus"
                pass
            "Latihan":

                scene bexer with fade
                $ Hour += 1
                $ bexercise += 1
                "..."
                if srel >= 450:
                    scene bexer2 with dissolve
                    s "Hmmm"
                    scene bexer3 with dissolve
                    if day ==1 and s_bbruises >=1:
                        b "Aduh!"
                        b "Turun!"
                        scene bexerb with dissolve
                        b "Saya masih kesakitan"
                        jump sbtlc

                    elif day ==3 and s_bbruises >=1:
                        b "Aduh!"
                        b "Turun!"
                        scene bexerb with dissolve
                        b "Saya masih kesakitan"
                        jump sbtlc

                    elif day ==5 and s_bbruises >=1:
                        b "Aduh!"
                        b "Turun!"
                        scene bexerb with dissolve
                        b "Saya masih kesakitan"
                        jump sbtlc
                    else:

                        pass
                    $ persistent.unlock_25 = True
                    b "Hah!"
                    b "Turun!"
                    scene bexer4 with dissolve
                    b "Hai!"
                    b "Hentikan!"
                    s "Hahahah"
                    scene bexer5 with vpunch
                    "..."
                    scene bexer6 with fade
                    "..."
                    scene bexer7 with dissolve
                    b "Grrr"
                    s "Ahhahah"
                    scene bexer6 with dissolve
                    b "Jangan pernah ..."
                    scene bexer7 with dissolve
                    b "... lakukan itu lagi"
                    scene bexer8 with dissolve
                    s "Apakah itu yang terbaik?"
                    $ sbexerrepeat += 1
                    menu:
                        "Bawa dia ke dinding":
                            scene bexer9 with dissolve
                            s "Ahh"
                            scene bexer10 with dissolve
                            b "Sungguh!"
                            scene bexer11 with dissolve
                            s "Ahhh"
                            scene bexer12 with dissolve
                            b "Ahhhhh"
                            scene bexer13 with fade
                            s "Persetan denganmu"
                            b "Hehehe"
                            scene broom_day with fade
                            "..."
                            jump broom_menu

                        "Lakukan di sini" if bexercise >=50 and sbexerrepeat >=3:
                            scene bexer14 with dissolve
                            s "Ahahaha"
                            scene bexer15 with dissolve
                            s "Hah!"
                            scene bexer16 with dissolve
                            s "Ahhh"
                            scene bexer17 with dissolve
                            s "[bname]! Berhenti! Itu menyakitkan"
                            s "Please"
                            menu:
                                "Cobalah untuk mendorong lebih banyak":
                                    scene bexer18 with dissolve
                                    s "Ahhhh"
                                    scene bexer18a with dissolve
                                    s "BERHENTI!"
                                    scene bexer19a with dissolve
                                    "..."
                                    scene bexer19 with fade
                                    s "Persetan denganmu"
                                    b "Hehehe"
                                    scene broom_day with fade
                                    "..."
                                    jump broom_menu
                                "Oke, saya akan berhenti tapi ...":

                                    b "Saya ingin Anda menyedotnya"
                                    scene bexer20 with fade
                                    s "Apakah kamu serius?"
                                    b "Ya, lakukan dengan pilihan"
                                    b "Or else"
                                    scene bexer21 with dissolve
                                    b "Bagaimana rasanya?"
                                    scene bexer22 with dissolve
                                    "..."
                                    scene bexer23 with fade
                                    b "Ahhh"
                                    scene broom_day with fade
                                    "..."
                                    jump broom_menu
                else:
                    pass
                scene bexer1 with fade
                b "Bagus!"
                scene black with fade
                "..."
                jump broom_menu

            "Hubungi Melinda" if callmel == 1 and melvisit == 0:
                $ melvisit = 1
                scene callelaine with dissolve
                ml "Hi [bname]"
                $ Hour += 1
                b "Hi"
                b "Anda menyuruh saya menelepon Anda"
                ml "Ya, bisakah Anda datang ke alamat ini?"
                b "Ok"
                jump melvisitr


            "Pergi untuk menguntit Melinda dan Cheryl" if bnamefixcheryl ==4 and stalkdone ==0:
                $ stalkdone = 1
                $ Hour += 1
                jump stalkmelch

            "Pergi bekerja untuk Daniel" if bworkstarted == 1 and bworked == 0:
                $ bworked = 1
                $ Hour += 2
                jump bworkday

            "Cari bantuan untuk menghentikan Cheryl menelepon Stewart" if bnamefixcheryl ==1:
                b "{i} Mungkin Elaine dapat membantu?! {/i}"
                b "{i} i \ 'll panggil dia {/i}"
                scene callelaine with dissolve
                e "Hi [bname]"
                b "Hi"
                e "Apa yang salah?"
                b "Saya butuh bantuan Anda, bisakah kami bertemu?"
                e "Sekarang?!"
                b "Ya jika memungkinkan"
                e "Baiklah, datang ke alamat ini"
                jump meetelaineforhelp

            "Hubungi Elaine untuk memeriksa bantuannya dengan Cheryl" if bnamefixcheryl >=2 and bnamefixcheryl <=3:
                scene callelaine with dissolve
                e "Hi [bname]"
                $ Hour += 1
                b "Hi"
                b "Ada berita?"
                e "Saya tidak tahu tetapi saya sedang memikirkan sesuatu"
                b "Apa itu?"
                e "Temui aku di rumah setelah dan jam"
                b "Ok"
                jump meetelaineforhelp1


            "Periksa [sname] halaman dan unggah gambar jika ada" if pagecheckdone ==0 and instauploads == 1:
                scene binsta3 with fade
                $ Hour += 1
                "..."
                scene binsta4 with dissolve
                $ pagecheck += 1
                $ pagecheckdone = 1
                if pagecheck >=3:
                    if nude_binsta_random1_posted ==0:
                        pass
                    else:
                        if snameinstaconvinced ==0:
                            $ snameinstaconvinced = 1
                            b "Hmmm"
                            b "Definitely better"
                            b "Saya akan menelepon [sname]"
                            scene binstas3 with fade
                            b "Jadi..."
                            b "Saya telah melakukan sedikit percobaan"
                            b "Untuk melihat reaksi para pengikut"
                            s "Dan..."
                            b "Saya telah memposting foto ini"
                            b "Sekarang jangan marah, saya sudah bilang itu percobaan"
                            s "Tunjukkan fotonya"
                            scene binsta_random1 with dissolve
                            b "Yang ini!"
                            s "[bname] !! Apakah Anda memposting foto telanjang di halaman saya!"
                            scene binstas3 with dissolve
                            b "Tunggu sebentar, biarkan aku selesai"
                            b "Foto itu memberi kami 30 pengikut"
                            scene binstas4 with dissolve
                            s "Saya tidak peduli menghapusnya sekarang"
                            s "Saya lebih suka mendapatkan pengikut asli yang tertarik pada saya, bukan pada gadis lain"
                            b "Ya, saya setuju"
                            b "Tetapi Anda harus melakukan foto yang sama dengan gadis ini"
                            s "Orang cabul!"
                            scene binstas5 with dissolve
                            b "Pfff dia pergi"
                            b "Saya akan menghapusnya"
                            b "Tapi pikirkan tentang apa yang saya katakan"
                            s "Orang cabul!"
                            scene broom_day with fade
                            "..."
                            jump broom_menu
                        else:

                            pass



                    b "Tidak bagus!"
                    b "Saya pikir saya perlu membeli pengikut untuk halamannya"
                    b "Mari kita lihat berapa biayanya"
                    scene binsta5 with dissolve
                    b "Apakah kamu serius!"
                    b "000 untuk 500 pengikut?"
                    b "Damn"
                    b "Tidak perlu sekarang"
                    if pagecheck >=4 and nude_binsta_random1_posted ==0:
                        b "{i} Tunggu, saya punya ide brilian {/i}"
                        menu:
                            "Cari Gadis Telanjang Online":
                                scene binsta4 with dissolve
                                b "Mari kita lihat apa yang kita punya"
                                scene binsta_random with dissolve
                                b "Nah, saya tidak ingin dengan wajah"
                                b "Saya perlu meyakinkannya secara bertahap"
                                scene binsta_random1 with dissolve
                                b "Terlihat bagus, mari kita simpan"
                                scene binsta4 with dissolve
                                b "Saatnya mempostingnya di halamannya"
                                "..."
                                "..."
                                b "Dingin"
                                $ nude_binsta_random1_posted = 1
                                b "Sekarang kita tunggu, saya akan memeriksa besok dan melihat hasilnya"
                                scene black with fade
                                "..."
                                jump broom_menu

                    if pagecheck >=4 and nude_binsta_random1_posted ==1:
                        menu:
                            "Beli pengikut" if bought_followers == 0 and mny >= 500:
                                $ bought_followers = 1
                                $ mny -= 500
                                pass
                            "Melanjutkan":
                                pass
                    else:



                        b "{i} Saya perlu memeriksa ini besok dan mencari sesuatu {/i}"
                        pass
                else:
                    b "Done"
                    b "{i} Saya perlu terus memeriksa ini setiap hari {/i}"
                    pass
                scene black with fade
                "..."
                jump broom_menu

            "{b} hubungi Elaine {/b}" if cselaine0 == 9 and Hour ==15:
                scene callelaine with fade
                $ Hour += 1
                b "Hi"
                e "{i}Hi [bname]{/i}"
                $ cselaine0 = 10
                e "{i} Apakah Anda berhasil mengeluarkannya {/i}"
                b "Berbuat salah..."
                b "Ya ... aku akan pergi sekarang ke kamarnya dan memberinya tiket"
                e "{i} Bagus, aku akan berada di sana 17:00 Sharp {/i}"
                b "Bagus, sampai jumpa"
                scene black with fade
                "..."
                jump broom_menu

            "{b} Saya perlu memanggil Elaine untuk merekam sesuatu pada kamera itu {/b}" if camerafixing == 2 and Hour ==15 and elaine_convince == 0 and workrequest ==3 and day !=7:
                b "{i} Saya harus membuatnya meyakinkan [mname] tentang pekerjaan baru {/i}"
                scene callelaine with fade
                $ ebizcheck = 0
                $ Hour += 1
                b "Hi there"
                e "{i}Hi [bname]{/i}"
                $ cselaine0 = 10
                b "Apakah Anda ingin menggunakan kamar saya?"
                e "Tentu saja, saya selalu memiliki bisnis"
                b "Dingin"
                e "{i} dapatkah Anda mengelola untuk mengeluarkannya {/i}"
                b "Berbuat salah..."
                b "Ya ... Saya akan menyingkirkan [sname]"
                e "{i} Bagus, aku akan berada di sana 17:00 Sharp {/i}"
                b "Bagus, sampai jumpa"
                scene bporn with fade
                b "{i} (tidak ada waktu untuk menjalankan dan membeli tiket sekarang) {/i}"
                b "{i} (Saya akan membelinya secara online) {/i}"
                $ mny -= 25
                b "{i} (hebat i \ \ 'll pergi dan temukan [sname]) {/i}"
                scene black with fade
                "..."
                jump broom_menu

            "{b} Temukan tempat untuk memperbaiki kamera {/b}" if camerafixing == 1:
                scene broom_day with fade
                b "{i}Hmm{/i}"
                $ camerafixing = 2
                b "{i} di mana harus memperbaikinya? {/i}"
                b "{i}Found it{/i}"
                scene broom_camera with dissolve
                "..."
                b "{i} let \ 's mengujinya {/i}"
                scene broom_camera1 with dissolve
                "..."
                scene camera_angle with fade
                b "{i}Perfect{/i}"
                scene black with fade
                "..."
                jump broom_menu
            "{b} buka internet {/b}":


                call screen inthelp











            "{b} Panggil Rowena {/b}" if contactrowena ==1 and Hour ==12:
                b "{i} mari kita lihat apakah kedipannya sengaja {/i}"
                scene callelaine with fade
                $ Hour += 1
                b "Hi"
                a "{i}Hi [bname]{/i}"
                b "Jadi bagaimana kabarmu?"
                scene rcall1d with dissolve
                a "Tidak terlalu baik"
                b "{i} mengapa? {/i}"
                a "Tidak ada ... Saya hanya bertengkar besar dengan pacar brengsek saya"
                b "{i} wow! Apakah Anda menangis {/i}"
                a "No"
                a "Bisakah Anda membawa [sname] dan datang?"
                b "{i}Hmm{/i}"
                b "Sure"
                scene black with fade
                "..."
                scene rcall2d with fade
                s "Uhuh! Jelas, mengerti"
                scene black with fade
                "..."
                scene rcall3d with dissolve
                b "{i} Apa yang harus dilakukan? {/i}"
                menu:
                    "Ambil [sname] dan pergi":
                        jump rowenavisit
                    "Pergi sendiri":

                        jump rowenalone

            "{b} Panggil Rowena {/b}" if rkiss >2 and Hour ==13:
                scene rcall with dissolve
                $ Hour += 1
                b "Halo!"
                b "Apa yang sedang kamu lakukan?"
                a "{i}Nothing{/i}"
                scene rcall1 with fade
                b "{i} Saya perlu berbicara dengan Anda {/i}"
                a "Ok"
                b "{i} Bisakah saya datang {/i}"
                a "Sekarang?"
                b "{i} Ya! {/i}"
                a "Ok"
                b "Ok saya akan berada di sana"
                jump rbffightrp

            "{b} hubungi Rowena 's Mom {/b}" if rowena_mom_number ==1 and Hour >=12 and Hour <15:
                $ rowena_mom_called = 1
                scene rcall with dissolve
                b "Halo!"
                b "Anda menyuruh saya menelepon Anda"
                rm "{i} [bname]? {/i}"
                b "Yes"
                rm "{i}Yeah{/i}"
                scene row_mom_visit with fade
                b "{i} Saya perlu berbicara dengan Anda {/i}"
                rm "Bisakah Anda datang, periksa mesin cuci saya?"
                b "{i} mesin cuci? Saya bisa memperbaiki hal -hal seperti itu {/i}"
                rm "Tolong datang dan lihat saja"
                b "{i} ok! Saya akan segera ke sana {/i}"
                jump rmvisit




            "{b} hubungi Rowena tentang Nude Beach {/b}" if browenabm == 1 and Hour <=14:
                b "{i} mari kita lihat apakah dia menerima untuk melakukan ini {/i}"
                scene callelaine with fade
                $ Hour += 1
                $ browenabm = 2
                b "Hi"
                a "{i}Hi [bname]{/i}"
                b "Jadi bagaimana kabarmu?"
                scene rcall1d with dissolve
                a "Tidak terlalu baik"
                a "Tapi bagaimanapun juga"
                b "{i} baik -baik saja, jadi saya menelepon Anda tentang apa yang terjadi di pantai {/i}"
                scene rorgybw with fade
                a "Yeah"
                scene rcall1d with dissolve
                a "Bagaimana dengan itu?"
                b "{i}Hmm{/i}"
                b "{i} Saya berpikir jika kami dapat menemukan cara untuk menipu [sname] untuk memiliki pesta, kami berempat {/i}"
                a "Wow!"
                a "Bagaimana Anda ingin saya melakukan itu?"
                b "Saya tidak tahu mungkin mengatakan kepadanya bahwa Anda akan memberi tahu [mname] tentang pantai telanjang"
                b "Or something"
                a "Oke, keren, saya akan mencobanya"
                scene callelaine with dissolve
                b "Hebat, terima kasih"
                scene rcall1d with dissolve
                b "{i} sampai jumpa {/i}"
                scene rcall1ds with dissolve
                a "Sampai jumpa"
                scene rcall1ds1 with dissolve
                s "Jadi!"
                a "Sepertinya Anda telah memenangkan taruhan"
                s "Dimana uang saya"
                a "Here"
                s "Saya tahu dia akan meminta ini"
                s "Thanks"
                scene rcall1ds2 with dissolve
                s "Peraturan Gadis!"
                scene rcall1ds3 with dissolve
                s "{i} mungkin saya bisa menggunakan ini untuk keuntungan saya {/i}"
                s "{i} Suatu hari saya akan {/i}"
                scene black
                "..."
                scene broom_day with fade
                b "{i} Saya bertanya -tanya di mana [sname] {/i}"
                b "{i}Anyways{/i}"
                call screen gnav


            "{b} periksa kamera aula untuk melihat apa yang terjadi dengan Rob {/b}" if hallcamera >=2 and robmvisit >= 1:
                scene camerarob0 with fade
                "..."
                scene camerarob with fade
                b "..."
                scene camerarob1 with fade
                b "Wow"
                scene camerarob2 with fade
                b "Sial, dia menghancurkannya"
                scene camerarob3 with dissolve
                b "Sialan apakah itu segalanya?"
                b "Mungkin kami pergi di sini"
                call screen gnav


            "{b} periksa kamera aula {/b}" if hallcamera >=2 and gnight >=4 and hallcamerachecked ==0:
                $ hallcamerachecked = 1
                scene binsta4 with dissolve
                b "Hmmm"
                scene checkcamera with dissolve
                b "..."
                scene checkcamera1 with dissolve
                "..."
                scene checkcamera2 with dissolve
                s "Hi [bname]"
                if srel >=250:
                    scene checkcamera3 with dissolve
                    s "Ewww"
                    s "Apa yang kamu tonton?"
                    s "Porno pasti!"
                    b "Tidak ada bisnis Anda"
                    s "Ok"
                    if persistent.patch_enabled:
                        s "Saya akan memberi tahu ibu"
                        pass
                    else:
                        s "Saya akan memberi tahu [mname]"
                        pass
                    b "Tunggu tolong jangan"
                    scene checkcamera5 with dissolve
                    s "Hmmm"
                    s "Saya butuh 00 dan mengambil foto Anda"
                    b "All right"
                    s "Hmmm"
                    s "Naked"
                    b "No problem"
                    scene checkcamera6 with dissolve
                    $ bphotonaked = 1
                    b "Ayo, ambil foto sialan itu"
                    s "Done"
                    s "Dan uangnya"
                    $ mny -=100
                    b "Di sini ambillah"
                    b "Ada lagi?"
                    if srel >=350:
                        s "Berbaring di lantai"
                        s "Di punggung Anda"
                        scene checkcamera7 with fade
                        b "Apa sekarang?"
                        scene checkcamera8 with dissolve
                        s "Wait"
                        scene checkcamera9 with dissolve
                        b "Apa?"
                        scene checkcamera10 with hpunch
                        b "Ahh"
                        scene checkcamera11 with dissolve
                        s "..."
                        scene checkcamera10 with dissolve
                        b "Apa yang sedang kamu lakukan?"
                        scene checkcamera12 with dissolve
                        s "..."
                        scene checkcamera13 with dissolve
                        s "Ya makanlah, itu tempatmu"
                        scene checkcamera14 with dissolve
                        s "Selamat tinggal, nikmati"
                        scene broom_day with fade
                        b "{i} itu bagus, saya akan pergi mandi {/i}"
                        call screen gnav
                    else:

                        s "Tidak, bye"
                        scene broom_day with fade
                        b "{i}Bitch{/i}"
                        call screen gnav
                else:
                    s "Ewww"
                    scene checkcamera4 with dissolve
                    s "Pervert"
                    b "..."
                    s "Saya keluar"
                    scene broom_day with fade
                    b "{i} terima kasih Tuhan dia pergi {/i}"
                    call screen gnav

                if persistent.patch_enabled:
                    b "Hi dad"
                    pass
                else:
                    b "Hi Stewart"
                    pass
            "Periksa foto yang telah Anda unduh dari telepon Daniel" if dphonestolen >=1:
                scene danielphone with dissolve
                b "Wow"
                scene danielphone1 with dissolve
                b "{i} aha! Jadi ... {/i}"
                scene danielphone2 with dissolve
                b "Saya sekarang yakin mereka dalam hubungan sialan"
                b "Hanya itu yang saya dapatkan yang membuktikan sesuatu"
                pass
            "kembali":
                scene broom_day with fade
                "..."
                call screen gnav

        scene broom_day with fade
        "..."
        call screen gnav

    elif Hour >=18 and Hour <21:
        if sgoestost == 1:
            scene black
            $ sgoestost = 2
            scene stch
            d "Dimana disini !!?"
            d "Anda tidak bisa serius"
            d "Baiklah beri saya 10 menit saya akan terbuka untuk Anda"
            scene stst with fade
            if persistent.patch_enabled:
                s "Ayah!!!"
                pass
            else:
                s "Hai!"
                pass
                scene stst1 with hpunch
                s "Aku merindukanmu"
                scene stst2 with fade
                d "Apa yang merindukanku, kita berbicara hampir setiap hari"
                s "Ya tapi sebenarnya lebih baik"
                scene stst3 with dissolve
                "..."
                d "Jadi tentang apa ini?"
                s "Saya pikir sudah saatnya Anda datang dan mengakhiri apa yang terjadi"
                s "Bawa kami kembali ke sini"
                d "Apa maksudmu?"
                s "Sit"
                scene black
                "..."
                scene stst4 with fade
                d "Wow! Semua ini terjadi dalam waktu singkat ini"
                s "Yes"
                scene stst5 with dissolve
                s "Itulah mengapa Anda harus datang dan membawa kami semua kembali"
                scene stst6 with dissolve
                d "Hey kemana kamu pergi?"
                s "Saya merindukan tempat itu"
                scene stst7 with dissolve
                d "Saya berharap ini bodoh tidak ada di kamar saya"
                s "Ha!!!"
                d "Damn"
                scene stst8 with dissolve
                s "Siapa ini!?"
                d "Dia seorang gadis yang saya berikan pelajaran"
                d "In mathematics"
                s "..."
                scene black
                "SEMENTARA ITU"
                scene hevening with fade
                "..."
                scene nheveningmelsw with dissolve
                b "Hi"
                b "Bagaimana?"
                m "Nanti [bname] saya perlu mandi dan bersantai"
                scene room3 with fade
                b "Kamu tidak apa apa?"
                b "Bisakah saya masuk?"
                m "Yes"
                scene stst9 with fade
                m "[bname] Saya tidak mengatakan Anda bisa masuk"
                m "Saya bilang ya saya ok ok"
                b "Err sorry"
                m "Pergi ke dapur dan hubungi [sname]"
                m "Saya akan datang dan menyiapkan makan malam"
                b "Dia tidak di sini"
                m "Dia sering keluar akhir -akhir ini"
                m "Pokoknya, tunggu saya"
                scene stst10 with fade
                m "Come Taste My Soup"
                scene stst11 with fade
                b "Itu bagus"
                m "..."
                b "Apa yang Anda pikirkan"
                m "Saya bertanya -tanya di mana [sname]"
                b "Mari kita minum dan menonton TV sampai dia datang"
                scene stst12 with fade
                m "Ya Tuhan [bname] selalu ini!"
                b "Ya saya menyukainya"
                m "Lebih baik Anda memberi saya pijat kaki daripada omong kosong ini"
                b "Ok"
                scene stst13 with fade
                m "Itu bagus"
                m "Saya pikir saya akan tidur"
                scene stst14 with dissolve
                m "Selamat malam"
                menu:
                    "Bergerak":
                        scene stst15 with dissolve
                        "..."
                        if mrel >= 400:
                            scene stst14 with dissolve
                            m "Ayo saya memiliki sesuatu untuk ditunjukkan kepada Anda"
                            scene stst16 with fade
                            b "Apa itu?"
                            m "Sepatu hak baru untuk bekerja"
                            scene stst17 with fade
                            b "Bagus"
                            scene stst18 with fade
                            m "Kunci pintu dan datang memijat saya"
                            m "Pertama Beri Saya Minuman"
                            scene stst19 with fade
                            b "Here"
                            m "Apa itu?"
                            b "Tequila"
                            m "Ok thanks"
                            scene stst20 with fade
                            "..."
                            scene stst21 with dissolve
                            m "[bname] Apa?"
                            b "Anda berbau harum"
                            if mrel >= 450:
                                pass
                            elif mfuckedsober >=1:
                                pass
                            else:
                                m "Terima kasih tapi saya lelah karena pekerjaan"
                                m "Tolong cukup, tidurlah"
                                b "Ok seperti yang Anda inginkan"
                                jump newdays

                            scene stst22 with dissolve
                            m "Ah"
                            scene stst23 with fade
                            "..."
                            scene stst24 with vpunch
                            b "Bangunlah di sini"
                            m "Ah"
                            scene ramm
                            play sound "sounds/mslide.wav"
                            m "[bname] condom"
                            "..."
                            stop sound
                            m "Ahh"
                            play sound "sounds/mpant2.wav"
                            "..."
                            stop sound
                            scene stst25 with dissolve
                            m "Ahh"
                            scene stst26 with dissolve
                            b "Selamat malam"
                            m "Selamat malam! Anda menghancurkan pantat saya"
                            jump newdays
                        else:

                            m "..."
                            scene stst14 with dissolve
                            m "Selamat malam sayang"
                            jump newdays
                    "Jangan":
                        "..."
                        jump newdays

        elif bbm == 1:
            scene black
            $ bbm = 2
            "SEMENTARA ITU"
            scene mdanb with fade
            ml "Bagaimana harimu sayang?"
            dn "Tidak buruk"
            ml "Apakah kamu makan?"
            dn "No"
            dn "Dengarkan Saya memiliki permintaan yang tidak biasa"
            dn "Tapi itu ada di pikiran saya untuk waktu yang lama"
            ml "Apa itu?"
            dn "Err saya selalu menginginkan threesome"
            dn "Bisakah kita..."
            scene mdanb1 with dissolve
            ml "..."
            dn "Saya minta maaf, lupakan saja bahwa saya ..."
            ml "Saya baru saja terkejut"
            ml "Anda tidak harus menyesal, saya pikir Anda ..."
            dn "Saya lakukan, tetapi saya merasa harus melakukan ini untuk Anda, jadi Anda tidak bosan"
            ml "Ok saya akan menemukan pria untuk kami"
            dn "Berbuat salah..."
            dn "{i} fuck aku tidak berarti threesome dengan seorang pria {/i}"
            dn "Ok"
            scene black
            "KEMBALI"
            pass

        elif bbm == 2:
            scene black
            $ bbm = 3
            "SEMENTARA ITU"
            scene mdanb2 with fade
            dn "Huh"
            dn "Siapa itu?"
            dn "Rob, seseorang yang bisa kita percayai"
            r "Hi Daniel"
            dn "Apa..."
            dn "Baiklah, biarkan aku pergi dan berubah"
            dn "Kami akan melakukannya di toilet, bukan di tempat tidur saya"
            dn "{i} sungguh jalang yang penuh kasih ayam {/i}"
            dn "{i} Saya perlu menyiapkan kamera saya {/i}"
            scene mdanb3 with fade
            ml "Kemarilah"
            scene mdanb4 with dissolve
            ml "Ah"
            scene mdanb5 with dissolve
            "..."
            scene mdanb6 with dissolve
            "..."
            scene mdanb7 with dissolve
            "..."
            scene mdanb8 with dissolve
            "..."
            scene mdanb9 with fade
            ml "Later Rob"
            r "Ok"
            dn "{i} i \ 'll Siapkan foto dan berikan kepada [bname] di versi berikutnya {/i}"
            scene black
            "KEMBALI"
            jump broom_menu




        elif wk >= 1 and cselaine0 == 0:
            $ cselaine0 = 1
            scene black
            "SEMENTARA ITU"
            scene cse with fade
            r "Kemana kamu pergi?"
            scene cse1 with dissolve
            e "Untuk melihat [mname]"
            r "Untuk apa?"
            e "Merampok! ..."
            scene cse2 with dissolve
            e "Maukah Anda menghentikan kecemburuan ini?!"
            r "..."
            scene black
            "KEMBALI"
            pass

        elif cselaine0 == 1 and meldan == 1:
            jump mdanlabel

        elif wk >= 2 and cselaine0 == 1 and robel ==2 and Hour ==18:
            $ cselaine0 = 2
            scene black
            "SEMENTARA ITU"
            scene cse with fade
            r "Kemana kamu pergi?"
            scene cse1 with dissolve
            e "Lagi?"
            r "Setiap malam Anda pergi ke [mname]?"
            e "Merampok! ..."
            scene cse2 with dissolve
            e "Maukah Anda menghentikannya"
            r "Aku ikut denganmu"
            scene black
            "KEMBALI"
            pass

        elif cselaine0 >= 5 and meldan == 2:
            jump mdanlabel1

        elif rowenacall == 1 and Hour >=19:
            scene broom_night with fade
            b "Hmm"
            play sound "sounds/mobilering.wav"
            b "Siapa nomor ini"
            stop sound
            scene rcall with dissolve
            b "Halo!"
            scene rcall1 with fade
            a "Saya perlu berbicara dengan Anda"
            b "{i} hmm ok tentang apa? {/i}"
            a "Bisakah kamu datang ke sini sendirian?"
            b "{i} sekarang! {/i}"
            a "Yes"
            b "Ok saya akan berada di sana"
            jump rbffight
        else:

            pass
        scene broom_night with fade
        b "Hmmm"
        b "Apa yang harus dilakukan?"
        menu:

            "Hubungi Melinda" if melvisit == 1 and melwork >= 0:
                scene bcallstew with fade
                b "Hai, apakah kamu punya sesuatu untukku?"
                if melwork ==0:
                    $ Hour += 1
                    $ melwork = 1
                    ml "{i} ya datang {/i}"
                    jump melwork

                elif melwork == 1:
                    $ Hour += 1
                    $ melwork += 1
                    ml "{i} Tidak ada hari ini {/i}"
                    pass

                elif melwork == 2:
                    $ Hour += 1
                    $ melwork = 0
                    ml "{i} Tidak ada hari ini {/i}"
                    pass


            "Belajar" if bstudied <2:
                $ Hour += 1
                $ bstudy += 1
                $ bstudied += 1
                scene bcourse with fade
                b "Hmm bagus"
                pass
            "Tonton porno":

                $ Hour += 1
                scene bporn with fade
                b "{i} (mari kita lihat) {/i}"
                if day == 3:
                    scene bporn1 with fade
                    "Ayo nak"
                    "Hehehe"
                    scene bporn2 with hpunch
                    "Ahhh"
                    scene bporn3 with dissolve
                    "..."
                    scene bporn4 with dissolve
                    "..."
                    scene bporn6 with dissolve
                    "..."
                    b "Sungguh!"
                    if srel >=9:
                        scene bporn7 with dissolve
                        "..."
                        pass
                    else:
                        pass
                    scene bporn5 with fade
                    b "Saya harus mencuci celana pendek ini"
                    scene broom_night with fade
                    "..."
                    call screen gnav

                elif day ==5:
                    scene bporn1 with fade
                    "Ayo nak"
                    "Hehehe"
                    scene bporn2 with hpunch
                    "Ahhh"
                    scene bporn3 with dissolve
                    "..."
                    scene bporn4 with dissolve
                    "..."
                    scene bporn6 with dissolve
                    b "Sungguh!"
                    if srel >=9:
                        scene bporn7 with dissolve
                        "..."
                        pass
                    else:
                        pass
                    scene bporn5 with fade
                    b "Saya harus mencuci celana pendek ini"
                    scene broom_night with fade
                    "..."
                    call screen gnav
                else:


                    scene bporn1 with fade
                    "Ayo nak"
                    "Hehehe"
                    scene bporn2 with hpunch
                    "Ahhh"
                    scene bporn3 with dissolve
                    "..."
                    scene bporn4 with fade
                    b "Sungguh!"
                    scene bporn5 with fade
                    b "Saya harus mencuci celana pendek ini"
                    scene broom_night with fade
                    "..."
                    call screen gnav

            "Edit [mname] Foto" if mphotoediting >=1:
                $ Hour += 1
                jump editmphotos


            "Lakukan riset untuk halaman mode [sname]" if rwena >= 2 and binstaexp <= 5 and instresearchdone ==0:
                $ Hour += 1
                scene binsta with fade
                b "Mari kita lihat"
                scene binsta1 with dissolve
                b "Hmm mudah peasy"
                b "Tapi saya butuh lebih banyak waktu untuk mengaturnya"
                b "Ini akan memakan waktu sekitar 6 hari"
                $ binstaexp += 1
                $ instresearchdone += 1
                scene broom_night with fade
                "..."
                call screen gnav

            "Buat halaman untuk [sname]" if binstaexp >5 and instadone ==0:
                $ Hour += 1
                scene binsta with fade
                b "Mari kita lakukan ini"
                scene binsta1 with dissolve
                b "Hmm"
                $ instadone = 1
                scene binsta2 with dissolve
                b "Bagus!"
                scene broom_night with fade
                "..."
                call screen gnav

            "Mulai mengunggah gambar di halaman [sname]" if instadone ==2 and skiss_asked == 1 and instauploads <1:
                $ Hour += 1
                scene binsta with fade
                b "Mari kita lakukan ini dengan gambar ponsel"
                scene binsta1 with dissolve
                b "Hmm"
                b "Gambar mana yang harus dipilih"
                $ instauploads = 1
                scene binsta2 with dissolve
                b "Bagus!"
                scene broom_night with fade
                "..."
                call screen gnav


            "Hubungi Stewart" if stewcalled ==0:
                $ Hour += 1
                $ stewcalled = 1
                $ cherylintro += 1
                scene bcallstew with fade
                if persistent.patch_enabled:
                    b "Hi dad"
                    pass
                else:
                    b "Hi Stewart"
                    pass

                d "Hi [bname]"
                d "Apakah semuanya baik -baik saja?"
                d "Bagaimana [mname]?"
                d "Apakah Anda butuh uang?"
                b "Ya semuanya terkendali"
                b "Dia baik -baik saja, bertahan hidup"
                menu:
                    "Saya akan memberi tahu Anda saat saya membutuhkan uang":
                        "Opsi untuk meminta uang belum tersedia"
                        b "Dan tidak, saya belum butuh uang"
                        b "Aku akan memberitahumu saat aku membutuhkan"
                        pass



                d "Ok, dan bagaimana [sname]"
                b "Dia baik -baik saja"
                d "Bisakah Anda memberi tahu saya di mana Anda tinggal"
                b "Maaf saya harus menutup"
                b "Seseorang ada di pintu"
                b "Aku akan meneleponmu nanti"
                scene nxday11 with dissolve
                d "Sial, dia tutup"
                scene broom_night with fade
                "..."
                call screen gnav

            "{b} periksa kamera {/b}" if camerafixing == 2:
                scene bporn with fade
                b "{i} mari kita lihat {/i}"
                if camexpose >=1 and camerarecording == 1:
                    b "{i} hmm mari kita periksa apa yang ada di {/i}"
                    scene camscenes1 with fade
                    b "{i}Hmm{/i}"
                    scene camscenes2 with fade
                    b "{i}same{/i}"
                    scene camscenes5 with dissolve
                    b "{i} Saya sudah melihat ini {/i}"
                    scene camscenes6 with dissolve
                    b "{i} keren {/i}"
                    b "Ah itu semua"
                    pass


                elif camerarecording == 1:
                    scene camscenes1 with fade
                    b "{i} juga tidak menunjukkan wajahnya {/i}"
                    scene camscenes2 with fade
                    b "{i}same{/i}"
                    scene camscenes5 with dissolve
                    $ camexpose = 1
                    b "{i} keren, saya perlu menyimpan ini {/i}"
                    b "{i} Lalu aku akan memanggilnya sekali lagi, dan menunjukkannya padanya {/i}"
                    pass


                elif camerarecording1 == 1 and camerarecording == 0:
                    scene camscenes3 with fade
                    b "{i} tidak menunjukkan wajahnya {/i}"
                    b "Damn"
                    pass


                elif camerarecording2 == 1 and camerarecording1 == 0:
                    scene camscenes4 with fade
                    b "{i} juga tidak menunjukkan wajahnya {/i}"
                    b "Damn"
                    pass
                else:




                    scene black with fade
                    b "Nothing"
                    pass

                scene black with fade
                "..."
                jump broom_menu

            "{b} periksa kamera aula {/b}" if hallcamera >=2 and gnight >=4 and hallcameracheckedm ==0:
                $ hallcameracheckedm = 1
                $ hallcamcheckm += 1
                scene bporn with dissolve
                b "Hmmm, mari kita lihat"
                scene checkcamera with dissolve
                b "..."
                scene checkcamera1 with dissolve
                "..."
                if hallcamcheckm >=3:
                    scene checkcamera15 with dissolve
                    b "Bagus"
                    m "[bname]"
                    scene checkcamera16 with hpunch
                    b "Huh"
                    m "Apa yang sedang kamu lakukan?"
                    b "Nothing"
                    m "Di telanjang?"
                    m "Menonton porno bukan?"
                    b "No"
                    scene checkcamera17 with dissolve
                    m "Berdiri!"
                    scene checkcamera18 with hpunch
                    b "Ah"
                    scene checkcamera19 with dissolve
                    m "Anda mendarat di kamar Anda sampai besok"
                    b "Apa!"
                    m "Saya tidak ingin melihat Anda keluar dari ruangan ini"
                    scene broom_night with fade
                    b "{i}(Damn){/i}"
                    b "{i} (apa yang harus dilakukan sekarang?) {/i}"
                    scene black
                    "Beberapa waktu berlalu"
                    scene broom_night with fade
                    b "Mungkin saya bisa memeriksa kamera"
                    scene checkcamera20 with dissolve
                    b "Wow mereka bersama"
                    m "Jangan takut"
                    s "Tapi itu film horor"
                    m "Tidak, itu tidak"
                    m "Saya akan mendapatkan minuman lagi"
                    scene checkcamera21 with dissolve
                    s "Hmm"
                    scene checkcamera20 with fade
                    b "Dingin"
                    m "Saya kira sudah waktunya tidur"
                    s "Bisakah aku tidur denganmu malam ini"
                    m "Tidak, tidak perlu"
                    scene checkcamera22 with dissolve
                    s "..."
                    scene broom_night with fade
                    b "{i} (mereka pergi) {/i}"
                    b "{i} (Saya kira sudah waktunya tidur) {/i}"
                    "Itu semua dalam versi ini"
                    jump newdays
                else:

                    b "Enough"
                    scene broom_night with fade
                    "..."
                    "Coba lebih banyak"
                    call screen gnav
            "kembali":

                scene broom_night with fade
                "..."
                call screen gnav

        scene broom_night with fade
        "..."
        call screen gnav

    elif Hour >=21:
        scene broom_night with fade
        b "{i} (Saya harus tidur) {/i}"
        jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
