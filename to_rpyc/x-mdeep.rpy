image mdt:
    "mdt00.jpg"
    pause 0.05
    "mdt01.jpg"
    pause 0.05
    "mdt02.jpg"
    pause 0.05
    "mdt03.jpg"
    pause 0.05
    "mdt04.jpg"
    pause 0.05
    "mdt05.jpg"
    pause 0.05
    "mdt06.jpg"
    pause 0.05
    "mdt07.jpg"
    pause 0.05
    "mdt08.jpg"
    pause 0.05
    "mdt09.jpg"
    pause 0.05
    "mdt10.jpg"
    pause 0.05
    "mdt11.jpg"
    pause 0.05
    "mdt12.jpg"
    pause 0.05
    "mdt13.jpg"
    pause 0.05
    "mdt14.jpg"
    pause 0.05
    "mdt15.jpg"
    pause 0.05
    "mdt16.jpg"
    pause 0.05
    "mdt17.jpg"
    pause 0.05
    "mdt18.jpg"
    pause 0.05
    "mdt19.jpg"
    pause 0.05
    "mdt20.jpg"
    pause 0.05
    "mdt21.jpg"
    pause 0.05
    "mdt22.jpg"
    pause 0.05
    "mdt23.jpg"
    pause 0.05
    "mdt24.jpg"
    pause 0.05
    "mdt25.jpg"
    pause 0.05
    "mdt26.jpg"
    pause 0.05
    "mdt27.jpg"
    pause 0.05
    "mdt28.jpg"
    pause 0.05
    "mdt29.jpg"
    pause 0.05
    "mdt30.jpg"
    pause 0.05
    "mdt31.jpg"
    pause 0.05
    "mdt32.jpg"
    pause 0.05
    "mdt33.jpg"
    pause 0.05
    "mdt34.jpg"
    pause 0.05
    "mdt35.jpg"
    pause 0.05
    "mdt36.jpg"
    pause 0.05
    "mdt37.jpg"
    pause 0.05
    "mdt38.jpg"
    pause 0.05
    "mdt39.jpg"
    pause 0.05
    "mdt40.jpg"
    pause 0.05
    "mdt41.jpg"
    pause 0.05
    "mdt42.jpg"
    pause 0.05
    "mdt43.jpg"
    pause 0.05
    "mdt44.jpg"
    pause 0.05
    "mdt45.jpg"
    pause 0.05
    "mdt46.jpg"
    pause 0.05
    "mdt47.jpg"
    pause 0.05
    "mdt48.jpg"
    pause 0.05
    "mdt49.jpg"
    pause 0.05
    repeat

label mdeep:
    scene mdt
    b "Ya!"
    "..."
    $ persistent.unlock_20 = True
    b "Lagi!"
    "..."
    scene girlnight52 with dissolve
    e "{i} (apa yang sedang terjadi) {/i}"
    e "{i} ([mname] hancur tenggorokannya) {/i}"
    e "{i} (What a Mess in [name]) {/i}"
    scene girlnight53 with dissolve
    m "Apakah itu Stewart terbaik Anda"
    b "..."
    scene girlnight54 with dissolve
    e "{i}(Oh wow){/i}"
    scene girlnight55 with dissolve
    e "{i} (oh my fucking god!) {/i}"
    e "{i} (i \ 'D lebih baik pergi jangan ingin mengintimidasi dia) {/i}"
    scene girlnight56 with dissolve
    b "..."
    scene girlnight57 with dissolve
    b "Ahhh!"
    menu:
        "Fokus Don \ 't cum" if mfuckedsober >= 1:
            b "Kemarilah"
            scene prefdc with fade
            m "[bname] Apa!"
            scene fdc
            m "Mmm"
            m "Ah"
            m "Ahh"
            m "Oh"
            "..."
            m "Ahhh"
            scene girlnight77 with dissolve
            e "{i} (oh Tuhan saya harus menjadi bagian dari ini) {/i}"
            scene girlnight78 with dissolve
            e "Bagaimana dengan saya?"
            scene girlnight79 with fade
            "..."
            scene girlnight80 with dissolve
            m "Ahh"
            scene girlnight81 with dissolve
            b "Ah shit"
            b "Saya tidak bisa lagi"
            e "Wait"
            scene girlnight82 with fade
            m "Ahh"
            scene girlnight83 with dissolve
            b "Ahh"
            scene girlnight59 with fade
            b "{i} (kurasa aku akan tidur sekarang) {/i}"
            jump newdays
        "Melanjutkan":
            pass

    e "{i} (i \ 'D lebih baik tinggalkan mereka sendiri) {/i}"
    scene girlnight58 with dissolve
    m "Selamat malam sayang"
    b "Selamat malam"
    b "{i} (kemana semua orang pergi?) {/i}"
    scene girlnight59 with hpunch
    b "Apakah Anda akan baik -baik saja?"
    m "Ya, saya hanya mengantuk"
    b "{i} (kurasa aku akan tidur sekarang) {/i}"
    jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc