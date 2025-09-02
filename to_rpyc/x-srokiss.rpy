image btvsa:
    "btvsa00.jpg"
    pause 0.01
    "btvsa01.jpg"
    pause 0.01
    "btvsa02.jpg"
    pause 0.01
    "btvsa03.jpg"
    pause 0.01
    "btvsa04.jpg"
    pause 0.01
    "btvsa05.jpg"
    pause 0.01
    "btvsa06.jpg"
    pause 0.01
    "btvsa07.jpg"
    pause 0.01
    "btvsa08.jpg"
    pause 0.01
    "btvsa09.jpg"
    pause 0.01
    "btvsa10.jpg"
    pause 0.01
    "btvsa11.jpg"
    pause 0.01
    "btvsa12.jpg"
    pause 0.01
    "btvsa13.jpg"
    pause 0.01
    "btvsa14.jpg"
    pause 0.01
    "btvsa15.jpg"
    pause 0.01
    "btvsa16.jpg"
    pause 0.01
    "btvsa17.jpg"
    pause 0.01
    "btvsa18.jpg"
    pause 0.01
    "btvsa19.jpg"
    pause 0.01
    "btvsa20.jpg"
    pause 0.01
    "btvsa21.jpg"
    pause 0.01
    "btvsa22.jpg"
    pause 0.01
    "btvsa23.jpg"
    pause 0.01
    "btvsa24.jpg"
    pause 0.01
    "btvsa25.jpg"
    pause 0.01
    "btvsa26.jpg"
    pause 0.01
    "btvsa27.jpg"
    pause 0.01
    "btvsa28.jpg"
    pause 0.01
    "btvsa29.jpg"
    pause 0.01
    "btvsa30.jpg"
    pause 0.01
    "btvsa31.jpg"
    pause 0.01
    "btvsa32.jpg"
    pause 0.01
    "btvsa33.jpg"
    pause 0.01
    "btvsa34.jpg"
    pause 0.01
    "btvsa35.jpg"
    pause 0.01
    "btvsa36.jpg"
    pause 0.01
    "btvsa37.jpg"
    pause 0.01
    "btvsa38.jpg"
    pause 0.01
    "btvsa39.jpg"
    pause 0.01
    "btvsa40.jpg"
    pause 0.01
    "btvsa41.jpg"
    pause 0.01
    "btvsa42.jpg"
    pause 0.01
    "btvsa43.jpg"
    pause 0.01
    "btvsa44.jpg"
    pause 0.01
    "btvsa45.jpg"
    pause 0.01
    "btvsa46.jpg"
    pause 0.01
    "btvsa47.jpg"
    pause 0.01
    "btvsa48.jpg"
    pause 0.01
    "btvsa49.jpg"
    pause 0.01
    "btvsa50.jpg"
    pause 0.01
    repeat



label srokiss:
    scene b_tv_s_r14 with hpunch
    b "Ouch"
    $ sflirtwithotherguys = 1
    if srel >=250:
        s "Mari ikut saya"
        scene b_tv_s_r16 with dissolve
        s "Sit"
        scene b_tv_s_r18 with dissolve
        s "Jangan pernah melakukannya lagi?"
        scene b_tv_s_r17 with dissolve
        b "Hehehe"
        scene b_tv_s_r18 with dissolve
        b "Lakukan apa?"
        s "Jangan pernah mencoba mencium Rowena, atau teman saya"
        b "Ya seolah -olah Anda memiliki orang lain selain Rowena"
        s "Aku sudah memperingatkanmu"
        b "Dan apa yang akan Anda lakukan?"
        s "Saya akan memasukkan ini ke dalam ..."
        s "Aku akan menggunakan ini untukmu"
        menu:
            "Tertawa":
                b "Ahahaha"
                if srel >=300:
                    s "Keluar!"
                    scene b_tv_s_r29 with dissolve
                    s "Tunggu!"
                    scene b_tv_s_r30 with dissolve
                    b "Apa?"
                    s "Berlutut!"
                    menu:
                        "Lakukan itu":
                            scene b_tv_s_r31 with dissolve
                            s "Kemarilah..."
                            s "Agar saya dapat memaafkan Anda"
                            scene b_tv_s_r32 with dissolve
                            s "Ahhh"
                            scene b_tv_s_r33 with dissolve
                            s "Yesss menciumnya dengan baik"
                            s "Cukup, Anda bisa pergi sekarang"
                            scene b_tv_s_r30 with dissolve
                            b "Apa -apaan"
                            s "Gadis lain kamu mencium mulut mereka"
                            $ sgrm = 1
                            s "Aku kamu mencium si kecilku"
                            s "Ingat itu"
                            b "Yeah right"
                            s "{i} (i \ 'll membuat dia membayar untuk ini) {/i}"
                            scene hall_d with fade
                            "..."
                            call screen gnav
                        "Meninggalkan":

                            b "Persetan"
                            show screen sreldw
                            $ srel -= 2
                            s "Mau mu"
                            hide screen sreldw
                            scene hall_d with fade
                            "..."
                            call screen gnav
                else:
                    pass
                s "Pergi!"
                s "Tinggalkan kamar"
                b "Hah! OKE"
                scene hall_d with fade
                "..."
                call screen gnav
            "Mengontrol":

                b "Ahahaha"
                s "Pergi!"
                s "Tinggalkan kamar"
                scene b_tv_s_r19 with hpunch
                s "Hey"
                scene b_tv_s_r20 with dissolve
                if sdom >=60:
                    s "Ahh"
                    scene b_tv_s_r22 with dissolve
                    s "Hahaha wait"
                    b "Too late"
                    s "Tolong jangan menyakiti saya"
                    b "Hmm"
                    scene b_tv_s_r23 with dissolve
                    b "{i} (kenapa dia masih menyimpannya di tangannya!?) {/i}"
                    scene b_tv_s_r24 with dissolve
                    "..."
                    menu:
                        "Ajari dia pelajaran":
                            b "Berikan ini padaku"
                            scene b_tv_s_r25 with dissolve
                            "..."
                            s "Ah"
                            scene b_tv_s_r27 with dissolve
                            s "Ahhhhhhh"
                            s "[bname] Harap berhenti"
                            b "Ok"
                            pass
                        "Melanjutkan":

                            pass


                    scene btvsa
                    s "Ahh"
                    b "Yesss"
                    s "[bname]"
                    s "Slowly"
                    scene b_tv_s_r28 with vpunch
                    b "Ahhh"
                    s "Keluar?!"
                    b "Yes"
                    scene b_tv_s_r29 with fade
                    b "Sampai jumpa lagi"
                    s "{i} (what a brengsek) {/i}"
                    scene hall_d with fade
                    "..."
                    call screen gnav
                else:


                    s "Hentikan [bname]"
                    b "Hehehe"
                    s "Aku bilang hentikan!"
                    b "OK"
                    scene b_tv_s_r21 with hpunch
                    b "Ouch"
                    s "Keluar"
                    scene hall_d with fade
                    "Naikkan poin dominasi Anda menjadi 60"
                    call screen gnav
    else:


        show screen sreldw
        $ srel -= 2
        b "Sorry"
        hide screen sreldw
        s "Don't speak"
        scene b_tv_s_r15 with dissolve
        b "Dia pergi"
        scene hall_d with fade
        "..."
        "Naikkan poin hubungan Anda menjadi 250"
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc