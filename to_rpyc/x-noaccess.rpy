label noaccess:
    show screen noaccessnotif
    "..."
    hide screen noaccessnotif
    "..."
    call screen etvnav

label noaccessback:
    call screen etvnav

label mroom_etv:
    scene door with fade
    b "{i} (pintu terkunci) {/i}"
    menu:
        "Ketukan":
            play sound "sounds/doorbell.wav"
            "..."
            stop sound
            b "{i} (mungkin tidur) {/i}"
            b "{i} (i \ 'll pergi tidur) {/i}"
            jump newdays

        "Periksa jendela" if windowfound ==1:
            scene black
            "..."
            scene mstairse with fade
            b "{i}(Hmmm){/i}"
            scene mstairse1 with dissolve
            "..."
            scene mstairse2 with dissolve
            "..."
            scene mstairse3 with fade
            "..."
            scene mstairse4 with dissolve
            b "{i} (oh fuck apakah dia melakukannya!) {/i}"
            scene mstairse5 with dissolve
            b "Oh sial!"
            scene mstairse6 with dissolve
            "..."
            scene mstairse7 with dissolve
            m "Ah"
            scene mstairse6 with dissolve
            "..."
            scene mstairse7 with dissolve
            m "..."
            scene mstairse3 with fade
            b "{i} (sepertinya dia sudah selesai) {/i}"
            b "{i} (Time to Sleep) {/i}"
            "Itu semua dalam opsi ini"
            jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc