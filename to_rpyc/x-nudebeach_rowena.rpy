label nudebeach_rowena:
    scene nbr with fade
    s "Ini terlihat seperti pantai terpencil"
    a "Tidak, biasanya ada lebih sedikit orang saat ini"
    if saction ==0:
        rb "Itu adalah pantai telanjang"
        scene nbr_s with hpunch
        s "Apa?"
        a "Oh itu normal"
        b "..."
    else:
        pass

    scene nbr1 with dissolve
    rb "Apa yang kita tunggu, mari kita lakukan ini"
    a "Ya, ayolah teman -teman"
    b "Hmm [sname]"
    scene nbr2 with dissolve
    s "Apa? Saya tidak akan melakukannya"
    b "Ayo, jangan menjadi pemalu"
    b "Kami nyaris tidak menemukan teman untuk perusahaan kami"
    b "Apa yang akan mereka pikirkan tentang kita, jika kita berhenti sekarang"
    $ saction += 1
    scene nbr3 with dissolve
    b "Ayo!"
    b "Selain itu, hanya kita, tidak ada orang di sini"
    scene nbr4 with fade
    rb "Let's swim"
    scene nbr5 with dissolve
    "..."
    scene nbr6 with dissolve
    s "Hentikan Rowena"
    s "Setidaknya tidak di depan pacar Anda"
    a "Mudah, tidak seperti [bname] adalah pacar Anda"
    s "Tolong hentikan"
    scene nbr7 with dissolve
    "Mereka semua berenang untuk sementara waktu"
    scene nbr8 with fade
    "..."
    scene nbr9 with dissolve
    s "[bname] Apakah Anda memiliki lotion yang cukup untuk kami semua"
    b "Yes babe"
    s "Huh"
    scene nbr10 with fade
    "..."
    if saction >1:
        scene nbr11 with dissolve
        b "{i}(Hmmm){/i}"
        scene nbr12 with dissolve
        rb "Ayo sayang, mari kita jalan -jalan"
        rb "Mereka mungkin ingin tetap sendirian juga"
        s "..."
        a "Ok"
        scene nbr13 with dissolve
        s "Itu menyeramkan, hentikan"
        b "Apa?"
        b "Anda tidak bisa menghentikan saya untuk menikmati keindahan"
        if saction >3:
            s "Hentikan!"
            s "Anda membuat saya malu"
            b "Apa?"
            $ nudebeachtalk += 1
            s "Semua orang melihat kami"
            b "Mengapa?"
            if nudebeachtalk <=2:
                scene nbr15 with dissolve
                "..."
                b "Saya bertanya mengapa?"
                b "{i}(Hmmm){/i}"
                b "{i} (dia tidak ingin menjawab, atau belum siap) {/i}"
                b "{i} (i \ 'll terus bertanya) {/i}"
                "Anda tinggal sebentar dan pulang"
                scene hall_d with fade
                b "{i} (...) {/i}"
                call screen gnav
            else:

                "..."
                b "Saya bertanya mengapa?"
                scene nbr16 with dissolve
                s "Karena hal Anda, selalu sulit"
                menu:
                    "Saya maafkan saya akan mengerjakannya":
                        b "... tapi seperti yang saya katakan, saya tidak bisa membantunya"
                        s "Anda harus mengendalikan"
                        b "I'll try"
                        "..."
                        pass
                    "Mengapa Anda melihat pertama kali":


                        scene nbr17 with dissolve
                        show screen scorr
                        s "..."
                        hide screen scorr
                        $ scorr += 1
                        scene nbr18 with dissolve
                        s "Aku akan mencari Rowena ..."
                        scene nbr19 with hpunch
                        s "Hah!!"
                        s "{i} (i \ 'd cuti lebih baik) {/i}"
                        scene nbr20 with dissolve
                        "..."
                        pass


                scene nbr_return with fade
                b "Mereka datang"
                scene nbr_return1 with fade
                rb "Biarkan \ menempatkan permainan"
                s "Game yang mana?"
                rb "Kebenaran atau berani"
                b "Ya ide bagus"
                scene nbr_g with fade
                b "Mari kita lihat"
                scene nbr_g_rb with dissolve
                a "Hahaha mendapatkanmu!"
                a "Kebenaran atau berani?"
                rb "Berani, tentu saja!"
                a "Hmmm"
                a "Flash Anda ... Anda tahu"
                rb "Mudah"
                scene nbr_rb with fade
                "..."
                b "Mari kita belok lagi"
                scene nbr_g_bs with fade
                b "Aha!"
                b "Kebenaran atau Berani!"
                if sgtruth <=1:
                    $ sgtruth += 1
                    scene nbr_g with dissolve
                    s "Truth"
                    menu:
                        "Apakah Anda Virgin?":
                            scene nbr_g_bs1 with dissolve
                            s "..."
                            s "No"
                            b "Hmm"
                            b "Ok"
                            pass
                        "Apakah Anda pernah menipu pacar Anda":

                            scene nbr_g_bs1 with dissolve
                            s "..."
                            s "Yes"
                            a "WHAAAA!"
                            b "Hmm"
                            b "Ok"
                            pass
                else:
                    scene nbr_g with dissolve
                    s "Dare"
                    b "Hmm"
                    $ sgtruth += 1
                    b "Saya ingin"
                    menu:
                        "Rowena untuk menciummu":
                            scene nbr_g_bs1 with dissolve
                            s "Mustahil!"
                            a "Ayo mudah"
                            "..."
                            scene nbr_k with fade
                            s "..."
                            if sgtruth >3:
                                scene nbr_k1 with dissolve
                                s "Saya bisa \ 't"
                                b "Chicken"
                                s "..."
                                s "{i} (fuck you) {/i}"
                                scene nbr_k2 with hpunch
                                b "Hah!"
                                "..."
                                if b_fightback == 1:
                                    b "{i} Waktunya mengambil bidikan itu! {/i}"
                                    b "{i} di mana ponsel saya {/i}"
                                    scene nbr_k3 with dissolve
                                    $ b_fightback = 2
                                    b "{i} hebat! {/i}"
                                    scene nbr_k4 with dissolve
                                    b "{i} ya itu \ s it {/i}"
                                    b "Cukup untuk kalian berdua"
                                    pass
                                else:
                                    b "Wow!"
                                    b "Cukup untuk kalian berdua"
                                    pass
                            else:

                                scene nbr_k1 with dissolve
                                s "Saya bisa \ 't"
                                b "Tapi itu dianggap telah hilang"
                                b "Chicken"
                                s "Yeah whatever"
                                pass

                b "Mari kita belok lagi"
                scene nbr_g_rs with fade
                a "Ok"
                a "Giliran saya untuk bertanya"
                s "Apa itu?"
                a "Kebenaran atau berani"
                s "Dare"
                scene nbr_g_rs1 with dissolve
                a "Hmm"
                if sgtruth <=4:
                    pass
                else:
                    a "Pergi dengan [bname] di belakang pepohonan dan lakukan sesuatu yang liar untuknya"
                    a "Sekarang karena kita tidak akan melihatnya ..."
                    a "Itu sampai [bname] untuk memutuskan apakah itu cukup berani atau tidak"
                    a "Jadi dia memutuskan apakah itu menang atau kalah"
                    scene nbr_g_bs1a with dissolve
                    if srel >=150:
                        s "..."
                        scene nbr_g_bs5 with fade
                        s "Apa yang kamu inginkan?"
                        menu:
                            "Seks oral":
                                s "All right"
                                scene nbr_g_bs6 with fade
                                "..."
                                scene nbr_g_bs7 with dissolve
                                s "Apakah cukup untuk Dare?"
                                b "Apa?!"
                                b "No way"
                                scene nbr_g_bs8 with dissolve
                                "..."
                                scene nbr_g_bs9 with dissolve
                                "..."
                                scene nbr_g_bs10 with dissolve
                                b "Hmmm"
                                b "Lovely"
                                scene nbr_g_bs11 with dissolve
                                "..."
                                if rowenabffuck ==1 and day ==4:
                                    jump rowenaorgy

                                elif rowenabffuck ==1 and day ==6:
                                    jump rowenaorgy
                                else:
                                    pass
                                scene nbr_g_bs12 with hpunch
                                b "Ahhh!"
                                scene nbr_g_bs13 with dissolve
                                b "Let's go"
                                pass
                            "Sialan":



                                b "Turun"
                                scene nbr_g_bs14 with dissolve
                                s "..."
                                scene nbr_g_bs15 with dissolve
                                s "Ahhh"
                                scene nbr_g_bs15a with dissolve
                                s "Aduh, cukup menyakitkan"
                                b "Mengapa?"
                                s "Beri aku di mulutku"
                                scene nbr_g_bs10 with dissolve
                                b "Hmmm"
                                b "Lovely"
                                scene nbr_g_bs11 with dissolve
                                "..."
                                if rowenabffuck ==1 and day ==4:
                                    jump rowenaorgy

                                elif rowenabffuck ==1 and day ==6:
                                    jump rowenaorgy
                                else:
                                    pass
                                scene nbr_g_bs12 with hpunch
                                b "Ahhh!"
                                scene nbr_g_bs13 with dissolve
                                b "Let's go"
                                pass
                    else:


                        s "Tidak, saya tidak suka"
                        a "Lalu kalah"
                        s "Saya tidak peduli"
                        scene nbr with fade
                        s "..."
                        scene hall_d with fade
                        b "{i} (...) {/i}"
                        call screen gnav

                a "Kiss [bname]"
                s "All right"
                scene nbr_g_bs2 with fade
                "..."
                scene nbr_g_bs3 with dissolve
                b "{i} (sialan! Payudaranya akan membuat saya meledak) {/i}"
                if sgtruth <=1:
                    pass
                else:
                    scene nbr_g_bs4 with dissolve
                    b "{i} (sial!) {/i}"
                    pass


                scene nbr_g_rb with dissolve
                "Anda bermain sebentar dan pulang"
                if rowenadp ==1 and rowenacall ==0:
                    scene nbr with fade
                    "..."
                    menu:
                        "Ingatkan Rowena tentang lipstik":
                            b "Rowena lipstik yang bagus"
                            scene nbrb with dissolve
                            a "Apa?"
                            a "Saya tidak memiliki lipstik"
                            b "Oh ya benar"
                            $ rowenacall = 1
                            scene nbrb1 with dissolve
                            "..."
                            scene nbr with dissolve
                            "..."
                            scene hall_d with fade
                            b "{i} (...) {/i}"
                            call screen gnav
                        "Tidak mengatakan apa -apa":

                            scene hall_d with fade
                            b "{i} (...) {/i}"
                            call screen gnav
                else:

                    pass
                scene hall_d with fade
                b "{i} (...) {/i}"
                call screen gnav
        else:


            scene nbr14 with fade
            b "Hehehe wait"
            "Anda tinggal sebentar dan pulang"
            scene black
            "Kunjungi sekali lagi"
            scene hall_d with fade
            b "{i} (...) {/i}"
            call screen gnav
    else:
        scene nbr11 with dissolve
        b "{i}(Hmmm){/i}"
        "..."
        "Anda tinggal sebentar dan pulang"
        scene black
        "Kunjungi sekali lagi"
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc