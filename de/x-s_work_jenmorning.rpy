label s_work_jenmorning:
    if day == 2:
        scene nwork_s_goingno with fade
        b "{i} (tidak ada orang di sini) {/i}"
        b "{i} (dimana mereka?) {/i}"
        b "{i} (mungkin [mname] kamar?) {/i}"
        scene nwork_s_going1 with fade
        m "Tolong ambilkan saya bra"
        scene nwork_s_going2 with dissolve
        b "{i}(Fuck it){/i}"
        m "Terima kasih"
        b "{i} (i \ 'D lebih baik pergi sebelum [mname] melihat saya) {/i}"
        scene broom_day with fade
        "..."
        call screen gnav

    elif day == 4:
        scene nwork_s_goingno with fade
        b "{i} (tidak ada orang di sini) {/i}"
        b "{i} (dimana mereka?) {/i}"
        b "{i} (mungkin [mname] kamar?) {/i}"
        scene nwork_s_going1 with fade
        m "Tolong ambilkan saya bra"
        scene nwork_s_going2 with dissolve
        b "{i}(Fuck it){/i}"
        scene nwork_s_going3 with dissolve
        m "Terima kasih sayang"
        b "{i} (i \ 'D lebih baik pergi sebelum [mname] melihat saya) {/i}"
        scene broom_day with fade
        "..."
        call screen gnav

    elif day == 6:
        scene nwork_s_goingno with fade
        b "{i} (tidak ada orang di sini) {/i}"
        b "{i} (dimana mereka?) {/i}"
        b "{i} (mungkin [mname] kamar?) {/i}"
        scene nwork_s_going1 with fade
        m "Tolong ambilkan saya bra"
        scene nwork_s_going2 with dissolve
        b "{i}(Fuck it){/i}"
        scene nwork_s_going4 with dissolve
        m "Terima kasih sayang"
        b "{i} (i \ 'D lebih baik pergi sebelum [mname] melihat saya) {/i}"
        scene broom_day with fade
        "..."
        call screen gnav
    else:
        pass
    scene nwork_s_going with fade
    b "{i}(Aha){/i}"
    s "Semoga harimu indah"
    m "Kamu juga sayang"
    b "{i} (i \ 'D lebih baik pergi sebelum [mname] melihat saya) {/i}"
    scene broom_day with fade
    "..."
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
