label elainelunch:
    scene elun with fade
    e "Yes exactly"
    m "Anda lihat?"
    scene elun1 with fade
    e "Terima kasih untuk makan siang [mname]"
    m "Mari kita minum segelas anggur"
    e "Ya tapi saya tidak bisa tetap terlambat"
    scene elun2 with dissolve
    m "Pur dua gelas anggur"
    b "Dua?"
    b "Bisakah saya mendapatkannya untuk saya?"
    m "No"
    scene elun3 with fade
    e "... dan bagaimana dengan Michael?"
    scene elun4 with dissolve
    m "[bname], belum ada yang harus Anda lakukan?"
    b "Seperti apa, tidak"
    m "Studi? Pembersihan!?"
    e "Tinggalkan kami sebentar [bname] Saya akan membantu Anda dengan studi Anda"
    scene elun5 with dissolve
    "..."
    b "Ok"
    scene broom_day with fade
    b "{i} (apa yang harus dilakukan sekarang) {/i}"
    scene broom_camera1 with fade
    b "{i}(Boring){/i}"
    scene elun6 with dissolve
    e "Selesai belajar?"
    b "Saya bahkan tidak ingin belajar"
    e "Apakah Anda ingin bersenang -senang?"
    b "Of course"
    e "Tapi Anda harus membayar"
    b "Hehe ok, berapa harganya?"
    e "Hanya $ 300, spesial untuk Anda"
    if mny >=300:
        b "Ok ini dia"
        $ mny -= 300
        pass
    else:
        b "Sial, aku tidak punya"
        e "Sayang sekali"
        e "Bye"
        scene hall_d with fade
        "..."
        call screen gnav

    e "Lalu ikut dengan saya, bantu saya dengan [mname]"
    b "Apa yang salah?"
    e "Tidak ada yang salah, hanya mabuk"
    b "Ahh"
    scene elmd
    b "Dingin"
    e "Pergi menangkapnya"
    e "Mari bersenang -senang"
    e "Lakukan seperti yang saya katakan"
    "..."
    scene elun7 with hpunch
    m "[bname] !!"
    b "Yes"
    m "Dapatkan aku minuman"
    b "Saya pikir Anda sudah cukup"
    scene elun8 with dissolve
    e "Dapatkan kami minuman [bname]"
    e "Jangan menjadi brengsek"
    scene elun9 with fade
    m "Saya muak diberitahu apa yang harus dilakukan"
    m "Saya ingin memutuskan sekali"
    e "Mari berlatih dengan [bname]"
    m "Apakah Anda yakin itu ide yang bagus"
    e "Itu tidak akan membahayakan siapa pun"
    m "Tapi aku akan membayarnya"
    e "Berhenti memiliki kompleks yang dibayar untuk seks [mname]"
    e "It's normal"
    b "{i} (apa yang mereka bicarakan) {/i}"
    scene elun10 with dissolve
    e "[bname] Datang ke sini pada empat"
    b "Apakah kamu serius!?"
    e "Lakukan seperti yang saya katakan"
    b "Ah Ok"
    scene elun11 with dissolve
    b "Aduh kamu berat"
    e "Ok"
    e "Apa yang Anda ingin dia lakukan [mname]"
    m "Berapa banyak kita membayarnya"
    e "Cukup bagi Anda untuk melakukan apapun yang Anda inginkan"
    $ persistent.unlock_70 = True
    m "Hmm"
    menu:
        "Cat":
            m "Saya ingin dia menjilat vagina saya"
            scene elblp
            m "Mmm"
            "..."
            m "..."
            e "Enough guys"
            e "Dapatkan pantat Anda di sini"
            pass
        "Pantat":

            m "Saya ingin dia menjilat pantat saya"
            scene elba with fade
            m "Uh"
            scene elbla
            m "Mmm"
            "..."
            m "..."
            e "Enough guys"
            e "Dapatkan pantat Anda di sini"
            pass
        "Fuck":

            pass

    scene elun12 with fade
    m "..."
    scene elun13 with dissolve
    m "Ahh"
    scene elun14 with dissolve
    m "Elaine"
    scene elun15 with dissolve
    e "Yes"
    m "More"
    scene elun16 with dissolve
    e "Yes"
    scene elun17 with dissolve
    "..."
    scene elun18 with fade
    e "Mari kita selesaikan dia"
    scene elunf with dissolve
    b "Yessss"
    scene elunf1 with dissolve
    "..."
    scene elunf2 with dissolve
    m "Ah"
    scene elunf3 with dissolve
    e "Mmm"
    scene elun18a with dissolve
    m "Ahhh"
    scene elun19 with dissolve
    "..."
    scene elun20 with dissolve
    b "Ah"
    scene elun21 with dissolve
    b "Fuck"
    scene elun22 with fade
    "..."
    scene elun23 with fade
    m "Apa yang terjadi Elaine"
    e "Tidak ada, kami hanya minum dan tertidur"
    m "Ok saya akan terus tidur"
    e "Biarkan saya membawa Anda ke kamar Anda"
    scene black
    "..."
    scene elun24 with fade
    e "Saya akan pergi sekarang [bname]"
    b "Dan di mana uang saya"
    e "..."
    e "Saya akan memberi Anda seks secara gratis sebagai gantinya"
    b "Ya, lain kali"
    jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
