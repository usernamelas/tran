image ep8_108 = Movie(play="video/episode8/108.webm", loop = True)
image ep8_109 = Movie(play="video/episode8/109.webm", loop = True)
image ep8_110 = Movie(play="video/episode8/110.webm", loop = True)
image ep8_111 = Movie(play="video/episode8/111.webm", loop = True)
image ep8_112 = Movie(play="video/episode8/112.webm", loop = True)

image ep8_168 = Movie(play="video/episode8/168.webm", loop = True)
image ep8_169 = Movie(play="video/episode8/169.webm", loop = True)
image ep8_170 = Movie(play="video/episode8/170.webm", loop = True)
image ep8_171 = Movie(play="video/episode8/171.webm", loop = True)
image ep8_172 = Movie(play="video/episode8/172.webm", loop = True)
image ep8_173 = Movie(play="video/episode8/173.webm", loop = True)

label episode8:
    $ progress = 109
    stop music fadeout 4.0
    scene expression ("images/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(2, 2) with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    show screen ui_message("Wednesday") with long_dissolve
    hide screen ui_newEpisode
    $ ui.saybehavior()
    $ ui.interact()

    hide screen ui_message

    call episode8_morning from _call_episode8_morning

    call episode8_denise from _call_episode8_denise

    if toby_job == 0:
        call episode8_realEstate from _call_episode8_realEstate
    else:
        call episode8_clubJob from _call_episode8_clubJob

    call episode8_driveHome from _call_episode8_driveHome

    if patricia_path == True:
        call episode8_trisChores from _call_episode8_trisChores
    if patricia_path == True:
        call episode8_betLost from _call_episode8_betLost
    else:
        show screen ui_message("Later that day") with long_dissolve
        $ ui.saybehavior()
        $ ui.interact()
        hide screen ui_message

    call episode8_dinner from _call_episode8_dinner

    if patricia_path == True:
        call episode8_night from _call_episode8_night

    return

label episode8_morning:

    scene expression ("images/episode8/001.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* reading *{/color}{/size}\n{i}\"When interested in someone, a woman might engage in some kind of physical touch.\"{/i}"
    toby "{size=12}{color=#FDCA6E}* reading *{/color}{/size}\n{i}\"This could be a brush of the hand, a tap on the shoulder or the knee, or something somewhat more obvious...like a hug or holding hands.\"{/i}"

    play sound "audio/fx/Cell Phone Ring Sound Effect - Free Sound Effects.mp3"
    scene expression ("images/episode8/002.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode8/003.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Hello?{/i}"
    courier "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Good morning sir. I have a package for you. Are you home?{/i}"
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Yes I am. I'll be out in a minute.{/i}"
    courier "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Great, thank you.{/i}"
    scene expression ("images/episode8/004.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Ever since I got a job it seems like I'm always buying shit and then forget I did. I wonder what I ordered this time?{/i}"
    scene expression ("images/episode8/005.webp") with fade
    courier "[toby!c]?"
    scene expression ("images/episode8/006.webp") with dissolve
    toby "Ya, itu aku."
    scene expression ("images/episode8/005.webp") with dissolve
    courier "Saya punya paket untuk Anda dari gaya lab."
    scene expression ("images/episode8/007.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Holy shit, this must be Tris' maid dress. I totally forgot about it. It's been two weeks since I ordered this.{/i}"
    toby "Terima kasih."
    courier "Semoga harimu menyenangkan, Pak!"
    scene expression ("images/episode8/008.webp") with dissolve
    toby "Kamu juga."
    if ep7_tris_gallery:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm not sure this is the right time to give her this given what happened in the bathroom two days ago.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Screw that, a bet is a bet. I won fair and square. Plus my room could use a good cleaning.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I can't wait to see her face when she sees this dress.{/i}"
    scene expression ("images/episode8/009.webp") with fade
    toby "Pagi [mom]."
    scene expression ("images/episode8/010.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    charlotte "Sayang pagi. Saya tidak tahu Anda keluar."
    scene expression ("images/episode8/009.webp") with dissolve
    toby "Saya baru saja pergi ke luar untuk mengambil paket."
    scene expression ("images/episode8/011_smile.webp") with dissolve
    charlotte "Paket lain? Anda yakin membeli banyak barang akhir -akhir ini."
    scene expression ("images/episode8/012_laugh.webp") with dissolve
    toby "Dalam pembelaan saya, yang ini bukan untuk saya. Ini untuk Tris."
    scene expression ("images/episode8/011_surprised.webp") with dissolve
    charlotte "Benar-benar? Anda sangat baik. Saya sangat senang kalian berdua bergaul dengan baik dan Anda merawat kecil Anda [sister]."
    scene expression ("images/episode8/012_awkward.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}If you only knew.{/i}"
    scene expression ("images/episode8/011_curious.webp") with dissolve
    charlotte "Jadi? Apa yang kamu beli dia?"
    scene expression ("images/episode8/012_awkward.webp") with dissolve
    toby "Gaun!?"
    scene expression ("images/episode8/011_smile.webp") with dissolve
    charlotte "Anda akan menjadi suami yang hebat suatu hari nanti jika Anda memperlakukan [sister] Anda dengan baik. Anda akan membuat seorang wanita sangat bahagia."
    scene expression ("images/episode8/012_smile.webp") with dissolve
    toby "Ummm ... ya ... tentu. Ngomong -ngomong, kamu akan pergi ke mana?"
    scene expression ("images/episode8/011_smile.webp") with dissolve
    charlotte "Saya akan mengambil [aunt] Denise dari stasiun kereta."
    scene expression ("images/episode8/012_curious.webp") with dissolve
    toby "Benar-benar? Apakah [aunt] Denise datang berkunjung?"
    scene expression ("images/episode8/011_laugh.webp") with dissolve
    charlotte "Anda memiliki ingatan ikan mas. Kami hanya membicarakan hal ini pada hari Minggu."
    scene expression ("images/episode8/012_laugh.webp") with dissolve
    toby "Dari apa yang saya baca, ikan mas memiliki ingatan tiga detik, bukan tiga hari."
    scene expression ("images/episode8/011_smile.webp") with dissolve
    charlotte "Maaf saya buruk. Ada perbedaan besar antara tiga detik dan tiga hari."
    scene expression ("images/episode8/012_smile.webp") with dissolve
    toby "Baik, aku akan memaafkanmu."
    scene expression ("images/episode8/011_curious.webp") with dissolve
    charlotte "Jadi? Apakah kamu datang?"
    scene expression ("images/episode8/012_curious.webp") with dissolve
    toby "Datang dimana?"
    scene expression ("images/episode8/011_laugh.webp") with dissolve
    charlotte "Ke stasiun kereta untuk mengambil [aunt] Anda, yang akan datang. Goldie!"
    scene expression ("images/episode8/012_laugh.webp") with dissolve
    toby "Saya tahu Anda pergi ke stasiun kereta, saya hanya berpikir Anda akan pergi sendiri."
    scene expression ("images/episode8/011_smile.webp") with dissolve
    charlotte "Itulah rencana ketika saya pikir Anda masih tidur, tetapi karena Anda sekarang, yah ..."
    scene expression ("images/episode8/012_laugh.webp") with dissolve
    toby "Baik, saya hanya akan meninggalkan hadiah Tris \ ', berubah dan kita bisa pergi."
    scene expression ("images/episode8/013.webp") with fade
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode8/014_texting.webp") with dissolve
    call sms_sent ("tris", "I got you something.", img_icon="images/episode8/015_icon.webp", img="images/episode8/015.webp") from _call_sms_sent_64
    if ep7_tris_gallery:
        call sms_incoming ("tris", "No gift will help me forget that you jerked off while looking at my pic.") from _call_sms_incoming_90
        hide screen message
        scene expression ("images/episode8/014.webp") with dissolve
        if toby_job == 0:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's going to be so mad when she opens this.{/i}"
        else:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}There's a good chance she'll kill me in my sleep over this.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Oh well, fuck it!{/i}"
        scene expression ("images/episode8/014_texting.webp") with dissolve
        call sms_sent ("tris", "At least I'm trying.") from _call_sms_sent_65
        call sms_incoming ("tris", "Whatever... Thank you for the gift, but I'm still not talking to you.") from _call_sms_incoming_91
        call sms_sent ("tris", "And that was my plan all along.") from _call_sms_sent_66
    else:
        call sms_incoming ("tris", "Oh my God. What did you buy me?") from _call_sms_incoming_92
        call sms_sent ("tris", "You'll find out when you get home.") from _call_sms_sent_67
        call sms_incoming ("tris", "I won't be home until later.") from _call_sms_incoming_93
        call sms_incoming ("tris", "Please tell me.") from _call_sms_incoming_94
        call sms_sent ("tris", "Nope. You'll have to live with the suspense.") from _call_sms_sent_68
        call sms_incoming ("tris", "I hate you!") from _call_sms_incoming_95
        call sms_sent ("tris", "Yeah, yeah. I love you too!") from _call_sms_sent_69
    hide screen message

    $ progress = 110
    scene expression ("images/episode8/016.webp") with fade
    toby "Haruskah kita?"
    charlotte "Ya, kami akan."

    scene expression ("images/episode8/017.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/018.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/019.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/020.webp") with dissolve
    charlotte "Sepertinya kereta memiliki sedikit penundaan. Anda tidak akan terlambat untuk bekerja, bukan?"
    toby "Jangan khawatir. Saya tidak akan masuk sampai sore ini hari ini."
    charlotte "Anda memiliki pekerjaan yang sangat aneh. Bukankah aneh tidak mengetahui jam Anda sebelumnya? Anda tidak dapat membuat rencana apa pun karena Anda tidak pernah tahu jika Anda harus pergi bekerja."
    scene expression ("images/episode8/021_laugh.webp") with dissolve
    toby "Tidak juga, selain itu tidak seperti jika saya memiliki rencana saya harus membatalkannya. Bos saya mengerti."
    scene expression ("images/episode8/022_smile.webp") with dissolve
    charlotte "Dia pasti sangat menyukaimu."
    scene expression ("images/episode8/021_smile.webp") with dissolve
    toby "Ya, saya pikir begitu. Maksud saya ada hari -hari ketika saya hanya bekerja 4 atau 5 jam dan uangnya masih bagus."
    scene expression ("images/episode8/022_sad.webp") with dissolve
    charlotte "Harap berhati -hati. Sesuatu tidak benar. Biasanya lebih sulit menghasilkan uang."
    scene expression ("images/episode8/021_smile.webp") with dissolve
    toby "Mungkin saya baru saja beruntung."
    scene expression ("images/episode8/022_curious.webp") with dissolve
    charlotte "Atau mungkin bos Anda menginginkan lebih dari Anda. Maksud saya, Anda seorang pria yang tampan dan dia adalah wanita yang lebih tua dengan kebutuhan."
    scene expression ("images/episode8/021_normal.webp") with dissolve
    toby "Dia menjalin hubungan. Saya tidak berpikir dia tidak memiliki kepuasan."
    scene expression ("images/episode8/022_normal.webp") with dissolve
    charlotte "Anda tidak pernah tahu masalah apa yang dihadapi setiap pasangan. Dan selain itu, wanita seusia saya semacam mencapai tahap kehidupan yang berbeda ketika kebutuhan dan keinginan mereka menjadi di luar kendali."
    scene expression ("images/episode8/021_curious.webp") with dissolve
    toby "Benar-benar?"
    scene expression ("images/episode8/022_sad.webp") with dissolve
    charlotte "Ya, dan semakin sulit untuk tetap setia kepada orang penting Anda."
    scene expression ("images/episode8/021_curious.webp") with dissolve
    toby "Pernahkah Anda berselingkuh di [dad]?"
    scene expression ("images/episode8/022_surprised.webp") with dissolve
    charlotte "Apa dengan pertanyaan itu? Tentu saja saya tidak. Saya tidak mengira saya memiliki dalam diri saya untuk intim dengan orang lain."
    scene expression ("images/episode8/022_normal.webp") with dissolve
    charlotte "Saya tidak berpikir saya bisa hidup dengan diri saya sendiri jika saya hanya pergi dan melakukan hal seperti itu dengan seseorang yang saya tidak cintai."
    scene expression ("images/episode8/021_normal.webp") with dissolve
    toby "Tetapi Anda masih memiliki kebutuhan dan keinginan."
    scene expression ("images/episode8/022_sad.webp") with dissolve

    charlotte "Sayangnya, ya. Itulah mengapa saya tidak sadar mendorong batas -batas di antara kami. Ada saat -saat ketika kami melangkah terlalu jauh mengingat fakta bahwa Anda adalah [son] saya."
    scene expression ("images/episode8/021_normal.webp") with dissolve
    menu:
        "[JGR] Saya tidak berpikir kami pergi jauh":
            $ ep8_pressure_charlotte = True

            $ charlotte_required_flags = [
            ep7_dirty_sunscreen,
            ep7_charlotte_flirt,
            ep6_dirtyMassage,
            ep4_charlotteMovie
            ]
            $ charlotte_path = check_flags(charlotte_required_flags, 3)

            if charlotte_path == False:
                stop music fadeout 1.0
                $ renpy.notify("Charlotte' path has been closed!")
                scene expression ("images/episode8/022_angry.webp") with dissolve
                charlotte "Cukup, [toby!c]. Anda adalah [son] saya. Saya tidak ingin membicarakannya lagi."
                scene expression ("images/episode8/027.webp") with dissolve:
                    xalign 0.0
                    linear 10.0 xalign 1.0

                $ ui.pausebehavior(9.3)
                $ ui.saybehavior()
                $ ui.interact()
                charlotte "Dan selain itu, sepertinya kereta Denise ada di sini."
                return
            else:


                if ep7_dirty_sunscreen == True:
                    scene expression ("images/episode8/022_surprised.webp") with dissolve
                    charlotte "Apakah Anda lupa apa yang terjadi kemarin?"
                    scene expression ("images/episode8/021_flirty.webp") with dissolve
                    toby "Tidak. Aku ingat aku menaruh tabir surya padamu."

                scene expression ("images/episode8/022_normal.webp") with dissolve
                charlotte "Bagian yang penting adalah bahwa saya masih [mother] Anda, meskipun rasanya menyenangkan untuk disentuh."
                scene expression ("images/episode8/022_sad.webp") with dissolve
                charlotte "Dan saya menikah dengan [father] Anda."
                scene expression ("images/episode8/021_curious.webp") with dissolve
                toby "Jadi, jika Anda akan menikah ..."
                scene expression ("images/episode8/022_angry.webp") with dissolve
                charlotte "[toby!c]! Saya masih [mother] Anda."
                scene expression ("images/episode8/021_smile.webp") with dissolve
                toby "Saya yang cantik [mother]."
                scene expression ("images/episode8/022_surprised.webp") with dissolve
                charlotte "[toby!c] !!!"
                scene expression ("images/episode8/021_normal.webp") with dissolve
                toby "Ada beberapa baris yang seharusnya kita lewati.Lihat, [mom]. Saya tahu apa yang Anda katakan dan saya mengerti. Anda benar."
                scene expression ("images/episode8/021_sad.webp") with dissolve
                toby "Tapi kadang -kadang saya hanya lupa bahwa Anda adalah [mother] saya. Terkadang saya melihat Anda untuk Anda. Seorang wanita cantik yang saya senang berbicara dan menghabiskan waktu bersama."
                scene expression ("images/episode8/022_cute.webp") with dissolve
                charlotte "Anda benar -benar berpikir saya cantik?"
                scene expression ("images/episode8/021_flirty.webp") with dissolve
                toby "Anda benar -benar cantik. Yang bisa saya harapkan hanyalah suatu hari nanti ketika saya menikah calon istri saya akan menjadi setengah dari wanita Anda."
                scene expression ("images/episode8/022_shy.webp") with dissolve
                charlotte "Anda akan membuat saya memerah."
                if emma_break == False:
                    scene expression ("images/episode8/022_curious.webp") with dissolve
                    charlotte "Tapi bagaimana Anda bisa melihat saya seperti itu ketika Anda memiliki pacar yang cantik seperti Emma."
                    scene expression ("images/episode8/021_normal.webp") with dissolve
                    toby "Saya tidak tahu, [mom]. Ya, dia pacar saya dan dia cantik, tetapi ada hal lain tentang Anda dan hubungan yang kami miliki."
                else:
                    scene expression ("images/episode8/022_curious.webp") with dissolve
                    charlotte "Tapi Anda masih muda dan ada banyak wanita cantik seusia Anda, bagaimana Anda bisa memandang saya?"
                    scene expression ("images/episode8/021_normal.webp") with dissolve
                    toby "Saya benar -benar tidak tahu, [mom]. Ya itu benar bahwa ada banyak wanita, tetapi entah bagaimana saya selalu membandingkannya dengan Anda. Hubungan yang kami miliki adalah sesuatu yang berbeda."

                scene expression ("images/episode8/022_shy.webp") with dissolve
                charlotte "Saya tidak tahu harus berkata apa. Yang saya tahu terkadang Anda membuat saya merasa sangat baik. Cantik, spesial dan dihargai. Anda membuat saya merasa muda lagi."
                scene expression ("images/episode8/021_normal.webp") with dissolve
                toby "Saya tidak melakukan sesuatu yang istimewa. Saya hanya mengatakan apa yang saya lihat di depan mata saya. Jika Anda terlihat bagus, saya akan mengatakannya. Anda mengajari saya untuk jujur pada diri saya dan orang -orang di sekitar saya."
                scene expression ("images/episode8/022_normal.webp") with dissolve
                charlotte "Tapi itu tidak mengubah fakta bahwa saya masih Anda [mother]. Itu tidak benar."
                scene expression ("images/episode8/021_smile.webp") with dissolve
                toby "Saya minta maaf jika saya melampaui. Saya akan mencoba lebih berhati -hati di lain waktu."
                scene expression ("images/episode8/022_sad.webp") with dissolve
                charlotte "Anda tidak punya apa -apa untuk meminta maaf, bukan seperti saya telah menghentikan Anda."
                scene expression ("images/episode8/021_flirty.webp") with dissolve
                toby "Dan terkadang Anda memulainya."
                scene expression ("images/episode8/022_laugh.webp") with dissolve
                charlotte "Seperti yang saya katakan, saya seorang wanita yang memiliki kebutuhan dan keinginan."
                scene expression ("images/episode8/021_smile.webp") with dissolve
                toby "Saya senang kami menyelesaikan ini."
                scene expression ("images/episode8/022_smile.webp") with dissolve
                charlotte "Saya juga."
                scene expression ("images/episode8/023.webp") with dissolve
                charlotte "Ayo pelukan [mom] Anda."
                $ unlockImage(persistent.charlotte_16)
                scene expression ("images/episode8/024.webp") with dissolve
                if toby_job == 0:
                    toby "Anda berbau harum."
                    charlotte "Anda juga tidak terlalu bau."
                    scene expression ("images/episode8/026.webp") with dissolve
                    toby "Saya mandi."
                else:

                    toby "Cobalah untuk tidak terangsang."
                    scene expression ("images/episode8/025.webp") with dissolve
                    charlotte "Aku? Anda adalah orang yang selalu berakhir dengan boner."
                    scene expression ("images/episode8/026.webp") with dissolve
                    toby "Saya pikir kami tidak membicarakan hal ini."
                    charlotte "Anda memulainya."

                scene expression ("images/episode8/027.webp") with dissolve:
                    xalign 0.0
                    linear 10.0 xalign 1.0

                $ ui.pausebehavior(9.3)
                $ ui.saybehavior()
                $ ui.interact()
                charlotte "Oh ... itu pasti kereta Denise."

                return
        "Saya pikir Anda benar. [JWRN7]"(csq="Jalur Charlotte \ 'ditutup"):


            $ charlotte_path = False
            $ renpy.notify("Charlotte' path has been closed!")
            scene expression ("images/episode8/027.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()
            charlotte "Oh ... itu pasti kereta Denise."
            return

    return

label episode8_denise:
    $ progress = 111

    scene expression ("images/episode8/028.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/029.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/030.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/031.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/032.webp") with dissolve
    denise "Ya Tuhan, [toby!c]. Lihatlah Anda! Apa yang terjadi dengan anak kecil yang lucu itu?"
    scene expression ("images/episode8/033.webp") with dissolve
    toby "Aku tidak lucu lagi?"
    scene expression ("images/episode8/032.webp") with dissolve
    denise "You went from \"I'm a nice guy to date your daughter\", to \"Your wife calls me daddy\"."
    scene expression ("images/episode8/034.webp") with dissolve
    toby "Aku merindukanmu, [auntie]."
    scene expression ("images/episode8/035_laugh_2.webp") with dissolve
    charlotte "Tinggalkan bocah itu sendirian. Berhenti menggodanya."
    scene expression ("images/episode8/036_laugh_1.webp") with dissolve
    denise "Anak laki -laki apa? Ini di sini jelas seorang pria sekarang."
    scene expression ("images/episode8/036_smile_3.webp") with dissolve
    denise "Saya yakin Anda benar -benar menghancurkan hati ke kiri dan ke kanan."
    scene expression ("images/episode8/037_smile_2.webp") with dissolve
    if toby_job == 0:
        toby "Saya mencoba menjadi pria yang baik. Jadi saya tidak bisa mengatakan bahwa saya terlalu hati -hati."
    else:
        toby "Saya tidak tahu apa yang harus dikatakan tentang menghancurkan hati, karena saya memberi tahu mereka di muka untuk tidak jatuh cinta."
    scene expression ("images/episode8/036_flirty_3.webp") with dissolve
    denise "Lihatlah pemain ini."
    scene expression ("images/episode8/036_flirty_1.webp") with dissolve
    denise "Dia mendapatkan ini darimu, bukankah dia?"
    scene expression ("images/episode8/035_ashamed_2.webp") with dissolve
    charlotte "Saya tidak berkeliling hati."
    scene expression ("images/episode8/036_smile_3.webp") with dissolve
    denise "Ya, dia melakukannya. Semua anak laki -laki di desa kami akan bermimpi tentang pergi bersamanya."
    scene expression ("images/episode8/035_smile_3.webp") with dissolve
    charlotte "Dan saya tidak, karena saya bukan pemain."
    scene expression ("images/episode8/035_curious_2.webp") with dissolve
    charlotte "Oh, tunggu! Dimana tasmu?"
    scene expression ("images/episode8/036_laugh_1.webp") with dissolve
    denise "Tas apa?"
    scene expression ("images/episode8/035_normal_2.webp") with dissolve
    charlotte "Yang dengan semua pakaian Anda."
    scene expression ("images/episode8/036_smile_1.webp") with dissolve
    denise "Saya bosan dengan pakaian saya dan saya tahu Anda akan membawa saya berbelanja. Itulah mengapa saya datang ke tempat pertama."
    scene expression ("images/episode8/037_sad_2.webp") with dissolve
    toby "Dan saya pikir Anda datang ke sini karena Anda merindukan kami."
    scene expression ("images/episode8/036_laugh_3.webp") with dissolve
    denise "Nak, saya pikir Anda terlalu banyak tidur di kamar Tris \ '. Anda perlahan -lahan berubah menjadi ratu drama yang memanipulasi orang setiap hari."
    scene expression ("images/episode8/035_laugh_3.webp") with dissolve
    charlotte "Melihat? Sudah kubilang bahwa kamu berubah menjadi ratu drama."
    scene expression ("images/episode8/037_normal_1.webp") with dissolve
    toby "Drama King!"
    scene expression ("images/episode8/036_smile_3.webp") with dissolve
    denise "Tidak. Tidak ada hal seperti itu. Hanya ratu yang mendapatkan semua bitchy!"
    scene expression ("images/episode8/037_normal_2.webp") with dissolve
    toby "Sangat jelas bahwa kalian berdua [sisters]."
    scene expression ("images/episode8/036_laugh_3.webp") with dissolve
    denise "Tapi saya yang seksi, kan?"
    scene expression ("images/episode8/038.webp") with dissolve
    charlotte "Tinggalkan bocah itu sendirian. Anda memaksanya memaksanya berbohong."
    denise "Apakah Anda sangat mengganggu Anda untuk mendengar kebenaran?"
    scene expression ("images/episode8/039.webp") with dissolve
    toby "Tidak ada jawaban yang benar di sini, dan saya menolak untuk memasuki sarang singa."
    scene expression ("images/episode8/040.webp") with dissolve
    denise "Dia pintar, yang ini. Bisakah kita menjaganya?"
    scene expression ("images/episode8/041.webp") with dissolve
    charlotte "Anda putus asa. Ayo ambilkan pakaian."
    $ progress = 112
    scene expression ("images/episode8/042.webp") with fade
    denise "Jadi, ini adalah toko terkenal tempat Anda membeli gaun emas mewah Anda?"
    charlotte "Yup, ini satu -satunya!"
    scene expression ("images/episode8/043.webp") with dissolve
    "{i} * Para wanita berbisik * {/i}"
    toby "Hai! Tidak ada rahasia di depan umum!"
    scene expression ("images/episode8/044.webp") with dissolve
    denise "Maaf sayang, tapi beberapa hal bukan untuk telinga Anda."
    scene expression ("images/episode8/045.webp") with dissolve
    toby "Sekarang Anda hanya membuat saya penasaran."
    scene expression ("images/episode8/044.webp") with dissolve
    denise "Maaf sayang, tapi jangan khawatir, saya akan membiarkan Anda membantu memilih apa yang harus saya beli."
    label memory_26:

        scene expression ("images/episode8/046.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode8/047.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode8/048.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode8/049.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        denise "Jadi? Bagaimana menurut Anda, [toby!c]?"
        menu:
            "[JGR] Saya menyukainya!":
                $ ep8_denise_clothes += 1
                denise "Lalu saya pikir saya harus mendapatkannya."
            "Saya tidak begitu yakin.":

                denise "Baik, saya tidak akan mendapatkannya."

        scene expression ("images/episode8/050.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        denise "Bagaimana dengan yang ini?"
        menu:
            "[JGR] Saya menyukainya. Itu terlihat luar biasa.":
                $ ep8_denise_sexy += 1
                $ ep8_denise_clothes += 1

                denise "Saya yakin Anda melakukannya. Inilah mengapa saya bertanya kepada Anda dan bukan [mother] Anda."
            "Maaf, saya tidak berpikir begitu.":

                denise "Jika pria itu tidak menyukainya, saya tidak membelinya."

        scene expression ("images/episode8/051.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        denise "Dengan baik?"
        menu:
            "[JGR] Ya, itu sangat bagus!":
                $ ep8_denise_clothes += 1
                denise "Besar!"
            "Saya tidak tahu harus berkata apa.":

                denise "Saya mengerti kalau begitu."

        scene expression ("images/episode8/052.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        denise "Bagaimana menurutmu?"
        menu:
            "[JGR] Sial, ya!":
                $ ep8_denise_sexy += 1
                $ ep8_denise_clothes += 1
                denise "Ini akan pulang dengan saya!"
            "Itu tidak sesuai dengan kepribadian Anda.":

                denise "Nah, jika Anda mengatakannya."

        scene expression ("images/episode8/053.webp") with dissolve
        denise "Hei [sis], bisakah kamu datang ke sini sebentar? Saya akan membutuhkan pendapat Anda tentang yang satu ini."
        scene expression ("images/episode8/054.webp") with dissolve
        toby "Bagaimana dengan saya?"
        scene expression ("images/episode8/055.webp") with dissolve
        charlotte "Anda memiliki banyak peluang untuk memberikan pendapat Anda, sayang."
        scene expression ("images/episode8/056.webp") with dissolve
        denise "Jadi? Bagaimana menurutmu? Ini tidak terlalu banyak?"
        charlotte "Yah, saya akan mengatakan itu terlalu sedikit, tapi itu terlihat sangat bagus untuk Anda."
        scene expression ("images/episode8/057.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is she trying on lingerie?{/i}"
        menu:
            "{i} [JGR] Ambil mengintip {/i}"(csq="Penting untuk jalur Denise"):
                $ ep8_peeping_toby = True
                scene expression ("images/episode8/058.webp") with dissolve:
                    yalign 1.0
                    linear 10.0 yalign 0.0

                $ ui.pausebehavior(9.3)
                $ ui.saybehavior()
                $ ui.interact()
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}[auntie!c] looks so hot. Should I send her a message letting her know that she should definitely buy this lingerie?{/i}"

                menu:
                    "{i} [JGR] Kirimkan dia pesan {/i}"(csq="Jalur Buka Denise"):
                        $ renpy.notify("Denise's path opened!")
                        $ denise_path = True
                        $ unlockImage(persistent.denise_01)
                        scene expression ("images/episode8/059_texting.webp") with dissolve
                        if toby_job == 0:
                            call sms_sent ("denise", "Sorry [auntie], I accidentally saw you in that and I have to admit you look gorgeous. You should definitely buy it.") from _call_sms_sent_70
                        else:
                            call sms_sent ("denise", "Hell yes. It looks amazing on you!") from _call_sms_sent_71

                        hide screen message

                    "{i} hentikan {/i}" if not _in_replay:
                        pass
            "{i} menjadi anak yang baik {/i}" if not _in_replay:
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I shouldn't. She's my [aunt] and besides, I don't think she'd appreciate it.{/i}"

        scene expression ("images/episode8/056.webp") with dissolve
        denise "Saya akan memikirkannya!"
        charlotte "Aku akan membiarkanmu berubah."

        scene expression ("images/episode8/060.webp") with dissolve
        charlotte "Haruskah Anda akan bekerja?"
        toby "Ini baik -baik saja, saya masih memiliki sekitar satu jam, jadi masih ada banyak waktu."

        if denise_path:
            play sound "audio/fx/notification_5.mp3"
            "*Notification Sound*"
            scene expression ("images/episode8/061.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It looks like [aunt] Denise saw my message.{/i}"
            scene expression ("images/episode8/062_texting.webp") with dissolve
            call sms_incoming ("denise", "On a scale from zero to ten how good do you think it looked on me.") from _call_sms_incoming_96
            call sms_sent ("denise", "I would say ten, but that would just go to your head. So I''ll say an eight. Eight and a half maybe.") from _call_sms_sent_72
            call sms_incoming ("denise", "Hmmm... That's decent and on a scale from zero to ten how hot was it?") from _call_sms_incoming_97
            call sms_sent ("denise", "Let's just say it's more than ten.") from _call_sms_sent_73
            hide screen message
            scene expression ("images/episode8/063.webp") with dissolve
            charlotte "Siapa yang Anda SMS semua smiley?"
            scene expression ("images/episode8/064.webp") with dissolve
            toby "Tidak ada. Itu bos saya, dia mengatakan itu baik -baik saja jika saya sedikit terlambat untuk bekerja. Itulah mengapa saya tersenyum."
            play sound "audio/fx/notification_5.mp3"
            scene expression ("images/episode8/062_texting.webp") with dissolve
            call sms_incoming ("denise", "You're such a bad liar!") from _call_sms_incoming_98
            call sms_sent ("denise", "Yeah, yeah, but I didn't lie about the fact that you look great in that.") from _call_sms_sent_74
            call sms_incoming ("denise", "Thank you dear, but I don't think I can afford it, I'm still thinking about it.") from _call_sms_incoming_99
            call sms_sent ("denise", "Let me buy it for you then.") from _call_sms_sent_75
            call sms_incoming ("denise", "I appreciate that, but I can't let you do that. Besides, your [mother] will not agree to that.") from _call_sms_incoming_100
            call sms_incoming ("denise", "Anyway, see you in a minute, before your [mother] comes back to check on me.") from _call_sms_incoming_101
            hide screen message
            scene expression ("images/episode8/063.webp") with dissolve
            charlotte "Anda harus sangat suka berbicara dengan bos Anda."
            scene expression ("images/episode8/065.webp") with dissolve
            denise "Tinggalkan anak laki -laki itu sendirian, kau hag tua."
            scene expression ("images/episode8/066.webp") with dissolve
            charlotte "Saya \ m hag lama? Karena Anda mendapat kereta semua yang Anda lakukan adalah menggodanya."
            scene expression ("images/episode8/067.webp") with dissolve
            denise "I \ M -nya [aunt]. Adalah tugas saya untuk menggodanya."
            charlotte "Ya, ya ... bagaimanapun, apakah Anda membeli karya terakhir itu?"
            $ unlockMemory(persistent.memory_26)
        else:

            scene expression ("images/episode8/065.webp") with dissolve
            denise "Dan saya sudah selesai."
            scene expression ("images/episode8/066.webp") with dissolve
            charlotte "Let \'s pergi check out."
            scene expression ("images/episode8/067.webp") with dissolve
            charlotte "Jadi? Apakah Anda membeli karya terakhir itu?"

        $ renpy.end_replay()

    denise "Tidak. Ini tidak seperti saya punya alasan untuk memakainya."
    scene expression ("images/episode8/068.webp") with dissolve
    charlotte "Jadi Anda masih belum melihat siapa pun?"
    denise "Tidak."
    charlotte "Apa yang terjadi dengan Bob?"
    denise "Dia adalah douchebag!"
    scene expression ("images/episode8/069.webp") with dissolve
    clerk "Itu akan menjadi 0,88."
    if denise_path:
        scene expression ("images/episode8/070.webp") with dissolve
        toby "Saya akan mendapatkan ini."
        scene expression ("images/episode8/071.webp") with dissolve
        denise "Anda tidak harus."
        scene expression ("images/episode8/072.webp") with dissolve
        toby "Saya senang. Ini yang paling tidak bisa saya lakukan untuk semua mainan yang Anda beli ketika saya masih muda."
        if charlotte_path:
            scene expression ("images/episode8/073.webp") with dissolve
            charlotte "Sayang, dia adalah [aunt] Anda. Ini tugasnya untuk membelikan Anda mainan."
            scene expression ("images/episode8/074.webp") with dissolve
            denise "Apakah kecemburuan itu saya dengar?"
            scene expression ("images/episode8/075.webp") with dissolve
            charlotte "Tentu saja tidak. Mengapa saya cemburu?"
            scene expression ("images/episode8/076.webp") with dissolve
            $ unlockImage(persistent.denise_02)
            denise "Ya, [toby!c]. Anda dapat membelinya. Terima kasih sayang."
        else:
            scene expression ("images/episode8/075.webp") with dissolve
            charlotte "Saya mengajarinya dengan baik. Jika dia ingin membelinya untuk Anda, saya katakan Anda membiarkannya."
            scene expression ("images/episode8/076.webp") with dissolve
            $ unlockImage(persistent.denise_02)
            denise "Baik, [toby!c]. Anda dapat membelinya untuk saya. Terima kasih!"


    $ progress = 113
    scene expression ("images/episode8/077.webp") with dissolve
    denise "Jadi? Dimana sekarang? Saya sangat membutuhkan kopi."
    toby "Yah, saya harus mulai bekerja. Kalian berdua menikmati kopi Anda."
    charlotte "Jangankah Anda ingin kami mengajak Anda bekerja?"
    toby "Ini baik -baik saja, aku akan naik taksi kembali ke rumah dan kemudian aku akan mengambil sepeda untuk bekerja."
    if denise_path == True:
        scene expression ("images/episode8/078.webp") with dissolve
        denise "Terima kasih atas pakaiannya."
        toby "Dengan senang hati."
        toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}And you really should have let me buy you that lingerie.{/i}"
        denise "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Shh... Your [mom] might hear you.{/i}"
        scene expression ("images/episode8/079.webp") with dissolve
        charlotte "Apa yang kalian berdua berbisik di sana."
        scene expression ("images/episode8/080.webp") with dissolve
        toby "Harus pergi bekerja. Sampai jumpa nanti malam!"
        scene expression ("images/episode8/080_2.webp") with dissolve
        denise "Bye [toby!c]."
        scene expression ("images/episode8/081.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe I should wait a few minutes and go back to buy that lingerie for [aunt] Denise?{/i}"
        menu:
            "{i} Pergi bekerja {/i}":
                pass
            "{i} [JGR] kembali untuk pakaian dalam {/i}":
                $ ep8_denise_lingerie = True
                show screen ui_message("5 minutes later") with long_dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode8/082.webp")
                hide screen ui_message

                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}OK, They can't see me now. I'll head back to the store.{/i}"
                scene expression ("images/episode8/083.webp") with dissolve
                toby "Hai, yang di sana. Teman saya berubah pikiran, dia memutuskan untuk membeli pakaian dalam juga."
                clerk "Tentu, tuan!"
                toby "Terima kasih!"
                scene expression ("images/episode8/084.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I hope she likes it.{/i}"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Even though I have no idea why I bought it. She's my [aunt], but honestly it's nice to see her happy.{/i}"
    else:
        scene expression ("images/episode8/080.webp") with dissolve
        toby "Harus pergi bekerja. Sampai jumpa nanti malam!"
        scene expression ("images/episode8/080_2.webp") with dissolve
        denise "Bye [toby!c]."

    return

label episode8_realEstate:
    $ progress = 114
    scene expression ("images/episode8/085.webp") with fade
    $ ui.saybehavior()
    $ ui.interact()
    katrina "Saya benar -benar perlu berbicara dengan Darlene tentang jadwal kerja Anda."
    scene expression ("images/episode8/086.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode8/087.webp") with dissolve
    toby "Maaf?"
    scene expression ("images/episode8/088.webp") with dissolve
    katrina "Tidak normal bagi seorang karyawan untuk datang bekerja di sore hari. Dia sangat memperlakukanmu dengan baik."
    scene expression ("images/episode8/087.webp") with dissolve
    toby "Mungkin saya melakukan sesuatu yang pantas diperlakukan dengan baik."
    scene expression ("images/episode8/088.webp") with dissolve
    katrina "Saya yakin. Anda anak yang baik."
    scene expression ("images/episode8/089.webp") with dissolve
    if darlene_path:
        katrina "Nikmati hari ini dan pastikan Anda berperilaku."
        scene expression ("images/episode8/090.webp") with dissolve
        toby "Ummm ... oke saya akan."
    else:
        katrina "Semoga harimu menyenangkan, [toby!c]."
        scene expression ("images/episode8/090.webp") with dissolve
        toby "Terima kasih Ma \ 'AM!"

    scene expression ("images/episode8/091.webp") with fade
    toby "Selamat siang."
    scene expression ("images/episode8/092.webp") with dissolve
    darlene "Hai [toby!c]. Bagaimana pagimu?"
    scene expression ("images/episode8/091.webp") with dissolve
    toby "Benar -benar bagus. Saya pergi untuk mengambil [aunt] saya dari stasiun kereta."
    scene expression ("images/episode8/092.webp") with dissolve
    darlene "Itu sangat bagus."
    scene expression ("images/episode8/093_curious.webp") with dissolve
    toby "Apa dengan bunganya? Tolong beritahu saya itu bukan ulang tahun Anda dan saya tidak mendapatkan apa -apa."
    scene expression ("images/episode8/094_laugh.webp") with dissolve
    darlene "Oh, ini? Katrina membelinya. Kami bertengkar minggu lalu, yang jelas salahnya, jadi hari ini dia akhirnya datang untuk meminta maaf."
    scene expression ("images/episode8/093_smile.webp") with dissolve
    toby "Saya senang Anda menyelesaikannya."
    scene expression ("images/episode8/094_smile.webp") with dissolve
    darlene "Siapa bilang kami menyelesaikan masalah? Aku masih kesal padanya, tapi setidaknya aku suka bunga dan aku suka cokelat yang bagus."
    if darlene_path:
        scene expression ("images/episode8/094_chocolate.webp") with dissolve
        darlene "Ingin beberapa?"
        scene expression ("images/episode8/093_normal.webp") with dissolve
        toby "Saya seharusnya tidak. Itu untukmu."
        scene expression ("images/episode8/094_chocolate.webp") with dissolve
        darlene "Omong kosong. Anda adalah karyawan favorit saya, saya akan dengan senang hati membaginya dengan Anda."
        scene expression ("images/episode8/093_chocolate.webp") with dissolve
        toby "Terima kasih!"
        scene expression ("images/episode8/094_smile.webp") with dissolve
        darlene "Terima kasih kembali."
    scene expression ("images/episode8/093_curious.webp") with dissolve
    toby "Jadi apa rencananya untuk hari ini?"
    scene expression ("images/episode8/094_normal.webp") with dissolve
    darlene "Sama seperti minggu lalu. Kami mencari apartemen murah yang dapat kami renovasi."
    scene expression ("images/episode8/093_normal.webp") with dissolve
    toby "Oke. Saya harus memulai saat itu."

    if darlene_path:
        label memory_27:

            scene expression ("images/episode8/095.webp") with dissolve:
                xalign 1.0
                linear 10.0 xalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode8/096.webp") with dissolve:
                xalign 0.0
                yalign 1.0
                linear 10.0 xalign 1.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode8/097.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode8/098.webp") with dissolve:
                yalign 0.0
                linear 10.0 yalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode8/099.webp") with dissolve:
                xalign 1.0
                yalign 1.0
                linear 10.0 xalign 0.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode8/100.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode8/101.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode8/102.webp") with dissolve:
                xalign 1.0
                linear 10.0 xalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode8/103.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode8/104.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode8/105_1.webp") with dissolve
            darlene "Saya ingin mengisap ayam ini sejak pertama kali saya melihatnya."
            scene expression ("images/episode8/105_2.webp") with dissolve
            toby "Mewujudkan impian Anda."
            scene expression ("images/episode8/105_1.webp") with dissolve
            darlene "Tapi sudah bertahun -tahun sejak saya mencicipi ayam asli. Bagaimana jika saya buruk dalam hal itu?"
            scene expression ("images/episode8/105_2.webp") with dissolve
            toby "Lalu aku akan memecatmu."
            scene expression ("images/episode8/106.webp") with dissolve
            darlene "Bisakah Anda memecat saya?"
            toby "Tentu saja, saya adalah COO perusahaan."
            darlene "Maaf Pak, saya akan melakukan yang terbaik."
            scene expression ("images/episode8/107.webp") with dissolve
            darlene "Tapi ini perusahaan saya, bagaimana Anda bisa memecat saya?"
            toby "Lalu aku akan memecatku juga."
            darlene "Tapi saya tidak menginginkannya."
            toby "Apa yang kamu inginkan?"
            darlene "Menjilat ayam ini!"

            scene expression ("images/episode8/108.webp") with dissolve
            show ep8_108
            $ ui.saybehavior()
            $ ui.interact()
            toby "Itu \ 'apakah itu nu'am. Jilat penisku. Gunakan lidah itu."
            hide ep8_108

            scene expression ("images/episode8/109.webp") with dissolve
            show ep8_109
            $ ui.saybehavior()
            $ ui.interact()
            toby "Mengapa Anda tidak memasukkannya ke dalam mulut Anda, jadi saya tidak akan harus memecat Anda!"
            hide ep8_109

            scene expression ("images/episode8/110.webp") with dissolve
            show ep8_110
            $ ui.saybehavior()
            $ ui.interact()
            hide ep8_110

            scene expression ("images/episode8/111.webp") with dissolve
            show ep8_111
            $ ui.saybehavior()
            $ ui.interact()
            toby "Itu saja. Teruslah pergi seperti itu."
            hide ep8_111

            scene expression ("images/episode8/112.webp") with dissolve
            show ep8_112
            $ ui.saybehavior()
            $ ui.interact()
            toby "Saya akan pergi ke cum."
            hide ep8_112

            menu:
                "{i} cum di mulutnya {/i}":
                    with flash
                    $ unlockImage(persistent.darlene_06)
                    scene expression ("images/episode8/113.webp") with dissolve:
                        yalign 0.0
                        linear 10.0 yalign 1.0

                    $ ui.pausebehavior(9.3)
                    $ ui.saybehavior()
                    $ ui.interact()
                    scene expression ("images/episode8/114.webp") with dissolve
                "{i} cum di wajahnya {/i}":


                    with flash
                    $ unlockImage(persistent.darlene_06)
                    scene expression ("images/episode8/115.webp") with dissolve:
                        yalign 1.0
                        linear 10.0 yalign 0.0

                    $ ui.pausebehavior(9.3)
                    $ ui.saybehavior()
                    $ ui.interact()

                    scene expression ("images/episode8/116.webp") with dissolve

            darlene "Maukah Anda memecat saya, Pak?"
            scene expression ("images/episode8/117.webp") with dissolve
            toby "Saya menang. Jangan khawatir. Anda adalah bos terbaik yang pernah ada."

            $ unlockMemory(persistent.memory_27)
            $ renpy.end_replay()

        show screen ui_message("20 minutes later") with long_dissolve
        $ ui.saybehavior()
        $ ui.interact()
        hide screen ui_message
        $ progress = 115
        scene expression ("images/episode8/118.webp"):
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the hell is going on? My head is killing me.{/i}"
        scene expression ("images/episode8/119.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}The fuck is happening?!{/i}"
        scene expression ("images/episode8/120.webp") with dissolve
        darlene "Kepalaku berputar."
        scene expression ("images/episode8/121.webp") with dissolve
        darlene "Apa yang baru saja terjadi? Mengapa kita telanjang?"
        scene expression ("images/episode8/122.webp") with dissolve
        toby "Maaf ma \ 'am. Sejujurnya saya tidak tahu."
        scene expression ("images/episode8/121.webp") with dissolve
        darlene "Tolong beritahu saya bahwa kami tidak berhubungan seks."
        scene expression ("images/episode8/122.webp") with dissolve
        toby "Saya tidak yakin, saya ingat sesuatu, tetapi saya tidak berpikir kita melakukannya."
        scene expression ("images/episode8/123.webp") with dissolve
        darlene "Sial ... aku akan membunuhnya."
        scene expression ("images/episode8/124.webp") with dissolve
        toby "Apakah Anda pikir itu alasannya?"
        scene expression ("images/episode8/125.webp") with dissolve
        darlene "Tolong, pulang. Kami akan berbicara besok dan saya sangat menyesal atas apa yang terjadi."
        scene expression ("images/episode8/126.webp") with dissolve
        toby "Ya ... Saya minta maaf untuk ini, tetapi untuk apa yang berharga saya hampir yakin kami tidak berhubungan seks."
        scene expression ("images/episode8/127.webp") with dissolve
        darlene "Tidak, kami tidak. Bukan itu cara kerjanya."
        scene expression ("images/episode8/128.webp") with dissolve
        toby "Apakah Anda tahu apa yang dilakukan obat -obatan itu?"
        scene expression ("images/episode8/125.webp") with dissolve
        darlene "Itu membuat setiap keinginan lebih kuat."
        darlene "Tolong, pergi saja! Kami akan berbicara besok."
        scene expression ("images/episode8/129.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode8/130.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the hell was in those chocolates?{/i}"
    else:

        scene expression ("images/episode8/131.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode8/132.webp") with dissolve:
            xalign 0.0
            yalign 1.0
            linear 10.0 xalign 1.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode8/133.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode8/134.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode8/135.webp") with dissolve:
            xalign 1.0
            yalign 1.0
            linear 10.0 xalign 0.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode8/100_1.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode8/136.webp") with dissolve
        toby "Jadi? Sampai besok?"
        scene expression ("images/episode8/137.webp") with dissolve
        darlene "Ya, tetapi Anda belum harus pergi, kami masih bisa bersenang -senang."
        scene expression ("images/episode8/136.webp") with dissolve
        toby "Maaf ma \ 'am, tapi saya tidak berpikir kita harus."
        scene expression ("images/episode8/137.webp") with dissolve
        darlene "Oh tolong, jangan malu. Aku tahu kamu ingin aku mengisap kemaluanmu."
        scene expression ("images/episode8/136.webp") with dissolve
        toby "Saya pikir saya harus pergi sekarang. Sampai besok."

        scene expression ("images/episode8/130.webp") with fade
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Today was really productive, but what just happened to Darlene?{/i}"

    return

label episode8_clubJob:
    $ progress = 114
    scene expression ("images/episode8/138.webp") with fade
    toby "Selamat siang."
    scene expression ("images/episode8/139.webp") with dissolve
    katrina "[toby!c]! Anda tepat waktu. Saya butuh bantuan Anda dengan sesuatu."
    scene expression ("images/episode8/140.webp") with dissolve
    toby "Seseorang menyebabkan masalah di klub? Apakah saya akhirnya bisa mengalahkan pantat pembuat masalah?"
    katrina "Tidak, saya punya Neil untuk itu. Anda terlalu pintar untuk dibuang pada hal -hal semacam itu."
    scene expression ("images/episode8/141_curious.webp") with dissolve
    toby "Lalu apa yang harus saya lakukan?"
    scene expression ("images/episode8/142_normal.webp") with dissolve
    katrina "Seberapa baik Anda di sekolah?"
    scene expression ("images/episode8/141_laugh.webp") with dissolve
    toby "Saya mengatakan cukup baik, saya tidak pernah menjadi yang terakhir, tapi tetap saja."
    scene expression ("images/episode8/142_smile.webp") with dissolve
    katrina "Tapi Anda masih tahu matematika dasar kan?"
    scene expression ("images/episode8/141_normal.webp") with dissolve
    toby "Ummm ... tentu. Tapi bisakah Anda lebih spesifik?"
    scene expression ("images/episode8/142_smile.webp") with dissolve
    katrina "Seseorang mencuri dari saya jadi saya ingin Anda memeriksa beberapa catatan dan mungkin Anda bisa mencari tahu siapa."
    scene expression ("images/episode8/141_curious.webp") with dissolve
    toby "Saya pikir klub memiliki akuntan."
    scene expression ("images/episode8/142_normal.webp") with dissolve
    katrina "Ini tidak ada hubungannya dengan klub. Ini untuk proyek sampingan saya."
    scene expression ("images/episode8/141_smile.webp") with dissolve
    toby "Jadi, semua paket dalam mengirimkan kiri dan kanan bukan untuk klub?"
    scene expression ("images/episode8/142_laugh.webp") with dissolve
    katrina "Tentu saja tidak. Apa yang bisa Anda berikan dari klub? Botol Tequila?"
    scene expression ("images/episode8/141_curious.webp") with dissolve
    toby "Bolehkah saya menanyakan apa yang ada di kotak -kotak itu?"
    scene expression ("images/episode8/142_smile.webp") with dissolve
    katrina "Cokelat."
    scene expression ("images/episode8/141_curious.webp") with dissolve
    toby "Apa maksudmu cokelat?"
    scene expression ("images/episode8/142_chocolate.webp") with dissolve
    katrina "Cokelat. Coklat dan manis."
    scene expression ("images/episode8/143.webp") with dissolve
    toby "Anda berantakan dengan saya kan?"
    scene expression ("images/episode8/142_laugh.webp") with dissolve
    katrina "Mengapa saya mengacaukan Anda? Menurut Anda apa yang ada di dalam kotak?"
    scene expression ("images/episode8/141_ashamed.webp") with dissolve
    toby "Narkoba?"
    scene expression ("images/episode8/142_laugh.webp") with dissolve
    katrina "Dan mengapa saya ingin Anda mengirimkan narkoba? Apakah saya terlihat seperti penguasa narkoba?"
    scene expression ("images/episode8/141_laugh.webp") with dissolve
    toby "Ummm ... kamu mungkin."
    scene expression ("images/episode8/142_smile.webp") with dissolve
    katrina "Nah, maaf mengecewakan Anda, tetapi Anda bukan pengedar narkoba."
    scene expression ("images/episode8/141_normal.webp") with dissolve
    toby "Tapi saya telah mengirimkan kotak -kotak di seluruh kota di beberapa tempat yang sangat teduh."
    scene expression ("images/episode8/141_curious.webp") with dissolve
    toby "Dalam dua bulan saya telah bekerja di sini, saya telah melihat banyak omong kosong, jadi permisi jika saya tidak percaya Anda bahwa kami adalah pembuat cokelat."
    scene expression ("images/episode8/142_laugh.webp") with dissolve
    katrina "Nah, lebih murah untuk bekerja dengan orang -orang yang teduh. Saya tidak harus membayar pajak dan omong kosong bodoh."
    scene expression ("images/episode8/141_normal.webp") with dissolve
    toby "Anda menyembunyikan Coke di dalam cokelat, kan?"
    scene expression ("images/episode8/142_laugh.webp") with dissolve
    katrina "Anda benar -benar ingin bekerja sebagai pengedar narkoba? Saya tahu beberapa orang yang bisa menghubungkan Anda dengan beberapa jika Anda benar -benar menginginkannya."
    scene expression ("images/episode8/142_flirty.webp") with dissolve
    katrina "Tetapi sampai saat itu Anda adalah dealer cokelat saya."
    scene expression ("images/episode8/141_laugh.webp") with dissolve
    toby "Saya tidak tahu jika Anda mengacaukan saya atau tidak."
    scene expression ("images/episode8/144.webp") with dissolve
    katrina "Demi sake, nak. Ambil saja satu."
    scene expression ("images/episode8/145.webp") with dissolve
    toby "Itu tidak akan membuat saya tinggi, bukan?"
    scene expression ("images/episode8/146.webp") with dissolve
    katrina "Makan saja saja! Anda membuat saya gila. Saya menelepon Anda di sini karena saya membutuhkan bantuan dengan dokumen."
    scene expression ("images/episode8/141_smile.webp") with dissolve
    toby "Sebenarnya, itu cukup bagus."
    scene expression ("images/episode8/142_smile.webp") with dissolve
    katrina "Tentu saja itu."
    scene expression ("images/episode8/141_curious.webp") with dissolve
    toby "Mengapa kami tidak menjualnya secara legal di toko -toko dan barang -barang?"
    scene expression ("images/episode8/142_smile.webp") with dissolve
    katrina "Karena saya masih berusaha mendapatkan resep yang benar."
    scene expression ("images/episode8/141_smile.webp") with dissolve
    toby "Tapi sudah sangat bagus."
    scene expression ("images/episode8/142_normal.webp") with dissolve
    katrina "Ini belum cukup kuat dan Anda kehilangan rasanya terlalu cepat."
    scene expression ("images/episode8/147.webp") with dissolve
    katrina "Sekarang dapatkah Anda fokus pada apa yang saya butuhkan untuk Anda lakukan?"
    toby "Umm ... tentu."
    scene expression ("images/episode8/148.webp") with dissolve
    katrina "Jangan ragu untuk makan sebanyak yang Anda inginkan, mungkin Anda akan memberi saya beberapa ide tentang cara meningkatkan rasanya."
    if katrina_path == True:
        label memory_28:


            scene expression ("images/episode8/149.webp") with dissolve:
                xalign 1.0
                linear 10.0 xalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode8/150.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode8/151.webp") with dissolve:
                yalign 0.0
                linear 10.0 yalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode8/152.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode8/153.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode8/154.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode8/155.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode8/158.webp") with fade
            katrina "Jadi? Pernahkah Anda menemukan pelakunya?"
            scene expression ("images/episode8/159.webp") with dissolve
            toby "Mungkin. Saya tidak begitu yakin. Sudah beberapa waktu sejak saya telah melakukan pekerjaan intelektual sebanyak ini dan kepala saya berputar."
            scene expression ("images/episode8/160.webp") with dissolve
            katrina "Jangan khawatir, Anda juga bisa mengerjakannya besok. Jadi? Bagaimana cokelatnya?"
            scene expression ("images/episode8/161.webp") with dissolve
            toby "Di samping adiktif?"
            toby "Sangat bagus, saya tidak tahu apa yang ingin Anda ubah."
            scene expression ("images/episode8/160.webp") with dissolve
            katrina "Ya ... Ngomong -ngomong, apakah itu aku atau semakin hangat di sini."
            scene expression ("images/episode8/162.webp") with dissolve
            toby "Tidak. Ini pasti semakin panas di sini."
            katrina "Mengapa Anda tidak menghapus bajumu dan bergabunglah dengan saya di sini."
            scene expression ("images/episode8/163.webp") with dissolve
            katrina "Tidak di sofa. Di lutut Anda di depan saya."
            scene expression ("images/episode8/164.webp") with dissolve
            katrina "Saya benar -benar berharap Anda bisa melacak orang yang mencuri dari saya. Aku sangat kecewa padamu, [toby!c]."
            toby "Maaf ma, tapi seperti saya bilang kepala saya berputar."
            katrina "Baik, aku akan memaafkanmu jika melakukan sesuatu untukku."
            scene expression ("images/episode8/165.webp") with dissolve
            toby "Apa yang kamu butuhkan?"
            scene expression ("images/episode8/166.webp") with dissolve
            katrina "Anda memiliki lidah kan? Memanfaatkannya dengan baik."

            scene expression ("images/episode8/167.webp") with dissolve:
                yalign 0.0
                linear 10.0 yalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            katrina "Itu benar, nak! Jilat vagina itu. Saya tahu Anda ingin."

            scene expression ("images/episode8/168.webp") with dissolve
            show ep8_168
            $ ui.saybehavior()
            $ ui.interact()
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes, yes... Like that. Use your tongue."
            hide ep8_168

            scene expression ("images/episode8/169.webp") with dissolve
            show ep8_169
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck, you're so good at this. Why didn't I try this before?"
            $ ui.saybehavior()
            $ ui.interact()
            hide ep8_169

            scene expression ("images/episode8/170.webp") with dissolve
            show ep8_170
            $ ui.saybehavior()
            $ ui.interact()
            katrina "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nFaster, [toby!c]. Faster!"
            hide ep8_170

            scene expression ("images/episode8/171.webp") with dissolve
            show ep8_171
            $ ui.saybehavior()
            $ ui.interact()
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nLike that... Yesss, yes..."
            hide ep8_171

            scene expression ("images/episode8/172.webp") with dissolve
            show ep8_172
            katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nDon't stop. Right there... Lick my pussy."
            $ ui.saybehavior()
            $ ui.interact()
            hide ep8_172

            scene expression ("images/episode8/173.webp") with dissolve
            show ep8_173
            $ ui.saybehavior()
            $ ui.interact()
            katrina "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nI'm going to cum. Don't stop, [toby!c]! Don't you dare stop!"
            hide ep8_173

            $ unlockImage(persistent.katrina_06)
            scene expression ("images/episode8/174.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            katrina "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nYes, yes... YES!"
            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()


            scene expression ("images/episode8/175.webp") with dissolve
            katrina "Anda adalah anak yang baik, [toby!c]. Ayo berbaring di sofa. Anda akan kembali normal dalam beberapa menit."
            toby "Tapi saya merasa normal!"
            katrina "Letakkan saja!"

            scene expression ("images/episode8/176.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()

            $ unlockMemory(persistent.memory_28)
            $ renpy.end_replay()

        show screen ui_message("20 minutes later") with long_dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode8/177.webp") with dissolve
        hide screen ui_message
        $ progress = 115
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck... My head is killing me! What happened.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I must have fallen asleep.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What a strange dream I had!{/i}"
        scene expression ("images/episode8/178.webp") with dissolve
        katrina "Selamat datang kembali ke Living, [toby!c]. Apakah Anda tidur nyenyak?"
        scene expression ("images/episode8/179.webp") with dissolve
        toby "Maaf, saya tidak tahu kapan saya tertidur. Saya tidak tahu bagaimana itu terjadi."
        scene expression ("images/episode8/178_2.webp") with dissolve
        katrina "Jangan melakukan gerakan tiba -tiba!"
        scene expression ("images/episode8/179.webp") with dissolve
        toby "Apa yang telah terjadi?"
        scene expression ("images/episode8/178.webp") with dissolve
        katrina "Nah, Anda terlalu menyukai cokelatnya dan menjadi sangat terangsang."
        scene expression ("images/episode8/180.webp") with dissolve
        toby "Jadi saya tidak bermimpi?"
        scene expression ("images/episode8/178_2.webp") with dissolve
        katrina "Tidak. Itu nyata dan saya harus mengatakan, jika saya tahu Anda sebagus dengan lidah Anda, saya akan membius Anda sebelumnya."
        scene expression ("images/episode8/181.webp") with dissolve
        toby "Apa sih di cokelat itu?"
        scene expression ("images/episode8/182.webp") with dissolve
        toby "Anda membius saya agar Anda bisa menggunakan saya?"
        katrina "Letakkan tanganmu di leherku sekali lagi dan aku akan menembakmu mati."
        scene expression ("images/episode8/185.webp") with dissolve
        katrina "Berhentilah berteriak seperti anak nakal manja!"
        katrina "Saya tidak melakukan apa -apa. Anda makan sekotak cokelat khusus, jadi itu salah Anda."
        scene expression ("images/episode8/184.webp") with dissolve
        toby "Karena Anda bilang itu cokelat normal."
        scene expression ("images/episode8/185.webp") with dissolve
        katrina "Mengapa Anda percaya itu cokelat normal? Mengapa saya membuat hal seperti itu?"
        scene expression ("images/episode8/184.webp") with dissolve
        toby "Jadi obat -obatan yang Anda minta saya berikan membuat orang melakukan apa yang Anda katakan untuk mereka lakukan?"
        scene expression ("images/episode8/185.webp") with dissolve
        katrina "Saya ingin mengatakan ya, tapi tidak. Satu -satunya hal yang dilakukannya membuat Anda terangsang dan semua keinginan Anda menjadi lebih kuat. Jadi, jika Anda ingin bercinta dengan seseorang, setelah Anda makan, Anda menginginkannya lebih banyak."
        katrina "Dan karena Anda sudah ingin menjilat vaginaku ... yah, Anda melihat hasil akhirnya."
        scene expression ("images/episode8/186.webp") with dissolve
        toby "Saya keluar dari sini. Saya tidak ingin menjilat apa pun!"
        scene expression ("images/episode8/187.webp") with dissolve
        katrina "Sampai jumpa besok dan pastikan Anda kehilangan sikap, atau kami akan memiliki masalah."
    else:

        scene expression ("images/episode8/149.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode8/156.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode8/157.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode8/188.webp") with dissolve
        katrina "Jadi, apakah Anda pernah menemukan pelakunya?"
        scene expression ("images/episode8/189.webp") with dissolve
        toby "Tidak yakin. Saya pikir begitu, tetapi saya perlu melihat lebih dalam pada ini."
        scene expression ("images/episode8/188.webp") with dissolve
        katrina "Anda mengecewakan saya [toby!c], untuk itu Anda akan menjilat vaginaku."
        scene expression ("images/episode8/189.webp") with dissolve
        toby "Tidak, aku tidak."
        scene expression ("images/episode8/188.webp") with dissolve
        katrina "Anda tidak makan cokelat?"
        scene expression ("images/episode8/189.webp") with dissolve
        toby "Tidak, saya tidak."
        scene expression ("images/episode8/189.webp") with dissolve
        katrina "Anda bisa pulang. Anda membosankan."

    return

label episode8_driveHome:
    $ progress = 116
    if toby_job == 0:
        scene expression ("images/episode8/190.webp") with fade
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should head home now, but let's see if I have any messages before I get on the bike.{/i}"
    else:
        scene expression ("images/episode8/192.webp") with fade
        if katrina_path == True:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should head home now, but let's see if I have any messages before I get on the bike.{/i}"
        else:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the fuck was in that chocolate and why was Katrina so eager for me to try?{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Anyway I should head home, but first let's see if I got any messages.{/i}"

    if toby_job == 0:
        scene expression ("images/episode8/191.webp") with dissolve
    else:
        scene expression ("images/episode8/193.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Tris texted me 20 minutes ago.{/i}"

    if toby_job == 0:
        scene expression ("images/episode8/191_texting.webp") with dissolve
    else:
        scene expression ("images/episode8/193_texting.webp") with dissolve

    if ep7_tris_gallery:
        call sms_incoming ("tris", "What the hell is this? Do you really expect me to forgive you with this kind of gift?", img_icon="images/episode8/194_icon.webp", img="images/episode8/194.webp") from _call_sms_incoming_102
    else:
        call sms_incoming ("tris", "What the hell is this? This is what you call a gift?", img_icon="images/episode8/194_icon.webp", img="images/episode8/194.webp") from _call_sms_incoming_103
    call sms_sent ("tris", "I never said anything about a gift. It was you who misunderstood what I meant.") from _call_sms_sent_76
    call sms_incoming ("tris", "Whatever it is, it's stupid!") from _call_sms_incoming_104
    call sms_sent ("tris", "Let me remind you that you lost a bet and my room is getting pretty dusty!") from _call_sms_sent_77
    call sms_incoming ("tris", "It was just a silly bet to motivate you to do things around the house.") from _call_sms_incoming_105
    call sms_sent ("tris", "Well it worked and so is the hot tub. And if you want it to stay working, I'd say you should do the same.") from _call_sms_sent_78
    call sms_incoming ("tris", "You're trying to manipulate me?") from _call_sms_incoming_106
    call sms_sent ("tris", "Maybe. Is it working?") from _call_sms_sent_79

    $ tris_required_flags = [
    ep1_let_patricia_win,
    ep3_kissPatricia,
    ep5_trisChange,
    ep6_caughtJerking,
    ep7_tris_gallery
    ]
    $ patricia_path = check_flags(tris_required_flags, 3)

    if patricia_path:
        call sms_incoming ("tris", "I hope you're proud of yourself.", img_icon="images/episode8/195_icon.webp", img="images/episode8/195.webp") from _call_sms_incoming_107
        call sms_sent ("tris", "I couldn't be more proud. You look great.") from _call_sms_sent_80
        call sms_incoming ("tris", "When will you be coming home?") from _call_sms_incoming_108
        call sms_sent ("tris", "Missing me already?") from _call_sms_sent_81
        call sms_incoming ("tris", "Not really, but the dress is way too short and I need to finish cleaning your room before you get home.") from _call_sms_incoming_109
        call sms_sent ("tris", "Shit... I'll be here at least two more hours.") from _call_sms_sent_82
        call sms_incoming ("tris", "Too bad for you. I'll only be cleaning your room when you're not home.") from _call_sms_incoming_110
        call sms_sent ("tris", "That's not fair!") from _call_sms_sent_83
        call sms_incoming ("tris", "Not my fault that you don't know how do make a bet.", img_icon="images/episode8/196_icon.webp", img="images/episode8/196.webp") from _call_sms_incoming_111
        call sms_incoming ("tris", "Gotta go. I have a dusty room to clean.") from _call_sms_incoming_112
        call sms_sent ("tris", "See you later!") from _call_sms_sent_84
    else:
        $ renpy.notify("Tris' path has been closed!")
        call sms_incoming ("tris", "No! Fuck you and your stupid hot tub.") from _call_sms_incoming_113
        call sms_sent ("tris", "Whoa... What's wrong?") from _call_sms_sent_85
        call sms_incoming ("tris", "Nothing, but this dress is stupid. I'm your [sister], not some whore you dress up like you want and make her do things for you.") from _call_sms_incoming_114
        call sms_incoming ("tris", "Our relationship is getting out of hand, so I'm going to put an end to it.") from _call_sms_incoming_115
        call sms_sent ("tris", "I think you're overreacting.") from _call_sms_sent_86
        call sms_incoming ("tris", "Maybe I am, but I think we should get back to our old relationship!") from _call_sms_incoming_116
    hide screen message
    if toby_job == 0:
        scene expression ("images/episode8/197.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        $ ui.pausebehavior(9.3)
    else:
        scene expression ("images/episode8/198.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0
        $ ui.pausebehavior(9.3)

    if patricia_path:
        if toby_job == 0:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She really thinks she can fool me? I'm going to fly home. I need to see how the dress looks on her.{/i}"
        else:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This little bitch tried to play me. Sorry darling, but I'm coming home now!{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I have no idea what happened to make her this mad.{/i}"

    scene expression ("images/episode8/199.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/200.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/201.webp") with fade
    toby "Hai [dad]. Dimana semuanya?"
    scene expression ("images/episode8/202.webp") with dissolve
    erwin "[mother] dan [aunt] Anda akan segera kembali dan [sister] Anda melakukan sesuatu di lantai atas."
    scene expression ("images/episode8/201.webp") with dissolve
    toby "Oke!"
    toby "Kenapa kamu pulang sepagi ini?"
    scene expression ("images/episode8/202.webp") with dissolve
    erwin "[mother] Anda membuat saya berjanji bahwa saya akan pulang untuk makan malam karena dia [sister] akan bergabung dengan kami."
    scene expression ("images/episode8/203.webp") with dissolve
    toby "Sampai jumpa saat makan malam."

    return


label episode8_trisChores:
    $ progress = 117
    scene expression ("images/episode8/204.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Now that's a nice view.{/i}"

    scene expression ("images/episode8/205.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/206.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode8/207.webp") with dissolve
    patricia "Oh, itu kamu. Anda mengejutkan saya."
    scene expression ("images/episode8/208.webp") with dissolve
    toby "Jangan biarkan aku menghentikanmu."
    scene expression ("images/episode8/209_1.webp") with dissolve
    patricia "Bagaimana saya bisa melanjutkan? Gaun ini terlalu pendek."
    scene expression ("images/episode8/208.webp") with dissolve
    toby "Itu terlihat bagus untukmu."
    scene expression ("images/episode8/209_2.webp") with dissolve
    patricia "Apakah Anda benar -benar berpikir begitu?"
    scene expression ("images/episode8/208.webp") with dissolve
    toby "Ya, tentu saja. Anda cantik, bahkan dalam gaun pelayan."

    scene expression ("images/episode8/210.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    patricia "Sejujurnya, saya pikir itu terlihat lucu juga."
    scene expression ("images/episode8/208.webp") with dissolve
    toby "Anda benar -benar dapat membuat bisnis dari ini, jika hal keperawatan tidak berhasil."
    scene expression ("images/episode8/211.webp") with dissolve
    patricia "Untuk sesaat di sana Anda hampir seperti normal [brother]."
    toby "Apa yang normal [brother] akan membeli gaun pembantu [sister] -nya?"
    scene expression ("images/episode8/212_laugh.webp") with dissolve
    patricia "Terutama dari toko seks."
    scene expression ("images/episode8/213_laugh.webp") with dissolve
    toby "Saya tidak membelinya dari toko seks. Saya mungkin terlihat seperti perv tetapi saya dapat meyakinkan Anda bahwa saya tidak."
    scene expression ("images/episode8/212_normal.webp") with dissolve
    patricia "Lalu kenapa begitu singkat?"
    scene expression ("images/episode8/213_smile.webp") with dissolve
    toby "Mungkin Anda memiliki kaki yang panjang."
    scene expression ("images/episode8/212_normal.webp") with dissolve
    patricia "Apa pun. Saya masih tidak melihat maksud saya berdandan sebagai pelayan."
    scene expression ("images/episode8/213_laugh.webp") with dissolve
    toby "Tidak ada gunanya. Saya merasa lucu dan baik, Anda kehilangan taruhan. Jadi Anda perlu merasakannya."
    scene expression ("images/episode8/212_normal.webp") with dissolve
    patricia "Oh percayalah. Saya merasa bahwa saya kehilangan taruhan. Kapan terakhir kali Anda membersihkan tempat ini?"
    scene expression ("images/episode8/213_smile.webp") with dissolve
    toby "Saya pikir tepat setelah saya selesai merenovasinya."
    scene expression ("images/episode8/212_facepalm.webp") with dissolve
    patricia "Itulah yang saya pikirkan. Ini berantakan di sini. Saya terkejut Anda belum sakit."
    scene expression ("images/episode8/213_flirty.webp") with dissolve
    toby "Apakah itu berarti bahwa begitu taruhan sudah berakhir Anda akan terus membersihkan kamar saya jadi saya tidak akan sakit?"
    scene expression ("images/episode8/212_arogant.webp") with dissolve
    patricia "Jika Anda membayar saya, mungkin."
    scene expression ("images/episode8/212_normal.webp") with dissolve
    patricia "Tapi tanpa gaun itu."
    scene expression ("images/episode8/213_flirty.webp") with dissolve
    toby "Jika Anda ingin membersihkan kamar saya telanjang, siapa saya untuk menghentikan Anda."
    scene expression ("images/episode8/212_facepalm.webp") with dissolve
    patricia "Maksud saya tanpa gaun bodoh ini."
    scene expression ("images/episode8/213_smile.webp") with dissolve
    toby "Maaf, maksud saya jika Anda ingin membersihkan kamar saya di pakaian dalam Anda, lakukanlah."
    scene expression ("images/episode8/212_angry.webp") with dissolve
    patricia "Izinkan saya mengulangi kalimat saya."
    scene expression ("images/episode8/212_normal.webp") with dissolve
    patricia "Maksud saya mengenakan pakaian normal, bukan dengan gaun bodoh ini."
    scene expression ("images/episode8/213_curious.webp") with dissolve
    toby "Bahkan tidak jika saya menaikkan gaji Anda?"
    scene expression ("images/episode8/212_curious.webp") with dissolve
    patricia "Berapa banyak yang kita bicarakan di sini?"
    scene expression ("images/episode8/213_normal.webp") with dissolve
    toby "Saya akan memikirkannya. Pertama saya perlu melihat seberapa baik Anda dalam hal ini."
    scene expression ("images/episode8/212_arogant.webp") with dissolve
    patricia "Percayalah, tidak ada seorang pun di rumah ini yang akan melakukan pekerjaan yang lebih baik daripada saya, atau bahkan melakukannya."
    scene expression ("images/episode8/213_smile.webp") with dissolve
    toby "Saya yakin [mom] dapat melakukan pekerjaan yang lebih baik dari Anda."
    scene expression ("images/episode8/212_laugh.webp") with dissolve
    patricia "And I'm pretty positive she would never agree to do it. She'll start with the \"You're old enough to clean your own room...\"."
    scene expression ("images/episode8/213_curious.webp") with dissolve
    toby "Lalu mungkin [dad]."
    scene expression ("images/episode8/212_laugh.webp") with dissolve
    patricia "Ya, semoga sukses dengan itu."
    patricia "Jadi, seperti yang saya katakan, saya satu -satunya pilihan Anda, jadi Anda lebih baik membayar saya dengan baik."
    scene expression ("images/episode8/213_flirty.webp") with dissolve
    toby "Tapi sampai saat itu saya hanya akan menikmati melihat Anda membersihkan kamar saya secara gratis."
    scene expression ("images/episode8/212_curious.webp") with dissolve
    patricia "Saya tahu Anda cabul. Normal seperti apa [brother] akan senang melihat [sister] membungkuk dengan gaun pendek."
    scene expression ("images/episode8/213_normal.webp") with dissolve
    toby "Maksud saya, saya akan menikmati tidak harus membayar Anda. Pikiran Anda berada di tempat kotor yang indah, [sis]."
    scene expression ("images/episode8/212_surprised.webp") with dissolve
    patricia "Tidak, itu tidak. Saya yakin itu persis seperti yang Anda maksud, tetapi sekarang Anda membuat alasan."
    scene expression ("images/episode8/213_smile.webp") with dissolve
    toby "Tidak. Satu -satunya cabul di rumah ini adalah Anda, sayang [sister]."
    scene expression ("images/episode8/212_curious.webp") with dissolve
    patricia "Anda agak melupakan semua boner yang Anda dapatkan karena saya."
    scene expression ("images/episode8/213_normal.webp") with dissolve
    toby "Bukan salah saya, Anda meletakkan payudara Anda di wajah saya."
    scene expression ("images/episode8/212_curious.webp") with dissolve
    patricia "Jadi sekarang salahku?"
    scene expression ("images/episode8/213_normal.webp") with dissolve
    toby "Tentu saja."
    scene expression ("images/episode8/212_flirty.webp") with dissolve
    patricia "Jadi jika saya melanjutkan pekerjaan saya di sekitar kamar Anda, membungkuk dengan gaun pendek ini, Anda tidak akan peduli?"
    scene expression ("images/episode8/213_smile.webp") with dissolve
    toby "Aku bahkan tidak akan mengenalmu di sini. Sudah kubilang. Aku bukan orang cabul sepertimu."
    scene expression ("images/episode8/212_smile.webp") with dissolve
    patricia "Dan jika Anda melihat Anda mulai membayar saya untuk membersihkan."
    scene expression ("images/episode8/213_laugh.webp") with dissolve
    toby "Anda kehilangan taruhan dan setelah 10 menit membersihkan kamar saya, Anda sudah mencoba menemukan jalan keluar dari itu?"
    scene expression ("images/episode8/212_arogant.webp") with dissolve
    patricia "Takut Anda akan kalah? Orang cabul!"
    scene expression ("images/episode8/213_normal.webp") with dissolve
    toby "Bagus."
    scene expression ("images/episode8/213_smile.webp") with dissolve
    toby "Saya merasa lucu bagaimana satu -satunya hal yang mengganggu Anda adalah kenyataan bahwa saya tidak membayar Anda. Tidak mengganggu Anda bahwa Anda harus membersihkan kamar saya selama dua bulan atau fakta bahwa Anda berpakaian seperti itu, tetapi fakta bahwa saya tidak membayar Anda."
    scene expression ("images/episode8/212_smile.webp") with dissolve
    patricia "Nah, saya butuh uang. Agak menjengkelkan untuk meminta uang [dad] dan dia mengatakan kepada saya bahwa dia baru saja memberi saya 0 lima hari yang lalu."
    scene expression ("images/episode8/213_normal.webp") with dissolve
    toby "Apa pun, itu tidak seperti Anda akan memenangkan taruhan ini, jadi ya. Saya pikir Anda harus kembali bekerja."
    scene expression ("images/episode8/212_curious.webp") with dissolve
    patricia "Kami bahkan belum membahas harganya."
    scene expression ("images/episode8/213_smile.webp") with dissolve
    toby "Apa intinya? Ini tidak seperti Anda akan menang."
    scene expression ("images/episode8/212_normal.webp") with dissolve
    patricia "Lalu saya akan memutuskan harga sendiri dan Anda akan menyetujui apa pun yang saya minta."
    scene expression ("images/episode8/213_laugh.webp") with dissolve
    toby "Bukan itu cara kerja."
    scene expression ("images/episode8/212_flirty.webp") with dissolve
    patricia "Baik -baik saja saya akan puas dengan 00."
    scene expression ("images/episode8/213_surprised.webp") with dissolve
    toby "00 untuk membersihkan kamar saya? Apakah kamu gila?"
    scene expression ("images/episode8/212_curious.webp") with dissolve
    patricia "Apa? Ini tidak seperti saya akan menang, kan?"
    scene expression ("images/episode8/213_laugh.webp") with dissolve
    toby "Untuk 00 Anda membersihkannya telanjang."
    scene expression ("images/episode8/212_normal.webp") with dissolve
    patricia "Dan saya yang sesat."
    scene expression ("images/episode8/213_normal.webp") with dissolve
    toby "Mesum dan gila. 00 adalah banyak uang untuk satu kamar."
    scene expression ("images/episode8/212_eyes.webp") with dissolve
    patricia "Bagus. 00!"
    scene expression ("images/episode8/213_laugh.webp") with dissolve
    toby "Dalam pakaian dalam?"
    scene expression ("images/episode8/212_curious.webp") with dissolve
    patricia "Mengapa Anda bahkan peduli? Tidak seperti saya akan menang, kan?"
    scene expression ("images/episode8/213_normal.webp") with dissolve
    toby "Lebih aman daripada maaf."
    scene expression ("images/episode8/212_normal.webp") with dissolve
    patricia "Bagus!!! 0, tapi saya melakukannya dengan pakaian saya sendiri."
    scene expression ("images/episode8/213_normal.webp") with dissolve
    toby "Tidak."
    scene expression ("images/episode8/212_meh.webp") with dissolve
    patricia "Anda sangat murah."
    scene expression ("images/episode8/213_curious.webp") with dissolve
    toby "Apa maksudmu aku murah? Saya membuat Anda menjadi penawaran yang bagus. 5 Di pakaian Anda sendiri, 0 dengan gaun itu, 00 di pakaian dalam Anda dan 00 benar -benar telanjang."
    scene expression ("images/episode8/213_normal.webp") with dissolve
    toby "Itu pilihanmu. Jika Anda membutuhkan lebih banyak uang, Anda tahu apa yang perlu Anda lakukan."
    scene expression ("images/episode8/212_curious.webp") with dissolve
    patricia "Mengapa Anda ingin melihat [sister] telanjang Anda?"
    scene expression ("images/episode8/213_normal.webp") with dissolve
    toby "Saya tidak. Saya hanya memberi Anda opsi sulit untuk memastikan saya tidak bangkrut."

    label memory_29:
        scene expression ("images/episode8/214_1.webp") with dissolve

        patricia "Bagus. Saya akan terus membersihkan kamar Anda seperti ini, tetapi Anda lebih baik tidak terlihat."
        scene expression ("images/episode8/214_2.webp") with dissolve
        toby "Jangan khawatir. Ini tidak seperti saya penasaran."
        scene expression ("images/episode8/215.webp") with dissolve
        patricia "Ya. Saya sangat beruntung bahwa Anda tidak penasaran karena gaun ini sangat pendek."
        menu:
            "{i} [JGR] Lihatlah {/i}":
                scene expression ("images/episode8/216.webp") with dissolve:
                    yalign 1.0
                    linear 10.0 yalign 0.0

                $ ui.pausebehavior(9.3)
                $ ui.saybehavior()
                $ ui.interact()
                toby "Ya, saya kira itu agak terlalu pendek."
                scene expression ("images/episode8/227_1.webp") with dissolve
                if _in_replay:
                    $ renpy.end_replay()

                return
            "{i} don \ 't lihat {/i}":
                pass

        toby "Saya tahu apa yang Anda coba dengan itu, tetapi itu tidak akan berhasil."
        scene expression ("images/episode8/217.webp") with dissolve
        patricia "Saya tidak tahu apa yang Anda bicarakan. Saya hanya membersihkan furnitur Anda dalam gaun yang sangat singkat ini. Saya hampir dapat merasakan bahwa pantat kecil saya yang lucu terbuka."
        menu:
            "{i} [JGR] Lihatlah {/i}":
                scene expression ("images/episode8/218.webp") with dissolve:
                    yalign 1.0
                    linear 10.0 yalign 0.0

                $ ui.pausebehavior(9.3)
                $ ui.saybehavior()
                $ ui.interact()
                toby "Saya tidak tahu apa yang Anda bicarakan karena pantat itu tidak kecil."
                scene expression ("images/episode8/227_1.webp") with dissolve
                if _in_replay:
                    $ renpy.end_replay()
                return
            "{i} don \ 't lihat {/i}":
                pass

        toby "Ya, kesalahan saya. Mungkin saya seharusnya membeli gaun yang lebih panjang."
        scene expression ("images/episode8/219.webp") with dissolve
        patricia "Oopsies ... betapa konyolnya saya, saya baru saja menjatuhkan bulu ini. Saya kira saya harus membungkuk untuk mengambilnya. Semoga tidak ada yang akan terlihat."
        menu:
            "{i} [JGR] Lihatlah {/i}":
                scene expression ("images/episode8/220.webp") with dissolve:
                    yalign 1.0
                    linear 10.0 yalign 0.0

                $ ui.pausebehavior(9.3)
                $ ui.saybehavior()
                $ ui.interact()
                toby "Saya hanya ingin memastikan Anda tidak kehilangan kain yang lebih tua."
                scene expression ("images/episode8/227_2.webp") with dissolve
                if _in_replay:
                    $ renpy.end_replay()
                return
            "{i} don \ 't lihat {/i}":
                pass

        toby "Cobalah untuk tidak menjatuhkannya lagi. Anda hanya akan menyebarkan debu lebih banyak lagi."
        scene expression ("images/episode8/221_1.webp") with dissolve
        patricia "Berbicara tentang debu. Ada banyak debu di sini. Aku lebih baik sedikit rapi."
        patricia "Ups. Bodohku, gaun ini juga sangat rendah. Puting saya hampir terlihat."
        menu:
            "{i} [JGR] Lihatlah {/i}":
                $ unlockImage(persistent.patricia_15)
                scene expression ("images/episode8/221_2.webp") with dissolve:
                    xalign 0.0
                    yalign 1.0
                    linear 10.0 yalign 0.2 xalign 1.0

                $ ui.pausebehavior(9.3)
                $ ui.saybehavior()
                $ ui.interact()
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck... She's such a tease. And dammit, she's good at it too.{/i}"
                scene expression ("images/episode8/227_2.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                $ unlockMemory(persistent.memory_29)
                $ renpy.end_replay()
                return

            "{i} don \ 't lihat {/i}"(csq="Tris \ 'Path ditutup") if not _in_replay:
                $ ep8_failed_maid = True
                stop music fadeout 1.0
                scene expression ("images/episode8/222.webp") with dissolve
                patricia "Anda tahu apa? Persetan denganmu! Anda bodoh."
                scene expression ("images/episode8/223.webp") with dissolve
                toby "Kenapa kamu marah? Apa masalahnya sekarang?"
                scene expression ("images/episode8/224.webp") with dissolve
                patricia "Anda tahu saya butuh uang dan Anda bisa membantu saya, tetapi tidak! Anda terlalu murah untuk membantu [sister] Anda keluar."
                scene expression ("images/episode8/223.webp") with dissolve
                toby "Jika Anda membutuhkan uang, tanyakan saja."
                scene expression ("images/episode8/224.webp") with dissolve
                patricia "Saya tidak ada pengemis. Saya mencoba melakukan sesuatu yang baik untuk Anda, tetapi tidak, Anda terlalu bodoh untuk itu."
                scene expression ("images/episode8/223.webp") with dissolve
                toby "Baik, Anda dapat membersihkan kamar saya dan saya bahkan akan membayar Anda."
                scene expression ("images/episode8/225.webp") with dissolve
                patricia "Saya tidak menginginkan apapun dari Anda."
                patricia "Selamat tinggal!"
                $ renpy.notify("Tris' path has been closed!")
                $ patricia_path = False
                scene expression ("images/episode8/226.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}The hell is her problem? I'd better go try to calm her down.{/i}"
    return

label episode8_betLost:
    patricia "Dan itulah yang saya sebut taruhan menang!"
    scene expression ("images/episode8/228.webp") with dissolve
    patricia "Kamarnya bersih. Saya menunggu pembayaran saya."
    scene expression ("images/episode8/229.webp") with dissolve
    toby "Di Sini."
    scene expression ("images/episode8/230.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode8/231.webp") with dissolve
    patricia "Senang berbisnis dengan Anda!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck I can almost see her nipples.{/i}"
    menu:
        "{i} [JGR] Lihat lebih baik {/i}":
            scene expression ("images/episode8/232.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode8/233.webp") with dissolve
            patricia "This is the part where you say, \"The pleasure is all mine\", karena itu jelas terjadi."
            scene expression ("images/episode8/231_2.webp") with dissolve
            toby "Kata gadis yang lebih kaya bagi pria yang 0 broker."
        "{i} menjadi anak yang baik {/i}":

            pass
    scene expression ("images/episode8/234.webp") with dissolve
    patricia "Saya akan kembali dalam dua hari."
    scene expression ("images/episode8/235.webp") with dissolve
    toby "Dua Hari? Saya pikir Anda akan membersihkannya setiap dua minggu, tidak setiap dua hari."
    scene expression ("images/episode8/234.webp") with dissolve
    patricia "Anda perlu belajar bernegosiasi dengan lebih baik."
    if toby_job == 0:
        patricia "Saya masih tidak mengerti bagaimana Anda menghasilkan uang di pekerjaan Anda! Anda sangat buruk dalam bernegosiasi."

    scene expression ("images/episode8/236.webp") with dissolve
    if toby_job == 0:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's something else.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This little bitch is playing me.{/i}"

    show screen ui_message("A few minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message

    return

label episode8_dinner:
    $ progress = 118

    scene expression ("images/episode8/237.webp")
    charlotte "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n[toby!c], Tris! Come see who came to visit."
    scene expression ("images/episode8/238.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I don't think Tris knows that [aunt] Denise came to visit.{/i}"
    scene expression ("images/episode8/239.webp") with dissolve
    toby "Apa dengan teriakan?"
    scene expression ("images/episode8/240.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    if patricia_path == True:
        scene expression ("images/episode8/241_1.webp") with dissolve
        patricia "Lihat siapa yang datang!"
        scene expression ("images/episode8/242.webp") with dissolve
        toby "Aku tahu. Saya pergi menjemputnya dari stasiun kereta pagi ini dan kemudian pergi berbelanja."
    else:
        scene expression ("images/episode8/241_2.webp") with dissolve
        patricia "Asal Anda tahu, dia tidak pantas mendapatkan pelukan Anda."
        scene expression ("images/episode8/242.webp") with dissolve
        toby "Terlambat untuk itu, [sis]. Dia sudah memberi saya satu pagi ini sebelum kami pergi berbelanja."
    scene expression ("images/episode8/243.webp") with dissolve
    patricia "Pengkhianat. Anda mengambil [toby!c] berbelanja, bukan saya?"
    denise "Mudah, harimau. Bukannya aku akan pergi besok. Kami masih bisa pergi jika Anda mau."
    patricia "Berapa lama Anda akan tinggal?"
    scene expression ("images/episode8/244.webp") with dissolve
    denise "Nah, saya di sini untuk kursus mekanik, jadi saya akan tinggal beberapa hari."
    scene expression ("images/episode8/245.webp") with dissolve
    denise "Tapi dalam pembelaan saya, saya membelikan Anda sesuatu yang bagus."
    scene expression ("images/episode8/246.webp") with dissolve
    patricia "Apa yang kamu bawa?"
    scene expression ("images/episode8/247.webp") with dissolve
    denise "Mengapa Anda tidak naik ke atas dan mencobanya. Saya harap ini akan terlihat bagus untuk Anda."
    scene expression ("images/episode8/248.webp") with dissolve
    patricia "Segera kembali dan jangan berani makan tanpa saya."
    scene expression ("images/episode8/249.webp") with dissolve

    denise "Sejak kapan dia mulai menyukai makanan sebanyak ini? Saya ingat memanggilnya tikus kecil saya karena dia hanya memilih makanannya."
    scene expression ("images/episode8/250.webp") with dissolve
    erwin "Tidak ada yang berubah. Dia masih baru saja menyentuh makanannya."
    scene expression ("images/episode8/251.webp") with dissolve
    charlotte "Bagaimana kamu tahu? Dia makan lebih baik dari biasanya."
    scene expression ("images/episode8/252.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}These guys are going to argue soon. Let's change the subject.{/i}"
    toby "Mengapa kita tidak duduk?"
    scene expression ("images/episode8/253.webp") with dissolve
    erwin "Jadi Denise, kursus apa yang Anda ikuti?"
    scene expression ("images/episode8/254.webp") with dissolve
    denise "Nah, karena Ayah tidak bisa lagi memperbaiki traktor, seseorang harus belajar bagaimana melakukannya."
    denise "Dan saya benar -benar menjadi sangat pandai memperbaiki hal -hal. Penduduk desa lainnya bahkan mulai membawa mobil mereka kepada saya, tetapi beberapa dari mereka cukup baru dan lebih sulit untuk diperbaiki."
    scene expression ("images/episode8/255.webp") with dissolve
    toby "Jadi pada dasarnya Anda menjadi mekanik desa?"
    scene expression ("images/episode8/256.webp") with dissolve
    denise "Saya dan Tuan Colon. Tetapi setelah saya menyelesaikan kursus ini, saya akan menjadi yang lebih berkualitas."
    scene expression ("images/episode8/257.webp") with dissolve
    charlotte "Apakah Tuan Colon masih hidup? Dia seperti apa? 110?"
    scene expression ("images/episode8/258.webp") with dissolve
    denise "Dia baru berusia 70 -an. Mungkin akhir 70 -an, tetapi Anda juga tidak lagi ayam musim semi."
    scene expression ("images/episode8/259.webp") with dissolve
    if patricia_path == True:
        patricia "Siapa yang sudah tua?"
    else:
        patricia "Siapa yang tidak lagi muda? [toby!c]? Tahun, dia menjadi sangat tua."
    scene expression ("images/episode8/260.webp") with dissolve
    charlotte "Ya ampun, ... lihat wanita muda ini."

    scene expression ("images/episode8/261.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    patricia "Anda menyukainya?"

    if patricia_path == True:
        scene expression ("images/episode8/262.webp") with dissolve
        toby "Anda terlihat cantik, [sis]."
        $ unlockImage(persistent.patricia_16)
    else:
        scene expression ("images/episode8/263.webp") with dissolve
        erwin "Anda tampak hebat Patricia."
    scene expression ("images/episode8/264.webp") with dissolve
    patricia "Terima kasih!"
    patricia "Jadi? Apa yang kamu bicarakan?"

    scene expression ("images/episode8/265.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/266.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/267.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/268.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/269.webp") with dissolve:
        yalign 1.0
        xalign 0.0
        linear 10.0 yalign 0.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/270.webp") with dissolve:
        xalign 1.0
        yalign 1.0
        linear 10.0 yalign 0.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/271.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/272.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/273.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode8/274.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    return

label episode8_night:
    $ progress = 119

    scene expression ("images/episode8/275.webp") with dissolve
    if toby_job == 0:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Dinner was really good, but I can't sleep. I'm so thirsty.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Dinner was really good, but fuck me I'm so thirsty.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'll go get some water.{/i}"

    scene expression ("images/episode8/276.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode8/277.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Look like the girls aren't asleep yet.{/i}"
    scene expression ("images/episode8/278.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Wonder what they're up to?{/i}"
    scene expression ("images/episode8/279.webp") with dissolve
    patricia "Baik ... Aku suka seseorang, tapi ..."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Sounds like they are talking about boys. Let's see if I can hear them from here.{/i}"
    scene expression ("images/episode8/280.webp") with dissolve
    denise "Jadi? Siapa dia?"
    patricia "Aku tidak akan memberitahumu namanya. Bagaimana jika Anda mengenalnya?"
    denise "Bagaimana saya bisa tahu? Satu -satunya orang yang saya kenal di kota ini adalah kalian."

    scene expression ("images/episode8/281_shy.webp") with dissolve
    patricia "Saya tahu, tapi saya tidak tahu ... itu aneh bagi saya."
    scene expression ("images/episode8/282_smile.webp") with dissolve
    denise "Baik, jangan beri tahu saya namanya. Jadi? Apa yang dia suka?"
    scene expression ("images/episode8/281_smile.webp") with dissolve
    patricia "Dia bodoh!"
    scene expression ("images/episode8/282_laugh.webp") with dissolve
    denise "Haha ... cinta muda. Saya merindukannya."
    scene expression ("images/episode8/282_curious.webp") with dissolve
    denise "Kenapa dia bodoh? Apa yang dia lakukan padamu?"
    scene expression ("images/episode8/281_shy.webp") with dissolve
    patricia "Tidak ada apa-apa!"
    scene expression ("images/episode8/282_laugh.webp") with dissolve
    denise "Itu masalahnya? Dia tidak melakukan sesuatu untuk Anda? Apakah Anda ingin dia?"
    scene expression ("images/episode8/281_surprised.webp") with dissolve
    patricia "Mustahil! Dia akan memisahkanku."
    scene expression ("images/episode8/282_surprised.webp") with dissolve
    denise "Apa? Dia akan apa?"
    scene expression ("images/episode8/281_scared.webp") with dissolve
    patricia "Maksudku, dia akan menghancurkan hatiku."
    scene expression ("images/episode8/282_curious.webp") with dissolve
    denise "Apakah Anda yakin itu yang Anda maksud?"
    scene expression ("images/episode8/281_shy.webp") with dissolve
    patricia "Mungkin?"
    scene expression ("images/episode8/282_smile.webp") with dissolve
    denise "Anda tahu Anda bisa berbicara dengan saya, bukan?"
    scene expression ("images/episode8/281_smile.webp") with dissolve
    patricia "Ya?"
    scene expression ("images/episode8/282_laugh.webp") with dissolve
    denise "Lalu bicara padaku, sayang. Anda tidak ingin memberi saya nama, baik, tetapi Anda harus memberi tahu saya apa yang terjadi di dalam kepala cantik Anda itu."
    scene expression ("images/episode8/281_smile.webp") with dissolve
    patricia "Yah, dia sangat bodoh, tapi lucu dan menjengkelkan, tapi lucu. Aku tidak tahu. Saya yakin saya bisa mengandalkannya, tetapi pada saat yang sama saya tidak berpikir dia menyukai saya."
    scene expression ("images/episode8/282_curious.webp") with dissolve
    denise "Jadi dia lucu, lucu dan Anda yakin Anda bisa mengandalkannya dan dia akan selalu ada untuk Anda jika Anda membutuhkan?"
    scene expression ("images/episode8/281_laugh.webp") with dissolve
    patricia "Anda lupa bodoh, sombong dan menjengkelkan."
    scene expression ("images/episode8/282_smile.webp") with dissolve
    denise "Mungkinkah Anda menjadi teman baik sehingga Anda berakhir di zona teman?"
    scene expression ("images/episode8/281_normal.webp") with dissolve
    patricia "Saya tidak tahu, [auntie]. Hanya saja aku tidak yakin dia benar untukku."
    scene expression ("images/episode8/282_smile.webp") with dissolve
    denise "Saya bukan yang terbaik untuk memberi Anda nasihat, karena Anda tahu situasi saya. Saya tidak menemukan yang tepat dan yang saya pikir adalah Tuan benar .... yah, dia selingkuh."
    scene expression ("images/episode8/281_curious.webp") with dissolve
    patricia "Itulah mengapa kalian berdua bercerai?"
    scene expression ("images/episode8/282_normal.webp") with dissolve
    denise "Tidak yakin apakah itu alasan utama."
    scene expression ("images/episode8/281_surprised.webp") with dissolve
    patricia "Apa maksudmu?"
    scene expression ("images/episode8/282_smile.webp") with dissolve
    denise "Saya tidak mengatakan bahwa saya akan dapat memaafkannya, karena sejujurnya saya benar -benar lega bahwa saya akhirnya punya alasan untuk menceraikannya."
    scene expression ("images/episode8/281_normal.webp") with dissolve
    patricia "Jika Anda tidak lagi mencintainya mengapa Anda menunggu alasannya?"
    scene expression ("images/episode8/282_sad.webp") with dissolve
    denise "Karena saya selalu berpikir dia adalah orang yang tepat untuk saya dan setelah waktu yang lama adalah normal untuk tidak merasakan hal yang sama seperti sebelumnya."
    scene expression ("images/episode8/282_normal.webp") with dissolve
    denise "Saya menikah ketika saya berusia 20 tahun. Dia adalah pacar pertama saya dan saya adalah pacar pertamanya. Kami sudah bersama selama 5 tahun dan semua orang terus memberi tahu kami bahwa kami adalah pasangan dan barang -barang yang sempurna."
    scene expression ("images/episode8/281_sad.webp") with dissolve
    patricia "Namun Anda masih bercerai."
    scene expression ("images/episode8/282_normal.webp") with dissolve
    denise "Ya. Dan sejak itu, saya sudah berkencan dengan pria lain dan meskipun mereka tidak cocok, itu bagus. Senang bertemu orang, memiliki banyak hubungan. Saya tidak mengatakan Anda harus menjadi ho."
    scene expression ("images/episode8/282_smile.webp") with dissolve
    denise "But you'll discover yourself more. So maybe there isn't such a thing as \"the right one\", so you should go out, try things out for yourself and if there is a \"right one\"Anda tidak akan pernah tahu kecuali Anda mencoba."
    scene expression ("images/episode8/281_smile.webp") with dissolve
    patricia "Terima kasih, [auntie]. Anda yang terbaik."
    scene expression ("images/episode8/282_flirty.webp") with dissolve
    denise "Sekarang kita lebih terbuka, seberapa besar dia?"
    scene expression ("images/episode8/281_normal.webp") with dissolve
    patricia "Umm ... dia satu tahun lebih tua dariku."
    scene expression ("images/episode8/282_laugh.webp") with dissolve
    denise "Anda mengatakan bahwa dia akan mencabik -cabik Anda. Seberapa besar dia dan bagaimana Anda tahu?"
    scene expression ("images/episode8/281_shy.webp") with dissolve
    patricia "Maksudmu, di bawah sana?"
    scene expression ("images/episode8/282_smile.webp") with dissolve
    denise "Ya, di bawah sana. Saya tidak membeli heat your heart. Tidak ada yang Anda katakan tentang dia menyarankan Anda berpikir dia mungkin menghancurkan hati Anda. Jadi? Saya mendengarkan."
    scene expression ("images/episode8/281_shy.webp") with dissolve
    patricia "Saya mendengar sesuatu."
    scene expression ("images/episode8/282_smile.webp") with dissolve
    denise "Jangan khawatir sayang, jika dia mencintaimu, itu tidak peduli seberapa besar dia, dia akan berhati -hati untuk tidak menyakitimu."
    scene expression ("images/episode8/281_curious.webp") with dissolve
    patricia "Bisakah dia menyakitiku?"
    scene expression ("images/episode8/282_smile.webp") with dissolve
    denise "Jangan khawatir sayang, aku yakin dia tidak bisa melukaimu."
    scene expression ("images/episode8/281_laugh.webp") with dissolve
    patricia "Ya, Anda mungkin benar."
    scene expression ("images/episode8/281_smile.webp") with dissolve
    patricia "Senang memiliki seseorang untuk diajak bicara tentang hal -hal semacam ini. Aku akan merindukanmu saat kau pergi."
    scene expression ("images/episode8/282_curious.webp") with dissolve
    denise "Mengapa Anda tidak berbicara dengan [mom] Anda? Saya yakin dia ingin membantu Anda. Bagaimanapun, itu adalah [mom] Anda yang membantu saya di tempat pertama."
    scene expression ("images/episode8/281_shy.webp") with dissolve
    patricia "Dia [mom] saya. Aku tidak tahu..."
    scene expression ("images/episode8/282_laugh.webp") with dissolve
    denise "Cobalah untuk membuka lebih banyak padanya. Saya yakin dia ingin membantu Anda, tetapi jika tidak, saya akan selalu ada di sini untuk Anda."
    scene expression ("images/episode8/281_smile.webp") with dissolve
    patricia "Terima kasih, [auntie]."
    scene expression ("images/episode8/283.webp") with dissolve
    denise "Kemarilah. Beri aku pelukan."
    scene expression ("images/episode8/284.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode8/285.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit. [aunt!c] Denise is looking right at me. Time to bail!{/i}"
    scene expression ("images/episode8/286.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode8/287.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}So Tris has finally found someone. Something sounds off and maybe a bit too familiar, but she can't be talking about me.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I mean, yeah. I do annoy her and have a big dick, but I'm pretty sure I'm not the only one.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It can't be me. I'm her [brother].{/i}"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
