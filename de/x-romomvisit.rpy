label romomvisit:
    scene phardon with fade
    b "..."
    a "Biarkan berenang?"
    s "Yeah"
    scene phardon1 with dissolve
    b "..."
    scene romovisit with fade
    "..."
    scene romovisit1 with fade
    b "Saya akan menggunakan toilet"
    s "Ok"
    scene romovisit2 with fade
    b "{i} (Saya ingin mencoba dan meniduri keduanya) {/i}"
    rm "Apa yang terjadi!"
    scene romom2 with dissolve
    b "Huh"
    rm "Hmmm apa yang kita miliki di sini?"
    b "Err"
    scene romom3 with hpunch
    b "Ah"
    scene row_visit59b with fade
    rm "Ya jilat aku bagus"
    scene row_visit61b with dissolve
    rm "Hmm"
    scene row_visit62b with dissolve
    rm "..."
    scene row_visit63b with dissolve
    rm "Yes"
    scene row_visit64b with dissolve
    rm "Ya, jilat"
    scene row_visit67b with dissolve
    b "Ahh!"
    scene row_visit68b with dissolve
    "..."
    scene row_visit69b with dissolve
    rm "{i} (fuck it, dia rock keras) {/i}"
    rm "{i} (dan sangat besar, ini harus masuk ke pantat saya) {/i}"
    rm "{i} (Saya harus mengatur catatan baru) {/i}"
    scene romovisit3 with fade
    rm "Ahhhh"
    scene romovisit4 with dissolve
    rm "Waiiit!"
    scene row_visit70b with fade
    "..."
    scene romom5 with dissolve
    rm "Anda tidak datang ey!"
    rm "Maaf sayang saya tidak bisa membantu Anda lagi"
    scene romom6 with fade
    rm "{i} (You Do It Girl) {/i}"
    scene romom7 with fade
    s "Apakah Anda pikir dia dengan ibumu?"
    a "Jangan katakan itu"
    s "Saya harap dia tidak menidurinya"
    s "Hehehe"
    scene romovisit5 with dissolve

    s "Ah akhirnya, ini dia"
    a "[sname] Lihatlah sesuatu yang menyodok"
    s "Apa yang kamu lakukan di toilet?"
    a "Wanking ahahaha"
    b "Apa?"
    s "Hahahaha"
    if srel >= 300:
        a "Bisakah kita mengonfirmasi?"
        s "Mungkin kita bisa"
        scene romovisit6 with fade
        b "Apakah Anda berdua mabuk?"
        a "Ya Bisakah Anda menangani dua keledai mabuk yang indah?"
        s "Baringkan dan santai saja"
        scene romovisit7 with dissolve
        b "Ahh"
        b "{i} (bodoh [sname] Secara teknis adalah menjilati pantat ibu Rowena) {/i}"
        scene romom13 with fade
        a "Ahhh"
        scene romom14 with dissolve
        s "Ohhh"
        menu:
            "Persetan keduanya":
                scene beginrndf with dissolve
                b "..."
                scene rndf
                s "Ahh"
                "..."
                a "Mhhhm"
                "..."
                scene romovisit8 with fade
                b "Ahhhh"
                "..."
                s "Saatnya pergi"
                jump broom_menu
            "Fuck [sname]":

                scene romom15 with dissolve
                s "Yess"
                scene romovisit10 with dissolve
                s "Ahhh"
                scene romovisit11 with dissolve
                s "Ahhh"
                a "Ya Tuhan !!"
                scene romovisit12 with vpunch
                "..."
                scene romovisit13 with hpunch
                s "Ah shit"
                a "Itu bagus kan?"
                s "Yes"
                s "Let 's Go [bname]"
                jump broom_menu
            "Fuck Rowena":

                b "Continue Rowena"
                scene romvf
                a "Ahh"
                "..."
                a "Persetan dengan hidupku"
                "..."
                a "Please"
                scene romovisit9 with dissolve
                s "[bname] Cukup Anda akan membunuhnya"
                b "Pantat lucu akan baik -baik saja"
                s "Yeah"
                s "Saatnya pergi"
                jump broom_menu
    else:



        s "Ayo, biarkan pulang [bname]"
        "Naikkan [sname] Hubungan ke 300"
        jump broom_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
