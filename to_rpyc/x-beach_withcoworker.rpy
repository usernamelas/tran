label beach_withcoworker:
    scene beacha with fade
    "..."
    scene beacha1 with dissolve
    s "Mengapa orang ini disini?"
    b "Aku tidak tahu"
    scene beacha2 with fade
    "..."
    menu:
        "Pergi berenang dengan [sname]":
            scene beacha3 with dissolve
            mb "Apakah Anda ingin minum?"
            b "Saya tidak menyukai orang ini"
            s "Tapi kenapa? Dia keren"
            b "Aku hanya tidak menyukai dia"
            s "Anda cemburu karena ia memiliki enam paket dan Anda tidak"
            b "Yeah right"
            scene black
            "..."
            scene beacha4 with fade
            s "Lihat dia membeli minuman untuk mereka berdua"
            b "Grrr"
            scene beacha5 with dissolve
            s "Tidakkah kamu ingin berenang?"
            m "Tidak, saatnya untuk pergi"
            scene hall_d with fade
            b "{i} (...) {/i}"
            call screen gnav
        "Tetap di sini":

            scene beacha6 with fade
            s "Dia keren orang ini"
            b "Apa -apaan [sname]!"
            s "Anda cemburu karena ia memiliki enam paket dan Anda tidak"
            b "Yeah right"
            scene black
            "..."
            scene beacha7 with fade
            s "Lihat dia"
            b "Diam [sname]!"
            scene beacha8 with dissolve
            m "Ayo teman -teman, mari kita pulang ke rumah"
            scene hall_d with fade
            b "{i} (...) {/i}"
            call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc