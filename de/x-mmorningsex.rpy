label mmorningsex:
    scene mmornsex with fade
    m "Sit"
    if mfuckedsober >= 1 and mrel >=200:
        scene mmornsex7 with dissolve
        m "Kamu tidak apa apa?"
        b "Apa maksudmu?"
        scene mmornsex8 with dissolve
        m "Lagi!!"
        b "Err"
        scene mmornsex9 with dissolve
        m "Biarkan saya melihatnya"
        m "Lepaskan pakaian Anda"
        scene mmornsex10 with dissolve
        "..."
        scene mmornsex11 with dissolve
        "..."
        scene mmornsex12 with dissolve
        b "..."
        scene mmornsex13 with hpunch
        b "Huh"
        scene mmoa
        "..."
        b "Ahh"
        m "Mhhm"
        "..."
        scene mmob
        "..."
        m "Yess"
        "..."
        m "Ahhh"
        scene mmornsex14 with fade
        m "Ahh"
        scene mmornsex15 with dissolve
        m "..."
        scene mmornsex16 with dissolve
        m "Enough [bname]"
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav
    else:
        pass
    scene mmornsex1 with dissolve
    "..."
    scene mmornsex2 with dissolve
    "..."
    scene mmornsex3 with dissolve
    m "Apakah kamu suka ini?"
    b "Yes"
    scene mmornsex4 with dissolve
    b "Tapi saya suka tanpa"
    scene mmornsex5 with dissolve
    m "Terima kasih atas dukungan Anda [bname]"
    m "Anda bisa pergi sekarang"
    scene mmornsex6 with dissolve
    b "Ok"
    scene hall_d with fade
    b "{i} (...) {/i}"
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
