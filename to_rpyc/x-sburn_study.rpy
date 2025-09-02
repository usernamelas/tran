label sburn_study:
    scene sroom_st_b with fade
    b "Hai [sname], apa yang salah?"
    scene sroom_st1_b with dissolve
    s "Saya mencoba belajar duh!"
    menu:
        "Menawarkan untuk membantu":
            b "Ingin bantuan saya?"
            s "Yes"
            scene sroom_st2 with dissolve
            b "Hmmm"
            $ srel += 1
            scene sroom_st3_b with dissolve
            b "Done"
            show screen srelup
            s "Thank youuuu"
            hide screen srelup
            scene sroom_st4_b with fade
            s "Sekarang izinkan saya menyelesaikan ini"
            b "Sure"
            pass
        "Tinggalkan dia sendiri":

            b "Lihat yah!"
            pass




    if instadone == 2:
        b "Err ... Apakah Anda ingin berlatih pemotretan untuk halaman Anda?"
        s "Hmm, ok, tapi pertama biarkan aku menyelesaikan ini, kembali setelah 5 menit"
        s "Saya akan siap"
        b "Apa yang akan kamu pakai?"
        s "Saya tidak tahu, saya akan menemukan sesuatu"
        scene door with fade
        b "{i} (...) {/i}"
        scene black
        "Setelah lima menit"
        scene sroom_inst_photos_b with fade
        b "Mengapa Anda tidak berubah?"
        s "Saya tidak bisa memakai bikini"
        b "Mengapa?"
        s "Karena terbakar matahari"
        b "Biarkan saya melihat ..."
        scene sroom_inst_photos1_b with fade
        s "Melihat"
        b "Oh yeah"
        b "Aku tidak tahu..."
        b "Apakah Anda ingin saya memakai lotion?"
        s "Apakah kamu punya?!"
        b "Saya akan mendapatkannya"
        b "Segera kembali"
        scene mroom_day with fade
        b "{i} (Di mana dia menyimpan lotion?) {/i}"
        "..."
        b "{i} (ah ini dia) {/i}"
        "..."
        scene sroom_inst_photos2_b with fade
        "..."
        b "Bisakah saya menarik tali sedikit?"
        s "Saya akan melakukannya"
        scene sroom_inst_photos3_b with dissolve
        s "Bagus?"
        b "Yes"
        scene sroom_inst_photos2_b with dissolve
        "..."
        b "Errm"
        b "Saya pikir Anda harus menghapus seluruh bagian atas"
        s "Apa!"
        b "Karena saya tidak dapat mencapai bagian terbakar sinar matahari di sana"
        if srel >=60:
            s "Hmm..."
            s "Alright"
            scene sroom_inst_photos4_b with dissolve
            s "Jika Anda datang sisi ini, anggap diri Anda mati"
            b "Heh yeah"
            b "Jangan khawatir tentang itu"
            scene sroom_inst_photos5_b with dissolve
            b "Bagaimana dengan bagian bawahnya?"
            s "Saya pikir Anda ingin mati!"
            s "Keluar!"
            b "Bagaimana jika saya tidak?"
            s "Beri aku atasanku! Dimana itu?"
            scene sroom_inst_photos6_b with dissolve
            menu:
                "Saya memiliki atasan Anda di sini datang dan mendapatkannya":
                    b "Saya memiliki atasan Anda di sini datang dan mendapatkannya"
                    pass
                "Jika Anda mau, saya juga bisa menerapkan lotion dari depan":

                    scene sroom_inst_photos6_c with dissolve
                    s "Anda ingin mati, datang"
                    b "Yeah"
                    pass

            scene sroom_inst_photos7_b with vpunch
            s "Aku akan membunuhmu, aku berkata!"
            b "Hahaha tunggu!"
            scene sroom_inst_photos8_b with fade
            b "Anda gila"
            "..."
            b "Ngomong -ngomong, mereka indah"
            scene sroom_inst_photos9_b with dissolve
            "..."
            scene door with fade
            b "{i} (...) {/i}"
            "Itu semua dalam versi ini"
            call screen gnav
        else:
            s "TIDAK!"
            s "Saya akan melanjutkan!"
            s "Keluar!"
            scene door with fade
            b "{i} (sialan yang dia patah!?) {/i}"
            "Naikkan poin Anda menjadi 60"
            call screen gnav
    else:

        pass





    scene door with fade
    b "{i} (...) {/i}"
    call screen gnav


label sburn_study_enter:
    scene sroom_st5_b with hpunch
    s "[bname] !! Apa yang salah denganmu?"
    b "Hai [sname], apa yang kamu lakukan?"
    s "Dengan serius!"
    b "Apa?"
    s "Anda masuk dan bertanya apa yang saya lakukan?"
    b "Jadi apa?"
    scene sroom_st7_b with dissolve
    b "Saya melihat Anda membutuhkan bantuan untuk ini"
    s "Tidak, saya bisa mengelola"
    b "Oke, sesuai keinginan Anda"
    scene door with fade
    b "{i} (...) {/i}"
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc