label neighb:
    if neibrep ==0:
        $ neibrep = 1
        scene neist0 with fade
        play sound "sounds/doorbell.wav"
        n "Siapa itu?"
        stop sound
        scene neist with dissolve
        b "Hi"
        n "Anda!"
        b "Saya baru saja menjelaskan hal ini"
        n "Sit"
        scene neist1 with dissolve
        n "Tidak ada yang perlu diperjelas"
        b "There is"
        b "Saya tidak memiliki kunci saya"
        if persistent.patch_enabled:
            b "Dan ibu dan saudara perempuan saya keluar"
            pass
        else:
            b "Dan teman sekamar saya keluar"
            pass
        n "Begitu?"
        n "Tapi aku tahu gadis muda itu masih ada"
        b "Ah, apakah kamu mengawasi kami?"
        n "Tidak, tapi saya sudah tua dan saya tinggal di rumah sepanjang hari"
        n "Jadi saya perhatikan ketika orang keluar dan di gedung ini"
        b "{i} (wanita tua menyeramkan) {/i}"
        b "Tapi sebenarnya mereka berdua keluar"
        b "Jadi jika Anda tidak keberatan saya tinggal di sini sampai mereka kembali"
        scene neist1a with dissolve
        n "Ya itu baik -baik saja, Anda bisa tinggal dan membantu saya menyirami tanaman saya"
        n "Saya mengalami sakit punggung"
        b "Ya, itu baik -baik saja"
        n "Anda bisa mulai dari sana di dekat jendela"
        scene neist1b with fade
        b "Mudah"
        n "Itu juga"
        scene neist1c with dissolve
        "..."
        nd "Bu, siapa itu?"
        scene neist2 with dissolve
        b "Huh"
        n "Itu tetangga kita"
        n "Ngomong -ngomong, whats your name"
        scene neist3 with dissolve
        b "Yes"
        n "Siapa namamu?"
        b "Err it \ 's [bname]"
        n "Senang bertemu denganmu [bname]"
        n "I'm Katy"
        n "Dan putri saya adalah Masha"
        b "Senang bertemu denganmu Masha"
        nd "Senang bertemu denganmu juga"
        n "Baik saya pikir seseorang datang"
        n "Anda bisa pergi sekarang"
        b "Baiklah, terima kasih telah membantu saya"
        scene hall_d with fade
        "..."
        call screen gnav
    else:

        scene neist0 with fade
        play sound "sounds/doorbell.wav"
        n "Siapa itu?"
        stop sound
        scene neist with dissolve
        b "Hi"
        n "Anda!"
        b "Saya kehilangan kunci lagi"
        n "Begitu?"
        b "Yes"
        n "Bagus, Anda dapat membantu saya menyirami tanaman"
        b "Yes sure"
        n "Anda bisa mulai dari sana di dekat jendela"
        scene neist1b with fade
        b "Mudah"
        n "Itu juga"
        scene neist1c with dissolve
        "..."
        scene neist2 with dissolve
        nd "Ah [bname] lagi"
        b "Ya itu aku"
        n "Anda bisa pergi sekarang"
        b "Baiklah, terima kasih telah membantu saya"
        menu:
            "Ambil masha untuk bertemu [sname]":
                b "Err"
                scene neist3 with dissolve
                b "Saya bertanya -tanya apakah Masha ingin bergabung dengan saya dan ..."
                b "[sname] di pantai"
                n "Mhhm"
                n "Jika dia mau"
                nd "Ya kenapa tidak"
                b "Ok saya akan segera kembali"
                scene b_tv_s_r30 with fade
                b "Jadi apa yang kamu katakan?"
                s "Dengan serius? Seorang gadis, tetangga kita?"
                b "Mengapa tidak?"
                if srel >=100:
                    s "Hmm Ok"
                    $ neibrep += 1
                    jump sneibeach
                else:
                    s "No thanks"
                    scene hall_d with fade
                    b "{i} (Saya perlu meningkatkan hubungan saya dengan [sname] menjadi 100) {/i}"
                    call screen gnav
            "Bawa Masha ke pantai" if neibrep >=2:
                b "Err"
                scene neist3 with dissolve
                b "Saya bertanya -tanya apakah Masha ingin bergabung dengan saya dan ..."
                b "[sname] di pantai"
                n "Mhhm"
                n "Jika dia mau"
                nd "Ya kenapa tidak"
                b "Ok lepaskan"
                jump mashabeach
            "Meninggalkan":

                pass
        scene hall_d with fade
        "..."
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc