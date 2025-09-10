label nudebeach_jenelaine:
    $ Hour += 1
    scene nbm_e0 with fade
    $ mvisitnudebeach += 1
    m "Apa?"
    e "Apakah Anda akan melakukannya atau tidak?"
    if mrel >=300:
        m "Hmm"
        m "Not today"
        scene nbm_e01 with dissolve
        e "Ayo!"
    else:
        m "No way"
        m "Dan Anda bilang Anda akan berperilaku benar!?"
        scene nbm_e01 with dissolve
        e "Mau mu"
        pass

    "..."
    if mvisitnudebeach >=5 and mrel >=400 and mcorr >= 20:
        scene nbm_e with fade
        e "Apa yang salah dengan Anda [mname]"
        m "Apa?"
        e "Anda terlihat aneh di bikini"
        e "Lihat sekeliling, semua orang telanjang"
        m "Saya bisa Elaine"
        scene nbm_e4 with dissolve
        e "Percayalah tidak ada yang peduli padamu"
        m "Hmm"
        scene nbm_e1 with fade
        b "{i} (keren) {/i}"
        scene nbm_e5 with dissolve
        e "Tidak apa -apa, jangan malu"
        b "Let's swim"
        scene nbm_e6 with fade
        "..."
        scene nbm_e7 with dissolve
        e "Tolong hentikan"
        e "Anda meminta perhatian dengan persembunyian ini"
        if mfuckedsober >= 1:
            "Dia berbisik kepada Elaine"
            m "Saya tidak hanya malu"
            m "Saya khawatir dia memiliki masalah ini lagi"
            e "Masalah mana?"
            m "Priapism"
            e "Oh berhenti mengada -ada"
            m "Dia ..."
            m "Oh aku akan memberitahumu nanti"
            m "Berjanjilah padaku kamu tinggal di sini"
            m "Saya perlu berbicara dengannya secara pribadi"
            e "All right"
            scene nbm_e8 with dissolve
            m "[bname] Honey Come With Me, saya perlu berbicara dengan Anda"
            scene nbmea with fade
            b "Kemana kita akan pergi?"
            m "Katakan dengan jujur"
            m "Kamu tidak apa apa?"
            scene nbmea1 with dissolve
            m "Atau Anda merasa sakit?"
            b "Tidak, saya ok"
            if mcorr >= 30:
                menu:
                    "Cobalah keberuntungan Anda":
                        scene nbm_e52 with dissolve
                        m "Saya tahu itu tidak tepat tapi ..."
                        m "Saya hanya ingin membantu Anda"
                        menu:
                            "cium dia":
                                scene nbm_e54 with dissolve
                                m "Itu hanya sampai hal ini hilang"
                                scene nbmm
                                m "..."
                                "..."
                                scene nbm_e55 with dissolve
                                "..."
                                pass
                            "Biarkan dia mengurusnya":

                                scene nbm_e53
                                b "Aku tahu"
                                pass
                                scene nbm_e57 with dissolve
                                "..."
                                scene nbm_e56 with dissolve
                                "..."
                                scene nbm_e58 with hpunch
                                m "Ughh"
                                scene nbm_e59 with dissolve
                                b "{i} (dia mengambil semuanya !!) {/i}"
                                scene nbm_e60 with dissolve
                                m "Ugh"
                                pass
                        scene nbm_e61 with dissolve
                        m "Jangan mendorongnya di mulutku seperti ini [bname]"
                        b "Ouch"
                        scene nbm_e62 with dissolve
                        m "Ah"
                        scene nbpd
                        m "Ahhh"
                        b "Grrr"
                        m "Ah"
                        "..."
                        scene nbm_e64 with dissolve
                        "..."
                        scene nbm_e66 with fade
                        m "Tidak ada yang pernah tahu tentang ini"
                        b "Ok"
                        m "Mari kita kembali"
                        if melsw == 7:
                            $ melsw = 8
                            scene nbm_e66a with fade
                            "..."
                            pass
                        else:
                            pass
                    "Melanjutkan":

                        m "Aku tidak percaya padamu"
                        m "Dapatkan pantat Anda di sini"
                        scene nbmea2 with dissolve
                        b "Mmm"
                        scene nbmea3 with hpunch
                        b "Ahh"
                        scene nbmea4 with dissolve
                        "..."
                        scene nbmea5 with vpunch
                        m "Hey"
                        scene nbmea6 with dissolve
                        m "[bname] Tidak di tengah pantai"
                        b "Kami berada di belakang di belakang pepohonan"
                        scene nbmea7 with vpunch
                        m "Ahh lambat"
                        scene nbmea8 with dissolve
                        "..."
                        scene nbmea9 with dissolve
                        m "[bname]"
                        scene nbmea10 with dissolve
                        m "Don't cum"
                        scene nbmea9 with dissolve
                        "..."
                        scene nbmea11 with dissolve
                        m "Yes honey"
                        scene nbmea12 with dissolve
                        m "Ya!"
                        scene nbmea13 with dissolve
                        b "I'm close"
                        m "Cum di mulutku [bname]"
                        scene nbmea14 with fade
                        "..."
                        scene nbmea15 with dissolve
                        b "Ahh"
                        scene nbmea16 with dissolve
                        b "Sungguh!"
                        scene nbmea1 with fade
                        m "Mari kita kembali ke Elaine"
                        pass
            else:

                m "Senang mengetahui"
                m "Mari kita lanjutkan dengan Elaine"
                scene black
                "Meningkatkan korupsinya menjadi 30"
                pass
        else:


            pass
        scene nbm_e8 with fade
        b "{i} (pantat bagus) {/i}"
        m "Oh ombaknya!"
        scene nbm_e9 with dissolve
        m "{i} (terbakar di sana) {/i}"
        b "{i} (oh fuck, dia berbalik seolah -olah dia tahu apa yang saya pikirkan) {/i}"
        e "Percayalah [mname], tidak ada orang di sini yang peduli, mereka telah melihat lebih dari Anda"
        m "{i} (setidaknya sekarang dia tidak bisa melihat banyak) {/i}"
        m "Ini bukan tentang orang, itu ..."
        e "Tentang apa?"
        m "Nothing"
        b "{i} (saya bisa \ 't lagi) {/i}"
        scene nbm_e11 with dissolve
        e "{i} (apa yang dia lakukan) {/i}"
        e "{i} (saya harus mengalihkan perhatiannya) {/i}"
        scene nbm_e43 with dissolve
        e "[bname]"
        e "Payudara mana yang menurut Anda lebih indah"
        b "Hah!"
        scene nbm_e44 with dissolve
        m "..."
        e "Ayo tidak ada yang perlu dipermalukan"
        $ persistent.unlock_28 = True
        menu:
            "[mname]":
                $ mnameboobs = 1
                b "[mname]"
                scene nbm_e45 with dissolve
                "..."
                pass
            "Milikmu":

                $ elaineboobs = 1
                b "Milikmu"
                scene nbm_e46 with dissolve
                "..."
                pass
        e "Baiklah, [bname] lebih baik Anda berenang, saya perlu berbicara dengan [mname]"
        e "In private"
        b "Ok"
        b "Tapi lebih baik jika seseorang datang dan bergabung dengan saya"
        e "Go i \ 'll ikuti Anda"
        scene nbm_e15 with dissolve
        e "Berhenti menutupi, Anda membodohi diri sendiri"
        m "Saya tidak menyukainya"
        scene nbm_e16 with dissolve
        e "Percayalah padaku berdiri"
        m "ELAINE! Saya tidak tahu apakah saya dicukur atau tidak"
        e "Hanya berdiri aku akan memeriksanya, pandangan sekilas"
        scene nbm_e17 with dissolve
        e "Hapus, biarkan saya melihat"
        scene nbm_e18 with dissolve
        "..."
        scene nbm_e19 with dissolve
        e "It's nothing"
        e "Saya akan berenang"
        e "Saya harap Anda berubah pikiran saat saya kembali"
        scene nbm_e20 with fade
        e "Apa yang salah denganmu?"
        b "Aku sangat terangsang, tapi aku tidak bisa cum"
        e "Ya Tuhan, izinkan saya membantu Anda di bawah air"
        scene nbm_e21 with dissolve
        e "Mengawasi dia"
        b "Yes"
        e "Apakah kamu dekat?"
        b "Tidak, itu tidak akan berhasil"
        scene nbm_e22 with dissolve
        e "Mungkin itu karena di bawah air"
        scene nbm_e23 with dissolve
        e "Pergi ke sana di belakang pepohonan dan saya akan mengikuti Anda"
        b "Ok"
        scene nbm_e24 with dissolve
        "..."
        e "Apakah kamu dekat?"
        b "No"
        e "Pikirkan sesuatu yang seksi"
        e "Cobalah untuk merasakan pantat saya"
        scene nbm_e25 with dissolve
        "..."
        e "Sepertinya tidak berhasil"
        scene nbm_e24 with dissolve
        e "Hmmm"
        e "Cobalah untuk melihat gadis yang lebih muda mungkin berhasil"
        b "Tidak, saya tidak berpikir begitu"
        e "Hmmm"
        e "Bagaimana dengan [mname]"
        e "Lihat betapa indahnya pantatnya?"
        scene nbm_e26 with dissolve
        "..."
        b "Yes"
        scene nbm_e27 with hpunch
        b "Ahhh"
        scene nbm_e28 with fade
        e "Jadi itu nyata"
        b "Hah!"
        e "Penyimpangan Anda"
        b "Yes"
        e "Dan apakah itu bekerja dengan [sname] juga?"
        b "Tidak, saya hanya bisa memikirkan [sname]"
        b "Itu tidak cukup"
        e "Oke, saya harus kembali padanya"
        scene black
        "SEMENTARA ITU"
        scene nbm_e29 with fade
        ml "Pantai Daniel apa ini?"
        dn "Nude"
        ml "Saya tidak ingin berada di sini, ayo pergi"
        dn "Tetapi..."
        dn "Tidak ada yang mengenal kami di sini"
        ml "Saya bilang mari kita pergi"
        scene nbm_e16 with fade
        e "Jadi, apakah Anda berubah pikiran?"
        m "Aku tidak tahu"
        e "Ayo"
        e "Beralihlah ke pepohonan dan coba, toh tidak ada orang di sini"
        scene nbm_e30 with dissolve
        e "Melihat! mudah"
        m "Not so"
        e "Lihatlah betapa gemuknya wanita ini di sana"
        $ persistent.unlock_15 = True
        e "Dan dia tidak peduli"
        scene nbm_e31 with dissolve
        m "Ya, tapi dia masih muda"
        e "Oh wow, seolah -olah Anda berusia 60 tahun"
        scene nbm_e30 with dissolve
        e "Demi Tuhan berhenti menjadi pemalu"
        e "Jangan terlalu memikirkannya"
        m "Dimana [bname]"
        e "Swimming"
        scene nbm_e32 with dissolve
        e "Lihat itu tidak sulit, sekarang Anda perlu mengambil tangan itu"
        scene nbm_e33 with dissolve
        m "..."
        e "Jangan khawatir dia tidak akan datang"
        e "Remove it"
        scene nbm_e34 with dissolve
        "..."
        e "Lihat, itu tidak sulit"
        e "Pokoknya di sini [bname] kembali"
        e "Let's go"
        scene nbmereturn with fade
        "..."
        jump nudebeach_jenelainereturn



    elif mvisitnudebeach >=3 and mrel >=300:
        scene nbm_e with fade
        e "Apa yang salah dengan Anda [mname]"
        m "Apa?"
        e "Anda terlihat aneh di bikini"
        e "Lihat sekeliling, semua orang telanjang"
        m "Saya bisa Elaine"
        scene nbm_e4 with dissolve
        e "Percayalah tidak ada yang peduli padamu"
        m "Hmm"
        scene nbm_e1 with fade
        b "{i} (keren) {/i}"
        scene nbm_e5 with dissolve
        e "Tidak apa -apa, jangan malu"
        b "Let's swim"
        scene nbm_e6 with fade
        "..."
        scene nbm_e7 with dissolve
        e "Tolong hentikan"
        e "Anda meminta perhatian dengan persembunyian ini"
        scene nbm_e8 with dissolve
        b "{i} (pantat bagus) {/i}"
        m "Oh ombaknya!"
        scene nbm_e9 with dissolve
        m "{i} (terbakar di sana) {/i}"
        b "{i} (oh fuck, dia berbalik seolah -olah dia tahu apa yang saya pikirkan) {/i}"
        e "Percayalah [mname], tidak ada orang di sini yang peduli, mereka telah melihat lebih dari Anda"
        m "{i} (setidaknya sekarang dia tidak bisa melihat banyak) {/i}"
        m "Ini bukan tentang orang, itu ..."
        e "Tentang apa?"
        m "Nothing"
        b "{i} (saya bisa \ 't lagi) {/i}"
        scene nbm_e11 with dissolve
        e "{i} (apa yang dia lakukan) {/i}"
        menu:
            "Masturbasi":
                scene nbm_e12 with dissolve
                "..."
                scene nbm_e13 with dissolve
                e "{i} (apakah dia bodoh atau apa?!) {/i}"
                e "{i} ([mname] mungkin memperhatikannya) {/i}"
                m "{i} (Saya tidak ingat jika saya mencukurnya dengan sempurna atau tidak?) {/i}"
                b "{i} (fuck i can \ \ 't cum) {/i}"
                scene nbm_e12 with dissolve
                "..."
                $ persistent.unlock_4 = True
                scene nbm_e13 with dissolve
                e "{i}(Oh God){/i}"
                e "[bname] Lebih baik Anda berenang, saya perlu berbicara dengan [mname]"
                e "In private"
                b "Ok"
                b "Tapi lebih baik jika seseorang datang dan bergabung dengan saya"
                e "Go i \ 'll ikuti Anda"
                scene nbm_e15 with dissolve
                e "Berhenti menutupi, Anda membodohi diri sendiri"
                m "Saya tidak menyukainya"
                scene nbm_e16 with dissolve
                e "Percayalah padaku berdiri"
                m "ELAINE! Saya tidak tahu apakah saya dicukur atau tidak"
                e "Hanya berdiri aku akan memeriksanya, pandangan sekilas"
                if mvisitnudebeach >=4:
                    scene nbm_e17 with dissolve
                    e "Hapus, biarkan saya melihat"
                    scene nbm_e18 with dissolve
                    "..."
                    scene nbm_e19 with dissolve
                    e "It's nothing"
                    e "Saya akan berenang"
                    e "Saya harap Anda berubah pikiran saat saya kembali"
                    scene nbm_e20 with fade
                    e "Apa yang salah denganmu?"
                    b "Aku sangat terangsang, tapi aku tidak bisa cum"
                    e "Ya Tuhan, izinkan saya membantu Anda di bawah air"
                    scene nbm_e21 with dissolve
                    e "Mengawasi dia"
                    b "Yes"
                    e "Apakah kamu dekat?"
                    b "Tidak, itu tidak akan berhasil"
                    if mvisitnudebeach >=5:
                        scene nbm_e22 with dissolve
                        e "Mungkin itu karena di bawah air"
                        scene nbm_e23 with dissolve
                        e "Pergi ke sana di belakang pepohonan dan saya akan mengikuti Anda"
                        b "Ok"
                        scene nbm_e24 with dissolve
                        "..."
                        e "Apakah kamu dekat?"
                        b "No"
                        e "Pikirkan sesuatu yang seksi"
                        e "Cobalah untuk merasakan pantat saya"
                        scene nbm_e25 with dissolve
                        "..."
                        e "Sepertinya tidak berhasil"
                        scene nbm_e24 with dissolve
                        e "Hmmm"
                        e "Cobalah untuk melihat gadis yang lebih muda mungkin berhasil"
                        b "Tidak, saya tidak berpikir begitu"
                        e "Hmmm"
                        e "Bagaimana dengan [mname]"
                        e "Lihat betapa indahnya pantatnya?"
                        scene nbm_e26 with dissolve
                        "..."
                        b "Yes"
                        scene nbm_e27 with hpunch
                        b "Ahhh"
                        scene nbm_e28 with fade
                        e "Jadi itu nyata"
                        b "Hah!"
                        e "Penyimpangan Anda"
                        b "Yes"
                        e "Dan apakah itu bekerja dengan [sname] juga?"
                        b "Tidak, saya hanya bisa memikirkan [sname]"
                        b "Itu tidak cukup"
                        e "Oke, saya harus kembali padanya"
                        if elaineshowsup >= 2 and elaineagain == 0:
                            scene black
                            "SEMENTARA ITU"
                            $ elaineagain = 1
                            scene nbm_e29 with fade
                            ml "Pantai Daniel apa ini?"
                            dn "Nude"
                            ml "Saya tidak ingin berada di sini, ayo pergi"
                            dn "Tetapi..."
                            dn "Tidak ada yang mengenal kami di sini"
                            ml "Saya bilang mari kita pergi"
                            pass

                        elif elaineshowsup >= 2 and elaineagain >= 3:
                            scene black
                            "SEMENTARA ITU"
                            scene nbm_e29c with fade
                            ml "Pantai Daniel apa ini?"
                            dn "Nude"
                            ml "Saya tidak ingin berada di sini, ayo pergi"
                            dn "Tetapi..."
                            dn "Tidak ada yang mengenal kami di sini"
                            ml "Saya bilang mari kita pergi"
                            if mrel >=350:
                                scene nbm_e16 with fade
                                e "Jadi, apakah Anda berubah pikiran?"
                                m "Aku tidak tahu"
                                e "Ayo"
                                e "Beralihlah ke pepohonan dan coba, toh tidak ada orang di sini"
                                scene nbm_e30 with dissolve
                                e "Melihat! mudah"
                                m "Not so"
                                e "Lihatlah betapa gemuknya wanita ini di sana"
                                $ persistent.unlock_15 = True
                                e "Dan dia tidak peduli"
                                scene nbm_e31 with dissolve
                                m "Ya, tapi dia masih muda"
                                e "Oh wow, seolah -olah Anda berusia 60 tahun"
                                scene nbm_e30 with dissolve
                                e "Demi Tuhan berhenti menjadi pemalu"
                                e "Jangan terlalu memikirkannya"
                                m "Dimana [bname]"
                                e "Swimming"
                                scene nbm_e32 with dissolve
                                e "Lihat itu tidak sulit, sekarang Anda perlu mengambil tangan itu"
                                scene nbm_e33 with dissolve
                                m "..."
                                e "Jangan khawatir dia tidak akan datang"
                                e "Remove it"
                                if mfuckedsober >= 1:
                                    m "Tidak, dia tidak ada di sana"
                                    e "Hapus sekarang, dia akan datang cepat atau lambat"
                                    m "TIDAK!! Aku khawatir tentang dia, biarkan aku pergi temukan dia"
                                    scene nbm_e47 with dissolve
                                    e "Saya mencoba membantu Anda tetapi Anda tidak akan berubah, sesuai dengan diri Anda sendiri"
                                    scene nbm_e48 with dissolve
                                    m "Ini dia?"
                                    b "Eh"
                                    m "Kamu tidak apa apa?"
                                    scene nbm_e49 with dissolve
                                    b "Mhhm"
                                    "..."
                                    b "Yes"
                                    scene nbm_e50 with dissolve
                                    m "Saya bisa melihatnya adalah priapism lagi"
                                    b "Err"
                                    scene nbm_e51 with dissolve
                                    m "{i} (siapa saya bodoh!) {/i}"
                                    scene nbm_e52 with dissolve
                                    m "Saya tahu itu tidak tepat tapi ..."
                                    m "Saya hanya ingin membantu Anda"
                                    menu:
                                        "cium dia":
                                            scene nbm_e54 with dissolve
                                            m "Itu hanya sampai hal ini hilang"
                                            scene nbmm
                                            m "..."
                                            "..."
                                            scene nbm_e55 with dissolve
                                            "..."
                                            pass
                                        "Biarkan dia mengurusnya":

                                            scene nbm_e53
                                            b "Aku tahu"
                                            pass
                                            scene nbm_e57 with dissolve
                                            "..."
                                            scene nbm_e56 with dissolve
                                            "..."
                                            scene nbm_e58 with hpunch
                                            m "Ughh"
                                            scene nbm_e59 with dissolve
                                            b "{i} (dia mengambil semuanya !!) {/i}"
                                            scene nbm_e60 with dissolve
                                            m "Ugh"
                                            pass
                                    scene nbm_e61 with dissolve
                                    m "Jangan mendorongnya di mulutku seperti ini [bname]"
                                    menu:
                                        "Ambil doggy -nya" if mrel >=400 and mcorr >= 15:
                                            b "Ouch"
                                            scene nbm_e62 with dissolve
                                            m "Ah"
                                            scene nbpd
                                            m "Ahhh"
                                            b "Grrr"
                                            m "Ah"
                                            "..."
                                            scene nbm_e64 with dissolve
                                            "..."
                                            scene nbm_e66 with fade
                                            m "Tidak ada yang pernah tahu tentang ini"
                                            if melsw == 7:
                                                $ melsw = 8
                                                scene nbm_e66a with fade
                                                "..."
                                                pass
                                            else:
                                                pass
                                        "Hidup dia":


                                            scene nbmk
                                            "..."
                                            m "..."
                                            "..."
                                            b "..."
                                            scene nbm_e63 with dissolve
                                            m "Ahhh"
                                            scene nbm_e65 with dissolve
                                            "..."
                                            scene nbm_e66 with fade
                                            m "Tidak ada yang pernah tahu tentang ini"
                                            if melsw == 7:
                                                scene nbm_e66a with fade
                                                $ melsw = 8
                                                "..."
                                                pass
                                            else:
                                                pass

                                    scene nbm_e67 with fade
                                    e "Kemana saja kamu?"
                                    m "Saya menemukannya di belakang pepohonan"
                                    m "Let's go"
                                    scene nbmereturn with fade
                                    "..."
                                    scene hall_d with fade
                                    b "{i} (...) {/i}"
                                    call screen gnav
                                else:


                                    pass
                                scene nbm_e34 with dissolve
                                "..."
                                e "Lihat, itu tidak sulit"
                                e "Pokoknya di sini [bname] kembali"
                                e "Let's go"
                                scene nbmereturn with fade
                                "..."
                                scene hall_d with fade
                                b "{i} (...) {/i}"
                                call screen gnav
                            else:

                                "Naikkan poin [mname] Anda menjadi 350"
                                pass
                        else:


                            pass
                    else:

                        e "Oke, saya harus kembali padanya"
                        pass

                    scene nbm_e16 with fade
                    e "Jadi, apakah Anda berubah pikiran?"
                    m "Tidak, berhentilah bertanya padaku"
                    e "Pfff"
                    e "Pokoknya di sini [bname] kembali"
                    e "Let's go"
                    scene nbmereturn with fade
                    "..."
                    scene hall_d with fade
                    b "{i} (...) {/i}"
                    call screen gnav
                else:

                    m "Saya tidak menginginkannya"
                    e "Pfff"
                    e "Saya akan melakukan berenang cepat dengan [bname]"
                    scene nbm_e20 with fade
                    e "Apa yang salah denganmu?"
                    b "Aku sangat terangsang, tapi aku tidak bisa cum"
                    e "Ya Tuhan, izinkan saya membantu Anda di bawah air"
                    scene nbm_e21 with dissolve
                    e "Mengawasi dia"
                    b "Yes"
                    e "Apakah kamu dekat?"
                    b "Tidak, itu tidak akan berhasil"
                    e "Oke, saya harus kembali padanya"
                    e "Kalau tidak, dia akan memperhatikan"
                    scene nbm_e16 with dissolve
                    e "Jadi, apakah Anda berubah pikiran?"
                    m "Tidak, berhentilah bertanya padaku"
                    e "Pfff"
                    e "Pokoknya di sini [bname] kembali"
                    e "Let's go"
                    scene nbmereturn with fade
                    "..."
                    scene hall_d with fade
                    b "{i} (...) {/i}"
                    call screen gnav
            "Berpura -pura tertidur":

                scene nbm_e35 with dissolve
                e "{i} (ah bagus, dia tertidur) {/i}"
                scene nbm_e36 with dissolve
                e "Sepertinya [bname] telah tertidur"
                m "Benar-benar?"
                e "Yes"
                e "Oh wow lihat pria di sana betapa hidup dia"
                scene nbm_e37 with dissolve
                m "Hidup dan menendang"
                $ menjoyedtheview = 1
                e "Hehehe"
                scene nbm_e38 with dissolve
                e "Ya Tuhan, kenapa kamu berbalik dan menutupi"
                m "SAYA..."
                e "Pfff"
                scene nbm_e39 with dissolve
                b "{i} (hehe sepertinya dia menikmati melihat penis itu) {/i}"
                b "{i} (itu adalah hal yang baik) {/i}"
                scene nbmereturn with fade
                "..."
                scene hall_d with fade
                b "{i} (...) {/i}"
                call screen gnav


            "Lihat pantatnya" if mvisitnudebeach >=5:
                scene nbm_e40 with dissolve
                b "{i}(Gorgeous){/i}"
                scene nbm_e41 with dissolve
                e "{i} (apakah dia bodoh atau apa?!) {/i}"
                scene nbm_e42 with dissolve
                b "{i} (fuck i can \ 't cum di sini) {/i}"
                scene nbm_e12 with dissolve
                "..."
                scene nbm_e13 with dissolve
                e "{i}(Oh God){/i}"
                e "[bname] Lebih baik Anda berenang, saya perlu berbicara dengan [mname]"
                e "In private"
                b "Ok"
                scene nbm_e15 with dissolve
                e "Berhenti menutupi, Anda membodohi diri sendiri"
                m "Saya tidak menyukainya"
                scene nbm_e16 with dissolve
                e "Percayalah padaku berdiri"
                m "ELAINE! Saya tidak tahu apakah saya dicukur atau tidak"
                e "Hanya berdiri aku akan memeriksanya, pandangan sekilas"
                e "Ayo"
                e "Beralihlah ke pepohonan dan coba, toh tidak ada orang di sini"
                scene nbm_e30 with dissolve
                e "Melihat! mudah"
                m "Not so"
                e "Lihatlah betapa gemuknya wanita ini di sana"
                e "Dan dia tidak peduli"
                scene nbm_e31 with dissolve
                m "Ya, tapi dia masih muda"
                e "Oh wow, seolah -olah Anda berusia 60 tahun"
                scene nbm_e30 with dissolve
                e "Demi Tuhan berhenti menjadi pemalu"
                e "Jangan terlalu memikirkannya"
                m "Dimana [bname]"
                e "Swimming"
                scene nbm_e32 with dissolve
                e "Lihat itu tidak sulit, sekarang Anda perlu mengambil tangan itu"
                scene nbm_e33 with dissolve
                m "..."
                e "Jangan khawatir dia tidak akan datang"
                e "Remove it"
                scene nbm_e34 with dissolve
                "..."
                e "Lihat, itu tidak sulit"
                e "Pokoknya di sini [bname] kembali"
                e "Let's go"
                scene nbmereturn with fade
                "..."
                scene hall_d with fade
                "..."
                b "{i} (...) {/i}"
                call screen gnav
            "Tidak melakukan apa -apa":


                scene nbm_e3 with fade
                "Anda meluangkan waktu dan pulang"
                scene nbmereturn with fade
                "..."
                scene hall_d with fade
                b "{i} (...) {/i}"
                call screen gnav
    else:



        scene nbm_e with fade
        "..."
        scene black
        "..."
        scene nbm_e2 with fade
        e "..."
        m "Ayo duduk di sampingku"
        scene nbm_e3 with dissolve
        "Anda meluangkan waktu dan pulang"
        scene nbmereturn with fade
        "..."
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
