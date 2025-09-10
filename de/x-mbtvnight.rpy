label mbtvnight:
    scene broom_night with fade
    b "{i} (apa yang harus dilakukan sekarang?) {/i}"
    menu:
        "Pergi lihat [sname]":
            scene door with fade
            b "{i} (Sepertinya pintu terbuka) {/i}"
            scene mbtvn5 with dissolve
            b "Hai!"
            s "Hi"
            b "Anda terus membaca sepanjang hari?"
            s "Apa masalah Anda?"
            b "Mari bersenang -senang?"
            s "Dan apa yang menyenangkan bagimu?"
            scene mbtvn6 with dissolve
            b "Hmm"
            menu:
                "Mari kita mainkan kebenaran atau berani":
                    scene mbtvn5 with dissolve
                    s "Saya tidak menyukainya"
                    b "WTF!"
                    s "Please go"
                    scene broom_night with fade
                    b "Saya kira sudah waktunya tidur"
                    "Tidak dalam versi ini"
                    jump newdays

                "Mari kita ambil beberapa foto" if pagecheck >=6 and srel >=200:
                    scene mbtvn5 with dissolve
                    s "Ya kenapa tidak"
                    b "Foto panas?"
                    if hotphotos_done ==1:
                        s "Yes"
                        pass
                    elif srel >=300:
                        s "Yes"
                        pass
                    else:

                        s "No [sname]"
                        b "Baiklah, lalu kenakan sesuatu yang bagus"
                        s "Ok"
                        scene sroom_inst_photos_suggestive6 with fade
                        b "Besar"
                        b "More"
                        scene sroom_inst_photos_suggestive7 with dissolve
                        b "Change"
                        scene sroom_inst_photos_suggestive8 with dissolve
                        b "Bagus"
                        scene sroom_inst_photos_suggestive8a with dissolve
                        "..."
                        b "Cobalah sesuatu yang lebih sugestif"
                        scene sroom_inst_photos_suggestive9a with dissolve
                        s "Apakah itu bagus?"
                        b "Apakah hanya itu yang bisa Anda lakukan?"
                        scene sroom_inst_photos_suggestive10a with dissolve
                        s "Please go"
                        b "Apa ...!"
                        s "Saya ingin melanjutkan membaca"
                        b "Anda gila!"
                        b "Bye"
                        scene broom_night with fade
                        b "Saya kira sudah waktunya tidur"
                        jump newdays

                    s "Di mana Anda ingin mengambilnya?"
                    b "Di tempat tidur"
                    scene mbtvn7 with fade
                    s "Bagaimana dengan ini?"
                    b "Bagus tapi tanpa pakaian"
                    s "..."
                    scene mbtvn8 with dissolve
                    s "Dengan serius?"
                    b "Ya, kenapa tidak?"
                    s "..."
                    scene mbtvn9 with fade
                    b "Much better"
                    "..."
                    b "Tetap seperti Anda"
                    b "Biarkan saya mengambilnya dari sudut lain juga"
                    scene mbtvn10 with dissolve
                    b "Dingin"
                    scene mbtvn9 with dissolve
                    s "Ok apa selanjutnya"
                    b "Terserah kamu"
                    b "Lakukan pose apa pun yang Anda sukai"
                    scene mbtvn11 with dissolve
                    "..."
                    b "Ini luar biasa"
                    if srel >=350:
                        scene mbtvn12 with dissolve
                        s "..."
                        scene mbtvn13 with dissolve
                        "..."
                        b "More more"
                        s "Foto yang cukup [bname]"
                        b "Tolong satu lagi"
                        b "Berlutut, itu akan menjadi panas aku bersumpah"
                        s "Hmm ok hanya satu"
                        scene mbtvn14 with fade
                        b "Fucking wow"
                        s "Enough"
                        s "Selamat malam"
                        b "Damn"
                        pass
                    else:
                        s "Foto yang cukup [bname]"
                        b "Damn"
                        pass

                    b "Ok"
                    b "Bye"
                    menu:
                        "Pergi tidur":
                            scene broom_night with fade
                            b "Saya kira sudah waktunya tidur"
                            jump newdays
                        "Menyelinap di [mname] dan Adam":

                            scene mbtvn1 with fade
                            mb "Itu lucu!"
                            m "Hahaha ya benar!"
                            b "Hmm"
                            m "Mari kita lanjutkan konser"
                            b "{i} (mereka tampak mabuk) {/i}"
                            b "{i} (Saya perlu melihat apa yang sedang terjadi) {/i}"
                            scene mbtvn2 with dissolve
                            m "Ya [bname]?"
                            b "Umm tidak ada, saya menyelesaikan studi saya"
                            b "Bisakah saya menonton TV dengan Anda?"
                            m "No"
                            if cherylfoundout >= 2 and cherylevent <6:
                                play sound "sounds/doorbell.wav"
                                m "Hmm siapa itu saat ini?"
                                stop sound
                                m "Buka pintu [bname]"
                                scene mbtvnc with dissolve
                                m "CHERYL!"
                                scene mbtvnc1 with dissolve
                                m "..."
                                c "Hi [mname]"
                                m "..."
                                c "Well"
                                c "Sepertinya saya datang pada waktu yang salah"
                                scene mbtvnc2 with dissolve
                                m "Tidak, tidak sama sekali, [bname] ambilkan segelas anggurnya"
                                m "Silakan masuk"
                                c "Baik saya lebih suka tidak mengganggu malam Anda yang nyaman"
                                c "Bisakah kami berbicara melalui telepon jika Anda tidak keberatan memberi saya nomor Anda?"
                                m "Baik saya lebih suka menelepon Anda jika Anda tidak keberatan"
                                c "Ini nomor saya, saya akan menunggu panggilan Anda"
                                $ mcallcheryl = 1
                                m "Thanks"
                                scene mbtvnc3 with fade
                                m "Senang sekarang?"
                                b "Sorry"
                                m "Pergi ke kamar Anda!"
                                scene broom_night with fade
                                b "{i} (fuck it i \ 'll go to sleep) {/i}"
                                jump newdays
                            else:

                                pass
                            m "Kembali ke kamar Anda"
                            b "{i}(Fuck it){/i}"
                            scene mbtvn3 with dissolve
                            b "{i} (setidaknya mereka menonton ini) {/i}"
                            b "{i} (i \ 'll pergi tidur) {/i}"
                            scene broom_night with fade
                            "..."
                            scene sleep1 with fade
                            "Setelah beberapa waktu"
                            b "{i} (i \ 'll pergi periksa mereka) {/i}"
                            scene mbtvn4 with fade
                            mb "Terima kasih untuk malam ini [mname]"
                            m "Terima kasih juga, selamat malam"
                            b "{i} (bagus, sekarang saya bisa tidur) {/i}"
                            scene broom_night with fade
                            "..."
                            jump newdays
        "Menyelinap di [mname] dan Adam":


            scene mbtvn1 with fade
            mb "Itu lucu!"
            m "Hahaha ya benar!"
            b "Hmm"
            m "Mari kita lanjutkan konser"
            b "{i} (mereka tampak mabuk) {/i}"
            b "{i} (Saya perlu melihat apa yang sedang terjadi) {/i}"
            scene mbtvn2 with dissolve
            m "Ya [bname]?"
            b "Umm tidak ada, saya menyelesaikan studi saya"
            b "Bisakah saya menonton TV dengan Anda?"
            m "No"
            if cherylfoundout >= 2 and cherylevent <6:
                play sound "sounds/doorbell.wav"
                m "Hmm siapa itu saat ini?"
                stop sound
                m "Buka pintu [bname]"
                scene mbtvnc with dissolve
                m "CHERYL!"
                scene mbtvnc1 with dissolve
                m "..."
                c "Hi [mname]"
                m "..."
                c "Well"
                c "Sepertinya saya datang pada waktu yang salah"
                scene mbtvnc2 with dissolve
                m "Tidak, tidak sama sekali, [bname] ambilkan segelas anggurnya"
                m "Silakan masuk"
                c "Baik saya lebih suka tidak mengganggu malam Anda yang nyaman"
                c "Bisakah kami berbicara melalui telepon jika Anda tidak keberatan memberi saya nomor Anda?"
                m "Baik saya lebih suka menelepon Anda jika Anda tidak keberatan"
                c "Ini nomor saya, saya akan menunggu panggilan Anda"
                $ mcallcheryl = 1
                m "Thanks"
                scene mbtvnc3 with fade
                m "Senang sekarang?"
                b "Sorry"
                m "Pergi ke kamar Anda!"
                scene broom_night with fade
                b "{i} (fuck it i \ 'll go to sleep) {/i}"
                jump newdays
            else:

                pass
            m "Kembali ke kamar Anda"
            b "{i}(Fuck it){/i}"
            scene mbtvn3 with dissolve
            b "{i} (setidaknya mereka menonton ini) {/i}"
            b "{i} (i \ 'll pergi tidur) {/i}"
            scene broom_night with fade
            "..."
            scene sleep1 with fade
            "Setelah beberapa waktu"
            b "{i} (i \ 'll pergi periksa mereka) {/i}"
            scene mbtvn4 with fade
            mb "Terima kasih untuk malam ini [mname]"
            m "Terima kasih juga, selamat malam"
            b "{i} (bagus, sekarang saya bisa tidur) {/i}"
            scene broom_night with fade
            "..."
            jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
