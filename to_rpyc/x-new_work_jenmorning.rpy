label new_work_jenmorning:
    if melsw >= 9 and msexwork <=3:
        scene nwork_going with fade
        b "Selamat pagi"
        $ msexwork += 1
        m "Pagi"
        b "Akan bekerja?"
        scene nwork_goingdr with dissolve
        m "Jangan mengingatkan saya"
        s "Selamat pagi"
        m "Saya kembali terlambat hari ini"
        scene nwork_goingdr1 with dissolve
        s "Apa yang salah dengannya?"
        b "Saya tidak tahu, tetapi dia memiliki masalah di tempat kerja"
        s "Setidaknya dia bisa kembali pagi saya"
        b "Tidak apa -apa, setidaknya kita punya hari untuk diri kita sendiri"
        if snupset >= 2:
            s "Ya, tapi saya harus pergi bertemu teman -teman saya"
            b "Teman-teman? Siapa Rowena?"
            $ sgoestost = 1
            s "Tidak, seorang teman yang datang ke kota"
            b "Hmm"
        else:
            s "Yes"
            b "Ok"
            pass
        b "Anyway"
        b "Sampai jumpa"
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav




    elif mrel >=150 and day == 2:
        scene nwork_goingna with fade
        b "{i} (dimana dia?) {/i}"
        menu:
            "Pergi mencari dia":
                scene nwork_going5 with fade
                b "{i}(Wow){/i}"
                scene nwork_going6 with dissolve
                m "Selamat pagi [bname]"
                b "..."
                b "Selamat pagi"
                scene nwork_going7 with dissolve
                m "Maaf saya sangat terlambat untuk bekerja"
                scene nwork_going8 with dissolve
                b "Bisakah saya membantu Anda dengan sesuatu?"
                scene nwork_going9 with dissolve
                m "Ya, beri saya bra saya dari laci di sana"
                scene nwork_going10 with dissolve
                b "Sure"
                menu:
                    "Beri dia bra yang salah":
                        scene nwork_going13 with dissolve
                        m "Ini bukan!"
                        m "The other"
                        b "Ok sorry"
                        pass
                    "Beri bra yang tepat":

                        show screen mrelup
                        $ mrel += 2
                        b "Here"
                        hide screen mrelup
                        pass

                scene nwork_going11 with fade
                m "Terima kasih"
                b "Sampai jumpa di malam hari"
                m "Yes"
                scene hall_d with fade
                b "{i} (...) {/i}"
                call screen gnav
            "Tidak perlu":



                scene black
                "..."
                scene hall_d with fade
                b "{i} (...) {/i}"
                call screen gnav

    elif mrel >=150 and day == 5:
        scene nwork_goingna with fade
        b "{i} (dimana dia?) {/i}"
        menu:
            "Pergi mencari dia":
                scene nwork_going5 with fade
                b "{i}(Wow){/i}"
                scene nwork_going6 with dissolve
                m "Selamat pagi [bname]"
                b "..."
                b "Selamat pagi"
                scene nwork_going7 with dissolve
                m "Maaf saya sangat terlambat untuk bekerja"
                scene nwork_going8 with dissolve
                b "Bisakah saya membantu Anda dengan sesuatu?"
                scene nwork_going9 with dissolve
                m "Ya, beri saya bra saya dari laci di sana"
                scene nwork_going10 with dissolve
                b "Sure"
                menu:
                    "Beri dia bra yang salah":
                        scene nwork_going14 with dissolve
                        m "Ini bukan!!"
                        m "The other"
                        b "{i} (hehe, tapi mengapa dia memilikinya) {/i}"
                        b "Ok sorry"
                        pass
                    "Beri bra yang tepat":

                        show screen mrelup
                        $ mrel += 2
                        b "Here"
                        hide screen mrelup
                        scene nwork_going12k with fade
                        m "Terima kasih"
                        b "Sampai jumpa di malam hari"
                        m "Yes"
                        scene hall_d with fade
                        b "{i} (...) {/i}"
                        call screen gnav

                scene nwork_going12 with fade
                m "Terima kasih"
                b "Sampai jumpa di malam hari"
                m "Yes"
                scene hall_d with fade
                b "{i} (...) {/i}"
                call screen gnav
            "Tidak perlu":



                scene black
                "..."
                scene hall_d with fade
                b "{i} (...) {/i}"
                call screen gnav
    else:






        pass
    scene nwork_going with fade
    b "Selamat pagi"
    m "Selamat pagi [bname]"
    menu:
        "Akan bekerja?":
            m "Yes"
            b "Hmmm"
            if startnework ==0:
                scene nwork_going1 with dissolve
                b "Hmm ..."
                b "Pakaian baru?"
                $ startnework = 1
                m "Ya, ini hari pertama saya dan saya ingin membuat kesan pertama yang baik"
                b "Itulah semangatnya"
                b "Apakah lebih baik dari sebelumnya?"
                m "Ya direkomendasikan oleh elaine"
                b "Jadi begitu"
                b "Dan apa jadwal Anda?"
                m "Itu sama 9 hingga 18"
                b "All right"
                $ startnework = 1
                b "Sampai jumpa di malam hari"
                pass
            else:
                b "Bagus"
                b "Sampai jumpa lagi"
                pass

            m "Sampai jumpa"
            if startnework ==1 and work_intro == 0:
                $ work_intro = 1
                scene hall_d with fade
                "..."
                scene black
                "SEMENTARA ITU"
                scene nwork_going2 with fade
                m "..."
                scene nwork_going3 with dissolve
                m "{i} (ini gila) {/i}"
                scene black
                "..."
                scene hall_d with fade
                b "{i} (...) {/i}"
                call screen gnav
            else:


                pass
            scene hall_d with fade
            b "{i} (...) {/i}"
            call screen gnav

        "Di mana Elaine" if elaineshowsup ==1 and day ==6:
            m "Dia di kamarku"
            b "Hmmm Ok"
            m "Biarkan dia tidur, cobalah untuk tidak mengganggunya"
            m "Katakan [sname] juga"
            b "Yes sure"
            m "Sampai jumpa lagi"
            scene hall_d with fade
            b "{i} (...) {/i}"
            call screen gnav

        "Di mana Elaine" if elaineagain ==2 and day ==6:
            m "Dia di kamarku"
            b "Hmmm Ok"
            m "Cobalah untuk tidak mengganggunya"
            m "Katakan [sname] juga"
            b "Yes sure"
            m "Sampai jumpa lagi"
            scene hall_d with fade
            b "{i} (...) {/i}"
            call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc