label nudebeach_jenelainereturn:
    $ mboobstalk = 1
    if mnameboobs == 1:
        $ mnameboobs = 0
        scene nbeachr with fade
        m "..."
        m "Ikuti saya, saya ingin menunjukkan sesuatu kepada Anda"
        scene nbeachr1 with fade
        m "Tolong bantu saya dengan bra"
        scene nbeachr2 with dissolve
        "..."
        scene nbeachr3 with dissolve
        "..."
        scene nbeachr4 with dissolve
        m "Saya akan menunjukkan set baru saya"
        scene nbeachr5 with dissolve
        b "{i} (oh my fucking god) {/i}"
        scene nbeachr6 with fade
        m "Bagaimana menurutmu?"
        m "Apakah itu terlalu terbuka?"
        b "Tidak sama sekali, itu luar biasa"
        m "Ok saya akan berubah sekarang"
        scene nbeachr7 with fade
        m "Dengarkan [bname] Saya tahu apa yang Anda katakan tidak sesuai, tapi ..."
        b "Sorry"
        m "Tidak, jangan khawatir, dia yang bertanya"
        m "Sebenarnya senang Anda mengatakan milik saya lebih baik"
        b "I've just said the truth"
        scene nbeachr8 with dissolve
        m "Anda pantas mendapatkan pelukan untuk itu"
        b "{i} (Apakah perangkap semacam ini!) {/i}"
        b "{i} (dia menggarisbawahi dan menawari saya pelukan!) {/i}"
        scene nbeachr9 with dissolve
        m "Terima kasih"
        scene nbeachr10 with dissolve
        b "{i} (sialan dia meletakkan tangannya!) {/i}"
        scene nbeachr9 with dissolve
        m "Sampai jumpa lagi"
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav



    elif elaineboobs == 1:
        $ elaineboobs = 0
        scene nbeachr11 with fade
        m "..."
        m "Ikuti saya ke kamar saya"
        scene nbeachr12 with fade
        m "Dengarkan [bname] Apa yang Anda katakan di pantai tidak sesuai"
        b "Tapi ... dia bertanya padaku"
        m "Omong kosong, Anda juga tidak perlu menatap payudaranya"
        b "I didn't"
        m "Dan Anda tidak boleh juga memberitahunya bahwa Anda lebih suka miliknya"
        menu:
            "Tapi mereka besar":
                scene nbeachr13 with dissolve
                m "Hah!"
                scene nbeachr14 with dissolve
                b "Aduh!"
                m "Besar dan terkulai ya!"
                b "Tapi cantik"
                $ mcorr += 2
                if mcorr >= 55:
                    m "Anda tidak tahu apa -apa"
                    m "Lihat"
                    scene nbeachr15 with dissolve
                    m "Apakah Anda melihat sesuatu yang terkulai?"
                    m "Or saggy"
                    b "No"
                    b "Maksud saya, saya tidak pernah dibandingkan"
                    b "..."
                    m "Kemarilah"
                    scene nbeachr16 with dissolve
                    m "Feel it"
                    scene nbeachr17 with dissolve
                    "..."
                    m "Tegas atau tidak?"
                    b "Kencang, dan terasa lembut saat disentuh pada saat bersamaan"
                    m "Exactly"
                    m "Jadi siapa yang memiliki payudara yang indah?"
                    b "Tentu saja, tapi aku malu untuk mengatakannya"
                    b "Itu tidak terasa benar"
                    b "Dan sejujurnya saya takut dengan reaksi Anda"
                    scene nbeachr18 with dissolve
                    m "Jangan pernah menjadi reaksi saya, lebih baik daripada menyakiti perasaan saya"
                    menu:
                        "Cium mereka":
                            $ mboobskiss += 1
                            scene nbeachr19 with dissolve
                            b "Sorry"
                            m "Oh"
                            scene nbeachr20 with dissolve
                            m "Hmm"
                            if mboobskiss <=2:
                                scene nbeachr21 with dissolve
                                m "Sampai jumpa nanti sayang"
                                scene hall_d with fade
                                b "{i} (...) {/i}"
                                call screen gnav
                            else:
                                scene nbeachr22 with dissolve
                                m "Ahh [bname]"
                                m "Ini tidak sesuai"
                                scene nbeachr23 with vpunch
                                b "Mhhm"
                                menu:
                                    "Cium dia":
                                        scene nbeachr24 with dissolve
                                        m "Enough [bname]"
                                        scene nbeachr21 with fade
                                        m "Sampai jumpa nanti sayang"
                                        scene hall_d with fade
                                        b "{i} (...) {/i}"
                                        call screen gnav
                                    "Berbalik dan peluknya":
                                        scene nbeachr25 with dissolve
                                        "..."
                                        scene nbeachr26 with dissolve
                                        m "{i} (apakah penisnya menyentuh saya) {/i}"
                                        m "Sampai jumpa nanti sayang"
                                        scene hall_d with fade
                                        b "{i} (...) {/i}"
                                        call screen gnav
                        "Tidak melakukan apa -apa":


                            scene nbeachr21 with dissolve
                            m "Sampai jumpa nanti sayang"
                            scene hall_d with fade
                            b "{i} (...) {/i}"
                            call screen gnav
                else:


                    m "Keluar!"
                    scene hall_d with fade
                    b "{i}(Damn it){/i}"
                    "Naikkan poin korupsi Anda menjadi 55"
                    call screen gnav
            "Ok maaf":

                m "Keluar!"
                scene hall_d with fade
                b "{i}(Damn it){/i}"
                call screen gnav
    else:

        scene nbeachr with fade
        m "Sampai jumpa"
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
