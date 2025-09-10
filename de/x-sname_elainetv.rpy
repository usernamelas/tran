label sname_elainetv:
    scene s_etv with fade
    b "Apa yang sedang kamu lakukan?"
    s "Hanya sedetik, saya sudah selesai"
    scene s_etv1 with dissolve
    b "Kuku?"
    s "Yes"
    menu:
        "Boleh saya lihat?":
            scene s_etv2 with dissolve
            s "Kuku saya?"
            b "Yes"
            scene s_etv3 with dissolve
            s "Here"
            b "Keren, mari kita ambil beberapa foto dengannya"
            s "Ya kenapa tidak"
            pass
        "Apakah Anda ingin mengambil beberapa foto?":

            scene s_etv4 with dissolve
            s "Ya dengan kuku saya mengagumkan"
            pass

    scene s_etv5 with fade
    b "It's cute"
    b "Tetapi..."
    b "Itu lebih lucu tanpa pakaian"
    if sbm ==1:
        s "Hmm"
        s "Ok"
        scene s_etv7 with dissolve
        b "Bagus"
        scene s_etv8 with dissolve
        "..."
        scene s_etv9 with dissolve
        b "{i} (saya tidak perlu memintanya untuk berpose) {/i}"
        scene s_etv10 with hpunch
        b "Sungguh!"
        scene s_etv11 with dissolve
        s "Cukup untuk hari ini"
        b "{i}(Damn){/i}"
        scene s_etv13 with fade
        b "Tapi kenapa?"
        s "Selamat malam"
        jump newdays

    elif sbm ==2:
        s "Hmm"
        s "Hanya jika Anda membersihkan kamar saya"
        b "Apa?"
        s "Anda telah mendengar saya"
        b "Seperti sekarang?"
        b "Saat ini?"
        s "Ya, atau saya tidak melepas apapun"
        b "{i}(Hmm){/i}"
        b "OK"
        s "Apa yang kamu tunggu?"
        s "Pergi dapatkan kuas dan mulailah!"
        scene door with fade
        b "{i} (dia ingin bermain mata) {/i}"
        b "{i} (setelah insiden malam itu) {/i}"
        scene s_etv14 with fade
        "..."
        scene s_etv15 with dissolve
        b "Done"
        b "Sekarang lepaskan dan biarkan saya mendapatkan beberapa pemotretan"
        s "Not yet"
        s "Saya menginginkan sesuatu yang lain"
        b "Hah!"
        scene s_etv16 with dissolve
        b "Apa itu?"
        s "Uang"
        b "Apa!!"
        s "Saya ingin 00"
        b "Untuk 00 saya akan mendapatkan seorang gadis untuk satu malam"
        s "Pergi mendapatkan seorang gadis dan tidak ada foto untukku"
        menu:
            "Meninggalkan":
                scene s_etv17 with dissolve
                b "Saya tidak bermain game seperti itu [sname]"
                s "Pervert"
                b "Selamat malam"
                jump newdays
            "Berikan dia 00":

                if mny>=100:
                    b "Ini dia"
                    s "Thanks"
                    scene s_etv8 with fade
                    b "Bagus"
                    $ mny -= 100
                    scene s_etv9 with dissolve
                    "..."
                    scene s_etv10 with hpunch
                    b "Sungguh!"
                    scene s_etv12 with dissolve
                    "..."
                    scene s_etv18 with dissolve
                    b "{i} (00 sepadan) {/i}"
                    menu:
                        "Lakukan sesuatu yang gila":
                            scene s_etv19 with vpunch
                            s "Ahhh!"
                            scene s_etv20 with dissolve
                            s "Turunkan aku!"
                            scene s_etv13 with dissolve
                            s "Saya lelah [bname]"
                            b "Serius, ketika mulai menyenangkan?!"
                            scene s_etv21 with fade
                            s "Saya harus tidur"
                            s "Ini terlambat untuk permainan kami"
                            b "Apa maksudmu terlambat?"
                            b "Apa pun!"
                            b "Selamat malam"
                            b "{i} (oh apa ini?) {/i}"
                            scene s_etv22 with dissolve
                            b "Hmm"
                            b "Ok"
                            scene s_etv21 with dissolve
                            b "Selamat malam"
                            scene door with fade
                            b "{i} (Saya harus mencari tahu apa yang terjadi) {/i}"
                            menu:
                                "Pergi tidur":
                                    jump newdays
                                "Kembali ke sana":

                                    b "Hmm"
                                    b "Mungkin saya tidak boleh?"
                                    "SEMENTARA ITU"
                                    scene s_etv23 with fade
                                    s "..."
                                    scene s_etv24 with dissolve
                                    b "Ahaa!"
                                    s "Ahhh"
                                    scene s_etv25 with dissolve
                                    s "Ya Tuhan, kamu menangkapku"
                                    b "Mengapa Anda menggunakan ini saat Anda memiliki real deal"
                                    s "Anda benar, saya tidak tahu apa yang terjadi pada saya"
                                    if srel>=150:
                                        s "Saya pikir saya pantas dihukum"
                                        b "Anda yakin melakukannya"
                                        s "Apakah Anda memiliki tali?"
                                        b "Ya saya akan kembali"
                                        s "Tapi tidak ada yang masuk, oke?"
                                        b "Apa maksudmu?"
                                        s "Tidak ada penetrasi, berjanji padaku?"
                                        s "Hanya hal -hal yang menyenangkan"
                                        b "Ok whatever"
                                        scene s_etv26 with fade
                                        s "Tolong kasihanilah"
                                        b "{i} (Saya suka bagaimana dia memainkannya) {/i}"
                                        menu:
                                            "Seks oral":
                                                scene s_etv27 with dissolve
                                                s "Ahh"
                                                scene s_etv28 with fade
                                                b "Kiss it"
                                                scene s_etv29 with dissolve
                                                b "Anak yang baik"
                                                scene s_etv30 with dissolve
                                                b "Ahh"
                                                scene s_etv31 with dissolve
                                                b "Ya!"
                                                scene s_etv32 with dissolve
                                                b "Ahhh"
                                                scene s_etv33 with fade
                                                s "Tolong lepaskan aku"
                                                b "Selamat malam"
                                                scene door with fade
                                                b "{i} (itu bagus) {/i}"
                                                scene s_etv34 with fade
                                                "..."
                                                scene s_etv35 with dissolve
                                                s "{i} (mengagumkan!) {/i}"
                                                scene s_etv34 with dissolve
                                                $ srbm = 1
                                                s "{i} (Anda ingin bermain, mari kita lihat siapa yang akan menang) {/i}"
                                                scene black
                                                "..."
                                                jump newdays
                                            "Seks":



                                                scene s_etv36 with fade
                                                "..."
                                                scene s_etv37 with dissolve
                                                s "Please [bname]"
                                                s "Tidak ada penetrasi!"
                                                scene s_etv38 with dissolve
                                                b "Syi!"
                                                s "Tolong tidak !!"
                                                b "Shh aku hanya menggosoknya"
                                                b "Anda harus dihukum"
                                                scene s_etv39 with dissolve
                                                "..."
                                                scene s_etv40 with dissolve
                                                s "Ahhh"
                                                b "{i} (fuck !! dia super basah) {/i}"
                                                scene s_etv41 with dissolve
                                                "..."
                                                s "Tolong lepaskan aku"
                                                b "Selamat malam"
                                                scene door with fade
                                                b "{i} (itu bagus) {/i}"
                                                scene s_etv34 with fade
                                                "..."
                                                scene s_etv35 with dissolve
                                                s "{i} (mengagumkan!) {/i}"
                                                $ srbm = 1
                                                scene s_etv34 with dissolve
                                                s "{i} (Anda ingin bermain, mari kita lihat siapa yang akan menang) {/i}"
                                                scene black
                                                "..."
                                                jump newdays
                                    else:



                                        s "Silakan pergi [bname]"
                                        b "Apa -apaan! Aku tidak akan pergi"
                                        s "Silakan pergi atau saya akan berteriak"
                                        b "Persetan denganmu!"
                                        scene door with fade
                                        b "{i} (dia tidak normal) {/i}"
                                        "Naikkan poin Anda menjadi 150"
                                        jump newdays
                        "Melanjutkan":






                            b "Wow!"
                            s "Selamat malam [bname]"
                            scene s_etv13 with fade
                            b "Tapi kenapa?"
                            s "Selamat malam"
                            jump newdays
                else:



                    b "Maaf saya tidak punya uang sekarang"
                    scene s_etv17 with dissolve
                    b "Selamat malam"
                    s "Selamat malam"
                    jump newdays
    else:

        s "Hmm"
        s "Ok"
        scene s_etv7 with dissolve
        "..."
        b "Sedikit lagi"
        scene s_etv6 with dissolve
        s "Enough [bname]"
        s "Please go"
        b "OK"
        b "{i} (kurasa aku akan tidur sekarang) {/i}"
        jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
