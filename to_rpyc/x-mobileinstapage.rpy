label mobileinstapage:
    $ smobilegiven = 1
    b "Hmm"
    b "{i} (Saya harap ini waktu yang tepat) {/i}"
    b "Aku punya sesuatu untukmu"
    s "Apa itu?"
    b "Ponsel baru"
    scene binstas_mob with dissolve
    s "Dengan serius!"
    b "Yes"
    scene binstas_mob2 with hpunch
    s "YOOO HOOO"
    s "Terima kasih [bname]"
    scene binstas_mob3 with dissolve
    b "{i} (i ... saya tidak bisa mengambilnya lagi) {/i}"
    b "[sname] Bangun"
    scene binstas_mob4 with dissolve
    s "Ini model terbaru, kan?"
    b "Yes"
    scene binstas_mob1 with hpunch
    s "Ya Tuhan, aku tidak bisa mempercayainya"
    scene binstas_mob5 with dissolve
    s "Terima kasih banyak"
    menu:
        "Cobalah keberuntungan Anda":
            scene binstas_mob6 with dissolve
            "..."
            scene binstas_mob7 with dissolve
            "..."
            b "{i} (keren, tidak ada reaksi) {/i}"
            pass
        "Jangan":
            pass
    scene binstas_mob4 with dissolve
    s "Terima kasih [bname]"
    s "Itu adalah kejutan yang menyenangkan"
    s "Sampai jumpa!"
    scene broom_night with fade
    "..."
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc