label hallrelax:
    scene b_relax_d with fade
    s "[bname] !!"
    scene b_relax_d1 with hpunch
    b "Hah!"
    scene b_relax_d16 with dissolve
    s "Apakah Anda menyelesaikan pekerjaan rumah Anda?"
    b "Itu kamu!"
    b "Tinggalkan aku sendiri!"
    scene b_relax_d17 with dissolve
    s "Hahaha gotcha"
    if srel >=25 and instadone == 2:
        scene b_relax_d18 with dissolve
        s "Bangun"
        s "Mari kita kunjungi Rowena"
        b "Ya keren"
        b "Maksud saya ya kenapa tidak?"
        s "Kita bisa berenang di kolam renangnya"
        b "Ok"
        scene b_relax_d19 with dissolve
        s "Hmmm"
        jump rowenavisit
    else:

        scene b_relax_d18 with dissolve
        s "Bangun"
        s "Mari kita melakukan sesuatu yang bermanfaat"
        b "Seperti apa?"
        s "Seperti membersihkan tempat ini"
        b "Ugghh Ok"
        scene b_relax_d20 with fade
        "..."
        b "Saya sudah selesai di sini"
        scene b_relax_d21 with dissolve
        s "Apa kamu yakin?"
        b "Yeah"
        s "I'll check"
        scene b_relax_d22 with fade
        s "Looks Ok"
        s "Anda mungkin pergi sekarang"
        b "Hehehe"
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav

label halltv_morning:
    scene stv_morning with fade
    "..."
    scene stv_morning2 with dissolve
    s "Apa yang kamu lakukan anak muda?"
    b "Dengan serius!"
    scene stv_morning3 with dissolve
    s "Hahahaha"
    scene stv_morning1 with fade
    s "Apa yang kita tonton"
    b "Anda bermaksud mengatakan apa yang saya tonton"
    s "Yeah whatever"
    b "Ini hanya sebuah film dokumenter"
    s "Uh huh"
    if rvisit >=1 and stalkb_rowena == 0:
        $ stalkb_rowena = 1
        s "Jadi ... Katakan padaku"
        s "Jika Anda menyukai Rowena, mengapa Anda tidak memberitahunya"
        b "Apa?!"
        s "Anda harus mengatasi rasa malu Anda, jika Anda tidak ingin menjadi pecundang"
        b "Saya tidak malu"
        scene stv_morning4 with dissolve
        s "Anda, tapi jangan biarkan itu masuk ke kepala Anda"
        s "Tidak apa -apa untuk merasa canggung, terkadang semua orang melakukannya"
        s "Teruslah mencoba, Anda akan menjadi lebih baik"
        b "Menurutmu begitu?"
        s "Of course"
        s "Setidaknya mulai dengan mengatakan kepadanya bahwa Anda menyukainya"
        s "Aku akan membantumu dengannya"
        b "Benar-benar?"
        s "Yes"
        scene stv_morning5 with dissolve
        s "Saya tidak ingin Anda menghabiskan seluruh hidup Anda sebagai perawan"
        b "Apa ..."
        scene stv_morning6 with fade
        s "Lihat ya!"
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav

    elif rvisit >=1 and stalkb_rowena == 1:
        $ stalkb_rowena = 2
        s "Jadi ... ada berita dengan Rowena?"
        b "Nothing"
        s "Tapi apakah Anda berbicara dengannya?"
        s "Maksud saya, apakah Anda mengungkapkan ketertarikan Anda?"
        scene stv_morning4 with dissolve
        b "Not yet"
        s "Mengapa tidak?"
        b "Saya masih memikirkannya"
        s "Tidak ada yang perlu dipikirkan"
        s "Katakan saja padanya"
        b "Tapi bagaimana jika?"
        s "Bagaimana jika apa?"
        s "Bagaimana jika dia menolak Anda?"
        s "Jadi apa?"
        s "Siapa yang peduli, pergi ke gadis berikutnya dalam antrean"
        b "Tidak, maksud saya bagaimana jika ..."
        b "Bagaimana jika dia ingin mencium"
        scene stv_morning8 with dissolve
        s "Ya Tuhan!"
        s "I'll go"
        scene stv_morning7 with fade
        s "Saya keluar"
        "..."
        scene b_tv_d with fade
        "..."
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav

    elif rvisit >=1 and stalkb_rowena == 2:
        s "Jadi ... ada berita dengan Rowena?"
        b "Not yet"
        scene stv_morning4 with dissolve
        s "Beri tahu saya saat Anda memberitahunya"
        scene stv_morning7 with fade
        s "Aku akan pergi sekarang"
        "..."
        scene b_tv_d with fade
        "..."
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav

    elif stalkb_rowena ==3:
        if rowenaslap ==0:
            s "Jadi ... bagaimana hasilnya dengan Rowena?"
            b "Tidak apa -apa, kami berbicara kecil"
            scene stv_morning4 with dissolve
            s "Seperti apa yang kamu bicarakan?"
            b "Seperti cuaca dan sebagainya"
            scene stv_morning8 with dissolve
            s "Ya Tuhan!"
            b "Tidak tunggu, ada lagi"
            scene stv_morning4 with dissolve
            b "Saya mengatakan kepadanya bahwa bikini -nya terlihat bagus"
            s "Aha itu awal yang baik"
            s "Anyway"
            scene stv_morning7 with fade
            s "Aku akan pergi sekarang"
            s "Pikirkan tentang apa yang akan Anda katakan untuk waktu berikutnya"
            scene b_tv_d with fade
            "..."
            scene hall_d with fade
            b "{i} (...) {/i}"
            call screen gnav
        else:

            if skiss_asked == 0:
                s "Jadi..."
                s "Apakah Anda ingin berbicara tentang apa yang terjadi dengan Rowena?"
                b "Tidak ... saya lebih suka"
                s "Ayo!"
                scene stv_morning4 with dissolve
                s "Anda bisa memberi tahu saya"
                b "Dengan baik..."
                menu:
                    "Berbohong":
                        b "Saya mencoba menciumnya"
                        scene stv_morning9 with dissolve
                        s "Dengan serius!!"
                        b "Anda tidak membantu"
                        s "Sorry"
                        scene stv_morning4 with dissolve
                        s "Jadi apa yang terjadi sebenarnya"
                        s "Saya pikir dia tersinggung, bukankah itu?"
                        b "NOOO, sebaliknya"
                        b "Tapi ternyata dia tidak menyukainya"
                        b "Mungkin aku bukan pencium yang baik"
                        scene stv_morning10 with dissolve
                        s "Ohh!!"
                        b "Anda merusak kepercayaan diri saya dengan ekspresi wajah Anda"
                        scene stv_morning4 with dissolve
                        s "Yeah sorry"
                        scene stv_morning7 with fade
                        s "Aku akan pergi sekarang"
                        s "Maaf untuk itu"
                        menu:
                            "Mungkin Anda bisa membantu saya?":
                                $ skiss_asked = 1
                                s "Apa?"
                                scene stv_morning11 with dissolve
                                s "Apa maksudmu?"
                                b "Maksudku, mungkin ..."
                                s "Mungkin apa?"
                                b "Mungkin Anda bisa mengajari saya cara mencium"
                                scene stv_morning7 with dissolve
                                s "Oh God"
                                s "Lihat ya nanti"
                                scene b_tv_d with fade
                                show screen opnotif_f
                                b "{i}(Damn){/i}"
                                hide screen opnotif_f
                                scene hall_d with fade
                                "..."
                                call screen gnav
                            "Tidak mengatakan apa -apa":

                                scene b_tv_d with fade
                                "..."
                                scene hall_d with fade
                                b "{i} (...) {/i}"
                                call screen gnav
                    "Katakan yang sebenarnya":


                        b "Saya bilang saya menyukai bikini -nya"
                        scene stv_morning10 with dissolve
                        s "Saya tidak mengerti..."
                        s "Terakhir kali Anda mengatakan kepadanya hal yang sama"
                        b "Err baik kali ini saya mengatakannya secara berbeda!"
                        scene stv_morning9 with dissolve
                        s "Biarkan saya menebak, Anda mengisyaratkan sesuatu yang seksual"
                        b "Tidak, tidak seperti itu"
                        scene stv_morning4 with dissolve
                        s "Baik, saya tidak tahu harus berkata apa"
                        s "Tetapi jika Anda ngiler, atau bereaksi sebagai bajingan"
                        s "Saya mungkin tidak akan bisa membantu Anda"
                        scene stv_morning7 with fade
                        s "Aku akan pergi sekarang"
                        s "Maaf untuk itu"
                        scene b_tv_d with fade
                        "..."
                        scene hall_d with fade
                        b "{i} (...) {/i}"
                        call screen gnav
            else:


                menu:
                    "Minta untuk membantu Anda mencium":
                        scene stv_morning4 with dissolve
                        b "Jadi, apakah Anda akan membantu saya?"
                        s "Dengan apa?"
                        b "Meningkatkan ciuman saya"
                        scene stv_morning12 with dissolve
                        s "No [bname]"
                        if srel >=80:
                            b "Oh ayolah !!"
                            b "Saya membantu Anda sepanjang waktu"
                            b "Sekarang aku membutuhkanmu ..."
                            scene stv_morning8 with dissolve
                            b "Apakah ini ya?"
                            s "TIDAK!"
                            if skiss ==1:
                                b "Ayo, kami sudah melakukannya beberapa hari yang lalu di kolam Rowena"
                                scene stv_morning13 with dissolve
                                "..."
                                scene stv_morning14 with dissolve
                                s "Oke, hanya satu ciuman"
                                if kissrepeat <2:
                                    $ kissrepeat += 1
                                    scene stv_morning15 with fade
                                    s "Pegang kudamu"
                                    s "Tanpa tangan"
                                    scene stv_morning16 with dissolve
                                    "..."
                                    scene stv_morning17 with dissolve
                                    "..."
                                    scene stv_morning16 with dissolve
                                    s "Aku akan pergi sekarang"
                                    scene stv_morning7 with fade
                                    "..."
                                    scene b_tv_d with fade
                                    "..."
                                    scene hall_d with fade
                                    "..."
                                    call screen gnav
                                if kissrepeat >=2 and kissrepeat <4:
                                    $ kissrepeat += 1
                                    b "Oke tapi bisakah kita mencobanya?"
                                    b "Saya ingin berlatih posisi yang berbeda"

                                    s "Bisakah Anda berhenti menjadi cabul?"
                                    s "Anda membuat saya berubah pikiran"
                                    b "Apa yang saya lakukan kali ini?"
                                    s "Semua yang Anda katakan memiliki sesuatu yang salah"
                                    b "Seperti apa?"
                                    s "Tidak ada, mari kita lakukan satu ciuman dan aku keluar"
                                    scene stv_morning19 with fade
                                    s "Hands away"
                                    b "Ok"
                                    scene stv_morning20 with dissolve
                                    "..."
                                    scene stv_morning7 with fade
                                    s "Sampai jumpa"
                                    scene b_tv_d with fade
                                    "..."
                                    scene hall_d with fade
                                    "..."
                                    call screen gnav
                                else:

                                    b "Oke tapi bisakah kita mencobanya?"
                                    b "Saya ingin berlatih posisi yang berbeda"

                                    s "Bisakah Anda berhenti menjadi cabul?"
                                    s "Anda membuat saya berubah pikiran"
                                    b "Apa yang saya lakukan kali ini?"
                                    s "Semua yang Anda katakan memiliki sesuatu yang salah"
                                    b "Seperti apa?"
                                    s "Tidak ada, mari kita lakukan satu ciuman dan aku keluar"
                                    scene stv_morning19 with fade
                                    s "Tangan Jauh!"
                                    b "Ok"
                                    menu:
                                        "Ambil kepalanya":
                                            scene stv_morning18 with hpunch
                                            $ kissrepeat += 1
                                            show screen scorr
                                            s "Ahh"
                                            hide screen scorr
                                            $ scorr += 1
                                            if kissrepeat >6:
                                                scene stv_morning22 with dissolve
                                                "..."
                                                $ kissrepeat -= 1
                                                scene stv_morning23 with dissolve
                                                "..."
                                                menu:
                                                    "Saya ingin lebih":
                                                        if sbm ==1:
                                                            scene stv_morning43 with dissolve
                                                            s "Lagi?"
                                                            b "Anda tahu, lebih banyak ciuman bahasa Prancis ..."
                                                            s "Ah"
                                                            s "Ok"
                                                            scene stv_morning44 with dissolve
                                                            "..."
                                                            scene stv_morning45 with dissolve
                                                            "..."
                                                            scene stv_morning46 with dissolve
                                                            "..."
                                                            scene stv_morning47 with dissolve
                                                            "..."
                                                            scene stv_morning46 with dissolve
                                                            "..."
                                                            scene stv_morning48 with dissolve
                                                            s "Ahhh"
                                                            "..."
                                                            s "Saya harus pergi [bname]"
                                                            scene hall_d with fade
                                                            b "{i} (sialan, apa yang terjadi padanya) {/i}"
                                                            call screen gnav

                                                        elif sbm ==2:
                                                            scene stv_morning21 with fade
                                                            s "TIDAK!"
                                                            b "Mengapa?"
                                                            s "Saya tidak ingin lebih"
                                                            if srel >= 150:
                                                                scene stv_morning44 with hpunch
                                                                s "Ah"
                                                                scene stv_morning45 with dissolve
                                                                "..."
                                                                scene stv_morning46 with dissolve
                                                                "..."
                                                                scene stv_morning47 with dissolve
                                                                "..."
                                                                scene stv_morning46 with dissolve
                                                                "..."
                                                                scene stv_morning48 with dissolve
                                                                s "Ahhh"
                                                                "..."
                                                                if srel >= 300:
                                                                    s "[bname]"
                                                                    scene stv_morning50 with hpunch
                                                                    s "Anda menjadi lebih baik dalam berciuman"
                                                                    b "Hehe kamu belum melihat segalanya"
                                                                    b "Tapi itu semua berkat Anda"
                                                                    s "Apa maksudmu?"
                                                                    scene stv_morning51 with dissolve
                                                                    s "Lepaskan benda ini"
                                                                    scene stv_morning52 with dissolve
                                                                    "..."
                                                                    scene stv_morning53 with dissolve
                                                                    s "Ahhh"
                                                                    scene stv_morning54 with dissolve
                                                                    "..."
                                                                    scene stv_morning55 with dissolve
                                                                    s "Hmmm"
                                                                    scene stv_morning56 with dissolve
                                                                    "..."
                                                                    scene stv_morning57 with hpunch
                                                                    b "..."
                                                                    b "{i}(Oh fuck){/i}"
                                                                    "..."
                                                                    scene stv_morning41 with fade
                                                                    s "Sorry [bname]"
                                                                    b "It's fine"
                                                                    scene hall_d with fade
                                                                    b "{i} (Saya pikir saya harus pergi mencuci) {/i}"
                                                                    call screen gnav
                                                                else:

                                                                    pass
                                                                s "Saya harus pergi [bname]"
                                                                scene hall_d with fade
                                                                b "{i} (sialan, apa yang terjadi padanya) {/i}"
                                                                call screen gnav
                                                            else:
                                                                pass
                                                            scene b_tv_d with fade
                                                            "..."
                                                            scene hall_d with fade
                                                            "..."
                                                            call screen gnav
                                                        else:



                                                            if srel >= 150:
                                                                scene stv_morning21 with fade
                                                                s "TIDAK!"
                                                                b "Mengapa?"
                                                                s "Saya tidak ingin lebih"
                                                                scene stv_morning44 with hpunch
                                                                s "Ah"
                                                                scene stv_morning45 with dissolve
                                                                "..."
                                                                scene stv_morning46 with dissolve
                                                                "..."
                                                                scene stv_morning47 with dissolve
                                                                "..."
                                                                scene stv_morning46 with dissolve
                                                                "..."
                                                                scene stv_morning48 with dissolve
                                                                s "Ahhh"
                                                                "..."
                                                                if srel >= 300:
                                                                    s "[bname]"
                                                                    scene stv_morning50 with hpunch
                                                                    s "Anda menjadi lebih baik dalam berciuman"
                                                                    b "Hehe kamu belum melihat segalanya"
                                                                    b "Tapi itu semua berkat Anda"
                                                                    s "Apa maksudmu?"
                                                                    scene stv_morning51 with dissolve
                                                                    s "Lepaskan benda ini"
                                                                    scene stv_morning52 with dissolve
                                                                    "..."
                                                                    scene stv_morning53 with dissolve
                                                                    s "Ahhh"
                                                                    scene stv_morning54 with dissolve
                                                                    "..."
                                                                    scene stv_morning55 with dissolve
                                                                    s "Hmmm"
                                                                    scene stv_morning56 with dissolve
                                                                    "..."
                                                                    scene stv_morning57 with hpunch
                                                                    b "..."
                                                                    b "{i}(Oh fuck){/i}"
                                                                    "..."
                                                                    scene stv_morning41 with fade
                                                                    s "Sorry [bname]"
                                                                    b "It's fine"
                                                                    scene hall_d with fade
                                                                    b "{i} (Saya pikir saya harus pergi mencuci) {/i}"
                                                                    call screen gnav
                                                                else:
                                                                    s "Saya harus pergi [bname]"
                                                                    scene hall_d with fade
                                                                    b "{i} (sialan, apa yang terjadi padanya) {/i}"
                                                                    call screen gnav
                                                            else:
                                                                scene stv_morning43 with dissolve
                                                                s "Lagi?"
                                                                b "Anda tahu, lebih banyak ciuman bahasa Prancis ..."
                                                                s "Ah"
                                                                s "OK"
                                                                scene stv_morning44 with dissolve
                                                                "..."
                                                                scene stv_morning49 with dissolve
                                                                s "Saya harus pergi [bname]"
                                                                b "Apa! Mengapa?"
                                                                s "Sampai jumpa"
                                                                scene b_tv_d with fade
                                                                "..."
                                                                scene hall_d with fade
                                                                "..."
                                                                call screen gnav
                                                    "Melanjutkan":

                                                        pass
                                            else:

                                                pass
                                            scene stv_morning21 with fade
                                            b "Apa?"
                                            s "Sudah kubilang tidak ada tangan!"
                                            if mobilephoneacquired ==1 and smobilegiven ==0:
                                                menu:
                                                    "Beri dia ponselnya":
                                                        $ smobilegiven = 1
                                                        b "Anda lebih baik berhenti bersikap kasar kepada saya"
                                                        scene stv_morning24 with dissolve
                                                        s "Apa?"
                                                        b "Saya memiliki..."
                                                        scene stv_morning25 with dissolve
                                                        b "Ini untukmu"
                                                        s "Dengan serius!!"
                                                        scene stv_morning26 with dissolve
                                                        b "Yes"
                                                        scene stv_morning27 with hpunch
                                                        b "Woah!"
                                                        "..."
                                                        scene stv_morning28 with dissolve
                                                        s "Apakah ini model terbaru?"
                                                        b "Anda bertaruh"
                                                        s "..."
                                                        b "Jadi, bisakah kita melanjutkan pelajaran kita?"
                                                        scene stv_morning29 with dissolve
                                                        s "Yes sure"
                                                        scene stv_morning30 with dissolve
                                                        s "Pelajaran yang mana?"
                                                        b "Maksud saya satu ciuman lagi"
                                                        s "[bname] Ini tidak pantas untuk ..."
                                                        s "Maksudku oke, letakkan aku"
                                                        b "Ayo hanya satu ciuman"
                                                        b "Tolong ajari aku"
                                                        scene stv_morning31 with dissolve
                                                        s "..."
                                                        s "Pertama, Anda melepas kacamatanya"
                                                        scene stv_morning32 with dissolve
                                                        "..."
                                                        scene stv_morning33 with dissolve
                                                        b "..."
                                                        scene stv_morning32 with dissolve
                                                        s "Senang?"
                                                        b "Yes"
                                                        s "Ok letakkan saya, saya harus pergi"
                                                        b "Sure"
                                                        scene hall_d with fade
                                                        "..."
                                                        call screen gnav
                                            else:
                                                pass
                                            scene b_tv_d with fade
                                            "..."
                                            scene hall_d with fade
                                            "..."
                                            call screen gnav
                                        "Jangan lakukan itu":

                                            scene stv_morning20 with dissolve
                                            "..."
                                            scene stv_morning7 with fade
                                            s "Sampai jumpa"
                                            scene b_tv_d with fade
                                            "..."
                                            scene hall_d with fade
                                            "..."
                                            call screen gnav
                            else:


                                b "Ayo!!"
                                s "Stop it"
                                b "Tapi kenapa?"
                                scene stv_morning7 with fade
                                s "Aku akan pergi sekarang"
                                scene b_tv_d with fade
                                "..."
                                scene hall_d with fade
                                "Anda perlu menyelesaikan sesuatu di kolam Rowena"
                                call screen gnav
                        else:
                            pass
                        s "Stop it"
                        b "Tapi kenapa?"
                        scene stv_morning7 with fade
                        s "Aku akan pergi sekarang"
                        scene b_tv_d with fade
                        "..."
                        scene hall_d with fade
                        "..."
                        call screen gnav

                    "Beri dia tiketnya" if ticketrequested == 3:
                        b "Ermm, aku punya sesuatu untukmu"
                        scene stv_morning10 with dissolve
                        s "Apa itu?"
                        b "Tiket untuk Taylor Shaft"
                        $ ticketrequested = 4
                        scene stv_morning9 with dissolve
                        s "Dengan serius!"
                        b "Ya, tapi saya ingin sesuatu sebagai balasannya"
                        scene stv_morning34 with hpunch
                        s "Dimana tiketnya !!"
                        b "Ini satu -satunya tiket untuk Anda"
                        s "Ya Terserah!"
                        s "Show me"
                        scene stv_morning35 with dissolve
                        s "Yaaaaah !!"
                        scene stv_morning36 with hpunch
                        s "Terima kasih Andauuuu !!!"
                        scene stv_morning31 with dissolve
                        s "Jadi apa yang Anda inginkan sebagai balasannya?"
                        menu:
                            "Ciuman":
                                s "Oke, lepaskan kacamata saya"
                                scene stv_morning32 with dissolve
                                "..."
                                scene stv_morning33 with dissolve
                                s "Mhhmm"
                                scene stv_morning40 with dissolve
                                "..."
                                scene stv_morning42 with dissolve
                                s "Mungkin Anda bisa membantu saya memilih apa yang akan dipakai untuk konser"
                                b "Sure"
                                scene stv_morning41 with dissolve
                                s "..."
                                scene stv_morning7 with fade
                                s "Kamar saya, setelah 5 menit"
                                scene hall_d with fade
                                b "{i} (keren) {/i}"
                                b "{i} (...) {/i}"
                                b "{i} (Itu, hampir 5 menit) {/i}"
                                scene concert_outfit with fade
                                s "Bagaimana menurutmu?"
                                b "Bagus"
                                b "Apakah itu indoor atau outdoor?"
                                s "Saya tidak tahu, apa bedanya?"
                                b "Me neither"
                                s "Lalu kenapa kamu bertanya?"
                                b "Saya tidak tahu saya pikir itu harus membuat perbedaan dalam apa yang harus dipakai"
                                b "Jika itu di luar ruangan, mungkin Anda harus mencoba sesuatu yang lebih santai"
                                s "Ok tunggu di luar"
                                scene door with dissolve
                                "..."
                                s "Anda bisa masuk!"
                                scene concert_outfit1 with fade
                                s "Yang ini?"
                                b "Luar biasa, kita harus mengambil pemotretan di dalamnya"
                                s "Yes"
                                b "Dengan jaket terbuka dan tanpa kemeja di bawahnya"
                                s "Izinkan saya menunjukkan satu lagi"
                                s "Tunggu"
                                b "Oh ayolah!"
                                s "Tolong tunggu"
                                scene door with dissolve
                                "..."
                                s "Anda bisa masuk!"
                                scene concert_outfit2 with fade
                                s "Jadi?"
                                b "Suka sekali"
                                scene concert_outfit3 with dissolve
                                s "Dingin"
                                b "Tanpa bra tentu saja"
                                s "Pervert"
                                b "Hahaha"
                                s "Pergi sekarang, saya ingin mengobrol dengan Rowena"
                                b "Ok"
                                scene door with fade
                                b "{i} (...) {/i}"
                                call screen gnav
                            "Saya ingin Anda menyiapkan makan siang telanjang":

                                scene stv_morning37 with dissolve
                                s "Pergi bercinta diri sendiri"
                                "..."
                                scene stv_morning38 with dissolve
                                s "Mhhmm"
                                scene stv_morning39 with dissolve
                                "..."
                                scene stv_morning42 with dissolve
                                s "Terima kasih [bname]"
                                scene stv_morning41 with dissolve
                                s "..."
                                if srel >= 100:
                                    $ snaked_lunch = 1
                                    pass
                                else:
                                    "Anda telah melewatkan sesuatu karena Anda memiliki poin hubungan yang rendah"
                                    pass
                                scene stv_morning7 with fade
                                s "Lihat yah!"
                                scene hall_d with fade
                                b "{i} (...) {/i}"
                                call screen gnav
                    "Tidak mengatakan apa -apa":



                        "..."
                        s "Boring"
                        scene stv_morning7 with fade
                        s "Aku akan pergi sekarang"
                        scene b_tv_d with fade
                        "..."
                        scene hall_d with fade
                        b "{i} (...) {/i}"
                        call screen gnav
    else:

        s "Boring"
        s "I'll go"
        scene stv_morning7 with fade
        "..."
        scene b_tv_d with fade
        "..."
        scene hall_d with fade
        b "{i} (...) {/i}"
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
