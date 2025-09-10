label snamecon_efuck:
    $ ticketrequested = 5
    $ Hour += 4
    scene s_efuck with fade
    b "Di mana Anda akan berpakaian seperti ini, wanita muda?!"
    s "Haha"
    s "Concert"
    b "Konser saat ini?"
    s "Saya akan melihat Rowena terlebih dahulu"
    s "Lalu kita pergi di sore hari"
    b "Oh, begitu"
    b "Nikmati waktu Anda"
    scene s_efuck1 with dissolve
    b "{i} (mungkin saya bisa ...) {/i}"
    menu:
        "Saatnya menelepon Elaine":
            "..."
            b "Hi"
            $ elainefuck = 2
            e "{i}Hi [bname]{/i}"
            b "Bisakah kamu datang sekarang?"
            e "{i} Untuk apa? {/i}"
            b "Tentang perjanjian kami"
            e "{i} oh ok, kemana? {/i}"
            b "Rumah, tidak ada yang ada di sini"
            e "{i} ok beri saya satu jam tolong {/i}"
            b "Bagus, sampai jumpa"
            scene black with fade
            "..."
            scene s_efuck2 with dissolve
            e "Hi [bname]"
            b "Hi"
            e "Mari kita lakukan ini"
            scene s_efuck3 with fade
            b "Saya punya pertanyaan"
            e "Apa?"
            b "Apa yang tidak kamu pakai sesuatu yang bagus"
            e "Saya harus berbohong untuk merampok, bahwa saya akan berolahraga"
            b "Hmm begitu"
            scene s_efuck4 with dissolve
            e "..."
            b "Jadi apa yang diizinkan?"
            e "Anda hanya bisa menyentuh"
            b "Hah! Tidak ada blowjob? Setidaknya"
            e "Tidak, tidak ada"
            b "Tidak, terima kasih tidak perlu"
            scene s_efuck6 with dissolve
            "..."
            e "Lepaskan pakaian Anda"
            scene s_efuck5 with fade
            b "Uhhh"
            scene s_efuck7 with dissolve
            e "Pria muda yang mudah"
            e "Tidak lebih dari blowjob"
            scene s_efuck8 with dissolve
            b "Ouch"
            b "{i} (Saya harus bercinta jalang ini) {/i}"
            scene s_efuck9 with dissolve
            e "Arghh"
            b "Saya tidak akan bertahan lama"
            scene s_efuck10 with hpunch
            e "Ahhhh"
            b "Sungguh!"
            scene s_efuck11 with dissolve
            b "..."
            b "Itu ...."
            e "Saya harus pergi [bname]"
            b "Dingin"
            b "Lihat yah"
            scene black with fade
            "..."
            jump broom_menu
        "Pergi tidur":




            b "{i} (tidak ada yang bisa dilakukan, lebih baik saya beristirahat) {/i}"
            scene black with fade
            "..."
            jump broom_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
