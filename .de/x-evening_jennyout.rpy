label evening_jennyout:
    scene eom with fade
    b "Hah!"
    m "Hai sayang, saya akan melihat elaine"
    b "{i} (hmm elaine!?) {/i}"
    b "Oke, nikmati waktu Anda"
    if msconvince == 2:
        m "Oh saya ingat ..."
        b "Apa?"
        m "Tidak ada yang sayang, sampai jumpa nanti"
        scene eom_sg with fade
        m "Apa yang sedang kamu lakukan?"
        s "Berencana memeriksa email saya ..."
        m "Lagi email!?"
        $ msconvince = 3
        m "Anda membumi"
        m "Saya ingin Anda tinggal di kamar Anda"
        m "Dan belajar untuk sisa malam itu"
        m "Saya akan memeriksa kemajuan Anda saat saya kembali"
        s "Tetapi"
        m "Tidak tapi"
        m "Atau saya akan mengunci pintu Anda dari luar"
        scene black
        "..."
        pass
    else:


        "..."
        b "{i} (Saya akan mencoba menemukan film porno itu) {/i}"
        pass
    scene eom1 with fade
    b "{i} (Saya harap [sname] tidak akan mengganggu saya) {/i}"
    b "{i} (jauh lebih baik jika dia melakukan hehehe) {/i}"
    scene eom2 with dissolve
    s "Astaga!"
    s "Apa yang kamu tonton!?"
    b "Film romansa"
    scene eom3 with dissolve
    s "Sepertinya lebih dari film porno"
    b "Jadi apa, itu keren"
    if persistent.patch_enabled:
        s "Apakah Anda takut ibu melihat Anda?"
        pass
    else:
        s "Apakah Anda takut [mname] melihat Anda?"
        pass

    b "Dia keluar"
    s "Di mana?"
    b "Dia bilang dia keluar dengan Elaine"
    s "OK"
    b "Saya mendapatkan bir, apakah Anda menginginkannya?"
    s "Yes please"
    scene eom4 with dissolve
    s "..."
    scene eom5 with dissolve
    s "Eww apakah kamu serius!"
    b "Ya, itu bagus"
    scene eom6 with dissolve
    s "It's dirty"
    b "Kotor itu panas"
    b "Saya bisa melakukan ini dengan Anda jika Anda mau"
    scene eom5 with dissolve
    if sbm ==1:
        s "Anda gila"
        b "Tidak, aku tidak"
        s "Dapatkan kami satu bir"
        scene eom9 with dissolve
        "..."
        scene eom10 with dissolve
        s "Tolong ubah"
        b "Mengapa?"
        s "Ubah saja"
        b "Saya tidak menginginkannya"
        s "Lalu aku pergi"
        scene eom11 with dissolve
        b "Apa -apaan!"
        "Masih ada lagi yang bisa dilihat di sini"
        "Mungkin besok malam saat Anda membuka komputer ..."
        "... Anda akan membuka sesuatu untuk Sabtu depan di adegan ini"
        jump mreturn

    elif sbm ==2:
        scene eom7 with dissolve
        "..."
        scene eom8 with dissolve
        s "Menjilati atau jari?"
        scene eom12 with dissolve
        b "..."
        scene eom8 with dissolve
        b "Keduanya!"
        s "Dapatkan kami satu bir"
        scene eom13 with fade
        "..."
        scene eom9 with fade
        "..."
        b "Jadi Anda tidak menjawab saya?"
        s "Jawab Apa?"
        b "Anda ingin jari atau menjilati?"
        b "Atau ini?"
        s "Eww"
        b "Jangan \ t eww saya, saya ingin membuktikan bahwa rasanya menyenangkan"
        if srel >=150:
            s "[bname] Apa yang kita tonton?"
            s "Bagaimana jika [mname] datang?"
            b "Jangan khawatir aku akan meletakkan kunci dari dalam, dia tidak bisa mengubah kunci"
            "..."
            scene eom14 with hpunch
            s "[bname]! Saya pikir saya mabuk"
            b "2 bir?"
            b "Dengan serius?"
            s "Tolong bawa saya ke kamar saya"
            scene eom15 with dissolve
            s "Bawa aku"
            scene eom16 with hpunch
            s "Ahhh"
            b "Hai!"
            s "I'm OK"
            scene eom17 with dissolve
            "..."
            menu:
                "Jilat":
                    scene eom20 with dissolve
                    s "Ahh"
                    scene eom21 with dissolve
                    s "[bname] Apa yang kamu lakukan?"
                    scene eom22 with dissolve
                    s "Ahhh"
                    scene eom23 with dissolve
                    s "[bname]"
                    s "Please stop"
                    b "Mengapa?"
                    scene eom24 with dissolve
                    s "Dia mungkin datang"
                    b "Mari kita lanjutkan di kamar Anda"
                    s "TIDAK!"
                    scene black
                    "..."
                    scene s_etv34 with fade
                    "..."
                    s "{i} (mengagumkan!) {/i}"
                    scene s_etv34 with dissolve
                    $ srbm = 1
                    s "{i} (Anda ingin bermain, mari kita lihat siapa yang akan menang) {/i}"
                    scene black
                    "SEMENTARA ITU"
                    jump mreturn
                "** persetan **":



                    scene eom18 with hpunch
                    s "Hah!"
                    s "[bname] !!"
                    scene eom19 with dissolve
                    s "Berhenti!"
                    "..."
                    scene mreturn_o with hpunch
                    m "[bname] !!"
                    b "Saya .. kami sedang bermain"
                    m "Keluar dari rumah saya!"
                    m "Anda berdua!"
                    scene black
                    "Permainan selesai"
                    return
        else:



            scene eom10 with dissolve
            s "Tolong ubah"
            b "Mengapa?"
            s "Ubah saja"
            b "Saya tidak menginginkannya"
            s "Lalu aku pergi"
            scene eom11 with dissolve
            b "Apa -apaan!"
            "Naikkan poin hubungan Anda menjadi 150"
            jump mreturn
    else:

        s "Anda gila"
        b "Tidak, aku tidak"
        b "Saya akan mendapatkan lebih banyak bir"
        scene eom4 with dissolve
        "..."
        scene eom10 with dissolve
        s "Tolong ubah"
        b "Mengapa?"
        s "Ubah saja"
        b "Saya tidak menginginkannya"
        s "Lalu aku pergi"
        scene eom11 with dissolve
        b "Apa -apaan!"
        jump mreturn


label mreturn:
    scene mreturn0 with fade
    m "Hai [bname]!"
    m "Masih terjaga?"
    b "Yes"
    scene mreturn1 with fade
    m "Ahhhh"
    b "Bagaimana malam itu?"
    m "Tidak buruk, saya kira saya terlalu tua untuk pesta?"
    b "Ingin mengadakan pesta setelahnya?"
    m "Yes"
    if msconvince ==3:
        scene mreturn2 with dissolve
        b "Oh"
        m "Dapatkan aku segelas anggur"
        b "Sure"
        pass
    else:

        scene mreturn2 with dissolve
        s "Apa yang terjadi padanya?"
        b "Oh"
        scene etv_ss with dissolve
        b "Jangan khawatir tentang dia, dia hanya santai"
        m "Bawa saya ke kamar saya [sname]"
        scene mreturn3 with dissolve
        m "Selamat malam Stewart"
        $ msconvince = 1
        b "{i} (Stewart !!) {/i}"
        b "{i} (sialan, saya harus menemukan cara untuk menyingkirkan [sname] untuk waktu berikutnya) {/i}"
        b "{i} (mungkin beri tahu [mname] bahwa dia tidak melakukannya dengan baik dalam studinya) {/i}"
        b "{i} (sementara dia menyiapkan makan malam?! Aku tidak tahu, mari kita lihat) {/i}"
        b "{i} (Saya harus melakukannya sebelum Sabtu malam depan) {/i}"
        b "{i} (kurasa aku akan tidur sekarang) {/i}"
        jump newdays

    scene mreturn4 with fade
    m "Terima kasih"
    scene mreturn5 with dissolve
    b "{i} (apa ...) {/i}"
    scene mreturn6 with dissolve
    "..."
    scene mreturn7 with dissolve
    m "Anda tahu apa yang harus dilakukan?"
    b "Of course"
    scene mreturn8 with dissolve
    m "Oh ya! Aku merindukan tangan itu Stewart"
    b "{i} (Stewart !!) {/i}"
    b "{i} (apakah ini jebakan?!) {/i}"
    b "Halo! Itu aku [bname]"
    m "Hahaha"
    scene mreturn9 with dissolve
    m "Ya benar!"
    m "Seh! Berhenti bermain dan berikan padaku"
    b "Memberi Anda apa?"
    scene mreturn10 with dissolve
    m "Aku bilang berikan padaku !!"
    b "Tapi aku tidak ..."
    m "Berikan padaku!"
    b "..."
    b "Bagaimana dengan [sname]"
    m "Dia membumi"
    m "Dia tidak akan datang"
    b "Bisakah kita pergi ke kamar saya setidaknya?"
    m "Sekarang kamarmu?!"
    b "Sungguh!"
    m "SIT!"
    scene mreturn11 with fade
    "..."
    scene mreturn12 with dissolve
    b "Oh sial!"
    scene mreturn13 with fade
    b "Ahhh"
    scene mreturn14 with dissolve
    b "Ahhh"
    if msexreturn ==0:
        $ msexreturn +=1
        pass

    elif msexreturn ==1:
        b "{i}(Damn){/i}"
        $ msexreturn +=1
        b "{i} (Saya perlu melakukan sesuatu sebelum saya cum) {/i}"
        b "{i} (apa yang Stewart panggil dia!) {/i}"
        b "Sayang!"
        b "Stop"
        b "Sayang! Berhenti!"
        scene mreturn14a with dissolve
        b "Berhenti!"
        m "Apa?"
        b "Kemarilah"
        m "Apa?"
        b "Duduk di atasnya"
        scene mreturn15a with dissolve
        b "Err mungkin Anda harus menghapus celana dalam dulu?"
        b "Berhenti Bergerak!"
        b "{i} (persetan dengan gosok ini membunuhku) {/i}"
        scene mreturn16a with dissolve
        "..."
        scene mreturn17a with hpunch
        b "Aduh, kenapa kamu tidak menghapusnya"
        m "Hapus sendiri"
        b "Oh fuck!"
        scene mreturn18a with hpunch
        b "Ahhh"
        scene mreturn16 with fade
        "..."
        b "{i}(Damn){/i}"
        b "{i} (i \ 'D lebih baik tidur) {/i}"
        jump newdays


    elif msexreturn ==2:
        b "{i}(Damn){/i}"

        b "{i} (Saya perlu melakukan sesuatu sebelum saya cum) {/i}"
        b "{i} (apa yang Stewart panggil dia!) {/i}"
        b "Sayang!"
        b "Stop"
        b "Sayang! Berhenti!"
        scene mreturn14a with dissolve
        b "Berhenti!"
        m "Apa?"
        b "Kemarilah"
        m "Apa?"
        b "Duduk di atasnya"
        scene mreturn15a with dissolve
        b "Err mungkin Anda harus menghapus celana dalam dulu?"
        b "Berhenti Bergerak!"
        b "{i} (persetan dengan gosok ini membunuhku) {/i}"
        scene mreturn16a with dissolve
        "..."
        scene mreturn17a with hpunch
        b "Aduh, kenapa kamu tidak menghapusnya"
        m "Hapus sendiri"
        scene mreturn19a with dissolve
        b "Saya akan melakukannya dengan celana dalam!"
        m "Ya tapi jangan cum \ '"
        b "Aduh leherku !!"
        scene mreturn20a with dissolve
        m "Jangan cum sekarang stewart, aku akan membunuhmu"
        b "Sudah selesai"
        if mrel >=150:
            m "Anda sudah selesai? !!"
            b "Yes"
            m "Maka Anda harus melepaskan saya!"
            m "Atau aku akan membunuhmu!"
            m "Anda tidak pernah membuat saya menikmati sex stewart, saya bersumpah tidak pernah"
            b "Euhh!"
            b "{i} (wow terlalu banyak informasi) {/i}"
            scene mreturn21a with fade
            m "Mhhm"
            scene mreturn22a with dissolve
            m "Ya Stewart itu itu!"
            scene mreturn23a with dissolve
            m "Aaaaah"
            scene mreturn17 with fade
            b "{i}(Awesome){/i}"
            "Itu semua dalam opsi ini"
            jump newdays
        else:
            scene mreturn16 with fade
            m "Bajingan!"
            b "{i}(Damn){/i}"
            b "{i} (i \ 'D lebih baik tidur) {/i}"
            jump newdays

    scene mreturn15 with fade
    "..."
    scene hall_n with fade
    b "{i} (i \ 'D lebih baik tidur) {/i}"
    jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
