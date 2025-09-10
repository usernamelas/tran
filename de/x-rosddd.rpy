label rosddd:
    if rorepeat ==0:
        scene rgts with fade
        d "Hi Rowena"
        $ rorepeat = 1
        a "Eh maaf datang tanpa pemberitahuan"
        a "Tapi saya sedang mencari [sname]"
        a "Mereka mengatakan kepada saya bahwa dia mungkin ada di sini"
        d "Tidak, belum pernah melihatnya"
        a "Oh"
        a "Ok"
        scene rgts1 with dissolve
        a "Damn"
        d "Apa yang salah?"
        a "Tidak ada, saya harus pergi"
        d "Ayo duduk, dan beri tahu saya apa yang salah"
        scene rgts2 with dissolve
        a "..."
        d "Duduk dan beri tahu saya masalahnya, jangan malu"
        scene rgts3 with dissolve
        a "Saya dalam masalah, saya telah meminjam uang"
        a "Dan sekarang saatnya untuk mengembalikannya"
        d "Hmm"
        d "Dan Anda sedang mencari [sname]"
        a "Yes"
        d "Untuk memberi Anda uang?"
        a "Mungkin dia bisa menemukan jalan"
        d "Dan berapa harganya?"
        a "$ 1000"
        d "Hmm"
        d "Jika saya memberi Anda, dapatkah Anda membayarnya kembali?"
        a "Mungkin aku bisa membersihkan rumah untukmu"
        d "Wait here"
        scene rgts4 with fade
        d "Here"
        a "Terima kasih"
        a "Apakah Anda ingin saya mulai membersihkan"
        d "Siapa bilang aku ingin kamu melakukan itu"
        d "Tidak perlu"
        d "Anda dapat mengembalikannya saat Anda melakukannya"
        a "Terima kasih"
        scene rgts5 with dissolve
        d "Huh"
        a "Terima kasih banyak"
        a "Bisakah saya tinggal sebentar dan menggunakan kolam renang?"
        d "Ya, tentu saja"
        scene rgts6 with fade
        "..."
        scene rgts7 with dissolve
        d "Nah, bukan ide yang bagus"
        scene rgts8 with fade
        a "kenapa lama sekali"
        d "Ini"
        a "Ah drinks"
        a "Ya itu sangat panas"
        scene rgts9 with dissolve
        d "Cheers"
        a "..."
        scene rgts10 with dissolve
        a "[sname] sangat beruntung memiliki ayah seperti Anda"
        d "Terima kasih"
        scene rgts11 with dissolve
        d "Huh"
        scene rgts12 with dissolve
        d "Apa?"
        a "Saya tahu Anda ingin melihatnya dengan benar?"
        scene rgts13 with dissolve
        a "Hehehe"
        scene robj
        a "..."
        "..."
        d "Ah ya tenggorokan dalamnya"
        "..."
        d "Yes"
        d "Anak yang baik"
        scene rgts14 with dissolve
        "..."
        scene rgts15 with fade
        a "Kami bahkan sekarang"
        a "Saya pikir saya membayar 000"
        d "Hmm"
        d "Saya kira demikian"
        a "Aku akan pergi sekarang"
        scene rgts16 with fade
        a "Apa yang telah terjadi?"
        s "Sepertinya dia mengubah kunci"
        s "Jangan khawatir kami akan mengetahuinya"
        s "Katakan padaku bagaimana kabarmu"
        scene hall_d with fade
        "..."
        call screen gnav

    elif rorepeat ==1:
        scene rgts with fade
        d "Hi Rowena"
        $ rorepeat = 2
        a "Hi"
        d "Sekali lagi Anda butuh uang?"
        a "Yes"
        d "Berapa harganya?"
        a "$2000"
        scene rgts17 with dissolve
        d "Sebanyak ini?"
        a "Ya maaf karena aku membutuhkannya untuk ibuku, dia sakit"
        scene rgts4 with fade
        d "Here"
        a "Terima kasih"
        scene rgts5 with dissolve
        a "Terima kasih banyak"
        a "Bisakah saya tinggal sebentar dan menggunakan kolam renang?"
        d "Ya, tentu saja"
        d "Aku akan bergabung denganmu nanti"
        scene rgts18 with fade
        "..."
        scene rgts19 with fade
        d "Saya punya minuman"
        a "Terima kasih"
        scene rgts20 with dissolve
        a "Cheers"
        scene rgts21 with dissolve
        a "Terima kasih"
        a "Apa yang Anda inginkan sebagai pengembalian?"
        d "Berlutut"
        scene rdana
        a "Ahh"
        a "AH"
        a "Lambat ... tolong"
        a "Ahhh"
        scene rdana000 with dissolve
        d "$2000 please"
        scene rdanaff
        a "Ahhh"
        "..."
        a "Saya tidak ingin 000!"
        d "..."
        scene rgts22 with hpunch
        a "Ahh"
        scene rgts23 with dissolve
        "..."
        scene rgts24 with fade
        a "Aku akan pergi sekarang"
        scene rgts16 with fade
        s "Jadi?"
        a "Saya sudah mendapatkan kuncinya"
        s "Dingin"
        a "Ya keren pantatku"
        s "Katakan padaku bagaimana kabarmu"
        scene hall_d with fade
        "..."
        call screen gnav

    elif rorepeat ==2:
        scene rgts with fade
        d "Hi Rowena"
        $ rorepeat = 3
        a "Hi"
        d "Sekali lagi Anda butuh uang?"
        a "Yes"
        d "Berapa harganya?"
        a "$2000"
        scene rgts17 with dissolve
        d "Sebanyak ini?"
        a "Ya maaf karena aku membutuhkannya untuk ibuku, dia sakit"
        scene rgts4 with fade
        d "Here"
        a "Terima kasih"
        scene rgts5 with dissolve
        a "Terima kasih banyak"
        a "Bisakah saya tinggal sebentar dan menggunakan kolam renang?"
        d "Ya, tentu saja"
        d "Aku akan bergabung denganmu nanti"
        scene rgts18 with fade
        "..."
        scene rgts19 with fade
        d "Saya punya minuman"
        a "Terima kasih"
        scene rgts20 with dissolve
        a "Cheers"
        scene rgts21 with dissolve
        a "Terima kasih"
        a "Apa yang Anda inginkan sebagai pengembalian?"
        d "Berlutut"
        scene rdanaff
        $ persistent.unlock_67 = True
        a "Ahh"
        a "AH"
        a "Lambat ... tolong"
        a "Ahhh"
        d "000 tolong !!!"
        scene rthrt
        a "Ahhh"
        d "Yeah"
        a "Mmmmm"
        scene rgts26 with hpunch
        "..."
        s "Apa -apaan!"
        d "Apa!!"
        a "Sorry [sname]"
        scene rgts28 with dissolve
        s "Keluar dari sini sebelum aku membunuhmu"
        a "..."
        d "Hai!"
        scene rgts27 with dissolve
        d "Stop it"
        s "Bitch"
        d "Hai!"
        s "Aku tahu dia ingin mencurimu"
        s "Anda memberinya uang, saya tahu"
        d "Saya tidak memberinya apapun"
        s "Jangan berbohong padaku, wanita jalang itu membeli segala macam tas dan pakaian"
        d "Mari kita bicara di dalam"
        scene rgts29 with fade
        s "Saya tidak percaya ini terjadi"
        s "Apa yang dia berikan sebagai imbalan"
        scene rgts30 with dissolve
        d "Hey hentikan"
        d "Don't overthink"
        s "Jangan terlalu memikirkan apa?"
        s "Bahwa Anda meniduri sahabat saya"
        s "Dulu sahabat"
        d "Kemarilah"
        scene rgts31 with dissolve
        d "Anda adalah putri saya"
        s "Apakah saya?"
        scene rgts32 with dissolve
        d "Yes"
        s "Prove it"
        scene rgts33 with dissolve
        d "Senang sekarang?"
        s "Ya, tapi uang membuatku lebih bahagia"
        d "Uang nanti"
        scene rgts34 with dissolve
        s "Ah"
        scene rgts35 with dissolve
        d "..."
        scene rgts36 with dissolve
        "..."
        scene rgts37 with dissolve
        "..."
        scene rgts38 with dissolve
        s "Ahh"
        scene rgts39 with dissolve
        "..."
        scene rgts40 with dissolve
        "..."
        scene rgts41 with fade
        d "Mengambil"
        s "Terima kasih"
        s "Anda menyelamatkan diri sendiri"
        d "Apa maksudmu?"
        s "Maksud saya, saya tidak akan memberi tahu siapa pun tentang apa yang terjadi"
        scene hall_d with fade
        "..."
        call screen gnav

    elif rorepeat >=3:
        scene stst28 with dissolve
        if persistent.patch_enabled:
            s "Ayah!"
            pass
        else:
            s "Seh!"
            pass
        d "Senang bertemu denganmu lagi [sname]"
        scene stst28 with dissolve
        s "Dimana dia?"
        d "Dimana siapa?"
        s "Rowena !!"
        d "[sname] Saya tidak menyukai nada ini"
        scene stst28a with hpunch
        s "Karma akan memukul Anda suatu hari nanti dengan semua kebohongan Anda"
        d "Uh huh"
        s "Biarkan pergi ke kolam renang"
        s "Saya telah membeli bikini baru"
        scene rgts42 with fade
        s "Apakah kamu menyukainya?"
        d "Apa ini [sname]"
        scene rgts43 with dissolve
        d "Anda tidak memakai ini di mana pun selain di sini"
        s "Of course"
        d "Bagaimana dengan yang merah muda yang Anda miliki di hari lain?"
        s "Ah yang itu"
        d "Juga hanya di sini"
        scene rgts44 with fade
        d "Cheers"
        if persistent.patch_enabled:
            s "Cheers Daddy!"
            pass
        else:
            s "Seh!"
            pass
        s "Dan jangan berpura -pura mengkhawatirkan saya"
        s "Lagipula apa yang Anda lakukan"
        d "Apa maksudmu"
        s "Anda tidak peduli dengan saya"
        scene rgts45 with fade
        s "Itu hanya Anda yang ingin menunjukkan kepada Anda pelindung"
        d "Apa?"
        s "Sementara Anda hanya ingin bercinta dengan vagina apapun"
        s "Sama seperti ..."
        scene rgts46 with dissolve
        d "Seperti siapa?"
        s "Nothing"
        s "Maksud saya, Anda hanya dipandu oleh penis Anda"
        scene rgts47 with hpunch
        d "Sungguh, mari kita lihat"
        s "Maksud saya ayolah, Anda terlalu putus asa bahwa Anda membayar untuk bercinta dengan gadis -gadis muda"
        scene rgts48 with vpunch
        d "Benar-benar!?"
        s "Ahahaha tunggu, di mana kacamata saya"
        scene sass
        $ persistent.unlock_68 = True
        s "Ah"
        "..."
        s "Mmm"
        "..."
        scene sdps1 with dissolve
        s "Please"
        d "Siapa yang putus asa?!"
        scene sdps2 with dissolve
        s "Aku! Saya"
        d "Berlutut"
        scene nddt
        d "..."
        "..."
        scene nddt000 with dissolve
        d "..."
        scene nddt
        $ persistent.unlock_69 = True
        "..."
        d "Ahh"
        scene nodd
        "..."
        d "Ugh"
        s "Gulp"
        "..."
        scene noddend with dissolve
        s "Aku bukan putrimu!"
        d "Apa?"
        scene noddend1 with dissolve
        s "Anda tidak memperlakukan putri Anda seperti itu"
        d "Bagaimana saya harus memperlakukannya?"
        s "Anda merusaknya"
        d "Menelan dan kemudian kita akan membicarakannya"
        scene noddend2 with dissolve
        s "..."
        scene rgts49 with fade
        d "Ini uangmu"
        s "Anda seperti [bname]"
        scene rgts50 with dissolve
        d "Apa maksudmu?"
        s "SAYA..."
        s "Maksud saya, Anda semua sama"
        s "Semua pria sama kan?"
        d "..."
        s "Aku akan melihatmu lain kali"
        s "Bye"
        d "Bye"
        scene rvsd0 with fade
        a "Fiuh!"
        a "Dia hampir menangkap kami"
        d "Yeah"
        a "Anda berhutang padaku"
        d "Aku berhutang budi padamu?"
        a "1000 $"
        scene rvsd with hpunch
        a "Ah"
        a "Mengapa?"
        d "Karena Anda adalah penggali emas"
        scene rvsd2 with hpunch
        d "Kemarilah!"
        a "Ahh"
        d "Aku akan mengajarimu pelajaran"
        scene rvsd3 with dissolve
        "..."
        $ persistent.unlock_76 = True
        scene darow with fade
        "..."
        a "Ahhh"
        a "..."
        d "..."
        "..."
        d "Turn"
        scene rvsd4 with dissolve
        d "Grrr"
        scene rvsd5 with dissolve
        "..."
        scene rvsd6 with dissolve
        "..."
        scene black
        "..."
        scene rvsd0 with fade
        d "Ambil ini"
        a "Terima kasih"
        scene hall_d with fade
        "..."
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
