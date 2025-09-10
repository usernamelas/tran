label bdomm:
    menu:
        "Berlutut dan hisap ini":
            $ mdom += 1
            scene mbgn52 with dissolve
            m "Ughh"
            scene mbgn53 with dissolve
            b "Oh yeah"
            scene mbgn54 with dissolve
            "..."
            scene mbgn55 with dissolve
            b "Oh fuck"
            b "Enough"
            scene mbgn56 with dissolve
            b "Ahhh"
            scene mbgn56a with dissolve
            "..."
            b "Sekarang Anda bisa tidur"
            scene mbgn57 with dissolve
            b "Selamat malam"
            scene black
            "..."
            jump newdays


        "Naik tempat tidur" if mdom >=3 and mrel >= 300:
            scene mbgn58 with fade
            m "Bawa aku"
            scene mbgn59 with hpunch
            m "Ahhh"
            scene mbgn60 with dissolve
            m "[bname] !! Ah"
            scene mbgn59 with dissolve
            m "Fuck me"
            scene mbgn61 with dissolve
            "..."
            scene mbgn62 with dissolve
            m "Ahh"
            scene mbgn63 with dissolve
            m "Yesss"
            scene mbgn65 with dissolve
            b "Kemarilah"
            m "{i} (dia mengambil biaya) {/i}"
            m "Saya buruk [bname]"
            scene mbgn66 with dissolve
            m "Ya menghukum saya"
            scene mbgn67 with dissolve
            "..."
            scene mbgn68 with dissolve
            b "Bangun!"
            scene mbgn69 with dissolve
            m "Apakah kamu dekat?"
            b "Yes"
            m "Jangan cum di dalam"
            scene mbgn70 with dissolve
            b "Mengapa tidak?"
            m "Ahhh tolong jangan di dalam"
            b "Ok saya menang \ 't"
            menu:
                "Dimasukkan ke dalam pantatnya dan cum" if mrel >= 400:
                    scene mbgn71 with dissolve
                    m "Ya Tuhan!"
                    $ persistent.unlock_29 = True
                    scene mbgn72 with dissolve
                    m "Ahhh"
                    scene mbgn71 with dissolve
                    "..."
                    scene mbgn71a with dissolve
                    b "Selamat malam"
                    scene mbgn74 with fade
                    m "Ya Tuhan, itu terbakar seperti neraka"
                    m "Aku akan membunuhmu Stewart"
                    scene black
                    "..."
                    jump newdays
                "Mengeluarkan":

                    scene mbgn73 with dissolve
                    b "Ahh"
                    scene mbgn57 with fade
                    b "Selamat malam"
                    scene black
                    "..."
                    jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
