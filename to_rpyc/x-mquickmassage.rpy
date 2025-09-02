label mquickmassage:
    scene mroom_qm with fade
    m "Beri aku sesaat"
    m "I'll change"
    b "Ok"
    "..."
    m "Maksud saya tunggu di pintu"
    m "Atau lihat saja"
    b "Ah yeah"
    scene m_room_p8 with dissolve
    "..."
    m "Done"
    scene mroom_qm1 with dissolve
    m "Di mana Anda ingin melakukannya?"
    menu:
        "Di tempat tidur":
            $ mrel -= 1
            show screen mreldw
            "..."
            hide screen mreldw
            b "{i} (Sepertinya itu jawaban yang salah) {/i}"
            pass
        "Dimanapun itu nyaman untuk Anda":

            $ mrel += 1
            pass
    scene mroom_qm2 with fade
    b "Jadi di mana paling menyakitkan?"
    if melsw >=9:
        m "Everywhere"
        b "Ok"
        scene mroom_qm3 with dissolve
        "..."
        scene mroom_qm4 with dissolve
        b "Bagaimana?"
        m "Ya bagus"
        b "Di mana lagi itu menyakitkan?"
        scene mroom_qm5 with dissolve
        "..."
        pass
    else:
        m "Lenganku, sepanjang hari aku membawa nampan bir"
        b "Ok"
        scene mroom_qm3 with dissolve
        "..."
        scene mroom_qm4 with dissolve
        b "Bagaimana?"
        m "Ya bagus"
        b "Di mana lagi itu menyakitkan?"
        scene mroom_qm5 with dissolve
        m "{i} (apakah saya menyuruhnya melakukan punggung atau tidak?) {/i}"
        m "{i} (itu tidak sesuai di tempat tidur) {/i}"
        "..."
        pass
    if mrel >=110:
        m "{i} (Saya kira sedikit pijat tidak akan terluka) {/i}"
        m "{i} (Plus menganggapnya sebagai pelatihan kecil untuk meningkatkan kepercayaan diri Anda) {/i}"
        pass
    else:
        scene mroom_qm4 with dissolve
        m "Itu cukup sayang"
        b "Ok"
        m "Terima kasih, Anda bisa pergi sekarang"
        m "Saya akan menyiapkan makan malam"
        scene door with fade
        "Naikkan poin hubungan Anda menjadi 110"
        call screen gnav


    scene mroom_qm4 with dissolve
    m "Punggung bawahku"
    m "Itu karena mengenakan sepatu hak tinggi sepanjang hari"
    b "Oh aku sudah mengerti"
    scene mroom_qm6 with fade
    b "Jadi, bagaimana Anda ingin saya melakukannya?"
    m "Pertama lepaskan bantal, jadi saya bisa memiliki ruang untuk kaki saya"
    m "Aku jatuh di sini"
    b "Oh Ok"
    b "Dan..."
    b "Bisakah saya duduk di atas Anda?"
    m "Lakukan apapun yang Anda inginkan, singkirkan rasa sakitnya"
    menu:
        "{s} Bisakah saya mendapatkan bir terlebih dahulu? {/s}" if mrel <200:
            "Tidak tersedia untuk Anda, angkat poin Anda, 200"
            m "No"
            pass

        "Bisakah saya minum bir dulu?" if mrel >=200:
            m "Ide bagus"
            m "Dapatkan aku satu juga"
            jump mquickmassagewithdrinks
        "Melanjutkan":


            pass

    m "Kami tidak punya banyak waktu"
    m "Saya perlu menyiapkan makan malam"
    menu:
        "Duduklah padanya":
            scene mroom_qm9 with dissolve
            "..."
            scene mroom_qm10 with dissolve
            b "{i} (sangat dekat untuk menggesernya di antara pipinya) {/i}"
            $ mcorr += 1
            m "Itu seharusnya cukup [bname]"
            m "Anda bisa pergi sekarang"
            scene door with fade
            "..."
            call screen gnav
        "Lakukan dari samping":

            scene mroom_qm7 with dissolve
            "..."
            scene mroom_qm8 with dissolve
            b "{i} (tampilan bagus) {/i}"
            m "Itu seharusnya cukup [bname]"
            m "Anda bisa pergi sekarang"
            scene door with fade
            "..."
            call screen gnav


label mquickmassagewithdrinks:
    scene mroom_qm12 with fade
    "..."
    scene mroom_qm11 with fade
    b "Ini salah satu untuk Anda"
    m "Terima kasih, lanjutkan"
    scene mroom_qm7 with fade
    "..."
    scene mroom_qm8 with dissolve
    "..."
    menu:
        "Lakukan lehernya":
            b "Biarkan saya melakukan leher Anda"
            scene mroom_qm13 with fade
            m "Anda pandai dalam hal itu"
            b "Thanks"
            scene mroom_qm14 with dissolve
            b "{i} (tampilan bagus) {/i}"
            scene mroom_qm15 with dissolve
            b "{i} (dan posisi ini!) {/i}"
            b "{i} (Saya hanya perlu mencabutnya) {/i}"
            if m_bbruises == 1:
                m "Saya pikir itu cukup [bname]"
                m "Bagaimana memar Anda"
                b "Better now"
                m "Berhenti dan tunjukkan padaku"
                scene mroom_qm20 with fade
                m "Apakah ini baru?!"
                b "Tidak, sama"
                b "Tapi saya tidak tahu mengapa itu semakin rendah"
                m "Ah ya, memar cenderung mengikuti gravitasi"
                m "Ini berarti semakin baik"
                b "Seriously"
                m "Ya saya mengingatnya dari kursus perawat saya"
                b "{i} (perawat!) {/i}"
                scene mroom_qm21bw with fade
                b "{i}(Hmmm){/i}"
                $ mnurse_im = 1
                m "[bname]!"
                scene mroom_qm20 with dissolve
                m "[bname]!"
                scene mroom_qm22bw with fade
                m "[bname] !!"
                scene mroom_qm20 with dissolve
                m "Apa yang salah denganmu"
                scene mroom_qm21 with dissolve
                m "Hah!"
                b "Ahh"
                b "Maaf!"
                scene mroom_qm22 with dissolve
                m "Saya kira sudah saatnya bagi saya untuk menyiapkan makan malam"
                b "Ok"
                scene door with fade
                "..."
                call screen gnav
            else:

                m "Saya pikir itu cukup [bname]"
                b "Oke, saya akan pergi"
                scene door with fade
                "..."
                call screen gnav
        "Lanjutkan di bagian belakang":


            if day ==2:
                jump mquickmalt
            elif day ==3:
                jump mquickmalt

            elif day ==5:
                jump mquickmalt1
            elif day ==6:
                jump mquickmalt1
            else:
                pass
            scene mroom_qm9 with fade
            "..."
            scene mroom_qm10 with dissolve
            b "{i} (sangat dekat untuk menggesernya di antara pipinya) {/i}"
            $ mcorr += 1
            m "Itu seharusnya cukup [bname]"
            m "Anda bisa pergi sekarang"
            menu:
                "Bisakah saya melakukan paha Anda?" if mcorr >=20:
                    m "Ya biarkan saya menyalakan punggung saya"
                    b "{i} (dia ingin mengawasi saya saat saya melakukannya) {/i}"
                    scene mroom_qm16 with fade
                    "..."
                    scene mroom_qm17 with dissolve
                    "..."
                    scene mroom_qm18 with dissolve
                    "..."
                    scene mroom_qm17 with dissolve
                    b "{i} (sialan ...) {/i}"
                    scene mroom_qm18 with dissolve
                    b "{i} (sangat dekat sejauh ini) {/i}"
                    scene mroom_qm19 with dissolve
                    "..."
                    m "Saya pikir itu cukup"
                    scene mroom_qm16 with dissolve
                    m "Terima kasih sayang"
                    if m_bbruises == 1:
                        m "Bagaimana memar Anda"
                        b "Better now"
                        m "Berhenti dan tunjukkan padaku"
                        scene mroom_qm20 with fade
                        m "Apakah ini baru?!"
                        b "Tidak, sama"
                        b "Tapi saya tidak tahu mengapa itu semakin rendah"
                        m "Ah ya, memar cenderung mengikuti gravitasi"
                        m "Ini berarti semakin baik"
                        b "Seriously"
                        m "Ya saya mengingatnya dari kursus perawat saya"
                        b "{i} (perawat!) {/i}"
                        scene mroom_qm21bw with fade
                        b "{i}(Hmmm){/i}"
                        $ mnurse_im = 1
                        m "[bname]!"
                        scene mroom_qm20 with dissolve
                        m "[bname]!"
                        scene mroom_qm22bw with fade
                        m "[bname] !!"
                        scene mroom_qm20 with dissolve
                        m "Apa yang salah denganmu"
                        scene mroom_qm21 with dissolve
                        m "Hah!"
                        b "Ahh"
                        b "Maaf!"
                        scene mroom_qm22 with dissolve
                        m "Saya kira sudah saatnya bagi saya untuk menyiapkan makan malam"
                        b "Ok"
                        menu:
                            "Apakah Anda ingin saya melakukan kaki Anda?":
                                m "Mhmm"
                                m "Sedikit Ya"
                                m "Beri aku bantal dulu"
                                scene mroom_qm23 with dissolve
                                m "Ahh"
                                scene mroom_qm24 with dissolve
                                m "{i} (oh Tuhan ini terasa enak) {/i}"
                                scene mroom_qm24w with dissolve

                                m "{i} (hentikan [mname]) {/i}"
                                scene mroom_qm26 with dissolve

                                m "{i} (hentikan pemikiran itu [mname]) {/i}"
                                scene mroom_qm23 with dissolve
                                b "Jadi apakah itu bagus?"
                                b "Anda telah diam sebentar"
                                m "Ya ya sayang"
                                m "Anda bisa pergi sekarang"
                                b "Ok"
                                scene door with fade
                                "..."
                                call screen gnav
                            "Apakah Anda yakin Anda baik -baik saja?":

                                if mrel >=200 and mcorr >=25:
                                    m "Ya saya"
                                    b "Ok saya akan pergi sekarang"
                                    "..."
                                    m "Tunggu di sana sesuatu yang ingin saya tunjukkan"
                                    scene mroom_qm27 with dissolve
                                    b "{i} (apakah dia membuka pakaian tanpa meminta saya untuk berbalik? !!) {/i}"
                                    scene mroom_qm28 with dissolve
                                    m "Hmm"
                                    m "Dimana saya meletakkannya?"
                                    scene mroom_qm29 with dissolve
                                    m "Ah itu di lemari pakaian, sekarang saya ingat"
                                    scene mroom_qm30 with fade
                                    "..."
                                    scene mroom_qm32 with dissolve
                                    b "{i} (saya tidak bisa mempercayai mata saya) {/i}"
                                    b "{i} (apakah dia menguji saya, atau dia tidak benar -benar peduli) {/i}"
                                    scene mroom_qm31 with fade
                                    m "Jadi bagaimana menurut Anda?"
                                    b "Cantik"
                                    b "Itu gaun malam"
                                    b "Apakah Anda berencana pergi makan malam"
                                    m "Maybe soon"
                                    b "Ah begitu"
                                    b "Oke, saya akan pergi sekarang"
                                    m "Tunggu aku akan menunjukkan sesuatu yang lain"
                                    scene mroom_qm42 with dissolve
                                    "..."
                                    scene mroom_qm43 with dissolve
                                    b "Oh"
                                    m "Apa oh"
                                    scene mroom_qm44 with dissolve
                                    b "Oh bagus"
                                    scene mroom_qm45 with dissolve
                                    m "Anda bisa pergi sekarang"
                                    b "Ok"
                                    scene door with fade
                                    "..."
                                    call screen gnav
                                else:

                                    m "Ya saya"
                                    m "Anda bisa pergi sekarang"
                                    b "Ok"
                                    scene door with fade
                                    "Naikkan poin hubungan Anda menjadi 200 dan poin korupsi menjadi 25"
                                    call screen gnav




                        scene door with fade
                        "..."
                        call screen gnav
                    else:

                        b "Ok"
                        menu:
                            "Apakah Anda ingin saya melakukan kaki Anda?":
                                m "Mhmm"
                                m "Sedikit Ya"
                                m "Beri aku bantal dulu"
                                scene mroom_qm23 with dissolve
                                m "Ahh"
                                scene mroom_qm24 with dissolve
                                m "{i} (oh Tuhan ini terasa enak) {/i}"
                                scene mroom_qm24w with dissolve

                                m "{i} (hentikan [mname]) {/i}"
                                scene mroom_qm25 with dissolve

                                m "{i} (hentikan pemikiran itu [mname]) {/i}"
                                scene mroom_qm23 with dissolve
                                b "Jadi apakah itu bagus?"
                                b "Anda telah diam sebentar"
                                m "Ya ya sayang"
                                m "Anda bisa pergi sekarang"
                                b "Ok"
                                scene door with fade
                                "..."
                                call screen gnav
                            "Apakah Anda yakin Anda baik -baik saja?":

                                if mrel >=200 and mcorr >=25:
                                    m "Ya saya"
                                    b "Ok saya akan pergi sekarang"
                                    "..."
                                    m "Tunggu di sana sesuatu yang ingin saya tunjukkan"
                                    scene mroom_qm27 with dissolve
                                    b "{i} (apakah dia membuka pakaian tanpa meminta saya untuk berbalik? !!) {/i}"
                                    scene mroom_qm28 with dissolve
                                    m "Hmm"
                                    m "Dimana saya meletakkannya?"
                                    scene mroom_qm29 with dissolve
                                    m "Ah itu di lemari pakaian, sekarang saya ingat"
                                    scene mroom_qm30 with fade
                                    b "{i} (saya tidak bisa mempercayai mata saya) {/i}"
                                    scene mroom_qm31 with dissolve
                                    m "Jadi bagaimana menurut Anda?"
                                    b "Cantik"
                                    b "Itu gaun malam"
                                    b "Apakah Anda berencana pergi makan malam"
                                    m "Maybe soon"
                                    b "Ah begitu"
                                    b "Oke, saya akan pergi sekarang"
                                    m "Tunggu aku akan menunjukkan sesuatu yang lain"
                                    scene mroom_qm42 with dissolve
                                    "..."
                                    scene mroom_qm43 with dissolve
                                    b "Oh"
                                    m "Apa oh"
                                    scene mroom_qm44 with dissolve
                                    b "Oh bagus"
                                    scene mroom_qm45 with dissolve
                                    m "Anda bisa pergi sekarang"
                                    b "Ok"
                                    scene door with fade
                                    "..."
                                    call screen gnav
                                else:

                                    m "Ya saya"
                                    m "Anda bisa pergi sekarang"
                                    b "Ok"
                                    scene door with fade
                                    "Naikkan poin hubungan Anda menjadi 200 dan poin korupsi menjadi 25"
                                    call screen gnav


                "{s} Bisakah saya melakukan paha Anda? {/s}" if mcorr <20:
                    m "Tidak, tidak apa -apa untuk saat ini"
                    b "Oke, saya akan pergi"
                    "Meningkatkan korupsi menjadi 20"
                    pass
                "Pergi":

                    pass
            scene door with fade
            "..."
            call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc