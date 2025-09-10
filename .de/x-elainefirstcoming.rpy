label elainefirstcoming:
    $ elaineshowsup = 1
    play sound "sounds/doorbell.wav"
    m "Hmm siapa itu saat ini?"
    stop sound
    scene etv_e with fade
    m "Oh hai elaine"
    e "Hi [mname]"
    e "Saya telah datang mengunjungi Anda"
    e "Apakah Anda keberatan jika saya menghabiskan waktu?"
    m "Oh tidak tentu saja tidak"
    scene etv_e1 with dissolve
    e "Saya harap saya tidak mengganggu Anda"
    e "Mungkin Anda akan tidur"
    m "Tidak, tidak sama sekali, kami biasanya menonton TV saat ini"
    e "Bagus"
    m "Saya akan segera kembali"
    scene etv_e2 with fade
    e "Bagaimana kabarmu [bname]?"
    b "Saya baik -baik saja, dan Anda?"
    scene etv_e3 with dissolve
    m "Apa yang ingin Anda minum Elaine?"
    e "Sama seperti Anda"
    scene etv_e4 with fade
    e "Jadi? Bagaimana perasaan Anda di tempat kerja?"
    m "It's OK"
    e "Apa maksudmu oke?"
    e "Apakah Anda terbiasa?"
    m "Not so"
    e "Tapi saya melihat sebaliknya"
    scene etv_e5 with dissolve
    m "Apa maksudmu?"
    e "Saya dapat melihat Anda berjalan -jalan dengan piyama dan dalih Anda"
    e "Berlatih lebih sedikit pakaian?"
    b "{i}(Haha){/i}"
    scene etv_e6 with dissolve
    "..."
    scene etv_e5 with dissolve
    m "Saya selalu memakai ini?"
    e "Lalu itu bagus"
    e "Anda telah menyingkirkan kompleks Anda"
    m "..."
    scene etv_e7 with dissolve
    e "Bisakah saya mendapatkan segelas anggur lagi?"
    e "Atau mungkin sesuatu yang lebih kuat"
    m "Elaine, apa yang salah?"
    e "Later"
    scene etv_e8 with dissolve
    m "Anda akan minum apa yang saya minum"
    m "Selain itu, saya tidak punya apa -apa selain anggur"
    scene etv_e4 with fade
    e "Cheers"
    m "Cheers"
    e "Bisakah saya berbicara dengan Anda"
    e "Privately"
    scene etv_e5 with dissolve
    m "Apa itu?"
    scene etv_e6 with dissolve
    m "[bname] Silakan tinggalkan kami sendirian untuk beberapa waktu"
    scene etv_e7 with dissolve
    m "Apa yang salah?"
    scene etv_e47 with dissolve
    e "Rob menendang saya"
    m "Apa maksudmu?"
    e "Dia menyeret saya keluar dari klub dan berkata saya tidak bisa pulang malam ini"
    e "Dia mengajukan cuti yang belum dibayar untuk hari itu"
    m "Wow!"
    m "Kenapa, apa yang terjadi?"
    e "Dia bilang aku mengizinkan pelanggan untuk meraba -raba pantatku"
    m "Apa!!"
    e "Ya dan sekarang saya tidak tahu apa yang harus dilakukan ..."
    e "Saya berpikir jika Anda membiarkan saya tidur di sini malam ini, dan kami akan mencari sesuatu"
    e "Tomorrow"
    b "{i} (keren) {/i}"
    m "Yeah sure"
    m "Anda bisa, di kamar saya"
    e "Terima kasih [mname]"
    m "Jangan khawatir tentang hal itu, dan besok saya akan berbicara dengan Rob"
    e "Besar"
    m "Biarkan saya menyiapkan tempat untuk Anda tidur"
    scene etv_e48 with dissolve
    b "{i} (sial, aku akan berpura -pura aku berjalan) {/i}"
    scene etv_e49 with dissolve
    b "Oh hai ... saya hanya berjalan"
    m "Duduklah dengan Elaine, aku akan kembali"
    m "Dia akan tinggal di sini malam ini"
    b "Oh Ok"
    scene etv_e2 with fade
    e "Jadi apa yang ada di [bname]?"
    b "Semua baik"
    e "Bagaimana [mname] saat ini?"
    e "Buka sedikit?"
    b "Hmm begitu ..."
    scene etv_e3 with fade
    m "Sudah siap Elaine, mari kita lanjutkan minuman di kamar saya"
    e "Oke, selamat malam [bname]"
    b "{i}(Hmm){/i}"
    if windowfound ==1:
        b "{i} (i \ 'll pergi periksa jendela) {/i}"
        scene ebizstairs0 with fade
        "..."
        scene etv_e50 with fade
        b "Mmm"
        scene etv_e51 with fade
        m "Pakai ini untuk tidur"
        e "Ini terlihat bagus"
        e "Saya punya ide"
        m "Apa itu?"
        e "Dapatkan kami minuman terlebih dahulu"
        scene etv_e52 with dissolve
        b "Kemana dia pergi?"
        "..."
        b "{i} (huh dia kembali) {/i}"
        scene etv_e53 with dissolve
        e "Thanks"
        e "Dua tembakan!"
        e "Apa itu?"
        m "Sesuatu yang bagus, coba"
        scene etv_e54 with dissolve
        e "..."
        scene etv_e55 with dissolve
        e "Wow, ini sangat kuat [mname]"
        e "Aku memberitahumu apa ..."
        e "Mengapa Anda tidak mempraktikkan beberapa langkah yang saya lakukan di tempat kerja?"
        m "Apa?"
        if mcorr >=10:
            m "Apakah saya harus melakukan strippng juga?"
            e "Ya, itu bagian yang menyenangkan"
            m "Oke, duduk dan nikmati"
            scene etv_e56 with fade
            e "Bagus!"
            b "{i} (apa yang terjadi, apakah dia stripping untuknya!) {/i}"
            scene etv_e57 with dissolve
            e "Kamu pergi gadis!"
            b "{i} (i \ 'm butir) {/i}"
            scene etv_e58 with dissolve
            e "Wooh!"
            $ persistent.unlock_5 = True
            b "{i} (apa !!!) {/i}"
            b "{i} (apakah dia menyentuhnya ...) {/i}"
            scene etv_e59 with dissolve
            b "{i} (saya tidak bisa melihat dengan jelas) {/i}"
            e "Lebih banyak [mname] Lainnya!"
            m "Tidak ada elaine, itu cukup"
            m "Mari kita tidur"
            scene black
            b "{i} (oh dia mematikan lampu) {/i}"
            b "{i} (sialan, mungkin akan tidur) {/i}"
            b "{i} (Saya pikir saya tidak punya opsi lain selain tidur) {/i}"
            jump newdays
        else:

            m "No"
            e "Mengapa?"
            m "Saya tidak menyukainya"
            m "Tolong mari kita tidur"
            scene black
            b "{i} (oh dia mematikan lampu) {/i}"
            b "{i} (sialan, mungkin akan tidur) {/i}"
            b "{i} (Saya pikir saya tidak punya opsi lain selain tidur) {/i}"
            "Anda tidak memiliki titik korupsi yang cukup [mname]"
            jump newdays
    else:
        b "{i} (Saya pikir saya tidak punya opsi lain selain tidur) {/i}"
        jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
