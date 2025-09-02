label hall_evening:
    if worktalk ==1:
        $ worktalk = 2
        scene hevening with fade
        "..."
        scene hevening1 with dissolve
        m "Hi [bname]"
        scene hevening2 with dissolve
        b "Hi there"
        b "Jadi bagaimana kabarmu?"
        s "Ya! Bagaimana?"
        scene hevening3 with dissolve
        m "Saya sudah mendapatkan pekerjaan"
        m "Saya akan mulai besok"
        s "Bagus!!"
        b "Bagaimana dengan jam kerja Anda?"
        scene hevening2 with dissolve
        m "Ini akan dari 10 hingga 18 hari, kecuali hari Minggu"
        b "Ok"
        m "Sekarang izinkan saya berubah dan saya akan mulai menyiapkan makan malam"
        s "Ok"
        scene black
        "..."
        scene mdan29 with fade
        ml "Bagaimana harimu sayang?"
        dn "Tidak buruk, bisnis sedang mengambil"
        dn "Bagaimana dengan milikmu?"
        ml "Saya menyewa pelayan baru untuk kedai kopi hari ini"
        dn "Bagus"
        dn "Tapi saya pikir Anda tidak membutuhkannya"
        ml "Saya tidak tahu, dia datang, dan menceritakan kisahnya"
        ml "Saya merasa harus melakukannya"
        ml "Mari kita lihat..."
        ml "Aku akan menyiapkan makan malam, ayo makan di teras"
        scene mdan30 with fade
        dn "Itu adalah makanan yang enak"
        dn "Thanks"
        ml "... Anda tahu Daniel"
        dn "Apa?"
        ml "Saya sangat bangga dengan siapa Anda menjadi"
        dn "Thanks"
        scene mdan31 with dissolve
        ml "Selamat malam"
        scene black
        "..."
        scene hall_n with fade
        "..."
        call screen gnav
    else:



        if startnework ==1:
            if bnamefixcheryl ==5 and bgmt ==0:
                $ bgmt = 1
                scene bgmt1 with fade
                $ persistent.unlock_43 = True
                "SEMENTARA ITU"
                "Uh hai"
                m "Yes Michael"
                "Kamu tidak apa apa?"
                m "Ya kenapa kamu bertanya?"
                "Saya tidak tahu tetapi hari ini Anda bukan diri Anda sendiri"
                m "Terima kasih telah bertanya tapi semuanya baik -baik saja"
                "Bisakah aku membawamu pulang"
                m "Tidak apa -apa saya akan mendapatkan taksi seperti biasa"
                "Tidak perlu, saya bisa membawamu itu dalam perjalanan"
                scene bgmt2 with dissolve
                m "Hah!"
                m "Apakah Anda tahu di mana saya tinggal?"
                scene bgmt3 with dissolve
                "Hehe tidak, tapi kota itu kecil"
                "Pasti Anda tidak akan tinggal di daerah terpencil"
                scene bgmt4 with fade
                m "Terima kasih Michael"
                pass
            else:
                pass
            jump newwork_return
        else:

            pass
        scene hevening with fade
        "..."
        scene hevening4 with dissolve
        m "Hi [bname]"
        b "Apa kabar hari ini"
        scene hevening5 with dissolve
        m "Melelahkan seperti biasa"
        m "Saya akan mulai menyiapkan makan malam"
        b "Ok"
        if e_showsupagain ==1:
            $ e_showsupagain = 2
            play sound "sounds/doorbell.wav"
            m "Hmm siapa itu saat ini?"
            stop sound
            scene hevening6 with fade
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
            if bexercise <= 100:
                b "Sial ya!"
                $ cselaine0 = 9
                b "Aku akan segera meneleponmu"
                scene hall_m_n32 with dissolve
                e "Terima kasih"
                scene hall_n with fade
                "..."
                call screen gnav
            else:

                b "Sial ya!"
                $ cselaine0 = 9
                b "Aku akan segera meneleponmu"
                scene hall_m_n32 with dissolve
                e "Terima kasih"
                scene hall_n with fade
                "..."
                call screen gnav
        else:

            if bworkstarted == 1 and cvisit ==0:
                $ cvisit = 1
                "SEMENTARA ITU"
                scene cvisith with fade
                "..."
                scene cvisith1 with dissolve
                ml "Bagaimana Nyonya Layanan?"
                ml "Saya sudah diberitahu bahwa Anda memiliki masalah dengan susu kedelai kami"
                c "Ya rasanya"
                ml "Dapatkah saya menawarkan Anda pengganti"
                ml "Apakah Anda memiliki semacam alergi atau semacamnya?"
                c "Tidak sama sekali, saya hanya suka rasa susu kedelai"
                ml "Nah, kami memiliki susu sapi segar"
                c "Oke, saya akan melakukannya"
                scene cvisith2 with dissolve
                ml "Saya yakin Anda akan menyukainya"
                "..."
                scene black
                "KEMBALI"
                scene hall_n with fade
                "..."
                call screen gnav
            else:
                pass
            scene hall_n with fade
            "..."
            call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc