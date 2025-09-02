label mtoi_practice:
    scene m_toi_p0 with fade
    b "..."
    scene m_toi_p2 with dissolve
    m "Apakah Anda punya masalah jika saya datang seperti itu?"
    b "{i} (pertanyaan perangkap?) {/i}"
    b "Hmm"
    menu:
        "Jangan tahu, saya tidak bisa melihat dengan jelas":
            m "Kenakan"
            pass
        "Tidak Memangnya kenapa?":
            m "Pakai lampu"
    scene m_toi_p with dissolve
    "..."
    scene m_toi_p1 with dissolve
    b "Jadi apa itu?"
    b "Berdiri di tempat Anda berada"
    m "Dan jangan katakan apa pun kecuali saya bertanya kepada Anda"
    b "Ok"
    scene m_toi_p3 with dissolve
    "..."
    scene m_toi_p4 with dissolve
    "..."
    scene m_toi_p5 with dissolve
    "..."
    scene m_toi_p6 with dissolve
    "..."
    scene m_toi_p7 with fade
    m "Itu saja"
    m "Anda bisa pergi"
    b "Apa?"
    m "Ya tolong pergi"
    b "..."
    scene black
    jump broom_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc