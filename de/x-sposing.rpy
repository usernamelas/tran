label sposing:
    scene spose with fade
    b "Wow"
    b "Barang Baru?"
    scene spose1 with dissolve
    b "Don't leave"
    scene spose2 with dissolve
    b "Bagaimana Anda menginginkannya?"
    s "Apa maksudmu?"
    b "Maksud saya, saya akan membiarkan Anda memilih kali ini"
    menu:
        "Coba di lantai" if sdom >=150:
            scene sfbja
            s "Uhh"
            "..."
            b "Yesss"
            s "Ughh"
            "..."
            scene slunchedend1 with dissolve
            b "Ahhh fuck!"
            scene slunchedend0 with dissolve
            "..."
            scene slunchedend with fade
            s "Hhh"
            b "Lihat yah"
            scene broom_day with fade
            "..."
            call screen gnav
        "Duduk":

            scene spose3 with dissolve
            b "{i}(Hmm){/i}"
            "..."
            s "Ughh"
            scene spose4 with dissolve
            s "Ahhh"
            scene spose5 with dissolve
            s "Mhhhm"
            scene spose6 with dissolve
            s "Ahhh"
            scene spose7 with dissolve
            s "[bname] Bukan pantatku"
            b "Ok"
            scene spose12 with dissolve
            s "Ahhh"
            scene spose13 with fade
            s "Apa? Pergi saja, saya akan santai sebentar"
            scene broom_day with fade
            "Ada pilihan lain selain duduk"
            "Jika Anda tidak mendapatkannya menaikkan poin DOM Anda menjadi 150"
            call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
