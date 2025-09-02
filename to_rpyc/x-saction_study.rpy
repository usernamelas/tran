label saction_study:
    scene sacts with fade
    b "Hey there"
    "..."
    b "Hei, apa yang salah?"
    scene sroom_st1s with dissolve
    s "Saya tidak ingin belajar"
    s "Tolong tinggalkan aku sendiri"
    b "Ayo!"
    b "Dia hanya mengkhawatirkan nilai Anda"
    s "Please go"
    b "Mengapa Anda sangat kesal tentang hal itu"
    b "Ayo kita belajar sebentar dan kemudian kita mengambil beberapa gambar"
    scene sroom_st17 with fade
    "..."
    s "Bagaimana dengan ini?"
    b "Biarkan saja"
    if saction >=2:
        jump saction_xx
    else:
        pass
    scene sroom_st18 with dissolve
    b "Lihat hasilnya"
    s "Ya itu benar"
    b "Hebat, waktu untuk mendapatkan beberapa foto sekarang"
    scene sroom_st19 with dissolve
    s "[bname] Saya tidak berminat sekarang"
    b "Anda akan berminat saat kami mendapatkan 1000 pengikut"
    if kissrepeat >=1 and instauploads == 1:
        s "Ok tapi tidak lama"
        b "Dingin"
        s "Wait outside"
        scene door with dissolve
        "..."
        s "Anda bisa masuk!"
        if saction ==0:
            jump saction_normal

        elif saction ==1:
            jump saction_hot
    else:

        s "Saya tidak bisa melakukannya sekarang, tolong jangan tanya lebih banyak"
        b "Ok dapatkan"
        b "Sampai jumpa"
        scene black
        "Anda perlu melakukan ciuman dan acara halaman selesai"
        jump broom_menu



label saction_normal:
    scene sacts1 with fade
    b "Hmmm"
    b "Pergi ke dinding"
    scene sacts2 with fade
    "..."
    b "More"
    scene sacts3 with dissolve
    b "Oke, cobalah untuk berbelok"
    scene sacts4 with dissolve
    b "Saya akan mengambil satu dari samping"
    scene sacts5 with dissolve
    b "Hmm"
    b "{i} (itu akan menjadi pose yang bagus untuk ...) {/i}"
    scene sacts6 with fade
    s "Cukup untuk hari ini"
    scene door with fade
    b "{i} (...) {/i}"
    call screen gnav


label saction_hot:
    scene sacts7 with fade
    b "Hmmm"
    b "Mari kita coba beberapa bidikan yang bagus"
    scene sacts8 with fade
    b "Berpura -pura bahwa Anda menghapus kemeja itu"
    scene sacts9 with dissolve
    s "Jangan tunjukkan wajahku"
    b "Ok"
    scene sacts10 with dissolve
    "..."
    scene sacts11 with dissolve
    b "{i}(Oh yeah){/i}"
    scene sacts12 with dissolve
    b "Oh demi keparat, aku sudah melihatnya"
    "..."
    b "Oke, mari kita ambil satu dari samping"
    scene sacts13 with fade
    b "Ya bagus"
    b "Beralihlah ke saya"
    scene sacts14 with dissolve
    s "I don't want to show more [bname]"
    s "Anda harus memahami ini"
    b "Nah kenapa tidak? Kami Membutuhkan Pengikut Ingat"
    b "Pikirkan seperti bisnis, segera kita akan menjadi kaya"
    s "Jika itu masalahnya, maka lakukan di halaman Anda"
    b "Saya akan melakukannya"
    b "Ini teleponnya, ambil foto saya, saya tidak peduli"
    scene sacts15 with fade
    b "Kunci pintu terlebih dahulu"
    s "Yep"
    scene sacts16 with fade
    s "Done"
    menu:
        "Lepaskan semuanya":
            scene sacts17 with dissolve
            s "..."
            scene sacts16 with dissolve
            s "..."
            scene sacts18 with dissolve
            s "Apakah kamu serius?"
            s "Keluar!"
            b "Apa -apaan"
            scene door with fade
            b "{i} (...) {/i}"
            call screen gnav
        "Berpose berpakaian":

            scene sacts19 with dissolve
            "..."
            scene sacts20 with dissolve
            "..."
            b "Enough"
            scene sacts16 with dissolve
            b "Mari \ memposting foto Anda sekarang"
            scene sacts21 with fade
            b "Saya perlu mengeditnya untuk memotong kepala Anda terlebih dahulu"
            b "Saya kira saya akan melakukannya di kamar saya"
            s "..."
            b "Saya akan menunjukkannya kepada Anda sebelum saya memposting"
            s "Ok cukup adil"
            b "{i} (dia sangat naif tidak menyadari bahwa itu akan menjadi jelas bahwa itu adalah fotonya) {/i}"
            b "{i} (dengan foto normalnya di seluruh halaman) {/i}"
            b "Sampai jumpa lagi"
            scene door with fade
            b "{i} (...) {/i}"
            call screen gnav


label saction_xx:
    scene sacts23 with fade
    m "Saya harap Anda belajar dan tidak melakukan hal ini"
    b "Ya kita"
    m "Show me"
    scene sacts22 with dissolve
    b "Anda lihat"
    m "Hmmm"
    m "Tunjukkan halaman yang Anda buat"

    scene sacts24 with dissolve
    b "Ini dia"
    b "Ini adalah halaman penggemar tentang gulat"
    m "Hmm ok, lanjutkan studi Anda"
    b "Jangan khawatir dia akan lewat dengan warna terbang"
    m "Ok bagus, sampai jumpa nanti"
    scene sroom_st18 with fade
    b "Lihat hasilnya"
    s "Ya itu benar"
    b "Hebat, waktu untuk mendapatkan beberapa foto sekarang"
    scene sroom_st19 with dissolve
    s "[bname] Saya tidak berminat sekarang"
    b "Anda akan berminat saat kami mendapatkan 1000 pengikut"
    b "Selain itu, saya baru saja menyelamatkan pantat Anda beberapa saat yang lalu"
    if kissrepeat >=1 and instauploads == 1 and srel >= 50:
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
        if persistent.patch_enabled:
            b "Dengar, aku baru saja menyelamatkanmu dengan ibu"
            b "Setidaknya bersyukur dan percayalah"
            pass
        else:
            b "Dengar, aku baru saja menyelamatkanmu dengan [mname]"
            b "Setidaknya bersyukur dan percayalah"
            pass
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
        if srel >= 90:
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
                "Pokoknya saya memutuskan untuk menambahkan pos pemeriksaan yang sama di tempat yang berbeda untuk pemain"
                "Untuk memiliki lebih banyak opsi untuk maju dengan [sname]"
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
                                $ sactiondone_nomast = 1
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
                            "Jangan memberitahunya":

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
        else:

            s "Tidak [bname] Saya tidak merasa baik -baik saja"
            b "All right"
            b "Let's continue"
            scene sacts31 with fade
            "..."
            s "Cukup untuk hari ini [bname]"
            b "Ok"
            b "Lihat yah"
            scene door with fade
            b "{i} (Saya membutuhkan lebih dari 90 poin hubungan) {/i}"
            call screen gnav
    else:


        s "Saya tidak bisa melakukannya sekarang, tolong jangan tanya lebih banyak"
        b "Ok dapatkan"
        b "Sampai jumpa"
        scene black
        "Anda perlu memiliki ciuman dan acara halaman dan hubungan lebih tinggi dari 50"
        jump broom_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc