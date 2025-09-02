label newwork_return:
    if mrob == 2:
        $ Hour += 1
        scene eveningrob with fade
        b "Hi"
        $ mrob = 3
        m "..."
        scene eveningrob1 with dissolve
        b "Huh"
        m "Katakan [sname] untuk menyiapkan makan malam"
        m "Saya akan tidur"
        scene nheveningmel1 with fade
        s "Dimana [mname]?"
        b "Dia pergi tidur"
        s "Hmm"
        b "Dia mengatakan bahwa Anda harus menyiapkan makan malam"
        s "Lebih baik memesan sesuatu yang siap"
        s "Apakah Anda punya uang?"
        b "Ya saya akan melakukannya"
        b "Dan setelah mungkin kita bisa ..."
        menu:
            "Tonton TV":
                s "Tapi saya memilih apa yang harus ditonton"
                b "Ok"
                scene black
                "SEMENTARA ITU"
                scene eveningrob2 with fade
                m "... Saya tidak ingin mendengarkan ini, bisakah Anda membuatnya?"
                scene eveningrob3 with dissolve
                e "Dia akan mengenali suaraku"
                m "{i} (biarkan gadis lain memanggilnya) {/i}"
                e "Ok saya akan melihat apa yang bisa saya lakukan"
                m "{i} (hubungi saya kembali) {/i}"
                e "Saya akan"
                m "{i} (apakah Rob disana?) {/i}"
                e "Tidak dia pergi hari ini"
                m "{i} (bisakah saya memintanya untuk mengikutinya dan mengambil beberapa foto untuk saya?) {/i}"
                e "Ya kenapa tidak"
                scene jopen1 with fade
                s "Itu makanan yang enak"
                b "Yeah"
                b "Jadi apa yang kita tonton?"
                b "Porno?"
                s "No"
                play sound "sounds/mobilering.wav"
                scene eveningrob4 with dissolve
                b "Huh, siapa itu?"
                stop sound
                scene eveningrob5 with dissolve
                b "Ya halo!"
                b "Siapa itu?"
                "..."
                b "Ah, apakah dia memberitahumu?"
                "..."
                b "Tempat yang sama?"
                b "Rumahnya?"
                b "Halo!?"
                scene eveningrob4 with dissolve
                b "Dia ditutup !!"
                s "Siapa itu?"
                b "Dia bilang Melinda menungguku"
                s "Siapa Melinda?"
                if snameworkmelinda ==4:
                    b "Itu wanita yang telah mengunjungi untuk pekerjaan Anda"
                    s "Oh ya saya lupa"
                    pass
                else:
                    b "Itu wanita yang memiliki klub dan toko -toko lain di sini"
                    s "Oh, begitu"
                    pass
                scene jopen1 with dissolve
                b "Saya harus pergi"
                b "Apa anda mau ikut dengan saya?"
                s "Tidak, saya lebih baik pergi melihat Rowena"
                b "Ok nanti"
                scene black
                "..."
                scene eveningrob6 with fade
                "..."
                scene eveningrob7 with dissolve
                b "{i} (sialan, tidak ada orang di sini) {/i}"
                b "{i} (lebih baik saya pergi) {/i}"
                scene eveningrob8 with dissolve
                "..."
                scene eveningrob9 with dissolve
                "..."
                scene eveningrob10 with dissolve
                r "..."
                scene eveningrob11 with dissolve
                r "Saya pikir dia pergi ke toko"
                m "{i} (apakah kamu yakin?) {/i}"
                r "Ya dan saya mengambil foto baik di sini maupun di rumahnya"
                m "{i} (ok terima kasih Rob, tolong tetap padanya dan beri saya informasi) {/i}"
                scene eveningrob12 with fade
                play sound "sounds/doorbell.wav"
                "..."
                stop sound
                scene eveningrob13 with dissolve
                $ persistent.unlock_72 = True
                m "Rob, apa yang terjadi?"
                r "Saya pergi, dia ada di dekat toko"
                m "Apakah Anda pikir kita bisa memeriksa di mana dia sekarang?"
                r "Ya, tentu saja"
                scene eveningrob14 with dissolve
                "..."
                scene eveningrob15 with dissolve
                r "Di situlah aku kehilangan dia"
                scene eveningrob16 with dissolve
                r "Toko ditutup"
                m "Mungkin dia kembali ke rumah"
                m "Mari kita kembali"
                scene eveningrob17 with fade
                m "Dia belum di sini"
                scene eveningrob13 with dissolve
                m "Baiklah, terima kasih telah membantu"
                r "Jangan menyebutkannya"
                m "Saya akan menelepon Anda jika saya butuh bantuan"
                scene eveningrob12 with fade
                m "{i} (Rob adalah pria baik yang manis) {/i}"
                scene hall_n with fade
                "..."
                call screen gnav
            "Pergi melihat Rowena":


                if sgoestost >= 2:
                    s "Tidak, saya punya rencana untuk bertemu dengannya sendiri"
                    scene black
                    "..."
                    scene eveningrob6 with fade
                    "..."
                    scene eveningrob7 with dissolve
                    b "{i} (sialan, tidak ada orang di sini) {/i}"
                    b "{i} (lebih baik saya pergi) {/i}"
                    scene eveningrob8 with dissolve
                    "..."
                    scene eveningrob9 with dissolve
                    "..."
                    scene eveningrob10 with dissolve
                    r "..."
                    scene eveningrob11 with dissolve
                    r "Saya pikir dia pergi ke toko"
                    m "{i} (apakah kamu yakin?) {/i}"
                    r "Ya dan saya mengambil foto baik di sini maupun di rumahnya"
                    m "{i} (ok terima kasih Rob, tolong tetap padanya dan beri saya informasi) {/i}"
                    scene eveningrob12 with fade
                    play sound "sounds/doorbell.wav"
                    "..."
                    stop sound
                    scene eveningrob13 with dissolve
                    m "Rob, apa yang terjadi?"
                    r "Saya pergi, dia ada di dekat toko"
                    m "Apakah Anda pikir kita bisa memeriksa di mana dia sekarang?"
                    r "Ya, tentu saja"
                    scene eveningrob14 with dissolve
                    "..."
                    scene eveningrob15 with dissolve
                    r "Di situlah aku kehilangan dia"
                    scene eveningrob16 with dissolve
                    r "Toko ditutup"
                    m "Mungkin dia kembali ke rumah"
                    m "Mari kita kembali"
                    scene eveningrob17 with fade
                    m "Dia belum di sini"
                    scene eveningrob13 with dissolve
                    m "Baiklah, terima kasih telah membantu"
                    r "Jangan menyebutkannya"
                    m "Saya akan menelepon Anda jika saya butuh bantuan"
                    scene eveningrob12 with fade
                    m "{i} (Rob adalah pria baik yang manis) {/i}"
                    scene hall_n with fade
                    "..."
                    call screen gnav
                else:
                    s "Ya kenapa tidak"
                    s "Mari kita pesan makanan terlebih dahulu"
                    scene black
                    "SEMENTARA ITU"
                    scene eveningrob2 with fade
                    m "... Saya tidak ingin mendengarkan ini, bisakah Anda membuatnya?"
                    scene eveningrob3 with dissolve
                    e "Dia akan mengenali suaraku"
                    m "{i} (biarkan gadis lain memanggilnya) {/i}"
                    e "Ok saya akan melihat apa yang bisa saya lakukan"
                    m "{i} (hubungi saya kembali) {/i}"
                    e "Saya akan"
                    m "{i} (apakah Rob disana?) {/i}"
                    e "Tidak dia pergi hari ini"
                    m "{i} (bisakah saya memintanya untuk mengikutinya dan mengambil beberapa foto untuk saya?) {/i}"
                    e "Ya kenapa tidak"
                    scene jopen1 with fade
                    s "Itu makanan yang enak"
                    b "Yeah"
                    play sound "sounds/mobilering.wav"
                    scene eveningrob4 with dissolve
                    b "Huh, siapa itu?"
                    stop sound
                    scene eveningrob5 with dissolve
                    b "Ya halo!"
                    b "Siapa itu?"
                    "..."
                    b "Ah, apakah dia memberitahumu?"
                    "..."
                    b "Tempat yang sama?"
                    b "Rumahnya?"
                    b "Halo!?"
                    scene eveningrob4 with dissolve
                    b "Dia ditutup !!"
                    s "Siapa itu?"
                    b "Dia bilang Melinda menungguku"
                    s "Siapa Melinda?"
                    if snameworkmelinda ==4:
                        b "Itu wanita yang telah mengunjungi untuk pekerjaan Anda"
                        s "Oh ya saya lupa"
                        pass
                    else:
                        b "Itu wanita yang memiliki klub dan toko -toko lain di sini"
                        s "Oh, begitu"
                        pass
                    scene jopen1 with dissolve
                    b "Saya harus pergi"
                    b "Apa anda mau ikut dengan saya?"
                    s "Tidak, saya lebih baik pergi begitu rowena"
                    b "Ok nanti"
                    scene black
                    "..."
                    scene eveningrob6 with fade
                    "..."
                    scene eveningrob7 with dissolve
                    b "{i} (sialan, tidak ada orang di sini) {/i}"
                    b "{i} (lebih baik saya pergi) {/i}"
                    scene eveningrob8 with dissolve
                    "..."
                    scene eveningrob9 with dissolve
                    "..."
                    scene eveningrob10 with dissolve
                    r "..."
                    scene eveningrob11 with dissolve
                    r "Saya pikir dia pergi ke toko"
                    m "{i} (apakah kamu yakin?) {/i}"
                    r "Ya dan saya mengambil foto baik di sini maupun di rumahnya"
                    m "{i} (ok terima kasih Rob, tolong tetap padanya dan beri saya informasi) {/i}"
                    scene eveningrob12 with fade
                    play sound "sounds/doorbell.wav"
                    "..."
                    stop sound
                    scene eveningrob13 with dissolve
                    m "Rob, apa yang terjadi?"
                    r "Saya pergi, dia ada di dekat toko"
                    m "Apakah Anda pikir kita bisa memeriksa di mana dia sekarang?"
                    r "Ya, tentu saja"
                    scene eveningrob14 with dissolve
                    "..."
                    scene eveningrob15 with dissolve
                    r "Di situlah aku kehilangan dia"
                    scene eveningrob16 with dissolve
                    r "Toko ditutup"
                    m "Mungkin dia kembali ke rumah"
                    m "Mari kita kembali"
                    scene eveningrob17 with fade
                    m "Dia belum di sini"
                    scene eveningrob13 with dissolve
                    m "Baiklah, terima kasih telah membantu"
                    r "Jangan menyebutkannya"
                    m "Saya akan menelepon Anda jika saya butuh bantuan"
                    scene eveningrob12 with fade
                    m "{i} (Rob adalah pria baik yang manis) {/i}"
                    scene hall_n with fade
                    "..."
                    call screen gnav





    elif jenopen >=1 and melsw >= 9:
        $ Hour += 1
        scene hevening with fade
        "..."
        scene nhevening with dissolve
        m "Hi [bname]"
        b "Hi"
        b "Apa kabar hari ini?"
        m "Seperti biasa, sial"
        m "Aku akan pergi melihat Elaine"
        m "Katakan [sname] untuk menyiapkan makan malam"
        b "Err"
        b "Bisakah aku ikut denganmu?"
        m "No"
        m "Maksud saya ingin melihatnya sendiri"
        m "Saya akan berubah dan pergi, saya tidak ingin terlambat"
        scene black
        "..."
        scene jopen with fade
        m "Selamat malam"
        scene nheveningmel with dissolve
        b "..."
        scene nheveningmel1 with dissolve
        s "Kemana dia pergi?"
        b "Untuk melihat Elaine"
        s "Hmm"
        b "Dia mengatakan bahwa Anda harus menyiapkan makan malam"
        s "Lebih baik memesan sesuatu yang siap"
        s "Apakah Anda punya uang?"
        b "Ya saya akan melakukannya"
        b "Dan mari kita menonton TV"
        menu:
            "Tidak, [sname] ingin pergi melihat Rowena" if sgoestost >= 2:
                s "Saya akan pergi melihat Rowena"
                b "Hmm"
                b "Ok"
                scene neif0 with fade
                play sound "sounds/doorbell.wav"
                if neibrep >=1:
                    b "Datang"
                    stop sound
                    scene neif with dissolve
                    b "Oh Hi"
                    if persistent.patch_enabled:
                        n "Dimana ibumu"
                        pass
                    else:
                        n "Dimana Landlady Anda"
                        pass
                    b "Dia keluar"
                    n "Oh, begitu"
                    scene neif1 with dissolve
                    b "{i}(Hmm){/i}"
                    scene neif with dissolve
                    b "Mengapa Anda tidak masuk"
                    n "..."
                    scene neif2 with fade
                    b "Jadi di mana Masha, mengapa dia tidak ikut denganmu"
                    n "Hmm"
                    n "Dia pergi ke teman -temannya"
                    n "Jadi Anda suka masha"
                    b "Yah bukan itu ..."
                    b "Aku hanya ..."
                    n "Jangan malu, saya tahu bagaimana menurut Anda anak laki -laki"
                    n "Anda suka gadis muda"
                    menu:
                        "Tidak perlu":
                            b "Tidak semua pria"
                            pass
                        "Ya":
                            b "Yeah hehe"
                            n "Baiklah, aku akan sampai jumpa nanti"
                            n "Selamat malam"
                            b "{i} (sialan aku mengatakan sesuatu yang salah) {/i}"
                            b "Selamat malam"
                            scene neif0 with fade
                            b "Mari kita lihat apa yang ada di TV"
                            jump snamefuckst
                    if persistent.patch_enabled:
                        n "Jadi jam berapa ibumu kembali"
                        pass
                    else:
                        n "Jadi jam berapa pengembalian pemilik rumah Anda"
                        pass
                    b "Saya pikir dia akan terlambat"
                    n "Saya bertanya karena saya membutuhkan Anda untuk membantu menyirami tanaman saya"
                    b "Sekarang?"
                    n "Ya itu tidak akan membutuhkan banyak"
                    b "All right"
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
                                "Ok"
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
                    scene black
                    "Kembali ke [bname]"
                    scene neif3 with fade
                    n "Mari kita mulai dengan beberapa minuman"
                    b "Bagaimana dengan membantu Anda"
                    n "Later"
                    scene neif4 with dissolve
                    n "Cheers"
                    b "{i} (wanita ini adalah cougar) {/i}"
                    scene neif5 with hpunch
                    b "Huh"
                    n "Bersantai aku tidak akan menggigit"
                    scene neif6 with dissolve
                    b "Only here"
                    scene neif7 with dissolve
                    "..."
                    menu:
                        "Biarkan dia melanjutkan blowjob":
                            scene neif8 with fade
                            b "Ahh"
                            scene neif9 with dissolve
                            "..."
                            scene neif10 with dissolve
                            n "Ah"
                            scene neif11 with dissolve
                            n "Lakukan lambat waktu berikutnya"
                            b "Ok bagaimana dengan bunganya"
                            n "Anda sudah menyiramnya"
                            b "Ah begitu"
                            n "Anda bisa pergi sekarang"
                            b "Selamat malam"
                            jump snamefuckst
                        "Persetan dia":
                            scene neif12 with dissolve
                            n "..."
                            scene neif13 with dissolve
                            n "Ahhh pantatku"
                            scene neif14 with dissolve
                            n "..."
                            scene neif15 with dissolve
                            n "Harder"
                            scene neif16 with dissolve
                            "..."
                            scene neif17 with fade
                            n "Lakukan lambat waktu berikutnya"
                            n "Itu menyakitkan"
                            b "Ok bagaimana dengan bunganya"
                            n "Anda sudah menyiramnya"
                            b "Ah begitu"
                            n "Anda bisa pergi sekarang"
                            b "Selamat malam"
                            jump snamefuckst
                else:
                    jump snamefuckst
            "Ya [sname] akan memilih film":

                s "Tapi saya memilih apa yang harus ditonton"
                b "Ok"
                scene jopen1 with fade
                s "Itu makanan yang enak"
                b "Yeah"
                b "Jadi kita menonton film porno?"
                s "No"
                s "Saya memiliki sesuatu untuk ditunjukkan kepada Anda, mungkin Anda dapat mengambil beberapa foto untuk saya"
                b "Keren ya"
                scene jopen2 with fade
                s "Tada!"
                b "Oh God"
                b "Ini perlu ditembak"
                s "Bagaimana Anda ingin mengambil foto"
                b "Berbaring dengan cara seksi di sofa"
                scene jopen4 with fade
                b "Bagus"
                b "Tapi saya pikir lebih baik menghapus roknya"
                scene jopen5 with dissolve
                "..."
                if jenopen >=2:
                    "SEMENTARA ITU"
                    scene jpnm
                    "..."
                    "..."
                    m "..."
                    "..."
                    pass
                else:
                    pass
                scene jopen3 with dissolve
                b "Oh wow"
                b "Sesuatu yang lebih genit"
                s "Yang terakhir gratis"
                s "Anda akan membayar permintaan berikutnya"
                scene jopen6 with dissolve
                b "Saya akan membayar apapun untuk keledai ini"
                s "Yes"
                b "Tetapi jika saya membayar saya akan melakukan apa yang saya inginkan"
                s "1000 $"
                b "Wow Ok"
                if mny >= 1000:
                    b "Saya ingin shower emas"
                    s "Ya apapun itu"
                    $ mny -= 1000
                    scene bds
                    s "Ahh"
                    "..."
                    s "Ahhh"
                    "..."
                    s "Ohhh"
                    "..."
                    scene jopen7 with fade
                    s "Ah"
                    scene jopen8 with dissolve
                    s "Hai!"
                    scene jopen9 with dissolve
                    s "Fuck"
                    b "Hahaha"
                    pass
                else:
                    b "Ok saya akan membayar Anda nanti"
                    $ srel -= 5
                    scene bds
                    s "Ahh"
                    "..."
                    s "Ahhh"
                    "..."
                    s "Ohhh"
                    "..."
                    scene jopen7 with fade
                    s "Ah"
                    pass

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
        call screen gnav



    if melsw == 3:
        $ melsw = 4
        $ Hour += 1
        scene hevening with fade
        "..."
        scene nhevening with dissolve
        m "Hi [bname]"
        b "Hi"
        scene nhevening5 with fade
        b "Jadi..."
        b "Apa kabar hari ini?"
        m "Seperti biasa, sial"
        b "Aku punya sesuatu untukmu"
        scene nhevening5nurse with dissolve
        m "Terima kasih, saya akan membukanya nanti"
        m "Saya lelah sekarang"
        b "Mungkin saya bisa memberi Anda pijatan"
        m "Tidak sekarang, terima kasih"
        b "Hmm Ok"
        scene nheveningmel with fade
        b "Mari kita lihat apa yang ada di"
        s "Apa yang Anda tonton [bname]?"
        scene nheveningmel1 with dissolve
        b "Jangan tahu, saya baru saja menyalakannya"
        m "[bname]"
        scene nheveningmel2 with dissolve
        b "Yes"
        m "Tolong datang sejenak"
        scene nheveningmel3 with dissolve
        m "Kunci pintu"
        scene door with dissolve
        b "Done"
        if dollnightw ==1:
            scene nheveningmel4 with dissolve
            m "Jadi Anda ingin saya memakai ini?"
            b "Err, tidak harus"
            b "Itu hanya hadiah"
            if mfuckedsober >=1:
                m "Duduk di tempat tidur"
                scene nheveningmel5 with dissolve
                b "..."
                scene nheveningmel6 with dissolve
                "..."
                scene nheveningmel7 with dissolve
                m "Stand Up Tunjukkan padaku"
                scene nheveningmel8 with dissolve
                if mmirror ==2:
                    m "Dapatkan cermin"
                    scene nheveningmel9 with fade
                    b "..."
                    m "Apa yang kamu tunggu?"
                    b "Mhhm"
                    scene nhmf
                    "..."
                    m "Ahh"
                    b "Stop screaming"
                    "..."
                    scene nheveningmel10 with dissolve
                    b "Ahhh"
                    scene nheveningmel11 with fade
                    b "{i} (nyeri punggung sialan, dia menguras saya) {/i}"
                    m "{i} (oh saya lupa tentang [sname]) {/i}"
                    m "Pergi [bname] sampai jumpa nanti"
                    scene nheveningmel21 with fade
                    m "Jadi apakah kamu akan memberitahuku"
                    b "Yes"
                    b "Saya mendapat uang dari Melinda"
                    m "Tapi kenapa?"
                    b "Dia bilang dia membutuhkan bantuanku dengan sesuatu"
                    m "Membantu dengan apa?"
                    b "Untuk meyakinkan Anda bekerja shift malam"
                    scene nheveningmel22 with dissolve
                    m "Benar-benar?"
                    b "Yes"
                    m "Dan apa yang kamu katakan padanya?"
                    scene nheveningmel21 with dissolve
                    b "Saya bilang saya tidak bisa berpikir saya bisa"
                    b "Tapi saya akan mencoba"
                    b "Tentu saja saya tidak akan melakukan itu"
                    m "Bagus, terus menjanjikannya sampai saya mencari sesuatu"
                    b "Bisakah saya mengambil uang darinya?"
                    m "Hehehe tentu saja"
                    m "Go now"
                    m "Dan terima kasih telah memberitahuku"
                    scene hall_n with fade
                    "..."
                    call screen gnav
                else:
                    m "Hmm ok Anda mungkin pergi sekarang"
                    m "Wait"
                    scene nheveningmel21a with fade
                    m "Bagaimana Anda membeli barang ini?"
                    b "Hal mana?"
                    m "The gift"
                    b "Ah"
                    b "Saya mendapat uang dari Melinda"
                    m "Mengapa?"
                    b "Dia bilang dia membutuhkan bantuanku dengan sesuatu"
                    m "Membantu dengan apa?"
                    b "Untuk meyakinkan Anda bekerja shift malam"
                    scene nheveningmel22a with dissolve
                    m "Benar-benar?"
                    b "Yes"
                    m "Dan apa yang kamu katakan padanya?"
                    scene nheveningmel21a with dissolve
                    b "Saya bilang saya tidak bisa berpikir saya bisa"
                    b "Tapi saya akan mencoba"
                    b "Tentu saja saya tidak akan melakukan itu"
                    m "Bagus, terus menjanjikannya sampai saya mencari sesuatu"
                    b "Bisakah saya mengambil uang darinya?"
                    m "Hehehe tentu saja"
                    m "Go now"
                    m "Dan terima kasih telah memberitahuku"
                    scene hall_n with fade
                    "..."
                    call screen gnav
            else:

                m "OK terima kasih"
                m "Anda bisa pergi sekarang"
                m "Wait"
                scene nheveningmel21a with fade
                m "Bagaimana Anda membeli barang ini?"
                b "Hal mana?"
                m "The gift"
                b "Ah"
                b "Saya mendapat uang dari Melinda"
                m "Mengapa?"
                b "Dia bilang dia membutuhkan bantuanku dengan sesuatu"
                m "Membantu dengan apa?"
                b "Untuk meyakinkan Anda bekerja shift malam"
                scene nheveningmel22a with dissolve
                m "Benar-benar?"
                b "Yes"
                m "Dan apa yang kamu katakan padanya?"
                scene nheveningmel21a with dissolve
                b "Saya bilang saya tidak bisa berpikir saya bisa"
                b "Tapi saya akan mencoba"
                b "Tentu saja saya tidak akan melakukan itu"
                m "Bagus, terus menjanjikannya sampai saya mencari sesuatu"
                b "Bisakah saya mengambil uang darinya?"
                m "Hehehe tentu saja"
                m "Go now"
                m "Dan terima kasih telah memberitahuku"
                scene hall_n with fade
                "..."
                call screen gnav

        elif valshoes == 1:
            scene nheveningmel12 with fade
            m "Ini mahal [bname]"
            b "Apa yang mahal?"
            m "Ini?"
            scene nheveningmel13 with dissolve
            b "Ah, tidak!"
            if mfuckedsober >=1:
                m "Duduk sekarang dan beri tahu saya bagaimana Anda membelinya?"
                scene nheveningmel14 with dissolve
                b "Hmm"
                scene nheveningmel15 with vpunch
                m "Anda akan mengatakan atau tidak?"
                b "No"
                scene nheveningmel16 with dissolve
                m "Lepaskan bajunya"
                scene nheveningmel17 with hpunch
                b "Ahh"
                m "Anda ingin bermain eh"
                scene nheveningmel18 with dissolve
                m "Aku akan menunjukkan padamu"
                scene nhcu
                b "Ahh"
                "..."
                m "Mmmm"
                "..."
                scene nheveningmel19 with dissolve
                m "Apakah Anda akan memberi tahu saya!"
                scene nhaa
                m "Oh"
                "..."
                b "..."
                m "Ahhh"
                scene nheveningmel20 with dissolve
                m "Ah"
                scene nheveningmel21 with fade
                m "Jadi apakah kamu akan memberitahuku"
                b "Yes"
                b "Saya mendapat uang dari Melinda"
                m "Tapi kenapa?"
                b "Dia bilang dia membutuhkan bantuanku dengan sesuatu"
                m "Membantu dengan apa?"
                b "Untuk meyakinkan Anda bekerja shift malam"
                scene nheveningmel22 with dissolve
                m "Benar-benar?"
                b "Yes"
                m "Dan apa yang kamu katakan padanya?"
                scene nheveningmel21 with dissolve
                b "Saya bilang saya tidak bisa berpikir saya bisa"
                b "Tapi saya akan mencoba"
                b "Tentu saja saya tidak akan melakukan itu"
                m "Bagus, terus menjanjikannya sampai saya mencari sesuatu"
                b "Bisakah saya mengambil uang darinya?"
                m "Hehehe tentu saja"
                m "Go now"
                m "Dan terima kasih telah memberitahuku"
                scene hall_n with fade
                "..."
                call screen gnav
            else:
                m "Anda bisa pergi sekarang"
                m "Wait"
                scene nheveningmel21 with fade
                m "Bagaimana Anda membeli barang ini?"
                b "Hal mana?"
                m "The gift"
                b "Ah"
                b "Saya mendapat uang dari Melinda"
                m "Mengapa?"
                b "Dia bilang dia membutuhkan bantuanku dengan sesuatu"
                m "Membantu dengan apa?"
                b "Untuk meyakinkan Anda bekerja shift malam"
                scene nheveningmel22 with dissolve
                m "Benar-benar?"
                b "Yes"
                m "Dan apa yang kamu katakan padanya?"
                scene nheveningmel21 with dissolve
                b "Saya bilang saya tidak bisa berpikir saya bisa"
                b "Tapi saya akan mencoba"
                b "Tentu saja saya tidak akan melakukan itu"
                m "Bagus, terus menjanjikannya sampai saya mencari sesuatu"
                b "Bisakah saya mengambil uang darinya?"
                m "Hehehe tentu saja"
                m "Go now"
                m "Dan terima kasih telah memberitahuku"
                scene hall_n with fade
                "..."
                call screen gnav

    elif melsw == 8:
        $ melsw = 9
        $ Hour += 1
        scene hevening with fade
        "..."
        scene nheveningmelsw with dissolve
        b "Hi"
        "..."
        b "Huh"
        b "Kamu tidak apa apa?!"
        scene nheveningmelsw1 with fade
        m "No"
        b "Mengapa?"
        m "Sesuatu yang buruk terjadi"
        b "Apa itu?"
        m "Later"
        scene nheveningmelsw2 with fade
        b "Katakan padaku apa yang terjadi?"
        m "..."
        scene nheveningmelsw3 with dissolve
        m "Mereka ingin saya bekerja shift malam"
        b "Jadi apa? Apakah Anda khawatir Anda kembali terlambat"
        m "Ini bukan shift malam yang tepat"
        b "Lalu apa?"
        scene nheveningmelsw4 with dissolve
        m "Anda tidak akan mengerti"
        b "Kenapa!"
        m "Itu shift hari tapi ..."
        b "Tapi apa?"
        m "Ini adalah jenis pekerjaan ..."
        m "Lebih dari pekerjaan pelayan"
        b "Lebih seperti apa?"
        b "Ayo katakan padaku aku bukan anak kecil"
        m "Nanti [bname] saya perlu mandi dan bersantai"
        scene nheveningmelsw5 with fade
        "..."
        scene room3 with fade
        b "{i} (mungkinkah itu melinda!) {/i}"
        b "{i} (Saya harus tahu lebih banyak) {/i}"
        scene nheveningmelsw6 with dissolve
        b "Hey"
        scene nheveningmelsw7 with dissolve
        b "Apakah itu akan melibatkan striptis?"
        scene nheveningmelsw8 with dissolve
        "..."
        scene nheveningmelsw7 with dissolve
        b "Apa?"
        b "Beri tahu saya"
        scene nheveningmelsw9 with dissolve
        m "Itu lebih dari sekadar striptis"
        m "Itu seperti ..."
        b "Seperti apa?"
        m "Klien dapat menghabiskan waktu dengan saya"
        b "Hmm"
        scene nheveningmelsw8 with dissolve
        m "Mari kita minum"
        b "Ok"
        m "Tunggu aku di luar, aku akan berubah dan kami pergi"
        scene nheveningmelsw10 with fade
        s "Keluar?"
        m "Hai [sname] Ya"
        s "Bisakah aku ikut denganmu?"
        m "No"
        s "Hmmph"
        $ snupset += 1
        m "Kami memiliki sesuatu untuk dilakukan"
        s "Apakah Anda akan terlambat?"
        m "Beberapa jam"
        s "Baiklah, dapatkah saya mengundang Rowena untuk datang?"
        m "Ya tidak masalah"
        scene nheveningmelsw11 with fade
        m "Saya pikir itu yang terbaik jika kita pergi melihat Elaine"
        m "Setidaknya saya bisa menanyakan pendapatnya"
        b "Ya ide bagus"
        scene nheveningmelsw12 with dissolve
        m "Ah Ok"
        m "Kami akan menunggumu"
        m "Ya ya mengerti, di bawah tikar pintu"
        scene nheveningmelsw13 with fade
        b "Bagaimana seseorang bisa menyimpan kunci di bawah matras"
        scene nheveningmelsw14 with fade
        m "Saya akan mendapatkan beberapa minuman sementara kami menunggunya"
        scene black
        "SEMENTARA ITU"
        scene nheveningmelsw15 with fade
        a "Yeah"
        scene black
        "..."
        scene nheveningmelsw16 with fade
        b "Jenis minuman apa ini?"
        m "Saya tidak tahu bahwa semua yang saya temukan"
        m "Itu kuat saya tahu"
        b "Jadi apa yang akan kamu lakukan?"
        m "Aku tidak tahu"
        m "Saya pikir saya akan mengundurkan diri"
        b "No"
        b "Saya kira lebih baik bermain pintar"
        m "Apa maksudmu?"
        b "Maksud saya bersabar, jangan kehilangan pekerjaan Anda"
        m "Saya tidak tahu sayang"
        m "Mari kita lihat apa yang dikatakan Elaine"
        b "Dimana dia"
        m "Dia mengatakan satu setengah jam dia akan berada di sini"
        b "Alright"
        m "Saya akan mendapatkan minuman lagi, apakah Anda ingin lebih?"
        b "Ya kenapa tidak"
        scene nheveningmelsw17 with dissolve
        "..."
        scene black
        "..."
        scene nheveningmelsw18 with fade
        s "Oh wow"
        "Biarkan \ 'bergabung dengan mereka"
        s "Huh"
        scene black
        "..."
        scene nheveningmelsw19 with fade
        m "Jika saya tinggal di tempat kerja, apakah itu akan membuat saya buruk?"
        b "No"
        scene nheveningmelsw20 with dissolve
        m "Aku benar -benar buruk?"
        b "Tidak, Anda tidak"
        menu:
            "Cium dia":
                scene nheveningmelsw21 with dissolve
                "..."
                scene nheveningmelsw22 with dissolve
                "..."
                pass
            "Jangan":
                m "Terima kasih"
                pass

        scene black with fade
        "SEMENTARA ITU"
        scene nheveningmelsw23 with fade
        "Mari kita bergabung dengan mereka"
        s "No"
        scene nheveningmelsw24 with dissolve
        "Hei Larry"
        rb "Apa?"
        "Kemarilah"
        scene sdp with dissolve
        s "Ahh"
        rb "Yes"
        "..."
        s "Ahhh"
        "..."
        scene nheveningmelsw25 with dissolve
        a "Mari kita pergi ke kamar guys"
        scene black
        "Di sisi lain"
        scene mlove
        $ persistent.unlock_46 = True
        m "Apakah saya buruk [bname]"
        b "Tidak, Anda tidak"
        m "Ah"
        play sound "sounds/mbreath.wav"
        "..."
        m "..."
        stop sound
        scene rdpp with fade
        a "Ahh"
        "..."
        a "Yes"
        "..."
        scene black
        "..."
        scene manall
        m "Katakan padaku aku buruk [bname]"
        b "Ah"
        m "Ahh"
        "..."
        play sound "sounds/mscream.wav"
        m "Ahhh"
        stop sound
        scene nheveningmelsw26 with dissolve
        e "..."
        m "Huh"
        scene nheveningmelsw27 with hpunch
        e "Santai, pakai sesuatu"
        scene black
        "..."
        scene nheveningmelsw28 with fade
        "..."
        scene black
        "Kembali ke [mname] dan Elaine"
        scene nheveningmelsw29 with fade
        e "Selalu membuat alasan"
        m "Apakah menurut Anda itu akan berhasil"
        e "Ya, mungkin menaikkan harga Anda, saat Anda secara pribadi dengan pria itu"
        m "Bagaimana jika dia menerima untuk membayarnya"
        e "Kemudian Anda memenangkan heheh"
        e "Just kidding"
        e "Katakanlah hari itu dalam sebulan itu"
        e "Maaf teman -teman saya punya menstruasi"
        m "Ya, dia akan meminta saya untuk blowjob"
        m "[bname] Tolong tinggalkan kami sendiri"
        e "Ayo biarkan dia tetap baik -baik saja"
        e "Anda tidak harus berpura -pura di depan saya, saya melihat segalanya"
        m "Jadi apa yang harus dilakukan sekarang?"
        e "Saya tidak tahu, jika Anda mampu meninggalkan pekerjaan itu, lakukanlah"
        e "Jika tidak, satu -satunya jalan keluar adalah membuat alasan, dan ini akan memberi Anda waktu untuk mencari tahu"
        m "All right"
        m "Saya kira sudah saatnya kita pergi"
        jump newdays






    elif e_showsupagain ==1:
        $ e_showsupagain = 2
        play sound "sounds/doorbell.wav"
        m "Hmm siapa itu saat ini?"
        stop sound
        scene nhevening6 with fade
        m "Oh hai elaine"
        e "Hi [mname]"
        e "Bagaimana cara kerja?"
        m "Tolong duduklah, saya akan berubah dan segera kembali"
        e "Sebenarnya saya perlu menggunakan toilet"
        m "Oke, Anda tahu di mana itu"
        e "Thanks"
        scene hevening7 with dissolve
        e "Ikuti saya, cepat"
        b "Hah!"
        scene hall_m_n31 with fade
        e "So"
        b "Jadi?"
        scene hall_m_n33 with dissolve
        e "Saya sangat membutuhkan kamar Anda dalam beberapa hari mendatang"
        b "Hmm..."
        b "Biarkan saya memikirkannya"
        e "Apa yang harus dipikirkan?"
        b "Errr"
        b "Saya butuh lebih banyak uang untuk risiko yang saya ambil"
        b "Itu tidak sepadan"
        scene hall_m_n35 with dissolve
        e "{i} (Saya tahu apa yang diperlukan untuk membuatnya berubah pikiran) {/i}"
        scene hall_m_n36 with dissolve
        e "Bukankah ini layak mengambil risiko?"
        menu:
            "Ya itu":
                b "Sial ya!"
                $ cselaine0 = 9
                b "Aku akan segera meneleponmu"
                scene hall_m_n32 with dissolve
                e "Terima kasih"
                scene hall_n with fade
                "..."
                call screen gnav
            "Aku tidak tahu":

                e "Apa maksudmu kamu tidak tahu?"
                b "Saya membutuhkan lebih banyak"
                e "Lebih seperti dalam apa?"
                scene hall_m_n44 with dissolve
                b "Lebih dari kalian"
                scene hall_m_n45 with dissolve
                e "[bname]! Apa yang kamu bicarakan"
                b "Ya Anda mendengar saya, saya ingin lebih dari tubuh ini"
                if persistent.patch_enabled:
                    e "Anda adalah putra sahabat saya"
                    pass
                else:
                    e "It's impossible"
                    pass
                b "Dan tidak mungkin lagi menyewa kamar saya"
                scene hall_m_n46 with dissolve
                e "Oke, tapi saya memutuskan apa yang diizinkan dan apa yang tidak"
                b "Yes"
                e "Kapan Anda ingin melakukannya?"
                e "Kita tidak bisa sekarang"
                b "Saya akan menelepon Anda saat waktunya"
                e "Ok"
                $ elainefuck = 1
                scene hall_n with fade
                "..."
                call screen gnav

    if mbunknown == 1 and day ==1:
        scene nheveningb with fade
        b "{i} (...) {/i}"
        m "Hi [bname]"
        m "Rekan kerjaku Adam bergabung dengan kami untuk makan malam malam ini"
        mb "Hi [bname]"
        scene nheveningb1 with dissolve
        m "Adam, tolong duduk"
        m "Saya akan mulai menyiapkan makan malam"
        scene hall_nb with fade
        "..."
        call screen gnav

    elif mbvisit >= 1 and day ==3:
        scene nheveningb with fade
        b "{i} (...) {/i}"
        m "Hi [bname]"
        mb "Hi [bname]"
        b "Hi"
        scene nheveningb1 with dissolve
        m "Adam, tolong duduk"
        m "Saya akan mulai menyiapkan makan malam"
        scene hall_nb with fade
        "..."
        call screen gnav
    else:

        pass
    scene hevening with fade
    "..."
    scene nhevening with dissolve
    m "Hi [bname]"
    if elaineshowsup ==1 and day ==6:
        $ elaineshowsup = 2
        scene nheveninge with dissolve
        e "[mname] Anda kembali"
        e "Katakan padaku, ada berita?"
        e "Bisakah saya kembali sekarang?"
        m "Ya saya berbicara dengan Rob"
        m "Semua baik sekarang"
        e "Terima kasih banyak"
        e "Aku berhutang padamu yang satu itu"
        m "Selamat malam Elaine"
        e "Selamat malam"
        pass

    elif elaineagain == 2 and day ==6:
        $ elaineagain = 3
        scene nheveninge with dissolve
        e "[mname] Anda kembali"
        e "Katakan padaku, ada berita?"
        e "Bisakah saya kembali sekarang?"
        m "Ya saya berbicara dengan Rob"
        m "Semua baik sekarang"
        e "Terima kasih banyak"
        e "Aku berhutang padamu yang satu itu"
        m "Selamat malam Elaine"
        e "Selamat malam"
        pass
    else:


        pass

    scene nhevening5 with fade
    b "Jadi..."
    b "Apa kabar hari ini"
    if day ==5:
        m "Hell of a Day"
        if sbm ==0 and sscall == 1:
            $ sbm = 1
            b "Ada sesuatu yang harus Anda ketahui"
            m "Apa itu?"
            b "[sname] sedang berbicara dengan Stewart"
            m "Dan?"
            b "Dia meminta uang kepadanya dan memberi tahu dia tentang situasi kami"
            scene nhevening7 with dissolve
            m "Apa!!"
            b "Yeah"
            scene nhevening8 with hpunch
            "..."
            scene pdinner_m5 with fade
            "..."
            m "Apakah kamu mengerti !!!"
            "..."
            m "APAKAH KAMU!"
            s "Ya, saya minta maaf"
            s "I'm sorry"
            m "Lain kali saya akan mengambil telepon ini dan menghancurkannya!"
            b "Hmm"
            b "Saatnya pergi"
            scene door with fade
            b "{i} (...) {/i}"
            call screen gnav
        else:
            pass
        "..."
        menu:
            "Apakah Anda ingin saya memberikan pijatan?":
                if mrel >=90:
                    jump mquickmassage
                else:
                    m "No thanks"
                    pass

            "Beri dia pakaian perawat" if mnurseoutfit ==2:
                b "Aku punya sesuatu untukmu"
                $ mnurseoutfit = 3
                scene nhevening5nurse with dissolve
                m "Terima kasih, saya akan membukanya nanti"
                m "Saya lelah sekarang"
                pass
            "Apakah Anda ingin pergi ke bioskop?":

                if mrel >=250:
                    m "Ya kenapa tidak"
                    m "Biarkan saya sedikit rileks dan kemudian kita pergi"
                    m "Pergi dan beri tahu [sname]"
                    m "Let \'s Go Congs"
                    b "Mhmm"
                    b "Ok"
                    scene cinenad with fade
                    s "Ya?"
                    b "Hmm apa yang salah"
                    s "Tidak ada, apa yang kamu inginkan?"
                    b "Saya datang untuk memeriksa apakah Anda ingin pergi bersama kami ke bioskop"
                    menu:
                        "Bawa dia bersamamu":
                            b "Jadi apa yang kamu katakan?"
                            s "Ya ayo pergi"
                            scene cinejengoing with fade
                            m "Let's go"
                            b "Ok"
                            jump cinenadjen
                        "Kirim dia ke Rowena":


                            b "Atau Anda lebih suka pergi dan keluar malam dengan Rowena"
                            s "Saya tidak ingin pergi ke Rowena"
                            s "Untuk apa?"
                            b "Habiskan saja malam, pergi keluar, bersenang -senang"
                            s "Huh"
                            menu:
                                "Berikan uang padanya" if mny >=50:
                                    b "Di sini ambil ini, nikmati malam"
                                    scene cinenad1 with dissolve
                                    s "Terima kasih!!"
                                    pass
                                "Melanjutkan":

                                    s "Lebih baik aku pergi bersamamu"
                                    scene cinejengoing with fade
                                    m "Let's go"
                                    b "Ok"
                                    jump cinenadjen

                    scene black
                    "..."
                    scene cinejengoing with fade
                    m "Dimana [mname]"
                    b "Dia bilang dia lebih suka pergi menemui Rowena"
                    m "All right"
                    m "Let's go"
                    b "Ok"
                    jump cinejen
                else:
                    m "Tidak, saya lelah sekarang"
                    b "Ok"
                    "Naikkan poin Anda menjadi 250"
                    pass
            "Melanjutkan":


                pass




    elif day ==6:
        m "Hell of a Day"
        if sbm ==0 and sscall == 1:
            $ sbm = 1
            b "Ada sesuatu yang harus Anda ketahui"
            m "Apa itu?"
            b "[sname] sedang berbicara dengan Stewart"
            m "Dan?"
            b "Dia meminta uang kepadanya dan memberi tahu dia tentang situasi kami"
            scene nhevening7 with dissolve
            m "Apa!!"
            b "Yeah"
            scene nhevening8 with hpunch
            "..."
            scene pdinner_m5 with fade
            "..."
            m "Apakah kamu mengerti !!!"
            "..."
            m "APAKAH KAMU!"
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

        "..."
        menu:
            "Apakah Anda ingin saya memberikan pijatan?":
                if mrel >=90:
                    jump mquickmassage
                else:
                    m "No thanks"
                    pass

            "Beri dia pakaian perawat" if mnurseoutfit ==2:
                b "Aku punya sesuatu untukmu"
                $ mnurseoutfit = 3
                scene nhevening5nurse with dissolve
                m "Terima kasih, saya akan membukanya nanti"
                m "Saya lelah sekarang"
                pass
            "Melanjutkan":

                pass
    else:



        m "Melelahkan seperti biasa"
        m "Saya akan mulai menyiapkan makan malam"
        b "Ok"
        if sbm ==0 and sscall == 1:
            $ sbm = 1
            b "Ada sesuatu yang harus Anda ketahui"
            m "Apa itu?"
            b "[sname] sedang berbicara dengan Stewart"
            m "Dan?"
            b "Dia meminta uang kepadanya dan memberi tahu dia tentang situasi kami"
            scene nhevening7 with dissolve
            m "Apa!!"
            b "Yeah"
            scene nhevening8 with hpunch
            "..."
            scene pdinner_m5 with fade
            "..."
            m "Apakah kamu mengerti !!!"
            "..."
            m "APAKAH KAMU!"
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
            menu:
                "Beri dia pakaian perawat" if mnurseoutfit ==2:
                    b "Aku punya sesuatu untukmu"
                    $ mnurseoutfit = 3
                    scene nhevening5nurse with dissolve
                    m "Terima kasih, saya akan membukanya nanti"
                    m "Saya lelah sekarang"
                    pass
                "Apakah Anda ingin saya memberikan pijatan?":

                    if mrel >=90:
                        jump mquickmassage
                    else:
                        m "No thanks"
                        pass

        pass
    scene hall_n with fade
    "..."
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
