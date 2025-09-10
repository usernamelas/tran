label jenmorning:
    $ Hour += 1
    if elaine_convince ==4 and startnework ==0:
        if sgrm >= 2:
            $ sgrm += 1
            b "{i} (Saya harus hati -hati) {/i}"
            b "{i} (i \ 'M masih grounded) {/i}"
            jump s_work_jenmorning
        else:
            jump new_work_jenmorning

    elif elaine_convince ==4 and startnework ==1:
        if sgrm >= 2:
            $ sgrm += 1
            b "{i} (Saya harus hati -hati) {/i}"
            b "{i} (i \ 'M masih grounded) {/i}"
            jump s_work_jenmorning
        else:
            jump new_work_jenmorning
    else:

        if sgrm >= 2:
            $ sgrm += 1
            b "{i} (Saya harus hati -hati) {/i}"
            b "{i} (i \ 'M masih grounded) {/i}"
            jump s_work_jenmorning
        else:
            pass

    scene work_going3 with fade
    b "Selamat pagi"
    m "Selamat pagi [bname]"
    menu:
        "Akan bekerja?":
            m "Yes"
            b "Hmmm"
            menu:
                "Apakah itu membayar dengan baik?" if wrkquestions ==1:
                    m "Tidak begitu, tapi tidak apa -apa"
                    m "Setidaknya kami memiliki penghasilan"
                    b "Yeah"
                    $ wrkquestions = 2
                    m "Persis ... aku harus pergi"
                    b "Ok"
                    "..."
                    m "Dengar, maukah kamu mencuci piring?"
                    b "Sure"
                    m "Terima kasih, beri aku pelukan"
                    show screen mrelup
                    scene work_going4 with dissolve
                    "..."
                    $ mrel += 1
                    hide screen mrelup
                    m "Sampai jumpa di malam hari"
                    pass


                "Bagaimana?" if wrkquestions ==0:
                    m "Tidak apa -apa, saya mengelola kedai kopi"
                    b "Apakah itu lingkungan yang aman"
                    $ wrkquestions = 1
                    m "Ya, itu dimiliki oleh seorang wanita"
                    b "Jadi begitu..."
                    m "Saya harus pergi"
                    b "Ok"
                    "..."
                    m "Dengar, bisakah kamu mencuci piring?"
                    b "Sure"
                    m "Terima kasih, beri aku pelukan"
                    show screen mrelup
                    scene work_going4 with dissolve
                    "..."
                    $ mrel += 5
                    hide screen mrelup
                    m "Sampai jumpa di malam hari"
                    pass

                "Sampai jumpa" if wrkquestions ==2:
                    b "Oke, sampai jumpa di malam hari"
                    m "Yes"
                    m "Dengar, bisakah kamu mencuci piring?"
                    b "Sure"
                    m "Terima kasih, beri aku pelukan"
                    show screen mrelup
                    scene work_going4 with dissolve
                    "..."
                    $ mrel += 2
                    hide screen mrelup
                    m "Sampai jumpa di malam hari"
                    pass
            scene work_going5 with fade
            "..."
            if wrkquestions ==0:
                scene work_going6 with dissolve
                s "Bagaimana cuci piring?"
                b "Hah!"
                scene work_going10 with dissolve
                b "Anda membuat saya takut"
                s "Sorry"
                b "Whatever"
                s "Saya melihat bahwa Anda sedang membantu hari ini"
                b "Jadi?"
                s "Errm ... Bisakah Anda mencuci pakaian saya?"
                b "Enyah!"
                scene work_going11 with dissolve
                s "Oke, bye"
                b "{i} (hmm cuciannya! Menarik) {/i}"
                menu:
                    "Tunggu, aku akan melakukannya, tapi apa yang ada di dalamnya untukku?":
                        pass
                    "Tunggu aku akan membantumu":
                        jump slaundry


                if srel >=150:
                    jump slaundryalt
                else:
                    pass
                s "Tidak ada, saya tidak ingin Anda melakukannya, saya telah berubah pikiran"
                "Tingkatkan Poin Hubungan Anda"
                scene hall_d with fade
                b "{i}(Damn){/i}"
                call screen gnav

            if wrkquestions >=1:
                scene work_going7 with dissolve
                "..."
                scene work_going8 with vpunch
                "..."
                s "Huuu!"
                b "Sungguh!"
                scene work_going9 with dissolve
                s "jaga mulutmu"
                b "Ya terserah!"
                scene work_going10 with dissolve
                b "Anda membuat saya takut"
                s "Sorry"
                b "Whatever"
                s "Saya melihat bahwa Anda sedang membantu hari ini"
                b "Jadi?"
                scene work_going12 with dissolve
                s "Errm ... Bisakah Anda mencuci pakaian saya?"
                b "Enyah!"
                scene work_going11 with dissolve
                s "Oke, bye"
                b "{i} (hmm cuciannya! Menarik) {/i}"
                menu:
                    "Tunggu, aku akan melakukannya, tapi apa yang ada di dalamnya untukku?":
                        pass
                    "Tunggu aku akan membantumu":
                        jump slaundry

                if srel >=150:
                    jump slaundryalt
                else:
                    pass
                s "Tidak ada, saya tidak ingin Anda melakukannya, saya telah berubah pikiran"
                "Tingkatkan Poin Hubungan Anda"
                scene hall_d with fade
                b "{i}(Damn){/i}"
                call screen gnav
        "Apa yang ada":

            m "Seperti yang Anda lihat, saya berangkat kerja"
            b "Hmm begitu"
            m "Dengar, bisakah kamu mencuci piring?"
            b "Sure"
            m "Terima kasih, beri aku pelukan"
            show screen mrelup
            scene work_going4 with dissolve
            "..."
            $ mrel += 1
            hide screen mrelup
            m "Sampai jumpa di malam hari"
            scene hall_d with fade
            b "{i} (...) {/i}"
            call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
