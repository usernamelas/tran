label sroom_day_photos:
    scene sd_photos with fade
    s "Jadi?"
    b "Saya berpikir mungkin kita bisa mengambil foto di meja ini untuk perubahan"
    s "Ya, kami bisa mencoba"
    b "Kemarilah, bersandar di sisi meja"
    scene sd_photos1 with dissolve
    s "Ok dan ...?"
    menu:
        "Tetap seperti Anda":
            scene sd_photos1 with dissolve
            b "Perfect"
            "..."
            s "Cukup untuk hari ini [bname]"
            b "Apa-apaan!"
            b "Hanya satu foto?"
            s "Ya saya telah berubah pikiran"
            if bcaught_s == 1 and b_fightback == 0:
                $ b_fightback = 1
                s "Selain itu, Anda berhutang uang kepada saya!"
                b "Uang apa?"
                s "Saya membutuhkannya"
                b "Untuk apa?"
                s "Tidak ada, saya hanya butuh $ 100"
                b "Ha!"
                b "Yeah right"
                b "Saya tidak punya uang"
                b "Ayo, saya pikir Anda tidak akan pergi!"
                scene sd_photos7 with dissolve
                s "Ya pasti ... tapi ..."
                s "Ada sesuatu yang ingin saya tunjukkan untuk Anda berhati -hati di lain waktu"
                s "Seseorang mungkin melihatmu"
                b "Hah! Apa itu?"
                scene etv_cbw with dissolve
                s "Ini"
                b "Hah!"
                scene sd_photos8 with dissolve
                s "Anda tahu [bname] saya bagus"
                if persistent.patch_enabled:
                    s "Dan Anda tahu bahwa saya tidak akan menunjukkan ini kepada ibu"
                    pass
                else:
                    s "Dan Anda tahu bahwa saya tidak akan menunjukkan ini kepada [mname]"
                    pass
                s "Tetapi Anda juga harus baik kepada saya sebagai balasannya"
                menu:
                    "Beri dia uang":
                        b "Biarkan saya melihat apa yang saya miliki"
                        if mny >=100:
                            $ go_counter -= 2
                            b "Di sini ambillah"
                            s "Terima kasih !!"
                            b "{i}(Fuck){/i}"
                            scene broom_day with fade
                            call screen gnav
                        else:
                            b "Saya tidak memilikinya sekarang"
                            b "Aku akan memberimu nanti"
                            s "Ok lihat ya!"
                            $ go_counter += 1
                            b "{i}(Fuck){/i}"
                            scene broom_day with fade
                            call screen gnav
                    "Saya tidak punya uang":

                        $ go_counter += 2
                        s "OK"
                        b "{i}(Fuck it){/i}"
                        scene broom_day with fade
                        call screen gnav


            elif b_fightback == 1:
                b "Apa -apaan!"
                scene sd_photos8 with dissolve
                s "Jangan lupa uang atau hadiah saya jika Anda mau"
                menu:
                    "Beri dia uang":
                        b "Biarkan saya melihat apa yang saya miliki"
                        if mny >=100:
                            $ go_counter -= 2
                            b "Di sini ambillah"
                            s "Terima kasih !!"
                            b "{i}(Fuck){/i}"
                            scene broom_day with fade
                            call screen gnav
                        else:
                            b "Saya tidak memilikinya sekarang"
                            b "Aku akan memberimu nanti"
                            $ go_counter += 1
                            s "Ok"
                            b "{i}(Fuck){/i}"
                            scene broom_day with fade
                            call screen gnav
                    "Saya tidak punya uang":

                        $ go_counter += 2
                        s "OK"
                        b "{i} (...) {/i}"
                        scene broom_day with fade
                        call screen gnav

            elif b_fightback == 2:
                scene sd_photos8 with fade
                s "Jangan lupakan uang saya"
                b "Tidak Ada Lagi Uang Sayang"
                s "Hehe, ok baik"
                b "Saya juga punya foto"
                scene nbr_k3_bw with dissolve

                "..."
                scene sd_photos9 with dissolve
                s "Errr"
                b "Sampai jumpa nanti sayang"
                scene broom_day with fade
                b "{i} (gotcha!) {/i}"
                call screen gnav
            else:
                pass
            b "{i}(Fuck it){/i}"
            scene broom_day with fade
            b "{i} (aku bersumpah dia tidak normal) {/i}"
            b "{i} (kadang -kadang dia hanya membentak) {/i}"
            "Itu semua dalam opsi ini"
            call screen gnav
        "Mengapa Anda tidak menghapus bikini?":

            s "Apa!?"
            b "Ya, saya akan mengambil tanpa wajah"
            b "Pastikan Anda memalingkan muka dari kamera"
            if srel >=100:
                scene sd_photos2 with fade
                b "Yang bagus"
                scene sd_photos3 with dissolve
                s "Saya pikir itu cukup untuk hari ini"
                b "Bisakah kita mengambil satu lagi?"
                if srel >=110:
                    s "Hanya satu!"
                    b "Yes"
                    b "Saya akan mengambil sedikit dari sisi atas"
                    b "Tetap di tempat Anda berada"
                    scene sd_photos4 with dissolve
                    b "Jangan lihat aku"
                    b "Saya tidak ingin menunjukkan wajah Anda"
                    s "Ok"
                    scene sd_photos5 with dissolve
                    b "Perfect"
                    s "Itu saja, tidak lebih"
                    scene sd_photos6 with dissolve
                    s "Sampai jumpa"
                    b "Ok"
                    scene broom_day with fade
                    b "{i} (dia tidak masuk akal, satu menit dia baik -baik saja, yang lain dia menutupi) {/i}"
                    b "{i} (suatu hari nanti saya akan menghapus semua hambatannya) {/i}"
                    call screen gnav
                else:

                    s "No"
                    b "Ok"
                    b "Sampai jumpa"
                    scene broom_day with fade
                    "..."
                    call screen gnav
            else:

                s "Maaf [bname] Saya tidak bisa melakukannya"
                b "Mengapa? Tapi kami melakukannya sebelumnya"
                s "Saya tidak suka"
                b "{i} (apa -apaan) {/i}"
                s "Tolong pergi sekarang"
                b "Ok"
                "Naikkan poin Anda menjadi 100"
                scene broom_day with fade
                "..."
                call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc