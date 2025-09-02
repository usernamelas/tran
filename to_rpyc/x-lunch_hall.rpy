
image slanod:
    "sla00.jpg"
    pause 0.01
    "sla01.jpg"
    pause 0.01
    "sla02.jpg"
    pause 0.01
    "sla03.jpg"
    pause 0.01
    "sla04.jpg"
    pause 0.01
    "sla05.jpg"
    pause 0.01
    "sla06.jpg"
    pause 0.01
    "sla07.jpg"
    pause 0.01
    "sla08.jpg"
    pause 0.01
    "sla09.jpg"
    pause 0.01
    "sla10.jpg"
    pause 0.01
    "sla11.jpg"
    pause 0.01
    "sla12.jpg"
    pause 0.01
    "sla13.jpg"
    pause 0.01
    "sla14.jpg"
    pause 0.01
    "sla15.jpg"
    pause 0.01
    "sla16.jpg"
    pause 0.01
    "sla17.jpg"
    pause 0.01
    "sla18.jpg"
    pause 0.01
    "sla19.jpg"
    pause 0.01
    "sla20.jpg"
    pause 0.01
    "sla21.jpg"
    pause 0.01
    "sla22.jpg"
    pause 0.01
    "sla23.jpg"
    pause 0.01
    "sla24.jpg"
    pause 0.01
    "sla25.jpg"
    pause 0.01
    "sla26.jpg"
    pause 0.01
    "sla27.jpg"
    pause 0.01
    "sla28.jpg"
    pause 0.01
    "sla29.jpg"
    pause 0.01
    "sla30.jpg"
    pause 0.01
    "sla31.jpg"
    pause 0.01
    "sla32.jpg"
    pause 0.01
    "sla33.jpg"
    pause 0.01
    "sla34.jpg"
    pause 0.01
    "sla35.jpg"
    pause 0.01
    "sla36.jpg"
    pause 0.01
    "sla37.jpg"
    pause 0.01
    "sla38.jpg"
    pause 0.01
    "sla39.jpg"
    pause 0.01
    "sla40.jpg"
    pause 0.01
    "sla41.jpg"
    pause 0.01
    "sla42.jpg"
    pause 0.01
    "sla43.jpg"
    pause 0.01
    "sla44.jpg"
    pause 0.01
    "sla45.jpg"
    pause 0.01
    "sla46.jpg"
    pause 0.01
    "sla47.jpg"
    pause 0.01
    "sla48.jpg"
    pause 0.01
    "sla49.jpg"
    pause 0.01
    "sla50.jpg"
    pause 0.01
    repeat

label lunch_hall:
    if workrequest ==3 and worktalk ==1:
        scene slunch with fade
        s "Hmmm"
        b "[sname] belum kembali?"
        s "No"
        s "Dia menyuruh saya menyiapkan makan siang hari ini"
        b "Lalu mengapa hal yang sama, mengapa Anda tidak mempersiapkan sesuatu yang menyenangkan"
        scene slunch1 with dissolve
        s "Duduk!"
        b "Yes ma'am"
        b "Ha ha ha!"
        scene slunch2 with dissolve
        s "Sekarang makan!"
        scene slunch3 with fade
        "..."
        b "Apakah Anda pikir dia akan mendapatkan pekerjaan?"
        s "Aku tidak tahu"
        b "Saya harap dia tidak karena saya tidak menyukai tempat ini"
        s "Mengapa?"
        b "Saya hanya tidak menyukainya"
        s "Baik saya harap dia melakukannya karena saya saya menyukainya"
        b "Mudah untuk Anda katakan karena Anda memiliki Rowena di sekitar"
        s "Nah, Anda bisa mengubahnya"
        s "Anda harus mendapatkan lebih banyak sosial, dan berhenti menjadi kutu buku cabul"
        b "Mee!"
        scene slunch4 with dissolve
        s "Ya kamu"
        b "Apa ..."
        s "Biarkan aku makan"
        b "Ok"
        scene slunch5 with fade
        b "Sampai jumpa lagi"
        s "..."
        scene broom_day with fade
        "..."
        call screen gnav


    elif workrequest ==3 and worktalk ==2 and day !=7:
        if snaked_lunch == 1:
            jump s_hot_lunch
        else:

            pass
        scene slunch with fade
        s "Hmmm"
        b "Apa untuk makan siang"
        scene slunch1 with dissolve
        s "Duduk!"
        scene slunch2 with dissolve
        s "Sekarang makan!"
        scene slunch6 with dissolve
        s "Tanpa pertanyaan"
        b "Yes ma'am"
        if nadiaasksforstrongdrinks == 1 and snamedrink == 0:
            $ snamedrink = 1
            scene slunch3 with dissolve
            s "Saya hanya mengajukan pertanyaan"
            b "Eh huh!"
            s "Apakah Anda memiliki minuman keras yang Anda bawa terakhir kali?"
            b "Hehe kenapa kamu membutuhkannya?"
            s "Saya hanya ingin mencobanya lagi"
            s "Bisakah kamu memberiku botol?"
            b "Of course"
            b "Apa yang saya dapatkan sebagai balasannya?"
            s "Dapatkan dan Anda akan melihat"
            b "Ok"
            pass
        else:


            scene slunch7 with dissolve
            s "Bagus"
            b "Hahahaha"
            pass

        scene slunch3 with fade
        b "Senang sekarang? Dia mendapat pekerjaan"
        s "Ya, tentu saja"
        if snameworkmelinda ==1:
            b "Ngomong -ngomong, aku punya sesuatu untuk ditanyakan padamu"
            s "Apa itu?"
            b "Apakah Anda ingin memiliki pekerjaan paruh waktu?"
            s "No"
            b "Anda tidak ingin tahu berapa banyak uang yang bisa Anda dapatkan?"
            s "Apakah terlalu banyak?"
            b "Sekitar 00 hingga 000 per kunjungan"
            s "Hmm"
            s "Biarkan saya menebak, pengawalan?"
            b "Ya, tapi mereka berkualitas tinggi, pribadi"
            b "Semacam klub pribadi"
            s "Saya akan memikirkannya"
            $ snameworkmelinda = 3
            b "Ok"
            pass
        elif snameworkmelinda == 4:
            b "Apakah Anda memutuskan tentang penawaran Melinda"
            s "No"
            b "Mengapa?"
            s "Saya perlu memikirkannya"
            b "Tidak ada yang perlu dipikirkan"
            s "Bagaimana Anda bisa menemukan alibi untuk saya meninggalkan rumah selama seminggu atau lebih?"
            b "Hmm true"
            b "Kita perlu memikirkan itu"
            pass
        else:
            pass
            "..."
        if snamedrink == 3:
            $ snamedrink = 4
            b "Lihat"
            b "Aku punya minuman ini untukmu"
            scene slunch3v with dissolve
            s "Yaaay!"
            s "Terima kasih"
            jump sdrinkreward

        elif elaineshowsup >=1 and day ==6:
            if beachalone == 2:
                $ beachalone = 3
                b "Lihat"
                b "Aku punya voucher ini untukmu"
                b "Anda bisa menggunakannya besok"
                s "Voucher jenis apa"
                b "Voucher belanja, ke mal terdekat"
                s "Berapa banyak di dalamnya!"
                $ giftcardrepeat += 1
                b "200 $"
                s "Wow serius!"
                b "Yes"
                scene slunch3v with dissolve
                s "Yaaay!"
                s "Saya akan pergi dengan rowena"
                b "Besar"
                if giftcardrepeat >= 4:
                    s "Tunggu di sini, saya akan segera kembali"
                    b "Hmmm"
                    scene slkmo with fade
                    b "Apa ..."
                    b "Sungguh!"
                    scene slunch_hot3 with dissolve
                    s "Ini adalah hadiah Anda karena Anda memberi saya voucher"
                    s "Sekarang makan!"
                    b "Yes ma'am"
                    scene slunch_hot4 with dissolve
                    "..."
                    scene slunch_hot5 with fade
                    b "Makanan enak"
                    s "Anda menyukainya?"
                    b "Yeah"
                    scene slunch_hot6 with dissolve
                    b "Lovely dress"
                    s "Yes"
                    b "Bisakah saya melihatnya?"
                    s "Setelah kita makan"
                    b "Ok"
                    scene slkmo1 with fade
                    b "Hmmm"
                    b "Sialan panas"
                    scene slkmo2 with dissolve
                    s "Tunggu!"
                    b "Wow kamu tidak memakai celana dalam?"
                    scene slkmo3 with dissolve
                    s "..."
                    b "Mari kita lihat"
                    scene slkmo4 with dissolve
                    s "Tolong berhenti [bname]"
                    b "Hmm"
                    b "Mari kita ambil foto Anda dalam hal ini"
                    s "Untuk halaman saya?"
                    b "Yes"
                    s "Ok keren"
                    scene slkmo5 with fade
                    s "Saya akan mengenakan celana dalam"
                    b "Anda tidak perlu"
                    b "Itu tidak menunjukkan"
                    b "Ubah pose"
                    scene slkmo6 with dissolve
                    "..."
                    scene slkmo7 with dissolve
                    b "Saya pikir Anda harus melepasnya!"
                    s "No"
                    b "Lalu, biarkan aku mengambil closeup seksi tanpa wajah"
                    b "Ini bagus untuk halaman"
                    s "Hmm"
                    s "Ok"
                    b "{/i} (hehehe semua orang akan tahu itu kamu) {i}"
                    menu:
                        "Kedudukan":
                            scene slkmo8 with dissolve
                            b "Itu keren"
                            scene slkmo9 with dissolve
                            "..."
                            scene slkmo10 with dissolve
                            b "Tembakan bagus"
                            b "Biarkan saya melakukan closeup"
                            scene slkmo11 with dissolve
                            "..."
                            b "Sedikit lagi"
                            scene slkmo12 with dissolve
                            b "Awesome"
                            b "Sedikit lagi?"
                            s "Tidak [bname] itu cukup"
                            b "Ohh..."
                            b "All right"
                            scene slkmo5 with fade
                            b "Sampai jumpa"
                            scene door with fade
                            b "{/i} (...) {i}"
                            call screen gnav


                        "Semua merangkak" if giftcardrepeat > 1:
                            scene slkmo13 with dissolve
                            b "Itu tidak ada di keempatnya"
                            s "Yes"
                            b "Tapi aku akan mengambil sesuatu yang menyenangkan"
                            b "Tetap seperti Anda"
                            scene slkmo14 with dissolve
                            b "Done"
                            b "Ubah pose"
                            scene slkmo15 with dissolve
                            s "Apakah gaunnya baik -baik saja?"
                            b "Yes awesome"
                            b "Tunggu biarkan saya mengambilnya dari beberapa sudut"
                            scene slkmo16 with dissolve
                            "..."
                            s "Tidak ada wajah, oke!?"
                            b "Yes sure"
                            scene slkmo17 with dissolve
                            b "Bagus"
                            b "Cobalah sesuatu yang lebih, saya percaya Anda bisa melakukan yang lebih baik"
                            scene slkmo18 with dissolve
                            $ persistent.unlock_14 = True
                            s "No face"
                            b "Ok Ok"
                            s "Saya pikir itu cukup"
                            b "Ya seperti yang Anda inginkan"
                            b "Saya akan mengerjakannya nanti"
                            b "Sampai jumpa"
                            scene door with fade
                            b "{/i} (...) {i}"
                            call screen gnav

                elif srel >= 400:
                    s "Tunggu di sini, saya akan segera kembali"
                    b "Hmmm"
                    scene slkmo with fade
                    b "Apa ..."
                    b "Sungguh!"
                    scene slunch_hot3 with dissolve
                    s "Ini adalah hadiah Anda karena Anda memberi saya voucher"
                    s "Sekarang makan!"
                    b "Yes ma'am"
                    scene slunch_hot4 with dissolve
                    "..."
                    scene slunch_hot5 with fade
                    b "Makanan enak"
                    s "Anda menyukainya?"
                    b "Yeah"
                    scene slunch_hot6 with dissolve
                    b "Lovely dress"
                    s "Yes"
                    b "Bisakah saya melihatnya?"
                    s "Setelah kita makan"
                    b "Ok"
                    scene slkmo1 with fade
                    b "Hmmm"
                    b "Sialan panas"
                    scene slkmo2 with dissolve
                    s "Tunggu!"
                    b "Wow kamu tidak memakai celana dalam?"
                    scene slkmo3 with dissolve
                    s "..."
                    b "Mari kita lihat"
                    scene slkmo4 with dissolve
                    s "Tolong berhenti [bname]"
                    b "Hmm"
                    b "Mari kita ambil foto Anda dalam hal ini"
                    s "Untuk halaman saya?"
                    b "Yes"
                    s "Ok keren"
                    scene slkmo5 with fade
                    s "Saya akan mengenakan celana dalam"
                    b "Anda tidak perlu"
                    b "Itu tidak menunjukkan"
                    b "Ubah pose"
                    scene slkmo6 with dissolve
                    "..."
                    scene slkmo7 with dissolve
                    b "Saya pikir Anda harus melepasnya!"
                    s "No"
                    b "Lalu, biarkan aku mengambil closeup seksi tanpa wajah"
                    b "Ini bagus untuk halaman"
                    s "Hmm"
                    s "Ok"
                    b "{/i} (hehehe semua orang akan tahu itu kamu) {i}"
                    menu:
                        "Kedudukan":
                            scene slkmo8 with dissolve
                            b "Itu keren"
                            scene slkmo9 with dissolve
                            "..."
                            scene slkmo10 with dissolve
                            b "Tembakan bagus"
                            b "Biarkan saya melakukan closeup"
                            scene slkmo11 with dissolve
                            "..."
                            b "Sedikit lagi"
                            scene slkmo12 with dissolve
                            b "Awesome"
                            b "Sedikit lagi?"
                            s "Tidak [bname] itu cukup"
                            b "Ohh..."
                            b "All right"
                            scene slkmo5 with fade
                            b "Sampai jumpa"
                            scene door with fade
                            b "{/i} (...) {i}"
                            call screen gnav


                        "Semua merangkak" if giftcardrepeat > 1:
                            scene slkmo13 with dissolve
                            b "Itu tidak ada di keempatnya"
                            s "Yes"
                            b "Tapi aku akan mengambil sesuatu yang menyenangkan"
                            b "Tetap seperti Anda"
                            scene slkmo14 with dissolve
                            b "Done"
                            b "Ubah pose"
                            scene slkmo15 with dissolve
                            b "Awesome"
                            b "Tunggu biarkan saya mengambilnya dari beberapa sudut"
                            scene slkmo16 with dissolve
                            "..."
                            s "Tidak ada wajah, oke!?"
                            b "Yes sure"
                            scene slkmo17 with dissolve
                            b "Bagus"
                            b "Cobalah sesuatu yang lebih, saya percaya Anda bisa melakukan yang lebih baik"
                            scene slkmo18 with dissolve
                            s "No face"
                            b "Ok Ok"
                            s "Saya pikir itu cukup"
                            b "Ya seperti yang Anda inginkan"
                            b "Saya akan mengerjakannya nanti"
                            b "Sampai jumpa"
                            scene door with fade
                            b "{/i} (...) {i}"
                            call screen gnav
                else:


                    pass
            else:

                pass
            b "Omong-omong"
            b "Tahukah Anda bahwa Elaine tidur di sini tadi malam?"
            s "Benar-benar?"
            b "Saya tidak tetapi ada sesuatu yang terjadi antara dia dan bf -nya"
            b "Dia tidur di kamar [sname]"
            s "Ah, oke"
            pass
        else:
            if beachalone == 2 and day ==6:
                $ beachalone = 3
                b "Lihat"
                b "Aku punya voucher ini untukmu"
                b "Anda bisa menggunakannya besok"
                s "Voucher jenis apa"
                b "Voucher belanja, ke mal terdekat"
                s "Berapa banyak di dalamnya!"
                b "200 $"
                s "Wow serius!"
                b "Yes"
                scene slunch3v with dissolve
                s "Yaaay!"
                s "Saya akan pergi dengan rowena"
                b "Besar"
                pass
            else:
                pass

        scene slunch4 with dissolve
        s "Biarkan aku makan"
        b "Ok"
        scene slunch8 with fade
        b "Terima kasih untuk makan siang [mname]"
        s "Terima kasih kembali"
        menu:
            "Bantu dia dengan hidangan":
                if srel >=30:
                    scene slunch9a with fade
                    b "Saya akan membantu Anda dengan hidangan"
                    scene slunch10a with dissolve
                    s "Hah!"
                    scene slunch11a with vpunch
                    s "[bname]! Saya pikir Anda akan membantu saya dengan hidangan"
                    b "Saya tentu saja akan"
                    s "Kalau begitu lakukan"
                    scene slunch10 with fade
                    b "Done"
                    scene slunch11 with dissolve
                    s "Terima kasih"
                    s "Lihat ya!"
                    b "{/i} (apa -apaan! Hanya terima kasih, mungkin lain kali saya harus mencoba tidak membantunya) {i}"
                    menu:
                        "Ambil dia" if workrequest ==3 and day !=7:
                            scene slunchdom with hpunch
                            b "Kemarilah!"
                            scene slunchdom1 with dissolve
                            if sdom >=100:
                                s "Biarkan aku pergi [bname]!"
                                menu:
                                    "Biarkan dia pergi":
                                        if srel >=200:
                                            s "Hmm"
                                            scene slunchdom8 with dissolve
                                            s "Mengapa Anda meraih saya jika Anda ingin membiarkan saya pergi?"
                                            b "Dengan serius?"
                                            b "Anda baru saja meminta saya untuk meninggalkan Anda sendiri"
                                            scene slunchdom9 with dissolve
                                            s "Ya tapi saya pikir Anda ingin mencium saya"
                                            b "Oh baik -baik saja"
                                            scene slunchdom10 with dissolve
                                            s "Hmm"
                                            scene slunchdom11 with fade
                                            "..."
                                            scene slunchdom12 with dissolve
                                            s "Hehe"
                                            scene slunchdom13 with dissolve
                                            "..."
                                            scene slunchdom14 with dissolve
                                            s "Saya akan pergi ke kamar saya sekarang"
                                            b "Ok"
                                            if srel >=400:
                                                scene slunchdom16 with fade
                                                s "{/i} (akankah dia datang?) {i}"
                                                scene slunchdom15 with dissolve
                                                b "Wow"
                                                scene slunchdom17 with dissolve
                                                b "Bagus"
                                                menu:
                                                    "Bisakah saya merasakannya?":
                                                        $ smaid += 1
                                                        scene slunchdom28 with dissolve
                                                        s "Anda tidak mengatakan Anda ingin membuat saya merasakan sesuatu"
                                                        b "Hehe"
                                                        scene slunchdom29 with dissolve
                                                        s "Ahh"
                                                        scene slunchdom30 with dissolve
                                                        s "Ahhh"
                                                        scene slunchdom31 with dissolve
                                                        "..."
                                                        scene slunchdom32 with dissolve
                                                        s "Ahhhh"
                                                        scene slunchdom33 with dissolve
                                                        s "[bname] !!!"
                                                        scene slunchdom34 with hpunch
                                                        b "Ahh"
                                                        scene slunchdom35 with fade
                                                        "..."
                                                        scene broom_day with fade
                                                        "..."
                                                        call screen gnav
                                                    "Mari kita ambil beberapa foto":

                                                        if smaid >= 3:
                                                            s "Hmm"
                                                            s "Anda tidak meminta untuk merasakannya?"
                                                            b "Tidak perlu"
                                                            scene slunchdom18 with fade
                                                            "..."
                                                            scene slunchdom19 with dissolve
                                                            "..."
                                                            scene slunchdom20 with dissolve
                                                            b "Hmm"
                                                            menu:
                                                                "Persetan dia":
                                                                    scene slanod
                                                                    s "Ahhh"
                                                                    "..."
                                                                    b "Hhh"
                                                                    "..."
                                                                    s "Fuck harder"
                                                                    b "Yess"
                                                                    scene slunchdom21 with dissolve
                                                                    s "Ahhh"
                                                                    scene slunchdom22 with fade
                                                                    s "Apa sih [bname]"
                                                                    b "Maaf, saya menarik keluar"
                                                                    s "Ya tarik keluar, tapi jangan semprotkan saya dengan cum Anda"
                                                                    b "Hehehe sorry"
                                                                    pass
                                                                "Bermain dengannya":

                                                                    scene slunchdom23 with dissolve
                                                                    s "Hmmm"
                                                                    scene slunchdom24 with dissolve
                                                                    s "Ah"
                                                                    scene slunchdom25 with dissolve
                                                                    s "Apakah Anda akan memasukkannya ke dalam atau sekarang?"
                                                                    b "No"
                                                                    scene slunchdom26 with dissolve
                                                                    "..."
                                                                    scene slunchdom27 with dissolve
                                                                    s "Mhhhm"
                                                                    b "Sampai jumpa lagi"
                                                                    pass
                                                        else:


                                                            s "Ya, hanya satu"
                                                            scene slunchdom18 with fade
                                                            s "Itu saja"
                                                            pass
                                            else:
                                                pass
                                        else:

                                            "Naikkan poin Anda menjadi 200"
                                            pass
                                    "Bawa dia ke meja" if srel >=200:
                                        s "..."
                                        scene slunchdom2 with dissolve
                                        b "Aduh!"
                                        s "Dimana kamu membawaku?"
                                        scene slunchdom3 with dissolve
                                        b "Untuk ciuman"
                                        scene slunchdom4 with dissolve
                                        s "Hmmm"
                                        scene slunchdom3 with dissolve
                                        s "Terima kasih [bname]"
                                        s "Saya harus pergi"
                                        menu:
                                            "Cangkir payudaranya":
                                                scene slunchdom5 with dissolve
                                                s "[bname]! Apakah Anda tidak ada pikiran"
                                                b "Tidak, aku tidak"
                                                s "Kemudian lepaskan tangan Anda"
                                                b "Saya tidak menginginkannya"
                                                if scorr >= 60:
                                                    scene slunchdom6 with dissolve
                                                    s "Dan saya akan melakukan ini"
                                                    b "Aduh! Bola saya"
                                                    s "Hahaha"
                                                    b "Anda menyakiti saya"
                                                    scene slunchdom7 with dissolve
                                                    s "Hahaha"
                                                    s "Apa yang akan Anda lakukan tentang itu!"
                                                    b "Kami akan melihat"
                                                    s "Letakkan kaki terbaik Anda ke depan hahaha!"
                                                    jump staughtalesson
                                                else:

                                                    s "Enough [bname]"
                                                    s "Sampai jumpa lagi"
                                                    scene broom_day with fade
                                                    "Naikkan poin korupsi Anda menjadi 60"
                                                    call screen gnav
                                            "Melanjutkan":


                                                "..."
                                                pass
                                        s "Sampai jumpa lagi"
                                        scene broom_day with fade
                                        "..."
                                        call screen gnav
                            else:

                                s "Biarkan aku pergi [bname]!"
                                "Naikkan poin dominasi Anda menjadi 100"
                                pass
                        "Melanjutkan":

                            pass
                    scene broom_day with fade
                    "..."
                    call screen gnav
                else:

                    scene slunch9 with fade
                    b "Saya akan membantu Anda dengan hidangan"
                    scene slunch10 with dissolve
                    show screen srelup
                    "..."
                    $ srel += 2
                    b "Done"
                    hide screen srelup
                    scene slunch11 with dissolve
                    s "Terima kasih"
                    b "Lihat ya!"
                    scene broom_day with fade
                    "..."
                    call screen gnav
            "Tidak perlu":



                scene slunch5 with fade
                show screen sreldw
                b "Sampai jumpa lagi"
                $ srel -= 1
                s "..."
                hide screen sreldw
                scene slunch5_hr with dissolve
                s "Hai!"
                s "Apakah Anda tidak akan membantu saya dengan hidangan?"
                b "Hmm"
                menu:
                    "Apa yang saya dapatkan sebagai balasannya?":
                        s "Hah!"
                        s "Apa yang kamu inginkan?"
                        menu:
                            "Saya ingin melihat bikini yang saya beli untuk Anda" if bikini3 == 2:
                                s "Whaaat!?"
                                b "Ya, Anda mendengar saya"
                                if sdom >=25 and srel >=60:
                                    scene slunch6_hr with dissolve
                                    b "Ayo! Apa yang kamu pikirkan?"
                                    $ sstrip = 1
                                    s "Mulailah mencuci, saya akan memikirkannya"
                                    b "Ok keren"
                                    scene slunch12 with fade
                                    "..."
                                    b "Done!"
                                    s "Oke, duduk di sofa dan tunggu saya"
                                    scene slunch7_hr with fade
                                    "..."
                                    scene slunch8_hr with dissolve
                                    s "Ini akan sekilas"
                                    b "... OKE"
                                    if hotphotos_done == 1:
                                        b "{/i} (hehe sekilas pantatku) {i}"
                                        scene slunch9_hra with dissolve
                                        "..."
                                        b "Terlihat bagus untukmu"
                                        s "Thanks"
                                        scene slunch10_hr with dissolve
                                        "..."
                                        scene slunch19_hr with dissolve
                                        b "{/i} (keren! Dia berubah setelah kami melakukan pemotretan panas) {i}"
                                        scene slunch20_hr with dissolve
                                        if elaineshowsup ==1 and day ==6:
                                            e "Di mana saya bisa mendapatkan air?"
                                            scene slunchse with dissolve
                                            s "Hah!"
                                            e "Bikini yang bagus [mname]"
                                            s "Thanks"
                                            b "Air ada di meja dapur"
                                            scene slunchse1 with dissolve
                                            e "Ok"
                                            scene slunchse2 with dissolve
                                            e "Saya akan kembali tidur"
                                            e "Terima kasih teman -teman"
                                            e "Anda dapat melanjutkan apapun yang Anda lakukan"
                                            s "Senang sekarang?"
                                            pass

                                        elif elaineagain ==2 and day ==6:
                                            e "Di mana saya bisa mendapatkan air?"
                                            scene slunchse with dissolve
                                            s "Hah!"
                                            e "Bikini yang bagus [mname]"
                                            s "Thanks"
                                            b "Air ada di meja dapur"
                                            scene slunchse1 with dissolve
                                            e "Ok"
                                            scene slunchse2 with dissolve
                                            e "Saya akan kembali tidur"
                                            e "Terima kasih teman -teman"
                                            e "Anda dapat melanjutkan apapun yang Anda lakukan"
                                            e "Mhm [mname]"
                                            scene slunchse with dissolve
                                            s "Ya?"
                                            e "Bolehkah saya bertanya sesuatu?"
                                            s "Sure"
                                            e "Privately please"
                                            s "Ya mari kita pergi ke kamarku"
                                            jump etalkwithsname
                                        else:




                                            s "Senang sekarang?"
                                            pass

                                        b "Hmm"
                                        menu:
                                            "Apakah Anda ingin melakukan pemotretan?":
                                                b "Tentu saja saya senang"
                                                b "Apakah Anda ingin mengambil beberapa foto dalam hal ini?"
                                                scene slunch21_hr with dissolve
                                                s "Saat ini?"
                                                b "Ya kenapa tidak"
                                                s "Hanya sedikit foto"
                                                b "Yes"
                                                jump sroom_day_photos
                                            "Tentu saja saya":

                                                scene slunch22_hr with dissolve
                                                s "Aku akan pergi sekarang"
                                                if srel >=200:
                                                    scene slunched with hpunch
                                                    b "Wait"
                                                    s "Apa yang kamu inginkan?"
                                                    b "Tidak ada yang ekstra?"
                                                    s "Not now"
                                                    if sdom >=35:
                                                        b "Hmm kenapa?"
                                                        s "Saya tidak merasa seperti itu"
                                                        b "Tapi saya saya merasa seperti itu"
                                                        scene slunched1 with vpunch
                                                        b "Lepaskan"
                                                        s "Hmmm"
                                                        scene slunched2 with fade
                                                        s "..."
                                                        jump slunchplus
                                                    else:


                                                        b "Hmm kenapa?"
                                                        s "Saya tidak merasa seperti itu"
                                                        b "Ok"
                                                        b "Bye"
                                                        "Naikkan poin dominasi Anda menjadi 35"
                                                        b "Terima kasih atas hadiahnya"
                                                        scene broom_day with fade
                                                        "..."
                                                        call screen gnav
                                                else:

                                                    pass

                                                b "Terima kasih atas hadiahnya"
                                                scene broom_day with fade
                                                "..."
                                                call screen gnav
                                    else:
                                        pass
                                    scene slunch9_hr with dissolve
                                    "..."
                                    b "Terlihat bagus untukmu"
                                    s "Enough please"
                                    scene slunch10_hr with dissolve
                                    s "Aku akan pergi sekarang"
                                    b "Terima kasih"
                                    scene broom_day with fade
                                    b "{/i} (keren) {i}"
                                    call screen gnav
                                else:
                                    scene slunch6_hrefuse with dissolve
                                    s "Saya sendiri akan mencuci piring"
                                    s "Ada jalan keluar!"
                                    b "Berengsek!"
                                    b "Ok Ok"
                                    scene broom_day with fade
                                    "Naikkan poin dominasi Anda menjadi 25 dan hubungan ke 60"
                                    call screen gnav
                            "Ciuman":

                                if srel >=200:
                                    s "Ok"
                                    pass
                                else:
                                    s "Whaaat!?"
                                    b "Ya, hanya ciuman"
                                    pass
                                scene slunch6_hr with dissolve
                                b "Ayo! Apa yang kamu pikirkan?"
                                s "Mulailah mencuci, saya akan memikirkannya"
                                b "Ok keren"
                                scene slunch10 with fade
                                "..."
                                b "Selesai!"
                                scene slunch11hr with fade
                                s "Ok"
                                s "Tidak ada barang pervy!"
                                scene slunch12hr with dissolve
                                "..."
                                menu:
                                    "Lihatlah":
                                        scene slunch13hr with dissolve
                                        b "Hmmm"
                                        menu:
                                            "Cangkir":
                                                scene slunch13hra with hpunch
                                                "..."
                                                if srel >=300 and scorr >=30:
                                                    s "Huh"
                                                    b "{/i} (keren! Tidak ada reaksi) {i}"
                                                    scene slunch19hr with dissolve
                                                    b "Hah!"
                                                    scene slunch20hr with dissolve
                                                    b "Aduh!"
                                                    b "Tinggalkan penis saya sendirian"
                                                    scene slunch11hr with dissolve
                                                    s "Anda pikir Anda bisa menyentuh payudara saya"
                                                    s "Dan aku tidak bisa menyentuh milikmu"
                                                    b "Baik jika Anda menyentuh milik saya, Anda harus mengurusnya"
                                                    s "Same here"
                                                    s "Dan Anda menyentuh dulu, jadi Anda lebih baik menyelesaikan apa yang Anda mulai"
                                                    b "Tidak apa -apa tapi Anda memakai sesuatu yang bagus untuk saya"
                                                    s "Ok"
                                                    jump sposing
                                                else:



                                                    scene slunch13hrb with dissolve
                                                    s "Hai!"
                                                    b "Err"
                                                    b "Sorry"
                                                    scene broom_day with fade
                                                    b "{/i}(Damn){i}"
                                                    call screen gnav
                                            "Jangan":
                                                pass
                                    "Hal pervy":

                                        scene slunch13hr with dissolve
                                        "..."
                                        if srel >=100:
                                            scene slunch14hr with dissolve
                                            "..."
                                            scene slunch16hr with dissolve
                                            b "{/i} (keren! Tidak ada reaksi) {i}"
                                            scene slunch19hr with dissolve
                                            b "Hah!"
                                            if srel >=300 and scorr >=30:
                                                scene slunch20hr with dissolve
                                                b "Aduh!"
                                                b "Tinggalkan penis saya sendirian"
                                                scene slunch11hr with dissolve
                                                s "Anda pikir Anda bisa menyentuh payudara saya"
                                                s "Dan aku tidak bisa menyentuh milikmu"
                                                b "Baik jika Anda menyentuh milik saya, Anda harus mengurusnya"
                                                s "Same here"
                                                s "Dan Anda menyentuh dulu, jadi Anda lebih baik menyelesaikan apa yang Anda mulai"
                                                jump sboobjob
                                            else:
                                                "Meningkatkan hubungan dengan 300 dan korupsi menjadi 30"
                                                pass


                                        elif sblowjobdone == 1:
                                            scene slunch14hr with dissolve
                                            "..."
                                            scene slunch16hr with dissolve
                                            b "{/i} (keren! Tidak ada reaksi) {i}"
                                            scene slunch19hr with dissolve
                                            b "Hah!"
                                            if srel >=300 and scorr >= 30:
                                                scene slunch20hr with dissolve
                                                b "Aduh!"
                                                b "Tinggalkan penis saya sendirian"
                                                scene slunch11hr with dissolve
                                                s "Anda pikir Anda bisa menyentuh payudara saya"
                                                s "Dan aku tidak bisa menyentuh milikmu"
                                                b "Baik jika Anda menyentuh milik saya, Anda harus mengurusnya"
                                                s "Same here"
                                                s "Dan Anda menyentuh dulu, jadi Anda lebih baik menyelesaikan apa yang Anda mulai"
                                                jump sboobjob
                                            else:
                                                "Meningkatkan hubungan dengan 300 dan korupsi menjadi 30"
                                                pass

                                        elif sphotos_progress == 2:
                                            scene slunch14hr with dissolve
                                            "..."
                                            scene slunch17hr with dissolve
                                            b "{/i} (keren! Tidak ada reaksi) {i}"
                                            scene slunch19hr with dissolve
                                            b "Hah!"
                                            if srel >=300 and scorr >= 30:
                                                scene slunch20hr with dissolve
                                                b "Aduh!"
                                                b "Tinggalkan penis saya sendirian"
                                                scene slunch11hr with dissolve
                                                s "Anda pikir Anda bisa menyentuh payudara saya"
                                                s "Dan aku tidak bisa menyentuh milikmu"
                                                b "Baik jika Anda menyentuh milik saya, Anda harus mengurusnya"
                                                s "Same here"
                                                s "Dan Anda menyentuh dulu, jadi Anda lebih baik menyelesaikan apa yang Anda mulai"
                                                jump sboobjob
                                            else:
                                                "Meningkatkan hubungan dengan 300 dan korupsi menjadi 30"
                                                pass
                                        else:





                                            scene slunch15hr with dissolve
                                            s "Hah!"
                                            scene slunch18hr with hpunch
                                            s "Pervert"
                                            b "Aduh!"
                                            b "Dia membentak"
                                            scene broom_day with fade
                                            "..."
                                            call screen gnav
                                    "Tidak perlu":

                                        pass

                                scene slunch11hr with fade
                                s "Terima kasih"
                                s "Untuk mencuci piring"
                                b "Lihat ya!"
                                scene broom_day with fade
                                "..."
                                call screen gnav
                    "Bantu dia":







                        b "Ok"
                        scene slunch10 with fade
                        show screen srelup
                        "..."
                        $ srel += 2
                        b "Done"
                        hide screen srelup
                        scene slunch11 with dissolve
                        s "Terima kasih"
                        b "Lihat ya!"
                        scene broom_day with fade
                        "..."
                        call screen gnav
    else:






        scene lunch with fade
        m "Sit [bname]"
        scene lunch1 with fade
        "..."
        menu:
            "Apa yang salah?":
                b "Apa yang salah?"
                scene lunch2 with dissolve
                m "Mengapa Anda tidak makan?"
                b "Saya!"
                pass
            "Bicaralah dengan [mname]":

                scene lunch3 with dissolve
                b "Bagaimana studi Anda [mname]?"
                scene lunch4 with dissolve
                s "Semuanya baik -baik saja"
                menu:
                    "Beri tahu saya jika Anda membutuhkan bantuan":
                        s "Saya akan"
                        pass
                    "Bagus":

                        b "Bagus"
                        scene lunch3 with dissolve
                        "..."
                        pass


            "Mata berkeliaran" if wk>=3:
                b "{/i}(Hmm){i}"
                b "{/i} (kiri atau kanan?) {i}"
                menu:
                    "Benar":
                        scene lunch_m_peek with dissolve
                        "..."
                        m "[bname]!"
                        scene lunch_m_s with dissolve
                        b "Yes"
                        pass
                    "Kiri":
                        scene lunch_s_peek with dissolve
                        "..."
                        m "[bname]!"
                        scene lunch_m_s with dissolve
                        b "Ya?"
                        pass

                scene lunch2 with dissolve
                m "Mengapa Anda tidak makan?"
                b "Saya!"
                pass


        if wk>=2:
            scene lunch6 with fade
            $ smoneym = 1
            if persistent.patch_enabled:
                s "Mama?"
                pass
            else:
                s "Madam"
                pass
            if smobilegiven == 1:
                pass
            else:
                m "Apa?"
                s "Tentang ponsel saya"
                s "Bisakah saya membeli yang baru?"
                m "[mname] Saya tidak punya uang untuk telepon!"
                scene lunch7 with dissolve
                s "Tetapi..."
                s "Baterai semakin habis"
                m "Saya bilang tidak"
        else:
            pass
        scene lunch1 with dissolve
        m "Itu waktu makan, bukan waktu bicara"
        b "OK"
        scene lunch5 with fade
        if persistent.patch_enabled:
            b "{/i} Terima kasih atas makan siang ibu {i}"
            pass
        else:
            b "{/i} Terima kasih untuk makan siang ma \ 'am {i}"
            pass
        if workrequest ==3:
            menu:
                "Apakah Anda membutuhkan bantuan dengan hidangan?":
                    scene lunch8 with fade
                    m "Anda baik"
                    scene lunch9 with fade
                    "..."
                    m "Terima kasih [bname]"
                    show screen mrelup
                    $ mrel += 2
                    b "It's ok"
                    hide screen mrelup
                    m "Saya harus pergi, saya punya janji kuku"
                    if mnailpolish == 1:
                        b "Keren Anda memutuskan untuk melakukannya?"
                        m "Yes"
                        menu:
                            "Bisakah aku ikut denganmu?":
                                m "Tidak dalam versi ini"
                                b "Ok"
                                pass
                            "Melanjutkan":

                                pass
                    else:
                        b "Keren, jangan khawatir"
                        pass

                    scene hall_d with fade
                    b "{/i} (kuku, janji!) {i}"
                    b "{/i} (hmm, mari kita coba cari tahu) {i}"
                    menu:
                        "Pergi ke jendela":
                            pass
                        "Ikuti dia" if elaine_convince == 4:
                            jump mgettingreadyfornails
                    scene mstairs with fade
                    "..."
                    scene lunch_stairs_nail with dissolve
                    b "{/i} (berdandan ...) {i}"
                    scene lunch_stairs_nail3 with dissolve
                    b "{/i}(Hmmm){i}"
                    if mrel >=200 and elaine_convince == 4:
                        scene lunch_stairs_nail3a with dissolve
                        m "{/i} (hmmm, ada seseorang di jendela) {i}"
                        m "{/i} (Mungkinkah itu neighbors boy) {i}"
                        m "{/i} (Saya akan melaporkannya ke polisi) {i}"
                        scene lunch_stairs_nail4a with dissolve
                        m "{/i} (atau tidak ...) {i}"
                        m "{/i} (hmm, senang dikagumi) {i}"
                    else:
                        pass
                    scene lunch_stairs_nail1 with dissolve
                    b "{/i} (ini terlihat lebih dari janji kuku ...) {i}"
                    scene lunch_stairs_nail2 with dissolve
                    m "{/i} (akhirnya, sehari untuk diri saya sendiri) {i}"
                    m "{/i} (i \ 'll do kuku, laser) {i}"
                    m "{/i} (dan makan siang dengan Melinda) {i}"
                    "Hei kamu!"
                    scene mstairs3 with vpunch
                    "Saya akan menelepon polisi"
                    b "Sial, bukan apa yang Anda pikirkan!"
                    "Saya menelepon polisi sekarang!"
                    b "Damn"
                    b "{/i} (saya harus pergi) {i}"
                    scene hall_d with fade
                    b "{/i} (sialan, [sname] kiri) {i}"
                    b "Saya pikir saya harus pergi menemuinya"
                    b "Kami tidak membutuhkan skandal apa pun"
                    menu:
                        "Pergi menemuinya":
                            jump neighb
                        "Tidak perlu":
                            call screen gnav
                "Meninggalkan":


                    pass
        else:
            pass
        scene hall_d with fade
        b "{/i} (...) {i}"
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
