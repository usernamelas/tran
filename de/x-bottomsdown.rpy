label bottomsdown:
    s "[bname] Tolong tinggalkan aku sendiri"
    menu:
        "Tinggalkan dia sendiri":
            scene door with fade
            b "{i} (...) {/i}"
            "..."
            $ srel += 5
            call screen gnav
        "Turun sepanjang jalan":

            scene sroom_av40 with dissolve
            if scorr >= 30:
                s "Pff"
                scene sroom_av41 with dissolve
                s "Apa yang kamu inginkan sekarang?"
                b "Hehe"
                menu:
                    "Menamparnya":
                        if scorr >= 80 and sdom >=150:
                            scene sroom_av42 with hpunch
                            s "Apakah hanya itu yang bisa Anda lakukan?"
                            scene sroom_av43 with hpunch
                            s "Ouch"
                            s "Apa ...!"
                            b "Anda telah menjadi gadis yang nakal"
                            scene sroom_av44 with dissolve
                            s "Benar-benar?"
                            b "Yes"
                            s "Seberapa buruk?"
                            b "Very"
                            s "Hmmm"
                            s "Jadi apakah saya pantas mendapatkan lebih banyak hukuman?"
                            b "{i} (hehe dia menyukainya) {/i}"
                            b "Hmm"
                            scene sroom_av45 with fade
                            s "Tolong jangan menghukum saya [bname]"
                            scene sroom_av46 with dissolve
                            s "Tolong jangan \ 't i ' ll melakukan apapun yang Anda inginkan"
                            b "Apa pun?"
                            s "Ya, tapi bukan seks"
                            b "Dan bagaimana jika saya memberi Anda uang untuk itu?"
                            scene sroom_av47 with dissolve
                            s "Hah!"
                            s "Apa pendapat Anda tentang saya?"
                            b "Nothing"
                            scene sroom_av48 with dissolve
                            b "Pertimbangkan itu sebagai hadiah"
                            s "Berapa harganya?"
                            b "Aku akan melihat apa yang aku miliki dan aku akan memberimu"
                            b "Jangan khawatir aku akan membuatmu bahagia"
                            scene sroom_av49 with dissolve
                            "..."
                            scene sroom_av48 with dissolve
                            s "Tetapi"
                            b "Tapi apa?"
                            s "Anda tidak ada di dalam, oke?"
                            b "Ok"
                            scene sroom_av50 with dissolve
                            s "Ahh"
                            scene sroom_av51 with dissolve
                            b "Yeah"
                            scene sroom_av52 with dissolve
                            s "[bname]"
                            s "Beri tahu saya sebelum Anda cum"
                            b "Ya, segera"
                            scene sroom_av53 with dissolve
                            s "Keluarkan"
                            scene sroom_av54 with dissolve
                            s "Menghukum mulutku [bname]"
                            scene sroom_av55 with vpunch
                            "..."
                            scene sroom_av56 with dissolve
                            "..."
                            scene sroom_av57 with fade
                            b "Lihat yah!"
                            scene door with fade
                            "Itu semua dalam opsi ini"
                            call screen gnav
                        else:




                            scene sroom_av15a with vpunch
                            s "Keluar brengsek !!"
                            b "I'm leaving"
                            scene door with fade
                            b "{i} (...) {/i}"
                            "Meningkatkan korupsi dan dominasi lebih banyak"
                            call screen gnav
                    "Seret dia keluar dari tempat tidur":

                        scene sroom_av41d with vpunch
                        if scorr >= 60:
                            b "Kemarilah"
                            scene sroom_av42d with dissolve
                            s "Tolong jangan menghukum saya [bname]"
                            scene sroom_av45 with fade
                            s "Tolong jangan menghukum saya [bname]"
                            scene sroom_av46 with dissolve
                            s "Tolong jangan \ 't i ' ll melakukan apapun yang Anda inginkan"
                            b "Apa pun?"
                            s "Ya, tapi bukan seks"
                            b "Dan bagaimana jika saya memberi Anda uang untuk itu?"
                            scene sroom_av47 with dissolve
                            s "Hah!"
                            s "Apa pendapat Anda tentang saya?"
                            b "Nothing"
                            scene sroom_av48 with dissolve
                            b "Pertimbangkan itu sebagai hadiah"
                            s "Berapa harganya?"
                            b "Aku akan melihat apa yang aku miliki dan aku akan memberimu"
                            b "Jangan khawatir aku akan membuatmu bahagia"
                            scene sroom_av49 with dissolve
                            "..."
                            scene sroom_av48 with dissolve
                            s "Tetapi"
                            b "Tapi apa?"
                            s "Anda tidak ada di dalam, oke?"
                            b "Ok"
                            scene sroom_av50 with dissolve
                            s "Ahh"
                            scene sroom_av51 with dissolve
                            b "Yeah"
                            scene sroom_av51a with dissolve
                            b "Kemarilah"
                            scene sroom_av52a with dissolve
                            s "[bname]"
                            s "Beri tahu saya sebelum Anda cum"
                            b "Ya, segera"
                            scene sroom_av53a with vpunch
                            if sdom >=150:
                                s "Ahhh"
                                scene sroom_av53 with dissolve
                                s "Keluarkan"
                                scene sroom_av54 with dissolve
                                s "Menghukum mulutku [bname]"
                                scene sroom_av55 with vpunch
                                "..."
                                scene sroom_av55a with dissolve
                                b "Ahhh"
                                scene sroom_av56 with dissolve
                                "..."
                                scene sroom_av57 with fade
                                b "Lihat yah!"
                                scene door with fade
                                "Itu semua dalam opsi ini"
                                call screen gnav
                            else:

                                s "Ahhh"
                                b "I cum"
                                scene sroom_av49 with fade
                                s "Apakah itu keluar?"
                                b "Ya, bisakah Anda merasa?"
                                s "Yes"
                                s "{i} (Saya benar -benar tidak dapat memberi tahu, karena dia memberi saya orgasme yang intens) {/i}"
                                s "Saya akan memeriksa toilet"
                                s "Sampai jumpa"
                                scene door with fade
                                "Naikkan Poin Dominasi Anda"
                                call screen gnav
                        else:
                            pass
                        s "Hai!"
                        scene sroom_av15a with vpunch
                        s "KELUAR!!"
                        b "Woah tenang!"
                        s "Keluar!"
                        b "I'm leaving"
                        scene door with fade
                        b "{i} (...) {/i}"
                        call screen gnav
            else:

                scene sroom_av15a with vpunch
                s "KELUAR!!"
                b "I'm leaving"
                scene door with fade
                b "{i} (...) {/i}"
                "Mengangkat korupsinya"
                call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
