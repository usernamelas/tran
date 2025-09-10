label rbffight:
    $ rowenacall = 2
    scene rcall2 with fade
    a "Hai [bname] datanglah mari kita bicara"
    rb "Tidak perlu berbicara"
    scene rcall3 with hpunch
    rb "Tidak ada yang mengancam GF saya!"
    menu:
        "Melawan*":
            scene rcall4 with hpunch
            a "Aaaah !!!"
            scene rcall5 with hpunch
            a "Berhenti!!"
            scene black
            "..."
            scene rcall6 with fade
            s "Hah!"
            s "Apa yang Terjadi padamu"
            b "Saya bertengkar"
            s "Dengan siapa?"
            b "Err aku tidak mengenalnya, di jalanan"
            scene rcall7 with dissolve
            s "Ya Tuhan, ayo biarkan aku membawamu ke kamarmu"
            menu:
                "Lebih baik jika Anda menelepon [mname]*":
                    jump bruisesjen
                "Oke":
                    jump bruisesnad
        "Jangan":

            scene rcall8 with hpunch
            b "Ahhh"
            a "Berhenti!!!"
            scene rcall9 with dissolve
            a "Biarkan dia pergi! Anda membunuhnya"
            scene rcall10 with fade
            a "..."
            scene rcall11 with dissolve
            $ rowenacall = 3
            a "Ya ampun ..."
            b "Tolong beri saya perban"
            scene rcall12 with fade
            a "Here"
            b "Bisakah Anda membantu saya dengan itu?"
            scene rcall13 with fade
            a "..."
            b "Bisakah Anda memeriksa apakah saya memiliki memar di paha bagian dalam saya?"
            scene rcall14 with dissolve
            a "Huh"
            a "Yes"
            scene rcall15 with dissolve
            a "Hah!"
            b "Apa?"
            menu:
                "Berhenti menatap":
                    a "Ah maaf!"
                    "Rowena! Rowena!"
                    scene rcall17 with dissolve
                    a "{i} itu ibuku memanggil {/i}"
                    b "{i} oh saya pikir saya harus pergi {/i}"
                    "Rowena! Kamu ada di mana?"
                    scene broom_night with fade
                    "..."
                    $ rowena_mom = 1
                    call screen gnav
                "Berhenti menatap atau aku akan bercerita [sname] tentang lipstik*":

                    a "Hmmm"
                    a "Jadi itulah masalahnya!"
                    b "Apa maksudmu?"
                    b "Halo!! Lihatlah memar saya!"
                    b "Anda menyebabkan semua ini, bukan saya"
                    scene rcall12 with dissolve
                    a "Jadi apa yang kamu inginkan sekarang?"
                    b "A kiss"
                    scene rcall18 with dissolve
                    "..."
                    scene rcall19 with dissolve
                    "Halo semuanya"
                    scene rcall20 with dissolve
                    a "Oh hai ibu"
                    b "Hello ma'am"
                    b "Saya baru saja pergi"
                    scene broom_night with fade
                    $ rowena_mom = 1
                    b "{i} (Saya merasa saya telah melihat ibunya di suatu tempat) {/i}"
                    call screen gnav




label bruisesjen:
    scene brjen with fade
    b "It's nothing"
    scene brjen1 with dissolve
    m "Lepaskan bajumu"
    scene brjen2 with dissolve
    m "Ya Tuhan !!"
    b "Itu hanya tendangan, tidak ada yang perlu dikhawatirkan"
    m "[sname] Dapatkan saya solusi pembersihan"
    $ m_bbruises = 1
    scene brjen3 with fade
    m "Terima kasih [sname]"
    m "Please leave"
    s "Mengapa?"
    scene brjen4 with dissolve
    "Dia membisikkan sesuatu untuk [sname]"
    s "Oh ya oke"
    scene brjen5 with fade
    m "Almost done"
    scene brjen6 with dissolve
    m "Di mana \ 'adalah kain kasa"
    b "{i}(Oh shit){/i}"
    scene brjen7 with dissolve
    m "Dan lepaskan celana pendeknya, saya ingin memeriksa apakah Anda memiliki lebih banyak memar"
    b "Err"
    scene brjen5 with dissolve
    m "Saya akan menghapusnya"
    scene brjen8 with dissolve
    m "Hah!"
    m "Ya maksud saya bagus, tidak ada memar"
    scene brjen9 with dissolve
    m "Tarik Kembali celana pendek Anda"
    m "Saya akan pergi sekarang, hubungi jika Anda membutuhkan saya"
    scene door with fade
    b "{i} (...) {/i}"
    call screen gnav

label bruisesnad:
    scene brnad with fade
    s "Biarkan saya mendapatkan sesuatu untuk membersihkannya untuk Anda"
    b "It's nothing"
    $ s_bbruises = 1
    scene brnad1 with dissolve
    s "Bisakah Anda melepas bajumu?"
    b "Tidak, tolong hapus sendiri"
    scene brnad2 with dissolve
    s "Mhhm"
    s "Aku akan membersihkan ini untukmu"
    scene brnad3 with fade
    "..."
    b "Saya pikir ada memar di pangkal paha saya"
    if srel >=300:
        s "Dan biarkan saya menebak"
        s "Anda juga ingin saya menghapus celana pendek"
        b "Hehehe bagaimana kamu tahu"
        scene brnad4 with dissolve
        s "Hah!"
        b "Apa? Apakah saya memiliki memar?"
        s "Yes"
        s "No"
        s "Not bruises"
        b "Lalu bagaimana?"
        scene brnad5 with dissolve
        "..."
        scene brnad6 with dissolve
        s "Ini!"
        b "Aduh!"
        b "Hentikan!"
        s "Lihat Anda baik -baik saja, Anda hanya bermain drama"
        b "It's painful"
        s "Pokoknya sekarang memar Anda bersih, saya akan membuat Anda rileks"
        s "Hubungi jika Anda membutuhkan sesuatu"
        b "The Fuck [sname]"
        scene door with fade
        b "{i} (...) {/i}"
        call screen gnav
    else:

        s "Saya kira itu cukup"
        b "{i}(Damn){/i}"
        scene door with fade
        b "{i} (...) {/i}"
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
