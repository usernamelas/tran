image chnightdance:
    "chnight28.jpg"
    pause 0.1
    "chnight29.jpg"
    pause 0.1
    "chnight30.jpg"
    pause 0.1
    "chnight31.jpg"
    pause 0.1
    "chnight32.jpg"
    pause 0.1
    "chnight33.jpg"
    pause 0.1
    "chnight34.jpg"
    pause 0.1
    "chnight35.jpg"
    pause 0.1
    "chnight36.jpg"
    pause 0.1
    "chnight37.jpg"
    pause 0.1
    "chnight38.jpg"
    pause 0.1
    "chnight39.jpg"
    pause 0.1



label cherylnight:
    scene chnight with fade
    m "Ya, saya akan menunggu Anda"
    scene chnight1 with fade
    m "Datang"
    $ persistent.unlock_21 = True
    scene chnight2 with dissolve
    c "Jadi?"
    m "Jadi?"
    c "Apa kabarmu?"
    m "Kami melakukannya dengan sangat baik"
    c "Bagus"
    c "..."
    c "Dimana [sname] dan [bname]"
    m "Saya akan menelepon mereka"
    scene chnight3 with dissolve
    "..."
    scene chnight4 with fade
    if persistent.patch_enabled:
        s "Bibi Cheryl!"
        pass
    else:
        s "CHERYL!"
        pass
    scene chnight5 with dissolve
    s "Aku merindukanmu"
    c "..."
    scene chnight6 with dissolve
    "..."
    scene chnight7 with fade
    c "Selamat malam semuanya"
    s "Selamat malam"
    b "Selamat malam"
    scene chnight8 with fade
    s "Kamu tidak apa apa?"
    m "Tolong tidur"
    b "..."
    m "Kalian berdua"
    menu:
        "Tinggal":
            b "Ok"
            b "Selamat malam"
            b "Let \'s Go [sname]"
            scene chnight9 with dissolve
            s "Selamat malam"
            scene chnight10 with dissolve
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
                m "{i} (apa yang kamu bicarakan [mname]) {/i}"
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
        "Pergi tidur":


            scene broom_night with fade
            b "{i} (...) {/i}"
            jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc