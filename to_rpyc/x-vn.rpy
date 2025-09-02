

label vn:

    if mrel >=150:
        scene nwork_goingna with fade
        b "{i} (dimana dia?) {/i}"
        menu:
            "Pergi mencari dia":
                scene nwork_going5 with fade
                b "{i}(Wow){/i}"
                scene nwork_going6 with dissolve
                m "Selamat pagi [bname]"
                b "..."
                b "Selamat pagi"
                scene nwork_going7 with dissolve
                m "Maaf saya sangat terlambat untuk bekerja"
                scene nwork_going8 with dissolve
                b "Bisakah saya membantu Anda dengan sesuatu?"
                scene nwork_going9 with dissolve
                m "Ya, beri saya bra saya dari laci di sana"
                scene nwork_going10 with dissolve
                b "Sure"
                menu:
                    "Beri dia bra yang salah":
                        scene nwork_going13 with dissolve
                        m "Ini bukan!"
                        m "The other"
                        b "Ok sorry"
                        pass
                    "Beri bra yang tepat":

                        show screen mrelup
                        $ mrel += 2
                        b "Here"
                        hide screen mrelup
                        pass

                scene nwork_going11 with fade
                m "Terima kasih"
                scene nwork_going with fade
                b "Sampai jumpa di malam hari"
                m "Yes"
                scene hall_d with fade
                b "{i} (...) {/i}"
                s "Hey"
                scene nwork_goingdr1 with dissolve
                s "Apa yang ada"
                b "[mname] Baru saja pergi"
                s "Jadi begitu"
                b "Ya kita punya hari untuk diri kita sendiri"
                s "Saya berencana untuk pergi menemui Rowena"
                b "Bisakah aku ikut denganmu?"
                s "Hmm"
                s "Ya kenapa tidak"
                if rosdad == 0:
                    pass
                elif rorepeat >=3:
                    s "{i} (i \ 'll temukan cara untuk pergi dengan rowena saja) {/i}"
                    pass
                jump rowenamorningvisit
    else:



        pass
    scene nwork_going with fade
    b "Selamat pagi"
    m "Pagi"
    b "Akan bekerja?"
    scene nwork_goingdr with dissolve
    m "Jangan mengingatkan saya"
    s "Selamat pagi"
    m "Saya kembali terlambat hari ini"
    scene nwork_goingdr1 with dissolve
    s "Apa yang salah dengannya?"
    b "Saya tidak tahu, tetapi dia memiliki masalah di tempat kerja"
    s "Setidaknya dia bisa kembali pagi saya"
    b "Tidak apa -apa, setidaknya kita punya hari untuk diri kita sendiri"
    s "Saya berencana untuk pergi menemui Rowena"
    b "Bisakah aku ikut denganmu?"
    s "Hmm"
    s "Ya kenapa tidak"
    if rosdad == 0:
        pass
    elif rorepeat >=3:
        s "{i} (i \ 'll temukan cara untuk pergi dengan rowena saja) {/i}"
        pass
    jump rowenamorningvisit



label rowenamorningvisit:
    scene row_visit7 with fade
    s "Kami tidak butuh waktu lama"
    scene row_visit8 with dissolve
    b "Surprisingly no"
    s "Haruskah kita berenang"
    a "Bukan untuk saya, maaf"
    s "Mengapa?"
    a "Tidak pandai dalam hal itu"
    a "Silakan, jangan keberatan saya, saya akan kecokelatan"
    scene row_visit9 with fade
    b "Aha!"
    scene row_visit10 with dissolve
    b "Anda pikir Anda cepat, hahaha"
    scene row_visit11 with dissolve
    s "Bllllehhh"
    b "Tangkap saya jika Anda bisa"
    scene row_visit12 with dissolve
    "..."
    scene row_visit13 with dissolve
    b "Huh"
    if rosdad == 0:
        scene row_visit14 with fade
        s "Saya ingin pergi ke suatu tempat tapi ..."
        $ rosdad = 2
        a "Dimana"
        s "Aku akan memberitahumu dalam perjalanan"
        s "Tapi pertama -tama bagaimana kita bisa menyimpan [bname] di sini?"
        s "Saya tidak ingin membawanya bersama kami"
        a "Hmm"
        a "Saya punya ide"
        a "Kita bisa membiarkan ibuku tinggal bersamanya"
        s "Dan apa yang akan kita katakan padanya?"
        s "Kita perlu menemukan alasan mengapa kita pergi"
        s "Saya pikir kita perlu mengalihkan perhatiannya dengan sesuatu"
        a "Ibuku adalah gangguan terbesar"
        scene row_visit14p with dissolve
        s "Tidak cukup, ambil pil ini masukkan segelas anggur dan biarkan memberinya"
        pass

    elif rorepeat >=3:
        scene row_visit14 with fade
        if persistent.patch_enabled:
            s "Apakah Anda ingin mengunjungi ayah saya?"
            pass
        else:
            s "Apakah Anda ingin mengunjungi Stewart?"
            pass
        a "Tapi bagaimana kita akan menyimpan [bname] di sini?"
        s "Saya tidak tahu, apakah Anda punya ide?"
        a "Hmm"
        a "Yes"
        a "Kita bisa membiarkan ibuku tinggal bersamanya"
        s "Dan apa yang akan kita katakan padanya?"
        s "Kita perlu menemukan alasan mengapa kita pergi"
        s "Saya pikir kita perlu mengalihkan perhatiannya dengan sesuatu"
        a "Ibuku adalah gangguan terbesar"
        scene row_visit14p with dissolve
        s "Tidak cukup, ambil pil ini masukkan segelas anggur dan biarkan memberinya"
        pass
    else:


        scene row_visit14 with fade
        s "Saya ingin pergi ke suatu tempat tapi ..."
        $ rosdad = 2
        a "Dimana"
        s "Aku akan memberitahumu dalam perjalanan"
        s "Tapi pertama -tama bagaimana kita bisa menyimpan [bname] di sini?"
        s "Saya tidak ingin membawanya bersama kami"
        a "Hmm"
        a "Saya punya ide"
        a "Kita bisa membiarkan ibuku tinggal bersamanya"
        s "Dan apa yang akan kita katakan padanya?"
        s "Kita perlu menemukan alasan mengapa kita pergi"
        s "Saya pikir kita perlu mengalihkan perhatiannya dengan sesuatu"
        a "Ibuku adalah gangguan terbesar"
        scene row_visit14p with dissolve
        s "Tidak cukup, ambil pil ini masukkan segelas anggur dan biarkan memberinya"
        pass



    scene row_visit15 with fade
    s "[bname]"
    s "Apakah Anda ingin minum sesuatu?"
    b "Ya, tentu saja"
    s "Kuat seperti biasa bukan?"
    scene row_visit80 with dissolve
    b "Uh huh"
    scene black
    "Setelah beberapa menit"
    scene row_visit87 with fade
    s "Cheers"
    b "Terima kasih"
    scene row_visit85 with fade
    b "Itu adalah minuman yang enak"
    b "Kemana mereka pergi"
    b "Saya pikir kami akan minum bersama"
    scene row_visit88 with hpunch
    b "Ah! Sungguh!"
    b "Apa salahnya!"
    b "Berengsek!"
    scene row_visit81 with fade
    b "Kesalahan maaf tapi saya perlu menggunakan toilet"
    rm "Ok"
    scene row_visit81a with dissolve
    rm "{i} (woah i \ 'm masih bagus) {/i}"
    scene row_visit81 with dissolve
    rm "Ok saya akan menunggu di luar"
    rm "Hubungi jika Anda membutuhkan sesuatu"
    b "Thanks"
    scene row_visit82 with fade
    b "Ini menyakitkan"
    scene row_visit83 with dissolve
    rm "Hei, apakah kamu baik -baik saja"
    b "Huh"
    scene row_visit84 with dissolve
    rm "Apa yang ingin Anda minum?"
    b "Hai..."
    b "Terserah, silakan air"
    rm "Duduk dan rileks, aku akan segera kembali"
    scene row_visit85 with fade
    "..."
    scene black
    "SEMENTARA ITU"
    scene srd6 with fade
    "..."
    scene srd7 with dissolve
    s "Seseorang mengawasi kami"
    scene srd8 with dissolve
    s "Jangan lihat !!"
    scene srd7 with dissolve
    a "Mari kita meneleponnya"
    s "Tidak kecuali dia membayar"
    if persistent.patch_enabled:
        a "[sname] Dia ayahmu"
        pass
    else:
        a "Anda tidak bisa dipercaya"
        pass
    s "Jadi apa!"
    s "Aku menjualmu kepadanya"
    a "Wow"
    s "Mari kita lakukan sesuatu"
    scene srd29 with dissolve
    d "Apa yang dia lakukan !!"
    scene srd30 with fade
    d "[sname] Apa yang terjadi?"
    a "Kami hanya bersenang -senang"
    scene black
    "SEMENTARA ITU"
    scene row_visit86 with dissolve
    rm "Ini minumanmu"
    b "Err saya tidak ingin minum"
    rm "Saya tahu bagaimana rasanya"
    rm "Itu terjadi pada kebanyakan anak laki -laki saat mereka melihat saya"
    b "Grrrr"
    rm "Minum sesekali, aku akan mengurusnya"
    scene row_visit89 with dissolve
    rm "Datang"
    b "Ah"
    scene row_visit90 with dissolve
    rm "Saya akan mengurusnya"
    rm "Itu kesalahan saya dan saya perlu menyelesaikannya"
    scene row_visit91 with dissolve
    rm "Hmm"
    scene row_visit92 with hpunch
    rm "Ah"
    scene row_visit93 with dissolve
    rm "Ughh"
    scene rowm
    rm "..."
    "..."
    b "Uh"
    rm "Yes"
    "Kembali ke Rowena dan [sname]"
    scene srdan
    a "Gulp"
    s "..."
    d "{i} (Rowena itu menyebalkan) {/i}"
    s "Tunggu jangan selesai sekarang"
    d "Ayo Rowena Ride Me Before I Explode"
    scene rdal with fade
    a "Mhmm"
    "..."
    s "Ahhh"
    scene srd31 with dissolve
    s "Ahh yes"
    scene row_visit94 with fade
    b "Ahh"
    rm "Tetap?!"
    b "Yes"
    rm "Go"
    b "Apa?"
    rm "Just leave"
    scene black
    "..."
    if robmvisit >= 1:
        pass

    elif mrob ==0:
        scene vch4 with fade
        $ mrob = 1
        $ persistent.unlock_71 = True
        m "Saya membutuhkan bantuan Anda Elaine"
        e "Apa yang salah begitu awal?"
        m "Dimana Rob?"
        e "Di sini kenapa?"
        m "Bolehkah saya meminta bantuannya?"
        e "Rob, tolong datang"
        scene vch5 with dissolve
        r "Apa itu?"
        scene vch6 with dissolve
        m "Saya ingin Anda pergi ke alamat ini"
        r "Untuk apa?"
        m "Saya curiga tentang sesuatu dan saya perlu mengkonfirmasi keraguan saya"
        m "Bisakah Anda melakukannya untuk saya?"
        r "Sekarang?"
        m "Ya jika Anda tidak keberatan"
        scene vch7 with dissolve
        e "[mname] Katakan padaku apa masalahnya"
        e "Saat Rob bersiap"
        pass
    else:

        scene vch4 with fade
        $ persistent.unlock_71 = True
        m "Saya membutuhkan bantuan Anda Elaine"
        e "Apa yang salah begitu awal?"
        m "Dimana Rob?"
        e "Di sini kenapa?"
        m "Bolehkah saya meminta bantuannya?"
        e "Rob, tolong datang"
        scene vch5 with dissolve
        r "Apa itu?"
        scene vch6 with dissolve
        m "Saya ingin Anda pergi ke alamat ini"
        r "Untuk apa?"
        m "Saya curiga tentang sesuatu dan saya perlu mengkonfirmasi keraguan saya"
        m "Bisakah Anda melakukannya untuk saya?"
        r "Sekarang?"
        m "Ya jika Anda tidak keberatan"
        scene vch7 with dissolve
        e "[mname] Katakan padaku apa masalahnya"
        e "Saat Rob bersiap"
        pass

scene phardon6 with fade
b "Ahh"
m "Huh"
m "Apakah kamu baik -baik saja sayang?"
b "Aku tidak tahu"
m "Apa yang salah, katakan padaku"
b "Kami berada di kolam renang dan tiba -tiba ini terjadi"
m "Apa yang Anda maksud dengan ini?"
scene phardon8 with dissolve
m "Oh"
if mfuckedsober >= 1:
    m "Lagi!"
    m "Ini adalah kedua kalinya terjadi pada Anda!"
    pass
else:
    scene phardon9 with dissolve
    m "Mungkin sengatan lebah?"
    b "Tidak, tidak ada yang terjadi"
    m "Kenakan kemeja dan biarkan pergi"
    b "Di mana?"
    m "Aku berkata pergi meletakkan bajumu"
    scene phardon10 with fade
    "... Ini Priapism"
    "Ereksi berkepanjangan yang tidak disebabkan oleh gairah seksual"
    scene phardon11 with dissolve
    "Saya tidak bisa memastikan apa yang menyebabkannya"
    "Tapi kemungkinan besar dia minum pil Ed"
    "Hah"
    m "Saya tidak berpikir dia tahu tentang ini"
    m "Tapi apa solusinya"
    "Kami memiliki dua solusi di sini"
    "Entah saya memberinya pil, yang tidak saya rekomendasikan"
    "Karena itu akan memengaruhi ereksi normalnya"
    "Atau kami mencoba untuk memenuhi kebutuhannya"
    m "EMM Bisakah Anda melakukannya di klinik Anda?"
    "Saya minta maaf itu tidak mungkin"
    "Saya tidak melakukan ini"
    m "Apa yang Anda rekomendasikan"
    "Temukan dia seorang gadis panggilan"
    m "Tidak akan terjadi, saya peduli dengan kesehatannya"
    "Sayang, itulah mengapa ada kondom"
    scene phardon12 with dissolve
    "..."
    scene phardon11 with dissolve
    "Selain itu, dia tidak perlu menembusnya"
    "Hanya handjob yang akan dilakukan"
    "Atau melihat ereksinya, dia mungkin membutuhkan dua ejakulasi"
    scene phardon12 with dissolve
    m "Ok, saya akan menemukan satu"
    if mrel >=400:
        $ mfuckedsober = 1
        pass
    else:
        scene ohard with fade
        m "{i} (i \ \ 've get it, i \' ll call elaine) {/i}"
        m "{i} (dia memahami dan akan membantu) {/i}"
        scene black
        "..."
        scene s_efuck2 with fade
        e "Apa yang salah [mname] Anda membuat saya takut"
        m "Saya ingin Anda bercinta [bname]"
        scene ohard1 with dissolve
        e "Apa?"
        m "Maaf karena ini langsung"
        m "Tapi ada alasannya, dan saya tidak ingin kehilangan waktu"
        m "Dia memiliki masalah medis"
        m "Priapisme atau semacamnya"
        m "Ereksi tanpa henti"
        m "Dokter merekomendasikan ini, atau pil"
        m "Saya tidak ingin memberinya pil"
        m "Jadi saya pikir Anda satu -satunya pilihan yang saya dapatkan"
        scene ohard2 with dissolve
        e "Oke, tapi kamu akan membayar saya kan?"
        e "kamu tahu itu"
        m "Of course"
        scene ohard3 with dissolve
        m "ELAINE! Kondom ok?"
        m "Atau aku akan membunuhmu"
        e "Sure"
        m "Saya ingin melihat kondom yang digunakan"
        e "OK"
        m "Semoga beruntung"
        e "Kepadanya, bukan aku"
        m "Yeah"
        scene ohard4 with dissolve
        m "{i} (kami akan melihat) {/i}"
        scene s_efuck6 with fade
        e "Hi [bname]"
        b "Ahhh hi"
        e "Saya di sini untuk ..."
        b "Aku tahu"
        e "Kamu tahu?"
        b "Ya [mname] memberitahuku"
        e "Baiklah, mari kita lakukan ini"
        scene ohard5 with dissolve
        e "Huh"
        scene ehrd
        e "Ahhh"
        b "Grr"
        "..."
        e "Ah shit"
        scene ohard6 with dissolve
        e "Please"
        b "Bangun"
        scene estd
        e "Ahhh"
        "..."
        e "Mmmm"
        "..."
        b "..."
        scene ohard7 with hpunch
        b "Ahhhhhhh"
        scene ohard8 with fade
        e "Ahh"
        e "Bagus yang saya ingat, saya perlu mendapatkan kondom dari tas saya"
        scene ohard9 with fade
        e "Ini kondom Anda"
        m "Dan di sini uang Anda"
        scene ohard10 with fade
        m "Semuanya akan baik -baik saja sayang, cobalah tidur sekarang"
        b "..."
        jump jenopenscenes


    scene phardon13 with fade
    b "Ahhh"
    b "Apa yang kita lakukan di sini?"
    m "Duduk dan rileks, aku akan memberitahumu"
    m "Hapus celana pendek Anda"
    scene phardon14 with dissolve
    m "Tolong ambilkan saya dua minuman terkuat Anda"
    m "Saya ingin terbuang dengan cepat"
    scene phardon15 with fade
    b "Ahhh"
    m "Drink"
    b "Mengapa Minum Sekarang?"
    b "Saya tidak dalam mood"
    m "Minum itu akan membuat Anda merasa lebih baik"
    m "Dan berbaring"
    m "Dengarkan Sayang ..."
    m "Apa yang akan saya lakukan selanjutnya ..."
    m "Adalah memastikan Anda baik -baik saja"
    m "Dan hanya itu"
    m "Saya harap Anda mengerti"
    scene phardon16 with dissolve
    b "Uh"
    scene phardon17 with dissolve
    m "..."
    m "{i} (itu sulit seperti batu) {/i}"
    m "Bagaimana jika saya melakukan ini"
    scene phardon18 with dissolve
    b "Ahh"
    m "{i} (ini bekerja \ 'T) {/i}"
    scene phardon18a with dissolve
    m "[bname]"
    m "Duduklah di sisi tempat tidur"
    scene phardon19a with fade
    m "..."
    scene mbj
    "..."
    b "Ahh"
    "..."
    m "..."
    b "Bagus tapi tidak akan bekerja"
    scene mbj00 with dissolve
    m "Biarkan saya mencoba lagi lebih lambat"
    scene mbjsl
    "..."
    m "Mhhm"
    b "Persetan itu menyakitkan"
    scene phardon19 with dissolve
    "..."
    scene phardon20 with dissolve
    m "..."
    scene phardon21 with dissolve
    b "..."
    b "Tunggu..."
    scene mblow
    m "..."
    b "Ahh"
    m "..."
    b "Argh"
    scene mblow00 with dissolve
    b "Tidak akan berhasil"
    m "Ok mari kita coba sesuatu yang lain"
    scene beginhos0 with fade
    m "Di lantai dan lambat tolong"
    b "Yes"
    m "Anda \ 'kembali mabuk [bname], tolong jangan gila"
    scene beginhos with dissolve
    m "..."
    scene hos
    "..."
    m "Ahhh"
    b "Grrr"
    m "Slowly"
    m "Ahhh"
    "..."
    scene endhos with dissolve
    m "Tuhan!"
    m "Let's relax"
    scene endhos1 with fade
    b "It's painful"
    m "Saya tidak tahu apa yang harus dilakukan madu"
    m "{i} (mungkin anal akan membantu?) {/i}"
    m "{i} (karena lebih ketat) {/i}"
    m "{i} (tapi saya akan dihancurkan) {/i}"
    b "Ah fuck"
    m "Honey apa?"
    b "Saya bisa merasakan denyut nadi saya di penis saya"
    m "{i} (Saya kira saya tidak punya pilihan) {/i}"
    scene phardon23 with fade
    m "Ayo sayang"
    scene anam
    "..."
    m "Oh"
    m "[bname]!"
    m "Apakah kamu dekat?"
    m "{i} (mungkin saya harus berbicara kotor padanya) {/i}"
    m "Apakah Anda suka bagaimana perasaan saya?"
    play sound "sounds/jenmoan.wav"
    "..."
    stop sound
    m "Persetan dengan pantatku [bname]"
    scene phardon24 with dissolve
    m "Persetan dengan lebih keras"
    scene anam
    m "Yes"
    m "Yes"
    "..."
    m "Ya ya ya!"
    scene anac
    b "Ahhh"
    b "I'm cumming"
    m "Ya lakukan di pantat saya"
    b "Ahh"
    "..."
    m "..."
    scene phardon26 with fade
    m "Saya akan mencuci dan kami pulang"
    scene phardon25 with fade
    m "Mmm"
    scene ohard10 with fade
    m "Semuanya akan baik -baik saja sayang, cobalah tidur sekarang"
    b "..."
    "..."
    jump jenopenscenes


label jenopenscenes:
    m "Saya akan berada di ruang tamu jika Anda membutuhkan saya"

    scene jopen20 with fade
    if jenopen ==0 and bnomn == 0:
        m "Apakah Anda baik -baik saja [bname]?"
        b "Yes better"
        m "Itu bagus untuk diketahui"
        m "Sit"
        scene jopen21 with dissolve
        m "Saya ingin menanyakan pendapat Anda"
        b "Tentang apa?"
        m "Apa pendapat Anda tentang pekerjaan yang saya lakukan?"
        b "Maksudmu bekerja di klub?"
        m "Yes"
        scene jopen22 with dissolve
        "..."
        b "Ini pekerjaan yang normal, sama seperti pekerjaan lain"
        m "Jadi maksud Anda, tidak apa -apa untuk Anda apa yang saya lakukan?"
        "Pastikan apa yang harus dipilih karena ini akan memengaruhi perilakunya"
        "Jika Anda ingin menjelajahi lebih banyak opsi, simpan di sini"
        scene jopen23 with dissolve
        menu:
            "Tentu saja (NTR)":
                b "Tentu saja tidak apa -apa"
                $ jenopen += 2
                m "Jadi begitu"
                pass
            "Baik itu tergantung pada apa yang Anda lakukan (tidak ada NTR)":

                $ bnomn = 1
                m "Jadi maksud Anda ada hal -hal yang tidak Anda terima"
                b "Maksud saya bukan hanya saya"
                b "Ada hal -hal yang tidak dapat diterima secara umum"
                m "Jadi begitu"
                pass
    else:

        m "Apakah Anda baik -baik saja [bname]?"
        b "Yes better"
        m "Itu bagus untuk diketahui"
        m "Sit"
        pass
    m "Dimana [sname]"
    b "Saya tidak tahu, dia pergi dengan Rowena dan tidak kembali"
    m "Ok"
    b "Anda tidak terlihat baik -baik saja!"
    b "Apa yang salah?"
    scene jopen22 with dissolve
    m "Ya hanya lelah"
    play sound "sounds/mobilering.wav"
    m "Huh itu Elaine"
    m "Saya akan segera kembali"
    stop sound
    scene jopen24 with fade
    m "Begitu, bisakah saya berbicara dengan Elaine?"
    m "Hai Elaine, saya ingin Anda melakukan hal berikut"
    scene black
    "..."
    scene jopen25 with fade
    play sound "sounds/mobilering.wav"
    b "{i} (siapa itu saat ini?) {/i}"
    scene jopen26 with dissolve
    stop sound
    b "Ya halo!"
    b "Siapa itu?"
    "..."
    b "Ah, apakah dia memberitahumu?"
    "..."
    b "Tempat yang sama?"
    b "Rumahnya?"
    b "Halo!?"
    scene jopen25 with dissolve
    b "{i} (sialan aku sangat lelah sekarang?) {/i}"
    b "{i} (mari kita lihat apa yang dia inginkan) {/i}"
    scene black
    "..."
    scene vch19 with fade
    c "Hi [bname]"
    c "Datang"
    b "Hi"
    b "Apa masalahnya?"
    c "Masalah mana?"
    b "Saya mendapat telepon dari seorang gadis bernama Ella"
    b "Dia bilang kamu ingin melihatku dengan mendesak"
    scene vch20 with dissolve
    c "Hah?"
    c "Saya tidak, dan jika saya ingin melihat Anda, saya akan menelepon Anda secara langsung"
    c "Datang"
    scene vch21 with dissolve
    c "Ini Declan, temanku"
    b "{i}(Huh){/i}"
    b "{i} (teman pantat saya) {/i}"
    "Hai"
    b "Hi"
    b "Saya harap saya tidak mengganggu malam Anda"
    c "Tidak, jangan khawatir sayang"
    c "Kami sedang minum"
    scene vch22 with dissolve
    if persistent.patch_enabled:
        c "[bname] adalah keponakan saya"
        pass
    else:
        c "[bname] adalah putra seorang teman saya"
        pass
    "Sebenarnya saya harus pergi"
    c "Mengapa Declan Dini!"
    c "[bname] keren, jangan khawatir tentang dia"
    "Waktu lain"
    "Selamat malam"
    b "Hmm"
    scene vch23 with dissolve
    c "..."
    scene vch24 with dissolve
    c "..."
    b "Apa?!"
    b "Itu bukan salahku"
    c "Saya tidak peduli, Anda harus menebusnya"
    scene vch25 with fade
    c "Lepaskan pakaian Anda dan duduk di sana"
    scene dach
    "..."
    c "Ahh"
    scene vch26 with dissolve
    c "Ahh"
    scene dach
    "..."
    c "Ah yes"
    scene dach
    "..."
    scene vch8 with dissolve
    r "Hah!"
    r "{i} (intuisi wanita tidak pernah salah) {/i}"
    scene vch11 with fade
    c "Terima kasih telah mengunjungi saya [bname]"
    b "Tapi tahukah Anda siapa yang dipanggil?"
    c "Tidak, saya tidak tahu ella"
    c "Apakah Anda memeriksa mungkin itu melinda"
    b "Ide bagus, mungkin"
    b "Apakah Anda pikir dia di rumah sekarang?"
    c "Saya tidak tahu"
    scene black
    "..."
    scene jopen24 with fade
    m "Eh huh!"
    m "Benar-benar!"
    "..."
    m "Ya tetaplah padanya"
    m "Tunggu aku aku datang"
    scene black
    "..."
    scene eveningrob6 with fade
    "..."
    scene eveningrob7 with dissolve
    b "{i} (sialan, tidak ada orang di sini) {/i}"
    b "{i} (lebih baik saya pergi) {/i}"
    scene eveningrob15 with fade
    r "Saya pikir dia mencari Melinda"
    m "Bagaimana Anda tahu?"
    scene eveningrob16 with dissolve
    r "Itu tokonya"
    scene vch27 with dissolve
    m "..."
    r "Kamu tidak apa apa"
    m "..."
    r "Mari kita kembali"
    scene vch28 with dissolve
    r "Apa! Apakah kamu menangis?"
    r "Hei, tunggu!"
    scene vch29 with dissolve
    "..."
    scene vch30 with dissolve
    r "..."
    m "..."
    m "Rob"
    scene vch31 with dissolve
    m "Saya bisa \ 't"
    r "Mengapa?"
    m "Selamat malam"
    r "Tunggu aku akan ikut denganmu"
    scene black
    "..."
    scene sret with fade
    s "{i} (Saya harap dia baik -baik saja) {/i}"
    scene jopen1 with dissolve
    s "Dimana [mname]"
    b "Tidak tahu, saya datang dan dia tidak ada di sini"
    s "Apa kabar hari ini?"
    b "Itu omong kosong"
    s "Mengapa?"
    b "Saya mengalami rasa sakit yang aneh setelah Anda pergi"
    s "Jenis rasa sakit apa?"
    scene sret1 with dissolve
    b "Huh"
    b "Dimana kamu?"
    m "Saya akan tidur"
    m "Jangan mengganggu saya"
    scene jopen1 with dissolve
    s "Apa yang salah?"
    b "Di penis"
    s "Ah, mungkin dari air kolam?"
    b "Aku tidak tahu..."
    scene sret2 with dissolve
    s "Jadi apa yang akan Anda lakukan?"
    scene jopen1 with dissolve
    if srel >=200:
        b "Saya pikir saya akan tidur"
        b "Mungkin di pagi hari menjadi lebih baik"
        s "Apakah Anda mencoba masturbasi?"
        b "Saya tidak ingin itu"
        b "Saya tidak merasakan apa pun di dalamnya"
        s "Saya dapat membantu Anda"
        b "Saya tidak berpikir Anda bisa"
        s "Ikuti saya ke kamar saya setelah 2 menit"
        s "Saya memiliki sesuatu untuk ditunjukkan kepada Anda"
        scene sret3 with fade
        s "Ayo saya akan membantu Anda"
        scene sret4 with dissolve
        s "Bagaimana Anda ingin saya membantu Anda?"
        menu:
            "Dengan pantatmu":
                scene swya
                s "Hmm"
                s "[bname] Sangat besar"
                s "..."
                s "Ahh"
                scene sret8 with dissolve
                "..."
                jump vnmorning
            "Dengan mulutmu":

                scene swym
                s "Hmm"
                s "..."
                s "Uh"
                "..."
                menu:
                    "Menyelesaikan":
                        scene sret6 with hpunch
                        s "Ughh"
                        scene sret7 with fade
                        b "Terima kasih"
                        jump vnmorning
                    "Menghancurkannya":
                        scene sdhr
                        s "Gulp"
                        "..."
                        s "..."
                        "..."
                        scene sret5 with dissolve
                        s "Ughh"
                        scene sret7 with fade
                        $ sdom += 1
                        show screen sdomup
                        b "Terima kasih"
                        hide screen sdomup
                        jump vnmorning
    else:
        b "Saya pikir saya akan tidur"
        b "Mungkin di pagi hari menjadi lebih baik"
        s "Ya ide bagus"
        "Anda setidaknya membutuhkan 200 poin hubungan"
        jump vnmorning

label vnmorning:
    b "Waktu untuk tidur"
    scene broom_day with fade
    b "Mari kita lihat"
    scene rooms_ms with fade
    b "[mname] Kamar atau [sname] atau toilet?"
    call screen jdcorr


label mroomtra:
    scene nwork_going8alt with dissolve
    m "[bname] Apa yang kamu lakukan di sini !!?"
    b "Maaf, saya baru saja memasuki pintu yang salah"
    b "Bisakah saya membantu Anda dengan sesuatu?"
    scene nwork_going9alt with dissolve
    m "Ya, beri saya bra saya dari laci di sana"
    scene nwork_going10 with dissolve
    b "{i} (payudaranya terlihat lebih kuat) {/i}"
    b "{i} (apakah dia melakukan sesuatu?) {/i}"
    b "Sure"
    menu:
        "Beri dia bra yang salah":
            scene nwork_going13alt with dissolve
            m "Bukan yang itu!"
            m "The other"
            b "Ok sorry"
            pass
        "Beri bra yang tepat":

            show screen mrelup
            $ mrel += 2
            b "Here"
            hide screen mrelup
            pass

    scene nwork_going11 with fade
    m "Terima kasih"
    b "Sampai jumpa di malam hari"
    m "Yes"
    jump daytra


label toilettra:
    scene ttra with fade
    b "Hmm"
    b "Sorry"
    scene ttra1 with dissolve
    m "[bname]"
    b "Saya ingin menggunakan toilet tidak tahu Anda di sini"
    m "Anda bisa kembali lagi nanti"
    b "Ok"
    scene room3 with fade
    b "{i} (dia mencukur kakinya) {/i}"
    b "{i} (Saya berharap saya melihat bagaimana dia mencukur vaginanya) {/i}"
    jump daytra


label sroomtra:
    scene sroom_av8 with fade
    b "Selalu membaca?"
    scene sroom_av9 with dissolve
    s "Apa yang kamu inginkan sekarang?"
    b "Breakfast"
    s "Persiapkan Sendiri"
    s "I'm busy"
    b "Untuk berapa lama?"
    s "Saya tidak tahu, mungkin setengah jam"
    b "Oke saya akan menunggu"
    jump daytra



label daytra:
    b "{i} (I \ 'D lebih baik istirahat di aula) {/i}"
    scene b_relax_d with fade
    "..."
    s "Sarapan sudah siap"
    b "Huh"
    scene slunch8 with dissolve
    b "Dingin"
    scene slunch3 with dissolve
    s "Bon appetit"
    b "Thanks"
    b "Jadi apa rencanamu hari ini?"
    s "Saya akan bertemu dengan Rowena di malam hari"
    s "Anda?"
    b "Bisakah aku ikut denganmu?"
    s "No"
    b "Oh"
    b "Mengapa tidak?"
    scene slunch4 with dissolve
    s "Rahasia!"
    s "Hanya bercanda, itu adalah seorang gadis"
    b "Hmm"
    b "Saya seorang gadis"
    scene slunch3v with dissolve
    s "Yeah hahaha"
    b "Ayo"
    s "Mari kita lihat di sore hari"
    scene slunch3 with dissolve
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

    scene slunch7 with fade
    s "Saya akan memikirkannya jika Anda mencuci piring"
    b "Deal"
    scene slunch12 with fade
    "..."
    scene slunch_hot10 with dissolve
    "..."
    scene slunch_hot11 with dissolve
    s "Terima kasih [bname]"
    b "Huh, kamu di sini!"
    scene slunch_hot12 with dissolve
    b "Wow gaun yang bagus"
    s "Hanya ucapan terima kasih telah mencuci piring"
    b "Bisakah saya mendapatkan ciuman?"
    s "Uh huh"
    scene slunch_hot13 with dissolve
    "..."
    scene slunch_hot14 with dissolve
    s "Terima kasih"
    s "Ngomong -ngomong, bagaimana perasaanmu?"
    b "Agak lebih baik, tetapi saya bisa menggunakan bantuan"
    scene slunch_hot18 with dissolve
    if srel >=200:
        s "Bantuan macam apa?"
        b "Untuk menghilangkan rasa sakit saya, Anda tahu"
        s "Hmm datang"
        menu:
            "Handjob":
                scene trahj with fade
                "..."
                scene trahj1 with dissolve
                s "..."
                scene trahj with dissolve
                "..."
                scene trahj1 with dissolve
                "..."
                scene trahj with dissolve
                s "..."
                scene trahj2 with dissolve
                s "Wow!"
                scene dtra with fade
                b "Terima kasih [sname]"
                s "Jangan lupa untuk membersihkan cum Anda dari meja dan sofa"
                pass
            "Biarkan \ duduk":

                scene trasp with fade
                "..."
                s "Ah"
                s "..."
                "..."
                b "Bagus bukankah itu?"
                s "Ahh"
                b "Bangunlah di sini"
                scene trami with dissolve
                s "Ya tekan tempat itu"
                scene trami1 with vpunch
                s "Ah"
                s "Bukan tempat itu [bname]!"
                b "Terlambat saya \ 'm cumming"
                scene dtra with fade
                b "Terima kasih [sname]"
                pass
    else:

        s "Hehe"
        scene slunch_hot19 with dissolve
        s "Lihat yah"
        pass



    if snameworkmelinda ==3:
        b "Er Apakah Anda ingin mengunjungi Melinda sekarang?"
        s "Ya tapi kami membuatnya cepat, saya perlu melihat Rowena nanti"
        b "Tentu, lepaskan"
        s "Saya akan berubah"
        b "Ok"
        scene black
        "..."
        scene melwrk39 with fade
        "..."
        ml "Hai [sname], sangat senang melihatmu"
        ml "Mari kita duduk dan berbicara"
        scene melwrk40 with dissolve
        s "[bname] Memberitahu saya bahwa Anda ingin melihat saya"
        scene melwrk41 with dissolve
        ml "[bname] Bisakah Anda meninggalkan kami sendirian sejenak"
        b "Ok"
        scene melwrk42 with dissolve
        ml "Jadi, saya punya satu klien pribadi dan elit"
        s "..."
        ml "Siapa yang mencari perusahaan untuk perjalanan ibiza -nya"
        s "Ok dan?"
        ml "Dia akan membayar perjalanan Anda dan semua biaya"
        ml "Ditambah sejumlah besar uang"
        s "Berapa harganya?"
        s "Dan untuk berapa hari?"
        ml "Ini selama satu minggu, untuk berapa banyak"
        ml "Dia ingin melihat gadis itu dulu"
        ml "Jadi, jika Anda tidak keberatan saya mengambil beberapa foto Anda"
        ml "Jadi saya bisa menunjukkannya"
        s "Ya kenapa tidak"
        ml "Mari kita pergi ke ruang studio"
        scene melwrk43 with fade
        ml "Bisakah Anda melakukan pose"
        ml "Saya secara pribadi akan mengambil foto untuknya"
        s "Yes"
        scene melwrk44 with dissolve
        "..."
        scene melwrk45 with dissolve
        ml "Bagus, bisakah kita mengambil sesuatu yang lebih terbuka?"
        scene melwrk46 with dissolve
        $ persistent.unlock_75 = True
        s "Hmm"
        ml "Jangan khawatir, Anda bisa mempercayai saya"
        ml "Saya akan membayar Anda untuk foto yang terbuka"
        s "Ok"
        scene melwrk47 with dissolve
        "..."
        scene melwrk48 with dissolve
        ml "Bagus"
        ml "Sekarang lihat aku"
        scene melwrk49 with dissolve
        ml "We're done"
        ml "Mari kita kembali ke ruang tamu dan kita akan membahas detailnya"
        scene melwrk50 with fade
        b "Jadi?"
        s "Dia menawari saya bepergian"
        $ snameworkmelinda = 4
        b "Apa maksudmu bepergian?"
        s "Untuk bepergian dengannya ke Eropa"
        b "Dan apa yang kamu katakan?"
        s "Saya belum tahu, saya akan memikirkannya"
        pass
    else:


        b "Jadi apa rencanamu?"
        s "Aku akan beristirahat sebentar kemudian bertemu Rowena"
        pass


    scene b_relax_d with fade
    b "{i} (apa yang harus dilakukan sekarang?) {/i}"
    b "{i} (hari membosankan) {/i}"
    b "{i} (mungkin saya bisa menelepon Melinda?) {/i}"
    b "{i} (atau elaine?) {/i}"
    b "Hmm"
    scene dtra1 with dissolve
    b "Hah! Anda lebih awal!"
    scene dtra2 with dissolve
    b "{i} (apa yang salah dengannya?) {/i}"
    b "Apa yang salah?"
    scene dtra3 with dissolve
    m "Kemana saja kamu kemarin?"
    b "Apa! Apa maksudmu?"
    scene dtra4 with dissolve
    m "Beri tahu saya!"
    b "Huh"
    scene dtra5 with dissolve
    b "Apa yang kamu bicarakan?"
    m "CHERYL!"
    m "Melinda?"
    m "Anda melihat mereka kemarin kan?"
    scene dtra6 with dissolve
    m "Apa?"
    m "Kucing itu mendapatkan lidahmu?"
    scene dtra6 with hpunch
    b "Anda menguntit saya!"
    m "Anda mengacaukan keluarga ini!"
    m "Anda menusuk saya di belakang !!"
    b "Apa -apaan!"
    m "Keluar dari wajahku!"
    scene dtra7 with dissolve
    b "Bagus!"
    b "Mau mu"
    scene black
    "..."
    scene dtra8 with fade
    b "{i} (i \ 'll call [sname] dan bergabung dengannya di Rowena \' s) {/i}"
    b "{i} (sampai yang satu ini tenang) {/i}"
    scene dtra9 with fade
    $ persistent.unlock_64 = True
    s "Tidak, kami keluar"
    b "{i} (sialan!) {/i}"
    b "{i} ([mname] telah menjadi gila) {/i}"
    s "Mengapa?"
    b "{i} (dimana kamu, aku akan datang untuk bertemu denganmu) {/i}"
    b "{i} (sampai dia tenang) {/i}"
    s "Tunggu kami di Rowena kami akan datang dalam sekitar satu jam atau lebih"
    b "{i}(Ok){/i}"
    scene dtra8 with fade
    b "{i} (Persetan dengan mereka, aku akan memanggil Daniel atau Melinda) {/i}"
    b "{i} (mungkin saya bisa menghasilkan beberapa dolar jika mereka punya pekerjaan) {/i}"
    scene mvr with fade
    d "{i} Tempat yang bagus! {/i}"
    scene mvr2 with fade
    ml "Hi [bname]"
    scene mvr3 with dissolve
    b "Jadi, apa ceritanya?"
    ml "Cerita yang mana?"
    b "Maksud saya, saya ingin mendengar apa yang sebenarnya Anda lakukan, sejujurnya kali ini"
    ml "Saya memiliki agen pemodelan tempat saya mempekerjakan orang"
    ml "Yang suka bekerja sebagai teman untuk orang kaya"
    b "..."
    b "Saya berkata dengan jujur"
    ml "Itu kebenaran"
    ml "Itulah mengapa saya menelepon Anda"
    ml "Anda akan menghasilkan banyak uang dengan saya, dengan ..."
    b "Saya apa?"
    ml "Ukuran Anda"
    b "Hmm"
    ml "Jadi, ingin melakukan beberapa casting tambahan?"
    b "Yep"
    play music "sounds/softpiano.mp3"
    scene dtra10 with fade
    m "{i} (Tuhan Mengapa?!) {/i}"
    scene dtra11 with dissolve
    "..."
    scene dtra12 with dissolve
    stop music fadeout 3.0
    m "{i} (i \ 'll call elaine) {/i}"
    scene dtra13 with fade
    m "{i} (Saya merasa buruk, saya butuh seseorang untuk diajak bicara) {/i}"
    e "Saya tidak bisa datang malam ini [mname]"
    m "{i} (Saya pikir Anda \ 're off) {/i}"
    scene dtra14 with dissolve
    e "Saya, tapi saya punya rencana"
    scene dtra12 with dissolve
    m "{i} (i \ 'll call dan bicar to rob) {/i}"
    scene dtra15 with dissolve
    m "Hi Rob"
    m "Apakah ini saat yang tepat untuk berbicara?"
    r "{i} (Tell Me What \'s Wrong?) {/i}"
    m "Saya merasa sedih, tidak tahu apa yang harus dilakukan"
    r "{i} (Saya pikir yang terbaik adalah menghadapinya) {/i}"
    r "{i} (dan lihat reaksinya) {/i}"
    r "{i} (mungkin dia tidak seburuk itu) {/i}"
    m "Saya melakukannya, dia menyangkal pada awalnya"
    m "Dan kemudian menyerbu"
    r "Hmm dengarkan aku harus pergi, aku akan meneleponmu nanti"
    play music "sounds/dramaticscene.mp3"
    scene dtra10 with fade
    m "{i} (Saya kira saya akan minum sampai saya pingsan) {/i}"
    "..."
    m "{i} (Ini akan memakan waktu lama, saya hampir tidak punya satu seteguk sejak satu jam) {/i}"
    m "{i} (saya bisa minum) {/i}"
    scene dtra16 with fade
    m "{i} (Saya bertanya -tanya di mana [sname]) {/i}"
    stop music fadeout 2.0
    m "{i} (saya bisa berbicara dengannya) {/i}"
    play sound "sounds/doorbell.wav"
    m "{i} (berbicara tentang iblis) {/i}"
    stop sound
    scene eveningrob13 with dissolve
    $ persistent.unlock_72 = True
    m "Rob"
    r "Hi"
    r "Kamu tidak apa apa?"
    m "Saya kira begitu"
    r "Anda terdengar hancur"
    m "Sort of"
    "Dia terisak"
    r "Bisakah saya masuk?"
    m "Yes please"
    m "Bisakah aku memberimu minuman?"
    r "Sure"
    scene dtra17 with fade
    m "Hidup saya benar -benar di luar kendali"
    m "Saya mencoba untuk menjaga kita tetap bersama, tetapi saya telah gagal dalam hal itu, sejak saya meninggalkan Stewart"
    r "Anda meninggalkan Stewart karena Anda tidak bahagia, tetapi apakah Anda dapat menemukan kebahagiaan?"
    m "Tidak ... mungkin saya terlalu egois?"
    r "Sudah terlambat untuk kembali"
    scene dtra18 with dissolve
    r "Mungkin mencari sesuatu yang hilang bukankah cara untuk pergi?"
    scene dtra19
    r "Kita harus mengambil kesenangan apa pun yang datang"
    scene dtra20 with dissolve
    "..."
    "..."
    scene dtra21 with fade
    m "Saya tidak bisa melakukan itu"
    m "{i} (dengan semua yang dilakukan Elaine padanya) {/i}"
    m "{i} (Saya tidak ingin menjadi alasan dia menipu dia) {/i}"
    r "Dengar, saya tahu bahwa Anda ingin lari dari saat ini"
    r "Tapi saya sangat menyukai Anda, dan Anda pantas mendapatkan seseorang untuk melindungi Anda"
    r "Aku di sini untukmu, aku ingin kamu menjadi milikku"
    r "Dan saya ingin Anda menginginkan saya, tanpa hambatan"
    scene dtra22 with dissolve
    m "..."
    m "All right"
    r "Bawa aku ke tempat tidurmu"
    scene dtra23 with fade
    m "{i} (apakah saya membiarkan ini terjadi?) {/i}"
    m "{i} (i \ 'm tidak mabuk) {/i}"
    r "Show me"
    m "{i} (apakah saya memberikan diri saya kepada pria lain?) {/i}"
    scene dtra24 with dissolve
    "..."
    scene dtra25 with dissolve
    r "Anda sangat cantik [mname] {w} sangat seksi"
    r "Carry on"
    scene dtra26 with dissolve
    "..."
    r "Sekarang lakukan aku"
    scene dtra27 with dissolve
    "..."
    scene dtra28 with dissolve
    m "{i} (dia sangat berotot) {/i}"
    r "Apakah kamu menyukainya?"
    scene dtra29 with dissolve
    "..."
    scene dtra30 with dissolve
    r "Keluarkan penisku"
    scene dtra31 with dissolve
    "..."
    scene dtra32 with dissolve
    "..."
    scene dtra33 with dissolve
    "..."
    scene dtra34 with dissolve
    m "{i} (Saya melakukan ini… persetan! Saya pantas bersenang -senang!) {/i}"
    scene dtra35 with dissolve
    m "{i} (fuck! Dia besar) {/i}"
    r "Ayo bawa ini ke tempat tidur, aku akan membuatmu benar sayang"
    scene dtra37 with fade
    m "Oh fuck"
    scene dtra38 with dissolve
    m "Ah"
    scene dtra36 with dissolve
    m "Oh Rob!"
    scene dtra39 with dissolve
    r "Vagina Anda merendam gadis basah {w} Apakah Anda ingin penis ini?"
    r "Pergi lambat ... tolong"
    scene dtra40 with dissolve
    m "{i} (Saya merasa sangat penuh) {/i}"
    m "Ahh"
    r "Santai saja, biarkan aku memberikannya padamu"
    scene dtra41 with dissolve
    m "{i} (ini bagus) {/i}"
    r "Apakah kamu menyukainya?"
    m "Rasanya ... {w} bagus {w} don \ 't stop"
    scene dtra42 with dissolve
    m "Ya Tuhan! .."
    m "Rob, Anda membuat saya cum!"
    scene dtra43 with dissolve
    m "Please"
    m "Don't stop"
    scene dtra44 with fade
    m "Saya pikir saya perlu tidur siang"
    r "Hmm"
    m "{i} (tuhan dia masih rock keras di dalam diriku) {/i}"
    r "Bisakah kita mengubahnya?"
    m "Mhm"
    r "Bisakah Anda naik ke atas?"
    m "Saya akan mencoba, kaki saya merasa lemah"
    scene dtra45 with fade
    r "Lakukan dengan kecepatan Anda sendiri"
    scene dtra46 with dissolve
    m "Oh fuck! Anda sangat dalam!"
    r "Itu gadis yang benar, susu ayam hitamku"
    r "Apakah Anda ingin cum saya?"
    m "Ya Tuhan, ya! Tolong cum untuk saya!"
    r "Di mana Anda menginginkannya?"
    m "Di dalam! Cum di dalam diriku!"
    scene dtra47 with vpunch
    m "Tuhan!"
    r "Sungguh! [mname], aku akan ..."
    scene dtra48 with fade
    m "Mmm"
    scene black
    "..."
    scene dtra49 with fade
    r "Bolehkah saya bertemu dengan Anda lagi?"
    m "SAYA..."
    r "Ingat, Anda dapat menelepon saya kapan saja Anda membutuhkan bantuan"
    m "Selamat malam"
    r "Selamat malam cantik"
    scene dtra50 with dissolve
    m "..."
    scene black
    "..."
    scene dtra51 with fade
    b "{i} (dimana [mname])? {/i}"
    b "{i} (mungkin tidur, saya harap)? {/i}"
    b "{i} (i \ 'll pergi lihat apakah [sname] kembali) {/i}"
    scene dtra52 with fade
    b "{i} (dia belum di sini) {/i}"
    b "{i} (i \ 'll cari kamarnya) {/i}"
    call screen jdssr


label drawerright:
    scene bdrr with fade
    b "Hmm"
    $ edpills = 1
    b "{i} (pil disfungsi ereksi!) {/i}"
    scene bdrr1 with dissolve
    b "{i} (jadi apa yang dia gunakan pada saya) {/i}"
    call screen jdssr

label drawerleft:
    scene bdrl with fade
    b "{i}(Hmmm){/i}"
    $ sdildo = 1
    b "{i} (mungkin saya bisa membuatnya menggunakannya di [mname]) {/i}"
    call screen jdssr


label d_one_tra:
    scene dtra52 with fade
    b "{i} (i \ 'll pergi sebelum dia datang dan memperhatikan bahwa pintunya terbuka) {/i}"
    scene broom_night with fade
    b "Hmm"
    if edpills == 1:
        b "{i} (Saya perlu menemukan cara untuk membuatnya membayar pil ED) {/i}"
        scene broom_camera1 with fade
        b "{i} (mari kita lihat apakah saya dapat menemukan afrodisiak yang bisa saya lawan dengan) {/i}"
        scene aphro with dissolve
        b "{i} (i \ 'll membeli paket blister ini) {/i}"
        $ aphropack = 1
        scene binsta1 with dissolve
        b "Dingin"
        if hallcamera ==2:
            b "Wow bagaimana saya bisa melupakan itu"
            b "{i} (i \ 'll periksa apa yang terjadi selama ketidakhadiran saya) {/i}"
            scene robwm with dissolve
            b "Huh"
            scene binsta1 with hpunch
            b "Fuck"
            scene robwm1 with dissolve
            b "Damn"
            b "{i} (sekarang saya tahu segalanya) {/i}"
            pass
        else:
            b "{i} (Saya berharap ada cara saya dapat memeriksa apa yang terjadi selama ketidakhadiran saya) {/i}"
            b "{i} (mungkin saya bisa menyesuaikan kamera) {/i}"
            b "{i} (let \ 's order one) {/i}"
            b "Hmm"
            b "$ 100 untuk kamera kecil!"
            b "Apa pun!"
            b "Itu harus tiba besok"
            $ hallcamera = 1
            pass

    elif hallcamera ==0:
        b "{i} (Saya berharap ada cara saya dapat memeriksa apa yang terjadi selama ketidakhadiran saya) {/i}"
        b "{i} (mungkin saya bisa menyesuaikan kamera) {/i}"
        b "{i} (let \ 's order one) {/i}"
        b "Hmm"
        b "$ 100 untuk kamera kecil!"
        b "Apa pun!"
        b "Itu harus tiba besok"
        $ hallcamera = 1
        pass
    else:
        pass

    scene broom_night with fade
    b "{i} (Saya kira sudah waktunya tidur) {/i}"
    b "{i} (jika saya bisa) {/i}"
    scene black
    "..."
    scene broom_day with fade
    b "{i} (mari kita lihat apa yang terjadi dengannya) {/i}"
    scene nwork_s_goingno with dissolve
    "..."
    scene nwork_going with dissolve
    b "Selamat pagi"
    m "Selamat pagi"
    scene nwork_goingna with dissolve
    b "{i} (keren, setidaknya dia mengucapkan selamat pagi) {/i}"
    "..."
    b "{i} (apa yang harus dilakukan sekarang?) {/i}"
    if aphropack ==1:
        play sound "sounds/doorbell.wav"
        b "Hmm siapa itu saat ini?"
        stop sound
        scene delivery with fade
        b "Itu afrodisiak, keren"
        $ aphropack = 2
        if hallcamera ==1:
            b "Dan kamera"
        else:
            pass
    elif hallcamera ==1:
        play sound "sounds/doorbell.wav"
        b "Hmm siapa itu saat ini?"
        stop sound
        scene delivery with fade
        b "Ahh itu kamera"
        b "Terima kasih"
        pass
    else:
        pass
    scene b_tv_d with fade
    b "{i} (Saya akan menonton TV sampai [sname] bangun) {/i}"
    scene b_tv_d1 with fade
    "Setelah beberapa jam"
    b "{i} (sepertinya dia akan tidur sepanjang hari jalang) {/i}"
    b "{i} (i \ 'll pergi melakukan beberapa pekerjaan untuk Daniel) {/i}"
    b "{i} (beberapa tunai tambahan tidak terluka) {/i}"
    scene cityd5d with fade
    b "Hai Daniel, saya di sini untuk bekerja"
    dn "Ah bagus"
    dn "Saya memiliki beberapa ponsel yang menunggu Anda"
    b "Tentu, saya akan mengerjakannya"
    dn "Di belakang meja"
    scene cityd8d with fade
    b "Done"
    scene cityd7d with dissolve
    dn "Hebat, ini 00 milikmu"
    $ mny += 100
    $ renpy.notify (_("He gave you 100 $"))
    $ renpy.pause ( 5, 0)
    b "Keren, terima kasih"
    scene cbl with dissolve
    $ persistent.unlock_22 = True
    c "Hi [bname]"
    b "Oh hi"
    c "Apakah Anda ingin ikut dengan saya untuk makan siang?"
    b "Tentu, saya akan menyelesaikan pekerjaan saya dan kami pergi"
    c "Besar"
    scene cityd8d with fade
    b "Done"
    scene cbl1 with fade
    "..."
    c "Biarkan makan di tempat saya"
    scene cbl2 with fade
    b "Terima kasih untuk makan siangnya, itu bagus"
    c "Tell Me [Name]"
    scene cbl3 with dissolve
    c "Bagaimana [mname]?"
    b "{i} (sialan lagi!) {/i}"
    b "Dia bagus"
    scene cbl4 with dissolve
    c "Ok saya akan berubah, tunggu saya"
    b "Mengubah?"
    scene cbl5 with fade
    c "Apakah Anda ingin ikut dengan saya ke pantai"
    b "Ya kenapa tidak"
    b "{i} ([mname] akan membunuhku untuk ini) {/i}"
    scene chbeach with fade
    b "{i} (ISN \ T That The Nude Beach?) {/i}"
    c "Baiklah, mari kita mendapatkan tan"
    scene chbeach1 with fade
    b "{i} (keren) {/i}"
    scene chbeach2 with dissolve
    b "{i}(God){/i}"
    c "Saya pikir saya akan berenang"
    scene chbeach3 with dissolve
    c "Ingin datang?"
    b "{i}(Of course){/i}"
    b "Yes"
    scene chbeach4 with fade
    "..."
    scene chbeach5 with fade
    c "Saya suka tempat ini"
    scene chbeach6 with dissolve
    b "..."
    scene chbeach7 with dissolve
    c "Karena di sini saya bisa mendapatkan cokelat penuh"
    scene chbeach8 with dissolve
    c "Apakah Anda tidak akan menanggalkan pakaian?"
    b "Yes"
    scene chbeach9 with dissolve
    c "Hmm"
    scene chbeach10 with dissolve
    b "Anda sangat cantik"
    c "Terima kasih"
    scene chbeach13 with dissolve
    b "Bolehkah saya mengajukan pertanyaan?"
    c "Shoot"
    scene chbeach14 with dissolve
    b "Kenapa kamu melakukan ini padaku?"
    b "Maksud saya jelas Anda tidak tertarik pada saya atau ingin memiliki hubungan dengan saya"
    b "Ngomong -ngomong, salah dan tidak akan berhasil"
    b "Jadi, apa motifnya?"
    c "Bisakah Anda memberi kami minuman?"
    b "..."
    b "Yes"
    scene chbeach15 with dissolve
    c "Cheers"
    scene chbeach16 with fade
    c "Sekarang lakukan aku"
    scene chbeach17 with dissolve
    b "..."
    c "Not oil"
    b "Lalu bagaimana?"
    c "Maksudku bercinta denganku"
    b "Huh"
    c "Itulah jawaban yang Anda cari"
    c "Mengerti sekarang?"
    b "Sort of"
    c "Jadi tunggu apa lagi?"
    b "Di Sini!!?"
    c "Yes"
    scene chbf
    c "..."
    "..."
    c "Ah yes"
    scene chba
    c "Fuck [bname]"
    "..."
    c "More"
    c "..."
    c "Buat aku cum"
    "..."
    scene chbfi with fade
    b "{i} (Saya perlu pergi sebelum [mname] kembali) {/i}"
    scene black
    "SEMENTARA ITU"
    scene dtra53 with fade
    m "Ya krim yang Anda berikan kepada saya bagus"
    m "Mereka lebih kencang dan lebih besar"
    m "Tapi saya masih mempertimbangkan operasi plastik"
    e "Jika itu yang Anda inginkan"
    e "Tapi Anda perlu mengulanginya setelah beberapa tahun"
    m "Jadi apa?"
    scene dtra54 with dissolve
    m "Ngomong -ngomong, di mana Rob, apakah dia sedang bekerja?"
    e "Yes"
    scene dtra53 with dissolve
    m "Ah Ok"
    m "Baiklah, saya harus pergi"
    e "Mengapa Anda harus pergi, tetap"
    m "Pergeseran kedua saya dimulai sekarang"
    e "Bekerja shift ganda hari ini?"
    m "Ya, saya butuh uang"
    m "Sampai jumpa"
    scene dtra55 with dissolve
    "..."
    scene dtra56 with fade
    b "{i} (dimana dia sampai sekarang?) {/i}"
    b "{i} (setidaknya saya kembali sebelum dia) {/i}"
    scene mstrp
    "..."
    "Ya"
    "..."
    "Saya menginginkannya"
    "Saya menginginkannya juga"
    scene mstripst1 with fade
    "Hai teman -teman, pegang hormon Anda"
    "Satu pria sekaligus"
    "Maksimal dua"
    "Saya akan pergi membayar"
    "Tidak, aku akan pergi, aku memesannya terlebih dahulu"
    scene mstrprob with dissolve
    "..."
    "Kami akan mengambilnya berdua"
    scene mstrprob1 with dissolve
    r "..."
    scene black
    "..."
    scene mstrprob2 with dissolve
    m "{i} (ah itu bagus untuk merasa diinginkan) {/i}"
    scene mstrprob4 with dissolve
    m "Ya..."
    scene mstrprob3 with dissolve
    m "Sembah aku!"
    scene mstrprob5 with dissolve
    "..."
    scene mstrprob6 with dissolve
    "..."
    scene mstrprob7 with fade
    m "Ughh"
    scene dtra56 with fade
    b "{i} (dimana dia?) {/i}"
    scene dtra57 with fade
    b "{i}(Aha){/i}"
    b "{i} (Bicar of the Devil) {/i}"
    b "Selamat malam"
    m "Selamat malam"
    scene dtra58 with dissolve
    b "{i} (bagus, dia duduk, mungkin aku bisa menebus) {/i}"
    b "Masih marah?"
    m "Marah? Apa maksudmu?"
    b "Lihat aku maaf, aku bukan orang jahat"
    b "Bukan apa yang Anda pikirkan"
    m "Saya lelah [bname] Saya ingin tidur"
    b "Mari kita minum satu minuman agar saya bisa menjelaskan diri saya sendiri"
    m "Saya bilang saya ingin tidur"
    b "Aku akan membuatmu secangkir teh"
    scene dtra59 with dissolve
    m "Chamomile please"
    if aphropack == 2:
        b "{i} (hebat, saya \ 'll letakkan afrodisiak di dalamnya) {/i}"
        pass
    else:
        pass
    scene dtra60 with fade
    b "Ini Chamomile Anda"
    m "Terima kasih"
    m "Selamat malam"
    scene dtra61 with fade
    if aphropack == 2:
        b "{i} (sekarang kita menunggu dan melihat) {/i}"
        pass
    else:
        b "{i} (membosankan, saya kira saya akan tidur) {/i}"
        scene eoco with fade
        "Ini adalah akhir dari bab satu"
        "Anda kehilangan beberapa adegan"
        "Kembali dan cari kamar [sname]"
        return

    scene dtra62 with fade
    m "{i} (apa yang salah dengan saya?) {/i}"
    m "{i} (apakah itu aku atau rob) {/i}"
    scene dtra63 with fade
    r "Saya tidak bisa malam ini"
    m "{i} (I Want You Now) {/i}"
    r "Ini hari liburku, besok kita akan memeriksanya"
    m "{i} (no It not your not off, jangan berbohong padaku) {/i}"
    m "{i} (IT \'s Me [mname]) {/i}"
    r "Saya maafkan AC bisa menunggu sampai besok"
    scene dtra62 with fade
    m "Mungkin Elaine ada di sana"
    m "{i} (apa yang salah [mname]) {/i}"
    m "{i} (apakah itu kemaluannya!?) {/i}"
    scene dtra61 with fade
    b "{i} (mungkin pil ini palsu) {/i}"
    scene dtra64 with dissolve
    m "Anda masih terjaga [bname]?"
    b "Yep"
    m "Dimana [sname]?"
    b "Saya tidak tahu"
    m "Oke, ambilkan segelas anggur dan biarkan menonton film"
    b "{i} (dia keren) {/i}"
    b "Right away"
    m "Saya akan memilih sesuatu"
    scene dtra65 with fade
    b "{i} (wow apakah dia memilih ini?) {/i}"
    m "Saya pikir dia akan membunuhnya"
    b "Ya, itulah yang kita sebut cougar"
    scene dtra66 with dissolve
    m "Hahaha, sungguh!?"
    scene dtra67 with dissolve
    m "Sudah kubilang"
    scene dtra66 with dissolve
    m "Tapi, saya tidak mengharapkan hal ini menerkam"
    b "Yes"
    scene dtra68 with dissolve
    m "Ahahaha"
    m "{i} (apa yang salah dengannya!) {/i}"
    b "{i} (hmm mungkin pil mulai berlaku) {/i}"
    b "Baiklah, saya kira ini waktu saya untuk tidur"
    scene dtra69 with dissolve
    m "Tunggu!"
    scene dtra70 with dissolve
    m "Tidak terlalu awal"
    scene dtra69 with dissolve
    m "Saya akan memberi Anda pertunjukan"
    scene dtra71 with dissolve
    m "Mari kita lihat apakah Anda bisa tidur setelah itu"
    scene dtra72 with dissolve
    m "Hmm"
    m "Apakah Anda suka?"
    b "Ya, tapi mari kita minum anggur"
    scene dtra73 with dissolve
    b "Anda bahkan tidak menyentuhnya"
    scene dtra74 with dissolve
    m "Tidak sebelum saya minum air mani Anda"
    scene dtra75 with dissolve
    m "Tolong berikan kepada saya [bname]"
    b "Memberi Anda apa?"
    m "Ayammu"
    scene dtra76 with dissolve
    m "..."
    scene dtra77 with dissolve
    b "Di mana Anda menginginkannya?"
    m "My mouth"
    scene dtra78 with dissolve
    m "Mmm"
    scene dtra79 with dissolve
    m "..."
    scene dtra80 with vpunch
    m "Ahh"
    scene dtra81 with dissolve
    m "Jadikan aku pelacurmu [bname]"
    play sound "sounds/door_openc.wav"
    scene dtra82 with dissolve
    s "Huh"
    scene dtra83 with dissolve
    stop sound
    if persistent.patch_enabled:
        s "Mama! Apa yang sedang kamu lakukan?"
        pass
    else:
        s "Apa yang terjadi?"
        pass
    m "Kami menonton film"
    m "Bergabunglah dengan kami jika Anda mau"
    s "Jenis film apa?"
    s "Porno?"
    scene dtra84 with dissolve
    m "Hmm"
    scene dtra85 with dissolve
    s "Astaga!"
    b "{i} (itu adalah lompatan tercepat) {/i}"
    m "Jangan khawatir tentang dia, dia hanya cemburu"
    s "{i} (dia keluar dari pikirannya) {/i}"
    scene dtra86 with dissolve
    m "Ya [bname] mengisap mereka"
    scene dtra87 with dissolve
    m "Mmmm"
    b "Bangun"
    scene dtra90 with fade
    s "{i} (mungkin dia mabuk) {/i}"
    s "{i} (bercinta, teriakannya sangat menjengkelkan) {/i}"
    scene dtra91 with dissolve
    m "Mmm"
    scene dtra92 with dissolve
    b "Mengisapnya"
    scene dtra93 with dissolve
    b "Aku akan memberimu penisku nanti"
    scene dtra94 with dissolve
    m "{i} (dia membuat saya basah) {/i}"
    scene dtra95 with dissolve
    m "FUCK ME [bname]"
    play sound "sounds/19675.mp3"
    scene dtra96 with dissolve
    m "Suhu!"
    scene dtra97 with dissolve
    m "Ya lakukan aku keras"
    scene dtra98 with dissolve
    "..."
    scene dtra99 with dissolve
    "..."
    scene dtra100 with dissolve
    m "Mhm"
    scene dtra101 with dissolve
    m "Aww Tuhan!"
    scene dtra102 with dissolve
    m "Tolong bor saya"
    scene dtra103 with dissolve
    m "..."
    scene dtra104 with dissolve
    m "Ah"
    scene dtra105 with dissolve
    m "Ahhh"
    scene dtra106 with dissolve
    m "Saya suka ayam itu"
    stop sound
    scene dtra107 with dissolve
    s "Hei tutup ..."
    scene dtra108 with dissolve
    s "... {w} bercinta ..."
    s "Astaga! Anda tidak tahu malu"
    m "Mmmm"
    m "Satu putaran lagi [bname]?"
    b "Yeah"
    scene dtra109 with dissolve
    s "Apa -apaan !!"
    scene eoco with fade
    "Ini adalah akhir dari bab satu"
    "Terima kasih telah bermain"
    "Sampai jumpa di Bab Dua"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
