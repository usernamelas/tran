label sdrinkreward:
    s "Tunggu di sini, saya akan segera kembali"
    b "Hmmm"
    scene slkmo with fade
    b "Apa ..."
    b "Sungguh!"
    scene slunch_hot3 with dissolve
    s "Ini adalah hadiah Anda karena Anda memberi saya minuman"
    s "Sekarang makan!"
    b "Yes ma'am"
    scene slunch_hot4 with dissolve
    "..."
    scene slunch_hot5 with fade
    b "Makanan enak"
    s "Anda menyukainya?"
    b "Yeah"
    scene slunch_hot6 with dissolve
    b "Lovely dress"
    s "Yes"
    b "Bisakah saya melihatnya?"
    b "Maksud saya"
    s "Setelah kita makan"
    b "Ok"
    scene slkmo1 with fade
    b "Hmmm"
    b "Sialan panas"
    scene slkmo2 with dissolve
    s "Tunggu!"
    b "Wow kamu tidak memakai celana dalam?"
    scene slkmo3 with dissolve
    s "..."
    b "Mari kita lihat"
    scene slkmo4 with dissolve
    s "Tolong berhenti [bname]"
    b "Hmm"
    b "Mari kita ambil foto Anda dalam hal ini"
    s "Untuk halaman saya?"
    b "Yes"
    s "Ok keren"
    scene slkmo5 with fade
    s "Saya akan mengenakan celana dalam"
    b "Anda tidak perlu"
    b "Itu tidak menunjukkan"
    b "Ubah pose"
    scene slkmo6 with dissolve
    "..."
    scene slkmo7 with dissolve
    b "Saya pikir Anda harus melepasnya!"
    s "No"
    b "Lalu, biarkan aku mengambil closeup seksi tanpa wajah"
    b "Ini bagus untuk halaman"
    s "Hmm"
    s "Ok"
    b "{i} (hehehe semua orang akan tahu itu kamu) {/i}"
    menu:
        "Kedudukan":
            scene slkmo8 with dissolve
            b "Itu keren"
            scene slkmo9 with dissolve
            "..."
            scene slkmo10 with dissolve
            b "Tembakan bagus"
            b "Biarkan saya melakukan closeup"
            scene slkmo11 with dissolve
            "..."
            b "Sedikit lagi"
            scene slkmo12 with dissolve
            b "Awesome"
            b "Sedikit lagi?"
            s "Tidak [bname] itu cukup"
            b "Ohh..."
            b "All right"
            scene slkmo5 with fade
            b "Sampai jumpa"
            scene door with fade
            b "{i} (...) {/i}"
            call screen gnav
        "Semua merangkak":


            scene slkmo13 with dissolve
            b "Itu tidak ada di keempatnya"
            s "Yes"
            b "Tapi aku akan mengambil sesuatu yang menyenangkan"
            b "Tetap seperti Anda"
            scene slkmo14 with dissolve
            b "Done"
            b "Ubah pose"
            scene slkmo15 with dissolve
            s "Apakah gaunnya baik -baik saja?"
            b "Yes awesome"
            b "Tunggu biarkan saya mengambilnya dari beberapa sudut"
            scene slkmo16 with dissolve
            "..."
            s "Tidak ada wajah, oke!?"
            b "Yes sure"
            scene slkmo17 with dissolve
            b "Bagus"
            b "Cobalah sesuatu yang lebih, saya percaya Anda bisa melakukan yang lebih baik"
            scene slkmo18 with dissolve
            $ persistent.unlock_14 = True
            if srel >= 300:
                b "Mungkin telanjang?"
                s "No face"
                b "Ok Ok"
                scene slkmo19 with dissolve
                s "Tidak ada wajah, aku membunuhmu"
                b "Don't worry"
                s "Ya tapi itu cukup untuk hari ini"
                b "Bagaimana dengan hadiah saya?"
                s "Bukankah ini cukup?"
                b "Tidak, saya menginginkan sesuatu untuk saya"
                s "Sesuatu apa?"
                scene slkmo20 with dissolve
                b "Seperti ini?"
                s "Hmm"
                s "Lakukan dengan cepat, saya memiliki hal -hal lain yang harus dilakukan"
                b "Ok"
                scene slkmo21 with dissolve
                s "Uhh"
                scene slkmo22 with hpunch
                b "Ahh"
                scene slkmo23 with dissolve
                b "Terima kasih"
                scene door with fade
                b "{i} (...) {/i}"
                call screen gnav
            else:


                pass
            s "No face"
            b "Ok Ok"
            s "Saya pikir itu cukup"
            b "Ya seperti yang Anda inginkan"
            b "Saya akan mengerjakannya nanti"
            b "Sampai jumpa"
            scene door with fade
            b "{i} (...) {/i}"
            call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
