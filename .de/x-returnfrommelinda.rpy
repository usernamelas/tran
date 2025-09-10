label returnfrommelinda:
    scene rfmel with fade
    m "Apa yang salah sayang?"
    b "Nothing"
    if mfuckedsober >= 1:
        m "Lagi?"
        m "Apakah itu menyakitkan?"
        pass
    else:

        pass
    b "Saya baik -baik saja, hanya merasa tertekan"
    m "Saya akan berubah dan kembali"
    scene rfmel1 with fade
    m "Hi [sname]"
    m "Apa yang salah dengan [bname]?"
    s "Saya tidak tahu, karena dia datang dia tidak berbicara"
    m "Kemana kamu pergi?"
    s "Visiting Rowena"
    m "Jangan terlambat"
    s "Hanya beberapa jam"
    m "All right"
    scene rfmel2 with fade
    m "Ya Tuhan, masih kesakitan?"
    m "Pergi bersiap -siaplah, mari kita keluar mengubah suasana hati dan berbicara"
    b "Saya tidak ingin pergi, saya akan tidur sekarang"
    if mfuckedsober >= 1:
        m "Wait"
        scene rfmel3 with fade
        m "Ambil gelas ini untuk Anda"
        b "Thanks"
        m "Anda dapat berbicara dengan saya [bname]"
        m "Katakan padaku apa yang mengganggumu"
        b "Itu melinda, saya merasa dia tidak akan meninggalkan kita sendirian"
        scene rfmel4 with dissolve
        m "Apakah itu?"
        b "Yes"
        b "{i} (saya tidak bisa menceritakan semuanya) {/i}"
        m "Apa yang terburuk yang bisa terjadi"
        b "Aku tidak tahu"
        m "Lalu bersantai"
        scene rfmel5 with dissolve
        m "Jangan khawatir tentang itu"
        scene rfmel6 with dissolve
        m "Sekarang lakukan kakiku"
        scene rfmel7 with dissolve
        m "Mmm"
        if mrel >=100:
            scene rfmel8 with fade
            m "Terima kasih [bname]"
            scene rfmel9 with dissolve
            "..."
            scene rfmel10 with dissolve
            "..."
            scene rfmel11 with dissolve
            m "Ini seharusnya membuat Anda merasa lebih baik"
            b "Tapi .. [sname]!"
            m "Pergi mengunci pintu"
            scene rfmel12 with fade
            "..."
            scene rfma
            m "Ahh"
            "..."
            m "Yes"
            "..."
            b "Aku cumming!"
            scene rfmel13 with dissolve
            m "Keluar [bname]"
            scene rfmel14 with fade
            m "Saya harap Anda merasa lebih baik sekarang"
            b "Yes"
            m "Selamat malam"
            jump newdays
        else:
            scene rfmel8 with fade
            m "Terima kasih [bname]"
            m "Selamat malam"
            b "Selamat malam"
            jump newdays
    else:

        m "Baiklah, cocok untuk diri Anda sendiri"
        jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
