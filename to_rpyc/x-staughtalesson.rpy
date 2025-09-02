image stlessonf:
    "stlf00.jpg"
    pause 0.03
    "stlf01.jpg"
    pause 0.03
    "stlf02.jpg"
    pause 0.03
    "stlf03.jpg"
    pause 0.03
    "stlf04.jpg"
    pause 0.03
    "stlf05.jpg"
    pause 0.03
    "stlf06.jpg"
    pause 0.03
    "stlf07.jpg"
    pause 0.03
    "stlf08.jpg"
    pause 0.03
    "stlf09.jpg"
    pause 0.03
    "stlf10.jpg"
    pause 0.03
    "stlf11.jpg"
    pause 0.03
    "stlf12.jpg"
    pause 0.03
    "stlf13.jpg"
    pause 0.03
    "stlf14.jpg"
    pause 0.03
    "stlf15.jpg"
    pause 0.03
    "stlf16.jpg"
    pause 0.03
    "stlf17.jpg"
    pause 0.03
    "stlf18.jpg"
    pause 0.03
    "stlf19.jpg"
    pause 0.03
    "stlf20.jpg"
    pause 0.03
    "stlf21.jpg"
    pause 0.03
    "stlf22.jpg"
    pause 0.03
    "stlf23.jpg"
    pause 0.03
    "stlf24.jpg"
    pause 0.03
    "stlf25.jpg"
    pause 0.03
    "stlf26.jpg"
    pause 0.03
    "stlf27.jpg"
    pause 0.03
    "stlf28.jpg"
    pause 0.03
    "stlf29.jpg"
    pause 0.03
    "stlf30.jpg"
    pause 0.03
    "stlf31.jpg"
    pause 0.03
    "stlf32.jpg"
    pause 0.03
    "stlf33.jpg"
    pause 0.03
    "stlf34.jpg"
    pause 0.03
    "stlf35.jpg"
    pause 0.03
    "stlf36.jpg"
    pause 0.03
    "stlf37.jpg"
    pause 0.03
    "stlf38.jpg"
    pause 0.03
    "stlf39.jpg"
    pause 0.03
    "stlf40.jpg"
    pause 0.03
    "stlf41.jpg"
    pause 0.03
    "stlf42.jpg"
    pause 0.03
    "stlf43.jpg"
    pause 0.03
    "stlf44.jpg"
    pause 0.03
    "stlf45.jpg"
    pause 0.03
    "stlf46.jpg"
    pause 0.03
    "stlf47.jpg"
    pause 0.03
    "stlf48.jpg"
    pause 0.03
    "stlf49.jpg"
    pause 0.03
    repeat

image stlessonfr:
    "stlf00.jpg"
    pause 0.01
    "stlf01.jpg"
    pause 0.01
    "stlf02.jpg"
    pause 0.01
    "stlf03.jpg"
    pause 0.01
    "stlf04.jpg"
    pause 0.01
    "stlf05.jpg"
    pause 0.01
    "stlf06.jpg"
    pause 0.01
    "stlf07.jpg"
    pause 0.01
    "stlf08.jpg"
    pause 0.01
    "stlf09.jpg"
    pause 0.01
    "stlf10.jpg"
    pause 0.01
    "stlf11.jpg"
    pause 0.01
    "stlf12.jpg"
    pause 0.01
    "stlf13.jpg"
    pause 0.01
    "stlf14.jpg"
    pause 0.01
    "stlf15.jpg"
    pause 0.01
    "stlf16.jpg"
    pause 0.01
    "stlf17.jpg"
    pause 0.01
    "stlf18.jpg"
    pause 0.01
    "stlf19.jpg"
    pause 0.01
    "stlf20.jpg"
    pause 0.01
    "stlf21.jpg"
    pause 0.01
    "stlf22.jpg"
    pause 0.01
    "stlf23.jpg"
    pause 0.01
    "stlf24.jpg"
    pause 0.01
    "stlf25.jpg"
    pause 0.01
    "stlf26.jpg"
    pause 0.01
    "stlf27.jpg"
    pause 0.01
    "stlf28.jpg"
    pause 0.01
    "stlf29.jpg"
    pause 0.01
    "stlf30.jpg"
    pause 0.01
    "stlf31.jpg"
    pause 0.01
    "stlf32.jpg"
    pause 0.01
    "stlf33.jpg"
    pause 0.01
    "stlf34.jpg"
    pause 0.01
    "stlf35.jpg"
    pause 0.01
    "stlf36.jpg"
    pause 0.01
    "stlf37.jpg"
    pause 0.01
    "stlf38.jpg"
    pause 0.01
    "stlf39.jpg"
    pause 0.01
    "stlf40.jpg"
    pause 0.01
    "stlf41.jpg"
    pause 0.01
    "stlf42.jpg"
    pause 0.01
    "stlf43.jpg"
    pause 0.01
    "stlf44.jpg"
    pause 0.01
    "stlf45.jpg"
    pause 0.01
    "stlf46.jpg"
    pause 0.01
    "stlf47.jpg"
    pause 0.01
    "stlf48.jpg"
    pause 0.01
    "stlf49.jpg"
    pause 0.01
    repeat

label staughtalesson:
    scene sroom_inst_photos_suggestive51 with fade
    b "Itulah yang akan saya lakukan tentang itu"
    scene stlessonp with dissolve
    "..."
    scene stlessonf
    s "..."
    b "Ya!"
    s "Ahhh"
    scene stlessonfr
    "..."
    s "Hmmm"
    s "Hmmmm"
    b "Ahhh"
    if elaineshowsup ==1 and day ==6:
        e "[bname] Di mana ..."
        scene stlesson_e with dissolve
        e "Hah!!"
        e "Astaga!!!"
        scene stlesson_e1 with dissolve
        e "Apakah kamu malu pada dirimu sendiri?!"
        e "Saya akan memberi tahu [mname] tentang ini"
        if sdom >=40:
            e "Kecuali Anda melakukan seperti yang saya katakan"
            b "Kami tidak peduli!"
            scene stlesson_e2 with dissolve
            s "Huh dia pergi, dia akan memberitahunya"
            b "Saya pikir dia akan melakukannya"
            s "Lalu lakukan sesuatu"
            b "Hei tolong kembali"
            b "Apa yang Anda inginkan dari kami"
            scene stlesson_e3 with dissolve
            e "Saya tidak menginginkan apa pun dari Anda"
            scene stlesson_e4 with dissolve
            e "Sebenarnya saya hanya ingin mengajari Anda cara melakukannya"
            "..."
            e "Datang ke sini [bname]"
            scene stlesson_e5 with dissolve
            e "Begitulah cara Anda selalu memulai"
            s "Huh"
            e "Jangan malu"
            e "Watch"
            scene stlesson_e6 with dissolve
            s "..."
            scene stlesson_e5 with dissolve
            e "Datanglah di sebelah saya"
            s "SAYA..."
            e "Atau saya akan memberi tahu [mname]"
            s "..."
            scene stlesson_e7 with dissolve
            b "Ohh bercinta bagus!"
            e "Cukup untuk saat ini, kami tidak ingin dia rusak"
            e "Dapatkan di lantai [mname]"
            scene stlesson_e8 with fade
            b "Ahhh"
            e "Apa! Apakah Anda selesai?"
            e "Mulutnya penuh dengan cum hehe"
            e "Bangun [sname]"
            e "Kiss me"
            scene stlesson_e9 with dissolve
            b "Ouch"
            b "Anda melangkahi saya"
            scene stlesson_e10 with dissolve
            e "Jangan khawatir teman -teman, ini akan menjadi rahasia kecil kita"
            $ sbesecret = 1
            scene broom_day with fade
            b "Sial, itu panas"
            call screen gnav
        else:

            e "Kecuali Anda melakukan seperti yang saya katakan"
            b "Kami tidak peduli!"
            scene stlesson_e2 with dissolve
            s "Huh dia pergi, dia akan memberitahunya"
            b "Nahh saya tidak peduli"
            e "Apa kamu yakin"
            b "Jangan khawatir tentang itu"
            s "Ok saya harap begitu, saya lebih baik pergi sekarang"
            scene broom_day with fade
            "Anda membutuhkan poin dominasi yang lebih tinggi"
            "Maaf tapi Anda melewatkan adegan ini"
            call screen gnav
    else:
        pass
    s "Hmmmmmm !!"
    menu:
        "Menyelesaikan":
            pass
        "Pelajaran dengan cara yang sulit" if sdom >=50:
            scene stlessonp4 with vpunch
            s "Arghh"
            scene stlessonp5 with dissolve
            s "..."
            b "{i} (dimana cum?) {/i}"
            menu:
                "Di mulutnya":
                    scene stlessonpm with dissolve
                    b "Ahhh"
                    pass
                "Di payudaranya":
                    scene stlessonpb with dissolve
                    b "Ahhh"
                    scene stlessonpb1 with fade
                    b "Aku akan mencuci"
                    scene broom_day with fade
                    "..."
                    call screen gnav

            scene stlessonp6 with fade
            b "Aku akan mencuci"
            s "Hmph"
            s "Tanpa menciumku?"
            b "{i}(Oh fuck){/i}"
            menu:
                "Berpura -pura Anda tidak mendengarnya":
                    scene broom_day with fade
                    $ srel -= 5
                    show screen sreldw
                    b "{i} (...) {/i}"
                    hide screen sreldw
                    call screen gnav
                "Cium dia":


                    scene stlessonp7 with dissolve
                    show screen srelup
                    "..."
                    $ srel += 5
                    b "{i} (bercinta hidupku) {/i}"
                    hide screen srelup
                    scene broom_day with fade
                    b "{i} (dia membuatku makan sendiri) {/i}"
                    call screen gnav


    scene stlessonp1 with hpunch
    b "Ahhh"
    s "Hmm"
    scene stlessonp2 with fade
    s "Saya belajar pelajarannya"
    s "..."
    scene stlessonp3 with dissolve
    s "Jaga sayang"
    s "Aku akan sampai jumpa nanti"
    s "Aku perlu mencuci cum di punggungku"
    scene broom_day with fade
    "..."
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc