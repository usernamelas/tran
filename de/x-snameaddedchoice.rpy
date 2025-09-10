label snameaddedchoice:
    s "Ok"
    b "Dingin"
    s "Wait outside"
    scene door with dissolve
    "..."
    s "Anda bisa masuk!"
    scene sacts25 with fade
    b "Oh keren"
    b "Mari kita coba beberapa foto telanjang yang bagus"
    s "Telanjang! TIDAK!"
    b "Kami sudah hampir telanjang"
    s "Tidak ada barang mesum, oke?"
    $ hotphotos_done = 1
    b "Yes sure"
    scene sacts26 with fade
    b "Oh please"
    b "Lepaskan tangan Anda"
    s "TIDAK!"
    b "Ayo, Anda harus mempercayai saya"
    scene sacts27 with dissolve
    "..."
    scene sacts28 with dissolve
    "..."
    menu:
        "Mengapa Anda tidak menghapus celana dalam?":
            s "TIDAK!"
            b "[sname] !! Kami mengunjungi pantai telanjang, dan saya telah melihat hampir segalanya"
            b "Saya akan mengambil foto dari samping"
            pass
        "Menghidupkan":

            b "Saya akan mengambil foto dari samping"
            pass

    scene sacts29 with fade
    "..."
    b "Mengapa Anda tidak melepas celana dalam?"
    scene sacts30 with dissolve
    s "Apa?"
    b "Saya akan mengunci pintu, jika itu membuat Anda merasa lebih baik"
    s "Itu terkunci, dan itu tidak membuat saya merasa lebih baik"
    b "Saya akan melepas bajuku, jika itu terjadi"
    b "Demi Tuhan, ayo, saya hanya akan mengambil dari sisi ini"
    s "Hmm"
    b "Jangan lupa bahwa saya membantu Anda beberapa saat yang lalu"
    s "Oke berbalik"
    b "Ok"
    scene sacts32 with dissolve
    "..."
    s "Anda dapat mengambil foto sekarang"
    scene sacts33 with dissolve
    "..."
    s "Apa?"
    s "Apakah Anda benar -benar melepas bajumu?"
    scene sacts34 with dissolve
    "..."
    b "Yeah"
    s "Anda benar -benar cabul"
    s "Saya tidak percaya saya melakukan ini"
    b "Oh tutup mulut, biarkan aku mengambil lebih banyak foto"
    b "Ini akan menyapanya"
    scene sacts35 with dissolve
    s "Menyapu apa?"
    b "Pengikut, dan uang"
    b "Ayo, mari kita lanjutkan"
    s "Saya tidak merasa seperti itu"
    b "Mengapa?"
    s "Saya tidak ingin membayangkan apa yang akan Anda lakukan di malam hari mengedit foto -foto itu"
    b "Oh ya, saya ingin membayangkan"
    if scorr >= 35:
        s "..."
        scene sacts37 with dissolve
        s "Bayangkan apa?"
        "Pilihan berikutnya sangat penting untuk dipajukan dengan [sname], simpan di sini untuk diputar ulang"
        menu:
            "Banyak hal yang bisa terjadi saat saya sendirian dengan foto -foto seperti itu":
                scene sacts38 with dissolve
                s "Seperti apa?"
                b "Ehmm"
                scene sacts39 with dissolve
                b "Apakah Anda yakin ingin tahu?"
                s "Saya hanya penasaran"
                menu:
                    "Katakan padanya":
                        b "Saya akan melakukannya"
                        scene sacts41 with dissolve
                        b "Seperti ini"
                        s "Hah!"
                        s "..."
                        b "Jadi?"
                        s "Ya, saya sudah mengerti maksud Anda"
                        s "Saya perlu tidur siang"
                        b "Ah Ok"
                        b "Sampai jumpa"
                        b "{i} (terlalu banyak) {/i}"
                        scene door with fade
                        b "{i} (...) {/i}"
                        call screen gnav
                    "Jangan katakan padanya*":

                        b "Aku tidak bisa memberitahumu"
                        scene sacts42 with dissolve
                        s "Mengapa?"
                        b "Ada hal -hal yang tidak bisa diberitahu"
                        scene sacts43 with dissolve
                        s "Hmm"
                        $ sactiondone_mast = 1
                        s "Baiklah, saya harus berdandan, tolong pergi"
                        b "Sampai jumpa"
                        b "{i} (terlalu banyak) {/i}"
                        scene door with fade
                        b "{i} (...) {/i}"
                        call screen gnav
            "Maksud saya, saya ingin menikmati kecantikan saat saya mengerjakan foto Anda":

                scene sacts38 with dissolve
                s "Hmm"
                $ sactiondone_mast = 1
                scene sacts44 with dissolve
                s "Baiklah, saya harus berdandan, tolong pergi"
                b "Sampai jumpa"
                b "{i} (terlalu banyak) {/i}"
                scene door with fade
                b "{i} (...) {/i}"
                call screen gnav
    else:
        s "Keluar!"
        s "Pervert"
        b "Apakah kamu serius?"
        s "Ya, tolong pergi"
        b "Dan bagaimana jika saya tidak"
        scene sacts36 with vpunch
        s "Lalu aku akan membunuhmu"
        b "Woah ..."
        b "Oke, kami akan melanjutkan lain kali"
        b "Lihat yah"
        scene door with fade
        b "{i} (Saya membutuhkan lebih dari 35 poin korupsi) {/i}"
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
