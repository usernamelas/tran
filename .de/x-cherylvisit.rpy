label cherylvisit:
    play sound "sounds/doorbell.wav"
    m "Hah!"
    m "Siapa itu saat ini?"
    b "Maybe Elaine"
    scene chcm with fade
    m "Buka pintu, aku akan berubah"
    stop sound
    b "Ok"
    scene chnight6 with fade
    c "[bname]"
    scene chnight5 with dissolve
    c "My baby"
    scene chnight2 with dissolve
    c "Bagaimana kabarmu [mname]?"
    m "[sname] [bname] Silakan tinggalkan kami sendiri"
    b "Ok"
    m "[bname] wait"
    scene chcm7 with fade
    m "Saya membunuh Anda jika Anda berbicara lebih banyak dengan Cheryl"
    b "Apa?"
    m "Anda mendengar saya?"
    menu:
        "Apakah Anda ingin saya mencoba dan memperbaiki sesuatu?":
            if mrel >= 300:
                m "Apa yang akan kamu lakukan?"
                b "Serahkan padaku"
                m "Katakan padaku sekarang"
                b "Aku akan berteman dengannya, aku akan membawanya ke dalam kita sehingga dia tidak bisa menyakiti kita"
                m "No"
                b "Baik itu akan berada di bawah pengawasan Anda"
                b "Saat Anda merasa salah, Anda bisa membatalkannya dan menendang saya"
                m "Baiklah, mari kita lihat"
                jump bchmnamenight
            else:

                m "No"
                b "Hmm"
                b "Ok seperti yang Anda inginkan"
                pass
        "Tidak mengatakan apa -apa":
            b "All right"
            pass
    scene black
    "Setelah beberapa waktu"
    scene chnight10 with fade
    b "Dia pergi, katakan padaku apa yang salah?"
    m "Saya merasa dia tidak akan meninggalkan kita sendirian"
    b "Kenapa kamu peduli?"
    scene chnight11 with dissolve
    m "Dapatkan aku minuman"
    b "Sure"
    scene chnight12 with dissolve
    b "Apakah Anda ingin menonton TV?"
    m "No"
    m "Dapatkan aku minuman lagi"
    b "OK"
    scene chnight13 with dissolve
    b "Sekarang apa?"
    if mrel >=450:
        m "Nothing"
        scene chnight14 with dissolve
        b "..."
        b "Biarkan saya membuat Anda merasa lebih baik"
        scene chnight15 with dissolve
        "..."
        scene chnight16 with dissolve
        b "Ayo bersorak"
        b "Kalau tidak, saya harus memberi Anda pertunjukan dansa"
        scene chnight17 with dissolve
        m "Dapatkan aku minuman lagi"
        m "Aku akan kembali"
        scene chnight18 with fade
        m "Apa yang sedang kamu lakukan?"
        s "Berencana memeriksa email saya ..."
        m "Saya muak dengan ini [sname]"
        m "Anda membumi selama satu jam"
        m "Saya ingin Anda tinggal di kamar Anda"
        m "Dan belajar selama satu jam"
        m "Hanya saat saya kembali dan periksa kemajuan Anda"
        m "Hanya dengan begitu, Anda bisa keluar, menyikat gigi dan pergi tidur"
        s "Tetapi"
        m "Tidak tapi"
        m "Atau saya akan mengunci pintu Anda dari luar"
        scene black
        "..."
        scene chnight12 with fade
        m "Terima kasih atas minumannya"
        scene chnight19 with fade
        m "Apakah Anda pikir dia akan memberitahunya?"
        b "Saya kira tidak demikian"
        b "Hanya tidak khawatir tentang itu"
        m "..."
        b "Saatnya menghibur Anda"
        scene chnight20 with dissolve
        b "Tada!"
        scene chnight21 with dissolve
        "..."
        scene chnight22 with dissolve
        m "Ha ha ha!"
        m "Bukan itu yang Anda lakukan"
        scene chnight23 with dissolve
        b "Dingin"
        scene chnight24 with dissolve
        "..."
        scene chnight25 with dissolve
        b "Ajari aku cara menari"
        m "{i} (hanya jika Anda meniduri saya dengan penis kuda ini) {/i}"
        scene chnight26 with dissolve
        m "{i} (apa yang Anda bicarakan [mname]) {/i}"
        b "Apa yang telah terjadi?"
        b "{i} (sepertinya dia belum mabuk) {/i}"
        b "Saya akan memberi Anda minuman lagi dan kemudian Anda mengajari saya"
        if mrel >=500 and mcorr >= 40:
            m "Ok"
            scene chnight12d with fade
            m "Terima kasih atas minumannya"
            m "Now showtime"
            scene chnightdance
            b "Wow"
            m "Yeah"
            b "Focus [bname]"
            scene chnight40 with dissolve
            b "Focus"
            menu:
                "Melompatinya":
                    scene chnight41 with dissolve
                    "..."
                    m "Ah"
                    scene chnight42 with dissolve
                    m "Ah"
                    scene chnight43 with vpunch
                    b "Oh sial!"
                    scene chnight44 with dissolve
                    b "Kamu tidak apa apa?"
                    m "Ya saya akan tidur"
                    m "Selamat malam"
                    b "Hmm"
                    b "{i} (dia tidak memanggil saya Stewart) {/i}"
                    b "Ok"
                    jump newdays
                "Melanjutkan":

                    scene chnight45 with hpunch
                    b "Oh sial!"
                    b "Kamu tidak apa apa?"
                    m "Ya, selamat malam"
                    m "Silakan tidur, saya ok"
                    b "Hmm"
                    b "Ok"
                    jump newdays
        else:


            m "Tidak, tolong tidur saja"
            b "{i}(Damn){/i}"
            b "Ok"
            jump newdays
    else:


        m "Tidak ada, hanya pergi tidur"
        b "{i}(Damn){/i}"
        b "Ok"
        jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
