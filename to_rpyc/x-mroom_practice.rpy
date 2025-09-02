image mroomw:
    "mroomw00.jpg"
    pause 0.15
    "mroomw01.jpg"
    pause 0.1
    "mroomw02.jpg"
    pause 0.1
    "mroomw03.jpg"
    pause 0.1
    "mroomw04.jpg"
    pause 0.1
    "mroomw05.jpg"
    pause 0.1
    "mroomw06.jpg"
    pause 0.1
    "mroomw07.jpg"
    pause 0.1
    "mroomw08.jpg"
    pause 0.1
    "mroomw09.jpg"
    pause 0.1
    "mroomw10.jpg"
    pause 0.1
    "mroomw11.jpg"
    pause 0.1
    "mroomw12.jpg"
    pause 0.1
    "mroomw13.jpg"
    pause 0.1
    "mroomw14.jpg"
    pause 0.1
    "mroomw15.jpg"
    pause 0.1
    "mroomw16.jpg"
    pause 0.1
    "mroomw17.jpg"
    pause 0.1
    "mroomw18.jpg"
    pause 0.1
    "mroomw19.jpg"
    pause 0.1
    "mroomw20.jpg"
    pause 0.1
    "mroomw21.jpg"
    pause 0.1
    "mroomw22.jpg"
    pause 0.1
    "mroomw23.jpg"
    pause 0.1
    "mroomw24.jpg"
    pause 0.1
    "mroomw25.jpg"
    pause 0.1
    "mroomw26.jpg"
    pause 0.1
    "mroomw27.jpg"
    pause 0.1
    "mroomw28.jpg"
    pause 0.1
    "mroomw29.jpg"
    pause 0.1
    "mroomw30.jpg"
    pause 0.1
    "mroomw31.jpg"
    pause 0.1
    "mroomw32.jpg"
    pause 0.1
    "mroomw33.jpg"
    pause 0.1
    "mroomw34.jpg"
    pause 0.1
    "mroomw35.jpg"
    pause 0.1
    "mroomw36.jpg"
    pause 0.1
    "mroomw37.jpg"
    pause 0.1
    "mroomw38.jpg"
    pause 0.1




label mroom_practice:
    m "Wait outside"
    scene door with dissolve
    "..."
    m "Anda bisa masuk kembali"
    if mrel >= 100:
        scene m_room_p4 with fade
        m "Sit"
        m "Saya ingin menanyakan sesuatu"
        b "Ok"
        scene m_room_p5 with dissolve
        m "Ini tentang [sname]"
        b "Yes"
        m "Bagaimana studinya?"
        menu:
            "Tidak terlalu bagus, tapi saya memastikan dia mengalami kemajuan":
                show screen mrelup
                scene m_room_p7 with dissolve
                m "Terima kasih untuk itu"
                $ mrel += 1
                hide screen mrelup
                pass
            "Dia baik, tapi aku merawatnya":


                m "Ok bagus"
                "..."
                m "Terima kasih"
                m "Itu semua"
                m "Anda bisa pergi sekarang"
                scene m_room_p6 with dissolve
                b "Ok"
                pass

        scene door with fade
        b "{i} (...) {/i}"
        call screen gnav
    else:




        pass
    scene m_room_p with fade
    m "Sit"
    m "Saya ingin menanyakan sesuatu"
    b "Ok"
    scene m_room_p1 with dissolve
    m "Ini tentang [sname]"
    b "Yes"
    m "Bagaimana studinya?"
    menu:
        "Tidak terlalu bagus, tapi saya memastikan dia mengalami kemajuan":
            show screen mrelup
            scene m_room_p2 with dissolve
            m "Terima kasih untuk itu"
            $ mrel += 1
            hide screen mrelup
            pass
        "Dia baik, tapi aku merawatnya":


            m "Ok bagus"
            "..."
            m "Terima kasih"
            $ mrel += 1
            m "Itu semua"
            m "Anda bisa pergi sekarang"
            scene m_room_p3 with dissolve
            b "Ok"
            pass

    scene door with fade
    b "{i} (...) {/i}"
    call screen gnav




label mroom_practice_b:
    if mrel >=400:
        m "Ada sesuatu yang saya ingin Anda lihat"
        b "Ok"
        m "Tolong berpaling"
        b "Ok"
        scene m_room_p8 with dissolve
        "..."
        menu:
            "Mengintip":
                scene m_room_p24 with dissolve
                "..."
                scene m_room_p25 with dissolve
                b "Hah!"
                pass
            "Jangan":
                "..."
                m "Anda bisa berbalik"
                $ mrel += 1
                show screen mrelup
                scene m_room_p25 with dissolve
                b "Wow"
                hide screen mrelup
                pass

        m "Duduk di tempat tidur"
        scene m_room_p26 with dissolve
        "..."
        b "Hmm"
        "..."
        m "Apakah kamu menyukainya?"
        b "Yes"
        if mrel >=450:
            m "Hmm"
            b "Mengapa Anda tidak memakai barang -barang ini saat kami pergi ke pantai"
            m "Saya bisa [bname]"
            b "Mengapa?"
            m "Anda tidak akan mengerti mengapa"
            scene m_room_p27 with dissolve
            m "Anyway"
            m "Izinkan saya menunjukkan yang lain"
            scene m_room_p28 with dissolve
            "..."
            scene m_room_p29 with fade
            "..."
            scene m_room_p30 with dissolve
            m "Apakah kamu menyukainya?"
            b "..."
            b "Yes"
            m "{i}(Enough [mname]){/i}"
            m "Anda mungkin pergi sekarang"
            b "Oh Ok"
            scene door with fade
            b "{i} (...) {/i}"
            call screen gnav
        else:
            m "{i}(Enough [mname]){/i}"
            m "Anda mungkin pergi sekarang"
            b "Oh Ok"
            scene door with fade
            b "{i} (...) {/i}"
            call screen gnav


    elif mbikini ==2 and mrel >=110:
        m "Ada sesuatu yang saya ingin Anda lihat"
        b "Ok"
        m "Tolong berpaling"
        b "Ok"
        scene m_room_p8 with dissolve
        "..."
        menu:
            "Mengintip":
                scene m_room_p13 with dissolve
                "..."
                scene m_room_p14 with dissolve
                "..."
                pass
            "Jangan":

                "..."
                m "Anda bisa berbalik"
                $ mrel += 1
                show screen mrelup
                scene m_room_p14 with dissolve
                b "Wow"
                hide screen mrelup
                pass


        m "Terima kasih [bname]"
        b "Wow sangat bagus"
        m "Duduk di tempat tidur"
        scene mroomw with dissolve
        "..."
        b "Hmm"
        "..."
        scene m_room_p15 with dissolve
        b "Hahaha peragaan busana yang bagus"
        m "Terima kasih"
        scene m_room_p16 with dissolve
        m "{i}(Enough [mname]){/i}"
        m "Anda mungkin pergi sekarang"
        b "Oh Ok"
        scene door with fade
        b "{i} (...) {/i}"
        call screen gnav
    else:


        pass
    m "Saya telah membeli bikini baru"
    m "Saya ingin menunjukkannya kepada Anda"
    b "Yes sure"
    $ mpracticegift = 1
    m "Tolong berpaling"
    b "Ok"
    scene m_room_p8 with dissolve
    "..."
    menu:
        "Mengintip":
            scene m_room_p9 with dissolve
            "..."
            scene m_room_p10 with dissolve
            "..."
            pass
        "Jangan":

            "..."
            m "Anda bisa berbalik"
            $ mrel += 1
            show screen mrelup
            scene m_room_p10 with dissolve
            "..."
            hide screen mrelup
            pass

    m "Apakah kamu menyukainya?"
    b "Yes"
    b "Bagus"
    scene m_room_p11 with dissolve
    m "Terima kasih [bname]"
    m "Anda mungkin pergi sekarang"
    if mbikini ==1:
        $ mbikini = 2
        b "Errm saya punya sesuatu untuk Anda"
        m "Apa itu?"
        b "Bikini, di sini ambillah"
        scene m_room_p12 with dissolve
        m "Oh terima kasih"
        b "..."
        m "{i} (Praktek yang Cukup untuk Hari Ini) {/i}"
        m "Sampai jumpa"
        scene door with fade
        b "{i} (...) {/i}"
        call screen gnav


    elif mbag ==1:
        $ mbag = 2
        b "Errm saya punya sesuatu untuk Anda"
        m "Apa itu?"
        b "Tas, di sini ambil"
        scene m_room_p12 with dissolve
        $ mrel += 2
        show screen mrelup
        m "Oh terima kasih"
        hide screen mrelup
        b "..."
        m "{i} (Praktek yang Cukup untuk Hari Ini) {/i}"
        m "Sampai jumpa"
        scene door with fade
        b "{i} (Saya pikir dia sangat menyukai tas itu) {/i}"
        call screen gnav
    else:

        b "Ok"
        scene door with fade
        b "{i} (...) {/i}"
        call screen gnav



label mroom_practice1:
    m "Tunggu aku di pintu"
    scene door with dissolve
    "..."
    m "Datang"
    scene m_room_p17 with fade
    m "Terima kasih untuk ini"
    m "Itu indah dan nyaman"
    b "Senang Anda menyukainya"
    m "Kemarilah"
    scene m_room_p18 with dissolve
    m "..."
    scene m_room_p19 with dissolve
    b "..."
    m "Saya akan menunjukkan apa yang saya dapatkan"
    b "Ok"
    scene m_room_p20 with dissolve
    "..."
    if mrel>= 120:
        scene m_room_p21 with dissolve
        m "Aku akan kembali, tetap di sini"
        scene m_room_p22 with fade
        m "Bagaimana menurutmu?"
        b "Apa itu?"
        m "Bikini, tapi saya berencana untuk mengembalikannya"
        m "Beri aku pendapat jujurmu"
        menu:
            "Terlihat bagus":
                $ mrel += 2
                m "Terima kasih"
                m "Saya akan memutuskan apa yang akan saya lakukan dengan itu"
                pass
            "Bisakah Anda berbalik, biarkan saya melihatnya dari belakang":

                m "Sure"
                scene m_room_p23 with dissolve
                b "Hmm"
                b "Ya, itu terlihat bagus"
                scene m_room_p22 with dissolve
                m "Terima kasih"
                m "Saya akan memutuskan apa yang akan saya lakukan dengan itu"
                pass
    else:
        pass

    m "{i} (Praktek yang Cukup untuk Hari Ini) {/i}"
    m "Sampai jumpa"
    scene door with fade
    b "{i} (itu tidak layak untuk membeli nightie ini hanya untuk ini) {/i}"
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc