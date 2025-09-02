label sclothes:
    b "{i} (mungkin saya dapat memeriksa sesuatu untuk pemotretan [sname] \) {/i}"
    scene btique with fade
    "Bagaimana saya bisa membantu Anda?"
    b "Hmm"
    b "Dapatkah saya melihat bikini apa atau semacamnya?"
    "Berapa ukurannya?"
    b "Kurasa kecil"
    "Ha ha"
    "Ok saya akan mendapatkan sesuatu"
    call screen sbikchoice



label highcut:
    scene hch with fade
    b "Saya suka yang ini"
    "$ 100 tolong"
    if bikini2 == 2:
        b "Oh tunggu sebentar, saya sudah membeli yang ini"
        b "Saya memiliki masalah kenangan dengan fashion, semuanya terlihat sama bagi saya hehe"
    else:
        pass
    if mny>=100:
        b "Ini dia"
        $ bikini2 = 1
        $ mny -= 100
        scene btique with dissolve
        "Sampai jumpa"
        jump broom_menu
    else:


        b "Sial, ini mahal"
        b "Maaf saya tidak punya jumlah ini sekarang"
        b "Saya akan kembali lagi nanti"
        scene btique with dissolve
        "Tidak masalah"
        "Sampai jumpa"
        jump broom_menu


label stringsling:
    scene ssling with fade
    b "Saya suka yang ini"
    "Tolong $ 150"
    if bikini3 == 2:
        b "Oh tunggu sebentar, saya sudah membeli yang ini"
        b "Saya memiliki masalah kenangan dengan fashion, semuanya terlihat sama bagi saya hehe"
    else:
        pass
    if mny>=150:
        b "Ini dia"
        $ bikini3 = 1
        $ mny -= 150
        scene btique with dissolve
        "Sampai jumpa"
        jump broom_menu
    else:


        b "Sial, ini mahal"
        b "Maaf saya tidak punya jumlah ini sekarang"
        b "Saya akan kembali lagi nanti"
        scene btique with dissolve
        "Tidak masalah"
        "Sampai jumpa"
        jump broom_menu

label microsk:
    scene mskirt with fade
    b "Saya suka yang ini"
    "$ 50 tolong"
    if microskirt1 == 2:
        b "Oh tunggu sebentar, saya sudah membeli yang ini"
        b "Saya memiliki masalah kenangan dengan fashion, semuanya terlihat sama bagi saya hehe"
    else:
        pass
    if mny>=50:
        b "Ini dia"
        $ microskirt1 = 1
        $ mny -= 50
        scene btique with dissolve
        "Sampai jumpa"
        jump broom_menu
    else:


        b "Sial, ini mahal"
        b "Maaf saya tidak punya jumlah ini sekarang"
        b "Saya akan kembali lagi nanti"
        scene btique with dissolve
        "Tidak masalah"
        "Sampai jumpa"
        jump broom_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc