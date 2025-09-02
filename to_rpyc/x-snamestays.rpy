label snamestays:
    scene mstripst15 with dissolve
    m "Terima kasih telah tinggal bersamaku"
    scene mstripst16 with dissolve
    m "..."
    scene mstripst17 with dissolve
    s "{i}(Hmm){/i}"
    scene mstripst18 with dissolve
    s "Semuanya akan baik -baik saja"
    scene mstripst19 with dissolve
    "..."
    scene mstripst20 with dissolve
    $ persistent.unlock_52 = True
    m "Ahh"
    scene mstripst21 with fade
    m "Apa yang sedang kamu lakukan?"
    s "Aku akan menjagamu"
    scene mstripst22 with dissolve
    "..."
    scene mstripst23 with dissolve
    m "Ah Tuhan!"
    scene mstripst24 with dissolve
    m "Ah"
    scene mstripst25 with dissolve
    s "{i} (mhhm dia berbau harum) {/i}"
    scene mstripst26 with fade
    m "Mhhm aku mencintaimu [sname]"
    m "Enough please"
    s "Not enough"
    scene mstripst27 with fade
    s "Ahh"
    scene mstripst28 with dissolve
    "..."
    scene mstripst29 with dissolve
    s "..."
    scene mstripst29a with hpunch
    s "Ahhh"
    scene msms
    s "Mmmm"
    "..."
    m "..."
    s "Mhm"
    "..."
    scene mstripst30 with fade
    s "Good night"
    jump newdays

label snamegoestost:
    if msho ==1:
        $ msho = 2
        pass
    else:
        pass
    scene stst27 with fade
    if persistent.patch_enabled:
        s "Ayah!"
        pass
    else:
        s "Seh!"
        pass
    d "Senang bertemu denganmu [sname]"
    scene stst28 with dissolve
    s "Dimana dia?"
    d "Dimana siapa?"
    s "Di mana Anda menyembunyikannya saat ini?"
    d "Siapa?"
    s "Ayo!"
    d "[sname] Saya tidak menyukai nada ini"
    if persistent.patch_enabled:
        s "Anda tahu, Anda dan ibu sama"
        pass
    else:
        s "Anda tahu, Anda dan [mname] sama"
        pass
    scene stst29 with dissolve
    d "Apa maksudmu?"
    s "Apa yang Anda lakukan yang juga dia lakukan"
    d "Huh"
    s "Ya saya juga tidak senang tentang hal itu"
    s "Itulah mengapa saya membutuhkan bantuan Anda"
    scene stst30 with dissolve
    "Dia terisak"
    d "Hei tenang, apa yang salah?"
    scene stst31 with dissolve
    s "Kami membutuhkan Anda bersama kami"
    s "Kita tidak bisa melanjutkan seperti ini"
    d "Hei oke, santai saja"
    d "Saya akan melakukan sesuatu"
    scene stst32 with dissolve
    s "Benar-benar?"
    d "Yes"
    s "Saya juga butuh uang, [mname] tidak memberi saya apapun"
    d "Jangan khawatir, aku akan memberimu beberapa"
    d "Cuci wajah Anda"
    s "Ok"
    scene stst33 with dissolve
    d "Dan bersiaplah saya akan memesan taksi untuk Anda"
    s "Tidak perlu saya memutuskan untuk tidur di sini"
    d "Tetapi..."
    s "Saya merindukan kamar saya"
    scene black
    "Malam itu"
    scene stst34 with fade
    s "Hmm"
    s "{i} (i \ 'll kembali lagi nanti) {/i}"
    s "{i} (jika [mname] melakukan omong kosong ini, saya bisa melakukannya juga) {/i}"
    scene stst35 with fade
    s "Hey"
    d "Huh"
    s "Apa yang sedang kamu lakukan?"
    scene stst36 with dissolve
    d "Akan tidur"
    d "Sudah terlambat dan saya punya pekerjaan"
    s "Bisakah saya tidur di sini, seperti masa lalu yang indah"
    d "[sname] Anda sudah tua sekarang, tidak sama"
    scene stst37 with dissolve
    s "Ya, tapi saya bisa tidur di sana"
    s "Di tempat tidur sofa"
    d "Baik, tapi saya benar -benar perlu tidur"
    scene stst38 with dissolve
    s "Tunggu jangan mematikan lampu"
    d "I'm not"
    d "Buka tempat tidur terlebih dahulu"
    s "Tunggu sebentar"
    scene stst39 with dissolve
    d "Huh"
    d "Saya akan mematikan lampu"
    s "Wait"
    scene black
    d "Maaf saya tidak bisa, mengelola"
    s "Ok saya masih bisa melihat"
    d "Good night"
    s "Good night"
    scene stst40 with fade
    "Nanti di malam hari"
    scene stst41 with dissolve
    d "Hah! [sname] Apa?"
    s "Bisakah saya tidur di sini?"
    s "Saya merindukan masa lalu saat Anda memperlakukan saya seperti putri Anda"
    d "Ya tapi ..."
    s "Apa? Apakah aku bukan putrimu lagi?"
    d "Anda, tapi sekarang berbeda"
    d "Anda terlalu tua sekarang"
    s "Tidak, bukan itu lagi, kamu tidak peduli padaku lagi"
    d "[sname] Anda adalah seorang wanita sekarang, jangan Anda mengerti!?"
    s "Saya bersedia..."
    s "Itulah mengapa ..."
    scene stlove
    d "Oh God"
    d "Stop"
    scene stlove177 with dissolve
    d "Ini tidak benar"
    d "Apa yang kamu lakukan?"
    s "Itulah yang saya lakukan"
    scene stst42 with dissolve
    if persistent.patch_enabled:
        d "Wow! Apa -apaan!"
        s "Please daddy"
        d "Apa?"
        s "Biarkan saya melihatnya"
        pass
    else:
        d "Wow! Apa -apaan!"
        s "Tolong biarkan saya melihatnya"
        pass
    menu:
        "Dia akan mengizinkannya":
            d "Ok hanya mengintip"
            scene stst44 with dissolve

            s "Mmmm"
            scene stst45 with fade
            "..."
            scene stst46 with dissolve
            s "..."
            scene stst47 with dissolve
            "..."
            scene stst48 with dissolve
            "..."
            scene stst49 with dissolve
            "..."
            scene stst50 with dissolve
            s "..."
            scene stst51 with dissolve
            s "..."
            scene stst52 with dissolve
            s "Hehehe"
            s "Ah saya baik atau tidak?"
            d "You are"
            d "Maksudku itu tidak relevan"
            s "Tolong dapatkan ke samping"
            s "Biarkan saya menunjukkan tarian saya"
            scene dste00 with fade
            d "Apakah kamu yakin itu tarian?"
            s "Ya percayalah"
            $ persistent.unlock_54 = True
            "Anda dapat menekan H untuk melihat animasi lengkap"
            scene dste
            "..."
            d "Ahh"
            "..."
            s "..."
            scene stst53a with vpunch
            d "Come here"
            scene stst53 with fade
            "..."
            scene stst54 with dissolve
            s "Apa rasanya seperti itu?"
            d "Apakah ini pertama kali Anda merasakan ini?"
            s "Yes"
            scene stst55 with dissolve
            d "Swallow, kamu akan baik -baik saja"
            s "..."
            scene stst56 with fade

            if persistent.patch_enabled:
                s "Selamat malam Ayah"
                pass
            else:
                s "Good night"
                pass
            d "Selamat malam, saya harus tidur"
            d "Saya memiliki pekerjaan awal besok"
            d "Saya akan menyimpan uang untuk Anda di atas meja"
            s "Thank you"
            jump newdays
        "TIDAK":

            d "No way"
            scene stst43 with dissolve
            s "Membosankan!"
            d "Pergi tidur sekarang"
            s "Good night"
            jump newdays


label snamegoestost1:
    if msho ==1:
        $ msho = 2
        pass
    else:
        pass
    scene stst27 with fade
    if persistent.patch_enabled:
        s "Ayah!"
        pass
    else:
        s "Seh!"
        pass
    d "Senang bertemu denganmu lagi [sname]"
    scene stst28 with dissolve
    s "Dimana dia?"
    d "Dimana siapa?"
    s "Di mana Anda menyembunyikannya saat ini?"
    d "Siapa?"
    s "Ayo!"
    d "[sname] Saya tidak menyukai nada ini"
    scene stst29 with dissolve
    s "Ok"
    s "Jadi bisakah saya tidur di sini lagi?"
    d "Yes"
    scene stst33 with dissolve
    d "Tapi apakah [mname] OK dengan itu?"
    s "Jangan khawatir tentang dia"
    d "Tetapi..."
    s "Saya merindukan kamar saya"
    scene black
    "..."
    scene stst35 with fade
    s "Hey"
    d "Huh"
    s "Apa yang sedang kamu lakukan?"
    scene stst36 with dissolve
    d "Akan tidur"
    d "Sudah terlambat dan saya punya pekerjaan"
    s "Ok"
    scene stst56 with fade
    s "Apa yang kamu tidur secepat ini?"
    d "Saya lelah [sname] Saya mengadakan pertemuan di pagi hari"
    s "Mari kita lihat tentang itu"
    scene stst44 with dissolve
    s "Mhmm"
    if persistent.patch_enabled:
        s "Please daddy"
        pass
    else:
        s "Silakan!"
        pass
    menu:
        "Dia akan mengizinkannya":
            scene smbj
            "..."
            d "Ah"
            "..."
            s "..."
            d "Ahh"
            d "Wait"
            pass
        "TIDAK":
            d "No way"
            scene stst43 with dissolve
            s "Membosankan!"
            d "Pergi tidur sekarang"
            s "Good night"
            jump newdays

    "..."
    menu:
        "Dia akan menciumnya":
            scene stst57 with dissolve
            "..."
            scene stst58 with dissolve
            s "Mmm"
            scene stst59 with dissolve
            s "Ahhh"
            scene stst60 with dissolve
            "..."
            scene stst61 with dissolve
            "..."
            scene stst62 with dissolve
            d "Hmm"
            scene stst56 with fade
            if persistent.patch_enabled:
                s "Selamat malam Ayah"
                pass
            else:
                s "Good night"
                pass
            d "Selamat malam, saya harus tidur"
            d "Saya memiliki pekerjaan awal besok"
            d "Saya akan menyimpan uang untuk Anda di atas meja"
            s "Thank you"
            jump newdays
        "Dia akan membiarkan dia melakukan apa yang dia inginkan":

            pass

    scene dste
    "..."
    d "Ahh"
    "..."
    s "..."
    scene stst53a with vpunch
    d "Come here"
    scene stst53 with fade
    "..."
    scene stst54 with dissolve
    s "Apa rasanya seperti itu?"
    d "Apakah ini pertama kali Anda merasakan ini?"
    s "Yes"
    scene stst55 with dissolve
    d "Swallow, kamu akan baik -baik saja"
    s "..."
    scene stst56 with fade
    if persistent.patch_enabled:
        s "Selamat malam Ayah"
        pass
    else:
        s "Good night"
        pass
    d "Selamat malam, saya harus tidur"
    d "Saya memiliki pekerjaan awal besok"
    d "Saya akan menyimpan uang untuk Anda di atas meja"
    s "Thank you"
    jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc