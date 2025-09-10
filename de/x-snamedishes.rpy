label snamedishes:
    s "Yes"
    scene dinner5 with dissolve
    s "Anda bisa mencuci piring untuk saya"
    b "Hmmm"
    menu:
        "Menerima":
            b "Ok"
            b "Dan apa yang saya dapatkan sebagai balasannya?"
            if sbm ==2:
                if persistent.patch_enabled:
                    s "Anda akan berterima kasih kepada saya karena tidak menunjukkan videonya kepada ibu"
                    b "Aha! OKE"
                    s "..."
                    b "Bagaimana dengan ciuman?"
                    s "Anda tidak mendengar saya?"
                    b "Aku mendengarmu, tapi setidaknya ciuman"
                    b "Itu tidak akan membahayakan"
                    pass
                else:
                    s "Anda akan berterima kasih kepada saya karena tidak menampilkan video ke [mname]"
                    b "Aha! OKE"
                    s "..."
                    b "Bagaimana dengan ciuman?"
                    s "Anda tidak mendengar saya?"
                    b "Aku mendengarmu, tapi setidaknya ciuman"
                    b "Itu tidak akan membahayakan"
                    pass
            else:

                s "A kiss"
                b "Ok keren"
                pass


            s "Tapi yang cepat"
            s "Dan tidak ada sentuhan"
            b "Sure"
            scene dinner10 with fade
            "..."
            b "Done"
            s "Ayo dapatkan ciumanmu"
            if snameworkmelinda ==1:
                b "Pertama saya punya sesuatu untuk ditanyakan kepada Anda"
                scene dinner10as with dissolve
                s "Apa itu?"
                b "Apakah Anda ingin memiliki pekerjaan paruh waktu?"
                s "No"
                b "Anda tidak ingin tahu berapa banyak uang yang bisa Anda dapatkan?"
                s "Apakah terlalu banyak?"
                b "Sekitar 00 hingga 000 per kunjungan"
                scene dinner10as1 with dissolve
                s "Hmm"
                scene dinner10as with dissolve
                s "Biarkan saya menebak, pengawalan?"
                b "Ya, tapi mereka berkualitas tinggi, pribadi"
                b "Semacam klub pribadi"
                s "Saya akan memikirkannya"
                $ snameworkmelinda = 3
                b "Ok tidak lupa untuk memberi tahu saya keputusan Anda"
                s "Tentu, sekarang dapatkan ciuman Anda dengan cepat"
                pass

            elif snameworkmelinda == 4:
                b "Apakah Anda memutuskan tentang penawaran Melinda"
                scene dinner10as with dissolve
                s "No"
                b "Mengapa?"
                s "Saya perlu memikirkannya"
                b "Tidak ada yang perlu dipikirkan"
                s "Bagaimana Anda bisa menemukan alibi untuk saya meninggalkan rumah selama seminggu atau lebih?"
                b "Hmm true"
                scene dinner10as1 with dissolve
                b "Kita perlu memikirkan itu"
                pass
            else:

                pass
            scene dinner11 with fade
            "..."
            scene dinner6 with fade
            s "Terima kasih"
            show screen srelup
            $ srel += 2
            s "Lihat ya!"
            hide screen srelup
            if workrequest ==3 and msuspbs ==0:
                $ msuspbs = 1
                scene dinner12 with dissolve
                "..."
                m "Ahem"
                m "Apa yang terjadi?"
                scene dinner13 with dissolve
                s "Nothing"
                b "Saya membantu [sname] dengan hidangan"
                m "Oke, pergi ke kamar Anda"
                scene dinner14 with dissolve
                m "..."
                scene hall_n with fade
                "..."
                call screen gnav
            if workrequest ==3 and msuspbs ==1:
                scene dinner12 with dissolve
                "..."
                m "Ahem"
                m "Apa yang terjadi?"
                $ persistent.unlock_66 = True
                scene dinner13 with dissolve
                s "Nothing"
                b "Saya membantu [sname] dengan hidangan"
                m "Oke, bagaimanapun saya baru saja datang untuk memberi tahu Anda bahwa saya akan pergi untuk melihat Elaine malam ini"
                m "Anda berdua berperilaku saat saya tidak di sini"
                scene dinner14 with dissolve
                m "..."
                scene hall_n with fade
                "..."
                scene msusp with fade
                m "Selamat malam, saya mungkin kembali terlambat"
                m "Sleep early"
                s "Oke!"
                scene sroom_av8 with fade
                b "Membaca saat ini?"
                scene sroom_av9 with dissolve
                s "Apa yang kamu inginkan sekarang?"
                b "Tidakkah Anda ingin menonton TV?"
                s "Tidak, tolong izinkan saya melanjutkan buku saya"
                b "Bagaimana dengan saya mengambil beberapa foto untuk portofolio Anda?"
                if srel >=250:
                    s "Setelah saya menyelesaikan bacaan saya"
                    b "Ok"
                    scene sroom_av11 with dissolve
                    s "Apa?"
                    b "Nothing"
                    scene sroom_av13 with dissolve
                    "..."
                    scene sroom_av13a with dissolve
                    s "Astaga"
                    scene sroom_av21 with dissolve
                    s "[bname] Dia mungkin datang sebentar lagi"
                    b "Tidak, dia baru saja pergi dan berkata dia akan terlambat"
                    scene msusp1 with hpunch
                    s "Ayo [bname]"
                    s "Yang Anda pikirkan adalah seks"
                    b "Saya tidak ingin seks, saya hanya ingin memberi Anda kesenangan"
                    scene btossa with fade
                    s "Apa?"
                    scene btoss
                    s "Ahh"
                    s "[bname]"
                    "..."
                    s "Apa yang sedang kamu lakukan"
                    s "Ahh"
                    scene msusp2 with fade
                    m "{i} (hmm dimana mereka?) {/i}"
                    if mfuckedsober >= 1:
                        scene msusp3 with dissolve
                        m "..."
                        scene msusp4 with dissolve
                        "..."
                        scene msusp5 with dissolve
                        m "..."
                        scene msusp7 with fade
                        m "{i} (apa yang telah saya lakukan untuk hidup saya!) {/i}"
                        scene msusp8 with fade
                        b "Kamu kembali?"
                        m "Yes"
                        s "{i} (sialan! Saya memberi tahu orang idiot ini berisiko) {/i}"
                        s "{i} (Saya harap dia tidak mendengar kami) {/i}"
                        b "Bisakah kami bergabung dengan Anda untuk minum"
                        m "Lakukan apapun yang Anda inginkan"
                        s "Aku akan tidur"
                        m "Duduk [sname], Minum bersama kami"
                        b "Ayo biarkan segelas anggur"
                        scene msusp9 with dissolve
                        s "Saya memberi tahu Anda bahwa ada sesuatu yang mencurigakan"
                        b "Tenang, mari kita duduk dan kita akan tahu apakah dia melihat atau memperhatikan kita"
                        scene msusp10 with fade
                        m "Jadi [sname] bagaimana studi Anda"
                        s "Itu bagus"
                        m "Hmm"
                        m "Apakah [bname] membantu Anda?"
                        s "Yes"
                        m "Jadi begitu"
                        m "Beri tahu saya..."
                        m "Hmm"
                        m "Ngomong -ngomong, aku punya sesuatu dan aku ingin kamu mencobanya"
                        m "Ingin melihat apakah itu bagus, saya akan membelinya untuk Anda"
                        s "Huh, ada apa?"
                        m "Itu di tempat tidurku, mengenakannya dan datang"
                        scene msusp11 with dissolve
                        m "Katakan padaku [bname]"
                        m "Apakah dia punya pacar?"
                        b "Err aku tidak tahu aku tidak menanyakan hal -hal seperti itu"
                        scene msusp12 with fade
                        m "Bagus"
                        s "Apa itu?"
                        m "Saya akan mendapatkan diri saya sama, tetapi warna yang berbeda"
                        m "Anda bisa pergi dan berubah sekarang"
                        scene msusp13 with dissolve
                        s "..."
                        m "Selamat malam [bname]"
                        scene msusp14 with fade
                        m "{i} (apa yang salah [mname]) {/i}"
                        scene msusp15 with dissolve
                        "..."
                        scene msusp16 with dissolve
                        m "Ahh"
                        scene msusp17 with dissolve
                        "..."
                        scene msusp18 with dissolve
                        "..."
                        scene msusp19 with dissolve
                        m "Ahh"
                        "..."
                        m "Lebih baik saya tidur siang"
                        if sm_rel == 1:
                            m "Atau tidak!"
                            m "Hmm"
                            scene msusp20 with fade
                            "..."
                            scene msusp21 with dissolve
                            "..."
                            scene msusp22 with dissolve
                            s "Apa?"
                            scene msusp23 with dissolve
                            $ persistent.unlock_77 = True
                            s "Huh"
                            scene msusp24 with dissolve
                            s "Hah!"
                            m "Cium aku [sname]"
                            scene msusp25 with dissolve
                            s "{i} (oh wow napasnya, dia mabuk) {/i}"
                            scene msusp26 with dissolve
                            s "{i} (dia melahap saya, jadi lapar) {/i}"
                            scene msusp27 with dissolve
                            s "Ah"
                            scene msusp28 with dissolve
                            s "{i} (yah kenapa tidak! Sumber uang lain) {/i}"
                            scene msusp29 with dissolve
                            s "Ahhh"
                            scene msusp30 with dissolve
                            s "Ahhh"
                            scene msusp31 with vpunch
                            s "Uh"
                            scene msusp32 with dissolve
                            "..."
                            scene msusp33 with dissolve
                            s "Ah saya merasa ingin ... kencing"
                            scene msusp34 with dissolve
                            m "Lalu lakukanlah!"
                            if persistent.patch_enabled:
                                s "Mom no"
                                pass
                            else:
                                s "No"
                                pass
                            m "Tolong lakukan itu"
                            scene msusp35 with vpunch
                            s "Ahh"
                            scene msusp36 with fade
                            m "Apa yang salah?"
                            s "SAYA.."
                            scene msusp37 with dissolve
                            s "Saya butuh uang"
                            m "Untuk apa?"
                            s "Saya ingin membeli sepatu baru, milik saya rusak"
                            m "Berapa banyak yang Anda inginkan?"
                            scene msusp38 with fade
                            s "Terima kasih"
                            m "Lihat [sname] Tidak ada yang harus tahu tentang ini"
                            s "Tentu saja, saya tahu"
                            m "Selamat malam"
                            scene msusp14 with fade
                            "..."
                            scene hall_n with fade
                            "..."
                            call screen gnav
                        else:
                            pass
                        scene hall_n with fade
                        "..."
                        call screen gnav


                    elif gnight >=5:
                        scene msusp3 with dissolve
                        m "..."
                        scene msusp4 with dissolve
                        "..."
                        scene msusp5 with dissolve
                        m "..."
                        scene msusp7 with fade
                        m "{i} (apa yang telah saya lakukan untuk hidup saya!) {/i}"
                        scene msusp8 with fade
                        b "Kamu kembali?"
                        m "Yes"
                        s "{i} (sialan! Saya memberi tahu orang idiot ini berisiko) {/i}"
                        s "{i} (Saya harap dia tidak mendengar kami) {/i}"
                        b "Bisakah kami bergabung dengan Anda untuk minum"
                        m "Lakukan apapun yang Anda inginkan"
                        s "Aku akan tidur"
                        m "Duduk [sname], Minum bersama kami"
                        b "Ayo biarkan segelas anggur"
                        scene msusp9 with dissolve
                        s "Saya memberi tahu Anda bahwa ada sesuatu yang mencurigakan"
                        b "Tenang, mari kita duduk dan kita akan tahu apakah dia melihat atau memperhatikan kita"
                        scene msusp10 with fade
                        m "Jadi [sname] bagaimana studi Anda"
                        s "Itu bagus"
                        m "Hmm"
                        m "Apakah [bname] membantu Anda?"
                        s "Yes"
                        m "Jadi begitu"
                        m "Beri tahu saya..."
                        m "Hmm"
                        m "Ngomong -ngomong, aku punya sesuatu dan aku ingin kamu mencobanya"
                        m "Ingin melihat apakah itu bagus, saya akan membelinya untuk Anda"
                        s "Huh, ada apa?"
                        m "Itu di tempat tidurku, mengenakannya dan datang"
                        scene msusp11 with dissolve
                        m "Katakan padaku [bname]"
                        m "Apakah dia punya pacar?"
                        b "Err aku tidak tahu aku tidak menanyakan hal -hal seperti itu"
                        scene msusp12 with fade
                        m "Bagus"
                        s "Apa itu?"
                        m "Saya akan mendapatkan diri saya sama, tetapi warna yang berbeda"
                        m "Anda bisa pergi dan berubah sekarang"
                        scene msusp13 with dissolve
                        s "..."
                        m "Selamat malam [bname]"
                        scene msusp14 with fade
                        m "{i} (apa yang salah [mname]) {/i}"
                        scene msusp15 with dissolve
                        "..."
                        scene msusp16 with dissolve
                        m "Ahh"
                        scene msusp17 with dissolve
                        "..."
                        scene msusp18 with dissolve
                        "..."
                        scene msusp19 with dissolve
                        m "Ahh"
                        "..."
                        m "Lebih baik saya tidur siang"
                        if sm_rel == 1:
                            m "Atau tidak!"
                            m "Hmm"
                            scene msusp20 with fade
                            "..."
                            scene msusp21 with dissolve
                            "..."
                            scene msusp22 with dissolve
                            s "Apa?"
                            scene msusp23 with dissolve
                            $ persistent.unlock_77 = True
                            s "Huh"
                            scene msusp24 with dissolve
                            s "Hah!"
                            m "Cium aku [sname]"
                            scene msusp25 with dissolve
                            s "{i} (oh wow napasnya, dia mabuk) {/i}"
                            scene msusp26 with dissolve
                            s "{i} (dia melahap saya, jadi lapar) {/i}"
                            scene msusp27 with dissolve
                            s "Ah"
                            scene msusp28 with dissolve
                            s "{i} (yah kenapa tidak! Sumber uang lain) {/i}"
                            scene msusp29 with dissolve
                            s "Ahhh"
                            scene msusp30 with dissolve
                            s "Ahhh"
                            scene msusp31 with vpunch
                            s "Uh"
                            scene msusp32 with dissolve
                            "..."
                            scene msusp33 with dissolve
                            s "Ah saya merasa ingin ... kencing"
                            scene msusp34 with dissolve
                            m "Lalu lakukanlah!"
                            if persistent.patch_enabled:
                                s "Mom no"
                                pass
                            else:
                                s "No"
                                pass
                            m "Tolong lakukan itu"
                            scene msusp35 with vpunch
                            s "Ahh"
                            scene msusp36 with fade
                            m "Apa yang salah?"
                            s "SAYA.."
                            scene msusp37 with dissolve
                            s "Saya butuh uang"
                            m "Untuk apa?"
                            s "Saya ingin membeli sepatu baru, milik saya rusak"
                            m "Berapa banyak yang Anda inginkan?"
                            scene msusp38 with fade
                            s "Terima kasih"
                            m "Lihat [sname] Tidak ada yang harus tahu tentang ini"
                            s "Tentu saja, saya tahu"
                            m "Selamat malam"
                            scene msusp14 with fade
                            "..."
                            scene hall_n with fade
                            "..."
                            call screen gnav
                        else:
                            pass
                        scene hall_n with fade
                        "..."
                        call screen gnav

                    elif mrel >=400:
                        scene msusp3 with dissolve
                        m "..."
                        scene msusp4 with dissolve
                        "..."
                        scene msusp5 with dissolve
                        m "..."
                        scene msusp7 with fade
                        m "{i} (apa yang telah saya lakukan untuk hidup saya!) {/i}"
                        scene msusp8 with fade
                        b "Kamu kembali?"
                        m "Yes"
                        s "{i} (sialan! Saya memberi tahu orang idiot ini berisiko) {/i}"
                        s "{i} (Saya harap dia tidak mendengar kami) {/i}"
                        b "Bisakah kami bergabung dengan Anda untuk minum"
                        m "Lakukan apapun yang Anda inginkan"
                        s "Aku akan tidur"
                        m "Duduk [sname], Minum bersama kami"
                        b "Ayo biarkan segelas anggur"
                        scene msusp9 with dissolve
                        s "Saya memberi tahu Anda bahwa ada sesuatu yang mencurigakan"
                        b "Tenang, mari kita duduk dan kita akan tahu apakah dia melihat atau memperhatikan kita"
                        scene msusp10 with fade
                        m "Jadi [sname] bagaimana studi Anda"
                        s "Itu bagus"
                        m "Hmm"
                        m "Apakah [bname] membantu Anda?"
                        s "Yes"
                        m "Jadi begitu"
                        m "Beri tahu saya..."
                        m "Hmm"
                        m "Ngomong -ngomong, aku punya sesuatu dan aku ingin kamu mencobanya"
                        m "Ingin melihat apakah itu bagus, saya akan membelinya untuk Anda"
                        s "Huh, ada apa?"
                        m "Itu di tempat tidurku, mengenakannya dan datang"
                        scene msusp11 with dissolve
                        m "Katakan padaku [bname]"
                        m "Apakah dia punya pacar?"
                        b "Err aku tidak tahu aku tidak menanyakan hal -hal seperti itu"
                        scene msusp12 with fade
                        m "Bagus"
                        s "Apa itu?"
                        m "Saya akan mendapatkan diri saya sama, tetapi warna yang berbeda"
                        m "Anda bisa pergi dan berubah sekarang"
                        scene msusp13 with dissolve
                        s "..."
                        m "Selamat malam [bname]"
                        scene msusp14 with fade
                        m "{i} (apa yang salah [mname]) {/i}"
                        scene msusp15 with dissolve
                        "..."
                        scene msusp16 with dissolve
                        m "Ahh"
                        scene msusp17 with dissolve
                        "..."
                        scene msusp18 with dissolve
                        "..."
                        scene msusp19 with dissolve
                        m "Ahh"
                        "..."
                        m "Lebih baik saya tidur siang"
                        if sm_rel == 1:
                            m "Atau tidak!"
                            m "Hmm"
                            scene msusp20 with fade
                            "..."
                            scene msusp21 with dissolve
                            "..."
                            scene msusp22 with dissolve
                            s "Apa?"
                            scene msusp23 with dissolve
                            $ persistent.unlock_77 = True
                            s "Huh"
                            scene msusp24 with dissolve
                            s "Hah!"
                            m "Cium aku [sname]"
                            scene msusp25 with dissolve
                            s "{i} (oh wow napasnya, dia mabuk) {/i}"
                            scene msusp26 with dissolve
                            s "{i} (dia melahap saya, jadi lapar) {/i}"
                            scene msusp27 with dissolve
                            s "Ah"
                            scene msusp28 with dissolve
                            s "{i} (yah kenapa tidak! Sumber uang lain) {/i}"
                            scene msusp29 with dissolve
                            s "Ahhh"
                            scene msusp30 with dissolve
                            s "Ahhh"
                            scene msusp31 with vpunch
                            s "Uh"
                            scene msusp32 with dissolve
                            "..."
                            scene msusp33 with dissolve
                            s "Ah saya merasa ingin ... kencing"
                            scene msusp34 with dissolve
                            m "Lalu lakukanlah!"
                            if persistent.patch_enabled:
                                s "Mom no"
                                pass
                            else:
                                s "No"
                                pass
                            m "Tolong lakukan itu"
                            scene msusp35 with vpunch
                            s "Ahh"
                            scene msusp36 with fade
                            m "Apa yang salah?"
                            s "SAYA.."
                            scene msusp37 with dissolve
                            s "Saya butuh uang"
                            m "Untuk apa?"
                            s "Saya ingin membeli sepatu baru, milik saya rusak"
                            m "Berapa banyak yang Anda inginkan?"
                            scene msusp38 with fade
                            s "Thank you"
                            m "Lihat [sname] Tidak ada yang harus tahu tentang ini"
                            s "Tentu saja, saya tahu"
                            m "Good night"
                            scene msusp14 with fade
                            "..."
                            scene msusp39 with fade
                            s "{i} (apa yang terjadi pada kita!?) {/i}"
                            $ sfedup = 1
                            s "{i} (ini harus berhenti) {/i}"
                            scene hall_n with fade
                            "..."
                            call screen gnav
                        else:
                            pass
                        scene hall_n with fade
                        "..."
                        call screen gnav
                    else:
                        scene msusp3 with dissolve
                        m "..."
                        scene msusp4 with dissolve
                        "..."
                        scene msusp6 with vpunch
                        m "Keluar dari rumah saya"
                        b "Ahh"
                        m "Kalian berdua"
                        "Permainan selesai"
                        return
                else:

                    $ Hour += 2
                    s "Tidak, tolong pergi"
                    "Dapatkan poin [sname] Anda lebih dari 250"
                    call screen gnav
            else:
                pass

            scene dinner7 with fade
            b "Berengsek!"
            "..."
            scene hall_n with fade
            b "{i} (akhirnya selesai) {/i}"
            "..."
            call screen gnav
        "Mustahil":

            scene dinner8 with dissolve
            s "Hah!"
            b "Maaf saya harus pergi"
            scene hall_n with fade
            "..."
            call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
