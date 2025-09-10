label newdays:
    $ day += 1
    $ Hour = 9
    $ drinkforbname = 0
    $ beachelainedone = 0
    $ beachrowenadone = 0
    $ beachdone = 0
    $ bstudied = 0
    $ tvwatched = 0
    $ pagecheckdone = 0
    $ swindowchecked = 0
    $ instresearchdone = 0
    $ stewcalled = 0
    $ sroomride = 0
    $ hallcamerachecked = 0
    $ hallcameracheckedm = 0
    $ stalkdone = 0
    if msho ==2:
        scene black
        $ msho = 3
        "Sementara itu di rumah"
        scene mshirt with fade
        m "Apa yang kamu inginkan?"
        b "Saya punya sesuatu untuk Anda katakan saya maaf"
        b "Tolong coba"
        m "Turn"
        scene mshirt1 with dissolve
        m "Terima kasih"
        $ mrel += 5
        b "Apakah Anda memaafkan saya?"
        m "Yes"
        scene mshirt2 with dissolve
        m "Listen dear"
        m "Ada hal -hal yang tidak boleh Anda katakan kepada seorang wanita"
        m "Apalagi jika wanita itu ..."
        b "JIKA APA?"
        m "Hanya itu"
        b "Hmm"
        b "Ok"
        m "Beri kami bir"
        scene mshirt3 with fade
        b "Jadi bagaimana semuanya"
        m "As always"
        m "Shit"
        b "Maaf untuk itu"
        b "Apakah Anda ingin pijatan?"
        m "Pijat saja, atau melibatkan rasa sakit?"
        menu:
            "Beberapa cinta, tidak ada rasa sakit":
                scene mshirt4 with fade
                m "Lalu lakukan"
                scene mshirt5 with dissolve
                m "Apa yang sedang kamu lakukan?"
                scene mshirt6 with dissolve
                b "Menunjukkan cinta"
                m "Wait"
                scene mshirt7 with dissolve
                m "Wait"
                scene mklo with fade
                "..."
                b "Ah"
                "..."
                b "Enough"
                scene msboob
                m "Mhhm"
                "..."
                "..."
                m "Yes"
                scene mshirt8 with fade
                b "Ah"
                b "Selamat malam"
                m "Ah selamat malam"
                pass
            "Nyeri itu baik":


                m "Mhhm"
                m "Saya ingin menghilangkan rasa sakit [bname] tidak menambahkannya"
                b "Saya akan menghilangkan rasa sakitnya"
                scene mshirt9 with fade
                m "Apa kamu yakin?"
                b "Trust me"
                scene mshirt10 with dissolve
                m "..."
                scene bmdom
                m "[bname]!"
                b ""
                "..."
                m "Ahhh"
                scene mshirt11 with dissolve
                "..."
                $ persistent.unlock_53 = True
                scene msdom
                if persistent.patch_enabled:
                    m "Anda ingin bercinta pantat Mommy ya!"
                    m "Jilat ini"
                    pass
                else:
                    m "Anda ingin bercinta pantat saya ya!"
                    m "Jilat ini"
                    pass
                scene mshirt12 with fade
                "..."
                pass
    else:

        pass
    if snameworkmelinda ==2:
        $ snameworkmelinda =3
        pass
    else:
        pass
    $ hallcamerachecked = 0
    $ hallcameracheckedm = 0
    $ stalkdone = 0
    if day >= 8:
        $ day = 1
        $ bworked = 0
        $ wk += 1
        $ bexercise -= 1
        $ staway -= 1
        $ mrel -= 5
        $ dayname = (_("Monday"))
    elif day == 1:
        $ bworked = 0
        $ dayname = (_("Monday"))
    elif day == 2:
        $ bworked = 0
        $ dayname = (_("Tuesday"))
    elif day == 3:
        $ mburnt = 0
        $ staway -= 1
        $ bexercise -= 1
        $ bworked = 0
        $ dayname = (_("Wednesday"))
    elif day == 4:
        $ bworked = 0
        $ sburnt = 0
        $ mrel -= 5
        $ srel -= 5
        $ dayname = (_("Thursday"))
    elif day == 5:
        $ bworked = 0
        $ staway -= 1
        $ dayname = (_("Friday"))
    elif day == 6:
        $ bworked = 0
        $ dayname = (_("Saturday"))
    elif day == 7:
        $ bworked = 0
        $ stewartcalled = 0
        $ dayname = (_("Sunday"))
    scene broom_day with fade
    "..."
    if startnework >= 1 and melsw >= 9 and msexwork >=3 and sgoestost >2 and snameworkmelinda==4 and msfkd >=1 and gnight >4 and persistent.unlock_23 == True:
        jump vn

    if bnamefixcheryl ==2:
        $ bnamefixcheryl = 3
        pass
    "..."
    if snamedrinkminus >=3:
        $ snamedrink = 0
        $ snamedrinkminus = 0
        call screen gnav

    if sgrm >= 5:
        $ sgrm = 1
        call screen gnav

    if elaineshowsup ==1 and day ==7:
        $ elaineshowsup = 2
        call screen gnav

    if cherylevent >=2 and cherylevent <5:
        $ cherylevent += 1
        call screen gnav

    elif elaineagain == 2 and day ==7:
        $ elaineagain = 3
        call screen gnav


    elif workrequest ==3:
        $ ebizcheck -= 1
        if snamedrink ==2:
            play sound "sounds/doorbell.wav"
            b "Hmm siapa itu saat ini?"
            stop sound
            scene delivery with fade
            b "Ahh itu minuman keras untuk [sname]"
            b "Terima kasih"
            $ snamedrink = 3
            call screen gnav

        if go_counter >4:
            scene bgo with dissolve
            b "Ahhhh Hari Baru!"
            m "[mname]!"
            b "Selamat pagi"
            m "Mau jelaskan ini?"
            scene bgo1 with dissolve
            b "Apa itu?"
            m "Ini"
            "..."
            scene etv_cbw with fade
            b "Err ... itu ..."
            scene bgo2 with dissolve
            m "Keluar dari rumah saya!"
            b "Apakah kamu serius?"
            if persistent.patch_enabled:
                m "Ya pergi ke ayahmu"
                m "Anda sama -sama sama"
                pass
            else:
                m "Ya hidup dengan stewart"
                m "Anda sama -sama sama"
                pass
            scene bgo3 with dissolve
            b "Ok fine"
            b "{i} (What a Bitch is [sname]) {/i}"
            scene black
            "Permainan selesai"
            return
        else:


            if hallcamera ==1:
                play sound "sounds/doorbell.wav"
                b "Hmm siapa itu saat ini?"
                stop sound
                scene delivery with fade
                b "Ahh itu kamera"
                b "Terima kasih"
                $ hallcamera = 2
                call screen gnav

            elif strongdrinksforgirlnight ==2:
                play sound "sounds/doorbell.wav"
                b "Hmm siapa itu saat ini?"
                stop sound
                scene delivery with fade
                b "Ahh itu minuman keras"
                b "Terima kasih"
                $ strongdrinksforgirlnight = 3
                call screen gnav


            elif toidoorscrew ==2:
                play sound "sounds/doorbell.wav"
                b "Hmm siapa itu saat ini?"
                stop sound
                scene delivery with fade
                b "Terima kasih"
                $ toidoorscrew = 3
                call screen gnav

            elif spiercings ==1:
                play sound "sounds/doorbell.wav"
                b "Hmm siapa itu saat ini?"
                stop sound
                scene delivery with fade
                b "Terima kasih"
                $ spiercings = 2
                call screen gnav

            elif mnurseoutfit ==1:
                play sound "sounds/doorbell.wav"
                b "Hmm siapa itu saat ini?"
                stop sound
                scene delivery with fade
                b "Terima kasih"
                $ mnurseoutfit = 2
                b "{i} (Saya akan memberikannya saat dia kembali dari kantor) {/i}"
                call screen gnav
            else:


                call screen gnav
    else:

        if hallcamera ==1:
            play sound "sounds/doorbell.wav"
            b "Hmm siapa itu saat ini?"
            stop sound
            scene delivery with fade
            b "Ahh itu kamera"
            b "Terima kasih"
            $ hallcamera = 2
            call screen gnav

        elif snamedrink ==2:
            play sound "sounds/doorbell.wav"
            b "Hmm siapa itu saat ini?"
            stop sound
            scene delivery with fade
            b "Ahh itu minuman keras untuk [sname]"
            b "Terima kasih"
            $ snamedrink = 3
            call screen gnav


        elif strongdrinksforgirlnight ==2:
            play sound "sounds/doorbell.wav"
            b "Hmm siapa itu saat ini?"
            stop sound
            scene delivery with fade
            b "Ahh itu minuman keras"
            b "Terima kasih"
            $ strongdrinksforgirlnight = 3
            call screen gnav


        elif snamedrink ==2:
            play sound "sounds/doorbell.wav"
            b "Hmm siapa itu saat ini?"
            stop sound
            scene delivery with fade
            b "Ahh itu minuman keras untuk [sname]"
            b "Terima kasih"
            $ snamedrink = 3
            call screen gnav


        elif toidoorscrew ==2:
            play sound "sounds/doorbell.wav"
            b "Hmm siapa itu saat ini?"
            stop sound
            scene delivery with fade
            b "Terima kasih"
            $ toidoorscrew = 3
            call screen gnav

        elif spiercings ==1:
            play sound "sounds/doorbell.wav"
            b "Hmm siapa itu saat ini?"
            stop sound
            scene delivery with fade
            b "Terima kasih"
            $ spiercings = 2
            call screen gnav

        elif mnurseoutfit ==1:
            play sound "sounds/doorbell.wav"
            b "Hmm siapa itu saat ini?"
            stop sound
            scene delivery with fade
            b "Terima kasih"
            $ mnurseoutfit = 2
            b "{i} (Saya akan memberikannya saat dia kembali dari kantor) {/i}"
            call screen gnav
        else:

            call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
