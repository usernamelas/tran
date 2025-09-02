label cherylblunch:
    scene cbl1 with fade
    "..."
    c "Biarkan makan di tempat saya"
    scene cbl2 with fade
    b "Terima kasih untuk makan siangnya, itu bagus"
    c "Katakan padaku [bname]"
    scene cbl3 with dissolve
    c "Bagaimana [mname] mengelola"
    c "Jenis pekerjaan apa yang dia lakukan untuk membeli hidup ini"
    b "Berbuat salah.."
    b "Pekerjaan normal"
    c "Hmm"
    c "Apakah cukup untuk membayar sewa, makanan, dan pengeluaran Anda"
    b "Yes"
    scene cbl4 with dissolve
    c "Ok saya akan berubah, tunggu saya"
    b "Mengubah?"
    scene cbl5 with fade
    c "Apakah Anda ingin ikut dengan saya ke pantai"
    scene cbl6 with dissolve
    b "Huh"
    scene cbl5 with dissolve
    b "{i} ([mname] akan membunuhku untuk ini) {/i}"
    menu:
        "Saya tidak bisa hari ini":
            b "Tidak, saya lebih suka, jujur"
            b "Tidak ada waktu"
            c "Baiklah, ambil ini"
            b "Apa itu?"
            c "Ambil saja"
            $ mny += 100
            $ renpy.notify (_("She gave you 100 $"))
            $ renpy.pause ( 5, 0)
            b "Oh thanks"
            b "Sampai jumpa, sampai jumpa"
            c "Bye darling"
            "..."
            jump broom_menu
        "Lepaskan":

            scene chbeach with fade
            b "{i} (ISN \ T That The Nude Beach?) {/i}"
            c "Baiklah, mari kita mendapatkan tan"
            scene chbeach1 with fade
            b "{i} (ohh my ...) {/i}"
            scene chbeach2 with dissolve
            b "{i}(God){/i}"
            c "Saya pikir saya akan berenang"
            scene chbeach3 with dissolve
            c "Ingin datang?"
            b "{i}(Of course){/i}"
            b "Yes"
            scene chbeach4 with fade
            "..."
            scene chbeach5 with fade
            c "Katakan padaku [bname]"
            c "Apa yang [mname] bekerja?"
            scene chbeach6 with dissolve
            b "..."
            menu:
                "Katakan padanya":
                    b "Baik itu ..."
                    scene chbeach5 with dissolve
                    b "Klub Malam"
                    c "Hmm"
                    c "Klub malam macam apa?"
                    b "Saya tidak tahu, tidak pernah mengunjunginya"
                    c "Jadi begitu"
                    scene chbeach5 with fade
                    "Anda menghabiskan waktu di pantai"
                    "Dan kemudian pulang"
                    jump broom_menu
                "Jangan":

                    $ chbopen = 1
                    b "Saya benar -benar tidak tahu"
                    c "Ok saya lihat"
                    scene chbeach5 with dissolve
                    c "Bukankah ini pantai telanjang?"
                    b "Err saya pikir begitu"
                    scene chbeach7 with dissolve
                    c "Keren, aku akan mendapatkan cokelat penuh"
                    scene chbeach8 with dissolve
                    c "Apakah Anda tidak akan menanggalkan pakaian?"
                    b "Yes"
                    scene chbeach9 with dissolve
                    c "Hmm"
                    scene chbeach10 with dissolve
                    c "Uhum [bname]"
                    c "Bisakah Anda membantu saya dengan minyak penyamakan?"
                    b "Yes"
                    scene chbeach12 with fade
                    "..."
                    scene chbeach11 with fade
                    c "Jadi apakah Anda tahu tempat dia bekerja?"
                    c "Maksud saya, apakah Anda mengunjunginya?"
                    b "Err no"
                    c "{i} (sepertinya dia tidak akan bicara) {/i}"
                    c "{i} (ini akan membutuhkan lebih dari pakaian) {/i}"
                    scene chbeach14 with dissolve
                    c "Bisakah Anda memberi kami minuman?"
                    b "..."
                    c "[bname]! Tolong minuman"
                    b "Ah pasti ya"
                    scene chbeach15 with fade
                    c "[bname] Bisakah Anda menaruh lebih banyak minyak di punggung saya, saya tidak ingin dibakar"
                    b "Yes"
                    scene chbeach16 with dissolve
                    c "Lalu lakukan"
                    scene chbeach17 with dissolve
                    "..."
                    c "Cukup biarkan aku menaruh untukmu"
                    c "Berbaring telentang"
                    scene chbeach18 with dissolve
                    $ persistent.unlock_31 = True
                    c "Aku akan meletakkan di dadamu"
                    b "Ugh"
                    scene chbeach19 with hpunch
                    b "{i}(Shit){/i}"
                    c "Lihat ada orang yang datang"
                    c "Saya pikir itu cukup untuk hari ini"
                    c "Apakah Anda ingin pergi ke suatu tempat?"
                    b "Di suatu tempat seperti ..."
                    b "Di mana?"
                    c "Untuk minum"
                    menu:
                        "Menerima":
                            scene cbl5 with fade
                            c "Mandi sebentar"
                            c "Saya akan melakukannya setelah Anda selesai"
                            scene cbl7 with fade
                            c "Ini kamar mandi"
                            scene cbl8 with dissolve
                            c "Anda bisa mulai"
                            scene cbl9 with dissolve
                            b "{i} (dia mendapat tempat yang bagus) {/i}"
                            b "{i} (Saya ingin tahu apa karyanya) {/i}"
                            scene cbl10 with dissolve
                            b "Hah!"
                            c "Aku punya handukmu"
                            scene cbl11 with dissolve
                            b "..."
                            scene cbl10 with dissolve
                            "..."
                            scene cbl12 with dissolve
                            c "Here"
                            b "Terima kasih"
                            c "Katakan padaku ketika kamu selesai jadi aku datang"
                            scene cbl9 with fade
                            b "{i} (dia sampai sesuatu) {/i}"
                            b "{i} (Saya harap, hehehe) {/i}"
                            scene cbl13 with fade
                            c "Selesai?"
                            b "Yes almost"
                            c "OK, keringkan dan tunggu saya di ruang utama"
                            scene cbl14 with fade
                            c "I'm done"
                            c "Mari kita minum di sini, lebih nyaman"
                            b "Ok"
                            scene cbl15 with dissolve
                            c "Katakan padaku [bname]"
                            c "Saya sangat ingin membantu Anda"
                            c "Apa itu pekerjaan [mname]"
                            menu:
                                "Katakan padanya":
                                    b "Dengan baik..."
                                    b "Dia bekerja di klub strip"
                                    scene cbl16 with dissolve
                                    c "Hmm"
                                    c "Ok"
                                    scene cbl15 with dissolve
                                    c "Cheers"
                                    b "Cheers"
                                    "..."
                                    c "Saya pikir sudah terlambat sekarang, kami tidak ingin [mname] mengkhawatirkan Anda"
                                    scene cbl17 with fade
                                    c "Selamat malam"
                                    $ Hour = 21
                                    $ btoldcheryl = 1
                                    b "{i} (apa -apaan) {/i}"
                                    jump broom_menu
                                "Jangan":

                                    b "Dengan baik..."
                                    b "Aku tidak tahu"
                                    c "Hmm"
                                    if bdtchr ==0:
                                        c "Hmm"
                                        scene cbl18 with dissolve
                                        $ bdtchr += 1
                                        c "Saya pikir sudah terlambat sekarang, kami tidak ingin [mname] mengkhawatirkan Anda"
                                        b "{i} (apa -apaan) {/i}"
                                        jump broom_menu

                                    elif bdtchr >=1:
                                        c "Hmm"
                                        scene cbl19 with dissolve
                                        c "Anda lucu saat berbohong"
                                        c "Bangun"
                                        scene cbl20 with fade
                                        c "Apakah Anda akan memberi tahu saya atau tidak?"
                                        scene cbl21 with dissolve
                                        $ persistent.unlock_38 = True
                                        c "Mau mu"
                                        menu:
                                            "Lakukan itu":
                                                scene cbl22 with dissolve
                                                c "Jadi Anda memutuskan untuk memberi tahu saya?"
                                                b "Yes"
                                                $ btoldcheryl = 1
                                                c "Dia bekerja di klub strip"
                                                scene cbl23 with dissolve
                                                c "Anak yang baik"
                                                b "..."
                                                menu:
                                                    "Fokus pada payudara":
                                                        scene cbl24 with dissolve
                                                        c "Ahhh"
                                                        scene cbl25 with dissolve
                                                        c "Ahhh"
                                                        scene cbl26 with dissolve
                                                        c "Sepertinya Anda menyukai payudara saya, tidak!"
                                                        b "Uhh ..."
                                                        scene cbl27 with dissolve
                                                        b "Yeah"
                                                        scene cbl17 with fade
                                                        c "Selamat malam"
                                                        $ Hour = 21
                                                        jump broom_menu
                                                    "Fokus pada keledai":

                                                        scene cbl28 with dissolve
                                                        c "Hmmm"
                                                        scene cbl29 with dissolve
                                                        c "Oh yeah"
                                                        scene cbl30 with dissolve
                                                        c "Ahh"
                                                        scene cbl31 with dissolve
                                                        "..."
                                                        scene cbl32 with dissolve
                                                        b "{i} (payudara sialan) {/i}"
                                                        scene cbl33 with fade
                                                        c "Anda bisa pergi sekarang, kami tidak ingin [mname] mengkhawatirkan Anda"
                                                        b "Selamat malam"
                                                        $ Hour = 21
                                                        jump broom_menu
                                            "Meninggalkan":


                                                b "Selamat malam"
                                                c "{i} (apa -apaan) {/i}"
                                                jump broom_menu
                        "Menolak":


                            b "Maaf saya tidak bisa hari ini"
                            c "Oh baik -baik saja"
                            $ Hour += 4
                            jump broom_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc