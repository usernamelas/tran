label study_event:
    s "Apa itu?"
    scene sroom_st2s with dissolve
    b "Hmm"
    scene sroom_st3s with dissolve
    b "Saya akan membantu Anda jika Anda memakai sesuatu yang bagus"
    scene sroom_st4s with dissolve
    s "Apa maksudmu?"
    b "Maksud saya sesuatu yang lebih baik dari apa yang Anda kenakan saat ini"
    if srel >=60:
        s "Hmm"
        s "Aku tidak tahu"
        b "Pikirkan itu seperti peragaan busana"
        s "Ok tetap saja"
        scene door with fade
        "..."
        s "Datang"
        b "{i} (mari kita lihat) {/i}"
        scene sroom_st5s with dissolve
        s "Anda menyukainya?"
        b "Hmm"
        b "Turn"
        scene sroom_st6s with dissolve
        s "Mengapa?"
        b "Saya ingin melihatnya"
        s "No"
        scene sroom_st7s with dissolve
        s "Katakan padaku kesepakatan atau tidak?"
        menu:
            "Tidak ada kesepakatan":
                if sdom >=25:
                    b "Hmm"
                    b "No deal"
                    s "Wait outside"
                    scene door with fade
                    "..."
                    s "Datang"
                    b "{i} (mari kita lihat) {/i}"
                    scene sroom_st10s with fade
                    s "Anda menyukainya?"
                    b "Hmm"
                    b "Turn"
                    scene sroom_st11s with dissolve
                    "..."
                    menu:
                        "[sname] Ayo!" if coversname == 1:
                            scene sroom_st10s with fade
                            s "Apa maksudmu?"
                            b "Saya telah menutupi Anda untuk halaman, menempatkan sesuatu yang bagus untuk saya"
                            scene sroom_st17s with dissolve
                            b "Saya akan mengambil beberapa foto"
                            scene sroom_st18s with dissolve
                            if srel >=80:
                                s "TIDAK..."
                                s "No photos"
                                b "Ok apapun yang kamu katakan"
                                s "Tolong tunggu di luar"
                                scene door with fade
                                "..."
                                s "Datang"
                                b "{i} (mari kita lihat) {/i}"
                                scene sroom_st19s with fade
                                b "Apakah bikini itu ..."
                                s "Ya itu itu"
                                b "Saya tidak bisa melihat bagian bawahnya"
                                scene sroom_st20s with hpunch
                                s "O M G Apa yang Harus Dilakukan Dengan Catatan Ulang Ini!"
                                b "Oh datang, yang saya tanyakan hanyalah jika Anda mengenakan bagian bawah"
                                s "Ya saya, di sini lihat"
                                scene sroom_st21s with dissolve
                                s "Senang?"
                                b "Wow yess"
                                b "Tentu saja, terlihat cantik"
                                b "{i} (apakah dia mencukur?) {/i}"
                                b "Bagaimanapun, mari kita mulai dengan studi Anda"
                                scene sroom_st22s with dissolve
                                b "Hmm"
                                b "Ya, begitulah cara Anda melakukannya"
                                scene sroom_st23s with dissolve
                                s "Terima kasih"
                                scene sroom_st24s with dissolve
                                b "{i} (wow putingnya) {/i}"
                                s "Well"
                                scene sroom_st23s with dissolve
                                s "Saya pikir itu semua untuk saat ini"
                                s "Jika saya membutuhkan sesuatu yang lain, saya akan bertanya kepada Anda"
                                b "Oh ok dapatkan, sampai jumpa"
                                s "Hati-hati"
                                scene door with fade
                                "..."
                                call screen gnav
                            else:

                                s "No"
                                s "Entah ini atau keluar"
                                b "Ok whatever"
                                pass
                        "Tidak buruk, datang duduk, mari kita mulai":


                            pass

                    scene sroom_st12s with fade
                    b "Ya, itu itu"
                    s "Sure"
                    menu:
                        "Tunggu biarkan saya melihat":
                            scene sroom_st13s with dissolve
                            b "Hmm"
                            b "Ya, itu saja, begitulah cara Anda melakukannya"
                            scene sroom_st14s with dissolve
                            s "Terima kasih"
                            scene sroom_st15s with dissolve
                            s "Well"
                            s "Saya pikir itu semua untuk saat ini"
                            s "Jika saya membutuhkan sesuatu yang lain, saya akan bertanya kepada Anda"
                            b "Oh ok dapatkan, sampai jumpa"
                            s "Hati-hati"
                            scene sroom_st16s with dissolve
                            "..."
                            scene door with fade
                            "..."
                            call screen gnav
                        "Ya percayalah":

                            b "Ya, percayalah pada yang satu itu"
                            scene sroom_st14s with dissolve
                            s "Terima kasih"
                            s "Nah, itu semua untuk saat ini"
                            s "Terima kasih"
                            scene door with fade
                            "..."
                            call screen gnav
                else:

                    scene sroom_stss_no with dissolve
                    s "Keluar"
                    scene door with fade
                    b "{i} (sialan yang dia patah!?) {/i}"
                    "Naikkan poin DOM Anda menjadi 25"
                    call screen gnav
            "Oke":
                scene sroom_st8s with fade
                b "Ya, itu itu"
                s "Sure"
                b "Tentu saja, percayalah pada yang satu itu"
                scene sroom_st9s with dissolve
                s "Terima kasih"
                s "Setidaknya saya bisa tidur siang sekarang"
                b "Oh ok dapatkan, sampai jumpa"
                scene door with fade
                "..."
                call screen gnav
    else:
        scene sroom_sts_no with vpunch
        s "Keluar!"
        scene door with fade
        b "{i} (sialan yang dia patah!?) {/i}"
        "Naikkan poin Anda menjadi 60"
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
