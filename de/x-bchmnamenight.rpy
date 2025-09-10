label bchmnamenight:
    $ ctempted += 1
    scene chnight46 with fade
    b "Hei, maukah kamu minum sesuatu"
    c "Hmm tentu saja"
    scene mbgn26 with dissolve
    "..."
    scene chnight47 with dissolve
    b "Ini dia"
    c "Terima kasih"
    scene chnight48 with fade
    c "Minuman ini terlalu kuat [bname]"
    c "Entah karena terlalu manis"
    c "Atau karena saya tidak makan sebelumnya"
    b "Ya saya juga"
    b "Tunggu, apakah Anda ingin melihat gerakan tarian saya?"
    c "Hehe"
    c "Ok"
    scene chnight49 with dissolve
    c "Hahahah"
    m "Hah! [bname] Hentikan!"
    m "Pergi ke kamar Anda"
    c "Biarkan dia menari, dia mabuk"
    c "Sebenarnya aku akan menari dengannya"
    scene chnight50 with dissolve
    m "Hah!"
    m "Hai!"
    if ctempted ==1:
        scene chnight51 with dissolve
        m "Hentikan!"
        c "Hmm"
        pass
    else:
        scene chnight51 with dissolve
        m "Hentikan!"
        c "Hmm"
        scene chnight52 with hpunch
        m "Pergi ke kamar Anda sekarang"
        scene chnight53 with fade
        c "Tenang saja, dia hanya seorang pemuda"
        c "Ditambah minuman ini terlalu kuat"
        scene chnight54 with dissolve
        m "Saya mengerti tetapi dia harus tahu lebih baik"
        scene black
        "SEMENTARA ITU"
        scene chnight55 with dissolve
        "..."
        scene chnight56 with dissolve
        c "Hi there"
        b "Errm Hi"
        scene chnight57 with dissolve
        c "Jangan khawatir dia tertidur"
        c "Terbuang dari minuman Anda"
        b "Oh Ok"
        c "Jadi beri tahu saya [bname], apa yang salah dengannya?"
        scene chnight56 with dissolve
        b "Apa maksudmu?"
        c "Tentang pekerjaan dan hubungannya dengan Stewart ..."
        b "Saya tidak mengerti"
        if chbopen ==1:
            c "Rasanya panas di sini, jangankah Anda memiliki AC?"
            scene chnight58 with dissolve
            b "SAYA..."
            scene chnight59 with dissolve
            c "Apakah Anda memiliki lebih banyak dari minuman ini?"
            menu:
                "Berbohong":
                    b "No Sorry, sudah selesai"
                    c "Ok saya kira saya akan pergi"
                    pass
                "Ya":

                    b "Yes"
                    c "Lalu dapatkan kami beberapa"
                    scene chnight60 with fade
                    b "Ini dia"
                    c "Terima kasih"
                    scene chnight61 with dissolve
                    c "Cheers"
                    b "Cheers"
                    c "Babak Lain?"
                    b "Ya putaran lain"
                    scene chnight60 with fade
                    b "Ini dia"
                    c "Duduk di tempat tidur"
                    scene chnight62 with dissolve
                    b "{i} (keren) {/i}"
                    scene chnight64 with fade
                    c "Ready"
                    scene chnight63 with dissolve
                    c "Mengapa Anda memerah"
                    scene chnight65 with dissolve
                    c "Jangan malu [bname]"
                    b "SAYA..."
                    c "Saya dapat menunjukkan lebih banyak jika Anda"
                    b "Jika saya apa?"
                    c "Jika Anda ceritakan lebih banyak tentang [mname] bekerja"
                    menu:
                        "Tapi aku sudah memberitahumu segalanya":
                            b "Tapi saya katakan semua yang saya tahu"
                            c "Hmm alright"
                            c "Thanks"
                            scene chnight66 with dissolve
                            c "Selamat malam sayang"
                            b "Selamat malam"
                            "Ini adalah satu -satunya pilihan untuk versi ini"
                            pass
        else:






            c "Hmm begitu, ok selamat malam"
            pass



    scene chnight10 with fade
    b "Dia pergi"
    m "Yes"
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
                    scene chnight42a with fade
                    m "..."
                    scene chnight43a with dissolve
                    m "Mudah..."
                    scene chnight44a with dissolve
                    m "[bname]"
                    scene chnight45a with dissolve
                    $ persistent.unlock_35 = True
                    m "Ahh"
                    scene chnight46a with dissolve
                    m "Stewart !!!"
                    scene chnight47a with dissolve
                    b "Oh fuck!"
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
