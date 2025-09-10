define dn = Character("Daniel")


label map_menu:
    if Hour >=9 and Hour <18:
        if bworkstarted == 1 and bworked == 0 and bikini1 >= 1 and bikini2 >=1:
            scene cityd with fade
            "..."
            menu:
                "Pergi bekerja untuk Daniel":
                    $ bworked = 1
                    $ Hour += 2
                    jump bworkday

                "Mari kita lihat mungkin saya bisa memeriksa [mname]" if startnework >= 1 and elaine_convince == 4 and Hour >=10 and day !=7:
                    jump workvisitday

        elif startnework >= 1 and Hour >=10 and bikini1 >= 1 and bikini2 >=1 and day !=7:
            b "Hmm"
            b "Mungkin saya bisa mengunjungi [mname] tempat baru"
            jump workvisitday

        elif startnework >= 1 and Hour >=10 and elaine_convince == 4 and mrel >=250 and day !=7:
            b "Hmm"
            b "Mungkin saya bisa mengunjungi [mname] tempat baru"
            jump workvisitday
        else:
            pass
        scene cityd with fade
        "..."
        scene cityd2 with dissolve
        b "{i} (Let \ 's lihat toko cleaners ini) {/i}"
        scene cityd3 with dissolve
        b "Keluar dari sini Anda bajingan kecil"
        b "{i} (apa -apaan!) {/i}"
        scene cityd1 with fade
        b "{i} (mungkin saya bisa bertanya di toko gadget ini) {/i}"
        if beach >=1 and cellshop ==1 and ebizaldoneonce == 0:
            scene cityd4d with dissolve
            b "..."
            dn "Hi"
            $ meldan = 1
            scene cityd5d with dissolve
            b "Hi"
            dn "Apakah Anda ingin membeli telepon?"
            b "Err Tidak, saya ingin berbicara dengan pemilik toko ini, apakah dia di sini?"
            dn "Saya pemiliknya"
            b "Tapi terakhir kali saya bertemu pria yang berbeda di sini"
            dn "Ah, maksudmu pasanganku, ya"
            dn "Kami berdua pemilik toko ini"
            b "Ummm jadi, saya sedang mencari pekerjaan paruh waktu"
            b "Apakah Anda membutuhkan seseorang?"
            dn "Saya \ M ALA SAJA TIDAK SAAT INI"
            dn "Bisnis lambat saat ini"
            dn "Anda dapat kembali dan memeriksa versi berikutnya"
            b "Oh! Oke"
            b "Terima kasih, saya akan pergi sekarang"
            "..."
            jump broom_menu


        elif meldan >= 1 and ebizaldoneonce == 1:
            if skiss_asked == 1 and pagecheck >=1 and instauploads >=1 and bworkstarted ==0:
                scene cityd3d with fade
                dn "Semoga harimu menyenangkan"
                scene cityd4d with dissolve
                b "..."
                dn "Hi there"
                $ bworkstarted = 1
                dn "Ia!"
                scene cityd5d with dissolve
                b "Oh hi"
                b "Jadi ... sesuatu yang baru dengan pekerjaan paruh waktu saya?"
                dn "Err sebenarnya ya"
                b "Dingin"
                dn "Bisakah Anda memperbaiki ponsel?"
                b "Dengan baik..."
                dn "Ini hal reparasi dasar"
                dn "Changing batteries"
                dn "Kliping pelindung layar"
                b "Ya tentu saja, saya bisa melakukan itu"
                dn "Saya memiliki telepon di sini, dapatkah Anda mengubah pelindung layar?"
                b "Sure"
                scene cityd6d with fade
                b "Done"
                scene cityd7d with dissolve
                dn "Hebat, kunjungi saat Anda punya waktu"
                dn "Saya akan membayar Anda $ 100 untuk setiap sesi reparasi"
                b "Keren, terima kasih"
                "..."
                jump broom_menu
            else:

                pass
            scene cityd4 with dissolve
            b "Bagus"
            "Hai"
            scene cityd5 with dissolve
            b "Hi"
            "Bagaimana saya bisa membantu?"
            $ cellshop = 1
            b "Ummm, saya sedang mencari pekerjaan paruh waktu"
            "Apakah Anda tahu tentang ponsel?"
            b "Yes"
            "Bagus, tapi saya minta maaf saya tidak perlu saat ini"
            "Anda bisa kembali dan memeriksa nanti"
            b "Oh! Oke"
            "Maaf bro!"
            b "{i} (apa -apaan!) {/i}"
            if instadone == 2 and bikini1 == 0:
                b "{i} (mungkin saya bisa memeriksa gaun yang bagus untuk pemotretan [sname] ) {/i}"
                scene btique with fade
                "Bagaimana saya bisa membantu Anda?"
                b "Hmm"
                b "{i} ([sname] suka bikini, jadi ...) {/i}"
                b "Dapatkah saya melihat bikini apa yang Anda miliki?"
                "Berapa ukurannya?"
                b "Tiny"
                "Ha ha"
                "Ok saya akan mendapatkan sesuatu"
                scene sbikini with fade
                "Kami memiliki ini untuk saat ini"
                "Yang di sebelah kanan adalah preorder"
                b "Ahh, tidak bisa menunggu itu"
                b "Saya akan mengambil apa yang tersedia"
                "$ 50 tolong"
                if mny>=50:
                    b "Ini dia"
                    $ bikini1 = 1
                    $ mny -= 50
                    scene btique with dissolve
                    "Sampai jumpa"
                    jump broom_menu
                else:


                    b "Sial, ini mahal"
                    b "Maaf saya tidak punya jumlah ini sekarang"
                    b "Saya akan kembali lagi nanti"
                    scene btique with dissolve
                    "Tidak masalah"
                    "Sampai jumpa"
                    jump broom_menu

            elif bikini1 ==2:
                jump sclothes
            else:

                jump broom_menu
        else:

            scene cityd4 with dissolve
            b "Bagus"
            "Hai"
            scene cityd5 with dissolve
            b "Hi"
            "Bagaimana saya bisa membantu?"
            $ cellshop = 1
            b "Ummm, saya sedang mencari pekerjaan paruh waktu"
            "Apakah Anda tahu tentang ponsel?"
            b "Yes"
            "Bagus, tapi saya minta maaf saya tidak perlu saat ini"
            "Anda bisa kembali dan memeriksa nanti"
            b "Oh! Oke"
            "Maaf bro!"
            jump broom_menu




    elif Hour >=18 and Hour <22:
        if Hour ==18 and melsw >=9:
            jump workvisitnight
        scene cityn with fade
        b "{i} (let \ 's lihat ...) {/i}"
        scene cityn1 with dissolve
        b "{i} (...) {/i}"
        b "{i} (toko kosong dan tertutup) {/i}"
        if robel ==0:
            scene cityn2 with fade
            "Biarkan aku pergi Rob!"
            r "Apa yang dia katakan?"
            "Merampok! Demi Tuhan dia adalah klien, dia bisa berbicara dengan saya!"
            "Tolong biarkan aku pergi"
            $ robel = 1
            b "{i} (apa -apaan) {/i}"
            scene cityn3 with dissolve
            b "{i} (i \ 'D lebih baik kembali ke rumah) {/i}"
            jump broom_menu
        else:
            if cselaine0 ==8:
                menu:
                    "Pergi beritahu Elaine dia bisa datang besok":
                        scene cityn3 with fade
                        b "..."
                        scene cityn4 with dissolve
                        b "Hi"
                        r "Hi [bname]"
                        b "Saya perlu melihat Elaine"
                        b "Saya punya pesan untuknya dari [mname]"
                        scene cityn5 with dissolve
                        r "Tunggu di sini, aku akan meneleponnya"
                        scene cityn6 with fade
                        e "Hi [bname]"
                        scene cityn7 with dissolve
                        b "[mname] ..."
                        b "Errm"
                        scene cityn8 with dissolve
                        b "Err [mname] mengatakan ..."
                        scene cityn7 with dissolve
                        b "... dia pergi ke bioskop besok"
                        e "Aha, oke, katakan padanya aku akan pergi bersamanya"
                        b "Dingin"
                        e "Saya harus pergi, terima kasih [bname]"
                        e "SMS saya jika Anda membutuhkan sesuatu yang baik -baik saja!"
                        b "Sure"
                        scene cityn9 with dissolve
                        "..."
                        if mny <50:
                            b "{i} (fuck, saya tidak punya uang untuk membeli tiket untuk [mname] dan [sname]) {/i}"
                            b "Ah, saya lupa"
                            e "Yes [bname]"
                            scene cityn7 with dissolve
                            b "Hmm ... bisakah saya meminjam uang?"
                            e "Oh tentu"
                            e "Berapa banyak yang Anda inginkan?"
                            b "Saya tidak tahu, 0?"
                            scene cityn10 with dissolve
                            e "Here"
                            e "Mengambil"
                            $ mny += 50
                            scene cityn7 with dissolve
                            b "Thanks"
                            b "Sampai jumpa..."
                            scene cityn11 with dissolve
                            e "Pria kecil yang malang"
                            e "Dia datang ke sini untuk mendapatkan uang"
                            scene cityn12 with fade
                            "..."
                            b "{i} (sekarang adalah waktu untuk membeli tiket bioskop) {/i}"
                            menu:
                                "Beli Tiket untuk Pertunjukan Besok":
                                    if workrequest ==3:
                                        scene citycinema with fade
                                        b "{i} (Saya harus membeli satu tiket untuk [sname] karena [mname] berfungsi) {/i}"
                                        scene citycinema1 with dissolve
                                        b "Bisakah saya mendapatkan 1 tiket untuk film terbaru?"
                                        $ mny -= 25
                                        $ cselaine0 = 9
                                        "Waktu pertunjukan yang mana?"
                                        b "17:00 Pertunjukan"
                                        scene citycinema2 with dissolve
                                        "Di Sini..."
                                        b "Thanks"
                                        b "{i} (Saya harus menelepon Elaine besok pukul 15:00) {/i}"
                                        scene cityn3 with fade
                                        b "{i} (Time to Go Home) {/i}"
                                        jump broom_menu
                                    else:

                                        pass
                                    scene citycinema with fade
                                    "..."
                                    scene citycinema1 with dissolve
                                    b "Bisakah saya mendapatkan 2 tiket untuk film terbaru?"
                                    $ mny -= 50
                                    $ cselaine0 = 9
                                    "Waktu pertunjukan yang mana?"
                                    b "17:00 Pertunjukan"
                                    scene citycinema2 with dissolve
                                    "Di Sini..."
                                    b "Thanks"
                                    b "{i} (Saya harus menelepon Elaine besok pukul 15:00) {/i}"
                                    scene cityn3 with fade
                                    b "{i} (Time to Go Home) {/i}"
                                    jump broom_menu
                                "Tunggu hari lain":

                                    pass
                        else:

                            menu:
                                "Beli Tiket untuk Pertunjukan Besok":
                                    if workrequest ==3:
                                        scene citycinema with fade
                                        b "{i} (Saya harus membeli satu tiket untuk [sname] karena [mname] berfungsi) {/i}"
                                        scene citycinema1 with dissolve
                                        b "Bisakah saya mendapatkan 1 tiket untuk film terbaru?"
                                        $ mny -= 25
                                        $ cselaine0 = 9
                                        "Waktu pertunjukan yang mana?"
                                        b "17:00 Pertunjukan"
                                        scene citycinema2 with dissolve
                                        "Di Sini..."
                                        b "Thanks"
                                        b "{i} (Saya harus menelepon Elaine besok pukul 15:00) {/i}"
                                        scene cityn3 with fade
                                        b "{i} (Time to Go Home) {/i}"
                                        jump broom_menu
                                    else:

                                        pass


                                    scene citycinema with fade
                                    "..."
                                    scene citycinema1 with dissolve
                                    b "Bisakah saya mendapatkan 2 tiket untuk film terbaru?"
                                    "Waktu yang mana?"
                                    $ mny -= 50
                                    $ cselaine0 = 9
                                    b "17:00 Pertunjukan"
                                    scene citycinema2 with dissolve
                                    "Di Sini..."
                                    b "Thanks"
                                    b "{i} (Saya harus menelepon Elaine besok pukul 15:00) {/i}"
                                    scene cityn3 with fade
                                    b "{i} (Time to Go Home) {/i}"
                                    jump broom_menu
                                "Tunggu hari lain":

                                    pass
                    "Tidak perlu sekarang":

                        pass
            else:

                pass
            scene cityn3 with fade
            b "{i} (i \ 'D lebih baik kembali ke rumah) {/i}"
            jump broom_menu
    else:


        scene cityn with fade
        b "{i} (i \ 'D lebih baik kembali ke rumah) {/i}"
        jump broom_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
