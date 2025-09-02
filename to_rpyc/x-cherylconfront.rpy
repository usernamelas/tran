label cherylconfront:
    scene chcm with fade
    play sound "sounds/doorbell.wav"
    m "Hah!"
    m "Siapa itu saat ini?"
    b "Maybe Elaine"
    stop sound
    scene chcm1 with dissolve
    $ persistent.unlock_23 = True
    c "[bname] [sname] Silakan pergi ke kamar Anda"
    scene chcm2 with dissolve
    c "Saya dan [mname] perlu berbicara"
    scene chcm3 with fade
    c "Katakan padaku [mname]"
    m "Apa?"
    c "Apakah Anda pikir tidak apa -apa bagi wanita yang sudah menikah untuk bekerja sebagai penari telanjang?"
    scene chcm3a with dissolve
    m "Huh"
    scene chcm3 with dissolve
    c "Jatuhkan kejutan palsu"
    c "Saya tahu tentang klub bawah tanah"
    c "Saya tahu segalanya"
    m "Berbuat salah..."
    scene chcm4 with dissolve
    m "..."
    c "Selamat malam"
    scene chcm5 with dissolve
    m "Tunggu!"
    c "Saya mengucapkan selamat malam"
    m "Tolong jangan beri tahu Stewart, saya akan memperbaikinya"
    c "Saya akan memikirkannya"
    scene chcm6 with dissolve
    "..."
    scene chcm7 with fade
    b "Jadi tentang apa?"
    m "..."
    scene chcm8 with hpunch
    m "Mengapa Anda memberi tahu dia tentang pekerjaan saya?"
    scene chcm9 with dissolve
    b "{i}(Damn){/i}"
    b "Aku tidak memberitahunya tentang apa pun"
    m "Lalu siapa yang memberitahunya tentang di mana saya bekerja?"
    b "Mereka mungkin mengikuti Anda"
    scene chcm10 with dissolve
    m "Saya tidak peduli Anda di kamar Anda sampai besok"
    b "{i}(Fuck){/i}"
    scene black
    "..."
    scene chcm11 with fade
    m "Mhhm"
    scene chcm12 with dissolve
    s "Err maaf saya hanya merasa panas"
    m "Santai [sname] Aku tidak marah"
    s "{i} (dia terlihat mabuk!?) {/i}"
    m "Bisakah saya tidur di sini malam ini?"
    scene bporn_s22 with dissolve
    s "Huh"
    scene chcm13 with dissolve
    s "Yes sure"
    scene chcm14 with fade
    "..."
    scene chcm15 with dissolve
    s "..."
    scene chcm16 with dissolve
    "..."
    scene chcm17 with dissolve
    s "..."
    menu:
        "Dia akan mencoba melakukan sesuatu":
            scene chcm18 with dissolve
            s "Hmm"
            scene chcm19 with dissolve
            "..."
            scene chcm20 with dissolve
            m "Ahhh"
            scene chcm20s with dissolve

            "..."
            scene chcm21 with dissolve
            m "Hmm"
            scene chcm22 with dissolve
            m "Hmm"
            scene chcm23 with dissolve
            m "Iya ini"
            scene chcm24 with hpunch
            m "Hah!"
            m "[sname] Apakah sudah pagi?"
            s "No"
            m "Mari kita kembali tidur"
            pass
        "TIDAK":



            pass

    scene chcm25 with fade
    s "Selamat pagi"
    s "Bagaimana perasaan Anda sekarang?"
    m "Better"
    m "Biarkan saya pergi dan bersiap -siap"
    s "Ok"
    scene chcm26 with fade
    "..."
    jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc