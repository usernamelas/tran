

label bworkday:
    if melsw == 1:
        scene cityd5d with fade
        $ melsw = 2
        b "Hai Daniel, saya di sini untuk bekerja"
        dn "Bagus, tepat waktu"
        b "Jadi apa yang Anda inginkan dari saya beberapa hari yang lalu di pantai?"
        dn "Yah, aku ingin tahu siapa wanita itu bersamamu di pantai?"
        b "Itu adalah teman ..."
        dn "Seorang teman siapa?"
        b "Seorang teman ibuku"
        scene cityd5dwe with dissolve
        dn "Anda bajingan kecil yang licik"
        b "Hahaha"
        b "Apakah Anda ingin saya menghubungkan Anda dengannya?"
        scene cityd5d with dissolve
        dn "Of course"
        b "Aku akan memberitahumu besok"
        b "Saya akan mulai bekerja"
        dn "Ok"
        scene cityd8d with fade
        b "Done"
        scene cityd7d with dissolve
        dn "Hebat, ini 00 milikmu"
        $ mny += 100
        $ renpy.notify (_("He gave you 100 $"))
        $ renpy.pause ( 5, 0)
        b "Keren, terima kasih"
        dn "Alright"
        b "Sampai jumpa!"
        scene black
        "..."
        scene cityde with fade
        e "Apa yang Anda lakukan di sini saat ini [bname]?"
        e "Anda beruntung bahwa Rob Is Not di sini"
        e "Saya juga beruntung"
        b "Saya datang untuk memberi tahu Anda sesuatu"
        e "Apa itu?"
        b "Saya punya pekerjaan untuk Anda"
        e "kerja apa"
        b "Business"
        scene cityde1 with dissolve
        e "Maksud Anda seorang klien"
        b "Ya dan klien penting"
        e "Siapa?"
        b "Daniel"
        e "No [bname]"
        b "Ayo, kita bisa mengetahui sesuatu tentang Cheryl dan Melinda"
        scene cityde2 with dissolve
        e "Baiklah, tapi harganya akan harganya"
        b "Itu tidak ada masalah"
        e "Dan dia harus bijaksana"
        e "Pokoknya saya akan mengelolanya"
        b "Ok sampai jumpa besok"
        jump broom_menu

    elif melsw == 2:
        $ melsw = 3
        scene cityd5d with fade
        b "Hai Daniel, saya di sini untuk bekerja"
        dn "Bagus, tepat waktu"
        b "Saya berhasil mendapatkan Anda Elaine"
        dn "Dengan serius?"
        b "Ya dia menunggumu"
        b "Di alamat ini"
        dn "Dingin"
        b "Tapi dia mengambil uang tunai"
        dn "No problem"
        dn "Berapa harganya?"
        b "Maybe $500"
        scene cityd5dw1e with dissolve
        dn "Oh"
        dn "Bukankah itu terlalu banyak?"
        b "Bukan untuknya, dia sangat bagus"
        b "Pokoknya saya akan memastikan lain kali dia memberi Anda diskon"
        dn "Baiklah, tetaplah di sini sampai saya datang"
        scene black
        "..."
        scene cityd5dw2e with fade
        dn "Hai, [bname] mengirim saya"
        e "Duduk, mari kita bicara dulu"
        scene black
        "Sementara itu"
        scene bworkm with fade
        b "Ini ponsel yang bagus"
        ml "Hi"
        scene bworkm4 with dissolve
        b "Oh hi"
        ml "Dimana Daniel?"
        b "Dia..."
        b "Dia keluar, aku tidak tahu"
        ml "Hmm"
        if melmeeting >= 4:
            b "Bagaimana ponsel Anda yang saya perbaiki terakhir kali"
            ml "Masih sempurna tapi saya terus mendapatkan beberapa pemberitahuan yang tidak diinginkan"
            ml "Mungkin Anda bisa memperbaikinya saat saya menunggu Daniel"
            pass
        else:
            b "Apakah Anda memiliki sesuatu untuk diperbaiki?"
            ml "Sebenarnya ya, mungkin Anda dapat membantu saya dengan ponsel saya"
            b "Apa masalahnya"
            ml "Saya terus mendapatkan beberapa pemberitahuan yang tidak diinginkan"
            ml "Mungkin Anda bisa memperbaikinya saat saya menunggu Daniel"
            pass
        b "Bisakah saya melihatnya?"
        scene bworkm3 with dissolve
        b "Hmm"
        b "Mari kita lihat"
        "..."
        scene cityd5dw3 with dissolve
        "..."
        scene cityd5dw4 with dissolve
        b "Hmmm"
        scene black
        "Kembali ke Daniel"
        scene dfe
        e "Ahhh"
        "..."
        dn "..."
        scene efd
        e "Oh god"
        "..."
        dn "Yes"
        scene black
        "..."
        scene cityd5dw5 with fade
        ml "Terima kasih"
        b "Itu mudah"
        scene cityd5dw6 with dissolve
        dn "Oh tepat waktu, mari kita pergi makan siang"
        ml "Kemana saja kamu?"
        dn "Err"
        dn "Saya pergi untuk membeli beberapa bagian"
        ml "Kenapa saya tidak tahu tentang itu? Dan di mana bagian -bagiannya"
        dn "Saya baru saja memeriksa harga"
        scene cityd5dw7 with dissolve
        ml "Anda tinggal di sini, saya pergi makan siang dengan [bname]"
        scene cityd5dw8 with fade
        ml "Jadi beri tahu saya [bname]"
        if persistent.patch_enabled:
            ml "Bagaimana kabar ibumu"
            pass
        else:
            ml "Bagaimana [mname]"
            pass
        b "Kamu kenal dia?"
        ml "Tentu saja dia bekerja untuk saya"
        b "Maksudmu ..."
        ml "Ya saya memiliki klub juga"
        ml "Yes"
        scene cityd5dw9 with dissolve
        b "..."
        ml "Pelayan, tolong periksa"
        scene cityd5dw10 with fade
        ml "Bagaimana hubungan Anda dengan [mname]"
        scene cityd5dw11
        b "Huh"
        b "Normal"
        scene cityd5dw10 with dissolve
        ml "Saya butuh bantuan dari Anda [bname]"
        b "Apa itu?"
        ml "Dia selalu menolak untuk bekerja di shift malam"
        ml "Apakah Anda pikir Anda dapat meyakinkannya untuk mengubahnya?"
        ml "Tentu saja tanpa memberitahunya bahwa saya bertanya kepada Anda"
        b "I'll try"
        ml "Lewati toko besok dan beri tahu saya"
        b "Ok"
        ml "Di sini ambil ini, beli diri Anda dan dia sesuatu"
        $ mny += 500
        $ renpy.notify (_("She gave you 500 $"))
        $ renpy.pause ( 5, 0)
        b "Oh wow terima kasih"
        b "Sampai besok"
        scene cityd5dw12 with dissolve
        b "{i} Mungkinkah dia ingin dia bekerja seperti Elaine? {/i}"
        "..."
        b "{i} Tentu saja {/i}"
        b "{i} bercinta dia, aku tidak akan membantunya {/i}"
        b "{i} i \ 'll pergi membeli sesuatu untuk [bname] {/i}"
        scene btique with fade
        "Hai bagaimana saya bisa membantu Anda?"
        b "Apa yang Anda punya sepatu?"
        "Kami memiliki pasangan Valentina yang bagus ini"
        scene valy
        b "Hmm"
        "$ 500"
        b "Oh"
        b "Dan pakaian dalam?"
        "Yang ini"
        scene mbdolly
        "$ 200"
        b "Hmm Ok"
        menu:
            "Saya akan mengambil sepatunya":
                $ valshoes = 1
                scene btique with fade
                "Ini dia"
                b "Thanks"
                pass
            "Saya akan mengambil pakaian dalam":

                $ dollnightw = 1
                scene btique with fade
                "Ini dia"
                b "Thanks"
                pass

        "Terima kasih"
        "Datang lagi"
        jump broom_menu

    elif melsw == 4:
        $ melsw = 5
        b "Hai Daniel, saya di sini untuk bekerja"
        dn "Hebat, mari kita mulai"
        scene bworkm4 with dissolve
        ml "Hi guys"
        b "Hi"
        dn "Hi"
        ml "[bname] Ikut denganku, aku perlu berbicara denganmu"
        dn "Huh"
        scene cityd5dw10 with fade
        ml "Begitu juga Anda meyakinkannya"
        b "Err saya mencoba"
        ml "Maksudmu dia menolak?"
        b "Dia akan mempertimbangkannya"
        ml "Mungkin Anda tidak berusaha keras"
        b "Maybe"
        ml "Lewati toko besok dan beri tahu saya"
        b "Ok"
        ml "Di sini ambil ini, beli diri Anda dan dia sesuatu"
        $ mny += 500
        $ renpy.notify (_("She gave you 500 $"))
        $ renpy.pause ( 5, 0)
        b "Oh wow terima kasih"
        b "Sampai besok"
        b "{i} fuck it i non \ 't membeli apapun {/i}"
        b "{i} i \ 'll baru saja datang besok dan mengatakan hal yang sama {/i}"
        jump broom_menu

    elif melsw == 5:
        $ melsw = 6
        b "Hai Daniel, saya di sini untuk bekerja"
        dn "Hebat, mari kita mulai"
        scene bworkm4 with dissolve
        ml "Hi guys"
        b "Hi"
        dn "Hi"
        ml "[bname] Ikut denganku, aku perlu berbicara denganmu"
        dn "Huh"
        scene cityd5dw10 with fade
        ml "Begitu juga Anda meyakinkannya"
        b "Err saya mencoba"
        ml "Maksudmu dia menolak?"
        b "Dia akan mempertimbangkannya"
        ml "Mungkin Anda tidak berusaha keras"
        b "Maybe"
        ml "Apakah Anda suka pantai?"
        b "Ya Mengapa?"
        ml "Saya merindukan tan saya"
        ml "Ingin ikut dengan saya?"
        b "Hmm"
        b "Of course"
        scene cityd5dw13 with fade
        ml "Tempat yang bagus, bukankah itu?"
        b "Yeah"
        ml "Mari kita kecokelatan"
        scene cityd5dw14 with dissolve
        ml "Itu pantai yang indah"
        b "Yes"
        b "{i} dia pikir saya tidak tahu tempat ini {/i}"
        ml "Jadi apa yang diperlukan untuk meyakinkan [mname]"
        b "Banyak uang"
        ml "Saya kira tidak demikian"
        scene cityd5dw15 with dissolve
        b "Kenapa kamu bilang begitu?"
        ml "Saya telah memberi Anda dan saya dapat memberi Anda lebih banyak lagi"
        ml "Itulah mengapa saya tidak berpikir itu masalahnya"
        b "Errr"
        scene cityd5dw16 with dissolve
        ml "Mungkin Anda bisa memberi tahu saya sesuatu yang bisa saya gunakan untuk meyakinkannya"
        b "Kesalahan seperti apa?"
        ml "Saya tidak tahu, Anda memikirkannya"
        b "Ok"
        ml "Follow me"
        scene cityd5dw17 with fade
        b "Jadi?"
        scene cityd5dw18 with dissolve
        ml "..."
        scene cityd5dw19 with dissolve
        ml "Anda tahu [bname] Saya suka pria seperti Anda"
        b "Seperti saya apa?"
        scene cityd5dw20 with dissolve
        ml "Seperti ini"
        ml "Oh besar!"
        ml "Anda tahu apa yang saya ingin hal ini lakukan?"
        b "Apa?"
        ml "Saya ingin merasa diperkosa olehnya, biarkan roleplay"
        b "Apakah kamu serius?"
        scene cityd5dw21 with dissolve
        ml "Ya, memperkosa saya [bname]"
        b "Apakah ini nyata?"
        ml "Saya menyukainya"
        scene cityd5dw22 with dissolve
        ml "Ahh ya robek bagian atas itu"
        scene cityd5dw23 with dissolve
        ml "Yeah"
        ml "Biarkan permainan peran, apa pun yang saya katakan untuk tidak Anda lakukan, Anda melakukannya"
        ml "Jernih?"
        b "All right"
        ml "Tolong jangan bercinta denganku"
        scene cityd5dw24 with dissolve
        "..."
        ml "Ah no"
        ml "Jangan memperkosa saya [bname]"
        scene mlba
        ml "Ahh"
        ml "Tolong jangan [bname]"
        scene mlba00
        "..."
        scene mlba
        ml "Ahh"
        "..."
        scene cityd5dw25 with dissolve
        ml "Jangan memperkosa saya [bname]"
        ml "Saya mohon Anda"
        scene cityd5dw27 with dissolve
        b "Ahhh"
        ml "Terima kasih sayang"
        scene black
        "NANTI"
        scene cityd5dw26 with fade
        "Permisi anak muda"
        b "Huh"
        scene cityd5dw28 with dissolve
        "Saya melihat apa yang Anda lakukan pada wanita di belakang pepohonan"
        b "Telah melakukan! Apakah apa?"
        scene cityd5dw29 with dissolve
        "Ini"
        scene cityd5dw30 with dissolve
        b "Tidak Tidak, Anda tidak mengerti"
        b "Bukan apa yang Anda pikirkan"
        ml "I \ 'm maaf [bname]"
        scene cityd5dw31 with dissolve
        b "Huh"
        ml "Saya harus menemukan cara bagi Anda untuk membantu saya"
        b "Tetapi"
        ml "Saya takut sekarang Anda tidak punya pilihan selain membantu saya dengan [mname]"
        b "Tetapi"
        ml "Santai sekarang, temukan cara untuk membantu saya"
        ml "Dan datang besok"
        jump returnfrommelinda

    elif melsw == 6:
        $ melsw = 7
        b "Hai Daniel, saya di sini untuk bekerja"
        dn "Hebat, mari kita mulai"
        scene bworkm4 with dissolve
        ml "Hi guys"
        b "Hi"
        dn "Hi"
        ml "[bname] Ikut denganku, aku perlu berbicara denganmu"
        dn "Huh"
        scene cityd5dw10 with fade
        ml "Pantai?"
        b "Yes"
        scene cityd5dw32 with fade
        ml "Jadi?"
        ml "Apakah Anda memiliki sesuatu untuk diceritakan kepada saya?"
        scene cityd5dw33 with dissolve
        b "Aku tidak tahu"
        b "Sejujurnya saya tidak bisa berbuat apa -apa"
        ml "Bukankah ada yang bisa Anda ceritakan tentang dia?"
        ml "Apakah dia punya pacar samping?"
        b "Tidak, saya tidak berpikir begitu"
        b "Dia hanya mengenal orang ini Adam dari klub"
        ml "Pelayan?"
        b "Ya saya pikir dia seorang pelayan"
        ml "Baiklah, hal lain?"
        b "Tidak, saya tidak punya yang lain"
        scene cityd5dw34 with dissolve
        ml "Lihat [bname] Saya mencoba membantu Anda"
        ml "Jadi Anda tidak membusuk di penjara untuk kalimat pemerkosaan"
        b "..."
        b "{i} Mungkin aku bisa memberitahunya tentang hal -hal yang aku lakukan dengannya saat dia mabuk? {/i}"
        b "{i} tapi dia tidak akan percaya padaku {/i}"
        ml "Apa yang kamu katakan?"
        b "Hmm"
        b "Saya tidak bisa, maksud saya tidak ada yang bisa saya lakukan"
        scene cityd5dw35 with fade
        ml "Suit yourself"
        b "{i} fuck! {/i}"
        b "Wait"
        ml "Pikiran berubah?"
        b "Saya akan menunjukkan tempat"
        b "Dan..."
        ml "Dan apa?"
        b "Follow me"
        scene cityd5dw17 with fade
        ml "Jadi?"
        b "Terkadang kami datang ke sini setelah pantai"
        ml "Dan apa yang terjadi di sini?"
        b "Saya tidak tahu, tapi dia meninggalkan kita untuk sementara waktu"
        b "Dan saya selalu berpikir dia bertemu seseorang secara diam -diam"
        b "Jadi jika Anda beruntung Anda mungkin ... tangkap dia ..."
        ml "Baiklah, itu memberi Anda lebih banyak waktu"
        ml "Mari kita lihat"

        ml "Aku akan pergi sekarang, dan kamu lebih baik tidak berbohong"
        scene cityd5dw36 with dissolve
        b "{i} fuck! Saya perlu keluar dari {/i} ini"
        b "{i} i \ 'll bawa [mname] Di sini lain kali dan mudah -mudahan ini cukup untuk Melinda {/i}"
        b "{i} dengan cara ini saya merasa kurang guyur {/i}"
        jump broom_menu

    elif melsw >= 9 and bbm ==0:
        scene cityd5d with fade
        b "Hai Daniel, saya di sini untuk bekerja"
        dn "Bagus, tepat waktu"
        dn "Apakah Elaine tersedia?"
        b "Apa maksudmu?"
        dn "Yes"
        b "Saya kira demikian"
        b "Anda tahu alamatnya"
        dn "Dingin"
        dn "Baiklah, tetaplah di sini sampai saya datang"
        scene black
        "..."
        scene cityd5dw2e with fade
        dn "Hi"
        e "Hi Daniel"
        e "Tolong selalu hubungi saya sebelum Anda datang"
        dn "Ya saya pikir begitu"
        scene black
        "Sementara itu"
        scene bworkm with fade
        b "{i} mungkin saya harus ... {/i}"
        scene black
        "..."
        scene iwtm0 with fade
        e "Yes"
        scene iwtm1 with dissolve
        e "Ahh"
        play sound "sounds/Cameraclick.wav"
        "..."
        scene iwtm2 with dissolve
        $ persistent.unlock_48 = True
        stop sound
        dn "Hah!"
        dn "[bname] Mengapa?"
        scene iwtm with dissolve
        b "Aku akan memberitahumu nanti"
        $ bbm = 1
        dn "Apa -apaan!"
        dn "Tolong pergi, jangan tinggalkan toko, sial!"
        b "Baiklah, sampai jumpa di sana"
        scene bworkm with fade
        b "{i} Sekarang saya bisa mengacaukannya dan Melinda {/i}"
        scene iwtm3 with hpunch
        dn "Apa yang baru saja kamu lakukan!?"
        b "Santai, saya melakukan ini karena saya butuh bantuan Anda"
        dn "Bantuan dengan siapa bajingan!"
        b "Dengar, apakah Anda akan bersantai atau kami membuatnya dengan cara yang sulit"
        dn "Speak up"
        b "Saya membutuhkan Anda untuk membantu saya dengan Melinda"
        if persistent.patch_enabled:
            b "Dia memberikan waktu yang sulit untuk ibuku"
            pass
        else:
            b "Dia memberikan waktu yang sulit kepada seorang teman saya"
            pass
        b "Dan aku ingin dia berhenti mengganggunya"
        dn "Dan apa hubungannya dengan saya?"
        dn "Dan mengambil foto saya dengan Elaine?"
        b "Seperti ini saya bisa memastikan Anda akan membantu saya"
        dn "Dan jika tidak? Anda akan menunjukkan foto saya ke Melinda?"
        dn "Apakah kamu bodoh?"
        b "Mengapa?"
        dn "Kedua cara saya kehilangan Anda idiot"
        dn "Ini tidak berfungsi seperti ini"
        b "Ah yes"
        b "... tapi jika saya menunjukkan foto, Anda kehilangan Melinda"
        dn "Hmm"
        scene iwtm4 with dissolve
        dn "Jadi apa yang Anda inginkan dari saya?"
        b "Beri saya beberapa info, beberapa foto dia"
        b "Foto tidak senonoh, apapun, sesuatu yang saya katakan padanya dengarkan jika Anda tidak berhenti saya akan menerbitkan ini"
        dn "{i} sungguh idiot, dia pikir dia bisa melakukan ini pada Melinda {/i}"
        dn "{i} dia akan berakhir di tas {/i}"
        dn "Baiklah, aku akan memberimu beberapa foto seksi, mari kita lihat"
        b "Ya tapi jangan ambilkan aku, foto normal dari rumah"
        b "Saya membutuhkan sesuatu yang dia tidak ingin ada yang tahu"
        b "Saya akan membayarnya"
        dn "Hmm ok pantat pintar"
        dn "Saya tidak butuh uang Anda tetapi 000 akan melakukannya"
        b "Ok deal"
        dn "Keluar dari wajahku"
        jump broom_menu

    elif melsw >= 9 and bbm ==3:
        if persistent.unlock_50 == True:
            b "Hai Daniel, saya di sini untuk bekerja"
            dn "Hi"
            scene bbm with dissolve
            ml "Hi guys"
            b "Hi"
            c "[bname] Apakah Anda ingin bergabung dengan kami untuk makan siang?"
            b "Ermm saya tidak berpikir saya bisa hari ini"
            ml "Ayo, makan siang sebentar"
            c "Ya, sudah lama kami tidak bertemu"
            b "..."
            b "All right"
            scene bbm1 with fade

            c "Biarkan makan di tempat saya"
            ml "Ya kenapa tidak"
            b "..."
            scene bbm2 with fade
            c "Jadi [bname] Anda tahu mengapa Anda ada di sini"
            scene bbm2a with dissolve
            b "Tidak, saya tidak \ 't"
            scene bbm4a with dissolve
            ml "Karena kami ingin mengingatkan Anda tentang apa yang Anda lakukan terakhir kali kepada saya"
            ml "Untuk berjaga -jaga jika Anda masih berpikir untuk memainkan game Anda"
            b "Game yang mana?"
            ml "Anda tahu betul apa yang saya bicarakan"
            c "Baiklah, aku akan meninggalkan kalian berdua sendirian"
            c "Saya tidak akan terlambat"
            b "Err"
            scene bbm18 with fade
            ml "Mulai sekarang, Anda akan melakukan apa yang saya katakan"
            b "Apa?"
            b "Apa maksudmu?"
            ml "Anda akan tahu kapan Cheryl datang"
            ml "Sekarang terdaftar"
            scene bbm19 with dissolve
            ml "Sit"
            scene mfmc
            ml "Anak yang baik"
            "..."
            ml "Yes"
            ml "Yess"
            b "Mmm"
            "..."
            scene bbm20 with dissolve
            b "God"
            scene bbm21 with dissolve
            c "Dengan baik!"
            ml "Tunggu aku belum selesai dengannya"
            scene bbm22 with fade
            "..."
            $ persistent.unlock_59 = True
            scene bbm23 with dissolve
            b "Ah"
            c "Saya ingin mengajarinya pelajaran"
            scene mhjmc
            "..."
            "..."
            c "Ahh"
            "..."
            c "My turn"
            c "Tinggalkan dia Melinda"
            c "Mari kita lihat apa yang bisa dia lakukan"
            scene bbm24 with dissolve
            c "Show me"
            scene cde
            c "Ahh!"
            "..."
            c "Fuck"
            ml "Kuda jantan yang mudah, Anda tidak perlu menghancurkannya"
            "..."
            scene bbm25 with dissolve
            ml "{i} Saya dapat menggunakan orang ini untuk menghasilkan uang {/i}"
            scene black
            "Anda mengambil barang -barang Anda dan kembali ke rumah"
            $ mny += 100
            scene bbm17 with fade
            ".."
            ml "Hey [bname]"
            scene bbm26 with dissolve
            b "Hey"
            ml "Di sini ambil nomor saya"
            $ callmel = 1
            ml "Hubungi saya jika Anda ingin menghasilkan uang"
            b "Kesalahan bagaimana?"
            ml "Hubungi saya dan Anda akan tahu"
            jump broom_menu
        else:



            pass
        scene cityd5d with fade
        b "Hai Daniel, saya di sini untuk bekerja"
        dn "Hi"
        dn "Inilah hal yang Anda minta"
        b "Hal apa?"
        dn "Foto Melinda"
        dn "Tapi aku harus memperingatkanmu, Melinda bukanlah seseorang ..."
        b "Bukankah seseorang apa?"
        dn "Seseorang yang dapat dengan mudah Anda memelintir lengan mereka"
        b "All right"
        dn "Berbicara tentang Iblis"
        scene bbm with dissolve
        ml "Hi guys"
        b "Hi"
        c "[bname] Apakah Anda ingin bergabung dengan kami untuk makan siang?"
        b "Ermm saya tidak berpikir saya bisa hari ini"
        ml "Ayo, makan siang sebentar"
        c "Ya, sudah lama kami tidak bertemu"
        b "..."
        b "All right"
        scene bbm1 with fade

        c "Biarkan makan di tempat saya"
        ml "Ya kenapa tidak"
        b "..."
        scene bbm2 with fade
        c "Jadi [bname] bagaimana [mname]?"
        b "Dia bagus"
        scene bbm4 with dissolve
        ml "..."
        c "Ah ya, kalian tinggal, aku perlu mengumpulkan sesuatu dari toko"
        c "Saya tidak akan terlambat"
        b "Err saya harus pulang ke rumah"
        c "Stay [bname]"
        b "Tidak, saya benar -benar harus pergi"
        c "Pokoknya saya harus berlari, Anda berurusan dengan Melinda"
        scene bbm5 with fade
        b "Baiklah, sampai jumpa"
        scene bbm6 with dissolve
        ml "Saya bilang Anda tinggal"
        scene bbm7 with fade
        ml "Bagaimana hubungan Anda dengan Daniel?"
        b "Bagus, kenapa kamu bertanya?"
        ml "Sit"
        scene melbf
        b "Ahh"
        "..."
        ml "Anda tidak akan cum?"
        b "No"
        "..."
        ml "Up"
        scene bbm8 with fade
        ml "Mari ikut saya"
        scene bbm9 with dissolve
        ml "Bisakah Anda melakukannya dengan baik?"
        b "Yes"
        scene bbm10 with dissolve
        ml "Mari kita coba sebelum Anda cum"
        scene bbm11 with vpunch
        b "Ahh"
        scene bbm12 with dissolve
        b "Pantat sialan ini besar, tidak ada yang akan bertahan lama"
        ml "Yeah"
        ml "Try harder"
        scene bbm13 with vpunch
        ml "Ahhh"
        scene bbm14 with dissolve
        "..."
        scene bbm15 with dissolve
        c "Apa!!"
        c "Di rumah saya dan di kamar saya!"
        scene bbm16 with dissolve
        c "Dapatkan saya dildo saya dari laci"
        ml "Dia menyerang saya"
        c "Ya saya memiliki semuanya di video"
        ml "Berbaring telentang"
        $ persistent.unlock_50 = True
        scene cmt
        "..."
        ml "..."
        c "..."
        scene black
        "Anda mengambil barang -barang Anda dan kembali ke rumah"
        $ mny += 100
        scene bbm17 with fade
        b "{i} Melinda ini berbahaya {/i}"
        b "{i} nah dia hanya jalang {/i}"
        b "{i} atau mungkin Daniel memberitahunya sesuatu {/i}"
        jump broom_menu





    elif melmilin == 1:
        $ melmilin = 2
        scene cityd5d with fade
        b "Hai Daniel, saya di sini untuk bekerja"
        dn "Bagus, tepat waktu"
        dn "Saya perlu menjalankan beberapa tugas"
        b "Jaga toko"
        b "OK"
        dn "Saya tidak akan terlambat"
        scene bworkm with dissolve
        b "{i} mari kita lihat apa yang perlu diperbaiki {/i}"
        ml "Selamat pagi Tuan -tuan"
        scene bworkm1 with dissolve
        b "Selamat pagi"
        ml "Bisakah Anda memeriksa ponsel saya"
        b "Sure"
        b "Apa yang tampaknya menjadi masalahnya?"
        ml "Itu tidak menagih dengan benar"
        b "Baiklah, itu akan siap besok"
        ml "Tidak bisakah Anda memeriksanya hari ini"
        ml "Saya akan ada untuk sementara waktu"
        scene bworkm1a with dissolve
        b "Hmmm"
        scene bworkm1 with dissolve
        b "Ok"
        b "Tolong kembalilah 2 jam"
        scene bworkm2 with fade
        b "Hmm"
        b "Mari kita periksa baterai"
        scene bworkm3 with fade
        b "Done"
        b "Hmm"
        menu:
            "Periksa file -nya":
                b "{i} let \'s download beberapa file {/i}"
                b "{i} mungkin saya mendapatkan beberapa foto tatas lezat {/i}"
                scene bworkm2 with dissolve
                $ melindafiles = 1
                $ persistent.unlock_10 = True
                b "Saya akan menghubungkan dan menyalakan semuanya"
                pass
            "Jangan mengambil risiko":

                pass
        scene bworkm4 with fade
        ml "Jadi, apakah ponsel saya siap?"
        b "Ya, ini dia"
        ml "Berapa harganya?"
        b "50 $"
        ml "Ini dia"
        scene bworkm5 with dissolve
        b "Terima kasih"
        ml "Bye"
        scene bworkm2 with fade
        b "Mari kita lihat apa lagi yang perlu dilakukan"
        "..."
        scene black
        "..."
        scene cityd7d with fade
        dn "Terima kasih telah merawat toko"
        b "Terima kasih kembali"
        b "Saya melakukan perbaikan tambahan untuk seorang wanita"
        dn "Hebat, ini 00 milikmu"
        $ mny += 100
        $ renpy.pause ( 5, 0)
        b "Keren, terima kasih"
        dn "Alright"
        b "Lihat yah!"
        "..."
        jump broom_menu

    elif melmilin >= 2 and melindafiles >=1:
        if melmeeting <=2:
            scene citymel with fade
            $ melmeeting += 1
            b "{i} (oh ini adalah wanita telepon) {/i}"
            b "{i} (Saya harus mencari tahu apakah mereka terkait) {/i}"
            pass
        elif melmeeting == 3:
            scene citymel1 with fade
            $ melmeeting += 1
            b "{i} (sialan, dia baru saja keluar, aku sangat tidak beruntung) {/i}"
            b "{i} (Saya harus mencari tahu bagaimana mereka terkait) {/i}"
            pass
        elif melmeeting == 4:
            scene citymel2 with fade

            $ melmeeting += 1
            b "{i} (keren, dia di dalam) {/i}"
            b "{i} (Saya harus memiliki teleponnya untuk sekali lagi) {/i}"
            scene citymel3 with dissolve
            b "Hai Daniel, saya di sini untuk bekerja"
            b "Oh hai, saya pikir saya sudah memperbaiki ponsel Anda terakhir kali"
            b "Saya pikir saya telah mengacaukannya karena saya lupa memunculkan ingatan"
            b "Saya harap Anda tidak mengeluh kepada bos saya"
            b "Jika Anda tidak keberatan, 5 menit saya akan memperbaikinya"
            scene citymel4 with dissolve
            $ persistent.unlock_11 = True
            ml "Tidak, tidak, semuanya baik -baik saja, jangan khawatir"
            ml "Thanks"
            b "{i} (sialan saya harus mencari tahu sesuatu) {/i}"
            scene citymel2 with dissolve
            ml "Baiklah Daniel, terima kasih"
            dn "Sampai jumpa"
            scene cityd5d with dissolve
            b "Jadi ... saya di sini untuk bekerja"
            pass
        else:

            if melmeeting >= 4 and willmeeting ==0:
                scene cityd5d with fade
                b "Hai Daniel, saya di sini untuk bekerja"
                dn "..."
                "Hai Daniel"
                scene cityd5dw with dissolve
                dn "H ... Hai"
                $ willmeeting = 1
                b "Hah!"
                scene cityd5dw1 with dissolve
                "Apa kabarmu?"
                "Saya melihat Anda memiliki toko sendiri sekarang"
                dn "Yes"
                "Dan bagaimana Melinda?"
                dn "Bagus bagus"
                "Katakan padanya aku sudah lewat dan menyapa"
                scene cityd5dw with dissolve
                dn "Sure"
                "Selamat tinggal"
                scene cityd5dw2 with dissolve
                b "So"
                b "Daniel? Kamu tidak apa apa?"
                scene cityd5d with dissolve
                dn "Yes"
                b "Siapa pria ini dan mengapa terlihat seperti kamu melihat hantu"
                dn "..."
                b "Saya minta maaf karena telah bertanya tetapi ada sesuatu yang salah"
                dn "Dia ..."
                dn "Dia adalah suami dari pemilik toko ini"
                b "Ah jadi kamu bukan pemiliknya?"
                dn "Baik saya semacam itu, tapi wanita yang datang untuk memperbaiki teleponnya"
                dn "Adalah pemilik yang sebenarnya"
                scene bworkm1bw with dissolve
                b "{i} (aha! Jadi itu suaminya) {/i}"
                b "{i} (dan siapa dia ke Daniel) {/i}"
                b "{i} (Mungkinkah dia hanya berselingkuh dengannya) {/i}"
                scene cityd5d with dissolve
                b "{i} (tidak, tidak mungkin, Anda tidak berselingkuh dengan seseorang dan memiliki toko bersama) {/i}"
                b "{i} (ada sesuatu yang lain) {/i}"
                dn "[bname]"
                dn "So"
                b "Ya, jadi seperti yang saya katakan saya di sini untuk bekerja"
                pass

            if melmeeting >= 4 and willmeeting ==1 and cherylintrodone >= 1 and cherylfoundout ==0:
                scene cityd5d with fade
                $ cherylfoundout = 1
                b "Hai Daniel, saya di sini untuk bekerja"
                dn "Ah bagus"
                $ buy_s_phonecounter += 1
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
                b "Aku akan pergi sekarang"
                jump cherylsawmc
            else:

                if dphonestolen ==0 and cherylevent ==1:
                    scene cityd5d with fade
                    b "Hai Daniel, saya di sini untuk bekerja"
                    dn "Hai, Anda bisa mulai"
                    b "Ok"
                    scene citddp1 with dissolve
                    "Selamat pagi"
                    dn "Selamat pagi"
                    "Bisakah Anda memeriksa ponsel ini"
                    dn "Ya yakin apa yang salah dengan itu?"
                    scene citddp with dissolve
                    b "{i} (hmm adalah telepon Daniel) {/i}"
                    b "{i} (ya!) {/i}"
                    menu:
                        "Cobalah untuk mengunduh data dari ponselnya":
                            $ dphonestolen = 1
                            scene citddp2 with dissolve
                            $ renpy.notify (_("YOU DOWNLOADED THE PHOTOS"))
                            pass
                        "Lanjutkan pekerjaan Anda":

                            pass
                    scene cityd8d with fade
                    b "Done"
                    scene cityd7d with dissolve
                    dn "Hebat, ini 00 milikmu"
                    $ mny += 100
                    $ renpy.notify (_("He gave you 100 $"))
                    $ renpy.pause ( 5, 0)
                    b "Keren, terima kasih"
                    b "Aku akan pergi sekarang"
                    dn "Alright"
                    b "Lihat yah!"
                    "..."
                    jump broom_menu

                elif dphonestolen ==1 and cherylevent ==1:
                    $ cherylevent = 2
                    scene cityd5d with fade
                    b "Hai Daniel, saya di sini untuk bekerja"
                    dn "Hai, Anda bisa mulai"
                    b "Ok"
                    scene cml with dissolve
                    $ persistent.unlock_22 = True
                    ml "Daniel I \ 'akan pergi makan siang dengan Cheryl"
                    c "Hi [bname]"
                    b "Hi"
                    ml "Hi [bname]"
                    c "Apakah Anda ingin makan siang bersama kami"
                    b "Ya kenapa tidak"
                    scene cml1 with fade
                    "..."
                    scene cml2 with fade
                    b "Bagaimana dengan ponsel Anda"
                    b "Masih bekerja dengan sempurna setelah saya memperbaikinya?"
                    ml "Tidak demikian, itu sedikit tertinggal"
                    b "Saya bisa memperbaikinya untuk Anda"
                    ml "Ini baik -baik saja untuk saat ini, saya akan memberi tahu Anda jika saya mengalami lebih banyak masalah"
                    c "Cheers"
                    b "Cheers"
                    c "Jadi [bname] bagaimana [mname] mengelola kehidupan ini?"
                    b "Dia bekerja"
                    ml "Di mana dia bekerja setelah dia meninggalkan kedai kopi saya?"
                    b "Itu restoran lain di dekatnya"
                    c "Hmm OK"
                    scene cml3 with fade
                    c "Jaga sayang, saya harap saya akan melihat Anda lagi"
                    scene cml4 with dissolve
                    b "Saya berharap begitu juga"
                    scene cml5 with dissolve
                    c "Di sini ambil ini"
                    b "Apa itu?"
                    c "Uang, jangan beri tahu [mname] tentang itu"
                    c "Hanya sedikit bantuan untuk Anda"
                    b "Tidak, aku bersumpah kami baik -baik saja"
                    b "Sudah kubilang dia bekerja"
                    c "Dia mungkin tidak dibayar dengan baik, apa yang bisa dibayar pekerjaan restoran"
                    b "Ini adalah tempat yang sangat mewah, klub bawah tanah membayar dengan baik"
                    scene cml6 with dissolve
                    c "Hmm Ok"
                    c "Sampai berjumpa lagi"
                    "..."
                    jump broom_menu
                else:

                    if ctempted >=1 and Hour >=12 and cherylevent >=6:
                        scene cityd5d with fade
                        b "Hai Daniel, saya di sini untuk bekerja"
                        dn "Hai, Anda bisa mulai"
                        b "Ok"
                        scene cbl with dissolve
                        $ persistent.unlock_22 = True
                        c "Hi [bname]"
                        b "Oh hi"
                        c "Apakah Anda ingin ikut dengan saya untuk makan siang?"
                        b "Tentu, saya akan menyelesaikan pekerjaan saya dan kami pergi"
                        c "Besar"
                        scene cityd8d with fade
                        b "Done"
                        scene cityd7d with dissolve
                        dn "Hebat, ini 00 milikmu"
                        $ mny += 100
                        $ renpy.notify (_("He gave you 100 $"))
                        $ renpy.pause ( 5, 0)
                        b "Keren, terima kasih"
                        b "Sampai jumpa Daniel"
                        jump cherylblunch
                    else:

                        pass
                scene cityd5d with fade
                b "Hai Daniel, saya di sini untuk bekerja"
                pass
    else:
        scene cityd5d with fade
        b "Hai Daniel, saya di sini untuk bekerja"
        pass


    dn "Ah bagus"
    $ buy_s_phonecounter += 1
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
    if buy_s_phonecounter >= 2 and mobilephoneacquired == 0:
        b "Err Daniel?"
        b "Berapa harga ponsel di sana?"
        dn "Oh itu? Ini untuk 100"
        b "Ya ampun!"
        dn "00 untukmu"
        if mny >= 500:
            menu:
                "Beli":
                    $ mobilephoneacquired = 1
                    $ mny -= 500
                    dn "Ini dia Pak Pak"
                    b "Thanks"
                    b "{i} (Saya harus menemukan momen yang tepat untuk diberikan kepadanya) {/i}"
                    b "Lihat yah!"
                    "Berhati -hatilah saat Anda memberikan [sname] ponsel"
                    "Hasil yang berbeda pada waktu yang berbeda"
                    jump broom_menu
                "Tidak sekarang":

                    b "Saya akan memikirkannya"
                    dn "Alright"
                    b "Lihat yah!"
                    "..."
                    jump broom_menu
        else:

            b "Baik saya tidak punya untuk saat ini"
            b "Mungkin lain kali"
            dn "Alright"
            b "Lihat yah!"
            "..."
            jump broom_menu

    elif buy_s_phonecounter >= 3 and camerasacquired == 0:
        b "Err Daniel?"
        b "Berapa banyak kamera di sana?"
        dn "Maksudmu kamera nirkabel?"
        b "Yes"
        scene cityd9d with dissolve
        dn "Hehehe mencoba memata -matai seseorang"
        b "Oh tidak, tidak ada hal semacam itu"
        dn "Ya saya tahu"
        scene cityd7d with dissolve
        dn "00 untukmu"
        if mny >= 200:
            menu:
                "Beli":
                    $ camerasacquired = 1
                    $ mny -= 200
                    dn "Ini kamera Anda"
                    b "Thanks"
                    b "{i} (Saya harus menemukan di mana menginstal yang satu ini) {/i}"
                    b "Lihat yah!"
                    "Anda akan dapat membeli lebih banyak kamera di masa depan"
                    jump broom_menu
                "Tidak sekarang":

                    b "Saya akan memikirkannya"
                    dn "Alright"
                    b "Lihat yah!"
                    "..."
                    jump broom_menu
        else:


            b "Baik saya tidak punya untuk saat ini"
            b "Mungkin lain kali"
            dn "Alright"
            b "Lihat yah!"
            "..."
            jump broom_menu


    elif ticketrequested == 2:
        b "Lihat yah!"
        b "{i} (Saya harus menemukan tempat membeli tiket konser untuk [sname]) {/i}"
        scene cityd2 with fade
        b "{i} (mungkin saya dapat menemukannya di toko serba ada) {/i}"
        scene city_cornerstore with fade
        b "{i} (i \ 'll tanyakan di sini) {/i}"
        scene city_cornerstore1 with dissolve
        b "Hi there"
        "Halo"
        b "Umm apakah Anda kebetulan menjual tiket untuk Taylor Shift?"
        "Ya tentu"
        "Level tempat duduk mana yang Anda inginkan dan berapa banyak yang Anda inginkan?"
        b "Uh hanya satu tiket"
        b "Dan apa yang tersedia"
        "Kami memiliki tiket Golden Circle untuk 50"
        "Panggung duduk VIP untuk 50"
        "Dan penerimaan umum untuk 5"
        b "{i} (sialan aku lupa bertanya [sname] tentang ini, nerd life menyebalkan!) {/i}"
        b "Saya kira saya akan pergi untuk lingkaran emas"
        b "Apakah ini yang paling dekat dengan panggung?"
        "Ya tapi itu tergantung pada waktu kedatangan Anda ke venue"
        b "Ya dia akan mengelolanya"
        if mny >= 150:
            menu:
                "Beli":
                    b "One please"
                    $ ticketrequested = 3
                    $ mny -= 150
                    scene city_cornerstore2 with dissolve
                    "..."
                    scene city_cornerstore1 with dissolve
                    "Ini dia"
                    b "Thanks"
                    b "{i} (mungkin waktu terbaik untuk memberikan [sname] tiketnya adalah saat kami berlatih berciuman di Hall, setelah saya menonton TV) {/i}"
                    jump broom_menu
                "Tidak sekarang":

                    b "Saya akan memikirkannya"
                    "Baiklah"
                    b "Thanks"
                    jump broom_menu
        else:

            b "Baik saya tidak punya uang sekarang"
            b "Mungkin lain kali"
            "Baiklah"
            b "Thanks"
            jump broom_menu


    elif mpracticegift == 1 and mbag ==0:
        b "Lihat yah!"
        b "{i} (mungkin saya harus mendapatkan sesuatu untuk [mname]) {/i}"
        scene btique with fade
        "Bagaimana saya bisa membantu Anda?"
        b "Hmm"
        b "{i}(Hmm){/i}"
        b "Sebenarnya saya tidak tahu"
        b "Saya ingin membeli hadiah bagus untuk seseorang"
        "Berapa umurnya?"
        b "Hmm di awal tiga puluhan"
        "Ha ha"
        "Ok saya akan mendapatkan sesuatu"
        "Saya dapat merekomendasikan dua ini untuk Anda"
        scene m_bag with fade
        "Tas ini bagus"
        b "Berapa harganya?"
        "$ 150"
        b "Wow"
        "Ya itu tas gucci"
        scene btique with fade
        b "Apa lagi yang Anda miliki?"
        scene m_bikini with fade
        "Dan bikini ini"
        b "Hmm bagus"
        b "Berapa bikini ini?"
        "$ 75"
        menu:
            "Beli tasnya" if mny >= 150:
                $ mny -= 150
                $ mbag = 1
                "Ini dia"
                b "Terima kasih"
                b "{i} (Saya akan memberikannya di kamarnya, perlu mencari tahu kapan) {/i}"
                b "Sampai jumpa"
                "..."
                jump broom_menu

            "Beli bikini" if mbikini==0 and mny >= 75:
                $ mny -= 75
                $ mbikini = 1
                "Ini dia"
                b "Terima kasih"
                b "{i} (Saya akan memberikannya di kamarnya, perlu mencari tahu kapan) {/i}"
                b "Sampai jumpa"
                "..."
                jump broom_menu
            "Tidak perlu sekarang":

                b "Thanks"
                b "Sampai jumpa"
                "..."
                jump broom_menu

    elif mpracticegift == 1 and mbikini ==0:
        b "Lihat yah!"
        b "{i} (mungkin saya harus mendapatkan sesuatu untuk [mname]) {/i}"
        scene btique with fade
        "Bagaimana saya bisa membantu Anda?"
        b "Hmm"
        b "{i}(Hmm){/i}"
        b "Sebenarnya saya tidak tahu"
        b "Saya ingin membeli hadiah bagus untuk seseorang"
        "Berapa umurnya?"
        b "Hmm di awal tiga puluhan"
        "Ha ha"
        "Ok saya akan mendapatkan sesuatu"
        "Saya dapat merekomendasikan dua ini untuk Anda"
        scene m_bag with fade
        "Tas ini bagus"
        b "Berapa harganya?"
        "$ 150"
        b "Wow"
        "Ya itu tas gucci"
        scene btique with fade
        b "Apa lagi yang Anda miliki?"
        scene m_bikini with fade
        "Dan bikini ini"
        b "Hmm bagus"
        b "Berapa bikini ini?"
        "$ 75"
        menu:
            "Beli tasnya" if mbag == 0 and mny >= 150:
                $ mny -= 150
                $ mbag = 1
                "Ini dia"
                b "Terima kasih"
                b "{i} (Saya akan memberikannya di kamarnya, perlu mencari tahu kapan) {/i}"
                b "Sampai jumpa"
                "..."
                jump broom_menu

            "Beli bikini" if mny >= 75:
                $ mny -= 75
                $ mbikini = 1
                "Ini dia"
                b "Terima kasih"
                b "{i} (Saya akan memberikannya di kamarnya, perlu mencari tahu kapan) {/i}"
                b "Sampai jumpa"
                "..."
                jump broom_menu
            "Tidak perlu sekarang":

                b "Thanks"
                b "Sampai jumpa"
                "..."
                jump broom_menu


    elif mpracticegift == 1 and mbikini >=1:
        b "Lihat yah!"
        b "{i} (mungkin saya harus mendapatkan sesuatu untuk [mname]) {/i}"
        scene btique with fade
        "Bagaimana saya bisa membantu Anda?"
        b "Hmm"
        b "{i}(Hmm){/i}"
        b "Sebenarnya saya tidak tahu"
        b "Saya ingin membeli hadiah bagus untuk seseorang"
        "Berapa umurnya?"
        b "Hmm di awal tiga puluhan"
        "Ha ha"
        "Ok saya akan mendapatkan sesuatu"
        "Saya dapat merekomendasikan dua ini untuk Anda"
        scene m_t_relax with fade
        "Ini adalah sesuatu untuk sehari -hari"
        scene btique with fade
        b "Apa lagi yang Anda miliki?"
        "Saya memiliki gaun tidur yang bagus"
        scene m_nightie with fade
        "Ini yang panas"
        b "Hmmm"
        menu:
            "Beli gaun tidur" if mnightie ==0 and mny >= 75:
                $ mny -= 75
                $ mnightie = 1
                "Ini dia"
                b "Terima kasih"
                b "{i} (Saya akan memberikannya di kamarnya, perlu mencari tahu kapan) {/i}"
                b "Sampai jumpa"
                "..."
                jump broom_menu

            "Beli bagian atas dan bawah sehari -hari" if mtrelax ==0 and mny >= 50:
                $ mny -= 50
                $ mtrelax = 1
                "Ini dia"
                b "Terima kasih"
                b "{i} (Saya akan memberikannya di kamarnya, perlu mencari tahu kapan) {/i}"
                b "Sampai jumpa"
                "..."
                jump broom_menu

            "Membeli sesuatu yang lain untuk meminta maaf padanya" if mhate ==1 and msho ==0 and mny >= 50:
                b "Apakah Anda memiliki sesuatu yang lain?"
                "MHHM Saya memiliki kemeja yang indah, ingin melihatnya?"
                b "Yeah sure"
                scene mshirto with dissolve
                b "Ya saya akan mengambilnya"
                $ mny -= 50
                $ msho = 1
                "Ini dia"
                b "Terima kasih"
                b "{i} (Saya akan memberikannya setelah kunjungan kerja malamnya) {/i}"
                b "Sampai jumpa"
                "..."
                jump broom_menu
            "Saya telah berubah pikiran":


                b "Thanks"
                b "Sampai jumpa"
                "Sepertinya Anda telah membeli semuanya untuk saat ini"
                jump broom_menu
    else:

        b "Lihat yah!"
        "..."
        jump broom_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
