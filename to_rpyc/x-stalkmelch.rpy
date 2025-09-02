label stalkmelch:
    if stalkrp <=1:
        scene bfmch0 with fade
        $ stalkrp += 1
        b "Hmm"
        b "{i} tidak ada yang ada di sini {/i}"
        b "{i} Waktunya pulang {/i}"
        b "{i} i \ 'll coba lagi besok {/i}"
        jump broom_menu

    elif stalkrp >=2:
        scene bfmch with fade
        $ stalkrp += 1
        b "Aha"
        b "{i}Calm [bname]{/i}"
        $ bnamefixcheryl = 5
        scene bfmch1 with fade
        ml "Jangan giliran, lirik saja di sudut itu"
        ml "Saya pikir seseorang menguntit kami"
        scene bfmch2 with dissolve
        c "Hmmm"
        c "[bname] !!"
        scene bfmch1 with dissolve
        c "Bagaimana Anda melihatnya?"
        ml "Bukan itu masalahnya"
        ml "Tahukah Anda mengapa dia menguntit kami?"
        c "Saya pikir ya"
        ml "Apa maksudmu?"
        ml "Apakah dia tahu?"
        c "Tidak, itu sesuatu yang lain"
        scene bfmch3 with dissolve
        b "{i} sialan, itu terlalu lama {/i}"
        scene bfmch4 with dissolve
        ml "Bagaimana Sales Payton?"
        "Tidak buruk"
        scene bfmch5 with dissolve
        c "Aku akan pergi sekarang Melinda"
        ml "Tunggu, kami pergi bersama"
        c "Tidak, biarkan aku kalah [bname] Pertama"
        scene bfmch6 with fade
        b "{i} Oh! Apakah dia datang mengunjungi kami? {/i}"
        scene bfmch7 with dissolve
        b "..."
        scene bfmch8 with dissolve
        b "{i} Apakah dia melihat [sname]! {/i}"
        b "{i} i \ 'll temukan {/i}"
        scene bfmch9 with fade
        b "Huh"
        scene bfmch10 with dissolve
        b "{i} apa -apaan {/i}"
        b "{i} i \ 'll GO in {/i}"
        scene bfmch11 with fade
        b "Hi"
        c "Hi [bname]"
        b "Saya perlu berbicara dengan Anda"
        c "Beri tahu saya"
        b "Tolong secara pribadi"
        c "Baiklah, saya tetap akan pergi"
        scene bfmch13 with fade
        c "Jadi?"
        if persistent.patch_enabled:
            b "Terakhir kali saya bertanya kepada Anda untuk tidak memberi tahu ayah tentang ibu"
            pass
        else:
            b "Terakhir kali saya meminta Anda untuk tidak memberi tahu Stewart tentang [mname]"
            pass
        c "Ya saya ingat"
        b "Bagus"
        c "Dan saya ingat memberi tahu Anda mengapa tidak"
        c "Dan Anda bilang Anda akan memberi tahu saya nanti"
        b "..."
        c "Jadi sekali lagi saya bertanya mengapa saya tidak harus memberitahunya"
        menu:
            "Mengancamnya":
                b "Karena jika Anda memberitahunya"
                b "Saya juga bisa menceritakan hal -hal tentang Anda"
                c "Hal -hal seperti apa"
                b "Saya tahu tentang Anda dan Melinda"
                scene bfmch12 with dissolve
                "..."
                c "Saya harus pergi sekarang"
                pass
            "Mainkan Nada Belas Kasihan":
                b "Tolong lakukan untuk kami"
                b "Saya dan [sname]"
                c "Hmm Ok"
                b "Oke, apakah ya atau tidak?"
                c "Saya harus pergi sekarang"
                pass
        scene bfmch15 with dissolve
        b "{i} Saya harap ini berhasil {/i}"
        scene black
        "..."
        scene bfmch14 with fade
        c "Ya, jangan khawatir"
        scene bfmch16 with fade
        "..."
        scene black
        "..."
        scene chst with fade
        d "Cheryl, sudah kubilang aku dalam rapat"
        d "Kami akan berbicara nanti"
        scene chst1 with dissolve
        "Apakah semuanya baik -baik saja?"
        d "Ya sayang, jangan khawatir"
        d "Mari ikut saya"
        scene chst2 with fade
        "Saya tidak tahu apakah kita harus melakukan ini"
        d "Itu baik -baik saja"
        scene bfmch17 with fade
        b "{i} i \ 'll pulang {/i}"
        jump broom_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc