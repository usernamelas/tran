
define a = Character("Rowena")

label hall_menu:
    if Hour ==9:
        jump morning_hall
    elif Hour ==10:
        if workrequest ==2:
            jump workrequest
        else:
            jump morning_hall
    elif Hour ==11:
        jump morning_hall

    elif Hour ==12:
        $ Hour += 1
        jump lunch_hall


    elif Hour >=13 and Hour <14:
        scene hall_d with fade
        b "{i} (tidak ada orang di sini) {/i}"
        call screen gnav

    elif Hour >=14 and Hour <15:
        if workrequest ==3 and day !=7:
            scene hall_d with fade
            b "{i} (tidak ada orang di sini) {/i}"
            call screen gnav
        else:
            pass
        $ Hour += 1
        scene hall_d_mc with fade
        b "{i} (...) {/i}"
        b "Saya tidak mengerti mengapa kami tidak menyewa seorang pelayan?"
        scene hall_d_mc1 with dissolve
        "..."
        b "Itu tidak akan harganya lebih mahal"
        b "hourly paid"
        scene hall_d_mc2 with dissolve
        m "Kami tidak punya uang [bname]"
        m "Berhenti mengulangi ini"
        m "Dan datang ke sini bantu saya!"
        b "Kami baru saja membersihkannya"
        m "Bukan area ini!"
        m "Ayo bantu saya"
        if mrel >=30:
            scene hall_d_mc3 with dissolve
            b "{i} (...) {/i}"
            scene hall_d_mc3a with dissolve
            m "Apa yang kamu tunggu?"
            b "Kesalahan ya ..."
            pass
        else:
            pass
        b "Oke, mulai dari mana?"
        m "Membersihkan kursi"
        scene hall_d_mc4 with fade
        b "{i} (...) {/i}"
        if mrel >=40:
            scene hall_d_mc5 with dissolve
            b "{i} (...) {/i}"
            scene hall_d_mc6 with dissolve
            "..."
            menu:
                "Bersihkan di belakangnya":
                    b "Saya akan membersihkan bagian itu"
                    scene hall_d_mc8 with fade
                    b "{i} (posisi itu bagus untuk ...) {/i}"
                    scene hall_d_mc9 with dissolve
                    b "{i} (a doggystyle kasar) {/i}"
                    scene hall_d_mc10 with dissolve
                    m "Apakah kamu sudah selesai?"
                    b "Yes"
                    pass
                "Saya sudah selesai":

                    pass
        else:
            "..."
            b "... Aku sudah selesai"
            pass
        "..."
        scene hall_d_mc7 with fade
        m "Anda bisa pergi sekarang"
        show screen mrelup
        $ mrel += 2
        m "Terima kasih"
        hide screen mrelup
        b "{i}(Hmm){/i}"
        scene hall_d with fade
        "..."
        call screen gnav

    elif Hour ==15:
        $ Hour += 1
        if mrob ==1 and workrequest ==3:
            $ Hour += 1
            $ mrob = 2
            "Sementara itu di [mname] bekerja"
            scene melwrk23a with fade
            "..."
            scene melwrk24a with dissolve
            "..."
            scene vch12 with dissolve
            r "{i} (ini dia) {/i}"
            scene vch13 with fade
            r "{i} (i \ 'll tunggu dia) {/i}"
            scene vch14 with fade
            r "Ini dia"
            m "Jadi? Apa yang telah terjadi?"
            r "Mereka membuat seks"
            r "Dan saya pikir dia memberinya uang pada akhirnya"
            scene vch15 with dissolve
            m "..."
            scene vch16 with vpunch
            r "Hai!"
            m "..."
            scene vch17 with fade
            m "Terima kasih Rob, Anda bisa menjatuhkan saya"
            scene vch18 with dissolve
            r "Beri tahu saya kapan pun Anda butuh bantuan"
            m "Tentu terima kasih"
            scene hall_d with fade
            "..."
            call screen gnav

        elif wk >=1 and rwena == 0 and day == 3:
            $ rwena = 1
            scene b_tv_s_r with fade
            b "{i} (oh who \ \ 'is this) {/i}"
            scene b_tv_s_r2 with dissolve
            b "Hi"
            s "Hi [bname]"
            s "Ini teman saya Rowena"
            a "Hi [bname]"
            b "Hi"
            s "Dia yang memiliki halaman Insta yang saya ceritakan"
            b "Ah begitu, keren, mari kita bahas tentang hal itu"
            scene b_tv_s_r1 with dissolve
            s "Tidak sekarang [bname]"
            b "Oh, ok lain kali"
            scene hall_d with fade
            "..."
            call screen gnav


        elif wk >=1 and rwena >= 1 and day >3:
            if day ==6 and rosdad == 0 and sgoestost >= 2:
                $ Hour += 1
                scene b_tv_s_r with fade
                s "Apakah Anda ingin keluar?"
                $ rosdad = 2
                a "Dimana"
                s "Ayo ayo pergi, aku akan memberitahumu di jalan"
                scene srd with fade
                if persistent.patch_enabled:
                    s "Ayah!"
                    pass
                else:
                    s "Seh!"
                    pass
                d "[sname] !!"
                s "Aku merindukanmu"
                scene srd2 with dissolve
                s "Rowena temanku"
                scene srd1 with fade
                s "Jadi apa?"
                s "Apa rencanamu?"
                s "Jangan beri tahu saya bahwa Anda akan tidur"
                s "Anda tidak bisa mengatakannya, ini masih lebih awal"
                d "Saya memiliki beberapa pekerjaan yang harus dilakukan"
                s "Baiklah, kami hanya akan bersantai"
                scene srd3 with fade
                s "Follow me"
                scene srd4 with dissolve
                a "Bagus"
                scene srd5 with dissolve
                "..."
                scene srd6 with dissolve
                "..."
                scene srd7 with dissolve
                s "Seseorang mengawasi Anda"
                scene srd8 with dissolve
                s "Jangan lihat !!"
                scene srd9 with fade
                s "Jadi bagaimana pekerjaan Anda?"
                d "Tidak buruk"
                s "Bagus bagus, kami akan berubah dan pergi"
                s "Sampai jumpa lain waktu"
                scene hall_d with fade
                "..."
                call screen gnav


            elif day ==7 and rosdad ==2:
                scene b_tv_s_r with fade
                $ Hour += 1
                s "Let \'s Go?"
                scene b_tv_s_r1 with fade
                b "Hei, apa?"
                s "Kami pergi, tinggalkan kami sendiri"
                b "Kemana, bisakah aku ikut denganmu?"
                s "No"
                b "Hmm"
                scene b_tv_d with fade
                "..."
                scene b_tv_d3 with dissolve
                m "[bname] Dimana [sname]"
                b "Saya tidak tahu dia pergi dengan Rowena"
                m "Ok"
                m "Apa yang ingin Anda makan untuk makan siang?"
                menu:
                    "Mari kita hubungi Elaine":
                        if mrel >=300:
                            m "Ide bagus"
                            jump elainelunch
                        else:
                            m "Tidak sayang, dia punya pekerjaan"
                            "Anda tidak memiliki poin yang cukup dengan [mname]"
                            "300 dibutuhkan"
                            pass
                    "Melanjutkan":

                        pass

                scene srd10 with fade
                b "Makan siang itu enak"
                b "Apakah Anda ingin minum?"
                if mrel >=100:
                    m "Ya kenapa tidak"
                    m "Aku punya sesuatu yang baru, aku akan menunjukkan padamu"
                    scene srd11 with fade
                    b "Wow"
                    scene srd12 with dissolve
                    m "Cheers"
                    "..."
                    m "Anda dapat menutup mulut [nama]"
                    m "Hahaha"
                    scene srd13 with dissolve
                    m "Jika Anda tidak berhenti menatap saya akan mengubahnya"
                    scene srd14 with dissolve
                    b "..."
                    b "Tidak, tidak menunggu"
                    m "..."
                    menu:
                        "Ambil pantatnya" if mdom>=2:
                            scene ghass with dissolve
                            m "Jangan hancurkan [bname]"
                            m "Saya akan menghapusnya"
                            scene srd_test with dissolve
                            m "Ahh"
                            scene srd_test3 with dissolve
                            m "Damn"
                            scene srd_test2 with dissolve
                            m "Sungguh!"
                            b "Kamu tidak apa apa?"
                            scene srd_test5 with dissolve
                            m "Lanjutkan, aku akan membunuhmu jika kamu tidak melakukannya dengan baik"
                            scene srd_test4 with hpunch
                            m "Ahhh"
                            scene srd_test with dissolve
                            "..."
                            scene srd_test3 with dissolve
                            "..."
                            scene srd_test4 with dissolve
                            "..."
                            scene srd_test6 with fade
                            "..."
                            scene black
                            "SEMENTARA ITU"
                            jump rosddd
                        "Bersikaplah lembut":


                            scene srd14 with dissolve
                            "..."
                            scene srd15 with fade
                            m "Apa [nama]"
                            scene srd16 with dissolve
                            "..."
                            scene srd17 with dissolve
                            "..."
                            scene srd19 with vpunch
                            m "Mhhm"
                            scene srd20 with dissolve
                            "..."
                            scene srd21 with dissolve
                            m "Ah [bname]"
                            scene srd22 with dissolve
                            m "Don't stop"
                            scene srd23 with dissolve
                            "..."
                            scene srd24 with dissolve
                            m "Mmmm"
                            scene mmiss
                            m "Yes"
                            "..."
                            m "..."
                            m "Yesss"
                            "..."
                            m "Jangan cum di dalam"
                            menu:
                                "Di mulutnya":
                                    scene srd25 with hpunch
                                    "..."
                                    scene srd26 with dissolve
                                    "..."
                                    scene srd27 with fade
                                    "..."
                                    b "Bye"
                                    scene black
                                    "SEMENTARA ITU"
                                    jump rosddd
                                "Melanjutkan":

                                    scene srd28 with fade
                                    "..."
                                    scene black
                                    "SEMENTARA ITU"
                                    jump rosddd
                else:

                    m "Tidak, saya lelah saya ingin tidur"
                    b "Hmm Ok"
                    scene b_tv_d with fade
                    "..."
                    scene black
                    "SEMENTARA ITU"
                    jump rosddd

            scene b_tv_s_r with fade
            if spregnantno == 1:
                a "Tidak khawatir, Anda tidak akan hamil"
                b "Hmm"
                pass
            else:
                pass
            "..."
            if sgrm >=1:
                if mfuckedsober >= 1:
                    s "Rowena! Apakah Anda ingin melakukan hal yang sama seperti terakhir kali"
                    a "Apa maksudmu?"
                    s "Mengajar [bname] pelajaran"
                    scene srviag with dissolve
                    a "Saya sudah memiliki pil dengan saya"
                    s "Hehe naughty"
                    scene srviag2 with dissolve
                    a "Mengambil"
                    scene srviag4 with fade
                    b "Hai gadis -gadis, ada apa"
                    s "Rowena, apakah Anda ingin jus?"
                    a "Yes please"
                    b "Hei, saya juga ingin jus"
                    menu:
                        "[sname] akan memasukkan pil ke dalam jusnya":
                            scene srviag5 with dissolve
                            s "Ambil, aku bersumpah seperti anak kecil"
                            scene b_tv_s_r1 with fade
                            s "Apa? Apakah Anda akan menonton kami sepanjang hari"
                            s "Tolong tinggalkan kami sendiri"
                            b "Anda ingin berbicara sepanjang hari?"
                            b "Mari kita melakukan sesuatu yang menyenangkan"
                            s "Nanti tolong, mari kita lakukan gadis -gadis yang berbicara dulu"
                            b "Ok setelah itu kami pergi ke kolam renang"
                            s "Ya Pergi Bersiap"
                            scene b_tv_s_r with fade
                            s "Jadi apa yang terjadi sekarang"
                            a "Anda ingin mengolok -oloknya, dia akan mengalami kesulitan"
                            a "Dan kami akan bersenang -senang di kolam renang"
                            s "Dingin"
                            scene srviag with dissolve
                            a "Mari kita kenakan sesuatu yang liar"
                            jump poolhardon1
                else:
                    pass
                s "Rowena, aku ingin menanyakan sesuatu padamu"
                a "Apa itu?"
                s "Saya ingin mengajar [bname] pelajaran"
                a "Hmm menarik, apa yang dia lakukan?"
                s "Aku akan memberitahumu lain kali, tapi aku ingin melakukan lelucon, sesuatu yang lucu dan seksi"
                scene srviag with dissolve
                a "Hmm"
                a "Saya punya ide"
                scene b_tv_s_r with dissolve
                a "Apakah Anda ingin melakukannya sekarang?"
                s "Yes sure"
                a "Aku akan kembali"
                scene srviag1 with fade
                $ persistent.unlock_44 = True
                b "Saya pikir Rowena ada di sini"
                s "Ya dia akan kembali, apa masalahmu"
                b "Nothing"
                s "Sekarang tinggalkan kami sendiri"
                b "{i} (mungkin dia di toilet aku akan mengikutinya) {/i}"
                scene b_tv_s_r3 with fade
                s "Jadi...?"
                a "Di sini masukkan ini di minumannya"
                scene srviag2 with dissolve
                s "Apa itu?"
                a "Itu pil untuk pria"
                s "Ya Tuhan dari mana Anda mendapatkannya?"
                a "Saya menemukannya dalam hal ibu saya"
                scene srviag3 with dissolve
                s "..."
                scene b_tv_s_r3 with dissolve
                s "Satu atau dua"
                a "Letakkan dua, semakin baik"
                scene srviag4 with dissolve
                b "Hai gadis -gadis, ada apa"
                s "Rowena, apakah Anda ingin jus?"
                a "Yes please"
                b "Hei, saya juga ingin jus"
                menu:
                    "[sname] akan memasukkan pil ke dalam jusnya":
                        scene srviag5 with dissolve
                        s "Ambil, aku bersumpah seperti anak kecil"
                        scene b_tv_s_r1 with fade
                        s "Apa? Apakah Anda akan menonton kami sepanjang hari"
                        s "Tolong tinggalkan kami sendiri"
                        b "Anda ingin berbicara sepanjang hari?"
                        b "Mari kita melakukan sesuatu yang menyenangkan"
                        s "Nanti tolong, mari kita lakukan gadis -gadis yang berbicara dulu"
                        b "Ok setelah itu kami pergi ke kolam renang"
                        s "Ya Pergi Bersiap"
                        scene b_tv_s_r with fade
                        s "Jadi apa yang terjadi sekarang"
                        a "Anda ingin mengolok -oloknya, dia akan mengalami kesulitan"
                        a "Dan Anda akan bersenang -senang di kolam renang"
                        s "Dingin"
                        scene srviag with dissolve
                        a "Mari kita kenakan sesuatu yang liar"
                        jump poolhardon
                    "Dia tidak akan melakukannya":


                        pass
            else:

                b "Hi There"
                pass
            if rwena == 1:
                $ rwena = 2
                scene b_tv_s_r2 with dissolve
                b "Haruskah kita membahas halaman Insta?"
                scene b_tv_s_r3 with dissolve
                s "Apa yang Anda katakan Rowena"
                a "Ya kenapa tidak"
                b "Jadi?"
                scene b_tv_s_r4 with dissolve
                a "Apakah Anda membuat halaman?"
                b "Tidak, tapi saya bisa melakukannya kapan saja"
                b "Itu mudah"
                b "Komputer adalah game saya"
                a "Apakah Anda tahu apa yang diperlukan untuk membuat konten dan halaman yang sukses?"
                b "Err, mungkin beberapa tagar yang dapat Anda bantu"
                scene b_tv_s_r5 with dissolve
                a "Anda perlu membeli kamera yang bagus, pakaian"
                a "Ini mode, Anda tidak bisa melakukannya murah"
                b "Itu membutuhkan banyak uang"
                s "[bname] ..."
                scene b_tv_s_r1 with dissolve
                s "Tinggalkan kami sendiri"
                b "Apa ...."
                b "Oke, terserah!"
                scene hall_d with fade
                show screen opnotif
                b "{i} (Saya harus melakukan penelitian terlebih dahulu) {/i}"
                b "{i} (dan kumpulkan uang) {/i}"
                hide screen opnotif
                "..."
                call screen gnav

            elif rwena ==2:
                if instadone == 1:
                    b "Hi"
                    scene b_tv_s_r4 with dissolve
                    a "Hi"
                    b "Saya telah membuat halaman"
                    a "Ah bagus"
                    a "Dan..."
                    a "Apakah Anda mendapatkan kamera?"
                    b "Tidak, belum mengerjakannya"
                    scene b_tv_s_r1 with dissolve
                    s "Tinggalkan kami sendiri [bname]"
                    b "Apa ...."
                    b "Oke, terserah!"
                    scene hall_d with fade
                    b "{i} (sialan, saya benar -benar perlu menemukan cara untuk mendapatkan uang) {/i}"
                    $ instadone = 2
                    show screen opmap
                    b "{i} (Saya harus mencari pekerjaan) {/i}"
                    hide screen opmap
                    call screen gnav
                else:

                    if instadone == 2:
                        b "Hi"
                        scene b_tv_s_r4 with dissolve
                        a "Hi"
                        b "Saya telah membuat halaman"
                        a "Ah bagus"
                        a "Dan..."
                        a "Apakah Anda mendapatkan kamera?"
                        b "Tidak, belum mengerjakannya"
                        scene b_tv_s_r1 with dissolve
                        if sdom >=20:
                            s "[bname] Kita perlu melanjutkan pembicaraan gadis -gadis kita"
                            s "Jika Anda tidak keberatan"
                            b "Saya bisa duduk di sana ..."
                            s "Ah Ok"
                            scene b_tv_s_r6 with fade
                            "..."
                            a "Saya perlu menggunakan kamar mandi"
                            s "Anda tahu di mana itu"
                            scene b_tv_s_r7 with fade
                            "..."
                            scene b_tv_s_r8 with dissolve
                            if stalkb_rowena >= 1:
                                s "Dengarkan [bname], Anda berbicara dengannya, atau tersesat"
                                s "Kami butuh waktu sendirian, gadis bicara apakah Anda mengerti?"
                                b "Hah!"
                                s "Please"
                                b "Ok"
                                s "Saat dia datang, tolong lakukan apapun yang ingin Anda lakukan dan pergi"
                                b "Sure"
                                a "I'm back"
                                scene b_tv_s_r9 with fade
                                menu:
                                    "Cium dia":
                                        b "Ah, ini dia"
                                        scene b_tv_s_r10 with hpunch
                                        $ rkiss += 1
                                        "..."
                                        scene b_tv_s_r11 with dissolve
                                        s "Eh huh!"
                                        if rkiss >2:
                                            b "{i}(Hmm){/i}"
                                            scene b_tv_s_r12 with fade
                                            s "[bname] !!"
                                            s "Dia punya pacar!"
                                            b "Jadi apa?!"
                                            if srel >=100:
                                                s "Ok baik -baik saja, lain kali saya akan mencium pria acak dan memberitahumu jadi apa!"
                                                b "Apa!?"
                                                b "Jadi apakah kita ... ??"
                                                if srel >=200:
                                                    scene b_tv_s_r13 with dissolve
                                                    s "Rowena aku akan sampai jumpa besok"
                                                    jump srokiss
                                                else:

                                                    pass
                                            else:

                                                pass
                                            s "Pergi ... tolong"
                                            scene hall_d with fade
                                            "..."
                                            call screen gnav
                                        else:

                                            b "{i}(Hmm){/i}"
                                            b "{i} (i \ 'll go sekarang, mari kita lihat bagaimana [sname] bereaksi) {/i}"
                                            scene hall_d with fade
                                            "..."
                                            call screen gnav

                                    "Mengapa kami tidak melakukan sesuatu?" if browenabm >=3:
                                        b "Ah, ini dia"
                                        scene b_tv_s_r9 with dissolve
                                        a "Yep"
                                        b "Mengapa kami tidak pergi ke suatu tempat"
                                        s "Dimana?"
                                        scene b_tv_s_r34 with dissolve
                                        b "Pergi bersiap -siaplah aku akan memberitahumu dalam perjalanan"
                                        jump ncabana
                                    "Sampai jumpa lain waktu":



                                        b "Ah, ini dia"
                                        b "Sampai jumpa lain waktu"
                                        if rowenacall >1:
                                            scene b_tv_s_r9w with dissolve
                                            a "Sampai jumpa juga"
                                            $ contactrowena = 1
                                            b "{i} Apakah dia mengedipkan mata padaku ?! {/i}"
                                            b "{i} i \ 'll tebak saya harus meneleponnya untuk mengetahui {/i}"
                                            pass
                                        else:

                                            a "Kamu juga"
                                            pass

                                        scene hall_d with fade
                                        b "{i} (sialan, saya benar -benar perlu menemukan cara untuk mendapatkan uang) {/i}"
                                        b "{i} (sialan pekerjaan ini) {/i}"
                                        call screen gnav
                            else:

                                pass
                            s "Dengarkan [bname], saya tahu bahwa Anda menyukai Rowena"
                            s "Tapi tolong, Anda perlu memberi kami waktu sendirian"
                            b "Hah!"
                            s "Please"
                            b "Ok"
                            s "Saat dia datang, tolong sambut dia dan pergi"
                            b "Sure"
                            a "I'm back"
                            scene b_tv_s_r9 with fade
                            b "Ah, ini dia"
                            b "Sampai jumpa lain waktu"
                            a "Kamu juga"
                            scene hall_d with fade
                            b "{i} (sialan, saya benar -benar perlu menemukan cara untuk mendapatkan uang) {/i}"
                            b "{i} (sialan pekerjaan ini) {/i}"
                            call screen gnav
                        else:

                            s "Tinggalkan kami sendiri [bname]"
                            b "Apa ...."
                            b "Oke, terserah!"
                            b "{i} (Saya harus meningkatkan dominasi saya) {/i}"
                            scene hall_d with fade
                            b "{i} (sialan, saya benar -benar perlu menemukan cara untuk mendapatkan uang) {/i}"
                            b "{i} (sialan pekerjaan ini) {/i}"
                            call screen gnav

                        pass
                    else:
                        pass
            b "Hi"
            scene b_tv_s_r4 with dissolve
            a "Hi"
            a "Apakah Anda mendapatkan kamera?"
            b "Tidak, belum mengerjakannya"
            scene b_tv_s_r1 with dissolve
            s "Tinggalkan kami sendiri [bname]"
            b "Apa ...."
            b "Oke, terserah!"
            scene hall_d with fade
            "..."
            call screen gnav
        else:

            pass
        scene b_tv_s with fade
        b "..."
        menu:
            "Mengganggunya" if workrequest >=3 and srel >= 200 and day !=7:
                scene b_tv_s1 with dissolve
                s "Apa yang kamu inginkan?"
                menu:
                    "Apa yang sedang kamu lakukan?":
                        s "Saya mencuci piring"
                        s "Duh!"
                        scene b_tv_sa with vpunch
                        s "Aduh!"
                        s "Bajingan menghentikannya"
                        pass

                    "Bicara tentang seorang gadis cantik" if srel >= 300 and hotphotos_done ==1:
                        $ sgrm = 1
                        scene b_tv_sa with vpunch
                        s "Aduh!"
                        s "Bajingan menghentikannya"
                        b "Ini tidak terlihat seperti pantat wanita"
                        scene b_tv_sa1 with dissolve
                        s "Aku membunuhmu"
                        b "Hey wait"
                        scene b_tv_s3 with fade
                        s "{i} (i \ 'll membuat dia membayar kata -katanya) {/i}"
                        b "Jika saya mengatakan ini karena saya peduli, Anda benar -benar perlu mengerjakan pantat Anda"
                        s "Tutup tv menonton tv \"
                        scene b_tv_sa2 with fade
                        s "Apa -apaan [bname]"
                        b "Apa, itu keren"
                        b "Biarkan menontonnya"
                        if srel >= 300:
                            scene b_tv_sa3 with dissolve
                            s "Sial, porno itu bodoh"
                            b "Mengapa? Tidak, itu tidak"
                            scene b_tv_s3 with dissolve
                            s "Itu, dengan semua oh dan ah palsu"
                            b "Ayo, jangan berpura -pura bahwa kamu adalah kue manis"
                            s "I am"
                            scene b_tv_s2 with dissolve
                            s "Dan Anda seorang bajingan"
                            scene b_tv_sa4 with dissolve
                            s "Tolong jangan menjadi bajingan"
                            scene b_tv_sa5 with dissolve
                            b "I won't"
                            scene b_tv_sa6 with dissolve
                            "..."
                            scene b_tv_sa7 with dissolve
                            s "Ahh"
                            scene b_tv_sa8 with dissolve
                            b "Change"
                            $ persistent.unlock_26 = True
                            scene b_tv_sa9 with fade
                            s "Mmmm"
                            scene b_tv_sa10 with dissolve
                            s "Wait"
                            scene b_tv_sa11 with dissolve
                            s "Oh"
                            scene b_tv_sa12 with dissolve
                            "..."
                            menu:
                                "Cum di dalam":
                                    scene b_tv_sa13 with dissolve
                                    $ spreg += 1
                                    b "Ahh"
                                    pass
                                "Cum di luar":
                                    scene b_tv_sa14 with dissolve
                                    b "Ahh"
                                    pass
                            scene b_tv_sa15 with dissolve
                            "..."
                            scene hall_d with fade
                            "..."
                            call screen gnav
                        else:

                            s "Hah!"
                            b "Ahahaha"
                            if persistent.patch_enabled:
                                s "Hentikan, saya akan memberitahu ibu untuk membatalkan saluran ini"
                                pass
                            else:
                                s "Hentikan, saya akan memberi tahu [mname] untuk membatalkan saluran ini"
                                pass
                            scene b_tv_s4 with dissolve
                            b "Ayo, tidak ada yang salah dalam hal ini"
                            b "Ini hanya sebuah pertunjukan, mungkin gulat"
                            s "Hanya! Hentikan!"
                            scene b_tv_s5 with dissolve
                            s "Ini jauh lebih baik"
                            scene b_tv_s6 with fade
                            b "{i} (boring, saya pikir saya akan pergi) {/i}"
                            scene hall_d with fade
                            "..."
                            call screen gnav

                        pass
            "Duduklah di sebelahnya":

                pass
        scene b_tv_s1 with dissolve
        b "Bergerak sedikit sehingga saya bisa duduk"
        s "Tinggalkan aku sendiri [bname] pergi melakukan sesuatu"
        b "Saya ingin melakukan sesuatu"
        b "Itu untuk menonton TV"
        s "Ok baik, tapi saya pilih"
        s "Saya tidak ingin pertunjukan bising"
        scene b_tv_s2 with dissolve
        b "Fine"
        scene b_tv_s3 with dissolve
        s "Hah!"
        b "Ahahaha"
        if persistent.patch_enabled:
            s "Hentikan, saya akan memberitahu ibu untuk membatalkan saluran ini"
            pass
        else:
            s "Hentikan, saya akan memberi tahu [mname] untuk membatalkan saluran ini"
            pass
        scene b_tv_s4 with dissolve
        b "Ayo, tidak ada yang salah dalam hal ini"
        b "Ini hanya sebuah pertunjukan, mungkin gulat"
        s "Hanya! Hentikan!"
        scene b_tv_s5 with dissolve
        s "Ini jauh lebih baik"
        menu:
            "Hei, apakah Anda ingin mengambil beberapa foto?" if srel >= 100:
                scene sroom_inst_photos_suggestive8a with fade
                b "Tidak bisakah Anda memikirkan gaun yang lebih baik?"
                b "Kami sudah menerima ini"
                scene sroom_inst_photos_suggestive10a with dissolve
                s "Ok tunggu di sini"
                scene schg with dissolve
                s "Saya akan mendapatkan pakaian sekolah saya"
                scene schg1 with fade
                b "Apakah Anda serius ini pakaian sekolah Anda?"
                s "Saya memotong rok lebih pendek"
                b "Hmmm"
                s "Ambil fotonya sekarang"
                b "Done"
                b "Turn"
                scene schg2 with dissolve
                b "Foto -foto ini akan menyenangkan"
                b "Sama tapi lihat kamera"
                scene schg3 with dissolve
                b "Cute"
                b "Sekarang lepaskan kemeja"
                if srel >= 150:
                    scene schg5 with dissolve
                    b "Taken"
                    b "Dan roknya"
                    if sdom >= 80:
                        scene schg6 with dissolve
                        b "Dingin"
                        b "More"
                        scene schg7 with dissolve
                        b "Pose macam apa itu"
                        scene schg8 with dissolve
                        b "Angkat kaki Anda"
                        b "Dan tangan seperti ini"
                        scene schg9 with dissolve
                        s "Apa?"
                        scene schg10 with fade
                        "..."
                        scene schg11 with dissolve
                        s "..."
                        scene schg12 with dissolve
                        s "Ahhh"
                        scene schg13 with dissolve
                        s "[bname] Harap berhenti"
                        scene schg14 with fade
                        b "Jangan katakan itu, saya tahu bajingan"
                        s "Idiot"
                        s "Keluar"
                        b "Hehehe"
                        scene hall_d with fade
                        "..."
                        call screen gnav
                    else:

                        s "TIDAK!"
                        b "Ayo!"
                        s "Keluar"
                        scene hall_d with fade
                        "Naikkan dominasi Anda ke 80 setidaknya"
                        call screen gnav
                else:

                    scene schg4 with dissolve
                    s "TIDAK!"
                    b "Ayo!"
                    s "Keluar"
                    scene hall_d with fade
                    "Naikkan hubungan Anda ke 150 setidaknya"
                    call screen gnav

            "Apakah Anda ingin pergi ke Rowena?" if srel >= 150:
                s "Ya kenapa tidak"
                jump romomvisit
            "Meninggalkan":

                pass
        scene b_tv_s6 with fade
        b "{i} (boring, saya pikir saya akan pergi) {/i}"
        scene hall_d with fade
        "..."
        call screen gnav

    elif Hour >=16 and Hour <17:
        if elaineshowsup ==1 and day ==6:
            $ Hour += 1
            scene hall_d_e with fade
            b "Huh"
            b "Sepenuhnya Telanjang!"
            scene hall_d_e1 with dissolve
            e "Oh hai [bname]"
            b "Hehehe"
            e "Maaf karena merasa di rumah"
            b "No problem"
            b "Errm ..."
            menu:
                "Bisakah kita...?":
                    e "Ya tapi saya tidak melakukan apa pun secara gratis"
                    b "Ah yeah"
                    b "Berapa harganya?"
                    e "$300"
                    b "Apa"
                    e "Saya biasanya mengambil 500"
                    e "Itu hanya untukmu"
                    menu:
                        "Lepaskan" if mny >=300:
                            $ mny -= 300
                            jump elainevisitfuck
                        "Terima kasih sekarang":
                            e "Ok"
                            scene hall_n with fade
                            "..."
                            call screen gnav
                "Sampai jumpa lagi":

                    e "Ok"
                    scene hall_n with fade
                    "..."
                    call screen gnav
        else:
            pass
        scene hall_n with fade
        b "{i} (tidak ada orang di sini) {/i}"
        call screen gnav

    elif Hour ==17:
        $ Hour += 1
        if lesbianchannel == 1:
            scene lesbchan with fade
            $ lesbianchannel = 2
            b "{i} (hmm mungkin saya harus mengaturnya di saluran lesbian saja) {/i}"
            scene lesbchan1 with dissolve
            b "{i} (mari kita lihat reaksi mereka hehehe) {/i}"
            scene hall_n with fade
            b "{i} (hebat) {/i}"
            call screen gnav

        elif cselaine0 == 11:
            if workrequest ==3 and day !=7:
                $ Hour -= 1
                scene cinenights with fade
                b "Siap?"
                s "Ya, mari kita pergi"
                scene black
                "..."
                scene cinenights1 with fade
                b "Inilah teaternya"
                b "Kurasa, aku meninggalkanmu sekarang"
                b "Kami bertemu di rumah"
                s "Apa?"
                s "Apakah Anda akan meninggalkan saya seperti ini?"
                b "Kenapa tidak, filmnya untukmu"
                s "Hmpff"
                b "{i} (oh fuck !!) {/i}"
                menu:
                    "Tetap bersamanya":
                        $ cselaine0 = 8
                        $ Hour += 1
                        b "Ok ok saya \ 'll tetap"
                        scene cinenights2 with dissolve
                        s "Yehey!"
                        b "Saya akan membeli tiket saya sendiri"
                        s "Ok"
                        scene citycinema1 with dissolve
                        b "Bisakah saya mendapatkan 1 tiket untuk film jam 17:00 o \ '?"
                        $ mny -= 25
                        b "17:00 Pertunjukan"
                        scene citycinema2 with dissolve
                        "Di Sini..."
                        b "Thanks"
                        scene black
                        "..."
                        scene cinenights3 with fade
                        s "Itu adalah film yang bagus"
                        b "Yeah"
                        scene cinenights4 with fade
                        $ srel += 2
                        show screen srelup
                        s "Terima kasih untuk malam yang indah [bname]"
                        hide screen srelup
                        scene broom_night with dissolve
                        "..."
                        scene cinenights5 with fade
                        b "Aha! Dia menyimpan uang itu, bagus"
                        $ mny += 70
                        $ renpy.notify (_("She left 70 $ for you"))
                        $ renpy.pause ( 5, 0)
                        scene broom_night with fade
                        "..."
                        call screen gnav
                    "Abaikan dan tinggalkan":


                        show screen sreldw
                        $ srel -= 2
                        b "Maaf tapi saya benar -benar harus mencari pekerjaan"
                        hide screen sreldw
                        scene cityn1 with fade
                        b "{i} (sialan, saya harus membuatnya cepat) {/i}"
                        scene black
                        "..."
                        jump elainebusiness
            else:


                pass
            scene cinenight with fade
            b "Siap saat Anda"
            m "Let's go"
            scene black
            "..."
            scene cinenight1 with fade
            b "Inilah teaternya"
            b "Kurasa, aku meninggalkanmu sekarang"
            b "Kami bertemu di rumah"
            m "Ok"
            scene cityn1 with fade
            b "{i} (sialan, saya harus membuatnya cepat) {/i}"
            scene black
            "..."
            jump elainebusiness
        else:

            scene hall_n with fade
            b "{i} (tidak ada orang di sini) {/i}"
            call screen gnav

    elif Hour ==18:
        $ Hour += 1
        if day == 7:
            scene hall_m_n with fade
            b "{i} (...) {/i}"
            scene hall_m_n2 with dissolve
            b "Apa yang salah?"
            scene hall_m_n3 with dissolve
            m "Tidak ada yang salah sayang"
            b "Oh OK"
            b "Bisakah saya menonton TV?"
            if workrequest ==3 and wrkquestions >=2:
                m "Sure"
                scene hall_m_n4 with fade
                "..."
                menu:
                    "Jadi, sampai ketika situasi ini akan berlanjut?":
                        m "Apa maksudmu?"
                        b "Saya berbicara tentang kehidupan kita di sini"
                        m "Apa yang salah dengan itu?"
                        scene hall_m_n5a with dissolve
                        b "Maksudku, aku merindukan kehidupan yang kita miliki sebelumnya"
                        scene hall_m_n6a with dissolve
                        m "{i} (Saya perlu menemukan solusi untuk ini) {/i}"
                        b "{i} (kenapa dia diam?) {/i}"
                        b "{i} (mungkin memikirkannya) {/i}"
                        scene hall_m_n5a with dissolve
                        m "Jangan khawatir, saya akan menemukan kami solusi"
                        b "Saya harap begitu"
                        if elaine_convince == 4:
                            scene hall_m_n8a with dissolve
                            s "Apa yang kamu tonton?"
                            m "..."
                            b "Hi [sname]"
                            s "Boring ... mari kita ubah menjadi sesuatu yang menyenangkan"
                            m "Anda lebih baik melanjutkan studi Anda"
                            scene hall_m_n7a with dissolve
                            s "Tapi kenapa!?"
                            m "Saya bilang lanjutkan studi Anda"
                            scene hall_m_n9a with dissolve
                            "..."
                            scene hall_m_n5a with dissolve
                            b "Aku akan pergi membantunya"
                            m "Ok sayang, bagus"
                            jump saction_study
                        else:

                            pass
                        scene hall_m_n4 with dissolve
                        "..."
                        scene hall_m_n1 with dissolve
                        m "Hi Elaine"
                        m "[bname] Buat ruang"
                        scene hall_m_n6 with fade
                        e "So?"
                        m "..."
                        scene hall_m_n7 with dissolve
                        m "[bname], bisakah Anda meninggalkan kami sendirian?"
                        if elaine_convince == 2:
                            b "Sure"
                            jump elaineconjen1
                        elif elaine_convince == 3:
                            jump elaineconjen2
                        else:
                            pass
                        scene hall_m_n26 with dissolve
                        b "{i}(Hmm){/i}"
                        scene hall_m_n27 with dissolve
                        m "[bname]! Saya bilang tolong tinggalkan kami sendiri"
                        b "Ahh, ya maaf"
                        scene hall_m_n20 with fade
                        m "Elaine, saya perlu menemukan jalan keluar dari situasi ini"
                        e "Apa maksudmu?"
                        scene hall_m_n21 with dissolve
                        m "Hidup ini, aku tidak bahagia"
                        m "[bname] tidak senang"
                        e "Nah sayang, dari apa yang saya lihat adalah Anda memiliki dua opsi di sini"
                        e "Entah Anda kembali ke Stewart"
                        m "Mustahil..."
                        m "Maksud saya tidak terlalu cepat"
                        e "Ok pilihan lainnya adalah Anda terus berkembang seperti yang Anda lakukan"
                        m "Tapi Elaine ... uang yang saya dapatkan"
                        m "Hampir tidak cukup sampai pertengahan bulan"
                        e "Hmm"
                        e "Itu bisa diselesaikan"
                        m "..."
                        e "Ayo bekerja dengan saya"
                        m "Saya tidak melakukan pekerjaan ini Elaine"
                        e "Saya tidak mendapatkan mengapa tidak, membayar dengan sangat baik"
                        e "Anda tidak akan membutuhkan bajingan itu dari Stewart"
                        scene hall_m_n20 with dissolve
                        b "{i} (hmm menarik) {/i}"
                        if camerasacquired == 1 and camerafixing ==0:
                            b "{i} (Saya kira sudah waktunya menggunakan kamera yang saya beli) {/i}"
                            $ camerafixing = 1
                            call screen gnav
                        elif elaine_convince == 1:
                            jump elaineconjen
                        else:
                            "..."
                            call screen gnav
                    "Pernahkah Anda memperhatikan sesuatu?":


                        m "Apa yang kamu bicarakan?"
                        scene hall_m_n5a with dissolve
                        b "Saya bertanya -tanya mengapa Stewart tidak pernah menelepon [sname]"
                        scene hall_m_n5b with dissolve
                        m "..."
                        scene hall_m_n5a with dissolve
                        m "Mari kita tonton TV sayang"
                        b "..."
                        if elaine_convince == 4:
                            b "Ok"
                            scene hall_m_n8a with dissolve
                            s "Apa yang kamu tonton?"
                            m "..."
                            b "Hi [sname]"
                            s "Boring ... mari kita ubah menjadi sesuatu yang menyenangkan"
                            m "Anda lebih baik melanjutkan studi Anda"
                            scene hall_m_n7a with dissolve
                            s "Tapi kenapa!?"
                            m "Saya bilang lanjutkan studi Anda"
                            scene hall_m_n9a with dissolve
                            "..."
                            scene hall_m_n5a with dissolve
                            b "Aku akan pergi membantunya"
                            m "Ok sayang, bagus"
                            jump saction_study
                        else:

                            pass

                        scene hall_m_n4 with dissolve
                        "..."
                        scene hall_m_n1 with dissolve
                        m "Hi Elaine"
                        m "[bname] Buat ruang"
                        scene hall_m_n6 with fade
                        e "Jadi?"
                        m "..."
                        scene hall_m_n7 with dissolve
                        m "[bname], bisakah Anda meninggalkan kami sendirian?"
                        if elaine_convince == 2:
                            b "Sure"
                            jump elaineconjen1

                        elif elaine_convince == 3:
                            jump elaineconjen2
                        else:

                            pass
                        scene hall_m_n26 with dissolve
                        b "{i}(Hmm){/i}"
                        scene hall_m_n27 with dissolve
                        m "[bname]! Saya bilang tolong tinggalkan kami sendiri"
                        b "Ahh, ya maaf"
                        scene hall_m_n20 with fade
                        m "Elaine, saya perlu menemukan jalan keluar dari situasi ini"
                        e "Apa maksudmu?"
                        scene hall_m_n21 with dissolve
                        m "Hidup ini, aku tidak bahagia"
                        m "[bname] tidak senang"
                        e "Nah sayang, dari apa yang saya lihat adalah Anda memiliki dua opsi di sini"
                        e "Entah Anda kembali ke Stewart"
                        m "Mustahil..."
                        m "Maksud saya tidak terlalu cepat"
                        e "Ok pilihan lainnya adalah Anda terus berkembang seperti yang Anda lakukan"
                        m "Tapi Elaine ... uang yang saya dapatkan"
                        m "Hampir tidak cukup sampai pertengahan bulan"
                        e "Hmm"
                        e "Itu bisa diselesaikan"
                        m "..."
                        e "Ayo bekerja dengan saya"
                        m "Saya tidak melakukan pekerjaan ini Elaine"
                        e "Saya tidak mendapatkan mengapa tidak, membayar dengan sangat baik"
                        e "Anda tidak akan membutuhkan bajingan itu dari Stewart"
                        scene hall_m_n20 with dissolve
                        b "{i} (hmm menarik) {/i}"
                        if camerasacquired == 1 and camerafixing ==0:
                            b "{i} (Saya kira sudah waktunya menggunakan kamera yang saya beli) {/i}"
                            $ camerafixing = 1
                            "..."
                            call screen gnav

                        elif elaine_convince == 1:
                            jump elaineconjen
                        else:

                            b "{i} (Saya perlu menemukan cara untuk membuat Elaine mempengaruhi dia) {/i}"
                            call screen gnav


                scene hall_m_n5 with dissolve
                m "Saya akan pergi sekarang, nikmati pertunjukannya"
                b "Saya kira saya akan pergi juga"
                scene hall_d with fade
                "..."
                call screen gnav
            else:

                pass
                m "Sure"
                scene hall_m_n4 with fade
                "..."
                scene hall_m_n5 with dissolve
                m "Saya akan pergi sekarang, nikmati pertunjukannya"
                b "Saya kira saya akan pergi juga"
                scene hall_d with fade
                "..."
                call screen gnav
        else:



            if workrequest ==3:
                jump hall_evening
            else:

                pass
            scene hall_m_n with fade
            b "{i} (...) {/i}"
            scene hall_m_n2 with dissolve
            b "Apa yang salah?"
            scene hall_m_n3 with dissolve
            m "Tidak ada yang salah sayang"
            b "Oh OK"
            b "Bisakah saya menonton TV?"
            m "Sure"
            e "Hello"
            if cselaine0 ==2:
                scene hall_m_n23 with fade
                m "Oh, hai Elaine"
                m "Hi Rob"
                $ cselaine0 = 3
                m "[bname] Buat ruang"
                scene hall_m_n24 with fade
                e "Jadi..."
                scene hall_m_n25 with dissolve
                m "[bname], bisakah Anda meninggalkan kami sendirian?"
                b "{i}(Damn){/i}"
                scene hall_d with fade
                "..."
                call screen gnav

            elif cselaine0 >=3 and cselaine0 <7:
                scene hall_m_n1 with dissolve
                m "Hi Elaine"
                $ cselaine0 += 1
                m "[bname] Buat ruang"
                scene hall_m_n6 with fade
                e "Jadi?"
                m "..."
                scene hall_m_n7 with dissolve
                m "[bname], bisakah Anda meninggalkan kami sendirian?"
                scene hall_m_n26 with dissolve
                b "{i}(Hmm){/i}"
                scene hall_m_n27 with dissolve
                m "[bname]! Saya bilang tolong tinggalkan kami sendiri"
                b "Ahh, ya maaf"
                b "Saya sedang memikirkan studi saya"
                scene hall_m_n28 with dissolve
                e "{i} (hmm, berpikir tentang studi) {/i}"
                m "Go please"
                scene hall_d with fade
                "Ulangi adegan ini"
                call screen gnav

            elif cselaine0 ==7:
                scene hall_m_n1 with dissolve
                m "Hi Elaine"
                $ cselaine0 = 8
                m "[bname] Buat ruang"
                scene hall_m_n6 with fade
                e "Jadi?"
                m "..."
                scene hall_m_n7 with dissolve
                m "[bname], bisakah Anda meninggalkan kami sendirian?"
                scene hall_m_n26 with dissolve
                b "{i}(Hmm){/i}"
                scene hall_m_n27 with dissolve
                m "[bname]! Saya bilang tolong tinggalkan kami sendiri"
                b "Ahh, ya maaf"
                b "Saya sedang memikirkan studi saya"
                scene hall_m_n28 with dissolve
                e "{i} (hmm, berpikir tentang studi) {/i}"
                m "Go please"
                e "{i} (Saya harus berbicara dengannya) {/i}"
                scene broom_night with fade
                "..."
                scene hall_m_n30 with fade
                e "Bolehkah saya menggunakan kamar mandi [mname]?"
                m "Of course"
                e "Dimana itu?"
                m "Di sebelah kiri, di sana"
                scene black
                "..."
                scene hall_m_n29 with fade
                b "Mari kita lihat apa yang online"
                e "Ahem ..."
                scene hall_m_n31 with fade
                e "Hi [bname]"
                b "Ah Hi"
                scene hall_m_n32 with dissolve
                e "Saya butuh bantuan Anda"
                b "Yakin apa itu?"
                e "Hmm..."
                e "Apakah mungkin bagi Anda untuk ..."
                e "Bagaimana mengatakannya ..."
                scene hall_m_n33 with dissolve
                e "Bisakah saya meminjam kamar Anda?"
                e "Saya perlu menggunakannya selama satu jam"
                b "Maksudmu sekarang?"
                e "No"
                e "Sekarang tidak mungkin"
                scene hall_m_n32 with dissolve
                e "Aku membutuhkanmu ..."
                scene hall_m_n34 with dissolve
                e "Untuk mengambil [mname] dan [sname]"
                b "Di mana?"
                e "Saya tidak tahu, Anda mengetahuinya"
                e "Hanya beberapa jam, mungkin bioskop, restoran?"
                e "Pada saat itu saya perlu menggunakan kamar Anda"
                b "Aha ... aku mengerti"
                e "Aku akan membayarmu untuk itu"
                e "Dan untuk keheningan Anda"
                b "Izinkan saya menemukan jalan dan saya akan memberi tahu Anda"
                e "Saya membutuhkan kamar Anda pada pukul 17:00"
                scene hall_m_n33 with dissolve
                b "Ok keren"
                b "Berbuat salah..."
                b "Bagaimana cara memberi tahu Anda saat saya mengaturnya?"
                e "Datanglah ke alamat ini malam sebelumnya, setelah 18:00"
                e "Tell Rob [mname] Memiliki pesan untuk saya"
                b "Ok"
                scene broom_night with fade
                "Gunakan peta pada atau setelah 18:00"
                call screen gnav
            else:

                pass
            scene hall_m_n1 with dissolve
            m "Hi Elaine"
            m "[bname] Buat ruang"
            scene hall_m_n6 with fade
            e "Jadi?"
            m "..."
            scene hall_m_n7 with dissolve
            m "[bname], bisakah Anda meninggalkan kami sendirian?"
            scene hall_d with fade
            if robel ==1:
                b "{i} (ada sesuatu yang terjadi!) {/i}"
                b "{i} (i \ 'll harus mencari tahu) {/i}"
                menu:
                    "Eavesdrop":
                        $ robel = 2
                        scene hall_m_n20 with fade
                        e "Bisakah saya meminta bantuan?"
                        m "Bantuan macam apa?"
                        e "Bisakah saya datang siang hari dan menggunakan kamar tidur Anda?"
                        m "Untuk apa?"
                        e "Rob mencekik saya, dan saya memiliki klien yang ingin melihat saya di siang hari"
                        scene hall_m_n21 with dissolve
                        m "Klien!?"
                        e "Anda tahu, klien reguler saya, mereka ingin bertemu saya di siang hari"
                        m "Saya masih tidak memahaminya"
                        e "Waktu pribadi! Klien dengan manfaat!"
                        scene hall_m_n22 with dissolve
                        m "..."
                        scene hall_m_n21 with dissolve
                        m "Saya maafkan saya tidak bisa melakukan ini"
                        m "Anda tahu saya tidak bisa melakukannya, dan bahkan jika saya bisa, ada [sname] dan [bname] di sekitar"
                        scene hall_m_n20 with dissolve
                        show screen opnotif_f
                        b "{i} (jadi Elaine melakukan pekerjaan semacam ini !!) {/i}"
                        hide screen opnotif_f
                        b "{i} (keren, saya harus menemukan cara untuk meyakinkan [mname]) {/i}"
                        b "{i} (atau mungkin berbicara dengan Elaine, saya harus mencari tahu di mana dia bekerja) {/i}"
                        "..."
                        b "{i} (Time to Go Now) {/i}"
                        scene hall_d with fade
                        "..."
                        call screen gnav
                    "Meninggalkan":

                        "..."
                        call screen gnav
            else:
                if ebizaldoneonce >= 1 and workrequest ==0:
                    scene hall_m_n20 with fade
                    m "Bisakah Anda membantu saya menemukan pekerjaan?"
                    $ workrequest = 1
                    e "Of course"
                    e "Apakah Anda membutuhkan bantuan dengan uang?"
                    scene hall_m_n21 with dissolve
                    m "Saya masih bisa mengelola, tetapi tidak lama"
                    m "Dan saya lebih suka bergantung pada diri saya sendiri"
                    b "{i}(Hmmm){/i}"
                    b "{i} (Time to Go Now) {/i}"
                    scene hall_d with fade
                    "..."
                    call screen gnav

                elif workrequest ==1:
                    scene hall_m_n20 with fade
                    m "Jadi? Ada berita tentang pekerjaan itu?"
                    e "Mengapa Anda tidak ikut bekerja dengan saya"
                    scene hall_m_n22 with dissolve
                    m "..."
                    e "Hahaha saya bercanda, tetapi Anda harus mempertimbangkannya suatu hari nanti"
                    scene hall_m_n21 with dissolve
                    m "Ayo Elaine, apakah Anda menemukan pekerjaan yang layak atau tidak?"
                    e "Ya saya lakukan"
                    $ workrequest =2
                    m "Apa itu?"
                    e "Sama seperti pekerjaan lama Anda"
                    m "Pelayan?"
                    e "Yes"
                    e "Mari kita temui pemiliknya besok pukul 10:00"
                    m "Ok"
                    b "{i}(Hmmm){/i}"
                    b "{i} (Time to Go Now) {/i}"
                    scene hall_d with fade
                    "..."
                    call screen gnav
                else:

                    "..."
                    call screen gnav




    elif Hour >=19 and Hour <20:
        $ Hour += 1
        if mtrelax ==2 and day ==2:
            jump pdinnerm_relax
        elif mtrelax ==2 and day ==4:
            jump pdinnerm_relax

        elif mbunknown == 1 and day ==1:
            jump pdinnerm_b

        elif mbvisit >= 1 and day ==3:
            jump pdinnerm_b
        else:
            pass
        scene pdinner_m with fade
        b "{i} (aha!) {/i}"
        scene pdinner_m1 with dissolve
        b "Apakah Anda membutuhkan bantuan saya?"
        m "Yes please"
        b "Apa yang kamu butuhkan?"
        m "Bisakah Anda mencuci piring?"
        menu:
            "Tentu ... tapi ... bisakah saya meminta imbalan sesuatu?":
                scene pdinner_m2 with dissolve
                m "Apa yang kamu inginkan?"
                menu:
                    "Tidak ada yang saya ubah pikiran":
                        pass
                    "Bisakah Anda memakai sesuatu?" if mbikini==0:
                        m "Sesuatu apa?"
                        b "Tidak ada yang saya ubah pikiran"
                        b "{i} (mungkin saya harus memeriksa apakah saya bisa membelikannya bikini) {/i}"
                        pass

                    "Bisakah Anda memakai sesuatu?" if mbikini==1:
                        m "Sesuatu apa?"
                        b "Errm saya punya sesuatu untuk Anda"
                        m "Apa itu?"
                        b "Bikini, di sini ambillah"
                        m "Terima kasih"
                        b "Jangankah Anda ingin mencobanya?"
                        if mrel >=110:
                            m "Selesaikan piring yang saya pakai"
                            b "Jadi begitu"
                            scene pdinner_hr with dissolve
                            "..."
                            scene pdinner_hr1 with dissolve
                            b "Done"
                            b "Aku akan pergi sekarang"
                            show screen mrelup
                            $ mrel += 1
                            m "Terima kasih [bname]"
                            hide screen mrelup
                            m "Ikuti saya ke kamar saya dan tunggu di pintu"
                            scene door with fade
                            b "{i} (...) {/i}"
                            m "Datang"
                            scene pdinner_bikini with fade
                            m "Senang?"
                            b "Yeah"
                            menu:
                                "Mungkin saya harus mengambil beberapa foto?":
                                    $ mbikinirequest = 1
                                    pass
                                "Apakah ukuran yang tepat?":

                                    m "Ya, kenapa kamu bertanya?"
                                    b "Karena rasanya agak ketat"
                                    scene pdinner_bikini3 with dissolve
                                    m "Mungkin sedikit di cangkir"
                                    b "Jadi begitu"
                                    pass

                            b "Mungkin saya harus mengambil beberapa foto untuk Anda di dalamnya?"
                            if mrel >=350:
                                jump mphotoshoot
                            elif mrel >=200 and mcorr >=25:
                                jump mphotoshoot
                            else:

                                pass


                            scene pdinner_bikini1 with dissolve
                            $ mbikinirequest = 1
                            m "Apa?"
                            scene pdinner_bikini2 with dissolve
                            m "Tidak mungkin, tolong pergi"
                            scene hall_n with fade
                            b "{i} (oh sialan aku mengacaukannya) {/i}"
                            call screen gnav
                        else:

                            m "Beri aku waktu, aku akan melakukannya suatu hari nanti"
                            b "Jadi begitu"
                            pass



                    "Bisakah Anda mengenakan bikini?" if mbikini ==2:
                        b "{i} (sialan, aku tidak bisa mengatakan ini langsung) {/i}"
                        b "Bagaimana Anda menyukai bikini?"
                        m "Ya terima kasih, itu bagus"
                        b "Tapi aku tidak melihatmu memakainya?"
                        m "Saya tidak terbiasa memakai bikini seperti itu"
                        if mrel >=110:
                            m "Selesaikan piring yang saya pakai"
                            b "Jadi begitu"
                            scene pdinner_hr with dissolve
                            "..."
                            scene pdinner_hr1 with dissolve
                            b "Done"
                            b "Aku akan pergi sekarang"
                            show screen mrelup
                            $ mrel += 1
                            m "Terima kasih [bname]"
                            hide screen mrelup
                            m "Ikuti saya ke kamar saya dan tunggu di pintu"
                            scene door with fade
                            b "{i} (...) {/i}"
                            m "Datang"
                            scene pdinner_bikini with fade
                            m "Senang?"
                            b "Yeah"
                            menu:
                                "Mungkin saya harus mengambil beberapa foto?":
                                    $ mbikinirequest = 1
                                    pass
                                "Apakah ukuran yang tepat?":

                                    m "Ya, kenapa kamu bertanya?"
                                    b "Karena rasanya agak ketat"
                                    scene pdinner_bikini3 with dissolve
                                    m "Mungkin sedikit di cangkir"
                                    b "Jadi begitu"
                                    pass

                            b "Mungkin saya harus mengambil beberapa foto untuk Anda di dalamnya?"
                            if mrel >=350:
                                jump mphotoshoot
                            elif mrel >=200 and mcorr >=25:
                                jump mphotoshoot
                            else:

                                pass


                            scene pdinner_bikini1 with dissolve
                            $ mbikinirequest = 1
                            m "Apa?"
                            scene pdinner_bikini2 with dissolve
                            m "Tidak, tolong pergi"
                            scene hall_n with fade
                            b "{i} (oh sialan aku mengacaukannya) {/i}"
                            call screen gnav
                        else:

                            m "Beri aku waktu, aku akan melakukannya suatu hari nanti"
                            b "Jadi begitu"
                            pass

                scene pdinner_hr with dissolve
                "..."
                scene pdinner_hr1 with dissolve
                b "Done"
                b "Aku akan pergi sekarang"
                show screen mrelup
                $ mrel += 5
                m "Terima kasih [bname]"
                m "Jangan terlambat untuk makan malam"
                hide screen mrelup
                scene hall_n with fade
                "..."
                call screen gnav
            "Tentu":

                scene pdinner_hr with dissolve
                "..."
                scene pdinner_hr1 with dissolve
                b "Done"
                b "Aku akan pergi sekarang"
                if msconvince ==3:
                    m "Jadi bagaimana [sname]?"
                    m "Apakah ada kemajuan dengan studinya"
                    menu:
                        "Ya":
                            $ msconvince = 0
                            m "Oke, bagus"
                            pass
                        "Tidak, tetap sama":
                            m "Ok saya lihat"
                            $ msconvince = 2
                            pass
                else:

                    pass
                show screen mrelup
                $ mrel += 1
                if mrel >=150:
                    m "Wait"
                    scene pdinner_hrk with fade
                    m "Terima kasih [bname]"
                    hide screen mrelup
                    scene pdinner_hrk1 with dissolve
                    "..."
                    menu:
                        "Mencuri ciuman":
                            scene pdinner_hrk2 with dissolve
                            m "{i} (Mungkinkah itu karena kesalahan? {/i}"
                            "..."
                            scene pdinner_hrk3 with dissolve
                            m "{i} (atau ...) {/i}"
                            pass
                        "Melanjutkan":

                            pass
                else:


                    pass
                m "Terima kasih [bname]"
                hide screen mrelup
                scene hall_n with fade
                "..."
                call screen gnav


            "Tentu ... tapi ... ada sesuatu yang ingin saya katakan" if msconvince == 1:
                scene pdinner_hr with dissolve
                "..."
                scene pdinner_hr1 with dissolve
                b "Done"
                m "Apa yang Anda ingin katakan padaku"
                b "Ini tentang [sname] Studi"
                m "Apa yang salah?"
                b "Dia masih berjuang"
                b "Dia menghabiskan banyak waktu di TV"
                b "Dia harus mendedikasikan lebih banyak waktu untuk kursusnya"
                m "Begitu, saya akan berbicara dengannya"
                b "Besar"
                show screen mrelup
                $ msconvince = 2
                $ mrel += 1
                m "Terima kasih [bname]"
                hide screen mrelup
                b "{i} (semoga menyingkirkan [sname]) {/i}"
                b "{i} (dia tidak akan mengganggu kita pada Sabtu malam) {/i}"
                scene hall_n with fade
                "..."
                call screen gnav


    elif Hour ==20:
        "..."
        $ Hour += 1
        if bnamefixcheryl >= 5 and stknw ==0:
            scene stdinner with fade
            $ stknw = 1
            m "Tepat tepat waktu [bname]"
            play sound "sounds/mobilering.wav"
            b "..."
            stop sound
            scene stdinner1 with dissolve
            m "Hello"
            c "{i}(Hi there){/i}"
            m "Oh hi"
            c "Dengarkan [mname] Anda sangat beruntung sehingga saya belum memberi tahu Stewart"
            c "Tentang apa yang Anda lakukan"
            m "..."
            c "Dia sangat sibuk untuk menjawab"
            c "Tapi segera aku akan memberitahunya sebuah"
            scene dinner_m1 with dissolve
            b "{i} (apa yang terjadi padanya) {/i}"
            s "..."
            m "[sname] Harap hapus tabelnya"
            m "[bname] Ikut denganku"
            scene stdinner2 with dissolve
            s "..."
            scene stdinner3 with fade
            b "Apa yang salah?"
            m "Cheryl menelepon dan dia bilang dia akan memberi tahu Stewart"
            b "Tentang apa?"
            m "Tentang pekerjaan saya"
            b "Biarkan dia tahu, apa -apaan"
            "[mname] mulai menangis"
            b "Oh fuck, jangan khawatir, aku akan berbicara dengannya"
            scene stdinner4 with dissolve
            m "Terima kasih"
            scene stdinner5 with dissolve
            if mrel >=250:
                scene stdinner6 with dissolve
                "..."
                scene stdinner7 with dissolve
                "..."
                pass
            elif mfuckedsober >=1:
                scene stdinner6 with dissolve
                "..."
                scene stdinner7 with dissolve
                "..."
                scene stdinner8 with fade
                m "Mhhm"
                scene stdinner9 with dissolve
                m "Ahh"
                scene stdinner12 with dissolve
                "..."
                scene stdinner11 with dissolve
                m "Ughh"
                scene stdinner10 with dissolve
                m "Saya perlu bersantai [bname]"
                pass
            else:

                pass

            m "Saya perlu mandi air panas dan tidur"
            b "All right"
            b "Saya akan pergi melihat Cheryl sekarang"
            scene stdinner13 with fade
            c "Oh hai [bname]"
            c "Kejutan yang menyenangkan"
            b "Tolong, bukankah Anda akan meninggalkan kami sendirian"
            scene stdinner14 with dissolve
            if persistent.patch_enabled:
                c "Jangan berbicara dengan bibi Anda seperti itu"
                pass
            else:
                c "Jangan berbicara dengan saya seperti itu"
                pass
            c "Dan aku tidak akan meninggalkanmu sendirian sampai ..."
            b "Sampai apa?"
            if melsw >= 8:
                c "Sampai Anda mengambil fotonya dengan kliennya"
                pass
            else:
                c "Sampai Anda memberi saya beberapa foto dia dalam posisi tidak senonoh"
                pass
            scene stdinner15 with dissolve
            c "Sekarang duduk dan tunggu"
            b "Apa -apaan!"
            b "No way"
            c "Don't speak"
            scene stdinner16 with fade
            c "Biarkan minum, mungkin Anda berubah pikiran"
            scene stdinner17 with dissolve
            c "Cheers"
            b "Cheers"
            c "Jadi, apakah Anda akan meninggalkan kami sendirian?"
            c "Tidak sebelum saya membuktikan bahwa dia menyebalkan"
            b "Dan apa yang membuatmu?"
            scene stdinner18 with dissolve
            c "Saya sudah satu, Anda tidak dapat memenangkan argumen ini"
            c "Tapi aku benci ketika seseorang berpura -pura suci sementara dia tidak"
            c "Kemarilah"
            scene stdinner19 with dissolve
            c "Apakah Anda akan melakukannya atau tidak?"
            b "Lakukan apa?"
            scene stdinner20 with dissolve
            b "Ini?"
            scene stdinner21 with fade
            c "Anak laki -laki yang mudah"
            scene chap
            b "Ah"
            "..."
            b "Hmm"
            c "Ah"
            "..."
            scene stdinner22 with dissolve
            $ persistent.unlock_47 = True
            c "Ahhh"
            scene stdinner13 with fade
            b "Seperti yang kami setujui"
            c "Saya akan memikirkannya"
            scene stdinner23 with fade
            m "Jadi?"
            b "Dia akan diam"
            m "Apa kamu yakin?"
            b "Yes"
            s "Siapa yang kamu bicarakan"
            m "[sname] Apa yang kamu lakukan di sini?"
            m "Tolong pergi ke kamar Anda"
            $ snupset += 1
            "[sname] menjadi lebih kesal"
            scene etv_ss with dissolve
            s "Hm"
            m "Tolong tinggalkan kami sendiri"
            scene stdinner24 with fade
            m "Bagaimana Anda meyakinkannya?"
            b "Saya memiliki cara saya"
            "..."
            b "Apa yang kita tonton?"
            m "Tidak ada, saya akan tidur"
            scene stdinner25 with dissolve
            m "Selamat malam"
            b "{i} (Saya kira saya akan tidur juga) {/i}"
            jump newdays






        elif mbunknown == 1 and day ==1:
            scene dinnerb with fade
            m "Tepat tepat waktu [bname]"
            m "Let's eat"
            scene dinnerb1 with dissolve
            mb "Terima kasih untuk makanan yang enak [mname]"
            mb "Anda memiliki keterampilan memasak yang baik"
            m "Anda menyambut sayang"
            scene dinnerb2 with fade
            mb "Terima kasih untuk makan malam [mname]"
            m "Sampai jumpa besok Adam"
            scene dinnerb3 with dissolve
            $ mbvisit += 1
            if persistent.patch_enabled:
                s "Mom"
                pass
            else:
                s "Ummm"
                pass
            m "Yes"
            s "Siapa dia?"
            m "Aku sudah memberitahumu, seorang rekan kerja"
            m "Seorang kolega di tempat kerja"
            s "Maksudku, dia datang untuk makan malam"
            m "Saya mengundangnya, dia tinggal sendiri"
            m "Dan tidak ada orang yang memasak untuknya"
            s "Ah"
            b "{i} (Saya tidak membeli omong kosong ini) {/i}"
            m "Selesaikan studi Anda!"
            scene hall_n with fade
            "..."
            call screen gnav

        elif mbvisit >= 1 and day ==3:
            scene dinnerb with fade
            m "Tepat tepat waktu [bname]"
            m "Let's eat"
            $ mbtv = 1
            scene dinnerb1 with dissolve
            mb "Terima kasih untuk makanan yang enak [mname]"
            mb "Anda memiliki keterampilan memasak yang baik"
            m "Anda menyambut sayang"
            m "Baiklah [sname] [bname]"
            m "Selesaikan studi Anda!"
            b "Hah!"
            s "Ok"
            scene hall_n with fade
            "..."
            call screen gnav
        else:

            pass
        scene dinner with fade
        m "Tepat tepat waktu [bname]"
        scene dinner1 with dissolve
        "..."
        menu:
            "Bicaralah dengan [sname]*":
                menu:
                    "Bagaimana studi Anda?*":
                        scene dinner_s with dissolve
                        s "Apa yang kamu bicarakan?"
                        b "Saya hanya memeriksa jika Anda membutuhkan bantuan saya"
                        scene dinner_s1 with dissolve
                        s "Grrr"
                        b "Hahahah"
                        if badgrds ==0 and workrequest ==3:
                            $ badgrds = 1
                            scene dinner_s6 with dissolve
                            m "Omong -omong ..."
                            m "Saya menerima email hari ini"
                            s "Huh"
                            m "Kelas Anda sangat buruk"
                            s "Sorry"
                            scene dinner_s6b with dissolve
                            m "Pastikan Anda membantunya!"
                            b "Yes ma'am"
                            pass
                        else:
                            pass
                    "Ada pembaruan tentang halaman Anda?*":


                        scene dinner_s2 with dissolve
                        s "Halaman yang mana?"
                        b "Kamu tahu"
                        scene dinner_s3 with dissolve
                        "..."
                        scene dinner_s4 with dissolve
                        b "{i}(Ahahaha){/i}"
                        b "Ya benar, maaf saya bingung"
                        scene dinner_s5 with dissolve
                        "..."
                        if instadone == 2 and instatalkm ==0:
                            scene dinner1 with dissolve
                            m "Halaman mana yang kamu bicarakan?"
                            scene dinner_s6 with dissolve
                            s "Nothing"
                            m "Saya mengatakan halaman yang mana?"
                            $ instatalkm = 1
                            s "Saya ingin membuat halaman instan"
                            m "Potong omong kosong ini [sname]!"
                            m "Fokus pada sesuatu yang berguna sebagai gantinya!"
                            pass

                        elif instatalkm == 1 and coversname == 0:
                            scene dinner1 with dissolve
                            m "Halaman mana yang kamu bicarakan?"
                            scene dinner_s6 with dissolve
                            s "Nothing"
                            m "Saya mengatakan halaman yang mana?"
                            s "Saya ingin membuat halaman instan"
                            scene dinner_s6b with dissolve
                            m "Apa ini [bname]?"
                            b "Berbuat salah..."
                            menu:
                                "Menutupinya":
                                    b "Ini adalah halaman game yang saya buat untuk bersenang -senang"
                                    b "Dan dia pikir itu buang -buang waktu"
                                    b "Jadi saya selalu menggodanya tentang hal itu"
                                    $ coversname = 1
                                    $ showcoverpage = 1
                                    m "Dia benar, buang -buang waktu"
                                    m "Saya ingin melihat halaman itu"
                                    b "Uhmm ya pasti, aku akan menunjukkannya padamu nanti"
                                    "..."
                                    pass
                                "Katakan yang sebenarnya":

                                    b "Kami membuat halaman untuknya"
                                    b "Dan..."
                                    show screen sreldw
                                    $ srel -= 1
                                    m "Dan apa?"
                                    hide screen sreldw
                                    b "Lihat, itu hanya untuk bersenang -senang"
                                    m "Jangan lihat aku [bname]"
                                    m "Anda pergi dan menghapus halaman itu"
                                    scene dinner_s6 with dissolve
                                    m "Dan kamu wanita muda"
                                    m "Anda lebih baik memotong omong kosong ini"
                                    m "Dan fokus pada studi Anda"
                                    s "Hmmp baik -baik saja"
                                    "..."
                                    pass
                        else:


                            pass
            "Bicaralah dengan [mname]*":



                if persistent.patch_enabled:
                    menu:
                        "Apakah Ayah meneleponmu?":
                            scene dinner_m with dissolve
                            m "No"
                            m "Apakah dia meneleponmu?"
                            menu:
                                "Berbohong":
                                    $ staway += 1
                                    $ mrel += 5
                                    "TIDAK"
                                    pass
                                "Katakan yang sebenarnya":

                                    b "Dia sedang memeriksa apakah kita baik -baik saja"
                                    m "Dan apa yang kamu katakan padanya?"
                                    b "Saya mengatakan kepadanya bahwa kami baik -baik saja"
                                    pass
                                "Belum dia meneleponmu?":

                                    m "No"
                                    b "Anda tahu apa!"
                                    b "Aku akan meneleponnya malam ini"
                                    m "Tidak [bname] Don \ 't!"
                                    b "Tapi kenapa tidak?"
                                    m "Saya bilang jangan!"
                                    b "Ok"
                                    if smoneym == 1:
                                        b "So [sname]"
                                        scene dinner_s with dissolve
                                        s "Yes"
                                        b "Tentang ponsel Anda, apakah masih berfungsi?"
                                        s "Ya tapi sangat lambat, dan terkadang crash"
                                        b "Hmm ok saya lihat"
                                        scene dinner9 with dissolve
                                        m "Waktu makan malam adalah untuk makan, tidak berbicara"
                                        pass

                        "Katakan padanya bahwa Anda telah bertemu dengan Bibi Cheryl" if cherylfoundout == 1:
                            scene dinner_m with dissolve
                            $ cherylfoundout = 2
                            m "Dimana kamu bertemu dengannya?"
                            b "Di tempat saya bekerja"
                            b "Dia datang dengan pemiliknya"
                            m "Apakah mereka tahu di mana Anda tinggal?"
                            b "Saya kira tidak demikian"
                            m "Apa maksudmu kamu tidak berpikir begitu?"
                            b "Mereka tidak tahu, jangan khawatir"
                            m "Saya harap dia tidak akan mencari tahu, dan memberi tahu Stewart, saya tidak ingin melihatnya di depan pintu saya"
                            s "Anda masih belum memaafkannya setelah sekian lama?"
                            pass

                        "Ada berita dari Bibi Cheryl?" if cherylfoundout >= 2 and mcallcheryl == 1:
                            scene dinner_mc with dissolve
                            m "Tidak, saya akan meneleponnya nanti"
                            s "Bibi Cheryl!"
                            $ mcallcheryl = 2
                            m "Sekarang makan, kalian berdua"
                            b "Ok"
                            scene dinner_m with dissolve
                            "..."
                            pass
                else:


                    menu:
                        "Apakah Stewart menelepon Anda?":
                            scene dinner_m with dissolve
                            m "No"
                            m "Apakah dia meneleponmu?"
                            menu:
                                "Berbohong":
                                    $ mrel += 5
                                    $ staway += 1
                                    "TIDAK"
                                    pass
                                "Katakan yang sebenarnya":

                                    b "Dia sedang memeriksa apakah kita baik -baik saja"
                                    m "Dan apa yang kamu katakan padanya?"
                                    b "Saya mengatakan kepadanya bahwa kami baik -baik saja"
                                    pass
                                "Belum dia meneleponmu?":

                                    m "No"
                                    b "Anda tahu apa!"
                                    b "Aku akan meneleponnya malam ini"
                                    m "Tidak [bname] Don \ 't!"
                                    b "Tapi kenapa tidak?"
                                    m "Saya bilang jangan!"
                                    b "Ok"
                                    if smoneym == 1:
                                        b "So [sname]"
                                        scene dinner_s with dissolve
                                        s "Yes"
                                        b "Tentang ponsel Anda, apakah masih berfungsi?"
                                        s "Ya tapi sangat lambat, dan terkadang crash"
                                        b "Hmm ok saya lihat"
                                        scene dinner9 with dissolve
                                        m "Waktu makan malam adalah untuk makan, tidak berbicara"
                                        pass

                        "Katakan padanya bahwa Anda telah bertemu Cheryl" if cherylfoundout == 1:
                            scene dinner_m with dissolve
                            $ cherylfoundout = 2
                            m "Dimana kamu bertemu dengannya?"
                            b "Di tempat saya bekerja"
                            b "Dia datang dengan pemiliknya"
                            m "Apakah mereka tahu di mana Anda tinggal?"
                            b "Saya kira tidak demikian"
                            m "Apa maksudmu kamu tidak berpikir begitu?"
                            b "Mereka tidak tahu, jangan khawatir"
                            m "Saya harap dia tidak akan mencari tahu, dan memberi tahu Stewart, saya tidak ingin melihatnya di depan pintu saya"
                            s "Anda masih belum memaafkannya setelah sekian lama?"
                            pass

                        "Ada berita dari Cheryl?" if cherylfoundout >= 2 and mcallcheryl == 1:
                            scene dinner_mc with dissolve
                            m "Tidak, saya akan meneleponnya nanti"
                            s "Bibi Cheryl!"
                            $ mcallcheryl = 2
                            m "Sekarang makan, kalian berdua"
                            b "Ok"
                            scene dinner_m with dissolve
                            "..."
                            pass


        m "..."
        scene dinner_m1 with dissolve
        b "{i} (apa yang terjadi padanya) {/i}"
        s "..."
        m "[sname] Harap hapus tabelnya"
        m "Saya perlu mandi air panas dan tidur"
        s "Sure"
        if startnework ==1 and ticketrequested ==0:
            s "Ermm"
            if persistent.patch_enabled:
                s "Mom"
                m "Apa?"
                s "Rowena mengundang saya untuk konser musik"
                m "Jadi?"
                s "Saya perlu membeli tiket untuk diri saya sendiri"
                m "Lupakan tentang hal itu kita tidak punya uang untuk itu"
                $ ticketrequested = 1
                scene dinner_m1_sad with dissolve
                s "..."
                b "{i} (hmm mungkin saya bisa bertanya kepada Rowena di mana saya bisa membeli ini) {/i}"
                b "{i} (Saya akan bertanya padanya saat kita mengunjunginya lain kali) {/i}"
                b "{i} (atau mengapa tidak bertanya [sname] secara langsung, saya akan memeriksa dengannya di kamarnya pada pukul 19:00) {/i}"
                pass
            else:


                s "[mname]"
                m "Apa?"
                s "Rowena mengundang saya untuk konser musik"
                m "Jadi?"
                s "Saya perlu membeli tiket untuk diri saya sendiri"
                m "Lupakan tentang hal itu kita tidak punya uang untuk itu"
                $ ticketrequested = 1
                scene dinner_m1_sad with dissolve
                s "..."
                b "{i} (hmm mungkin saya bisa bertanya kepada Rowena di mana saya bisa membeli ini) {/i}"
                b "{i} (Saya akan bertanya padanya saat kita mengunjunginya lain kali) {/i}"
                b "{i} (atau mengapa tidak bertanya [sname] secara langsung, saya akan memeriksa dengannya di kamarnya pada pukul 19:00) {/i}"
                pass
        elif startnework ==1 and laptoprequested ==0:
            s "Ermm"
            if persistent.patch_enabled:
                s "Mom"
                m "Apa?"
                s "Bisakah saya mendapatkan laptop baru"
                m "Apa??"
                s "Punyaku sudah lambat dan ..."
                m "Ini tidak lambat sama sekali, kami membelinya tahun lalu untuk Anda"
                m "[sname] Anda tahu bahwa kami tidak punya uang"
                s "Ya tapi ..."
                m "Jadi Anda sudah tahu jawaban saya"
                $ laptoprequested = 1
                scene dinner_m1_sad with dissolve
                s "..."
                b "{i}(Hmm){/i}"
                pass
            else:


                s "[mname]"
                m "Apa?"
                s "Bisakah saya mendapatkan laptop baru"
                m "Apa??"
                s "Punyaku sudah lambat dan ..."
                m "Ini tidak lambat sama sekali, kami membelinya tahun lalu untuk Anda"
                m "[sname] Anda tahu bahwa kami tidak punya uang"
                s "Ya tapi ..."
                m "Jadi Anda sudah tahu jawaban saya"
                $ laptoprequested = 1
                scene dinner_m1_sad with dissolve
                s "..."
                b "{i}(Hmm){/i}"
                pass
        else:
            pass


        "..."
        if cherylfoundout == 2:
            jump followmnamech

        elif btoldcheryl ==1 and bnamefixcheryl ==0:
            play sound "sounds/doorbell.wav"
            m "Siapa sekarang?"
            stop sound
            jump chprb


        elif cherylevent ==5:
            $ cherylevent = 6
            jump cherylconfront

        elif cherylevent ==6 and day == 2 and mrob <3:
            jump cherylvisit


        elif mcallcheryl ==2 and cherylevent <=1:
            $ cherylevent = 1
            jump cherylnight

        elif day ==3:
            scene dinner3 with fade
            "..."
            menu:
                "Tanyakan apakah [sname] membutuhkan bantuan":
                    b "Apakah Anda membutuhkan bantuan dengan hidangan?"
                    scene dinner4 with dissolve
                    s "Tidak, tapi terima kasih telah bertanya"
                    b "Oke, lihat ya"
                    scene hall_n with fade
                    "..."
                    call screen gnav
                "Ikuti [mname]":

                    b "{i} (mari kita lihat) {/i}"
                    scene room3 with fade
                    b "Hmmm"
                    b "Apakah semuanya baik -baik saja?"
                    if mrel >=35:
                        scene toi_m_n with dissolve
                        m "Yes [bname]"
                        m "I'm ok"
                        b "Tentu?"
                        m "Ya tolong, saya hanya mandi"
                        b "Oke..."
                        scene toi_m_n7 with dissolve
                        "..."
                        m "Please go"
                        if workrequest ==3 and mrel >=50:
                            scene toi_m_n8 with dissolve
                            "..."
                            scene toi_m_n1 with fade
                            m "{i} (pekerjaan ini mengambil tol pada saya) {/i}"
                            m "{i} (dan tidak ada) {/i}"
                            "..."
                            m "{i} (Anda dapat berhenti [mname]) {/i}"
                            m "{i} (Anda bisa \ 't) {/i}"
                            scene toi_m_n1pov with dissolve
                            m "{i} (hmmm itu rendam yang sangat dibutuhkan) {/i}"
                            b "Saya minta maaf..."
                            m "Ya [bname] Apa yang Anda inginkan?"
                            b "Saya sangat perlu menggunakan toilet"
                            scene toi_m_n9 with dissolve
                            m "Masuk, aku di bak mandi"
                            if elaine_convince ==4 and mrel >=150:
                                b "Pintunya?"
                                m "Itu tidak terkunci, masuk"
                                b "Huh, saya pikir itu terkunci, oke"
                                scene toi_m_n10a with dissolve
                                "..."
                                scene toi_m_n11 with dissolve
                                b "{i} (sialan, saya perlu memikirkan sesuatu) {/i}"
                                scene toi_m_n10 with dissolve
                                b "I'm done"
                                m "Tolong beri saya handuk"
                                b "Dimana itu?"
                                scene toi_m_n15a with dissolve
                                m "There"
                                b "Oh Ok"
                                scene toi_m_n16a with dissolve
                                m "Thanks"
                                b "{i} (keren, dia tidak lagi menutupi payudaranya) {/i}"
                                m "Anda bisa pergi sekarang"
                                b "Ok"
                                scene black
                                "..."
                                scene hall_n with fade
                                "..."
                                call screen gnav
                            else:
                                m "Langsung ke toilet"
                                b "Sure"
                                b "Pintunya?"
                                m "Itu tidak terkunci, masuk"
                                b "Huh, saya pikir itu terkunci, oke"
                                scene toi_m_n10 with dissolve
                                "..."
                                pass
                            scene toi_m_n11 with dissolve
                            b "{i} (sialan, saya perlu memikirkan sesuatu) {/i}"
                            scene toi_m_n10 with dissolve
                            b "I'm done"
                            if mrel >=100:
                                m "Tolong beri saya handuk"
                                b "Dimana itu?"
                                scene toi_m_n15 with dissolve
                                m "There"
                                b "Oh Ok"
                                scene toi_m_n16 with dissolve
                                m "Thanks"
                                m "Anda bisa pergi sekarang"
                                b "Ok"
                                scene black
                                "..."
                                scene hall_n with fade
                                "..."
                                call screen gnav
                            else:
                                m "Tolong langsung"
                                b "Sure"
                                scene black
                                "..."
                                scene hall_n with fade
                                "..."
                                call screen gnav
                        else:


                            scene toi_m_n1 with fade
                            "..."
                            scene black
                            "..."
                            scene hall_n with fade
                            "..."
                            call screen gnav
                    else:

                        scene toi_m_n with dissolve
                        m "Yes [bname]"
                        m "I'm ok"
                        b "Tentu?"
                        m "Ya tolong, saya hanya mandi"
                        b "Oke..."
                        scene toi_m_n1 with fade
                        "..."
                        scene black
                        "Naikkan poin Anda menjadi 35"
                        scene hall_n with fade
                        "..."
                        call screen gnav

        elif day ==5:
            scene dinner3 with fade
            "..."
            menu:
                "Tanyakan apakah [sname] membutuhkan bantuan":
                    b "Apakah Anda membutuhkan bantuan dengan hidangan?"
                    scene dinner4 with dissolve
                    if srel >=10:
                        jump snamedishes
                    else:

                        pass
                    s "Tidak, tapi terima kasih telah bertanya"
                    b "Oke, lihat ya"
                    scene hall_n with fade
                    "..."
                    call screen gnav
                "Ikuti [mname]":



                    b "{i} (mari kita lihat) {/i}"
                    scene room3 with fade
                    b "Hmmm"
                    b "Apakah semuanya baik -baik saja?"
                    if mrel >=35:
                        scene toi_m_n with dissolve
                        m "Yes [bname]"
                        m "I'm ok"
                        b "Tentu?"
                        m "Ya tolong, saya hanya mandi"
                        b "Oke..."
                        scene toi_m_n7 with dissolve
                        "..."
                        m "Please go"
                        if workrequest ==3 and mrel >=60:
                            scene toi_m_n8 with dissolve
                            "..."
                            scene toi_m_n1 with fade
                            m "{i} (pekerjaan ini mengambil tol pada saya) {/i}"
                            m "{i} (dan tidak ada) {/i}"
                            "..."
                            m "{i} (Anda dapat berhenti [mname]) {/i}"
                            m "{i} (Anda bisa \ 't) {/i}"
                            scene toi_m_n1pov with dissolve
                            m "{i} (hmmm itu rendam yang sangat dibutuhkan) {/i}"
                            b "Saya minta maaf..."
                            m "Ya [bname] Apa yang Anda inginkan?"
                            b "Saya sangat perlu menggunakan toilet"
                            scene toi_m_n9 with dissolve
                            m "Masuk, aku di bak mandi"
                            m "Langsung ke toilet"
                            b "Sure"
                            b "Pintunya?"
                            m "Itu tidak terkunci, masuk"
                            b "Huh, saya pikir itu terkunci, oke"
                            scene toi_m_n10 with dissolve
                            "..."
                            menu:
                                "Ambil tempat sampah":
                                    scene toi_m_n12 with dissolve
                                    b "{i} (mungkin jika memakan waktu lebih lama, sampai dia selesai) {/i}"
                                    "..."
                                    m "Apakah Anda selesai [bname]"
                                    b "Not yet"
                                    m "Oke, tetaplah di tempat Anda berada, saya keluar dari bak mandi"
                                    b "Ok"
                                    "..."
                                    b "Apakah kamu sudah selesai"
                                    m "Hanya satu detik"
                                    scene toi_m_n13 with dissolve
                                    b "{i}(Wow){/i}"
                                    scene toi_m_n14 with dissolve
                                    m "Anda ingin memberi tahu saya sesuatu?"
                                    menu:
                                        "Terima kasih":
                                            b "Ya, saya ingin berterima kasih atas semua yang Anda lakukan untuk kami"
                                            scene toi_m_n14hug with dissolve
                                            show screen mrelup
                                            m "Anda menyambut sayang"
                                            hide screen mrelup
                                            $ mrel += 1
                                            menu:
                                                "Peluknya":
                                                    scene toi_m_n15hug with dissolve
                                                    if mrel >=250:
                                                        m "..."
                                                        scene toi_m_n16hug with dissolve
                                                        $ mtoiletsuspicious += 1
                                                        m "{i} (apakah dia naif ?!) {/i}"
                                                        if mtoiletsuspicious >2:
                                                            m "{i} (hanya ada satu cara untuk mengetahuinya) {/i}"
                                                            scene toi_m_n15hug with dissolve
                                                            m "Sebentar saja izinkan saya mengenakan pakaian saya"
                                                            scene toi_m_n17hug with dissolve
                                                            "..."
                                                            scene toi_m_n18hug with dissolve
                                                            b "{i} (wow apa yang terjadi?!) {/i}"
                                                            m "Tolong ambilkan pakaian dalam itu dari laci"
                                                            scene toi_m_n19hug with dissolve
                                                            "..."
                                                            scene toi_m_n20hug with dissolve
                                                            b "Ini dia"
                                                            m "Terima kasih"
                                                            m "Turn"
                                                            scene toi_m_n19hug with dissolve
                                                            "..."
                                                            scene toi_m_n21hug with dissolve
                                                            m "Jadi, apakah kamu menyukainya?"
                                                            b "Seperti apa?"
                                                            m "The lingerie"
                                                            b "Hmm saya tidak tahu"
                                                            b "Belum pernah melihat satu pada wanita sebelumnya"
                                                            b "Tapi ya itu bagus"
                                                            m "Terima kasih"
                                                            m "Anda mungkin pergi sekarang"
                                                            b "Ok"
                                                            b "Sampai jumpa"
                                                            scene room3 with dissolve
                                                            b "{i} (itu bagus) {/i}"
                                                            scene toi_m_n22hug with fade
                                                            "..."
                                                            scene black
                                                            "Itu semua dalam opsi ini"
                                                            scene hall_n with fade
                                                            "..."
                                                            call screen gnav
                                                        else:
                                                            m "Anda bisa pergi sekarang"
                                                            scene room3 with dissolve
                                                            b "..."
                                                            scene black
                                                            "..."
                                                            scene toi_m_n22hug with fade
                                                            m "{i} (i \ 'll lihat apakah itu berulang untuk beberapa kali) {/i}"
                                                            m "{i} (lalu aku akan melakukan sesuatu tentang hal itu) {/i}"
                                                            scene hall_n with fade
                                                            "..."
                                                            call screen gnav
                                                    else:


                                                        m "Anda bisa pergi sekarang"
                                                        scene black
                                                        "Naikkan poin hubungan Anda menjadi 250"
                                                        scene hall_n with fade
                                                        "..."
                                                        call screen gnav
                                                "Meninggalkan":

                                                    pass
                                            scene black
                                            "..."
                                            scene hall_n with fade
                                            "..."
                                            call screen gnav
                                        "Tidak ada":

                                            b "Err tidak, keluar saja"
                                            m "All right"
                                            scene black
                                            "..."
                                            scene hall_n with fade
                                            "..."
                                            call screen gnav
                                "Kencing":

                                    scene toi_m_n11 with dissolve
                                    "..."
                                    scene toi_m_n10 with dissolve
                                    b "I'm done"
                                    m "Tolong langsung"
                                    b "{i} (itu terlalu cepat) {/i}"
                                    b "Sure"
                                    scene black
                                    "..."
                                    scene hall_n with fade
                                    "..."
                                    call screen gnav
                        else:


                            scene toi_m_n1 with fade
                            "..."
                            scene black
                            "Naikkan poin [mname] Anda menjadi 60 dan [mname] seharusnya mulai bekerja di klub"
                            scene hall_n with fade
                            "..."
                            call screen gnav
                    else:

                        scene toi_m_n with dissolve
                        m "Yes [bname]"
                        m "I'm ok"
                        b "Tentu?"
                        m "Ya tolong, saya hanya mandi"
                        b "Oke..."
                        scene toi_m_n1 with fade
                        "..."
                        scene black
                        "..."
                        scene hall_n with fade
                        "..."
                        call screen gnav



        elif day ==4:
            scene dinner3 with fade
            "..."
            menu:
                "Tanyakan apakah [sname] membutuhkan bantuan":
                    b "Apakah Anda membutuhkan bantuan dengan hidangan?"
                    scene dinner4 with dissolve
                    s "Tidak, tapi terima kasih telah bertanya"
                    b "Oke, lihat ya"
                    scene hall_n with fade
                    "..."
                    call screen gnav
                "Ikuti [mname]":

                    b "{i} (mari kita lihat) {/i}"
                    scene room3 with fade
                    b "Hmmm"
                    b "Apakah semuanya baik -baik saja?"
                    if mrel >=35:
                        scene toi_m_n with dissolve
                        m "Yes [bname]"
                        m "I'm ok"
                        b "Tentu?"
                        m "Ya tolong, saya hanya mandi"
                        b "Oke..."
                        scene toi_m_n7 with dissolve
                        "..."
                        m "Please go"
                        if workrequest ==3 and mrel >=60:
                            scene toi_m_n8 with dissolve
                            "..."
                            scene toi_m_n1 with fade
                            m "{i} (pekerjaan ini mengambil tol pada saya) {/i}"
                            m "{i} (dan tidak ada) {/i}"
                            "..."
                            m "{i} (Anda dapat berhenti [mname]) {/i}"
                            m "{i} (Anda bisa \ 't) {/i}"
                            scene toi_m_n1pov with dissolve
                            m "{i} (hmmm itu rendam yang sangat dibutuhkan) {/i}"
                            b "Saya minta maaf..."
                            m "Ya [bname] Apa yang Anda inginkan?"
                            b "Saya sangat perlu menggunakan toilet"
                            scene toi_m_n9 with dissolve
                            m "Masuk, aku di bak mandi"
                            m "Langsung ke toilet"
                            b "Sure"
                            b "Pintunya?"
                            m "Itu tidak terkunci, masuk"
                            b "Huh, saya pikir itu terkunci, oke"
                            scene toi_m_n10 with dissolve
                            "..."
                            menu:
                                "Ambil tempat sampah":
                                    scene toi_m_n12 with dissolve
                                    b "{i} (mungkin jika memakan waktu lebih lama, sampai dia selesai) {/i}"
                                    "..."
                                    m "Apakah Anda selesai [bname]"
                                    b "Not yet"
                                    m "Oke, tetaplah di tempat Anda berada, saya keluar dari bak mandi"
                                    b "Ok"
                                    "..."
                                    b "Apakah kamu sudah selesai"
                                    m "Hanya satu detik"
                                    scene toi_m_n13 with dissolve
                                    b "{i}(Wow){/i}"
                                    scene toi_m_n14 with dissolve
                                    m "Anda ingin memberi tahu saya sesuatu?"
                                    menu:
                                        "Terima kasih":
                                            b "Ya, saya ingin berterima kasih atas semua yang Anda lakukan untuk kami"
                                            scene toi_m_n14hug with dissolve
                                            show screen mrelup
                                            m "Anda menyambut sayang"
                                            hide screen mrelup
                                            $ mrel += 1
                                            menu:
                                                "Peluknya":
                                                    scene toi_m_n15hug with dissolve
                                                    if mrel >=250:
                                                        m "..."
                                                        scene toi_m_n16hug with dissolve
                                                        $ mtoiletsuspicious += 1
                                                        m "{i} (apakah dia naif ?!) {/i}"
                                                        if mtoiletsuspicious >2:
                                                            m "{i} (hanya ada satu cara untuk mengetahuinya) {/i}"
                                                            scene toi_m_n15hug with dissolve
                                                            m "Sebentar saja izinkan saya mengenakan pakaian saya"
                                                            scene toi_m_n17hug with dissolve
                                                            "..."
                                                            scene toi_m_n18hug with dissolve
                                                            b "{i} (wow apa yang terjadi?!) {/i}"
                                                            m "Tolong ambilkan pakaian dalam itu dari laci"
                                                            scene toi_m_n19hug with dissolve
                                                            "..."
                                                            scene toi_m_n20hug with dissolve
                                                            b "Ini dia"
                                                            m "Terima kasih"
                                                            m "Turn"
                                                            scene toi_m_n19hug with dissolve
                                                            "..."
                                                            scene toi_m_n21hug with dissolve
                                                            m "Jadi, apakah kamu menyukainya?"
                                                            b "Seperti apa?"
                                                            m "The lingerie"
                                                            b "Hmm saya tidak tahu"
                                                            b "Belum pernah melihat satu pada wanita sebelumnya"
                                                            b "Tapi ya itu bagus"
                                                            m "Terima kasih"
                                                            if mrel >=260:
                                                                m "Izinkan saya menunjukkan sesuatu yang lain"
                                                                scene toi_m_n21huga with dissolve
                                                                "..."
                                                                scene toi_m_n22huga with dissolve
                                                                menu:
                                                                    "Terus mencari":
                                                                        b "{i} (keren) {/i}"
                                                                        m "[bname]"
                                                                        pass
                                                                    "Berbelok":

                                                                        scene toi_m_n19hug with dissolve
                                                                        "..."
                                                                        scene toi_m_n23hug with dissolve
                                                                        "..."
                                                                        m "Jadi, apakah kamu suka ini?"
                                                                        b "Ya, hampir sama"
                                                                        pass
                                                            else:

                                                                pass
                                                            m "Anda mungkin pergi sekarang"
                                                            b "Ok"
                                                            b "Sampai jumpa"
                                                            scene room3 with dissolve
                                                            b "{i} (itu bagus) {/i}"
                                                            scene toi_m_n22hug with fade
                                                            "..."
                                                            scene black
                                                            "Itu semua dalam opsi ini"
                                                            scene hall_n with fade
                                                            "..."
                                                            call screen gnav
                                                        else:
                                                            m "Anda bisa pergi sekarang"
                                                            scene room3 with dissolve
                                                            b "..."
                                                            scene black
                                                            "..."
                                                            scene toi_m_n22hug with fade
                                                            m "{i} (i \ 'll lihat apakah itu berulang untuk beberapa kali) {/i}"
                                                            m "{i} (lalu aku akan melakukan sesuatu tentang hal itu) {/i}"
                                                            scene hall_n with fade
                                                            "..."
                                                            call screen gnav
                                                    else:


                                                        m "Anda bisa pergi sekarang"
                                                        scene black
                                                        "Naikkan poin hubungan Anda menjadi 250"
                                                        scene hall_n with fade
                                                        "..."
                                                        call screen gnav
                                                "Meninggalkan":

                                                    pass
                                            scene black
                                            "..."
                                            scene hall_n with fade
                                            "..."
                                            call screen gnav
                                        "Tidak ada":

                                            b "Err tidak, keluar saja"
                                            m "All right"
                                            scene black
                                            "..."
                                            scene hall_n with fade
                                            "..."
                                            call screen gnav
                                "Kencing":

                                    scene toi_m_n11 with dissolve
                                    "..."
                                    scene toi_m_n10 with dissolve
                                    b "I'm done"
                                    m "Tolong langsung"
                                    b "{i} (itu terlalu cepat) {/i}"
                                    b "Sure"
                                    scene black
                                    "..."
                                    scene hall_n with fade
                                    "..."
                                    call screen gnav
                        else:


                            scene toi_m_n1 with fade
                            "..."
                            scene black
                            "Naikkan poin [mname] Anda menjadi 60 dan [mname] seharusnya mulai bekerja di klub"
                            scene hall_n with fade
                            "..."
                            call screen gnav
                    else:

                        scene toi_m_n with dissolve
                        m "Yes [bname]"
                        m "I'm ok"
                        b "Tentu?"
                        m "Ya tolong, saya hanya mandi"
                        b "Oke..."
                        scene toi_m_n1 with fade
                        "..."
                        scene black
                        "..."
                        scene hall_n with fade
                        "..."
                        call screen gnav



        elif day ==1:
            scene dinner3 with fade
            "..."
            menu:
                "Tanyakan apakah [sname] membutuhkan bantuan":
                    b "Apakah Anda membutuhkan bantuan dengan hidangan?"
                    scene dinner4 with dissolve
                    if srel >=50:
                        jump snamedishes
                    else:

                        pass
                    s "Tidak, tapi terima kasih telah bertanya"
                    b "Oke, lihat ya"
                    scene hall_n with fade
                    "..."
                    call screen gnav
                "Ikuti [mname]":

                    b "{i} (mari kita lihat) {/i}"
                    scene room3 with fade
                    b "Hmmm"
                    b "Apakah semuanya baik -baik saja?"
                    scene toi_m_n with dissolve
                    m "Yes [bname]"
                    m "I'm ok"
                    m "Ya tolong, saya hanya mandi"
                    b "Tapi saya ingin menggunakan toilet"
                    if mrel >20:
                        m "Ok masuk"
                        m "Tapi tolong buat cepat"
                        scene toi_m_n4 with fade
                        "..."
                        b "Done"
                        m "Terima kasih, sekarang tolong keluar"
                        b "Sure"
                        scene toi_m_n6a with fade
                        "..."
                        if elaine_convince == 4 and mrel>= 80 and mnightie == 2:
                            m "[bname]!"
                            m "Masih di sana?"
                            b "Yes"
                            b "Apa itu?"
                            m "Kembali"
                            scene toi_m_n7 with fade
                            m "Follow me"
                            jump mroom_practice1
                        else:

                            pass
                        scene room3 with fade
                        "..."
                        call screen gnav
                    else:


                        pass
                    m "Tidak sekarang [bname]"
                    m "Beri aku 5 menit"
                    b "Ok"
                    scene toi_m_n1 with fade
                    "..."
                    scene black
                    "..."
                    scene hall_n with fade
                    "..."
                    call screen gnav
        else:
            b "{i} (saya kira saya \ 'l pergi tidur) {/i}"
            scene hall_n with fade
            "..."
            call screen gnav


    elif Hour == 21:
        if wk >= 1:
            if workrequest ==3:
                if day == 7:
                    if mburnt == 1:
                        jump mburn_nightevent
                    else:
                        jump eveningtv_afterwork

                elif startnework ==1 and day ==6:
                    jump evening_jennyout
                else:

                    jump eveningtv_afterwork
            else:
                pass
            scene hall_m_n8 with fade
            b "{i} (...) {/i}"
            b "Bisakah saya menonton TV dengan Anda?"
            scene hall_m_n9 with dissolve
            if mwork ==1:
                pass
            else:
                pass
            m "Ya, duduk"
            scene hall_m_n10 with fade
            b "Apa yang kita tonton?"
            m "Saya akan melihat apa yang ada"
            scene hall_m_n11 with dissolve
            m "Ya, mari kita menonton pertunjukan musik"
            if pornchanel == 0:
                menu:
                    "Katakan padanya untuk memakai saluran 5" if mrel >=10:
                        scene hall_m_n12 with dissolve
                        b "Saya tidak suka blues"
                        b "Dapatkah Anda berubah ke saluran kelima"
                        b "Mereka memiliki musik yang lebih baik"
                        scene hall_m_n11 with dissolve
                        m "Sure"
                        scene hall_m_n13 with dissolve
                        $ pornchanel = 1
                        "..."
                        scene hall_m_n14 with hpunch
                        m "Oh!"
                        scene hall_m_n15 with dissolve
                        m "Apa ..."
                        $ mrel -= 1
                        show screen mreldw
                        m "Mengapa Anda menyuruh saya mengubah ini"
                        hide screen mreldw
                        b "Saya ... saya tidak tahu"
                        m "Saya akan menelepon orang kabel besok"
                        b "Ya, jadi apa!"
                        scene hall_m_n16 with fade
                        m "Selamat malam!"
                        m "Pergi ke kamar Anda!"
                        scene hall_n with fade
                        b "{i} (sialan!) {/i}"
                        b "{i} (kurasa aku akan tidur juga) {/i}"
                        jump newdays
                    "Tontonlah":

                        scene hall_m_n12 with dissolve
                        b "Saya tidak suka blues"
                        m "Just watch"
                        scene hall_m_n11 with dissolve
                        "..."
                        scene hall_m_n10 with fade
                        m "Itu bagus"
                        b "Ya, membosankan"
                        scene hall_m_n16 with fade
                        m "Selamat malam!"
                        scene hall_n with fade
                        b "{i} (kurasa aku akan tidur juga) {/i}"
                        jump newdays
            else:
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
                    scene hall_m_n18 with dissolve
                    m "Terlihat bagus"
                    m "Saya suka film klasik"
                    b "{i} (sialan! Itu film erotis) {/i}"
                    b "{i} (Saya harus mengubahnya sekarang, jika tidak dia akan memblokir setiap saluran) {/i}"
                    scene hall_m_n12 with dissolve
                    b "Anda tahu apa, mengapa kami tidak melihat beberapa film dokumenter"
                    m "Anda tidak menyukai ini?"
                    b "TIDAK..."
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
                    b "{i} (kurasa aku akan tidur juga) {/i}"
                    jump newdays
                else:

                    pass
                scene hall_m_n11 with dissolve
                "..."
                scene hall_m_n10 with fade
                m "Itu bagus"
                b "Ya, membosankan"
                scene hall_m_n16 with fade
                m "Selamat malam!"
                scene hall_n with fade
                b "{i} (kurasa aku akan tidur juga) {/i}"
                jump newdays
        else:

            scene hall_n with fade
            b "{i} (tidak ada orang di sini) {/i}"
            b "{i} (Saya harus tidur) {/i}"
            jump newdays

    elif Hour >21:
        scene hall_n with fade
        b "{i} (tidak ada orang di sini) {/i}"
        b "{i} (Saya harus tidur) {/i}"
        jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
