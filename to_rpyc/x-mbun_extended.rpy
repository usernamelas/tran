label mbun_extended:
    b "{i} (hmm apa yang harus diberikan padanya?) {/i}"
    menu:
        "Lebih banyak anggur":
            b "Hmm, pilihan yang bagus"
            pass
        "Minuman keras":

            b "Hmm, pilihan yang bagus"
            scene etv_aw32_br with fade
            m "Terima kasih, ini sangat manis"
            b "Ya itu"
            scene etv_aw23_bra with dissolve
            b "{i} (mari lakukan ini lagi) {/i}"
            m "[bname]"
            scene etv_aw30_bra with dissolve
            b "{i} (sial!) {/i}"
            b "Yes"
            m "Bawa aku ke kamarku"
            scene etv_aw31_br with fade
            m "Terima kasih [bname]"
            b "Selamat malam"
            m "Sleep here"
            b "Ah ok"
            scene etv_aw33_br with dissolve
            "..."
            scene etv_aw34_br with dissolve
            b "{i} (Saya ingin mengisap ini) {/i}"
            b "{i} (tapi lebih baik membiarkannya mempercayai saya untuk saat ini) {/i}"
            menu:
                "Lakukan itu":
                    scene etv_aw35_br with dissolve
                    "..."
                    scene etv_aw36_br with dissolve
                    "..."
                    scene etv_aw35_br with dissolve
                    "..."
                    if mrel >= 450 and msex >=1:
                        scene etv_aw37_br with dissolve
                        "..."
                        m "Stewart datang ke sini"
                        scene etv_aw38_br with dissolve
                        "..."
                        scene jbpractice79 with dissolve
                        m "Berikan padaku!"
                        b "Apa?"
                        m "Letakkan di dalam!"
                        menu:
                            "Lakukan itu":
                                scene etv_aw39_br with dissolve
                                "..."
                                scene etv_aw40_br with hpunch
                                m "Ahhh!"
                                scene etv_aw41_br with dissolve
                                m "Ahh"
                                scene etv_aw41_br_bw with dissolve
                                "..."
                                scene etv_aw42_br with fade
                                m "[bname] Apa yang kamu lakukan di sini?"
                                b "Anda menyuruh saya tidur di sini"
                                m "Tolong pergi ke kamar Anda"
                                scene etv_aw43_br with dissolve
                                b "{i} (apakah itu terjadi? Atau apakah saya bermimpi?!) {/i}"
                                jump newdays
                            "Jangan":

                                b "Saya tidak bisa sekarang"
                                m "Oh! Seperti biasa Steve"
                                b "Huh"
                                scene black
                                "..."
                                scene etv_aw42_br with fade
                                m "[bname] Apa yang kamu lakukan di sini?"
                                b "Anda menyuruh saya tidur di sini"
                                m "Tolong pergi ke kamar Anda"
                                jump newdays
                    else:

                        m "Cukup Stewart, Let \'s Sleep"
                        scene black
                        "..."
                        scene etv_aw42_br with fade
                        m "[bname] Apa yang kamu lakukan di sini?"
                        b "Anda menyuruh saya tidur di sini"
                        m "Tolong pergi ke kamar Anda"
                        jump newdays

    scene etv_aw18_r with fade
    m "Terima kasih"
    m "Continue please"
    scene etv_aw28_br with fade
    "..."
    scene etv_aw24_br with dissolve
    b "Ahh!"
    scene etv_aw29_br with dissolve
    b "Saatnya melakukannya"
    m "[bname]"
    scene etv_aw30_br with dissolve
    b "{i} (sial!) {/i}"
    b "Yes"
    m "Bawa aku ke kamarku"
    scene etv_aw31_br with fade
    b "Selamat malam"
    m "Selamat malam [bname]"
    scene black
    "..."
    jump bs_afterjmassage
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc