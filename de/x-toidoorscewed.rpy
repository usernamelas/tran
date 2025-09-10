image toidsa:
    "toidsa00.jpg"
    pause 0.05
    "toidsa01.jpg"
    pause 0.05
    "toidsa02.jpg"
    pause 0.05
    "toidsa03.jpg"
    pause 0.05
    "toidsa04.jpg"
    pause 0.05
    "toidsa05.jpg"
    pause 0.05
    "toidsa06.jpg"
    pause 0.05
    "toidsa07.jpg"
    pause 0.05
    "toidsa08.jpg"
    pause 0.05
    "toidsa09.jpg"
    pause 0.05
    "toidsa10.jpg"
    pause 0.05
    "toidsa11.jpg"
    pause 0.05
    "toidsa12.jpg"
    pause 0.05
    "toidsa13.jpg"
    pause 0.05
    "toidsa14.jpg"
    pause 0.05
    "toidsa15.jpg"
    pause 0.05
    "toidsa16.jpg"
    pause 0.05
    "toidsa17.jpg"
    pause 0.05
    repeat

label toidoorscewed:
    scene tod_d_s1 with dissolve
    s "Hai!"
    if srel >=150:
        scene tod_d_s with vpunch
        s "Betapa sih yang Anda masuk!"
        b "Hehehe"
        s "Keluar!"
        scene tod_d_s2 with dissolve
        s "Stop staring"
        menu:
            "Beri aku ciuman":
                scene tod_d_s3 with dissolve
                b "Ayo hanya satu ciuman yang saya tidak akan gigit"
                scene tod_d_s4 with hpunch
                "..."
                scene tod_d_s5 with dissolve
                menu:
                    "Cium dia":
                        scene tod_d_s6 with dissolve
                        s "Mhhm"
                        scene tod_d_s3 with fade
                        b "Sekarang Anda dapat melanjutkan mandi Anda"
                        if srel >=150:
                            s "Tunggu!"
                            s "Beri aku satu lagi!"
                            scene tod_d_s3a with dissolve
                            "..."
                            scene tod_d_s3b with dissolve
                            "..."
                            scene tod_d_s3a with dissolve
                            s "Anda mungkin pergi sekarang"
                            pass
                        else:

                            pass
                        scene room3 with fade
                        "..."
                        call screen gnav
                    "Cium dia dan biarkan tangan Anda melakukan pekerjaan":

                        scene tod_d_s7 with dissolve
                        s "Hah!"
                        scene tod_d_s8 with dissolve
                        s "Ahhh"
                        menu:
                            "Bawa dia ke dinding" if srel >=400:
                                scene tod_d_s9 with fade
                                s "Don't [bname]"
                                b "Mengapa tidak?"
                                s "Karena itu tidak benar"
                                b "Dan kalau..."
                                scene tod_d_s10 with hpunch
                                b "... saya melakukan ini!"
                                scene tod_d_s11 with dissolve
                                s "Ahhh"
                                scene tod_d_s12 with dissolve
                                s "..."
                                scene tod_d_s11 with dissolve
                                s "Itu menyakitkan!"
                                scene tod_d_s13 with hpunch
                                b "Woahh!"
                                if srel >=500:
                                    scene toidsa
                                    s "Ahhh"
                                    "..."
                                    b "Hmm"
                                    "..."
                                    s "..."
                                    pass
                                else:
                                    pass
                                scene tod_d_s14 with dissolve
                                b "Ahh"
                                menu:
                                    "Turunkan dia, bersikap tangguh" if sdom >=40:
                                        scene tod_d_s16 with dissolve
                                        s "Meneguk!"
                                        scene tod_d_s17 with fade
                                        show screen sreldw
                                        $ srel -= 2
                                        b "Hehe maaf aku akan pergi"
                                        hide screen sreldw
                                        scene room3 with fade
                                        "..."
                                        call screen gnav
                                    "Selesai di dalam":

                                        scene tod_d_s14 with hpunch
                                        b "Sungguh!"
                                        $ spreg += 1
                                        s "Anda gila!"
                                        scene tod_d_s15 with fade
                                        s "Keluar, biarkan aku mencuci"
                                        scene room3 with fade
                                        "..."
                                        call screen gnav

                            "{s} bawa dia ke dinding {/s}" if srel <400:
                                "Belum terbuka untuk Anda"
                                scene tod_d_s3 with fade
                                b "Sekarang Anda dapat melanjutkan mandi Anda"
                                scene room3 with fade
                                "..."
                                call screen gnav
                            "Cukup":

                                scene tod_d_s3 with fade
                                b "Sekarang Anda dapat melanjutkan mandi Anda"
                                scene room3 with fade
                                "..."
                                call screen gnav
            "Ambil fotonya dengan ponsel Anda":



                scene tod_d_s2bw with dissolve
                "..."
                scene tod_d_s with vpunch
                s "Hai!! Aku berkata !!"
                b "Hehe ok ok"
                scene room3 with fade
                "..."
                call screen gnav
    else:


        scene tod_d_s2 with dissolve
        s "Tolong keluar"
        menu:
            "Beri aku ciuman":
                scene tod_d_s3 with dissolve
                b "Ayo hanya satu ciuman yang saya tidak akan gigit"
                scene tod_d_s4 with hpunch
                "..."
                scene tod_d_s5 with dissolve
                menu:
                    "Cium dia":
                        scene tod_d_s6 with dissolve
                        s "Mhhm"
                        scene tod_d_s3 with fade
                        b "Sekarang Anda dapat melanjutkan mandi Anda"
                        scene room3 with fade
                        "..."
                        call screen gnav
                    "Cium dia dan biarkan tangan Anda melakukan pekerjaan":

                        scene tod_d_s7 with dissolve
                        s "Hah!"
                        scene tod_d_s with vpunch
                        s "Hai!"
                        s "Apa yang sedang kamu lakukan!"
                        b "Hehe sorry"
                        s "Keluar!"
                        scene room3 with fade
                        b "Hehehe"
                        call screen gnav
            "Ambil fotonya dengan ponsel Anda":


                scene tod_d_s2bw with dissolve

                "..."
                scene tod_d_s with vpunch
                s "Hai!! KELUAR!!"
                b "Hehe ok ok"
                scene room3 with fade
                "..."
                call screen gnav
            "Meninggalkan":

                b "Ok"
                scene room3 with fade
                "..."
                call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
