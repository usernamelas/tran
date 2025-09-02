label s_hot_lunch:
    $ snaked_lunch = 2
    b "Mari kita periksa apa untuk makan siang"
    scene slunch_hot with fade
    b "Apa!!!"
    b "Itu!!!"
    b "Sungguh!"
    scene slunch_hot1 with dissolve
    s "Satu lagi kata pervy dan saya mengubahnya"
    s "Dipahami?"
    b "Tentu saja saya mengerti"
    s "Duduk!"
    scene slunch_hot2 with dissolve
    b "Dari mana Anda mendapatkan benda itu?"
    s "Ini bukan urusan Anda"
    scene slunch_hot3 with dissolve
    s "Ini adalah hadiah Anda karena Anda memberi saya tiket"
    s "Sekarang makan!"
    b "Yes ma'am"
    scene slunch_hot4 with dissolve
    "..."
    scene slunch_hot5 with fade
    b "Makanan enak"
    s "Anda menyukainya?"
    b "Yeah"
    scene slunch_hot6 with dissolve
    s "..."
    scene slunch_hot7 with dissolve
    s "Oh sial!"
    s "Aku akan kembali"
    b "Apa?"
    scene slunch_hot8 with dissolve
    b "Apa yang salah?"
    s "Saya tidak bisa tetap seperti ini"
    s "Bagaimana jika dia kembali"
    b "Hehehe dia di tempat kerja santai!"
    scene slunch_hot9 with dissolve
    b "Kembali ke sana, lanjutkan makan siang Anda"
    s "Tetapi..."
    b "Dia tidak akan datang!"
    s "Anda pikir begitu?"
    b "Ya, ayo selesaikan makan siang Anda"
    b "Aku akan mencuci piring untukmu"
    scene slunch_hot10 with fade
    "..."
    scene slunch_hot11 with dissolve
    "..."
    s "Selesai?"
    b "Yes"
    s "Ayo ambil ciumanmu"
    scene slunch_hot12 with dissolve
    b "Dan pelukan juga"
    scene slunch_hot13 with dissolve
    "..."
    scene slunch_hot14 with fade
    "..."
    scene slunch_hot15 with dissolve
    "..."
    menu:
        "Cobalah keberuntungan Anda":
            scene slunch_hot16 with dissolve
            "..."
            scene slunch_hot17 with dissolve
            "..."
            b "{i}(No reaction){/i}"
            b "{i}(Wow){/i}"
            s "Saya harus pergi [bname]"
            pass
        "Melanjutkan":

            s "Saya harus pergi [bname]"
            pass

    scene slunch_hot18 with dissolve
    s "Sampai jumpa"
    b "Tunggu! Anda tidak memberi tahu saya dari mana Anda mendapatkan gaun ini?"
    s "Rahasia!"
    scene slunch_hot19 with dissolve
    b "Berengsek!"
    b "Ayo! Beri tahu saya"
    s "Saya sudah membelinya untuk Halloween"
    b "Dan..."
    s "Rahasia!"
    scene slunch_hot20 with dissolve
    b "{i} (apa -apaan) {/i}"
    scene door with fade
    b "{i} (...) {/i}"
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc