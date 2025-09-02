label rowenaorgy:
    a "Ahem!"
    scene rorgy1 with dissolve
    s "Hah!"
    if browenabm ==2:
        scene rorgy2 with dissolve
        $ browenabm =3
        a "Saya melihat Anda menikmati waktu Anda"
        s "Kita sudah selesai, ayo pergi"
        scene rorgy3 with dissolve
        a "Not yet"
        scene rorgy4 with dissolve
        s "Apa?!"
        s "TIDAK!!"
        a "Ok seperti yang Anda inginkan"
        a "Saya akan menunjukkan foto -foto ini ke [mname]"
        scene rorgy5 with dissolve
        "..."
        scene rorgy6 with dissolve
        s "Apa yang kamu inginkan?"
        a "Let \'s Go, Anda akan segera tahu"
        scene rorgy7 with fade
        a "Ayo, jangan malu"
        scene rorgy8 with dissolve
        "..."
        scene rorgy9 with dissolve
        a "Ahhh"
        scene rorgy10 with dissolve
        a "{i} (Saya ingin dia untuk saya) {/i}"
        a "Datang ke sini [sname]"
        scene rorgy11 with dissolve
        a "Ahhh"
        $ persistent.unlock_17 = True
        scene rorgy12 with dissolve
        b "Ahh aku cum"
        a "{i} (Saya ingin makan [sname]) {/i}"
        scene rorgy13 with fade
        s "Ahhh"
        scene nbr with fade
        s "..."
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav

    elif browenabm ==3:
        scene rorgy2 with dissolve
        a "Saya melihat Anda menikmati waktu Anda"
        s "Kita sudah selesai, ayo pergi"
        scene rorgy3 with dissolve
        a "Not yet"
        scene rorgy4 with dissolve
        s "Apa?!"
        s "Hmm"
        scene rorgy5 with dissolve
        "..."
        scene rorgy6 with dissolve
        s "Apa yang kamu inginkan?"
        a "Let's go"
        scene rorgy7 with fade
        a "Ayo, jangan malu"
        scene rorgy8 with dissolve
        "..."
        scene rorgy9 with dissolve
        a "Ahhh"
        scene rorgy10 with dissolve
        a "{i} (Saya ingin dia untuk saya) {/i}"
        a "Datang ke sini [sname]"
        rb "Hei, bagaimana dengan saya?"
        a "Oh maaf sayang"
        a "Kemarilah"
        scene rorgy14 with fade
        rb "Ahhh"
        scene rorgy15 with dissolve
        a "Sayang, apakah kamu ingin membawaku dengan [bname]?"
        rb "Yeah"
        a "Bagaimana denganmu [bname]"
        menu:
            "Tidak, ini gila":
                b "Let \'s Go [sname]"
                scene rorgyend with fade
                s "..."
                scene hall_d with fade
                b "{i} (...) {/i}"
                call screen gnav
            "Ya tentu":

                pass
        scene rorgy16 with fade
        "..."
        scene rorgy17 with dissolve
        a "Biarkan [bname] ambil pantatku"
        scene rorgy18 with dissolve
        a "Ahhhh"
        rb "I'm done"
        b "Kemarilah Rowena"
        scene rorgy19 with fade
        b "Grrr"
        scene rorgy20 with dissolve
        b "..."
        scene rorgy21 with dissolve
        "..."
        scene rorgy22 with dissolve
        s "..."
        $ sgrm = 1
        s "{i} (i \ 'll membuat dia membayar untuk ini) {/i}"
        scene rorgy23 with dissolve
        "..."
        scene rorgy24 with dissolve
        s "Cukup! Lepaskan"
        scene nbr with fade
        s "..."
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav
    else:






        scene rorgy with dissolve
        a "Saya melihat Anda menikmati waktu Anda"
        a "Lanjutkan, kami sedang menunggumu"
        s "Tidak, kita sudah selesai"
        $ browenabm = 1
        b "{i} (mungkin saya harus berbicara dengan Rowena tentang ini) {/i}"
        b "{i} (kita dapat memiliki pesta) {/i}"
        scene nbr with fade
        s "..."
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc