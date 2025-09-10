label mroomdiscuss:
    if mrel >=200 and elaine_convince == 4:
        scene mroom_av_da with fade
        b "Hi"
        scene mroom_av_d1a with hpunch
        m "Hah!"
        m "[bname]"
        pass
    else:
        scene mroom_av_d with fade
        b "Hi"
        scene mroom_av_d1 with hpunch
        m "Hah!"
        m "[bname]"
        pass

    scene mroom_av_d2 with fade
    m "Bagaimana Anda bisa masuk ke sini? !!"
    b "Pintu terbuka"
    m "Oke, jadi apa yang ingin kamu katakan padaku?"
    menu:
        "Saya tidak enak badan":
            b "Maksud saya tentang seluruh situasi ini"
            m "Apa yang salah dengan itu?"
            b "Tidak ada uang, tidak ada teman, tidak ada"
            b "Yang bisa kita lakukan hanyalah duduk di rumah"
            b "Atau pergi ke pantai"
            b "Maksudku, aku merindukan kehidupan yang kita miliki sebelumnya"
            m "Saya tahu sayang"
            m "Dan saya sedang mengerjakannya"
            scene mroom_av_d3 with dissolve
            m "Ini akan baik -baik saja"
            scene mroom_av_d4 with dissolve
            m "Saya akan melakukan apa pun yang saya bisa untuk membuat segalanya baik -baik saja"
            b "{i} (payudara sialan sangat dekat) {/i}"
            b "{i} (saya bahkan bisa menciumnya) {/i}"
            scene mroom_av_d5 with fade
            if mrel >=200 and elaine_convince == 4:
                m "Don't cry"
                menu:
                    "Aku tidak menangis":
                        pass
                    "Saya tidak bisa menahannya":

                        show screen mrelup
                        b "{i} (pekerjaan bagus [bname]) {/i}"
                        hide screen mrelup
                        b "{i} (dia merasa emosional) {/i}"
                        $ mrel += 2
                        pass
            else:


                pass
            m "Santai sayang, dan jangan khawatir tentang itu"
            b "Ok"
            if mbikini ==1:
                $ mbikini = 2
                b "Errm saya punya sesuatu untuk Anda"
                m "Oh, apa itu?"
                b "A bikini"
                scene mroom_av_d10 with dissolve
                m "Ohh terima kasih"
                b "..."
                scene mroom_av_d11 with dissolve
                m "{i} (hmmm, mungkin itu ide yang bagus untuk mendapatkan kepercayaan diri di sekitar pria) {/i}"
                "..."
                scene mroom_av_d10 with dissolve
                m "Saya memberi tahu Anda apa"
                m "Biarkan saya memakainya untuk Anda"
                m "Saya pikir Anda pantas menjadi orang pertama yang melihatnya"
                b "Ya keren"
                m "Tolong putar saat saya berubah"
                scene mroom_av_d12 with dissolve
                "..."
                m "Bagaimana menurutmu?"
                scene mroom_av_d13 with dissolve
                menu:
                    "Wow seksi!":
                        $ mrel -= 1
                        m "Terima kasih"
                        m "Sampai jumpa"
                        scene door with fade
                        b "{i} (...) {/i}"
                        call screen gnav
                    "Cantik":

                        scene mroom_av_d14 with dissolve
                        m "Terima kasih"
                        b "It's nothing"
                        m "Sampai jumpa"
                        scene door with fade
                        b "{i} (...) {/i}"
                        call screen gnav

            elif mbikini ==2:
                m "{i} (mungkin saya bisa) {/i}"
                scene mroom_av_d20 with dissolve
                m "{i} (tidak [mname] dia bukan tikus lab Anda) {/i}"
                m "{i} (tapi itu tidak akan terluka, itu seperti aku di kolam bersamanya) {/i}"
                m "{i} (ya itu akan membuatnya merasa dihargai dengan mengambil pendapatnya) {/i}"
                m "{i} (dan itu meningkatkan kepercayaan diri saya juga) {/i}"
                m "{i} (win win!) {/i}"
                b "Sampai jumpa lagi"
                scene mroom_av_d21 with dissolve
                m "Tunggu!"
                b "Apa?"
                m "Saya ingin memasang sesuatu untuk Anda"
                m "Tolong berpaling saat saya berubah"
                b "Ok"
                scene mroom_av_d12 with dissolve
                "..."
                menu:
                    "Mengintip":
                        scene mroom_av_d22 with dissolve
                        b "{i} (wow!) {/i}"
                        menu:
                            "Melanjutkan":
                                pass
                            "Terus mengintip":
                                scene mroom_av_d23 with dissolve
                                $ mrel -= 1
                                b "{i} (wow wow!) {/i}"
                                scene mroom_av_d24 with dissolve
                                show screen mreldw
                                m "..."
                                hide screen mreldw
                                scene mroom_av_d25 with dissolve
                                b "{i} (oh fuck!) {/i}"
                                m "Bagaimana menurutmu?"
                                pass
                    "Jangan":


                        m "Bagaimana menurutmu?"
                        pass
                scene mroom_av_d26 with dissolve
                b "Bagus"
                b "Anda harus memakainya ke pantai"
                scene mroom_av_d26a with dissolve
                m "Ya saya akan memikirkannya"
                scene mroom_av_d27 with dissolve
                m "Thanks again"
                m "Sampai jumpa"
                scene door with fade
                b "{i} (...) {/i}"
                call screen gnav
            else:


                m "Sampai jumpa"
                scene door with fade
                b "{i} (sialan, saya tidak tahu apa yang harus dilakukan) {/i}"
                b "{i} (Saya tidak bisa berpura -pura tidak bersalah selamanya) {/i}"
                if mpracticegift ==0:
                    b "{i} (mungkin aku harus memberinya hadiah, seperti [sname]) {/i}"
                    $ mpracticegift = 1
                    pass
                else:
                    pass
                "..."
                call screen gnav
        "Kamu tidak apa apa?":



            m "Ya saya"
            m "Tapi saya lebih suka tetap sendiri"
            m "Please"
            if persistent.patch_enabled:
                b "Tentang ayah ..."
                pass
            else:
                b "Tentang Stewart ..."
                pass

            m "Ya ada apa dengan dia?"
            b "Bajingan, dia melupakan kita"
            scene mroom_av_d6 with dissolve
            m "..."
            b "{i} (oh, dia menderita sebanyak itu) {/i}"
            menu:
                "Mengintip":
                    scene mroom_av_d7 with dissolve
                    b "Hmm"
                    m "[bname]"
                    m "Saya ingin tetap sendirian, silakan pergi"
                    b "Errm ok"
                    if mpracticegift ==0:
                        b "{i} (mungkin aku harus memberinya hadiah, seperti [sname]) {/i}"
                        $ mpracticegift = 1
                        pass
                    else:
                        pass

                    scene door with fade
                    "..."
                    call screen gnav
                "Beri dia pelukan":

                    scene mroom_av_d8 with dissolve
                    show screen mrelup
                    $ mrel += 1
                    b "Tolong santai saja"
                    hide screen mrelup
                    m "Terima kasih atas dukungannya [bname]"
                    scene mroom_av_d9 with dissolve
                    b "Ya ya, tidak apa -apa"
                    b "{i} (sialan, saya tidak tahu apa yang harus dilakukan) {/i}"
                    b "{i} (Saya tidak bisa berpura -pura tidak bersalah selamanya) {/i}"
                    if mpracticegift ==0:
                        b "{i} (mungkin aku harus memberinya hadiah, seperti [sname]) {/i}"
                        $ mpracticegift = 1
                        pass
                    else:
                        pass
                    b "Aku akan pergi sekarang"
                    scene door with fade
                    "..."
                    call screen gnav

                "Beri dia tasnya" if mbag ==1:
                    $ mbag = 2
                    $ mrel += 2
                    b "Aku punya sesuatu untukmu"
                    scene mroom_av_d15 with dissolve
                    m "Apa itu?"
                    b "A bag"
                    b "Ambillah"
                    scene mroom_av_d8 with hpunch
                    m "Ohh [bname]"
                    show screen mrelup
                    m "Terima kasih"
                    hide screen mrelup
                    scene mroom_av_d9 with dissolve
                    b "{i} (terima kasih untuk itu) {/i}"
                    scene mroom_av_d16 with dissolve
                    "..."
                    scene mroom_av_d17 with fade
                    m "Itu indah kan?"
                    scene mroom_av_d18 with dissolve
                    b "Memang itu"
                    m "Tapi merek ini mahal"
                    m "Bagaimana Anda bisa membayarnya?"
                    scene mroom_av_d17 with dissolve
                    b "Jangan khawatir tentang itu"
                    b "Saya membayarnya dari gaji saya di toko ponsel"
                    scene mroom_av_d19 with dissolve
                    m "Toko seluler yang mana?"
                    b "Saya katakan bahwa saya mulai bekerja paruh waktu"
                    m "Anda melakukannya?"
                    b "Yes"
                    scene mroom_av_d17 with dissolve
                    m "Ok mungkin saya lupa"
                    m "Pokoknya sampai jumpa nanti"
                    m "Terima kasih untuk tasnya"
                    scene door with fade
                    "..."
                    call screen gnav

                "Beri dia bagian atas dan bawah sehari -hari" if mtrelax ==1:
                    $ mtrelax = 2
                    $ mrel += 5
                    b "Aku punya sesuatu untukmu"
                    scene mroom_av_d15 with dissolve
                    m "Apa itu?"
                    b "Ini"
                    scene mroom_av_d8 with hpunch
                    m "Ohh [bname]"
                    show screen mrelup
                    m "Terima kasih"
                    hide screen mrelup
                    scene mroom_av_d9 with dissolve
                    b "{i} (terima kasih untuk itu) {/i}"
                    m "Sampai jumpa"
                    scene mroom_av_d21 with dissolve
                    m "..."
                    m "Tunggu, biarkan aku mengenakannya"
                    m "Tolong berpaling saat saya berubah"
                    b "Ok"
                    scene mroom_av_d12 with dissolve
                    "..."
                    menu:
                        "Mengintip":
                            scene mroom_av_d28 with dissolve
                            b "{i} (wow!) {/i}"
                            menu:
                                "Melanjutkan":
                                    pass
                                "Terus mengintip":
                                    scene mroom_av_d29 with dissolve
                                    $ mrel -= 1
                                    b "{i}(Wow){/i}"
                                    scene mroom_av_d30 with dissolve
                                    show screen mreldw
                                    m "..."
                                    hide screen mreldw
                                    scene mroom_av_d31 with dissolve
                                    b "{i} (oh fuck!) {/i}"
                                    m "Bagaimana menurutmu?"
                                    pass
                        "Jangan":


                            m "Bagaimana menurutmu?"
                            pass

                    scene mroom_av_d32 with dissolve
                    b "Bagus"
                    m "Thanks again"
                    m "Sampai jumpa"
                    scene door with fade
                    b "{i} (...) {/i}"
                    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
