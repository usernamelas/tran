image ep3_003 = Movie(play="video/episode3/003.webm", image="images/episode3/004.webp", loop = False)
image ep3_405 = Movie(play="video/episode3/405.webm", loop=True)
image ep3_407 = Movie(play="video/episode3/407.webm", loop=True)
image ep3_425 = Movie(play="video/episode3/425.webm", loop=True)
image ep3_426 = Movie(play="video/episode3/426.webm", loop=True)
image ep3_428 = Movie(play="video/episode3/428.webm", loop=True)

label episode3:
    stop music fadeout 4.0

    call episode3_morning from _call_episode3_morning

    call episode3_goShopping from _call_episode3_goShopping

    call episode3_shopping from _call_episode3_shopping

    call episode3_back_home from _call_episode3_back_home

    call episode3_movie_night from _call_episode3_movie_night

    call episode3_charlote_night from _call_episode3_charlote_night

    call episode3_emma_morning from _call_episode3_emma_morning

    call episode3_callGirls from _call_episode3_callGirls

    call episode3_beach from _call_episode3_beach

    if ep3_lieGirls == True:
        if lisa_path == True:
            call episode3_dateLisa from _call_episode3_dateLisa
        else:
            call episode3_dateLauren from _call_episode3_dateLauren
    else:
        pass


    return

label episode3_morning:
    scene expression ("images/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(1, 3) with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_newEpisode
    show screen ui_message("The next morning") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message


    $ progress = 31
    scene expression ("images/episode3/001.webp") with dissolve
    charlotte "Bangun sayang. Kami memiliki hal -hal yang harus dilakukan hari ini!"
    scene expression ("images/episode3/002.webp") with dissolve
    toby "Lima menit lagi."
    charlotte "Ayo, sayang. Ini sudah jam 11 pagi."

    show ep3_003 with dissolve
    toby "Itu bukan alasan untuk bangun. Saya tidak punya apa -apa untuk dilakukan hari ini!"
    scene expression ("images/episode3/004.webp")
    hide ep3_003
    charlotte "Mungkin Anda tidak, tetapi saya punya banyak hal untuk dilakukan dan saya membutuhkan bantuan Anda."
    toby "Apa yang harus kita lakukan?"
    charlotte "Malam ini [father] Anda dan saya memiliki acara penggalangan dana dan saya butuh gaun."
    toby "Kedengarannya seperti itu masalah Anda."
    scene expression ("images/episode3/005.webp") with dissolve
    charlotte "Oh, jangan seperti itu, sayang. Apakah Anda benar -benar membiarkan [mother] Anda berbelanja sendirian?"
    toby "Ambil Tris!"
    charlotte "Anda tahu dia punya sekolah hari ini."
    scene expression ("images/episode3/006.webp") with dissolve
    toby "Apakah Anda yakin ingin pergi ke pesta itu dan berpura -pura menjadi pasangan yang sempurna? Maksudku, kita berdua tahu bahwa jauh dari kebenaran."
    scene expression ("images/episode3/007.webp") with dissolve
    charlotte "Mungkin kita tidak, tapi pergi bisa membantu hubungan kita. Aku harus berada di sana sayang."
    charlotte "Saya perlu mendukungnya. Bagaimanapun, dia adalah suamiku. Jenis wanita seperti apa saya jika saya tidak berada di sisinya."
    scene expression ("images/episode3/008.webp") with dissolve
    charlotte "Selain itu, saya mendengar akan ada makanan yang luar biasa di sana. Dan bagaimana saya bisa mengatakan tidak untuk itu?"
    toby "Baik, tapi tolong jangan minum. Kami berdua tahu Anda tidak terlalu baik saat alkohol terlibat."
    scene expression ("images/episode3/009.webp") with dissolve
    charlotte "Berbicara tentang alkohol. Maaf jika saya mengambilnya terlalu jauh tadi malam. Saya cukup sia -sia dan memiliki satu gelas terlalu banyak."
    toby "Anda tidak perlu meminta maaf. Anda tidak berlebihan dengan apa pun."
    charlotte "Bagus, karena saya tidak ingat banyak tentang tadi malam, hanya saja Anda meminta saya untuk menari."
    scene expression ("images/episode3/010.webp") with long_dissolve
    toby "Untuk apa itu?"
    scene expression ("images/episode3/011.webp") with dissolve
    charlotte "Terima kasih telah membawaku ke tempat tidur tadi malam. Akan sangat buruk jika Tris melihat saya seperti itu."
    charlotte "Anda tahu bagaimana dia bisa."
    scene expression ("images/episode3/012.webp") with dissolve
    toby "Tempat tidur apa? Aku meninggalkanmu sendirian untuk tidur di sofa."
    scene expression ("images/episode3/013.webp") with dissolve
    charlotte "Ah, benarkah? Apakah Anda benar -benar berpikir saya tidak? Saya hanya lelah dan saya menyukai perhatian. Itu menyenangkan."
    charlotte "Dan omong -omong. Anda benar -benar harus menelepon seseorang segera untuk memperbaiki loteng, karena saya mungkin ingin menerima tawaran Anda."
    toby "Menawarkan? Apa yang kamu bicarakan?"
    scene expression ("images/episode3/014.webp") with dissolve
    charlotte "Jangan bermain bodoh denganku. Aku mendengarmu."
    scene expression ("images/episode3/015.webp") with fade
    toby "{size=12}{color=#FDCA6E}* remembering *{/color}{/size}\n{i}Sorry [mom]. I'm going to fix up the attic and let you sleep there with me whenever you feel like it.{/i}"
    scene expression ("images/episode3/014.webp") with fade
    toby "Saya pikir Anda mengatakan Anda tidak bisa mengingat apa pun dari tadi malam."
    scene expression ("images/episode3/016.webp") with dissolve
    charlotte "Ya, yah ... mungkin aku berbohong."
    charlotte "Oke, waktu berpakaian dan mendapatkan sesuatu untuk dimakan, kami memiliki hari yang panjang di depan."
    toby "Apakah saya benar -benar harus pergi berbelanja dengan Anda?"
    scene expression ("images/episode3/017.webp") with dissolve
    charlotte "Jangan terlalu lama!"

    return


label episode3_goShopping:
    $ progress = 32
    show screen ui_message("A short time later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/018.webp") with dissolve
    hide screen ui_message
    charlotte "Itu sepeda yang bagus. Apakah Anda merindukan sepeda lama Anda setiap kali Anda melihatnya?"
    scene expression ("images/episode3/019.webp") with dissolve
    toby "Nah. Saya tidak benar -benar merindukannya. Maksudku, itu tidak seperti yang lama, tapi itu masih cukup bagus."
    charlotte "Apa yang kamu bicarakan?"
    scene expression ("images/episode3/020.webp") with dissolve
    toby "Oh. Apakah saya lupa memberi tahu Anda? Itu sepedaku. Bos saya memberikannya kepada saya. Dia mengatakan bahwa saya akan membutuhkan cara untuk berkeliling kota."
    charlotte "Benar-benar? Dia pasti sangat ingin Anda memberi Anda sepeda di hari pertama Anda."
    scene expression ("images/episode3/021.webp") with dissolve
    charlotte "Harap berhati -hati. Saya tidak ingin menghabiskan sebulan mengawasi Anda lagi di rumah sakit."
    toby "Jangan khawatir, [mom]. Saya lebih dewasa sekarang dan saya jauh lebih aman dari sebelumnya."
    scene expression ("images/episode3/022.webp") with dissolve
    toby "Jika Anda mau, kami dapat mengambil sepeda saya sehingga Anda dapat melihat sendiri seberapa aman saya."
    charlotte "Sepeda Anda adalah dua kursi. Di mana Tris akan duduk?"
    scene expression ("images/episode3/023.webp") with dissolve
    toby "Saya pikir Anda bilang dia punya sekolah hari ini?."
    charlotte "Dia tidak pernah memaafkan saya jika dia tahu kami pergi berbelanja tanpa dia."
    toby "Lalu kenapa saya di sini lagi?"
    scene expression ("images/episode3/024.webp") with dissolve
    charlotte "Nah, siapa yang akan membawa tas kami? Siapa yang akan mengantar kita?"
    toby "Banyak manja?"
    charlotte "Bisa aja. Jangan berpura -pura bahwa Anda tidak suka berbelanja dengan [mom] Anda."
    toby "Apakah saya benar -benar perlu menjawabnya?"
    scene expression ("images/episode3/025.webp") with dissolve
    charlotte "Potong, potong! Waktu adalah uang."

    scene expression ("images/episode3/026.webp") with long_dissolve
    charlotte "Jadi ini sekolah Tris?"
    scene expression ("images/episode3/027.webp") with dissolve
    toby "Yup. Tampaknya agak kecil jika Anda bertanya kepada saya."
    charlotte "Mungkin di sini akan lebih mudah baginya untuk berteman, karena di sekolah yang lebih kecil semua orang tahu semua orang."
    toby "Ya, mungkin."
    scene expression ("images/episode3/028.webp") with dissolve
    charlotte "Dan siapa tahu, mungkin dia akhirnya akan mendapatkan pacar."
    scene expression ("images/episode3/029.webp") with dissolve
    toby "Apakah dia benar -benar tidak pernah punya pacar?"
    scene expression ("images/episode3/028.webp") with dissolve
    charlotte "Sejauh yang saya tahu, tidak. Dia tidak pernah memilikinya. Entah dia sangat pandai menyimpan rahasia atau dia benar -benar belum punya pacar."
    charlotte "Ngomong -ngomong, kami tidak pernah membicarakannya. Bagaimana hari pertama Anda di tempat kerja? Saya ingat Anda memberi tahu saya sesuatu seperti Anda mendapatkan 00 dalam satu hari."
    charlotte "Itu tidak buruk untuk hari pertama Anda."
    scene expression ("images/episode3/030.webp") with dissolve
    toby "Saya bilang saya mendapatkan, 000."
    scene expression ("images/episode3/031.webp") with dissolve
    charlotte "Benar-benar? Itu bagus! Maksud saya, itulah yang saya pikirkan, tetapi saya tidak yakin apakah saya salah paham kemarin."
    charlotte "Cara untuk pergi, sayang. Bagaimana Anda melakukannya?"
    scene expression ("images/episode3/029.webp") with dissolve
    if toby_job == 0:
        toby "Nah, Nyonya Darlene menyuruh saya menjual apartemen dan kemudian dia menghilang."
        toby "Saya terkejut. Dia baru saja meninggalkan saya di sana di tengah -tengah apartemen sendirian dengan klien dan saya tidak tahu apa yang harus dilakukan."
        scene expression ("images/episode3/028.webp") with dissolve
        charlotte "Sama seperti itu? Dia mempercayaimu?"
        scene expression ("images/episode3/029.webp") with dissolve
        toby "Ya. Dia mengatakan kepada saya untuk tidak pergi di bawah 100 ribu dan kemudian dia berjalan keluar."
        toby "Jadi setelah bernegosiasi dengan klien kami menetap di 101k."
        toby "Setelah itu, ketika Ny. Darlene akhirnya muncul kembali, dia mengatakan sesuatu seperti, apartemen itu hanya bernilai 80k, tetapi saya senang Anda berhasil menjualnya seharga 101k. Jadi dia memberi saya tambahan atas harga yang dia inginkan."
        scene expression ("images/episode3/028.webp") with dissolve
        charlotte "Wow, dia pasti sangat menyukaimu. Saya sangat senang Anda menemukan pekerjaan yang baik."
        charlotte "Saya ingin tahu, mari kita katakan Anda menjual apartemen seharga 110 ribu, dia akan memberi Anda 10 ribu tambahan?"
        scene expression ("images/episode3/029.webp") with dissolve
        toby "Saya meragukannya, tapi itu akan menyenangkan. Apa pun. , 000 cukup baik untuk saya."
    else:

        toby "Yah, saya bertaruh dengan Nyonya Katrina dan saya menang!"
        scene expression ("images/episode3/031.webp") with dissolve
        charlotte "Sama seperti itu? Anda bertaruh dia, 000? Apa yang akan terjadi jika Anda kalah?"
        scene expression ("images/episode3/029.webp") with dissolve
        toby "Tidak ada yang saya kira. Tapi pekerjaan itu menyenangkan."
        scene expression ("images/episode3/028.webp") with dissolve
        charlotte "Saya tidak tahu harus berkata apa, [toby!c]. Saya tidak berpikir itu baik untuk Anda. Jadi apa sebenarnya pekerjaan Anda di sana?"
        scene expression ("images/episode3/029.webp") with dissolve
        toby "Nah, tugas saya adalah menyambut orang dan mengundang mereka di klub. Kebanyakan perempuan."
        scene expression ("images/episode3/028.webp") with dissolve
        charlotte "Itu pintar. Menempatkan pria tampan di pintu masuk dan membuat para gadis masuk ke dalam klub."
        scene expression ("images/episode3/029.webp") with dissolve
        toby "Anda akan membuat saya memerah. Saya tidak terlalu tampan. Saya hanya ... rata -rata!"
        scene expression ("images/episode3/028.webp") with dissolve
        charlotte "Omong kosong!"

    scene expression ("images/episode3/032.webp") with dissolve
    charlotte "Bagaimanapun. Di sinilah sang putri."
    scene expression ("images/episode3/033.webp") with dissolve
    patricia "Hai teman -teman. Apa yang kalian berdua lakukan di sini? Apakah saya melakukan sesuatu yang salah?"
    scene expression ("images/episode3/034.webp") with dissolve
    toby "Kami akan pergi ..."
    scene expression ("images/episode3/035.webp") with dissolve
    charlotte "Untuk mengunjungi [aunt] Denise. Dia mengatakan bahwa dia membutuhkan bantuan di sekitar pertanian."
    scene expression ("images/episode3/036.webp") with dissolve
    toby "Ya ... itu benar. Dia baru saja menelepon pagi ini. Sesuatu tentang memerah susu sapi."
    scene expression ("images/episode3/037.webp") with dissolve
    patricia "Tidak bisakah aku tinggal di rumah?"
    scene expression ("images/episode3/035.webp") with dissolve
    charlotte "Apakah Anda benar -benar ingin saya memberi tahu [auntie] Anda bahwa Anda tidak ingin melihatnya?"
    scene expression ("images/episode3/037.webp") with dissolve
    patricia "Saya ingin melihatnya, tetapi setiap kali kita pergi ke sana, dia mencoba mengajari saya cara memerah susu sapi dan melakukan hal -hal pertanian."
    scene expression ("images/episode3/035.webp") with dissolve
    charlotte "Anda tidak pernah tahu kapan Anda membutuhkan keterampilan itu."
    scene expression ("images/episode3/038.webp") with dissolve
    patricia "Tidak seperti yang tidak pernah?"
    scene expression ("images/episode3/034.webp") with dissolve
    toby "Terlambat sekarang. Kami sudah pergi!"
    scene expression ("images/episode3/037.webp") with dissolve
    patricia "Tapi dia tinggal sejauh ini dari sini dan saya perlu mengerjakan pekerjaan rumah untuk sekolah besok."
    scene expression ("images/episode3/039.webp") with dissolve
    charlotte "Jangan khawatir sayang. Kami hanya satu jam lagi."
    scene expression ("images/episode3/037.webp") with dissolve
    patricia "Tapi saya tidak punya pakaian kerja. Saya meninggalkan semua pakaian lama saya saat kami pindah."
    scene expression ("images/episode3/039.webp") with dissolve
    charlotte "Aku juga, sayang, tapi jangan khawatir, kita akan berbelanja dulu!"
    scene expression ("images/episode3/040.webp") with dissolve
    charlotte "Ayo [toby!c]. Kami tidak punya waktu sepanjang hari."
    scene expression ("images/episode3/041.webp") with dissolve
    patricia "Yay."
    charlotte "Saya sangat menyukai antusiasme."
    patricia "Saya bersikap sarkastik."
    charlotte "Saya tidak bisa memberi tahu!"

    return


label episode3_shopping:

    $ progress = 33
    default episode3_shopping_choice = None

    scene expression ("images/episode3/042.webp") with dissolve
    charlotte "Di sinilah kita. Mari kita lihat apakah mereka memiliki pakaian pertanian."
    patricia "Haruskah kita benar -benar membeli pakaian hanya untuk satu kesempatan? Apakah kita suka miskin?"
    scene expression ("images/episode3/043.webp") with dissolve
    charlotte "Selama kita memiliki satu sama lain, kita tidak miskin."
    patricia "Oke [mom]. Pastikan Anda membayar pakaian dengan cinta Anda untuk kami."
    scene expression ("images/episode3/044.webp") with dissolve
    patricia "Saya pergi ke sana. Anda ikut dengan saya, atau Anda pergi dengan [mom]?"
    scene expression ("images/episode3/045.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What should I do? Should I help Tris or [mom]?{/i}"
    menu:
        "{i} pergi dengan Tris {/i}":
            $ episode3_shopping_choice = 0
            call episode3_shopping_patricia from _call_episode3_shopping_patricia
        "{i} pergi dengan [mom] {/i}":

            $ episode3_shopping_choice = 1
            call episode3_shopping_charlotte from _call_episode3_shopping_charlotte
    $ progress = 34
    scene expression ("images/episode3/045.webp") with dissolve

    if episode3_shopping_choice == 0:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see if [mom] needs any help.{/i}"
        call episode3_shopping_charlotte from _call_episode3_shopping_charlotte_1
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see if Tris needs any help.{/i}"
        call episode3_shopping_patricia from _call_episode3_shopping_patricia_1
    $ progress = 35
    call episode3_shopping_dressingRoom from _call_episode3_shopping_dressingRoom

    return


label episode3_shopping_patricia:
    scene expression ("images/episode3/046.webp") with dissolve
    toby "Jadi? Apa yang kita cari?"
    patricia "Saya tidak tahu. Sesuatu yang lucu? Mungkin beberapa celana pendek dan kemeja?"
    scene expression ("images/episode3/047.webp") with dissolve
    toby "Anda menyadari bahwa Anda pergi ke pertanian, kan? Mengapa bagian yang lucu?"
    patricia "Saya masih bisa terlihat lucu dan modis di sana."
    toby "Saya yakin sapi akan menghargainya."
    scene expression ("images/episode3/048.webp") with dissolve
    patricia "Moron!"
    scene expression ("images/episode3/049.webp") with long_dissolve
    toby "Kemarilah ... biarkan aku melihat bagaimana ini akan terlihat padamu."
    scene expression ("images/episode3/050.webp") with dissolve
    patricia "Apakah kamu bahagia?"
    toby "Hmm ... kamu terlihat persis seperti cowgirl. Mungkin tambahkan beberapa sepatu bot dan Anda akan cocok dengan baik."
    scene expression ("images/episode3/051.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    menu:
        "{i} [JGR] Flirt {/i}"(csq="Tris +1 & Galeri Gambar"):
            $ patricia_rel += 1
            $ unlockImage(persistent.patricia_06)
            toby "Masukkan lidah itu ke dalam mulut Anda sebelum saya datang dengan ide."
            scene expression ("images/episode3/052.webp") with dissolve
            patricia "Aku [sister], bodoh!"
            toby "Aku pun mencintaimu!"
        "{i} don \ 't flirt {/i}":
            pass
    patricia "Kemana kamu pergi sekarang?"
    scene expression ("images/episode3/053.webp") with dissolve
    toby "Saya akan mencari pakaian cowgirl!"
    scene expression ("images/episode3/054.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Speaking of cowgirl outfits. I think this might be exactly what she needs.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Wait, what am I doing? It's not like we're actually going to see [aunt] Denise.{/i}"
    scene expression ("images/episode3/055.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But for the sake of the game it's totally worth making her try on this outfit.{/i}"
    scene expression ("images/episode3/056.webp") with dissolve
    toby "Anda menyadari bahwa [auntie] tidak memiliki kolam renang?"
    scene expression ("images/episode3/057.webp") with dissolve
    patricia "Saya tidak ingin lelucon Anda."
    patricia "Apa pendapat Anda tentang baju renang ini? Karena kita tinggal sangat dekat dengan pantai, saya berpikir mungkin saya harus mendapatkan satu lagi."
    scene expression ("images/episode3/058.webp") with dissolve
    toby "Mengapa Anda tidak mencobanya dan saya akan memilih pakaian yang sempurna untuk hari ini. Saya melihat sesuatu di sana."
    patricia "Dingin! Aku akan pergi ke ruang ganti kalau begitu."
    scene expression ("images/episode3/059.webp") with dissolve
    patricia "Dan [toby!c], tolong jangan bawakan pakaian jelek."
    toby "Menurut Anda, orang seperti apa saya?"
    patricia "Itulah mengapa saya memberi tahu Anda!"
    toby "Saya berjanji. Anda akan terlihat hebat."
    scene expression ("images/episode3/060.webp") with dissolve
    patricia "Kejutan saya."

    return


label episode3_shopping_charlotte:
    scene expression ("images/episode3/061.webp") with dissolve
    toby "Jadi? Apa yang kita cari?"
    charlotte "Saya belum yakin. Sesuatu yang elegan, tapi masih seksi, tapi tidak slutty. Saya ingin terlihat seperti wanita seusia saya, tetapi seorang wanita yang berkelas."
    scene expression ("images/episode3/062.webp") with dissolve
    toby "Sempurna. Saya mengerti persis apa yang Anda inginkan."
    charlotte "Benar-benar?"
    toby "No tidak!"
    scene expression ("images/episode3/063.webp") with dissolve
    toby "Jadi izinkan saya meluruskan ini. Anda ingin gaun yang tidak begitu pendek sehingga terlihat slutty, tetapi masih cukup ketat untuk menunjukkan kurva Anda. Mungkin menunjukkan beberapa belahan dada, tetapi tidak terlalu banyak, namun tidak terlalu sedikit?"
    charlotte "Anda semakin dekat."
    toby "Adapun warnanya, sesuatu yang tidak akan meneriakkan perhatian, namun juga tidak boleh dilewatkan."
    scene expression ("images/episode3/064.webp") with dissolve
    charlotte "Saya suka cara Anda berpikir. Jadi, apa yang kamu katakan? Manakah dari keduanya yang akan terlihat lebih baik pada saya?"
    menu:
        "{i} [JGR] Flirt {/i}"(csq="Charlotte +1 & Galeri Gambar"):
            $ charlotte_rel += 1
            scene expression ("images/episode3/065.webp") with dissolve
            toby "Ketika Anda terlihat seperti ini, saya tidak berpikir gaun itu akan membantu Anda dengan cara apa pun, tetapi mungkin yang emas lebih dekat dengan apa yang Anda inginkan."
            $ unlockImage(persistent.charlotte_06)
        "{i} don \ 't flirt {/i}":
            toby "Aku tidak tahu benar -benar, tapi aku merasa emas adalah satu -satunya untukmu."
    scene expression ("images/episode3/066.webp") with dissolve
    charlotte "Terima kasih sayang. Saya akan mencobanya dan melihat apa yang Anda pikirkan."
    toby "Senang saya bisa membantu."
    scene expression ("images/episode3/067.webp") with dissolve
    charlotte "Omong-omong. Anda tidak memberi tahu Tris apa yang sebenarnya terjadi, kan? Dia masih berpikir kita akan mengunjungi Denise [aunt]?"
    toby "Yup. Dia tidak tahu."
    toby "Tapi bagaimana Anda mendapatkan tipu muslihat itu?"
    charlotte "Oh, [sister] saya memberi tahu saya pagi ini bahwa dia ingin kami berkunjung segera, karena kami begitu dekat sekarang dan itu memberi saya ide, karena saya tahu seberapa banyak Tris membenci pergi ke pedesaan."
    scene expression ("images/episode3/068.webp") with dissolve
    charlotte "Cukup dengan itu, saya akan mencoba gaun ini."

    return


label episode3_shopping_dressingRoom:
    $ progress = 36

    scene expression ("images/episode3/069.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the hell is taking so long for these women to try on clothes? It's taking like forever.{/i}"
    if patricia_rel >= 4:
        label memory_06:


            scene expression ("images/episode3/070.webp") with dissolve
            patricia "[toby!c] Apakah Anda di sini?"
            toby "Ya, tentu saja. Apa yang kamu butuhkan?"
            scene expression ("images/episode3/071.webp") with dissolve
            patricia "Hanya pendapat Anda tentang sesuatu."
            toby "Ya Tentu!"

            scene expression ("images/episode3/072.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()
            patricia "Jadi? Apa pendapat Anda tentang pakaian renang baru saya?"
            toby "Wow. Maksud saya..."
            toby "Ya, itu terlihat bagus. Anda harus membelinya."
            scene expression ("images/episode3/073.webp") with dissolve
            patricia "Saya tahu, tetapi saya tidak berpikir [mom] mampu membeli sebanyak ini."
            scene expression ("images/episode3/074.webp") with dissolve
            toby "Saya memberi Anda 00 baru kemarin. Anda sudah menghabiskan semuanya?"
            scene expression ("images/episode3/073.webp") with dissolve
            patricia "Tidak, saya hanya menghabiskan hari ini, tetapi pakaian renangnya adalah 40."
            menu:
                "[JGR] Jangan khawatir tentang hal itu. Aku akan memberimu 0 lainnya."(csq="Tris +1 & Gallery Image & Important for Tris' path"):
                    $ patricia_rel += 1
                    $ ep3_kissPatricia = True
                    $ unlockImage(persistent.patricia_07)
                    scene expression ("images/episode3/075.webp") with dissolve
                    patricia "Benar-benar?"
                    scene expression ("images/episode3/074.webp") with dissolve
                    toby "Tentu saja. Anda satu -satunya [sister] saya. Jika saya tidak bisa merusak Anda, lalu siapa yang akan?"
                    scene expression ("images/episode3/076.webp") with dissolve
                    patricia "Terima kasih, terima kasih, terima kasih! Anda yang terbaik."
                    toby "Apa yang bisa saya katakan."
                    scene expression ("images/episode3/077.webp") with dissolve
                    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Did she just kiss my lips?{/i}"
                    scene expression ("images/episode3/078.webp") with dissolve
                    patricia "Apa -apaan [toby!c]. Mengapa Anda menoleh?"
                    toby "Saya tidak tahu apa yang akan Anda lakukan. Saya kebetulan berbalik pada saat yang sama."
                    toby "Lain kali, mengapa Anda tidak memberi saya peringatan alih -alih hanya mencium saya."
                    scene expression ("images/episode3/079.webp") with dissolve
                    patricia "Anda menjijikkan. Anda membiarkan [sister] Anda mencium Anda!"
                    toby "Saya tidak melakukan apa -apa."
                    scene expression ("images/episode3/080.webp") with dissolve
                    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What a moron. She kisses me and then she's the one who is mad.{/i}"

                    $ unlockMemory(persistent.memory_06)

                "Saya yakin [mom] akan setuju untuk membayar perbedaannya." if not _in_replay:
                    scene expression ("images/episode3/073.webp") with dissolve
                    patricia "Saya hanya bisa berharap. Bagaimanapun, saya harus mencoba pakaian yang Anda pilih untuk saya."

            $ renpy.end_replay()


    scene expression ("images/episode3/081.webp") with long_dissolve
    charlotte "Jadi? Bagaimana menurutmu? Haruskah saya memakai yang ini malam ini?"

    scene expression ("images/episode3/082.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode3/083.webp")
    charlotte "Jadi? Bagaimana menurutmu?"
    toby "Anda harus membelinya.Wow [mom]. Anda terlihat luar biasa. Gaun itu terlihat sangat bagus untukmu."
    scene expression ("images/episode3/084.webp")
    charlotte "Kamu benar -benar berpikir begitu?"
    toby "Tentu saja. Anda cantik."
    charlotte "Apakah terlalu banyak untuk usia saya?"
    scene expression ("images/episode3/085.webp")
    menu:
        "[JGR] Usia Anda? Apa artinya itu?"(csq="Charlotte +1"):
            $ charlotte_rel += 1
            charlotte "Anda tahu ... Saya bukan 20 lagi. Saya seharusnya tidak memakai gaun ketat ini."
            toby "Omong kosong. Saya berpikir untuk ikut serta untuk memastikan tidak ada yang menculik Anda."
        "Tentu saja tidak.":


            charlotte "Terima kasih sayang. Saya akan menunggu untuk melihat apa yang dikatakan Tris."
    scene expression ("images/episode3/085_1.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/086.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    patricia "Ta da!"
    patricia "Apa yang kalian pikirkan?"
    scene expression ("images/episode3/087.webp") with dissolve
    patricia "Wow [mom]. Kamu terlihat luar biasa."
    patricia "Apa kesempatannya?"
    scene expression ("images/episode3/088.webp") with dissolve
    charlotte "Saya akan pergi ke acara dengan [father] malam ini, jadi saya ingin membeli gaun baru."
    scene expression ("images/episode3/089.webp") with dissolve
    patricia "Saya pikir kita akan [aunt] pertanian Denise?"
    scene expression ("images/episode3/088.webp") with dissolve
    charlotte "Itulah mengapa Anda berpakaian seperti gadis desa?"
    charlotte "Itu terlihat luar biasa bagimu. Tidak dapat menunggu sampai Denise mendengar tentang pakaian baru Anda."
    scene expression ("images/episode3/089.webp") with dissolve
    patricia "Mendengar? Bagaimana dengan melihat? Apakah kita akan melihat [auntie] hari ini?"
    scene expression ("images/episode3/090.webp") with dissolve
    charlotte "Darimana kamu mendapatkan ide itu? Kami tidak punya waktu untuk itu, sayang. Sudah kubilang. Malam ini saya memiliki hal lain yang terjadi."
    scene expression ("images/episode3/091.webp") with dissolve
    patricia "Oh tidak. Anda berantakan dengan saya. Aku akan mendapatkanmu!"
    scene expression ("images/episode3/092.webp") with dissolve
    patricia "Dan kamu! Anda tahu tentang ini?"
    toby "Saya tidak ada hubungannya dengan ini."
    scene expression ("images/episode3/093.webp") with dissolve
    patricia "Anda tidur di lantai."
    toby "Layak untuk melihat Anda dalam hal itu."
    scene expression ("images/episode3/094.webp") with dissolve
    patricia "Saya akan berubah."
    scene expression ("images/episode3/088.webp") with dissolve
    charlotte "Jangan mengembalikan pakaian itu. Saya membelinya untuk Anda. Anda tidak pernah tahu kapan Anda akan membutuhkannya."
    scene expression ("images/episode3/094.webp") with dissolve
    patricia "Apa pun!"
    scene expression ("images/episode3/095.webp") with dissolve
    charlotte "Itu sepadan!"
    if charlotte_rel >= 5:

        charlotte "Jangan pergi ke mana pun, saya membutuhkan pendapat seorang pria tentang hal lain."
        toby "Tentu, [mom]. Apa pun."
        show screen ui_message("A few minutes later") with long_dissolve
        $ ui.saybehavior()
        $ ui.interact()
        label memory_07:


            scene expression ("images/episode3/096.webp") with dissolve
            hide screen ui_message
            charlotte "[toby!c]. Apakah kamu di sini?"
            toby "Ya [mom]. Butuh sesuatu?"
            charlotte "Silakan datang ke sini sebentar."

            scene expression ("images/episode3/097.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()
            $ unlockImage(persistent.charlotte_07)
            charlotte "Untuk saat ini lupakan bahwa saya adalah [mother] Anda. Beri aku pendapat jujurmu sebagai seorang pria. Apakah ini cukup seksi?"
            scene expression ("images/episode3/098.webp") with dissolve
            toby "Uhum ... maksudku ..."
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}If I ever end up with a woman as beautiful as [mom] I'm going to live in her pussy.{/i}"
            scene expression ("images/episode3/099.webp") with dissolve
            charlotte "Uhum ... Terima kasih atas pendapat jujur Anda. Tidak ada kata yang dibutuhkan."
            scene expression ("images/episode3/100.webp") with dissolve
            toby "Apa?"
            scene expression ("images/episode3/101.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck my life. Not again!{/i}"
            scene expression ("images/episode3/102.webp") with dissolve
            charlotte "Saya akan berubah sekarang. Terima kasih sayang."
            toby "Uhum ... selamat datang?"

            $ unlockMemory(persistent.memory_07)
            $ renpy.end_replay()
    else:

        charlotte "Saya akan berubah kembali."
    scene expression ("images/episode3/103.webp") with dissolve
    patricia "Dimana [mom]?"
    toby "Dia masih di ruang ganti. Dia harus segera selesai."
    patricia "Aku masih membencimu karena berbohong padaku."
    scene expression ("images/episode3/104.webp") with dissolve
    toby "Aku tidak berbohong padamu. Aku hanya tidak memberitahumu seluruh kebenaran."
    patricia "Aku membenci kalian berdua. Saya bisa mencari pakaian yang lebih bagus."
    scene expression ("images/episode3/105.webp") with dissolve
    charlotte "Oh tolong ... jangan menjadi bayi seperti itu. Itu lucu."
    patricia "Untukmu!"
    charlotte "Dan [toby!c]."
    charlotte "Bagaimanapun. Mari kita bayar untuk semua ini dan mungkin ambil kopi saat kita ada di sini."

    return


label episode3_back_home:
    $ progress = 37

    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/106.webp") with dissolve
    hide screen ui_message
    patricia "Kami akhirnya pulang. Tidak bisa menunggu untuk berbaring."
    charlotte "Apakah Anda terlalu muda untuk lelah hanya karena berbelanja?"
    patricia "Saya mungkin terlihat muda, tetapi saya memiliki jiwa tua."
    scene expression ("images/episode3/107.webp") with dissolve
    toby "Apakah Anda masih percaya pada reinkarnasi?"
    scene expression ("images/episode3/108.webp") with dissolve
    patricia "Saya yakin Anda lebih baik diam jika Anda tidak ingin tidur di lantai."
    scene expression ("images/episode3/107.webp") with dissolve
    toby "Maaf ratu saya. Saya lupa bahwa dalam kehidupan lain Anda adalah ratu kerajaan yang hebat."
    scene expression ("images/episode3/108.webp") with dissolve
    patricia "Itu petani kanan. Jangan membuatku telah membuatmu dicambuk."
    scene expression ("images/episode3/107.webp") with dissolve
    toby "Tidak tahu Anda menjadi BDSM."
    scene expression ("images/episode3/109.webp") with dissolve
    patricia "Bds ... apa?"
    scene expression ("images/episode3/110.webp") with dissolve
    charlotte "Jangan mendengarkan [brother] Anda. Dia baru saja membuat lelucon bodoh."

    scene expression ("images/episode3/111.webp") with fade
    erwin "Kemana saja kamu sepanjang hari? Kami akan terlambat."
    scene expression ("images/episode3/112.webp") with dissolve
    charlotte "Saya pergi membeli gaun untuk acara Anda dan kemudian anak -anak ingin berhenti untuk minum kopi."
    scene expression ("images/episode3/111.webp") with dissolve
    erwin "Tidakkah kamu sudah punya cukup gaun? Mengapa Anda tidak mengenakan salah satunya? Apakah Anda benar -benar perlu membeli yang baru?"
    scene expression ("images/episode3/113.webp") with dissolve
    charlotte "Saya akan berubah. Saya akan berada di bawah dalam satu menit."
    scene expression ("images/episode3/114.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Dammit [dad]. Why do you have to be such a dick!{/i}"
    scene expression ("images/episode3/115.webp") with dissolve
    toby "Sungguh, [dad]? Benar-benar? Beginilah cara Anda memperlakukan istri Anda? Dia mencoba yang terbaik untuk terlihat baik untuk Anda dan ini adalah tanggapan Anda!"
    scene expression ("images/episode3/116.webp") with dissolve
    erwin "Mari kita lihat bagaimana perasaan Anda setelah 20 tahun menikah. Anda pikir Anda sangat pintar sehingga Anda dapat menguliahi saya!"
    toby "Maksud Anda 21 tahun pernikahan."
    toby "Tahukah Anda apa itu kemarin?"
    erwin "Suatu hari di mana saya tidak menghasilkan banyak uang!"
    scene expression ("images/episode3/117.webp") with dissolve
    toby "Itu adalah hari jadi ke -21 Anda, tetapi tentu saja Anda tidak ingat, karena yang Anda pedulikan hanyalah uang!"
    toby "Izinkan saya memberi tahu Anda sesuatu. Dunia tidak berputar di sekitar uang berharga Anda. Itu bukan dari mana kebahagiaan berasal."
    erwin "Seperti Anda tahu apa yang Anda bicarakan. Anda akan melihat berbagai hal secara berbeda ketika Anda seusia saya!"
    scene expression ("images/episode3/118.webp") with dissolve
    toby "Anda mengacau kemarin. Setidaknya malam ini cobalah menjadi lebih dari seorang pria dan hargai apa yang Anda miliki."
    toby "Anda begitu fokus pada apa yang tidak Anda miliki sehingga Anda lupa apa yang Anda miliki."
    scene expression ("images/episode3/119.webp") with dissolve
    erwin "Dan apa yang saya miliki, di samping hutang?"
    toby "Anda memiliki kami!"
    erwin "Saya sangat bersyukur untuk itu. Saya pasti akan meminta uang saat sewa jatuh tempo."
    scene expression ("images/episode3/118.webp") with dissolve
    toby "Mungkin kamu harus!"
    scene expression ("images/episode3/120.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I don't know what's gotten into him, but it's like I don't even recognize him any more. I really hope he's nice to [mom] tonight.{/i}"
    scene expression ("images/episode3/121.webp") with dissolve
    patricia "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n[toby!u]. I'm changing! Don't you know how to knock?"
    toby "Maaf [sis]. Saya tidak bermaksud!"
    patricia "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nOut! Now!"
    scene expression ("images/episode3/122.webp") with dissolve
    erwin "Anda bahkan belum menikah dan para wanita sudah berteriak pada Anda. Semoga beruntung! Anda akan membutuhkannya!"
    scene expression ("images/episode3/123.webp") with dissolve
    toby "Terserah, [dad]."

    scene expression ("images/episode3/124.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    toby "Wow, [mom]. Anda terlihat luar biasa."
    scene expression ("images/episode3/125.webp") with dissolve
    charlotte "Bisa aja. Anda akan membuat saya memerah! Anda sudah melihat saya dalam gaun ini!"
    toby "Anda masih terlihat bagus!"
    charlotte "Kemarilah sayang!"
    scene expression ("images/episode3/126.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/127.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}[mom!c]'s boobs are perfect.{/i}"
    scene expression ("images/episode3/126.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And I need to stop staring at my [mom] like that!{/i}"
    scene expression ("images/episode3/128.webp") with dissolve
    charlotte "Bersikaplah baik dan jaga dengan baik [sister] Anda. Oke?"
    toby "Anda dapat mengandalkan saya, [mom]."
    scene expression ("images/episode3/129.webp") with dissolve
    charlotte "Sampai jumpa malam ini atau semoga besok pagi!"
    toby "Bye [mom]. Bersenang -senanglah malam ini!"
    scene expression ("images/episode3/130.webp") with fade
    toby "Apakah kamu sudah selesai? Bisakah saya masuk?"
    patricia "Belum. Saya masih mencoba pakaian baru."
    toby "Anda mencobanya di toko. Apa gunanya mencobanya lagi?"
    patricia "Mengapa saya harus menjelaskan? Ini tidak seperti yang Anda mengerti."
    toby "Apa pun!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe I'll just go take a shower since the princess won't let me in!{/i}"
    scene expression ("images/episode1/091.webp") with fade
    $ ui.saybehavior()
    $ ui.interact()

    return


label episode3_movie_night:
    $ progress = 38

    show screen ui_message("One hour later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/131.webp") with dissolve
    hide screen ui_message
    toby "Hei [sis]. Apa yang sedang kamu lakukan?"
    scene expression ("images/episode3/132.webp") with dissolve
    patricia "Saya sedang mencari film untuk ditonton. Ingin bergabung?"
    toby "Tentu. Mengapa tidak!"
    patricia "Tapi saya memilih filmnya."
    scene expression ("images/episode3/133.webp") with dissolve
    toby "Biarkan saya menebak. Anda sudah mencari film roman yang belum pernah Anda lihat?"
    patricia "Mungkin?"
    toby "Apakah Anda sudah bosan dengan film -film itu? Anda telah melihat seribu."
    scene expression ("images/episode3/134.webp") with dissolve
    patricia "Mungkin membosankan untuk Anda, karena Anda adalah orang yang menyebalkan dan penipu. Anda mungkin hanya suka menonton film porno."
    scene expression ("images/episode3/135.webp") with dissolve
    toby "Itu adalah hal yang satu kali dan selain itu, saya katakan itu karena saya benar -benar membutuhkan seseorang untuk diajak bicara, bukan agar Anda bisa melemparkannya kembali ke wajah saya."
    toby "Jika saya tahu Anda akan seperti ini, saya tidak akan memberi tahu Anda apa pun."
    scene expression ("images/episode3/134.webp") with dissolve
    patricia "Sudah terlambat sekarang. Kotak Pandora sudah terbuka."
    scene expression ("images/episode3/135.webp") with dissolve
    toby "Apa pun!"
    scene expression ("images/episode3/136.webp") with dissolve
    patricia "Di Sini. Anda memegang laptop, saya menemukan yang bagus. Perhatikan mungkin Anda akan belajar satu atau dua hal!"
    toby "Anda sangat lucu!"
    scene expression ("images/episode3/137.webp") with dissolve
    toby "Saya tidak sabar untuk melihat seperti apa cinta sejati."
    patricia "Saya suka antusiasme Anda!"
    scene expression ("images/episode3/138.webp") with dissolve
    toby "Dan menurut Anda apa yang Anda lakukan?"
    patricia "Diam dan biarkan saya merasa nyaman. Anda orang yang meminta untuk menonton film, jadi menghadapinya!"
    scene expression ("images/episode3/139.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm pretty sure she asked me to join her, but whatever!{/i}"

    show screen ui_message("A short time later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/140.webp") with dissolve
    hide screen ui_message

    toby "Tunggu, bukankah dia sudah punya pacar atau semacamnya? Kenapa dia mencium pria itu?"
    toby "I thought you said that in romantic movies people don't cheat, like \"shitty people\"lakukan dalam kehidupan nyata!"

    scene expression ("images/episode3/141.webp") with dissolve
    patricia "Ya, tapi Anda tidak mengerti. Mereka tidak rukun lagi. Dia brengsek. Dia jatuh cinta dengan pria ini. Dia 10 kali lebih baik dari pacarnya."
    scene expression ("images/episode3/142.webp") with dissolve
    toby "Oh, sekarang saya mengerti. Jadi tidak apa -apa untuk menipu selama Anda melakukannya dengan orang yang Anda cintai."
    toby "Atau jika Anda seorang wanita."
    scene expression ("images/episode3/141.webp") with dissolve
    patricia "Tidak ... tidak seperti itu. Mereka akan segera putus."
    scene expression ("images/episode3/142.webp") with dissolve
    toby "Jadi putus dan kemudian lakukan apa pun yang Anda inginkan dengan pria baru yang Anda sukai. Jangan menciumnya saat Anda sudah punya pacar."
    scene expression ("images/episode3/143.webp") with dissolve
    patricia "Syi! Anda merusak film."
    toby "You're the one who told me to watch a romantic movie with you, so I'll \"learn a thing or two.\""
    patricia "Ya, tapi mereka hanya berciuman. Itu tidak seperti dia kecurangan."
    scene expression ("images/episode3/144.webp") with dissolve
    toby "Ahh, oke ... itu sebabnya dia merobek bra -nya."
    toby "Maksudku ya, dia masih menciumnya, kecuali sekarang dia mencium payudaranya. Itu jauh lebih baik."
    scene expression ("images/episode3/145.webp") with dissolve
    patricia "Oke, jadi mungkin ini bukan contoh terbaik dari romansa."
    patricia "Tapi mereka masih hanya berciuman. Jadi lebih baik dari apa yang Anda lakukan dengan gadis lain itu."

    if ep2_laurenBlowjob == False:
        toby "Aku hanya mencium seorang gadis dan kemudian merasa seperti omong kosong tentang hal itu. Ini tidak lebih buruk dari apa yang mereka lakukan."
        patricia "Ah, benarkah? Saya pikir Anda melakukan sesuatu yang lebih buruk."
        scene expression ("images/episode3/146.webp") with dissolve
        toby "Lebih buruk dari ini? Bung itu baru saja menarik celana dalamnya dan akan menidurinya."
    else:
        scene expression ("images/episode3/146.webp") with dissolve
        toby "Apakah Anda yakin lebih baik dari ini? Dia hanya memberiku blowjob."
        toby "Bung itu baru saja menarik celana dalamnya dan akan menidurinya."
    scene expression ("images/episode3/147.webp") with dissolve
    patricia "Pertama -tama ... mereka tidak bercinta. Mereka bercinta."
    toby "Uhum ..."
    toby "Oh, dan omong -omong, saya pikir Anda tidak suka menonton film porno?"
    patricia "Baik ... film ini bukan contoh terbaik. Ini agak eksplisit dan gadis itu hanya berselingkuh pada pacarnya, tetapi Anda masih harus mengakui. Ini film yang bagus."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And hot, if you're asking me!{/i}"
    scene expression ("images/episode3/148.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fucking hell... Maybe a little bit too hot.{/i}"
    patricia "Hai! Pegang laptop masih."
    toby "Tonton saja filmnya dan tutup mulut."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Good thing she's innocent and doesn't understand what's going on.{/i}"
    scene expression ("images/episode3/149.webp") with dissolve
    patricia "Beri aku itu. Anda bahkan tidak tahu cara memegang laptop."
    scene expression ("images/episode3/150.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit!{/i}"
    patricia "Apakah Anda mendapatkan kesalahan?"
    scene expression ("images/episode3/151.webp") with dissolve
    toby "Tidak, aku tidak. Anda bodoh."
    patricia "Anda mendapatkan Boner dari menonton film romantis. Jenis Pervanya yang melakukan itu?"
    toby "Saya bukan seorang perv. Ini adalah sesuatu yang normal bagi seorang pria untuk terangsang ketika dia melihat adegan seks yang panas."
    scene expression ("images/episode3/152.webp") with dissolve
    patricia "Ya, ya. Yakin Anda bukan orang cabul."
    patricia "Letakkan barang Anda kembali tidur dan biarkan menyelesaikan film."
    scene expression ("images/episode3/153.webp") with dissolve
    toby "Saya tidak bisa hanya menidurkannya. Itu bukan cara kerjanya!"
    patricia "Benar-benar? Lalu bagaimana cara kerjanya?"
    toby "Kami tidak perlu membicarakannya."
    scene expression ("images/episode3/154.webp") with dissolve
    toby "Apa yang sedang kamu lakukan? Saya pikir kami sedang menonton film!"
    scene expression ("images/episode3/155.webp") with fade

    patricia "Tidak. Kami sudah selesai! Kami bermain-mantra-rock-scissors dan pemenangnya, saya, akan bertanya kepada pecundang, Anda, pertanyaan dan Anda harus menjawab."
    toby "Saya kira tidak demikian."
    scene expression ("images/episode3/156.webp") with dissolve
    patricia "Banyak ayam?"
    toby "Saya bukan ayam. Saya hanya tidak ingin menjawab pertanyaan bodoh Anda. Jika Anda ingin tahu sesuatu, cari saja di internet seperti orang lain."
    patricia "Internet penuh dengan omong kosong. Saya ingin mempelajari tangan pertama ini!"
    $ progress = 39
    scene expression ("images/episode3/157.webp") with dissolve
    toby "Bagus! Kami pergi tiga!"
    patricia "Sempurna!"
    menu:
        "{i} rock {/i}":
            scene expression ("images/episode3/160.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
        "{i} kertas {/i}":
            scene expression ("images/episode3/162.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
        "{i} gunting {/i}":
            scene expression ("images/episode3/158.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
    scene expression ("images/episode3/164.webp") with dissolve
    patricia "Awww, sepertinya aku menang!"
    toby "Apa pun. Menembak!"
    scene expression ("images/episode3/166.webp") with dissolve
    patricia "Seberapa sering Anda mendapatkan kesalahan?"
    scene expression ("images/episode3/167.webp") with dissolve
    toby "Benar-benar? Itu pertanyaan pertama Anda?"
    scene expression ("images/episode3/168.webp") with dissolve
    patricia "Ayo. Ini tidak seperti saya pernah punya pacar untuk mempelajari semua hal ini, dan semua gadis seusia saya sudah tahu hal -hal seperti ini."
    scene expression ("images/episode3/167.webp") with dissolve
    toby "Saya meragukannya!"
    toby "Beberapa hari lebih sering daripada yang lain.Oke, baiklah. Beberapa kali sehari. Setiap kali saya merasa terangsang atau saya melihat sesuatu yang seksi, tetapi saya tidak bisa menghitung berapa kali."
    scene expression ("images/episode3/168.webp") with dissolve
    patricia "Apa yang harus Anda lakukan untuk membuatnya hilang?"
    scene expression ("images/episode3/169.webp") with dissolve
    toby "Bahwa [sister] saya adalah pertanyaan yang berbeda!"
    scene expression ("images/episode3/157.webp") with dissolve
    patricia "Apa pun. Saya akan menang dan Anda masih harus tetap menjawab."
    toby "Anda menang!"
    menu:
        "{i} rock {/i}":
            scene expression ("images/episode3/160.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
        "{i} kertas {/i}":
            scene expression ("images/episode3/162.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
        "{i} gunting {/i}":
            scene expression ("images/episode3/158.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
    scene expression ("images/episode3/164.webp") with dissolve
    patricia "Jadi ... apakah Anda harus selalu bermasturbasi untuk membuatnya pergi?"
    toby "Anda curang!"
    patricia "Saya tidak!"
    scene expression ("images/episode3/167.webp") with dissolve
    toby "Apakah semua pertanyaan akan menjadi tentang ini?"
    scene expression ("images/episode3/168.webp") with dissolve
    patricia "Berhenti menghindari jawabannya!"
    scene expression ("images/episode3/167.webp") with dissolve
    toby "TIDAK! Saya bukan wanker kronis. Ya, masturbasi kadang -kadang membantu membuatnya hilang untuk sementara waktu, tetapi kadang -kadang itu hilang dengan sendirinya. Seperti sekarang."
    toby "Boner saya hilang dan saya tidak brengsek!"
    scene expression ("images/episode3/170.webp") with dissolve
    patricia "Anda tidak punya boner lagi?"
    toby "TIDAK! Sekarang bisakah kita kembali ke permainan?"
    patricia "Apakah itu hilang secepat itu ketika Anda juga berhubungan seks?"
    toby "Saya minta maaf, saya tidak mendengarnya. Apakah Anda mengatakan sudah waktunya untuk babak berikutnya? Kenapa, ya itu!"
    scene expression ("images/episode3/157.webp") with dissolve
    patricia "Bagus! Jangan menjawab pertanyaannya!"
    patricia "Pesta Pooper!"
    menu:
        "{i} rock {/i}":
            scene expression ("images/episode3/161.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
        "{i} kertas {/i}":
            scene expression ("images/episode3/163.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
        "{i} gunting {/i}":
            scene expression ("images/episode3/159.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
    scene expression ("images/episode3/165.webp") with dissolve
    toby "Akhirnya."
    scene expression ("images/episode3/171.webp") with dissolve
    toby "Karena Anda belum punya pacar, apakah Anda pernah mencium anak laki -laki?"
    scene expression ("images/episode3/172.webp") with dissolve
    patricia "Ya ... tentu saja saya punya. Maksudku, siapa yang belum mencium seorang anak laki -laki! Ya, saya punya."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She looks like she's lying to me!{/i}"
    scene expression ("images/episode3/171.webp") with dissolve
    toby "Apa kamu yakin?"
    scene expression ("images/episode3/173.webp") with dissolve
    patricia "Mengapa Anda bahkan ingin tahu?"
    scene expression ("images/episode3/171.webp") with dissolve
    toby "Apakah Anda lebih suka pertanyaan seperti yang Anda tanyakan kepada saya?"
    scene expression ("images/episode3/173.webp") with dissolve
    patricia "TIDAK!"
    patricia "Oke, oke! Aku belum mencium siapa pun!"
    scene expression ("images/episode3/174.webp") with dissolve
    toby "Bahkan bukan ciuman sederhana? Tanpa lidah?"
    scene expression ("images/episode3/172.webp") with dissolve
    patricia "Kedengarannya seperti pertanyaan yang berbeda!"

    scene expression ("images/episode3/157.webp") with dissolve
    patricia "Siap untuk babak berikutnya?"
    menu:
        "{i} rock {/i}":
            scene expression ("images/episode3/160.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
        "{i} kertas {/i}":
            scene expression ("images/episode3/162.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
        "{i} gunting {/i}":
            scene expression ("images/episode3/158.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
    scene expression ("images/episode3/164.webp") with dissolve
    toby "Aku bersumpah. Game ini dicurangi."
    scene expression ("images/episode3/166.webp") with dissolve
    patricia "Jadi, apa yang Anda pikirkan saat menyentak? Atau apa yang kamu tonton?"
    scene expression ("images/episode3/174.webp") with dissolve
    toby "Apa dengan pertanyaan -pertanyaan ini?"
    scene expression ("images/episode3/168.webp") with dissolve
    patricia "Cepat atau lambat saya akan punya pacar dan saya perlu memahaminya."
    scene expression ("images/episode3/167.webp") with dissolve
    toby "Pertanyaan ini terlalu pribadi."
    scene expression ("images/episode3/168.webp") with dissolve
    patricia "Bagus. Biarkan saya mengulanginya. Apakah Anda hanya melihat telanjang Emma atau Anda juga menonton film porno?"
    scene expression ("images/episode3/175.webp") with dissolve
    toby "Jadi beginilah cara Anda bermain? Saya tahu persis apa yang akan saya tanyakan selanjutnya."
    scene expression ("images/episode3/168.webp") with dissolve
    patricia "Dan jawaban untuk pertanyaan Anda adalah?"
    scene expression ("images/episode3/175.webp") with dissolve
    toby "Keduanya."
    scene expression ("images/episode3/176.webp") with dissolve
    patricia "Anda adalah cabul [bro]. Apakah semua pria menyukaimu?"
    scene expression ("images/episode3/157.webp") with dissolve
    toby "Ayo Bermain. Giliranku untuk menang."
    patricia "Semoga berhasil dengan itu!"

    menu:
        "{i} rock {/i}":
            scene expression ("images/episode3/161.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
        "{i} kertas {/i}":
            scene expression ("images/episode3/163.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
        "{i} gunting {/i}":
            scene expression ("images/episode3/159.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
    scene expression ("images/episode3/165.webp") with dissolve
    toby "Itu lebih baik."
    scene expression ("images/episode3/171.webp") with dissolve
    toby "Pernahkah Anda meraba diri sendiri?"
    scene expression ("images/episode3/172.webp") with dissolve
    patricia "Ini sangat pribadi!"
    scene expression ("images/episode3/174.webp") with dissolve
    toby "Dan apa yang saya pikirkan ketika saya brengsek bukan?"
    scene expression ("images/episode3/177.webp") with dissolve
    patricia "Ya, saya telah meraba diri!"
    $ unlockImage(persistent.patricia_08)
    scene expression ("images/episode3/169.webp") with dissolve
    toby "Dan aku sudah cabul?"
    scene expression ("images/episode3/168.webp") with dissolve
    patricia "Perbedaannya adalah saya cukup yakin Anda melakukannya setiap hari. Saya hanya melakukannya sekali atau dua kali!"

    scene expression ("images/episode3/157.webp") with dissolve
    patricia "OK ... Biarkan lagi. Saya tahu persis apa yang ingin saya tanyakan."
    menu:
        "{i} rock {/i}":
            scene expression ("images/episode3/160.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
        "{i} kertas {/i}":
            scene expression ("images/episode3/162.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
        "{i} gunting {/i}":
            scene expression ("images/episode3/158.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
    scene expression ("images/episode3/164.webp") with dissolve
    toby "Bagaimana Anda bisa menang begitu banyak?"
    patricia "Anda sangat dapat diprediksi!"
    toby "Keberuntungan murni!"
    scene expression ("images/episode3/166.webp") with dissolve
    patricia "Berapa banyak gadis yang Anda miliki sebelum Emma?"
    scene expression ("images/episode3/169.webp") with dissolve
    toby "Akhirnya sesuatu yang lebih normal."
    toby "Emma adalah pacar kedua saya."
    scene expression ("images/episode3/168.webp") with dissolve
    patricia "Saya tahu dia adalah pacar kedua Anda, tapi yang saya tanyakan kepada Anda adalah berapa banyak gadis yang tidur dengan Anda sebelum Emma."
    scene expression ("images/episode3/167.webp") with dissolve
    toby "Tiga!"
    scene expression ("images/episode3/166.webp") with dissolve
    patricia "Anda sudah berhubungan seks dengan hanya tiga gadis? Saya mengharapkan angka yang lebih besar."
    scene expression ("images/episode3/174.webp") with dissolve
    toby "Apakah itu yang Anda pikirkan tentang [brother] Anda? Saya bukan tipe pria yang tidur dengan semua orang yang dilihatnya."
    scene expression ("images/episode3/166.webp") with dissolve
    patricia "Namun Anda masih berselingkuh di Emma?"
    scene expression ("images/episode3/178.webp") with dissolve
    if ep2_laurenBlowjob:
        toby "Hei, kami tidak bercinta. Saya baru saja terjebak pada saat itu, dan dia memberi saya blowjob. Itu semua."
    else:
        toby "Tunggu sebentar, aku tidak meniduri siapa pun. Dia hanya menciumku dan aku bahkan merasa seperti omong kosong."
    toby "Tapi jangan khawatir. Itu hal terakhir yang akan saya katakan mulai sekarang."
    scene expression ("images/episode3/168.webp") with dissolve
    patricia "Bagus. Saya tidak akan membawanya lagi."

    scene expression ("images/episode3/157.webp") with dissolve
    patricia "Satu putaran lagi?"
    menu:
        "{i} rock {/i}":
            scene expression ("images/episode3/161.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
        "{i} kertas {/i}":
            scene expression ("images/episode3/163.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
        "{i} gunting {/i}":
            scene expression ("images/episode3/159.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
    scene expression ("images/episode3/165.webp") with dissolve
    toby "Sempurna. Sangat sedikit [sister], mengapa Anda tidak memberi tahu saya apa yang Anda pikirkan ketika Anda jari diri?"
    scene expression ("images/episode3/173.webp") with dissolve
    patricia "Itu terlalu pribadi. Mungkin saya tidak memikirkan siapa pun!"
    scene expression ("images/episode3/171.webp") with dissolve
    toby "Pertanyaan saya adalah apa yang Anda pikirkan, bukan siapa yang Anda pikirkan, tetapi saya suka ke mana arahnya."
    toby "Jadi? Siapa pria yang beruntung?"
    play sound "audio/fx/Cell Phone Ring Sound Effect - Free Sound Effects.mp3"
    scene expression ("images/episode3/179.webp") with dissolve
    $ progress = 40
    patricia "Disimpan oleh bel. Anda harus mendapatkannya!"
    toby "Saya akan meneleponnya kembali setelah Anda menjawab."
    scene expression ("images/episode3/180.webp") with dissolve
    play sound "audio/fx/Cell Phone Ring Sound Effect - Free Sound Effects.mp3"
    patricia "Bagaimana jika itu sangat penting?"
    toby "Sekali lagi, saya akan meneleponnya kembali segera setelah Anda menjawab."
    scene expression ("images/episode3/181.webp") with dissolve
    patricia "Late!"
    toby "Beri aku itu!"
    scene expression ("images/episode3/182.webp") with dissolve

    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Hey sweetie. Are you sleeping?{/i}"
    toby "Hai [mom], tidak, saya tidak. Saya dan Tris sedang bermain game."
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I'm sorry to ruin your fun, but can you please come pick me up?{/i}"
    toby "Tentu, [mom]. Apakah semuanya baik -baik saja?"
    charlotte "Jangan khawatir. Semuanya baik -baik saja, hanya saja [father] Anda adalah bajingan."
    scene expression ("images/episode3/183.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Her voice is cracking like she's been crying.{/i}"
    toby "Ya [mom], cukup SMS saya alamatnya dan saya akan berada di sana!"
    charlotte "Terima kasih sayang. Aku mencintaimu!"
    toby "Aku juga mencintaimu [mom]."
    charlotte "Jika Tris meminta Anda, katakan saja padanya bahwa Erwin memiliki beberapa bisnis yang belum selesai!"
    toby "Tentu ... aku akan segera ke sana."
    scene expression ("images/episode3/184.webp") with dissolve
    patricia "Apakah sesuatu terjadi?"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What should I do? Should I lie to her, or tell her the truth. I mean sooner or later she's bound to find out.{/i}"
    menu:
        "{i} berbohong padanya {/i}":
            $ ep3_liePatricia = True
            scene expression ("images/episode3/185.webp") with dissolve
            toby "Tidak, tidak ada apa -apa. [dad!c] memiliki beberapa bisnis yang belum selesai dan dia meminta saya untuk menjemputnya."
            patricia "Saya bukan anak kecil lagi. Anda bisa mengatakan yang sebenarnya!"
            toby "Yang benar adalah bahwa Anda masih menghindari menjawab pertanyaan saya."
            scene expression ("images/episode3/186.webp") with dissolve
            patricia "Anda harus mengambil [mom], saya akan menyelesaikan film."
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She knows I'm lying, but what can I do? [mom!c] asked me not to tell her the truth!{/i}"
        "{i} [JGR] Katakan yang sebenarnya {/i}"(csq="Tris +1"):

            $ patricia_rel += 1
            scene expression ("images/episode3/187.webp") with dissolve
            toby "Aku juga tidak yakin. Dia hanya mengatakan kepada saya bahwa [dad] adalah seorang bajingan."
            patricia "Apa yang dia lakukan kali ini?"
            toby "Saya belum tahu."
            patricia "Aku ingin ikut denganmu!"
            toby "Maaf [sis], tetapi sepeda saya hanya memiliki dua kursi dan selain itu, [mom] mengatakan kepada saya untuk tidak memberi tahu Anda, tetapi Anda layak mengetahui yang sebenarnya."
            scene expression ("images/episode3/188.webp") with dissolve
            patricia "Terima kasih telah mempercayai saya. Pastikan [mom] baik -baik saja!"

    return


label episode3_charlote_night:
    $ progress = 41
    scene expression ("images/episode3/189.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This must be the place. I'll text [mom] and let her know that I'm here.{/i}"
    scene expression ("images/episode3/190.webp") with dissolve
    charlotte "Anda tiba di sini dengan cepat!"
    scene expression ("images/episode3/191.webp") with dissolve
    toby "Saya baru saja akan mengirimi Anda SMS. Apakah semuanya baik -baik saja?"
    scene expression ("images/episode3/192.webp") with dissolve
    charlotte "Itu akan terjadi, begitu kita pulang."
    charlotte "Dimana mobilnya? Mengapa Anda datang dengan sepeda?"
    scene expression ("images/episode3/193.webp") with dissolve
    toby "Mobil? Saya pikir kalian mengambilnya."
    scene expression ("images/episode3/192.webp") with dissolve
    charlotte "Tidak, sayang! Bagaimana saya bisa mengendarai sepeda dengan gaun ini?"
    scene expression ("images/episode3/193.webp") with dissolve
    toby "Maaf [mom], saya tidak memikirkan hal ini. Saya datang sesegera mungkin."
    scene expression ("images/episode3/194.webp") with dissolve
    charlotte "Jangan khawatir sayang. Saya punya ide!"
    charlotte "Kembali!"

    show screen ui_message("A few minutes later") with long_dissolve

    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/195.webp") with dissolve
    hide screen ui_message
    charlotte "Jadi? Bagaimana menurutmu. Bisakah saya mengendarai sepeda sekarang?"

    scene expression ("images/episode3/196.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Uhum... Wow!{/i}"
    scene expression ("images/episode3/197_0.webp") with dissolve
    toby "Apa yang terjadi dengan gaunmu?"
    scene expression ("images/episode3/197.webp") with dissolve
    charlotte "Mari kita katakan bahwa saya sangat baik dengan gunting."
    toby "Anda memotong gaun Anda?"
    charlotte "Ini tidak seperti saya pergi ke acara lain dengan [dad] Anda dalam waktu dekat."
    scene expression ("images/episode3/198.webp") with dissolve
    charlotte "Jadi? Apa yang kamu tunggu? Apakah kita pergi atau tidak?"
    toby "Tentu, [mom]."

    scene expression ("images/episode3/199.webp") with dissolve
    toby "Apakah Anda yakin tidak ingin berbicara tentang apa yang terjadi?"
    charlotte "Tolong bawa aku pulang!"

    scene expression ("images/episode3/200.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode3/201.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode3/202.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode3/203.webp") with dissolve
    charlotte "Tunggu! Tarik di sini!"
    toby "Maaf?"
    charlotte "Kataku, menepi ke bar ini."
    scene expression ("images/episode3/204.webp") with dissolve
    toby "Aku tidak membiarkanmu mabuk lagi. Kita perlu berbicara tentang apa yang terjadi."
    scene expression ("images/episode3/205.webp") with dissolve
    charlotte "Sesuai dengan diri Anda. Aku masuk!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit! She's acting like a child! A spoiled one, too.{/i}"
    scene expression ("images/episode3/206.webp") with long_dissolve
    charlotte "Senang Anda bisa bergabung dengan saya."
    toby "Saya di sini karena saya tidak membiarkan Anda mabuk!"
    scene expression ("images/episode3/207.webp") with dissolve
    charlotte "Tolong dua bir!"
    barmaid "Tentu ma \ 'am. Satu detik."
    scene expression ("images/episode3/208.webp") with dissolve
    toby "Tolong bawakan kami dua cola!"
    barmaid "Tentu Pak. Ada lagi?"
    toby "Tidak, itu saja. Terima kasih!"
    scene expression ("images/episode3/209.webp") with dissolve

    toby "Jadi? Apakah Anda akan memberi tahu saya apa yang terjadi? Apa yang masuk ke dalam dirimu?"
    charlotte "Anda tidak akan meninggalkannya sendirian sampai saya memberi tahu Anda, saya mengambilnya?"
    toby "Cukup banyak. Anda menceritakan semuanya atau saya akan meninggalkan Anda di sini."
    toby "Saya [son] Anda, saya peduli untuk Anda, tetapi jika Anda akan menutup saya, saya akan pergi dan Anda bisa mabuk seperti yang Anda inginkan dan saya tidak peduli!"
    scene expression ("images/episode3/210.webp") with dissolve
    charlotte "Anda pembohong yang mengerikan. Ketika Anda akan berbohong, pastikan Anda percaya apa yang Anda katakan."
    scene expression ("images/episode3/211.webp") with dissolve
    toby "Itu saja! Saya tidak membantu Anda jika Anda tidak akan memberi tahu saya apa yang terjadi."
    scene expression ("images/episode3/212.webp") with dissolve
    charlotte "[toby!c] Tolong. Duduklah aku akan memberitahumu segalanya."
    scene expression ("images/episode3/213.webp") with dissolve
    charlotte "Jadi, tak lama setelah kami sampai di sana, Erwin dan dua rekannya meninggalkan ruangan bersama."
    scene expression ("images/episode3/214.webp") with dissolve
    barmaid "Ini minuman Anda."
    toby "Maaf Nona. Kami hanya memesan ..."
    charlotte "Itu sempurna. Terima kasih!"
    scene expression ("images/episode3/215.webp") with dissolve
    toby "Sudah kubilang aku tidak membiarkanmu mabuk lagi."
    charlotte "Jangan khawatir sayang."
    scene expression ("images/episode3/216.webp") with dissolve
    charlotte "Saya tidak mabuk hanya pada dua bir!"
    toby "Apa maksudmu dua bir?"
    scene expression ("images/episode3/217.webp") with dissolve
    charlotte "Saya tidak bisa membiarkan Anda minum bir dan kemudian mengantarkan kami pulang. Jadi saya akan membuat pengorbanan."
    toby "Apa pun. Jadi? Apa yang terjadi setelah itu?"
    scene expression ("images/episode3/218.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/219_normal.webp") with dissolve
    charlotte "Jadi orang -orang itu pergi dan saya ditinggalkan di sana bersama dua wanita lainnya. Maksud saya dua pelacur, karena saya adalah satu -satunya wanita di sana."
    scene expression ("images/episode3/219_arogant.webp") with dissolve
    charlotte "Maksudku, salah satu dari mereka tampak seperti pelacur berbayar dan yang lain seperti dia adalah nyonya. Maksud saya, dia berusia 20 tahun, sementara pria itu sekitar 45."
    scene expression ("images/episode3/220_curious.webp") with dissolve
    toby "Dan itulah yang mengganggu Anda? Bahwa dia meninggalkanmu dengan dua wanita?"
    scene expression ("images/episode3/220_normal.webp") with dissolve
    toby "Saya yakin mereka memiliki beberapa hal penting untuk dibahas."
    scene expression ("images/episode3/219_serious.webp") with dissolve
    charlotte "Persis seperti apa yang saya pikirkan pada awalnya, karena itulah yang saya lakukan. Saya adalah istri yang mempercayai segalanya."
    charlotte "Wanita yang berbohong pada dirinya sendiri, supaya dia bisa berpura -pura bahwa semuanya baik -baik saja."
    scene expression ("images/episode3/220_angry.webp") with dissolve
    toby "Tolong jangan beri tahu saya bahwa dia selingkuh!"
    scene expression ("images/episode3/219_laugh.webp") with dissolve
    charlotte "Saya akan membunuhnya sendiri, tetapi tidak, dia bukan tipe pria yang menipu. Dia jauh dari sempurna, tapi setidaknya dia bukan penipu!"
    scene expression ("images/episode3/219_normal.webp") with dissolve
    charlotte "Ngomong -ngomong, setelah sekitar satu jam, mereka semua kembali mabuk!"
    charlotte "Dan aku belum melihatnya mabuk seperti ini selamanya, tapi malam ini dia berbeda."
    charlotte "Saya pikir dia mencoba mengesankan orang -orang yang telah dia minum."
    scene expression ("images/episode3/220_normal.webp") with dissolve
    toby "Saya mengerti."
    scene expression ("images/episode3/219_serious.webp") with dissolve
    charlotte "Dan ini adalah bagian yang membuatku kesal ..."
    charlotte "Jadi, salah satu dari mereka mulai mengolok -olok istrinya. Betapa dia suka bercinta. Betapa baiknya dia di tempat tidur."
    charlotte "Berapa banyak penis yang bisa dia ambil. Dia memalukan dia."
    scene expression ("images/episode3/219_surprised.webp") with dissolve
    charlotte "Dan pelacur itu tertawa seperti itu adalah pujian terbaik yang pernah ada."
    scene expression ("images/episode3/219_arogant.webp") with dissolve
    charlotte "Lalu datanglah giliran orang lain untuk mengolok -olok bimbo pantatnya."
    charlotte "Dia membual betapa dia suka mengisap ayam. Kadang -kadang dia membangunkannya dengan memberinya blowjob."
    charlotte "Seberapa besar pantatnya dan bagaimana dia suka anal. Dia menikmati anal lebih dari seks normal, karena dia menyebalkan!"
    scene expression ("images/episode3/220_awkward.webp") with dissolve
    toby "Tolong, tolong beri tahu saya [dad] tidak bergabung dengan percakapan."
    scene expression ("images/episode3/219_angry.webp") with dissolve
    charlotte "Aku tidak akan berbohong padamu, karena aku tidak berbohong. Tapi sepotong kotoran itu sebenarnya, pembohong."
    charlotte "Anda ingin tahu apa yang dia katakan berusaha bersaing dengan mereka?"
    scene expression ("images/episode3/220_sad.webp") with dissolve
    toby "Tidak juga, tapi teruskan."
    scene expression ("images/episode3/219_angry.webp") with dissolve
    charlotte "He said something like \"You know how these bitches are. As long as you give them money they'll do anything for you.\""
    charlotte "Dan kemudian mereka semua tertawa."
    scene expression ("images/episode3/219_crying.webp") with dissolve
    charlotte "Dia mengatakan itu tentang saya. Wanita yang telah berdiri di sampingnya tidak peduli apa. Saya berada di sisinya ketika dia kaya. Saya berada di sisinya ketika dia miskin."
    charlotte "Saya mendukungnya. I \ m [mother] dari [kids]. Mengapa Anda pergi dan mempermalukan satu -satunya orang yang telah mendukung Anda melalui segalanya?!"
    charlotte "Apa yang saya lakukan untuk mendapatkannya?"
    scene expression ("images/episode3/221.webp") with dissolve
    toby "Tolong berhenti menangis. Anda menghancurkan hati saya. Sangat menyakitkan melihat Anda seperti ini."
    toby "Mengapa Anda tidak meninggalkannya? Dia jelas tidak sepadan."
    scene expression ("images/episode3/222.webp") with dissolve
    charlotte "Aku tidak bisa meninggalkannya. Dia tidak selalu seperti itu, kita memiliki banyak kenangan indah bersama."
    toby "Ya, tapi ... selama beberapa bulan terakhir Anda baru saja terluka."
    charlotte "Saya tahu sayang, tetapi ketika Anda menikahi seseorang, Anda berjanji untuk berada di sana menjadi lebih baik atau lebih buruk. Saya melakukan yang terbaik untuk menepati janji itu."
    toby "Aku mencintaimu [mom]!"
    scene expression ("images/episode3/223.webp") with dissolve
    charlotte "Jadi Anda tidak akan meninggalkan saya di sini jika saya minum botol ini juga?"
    scene expression ("images/episode3/224.webp") with dissolve
    toby "Tidak, silakan."
    scene expression ("images/episode3/225.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm going to talk to [dad] about this because [mom] doesn't deserve this.{/i}"
    label memory_08:
        scene expression ("images/episode3/226.webp") with dissolve

        toby "Apa yang sedang kamu lakukan?"
        charlotte "Saya perlu menjernihkan kepala saya!"

        scene expression ("images/episode3/227.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        $ progress = 42
        toby "Saya tidak mengikuti. Mengapa Anda melepas sepatu Anda?"
        scene expression ("images/episode3/228.webp") with dissolve
        charlotte "Kami akan bermain biliar."
        toby "Sekarang Anda hanya memanfaatkan fakta bahwa saya tidak akan mencoba mengalahkan Anda karena Anda mengalami malam yang sulit."
        scene expression ("images/episode3/229.webp") with long_dissolve
        charlotte "Anda tidak bisa mengalahkan saya bahkan jika Anda mencoba!"
        toby "Oke, Anda memintanya!"
        scene expression ("images/episode3/230.webp") with dissolve
        charlotte "Anda bisa istirahat."
        toby "Tidak mungkin, nona pertama!"
        scene expression ("images/episode3/231.webp") with dissolve
        charlotte "Silakan?"
        charlotte "Saya membutuhkan penyegaran cepat pada permainan. Saya belum bermain dalam 20 tahun."
        toby "Baik ... izinkan saya menunjukkan kepada Anda bagaimana ini selesai!"
        scene expression ("images/episode3/232.webp") with dissolve
        toby "Apakah Anda siap untuk kalah?"
        charlotte "Saya akan mencoba tidak menangis!"
        play sound "audio/fx/Billiards Break Sound FX.mp3"
        scene expression ("images/episode3/233.webp") with dissolve
        charlotte "Wow, kamu sangat bagus. Bukan satu bola pun."
        toby "Sangat lucu. Mari kita lihat apa yang Anda dapatkan!"
        scene expression ("images/episode3/234.webp") with dissolve
        charlotte "Saya pikir kita perlu sedikit taruhan."
        charlotte "Jika saya menang, Anda harus membawa saya ke restoran yang bagus akhir pekan ini."
        toby "Sempurna. Dan jika saya menang, Anda tidak memasukkan alkohol di mulut Anda selama dua minggu."
        scene expression ("images/episode3/235.webp") with dissolve
        charlotte "Mari kita buat 4 untuk membuatnya berharga."
        toby "Sempurna."
        toby "Jika saya jadi Anda, saya akan pergi ke bar sekarang dan memesan beberapa minuman lagi sebelum Anda kehilangan taruhan."
        scene expression ("images/episode3/236.webp") with dissolve
        charlotte "Jika aku jadi kamu, aku akan duduk."
        scene expression ("images/episode3/237.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Uhum... [mom!c]'s ass is amazing in that dress.{/i}"
        play sound "audio/fx/Billiards Break Sound FX.mp3"
        scene expression ("images/episode3/238.webp") with dissolve
        charlotte "Saya mendapat garis -garis. Saya seorang harimau."
        toby "Umm ... ya. Seseorang minum terlalu banyak."
        scene expression ("images/episode3/238_1.webp") with dissolve
        charlotte "Saya adalah kucing. Rawr"
        toby "Apa yang bisa saya katakan, nikmati saat itu berlangsung, karena itu satu -satunya tembakan yang Anda buat."
        scene expression ("images/episode3/239.webp") with dissolve
        charlotte "Ya, Anda mungkin benar. Mungkin itu hanya keberuntungan!"
        scene expression ("images/episode3/240.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I need to stop staring at my [mom]. It's wrong!{/i}"
        scene expression ("images/episode3/241.webp") with dissolve
        play sound "audio/fx/Billiards Break Sound FX.mp3"
        charlotte "Ups. Dua lagi."
        scene expression ("images/episode3/242.webp") with dissolve
        charlotte "Ada keberuntungan lagi!"
        scene expression ("images/episode3/243.webp") with dissolve
        toby "Itu saja, saya datang ke sana, karena Anda harus curang."
        scene expression ("images/episode3/244.webp") with dissolve
        charlotte "Ya, pastikan Anda memperhatikan, karena saya hanya akan menunjukkan ini sekali ini!"
        scene expression ("images/episode3/245.webp") with dissolve
        play sound "audio/fx/Billiards Break Sound FX.mp3"
        charlotte "Wow, saya melakukannya lagi. Saya pasti sangat beruntung hari ini!"
        scene expression ("images/episode3/246.webp") with dissolve
        charlotte "Katakan padaku sayang. Mana yang kamu ingin aku dapatkan?"
        toby "Yang hitam?"
        scene expression ("images/episode3/246_1.webp") with dissolve
        charlotte "Lucu, tapi belum."
        scene expression ("images/episode3/247.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode3/248.webp") with dissolve
        play sound "audio/fx/Billiards Break Sound FX.mp3"
        charlotte "Dua lagi!"
        toby "Siapa Anda dan di mana [mom] saya?"
        scene expression ("images/episode3/249.webp") with dissolve
        charlotte "Aku tidak yakin di mana dia sekarang, tapi aku sangat tahu di mana dia akan berada di hari Sabtu!"
        toby "Dan dimana itu?"
        scene expression ("images/episode3/250.webp") with dissolve
        charlotte "Di restoran kecil yang enak minum anggur dan makan steak yang enak."
        scene expression ("images/episode3/251.webp") with dissolve
        charlotte "Ini adalah yang terakhir dan kemudian keinginan Anda menjadi kenyataan!"
        toby "Jangan khawatir tentang saya. Anda tidak harus melakukan ini untuk saya!"
        scene expression ("images/episode3/252.webp") with dissolve
        play sound "audio/fx/Billiards Break Sound FX.mp3"
        charlotte "Terlambat sekarang. Anda meminta saya untuk menenggelamkan bola hitam. Keinginan Anda adalah perintah saya!"

        scene expression ("images/episode3/253.webp") with dissolve
        charlotte "Dan sekarang untuk menang!"
        play sound "audio/fx/Billiards Break Sound FX.mp3"
        scene expression ("images/episode3/254.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode3/255.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode3/256.webp") with dissolve

        charlotte "Maaf sayang. Bisakah Anda mengingatkan saya? Apa yang baru saja terjadi?"
        toby "Saya pikir Anda baru saja mencium pipi saya."
        scene expression ("images/episode3/257.webp") with dissolve
        charlotte "Maksudku, sebelum itu."
        charlotte "Saya cukup yakin saya menang!"
        toby "Tetap membual!"
        scene expression ("images/episode3/258.webp") with dissolve
        charlotte "Jangan menjadi pecundang yang miskin!"
        scene expression ("images/episode3/259.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Umm... Eyes up. She's my [mom].{/i}"
        scene expression ("images/episode3/259_1.webp") with dissolve
        charlotte "Jika Anda seorang anak yang baik, saya akan mengajari Anda semua yang saya tahu!"
        $ progress = 43
        $ unlockImage(persistent.charlotte_08)
        menu:
            "{i} [JGR] Flirt {/i}":
                toby "Semua yang Anda tahu?"
                scene expression ("images/episode3/260.webp") with dissolve
                charlotte "Hanya tentang kolam renang untuk saat ini."
                toby "Tentu saja, itulah yang saya maksud!"
            "{i} don \ 't flirt {/i}" if not _in_replay:
                scene expression ("images/episode3/260.webp") with dissolve
                pass

        charlotte "Terima kasih untuk malam ini. Ini bagus."

        $ unlockMemory(persistent.memory_08)
        $ renpy.end_replay()

    charlotte "Oke, waktunya pulang!"
    toby "Tentu [mom]."
    scene expression ("images/episode3/261.webp") with fade
    toby "Dan di sinilah kita!"
    charlotte "Terima kasih sayang untuk semuanya!"
    toby "Dengan senang hati!"
    if charlotte_rel >=5:
        label memory_09:


            scene expression ("images/episode3/262.webp") with dissolve
            charlotte "Bisakah Anda membantu saya berubah? Saya merasa sedikit pusing."
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm not sure this is a good idea, but how can I say no to [mom].{/i}"
            toby "Tentu saja!"
            scene expression ("images/episode3/263.webp") with dissolve
            toby "Apa yang perlu saya lakukan?"
            charlotte "Lepaskan gaun saya dan pastikan Anda tidak mengintip."
            scene expression ("images/episode3/264.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode3/265.webp") with dissolve
            charlotte "Bisakah Anda memberikan saya atasan itu?"
            scene expression ("images/episode3/266.webp") with dissolve
            toby "Di Sini!"
            scene expression ("images/episode3/267.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... That's her nipple.{/i}"
            scene expression ("images/episode3/268.webp") with dissolve
            charlotte "Anda adalah anak yang manis. Anda tahu itu, kan?"
            toby "Uhum ... ya."
            charlotte "Emma adalah gadis yang sangat beruntung untuk memilikimu!"
            toby "Terima kasih [mom]."
            scene expression ("images/episode3/269.webp") with dissolve
            toby "Selamat malam, [mom]."
            charlotte "Selamat malam, sayang."

            $ unlockMemory(persistent.memory_09)
            $ renpy.end_replay()
    else:
        charlotte "Selamat malam, sayang!"

    scene expression ("images/episode3/270.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I feel so bad for [mom]. How can [dad] be such a dick to her?{/i}"
    scene expression ("images/episode3/271.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I really need to talk to him about this! I will not allow him to treat [mom] like this.{/i}"
    stop music fadeout 1.0
    return


label episode3_emma_morning:
    show screen ui_message("Thursday") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message

    $ progress = 44
    scene expression ("images/episode3/272.webp") with long_dissolve
    play sound "audio/fx/notification_5.mp3"
    with shake
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/273.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/272.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    with shake
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/274.webp") with dissolve

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Who's waking me up this early?{/i}"
    scene expression ("images/episode3/275.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}A message from Emma. We haven't talked much since I got here.{/i}"

    scene expression ("images/episode3/276_texting.webp") with dissolve
    call sms_incoming ("emma", "Morning sunshine!\n How are you? \nWe haven't talked in a few days and was wondering if everything is okay.") from _call_sms_incoming
    call sms_sent ("emma", "Hi there sweetheart. \nYeah, I'm fine. I've just had a rough few days. \nSorry for not texting. \nHow are you?") from _call_sms_sent
    call sms_incoming ("emma", "I miss you very much.\nI caught a cold yesterday and now I'm stuck at home.\nWish you were here.") from _call_sms_incoming_1
    call sms_sent ("emma", "How did that happen?") from _call_sms_sent_1
    hide screen message

    scene expression ("images/episode3/276.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Oh... She's video calling me. I sure hope I look good in the morning!{/i}"
    scene expression ("images/episode3/281_greet.webp") with dissolve
    toby "Sayang pagi! Senang Anda menelepon."
    scene expression ("images/episode3/282_laugh.webp") with dissolve
    emma "Siapa pria tampan itu?"
    scene expression ("images/episode3/281_happy.webp") with dissolve
    toby "Saya pikir hawa dingin mengacaukan otak Anda. Aku tidak terlalu tampan."
    scene expression ("images/episode3/282_kiss.webp") with dissolve
    emma "Anda tidak berpikir begitu?"
    scene expression ("images/episode3/281_happy.webp") with dissolve
    toby "Tentu saja tidak. Jadi bagaimana Anda masuk angin dalam panas ini?"
    scene expression ("images/episode3/282_laugh.webp") with dissolve
    emma "You know what they say: \"Smart people get colds in the summer\"."
    scene expression ("images/episode3/281_laugh.webp") with dissolve
    toby "Secara harfiah tidak ada yang mengatakan itu."
    scene expression ("images/episode3/282_shy.webp") with dissolve
    emma "Saya bersedia! Apakah Anda mengatakan saya tidak pintar?"
    scene expression ("images/episode3/281_smile.webp") with dissolve
    toby "Apakah Anda benar -benar berpikir saya berkencan dengan seorang gadis bodoh?"
    scene expression ("images/episode3/282_happy.webp") with dissolve
    emma "Itulah yang saya pikirkan!"
    scene expression ("images/episode3/282_curious.webp") with dissolve
    emma "Bagaimana kabarmu cintaku? Bagaimana kota baru memperlakukan Anda?"
    scene expression ("images/episode3/281_normal.webp") with dissolve
    toby "Ini agak membosankan. Saya belum punya teman di sini. Sejauh ini saya dan [family] saya sejauh ini!"
    scene expression ("images/episode3/282_flirty.webp") with dissolve
    emma "Bagaimana Anda bisa bosan? Pria tampan seperti Anda tidak boleh bosan. Saya yakin ada banyak gadis yang berbaris di luar pintu Anda menunggu untuk bertemu dengan Anda!"
    scene expression ("images/episode3/282_laugh.webp") with dissolve
    emma "Sayang sekali bagi mereka, Anda setia kepada pacar Anda!"
    scene expression ("images/episode3/281_sad.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yeah... I'm nothing but faithful.{/i}"
    scene expression ("images/episode3/282_curious.webp") with dissolve
    emma "Ada masalah? Anda tiba -tiba terlihat terganggu!"
    scene expression ("images/episode3/281_sad.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I can't tell her what happened. She'll hate me but I can't hide everything from her either.{/i}"
    scene expression ("images/episode3/281_normal.webp") with dissolve
    toby "Tidak, itu bukan apa -apa. Hanya saja kita perlu membicarakan sesuatu."
    scene expression ("images/episode3/282_scared.webp") with dissolve
    emma "Anda membuat saya takut, sayang. Tolong beritahu saya tidak ada gadis lain atau semacamnya, karena saya akan mati jika Anda melakukannya!"
    scene expression ("images/episode3/281_normal.webp") with dissolve
    toby "Tidak, tidak. Bukan itu. Hanya saja aku tidak jujur denganmu tentang sesuatu."
    toby "Ini tentang mengapa kami pindah."
    scene expression ("images/episode3/282_curious.webp") with dissolve
    emma "Apakah sesuatu yang buruk terjadi?"
    scene expression ("images/episode3/281_sad.webp") with dissolve
    toby "Sebenarnya ya. [dad] saya bangkrut."
    toby "Itulah mengapa kami harus pindah. Perusahaan itu bangkrut dan dia ditawari pekerjaan di sini dengan salah satu mitranya."
    scene expression ("images/episode3/282_curious.webp") with dissolve
    emma "Mengapa Anda hanya memberi tahu saya ini sekarang?"
    scene expression ("images/episode3/281_normal.webp") with dissolve
    toby "Saya tidak tahu bagaimana Anda akan bereaksi. Saya tidak ingin menempatkan Anda dalam situasi yang sulit."
    scene expression ("images/episode3/282_angry.webp") with dissolve
    emma "Apa yang sangat sulit tentang situasi ini? [dad] Anda dulu punya uang dan sekarang dia tidak! Bukan masalah besar, apa hubungannya dengan hubungan kita?"
    scene expression ("images/episode3/281_sad.webp") with dissolve
    toby "..."
    scene expression ("images/episode3/282_angry.webp") with dissolve
    emma "Oh, saya mengerti. Anda percaya teman bodoh Anda. Orang -orang yang memberi tahu Anda bahwa saya hanya dengan Anda karena uang dan hadiah mahal Anda."
    emma "Baiklah, biarkan saya menjadi sangat jelas. Saya tidak peduli tentang uang [dad] Anda. Pada kencan pertama kami, saya tidak tahu Anda punya uang!"
    scene expression ("images/episode3/282_angry2.webp") with dissolve
    emma "Apakah Anda ingat kencan pertama kami? Anda membelikan saya es krim. Itu dia, dan aku masih jatuh cinta padamu."
    emma "Saya tidak membutuhkan apapun dari Anda. Saya hanya perlu dicintai. Itu semua yang pernah saya tanyakan dari Anda!"
    scene expression ("images/episode3/282_angry.webp") with dissolve
    emma "Dan sekarang Anda mengatakan kepada saya bahwa Anda yakin saya adalah penggali emas, sama seperti yang dilakukan orang lain?"
    scene expression ("images/episode3/282_sad.webp") with dissolve
    emma "Mengapa kita bahkan bersama jika Anda tidak bisa jujur kepada saya dan tidak mempercayai saya dengan segala sesuatu yang terjadi dalam hidup Anda!"
    emma "Jika saya hanya di sini untuk mengisap ayam, maka saya minta maaf saya membuang -buang waktu saya dengan Anda. Aku mencintaimu [toby!c]. Aku mencintaimu dan hanya kamu."
    emma "Saya tidak peduli dengan uang. Saya tidak peduli dengan hadiah. Saya tidak peduli tentang apa pun, tetapi untuk bersama Anda!"
    scene expression ("images/episode3/282_sad2.webp") with dissolve
    emma "Apakah Anda benar -benar berpikir begitu sedikit tentang saya?"
    scene expression ("images/episode3/281_sad.webp") with dissolve
    toby "Lihat, aku minta maaf. Aku pun mencintaimu. Aku tidak ingin kehilanganmu, aku sangat takut."
    scene expression ("images/episode3/282_angry.webp") with dissolve
    emma "Apakah Anda takut kehilangan saya karena Anda bangkrut?"
    scene expression ("images/episode3/281_sad.webp") with dissolve
    toby "Saya tahu itu salah, saya hanya takut. Itu semua!"
    scene expression ("images/episode3/282_angry.webp") with dissolve
    emma "Lihat. Anda seorang pria yang cerdas. Anda adalah pria yang saya cintai dan tidak ada yang akan mengubahnya."
    emma "Aku hanya ingin bersamamu."
    emma "Tapi saya tidak bisa bersama seorang pria yang berpikir saya adalah penggali emas, hanya karena beberapa orang bodoh lainnya mengatakan kepadanya!"
    scene expression ("images/episode3/282_normal.webp") with dissolve
    emma "Aku ingin bersamamu, tapi kamu harus lebih jujur denganku mulai sekarang!"
    emma "Apakah ada hal lain yang terjadi dalam hidup Anda yang perlu saya ketahui?"
    scene expression ("images/episode3/281_sad.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yes. I just fucking cheated on you!{/i}"
    scene expression ("images/episode3/281_normal.webp") with dissolve
    toby "Uhum ... Saya mendapat pekerjaan kemarin!"
    scene expression ("images/episode3/282_happy.webp") with dissolve
    emma "Benar-benar? Anda sudah menemukan pekerjaan?"
    emma "Itu cinta yang luar biasa. Sudah kubilang, kamu pintar. Anda pernah ke sana selama 3 hari dan Anda sudah memiliki pekerjaan."
    scene expression ("images/episode3/281_laugh.webp") with dissolve
    toby "Ya, itu terjadi langsung dari mimpi."
    scene expression ("images/episode3/282_curious.webp") with dissolve
    emma "Jadi? Dimana kamu bekerja?"
    scene expression ("images/episode3/281_normal.webp") with dissolve
    if toby_job == 0:
        toby "Saya bekerja sebagai agen real estat."
        scene expression ("images/episode3/282_happy.webp") with dissolve
        emma "Itu sangat keren."
        emma "Dan bagaimana sejauh ini?"
        scene expression ("images/episode3/281_laugh.webp") with dissolve
        toby "Pada hari pertama saya, saya menjual apartemen!"
        scene expression ("images/episode3/282_flirty.webp") with dissolve
        emma "Anda sudah menjual satu? Itu bayiku! Saya senang melihat Anda bernegosiasi dan sebagainya."
        scene expression ("images/episode3/281_happy.webp") with dissolve
        toby "Mungkin kamu akan. Saya akan memberi tahu bos saya bahwa Anda adalah seorang pelanggan dan kemudian kami akan melihat apartemen! Dan kemudian kita akan bernegosiasi!"
        scene expression ("images/episode3/282_flirty.webp") with dissolve
        if ep2_laurenBlowjob:
            emma "Jika saya mengisap kemaluan Anda, maukah Anda memberi saya diskon?"
        else:
            emma "Jika saya memberi Anda ciuman, maukah Anda memberi saya diskon?"
        emma "Apa yang kamu katakan?"
        scene expression ("images/episode3/281_surprised.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}You have no idea.{/i}"
        scene expression ("images/episode3/281_awkward.webp") with dissolve
        toby "Tentu saja. Apapun untukmu!"
        scene expression ("images/episode3/282_laugh.webp") with dissolve
        emma "Pefect. Can't wait to \"negotiate\"denganmu!"
    else:

        toby "Saya bekerja di klub. Saya semacam pengawal, bartman, pelayan?"
        scene expression ("images/episode3/282_curious.webp") with dissolve
        emma "Bagaimana cara kerjanya?"
        scene expression ("images/episode3/281_laugh.webp") with dissolve
        toby "Nah, sebagai permulaan pada hari -hari kami mengadakan pesta besar, saya akan duduk di luar, mencoba meyakinkan orang untuk masuk!"
        toby "Lalu saya akan memastikan semua orang memiliki semua yang mereka butuhkan."
        toby "Juga jika ada orang yang gaduh, pekerjaan saya adalah mengganggu, atau memberi tahu pengawal."
        scene expression ("images/episode3/282_flirty.webp") with dissolve
        emma "Anda membuatnya terdengar sangat berbahaya!"
        scene expression ("images/episode3/281_happy.webp") with dissolve
        toby "Itu tidak berbahaya. Saya hanya perlu memastikan semuanya di klub berjalan dengan baik dan tidak ada masalah!"
        scene expression ("images/episode3/282_laugh.webp") with dissolve
        emma "Itu membuat Anda menjadi manajer, bukan seorang bartman, pengawal, pelayan."
        scene expression ("images/episode3/281_laugh.webp") with dissolve
        toby "Ya, saya kira Anda bisa mengatakan itu!"
        scene expression ("images/episode3/282_happy.webp") with dissolve
        emma "Saya tidak sabar untuk datang mengunjungi Anda di klub ini."
        scene expression ("images/episode3/282_flirty.webp") with dissolve
        if ep2_laurenBlowjob:
            emma "Ketika saya akan melihat bahwa Anda akan stres di tempat kerja, saya akan menarik Anda di kamar mandi dan memberi Anda blowjob terbaik untuk menghilangkan stres Anda!"
        else:
            emma "Ketika saya akan melihat bahwa Anda akan stres di tempat kerja, saya akan datang dan memberi Anda ciuman di balik meja!"
        emma "Apa pendapat Anda tentang proposal saya?"
        scene expression ("images/episode3/281_surprised.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}You have no idea what you just said.{/i}"
        scene expression ("images/episode3/281_awkward.webp") with dissolve
        toby "Apa yang bisa saya katakan! Tak sabar menunggu!"

    scene expression ("images/episode3/283.webp") with dissolve
    play sound "audio/fx/Cell Phone Ring Sound Effect - Free Sound Effects.mp3"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Who is this calling me?{/i}"
    toby "Sayang, saya punya panggilan lain. Saya perlu menerimanya, itu mungkin bos saya!"
    emma "Tentu saja, sayang!"
    play sound "audio/fx/Cell Phone Ring Sound Effect - Free Sound Effects.mp3"
    emma "Bicaralah denganmu nanti!"
    toby "Sampai jumpa!"

    return

label episode3_callGirls:
    $ progress = 45
    call fixGirlPaths from _call_fixGirlPaths_1

    scene expression ("images/episode3/284.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Hello?{/i}"
    woman "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Hi, is this [toby!c]?{/i}"
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Yes, who is asking?{/i}"

    scene expression ("images/episode3/285.webp") with dissolve
    if lisa_path:
        lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I'll give you a hint. I kissed you yesterday.{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Oh, hi Lisa. How are you?{/i}"
        lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Very happy actually. I was curious to see if the hint would point in my direction or it would confuse you.{/i}"
        scene expression ("images/episode3/286.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I'm not that kind of guy.{/i}"
        if toby_job == 0:
            lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I hope it's OK that I took your phone number from the contract?{/i}"
            toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}No problem. It's fine.{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}How are you?{/i}"
        lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}A little bit bored and was wondering if you could show us around the city maybe.{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I would love to, but I'm kinda new too. I just moved here this week.{/i}"
        if toby_job == 0:
            lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Really? But then why did your boss say that you're the employee of the month?{/i}"
            toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I think she was testing me, to see if I have what it takes to be an agent.{/i}"
            toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}That was my first day on the job.{/i}"
            lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Oh my God... And you did so well on your first day?{/i}"
            toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}What can I say, I'm a man of many talents.{/i}"
        scene expression ("images/episode3/284.webp") with dissolve
        lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}So I guess you don't know the city any better than us?{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Well, I have seen the beach!{/i}"
        lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Then you win, because we haven't seen it.{/i}"
        lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}What do you say, care to show us the beach?{/i}"
        scene expression ("images/episode3/287.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Spending time with this girl might affect my relationship with Emma. I don't want to cheat again.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think the proper thing to do is go and explain the situation to her. I'm going to tell her that I have a girlfriend and I can't be dating anyone else.{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Umm... Sure, let's meet there.{/i}"
        lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Sweet!{/i}"
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Just so you know, you've actually been talking to Lauren. Lisa was too shy to call you.{/i}"
        scene expression ("images/episode3/286.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Oh. Well then tell Lisa I say hi!{/i}"
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Why don't you tell her yourself?{/i}"
        lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Hi?{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Hi Lisa, how are you today?{/i}"
        lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I'm... I'm fine, thank you!{/i}"
        lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}How are you?{/i}"
        scene expression ("images/episode3/288.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Glad that you decided to call. So are we going to the beach later?{/i}"
        lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}If you can, I'd love that.{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Of course. Should I come pick you up or do you have a car?{/i}"
        lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Don't worry about it, we'll meet you there.{/i}"
        scene expression ("images/episode3/284.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}That's perfect, because I only have a bike!{/i}"
        lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}And what would have you done if I had said to come pick us up?{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I would take you to the beach one at a time.{/i}"
        lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}You're a funny guy [toby!c], can't wait to see you later.{/i}"
        scene expression ("images/episode3/288.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}See you in about 2 hours?{/i}"
        lisa "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Perfect. See you later [toby!c].{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}See you later.{/i}"
    else:

        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}The girl who still has the taste of your cum in her mouth.{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Hi Lauren, how are you?{/i}"
        scene expression ("images/episode3/286.webp") with dissolve
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Trying not to sound desperate. I don't want you to think that I'm the kind of girl who calls a guy, but me and Lisa were getting really bored.{/i}"
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}And since you're the only guy we know in this city, we were wondering if you'd like to show us around.{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I would love to, but there is one slight problem. I just moved here as well and I don't know much of the city either.{/i}"
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Well then, this sucks.{/i}"
        scene expression ("images/episode3/287.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Spending time with Lauren might affect my relationship with Emma. I don't want to cheat again.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think the proper thing to do is go and explain the situation to her. I'm going to tell her that I have a girlfriend and I can't be dating anyone else.{/i}"
        scene expression ("images/episode3/288.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}But since I haven't seen the city either we can check it out together.{/i}"
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}There are two things that I like in a man. A big cock and a big brain. I like how you think.{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Thank you for the compliment?{/i}"
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}It was my pleasure.{/i}"
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I heard this city has a nice beach, why don't we go there?{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I actually went there on Monday and it's really nice. I think that's a good idea.{/i}"
        scene expression ("images/episode3/286.webp") with dissolve
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I knew why I was calling you. You're the right man for the job.{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}What can I say. I'm full of surprises.{/i}"
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Perfect then, can you come pick us up, or should we meet there?{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I would love too, but at the moment I only have a bike. I would need to take you to the beach one at a time.{/i}"
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Fuck! I knew you were perfect. Don't say anything else about the bike or I'm going to get really horny!{/i}"
        scene expression ("images/episode3/287.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This girl is bat shit crazy.{/i}"
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}We'll take Lisa's car then, but I expect you to take me for a ride on the back on your bike!{/i}"
        scene expression ("images/episode3/288.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}We'll see how you behave. Depends if you're a good girl or not!{/i}"
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I'm not sure how should I behave. Should I be a good girl, or a bad girl?{/i}"
        scene expression ("images/episode3/286.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I let you decide which is better.{/i}"
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I think I already did.{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}So see you there in about two hours?{/i}"
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Sounds like a plan!{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Bye Lauren. Tell Lisa I said hi!{/i}"
        lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Bye sexy! See you later.{/i}"

    scene expression ("images/episode3/283.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}These girls are trouble for my relationship!{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I have a message from Emma.{/i}"

    scene expression ("images/episode3/290_texting.webp") with dissolve
    call sms_incoming ("emma", "I just took some pills and now I'm going to try and get some sleep.") from _call_sms_incoming_2
    call sms_incoming ("emma", "I love you very much and can't wait to come visit you so I can beat your ass for thinking I'm a gold digger.") from _call_sms_incoming_3
    call sms_incoming ("emma", "And maybe later we will make love so I can forgive you.", img_icon="images/episode3/291_icon.webp", img="images/episode3/291.webp") from _call_sms_incoming_4
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's a sweetheart.{/i}"
    window hide
    call sms_sent ("emma", "Sleep tight and get well.") from _call_sms_sent_2
    call sms_sent ("emma", "Love you too!") from _call_sms_sent_3
    hide screen message

    scene expression ("images/episode2/005.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}My whole life is turning upside down.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}On one hand I do love Emma and now that I've told her what really happened with my [dad]'s company, I feel like she genuinely cares about me.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But beside that, I know that long distance relationships rarely work. I mean look at how my first relationship turned out.{/i}"
    if lisa_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}On the other hand, Lisa is exactly my type of girl. She's sweet, cute, sexy, smart and on top of that she's here.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}On the other hand, Lauren is crazy, sexy, fun and on top of that she's here.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I need to think this through and figure it out before I meet the girls.{/i}"
    return


label episode3_beach:
    $ progress = 46

    show screen ui_message("Two hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/294.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmm... I wonder where the girls are. Maybe they haven't arrived yet.{/i}"

    if lisa_path:
        scene expression ("images/episode3/295.webp") with dissolve
        lisa "Tebak siapa?"
        menu:
            "[JGR] Gadis tercantik."(csq="Lisa +1 & Galeri Gambar"):
                $ lisa_rel += 1
                scene expression ("images/episode3/296.webp") with dissolve
                lisa "Saya butuh nama hanya untuk memastikan Anda berpikir saya benar -benar gadis tercantik!"
                menu:
                    "{i} [JGR] lisa {/i}"(csq="Gambar galeri"):
                        $ unlockImage(persistent.lisa_03)
                        scene expression ("images/episode3/297.webp") with dissolve
                        lisa "Itu benar! Anda dapat menebaknya!"
                    "{i} Lauren {/i} [JLA1]"(csq="Lauren +1 & Galeri Gambar & jalur samping Lauren terbuka"):
                        $ unlockImage(persistent.lauren_03)
                        $ lauren_sidePath = True
                        $ lauren_rel += 1
                        scene expression ("images/episode3/298.webp") with dissolve
                        lauren "Aduh, itu pasti sakit untukmu sayang."
                        lisa "Anda adalah orang yang kejam, [toby!c]."
                        toby "Oh, ayolah. Saya baru saja bermain -main!"
                        pass
            "Lisa?":
                scene expression ("images/episode3/297.webp") with dissolve
                lisa "Itu benar! Anda dapat menebaknya!"

        scene expression ("images/episode3/303.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode3/304.webp") with dissolve
        lisa "Apa kabarmu? Apakah Anda menunggu lama?"
        scene expression ("images/episode3/305.webp") with dissolve
        toby "Tidak, saya baru saja sampai di sini. Anda tidak perlu khawatir"
    else:

        scene expression ("images/episode3/299.webp") with dissolve
        lauren "Tebak siapa?"
        menu:
            "[JGR] Gadis terpanas di dunia."(csq="Lauren +1"):
                $ lauren_rel += 1
                scene expression ("images/episode3/300.webp") with dissolve
                lauren "Saya butuh nama hanya untuk memastikan Anda berpikir saya adalah gadis terpanas!"
                menu:
                    "{i} [JGR] Lauren {/i}"(csq="Gambar galeri"):
                        $ unlockImage(persistent.lauren_03)
                        scene expression ("images/episode3/301.webp") with dissolve
                        lauren "Itu benar! Aku semua milikmu untuk diambil!"
                    "{i} lisa {/i} [JLI1]"(csq="Lisa +1 & Galeri Gambar & jalur samping Lisa terbuka"):
                        $ unlockImage(persistent.lisa_03)
                        $ lisa_sidePath = True
                        $ lisa_rel += 1
                        scene expression ("images/episode3/302.webp") with dissolve
                        lauren "Yang menyakiti Anda jackass."
                        lisa "Anda adalah orang yang kejam, [toby!c]."
                        toby "Oh, ayolah. Saya baru saja bermain -main!"
                        pass
            "Lauren?":
                scene expression ("images/episode3/301.webp") with dissolve
                lauren "Itu benar! Anda dapat menebaknya!"




        scene expression ("images/episode3/303.webp") with dissolve:
            yalign 1.0
            xalign 0.0
            linear 10.0 yalign 0.0 xalign 0.8

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode3/305.webp") with dissolve
        lisa "Apakah Anda menunggu lama?"
        scene expression ("images/episode3/304.webp") with dissolve
        toby "Tidak, saya baru saja sampai di sini. Anda tidak perlu khawatir"

    scene expression ("images/episode3/306.webp") with dissolve
    lisa "Bagus. Lagipula aku akan menyalahkan Lauren."
    scene expression ("images/episode3/307.webp") with dissolve
    if lisa_path:
        lauren "Menyalahkan saya? Butuh waktu hampir 45 menit untuk melakukan make up. Dan saya tidak tahu mengapa karena kami pergi ke pantai."
        scene expression ("images/episode3/308.webp") with dissolve
        lauren "Atau mungkin aku tahu apa yang membuatku begitu lama!"
        scene expression ("images/episode3/309.webp") with dissolve
        lisa "Jangan percaya padanya. Itu tidak membutuhkan waktu 45 menit. Hanya butuh 30 menit."
        scene expression ("images/episode3/310.webp") with dissolve
        toby "Itu jauh lebih baik. Anda melihat Lauren, 30 menit jauh dari 45."
        scene expression ("images/episode3/309.webp") with dissolve
        lisa "Anda menggodaku!"
        scene expression ("images/episode3/310.webp") with dissolve
        toby "Mari kita dapatkan kursi lounger."
    else:
        lauren "Itu salahku, kami terlambat. Saya harus merias wajah, menata rambut saya."
        scene expression ("images/episode3/308.webp") with dissolve
        lauren "Maksudku, aku punya alasan!"
        scene expression ("images/episode3/309.webp") with dissolve
        lisa "Haruskah saya meninggalkan kalian berdua sendirian?"
        scene expression ("images/episode3/310.webp") with dissolve
        toby "Jangan khawatir. Mari kita dapatkan kursi lounger."

    scene expression ("images/episode3/311.webp") with dissolve
    toby "Jadi mengapa kalian berdua pindah ke sini?"
    lisa "Kami pergi ke perguruan tinggi setempat dalam dua bulan, jadi kami ingin datang lebih awal dan merasa nyaman dengan kota dan orang -orang."
    lauren "Bagaimana denganmu?"
    scene expression ("images/episode3/312.webp") with dissolve
    toby "Baik dalam kasus saya itu sedikit lebih menyedihkan. Bisnis [family] bangkrut dan kami memiliki beberapa mitra di sini, jadi kami harus pindah ke sini."
    lauren "Itu menyebalkan! Dan apa yang kamu lakukan sekarang? Apakah Anda akan kuliah atau semacamnya?"
    lauren "Maksud saya, saya kira Anda 21, 22?"
    scene expression ("images/episode3/313.webp") with dissolve
    toby "Tebakan."
    if toby_job == 0:
        lisa "Mengingat fakta bahwa Anda bekerja sebagai agen real estat, saya ingin mengatakan 23, tetapi saya tidak berpikir Anda jauh lebih tua dari kami."
    else:
        lisa "Anda bertindak seperti Anda berusia 23 tahun atau bahkan lebih tua, tetapi saya benar -benar tidak berpikir Anda jauh lebih tua dari kami."
    lisa "Jadi saya pergi dengan 20."
    if lauren_path:
        lauren "Tidak ... dengan ukuran kemaluan Anda, saya katakan 24."
        scene expression ("images/episode3/314.webp") with dissolve
        lisa "Ukuran kemaluannya? Apa hubungannya dengan usia?"
        lauren "Anda hanya melihat satu ayam. Tentu saja Anda tidak dapat membedakannya."
    else:
        lauren "Tidak ... lihat dia, sangat nyaman dengan para wanita. Dia harus berusia setidaknya 24 tahun."
        scene expression ("images/episode3/314.webp") with dissolve
        lisa "Nyaman dengan para wanita? Apa hubungannya dengan usia?"
        lauren "Anda hanya punya satu pacar dan dia penipu. Jadi Anda tidak tahu bahwa ketika seorang pria pemalu itu berarti dia baik wanita atau dia sedikit lebih dewasa."
        toby "Atau dia hanya memiliki [mother] dan [sister]."
    scene expression ("images/episode3/315.webp") with dissolve
    lauren "Jadi? Siapa yang benar dan siapa yang salah?"
    toby "Nah, saya baru berusia 20 tahun."
    lisa "Jadi Anda hanya satu tahun lebih tua dari kami?"
    scene expression ("images/episode3/316.webp") with dissolve
    lauren "Tentu, Anda hanya harus memberitahunya berapa umur Anda. Anda tidak bisa mengizinkan saya mengajukan pertanyaan kepadanya. Saya ingin melihat berapa usia yang dia pikirkan!"
    lisa "Dia akan mengatakan 41. Kamu hag tua."
    scene expression ("images/episode3/317.webp") with dissolve

    lauren "Hag tua? Aku akan menunjukkan padamu."
    scene expression ("images/episode3/318.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/319.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/320.webp") with dissolve
    $ progress = 47
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}These girls are nice, but why am I falling for them? I have a girlfriend. The reason I came here was to make them understand we can only be friends. That's all.{/i}"
    scene expression ("images/episode3/321.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/322.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/323.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/324.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/325.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/326.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/326_1.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/327.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/328.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/328_1.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    if lisa_path == True:
        scene expression ("images/episode3/329.webp") with dissolve
        menu:
            "{i} [JGR] Tangkap lisa {/i}"(csq="Lisa +1 & Galeri Gambar"):
                $ unlockImage(persistent.lisa_04)
                $ lisa_rel += 1
                scene expression ("images/episode3/330.webp") with dissolve
                lisa "Maaf untuk itu! Dia bodoh!"
                toby "Jangan khawatir sayang."
            "{i} don \ 't menangkapnya {/i}":
                scene expression ("images/episode3/331.webp") with dissolve
                lisa "Kamu jalang!"
    else:
        scene expression ("images/episode3/332.webp") with dissolve
        menu:
            "{i} [JGR] Tetap di sana {/i}"(csq="Lauren +1 & Galeri Gambar"):
                $ unlockImage(persistent.lauren_04)
                $ lauren_rel += 1
                scene expression ("images/episode3/333.webp") with dissolve
                lauren "Ups. Bad saya!"
                toby "Jangan khawatir sayang."
            "{i} pindah {/i}":
                scene expression ("images/episode3/334.webp") with dissolve
                lauren "Saya tidak percaya Anda pindah!"


    scene expression ("images/episode3/335.webp") with long_fade
    if toby_job == 0:
        lauren "Jadi [toby!c], ceritakan lebih banyak tentang diri Anda? Bagaimana Anda menemukan pekerjaan ini?"
        toby "Oh, pekerjaanku? Sebenarnya ini lucu."
        toby "Senin pagi, saya sarapan dan [mom] saya mencari pekerjaan untuk dirinya sendiri."
        scene expression ("images/episode3/336.webp") with dissolve
        toby "Dia tidak pernah bekerja sehari pun dalam hidupnya dan sekarang di sini dia mencari pekerjaan."
        lisa "Dia persis seperti [mom] saya."
        toby "Ah, benarkah?"
        lisa "Ya. Dia selalu merawat saya dan saudara lelaki saya. Dia tidak pernah bekerja sehari pun."
        scene expression ("images/episode3/337.webp") with dissolve
        lauren "Anda memiliki banyak kesamaan."
        lisa "Diam!"
        lisa "Jadi apa yang terjadi kemudian?"
        toby "Ya, jadi. Itu dia, mencari pekerjaan dan saya melihatnya. Aku tidak bisa membiarkannya bekerja, maksudku, dia adalah [mom]. Saya ingin merawatnya."
        scene expression ("images/episode3/338.webp") with dissolve
        lauren "Anda seorang pria [family]. Jadi begitu!"
        toby "Mari kita katakan bahwa saya adalah pria [family]. Jadi saya bilang saya akan menjadi orang yang menelepon tentang pekerjaan itu."
        toby "Secara mengejutkan, bos saya benar -benar membutuhkan seseorang dan meminta saya untuk datang pada hari yang sama."
        toby "Jadi di sanalah saya, dua jam kemudian, di kantornya berbicara dengan istrinya."
        scene expression ("images/episode3/339.webp") with dissolve
        lauren "Istrinya? Apakah dia seorang lesbian?"
        toby "Ya dia, tetapi bagian yang lucu adalah bahwa saya tidak tahu dengan siapa saya berbicara pada awalnya dan istrinya terus mengajukan pertanyaan pribadi kepada saya."
        toby "Rasanya sangat canggung, karena ini adalah wawancara kerja pertama saya dan itu sangat aneh."
        lisa "Saya pikir siapa pun akan merasakan hal yang sama dalam situasi Anda."
        scene expression ("images/episode3/340.webp") with dissolve
        toby "Ya, jadi setelah saya menjawab beberapa pertanyaannya, Nyonya Darlene datang di kantor."
        toby "Dia meminta maaf atas segalanya dan kemudian dia bertanya kepada saya tentang diri saya dan sebagainya, dan kemudian dia mengatakan kepada saya bahwa dia sangat menyukaiku."
        if lisa_path == True:
            lauren "Saya pikir Lisa tahu mengapa dia menyukai Anda."
        else:
            lauren "Saya bisa melihat mengapa!"
        scene expression ("images/episode3/341.webp") with dissolve
        toby "Terima kasih! Dan kemudian dia hanya memberi tahu saya, saya ingin Anda datang besok dengan saya untuk menjual apartemen."
        lisa "Apartemen yang Anda jual kami?"
        toby "Ho!"
        lisa "Itu sangat keren. Biasanya orang tidak dipekerjakan secepat itu."
        scene expression ("images/episode3/342.webp") with dissolve
        lauren "Jadi? Apakah kamu menidurinya?"
        toby "Tentu saja tidak. Maksudku, dia sudah menikah. Saya tidak mencari masalah dengan wanita yang sudah menikah!"
        if lisa_path == True:
            scene expression ("images/episode3/343.webp") with dissolve
            lauren "Lihat Lisa? Seperti inilah pria yang baik!"
            lisa "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n{i}Lauren!{/i}"
            scene expression ("images/episode3/344.webp") with dissolve
            lisa "Maaf untuk itu. Dia pasti memukul kepalanya ketika dia masih kecil."
            toby "Anda tidak punya alasan untuk merasa buruk. Ini baik -baik saja!"
        else:
            scene expression ("images/episode3/343.webp") with dissolve
            lauren "Lihat Lisa? Sudah kubilang ada lebih banyak baginya di samping ayam gemuk besar!"
            lisa "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n{i}Lauren!{/i}"
    else:

        lauren "Jadi [toby!c], ceritakan lebih banyak tentang diri Anda. Anda baru saja pindah dan sudah pergi mencari vagina di klub?"
        toby "Saya sebenarnya ada di sana untuk pertemuan bisnis."
        lauren "Pertemuan Bisnis? Anda mengadakan pertemuan bisnis di klub?"
        toby "Ya. Saya akan bekerja di klub itu. Pekerjaan saya adalah mengawasi semua yang terjadi."
        scene expression ("images/episode3/336.webp") with dissolve
        toby "Untuk memastikan semua orang bersenang -senang. Untuk memastikan orang tidak berkelahi."
        lisa "Jadi Anda menjadi Knight in Shining Armor adalah bagian dari pekerjaan itu?"
        toby "Mungkin?"
        lauren "Mungkin pantatku. Saya melihat Anda melihat kami ketika kami tiba. Anda berbicara dengan seorang wanita."
        scene expression ("images/episode3/337.webp") with dissolve
        lauren "Anda hanya ingin menggoda kami dan pria itu menghalangi Anda!"
        toby "Anda dekat, tapi tidak. Bos saya memperhatikan bahwa pria itu bertaruh dengan teman -temannya dan kemudian dia datang untuk menggoda Anda."
        lisa "Jadi dia mengirimmu?"
        toby "Saya adalah orang yang bersikeras. Dia hanya mengatakan kepada saya bahwa ini adalah situasi yang perlu kita hindari. Pria membuat gadis merasa tidak nyaman."
        scene expression ("images/episode3/338.webp") with dissolve
        lauren "Saya suka pekerjaan Anda! Itu keren!"
        toby "Ya, jadi itu cukup banyak tes saya dan karena saya lulus, saya mendapatkan pekerjaan."
        lisa "Jadi pada dasarnya Anda berhutang kepada kami, kan?"
        toby "Jika itu bagaimana Anda ingin meletakkannya, mengapa tidak!"
        scene expression ("images/episode3/339.webp") with dissolve
        lauren "Anda berhutang besar pada kami! Mulai sekarang kami hanya akan mengunjungi klub itu, karena Anda membuat kami merasa aman."
        toby "Berbicara tentang klub. Anda baru saja memarahi saya pada hari pertama saya di kota saya pergi untuk mendapatkan beberapa vagina di klub. Saya menjelaskan mengapa saya ada di sana, sekarang giliran Anda."
        lisa "Jangan lihat aku. Dia membuatku datang. Dia orang yang ingin pergi."
        toby "Jadi, Lauren! Apa yang Anda cari di klub?"
        scene expression ("images/episode3/340.webp") with dissolve
        lauren "Saya tidak yakin Anda siap mendengar jawabannya!"
        toby "Bisa aja. Saya lahir siap!"
        if lisa_path == True:
            lauren "Lisa membutuhkan bercinta yang baik dan saya memutuskan untuk bermain wingman. Atau itu adalah Winggirl?"
            scene expression ("images/episode3/341.webp") with dissolve
            lisa "Tolong jangan dengarkan dia! Dia bodoh!"
            lauren "Saya mungkin, tapi itu tidak berarti saya berbohong!"
        else:
            lauren "Saya mencari penis untuk mengisap!"
            scene expression ("images/episode3/341.webp") with dissolve
            lisa "Dan coba tebak, dia menemukan persis apa yang dia cari!"
            lauren "Sebenarnya saya melakukannya. Saya menemukan ayam gemuk besar!"

        scene expression ("images/episode3/342.webp") with dissolve
        toby "Ya! Apa yang bisa saya katakan, saya akan memastikan bahwa Anda akan bersenang -senang setiap kali Anda ada di sana."
        if lisa_path == True:
            scene expression ("images/episode3/343.webp") with dissolve
            lauren "Dan mengapa tidak membuat Anda merasa baik juga!Lihat Lisa? Beginilah cara pria sejati harus bertindak. Membuat Anda merasa aman!"
            lisa "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n{i}Lauren!{/i}"
            scene expression ("images/episode3/344.webp") with dissolve
            lisa "Maaf untuk itu. Dia pasti memukul kepalanya ketika dia masih kecil."
            toby "Anda tidak punya alasan untuk merasa buruk. Ini baik -baik saja!"
        else:
            scene expression ("images/episode3/343.webp") with dissolve
            lauren "Lihat Lisa? Sudah kubilang ada lebih banyak baginya di samping ayam besar!"
            lisa "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n{i}Lauren!{/i}"
            lauren "Dia juga seorang pria yang akan menjaga kita tetap aman di klubnya!"

    scene expression ("images/episode3/345.webp") with dissolve
    barman "Halo teman -teman. Apa yang bisa saya dapatkan dari Anda?"
    toby "Hai, yang di sana. Saya ada di sini pada hari Senin dan Anda memberi saya sesuatu yang sangat, sangat bagus."
    barman "Aku ingat kamu! Anda menyukainya?"
    if ep1_get_charlotte_drunk == True:
        toby "Saya tidak mendapatkan kesempatan untuk meminumnya, jadi sekarang saya harap saya akan melakukannya!"
    else:
        toby "Ya, sebenarnya itu benar -benar bagus!"
    scene expression ("images/episode3/346.webp") with dissolve
    barman "Dan untuk para wanita?"
    lauren "Beri kami hal yang sama."
    lisa "Apakah itu memiliki alkohol?"
    barman "Itu benar!"
    lauren "Jangan repot -repot bertanya padanya. Dia akan mendapatkan hal yang sama dengan kita!"
    barman "Apa kamu yakin?"
    lisa "Bagus! Beri kami hal yang sama seperti [toby!c]."
    barman "Datang Tepat!"


    scene expression ("images/episode3/347_curious_3.webp") with dissolve
    toby "Jadi saya sudah menceritakan kisah saya. Sekarang giliranmu!"
    scene expression ("images/episode3/348_smile_1.webp") with dissolve
    lisa "Baik tidak banyak yang bisa dikatakan tentang saya, jadi saya akan membiarkan Lauren memulai."
    scene expression ("images/episode3/349_laugh_2.webp") with dissolve
    lauren "Bagus! Saya akan mulai."
    scene expression ("images/episode3/349_smile_1.webp") with dissolve
    lauren "Saya ingin memulai dengan mengatakan bahwa saya bukan ho. Saya mungkin agak gila dan saya suka seks, tapi saya tidak ada."
    scene expression ("images/episode3/347_normal_3.webp") with dissolve
    toby "Tidak ada yang mengatakan Anda."
    toby "Jadi selain seks, apa lagi yang Anda suka."
    scene expression ("images/episode3/349_laugh_1.webp") with dissolve
    lauren "Ya, jadi. Saya suka menari dan bermain gitar. Maksud saya, saya dulu suka bermain gitar."
    scene expression ("images/episode3/349_nails_1.webp") with dissolve
    lauren "Sekarang saya tidak bisa bermain lagi karena ini, tapi kadang -kadang saya merindukannya. Saya juga suka pergi ke gym."
    scene expression ("images/episode3/349_smile_1.webp") with dissolve
    lauren "Sepertinya saya mengganti gitar dengan gym. Saya suka kata -kata yang dimulai dengan G."
    scene expression ("images/episode3/349_laugh_1.webp") with dissolve
    lauren "Apakah Anda menyukai G?"
    scene expression ("images/episode3/348_facepalm_3.webp") with dissolve
    lisa "Saya tidak percaya Anda bertanya apakah dia menyukai tempat G!"
    scene expression ("images/episode3/349_laugh_2.webp") with dissolve
    lauren "Siapa bilang sesuatu tentang G Spot? Saya hanya bertanya kepadanya apakah dia menyukai surat G."
    scene expression ("images/episode3/347_laugh_3.webp") with dissolve
    menu:
        "[JGR] Saya suka \ 'g \'."(csq="Lauren +1 & Galeri Gambar"):
            $ lauren_rel += 1
            $ unlockImage(persistent.lauren_05)
            toby "Nah, untuk menjawab pertanyaan Anda, saya pikir saya suka \ 'g \'."
            scene expression ("images/episode3/349_flirty_1.webp") with dissolve
            lauren "Saya akan mengingatnya."
        "{i} ubah subjek {/i}":
            toby "Jadi apa lagi yang kamu suka?"
    scene expression ("images/episode3/349_happy_1.webp") with dissolve
    lauren "Saya suka es krim. Maksud saya, saya suka es krim, sebenarnya."
    scene expression ("images/episode3/349_curious_1.webp") with dissolve
    lauren "Apakah Anda akan membawa kami untuk mendapatkan es krim?"
    scene expression ("images/episode3/347_happy_3.webp") with dissolve
    toby "Saya akan memikirkannya. Itu juga tergantung pada Lisa. Saya perlu belajar lebih banyak tentang dia juga."
    scene expression ("images/episode3/347_curious_2.webp") with dissolve
    toby "Bagaimana jika Anda membuat semacam pembunuh berantai!"
    scene expression ("images/episode3/348_laugh_1.webp") with dissolve
    lisa "Apakah saya benar -benar terlihat seperti bisa membunuh siapa pun?"
    scene expression ("images/episode3/349_smile_1.webp") with dissolve
    lauren "Dia tidak punya nyali untuk membunuh lalat, bagaimana dia membunuh siapa pun."
    scene expression ("images/episode3/348_pouty_3.webp") with dissolve
    lisa "Anda punya waktu. Sekarang giliranku!"
    scene expression ("images/episode3/349_flirty_2.webp") with dissolve
    lauren "Permisi. Saya tidak tahu Anda ingin membuatnya terkesan juga."
    scene expression ("images/episode3/348_tongue_3.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/347_laugh_3.webp") with dissolve
    toby "Jika saya jadi Anda, saya adalah zip. Maksudku, dia terlihat sangat gila."
    scene expression ("images/episode3/348_laugh_1.webp") with dissolve
    lisa "Saya bukan pembunuh berantai!"
    scene expression ("images/episode3/347_happy_2.webp") with dissolve
    toby "Saya percaya Anda. Jadi jika Anda tidak ada pembunuh berantai daripada ceritakan lebih banyak tentang diri Anda."
    scene expression ("images/episode3/348_happy_1.webp") with dissolve
    lisa "Jadi saya suka membaca, saya suka bermain tenis, saya suka melukis, tapi sayangnya lukisan saya sama dengan musik untuk Lauren."
    scene expression ("images/episode3/348_sad_1.webp") with dissolve
    lisa "Saya belum melukis apa pun seperti selamanya. Saya sangat sibuk dengan tahun senior saya di sekolah menengah dan dengan masuk perguruan tinggi sehingga saya agak mengabaikan lukisan itu."
    scene expression ("images/episode3/348_smile_1.webp") with dissolve
    lisa "Dan juga saya mencintai anak -anak. Saya ingin menjadi guru."
    scene expression ("images/episode3/347_laugh_2.webp") with dissolve
    toby "Anda akan menjadi guru pertama yang benar -benar saya rukun."
    scene expression ("images/episode3/348_laugh_1.webp") with dissolve
    lisa "Buruk itu?"
    scene expression ("images/episode3/347_normal_2.webp") with dissolve
    toby "Anda tidak tahu!"
    scene expression ("images/episode3/350.webp") with dissolve
    barman "Ini minuman Anda."
    scene expression ("images/episode3/351.webp") with dissolve
    toby "Terima kasih!"
    lisa "Anda tidak harus membayar untuk kami."
    toby "Jangan khawatir, itu padaku."
    scene expression ("images/episode3/352.webp") with dissolve
    lauren "Jadi [toby!c], saya ingin menanyakan sesuatu kepada Anda."
    lauren "Kenapa pria keren seperti Anda tidak punya pacar?"
    scene expression ("images/episode3/353.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit. Now is the moment. What should I do?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Should I tell them the truth or lie to them and maybe break up with Emma afterwards.{/i}"
    $ progress = 48
    menu:
        "{i} beri tahu mereka kebenaran {/i} [JWRN]"(csq="Untuk sementara menutup jalan dengan gadis -gadis itu"):
            $ ep3_lieGirls = False
            $ unlockImage(persistent.emma_04)
            scene expression ("images/episode3/354_awkward_3.webp") with dissolve
            toby "Umm ... tentang itu. Alasan utama mengapa saya benar -benar ingin datang dan melihat Anda, adalah karena saya perlu memberi tahu Anda sesuatu."
            toby "Saya punya pacar, dan saya ingin meminta maaf atas semua yang saya lakukan."
            if lisa_path == True:
                scene expression ("images/episode3/355_sad_1.webp") with dissolve
                lisa "Anda lakukan?"
                scene expression ("images/episode3/354_sad_2.webp") with dissolve
                toby "Saya minta maaf jika saya membuat Anda berpikir sebaliknya. Saya minta maaf atas ciuman dan segalanya."
                toby "Saya terjebak pada saat itu dan ya, itu terjadi."
                scene expression ("images/episode3/355_awkward_1.webp") with dissolve
                lisa "Tidak ... Ini bukan salahmu. Aku adalah orang yang menciummu!"
                scene expression ("images/episode3/357_angry_2.webp") with dissolve
                lauren "Bukan salahnya? Dia bisa mendorongmu, tapi tidak, dia ingin menciummu."
                scene expression ("images/episode3/357_angry_1.webp") with dissolve
                lauren "Anda seorang bajingan. Anda tahu itu, kan?"
                scene expression ("images/episode3/354_sad_3.webp") with dissolve
                toby "Saya tahu itu. Dan saya minta maaf untuk semuanya."
                scene expression ("images/episode3/357_sad_2.webp") with dissolve
                lauren "Ayo gadis. Ayo pergi. Dia sama seperti mantanmu."
                scene expression ("images/episode3/357_angry_1.webp") with dissolve
                lauren "Terima kasih atas minumannya!"
            else:
                scene expression ("images/episode3/357_surprised_1.webp") with dissolve
                lauren "Wow! Dan Anda tidak berpikir untuk menyebutkan ini sebelum saya mengisap kemaluan Anda?"
                scene expression ("images/episode3/354_awkward_3.webp") with dissolve
                toby "Maaf, saya baru saja ..."
                scene expression ("images/episode3/357_angry_1.webp") with dissolve
                lauren "Tidak, itu baik -baik saja. Sepertinya saya mungkin ho."
                scene expression ("images/episode3/356.webp") with dissolve
                lauren "Tapi seorang pria yang menipu pacarnya lebih buruk!"
                lauren "Biarkan saja!"

            scene expression ("images/episode3/358.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe it's better this way.{/i}"
            scene expression ("images/episode3/359.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think I should go home now.{/i}"
            return
        "{i} [JGR] berbohong kepada mereka {/i}":

            $ ep3_lieGirls = True
            scene expression ("images/episode3/354_sad_3.webp") with dissolve
            toby "Yah, saya baru saja mengeluarkan hubungan. Ketika pacar saya tahu saya sedang bergerak, dia menyarankan agar kita putus, karena hubungan jarak jauh tidak pernah berhasil."
            scene expression ("images/episode3/355_sad_1.webp") with dissolve
            lisa "Oh, itu menyebalkan. Saya sangat menyesal!"
            scene expression ("images/episode3/354_awkward_2.webp") with dissolve
            toby "Jangan khawatir tentang hal itu, baik -baik saja!"
            scene expression ("images/episode3/357_flirty_1.webp") with dissolve
            lauren "Jadi pada dasarnya, alasan Anda lajang adalah karena Anda baru saja keluar dari suatu hubungan dan belum ada wanita jalang yang berhasil mendapatkan tangannya?"
            scene expression ("images/episode3/354_laugh_3.webp") with dissolve
            toby "Saya tidak akan mengatakan pelacur, tetapi kurang lebih Anda tepat!"

            if lisa_path == True:
                scene expression ("images/episode3/357_flirty_2.webp") with dissolve
                lauren "Dia semua milikmu. Lompat dia, sebelum orang lain melakukannya!"
                scene expression ("images/episode3/355_shy_3.webp") with dissolve
                lisa "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n{i}Lauren! You're making him feel awkward.{/i}"
                scene expression ("images/episode3/354_smile_2.webp") with dissolve
                toby "Jangan khawatir. Ini baik -baik saja. Saya sudah terbiasa!"
            else:

                scene expression ("images/episode3/357_flirty_2.webp") with dissolve
                lauren "Jadi itu berarti saya harus mendapatkan Anda sebelum orang lain melakukannya?"
                scene expression ("images/episode3/354_flirty_3.webp") with dissolve
                toby "Saya pikir itu sebaliknya!"

            scene expression ("images/episode3/355_awkward_1.webp") with dissolve
            lisa "Ngomong -ngomong, apa lagi yang bisa kamu lakukan di pantai ini?"
            scene expression ("images/episode3/357_laugh_2.webp") with dissolve
            lauren "Saya punya ide!"
            scene expression ("images/episode3/355_smile_3.webp") with dissolve
            lisa "Jika itu adalah salah satu lelucon seks bodoh Anda, maka lewati!"
            scene expression ("images/episode3/357_flirty_2.webp") with dissolve
            lauren "Menurut Anda, cabang seperti apa?"
            scene expression ("images/episode3/360.webp") with dissolve

            if lisa_path == True:
                lauren "Saya akan menyarankan Anda dan [toby!c] berjalan -jalan di belakang batu -batu itu dan memberi tahu saya apa yang dapat Anda lakukan di sana!"
                lisa "Persis seperti apa lelucon seks!"
                lauren "Saya tidak pernah mengatakan berhubungan seks di sana, Anda orang yang berpikir itu akan menjadi ide yang bagus!"
            else:
                lauren "Saya akan menyarankan agar saya dan [toby!c] pergi ke belakang batu -batu itu dan kemudian kembali untuk memberi tahu Anda apa yang dapat Anda lakukan di sana!"
                lisa "Persis seperti apa lelucon seks!"
                lauren "Saya tidak mengatakan apa -apa tentang berhubungan seks di sana. Anda yang memiliki pikiran kotor di sini."
            scene expression ("images/episode3/361.webp") with dissolve
            toby "Nah, kami bisa bermain voli pantai, jika Anda tidak terlalu takut Anda akan kalah!"
            scene expression ("images/episode3/362.webp") with dissolve
            if lisa_path:
                lisa "Oke, tapi kami bermain dua melawan satu!"
            else:
                lauren "Oke, tapi kami bermain dua melawan satu. Saya yakin Anda bisa menangani threesome!"
                lisa "Orang cabul!"
            scene expression ("images/episode3/361.webp") with dissolve
            toby "Kesepakatan!"
            pass

    scene expression ("images/episode3/363.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/364.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/365.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/366.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/367_1.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/367_2.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/367_3.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/368_1.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/368_2.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/368_3.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    show screen ui_message("A few hours later") with long_dissolve
    $ progress = 49
    $ ui.saybehavior()
    $ ui.interact()
    if lisa_path == True:
        scene expression ("images/episode3/369.webp") with dissolve
        hide screen ui_message
        lisa "Saya pikir aman untuk mengatakan kami menendang pantat Anda."
        toby "Aku membiarkanmu menang!"
        lauren "Sungguh pembohong!"
        scene expression ("images/episode3/370.webp") with dissolve
        lauren "Bagaimana Anda bisa berdiri berbohong seperti itu?"
        toby "Saya beruntung saya lucu!"
        lisa "Dan siapa yang memberitahumu itu?"
        toby "Saya [mother] dan [father]."
        scene expression ("images/episode3/371.webp") with dissolve
        lisa "Mereka berbohong padamu!"
        toby "Mustahil!"
        scene expression ("images/episode3/372.webp") with dissolve
        lauren "Pokoknya teman -teman, saya pikir saya akan pulang. Aku akan membiarkan kalian berdua mencintai burung sedikit lagi. Bisakah Anda membawa Lisa pulang nanti?"
        scene expression ("images/episode3/373.webp") with dissolve
        toby "Saya ingin sekali, jika Anda tidak takut mengendarai sepeda."
        lisa "Anda tidak tahu siapa yang Anda bicarakan juga!"
        scene expression ("images/episode3/372.webp") with dissolve
        lauren "Itu bagus sekali kalau begitu."
        scene expression ("images/episode3/380.webp") with dissolve
        lauren "Jangan tinggal terlalu lama, oke?"
        lisa "Oke, Bu!"
        scene expression ("images/episode3/381.webp") with dissolve
        lauren "Jaga dia dengan baik. Oke [toby!c]?"
        toby "Ya ma \ 'am."
        lauren "Aku mencintaimu!"
        lisa "Love You Sweetie!"
        if lauren_sidePath == True:
            scene expression ("images/episode3/383.webp") with dissolve
            lauren "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Bye sexy!{/i}"
            toby "Sampai jumpa!"

        return
    else:

        scene expression ("images/episode3/374.webp") with dissolve
        hide screen ui_message
        lauren "Kami menendang pantatmu."
        toby "Saya tidak berpikir Anda mengerti bagaimana Anda memenangkan game ini."
        toby "Aku menendang pantatmu."
        scene expression ("images/episode3/375.webp") with dissolve
        lisa "Itu bohong! Kami menang."
        lisa "Anda sangat jelek jika Anda bertanya kepada saya!"
        scene expression ("images/episode3/376.webp") with dissolve
        lauren "Dia tidak perlu pandai dalam bola voli selama dia pandai dalam kegiatan lain!"
        toby "Seseorang tahu apa yang penting dalam hidup!"
        scene expression ("images/episode3/377.webp") with dissolve
        lisa "Saya pikir saya harus pulang. Saya lelah. Saya bisa datang menjemput Anda nanti jika Anda mau."
        scene expression ("images/episode3/378.webp") with dissolve
        toby "Jangan khawatir. Aku akan membawanya pulang."
        scene expression ("images/episode3/377.webp") with dissolve
        lisa "Segar bugar?"
        scene expression ("images/episode3/378.webp") with dissolve
        toby "Segar bugar."
        scene expression ("images/episode3/379.webp") with dissolve
        toby "Saya harap Anda tidak takut mengendarai sepeda dengan saya."
        lauren "Jangan khawatir tentang saya. Saya suka berkuda."
        scene expression ("images/episode3/377.webp") with dissolve
        lisa "Orang cabul!"
        scene expression ("images/episode3/380.webp") with dissolve
        lisa "Cobalah untuk tidak hamil."
        lauren "Saya akan melakukan yang terbaik."
        scene expression ("images/episode3/382.webp") with dissolve
        lisa "Sampai jumpa nanti."
        lauren "Bye Love!"
        lisa "Sampai jumpa!"
        if lisa_sidePath == True:
            scene expression ("images/episode3/384.webp") with dissolve
            lisa "Bye [toby!c]!"
            toby "Bye Lisa!"
        return


label episode3_dateLisa:
    $ progress = 50

    scene expression ("images/episode3/385.webp") with dissolve
    lisa "Apakah Anda yakin ingin tinggal? Saya bisa pulang dengan Lauren jika Anda memiliki hal -hal yang lebih baik untuk dilakukan."
    toby "Izinkan saya memeriksa jadwal saya, terlebih dahulu."
    lisa "Oke."
    toby "Aku main -main denganmu! Tentu saja saya ingin menghabiskan lebih banyak waktu dengan Anda!"
    scene expression ("images/episode3/386.webp") with dissolve
    lisa "Oh! Saya masih tidak tahu kapan Anda serius atau ketika Anda hanya menggodaku."
    toby "Jangan khawatir, Anda akan mencari tahu pada akhirnya!"
    scene expression ("images/episode3/387.webp") with dissolve
    toby "Ayo, mari kita berjalan -jalan."
    scene expression ("images/episode3/388.webp") with long_dissolve
    lisa "Maaf tentang Lauren. Dia agak gila, tapi dia sahabatku dan aku mencintainya."
    toby "Sudah kubilang sebelumnya, itu tidak mengganggu saya. Saya juga punya teman seperti itu. Senang rasanya memilikinya."
    lisa "Ya, menghabiskan waktu dengan mereka itu menyenangkan!"
    scene expression ("images/episode3/389.webp") with dissolve
    toby "Ya, itu menyenangkan! Tapi menghabiskan waktu seperti ini lebih baik!"
    lisa "Umm ..."
    toby "Apakah saya mengatakan sesuatu yang salah?"
    scene expression ("images/episode3/390.webp") with dissolve
    lisa "Tidak, itu hanya itu ... hanya itu, aku mulai jatuh cinta padamu dan aku sedikit takut."
    toby "Takut? Kenapa begitu?"
    lisa "Karena mantan pacar saya. Saya tidak ingin melewatinya lagi."
    scene expression ("images/episode3/391.webp") with dissolve
    toby "Jika Anda ingin membicarakannya, saya ada di sini."
    lisa "Umm ... baik ayah saya dan ayahnya adalah teman baik di perguruan tinggi. Mereka menjadi kaya bersama dan kami tumbuh bersama."
    lisa "Kami mulai berkencan dan itu datang secara alami, tetapi ia terbiasa menjadi tipe pria yang mengendalikan segalanya."
    lisa "Ayahnya memiliki 51 %% dari perusahaan sementara ayah saya hanya memiliki 49 %% dan dia selalu bertindak seolah -olah dia lebih baik dari saya."
    scene expression ("images/episode3/392.webp") with dissolve
    toby "Bagaimana dia bisa lebih baik darimu hanya karena ayahnya punya sesuatu?"
    lisa "Persis ... Ngomong -ngomong, dia satu -satunya pacarku dan dia selalu mengendalikanku. Dia selalu memberi tahu saya apa yang harus dimakan, cara berpakaian dan sebagainya."
    lisa "Awalnya saya pikir ini adalah bagaimana hal -hal seharusnya dalam suatu hubungan."
    scene expression ("images/episode3/393.webp") with dissolve
    lisa "It was strange for me, because I was always controlled and whenever I was asked him something, he was like \"I don't have to tell you anything!\""
    toby "Saya menyesal Anda berada dalam hubungan yang beracun!"
    lisa "Ya. Beruntung bagi saya, Lauren menangkapnya selingkuh dengan beberapa gadis dan kemudian kami putus dan sejak itu saya bahkan belum berbicara dengan pria lain."
    scene expression ("images/episode3/394.webp") with dissolve
    toby "Saya mengerti. Anda takut."
    lisa "Sedikit."
    lisa "Jadi menurut Anda apakah kami bisa melakukannya dengan lambat?"
    scene expression ("images/episode3/395.webp") with dissolve
    toby "Lihat, saya sangat menyukai Anda dan jika ini yang Anda butuhkan, saya akan berada di sini. Kecepatan apa pun yang Anda butuhkan!"
    scene expression ("images/episode3/396.webp") with dissolve
    lisa "Terima kasih."
    toby "Tidak masalah!"
    scene expression ("images/episode3/397.webp") with dissolve
    toby "Haruskah kita duduk?"
    lisa "Saya akan menyukainya!"
    scene expression ("images/episode3/398.webp") with dissolve
    lisa "Ngomong -ngomong, saya perlu meminta maaf atas cara kami bertemu."
    lisa "Saya tidak tahu apa yang terjadi pada saya. Anda adalah orang kedua yang pernah saya cium. Itu sangat aneh."
    toby "Ya, saya akan bertanya tentang itu."
    toby "Maksud saya untuk mengenal Anda lebih baik, ciuman itu tidak tampak seperti gaya Anda."
    scene expression ("images/episode3/399.webp") with dissolve
    lisa "Saya sangat senang Anda menolak blowjob Lauren dan kemudian dia agak mendorong saya. Itu semua terjadi begitu cepat."
    toby "Jadi saya harus berterima kasih kepada Lauren untuk ciumannya?"
    lisa "Nah, tidak apa -apa. Anda bisa berterima kasih kepada saya!"
    scene expression ("images/episode3/400.webp") with dissolve
    lisa "Masalahnya adalah bahwa Lauren selalu bertindak sangat bodoh. Setiap kali dia melihat seorang pria seksi, dia mulai bertingkah seperti pelacur. Dia suka bersenang -senang."
    lisa "Dan melihat Anda menolak itu untuk ciuman di pipi benar -benar lucu."
    toby "Apa yang bisa saya katakan. Saya penuh kejutan!"
    scene expression ("images/episode3/401.webp") with dissolve
    lisa "Ya, kamu!"
    toby "Tuhan ... kamu sangat cantik!"
    scene expression ("images/episode3/402.webp") with dissolve
    lisa "Terima kasih!"
    scene expression ("images/episode3/403.webp") with dissolve
    lisa "Apakah kamu benar -benar menyukaiku?"
    toby "Tentu saja! Apa yang tidak disukai?"
    scene expression ("images/episode3/404.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode3/404_1.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wanna kiss her so bad!{/i}"
    menu:
        "{i} [JGR] Cium dia {/i}"(csq="Lisa +1 & Galeri Gambar"):
            $ unlockImage(persistent.lisa_05)
            $ lisa_rel += 1
            $ ep3_kissLisa = True
            show ep3_405
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode3/406.webp") with dissolve
            hide ep3_405
            toby "Maaf. Saya tahu Anda mengatakan bahwa Anda ingin melakukannya dengan lambat, saya hanya tidak bisa ..."
            lisa "Don't worry"
            show ep3_407
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode3/407.webp")
            hide ep3_407
        "{i} don \ 't to apa pun {/i}":
            pass
    scene expression ("images/episode3/409.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/utils/black.png") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    return


label episode3_dateLauren:
    $ progress = 50

    scene expression ("images/episode3/410.webp") with dissolve
    lauren "Saya harap \ 'tidak masalah bagi Anda, jika Anda memiliki sesuatu yang lain, saya dapat pergi dengan Lisa."
    toby "Anda tidak perlu khawatir! Saya ingin meluangkan waktu dengan Anda, dan mungkin mengenal Anda lebih baik."
    scene expression ("images/episode3/411.webp") with dissolve
    lauren "Haruskah kita berjalan -jalan?"
    toby "Tentu saja! Mengapa tidak!"
    scene expression ("images/episode3/412.webp") with dissolve
    lauren "Saya melihat kita menuju ke batu!"
    lauren "Saya bercanda dengan seks di balik batu. Saya hanya suka menggoda Lisa. Ini lucu karena dia sangat memalukan dalam hal seks."
    toby "Dan Anda mengambil setiap kesempatan untuk mengolok -oloknya?"
    scene expression ("images/episode3/413.webp") with dissolve
    lauren "Tidak selalu, tetapi itu adalah kesenangan yang bersalah."
    toby "Saya mengerti."
    toby "Tapi hanya untuk memperjelas, saya tidak berpikir untuk pergi ke belakang batu, saya hanya suka dermaga di atas air!"
    toby "Itu terlihat sangat romantis!"
    scene expression ("images/episode3/414.webp") with dissolve
    lauren "Oh ... aku merasa sangat kotor sekarang. Anda berbicara tentang hal -hal romantis yang lucu dan saya berbicara tentang seks di luar ruangan!"
    toby "Jangan salah paham, Sex on the Beach terdengar menarik, tetapi Anda akan berakhir dengan pasir di vagina Anda!"
    toby "Dan kami tidak menginginkannya!"
    scene expression ("images/episode3/415.webp") with dissolve
    lauren "Anda sangat gila. Saya tidak pernah memikirkan seks di pantai seperti itu, tetapi sekarang saya hanya bisa memikirkan biji -bijian pasir di vagina saya!"
    toby "Senang rasanya seseorang melihat Anda sesekali, kan?"
    lauren "Ya. Anda tidak tahu!"
    scene expression ("images/episode3/416.webp") with dissolve
    toby "Jadi, bagaimana Anda berakhir di kota? Datang ke sini untuk kuliah untuk menjadi guru seperti Lisa?"
    lauren "Kota ini besar dan ya!Sebenarnya tidak. Saya akan menjadi penari profesional. Ada lebih banyak peluang di sini."
    toby "Apakah Anda lebih suka gaya menari?"
    scene expression ("images/episode3/417.webp") with dissolve
    lauren "Sejujurnya, saya sangat suka tarian eksotis, tetapi saya tidak berpikir saya akan pandai dalam hal itu, jadi saya pikir saya hanya akan tetap berpegang pada kontemporer."
    lauren "Saya berharap untuk bergabung dengan band dan menari di video musik."
    lauren "Kamu tahu?"
    scene expression ("images/episode3/418.webp") with dissolve
    toby "Sorry. You lost me after \"exotic dancer\"."
    lauren "Anda sangat bodoh! Saya menyukainya!"
    toby "Aku hanya mengacaukanmu, aku sangat berharap kamu akan menemukan band!"
    scene expression ("images/episode3/419.webp") with dissolve
    toby "Umm ... dermaga seperti ini!"
    lauren "Tapi batu -batu ini seperti ini!"
    toby "Saya pikir Anda mengatakan kepada saya bahwa Anda tidak ingin pergi ke belakang batu!"
    lauren "Saya tidak ingin berhubungan seks, karena saya mungkin berakhir dengan pasir di vagina saya, tetapi saya tidak mengatakan saya tidak ingin pergi ke belakang batu!"
    scene expression ("images/episode3/420.webp") with dissolve
    toby "Pimpin!"
    lauren "Jangan lihat pantatku!"
    scene expression ("images/episode3/421.webp") with dissolve
    toby "Uhum ... ya, benar!"
    scene expression ("images/episode3/422.webp") with dissolve
    lauren "Saya benar. Tempat ini sangat bagus untuk melakukan hal -hal nakal!"
    toby "Saya bisa memikirkan satu atau dua hal yang harus dilakukan di sini."
    lauren "Suka minum alkohol?"
    menu:
        "{i} [JGR] Cium dia {/i}"(csq="Lauren +1 & Galeri Gambar"):
            $ unlockImage(persistent.lauren_05)
            $ lauren_rel += 1
            $ ep3_kissLauren = True
            scene expression ("images/episode3/424.webp") with dissolve
            toby "Saya pikir saya bisa mendapatkan ide yang lebih baik!"
            lauren "Begitu?"

            scene expression ("images/episode3/425.webp")
            show ep3_425
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode3/426.webp")
            hide ep3_425
            show ep3_426

            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode3/427.webp")
            hide ep3_426
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wanna kiss her boobs so much!{/i}"
            scene expression ("images/episode3/428.webp")
            show ep3_428

            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode3/429.webp") with dissolve
            hide ep3_428
            lauren "Tolong berhenti, atau aku akan menidurimu di sini dan kemudian aku mungkin menyesal!"
            scene expression ("images/episode3/430.webp") with dissolve
            toby "Apakah ada yang salah?"
            lauren "Ya itu! Saya biasa bersenang -senang dan berhubungan seks, tetapi untuk beberapa alasan sialan saya menginginkan Anda lebih dari sekedar seks."
            lauren "Saya merasakan kupu -kupu di perut saya dan itu menakutkan!"
            lauren "Tolong jangan membenciku, aku hanya ..."
            scene expression ("images/episode3/431.webp") with dissolve
            toby "Tidak apa -apa, ayo duduk di dermaga!"
            lauren "Anda manis!"
        "{i} tertawa {/i}":

            scene expression ("images/episode3/423.webp") with dissolve
            toby "Dan menggunakan narkoba!"
            lauren "Ya, kenapa aku tidak memikirkan itu!"
            lauren "Ngomong -ngomong, mari kita kembali ke dermaga!"

    scene expression ("images/episode3/432.webp") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
