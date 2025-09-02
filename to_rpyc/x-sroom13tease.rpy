label sroom13tease:
    b "Call her"
    b "Mari kita lihat apakah dia datang"
    scene sroom_av15a with vpunch
    s "Aku akan membunuhmu"
    scene srtease with dissolve
    b "Ouch"
    s "Apakah Anda akan menghentikan game ini?"
    b "Ya, tolong lepaskan saya"
    scene srtease1 with hpunch
    s "Hai!"
    b "Santai, aku tidak akan menyakitimu"
    b "Aku hanya ingin menciummu"
    scene srtease2 with fade
    "..."
    menu:
        "Membuka pakaiannya dan melanjutkan" if srel>=300:
            scene srtease4 with dissolve
            "..."
            scene srtease5 with dissolve
            s "Anda mencekik saya"
            scene srtease6 with fade
            b "Bagaimana dengan mencekik ini"
            s "Ahhh"
            scene srtease7 with dissolve
            s "..."
            scene srtease8 with fade
            s "Apakah kamu cum?"
            b "Tidak, hehehe"
            scene srtease3 with fade
            b "Cuci diri Anda sendiri"
            scene door with fade
            b "{i} (...) {/i}"
            "..."
            call screen gnav
        "Melanjutkan":
            pass
    scene srtease3 with fade
    "..."
    scene door with fade
    b "{i} (...) {/i}"
    "..."
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc