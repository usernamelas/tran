label jenpracticextend:
    scene jbpractice13n with fade
    m "Wi yang bagus ..."
    "Hickup"
    m "Wine"
    b "{i} (keren dia mabuk) {/i}"
    menu:
        "Mengapa Anda tidak memberi saya pertunjukan dansa baru":
            if persistent.unlock_19 == True and mrel>= 400:
                scene jbpractice66 with dissolve
                m "All right"
                m "Aku akan kembali"
                scene jbpractice2 with dissolve
                "..."
                scene jbpractice83 with fade
                b "Dingin"
                scene jbpractice84 with dissolve
                b "Saya suka tarian ini"
                scene jbpractice85 with dissolve
                "..."
                scene jbpractice86 with dissolve
                m "Lepaskan tabel"
                scene jbdnc0 with fade
                b "Wow"
                m "..."
                scene jbdnc01 with dissolve
                m "Yes"
                scene jbdnc12 with dissolve
                b "{i} (itu itu, saya bisa \ 't lagi) {/i}"
                b "{i} (Saya ingin pantat itu sekarang!) {/i}"
                scene jbpractice87 with dissolve
                m "Tidak ada Stewart"
                b "{i} (sialan dia terlalu ketat) {/i}"
                scene jbpractice88 with fade
                b "Ahhh"
                scene jbpractice89 with dissolve
                m "Sit"
                scene jbpractice90 with dissolve
                "..."
                scene jbpractice91 with dissolve
                b "Fuck"
                b "Saya akan pergi ke cum"
                scene jbpractice92 with fade
                "..."
                scene jbpractice93 with dissolve
                m "Ya bermain dengannya"
                m "Ahhh"
                m "Cium aku di sana"
                scene jbpractice94 with fade
                "..."
                scene jbpractice95 with dissolve
                m "Yeah"
                scene jbpractice96 with dissolve
                m "Mhhhm"
                scene jbpractice97 with fade
                m "Selamat malam Stewart"
                b "Ahh selamat malam"
                jump newdays
            else:

                scene jbpractice66 with dissolve
                m "Saya akan memberi Anda pertunjukan lain"
                scene mdnc
                "..."
                m "Wooh!"
                b "Bagus"
                m "Yeah"
                b "Woah berhati -hatilah Anda akan jatuh"
                scene jbpractice67 with hpunch
                "..."
                scene jbpractice67a with dissolve
                m "..."
                scene jbpractice68 with dissolve
                m "Apa?"
                menu:
                    "Saya pikir Anda harus melepasnya":
                        if mrel >=450:
                            m "Yang mana?"
                            b "Panty Anda"
                            m "Apa untuk Stewart"
                            b "Saya akan menghapusnya"
                            scene jbpractice98 with dissolve
                            m "Ahhh"
                            scene jbpractice99 with dissolve
                            "..."
                            m "Mari kita duduk di suatu tempat"
                            scene jbpractice100 with dissolve
                            m "Ahh"
                            scene jbpractice101 with dissolve
                            m "Tolong bawa saya ke kamar saya"
                            scene jbpractice70 with fade
                            b "Saya harap Anda akan baik -baik saja"
                            b "Selamat malam"
                            "..."
                            m "Tidur di sini [bname]"
                            b "Huh"
                            m "Yes"
                            scene jbpractice71 with dissolve
                            "..."
                            scene jbpractice72 with dissolve
                            b "{i} (Saya ingin mengisap ini) {/i}"
                            b "{i} (tapi lebih baik membiarkannya mempercayai saya untuk saat ini) {/i}"
                            menu:
                                "Lakukan itu":
                                    scene jbpractice75 with dissolve
                                    "..."
                                    scene jbpractice76 with dissolve
                                    "..."
                                    scene jbpractice75 with dissolve
                                    "..."
                                    scene jbpractice77 with dissolve
                                    "..."
                                    m "Kemarilah"
                                    scene jbpractice78 with dissolve
                                    "..."
                                    scene jbpractice79 with dissolve
                                    m "Berikan padaku!"
                                    b "Apa?"
                                    m "Letakkan di dalam!"
                                    menu:
                                        "Lakukan itu":
                                            scene jbpractice80 with dissolve
                                            "..."
                                            scene jbpractice81 with hpunch
                                            m "Ahhh!"
                                            scene jbpractice81a with dissolve
                                            "..."
                                            scene jbpractice82 with dissolve
                                            m "Ini Stewart yang menyakitkan, tolong hentikan"
                                            b "{i} (lagi Stewart shit) {/i}"
                                            m "Stewart Berhenti!"
                                            b "Ok"
                                            scene jbpractice72 with fade
                                            b "{i} (mungkin saya seharusnya tidak tinggal) {/i}"
                                            b "{i} (Saya seharusnya tidak berada di sini saat dia bangun) {/i}"
                                            menu:
                                                "Meninggalkan":
                                                    "..."
                                                    jump newdays
                                                "Tinggal":

                                                    scene black
                                                    "..."
                                                    scene jbpractice73a with fade
                                                    m "Hah!"
                                                    m "[bname] Apa yang kamu lakukan di sini?"
                                                    b "Anda menyuruh saya tidur"
                                                    m "Keluar dari rumah saya"
                                                    b "Sial, apakah kamu serius?"
                                                    m "Ya, pergi sekarang"
                                                    scene black
                                                    "Permainan selesai"
                                                    return
                                        "Jangan":



                                            b "Saya tidak bisa sekarang"
                                            m "Oh! Seperti biasa Steve"
                                            b "Huh"
                                            pass
                        else:


                            "Angkat hubungan Anda menjadi 450 untuk melihat lebih banyak"
                            m "Hmm"
                            m "Tolong bawa saya ke kamar saya"
                            scene jbpractice70 with fade
                            b "Saya harap Anda akan baik -baik saja"
                            b "Selamat malam"
                            "..."
                            m "Tidur di sini [bname]"
                            b "Huh"
                            m "Yes"
                            scene jbpractice71 with dissolve
                            "..."
                            scene jbpractice72 with dissolve
                            b "{i} (Saya ingin mengisap ini) {/i}"
                            b "{i} (tapi lebih baik membiarkannya mempercayai saya untuk saat ini) {/i}"
                            menu:
                                "Lakukan itu":
                                    scene jbpractice75 with dissolve
                                    "..."
                                    scene jbpractice76 with dissolve
                                    "..."
                                    scene jbpractice75 with dissolve
                                    "..."
                                    scene jbpractice77 with dissolve
                                    "..."
                                    m "Kemarilah"
                                    scene jbpractice78 with dissolve
                                    "..."
                                    scene jbpractice79 with dissolve
                                    m "Berikan padaku!"
                                    b "Apa?"
                                    m "Letakkan di dalam!"
                                    menu:
                                        "Lakukan itu":
                                            scene jbpractice80 with dissolve
                                            "..."
                                            scene jbpractice81 with hpunch
                                            m "Ahhh!"
                                            scene jbpractice82 with dissolve
                                            m "Ini Stewart yang menyakitkan, tolong hentikan"
                                            $ persistent.unlock_6 = True
                                            b "{i} (lagi Stewart shit) {/i}"
                                            m "Stewart Berhenti!"
                                            b "Ok"
                                            scene jbpractice72 with fade
                                            b "{i} (mungkin saya seharusnya tidak tinggal) {/i}"
                                            b "{i} (Saya seharusnya tidak berada di sini saat dia bangun) {/i}"
                                            menu:
                                                "Meninggalkan":
                                                    "..."
                                                    jump newdays
                                                "Tinggal":

                                                    scene black
                                                    "..."
                                                    scene jbpractice73a with fade
                                                    m "Hah!"
                                                    m "[bname] Apa yang kamu lakukan di sini?"
                                                    b "Anda menyuruh saya tidur"
                                                    m "Keluar dari rumah saya"
                                                    b "Sial, apakah kamu serius?"
                                                    m "Ya, pergi sekarang"
                                                    scene black
                                                    "Permainan selesai"
                                                    return
                                        "Jangan":



                                            b "Saya tidak bisa sekarang"
                                            m "Oh! Seperti biasa Steve"
                                            b "Huh"
                                            pass
        "Melanjutkan":



            scene jbpractice66 with dissolve
            m "Saya akan memberi Anda pertunjukan lain"
            scene mdnc
            "..."
            m "Wooh!"
            b "Bagus"
            m "Yeah"
            b "Woah berhati -hatilah Anda akan jatuh"
            m "Saya kira sudah waktunya tidur"
            scene jbpractice30 with fade
            m "Terima kasih sayang"
            b "Jangan lupakan gaun tidurmu"
            scene jbpractice45 with dissolve
            m "Terima kasih telah mengingatkan saya"
            jump mnightshow
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
