label followmnamech:
    b "{i} (Let \ melihat apakah dia baik -baik saja setelah mengetahui tentang cheryl) {/i}"
    scene room3 with fade
    $ cherylfoundout = 3
    b "Hmmm"
    b "Itu terkunci, mungkin dia ada di kamarnya"
    scene door with fade
    b "{i}(Hmm){/i}"
    b "Apakah Anda masuk?"
    m "Saya baik -baik saja tidak khawatir"
    b "Ya tapi bisakah saya masuk?"
    if elaine_convince ==4 and mrel >=200:
        scene fmch with fade
        m "Yes"
        b "Kamu tidak apa apa?"
        m "Aku tidak tahu"
        b "Apakah karena Cheryl?"
        scene fmch1 with dissolve
        m "Yes"
        b "Jangan khawatir tentang dia"
        b "Tidak ada yang tahu di mana saya tinggal"
        b "Dan saya memastikan tidak ada yang mengikuti saya dalam perjalanan pulang"
        m "Apa kamu yakin?"
        b "Yes"
        scene fmch2 with dissolve
        m "Saya tidak ingin Stewart berada di depan pintu saya"
        b "..."
        m "Setidaknya tidak sekarang"
        scene fmch3 with fade
        m "Saya \ 'm maaf [bname] tapi saya ingin waktu sendirian"
        m "Aku akan melihatmu nanti di aula"
        b "All right"
        scene broom_night with fade
        "..."
        call screen gnav
    else:

        m "Tidak, maaf"
        b "Jika ini tentang Cheryl"
        b "Jangan khawatir tentang itu"
        b "Saya sudah memastikan tidak ada yang mengikuti saya dalam perjalanan pulang"
        m "Saya ingin waktu sendirian"
        m "Aku akan melihatmu nanti di aula"
        b "All right"
        scene broom_night with fade
        "..."
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc