label beachevent:
    scene b_relax_d7 with fade
    "..."
    s "Iaaaah!"
    scene beach with dissolve
    m "[bname]"
    scene beach1 with dissolve
    m "Apakah Anda bergabung dengan kami?"
    b "Tidak, saya akan berbaring dan menikmati matahari"
    scene beach2 with dissolve
    b "{i} (mungkin saya bisa mendapatkan tabir surya) {/i}"
    scene beach3 with fade
    "Bagaimana saya bisa membantu Anda hari ini Pak?"
    b "Saya ingin tabir surya"
    b "Tunggu! Berapa harga per potong?"
    "0"
    b "{i} (fuck it mahal!) {/i}"
    b "Bagaimanapun..."
    if mny <10:
        b "Terima kasih, tidak perlu"
        scene b_relax_d10 with fade
        s "Matahari kuat hari ini"
        b "Yeah"
        m "Pokoknya kami tidak tinggal lama"
        scene beach5 with dissolve
        "..."
        scene b_relax_d10 with dissolve
        m "Saya pikir sudah waktunya untuk kita pergi"
        s "Yeah whatever"
        scene b_relax_d11 with fade
        "..."
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav
    else:

        b "Oke, beri aku satu"
        scene beach4 with dissolve
        b "Thanks"
        $ mny -= 10
        scene b_relax_d10 with fade
        b "{i} (waktu untuk menggunakan lotion) {/i}"
        menu:
            "Gunakan diri Anda sendiri":
                scene b_tv_d11a with fade
                "..."
                b "{i} (saya masih punya beberapa) {/i}"
                b "{i} (mungkin saya bisa menawarkan ke ...) {/i}"
                menu:
                    "[mname]":
                        scene beach11 with dissolve
                        s "Ini sangat panas, saya pikir saya akan pergi berenang lagi"
                        b "{i} (keren, tepat waktu) {/i}"
                        scene beach12 with dissolve
                        b "Saya masih memiliki lotion"
                        m "Losion!?"
                        b "Yes"
                        b "Anda mau?"
                        m "Ok"
                        scene beach13 with fade
                        m "Letakkan beberapa di telapak tangan saya, lalu oleskan sisanya di punggung saya"
                        scene beach14 with dissolve
                        "..."
                        b "Hmm"
                        menu:
                            "Bagian atas akan menghalangi":
                                b "Bisakah saya melonggarkannya?"
                                scene beach15 with dissolve
                                if mrel >=50:
                                    m "ya sedikit"
                                    scene beach15a with dissolve
                                    m "Enough"
                                    b "Yes Ok"
                                    "..."
                                    m "Bukankah kamu sudah selesai?"
                                    b "Hampir, bisakah Anda berdiri, jadi saya bisa mencapai punggung bawah Anda"
                                    scene beach17 with dissolve
                                    b "Selesai di sini, apakah Anda ingin bagian belakang paha Anda tertutup?"
                                    if mrel >=60:
                                        m "Ok"
                                        scene beach17b with dissolve
                                        "..."
                                        menu:
                                            "Lakukan kaki":
                                                scene beach23c with dissolve
                                                "..."
                                                scene beach24c with dissolve
                                                m "Itu cukup [bname]"
                                                scene beach25c with dissolve
                                                s "Hai! Saya sudah selesai"
                                                s "Oh wow, tabir surya?"
                                                m "Yes"
                                                b "It's finished"
                                                s "Oh ok"
                                                scene beach19 with fade
                                                m "Saatnya pergi"
                                                $ sburnt = 1
                                                scene b_relax_d11 with fade
                                                "..."
                                                scene hall_d with fade
                                                b "{i} (...) {/i}"
                                                call screen gnav
                                            "Lakukan pantatnya":



                                                scene beach17c with dissolve
                                                "..."
                                                if mrel >=120:
                                                    scene beach18c with dissolve
                                                    "..."
                                                    m "[bname] ... saya pikir ..."
                                                    scene beach19c with dissolve
                                                    m "... Saya pikir itu cukup untuk hari ini"
                                                    m "Huh"
                                                    b "{i} (fuck saya pikir saya menyentuh vaginanya) {/i}"
                                                    b "{i} (kenapa dia berubah tiba -tiba!?) {/i}"
                                                    b "{i} (Saya perlu berpura -pura bahwa saya tidak terlihat) {/i}"
                                                    scene beach20c with dissolve
                                                    m "[bname]"
                                                    m "Ahem"
                                                    scene beach21c with dissolve
                                                    b "Yes"
                                                    m "Tanganmu!"
                                                    m "Stand up"
                                                    scene beach22c with dissolve
                                                    m "Mmm"
                                                    m "Honey"
                                                    m "Ada hal -hal yang ..."
                                                    scene beach25c with dissolve
                                                    s "Hai! Saya sudah selesai"
                                                    s "Oh wow, tabir surya?"
                                                    m "Yes"
                                                    b "It's finished"
                                                    s "Oh ok"
                                                    scene beach19 with fade
                                                    m "Saatnya pergi"
                                                    $ sburnt = 1
                                                    scene b_relax_d11 with fade
                                                    "..."
                                                    scene hall_d with fade
                                                    "Itu segalanya di sini"
                                                    b "{i} (...) {/i}"
                                                    call screen gnav
                                                else:




                                                    m "Saya pikir itu cukup [bname]"
                                                    "Naikkan poin Anda"
                                                    pass
                                    else:
                                        scene beach17 with dissolve
                                        m "Saya pikir itu cukup"
                                        pass
                                else:



                                    m "Tidak, teruskan saja"
                                    scene beach16 with dissolve
                                    m "Saya pikir itu cukup"
                                    "Naikkan poin Anda menjadi 50"
                                    pass
                            "Melanjutkan":

                                b "Saya pikir kita sudah selesai di sini"
                                scene beach16 with dissolve
                                m "Ya itu \ 'll do"
                                pass
                        scene beach18 with fade
                        s "Oh wow, tabir surya?"
                        m "Yes"
                        b "It's finished"
                        s "Oh ok"
                        scene beach19 with fade
                        m "Saatnya pergi"
                        $ sburnt = 1
                        scene b_relax_d11 with fade
                        "..."
                        scene hall_d with fade
                        b "{i} (...) {/i}"
                        call screen gnav
                    "[sname]":

                        scene beach20 with dissolve
                        s "Ugh itu sangat panas"
                        m "Ya, saya pikir kita harus masuk ke dalam air lagi"
                        s "Yes"
                        b "Ahem, [sname] ..."
                        m "Let's go"
                        s "Hanya sesaat aku akan mengikutimu"
                        "..."
                        scene beach21 with fade
                        b "Apakah Anda ingin tabir surya?"
                        s "Anda punya?"
                        b "Yes"
                        b "Biarkan aku menaruh untukmu"
                        s "Ya keren"
                        scene beach22 with fade
                        s "Perasaan yang bagus"
                        b "Yeah"
                        s "Beri aku beberapa, aku akan memakai di sini"
                        menu:
                            "Bisakah saya melepaskan bagian atas?":
                                if srel >=50:
                                    scene beach24 with dissolve
                                    s "Hmmm"
                                    scene beach25 with dissolve
                                    s "Bukan untie penuh"
                                    scene beach26 with dissolve
                                    s "Lambat, tidak penuh, saya katakan"
                                    b "Ok"
                                    b "Ingin saya melakukan bagian belakang kaki Anda sekarang?"
                                    s "Yep"
                                    scene beach27 with fade
                                    b "..."
                                    scene beach28 with dissolve
                                    b "{i}Focus [bname]{/i}"
                                    d "Enough [bname]"
                                    scene beach29 with dissolve
                                    s "Terima kasih"
                                    pass
                                else:
                                    scene beach23 with fade
                                    s "No"
                                    s "Saya pikir itu cukup"
                                    b "Err ok"
                                    "Naikkan poin Anda menjadi 50"
                                    pass
                            "Melanjutkan":


                                scene beach23 with fade
                                s "Saya pikir itu cukup"
                                b "Err ok"
                                pass

                        scene beach30 with fade
                        m "Dari mana Anda mendapatkan tabir surya?"
                        s "[bname] memilikinya"
                        b "Yeah"
                        m "Beri aku beberapa"
                        b "It's finished"
                        m "Ahh"
                        scene beach31 with fade
                        m "Saatnya pergi"
                        $ mburnt = 1
                        scene b_relax_d11 with fade
                        "..."
                        scene hall_d with fade
                        b "{i} (...) {/i}"
                        call screen gnav
            "Menawarkan ke [sname]":



                s "Yeah thanks"
                pass
            "Menawarkan ke [mname]":

                m "Ya terima kasih"
                pass


        b "Haruskah saya menempatkan untuk Anda?"
        s "Tidak, terima kasih kami akan mengelola"
        scene beach6 with fade
        m "Saya pikir itu cukup"
        scene beach7 with dissolve
        "..."
        scene beach8 with dissolve
        m "Tolong taruh untukku"
        scene beach9 with fade
        b "Hei, bagaimana dengan saya?"
        s "Maaf [bname], sudah selesai"
        scene beach10 with fade
        b "{i}(Damn){/i}"
        scene black
        "Setelah beberapa saat"
        scene b_relax_d10 with fade
        m "Saya pikir sudah waktunya untuk kita pergi"
        s "Yeah"
        scene b_relax_d11 with fade
        "..."
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
