image ralonea:
    "ralonea00.jpg"
    pause 0.05
    "ralonea01.jpg"
    pause 0.05
    "ralonea02.jpg"
    pause 0.05
    "ralonea03.jpg"
    pause 0.05
    "ralonea04.jpg"
    pause 0.05
    "ralonea05.jpg"
    pause 0.05
    "ralonea06.jpg"
    pause 0.05
    "ralonea07.jpg"
    pause 0.05
    "ralonea08.jpg"
    pause 0.05
    "ralonea09.jpg"
    pause 0.05
    "ralonea10.jpg"
    pause 0.05
    "ralonea11.jpg"
    pause 0.05
    "ralonea12.jpg"
    pause 0.05
    "ralonea13.jpg"
    pause 0.05
    "ralonea14.jpg"
    pause 0.05
    "ralonea15.jpg"
    pause 0.05
    "ralonea16.jpg"
    pause 0.05
    "ralonea17.jpg"
    pause 0.05
    repeat

label rowenalone:
    scene ralone with fade
    a "Hi [bname]"
    b "Hi"
    a "Dimana [sname]"
    b "Dia tidak bisa membuatnya"
    a "Ah begitu, tolong masuk"
    scene ralone1 with fade
    b "Jadi apa yang terjadi?"
    a "Tidak ada, dia hanya bajingan"
    b "Mengapa?"
    a "Dia pikir saya berselingkuh dengan Anda"
    scene ralone2 with dissolve
    b "Aku!"
    a "Yes"
    b "Apa-apaan!"
    scene ralone1 with dissolve
    a "Anyway"
    a "Apakah Anda ingin berenang?"
    scene ralone3 with fade
    a "Anda tetap dalam hal ini?"
    scene ralone4 with dissolve
    "..."
    scene ralone5 with dissolve
    a "Terima kasih telah datang [bname], sangat membosankan untuk sendirian"
    b "Yeah"
    scene ralone6 with dissolve
    a "So lonely"
    b "Yes"
    scene ralone7 with dissolve
    b "Indeed"
    menu:
        "Bergerak" if rowenacall <2:
            $ rowenamove += 1
            scene ralone8 with dissolve
            if rowenamove ==1:
                a "Hah!"
                a "[bname] please"
                a "Stop it"
                b "Ok sorry"
                scene ralone5 with fade
                "Anda menghabiskan waktu"
                "Dan pulang"
                scene ralone5e with fade
                a "Terima kasih telah datang [bname]"
                scene broom_day with fade
                b "{i} (mungkin saya harus mencoba keberuntungan saya lain kali) {/i}"
                call screen gnav
            else:

                pass
        "Bergerak" if rowenacall >=2:
            $ rowenamove += 1
            scene ralone8 with dissolve
            pass
        "Jangan":

            scene ralone5 with dissolve
            "Anda menghabiskan waktu"
            "Dan pulang"
            scene ralone5e with fade
            a "Terima kasih telah datang [bname]"
            scene broom_day with fade
            "..."
            call screen gnav

    "..."
    a "Hmm"
    $ persistent.unlock_13 = True
    scene ralone9 with dissolve
    a "Anda seperti pria seperti itu"
    a "Let's swim"
    scene ralone10 with dissolve
    b "Hmm"
    scene ralone11 with dissolve
    a "Airnya terasa enak"
    b "Yeah"
    scene ralone12 with fade
    b "Apakah Anda memiliki sesuatu untuk diminum?"
    a "Ya Tentu, apa yang Anda inginkan?"
    b "Anything"
    scene ralone13 with dissolve
    "..."
    scene ralone14 with fade
    "..."
    scene ralone15 with dissolve
    "..."
    scene ralone16 with dissolve
    "..."
    scene ralone17 with dissolve
    b "Apa yang salah?"
    b "Apakah kamu menangis?"
    scene ralone18 with dissolve
    b "Hey berhenti menangis"
    scene ralone19 with dissolve
    "..."
    scene ralone20 with dissolve
    a "{i} (Ya Tuhan, dia sangat besar) {/i}"
    scene ralone21 with dissolve
    b "Semuanya akan baik -baik saja"
    scene ralone22 with dissolve
    a "Mhhm"
    menu:
        "Berlututnya":
            scene ralone23 with fade
            "..."
            scene ralone24 with hpunch
            b "Enough teasing"
            scene ralone25 with dissolve
            b "Yeah"
            scene ralone26 with dissolve
            "..."
            scene ralone5e with fade
            a "Terima kasih telah datang [bname]"
            scene broom_day with fade
            "Saya harus mengunjunginya beberapa kali lagi"
            call screen gnav

        "Persetan dia" if rowenamove >2:
            scene ralonea
            "..."
            a "Ah"
            b "..."
            a "Ahh"
            scene ralone27 with hpunch
            b "Ahhh"
            scene ralone28 with dissolve
            "..."
            scene broom_day with fade
            "..."
            call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc