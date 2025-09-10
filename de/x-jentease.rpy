image jenta:
    "jenta00.jpg"
    pause 0.03
    "jenta01.jpg"
    pause 0.03
    "jenta02.jpg"
    pause 0.03
    "jenta03.jpg"
    pause 0.03
    "jenta04.jpg"
    pause 0.03
    "jenta05.jpg"
    pause 0.03
    "jenta06.jpg"
    pause 0.03
    "jenta07.jpg"
    pause 0.03
    "jenta08.jpg"
    pause 0.03
    "jenta09.jpg"
    pause 0.03
    "jenta10.jpg"
    pause 0.03
    "jenta11.jpg"
    pause 0.03
    "jenta12.jpg"
    pause 0.03
    "jenta13.jpg"
    pause 0.03
    "jenta14.jpg"
    pause 0.03
    "jenta15.jpg"
    pause 0.03
    "jenta16.jpg"
    pause 0.03
    "jenta17.jpg"
    pause 0.03
    "jenta18.jpg"
    pause 0.03
    "jenta19.jpg"
    pause 0.03
    "jenta20.jpg"
    pause 0.03
    "jenta21.jpg"
    pause 0.03
    "jenta22.jpg"
    pause 0.03
    "jenta23.jpg"
    pause 0.03
    "jenta24.jpg"
    pause 0.03
    "jenta25.jpg"
    pause 0.03
    "jenta26.jpg"
    pause 0.03
    "jenta27.jpg"
    pause 0.03
    "jenta28.jpg"
    pause 0.03
    "jenta29.jpg"
    pause 0.03
    "jenta30.jpg"
    pause 0.03
    "jenta31.jpg"
    pause 0.03
    "jenta32.jpg"
    pause 0.03
    "jenta33.jpg"
    pause 0.03
    "jenta34.jpg"
    pause 0.03
    "jenta35.jpg"
    pause 0.03
    "jenta36.jpg"
    pause 0.03
    "jenta37.jpg"
    pause 0.03
    "jenta38.jpg"
    pause 0.03
    "jenta39.jpg"
    pause 0.03
    "jenta40.jpg"
    pause 0.03
    "jenta41.jpg"
    pause 0.03
    "jenta42.jpg"
    pause 0.03
    "jenta43.jpg"
    pause 0.03
    "jenta44.jpg"
    pause 0.03
    "jenta45.jpg"
    pause 0.03
    "jenta46.jpg"
    pause 0.03
    "jenta47.jpg"
    pause 0.03
    "jenta48.jpg"
    pause 0.03
    "jenta49.jpg"
    pause 0.03
    "jenta50.jpg"
    pause 0.03
    "jenta51.jpg"
    pause 0.03
    "jenta52.jpg"
    pause 0.03
    "jenta53.jpg"
    pause 0.03
    "jenta54.jpg"
    pause 0.03
    "jenta55.jpg"
    pause 0.03
    "jenta56.jpg"
    pause 0.03
    "jenta57.jpg"
    pause 0.03
    "jenta58.jpg"
    pause 0.03
    "jenta59.jpg"
    pause 0.03
    "jenta60.jpg"
    pause 0.03
    repeat

label jentease:
    scene jent with fade
    m "Hi [bname]"
    b "Dimana semua orang"
    m "Mereka pergi, ingin bergabung dengan saya?"
    b "Sure"
    m "Ambil gelas"
    if gnight >=6:
        m "Izinkan saya menunjukkan sesuatu"
        scene jent1 with fade
        m "Aku akan kembali"
        scene jent7 with fade
        b "Astaga!"
        scene jent8 with dissolve
        m "Apakah kamu menyukainya?"
        b "Tentu saja!"
        scene jent9 with dissolve
        m "Lalu aku akan memberimu pertunjukan"
        m "Matikan TV"
        b "Apakah Anda memiliki sesuatu yang lain?"
        m "Maybe"
        b "Bisakah saya melihat?"
        if mfuckedsober >= 1:
            m "Hmm"
            m "Wait here"
            scene jent10 with fade
            b "Saya pernah melihat ini sebelumnya!"
            pass
        else:
            m "Not today"
            pass
        $ jenteaselingerie = 1
        m "Matikan TV"
        pass
    else:

        m "Aku akan memakai sesuatu untukmu"
        scene jent1 with fade
        "..."
        scene jent2 with fade
        m "Apakah kamu menyukainya?"
        b "Amazing"
        m "Maka Anda akan lebih menyukai ini"
        m "Matikan TV"
        pass
    scene jenta
    m "Merayu!"
    "..."
    b "Wow"
    "..."
    scene jent3 with hpunch
    m "Thanks [bname]"
    scene jent4 with dissolve
    "..."
    scene jent5 with dissolve
    m "Mhhm"
    scene jent4 with dissolve
    if mfuckedsober >= 1:
        m "Hmm"
        m "Bagaimana kabarmu ..."
        b "Saya apa?"
        m "Kondisi Anda"
        b "Tidak apa -apa sekarang"
        b "Tapi terkadang"
        m "Undress"
        m "Saya ingin memeriksa"
        scene jhj00 with dissolve
        b "Huh"
        scene jhj
        $ persistent.unlock_45 = True
        b "Damn"
        b "..."
        "..."
        scene jent11 with dissolve
        b "Ahhh"
        m "Senang mengetahui bahwa Anda baik -baik saja"
        m "Selamat malam [bname]"
        b "Selamat malam"
        b "{i} (Saya kira itu untuk opsi ini) {/i}"
        b "{i} (i \ 'll pergi tidur) {/i}"
        jump newdays
    else:
        pass
    m "Bawa aku ke kamarku"
    scene jent6 with fade
    m "Selamat malam [bname]"
    b "Selamat malam"
    b "{i} (Saya kira itu untuk opsi ini) {/i}"
    b "{i} (i \ 'll pergi tidur) {/i}"
    jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
