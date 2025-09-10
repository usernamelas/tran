label mquickmalt:
    scene mroom_qm9 with fade
    "..."
    scene mroom_qm10 with dissolve
    b "{i} (sangat dekat untuk menggesernya di antara pipinya) {/i}"
    $ mcorr += 1
    scene mroom_qm10a with dissolve
    m "Itu seharusnya cukup [bname]"
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
            b "Ok"
            menu:
                "Biarkan saya melakukan kaki Anda?":
                    m "Mhmm"
                    m "Sedikit Ya"
                    m "Beri aku bantal dulu"
                    scene mroom_qm23 with dissolve
                    m "Ahh"
                    scene mroom_qm24 with dissolve
                    m "{i} (oh Tuhan ini terasa enak) {/i}"
                    scene mroom_qm24w with dissolve

                    m "{i} (hentikan [mname]) {/i}"
                    scene mroom_qm25bw with dissolve

                    m "{i} (hentikan pemikiran itu [mname]) {/i}"
                    scene mroom_qm25abw with dissolve
                    m "Ahh"
                    scene mroom_qm25bbw with dissolve
                    m "..."
                    if mrel >= 300:
                        pass
                    else:
                        pass
                    scene mroom_qm23 with dissolve
                    b "Jadi apakah itu bagus?"
                    if mfuckedsober >=1:
                        scene mroom_qmf23 with dissolve
                        m "Yes"
                        scene mroom_qmf24 with dissolve
                        b "Huh"
                        m "Hapus celana pendek Anda"
                        scene mfjob02 with dissolve
                        m "Mhhm"
                        scene mfjob05 with dissolve
                        b "Ah"
                        scene mfjob06 with dissolve
                        "..."
                        scene mfjob40 with dissolve
                        "..."
                        scene mfjob80 with dissolve
                        m "..."
                        scene mroom_qmf25 with dissolve
                        "..."
                        m "Anda bisa pergi sekarang"
                        b "Ok"
                        scene door with fade
                        "..."
                        call screen gnav
                    else:
                        pass
                    scene mroom_qm23a with dissolve
                    b "Anda telah diam sebentar"
                    m "Ya ya sayang"
                    m "Anda bisa pergi sekarang"
                    b "Ok"
                    scene door with fade
                    "..."
                    call screen gnav
                "Melanjutkan":

                    if mrel >=200 and mcorr >=25:
                        m "Tunggu di sana sesuatu yang ingin saya tunjukkan"
                        scene mroom_qm27 with fade
                        b "{i} (apakah dia membuka pakaian tanpa meminta saya untuk berbalik? !!) {/i}"
                        scene mroom_qm28 with dissolve
                        m "Hmm"
                        m "Dimana saya meletakkannya?"
                        scene mroom_qm29 with dissolve
                        m "Ah itu di lemari pakaian, sekarang saya ingat"
                        scene mroom_qm30 with fade
                        b "{i} (saya tidak bisa mempercayai mata saya) {/i}"
                        scene mroom_qm32 with dissolve
                        b "{i} (apakah dia menguji saya, atau dia tidak benar -benar peduli) {/i}"
                        scene mroom_qm31 with dissolve
                        m "Jadi bagaimana menurut Anda?"
                        b "Cantik"
                        b "Itu gaun malam"
                        b "Apakah Anda berencana pergi makan malam"
                        m "Maybe soon"
                        b "Ah begitu"
                        b "Apakah Anda memiliki sesuatu yang lain?"
                        m "No"
                        if jenteaselingerie ==1:
                            b "Tapi Anda berjanji kepada saya untuk menunjukkan sesuatu"
                            m "Kapan itu?"
                            b "Setelah malam Anda dengan Elaine"
                            m "Huh"
                            m "Mungkin itu ..."
                            m "Saya tidak berpikir saya mengatakan bahwa saya akan menunjukkan itu"
                            m "Biarkan saya mendapatkannya"
                            scene mroom_qm39 with dissolve
                            "..."
                            if melsw >=9:
                                scene mroom_qm40a with dissolve
                                b "Bagus"
                                b "Apakah itu untuk bekerja?"
                                m "Yes"
                                scene mroom_qm41a with dissolve
                                m "Enough"
                                pass
                            else:
                                pass
                            scene mroom_qm40 with dissolve
                            b "Bagus"
                            b "Di mana Anda berencana untuk memakainya?"
                            scene mroom_qm41 with dissolve
                            m "Enough"
                            pass
                        else:
                            pass
                        b "Oke, saya akan pergi sekarang"
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


label mquickmalt1:
    scene mroom_qm9 with fade
    "..."
    scene mroom_qm10 with dissolve
    b "{i} (sangat dekat untuk menggesernya di antara pipinya) {/i}"
    $ mcorr += 1
    scene mroom_qm10a with dissolve
    m "Itu sangat bagus [bname]"
    menu:
        "Bisakah saya melakukan paha Anda?" if mcorr <20:
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
            b "Ok"
            menu:
                "Biarkan saya melakukan kaki Anda?":
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
                    scene mroom_qm25abw with dissolve
                    m "Ahh"
                    scene mroom_qm25bbw with dissolve
                    m "..."
                    if mrel >= 300:
                        pass
                    else:
                        pass
                    scene mroom_qm23 with dissolve
                    b "Jadi apakah itu bagus?"
                    if mfuckedsober >=1:
                        scene mroom_qmf23 with dissolve
                        m "Yes"
                        scene mroom_qmf24 with dissolve
                        b "Huh"
                        m "Hapus celana pendek Anda"
                        scene mfjob02 with dissolve
                        m "Mhhm"
                        scene mfjob05 with dissolve
                        b "Ah"
                        scene mfjob06 with dissolve
                        "..."
                        scene mfjob40 with dissolve
                        "..."
                        scene mfjob80 with dissolve
                        m "..."
                        scene mroom_qmf25 with dissolve
                        "..."
                        m "Anda bisa pergi sekarang"
                        b "Ok"
                        scene door with fade
                        "..."
                        call screen gnav
                    else:
                        pass
                    scene mroom_qm23a with dissolve
                    b "Anda telah diam sebentar"
                    m "Ya ya sayang"
                    m "Anda bisa pergi sekarang"
                    b "Ok"
                    scene door with fade
                    "..."
                    call screen gnav
                "Melanjutkan":

                    if mrel >=200 and mcorr >=25:
                        m "Tunggu di sana sesuatu yang ingin saya tunjukkan"
                        scene mroom_qm27 with fade
                        b "{i} (apakah dia membuka pakaian tanpa meminta saya untuk berbalik? !!) {/i}"
                        scene mroom_qm28 with dissolve
                        m "Hmm"
                        m "Dimana saya meletakkannya?"
                        scene mroom_qm29 with dissolve
                        m "Ah itu di lemari pakaian, sekarang saya ingat"
                        scene mroom_qm30 with fade
                        b "{i} (saya tidak bisa mempercayai mata saya) {/i}"
                        scene mroom_qm32 with dissolve
                        b "{i} (apakah dia menguji saya, atau dia tidak benar -benar peduli) {/i}"
                        scene mroom_qm31 with dissolve
                        m "Jadi bagaimana menurut Anda?"
                        b "Cantik"
                        b "Itu gaun malam"
                        b "Apakah Anda berencana pergi makan malam"
                        m "Maybe soon"
                        b "Ah begitu"
                        b "Oke, saya akan pergi sekarang"
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

        "Bisakah saya melakukan paha Anda?" if mcorr >=20:
            scene mroom_qm33 with dissolve
            "..."
            m "Yes"
            scene mroom_qm34 with dissolve
            m "Ya itu tempatnya"
            b "{i} (wow!) {/i}"
            scene mroom_qm35 with dissolve
            m "Saya \ m maaf telah membuat suara [bname]"
            m "Tapi aku sangat lelah hari ini"
            b "Jangan khawatir tentang itu"
            scene mroom_qm34 with dissolve
            m "Continue please"
            scene mroom_qm36 with dissolve
            "..."
            scene mroom_qm37 with dissolve
            m "Oh ya, kamu menjadi lebih baik"
            m "Cukup saya pikir"
            m "Lakukan sesuatu yang lain"
            menu:
                "Biarkan saya melakukan kaki Anda?":
                    m "Mhm Ok"
                    m "Biarkan aku berbalik"
                    scene mroom_qm16 with fade
                    m "Tolong beri saya bantal"
                    scene mroom_qm23 with dissolve
                    m "Ahh"
                    scene mroom_qm24 with dissolve
                    m "{i} (oh Tuhan ini terasa enak) {/i}"
                    scene mroom_qm24w with dissolve

                    m "{i} (hentikan [mname]) {/i}"
                    scene mroom_qm25 with dissolve

                    m "{i} (hentikan pemikiran itu [mname]) {/i}"
                    scene mroom_qm25abw with dissolve
                    m "Ahh"
                    scene mroom_qm25bbw with dissolve
                    m "..."
                    if mrel >= 400:
                        scene mroom_qm23 with dissolve
                        b "Jadi apakah itu bagus?"
                        scene mroom_qmf23 with dissolve
                        m "Yes"
                        scene mroom_qmf24 with dissolve
                        b "Huh"
                        m "Hapus celana pendek Anda"
                        scene mfjob02 with dissolve
                        m "Mhhm"
                        scene mfjob05 with dissolve
                        b "Ah"
                        scene mfjob06 with dissolve
                        "..."
                        scene mfjob40 with dissolve
                        "..."
                        scene mfjob80 with dissolve
                        m "..."
                        scene mroom_qmf25 with dissolve
                        "..."
                        m "Anda bisa pergi sekarang"
                        b "Ok"
                        scene door with fade
                        "..."
                        call screen gnav
                    else:
                        pass
                    scene mroom_qm23 with dissolve
                    b "Jadi apakah itu bagus?"
                    if mfuckedsober >=1:
                        scene mroom_qmf23 with dissolve
                        m "Yes"
                        scene mroom_qmf24 with dissolve
                        b "Huh"
                        m "Hapus celana pendek Anda"
                        scene mfjob02 with dissolve
                        m "Mhhm"
                        scene mfjob05 with dissolve
                        b "Ah"
                        scene mfjob06 with dissolve
                        "..."
                        scene mfjob40 with dissolve
                        "..."
                        scene mfjob80 with dissolve
                        m "..."
                        scene mroom_qmf25 with dissolve
                        "..."
                        m "Anda bisa pergi sekarang"
                        b "Ok"
                        scene door with fade
                        "..."
                        call screen gnav
                    else:
                        pass
                    scene mroom_qm23a with dissolve
                    b "Anda telah diam sebentar"
                    m "Ya ya sayang"
                    m "Anda bisa pergi sekarang"
                    b "Ok"
                    scene door with fade
                    "..."
                    call screen gnav
                "Melanjutkan":

                    if mrel >=200 and mcorr >=25:
                        m "Tunggu di sana sesuatu yang ingin saya tunjukkan"
                        scene mroom_qm27 with fade
                        b "{i} (apakah dia membuka pakaian tanpa meminta saya untuk berbalik? !!) {/i}"
                        scene mroom_qm28 with dissolve
                        m "Hmm"
                        m "Dimana saya meletakkannya?"
                        scene mroom_qm29 with dissolve
                        m "Ah itu di lemari pakaian, sekarang saya ingat"
                        scene mroom_qm30 with fade
                        b "{i} (saya tidak bisa mempercayai mata saya) {/i}"
                        scene mroom_qm32 with dissolve
                        b "{i} (apakah dia menguji saya, atau dia tidak benar -benar peduli) {/i}"
                        scene mroom_qm31 with dissolve
                        m "Jadi bagaimana menurut Anda?"
                        b "Cantik"
                        b "Itu gaun malam"
                        b "Apakah Anda berencana pergi makan malam"
                        m "Maybe soon"
                        b "Ah begitu"
                        b "Oke, saya akan pergi sekarang"
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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
