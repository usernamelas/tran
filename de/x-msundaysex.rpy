label msundaysex:
    scene black
    $ Hour += 3
    "Setelah 1 jam"
    scene sdayclea81 with dissolve
    m "Dimana [sname]"
    b "Dia memutuskan untuk mengunjungi Rowena, dia akan terlambat"
    m "Ok"
    m "Apa yang ingin kamu makan?"
    b "Apapun, saya tidak keberatan"
    scene sdayclea82 with fade
    m "Bon appetit"
    b "Kamu juga"
    scene sdayclea83 with fade
    b "Tidak ada apa -apa di TV saat ini"
    b "Mari Mainkan Film"
    m "Saya tahu apa yang Anda inginkan, dan jawabannya tidak, bukan film itu"
    b "Ok saya akan mendapatkan minuman"
    m "Whatever"
    scene sdayclea84 with fade
    b "Apakah Anda ingin pijatan?"
    m "Apakah Anda menawarkan saya pijatan"
    m "Atau Anda menginginkan yang lain?"
    b "Both"
    m "[bname] Apa yang saya lakukan pada Anda?"
    b "Anda adalah segalanya saya"
    scene sdayclea85 with dissolve
    m "..."
    scene sdayclea86 with dissolve
    m "Terima kasih sayang"
    scene sdayclea87 with dissolve
    m "Hai! [sname] akan kembali sebentar lagi"
    b "Tidak, jangan khawatir, dia akan tetap terlambat"
    m "Bagaimana Anda tahu?"
    b "Percayalah, dan saya tetap terkunci pintu"
    if sgoestost >= 2:
        scene black
        "SEMENTARA ITU"
        scene sdayclea88 with fade
        if persistent.patch_enabled:
            s "Ayah!!!"
            pass
        else:
            s "Hai!"
        d "Hi sweetheart"
        scene sdayclea89 with dissolve
        s "Aku merindukanmu"
        d "..."
        scene sdayclea90 with dissolve
        d "Apa"
        scene sdayclea91 with dissolve
        d "Apakah kamu melakukannya?"
        scene sdayclea92 with dissolve
        s "Inilah yang saya lakukan"
        if sundaysex ==0:
            d "Apa!"
            $ sundaysex += 1
            d "Bangun"
            s "Mengapa?"
            d "Kami tidak melakukan ini lagi!"
            s "Tapi aku suka apa yang kamu ajarkan padaku"
            s "Apakah saya siswa yang buruk?"
            s "Lalu ajari aku"
            scene sdayclea92a with dissolve
            d "Aku akan mengajarimu pelajaran sekarang"
            $ persistent.unlock_55 = True
            scene dsm with fade
            s "Ah"
            s "Ah"
            if persistent.patch_enabled:
                s "Ayah itu menyakitkan"
                pass
            else:
                s "It's painful"
                pass
            d "Hentikan game ini"
            scene sdayclea92b with fade
            "..."
            scene sdayclea92c with dissolve
            d "Stop"
            scene black
            "Kembali ke [mname]"
            pass
        else:

            s "Dan Anda tidak mengatakan tidak kali ini"
            s "Anda tidak punya waktu"
            $ persistent.unlock_56 = True
            scene sdbj
            d "Ah"
            "..."
            d "..."
            "..."
            s "..."
            "..."
            scene sdbjend with dissolve
            "..."
            scene sdbjend1 with dissolve
            "..."
            scene sdbjend2 with dissolve
            "..."
            scene sdbjend3 with hpunch
            d "AHhh"
            scene sdbjend4 with dissolve
            s "..."
            scene black
            "Kembali ke [mname]"
            pass
    else:

        "Ada beberapa adegan untuk [sname] dengan Stewart pastikan Anda membukanya"
        pass
    scene pwmp

    "..."
    m "Ahh"
    "..."
    m "Cium aku [bname]"
    "..."
    scene tfm000 with dissolve
    m "Mhhm"
    scene tfm034 with dissolve
    "..."
    scene tfm045 with dissolve
    "..."
    scene tfm056 with dissolve
    "..."
    scene tfm060 with dissolve
    "..."
    if sundaysex >=1 and sgoestost >= 2:
        scene black
        "SEMENTARA ITU"
        scene sdayclea93 with fade
        "..."
        scene black
        "Kembali ke [mname]"
        scene sdayclea94 with fade
        b "Anda akan tidur di sini?"
        m "Tidak, biarkan aku tidur sebentar"
        b "Ok saya akan membawa Anda ke kamar Anda"
        scene sdayclea95 with fade
        m "Di mana?"
        b "Here"
        scene sdnv
        $ persistent.unlock_62 = True
        "..."
        m "Mmm"
        "..."
        scene sdayclea96 with dissolve
        "..."
        scene sdayclea97 with dissolve
        m "Ahh"
        scene sdayclea98 with dissolve
        m "[bname] enough"
        scene sdayclea99 with fade
        b "Selamat malam!"
        scene sdayclea100 with fade
        m "{i} (saya menjadi sangat buruk) {/i}"
        m "{i} (mungkin saya harus mulai membuka seperti elaine) {/i}"
        $ jenopen = 1
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav
    else:
        m "turn"
        scene mlbb

        b "Fuck"
        "..."
        b "Ahh"
        scene sdayclea94 with fade
        b "Anda akan tidur di sini?"
        m "Tidak, biarkan aku tidur sebentar"
        b "Ok saya akan membawa Anda ke kamar Anda"
        scene sdayclea95 with fade
        m "Di mana?"
        b "Here"
        scene sdnv
        "..."
        m "Mmm"
        "..."
        scene sdayclea96 with dissolve
        "..."
        scene sdayclea97 with dissolve
        m "Ahh"
        scene sdayclea98 with dissolve
        m "[bname] enough"
        scene sdayclea99 with fade
        b "Selamat malam!"
        scene sdayclea100 with fade
        m "{i} (saya menjadi sangat buruk) {/i}"
        m "{i} (mungkin saya harus mulai membuka seperti elaine) {/i}"
        $ jenopen = 1
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
