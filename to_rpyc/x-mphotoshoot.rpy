label mphotoshoot:
    m "Bagaimana Anda menginginkannya?"
    $ mbikinirequest = 1
    scene mphotoshoot with dissolve
    b "{i} (di pantat tolong hehehe) {/i}"
    m "Saya menunggu!"
    scene mphotoshoot1 with dissolve
    b "Ah maaf, ya condongkan saja di dinding"
    b "Saya akan mendapatkan telepon"
    scene mphotoshoot2 with fade
    b "Bagus"
    b "Ok sekarang lakukan tangan di udara"
    scene mphotoshoot3 with dissolve
    m "Seperti itu?"
    b "Ya bagus"
    b "Berbelok ke kanan"
    if day ==5:
        scene mphotoshoot5 with dissolve
        b "More"
        pass
    elif day ==6:
        scene mphotoshoot6 with dissolve
        b "More"
        pass
    else:
        scene mphotoshoot7 with dissolve
        b "More"
        pass
    if mrel >=370:
        scene mphotoshoot8 with dissolve
        b "..."
        b "Apa?"
        scene mphotoshoot9 with dissolve
        m "Apa yang akan Anda lakukan dengan foto -foto ini?"
        b "Aku akan menyimpannya untukmu"
        b "Semacam membuat portofolio Anda"
        m "Eh huh! Lalu apa?"
        b "Tidak ada, Anda menyimpannya"
        b "Jika suatu hari Anda memutuskan untuk menjualnya"
        if mcorr >=50:
            b "Jadi? Haruskah kita melanjutkan?"
            m "Yes"
            scene mphotoshoot10 with dissolve
            "..."
            if mmirror ==0:
                m "Alangkah baiknya jika ada cermin dinding"
                $ mmirror = 1
                b "Ya ide bagus"
                b "Bisakah Anda mengubah pose?"
                pass
            elif mmirror ==2:
                m "Alangkah baiknya jika ada cermin dinding"
                b "Saya punya satu"
                scene mphotoshoot11 with dissolve
                m "Ayo Dapatkan Di Sini"
                b "Ok"
                scene mphotoshoot12 with fade
                "..."
                scene mphotoshoot13 with dissolve
                m "Haruskah kita mulai?"
                b "Oh ya pasti"
                scene mphotoshoot14 with dissolve
                m "Saya pikir Anda tidak dapat mengambil foto seperti itu"
                b "Mengapa?"
                m "Anda ditampilkan di cermin"
                b "Hehehe ya maaf"
                scene mphotoshoot15 with dissolve
                "..."
                if springstring == 1:
                    scene mphotoshoot16 with dissolve
                    b "Mengapa Anda tidak mencoba ini"
                    $ springstring = 2
                    m "Apa itu?"
                    b "Itu adalah sesuatu yang saya punya untuk Anda"
                    scene mphotoshoot17 with dissolve
                    m "Anda tidak dapat mengharapkan saya mengambil foto dalam hal ini?"
                    b "Mengapa tidak?"
                    m "Itu cukup [bname]"
                    b "Tetapi!"
                    m "Mungkin lain kali"
                    m "Tolong pergi saja"
                    b "Ok"
                    scene hall_n with fade
                    "..."
                    call screen gnav



                elif springstring == 2:
                    scene mphotoshoot16 with dissolve
                    b "Kami melanjutkan?"
                    m "Menoleh"
                    scene mphotoshoot17 with dissolve
                    "..."
                    $ mphotoediting = 1
                    scene mphotoshoot18 with dissolve
                    $ persistent.unlock_37 = True
                    b "Bagus"
                    m "Mari kita ambil satu dengan ini"
                    scene mphotoshoot19 with fade
                    "..."
                    scene mphotoshoot20 with dissolve
                    "..."
                    m "Cukup untuk hari ini"
                    b "Ok"
                    scene hall_n with fade
                    "..."
                    call screen gnav
                else:
                    m "Cukup untuk hari ini"
                    b "Ok"
                    scene hall_n with fade
                    "..."
                    call screen gnav
            else:

                b "Yang bagus"
                b "Sekarang pose lain"
                pass
        else:
            b "Jadi? Haruskah kita melanjutkan?"
            pass
    else:

        pass
    scene mphotoshoot4 with dissolve
    m "Tidak, itu cukup"
    b "Oh"
    m "Pergi Cuci dan Bersiaplah Untuk Makan Malam"
    b "Ok"
    scene hall_n with fade
    "..."
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc