image ep9_168 = Movie(play="video/episode9/168.webm", loop = True)
image ep9_169 = Movie(play="video/episode9/169.webm", loop = True)
image ep9_170 = Movie(play="video/episode9/170.webm", loop = True)
image ep9_171 = Movie(play="video/episode9/171.webm", loop = True)
image ep9_172 = Movie(play="video/episode9/172.webm", loop = True)
image ep9_173 = Movie(play="video/episode9/173.webm", loop = True)
image ep9_253 = Movie(play="video/episode9/253.webm", image="images/episode9/253_1.webp", loop = False)
image ep9_273 = Movie(play="video/episode9/273.webm", image="images/episode9/273.webp", loop = False)
image ep9_276 = Movie(play="video/episode9/276.webm", loop = True)
image ep9_277 = Movie(play="video/episode9/277.webm", loop = True)
image ep9_278 = Movie(play="video/episode9/278.webm", loop = True)
image ep9_282 = Movie(play="video/episode9/282.webm", image="images/episode9/282.webp", loop = False)
image ep9_284 = Movie(play="video/episode9/284.webm", image="images/episode9/284.webp", loop = False)
image ep9_286 = Movie(play="video/episode9/286.webm", loop = True)
image ep9_287 = Movie(play="video/episode9/287.webm", loop = True)
image ep9_288 = Movie(play="video/episode9/288.webm", loop = True)
image ep9_289 = Movie(play="video/episode9/289.webm", loop = True)
image ep9_290 = Movie(play="video/episode9/290.webm", loop = True)

label episode9:
    $ progress = 120
    stop music fadeout 4.0
    scene expression ("images/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(2, 3) with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    show screen ui_message("Thursday") with long_dissolve
    hide screen ui_newEpisode
    $ ui.saybehavior()
    $ ui.interact()

    hide screen ui_message

    call episode9_morning from _call_episode9_morning

    call episode9_breakfast from _call_episode9_breakfast

    call episode9_garage from _call_episode9_garage

    call episode9_sport from _call_episode9_sport

    call episode9_shower from _call_episode9_shower

    call episode9_gym from _call_episode9_gym

    call episode9_cinema from _call_episode9_cinema

    if patricia_path:
        call episode9_drive_tris from _call_episode9_drive_tris
    else:
        call episode9_drive_denise from _call_episode9_drive_denise

    if emma_break == False:
        call episode9_emma from _call_episode9_emma

    return

label episode9_morning:





    scene expression ("images/episode9/001.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    denise "Pagi, sayang ... apakah kamu tidur?"
    scene expression ("images/episode9/002.webp") with dissolve
    toby "Tidak ... Saya sudah bangun selama sekitar 10 menit."
    scene expression ("images/episode9/003.webp") with dissolve
    denise "[mother] Anda menyuruh saya datang bertanya apakah Anda lapar. Dia membuat sarapan."
    scene expression ("images/episode9/002.webp") with dissolve
    toby "Sebenarnya, saya bisa makan sesuatu."
    scene expression ("images/episode9/004.webp") with dissolve
    denise "Saya suka kamar Anda. Anda melakukan pekerjaan yang sangat baik."
    scene expression ("images/episode9/005.webp") with dissolve
    toby "Anda menyukainya?"
    scene expression ("images/episode9/006_smile.webp") with dissolve
    denise "Jika saya tidak tahu lebih baik, saya pikir ini adalah apa yang Anda lakukan untuk mencari nafkah."
    scene expression ("images/episode9/007_laugh.webp") with dissolve
    toby "Tunggu saja sampai Anda melihat halaman."
    scene expression ("images/episode9/006_laugh.webp") with dissolve
    denise "Sekarang Anda hanya menyombongkan diri."
    scene expression ("images/episode9/007_smile.webp") with dissolve
    toby "Apa yang bisa saya katakan. Halaman itu adalah pièce de résistance saya."
    scene expression ("images/episode9/006_mouth.webp") with dissolve
    denise "Anda memiliki sedikit orang Italia yang terjebak di mulut Anda."
    scene expression ("images/episode9/007_laugh.webp") with dissolve
    if toby_job == 0:
        toby "Aku sangat merindukanmu, [auntie]. Aku sangat merindukanmu dan lelucon lamamu, tapi itu bahasa Prancis, bukan bahasa Italia."
    else:
        toby "Itu bahasa Prancis bukan bahasa Italia."
    scene expression ("images/episode9/006_normal.webp") with dissolve
    denise "Oh ... whoops ... aku agak merusak lelucon itu."
    scene expression ("images/episode9/007_curious.webp") with dissolve
    toby "Jadi Anda sudah melihatnya?"
    scene expression ("images/episode9/006_smile.webp") with dissolve
    denise "Tentu saja. Saya menikmati kopi pagi saya dengan [mom] di luar Anda. Dia tidak berhenti membahas betapa hebatnya dia [son]."
    scene expression ("images/episode9/007_laugh.webp") with dissolve
    toby "Dia tidak berbohong."
    scene expression ("images/episode9/006_laugh.webp") with dissolve
    denise "Yang gagal dia sebutkan adalah bahwa dia juga sedikit sombong."
    scene expression ("images/episode9/007_curious.webp") with dissolve
    toby "Apakah dia?"
    scene expression ("images/episode9/006_smile.webp") with dissolve
    denise "Dan bagaimana ..."
    scene expression ("images/episode9/006_flirty.webp") with dissolve
    denise "Dengan sikap seperti itu, di rumah dia akan memiliki semua gadis yang menjilat kakinya."
    scene expression ("images/episode9/007_flirty.webp") with dissolve
    toby "Mungkin saya harus datang mengunjungi desa Anda suatu hari nanti."
    scene expression ("images/episode9/006_normal.webp") with dissolve
    denise "Mungkin kamu harus. Saya membutuhkan pria yang percaya diri di sekitar rumah untuk memerah susu sapi saya."
    scene expression ("images/episode9/007_curious.webp") with dissolve
    toby "Tidak bisakah aku datang hanya untuk memiliki wanita menjepit kakiku?"
    scene expression ("images/episode9/006_smile.webp") with dissolve
    denise "Siapa yang mengatakan sesuatu tentang wanita?"
    scene expression ("images/episode9/007_normal.webp") with dissolve
    toby "Anda melakukannya. Hanya satu menit yang lalu."
    scene expression ("images/episode9/006_laugh.webp") with dissolve
    denise "Saya mengacu pada sapi."
    scene expression ("images/episode9/007_meh.webp") with dissolve
    toby "Oh, sial. Saya hanya ingat bahwa saya memiliki sesuatu untuk dilakukan, jadi saya kira datang ke desa Anda harus menunggu."
    scene expression ("images/episode9/006_sad.webp") with dissolve
    denise "Itu sangat menyedihkan. Saya akan membuat seorang pria keluar dari Anda di sana."
    scene expression ("images/episode9/007_normal.webp") with dissolve
    toby "Aku laki laki. Anda mengatakannya sendiri kemarin."
    scene expression ("images/episode9/006_muscle.webp") with dissolve
    denise "Aku belum melihatmu hampir telanjang, sampai sekarang. Anda pada dasarnya seorang pria di tubuh anak laki -laki."
    if denise_path:
        scene expression ("images/episode9/007_flirty.webp") with dissolve
        toby "Jika Anda melihat saya telanjang, maka saya cukup yakin Anda akan mengatakan saya adalah seorang pria di tubuh kuda jantan."
        scene expression ("images/episode9/006_flirty.webp") with dissolve
        denise "Dan apakah Anda membiarkan anak perempuan mengendarai Anda, atau apakah Anda masih perlu dijinakkan?"
        scene expression ("images/episode9/007_arogant.webp") with dissolve
        toby "Hanya yang berani yang bisa mengendarai saya karena saya bisa menjadi sedikit liar."
        scene expression ("images/episode9/006_laugh.webp") with dissolve
        denise "Astaga. Saya sekarat. Saya selalu berpikir Anda memiliki pikiran yang kotor, tetapi anak laki -laki, pikiran Anda kotor, kotor."
        scene expression ("images/episode9/007_curious.webp") with dissolve
        toby "Apa maksudmu?"
        scene expression ("images/episode9/006_smile.webp") with dissolve
        denise "Nah, [sister] Anda lebih seperti Erwin, jadi hanya benar yang harus diambil seseorang setelah [mother] Anda."
        scene expression ("images/episode9/007_curious.webp") with dissolve
        toby "Apakah Anda mengatakan [mom] memiliki pikiran kotor?"
        scene expression ("images/episode9/006_sealed.webp") with dissolve
        denise "Bibirku disegel."
        scene expression ("images/episode9/007_laugh.webp") with dissolve
        toby "Malam ini Anda sedang tidur dengan saya, karena kami memiliki banyak hal untuk dibahas."
        scene expression ("images/episode9/006_meh.webp") with dissolve
        denise "Saya tidak tahu apa yang terjadi pada generasi Anda. Kembali ketika saya masih muda, mereka setidaknya akan membelikan Anda kopi terlebih dahulu."
        scene expression ("images/episode9/007_smile.webp") with dissolve
        toby "Anda semakin tua [auntie]."
        scene expression ("images/episode9/006_laugh.webp") with dissolve
        denise "Itu akan terlihat begitu."
        scene expression ("images/episode9/007_flirty.webp") with dissolve
        if toby_job == 0:
            toby "Tapi masih cantik"
        else:
            toby "Tapi masih cantik sekali."
        scene expression ("images/episode9/006_flirty.webp") with dissolve
        denise "Saya harap Anda tidak memuji saya dengan harapan membuat saya memberi tahu Anda apa [sister] dan saya berbicara tentang tadi malam, kan?"
        scene expression ("images/episode9/007_awkward.webp") with dissolve
        toby "Berbicara tentang itu. Ya ... saya tidak bermaksud mendengar percakapan Anda. Saya baru saja melihat bahwa lampu menyala dan saya pikir itu menyenangkan untuk bergaul dengan favorit saya [aunt]."
        scene expression ("images/episode9/006_laugh.webp") with dissolve
        denise "Begitu?"
        scene expression ("images/episode9/007_smile.webp") with dissolve
        toby "Tentu saja."
        scene expression ("images/episode9/006_normal.webp") with dissolve
        denise "Masalahnya adalah, ketika Anda secara tidak sengaja mendengarkan percakapan, biasanya itu selama 10 detik ... bukan 10 menit."
        scene expression ("images/episode9/007_curious.webp") with dissolve
        toby "Um ... itu hanya 10 detik."
        scene expression ("images/episode9/006_laugh.webp") with dissolve
        denise "Pembohong! Saya melihat ketika Anda membuka pintu sedikit lagi untuk mendengar lebih baik"
        scene expression ("images/episode9/007_normal.webp") with dissolve
        toby "Bagus! Saya mendengarkan. Saya penasaran. Anda tahu saya peduli [brother]."
        scene expression ("images/episode9/008.webp") with dissolve
        denise "Dari itu saya tidak ragu."
    else:
        scene expression ("images/episode9/007_normal.webp") with dissolve
        toby "Pujian Anda paling menyakitkan."
        scene expression ("images/episode9/006_laugh.webp") with dissolve
        denise "Saya senang Anda menyukai mereka."
        scene expression ("images/episode9/008.webp") with dissolve
        denise "Saya diberitahu bahwa saya membuat pujian terbaik."

    scene expression ("images/episode9/009.webp") with dissolve
    denise "Ngomong -ngomong, saya harus pergi memberi tahu [mother] Anda bahwa Anda lapar."
    scene expression ("images/episode9/010.webp") with dissolve
    toby "Terima kasih."

    if ep8_denise_lingerie:
        toby "Ngomong -ngomong, aku sudah memberimu sesuatu kemarin. Itu ada di dalam tas merah di bawah meja."
        scene expression ("images/episode9/011.webp") with dissolve
        denise "Anda memanjakan saya sayang."
        denise "Apa yang kamu dapatkan padaku?"
        scene expression ("images/episode9/011_2.webp") with dissolve
        toby "Mengapa Anda tidak melihatnya?"
        scene expression ("images/episode9/012.webp") with dissolve
        $ unlockImage(persistent.denise_03)
        denise "Astaga! Anda gila!"
        scene expression ("images/episode9/013.webp") with dissolve
        denise "Anda membelikan saya pakaian dalam?"
        scene expression ("images/episode9/011_2.webp") with dissolve
        toby "Itu terlihat sangat bagus untukmu. Sayang sekali meninggalkannya di sana."
        scene expression ("images/episode9/013.webp") with dissolve
        denise "Terima kasih. Saya pikir Anda pantas mendapatkan ciuman untuk ini."
        scene expression ("images/episode9/014.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode9/015.webp") with dissolve
        denise "Terima kasih lagi! Anda adalah favorit saya [nephew]."
        toby "I \ m Anda satu -satunya [nephew]."
        denise "Itulah yang membuat Anda lebih istimewa."
        toby "Saya gagal memahami logikanya."
        scene expression ("images/episode9/016.webp") with dissolve
        denise "Anda akan memahami logikanya setelah Anda bertambah tua."
        scene expression ("images/episode9/017.webp") with dissolve
        toby "Apakah Anda akan mencobanya, seperti yang dilakukan Tris dengan hadiah Anda?"
        scene expression ("images/episode9/016.webp") with dissolve
        denise "Dan kemudian kembali untuk menunjukkan kepada Anda?"
        scene expression ("images/episode9/017.webp") with dissolve
        toby "Itu akan menyenangkan. Lagi pula, saya perlu melihat apakah itu terlihat sama baiknya dengan Anda seperti pada manekin."
        scene expression ("images/episode9/018.webp") with dissolve
        denise "Anda sudah melihat saya di dalamnya."
        scene expression ("images/episode9/017.webp") with dissolve
        toby "Baik, saya akan membeli lebih banyak."
        scene expression ("images/episode9/019.webp") with dissolve
        denise "Karena kelaparan pagi Anda, Anda tidak berpikir jernih. Ini adalah [aunt] Anda mencoba untuk menggoda."
        toby "Umm ..."
        scene expression ("images/episode9/020_2.webp") with dissolve
    else:
        scene expression ("images/episode9/020_1.webp") with dissolve

    denise "Sampai jumpa di lantai bawah."

    if ep8_denise_lingerie:
        scene expression ("images/episode9/021.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}[auntie!c] is right. What the fuck is wrong with me, flirting with her.{/i}"

    return

label episode9_breakfast:
    $ progress = 121

    scene expression ("images/episode9/022.webp") with dissolve
    toby "Pagi!"
    scene expression ("images/episode9/023.webp") with dissolve
    charlotte "Pagi, sayang. Bagaimana Anda tidur?"
    scene expression ("images/episode9/024.webp") with dissolve
    toby "Saya tidur nyenyak, tidak seperti [aunt] Denise."
    scene expression ("images/episode9/025.webp") with dissolve
    denise "Apa maksudmu? Menurut Anda mengapa saya tidak tidur nyenyak?"
    scene expression ("images/episode9/026.webp") with dissolve
    toby "Anda memberi tahu saya pagi ini bahwa Anda tidak bisa tidur dengan semua mendengkur Tris."
    scene expression ("images/episode9/025.webp") with dissolve
    denise "Saya tidak mengatakan hal seperti itu."
    scene expression ("images/episode9/027.webp") with dissolve
    patricia "Saya akan tetap dan mendengarkan lelucon lucu Anda, tetapi beberapa dari kami cukup pintar untuk kuliah."
    scene expression ("images/episode9/028.webp") with dissolve
    denise "Sayang, jangan dengarkan [brother] Anda. Aku tidak mengatakan apa -apa tentang mendengkur kecilmu yang lucu. Saya tidur cukup baik dengan beberapa musik di latar belakang."
    scene expression ("images/episode9/029.webp") with dissolve
    patricia "Saya tidak mendengkur!"
    scene expression ("images/episode9/028.webp") with dissolve
    denise "Aku hanya mengacaukanmu sayang. Anda tidak mendengkur. Saya tidur seperti malaikat."
    scene expression ("images/episode9/030.webp") with dissolve
    patricia "Itu benar. Nah, malaikat ini harus kuliah. Tidak seperti orang lain di ruangan ini."
    scene expression ("images/episode9/031.webp") with dissolve
    charlotte "Berhati -hatilah, sayang. Dan jangan dengarkan kata [brother] atau [aunt] Anda."
    scene expression ("images/episode9/032.webp") with dissolve
    toby "Anda yang terbaik, [auntie]."
    scene expression ("images/episode9/033.webp") with dissolve
    charlotte "Oke, kalian berdua. Anda benar -benar perlu berhenti dengan lelucon mendengkur. Minggu lalu dia memintaku untuk membawanya ke dokter untuk bajingan, karena sekarang dia pikir hidungnya terlalu besar."
    scene expression ("images/episode9/034.webp") with dissolve
    denise "Hidung kancing kecilnya terlalu besar? Apakah dia serius?"
    scene expression ("images/episode9/033.webp") with dissolve
    charlotte "Semuanya karena [toby!c]. Dia telah mengacaukannya dan sekarang dia berpikir bahwa dia mendengus karena hidungnya terlalu besar."
    scene expression ("images/episode9/035.webp") with dissolve
    denise "Astaga! Saya merasa sangat buruk sekarang. Aku seharusnya tidak menggodanya."
    scene expression ("images/episode9/036.webp") with dissolve
    charlotte "Ini baik -baik saja. Saya akan berbicara dengannya nanti, tetapi pemuda ini benar -benar perlu berhenti mengacaukannya tentang itu."
    scene expression ("images/episode9/037.webp") with dissolve
    toby "Baik ... aku akan berhenti menggodanya!"
    scene expression ("images/episode9/038_curious_2.webp") with dissolve
    denise "Ngomong -ngomong [toby!c], apakah Anda punya rencana pagi ini?"
    scene expression ("images/episode9/039_normal_1.webp") with dissolve
    toby "Tidak terlalu. Mengapa Anda bertanya?"
    scene expression ("images/episode9/038_smile_2.webp") with dissolve
    denise "Charlotte memberi tahu saya tentang sepeda Anda dan saya ingin tahu jika Anda bisa membawa saya ke garasi."
    scene expression ("images/episode9/039_smile_1.webp") with dissolve
    toby "Umm ... tentu. Tapi saya tidak punya helm, jadi jika Anda tidak takut untuk hidup di tepi saya sedikit akan membawa Anda."
    scene expression ("images/episode9/040_curious_2.webp") with dissolve
    charlotte "Ngomong -ngomong ... kapan kamu akan mendapatkan helm untuk sepeda itu? Sudah 2 bulan sudah 2 bulan dan Anda masih tidak punya helm."
    scene expression ("images/episode9/039_laugh_3.webp") with dissolve
    toby "Saya membutuhkan waktu 15 menit untuk menata rambut saya seperti ini dan Anda mengharapkan saya mengenakan helm yang akan merusaknya?"
    scene expression ("images/episode9/038_laugh_3.webp") with dissolve
    denise "Dia adalah versi Anda yang lebih muda."
    scene expression ("images/episode9/040_normal_1.webp") with dissolve
    charlotte "Dia mengalami kecelakaan."
    scene expression ("images/episode9/038_smile_3.webp") with dissolve
    denise "Itu dua tahun lalu. Saya yakin dia lebih berhati -hati sekarang."
    scene expression ("images/episode9/038_smile_2.webp") with dissolve
    denise "Dia sama sepertimu. Tampaknya adalah segalanya. Dia tidak memiliki jaket yang akan menutupi pantat gemuk itu. Dan sekarang dia mengeluh tentang punggungnya yang terluka."
    scene expression ("images/episode9/040_laugh_1.webp") with dissolve
    charlotte "Mungkin mengejutkan Anda mengetahui bahwa saya masih mengenakan pakaian semacam itu."
    scene expression ("images/episode9/038_laugh_3.webp") with dissolve
    denise "Anda perlu memeriksa akta kelahiran Anda sesekali. Anda tidak 20 tahun lagi."
    if charlotte_path:
        scene expression ("images/episode9/039_smile_1.webp") with dissolve
        toby "Mungkin, tapi dia masih terlihat lebih baik dari setengah dari gadis berusia 20 tahun yang saya kenal."
    else:
        scene expression ("images/episode9/040_smile_1.webp") with dissolve
        charlotte "Mungkin, tapi kadang -kadang saya masih mendapatkan 20 tahun."

    scene expression ("images/episode9/038_flirty_2.webp") with dissolve
    denise "Jika dia terlihat seperti dia berusia 20 -an, maka saya harus terlihat hampir legal?"
    scene expression ("images/episode9/040_curious_1.webp") with dissolve
    charlotte "Hampir tidak sah untuk apa?"
    scene expression ("images/episode9/038_laugh_2.webp") with dissolve
    denise "Sudah kubilang dia tua."
    scene expression ("images/episode9/038_normal_3.webp") with dissolve
    denise "Ini referensi porno."
    scene expression ("images/episode9/040_surprised_1.webp") with dissolve
    charlotte "Anda menonton film porno?"
    scene expression ("images/episode9/038_laugh_3.webp") with dissolve
    denise "Anda tidak?"
    scene expression ("images/episode9/040_shy_1.webp") with dissolve
    charlotte "Tidak. Saya tidak dan ini bukan subjek yang harus kita diskusikan sementara [toby!c] di sekitar."
    scene expression ("images/episode9/039_laugh_3.webp") with dissolve
    denise "Mengapa tidak? Ini tidak seperti saya tidak menontonnya."
    scene expression ("images/episode9/040_awkward_1.webp") with dissolve
    charlotte "Saya pikir Anda harus sampai ke kursus Anda."
    scene expression ("images/episode9/038_smile_3.webp") with dissolve
    denise "Saya menunggu [toby!c] untuk menyelesaikan sarapannya."
    scene expression ("images/episode9/039_laugh_1.webp") with dissolve
    if charlotte_path and denise_path:
        toby "Agak sulit untuk fokus pada makanan saya ketika dua wanita tercantik yang saya kenal sedang memperdebatkan jenis porno yang mereka tonton."
    else:
        toby "Agak sulit untuk fokus pada makanan saya ketika Anda berdua memperdebatkan jenis porno apa yang Anda tonton."
    scene expression ("images/episode9/040_awkward_2.webp") with dissolve
    charlotte "Tidak ada yang memperdebatkan apapun."
    scene expression ("images/episode9/038_flirty_3.webp") with dissolve
    denise "Sebenarnya, saya pikir kita harus berdebat sedikit lagi."
    scene expression ("images/episode9/038_flirty_2.webp") with dissolve
    denise "Jenis porno apa yang Anda tonton?"
    scene expression ("images/episode9/040_surprised_1.webp") with dissolve
    charlotte "Anda merusak [son] saya."
    scene expression ("images/episode9/038_laugh_3.webp") with dissolve
    denise "Oh tolong ... dia tahu lebih banyak tentang seks daripada gabungan kami berdua."
    scene expression ("images/episode9/040_awkward_1.webp") with dissolve
    charlotte "Saya pikir itu cukup."
    scene expression ("images/episode9/038_smile_3.webp") with dissolve
    denise "Baik ... Saya akan berubah untuk kursus saya."
    scene expression ("images/episode9/041.webp") with dissolve
    denise "[toby!c] Sayang, tolong selesaikan makanan Anda. Kita harus pergi dalam 5 menit."
    scene expression ("images/episode9/042.webp") with dissolve
    charlotte "Saya tidak tahu apa yang terjadi padanya. Dia selalu lebih terbuka pada beberapa hal, tetapi akhir -akhir ini sepertinya dia kehilangan perhatian."
    toby "Dan Anda tidak berbicara secara terbuka tentang hal -hal ini? Apakah Anda lupa bagaimana Anda menggoda saya tentang semua detail dari tanggal saya? Memang, kami tidak berbicara tentang pornografi, tetapi kami masih berbicara dengan sangat terbuka tentang seks."
    toby "Aku tidak tahu apa yang terjadi padamu sejak dia muncul."
    scene expression ("images/episode9/043.webp") with dissolve
    charlotte "Saya tidak tahu ... mungkin saya tidak ingin dia berpikir saya buruk [mother]."
    toby "Bagaimana Anda bisa menjadi buruk [mother] jika Anda berbicara secara terbuka tentang seks dengan [children] Anda."
    charlotte "Saya hanya berbicara seperti ini dengan Anda, bukan dengan Tris. Dia terlalu polos untuk itu."
    toby "Apakah dia benar -benar?"
    scene expression ("images/episode9/043_2.webp") with dissolve
    charlotte "Dia tidak pernah punya pacar. Dia terlalu tidak bersalah."
    toby "Ya, Anda benar. Dia tidak bersalah, tetapi saya tahu bahwa anak laki -laki seusia saya akan melakukan apa saja untuk seorang gadis seperti dia. Dia perlu belajar tentang hal -hal semacam ini."
    scene expression ("images/episode9/044.webp") with dissolve
    denise "Dia benar. Tris tidak dapat mengatakan kontol atau ayam tanpa memerah."
    scene expression ("images/episode9/045.webp") with dissolve
    charlotte "Anda seharusnya diubah."
    scene expression ("images/episode9/044.webp") with dissolve
    denise "Maaf, tapi subjek ini terlalu menarik."
    scene expression ("images/episode9/045.webp") with dissolve
    charlotte "Anda pergi berubah, atau saya tidak akan membiarkan [toby!c] membawa Anda dan Anda harus pergi dengan saya di mobil saya."
    scene expression ("images/episode9/044.webp") with dissolve
    denise "Anda menyebutnya mobil? Anda kebetulan mengendarai mobil ibu rumah tangga paling stereotip yang mungkin ada."
    scene expression ("images/episode9/045.webp") with dissolve
    charlotte "Sepertinya Anda memiliki alasan yang bagus untuk berubah."
    scene expression ("images/episode9/044.webp") with dissolve
    denise "Oke, Bu!"
    scene expression ("images/episode9/046_1.webp") with dissolve
    charlotte "Dia menyebut dirinya mekanik, tetapi dia bahkan tidak bisa menghargai mobil yang bagus."
    scene expression ("images/episode9/046_2.webp") with dissolve
    toby "Jangan biarkan dia sampai ke Anda."
    scene expression ("images/episode9/046_1.webp") with dissolve
    charlotte "Anda tidak berpikir mobil saya jelek, bukan?"
    scene expression ("images/episode9/047.webp") with dissolve
    toby "Nah, maukah Anda melihat waktu ... saya harus pergi!"
    scene expression ("images/episode9/048.webp") with dissolve
    charlotte "Anda dan [aunt] Anda tidak diperbolehkan lagi di mobil saya!"
    scene expression ("images/episode9/047.webp") with dissolve
    toby "Love You, [mom]!"
    scene expression ("images/episode9/048.webp") with dissolve
    charlotte "Itulah yang kamu sebut cinta? Berpihak pada musuh?"
    scene expression ("images/episode9/049.webp") with dissolve
    denise "Biarkan saya menebak. Saya musuh?"

    scene expression ("images/episode9/050.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if denise_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}That is one hot enemy.{/i}"

    scene expression ("images/episode9/051.webp") with dissolve
    charlotte "Ya, kamu!"
    scene expression ("images/episode9/052.webp") with dissolve
    denise "Musuh pergi sekarang."
    denise "Sampai jumpa lagi, Bu."
    scene expression ("images/episode9/053.webp") with dissolve
    charlotte "Apa pun ... selamat tinggal, dan sayang, tolong jaga [aunt] Anda."
    scene expression ("images/episode9/053_2.webp") with dissolve
    toby "Oke, [mom]."

    return


label episode9_garage:
    $ progress = 122

    scene expression ("images/episode9/054.webp") with fade
    denise "Itu?"
    menu:
        "{i} [JGR] Flirt {/i}"(csq="Denise +1"):
            $ denise_rel += 1
            scene expression ("images/episode9/055.webp") with dissolve
            toby "Tidak. Saya mendapatkan wanita saya di sini. Itu hanya sepeda."
            denise "Pemain."
            toby "Saya tidak."
            scene expression ("images/episode9/056.webp") with dissolve
            denise "Anda telah menjadi pemain seperti itu sehingga Anda bahkan tidak tahu cara berbicara dengan seorang wanita tanpa menggoda."
            toby "Mungkin aku ingin menggoda denganmu."
            denise "Itu lebih buruk. Tidak hanya saya jauh lebih tua dari Anda, tetapi saya juga [aunt] Anda."
            scene expression ("images/episode9/057.webp") with dissolve
            toby "Anda datang, atau Anda ingin tinggal di sini dan berdebat jika saya menggoda Anda atau tidak?"
        "{i} mainkan keren {/i}":
            toby "Anda seorang wanita. Itu benar ada binatang buas."
            scene expression ("images/episode9/056.webp") with dissolve
            denise "Saya, seorang wanita? Katakan padaku wanita apa yang akan tahu bahwa motor ini adalah 1850cc, 6 kecepatan, dan memiliki 120 tenaga kuda, lebih atau kurang."
            toby "127 hp."
            denise "Saya cukup dekat, saya katakan."
            scene expression ("images/episode9/057.webp") with dissolve
            toby "Anda datang atau Anda masih ingin membuktikan bahwa Anda tidak ada wanita?"

    scene expression ("images/episode9/058.webp") with dissolve
    denise "Anda berada di kursi saya."
    toby "Anda ingin mengemudi?"
    denise "Tidak. Saya perlu."

    scene expression ("images/episode9/059.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/060.webp") with dissolve:
        yalign 1.0
        xalign 0.0
        linear 10.0 yalign 0.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/061.webp") with dissolve:
        xalign 0.0
        linear 5.0 xalign 1.0

    $ ui.pausebehavior(4.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/062.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/063.webp") with dissolve
    denise "Terima kasih atas perjalanannya. Itu menyenangkan!"
    scene expression ("images/episode9/064.webp") with dissolve
    toby "Saya akan mengatakan bahwa kesenangan adalah milik saya, tetapi kami berdua tahu bahwa Anda menikmatinya lebih dari saya."
    scene expression ("images/episode9/065.webp") with dissolve
    denise "Sampai jumpa nanti, dan omong -omong, rantai Anda agak longgar. Itu bisa mudah patah."
    scene expression ("images/episode9/066.webp") with dissolve
    toby "Umm ... oke!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}That woman is crazy. This was the first and last time I go with her on a bike when she's driving.{/i}"
    scene expression ("images/episode9/067.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should head back home now.{/i}"

    return

label episode9_sport:
    $ progress = 123




    scene expression ("images/episode9/068.webp") with fade
    $ ui.saybehavior()
    $ ui.interact()
    label memory_30:
        if _in_replay:

            scene expression ("images/utils/black.png") with dissolve
            menu:
                "Pilih pekerjaan Anda"
                "Agen real estat":
                    $ toby_job == 0
                "Manajer klub":
                    $ toby_job == 1
        scene expression ("images/episode9/069.webp") with dissolve
        if toby_job == 0:
            toby "Apa yang Anda coba lakukan, [mom]?"
        else:
            toby "Umm ... apa yang kamu lakukan, [mom]?"
        scene expression ("images/episode9/070.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode9/070_2.webp") with dissolve
        charlotte "Apa maksudmu? Saya berolahraga."
        scene expression ("images/episode9/069.webp") with dissolve
        toby "Apakah Anda yakin bahwa latihan itu?"
        scene expression ("images/episode9/070_2.webp") with dissolve
        charlotte "Ya. Saya melihat ini di internet tempo hari dan saya ingin mencobanya."
        scene expression ("images/episode9/069.webp") with dissolve
        toby "Saya belum melihat Anda berolahraga belakangan ini. Apa yang telah terjadi?"
        scene expression ("images/episode9/071.webp") with dissolve
        charlotte "[aunt] Anda terjadi."
        toby "Anda harus sedikit lebih spesifik."
        scene expression ("images/episode9/072.webp") with dissolve
        charlotte "Jadi kemarin ketika Anda pergi bekerja, Denise dan saya pergi ke spa untuk sedikit bersantai."
        charlotte "Dan pelacur itu mengolok -olok perutku."
        scene expression ("images/episode9/073.webp") with dissolve
        toby "Uhhh ... apa dengan bahasa? Anda harus benar -benar kesal padanya."
        scene expression ("images/episode9/074.webp") with dissolve
        charlotte "Jangan berani -berani mengolok -olok saya, karena kami berada di kapal yang sama. Dia mengolok -olokmu juga."
        scene expression ("images/episode9/073.webp") with dissolve
        toby "Apa yang bisa dia ajak mengolok -olok? Saya tidak memiliki perut."
        scene expression ("images/episode9/074.webp") with dissolve
        charlotte "Tidak. Dia mengolok -olok lengan kurus Anda."
        if charlotte_path == False and not _in_replay:
            charlotte "Ngomong -ngomong, aku kembali ke sana, karena aku tidak bisa membiarkannya mengolok -olokku. Saya lebih tua [sister]."
            scene expression ("images/episode9/075.webp") with dissolve
            toby "Bersenang -senanglah. Saya pergi ke kamar saya untuk membaca."
            scene expression ("images/episode8/001.webp") with fade
            $ ui.saybehavior()
            $ ui.interact()
            show screen ui_message("After a while") with long_dissolve
            $ ui.saybehavior()
            $ ui.interact()
            hide screen ui_message
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It's really interesting to see how women think or act in different situations, but I think I should go take a shower and get ready for work.{/i}"
        else:
            charlotte "Jadi mengapa Anda tidak berubah menjadi sesuatu yang lebih nyaman dan bergabung dengan saya."
            scene expression ("images/episode9/076.webp") with dissolve
            toby "Nah ... aku akan pergi ke gym setelah bekerja. Saya benar -benar tidak berpikir pilates Anda, yoga atau apa pun yang Anda lakukan akan membantu saya."
            charlotte "Tapi bisakah Anda setidaknya membantu saya?"
            toby "Apakah saya harus menjadi bola karet Anda lagi?"
            scene expression ("images/episode9/077.webp") with dissolve
            charlotte "Mungkin? Saya memang membutuhkan pria yang kuat untuk membantu saya."
            toby "Tunggu, saya pikir saya memiliki lengan kurus?"
            scene expression ("images/episode9/078.webp") with dissolve
            charlotte "Itu pendapat Anda [aunt] Anda, bukan milik saya."
            charlotte "Bagi saya Anda adalah pemuda terkuat, paling tampan dan seksi."
            toby "Anda mencoba membuat saya terpencil."
            scene expression ("images/episode9/077.webp") with dissolve
            charlotte "Dan itu berfungsi?"
            toby "Baik ... apa yang harus saya lakukan?"
            scene expression ("images/episode9/079.webp") with dissolve
            charlotte "Pertama saya harus menyelesaikan peregangan saya."
            scene expression ("images/episode9/080.webp") with dissolve
            toby "Itulah yang kamu lakukan? Anda sedang peregangan?"
            scene expression ("images/episode9/081.webp") with dissolve
            charlotte "Tepat. Peregangan adalah bagian terpenting."
            scene expression ("images/episode9/082.webp") with dissolve
            toby "Saya tidak ragu tentang itu."
            if toby_job == 0:
                toby "Jangan ragu untuk meregangkan sebanyak yang Anda butuhkan."
            else:
                toby "Saya juga mengatakan itu penting bagi saya bahwa Anda meregangkan."
            scene expression ("images/episode9/083.webp") with dissolve
            charlotte "Mhmmm."
            scene expression ("images/episode9/084.webp") with dissolve
            toby "Sekarang apa?"
            charlotte "Sekarang Anda membantu saya menyelesaikan peregangan."
            scene expression ("images/episode9/085.webp") with dissolve
            charlotte "Cobalah untuk tidak mengangkat kaki saya terlalu tinggi karena saya mungkin jatuh."
            toby "Apakah Anda benar -benar membutuhkan saya untuk ini?"
            scene expression ("images/episode9/086.webp") with dissolve
            charlotte "Sekarang kaki lainnya."
            toby "Saya merasa sedikit digunakan."
            scene expression ("images/episode9/087.webp") with dissolve
            charlotte "Mengapa Anda selalu harus mengatakan sesuatu yang negatif? Tidak bisakah Anda menikmati menghabiskan waktu dengan indahnya [mother]?"
            scene expression ("images/episode9/088.webp") with dissolve
            charlotte "Sekarang saya akan melakukan beberapa crunch."
            toby "Berapa banyak?"
            charlotte "30 akan menyenangkan. Tapi saya bukan usia 20 -an, jadi mari kita lihat berapa banyak yang bisa saya lakukan."
            scene expression ("images/episode9/089.webp") with dissolve
            toby "Berhentilah mengeluh tentang usia Anda. Ini tidak seperti Anda berusia 60 tahun."
            scene expression ("images/episode9/090.webp") with dissolve
            charlotte "Saya lebih dekat ke 60 dari saya hingga 20, jadi aman untuk mengatakan bahwa saya sudah tua."
            scene expression ("images/episode9/089.webp") with dissolve
            toby "Namun Anda terlihat lebih baik dari kebanyakan gadis berusia 20 tahun."
            scene expression ("images/episode9/090.webp") with dissolve
            charlotte "Saya pasti telah melakukan sesuatu yang salah dengan Anda karena Anda jelas lebih menyukai wanita yang lebih tua daripada anak perempuan seusia Anda."
            scene expression ("images/episode9/089.webp") with dissolve
            toby "Sebenarnya, saya tidak menganggap usia sangat penting bagi saya."
            scene expression ("images/episode9/090.webp") with dissolve
            toby "Maksudku, aku tidak peduli berapa umurnya atau muda, selama dia panas dan pintar. Saya benar -benar berpikir sikapnya lebih penting daripada penampilannya."
            scene expression ("images/episode9/089.webp") with dissolve
            charlotte "Itu tidak keluar dengan benar. Saya sangat berharap Anda peduli betapa muda dia."
            scene expression ("images/episode9/090.webp") with dissolve
            toby "Ha ... ha ... sangat lucu! Anda melewatkan bagian penting."
            scene expression ("images/episode9/089.webp") with dissolve
            charlotte "Tidak, saya tidak. Aku hanya suka mengacaukanmu. Tapi saya masih berpikir itu aneh bagi pria muda yang tampan seperti Anda untuk tertarik pada wanita yang lebih tua."
            scene expression ("images/episode9/090.webp") with dissolve
            toby "Mengapa itu aneh?"
            scene expression ("images/episode9/089.webp") with dissolve
            charlotte "Yah, mari kita jujur. Gadis yang lebih muda terlihat lebih baik. Seorang wanita yang lebih tua memiliki kerutan, pantatnya semakin rata dan payudara mereka semakin saggier, sementara gadis -gadis yang lebih muda ... yah, itu cerita yang berbeda."
            scene expression ("images/episode9/090.webp") with dissolve
            toby "Ya, saya kira, tapi ada wanita seperti Anda yang telah merawat diri mereka sendiri. Mereka berolahraga secara teratur, mereka merawat kulit mereka dengan baik, dan mari kita hadapi itu ... wanita yang lebih tua memiliki payudara yang jauh lebih besar."
            scene expression ("images/episode9/089.webp") with dissolve
            charlotte "Ngomong -ngomong, apakah Anda sudah menghitung crunch saya?"
            scene expression ("images/episode9/090.webp") with dissolve
            toby "Yup. Anda hanya pada 7."
            scene expression ("images/episode9/089.webp") with dissolve
            charlotte "Sial ... aku benci Denise."
            scene expression ("images/episode9/090.webp") with dissolve
            toby "Mengapa?"
            scene expression ("images/episode9/089.webp") with dissolve
            charlotte "Karena saya benar -benar tidak suka berolahraga, tetapi saya tidak bisa membiarkannya mengolok -olok perut saya."
            scene expression ("images/episode9/090.webp") with dissolve
            toby "Anda adalah wanita paling cantik persis seperti Anda. Saya tidak mengerti mengapa Anda bahkan repot -repot dengan ini."
            scene expression ("images/episode9/089.webp") with dissolve
            charlotte "And you're as bad with your words as your [father]. I didn't say I was ugly. I said I was fat and your answer was: \"You're beautiful the way you are\"."
            scene expression ("images/episode9/090.webp") with dissolve
            toby "Tapi Anda tidak gemuk."
            scene expression ("images/episode9/089.webp") with dissolve
            charlotte "Terlambat."
            scene expression ("images/episode9/090.webp") with dissolve
            charlotte "Berapa banyak sekarang?"
            scene expression ("images/episode9/089.webp") with dissolve
            toby "Sebelas."
            scene expression ("images/episode9/091.webp") with dissolve
            charlotte "Itu saja ... saya tidak tahan lagi."
            toby "Ayo, 4 lagi."
            charlotte "Saya pikir Anda bilang saya tidak gemuk, jadi mengapa saya perlu melakukan 4 lagi?"
            toby "Anda meminta saya untuk membantu Anda. Jadi berhentilah mengeluh dan terus berjalan. Jika Anda tidak, saya akan naik ke atas."
            scene expression ("images/episode9/090.webp") with dissolve
            charlotte "{size=12}{color=#FDCA6E}* mocking *{/color}{/size}\n{i}I'Ll Go UpStAiRS.{/i}"
            scene expression ("images/episode9/089.webp") with dissolve
            toby "Kemiripan antara Anda dan Tris luar biasa."
            scene expression ("images/episode9/090.webp") with dissolve
            charlotte "Apakah dia mengejek Anda dengan cara yang sama seperti saya?"
            scene expression ("images/episode9/089.webp") with dissolve
            toby "Saya dikelilingi oleh pengganggu."
            scene expression ("images/episode9/090.webp") with dissolve
            charlotte "Pengganggu ini perlu tahu berapa banyak crunch yang tersisa."
            scene expression ("images/episode9/089.webp") with dissolve
            toby "Satu lagi."
            scene expression ("images/episode9/090.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode9/091.webp") with dissolve
            charlotte "Saya sekarat."
            scene expression ("images/episode9/092.webp") with dissolve
            toby "Jadi? Apa selanjutnya?"
            scene expression ("images/episode9/093.webp") with dissolve
            charlotte "Sekarang Anda membawakan saya sebotol air."
            scene expression ("images/episode9/094.webp") with dissolve
            toby "Saya merasa bahwa Anda menggunakan saya."
            scene expression ("images/episode9/095.webp") with dissolve
            charlotte "Anda terlalu dramatis. Hanya karena [mother] Anda meminta Anda dengan ramah untuk membantunya dalam latihan dan membawakannya air?"
            scene expression ("images/episode9/096.webp") with dissolve
            toby "Dan masih baru jam 11 pagi."
            scene expression ("images/episode9/097.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode9/098.webp") with dissolve
            charlotte "Sekarang, Anda perlu membantu saya mendorong kaki saya kembali."
            scene expression ("images/episode9/099.webp") with dissolve
            toby "Seperti ini?"
            charlotte "Tepat."
            toby "Dan apa yang akan Anda lakukan sejak saya melakukan semua pekerjaan?"
            charlotte "Nikmati."
            scene expression ("images/episode9/100.webp") with dissolve
            toby "Melihat saya di atas?"
            scene expression ("images/episode9/101.webp") with dissolve
            charlotte "Maksud saya menikmati latihan ini. Anda memutar kata -kata saya."
            scene expression ("images/episode9/100.webp") with dissolve
            toby "Saya hanya mengatakannya seperti itu."
            scene expression ("images/episode9/101.webp") with dissolve
            charlotte "Jadi itu adalah imajinasi saya bahwa Anda sedikit sesat?"
            scene expression ("images/episode9/100.webp") with dissolve
            toby "Sepertinya itu."
            scene expression ("images/episode9/101.webp") with dissolve
            charlotte "Bad saya kalau begitu. Tetapi untuk menjawab pertanyaan Anda, saya suka ketika Anda berada di atas."
            scene expression ("images/episode9/100.webp") with dissolve
            toby "..."
            scene expression ("images/episode9/101.webp") with dissolve
            charlotte "Anda bisa lebih sulit. Dorong lebih keras."
            scene expression ("images/episode9/100.webp") with dissolve
            toby "Seperti ini?"
            scene expression ("images/episode9/101.webp") with dissolve
            charlotte "{size=12}{color=#FDCA6E}* moaning slightly *{/color}{/size}\n{i}Mhmmm.{/i}"
            scene expression ("images/episode9/100.webp") with dissolve
            charlotte "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\n{i}Yes... Just like that.{/i}"
            scene expression ("images/episode9/103.webp") with dissolve
            toby "Ummm ..."
            scene expression ("images/episode9/102.webp") with dissolve
            charlotte "Ya Tuhan ... Saya berharap Anda bisa melihat wajah Anda. Itu tak ternilai harganya."
            charlotte "Apa yang terjadi, sayang? Apakah pikiran Anda berkeliaran?"
            scene expression ("images/episode9/100.webp") with dissolve
            toby "Tidak ... Saya tidak tahu apa yang Anda bicarakan."
            scene expression ("images/episode9/101.webp") with dissolve
            charlotte "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\n{i}Yes... You're doing it right.{/i}"
            scene expression ("images/episode9/100.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}OK, I see how it is...Well, two can play this game.{/i}"
            scene expression ("images/episode9/101.webp") with dissolve
            toby "Anda menyukainya? Anda suka ketika saya mendorong sepanjang jalan?"
            scene expression ("images/episode9/100.webp") with dissolve
            charlotte "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\n{i}Yes! It feels so good. I love it.{/i}"
            scene expression ("images/episode9/101.webp") with dissolve
            toby "Saya bisa pergi lebih keras jika Anda pikir Anda bisa menerimanya."
            scene expression ("images/episode9/100.webp") with dissolve
            charlotte "Oh, saya bisa menerimanya, tetapi sayangnya untuk Anda, saya hanya perlu melakukan 10 ini, jadi mungkin lain kali."
            scene expression ("images/episode9/101.webp") with dissolve
            toby "Ya ... mungkin lain kali."
            scene expression ("images/episode9/105.webp") with dissolve
            charlotte "Apakah Anda siap untuk latihan berikutnya?"
            toby "Pukul aku."
            scene expression ("images/episode9/106.webp") with dissolve
            charlotte "Saya harus tetap seperti ini selama 30 detik, tetapi Anda harus membantu saya dan memastikannya sesegera mungkin."
            scene expression ("images/episode9/107.webp") with dissolve
            toby "Seperti ini?"
            charlotte "Itu lurus?"
            scene expression ("images/episode9/108.webp") with dissolve
            toby "Setinggi mungkin."
            scene expression ("images/episode9/109.webp") with dissolve
            charlotte "Apa yang tidak benar?"
            scene expression ("images/episode9/110.webp") with dissolve
            toby "Nah, di sini agak bergelombang."
            scene expression ("images/episode9/111.webp") with dissolve
            charlotte "Saya tidak akan mengatakan itu hanya sedikit, tetapi Anda memiliki pandangan yang lebih baik."
            scene expression ("images/episode9/112.webp") with dissolve
            charlotte "Sekarang pergi ke sisi lain, tetapi kali ini cobalah untuk menjaga diri Anda sendiri."
            toby "Tentu saja saya akan ... apa maksud Anda? Saya seorang profesional."
            scene expression ("images/episode9/113.webp") with dissolve
            charlotte "Jadi? Bagaimana sekarang?"
            toby "Baik itu masih bergelombang."
            charlotte "Di tempat yang sama?"
            toby "Lebih baik tunjukkan padamu. Saya tidak baik dengan kata -kata."
            scene expression ("images/episode9/114.webp") with dissolve
            toby "Di sini."
            scene expression ("images/episode9/114_1.webp") with dissolve
            charlotte "Saya tidak yakin saya mengerti di mana. Bisakah Anda memeras sedikit."
            scene expression ("images/episode9/114.webp") with dissolve
            $ ui.pausebehavior(0.2)
            scene expression ("images/episode9/115.webp") with dissolve
            charlotte "{size=12}{color=#FDCA6E}* moaning slightly *{/color}{/size}\n{i}Oh... There?{/i}"
            toby "Ya..."
            scene expression ("images/episode9/116.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode9/117.webp") with dissolve
            charlotte "Saya pikir ada satu tempat bergelombang lagi."
            scene expression ("images/episode9/118.webp") with dissolve
            toby "Anda masih memiliki 10 detik tersisa."
            scene expression ("images/episode9/117.webp") with dissolve
            charlotte "Ya, tapi terlalu panas untuk Anda."
            scene expression ("images/episode9/118.webp") with dissolve
            toby "Hanya untuk saya?"
            scene expression ("images/episode9/119.webp") with dissolve
            charlotte "Mungkin ... tapi dalam kasus Anda itu sedikit lebih jelas."
            scene expression ("images/episode9/120.webp") with dissolve
            toby "[mom!c] ... apa yang kamu lakukan?"
            charlotte "Saya tidak yakin. Saya membuat semuanya bahkan. Hanya adil bagi saya untuk membalas budi."
            scene expression ("images/episode9/121.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck... She's so close. It almost feels right to kiss her right now. To kiss her beautiful lips.{/i}"
            $ unlockImage(persistent.charlotte_17)
            scene expression ("images/episode9/122.webp") with dissolve
            charlotte "Ummm ... Saya tidak berpikir ini adalah ide yang sangat bagus, [toby!c]. Haruskah kita berhenti?"
            toby "Saya tidak yakin saya mau. Apakah Anda ingin berhenti?"
            charlotte "{size=12}{color=#FDCA6E}* softly speaking *{/color}{/size}\n{i}I don't know. It feels wrong to stop, but it feels wrong to continue, too.{/i}"
            $ unlockMemory(persistent.memory_30)
        $ renpy.end_replay()

        scene expression ("images/episode9/123.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        stop music fadeout 1.0
        scene expression ("images/episode9/124.webp") with dissolve
        patricia "Apa yang kalian lakukan?"
        scene expression ("images/episode9/125.webp") with dissolve
        charlotte "Halo sayang. [brother] Anda membantu saya dengan beberapa latihan."
        scene expression ("images/episode9/124.webp") with dissolve
        if patricia_path:
            patricia "Bisakah saya bergabung dengan Anda?"
            scene expression ("images/episode9/125.webp") with dissolve
            charlotte "Anda bisa bergabung dengan saya, karena [toby!c] akan mandi."

        scene expression ("images/episode9/126.webp") with dissolve
        patricia "Membosankan."

        scene expression ("images/episode9/127_1.webp") with dissolve
        if patricia_path:
            charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I think you should go take a cold shower.{/i}"
        else:
            charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Umm... Make sure your shower is cold.{/i}"
        scene expression ("images/episode9/127_2.webp") with dissolve
        toby "Saya pikir Anda benar."
        scene expression ("images/episode9/128.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
    return


label episode9_shower:
    $ progress = 124

    scene expression ("images/episode9/130.webp") with fade
    if charlotte_path:
        if toby_job == 0:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the hell was that?{/i}"
        else:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the fuck was that?{/i}"

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}If Tris hadn't come in the room, was I going to kiss my [mother]?{/i}"
        scene expression ("images/episode9/131.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And am I crazy thinking that she wanted it to happen?{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is my [mother] really attracted to me? And am I actually attracted to her?{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yeah, she's beautiful and I told her so. But for the first time I actually felt like I wanted to kiss her.{/i}"
        scene expression ("images/episode9/132.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why did she say that it felt wrong to stop? Was she really talking about a kiss or did I misunderstand?{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But she also said it would also be wrong to continue...which means she was totally talking about a kiss, because it's wrong to kiss your [mother].{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Or, is it?{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And fuck... Her hand was on my cock.{/i}"
    else:
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode9/131.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()

    play sound "audio/fx/Cell Phone Ring Sound Effect - Free Sound Effects.mp3"
    if toby_job == 0:
        scene expression ("images/episode9/133.webp") with dissolve
    else:
        scene expression ("images/episode9/134.webp") with dissolve
    play sound "audio/fx/Cell Phone Ring Sound Effect - Free Sound Effects.mp3"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Ugh...this is a terrible time to call me.{/i}"

    scene expression ("images/episode9/132.webp") with dissolve

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'll call her when I'm done.{/i}"
    play sound "audio/fx/Cell Phone Ring Sound Effect - Free Sound Effects.mp3"
    if toby_job == 0:
        scene expression ("images/episode9/133.webp") with dissolve
    else:
        scene expression ("images/episode9/134.webp") with dissolve
    play sound "audio/fx/Cell Phone Ring Sound Effect - Free Sound Effects.mp3"
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode9/135.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fine... You win.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see what's so important that she called me twice.{/i}"

    scene expression ("images/episode9/136.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Looks like she sent me a text. Wonder what this is all about.{/i}"

    scene expression ("images/episode9/136_texting.webp") with dissolve
    if toby_job == 0:

        call sms_incoming ("darlene", "Morning [toby!c]. I wanted to say that you can stay home today.") from _call_sms_incoming_117
        call sms_sent ("darlene", "OK... Is everything alright?") from _call_sms_sent_87
        call sms_incoming ("darlene", "Yes... Everything is fine, it's just that after what happened yesterday, I think it's better for you to take a day off.") from _call_sms_incoming_118
        call sms_sent ("darlene", "Since you brought it up...What actually happened?") from _call_sms_sent_88
        if darlene_path:

            call sms_incoming ("darlene", "I think we both know what happened.") from _call_sms_incoming_119
            call sms_sent ("darlene", "Well, only sort of. I know you gave me a blowjob, but the thing is I don't understand why. What's with that chocolate?") from _call_sms_sent_89
            call sms_incoming ("darlene", "I think you deserve an explanation. Unfortunately I can't give it to you over the phone, but I want to apologize for what happened.") from _call_sms_incoming_120
            call sms_sent ("darlene", "You have nothing to apologize for. It's not like you had any control and if what you said was true, we both wanted that.") from _call_sms_sent_90
            call sms_incoming ("darlene", "That's exactly what scares me. The fact that we both wanted that.") from _call_sms_incoming_121
            call sms_sent ("darlene", "This is why you're telling me to stay home?") from _call_sms_sent_91
            call sms_incoming ("darlene", "Yes... I need to sort my head.") from _call_sms_incoming_122
            call sms_incoming ("darlene", "By the way, how are you feeling? Did you have any trouble sleeping?") from _call_sms_incoming_123
            call sms_sent ("darlene", "Not really. I've been really thirsty, but besides that, I'm fine.") from _call_sms_sent_92
            call sms_incoming ("darlene", "I see. Ok, Then. See you tomorrow?") from _call_sms_incoming_124
            call sms_sent ("darlene", "If you think that's ok, sure.") from _call_sms_sent_93
            call sms_incoming ("darlene", "Yes, it should be fine.") from _call_sms_incoming_125
            call sms_incoming ("darlene", "Have a good day, [toby!c].") from _call_sms_incoming_126
            call sms_sent ("darlene", "Yeah... You too.") from _call_sms_sent_94
        else:

            call sms_incoming ("darlene", "You deserve an explanation, but I can't give you too much detail over the phone, but I'm sorry for how I behaved.") from _call_sms_incoming_127
            call sms_sent ("darlene", "Ummm...") from _call_sms_sent_95
            call sms_incoming ("darlene", "The thing is, I ate something I shouldn't have and it messed with my brain so I'm sorry about that.") from _call_sms_incoming_128
            call sms_sent ("darlene", "But you're feeling okay now?") from _call_sms_sent_96
            call sms_incoming ("darlene", "I do feel better, but I still need to recover so that's why I'm giving you the day off.") from _call_sms_incoming_129
            call sms_sent ("darlene", "I hope you get well. And as for yesterday, you have nothing to worry about.") from _call_sms_sent_97
            call sms_incoming ("darlene", "Thank you for understanding, [toby!c].") from _call_sms_incoming_130
            call sms_incoming ("darlene", "Have a good day and see you tomorrow.") from _call_sms_incoming_131
            call sms_sent ("darlene", "See you tomorrow.") from _call_sms_sent_98
    else:


        if katrina_path:

            call sms_incoming ("katrina", "Answer the fucking phone when I call you. You little shit.") from _call_sms_incoming_132
            call sms_sent ("katrina", "I was in the shower, getting ready to come to work.") from _call_sms_sent_99
            call sms_sent ("katrina", "So? What's so important?") from _call_sms_sent_100
            call sms_incoming ("katrina", "I see you haven't fixed your attitude yet.") from _call_sms_incoming_133
            call sms_sent ("katrina", "No. I haven't! You fucking drugged me.") from _call_sms_sent_101
            call sms_incoming ("katrina", "Boo hoo... So what? You're still crying because you licked my pussy?") from _call_sms_incoming_134
            call sms_sent ("katrina", "I'm really not in the mood.") from _call_sms_sent_102
            call sms_incoming ("katrina", "Then you better not step in my office until you realize that it was something you wanted.") from _call_sms_incoming_135
            call sms_sent ("katrina", "What the fuck are you talking about? I didn't want that.") from _call_sms_sent_103
            call sms_incoming ("katrina", "Stop lying to yourself. That's not how it works.") from _call_sms_incoming_136
            call sms_sent ("katrina", "Then how do they work?") from _call_sms_sent_104
            call sms_incoming ("katrina", "I can't say much over the phone, but maybe you'd do almost anything to fuck me and in that moment you thought that if you licked my pussy you'd end up fucking me.") from _call_sms_incoming_137
            call sms_sent ("katrina", "Whatever.") from _call_sms_sent_105
            call sms_incoming ("katrina", "Ha... You really think you can fuck me just like that?") from _call_sms_incoming_138
            call sms_incoming ("katrina", "Keep dreaming bitch.") from _call_sms_incoming_139
            call sms_sent ("katrina", "You done? Slut!") from _call_sms_sent_106
            call sms_incoming ("katrina", "You like to talk dirty?") from _call_sms_incoming_140
            call sms_sent ("katrina", "This isn't dirty talk. You are actually a fucking slut.") from _call_sms_sent_107
            call sms_incoming ("katrina", "Don't come to the club today, or else...", img_icon="images/episode9/137_icon.webp", img="images/episode9/137.webp") from _call_sms_incoming_141
            call sms_sent ("katrina", "Keep practicing, because I don't want you to bite my cock when you suck it.") from _call_sms_sent_108
            call sms_incoming ("katrina", "Try not to jerk off on this photo.") from _call_sms_incoming_142
            call sms_sent ("katrina", "Don't you worry. I'll keep my cum for your pretty face.") from _call_sms_sent_109
            call sms_incoming ("katrina", "And I thought you wanted me to swallow.") from _call_sms_incoming_143
            call sms_sent ("katrina", "You don't deserve my cum in your mouth, slut!") from _call_sms_sent_110
            call sms_incoming ("katrina", "Fuck you.") from _call_sms_incoming_144
            call sms_sent ("katrina", "You too.") from _call_sms_sent_111
        else:

            call sms_incoming ("katrina", "When I call, you answer.") from _call_sms_incoming_145
            call sms_sent ("katrina", "I was in the shower, getting ready for work.") from _call_sms_sent_112
            call sms_incoming ("katrina", "I'm not in the mood for boring people. Don't come in today.") from _call_sms_incoming_146
            call sms_sent ("katrina", "What the fuck happened?") from _call_sms_sent_113
            call sms_incoming ("katrina", "You're boring. I really wanted to have my pussy licked yesterday.") from _call_sms_incoming_147
            call sms_sent ("katrina", "Sorry, but that's not how things work.") from _call_sms_sent_114
            call sms_incoming ("katrina", "It could have.") from _call_sms_incoming_148
            call sms_sent ("katrina", "What do you mean?") from _call_sms_sent_115
            call sms_incoming ("katrina", "I mean the next time I offer you chocolate, you accept it.") from _call_sms_incoming_149
            call sms_sent ("katrina", "Sorry, not going to happen.") from _call_sms_sent_116
            call sms_incoming ("katrina", "Whatever.") from _call_sms_incoming_150
            call sms_sent ("katrina", "So, I'm not coming to work today?") from _call_sms_sent_117
            call sms_incoming ("katrina", "Nope. See you tomorrow.") from _call_sms_incoming_151
            call sms_sent ("katrina", "Okay...") from _call_sms_sent_118

    scene expression ("images/episode9/138.webp") with dissolve
    hide screen message
    if toby_job == 0:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Well, that was a strange conversation.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}The fuck is her problem?{/i}"
    scene expression ("images/episode9/139.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Whatever. At least I have the day off.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}That means I can go to gym early today. I really want to workout.{/i}"

    return


label episode9_gym:
    $ progress = 125
    stop music fadeout 1.0
    show screen ui_message("Some time later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode9/140.webp") with dissolve
    hide screen ui_message
    toby "Selamat tinggal, [mom]! Sampai jumpa lagi."
    scene expression ("images/episode9/141.webp") with dissolve
    charlotte "Anda akan bekerja dengan berpakaian seperti itu?"
    scene expression ("images/episode9/140.webp") with dissolve
    toby "Saya pergi hari ini, jadi saya pergi ke gym. Harus mengerjakan lengan kurus ini!"
    scene expression ("images/episode9/141.webp") with dissolve
    charlotte "Oh, oke ... bersenang -senang!"
    scene expression ("images/episode9/140.webp") with dissolve
    toby "Terima kasih!"


    scene expression ("images/episode9/142.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/143.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/144.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/145.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/146.webp") with dissolve:
        xalign 1.0
        yalign 1.0
        linear 10.0 xalign 0.0 yalign 0.0


    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/147.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/148.webp") with dissolve
    if sheila_path:
        sheila "Hai seksi ... belum pernah melihatmu cukup lama. Saya mulai berpikir Anda tidak menyukai saya lagi."
        toby "Aku belum menjadi gila."
        sheila "Bahkan bukan untukku?"
        if toby_job == 0:
            toby "Nah, Anda membuat saya gila. Tapi hanya sedikit."
        else:
            toby "Pantatmu membuatku gila. Tapi hanya sedikit."

        scene expression ("images/episode9/149_flirty.webp") with dissolve
        sheila "Hanya sedikit?"
        scene expression ("images/episode9/150_smile.webp") with dissolve
        toby "Tentu saja. Anda tidak mengira saya akan menjadi gila begitu saja, bukan?"
        scene expression ("images/episode9/149_smile.webp") with dissolve
        sheila "Tidak ... tentu saja tidak. Saya kira saya harus berusaha lebih keras."
        scene expression ("images/episode9/150_laugh.webp") with dissolve
        toby "Jangan mengecewakan saya."
        scene expression ("images/episode9/149_scout.webp") with dissolve
        sheila "Pramuka kehormatan."
        scene expression ("images/episode9/150_curious.webp") with dissolve
        toby "Saya tidak pernah membayangkan Anda sebagai Girl Scout."
        scene expression ("images/episode9/149_smile.webp") with dissolve
        sheila "Saya tidak pernah memberi tahu Anda tentang fase pramuka perempuan saya?"
        scene expression ("images/episode9/150_flirty.webp") with dissolve
        toby "Sejujurnya, kami tidak banyak bicara ketika kami bertemu."
        scene expression ("images/episode9/149_flirty.webp") with dissolve
        sheila "Saya berbicara. Anda yang memiliki mata tertutup dan mulut terbuka."
        scene expression ("images/episode9/150_laugh.webp") with dissolve
        toby "I don't think that \"Yes\", \"Harder\", \"Don't stop\", \"You have the biggest dick ever\", dianggap berbicara."
        scene expression ("images/episode9/149_laugh.webp") with dissolve
        sheila "\"You have the biggest dick\"? Saya gagal mengingat mengatakan itu, tapi apa pun."
        scene expression ("images/episode9/150_smile.webp") with dissolve
        toby "Mungkin bukan kata -kata itu, tapi itu tersirat."
        scene expression ("images/episode9/149_flirty.webp") with dissolve
        sheila "I think it was more like \"Your big dick feels so good in my tight pussy\"."
        scene expression ("images/episode9/150_horny.webp") with dissolve
        toby "Anda membuat saya terangsang sekarang."
        scene expression ("images/episode9/149_laugh.webp") with dissolve
        sheila "Jadi bisa bilang aku membuatmu gila?"
        scene expression ("images/episode9/150_smile.webp") with dissolve
        toby "Tidak terlalu terangsang."
        scene expression ("images/episode9/149_flirty.webp") with dissolve
        sheila "Bahkan jika saya mengatakan bahwa saya tidak mengenakan celana dalam hari ini? Ketika saya membungkuk, Anda hampir bisa melihat gurun Sahara."
        scene expression ("images/episode9/150_curious.webp") with dissolve
        toby "Gurun Sahara?"
        scene expression ("images/episode9/149_laugh.webp") with dissolve
        sheila "Anda tahu gurun terbesar di dunia? Suatu tempat di Afrika."
        scene expression ("images/episode9/150_cool.webp") with dissolve
        toby "Ini bukan yang terbesar. Gurun terbesar adalah di Antartika."
        scene expression ("images/episode9/149_meh.webp") with dissolve
        sheila "Apakah Anda cookie pintar? Maksud saya gurun pasir terbesar."
        scene expression ("images/episode9/150_cool.webp") with dissolve
        toby "Aku tahu. Saya sangat menyenangkan di pesta."
        scene expression ("images/episode9/149_laugh.webp") with dissolve
        sheila "Saya hanya bisa membayangkan."
        scene expression ("images/episode9/150_curious.webp") with dissolve
        toby "Jadi? Apa kesepakatan dengan gurun Sahara?"
        scene expression ("images/episode9/149_awkward.webp") with dissolve
        sheila "Anda merusak lelucon saya. Maksud saya jika saya membungkuk, Anda bisa melihat kaki unta, karena Anda tahu? Saya tidak memakai celana dalam."
    else:



        sheila "Hai [toby!c] ... di mana saja? Aku belum melihatmu sebentar."
        toby "Saya sudah cukup sibuk dengan pekerjaan dan semacamnya."

        scene expression ("images/episode9/149_curious.webp") with dissolve
        sheila "Oh ... bagaimana cara kerja?"
        scene expression ("images/episode9/150_smile.webp") with dissolve
        toby "Sebenarnya bagus. Hari ini adalah hari libur yang langka."
        scene expression ("images/episode9/149_normal.webp") with dissolve
        sheila "Sekarang itulah yang saya sebut pekerjaan yang bagus. Anda mendapatkan hari libur di pertengahan minggu."
        scene expression ("images/episode9/150_laugh.webp") with dissolve
        toby "Anda adalah pelatih pribadi. Saya tidak bisa membayangkan itu sangat menegangkan dan saya bertaruh jika Anda ingin mengambil cuti di tengah minggu Anda bisa."
        scene expression ("images/episode9/149_smile.webp") with dissolve
        sheila "Anda akan terkejut. Dan untuk hari libur saya bisa, tetapi jika saya terlalu sering melakukannya saya akan mulai kehilangan klien."
        scene expression ("images/episode9/149_normal.webp") with dissolve
        sheila "Karena saya memiliki jadwal yang tetap. Saya memiliki beberapa klien dan masing -masing dari mereka memiliki janji jadwal. Saya bertemu dengan masing -masing tiga kali seminggu, jadi jika saya ingin mengambil cuti hari Kamis, saya harus memindahkan semua klien saya ke hari Jumat, dan itu sudah penuh."
        scene expression ("images/episode9/150_normal.webp") with dissolve
        toby "Oh ... tapi saya yakin Anda bisa melatih lebih dari satu orang sekaligus."
        scene expression ("images/episode9/149_smile.webp") with dissolve
        sheila "Ya saya bisa, tetapi tidak semua orang suka itu, sebagian besar lebih suka sesi satu lawan satu."
        scene expression ("images/episode9/150_normal.webp") with dissolve
        toby "Tapi setidaknya Anda menyukai apa yang Anda lakukan?"
        scene expression ("images/episode9/149_laugh.webp") with dissolve
        sheila "Sebenarnya banyak. Kepuasan terbesar adalah ketika Anda melihat seseorang mendapatkan hasil yang baik setelah mendengarkan saran Anda."
        scene expression ("images/episode9/150_smile.webp") with dissolve
        toby "Saya hanya bisa membayangkan. Apa perubahan terbesar yang Anda lihat pada seseorang?"
        scene expression ("images/episode9/149_laugh.webp") with dissolve
        sheila "Yah ... saya punya klien ini. Dia benar -benar terlihat cukup bagus, tetapi dia masih perlu kehilangan beberapa pound. Mungkin 20 atau lebih."
        scene expression ("images/episode9/149_smile.webp") with dissolve
        sheila "Setelah satu bulan dia harus kalah 25."
        scene expression ("images/episode9/150_normal.webp") with dissolve
        toby "Ummm ... Saya tidak mengikuti. Dia gemuk?"
        scene expression ("images/episode9/149_meh.webp") with dissolve
        sheila "Anda merusak lelucon saya. Ya, dia gemuk."

    scene expression ("images/episode9/150_laugh.webp") with dissolve
    toby "Maaf saya merusak lelucon yang begitu bagus."
    scene expression ("images/episode9/149_laugh.webp") with dissolve
    sheila "Jangan khawatir saya tahu lebih banyak."
    scene expression ("images/episode9/150_smile.webp") with dissolve
    toby "Oh bagus! Mari kita dengar satu."
    scene expression ("images/episode9/149_normal.webp") with dissolve
    sheila "Hmmm ... biarkan aku berpikir."
    scene expression ("images/episode9/150_laugh.webp") with dissolve
    toby "Luangkan semua waktu yang Anda butuhkan."
    scene expression ("images/episode9/149_smile.webp") with dissolve
    sheila "Aku tahu. Mengapa jamur diundang ke semua pesta?"
    scene expression ("images/episode9/150_surprised.webp") with dissolve
    toby "Mengalahkan saya."
    scene expression ("images/episode9/149_laugh.webp") with dissolve
    sheila "Karena mereka adalah jamur!"
    scene expression ("images/episode9/150_normal.webp") with dissolve
    toby "Umm ..."
    scene expression ("images/episode9/149_awkward.webp") with dissolve
    sheila "Kamu mengerti? Fungis ... teman -teman yang menyenangkan?"
    scene expression ("images/episode9/150_normal.webp") with dissolve
    toby "Ya. Ya..."
    scene expression ("images/episode9/149_normal.webp") with dissolve
    sheila "Bisa aja. Seperti yang bisa Anda lakukan dengan lebih baik."
    scene expression ("images/episode9/150_laugh.webp") with dissolve
    toby "Saya tidak berpikir itu sangat sulit untuk mengalahkannya."
    scene expression ("images/episode9/149_normal.webp") with dissolve
    sheila "Berikan tembakan terbaik Anda."
    scene expression ("images/episode9/150_smile.webp") with dissolve
    toby "Anda memintanya."
    scene expression ("images/episode9/149_flirty.webp") with dissolve
    sheila "Pukul aku. Pukul aku dengan keras."
    scene expression ("images/episode9/150_normal.webp") with dissolve
    toby "Apa yang dikatakan pipi satu pantat kepada yang lain?"
    scene expression ("images/episode9/149_curious.webp") with dissolve
    sheila "Saya tidak tahu ... apa?"
    scene expression ("images/episode9/150_laugh.webp") with dissolve
    toby "Bersama -sama, kita bisa menghentikan omong kosong ini."
    scene expression ("images/episode9/149_laugh.webp") with dissolve
    sheila "\"Together, we can stop this shit!\"Sialan ... itu sangat lucu."
    scene expression ("images/episode9/150_smile.webp") with dissolve
    toby "Sudah kubilang tidak sulit untuk mengalahkan lelucon jamur Anda."
    scene expression ("images/episode9/149_normal.webp") with dissolve
    sheila "Saya tidak pernah mengatakan lelucon Anda lebih lucu. Saya hanya memiliki selera humor yang lebih baik jadi saya mendapatkan lelucon, tetapi Anda tidak mendapatkan milik saya. Itu bukan masalah saya."
    scene expression ("images/episode9/149_smile.webp") with dissolve
    sheila "Saya masih lebih menyukai jamur saya."
    scene expression ("images/episode9/150_laugh.webp") with dissolve
    toby "Itu bukan sesuatu yang Anda katakan dengan keras."
    scene expression ("images/episode9/149_laugh.webp") with dissolve
    sheila "Ya, mungkin Anda benar. Orang -orang mungkin berpikir saya adalah obat -obatan yang buruk ketika ada begitu banyak pilihan lain di kota ini."
    scene expression ("images/episode9/150_curious.webp") with dissolve
    toby "Saya tidak berpikir itu hanya berlaku untuk kota ini. Saya akan berpikir Anda dapat memiliki akses ke segala jenis obat di kota mana pun."
    scene expression ("images/episode9/149_normal.webp") with dissolve
    sheila "I almost forgot you're new in town. You never tried \"The Hooker\"?"
    scene expression ("images/episode9/150_surprised.webp") with dissolve
    toby "Apa itu?"
    scene expression ("images/episode9/149_smile.webp") with dissolve
    sheila "Ini adalah obat lokal baru yang membuat Anda benar -benar terangsang."

    if toby_job == 1:
        scene expression ("images/episode9/149_curious.webp") with dissolve
        sheila "Jangan beri tahu saya bahwa Anda telah bekerja di klub itu selama ini dan tidak pernah melihat pil merah muda itu?"
        scene expression ("images/episode9/150_normal.webp") with dissolve
        toby "Saya pikir itu ekstasi."

    scene expression ("images/episode9/150_curious.webp") with dissolve
    toby "Pernahkah Anda mencobanya?"
    scene expression ("images/episode9/149_normal.webp") with dissolve
    sheila "Tidak, tetapi saya penasaran untuk mencobanya, terutama sekarang setelah saya mendengar ada versi cokelat dari obat tersebut."
    scene expression ("images/episode9/150_thinking.webp") with dissolve
    if toby_job == 0:
        if darlene_path:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She must be talking about the chocolate me and Mrs. Darlene had yesterday.{/i}"
        else:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She must be talking about the chocolate Mrs. Darlene had yesterday.{/i}"
    else:
        if katrina_path:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She must be talking about the chocolate Mrs. Katrina gave me yesterday.{/i}"
        else:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She must be talking about the chocolate Mrs. Katrina tried to give me yesterday.{/i}"

    if sheila_path:
        scene expression ("images/episode9/149_flirty.webp") with dissolve
        sheila "Saya tahu wajah itu. Sesuatu memberi tahu saya bahwa Anda tahu apa yang saya bicarakan."
        scene expression ("images/episode9/150_normal.webp") with dissolve
        toby "Saya tidak tahu, mungkin."
        scene expression ("images/episode9/149_flirty.webp") with dissolve
        sheila "Nah, jika Anda berhasil mendapatkan sesuatu seperti itu, saya pikir itu bisa menyenangkan."
        scene expression ("images/episode9/150_smile.webp") with dissolve
        toby "Ya. Saya kira itu bisa saja."
        scene expression ("images/episode9/149_smile.webp") with dissolve
        sheila "Sial, aku menjadi terangsang hanya memikirkannya."
        scene expression ("images/episode9/150_flirty.webp") with dissolve
        toby "Ingin pergi ke ruang ganti?"
        scene expression ("images/episode9/149_normal.webp") with dissolve
        sheila "Saya benar -benar ingin, tetapi seseorang memberi tahu bos saya bahwa dia melihat saya berhubungan seks dengan Anda di kamar mandi dan itu buruk. Saya sangat suka pekerjaan ini dan tidak ingin kehilangannya."
        scene expression ("images/episode9/149_smile.webp") with dissolve
        sheila "Tetapi jika Anda mau, saya bebas besok malam. Kamu tahu? Untuk pergi berkencan seperti orang normal."
        scene expression ("images/episode9/150_laugh.webp") with dissolve
        toby "Maaf tentang itu."
        scene expression ("images/episode9/150_smile.webp") with dissolve
        toby "Tapi ya. Kencan besok terdengar bagus."
        scene expression ("images/episode9/149_curious.webp") with dissolve
        sheila "Dan apakah Anda pikir Anda bisa mendapatkan beberapa pil atau cokelat itu untuk besok?"
        scene expression ("images/episode9/150_laugh.webp") with dissolve
        toby "Nah jika wanita itu mau, saya akan melakukan yang terbaik."
        scene expression ("images/episode9/149_flirty.webp") with dissolve
        sheila "Saya tahu Anda adalah orang yang tepat untuk pekerjaan itu."
        scene expression ("images/episode9/150_laugh.webp") with dissolve
        toby "Saya tidak bisa menjanjikan Anda."
        scene expression ("images/episode9/149_smile.webp") with dissolve
        sheila "Saya percaya Anda banyak akal."
        scene expression ("images/episode9/151.webp") with dissolve
        sheila "Saya pergi ke kamar mandi untuk mendingin sekarang, karena semua pembicaraan ini membuat saya sangat terangsang."
        menu:
            "{i} [JGR] Ikuti dia {/i}"(csq="Acara kamar mandi"):
                $ ep9_follow_sheila = True
            "{i} Lanjutkan pelatihan Anda {/i}":


                pass
    else:

        scene expression ("images/episode9/149_smile.webp") with dissolve
        sheila "Saya tahu wajah itu. Itu adalah wajah seorang pria yang tahu sesuatu."
        scene expression ("images/episode9/150_laugh.webp") with dissolve
        toby "Saya tidak yakin. Saya mungkin pernah mendengar sesuatu tentang itu."
        scene expression ("images/episode9/149_curious.webp") with dissolve
        sheila "Apakah Anda tahu di mana saya bisa mendapatkannya?"
        scene expression ("images/episode9/150_normal.webp") with dissolve
        toby "Pil? Tidak begitu yakin. Cokelat? Mungkin."
        scene expression ("images/episode9/149_smile.webp") with dissolve
        sheila "Either way baik -baik saja."
        scene expression ("images/episode9/150_curious.webp") with dissolve
        toby "Tapi tahukah Anda apa yang terjadi pada orang lain?"
        scene expression ("images/episode9/149_laugh.webp") with dissolve
        sheila "Saya mendengar sesuatu tentang membuat Anda lebih hornier."
        scene expression ("images/episode9/150_normal.webp") with dissolve
        toby "Hanya itu yang saya tahu."
        scene expression ("images/episode9/149_curious.webp") with dissolve
        sheila "Jadi menurut Anda apakah Anda bisa mendapatkan saya beberapa?"
        scene expression ("images/episode9/150_laugh.webp") with dissolve
        toby "Apa yang bisa saya lakukan?"
        scene expression ("images/episode9/149_smile.webp") with dissolve
        sheila "Sekarang Anda terdengar seperti pengedar narkoba sungguhan."
        scene expression ("images/episode9/150_laugh.webp") with dissolve
        toby "Saya lebih suka istilah dealer cokelat."
        scene expression ("images/episode9/149_laugh.webp") with dissolve
        sheila "Bagaimana dengan sesi pelatihan gratis?"
        scene expression ("images/episode9/150_smile.webp") with dissolve
        toby "Aku akan mengatakan kamu sedikit murah, tapi aku akan mengambilnya."
        scene expression ("images/episode9/149_smile.webp") with dissolve
        sheila "Anda masih mendapatkan nomor saya dengan benar?"
        scene expression ("images/episode9/150_laugh.webp") with dissolve
        toby "Ya."
        scene expression ("images/episode9/151.webp") with dissolve
        sheila "Dalam hal ini, beri tahu saya jika Anda berhasil mendapatkan beberapa."
        toby "Oke ... saya akan."


    if ep9_follow_sheila == False:
        scene expression ("images/episode9/152.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}So those drugs are called \"The Hooker\", mungkin karena efeknya pada orang. {/i}"
        scene expression ("images/episode9/153.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wonder if Mrs. Katrina can help me.{/i}"
        if toby_job == 0:
            scene expression ("images/episode9/152.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Speaking of help. Why the fuck am I helping Sheila with her drugs?{/i}"
            scene expression ("images/episode9/153.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Have I gone mad? What's wrong with me?{/i}"
        else:
            scene expression ("images/episode9/152.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck. I'm not really in the mood to talk to Katrina.{/i}"
            scene expression ("images/episode9/153.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why the fuck did I tell Sheila I'll help her with her drugs?{/i}"
        scene expression ("images/episode9/152.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Anyway. I'd better finish this and head to the showers.{/i}"
        scene expression ("images/episode9/153.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Three.{/i}"
        scene expression ("images/episode9/152.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode9/153.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Four.{/i}"
        scene expression ("images/episode9/152.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode9/153.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Five.{/i}"
        scene expression ("images/episode9/152.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode9/153.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Six...{/i}"
        scene expression ("images/episode9/152.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm curious what else that chocolate could do. {/i}"
        scene expression ("images/episode9/153.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Biologically speaking, I don't think it's possible to only affect your arousal.{/i}"
        scene expression ("images/episode9/152.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}There has to be other effects.{/i}"
        scene expression ("images/episode9/153.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Eight.{/i}"
        scene expression ("images/episode9/152.webp") with dissolve
        if toby_job == 0:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I hope Darlene knows about it, so I can ask her.{/i}"
        else:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'll have to ask Katrina about it.{/i}"
        scene expression ("images/episode9/153.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Nine.{/i}"
        scene expression ("images/episode9/152.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode9/153.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Ten.{/i}"
        scene expression ("images/episode9/154.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'll go take a shower now.{/i}"

        scene expression ("images/episode9/155.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode9/156.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode9/157.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
    else:


        label memory_31:

            scene expression ("images/episode9/155.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode9/158.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode9/159.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode9/160.webp") with dissolve
            sheila "Hey seksi."
            toby "Pikiran jika saya bergabung?"
            sheila "Anda akan membuat saya dalam kesulitan. Anda tidak bisa menunggu sampai besok?"
            toby "Ini sulit."
            scene expression ("images/episode9/161.webp") with dissolve
            sheila "Sayangnya saya benar -benar tidak dapat berhubungan seks dengan klien di kamar mandi, jadi kami harus menemukan cara lain untuk memperbaiki masalah Anda."
            toby "Apakah kita akan pergi?"
            sheila "Anda pergi ke kios itu dan saya akan pergi ke saya."
            scene expression ("images/episode9/162.webp") with dissolve
            toby "Saya gagal melihat bagaimana ini akan memperbaiki masalah saya."
            scene expression ("images/episode9/163.webp") with dissolve
            sheila "Menikmati!"
            scene expression ("images/episode9/164.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Ummm... {/i}"
            scene expression ("images/episode9/165.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What is she doing?{/i}"
            scene expression ("images/episode9/166.webp") with dissolve
            sheila "Jika Anda ingin saya melanjutkan Anda lebih baik mulai membelai ayam keras Anda."
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's such a tease.{/i}"
            scene expression ("images/episode9/167.webp") with dissolve
            sheila "Itulah yang ingin saya lihat."

            show ep9_168 with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            show ep9_169 with dissolve
            hide ep9_168

            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, she's so hot staring straight at me while she plays with her pussy.{/i}"
            $ ui.saybehavior()
            $ ui.interact()
            sheila "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nYou like what you see?"
            toby "Anda bercanda, kan? Saya menyukainya!"
            show ep9_170 with dissolve
            hide ep9_169

            $ ui.saybehavior()
            $ ui.interact()
            sheila "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nThen let me help you get a better view."
            show ep9_171 with dissolve
            hide ep9_170

            $ ui.saybehavior()
            $ ui.interact()
            sheila "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nHow do you like it now?"
            show ep9_172 with dissolve
            hide ep9_171

            toby "Saya lebih suka lebih baik jika kita berada di kios yang sama."
            $ ui.saybehavior()
            $ ui.interact()
            sheila "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nDon't worry. I'm sure you can wait til tomorrow and if you get what I want, you'll get to have me any way you want."
            show ep9_173 with dissolve
            hide ep9_172

            toby "Saya dekat."
            sheila "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nMe too."
            $ ui.saybehavior()
            $ ui.interact()
            toby "Saya akan pergi ke cum."
            sheila "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI'm going to cum too... Cum for me baby... Let me see your thick seed."
            scene expression ("images/episode9/173.webp")
            hide ep9_173

            scene expression ("images/episode9/174.webp") with dissolve:
                yalign 0.0
                linear 10.0 yalign 1.0

            $ ui.pausebehavior(9.3)
            with flash
            with flash
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode9/175.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            $ unlockImage(persistent.sheila_07)
            sheila "Sampai jumpa besok, seksi! Dan tolong jangan mengecewakan saya."

            scene expression ("images/episode9/156.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}That was interesting. I would have preferred fucking her brains out, but that was pretty hot too.{/i}"

            scene expression ("images/episode9/157.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            $ unlockMemory(persistent.memory_31)
            $ renpy.end_replay()


    scene expression ("images/episode9/176.webp") with fade
    $ progress = 126
    if patricia_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Looks like I have five messages from Tris.{/i}"
        scene expression ("images/episode9/176_texting.webp") with dissolve

        call sms_incoming ("tris", "We're going to a movie with [mom] and [auntie]. You coming too?") from _call_sms_incoming_152
        call sms_incoming ("tris", "I meant, you're going too. It was not a question.") from _call_sms_incoming_153
        call sms_incoming ("tris", "Fine... Please, [bro]. Want to come to a movie with us? I don't want to go with [mom] and [auntie] by myself. They'll just tease me about boys.") from _call_sms_incoming_154
        call sms_incoming ("tris", "Please?", img_icon="images/episode9/177_icon.webp", img="images/episode9/177.webp") from _call_sms_incoming_155
        call sms_incoming ("tris", "Answer your fucking phone.") from _call_sms_incoming_156
        if toby_job == 0:
            call sms_sent ("tris", "Fine... I'm coming.") from _call_sms_sent_119
        else:
            call sms_sent ("tris", "For fuck sake woman. Yes, I'm coming.") from _call_sms_sent_120
        call sms_incoming ("tris", "What took you so long?") from _call_sms_incoming_157
        call sms_sent ("tris", "I was taking a shower. I'm at the gym.") from _call_sms_sent_121
        call sms_incoming ("tris", "Good, you really needed a shower.") from _call_sms_incoming_158
        call sms_sent ("tris", "It's my second today. How many did you take?") from _call_sms_sent_122
        call sms_incoming ("tris", "That's just figures. So are you coming?") from _call_sms_incoming_159
        call sms_sent ("tris", "Yes, I am.") from _call_sms_sent_123
        call sms_sent ("tris", "What time is the movie?") from _call_sms_sent_124
        call sms_incoming ("tris", "It starts in 10 minutes. We're buying tickets now.") from _call_sms_incoming_160
        call sms_sent ("tris", "Okay. I'll be there in 15 minutes. Buy me a ticket too and send it to me.") from _call_sms_sent_125
        call sms_incoming ("tris", "Okay... See you here.") from _call_sms_incoming_161
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Looks like I have a message from [aunt] Denise.{/i}"
        call sms_incoming ("denise", "Hi dear. Me and the girls are going to a movie. I hope to see you there too. It would be nice to spend some more time with my favorite [nephew] since tomorrow I'll be going back home.") from _call_sms_incoming_162
        call sms_sent ("denise", "You're leaving already?") from _call_sms_sent_126
        call sms_incoming ("denise", "Unfortunately I have to go back, but you don't need to cry over me. I'll be back next week.") from _call_sms_incoming_163
        call sms_sent ("denise", "Did you have a chance to try out the hot tub?") from _call_sms_sent_127
        call sms_incoming ("denise", "Yes... Yesss... YES! It was perfect. I'm hoping you can build me one like it back home.") from _call_sms_incoming_164
        call sms_sent ("denise", "Haha... I'll think about it.") from _call_sms_sent_128
        call sms_incoming ("denise", "Okay then. See you at the movies.") from _call_sms_incoming_165
        call sms_sent ("denise", "What time does it start?") from _call_sms_sent_129
        call sms_incoming ("denise", "Oh. I forgot to mention that. The movie starts in 10 minutes.") from _call_sms_incoming_166
        call sms_incoming ("denise", "Can you make it?") from _call_sms_incoming_167
        call sms_sent ("denise", "I'll be there in 15. Tell Tris to buy me a ticket and send it to me.") from _call_sms_sent_130
        call sms_incoming ("denise", "Okay, sweetie. See you soon!") from _call_sms_incoming_168
        call sms_sent ("denise", "See you.") from _call_sms_sent_131

    hide screen message
    scene expression ("images/episode9/178.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... I forgot to ask her what movie we're seeing.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Oh well. Too late now. I already told them to buy me a ticket.{/i}"

    return


label episode9_cinema:
    $ progress = 127


    scene expression ("images/episode9/179.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see... Row 7, seat 6.{/i}"
    scene expression ("images/episode9/180.webp") with dissolve
    charlotte "Kenapa lama sekali?"
    toby "Saya tidak tahu tentang film itu sampai 15 menit yang lalu. Sebenarnya aku sudah bisa tiba di sini dengan cukup cepat."
    scene expression ("images/episode9/181.webp") with dissolve
    denise "Tinggalkan bocah itu sendirian, setidaknya kita memiliki seorang pria untuk menemani kita."
    toby "Terima kasih."
    scene expression ("images/episode9/182.webp") with dissolve
    toby "Jadi? Film apa yang kita tonton?"
    denise "\"Friends with Benefits\"."
    toby "Kedengarannya menarik."
    denise "Sebenarnya itu."
    if patricia_path == True:
        scene expression ("images/episode9/183.webp") with dissolve
        patricia "Saya yakin Anda akan menyukainya."
        toby "Apa yang saya lewatkan?"
        patricia "Nah, keduanya menjalin hubungan dengan orang lain dan mereka berdua putus, tetapi memutuskan untuk terus berteman."
        patricia "Dan sekarang dia pindah ke New York dan dia akan menjemputnya untuk wawancara kerja."
        toby "Oh keren."
        show screen ui_message("A few minutes later") with long_dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode9/184_normal.webp") with dissolve
        hide screen ui_message
        patricia "Oh sial. Mantannya memanggilnya saat dia berkencan dengan gadis lain"
        scene expression ("images/episode9/185_normal.webp") with dissolve
        toby "Secara teknis mereka tidak berkencan. Ini adalah pertemuan bisnis."
        scene expression ("images/episode9/184_curious.webp") with dissolve
        patricia "What does \"emotionally unavailable\"berarti?"
        scene expression ("images/episode9/185_smile.webp") with dissolve
        toby "Saya kira itu ketika seseorang tidak dapat mencintai seseorang. Maksud saya, mereka dapat menghabiskan waktu bersama dan bersenang -senang, tetapi masih belum ada emosi di sana."
        scene expression ("images/episode9/184_curious.webp") with dissolve
        patricia "Pernahkah Anda secara emosional tidak tersedia?"
        scene expression ("images/episode9/185_laugh.webp") with dissolve
        toby "Tidak yakin apakah itu istilah yang tepat, tetapi ada saat -saat ketika saya merasa saya tidak bisa terhubung sama sekali dengan seorang gadis. Semuanya hebat kecuali saya tidak punya perasaan untuknya."
        if emma_break:
            scene expression ("images/episode9/184_smile.webp") with dissolve
            patricia "Itulah mengapa Anda putus dengan Emma?"
            scene expression ("images/episode9/185_normal.webp") with dissolve
            toby "Tidak. Aku putus dengannya karena hal -hal tidak sama seperti sebelumnya. Aku mencintainya."
        scene expression ("images/episode9/184_curious.webp") with dissolve
        patricia "Bagaimana jika seorang gadis menyukai Anda dan Anda tidak menyukai punggungnya. Bukankah itu membuat Anda tidak tersedia secara emosional?"
        scene expression ("images/episode9/185_laugh.webp") with dissolve
        toby "Mungkin itu membuat saya tidak menyadari situasi."
        scene expression ("images/episode9/184_normal.webp") with dissolve
        patricia "Tetapi bagaimana jika Anda tahu seorang gadis menyukai Anda dan Anda masih tidak menyukai punggungnya?"
        scene expression ("images/episode9/185_smile.webp") with dissolve
        toby "Saya tidak tahu, [sis]. Setidaknya dalam kasus saya ada banyak hal yang menarik minat saya pada seorang wanita."
        scene expression ("images/episode9/184_laugh.webp") with dissolve
        patricia "Biarkan saya menebak. Mata, bibir, payudara, pantat dan kaki."
        scene expression ("images/episode9/185_curious.webp") with dissolve
        toby "Apakah Anda benar -benar berpikir saya dangkal?"
        scene expression ("images/episode9/184_curious.webp") with dissolve
        patricia "Anda tidak?"
        scene expression ("images/episode9/185_laugh.webp") with dissolve
        toby "Tidak ... aku tidak."
        scene expression ("images/episode9/184_normal.webp") with dissolve
        patricia "Baik ... aku percaya kamu! Mari kita terus menonton."

        show screen ui_message("A few moments later") with long_dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode9/184_curious.webp") with dissolve
        hide screen ui_message
        patricia "Apakah Anda pikir saya menarik?"
        scene expression ("images/episode9/185_surprised.webp") with dissolve
        toby "Apa yang masuk ke dalam dirimu? Anda benar -benar ke film ini."
        scene expression ("images/episode9/184_laugh.webp") with dissolve
        patricia "Mungkin. Bagian terakhir itu berbicara kepada saya. Dia bertanya kepadanya apa yang dia suka tentang dia secara fisik dan dia bisa mengatakannya dengan jelas. Jadi saya bertanya kepada Anda."
        scene expression ("images/episode9/185_normal.webp") with dissolve
        toby "Mereka bukan [related]. I \ m Anda [brother]."
        scene expression ("images/episode9/184_normal.webp") with dissolve
        patricia "Jadi, apakah saya terlihat bagus?Ayo. Lakukan untukku. Terkadang saya merasa kepribadian saya tidak cukup baik bagi anak laki -laki untuk menyukai saya."
        scene expression ("images/episode9/184_curious.webp") with dissolve
        patricia "Apakah saya seorang gadis yang tampan?"
        scene expression ("images/episode9/185_flirty.webp") with dissolve
        toby "Ya kamu."
        scene expression ("images/episode9/184_flirty.webp") with dissolve
        patricia "Apa yang kamu sukai dari saya?"
        scene expression ("images/episode9/185_laugh.webp") with dissolve
        toby "Anda mengubah pertanyaan. Anda bertanya apakah saya pikir Anda menarik."
        scene expression ("images/episode9/184_smile.webp") with dissolve
        patricia "Hal yang sama."
        scene expression ("images/episode9/185_flirty.webp") with dissolve
        toby "Jawabannya adalah ya. Saya pikir Anda sangat menarik."
        scene expression ("images/episode9/184_smile.webp") with dissolve
        patricia "Terima kasih!"
        scene expression ("images/episode9/184_surprised.webp") with dissolve
        patricia "Kotoran. Mereka akan berhubungan seks seperti itu. Tidak ada emosi. Tidak ada apa -apa."
        scene expression ("images/episode9/184_curious.webp") with dissolve
        patricia "Apakah Anda pikir itu mungkin?"
        scene expression ("images/episode9/185_curious.webp") with dissolve
        toby "Untuk berhubungan seks tanpa ikatan?"
        scene expression ("images/episode9/184_normal.webp") with dissolve
        patricia "Ya."
        if toby_job == 0:
            scene expression ("images/episode9/185_smile.webp") with dissolve
            toby "Ya saya pikir begitu, tapi mungkin tidak sebagus itu."
            scene expression ("images/episode9/184_curious.webp") with dissolve
            patricia "Mengapa tidak?"
            scene expression ("images/episode9/185_normal.webp") with dissolve
            toby "Karena ketika Anda mencintai seseorang, itu tidak hanya tentang seks, itu adalah sesuatu yang lebih."
            scene expression ("images/episode9/184_normal.webp") with dissolve
            patricia "Menarik."
        else:

            scene expression ("images/episode9/185_smile.webp") with dissolve
            toby "Cukup mudah untuk berhubungan seks tanpa menjadi emosional."
            scene expression ("images/episode9/184_curious.webp") with dissolve
            patricia "Tapi apakah itu bagus?"
            scene expression ("images/episode9/185_normal.webp") with dissolve
            toby "Seks itu seks! Kamu bercinta sampai kamu cum. Orgasme sama."
            scene expression ("images/episode9/184_normal.webp") with dissolve
            patricia "Menarik."

        scene expression ("images/episode9/184_surprised.webp") with dissolve
        patricia "Apa yang terjadi di sana?"
        scene expression ("images/episode9/185_laugh.webp") with dissolve
        toby "Dia mungkin masuk ke mulutnya."
        scene expression ("images/episode9/184_iecx.webp") with dissolve
        patricia "Eww ... itu kotor."
        scene expression ("images/episode9/185_curious.webp") with dissolve
        toby "Menurut Anda mengapa itu kotor?"
        scene expression ("images/episode9/184_normal.webp") with dissolve
        patricia "Aku tidak tahu. Ini seperti dia kencing di mulutmu."
        scene expression ("images/episode9/185_laugh.webp") with dissolve
        toby "Sama sekali tidak seperti itu."
        scene expression ("images/episode9/184_curious.webp") with dissolve
        patricia "Mengapa wanita melakukan itu?"
        scene expression ("images/episode9/185_laugh.webp") with dissolve
        toby "Kemungkinan besar karena itu membuat pria merasa nyaman dengan diri mereka sendiri atau karena itu membuat mereka merasa slutty."
        scene expression ("images/episode9/184_smile.webp") with dissolve
        patricia "Apakah Anda pernah selesai di mulut Emma?"
        scene expression ("images/episode9/185_normal.webp") with dissolve
        toby "Saya tidak akan membicarakannya."
        scene expression ("images/episode9/184_meh.webp") with dissolve
        patricia "Anda membosankan."
        scene expression ("images/episode9/184_curious.webp") with dissolve
        patricia "Bagaimana rasanya cum?"
        scene expression ("images/episode9/185_laugh.webp") with dissolve
        toby "Saya tidak pernah mencicipinya."
        scene expression ("images/episode9/184_normal.webp") with dissolve
        patricia "Anda bermaksud mengatakan bahwa setelah Anda masuk ke mulut Emma, Anda tidak menciumnya?"
        scene expression ("images/episode9/185_smile.webp") with dissolve
        toby "Seperti yang saya katakan. Saya tidak akan membicarakan hal ini dengan Anda, jadi Anda bisa melupakannya."
        scene expression ("images/episode9/184_normal.webp") with dissolve
        patricia "Beberapa teman saya mengatakan bahwa itu asin. Apakah itu benar?"
        scene expression ("images/episode9/185_normal.webp") with dissolve
        toby "Seperti yang saya katakan. Saya tidak pernah mencicipinya."
        scene expression ("images/episode9/184_curious.webp") with dissolve
        patricia "Tidak pernah, pernah?"
        scene expression ("images/episode9/185_laugh.webp") with dissolve
        toby "Tidak. Sekarang tutup mulut dan terus menonton film."
        scene expression ("images/episode9/184_sad.webp") with dissolve
        patricia "Bagus."
        show screen ui_message("A few moments later") with long_dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode9/184_curious.webp") with dissolve
        hide screen ui_message
        patricia "Ngomong -ngomong, apa tipenya Anda?"
        scene expression ("images/episode9/185_normal.webp") with dissolve
        toby "Saya tidak mengira saya punya satu."
        scene expression ("images/episode9/184_normal.webp") with dissolve
        patricia "Apa maksudmu kamu tidak punya tipe? Setiap orang memiliki tipe."
        scene expression ("images/episode9/185_normal.webp") with dissolve
        toby "Dia harus tampan, tetapi selain itu saya pikir lebih penting apa yang ada di dalam kepalanya."
        scene expression ("images/episode9/184_curious.webp") with dissolve
        patricia "Jadi Anda mengatakan bahwa jika Anda harus memilih antara bimbo dengan payudara palsu, pantat besar, Botox di bibirnya atau seorang gadis cantik sederhana dengan pantat datar, tidak ada payudara apa pun, Anda akan memilih bimbo?"
        scene expression ("images/episode9/185_laugh.webp") with dissolve
        if toby_job == 0:
            toby "Kemungkinan besar saya tidak akan memilihnya."
        else:
            toby "Yah ... Saya ingin lebih mengenal bimbo, karena saya yakin dia memberikan blowjobs yang bagus, tetapi pada akhirnya saya pikir saya akan tetap dengan pantat datar."
            scene expression ("images/episode9/184_normal.webp") with dissolve
            patricia "Anda dangkal."
        scene expression ("images/episode9/184_surprised.webp") with dissolve
        patricia "Ooooh ... dia cemburu melihatnya menggoda dengan gadis lain."
        scene expression ("images/episode9/185_curious.webp") with dissolve
        toby "Anda tahu perasaan itu?"
        scene expression ("images/episode9/184_smile.webp") with dissolve
        patricia "Bagaimana saya tahu?"
        scene expression ("images/episode9/185_curious.webp") with dissolve
        toby "Aku tidak tahu. Mungkin Anda menyukai seseorang dan dia tidak tertarik pada Anda dan kemudian ketika Anda melihatnya dengan gadis lain, Anda kesal?"
        scene expression ("images/episode9/184_laugh.webp") with dissolve
        patricia "Saya tidak akan pernah kesal karena hal seperti itu."
        scene expression ("images/episode9/185_laugh.webp") with dissolve
        toby "Ya, benar. Karena kami berdua tahu amarah Anda dan betapa hebatnya Anda menanganinya ketika seseorang tidak melakukan apa yang Anda inginkan."
        scene expression ("images/episode9/184_smile.webp") with dissolve
        patricia "Saya memiliki temperamen seperti itu, bukan?"
        scene expression ("images/episode9/185_smile.webp") with dissolve
        toby "100 %%."
        scene expression ("images/episode9/184_normal.webp") with dissolve
        patricia "Sial ... aku sudah kacau. Tetapi untuk menjawab pertanyaan Anda. Mungkin sekali atau dua kali."
        scene expression ("images/episode9/184_surprised.webp") with dissolve
        patricia "Lihat ... mereka jatuh cinta."
        scene expression ("images/episode9/185_laugh.webp") with dissolve
        toby "Anda benar -benar ke dalam film ini."
        scene expression ("images/episode9/184_smile.webp") with dissolve
        patricia "Ya ... Maksudku, lihat betapa lucunya mereka bersama."
        scene expression ("images/episode9/184_normal.webp") with dissolve
        patricia "Selalu menyenangkan melihat akhir yang bahagia."
        scene expression ("images/episode9/185_normal.webp") with dissolve
        toby "Akhir yang bahagia hanya ada di film. Dalam kehidupan nyata itu jauh lebih rumit."
        scene expression ("images/episode9/184_sad.webp") with dissolve
        patricia "Ya ... apakah kamu percaya pada cinta?"
        scene expression ("images/episode9/185_normal.webp") with dissolve
        if toby_job == 0:
            toby "Ya. Saya pikir ada orang yang sangat mencintai satu sama lain."
            scene expression ("images/episode9/184_curious.webp") with dissolve
            patricia "Apakah Anda pikir Anda akan menemukan cinta sejati Anda?"
            if emma_break == False:
                scene expression ("images/episode9/185_laugh.webp") with dissolve
                toby "Anda bertanya kepada seorang pria yang menjalin hubungan jika dia pikir dia akan menemukan cinta sejati?"
                scene expression ("images/episode9/184_normal.webp") with dissolve
                patricia "Oh maksudmu, Emma? Apakah Anda benar -benar berpikir dia adalah orangnya?"
                scene expression ("images/episode9/185_normal.webp") with dissolve
                toby "Aku tidak tahu. Mungkin. Maksud saya, akan menyenangkan untuk tidak terluka atau terluka lagi."
                scene expression ("images/episode9/184_sad.webp") with dissolve
                patricia "Jadi begitu."
            else:
                toby "Saya pikir cinta berlebihan."
                scene expression ("images/episode9/184_sad.webp") with dissolve
                patricia "Mengapa menurutmu begitu?"
                scene expression ("images/episode9/185_normal.webp") with dissolve
                toby "Karena kebanyakan orang yang mengatakan mereka dalam cinta tidak benar -benar mencintai orang seperti yang mereka pikirkan. Mereka menyukai gagasan bersama seseorang."
                toby "They love the idea of being appreciated, being cared for. Having sex. But \"love till death do us part\"Kedengarannya terlalu bagus untuk menjadi kenyataan."
                scene expression ("images/episode9/184_sad.webp") with dissolve
                patricia "Jadi begitu."
        else:
            toby "Saya pikir cinta berlebihan."
            scene expression ("images/episode9/184_sad.webp") with dissolve
            patricia "Mengapa menurutmu begitu?"
            scene expression ("images/episode9/185_normal.webp") with dissolve
            toby "Karena kebanyakan orang yang mengatakan mereka dalam cinta tidak benar -benar mencintai orang seperti yang mereka pikirkan. Mereka menyukai gagasan bersama seseorang."
            toby "They love the idea of being appreciated, being cared for. Having sex. But \"love till death do us part\"Kedengarannya terlalu bagus untuk menjadi kenyataan."
            scene expression ("images/episode9/184_sad.webp") with dissolve
            patricia "Jadi begitu."
        show screen ui_message("Some minutes later") with long_dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode9/186_1.webp") with dissolve
        hide screen ui_message
        $ ui.saybehavior()
        $ ui.interact()
    else:
        toby "Apa yang saya lewatkan?"
        denise "Kedua orang ini baru saja putus dengan pacar mereka dan sekarang satu orang pindah ke New York dan dia menunggunya di bandara."
        toby "Oh, jadi saya tidak terlalu merindukan."
        denise "Tidak."
        show screen ui_message("A few moments later") with long_dissolve
        $ ui.saybehavior()
        $ ui.interact()
        hide screen ui_message
        scene expression ("images/episode9/185_sleep.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode9/186_2.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()

    scene expression ("images/episode9/187.webp") with dissolve
    charlotte "Jadi? Apakah kalian menyukai filmnya?"
    scene expression ("images/episode9/188.webp") with dissolve
    denise "Selain fakta bahwa itu membuat saya merasa sangat kesepian, ya itu hebat."
    scene expression ("images/episode9/187.webp") with dissolve
    charlotte "Bagaimana denganmu, [toby!c]?"
    if patricia_path:
        scene expression ("images/episode9/188.webp") with dissolve
        denise "Saya tidak berpikir dia bisa memperhatikan banyak film karena Tris. Dia membicarakan semuanya."
        scene expression ("images/episode9/189_1.webp") with dissolve
        patricia "Itu tidak benar. Saya melihat bahwa dia bosan dengan film itu jadi saya memutuskan untuk menjelaskan bagian -bagian penting kepadanya."
        scene expression ("images/episode9/190.webp") with dissolve
        toby "Dan saya menghargainya."
        scene expression ("images/episode9/191_1.webp") with dissolve
        toby "Bagaimanapun. Aku pulang. Apakah ada yang ikut dengan saya di sepeda?"
        scene expression ("images/episode9/192.webp") with dissolve
        patricia "Baik ... aku datang! Anda tidak harus memohon."
        toby "Saya menghargainya."
    else:
        scene expression ("images/episode9/189_1.webp") with dissolve
        patricia "Dia tidur melalui seluruh film. Begitu dia menyelesaikan popcorn -nya, dia tertidur."
        scene expression ("images/episode9/190.webp") with dissolve
        toby "Anda tidak memberi tahu saya bahwa itu adalah film cewek."
        scene expression ("images/episode9/189_2.webp") with dissolve
        patricia "Tidak!"
        scene expression ("images/episode9/191_2.webp") with dissolve
        toby "Apa pun. Aku pulang. Siapa yang ikut dengan saya?"
        scene expression ("images/episode9/193.webp") with dissolve
        denise "Leg, koboi."
        toby "Dan kali ini saya mengemudi."
        denise "Bagus!"
    return


label episode9_drive_denise:
    $ progress = 128

    scene expression ("images/episode9/194.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/195.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/196.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if emma_break:
        scene expression ("images/episode9/197.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
    else:

        scene expression ("images/episode9/198.webp") with dissolve:
            xalign 1.0
            yalign 1.0
            linear 10.0 yalign 0.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode9/199.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode9/200.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    return


label episode9_drive_tris:
    $ progress = 128

    scene expression ("images/episode9/201.webp") with dissolve
    patricia "Jadi? Dimana sekarang?"
    toby "Rumah? Bukankah itu rencananya?"
    scene expression ("images/episode9/202.webp") with dissolve
    patricia "Umm ... ya."
    toby "Ayo ... Katakan padaku apa yang ada di pikiranmu."
    scene expression ("images/episode9/203.webp") with dissolve
    patricia "Yah saya sudah begitu sibuk beberapa minggu terakhir ini dengan final dan kemudian perburuan perguruan tinggi dan sekarang benar -benar pergi ke perguruan tinggi, sehingga saya tidak punya banyak waktu untuk bersantai."
    toby "Baik ... mari kita pergi ke tempat kita."
    scene expression ("images/episode9/204_1.webp") with dissolve
    patricia "Dan Anda akan membiarkan saya mengemudi?"
    scene expression ("images/episode9/204_2.webp") with dissolve
    toby "Umm ... Saya sangat ingin terus hidup."
    scene expression ("images/episode9/205.webp") with dissolve
    patricia "Silakan?"
    toby "..."
    scene expression ("images/episode9/206_1.webp") with dissolve
    patricia "Anda membiarkan [aunt] Denise Drive. Mengapa Anda tidak mengizinkan saya?"
    scene expression ("images/episode9/206_2.webp") with dissolve
    toby "Pertama -tama, Denise tahu cara naik."
    scene expression ("images/episode9/205_1.webp") with dissolve
    patricia "Anda juga bisa mengajari saya."
    scene expression ("images/episode9/205_2.webp") with dissolve
    toby "Persetan. Aku jadi akan menyesali ini."

    scene expression ("images/episode9/207.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/208.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/209.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/210.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/211.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/212.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/213.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/214.webp") with dissolve
    toby "Menepi di sini."
    patricia "Oke!"
    toby "Jangan masuk ke ..."
    scene expression ("images/episode9/215.webp") with dissolve
    toby "Terlambat."
    scene expression ("images/episode9/216.webp") with dissolve
    patricia "Dan kami diparkir."
    patricia "Saya sangat pandai dalam hal ini."
    toby "Kecuali fakta bahwa Anda hampir pergi ke rumput. Untungnya ada pagar kecil itu."
    scene expression ("images/episode9/217.webp") with dissolve
    patricia "Seperti Anda bisa melakukan pekerjaan yang lebih baik."
    scene expression ("images/episode9/218.webp") with dissolve
    toby "Ya ... bayangkan itu."
    scene expression ("images/episode9/219.webp") with dissolve
    patricia "Saya melakukan hal yang sama."
    scene expression ("images/episode9/220.webp") with dissolve
    toby "Kecuali dalam kasus Anda itu ada di pagar."
    scene expression ("images/episode9/219.webp") with dissolve
    patricia "Tidak. Saya tidak ingatan akan hal itu."
    scene expression ("images/episode9/221.webp") with dissolve
    toby "Jadi? Apakah Anda menyukainya?"
    patricia "Astaga. Ya! Itu luar biasa. Jantungku masih berdetak seperti orang gila. Saya hampir bisa merasakan adrenalin!"
    scene expression ("images/episode9/222_curious.webp") with dissolve
    patricia "Tapi apa ide besarnya dengan kopling? Mengapa Anda terus mengatakan kepada saya untuk menarik benda itu."
    scene expression ("images/episode9/223_laugh.webp") with dissolve
    toby "Karena untuk mengganti persneling, Anda harus menarik kopling."
    scene expression ("images/episode9/222_normal.webp") with dissolve
    patricia "Saya tidak menyukai bagian itu."
    scene expression ("images/episode9/223_meh.webp") with dissolve
    toby "Saya minta maaf atas ketidaknyamanan ini. Saya berjanji untuk menghapusnya untuk Anda."
    scene expression ("images/episode9/222_surprised.webp") with dissolve
    patricia "Anda bisa menghapusnya?"
    scene expression ("images/episode9/223_laugh.webp") with dissolve
    toby "TIDAK! Saya bisa \ 't. Saya mengacaukan Yang Mulia."
    scene expression ("images/episode9/222_laugh.webp") with dissolve
    patricia "Akhirnya! Anda akhirnya memberi saya rasa hormat yang pantas saya dapatkan. Selain mengacaukan saya, kedengarannya sempurna."
    scene expression ("images/episode9/223_smile.webp") with dissolve
    toby "Anda terlalu manja."
    scene expression ("images/episode9/222_smile.webp") with dissolve
    patricia "Saya pikir kita berdua tahu itu tidak lagi terjadi. Ya, saya agak manja, tetapi saya tidak berpikir saya lagi."
    scene expression ("images/episode9/223_curious.webp") with dissolve
    toby "Sedikit? Apakah Anda lupa bahwa 2 tahun yang lalu pada hari Natal saya mendapat kemeja dan Anda mendapat sepatu kets 00?"
    scene expression ("images/episode9/222_normal.webp") with dissolve
    patricia "Pertama -tama, itu salah Anda karena tidak menulis surat kepada Santa. Dalam kasus saya, saya tahu persis apa yang saya inginkan."
    scene expression ("images/episode9/223_normal.webp") with dissolve
    toby "Santa tidak ada. Mengapa saya menulis surat kepadanya?"
    scene expression ("images/episode9/222_laugh.webp") with dissolve
    patricia "Saya tahu bahwa Santa tidak ada, bodoh. Tetapi [mom] dan [dad] perlu tahu persis apa yang kita inginkan."
    scene expression ("images/episode9/222_smile.webp") with dissolve
    patricia "Dan kedua sepatu kets itu tidak ada. Mereka baru berusia 95 tahun."
    scene expression ("images/episode9/223_normal.webp") with dissolve
    toby "Oh, ya. Saya melihat di mana kebingungan itu. [mom!c] mengatakan bahwa hadiah Natal adalah 50, karena bajuku adalah 0."
    scene expression ("images/episode9/222_eyes.webp") with dissolve
    patricia "Baik ... saya dimanjakan."
    scene expression ("images/episode9/222_smile.webp") with dissolve
    patricia "Tapi saya tidak lagi."
    scene expression ("images/episode9/223_curious.webp") with dissolve
    toby "Benar-benar?"
    scene expression ("images/episode9/222_normal.webp") with dissolve
    patricia "Tentu saja. Apakah Anda lupa siapa yang membersihkan kamar Anda?"
    scene expression ("images/episode9/223_meh.webp") with dissolve
    toby "Untuk uang, meskipun Anda kehilangan taruhan."
    scene expression ("images/episode9/222_smile.webp") with dissolve
    patricia "Anda kehilangan satu juga. Bukan salahku, kau menerimanya."
    scene expression ("images/episode9/222_normal.webp") with dissolve
    patricia "Dan selain itu akan lebih mudah untuk hanya meminta uang [mom], tetapi tidak. Saya memutuskan untuk melakukan beberapa pekerjaan."
    scene expression ("images/episode9/223_laugh.webp") with dissolve
    toby "Wow, kamu sudah dewasa."
    scene expression ("images/episode9/222_laugh.webp") with dissolve
    patricia "Saya tahu, kan?"
    scene expression ("images/episode9/223_smile.webp") with dissolve
    toby "Ya."
    scene expression ("images/episode9/223_curious.webp") with dissolve
    toby "Bagaimanapun. Bagaimana sekolah?"
    scene expression ("images/episode9/222_sad.webp") with dissolve
    patricia "Ini bagus, tetapi ada banyak siswa pintar dan sangat sulit untuk bersaing dengan mereka."
    scene expression ("images/episode9/223_laugh.webp") with dissolve
    toby "Anda tidak harus bersaing dengan mereka. Anda hanya perlu baik di sekolah."
    scene expression ("images/episode9/222_normal.webp") with dissolve
    patricia "Saya berharap semudah itu, tapi tidak. Saya perlu bersaing dengan mereka karena saya membutuhkan beasiswa."
    scene expression ("images/episode9/223_curious.webp") with dissolve
    toby "Anda tidak pernah memperjuangkan beasiswa."
    scene expression ("images/episode9/222_smile.webp") with dissolve
    patricia "Saya tidak bisa membersihkan kamar Anda selamanya. Ya, itu menyenangkan, tapi saya perlu mendapatkan uang juga. Aku tidak bisa mengandalkanmu selamanya."
    scene expression ("images/episode9/223_smile.webp") with dissolve
    toby "Lihat. Anda adalah [sister] saya dan meskipun kami saling menginjak satu sama lain, Anda tahu bahwa saya akan melakukan apa saja untuk Anda."
    scene expression ("images/episode9/222_cute.webp") with dissolve
    patricia "Saya tahu, itulah mengapa saya membersihkan kamar Anda, karena itu yang paling tidak bisa saya lakukan untuk Anda."
    scene expression ("images/episode9/223_laugh.webp") with dissolve
    toby "Jadi itu berarti Anda akan melakukannya secara gratis?"
    scene expression ("images/episode9/222_cool.webp") with dissolve
    patricia "Tidak. Itulah mengapa Anda akan memberi saya kenaikan gaji."
    scene expression ("images/episode9/223_laugh.webp") with dissolve
    toby "Tidak. Saya sudah memberi tahu Anda apa yang harus Anda lakukan untuk kenaikan gaji."
    scene expression ("images/episode9/222_curious.webp") with dissolve
    patricia "Apa yang menurut Anda menarik tentang saya?"
    scene expression ("images/episode9/223_normal.webp") with dissolve
    toby "Tiba -tiba pertanyaan apa dengan pertanyaan itu?"
    scene expression ("images/episode9/222_smile.webp") with dissolve
    patricia "Kembali ke teater Anda mengatakan bahwa Anda pikir saya menarik. Jika Anda adalah [brother] saya, apa yang paling menarik bagi Anda?"
    scene expression ("images/episode9/223_normal.webp") with dissolve
    toby "Secara fisik?"
    scene expression ("images/episode9/222_cute.webp") with dissolve
    patricia "Ya. Fisik yang ketat."
    scene expression ("images/episode9/224.webp") with dissolve
    menu:
        "{i} mata {/i}":
            $ ep9_tris_face = 1
            toby "Aku suka matamu. Anda memiliki mata yang luar biasa."
            scene expression ("images/episode9/225.webp") with dissolve
            patricia "Apa yang sangat baik tentang mataku? Mereka coklat. Itu sangat utama. Saya berharap mereka ... Saya tidak tahu, hijau atau bahkan biru."
            toby "Saya kira tidak demikian. Matamu cantik, ketika aku melihat di dalamnya, aku merasa bisa tersesat di sana dan mereka sangat besar."
        "{i} hidung {/i}":
            $ ep9_tris_face = 2
            toby "Saya suka hidung kecil Anda yang lucu."
            scene expression ("images/episode9/225.webp") with dissolve
            patricia "Anda sangat menyukai hidung saya? Tidakkah menurutmu terlalu besar?"
            toby "Besar? Apa yang kamu bicarakan? Ini sangat kecil dan lucu dan runcing. Saya pikir itu hidung yang sempurna."
        "{i} bibir {/i}":
            $ ep9_tris_face = 3
            toby "Aku suka bibirmu. Mereka sangat selera."
            scene expression ("images/episode9/225.webp") with dissolve
            patricia "Anda pikir saya memiliki bibir yang bagus?"
            toby "Ya ... Bibir Anda terlihat sangat menggugah selera. Jika Anda tidak bermimpi tentang mencium bibir itu."
        "{i} neck {/i}":
            $ ep9_tris_face = 4
            toby "Saya sangat suka leher Anda."
            scene expression ("images/episode9/225.webp") with dissolve
            patricia "Leherku? Apa yang bisa sangat menarik di leher?"
            toby "Yah, mungkin rambut sedikit membantu di sini, karena itu memperlihatkannya."
            patricia "Oh?"
            toby "Anda memiliki leher yang sangat indah. Saya tidak tahu bagaimana menjelaskannya dengan lebih baik, tetapi itu mulia."
        "{i} [JGR] mod: Semua hal di atas {/i}":
            $ ep9_tris_face = 1
            toby "Aku suka matamu. Anda memiliki mata yang luar biasa."
            scene expression ("images/episode9/225.webp") with dissolve
            patricia "Apa yang sangat baik tentang mataku? Mereka coklat. Itu sangat utama. Saya berharap mereka ... Saya tidak tahu, hijau atau bahkan biru."
            toby "Saya kira tidak demikian. Matamu cantik, ketika aku melihat di dalamnya, aku merasa bisa tersesat di sana dan mereka sangat besar."
            $ ep9_tris_face = 2
            scene expression ("images/episode9/225.webp") with dissolve
            patricia "Anda sangat menyukai hidung saya? Tidakkah menurutmu terlalu besar?"
            toby "Besar? Apa yang kamu bicarakan? Ini sangat kecil dan lucu dan runcing. Saya pikir itu hidung yang sempurna."
            $ ep9_tris_face = 3
            scene expression ("images/episode9/225.webp") with dissolve
            patricia "Anda pikir saya memiliki bibir yang bagus?"
            toby "Ya ... Bibir Anda terlihat sangat menggugah selera. Jika Anda tidak bermimpi tentang mencium bibir itu."
            $ ep9_tris_face = 4
            scene expression ("images/episode9/225.webp") with dissolve
            patricia "Leherku? Apa yang bisa sangat menarik di leher?"
            toby "Yah, mungkin rambut sedikit membantu di sini, karena itu memperlihatkannya."
            patricia "Oh?"
            toby "Anda memiliki leher yang sangat indah. Saya tidak tahu bagaimana menjelaskannya dengan lebih baik, tetapi itu mulia."

    scene expression ("images/episode9/222_shy.webp") with dissolve
    patricia "Terima kasih. Saya menghargainya."
    scene expression ("images/episode9/223_smile.webp") with dissolve
    toby "Jangan khawatir."
    scene expression ("images/episode9/222_shy.webp") with dissolve
    patricia "Nah, apa yang Anda katakan itu bagus, dan membantu saya berpikir saya cantik, tapi yang lebih saya penasaran adalah jika saya seksi. Aku tidak tahu. Panas, mungkin?"
    scene expression ("images/episode9/223_laugh.webp") with dissolve
    toby "Anda ingin tahu jika Anda panas?"
    scene expression ("images/episode9/222_normal.webp") with dissolve
    patricia "Mungkin. Masalahnya, saya memiliki beberapa rasa tidak aman tentang penampilan saya. Semua orang memberi tahu saya betapa cantiknya saya, betapa bagusnya rambut saya, betapa bagusnya riasan saya, tetapi saya tidak yakin apakah itu cukup."
    scene expression ("images/episode9/223_curious.webp") with dissolve
    toby "Cukup untuk apa?"
    scene expression ("images/episode9/222_smile.webp") with dissolve
    patricia "Aku tidak tahu."
    scene expression ("images/episode9/223_thinking.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think she's talking about the mysterious boy. Let's see if I can fish for some more info about this guy.{/i}"
    scene expression ("images/episode9/223_smile.webp") with dissolve
    toby "Anda memiliki masalah anak laki -laki?"
    scene expression ("images/episode9/222_laugh.webp") with dissolve
    patricia "Tidak ... Mengapa Anda berpikir begitu?"
    scene expression ("images/episode9/223_laugh.webp") with dissolve
    toby "Anda bertanya apakah saya pikir Anda seksi. Saya [brother] Anda, jadi itu berarti Anda ingin beberapa pria memperhatikan Anda, tetapi Anda mungkin berpikir Anda tidak cukup baik untuknya."
    scene expression ("images/episode9/222_cool.webp") with dissolve
    patricia "Saya cukup baik untuk anak laki -laki mana pun. Saya tidak punya masalah anak laki -laki."
    scene expression ("images/episode9/223_smile.webp") with dissolve
    toby "Itulah mengapa Anda mengatakan Anda memiliki rasa tidak aman?"
    scene expression ("images/episode9/222_shy.webp") with dissolve
    patricia "..."
    scene expression ("images/episode9/223_flirty.webp") with dissolve
    if toby_job == 0:
        toby "Ya. Saya pikir Anda sangat seksi. Sejujurnya saya pikir Anda adalah gadis paling cantik yang saya kenal."
    else:
        toby "Ya. Saya pikir Anda seksi. Sebenarnya saya tidak berpikir seksi sudah cukup untuk menggambarkan betapa panasnya Anda, karena [sis], Anda terlihat sangat bagus."
    scene expression ("images/episode9/222_surprised.webp") with dissolve
    patricia "Kamu benar -benar berpikir begitu?"
    scene expression ("images/episode9/223_smile.webp") with dissolve
    toby "Apakah saya pernah berbohong kepada Anda?"
    scene expression ("images/episode9/222_thinking.webp") with dissolve
    patricia "Biarkan saya berpikir ..."
    scene expression ("images/episode9/222_laugh.webp") with dissolve
    patricia "Ya, Anda punya."
    scene expression ("images/episode9/223_surprised.webp") with dissolve
    toby "Kapan?"
    scene expression ("images/episode9/222_laugh.webp") with dissolve
    patricia "Anda mengatakan bahwa ketika Anda mendapatkan pekerjaan Anda, Anda akan membawa saya ke restoran yang sangat mahal."
    scene expression ("images/episode9/223_laugh.webp") with dissolve
    toby "Pertama -tama itu adalah 8 tahun yang lalu."
    scene expression ("images/episode9/222_cute.webp") with dissolve
    patricia "Itu tidak penting. Janji adalah janji."
    scene expression ("images/episode9/223_laugh.webp") with dissolve
    toby "Sudah kubilang karena kamu menangis. Aku harus membuatmu berhenti entah bagaimana karena pengasuh bodoh itu tidak tahu apa yang harus dilakukan denganmu."
    scene expression ("images/episode9/222_surprised.webp") with dissolve
    patricia "Saya tidak menangis. Saya tidak punya alasan untuk."
    scene expression ("images/episode9/223_meh.webp") with dissolve
    toby "Benar-benar? Anda kesal di [dad] karena ia membawa [mom] ke restoran mewah dan meninggalkan kami di rumah bersama Ms. Amelia."
    scene expression ("images/episode9/222_normal.webp") with dissolve
    patricia "Aku benci wanita jalang itu."
    scene expression ("images/episode9/223_laugh.webp") with dissolve
    toby "Anda membenci siapa pun yang tidak akan membiarkan Anda makan permen."
    scene expression ("images/episode9/222_laugh.webp") with dissolve
    patricia "Biasanya itu Ms. Amelia."
    scene expression ("images/episode9/222_smile.webp") with dissolve
    patricia "Tapi bukan itu intinya. Intinya adalah Anda berbohong kepada saya."
    scene expression ("images/episode9/223_normal.webp") with dissolve
    toby "Untuk itu saya maafkan maaf. Aku benar -benar akan menebusnya. Senang?"
    scene expression ("images/episode9/222_smile.webp") with dissolve
    patricia "Hanya setelah Anda memberi tahu saya apa yang Anda sukai dari saya."
    scene expression ("images/episode9/223_smile.webp") with dissolve
    toby "Saya sudah melakukannya."
    scene expression ("images/episode9/222_laugh.webp") with dissolve
    patricia "Anda terlalu banyak pria."
    scene expression ("images/episode9/222_flirty.webp") with dissolve
    patricia "Anda mengatakan bahwa saya seksi. Apa yang membuatmu mengatakan itu."
    scene expression ("images/episode9/223_laugh.webp") with dissolve
    toby "Anda! Anda membuat saya mengatakannya."
    scene expression ("images/episode9/222_smile.webp") with dissolve
    patricia "Saya hanya bertanya. Dengan baik."
    scene expression ("images/episode9/222_pouty.webp") with dissolve
    patricia "Sebenarnya sangat bagus."
    scene expression ("images/episode9/223_laugh.webp") with dissolve
    if toby_job == 0:
        toby "Bagus. Tolong berdiri."
        scene expression ("images/episode9/222_curious.webp") with dissolve
        patricia "Mengapa?"
        scene expression ("images/episode9/223_smile.webp") with dissolve
        toby "Jadi saya bisa melihat Anda lebih baik."
        scene expression ("images/episode9/222_laugh.webp") with dissolve
        patricia "Apakah Anda memberi tahu saya bahwa Anda tidak pernah menatap saya?"
        scene expression ("images/episode9/223_normal.webp") with dissolve
        toby "Apakah Anda ingin saya memberi tahu Anda atau tidak?"
        scene expression ("images/episode9/226.webp") with dissolve
        patricia "Sekarang apa?"
        toby "Sekarang Anda berpose."
    else:

        toby "Bagus. Berdiri dan berpose untukku."
        scene expression ("images/episode9/222_flirty.webp") with dissolve
        patricia "Apakah Anda memberi tahu saya bahwa Anda tidak pernah menatap saya?"
        scene expression ("images/episode9/223_normal.webp") with dissolve
        toby "Saya tidak pernah punya waktu untuk menganalisis tubuh Anda. Saya selalu hanya melirik jadi Anda tidak melihat saya."
        scene expression ("images/episode9/222_surprised.webp") with dissolve
        patricia "Tapi saya [sister] Anda. Bagaimana Anda bisa melihat saya, Anda cabul."
        scene expression ("images/episode9/223_normal.webp") with dissolve
        toby "Kata gadis yang akan berpose untuknya [brother]."
        scene expression ("images/episode9/222_laugh.webp") with dissolve
        patricia "Anda membuatnya terdengar sangat kotor."
        scene expression ("images/episode9/223_laugh.webp") with dissolve
        toby "Apakah Anda akan berpose untuk saya atau tidak?"
        scene expression ("images/episode9/226.webp") with dissolve
        patricia "Ya, Tuan!"
        toby "Sekarang Pose!"

    scene expression ("images/episode9/227.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    patricia "Bagaimana ini?"
    toby "Itu bagus, tetapi Anda harus berbalik juga."

    scene expression ("images/episode9/227_2.webp") with dissolve
    patricia "Anda sedikit cabul."

    scene expression ("images/episode9/228.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    patricia "Jadi? Pernahkah Anda melihat semua yang Anda butuhkan?"
    if toby_job == 0:
        toby "Kecuali satu hal. Mengapa Anda tidak berbalik dan menaikkan bagian atas Anda sedikit."
    else:
        toby "Tidak. Balikkan dan angkat atasan Anda."

    scene expression ("images/episode9/229.webp") with dissolve
    patricia "Apakah kamu serius?"
    toby "Mengapa saya tidak? Ini tidak seperti itu pertama kali aku akan melihatmu di bramu."
    scene expression ("images/episode9/230.webp") with dissolve
    patricia "Tapi kami tidak pernah di depan umum dan karena Anda melihat lebih dari sekadar bra saya, saya yakin Anda memiliki ide yang cukup bagus."

    if toby_job == 0:
        toby "Tolong menyegarkan ingatan saya."
    else:
        toby "Apakah Anda ingin jawaban saya atau tidak?"

    scene expression ("images/episode9/231.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    $ unlockImage(persistent.patricia_17)

    patricia "Jadi? Apa yang begitu seksi tentang saya?"
    scene expression ("images/episode9/232.webp") with dissolve
    menu:
        "Payudara":
            $ ep9_tris_body = 1
            toby "Anda memiliki payudara yang sangat bagus."
            scene expression ("images/episode9/233.webp") with dissolve
            patricia "Tapi mereka sangat kecil."
            toby "Anda berusia 18 tahun. Saya pikir Anda memiliki payudara yang cukup besar untuk usia Anda."
            scene expression ("images/episode9/234.webp") with dissolve
            patricia "Saya tidak tahu harus berkata apa, tetapi jika Anda mengatakan demikian, saya akan mempercayai Anda."
        "Pantat":

            $ ep9_tris_body = 2
            toby "Anda memiliki pantat terbaik yang pernah saya lihat."
            scene expression ("images/episode9/233.webp") with dissolve
            patricia "Benar-benar? Apakah Anda benar -benar berpikir saya memiliki pantat yang hebat?"
            toby "Ini sempurna. Itu terlihat sangat kuat dan bulat."
            scene expression ("images/episode9/234.webp") with dissolve
            patricia "Anda benar tentang itu!"
        "Kaki":

            $ ep9_tris_body = 3
            toby "Anda memiliki kaki panjang seksi yang cantik."
            scene expression ("images/episode9/233.webp") with dissolve
            patricia "Tapi mereka terlihat seperti tongkat."
            toby "Sama sekali tidak. Mereka sempurna."
            scene expression ("images/episode9/234.webp") with dissolve
            patricia "Anda hanya mengatakan itu karena Anda terlalu malu untuk mengatakan sesuatu yang kotor."
            toby "Sama sekali tidak. Anda memiliki pantat yang bagus dan payudara yang bagus, tetapi kaki Anda membunuh saya."
        "Kaki":

            $ ep9_tris_body = 4
            toby "Aku suka kakimu."
            scene expression ("images/episode9/233.webp") with dissolve
            patricia "Kakiku? Aku bahkan tidak menunjukkan kakiku."
            toby "Tidak, tapi saya sudah melihat mereka berkali -kali. Mereka sangat baik."
            patricia "Lalu mengapa Anda membuat saya mengangkat atasan saya jika Anda hanya akan mengatakan kaki saya?"
            toby "Sedikit pengembalian untuk semua menggoda Anda."
            scene expression ("images/episode9/234.webp") with dissolve
            patricia "Anda sangat buruk!"
        "[JGR] mod: semua hal di atas":

            $ ep9_tris_body = 1
            toby "Anda memiliki payudara yang sangat bagus."
            scene expression ("images/episode9/233.webp") with dissolve
            patricia "Tapi mereka sangat kecil."
            toby "Anda berusia 18 tahun. Saya pikir Anda memiliki payudara yang cukup besar untuk usia Anda."
            scene expression ("images/episode9/234.webp") with dissolve
            patricia "Saya tidak tahu harus berkata apa, tetapi jika Anda mengatakan demikian, saya akan mempercayai Anda."
            $ ep9_tris_body = 2
            toby "Anda memiliki pantat terbaik yang pernah saya lihat."
            scene expression ("images/episode9/233.webp") with dissolve
            patricia "Benar-benar? Apakah Anda benar -benar berpikir saya memiliki pantat yang hebat?"
            toby "Ini sempurna. Itu terlihat sangat kuat dan bulat."
            scene expression ("images/episode9/234.webp") with dissolve
            patricia "Anda benar tentang itu!"
            $ ep9_tris_body = 3
            toby "Anda memiliki kaki panjang seksi yang cantik."
            scene expression ("images/episode9/233.webp") with dissolve
            patricia "Tapi mereka terlihat seperti tongkat."
            toby "Sama sekali tidak. Mereka sempurna."
            scene expression ("images/episode9/234.webp") with dissolve
            patricia "Anda hanya mengatakan itu karena Anda terlalu malu untuk mengatakan sesuatu yang kotor."
            toby "Sama sekali tidak. Anda memiliki pantat yang bagus dan payudara yang bagus, tetapi kaki Anda membunuh saya."
            $ ep9_tris_body = 4
            toby "Aku suka kakimu."
            scene expression ("images/episode9/233.webp") with dissolve
            patricia "Kakiku? Aku bahkan tidak menunjukkan kakiku."
            toby "Tidak, tapi saya sudah melihat mereka berkali -kali. Mereka sangat baik."
            patricia "Lalu mengapa Anda membuat saya mengangkat atasan saya jika Anda hanya akan mengatakan kaki saya?"
            toby "Sedikit pengembalian untuk semua menggoda Anda."
            scene expression ("images/episode9/234.webp") with dissolve
            patricia "Anda sangat buruk!"

    scene expression ("images/episode9/235_1.webp") with dissolve
    patricia "Terima kasih [bro]."
    scene expression ("images/episode9/235_2.webp") with dissolve
    toby "Apa yang telah saya lakukan untuk mendapatkan begitu banyak cinta?"
    scene expression ("images/episode9/235_1.webp") with dissolve
    patricia "Saya tidak tahu, tetapi Anda membuat saya merasa sangat baik tentang diri saya sendiri."
    scene expression ("images/episode9/235_2.webp") with dissolve
    toby "Anda tidak punya alasan untuk merasa tidak aman. Anda sempurna."
    scene expression ("images/episode9/236.webp") with dissolve
    patricia "Kamu benar -benar berpikir begitu?"
    toby "Ya."
    toby "Dan saya minta maaf karena telah mengolok -olok Anda saat Anda tidur. Anda tidak mendengkur dan Anda tidak perlu bajingan. Anda sempurna."
    scene expression ("images/episode9/237.webp") with dissolve
    patricia "Saya akan membunuh [mom] karena memberi tahu Anda tentang itu."
    toby "Saya minta maaf tentang itu."
    scene expression ("images/episode9/238.webp") with dissolve
    patricia "Terima kasih!"
    scene expression ("images/episode9/239.webp") with dissolve
    toby "Sudah pergi?"
    scene expression ("images/episode9/238.webp") with dissolve
    patricia "Ya. Saya mulai lelah dan saya harus bangun pagi untuk sekolah besok."
    scene expression ("images/episode9/240.webp") with dissolve
    toby "Oke, tapi saya mengemudi kali ini."
    patricia "Baik ... tunjukkan bagaimana ini dilakukan."

    scene expression ("images/episode9/241.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/242.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode9/243.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if emma_break:

        scene expression ("images/episode9/244.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
    else:


        scene expression ("images/episode9/198.webp") with dissolve:
            xalign 1.0
            yalign 1.0
            linear 10.0 yalign 0.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode9/245.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode9/246.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    return

label episode9_emma:
    $ progress = 129

    scene expression ("images/episode9/247.webp") with dissolve
    toby "Halo, Sayang. Apakah semuanya baik -baik saja? Apa yang kamu lakukan di sini?"
    emma "Ya, sayang. Semuanya bagus. Saya sudah banyak memikirkan kami akhir -akhir ini dan saya mendapatkan hadiah."
    toby "Anda tahu Anda seharusnya tidak memilikinya."
    scene expression ("images/episode9/248.webp") with dissolve
    emma "Mungkin, tapi saya pikir pacar saya layak mendapatkan yang terbaik."
    toby "Sekarang Anda membuat saya sangat penasaran."
    toby "Di mana hadiah ini yang Anda bicarakan?"
    scene expression ("images/episode9/249.webp") with dissolve
    emma "Anda harus membuka kotak terlebih dahulu."
    scene expression ("images/episode9/250.webp") with dissolve
    toby "Itu kotak yang luar biasa, jika Anda bertanya kepada saya."
    scene expression ("images/episode9/249.webp") with dissolve
    emma "Anda menyukainya?"
    toby "Apakah Anda bercanda? Saya menyukainya."
    label memory_32:
        if _in_replay:

            scene expression ("images/utils/black.png") with dissolve
            menu:
                "Pilih pekerjaan Anda"
                "Agen real estat":
                    $ toby_job == 0
                "Manajer klub":
                    $ toby_job == 1
        scene expression ("images/episode9/251.webp") with dissolve
        toby "Ayo. Biarkan masuk ke dalam. Bagaimanapun, saya memiliki hadiah untuk diterima."
        emma "Dan sungguh hadiah."
        scene expression ("images/episode9/252.webp") with fade
        toby "Datang ke sini dulu. Aku ingin menciummu."
        emma "Bibir ini adalah milikmu."

        scene expression ("images/episode9/253.webp") with dissolve
        show ep9_253
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode9/253_1.webp") with dissolve
        hide ep9_253

        toby "Saya sangat merindukan bibir ini."
        emma "Setiap kali Anda ingin mereka hubungi saya dan Anda akan memilikinya. Anda masih memiliki nomor saya kan?"
        scene expression ("images/episode9/254.webp") with dissolve
        toby "Anda sangat konyol. Tentu saja saya memilikinya."
        scene expression ("images/episode9/255.webp") with dissolve
        emma "Berbicara tentang hadiah, mengapa Anda tidak membuat diri Anda nyaman di tempat tidur sementara saya membuka kusut hadiah Anda."
        scene expression ("images/episode9/254.webp") with dissolve
        toby "Jadi begitulah caranya?"
        scene expression ("images/episode9/256.webp") with dissolve
        emma "Menikmati!"

        scene expression ("images/episode9/257.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode9/258.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode9/259.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode9/260.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode9/261.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode9/262.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode9/263.webp") with dissolve
        emma "Apakah Anda siap mendapatkan hadiah Anda?"
        toby "Apakah Anda mengatakan bahwa implan payudara Anda tidak ada saat ini?"
        emma "Tidak konyol, Anda sudah melihat itu. Saya memiliki kejutan baru untuk Anda."
        scene expression ("images/episode9/264.webp") with dissolve
        emma "Mengapa Anda tidak membantu saya dengan celana dalam saya."
        scene expression ("images/episode9/265.webp") with dissolve
        emma "Itu saja. Jangan berhenti!"
        scene expression ("images/episode9/266.webp") with dissolve

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the fuck is that. Is she using a butt plug?{/i}"
        scene expression ("images/episode9/267.webp") with dissolve
        emma "Anda bisa menariknya keluar."
        scene expression ("images/episode9/268.webp") with dissolve
        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\n{i}Mhmmm...{/i}"
        scene expression ("images/episode9/269.webp") with dissolve
        if toby_job == 0:
            toby "Tolong beritahu saya ini bukan hadiah saya. Anda memberi saya steker pantat dan kemudian pergi untuk pulang?"
            scene expression ("images/episode9/270.webp") with dissolve
            emma "Sekarang setelah Anda menyebutkannya."
            scene expression ("images/episode9/271.webp") with dissolve
            emma "Selamat tinggal!"
            toby "Tidak mungkin aku membiarkanmu pergi sekarang."
        else:

            toby "Saya akan menikmati hadiah saya."
            scene expression ("images/episode9/270.webp") with dissolve
            emma "Kami membicarakan hal ini tepat sebelum Anda pergi dan saya telah banyak berpikir dan karena Anda pantas mendapatkan yang terbaik, saya melatih bajingan saya untuk Anda."

        scene expression ("images/episode9/272.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\nAre you sure you're ready for this?"
        emma "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\nI'm ready to do anything as long as I'm with you."
        emma "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\nJust please be gentle."
        if toby_job == 0:
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\nDon't worry, honey. I will."
        else:
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\nYou have nothing to worry about. You're my slut after all."

        scene expression ("images/episode9/273_0.webp") with dissolve
        show ep9_273
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode9/273.webp") with dissolve
        hide ep9_273

        scene expression ("images/episode9/274.webp") with dissolve
        emma "Saya harap Anda masih memiliki pelumas yang kami beli tempo hari."
        if toby_job == 0:
            toby "Ya. Biarkan saya mendapatkannya."
            emma "Belum. Izinkan saya melumasi penis Anda seperti yang saya suka dulu."
        else:
            toby "Saya lakukan, tetapi mengapa Anda tidak menggunakan mulut Anda yang cantik untuk melumasi penisku dan kemudian kita bisa menggunakan pelumas."
            emma "Aku akan sangat mengisap penismu dengan baik sehingga kamu tidak perlu melumasi."

        scene expression ("images/episode9/275.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode9/276.webp") with dissolve
        show ep9_276
        $ ui.saybehavior()
        $ ui.interact()
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This girl is perfect. I don't know what I have done to deserve her.{/i}"
        hide ep9_276

        scene expression ("images/episode9/277.webp") with dissolve
        show ep9_277
        toby "Sial ... ini terasa sangat enak."
        $ ui.saybehavior()
        $ ui.interact()
        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nMhmmmm..."
        hide ep9_277

        scene expression ("images/episode9/278.webp") with dissolve
        show ep9_278
        if toby_job == 1:
            toby "Apakah Anda tidak tahu itu tidak sopan untuk berbicara dengan mulut penuh?"
        $ ui.saybehavior()
        $ ui.interact()
        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nImmm wanmmmt yummm."
        hide ep9_278

        scene expression ("images/episode9/279.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        toby "Aku juga sangat menginginkanmu."
        emma "Bawa aku."
        if toby_job == 0:
            toby "Apakah Anda yakin tentang bagian anal?"
            emma "Saya cukup yakin. Selama Anda, satu -satunya yang meniduri saya di bajingan ketat saya."

            scene expression ("images/episode9/280.webp") with dissolve:
                yalign 0.0
                linear 10.0 yalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            toby "Biarkan saya melumasi penis saya dulu."

        scene expression ("images/episode9/281.webp") with dissolve:
            xalign 0.0
            yalign 0.0
            linear 10.0 yalign 1.0 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        if toby_job == 0:
            toby "Saya masuk. Cobalah untuk rileks sebanyak mungkin."
        else:
            emma "Apakah Anda tidak akan melumasi terlebih dahulu?"
            toby "Itulah yang Anda lakukan dengan bayi mulut Anda. Sekarang cobalah untuk bersantai karena saya masuk."


        show ep9_282
        emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nMhmmmm... Fuck!"
        scene expression ("images/episode9/282.webp") with dissolve
        hide ep9_282

        scene expression ("images/episode9/283.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        if toby_job == 0:
            toby "Apakah kamu baik -baik saja?"
            emma "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nYes I'm fine, but your cock is so much bigger than that anal plug."
        else:
            emma "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nFuck. I forgot how big your cock is. You're stretching my asshole so much."

        emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nI need to relax more."


        show ep9_284
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode9/284.webp") with dissolve
        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck! Your cock is so big. It fills my asshole."
        hide ep9_284

        scene expression ("images/episode9/285.webp") with dissolve:
            xalign 1.0
            yalign 0.0
            linear 10.0 yalign 1.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        if toby_job == 0:
            toby "Apakah kamu baik -baik saja sayang?"
        else:
            toby "Apakah kamu baik -baik saja?"

        emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes, dear. You can start moving, but not too fast."
        scene expression ("images/episode9/293.webp") with dissolve:
            yalign 1.0
            xalign 0.0
            linear 10.0 yalign 0.2 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        toby "Jika terlalu sakit, beri tahu saya."
        emma "Apakah kita akan menggunakan kata yang aman?"
        toby "Kami bisa."
        emma "The safe word will be \"Don't you dare fucking stop\"."
        toby "Itu bisa berbahaya."
        emma "Saya seorang gadis besar. Saya bisa menerimanya!"
        toby "Oke kalau begitu."

        scene expression ("images/episode9/286.webp") with dissolve
        show ep9_286
        emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nFuck me... You're so big."
        $ ui.saybehavior()
        $ ui.interact()
        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes... Yes... YES!"
        hide ep9_286

        scene expression ("images/episode9/287.webp") with dissolve
        show ep9_287
        $ ui.saybehavior()
        $ ui.interact()
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It looks like she's enjoying it. Maybe I can speed up a little bit.{/i}"
        hide ep9_287

        scene expression ("images/episode9/288.webp") with dissolve
        show ep9_288
        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck! Yes! Yess!"
        $ ui.saybehavior()
        $ ui.interact()
        emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nFill my tight asshole with that big cock of yours."
        hide ep9_288

        scene expression ("images/episode9/289.webp") with dissolve
        show ep9_289
        if toby_job == 0:
            toby "Saya suka saat Anda berbicara seperti itu."
        else:
            toby "Anda suka pelacur?"
        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes... It's so fucking good. Your cock feels so good in my asshole."
        $ ui.saybehavior()
        $ ui.interact()
        hide ep9_289

        scene expression ("images/episode9/290.webp") with dissolve
        show ep9_290
        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nMhmmm... Yes! Fucking yesss!"
        $ ui.saybehavior()
        $ ui.interact()
        emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nI'm going to cum soon."
        toby "Saya juga."
        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nCome in me. Come inside my asshole."
        hide ep9_290
        toby "Aku cumming ..."
        with flash
        with flash

        scene expression ("images/episode9/291.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        emma "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes... Yes... YESSS!"

        scene expression ("images/episode9/292.webp") with dissolve:
            xalign 0.0
            yalign 0.0
            linear 10.0 xalign 1.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        $ unlockImage(persistent.emma_08)
        emma "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nFuck that was so good!"


        scene expression ("images/episode9/294.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        if patricia_path:
            scene expression ("images/episode9/295.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

        scene expression ("images/episode9/296.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.4

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        emma "Aku sangat mencintaimu [toby!c]."
        emma "Tolong jangan sampai Anda meninggalkan saya."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She sounds sad.{/i}"
        toby "Apakah kamu baik -baik saja?"

        scene expression ("images/episode9/297.webp") with dissolve:
            xalign 1.0
            yalign 1.0
            linear 10.0 yalign 0.3 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        emma "Saya baik-baik saja. Hanya saja saya berharap Anda bisa menghabiskan lebih banyak waktu dengan saya, karena Anda semua yang saya miliki."
        toby "Saya minta maaf tentang itu. Saya akan mencoba menjadi lebih baik."
        emma "Saya memberi Anda semua yang saya miliki. Aku tidak punya apa -apa lagi untuk diberikan padamu. Saya berharap ini cukup."
        toby "Anda benar -benar sempurna untuk saya."

        scene expression ("images/episode9/298.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.3

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        emma "Aku mencintaimu!"
        toby "Aku pun mencintaimu!"

        scene expression ("images/episode9/299.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode9/300.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        $ unlockMemory(persistent.memory_32)
        $ renpy.end_replay()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
