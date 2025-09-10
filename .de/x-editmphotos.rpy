label editmphotos:
    scene bporn with dissolve
    b "{i} (Mari kita lihat apa yang kita punya) {/i}"
    scene mphotoshoot13 with fade
    b "{i} (cantik) {/i}"
    scene mphotoshoot20 with fade
    b "{i}(Fuck){/i}"
    m "Apa yang sedang kamu lakukan?"
    scene mnphotos with hpunch
    b "Huh"
    b "Saya sedang memeriksa foto Anda"
    m "Memeriksa?!"
    b "Maksud saya pengeditan"
    scene mnphotos1 with dissolve
    m "Lalu mengapa Anda menutup laptop?"
    m "Tunjukkan bagaimana Anda mengeditnya"
    scene mnphotos2 with dissolve
    m "Aha"
    scene mphotoshoot20 with dissolve
    m "Jadi inilah yang Anda edit"
    b "Ya itu indah dan tidak menunjukkan wajah Anda"
    m "Ya pantatku cantik"
    b "{i} (dia harus mabuk) {/i}"
    scene mnphotos with dissolve
    m "Ok saya akan meninggalkan Anda untuk terus mengedit"
    m "Dan kunci pintu Anda saat Anda melakukannya"
    m "Saya tidak ingin skandal"
    scene emphotos with dissolve
    b "{i} (dia pasti mabuk) {/i}"
    scene bporn with dissolve
    b "{i} (let \ 's lanjutkan) {/i}"
    scene black
    "SEMENTARA ITU"
    scene mnphotos3 with fade
    m "{i} (Apa yang Anda lakukan pada hidup Anda [mname]!) {/i}"
    m "{i} (apakah ini benar -benar terjadi!) {/i}"
    scene emphotos1 with dissolve
    if mrel >=450:
        m "{i} (i \ 'll lihat apa yang dia lakukan) {/i}"
        scene emphotos5 with fade
        m "[bname]"
        m "Apakah kamu di!"
        b "Yes"
        m "Open"
        b "{i} (setidaknya celana pendek cepat) {/i}"
        scene emphotos6 with fade
        m "Apa yang sedang kamu lakukan?"
        b "Masih mengedit beberapa foto"
        scene emphotos4 with dissolve
        m "Sekali lagi menyembunyikannya"
        m "Show me"
        m "Saya berjanji saya tidak akan marah"
        scene emphotos7 with dissolve
        m "Jadi begitu!"
        m "Sekarang Anda melakukan ini?"
        scene emphotos8 with dissolve
        b "Hehe"
        b "Apakah Anda ingin mengambil lebih banyak foto?"
        b "Tapi kali ini dengan riasan kuku"
        scene emphotos9 with dissolve
        m "..."
        m "Maksudmu cat kuku?"
        m "Anda tidak tahu apa -apa tentang hal -hal wanita sayang"
        m "Manikur membutuhkan waktu"
        b "Tapi itu indah, saya tidak melihat Anda memilikinya"
        $ mnailpolish = 1
        m "Saya akan segera melakukannya"
        m "Mari kita ambil beberapa foto untuk saat ini"
        b "Ok"
        m "Dalam jubah ini?"
        b "Apakah Anda memiliki sesuatu yang lain?"
        m "Ya saya punya sesuatu yang menyenangkan"
        m "Anda akan menyukai foto -fotonya"
        scene emphotos10 with fade
        m "Jadi?"
        m "Di mana Anda ingin melakukannya?"
        b "Di dinding"
        scene emphotos11 with fade
        b "Wow bagus"
        scene emphotos12 with dissolve
        b "Satu lagi?"
        scene emphotos13 with dissolve
        m "Cukup untuk saat ini"
        m "Mungkin versi berikutnya"
        b "Ok"
        scene broom_night with fade
        "..."
        call screen gnav
    else:
        m "{i} (Saya perlu memeriksa apa yang dia lakukan) {/i}"
        scene emphotos2 with fade
        m "{i}(Oh God){/i}"
        scene emphotos3 with dissolve
        m "{i}(Oh God){/i}"
        $ mcorr += 1
        m "{i} (Saya tidak ingin melihat ini {/i}"
        show screen mcorr
        "..."
        hide screen mcorr
        scene mnphotos3 with fade
        m "{i} (...) {/i}"
        scene broom_night with fade
        "..."
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
