label pdinnerm_relax:
    scene pdinner_mr with fade
    b "{i} (aha!) {/i}"
    b "{i} (dia memakai ini!) {/i}"
    scene pdinner_mr1 with dissolve
    b "Apakah Anda membutuhkan bantuan saya?"
    m "Yes please"
    b "Apa yang Anda butuhkan?"
    m "Bisakah Anda mencuci piring?"
    menu:
        "Tentu ... tapi ... bisakah saya meminta imbalan sesuatu?":
            scene pdinner_mr2 with dissolve
            m "Apa yang kamu inginkan?"
            menu:
                "Tidak ada yang saya ubah pikiran":
                    pass
                "Bisakah Anda memakai gaun tidur?" if mnightie == 2:
                    b "{i} (sialan, aku tidak bisa mengatakan ini langsung) {/i}"
                    b "Apakah kamu suka nightie?"
                    m "Ya terima kasih, itu bagus"
                    b "Tapi aku tidak melihatmu memakainya?"
                    m "Saya tidak terbiasa memakai bikini seperti itu"
                    m "Beri aku waktu, aku akan melakukannya suatu hari nanti"
                    b "Jadi begitu"
                    pass

            scene pdinner_mr3 with dissolve
            "..."
            scene pdinner_mr2 with fade
            b "Done"
            b "Aku akan pergi sekarang"
            show screen mrelup
            $ mrel += 1
            m "Terima kasih [bname]"
            m "Jangan terlambat untuk makan malam"
            hide screen mrelup
            scene hall_n with fade
            "..."
            call screen gnav
        "Tentu":

            scene pdinner_mr3 with dissolve
            "..."
            scene pdinner_mr2 with fade
            b "Done"
            b "Aku akan pergi sekarang"
            if msconvince ==3:
                m "Jadi bagaimana [sname]?"
                m "Apakah ada kemajuan dengan studinya"
                menu:
                    "Ya":
                        $ msconvince = 0
                        m "Oke, bagus"
                        pass
                    "Tidak, tetap sama":
                        m "Ok saya lihat"
                        $ msconvince = 2
                        pass
            else:

                pass
            show screen mrelup
            $ mrel += 1
            m "Terima kasih [bname]"
            hide screen mrelup
            scene hall_n with fade
            "..."
            call screen gnav


        "Tentu ... tapi ... ada sesuatu yang ingin saya katakan" if msconvince == 1:
            scene pdinner_mr3 with dissolve
            "..."
            scene pdinner_mr2 with dissolve
            b "Done"
            m "Apa yang Anda ingin katakan padaku"
            b "Ini tentang [sname] Studi"
            m "Apa yang salah?"
            b "Dia masih berjuang"
            b "Dia menghabiskan banyak waktu di TV"
            b "Dia harus mendedikasikan lebih banyak waktu untuk kursusnya"
            m "Begitu, saya akan berbicara dengannya"
            b "Besar"
            show screen mrelup
            $ msconvince = 2
            $ mrel += 2
            m "Terima kasih [bname]"
            hide screen mrelup
            b "{i} (semoga menyingkirkan [sname]) {/i}"
            b "{i} (dia tidak akan mengganggu kita pada Sabtu malam) {/i}"
            scene hall_n with fade
            "..."
            call screen gnav



label pdinnerm_b:
    scene pdinner_m with fade
    b "{i} (aha!) {/i}"
    scene pdinner_m1 with dissolve
    b "Apakah Anda membutuhkan bantuan saya?"
    m "Yes please"
    b "Apa yang kamu butuhkan?"
    m "Bisakah Anda mencuci piring?"
    b "Sure"
    scene pdinner_hr with dissolve
    b "{i} (hanya jika idiot ini tidak ada di sini) {/i}"
    scene pdinner_hrb with dissolve
    b "Pfff"
    scene pdinner_hr1 with dissolve
    b "Done"
    b "Aku akan pergi sekarang"
    show screen mrelup
    $ mrel += 1
    m "Terima kasih [bname]"
    hide screen mrelup
    scene hall_n with fade
    "..."
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
