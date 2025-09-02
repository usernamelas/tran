label sbtlc:
    s "Apakah Anda ingin saya menerapkan sesuatu untuk Anda?"
    b "Ya tolong, saya punya tabung di sana"
    scene bexerb1 with fade
    s "Hapus celana pendek Anda"
    scene bexerb2 with dissolve
    s "Mari kita lakukan ini"
    b "Lakukan apa?"
    scene bexerb3 with dissolve
    s "Untuk meletakkan lotion! Duh"
    b "Ya tapi lotion tidak akan membantu sebanyak hal lainnya"
    s "Hal lagi apa?"
    scene bexerb4 with dissolve
    b "Duh! Ini"
    scene bexerb5 with dissolve
    s "Jadi, bagaimana Anda ingin saya membantu?"
    menu:
        "Seks oral":
            s "Hmm"
            scene bexerb6 with dissolve
            s "Grrr"
            scene bexerb7 with dissolve
            s "Blaaahhh"
            b "[sname] Tidak ada waktu untuk bermain, saya kesakitan"
            scene bexerb8 with dissolve
            s "Boooo"
            scene bexerb9 with dissolve
            b "Itu saja aku keluar"
            s "Hahahaha"
            b "Berhentilah tertawa atau aku akan menghukummu"
            s "Ahahahahaha"
            scene bexerb10 with hpunch
            s "Aghh"
            scene bexerb11 with dissolve
            s "..."
            scene bexerb12 with dissolve
            b "Anda mungkin tertawa sekarang"
            s "..."
            scene broom_day with fade
            "..."
            jump broom_menu
        "Mengendarai":


            scene bexerb13 with dissolve
            "..."
            scene bexerb14 with dissolve
            s "Perlahan oke?"
            scene bexerb15 with dissolve
            s "Ahh"
            scene bexerb16 with dissolve
            "..."
            scene bexerb17 with dissolve
            s "Ahhh"
            scene bexerb18 with dissolve
            s "Persetan aku [bname] Persetan denganku!"
            scene bexerb19 with dissolve
            b "Saya ingin cum di pantat Anda"
            if sdom >=100:
                s "No [bname]"
                scene bexerb21 with dissolve
                s "[bname] Aku sudah memberitahumu NOOOOOO"
                scene bexerb22 with dissolve
                s "Ahhh"
                scene bexerb23 with dissolve
                s "..."
                scene bexerb24 with dissolve
                b "Sampai jumpa"
                s "Ahh"
                scene broom_day with fade
                "..."
                jump broom_menu
            else:

                s "Tidak [bname] hanya cum keluar"
                scene bexerb20 with dissolve
                b "Ahh"
                b "Anda mungkin pergi sekarang"
                scene broom_day with fade
                "Tingkatkan poin dominasi Anda menjadi 100"
                jump broom_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc