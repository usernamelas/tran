label rmvisit:
    scene rmvist with fade
    rm "Hi [bname]"
    rm "Tolong ikuti saya, saya akan menunjukkan mesin pencuci piring"
    scene rmvisit1 with fade
    b "Dimana itu?"
    scene rmvisit2 with dissolve
    rm "Di belakangmu"
    scene rmvisit3 with dissolve
    b "Hah!"
    rm "Membuka pakaian diri dan mulai memakan saya"
    menu:
        "Lakukan itu":
            pass
        "Jangan":

            b "Saya maafkan saya tidak bisa melakukan itu"
            rm "Hmm"
            rm "Mau mu"
            b "Terima kasih"
            scene hall_d with fade
            b "{i} (apa itu) {/i}"
            call screen gnav

    scene row_visit66b with fade
    rm "Siap mengambilnya"
    scene row_visit67b with dissolve
    b "Ahh!"
    menu:
        "Lanjutkan menjilati (tunduk)":
            scene row_visitbs with dissolve
            "..."
            scene row_visitbs1 with dissolve
            b "Ahhh"
            b "{i} (fuck, itu terlalu banyak) {/i}"
            b "{i} (Time to Stand Up) {/i}"
            pass
        "Berhenti menjilati":

            pass
    rm "Giliran saya sekarang"
    scene row_visit68b with dissolve
    "..."
    scene row_visit69b with dissolve
    "..."
    scene row_visit70b with fade
    b "Ughh"
    scene row_visit71b with dissolve
    b "..."
    scene row_visit72b with dissolve
    $ persistent.unlock_24 = True
    rm "Lakukan dengan benar"
    b "Yes"
    scene row_visit72c with dissolve
    b "Saya akan melakukannya dengan benar"
    rm "Ahh"
    scene row_visit73c with dissolve
    rm "Ahhh"
    rm "Berikan padaku"
    scene row_visit75b with fade
    b "Fuck"
    scene row_visit76b with dissolve
    "..."
    scene row_visit77b with dissolve
    "..."
    scene row_visit78b with fade
    s "Kemana saja kamu?"
    b "Apa yang salah?"
    s "Apa yang terjadi dengannya?"
    b "Dia memberi kuliah, dan mengancam dia akan memberi tahu orang tua saya"
    b "Dimana Rowena?"
    s "Mereka melarikan diri sejak dia muncul"
    b "Ayo biarkan pulang"
    scene broom_day with fade
    "..."
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
