label bgroundednight:
    scene black
    "..."
    $ smalonenight += 1
    scene jbpractice2 with fade
    b "{i} (Saya ingin tahu kemana [mname] pergi!) {/i}"
    scene jbpractice3r with dissolve
    b "Uh oh"
    b "Apa yang salah?"
    m "..."
    scene mbgn with dissolve
    m "Apakah Anda menghubungi Stewart?"
    b "Err no"
    scene mbgn1 with dissolve
    m "Jangan berbohong padaku"
    $ persistent.unlock_27 = True
    b "Hey"
    m "Pergi ke kamar Anda, Anda membumi selama 2 hari"
    b "Apa?"
    m "Dan janganlah Anda berani keluar darinya"
    m "Saya akan mengirim makanan Anda ke sana"
    scene black
    "..."
    scene jbpractice1 with fade
    m "Hentikan semua yang Anda lakukan dan tonton TV dengan saya"
    s "Ok"
    scene mbgn2 with fade
    s "..."
    scene mbgn3 with dissolve
    s "..."
    scene mbgn2 with dissolve
    s "Bisakah saya minum juga?"
    m "Ya, dapatkan apapun yang Anda inginkan"
    s "Thanks"
    scene mbgn4 with fade
    s "Aku akan kembali"
    m "Dimana ..."
    s "Saya ingin menunjukkan sesuatu kepada Anda ..."
    scene mbgn5 with fade
    m "Huh"
    s "Apa pendapat Anda tentang ini?"
    s "Bisakah saya memakainya di pantai pada hari Minggu?"
    m "Darimana kamu mendapatkannya?"
    s "Saya sudah membelinya"
    m "Dari mana uangnya?"
    s "[bname]"
    scene mbgn6 with dissolve
    "..."
    scene mbgn5 with dissolve
    m "Ya kamu bisa"
    m "Duduk, aku akan menunjukkan milikku"
    scene mbgn7 with fade
    s "Wow cantik"
    scene mbgn8 with dissolve
    s "Tapi itu bukan pakaian renang"
    m "Lalu apa itu?"
    s "Sepertinya pakaian dalam bagiku"
    m "Tidak, itu tidak"
    scene mbgn9 with dissolve
    s "Tunjukkan padaku dari belakang"
    if smalonenight ==1:
        m "Saya lelah sekarang [sname]"
        m "Aku akan tidur"
        scene mbgn10 with dissolve
        m "Selamat malam"
        s "Selamat malam"
        jump newdays

    elif smalonenight ==2:
        m "Mari kita selesaikan minuman ini dulu"
        scene mbgn11 with fade
        m "Saya pikir saya akan menunjukkan bikini lebih baik"
        s "Hmmm"
        scene mbgn12 with fade
        m "Bagaimana menurutmu?"
        s "Oh wow"
        scene mbgn13 with dissolve
        s "Bagus"
        s "Mengapa Anda tidak memakai ini ke pantai?"
        scene mbgn14 with dissolve
        m "Apakah Anda bercanda?"
        scene mbgn15 with dissolve
        s "Ya saya tahu [bname] kadang -kadang pervy"
        scene mbgn16 with dissolve
        m "[bname]?"
        m "{i} (dia tahu sesuatu ...) {/i}"
        m "Apa maksudmu?"
        scene mbgn14 with dissolve
        s "Saya mengatakannya, kadang -kadang dia bisa menjadi cabul"
        m "Hmm"
        m "Baiklah, saya pikir saya akan tidur sekarang"
        scene mbgn17 with dissolve
        m "Selamat malam"
        s "Selamat malam"
        jump newdays

    elif smalonenight ==3:
        m "Mari kita selesaikan minuman ini dulu"
        scene mbgn11 with fade
        m "Saya pikir saya akan menunjukkan bikini lebih baik"
        s "Hmmm"
        scene mbgn12 with fade
        m "Bagaimana menurutmu?"
        s "Oh wow"
        scene mbgn13 with dissolve
        s "Bagus"
        s "Mengapa Anda tidak memakai ini ke pantai?"
        scene mbgn14 with dissolve
        m "Apakah Anda bercanda?"
        scene mbgn15 with dissolve
        s "Ya saya tahu [bname] kadang -kadang pervy"
        scene mbgn16 with dissolve
        m "[bname]?"
        m "Apa maksudmu?"
        scene mbgn14 with dissolve
        s "Saya mengatakannya, kadang -kadang dia bisa menjadi cabul"
        m "Hmm"
        m "Baiklah, saya pikir saya akan tidur sekarang"
        scene mbgn17 with dissolve
        m "Selamat malam"
        s "Hmm"
        menu:
            "[sname] akan bertanya apakah dia bisa tidur di tempat tidur [mname]":
                scene mbgn18 with dissolve
                s "..."
                s "Bisakah aku tidur denganmu malam ini"
                m "Tidak malam ini sayang"
                m "Saya lelah"
                scene mbgn19 with dissolve
                s "Ok"
                s "Selamat malam"
                jump newdays
            "Tidak perlu":

                s "Selamat malam"
                jump newdays




    elif smalonenight >=4 and smalonenight <=6:
        m "Mari kita selesaikan minuman ini dulu"
        scene mbgn11 with fade
        m "Saya pikir saya akan menunjukkan bikini lebih baik"
        s "Hmmm"
        $ nadiaasksforstrongdrinks = 1
        scene mbgn12 with fade
        m "Bagaimana menurutmu?"
        s "Oh wow"
        scene mbgn13 with dissolve
        s "Bagus"
        s "Mengapa Anda tidak memakai ini ke pantai?"
        scene mbgn14 with dissolve
        m "Apakah Anda bercanda?"
        scene mbgn15 with dissolve
        s "Ya saya tahu [bname] kadang -kadang pervy"
        scene mbgn16 with dissolve
        m "[bname]?"
        m "Apa maksudmu?"
        scene mbgn14 with dissolve
        s "Saya mengatakannya, kadang -kadang dia bisa menjadi cabul"
        m "Hmm"
        if hallcamera ==0:
            scene black
            "SEMENTARA ITU"
            scene bporn with fade
            b "{i}(Hmm){/i}"
            b "{i} (Saya ingin tahu apa yang mereka lakukan) {/i}"
            b "{i} (Saya harus melihat apakah saya dapat memperbaiki kamera) {/i}"
            b "{i} (Saya akan memeriksa online besok) {/i}"
            scene mbgn14 with fade
            pass
        else:
            pass

        m "Baiklah, saya pikir saya akan tidur sekarang"
        scene mbgn17 with dissolve
        m "Selamat malam"
        s "Hmm"
        menu:
            "[sname] akan bertanya apakah dia bisa tidur di tempat tidur [mname]":
                scene mbgn18 with dissolve
                s "..."
                s "Bisakah aku tidur denganmu malam ini"
                m "Ok"
                m "Tapi aku mabuk"
                s "Aku akan membawamu ke kamarku"
                scene mbgn20 with fade
                m "Saya akan menyelesaikan gelas ini terlebih dahulu"
                m "Anda pergi tidur sekarang"
                scene chcm16 with fade
                "..."
                scene chcm17 with dissolve
                "..."
                scene chcm18 with dissolve
                "..."
                scene mbgn21 with dissolve
                "..."
                scene mbgn22 with dissolve
                "..."
                scene mbgn23 with dissolve
                m "Ahhh"
                scene mbgn24 with dissolve
                s "{i} (apakah dia bangun!) {/i}"
                s "{i} (Saya pikir sudah waktunya berhenti) {/i}"
                scene mbgn25 with fade
                m "[sname]?"
                s "Ya!"
                m "Saya perlu tidur di kamar saya"
                s "Ah Ok"
                scene black
                "..."
                jump newdays
            "Tidak perlu":

                s "Selamat malam"
                jump newdays

    elif smalonenight >=7:
        m "Mari kita selesaikan minuman ini dulu"
        scene mbgn11 with fade
        m "Saya pikir saya akan menunjukkan bikini lebih baik"
        s "Hmmm"
        $ nadiaasksforstrongdrinks = 1
        scene mbgn12 with fade
        m "Bagaimana menurutmu?"
        s "Oh wow"
        scene mbgn13 with dissolve
        s "Bagus"
        s "Mengapa Anda tidak memakai ini ke pantai?"
        scene mbgn14 with dissolve
        m "Apakah Anda bercanda?"
        scene mbgn15 with dissolve
        s "Ya saya tahu [bname] kadang -kadang pervy"
        scene mbgn16 with dissolve
        m "[bname]?"
        m "Apa maksudmu?"
        scene mbgn14 with dissolve
        s "Saya mengatakannya, kadang -kadang dia bisa menjadi cabul"
        m "Hmm"
        if snamedrink >= 4:
            s "Mari kita minum lagi"
            m "Hanya satu, saya perlu tidur lebih awal"
            $ snamedrinkminus += 1
            scene mbgn26 with dissolve
            s "Hmmm"
            scene mbgn27 with dissolve
            s "Di sini mulai, saya akan segera kembali"
            m "Kemana kamu pergi?"
            s "Ada sesuatu yang ingin saya tunjukkan"
            scene mbgn28 with dissolve
            s "..."
            scene mbgn29 with dissolve
            m "[sname] Apa yang kamu kenakan?"
            s "Bukankah itu lucu?"
            m "Ya tapi ..."
            s "Apa yang Anda khawatirkan [bname] tidak akan datang kan?"
            s "Anda telah mengatakan Anda membumi dia"
            m "..."
            scene mbgn30 with dissolve
            s "Cheers"
            scene mbgn31 with fade
            m "Ini sangat kuat"
            s "Tidak demikian, tapi itu membuat saya merasa hangat, mungkin saya harus menghapus celemek ini"
            "..."
            scene mbgn32 with fade
            m "Huh"
            scene mbgn33 with dissolve
            "..."
            scene mbgn34 with dissolve
            "..."
            scene mbgn35 with fade
            s "Ahhh"
            scene mbgn36 with dissolve
            m "Mari kita lakukan ini dengan benar"
            scene mbgn37 with fade
            "..."
            scene mbgn38 with dissolve
            s "Ahhh"
            s "Biarkan saya melakukannya untuk Anda"
            s "Aku akan kembali"
            if hallcamera ==2:
                scene bporn with fade
                b "{i}(Hmm){/i}"
                b "{i} (Let \ 'S Periksa Kamera) {/i}"
                scene mbgn38c with dissolve
                b "{i} (oh wow!) {/i}"
                pass
            else:

                pass
            scene mbgn39 with fade
            s "Saya tahu Anda merindukan ini"
            scene mbgn40 with dissolve
            m "Ahhh"
            if hallcamera ==2:
                scene mbgn40c with dissolve
                b "{i} (Tuhan!) {/i}"
                b "{i} (mungkin sudah waktunya saya bergabung?) {/i}"
                menu:
                    "Bergabunglah dengan mereka":
                        scene mbgn44 with fade
                        b "Hmm"
                        b "Baiklah dengan baik"
                        scene mbgn45 with hpunch
                        s "Hah!"
                        b "Apa yang terjadi di sini?"
                        s "Tidak ada, kami hanya berpesta"
                        s "Dan apa yang kamu lakukan di sini?"
                        b "Hmm"
                        scene mbgn46 with dissolve
                        b "Tidak ada, saya hanya merekam semua ini"
                        s "Apa?"
                        s "Tidak, kamu tidak"
                        b "Baik kita akan menunggu sampai [mname] bangun dan kita akan lihat"
                        s "Hmm"
                        menu:
                            "Meninggalkan":
                                scene mbgn47 with fade
                                s "Sial, aku tidak peduli, aku akan melanjutkan"
                                $ bs_sex = 1
                                pass
                            "Tunggu":

                                scene mbgn45 with dissolve
                                s "Apa yang kamu tunggu?"
                                b "Continue"
                                s "Saya tidak suka"
                                scene mbgn75 with dissolve
                                s "Apa yang sedang kamu lakukan?"
                                b "Anda dapat bergabung dengan saya jika Anda mau"
                                if scorr >=100 and srel >=300:
                                    "Dia memutuskan untuk bergabung dengan Anda"
                                    s "Tunggu biarkan melakukannya dengan benar"
                                    scene mbgn76 with dissolve
                                    m "Haha"
                                    scene mbgn77 with dissolve
                                    "..."
                                    scene mbgn78 with vpunch
                                    m "Ahh"
                                    scene mbgn79 with dissolve
                                    s "Yes"
                                    scene mbgn80 with dissolve
                                    s "Ahhh"
                                    b "Dia menginginkanmu"
                                    b "Ayo dia [sname]"
                                    scene mbgn81 with dissolve
                                    "..."
                                    scene mbgn82 with dissolve
                                    m "Uh"
                                    scene mbgn83 with dissolve
                                    $ persistent.unlock_32 = True
                                    "..."
                                    scene mbgn84 with fade
                                    "..."
                                    scene mbgn85 with hpunch
                                    b "Ugghh"
                                    scene mbgn86 with fade
                                    m "Selamat malam sayang"
                                    b "Ya Tuhan"
                                    scene black
                                    "..."
                                    jump newdays
                                else:



                                    s "Saya keluar dari sini"
                                    b "Better"
                                    "Meningkatkan [sname] korupsi menjadi 100 dan hubungan menjadi 300"
                                    scene mbgn48 with fade
                                    m "[bname]"
                                    m "Mengapa Anda tidak ada di kamar Anda?"
                                    b "Kamu tidak apa apa"
                                    m "Ya, dan Anda membumi"
                                    b "Biarkan saya membawa Anda ke kamar Anda"
                                    m "Dapatkan aku gelas sialan ini, itu luar biasa"
                                    scene mbgn49 with fade
                                    m "Dimana minuman saya?"
                                    b "Di sini bersamaku"
                                    b "Saya akan memberikannya kepada Anda jika Anda melakukan sesuatu untuk saya"
                                    m "Berikan dulu"
                                    b "Here"
                                    scene mbgn50 with dissolve
                                    m "Jadi apa yang kamu inginkan?"
                                    scene mbgn51 with dissolve
                                    jump bdomm
                            "Kecuali Anda menghentikan semuanya sekarang dan pergi ke kamar Anda":

                                b "Lalu aku bisa melupakannya"
                                s "..."
                                b "Apa yang kamu katakan?"
                                scene mbgn45 with dissolve
                                s "Ok"
                                b "Lalu kalahkan"
                                s "Ok"
                                scene mbgn48 with fade
                                m "[bname]"
                                m "Mengapa Anda tidak ada di kamar Anda?"
                                b "Kamu tidak apa apa"
                                m "Ya, dan Anda membumi"
                                b "Biarkan saya membawa Anda ke kamar Anda"
                                m "Dapatkan aku gelas sialan ini, itu luar biasa"
                                scene mbgn49 with fade
                                m "Dimana minuman saya?"
                                b "Di sini bersamaku"
                                b "Saya akan memberikannya kepada Anda jika Anda melakukan sesuatu untuk saya"
                                m "Berikan dulu"
                                b "Here"
                                scene mbgn50 with dissolve
                                m "Jadi apa yang kamu inginkan?"
                                scene mbgn51 with dissolve
                                jump bdomm
                    "Jangan":


                        pass
            else:

                pass
            scene mbgn41 with dissolve
            m "[sname] Cium aku"
            scene mbgn42 with dissolve
            m "Ahhh tidak ada di sana"
            scene mbgn43 with fade
            m "Selamat malam sayang"
            b "{i} (apa yang saya tonton saja) {/i}"
            scene black
            "..."
            jump newdays
        else:

            pass
        m "Baiklah, saya pikir saya akan tidur sekarang"
        scene mbgn17 with dissolve
        m "Selamat malam"
        s "Hmm"
        menu:
            "[sname] akan bertanya apakah dia bisa tidur di tempat tidur [mname]":
                scene mbgn18 with dissolve
                s "..."
                s "Bisakah aku tidur denganmu malam ini"
                m "Ok"
                m "Tapi aku mabuk"
                s "Aku akan membawamu ke kamarku"
                scene mbgn20 with fade
                m "Saya akan menyelesaikan gelas ini terlebih dahulu"
                m "Anda pergi tidur sekarang"
                scene chcm16 with fade
                "..."
                scene chcm17 with dissolve
                "..."
                scene chcm18 with dissolve
                "..."
                scene mbgn21 with dissolve
                "..."
                scene mbgn22 with dissolve
                "..."
                scene mbgn23 with dissolve
                m "Ahhh"
                scene mbgn24 with dissolve
                $ persistent.unlock_27 = True
                s "{i} (apakah dia bangun!) {/i}"
                s "{i} (Saya pikir sudah waktunya berhenti) {/i}"
                scene mbgn25 with fade
                m "[sname]?"
                s "Ya!"
                m "Saya perlu tidur di kamar saya"
                s "Ah Ok"
                scene black
                "..."
                jump newdays
            "Tidak perlu":

                s "Selamat malam"
                jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
