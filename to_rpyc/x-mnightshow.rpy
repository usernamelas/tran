label mnightshow:
    m "Ayo saya ingin menunjukkan sesuatu kepada Anda"
    b "Ok"
    scene mnshow with fade
    if elaine_convince ==4 and mrel >=150:
        pass
    else:
        m "Turn away"
        pass
    m "I'll change"
    "..."
    m "Oh..."
    scene mnshow1 with dissolve
    m "Dapatkah Anda membantu saya melepas ini"
    b "{i} (keren ...) {/i}"
    b "Yes sure"
    scene mnshow2 with dissolve
    "..."
    scene mnshow3 with dissolve
    m "Biarkan aku mengambil tanganku"
    if elaine_convince ==4 and mrel >=150:
        scene mnshow4a with dissolve
        m "Saya akan menunjukkan apa yang saya beli"
        scene mnshow5a with fade
        "..."
        pass
    else:
        m "Tutup matamu"
        scene mnshow4 with dissolve
        m "Saya akan menunjukkan apa yang saya beli"
        m "Mata tertutup?"
        b "Yes"
        m "Turn away"
        scene mnshow5 with fade
        "..."
        pass

    scene mnshow6 with fade
    m "Jadi bagaimana menurut Anda?"
    b "{i} (sialan saya pikir sesuatu yang panas) {/i}"
    b "Uhmm bagus"
    m "Sepertinya Anda tidak menyukainya"
    if mnurseoutfit == 3 and mrel >=250:
        m "Putar aku akan menunjukkan sesuatu yang lain"
        scene mnshow7 with fade
        "..."
        scene mnshow8 with fade
        b "Wow jadi kamu sudah memutuskan untuk memakainya?"
        m "Hmm ya, hanya untuk saat ini"
        scene mnshow9 with dissolve
        m "{i} (apa yang kamu lakukan [mname]!) {/i}"
        menu:
            "Semakin dekat":
                b "Apa yang salah?"
                scene mnshow11 with dissolve
                m "Tidak ada yang salah sayang"
                b "Tapi tiba -tiba Anda menjadi terdiam"
                menu:
                    "Lihatlah":
                        scene mnshow12 with dissolve
                        b "{i} (fuck!) {/i}"
                        b "{i} (jika saya melanjutkan ini, saya akan mendapatkan ereksi) {/i}"
                        scene mnshow11 with dissolve
                        b "{i}(Shit){/i}"
                        scene mnshow13 with dissolve
                        m "Hah!"
                        scene mnshow15 with dissolve
                        b "{i}(Shit){/i}"
                        $ mcorr += 1
                        scene mnshow13 with dissolve
                        if mcorr >=25 and mbikinirequest ==1:
                            m "Anda tahu, Anda ingin melihat bikini dan mengambil foto untuk saya sebelumnya"
                            b "Yes"
                            m "Saya telah memutuskan untuk membiarkan Anda mengambil dua"
                            b "Ok keren"
                            scene mnshow16 with dissolve
                            "..."
                            scene mnshow17 with dissolve
                            "..."
                            scene mnshow18 with dissolve
                            m "Biarkan saya mendapatkan bikini"
                            scene mnshow19 with fade
                            m "Jadi di mana kita mengambil foto?"
                            b "Mungkin di dinding adalah ide yang bagus"
                            m "Ok"
                            b "Saya akan membersihkan area tersebut"
                            scene mnshow20 with fade
                            "..."
                            b "Bagus"
                            m "Satu lagi tersisa"
                            m "Ok cobalah untuk bersandar di dinding"
                            scene mnshow21 with dissolve
                            "..."
                            scene mnshow22 with dissolve
                            m "Saya pikir itu cukup untuk hari ini"
                            b "Ok"
                            m "Jangan lupa mengirimi saya fotonya"
                            b "{i} (wow shit!) {/i}"
                            b "{i} (Saya mengambilnya di ponsel saya keren!) {/i}"
                            $ mphotos = 1
                            pass
                        else:

                            "Naikkan korupsi Anda menjadi 25 poin"
                            "Dan Anda perlu memintanya untuk mengenakan bikini di lain waktu"
                            pass
                        m "Selamat malam sayang"
                        b "Selamat malam"
                        scene black
                        "SEMENTARA ITU"
                        scene jbpractice31 with fade
                        s "I'm studying"
                        m "Saya bisa melihatnya"
                        m "Setelah selesai, Anda bisa keluar dari kamar Anda"
                        s "Thanks"
                        jump bs_afterjmassage
                    "Katakan padanya untuk tidak khawatir":

                        b "Jangan khawatir, semuanya akan baik -baik saja"
                        m "Aku tahu"
                        m "Saya hanya merasa tidak enak tentang sesuatu"
                        scene mnshow14 with dissolve
                        m "Terima kasih telah mendukung saya"
                        b "..."
                        m "Selamat malam"
                        b "Oke, saya akan pergi"
                        scene black
                        "SEMENTARA ITU"
                        scene jbpractice31 with fade
                        s "I'm studying"
                        m "Saya bisa melihatnya"
                        m "Setelah selesai, Anda bisa keluar dari kamar Anda"
                        s "Thanks"
                        jump bs_afterjmassage
            "Melanjutkan":

                b "Apa yang salah?"
                scene mnshow10 with fade
                m "Itu [bname]"
                m "Aku akan tidur"
                m "Selamat malam"
                b "Oke, saya akan pergi"
                scene black
                "SEMENTARA ITU"
                scene jbpractice31 with fade
                s "I'm studying"
                m "Saya bisa melihatnya"
                m "Setelah selesai, Anda bisa keluar dari kamar Anda"
                s "Thanks"
                jump bs_afterjmassage
    else:



        m "Ok terima kasih telah memeriksanya dengan saya"
        m "Selamat malam"
        b "Oke, saya akan pergi ke kamar saya"
        "Ada sesuatu yang bisa Anda beli untuknya, jika sudah melakukannya, maka poin Anda tidak cukup"
        "300 dibutuhkan"
        scene black
        "SEMENTARA ITU"
        scene jbpractice31 with fade
        s "I'm studying"
        m "Saya bisa melihatnya"
        m "Setelah selesai, Anda bisa keluar dari kamar Anda"
        s "Thanks"
        jump bs_afterjmassage
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc