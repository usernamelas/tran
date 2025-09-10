label m_b_naivetalk:
    scene mbntalk with fade
    $ naivetalk = 1
    b "..."
    m "Saya telah melihat apa yang telah Anda lakukan"
    b "Melakukan apa?"
    m "Listen [bname]"
    m "Jangan menyangkalnya"
    scene mbntalk1 with dissolve
    m "Anda tidak dapat bermain game seperti itu dengan [sname]"
    b "Mengapa?"
    m "Kemarilah sayang"
    scene mbntalk2 with dissolve
    m "Anda dapat menarik jenis permainan ini ..."
    m "Pada seorang teman"
    m "Seorang teman pria"
    m "Bukan seorang gadis"
    m "Apakah Anda mengerti apa yang saya bicarakan"
    b "Tidak begitu, tapi saya ingat ini jadi saya tidak mengulanginya"
    m "Bagus"
    scene mbntalk3 with dissolve
    b "Sorry"
    m "Itu baik -baik saja"
    scene mbntalk4 with fade
    b "{i} (phew! Sangat dekat) {/i}"
    "..."
    m "{i} (bocah kecil yang malang, dia super naif) {/i}"
    "..."
    scene door with fade
    b "{i} (...) {/i}"
    "..."
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
