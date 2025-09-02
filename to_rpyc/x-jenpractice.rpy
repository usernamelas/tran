image mdnc:
    "mdnc00.jpg"
    pause 0.05
    "mdnc01.jpg"
    pause 0.05
    "mdnc02.jpg"
    pause 0.05
    "mdnc03.jpg"
    pause 0.05
    "mdnc04.jpg"
    pause 0.05
    "mdnc05.jpg"
    pause 0.05
    "mdnc06.jpg"
    pause 0.05
    "mdnc07.jpg"
    pause 0.05
    "mdnc08.jpg"
    pause 0.05
    "mdnc09.jpg"
    pause 0.05
    "mdnc10.jpg"
    pause 0.05
    "mdnc11.jpg"
    pause 0.05
    "mdnc12.jpg"
    pause 0.05
    "mdnc13.jpg"
    pause 0.05
    "mdnc14.jpg"
    pause 0.05
    "mdnc15.jpg"
    pause 0.05
    "mdnc16.jpg"
    pause 0.05
    "mdnc17.jpg"
    pause 0.05
    "mdnc18.jpg"
    pause 0.05
    "mdnc19.jpg"
    pause 0.05
    "mdnc20.jpg"
    pause 0.05
    "mdnc21.jpg"
    pause 0.05
    "mdnc22.jpg"
    pause 0.05
    "mdnc21.jpg"
    pause 0.05
    "mdnc20.jpg"
    pause 0.05
    "mdnc19.jpg"
    pause 0.05
    "mdnc18.jpg"
    pause 0.05
    "mdnc17.jpg"
    pause 0.05
    "mdnc16.jpg"
    pause 0.05
    "mdnc15.jpg"
    pause 0.05
    "mdnc14.jpg"
    pause 0.05
    "mdnc13.jpg"
    pause 0.05
    "mdnc12.jpg"
    pause 0.05
    "mdnc11.jpg"
    pause 0.05
    "mdnc10.jpg"
    pause 0.05
    "mdnc09.jpg"
    pause 0.05
    "mdnc08.jpg"
    pause 0.05
    "mdnc07.jpg"
    pause 0.05
    "mdnc06.jpg"
    pause 0.05
    "mdnc05.jpg"
    pause 0.05
    "mdnc04.jpg"
    pause 0.05
    "mdnc03.jpg"
    pause 0.05
    "mdnc02.jpg"
    pause 0.05
    "mdnc01.jpg"
    pause 0.05
    repeat


label jenpractice:
    m "Tunggu di sini, saya akan segera kembali"
    b "..."
    scene jbpractice with fade
    if mfuckedsober >=1:
        pass
    else:
        m "{i} (Saya harap saya tidak akan menyesal ini sepanjang hidup saya) {/i}"
        pass
    scene jbpractice1 with fade
    m "Apa yang sedang kamu lakukan?"
    s "Berencana memeriksa email saya ..."
    m "Saya muak dengan ini [sname]"
    m "Anda membumi selama satu jam"
    m "Saya ingin Anda tinggal di kamar Anda"
    m "Dan belajar selama satu jam"
    m "Hanya saat saya kembali dan periksa kemajuan Anda"
    m "Hanya dengan begitu, Anda bisa keluar, menyikat gigi dan pergi tidur"
    s "Tetapi"
    m "Tidak tapi"
    m "Atau saya akan mengunci pintu Anda dari luar"
    if sgrm >=1:
        menu:
            "[sname] akan tikus pada [bname]":
                $ sgrm += 1
                s "{i} (Saya perlu membuat [bname] membayar tindakannya) {/i}"
                s "Ok saya akan belajar, tapi ada sesuatu yang ingin saya katakan"
                scene jbpractice1r with dissolve
                m "Apa itu?"
                s "Suatu hari ..."
                m "Ya?!"
                s "Saya mendengar [bname] berbicara di telepon ..."
                m "Ayo, ludah!"
                if persistent.patch_enabled:
                    s "Tentangmu, untuk Ayah"
                    pass
                else:
                    s "Tentang Anda, ke Stewart"
                    pass
                scene jbpractice1r1 with dissolve
                m "Hmmm"
                s "{i} (keren, berhasil) {/i}"
                jump bgroundednight
            "Tidak perlu":


                pass
    else:
        pass
    scene black
    "..."
    scene jbpractice2 with fade
    b "{i} (Saya ingin tahu kemana [mname] pergi!) {/i}"
    if mfuckedsober >=1 and mrel >=300:
        scene jbpractice3a with fade
        b "Oh!"
        m "Lihat apa yang mereka berikan kepada kami untuk dipakai di tempat kerja"
        b "Bagus!"
        b "Biarkan saya melihat dari belakang"
        scene jbpractice4a with dissolve
        b "..."
        b "Ok"
        b "Apakah Anda menari dalam yang satu ini?"
        scene jbpractice3a with dissolve
        m "Tidak, hanya untuk menyajikan makanan"
        b "Ah dan bagaimana dengan saya?"
        b "Tidak akan menari?"
        m "No"
        m "Saya akan pergi berubah, menyiapkan segelas anggur untuk saya"
        if mnvylingerie ==1:
            $ mrel += 30
            b "Aku punya sesuatu untukmu"
            m "Apa itu?"
            b "Di sini, coba"
            $ mnvylingerie = 2
            scene jbpractice5a with fade
            m "..."
            b "Wow"
            scene jbpractice6a with dissolve
            m "Saya akan berubah lagi"
            b "Damn"
            pass
        else:


            pass

        scene jbpractice10 with fade
        m "..."
        scene jbpractice13 with dissolve
        b "Cheers"
        scene jbpractice14 with dissolve
        m "Cheers"
        scene jbpractice15 with dissolve
        b "{i} (aduh di kontol saya !!) {/i}"
        m "Anda tahu apa yang harus dilakukan"
        b "Hehe yes"
        m "Ini pekerjaan Anda mulai sekarang"
        b "Tidak masalah sama sekali"
        scene jbpractice16 with dissolve
        m "Yess itu itu"
        m "..."
        scene jbpractice16a with dissolve
        b "..."
        scene jbpractice17a with dissolve
        b "..."
        b "The glass"
        scene jbpractice18a with dissolve
        m "Huh"
        m "Saya akan memberi Anda pertunjukan dansa karena Anda melakukan pijat yang baik"
        scene jbpractice19 with dissolve
        "..."
        scene jbpractice20 with dissolve
        "..."
        scene mdfb with fade
        b "..."
        b "Oh yeah"
        "..."
        scene jbpractice20a with dissolve
        $ persistent.unlock_74 = True
        b "Saya tidak bisa lagi"
        scene jbpractice21a with dissolve
        m "..."
        scene jbpractice22a with dissolve
        m "Ah"
        scene jbpractice23a with dissolve
        m "Ugh"
        scene jbpractice24a with dissolve
        m "[bname] Ah"
        scene jbpractice25a with dissolve
        m "Anda menjadi bayi yang baik"
        scene jbpractice26a with dissolve
        b "Almost done"
        m "Tolong di mulutku"
        scene jbpractice27a with dissolve
        m "Ugh"
        scene jbpractice28a with dissolve
        b "Selamat malam"
        jump newdays
    else:


        pass
    scene jbpractice3 with dissolve
    b "Oh!"
    m "So [bname]"
    m "Apa pendapat Anda tentang pakaian ini"
    b "Ya itu o.k, bagus"
    scene jbpractice4 with dissolve
    m "Apakah itu menunjukkan terlalu banyak"
    b "{i} (oh sial, saya harus memiliki jawaban yang bagus) {/i}"
    b "Terlalu banyak dari apa?"
    scene jbpractice5 with dissolve
    m "Oh nevermind"
    if mrel >50:
        m "Aku akan kembali"
        m "{i} (Elaine benar) {/i}"
        m "{i} (dia tidak tahu apa -apa) {/i}"
        scene jbpractice2 with dissolve
        b "{i} (keren) {/i}"
        scene jbpractice6 with fade
        m "Bagaimana dengan ini?"
        b "Itu bagus juga"
        m "Hmm OK"
        m "Tidak ada masalah dengan itu?"
        scene jbpractice7 with dissolve
        m "Maksud saya, apakah boleh bagi seorang wanita untuk keluar seperti ini?"
        b "{i} (hehehe apa yang dia coba katakan!) {/i}"
        b "Ya ... jika dia suka mengapa tidak?"
        b "Saya tidak melihat sesuatu yang salah dengannya"
        if mrel >80:
            m "Aku akan kembali"
            b "{i} (keren) {/i}"
            scene jbpractice2 with dissolve
            "..."
            "..."
            scene jbpractice8 with fade
            m "{i}(Hmm){/i}"
            scene jbpractice2 with fade
            "..."
            b "{i} (apa yang membawanya begitu lama) {/i}"
            scene jbpractice9 with dissolve
            m "Bagaimana sekarang?"
            b "Ermm ya, itu sangat bagus"
            if mrel >=300:
                m "Aku akan kembali"
                b "{i} (keren ada sesuatu yang baru) {/i}"
                scene jbpractice2 with dissolve
                "..."
                scene jbpractice8 with fade
                m "{i}(Hmm){/i}"
                m "{i} (haruskah saya memakai ini?) {/i}"
                m "{i} (hmm saya serius tidak tahu) {/i}"
                m "{i} (mari kita coba sekilas dan lihat apa yang dia pikirkan) {/i}"
                m "{i} (Pokoknya cepat atau lambat saya harus memakainya untuk bekerja) {/i}"
                scene jbpractice2 with fade
                "..."
                b "{i} (apa yang membawanya begitu lama) {/i}"
                scene jbpractice9a with dissolve
                m "Menurut Anda apa ini?"
                b "{i} (apa ...) {/i}"
                b "Errm"
                b "Warna bagus"
                m "Ok"
                scene jbpractice10a with dissolve
                m "Saya akan berubah"
                b "Simpan, itu baik -baik saja"
                m "Tidak, saya tidak ingin tetap dalam hal ini"
                pass
            else:

                pass
            scene jbpractice10 with dissolve
            m "Apakah Anda ingin menonton TV?"
            scene jbpractice11 with dissolve
            m "Tapi tidak terlalu lama"
            menu:
                "Apakah Anda ingin minum?" if mrel >100:
                    m "Ya, segelas anggur"
                    scene jbpractice13 with fade
                    b "Saya punya satu untuk saya juga"
                    b "Jika itu oke"
                    scene jbpractice14 with dissolve
                    m "Cheers"
                    scene jbpractice15 with dissolve
                    b "{i} (aduh di kontol saya !!) {/i}"
                    m "Anda tahu apa yang harus dilakukan"
                    b "Hehe yes"
                    m "Ini pekerjaan Anda mulai sekarang"
                    b "Tidak masalah sama sekali"
                    scene jbpractice16 with dissolve
                    m "Yess itu itu"
                    m "..."
                    b "Apakah Anda ingin saya memijat punggung Anda?"
                    m "Tentu saja saya mau"
                    scene jbpractice17 with fade
                    m "..."
                    b "Apakah saya lebih baik?"
                    m "Yes amazing"
                    menu:
                        "Saya pikir lebih baik Anda menghapus bagian atas" if mrel >110:
                            b "Saya tidak akan harus membahas senar dan sebagainya"
                            m "Hmm"
                            m "{i} (apakah itu ide yang bagus [mname]) {/i}"
                            scene jbpractice18 with dissolve
                            m "{i} (saya tidak tahu) {/i}"
                            m "Berpaling di kepalamu"
                            b "{i}(Yeah right){/i}"
                            b "Ok"
                            scene jbpractice19 with dissolve
                            "..."
                            scene jbpractice20 with dissolve
                            "..."
                            scene jbpractice21 with fade
                            m "..."
                            scene jbpractice22 with dissolve
                            "..."
                            menu:
                                "Lakukan sesuatu":
                                    scene jbpractice23 with dissolve
                                    "..."
                                    scene jbpractice24 with dissolve
                                    "..."
                                    scene jbpractice25 with dissolve
                                    m "..."
                                    scene jbpractice26 with dissolve
                                    m "{i} (apakah dia hanya menyentuh payudara saya?) {/i}"
                                    m "Ermm"
                                    scene jbpractice27 with fade
                                    m "Saya akan pergi minum lagi"
                                    scene jbpractice28 with dissolve
                                    m "Continue"
                                    scene jbpractice29 with dissolve
                                    m "Yes yes"
                                    b "..."
                                    m "Jadikan lebih sulit"
                                    b "{i} (fuck!) {/i}"
                                    m "Ya Tuhan itu bagus"
                                    b "Saya mencoba yang terbaik"
                                    m "Saya pikir itu sudah cukup, mari kita lihat film apa yang ada di TV"
                                    b "Ya kedengarannya ide yang bagus"
                                    b "Saya akan menemukan sesuatu"
                                    b "{i} (Saya pikir saya akan menonton payudara Anda sebagai gantinya) {/i}"
                                    scene jbpractice33 with fade
                                    b "{i} (Saya harap dia tidak akan kehilangan itu) {/i}"
                                    m "..."
                                    scene jbpractice34 with dissolve
                                    b "{i} (masih keren!) {/i}"
                                    m "Hah!"
                                    b "Apa?"
                                    scene jbpractice35 with dissolve
                                    m "Saya akan mendapatkan segelas anggur lagi"
                                    b "Yeah sure"
                                    b "{i} (dia tidak berpikir) {/i}"
                                    scene jbpractice33 with fade
                                    m "Itu adalah segelas anggur yang enak"
                                    b "Ya, itu"
                                    m "..."
                                    b "{i} (sialan panas, saya harap dia menikmatinya sama seperti yang saya lakukan) {/i}"
                                    menu:
                                        "Tanyakan tentang pekerjaannya" if elaine_convince == 4:
                                            b "{i} (ya itu ide yang bagus jadi dia tidak akan memperhatikan) {/i}"
                                            b "{i} (dan aku mengalihkan perhatian diriku, mungkin boner akan pergi) {/i}"
                                            b "Jadi bagaimana cara kerja?"
                                            m "Fucked up"
                                            b "{i} (wow, saya tidak pernah mendengarnya bersumpah) {/i}"
                                            b "Mengapa?"
                                            m "Itu semua mentalitas kepiting terpelintir"
                                            b "Mentalitas apa!?"
                                            m "Belum lagi tarian strip dan segala macam hal jelek yang terjadi di sana"
                                            b "Oh wow, apakah kamu menari?"
                                            m "Saya tidak, tidak pernah"
                                            b "Aku tidak pernah melihatmu menari"
                                            m "Maksud saya, saya tidak akan pernah menari di sana, di tempat kerja"
                                            b "Bagaimana dengan sekarang?"
                                            b "Maukah Anda melakukannya untuk saya?"
                                            scene jbpractice35 with dissolve
                                            m "Apa?"
                                            b "Ermm aku tidak bersungguh -sungguh"
                                            if mrel >=200:
                                                scene jbpractice66 with dissolve
                                                m "Hahahaha"
                                                m "Anda takut!"
                                                m "Duduk dan nikmati"
                                                $ dancerepeat += 1
                                                scene mdnc
                                                $ persistent.unlock_2 = True
                                                "..."
                                                m "Wooh!"
                                                b "Bagus"
                                                m "Yeah"
                                                b "Woah berhati -hatilah Anda akan jatuh"
                                                if dancerepeat <=5:
                                                    m "Saya kira sudah waktunya tidur"
                                                    scene jbpractice30 with fade
                                                    m "Terima kasih sayang"
                                                    b "Jangan lupakan gaun tidurmu"
                                                    scene jbpractice45 with dissolve
                                                    m "Terima kasih telah mengingatkan saya"
                                                    if mrel >= 200:
                                                        jump mnightshow
                                                    elif mnightie == 2:
                                                        jump mnightshow
                                                    else:
                                                        pass
                                                    scene hall_n with fade
                                                    b "{i} (lebih baik saya melanjutkan di kamar saya) {/i}"
                                                    scene black
                                                    "SEMENTARA ITU"
                                                    scene jbpractice31 with fade
                                                    s "I'm studying"
                                                    m "Saya bisa melihatnya"
                                                    m "Setelah selesai, Anda bisa keluar dari kamar Anda"
                                                    s "Thanks"
                                                    jump bs_afterjmassage
                                                else:

                                                    scene jbpractice67 with hpunch
                                                    m "Ahh"
                                                    scene jbpractice68 with dissolve
                                                    m "Terima kasih [bname]"
                                                    scene jbpractice69 with dissolve
                                                    "..."
                                                    m "Tolong bawa saya ke kamar saya"
                                                    b "{i} (dia tidak membingungkan saya dengan steve) {/i}"
                                                    menu:
                                                        "Sentuh dia di sana":
                                                            scene jbpractice67 with dissolve
                                                            "..."
                                                            scene jbpractice67a with dissolve
                                                            m "..."
                                                            scene jbpractice68 with dissolve
                                                            m "Apa?"
                                                            $ msex = 1
                                                            b "Saya pikir Anda harus melepas pantat Anda"

                                                            m "Hmm"
                                                            m "Tolong bawa saya ke kamar saya"
                                                            pass
                                                        "Biarkan sampai dia lebih mabuk":

                                                            b "Ayo biarkan duduk dan minum lagi"
                                                            jump jenpracticextend
                                                        "Melanjutkan":

                                                            pass
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
                                                            if mrel >= 450 and msex >=1:
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
                                                                        menu:
                                                                            "Lanjutkan menidurinya":
                                                                                if mrel>=550:
                                                                                    scene jbpractice83y with dissolve
                                                                                    m "Ahh"
                                                                                    scene jbpractice84y with dissolve
                                                                                    "..."
                                                                                    scene jbpractice85y with dissolve
                                                                                    m "Ini Stewart yang menyakitkan! Berhenti!"
                                                                                    pass
                                                                                else:
                                                                                    scene jbpractice82y with dissolve
                                                                                    m "Aku bilang berhenti!"
                                                                                    pass
                                                                            "Berhenti":
                                                                                pass
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
                                                                b "{i} (lebih baik saya tidak mengambil risiko) {/i}"
                                                                "Naikkan poin Anda menjadi 450"
                                                                pass
                                                        "Jangan":


                                                            pass
                                                    scene black
                                                    "..."
                                                    scene jbpractice73 with fade
                                                    m "Hah!"
                                                    m "[bname] Apa yang kamu lakukan di sini?"
                                                    b "Anda menyuruh saya tidur"
                                                    m "Tolong pergi ke kamar Anda sekarang"
                                                    b "Ok"
                                                    scene jbpractice74 with dissolve
                                                    "..."
                                                    jump newdays
                                            else:



                                                m "Lebih baik Anda tidak bermaksud"
                                                b "Ok"
                                                m "Selamat malam"
                                                b "{i}(Damn){/i}"
                                                scene hall_n with fade
                                                b "{i} (lebih baik saya melanjutkan di kamar saya) {/i}"
                                                scene black
                                                "SEMENTARA ITU"
                                                scene jbpractice31 with fade
                                                s "I'm studying"
                                                m "Saya bisa melihatnya"
                                                m "Setelah selesai, Anda bisa keluar dari kamar Anda"
                                                s "Thanks"
                                                jump bs_afterjmassage
                                        "Sembunyikan pangkal paha Anda dengan bantal":




                                            scene jbpractice41 with dissolve
                                            b "{i} (ini jauh lebih baik, dia tidak bisa melihat tonjolan saya) {/i}"
                                            m "Sepertinya film yang bagus"
                                            b "Ya, terlalu buruk itu hampir di akhir"
                                            m "Apakah itu?"
                                            b "Saya kira demikian"
                                            b "Saya akan mencoba menemukan sesuatu yang lebih baik"
                                            scene jbpractice42 with dissolve
                                            b "iya ini"
                                            scene jbpractice43 with dissolve
                                            b "{i} (film apa yang panas) {/i}"
                                            menu:
                                                "Lakukan itu":
                                                    scene jbpractice46 with dissolve
                                                    "..."
                                                    scene jbpractice47 with hpunch
                                                    b "Hah!"
                                                    m "Di mana pijatan saya"
                                                    b "{i} (keren, dia mabuk) {/i}"
                                                    scene jbpractice48 with dissolve
                                                    m "Ya!"
                                                    scene jbpractice49 with dissolve
                                                    b "{i} (sekarang adalah waktunya) {/i}"
                                                    scene jbpractice50 with dissolve
                                                    "..."
                                                    scene jbpractice51 with dissolve
                                                    m "Ya!!"
                                                    b "{i} (ah fuck saya bisa \ 't lagi) {/i}"
                                                    if mrel >=200:
                                                        scene jbpractice49 with dissolve
                                                        m "Mengapa Anda berhenti?"
                                                        scene jbpractice55
                                                        m "Berikan padaku"
                                                        b "Aku akan ..."
                                                        scene jbpractice56 with hpunch
                                                        b "Woah meja"
                                                        m "Blaargh"
                                                        b "Apa -apaan itu, bau itu"
                                                        scene jbpractice57 with dissolve
                                                        m "Maaf steve saya tidak merasa sehat"
                                                        m "Saya akan pergi ke toilet"
                                                        b "Aku akan ikut denganmu"
                                                        b "{i} (steve siapa) {/i}"
                                                        scene jbpractice58 with fade
                                                        b "Apa yang salah?"
                                                        m "Saya memiliki terlalu banyak minuman"
                                                        m "Tinggalkan saja! Saya ingin muntah"
                                                        b "{i} (i \ 'll call [sname]) {/i}"
                                                        b "{i} (Saya harap dia tidak akan mati) {/i}"
                                                        scene jbpractice59 with fade
                                                        b "[sname] Datang cepat"
                                                        s "Apa yang salah"
                                                        scene jbpractice60 with fade
                                                        s "Apa yang telah terjadi?"
                                                        b "Saya tidak tahu dia mulai muntah"
                                                        s "Ok tinggalkan kami sendiri"
                                                        scene black
                                                        "..."
                                                        scene jbpractice61 with fade
                                                        m "[sname] Dapatkan aku gaun tidurku, itu di aula"
                                                        s "Ok"
                                                        s "{i} (Tunggu sebentar, Kenapa Nighttie is the Hall) {/i}"
                                                        s "{i} (dan kenapa dia telanjang di depan [bname]) {/i}"
                                                        scene black
                                                        "..."
                                                        scene jbpractice62 with fade
                                                        m "Bantu saya melepas celana dalam"
                                                        scene jbpractice63 with dissolve
                                                        s "Done"
                                                        $ sm_rel = 1
                                                        scene jbpractice64 with dissolve
                                                        s "Hmm"
                                                        s "{i} (dia super cantik) {/i}"
                                                        scene jbpractice65 with fade
                                                        m "Ya saya akan baik -baik saja"
                                                        m "Biarkan aku tidur"
                                                        s "Selamat malam"
                                                        jump bs_afterjmassage
                                                    else:


                                                        "Naikkan poin Anda"
                                                        pass
                                                    scene jbpractice52 with hpunch
                                                    m "Kenapa kamu berhenti!?"
                                                    b "Ermm"
                                                    b "SAYA..."
                                                    scene jbpractice53 with dissolve
                                                    m "Lelah?"
                                                    b "Ya sedikit"
                                                    b "Saya kira saya akan tidur"
                                                    scene jbpractice54 with fade
                                                    "..."
                                                    scene black
                                                    "..."
                                                    jump bs_afterjmassage
                                                "Lanjutkan menonton tanpa masturbasi **":

                                                    scene jbpractice44 with fade
                                                    m "{i} (oh ... minuman ini membuatku berhalusinasi) {/i}"
                                                    m "Saya kira sudah waktunya tidur"
                                                    scene jbpractice30 with fade
                                                    m "Terima kasih sayang"
                                                    b "Jangan lupakan gaun tidurmu"
                                                    scene jbpractice45 with dissolve
                                                    m "Terima kasih telah mengingatkan saya"
                                                    if mrel >= 200:
                                                        jump mnightshow
                                                    elif mnightie == 2:
                                                        jump mnightshow
                                                    else:
                                                        pass
                                                    scene hall_n with fade
                                                    b "{i} (lebih baik saya melanjutkan di kamar saya) {/i}"
                                                    scene black
                                                    "SEMENTARA ITU"
                                                    scene jbpractice31 with fade
                                                    s "I'm studying"
                                                    m "Saya bisa melihatnya"
                                                    m "Setelah selesai, Anda bisa keluar dari kamar Anda"
                                                    s "Thanks"
                                                    jump bs_afterjmassage
                                        "Jangan":

                                            b "{i} (sialan tonjolan ini) {/i}"
                                            scene jbpractice37 with dissolve
                                            m "Sepertinya film yang bagus"
                                            b "Ermmm"
                                            b "Yes"
                                            b "Apakah Anda ingin minum?"
                                            m "Yes please"
                                            b "{i} (hahaha keren, dia benar -benar mabuk) {/i}"
                                            scene jbpractice38 with dissolve
                                            m "Tetapi..."
                                            m "Saya sudah punya satu"
                                            if mrel >= 300:
                                                b "Nevermind, aku akan memberimu satu"
                                                m "Yes please"
                                                jump jenpracticextend
                                            else:

                                                pass
                                            b "Hahaha ya saya lupa, saya harus mabuk"
                                            m "Saya pikir itu cukup minuman untuk saya"
                                            scene jbpractice32 with dissolve
                                            b "{i} (sialan! Dia memperhatikannya) {/i}"
                                            scene jbpractice39 with fade
                                            b "{i} (mungkin saya harus mengubahnya) {/i}"
                                            "..."
                                            b "{i} (ya, saya pikir lebih baik mengubahnya) {/i}"
                                            "..."
                                            m "Selamat malam [bname]"
                                            scene jbpractice40 with dissolve
                                            "..."
                                            scene hall_n with fade
                                            b "{i} (lebih baik saya melanjutkan di kamar saya) {/i}"
                                            scene black
                                            "SEMENTARA ITU"
                                            scene jbpractice31 with fade
                                            s "I'm studying"
                                            m "Saya bisa melihatnya"
                                            m "Setelah selesai, Anda bisa keluar dari kamar Anda"
                                            s "Thanks"
                                            jump bs_afterjmassage

                                    scene jbpractice27 with dissolve
                                    m "Udah dulu ya"
                                    b "Jangan lupakan gaun tidurmu"
                                    if mrel >= 200:
                                        jump mnightshow
                                    elif mnightie == 2:
                                        jump mnightshow
                                    else:
                                        pass
                                    scene hall_n with fade
                                    b "{i} (lebih baik saya melanjutkan di kamar saya) {/i}"
                                    scene black
                                    "SEMENTARA ITU"
                                    scene jbpractice31 with fade
                                    s "I'm studying"
                                    m "Saya bisa melihatnya"
                                    m "Setelah selesai, Anda bisa keluar dari kamar Anda"
                                    s "Thanks"
                                    jump bs_afterjmassage
                                "Melanjutkan":


                                    scene jbpractice23 with dissolve
                                    m "Saya kira itu cukup"
                                    m "Selamat malam sayang"
                                    b "Selamat malam"
                                    scene hall_n with fade
                                    b "{i} (i \ 'D lebih baik tidur) {/i}"
                                    jump bs_afterjmassage
                        "Melanjutkan":


                            m "Saya kira itu cukup"
                            m "Selamat malam sayang"
                            b "Selamat malam"
                            scene hall_n with fade
                            b "{i} (i \ 'D lebih baik tidur) {/i}"
                            jump bs_afterjmassage
                "Melanjutkan":

                    m "Saya kira itu"
                    pass

            scene jbpractice12 with fade
            m "Selamat malam sayang"
            scene jbpractice12_1 with dissolve
            b "Selamat malam"
            scene hall_n with fade
            b "{i} (i \ 'D lebih baik tidur) {/i}"
            jump newdays
        else:
            m "All right"
            m "Selamat malam"
            b "Oh OK"
            scene hall_n with fade
            b "{i} (i \ 'D lebih baik tidur) {/i}"
            b "{i} (mungkin saya melakukan sesuatu yang salah?!) {/i}"
            scene black
            "Naikkan poin Anda lebih tinggi dari 80"
            jump newdays
    else:

        m "Selamat malam"
        b "Oh OK"
        scene hall_n with fade
        b "{i} (i \ 'D lebih baik tidur) {/i}"
        b "{i} (mungkin saya melakukan sesuatu yang salah?!) {/i}"
        scene black
        "Naikkan poin Anda lebih tinggi dari 50"
        jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc