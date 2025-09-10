label rowenatoilet:
    scene toi_rws with dissolve
    a "Hmmm"
    scene toi_rws1 with dissolve
    b "Err"
    b "Apa yang sedang kamu lakukan?"
    b "[sname] ada di rumah"
    a "Kami punya waktu untuk quickie"
    a "Dan saya mengunci pintu"
    scene toi_rws2 with dissolve
    "..."
    scene toi_rws3 with dissolve
    b "Ya, kenapa tidak"
    scene toi_rws4 with dissolve
    a "Ahh"
    a "Membuka pakaian saya dulu"
    scene toi_rws5 with fade
    a "Yes better"
    scene toi_rws6 with dissolve
    a "Ahhh"
    $ persistent.unlock_16 = True
    b "SHHH, diam"
    scene toi_rws7 with dissolve
    a "Ahhhh"
    scene toi_rws8 with dissolve
    b "Diam!"
    scene black
    "SEMENTARA ITU"
    scene toi_rws9 with fade
    s "{i} apa yang membuatnya begitu lama {/i}"
    scene toi_rws7 with dissolve
    b "Yes"
    menu:
        "Air mani":
            scene toi_rws10 with hpunch
            b "Ahhh!"
            scene toi_rws11 with fade
            b "Cepat, pergi sebelum [sname] mulai mencari Anda"
            a "Ahhh ... ok"
            b "Sampai jumpa"
            scene room3 with fade
            "..."
            call screen gnav
        "Melanjutkan":

            scene toi_rws12 with fade
            b "Ya!"
            scene toi_rws13 with dissolve
            a "Hmmm"
            scene toi_rws14 with fade
            b "Ahhh"
            s "Rowena! Apakah kamu masih di sana?"
            a "Hah!"
            scene toi_rws15 with dissolve
            a "Ya, hanya sedetik"
            b "Sungguh!"
            scene toi_rws16 with dissolve
            s "Kenapa lama sekali?"
            s "Errm, apakah Anda memutuskan untuk mandi?"
            scene toi_rws17 with dissolve
            a "Tidak Memangnya kenapa?"
            s "Karena Anda benar -benar telanjang"
            a "Ah ya, saya lebih suka menggunakan toilet telanjang"
            s "Hmm begitu"
            a "Pokoknya saya sudah selesai"
            s "Ok"
            scene toi_rws18 with fade
            s "{i} Saya bertanya -tanya di mana [bname] {/i}"
            scene broom_day with fade
            b "{i} itu sudah dekat {/i}"
            call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
