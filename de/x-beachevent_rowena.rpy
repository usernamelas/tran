label beachevent_rowena:
    scene beachr with fade
    s "Bagus karena Anda tidak memakai yang lain"
    a "Of course"
    if saction ==0:
        rb "Tempat ini membosankan"
        rb "Kami seharusnya pergi ke tempat favorit saya"
        scene beachr1 with dissolve
        s "Tempat favoritnya?"
        a "Aku akan memberitahumu nanti"
        scene beachr2 with fade
        rb "... ya itu jauh lebih baik"
        b "Dimana pantai itu?"
        s "Ini adalah pantai telanjang [bname]"
        "Dia berbisik"
        b "Oh keren, kita harus pergi ke sana"
        scene beachr3 with dissolve
        s "Serius?"
        b "Ini akan bagus untuk halaman Anda"
        s "Ya dengan m ..."
        b "Ahem"
        s "Dengan [mname] pergi bersama kami"
        scene beachr4 with dissolve
        a "Kita bisa pergi sendiri selama hari kerja"
        s "Ya tapi saya tidak melepas pakaian saya"
        a "Ya tidak apa -apa, kami akan hahaha"
        a "Mari kita berenang"
        pass
    else:

        rb "Tempat ini membosankan"
        rb "Kami seharusnya pergi ke tempat favorit saya"
        scene beachr1 with dissolve
        s "Katakan padanya untuk tetap diam"
        scene beachr2 with fade
        b "Saya pikir itu lebih baik"
        s "Shhh"
        "Dia berbisik"
        scene beachr3 with dissolve
        a "Jadi, apakah kita akan berenang atau apa?"
        b "Dalam telanjang"
        s "[bname]!"
        scene beachr4 with dissolve
        a "Hahaha"
        a "Let's go"
        pass
    menu:
        "[sname] Tetap":
            s "Kamu pergi sendiri, aku akan tinggal"
            a "Mengapa?"
            s "Saya tidak dalam mood"
            a "Ok"
            scene beachr6 with fade
            s "Tolong beri kami lotion"
            b "Hah! Anda terdengar seperti Anda memberi pesanan"
            scene beachr7 with dissolve
            s "Hehe please"
            scene beach3 with fade
            "Bagaimana saya bisa membantu Anda hari ini Pak?"
            b "Saya ingin tabir surya"
            b "Tunggu! Berapa harga per potong?"
            "0"
            b "Tolong beri saya satu"
            scene beach4 with dissolve
            b "Thanks"
            scene beachr8 with fade
            b "Anda harus menempatkan saya setelah itu"
            s "Ok"
            menu:
                "Bisakah saya melepaskan bagian atas?":
                    if srel >=50:
                        scene beachr9 with dissolve
                        s "Hmmm"
                        s "Bukan untie penuh"
                        scene beachr10 with dissolve
                        s "Lambat, tidak penuh, saya katakan"
                        b "Ok"
                        b "Ingin saya melakukan bagian belakang kaki Anda sekarang?"
                        s "Yes"
                        scene beachr11 with fade
                        b "..."
                        scene beachr12 with dissolve
                        b "{i} fokus! {/i}"
                        d "Enough [bname]"
                        s "Terima kasih"
                        b "Bisakah Anda menempatkan saya sekarang?"
                        s "Yes"
                        scene beachr13 with fade
                        "..."
                        b "Bisakah Anda meletakkan kaki saya?"
                        s "Ya, berdiri"
                        scene beachr14 with fade
                        s "Tidak seperti ini [bname]"
                        b "Mengapa tidak?"
                        scene beachr15 with dissolve
                        s "Duh! Apakah Anda ingin saya mengenakan penis Anda atau apa yang Anda cabul?"
                        b "Hahaha ok"
                        scene beachr18 with fade
                        a "Oh apakah ada tabir surya yang tersisa"
                        s "Tidak, maaf"
                        scene black
                        "Anda meluangkan waktu dan kemudian kembali ke rumah"
                        scene beachr19 with fade
                        "..."
                        scene hall_d with fade
                        b "{i} (...) {/i}"
                        call screen gnav
                    else:

                        scene beachr16 with fade
                        s "No"
                        s "Saya pikir itu cukup"
                        b "Err ok"
                        "Naikkan poin Anda menjadi 50"
                        scene black
                        "..."
                        scene beachr17 with fade
                        a "Oh apakah ada tabir surya yang tersisa"
                        b "No Sorry itu selesai"
                        scene black
                        "Anda meluangkan waktu dan kemudian kembali ke rumah"
                        scene beachr19 with fade
                        "..."
                        scene hall_d with fade
                        b "{i} (...) {/i}"
                        call screen gnav
                "Melanjutkan":


                    scene beachr16 with fade
                    s "Saya pikir itu cukup"
                    b "Err ok"
                    scene black
                    "..."
                    scene beachr17 with fade
                    a "Oh apakah ada tabir surya yang tersisa"
                    b "No Sorry itu selesai"
                    scene black
                    "Anda meluangkan waktu dan kemudian kembali ke rumah"
                    scene beachr19 with fade
                    "..."
                    scene hall_d with fade
                    b "{i} (...) {/i}"
                    call screen gnav
        "Mereka semua pergi":


            scene beachr5 with fade
            "..."
            scene black
            "Anda meluangkan waktu dan kemudian kembali ke rumah"
            scene beachr19 with fade
            "..."
            scene hall_d with fade
            b "{i} (...) {/i}"
            call screen gnav

    scene beachr19 with fade
    "..."
    scene hall_d with fade
    b "{i} (...) {/i}"
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
