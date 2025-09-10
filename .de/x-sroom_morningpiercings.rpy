image spiera:
    "spiera00.jpg"
    pause 0.02
    "spiera01.jpg"
    pause 0.02
    "spiera02.jpg"
    pause 0.02
    "spiera03.jpg"
    pause 0.02
    "spiera04.jpg"
    pause 0.02
    "spiera05.jpg"
    pause 0.02
    "spiera06.jpg"
    pause 0.02
    "spiera07.jpg"
    pause 0.02
    "spiera08.jpg"
    pause 0.02
    "spiera09.jpg"
    pause 0.02
    "spiera10.jpg"
    pause 0.02
    "spiera11.jpg"
    pause 0.02
    "spiera12.jpg"
    pause 0.02
    "spiera13.jpg"
    pause 0.02
    "spiera14.jpg"
    pause 0.02
    "spiera15.jpg"
    pause 0.02
    "spiera16.jpg"
    pause 0.02
    "spiera17.jpg"
    pause 0.02
    "spiera18.jpg"
    pause 0.02
    "spiera19.jpg"
    pause 0.02
    "spiera20.jpg"
    pause 0.02
    "spiera21.jpg"
    pause 0.02
    "spiera22.jpg"
    pause 0.02
    "spiera23.jpg"
    pause 0.02
    "spiera24.jpg"
    pause 0.02
    "spiera25.jpg"
    pause 0.02
    "spiera26.jpg"
    pause 0.02
    "spiera27.jpg"
    pause 0.02
    "spiera28.jpg"
    pause 0.02
    "spiera29.jpg"
    pause 0.02
    "spiera30.jpg"
    pause 0.02
    "spiera31.jpg"
    pause 0.02
    "spiera32.jpg"
    pause 0.02
    "spiera33.jpg"
    pause 0.02
    "spiera34.jpg"
    pause 0.02
    "spiera35.jpg"
    pause 0.02
    "spiera36.jpg"
    pause 0.02
    "spiera37.jpg"
    pause 0.02
    "spiera38.jpg"
    pause 0.02
    "spiera39.jpg"
    pause 0.02
    "spiera40.jpg"
    pause 0.02
    "spiera41.jpg"
    pause 0.02
    "spiera42.jpg"
    pause 0.02
    "spiera43.jpg"
    pause 0.02
    "spiera44.jpg"
    pause 0.02
    "spiera45.jpg"
    pause 0.02
    "spiera46.jpg"
    pause 0.02
    "spiera47.jpg"
    pause 0.02
    "spiera48.jpg"
    pause 0.02
    "spiera49.jpg"
    pause 0.02
    "spiera50.jpg"
    pause 0.02
    "spiera51.jpg"
    pause 0.02
    repeat

image svcu:
    "svcu00.jpg"
    pause 0.01
    "svcu01.jpg"
    pause 0.01
    "svcu02.jpg"
    pause 0.01
    "svcu03.jpg"
    pause 0.01
    "svcu04.jpg"
    pause 0.01
    "svcu05.jpg"
    pause 0.01
    "svcu06.jpg"
    pause 0.01
    "svcu07.jpg"
    pause 0.01
    "svcu08.jpg"
    pause 0.01
    "svcu09.jpg"
    pause 0.01
    "svcu10.jpg"
    pause 0.01
    "svcu11.jpg"
    pause 0.01
    "svcu12.jpg"
    pause 0.01
    "svcu13.jpg"
    pause 0.01
    "svcu14.jpg"
    pause 0.01
    "svcu15.jpg"
    pause 0.01
    "svcu16.jpg"
    pause 0.01
    "svcu17.jpg"
    pause 0.01
    "svcu18.jpg"
    pause 0.01
    "svcu19.jpg"
    pause 0.01
    "svcu20.jpg"
    pause 0.01
    "svcu21.jpg"
    pause 0.01
    "svcu22.jpg"
    pause 0.01
    "svcu23.jpg"
    pause 0.01
    "svcu24.jpg"
    pause 0.01
    "svcu25.jpg"
    pause 0.01
    "svcu26.jpg"
    pause 0.01
    "svcu27.jpg"
    pause 0.01
    "svcu28.jpg"
    pause 0.01
    "svcu29.jpg"
    pause 0.01
    "svcu30.jpg"
    pause 0.01
    "svcu31.jpg"
    pause 0.01
    "svcu32.jpg"
    pause 0.01
    "svcu33.jpg"
    pause 0.01
    "svcu34.jpg"
    pause 0.01
    "svcu35.jpg"
    pause 0.01
    "svcu36.jpg"
    pause 0.01
    "svcu37.jpg"
    pause 0.01
    "svcu38.jpg"
    pause 0.01
    "svcu39.jpg"
    pause 0.01
    "svcu40.jpg"
    pause 0.01
    "svcu41.jpg"
    pause 0.01
    "svcu42.jpg"
    pause 0.01
    "svcu43.jpg"
    pause 0.01
    "svcu44.jpg"
    pause 0.01
    "svcu45.jpg"
    pause 0.01
    "svcu46.jpg"
    pause 0.01
    "svcu47.jpg"
    pause 0.01
    "svcu48.jpg"
    pause 0.01
    "svcu49.jpg"
    pause 0.01
    "svcu50.jpg"
    pause 0.01
    "svcu51.jpg"
    pause 0.01
    repeat

label sroom_morningpiercings:
    scene door with fade
    b "{i} (...) {/i}"
    s "Datang"
    scene sroompier with fade
    s "Jadi bagaimana menurut Anda?"
    b "Tentang apa?"
    s "Duh the Piercings"
    scene sroompier1 with dissolve
    b "Ah, yang ini"
    b "Saya tidak memperhatikan"
    s "Itu indah, bukan"
    b "Yeah"
    menu:
        "Mengapa kita tidak pergi ke pantai ini?" if sgoestost >= 2:
            s "Ya, dengan Rowena"
            b "Dingin"
            scene bwr with fade
            b "Dimana pacarmu Rowena?"
            a "Dia memiliki pekerjaan hari ini"
            s "Jangan khawatir dengan atasan bikini ini kita akan menemukannya pacar yang lebih baik"
            scene bwr1 with dissolve
            a "Hahaha"
            b "Hei bagus, anting -anting dari mana Anda mendapatkannya?"
            scene bwr1a with dissolve
            s "Secret"
            scene bwr2 with fade
            b "Mengapa Anda tidak menghapus bikini Anda"
            b "Ini adalah pantai telanjang"
            s "Kami tidak ingin, tidak gratis"
            b "Huh"
            s "Jangan peluk aku, tidak ada yang gratis"
            b "Apa -apaan!"
            b "Sesuai dengan dirimu sendiri, aku akan berenang"
            scene bwr3 with dissolve
            s "Lihat Rowena, ini salah satu untuk Anda"
            s "Dia terlihat kaya"
            scene bwr4 with dissolve
            a "Yang mana?"
            s "Yang ada di sebelah kiri"
            a "Bagaimana Anda tahu dia?"
            scene bwr5 with dissolve
            s "Hi guys"
            "Hai, yang di sana"
            s "Sudah pergi?"
            scene bwr6 with dissolve
            s "Still early"
            "Ya, apa yang Anda sarankan"
            s "Kami bisa pergi pesta dengan kalian"
            "Bukan ide yang buruk"
            "Apa yang bisa Anda tawarkan"
            s "Tidak, tidak, Anda salah paham"
            s "Kami akan pergi ke pesta hanya setelah mengetahui apa yang Anda tawarkan"
            scene bwr7 with dissolve
            "Apa yang kamu katakan?"
            scene bwr8 with dissolve
            "Terserah kamu"
            scene bwr7 with dissolve
            "Bocah pirang adalah untukku"
            scene bwr9 with dissolve
            "Berapa harga Anda?"
            s "$ 4000"
            a "Hah!"
            "Berurusan, lepaskan"
            scene bwr10 with fade
            b "Apa -apaan"
            b "Hey kemana kamu pergi"
            $ persistent.unlock_64 = True
            scene bwr11 with dissolve
            b "{i} (fuck it, bitches, mereka pergi dengan sial guys) {/i}"
            scene srgb with fade
            s "Tempat yang bagus"
            a "[sname] Apa yang kita lakukan?"
            scene srgb1 with dissolve
            s "Shh"
            s "Ini adalah bisnis yang sebenarnya"
            s "Begitulah cara anak perempuan menghasilkan uang"
            scene srgb2 with fade
            "Masih belum siap"
            scene srgb3 with dissolve
            s "Kami sedang menunggumu laki -laki besar"
            scene srgb4 with dissolve
            a "Huh"
            scene srgb5 with dissolve
            "..."
            scene srgb6 with dissolve
            s "Ahhh"
            scene srgb7 with dissolve
            s "Sudah kubilang kamu akan menyukainya"
            scene srgb7a with fade
            s "..."
            scene black
            "SEMENTARA ITU"
            scene srgb8 with fade
            b "Huh"
            if mbvisit >= 1:
                mb "Hai [bname] Saya baru saja pergi"
                pass
            elif mbunknown == 1:
                "Hai saya baru saja pergi"
                b "Siapa kamu?"
                mb "Saya Adam, [mname] rekan kerja"
                b "Oke dan dimana dia?"
                mb "Saya baru saja mengantarnya pulang"
                mb "Dia pergi ke kamar mandi"
                pass
            else:
                "Hai saya baru saja pergi"
                b "Siapa kamu?"
                mb "Saya Adam, [mname] rekan kerja"
                b "Oke dan dimana dia?"
                mb "Saya baru saja mengantarnya pulang"
                mb "Dia pergi ke kamar mandi"
                pass
            scene srgb9 with fade
            m "Hai [bname] ya saya di sini"
            b "..."
            m "Selamat malam Adam"
            mb "Selamat malam"
            scene srgb10 with fade
            b "{i} (ada sesuatu yang salah dengannya) {/i}"
            b "{i} (dia tidak berbicara) {/i}"
            scene srgb11 with dissolve
            b "Apa yang salah?"
            m "Dimana [sname]"
            b "Kami pergi ke Rowena dan dia tinggal bersamanya"
            m "Ok"
            m "Aku akan tidur sekarang"
            b "Ini awal?"
            m "Selamat malam"
            scene srgb12 with dissolve
            b "{i} (ada sesuatu yang pasti) {/i}"
            b "{i} (itu lebih baik saya menonton tv) {/i}"
            scene srgb13 with fade
            "..."
            s "[bname]"
            scene srgb14 with dissolve
            b "Anda datang!"
            s "Saya butuh bantuan Anda"
            b "Setelah Anda meninggalkan saya di pantai?"
            b "Anda meminta bantuan?"
            scene srgb15 with dissolve
            s "Saya serius [bname]"
            s "Saya perlu pergi ke ruang gawat darurat"
            scene srgb16 with fade
            "Ada pendarahan kecil di ujung rektum"
            "Tapi semuanya akan baik -baik saja dengan obat yang kami berikan padanya"
            b "Ok thanks"
            scene srgb17 with fade
            b "Apa yang Anda lakukan untuk diri sendiri"
            s "Tolong jangan beri tahu siapa pun"
            b "Tapi mengapa Anda memasukkan diri Anda ke semua omong kosong ini"
            s "Uang"
            b "Uang apa?"
            s "Saya melakukannya untuk uang"
            $ sgmtb = 1
            b "Tidak ada yang bisa saya?"
            s "Aku akan memberimu sesuatu, biarkan aku memasang krim dan tidur siang terlebih dahulu"
            b "Ok"
            scene door with fade
            "..."
            call screen gnav
        "Mengangkatnya":






            scene sroompier4 with hpunch
            s "Dimana kamu membawaku?"
            b "Ke tempat tidur"
            if srel >=400:
                s "Apa yang akan Anda lakukan di tempat tidur?"
                scene sroompier6 with fade
                b "Saya akan melakukan ini"
                s "..."
                scene sroompier7 with dissolve
                s "Ahhh"
                s "Anda membunuh saya"
                scene sroompier8 with dissolve
                "..."
                scene sroompier9 with dissolve
                s "Slowly please"
                b "Ok"
                s "Dan jangan cum di dalam"
                scene sroompier10 with dissolve
                s "[bname]!"
                scene sroompier11 with dissolve
                s "Ahhh"
                scene sroompier19 with dissolve
                s "Ohhh"
                scene sroompier20 with dissolve
                s "Not inside"
                scene sroompier12 with fade
                s "Aku akan mencuci"
                b "Yeah ok"
                scene door with fade
                "..."
                call screen gnav



            elif srel >=200:
                s "Tidak [bname], tolong"
                b "Apa tidak?"
                s "Tolong taruh saya [bname]"
                b "Ok"
                scene sroompier with fade
                s "Sampai jumpa"
                scene door with fade
                "Naikkan poin hubungan Anda menjadi 400"
                call screen gnav
            else:

                s "Apa!"
                s "Menjatuhkanku"
                b "No"
                s "Aku bilang menjatuhkanku"
                b "Ok"
                scene sroompier5 with fade
                b "Sampai jumpa"
                s "..."
                scene door with fade
                "Naikkan poin hubungan Anda menjadi 400"
                call screen gnav
        "Cium dia":

            scene sroompier2 with hpunch
            "..."
            $ srel += 1
            scene sroompier3 with dissolve
            show screen srelup
            "..."
            hide screen srelup
            scene sroompier2 with dissolve
            if srel >=300:
                s "Cukup tolong letakkan saya"
                b "Ok"
                scene sroompier13 with dissolve
                s "Mmm"
                scene sroompier14 with dissolve
                s "Ahhh"
                scene sroompier15 with dissolve
                "..."
                if srel >=400:
                    scene sroompier16 with dissolve
                    s "Dimana kamu membawaku?"
                    b "Ke lantai, tapi pertama -tama mari kita lepaskan ini"
                    scene spiera00 with dissolve
                    s "Lambat oke?"
                    b "Yes"
                    s "Turunkan Tangan Anda"
                    scene spiera
                    $ persistent.unlock_9 = True
                    s "Uhh"
                    "..."
                    b "Astaga!"
                    scene svcu
                    "..."
                    b "I'm close"
                    s "Mengeluarkan"
                    menu:
                        "Mengeluarkan":
                            pass
                        "Jangan":
                            scene sroompier21 with vpunch
                            b "Ahhh"
                            s "Apa ...."
                            b "Sorry"
                            $ spreg += 1
                            scene sroompier22 with fade
                            s "..."
                            b "Sampai jumpa!"
                            scene door with fade
                            "..."
                            call screen gnav

                    scene sroompier17 with hpunch
                    b "Ahhh"
                    scene sroompier18 with dissolve
                    b "Lihat yah!"
                    scene door with fade
                    "..."
                    call screen gnav
                else:
                    s "Enough [bname]"
                    s "Please"
                    b "Apakah Anda yakin ingin berhenti?"
                    s "Yes please"
                    scene sroompier1 with fade
                    b "Ok sampai jumpa"
                    b "Dan tindikan yang indah"
                    s "Thanks"
                    scene door with fade
                    "Naikkan poin hubungan Anda menjadi 400 untuk melihat lebih banyak"
                    call screen gnav
            else:

                s "Cukup tolong letakkan saya"
                scene sroompier with fade
                s "Sampai jumpa"
                scene door with fade
                "Naikkan poin hubungan Anda menjadi 300 untuk mendapatkan lebih banyak"
                call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
