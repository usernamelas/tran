label elaineconjen:
    scene hall_m_n21 with dissolve
    e "Saya tidak mengatakan Anda menyukai saya"
    e "Mungkin Anda bisa bekerja sebagai pelayan"
    e "Seperti masa lalu yang indah"
    m "Pelayan?"
    m "Apakah gajinya bagus?"
    e "Gaji tidak, tetapi biaya layanan dan tips adalah 3 kali lipat dari apa yang Anda dapatkan sekarang"
    scene hall_m_n39 with dissolve
    m "Benar-benar?"
    e "Ya, terkadang lebih"
    scene hall_m_n21 with dissolve
    m "Dan apakah itu aman?"
    m "Saya tidak ingin dipukul oleh orang -orang yang buruk dan mabuk"
    e "Hahaha, itu sebabnya kami mengalami penjaga"
    e "Dan itu benar -benar terserah Anda jika Anda ingin menghibur pelanggan di luar giliran Anda"
    m "Saya tidak ingin melakukan itu"
    e "Aku tahu"
    e "Tetapi jika Anda ingin mendapatkan lebih banyak tips"
    e "Anda harus melakukan beberapa gerakan twerking saat menyajikan minuman"
    e "Saya ulangi, saya tidak ingin melakukan itu!"
    e "Ya ya, saya mengerti"
    m "Saya lebih suka mati daripada melakukan ini"
    m "Saya hanya tidak mengerti bagaimana Anda bisa melakukannya"
    e "Saya pikir saya akan menyelamatkan diri dari kuliah dan pergi"
    $ elaine_convince = 2
    scene hall_m_n20 with dissolve
    b "{i} (waktu untuk pergi) {/i}"
    "..."
    call screen gnav

label elaineconjen1:
    scene hall_m_n21 with dissolve
    e "Jadi?"
    m "Saya sedang berpikir"
    m "Jika saya ingin melakukan pekerjaan ini"
    m "Apa yang dikenakan pelayan?"
    e "Dengan baik..."
    m "Apakah itu selalu harus minim seperti apa yang Anda pakai terakhir kali?"
    m "Atau Anda punya beberapa pilihan?"
    e "[mname] Sudah kubilang, itu benar -benar normal, hanya kepribadian yang keren"
    e "Beberapa gerakan menggoda"
    e "Dan Anda akan menguasainya"
    e "Di akhir bulan Anda akan melakukan 4 hingga 5 angka"
    m "Saya mengajukan pertanyaan, apakah itu harus minim atau tidak"
    scene hall_m_n39 with dissolve
    e "Seharusnya topless seperti yang Anda lihat saya"
    e "Tapi saya akan mencoba meyakinkan mereka untuk pengecualian untuk Anda, jika Anda tertarik"
    "..."
    e "Itu aman, percayalah"
    e "Tidak ada yang bisa memaksa Anda untuk melakukan apa pun yang tidak ingin Anda lakukan"
    e "Sajikan minuman dan itu"
    scene hall_m_n21 with dissolve
    m "Mari kita lihat"
    $ elaine_convince = 3
    scene hall_m_n20 with dissolve
    b "{i} (waktu untuk pergi) {/i}"
    "..."
    call screen gnav


label elaineconjen2:
    scene hall_m_n21 with dissolve
    e "Saya berhasil membuat Anda pengecualian, Anda tidak harus memakai yang topless"
    m "Bagus ... bagaimana tampilan seragamnya?"
    e "Di sini aku punyamu"
    e "Pakai"
    scene hall_m_n40 with fade
    m "Ini terlalu banyak"
    e "Oh ayolah! Ini hanya rok dan atasan yang normal"
    m "Saya tidak tahu Elaine"
    e "Mari kita tanya [bname]"
    m "Apa?"
    scene hall_m_n41 with dissolve
    m "Apakah kamu serius"
    e "Baik kita membutuhkan pendapat yang tidak memihak"
    m "SAYA..."
    scene hall_m_n42 with dissolve
    m "Dia begitu ..."
    m "Dia tidak tahu apa -apa tentang mode atau seksualitas"
    m "Dia orang yang paling naif yang pernah ada"
    e "Itulah mengapa, kita perlu mendapatkan pendapat orang normal"
    e "Dan menjadi begitu naif, kami akan menyaksikan reaksinya"
    m "Anda pikir begitu?"
    e "Yes"
    e "Panggil dia"
    m "All right"
    scene hall_m_n43 with dissolve
    e "{i} (naif pantatku) {/i}"
    scene mpractice with fade
    e "Jadi [bname] Apa pendapat Anda tentang pakaian ini"
    scene mpractice1 with dissolve
    e "Apakah ini terlalu pendek?"
    scene mpractice2 with dissolve
    b "Berbuat salah..."
    b "Tidak, itu normal"
    scene mpractice3 with dissolve
    m "Ok [bname] Terima kasih"
    m "Tolong tinggalkan kami sendiri"
    b "Keren ok"
    scene mpractice4 with dissolve
    b "{i}(Interesting){/i}"
    "..."
    $ elaine_convince = 4
    b "{i} (waktu untuk pergi) {/i}"
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc