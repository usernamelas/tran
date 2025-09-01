image ep7_052 = Movie(play="video/episode7/052.webm", image="images/episode7/052.webp", loop = False)
image ep7_358 = Movie(play="video/episode7/358.webm", loop = True)
image ep7_362 = Movie(play="video/episode7/362.webm", loop = True)
image ep7_375 = Movie(play="video/episode7/375.webm", loop = True)
image ep7_377 = Movie(play="video/episode7/377.webm", loop = True)
image ep7_378 = Movie(play="video/episode7/378.webm", loop = True)
image ep7_381 = Movie(play="video/episode7/381.webm", loop = True)
image ep7_382 = Movie(play="video/episode7/382.webm", loop = True)
image ep7_385 = Movie(play="video/episode7/385.webm", loop = True)
image ep7_386 = Movie(play="video/episode7/386.webm", loop = True)
image ep7_387 = Movie(play="video/episode7/387.webm", loop = True)
image ep7_388 = Movie(play="video/episode7/388.webm", loop = True)
image ep7_424 = Movie(play="video/episode7/424.webm", loop = True)
image ep7_426 = Movie(play="video/episode7/426.webm", loop = True)
image ep7_430 = Movie(play="video/episode7/430.webm", loop = True)
image ep7_431 = Movie(play="video/episode7/431.webm", loop = True)
image ep7_434 = Movie(play="video/episode7/434.webm", image="images/episode7/434.webp", loop = False)
image ep7_435 = Movie(play="video/episode7/435.webm", loop = True)
image ep7_436 = Movie(play="video/episode7/436.webm", loop = True)
image ep7_437 = Movie(play="video/episode7/437.webm", loop = True)
image ep7_438 = Movie(play="video/episode7/438.webm", loop = True)
image ep7_440 = Movie(play="video/episode7/440.webm", loop = True)
image ep7_441 = Movie(play="video/episode7/441.webm", loop = True)
image ep7_466 = Movie(play="video/episode7/466.webm", loop = True)
image ep7_470 = Movie(play="video/episode7/470.webm", loop = True)
image ep7_471 = Movie(play="video/episode7/471.webm", loop = True)
image ep7_472 = Movie(play="video/episode7/472.webm", loop = True)
image ep7_473 = Movie(play="video/episode7/473.webm", loop = True)
image ep7_474 = Movie(play="video/episode7/474.webm", loop = True)
image ep7_475 = Movie(play="video/episode7/475.webm", loop = True)
image ep7_477 = Movie(play="video/episode7/477.webm", loop = True)
image ep7_478 = Movie(play="video/episode7/478.webm", loop = True)

label episode7:
    $ progress = 95
    stop music fadeout 4.0
    scene expression ("images/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(2, 1) with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    show screen ui_message("Monday") with long_dissolve
    hide screen ui_newEpisode
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message

    call episode7_monday_morning from _call_episode7_monday_morning
    call episode7_monday_collage_road from _call_episode7_monday_collage_road
    call episode7_monday_college from _call_episode7_monday_college
    call episode7_monday_back_home from _call_episode7_monday_back_home

    if toby_job == 0:
        call episode7_monday_realEstate from _call_episode7_monday_realEstate
    else:
        call episode7_monday_club from _call_episode7_monday_club

    call episode7_monday_evening from _call_episode7_monday_evening

    $ progress = 105
    if ep7_monday_date == "emma":
        call episode7_emma_date from _call_episode7_emma_date
    elif ep7_monday_date == "Lisa":
        call episode7_lisa_date from _call_episode7_lisa_date
    elif ep7_monday_date == "Lauren":
        call episode7_lauren_date from _call_episode7_lauren_date
    else:
        call episode7_monday_night from _call_episode7_monday_night

    call episode7_tuesday_morning from _call_episode7_tuesday_morning

    $ progress = 108
    if ep7_tuesday_date == "lisa":
        call episode7_lisa_date from _call_episode7_lisa_date_1
    elif ep7_tuesday_date == "Lauren":
        call episode7_lauren_date from _call_episode7_lauren_date_1

    return

label episode7_monday_morning:

    scene expression ("images/episode7/001.webp") with dissolve
    patricia "Bangkit dan bersinar, [toby!c]."
    toby "..."
    patricia "[toby!c] ... bangun!"
    toby "..."
    scene expression ("images/episode7/002.webp") with dissolve
    patricia "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n[toby!u]!!! Wake up."
    scene expression ("images/episode7/003.webp") with dissolve
    if toby_job == 0:
        toby "Kenapa kamu berteriak?"
    else:
        toby "Kenapa kamu berteriak?"
    scene expression ("images/episode7/004.webp") with dissolve
    patricia "Selamat pagi untukmu juga."
    if toby_job == 0:
        scene expression ("images/episode7/006.webp") with dissolve
        toby "Jam berapa sekarang? Apa yang terjadi?"
    else:
        toby "Jadi? Apakah Anda akan memberi tahu saya apa yang Anda inginkan atau apakah Anda baru saja membangunkan saya tanpa alasan?"
        scene expression ("images/episode7/005.webp") with dissolve
        patricia "Bagaimana Anda bisa begitu jahat pada bunga halus seperti saya?"
        scene expression ("images/episode7/006.webp") with dissolve
        toby "Bagus. Apa yang terjadi?"
    scene expression ("images/episode7/007.webp") with dissolve
    patricia "Nah, saya pikir Anda merindukan saya karena kami tidak lagi berbagi kamar."
    scene expression ("images/episode7/006.webp") with dissolve
    toby "Tolong beritahu saya bahwa bukan mengapa Anda membangunkan saya. Saya mengalami malam yang panjang tadi malam."
    scene expression ("images/episode7/008.webp") with dissolve
    patricia "Kehilangan [brother] saya bukan alasan yang cukup baik?"
    scene expression ("images/episode7/009.webp") with dissolve
    toby "Tidak tidak tidak. Wajah cemberut dan mata besar tidak akan bekerja kali ini."
    scene expression ("images/episode7/007.webp") with dissolve
    patricia "Baik ... Aku membangunkanmu karena hari ini adalah harinya."
    scene expression ("images/episode7/009.webp") with dissolve
    toby "Anda akan menikah?"
    scene expression ("images/episode7/007.webp") with dissolve
    patricia "Bukan hari itu, idiot. Untuk itu saya membutuhkan manusia, dan semua orang yang saya temui di sini sejauh ini terlalu bodoh. Tapi siapa tahu, mungkin itu akan berubah hari ini."
    scene expression ("images/episode7/010.webp") with dissolve
    toby "Dan mengapa itu berubah?"
    scene expression ("images/episode7/011.webp") with dissolve
    patricia "Karena, hari ini adalah hari pertama kuliah saya."

    if emma_break == True:
        scene expression ("images/episode7/010.webp") with dissolve
        toby "Saya masih tidak mengerti mengapa Anda harus membangunkan saya. Ini hari pertama kuliah Anda, bukan milik saya."
        scene expression ("images/episode7/011.webp") with dissolve
        patricia "Karena Anda menjadi baik [brother] akan mengarahkan saya ke sana."
        scene expression ("images/episode7/009.webp") with dissolve
        toby "Ya. Tidak akan terjadi. Selain itu, Anda memiliki lisensi pengemudi."
        scene expression ("images/episode7/008.webp") with dissolve
        patricia "Aku benci mengemudi."
        scene expression ("images/episode7/009.webp") with dissolve
        toby "Dan aku benci bangun lebih awal."
        scene expression ("images/episode7/012.webp") with dissolve
        patricia "Ya. Sayang sekali kamu sudah naik."
        patricia "Aku akan berpakaian. Sampai jumpa di lantai bawah."
        scene expression ("images/episode7/013.webp") with dissolve
        pass
    else:

        scene expression ("images/episode7/014.webp") with dissolve
        toby "Kotoran. Terima kasih telah mengingatkan saya. Saya berjanji Emma saya akan membawanya ke sekolah."
        scene expression ("images/episode7/015.webp") with dissolve
        patricia "Bukan itu sebabnya saya membangunkan Anda. Saya butuh tumpangan. Saya tidak peduli dengan Emma."
        scene expression ("images/episode7/016.webp") with dissolve
        toby "Nah, dalam hal ini Anda harus menemukan diri Anda pacar yang bisa menjemput Anda."
        scene expression ("images/episode7/017.webp") with dissolve
        patricia "Baik ... kami bisa membawanya bersama kami jika Anda berjanji."
        scene expression ("images/episode7/018.webp") with dissolve
        toby "Siapa bilang aku membawamu bersama kami?"
        scene expression ("images/episode7/019.webp") with dissolve
        patricia "Hati Anda yang besar berkata begitu."
        patricia "Aku akan berpakaian. Sampai jumpa di lantai bawah."
        scene expression ("images/episode7/020.webp") with dissolve
        pass

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Damn... She's such a headache{/i}."

    $ progress = 96
    scene expression ("images/episode7/021.webp") with fade

    toby "Pagi, [mom]."

    scene expression ("images/episode7/022.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/023.webp") with dissolve
    charlotte "Pagi madu. Seseorang bangun lebih awal. Tidur nyenyak?"
    scene expression ("images/episode7/024.webp") with dissolve
    toby "Sampai Tris memutuskan untuk membangunkan saya sehingga saya bisa membawanya ke hari pertama sekolahnya."
    scene expression ("images/episode7/025.webp") with dissolve
    charlotte "Oh ... malang kamu."
    scene expression ("images/episode7/026.webp") with dissolve
    charlotte "Kamu lapar? Aku bisa membuatmu makan."
    scene expression ("images/episode7/027.webp") with dissolve
    toby "Tidak terlalu. Jika Anda bisa membuatkan saya kopi yang luar biasa."
    scene expression ("images/episode7/026.webp") with dissolve
    charlotte "Kopi sudah siap. Saya membuat lebih banyak pagi ini."
    scene expression ("images/episode7/027.webp") with dissolve
    toby "Jadi? Bagaimana buku Anda? Saya kira Anda sedang mengerjakannya, kan?"
    scene expression ("images/episode7/028.webp") with dissolve
    charlotte "Saya semakin dekat untuk menyelesaikannya. Semoga dalam satu atau dua minggu itu akan siap."
    scene expression ("images/episode7/027.webp") with dissolve
    toby "Tidak bisa menunggu untuk membacanya."
    scene expression ("images/episode7/029.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode7/030.webp") with dissolve
    toby "Untuk apa itu?"
    charlotte "Karena setelah saya memberi tahu Anda bahwa Anda tidak akan membaca buku saya, Anda akan menyusuri jalan drama yang mengatakan bahwa saya tidak cukup mencintaimu dan semua itu."
    charlotte "Jadi aku memberimu sedikit ciuman untuk menunjukkan betapa aku mencintaimu."
    scene expression ("images/episode7/031_pouty.webp") with dissolve
    toby "Rupanya masih belum cukup."
    scene expression ("images/episode7/032_emotionless.webp") with dissolve
    charlotte "Aduh, terjadi lagi. Saya tidak pernah menyadari bahwa Anda adalah ratu drama seperti itu."
    scene expression ("images/episode7/031_laugh.webp") with dissolve
    toby "Maksudmu raja."
    scene expression ("images/episode7/032_smile.webp") with dissolve
    charlotte "Tidak. Ratu drama. Seorang raja tidak akan pernah menyebalkan tentang hal seperti ini. Ratu lebih menyebalkan."
    scene expression ("images/episode7/031_laugh.webp") with dissolve
    toby "Bahasa Muda Bahasa. Anda beruntung kami tidak memiliki toples bersumpah lagi karena Anda akan bermasalah."
    scene expression ("images/episode7/032_laugh.webp") with dissolve
    charlotte "Apa yang bisa saya katakan. Pengaruh buruk."
    scene expression ("images/episode7/031_curious.webp") with dissolve
    toby "Pengaruh Buruk Apa? Anda selalu pulang dengan saya dan Tris."
    scene expression ("images/episode7/032_smile.webp") with dissolve
    charlotte "Tepat."
    scene expression ("images/episode7/031_smile.webp") with dissolve
    toby "Ya, saya merasakan Anda. Tris adalah pengaruh yang sangat buruk, tetapi tidak mengatakannya dengan keras, dia mungkin mendengarmu."
    scene expression ("images/episode7/031_smile.webp") with dissolve
    toby "Lihat aku jam 7:20 pagi."
    scene expression ("images/episode7/032_laugh.webp") with dissolve
    charlotte "Ya. Dia menghancurkanmu. Beruntung bagi Anda, Anda tidak perlu berbagi kamar lagi dengannya."
    scene expression ("images/episode7/031_laugh.webp") with dissolve
    toby "Tepat. Siapa yang tahu apa yang bisa terjadi jika saya tinggal di sana lagi."
    scene expression ("images/episode7/032_smile.webp") with dissolve
    charlotte "Bagaimana jika dia meyakinkan Anda untuk kuliah. Bayangkan itu."
    scene expression ("images/episode7/031_normal.webp") with dissolve
    toby "Bukan ini lagi. Tolong, [mom]. Ini masih lebih awal."
    toby "Kami telah melakukan percakapan ini. \ 'Anda harus kuliah sehingga Anda bisa mendapatkan pekerjaan yang baik untuk mendapatkan uang yang baik. \' Saya sudah melakukannya."
    scene expression ("images/episode7/032_sad.webp") with dissolve
    if toby_job == 0:
        charlotte "Ya, tetapi bagaimana jika perusahaan bangkrut? Apa yang akan Anda lakukan?"
        scene expression ("images/episode7/031_normal.webp") with dissolve
        toby "Aku akan khawatir tentang itu. Saat ini kuliah hanya akan memengaruhi pekerjaan saya."
        scene expression ("images/episode7/032_sad.webp") with dissolve
        charlotte "Ya, tapi Anda punya cukup waktu untuk bekerja dan kuliah."
    else:
        charlotte "Melakukan siapa yang tahu apa."
        scene expression ("images/episode7/031_normal.webp") with dissolve
        toby "Saya mengelola klub. Saya baru berusia 20 tahun dan sudah mengelola klub."
        scene expression ("images/episode7/032_sad.webp") with dissolve
        charlotte "Ya, tapi bagaimana jika bos Anda memutuskan bahwa Anda tidak cukup baik lagi?"
    scene expression ("images/episode7/031_smile.webp") with dissolve
    toby "Berhenti khawatir. Semuanya akan baik -baik saja. Saya tidak akan mati kelaparan."
    scene expression ("images/episode7/032_laugh.webp") with dissolve
    charlotte "Bagus. Aku akan berhenti mengomelmu sebelum kamu memanggilku seorang nenek lagi."
    scene expression ("images/episode7/031_laugh.webp") with dissolve
    toby "Aku tidak pernah memanggilmu seorang nenek."
    scene expression ("images/episode7/032_pissed.webp") with dissolve
    charlotte "Anda benar. Anda memanggil saya hag tua."
    scene expression ("images/episode7/031_innocent.webp") with dissolve
    toby "Oh, benar. Maaf tentang itu, tetapi Anda datang."
    scene expression ("images/episode7/032_surprised.webp") with dissolve
    charlotte "Tidak! Saya senang Anda selesai merenovasi kamar Anda."
    scene expression ("images/episode7/031_laugh.webp") with dissolve
    if emma_break == True:
        toby "Dan kemudian Anda harus bertanya kepada saya kapan saya akan membawa wanita pulang."
    else:
        toby "Dan kemudian Anda harus bertanya kepada saya ketika saya akan membawa Emma pulang."
    scene expression ("images/episode7/032_laugh.webp") with dissolve
    charlotte "Tentu saja. Saya harus tahu jadi saya tidak akan masuk."
    scene expression ("images/episode7/031_normal.webp") with dissolve
    toby "Ya benar."
    scene expression ("images/episode7/032_smile.webp") with dissolve
    charlotte "Omong-omong. Bagaimana Anda menyukai kamar baru Anda?"
    scene expression ("images/episode7/031_smile.webp") with dissolve
    toby "Sebenarnya, itu cukup bagus. Saya sangat merindukan kamar saya sendiri, tetapi sisi bawahnya adalah bahwa saya tidak memiliki Tris untuk membersihkan setelah saya."
    scene expression ("images/episode7/032_laugh.webp") with dissolve
    charlotte "Anda hidup seperti raja di sana."
    scene expression ("images/episode7/031_laugh.webp") with dissolve
    toby "Kecuali saat dia mendengkur."
    scene expression ("images/episode7/035.webp") with dissolve
    patricia "Saya tidak mendengkur!"
    scene expression ("images/episode7/036.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/037.webp") with dissolve
    charlotte "Ya ampun. Siapa yang ingin Anda kagumi?"
    scene expression ("images/episode7/038.webp") with dissolve
    patricia "Bukan siapa-siapa. Saya ingin berpakaian bagus, sejak di sekolah menengah saya terpaksa memakai seragam jelek itu."
    scene expression ("images/episode7/039.webp") with dissolve
    patricia "Jadi? Apakah kita akan pergi atau Anda masih ingin mengeluh tentang mendengkur saya yang tidak ada?"
    scene expression ("images/episode7/040.webp") with dissolve
    toby "Beberapa malam jika saya mendengarkan dengan cermat saya masih bisa mendengarnya dari loteng."
    scene expression ("images/episode7/039.webp") with dissolve
    patricia "Dan aku masih bisa mencium bau kentutmu."
    scene expression ("images/episode7/041.webp") with dissolve
    charlotte "Kids!"
    scene expression ("images/episode7/042.webp") with dissolve
    toby "Bye, [mom]. Sampai jumpa lagi."
    patricia "Bye, [mom]."
    scene expression ("images/episode7/043.webp") with dissolve
    charlotte "Berhati -hatilah dan cobalah untuk tidak saling membunuh sebelum Anda sampai di sana."

    return

label episode7_monday_collage_road:
    $ progress = 97
    scene expression ("images/episode7/044.webp") with fade
    if emma_break == True:
        toby "Jadi? Apakah Anda siap untuk hari pertama kuliah Anda?"
        patricia "Saya kira kita akan segera mengetahuinya."
        patricia "Sejujurnya, saya sedikit gugup."
        scene expression ("images/episode7/045.webp") with dissolve
        toby "Saya kira itu hanya normal."
        patricia "Seperti Anda tahu."
        toby "Ha ha. Sangat lucu. Setidaknya saya sudah memiliki pekerjaan dan mendapatkan uang, sementara Anda harus menyelesaikan kuliah terlebih dahulu."
        scene expression ("images/episode7/046.webp") with dissolve
        patricia "Sebenarnya tidak juga. Saya bisa bekerja sebagai magang untuk rumah sakit setempat, tetapi hanya jika saya memiliki nilai bagus."
        toby "Saya pikir magang tidak dibayar?"
        patricia "Yah, itu bukan aturan. Saya mendengar bahwa beberapa magang di rumah sakit dibayar."
        scene expression ("images/episode7/047.webp") with dissolve
        toby "Jadi apakah ini berarti Anda mengatur menjadi perawat?"
        patricia "Yup. Saya akan menjadi perawat terbaik."
        toby "Apa pendapat Bea tentang ini?"
        patricia "Dia harus terbiasa dengan gagasan berada di tempat kedua."
        scene expression ("images/episode7/048.webp") with dissolve
        toby "Anda adalah teman yang baik."
        patricia "Saya tahu ... kan?"

        scene expression ("images/episode7/066.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        return
    else:

        toby "Apa yang kamu lakukan di kursi depan? Itu kursi Emma."
        patricia "Ya, ya. Saya tahu, Anda punya pacar yang Anda cintai dan semuanya."
        toby "Jadi? Kenapa kamu duduk di sana?"
        scene expression ("images/episode7/045.webp") with dissolve
        patricia "Wow, kamu sangat menjengkelkan. Saya akan pindah ke belakang begitu kita sampai di tempatnya."
        toby "Baik, Anda bisa duduk di sini sampai saat itu."
        patricia "{size=12}{color=#FDCA6E}* mocking *{/color}{/size}\n{i}FiNe. YoU CaN SiT HeRe UnTiL ThEn.{/i}"
        toby "Bodoh."
        scene expression ("images/episode7/049_texting.webp") with fade
        call sms_sent ("emma", "Hi honey. I'm downstairs.") from _call_sms_sent_60
        call sms_incoming ("emma", "Great. I'll be down in a minute.") from _call_sms_incoming_84
        hide screen message


        scene expression ("images/episode7/050.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        emma "Hey seksi."
        scene expression ("images/episode7/051.webp") with dissolve
        toby "Wow, kamu sangat cantik."
        emma "Terima kasih sayang."

        scene expression ("images/episode7/052.webp") with dissolve
        show ep7_052 with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        hide ep6_005

        toby "Saya masih merasa sulit terbiasa dengan potongan rambut baru Anda, tapi persetan dengan saya, Anda terlihat baik."
        emma "Anda akan membuat saya memerah."
        toby "Sedikit merah di pipi Anda tidak akan menyakitkan."
        scene expression ("images/episode7/053.webp") with dissolve
        emma "Saya suka ketika pipi saya menjadi merah karena Anda memberikannya dengan keras."
        scene expression ("images/episode7/054.webp") with dissolve
        toby "Omong-omong. Saya tidak berpikir Anda telah melihat Tris sebentar lagi."
        scene expression ("images/episode7/055.webp") with dissolve
        patricia "Hai Emma."
        scene expression ("images/episode7/056.webp") with dissolve
        emma "Hai Tris. Maaf tentang itu. Saya tidak tahu Anda ada di dalam mobil."
        scene expression ("images/episode7/057.webp") with dissolve
        patricia "Astaga. Saya suka rambutnya. Itu terlihat sangat bagus untukmu."
        scene expression ("images/episode7/058.webp") with dissolve
        emma "Kamu benar -benar berpikir begitu? Terima kasih. Dan saya suka make up Anda. Saya tidak tahu siapa yang melakukannya, tetapi cantik sekali."
        scene expression ("images/episode7/059.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Jesus...Women are so fake. I know for a fact that they hate each other and yet they still talk like they are best friends.{/i}"
        scene expression ("images/episode7/060.webp") with dissolve
        toby "Jadi, apakah kalian siap untuk hari pertama kuliah?"
        scene expression ("images/episode7/061.webp") with dissolve
        emma "Anda tidak tahu. Saya tidak sabar untuk memulai."
        scene expression ("images/episode7/062.webp") with dissolve
        patricia "Di sisi lain saya tidak begitu bersemangat."
        scene expression ("images/episode7/063.webp") with dissolve
        emma "Apa jurusan Anda?"
        scene expression ("images/episode7/062.webp") with dissolve
        patricia "Perawatan."
        scene expression ("images/episode7/063.webp") with dissolve
        emma "Itu sangat bagus."
        scene expression ("images/episode7/064.webp") with dissolve
        patricia "Bagaimana denganmu?"
        scene expression ("images/episode7/063.webp") with dissolve
        emma "Psikologi, Klinis & Konseling."
        scene expression ("images/episode7/065.webp") with dissolve
        toby "Keduanya berada di area yang sama? Jadi saya kira Anda akan memiliki beberapa subjek bersama."
        scene expression ("images/episode7/061.webp") with dissolve
        emma "Ya dan tidak. Saya lebih tentang sisi ilmu sosial saat menyusui lebih banyak ilmu kesehatan."
        scene expression ("images/episode7/064.webp") with dissolve
        patricia "Tapi kami masih memiliki beberapa subjek bersama."
        scene expression ("images/episode7/065.webp") with dissolve
        toby "Itu bagus. Setidaknya Anda akan mengenal seseorang."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This is not going to end well.{/i}"

        scene expression ("images/episode7/067.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        return

label episode7_monday_college:
    $ progress = 98
    if emma_break == True:
        scene expression ("images/episode7/068.webp") with fade
        toby "Saya pikir ini dia."
        patricia "Terima kasih, [toby!c]."
        toby "Bersikaplah baik dan bersenang -senang."
        scene expression ("images/episode7/069.webp") with dissolve
        patricia "Sekarang, sekarang. Jangan menjadi sentimental pada saya. Ini tidak seperti saya \ 'm pindah. Aku akan kembali malam ini."
        toby "Siapa bilang saya menjadi sentimental. Saya baru saja memberi Anda nasihat dan Anda mulai memeluk saya."
        scene expression ("images/episode7/070.webp") with dissolve
        patricia "Aku? Anda orang yang meraih saya."
        patricia "Sekarang biarkan aku pergi, sebelum beberapa pria seksi melihatku bersamamu dan berpikir aku adalah pacarmu."
        scene expression ("images/episode7/071.webp") with dissolve
        if toby_job == 0:
            toby "Beberapa pria menyukai tantangan dan Anda memiliki pacar mungkin satu."
            scene expression ("images/episode7/072.webp") with dissolve
            patricia "Orang -orang itu disebut pemain dan saya untuk satu, tidak menyukai mereka."
            scene expression ("images/episode7/071.webp") with dissolve
            toby "Itulah mengapa Anda sangat menyukai saya?"
            scene expression ("images/episode7/073.webp") with dissolve
            patricia "Saya tidak. Saya tahu Anda seorang pemain."
            scene expression ("images/episode7/074.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Does she really think I'm a player?{/i}"
        else:

            toby "Tidak ada orang waras yang akan berpikir saya akan berkencan dengan Anda. Lihat aku sangat keren, dan kamu ... yah, tidak terlalu keren."
            scene expression ("images/episode7/072.webp") with dissolve
            patricia "Mungkin tidak begitu keren, tapi seksi."
            scene expression ("images/episode7/071.webp") with dissolve
            toby "Ya ampun. Seseorang penuh dengan dirinya sendiri."
            scene expression ("images/episode7/073.webp") with dissolve
            patricia "Anda tidak dapat menyangkalnya."

            scene expression ("images/episode7/074.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's so full of herself. You can almost tell she's my younger [sister].{/i}"

        scene expression ("images/episode7/075.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit. Is that Emma?{/i}"


        scene expression ("images/episode7/076.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She changed her hair. My God she looks good.{/i}"
        scene expression ("images/episode7/077.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's looking right at me. Maybe I should go say hi?{/i}"
        scene expression ("images/episode7/078.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I guess I have my answer, but hell she looks good.{/i}"
        scene expression ("images/episode7/079.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe I shouldn't have broken up with her.{/i}"
        scene expression ("images/episode7/080.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Nope... I can't go there. We broke up. It's better this way.{/i}"
    else:

        scene expression ("images/episode7/081.webp") with dissolve
        toby "Di sini kami berada di perguruan tinggi Anda."
        scene expression ("images/episode7/082.webp") with dissolve
        patricia "Astaga. Ini sangat besar."
        scene expression ("images/episode7/083.webp") with dissolve
        emma "Anda tidak tahu berapa kali saya mengatakan itu."
        scene expression ("images/episode7/084.webp") with dissolve
        patricia "Anda pernah ke perguruan tinggi ini sebelumnya?"
        scene expression ("images/episode7/085.webp") with dissolve
        toby "Anda harus pergi sekarang, saya pikir kelas sudah dimulai."
        scene expression ("images/episode7/086.webp") with dissolve
        patricia "Belum ada kelas apa pun. Anda tidak tahu bagaimana kuliah bekerja."
        emma "Ya. Anda sangat buruk dalam hal ini."
        scene expression ("images/episode7/087.webp") with dissolve
        emma "Ayo Tris. Lepaskan."
        scene expression ("images/episode7/088.webp") with dissolve
        $ ep7_monday_date = "emma"

        toby "Ngomong -ngomong, jangan membuat rencana untuk malam ini. Kami pergi untuk merayakan hari pertama sekolah Anda!"
        scene expression ("images/episode7/087.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe my mind is playing tricks on me, but it's almost like they are getting along. It would be nice to have the most important women in my life getting along.{/i}"
        scene expression ("images/episode7/089.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}The most important and the hottest women in my life.{/i}"
        scene expression ("images/episode7/080.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Nope. I'm not going there. I'm not going to stare at their asses. Tris is my younger [sister].{/i}"

    if lisa_path:
        scene expression ("images/episode7/090.webp") with shake
        lisa "Sayang hati -hati. Anda mungkin mematahkan kaki saya dan kemudian Anda harus membawa saya berkeliling."
        scene expression ("images/episode7/091.webp") with dissolve
        toby "Oh. Halo. Maaf jika ... saya tidak melihat Anda."
        scene expression ("images/episode7/093.webp") with dissolve
        lisa "Itu aneh mengingat fakta bahwa Anda mengatakan Anda hanya memiliki mata untuk saya."
        scene expression ("images/episode7/094.webp") with dissolve
        toby "Saya menurunkan [sister] saya dan memastikan dia baik -baik saja."
        scene expression ("images/episode7/095.webp") with dissolve
        lauren "Pria yang begitu peduli. Sudah kubilang dia penjaga."
        scene expression ("images/episode7/094.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yeah... You have no idea.{/i}"
        if emma_break:
            $ ep7_monday_date = "lisa"
            toby "Jadi, apakah Anda bebas berkencan dengan penjaga malam ini?"
            scene expression ("images/episode7/093.webp") with dissolve
            lisa "Saya ingin sekali."
        else:
            $ ep7_tuesday_date = "lisa"
            toby "Jadi, apakah Anda bebas berkencan dengan penjaga besok?"
            scene expression ("images/episode7/093.webp") with dissolve
            lisa "Saya lebih suka kita keluar malam ini, tetapi jika Anda hanya bisa besok, saya tidak punya banyak pilihan. Kami akan melakukannya besok."

        scene expression ("images/episode7/098.webp") with dissolve
        toby "Saya akan membiarkan Anda menjelajahi kampus. Sampai jumpa."
        scene expression ("images/episode7/099.webp") with dissolve
        lisa "Sampai jumpa."
        lauren "Bye [toby!c]."


    elif lauren_path:
        scene expression ("images/episode7/090.webp") with shake
        lauren "Hati -hati seksi. Kami berada di tempat umum. Tunggu sampai malam ini."
        scene expression ("images/episode7/091.webp") with dissolve
        toby "Oh. Hai, yang di sana. Aku tidak melihatmu."
        scene expression ("images/episode7/096.webp") with dissolve
        lauren "Mari kita lihat. SIAPA YANG ANDA MEMBERIKAN?"
        scene expression ("images/episode7/094.webp") with dissolve
        toby "Tidak ada seorang pun. Saya baru saja menurunkan [sister] saya dan memastikan dia baik -baik saja."
        scene expression ("images/episode7/097.webp") with dissolve
        lauren "Itu sangat bagus."

        if emma_break:
            $ ep7_monday_date = "lauren"
            scene expression ("images/episode7/094.webp") with dissolve
            toby "Bagaimanapun. Anda menyebutkan sesuatu tentang malam ini. Jam berapa saya harus datang menjemput Anda."
            scene expression ("images/episode7/097.webp") with dissolve
            lauren "Secepat mungkin."
            scene expression ("images/episode7/094.webp") with dissolve
            toby "Tujuh?"
            scene expression ("images/episode7/097.webp") with dissolve
            lauren "Jika Anda tidak dapat tujuh lebih awal."
        else:
            $ ep7_tuesday_date = "lauren"
            toby "Bagaimanapun. Anda menyebutkan sesuatu tentang malam ini, sayangnya saya tidak bisa, tapi mungkin besok?"
            scene expression ("images/episode7/097.webp") with dissolve
            lauren "Baik, saya akan menjaga hormon saya tetap terkendali sampai besok."

        scene expression ("images/episode7/098.webp") with dissolve
        toby "Saya akan membiarkan Anda menjelajahi kampus. Sampai jumpa."
        scene expression ("images/episode7/099.webp") with dissolve
        lauren "Sampai jumpa seksi."
        lisa "Nanti, [toby!c]."
    else:

        scene expression ("images/episode7/100.webp") with shake
        if lisa_rel > 0:
            lisa "[toby!c]! Perhatikan kemana Anda pergi!"
        else:
            lauren "Hati -hati, [toby!c]! Anda memiliki kesempatan."

        scene expression ("images/episode7/091.webp") with dissolve
        toby "Maaf nona. Saya tidak bermaksud."

        if lisa_rel > 0:
            scene expression ("images/episode7/101_1.webp") with dissolve
            lisa "Berhati -hatilah lain kali."
        else:
            scene expression ("images/episode7/101_2.webp") with dissolve
            lauren "Itulah yang terjadi saat Anda memeriksa pelacur."

        scene expression ("images/episode7/102.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I guess I deserve the cold response.{/i}"

    return

label episode7_monday_back_home:
    $ progress = 99
    stop music fadeout 2.0
    scene expression ("images/episode7/103.webp") with fade
    if toby_job == 0:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should get ready for work. Mrs. Darlene told me that I have to take care of an apartment that is being renovated.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should get ready for work. Mrs. Katrina told me I have to deliver something.{/i}"

    scene expression ("images/episode7/104.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'll go let [mom] know I'm leaving for work.{/i}"
    scene expression ("images/episode7/105.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Nope. She's not here. Maybe she's taking a shower.{/i}"
    scene expression ("images/episode7/106.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think I see her outside. She must be tanning.{/i}"
    scene expression ("images/episode7/107.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit. She's topless.{/i}"

    menu:
        "{i} [JGR] Lihat lebih baik {/i}":
            scene expression ("images/episode7/108.webp") with dissolve:
                xalign 1.0
                linear 10.0 xalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()


            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}[mom!c]'s looking so good.{/i}"

            scene expression ("images/episode7/109.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Especially her boobs. They are so firm and her nipples are so beautiful.{/i}"
            scene expression ("images/episode7/110.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Actually she's is quite beautiful all around, not just her boobs.{/i}"
            scene expression ("images/episode7/111.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I really should stop looking. She's my [mom] for fuck sake.{/i}"
        "Saya seharusnya tidak melihat. Lagipula dia [mom] saya.":

            scene expression ("images/episode7/111.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yeah. Better this way.{/i}"

    scene expression ("images/episode7/112.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Wait a minute... Is that her laptop? I'm really curious to see what's going on with her book.{/i}"
    scene expression ("images/episode7/113.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see where we were.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think I left off on chapter two. So far the main character was obsessed with the waiter. She managed to convince her husband to go there every other day, just so she'd see the waiter.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see what's going on.{/i}"

    scene expression ("images/episode7/114.webp") with fade
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I don't know what to do. I can't stop thinking about him.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I shouldn't have these kind of fantasies first of all.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I can't. I'm a married woman.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I mean. I shouldn't.{/i}"
    scene expression ("images/episode7/115.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}No way in hell I'm taking you there.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}You'll do something stupid.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Promise?{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Fine, but if you do something stupid I'm not talking to you ever again.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Bye, Esined. See you then.{/i}"

    scene expression ("images/episode7/113.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}[mom!c] really needs to step up her naming game. Esined is [aunt] Denise's name backwards.{/i}"
    scene expression ("images/episode7/116.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's jump to the date, before [mom] catches me reading her book.{/i}"

    scene expression ("images/episode7/117.webp") with fade
    denise_ "Jadi? Siapa pelayannya?"
    scene expression ("images/episode7/118.webp") with dissolve
    charlotte_ "Aku tidak memberitahumu apa pun. Membawa Anda ke sini adalah kesalahan."
    scene expression ("images/episode7/119.webp") with dissolve
    denise_ "Oke. Jangan bilang padaku. Ini tidak seperti saya tidak tahu tipe Anda."
    denise_ "Mari kita lihat."
    denise_ "Tidak. Terlalu botak dan tua."
    scene expression ("images/episode7/120.webp") with dissolve
    denise_ "Terlalu gemuk."
    scene expression ("images/episode7/121.webp") with dissolve
    denise_ "Nah, halo. Biarkan saya melihat apakah saya ingat tipe Anda."
    scene expression ("images/episode7/122.webp") with dissolve
    denise_ "Rambut gelap, mata cokelat, tinggi dan tidak terlalu kurus, tidak terlalu berotot. Saya hanya perlu melihat senyumnya dan kemudian saya akan mengonfirmasi."
    scene expression ("images/episode7/123.webp") with dissolve
    waiter "Selamat malam wanita."
    waiter "Tampaknya Anda orang yang menikmati makanan kami. Saya tidak yakin apakah Anda atau suami Anda ingin datang begitu sering, tetapi sekarang saya pikir saya tahu jawabannya."
    scene expression ("images/episode7/124.webp") with dissolve
    denise_ "Ya. Dia menyukai segalanya di sini. Segala sesuatu di menu dan mati."
    scene expression ("images/episode7/125.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yeah... It was a big mistake bringing her here.{/i}"
    scene expression ("images/episode7/126.webp") with dissolve
    waiter "Ya. Kami memiliki lampu gantung yang sangat bagus."
    waiter "Jadi? Apa yang bisa saya dapatkan untuk Anda para wanita?"
    scene expression ("images/episode7/116.webp") with dissolve
    waiter "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's skip this part. [mom!c] could be done any minute.{/i}"
    scene expression ("images/episode7/113.webp") with dissolve
    waiter "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}They're talking about the waiter. He's hot, cute. Blah, blah, blah...{/i}"
    waiter "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Interesting.{/i}"
    scene expression ("images/episode7/127.webp") with dissolve
    charlotte_ "Apa yang sedang kamu lakukan?"
    scene expression ("images/episode7/128.webp") with dissolve
    denise_ "Karena Anda tidak akan bergerak padanya, saya mungkin. Sayang sekali tidak."
    scene expression ("images/episode7/127.webp") with dissolve
    charlotte_ "Anda benar -benar menyebalkan. Anda tahu bahwa saya menyukainya."
    scene expression ("images/episode7/128.webp") with dissolve
    denise_ "Tapi Anda sudah menikah dan terlalu takut untuk menipu suami Anda dan saya tidak punya satu, jadi tidak ada salahnya tidak melakukan pelanggaran."
    scene expression ("images/episode7/129.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode7/130.webp") with dissolve
    charlotte_ "Ayo, biarkan pergi, sebelum Anda berhubungan seks dengannya di depan saya."
    denise_ "Anda ingin melihat ukuran kemaluannya, kan?"
    charlotte_ "Jalang!"
    scene expression ("images/episode7/113.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}[aunt!c] Denise is fun. I wonder if that's how she was back when they were young or this is just [mom]'s imagination.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's continue.{/i}"

    scene expression ("images/episode7/131.webp") with fade
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why does she have to be like that? She knows that I like him. It's not like I care who he's dating.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But she's my [sister]. At least she could have the decency to go after for someone else.{/i}"

    scene expression ("images/episode7/132.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I just got a message.{/i}"

    scene expression ("images/episode7/133.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wonder who this is.{/i}"
    scene expression ("images/episode7/133_texting.webp") with dissolve
    call sms_incoming ("unknown", "Hello. Your friend left this phone number on a napkin. I've been fighting with the idea of texting you for over an hour. I know you're married so I don't want to cause any problems.") from _call_sms_incoming_85
    hide screen message
    scene expression ("images/episode7/134.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit, shit, shit. She gave him my number?{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What should I do? Should I write him back. I can't. I'm a married woman.{/i}"
    scene expression ("images/episode7/135.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe I should tell him that this was a joke.{/i}"
    scene expression ("images/episode7/133.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit. Another message.{/i}"
    scene expression ("images/episode7/133_texting.webp") with dissolve
    call sms_incoming ("unknown", "All I wanted to say is that I loved your dress.") from _call_sms_incoming_86
    hide screen message
    scene expression ("images/episode7/135.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Oh my God. What I'm going to do now?{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe just a simple \"Thank you\". Tidak ada emoji, tidak ada apa -apa. Saya tidak ingin terdengar terlalu genit. Saya tidak tertarik untuk menghancurkan pernikahan saya. {/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Or don't say anything back, and he'll understand?{/i}"
    scene expression ("images/episode7/133.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Another message.{/i}"
    scene expression ("images/episode7/133_texting.webp") with dissolve
    call sms_incoming ("unknown", "Have a good night and I hope I didn't cause any problems.") from _call_sms_incoming_87
    hide screen message
    scene expression ("images/episode7/135.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I can't leave him hanging. I'll just say \"Thank you. Have a good night to you too.\"{/i}"
    scene expression ("images/episode7/133_texting.webp") with dissolve
    call sms_sent ("unknown", "Thank you. Have a good night to you too. :)") from _call_sms_sent_61
    hide screen message
    scene expression ("images/episode7/136.webp") with dissolve
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why did I add the smiley face at the end? I'm so bad at this.{/i}"
    charlotte_ "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}That's it. I'm going to delete the number. I'm a married woman.{/i}"
    scene expression ("images/episode7/116.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit. [mom!c] is coming!{/i}"
    scene expression ("images/episode7/137.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I need to close the laptop fast!{/i}"

    scene expression ("images/episode7/138.webp") with dissolve
    charlotte "Oh. Anda sudah kembali?"
    scene expression ("images/episode7/139.webp") with dissolve
    toby "Ya. Aku hanya mencarimu. Saya akan bekerja."
    scene expression ("images/episode7/138.webp") with dissolve
    charlotte "Saya suka bahwa Anda masih memberi tahu saya ke mana Anda pergi meskipun Anda sudah dewasa."
    scene expression ("images/episode7/139.webp") with dissolve
    toby "Umm ... Saya tidak pernah memikirkannya seperti itu. Rasanya normal dan selain itu, tidak seperti Anda akan menghentikan saya."
    scene expression ("images/episode7/140.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode7/141.webp") with dissolve
    toby "Sampai jumpa nanti malam."

    return

label episode7_monday_realEstate:
    $ progress = 100
    stop music fadeout 2.0
    scene expression ("images/episode7/142.webp") with fade
    if emma_break:
        toby "Pagi. Maaf saya terlambat. [sister] saya mulai kuliah hari ini dan saya harus membawanya."
    else:
        toby "Pagi. Maaf saya terlambat. Saya harus membawa pacar saya ke hari pertama kuliahnya."

    scene expression ("images/episode7/143.webp") with dissolve
    darlene "Jangan khawatir. Jadi? Bagaimana kuliahnya? Apakah dia menyukainya?"
    scene expression ("images/episode7/142.webp") with dissolve
    toby "Saya harap begitu. Saya tidak yakin. Aku akan memberitahumu setelah minggu pertama."
    scene expression ("images/episode7/143.webp") with dissolve
    darlene "Ya, Anda benar."
    scene expression ("images/episode7/144.webp") with dissolve
    darlene "Bagaimanapun. Inilah kontrak yang saya miliki dengan tim konstruksi. Pekerjaan itu seharusnya dilakukan 3 minggu yang lalu."
    darlene "Pergi ke sana dan bersikap memerintah.Juga di sini adalah daftar semua pembayaran saya. Yang terakhir adalah tiga minggu yang lalu, seperti kami setuju. Saya menahan tawaran saya."
    scene expression ("images/episode7/145_1.webp") with dissolve
    toby "Mengapa kami tidak pergi ke sana dengan seorang pengacara. Saya yakin kita akan memenangkan kasus ini."
    scene expression ("images/episode7/145_2.webp") with dissolve
    darlene "Anda hanya perlu mengintimidasi pekerja. Mereka hanya perlu merenovasi apartemen. Pekerjaan itu terlalu kecil untuk menjadi masalah."
    scene expression ("images/episode7/145_1.webp") with dissolve
    toby "Saya mengerti."
    scene expression ("images/episode7/145_2.webp") with dissolve
    darlene "Bagaimanapun, mandor itu Gregory. Anda harus berbicara dengannya."
    scene expression ("images/episode7/146.webp") with dissolve
    toby "Ada lagi?"
    darlene "Saya mengadakan pertemuan sore ini, jadi ketika Anda kembali, saya mungkin tidak akan berada di sini. Lanjutkan perburuan Anda untuk apartemen di dekat Stasiun Bridingval."
    scene expression ("images/episode7/147.webp") with dissolve
    toby "Akan melakukannya."
    darlene "Dan supaya Anda tahu, semua bangunan itu disewa oleh Kat. Jadi cobalah untuk tidak membuat orang marah kecuali untuk kontraktor."


    scene expression ("images/episode7/148.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/149.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This must be the building. Let's see, Darlene said that the apartment we're renovating is number 7.{/i}"
    scene expression ("images/episode7/150.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}So, let's see where apartment 7 is.{/i}"
    woman "Apakah Anda mencari sesuatu?"
    scene expression ("images/episode7/151.webp") with dissolve
    toby "Halo. Ya. Saya mencari apartemen 7."

    scene expression ("images/episode7/152.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    $ progress = 101

    woman "..."
    scene expression ("images/episode7/153.webp") with dissolve
    woman "Saya berkata, ikuti saya. Saya pergi ke apartemen 8."
    scene expression ("images/episode7/154.webp") with dissolve
    toby "Maaf, saya memiliki kepala di awan. Banyak di pikiran saya."
    scene expression ("images/episode7/153.webp") with dissolve
    woman "Saya yakin."
    scene expression ("images/episode7/155.webp") with dissolve
    toby "Biarkan saya membantu Anda dengan itu."
    woman "Anda sangat baik."
    scene expression ("images/episode7/156.webp") with dissolve
    woman "Jadi bisnis apa yang Anda miliki di sini?"
    toby "Perusahaan yang bekerja untuk memiliki gedung dan bos saya mengirim saya untuk melihat apa yang butuh waktu lama bagi sebuah apartemen yang akan direnovasi."
    woman "Karena selama 4 minggu terakhir hanya ada satu pekerja yang muncul setiap hari, tetapi Anda tidak mendengarnya dari saya."
    scene expression ("images/episode7/157.webp") with dissolve
    toby "Itu bagus untuk diketahui. Terima kasih atas infonya."
    woman "Dengan senang hati. Semakin cepat mereka meninggalkan lebih cepat saya akhirnya bisa istirahat."
    toby "Anda bekerja di shift malam?"
    woman "Anda bisa mengatakan itu."
    scene expression ("images/episode7/158.webp") with dissolve
    woman "Nah, ini aku. Terima kasih atas bantuannya. Apartemen yang Anda cari adalah di sebelah yang satu ini."
    toby "Terima kasih dan saya akan melihat apa yang bisa saya lakukan."
    woman "Sampai jumpa!"
    scene expression ("images/episode7/159.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Now let's see what's going on here.{/i}"
    scene expression ("images/episode7/160.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I don't know what she was complaining about, it's very quiet for a construction site.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should enter quietly, so I can see what's going on.{/i}"

    scene expression ("images/episode7/161.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Looks like nobody is here. Let's check the other room.{/i}"
    scene expression ("images/episode7/162.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the fuck is he doing there.{/i}"


    scene expression ("images/episode7/163.webp") with dissolve
    toby "Saya tidak berpikir itu yang Anda bayar."
    scene expression ("images/episode7/164.webp") with dissolve
    worker "Siapa kamu? Apa yang kamu lakukan di sini? Ini adalah properti pribadi."
    scene expression ("images/episode7/163.webp") with dissolve
    toby "Aku tahu. Perusahaan kami membayar Anda untuk menyelesaikan ini. Dimana semuanya?"
    scene expression ("images/episode7/166.webp") with dissolve
    worker "Saya hanya menjawab Nyonya Darlene. Jadi berhentilah membuang -buang waktu saya."
    scene expression ("images/episode7/165.webp") with dissolve
    toby "Anda berbicara dengan saya.Buang waktu Anda? Buang waktu Anda melakukan apa? Dengarkan di sini."
    toby "Dimana Gregory?"
    scene expression ("images/episode7/166.webp") with dissolve
    gregory "Tepat di depanmu."
    scene expression ("images/episode7/165.webp") with dissolve
    toby "Kami memegang bagian dari kesepakatan kami. Kami menjaga jadwal pembayaran, namun apartemen jelas masih belum selesai.Besar. Aku akan bertanya lagi padamu lagi. Dimana semua orang."
    scene expression ("images/episode7/166.webp") with dissolve
    gregory "Para kru sedang istirahat makan siang. Lihat anak. Mengapa Anda tidak kembali ke atasan Anda dan mengatakan kepadanya bahwa kami memiliki beberapa masalah dan itu akan memakan waktu lebih lama lagi."
    scene expression ("images/episode7/165.webp") with dissolve
    toby "Anda seharusnya memikirkan hal itu sebelum menandatangani.Saya tidak peduli dengan masalah Anda. Perusahaan Anda menandatangani kontrak. Bukan masalah saya masalah apa yang Anda temui."
    scene expression ("images/episode7/167.webp") with dissolve
    gregory "Berapa usiamu? 18? Anda tidak tahu betapa sulitnya pekerjaan ini."
    scene expression ("images/episode7/168.webp") with dissolve
    toby "Pertama -tama usia saya bukanlah perhatian Anda. Kedua, jangan letakkan tanganmu padaku."
    toby "Saya datang ke sini untuk memberi tahu Anda bahwa jika pekerjaan itu tidak dilakukan pada akhir minggu ini kami akan menuntut Anda. Pagi ini Darlene sangat kesal sehingga dia memanggil pengacaranya tentang ini."
    toby "Anda akan dituntut karena harga pekerjaan dikalikan dengan 3 untuk setiap minggu Anda tertunda. Saya adalah orang yang meyakinkannya untuk menunggu sampai akhir minggu."
    toby "Jadi, jika Anda akan berbicara dengan saya, hanya karena saya lebih muda, ingatlah bahwa saya adalah coo dari perusahaan, dan saya tidak akan mentolerir rasa tidak hormat."
    scene expression ("images/episode7/169.webp") with dissolve
    toby "Jadi saya tidak mengenal Anda atau pengacara apa yang Anda mampu, tetapi saya dapat meyakinkan Anda bahwa pengacara kami tidak pernah kehilangan kasus."
    toby "Anda mengatakan bahwa pekerja Anda sedang istirahat makan siang. Satu -satunya pekerjaan saya untuk hari ini adalah ini, jadi saya punya waktu untuk menunggu mereka. Jadi, jika Anda berbohong, saya sarankan Anda pergi menelepon siapa pun yang Anda inginkan dan mendapatkannya di sini."
    toby "Pada akhir minggu saya ingin pekerjaan ini selesai."
    scene expression ("images/episode7/170.webp") with dissolve
    gregory "Lihat, kami mulai dengan kaki yang salah. Anda tidak perlu berkeliaran di sini. Kami akan selesai pada akhir minggu. Saya hanya harus menunggu tim saya kembali dari istirahat makan siang."
    scene expression ("images/episode7/169.webp") with dissolve
    toby "Saya bilang saya akan menunggu di sini. Ini adalah properti kami sehingga saya dapat melakukan apa pun yang saya inginkan di sini dan jika saya ingin tinggal di sini sampai semua orang kembali dari makan siang, saya akan tinggal."
    toby "Tetapi jika tidak ada yang datang ke sini saya akan memanggil pengacara itu sendiri."
    scene expression ("images/episode7/170.webp") with dissolve
    gregory "Aku akan memanggil orang -orang untuk kembali dari istirahat makan siang mereka."
    scene expression ("images/episode7/171.webp") with dissolve
    toby "Ya. Lakukan itu!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It's nice to be bad sometimes. I feel so cool.{/i}"
    scene expression ("images/episode7/172.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm curious what he was looking at.{/i}"
    scene expression ("images/episode7/173.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}There is a hole directly to that woman's apartment.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit. She's changing.{/i}"
    menu:
        "{i} [JGR] Tetap mencari {/i}"(csq="Gambar galeri"):
            scene expression ("images/episode7/174.webp") with dissolve
            $ ep7_peep = True
            $ ui.saybehavior()
            $ ui.interact()
            $ unlockImage(persistent.kayla_01)
            scene expression ("images/episode7/175.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I can see why he sent everybody away. She's looking good.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should stop before he sees me.{/i}"
            pass
        "Saya seharusnya tidak. Itu bukan moral.":
            pass

    scene expression ("images/episode7/176_1.webp") with dissolve
    toby "Jadi? Apakah semua orang kembali?"
    scene expression ("images/episode7/176_2.webp") with dissolve
    gregory "Ya."
    scene expression ("images/episode7/176_1.webp") with dissolve
    toby "Aku juga akan mengobrol dengan wanita di sebelah dan aku yakin dia ingin mengajukan tuntutan begitu dia tahu kamu sudah mengintipnya. Saya pribadi akan menutupi biaya biaya hukumnya.Biarkan saya menjadi jelas. Anda memiliki sampai hari Jumat untuk menyelesaikannya. Jika pekerjaan tidak selesai, kami akan melihat Anda di pengadilan."
    scene expression ("images/episode7/177.webp") with dissolve
    toby "Tutupi lubang itu hari ini."
    gregory "Lubang apa."
    toby "Jangan bermain bodoh dengan saya. Saya memiliki hari yang panjang."

    scene expression ("images/episode7/178.webp") with dissolve
    if ep7_peep:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What a pervert, but I do understand him. That woman is gorgeous.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What a pervert.{/i}"

    scene expression ("images/episode7/179.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see if I can find any decent properties for sale.{/i}"

    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode7/180.webp") with dissolve
    hide screen ui_message

    if ep7_monday_date:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I need to go take a shower before going on my date.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should go home now.{/i}"

    return

label episode7_monday_club:
    $ progress = 100
    stop music fadeout 2.0
    scene expression ("images/episode7/181.webp") with dissolve
    toby "Pagi."
    scene expression ("images/episode7/182.webp") with dissolve
    katrina "Saya ingat mengatakan kepada Anda untuk berada di sini pada jam 10 o \ '. Hampir 11."
    scene expression ("images/episode7/181.webp") with dissolve
    toby "Saya akan meminta maaf, tetapi saya ingat dengan baik bahwa Anda mengajari saya tidak akan meminta maaf ketika saya melakukan sesuatu yang menguntungkan saya."
    scene expression ("images/episode7/183.webp") with dissolve
    katrina "Dan apa yang telah Anda lakukan yang menguntungkan Anda?"
    scene expression ("images/episode7/184.webp") with dissolve
    if emma_break:
        toby "Saya membawa [sister] saya ke sekolah. Jika saya tidak, [mom] saya akan benar -benar kesal dan demi kewarasan saya, saya tidak ingin dimarahi."
        katrina "Kita masih perlu memperbaiki bagian yang memarahi. Apa kamu, 12?"
        toby "Mari kita katakan bahwa terkadang cinta dan hormat membuat Anda melakukan hal -hal aneh."
    else:
        toby "Saya membawa pacar saya ke sekolah sehingga setiap pria yang ingin mengetuk pantatnya akan tahu dia tidak tersedia. Itu, dan saya benar -benar ingin blowjob malam ini, jadi saya harus membawanya."
        katrina "Jenis blowjob apa yang akan dia berikan malam ini?"
        toby "Jenis yang ceroboh dengan sedikit kedalaman."
        katrina "Itu adalah alasan yang sangat bagus untuk terlambat."
    scene expression ("images/episode7/185.webp") with dissolve
    toby "Jadi? Apa pekerjaan saya hari ini? Siapa yang harus saya intimidasi?"
    scene expression ("images/episode7/186.webp") with dissolve
    katrina "Anda belum terlihat sangat menakutkan. Saya punya neal untuk itu. Kamu sayangku, punya paket untuk dikirim."
    scene expression ("images/episode7/185.webp") with dissolve
    toby "Jadi saya masih seorang tugas."
    scene expression ("images/episode7/187.webp") with dissolve
    katrina "Jangan khawatir, aku akan memberitahunya untuk membuatnya layak dikendarai."
    scene expression ("images/episode7/185.webp") with dissolve
    toby "Dia? Jadi saya harus mengirimkan paket kepada seorang wanita?"
    scene expression ("images/episode7/187.webp") with dissolve
    katrina "Wanita yang sangat seksi."
    if emma_break:
        scene expression ("images/episode7/185.webp") with dissolve
        toby "Seberapa panas?"
        scene expression ("images/episode7/187.webp") with dissolve
        katrina "Saya akan membiarkan Anda memutuskan sendiri."
    else:
        scene expression ("images/episode7/185.webp") with dissolve
        toby "Apakah Anda tidak mendengar apa yang saya katakan tentang saya punya pacar dan semuanya?"
        scene expression ("images/episode7/187.webp") with dissolve
        katrina "Haruskah saya memberitahunya untuk tidak memberi Anda pertunjukan?"
        scene expression ("images/episode7/185.webp") with dissolve
        toby "Sebenarnya, saya akan memutuskan sendiri ketika saya melihatnya."
        scene expression ("images/episode7/187.webp") with dissolve
        katrina "Itu anakku!"
        scene expression ("images/episode7/185.webp") with dissolve
        toby "Segera menjadi pria Anda."
        scene expression ("images/episode7/186.webp") with dissolve
        katrina "Apa yang telah saya lakukan untuk Anda. Anda menjadi sangat sombong."
    scene expression ("images/episode7/188.webp") with dissolve
    toby "Jadi ini paketnya?"
    scene expression ("images/episode7/189.webp") with dissolve
    katrina "Yup. Alamatnya ada di belakang. Apartemennya adalah nomor 8."
    scene expression ("images/episode7/188.webp") with dissolve
    toby "Haruskah saya kembali begitu saya mengirimkan ini?"
    scene expression ("images/episode7/189.webp") with dissolve
    katrina "Tentu saja Anda kembali. Tugas Anda adalah mengawasi klub."
    scene expression ("images/episode7/188.webp") with dissolve
    toby "Tidak ada yang akan berada di sini hari ini. Ini hari Senin."
    scene expression ("images/episode7/189.webp") with dissolve
    katrina "Bagaimana jika saya kesepian?"
    scene expression ("images/episode7/190.webp") with dissolve
    toby "Oke bos. Sampai jumpa lagi."


    scene expression ("images/episode7/191.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/192.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I guess this is it.{/i}"
    scene expression ("images/episode7/193.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Now let's see. Where is apartment 8?{/i}"
    woman "Apakah Anda mencari sesuatu?"
    scene expression ("images/episode7/194.webp") with dissolve
    toby "Hai. Ya. Saya mencari apartemen 8."
    $ progress = 101
    scene expression ("images/episode7/195.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    woman "Anda harus [toby!c]."
    menu:
        "{i} [JGR] Pendekatan genit {/i}"(csq="Jalur Kayla terbuka"):
            $ renpy.notify("Kayla's path opened!")
            $ kayla_path = True
            scene expression ("images/episode7/196.webp") with dissolve
            toby "Dan Anda harus menjadi wanita seksi yang disebutkan Katrina."
            scene expression ("images/episode7/197.webp") with dissolve
            woman "Apakah dia benar -benar mengatakan itu?"
            scene expression ("images/episode7/196.webp") with dissolve
            toby "Ya, tetapi Anda tahu bagaimana keadaannya. Saya harus setuju dengan bos saya jika saya ingin semuanya berjalan baik untuk saya."
            scene expression ("images/episode7/197.webp") with dissolve
            woman "Itu satu -satunya alasan?"
            scene expression ("images/episode7/196.webp") with dissolve
            toby "Siapa tahu. Maksud saya, saya masih tidak tahu nama Anda dan Anda mengharapkan saya untuk berbagi rahasia yang mendalam hanya karena?"
        "Ya. Itu aku. Dan kamu?":

            pass
    scene expression ("images/episode7/198.webp") with dissolve
    kayla "I \ 'M Kayla."
    scene expression ("images/episode7/199.webp") with dissolve
    toby "Senang bertemu denganmu Kayla. Katrina mengatakan kepada saya untuk membawa ini kepada Anda, tetapi saya pikir saya harus membantu Anda dengan apartemen Anda."
    scene expression ("images/episode7/156.webp") with dissolve
    kayla "Pria seperti itu."
    toby "Anda bisa berterima kasih kepada ibuku karena telah membesarkan pria seperti itu."
    if kayla_path:
        scene expression ("images/episode7/157.webp") with dissolve
        kayla "Anda sudah ingin saya bertemu orang tuamu?"
        toby "Saya pikir Anda benar. Terlalu cepat untuk itu. Pertama kita perlu bercinta dan setelah kita dapat bertemu orang tua satu sama lain."
        kayla "Jadi itu urutan yang benar?"
        toby "Setidaknya tiga kali."
        kayla "Hanya tiga? Saya sudah berpikir setidaknya empat."
        toby "Bagus. Lima kali dan kemudian kita akan bertemu orang tua."
    else:

        scene expression ("images/episode7/157.webp") with dissolve
        kayla "Beri aku alamatnya dan aku akan melakukannya."
        toby "Saya tidak bisa melakukan itu. Dia juga mengatakan kepada saya untuk tidak memberikan alamat saya kepada orang asing."
        kayla "Wanita yang pintar."
    scene expression ("images/episode7/158.webp") with dissolve
    kayla "Nah, ini aku."
    toby "Besar. Di Sini."
    if kayla_path:
        scene expression ("images/episode7/200.webp") with dissolve
        kayla "Anda bilang Anda seorang pria dan sekarang Anda hanya memberi saya kotak berat seperti itu. Paling tidak yang bisa Anda lakukan adalah membawanya."
        toby "Jika itu yang diinginkan wanita itu."
        scene expression ("images/episode7/201.webp") with dissolve
        toby "Jadi. Di mana saya harus meletakkan ini?"
        scene expression ("images/episode7/202.webp") with dissolve
        kayla "Tepat di sana di atas meja."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is she really going to undress with me right here?{/i}"
        scene expression ("images/episode7/203.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck me. She is.{/i}"
        scene expression ("images/episode7/204.webp") with dissolve
        kayla "Terima kasih [toby]. Anda bisa pergi sekarang."
        toby "Saya harap saya akan menemukan pintu dengan semua darah di kepala saya."
        scene expression ("images/episode7/205.webp") with dissolve
        kayla "Yang mana?"
        toby "Yang benar."
        scene expression ("images/episode7/206.webp") with dissolve
        kayla "Pintunya ada di sana."
        scene expression ("images/episode7/207.webp") with dissolve
        toby "Benar. Ini benar -benar terlihat seperti pintu sebenarnya."
        scene expression ("images/episode7/208.webp") with dissolve
        kayla "Sampai jumpa."
        scene expression ("images/episode7/159.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck me, she's such a tease.{/i}"
    else:

        kayla "Terima kasih!"
        scene expression ("images/episode7/159.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}That's it. I should get back to work.{/i}"

    scene expression ("images/episode7/209.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I guess this is my life now. Take packages from one place to another without looking what's inside and earn money.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm curious what's inside, but I think it's safer that I don't know.{/i}"

    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode7/210.webp") with dissolve
    hide screen ui_message

    if ep7_monday_date:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It's safe to say that I can go home and take a shower before going on my date.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should go home now.{/i}"

    return

label episode7_monday_evening:
    $ progress = 102

    scene expression ("images/episode7/211.webp") with fade
    toby "Hai [mom]."
    scene expression ("images/episode7/212.webp") with dissolve
    charlotte "Oh, hai [toby!c]. Bagaimana cara kerja?"
    scene expression ("images/episode7/213.webp") with dissolve
    toby "Tidak terlalu menarik dan tidak ada yang buruk. Hanya hari normal. Apa yang kamu buat?"
    scene expression ("images/episode7/212.webp") with dissolve
    charlotte "Sesuatu yang sangat bagus. Anda akan menyukainya."
    if ep7_monday_date:
        scene expression ("images/episode7/214.webp") with dissolve
        toby "Sebenarnya aku keluar malam ini."
        if emma_break:
            scene expression ("images/episode7/215.webp") with dissolve
            charlotte "Jadi? Siapa gadis yang beruntung? Kapan saya bisa bertemu dengannya?"
            scene expression ("images/episode7/216.webp") with dissolve
            toby "Menurut Anda mengapa saya keluar dengan seorang gadis?"
        else:
            scene expression ("images/episode7/215.webp") with dissolve
            charlotte "Katakan Emma, saya menyapa."
            scene expression ("images/episode7/214.webp") with dissolve
            toby "Menurut Anda mengapa saya keluar dengan Emma?"

        scene expression ("images/episode7/215.webp") with dissolve
        charlotte "Saya tahu senyum itu. Itu senyummu bercinta."
        scene expression ("images/episode7/216.webp") with dissolve
        toby "[mom!c] !!!"
        scene expression ("images/episode7/215.webp") with dissolve
        charlotte "Bisa aja. Ini tidak seperti saya tidak tahu [son] saya. Tetapi gunakan perlindungan jika Anda tidak siap untuk memiliki anak."
        scene expression ("images/episode7/217.webp") with dissolve
        toby "Saya akan mandi."
    else:

        scene expression ("images/episode7/214.webp") with dissolve
        toby "Baunya harum. Tak sabar menunggu."
        scene expression ("images/episode7/215.webp") with dissolve
        charlotte "Tentu saja baunya enak. Aku yang sedang memasak."
        scene expression ("images/episode7/216.webp") with dissolve
        toby "Beruntung Anda sederhana."
        scene expression ("images/episode7/215.webp") with dissolve
        charlotte "Kesederhanaan berlebihan. Ini untuk orang yang tidak tahu cara memasak."
        scene expression ("images/episode7/217.webp") with dissolve
        toby "Aku akan mandi."

    scene expression ("images/episode7/218.webp") with fade
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode7/219.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode7/220.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    $ progress = 103
    scene expression ("images/episode7/221.webp") with fade
    patricia "Anda benar -benar perlu belajar menutup pintu."
    scene expression ("images/episode7/222.webp") with dissolve
    toby "Anda perlu belajar cara mengetuk."
    if emma_break == False:
        scene expression ("images/episode7/221.webp") with dissolve
        patricia "Aku sudah terbiasa denganmu tidur di Emma sehingga aku lupa kamu tinggal di sini."
        scene expression ("images/episode7/222.webp") with dissolve
        toby "Aku bahkan tidak sering tidur di sana dan itu akan segera berakhir ketika dia menemukan asrama."
        scene expression ("images/episode7/223.webp") with dissolve
        patricia "Malang kamu. Anda akan melakukan lebih sedikit seks."
        scene expression ("images/episode7/224.webp") with dissolve
        toby "Sebenarnya. Malang kamu, karena dia akan datang ke sini dan kami akan melakukan seks yang gila dan liar tepat di atas kamar Anda."
        scene expression ("images/episode7/225.webp") with dissolve
        patricia "Eww ... kamu kotor. Jangan ingin tahu detailnya."
    else:
        scene expression ("images/episode7/223.webp") with dissolve
        patricia "Ini tidak seperti ada sesuatu yang menarik untuk dilihat."
        scene expression ("images/episode7/224.webp") with dissolve
        toby "Bagaimana jika saya menyentak?"
        if ep6_caughtJerking:
            scene expression ("images/episode7/225.webp") with dissolve
            patricia "Ini tidak seperti ini pertama kalinya."
        else:
            scene expression ("images/episode7/225.webp") with dissolve
            patricia "Eww ... kamu kotor."

    scene expression ("images/episode7/226_normal.webp") with dissolve
    toby "Jadi? Bagaimana hari pertama sekolah Anda?"
    scene expression ("images/episode7/227_smile.webp") with dissolve
    patricia "Sebenarnya itu cukup menarik."
    scene expression ("images/episode7/227_happy.webp") with dissolve
    patricia "Saya bisa masuk ke semua kelas yang ingin saya ambil semester ini."
    scene expression ("images/episode7/227_smile.webp") with dissolve
    patricia "Saya bertemu beberapa orang baru juga."
    if emma_break == True:
        scene expression ("images/episode7/227_flirty.webp") with dissolve
        patricia "Saya melihat mantan Anda. Dia semua menyebalkan dan genit."
        scene expression ("images/episode7/226_normal.webp") with dissolve
        toby "Saya melihatnya juga."
        scene expression ("images/episode7/227_flirty.webp") with dissolve
        patricia "Jadi itu berarti Anda telah melihat penampilan barunya."
        scene expression ("images/episode7/227_normal.webp") with dissolve
        patricia "Dia lebih mirip pelacur sekarang."
        scene expression ("images/episode7/226_normal.webp") with dissolve
        toby "Kami putus karena hal -hal sulit dalam hubungan jarak jauh, tetapi dia tidak menyebalkan."
        toby "Saya mengerti. Anda membencinya karena dia adalah pacar saya, tetapi sekarang tidak ada alasan bagi Anda untuk membencinya."
        scene expression ("images/episode7/227_normal.webp") with dissolve
        patricia "Kamu masih mencintainya?"
        scene expression ("images/episode7/226_smile.webp") with dissolve
        toby "Saya tidak mengatakan itu. Itu adil, saya pikir itu tidak adil. Dia sangat baik bagiku saat kami bersama."
    else:
        scene expression ("images/episode7/226_normal.webp") with dissolve
        toby "Bagaimana Anda bergaul dengan Emma?"
        scene expression ("images/episode7/227_happy.webp") with dissolve
        patricia "Saya masih berpikir dia menyebalkan, tapi kami hampir melakukan percakapan normal."
        scene expression ("images/episode7/226_laugh.webp") with dissolve
        toby "Itu hampir terdengar seperti kemajuan."
        scene expression ("images/episode7/227_smile.webp") with dissolve
        patricia "Apa yang bisa saya katakan. Saya seorang malaikat dan [mom] mengatakan kepada saya untuk bersikap baik padanya."
        scene expression ("images/episode7/226_laugh.webp") with dissolve
        toby "Saya kira saya harus berterima kasih padanya?"
        scene expression ("images/episode7/227_smile.webp") with dissolve
        patricia "Yah, dia tidak semuanya buruk."
    scene expression ("images/episode7/226_curious.webp") with dissolve
    toby "Jadi? Ada anak laki -laki yang lucu?"
    scene expression ("images/episode7/227_flirty.webp") with dissolve
    patricia "Aku tidak tahu. Mungkin?"
    scene expression ("images/episode7/226_laugh.webp") with dissolve
    toby "Ya atau tidak."
    scene expression ("images/episode7/227_laugh.webp") with dissolve
    patricia "Aku tidak memberitahumu apa pun. Maka Anda akan bisa menggodaku tentang hal itu."
    scene expression ("images/episode7/226_smile.webp") with dissolve
    toby "Aku akan menggodamu apa pun yang terjadi."
    scene expression ("images/episode7/227_smile.webp") with dissolve
    patricia "Lebih baik menggodaku tanpa mengetahui keterangan apa pun."
    scene expression ("images/episode7/226_laugh.webp") with dissolve
    toby "Bagus. Saya akan bertanya kepada Bea lain kali saya akan membawanya pulang, karena Anda terlalu takut untuk mengemudi."
    scene expression ("images/episode7/227_normal.webp") with dissolve
    patricia "Pertama. Saya tidak takut mengemudi, tetapi ketika saya memiliki sopir mengapa saya harus?"
    scene expression ("images/episode7/226_laugh.webp") with dissolve
    toby "Itulah yang saya bagi Anda? Seorang sopir?"
    scene expression ("images/episode7/227_smile.webp") with dissolve
    patricia "Yang lucu."
    scene expression ("images/episode7/226_smile.webp") with dissolve
    toby "Itu tidak membantu sama sekali."
    scene expression ("images/episode7/227_smile.webp") with dissolve
    patricia "Apa? Mendapatkan pujian dari seorang gadis manis tidak melakukan apa pun untuk Anda?"
    scene expression ("images/episode7/227_laugh.webp") with dissolve
    patricia "Anda harus mempertimbangkan kemungkinan bahwa Anda mungkin gay."
    scene expression ("images/episode7/226_laugh.webp") with dissolve
    toby "Atau mungkin saya mendapatkan begitu banyak pujian yang saya gunakan untuk mereka."
    scene expression ("images/episode7/227_laugh.webp") with dissolve
    patricia "Ya, benar. Saya lupa betapa panasnya pai saya [brother] saya."
    scene expression ("images/episode7/226_smile.webp") with dissolve
    toby "Saya pikir Anda melupakan alasan Anda tidak dapat menemukan pacar. Karena Anda membandingkannya dengan saya."
    scene expression ("images/episode7/227_normal.webp") with dissolve
    patricia "Hampir tidak alasan, tapi baik -baik saja."
    scene expression ("images/episode7/227_flirty.webp") with dissolve
    patricia "Omong-omong. Saya memulai kelas yang mungkin Anda temukan menarik."
    scene expression ("images/episode7/226_curious.webp") with dissolve
    toby "Anda mengambil seksualitas manusia?"
    scene expression ("images/episode7/227_surprised.webp") with dissolve
    patricia "Itu tebakan yang mudah. Itu satu -satunya subjek yang menurut Anda menarik?"
    scene expression ("images/episode7/226_laugh.webp") with dissolve
    toby "Tidak terlalu. Saya benar -benar bisa pergi untuk beberapa psikologi, tetapi memberi Anda pikir saya cabul, itu satu -satunya subjek yang Anda pikir akan menarik minat saya."
    scene expression ("images/episode7/227_normal.webp") with dissolve
    patricia "Yah saya juga mengambil psikologi. Saya bertemu seorang gadis baru di sana. Dia sangat lucu dan lucu."
    scene expression ("images/episode7/226_smile.webp") with dissolve
    toby "Dan Anda mengatakan bahwa saya mungkin memiliki masalah dengan orientasi seksual saya."
    scene expression ("images/episode7/227_laugh.webp") with dissolve
    patricia "Tidak seperti itu. Maksudku, ya dia seksi, tapi dia sebenarnya baik. Dia akan menjadi guru."
    scene expression ("images/episode7/226_smile.webp") with dissolve
    toby "Itu bagus."
    scene expression ("images/episode7/226_curious.webp") with dissolve
    toby "Dan apa yang akan Anda pelajari dalam seksualitas manusia?"
    scene expression ("images/episode7/227_laugh.webp") with dissolve
    patricia "Saya pikir Anda tidak tertarik dengan subjek kasar seperti itu."
    scene expression ("images/episode7/226_smile.webp") with dissolve
    toby "Saya tidak, tetapi saya melihatnya di mata Anda bahwa Anda ingin membicarakannya."

    if ep6_caughtJerking:
        scene expression ("images/episode7/227_flirty.webp") with dissolve
        patricia "Sebenarnya, saya pikir itu ide yang buruk. Maksud saya, Anda tidak ingin berakhir dengan boner ketika saya memberi tahu Anda bahwa saya akan belajar tentang seks."
        patricia "Lalu Anda akan menjadi keras lagi, dan apa yang Anda sebut lagi? Bola Biru?"
        scene expression ("images/episode7/226_laugh.webp") with dissolve
        toby "Anda mungkin akan mempelajari lebih lanjut tentang STD."
        scene expression ("images/episode7/227_smile.webp") with dissolve
        patricia "Mungkin, tapi itu hanya satu pelajaran. Saya yakin akan ada sesuatu tentang posisi seksual."
        scene expression ("images/episode7/227_flirty.webp") with dissolve
        patricia "Atau mengenal diri sendiri lebih baik, di mana kita akan menjelajahi bagian -bagian sensitif kita."
        scene expression ("images/episode7/227_sexy.webp") with dissolve
        patricia "Mungkin kita harus mencoba posisi yang berbeda. Dengan pakaian kami menyala."
        scene expression ("images/episode7/228.webp") with dissolve
        patricia "Atau mungkin tanpa pakaian."
    else:
        scene expression ("images/episode7/227_laugh.webp") with dissolve
        patricia "Saya tidak punya keinginan untuk membicarakan hal -hal nakal dengan Anda."
        patricia "Siapa yang tahu efek apa yang bisa terjadi pada Anda."
        scene expression ("images/episode7/226_laugh.webp") with dissolve
        toby "Apa efek yang bisa didengarkan tentang STD pada saya?"
        scene expression ("images/episode7/227_smile.webp") with dissolve
        patricia "Siapa bilang itu hanya tentang PMS. Ada pelajaran tentang hal lain."
        scene expression ("images/episode7/227_flirty.webp") with dissolve
        patricia "Seperti posisi seksual misalnya."
        patricia "Atau mengenal diri sendiri lebih baik. Mungkin kita harus menjelajahi bagian -bagian sensitif kita."
        scene expression ("images/episode7/226_laugh.webp") with dissolve
        toby "Anda terlalu banyak pemalu untuk itu."
        scene expression ("images/episode7/227_sexy.webp") with dissolve
        patricia "Mungkin, tapi Anda tahu saya suka mendapatkan nilai bagus dan jika ini yang harus saya lakukan, saya akan melakukannya."
        scene expression ("images/episode7/228.webp") with dissolve
        patricia "Saya harus lebih mengeksplorasi bagian sensitif saya."
    scene expression ("images/episode7/229.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit I have a boner. I can't let Tris see me like this. Again.{/i}"
    if ep6_caughtJerking:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I can't give her the satisfaction.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She will think I'm a pervert, but why is she teasing me like this?{/i}"
    scene expression ("images/episode7/231.webp") with dissolve
    toby "Membosankan. Aku akan meninggalkanmu di kamar mandi."
    if ep6_caughtJerking:
        scene expression ("images/episode7/230.webp") with dissolve
        patricia "Apakah itu tonjolan yang saya lihat? Anda benar -benar lemah di game ini."
    else:
        scene expression ("images/episode7/230.webp") with dissolve
        patricia "Ewww ... kamu kesulitan?"
    toby "Itu bukan apa -apa. Saya akan pergi."
    scene expression ("images/episode7/232.webp") with dissolve
    patricia "Tunggu. Jangan pergi."
    if ep6_caughtJerking:
        toby "Lihat. Saya mengalami hari yang sulit di tempat kerja dan selain itu saya tidak ingin permainan Anda."
    else:
        toby "Dengar, saya tidak tahu apa yang Anda pikir akan terjadi ketika Anda membicarakan semua hal itu, tetapi saya keluar."
    scene expression ("images/episode7/233.webp") with dissolve
    patricia "Maaf, tetapi hari ini guru seksualitas manusia kami memberi tahu kami bahwa pria menjadi terangsang dengan apa yang mereka lihat sementara wanita menjadi horney dengan apa yang mereka dengar."
    patricia "Tetapi dia mengatakan bahwa kebanyakan pria benar -benar terangsang karena berbicara kotor. Dia mendorong kami untuk berbicara kotor dengan pacar kami selama beberapa menit hanya untuk melihat reaksi mereka."
    if ep6_caughtJerking:
        patricia "Dan saya sudah tahu Anda sulit melihat sesuatu, jadi saya ingin melihat apakah itu benar -benar berhasil."
    else:
        patricia "Dan karena saya tidak punya pacar, saya pikir akan lucu untuk mencobanya pada Anda."
    scene expression ("images/episode7/234.webp") with dissolve
    toby "Ini bukan pembicaraan kotor."
    scene expression ("images/episode7/235.webp") with dissolve
    patricia "Jadi apa itu?"
    scene expression ("images/episode7/234.webp") with dissolve
    toby "Anda terlalu tidak bersalah untuk itu, jadi saya pergi."
    scene expression ("images/episode7/236.webp") with dissolve
    patricia "Jangan pergi seperti itu. Bea menungguku di luar. Apa yang akan dia pikirkan jika dia melihatmu dengan boner meninggalkan kamar mandi?"
    if toby_job == 0:
        scene expression ("images/episode7/234.webp") with dissolve
        toby "Kotoran. Apa yang Anda pikirkan akan terjadi?"
    else:
        scene expression ("images/episode7/237.webp") with dissolve
        toby "Lalu apa ide besarmu? Menurut Anda apa yang akan terjadi?"
    scene expression ("images/episode7/236.webp") with dissolve
    patricia "Berapa lama waktu yang dibutuhkan untuk turun?"
    scene expression ("images/episode7/237.webp") with dissolve
    toby "Aku tidak tahu. Menit?"
    scene expression ("images/episode7/235.webp") with dissolve
    patricia "Tidak bisakah kamu melakukan sesuatu?"
    scene expression ("images/episode7/238.webp") with dissolve
    toby "Yah, aku bisa menyentak, tapi tidak saat kamu di sini."
    scene expression ("images/episode7/233.webp") with dissolve
    patricia "Aku tidak akan melihat."
    scene expression ("images/episode7/238.webp") with dissolve
    toby "Bukan itu cara kerja. Aku tidak bisa menyentak. Saya perlu menonton sesuatu atau seseorang melakukannya untuk saya, jika tidak, itu akan memakan waktu selamanya."
    scene expression ("images/episode7/233.webp") with dissolve
    patricia "Kemudian tonton porno atau apa pun yang biasanya Anda lakukan."
    scene expression ("images/episode7/237.webp") with dissolve
    toby "Saya tidak membawa ponsel saya. Lihat ini benar -benar canggung. Bawa saja ponsel saya dan saya akan segera selesai."
    scene expression ("images/episode7/239.webp") with dissolve
    patricia "Tapi apa yang akan dipikirkan Bea jika saya keluar dari kamar mandi dengan riasan masih ada."
    scene expression ("images/episode7/238.webp") with dissolve
    toby "Pada titik ini saya tidak benar -benar peduli padanya. Anda tahu apa, saya keluar. Dia temanmu jadi tanggung jawabmu untuk menjelaskan kepadanya mengapa aku keluar dengan boner."
    scene expression ("images/episode7/240.webp") with dissolve
    patricia "Gunakan milikku!"
    scene expression ("images/episode7/241.webp") with dissolve
    toby "Beri aku itu dan jangan lihat. Ini sudah cukup canggung."
    patricia "Tentu saja saya menang. Ini tidak seperti saya tertarik melihat [brother] brengsek ke ponsel saya."
    patricia "Tapi silakan gunakan penyamaran atau hapus sejarah sesudahnya. Ini tidak seperti saya ingin melihat apa yang Anda lihat."
    scene expression ("images/episode7/242.webp") with dissolve
    toby "Tolong, tutup mulut. Cukup buruk Anda di sini."
    scene expression ("images/episode7/242_1.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see... what I should look at?{/i}"
    menu:
        "{i} Beberapa situs porno {/i}":
            scene expression ("images/episode7/243.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck this is so awkward.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Come on [toby!c]. Forget your [sister] is in the bathroom. Just jerk off. Look at the porn that's playing.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Look at that big ass. Those huge tits.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}That's it. I'm going to cum.{/i}"
            scene expression ("images/episode7/244_0.webp") with dissolve
            with flash
            scene expression ("images/episode7/244.webp") with dissolve
            with flash
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This was the most awkward wank ever.{/i}"
            scene expression ("images/episode7/245.webp") with dissolve
            toby "Di Sini. Jangan pernah membicarakan hal ini."
        "{i} [JGR] Lihatlah ke galeri {/i}"(csq="Tris +1 & Galeri Gambar & Penting untuk Tris \ 'Path"):


            $ ep7_tris_gallery = True
            scene expression ("images/episode7/242_1.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I don't know what's worse. Me jerking of while my [sister] is in the bathroom, or me looking at her gallery hoping to find jerk off material.{/i}"
            scene expression ("images/episode7/246.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}No. I can't jerk off to this. She's way to sweet.{/i}"
            scene expression ("images/episode7/247.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}A photo with her and Bea. Too silly, I can't look at this while jerking off.{/i}"
            scene expression ("images/episode7/248.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Oops. This one looks interesting, but maybe I can find something better.{/i}"
            scene expression ("images/episode7/249.webp") with dissolve
            $ unlockImage(persistent.patricia_14)
            with shake
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck. This photo is really hot. I wonder if she sent those pictures to anyone.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Nah. Can't be. She's too innocent for that and besides, it's not like she has a boyfriend.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But that's not what I am doing here. I need to finish jerking off.{/i}"
            scene expression ("images/episode7/250.webp") with dissolve
            patricia "Berapa lama waktu yang dibutuhkan."
            scene expression ("images/episode7/251.webp") with dissolve
            toby "Tolong tutup mulut. Saya akan memberi tahu Anda ketika saya selesai."
            scene expression ("images/episode7/243.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This feels so wrong.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But she's so damn hot in this photo.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I can't believe I'm jerking off to my little [sister]'s photo.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck. She's so hot!{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm almost there.{/i}"
            scene expression ("images/episode7/244.webp") with dissolve
            with flash
            with flash
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yes, yes, yes...{/i}"
            stop music fadeout 2.0
            scene expression ("images/episode7/252.webp") with dissolve
            patricia "Apa yang kamu lihat, kamu perv?"
            patricia "Apa yang salah denganmu! Aku sialanmu [sister]."
            scene expression ("images/episode7/253.webp") with dissolve
            patricia "Beri aku bahwa kamu sialan. Aku tidak ingin bertemu denganmu lagi."
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}There is nothing I could say to make this any better.{/i}"

    $ progress = 104

    scene expression ("images/episode7/254.webp") with fade
    toby "Hai Bea."
    scene expression ("images/episode7/255.webp") with dissolve
    beatrice "Oh. Hai [toby!c]. Apa kabarmu?"
    scene expression ("images/episode7/256.webp") with dissolve
    if ep7_monday_date:
        toby "Saya baru saja kembali dari kantor dan bersiap -siap untuk pergi keluar dengan beberapa teman. Bagaimana hari pertama kuliah?"
    else:
        toby "Saya baru saja kembali dari kantor dan mandi. Apa kabarmu? Bagaimana hari pertama kuliah?"
    scene expression ("images/episode7/257.webp") with dissolve
    beatrice "Sebenarnya itu sangat bagus. Saya sangat menyukainya. Aku tidak tahu apakah Tris memberitahumu, tapi aku merasa sedikit lebih keren sekarang karena aku seorang siswa."
    scene expression ("images/episode7/256.webp") with dissolve
    toby "Ya, dia membual tentang betapa kerennya menjadi seorang siswa. Saya harus mendengarkannya mengoceh ketika saya sedang menyikat gigi."
    scene expression ("images/episode7/257.webp") with dissolve
    beatrice "Ya. Saya tidak berpikir itulah yang ingin Anda dengar setelah seharian bekerja sambil menyikat gigi."
    scene expression ("images/episode7/258.webp") with dissolve
    toby "Yup. Anda benar."
    scene expression ("images/episode7/259.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should leave before Tris comes out. I feel like I should avoid her for now.{/i}"
    scene expression ("images/episode7/256.webp") with dissolve
    if ep7_monday_date:
        toby "Bagaimanapun. Saya harus pergi. Saya tidak suka terlambat."
        scene expression ("images/episode7/257.webp") with dissolve
        beatrice "Tidak seperti [sister] Anda. Dia selalu terlambat."
        scene expression ("images/episode7/260.webp") with dissolve
        toby "Aku tahu. Pokoknya, sampai jumpa."
    else:
        toby "Ngomong -ngomong, aku akan membiarkanmu dan Tris menikmati malam."
        scene expression ("images/episode7/257.webp") with dissolve
        if beatrice_path == True:
            beatrice "Anda bisa tinggal bersama kami. Kami akan menonton film."
            scene expression ("images/episode7/260.webp") with dissolve
            toby "Sebenarnya aku terlalu lelah. Mungkin lain kali."
        else:

            beatrice "Terima kasih. Sampai jumpa."
            scene expression ("images/episode7/260.webp") with dissolve
            toby "Ya. Kamu juga!"

    return

label episode7_monday_night:
    scene expression ("images/episode7/261.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmm... It's still early. What should I do?{/i}"
    scene expression ("images/episode7/262.webp") with dissolve
    if toby_job == 0:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I could continue the book Darlene gave me.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I could continue the book Katrina gave me.{/i}"

    scene expression ("images/episode7/263.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see where we were.{/i}"

    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/264.webp") with dissolve
    hide screen ui_message

    $ ui.saybehavior()
    $ ui.interact()

    return


label episode7_tuesday_morning:
    $ progress = 106
    stop music fadeout 2.0
    show screen ui_message("Tuesday") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message

    if ep7_monday_date:
        scene expression ("images/episode7/267.webp")
        toby "Pagi, [mom]."
        scene expression ("images/episode7/268.webp") with dissolve
        charlotte "Seseorang memiliki malam yang sangat baik."
        scene expression ("images/episode7/267.webp") with dissolve
        toby "Saya tidak akan memberi Anda detail jadi lepaskan pikiran Anda."
        scene expression ("images/episode7/268.webp") with dissolve
        charlotte "Bagus. Saya tidak akan menanyakan kali ini."
    else:
        scene expression ("images/episode7/265.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I must have fallen asleep while reading the book.{/i}"

        scene expression ("images/episode7/266.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It's 11 o'clock already.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}At least Tris didn't wake me up to take her to school, but after last night I wouldn't want to see me if I were her.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Anyway, let's see what [mom] is doing.{/i}"

        scene expression ("images/episode7/269.webp") with dissolve
        toby "Pagi, [mom]."
        scene expression ("images/episode7/270.webp") with dissolve
        charlotte "Selamat pagi untukmu terlalu mengantuk. Bagaimana Anda tidur?"
        scene expression ("images/episode7/269.webp") with dissolve
        toby "Sebenarnya sangat baik, karena Tris tidak membangunkan saya untuk membawanya ke sekolah."
        scene expression ("images/episode7/270.webp") with dissolve
        charlotte "Ya, dia membangunkan saya. Dia mengatakan bahwa Anda membawanya kemarin dan dia akan merasa tidak enak untuk membangunkan Anda lagi."
        scene expression ("images/episode7/271.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I don't buy that shit. She never feels bad about waking me up. Must be because of the bathroom event.{/i}"

    scene expression ("images/episode7/272.webp") with dissolve
    toby "Ngomong -ngomong, apa yang kamu lakukan?"
    scene expression ("images/episode7/273.webp") with dissolve
    charlotte "Saya menikmati kopi saya dan kemudian saya akan keluar untuk memangkas rumput."
    scene expression ("images/episode7/272.webp") with dissolve
    toby "Anda tidak harus. Sudah kubilang aku merawat halaman belakang."
    scene expression ("images/episode7/273.webp") with dissolve
    charlotte "Saya tahu apa yang Anda katakan, tetapi saya merasa sangat buruk untuk membiarkan Anda mengurus segala sesuatu di sekitar rumah."
    scene expression ("images/episode7/274.webp") with dissolve
    charlotte "Saya merasakan diva seperti itu. Anda dan [father] Anda tidak membiarkan saya mendapatkan pekerjaan. Dan Anda tidak membiarkan saya melakukan pekerjaan apa pun di sekitar rumah."
    scene expression ("images/episode7/275.webp") with dissolve
    toby "Tidak ada [mother] saya yang akan melakukan tugas saya."
    scene expression ("images/episode7/276.webp") with dissolve
    charlotte "Anda anak yang baik."
    scene expression ("images/episode7/277.webp") with dissolve
    charlotte "Saya berjanji saya akan merasa buruk melihat Anda bekerja sementara saya menikmati bak mandi air panas."
    scene expression ("images/episode7/275.webp") with dissolve
    toby "Sepertinya Anda merasa kasihan pada saya."
    scene expression ("images/episode7/273.webp") with dissolve
    charlotte "Aku akan memberimu sesuatu untuk dimakan dan kemudian aku tidak akan merasa sangat buruk."
    scene expression ("images/episode7/275.webp") with dissolve
    toby "Kesepakatan."


    show screen ui_message("A short time later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message

    scene expression ("images/episode7/278.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/279.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/280.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/281.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/282.webp") with dissolve:
        xalign 1.0
        yalign 0.0
        linear 10.0 yalign 1.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/283.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/284.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/285.webp") with dissolve
    charlotte "Saya pikir saya akan merasa tidak enak melihat Anda bekerja sementara saya bersantai di bak mandi air panas, tetapi sejujurnya saya tidak merasakan penyesalan apa pun."
    charlotte "Sebenarnya cukup bagus."
    scene expression ("images/episode7/286.webp") with dissolve
    toby "Anda tahu Anda benar -benar pengganggu?"
    scene expression ("images/episode7/285.webp") with dissolve
    charlotte "Saya seorang pengganggu? Kemarilah dan minta maaf."
    scene expression ("images/episode7/286.webp") with dissolve
    toby "Dengan sikap itu?"
    scene expression ("images/episode7/287.webp") with dissolve
    charlotte "Bagus. Lalu lebih dekat sehingga saya bisa memberi tahu Anda sebuah rahasia."
    scene expression ("images/episode7/286.webp") with dissolve
    toby "Saya tidak suka gosip."
    scene expression ("images/episode7/287.webp") with dissolve
    charlotte "Hanya untuk sesaat. Saya berjanji Anda tidak akan menyesalinya."
    scene expression ("images/episode7/288_1.webp") with dissolve
    toby "Jadi? Apa rahasianya?"
    scene expression ("images/episode7/288_2.webp") with dissolve
    charlotte "Mendekati. Saya tidak bisa meneriakkan rahasia."
    scene expression ("images/episode7/289.webp") with dissolve
    charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I'm not a bully. A bully would have called you here just to splash you.{/i}"
    scene expression ("images/episode7/290.webp") with dissolve
    charlotte "Beruntung untukmu, aku bukan pengganggu."
    scene expression ("images/episode7/291.webp") with dissolve
    toby "Jadi beginilah cara Anda bermain."
    scene expression ("images/episode7/292_1.webp") with dissolve
    toby "Ambil ini."
    scene expression ("images/episode7/292_2.webp") with dissolve
    charlotte "Sekarang siapa pengganggu itu?"
    scene expression ("images/episode7/293.webp") with dissolve
    toby "Saya adalah korban di sini!Anda. Anda memulainya. Saya baru saja merespons."
    charlotte "Oh sayang."
    scene expression ("images/episode7/294.webp") with dissolve
    charlotte "Datang ke [mommy]."
    toby "Tidak, tidak, tidak ... Anda tidak menarik saya di bak mandi air panas."
    scene expression ("images/episode7/295.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode7/296.webp") with dissolve
    charlotte "Saya menang!"
    scene expression ("images/episode7/297.webp") with dissolve
    menu:
        "{i} [JGR] Pendekatan genit {/i}"(csq="Charlotte +1 & Galeri Gambar & Penting untuk Path Charlotte \ '"):
            $ ep7_charlotte_flirt = True
            $ charlotte_rel += 1
            $ unlockImage(persistent.charlotte_14)
            scene expression ("images/episode7/298.webp") with dissolve
            if toby_job == 0:
                toby "Ummm ... ya, apa yang sebenarnya menang?"
            else:
                toby "Sebenarnya, saya menganggap diri saya sebagai pemenang."
        "{i} Ceritakan padanya tentang payudara yang terbuka {/i}":
            scene expression ("images/episode7/298.webp") with dissolve
            toby "[mom!c] Anda punya situasi di sana."

    scene expression ("images/episode7/299.webp") with dissolve
    charlotte "Ups ... yang seharusnya tidak terjadi."

    if ep7_charlotte_flirt:
        scene expression ("images/episode7/300.webp") with dissolve
        toby "Itu tidak seperti yang saya pikirkan."
        scene expression ("images/episode7/301.webp") with dissolve
        charlotte "[toby!c] !!! Hanya wanita yang terangsang saat mereka basah. Pria tidak!"

    scene expression ("images/episode7/302_1.webp") with dissolve
    charlotte "Mari kita pergi ke lounge. Saya membutuhkan pria yang kuat untuk meletakkan tabir surya di punggung saya."
    scene expression ("images/episode7/302_2.webp") with dissolve
    toby "Saya akan melakukan lebih banyak pekerjaan, tetapi karena seseorang memiliki ide lain untuk saya, saya akan memakai batang saya dan segera kembali."
    if ep7_charlotte_flirt:
        scene expression ("images/episode7/303.webp") with dissolve
        toby "Pada saat saya kembali, saya berharap Anda kehilangan bagian atas."
        scene expression ("images/episode7/304.webp") with dissolve
        charlotte "[toby!c]! Bukan itu bagaimana Anda berbicara dengan [mother] Anda."
        scene expression ("images/episode7/303_2.webp") with dissolve
        toby "Lalu saya sarankan Anda menemukan orang lain untuk menerapkan tabir surya karena saya tidak akan berjuang di sekitar senar."
    else:
        scene expression ("images/episode7/303.webp") with dissolve
        toby "Kembali!"

    label memory_22:

        scene expression ("images/episode7/305.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ progress = 107
        $ ui.pausebehavior(9.3)
        if ep7_charlotte_flirt:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Looks like [mom] took my advice.{/i}"
        else:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Looks like [mom] got ready. Can't say I mind.{/i}"

        scene expression ("images/episode7/306.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode7/306_1.webp") with dissolve
        if ep7_charlotte_flirt:
            charlotte "Saya menyukai gagasan tidak mendapatkan garis tan jadi saya menerima saran Anda."
            scene expression ("images/episode7/307.webp") with dissolve
            toby "Apa yang bisa saya katakan. Saya memberikan nasihat yang bagus."
        else:
            charlotte "Saya tidak ingin garis tan jadi saya memutuskan untuk menghapus bagian atas. Saya harap itu tidak mengganggu Anda."
            scene expression ("images/episode7/307.webp") with dissolve
            toby "Sama sekali tidak."

        scene expression ("images/episode7/308.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode7/309.webp") with dissolve
        charlotte "Saya merasa agak manja. Pertama saya tidak diizinkan untuk bekerja. Kemudian saya tidak diizinkan untuk bekerja di sekitar rumah."
        charlotte "Sekarang Anda memijat saya."
        toby "Saya menerapkan tabir surya, tidak memijat Anda."
        scene expression ("images/episode7/310.webp") with dissolve
        charlotte "Rasanya sama. Anda memiliki tangan yang sangat bagus."
        toby "Ya, Anda bisa mengatakan bahwa Anda sedikit manja, tetapi Anda pantas mendapatkannya."
        scene expression ("images/episode7/311_laugh.webp") with dissolve
        charlotte "Apa yang telah saya lakukan untuk mendapatkan ini?"
        scene expression ("images/episode7/312_flirty.webp") with dissolve
        toby "Anda menjadi [mother] saya. Jadi saya mengatakan itu alasan yang cukup bagus."
        scene expression ("images/episode7/311_smile.webp") with dissolve
        charlotte "Anda tidak salah. Itu tidak selalu mudah."
        scene expression ("images/episode7/312_curious.webp") with dissolve
        toby "Apa maksudmu? Saya adalah seorang malaikat."
        scene expression ("images/episode7/311_laugh.webp") with dissolve
        charlotte "Yang jatuh mungkin."
        scene expression ("images/episode7/312_smile.webp") with dissolve
        toby "Ayo. Saya tidak seburuk itu."
        scene expression ("images/episode7/311_laugh.webp") with dissolve
        charlotte "Anda mengunci guru Anda di ruang kelas hanya karena dia tidak membiarkan Anda mencium seorang gadis."
        scene expression ("images/episode7/312_smile.webp") with dissolve
        toby "Seseorang harus mengajar gadis itu cara mencium dengan benar."
        scene expression ("images/episode7/311_cute.webp") with dissolve
        charlotte "Anda berusia 10 tahun. Anda juga tidak tahu cara mencium."
        scene expression ("images/episode7/312_laugh.webp") with dissolve
        toby "Saya memang tahu. Sehari sebelum gadis lain menciumku."
        scene expression ("images/episode7/311_smile.webp") with dissolve
        charlotte "Anda selalu menjadi pelajar yang cepat."
        scene expression ("images/episode7/312_laugh.webp") with dissolve
        toby "Menurut Anda, bagaimana lagi saya belajar memberikan pijatan yang baik?"
        scene expression ("images/episode7/311_flirty.webp") with dissolve
        charlotte "Saya pikir Anda hanya menerapkan tabir surya."
        scene expression ("images/episode7/312_laugh.webp") with dissolve
        toby "Saya menggunakan istilah yang Anda pahami."
        scene expression ("images/episode7/311_laugh.webp") with dissolve
        charlotte "Saya kira saya harus mengucapkan terima kasih."
        scene expression ("images/episode7/312_flirty.webp") with dissolve
        toby "Ciuman di pipi begitu aku selesai sudah cukup."
        scene expression ("images/episode7/311_smile.webp") with dissolve
        charlotte "Itu bisa dilakukan, tetapi pertama -tama Anda perlu menyelesaikannya."
        scene expression ("images/episode7/313.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}When you have an ass like that I don't want to finish at all.{/i}"
        scene expression ("images/episode7/314.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe I could go lower on her ass.{/i}"
        menu:
            "{i} [JGR] Jalan lebih rendah {/i}"(csq="Acara Khusus & Penting untuk Charlotte \ 'Path."):
                $ ep7_dirty_sunscreen = True

                scene expression ("images/episode7/315.webp") with dissolve
                charlotte "Pastikan Anda tidak ketinggalan tempat."
                scene expression ("images/episode7/316.webp") with dissolve
                toby "Jangan khawatir [mom]. Saya tahu apa yang saya lakukan."
                scene expression ("images/episode7/315.webp") with dissolve
                charlotte "Saya bisa melihat itu."

            "{i} mainkan aman {/i}" if not _in_replay:
                pass

        scene expression ("images/episode7/317.webp") with dissolve
        toby "Kaki Anda juga perlu dilindungi oleh matahari."
        charlotte "Betapa bijaksana!"
        scene expression ("images/episode7/318.webp") with dissolve
        toby "Tentu saja. Saya tidak ingin [mom] saya memiliki tan yang tambal sulam."

        if ep7_dirty_sunscreen:
            scene expression ("images/episode7/319.webp") with dissolve
            charlotte "Dalam hal ini saya pikir Anda melewatkan satu tempat."
            scene expression ("images/episode7/320.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I haven't forgotten your side boobs [mom]. I kept the best for dessert.{/i}"
            toby "Sudahkah saya sekarang. Saya bertanya -tanya apa yang mungkin saya lewatkan."
            scene expression ("images/episode7/319.webp") with dissolve
            charlotte "Baik jika Anda tidak tahu saya tidak memberi tahu Anda."
            scene expression ("images/episode7/321.webp") with dissolve
            toby "Mari kita bermain panas dan dingin."
            charlotte "Baik -baik saja denganku."
            scene expression ("images/episode7/322.webp") with dissolve
            toby "Mari kita mulai dari sini."
            scene expression ("images/episode7/323.webp") with dissolve
            charlotte "Saya tidak tahu harus berkata apa. Ini semakin panas, tetapi Anda pergi ke arah yang salah, jadi saya kira saya harus mengatakan dingin?"
            toby "Dingin sudah."
            scene expression ("images/episode7/324.webp") with dissolve
            toby "Jadi mari kita pergi ke sini."
            charlotte "Ini semakin hangat."
            scene expression ("images/episode7/325.webp") with dissolve
            charlotte "Semakin hangat."
            toby "Apakah sekarang?"
            scene expression ("images/episode7/326.webp") with dissolve
            charlotte "Sangat hangat sekarang."
            toby "Saya cukup positif saya menerapkan tabir surya di leher Anda, jadi saya kira saya harus pergi ke tempat lain."
            scene expression ("images/episode7/327.webp") with dissolve
            charlotte "Panas."
            scene expression ("images/episode7/328.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode7/329.webp") with dissolve
            charlotte "Itu sebenarnya api."
            scene expression ("images/episode7/330.webp") with dissolve
            toby "Apakah Anda suka saat saya bermain dengan api?"
            scene expression ("images/episode7/329.webp") with dissolve
            charlotte "Saya seharusnya tidak, tetapi tidak dapat membantu. Tanganmu ajaib."
            scene expression ("images/episode7/330.webp") with dissolve
            toby "Jangan mendapatkan ide. Saya hanya menerapkan tabir surya."
            scene expression ("images/episode7/331.webp") with dissolve
            charlotte "Siapa yang mengatakan sebaliknya?"
            scene expression ("images/episode7/332.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}[mom!c]'s boobs are so firm. I never had a girlfriend with boobs like this.{/i}"
            scene expression ("images/episode7/333.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode7/334.webp") with dissolve
            charlotte "Saya tidak yakin Anda perlu menempatkan tabir surya di sana."
            scene expression ("images/episode7/335.webp") with dissolve
            toby "Jangan khawatir. Saya tahu apa yang saya lakukan."
            scene expression ("images/episode7/334.webp") with dissolve
            charlotte "Anda adalah profesional. Anda tahu yang terbaik."
            $ unlockImage(persistent.charlotte_15)
            scene expression ("images/episode7/336.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, fuck... Not now.{/i}"
            scene expression ("images/episode7/337.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I hope she doesn't notice.{/i}"
            charlotte "Saya pikir itu cukup. Anda harus mandi air dingin. Bagaimanapun, kita seharusnya tidak bermain dengan api."
            scene expression ("images/episode7/338.webp") with dissolve
            toby "Maaf untuk itu."
            scene expression ("images/episode7/339.webp") with dissolve
            charlotte "Jangan khawatir, itu normal, tapi saya masih Anda [mom], jadi itu membuatnya sangat canggung. Saya minta maaf saya menempatkan Anda dalam situasi ini."

            scene expression ("images/episode7/340.webp") with dissolve:
                xalign 1.0
                linear 10.0 xalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode7/341.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            $ unlockMemory(persistent.memory_22)
            $ renpy.end_replay()
        else:
            scene expression ("images/episode7/342.webp") with dissolve
            toby "Saya pikir saya sudah selesai."
            scene expression ("images/episode7/343.webp") with dissolve
            charlotte "Terima kasih!"
            scene expression ("images/episode7/342.webp") with dissolve
            toby "Bagaimana dengan hadiah saya."
            scene expression ("images/episode7/343.webp") with dissolve
            charlotte "Tentu saja. Saya belum melupakannya."
            scene expression ("images/episode7/344.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode7/345.webp") with dissolve
            charlotte "Terima kasih. Anda yang terbaik!"

    return

label episode7_emma_date:
    stop music fadeout 2.0
    scene expression ("images/episode7/346.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It looks it's almost 8 o'clock. I should go pick Emma up.{/i}"


    scene expression ("images/episode7/347.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/348.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/349.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/350.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/351.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/352.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/353.webp") with dissolve
    toby "Ya Tuhan, kamu sangat cantik!"
    emma "Tolong hentikan. Ini sudah keempat kalinya malam ini."
    toby "Saya tidak bisa menahannya. Jika ya, Anda."
    emma "Saya sangat senang Anda membiarkan saya memotong rambut saya."
    scene expression ("images/episode7/354.webp") with dissolve
    waitress "Ini pizza Anda."
    scene expression ("images/episode7/355.webp") with dissolve
    waitress "Appetito Buon."
    emma "Grazie."
    scene expression ("images/episode7/356_laugh.webp") with dissolve
    toby "Kapan Anda belajar berbicara bahasa Italia?"
    scene expression ("images/episode7/357_arogant.webp") with dissolve
    emma "Bisa aja. Saya berbicara seperti 6 bahasa."
    scene expression ("images/episode7/356_surprised.webp") with dissolve
    toby "Anda \ 'benar -benar omong kosong, kan?"
    scene expression ("images/episode7/357_laugh.webp") with dissolve
    emma "Tentu saja saya, tetapi saya tahu kata -kata penting dalam beberapa bahasa."
    scene expression ("images/episode7/356_smile.webp") with dissolve
    toby "Dan apa kata -kata penting itu?"
    scene expression ("images/episode7/357_laugh.webp") with dissolve
    emma "\"Thank you\", \"Enjoy your meal\", \"Love you\", \"Help\", \"Fuck off\"Dan beberapa orang lain yang tidak akan saya katakan dengan keras."
    scene expression ("images/episode7/356_laugh.webp") with dissolve
    toby "Sekarang Anda membuat saya benar -benar penasaran, apa kata -kata yang tidak akan Anda katakan dengan keras?"
    scene expression ("images/episode7/357_shy.webp") with dissolve
    emma "Anda harus memahami beberapa hal. Cindylah yang membuatku belajar semua kata -kata itu."
    scene expression ("images/episode7/356_laugh.webp") with dissolve
    toby "Anda [sister]?"
    scene expression ("images/episode7/357_shy.webp") with dissolve
    emma "Dan itu sebelum aku bertemu denganmu."
    scene expression ("images/episode7/356_smile.webp") with dissolve
    toby "Sekarang saya sangat ingin tahu mengapa itu relevan."
    scene expression ("images/episode7/357_laugh.webp") with dissolve
    emma "Yah dia bilang aku cantik dan aku pantas mendapatkan orang kaya dan mungkin orang -orang kaya itu tidak akan berada dari sekitar sini jadi aku harus belajar bahasa lain."
    scene expression ("images/episode7/356_laugh.webp") with dissolve
    toby "Jadi pada dasarnya [sister] Anda mencoba membuat Anda menjadi penggali emas."
    scene expression ("images/episode7/357_smile.webp") with dissolve
    emma "Tetapi karena kami berdua tahu Anda tidak punya uang sebanyak itu, namun saya masih mencintaimu."
    scene expression ("images/episode7/356_smile.webp") with dissolve
    toby "I think this nicest insult I've ever gotten. \"You're poor, but I still love you.\""
    scene expression ("images/episode7/357_laugh.webp") with dissolve
    emma "Anda bersikap konyol dan bermain korban biasanya adalah permainan saya."
    scene expression ("images/episode7/356_curious.webp") with dissolve
    toby "Baik, baiklah. Jadi apa kata lain?"
    scene expression ("images/episode7/357_shy.webp") with dissolve
    emma "Makanan akan menjadi dingin."
    scene expression ("images/episode7/356_laugh.webp") with dissolve
    toby "Persetan dengan makanannya. Katakan padaku kata -katanya."
    scene expression ("images/episode7/357_smile.webp") with dissolve
    emma "You just said \"fuck the food\"di tempat Italia? Bersyukur mereka tidak menendangmu."
    scene expression ("images/episode7/356_smile.webp") with dissolve
    toby "Anda akan menghindari menjawab?"
    scene expression ("images/episode7/357_shy.webp") with dissolve
    emma "Baik, tapi jika kamu tertawa, aku membunuhmu."
    scene expression ("images/episode7/356_curious.webp") with dissolve
    toby "Saya semua telinga."
    scene expression ("images/episode7/357_laugh.webp") with dissolve
    emma "Oke, jadi dia mengatakan bahwa jika saya akan bertemu dengan orang asing yang kaya, saya setidaknya harus tahu bagaimana mengatakannya ... tidak ada yang baik ... saya tidak mengatakan"
    scene expression ("images/episode7/356_normal.webp") with dissolve
    toby "Kami tidak berhubungan seks malam ini."
    scene expression ("images/episode7/357_surprised.webp") with dissolve
    emma "Jangan mengacaukan ritual suci [toby!c]."
    scene expression ("images/episode7/356_laugh.webp") with dissolve
    toby "Maaf saya pergi sedikit jauh dengan itu."
    scene expression ("images/episode7/357_laugh.webp") with dissolve
    emma "\"Fuck me hard\", \"You have a very big dick\", \"God it feels so good\", \"Yes sir\"Dan beberapa orang lain, tetapi saya berhenti sekarang, sebelum seseorang mendengar kami."
    scene expression ("images/episode7/356_laugh.webp") with dissolve
    toby "Astaga. Dia tidak hanya ingin Anda menjadi penggali emas, tetapi dia juga ingin Anda memalsukan orgasme dan memberikan harapan palsu kepada orang lain."
    scene expression ("images/episode7/356_smile.webp") with dissolve
    toby "Aku sangat beruntung aku tidak kaya, dengan cara ini aku tahu pasti penisku terasa enak dan besar."
    scene expression ("images/episode7/357_arogant.webp") with dissolve
    emma "Apakah kamu sangat yakin?"
    scene expression ("images/episode7/356_laugh.webp") with dissolve
    toby "Sekarang Anda \ 'membibit saya. Saya sarankan untuk tidak bermain dengan api atau Anda mungkin terbakar."
    scene expression ("images/episode7/357_laugh.webp") with dissolve
    emma "Saya harus. Anda tidak seharusnya mengolok -olok saya. Ingat?"
    scene expression ("images/episode7/356_laugh.webp") with dissolve
    toby "Tapi itu sangat lucu."
    scene expression ("images/episode7/356_curious.webp") with dissolve
    toby "Jadi dalam bahasa apa kita akan bercinta malam ini?"
    scene expression ("images/episode7/357_smile.webp") with dissolve
    emma "Jika kita tidak akan makan pizza ini, kita tidak akan bercinta sama sekali, atau setidaknya aku tidak akan bisa berada di atas seperti yang kamu suka, karena aku akan kelaparan."
    scene expression ("images/episode7/356_laugh.webp") with dissolve
    toby "Baik, kami makan, tapi itu omong kosong. Anda tidak selalu di atas."
    scene expression ("images/episode7/357_smile.webp") with dissolve
    emma "Tidak. Terkadang kamu meniduriku dari belakang."
    scene expression ("images/episode7/356_flirty.webp") with dissolve
    toby "Yah, bukan salahku, aku suka melihat payudaramu memantul."
    show ep7_358
    emma "Maksudmu, seperti ini?"
    toby "Ya, tapi biasanya mereka tidak tertutup."
    scene expression ("images/episode7/359.webp") with dissolve
    hide ep7_358
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode7/360.webp") with dissolve
    emma "Ya, saya pikir Anda benar. Payudara saya selalu terbuka."
    scene expression ("images/episode7/361.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    emma "Mari kita coba ini lagi."
    show ep7_362
    emma "Maksudmu seperti ini?"
    toby "Sial, aku sangat menginginkanmu."
    emma "Apa yang kamu tunggu?"
    toby "Agar Anda pergi ke kamar mandi dan menunggu saya di sana."
    scene expression ("images/episode7/363.webp") with dissolve
    hide ep7_362
    emma "Apakah kamu serius?"
    scene expression ("images/episode7/364.webp") with dissolve
    toby "Apakah saya terlihat seperti bercanda?"
    scene expression ("images/episode7/365.webp") with dissolve
    emma "Tetapi jika mereka menendang saya, Anda akan membelikan saya pizza lain."
    scene expression ("images/episode7/364.webp") with dissolve
    toby "Kata kastil goyang."
    scene expression ("images/episode7/366.webp") with dissolve
    emma "Kastil goyang ..."
    scene expression ("images/episode7/367.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should wait a few moments before going after her.{/i}"
    show screen ui_message("One minute later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode7/367_2.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck it... I can't hold it anymore.{/i}"
    scene expression ("images/episode7/368.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode7/369.webp") with dissolve
    waitress "Harap diam dan jangan tinggalkan apa pun."
    scene expression ("images/episode7/370.webp") with dissolve
    toby "Umm ... oke?"

    scene expression ("images/episode7/371.webp") with fade
    toby "Astaga. Itu sangat lucu."
    scene expression ("images/episode7/372.webp") with dissolve
    emma "Apa? Apa yang terjadi?"
    scene expression ("images/episode7/371.webp") with dissolve
    toby "Pelayan mengatakan kepada saya untuk diam dan tidak membuat kekacauan."
    label memory_23:


        scene expression ("images/episode7/373.webp") with dissolve
        emma "Saya suka kota ini."

        scene expression ("images/episode7/374.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        emma "Tapi aku lebih mencintaimu."
        scene expression ("images/episode7/375.webp") with dissolve
        show ep7_375
        $ ui.saybehavior()
        $ ui.interact()

        hide ep7_375

        scene expression ("images/episode7/376.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.2

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        toby "Aku sangat menginginkanmu."
        emma "Bawa aku. Aku sangat merindukanmu saat kamu di sini dan aku terjebak di rumah."

        scene expression ("images/episode7/377.webp") with dissolve
        show ep7_377
        emma "Ya ... ya ... puting saya sangat sensitif sekarang."
        $ ui.saybehavior()
        $ ui.interact()
        emma "Saya suka saat Anda menjilat puting saya."
        hide ep7_377

        scene expression ("images/episode7/378.webp") with dissolve
        show ep7_378
        $ ui.saybehavior()
        $ ui.interact()

        emma "Sial ... ini sangat bagus."

        hide ep7_378

        scene expression ("images/episode7/379.webp") with dissolve:
            yalign 1.0
            xalign 1.0
            linear 10.0 yalign 0.1 xalign 0.1

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        toby "Kemarilah ... Aku akan menidurimu begitu keras kamu tidak akan bisa berdiri."

        scene expression ("images/episode7/380.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        if toby_job == 0:
            emma "Pertama biarkan aku mengisap ayam besarmu itu. Saya tahu Anda menyukainya."
        else:
            toby "Tapi pertama -tama mengapa kamu tidak mengisap penisku, pelacur?"
            emma "Ya Pak!"

        scene expression ("images/episode7/381.webp") with dissolve
        show ep7_381
        $ ui.saybehavior()
        $ ui.interact()
        hide ep7_381

        scene expression ("images/episode7/382.webp") with dissolve
        show ep7_382
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck... She sucks so good. How did I manage to get a girlfriend this crazy.{/i}"
        hide ep7_382

        scene expression ("images/episode7/383.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode7/384.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        if toby_job == 0:
            emma "Berikan padaku dengan keras, cintaku. Berikan padaku [toby!c]!"
        else:
            emma "Berikan padaku dengan keras. Persetan pelacur Anda!"
            toby "Ya ... Anda adalah pelacur saya!"

        scene expression ("images/episode7/385.webp") with dissolve
        show ep7_385
        emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes, yes..."
        $ ui.saybehavior()
        $ ui.interact()
        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nRight there. Don't stop!"
        if toby_job == 1:
            toby "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYou like it, slut?"
            emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes. Yes... I do!"
        hide ep7_385

        scene expression ("images/episode7/386.webp") with dissolve
        show ep7_386
        emma "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nYes. Yesss... YESSS!"
        if toby_job == 0:
            emma "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nGive it to me. Give it to me hard!"
        else:
            emma "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nGive it to me. Fuck your slut!"
        hide ep7_386


        scene expression ("images/episode7/387.webp") with dissolve
        show ep7_387
        $ ui.saybehavior()
        $ ui.interact()
        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nHarder... Harder..."
        hide ep7_387


        scene expression ("images/episode7/388.webp") with dissolve
        show ep7_388
        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nLike that... Don't stop!"
        $ ui.saybehavior()
        $ ui.interact()
        emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nI'm very close. What about you?"
        toby "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nI'm close too."
        hide ep7_388

        scene expression ("images/episode7/389.webp") with dissolve:
            xalign 0.0
            yalign 1.0
            linear 10.0 yalign 0.2 xalign 1.0
        with flash
        with flash
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()

        $ ui.interact()

        emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes, yes, yesss... I'm cumming."

        $ unlockImage(persistent.emma_07)
        scene expression ("images/episode7/390.webp") with dissolve:
            xalign 1.0
            yalign 0.0
            linear 10.0 yalign 1.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode7/391.webp") with dissolve

        if toby_job == 0:
            toby "Sial ... itu sangat, sangat bagus!"
            emma "Aku sangat mencintaimu."
            toby "Aku mencintaimu."
        else:
            emma "Persetan denganmu."
            toby "Dan kamu hebat, pelacur kecilku!"
            emma "Aku milikmu!"

        $ unlockMemory(persistent.memory_23)
        $ renpy.end_replay()

    scene expression ("images/episode7/392.webp") with fade
    emma "Apakah ini saya atau orang -orang melihat kami?"
    toby "Mereka mungkin. Anda lupa menghidupkan mode diam."
    emma "Ketika saya kacau, sulit untuk diam."

    scene expression ("images/episode7/393.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.1

    $ ui.pausebehavior(9.3)
    emma "Ayo makan. Saya sangat lapar!"
    toby "Bon appétit."

    scene expression ("images/episode7/394.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/395.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    return


label episode7_lisa_date:
    stop music fadeout 1.0
    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode7/396.webp")
    hide screen ui_message

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Lisa told me to let her know when I'm about to leave.{/i}"


    scene expression ("images/episode7/396_texting.webp") with dissolve
    call sms_sent ("lisa", "Hey sexy. I'm leaving in 2 minutes. I'll let you know when I'm downstairs.") from _call_sms_sent_62
    call sms_incoming ("lisa", "Actually I was hoping you could come upstairs tonight.", img_icon="images/episode7/397_icon.webp", img="images/episode7/397.webp") from _call_sms_incoming_88
    call sms_sent ("lisa", "With pleasure. See you in about 20 minutes.") from _call_sms_sent_63

    hide screen message

    scene expression ("images/episode7/347.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/398.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/399.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/400.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/401.webp") with dissolve:
        xalign 0.0
        yalign 0.0
        linear 10.0 yalign 1.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/410.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/402.webp") with dissolve
    toby "Jadi? Apakah Anda akan memberi tahu saya apa kesempatan itu?"
    lisa "Tidak! Saya akan memberi tahu Anda nanti jika Anda berperilaku."
    toby "Saya akan menjadi malaikat."
    scene expression ("images/episode7/403.webp") with dissolve
    lisa "Pinky bersumpah?"
    scene expression ("images/episode7/404_laugh.webp") with dissolve
    toby "Bagus. Saya akan mencoba menjadi malaikat."
    scene expression ("images/episode7/405_smile.webp") with dissolve
    lisa "Cukup bagus untukku."
    scene expression ("images/episode7/404_curious.webp") with dissolve
    toby "Omong-omong. Dimana Lauren? Aku belum melihatnya di sekitar."
    scene expression ("images/episode7/405_shy.webp") with dissolve
    lisa "Nah, dia tidak akan pulang malam ini."
    scene expression ("images/episode7/404_smile.webp") with dissolve
    toby "Jadi, itu hanya aku dan kamu?"
    scene expression ("images/episode7/405_smile.webp") with dissolve
    lisa "Yup. Aku dan kamu sepanjang malam."
    scene expression ("images/episode7/404_laugh.webp") with dissolve
    toby "Apakah Anda mengundang saya untuk menginap?"
    scene expression ("images/episode7/405_laugh.webp") with dissolve
    lisa "Seperti yang saya katakan. Hanya jika Anda berperilaku."
    scene expression ("images/episode7/405_smile.webp") with dissolve
    lisa "Dan saya bertanya kepada Lauren apakah dia bisa pergi sehingga Anda tidak akan merasa tidak enak karena dia tidur di sofa."
    scene expression ("images/episode7/404_smile.webp") with dissolve
    toby "Ya Tuhan, kamu sangat cantik malam ini."
    scene expression ("images/episode7/405_surprised_shy.webp") with dissolve
    lisa "Umm ..."
    scene expression ("images/episode7/405_shy.webp") with dissolve
    lisa "Itu entah dari mana. Saya tidak mengharapkannya."
    scene expression ("images/episode7/404_smile.webp") with dissolve
    toby "Nah, Anda, jadi saya harus mengatakannya."
    scene expression ("images/episode7/405_smile.webp") with dissolve
    lisa "Terima kasih [toby!c]. Anda juga tidak terlalu buruk."
    scene expression ("images/episode7/404_laugh.webp") with dissolve
    toby "Saya mandi."
    scene expression ("images/episode7/405_laugh.webp") with dissolve
    lisa "Ah, benarkah? Wow, maksudku itu sesuatu. Anda benar -benar siap untuk tanggal ini."
    scene expression ("images/episode7/404_laugh.webp") with dissolve
    toby "Tentu saja. Anda pantas mendapatkan yang terbaik."
    scene expression ("images/episode7/405_happy.webp") with dissolve
    lisa "Dan seseorang yang membuatmu tersenyum.Anda membuat saya bahagia, [toby!c]. Aku sangat senang aku bertemu denganmu. Senang akhirnya memiliki seseorang yang memahami Anda."
    scene expression ("images/episode7/404_smile.webp") with dissolve
    toby "Apakah kamu jatuh cinta padaku, sayang?"
    scene expression ("images/episode7/405_laugh.webp") with dissolve
    lisa "Tidak ... tentu saja tidak! Saya tidak jatuh begitu saja."
    scene expression ("images/episode7/404_smile.webp") with dissolve
    toby "Oh, and all that \"I make you happy\"hanya ..."
    scene expression ("images/episode7/405_shy.webp") with dissolve
    lisa "Bagus. Ya, mungkin aku jatuh cinta padamu, tapi tuhan kamu sangat lucu dan pengertian dan baik. Bagaimana mungkin saya tidak!"
    scene expression ("images/episode7/404_smile.webp") with dissolve
    toby "Anda lisa yang hebat. Saya senang Anda datang ke dalam hidup saya dua bulan lalu."
    scene expression ("images/episode7/405_surprised.webp") with dissolve
    lisa "Hanya dua bulan yang berlalu sejak kita bertemu?"
    scene expression ("images/episode7/404_smile.webp") with dissolve
    toby "I thought girls count the days/months/years and so on."
    scene expression ("images/episode7/405_thinking.webp") with dissolve
    lisa "Nah jika saya melakukan beberapa matematika, itu hanya 8 minggu sehingga sebenarnya bukan dua bulan."
    scene expression ("images/episode7/404_meh.webp") with dissolve
    toby "Smartass!"
    scene expression ("images/episode7/405_laugh.webp") with dissolve
    lisa "Aku tahu. Saya cukup pintar kan?"
    scene expression ("images/episode7/404_laugh.webp") with dissolve
    toby "Anda tidak tahu. Sebenarnya Anda lakukan. Anda membual di sini."
    scene expression ("images/episode7/405_smile.webp") with dissolve
    lisa "Anda sangat konyol."
    scene expression ("images/episode7/405_happy.webp") with dissolve
    lisa "Anyway, what I wanted to say by \"only two months\"adalah rasanya seperti kita sudah saling kenal sejak selamanya. Saya sudah terbiasa dengan Anda dan kota yang rasanya selamanya sejak saya datang ke sini."
    scene expression ("images/episode7/404_laugh.webp") with dissolve
    toby "Ya, saya mengerti. Saya merasakan hal yang sama. Itu bagus!"
    scene expression ("images/episode7/405_shy.webp") with dissolve
    lisa "Anda akan membuat saya memerah."
    scene expression ("images/episode7/404_smile.webp") with dissolve
    toby "Bukan salahku kau ini lucu."

    scene expression ("images/episode7/406.webp") with dissolve
    lisa "Itu saja. Kami sedang makan sekarang, sebelum menjadi dingin."
    toby "Ya, itulah satu -satunya alasan. Bukan fakta bahwa Anda tidak tahu cara menerima pujian."
    scene expression ("images/episode7/407.webp") with dissolve
    lisa "Seorang gadis seperti saya selalu mendapat pujian, jadi saya tidak tahu apa yang Anda bicarakan."
    toby "Anda cantik."
    scene expression ("images/episode7/408.webp") with dissolve
    lisa "[toby!c] ... Berhenti mengacaukan saya!"
    toby "Sayang sekali membiarkannya menjadi dingin.Bagus. Biarkan makan. Anda telah menempatkan jiwa Anda ke dalam piring yang tampak luar biasa ini."
    lisa "Sedikit peregangan untuk mengatakan bahwa saya menempatkan jiwa saya di dalamnya, tetapi Anda semakin dekat."
    scene expression ("images/episode7/409.webp") with dissolve
    lisa "Selamat makan."
    toby "Terima kasih!"
    scene expression ("images/episode7/411.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    show screen ui_message("Some time later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/412.webp") with dissolve
    hide screen ui_message
    toby "Sial, Lisa. Jika saya tahu bahwa Anda memasak ini, saya tidak akan pernah membawa Anda keluar jika semua tanggal kami seperti ini."
    lisa "Nah, masih ada lagi. Ada makanan penutup."
    toby "Itu saja. Aku akan pulang gemuk."
    scene expression ("images/episode7/413.webp") with dissolve
    toby "Apa untuk hidangan penutup?"
    lisa "Anda akan melihat."
    scene expression ("images/episode7/414.webp") with dissolve
    lisa "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I'll be right back. I have left the dessert in the other room so you won't peek.{/i}"
    toby "Kalau begitu, aku akan menunggu di sini."
    scene expression ("images/episode7/415.webp") with dissolve
    lisa "Kembali!"
    scene expression ("images/episode7/416.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wonder what type of dessert you keep in the bedroom. I'm not going to get ahead of myself, because I told her I'll wait for her to be ready.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But, fuck... How I wish the dessert is not actual dessert.{/i}"
    with shake
    label memory_24:


        scene expression ("images/episode7/417.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Lisa just sent me a text.{/i}"
        scene expression ("images/episode7/417_texting.webp") with dissolve


        call sms_incoming ("lisa", "You can come to get your dessert.", img_icon="images/episode7/418_icon.webp", img="images/episode7/418.webp") from _call_sms_incoming_89
        scene expression ("images/episode7/417.webp") with dissolve
        hide screen message
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}You don't have to tell me twice.{/i}"

        scene expression ("images/episode7/419.webp") with dissolve
        toby "Saya suka makanan penutup."
        scene expression ("images/episode7/420.webp") with dissolve
        lisa "Anda bahkan belum mencicipinya."
        scene expression ("images/episode7/421.webp") with dissolve
        toby "Saya yakin saya akan menyukainya. Itu terlihat lezat."
        scene expression ("images/episode7/422.webp") with dissolve
        lisa "Saya tidak tahu caranya, tetapi Anda membuat saya kurang gugup."
        toby "Kenapa kamu gugup?"
        lisa "Karena saya berpikir bahwa mungkin kita bisa pindah ke langkah berikutnya."
        scene expression ("images/episode7/423.webp") with dissolve
        toby "Apa kamu yakin?"
        lisa "Ya ... Anda sangat sabar dengan saya dan saya ... Saya pikir saya sudah siap."

        scene expression ("images/episode7/424.webp") with dissolve
        show ep7_424
        $ ui.saybehavior()
        $ ui.interact()
        hide ep7_424

        scene expression ("images/episode7/425.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)

        lisa "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Can we take it slow please?{/i}"
        toby "Tentu. Anda tidak perlu merasakan tekanan apa pun."

        scene expression ("images/episode7/426.webp") with dissolve
        show ep7_426
        $ ui.saybehavior()
        $ ui.interact()
        hide ep7_426

        scene expression ("images/episode7/427.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode7/428.webp") with dissolve:
            xalign 0.0
            yalign 0.0
            linear 10.0 yalign 1.0 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()


        lisa "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I'm going to take care of you first. I hope you don't mind.{/i}"

        scene expression ("images/episode7/429.webp") with dissolve:
            xalign 1.0
            yalign 1.0
            linear 10.0 yalign 0.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        lisa "Ummm ..."

        scene expression ("images/episode7/430.webp") with dissolve
        show ep7_430
        $ ui.saybehavior()
        $ ui.interact()
        hide ep7_430

        scene expression ("images/episode7/431.webp") with dissolve
        show ep7_431
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It's a bit uncomfortable. She's using too much teeth, but I can see she's trying.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I guess she doesn't do this too often.{/i}"
        toby "Aku sangat menginginkanmu."
        hide ep7_431

        scene expression ("images/episode7/432.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.15

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        lisa "Tolong lakukan dengan lambat."
        toby "Jangan khawatir sayang. Saya akan pergi selambat yang Anda butuhkan."

        scene expression ("images/episode7/433.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.2

        $ ui.pausebehavior(9.3)

        lisa "{size=12}{color=#FDCA6E}* whimpering *{/color}{/size}\nOuchh... Mhmmm..."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Am I hurting her? She feels so tight.{/i}"
        toby "Apakah kamu baik -baik saja? Haruskah saya terus berjalan?"
        lisa "{size=12}{color=#FDCA6E}* whimpering *{/color}{/size}\nMhmmm... Yes, please do."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She looks like she's in pain.{/i}"

        scene expression ("images/episode7/434.webp") with dissolve
        show ep7_434
        $ ui.saybehavior()
        $ ui.interact()
        lisa "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nOuch... Fuck..."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I can't believe how tight her pussy is.{/i}"
        toby "Apakah Anda yakin Anda baik -baik saja?"
        lisa "Jangan khawatir, itu sakit saat Anda masuk. Anda bisa terus berjalan."
        hide ep7_434

        scene expression ("images/episode7/435.webp") with dissolve
        show ep7_435
        lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nMhmmm... "
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I need to take it slow with her. She's as tight as a virgin.{/i}"
        lisa "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes... Yesss... Yesss!"
        hide ep7_435

        scene expression ("images/episode7/436.webp") with dissolve
        show ep7_436
        lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nGod! This feels so good."
        $ ui.saybehavior()
        $ ui.interact()
        lisa "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nYou can go faster."
        hide ep7_436

        scene expression ("images/episode7/437.webp") with dissolve
        show ep7_437
        lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nMhmmm... Yes... Yes... "
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Her pussy feels so good.{/i}"
        $ ui.saybehavior()
        $ ui.interact()
        lisa "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYou're so big! It feels great!"
        hide ep7_437

        scene expression ("images/episode7/438.webp") with dissolve
        show ep7_438
        lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck... Yesss..."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It's funny to hear those words coming out of her mouth. She never curses.{/i}"
        $ ui.saybehavior()
        $ ui.interact()
        lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI'm going to cum."
        hide ep7_438

        scene expression ("images/episode7/439.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        lisa "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nYes... Yessss.... YES!"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's cumming already? {/i}"
        lisa "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nPlease keep going! Don't stop..."

        scene expression ("images/episode7/440.webp") with dissolve
        show ep7_440
        $ ui.saybehavior()
        $ ui.interact()
        lisa "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nGod! I never felt so good. Yes... Yesss..."
        lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck me [toby!c]... Fuck me..."
        hide ep7_440

        scene expression ("images/episode7/441.webp") with dissolve
        show ep7_441
        lisa "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nYes... Yesss... YES! "
        $ ui.saybehavior()
        $ ui.interact()
        lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI'm going to cum."
        toby "Aku juga akan cum!"
        lisa "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nYou can cum inside. I'm on the pill."
        hide ep7_441

        scene expression ("images/episode7/442.webp") with dissolve:
            yalign 1.0
            xalign 0.0
            linear 10.0 xalign 1.0 yalign 0.0

        lisa "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nGod. That felt so good."

        scene expression ("images/episode7/443.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.3

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        $ unlockImage(persistent.lisa_09)

        toby "Kamu datang dua kali?"
        lisa "Aku tidak tahu. Saya kira demikian."
        toby "Anda tidak tahu jika Anda datang? Apakah saya seburuk itu?"
        scene expression ("images/episode7/444.webp") with dissolve
        lisa "Tidak konyol ... Saya tahu bahwa saya datang dua kali, hanya saja itu pertama kali saya mengalami orgasme. Saya sedikit tidak yakin bagaimana rasanya."
        toby "Oh ... Saya senang mendengar bahwa saya telah menjadi orang pertama yang memberi Anda orgasme."
        toby "Saya harap saya tidak merusak saat ini, tetapi apakah Anda seorang perawan?"
        scene expression ("images/episode7/445.webp") with dissolve
        lisa "Sayangnya tidak. Saya berhubungan seks dengan mantan pacar saya. Sebenarnya saya tidak tahu apa itu, karena itu tidak terasa sebagus ini."
        lisa "Saya tidak pernah menyukai seks, karena itu tidak melakukan apa pun untuk saya, tapi malam ini, itu ... itu adalah sesuatu yang lain."
        lisa "Rasanya sangat enak!"
        toby "Saya senang Anda menyukainya."
        scene expression ("images/episode7/446.webp") with dissolve
        lisa "Saya harap saya tidak merusak momen dengan langkah saya. Tapi saya benar -benar membutuhkan Anda untuk mengambilnya lambat pada awalnya. Itu sakit!"
        toby "Jangan khawatir sayang. Kamu hebat."
        scene expression ("images/episode7/447.webp") with dissolve
        lisa "I ... {w} Aku mencintaimu [toby!c]."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Did she just said she loves me. This is the first time she used that word.{/i}"

        menu:
            "[JGR] Aku juga mencintaimu, Lisa."(csq="Lisa +1"):
                $ ep7_lisa_loveYouBack = True
                scene expression ("images/episode7/448.webp") with dissolve
                lisa "Saya sangat senang kami melakukan ini dan terima kasih telah bersabar dengan saya. Saya sangat membutuhkannya."
                toby "Saya melakukannya karena saya mencintaimu dan bagaimana perasaan Anda lebih penting daripada seks."
                scene expression ("images/episode7/449.webp") with dissolve
                lisa "Anda akan membuatku menangis."
            "Anda benar -benar sempurna."(csq="Mungkin merusak hubungan di masa depan"):

                scene expression ("images/episode7/450.webp") with dissolve
                lisa "Terima kasih!"

        $ unlockMemory(persistent.memory_24)
        $ renpy.end_replay()

    scene expression ("images/episode7/485.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    return

label episode7_lauren_date:
    stop music fadeout 2.0
    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode7/346.webp")
    hide screen ui_message

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It's getting late. I should go pick Lauren up.{/i}"


    scene expression ("images/episode7/347.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/451.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/452.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/453.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/454.webp") with dissolve:
        yalign 1.0
        xalign 1.0
        linear 10.0 xalign 0.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/455.webp") with dissolve:
        yalign 1.0
        xalign 0.0
        linear 10.0 xalign 1.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/456.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/457.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/458.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode7/459.webp") with dissolve
    lauren "Saya tidak menunjukkan kepada Anda. Setiap anak memiliki tahap itu dalam hidup mereka."
    toby "Saya belum. Saya tidak pernah melewati fase emo."
    lauren "Anda tidak tahu apa yang Anda lewatkan."
    scene expression ("images/episode7/460_laugh.webp") with dissolve
    toby "Itulah mengapa saya perlu melihatnya dengan mata sendiri."
    scene expression ("images/episode7/461_smile.webp") with dissolve
    lauren "Berjanji untuk tidak menertawakanku?"
    scene expression ("images/episode7/460_smile.webp") with dissolve
    toby "Apakah saya pernah?"
    scene expression ("images/episode7/461_laugh.webp") with dissolve
    lauren "Ya, Anda punya. Ketika burung itu buang air di pundakku."
    scene expression ("images/episode7/460_laugh.webp") with dissolve
    toby "Dalam pembelaan saya, saya tertawa hanya setelah membantu Anda membersihkan."
    scene expression ("images/episode7/461_normal.webp") with dissolve
    lauren "Saya merasa sangat buruk. Saya berusaha menjadi sangat seksi dan burung itu merusak segalanya."
    scene expression ("images/episode7/460_flirty.webp") with dissolve
    toby "Kami masih berhubungan seks."
    scene expression ("images/episode7/461_laugh.webp") with dissolve
    lauren "Di kamar mandi, karena Anda mengatakan bahwa Anda tidak mengacau."
    scene expression ("images/episode7/460_smile.webp") with dissolve
    toby "Pilihan kata -kata yang buruk, tetapi jangan hindari subjek aslinya. Saya perlu melihat emo lauren."
    scene expression ("images/episode7/461_smile.webp") with dissolve
    lauren "Bagus. Tetapi jika Anda tertawa, saya menggigit kemaluan Anda."
    scene expression ("images/episode7/460_laugh.webp") with dissolve
    toby "Baik ... malam ini kita akan melewatkan blowjob."
    scene expression ("images/episode7/461_laugh.webp") with dissolve
    lauren "Anda seharusnya mengatakan bahwa Anda tidak akan tertawa."
    scene expression ("images/episode7/460_happy.webp") with dissolve
    toby "Saya perlu melihat gambar terlebih dahulu dan kemudian saya akan memutuskan."
    scene expression ("images/episode7/462.webp") with dissolve
    lauren "Bagus."
    scene expression ("images/episode7/463.webp") with dissolve
    toby "Badass yang luar biasa. Saya mengerti mengapa Anda kehilangan keperawanan Anda hanya setelah fase itu berlalu."
    scene expression ("images/episode7/464.webp") with dissolve
    lauren "Kamu bajingan! Saya katakan itu dengan percaya diri!"
    toby "Saya tidak pernah memberi tahu siapa pun, tetapi Anda telah salah paham dengan apa yang ingin saya katakan."
    scene expression ("images/episode7/461_meh.webp") with dissolve
    lauren "Dan? Apa yang penulis coba katakan?"
    scene expression ("images/episode7/460_smile.webp") with dissolve
    toby "Anda terlihat sangat badass sehingga setiap anak laki -laki kurus terlalu takut Anda akan memecahkannya."
    scene expression ("images/episode7/461_laugh.webp") with dissolve
    lauren "Sudahkah Anda melihat foto itu? Saya adalah anak laki -laki kurus."
    scene expression ("images/episode7/460_laugh.webp") with dissolve
    toby "Saya tidak diizinkan untuk melihat di bawah leher. Saya tidak tahu berapa usia Anda di sana, tetapi saya tahu saya tidak diizinkan untuk menilai."
    scene expression ("images/episode7/461_laugh.webp") with dissolve
    lauren "Baiklah aku memberitahumu. Saya datar sebagai papan."
    scene expression ("images/episode7/460_smile.webp") with dissolve
    toby "Beruntung bagi kami berdua, Anda tidak lagi."
    scene expression ("images/episode7/461_flirty.webp") with dissolve
    lauren "Dan beruntung untukmu, aku bukan emo lagi."
    scene expression ("images/episode7/460_curious.webp") with dissolve
    toby "Kenapa begitu? Mungkin saya ingin musik inti keras di latar belakang sementara saya bercinta Anda malam ini."
    scene expression ("images/episode7/461_laugh.webp") with dissolve
    lauren "Saya tidak akan menyarankan itu. Musik itu membuatku marah dan membuatku menginginkan darah."
    scene expression ("images/episode7/460_curious.webp") with dissolve
    toby "Milikku atau milikmu?"
    scene expression ("images/episode7/461_laugh.webp") with dissolve
    lauren "Darah dari penismu. Saya akan menggigitnya sampai berdarah."
    scene expression ("images/episode7/460_yuck.webp") with dissolve
    toby "Seh!"
    scene expression ("images/episode7/461_flirty.webp") with dissolve
    lauren "Saya dapat kembali ke fase emo jika Anda mau."
    scene expression ("images/episode7/460_laugh.webp") with dissolve
    toby "Anda tahu apa yang mereka katakan. Beberapa hal dimaksudkan untuk diubah."
    scene expression ("images/episode7/461_laugh.webp") with dissolve
    lauren "Jadi tidak ada musik malam ini?"
    scene expression ("images/episode7/460_flirty.webp") with dissolve
    toby "Hanya suara pipimu yang bertepuk tangan."
    scene expression ("images/episode7/461_laugh.webp") with dissolve
    lauren "Itu suara yang luar biasa."
    scene expression ("images/episode7/460_smile.webp") with dissolve
    toby "Anda memberi tahu saya? Saya suka suara itu. Tidak sabar untuk mendengarnya malam ini."
    scene expression ("images/episode7/461_curious.webp") with dissolve
    lauren "Apakah Anda yakin akan mendengarnya malam ini?"
    scene expression ("images/episode7/460_laugh.webp") with dissolve
    toby "Yah saya melakukan semuanya dengan buku itu. Setiap kencan yang sempurna membutuhkan beberapa hal."
    scene expression ("images/episode7/461_laugh.webp") with dissolve
    lauren "Oh ... dan apa saja hal -hal itu?"
    scene expression ("images/episode7/460_smile.webp") with dissolve
    toby "Nah di situs web saya menemukan mereka mengatakan bahwa kencan yang sempurna harus dimulai dengan saya tepat waktu."
    scene expression ("images/episode7/461_happy.webp") with dissolve
    lauren "Langkah Satu Lengkap!"
    scene expression ("images/episode7/460_smile.webp") with dissolve
    toby "Kemudian mereka mengatakan bahwa beberapa gadis menyukai bunga, jadi saya membawa beberapa."
    scene expression ("images/episode7/461_curious.webp") with dissolve
    lauren "Saya pasti melewatkan bagian itu."
    scene expression ("images/episode7/460_laugh.webp") with dissolve
    toby "Kedengarannya seperti masalah Anda, tapi saya tidak terlalu tidak berperasaan."
    scene expression ("images/episode7/460_arogant.webp") with dissolve
    toby "Saya adalah bunga di antara bunga -bunga sehingga diperhitungkan."
    scene expression ("images/episode7/461_flirty.webp") with dissolve
    lauren "Dan bagaimana ... maaf saya tidak tahu bagaimana saya bisa melewatkannya."
    scene expression ("images/episode7/460_smile.webp") with dissolve
    toby "Itu mengerikan datang darimu, tapi aku akan mengabaikannya."
    scene expression ("images/episode7/461_smile.webp") with dissolve
    lauren "Saya menghargainya. Jadi apa hal berikutnya yang harus dimiliki kencan yang sempurna."
    scene expression ("images/episode7/460_happy.webp") with dissolve
    toby "Makan malam romantis dengan makanan enak di mana Anda bisa melihat matahari terbenam."
    scene expression ("images/episode7/461_smile.webp") with dissolve
    lauren "Anda dapat memeriksanya."
    scene expression ("images/episode7/460_laugh.webp") with dissolve
    toby "Tentu saja bisa. Lagipula itu ide saya."
    scene expression ("images/episode7/461_laugh.webp") with dissolve
    lauren "Ya, saya ingat ketika saya memberi tahu Anda bahwa saya tidak ingin tinggal di restoran malam ini, tetapi berjalan -jalan ke pantai dan Anda terlalu lapar sehingga kami berhenti di toko burger."
    scene expression ("images/episode7/460_smile.webp") with dissolve
    toby "Bagus. Sebagian ide saya."
    scene expression ("images/episode7/461_laugh.webp") with dissolve
    lauren "Tapi itu bagus. Apa lagi yang harus dimiliki kencan yang sempurna?"
    scene expression ("images/episode7/460_wine.webp") with dissolve
    toby "Anggur yang enak."
    scene expression ("images/episode7/460_laugh.webp") with dissolve
    toby "Sebelum Anda mengatakan sesuatu, saya memang mencoba meyakinkan Anda untuk mendapatkan soda anggur, tetapi Anda terlalu keras kepala dengan Coke Anda."
    scene expression ("images/episode7/461_sad.webp") with dissolve
    lauren "Maaf saya merusak teman kencan Anda. Yang ini ada pada saya."
    scene expression ("images/episode7/460_smile.webp") with dissolve
    toby "Tepatnya, jadi masih merupakan kencan yang sempurna di sisi saya."
    scene expression ("images/episode7/461_laugh.webp") with dissolve
    lauren "Tentu saja. Sisi saya dari tanggal itu bahkan tidak dihitung."
    scene expression ("images/episode7/460_smile.webp") with dissolve
    toby "Juga di situs web yang mereka sebutkan tentang melakukan percakapan nyata dan Anda harus mengakui, Anda tidak bosan dengan mendengarkan saya berbicara."
    scene expression ("images/episode7/461_smile.webp") with dissolve
    lauren "Ya, karena itulah percakapan itu. Anda berbicara, saya mendengarkan."
    scene expression ("images/episode7/460_flirty.webp") with dissolve
    toby "You'll talk tonight. Something like \"Yes\", \"Harder\", \"I came four times\", \"This was the best sex of my life\", \"Every other guy before you was just nothing compared to you\"."
    scene expression ("images/episode7/461_laugh.webp") with dissolve
    lauren "Hanya empat?"
    scene expression ("images/episode7/460_arogant.webp") with dissolve
    toby "Bagaimanapun, saya manusia."
    scene expression ("images/episode7/461_smile.webp") with dissolve
    lauren "Dapat dimengerti, tetapi manusia dengan sikap dewa."
    scene expression ("images/episode7/460_laugh.webp") with dissolve
    toby "Tepat."
    scene expression ("images/episode7/461_curious.webp") with dissolve
    lauren "Apakah situs web Anda mengatakan hal lain tentang kencan yang sempurna."
    scene expression ("images/episode7/460_laugh.webp") with dissolve
    toby "Yup. They said something like \"Turn your goddamn phone off\". Yang saya lakukan."
    scene expression ("images/episode7/461_curious.webp") with dissolve
    lauren "Kapan itu?"
    scene expression ("images/episode7/460_laugh.webp") with dissolve
    toby "Satu jam yang lalu ketika baterai saya mati."
    scene expression ("images/episode7/461_laugh.webp") with dissolve
    lauren "Oh ... jadi pada dasarnya itu adalah kencan yang sempurna."
    scene expression ("images/episode7/460_flirty.webp") with dissolve
    toby "Ya. Yang berarti malam ini aku akan keluar dari otakmu."
    scene expression ("images/episode7/461_sexy.webp") with dissolve
    lauren "Mengapa menunggu sampai malam ini?"
    scene expression ("images/episode7/460_curious.webp") with dissolve
    toby "Saya mendengarkan."

    label memory_25:
        if _in_replay:
            scene expression ("images/utils/black.png") with dissolve
            menu:
                "Pilih pekerjaan Anda"
                "Agen real estat":
                    $ toby_job == 0
                "Manajer klub":
                    $ toby_job == 1
        scene expression ("images/episode7/465.webp") with dissolve

        lauren "Apakah Anda ingat pertama kali kami datang ke sini. Anda ingin melakukan sesuatu dan saya menghentikan Anda?"
        toby "Ya. Kedengarannya akrab."
        lauren "Nah, katakan saja aku tidak akan menghentikanmu kali ini."

        scene expression ("images/episode7/466.webp") with dissolve
        show ep7_466
        $ ui.saybehavior()
        $ ui.interact()
        hide ep7_466

        scene expression ("images/episode7/467.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode7/468.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode7/469.webp") with dissolve:
            xalign 0.0
            yalign 1.0
            linear 10.0 xalign 1.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode7/470.webp") with dissolve
        show ep7_470
        lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes... YES!"
        $ ui.saybehavior()
        $ ui.interact()
        lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck yes!"
        hide ep7_470

        scene expression ("images/episode7/471.webp") with dissolve
        show ep7_471
        $ ui.saybehavior()
        $ ui.interact()
        lauren "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nDon't stop. Fuck me [toby!c]!"
        hide ep7_471

        scene expression ("images/episode7/472.webp") with dissolve
        show ep7_472
        lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nMhmmm... Yeah... "
        lauren "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nThis feels so good."
        $ ui.saybehavior()
        $ ui.interact()
        hide ep7_472

        scene expression ("images/episode7/473.webp") with dissolve
        show ep7_473
        lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYour cock is just perfect inside me."
        $ ui.saybehavior()
        $ ui.interact()
        hide ep7_473

        scene expression ("images/episode7/474.webp") with dissolve
        show ep7_474
        lauren "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nYes, yes, YES!"
        $ ui.saybehavior()
        $ ui.interact()
        lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck me [toby!c]!"
        lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nGive it to me hard!"
        hide ep7_474

        scene expression ("images/episode7/475.webp") with dissolve
        show ep7_475
        lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes, yes, YES!"
        $ ui.saybehavior()
        $ ui.interact()
        lauren "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nI'm cumming!"
        hide ep7_475

        scene expression ("images/episode7/476.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        lauren "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Are you close?{/i}"
        toby "Ya!"
        lauren "Saya ingin Anda cum di mulut saya."

        scene expression ("images/episode7/477.webp") with dissolve
        show ep7_477
        $ ui.saybehavior()
        $ ui.interact()
        lauren "Mhmmmm .... mmmm."
        hide ep7_477

        scene expression ("images/episode7/478.webp") with dissolve
        show ep7_478
        $ ui.saybehavior()
        $ ui.interact()
        hide ep7_478

        scene expression ("images/episode7/479.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        toby "Sial ... itu sangat intens."

        scene expression ("images/episode7/480.webp") with dissolve:
            yalign 1.0
            xalign 1.0
            linear 10.0 xalign 0.0 yalign 0.5

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        $ unlockImage(persistent.lauren_09)


        if toby_job == 0:
            lauren "Begitu banyak cum!"
        else:
            toby "Anda terlihat seperti pelacur."
            lauren "Dan Anda menyukainya kan?"
            toby "Saya menyukainya!"

        scene expression ("images/episode7/481.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        $ unlockMemory(persistent.memory_25)
        $ renpy.end_replay()

    scene expression ("images/episode7/482.webp") with dissolve
    lauren "Itu sangat bagus. Saya masih tidak tahu mengapa kita tidak melakukan ini sebelumnya."
    toby "Terutama karena kami bercinta sebelum keluar."
    lauren "Ya, kami gila seperti itu."
    scene expression ("images/episode7/483.webp") with dissolve
    lauren "Ingin datang ke tempat saya? Lisa sedang tidur di beberapa teman."
    toby "Tentu. Babak Dua?"
    lauren "Dan tiga dan empat. Anda menjanjikan saya empat orgasme."
    toby "Haha ... kesepakatan."

    scene expression ("images/episode7/484.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
