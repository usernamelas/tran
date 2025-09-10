label mgettingreadyfornails:
    if mrel>=200:
        pass
    else:
        scene door with fade
        b "{i} (oh sialan itu terkunci) {/i}"
        "Naikkan poin Anda menjadi 200"
        call screen gnav
    scene door with fade
    b "{i} (Sepertinya pintu terbuka) {/i}"
    scene mroom_gr with dissolve
    b "{i} (dia tidak memperhatikan bahwa saya sudah masuk) {/i}"
    scene mroom_gr1 with dissolve
    b "{i} (keren) {/i}"
    scene mroom_gr2 with dissolve
    "..."
    if mgready ==0:
        $ mgready += 1
        scene mroom_gr3 with dissolve
        b "..."
        m "[bname]!"
        m "Apa yang kamu lakukan di sini"
        b "Maaf saya tersesat"
        m "All right"
        m "Please go"
        scene door with fade
        b "{i} (mungkin hari Minggu depan segalanya akan lebih baik) {/i}"
        call screen gnav

    elif mgready ==1:
        $ mgready += 1
        scene mroom_gr4 with dissolve
        b "..."
        m "[bname]!"
        b "Maaf saya tersesat"
        scene mroom_gr6 with dissolve
        m "It's okay"
        m "Saya baru saja berubah"
        m "Anda mungkin pergi sekarang"
        scene door with fade
        b "{i} (hmm dia tidak marah) {/i}"
        call screen gnav

    elif mgready ==2:
        $ mgready += 1
        scene mroom_gr5 with dissolve
        m "..."
        scene mroom_gr7 with dissolve
        b "{i} (keren) {/i}"
        scene mroom_gr8 with dissolve
        b "{i} (haha dia tampak senang) {/i}"
        scene mroom_gr9 with dissolve
        m "[bname]!"
        b "Maaf saya tersesat"
        m "It's okay"
        m "Saya baru saja berubah"
        m "Anda mungkin pergi sekarang"
        scene door with fade
        b "{i} (hmm keren! Dia tidak peduli) {/i}"
        call screen gnav
    else:

        scene mroom_gr5 with dissolve
        m "..."
        scene mroom_gr7 with dissolve
        b "{i} (keren) {/i}"
        scene mroom_gr8 with dissolve
        b "{i} (haha dia tampak senang) {/i}"
        if mrel >=200 and elaine_convince == 4:
            scene mroom_gr12 with dissolve
            "..."
            scene mroom_gr13 with dissolve
            m "[bname]?"
            scene mroom_gr9 with dissolve
            b "Maaf saya tersesat"
            m "It's okay"
            m "Saya baru saja berubah"
            scene mroom_gr10 with dissolve
            "..."
            scene mroom_gr14 with dissolve
            m "Tolong ambilkan sepatunya"
            b "Sure"
            scene mroom_gr15 with dissolve
            m "Ini dia"
            scene mroom_gr16 with dissolve
            m "Terima kasih"
            "Itu semua di sini"
            pass
        else:
            scene mroom_gr9 with dissolve
            m "[bname]!"
            b "Maaf saya tersesat"
            m "It's okay"
            m "Saya baru saja berubah"
            scene mroom_gr10 with dissolve
            "..."
            pass

        scene mroom_gr11 with fade
        m "Done"
        m "Sampai jumpa lagi"
        scene door with fade
        "..."
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
