image stoibj:
    "stbj00.jpg"
    pause 0.05
    "stbj01.jpg"
    pause 0.05
    "stbj02.jpg"
    pause 0.05
    "stbj03.jpg"
    pause 0.05
    "stbj04.jpg"
    pause 0.05
    "stbj05.jpg"
    pause 0.05
    "stbj06.jpg"
    pause 0.05
    "stbj07.jpg"
    pause 0.05
    "stbj08.jpg"
    pause 0.05
    "stbj09.jpg"
    pause 0.05
    "stbj10.jpg"
    pause 0.05
    "stbj11.jpg"
    pause 0.05
    "stbj12.jpg"
    pause 0.05
    "stbj13.jpg"
    pause 0.05
    "stbj14.jpg"
    pause 0.05
    "stbj15.jpg"
    pause 0.05
    "stbj16.jpg"
    pause 0.05
    "stbj17.jpg"
    pause 0.05
    "stbj18.jpg"
    pause 0.05
    "stbj19.jpg"
    pause 0.05
    "stbj20.jpg"
    pause 0.05
    "stbj21.jpg"
    pause 0.05
    "stbj22.jpg"
    pause 0.05
    "stbj23.jpg"
    pause 0.05
    "stbj24.jpg"
    pause 0.05
    "stbj25.jpg"
    pause 0.05
    "stbj26.jpg"
    pause 0.05
    "stbj27.jpg"
    pause 0.05
    "stbj28.jpg"
    pause 0.05
    "stbj29.jpg"
    pause 0.05
    "stbj30.jpg"
    pause 0.05
    "stbj31.jpg"
    pause 0.05
    "stbj32.jpg"
    pause 0.05
    "stbj33.jpg"
    pause 0.05
    "stbj34.jpg"
    pause 0.05
    "stbj35.jpg"
    pause 0.05
    "stbj36.jpg"
    pause 0.05
    "stbj37.jpg"
    pause 0.05
    "stbj38.jpg"
    pause 0.05
    "stbj39.jpg"
    pause 0.05
    "stbj40.jpg"
    pause 0.05
    "stbj41.jpg"
    pause 0.05
    "stbj42.jpg"
    pause 0.05
    "stbj43.jpg"
    pause 0.05
    "stbj44.jpg"
    pause 0.05
    "stbj45.jpg"
    pause 0.05
    "stbj46.jpg"
    pause 0.05
    "stbj47.jpg"
    pause 0.05
    "stbj48.jpg"
    pause 0.05
    repeat

label toidoorscewed_morning:
    scene toi_d_s with fade
    s "Ya maksud saya tunggu!"
    scene toi_d_se with vpunch
    s "HAH!"
    s "Bagaimana Anda masuk?"
    b "Lanjutkan, saya akan melihat Anda kencing"
    if srel >=150:
        if sdom >=80:
            s "Saya tidak suka [bname]"
            b "Dan saya menyukainya, jadi Anda lebih baik tinggal"
            scene toi_d_se4 with dissolve
            s "You're crazy"
            scene toi_d_se5 with dissolve
            s "And dirty"
            menu:
                "Saya akan menunjukkan kepada Anda apa yang kotor" if sdom >=150:
                    scene toi_d_se6 with hpunch
                    s "Hey"
                    scene toi_d_se7 with dissolve
                    s "Fuck [bname]"
                    scene toi_d_se8 with dissolve
                    s "Aku masih kencing"
                    scene toi_d_se9 with dissolve
                    a "Ahhh"
                    $ bpee_dom = 1
                    scene toi_d_se10 with fade
                    s "Anda kotor seperti orang tua"
                    b "Hehehe apakah itu pujian?"
                    s "Yeah"
                    b "{i}(Hmmm){/i}"
                    menu:
                        "Selesaikan dia":
                            b "..."
                            scene toi_d_se11 with vpunch
                            if srel >=150:
                                s "Ahh"
                                scene toi_d_se12 with dissolve
                                "..."
                                scene toi_d_se13 with dissolve
                                s "Ahhh !! [bname]"
                                scene toi_d_se14 with dissolve
                                "..."
                                scene toi_d_se15 with dissolve
                                s "Ahhh!"
                                if srel >=250:
                                    scene stoibj
                                    s "Hmm"
                                    "..."
                                    s "Hhh"
                                    b "Yeah"
                                    "..."
                                    scene stoibj_end with dissolve
                                    b "Ahhh"
                                    "..."
                                    scene toi_d_se17 with fade
                                    s "Aku membencimu"
                                    b "Hehehe"
                                    b "Sampai jumpa lagi"
                                    if srel >=200:
                                        scene sckiss with hpunch
                                        b "What"
                                        scene sckiss1 with dissolve
                                        b "The fuck"
                                        pass
                                    else:
                                        pass
                                    scene room3 with dissolve
                                    call screen gnav
                                else:


                                    scene toi_d_se16 with fade
                                    s "Anda gila, saya bisa bersumpah"
                                    b "Hehehe"
                                    pass
                            else:
                                s "Berhenti!!"
                                s "Silahkan pergi!"
                                b "Ok"
                                "Naikkan hubungan Anda menjadi 150"
                                pass
                        "Melanjutkan":

                            pass
                    b "Sampai jumpa lagi"
                    scene room3 with dissolve
                    call screen gnav

                "{s} i  'll tunjukkan apa yang kotor {/s}" if sdom <150:
                    scene toi_d_se6 with hpunch
                    s "Hei hentikan! Saya akan memberi tahu [mname]"
                    b "Ok apapun, saya akan pergi sekarang"
                    scene room3 with dissolve
                    "Belum tersedia untuk Anda"
                    "Naikkan lebih banyak poin dominasi Anda"
                    call screen gnav
                "Melanjutkan":


                    b "Ya terserah, saya akan pergi sekarang"
                    scene room3 with dissolve
                    call screen gnav
        else:

            scene toi_d_se3 with dissolve
            s "Aku bersumpah kamu gila"
            b "Mengapa Anda berhenti"
            s "Saya tidak menyukainya"
            scene room3 with dissolve
            b "{i} (Saya harus menaikkan poin dominasi) {/i}"
            call screen gnav
    else:
        scene toi_d_se1 with dissolve
        s "Keluar!"
        b "Hehe ok ok"
        "Naikkan Poin Dominasi Anda"
        scene toi_d_se2 with dissolve
        b "Apa -apaan! Anda masih kencing"
        b "Dan di lantai"
        b "Aku keluar dari sini"
        scene room3 with dissolve
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
