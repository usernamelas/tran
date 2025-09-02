label pagecheckphotoprogress:
    scene binstas2a with dissolve
    s "Wow! Kami memiliki nomor pengikut yang baik"
    b "Yes"
    b "Sudah kubilang!"
    scene binstas with dissolve
    s "Biarkan saya melihatnya lagi"
    s "Wow, aku tidak percaya mataku"

    menu:
        "Sentuh dia" if sphotos_progress == 0:
            scene binstas6 with dissolve
            $ sphotos_progress = 1
            b "{i} (pantat yang kuat) {/i}"
            scene binstas7 with dissolve
            b "{i} (...) {/i}"
            b "Yes"
            pass

        "Sentuh dia" if sphotos_progress == 1:
            scene binstas6 with dissolve
            b "{i} (pantat yang kuat) {/i}"
            scene binstas7 with dissolve
            b "{i} (...) {/i}"
            scene binstas6 with dissolve
            b "Yes"
            menu:
                "Tarik tali":
                    $ sphotos_progress = 2
                    scene binstas8 with dissolve
                    "..."
                    b "{i} (keren, tidak ada reaksi) {/i}"
                    pass
                "Melanjutkan":



                    pass


        "Sentuh dia" if sphotos_progress >= 2:
            scene binstas6 with dissolve
            b "{i} (pantat yang kuat) {/i}"
            scene binstas7 with dissolve
            b "{i} (...) {/i}"
            scene binstas6 with dissolve
            b "Yes"
            menu:
                "Tarik tali":
                    scene binstas8 with dissolve
                    "..."
                    b "{i} (keren, tidak ada reaksi) {/i}"
                    scene binstas9 with dissolve
                    s "Ok"
                    s "Bagus"
                    b "Bisakah Anda bayangkan, gambar telanjang apa yang akan dilakukan?"
                    s "Saya tahu [bname] tetapi saya tidak merasa seperti itu"
                    b "Ya bagaimanapun ..."
                    s "Jangan lupa untuk keluar"
                    s "Kami tidak ingin [mname] tersandung di atasnya"
                    scene binstas with dissolve
                    b "Yes right"
                    b "Dan kami akan menunggu hasil yang lebih baik"
                    scene binstas10 with dissolve
                    "Segera setelah Anda menutup halaman"
                    "Tab lain muncul"
                    s "Ewww"
                    s "Bagaimana dia bisa melakukan ini ...."
                    b "Ya itu terlalu besar untuk mulutnya"
                    s "Anda kotor!"
                    s "Dan cabul"
                    b "Hahaha"
                    s "Sekali lagi, terima kasih [bname]"
                    b "Sampai jumpa"
                    scene broom_night with fade
                    "..."
                    call screen gnav
                "Melanjutkan":



                    pass
        "Melanjutkan":

            pass

    scene binstas2a with fade
    s "Ok"
    b "Bagus!"
    s "Untuk saat ini"
    b "Sekarang kami menunggu hasilnya"
    s "Thanks [bname]"
    b "Sampai jumpa"
    scene broom_night with fade
    "..."
    call screen gnav

label pagecheckphotoprogressn:
    scene binstas2an with dissolve
    s "Ya!!"
    scene binstan with dissolve
    s "Luar biasa!"
    b "Saya pikir segera kita bisa mulai menghasilkan uang darinya!"
    s "Yeah"
    scene binstan1 with dissolve
    s "Thanks [bname]"
    s "Sampai jumpa"
    b "{i}(WTF){/i}"
    scene broom_night with fade
    "..."
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc