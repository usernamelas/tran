label melwork:
    if wrokmelindrp <=2:
        scene melwrk with fade
        ml "Gadis itu menunggumu di dalam ruangan itu"
        $ wrokmelindrp += 1
        scene melwrk4 with dissolve
        "..."
        scene melwrk5 with dissolve
        "..."
        scene melwrk6 with dissolve
        "..."
        scene melwrk7 with dissolve
        "..."
        scene melwrk8 with fade
        "Itu bagus"
        scene melwrk with fade
        ml "Ini uangmu"
        $ mny += 500
        b "Thanks"
        if wrokmelindrp ==2:
            scene melwrk9 with fade
            m "{i} (Saya ingin tahu kemana dia pergi sepanjang waktu) {/i}"
            play sound "sounds/door_openc.wav"
            m "{i} (aha itu dia) {/i}"
            m "[bname] Apakah itu Anda?"
            b "Yes"
            stop sound
            m "Kemarilah"
            scene melwrk10 with fade
            m "Kemana saja kamu selama ini?"
            b "Tidak ada, hanya berjalan -jalan"
            m "Mhhm"
            b "Bisakah saya pergi?"
            m "Yes"
            jump broom_menu
        else:

            jump broom_menu

    elif wrokmelindrp >2:
        $ wrokmelindrp += 1
        if wrokmelindrp >=5:
            if snameworkmelinda ==3:
                scene melwrk39 with fade
                "..."
                ml "Hai [sname], sangat senang melihatmu"
                ml "Mari kita duduk dan berbicara"
                scene melwrk40 with dissolve
                s "[bname] Memberitahu saya bahwa Anda ingin melihat saya"
                scene melwrk41 with dissolve
                ml "[bname] Bisakah Anda meninggalkan kami sendirian sejenak"
                b "Ok"
                scene melwrk42 with dissolve
                ml "Jadi, saya punya satu klien pribadi dan elit"
                s "..."
                ml "Siapa yang mencari perusahaan untuk perjalanan ibiza -nya"
                s "Ok dan?"
                ml "Dia akan membayar perjalanan Anda dan semua biaya"
                ml "Ditambah sejumlah besar uang"
                s "Berapa harganya?"
                s "Dan untuk berapa hari?"
                ml "Ini selama satu minggu, untuk berapa banyak"
                ml "Dia ingin melihat gadis itu dulu"
                ml "Jadi, jika Anda tidak keberatan saya mengambil beberapa foto Anda"
                ml "Jadi saya bisa menunjukkannya"
                s "Ya kenapa tidak"
                ml "Mari kita pergi ke ruang studio"
                scene melwrk43 with fade
                ml "Bisakah Anda melakukan pose"
                ml "Saya secara pribadi akan mengambil foto untuknya"
                s "Yes"
                scene melwrk44 with dissolve
                "..."
                scene melwrk45 with dissolve
                ml "Bagus, bisakah kita mengambil sesuatu yang lebih terbuka?"
                scene melwrk46 with dissolve
                $ persistent.unlock_75 = True
                s "Hmm"
                ml "Jangan khawatir, Anda bisa mempercayai saya"
                ml "Saya akan membayar Anda untuk foto yang terbuka"
                s "Ok"
                scene melwrk47 with dissolve
                "..."
                scene melwrk48 with dissolve
                ml "Bagus"
                ml "Sekarang lihat aku"
                scene melwrk49 with dissolve
                ml "We're done"
                ml "Mari kita kembali ke ruang tamu dan kita akan membahas detailnya"
                scene melwrk50 with fade
                b "Jadi?"
                s "Dia menawari saya bepergian"
                $ snameworkmelinda = 4
                b "Apa maksudmu bepergian?"
                s "Untuk bepergian dengannya ke Eropa"
                b "Dan apa yang kamu katakan?"
                s "Saya belum tahu, saya akan memikirkannya"
                pass
            else:
                pass
            scene melwrk29 with fade
            $ persistent.unlock_65 = True
            ml "Tidak ada gadis hari ini, tapi aku ingin melihatmu"
            ml "Follow me"
            scene melwrk28 with fade
            ml "Jadi, apakah Anda tahu ada orang yang ingin bekerja seperti Anda dan mendapatkan banyak uang?"
            ml "Seseorang yang cantik tentu saja"
            b "Eh tidak juga"
            b "Saya tidak punya banyak teman"
            if persistent.patch_enabled:
                ml "Bagaimana dengan adikmu?"
                pass
            else:
                ml "Bagaimana dengan teman sekamar Anda"
                pass
            b "Hah!"
            b "Bagaimana Anda tahu [sname]"
            ml "Saya tahu, jangan khawatir tentang itu sekarang"
            ml "Apakah Anda pikir dia tertarik"
            b "Tidak, saya tidak berpikir begitu"
            scene melwrk30 with dissolve
            ml "Periksa saja dengannya"
            ml "Saya yakin dia akan seperti banyak uang"
            b "..."
            b "Saya akan melihat apa yang bisa saya lakukan"
            ml "Mengapa Anda tidak meneleponnya sekarang?"
            b "Err"
            ml "Hubungi saja dan tanyakan"
            if snameworkmelinda ==0:
                $ snameworkmelinda = 1
                pass
            else:
                pass
            b "Hmm"
            menu:
                "Saya perlu menyiapkannya":
                    b "Aku tidak bisa memberitahunya ini"
                    ml "Hmm baik -baik saja, beri tahu saya saat Anda melakukannya"
                    ml "Semoga harimu menyenangkan"
                    ml "Bye"
                    pass
                "Oke":

                    scene melwrk32 with dissolve
                    "..."
                    scene melwrk33 with dissolve
                    s "{i} (apa yang dia inginkan sekarang) {/i}"
                    scene melwrk32 with dissolve
                    b "Dia tidak menjawab"
                    ml "Ok kami akan mencoba nanti"
                    ml "Ayo ikuti aku"
                    ml "Mari kita hadiahi hari ini"
                    scene melwrk31 with fade
                    "..."
                    scene bomel with dissolve
                    ml "Yes"
                    scene bomel1 with dissolve
                    b "..."
                    scene bomel2 with dissolve
                    b "Ahh"
                    scene bomel3 with dissolve
                    ml "Lakukan sayang"
                    scene bomel4 with dissolve
                    b "Ahh"
                    scene black
                    scene melwrk29 with fade
                    $ mny += 100
                    ml "Ini sesuatu untuk Anda"
                    ml "Jangan lupa untuk bertanya [sname]"
                    pass
        else:

            scene melwrk with fade
            ml "Gadis itu menunggumu di dalam ruangan itu"
            scene melwrk1 with dissolve
            "..."
            scene melwrk2 with dissolve
            "..."
            scene melwrk3 with dissolve
            "..."
            scene melwrk with fade
            ml "Ini uangmu"
            $ mny += 500
            b "Thanks"
            pass
        "..."
        if wrokmelindrp >=3:
            $ Hour += 1
            scene melwrk9 with fade
            m "{i} (Saya bertanya -tanya ke mana dia pergi sepanjang waktu) {/i}"
            m "{i} (mungkin itu benar apa yang dikatakan Elaine) {/i}"
            play sound "sounds/door_openc.wav"
            m "{i} (aha itu dia) {/i}"
            m "[bname] Apakah itu Anda?"
            b "Yes"
            m "Kemarilah"
            scene melwrk10 with fade
            m "Kemana saja kamu selama ini?"
            b "Tidak ada, hanya berjalan -jalan"
            m "Mhhm"
            b "Bisakah saya pergi?"
            m "Tunggu saya di kamar saya"
            scene melwrk11 with fade
            m "Katakan padaku kemana saja kamu"
            m "Dan jangan berbohong"
            b "Aku bersumpah, aku berjalan -jalan di kota"
            m "Apakah Anda mengunjungi Melinda?"
            b "Apa?"
            b "TIDAK!!"
            m "Keluar"
            b "..."
            scene hall_d with fade
            b "{i} (...) {/i}"
            b "{i} (dia tampak sangat marah) {/i}"
            b "{i} (mungkin saya harus kembali ke sana) {/i}"
            menu:
                "Tidak, tonton saja TV":
                    scene melwrk21 with dissolve
                    b "{i} (mari kita lihat apa yang ada) {/i}"
                    scene melwrk22 with dissolve
                    b "Hah!"
                    m "Saya akan bekerja, saya memiliki shift malam"
                    m "Beri tahu [sname] untuk menyiapkan makanan jika Anda ingin makan"
                    b "{i} (sialan, dia sangat marah) {/i}"
                    scene black
                    scene nheveningmel1 with fade
                    s "Kemana dia pergi?"
                    b "Dia memiliki shift malam"
                    s "Hmm"
                    b "Dan dia mengatakan bahwa Anda harus menyiapkan makan malam"
                    s "Lebih baik memesan sesuatu yang siap"
                    s "Apakah Anda punya uang?"
                    b "Ya saya akan melakukannya"
                    b "Dan mari kita menonton TV"
                    menu:
                        "Tidak, [sname] ingin pergi melihat Rowena" if sgoestost >= 2:
                            s "Saya akan pergi melihat Rowena"
                            b "Hmm"
                            b "Ok"
                            jump snamefuckst1
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
                            if snameworkmelinda ==1:
                                b "Tapi pertama -tama saya punya sesuatu untuk ditanyakan kepada Anda"
                                s "Apa itu?"
                                b "Apakah Anda ingin memiliki pekerjaan paruh waktu?"
                                s "No"
                                b "Anda tidak ingin tahu berapa banyak uang yang bisa Anda dapatkan?"
                                s "Apakah terlalu banyak?"
                                b "Sekitar 00 hingga 000 per kunjungan"
                                scene jopen1a with dissolve
                                s "Hmm"
                                scene jopen1 with dissolve
                                s "Biarkan saya menebak, pengawalan?"
                                b "Ya, tapi mereka berkualitas tinggi, pribadi"
                                b "Semacam klub pribadi"
                                s "Saya akan memikirkannya"
                                $ snameworkmelinda = 3
                                b "Oke, sekarang tunjukkan apa yang Anda dapatkan"
                                pass
                            else:
                                pass
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
                                if wrokmelindrp >=5:
                                    scene mhbg
                                    m "..."
                                    m "Ah"
                                    "..."
                                    m "Mmm"
                                    "..."
                                    scene mfbg
                                    "..."
                                    m "Ah perlahan -lahan tolong"
                                    "..."
                                    "..."
                                    scene black with fade
                                    "..."
                                    pass
                                else:

                                    "SEMENTARA ITU"
                                    scene melwrk23 with fade
                                    "..."
                                    scene melwrk24 with dissolve
                                    "Ah"
                                    m "..."
                                    scene melwrk25 with dissolve
                                    "Ya saya akan membawanya"
                                    "Bayar dan temui dia di kamar"
                                    "Itu aku dan temanku"
                                    scene melwrk26 with dissolve
                                    m "Huh"
                                    "Ya Anda membayar ganda, untuk keduanya"
                                    scene melwrk27 with fade
                                    m "Slowly guys"
                                    scene mwdf
                                    m "..."
                                    "..."
                                    m "..."
                                    "..."
                                    scene black
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
                                b "Saya Ingin Sesuatu Bang"
                                s "Ya apapun itu"
                                $ mny -= 1000
                                scene ths
                                s "Ahh"
                                "..."
                                s "Ahhh"
                                "..."
                                scene ths011 with dissolve
                                s "[bname] !!!"
                                "..."
                                s "STTOPPP!"
                                scene jopen7a with fade
                                s "Ah"
                                scene jopen9 with dissolve
                                s "Fuck"
                                b "Hahaha"
                                jump broom_menu
                            else:

                                b "Ok saya akan membayar Anda nanti"
                                $ srel -= 5
                                scene bds
                                s "Ahh"
                                "..."
                                s "Ahhh"
                                s "[bname]"
                                "..."
                                s "Ohhh"
                                "..."
                                scene jopen7 with fade
                                s "Ah"
                                jump broom_menu
                "Siapkan secangkir teh untuknya":

                    scene melwrk12 with fade
                    b "Saya membuat Anda secangkir teh"
                    scene melwrk13 with dissolve
                    m "..."
                    b "Dan pijatan juga"
                    m "Lalu mulai"
                    scene mwms0 with dissolve
                    m "..."
                    scene mwms0 with dissolve
                    "..."
                    scene mwms1 with dissolve
                    "..."
                    scene mwms2 with dissolve
                    m "Apakah ini pijatan atau apa?"
                    m "Stop it"
                    b "Tidak, Anda benar, saya harus berubah"
                    scene melwrk14 with dissolve
                    m "Ah"
                    scene melwrk15 with dissolve
                    m "Ya itu belaian"
                    m "Seperti perempuan"
                    menu:
                        "Ajari dia pelajaran":
                            scene mwfma
                            m "Ah"
                            m "Ahh"
                            m "..."
                            m "Stop"
                            menu:
                                "Jangan berhenti" if wrokmelindrp >=5:
                                    scene melwrk34 with hpunch
                                    m "Ahh"
                                    scene melwrk35 with dissolve
                                    b "..."
                                    scene melwrk37 with dissolve
                                    m "Break My Ass [bname]"
                                    scene melwrk38 with dissolve
                                    m "Ahh"
                                    scene melwrk36 with dissolve
                                    m "..."
                                    pass
                                "Berhenti":
                                    "..."
                                    scene melwrk16 with dissolve
                                    "..."
                                    pass
                            scene melwrk17 with dissolve
                            b "Nanti..."
                            jump broom_menu
                        "Lanjutkan romantis":

                            scene melwrk18 with dissolve
                            m "Hmm"
                            scene melwrk18a with dissolve
                            m "Apa yang Anda jilakan [bname]"
                            scene melwrk19 with dissolve
                            m "My turn"
                            scene mssd
                            play sound "sounds/SexSuck10.wav"
                            "..."
                            b "Ahh"
                            stop sound
                            play sound "sounds/SexSuck10.wav"
                            "..."
                            "..."
                            stop sound
                            "..."
                            scene melwrk20a with hpunch
                            m "..."
                            scene melwrk20 with fade
                            b "Later"
                            jump broom_menu
        else:
            jump broom_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc