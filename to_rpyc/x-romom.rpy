label romom1:
    scene romom1 with fade
    b "Mungkin jika saya cum akan pergi"
    rm "Apa yang terjadi!"
    scene romom2 with dissolve
    b "Huh"
    rm "Hmmm apa yang kita miliki di sini?"
    b "Err"
    scene romom3 with hpunch
    b "Ah"
    scene row_visit59b with fade
    rm "Ya jilat aku bagus"
    scene row_visit61b with dissolve
    rm "Hmm"
    scene row_visit62b with dissolve
    rm "..."
    scene row_visit63b with dissolve
    rm "Yes"
    scene row_visit64b with dissolve
    rm "Ya, jilat"
    scene row_visit67b with dissolve
    b "Ahh!"
    scene row_visit68b with dissolve
    "..."
    scene row_visit69b with dissolve
    rm "{i} (fuck it, dia rock keras) {/i}"
    rm "{i} (dan sangat besar, ini harus masuk ke pantat saya) {/i}"
    rm "{i} (Saya harus mengatur catatan baru) {/i}"
    scene romom4 with fade
    rm "Ahhhh"
    rm "{i} (Saya harap dia segera cumming) {/i}"
    scene row_visit70b with fade
    "..."
    scene romom5 with dissolve
    rm "Anda tidak datang ey!"
    rm "Maaf sayang saya tidak bisa membantu Anda lagi"
    scene romom6 with fade
    rm "{i} (You Do It Girl) {/i}"
    scene romom7 with fade
    s "Apakah Anda pikir dia baik -baik saja?"
    a "..."
    s "Saya harap kami tidak mengacaukannya"
    scene romom8 with dissolve
    s "Ah akhirnya, apakah kamu baik -baik saja?"
    b "Same shit"
    a "Saya pikir kami bisa memperbaikinya untuk Anda"
    a "Benar [sname]?"
    if srel >= 300:
        s "Mungkin kita bisa"
        scene romom9 with fade
        s "Baringkan dan santai saja"
        s "Kami akan mengurus rasa sakit Anda"
        scene romom10 with dissolve
        s "Wow"
        scene romom11 with dissolve
        b "Ahh"
        b "{i} (bodoh [sname] Secara teknis adalah menjilati pantat ibu Rowena) {/i}"
        scene romom12 with dissolve
        "..."
        scene romom13 with dissolve
        a "Ahhh"
        scene romom14 with dissolve
        s "Ohhh"
        menu:
            "Persetan keduanya":
                scene beginrndf with dissolve
                b "..."
                scene rndf
                s "Ahh"
                "..."
                a "Mhhhm"
                "..."
                scene romom25 with fade
                s "Apakah Anda merasa lebih baik?"
                b "Yes"
                s "Let's go"
                jump broom_menu
            "Fuck [sname]":

                scene romom15 with dissolve
                s "Yeah"
                scene romom16 with dissolve
                s "Ahhh"
                b "Sorry [sname]"
                b "Tapi Anda bilang Anda akan membuat saya merasa lebih baik"
                scene romom17 with dissolve
                s "Ya Tuhan !!"
                scene romom18 with hpunch
                s "Ah shit"
                scene romom25 with fade
                s "Apakah Anda merasa lebih baik?"
                b "Yes"
                s "Let's go"
                jump broom_menu
            "Fuck Rowena":

                b "Continue Rowena"
                scene romom19 with dissolve
                a "Ahh"
                scene romom20 with dissolve
                "..."
                scene romom21 with dissolve
                a "..."
                scene romom22 with dissolve
                a "Tidak ada di sana [bname]"
                a "[sname] Tolong beri tahu dia"
                scene romom23 with dissolve
                a "Tolong [sname] Katakan padanya"
                a "Please"
                s "[bname] Cukup Anda akan membunuhnya"
                scene romom24 with dissolve
                s "Dia akan baik -baik saja"
                scene romom25 with fade
                s "Apakah Anda merasa lebih baik?"
                b "Yes"
                s "Let's go"
                jump broom_menu

    elif scorr >= 50:
        s "Mungkin kita bisa"
        scene romom9 with fade
        s "Baringkan dan santai saja"
        s "Kami akan mengurus rasa sakit Anda"
        scene romom10 with dissolve
        s "Wow"
        scene romom11 with dissolve
        b "Ahh"
        b "{i} (bodoh [sname] Secara teknis adalah menjilati pantat ibu Rowena) {/i}"
        scene romom12 with dissolve
        "..."
        scene romom13 with dissolve
        a "Ahhh"
        scene romom14 with dissolve
        s "Ohhh"
        menu:
            "Persetan keduanya":
                scene beginrndf with dissolve
                b "..."
                scene rndf
                s "Ahh"
                "..."
                a "Mhhhm"
                "..."
                scene romom25 with fade
                s "Apakah Anda merasa lebih baik?"
                b "Yes"
                s "Let's go"
                jump broom_menu
            "Fuck [sname]":


                scene romom15 with dissolve
                s "Yeah"
                scene romom16 with dissolve
                s "Ahhh"
                b "Sorry [sname]"
                b "Tapi Anda bilang Anda akan membuat saya merasa lebih baik"
                scene romom17 with dissolve
                s "Ya Tuhan !!"
                scene romom18 with hpunch
                s "Ah shit"
                scene romom25 with fade
                s "Apakah Anda merasa lebih baik?"
                b "Yes"
                s "Let's go"
                jump broom_menu
            "Fuck Rowena":

                b "Continue Rowena"
                scene romom19 with dissolve
                a "Ahh"
                scene romom20 with dissolve
                "..."
                scene romom21 with dissolve
                a "..."
                scene romom22 with dissolve
                a "Tidak ada di sana [bname]"
                a "[sname] Tolong beri tahu dia"
                scene romom23 with dissolve
                a "Tolong [sname] Katakan padanya"
                a "Please"
                s "[bname] Cukup Anda akan membunuhnya"
                scene romom24 with dissolve
                s "Dia akan baik -baik saja"
                scene romom25 with fade
                s "Apakah Anda merasa lebih baik?"
                b "Yes"
                s "Let's go"
                jump broom_menu
    else:
        s "Hmm tidak, aku akan membawanya pulang"
        scene phardon6 with fade
        b "Ahh"
        m "Huh"
        scene phardon7 with dissolve
        m "Apakah kamu baik -baik saja sayang?"
        b "Aku tidak tahu"
        m "Hal yang sama?"
        b "Ya saya pikir begitu"
        scene phardon8 with dissolve
        m "Oh"
        scene phardon9 with dissolve
        m "Kenakan kemeja dan biarkan pergi"
        b "Di mana?"
        m "Aku berkata pergi meletakkan bajumu"
        if mrel >=400:
            $ mfuckedsober = 1
            pass
        else:
            scene ohard with fade
            "Pastikan Anda memiliki 400 poin hubungan"
            m "{i} (i \ \ 've get it, i \' ll call elaine) {/i}"
            m "{i} (dia memahami dan akan membantu) {/i}"
            scene black
            "..."
            scene s_efuck2 with fade
            e "Apa yang salah [mname] Anda membuat saya takut"
            m "Saya ingin Anda bercinta [bname]"
            scene ohard1 with dissolve
            e "Apa?"
            m "Maaf karena ini langsung"
            m "Tapi ada alasannya, dan saya tidak ingin kehilangan waktu"
            m "Dia memiliki masalah medis"
            m "Priapisme atau semacamnya"
            m "Ereksi tanpa henti"
            m "Dokter merekomendasikan ini, atau pil"
            m "Saya tidak ingin memberinya pil"
            m "Jadi saya pikir Anda satu -satunya pilihan yang saya dapatkan"
            scene ohard2 with dissolve
            e "Oke, tapi kamu akan membayar saya kan?"
            e "kamu tahu itu"
            m "Of course"
            scene ohard3 with dissolve
            m "ELAINE! Kondom ok?"
            m "Atau aku akan membunuhmu"
            e "Sure"
            m "Saya ingin melihat kondom yang digunakan"
            e "OK"
            m "Semoga beruntung"
            e "Kepadanya, bukan aku"
            m "Yeah"
            scene ohard4 with dissolve
            m "{i} (kami akan melihat) {/i}"
            scene s_efuck6 with fade
            e "Hi [bname]"
            b "Ahhh hi"
            e "Saya di sini untuk ..."
            b "Aku tahu"
            e "Kamu tahu?"
            b "Ya [mname] memberitahuku"
            e "Baiklah, mari kita lakukan ini"
            scene ohard5 with dissolve
            e "Huh"
            scene ehrd
            e "Ahhh"
            b "Grr"
            "..."
            e "Ah shit"
            scene ohard6 with dissolve
            e "Please"
            b "Bangun"
            scene estd
            e "Ahhh"
            "..."
            e "Mmmm"
            "..."
            b "..."
            scene ohard7 with hpunch
            b "Ahhhhhhh"
            scene ohard8 with fade
            e "Ahh"
            e "Bagus yang saya ingat, saya perlu mendapatkan kondom dari tas saya"
            scene ohard9 with fade
            e "Ini kondom Anda"
            m "Dan di sini uang Anda"
            scene ohard10 with fade
            m "Semuanya akan baik -baik saja sayang, cobalah tidur sekarang"
            b "..."
            jump newdays


        scene phardon13 with fade
        b "Ahhh"
        b "Apa yang kita lakukan di sini?"
        m "Duduk dan rileks, aku akan memberitahumu"
        m "Hapus celana pendek Anda"
        scene phardon14 with dissolve
        m "Tolong ambilkan saya dua minuman terkuat Anda"
        m "Saya ingin terbuang dengan cepat"
        scene phardon15 with fade
        b "Ahhh"
        m "Drink"
        b "Mengapa Minum Sekarang?"
        b "Saya tidak dalam mood"
        m "Minum itu akan membuat Anda merasa lebih baik"
        m "Dan berbaring"
        m "Dengarkan Sayang ..."
        m "Apa yang akan saya lakukan selanjutnya ..."
        m "Adalah memastikan Anda baik -baik saja"
        m "Dan hanya itu"
        m "Saya harap Anda mengerti"
        scene phardon16 with dissolve
        b "Uh"
        scene phardon17 with dissolve
        m "..."
        m "{i} (itu sulit seperti batu) {/i}"
        m "Bagaimana jika saya melakukan ini"
        scene phardon18 with dissolve
        b "Ahh"
        m "{i} (ini bekerja \ 'T) {/i}"
        scene phardon18a with dissolve
        m "[bname]"
        m "Duduklah di sisi tempat tidur"
        scene phardon19a with fade
        m "..."
        scene mbj
        "..."
        b "Ahh"
        "..."
        m "..."
        b "Bagus tapi tidak akan bekerja"
        scene mbj00 with dissolve
        m "Biarkan saya mencoba lagi lebih lambat"
        scene mbjsl
        "..."
        m "Mhhm"
        b "Persetan itu menyakitkan"
        scene phardon19 with dissolve
        "..."
        scene phardon20 with dissolve
        m "..."
        scene phardon21 with dissolve
        b "..."
        b "Tunggu..."
        scene mblow
        m "..."
        b "Ahh"
        m "..."
        b "Argh"
        scene mblow00 with dissolve
        b "Tidak akan berhasil"
        m "Ok mari kita coba sesuatu yang lain"
        scene beginhos0 with fade
        m "Di lantai dan lambat tolong"
        b "Yes"
        m "Anda \ 'kembali mabuk [bname], tolong jangan gila"
        scene beginhos with dissolve
        m "..."
        scene hos
        "..."
        m "Ahhh"
        b "Grrr"
        m "Slowly"
        m "Ahhh"
        "..."
        scene endhos with dissolve
        m "Tuhan!"
        m "Let's relax"
        scene endhos1 with fade
        b "It's painful"
        m "Saya tidak tahu apa yang harus dilakukan madu"
        m "{i} (mungkin anal akan membantu?) {/i}"
        m "{i} (karena lebih ketat) {/i}"
        m "{i} (tapi saya akan dihancurkan) {/i}"
        b "Ah fuck"
        m "Honey apa?"
        b "Saya bisa merasakan denyut nadi saya di penis saya"
        m "{i} (Saya kira saya tidak punya pilihan) {/i}"
        scene phardon23 with fade
        m "Ayo sayang"
        scene anam
        "..."
        m "Oh"
        m "[bname]!"
        b "Ahh"
        m "Apakah kamu dekat?"
        play sound "sounds/jenmoan.wav"
        m "Persetan dengan pantatku [bname]"
        stop sound
        scene phardon24 with dissolve
        m "Persetan dengan lebih keras"
        scene anam
        m "Yes"
        m "Yes"
        "..."
        m "Yes"
        scene anac
        b "Ahhh"
        b "Ahh"
        "..."
        m "..."
        scene phardon26 with fade
        m "Saya akan mencuci dan kami pulang"
        scene phardon25 with fade
        m "Mmm"
        scene ohard10 with fade
        m "Semuanya akan baik -baik saja sayang, cobalah tidur sekarang"
        b "..."
        jump newdays





label romom:
    scene romom1 with fade
    b "Mungkin jika saya cum akan pergi"
    rm "Apa yang terjadi!"
    scene romom2 with dissolve
    b "Huh"
    rm "Hmmm apa yang kita miliki di sini?"
    b "Err"
    scene romom3 with hpunch
    b "Ah"
    scene row_visit59b with fade
    rm "Ya jilat aku bagus"
    scene row_visit61b with dissolve
    rm "Hmm"
    scene row_visit62b with dissolve
    rm "..."
    scene row_visit63b with dissolve
    rm "Yes"
    scene row_visit64b with dissolve
    rm "Ya, jilat"
    scene row_visit67b with dissolve
    b "Ahh!"
    scene row_visit68b with dissolve
    "..."
    scene row_visit69b with dissolve
    rm "{i} (fuck it, dia rock keras) {/i}"
    rm "{i} (dan sangat besar, ini harus masuk ke pantat saya) {/i}"
    rm "{i} (Saya harus mengatur catatan baru) {/i}"
    scene romom4 with fade
    rm "Ahhhh"
    rm "{i} (Saya harap dia segera cumming) {/i}"
    scene row_visit70b with fade
    "..."
    scene romom5 with dissolve
    rm "Anda tidak datang ey!"
    rm "Maaf sayang saya tidak bisa membantu Anda lagi"
    scene romom6 with fade
    rm "{i} (You Do It Girl) {/i}"
    scene romom7 with fade
    s "Apakah Anda pikir dia baik -baik saja?"
    a "..."
    s "Saya harap kami tidak mengacaukannya"
    scene romom8 with dissolve
    s "Ah akhirnya, apakah kamu baik -baik saja?"
    b "Same shit"
    a "Saya pikir kami bisa memperbaikinya untuk Anda"
    a "Benar [sname]?"
    if srel >= 300:
        s "Mungkin kita bisa"
        scene romom9 with fade
        s "Baringkan dan santai saja"
        s "Kami akan mengurus rasa sakit Anda"
        scene romom10 with dissolve
        s "Wow"
        scene romom11 with dissolve
        b "Ahh"
        b "{i} (bodoh [sname] Secara teknis adalah menjilati pantat ibu Rowena) {/i}"
        scene romom12 with dissolve
        "..."
        scene romom13 with dissolve
        a "Ahhh"
        scene romom14 with dissolve
        s "Ohhh"
        menu:
            "Persetan keduanya":
                scene beginrndf with dissolve
                b "..."
                scene rndf
                s "Ahh"
                "..."
                a "Mhhhm"
                "..."
                scene romom25 with fade
                s "Apakah Anda merasa lebih baik?"
                b "Yes"
                s "Let's go"
                jump broom_menu
            "Fuck [sname]":

                scene romom15 with dissolve
                s "Yeah"
                scene romom16 with dissolve
                s "Ahhh"
                b "Sorry [sname]"
                b "Tapi Anda bilang Anda akan membuat saya merasa lebih baik"
                scene romom17 with dissolve
                s "Ya Tuhan !!"
                scene romom18 with hpunch
                s "Ah shit"
                scene romom25 with fade
                s "Apakah Anda merasa lebih baik?"
                b "Yes"
                s "Let's go"
                jump broom_menu
            "Fuck Rowena":

                b "Continue Rowena"
                scene romom19 with dissolve
                a "Ahh"
                scene romom20 with dissolve
                "..."
                scene romom21 with dissolve
                a "..."
                scene romom22 with dissolve
                a "Tidak ada di sana [bname]"
                a "[sname] Tolong beri tahu dia"
                scene romom23 with dissolve
                a "Tolong [sname] Katakan padanya"
                a "Please"
                s "[bname] Cukup Anda akan membunuhnya"
                scene romom24 with dissolve
                s "Dia akan baik -baik saja"
                scene romom25 with fade
                s "Apakah Anda merasa lebih baik?"
                b "Yes"
                s "Let's go"
                jump broom_menu

    elif scorr >= 50:
        s "Mungkin kita bisa"
        scene romom9 with fade
        s "Baringkan dan santai saja"
        s "Kami akan mengurus rasa sakit Anda"
        scene romom10 with dissolve
        s "Wow"
        scene romom11 with dissolve
        b "Ahh"
        b "{i} (bodoh [sname] Secara teknis adalah menjilati pantat ibu Rowena) {/i}"
        scene romom12 with dissolve
        "..."
        scene romom13 with dissolve
        a "Ahhh"
        scene romom14 with dissolve
        s "Ohhh"
        menu:
            "Fuck [sname]":
                scene romom15 with dissolve
                s "Yeah"
                scene romom16 with dissolve
                s "Ahhh"
                b "Sorry [sname]"
                b "Tapi Anda bilang Anda akan membuat saya merasa lebih baik"
                scene romom17 with dissolve
                s "Ya Tuhan !!"
                scene romom18 with hpunch
                s "Ah shit"
                scene romom25 with fade
                s "Apakah Anda merasa lebih baik?"
                b "Yes"
                s "Let's go"
                jump broom_menu
            "Fuck Rowena":

                b "Continue Rowena"
                scene romom19 with dissolve
                a "Ahh"
                scene romom20 with dissolve
                "..."
                scene romom21 with dissolve
                a "..."
                scene romom22 with dissolve
                a "Tidak ada di sana [bname]"
                a "[sname] Tolong beri tahu dia"
                scene romom23 with dissolve
                a "Tolong [sname] Katakan padanya"
                a "Please"
                s "[bname] Cukup Anda akan membunuhnya"
                scene romom24 with dissolve
                s "Dia akan baik -baik saja"
                scene romom25 with fade
                s "Apakah Anda merasa lebih baik?"
                b "Yes"
                s "Let's go"
                jump broom_menu
    else:



        s "Hmm tidak, aku akan membawanya pulang"
        scene phardon6 with fade
        b "Ahh"
        m "Huh"
        scene phardon7 with dissolve
        m "Apakah kamu baik -baik saja sayang?"
        b "Aku tidak tahu"
        m "Apa yang salah, katakan padaku"
        b "Kami berada di kolam renang dan tiba -tiba ini terjadi"
        m "Apa yang Anda maksud dengan ini?"
        scene phardon8 with dissolve
        m "Oh"
        scene phardon9 with dissolve
        m "Mungkin sengatan lebah?"
        b "Tidak, tidak ada yang terjadi"
        m "Kenakan kemeja dan biarkan pergi"
        b "Di mana?"
        m "Aku berkata pergi meletakkan bajumu"
        scene phardon10 with fade
        "... Ini Priapism"
        "Ereksi berkepanjangan yang tidak disebabkan oleh gairah seksual"
        scene phardon11 with dissolve
        "Saya tidak bisa memastikan apa yang menyebabkannya"
        "Tapi kemungkinan besar dia minum pil Ed"
        "Hah"
        m "Saya tidak berpikir dia tahu tentang ini"
        m "Tapi apa solusinya"
        "Kami memiliki dua solusi di sini"
        "Entah saya memberinya pil, yang tidak saya rekomendasikan"
        "Karena itu akan memengaruhi ereksi normalnya"
        "Atau kami mencoba untuk memenuhi kebutuhannya"
        m "EMM Bisakah Anda melakukannya di klinik Anda?"
        "Saya minta maaf itu tidak mungkin"
        m "Apa yang Anda rekomendasikan"
        "Temukan dia seorang gadis panggilan"
        m "Tidak akan terjadi, saya peduli dengan kesehatannya"
        "Sayang, itulah mengapa ada kondom"
        scene phardon12 with dissolve
        "..."
        scene phardon11 with dissolve
        "Selain itu, dia tidak perlu menembusnya"
        "Hanya handjob yang akan dilakukan"
        "Atau melihat ereksinya, dia mungkin membutuhkan dua ejakulasi"
        scene phardon12 with dissolve
        m "Ok, saya akan menemukan satu"
        if mrel >=400:
            $ mfuckedsober = 1
            pass
        else:
            scene ohard with fade
            m "{i} (i \ \ 've get it, i \' ll call elaine) {/i}"
            m "{i} (dia memahami dan akan membantu) {/i}"
            scene black
            "..."
            scene s_efuck2 with fade
            e "Apa yang salah [mname] Anda membuat saya takut"
            m "Saya ingin Anda bercinta [bname]"
            scene ohard1 with dissolve
            e "Apa?"
            m "Maaf karena ini langsung"
            m "Tapi ada alasannya, dan saya tidak ingin kehilangan waktu"
            m "Dia memiliki masalah medis"
            m "Priapisme atau semacamnya"
            m "Ereksi tanpa henti"
            m "Dokter merekomendasikan ini, atau pil"
            m "Saya tidak ingin memberinya pil"
            m "Jadi saya pikir Anda satu -satunya pilihan yang saya dapatkan"
            scene ohard2 with dissolve
            e "Oke, tapi kamu akan membayar saya kan?"
            e "kamu tahu itu"
            m "Of course"
            scene ohard3 with dissolve
            m "ELAINE! Kondom ok?"
            m "Atau aku akan membunuhmu"
            e "Sure"
            m "Saya ingin melihat kondom yang digunakan"
            e "OK"
            m "Semoga beruntung"
            e "Kepadanya, bukan aku"
            m "Yeah"
            scene ohard4 with dissolve
            m "{i} (kami akan melihat) {/i}"
            scene s_efuck6 with fade
            e "Hi [bname]"
            b "Ahhh hi"
            e "Saya di sini untuk ..."
            b "Aku tahu"
            e "Kamu tahu?"
            b "Ya [mname] memberitahuku"
            e "Baiklah, mari kita lakukan ini"
            scene ohard5 with dissolve
            e "Huh"
            scene ehrd
            e "Ahhh"
            b "Grr"
            "..."
            e "Ah shit"
            scene ohard6 with dissolve
            e "Please"
            b "Bangun"
            scene estd
            e "Ahhh"
            "..."
            e "Mmmm"
            "..."
            b "..."
            scene ohard7 with hpunch
            b "Ahhhhhhh"
            scene ohard8 with fade
            e "Ahh"
            e "Bagus yang saya ingat, saya perlu mendapatkan kondom dari tas saya"
            scene ohard9 with fade
            e "Ini kondom Anda"
            m "Dan di sini uang Anda"
            scene ohard10 with fade
            m "Semuanya akan baik -baik saja sayang, cobalah tidur sekarang"
            b "..."
            jump newdays


        scene phardon13 with fade
        b "Ahhh"
        b "Apa yang kita lakukan di sini?"
        m "Duduk dan rileks, aku akan memberitahumu"
        m "Hapus celana pendek Anda"
        scene phardon14 with dissolve
        m "Tolong ambilkan saya dua minuman terkuat Anda"
        m "Saya ingin terbuang dengan cepat"
        scene phardon15 with fade
        b "Ahhh"
        m "Drink"
        b "Mengapa Minum Sekarang?"
        b "Saya tidak dalam mood"
        m "Minum itu akan membuat Anda merasa lebih baik"
        m "Dan berbaring"
        m "Dengarkan Sayang ..."
        m "Apa yang akan saya lakukan selanjutnya ..."
        m "Adalah memastikan Anda baik -baik saja"
        m "Dan hanya itu"
        m "Saya harap Anda mengerti"
        scene phardon16 with dissolve
        b "Uh"
        scene phardon17 with dissolve
        m "..."
        m "{i} (itu sulit seperti batu) {/i}"
        m "Bagaimana jika saya melakukan ini"
        scene phardon18 with dissolve
        b "Ahh"
        m "{i} (ini bekerja \ 'T) {/i}"
        scene phardon18a with dissolve
        m "[bname]"
        m "Duduklah di sisi tempat tidur"
        scene phardon19a with fade
        m "..."
        scene mbj
        "..."
        b "Ahh"
        "..."
        m "..."
        b "Bagus tapi tidak akan bekerja"
        scene mbj00 with dissolve
        m "Biarkan saya mencoba lagi lebih lambat"
        scene mbjsl
        "..."
        m "Mhhm"
        b "Persetan itu menyakitkan"
        scene phardon19 with dissolve
        "..."
        scene phardon20 with dissolve
        m "..."
        scene phardon21 with dissolve
        b "..."
        b "Tunggu..."
        scene mblow
        m "..."
        b "Ahh"
        m "..."
        b "Argh"
        scene mblow00 with dissolve
        b "Tidak akan berhasil"
        m "Ok mari kita coba sesuatu yang lain"
        scene beginhos0 with fade
        m "Di lantai dan lambat tolong"
        b "Yes"
        m "Anda \ 'kembali mabuk [bname], tolong jangan gila"
        scene beginhos with dissolve
        m "..."
        scene hos
        "..."
        m "Ahhh"
        b "Grrr"
        m "Slowly"
        m "Ahhh"
        "..."
        scene endhos with dissolve
        m "Tuhan!"
        m "Let's relax"
        scene endhos1 with fade
        b "It's painful"
        m "Saya tidak tahu apa yang harus dilakukan madu"
        m "{i} (mungkin anal akan membantu?) {/i}"
        m "{i} (karena lebih ketat) {/i}"
        m "{i} (tapi saya akan dihancurkan) {/i}"
        b "Ah fuck"
        m "Honey apa?"
        b "Saya bisa merasakan denyut nadi saya di penis saya"
        m "{i} (Saya kira saya tidak punya pilihan) {/i}"
        scene phardon23 with fade
        m "Ayo sayang"
        scene anam
        "..."
        m "Oh"
        m "[bname]!"
        b "Ahh"
        m "Apakah kamu dekat?"
        play sound "sounds/jenmoan.wav"
        m "Persetan dengan pantatku [bname]"
        stop sound
        scene phardon24 with dissolve
        m "Persetan dengan lebih keras"
        scene anam
        m "Yes"
        m "Yes"
        "..."
        m "Yes"
        scene anac
        b "Ahhh"
        b "Ahh"
        "..."
        m "..."
        scene phardon26 with fade
        m "Saya akan mencuci dan kami pulang"
        scene phardon25 with fade
        m "Mmm"
        scene ohard10 with fade
        m "Semuanya akan baik -baik saja sayang, cobalah tidur sekarang"
        b "..."
        jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
