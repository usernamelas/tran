

define ms = Character("Mila __tag_0 __ (pikiran)", image="mila", color=u'#df0e8f', what_italic=True)
define m = Character("Mila", image="mila", color=u'#df0e8f')
define p = Character("Paul", image="paul", color=u'#1e7316')
define l = Character("Liz", color=u'#a8b9bf')
define ls = Character("Liz __tag_0 __ (Pikiran)", color=u'#a8b9bf')
define n = Character("")
define bob_unknown = Character("???")
define bob = Character("Bob", color=u'#0321a7')
define d = Character("Dick")
define Courier = Character("Kurir")
define ps = Character("Paul (pikiran)", color=u'#1e7316')
define k = Character("Kira", image="kiki", color=u'#F5F5DC')

define l_translation1 = Character("Liz", color=u'#a8b9bf', what_textshader="reverse_typewriter", slow=True, what_slow_cps=translation_shader_korean_cps)
define l_translation2 = Character("", what_textshader="slow_typewriter", slow=True, what_slow_cps=translation_shader_cps)
define Kim_translation1 = Character("Kim", what_textshader="reverse_typewriter", slow=True, what_slow_cps=translation_shader_korean_cps)
define Kim_translation2 = Character("", what_textshader="slow_typewriter", slow=True, what_slow_cps=translation_shader_cps)
define nobody_translation1 = Character("???", what_textshader="reverse_typewriter", slow=True, what_slow_cps=translation_shader_korean_cps)
define nobody_translation2 = Character("", what_textshader="slow_typewriter", slow=True, what_slow_cps=translation_shader_cps)


define ma = Character("Mila", kind=nvl, image="mila", callback=Phone_SendSound)
define md = Character("Mila", kind=nvl, image="mila", callback=Phone_SendSound)
define pm = Character("Paul (suami)", kind=nvl, callback=Phone_ReceiveSound)
define dm = Character("Dick82", kind=nvl, callback=Phone_ReceiveSound)
define bob_message = Character("Bob", kind=nvl, callback=Phone_ReceiveSound)


define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)


default paul_took_initiative = False
default paul_touch_ass = False
default mila_was_in_the_room = False
default bday_sub = True
default bob_love = 0


default mila_dom = 0

default dom = 0

default bday_bobs_slut = False

label start:
scene bg restricted
"Terima kasih khusus kepada __Tag_0__Saint Blackmoor__tag_1__ untuk mengedit dan mengoreksi game ini"
menu:
    "Jika Anda berumur kurang dari 18 tahun, tutup game ini"
    "Biarkan saya masuk, saya berusia 18+":
        jump start2
    "Saya bukan 18+":

        jump end

label start2:
scene bg mila_first with dissolve

ms "Berapa lama kita bertemu? __Tag_0__back di sekolah, lima belas tahun yang lalu."
ms "Mengingat saat -saat itu sangat menyenangkan ... __tag_0__ththing sangat mengasyikkan dan bersemangat saat itu."
ms "Hidup saya dengan Paul dimulai seperti dongeng yang selalu saya impikan untuk hidup."
scene bg wedding with dissolve
ms "“Mereka hidup bahagia selamanya” - sebuah kisah yang saya impikan sebagai seorang anak. __Tag_0__ Pangeran di atas kuda putih memberi saya kebahagiaan."
ms "Hidup saya penuh dengan kesenangan dan kegembiraan. __Tag_0__ dan sepertinya semuanya sempurna. __Tag_0__paul benar -benar seorang pangeran. __Tag_0__e tampan, pintar, dan bisa menjagaku."
ms "Tapi sesuatu telah berubah baru -baru ini. __Tag_0__everthing sangat baik dan manis sehingga tidak ada yang perlu digosipkan dengan teman -teman saya. __Tag_0__everthing sangat bagus ... __tag_0__that adalah satu -satunya pemikiran yang tetap ada di kepalaku ..."
scene wedding_bw with dissolve
ms "Kebahagiaan ...__ tag_0__ membosankan."
ms "Bukannya saya ingin drama atau masalah apa pun ... __tag_0__but tingkat perawatan dan cinta yang diberikan Paul kepada saya ... __tag_0__ ini percaya dia menunjukkan kepada saya ... __tag_0__ membuat saya ingin ...__ tag_0__ hal ..."
scene bathroom_start_worried_steam with fade
show hand_sprite at center:
    xpos 0.7
    easeout 0.5 xpos 0.166
pause 0.7
hide hand_sprite
scene bathroom_start_worried with dissolve
ms "Hal -hal yang tidak ingin saya katakan dengan keras."
ms "Hal -hal yang bahkan tidak ingin saya pikirkan."
ms "Mungkin saya tidak pantas mendapatkan iman dan kepercayaannya."
ms "Karena iman__tag_0__ adalah bohong."
ms "Dan kepercayaan adalah rasa sakit yang Anda izinkan orang lain timpa pada Anda."
scene bathroom_start_worried_2 with dissolve
ms "Dan mungkin itulah yang dia inginkan?"
ms "Mungkin kedengarannya egois, tapi saya ingin lebih. __Tag_0__ Saya ingin lebih banyak petualangan, lebih banyak hasrat, lebih banyak kebebasan."
scene bathroom_start_sad with dissolve
ms "Saya mencintai Paul, tetapi kadang -kadang sepertinya dia tidak mengerti saya. __Tag_0__e sangat peduli pada saya sehingga saya mulai merasa terlindungi, seperti di kandang emas."
ms "Dan saya tidak tahu harus berbuat apa. __Tag_0__meybe saya perlu berbicara dengannya, tapi saya takut dengan reaksinya."
ms "Semua ini terdengar sangat konyol. __Tag_0__i harus senang dengan apa yang saya miliki. __Tag_0__but saya tidak bisa menahan diri. Saya ingin lebih. Saya ingin merasa hidup."
scene bathroom_start_naughty with dissolve
ms "Pikiran -pikiran ini memakan saya. __Tag_0__ pasti ketika rutinitas menjadi sangat membosankan sehingga pikiran saya mulai menyembunyikan kenyataan dari saya."
ms "Di mana saya tidak harus membuat keputusan.Itu mengirim saya ke dunia fantasi. __Tag_0__a dunia di mana saya tidak harus menjadi gadis yang baik. __Tag_0__a dunia di mana saya bukan seorang ratu."
scene bathroom_start_naughty_2 with dissolve
ms "Saya seseorang yang jauh lebih buruk. Seseorang ... __tag_0__ berbeda."
ms "Seseorang yang tidak pernah bosan berbicara tepat setelah menyapa. __Tag_0__esomeone yang tidak merasa jijik dengan perhatian, tetapi malah sangat membutuhkannya."
ms "Seseorang yang tahu bagaimana menikmati hidup dan berjuang untuk itu."
scene bathroom_start_sad_2 with dissolve
ms "Seseorang yang bukan saya."
stop music

play sound "vibro.mp3"
scene bg apartments with dissolve
show mila camisole_and_shorts_surprised at center:
    xpos 0.6
ms "Saya melompat, keluar dari pikiran saya."
pm "Bagaimana kabarmu, sinar matahari?"
ms "..."
show mila camisole_and_shorts_irritated
ms "Haaaa ..."
show mila camisole_and_shorts_sad_looking_aside
ms "Saya tidak ingin menjawab. Jika saya mengatakan yang sebenarnya, dia akan mulai berkotek dan merengek .__ tag_0__ dia mungkin akan menyarankan saya untuk menemui terapis."
ms "Saya tidak ingin menyelesaikan masalah saya .__ TAG_0__ Saya tidak ingin menyelesaikan apa pun."
ms "Minat saya melayang lebih jauh dan jauh dari normal."
ms "Pada awalnya, saya membaca novel romantis dan membayangkan diri saya sebagai pahlawan wanita, terjebak dalam angin puyuh peristiwa."
ms "Namun seiring waktu, kisah -kisah yang membuat saya tertarik menjadi semakin bengkok dan erotis."
show mila camisole_and_shorts_naughty
ms "Lalu saya membaca fanfik terkenal dan mencoba membayangkan diri saya sebagai seorang penurut .__ tag_0__ seorang budak."
ms "Dan ide ini sangat membuat saya terpesona sehingga saya mendaftar di situs kencan untuk orang-orang yang berpikiran sama."
ms "Ternyata ada banyak seperti saya .__ tag_0__ Sulit untuk menemukan seseorang yang bisa dan tahu bagaimana mendominasi daripada mereka yang ingin mengirimkan."
play sound "vibro.mp3"
pm "Apakah kamu sibuk?"
show mila camisole_and_shorts_sad_looking_aside
ms "Saya tidak pernah berani memberi tahu Paul tentang ini. Kehidupan seks kami adalah vanilla yang sakit -sakitan."
ms "Dia tidak ingin bereksperimen, dan saya takut menunjukkan kepadanya sisi yang salah dari saya, yang dia nikahi. Takut tampak sesat."
ms "Bagaimana cara memberitahunya tentang ini?"
ms "Apalagi karena dia selalu sibuk ..."
play sound "vibro.mp3"
pm "Saya akan bekerja terlambat hari ini."
show mila camisole_and_shorts_irritated
m "*Mendesah*"
show mila camisole_and_shorts_embarassed
ms "So that's why I opened up my true self \"there\". Di forum dengan halaman, hitam seperti keinginan saya."
nvl clear
dm "Tuliskan pengukuran dan berat badan Anda."
show mila camisole_and_shorts_irritated_2
ms "That was the first thing Dick wrote to me. No \"hello\", no \"what's your name\", no \"what are you looking for on this site\"."
ms "Saya tidak tahu apa yang membuat saya menjawab pesan arogan dan kurang ajar ini. Tapi sesuatu yang ada di nada suaranya membuatku menjawab."
md "Mengapa?"
dm "Saya ingin tahu."
show mila camisole_and_shorts_smirk
md "Dan saya ingin satu juta dolar dan helikopter."
dm "Anda tidak akan mendapatkannya di situs ini."
md "TIDAK?"
dm "Tidak. Dan Anda datang ke sini bukan untuk itu."
show mila camisole_and_shorts_naughty
ms "Sesuatu menghantam hatiku. Saya menatap layar dan menunggu. Menunggu dia untuk mengatakan apa yang tidak ingin saya dengar."
dm "Anda datang ke sini karena Anda ingin seseorang melihat Anda yang sebenarnya."
show mila camisole_and_shorts_naughty_surprised
ms "Jantungku berdegup kencang. Seorang asing di sisi lain layar tahu lebih banyak tentang saya daripada suami saya, yang telah mengenal saya selama lebih dari sepuluh tahun."
dm "Saya ingin tahu. Aku ingin menemuimu. Anda yang sebenarnya. Dalam semua kecantikan dan keburukan, kekotoran, dan kemurnian Anda."
ms "..."
show mila camisole_and_shorts_thinking
ms "Saya ragu -ragu selama beberapa menit lagi."
ms "Untuk beberapa alasan, bagi saya sepertinya dia sedang menunggu. Menunggu jawaban saya dengan ketegangan."
ms "Perasaan itu sedemikian rupa sehingga terasa seperti saya berdiri di depannya. Dan tatapannya melahap tubuhku. Menyaksikan setiap gerakan otot di wajah saya."
show mila camisole_and_shorts_embarassed2
md "Berat badan saya 54 kilogram ..."
dm "Oh, bagus, sungguh manis!"
show mila camisole_and_shorts_shy_smile
ms "Saya tersenyum."
dm "Berapa usiamu?"
md "Saya tiga puluh dua."
dm "Telah menikah?"
show mila camisole_and_shorts_embarassed
ms "I didn't like that I hesitated before answering as if I wanted to say \"No\".__ tag_0__ Tapi bagaimanapun, jari -jari saya masih mengetuk layar."
md "Ya."
dm "Ha ha. Jadi Anda selingkuh?"
show mila camisole_and_shorts_irritated_2
md "TIDAK!"
ms "Pertanyaannya membuatku marah. Saya tidak akan pernah! .."
dm "Ha ha. Hanya berencana untuk? Mengerti, mengerti."
show mila camisole_and_shorts_angry
ms "Beraninya dia?"
ms "Saya tidak merencanakan apa pun!"
ms "Saya hanya bereksperimen."
show mila camisole_and_shorts_embarassed2
ms "Sedikit ..."
dm "Berapa ukuran bra Anda?"
show mila camisole_and_shorts_sad_looking_aside
ms "Apakah saya benar -benar harus menjawabnya?"
ms "Mengapa saya bahkan berbicara dengannya?"
md "Saya seorang+ cangkir."
show mila camisole_and_shorts_embarassed
ms "Aaaand __tag_0__i menjawab."
dm "A+?"
dm "Apakah itu cara mengatakan Anda tidak memiliki payudara, tetapi Anda berusaha sangat keras untuk memasukkannya ke dalam bra?"
show mila camisole_and_shorts_irritated_2
ms "Oh, tutup mulut!"
dm "Kirimkan saya selfie."
show mila camisole_and_shorts_embarassed2
ms "Jantungku mulai berdebar seperti orang gila lagi .__ tag_0__ ini berbahaya."
ms "Jika saya melakukan ini, tidak ada jalan untuk kembali .__ tag_0__ jika saya melakukan ini, semua orang mungkin mencari tahu siapa saya sebenarnya."
ms "Mereka akan menunjuk jari."
ms "Tertawa di belakang punggungku."
ms "Saya tidak akan pernah bisa mencucinya dari hidup saya."
ms "..."
show mila camisole_and_shorts_biting_lips
ms "..."
ms "..."
show mila camisole_and_shorts_embarassed2
md "Saya tidak ingin"
dm "Bagaimana lagi saya tahu Anda tidak palsu?"
dm "Mungkin Anda pria berkeringat gemuk yang suka berpura -pura memiliki istri yang selingkuh?"
show mila camisole_and_shorts_angry
md "Saya bukan seorang pria."
dm "Buktikan itu."
show mila camisole_and_shorts_naughty
ms "Saya menurunkan tangan saya dan menyentuh diri saya sendiri .__ tag_0__ vagina saya basah .__ tag_0__ tekanan dan permintaan menyalakan saya .__ tag_0__ Saya menyukainya, lebih menyukainya."


menu:
    "I should stop here ({color=#ad9546}\"Loyal\"{/color} / {color=#c57d43}\"Polyamorus (harem)\"__tag_0__ rute)":
        jump Loyal
    "Tidak ada salahnya jika tidak ada yang tahu ... (__tag_0__cheating__tag_1__ / __tag_2__sharing__tag_1__ rute)":

        jump NTR_Netorase


label NTR_Netorase:
show mila camisole_and_shorts_shy_smile
md "Apakah Anda berjanji untuk tidak mempostingnya di mana saja?"
dm "Ya."
show mila camisole_and_shorts_embarassed
md "Tunggu."
ms "Jantungku berdebar kencang di pelipisku. Saya membutuhkan waktu lama untuk memilih sudut. Redid foto beberapa kali sampai akhirnya saya memutuskan, mengenakan topeng di wajah saya terlebih dahulu."
play sound "shot.mp3"
show mila camisole_and_shorts_shy_smile
ms "..."
show dick_selfie1x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "__Tag_0__"
hide dick_selfie1x
md "Ini dia."
dm "Nah, kamu manis."
ms "Bukannya saya sangat senang dengan pujian itu."
dm "Dan Anda tidak punya payudara."
show mila camisole_and_shorts_angry
ms "?!"
ms "Hanya karena saya tidak memiliki bazonga besar bukan berarti saya tidak punya payudara."
show mila camisole_and_shorts_naughty_surprised
dm "Tapi saya masih ingin mengambilnya."
show mila camisole_and_shorts_shy_smile
ms "Bajingan ..."
dm "Jangan menutupi wajah Anda lagi."
show mila camisole_and_shorts_embarassed
ms "Tentu, terus bermimpi."
ms "Mengapa Anda bahkan berpikir saya akan mengirimkan sesuatu kepada Anda?"
dm "Aku menyukaimu. Aku ingin bermain denganmu, gadis."
show mila camisole_and_shorts_embarassed2
ms "Apa maksudnya?"
dm "Bagaimana harimu berlalu?"
show mila camisole_and_shorts_sad_looking_aside
md "Saya bangun, melakukan hal -hal saya, dan tidur."
dm "Wow, itu mungkin deskripsi paling rinci dari rutinitas harian yang pernah saya lihat! 😂"
md "Maaf, saya tidak terlalu baik dengan perkenalan. Apa yang ingin Anda ketahui?"
dm "Apakah ada sesuatu dalam hidup Anda yang memberi Anda kegembiraan?"
show mila camisole_and_shorts_naughty_surprised
ms "Saya tersesat karena kata -kata dan tidak tahu bagaimana menjawab."
dm "Apakah ada sesuatu yang bisa Anda tersesat dan tidak memperhatikan waktu berlalu? Sesuatu yang dapat Anda bicarakan tanpa henti jika ditanya?"
show mila camisole_and_shorts_sad_looking_aside
md "Aku tidak tahu."
md "Saya suka menjahit."
md "Kukira..."
dm "Jahit?"
show mila camisole_and_shorts_shy_smile
md "Ya."
md "Saya dapat menghabiskan berjam -jam memilih pola, menggambar desain, mencari kain, dan menyiapkan pola."
md "Saya memiliki manekin sendiri, mesin dengan overlock, dan bahkan mesin rajutan semi-otomatis Jepang."
md "Saya mendedikasikan semua waktu luang saya untuk ini."
show mila camisole_and_shorts_grin3
md "Misalnya, saya hampir selesai dengan blus sekarang."
md "Saya hanya perlu membuat kembali lengan baju dan menjahit kancing."
md "Kain ini tidak mudah dikerjakan."
md "Sangat tipis sehingga robek jika Anda menjahit dengan jahitan yang terlalu kecil, tetapi jika Anda menggunakan yang lebih besar, ia meninggalkan kerutan."
dm "Jadi begitu"
show mila camisole_and_shorts_embarassed3
ms "Saya menghentikan diri saya sendiri. Fiuh, itu sudah dekat. Siapa yang tertarik mendengarkan saya berbicara tentang menjahit?"
show mila camisole_and_shorts_embarassed2
ms "Saya orang idiot."
show mila camisole_and_shorts_sad_looking_aside
md "Saya minta maaf"
dm "Untuk apa?"
show mila camisole_and_shorts_sad_looking_down
md "Anda mungkin bosan dengan saya."
md "Saya berbicara terlalu banyak, bukan?"
show mila camisole_and_shorts_worried
ms "Kenapa dia tidak menanggapi?"
ms "Saya mulai mengetik pesan dan kemudian menghapusnya lagi karena saya tidak yakin harus berkata apa dalam situasi ini."
ms "Dan mengapa saya bahkan ingin mengatakan sesuatu?"
ms "..."
show mila camisole_and_shorts_irritated_2
ms "Seluruhnya dengan itu"
ms "Saya mencoba mengalihkan perhatian diri saya dan melakukan pembersihan, tetapi pikiran saya terus kembali ke percakapan ini."
ms "Saya ingin menyingkirkan telepon saya, tetapi saya membuka obrolan lagi dan menatap pesan terakhir saya."
show mila camisole_and_shorts_shy
ms "Napas saya lebih cepat. Saya tahu saya tidak melakukan kesalahan, tapi ..."
ms "Saya ingin memohon pengampunan."
show mila camisole_and_shorts_embarassed
ms "Saya ingin merasa terhina."
ms "Saya ingin seseorang menghukum saya karena pikiran bodoh saya."
show mila camisole_and_shorts_sad_looking_aside
md "Apakah saya melakukan sesuatu yang salah?"
ms "Statusnya berkedip, dia membaca pesan itu tetapi tidak membalas."
show mila camisole_and_shorts_embarassed2
ms "Saya tertelan. Wajahku terbakar karena rasa malu, dan ada benjolan yang panas dan gatal di perutku."
md "Bisakah saya menebus kesalahan saya?"
dm "Berlutut dan lutut selfie jika Anda ingin meminta maaf."
show mila camisole_and_shorts_angry
ms "Mohon maaf? __ tAG_0__ Mohon maaf untuk apa?"
ms "Saya tidak melakukan kesalahan"
show mila camisole_and_shorts_shy
ms "Tetapi..."
ms "Saya menyarankannya sendiri, bukan?"
ms "Perlahan -lahan aku berlutut dan mulai menyesuaikan sudut."
show mila camisole_and_shorts_naughty
ms "Dia ingin foto dengan wajahku ... tapi apakah itu sepadan?"
ms "Jika seseorang mengetahuinya, saya akan memiliki masalah."
show mila camisole_and_shorts_biting_lips
ms "Semakin saya memikirkannya, semakin saya ingin melakukannya."
ms "Dan semakin saya ingin melakukannya, semakin saya terangsang."
play sound "shot.mp3"
ms "..."
show dick_selfie2x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "__Tag_0__"
hide dick_selfie2x
show mila camisole_and_shorts_shy_smile
dm "Anak yang baik."
dm "Saya hanya sibuk, Anda tidak perlu meminta maaf."
show mila camisole_and_shorts_surprised
dm "Tetapi tindakan Anda menunjukkan potensi besar."
ms "Saya jatuh ke tempat tidur dan menekan wajah saya ke bantal."
show mila camisole_and_shorts_hiding_face
ms "AAAA"
ms "Saya orang idiot!"
play sound "vibro.mp3"
dm "Tetap..."
dm "Jika Anda menutupi wajah Anda dengan topeng sekali lagi - ini sudah berakhir"
show mila camisole_and_shorts_embarassed2
ms "..."
dm "Dipahami?"
ms "..."
show mila camisole_and_shorts_biting_lips
ms "Apakah saya benar -benar mempertimbangkan ini? ..."
md "Ya"
"..."
show mila camisole_and_shorts_shy_smile
dm "Bagus"
"..."
dm "Apa yang tidak kamu sukai dari kehidupan pernikahan?"
show mila camisole_and_shorts_worried
md "Saya tidak mengatakan saya tidak menyukainya."
dm "Tapi kamu di sini. Pasti ada alasan untuk itu."
show mila camisole_and_shorts_thinking
ms "Saya tidak tahu harus berkata apa."
dm "Ada sesuatu yang orang asing yang bahkan tidak dimiliki teman terdekat - kemampuan untuk secara terbuka membicarakan apa pun."
show mila camisole_and_shorts_shy
dm "Ini seperti berbicara dengan terapis."
dm "Hanya lebih baik."
dm "Gratis."
dm "Dia tidak memuaskanmu secara seksual?"
show mila camisole_and_shorts_sad_looking_down
md "TIDAK"
md "Semuanya baik -baik saja."
ms "Saya tidak suka bahwa saya ragu -ragu sebelum mengetiknya"
dm "Tapi apakah dia melakukan sesuatu yang salah?"
show mila camisole_and_shorts_embarassed
ms "Saya tersipu."
ms "Membicarakannya sepertinya memalukan."
ms "Tidak menyenangkan."
ms "Salah."
ms "Sebelumnya saya tidak akan pernah mengatakannya dengan keras."
show mila camisole_and_shorts_shy_smile
ms "Tapi sekarang saya merasa seperti orang yang berbeda."
show mila camisole_and_shorts_embarassed2
md "Ya..."
md "Mungkin..."
dm "Apakah Anda tidak menyukai ukurannya?"
show mila camisole_and_shorts_naughty_surprised
md "Apa maksudmu?"
show mila camisole_and_shorts_embarassed3
md "Oh..."
show mila camisole_and_shorts_embarassed
ms "Saya tersipu"
md "Jadi begitu..."
md "Tidak, semuanya baik -baik saja."
show mila camisole_and_shorts_embarassed2
md "Mungkin."
md "Aku tidak tahu."
dm "Pernahkah Anda mencoba penis lain?"
show mila camisole_and_shorts_angry
md "Tentu saja tidak!"
dm "Bagaimana dengan mainan?"
show mila camisole_and_shorts_embarassed
ms "Um ..."
md "Tabung deodoran ..."
dm "Saya akan tertawa jika tidak begitu menyedihkan ..."
dm "Apa yang Anda bayangkan?"
show mila camisole_and_shorts_thinking
ms "Mengapa dia mengubah tema begitu cepat?"
show mila camisole_and_shorts_giggle
md "Oh, saya ingin mengunjungi Prancis!"
md "Berjalan di sepanjang jalan -jalan sempit Eropa tua ..."
md "Atau pergi ke butik modis dan kunjungi atelier yang terkenal ..."
dm "Sangat menarik."
dm "Tapi saya tidak bermaksud begitu."
dm "Maksud saya, apa pendapat Anda ketika Anda melakukan masturbasi."
show mila camisole_and_shorts_embarassed3
ms "Oh..."
show mila camisole_and_shorts_embarassed2
ms "Saya merasa bodoh."
ms "Dia tidak tertarik dengan mimpiku."
ms "Dan saya sebagai pribadi."
ms "Dia hanya tertarik pada tubuh saya ..."
show mila camisole_and_shorts_biting_lips
ms "Sedikit bibirku."
ms "Saya menyukainya."
ms "Itu sebabnya saya di sini."
ms "Gairah membuatnya sulit untuk berpikir jernih."
ms "Saya merasa mabuk dengan nafsu."
ms "Saya ingin mengatakan sesuatu yang ceroboh."
ms "Sesuatu yang seksual dan berani."
show mila camisole_and_shorts_grin
md "Saya membayangkan diri saya kacau oleh banyak pria."
md "Untuk digunakan seperti boneka karet."
md "Seolah -olah hanya objek untuk memuaskan nafsu mereka."
show mila camisole_and_shorts_naughty
ms "Aku bernafas berat."
ms "Darah bergegas ke pipiku."
ms "Saya sangat membayangkannya."
ms "Dan saya menyukainya."
dm "Apakah Anda membayangkan diri Anda sebagai pelacur?"
show mila camisole_and_shorts_biting_lips
ms "Saya tertelan."
md "Ya."
dm "Jadi Anda suka mengirimkan dan menyajikan jantan terangsang?"
md "__tag_0__"
dm "Katakan."
dm "Katakan dengan keras."
show mila camisole_and_shorts_irritated_2
ms "Omong kosong apa."
ms "Dia tidak akan tahu apakah saya mengatakannya atau tidak."
show mila camisole_and_shorts_biting_lips
ms "Bibirku kesemutan dengan kegembiraan."
ms "Vagina saya gatal dan mengidam perhatian .__ tag_0__ Saya bisa merasakan betapa basah celana saya."
show mila camisole_and_shorts_embarassed
m "SAYA..."
ms "Suaraku terdengar kasar dan serak."
m "Saya ... ingin dilirik oleh pria terangsang."
show mila camisole_and_shorts_grin
ms "Hehe."
ms "Itu keluar konyol."
show mila camisole_and_shorts_embarassed2
m "Saya seorang pelacur"
show mila camisole_and_shorts_grin2
m "Ha ha."
show mila camisole_and_shorts_embarassed3
m "SAYA SEORANG PELACUR!"
show mila camisole_and_shorts_grin3
ms "HA HA HA"
ms "Sesuatu meledak dari saya bersama dengan tawa."
ms "Sukacita."
ms "Kebanggaan."
ms "Dan rasa pembebasan dari a__tag_0__ sangat, __ tag_0__ sangat, __ tag_0__ penjara yang sangat lama."
ms "Seolah -olah rantai yang tidak terlihat menarik jiwaku seumur hidupku."
ms "Dan rantai itu akhirnya menghilang."
dm "Dengan baik?"
show mila camisole_and_shorts_embarassed
ms "Dia tidak bisa mendengarku, bukan?"
show mila camisole_and_shorts_embarassed2
ms "Dia tidak bisa, kan?"
dm "Apakah Anda mencobanya?"
show mila camisole_and_shorts_thinking
md "Ya."
dm "Dan Anda menyukainya."
show mila camisole_and_shorts_embarassed
md "Ya."
dm "Aha."
dm "Anda adalah pelacur yang lahir alami."
show mila camisole_and_shorts_shy_smile
dm "Nah, sekarang kita sudah menyelesaikannya ..."
dm "Menanggalkan pakaian."
show mila camisole_and_shorts_surprised
ms "?!"
show mila camisole_and_shorts_angry
md "Maaf, apa?"
dm "Menanggalkan pakaian."
dm "Saya ingin melihat Anda telanjang."
ms "Saya membuang telepon seolah -olah menjadi panas."
ms "Kata -katanya pertama kali mendidih pikiran saya, dan kemudian menyedihkan saya, seolah menyiram saya dengan seember air es."
ms "And the proper, well-behaved girl inside me screamed - \"No!.{w} Don't do this!\"."
play sound "vibro.mp3"
show mila camisole_and_shorts_worried
ms "Tapi kemudian rasa ingin tahu dan gairah mengambil alih lagi."
play sound "vibro.mp3"
ms "Saya mengambil telepon di tangan saya dan ragu -ragu untuk membuka kunci layar."
play sound "vibro.mp3"
ms "Itu terus berdengung di tangan saya."
ms "Saya takut membaca pesan Dick."
ms "Takut bahwa saya akan mengambil alih dan saya tidak akan bisa menolak."
show mila camisole_and_shorts_shy
ms "Dan lakukan sesuatu yang memalukan."
ms "Dan bagian terburuk - bahkan tidak menyesal melakukannya."
dm "Bayangkan saja Anda menjadi sorotan."
dm "Bahwa saya dan pria -pria lain melahap tubuh Anda dengan pandangan penuh nafsu."
show mila camisole_and_shorts_embarassed
dm "Anda merasakan panas dan gatal, bukan?"
dm "Kulit Anda menjadi sangat sensitif sehingga pakaian terasa kasar dan tidak perlu."
show mila camisole_and_shorts_biting_lips
dm "Anda merasa seperti Anda bukan diri Anda yang sebenarnya"
dm "Sedikit menggoda kami."
dm "Tunjukkan tubuh Anda."
dm "Seperti budak yang baik Anda."
show mila camisole_and_shorts_dazed
ms "Saya merasa dihipnotis"
ms "Kakiku baru saja pergi ke kamar mandi"
scene br
show mila2 camisole_and_shorts_dazed at left
ms "Dick berkata ...__ tag_0__ Tidak ada lagi penutup wajah ..."
ms "Saya perlu membuat selfie yang kotor, tanpa menyembunyikan wajah saya ..."
show mila camisole_and_shorts_angry at right with hpunch
ms "The remains of my consciousness fought with the \"new me\""
ms "And the \"new me\"menang"
show mila camisole_and_shorts_worried at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
ms "Semua orang akan dapat melihat saya ..."
ms "Dan Paul ..."
show mila camisole_and_shorts_angry at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
ms "Apa yang akan dia lakukan jika dia tahu?"
show mila2 camisole_and_shorts_dazed at left:
    easein 0.7 xzoom 1.1 yzoom 1.1
    easein 0.3 xzoom 1 yzoom 1
ms "Pertanyaan -pertanyaan itu ..."
show mila camisole_and_shorts_angry:
    easein 0.5 xzoom 0.9 yzoom 0.9 yalign 1.0
ms "Terlalu rumit ..."
ms "..."
show mila camisole_and_shorts_angry at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5):
    easein 0.5 xzoom 0.8 yzoom 0.8 yalign 1.0
ms "Diri saya yang kedua terus berteriak pada saya"
show mila camisole_and_shorts_angry at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5):
    easein 0.5 xzoom 0.7 yzoom 0.7 yalign 1.0
ms "Tapi suaranya menjadi lebih tenang sampai aku tidak bisa mendengarnya sama sekali."
hide mila with dissolve
"..."
ms "Pesona oleh pikiran saya sendiri, saya mendekati wastafel dan membasahi kamisol saya dengan air"
play sound "shot.mp3"
show mila2 camisole_and_shorts_dazed at center:
    xpos 0.6
ms "..."
hide mila2
show dick_selfie3x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "__Tag_0__"
hide dick_selfie3x
dm "Tidak buruk."
dm "Tetapi..."
show mila camisole_and_shorts_scared_shy at center:
    xpos 0.6
md "Saya melepas topeng!"
dm "Jadi begitu"
dm "Tapi Anda masih menutupi wajah Anda"
dm "Jangan"
show mila camisole_and_shorts_sad_looking_aside
md "Saya tidak yakin bahwa saya bisa ..."
md "Maksudku harus ..."
md "Maksud saya..."
ms "..."
dm "Kemudian tarik bajumu dan tunjukkan payudara Anda, pelacur."
show mila camisole_and_shorts_embarassed2
ms "Saya tertelan"
ms "Lebih bersemangat daripada malu, saya sedikit ragu."
ms "Itu ...__ tag_0__ saya bisa melakukan ...__ tag_0__ Saya dengan patuh mengangkat bajuku dan mengambil foto lain."
ms "Perasaan kebebasan dan gairah membanjiri saya ..."
play sound "shot.mp3"
show mila camisole_and_shorts_shy_smile
ms "..."
show dick_selfie4x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "__Tag_0__"
hide dick_selfie4x
dm "Lepaskan bajumu."
show mila camisole_and_shorts_topless_biting_lips
ms "Kemeja itu jatuh ke kakiku."
ms "Saya melihat refleksi saya di cermin seolah -olah untuk pertama kalinya."
show mila camisole_and_shorts_topless_smug
ms "ME yang lain sedang menatapku."
ms "Berani, kurang ajar, dan seksi."
ms "Saya memandang diri saya seperti itu dan terangsang."
ms "Saya benar -benar ingin menanggalkan pakaian."
ms "Saya ingin menunjukkan diri saya."
show mila camisole_and_shorts_topless_caress
ms "Tunjukkan setiap ..."
ms "Bagian..."
ms "Dari tubuh saya ..."
play sound "shot.mp3"
ms "..."
show dick_selfie5x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "__Tag_0__"
hide dick_selfie5x
play sound "shot.mp3"
show mila camisole_and_shorts_topless_biting_lips
ms "Saya bahkan tidak peduli bahwa saya menunjukkan wajah saya"
ms "Jari -jariku melepaskan tali celana pendek"
ms "Jantungku berdetak seperti orang gila"
play sound "shot.mp3"
ms "..."
show dick_selfie6x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "__Tag_0__"
hide dick_selfie6x
show mila camisole_and_shorts_topless_smug
ms "Dan dengan setiap tembakan diambil, suara saya yang kedua menjadi lebih keras dan lebih keras."
play sound "shot.mp3"
ms "..."
show dick_selfie7x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "__Tag_0__"
hide dick_selfie7x
ms "Itu memberi tahu tubuh saya apa yang harus dilakukan."
ms "Dan tubuh saya mematuhi perintah -perintah itu dengan penuh semangat."
show mila camisole_and_shorts_topless_biting_lips
ms "Celana ini menempel pada vagina basah saya dengan kain tipis."
ms "Saya belum pernah merasa begitu terangsang sebelumnya."
ms "Gairah itu menelan saya, __ tag_0__ mengkonsumsi saya, _ tag_0__ menuntut lebih dan lebih .__ tag_0__ itu seperti obat."
play sound "vibro.mp3"
dm "Lepaskan celana dalam Anda, berbalik dan sebarkan pantat Anda."
dm "Begitulah cara pelacur mengundang tuannya."
show mila camisole_and_shorts_topless_smug
ms "Saya memalingkan muka dari layar dan melihat refleksi saya."
ms "Percikan di mataku terbakar lebih cerah dan lebih cerah."
ms "Kepala saya memprotes sikapnya terhadap saya dan kata -katanya."
show mila camisole_and_shorts_topless_caress_licking_lips
ms "Tapi tanganku menarik celana dalam ..."
play sound "shot.mp3"
ms "..."
show dick_selfie8x at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
md "__Tag_0__"
hide dick_selfie8x


play sound "door-open-close.mp3"
show mila camisole_and_shorts_topless_surprised
ms "Berengsek!"
ms "Saya kehilangan jejak waktu ..."
p "__Tag_0__honey!"
ms "Bajuku basah, jika aku keluar seperti ini ..."
p "__Tag_0__sweetie, apakah kamu di rumah?"
show mila oversized_shirt_shy
ms "Saya mengenakan kemeja Paul"
ms "Apakah ini oke? __ tag_0__ Bisakah saya menyapa dia seperti ini?"
ms "..."
scene bg door with fade
scene bg mila_shirt_tug
m "H-HI."
p "Halo sayang"
ms "Paul tidak melihat pada awalnya - dia melihat layar teleponnya"
ms "Tapi setelah beberapa detik ..."
p "Bagaimana ..."
scene bg mila_shirt_tug2
p "Wow!"
"..."
p "Ini..."
p "Ini..."
p "Apa ini?"
ms "Tatapannya berkeliaran di tubuhku."
scene bg mila_shirt_tug3
ms "Paul menatapku dengan tampilan yang sama sekali berbeda."
ms "Bukan ayah yang biasa dan merendahkan."
ms "Tapi yang bernafsu ..."
ms "Dan itu semakin membangkitkan saya."
scene bg mila_shirt_tug4
m "SAYA..."
ms "Saya ingin dia menekan saya ke dinding di sini ..."
m "Saya menaruh semuanya di mesin cuci ... __tag_0__ jadi ..."
ms "Jadi dorong aku ke sini di sini dan persetan denganku seperti tidak ada hari esok !!!"
p "I-saya lihat ..."
ms "Jelas Paul tidak melakukannya ..."
ms "Saya malu dengan pikiran saya sendiri."
ms "Paul, merah sebagai lobster, berjalan ke ruang tamu, berusaha untuk tidak melihat saya."
"..."
scene bg mila_shirt_tug5
ms "Nah ... __tag_0__ apa lagi yang saya harapkan?"
ms "Dia selalu lelah setelah bekerja."
ms "Itu adalah perilakunya yang biasa ..."
ms "Tapi mengapa itu sangat mengganggu saya?"
scene bg mila_shirt_tug6
ms "... Tidak, sungguh, mengapa itu sangat mengganggu saya?"
ms "Mungkin..."
ms "Mungkin saya harus berbicara dengannya tentang ... __tag_0__ semua ini?"
ms "Saya merasa, dengan semua yang saya lakukan, saya baru saja tenggelam lebih dalam"
ms "Mungkin aku membutuhkan ksatriaku ..."

menu:
    "Saya harus berbicara dengan Paul sebelum saya membuat lebih banyak kesalahan ... (__ tag_0__sharing__tag_1__ rute)":
        jump Netorase
    "Saya melakukan apa yang saya inginkan, dan tidak ada yang akan menghentikan saya (__tag_0__cheating__tag_1__ rute)":

        jump NTR


label Netorase:

ms "SAYA…"
ms "Saya harus menceritakan semuanya padanya ..."
ms "Sebelum saya melakukan sesuatu yang bodoh ..."
ms "Ini tidak bisa berlangsung lagi."
"__tag_0 __..."
scene bg apartments
ms "Saya memberi tahu Paul segalanya."
ms "Dia tidak ingin percaya apa yang dia dengar"
ms "Tapi begitu saya menunjukkan foto -fotonya, wajahnya berubah"
ms "Dia akhirnya menyadari"
ms "Dia akhirnya percaya"
ms "Kejutan berubah menjadi kemarahan"
ms "Saya belum pernah melihatnya seperti ini"
ms "Dan saya menjadi takut"
ms "Tapi selain ketakutan, perasaan lain muncul di hatiku ..."
"__tag_0 __..."
scene bg talking_out1
m "Paul?"
ms "..."
m "SAYA…"
scene bg talking_out2
p "Diam."
ms "Suaranya terdengar kasar dan rendah"
ms "Sepertinya orang lain berbicara dengan saya"
ms "Atau sesuatu yang berbeda"
ms "Sesuatu yang jahat dan agresif"
ms "Sesuatu yang kebinatangan ..."
ms "Takut meremas tenggorokanku"
ms "Tapi dengan itu datang kegembiraan"
ms "Rasa bahaya yang belum pernah terjadi sebelumnya memabukkan saya"
ms "Saya tertelan ..."
scene bg talking_out3
ms "...{image=emoji/heart.png}"
ms "..."
scene bg talking_out4
p "Sepanjang hidupku…"
ms "Suara Paul terdengar sangat serak dan rendah ..."
ms "Seolah -olah itu bukan suaranya sama sekali."
p "Saya mencoba menjadi pria yang "baik""
p "Ketika saya diintimidasi di sekolah, saya bertahan"
p "Saya sedang menunggu."
p "Ketika semua orang hidup, mereka hidup dan berkencan di universitas, saya belajar."
p "Karena saya percaya bahwa akan ada seseorang ..."
p "Setidaknya satu orang di dunia buruk ini, yang akan memahami saya."
p "Siapa yang akan menghargai ... __tag_0__my upaya. __Tag_0__LOYALTY saya."
p "Martabat saya, __tag_0__my Honor."
p "Tapi semua gadis yang saya sukai saat itu ..."
p "Jatuh cinta dengan beberapa bajingan"
p "Dan itu membuatku marah."
p "Itu mengubah saya masuk ke luar, __tag_0__i muak dengan kemunafikan dan kebodohan mereka"
p "Tapi tetap saja ... __tag_0__hope terus berkilau di hatiku"
p "Harapan, __tag_0__ yang akan saya temukan ..."
scene bg talking_out5
p "Anda."
"__tag_0 __..."
p "Dan kamu…"
scene bg talking_out6
m "Paul ... aku ..."
scene bg talking_out7
p "Tutup mulut!"
ms "Kata -kata tersangkut di tenggorokanku."
scene bg talking_out8
ms "Tapi teriakan dan ketakutannya tidak membuatku ingin melarikan diri."
ms "Justru sebaliknya."
ms "Saya mengalir seperti pelacur terakhir."
scene bg talking_out9
ms "Aku menggigit bibirku dan menundukkan kepalaku, berusaha untuk tidak memberikan diriku."
p "Anda! __Tag_0__i melakukan segalanya untuk Anda!"
p "Semuanya!"
p "Apa pun yang Anda inginkan, saya melakukannya."
p "Yang saya inginkan sebagai imbalan hanyalah kepercayaan diri, __Tag_0____ yang Anda tidak akan menusuk saya di belakang."
p "Semua yang saya minta sedikit hormat."
p "Dan setidaknya setetes loyalitas sialan."
p "Apakah itu sulit?"
p "Apakah saya bertanya terlalu banyak?"
"__tag_0 __..."
scene bg talking_out10
p "Sialan kenapa?"
ms "..."
p "Mengapa? Mengapa Anda melakukan ini?"
ms "Paul mengepalkan tinjunya dan menamparku"
scene bg talking_out10 with hpunch
m "Ahhh ..."
ms "Saya tidak bisa menahan erangan saya."
ms "Dia menampar saya, tapi itu masih menampar Paul"
ms "Itu tidak menyakiti saya .__ tag_0__ diri saya yang sesat menginginkan lebih dari itu"
ms "Emosinya ...__ tag_0__ rasa sakitnya ...__ tag_0__ kemarahannya"
ms "Saya bahkan ingin memprovokasi dia, jadi saya tidak berusaha keras untuk menyamarkan erangan saya sebagai erangan rasa sakit."
scene bg talking_out9
p "Apakah ini yang Anda inginkan?"
p "Untuk diekspos? __Tag_0__ untuk menjadi pelacur?"
p "Untuk digunakan seperti sesuatu?"
ms "Aku diam -diam menatapnya"
ms "Dia tidak terlihat seperti dirinya sendiri"
ms "Kuat, mengancam, menakutkan"
ms "Seperti binatang yang marah"
ms "Saya menatapnya dan hampir tidak bisa menahan keinginan untuk memasukkan tangan saya ke dalam celana saya ..."
ms "Sial, betapa seksi dia sekarang ..."
p "Sebarkan kakimu"
ms "Suaranya yang memerintah bergema di kepalaku"
ms "Tangannya meraih ke bawah dan menarik celananya."

label hscene_netorase_hatefuck:
scene bg talking_out11
ms "Saya mengangkat kaki saya dan melebarkan vaginaku, merasakan dengan jari -jari saya betapa basahnya saya"
ms "Paul memasuki saya dengan tajam dan cepat"
scene bg talking_out12 with dissolve
ms "Tanpa bertanya, seperti biasa, __tag_0__jap itu menyakitkan, __tag_0__jap"
ms "Dia memuaskan keinginannya dengan tubuh saya"
scene bg talking_out13 with dissolve
ms "Kasar, dengan kemarahan kebinatangan"
scene bg talking_out14 with dissolve
ms "Tangannya yang kuat meraih pantatku dan memegang pinggulku erat -erat"
scene bg talking_out15 with dissolve
m "Ahhh. Ahhh ... ahhhh!"
ms "Saya datang segera dan, tanpa mencoba menyembunyikan orgasme saya, menyerah pada kejang -kejang manis"
m "Ahhhh!"
ms "Ketika saya membuka mata, saya memperhatikan bahwa kemarahannya secara bertahap mulai surut."
ms "Di tempatnya datang nafsu dan kejutan"
scene bg talking_out15a with dissolve
ms "Saya memandang Paul dan tersenyum"
m "Ya, cintaku ...__ tag_0__ inilah yang saya inginkan ..."
ms "Paul meremas pinggulku lebih keras dan setelah beberapa pukulan mulai memompa spermanya ke dalamku"
scene bg talking_out16 with dissolve
ms "Saya menikmati sensasi ini - dinding vagina saya merasakan setiap kejang penisnya"
ms "Paul melepaskan pinggulku dan duduk di sofa dengan kepalanya di tangannya."
ms "Saya tidak tahu bagaimana mendukungnya dan bagaimana menunjukkan kepadanya bahwa tidak ada hal buruk yang terjadi"
scene bg talking_out17 with fade
ms "Aku diam -diam berlutut dan mengambil penisnya ke mulutku, membersihkannya dari sperma."
ms "..."
ms "Paul mengangkat kepalanya dan menatapku dengan terkejut untuk sementara waktu."
p "Apa yang sedang kamu lakukan?"
scene bg talking_out18 with dissolve
ms "Saya menjilat setetes sperma dari penisnya dan menjawab"
ms "Anda sendiri mengatakan bahwa saya pelacur, dan saya berperilaku seperti yang diinginkan suami saya."
ms "Aku menunjukkan lidahku dengan sisa -sisa sperma kemudian menjilat bibirku dan tertelan"
m "Mmm…"
"__tag_0 __..."
scene bg talking_out20 with dissolve
ms "..."
m "Apakah kamu ... membenciku sekarang?"
ms "..."
ms "Paul memalingkan muka."
ms "Aku menyandarkan siku di pangkuannya dan menekan pipiku ke penisnya."
scene bg talking_out21 with dissolve
m "Hidup kita tampak membosankan bagiku, cintaku."
ms "..."
m "SAYA..."
m "I wanted something new. So that you stop considering me \"yours\"."
ms "Paul menatapku dalam ketakutan."
m "Aku bukan apa -apa, cintaku."
m "Saya manusia."
m "Saya seorang wanita."
m "Dan saya tidak akan selalu melakukan apa yang Anda harapkan dari saya."
ms "..."
ms "Paul sedikit santai, tetapi masih diam."
scene bg talking_out20 with dissolve
m "Aku mencintaimu, Paul."
ms "Paul bergetar seolah -olah terpukul."
ms "Saya mengabaikan reaksinya."
m "Aku akan selalu mencintaimu."
m "Dan aku tahu kamu juga mencintaiku."
ms "Paul dengan ragu -ragu mengangkat tangannya dan menepuk kepalaku."
ms "Aku memejamkan mata dan tersenyum."
ms "..."
ms "..."
m "Dengan baik..."
m "Jadi ... katakan dengan jujur ..."
scene bg talking_out21 with dissolve
m "Apakah Anda menyukainya?"
ms "..."
ms "Tangan Paul membeku, tetapi kemudian dia terus membelai kepalaku."
ms "..."
p "Ya.."
ms "Suaranya terdengar tidak pasti. Seolah -olah dia meragukan kata -kata dan perasaannya."
ms "..."
m "Dan apa sebenarnya yang Anda ..."
p "Aku tidak tahu."
ms "Kali ini dia menjawab lebih cepat dan lebih tajam."
ms "..."
ms "..."
m "Anda…"
m "Apakah Anda ingin melakukan hal seperti itu lagi?"
ms "..."
ms "..."
p "Apa sebenarnya?"
ms "..."
m "Dengan baik…"
scene bg talking_out19 with dissolve
ms "Saya menjilat penisnya"
m "Saya belum tahu… belum ..."
ms "..."
m "Misalnya ... Pernahkah Anda membayangkan saya ..."
ms "..."
m "Dalam ... __tag_0__role yang sedikit berbeda? Bukan hanya istri putri polos Anda."
ms "..."
ms "..."
scene bg talking_out18 with dissolve
m "Misalnya, jika saya adalah instruktur kebugaran dan pria gemuk berkeliaran di sekitar saya ..."
ms "Paul tegang."
m "TIDAK?"
ms "..."
scene bg talking_out17 with dissolve
m "Nah, atau mungkin beberapa bawahan Anda dari pekerjaan akan datang kepada kami ..."
m "Anda tahu yang hijau ..."
ms "..."
p "Saya menerima promosi belum lama ini, saya belum memiliki bawahan."
m "Mana yang berarti tidak?"
ms "..."
p "TIDAK."
ms "..."
scene bg talking_out18 with dissolve
m "Mungkin dengan seseorang yang lebih tua?"
ms "Dick Paul berkedut dan menyodok pipiku."
ms "Saya mengangkat mata dan menatapnya."
ms "..."
ms "Paul tidak mengatakan apa -apa."
m "Dengan seseorang yang jelas tidak setara."
ms "Penisnya mulai dipenuhi dengan darah."
scene bg talking_out22 with dissolve
m "Bayangkan seorang pria yang lebih tua yang gemuk dengan kaos Bandit Smoky yang memegangi rambut saya dan meniduriku dari belakang ..."
ms "..."
ms "Penisnya menjadi sangat sulit."
ms "Hehe ..."
m "Seseorang di sini tidak membiarkanmu berbohong."
ms "Paul memalingkan rasa malu dan tidak menjawab."
ms "Aku berlari lidah di sepanjang poros penisnya, seperti yang kulihat dengan porno."
m "Bayangkan dia duduk di tempat tidur, dan saya berlutut di depannya ..."
p "..."
m "Bagaimana penisnya yang tebal dan berbulu menembus mulut kecil saya ..."
ms "Paul tegang seolah -olah sebelum orgasme"
ms "Hehe ..."
m "Bagaimana dia menutupi wajahku dengan sperma tebal ..."
p "Ahhh ..."
ms "Paul tidak tahan dan memulai Cumming"
scene bg talking_out23 with dissolve
ms "Saya membuka mulut saya lebih lebar dan membiarkannya berejakulasi di dalam mulut keinginan saya"
ms "Spermanya terasa manis ..."
ms "Saya dengan mudah menelannya sedikit demi sedikit"
scene bg talking_out24 with dissolve
ms "Ketika penisnya berhenti berkedut, aku meremas tetes terakhir cumnya"
ms "Penisnya menjadi lebih lembut dan lebih kecil"
ms "Saya membuka mulut saya dan menunjukkan kepada Paul yang tersisa"
scene bg talking_out25 with dissolve
m "Ahah…"
m "Apakah itu yang kamu suka?"
p "..."
m "Dipahami"
m "..."
ms "Paul lemas dan terengah -engah."
p "Di mana Anda mempelajarinya?"
ms "Saya mengumpulkan sperma dari pipi saya dengan jari saya dan menjilatnya."
ms "Lalu aku bersandar ke telinganya dan menjawab."
m "Saya menyedot petugas kebersihan lama setiap hari."
ms "..."
ms "Paul menatapku dengan tak percaya."
m "Ahaha"
m "Saya bercanda"
"__tag_0 __..."
if _in_replay:
    return


scene bg apartments
n "Beberapa minggu telah berlalu."
ms "Kehidupan seks kami dipenuhi dengan fantasi bejat"
show mila red_thinking at right:
    xzoom 0.8 yzoom 0.8
ms "Kami berbicara, kami menemukan apa yang kami masing -masing bersembunyi di bawah permukaan"
ms "Yang kami diskusikan dan kemudian menjadi nyata"
show mila red_shy at right:
    xzoom 0.8 yzoom 0.8
ms "Tapi, saya khawatir kita menjadi sedikit lebih berisik dari sebelumnya ..."
ms "Saya harap kami tidak terlalu mengganggu tetangga ..."
show mila red_naughty at right:
    xzoom 0.8 yzoom 0.8
ms "..."
ms "Berpikir tentang tadi malam membuatku agak panas ..."
ms "..."
ms "Saya harus pergi ke toko kelontong untuk menjernihkan pikiran saya ..."
"__tag_0 __..."
scene bg grocery_store
show mila red_bags at right:
    xzoom 0.8 yzoom 0.8
ms "Sial, tasnya sangat berat."
ms "Bagaimana saya bisa menyeret semuanya pulang?"
"__tag_0 __..."
scene bg street
show mila red_sweat at right:
    xzoom 0.8 yzoom 0.8
m "Haah __tag_0__haah"
ms "Oke..."
ms "Ini adalah lingkungan saya"
ms "Yang utama adalah sampai ke pintu masuk ... __tag_0__ lalu lift ... __tag_0__ dan kemudian saya hampir di rumah ..."
ms "Mengapa saya mendapatkan begitu banyak daging? __Tag_0__ dan mengapa saya membeli nanas?"
ms "Jelas mereka bagus, mungkin karena saya mendengar mereka mempermanis sperma pria __tag_0__ *terkikik *"
ms "Tapi sekarang aku perlu membawanya pulang entah bagaimana ..."
ms "Saya hanya akan beristirahat sedikit, dan kemudian melangkah lebih jauh ..."
ms "Aku lelah meletakkan tas dan menghela nafas."
show mila red_rest at right:
    xzoom 0.8 yzoom 0.8
m "Ugh ... punggungku."
ms "Seorang pria paruh baya yang montok dan tinggi muncul di sebelah saya seolah -olah entah dari mana."
ms "Meskipun sangat besar langkahnya sangat sunyi, sehingga saya tidak mendengarnya sama sekali"
ms "Dan meskipun begitu besar, dia membungkuk dalam upaya untuk menyembunyikan kehadirannya, seolah -olah dia tidak ingin orang memperhatikannya"
show mila red_surprised at right:
    xzoom 0.8 yzoom 0.8
ms "Ketika saya mendengar suaranya yang tenang, saya bahkan bergidik."
ms "Pria itu tersenyum canggung."
show someone at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "Permisi ... dapatkah saya membantu Anda?"
ms "..."
ms "Dia sedikit bersandar ke arahku"
ms "Saya mencium aroma keringat yang samar dan cologne murah."
ms "Aku menelan dan bergegas melambaikan tangan di depanku."

show mila red_waving_hands at right:
    xzoom 0.8 yzoom 0.8
m "Tidak, tidak, tidak apa -apa"
ms "Sepertinya wajahnya tidak berubah, tetapi saya merasa penolakan saya telah membuatnya kesal."

hide someone
show bob waving at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "Maaf ... Saya tidak bermaksud menakut -nakuti Anda."
ms "..."

show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "Anda mungkin tidak suka berada di dekat saya, jadi saya akan mengambil cuti saya ..."

show mila red_sad at right:
    xzoom 0.8 yzoom 0.8
ms "Hati saya tenggelam dengan simpati."
ms "Tanpa menyadarinya, saya meraih tangannya."

show mila red_wait at right:
    xzoom 0.8 yzoom 0.8
m "Harap tunggu!"
m "Bahkan, akan lebih bagus jika Anda bisa membantu saya ..."

show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "..."

show mila red_scratch at right:
    xzoom 0.8 yzoom 0.8
m "Saya tidak tahu mengapa saya menolak tawaran Anda. Saya tidak bisa membayangkan bagaimana saya akan mengelola membawa tas -tas ini menaiki tangga."

show bob surprised at left:
    xzoom 0.9 yzoom 0.9
ms "Pria itu mengangkat alisnya terkejut, tidak mempercayai telinganya."
bob_unknown "Hmm ...__ tag_0__ pasti ..."
bob_unknown "..."
m "..."

show mila red_awkward_smile at right:
    xzoom 0.8 yzoom 0.8


show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "..."
ms "Dia agak menyeramkan ..."

show mila red_wait at right:
    xzoom 0.8 yzoom 0.8
m "Tepat di tikungan, __ tag_0__ Gedung apartemen besar itu, Anda tahu?"


show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "..."
bob_unknown "Maksud Anda 32/1 di 3rd st?"

show mila red_scratch at right:
    xzoom 0.8 yzoom 0.8

m "Ya! Anda tahu jalanan dengan cukup baik, haha!"

show mila red_creep at right:
    xzoom 0.8 yzoom 0.8

ms "Menakutkan!"
ms "Pria itu tampak agak sakit dari senyum canggung saya"

show bob sad2 at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "No, I don't know \"the streets\". Saya hanya tinggal di gedung ini"

show mila red_scratch at right:
    xzoom 0.8 yzoom 0.8

ms "Oh ... ok kalau begitu ..."

show mila red_sad at right:
    xzoom 0.8 yzoom 0.8

"Dia mengulurkan tangannya kepada saya dan saya memberinya tas."

"Kami berjalan dalam keheningan yang canggung"
"__tag_0 __..."
"Ketika kami datang ke gedung, kami mengetahui bahwa lift tidak berfungsi"

show mila red_angry at right:
    xzoom 0.8 yzoom 0.8

m "Apakah Anda bercanda?!"
ms "Pria itu tertawa kering"
ms "Saya menatapnya dan kemudian ke tas"
ms "__tag_0 __..."
ms "Nah ... __tag_0__ akan kasar untuk memintanya untuk membawa mereka ke lantai 14 kan?"
ms "Tapi pria itu baru saja berjalan ke tangga"
scene bg stairs
show mila red_awkward_smile at right:
    xzoom 0.8 yzoom 0.8
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "Anda tinggal di 1420R, kan?"
show mila red_creep at right:
    xzoom 0.8 yzoom 0.8

ms "..."
ms "Menakutkan!"
show bob sad at left:
    xzoom 0.9 yzoom 0.9
ms "Pria itu tersenyum sedih lagi dan melihat ke samping"
bob_unknown "Saya tetangga Anda, itu sebabnya saya tahu"


show mila red_sad at right:
    xzoom 0.8 yzoom 0.8

ms "Oh..."
ms "Tunggu jika dia adalah tetangga kita, maka dia pasti telah mendengar ... game baru kita ..."

show mila red_shy at right:
    xzoom 0.8 yzoom 0.8

ms "Saya mencoba menutupi rasa malu saya dengan tawa"

show mila red_scratch at right:
    xzoom 0.8 yzoom 0.8
m "Ahah, maaf, aku seharusnya tahu"

show bob shy at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "Oh jangan khawatir ... __tag_0__i baru saja memperhatikan ... bahwa saya memiliki tetangga"
ms "..."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "Maksud saya, saya tidak terlalu sosial ..."
ms "Saya ingin menjawab, tetapi menaiki tangga mengetuk semua keinginan untuk membicarakan saya"
"__tag_0 __..."

scene bg doors
show mila red_rest at right:
    xzoom 0.8 yzoom 0.8
m "Haaaa ... __tag_0__haaaa ... __tag_0__haaaa ..."
ms "Empat belas lantai, ini bukan lelucon, bukan?"
ms "Saya mencondongkan tubuh ke depan untuk menarik napas"
show cg leaning_red1 at center:
    xzoom 0.5 yzoom 0.5 ypos 1
    linear 1.0 ypos 0.75
ms "Ketika saya melihat ke atas, pria itu berbalik tajam. __Tag_0__ wajahnya berwarna merah cerah."

show bob shy at left:
    xzoom 0.9 yzoom 0.9
ms "Saya melihat ke bawah dan menyadari bahwa membungkuk memberinya pemandangan payudara saya yang sangat baik."
ms "..."

show mila red_shy at right:
    xzoom 0.8 yzoom 0.8

ms "Ya Tuhan ... apakah dia menatapku?"
ms "..."
ms "Yah, bukan karena saya menentangnya ..."
ms "Harga kecil untuk dibayar untuk membantu saya membawa tas."
ms "Mungkin aku bahkan harus menghiburnya sedikit."
ms "Aku lebih tersenyum dan lebih condong ke depan"
m "Terima kasih banyak, tetangga saya yang ramah!"
show cg leaning_red2 at center:
    xzoom 0.5 yzoom 0.5 ypos 1
    linear 1.0 ypos 0.75
ms "Ini akan memberinya pandangan yang sedikit lebih baik."

show bob surprised at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "..."
ms "Hehe"

show bob waving at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "Tidak, tidak, itu bukan apa -apa!"
ms "Dia melambaikan tangannya."


show bob shy at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "Dengan senang hati saya membantu."
show mila red_giggle at right:
    xzoom 0.8 yzoom 0.8
ms "Hehe ..."
ms "Tentu saja itu menyenangkan ..."


hide cg leaning_red2
show mila red_smile at right:
    xzoom 0.8 yzoom 0.8
m "Nama saya Mila. Kami tidak pernah memperkenalkan diri kami ..."

bob_unknown "Anda memiliki nama yang begitu indah!"
m "Terima kasih!"

show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "..."
m "..."

m ".__ tag_0 __.__ tag_0__?"
show mila red_awkward_smile at right:
    xzoom 0.8 yzoom 0.8
m "Dan kamu?"


show bob surprised at left:
    xzoom 0.9 yzoom 0.9
bob_unknown "Oh! __Tag_0__sorry! __Tag_0__i am bob ..."
ms "Itu canggung ..."

show mila red_smile at right:
    xzoom 0.8 yzoom 0.8


m "Nah, senang bertemu denganmu, Bob."
ms "..."

show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "Senang bertemu denganmu juga, Nona"
ms "..."
bob "..."

show mila red_awkward_smile at right:
    xzoom 0.8 yzoom 0.8

ms "Jeda diseret"


show bob sad at left:
    xzoom 0.9 yzoom 0.9
ms "Dia mulai terlihat agak sedih dan tertekan lagi."
ms "Saya menepuk pundaknya dan mengambil tas saya"

show mila red_bags at right:
    xzoom 0.8 yzoom 0.8

m "Oke, saya tidak akan membuang waktu Anda lagi."
bob "Tentu..."
ms "Dia mengerutkan bibirnya dan mengangguk."
ms "Pria besar itu tampak seperti akan menangis."
ms "..."
ms "Saya melihat paket saya."
ms "..."

show mila red_shy at right:
    xzoom 0.8 yzoom 0.8

m "Apakah Anda sudah menikah, Bob?"
ms "..."

show bob sad2 at left:
    xzoom 0.9 yzoom 0.9
ms "Dia menjadi lebih sedih."
bob "TIDAK."
ms "Jawabannya terdengar tajam, jika tidak kasar."
ms "..."

show mila red_waving_hands at right:
    xzoom 0.8 yzoom 0.8

m "Maaf, saya tidak bermaksud menyinggung perasaan Anda."
bob "..."

show mila red_smile at right:
    xzoom 0.8 yzoom 0.8

m "Saya baru saja mengambil banyak daging dan sayuran ..."
m "Maukah Anda membiarkan saya memperlakukan Anda dengan rebusan terkenal di dunia saya?"
bob "..."

show bob surprised at left:
    xzoom 0.9 yzoom 0.9
ms "Bob menatapku dengan tak percaya."
ms "..."

show mila red_awkward_smile at right:
    xzoom 0.8 yzoom 0.8

m "? ..."
m "Anda tidak suka rebusan?"


show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "SAYA BERSEDIA! Ya! Saya menginginkannya, tentu saja saya menginginkannya!"
ms "Dia menunjukkan tasnya yang berisi beberapa bungkus mie instan."
bob "Saya tidak tahu cara memasak dan karena itu saya tidak makan dengan baik ..."

show mila red_nagging at right:
    xzoom 0.8 yzoom 0.8

ms "Aku meletakkan satu tangan di pinggulku dan mengibaskan jari padanya."
m "Anda tidak bisa melakukan itu, Bob! Anda akan memberi diri Anda maag!"
ms "..."


show bob smile at left:
    xzoom 0.9 yzoom 0.9
ms "Bob tersenyum dan menggaruk bagian belakang kepalanya."
bob "Maaf, Nona."
ms "..."

show mila red_scratch at right:
    xzoom 0.8 yzoom 0.8

m "Sebenarnya __tag_0__i Mrs."


show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "Oh ... __tag_0__right ... __tag_0__sure ... __tag_0__ yang sangat ..."
ms "Bob menjadi sedih lagi."

show mila red_sad at right:
    xzoom 0.8 yzoom 0.8

ms "Dia tampak seperti anak anjing yang hilang"
ms "Saya tidak tahan"
ms "Mereka berkata - Berbagi itu peduli ..."
ms "..."

show mila red_shy at right:
    xzoom 0.8 yzoom 0.8

ms "..."
m "Apakah kamu sibuk sekarang?"
"__tag_0 __..."

show bob surprised at left:
    xzoom 0.9 yzoom 0.9
bob "Tidak ... tapi kenapa kamu bertanya?"
ms "..."

show mila red_wait at right:
    xzoom 0.8 yzoom 0.8

m "Nah, Anda bisa membantu saya memasak. Dan pada saat yang sama kita bisa makan malam bersama ..."
m "Paul akan pulang terlambat hari ini, jadi saya khawatir akan menyedihkan menghabiskan malam saya sendirian."
bob "..."

show bob smile at left:
    xzoom 0.9 yzoom 0.9
bob "I .. Ya! __Tag_0__Just Biarkan saya mandi."

show mila red_smile at right:
    xzoom 0.8 yzoom 0.8

m "Tentu, tentu ..."
ms "..."

show mila red_shy at right:
    xzoom 0.8 yzoom 0.8

ms "Saya memiliki gagasan untuk menggodanya lagi, jadi saya menarik kembali kaus saya dan melambaikannya, mengungkapkan pemandangan dada saya."
show cg leaning_red3 at center:
    xzoom 0.5 yzoom 0.5 ypos 1
    linear 1.0 ypos 0.75
m "Ya! Saya perlu mandi juga! __Tag_0__ itu sangat panas hari ini, ya?"

show bob shy at left:
    xzoom 0.9 yzoom 0.9
bob "__Tag_0 __... ya ... __tag_0__ sangat panas."
show mila red_smile at right:
    xzoom 0.8 yzoom 0.8

ms "..."
ms "..."
hide cg leaning_red3
show mila red_waving_hands at right:
    xzoom 0.8 yzoom 0.8
m "Nah, sampai jumpa nanti."
ms "Saya pergi ke apartemen dan menutup pintu."
play sound "door-open-close.mp3"
hide mila red_waving_hands
hide bob shy


"__tag_0 __..."
scene bg bedroom
ms "Saya mandi dan berdiri di depan lemari."
show mila nude_think at right
ms "Hmmm ..."
ms "Bob terlihat seperti seorang pria, yang memohon untuk digoda ..."
ms "Tapi saya tidak boleh berlebihan - dia mungkin berpikir bahwa saya semacam orang aneh"
show mila oversized_shirt_posing at right
ms "Mungkin sesuatu seperti ini?"
ms "..."
ms "Nah ... __tag_0__ juga ... __tag_0__random ... __tag_0__also rasanya salah karena suatu alasan ..."
show mila casual_skeptic at right:
    xpos 0.9
    ypos 0.95
ms "__tag_0 __..."
ms "Dan itu agak ... __tag_0__Lain ..."
ms "Hmmm ..."
show mila robe_puzzled at right
ms "..."
show mila robe_from_behind_looking at right
ms "..."
ms "Itu saja! __Tag_0__ Saya pikir ..."
ms "Saya ingin tahu apakah terlalu banyak?"
ms "Berputar di depan cermin dan memperbaiki riasan saya, saya hampir melewatkan ketukan yang hati -hati dan tenang di pintu."
"__tag_0 __..."
scene bg door
play sound "door-open-close.mp3"
show bob waving at left:
    xzoom 0.9 yzoom 0.9
bob "... __tag_0__h-hello?"
show mila robe_smile_open_mouth at right
m "Hai lagi! __Tag_0__Anda mengetuk dengan tenang sehingga saya pikir itu mungkin draft, haha."
show bob shy at left:
    xzoom 0.9 yzoom 0.9
ms "Bob tersenyum malu -malu."
show mila robe_smile_grin at right
m "Ayo masuk."
ms "Tetesan air terlihat di kulitnya."
show mila robe_curious at right
ms "Apakah dia terburu -buru sehingga dia lupa mengeringkan dirinya sendiri?"
ms "Meskipun dia jelas baru saja datang dari kamar mandi, dia berpakaian sama seperti sebelumnya .."
show mila robe_blush_shy_looking_aside at right
ms "Tapi yang paling penting, saya tidak bisa tidak melihat tonjolan besar di celananya."
show mila robe_blush_smirk at right
ms "Apakah dia sangat menyukai jubah saya, ya?"
ms "Saya tersenyum pada pikiran saya dan memanggilnya ke dapur."
"__tag_0 __..."
scene bg kitchen
ms "..."
show mila robe_from_behind_not_looking at right
ms "Saat kami sedang memasak, saya perhatikan sebagai bob melempar melirik pantat saya"
ms "Saya ingin lebih menggodanya, tetapi saya tidak mengambil risiko dan hanya berpura -pura, bahwa saya tidak memperhatikan"
ms "Aku sudah pergi terlalu jauh dengan jubahnya ..."
ms "Dan itu benar -benar berbahaya untuk memprovokasi dia lebih banyak"
ms "Akan lebih baik jika saya berpura -pura naif dan ceroboh"
ms "Dan pertama -tama saya perlu berbicara dengan Paul tentang ..."
show mila robe_think at right
ms "Tentang apa?"
ms "Saya melirik Bob."
show bob idle at left:
    xzoom 0.9 yzoom 0.9
ms "Setelah diperiksa lebih dekat, dia mungkin sudah lebih dari lima puluh."
ms "Bangunannya adalah ... __tag_0__well dia tidak dibangun dengan baik untuk sedikitnya."
show mila robe_blush_shy_looking_aside at right
ms "Satu -satunya hal yang bisa dia bersaing dengan Paul adalah ukuran penisnya, dilihat dari tonjolan di celananya ..."
ms "Tapi saya tidak berpikir itu akan menjadi masalah bagi Paul, mengetahui kekusutannya ..."
hide mila robe_blush_shy_looking_aside
"__tag_0 __..."
ms "..."
ms "Ketika makanan sudah siap, Bob berdiri dan akan pergi."
show mila robe_puzzled at right
m "Kemana kamu pergi?"
bob "..."
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "I ... __tag_0__ Saya lupa membawa wadah makanan, __tag_0__so saya ingin pergi dan mendapatkannya ..."
show mila robe_puzzled_frown at right
m "Wadah? __Tag_0__Menapa Anda membutuhkannya?"
"Bob menatapku dalam kebingungan."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "Tetapi Anda mengatakan bahwa Anda ingin memperlakukan saya untuk merebus ..."
show mila robe_blush_smirk at right
ms "Saya tidak bisa menahannya, saya ingin menggodanya lebih banyak ... __tag_0____ reaksi itu adalah jenis yang membuat Anda ingin memainkannya sedikit ..."
m "Apakah saya?"
show bob sad2 at left:
    xzoom 0.9 yzoom 0.9
ms "Bob tersenyum lebih menyedihkan"
show mila robe_smile_grin at right
ms "Saya terkikik dan mengangguk ke arah kursi."
m "Duduk. __Tag_0__ memungkinkan saya menjagamu."
show bob idle at left:
    xzoom 0.9 yzoom 0.9
ms "Dia duduk di meja dengan malu."
show mila robe_from_behind_not_looking at right
ms "Saya menoleh ke wastafel dan akan mengambil piring biasa"
ms "Hmmm ..."
show mila robe_from_behind_looking at right
ms "Saya kira Bob membutuhkan porsi yang lebih besar"
ms "Dan ... __tag_0__ akan menyenangkan untuk menggodanya lebih banyak."
show mila robe_from_behind_not_looking_reaching_tiptoes at right
ms "Saya meregangkan punggung saya dan berdiri berjinjit, dalam upaya meraih mangkuk besar di atasnya"
ms "Saya segera meraih tepi, __tag_0__ tetapi merasakan tatapannya di pantat saya, saya lebih berdiri dengan berjinjit dan membungkuk untuk memberinya pandangan yang lebih baik."
show cg robe_close_up_butt at center:
    xzoom 0.75 yzoom 0.75 ypos 1 xpos 0.5
    linear 1.0 ypos 0.75
ms "Hehe."
ms "Ini sangat menyenangkan!"
ms "..."
show bob shy at left:
    xzoom 0.9 yzoom 0.9
ms "Melirik ke atas bahu saya, saya perhatikan bahwa Bob mengalami kesulitan menutupi kesalahannya."
ms "Hehehe."
ms "..."
ms "..."
ms "Saya mengatur meja dan duduk di seberangnya."
scene bg kitchen
"__tag_0 __..."
ms "Kami baru saja makan dalam keheningan untuk sementara waktu."
show mila robe_curious at right
m "Jadi ... __tag_0__ itu bagus?"
show bob smile at left:
    xzoom 0.9 yzoom 0.9
bob "Ya, Nyonya, semuanya sangat enak!"
show mila robe_smile_open_mouth at right
m "Panggil saja aku Mila, kalau tidak, Mrs. terdengar sedikit juga ..."
ms "Bob tersenyum meminta maaf dan mengangguk."
"__tag_0 __..."
"__tag_0 __..."
show mila robe_puzzled at right
ms "Keheningan ini membuatnya sulit untuk bernafas ..."
ms "Sepertinya dia ingin berbicara dengan saya tetapi terlalu takut untuk memulai percakapan"
ms "Saya mencoba memecahkan es lagi"
show mila robe_smile_open_mouth at right
m "Jadi ... __tag_0__ Apa yang Anda lakukan untuk mencari nafkah?"
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "..."
bob "Saya semacam pengembang, __tag_0__i tebakan ..."
show mila robe_puzzled at right
ms "Jawaban macam apa itu?"
show mila robe_smile_awkward_open_mouth at right
m "Maksudmu di dalamnya?"
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "Ya..."
show mila robe_puzzled at right
"__tag_0 __..."
ms "Apakah dia nyata?"
ms "Keterampilan komunikasinya benar -benar terbaik ..."
show mila robe_smile_awkward_open_mouth at right
m "Apakah Anda punya hobi? _ Tag_0__ Apa yang ingin Anda lakukan di waktu luang Anda?"
bob "..."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
ms "Bob menatapku sebentar"
bob "Saya ... __tag_0__i suka memancing, __tag_0__ Saya pikirkan."
ms "Itu sesuatu"
show mila robe_smile_open_mouth_excited at right
m "Ah, benarkah? __Tag_0__ Apa ikan terbesar yang pernah Anda tangkap?"
show bob sad2 at left:
    xzoom 0.9 yzoom 0.9
bob "..."
ms "Entah bagaimana dia menjadi lebih sedih"
show mila robe_puzzled at right
ms "Orang ini adalah ranjau darat berjalan"
bob "Sebenarnya saya tidak suka memancing, maaf"
show mila robe_puzzled at right
m "..."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "Saya berbohong ..."
ms "Uhuh"
ms "Sekarang saya tidak mengerti apa -apa ..."
show mila robe_smile_awkward_open_mouth at right
m "Erm ... __tag_0__ mengapa?"
bob "..."
show mila robe_puzzled at right
ms "Bob ragu -ragu __tag_0__ tapi saya diam -diam menunggu jawabannya"
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "Aku ... aku tidak tahu ..."
bob "Saya pikir hobi saya mungkin tampak aneh ..."
show mila robe_puzzled at right
m "..."
show mila robe_puzzled_frown at right
ms "Tolong jangan katakan bahwa Anda memiliki koleksi orang mati di dada atau sesuatu ..."
show mila robe_think at right
ms "Saya kira ... __tag_0__i perlu mendorongnya entah bagaimana ..."
show mila robe_smile_open_mouth at right
m "Anda tahu apa hobi saya?"
bob "..."
ms "Dia menatapku dengan antisipasi"
show mila robe_blush_shy_looking_aside at right
m "I __tag_0__collect Socks kesepian"
bob "..."
m "..."
bob "..."
show mila robe_smile_open_mouth at right
m "Anda tahu, yang tersisa pada pasangan setelah mencuci?"
m "Entah bagaimana, saya tidak bisa membuangnya, dan kadang -kadang, saya pergi melalui mereka berharap untuk menyatukan kembali pasangannya."
bob "..."
show mila robe_smile_grin at right
m "Hobi bodoh, ya?"
show bob smile at left:
    xzoom 0.9 yzoom 0.9
bob "..."
bob "Heh"
show mila robe_smile_open_mouth at right
m "Jadi jangan takut untuk memberi tahu saya tentang hobi Anda"
m "Saya ragu bahwa Anda lebih bodoh dari saya ..."
bob "..."
show mila robe_puzzled at right
m "..."
show bob shy at left:
    xzoom 0.9 yzoom 0.9
bob "..."
bob "Baik ... __tag_0__ Saya suka anime dan game ..."
"__tag_0 __..."
show mila robe_smile_awkward_open_mouth at right
m "..."
m "Maksudmu ... __tag_0__something Extreme?"
bob "Tidak, tidak!"
bob "Hanya yang biasa ..."
show mila robe_smile_awkward_angry at right
ms "..."
ms "Itu saja?"
ms "Dimana lucunya?"
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "Itu hanya ..."
bob "Saya selalu melakukan segalanya pada saat yang salah dalam hidup ..."
m "..."
show mila robe_curious at right
bob "Seperti ... Saya berusia 52 tahun, dan saya suka hal -hal yang dibuat untuk para remaja."
bob "Saya belum pernah menikah atau bahkan dalam suatu hubungan karena saya selalu berpikir bahwa itu adalah hal untuk masa depan."
show mila robe_sad at right
bob "Saya selalu terlambat ... rekan -rekan saya mengolok -olok saya ..."
bob "Saya melewatkan promosi saya, pemakaman ibu saya, semuanya ..."
show bob sad2 at left:
    xzoom 0.9 yzoom 0.9
show mila robe_sad_tears at right
bob "Saya merindukan hidup saya ..."
bob "Dan sekarang ... sekarang saya hanya seorang wimp tua yang menyedihkan yang mengeluh tentang masalahnya ..."
ms "..."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "... __tag_0__sorry ..."
bob "Saya merusak suasana hati ... __tag_0__ saya selalu melakukan ..."
"__tag_0 __..."
ms "Itu ... __tag_0__tough untuk mendengar ..."
ms "Bob menatapku dan tersenyum kosong dan sedih"
bob "Jadi ... yah ..."
show bob smile at left:
    xzoom 0.9 yzoom 0.9
bob "Terima kasih untuk malAm Ini."
ms "Senyumannya tampak sama ... __tag_0__T tetapi suaranya tampak aneh bagiku."
ms "Tampaknya jauh ... __tag_0__ BAIK ... __tag_0__dying ..."
show mila robe_sad_tears_open_mouth at right
m "Bob?"
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "Saya mungkin harus pergi. Jangan khawatir, aku tidak akan mengganggumu lagi ..."
ms "Dia berdiri."
show mila robe_sad at right
ms "Saya merasakan benjolan di tenggorokan saya."
ms "Seolah -olah ... jika saya tidak melakukan sesuatu sekarang, saya akan menyesalinya selama sisa hidup saya."
ms "Karena itu, ketika dia lewat, aku meraih tangannya tanpa berpikir"
show mila robe_think at right
m "Tunggu."
show bob sad2 at left:
    xzoom 0.9 yzoom 0.9
ms "Bob menatapku kosong."
ms "Ada begitu banyak kesedihan di matanya ... __tag_0__ itu seolah -olah tidak ada orang yang tersisa di dalam. __Tag_0__hust shell kosong."
show mila robe_proud at right
m "Apakah Anda tidak ingin mengejar ketinggalan?"
show bob surprised at left:
    xzoom 0.9 yzoom 0.9
bob "Mengejar? Apa maksudmu?"
show mila robe_grin_thumbs_up at right
m "Hah. Serahkan itu padaku!"
"__tag_0 __..."
show mila robe_puzzled at right
ms "Saya tidak tahu !!!"
show bob idle at left:
    xzoom 0.9 yzoom 0.9
ms "Bob baru saja memiringkan kepalanya ke samping."
show mila robe_think at right
ms "I need to figure out how exactly \"he\" can \"catch up\"..."
ms "Meskipun, jika Anda memikirkannya, tidak seperti saya dapat membantu dengan banyak ..."
ms "Pertama-tama, saya perlu memperbaiki harga dirinya ..."
bob "..."
show mila robe_puzzled at right
ms "Dan mungkin citra publiknya juga ..."
ms "Uang bisa membantu ..."
show mila robe_puzzled_frown at right
ms "Kasihan aku tidak punya itu ..."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "? ..."
show mila robe_sad at right
ms "Dan saya tidak tahu bagaimana seseorang bisa menjadi kaya dengan cepat"
ms "__tag_0 __..."
ms "Sejujurnya saya tidak tahu bagaimana seseorang bisa menjadi kaya sama sekali"
ms "Dan bahkan jika saya bisa - itu tidak akan menyelesaikan masalah ..."
show mila robe_think at right
ms "Hmmm__tag_0 __..."
ms "Saya melihat sekilas refleksi saya sendiri di cermin"
show mila robe_smile_open_mouth_excited at right
m "Oh!"
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "?"
show mila robe_proud at right
m "Anda, sayangku, akan menemukan pacar!"
bob "..."
show bob sad2 at left:
    xzoom 0.9 yzoom 0.9
ms "Bob tertawa sedih, jika tidak Evilly."
bob "Hah! Apakah Anda pikir saya belum mencoba?"
show bob sad at left:
    xzoom 0.9 yzoom 0.9
bob "Semua wanita tertarik pada wajah lucu! Atau uang. Saya tidak memiliki yang satu maupun yang lain!"
show mila robe_smile_awkward_angry at right
m "..."
bob "..."
m "..."
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "Baiklah, oke, tidak setiap wanita ... __tag_0__but hampir semua orang ... __tag_0__i maksudkan tidak ada pelanggaran ..."
show mila robe_puzzled at right
ms "Saya menghentikannya dengan gerakan."
m "Anda mungkin benar sampai batas tertentu. Tapi kami, orang -orang, semua tertarik pada apa yang sudah diminati."
bob "..."

show mila robe_smile_open_mouth at right
m "Jadi, __tag_0__ apa artinya?"
m "..."
bob "..."
m "..."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
ms "Bob menghela nafas"
bob "Apa artinya?"
ms "Hebat, setidaknya beberapa reaksi."

show mila robe_proud at right
m "Itu berarti hal utama adalah menunjukkan bahwa Anda memiliki nilai. __Tag_0__ bahwa Anda sudah ... __tag_0__ dalam permintaan dan __tag_0__tomeone yang layak untuk diketahui."
ms "Bob menyipitkan matanya."

show mila robe_blush_smirk at right
m "Lihat."
ms "Saya mengambil sikunya dan mengambil foto."
play sound "shot.mp3"
show cg selfie_with_bob at center:
    xzoom 0.8 yzoom 0.8 ypos 1
    linear 1.0 ypos 0.75

show mila robe_proud at right
m "Melihat?"
show bob shy at left:
    xzoom 0.9 yzoom 0.9
bob "..."

show mila robe_blush_smirk at right
m "Kami terlihat seperti pasangan."
bob "..."

show mila robe_smile_open_mouth at right
m "Saya tidak memiliki nomor Anda, izinkan saya mengirimkan foto ini ..."
bob "Ah? Ya ok…"
ms "Bob sepertinya tidak percaya apa yang terjadi."
ms "..."
hide cg selfie_with_bob
nvl clear
md "__Tag_0__"
show bob idle at left:
    xzoom 0.9 yzoom 0.9
ms "Bob diam -diam menatap layar teleponnya"
show mila robe_smile_grin at right
ms "Aku meremas tangannya dan menunggu sampai akhirnya dia memperhatikanku."
m "Anda pria hebat Bob."
m "Jangan terlalu khawatir tentang orang bodoh."
m "Banyak cewek menyukai pria besar"
m "Jangan menyatukan semua orang ke keranjang yang sama."
bob "..."
show bob shy at left:
    xzoom 0.9 yzoom 0.9
bob "Apakah kamu?"
show mila robe_puzzled at right
m "..."
m "M?"
ms "Pertanyaannya mengejutkan saya."
bob "Do __tag_0__you__tag_1__ __tag_2__ seperti orang besar?"
show mila robe_blush_smirk at right
ms "..."
m "Ya, Bob. __Tag_0__ Saya suka orang -orang besar."
ms "Untuk beberapa alasan kedengarannya erotis. __Tag_0__my Tummy terasa hangat dan aku hampir tidak bisa menahan keinginan untuk meremas kakiku."
show bob smile at left:
    xzoom 0.9 yzoom 0.9
bob "..."
show mila robe_smile_open_mouth at right
m "Posting foto ini di jejaring sosial. __Tag_0__i akan membuat halaman baru dan mengatakan bahwa saya baru -baru ini bertemu dengan pria paling luar biasa dalam hidup saya."
show bob sad at left:
    xzoom 0.9 yzoom 0.9
ms "Bob mengerutkan kening."
bob "Mengapa Anda membutuhkan halaman lain? .."
m "..."
show mila robe_puzzled at right
ms "..."
m "Yang saat ini berisi foto dan foto pernikahan saya dengan Paul. Akan aneh jika seseorang melihatnya."
bob "Ah ... yah, ya, kedengarannya masuk akal."
ms "..."
ms "Bob memposting foto di halamannya."
ms "..."
show mila robe_think at right
ms "Saya merasa itu tidak cukup ..."
show mila robe_smile_open_mouth_excited at right
ms "Oh! __Tag_0__i muncul dengan ide lain."
show mila robe_blush_smirk at right
m "Datanglah besok pagi. __Tag_0__ Saya akan memberi Anda sesuatu."
show bob surprised at left:
    xzoom 0.9 yzoom 0.9
bob "..."
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "Ok ... __tag_0__ saya akan"
play sound "door-open-close.mp3"
show bob surprised at left:
    xzoom 0.9 yzoom 0.9
    linear 1.0 xpos 0.75
show mila robe_blush_smirk at right:
    linear 1.0 xpos 0.9
p "Saya di rumah!"
show mila robe_smile_open_mouth at right:
    xpos 0.9
m "Oh, ini Paul. __Tag_0__ memungkinkan saya memperkenalkan Anda."
show paul suit_shock at left
ms "Paul membeku ketika dia melihat pria yang begitu besar dan perlahan -lahan mengalihkan pandangannya kepada saya."
show paul suit_frown at left
ms "Melihat pakaian saya dan penampilan yang malu, dia mengerutkan kening."
p "Apakah ini ... __tag_0__ itu ini yang saya pikirkan?"
ms "..."
show mila robe_blush_smirk at right:
    xpos 0.9
m "No. __tag_0__at paling tidak."
show bob idle at left:
    xzoom 0.9 yzoom 0.9 xpos 0.75
ms "Bob memandang dariku ke Paul dengan pertanyaan sunyi di matanya."
show mila robe_smile_open_mouth at right:
    xpos 0.9
m "Ini Bob."
ms "Saya secara singkat memberi tahu Paul tentang bagaimana Bob membantu saya membawa tas saya dan menyiapkan makan malam"
scene bg door
ms "Bob membuka mulutnya untuk menambahkan sesuatu, tetapi saya menariknya ke arah pintu keluar."
show mila robe_smile_awkward_open_mouth at right
m "Oke, Bob, __tag_0__ terima kasih lagi atas bantuan Anda, __tag_0__ Senang bertemu dengan Anda."
ms "Dan sudah ada di pintu yang saya tambahkan."
show mila robe_blush_smirk at right
m "Datanglah besok pagi sebelum bekerja. __Tag_0__ tidak lupa!"
show bob sad at left:
    xzoom 0.9 yzoom 0.9
ms "Dia mengangguk, masih bingung."
bob "Tentu ... __tag_0__good Night ..."
hide bob_sad
play sound "door-open-close.mp3"
ms "Saya bergegas ke kamar tidur, untuk memberi Paul penjelasan yang tepat"
ms "Saya tidak ingin dia berpikir saya melakukan apa pun tanpa persetujuannya."


label hscene_netorase_hj_with_paul:
scene bg apartments
ms "Paul menungguku di ruang tamu dengan tangan bersilang"
ms "Aku berlutut di depannya dan melepas celananya."
show cg mila_paul_hj_smile with dissolve
ms "Dick Hard Rock -nya muncul di wajahku"
ms "Saya mengambilnya di tangan saya dan memandang Paul"
m "Sebelum Anda mengajukan pertanyaan - tidak ada yang terjadi"
p "..."
m "Aku sedikit memalsukan payudaraku, dan biarkan dia melihat pantatku sedikit"
p "..."
m "Itu ... __tag_0__ exciting"
p "..."
m "..."
m "Apakah ini yang Anda inginkan?"
p "..."
show cg mila_paul_hj_worried with dissolve
p "Saya tidak yakin ..."
p "..."
p "Sungguh menyakitkan membayangkan Anda ... dengan orang lain ..."
m "..."
m "Apakah Anda ingin berhenti?"
p "..."
p "..."
p "__tag_0__no ..."
m "..."
show cg mila_paul_hj_idle with dissolve
p "Mmm ..."
p "Apa yang Anda rencanakan selanjutnya?"
m "..."
m "Saya ingin meningkatkan harga dirinya terlebih dahulu ..."
m "Jadi saya akan berpura -pura menjadi pacarnya atau semacamnya ..."
ms "Paul membuat meringis"
m "Anda tidak suka idenya?"
p "..."
p "Hanya saja ... __tag_0__no ... __tag_0__i'm hanya cemburu, saya pikir ..."
m "..."
m "Apakah Anda ingin meletakkan beberapa ... __tag_0__RRICTIONS pada tindakan saya?"
p "..."
p "Jangan jatuh cinta padanya ..."
show cg mila_paul_hj_smile with dissolve
m "Saya tidak akan. __Tag_0__i mencintaimu."
p "..."
p "Aku juga mencintaimu, sayang ..."
m "Sayang?"
p "Ya?"
m "Apa fantasi Anda tentang ... semua ini?"
p "Aku ... aku takut menggali lebih dalam ke dalamnya ..."
p "Takut mengakui hal itu ... bahwa saya suka ketika orang lain ... dengan Anda ..."
ms "Dia tampak sangat rentan ... Saya ingin mendukungnya entah bagaimana"
m "Aku mencintaimu"
p "Aku tahu..."
p "Hanya saja ... itu salah ... bukan yang saya inginkan, tapi saya lakukan ..."
p "Setiap kali saya memiliki satu pemikiran tentang hal itu, saya membenci diri saya sendiri untuk itu ..."
p "Tapi ... sangat menyenangkan ..."
m "Bisakah Anda ... berbagi salah satu pemikiran ini dengan saya?"
p "..."
p "Tidak ... itu memalukan"
show cg mila_paul_hj_idle with dissolve
m "Please Please?"
p "Sayang, tidak"
m "Cantik sekali?"
p "..."
m "Saya akan berutang satu keinginan jika Anda melakukannya"
p "..."
p "__Tag_0__fine ..."
m "Hehe"
p "..."
m "Jadi?"
m "Saya semakin bersemangat"
p "Ingat terakhir kali, ketika kami berada di restoran bersama kolega saya?"
m "..."
m "__tag_0 __..."
show cg mila_paul_hj_smile with dissolve
m "Oh! Saya bersedia! Kami makan steak. Yang buruk."
p "Ya. Juga, Anda duduk di seberang saya, dan salah satu kolega saya duduk di sebelah Anda."
m "Benar!"
p "..."
p "I ... __tag_0__imagined ... __tag_0__multiple Times ..."
p "Bahwa Anda memberinya handjob saat itu di bawah meja ..."
m "__tag_0 __..."
show cg mila_paul_hj_worried with dissolve
m "Bagaimana ... __tag_0__ bagaimana Anda tahu?"
p "...Apa?"
m "Saya pikir kami bijaksana ..."
m "Saya menutupi tangan saya dengan serbet"
m "Kemudian, saya membuka ritsleting celananya dan mengambil penisnya di tangan saya"
m "Apakah Anda ingat saat dia terkejut?"
p "..."
m "Ya. Dan kemudian saya mulai menggerakkan tangan saya"
show cg mila_paul_hj_smile with dissolve
m "Seperti ini"
m "Tetapi saya mencoba melakukannya dengan lambat untuk tidak tertangkap"
m "Kemudian..."
show cg mila_paul_hj_open with dissolve
p "Urgh ..."
p "Sungguh!"
m "Ahaha!"
m "Mmm ..."
m "Beri aku cum manis itu, sayang ..."
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
scene mila_paul_hj_cum_1 with flash
p "Ohhh yess ..."
scene mila_paul_hj_cum_2 with dissolve
m "..."
scene mila_paul_hj_cum_3 with flash
p "Mmm ..."
scene mila_paul_hj_cum_4 with dissolve
m "Hehehe ..."
scene mila_paul_hj_cum_5 with dissolve
ms "Paul menatapku dengan senyum puas di wajahnya"
ms "Saya tersenyum balik"
m "..."
ms "Saya dengan lembut memerah tetes terakhir dari air mani dan mengisapnya"
p "Mmm ..."
p "Anda adalah yang terbaik ..."
m "hehe"
m "__tag_0 __..."
scene bg apartments with dissolve
ms "Saya berdiri dan akan pergi ke kamar mandi"
p "Tunggu..."
m "?"
show mila robe_cum_idle at center
p "Apakah itu nyata? __Tag_0__i berarti ... __tag_0__ apakah Anda ..."
m "__tag_0 __..."
show mila robe_cum_angry at center
m "Tentu saja tidak, konyol!"
m "Saya tidak akan melakukan sesuatu yang bisa menyakiti Anda!"
m "Apakah Anda pikir saya mampu mengkhianati?"
p "..."
p "TIDAK..."
p "Anda juga terlihat panas saat Anda marah dan tertutup cum"
show mila robe_cum_confused at center
m "__tag_0 __..."
show mila robe_cum_smirk at center
m "..."
m "Anda pikir?"
p "Ya..."
m "Bayangkan ..."
m "Itu bukan sperma Anda ..."
show mila robe_cum_wink at center with dissolve
pause 0.5
show mila robe_cum_smirk at center
p "..."
p "Sial ..."
m "Hehehe"
m "Dan juga ..."
show mila robe_cum_wink at center
ms "Aku bersandar di dekat telinganya dan berbisik"
m "__Tag_0__Jika Anda ingin saya menyentak orang lain ..."
m "__Tag_0__just bertanya"
p "!!!"
m "Aku berhutang padamu, ingat?"
p "..."
p "Anda adalah setan kecil ..."
show mila robe_cum_smirk at center
m "..."
m "Terakhir kali saya memeriksa, saya adalah malaikat Anda ..."
p "..."
p "Aku mencintaimu"
m "..."
p "Aku pun mencintaimu"
if _in_replay:
    return
"__tag_0 __..."


label v122:
scene bg kitchen
"__tag_0 __..."
"..."
show mila robe_think at center
ms "Hari berikutnya saya bangun pagi dan memasak makan siang."
ms "Saya berusaha lebih keras dari yang saya lakukan untuk Paul."
ms "Pada akhirnya, makanan saya tidak lebih dari rutinitas untuknya ..."
ms "Tapi untuk Bob ... __tag_0__ itu sesuatu yang jauh lebih ..."
ms "Itulah mengapa saya berusaha lebih keras di dalamnya"
show mila robe_blush_shy_looking_aside at center
ms "Saya terus mengingat sensasi tatapannya"
ms "Itu menyerupai perasaan yang terlupakan untukku ..."
ms "Sesuatu yang saya pikir tidak akan saya rasakan lagi ..."
ms "Dan itulah mengapa ... __tag_0__ saya ingin lebih ..."
show mila robe_blush_smirk at center
ms "Sesuatu yang lebih mendebarkan ... __tag_0__Something lebih berani ..."
ms "Sesuatu, itu akan membuat Bob lebih percaya diri ..."
ms "Sesuatu, itu membuatku merasa berbeda ..."
ms "Something, that will shut up his \"compassionate\"kolega ..."
ms "..."
ms "..."
show mila robe_puzzled at center
ms "Hmmm ..."
ms "..."
show mila robe_smile_open_mouth_excited at center
ms "Oh!"
show mila robe_think at center
ms "Saya memakai lipstik tebal dan mencium serbet."
ms "..."
show mila robe_blush_smirk at center
ms "Heh."
ms "Terlihat erotis."
ms "Saya meletakkannya di atas."
show mila robe_think at center
ms "..."
ms "Saya ingin menambahkan sesuatu yang lain ..."
ms "..."
show mila robe_smile_grin at center
ms "Aku menyeringai pada pikiranku, __tag_0__ menarik celana dalamku dan meletakkannya di bagian bawah."
ms "Ada setitik jus vagina saya di tengah."
ms "Hehe."
ms "Persis apa yang dibutuhkan."
ms "Dia harus menemukannya setelah makan siang."
ms "..."
show mila robe_smile_awkward_open_mouth at center
ms "Dibawa oleh pikiran saya, saya lagi hampir melewatkan ketukan yang tenang di pintu."
scene bg door
show mila robe_smile_awkward_open_mouth at center:
    linear 1.0 xpos 0.9
ms "Saya bergegas ke pintu dan membukanya - saya takut Bob akan dengan cepat berubah pikiran dan pergi."
ms "Melihat wajahnya yang bingung, aku tidak bisa menahan senyum."
show mila robe_smile_open_mouth at right
m "Halo Bob."
show bob waving at left:
    xzoom 0.9 yzoom 0.9
bob "H-hello ..."
m "..."
bob "..."
show mila robe_smile_awkward_angry at right
m "..."
ms "Saya perlu melakukan sesuatu dengan suasana canggung dan jeda suatu hari nanti ..."
show mila robe_smile_open_mouth_excited at right
m "Ini dia."
ms "Saya menyerahkan sekantong wadah."
show bob surprised at left:
    xzoom 0.9 yzoom 0.9
bob "..."
ms "Dia menatapku dalam kebingungan."
bob "Apa ini?"
show mila robe_proud at right
m "Ini makan siangmu."
bob "..."
m "Makan di perusahaan kolega."
show mila robe_smile_grin at right
m "Jadikan mereka iri padamu!"
bob "..."
show mila robe_puzzled_frown at right
m "..."
bob "..."
ms "Bob diam sebentar dan kemudian berteriak:"
show bob waving at left:
    xzoom 0.9 yzoom 0.9
bob "Tidak tidak tidak! Saya tidak bisa menerima ini!"
show mila robe_shhhh_finger at right
m "Syi!"
ms "Saya meletakkan jari saya ke bibir saya."
show mila robe_smile_awkward_open_mouth at right
m "Diam!"
m "Atau Anda akan membangunkan tetangga."
bob "..."
show mila robe_smile_open_mouth at right
m "Anda ingin menggoda para idiot ini, bukan?"
show bob idle at left:
    xzoom 0.9 yzoom 0.9
bob "..."
bob "Ya…"
m "Ini dia. __Tag_0__okay, saya perlu menyiapkan makan siang untuk Paul juga. __Tag_0__so semoga harimu menyenangkan, dan semoga sukses untukmu."
show bob smile at left:
    xzoom 0.9 yzoom 0.9
bob "Terima kasih!"
ms "Senyumnya sangat tulus dan baik hati sehingga saya tidak tahan dan berbalik."
show mila robe_sad at right
ms "Saya merasa seperti pengganggu ..."
ms "Seperti saya orang jahat yang berbohong kepada anak yang murni ..."
ms "Saya tidak tahan dan hanya menutup pintu."
play sound "door-open-close.mp3"
show mila robe_sad_tears at right
ms "Omong kosong…"
ms "Ini tidak adil…"
ms "Lebih baik aku tidak mengacaukannya ..."


"__tag_0 __..."
scene bg apartments
ms "Saya melakukan pekerjaan harian dan berbaring di sofa untuk beristirahat"
bob_message "Halo, Mila."
bob_message "Saya memiliki permintaan yang aneh ..."
bob_message "Bisakah saya menelepon?"
ms "Saya dengan cepat memeriksa refleksi saya di cermin, membuat beberapa penyesuaian dan memulai panggilan video."
show cg videocall_smile at center:
    xzoom 0.8 yzoom 0.8
ms "Ketika dia menjawab telepon, saya tersenyum."
m "Halo, beruangku! __Tag_0__ bagaimana makan siangmu hari ini?"
show cg videocall_wink
m "Saya tidak percaya diri dengan keterampilan memasak saya, tetapi saya cukup yakin bahwa saya akan mendapatkan baik dengan beberapa latihan"
show cg videocall_smile
bob "Mata Bob melesat dari sisi ke sisi."
bob "W-we ... __tag_0__erm ... __tag_0__ setiap orang bisa mendengarmu ..."
show cg videocall_surprise
ms "Saya berpura -pura kejutan."
show cg videocall_closed_eyes_smile
m "Oh maaf! Apakah Anda di kantor? __Tag_0__jap ada seseorang di dekatnya - maafkan saya!"
bob "..."
show cg videocall_smile
m "..."
bob "..."
show cg videocall_smile_awkward
m "Halo? Koneksi hilang?"
show cg videocall_smile
bob "N-no ... ini ... saya hanya tidak tahu bagaimana menjawab ..."
ms "Seorang pria mengangkat telepon dan menatap kamera."
ms "Di sebelahnya ada beberapa orang lain berjas."
show cg videocall_smile_awkward
ms "Saya tersenyum sopan dan melambai pada mereka."
ms "..."
ms "Mereka menatapku selama beberapa detik."
ms "Ketika saya mulai merasa tidak nyaman, salah satu dari mereka bertanya:"
bob_unknown "Apakah Anda benar -benar berkencan dengan Bob?"
show cg videocall_shy_giggle
ms "Saya memalsukan rasa malu."
m "H-dia mengatakan itu?"
ms "Saya menekan tangan saya ke pipi saya dan terkikik."
m "W-We tidak mengatakan sumpah, tetapi jika Bob berkata begitu ... hehehe ..."
bob_unknown "..."
bob "..."
hide cg videocall_shy_giggle
ms "Keheningan memerintah lagi untuk beberapa waktu, yang kemudian meledak dengan teriakan mereka"
ms "Saya mendengarkan mereka dan mencoba yang terbaik untuk tidak berteriak pada mereka"
show mila robe_smile_awkward_angry at right
bob_unknown "Oh ayolah!"
bob_unknown "Kenapa lucu sekali dengan shitfuck ini?!"
bob_unknown "Tidak bisakah dia menemukan orang lebih baik?"
bob_unknown "Lelucon!"
bob_unknown "__Tag_0____ Bob jelek Anda punya pacar dan saya tidak? Hidup itu tidak adil ..."
bob_unknown "Saya tidak percaya ... Saya tidak percaya ..."
ms "Untuk beberapa alasan, reaksi mereka membuat saya jengkel. Lebih dari yang saya kira."
hide mila
show cg videocall_cold_smile at center:
    xzoom 0.8 yzoom 0.8
m "Saya minta maaf? Mengapa Anda berbicara tentang bob saya seperti itu? Itu kasar!"
ms "Suara -suara itu secara bertahap mereda."
bob_unknown "Pria yang memegang telepon dijawab."
bob_unknown "Kami terlalu mencintai Bob, Anda tahu?"
ms "Seseorang tertawa di belakangnya."
ms "Saya mengertakkan gigi saya tetapi tetap diam."
bob_unknown "Kami hanya tidak ingin ada yang memanfaatkan ... "sisi baik""
show cg videocall_smile_awkward
ms "Saya tersenyum."
ms "Ya, tentu. __Tag_0__tell me a story"
m "Ah, benarkah? __Tag_0__ terima kasih! __Tag_0__ Anda semuanya sangat baik!"
bob "..."
bob_unknown "Maukah Anda bergabung dengan kumpul-kumpul malam kita malam ini?"
show cg videocall_happy_smile_open_mouth
ms "Saya berpura -pura sukacita."
m "Oh, dengan senang hati! Sekarang bisakah Anda meneruskan telepon ke Bob?"
hide mila robe_smile_awkward_angry
"__tag_0 __..."
hide cg videocall_happy_smile_open_mouth
ms "Kami mengobrol lagi, tetapi dia sangat malu sehingga dia berbicara omong kosong."
ms "Jadi saya mengakhiri percakapan tanpa memiliki kesempatan untuk menggodanya dengan benar."
ms "Percakapan meninggalkan aftertaste yang tidak menyenangkan."
ms "Saya merasa marah dan jengkel karena saya tidak merasa dalam waktu yang lama."
ms "Mereka tidak percaya bahwa seseorang dapat berkencan dengan Bob murni karena keinginan? Saya akan menunjukkan kepada Anda, brengsek."
bob_message "Anda tidak perlu melakukan ini ..."
ms "Bob menulis sesuatu yang lain, tetapi tidak punya waktu untuk mengirim pesan. Saya menjawab lebih cepat."
ma "Saya ingin melakukan ini."
ma "Jadi saya akan datang."
ms "Saya ingin menghiburnya, jadi saya memilih sudut yang lebih baik dan mengambil selfie."
play sound "shot.mp3"
ms "..."
show bob_selfie1x at right:
    xzoom 0.75 yzoom 0.75
    ypos 0.9 xpos 0.95
md "__Tag_0__"
hide bob_selfie1x
"..."
ms "Saya menunggu beberapa menit, tetapi Bob tidak menjawab"
show mila robe_curious
ms "Saya membuka lemari dan mulai memilih pakaian."
m "Hmmm ..."
bob_message "Kamu sangat cantik, mila ..."
show mila robe_proud
ms "..."
ms "Oh dia sangat manis ..."
show mila robe_smile_awkward_angry
ms "..."
ms "It's just made me even more angry at his so-called \"Friends\""
show mila robe_blush_smirk
ms "Baiklah"
ms "Operation \"make them jealous\"telah dimulai secara resmi"
ms "Tujuan saya adalah terlihat seksi dan sederhana sekaligus"
show mila robe_curious
ms "..."
ms "Hmmm"
ms "Bagaimana dengan ini?"
show mila dress_front:
    xzoom 1.1 yzoom 1.1
ms "..."
ms "Baik itu benar -benar seksi"
ms "Tetapi..."
show mila dress_back
ms "Saya terlihat seperti pelacur ..."
ms "Saya pikir saya perlu mencoba sesuatu yang lain"
ms "..."
show mila summerdress_front:
    xzoom 1 yzoom 1
ms "..."
ms "Yang ini terlihat bagus"
ms "Saya suka warna dan gambar secara keseluruhan"
show mila summerdress_back
ms "..."
ms "Tapi ... __tag_0__ dengan bob aku akan terlihat seperti orang gila dengan masalah ayah ..."
ms "..."
ms "..."
show mila summerdress_front
ms "Apakah saya orang gila dengan masalah ayah?"
"__tag_0 __..."
ms "Tidak ... __tag_0__ saya pikir ... __tag_0__ Lagi pula, mari kita coba yang lain ..."
ms "..."
show mila jeans_and_blouse_front:
    ypos 0.95
ms "..."
ms "..."
show mila jeans_and_blouse_back
ms "..."
ms "Jadi?"
ms "..."
ms "Saya kira tidak apa -apa ..."
ms "Saya tidak punya waktu untuk memilih sesuatu yang berbeda"
ms "Ayo pergi dengan ini"
"__tag_0 __..."


scene bg taxi
play sound "car_door.mp3"
"..."
ms "Saya naik taksi dan mengirim sms Bob bahwa saya akan segera ke sana."
bob_message "Kamu benar -benar ingin datang?"
bob_message "Saya tidak yakin itu ide yang bagus ..."
ma "Saya sudah datang, Bob"
"..."
ms "Bob tidak menjawab"
"__tag_0 __..."
play sound "car_door.mp3"
"..."
show bg mila_and_car:
    ypos 1.0
    linear 4.0 ypos 2.65
ms "Keluar dari taksi, saya hampir tersandung."
ms "Saya sudah lama tidak memakai sepatu hak ..."
ms "Saya mengambil waktu sejenak untuk mengumpulkan pikiran saya, dan pergi ke kafe."
play sound "shop_door.mp3"
"..."
scene bg cafe
ms "Ada banyak orang di dalam"
ms "Suara keras lusinan orang yang berbicara, berbisik, berteriak dan tertawa - semuanya pada saat yang sama, memenuhi telingaku"
show mila jeans_and_blouse_front
ms "Saya menemukan Bob di sudut dengan sebotol bir di tangannya, dia dengan gugup menatap saya"
ms "Saya tidak yakin seperti apa wajahnya - dia tampak seperti khawatir bahkan lebih dari biasanya dan lega pada saat yang sama"
show mila jeans_and_blouse_waving
ms "Aku tersenyum, melambai padanya dan berteriak"
m "Hai, ayah saya beruang!"
ms "Untuk sesaat, semua percakapan terdiam."
ms "Puluhan mata menatapku"
show mila jeans_and_blouse_run_smile
ms "Saya mencoba mengabaikan mereka dan berlari ke arah Bob."
bob_unknown "..."
bob_unknown "__Tag_0 __ (bisikan) Saya tidak percaya ini nyata ..."
hide mila
show milaandbob lap_surprise at right:
    xpos 0.9
ms "Aku mendekati Bob, memeluknya dan duduk di pangkuannya."
ms "Beberapa kolega masih menatap kami dengan tak percaya, jadi saya menekan pipi saya ke Bob dan menciumnya."
"..."
bob_unknown "__Tag_0 __ (berbisik) bercinta dunia ini ..."
show milaandbob lap_blush
ms "..."
ms "Hehe."
ms "Tidak, bercinta __tag_0__you__tag_1__, idiot."
ms "Saya merasakan sesuatu yang sulit ditekan di paha saya."
ms "..."
show milaandbob lap_blush2
ms "Sesuatu? __Tag_0__T IT'S Bob's Dick, Mila ..."
ms "Saya menekan rasa malu saya"
ms "Bagaimanapun, ini adalah reaksi yang sepenuhnya alami."
ms "..."
show milaandbob lap_blush2_looking_aside
ms "Belum lagi saya menikmati kegembiraannya."
show milaandbob lap_smirk_lookin_at_bob
ms "Saya memandang Bob dan tersenyum licik, memberi tahu dia bahwa saya telah memperhatikan."
show milaandbob lap_smirk_lookin_at_bob_looking_away
ms "Dia berbalik malu."
ms "Hehehe."
ms "..."
show milaandbob lap_blush2_looking_aside
ms "Rekan -rekan Bob bersikeras agar saya minum bersama mereka, tetapi saya berhasil menolak, mengutip toleransi alkohol yang buruk."
bob_unknown "Jika Anda tidak akan minum bersama kami, setidaknya beri tahu kami bagaimana Anda bertemu Bob?"
ms "Saya mencoba menjawab, tetapi pria lain berteriak:"
bob_unknown "Better tell us where can I \"meet\"denganmu juga?"
ms "Kerumunan tertawa terbahak -bahak"
show milaandbob lap_smile
ms "I answered with a polite smile, like I didn't get \"the joke\"."
ms "Pemabuk selalu membuat lelucon buruk"
ms "Tetap saja, duduk di pangkuan Bob adalah pilihan yang tepat."
ms "Dengan cara ini saya segera menjelaskan siapa pria saya."
ms "..."
show milaandbob lap_blush2_looking_aside
ms "Pikiran itu membuatku menggigil."
ms "Laki -laki saya adalah paul, __tag_0__ tidak ada bob ...__ tag_0__ namun saya duduk di pangkuannya dan menggosok pantat saya di penisnya yang ereksi ..."
ms "Aku kembali merasa ketika kemaluannya menempel di pantatku, tetapi kali ini kesiapan pertempurannya menyebabkan aku bukan kelembutan, tetapi keinginan."
ms "Saya merasa seperti pelacur."
ms "..."
show milaandbob lap_blush_closed_eyes
ms "Mmm…"
ms "Saya menekan erangan saya, tetapi gagal menekan keinginan saya untuk menggosok celah saya terhadap ayam Bob"
ms "Bob dengan lembut meletakkan tangannya di pinggangku dan berbisik:"
show milaandbob lap_blush_hand_on_waist_looking_at_eachother
bob "Saya harus pergi ... ke kamar kecil."
ms "Sentuhan lembut dan napas panasnya menyebabkan kawanan merinding baru yang melompat di sepanjang tulang belakang saya."
hide milaandbob lap_blush_hand_on_waist_looking_at_eachother
ms "Begitu Bob pergi, salah satu rekan pelecehnya bergerak lebih dekat dan meletakkan tangannya di lutut saya."
show cg hand_on_knee at center:
    xzoom 0.6 yzoom 0.6
    ypos 0.8
"..."
bob_unknown "Katakan dengan jujur, berapa dia membayar Anda?"
ms "Saya terpana dengan pertanyaan ini."
bob_unknown "Saya akan membayar tiga kali lebih banyak daripada dia membayar Anda selama sebulan hanya untuk satu malam."
bob_unknown "Apakah Anda melakukan anal?"
hide cg hand_on_knee
ms "Untuk sesaat saya tidak percaya apa yang baru saja saya dengar"
ms "Tapi kemudian ..."
show mila jeans_and_blouse_angry_open at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
play sound "slap.mp3"
"TAMPARAN!"
ms "Aku melemparkan tangannya dan menampar wajahnya."
m "Menurutmu menurutmu apa?!"
show mila jeans_and_blouse_angry_close
bob_unknown "..."
m "..."
ms "Seluruh kafe menjadi diam."
bob_unknown "..."
ms "Saya berdiri dan melihat semua orang di sekitar saya dengan penghinaan."
show mila jeans_and_blouse_angry_open
m "Saya benar -benar berharap itu hanya imajinasi saya."
m "Bahwa Anda benar -benar menghormatinya dan memahami betapa baiknya Bob."
show mila jeans_and_blouse_angry_close
ms "Saya melihat pria yang baru saja menawari saya uang."
show mila jeans_and_blouse_angry_disgust_open
m "Satu -satunya pelacur di meja ini adalah Anda."
m "Saya yakin teman Anda akan membayar Anda tiga kali lipat untuk meniduri Anda."
show mila jeans_and_blouse_angry_close
ms "Saya melihat sekeliling dan memperhatikan bahwa Bob sudah kembali dari toilet dan berdiri beberapa langkah dari saya dengan mulut terbuka."
show bob surprised at left:
    xzoom 0.8 yzoom 0.8
show mila jeans_and_blouse_angry_open
m "Kami meninggalkan Bob."
m "Saya sangat perlu bercinta dengan seseorang."
ms "Pria sombong yang mencoba membelikanku pucat dan terdiam."
ms "Aku meliriknya dengan penghinaan"
show mila jeans_and_blouse_angry_disgust_open
m "A asli __tag_0__man__tag_1__"
show mila jeans_and_blouse_angry_close:
    easein 0.5 xpos 0.25
    linear 0.4 xzoom -1.0
ms "Saya mengambil tangan Bob dan berjalan ke pintu keluar."
show mila jeans_and_blouse_angry_open:
    easein 1 xpos 0.8
show bob surprised at left:
    xzoom 0.8 yzoom 0.8
    easein 1 xpos 0.5
m "Miliki malam yang menyebalkan, brengsek"
bob_unknown "..."
"..."
play sound "shop_door.mp3"


scene bg night_city
ms "Ketika kami bergerak jauh dari kafe dan kemarahan saya menguap, saya merasa malu dengan apa yang telah saya lakukan."
ms "Saya menghela nafas."
show mila jeans_and_blouse_remorse at center
m "Maaf, Bob ... saya tidak bisa menolak."
show bob smile at left:
    xzoom 0.8 yzoom 0.8
ms "Dia menggaruk bagian belakang kepalanya dengan malu."
bob "Tidak, Anda tidak perlu meminta maaf ... __tag_0__it adalah saya ... __tag_0__ Anda tahu? .. __tag_0__ dan tidak ada seorang pun sebelumnya ... __tag_0__ seperti, secara umum ..."
ms "Bob menatapku dan tersenyum."
show bob idle
bob "Terima kasih."
show mila jeans_and_blouse_run_smile
m "Hah."
m "Dengan senang hati."
show bob smile
bob "Sejujurnya, saya bahkan menyukainya."
show mila jeans_and_blouse_proud_smile
ms "Saya mengembalikan senyumnya."
ms "Bob tidak mengalihkan pandangan dari saya untuk waktu yang lama."
bob "Kamu tersenyum dengan sangat indah ..."
show bob sad
ms "..."
show mila jeans_and_blouse_blush_embarassed
ms "Berhenti ... __tag_0__ Anda memalukan saya ..."
show mila jeans_and_blouse_blush_embarassed_twist_hair
m "T-terima kasih ..."
show bob shy
bob "Maaf…"
show mila jeans_and_blouse_surprise
m "???"
ms "Saya menatapnya dengan terkejut."
m "Untuk apa?"
show bob sad
bob "Saya pikir saya telah jatuh cinta dengan Anda."
show mila jeans_and_blouse_shock
m "Semuanya tiba -tiba melambat dan kemudian berhenti."
ms "..."
m "Apa?"
show bob sad2
bob "Aku mencintaimu, Mila."
ms "Bob tersenyum sedih."
show mila jeans_and_blouse_panic at center with hpunch
m "..."
ms "Omong kosong…"
ms "Omong kosong!"
ms "Fuck fuck!"
show mila jeans_and_blouse_sad_looking_aside
m "SAYA…"
ms "Bob mengangkat tangannya dalam gerakan berhenti."
show bob waving
bob "Jangan berkeringat ... __tag_0__ setiap hal baik."
bob "Saya sudah tahu jawaban Anda ..."
show bob sad
ms "Matanya menjadi kusam dan kosong lagi."
show mila jeans_and_blouse_sad_looking_down
ms "Sialan! Anda tidak bisa bermain dengan perasaan orang ..."
ms "Apa yang saya lakukan?"
ms "Aku tidak bisa meninggalkannya pada nasibnya sekarang."
ms "Kami bertanggung jawab untuk mereka yang jatuh cinta dengan kami!"
show mila jeans_and_blouse_sad_looking_up
m "..."
show mila jeans_and_blouse_sad_looking_up:
    easein 0.5 xpos 0.35
show bob sad
ms "Bob berbalik dan hendak pindah, tapi aku meraih lengannya, memaksanya untuk menatapku."
m "Tunggu."
ms "Hidup kembali ke mata Bob sejenak, tetapi segera keluar lagi."
show mila jeans_and_blouse_serious_open_mouth
m "Saya sudah menikah Bob. Dan saya mencintai suami saya."
show bob sad2
ms "Bob terkekeh dan mengangguk."
bob "Aku tahu."
m "Tetapi…"
ms "Aku menutup mataku."
show mila jeans_and_blouse_blush_looking_aside
m "Saya akan memikirkan tentang apa ... __tag_0__ kita bisa lakukan ..."
show bob sad
ms "Bob mengerutkan kening."
bob "Apa maksudmu?"
"..."
"..."
show mila jeans_and_blouse_front
m "Ayo pergi."
bob "..."
bob "Dimana?"
show mila jeans_and_blouse_run_smile:
    easeout 1 xpos 0.65
show bob sad:
    easeout 1 xpos 0.25
m "Ke rumah, dimana lagi?"
ms "Aku menariknya bersamaku."
bob "Mila ..."
ms "Bob memprotes dengan ragu -ragu, tetapi mengikuti."
ms "Aku berbalik dan mengedipkan mata padanya."
show mila jeans_and_blouse_smile_wink
m "Serahkan padaku!"
bob "..."
hide mila
hide bob
"__tag_0 __..."
scene bg doors
ms "Saya meninggalkan Bob di pintu apartemennya dan menyuruhnya datang untuk makan siang besok pagi."
ms "Dia masih menatapku dengan tak percaya, tetapi setuju."



"__tag_0 __..."
scene bg apartments
play sound "door-open-close.mp3"
show mila jeans_and_blouse_sad_looking_aside at center
ms "Memasuki apartemen, saya tidak tahan dan menangis"
ms "Perasaan Bob dan pengakuannya sangat murni ... __tag_0__ sangat tulus"
ms "Sesuatu pecah dalam diriku ..."
ms "Di satu sisi, saya senang."
show mila jeans_and_blouse_sad_looking_up
ms "__Tag_0__ sebagai seorang pria ...Sangat bodoh untuk menyangkal bahwa saya suka Bob. __Tag_0__ sebagai pribadi. __Tag_0__ sebagai teman."
ms "Saya belum pernah mengalami ini sebelumnya ... __tag_0__ Belum pernah saya harus menolak setelah pengakuan."
ms "Satu -satunya orang lain yang mengaku kepada saya adalah Paul ..."
ms "Entah bagaimana terjadi bahwa semua orang di sekitar kami tahu bahwa kami berkencan dan semuanya baik -baik saja dalam hubungan kami ..."
ms "Mungkin itu sebabnya tidak ada yang mencoba mengaku kepada saya ..."
ms "Tapi perasaan ini ... __tag_0__ Kehancuran ... __tag_0__ pengkhianatan ..."
ms "Saya tidak bisa menggambarkannya ..."
ms "Itu menghancurkan saya dari dalam. __Tag_0__ Saya ingin mendukung Bob ... __tag_0__ untuk memberinya kebahagiaan ..."
ms "Tapi aku tidak bisa ..."
show mila jeans_and_blouse_sad_looking_up:
    linear 1.0 xpos 0.75
show paul suit_shock at left
p "Bayi?"
show mila jeans_and_blouse_sad_looking_aside
m "..."
p "Apa yang terjadi?"
ms "Saya tidak tahu bagaimana menjawab"
ms "Saya tidak tahu harus mulai dari mana"
ms "Saya sangat bingung, __tag_0__ pikiran saya saling terkait, __tag_0__, dan itu memunculkan makna dan gambar yang aneh"
ms "Saya diam -diam membiarkan mereka keluar"
p "Cahaya matahari?"
label first_nts_choice:
    show screen nts_stats_overlay

    menu:
        "Mila tersesat dalam pikirannya. Paul harus:"
        "Dorong dia untuk menjawab (ketundukan Mila + 1)":
            $ dom += 1
            jump push
        "Biarkan dia menjadi, dia akan berbicara saat dia siap (dominasi Mila + 1)":
            $ mila_dom += 1
            jump slide

label push:

show paul suit_frown:
    easeout 1.0 xpos 0.45
show mila jeans_and_blouse_sad_looking_up:
    linear 1.0 xpos 0.75
ms "Paul mengambil tanganku, yang menarikku keluar dari angin puyuh emosi."
hide screen nts_stats_overlay
show mila jeans_and_blouse_run_smile
ms "Saya menatapnya dengan rasa terima kasih dan tersenyum"
p "Apa yang terjadi?"
ms "Suaranya terdengar lebih ketat dan lebih keras"
ms "Ini memiliki efek menguntungkan bagi saya"
ms "Akhirnya, pikiran saya jatuh ke tempatnya, dan saya bisa tenang."
jump lovetalk

label slide:

show mila jeans_and_blouse_sad_looking_down
ms "Subbed dalam pikiran saya, saya tidak memperhatikan bagaimana cangkir cokelat panas muncul di tangan saya."
hide screen nts_stats_overlay
ms "Saya tidak tahu berapa banyak waktu yang telah berlalu, tetapi saya bisa tenang dan menertibkan pikiran saya."
ms "Paul diam -diam menunggu."
show mila jeans_and_blouse_run_smile
ms "Aku tersenyum syukur padanya."

label lovetalk:

show mila jeans_and_blouse_serious_open_mouth
ms "Saya memberi tahu Paul apa yang terjadi."
ms "Tentang kolega Bob. __Tag_0__ tentang pertemuan kami di sebuah kafe. __Tag_0__ dan tentang pengakuannya."
ms "Paul mendengarkan dengan cermat saya. Dan saat ini, dia hanya menghela nafas."
show paul suit_frown
p "Saya tahu ini bisa terjadi ..."
m "..."
p "..."
show mila jeans_and_blouse_sad_looking_aside
m "Ini menyebalkan, ya?"
ms "Suaraku gemetar. __Tag_0__ Saya tidak mengerti bagaimana perasaan saya."
ms "Tetapi saya mengerti bahwa jika Paul mengatakan sesuatu yang kejam sekarang, saya tidak akan bisa tahan dan akan melakukan sesuatu ..."
ms "Dan akan menyesalinya setelah itu."
show paul suit_sad
p "..."
p "Aku takut bahkan membayangkan diriku di tempatnya ..."
ms "..."
show mila jeans_and_blouse_surprise
ms "Bagaimana saya bisa berpikir bahwa dia akan mengatakan sesuatu yang keras?"
ms "Lagipula dia adalah suamiku ... __tag_0__ untuk alasannya."
ms "..."
show mila jeans_and_blouse_sad_looking_up
m "Saya ... saya juga ... __tag_0__ Saya tidak tahu bagaimana harus bereaksi terhadap ini ..."
p "..."
m "..."
p "..."
show mila jeans_and_blouse_serious_open_mouth
m "Dengarkan ... __tag_0__ apakah kamu ... __tag_0__ apakah kamu ingat bagaimana rasanya? __Tag_0__ untuk jatuh cinta?"
p "..."
show paul suit_frown
p "Saya tidak yakin apa maksud Anda ...__ tag_0__ saya suka __tag_1__you__tag_2__. __Tag_0__ Tidak sedikit dari aku mencintaimu sepuluh tahun yang lalu."
ms "Perasaan hangat tumpah di tubuh saya"
show mila jeans_and_blouse_run_smile
m "Aku pun mencintaimu."
p "..."
m "Tapi saya tidak membicarakannya. __Tag_0__i berarti ..."
show mila jeans_and_blouse_sad_looking_down
m "Apakah Anda ingat perasaan itu, saat Anda jatuh cinta?"
show mila jeans_and_blouse_sad_looking_up
m "Ingat seberapa sering jantung Anda berdetak lebih cepat saat pikiran itu?"
show mila jeans_and_blouse_sad_looking_aside
m "Apa yang terjadi di siang hari terus mengulangi dalam ingatan Anda berulang kali."
show mila jeans_and_blouse_sad_looking_down
m "Betapa putus asa, bahkan menyakitkan, Anda ingin menyentuh, berpelukan, pelukan dan ciuman?"
p "..."
show paul suit_shock
p "Tentu. __Tag_0__ dan saya masih merasakannya. __Tag_0__ untuk saya tidak ada yang berubah ..."
show mila jeans_and_blouse_angry_close
ms "Saya mengerutkan kening."
m "Tidak. __Tag_0__ Sesuatu telah berubah."
show mila jeans_and_blouse_serious_open_mouth
m "Terkadang bagi saya sepertinya Anda bosan dengan saya ..."
m "Bahwa aku bukan lagi gadis paling cantik dan diinginkan untukmu ... __tag_0__ bahwa aku hanya membosankan ..."
show mila jeans_and_blouse_sad_looking_down
m "Semua yang Anda katakan dan lakukan untuk saya adalah rutinitas yang sama untuk Anda seperti bekerja."
p "..."
show paul suit_frown
p "Anda salah..."
show mila jeans_and_blouse_run_smile
m "Aku tahu. __Tag_0__ Maksud saya ... __tag_0__ sekarang saya tahu."
show mila jeans_and_blouse_sad_looking_aside
m "Tapi perasaan ini ... __tag_0__ kelelahan ini ..."
m "Ada di dalam. __Tag_0__ itu. __Tag_0__ tidak hilang."
show mila jeans_and_blouse_sad_looking_up
m "Dan kata -kata Bob ... __tag_0__ mereka membangunkan sesuatu di dalam diri saya."
show mila jeans_and_blouse_sad_looking_down
m "Sensasi itu. __Tag_0__ Lupa sensasi cinta ..."
show screen nts_stats_overlay
menu:
    "Haruskah Paul melakukan sesuatu?"
    "Ambil inisiatif, tunjukkan kepadanya cintamu (kepatuhan Mila + 1)":
        $ dom += 1
        $ paul_took_initiative = True
        jump cafe
    "Lebih baik memberinya beberapa ruang untuk membiarkannya mengetahui perasaannya (dominasi Mila + 1)":

        $ mila_dom += 1
        jump chat

label cafe:
p "..."
show paul suit_open_mouth_neutral
p "Kamu tahu. Saya punya ide."
hide screen nts_stats_overlay
show mila jeans_and_blouse_surprise
m "?"
p "Ayo pergi."
m "Apa? __Tag_0__ di mana?"
p "Ayo pergi, aku akan memberitahumu sepanjang jalan"
m "..."
n "__tag_0__. __tag_0__. __tag_0__."
scene mall
show mila jeans_and_blouse_serious_open_mouth
m "Dan? __Tag_0__ Apa yang kita lakukan di sini?"
show mila jeans_and_blouse_serious_open_mouth:
    linear 1.0 xpos 0.75
show paul suit_grin:
    xpos 0.25
ms "Paul hanya menyeringai sebagai tanggapan dan menarik saya ke toko pakaian."
"..."
show paul suit_frown
show mila jeans_and_blouse_run_smile
m "Apa yang kita cari?"
ms "Paul memilah gaun dan pakaian yang berbeda dengan wajah yang tidak puas"
p "Kami memilih gaun untuk Anda"
show mila jeans_and_blouse_front
ms "Paul mengeluarkan gaun lain, meringis dan meletakkannya kembali"
ms "Saya berlari melalui rak dengan mata saya"
ms "Saya sudah memiliki beberapa gaun di rumah, yang tidak pernah saya kenakan."
ms "Semua sama, kita tidak pernah pergi ke tempat -tempat di mana memakainya akan sesuai ..."
show mila jeans_and_blouse_serious_open_mouth
m "Sayang, saya punya gaun. Jika Anda memperingatkan saya sebelumnya, saya akan mengenakannya untuk Anda."
ms "Paul menatapku dengan serius"
ms "Dia sepertinya mengambil kata -kata saya karena dia tidak bisa merumuskan apa yang ingin dia lakukan."
show paul suit_open_mouth_neutral
p "Saya ingin ...__ tag_0__ mendandani Anda."
p "Entah bagaimana dengan cara khusus ..."
show paul suit_blush_looking_aside
p "Dan membual. __Tag_0__kind dari ... __tag_0__ seperti: __tag_0__everyone, lihat - __tag_0__ gadis ini bersamaku."
p "Sesuatu seperti itu ..."
m "..."
show mila jeans_and_blouse_run_smile
ms "Saya tersenyum"
m "Apakah Anda memiliki sesuatu dalam pikiran?"
show paul suit_frown
ms "Paul kembali ke rak"
p "Tidak juga ... __tag_0__ Saya ingin sesuatu yang lebih ... __tag_0__ __tag_2__ Frank."
show mila jeans_and_blouse_blush_embarassed
ms "Jantungku berdegup kencang ..."
ms "Tubuh saya menjadi hangat .__ tag_0__ pakaian saya tiba -tiba menjadi berduri dan kaku __tag_0__ dan kulit saya menjadi terlalu sensitif."
ms "Saya tertelan"
ms "Sensasi ini ..."
show mila jeans_and_blouse_blush_embarassed_twist_hair
ms "Mereka tidak seperti cinta"
ms "Mereka tidak mirip dengan apa pun yang sebelumnya berpengalaman"
ms "Saya ingin Paul memberi tahu saya apa yang harus dilakukan"
ms "Saya ingin dia memuji saya"
show mila jeans_and_blouse_blush_looking_aside
ms "Sehingga dia menatapku dan hanya aku"
ms "Jadi dia membanggakan saya"
ms "Jadi dia akan menggunakan saya. __Tag_0__ sebagai sesuatu."
ms "Jadi orang lain menginginkan saya."
ms "Sehingga Paulus memutuskan siapa yang layak untuk saya"
show mila jeans_and_blouse_run_smile
m "Mungkin sesuatu seperti ini?"
ms "Saya menunjuk gaun pendek merah dengan punggung terbuka"
ms "Kegembiraan membuat pikiran saya berkabut"
ms "Paul menatapku dengan terkejut dan gaun yang aku pilih"
show paul suit_open_mouth_neutral
p "Apa kamu yakin?"
m "..."
p "..."
show mila jeans_and_blouse_proud_smile
m "Jika suami saya menginginkannya, saya bahkan bisa telanjang"
ms "Saya sendiri tidak percaya apa yang saya katakan"
ms "Tetapi jika Paul benar -benar menyuruh saya menanggalkan pakaian"
show mila jeans_and_blouse_blush_looking_aside
ms "Saya akan mematuhi"
p "..."
m "..."
show paul suit_blush_looking_aside
p "Lalu ... __tag_0__let mencoba"
p "Dan ini"
ms "Paul memberiku sepatu hak tinggi"
show mila jeans_and_blouse_surprise
m "..."
m "Saya khawatir saya tidak bisa berjalan di dalamnya"
p "..."
show paul suit_open_mouth_neutral
p "Lalu aku akan membawamu."
show mila jeans_and_blouse_blush_looking_aside
m "..."
m "Oke..."
scene changing room
ms "Saya pergi ke ruang pas"
n "__tag_0__. __tag_0__. __tag_0__."
show mila sly_dress_shy at right:
    xpos 0.75
m "..."
show paul suit_shock:
    xpos 0.3
p "..."
m "..."
m "Dengan baik?"
show paul suit_open_mouth_blush
p "Anda terlihat luar biasa"
show mila sly_dress_shy_giggle
m "..."
m "Hehe"
p "Dan sangat seksi"
show mila sly_dress_shy
m "..."
show paul suit_open_mouth_neutral
p "Berbalik"
show mila sly_dress_from_behind
m "..."
p "..."
show paul suit_open_mouth_blush
p "Anda ... __tag_0__ __tag_1__ ass __tag_2__ terlihat mengagumkan"
ms "Suara Paul menjadi sedikit lebih tenang. Rupanya, masih sulit baginya untuk memainkan macho brutal."
ms "Saya menyembunyikan senyum dan melengkung punggung saya untuk memberinya pemandangan terbaik"
show mila sly_dress_from_behind_arched_back
p "Ahem ... __tag_0__ kita akan menerimanya!"
show mila sly_dress_shy_giggle
m "..."
m "Nah ... apa selanjutnya?"
show paul suit_grin
ms "Paul menyeringai."
p "Sekarang kami pergi ke restoran."
"__tag_0__. __tag_0__. __tag_0__."
scene bg restaurant
show mila sly_dress_neutral:
    xpos 0.5 ypos 0.1
show paul suit_shock:
    xpos 0.15
"???" "Selamat datang!"
show mila sly_dress_shy:
    easeout 1 xpos 0.085
ms "Segera setelah kami masuk ke dalam, seorang pelayan muda bertemu kami"
ms "Kami berdua merasa malu untuk saling memandang, jadi saya secara naluriah bersembunyi di belakang Paul"
ms "Dia mencoba yang terbaik untuk tidak melihat garis leher saya dan fokus pada Paul sendirian"
"..."
ms "Musik diputar dengan tenang"
ms "Tidak banyak makan malam di restoran"
show mila sly_dress_from_behind:
    xpos 0.5
hide paul
ms "Saat kami berjalan ke meja, saya mencoba menarik gaun itu, karena sedang berjuang, mengekspos pantat saya"
ms "Saya benar -benar merasakan pandangan orang yang ditujukan kepada saya"
show mila sly_dress_shy
ms "... __tag_0__ sangat memalukan"
ms "Tapi __tag_0__i menyukainya"
ms "..."
hide mila
ms "Paul memesan sebotol anggur dan bersikeras agar saya minum beberapa gelas."
ms "Ini agak menjernihkan kepalaku dan memberontak pikiranku pada saat yang sama."
show big mila_table_relaxed_from_left
ms "Senyuman muncul di wajahku, semua kegugupan dan peristiwa hari ini menghilang di suatu tempat."
ms "Hanya kegembiraan yang tersisa."
ms "Paul memperhatikan perubahan dalam suasana hati saya."
show big paul_serious_open_mouth_from_right with wipeleft
p "Saya ingin Anda melakukan sesuatu untuk saya."
show big mila_table_intrigued_from_left with wiperight
m "?"
ms "Aku mencondongkan tubuh ke depan untuk menjadi lebih dekat dengannya."
m "Anda memiliki semua perhatian saya."
show big paul_serious_open_mouth_from_right with wipeleft
p "Saya ingin Anda menunjukkan payudara Anda kepada seseorang di sini."
show big mila_table_surptised_from_left with wiperight
ms "..."
ms "Jika bukan karena anggur, saya akan takut dan menolak."
show big mila_table_smirk_from_left
ms "Tapi saya hanya tersenyum dan mengambil beberapa tegukan lagi."
m "Kepada siapa misalnya?"
show big paul_serious_open_mouth_from_right with wipeleft
p "Bagaimana dengan pria itu di dekat toilet?"
show big mila_table_profile_looking_to_the_side_from_left with wiperight
ms "Saya melihat ke mana dia menunjuk."
show big mila_table_smirk_from_left
m "Tentu"
"__tag_0__. __tag_0__. __tag_0__."
hide big
show mila sly_dress_from_behind_arched_back
ms "Aku bangkit dan, kucing berjalan menuju pria itu"
ms "Saya tidak lagi peduli bahwa gaun itu menarik dan membuka pandangan yang jelas di pantat saya"
ms "Justru sebaliknya. __Tag_0__ Saya ingin menunjukkan lebih banyak lagi ..."
ms "Aku masih sedikit bergoyang ..."
ms "Namun ternyata untuk dengan yakin berdiri di atasnya, Anda hanya perlu sedikit lebih percaya diri"
ms "Dan anggur melakukan pekerjaan yang baik dengan memberi saya kepercayaan diri"
ms "Saya meluruskan tali sehingga lebih mudah bagi dada saya."
ms "Mendekati pria yang saya pura -pura sedikit lebih mabuk daripada yang sebenarnya, dan membungkuk, mendorong payudaraku bersama dengan siku"
show mila sly_dress_drunk_tits_out
m "Saya minta maaf"
"???" "..."
ms "Pria itu menatapku dan tatapannya berhenti di dadaku."
show mila sly_dress_drunk_tits_out_pointing_finger
m "Pintu di sebelah kiri apakah itu toilet pria atau wanita?"
ms "Pria itu tersenyum tidak menyenangkan, meraih tanganku dengan erat dan menarikku ke toilet."
"???" "Di sebelah kanan, izinkan saya membantu Anda, gadis."
scene bg toilet
play sound "door-open-close.mp3"
show mila sly_dress_scared
ms "Saya tidak punya waktu untuk sadar, dia sudah menyeret saya ke dalam stan."
ms "Saya sangat takut, tetapi tidak bisa berteriak; Tenggorokan saya kering, dan saya hanya bisa bergumam dengan lemah."
show mila sly_dress_scared_open_mouth
m "W-tunggu ..."
show cg pinned_to_the_wall_scared_cry:
    xzoom 0.75 yzoom 0.75 ypos 1.0
    linear 1.0 ypos 0.025
show mila sly_dress_scared_open_mouth:
    linear 1.0 xpos 0.85
ms "Tapi pria itu tidak mendengarkan saya"
ms "Sebelumnya, ketika Paul marah padaku, aku merasa takut"
ms "Tapi ketakutan itu tidak menakutkan"
ms "Jenis ketakutan itu, yang membuatmu terangsang"
ms "Seperti saat Anda tahu, bahwa kali ini seks akan menjadi kasar"
ms "Kasar, tapi ... __tag_0__safe."
ms "Karena aku tahu Paul tidak akan pernah menyakitiku ..."
ms "Tapi sekarang ..."
ms "Ketakutan ini sama sekali tidak menyenangkan"
ms "Ketakutan ini jelek, _ tag_0__ kekerasan, _ tag_0__ berbahaya ..."
ms "Satu -satunya hal yang saya inginkan pada saat itu adalah melarikan diri"
ms "..."
ms "Pria itu menyematkanku ke dinding toilet dan meraih payudaraku"
ms "Tapi untungnya, dia tidak punya waktu untuk melakukan apa pun."
show cg pinned_to_the_wall_scared_cry_pleading_eyes:
    xzoom 0.75 yzoom 0.75 ypos 1.0
    linear 1.0 ypos 0.025
ms "Pintu terayun terbuka dan Paul memasuki toilet."
ms "Pria itu menatapnya dengan tidak senang."
hide cg
"???" "Saya tidak keberatan berbagi, tetapi saya akan menjadi yang pertama."
show paul suit_angry at left:
    xzoom -1
show mila sly_dress_scared
p "..."
p "..."
show paul suit_angry_open_mouth
p "Bukan untuk Anda memutuskan"
show paul suit_angry_open_mouth:
    easeout 0.5 xpos 0.5
ms "Paul mengambil tanganku"
show paul suit_open_mouth_neutral
p "Ayo, sayang."
show paul suit_open_mouth_neutral:
    linear 0.5 xpos 0.25
show mila sly_dress_scared:
    linear 0.5 xpos 0.65
"???" "..."
show paul suit_open_mouth_neutral:
    linear 0.5 xpos 0.15
show mila sly_dress_scared:
    linear 0.5 xpos 0.35 xzoom -1
ms "Pria itu tidak ikut campur, dan membiarkan kami melewatinya."
ms "Tapi dia membuat meringis dan meludah di lantai."
"???" "Sialan Cuckold."
m "..."
p "..."
play sound "door-open-close.mp3"
scene bg restaurant
show paul suit_sad at center
show mila sly_dress_scared at right:
    xpos 0.85
m "..."
p "..."
ms "Suasana hati itu rusak."
ms "Kabut anggur langsung menghilang dari kepalaku."
ms "Suasana hati yang menyenangkan hilang."
ms "Kami baru saja menelepon taksi dan kembali ke rumah, tidak berbicara dalam perjalanan kembali."
"__tag_0__. __tag_0__. __tag_0__."
if _in_replay:
    return
jump lovetalk2

label chat:
scene bg apartments
show paul suit_frown at left
p "..."
show mila robe_think at right
ms "Keheningan tegang jatuh di kamar"
hide screen nts_stats_overlay
ms "Emosi dan perasaan membuat saya kewalahan"
ms "Di sebelah Paul, saya selalu merasa sangat terlindungi dan tenang ..."
show mila robe_puzzled_frown
ms "Tapi pada saat yang sama ..."
ms "Saya menginginkan sesuatu yang lain"
show mila robe_blush_shy_looking_aside
ms "Dan Paul juga menginginkan ini, __tag_0__ Saya pikir ..."
ms "Dia terlalu dibatasi oleh prinsip -prinsipnya untuk mengakuinya"
ms "..."
show mila robe_sad
ms "Pikiran tentang Bob dan pengakuannya meledak di kepalaku"
ms "Mereka bercampur dengan pikiran hubungan saya dengan Paul, __tag_0____about keluhan saya ... __tag_0__ dan tentang tindakan saya."
show mila robe_puzzled_frown
ms "Perasaan gentar ini ... mereka mirip dengan apa yang saya rasakan ketika saya mengirim sms dengan pria itu dari aplikasi ..."
ms "Siapa namanya lagi? __ tag_0 __... __tag_0__dick, saya pikir?"
show mila robe_shhhh_finger
ms "..."
ms "Mungkin mengulangi pengalaman itu bermanfaat, __ tAG_0__ tetapi kali ini, itu harus termasuk Paul."
ms "Ini mungkin membantu saya untuk mengatur pikiran saya dan memahami jika saya membingungkan kegembiraan dengan cinta ..."
hide mila
scene bg mila_on_laps_smile
ms "Saya berbaring di dekat Paul dan mengeluarkan tablet saya."
ms "Paul diam -diam menepuk kepalaku."
ms "Saya meringkuk kepadanya untuk menunjukkan bahwa saya menyukainya."
ms "..."
p "Ada apa?"
ms "..."
scene bg mila_on_laps_looking_up
m "Ingat situs tempat saya mengobrol dengan pria itu?"
p "..."
p "Ya."
ms "Suara Paul terdengar agak kasar."
ms "Rupanya dia belum sepenuhnya bisa mengatasi kecemburuannya."
scene bg mila_on_laps_looking_up_open_mouth
m "Saya ingin kami mengobrol di sana dengan seseorang."
scene bg mila_on_laps_looking_up
ms "Paul tegang."
scene bg mila_on_laps_looking_up_open_mouth
m "Bersama."
scene bg mila_on_laps_looking_up
p "..."
p "Bersama?"
scene bg mila_on_laps_smile
m "Ya. __Tag_0__together."
ms "Saya melihat suami saya."
scene bg mila_on_laps_looking_up_concerned
m "Anda tidak suka idenya?"
p "..."
m "..."
p "..."
scene bg mila_on_laps_smile
m "I'll take your silence as \"Yes\""
ms "Setelah beberapa menit berkeliaran di situs, saya menerima pesan dari beberapa pria."
ms "Setelah representasi dangkal, percakapan mulai menjadi lebih jujur."
ms "..."
ms "Yang umumnya tidak mengejutkan - mengetahui subjek situs."
ms "..."
scene bg mila_on_laps_looking_up_open_mouth
m "Dia mengatakan bahwa dia ingin mengetahui preferensi seksual saya."
scene bg mila_on_laps_smile
p "..."
p "Dan apa yang Anda jawab?"
scene bg mila_on_laps_looking_up_open_mouth
m "Belum ada"
scene bg mila_on_laps_smile
p "..."
m "Saya akan menulisnya seperti ini: Saya suka ketika saya digunakan sebagai objek."
scene bg mila_on_laps_looking_up_open_mouth
p "..."
scene bg mila_on_laps_smile
m "Agak membosankan, bukan begitu?"
p "..."
m "Bagaimana: Saya menyukainya ketika mereka menghukum saya seperti saya adalah gadis yang nakal."
scene bg mila_on_laps_looking_up_open_mouth
p "..."
p "Mungkin lebih baik untuk mengatakan: bercinta seperti pelacur yang tidak berguna ..."
m "..."
scene bg mila_on_laps_smirk
m "..."
scene bg mila_on_laps_smile
m "..."
m "Dia mengatakan bahwa dia meniduri semua pelacurnya seperti itu."
p "..."
scene bg mila_on_laps_looking_up_open_mouth_giggle
m "I am pretty sure that those \"bitches\"adalah imajiner, meskipun ..."
p "..."
p "Kita semua ingin tampak lebih keren dari kita."
m "..."
scene bg mila_on_laps_looking_up_open_mouth
m "Semua kecuali Anda."
scene bg mila_on_laps_smirk
m "Anda sudah paling keren."
p "..."
scene bg mila_on_laps_smile
m "..."
m "Dia mengatakan bahwa dia ingin mengikat saya dan bercinta lubang kepalaku."
p "..."
p "Kedengarannya panas ..."
m "..."
scene bg mila_on_laps_looking_up_concerned
m "Anda pikir?"
m "..."
m "Kemudian..."
scene bg mila_on_laps_shy
m "Apakah __tag_0__you__tag_1__ akan bercinta dengan lubang kepalanya?"
p "..."
p "Ya, saya pikir saya melakukannya ..."
m "..."
scene bg mila_on_laps_smirk
m "Apakah Anda ingin saya membawa tali?"
p "..."
p "Kamu sangat bejat ..."
scene bg mila_on_laps_looking_up_open_mouth_giggle
m "Hehehe"
p "..."
ms "Suasana hati terlalu menyenangkan untuk proposal saya untuk beraksi"
ms "Jadi saya kembali ke obrolan."
scene bg mila_on_laps_smile
m "..."
m "Oh! Dia meminta untuk mengirim foto."
p "..."
p "Ini berbahaya, Mila."
m "Aku tahu."
p "..."
scene bg mila_on_laps_shy
m "..."
p "..."
p "Mungkin jika kita mengambilnya tanpa wajah Anda di dalamnya?"
m "..."
scene bg mila_on_laps_looking_up_open_mouth_giggle
m "__tag_0__. __tag_0__. __tag_0__."
scene bg apartments
ms "Saya dengan mudah melompat dari tempat tidur dan menyerahkan telepon kepada Paul."
show mila robe_smile_grin at center
m "Katakan apa yang harus saya lakukan."
p "..."
p "Lepaskan sabuk, __tag_0__ Saya pikirkan ..."
ms "Saya mematuhi tanpa ragu -ragu."
show mila robe_untied
ms "Goosebumps berlari ke bawah tubuh."
ms "Mata hitam kamera menatapku dari tangan Paul."
ms "Saya merasa seperti kelinci di depan ular."
ms "Seolah dihipnotis, saya mengharapkan nasib saya."
ms "Saya merindukan ini."
ms "Jubah mandi mengalir melintasi tubuh saya, membuka pemandangan pusar dan vagina."
ms "Saya melihat mata kamera, dan itu menatap saya."
p "..."
p "Tunjukkan diri Anda"
show mila nude_think
m "Perlahan -lahan saya membuang jubah mandi saya, memperlihatkan tubuh saya."
p "..."
p "Ya Tuhan, kamu sangat cantik ..."
show mila nude_blush
m "..."
ms "Saya lupa saat terakhir kali Paul menceritakan perasaannya secara terbuka."
ms "Saya hampir tidak menahan diri, __tag_0__i mengusir pikiran yang saya impikan diikat."
show mila nude_blush_masturbate
ms "Dan ingin merasakan ayam paul yang kuat di tenggorokanku."
m "..."
p "..."
p "Siap."
show mila nude_surprised:
    pause 0.3
show mila nude_blush
ms "Suara Paul menarik saya keluar dari pikiran saya."
ms "Saya mengambil telepon dan melihat bahwa dia sudah mengirim beberapa foto kepada pria itu."
show mila nude_blush_looking_aside
m "..."
ms "Keheningan yang sangat tegang digantung."
ms "Sejujurnya, saya tidak lagi benar -benar ingin terus mengirim SMS dengan orang asing."
ms "Tetapi saya memutuskan bahwa lebih baik memompa kegembiraan Paul lebih banyak"
show mila nude_reading_message_hand_on_hip
m "..."
m "Dia menulis bahwa saya sangat seksi."
p "Dan saya setuju dengannya."
show mila nude_reading_message_hand_on_hip_grin
m "Hehe"
ms "Saya perhatikan bahwa penis Paul bengkak"
show mila nude_reading_message_hand_on_hip_biting_lips
ms "Sedikit lebih dan dia tidak akan bisa menahan diri ..."
show mila nude_reading_message_hand_on_hip_annoyed
m "..."
m "Dia mengirim Dickpic"
p "..."
m "..."
p "..."
show mila nude_reading_message_hand_on_hip_annoyed_open_mouth
m "Siapakah idiot yang datang dengan gagasan bahwa ada seseorang yang suka foto Dick?"
show mila nude_reading_message_hand_on_hip_annoyed
p "..."
show mila nude_reading_message_hand_on_hip_annoyed_open_mouth
m "Dan sekarang dia ingin FaceTime"
show mila nude_reading_message_hand_on_hip_annoyed
p "..."
show mila nude_reading_message_hand_on_hip_annoyed_open_mouth
m "Dan sekarang dia spam dengan banyak pesan."
m "Menakutkan..."
show mila nude_sad
ms "Sesaat dan suasana hati hilang."
ms "Pria itu terus membuat tuntutan untuk mengambil lebih banyak foto, menunjukkan wajah saya dan bertanya di mana saya tinggal."
ms "Upaya untuk membantunya menemukan setidaknya sebagian kecil dari kewarasan tidak mengarah pada apa pun, jadi saya hanya memblokirnya."
ms "..."
ms "..."
ms "Suasana hati lagi menjadi suram."
ms "Dan pikiran tentang pengakuan Bob merangkak ke kepalaku lagi."
"__tag_0__. __tag_0__. __tag_0__."
if _in_replay:
    return

label lovetalk2:
scene bg apartments
ms "Merasakan kelelahan dari semua yang terjadi, saya memutuskan untuk mandi"
scene 127_b-day_shower
ms "..."
ms "Jet air panas membantu saya tenang dan menertibkan pikiran saya."
ms "Tetapi pikiran tentang pengakuan Bob masih belum hilang."
ms "Mereka hanya berhenti menjadi sangat menjengkelkan."
ms "__Tag_0__ terhadap diri saya sendiri.Hanya ada rasa sakit dan kebencian yang membosankan. __Tag_0__ menuju kehidupan. __Tag_0__ menuju nasib."
scene br
ms "Ketika saya meninggalkan kamar mandi dan mata saya bertemu dengan Paul, saya menyadari bahwa dia memikirkan pikiran yang sama."
scene bg apartments
show mila robe_puzzled_frown at right
show paul suit_sad at left
ms "Kami tersenyum sedih satu sama lain."
m "..."
p "..."
p "Perasaan yang tidak menyenangkan, kan?"
show mila robe_smile_awkward_open_mouth
m "Ya..."
p "..."
m "..."
show paul suit_open_mouth_neutral
p "Apa yang harus kita lakukan?"
show paul suit_sad
show mila robe_curious
m "Saya tidak tahu ... saya tidak yakin ..."
p "..."
m "..."
show paul suit_open_mouth_neutral
p "Dengar ... __tag_0__ Tampaknya bagi saya bahwa kita berdua mengerti bahwa ... __tag_0__games ... __tag_0__ tidak boleh dipikirkan ..."
p "Kali ini kita bisa mengatakan kita beruntung. __Tag_0__but Lain kali sebaliknya bisa jauh lebih buruk ..."
show paul suit_frown
ms "Saya hanya mengangguk sebagai tanggapan"
m "..."
show paul suit_blush_looking_aside
p "Itulah sebabnya..."
ms "Paul ragu -ragu, mengumpulkan pikirannya"
show mila robe_blush_shy_looking_aside
ms "Dia sepertinya bertengkar dengan dirinya sendiri, mencoba memilih kata -kata yang tepat."
ms "Saya menunggu dengan diam -diam, berusaha untuk tidak mengganggu aliran perasaan dan pikirannya"
show paul suit_open_mouth_blush
p "Saya pikir kita lebih baik tidak melakukan ini dengan beberapa orang asing acak ..."
show mila robe_puzzled
ms "Saya hanya mengangguk setuju. Sangat bodoh untuk menyangkal yang jelas."
show paul suit_blush_looking_aside
p "Lebih baik melakukan ini dengan orang lain ... __tag_0__ dengan seseorang yang layak ... __tag_0__ dari perhatian seperti itu ..."
ms "Akhirnya saya sadar apa yang dia maksud."
show mila robe_blush_shy_looking_aside
ms "Tubuh saya sekali lagi disiram dengan panas."
ms "Pengalaman digantikan lagi oleh kegembiraan"
ms "Dan kegembiraan ini mendorong solusi untuk semua masalah sekaligus."
show mila robe_blush_smirk
ms "Saya duduk di pangkuan Paul dan membawa wajah saya dekat dengannya."
ms "Penisnya belum berhasil bengkak"
ms "Karena itu, saya mulai memindahkan pinggul saya perlahan, menggosok vagina kemaluannya."
scene bg mila_on_top_of_paul
m "Anda pikir?"
m "Dimana saya harus memulai?"
show screen nts_stats_overlay
menu:
    "Apa yang harus dilakukan Paul?"
    "Ceritakan fantasinya kepada Mila (Ketundukan Mila + 1)":
        $ dom += 1
        jump fantasy
    "Hesitate (Mila's dominance + 1)":

        $ mila_dom += 1
        jump mila_lead

label fantasy:
scene bg mila_on_top_of_paul
ms "Paul ran his hands along my hips and looked passionately at me."
p "Saya ingin Anda bertemu Bob telanjang."
hide screen nts_stats_overlay
ms "Hoo ... Aku tidak berharap dia begitu mudah."
m "..."
m "Apakah Anda pikir dia bisa menahan diri dan tidak menyerang saya?"
p "Bob bukan orang seperti itu."
p "Saya pikir dia akan malu dan berpaling."
scene bg mila_on_top_of_paul_giggle
m "Ahah, saya pikir Anda benar."
ms "Tangan Paul meluncur di atas tubuh saya dan saya merasakan kegembiraan."
scene bg mila_on_top_of_paul
ms "Pinggul saya bergerak dengan keinginan mereka sendiri. Vagina saya hanya menuntut agar saya menggosoknya pada sesuatu."
ms "Dan dengan nyaman, penis Paul yang keras berada di tempat yang tepat."
p "Maka Anda akan memberinya makan siang ..."
m "..."
scene bg mila_on_top_of_paul_unsatisfied
m "Dan itu saja?"
ms "Saya berhenti sejenak."
ms "Paul tersenyum jahat."
p "Saya tahu itu tidak akan cukup untuk istri pelacur saya."
ms "Kata -kata kasarnya membuat putingku mengeras."
ms "Aku tersenyum malu."
m "Maaf..."
p "Untuk apa? Aku mencintaimu apa adanya."
ms "Paul menyentuh vaginaku dengan penisnya."
ms "Saya membiarkannya masuk ke saya dan perlahan -lahan mendorong pinggul saya ke bawah."
scene bg mila_on_top_of_paul_head_up
m "Ahhhh ..."
p "Anak yang baik."
ms "Aku menggigit bibirku dan membeku."
ms "Terlepas dari kenyataan bahwa saya sangat ingin merasakan setiap nada di kemaluannya ..."
ms "Saya juga ingin Paul membuat saya bergerak ..."
p "Maka Anda akan berlutut di depannya."
p "Ambil kemaluannya di tanganmu ..."
scene bg mila_on_top_of_paul
ms "Saya tidak tahan dan mulai memindahkan pinggul saya ..."
p "..."
p "Dan ... __tag_0__ Apa yang akan Anda lakukan selanjutnya?"
jump sex_paul

label mila_lead:
ms "Paul diam -diam menghindari matanya."
ms "Masih sulit baginya untuk mengakui keinginannya."
hide screen nts_stats_overlay
scene bg mila_on_top_of_paul_after_sex_kiss
ms "Karena itu, aku mencondongkan tubuh lebih dekat menciumnya dan kemudian berbisik:"
m "Saya pikir kami siap memberikan yang baik ... __tag_0__tender ... __tag_0__handjob ..."
ms "Saya menggerakkan tangan saya lebih rendah dan membelai penisnya yang keras"
m "Saya pikir Bob memiliki ayam yang gemuk dan sehat."
ms "Paul memejamkan mata dan mulai bernapas dengan cepat"
ms "Kontolnya semakin kuat dan lebih panas di tangan saya."
ms "Saya mulai membelai perlahan"
m "Besok dia akan datang kepada kita"
m "Dan saya akan menurunkan celananya ..."
m "Aku akan berlutut di depannya ..."
ms "Dick Paul benar -benar mengeras."
ms "Saya membimbingnya ke vagina saya yang sudah dibanjiri jus."
ms "Tangan Paul ada di pantatku. Dia menarikku ke bawah."
ms "Tapi aku tidak menyerah dan hanya menggoda penisnya dengan bibir basah vaginaku."
m "Bayangkan betapa terkejutnya dia akan ..."
m "Kemungkinan besar dia tidak akan bisa bertahan lama dan ingin cum pada saya ..."
m "Tapi aku tidak akan segera membiarkannya berakhir ..."
scene bg mila_on_top_of_paul_head_up
ms "Aku membentangkan bibirku dengan tangan kedua dan menurunkan pinggulku, membiarkan kemaluannya masuk ke dalamku."
m "Mmm ..."
ms "Saya tidak bisa menahan erangan."
p "Ya Tuhan ..."
ms "Saya tersenyum"
scene bg mila_on_top_of_paul
m "Haruskah saya melanjutkan?"
p "Ya ya! Sayang kamu yang terbaik!"
scene bg mila_on_top_of_paul_giggle
m "Ahah ..."

label sex_paul:
scene bg mila_on_top_of_paul
m "Lalu aku akan membuka mulut dan melihat Bob ..."
ms "Tampak bagi saya bahwa penis Paul jauh lebih besar dan lebih panas dari biasanya ..."
ms "Atau mungkin vaginaku yang mengencangkan lebih dari biasanya."
ms "Saya bergerak perlahan, terjun ke dalam imajinasi saya"
scene bg mila_on_top_of_paul_head_up
m "Tubuh berat Bob menggantung padaku"
m "Ayamnya yang gemuk bergoyang di depan hidungku ..."
m "Perlahan aku menjilat ketoknya ..."
ms "Aku menjilat bibirku, mereka tiba -tiba mati rasa."
m "Dan kemudian saya mengambilnya di mulut ..."
ms "Penis Paul menyentuh tempat yang paling menyenangkan."
ms "Dan karena gerakan yang lambat, dimungkinkan untuk merasakan setiap milimeter penisnya ..."
scene bg mila_on_top_of_paul
m "Itu tidak pas di mulut saya."
m "Itu terlalu tebal dan panjang untukku."
m "Saya mencoba menelannya lebih dalam, tapi saya tidak bisa ..."
ms "Tangan Paul meremas pantatku."
scene bg mila_on_top_of_paul_head_up
ms "Saya merasakan orgasme yang mendekat ..."
ms "Tapi saya mencoba untuk tetap di ambang, tunda ..."
ms "Meskipun kesadaran saya perlahan berlayar di ranah mimpi ..."
ms "Pada saat yang sama, saya kehilangan kendali atas tindakan saya."
ms "Pinggul saya mulai bergerak lebih cepat dan lebih cepat ..."
m "Bob memutuskan untuk membantuku ..."
m "Dia mengambil rambutku ..."
m "DAN..."
define flash = Fade(0.1, 0.0, 0.5, color="#FF0080")
scene bg mila_on_top_of_paul_head_up with flash
m "..."
scene bg mila_on_top_of_paul_after_sex_kiss with flash
p "..."
scene bg mila_on_top_of_paul_after_sex with flash
m "..."
m "Ho!"
m "..."
ms "Aku menggaruk punggung Paul dan menekan diriku ke arahnya."
ms "Kami datang hampir pada saat yang sama ..."
ms "Saya tidak segera mengerti ini, tetapi hanya beberapa detik setelah saya datang sendiri."
ms "Ayam Paul masih sedikit berdenyut dan saya dengan penuh syukur meremas vagina saya untuk membantunya melepaskan isi bola ke dalam diri saya."
p "Haaaa ..."
ms "Tubuh Paul akhirnya rileks."
scene bg mila_on_top_of_paul_after_sex_kiss
ms "Aku memeluk kepalanya dan menciumnya dengan penuh gairah."
m "..."
p "..."
m "..."
p "..."
scene bg mila_on_top_of_paul_giggle
m "Itu sangat keren ..."
p "..."
m "..."
p "Anda tidak mengatakan ..."
m "..."
p "..."
m "Paul ..."
p "Ya?"
scene bg mila_on_top_of_paul_after_sex_kiss
m "..."
m "Aku mencintaimu."
scene bg mila_on_top_of_paul_giggle
ms "Paul memelukku erat -erat"
p "..."
m "..."
p "..."
scene bg mila_on_top_of_paul_unsatisfied
m "So... {w}What should I... {w}I mean \"we\"mengerjakan?"
p "..."
m "..."
p "..."
p "Ayo ... __tag_0__Let tidak menghancurkan hatinya ..."
scene bg mila_on_top_of_paul
m "..."
p "Kemudian..."
p "Mari kita lihat apa yang akan terjadi."
m "..."
p "Saya pikir Anda akan tahu apa yang harus dilakukan ..."
p "Lakukan saja hal yang benar ..."
p "I ... __tag_0__i mempercayai niat Anda."
scene bg mila_on_top_of_paul with fade
"__tag_0__. __tag_0__. __tag_0__."




scene bg door
"..."
ms "Keesokan harinya Bob mengetuk pintu dengan lembut."
show mila robe_shhhh_finger
ms "Menyapa dia sambil tersenyum, aku menyerahkan makan siangnya."
show bob surprised at left:
    xzoom 0.9 yzoom 0.9
ms "Dia menatapku dengan bingung."
m "Ambillah. __Tag_0__ Ini untuk Anda."
bob "..."
m "Ambillah, tangan saya akan jatuh."
ms "Bob dengan ragu -ragu menerima tas makanan."
show mila robe_puzzled_frown
m "Jadi…"
bob "..."
show mila robe_puzzled
m "Saya memikirkan kata -kata Anda ..."
show bob waving:
    xzoom 0.9 yzoom 0.9
bob "Anda melakukannya?"
ms "Bob tertawa palsu"
show bob smile:
    xzoom 0.9 yzoom 0.9
bob "Maaf, saya seharusnya tidak mengatakan itu ..."
show mila robe_puzzled_frown
show bob sad2:
    xzoom 0.9 yzoom 0.9
bob "Maksud saya ... _ tag_0__ Saya tahu jawaban Anda ... __tag_0__ dan saya tidak pernah ingin membuat Anda ... __tag_0__ tidak nyaman ..."
ms "Bob menghela nafas"
show mila robe_sad
show bob sad:
    xzoom 0.9 yzoom 0.9
bob "Saya tidak tahu mengapa saya mengatakan itu ..."
ms "Dia menatapku"
bob "Anda seharusnya tidak diganggu dengan itu ... __Tag_0__Si selalu seperti itu ..."
show mila robe_sad_tears
m "..."
m "Kata -katanya membuatku sedih, tapi entah bagaimana, aku berhasil menyatukan diri dan tersenyum."
show mila robe_smile_open_mouth
m "Jangan khawatir, Bob. Tidak apa -apa"
show bob idle:
    xzoom 0.9 yzoom 0.9
ms "Dia tersenyum palsu"
bob "Tentu. __Tag_0__jap kamu bilang begitu ..."
ms "Saya benar -benar merasakan keinginannya untuk pergi secepat mungkin"
show mila robe_blush_shy_looking_aside
m "Tidak apa -apa bob, __tag_0__beCause, __tag_0__i akan menjadi pacarmu"
bob "..."
m "..."
bob "..."
show mila robe_puzzled
m "..."
show bob smile:
    xzoom 0.9 yzoom 0.9
bob "Ahah! Itu lelucon yang lucu!"
ms "Matanya memberitahuku bahwa dia tidak menemukan itu paling tidak lucu sama sekali."
show mila robe_puzzled_frown
m "Saya tidak bercanda. __Tag_0__well ... __tag_0__maybe saya ... __tag_0__kind dari ..."
show mila robe_smile_awkward_open_mouth
m "Ngomong -ngomong, __tag_0__i berarti, __tag_0__i'll __tag_2__pretend__tag_3__ menjadi pacarmu"
show bob sad2:
    xzoom 0.9 yzoom 0.9
bob "Saya tidak suka kemana perginya, jadi saya mungkin harus pergi"
ms "Dia mengerutkan kening dan berbalik untuk pergi"
ms "Saya harus mengambil lengan bajunya untuk menghentikannya"
show mila robe_worried_open_mouth_wait
m "Tunggu!"
bob "..."
show bob sad:
    xzoom 0.9 yzoom 0.9
ms "Dia menatapku dengan mata tumpul"
ms "Saya tidak suka tampilan itu"
ms "Menilai. Gelisah. Bahkan menyakitkan. Untuk kami berdua"
ms "Saya menghela nafas"
show mila robe_think
m "Bob. Dengarkan aku."
ms "Dia tidak menjawab"
ms "Tapi dia tidak mencoba berpaling dari saya juga"
m "..."
ms "Mengapa begitu sulit untuk mengumpulkan pikiran saya?"
m "..."
show mila robe_blush_shy_looking_aside
m "Apakah ... __tag_0__ apakah Anda menyukai saya, Bob?"
bob "..."
ms "Bob mengepalkan giginya dan menatapku dengan rasa sakit di matanya"
show bob frown_dull_eyes:
    xzoom 0.9 yzoom 0.9
bob "Anda ... __tag_0__ Ketahui jawabannya"
show mila robe_smile_awkward_open_mouth
m "Aku tidak ingin menyakitimu, Bob"
m "Aku hanya ..."
ms "Saya mencoba menemukan kata -kata yang tepat ... __tag_0__but saya gagal ..."
show mila robe_puzzled_frown
m "Tanya saja aku, Bob"
bob "..."
m "..."
show bob idle:
    xzoom 0.9 yzoom 0.9
ms "Bob mencibir tapi senyum sedih dan mengangguk"
bob "Tentu ... __tag_0__i akan ... __tag_0__someday."
ms "TIDAK! __Tag_0__ itu bukan yang saya maksud, Anda konyol"
show mila robe_curious
m "MEMBERIKAN SAYA."
show bob sad:
    xzoom 0.9 yzoom 0.9
ms "Bob mengerutkan kening"
bob "Ya, tentu saja, __tag_0__i akan ..."
show mila robe_smile_awkward_angry
m "Bertanya. __Tag_0__me. __Tag_0__out .__ tag_0__"
bob "..."
show bob sad2:
    xzoom 0.9 yzoom 0.9
ms "Bob menghela nafas"
bob "Tapi kamu sudah menikah ..."
show mila robe_smile_awkward_open_mouth
m "Ya Bob, saya. Itulah mengapa itu hanya kepura -puraan"
bob "..."
show mila robe_smile_open_mouth
m "Tapi itu tidak berarti itu tidak ada gunanya"
show mila robe_proud
m "MEMBERIKAN SAYA."
m "Dan lihat sendiri, bahwa saya tidak akan menolak Anda"
bob "..."
show bob frown_dull_eyes:
    xzoom 0.9 yzoom 0.9
bob "Ini tidak benar dan saya tidak menyukainya"
show mila robe_smile_awkward_angry
m "Apakah kamu? __Tag_0__Anda tidak suka berbicara dengan saya? __Tag_0__ Anda tidak ingin berkencan dengan saya?"
bob "..."
show mila robe_curious
m "_ Tag_0__ lebih banyak lagiLihat. __Tag_0__ kamu pria yang baik. __Tag_0__ dan Anda bernilai lebih dari yang Anda pikirkan."
m "Dan saya akan membuktikannya kepada Anda."
show mila robe_grin_thumbs_up
m "As long as you need - I will be your \"girlfriend\""
show mila robe_smile_grin
m "Saya akan memasak untuk Anda, pergi berkencan dengan Anda, berbicara dengan Anda dan hal -hal seperti itu."
show mila robe_smile_open_mouth_excited
m "Dan saya akan membantu Anda mendapatkan kepercayaan diri Anda"
bob "..."
show mila robe_proud
m "Oke?"
bob "Dengan baik..."
ms "Melihat lebih dekat, saya perhatikan bahwa Bob mengenakan T-shirt keriput dengan kerah kotor yang dibalik ke luar."
ms "Saya secara otomatis mencoba memperbaikinya, karena saya selalu melakukannya untuk Paul, ketika dia sedang terburu -buru."
ms "Bob berdiri tak bergerak."
bob "..."
scene bg door
show cg mila_and_bob_hands_on_sholders at center:
    xzoom 0.85 yzoom 0.85
    linear 1.0 ypos 0.85
ms "Aku menatap wajahnya dan, memperhatikan penampilannya yang malu, memalingkan muka."
ms "Dia sangat besar ... dan dia sangat dekat ... Aku merasa sangat muda dan feminin"
ms "Untuk sesaat saya ingat fantasi kemarin ..."
ms "Dan untuk sesaat saya ingin menjadikannya nyata"
ms "Saya menemukan tangan saya masih tergeletak di pundaknya yang lebar dan dengan cepat melangkah sedikit ke belakang"
scene bg door
show bob shy:
    xzoom 0.9 yzoom 0.9
bob "..."
show mila robe_blush_shy_looking_aside
m "..."
ms "Woah ..."
ms "Apa itu?"
show mila robe_puzzled
ms "Mengapa jantungku berdegup kencang?"
ms "Entah bagaimana aku berhasil tenang, tersenyum berani dan menatapnya"
ms "Saya perlu mengatakan sesuatu sebelum menjadi lebih aneh ..."
show mila robe_smile_awkward_open_mouth
m "Jadi?"
bob "..."
show bob surprised:
    xzoom 0.9 yzoom 0.9
bob "Oke ... kurasa ..."
ms "Aku tersenyum padanya dan dia tersenyum mundur"
show mila robe_blush_smirk
m "Itu sudah diselesaikan"
show mila robe_holding_hand_open_mouth_blush
ms "Saya mengulurkan tangan kosong saya"
m "Beri saya kunci apartemen Anda, saya akan membersihkannya dan mencuci pakaian Anda."
m "Saya yakin Anda sudah lama tidak melakukannya."
bob "..."
ms "Bob memalingkan muka dan menggaruk bagian belakang kepalanya."
show bob doubting_scratching_head:
    xzoom 0.9 yzoom 0.9
bob "Erm ..."
show mila robe_holding_hand_open_mouth_brow_up
m "Apa?"
bob "..."
m "..."
bob "..."
show mila robe_holding_hand_open_mouth_blush
m "Dengar, Anda perlu terbiasa dengan gagasan bahwa seseorang ingin melakukan sesuatu yang baik untuk Anda."
show mila robe_holding_hand_open_mouth_blush2
m "Just ... __tag_0__beCause."
bob "..."
m "..."
bob "Saya tidak..."
ms "Saya merasa seperti dia akan menolak proposal saya lagi, jadi saya segera mengganggu dia."
show mila robe_holding_hand_open_mouth_frown
m "Berhentilah berpikir bahwa sesuatu yang buruk mungkin terjadi!"
m "Saya pacar Anda, ingat?"
show mila robe_holding_hand_open_mouth_blush3_looking_aside
m "Dan saya hanya ingin ... __tag_0____tag_1__please__tag_2__ Anda."
ms "..."
show mila robe_blush_smirk
ms "Tunggu ... __tag_0__ itu terdengar agak cabul ..."
ms "..."
ms "Hehe"
bob "..."
show mila robe_holding_hand_open_mouth_blush2
ms "Saya dengan sabar menunggu reaksinya"
ms "..."
show bob idle:
    xzoom 0.9 yzoom 0.9
ms "Bob masih ragu -ragu, tetapi tidak melepas kunci dan meletakkannya di tangan saya."
show mila robe_smile_grin
ms "Saya tersenyum."
m "Bersiaplah untuk terkejut - apartemen Anda akan sebersih sebelumnya!"
show bob smile:
    xzoom 0.9 yzoom 0.9
bob "Tentu ... __tag_0__hehe ..."
bob "Erm…"
ms "Bob menggaruk kepalanya lagi."
show bob shy:
    xzoom 0.9 yzoom 0.9
bob "Hanya saja, jangan membersihkan kamarku ... __tag_0__please"
bob "Di sana ... __tag_0__i akan membersihkannya sendiri ..."
bob "..."
show mila robe_puzzled_frown
m "..."
show mila robe_bow_down
ms "Setelah beberapa saat, saya bergabung dengan telapak tangan saya dan sedikit membungkuk"
m "Mau mu..."
m "..."
m "...menguasai"
show mila robe_blush_smirk
ms "Cabul!"
ms "Bob dengan malu -malu tersenyum dan pergi dengan tergesa -gesa"
show mila robe_smile_open_mouth_excited
ms "Saya melambai di punggungnya dan menutup pintu"
"..."
show mila robe_smile_awkward_open_mouth
m "Yah ... __tag_0__ yang berjalan dengan baik, saya pikir ..."
"..."
show mila robe_curious
m "Apa yang ada di dalam kamarnya, saya bertanya -tanya?"
"__tag_0 __..."


scene bg apartments
ms "Setelah menyelesaikan tugas saya sebelum makan siang, saya akhirnya pergi untuk membersihkan flat Bob"
ms "Saya berharap itu kotor, tetapi ternyata tidak seburuk yang seharusnya."
scene bg bobs_apartments_dirty
play sound "door-open-close.mp3"
ms "Menggulung lengan baju saya, saya mengambil sampah, mengumpulkan pakaian kotor untuk dicuci nanti, dan mengepel lantai."
ms "Aparently Bob tidak memiliki mesin cuci ..."
"..."
show mila casual_sad
ms "Tunggu sebentar ..."
ms "Apa itu?"
ms "Apakah itu semacam jas?"
ms "Bukankah itu agak kecil untuk dipakai Bob?"
ms "Mengapa dia membutuhkannya?"
ms "Saya menciumnya"
show mila casual_disgust_covered_nose
ms "Eugh ... bau ..."
ms "Perlu dicuci saat itu"
show mila casual_proud
ms "Setelah beberapa jam flat menjadi jauh lebih bersih."
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
scene bg bobs_apartments_clean with flash
show mila casual_proud
"..."
ms "Ketika pembersihan selesai, saya tidak bisa menahan diri dan pergi ke pintu kamar tidur Bob."
scene bg closed_door
show mila casual_skeptic at right:
    ypos 1.2
ms "..."
ms "Dia secara khusus meminta saya untuk tidak masuk ke dalam ..."
ms "Hmmm ..."
show screen nts_stats_overlay
menu:
    "Haruskah saya membukanya?"
    "Lebih mudah untuk meminta pengampunan daripada meminta izin ... (dominasi Mila + 1)":
        $ mila_dom += 1
        $ mila_was_in_the_room = True
        jump bob_door_opened
    "Beberapa pintu harus tetap tertutup ...":

        jump bob_door_not_opened

label bob_door_opened:
show mila casual_worried
ms "Saya tidak bisa menahan diri ... saya perlu tahu"
hide screen nts_stats_overlay
play sound "creak.mp3"
scene bg bobs_room
ms "Pintu terbuka dengan derit yang tenang"
ms "Saya tahu tidak ada seorang pun di ruangan itu, __tag_0__but untuk beberapa alasan saya membeku dan melihat sekeliling"
m "..."
show mila casual_relieved
m "Ayo Mila ..."
m "Anda tidak melakukan sesuatu yang ilegal ..."
ms "Saya melihat ke dalam"
ms "Tempat sampah di sebelah komputer diisi dengan serbet bekas. __Tag_0__ Udara basi berbau samar -samar dari sperma dan keringat. __Tag_0__i menutupi hidung saya."
show mila casual_disgust_covered_nose
m "Ugh ..."
ms "Di atas meja ada komputer yang dimatikan dan foto berbingkai."
ms "Saya melihatnya lebih dekat"
show cg selfie_in_a_frame at left:
    yzoom 0.7 xzoom 0.7
    linear 0.6 ypos 0.8
show mila casual_worried
m "Dia mencetak selfie itu, hah ..."
m "..."
m "..."
show mila casual_sad
ms "Entah bagaimana itu menyedihkan ..."
ms "Saya tidak tahan dan berpaling"
play sound "creak.mp3"
scene bg closed_door
ms "..."
ms "..."
m "Saya kira saya benar -benar seharusnya tidak membuka pintu ..."
m "..."
show mila casual_interested_blush
m "Tetapi..."
m "Dia banyak masturbasi ..."
m "..."
m "Apa yang dia impikan, aku bertanya -tanya?"
m "..."
m "..."
m "Pokoknya ... saya sudah selesai. __Tag_0__i harus pulang sekarang."
jump maid1_continue

label bob_door_not_opened:
show mila casual_proud
m "Tidak ... __tag_0__i seharusnya tidak pergi ke sana. Dia memintaku untuk tidak ..."
m "..."
hide screen nts_stats_overlay
show mila casual_worried
ms "Tapi ... __tag_0__ Batasan ini membuat saya dalam suasana hati ..."
ms "Untuk sedikit kerusakan. .."
show mila casual_thinking
m "Hmmm ..."
ms "Apa yang harus saya lakukan?"
show mila casual_interested_blush
ms "Mungkin sedikit menggodanya?"
ms "Saya berdiri di tengah -tengah apartemen yang rapi dan mengambil selfie."
play sound "shot.mp3"
"..."
show cg maid1_selfie_casual:
    yzoom 0.9 xzoom 0.9
m "Hmmm…"
ms "Ada sesuatu yang hilang…"
ms "Saya melepas bra saya dan menyesuaikan kaus saya."
play sound "shot.mp3"
"..."
show cg maid1_selfie_casual_pokies_v_grin_blush:
    yzoom 0.9 xzoom 0.9
ms "Hehe."
ms "Itu lebih baik."
ma "__Tag_0__"
ms "Saya mengirim foto itu ke Bob dan menunggu tanggapannya dengan tidak sabar."
show mila casual_hand_in_pants_heavy_breathing
ms "Ketika saya memperhatikan bahwa dia telah membaca pesan saya, saya tidak bisa menahan diri dan meletakkan tangan saya di celana dalam saya."
ms "Vagina saya adalah jus yang mengalir"
m "Ayo pacar tersayang ..."
m "Katakan sesuatu ..."
show mila casual_hand_in_pants_biting_lips
m "..."
bob_message "Terima kasih"
ms "..."
show mila casual_laugh
ms "Hehe."
ms "Betapa keringnya."
m "..."
show mila casual_smile
ms "Jawabannya semacam menghancurkan suasana hati. Saya merasa lebih gembira dari terangsang"
ms "Jadi saya terkikik dan berpikir bahwa akan lebih lucu untuk menggodanya lebih banyak"
ma "Sudahkah Anda berubah pikiran tentang kamar Anda? Saya bisa membersihkannya juga, Anda tahu?"
ms "Jawabannya datang hampir seketika"
bob_message "TIDAK!"
show mila casual_laugh
ms "Ahah."
ma "Bagus."
"..."
show mila casual_thinking
ms "Tetap saja, apa yang ada di dalam kamarnya?"
ms "Saya melihat pintu tertutup untuk terakhir kalinya dan meninggalkan apartemen Bob"
"..."




label maid1_continue:
scene bg apartments
"__tag_0 __..."
ms "Keesokan harinya, Bob dengan malu -malu mengucapkan terima kasih atas makan siang dan pembersihannya."
ms "Tetapi setiap hari ia menjadi lebih suram dan suram."
ms "Seminggu kemudian dia tidak datang sama sekali."
ms "Aku mengetuk pintunya, tetapi tidak ada yang membukanya."
scene bg bobs_apartments_clean
play sound "door-open-close.mp3"
ms "Ketika saya membuka pintu dengan kunci, ternyata dia sudah pergi."
show mila robe_puzzled_frown
m "..."
m "Apa? .."
ms "Saya masih menyimpan bagian dari kesepakatan saya - moped lantai dan merapikan ruangan."
show mila robe_puzzled
ms "Beberapa kali saya mengambil telepon saya dan mencoba mengirim pesan kepada Bob"
ms "Tapi tidak bisa memilih kata -kata yang tepat"
"..."
show mila robe_think
m "Haaa ..."
ms "Dengan jiwa yang berat saya kembali ke rumah"
scene bg apartments
play sound "door-open-close.mp3"
ms "Di malam hari, ketika saya mendengar bahwa Bob telah kembali ke rumah, saya datang kepadanya."
scene bg doors
show mila robe_puzzled_frown
m "..."
show bob sad2:
    xzoom 0.9 yzoom 0.9
ms "Bob membuka pintu tetapi bahkan tidak menatapku."
ms "..."
show mila robe_smile_awkward_open_mouth
m "..."
m "Bob?"
show bob sad:
    xzoom 0.9 yzoom 0.9
bob "..."
bob "Selamat malam…"
m "..."
show mila robe_worried_open_mouth_wait
m "Ya, hai. Apa yang telah terjadi?"
show bob doubting_scratching_head:
    xzoom 0.9 yzoom 0.9
bob "..."
bob "..."
ms "Bob tidak menjawab."
ms "..."
show mila robe_sad
m "Bob? Apakah saya entah bagaimana menyakiti Anda?"
bob "..."
ms "Bob menggelengkan kepalanya dan menghela nafas."
show bob sad:
    xzoom 0.9 yzoom 0.9
bob "Tidak ... __tag_0__i ..."
bob "Baik ...__ tag_0__ pertama -tama, __tag_0__ terima kasih ..."
show mila robe_sad_tears
ms "Saya mengangguk. Meskipun dia tidak menatapku dan hampir tidak melihat flat yang bersih."
ms "Untuk beberapa alasan saya merasa tidak enak ... __tag_0__ perasaan pahit yang menjijikkan menggaruk saya di dalam"
ms "Saya tertelan, mencoba menyingkirkannya"
ms "Itu tidak membantu"
show bob frown_dull_eyes:
    xzoom 0.9 yzoom 0.9
bob "..."
bob "Saya pikir sudah waktunya berhenti ..."
m "..."
m "..."
show mila robe_sad_tears_open_mouth
m "Mengapa?"
show mila robe_sad_tears
ms "Suaraku pecah"
ms "Bob dengan cepat menatapku tapi segera berbalik"
bob "..."
show bob sad:
    xzoom 0.9 yzoom 0.9
bob "Ini ...__ tag_0__ itu tidak nyata ..."
bob "Tapi ...__ tag_0__ melelahkan ..."
bob "..."
bob "Dan ...__ tag_0__ semakin lama berlangsung ..."
bob "Semakin menyakitkan menjadi ..."
show mila robe_sad_tears_open_mouth
m "..."
m "Bob…"
show mila robe_sad_tears
show bob frown_dull_eyes:
    xzoom 0.9 yzoom 0.9
bob "..."
ms "Dia menatapku kosong ..."
ms "Saya mengambil tangannya."
show mila robe_sad_tears_open_mouth
m "Dan apa yang nyata?"
bob "..."
show mila robe_puzzled_frown
m "Bisakah Anda merasakan sentuhan saya?"
ms "Dia tidak bereaksi."
ms "Sesuatu di dalam diriku retak"
ms "Saya tidak bisa melihatnya menderita lagi"
ms "Mengikuti dorongan tiba -tiba saya berdiri di atas berjinjit, meraih lehernya dan menekan bibir saya ke bibirnya"
scene cg mila_kiss_bob with flash
ms "Saya merasakan rasa air mata saya yang asin dan sedikit rasa tembakau"
ms "Bibirnya sangat lembut dan besar ..."
ms "Dia berdiri di sana, membeku, dan aku tidak yakin dia menyukainya atau tidak ..."
ms "Setelah beberapa detik yang sangat lama saya menarik diri"
scene bg doors
show mila robe_blush_shy_looking_aside
show bob surprised:
    xzoom 0.9 yzoom 0.9
bob "..."
m "..."
bob "..."
m "..."
show mila robe_sad_tears_open_mouth
m "Bagaimana dengan itu?"
bob "..."
ms "Hidup muncul di matanya lagi."
ms "Dia menatapku dengan terkejut."
bob "..."
show mila robe_blush_shy_looking_aside
m "Apakah ini juga tidak nyata?"
bob "..."
show bob sad2:
    xzoom 0.9 yzoom 0.9
bob "Saya ... __tag_0__i tidak tahu harus berpikir apa ... __tag_0__ dan saya tidak tahu bagaimana menjawab."
ms "Aku melangkah lebih dekat dan menatap matanya"
ms "Dia tampak seperti rusa yang ketakutan"
show mila robe_smile_awkward_angry
ms "Dia masih tidak percaya padaku"
ms "Dia masih ingin melarikan diri"
ms "..."
show mila robe_proud
ms "Tapi aku tidak akan membiarkanmu melakukan itu"
ms "Saya tersenyum dan menyeka air mata saya"
show mila robe_blush_smirk
m "Aku menyukaimu, Bob"
show bob surprised:
    xzoom 0.9 yzoom 0.9
bob "..."
show mila robe_smile_open_mouth
m "Jika saya belum menikah, Anda akan memiliki peluang besar dengan saya."
bob "..."
show mila robe_shhhh_finger
m "Kalau saja Anda bisa menjadi lebih percaya diri ..."
m "Maka kemungkinan besar Anda akan menemukan diri Anda wanita yang layak."
bob "..."
show bob sad:
    xzoom 0.9 yzoom 0.9
show mila robe_puzzled_frown
ms "Bob menatapku dengan rasa sakit."
bob "Saya ... __tag_0__ Saya tidak ingin orang lain lagi."
m "..."
bob "..."
show mila robe_smile_awkward_angry
ms "Dan bagaimana saya harus menjawabnya?"
ms "..."
ms "Sialan ..."
ms "Fuck fuck"
show mila robe_think
ms "Pikirkan, Mila ... __tag_0__think"
m "..."
ms "Jeda diseret bersama"
ms "Bob menghela nafas dan tersenyum sedih"
show bob frown_dull_eyes:
    xzoom 0.9 yzoom 0.9
bob "Bisakah Anda __tag_0__Leave saya sendiri?"
ms "Saya tersentak"
show mila robe_puzzled_frown
bob "SAYA…"
bob "Saya khawatir saya akan mengatakan sesuatu ... __tag_0__ bahwa saya akan menyesal mengatakan nanti."
bob "..."
m "..."
show mila robe_curious
m "Haaa ..."
ms "Tiba -tiba saya merasa sangat lelah dengan segalanya."
ms "Kesulitan emosional juga bisa melelahkan"
show mila robe_irritated_open_mouth
m "Anda tahu apa?"
m "Bagus. __Tag_0__i akan pergi."
show bob sad:
    xzoom 0.9 yzoom 0.9
bob "..."
ms "Bob terkekeh"
ms "Saya mengabaikan reaksinya"
m "Tapi besok Anda akan menjemput saya setelah bekerja"
m "Dan kami akan pergi berkencan"
show bob surprised:
    xzoom 0.9 yzoom 0.9
bob "Tetapi..."
show mila robe_iritated_atatata
m "Atatata"
m "Tidak ada tetapi."
show mila robe_irritated_open_mouth
m "Aku mendengarmu. __Tag_0__i menyakitimu, __tag_0__blah bla bla"
m "Tetapi. __Tag_0__ Anda juga menyakiti saya. __Tag_0__ seperti sekarang"
m "Mengapa saya harus menanggungnya? __ tag_0__ Saya bisa melarikan diri juga .__ tag_0__ berpura -pura bahwa saya tidak mengenal Anda .__ tag_0__ yang tidak saya pedulikan."
m "Tapi saya tidak akan."
m "Karena saya peduli .__ tag_0__ saya tahu Anda .__ tag_0__ dan saya menyukai Anda."
m "Sebaliknya, __tag_0__ Anda tahu apa yang akan saya lakukan? __Tag_0__i akan menghadapinya"
m "Tidak ada cara untuk berkomitmen pada hubungan dan tidak merasakan sakit sama sekali"
m "Anda akan menyakiti saya .__ tag_0__ Saya akan menyakiti Anda .__ tag_0__ tetapi rasa sakit bukan satu -satunya hal yang mungkin kita alami."
m "Saya tidak takut terluka. __Tag_0__ itu lebih baik daripada tidak merasakan apa -apa sama sekali, bukan?"
show bob frown_dull_eyes:
    xzoom 0.9 yzoom 0.9
bob "..."
m "Jadi kumpulkan kotoran Anda, dan perlakukan saya untuk makan enak .__ tag_0__ atau sesuatu .__ tag_0__ Sebenarnya saya tidak peduli; Mari kita bersenang -senang."
bob "..."
m "Oke?"
ms "Bob tidak menjawab. Dia berdiri di sana dan menatapku seolah aku hantu"
m "Oke. Besok. Malam. Selamat tinggal."
scene bg door
play sound "door-open-close.mp3"
show mila robe_sad_tears
ms "Saya menutup pintu, dan baru pada saat itu saya merasa bahwa saya tidak memiliki kekuatan untuk berdiri dan menahan air mata saya."
ms "Argumen tidak pernah menjadi setelan kuat saya, lagipula ..."




scene bg apartments
hide mila
show cg mila_hugging_knees at center:
    xzoom 0.9 yzoom 0.9 ypos 0.9
ms "Saya tidak punya waktu untuk pulih sebelum Paul kembali ke rumah."
ms "Dia menemukan saya duduk di tempat tidur, memeluk lutut saya."
p "..."
p "Sayang? Apa yang telah terjadi? Apakah kamu terluka?"
ms "Saya tidak bisa menjawab dengan benar, dan hanya menangis."
ms "Paul memelukku dan memberiku waktu untuk mengumpulkan pikiranku."

show cg mila_paul_hug at center:
    ypos 1.8
    linear 5.0 ypos 1.1
ms "Kehadirannya selalu memiliki efek menenangkan pada saya."
ms "Beberapa menit kemudian saya akhirnya bisa menarik diri dan memberitahunya apa yang terjadi."
hide cg
show paul suit_open_mouth_neutral at left
m "..."
p "Apakah Anda merasa lebih baik?"
show mila robe_blush_shy_looking_aside at right
ms "Saya mengangguk"
p "..."
m "..."
show paul suit_sad
p "..."
p "Bisakah saya benar -benar jujur dengan Anda?"
show mila robe_puzzled_frown
ms "..."
ms "Untuk beberapa alasan, nadanya tampak menakutkan bagi saya. Aku mengangguk rajin, berusaha untuk tidak membayangkan banyak hal."
m "Tentu..."
p "..."
show paul suit_frown
p "Saya sangat khawatir tentang Bob ...__ tag_0__ tetapi begitu Anda mengatakan Anda menciumnya, saya tidak bisa memikirkan hal lain ..."
m "..."
m "..."
show mila robe_sad
ms "Telapak tangan saya langsung menjadi berkeringat."
ms "Aku menelan dengan gugup."
show mila robe_curious
m "Anda ...__ tag_0__ Apakah Anda ingin menghentikan semua ini?"
p "..."
show mila robe_sad
ms "Paul diam, tenggelam dalam pikirannya."
m "..."
ms "Dalam percakapan dengan Bob, saya menyerah pada emosi."
ms "Tapi sekarang pikiran yang berbeda mengerumuni kepalaku."
ms "Saya menyesal bahwa saya melakukannya dan mencoba membenarkan diri saya."
ms "Saya marah pada Paul dan, pada saat yang sama, berjuang dengan keinginan untuk mulai berdoa untuk pengampunan."
ms "Saya yakin hanya satu."
show mila robe_sad_tears
ms "Saya tidak ingin hubungan saya dengan Paul putus."
ms "Saya menyadari bahwa saya bisa memikirkan Bob dan memanjakan diri saya hanya jika semuanya baik -baik saja di rumah."
ms "Jika Paul senang ..."
m "..."
show mila robe_sad_tears_open_mouth
m "Paul?"
show mila robe_sad_tears
show paul suit_open_mouth_neutral
p "Ah? Maaf, apa yang kamu katakan?"
m "..."
show mila robe_sad_tears_open_mouth
m "Saya bertanya apakah Anda ingin ... menghentikan semua ini?"
show mila robe_sad_tears
p "..."
show paul suit_shock
ms "Paul menatapku dengan terkejut."
p "Tidak, kenapa kamu bertanya?"
m "..."
show mila robe_sad_tears_open_mouth
m "Saya pikir Anda marah pada saya ..."
show mila robe_sad_tears
p "..."
p "Oh..."
show paul suit_grin
p "Ahah .__ tag_0__ Tidak. Semuanya baik -baik saja!"
show paul suit_open_mouth_blush
p "Aku hanya ...__ tag_0__ aku mencoba membayangkan ciumanmu ..."
show paul suit_blush_looking_aside
show mila robe_smile_awkward_open_mouth:
    easein 1 xpos 0.8
m "..."
m "Oh ...__ tag_0__uhm ...__ tag_0__ dan bagaimana menurut Anda?"
p "..."
show paul suit_open_mouth_blush
p "Bahwa itu pasti sangat seksi ..."
show paul suit_blush_looking_aside
ms "Semua kekhawatiran saya menghilang seolah -olah dengan gelombang tongkat ajaib."
show mila robe_smile_grin
ms "Saya tersenyum."
m "Anda pikir?"
show paul suit_grin
p "Ya ...__ tag_0__ Tapi apa yang pasti - saya tersinggung bahwa saya tidak melihatnya."
show mila robe_blush_smirk:
    easein 1 xpos 0.6
m "Heh ...__ tag_0__ apakah Anda ingin saya mengambil foto lain kali?"
p "..."
show paul suit_sad
ms "Paul menatapku dengan tatapan tajam."
show mila robe_blush_shy_looking_aside
ms "Saya merasa ngeri, tetapi tidak memalingkan muka."
p "..."
show paul suit_grin
p "Lain kali, ya?"
show mila robe_blush_smirk
m "..."
show paul suit_open_mouth_blush
p "Ya. Saya menginginkannya"
show paul suit_blush_looking_aside
m "..."
p "..."
show mila robe_puzzled
m "Paul ..."
show paul suit_open_mouth_neutral
p "?"
m "..."
show mila robe_puzzled_frown
m "Anda tidak keberatan bahwa kami akan berkencan?"
show paul suit_blush_looking_aside
p "..."
show paul suit_open_mouth_blush
p "Saya kira ...__ tag_0__ saya masih merasa seksi."
show mila robe_shhhh_finger
p "Saya tidak tahu mengapa."
p "Dan saya cukup yakin, bahwa saya tidak ingin tahu alasannya."
show paul suit_blush_looking_aside
m "..."
p "..."
show paul suit_sad
p "Just ...__ tag_0__ Jangan mengkhianati kepercayaan saya ..."
show mila robe_worried_open_mouth_wait
m "Saya tidak akan pernah!"
p "Saya tahu .__ tag_0__ dan tetap saja. Hanya ...__ tag_0__ tidak."
show mila robe_puzzled_frown
m "..."
hide paul
show mila robe_puzzled_frown at center
ms "Aku menatapnya dan tatapannya membuatku menggigil."
ms "Tapak kepercayaan antara kita ini terus merentang di bawah tekanan tindakan kita."
ms "Dan kami terus menariknya dalam upaya untuk merobeknya."
ms "Tapi kami selalu berhenti pada saat terakhir. Yang baru saja membuat tapak lebih kuat."
ms "Saya tidak ingin membuat Paul menderita."
ms "Saya ingin buktinya .__ tag_0__ kekuatan .__ tag_0__ Saya ingin perasaannya .__ tag_0__ semuanya."
ms "Saya ingin mengirimkan kepadanya .__ tag_0__ untuk menunjukkan kepadanya, bahwa apa pun yang terjadi dengan kami ...__ tag_0__ apa pun yang kami lakukan sendiri ...__ tag_0__ hatiku adalah propertinya."
ms "Dan tidak ada apa -apa, __ tag_0__ secara harfiah tidak ada, __ tag_0__ yang bisa memisahkan kita."
m "..."
show mila robe_smile_awkward_open_mouth
m "Apakah Anda ingin memberikan instruksi?"
show screen nts_stats_overlay
menu:
    "Apa yang harus disarankan Paul?"
    "Biarkan dia menyentuh pantatmu (kepatuhan Mila + 1)":
        $ dom += 1
        $ paul_touch_ass = True
        jump netorase1_choice1
    "Lakukan apa yang menurut Anda benar (dominasi Mila + 1)":
        $ mila_dom += 1
        jump netorase1_choice2

label netorase1_choice1:
show mila robe_blush_shy_looking_aside
ms "Darah bergegas ke pipi saya, dan saya merasa wajah saya menjadi merah."
m "..."
hide screen nts_stats_overlay
show mila robe_puzzled
m "Anda yakin?"
show paul suit_open_mouth_neutral at left
p "Ya."
show paul suit_grin
ms "Paul tersenyum padaku. Dia menjawab tanpa ragu -ragu."
m "..."
show mila robe_puzzled_frown
m "Tapi Anda tidak akan bisa menonton ..."
p "..."
p "Itulah mengapa saya ingin mendengar semua detail yang menarik sesudahnya."
m "..."
show mila robe_blush_smirk
m "..."
m "Bagus. Saya akan melihat apa yang bisa saya lakukan."
p "..."
show paul suit_smirk
ms "Paul entah bagaimana tersenyum nakal."
p "Itu gadisku."
p "..."
ms "Saya tidak akan berbohong. Saya menyukai reaksinya."
"..."
jump netorase1_continue

label netorase1_choice2:
show paul suit_blush_looking_aside at left
show mila robe_puzzled_frown
ms "Paul tetap diam .__ tag_0__ jadi saya pikir akan benar untuk menyarankan sesuatu."
hide screen nts_stats_overlay
show mila robe_blush_smirk
m "..."
m "Tidak ada apa-apa? Saya pikir saya hanya akan menghisapnya kalau begitu ..."
show paul suit_extremely_shocked
p "!!!"
ms "Paul menatapku dengan tak percaya."
show mila robe_shhhh_finger:
    easein 1 xpos 0.4
m "Anda tidak suka idenya?"
p "..."
show paul suit_blush_looking_aside
ms "Paul mengerti, bahwa saya bercanda dan menjadi malu dengan reaksinya."
ms "Saya tidak bisa menahannya .__ tag_0__ Saya ingin menggodanya lebih banyak."
show mila robe_blush_smirk:
    easein 1 xpos 0.3
m "Anda sepertinya menyukainya sebelumnya? Apa yang telah terjadi?"
p "..."
ms "Paul tidak menjawab."
show mila robe_shhhh_finger
m "Hehe .__ tag_0__ lalu ...__ tag_0__ Mungkin saya harus menyentuhnya?"
p "..."
ms "Paul tersenyum padaku dengan hati -hati."
ms "Aku tersenyum padanya."
m "..."
show mila robe_proud
m "Jadi? Bagaimana menurutmu?"
p "..."
show paul suit_open_mouth_blush
p "Saya pikir Anda bisa menggosoknya ... __Tag_0__Through pakaiannya ..."
show paul suit_blush_looking_aside
ms "Saya menggosok tonjolan Paul."
show mila robe_blush_smirk
m "Seperti ini?"
p "..."
show paul suit_open_mouth_blush
p "Ya..."
show paul suit_blush_looking_aside
show mila robe_smile_grin
m "Hehe ..."
m "Dengan baik..."
m "Saya melihat apa yang bisa saya lakukan ..."
p "..."

label netorase1_continue:
"__tag_0 __..."
scene bg bedroom
ms "Saya takut bahwa saya tidak akan tertidur karena pikiran saya."
ms "Tapi ternyata saya sangat kelelahan sehingga saya tertidur segera setelah kepala saya menyentuh bantal."





n "__tag_0__. __tag_0__. __tag_0__."
scene bg apartments
ms "Hari berlalu dengan gembira."
ms "Saya mencoba terganggu dengan membersihkan dan memasak, tetapi pemikiran saya tentang tanggal yang akan datang tidak hilang."
show mila robe_think
m "..."
m "Saya seperti seorang siswi sebelum kencan pertamanya, apa masalahnya?"
m "..."
show mila robe_smile_awkward_open_mouth
ms "Ketika waktu mendekati enam, saya mulai bersiap."
ms "Awalnya saya ingin berdandan ... tetapi pada akhirnya saya memutuskan untuk tidak berlebihan."
show mila robe_untied
ms "Saya tidak ingin membuat Bob semakin gugup."
n "..."
show mila jeans_and_blouse_front
n "..."
ms "Bob datang segera setelah bekerja."
ms "Meskipun saya mendengar dia menginjak -injak kekuatan pengumpulan pintu. Saya memutuskan untuk tidak terburu -buru."
ms "Akhirnya dia mengetuk."
show mila jeans_and_blouse_waving at right
m "..."
show bob idle at left:
    xzoom 0.8 yzoom 0.8
bob "..."
show mila jeans_and_blouse_remorse
m "..."
m "Bob ..."
bob "Halo..."
show mila jeans_and_blouse_angry_open
m "Ya, hai ...__ tag_0__ apa yang Anda kenakan?"
show mila jeans_and_blouse_angry_close
show bob doubting_scratching_head
bob "..."
bob "..."
bob "Pakaian biasa saya!"
m "..."
show mila jeans_and_blouse_angry_open
m "Benar."
show mila jeans_and_blouse_angry_close
show bob frown_dull_eyes
bob "..."
bob "Saya seharusnya datang dengan pakaian kerja?"
show mila jeans_and_blouse_remorse
m "..."
m "Haaaa ..."
m "Ayo pergi."
play sound "door-open-close.mp3"
scene bg doors
show bob doubting_scratching_head at left:
    xzoom 0.8 yzoom 0.8
bob "..."
bob "Oh, oke ..."
show bob idle
ms "Bob melangkah mundur dan mengikuti saya dari belakang."
show mila jeans_and_blouse_back
ms "Pada awalnya, saya ingin mengganggu dia karena dia tidak memuji penampilan saya dan pergi berkencan di kainnya yang biasa ..."
ms "Tapi kemudian saya ingat bahwa ini adalah kencan pertamanya. Saya seharusnya tidak berharap terlalu banyak darinya."
m "Bob ..."
show bob frown_dull_eyes
bob "Ya?"
m "..."
m "Jika Anda menyukai pemandangan dari belakang, maka saya tidak keberatan."
show bob surprised
bob "!"
m "Tetapi secara umum, pasangan biasanya berjalan dekat dengan kencan."
show bob frown_dull_eyes
bob "S-Sorry ..."
m "Bob menyusul saya dalam dua langkah dan mencoba menjaga langkah kami."
show mila jeans_and_blouse_run_smile
m "..."
n "__tag_0__. __tag_0__. __tag_0__."
scene mall
ms "Ketika kami memasuki mal, Bob mulai ketinggalan lagi."
ms "Aku harus meraih lengannya untuk tidak melupakannya."
show mila jeans_and_blouse_serious_open_mouth at center
m "..."
m "Kenapa kamu begitu takut?"
show bob sad at left:
    xzoom 0.8 yzoom 0.8
ms "Bob mengerutkan kening."
bob "Saya tidak takut ... __tag_0__ itu hanya ... __tag_0__people menemukan saya tidak menyenangkan."
bob "Oleh karena itu, saya mencoba untuk tidak menemukan siapa pun ..."
show mila jeans_and_blouse_sad_looking_aside
ms "Saya tidak tahu bagaimana menjawab."
show bob frown_dull_eyes
bob "Anda tidak pernah mengalami tampilan jijik yang tidak menyenangkan."
bob "Karena itu, saya tidak menyembunyikan diri untuk kesenangan mereka ... __tag_0__i melakukannya untuk diri saya sendiri."
bob "Saya tidak melihatnya dan tetap berprofil rendah, untuk menghindari menarik perhatian."
bob "Dan agar tidak merasa lebih buruk dari yang sudah saya lakukan ..."
show mila jeans_and_blouse_sad_looking_up
m "..."
m "Maaf..."
show bob sad
ms "Bob tersenyum sedih."
bob "Tidak apa-apa..."
m "..."
show mila jeans_and_blouse_sad_looking_down
m "Bagaimana dengan saya?"
show bob surprised
ms "Bob menatapku dengan terkejut."
show mila jeans_and_blouse_sad_looking_up
m "Apakah saya juga melihat Anda dengan jijik?"
bob "..."
show bob sad
bob "TIDAK..."
show mila jeans_and_blouse_serious_open_mouth
m "Maka jangan lihat mereka .__ tag_0__ Lihatlah saya."
bob "..."
show mila jeans_and_blouse_front
m "..."
bob "..."
show bob idle
ms "Bob tersenyum."
bob "Oke."
ms "Aku sedikit meremas tangannya dan tersenyum."
m "Bagus."
show mila jeans_and_blouse_waving
m "Sekarang kami akan pergi ke toko dan melihat beberapa pakaian untuk Anda ..."
"..."
scene changing room
ms "Bob menggerutu saat aku memilih pakaian untuknya."
ms "Setelah beberapa waktu saya menjawabnya, tetapi setelah beberapa saat saya mulai mengabaikannya."
ms "Bob mengerutkan kening, tetapi berhenti menggerutu."
"..."
"???" "Apakah Anda membutuhkan bantuan untuk membuat pilihan?"
ms "Seorang gadis konsultan mendekati saya."
ms "Saya ingin menolak pada awalnya, tetapi kemudian saya menyadari bahwa saya telah berkeliaran di sekitar toko selama setengah jam dan tidak dapat menemukan apa yang saya inginkan."
show mila jeans_and_blouse_run_smile
m "Ya, saya pikir begitu. __Tag_0__bob, tolong datang ke sini."
show bob frown_dull_eyes at left:
    xzoom 0.8 yzoom 0.8
bob "..."
bob "Bob yang patuh datang lebih dekat dan berdiri di sampingku, berusaha untuk tidak memenuhi tatapan wiraniaga itu."
ms "Gadis itu menatapnya dengan pandangan cepat dan tersenyum sopan, tapi aku jelas merasakan apa yang dibicarakan Bob."
ms "Dia memancarkan permusuhan, dan aku benar -benar bisa merasakannya, bahkan ketika dia menyembunyikannya di balik senyum."
show mila jeans_and_blouse_remorse
m "..."
m "Aku ingin tahu apa yang dia lakukan padanya? Bob dikelilingi oleh beberapa aura yang memaksa orang lain untuk membencinya."
bob "..."
"???" "Apakah Anda mencoba memilih pakaian untuk ... ayah Anda? Apa kesempatannya?"
show mila jeans_and_blouse_angry_close
ms "Reaksinya karena beberapa alasan membuat saya keluar dari kebiasaan itu dan membuat saya marah."
show mila jeans_and_blouse_angry_open
m "Dia adalah pacarku."
show mila jeans_and_blouse_angry_close
ms "Untuk sesaat, jijik penjual bocor ke wajahnya. Dan kali ini diserahkan kepada saya."
ms "Saya bertemu tatapannya, siap mengatur skandal jika dia berperilaku tidak tepat."
m "..."
ms "Tapi ternyata dia merasakan tekad saya dan menurunkan matanya."
"???" "Saya minta maaf, saya tidak bermaksud membuat Anda kesal."
m "..."
show mila jeans_and_blouse_proud
ms "Saya menatap Bob dan membaca rasa terima kasih di matanya."
ms "Heh."
show mila jeans_and_blouse_smile_wink
ms "Itu dia."
"..."
"..."



ms "Kami menghabiskan lebih dari satu jam untuk mencoba pakaian yang berbeda. __Tag_0__judging oleh wajah Bob, dia menyesal setuju untuk pergi bersamaku pada tanggal sekitar 10 menit kemudian."
ms "Tetapi pada akhirnya, itu sepadan."
show mila jeans_and_blouse_run_smile at center
"..."
"..."
show bob suit_sceptic at left:
    xzoom 0.8 yzoom 0.8
m "Sepertinya saya ini adalah pilihan kami."
show bob suit_happy
ms "Bob Shone."
bob "Itu sudah selesai? Bisakah kita pergi sekarang?"
show mila jeans_and_blouse_serious_open_mouth
ms "Aku memutar mataku."
ms "Bagus bahwa Paul sendiri terlibat dalam pakaiannya ..."
"..."
scene mall
ms "Kami membayar pakaian dan meninggalkan toko."
ms "Bob, dilihat dari wajahnya, tidak puas dengan hobi kami"
show mila jeans_and_blouse_run_smile
m "Nah, apa selanjutnya?"
show bob suit_sceptic at left:
    xzoom 0.8 yzoom 0.8
bob "..."
bob "Sebut saja sehari?"
show mila jeans_and_blouse_surprise
m "..."
m "Tidak."
show bob suit_awkward_smile
ms "Bob menghela nafas, tetapi memperhatikan tatapan saya yang tidak senang tersenyum."
show mila jeans_and_blouse_haaaa_tired_irritated
m "..."
m "Haaaa ..."
show mila jeans_and_blouse_angry_open
m "Bob, apakah Anda tidak puas dengan sesuatu?"
show bob suit_sceptic
bob "..."
ms "Bob tidak mengatakan apa -apa."
m "Anda berkencan dengan seorang gadis yang dua puluh tahun lebih muda dari Anda."
m "Saya membantu Anda memilih jas dan memasak untuk Anda"
show mila jeans_and_blouse_angry_disgust_open
m "Saya bisa bersantai di rumah atau melakukan sesuatu yang lain sekarang, tetapi tidak - saya menghabiskan waktu pribadi dengan Anda."
m "Jadi saya tertarik: apakah Anda tidak puas dengan sesuatu?"
show mila jeans_and_blouse_angry_close
ms "Bob sekaligus bergumam."
show bob suit_frown_open_mouth
bob "Saya tidak memaksa Anda untuk ikut dengan saya."
ms "Nada suaranya lebih berarti daripada kesal."
bob "Saya tidak membutuhkan kasihan Anda. _ TAG_0__ Anda di tempat pertama yang memprakarsai semua ini ... _ tag_0__ lelucon."
show bob suit_sceptic
show mila jeans_and_blouse_remorse
m "..."
ms "Saya hampir membentaknya, tetapi menahan diri."
ms "Saya ingin bersenang -senang, bukan pertengkaran."
show mila jeans_and_blouse_surprise
m "..."
ms "Tapi sekarang jelas mengapa dia tidak punya pacar."
m "..."
ms "Kita harus membantunya untuk berperilaku."
show mila jeans_and_blouse_serious_open_mouth
m "Lelucon, katamu ..."
ms "Merasakan kekesalan saya, Bob menyusut kembali dan tidak mengatakan apa -apa."
show mila jeans_and_blouse_angry_open
m "Saya melihat bahwa Anda tidak puas. __Tag_0__ Anda tidak suka saya membantu Anda dengan pakaian, __tag_0__ Anda tidak suka saya memasak untuk Anda, __ tag_0__ Anda tidak suka bahwa saya setuju untuk menjadi pacar Anda."
m "Berapa banyak lapisan baju besi Anda yang perlu saya atasi untuk akhirnya sampai ke bob, yang puas dengan setidaknya satu hal?"
m "Yang saya dapatkan dari Anda adalah cemberut dan kerutan Anda."
show mila jeans_and_blouse_angry_close
show bob suit_frown_open_mouth
bob "..."
ms "Bob membuka mulutnya untuk mengatakan sesuatu, tetapi setelah sesaat dia menutupnya dan berbalik."
show bob suit_sceptic
show mila jeans_and_blouse_front
ms "Saya datang sedikit lebih dekat dan memaksanya untuk menatap saya."
show mila jeans_and_blouse_serious_open_mouth
m "Apa yang kamu inginkan?"
show mila jeans_and_blouse_surprise
bob "..."
show mila jeans_and_blouse_serious_open_mouth
m "Apakah Anda ingin kembali ke rumah? __Tag_0__ dan lupa sesegera mungkin, kencan yang buruk di mana seorang gadis yang menjengkelkan membuat Anda mencoba pakaian?"
m "Apakah Anda menginginkannya?"
show mila jeans_and_blouse_surprise
show bob suit_frown
bob "..."
ms "Bob mengerutkan kening, tetapi terus diam."
show mila jeans_and_blouse_serious_open_mouth
m "Saya tidak tahu cara membaca pikiran Bob. __Tag_0__ Apa yang Anda inginkan?"
show mila jeans_and_blouse_surprise
bob "..."
ms "Matanya berlari dari sisi ke sisi, seperti seorang remaja, terperangkap dalam pencurian kue."
ms "Saya mengambil langkah mundur untuk memberinya sedikit ruang."
bob "..."
show mila jeans_and_blouse_serious_open_mouth
m "Saya menyeret Anda ke toko pakaian karena bagi saya sepertinya Anda tidak peduli tentang tanggalnya. __Tag_0__ Babi saya juga."
m "Untungnya, saya tidak terlalu banyak berpakaian untuk acara ini."
m "Bayangkan betapa bodohnya penampilan saya jika saya melakukannya?"
show mila jeans_and_blouse_remorse
bob "..."
show bob suit_frown_open_mouth
bob "Kami tetap terlihat bodoh bersama."
show mila jeans_and_blouse_frown
m "..."
show mila jeans_and_blouse_frown_open_mouth
m "Apakah Anda benar -benar berpikir begitu?"
show bob suit_frown at left:
    xzoom 0.8 yzoom 0.8
ms "Bob memalingkan muka."
m "Bob?"
bob "..."
scene bg mila_incoming_hug
ms "Aku membawanya ke dagu dan membuatnya menatapku."
m "Apakah Anda benar -benar berpikir begitu atau Anda hanya takut berdebat dengan orang lain?"
bob "..."
scene bg mila_incoming_hug_looking_aside
m "Lihat."
ms "Saya menoleh ke permukaan cermin dari salah satu jendela."
scene bg mila_and_bob_mirror
m "Apakah kita terlihat bodoh?"
bob "..."
scene bg mila_and_bob_mirror_hand_on_hip
m "Kami terlihat seksi bersama, jika Anda bertanya kepada saya. __Tag_0__ seperti seorang gadis dengan Sugardaddy -nya."
ms "Bob tidak menjawab, tetapi wajahnya bersih, dan aku bahkan memperhatikan semacam senyum."
ms "Saya sedikit mendorongnya dengan pinggul saya."
scene bg mila_and_bob_mirror_hand_on_hip_smile
m "Berhentilah mengkhawatirkan pendapat orang lain."
m "Tidak mungkin bagi kita untuk disukai oleh setiap orang."
m "Mereka tidak menyukaimu. __Tag_0__well, persetan. __Tag_0__jap mereka tidak ingin melihat Anda. __Tag_0__well, biarkan mereka berpaling."
m "Jika Anda mengangkat kepala, Anda dapat melihat bahwa tidak semua orang membenci Anda."
m "Ada beberapa, yang menyukaimu."
scene bg mila_and_bob_mirror_hand_on_hip_embarassed_pointing_at_self
m "Seperti __tag_0__me__tag_1__, misalnya ..."
bob "..."
m "..."
scene bg mila_and_bob_mirror_hand_on_hip_smile_shy
m "Dan sekarang saya ingin minum."
m "Semakin panas di sini ..."
bob "..."
m "Apakah kita akan pergi? Atau apakah Anda ingin berlari pulang?"
bob "..."
ms "Bob berpikir beberapa saat, tetapi akhirnya tersenyum dan mengangguk."
ms "Saya membawanya di bawah siku."
scene mall
show mila jeans_and_blouse_run_smile
m "Saya tidak akan memaksa Anda untuk memilih tempat pertama kali."
m "Saya tahu satu tempat di mana Anda bisa makan dan menari dengan nikmat."
m "Tapi lain kali giliran Anda untuk memilih tempat."
ms "Bob tidak menjawab."
show mila jeans_and_blouse_proud_smile
m "Nah, itu sudah diselesaikan."
n "__tag_0__. __tag_0__. __tag_0__."
scene bg restaurant

if paul_took_initiative:
    ms "Saya sudah ke restoran ini bersama Paul."
    ms "Dan saya ingin menulis ulang pengalaman negatif kami dengan sesuatu yang menyenangkan."
    jump continue_bob_restaurant
ms "Kami pergi ke restoran terdekat. Di dalam, baunya menyenangkan dan segar, dan hangat, cahaya lembut menyala di luar angkasa."
ms "Tempat menari adalah di tengah aula, yang saat ini kosong."
label continue_bob_restaurant:
ms "Pelayan membawa kami ke meja kami, menerima perintah kami dan pergi."
ms "Kami mengobrol tentang pekerjaan dan minum sedikit anggur."
scene bg mila_table_blouse_playful
ms "Kehangatan tumpah ke tubuh saya, saya merasa mabuk."
ms "Anggur membuat kami santai."
ms "Saya ingin kembali ke suasana hati yang menyenangkan dan mengubah subjek menjadi sesuatu yang menarik dan kurang menyedihkan. __Tag_0__i telah mencapai titik di mana saya lelah merasa seperti pacar yang hanya merengek."
m "..."
m "Ayo bermain game."
ms "Anggur memacu sifat menyenangkan saya. Saya ingin berbicara tentang topik yang lebih jujur."
ms "Bob mengerutkan kening."
bob "Permainan?"
scene bg mila_table_blouse_seductive_gaze
m "Ya. Anda mengajukan pertanyaan, atau membuat pernyataan tentang saya, dan jika Anda benar - saya akan minum."
bob "Dan jika tidak?"
m "Kemudian selanjutnya adalah giliran saya untuk bertanya. Dan kemudian Anda lagi."
bob "..."
m "Apakah kita bermain?"
ms "Bob tidak mau setuju, tetapi anggur itu berperan, atau dia sendiri bosan dengan penolakannya yang konstan."
bob "Bagus."
scene bg mila_table_blouse_grin
m "Hah. Saya akan mulai."
scene bg mila_table_blouse_think
m "Terakhir kali Anda pergi berkencan setidaknya lima tahun yang lalu."
scene bg mila_table_blouse_playful
ms "Bob mengambil waktu sejenak untuk berpikir."
bob "Tidak. Sekitar dua tahun yang lalu, saya bertemu dengan seorang wanita. Kami pergi ke bioskop. Sekali."
scene bg mila_table_blouse_surprise
ms "Saya tidak bisa menahan diri dan mengangkat alis saya dengan terkejut."
m "Benar-benar? Dan apa yang terjadi selanjutnya?"
bob "Sekarang bukan giliran Anda untuk mengajukan pertanyaan."
ms "Bob menyeringai."
scene bg mila_table_blouse_grin
m "Itu benar."
scene bg mila_table_blouse_playful
bob "..."
bob "Anda merasa kasihan pada saya dan itulah mengapa Anda melakukan semua ini."
scene bg mila_table_blouse_think
ms "Saya berpikir sejenak, tetapi kemudian saya menggelengkan kepala."
m "\"Sorry\"bukan kata yang cocok. Aku menyukaimu dan karena itu aku ... mengkhawatirkanmu. Ini lebih dekat dengan kebenaran."
scene bg mila_table_blouse_seductive_gaze
m "Ada alasan lain, tetapi kami berdua tidak siap untuk itu."
ms "Kami bertiga belum siap untuk itu, itu akan lebih akurat."
bob "..."
bob "Kami berdua gagal ... game ini membosankan ..."
scene bg mila_table_blouse_grin
m "Ahah."
m "Apakah Anda mengatakan bahwa kami harus menaikkan taruhannya? Anda benar!"
bob "Bukan itu yang saya ..."
ms "Bob mencoba mengatakan sesuatu, tetapi saya tidak ingin mendengarkan."
scene bg mila_table_blouse_seductive_gaze
m "Anda ingin mencium saya sekarang."
ms "Bob berhenti berbicara dan menatapku."
ms "Lalu dia perlahan mengangkat gelas dan menyesap."
scene bg mila_table_blouse_grin
ms "Saya tersenyum."
scene bg mila_table_blouse_think
m "Hmmm ... Anda pikir Anda melakukan sesuatu yang salah dengan berkencan dengan wanita yang sudah menikah."
ms "Bob menyesap lagi."
scene bg mila_table_blouse_playful
m "Sejujurnya, tidak mudah bagi saya .__ TAG_0__ Saya tidak yakin apa yang Anda pikirkan, __ tag_0__, tapi ini adalah pertama kalinya saya berkencan dengan orang lain selain Paul .."
bob "..."
ms "Bob tampak bingung."
ms "Bagus. Hidup tidak semudah yang Anda pikirkan. Saya yakin Anda tidak mengerti apa yang saya inginkan dan apa yang saya rasakan."
ms "Tapi Anda akan, pada akhirnya."
scene bg mila_table_blouse_think
m "Hmmm ... mari kita tambahkan beberapa bumbu."
ms "Bob menatapku dengan waspada."
scene bg mila_table_blouse_playful
m "Anda masturbasi membayangkan seks dengan saya."
bob "!!!"
ms "Bob menatapku dengan kaget."
m "..."
scene bg mila_table_blouse_seductive_gaze
ms "Saya tetap diam, dan menunggu jawabannya."
bob "..."
m "Dengan baik? Apakah saya salah?"
bob "..."
bob "..."
ms "Bob berbalik dan membawa gelas ke bibirnya."
scene bg mila_table_blouse_blush_naughty_whispering
ms "Aku tidak bisa menolak, sedikit mencondongkan tubuh ke depan untuk menjadi lebih dekat dengannya dan berbisik:"
m "Saya juga."
bob "!"
scene bg mila_table_blouse_playful
m "Itu sebabnya, saya juga akan menyesap."
bob "..."
"__tag_0 __..."
ms "Pada suatu saat, saya tidak tahu bagaimana itu terjadi, tidak ada anggur di dalam botol."
ms "Dan tiba -tiba, pikiran saya mulai berputar -putar di kepala saya dengan kecepatan tinggi, dan saya tidak bisa menangkapnya lagi."
ms "Inilah saatnya. __Tag_0__ momen, ketika kita harus berhenti berbicara dan mengambil tindakan."
scene bg mila_table_blouse_playful_drunk
m "Kita harus menari! Bisakah kita menari?"
ms "Bob menggelengkan kepalanya."
bob "Tidak, terima kasih."
scene bg mila_table_blouse_pout_drunk
m "..."
bob "Apakah giliran saya untuk mengajukan pertanyaan?"
m "Itu adalah permintaan, bukan pertanyaan, Bob."
bob "Ah ... maaf ..."
scene bg mila_table_blouse_playful_drunk
m "Ayo oooon. __Tag_0__Jika Anda menari dengan saya, saya akan memenuhi salah satu keinginan Anda."
bob "..."
scene bg restaurant
show mila jeans_and_blouse_drunk_hand_open at center
ms "Saya bangkit dan mengulurkan tangan saya."
m "Datang!"
ms "Hehe ... terdengar cabul!"
ms "Bob sedikit melawan saya, tetapi ketika dia mengerti saya tidak akan mundur, dia berdiri."
bob "Saya tidak tahu cara menari."
scene bg mila_and_bob_dance
ms "Aku tersenyum dan meletakkan tangannya di pinggangku."
m "Tidak ada yang rumit. Dengarkan saja musiknya."
ms "Menurut tangannya yang gemetar, jelas dia khawatir."
ms "Tetapi anggur dan seluruh situasinya sangat memabukkan sehingga ketidakpastiannya hanya meningkatkan nafsu makan saya."
if paul_touch_ass == False:
    jump mila_took_iniative

ms "Saya mengambil langkah maju dan menekan tubuh saya ke tubuhnya."
ms "Tangannya tetap menggantung di udara."
ms "Saya mengambil pergelangan tangannya dan bertemu matanya."
ms "Dia tidak menolak."
show cg mila_and_bob_dance_hands_on_ass at truecenter with dissolve
ms "Perlahan -lahan aku menurunkan tangannya ke punggungku, dan kemudian menariknya ke bawah sampai telapak tangannya berada di pantatku."
ms "Dengan perut saya, saya merasa ketika kemaluannya menjadi keras."
ms "Aku tersenyum, melepaskan pergelangan tangannya dan memeluk lehernya."
bob "..."
ms "Kami hampir membeku di posisi ini."
ms "Perlahan -lahan saya memindahkan pinggul saya ke ritme musik, menggosok seluruh tubuh saya ke arahnya."
ms "Bob ingin melepas tangannya, tetapi saya berhasil mencegat pergelangan tangannya dan menekannya ke pantat saya."
m "..."
ms "Jika Paul tidak meminta itu ... __tag_0__i saya tidak yakin siapa di antara kita yang lebih malu dalam situasi ini - I atau Bob. ..."
ms "Tapi kami terus bergerak perlahan, _ tag_0__ takut untuk berpaling dari satu sama lain, _ tag_0__ takut untuk mematahkan keseimbangan yang tidak terlihat dan melihat diri kami dari samping."
jump continue_dance_bob

label mila_took_iniative:

ms "Saya pikir akan lebih mudah bagi Bob jika dia tidak bisa melihat mata saya."
ms "Jadi saya membalikkan punggung saya dan mundur selangkah."
show cg mila_and_bob_dance_from_behind at center:
    ypos 1.8
    linear 5.0 ypos 1.1
ms "Saya merasa dengan punggung saya dan memanaskan penisnya yang keras."
ms "Baru -baru ini, fakta yang satu ini bisa membuat saya merah."
ms "Tapi sekarang ..."
ms "Sekarang saya ingin lebih menghirinya dan merasakan setiap milimeter kemaluannya."
ms "Saya berbalik dan mata kami bertemu."
ms "Dia malu, dan aku tersenyum padanya."
ms "Dan rasa malunya membangunkan bagian kesadaran saya yang lebih muram."
m "Anda tahu mereka mengatakan bahwa tarian itu seperti seks."
ms "Aku menekannya dengan seluruh tubuhku dan menggosok pantatku ke penisnya."
m "Dan ada yang mengatakan bahwa tarian itu bahkan lebih baik."
ms "Bob praktis berhenti bergerak. Dia tampak seperti kelinci yang ketakutan."
ms "Dan sialan betapa aku menyukai kekuatan ini atas dia ..."
ms "Aku bangun berjinjit dan mendorong kemaluannya dengan pantatku."
ms "Berat badan saya tidak akan cukup untuk menjatuhkannya - lagipula dia jauh lebih berat dari saya."
ms "Tapi Bob masih sedikit terhuyung -huyung dan meraih pinggulku."
show cg mila_and_bob_dance_from_behind_hands_on_hips:
    ypos 1.8
    linear 5.0 ypos 1.1
ms "Saya menangkap tatapannya dan tersenyum."
ms "Bob ingin melepas tangannya, tetapi saya membawanya di pergelangan tangan dan menjalankannya di sepanjang tubuh saya, di sepanjang pinggang saya, ke pinggul saya ..."
ms "Di dadaku ..."
define flash = Fade(0.1, 0.0, 0.5, color="#FF0080")
show cg mila_and_bob_dance_from_behind_hands_on_tits with flash
ms "Telapak tangannya terpaku pada pakaianku, dan satu -satunya pikiran di kepalaku adalah:"
ms "Saya ingin telanjang ..."

label continue_dance_bob:
scene bg restaurant
ms "Tetapi musik berakhir, dan kami mendapati diri kami berpelukan di depan mata, dan tiba -tiba menjadi memalukan."
show mila jeans_and_blouse_sad_looking_up
m "..."
show bob suit_awkward_smile:
    xzoom 0.8 yzoom 0.8
bob "..."
hide bob
hide mila
scene bg bob_table_happy_laugh
ms "Kami kembali ke meja kami."
ms "Untuk sementara kami minum anggur secara diam -diam, yang memungkinkan kami untuk sedikit rileks. Dan kemudian mengoceh sampai penutupan."
ms "Akhirnya, Bob tersenyum padaku dan berbicara tanpa batasan kompleksnya."
ms "Kami kembali ke rumah setelah tengah malam ... mabuk dan bahagia."
"..."
"..."
scene bg doors with fade
show mila jeans_and_blouse_front
m "Terima kasih Bob ..."
m "Saya bersenang -senang."
show bob suit_smile at left:
    xzoom 0.8 yzoom 0.8
ms "Bob tersenyum. __Tag_0__ secara nyata. __Tag_0__ itu bukan meringisnya yang biasa. __Tag_0__ itu adalah senyum sukacita yang baik dan solid."
show mila jeans_and_blouse_run_smile
ms "Saya tersenyum balik."
bob "Terima kasih. Saya juga menyukainya ..."
m "..."
show bob suit_frown
ms "Dalam waktu kurang dari satu detik, senyumnya memudar lagi, dan kesedihan kembali ke matanya."
bob "Oke, saya akan pergi. __Tag_0__ memiliki malam yang baik."
ms "Bob buru -buru berbalik, tapi aku menangkap lengan bajunya dengan gerakan yang biasa."
show mila jeans_and_blouse_sad_looking_up
m "Tunggu..."
show bob suit_sceptic
ms "Bob membeku dan berbalik."
hide mila
show cg mila_kiss_shy_looking_down at right:
    xzoom 0.85 yzoom 0.85
    ypos 0.9
ms "Saya bermain dengan kunci di tangan saya."
m "Tahukah Anda apa artinya jika Anda membawa seorang gadis pulang setelah kencan dan dia tidak bersembunyi di belakang pintu segera?"
show bob suit_frown
bob "..."
show bob suit_frown_open_mouth
bob "TIDAK? Bagaimana saya harus tahu?"
show bob suit_frown
m "..."
show cg mila_kiss_shy_looking_up_biting_lip with dissolve
ms "Aku melirik Bob dan tersenyum dengan sugestif."
ms "Bob tidak mengerti petunjuknya."
show cg mila_kiss_shy_looking_up_hair_hand with dissolve
ms "Aku melepas rambutku di belakang telingaku dan menembak mataku lagi."
ms "Bob menatapku dengan serius."
show cg mila_kiss_haaaa with dissolve
ms "Saya menghela nafas."
show cg mila_kiss_pout with dissolve
m "Cium aku sudah ..."
bob "Saya tidak berpikir ..."
ms "Saya mengganggu alasannya dengan gerakan."
m "Berhenti berpikir. __Tag_0__ough dari keraguan Anda. __Tag_0__i sudah menunjukkan inisiatif yang cukup."
ms "Saya berhenti untuk memberikan kata -kata saya berikutnya lebih banyak kekuatan."
show cg mila_kiss_love_smile with dissolve
m "Giliranmu."
bob "..."
m "..."
ms "Keheningan menjadi sangat tegang dan tajam sehingga sepertinya bisa memotong Anda."
ms "Bob menelan dan mengambil langkah ke arahku."
show cg mila_kiss_kiss:
    ypos 1
    linear 1 ypos 0.9
ms "Aku mengangkat daguku dan memejamkan mata agar lebih mudah baginya untuk menciumku."
hide bob
m "..."
bob "..."
m "..."
show cg mila_and_bob_kiss_side at truecenter:
    xzoom 1 yzoom 1
bob "..."
m "..."
ms "Ciuman itu sangat ringan dan lembut sehingga aku hampir tidak melihatnya."
hide cg
show bob suit_awkward_smile at left:
    xzoom 0.8 yzoom 0.8
show mila jeans_and_blouse_blush_embarassed_twist_hair
ms "Saya membuka mata dan menatap Bob."
ms "Dia berbalik, malu."
m "..."
bob "..."
show mila jeans_and_blouse_blush_looking_aside
ms "Kami berdiri dalam keheningan yang canggung untuk sementara waktu."
m "Selamat malam Bob. __Tag_0__THanks untuk malam yang indah."
ms "Bob tersenyum dan membuka mulutnya untuk mengatakan sesuatu."
ms "Tapi matanya berhenti di pintu kami, dan dia menjadi sedih lagi."
show bob suit_frown_open_mouth
bob "Dan kalian ... kalian berdua ..."
show bob suit_awkward_smile
ms "Bob tersenyum sedih."
show mila jeans_and_blouse_sad_looking_aside
bob "Selamat malam."
ms "Dia berbalik dan pergi ke apartemennya."
m "..."
m "..."






"__tag_0__. __tag_0__. __tag_0__."
scene bg door with fade
play sound "door-open-close.mp3"
label menu_paul_and_mila_first_dominance_challenge:
show screen nts_stats_overlay
menu:
    "Siapa yang lebih dominan sekarang?"

    "Paul (membutuhkan 2+ kepatuhan Mila) (kepatuhan Mila + 1)" if dom >= 2:
        $ dom += 1
        jump netorase_stats_scene1_paul

    "Paul (tidak cukup ketundukan Mila)" if dom < 2:
        "Paul ragu -ragu, dia tidak yakin, bahwa Mila siap untuk didominasi."
        "Dia membutuhkan setidaknya 2 kepatuhan."
        jump menu_paul_and_mila_first_dominance_challenge

    "Mila (membutuhkan 2+ dominasi) (dominasi Mila + 1)" if mila_dom >= 2:
        $ mila_dom += 1
        jump netorase_stats_scene1_mila

    "Mila (tidak cukup dominasi)" if mila_dom < 2:
        "Mila ragu -ragu. Dia masih tidak memiliki tekad untuk mendominasi."
        "Dia membutuhkan setidaknya 2 dominasi."
        jump menu_paul_and_mila_first_dominance_challenge


label netorase_stats_scene1_paul:
show bg paul_and_mila_kiss_shock
ms "Begitu saya membuka pintu, Paul meraih tangan saya dan menyeret saya ke dalam."
hide screen nts_stats_overlay
ms "Pintu menghantam di belakangku, dan aku mendapati diriku ditekan dengan punggung ke pintu."
ms "Paul menutupi bibirku dengan bibirnya dan dengan penuh semangat menciumku sebelum aku berhasil memahami apa yang terjadi."
show bg paul_and_mila_kiss_closed_pleasure
ms "Tangannya yang panas meluncur di atas tubuhku."
ms "Saya memejamkan mata dan menyerah pada sensasi."
ms "Setelah beberapa saat yang panjang, Paul bersandar dan saya bisa menarik napas."
show bg paul_and_mila_face_to_face
m "..."
p "..."
m "Hai..."
m "Apa itu?"
p "I ... __tag_0__KEKU Anda saat Anda meninggalkan lift."
p "Saya melihat melalui lubang intip ..."
show bg paul_and_mila_face_to_face_embarassed
ms "Acara sebelumnya melintas di kepalaku."
ms "Darah bergegas ke wajahku dan tiba -tiba menjadi lebih panas di sini dari sebelumnya."
show bg paul_and_mila_face_to_face_embarassed_cautious
ms "Punggung saya tertutup keringat dingin. Saya bertemu tatapan Paul, berharap melihat kemarahan, kecemburuan dan kebencian di sana."
ms "Tapi itu hanya keinginan kebinatangan murni."
ms "Saya tertelan."
m "Apakah Anda ingin ... __tag_0__i berarti ...__ tag_0__ mungkin kita harus pergi ke kamar tidur?"
p "TIDAK."
ms "Dengan suara serak yang rendah, merinding yang melintasi kulit saya."
show bg paul_and_mila_face_to_face_embarassed_biting_lip
ms "Tangannya yang kuat membelai tubuhku dan aku meleleh di bawah sentuhannya."
p "Angkat bajumu."
ms "Anggur dan keinginan memerintah di atas kepalaku."
ms "Saya hanya ingin satu hal - untuk patuh."
ms "Dengarkan suaranya. Lakukan apa yang dia inginkan."
show bg paul_and_mila_face_to_face_embarassed_pulled_by_self
m "..."
m "..."
p "Lepaskan."
show bg paul_and_mila_face_to_face_embarassed_bra
ms "Saya patuh."
m "..."
ms "Dia menciumku lagi dan berlari di pinggang dan pinggulku."
ms "Saya merasakan keinginannya dengan seluruh tubuh saya."
ms "Dan saya mengerti betapa sulitnya baginya untuk menahan diri."
ms "Saya tidak mengerti __tag_0__why__tag_1__ dia menahan diri."
ms "Dia bersandar lagi."
p "Lepaskan bra."
show bg paul_and_mila_face_to_face_embarassed_topless
ms "Saya patuh."
ms "Bra tergelincir di sepanjang siku saya dan jatuh ke lantai."
ms "Ruangan itu panas tapi kulit dadaku jauh lebih lembut dan sensitif."
ms "Saya merasakan ratusan jarum yang tidak terlihat menggali kulit."
ms "Paul melahapku dengan matanya."
ms "Dia melihatku telanjang ratusan kali."
ms "Tapi sekarang ... untuk beberapa alasan rasanya itu adalah pertama kalinya kami."
show bg paul_and_mila_face_to_face_embarassed_topless_squeeze
ms "Paul dengan kasar meremas putingku yang keras."
m "Aduh!"
ms "Paul melepaskan puting saya segera, tetapi rasa sakit itu tidak ingin menghilang."
ms "Aku menutupi dada dengan tanganku."
show bg paul_and_mila_face_to_face_embarassed_topless_covering_breasts
m "Itu menyakitkan ..."
ms "Paul mengabaikan kata -kata saya lagi menggali bibirnya ke bibirku."
ms "Dia menekan saya ke pintu dan saya merasa terkunci di ruang sempit ini."
ms "Agresi dan keinginannya terasa seolah -olah dia ingin memakanku."
show cg paul_and_mila_kiss_close_up
ms "Saya kembali merasakan campuran ketakutan dan kegembiraan."
ms "Seperti aku memangsa di tangannya."
ms "Tapi itu tidak menakutkan."
ms "Saya tahu bahwa dia akan berhenti jika saya bertanya .__ tag_0__ saya melihat keinginannya yang mentah, dan saya menyukai kenyataan bahwa saya membuatnya merasa seperti itu."
ms "Saya ingin menjinakkan sifat binatangnya. __Tag_0__ dan untuk ini perlu dipatuhi. __Tag_0__Adapt."
ms "Jadi ke pikiran saya, saya tidak memperhatikan ketika tangan Paul membuka kancing jeans saya."
ms "Saya merasa jari -jarinya menyebarkan labia basah saya."
ms "Telapak tangannya menekan klitoris dan saya menggerakkan pinggul saya ke depan melekat padanya lebih kuat."
show cg paul_and_mila_jeans_shlick at truecenter:
    xzoom 0.7 yzoom 0.7
m "Mmm ..."
p "Kamu sangat basah, pelacur ..."
m "..."
ms "Kata -kata kasar Paul terbang melewati telingaku."
ms "Saya terlalu fokus pada sensasi. __Tag_0__ dan saya ingin mendengar suaranya terlalu banyak."
m "Mmm ..."
ms "Saya tidak memperhatikan pada titik apa dia menurunkan jeans saya. __Tag_0__ mereka menghalangi, jadi saya benar -benar menghapusnya."
ms "Paul terus membelai vagina saya saat saya dilucuti."
ms "Itu sebabnya sulit untuk menanggalkan pakaian."
ms "Tapi aku tidak ingin dia berhenti."
ms "Saya tidak ingin sensasi ini berhenti sejenak."
ms "Dan saya tidak ingin kehilangan suasana hati saya ..."
ms "Paul mendesak saya ke pintu dan menghentikan jari -jarinya yang bergerak."
show cg paul_and_mila_panties_shlick
ms "Aku tidak bisa menahan diri dan mulai menggerakkan pinggulku sendiri, bercinta dengan jari -jarinya, seperti mereka adalah penisnya."
ms "Tetapi Paul tidak membiarkan saya merangsang diri saya terlalu banyak, menahan saya di ambang orgasme."

if paul_touch_ass:
    p "Apakah Anda melakukan apa yang saya minta?"
    ms "Saya mengerang sebagai tanggapan sesuatu yang tidak jelas."
    show cg paul_and_mila_panties_shlick_wipe_hand:
        xzoom 1 yzoom 1
    ms "Paul menarik jari -jarinya dari vaginaku dan menyeka mereka di wajahku."
    ms "Kelembaban, penghinaan dan stimulasi berhenti memungkinkan saya sedikit sadar."
    p "Anda melakukan apa yang saya minta, pelacur?"
    show cg mila_dazed_with_paul
    m "..."
    ms "Saya tidak segera mengerti apa yang dia tuntut."
    ms "Tetapi kemudian saya menyadari bahwa dia berbicara tentang permintaannya."
    m "Ya ... __tag_0__ke ...__ tag_0__ kami menari ..."
    ms "Pikiranku berkabut .__ tag_0__ Aku ingin berhenti berbicara dan akhirnya merasakan kemaluannya di dalam."
    ms "Benjolan berdiri di tenggorokanku."
    show cg mila_dazed_tears_with_paul
    ms "Tatapan tindik Paul dipenuhi dengan kecemburuan dan keinginan .__ tag_0__ Saya tidak bisa mengerti apa yang dia pikirkan .__ tag_0__ untuk beberapa alasan, saya merasa tersinggung dan air mata muncul di mata saya."
    m "Aku meletakkan tangan Bob di pantatku ..."
    m "Dan aku menggosoknya saat kami menari ..."
    jump netorase_stats_scene1_paul_continue

ms "Saya menyadari bahwa Paul hampir tidak menahan diri, dan saya lebih ingin menggodanya."
show cg paul_and_mila_panties_shlick_smirk
m "Anda tahu saat kami berada di tanggal itu ..."
ms "Saya tidak mengenali suara saya. Kedengarannya lebih rendah dari biasanya."
ms "Seolah -olah itu bukan saya berbicara, tetapi orang lain."
m "Kami pergi menari ..."
ms "Paul menarik celana saya .__ tag_0__ kainnya dengan menyakitkan dipindahkan ke dalam vagina, __ tag_0__ tapi saya senang dengan stimulasi apa pun."
ms "Dan kecemburuannya bercampur dengan keinginan lebih membuat saya bersemangat."
ms "Saya sedikit mendorong pinggul saya, tidak mengalihkan pandangan dari Paul."
m "Aku menempel padanya dengan tubuhku ..."
m "Aku merasakan kemaluannya menggosok pantatku."
m "Dan Anda tahu apa yang dia lakukan pada saat itu?"
p "..."
ms "Paul lagi memasukkan jari -jarinya ke dalam vaginaku dan aku mengerang tanpa sadar."
m "Mmm ..."
ms "Gerakan Paul kasar, cepat, dan sedikit canggung."
show cg paul_and_mila_panties_shlick_hand_in_pants
ms "Ini memungkinkan saya untuk sedikit sadar dan meletakkan tangan saya di celananya."
ms "Aku merasakan kemaluannya dan melingkarkan tanganku."
ms "Gerakan Paul menjadi kurang kuat, ia terganggu oleh sensasinya."
ms "Aku berbisik di telinganya."
m "Saat kami menari tangannya meluncur di seluruh tubuhku ..."
m "Dia membelai pinggulku ..."
m "Perutku ..."
m "Payudaraku ..."
show cg paul_and_mila_kiss_close_up:
    xzoom 1 yzoom 1
ms "Paul dengan penuh semangat menciumku dan mendesakku ke pintu ..."
m "Mmm ..."
label netorase_stats_scene1_paul_continue:
ms "Saya mendengar klik kunci."
hide screen nts_stats_overlay
ms "Jantungku berdebar kencang di dadaku."
scene bg mila_panties_shock_scared
m "Paul? Apakah kamu gila?!"
p "Shhhh."
m "Saya hampir telanjang!"
p "Hush, kataku."
ms "Paul membuka pintu dan mengambil tanganku dari celananya."
ms "Saya melihat sekeliling dengan gugup, panik, berharap bahwa salah satu pintu tetangga kami akan terbuka ..."
ms "Bagaimana saya melihat di mata mereka jika ini terjadi?"
scene bg mila_panties_scared_blush
m "..."
ms "Mereka akan menunjuk ke arahku ..."
ms "Wanita akan sangat jijik ..."
ms "Dan para pria ... akan melahap saya dengan mata mereka ..."
scene bg mila_panties_blush_closed_biting
m "Mmm ..."
"..."
scene bg mila_at_door_panties with fade
ms "Saya mendapati diri saya berdiri di seberang pintu apartemen Bob."
ms "Paul memaksa saya untuk membungkuk punggung saya."
ms "Udara dingin menusuk kulit. Tapi kegembiraan tidak memungkinkan saya untuk membeku."
ms "Paul mengambil rambutku dan memasukkan jari -jarinya ke dalam vaginaku."
scene bg mila_at_door_finger_fuck
m "Mmm ..."
ms "Saya tidak bisa menahan erangan."
p "Jadi, Anda menari dan mencium pria lain, terlepas dari kenyataan bahwa Anda sudah menikah?"
m "..."
ms "Sejenak saya takut. Tetapi merasakan jari -jari Paul di vaginaku dan sentuhannya, aku menyadari bahwa dia tidak marah."
ms "Bahwa ini hanya bagian dari permainan."
scene bg mila_at_door_finger_fuck_clenched_teeth
m "Ya..."
p "Dan Anda bersemangat dari itu?"
ms "Saya tanpa sadar meremas kaki saya dan mendorong pinggul saya ke arah jari -jarinya, ingin merasakannya lebih dalam dalam diri saya."
m "Ya ...__ tag_0__ sangat ..."
p "Apa yang akan Anda sebut seorang gadis yang berperilaku seperti itu?"
scene bg mila_at_door_finger_fuck_pressed_lips
m "..."
ms "Saya tidak ingin mengatakannya dengan keras. Terutama di sini, di tempat umum ...__ tag_0__ tepat di pintu ke apartemen Bob ..."
ms "Tapi kegembiraan mengambil alih."
m "__Tag_0__slut ..."
p "Artinya, Anda mengakui bahwa Anda adalah pelacur nymphomaniac, yang meleleh dari sentuhan pria lain?"
m "__Tag_0__yes ..."
scene bg mila_at_door_finger_fuck_scream
m "__Tag_0__yes__tag_1__ __tag_2__yes__tag_1__ __tag_4__yes!"
p "Diam, jangan berteriak ..."
ms "Pikiran saya ditutupi oleh kabut merah muda, saya berdiri di tepi jurang, dan hampir tidak menahan teriakan saya."
ms "Paul menghentikan jari -jarinya."
scene bg mila_at_door_finger_fuck_pressed_lips
p "Tidakkah Anda berpikir bahwa ini tidak cukup untuk Anda?"
ms "Saya bingung ...__ tag_0__ Saya tidak mengerti apa yang dia katakan, __ tag_0__ Saya hanya ingin merasakan kemaluannya di dalam ..."
m "Hah?"
p "Apakah Anda ingin cum, pelacur?"
scene bg mila_at_door_finger_fuck_begging
m "Ya, sangat ... Tag_0__ tolong, persetan dengan saya ..."
ms "Tetapi Paul tidak terburu -buru dan terus memelukku di ambang."
m "Silakan..."
ms "Paul membawaku ke tenggorokan dan membawa bibirnya dekat ke telingaku."
scene bg mila_at_door_finger_fuck_holding_neck
p "Anda tahu, saya pikir untuk orang cabul seperti Anda itu tidak cukup."
ms "Saya tertelan. Bahkan melalui tabir kegembiraan, saya mengerti bahwa ada sesuatu yang salah."
p "Saya pikir Anda menginginkan lebih. Jadi?"
m "..."
ms "Saya tidak mengatakan apa -apa."
scene bg mila_at_door_finger_fuck_bitting_lips
ms "Paul menggerakkan jari -jarinya dan aku menggigit bibirku agar tidak mengerang."
ms "Tetesan jus saya mengalir ke bawah kaki saya."
ms "Saya menyadari bahwa saya akan melakukan apa saja untuk cum."
scene bg mila_at_door_finger_fuck_begging
m "Paul ... tolong ..."
p "Diam."
scene bg mila_at_door_finger_fuck_bitting_lips
ms "Aku menggigit bibirku."
p "Anda hanya malu mengakuinya, bukan?"
m "..."
p "Tapi tanyakan pada dirimu sendiri. Siapa kamu?"
m "..."
scene bg mila_at_door_finger_fuck_tears
ms "Saya tertelan."
ms "Katakan."
m "Saya ...__ tag_0__ Saya seorang pelacur ..."
p "Tepat."
p "Ingat ini ketika Anda ragu bagaimana berperilaku dengan Bob."
p "Dipahami?"
m "..."
m "Ya..."
p "Apakah Anda suka menjadi pelacur?"
scene bg mila_at_door_finger_fuck_bitting_lips
ms "Jari -jari Paul terus membelai saya. Tapi kali ini saya menyadari bahwa dia mendorong saya lebih dekat ke tepi."
m "Ya!"
p "Diam."
p "Apakah Anda ingin terlihat?"
m "..."
scene bg mila_at_door_finger_fuck_hands_mouth
ms "Aku menggenggam mulutku dengan tangan dan menutup mataku, berkonsentrasi pada sensasi."
p "Besok Anda akan berperilaku seperti pelacur dengan bob."
ms "..."
ms "Saya hampir tidak mengerti apa yang dia katakan. Saya menyerah pada aliran perasaan dan sensasi."
p "Besok Anda akan memberinya kesenangan."
p "Bukan sebagai pelacur yang mengharapkan sesuatu sebagai balasannya."
p "Anda akan menyenangkan dia seperti pelacur sungguhan."
p "Dipahami?"
m "MGM ..."
ms "Saya terus menjepit mulut saya dan berusaha untuk tidak membuat suara."
ms "Saya mendengar suara lift, seseorang menyebutnya di salah satu lantai. Tetapi Paul tidak memperhatikan hal itu."
ms "Ketakutan ditangkap, rasa malu dan kegembiraan dicampur menjadi koktail sesak."
ms "Dan jari -jari Paul terus menekan bagian dalam vaginaku."
p "Apakah Anda ingin cum?"
m "MGM!"
ms "Saya bergumam dalam hal afirmatif yang tidak jelas."
p "Apakah Anda akan berperilaku seperti pelacur mulai sekarang?"
m "MGM!"
ms "Ya, persetan! __ tag_0__ Biarkan aku cum ..."
scene bg mila_at_door_finger_fuck_hands_mouth_tight_hug
ms "Paul meremasku dalam pelukannya dan mulai meniduriku dengan jari -jarinya."
scene bg mila_at_door_finger_fuck_hands_mouth_tight_hug_rolling_eyes with flash
m "..."
scene bg mila_at_door_finger_fuck_hands_mouth_tight_hug_rolling_eyes_legs with flash
m "!"
scene bg mila_at_door_finger_fuck_hands_mouth_tight_hug_rolling_eyes_legs_cum with flash
m "!!!"
ms "Tampaknya bagi saya sejenak saya kehilangan kesadaran."
ms "Otot -otot kaki saya dikurangi secara tidak sadar."
ms "Napas saya berhenti."
ms "Tampak bagi saya bahwa hati saya juga berhenti berkelahi."
ms "Atau dipukuli begitu keras sehingga saya tuli."
scene bg mila_at_door_finger_fuck_hands_mouth_tight_hug_leg_after_sex
ms "Sepertinya saya berteriak, tetapi Paul menjepit mulut saya dengan tangannya."
ms "Melalui tabir orgasme, saya mendengar lonceng lift."
ms "Paul menarikku ke dalam flat kami dan kami menghilang di belakang pintu sesaat sebelum lift terbuka."
scene bg paul_and_mila_face_to_face_tired
m "Haaa haaa ..."
ms "Saya berbaring di lantai dan bernafas berat dari orgasme yang baru saja berpengalaman ..."
scene bg paul_and_mila_face_to_face_laugh
p "Ahah."
ms "Paul tertawa dan aku tertawa bersamanya."
ms "Saya merasa ringan dan bahagia ..."
ms "Kepalaku kosong dan bebas dari pikiran."
scene bg paul_and_mila_lying_from_above
m "..."
p "..."
p "Tetapi jika ada, itu bukan lelucon."
scene bg paul_and_mila_lying_from_above_mila_confused
ms "Aku mengangkat kepalaku dan menatapnya dengan bingung."
p "Maksudku ... besok ...__ tag_0__ aku ingin kamu ...__ tag_0__ untuk melangkah lebih jauh ..."
ms "Saya tertelan."
m "Apakah kamu serius?"
p "..."
p "Ya."

if dom >= mila_dom:
    m "Saya ... Saya tidak yakin bisa."
    scene bg paul_and_mila_lying_from_above_mila_confused_paul_looking
    p "Anda bisa .__ tag_0__ Hanya ingat bagaimana perasaan Anda hari ini."
    p "Bangunlah cabul batin Anda."
    p "Meskipun ... saya ragu dia sedang tidur ..."
    ms "Aku bercanda memukul bahu."
    scene bg paul_and_mila_lying_from_above_mila_shy_love_paul_looking
    m "Hai!"
    p "Ahah ..."
    m "..."
    p "..."
    scene bg paul_and_mila_lying_from_above_mila_smirk_paul_confused
    p "Jadi?"
    p "Maukah Anda melakukannya untuk saya?"
    m "..."
    m "..."
    m "__Tag_0__fine ..."
    ms "Tiba -tiba saya merasa panas karena rasa malu atau kegembiraan."
    ms "Saya tidak segera menyadari apa yang saya setujui."
    ms "Batas -batas dari hal -hal yang dapat diterima diperluas, apa yang dulu tampaknya tidak terpikirkan sekarang menjadi kenyataan."
    scene bg paul_and_mila_lying_from_above_hug
    ms "Saya ingin merasakan hubungan kami, keintiman dan cinta kami, jadi saya menempel padanya."
    ms "Dia membelai punggungku."
    ms "Gerakan sederhana ini sudah cukup bagi saya untuk tenang."
    m "Bagus..."
    ms "Saya mengulangi dengan lebih percaya diri."
    if _in_replay:
        return
    jump bob_first_hj
ms "Terlepas dari orgasme saya baru -baru ini, suasana hati yang menyenangkan mengambil alih saya."
scene bg paul_and_mila_lying_from_above_mila_smirk
m "Apakah itu benar?"
p "..."
ms "Reaksi proaktif saya membuat Paul sedikit bingung."
show bg paul_and_mila_lying_from_above_mila_smirk_paul_confused
m "Artinya, Anda ingin istri Anda berperilaku seperti pelacur?"
p "..."
ms "Aku memanjatnya dan tersenyum."
show bg paul_and_mila_missionary_smirk
m "Apakah Anda ingin gadis Anda yang berharga berperilaku bejat tidak hanya dengan Anda, kan?"
ms "Tetapi Paul tidak memalingkan muka kali ini dan tersenyum padaku."
ms "Tangannya membelai pinggulku."
p "Ya sayang. Saya menginginkannya."
m "Hehehe ..."
ms "Aku merasakan penisnya yang keras menggosok pantatku."
ms "Kulit saya diwarnai dengan kegembiraan."
ms "Saya merasa seperti batas -batas hal yang dapat diterima telah diperluas, apa yang dulu tampaknya tidak terpikirkan sekarang menjadi kenyataan."
ms "Dan saya semakin menyukai kenyataan ini ..."
m "Bagus."
ms "Saya membungkuk."
show bg paul_and_mila_lying_from_above_hug
m "Tetapi Anda lebih baik mengambil tanggung jawab dan mencintaiku seperti yang akan saya lakukan."
ms "Paul tersenyum."
p "Tentu saja."
p "Anda adalah wanita terpanas di dunia."
if _in_replay:
    return
jump bob_first_hj

label netorase_stats_scene1_mila:
scene bg door with fade
play sound "door-open-close.mp3"
show paul suit_open_mouth_blush at left
ms "Ketika saya pulang, seorang Paul yang bersemangat bertemu saya hampir di ambang pintu."
ms "Dia membeku beberapa langkah dari saya dan membuka mulutnya, tetapi tidak mengatakan apa -apa."
show mila jeans_and_blouse_sad_looking_up at center
p "..."
m "..."
m "Halo..."
p "Halo..."
show paul suit_blush_looking_aside
ms "Paul memalingkan muka."
show mila jeans_and_blouse_front
ms "Ciuman dengan Bob, kencan, dan perilaku pasif Paulus menempatkan sifat sadis pada diriku."
ms "Saya membuka ritsleting lalat dengan celana jins dan pergi ke arahnya."
ms "Tekanan saya memaksanya untuk mengambil beberapa langkah ke belakang sampai dia menabrak kursi dan duduk."
ms "Saya tersenyum dan menurunkan jeans saya."
scene bg mila_unzipped_lowered_jeans_smirk_tease
m "Kami bersenang -senang bersama."
m "Kami berjalan sedikit, dan kemudian pergi ke restoran."
scene bg mila_from_behind_pulloff_jeans
ms "Aku membalikkan punggungku ke Paul dan membungkuk untuk menarik celana jinsku."
ms "Penis Paul membengkak dan menonjol di celananya."
m "Kami minum sedikit dan menari."
ms "Saya berbalik dan melemparkan kaki saya di bahu Paul."
scene bg mila_leg_on_shoulder_wet_panties
ms "Saya membawa selangkangan saya lebih dekat ke wajahnya dan merasakan napas panas di vaginaku."
m "Kami menari dan tangannya membelai tubuhku ..."
scene bg mila_leg_on_shoulder_panties_aside_juice
ms "Saya memindahkan celana dalam saya dan menunjukkan betapa basahnya saya."
m "Apakah Anda ingin mencicipi betapa saya menyukainya?"
ms "Paul tidak ragu -ragu, dia dengan penuh semangat meletakkan lidahnya di vaginaku dan mulai menjilat jusku."
scene bg mila_leg_on_shoulder_panties_aside_juice_spread_pussy
m "Mmm ... anak yang baik ..."
m "..."
m "Mmmm ..."
m "Ya..."
m "Seperti itu ..."
m "Ahhh ..."
ms "Lidah Paul bermain dengan klitoris saya dan jatuh jauh ke dalam vaginaku."
scene bg mila_leg_on_shoulder_panties_aside_head_grab
ms "Aku meraih rambutnya dan menekannya ke selangkanganku."
m "Oh ya ..."
ms "Saya menyadari bahwa sulit bagi saya untuk berdiri di atas kaki saya."
ms "Tapi saya tidak ingin pergi tidur dan memberikan diri saya pada belas kasihan Paul."
ms "Saya ingin menggodanya ..."
ms "Saya bersandar dan kemudian mengambil langkah."
m "Menanggalkan pakaian dan berbaring."
ms "Paul ragu untuk beberapa waktu, tetapi kemudian dipatuhi."
scene bg mila_panties_aside_pov_face_sitting
ms "Aku berdiri di atas wajahnya."
ms "Dia terlihat sangat manis dan tak berdaya dari atas ..."
ms "Saya bertanya -tanya bagaimana Bob akan terlihat dari sudut yang sama?"
m "..."
scene bg mila_panties_aside_pov_face_sitting_looking_aside_confused
m "!"
ms "Apa yang saya pikirkan?"
m "..."
ms "Tunggu ...__ tag_0__ kenapa tidak?"
scene bg mila_panties_aside_pov_face_sitting_grin
ms "Saya menyeringai."
m "Apakah Anda ingin istri Anda duduk di wajah Anda?"
p "Ya!"
ms "Paul meraih penisnya dan membuat beberapa pukulan."
scene bg mila_panties_aside_pov_face_sitting_threaten_finger
ms "Saya mengguncang jari saya."
m "Tidak, berhenti!"
m "Lepas tangan."
ms "Paul mematuhi."
scene bg mila_panties_aside_pov_face_sitting
m "Anak yang baik."
ms "Aku berjongkok dan menekan vaginaku ke bibirnya."
scene bg mila_panties_aside_face_sitting_from_side_hands_on_chest
ms "Hidungnya memasuki vaginaku. Saya menggigit bibir saya dan membuat beberapa gerakan untuk merasa nyaman."
m "Mmm ..."
ms "Paul bernapas melalui mulutnya, dan merasakan napasnya, klitoris saya menjadi lebih sensitif."
ms "Paul mulai membelai dengan lembut dengan lidahnya."
m "Mmm, ya ..."
m "Seperti itu ..."
p "..."
m "Tampak bagi saya bahwa saya menjadi kecanduan sensasi ini ..."
m "Mmm ...."
ms "Saya meletakkan tangan saya di dada Paul dan membuat beberapa gerakan dengan pinggul saya."
m "Haaa haaa ..."
m "Yeees ..."
ms "Paul Dick bergoyang di depan wajahku. Dia sedikit berdenyut, seolah mencoba menarik perhatian."
m "Apakah Anda ingin saya menyentak Anda?"
p "Ya! Aku mohon!"
m "Ahah ..."
m "Saya akan melakukan apa pun yang Anda inginkan, tetapi dengan satu kondisi ..."
ms "Paul membeku sebentar, tetapi kemudian terus membelai vaginaku dengan lidahnya."
m "Besok saya akan melakukan hal yang sama untuk Bob."
ms "Paul membeku lagi."
ms "Saya menggerakkan pinggul saya dan ujung jari saya berlari di sepanjang perut dan pinggulnya."
m "Apa yang kamu katakan?"
p "..."
ms "Pangkulnya berdenyut dalam gerakan awal untuk membuatku membelai."
ms "Tapi saya ingin mendengar suara Paul."
ms "Saya ingin merasa bahwa dia sudah siap ...__ tag_0__ bahwa kita berdua siap .__ tag_0__ ke langkah berikutnya__tag_0__ ke dalam jurang."
ms "Bahwa kita siap untuk beralih dari kata -kata ke tindakan, dari fantasi ke kenyataan."
ms "Paul ragu -ragu dan saya menyadari bahwa dia belum siap. Dia akan menolak."
ms "Karena itu, saya baru saja mulai menikmati sensasi."
ms "Saya menutup mata dan menggerakkan pinggul saya, mendekati orgasme."
m "Ya, sayang ...__ tag_0__ seperti ini ..."
m "Lainnya ...__ tag_0__ di sana, ya ..."
m "Ahhh ahhh ..."
m "Saya hampir ...__ tag_0__ sedikit lebih sedikit tekanan ..."
m "Ahhh ..."
m "Mmm ..."
ms "Saya merasa seperti Paul mengambil saya di pergelangan tangan dan menarik saya ke bawah."
ms "Awalnya saya tidak mengerti apa yang dia inginkan."
ms "Tetapi ketika kemaluannya menusuk telapak tangan saya, saya dilemparkan ke dalam panas."
ms "Untuk beberapa alasan, saya membayangkan bahwa di tangan saya adalah penis Bob, bukan milik Paul."
ms "Perlahan -lahan saya berlari ke bawah, mencoba beradaptasi dengan ritme saya sendiri."
ms "Rasanya seperti saya menyentuhnya untuk pertama kalinya."
ms "Paul mulai memindahkan pinggulnya."
ms "Dia sudah berada di tepi."
m "Mmm ...."
ms "Ayamnya mulai berdenyut di tangan saya, dan pada saat itu, saya menyadari bahwa saya juga tidak jauh dari orgasme."
ms "Saya ingin merasakan sperma di kulit saya, jadi saya membungkuk dan meletakkan wajah saya lebih dekat."
p "Mhhmhm!"
ms "Paul menembaki wajahku dengan aliran sperma yang ketat."
ms "Itu sangat panas sehingga rasanya seperti membakar saya ...__ tag_0__ dan ini adalah jerami terakhir bagi saya."
scene bg mila_orgasm_close_up_split_from_side
ms "Saya merasakan otot -otot kaki saya mulai berdesir dari orgasme saya."
ms "Sensasinya begitu cerah dan berat sehingga bagi saya tampaknya saya sekarat."
ms "Saya hampir tidak merasakan bagaimana Paul menutupi wajah saya dengan sperma."
ms "Sensasi itu hilang dalam badai umum sensasi."
ms "Saya menggali kuku saya ke pinggul Paul dan menggeram seperti binatang buas."
"..."
"__tag_0__. __tag_0__. __tag_0__."
scene bg mila_in_sperm_on_pauls_chest
ms "Ketika kami akhirnya tenang, saya menyadari bahwa saya tidak bisa bergerak."
ms "Tapi entah bagaimana saya mengumpulkan kekuatan saya, berguling dan berbaring di sebelah Paul."
m "Fuuuh ..."
m "Itu keren."
p "Itu benar -benar ..."
m "..."
p "..."
scene bg mila_looking_at_paul_in_sperm_on_pauls_chest_paul_worried
p "Apakah lelucon itu tentang ... tentang Bob?"
ms "Saya menatapnya."
m "What will you say if I say \"No\"?"
p "..."
scene bg mila_looking_at_paul_in_sperm_on_pauls_chest_paul_frown
ms "Paul mengerutkan kening."
ms "Saya sedang menunggu jawabannya dan untuk beberapa alasan, saya khawatir."
p "..."
p "Aku tidak tahu..."
scene bg mila_looking_at_paul_smile_in_sperm_on_pauls_chest_paul_frown
ms "Saya tersenyum. Untuk beberapa alasan, saya tahu bahwa dia akan menjawab seperti itu."
m "Lalu tidak. Itu bukan lelucon."
p "..."
m "Apa yang kamu katakan sekarang?"
ms "Paul diam bahkan lebih lama."
ms "Tapi tetap saja setelah beberapa saat dia diam -diam menjawab."
scene bg mila_looking_at_paul_smile_in_sperm_on_pauls_chest_paul_fine
p "__Tag_0__fine ..."
ms "Dia tampak sangat rentan bagi saya."
ms "Saya menghela nafas."
p "Paul."
ms "Dia menatapku dan segera memalingkan muka."
scene bg mila_looking_at_paul_serious_in_sperm_on_pauls_chest_paul_giggle
p "Lihat aku."
ms "Paul mendongak dan tersenyum aneh."
m "?"
p "..."
p "Anda terlihat sangat lucu ketika Anda mencoba untuk menjadi serius dengan sperma."
ms "Aku menjilat bibirku."
m "Anda pikir?"
ms "Paul tersipu."
ms "Ketegangan di antara kita menguap."
scene bg mila_looking_at_paul_serious_in_sperm_on_pauls_chest_paul_serious
m "Lihat. __Tag_0__i melakukan apa yang saya lakukan, karena kami berdua menyukainya, dan hanya jika itu benar kami akan melanjutkan .__ tag_0__ Anda memang mengerti itu, kan?"
p "..."
p "Ya."
m "Kita dapat menghentikannya kapan saja jika kita ingin .__ tag_0__ seperti sekarang, misalnya."
p "..."
m "Memahami?"
p "..."
p "Ya."
m "..."
m "Saya akan bertanya lagi, apakah Anda ingin melanjutkan?"
ms "Paul bertemu dengan pandangan saya dengan lebih percaya diri."
p "Ya. __Tag_0__ Ya, saya menginginkannya."
scene bg mila_looking_at_paul_smile_in_sperm_on_pauls_chest_paul_confident
ms "Saya tersenyum."
m "Oke."
m "Aku mencintaimu, Paul."
p "..."
p "Aku pun mencintaimu..."
if _in_replay:
    return



label bob_first_hj:
"__tag_0 __..."
scene bg mila_woke_up_stretch
ms "Saya bangun lebih awal"
ms "Sesuatu berubah dalam diriku ..."
ms "Rasanya seperti saya masih dalam mimpi"
ms "Dan bisa melakukan apa pun yang bahkan belum pernah saya impikan sebelumnya"
ms "Aku mencium Paul yang masih tidur dan diam -diam pergi ke kamar mandi"
scene br with fade
show mila casual_worried at center
ms "..."
ms "Jari gemetar dengan kegembiraan atau kegugupan"
ms "Saya tidak yakin ada lebih banyak kegembiraan atau lebih banyak kegugupan ..."
ms "Saya menggerakkan paha dan dada saya"
ms "Kulit yang ditutupi merinding sebagai respons terhadap sentuhan ini."
ms "..."
show mila casual_thinking
ms "Untuk beberapa alasan saya tidak bisa memutuskan ..."
ms "Saya tahu apa yang perlu saya lakukan ... __tag_0__ Apa yang ingin saya lakukan ..."
ms "Tapi ketakutan menghalangi saya; Saya merasa tidak berdaya dan rentan."
ms "Saya ingin melakukannya ... tetapi pada saat yang sama saya ingin menyembunyikan ..."
show mila casual_interested_blush
ms "Tatapan saya jatuh pada jas yang saya temukan di apartemen Bob dan mencuci."
ms "..."
m "Saya bertanya -tanya apakah itu cocok untuk saya?"
ms "..."
show mila dva_concerned
ms "..."
show mila dva_back
ms "..."
show mila dva_posing
ms "..."
m "Ahah ..."
ms "Kegugupan menghilang seolah -olah dengan tangan."
show mila dva_think
ms "Hm ..."
m "Bagaimana kalau..."
ms "Saya melihat diri saya di cermin"
ms "..."
ms "Saya pikir saya telah melihat karakter ini di suatu tempat ..."
show mila dva_serious
ms "Haruskah dia serius?"
ms "..."
show mila dva_think
ms "Tidak, ada sesuatu yang salah."
show mila dva_cheerful
ms "Mungkin ceria dan cerah?"
ms "..."
show mila dva_concerned
ms "Hehe. Terlihat keren."
ms "Saya sangat berbeda dari diri saya sehingga itu memberi saya kepercayaan diri"
ms "Saya mengenakan mantel saya dan hati -hati, berusaha untuk tidak membuat suara apa pun, saya pergi ke apartemen Bob."
play sound "door-open-close.mp3"
scene bg bobs_apartments_clean with fade
ms "Jantungku berdegup kencang di dadaku"
play sound "heart.mp3"
ms "Telapak tangan tertutup keringat"
show mila dva_concerned
ms "Apa yang saya lakukan?"
ms "Apa yang saya lakukan di sini?"
ms "Mila ... apakah kamu mengerti apa yang akan terjadi setelahnya?"
ms "..."
show mila dva_concerned_looking_aside_blush
ms "Ya, kami sepakat bahwa saya akan berperilaku ...__ tag_0__ berbeda"
ms "Tapi sialan ..."
scene bg closed_door
show mila dva_concerned:
    ypos 0.35
ms "Aku mengulurkan tangan ke pegangan pintu ke kamar Bob dan membeku."
play sound "heart.mp3"
show mila dva_concerned_looking_aside_blush
ms "Saya ... apakah saya benar -benar ingin melakukan ini?"
ms "..."
show mila dva_scared
ms "Lagi pula, tidak akan ada jalan untuk kembali."
ms "Bagaimana jika Paul berpikir ini bukan yang dia inginkan?"
ms "Bagaimana jika saya tidak menyukainya?"
ms "Apa yang akan saya sampaikan kepada Bob dalam kasus itu?"
ms "..."
ms "Sialan sial"
ms "Saya tertelan."
ms "Pikiran bergegas di kepalaku dengan kacau. Saya tidak bisa melacaknya."
ms "Kaki saya mundur selangkah tanpa perintah saya."
ms "..."
show mila dva_concerned
ms "Mungkin ada baiknya memikirkan kembali semuanya lagi?"
ms "Kami ... __tag_0__k kami bisa pergi ke bar bersama ...__ tag_0__ atau mengundang Bob ke atas ..."
ms "..."
scene bg bobs_apartments_clean
show mila dva_sad_smile
ms "Ya .__ tag_0__ mungkin lebih baik melakukan itu."
stop sound
ms "Saya entah bagaimana segera tenang, berbalik dan berjalan menuju pintu keluar."
ms "Akan lebih baik dengan cara ini."
ms "..."
show mila dva_concerned
ms "Berjalan melewati cermin, aku melirik diriku dan membeku."
ms "..."
ms "Tunggu."
ms "Apakah saya berpakaian apa -apa?"
ms "Mungkin setidaknya mengambil selfie?"
play sound "shot.mp3"
scene bg mila_bobs_apartment_dva_selfie_smile
ms "Saya tersenyum pada ide saya, mengeluarkan telepon saya dan mengarahkan kamera ke diri saya sendiri."
ms "..."
scene bg mila_bobs_apartment_dva_selfie_upset
ms "..."
ms "Untuk beberapa alasan, ketakutan saya dan keinginan kekal untuk setengah-setengah membuat saya jengkel."
scene bg mila_bobs_apartment_dva_selfie_agry
ms "Berapa lama waktu yang dibutuhkan untuk menerima diri saya sendiri?"
ms "Apakah saya benar -benar kucing yang menakutkan?"
ms "..."
ms "Persetan"
ms "Aku akan masuk"
scene bg closed_door
ms "..."
play sound "door-open-close.mp3"
scene bg bobs_room_bob_sleep
show mila dva_scared at truecenter:
    ypos 0.75 xpos 0.75
ms "..."
ms "Setelah saya datang ke kamar, saya langsung membeku"
ms "Semua keberanian saya menguap"
ms "Bob berbaring di tempat tidur mendengkur."
if mila_was_in_the_room:
    ms "Ruangan itu juga berbau sperma dan keringat."
    ms "Baunya tampak semakin kuat"
    jump dva_continue
ms "Ada aroma keringat dan sperma yang berat di ruangan itu."
ms "Udara tampak lengket dan kotor."
label dva_continue:
scene bg bobs_room_bob_sleep_mila_opens_window
ms "Saya berjingkat ke jendela dan membukanya."
ms "Udara dingin segar langsung membersihkan ruang bau"
scene bg bobs_room_bob_sleep
ms "Dada Bob naik dan jatuh perlahan. __Tag_0__e tidur nyenyak dengan anggota tubuhnya yang tersebar di tempat tidur."
show mila dva_concerned at truecenter:
    ypos 0.75 xpos 0.75
ms "..."
ms "Jadi ... jadi apa selanjutnya?"
ms "..."
show mila dva_scared
ms "Saya tertelan."
ms "Lalu aku perlahan -lahan duduk di tepi tempat tidur dan menyentuh kaki Bob."
m "__Tag_0__bob!"
ms "..."
ms "Dia tidak bereaksi."
m "__Tag_0__bob !!"
ms "Saya memanggilnya sedikit lebih keras, tetapi dia masih tidak menanggapi."
ms "..."
play sound "heart.mp3" loop
ms "Jantungku berdegup kencang di dadaku."
ms "Saya meraih tepi selimut dan menariknya ke samping"
ms "..."
ms "..."
ms "Sedetik kemudian meluncur ke lantai."
scene bg bob_on_bed_nude_flacid_sleep_mila_shock
ms "Oh. __Tag_0__my .__ tag_0__ Tuhan."
ms "Bob's Dick lebih tebal dari Paul bahkan dalam keadaan santai ini."
scene bg bob_on_bed_nude_flacid_sleep_mila_blush
ms "Saya ingin menyentuhnya, tetapi saya menahan diri, takut membangunkan Bob."
ms "Kulit di penisnya telah memerah - rupanya dia tersentak kemarin seolah tidak ada hari esok"
ms "..."
scene bg bob_on_bed_nude_flacid_sleep_mila_bitlip
ms "Saya bertanya -tanya apa yang dia bayangkan?"
ms "..."
ms "Seolah dihipnotis, saya melihat penisnya dan membayangkan Bob masturbasi."
ms "Tanganku meraih ke bawah."
ms "Jas itu mencegah saya menyentuh vaginaku, jadi saya hanya menggosoknya melalui pakaian saya."
m "__Tag_0__bob?"
ms "Saya memanggilnya lagi. Suaraku terdengar serak dan rendah."
ms "Saya tertelan."
ms "Bob tidak bereaksi."
ms "..."
ms "Apa yang harus saya lakukan? .."
ms "..."
scene bg bob_on_bed_nude_flacid_sleep_mila_scared
ms "Aku membelai kakinya."
ms "Napasnya membeku sejenak, dan aku membeku bersamanya."
ms "Saya tidak tahu apa yang saya inginkan lebih banyak, baginya untuk bangun atau tidak."
ms "Kulitnya lembut dan panas. __Tag_0__Saya merasakan betapa beratnya tubuhnya hanya dengan menyentuhnya."
ms "Tatapan saya tertarik pada kemaluannya. Saya tidak memperhatikan kapan saya semakin dekat."
ms "Tanganku dengan lembut membelai pahanya, sangat dekat dengan bola -bola besarnya."
scene bg closeup_hand_near_mila_aroused
ms "Aroma penis yang berat dan tidak menyenangkan memenuhi hidung saya."
ms "Saya ingin berpaling darinya, tetapi pada saat yang sama baunya membuat saya bersemangat."
m "__Tag_0__bob!?"
ms "Untuk beberapa alasan suara saya terdengar lebih tenang dari kali terakhir .__ tag_0__ sekarang saya takut membangunkannya."
ms "Saya ingin momen ini bertahan selama mungkin."
ms "Bau ini .__ tag_0__ situasi ini .__ tag_0__ pakaian saya ...__ tag_0__ Semua ini mengeluarkan sesuatu yang liar dan binatang dalam diri saya."
ms "Aku menjilat bibirku."
scene bg bob_on_bed_nude_flacid_sleep_mila_scared
ms "Bob pindah, dan aku menarik tanganku kembali."
ms "..."
ms "Tapi tidak ada yang terjadi."
scene bg bob_on_bed_nude_flacid_sleep_mila_angry
ms "Takut melumpuhkan saya sejenak, tetapi setelah beberapa saat, saya mengendalikan diri dan menjadi marah."
stop sound
ms "Aku benar -benar bergerak lebih dekat dan meraih penis Bob."
scene bg flacid_handjob_mila_angry
ms "Jari -jariku hampir tidak bisa membungkus kemaluannya yang tebal."
bob "Mmm ..."
ms "Bob menggumamkan sesuatu dalam tidurnya, tapi aku tidak mengerti apa."
play sound ["loops/SexSlide5.wav", "<diam 1>", "loops/SexSlide6.wav", "<diam 1>", "loops/SexSlide7.wav", "<diam 1>", "loops/SexSlide8.wav", "<diam 1>", "loops/SexSlide9.wav", "<diam 1>", "loops/SexSlide10.wav", "<diam 1>", "loops/SexSlide11.wav", "<diam 1>", "loops/SexSlide13.wav", "<diam 1>", "loops/SexSlide14.wav", "<diam 1>", "loops/SexSlide15.wav", "<diam 1>", "loops/SexSlide16.wav", "<diam 1>", "loops/SexSlide17.wav", "<diam 1>", "loops/SexSlide18.wav", "<diam 1>", "loops/SexSlide19.wav", "<diam 1>", "loops/SexSlide20.wav", "<diam 1>"] loop
scene bg flacid_handjob_mila_excited_low
ms "Perlahan -lahan aku membelai kemaluannya, menikmati cara itu mengeras dan berdenyut di tanganku."
ms "Ya Tuhan, ya Tuhan, ya Tuhan!"
ms "Saya melakukannya!"
scene bg flacid_handjob_mila_excited
ms "Saya melakukannya !!!"
ms "Aku menyentak Bob!"
ms "Penisnya ada di tanganku!"
scene bg flacid_handjob_mila_excited_high
ms "AAAAA !!!"
ms "Saya pelacur!"
ms "..."
ms "Dick Bob sedikit membengkak, tetapi kemudian berhenti menanggapi sentuhan saya."
scene bg flacid_handjob_mila_offended
ms "Untuk beberapa alasan saya merasa terhina dengan ini."
ms "Apakah saya tidak cukup baik untuk Anda?"
ms "..."
ms "Saya duduk lebih nyaman dan membawa wajah saya lebih dekat ke penis."
scene bg pov_handjob_eww
ms "Bau itu menjadi lebih kuat."
ms "Untuk sesaat saya berpikir untuk menggunakan mulut saya untuk membantu diri saya sendiri, tetapi baunya menghilangkan semua keinginan."
scene bg pov_handjob_neutral
ms "Saya meraih penisnya dengan kedua tangan dan mulai memijatnya dengan lembut sepanjang panjangnya."
bob "Hmmm ..."
ms "Bob membuka matanya dan menatapku dengan terkejut."
scene bg pov_handjob_awkward
ms "Saya bingung, dan tidak tahu harus berbuat apa ..."
ms "..."
ms "..."
ms "Tangan saya terus memijat penisnya sendiri."
ms "Aku tersenyum dan meludah di kokir, menambahkan sedikit pelumas."
ms "Bob menggosok matanya dan menatapku tanpa mengucapkan sepatah kata pun."
scene bg pov_handjob_bigger_cock_blush_bitlip
ms "Kontolnya menjadi sangat keras di tangan saya, berubah menjadi raksasa yang nyata."
ms "Ya Tuhan, bagaimana itu bisa muat di dalam diriku?"
ms "..."
ms "..."
ms "Siapa bilang ini mungkin terjadi?"
scene bg pov_handjob_bigger_cock_shy_smile
ms "Aku tersenyum malu -malu pada pikiranku."
ms "Bob takut bergerak dan hanya menatapku dengan diam -diam."
ms "..."
ms "..."
ms "Jeda masih canggung dan sulit."
ms "Saya baru saja menggerakkan lengan saya dan mencoba fokus pada gerakan."
ms "Bob menatapku dan tampaknya tidak bernafas atau berkedip."
scene bg pov_handjob_bigger_cock_looking_down_shy
ms "Ada begitu banyak nafsu dalam pandangannya ... begitu banyak keinginan."
ms "Saya menelan dan menurunkan mata saya dengan rasa malu."
ms "Sial ... aku menyukainya saat dia menatapku seperti itu."
ms "Kegembiraan mendadak pikiranku."
ms "Saya ingin melakukan sesuatu yang lebih bejat ..."
show screen nts_stats_overlay
menu:
    "Saya hanya akan bersantai dan mencoba untuk menyenangkannya (ketundukan Mila + 1)":
        $ dom += 1
        jump mila_sub_hj_bob
    "Saya ingin menggodanya (dominasi Mila + 1)":

        $ mila_dom += 1
        jump mila_dom_hj_bob

label mila_sub_hj_bob:
ms "Saya merasa seolah -olah ada sesuatu yang menekan bahu saya menyeret saya ke arah kemaluannya."
hide screen nts_stats_overlay
scene bg pov_handjob_bigger_cock_shy_smile
ms "Saya memandang Bob dan menatap tatapannya."
ms "Dia perlahan dan mantap mengikuti setiap gerakan saya."
play sound "heart.mp3" loop
ms "Bibirku mati rasa dengan kegembiraan."
ms "Mulutku dipenuhi air liur."
ms "Perlahan saya mulai lebih rendah"
ms "Bau penisnya menjadi tak tertahankan .__ tag_0__ tak tertahankan."
scene bg pov_handjob_bigger_cock_closer
ms "Aku membungkuk lebih dekat ke penisnya."
ms "Begitu dekat sehingga saya bisa melihat pola kulitnya."
ms "Setetes pre-cum muncul di cockhead."
scene bg pov_handjob_bigger_cock_closer_closed_eyes
ms "Aku menutup mataku ..."
ms "Lalu bersandar lebih dekat."
ms "Dan mencium kemaluannya."
play sound "kiss.mp3"
scene bg pov_handjob_bigger_cock_closed_eyes_kiss
bob "Mmm ..."
ms "Bob bergidik dan mengerang."
ms "Kepala ayam itu panas dan basah dari precum asin."
ms "Saya membuka mata dan menatapnya"
play sound "lick.wav"
scene bg pov_handjob_bigger_cock_open_eyes_lick
ms "Aku menjilat penisnya dengan lembut tanpa mengalihkan pandangan dari Bob."
play sound "putin.wav"
scene bg pov_handjob_bigger_cock_open_eyes_deep_kiss
ms "Aku membelah bibirku dan dengan hati -hati membiarkan kepala penisnya masuk ke dalam mulutku."
ms "Saya harus berusaha keras untuk membuka mulut cukup untuk menghindari memukul penis dengan gigi saya."
ms "Dan saya masih tidak berhasil."
ms "Ya Tuhan, betapa besar yang dia miliki."
ms "Tangan kedua saya, di atas kehendak saya, turun dan mulai membelai klitoris saya."
play sound "moan1.wav"
scene bg pov_handjob_bigger_cock_closed_eyes_deep_kiss
m "Mmm ..."
ms "Kali ini saya mengerang."
ms "Saya merasakan Bob bergerak dan merasakan sentuhan lembut pada rambut saya."
scene bg pov_handjob_bigger_cock_open_eyes_hands_on_head_deep_kiss_surprised
ms "Saya membuka mata dan menyadari bahwa Bob memegang kepala saya."
ms "Gairah dan keinginan menutupi matanya seperti tabir."
ms "..."
ms "Saya merasa bahwa dia memiliki sedikit kendali atas dirinya sendiri dan mencoba menarik diri."
ms "Tapi dia hanya mendesakku lebih dekat padanya."
play sound "gag1.mp3"
m "Mmm!"
ms "Bob perlahan tapi mantap mendorong kemaluannya lebih dalam di dalam mulutku"
play sound "moanprotest.wav"
scene bg pov_handjob_bigger_cock_open_eyes_hands_on_head_suck_scared_frown_mascara_tears
m "MMM!"
ms "Saya mencoba menolak ..."
ms "Tapi dia terlalu kuat dan terlalu rela"
play sound ["suck1/1.mp3", "suck1/2.mp3", "suck1/3.mp3", "suck1/4.wav", "suck1/5.mp3", "suck1/6.mp3", "suck1/7.mp3", "suck1/8.mp3", "suck1/9.wav", "suck1/10.mp3", "suck1/11.mp3", "suck1/12.mp3"] loop
scene bg pov_face_fuck_mascara_tears_saliva_scared
ms "Bob, tidak memperhatikan perlawananku, mulai benar -benar meniduri kepalaku"
ms "Kemaluannya menumbuk kepalanya yang besar ke tenggorokanku."
ms "Saya entah bagaimana berhasil bernapas melalui hidung saya."
scene bg pov_face_fuck_mascara_tears_saliva_idle
m "Payah payah mengisap"
ms "..."
ms "..."
ms "Lampu menyala di depan mataku. Sepertinya ayam Bob mengetuk semua pikiran dari kepalaku."
ms "Saya menyadari bahwa tangan saya masih dengan panik membelai vagina saya."
ms "Dan sial ... __tag_0__ Saya menyukai hasratnya yang brutal."
play sound ["suck2/1.wav", "suck2/2.wav", "suck2/3.wav", "suck2/4.wav", "suck2/5.wav", "suck2/6.wav", "suck2/7.wav", "suck2/8.wav", "suck2/9.wav", "suck2/10.wav", "suck2/11.wav"] loop
scene bg pov_face_fuck_mascara_tears_saliva_seductive_gaze
ms "Dan juga terlepas dari kenyataan bahwa ia memiliki kontrol diri yang buruk, ia masih cukup lembut dan tidak melewati garis kekejaman."
ms "Itu memungkinkan saya untuk sedikit rileks."
m "Payah payah mengisap."
ms "Saya menyadari bahwa Bob akan segera cum, dan saya mulai membelai bolanya dengan tangan saya."
m "Payah payah mengisap."
ms "Saya merasa ada sesuatu yang hilang."
ms "Seperti saya takut untuk masuk semua ..."
ms "Takut untuk membiarkan diri saya pergi ... __tag_0__ dan melakukannya setengah-setengah"
ms "Seperti saya tidak ingin menyenangkan dia ..."
ms "Dan itu membuatku marah"
play sound ["suck3/1.wav", "suck3/2.wav", "suck3/3.wav", "suck3/4.wav", "suck3/5.wav", "suck3/6.wav", "suck3/7.wav", "suck3/8.wav", "suck3/9.wav", "suck3/10.wav", "suck3/11.wav", "suck3/12.wav", "suck3/13.wav"] loop
play music ["moans/1.wav", "<diam 3>", "moans/2.wav","<diam 3>", "moans/3.wav", "<diam 3>"] loop
scene bg pov_face_fuck_mascara_tears_saliva_smile
ms "Saya mulai menggerakkan lidah saya ke dalam mulut saya, menjilati kepala kemaluannya yang menabrak tenggorokan saya."
m "Mmm ..."
ms "Saya menyadari bahwa saya tidak dapat menahan erangan saya, meskipun perawatannya kasar."
ms "Saya ingin dia terus menggunakan saya."
ms "Seperti mainan seks. __Tag_0__Just seperti cumdump."
ms "Seperti pelacur."
m "Mmm ..."
ms "Cum untukku, anak besar ..."
m "Mmm ..."
ms "..."
ms "Tunggu sebentar ..."
ms "Air mani?"
ms "..."
ms "Dia akan segera cum ..."
ms "..."
ms "Tidak akan aku tersedak ..."
bob "Urgh! .."
stop music
stop sound
scene bg pov_face_fuck_mascara_tears_pressed_before_cum with hpunch
ms "Bob menegang dan menekan kepalaku ke selangkangannya."
ms "Terlepas dari keinginan untuk membebaskan diri dari cengkeramannya, saya mencoba untuk rileks dan membiarkan penisnya masuk lebih dalam"
ms "Itu benar -benar menembus tenggorokan saya"
ms "Aku merasakan ketoknya semakin mengencang, dan sebentar lagi menembak banyak sperma tebal ke tenggorokanku."
play sound "SWFSlosh4.wav"
scene bg pov_face_fuck_mascara_tears_pressed_cum_full_mouth with hpunch
ms "Itu langsung mengisi seluruh mulut saya."
ms "Tapi itu baru permulaan."
play sound ["SWFSlosh4.wav", "<diam 0>", "SDTGag14.wav"]
scene bg pov_face_fuck_mascara_tears_pressed_cum_full_mouth_let_out with hpunch
ms "Beban berikutnya tidak kurang dari yang pertama, __ tAG_0__ dan dari tekanan itu terciprat dan mulai mengalir menuruni penis dan bola di aliran tebal."
play sound ["SWFSlosh5.wav", "SDTGag2.wav", "SWFSlosh4.wav", "SWFSlosh4.wav", "SDTGag10.wav", "SWFSlosh5.wav", "SWFSlosh4.wav","SWFSlosh5.wav", "SDTGag6.wav"]
scene bg pov_face_fuck_mascara_tears_pressed_cum_full_mouth_let_out_cum_from_nose_choking with hpunch
ms "Beban ketiga keluar melalui hidung saya, membuat saya tidak mungkin bernafas secara normal."
ms "Air mata mengalir dari mataku."
ms "Saya menepuk tangan Bob dan dia segera membiarkan saya pergi."
ms "Aku menarik diri, tertelan dan menarik napas dalam -dalam."
scene bg pov_leaned_back_facial_handjob_cum
ms "Aroma dan sisa -sisa sperma masih ada di mulutku"
play sound "SWFSlosh4.wav"
ms "Bob terus cum di seluruh tanganku."
play sound "SWFSlosh5.wav"
ms "Muat demi beban. Saya belum pernah melihat begitu banyak sperma."
ms "Rasanya seperti kuda datang pada saya."
jump mila_bob_handjob_continue

label mila_dom_hj_bob:
ms "Perasaan kekuasaan atas Bob membangkitkan sesuatu yang sesat dalam diri saya."
hide screen nts_stats_overlay
scene bg pov_handjob_bigger_cock_smug_dom
ms "Akhir -akhir ini, saya mulai merasa bisa mengendalikan Paul ketika saya memegang penisnya."
ms "Dan perasaan yang sama muncul ketika saya mengambil Bob dengan penis."
ms "Seorang pria besar dan kuat terletak di depan saya dan sepenuhnya tunduk pada kehendak saya."
ms "Dia siap melakukan apa saja untuk saya."
ms "Dia tampak seperti binatang kecil"
ms "Takut. __Tag_0__ dan bersemangat."
scene bg pov_handjob_bigger_cock_smug_smirk
ms "Senyum merayap ke bibirku."
m "Letakkan tangan Anda di belakang kepala."
ms "Saya kagum pada betapa rendah dan kuatnya suara saya."
ms "Saya bahkan tidak terkejut ketika Bob mematuhi perintah saya tanpa pertanyaan."
ms "Saya ingin menggoda bob .__ tag_0__ memaksanya untuk tunduk di depan saya."
scene bg pov_handjob_bigger_cock_open_mouth_saliva_flow
ms "Aku menjulurkan lidahku dan menunjukkan bagian dalam mulutku."
ms "Aliran air liur mengalir dari lidah dan mendarat di kepala penis."
ms "Saya menggosoknya dengan lembut dengan jari -jari saya."
scene bg pov_handjob_bigger_cock_smug_smirk_wet_cock
m "Apakah Anda ingin lidah ini menyentuh penis Anda?"
bob "YA!"
ms "Bob praktis meneriakkannya."
scene bg pov_handjob_bigger_cock_giggle_laugh_wet_cock
m "Ahahaha"
scene bg pov_handjob_bigger_cock_smug_smirk_wet_cock
m "Anak yang baik."
m "Untuk melakukan ini, Anda perlu mendengarkan saya, mengerti?"
ms "Bob mengangguk dengan tergesa -gesa."
m "Anak yang baik."
m "Tanyakan majikanmu."
bob "P-tolong ..."
m "Tolong apa?"
bob "Blow Me, Nyonya!"
scene bg pov_handjob_bigger_cock_frown_wet_cock
m "..."
m "Saya tidak mengatakan apa -apa tentang memberi Anda blowjob."
m "Saya mengatakan lidah ini akan menyentuh penis Anda."
bob "Maaf Nyonya!"
ms "Bob mengulurkan tangannya dan melambaikannya di depannya dengan meminta maaf."
m "Tangan di belakang kepala!"
ms "Bob buru -buru mengikuti perintah saya."
scene bg pov_handjob_bigger_cock_smug_smirk_wet_cock
m "Anak yang baik"
ms "Omong kosong .__ tag_0__ Saya suka kekuatan ini."
m "Ayo bermain game."
bob "Game?"
m "Ya .__ tag_0__ Saya akan mulai melakukan ini."
stop sound
ms "Aku mencondongkan tubuh lebih rendah .__ tag_0__ aroma berat dari kemaluannya memenuhi hidungku."
ms "Tapi saya sudah cukup bersemangat untuk tidak memperhatikannya."
scene bg from_side_licking_balls_handjob_closed_eyes
play sound "moans_suck.wav"
ms "Aku menjulurkan lidahku dan menjilat bolanya, asin dari keringat sambil mengintensifkan gerakan dengan tanganku."
bob "Ya Tuhan ..."
scene bg from_side_handjob_open_eyes_giggle
play sound "chuckle.wav"
ms "Saya terkekeh."
m "Jika Anda bisa menahannya tanpa cumming sebentar, maka jadilah itu. Aku akan meledakkanmu."
ms "Bob membuka matanya lebar -lebar dan menatapku dengan tak percaya."
scene bg from_side_licking_balls_handjob_open_eyes
play sound "moans_suck.wav" loop
ms "Aku menjilatnya lagi."
m "Mari kita mulai."
scene bg from_side_sucking_balls_handjob_open_eyes
ms "Aku mengisap bolanya ke dalam mulutku dan terus menyentak penisnya, yang tampaknya menjadi lebih besar."
bob "Urgh ..."
ms "Bob menutup matanya dan menggigit bibirnya."
scene bg from_side_handjob_open_eyes_piercing_eyes
m "Buka matamu dan lihat aku, Bob."
m "Tidak adil untuk berpaling."
scene bg from_side_licking_shaft_open_eyes
ms "Merasa tatapannya, aku tersenyum dan berlari lidah basah di sepanjang panjang poros."
ms "Aku bahkan tidak tahu apakah aku ingin dia kalah ..."
ms "Atau saya ingin kehilangan diri saya sendiri ..."
ms "Saya bertanya -tanya seperti apa ...__ tag_0__ untuk merasakan baut besar ini di mulut Anda."
ms "Aku memiringkan kepalaku dan melingkarkan bibirku di sekitar poros penisnya."
bob "Mmm ..."
ms "Saya merasa bahwa Bob sudah berada di ambang."
ms "Dan segera dia akan menutupi saya dengan spermanya."
ms "Dan saya tidak akan pernah bisa mencuci diri dari ini."
ms "Saya tidak bisa lagi berhenti menjadi diri saya."
ms "Saya seorang pelacur."
ms "Dan pelacur ...__ tag_0__ pelacur suka sperma."
scene bg from_side_licking_shaft_open_eyes
ms "Aku berlari lidah di sepanjang seluruh poros dan, __ tag_0__ merasakan penis tegang Bob dari sentuhanku, __ tag_0__ aku perlahan membuka mulutku ..."
scene bg pov_sucking_cockhead_piercing_eyes
play sound "moan_suck2.wav"
ms "Dan biarkan penisnya masuk ke mulut saya yang basah."
bob "Ya Tuhan!"
ms "Bob mulai segera Cumming."
ms "Saya ingin mengisap spermanya dengan lembut dan melepaskannya."
ms "Itu rencanaku ...__ tag_0__ tapi ..."
scene bg pov_sucking_cockhead_piercing_eyes_cum_first
play sound "SWFSlosh4.wav"
ms "Ada begitu banyak sperma sehingga langsung mengisi mulut saya dan mulai mengalir ke tangan saya dan turun ke bolanya."
play sound "SWFSlosh4.wav"
ms "Dan sialan ...__ tag_0__ itu sangat panas ..."
scene bg pov_sucking_cockhead_piercing_eyes_cum_second
play sound "SWFSlosh5.wav"
ms "Merasa aliran panas sperma pria lain memenuhi mulut saya."
ms "Merasa bahwa dia ada dalam kekuatan saya."
ms "Bahwa dia milikku."
play sound "SWFSlosh4.wav"
scene bg pov_sucking_cockhead_piercing_eyes_cum_smile
ms "Tanpa membiarkan penisnya keluar dari mulut saya, saya memandang Bob dan tersenyum."
ms "Anak yang baik."
ms "Bob tidak berhenti Cumming. Dia terus memompa mulut saya dengan air mani."
play sound "SWFSlosh5.wav"
scene bg pov_leaned_back_facial_handjob_cum_smile
ms "Aku melepaskan penisnya dari mulutku dan bersandar, lelah."

label mila_bob_handjob_continue:
ms "Itu menutupi tangan saya dan perlahan mengalir ke poros dan ke bola berbulu itu."
ms "Setelah beberapa detik, kejang berakhir dan semuanya menjadi sunyi."
ms "Bob menutupi wajahnya dengan tangan dan diam."
bob "I ...__ tag_0__ Saya minta maaf."
scene bg pov_leaned_back_facial_handjob_cum_smile
ms "Saya memerah sisa sperma dari kemaluannya dan bertanya dengan menarik."
m "Untuk apa? __ tag_0__ untuk cumming di seluruh saya?"
ms "Acara terbaru ini membangunkan pelacur nyata di dalam diri saya. __Tag_0__ dan saya tidak merasa canggung sama sekali. __Tag_0__quite sebaliknya. __Tag_0__Saya merasa bangga dan kuat"
bob "..."
bob "Ya…"
bob "Pada awalnya ...__ tag_0__ saya pikir saya masih bermimpi ... __tag_0__ dan kemudian ... __tag_0__i tidak bisa berhenti"
bob "Maaf! Saya sangat menyesal ..."
scene pov_leaned_back_facial_handjob_cum_looking_aside_doubtful
m "..."
ms "Saya tidak ingin menerima permintaan maafnya"
ms "Saya merasa jika saya menerimanya, itu berarti saya setuju bahwa dia melakukan sesuatu yang salah."
ms "Dan dia tidak."
scene bg pov_leaned_back_facial_handjob_cum_smile
m "Itu bukan mimpi bob .__ tag_0__ untuk kami berdua .__ tag_0__ tidakkah Anda ingin melihat seperti apa?"
ms "Bob Froze."
scene pov_leaned_back_facial_handjob_cum_smirk
m "Sperma tebal Anda mengalir ke bawah jari saya .__ tag_0__ Saya dengan lembut memijat penis besar Anda sampai secara bertahap menjadi lebih lembut ..."
bob "..."
scene pov_leaned_back_facial_handjob_cum_looking_aside_doubtful
m "TIDAK?"
ms "Bob melepaskan tangannya dari wajahnya dan menatap wajahku terlebih dahulu, tetapi matanya masih terikat pada penis."
scene waving_hand_with_cum_facial_grin_teasing
ms "Aku melambai padanya dengan jari -jariku diwarnai dengan spermanya."
ms "Dia melihatnya diam -diam, seolah -olah dia terpesona."
ms "..."
scene waving_hand_with_cum_facial_demanding
m "Anda tahu apa?"
m "Ambil foto saya."
bob "... __tag_0__ Apa?!"
m "Saya bilang ambil telepon Anda__tag_0__ dan buat foto saya."
bob "W-Why? __Tag_0__a gambar? Itu berbahaya!"
scene waving_hand_with_cum_facial_tilted_head_doubts
m "Apakah itu? __ tAG_0__ Maukah Anda menunjukkannya kepada kolega Anda yang menyebalkan? __ tag_0__ atau mempostingnya di suatu tempat?"
bob "..."
scene waving_hand_with_cum_facial_demanding
m "No. __tag_0__Kau tidak."
m "Anda bukan orang seperti itu."
ms "Aku dengan lembut membelai penisnya."
ms "..."
scene waving_hand_with_cum_facial_shy_looking_aside
m "Itulah mengapa saya bisa melakukan ... __tag_0__Risky hal -hal ... __tag_0__ dengan Anda __tag_0__ dan untuk Anda."
m "..."
bob "..."
scene waving_hand_with_cum_facial_shy
m "Saya bukan orang suci, Anda tahu? __Tag_0__girls juga memiliki beberapa pemikiran cabul ..."
m "Itu hanya ..."
scene waving_hand_with_cum_facial_shy_looking_aside
m "Kebanyakan pria hanyalah monyet terangsang ... __tag_0__Jika Anda memberi mereka sedikit menggoda ... __tag_0__ baik ..."
m "..."
bob "..."
scene waving_hand_with_cum_facial_grin_teasing
m "Nevermind ... __tag_0__com on, sudah membuat gambar, __ tag_0__ teruskan"
play sound "shot.mp3"
ms "..."
bob "Terima kasih..."
m "Ahah .__ tag_0__ dengan senang hati."
m "Dan coba tebak?"
ms "Bob menatapku dengan bertanya."
m "Kirimkan saya salinannya juga."
bob "..."
scene waving_hand_with_cum_facial_teasing
m "Ketika saya masturbasi malam ini, saya akan melihatnya."
bob "!!!"
m "Ya, anak perempuan juga melakukannya."
scene waving_hand_with_cum_facial_shy_looking_aside
m "Dan schlong Anda dan seluruh pengalaman ini ..."
scene waving_hand_with_cum_facial_shy
m "Itu sangat seksi."
bob "..."
ms "Bob membuka dan menutup mulutnya, tetapi tidak menjawab."
scene waving_hand_with_cum_facial_demanding
m "Oke, saya harus mencuci tangan."
m "Makan siang ada di atas meja."
m "Dan semoga harimu menyenangkan di tempat kerja."
ms "Aku menciumnya tapi lupa bahwa tanganku tertutup air mani."
scene mila_licking_cum_from_fingers
ms "Aku berhenti sejenak, dan kemudian menjilat telapak tanganku tepat di depannya"
bob "..."
ms "Kemaluannya menjadi keras lagi"
scene mila_licking_cum_from_fingers_smile
ms "Hehe .__ tag_0__ saya akan membiarkan Anda menghadapinya sendiri"
ms "Sial, aku pelacur ..."
"..."
scene black
"..."
if _in_replay:
    return



scene bg paul_and_bob_at_bar with fade
play music "bar.mp3"
p "..."
bob "..."
p "..."
bob "..."
p "Hmm..."
ps "Bob mengambil birnya dan menyesap diam -diam."
ps "Kami duduk seperti ini selama beberapa menit .__ TAG_0__ Saya telah berhasil minum segelas wiski dan menyeruput yang kedua."
ps "Terlepas dari kenyataan bahwa merokok dilarang di dalam, ada aroma rokok yang kuat di udara."
ps "Di belakang kami, beberapa pria berdebat tentang politik .__ tag_0__ suara keras mereka, kacamata dan botol dan tawa menyelimuti kami dalam tirai kebisingan."
ps "Membuat pertemuan kami sangat intim."
ps "Tapi percakapan itu masih tidak bisa dimulai."
p "..."
ps "Bob menulis kepada saya sore ini dan meminta untuk bertemu. Saya mengundangnya ke sebuah bar di dekat rumah saya."
ps "Tetapi setelah salam, kami hanya menyesap minuman kami dalam keheningan, terlalu malu untuk berbicara."
p "Haaaa ..."
ps "Saya menghembuskan napas dengan lelah."
ps "Rasanya jika saya tidak memulai percakapan, Bob hanya akan mabuk dan tertidur tepat di bar"
p "Jadi apa yang ingin Anda bicarakan?"
ps "Bob bergidik dan menatapku ketakutan."
ps "Keringat menutupi dahinya dan murid -muridnya melesat dari sisi ke sisi."
ps "Tetapi bahkan setelah satu menit dia masih tidak menjawab."
ps "Saya memutuskan untuk membantunya."
p "Jika ini tentang apa yang terjadi pagi ini, maka saya sudah tahu."
p "Mila memberitahuku segalanya."
ps "Bob menatapku dengan terkejut."
if dom >= mila_dom:
    p "Secara umum, akan lebih benar untuk mengatakan bahwa saya menyuruhnya melakukannya."
if mila_dom > dom:
    p "Saya tidak keberatan dengan apa yang dia lakukan. Justru sebaliknya."
bob "Erm ..."
ps "Bob menggaruk bagian atas kepalanya, bingung."
ps "Aku menghembuskan dan membungkuk siku di atas meja, memutar -mutar gelas wiski di tanganku."
p "Sulit dimengerti kan?"
ps "Bob hanya mengangguk sebagai tanggapan."
p "..."
p "Kamu tahu..."
p "Kami sudah bersama begitu lama, itu ..."
p "Tidak, bukan itu yang ingin saya katakan ..."
ps "Saya memutar gelas di tangan saya dan menunggu suara di belakangku menjadi lebih keras."
ps "Seolah takut orang lain akan mendengar kata -kata saya."
p "Ketika Anda sedang jatuh cinta, Anda ingin objek perasaan Anda menjadi sempurna."
p "Dalam segala hal."
p "Dan begitulah cara Anda melihatnya."
p "Ideal."
p "Pesenam, __ tag_0__ berkemauan keras dan indah, __ tag_0__ cerdas dan baik ..."
p "Perawan..."
ps "Bob tersenyum sedih."
bob "Satu -satunya hal yang cukup bagi saya adalah dia mencintaiku kembali."
ps "Saya mengangguk."
p "Untukku juga."
p "Tapi itulah yang membuat Anda melihatnya dengan cara yang berbeda."
p "Anda menipu diri sendiri karena Anda ingin ditipu."
p "Tetapi dalam kenyataannya dia akan sempurna, hanya dengan fakta bahwa dia mencintaimu"
p "Dan kamu mencintainya."
bob "Itulah yang saya tidak mengerti mengapa ..."
ps "Saya mengangkat tangan saya dalam gerakan berhenti."
p "Biarkan saya selesai."
bob "..."
bob "Bob segera terdiam."
p "Awalnya saya melihatnya sebagai gadis yang pemalu dan patuh."
p "Dan saya menyukainya."
p "Dan mengetahui bahwa dia menaruh topeng ini pada dirinya sendiri."
p "Karena itulah yang saya tunggu. Apa yang ingin saya dan semua orang di sekitar kita ingin lihat."
p "Ini adalah bagaimana koneksi dibentuk .__ tag_0__ kesetiaan Anda satu sama lain dan tekad untuk mengubah diri Anda untuk memenuhi harapan pasangan Anda mengikat Anda."
p "Tetapi jika Anda memikirkannya ...__ tag_0__ Anda berubah. Dan apa yang Anda suka berubah dengan Anda."
ps "Saya mengangkat gelas saya dan menyesap wiski dan memegang cairan yang mendidih di lidah saya."
ps "Menelan dan menghembuskan napas, saya melihat aroma kayu ek yang samar."
p "Ketika saya berusia 20 tahun, saya membenci wiski. Saya meminumnya hanya diencerkan dengan cola .__ tag_0__ tetapi dengan usia ... selera saya telah berubah."
bob "..."
p "Dan sama di sini .__ tag_0__ Saya menyukai fakta bahwa Mila adalah seorang gadis yang pemalu dan patuh .__ tag_0__ gadis saya."
p "Tapi saya hanya menyukainya karena saya merasa tidak aman."
p "Saya tidak yakin tentang dia."
p "Tapi seiring waktu ...__ tag_0__ menjadi membosankan."
bob "..."
p "Tentu saja, kami berbicara ...__ tag_0__ kami mencoba berbagai hal."
p "Tetapi kehidupan intim kita menjadi hambar."
p "Dan fantasi saya ...__ tag_0__ perselisihan di suatu tempat yang jauh."
p "Ini seperti ...__ tag_0__ Anda menonton film porno, brengsek untuk wanita lain, wanita bejat."
p "Dan Anda bahkan membayangkan diri Anda bersama mereka."
p "Tapi koneksi Anda dengan yang Anda cintai ...__ tag_0__ itu kehilangan ketegangan."
p "Itu mulai menjuntai di antara Anda, seperti rantai yang menghambat gerakan Anda."
p "Dan di suatu tempat pada saat ini topeng Anda mulai retak."
p "Dan Anda bertanya -tanya - apakah Anda mencintainya, atau topengnya?"
p "Anda menyadari bahwa Anda punya pilihan."
p "Anda dapat memenuhi fantasi Anda dengan orang lain."
p "Dan Anda harus mempertahankan penampilan perasaan sebelumnya .__ tag_0__ berbohong padanya .__ tag_0__ dan untuk diri sendiri."
p "Anda terbiasa berpura -pura."
p "Dan itu akan membuat cinta Anda platonik .__ tag_0__ hanya kepura -puraan"
p "Atau Anda akan menghancurkan hubungan Anda."
p "Tetapi Anda juga dapat mencoba ...__ tag_0__ untuk melakukan hal yang sama yang Anda lakukan di awal."
p "Bicara .__ TAG_0__ Lepaskan topeng Anda, paparkan kelemahan Anda, tampak rentan di depan satu sama lain."
p "Membiarkan diri Anda dicintai seperti .__ tag_0__ untuk mencintai manusia yang benar -benar lemah dan jelek di dalam .__ tag_0__ untuk membandingkan harapan."
p "Kami melepas topeng kami untuk memakai yang baru."
p "Mereka yang lebih sesuai dengan keinginan pasangan."
p "Mereka yang sesuai dengan situasi saat ini dengan cara terbaik."
ps "Saya melihat Bob."
p "Dan terkadang topeng pelacur itu paling sesuai dengan yang terbaik."
ps "Bob tidak mengalihkan pandangan dari botolnya, seolah -olah dia takut menatapku."
bob "..."
bob "Itu salah ..."
ps "Saya terkekeh."
p "Orang membuat aturan."
p "Aturan tentang apa yang salah dan apa yang benar."
p "Apa yang bisa dan tidak bisa Anda lakukan."
p "Aturan tentang apa yang dianggap curang."
p "Aturan tentang apa yang dianggap pengkhianatan."
bob "..."
p "Saya suka perubahan ini."
p "Mereka menghembuskan kehidupan ke dalam hubungan kita."
p "Mereka memberi saya kembali perasaan ...__ tag_0__ dari kesegaran ...__ tag_0__ dan gairah."
p "Saya bertanya -tanya seberapa jauh kita bisa pergi?"
p "Saya cemburu, __ tag_0__ ya .__ tag_0__ itu menyakitkan, __ tag_0__ benar."
p "Tapi pada saat yang sama ...__ tag_0__ Mila baru ini membuat saya seperti neraka."
bob "..."
p "..."
bob "..."
bob "Hidup Anda sangat sempurna sehingga saya ingin membunuh Anda dan merangkak ke kulit Anda."
p "..."
ps "Saya mencoba memahami apa yang saya dengar selama beberapa waktu, tidak tahu bagaimana harus bereaksi."
p "Saya ... Saya tidak yakin Anda bisa melakukan itu."
ps "Bob mengangguk dan menyesap birnya."
bob "Aku tahu."
bob "Saya terlalu gemuk."
p "..."
p "Ini bukan yang saya maksud ..."
ps "Saya masih tidak mengerti apakah dia bercanda atau serius."
bob "..."
p "..."
ps "Bob berdeham."
bob "Hmm..."
bob "Jadi itu artinya ... Anda tidak keberatan saya ... bahwa kami ... itu mila ..."
p "Ya. Saya tidak keberatan."
bob "..."
p "..."
bob "Apa lagi yang bisa saya lakukan padanya?"
p "..."
ps "Saya mengerutkan kening. Saya tidak suka apa yang dia katakan."
p "Apa maksudmu?"
p "She's human. She is not a thing that you can somehow \"use\"."
bob "Saya tidak bermaksud seperti itu ..."
bob "Maksud saya..."
bob "Apakah ada batasan?"
p "..."
ps "Saya tertelan."
ps "Setetes keringat dingin berlari di punggungku."
ps "Saya takut dengan pikiran saya, tetapi pada saat yang sama saya merasa lega."
ps "Seolah -olah kesadaran akan keinginan saya membebaskan saya."
p "Apapun yang dia inginkan."
bob "..."
p "..."
ps "Kami duduk untuk beberapa waktu dalam keheningan."
ps "Saya menyelesaikan wiski saya, menepuk punggungnya, dan pulang."
ps "Bob hanya mengangguk sebagai tanggapan dan memesan bir lagi."
ps "..."
stop music




label a125:
scene bg apartments with fade
show mila robe_puzzled_frown at right
ms "..."
ms "..."
show mila robe_puzzled:
    xzoom -1
    easein 0.7 xpos 0.25
"ketuk ketuk ketuk"
ms "..."
ms "..."
show mila robe_puzzled_frown:
    easein 0.7 xpos 0.95
"ketuk ketuk ketuk"
ms "..."
ms "..."
show mila robe_irritated_open_mouth:
    easein 0.7 xpos 0.55
"ketuk ketuk"
m "Haaaaa ..."
ms "..."
ms "Setelah blowjob, saya mandi. Kemudian akhirnya menghantam saya, apa yang sebenarnya terjadi sekarang."
ms "Atau lebih tepatnya, saya merasakannya lebih awal - saat saya melepas gugatan itu. __Tag_0__it sangat ketat, seperti kulit kedua."
ms "Dan begitu saya membebaskan diri dari itu ...__ tag_0__ saya menjadi diri saya lagi."
show mila robe_blush_shy_looking_aside
ms "Mila. Istri Paul. Istri yang mengisap tetangganya saat suaminya sedang bersiap -siap untuk bekerja ..."
ms "Kenangan menyapu di atas saya di mana dingin dan panas secara bersamaan."
ms "Panaskan dari peristiwa yang berkedip di depan mata saya, membangunkan nafsu dengan kesesatan mereka."
ms "Dingin karena takut akan konsekuensinya."
ms "Apa yang akan dikatakan Paul? __ tag_0__ Saya mengirim sms kepadanya, dan memberi tahu apa yang saya lakukan ..."
ms "Tapi yang dia jawab hanyalah "kita akan bicara di malam hari" ..."
ms "..."
show mila robe_irritated_open_mouth:
    easein 0.7 xpos 0.25
"ketuk ketuk ketuk"
ms "..."
show mila robe_iritated_atatata
ms "Aku benci saat dia melakukan itu ..."
ms "Apakah itu sulit untuk mengatakan apa yang Anda pikirkan segera?"
ms "Apakah perlu membuat saya khawatir?"
ms "..."
show mila robe_irritated_open_mouth:
    easein 0.7 xpos 0.95
"ketuk ketuk ketuk"
ms "..."
show mila robe_irritated_open_mouth:
    easein 0.7 xpos 0.55
"ketuk ketuk ketuk"
ms "..."
show mila robe_puzzled
ms "Mungkin saya harus bertemu dengannya dengan cara khusus?"
show mila robe_blush_smirk
ms "Untuk meringankan ketegangan ...__ tag_0__ bukan karena saya menginginkannya sendiri ..."
show screen nts_stats_overlay
menu:
    "Bagaimana saya harus menyapa Paul saat dia pulang?"
    "Dengan kepatuhan (kepatuhan Mila + 1)":
        $ dom += 1
        jump netorase_greetings_mila_sub
    "Take Control (dominasi Mila + 1)":
        $ mila_dom += 1
        jump netorase_greetings_mila_dom

label netorase_greetings_mila_sub:
show mila robe_shhhh_finger
ms "Dia mungkin akan menyukainya jika saya bertemu dengannya sebagai budak ..."
hide screen nts_stats_overlay
show mila robe_blush_smirk
ms "Pelacur budak ..."
ms "..."
ms "Hehe"
ms "Kunci pintu diklik."
ms "Aku buru -buru berlutut dan mengambil pose yang rendah hati."
scene mila_kneeling_robe
ms "Paul berjalan ke apartemen dan membeku sejenak."
p "..."
ms "Saya takut untuk melihat ke atas."
ms "Paul mendekat dan berdiri di depan saya."
p "..."
m "..."
p "Saya suka salam ini."
scene mila_kneeling_robe_light_smile
ms "Dadaku terasa hangat"
m "Saya senang ..."
p "Ngomong -ngomong, aku hanya minum dengan Bob."
scene mila_kneeling_robe_surprised
ms "Saya mengangkat kepala dengan terkejut."
p "Dia memanggil saya sendiri."
p "Bisakah kamu ..."
ms "Paul menyela dirinya dan menurunkan suaranya"
p "Bangun dan tuangkan saya teh. __Tag_0__Kami perlu bicara .__ tag_0__ dan saya pikir saya terlalu banyak minum."
jump netorase_greetings_continue
label netorase_greetings_mila_dom:
show mila robe_smile_awkward_angry
ms "Seringai jahat merayap ke wajahku"
hide screen nts_stats_overlay
ms "Mengapa saya harus repot? __ tag_0__ Dialah yang membuat saya khawatir."
ms "Sekarang gilirannya."
ms "Kunci pintu diklik."
show mila robe_curious
ms "Aku menyilangkan tangan di atas dadaku dan mengambil pose yang mengancam"
ms "Paul memperhatikan saya dan mengerutkan kening"
show paul suit_open_mouth_neutral at left
p "Bayi?"
p "Apakah ada yang salah?"
m "..."
ms "Aku terus diam -diam memelototinya."
ms "Mata Paul melesat."
show paul suit_sad
p "Em ..."
p "Maaf sudah terlambat? .."
ms "Mudah -mudahan dia menatapku."
p "Tidak, bukan itu masalahnya."
m "..."
ms "Sejujurnya, bahkan saya tidak tahu apa masalahnya .__ tag_0__ tapi dia harus sedikit berjuang juga .__ tag_0__ yang saya lakukan"
ms "..."
ms "Saya hanya ingin menggodanya."
show paul suit_open_mouth_blush
p "Hmm ...__ tag_0__ saya bertemu bob ...__ tag_0__ kami minum."
show mila robe_blush_shy_looking_aside
m "Apa?.."
ms "Semua kepercayaan diri saya yang berpura-pura menghilang."
ms "Saya tertelan."
m "Ayo, katakan padaku."
ms "Saya menarik Paul ke dapur."
label netorase_greetings_continue:
scene bg kitchen
ms "..."
ms "Paul memberi tahu saya tentang percakapannya dengan Bob."
ms "Kami berdua diam selama beberapa waktu."
ms "Paul meminum secangkir teh dan itu sedikit menenangkannya"
m "..."
show mila robe_puzzled at center
m "Jadi bagaimana menurut Anda? Bagaimana perasaannya ...__ tag_0__ tentang semua ini?"
ms "Paul menatapku dan mengangkat bahu."
show paul suit_open_mouth_neutral at left
p "Sulit dikatakan. Tampak bagi saya bahwa dia bingung, dan dia berusaha memahami apa yang lebih kuat - hati nuraninya atau nafsu."
ms "Aku mengangguk dengan serius, tetapi tidak tahu harus berkata apa."
ms "Kepalaku dipenuhi dengan koktail pikiran dan keinginan yang aneh."
ms "Tapi satu perasaan paling menonjol .__ tag_0__ kecemasan."
ms "Ini tidak seperti saya tidak ingin tahu tentang apa yang dipikirkan Bob ..."
ms "Saya hanya ingin tahu apa yang dipikirkan Paul tentang apa yang terjadi pagi ini lebih dari apa pun."
ms "Saya ingin melihat reaksinya. Rasakan koneksi kami."
ms "Dan menilai dari wajahnya yang khawatir, Paul memikirkan hal yang sama."
show paul suit_blush_looking_aside
p "..."
p "Hmm..."
ms "Paul berdeham."
show paul suit_open_mouth_blush
p "Jadi ...__ tag_0__ tentang apa yang terjadi pagi ini ..."
ms "Saya merasa seperti musim semi yang melingkar."
ms "Koneksi Paul dan aku semakin kencang, dengan menyakitkan menguras kepercayaan diri dariku."
show mila robe_sad
ms "Sepertinya saya mulai secara fisik merasakan ketegangan ini .__ tag_0__ dan itu membuat tubuh saya mendambakan perhatian Paul lebih dari sebelumnya."
ms "Saya ingin meringkuk padanya, __ tag_0__ mencium aroma oranye-cinnamon dari cologne-nya .__ tag_0__ merasakan elastisitas tubuhnya .__ tag_0__ dan kehangatannya."
ms "Saya ingin memastikan ... __tag_0__ bahwa dia masih mencintaiku .__ tag_0__ bahkan setelah apa yang saya lakukan .__ tag_0__ bahkan mengetahui apa yang akan saya lakukan."
show paul suit_sad
p "I ...__ tag_0__ Saya pikir hal ini, itu terjadi di pagi hari ...__ tag_0__ bukan itu yang saya inginkan ..."
show mila robe_sad_tears
ms "Dari kata -kata dan suasana hati pertama Paul, saya sudah tahu apa yang ingin dia katakan."
ms "Bahwa inilah yang paling saya takuti ..."
ms "Harapan saya hancur."
ms "Kebanggaan dan kepercayaan diri saya menguap .__ tag_0__ Saya siap melakukan apa saja untuk memenangkan kasih sayangnya."
ms "Sepertinya seluruh hidup saya berkedip di depan mata saya .__ tag_0__ pikiran saya memberi saya ratusan opsi tentang apa yang bisa saya katakan, __ tag_0__ apa yang harus saya katakan."
ms "Tapi saya tidak suka mereka."
ms "Kebencian dan ketakutan menyakiti saya hampir secara fisik .__ tag_0__ air mata berkumpul di mata saya .__ tag_0__ dan tidak peduli seberapa keras saya mencoba - saya tidak bisa menelan benjolan di tenggorokan saya"
ms "Dengan tangan gemetar, aku mengambil tangan Paul dan menyentuhnya dengan bibirku."
scene mila_kiss_pauls_hand
p "..."
ms "Sesaat kemudian saya merasakan sentuhan lembut di kepala saya."
ms "Saya tidak langsung berani mengangkat kepala, tetapi ketika saya akhirnya melakukannya, saya melihat Paul menatap saya dengan terkejut."
scene bg kitchen
show paul suit_open_mouth_neutral at left
p "..."
show mila robe_sad_tears at center
p "Apa yang sedang kamu lakukan?"
ms "Saya tidak bisa mengatakan sepatah kata pun dan hanya menutup mata dan menggelengkan kepala."
ms "Saya berharap dia tidak akan meninggalkan saya ..."
ms "Saya tidak bisa membayangkan hidup saya tanpa dia ..."
m "..."
p "..."
p "Nah ... yang saya maksud adalah, bahwa saya tidak suka hal -hal yang Anda lakukan adalah tersembunyi ..."
ms "Saya merasakan kegugupannya. Paul membuat jeda, mencoba mengumpulkan pikirannya"
p "Maksud saya ...__ tag_0__ saya suka ketika Anda memberi tahu saya apa yang Anda lakukan ...__ tag_0__ tapi, __ tag_0__ Saya ingin melihatnya juga ..."
if dom >= mila_dom:
    show paul suit_smirk
    p "Saya ingin memberi tahu Anda apa yang harus dilakukan. Saya ingin melatih dan membimbing Anda tentang cara menjadi pelacur yang ideal untuk saya ..."
    ms "Paul menatapku dengan percaya diri"
    ms "Suaranya terdengar dengan cara yang memerintah yang membuatku menggigil belakangan ini."
    ms "Saya melihat ke bawah dan mencoba menenangkan hati balapan saya."
    show mila robe_worried_open_mouth_wait
    m "..."
    ms "Saya ingin merasakan kekuatannya atas saya."
    ms "Saya ingin merasakan keinginan dan hasratnya."
    ms "Ketika saya tunduk pada keinginannya yang sesat, saya merasa seperti saya terjun ke kedalaman kesadarannya."
    ms "Saya menyesuaikan diri dengan persyaratannya, menebak apa yang dia inginkan."
    ms "Saya melihat sisi rentannya .__ tag_0__ saya menariknya .__ tag_0__ saya diserap olehnya."
    ms "Dan saya bisa menyakitinya dengan bereaksi secara berbeda dari yang dia harapkan."
    ms "Dia tidak bisa memaksa saya untuk melakukan apa pun .__ tag_0__ Saya mematuhi perintahnya hanya karena saya ingin."
    ms "Kemungkinan penolakan mengancamnya .__ tag_0__ dan itu memberi saya kekuatan."
    ms "Jadi siapa yang bertanggung jawab? __ tag_0__ orang yang memberi perintah? __ tag_0__ atau orang yang mematuhi?"
    m "..."
    m "Apa ... __tag_0__ Apa yang Anda ingin saya lakukan? ..__ tag_0__ master ..."
    ms "Sangat mudah untuk mengatakan .__ tag_0__ Kata ini pas, seolah -olah seharusnya ada."
    ms "Master ...__ tag_0__ bahkan memikirkannya membuat saya menggigil."
    ms "Setelah mengatakan ini, seolah -olah saya telah membuka pintu ke sudut -sudut tersembunyi pikiran saya."
    ms "Bagian -bagian dari saya yang saya coba kontrol dengan sekuat tenaga, __ tag_0__ mencoba menahannya dan menyembunyikannya."
    ms "Dan apa yang terkunci di dalam mulai mengatasiku .__ tag_0__ itu menangkap kesadaranku."
    ms "Itu menjadi bagian dari diriku .__ tag_0__ setiap langkah sesat selanjutnya membuka pintu ini lebih jauh."
    ms "Dan saya tidak lagi yakin bahwa saya akan dapat menutupnya."
    ms "Belum lagi, __ tAG_0__ yang tidak saya inginkan."
    show paul suit_grin
    p "..."
    ms "Paul menyukai bagaimana saya memanggilnya dan menyeringai."
    p "Saya pikir Anda harus berbicara dengan Bob."
    m "..."
    show mila robe_puzzled_frown
    m "Tapi ... kamu bilang kamu ingin melihat ..."
    show paul suit_smirk
    p "Ya .__ tag_0__ Tapi saya pikir Bob belum siap untuk pengalaman ini ...__ tag_0__."
    ms "Saya mengangguk."
    p "Karena itu, tugas Anda adalah menuntunnya ke ini."
    m "..."
    show mila robe_blush_smirk
    m "Pimpin dia, ya"
    m "Tapi ...__ tag_0__ bagaimana saya bisa melakukan ini?"
    ms "Paul mengangkat bahu."
    p "Tidak tahu. Pikirkan sesuatu. Tawarkan sesuatu sebagai imbalan, misalnya."
    show mila robe_think
    m "..."
    m "..."
    show mila robe_shhhh_finger
    m "Bagus..."
    p "..."
    ms "Suara bukaan pintu yang teredam terdengar dari balik dinding. Bob pulang."
    ms "Paul dan saya saling memandang."
    m "..."
    p "..."
    show mila robe_worried_open_mouth_wait
    m "Saya mungkin harus pergi dan berbicara dengannya, kan?"
    p "Ya."
    ms "Saya memandang diri saya sendiri dan memperlancar kerutan yang tidak ada pada jubah saya."
    m "Apakah saya terlihat baik -baik saja?"
    p "..."
    p "Tidak .__ tag_0__ Anda terlihat panas."
    show mila robe_worried_open_mouth_wait
    m "..."
    m "Terima kasih."
    scene bg door
    ms "Aku berjalan ragu -ragu menuju pintu keluar."
    ms "Sudah di pintu Paul memanggilku."
    show mila robe_from_behind_looking
    ms "Saya berbalik."
    p "Saat Anda kembali, kejutan kecil akan menanti Anda."
    ms "Nada suaranya tidak meninggalkan keraguan tentang sifat kejutan yang dia bicarakan."
    ms "Saya merasa panas."
    ms "Aku bertanya -tanya dengan apa dia muncul?"
    show mila robe_from_behind_not_looking
    ms "Saya menelan dan berjalan ke kesejukan koridor."
    jump netorase_talking_after_blowjob_continue

show paul suit_smirk
p "Saya ingin melihat Anda, saat Anda berada di ...__ tag_0__ mode nakal .__ tag_0__ dengan orang lain ..."
ms "Paul terdiam, malu."
ms "Saya menunggu sedikit, memberinya waktu untuk mengumpulkan pikirannya."
ms "Tetapi dengan setiap saat yang lewat saya menjadi tidak sabar"
ms "Dan keinginan untuk menggodanya."
show mila robe_blush_smirk
m "Jadi Anda ingin melihat bagaimana mulut kecil saya mengisap penis pria lain?"
ms "Paul tidak menjawab."
ms "Aku mendekatinya dan mengangkat wajahnya di dagu."
scene mila_dominant_face
ms "Wajahnya yang malu membangkitkan sesuatu dalam diri saya."
ms "Sesuatu yang agresif, tetapi tidak jahat."
ms "Keinginan untuk mengontrol ...__ tag_0__ untuk menaklukkan ...__ tag_0__ untuk menggoda ..."
ms "Saya tidak tahu bagaimana menggambarkan perasaan ini."
ms "Itu adalah sesuatu yang sulit dipahami .__ tag_0__ keinginan untuk menimbulkan rasa sakit demi kesenangan."
ms "Rasa sakitnya dapat bervariasi .__ tag_0__ tidak harus fisik."
ms "Saya ingin merasakan kerendahan hati .__ tag_0__ keinginannya untuk mengikuti keinginan saya."
ms "Kenikmatan dan kekagumannya pada sisi saya yang paling menjijikkan."
m "Betapa nakal ..."
ms "Kata -kata yang tepat muncul entah dari mana .__ tag_0__ Saya hanya tahu apa yang harus saya katakan .__ tag_0__ karena saya mengatakan semua yang saya inginkan. Tanpa menahan diri."
ms "Setelah mengatakan ini, seolah -olah saya telah membuka pintu ke sudut -sudut tersembunyi pikiran saya."
ms "Bagian -bagian yang saya coba untuk tidak dikeluarkan."
ms "Dan apa yang terkunci di dalam mulai mengatasiku. Menangkap kesadaran saya."
ms "Itu menjadi bagian dari diriku. Setiap langkah sesat selanjutnya membuka pintu ini lebih jauh."
ms "Dan saya tidak lagi yakin bahwa saya akan dapat menutupnya."
ms "Belum lagi saya tidak mau."
ms "Saya ingin menjadi berbeda .__ tag_0__ menjadi diri saya yang sebenarnya. __Tag_0__ tanpa mengabaikan, tanpa menyangkal bagian -bagian saya yang terkunci di dalam."
ms "Terkunci di bawah moralitas, pendidikan, tradisi ... akal sehat."
ms "Saya ingin Paul melihat bagian saya ini .__ tag_0__ Saya ingin dia menyukainya .__ tag_0__ Saya ingin dia mencintaiku apa pun yang terjadi."
ms "Terlepas dari hal -hal yang paling menjijikkan yang akan saya lakukan .__ tag_0__ kepadanya .__ tag_0__ untuk kami."
m "..."
ms "Suara bukaan pintu yang teredam terdengar dari balik dinding. Bob pulang."
ms "Saya ingin bermain dengan Paul lagi, tetapi suara ini memberi saya ide lain"
scene bg kitchen with fade
show mila robe_blush_smirk
m "Lepaskan pakaian Anda dan tunggu saya di sini. Saya perlu berbicara dengan kekasih saya."
show paul suit_blush_looking_aside at left
ms "Paul memerah, baik dari rasa malu atau kemarahan."
ms "Saya hanya menyeringai pada reaksinya."
ms "Tapi kemudian wajahnya menjadi cerah, seolah -olah dia telah mengingat sesuatu."
ms "Seringai lucu merayap ke wajahnya."
show paul suit_smirk
p "Oke, mam ..."
show mila robe_puzzled_frown
ms "Saya mengerutkan kening."
m "Apakah ada yang salah?"
p "Tidak ... Saya hanya ingat sesuatu. Saya akan menunjukkan kepada Anda saat Anda kembali."
m "..."
ms "Saya penuh dengan rasa ingin tahu, tetapi saya memutuskan bahwa sedikit kejutan tidak akan memperburuknya."
ms "Jadi saya menuju ke pintu."
scene bg door
p "Selamat bersenang-senang."
show mila robe_from_behind_not_looking
ms "Aku membeku sebentar, untuk beberapa alasan yang ketakutan dengan nada mengejek dalam suaranya."
ms "Tetapi tidak tahu apa yang harus dijawab, saya hanya berterima kasih padanya dan pergi ke kesejukan koridor."

label netorase_talking_after_blowjob_continue:
scene bg bobs_apartments_clean with fade
ms "Meskipun saya memiliki kunci, saya merasa itu benar untuk mengetuk daripada membuka pintu sendiri."
ms "Bob segera membukanya."
ms "Bau alkohol yang gigih menghantam hidungku, dan penisnya yang ereksi menarik perhatian saya."
show bob nude_flaccid_drunk at right:
    ypos 1.05
ms "Bob benar -benar telanjang."
ms "Dia meraih tanganku dan menarikku ke dalam."
show mila robe_holding_hand_open_mouth_blush2 at left
m "W-apa? Wait!"
scene bob_kiss_mila_forced
ms "Pintu apartemen menabrak saya. Bob menekanku ke pintu dan menciumku dengan paksa."
ms "Tangannya mulai meraba -raba tubuhku dengan rakus."
ms "Tekanannya yang tiba -tiba dan perilaku yang kurang ajar membuat saya marah."
ms "Saya meletakkan siku di pintu dan mendorongnya menjauh dari saya dengan sekuat tenaga."
ms "Saya tidak yakin usaha saya menggerakkannya bahkan satu inci."
ms "Tapi, merasakan perlawanan saya, dia menarik diri dengan terkejut dan menatap saya dengan tatapan yang diselingi oleh alkohol."
scene bg bobs_apartments_clean
show mila robe_iritated_atatata at left
m "Apa -apaan, Bob!"
show bob nude_flaccid_drunk at right:
    ypos 1.05
ms "Dia mengerutkan kening dan mundur selangkah."
bob "Apakah saya melakukan sesuatu ... Hic ... salah?"
m "..."
m "Apakah Anda melakukan sesuatu yang salah? Apa -apaan?"
ms "Untuk beberapa alasan perilakunya membuatku takut. Saya segera kehilangan kendali atas apa yang terjadi."
ms "Lidahnya meledak ke dalam mulut saya dengan begitu cepat dan tidak terduga sehingga saya merasa diperkosa."
ms "Tubuh saya menjadi sensitif, tetapi tidak dalam arti vulgar .__ tag_0__ justru sebaliknya .__ tag_0__ Tampak bagi saya bahwa semuanya ditutupi dengan jarum."
ms "Sentuhan apa pun menyebabkan kekesalan ... dan ketakutan."
show mila robe_irritated_open_mouth
m "..."
bob "P-paul berkata ...__ tag_0__ hic ...__ tag_0__ bahwa saya dapat melakukan apapun ...__ tag_0__ hic ...__ tag_0__ saya ingin ..."
show mila robe_smile_awkward_angry
m "Oooh, benarkah? __ tag_0__ itu sangat manis! __ tag_0__ tapi bukankah kalian berdua, aku tidak tahu, tanyakan dulu?"
bob "..."
ms "Bob mengerutkan kening."
show bob nude_flaccid_frown
bob "B-tapi ... kaulah ..."
ms "Saya mengganggu gumamannya yang tidak jelas."
m "Yes. I started it myself. But that doesn't mean you can do whatever you want with me, just because \"Paul said it\""
ms "Bob membungkuk dan tampaknya menjadi lebih kecil."
show bob nude_flaccid_sad
bob "Saya melihat ...__ tag_0__ hic ..."
ms "Suaranya terdengar tidak menyedihkan, tapi acuh tak acuh .__ tag_0__ seolah -olah dia tahu ini akan terjadi .__ tag_0__ dia berbalik dariku dan berjalan menuju kamar tidur."
show bob nude_from_behind
show mila robe_worried_open_mouth_wait
ms "Sosoknya yang membungkuk tidak membangkitkan apa pun selain kasihan."
ms "Semakin jauh dia pindah, semakin tenang dan lebih aman yang saya rasakan."
ms "Dan semakin jelas bagi saya bahwa saya terlalu keras."
m "Tunggu..."
show bob nude_from_behind_looking_back_sad
ms "Bob berhenti dan berbalik .__ tag_0__ penisnya digantung seperti sosis tanpa bentuk di antara kakinya .__ tag_0__ dan saya harus berusaha untuk tidak melihat ke bawah."
bob "Apa? __ tag_0__ hic ..."
ms "Suaranya terdengar kering, hampir keras."
m "..."
ms "Saya mencoba menemukan kata -kata, tetapi saya masih tidak bisa merumuskan apa yang ingin saya katakan."
m "Saya ... Saya merasa menyesal ..."
show bob nude_flaccid_angry
ms "Bob tidak membiarkan saya selesai."
ms "Matanya berkedip dengan kemarahan."
bob "Anda minta maaf? Jangan mengasihani saya!"
ms "Saya terkejut dengan agresi mendadak dan ingin mundur, tetapi saya menyadari punggung saya masih beristirahat di pintu."
bob "Anda selamanya minta maaf .__ tag_0__ Anda semua selalu berbicara dengan saya karena kasihan."
bob "Sepertinya Anda membantu saya."
bob "Saya tidak pernah meminta untuk diselamatkan."
show mila robe_puzzled_frown
m "Saya tidak..."
show bob nude_flaccid_sad
bob "Hentikan sudah .__ tag_0__ cukup."
show mila robe_sad
m "..."
ms "Saya tidak tahu bagaimana menjawab .__ tag_0__ Kemarahan melonjak di Bob sehingga dia berhenti hiccuping dan tampak sadar."
bob "Mengapa semua orang di sekitar melakukan apa pun yang mereka inginkan dan tidak peduli dengan pendapat saya?"
bob "Mengapa Anda selalu memutuskan untuk saya?"
bob "Mengapa saya harus selalu memikirkan apa yang diinginkan orang lain?"
bob "Bagaimana dengan apa yang saya inginkan?"
show mila robe_worried_open_mouth_wait
m "..."
ms "Suaranya menghantam saraf saya seperti palu derik .__ tag_0__ Saya menundukkan kepala, melawan rasa malu."
bob "Anda tidak memberi saya hak untuk pergi, __ tag_0__ Anda mulai memanipulasi saya dan mendorong saya ke arah yang cocok untuk Anda."
bob "Tapi Anda hanya memanjakan keinginan Anda, bukan?"
bob "Anda tidak peduli tentang saya .__ tag_0__ Anda tidak peduli tentang pikiran dan perasaan saya."
m "..."
ms "Kebencian terbakar di tenggorokan saya, mata saya berair dan gatal. Saya hampir tidak bisa menahan diri untuk tidak menangis."
ms "Karena saya tahu .__ tag_0__ dia benar."
m "..."
bob "Cukup .__ tag_0__ Saya sudah selesai dengan itu."
show mila robe_from_behind_not_looking
ms "Saya tidak tahan lagi .__ tag_0__ Saya berbalik untuk pergi dan meraih pegangan pintu."
ms "Nyali saya menuntut untuk dengan cepat meninggalkan ruangan ini .__ tag_0__ untuk melarikan diri."
ms "Tidak ada yang ingin menjadi orang jahat .__ tag_0__ dan saya sudah menemukan ratusan alasan untuk diri saya sendiri."
ms "Itu untuk keuntungan Bob .__ tag_0__ bahwa dia pasti menikmatinya .__ tag_0__ bahwa dia bisa menolaknya kapan saja."
ms "Tapi saya tahu itu semua bohong."
ms "Dan itu membuat saya merasa lebih tersinggung .__ tag_0__ bahkan lebih menyakitkan."
show mila robe_from_behind_looking
m "..."
ms "Jika saya pergi sekarang, saya hanya akan membuktikan kepadanya bahwa dia benar."
ms "Apa yang akan dia lakukan setelah ini?"
m "..."
ms "Apa yang akan saya lakukan dan bagaimana perasaan saya sesudahnya? Bisakah saya berpura -pura tidak ada yang terjadi?"
ms "...__ tag_0__ no .__ tag_0__ tentu saja tidak."
m "..."
show mila robe_puzzled_frown
ms "Aku melepaskan pegangan dan berbalik, untuk menghadapi Bob."
m "Saya ... Maaf."
ms "Suaraku gemetar dan terdengar tenang dan lemah."
ms "Bob menghela nafas."
bob "Saya tidak perlu permintaan maaf Anda .__ tag_0__ Saya ingin dibiarkan sendiri."
m "..."
show mila robe_puzzled
m "Tampaknya bagi saya bahwa baru -baru ini Anda menginginkan sesuatu yang berbeda ..."
bob "Apakah Anda akan berpura -pura peduli lagi?"
m "..."
show mila robe_smile_awkward_angry
m "..."
ms "Tunggu sebentar ... pada titik apa ini menjadi pengadilan saya?"
ms "Saya seharusnya tidak merasa bersalah karena takut."
ms "Kata -kata Bob mencerminkan perasaannya .__ tag_0__ sederhana dan jujur, seperti remaja."
ms "Dia masih melihat dunia dalam warna hitam dan putih .__ tag_0__ dan dia menolak untuk tumbuh dewasa."
ms "Menolak untuk melihat sesuatu yang kurang dari sempurna .__ tag_0__ sesuatu yang bertentangan .__ tag_0__ sesuatu seperti manusia."
ms "Tidak ada halftones di dunianya .__ tag_0__ Dia melindungi dunia ini, menghargainya .__ tag_0__ karena melindunginya dari kenyataan menjijikkan."
ms "Sebuah kenyataan di mana semuanya dicat abu -abu gelap."
ms "Saya tidak bisa menahan diri .__ tag_0__ Saya merasa kasihan padanya .__ tag_0__ meskipun dia tidak menyukainya."
ms "Tapi ini bodoh .__ tag_0__ Anda tidak dapat menilai seseorang atas perasaan mereka .__ tag_0__ kami tidak dapat memilih apa yang kami rasakan .__ tag_0__ kami hanya merasakan."
ms "Dan yang kami lakukan hanyalah mencoba menemukan alasan yang masuk akal mengapa."
show mila robe_worried_open_mouth_wait
m "Bob ..."
show bob nude_flaccid_crossed_arms
ms "Dia menyilangkan tangan di dadanya dan berbalik."
ms "Seperti anak kecil ..."
show mila robe_irritated_open_mouth
m "Saya tidak bermaksud menyinggung perasaan Anda .__ tag_0__ tetapi Anda tidak melihat saya sebagai pribadi sama sekali pada saat itu .__ tag_0__ Anda ingin menggunakan saya seperti sesuatu."
ms "Bukannya aku menentangnya ...__ tag_0__ tapi ini membutuhkan suasana hati yang berbeda."
ms "Saya memutuskan untuk tidak memberitahunya ini ...__ tag_0__ untuk saat ini."
bob "Tapi kamu ..."
m "Ya."
ms "Saya mengganggu dia lagi."
m "Ya, saya melakukan apa yang saya inginkan .__ tag_0__ tetapi saya tidak ingat bahwa setidaknya sekali saya memaksa Anda untuk melakukan sesuatu."
ms "Bob memalingkan muka dan meringis .__ tag_0__ dia mungkin melihatnya secara berbeda."
ms "Saya menghela nafas."
m "Dengar, saya tidak menentang tampilan ...__ tag_0__ kelembutan dari Anda."
show bob nude_bigger_penis_crossed_arms_shock
ms "Bob memelototiku. Penisnya berkedut dan mulai dipenuhi dengan darah."
ms "Saya hampir tidak bisa menahan diri untuk tidak menatapnya."
m "Semuanya hanya memiliki tempat, waktu, dan suasana hatinya ..."
bob "..."
show bob nude_bigger_penis_crossed_arms_frown
bob "Anda dan hanya Anda yang akan memutuskan semuanya, rupanya?"
if mila_dom >= dom:
    show mila robe_blush_smirk
    m "Dan bukankah itu yang Anda inginkan?"
    bob "..."
    ms "Bob mengangkat satu alis dengan skeptis."
    m "..."
    ms "Kapan dia menjadi begitu sombong?"
    m "..."
    show mila robe_proud
    m "Oke, mari kita lakukan dengan cara ini. Kami akan bertukar persyaratan."
    jump netorase_talking_with_Bob_after_blowjob_continue

show mila robe_worried_open_mouth_wait
ms "Saya memalingkan muka."
ms "Saya tidak ingin menjawab pertanyaan ini .__ tag_0__ Saya tidak ingin mengatakannya dengan keras."
ms "Saya takut dia akan mengambil kata -kata saya secara tidak benar."
ms "Saya benar -benar tidak ingin memutuskan apa pun .__ tag_0__ Saya merasa sangat nyaman ketika Paul memberi tahu saya apa yang harus dilakukan."
ms "Saya tidak ingin bertanggung jawab atas pilihan saya."
ms "Saya tidak ingin menjadi gadis yang baik .__ tag_0__ Saya ingin menjadi gadis yang buruk."
ms "Gadis yang sangat buruk."
ms "Tapi pada saat yang sama, saya tidak ingin merasa seperti itu saya ..."
ms "Saya ingin merasa seperti saya dipaksa untuk melakukan ini ...__ tag_0__ bahwa saya dikendalikan oleh orang lain."
ms "Tapi saya tidak bisa mengatakannya dengan keras ..."
m "..."
bob "Saya tahu itu."
ms "Bob menghela nafas dengan sedih."
m "TIDAK..."
ms "Saya entah bagaimana memerasnya sendiri .__ tag_0__ Saya tidak ingin membicarakan topik ini .__ tag_0__ Saya tidak ingin mengakuinya."
ms "Tapi saya harus."
ms "Karena itulah yang diinginkan Paulus."
ms "Pikiran terakhir memberi saya kekuatan dan kepercayaan diri."
show mila robe_blush_smirk
ms "Ya .__ tag_0__ Paul menyuruh saya berbicara dengan Bob .__ tag_0__ ini adalah kehendaknya .__ tag_0__ Saya harus melakukannya."
m "Tidak ada bob .__ tag_0__ saya tidak akan menjadi satu -satunya yang memutuskan"
ms "Saya akhirnya bisa mengatakannya lebih kuat .__ tag_0__ Bob menatap saya dengan menarik."
m "Saya ingin menawarkan Anda ...__ tag_0__ Kondisi lain ..."

label netorase_talking_with_Bob_after_blowjob_continue:
bob "Kondisi?"
show mila robe_proud
m "Ya."
ms "Bob mengerutkan kening."
m "Tiga kondisi dari saya .__ tag_0__ tiga kondisi dari Anda."
bob "Kondisi untuk apa?"
ms "Saya menelan benjolan di tenggorokan saya dan mencoba terlihat percaya diri sebanyak yang saya bisa."
m "Tiga kondisi untuk melakukannya lagi."
bob "..."
m "..."
bob "Lakukan? Lakukan apa?"
ms "Aku mengerutkan bibirku dengan tidak senang."
show mila robe_holding_hand_open_mouth_blush3_looking_aside
m "Jangan membuat saya mengatakannya dengan keras .__ tag_0__ Saya juga tidak nyaman, sial! __ tag_0__ Saya tidak pernah melakukan hal seperti ini, apa yang Anda inginkan dari saya?"
ms "Bob agak terkejut dengan teguran saya dan tidak menjawab."
bob "..."
show mila robe_proud
m "Hmm..."
ms "Saya batuk di tangan saya, mendapatkan kembali ketenangan saya."
m "Saya ingin ... hubungan kami memiliki dampak positif pada kami berdua."
m "Karena itu, kondisi pertama saya adalah saya ingin Anda memiliki hobi kreatif."
ms "Bob segera tenggelam."
bob "Untuk apa? __ tag_0__ Saya seorang pecundang .__ tag_0__ Saya mencoba menggambar, memahat, membuat game, menulis lagu - saya mengerikan .__ tag_0__ Saya tidak akan pernah menjadi layak."
ms "Saya hanya tersenyum hangat sebagai tanggapan."
show mila robe_smile_open_mouth
m "Kreativitas bukan tentang menjadi lebih baik dari yang lain."
m "Kreativitas adalah tentang mengekspresikan diri Anda, __ tag_0__ membantu diri sendiri dan orang lain memahami orang seperti apa Anda."
m "Anda dapat membuat sesuatu, bahkan jika tidak ada yang akan melihatnya."
show bob nude_bigger_penis_crossed_arms_warm_smile
bob "..."
ms "Bob tersenyum sesaat, tapi kemudian mengerutkan kening lagi."
show bob nude_bigger_penis_crossed_arms_frown
bob "Sekali lagi! __ tag_0__ Anda melakukannya lagi! __ tag_0__ Saya menolak karena saya ingin menolak .__ tag_0__ Saya tidak ingin membuang waktu untuk ini."
show mila robe_curious
ms "Aku melipat tanganku di atas dada."
m "Pertama -tama, Anda tidak menolak .__ tag_0__ kedua, ini adalah kondisi saya .__ tag_0__ tetapi Anda dapat mengedepankan Anda untuk menebusnya .__ tag_0__ belajar untuk bernegosiasi, bukan menolak."
ms "Bob menghela nafas."
bob "Mengapa Anda ingin saya memiliki hobi?"
ms "Saya mengangkat bahu dan terkekeh."
m "Hanya karena .__ tag_0__ inilah yang saya inginkan .__ tag_0__ Ini adalah kemauan saya .__ tag_0__ Anda tahu, cukup menyenangkan menginginkan sesuatu dan melakukan sesuatu untuk mencapainya."
ms "Bob menurunkan matanya."
bob "Ya. Itu pasti bagus ..."
ms "Suaranya terdengar kusam dan tak bernyawa."
m "..."
show mila robe_blush_smirk
m "Jadi? Apa kondisi Anda?"
bob "Saya tidak punya. Saya tidak ingin memikirkannya."
bob "Mimpi adalah untuk mereka yang berbakat .__ tag_0__ untuk orang -orang seperti saya ... sulit untuk memiliki mimpi."
ms "Bob menjawab setelah jeda singkat .__ tag_0__ tapi saya tidak suka jawabannya."
show mila robe_irritated_open_mouth
m "Saya tidak bertanya apa yang tidak Anda inginkan .__ tag_0__ Saya bertanya apa kondisi Anda? __ tag_0__ Apa yang Anda inginkan, Bob?"
ms "Bob mengangkat tangannya dan memelototiku selama beberapa detik."
ms "Saya tidak memalingkan muka dan bahkan tidak berkedip."
bob "Saya ingin Anda melepas pakaian Anda."
ms "Dari sudut mata saya, saya melihat penisnya yang besar bergoyang di udara"
ms "Sial, saya tidak keberatan melepas pakaian saya sendiri ..."
ms "Tapi saya perlu mengikuti aturan .__ tag_0__ jika tidak saya akan kehilangan kendali lagi .__ tag_0__ dan semua ini akan berubah menjadi pengalaman menjijikkan di mana saya akan merasa digunakan dan diperkosa."
ms "Aku mengangguk perlahan, mengawasi Bob, seolah -olah takut jika aku kehilangan pandangannya untuk sesaat, dia akan bergegas ke arahku."
m "Baik .__ tag_0__ segera setelah Anda memenuhi kondisi saya, __ tag_0__ Saya akan menanggalkan pakaian."
ms "Bob terkejut pada awalnya .__ tag_0__ kemudian dia mencerahkan, dan kemudian mengerutkan kening lagi."
bob "Apa maksudmu? Apa yang perlu saya lakukan secara spesifik?"
show mila robe_think
ms "Suaranya terdengar terputus -putus, serak dan rendah. Dia hampir tidak bisa menahan kegembiraannya."
ms "Dan saat ini menakutkan dan mengasyikkan."
ms "Saya menjawab dengan tenang, tidak menunjukkan kegembiraan saya, agar tidak memicu dia lebih banyak lagi."
show mila robe_irritated_open_mouth
m "Saya akan menanggalkan pakaian ketika Anda menunjukkan kepada saya apa yang Anda buat dengan tangan Anda sendiri."
ms "Bob meremehkan."
bob "Tidak .__ tag_0__ ini tidak akan berhasil .__ tag_0__ Anda dapat mengatakan saya tidak melakukan cukup usaha atau semacamnya .__ tag_0__ Bagaimana saya tahu jika saya menjaga sisi kesepakatan saya?"
ms "Dia mengatakannya dengan jelas dan tegas .__ tag_0__ Saya menyadari bahwa saya tidak mungkin dapat meyakinkannya dan sudah mulai datang dengan solusi."
ms "Tapi Bob mengalahkanku untuk itu."
show bob nude_bigger_penis_crossed_arms_smirk
bob "Saya akan mulai menggambar .__ tag_0__ dan Anda akan berpose untuk saya .__ tag_0__ telanjang."
show mila robe_puzzled
ms "Saya tertelan."
ms "Saya merasa tidak bisa menolak."
ms "Jadi saya mengangguk ragu -ragu."
m "Kesepakatan..."
bob "..."
bob "Apa selanjutnya?"
m "Erm ..."
ms "Saya agak terkejut dengan tekanannya, tetapi mencoba menyatukan diri dan terlihat percaya diri."
show mila robe_proud
m "Kondisi kedua ..."
show mila robe_think
ms "Sayang sekali saya tidak memikirkan hal ini sebelumnya ..."
ms "Kontolnya masih bergoyang di udara, terus -menerus menarik perhatian. Aku bisa dengan jelas mencium aroma musky -nya."
ms "Dan itu membawa kembali kenangan tentang apa yang terjadi pagi ini."
ms "Mulutku dipenuhi air liur. Seolah -olah takut monster ini akan mulai menabrak tenggorokan saya lagi."
ms "Saya tertelan."
ms "Aku bertanya -tanya ... apa yang akan terjadi jika dia abstain untuk sementara waktu?"
ms "Berapa banyak sperma yang akan diproduksi raksasa ini saat dia cums?"
ms "Batin saya yang sesat gemetar dengan antisipasi."
ms "Dia mengendalikan tubuh dan bibir saya sejenak dan mewariskan keinginannya sebagai milikku."
show mila robe_blush_smirk
m "Saya ingin Anda menjauhkan diri dari masturbasi selama tiga hari."
ms "Bob mengangkat alisnya dengan terkejut, tetapi kemudian mengerutkan kening lagi."
bob "Apa -apaan? Sekarang saya bahkan tidak bisa brengsek?"
ms "Saya mencoba untuk tidak kehilangan penampilan percaya diri di bawah tekanannya."
show mila robe_proud
m "Ini adalah kondisi kedua saya."
ms "Bob ingin keberatan, tetapi berhenti pendek, dan kemudian menyeringai."
bob "Hah .__ tag_0__ baik .__ tag_0__ maka Anda harus menonton beberapa film porno favorit saya dan menulis ulasan terperinci tentang mereka."
bob "Dan juga ..."
show mila robe_irritated_open_mouth
m "Ada lagi?"
ms "Bahkan itu sangat berani, dan bukankah itu cukup baginya?"
bob "Tidak. Anda juga tidak dapat mengalami orgasme."
show mila robe_puzzled_frown
ms "Saya memandang Bob dengan marah."
m "Kedengarannya lebih dari satu kondisi ..."
ms "Bob terkekeh."
bob "Tapi ini dia. Ini adalah kondisi kedua saya"
show mila robe_irritated_open_mouth
m "Kemudian saya akan menambahkan sesuatu ke milik saya - Anda harus meninggalkan komentar terperinci tentang hal -hal yang saya kirimkan kepada Anda."
ms "Bayangan ketidakpastian jatuh di wajah Bob."
bob "Erm ... apa yang akan kamu kirimkan padaku?"
m "Heh."
show mila robe_proud
ms "Saya terkekeh."
m "Sesuatu yang akan membuat kepatuhan dengan kondisi saya lebih sulit."
ms "Bob terus mengerutkan kening, tetapi tetap mengangguk."
bob "Kesepakatan."
m "..."
ms "Entah bagaimana kami dipanaskan dalam perselisihan ini."
ms "Tapi saya suka bahwa Bob mulai berdebat dengan saya .__ tag_0__ dan mempertahankan posisinya lebih kuat."
ms "Dia masih tampak tidak yakin dengan kata -kata dan tindakannya .__ tag_0__ dan saya mencoba menemukan garis apa yang diizinkan."
ms "Tapi dia benar -benar melangkah di jalur pertumbuhan, bukan menurun."
ms "Dan dalam hal ini saya tidak bisa tidak bersukacita."
m "..."
ms "Saya hanya perlu mendorongnya sedikit lebih jauh ke arah yang benar."
m "Dan kondisi ketiga."
ms "Bob menatapku dengan seksama."
m "Saya ingin Anda mendapatkan promosi di tempat kerja."
show bob nude_bigger_penis_crossed_arms_frown
ms "Bob tiba -tiba menjadi lemas dan pekat."
ms "Tidak ada jejak yang tetap dari kepercayaannya sebelumnya."
ms "Dia bahkan tampaknya telah menyusut dalam ukuran .__ tag_0__ walaupun saya mengerti bahwa itu tidak mungkin."
bob "Haaa ...."
ms "Dia menghela nafas jengkel dan lelah."
show mila robe_puzzled
bob "Saya tahu bahwa pada akhirnya Anda akan meminta saya untuk mendapatkan Anda bintang dari langit atau memberi Anda sebuah pulau."
bob "Nah, saya minta maaf, __ tag_0__ tapi itu tidak mungkin."
ms "His voice sounded angry, even mocking."
ms "Tetapi tepi kata -katanya yang tajam tidak diarahkan kepada saya .__ tag_0__ yang terpenting, dia melukai dirinya sendiri dengan itu."
m "..."
ms "Saya tahu sulit untuk menginspirasi dia."
ms "Tetapi seperti yang ditunjukkan latihan, kemarahan memberinya energi yang cukup untuk melakukan sesuatu."
ms "Jadi saya dengan hati -hati menambahkan."
show mila robe_worried_open_mouth_wait
m "Ya ... dan ini adalah kondisi ketiga saya."
ms "Bob memelototiku."
ms "Beberapa api aneh berkobar di matanya."
ms "Itu menakutkan, __ tag_0__ tapi menarik."
bob "Ya?"
bob "Apakah itu kondisi Anda?"
ms "Aku mengangguk perlahan sebagai tanggapan, tidak mengalihkan pandangan darinya."
bob "Nah, mengapa tidak? __ tag_0__ Mengapa tidak melakukannya dalam beberapa hari apa yang tidak bisa saya lakukan dalam 30 tahun terakhir?"
bob "Bagaimanapun, ini sangat sederhana!"
bob "Yang harus saya lakukan hanyalah mencoba, bukan?"
ms "Saya diam .__ tag_0__ dia belum dalam keadaan untuk mendengar apa pun."
bob "Dan siapa yang peduli bahwa saya sudah mencoba berkali -kali .__ tag_0__ Saya mempermalukan diri sendiri, __ tag_0__ Saya melakukan semua yang saya bisa untuk mengubah sesuatu."
bob "Itu tidak ada gunanya."
bob "Cukup untuk hanya percaya pada diri sendiri! Lakukan saja! __ tag_0__ Saya muak dengan omong kosong ini."
bob "Itu tidak berhasil .__ tag_0__ dunia tidak adil .__ tag_0__ Hidup adalah permainan buruk dengan keseimbangan yang buruk."
bob "Jika Anda terlahir aneh, __ tag_0__ jika Anda tidak memiliki bakat, __ tAG_0__ tidak ada yang peduli dengan Anda."
bob "Tidak ada yang peduli apa yang Anda inginkan .__ tag_0__ orang hanya menyeka kaki mereka."
m "..."
ms "Bob terdiam. Kemarahannya mulai mereda."
ms "Tapi saya tidak ingin dia tenang .__ tag_0__ Saya ingin menambahkan bahan bakar ke api ini."
m "Saya tidak meminta Anda untuk mempermalukan diri sendiri .__ tag_0__ Saya meminta Anda untuk memompa keinginan dan kepercayaan diri Anda .__ tag_0__ untuk menyadari bahwa Anda layak."
m "Untuk memahami, bahwa orang -orang akan mulai menghormati Anda hanya ketika Anda mulai menghormati diri sendiri."
m "Ketika Anda menerima diri sendiri, maafkan diri Anda dan cintai diri Anda sendiri .__ tag_0__ hanya apa adanya."
m "Itu tidak berarti, bahwa Anda harus menyerah untuk mencoba menjadi lebih baik .__ tag_0__ justru sebaliknya."
m "Cintai dirimu sendiri .__ tag_0__ Benci kelemahanmu .__ tag_0__ Bangun versi dirimu yang lebih baik."
ms "Bob meremehkan."
bob "Saya sudah cukup."
bob "Saya tidak ingin mendengarkan omong kosong ini ..."
m "..."
ms "Saya merasa kesal."
show mila robe_iritated_atatata
m "Sialan itu bob!"
ms "Dia bahkan tersentak karena terkejut."
m "Ini adalah kondisi ketiga saya bob .__ tag_0__ hal terakhir .__ tag_0__ itu saja yang Anda butuhkan."
m "Anda mengerti?"
m "Ini bukan bintang dari langit .__ tag_0__ Ini bukan tantangan dari beberapa omong kosong ticktock .__ tag_0__ itu adalah langkah kecil."
m "Tapi selangkah lebih maju, bukan lebih dalam ke dalam quagmire .__ tag_0__ inilah yang dapat Anda lakukan .__ tag_0__ dan demi suntikan, Anda bisa."
m "Anda tidak akan mencoba .__ tag_0__ tidak perlu mencoba .__ tag_0__ berupaya untuk itu .__ tag_0__ dan lakukan."
m "Saya tidak meminta Anda untuk menggandakan gaji bulanan Anda .__ TAG_0__ Bahkan jika Anda menaikkan cek Anda pada $ 1 sudah cukup."
m "Dapatkan kenaikan gaji."
m "Dan Anda akan mendapatkan apa yang Anda inginkan dari saya."
bob "..."
m "Hidup adalah pendakian .__ tag_0__ Jangan mencoba melompati tebing .__ tag_0__ membuat satu langkah kecil pada satu waktu."
m "Kami selalu punya pilihan - untuk melarikan diri dengan memalukan dari apa yang tidak kami sukai."
m "Atau menerima diri kita sendiri dan melakukan apa yang ingin kita lakukan."
m "Dalam kasus kedua, Anda mungkin menemukan sesuatu yang Anda benci .__ tag_0__ dan lebih dari sekali .__ tag_0__ Anda dapat melukai diri sendiri, kalah, membuat kesalahan .__ tag_0__ demi mendapatkan kesempatan."
m "Dan tidak masalah apakah Anda mendapatkannya atau tidak .__ tag_0__ yang penting adalah Anda terus mencoba sepanjang jalan .__ tag_0__ seseorang mengolok -olok jika dia berhenti memanjat."
m "Dan ya, jika Anda melarikan diri, Anda akan menyimpan apa yang Anda miliki .__ tag_0__ Anda tidak akan jatuh. __Tag_0__ tetapi Anda akan dibiarkan sendirian dengan rasa malu dan kekecewaan Anda."
m "Lihat sekeliling Bob."
m "Apakah ini yang Anda inginkan? __ tag_0__ Apa yang Anda coba simpan?"
ms "Bob menyipitkan matanya."
ms "Kata -kata saya tampak semakin marah padanya."
bob "Anda tidak tahu apa yang telah saya lalui .__ tag_0__ apa yang saya alami dan alami."
bob "Bagaimana Anda bisa tahu? Anda adalah ibu rumah tangga."
ms "Komentarnya memicu saya"
m "\"Just\"seorang istri rumah?"
m "Pertama -tama saya adalah pesenam profesional .__ tag_0__ dan yang bagus .__ tag_0__ Saya sudah pensiun sekarang, dan saya memilih untuk menjadi ibu rumah tangga setelah itu."
m "Dan hal kedua - menjadi ibu rumah tangga tidak mudah .__ tag_0__ itu banyak pekerjaan yang sebenarnya."
ms "Bob terlihat seperti dia menyesal sejenak, tetapi kemudian dia mengerutkan kening lagi dan melanjutkan pidatonya."
bob "Itu hanya membuktikan maksud saya."
bob "Bukan untuk Anda untuk mengatakan semua ini kepada saya - Anda berbakat .__ tag_0__ Anda dilahirkan dengan sendok emas di mulut Anda."
bob "Dan coba tebak? __ tag_0__ Saya akan membuktikannya kepada Anda."
ms "Saya menelan lagi. Ada begitu banyak kekuatan dan kepercayaan diri pada kata -katanya ...__ tag_0__ saya menangkap diri saya berpikir bahwa saya mengagumi kemarahannya."
ms "Ada sesuatu yang sangat manusiawi dalam emosi ini .__ tag_0__ sesuatu yang menjijikkan dan indah pada saat yang sama .__ tag_0__ sesuatu yang menjijikkan dan mengasyikkan."
ms "Saya merasakan darah terburu -buru ke wajah saya."
bob "Anda pikir ini semua tentang motivasi, ya?"
bob "Maka kondisi ketiga saya adalah ini."
show mila robe_excited_and_shy
bob "Ketika saya dipromosikan, saya akan bercinta dengan Anda .__ tag_0__ Saya akan meletakkan pantat kecil Anda di sofa ini, __ tag_0__ ambil rambut Anda dan bercinta Anda sampai saya mengosongkan bola saya."
bob "Aku akan bercinta dengan tenggorokanmu dan kamu akan menelan penisku sampai ke bola .__ tag_0__ kamu akan mengendarai kemaluanku seperti rodeo liar."
bob "Saya akan menutupi Anda dengan cum saya dari kepala sampai ujung kaki dan Anda akan berterima kasih kepada saya untuk itu."
show bob nude_bigger_penis_crossed_arms_smirk
bob "Bagaimana suara itu? __ tag_0__ tidak apa -apa untuk Anda? __Tag_0__ Apakah Anda menginginkan promosi saya sebanyak itu?"
ms "Bob menjadi semakin marah dengan setiap kata. __Tag_0__ dan dengan setiap kata yang dia katakan, saya menjadi semakin bersemangat."
if mila_dom >= dom:
    ms "Saya ingin mengekang energinya. Menaklukkan dia."
    ms "Dan sial, saya membayangkan semua ini dalam warna."
    jump netorase_mila_and_bob_third_condition_continue

ms "Meskipun sepertinya energi yang sama seperti sebelumnya, __ tag_0__ saya tidak merasa terancam."
ms "Saya tidak merasa bekas .__ tag_0__ sebaliknya .__ tag_0__ Sekarang saya merasakan kekuatan saya atasnya."
ms "Dia menginginkannya .__ tag_0__ dia menyuarakannya .__ tag_0__ dan sekarang menjadi keinginan saya."
ms "Untuk memuaskannya .__ tag_0__ untuk menggunakan tubuh saya untuk tujuan yang dimaksudkan."
label netorase_mila_and_bob_third_condition_continue:
ms "Mencoba untuk tidak menunjukkan kegembiraan saya, saya mengangguk perlahan."
m "Bagus."
show bob nude_bigger_penis_crossed_arms_shock
bob "..."
bob "W-apa?"
ms "Bob kehilangan kepercayaan diri dan mengedipkan matanya karena terkejut."
ms "Rupanya, kemarahannya menerobos hambatan kesadarannya, dan semua fantasi ini hanya meledak."
show mila robe_blush_smirk
m "Saya bilang oke."
ms "Merasa mengendalikan situasi memberi saya lebih percaya diri."
ms "Jadi saya bisa tersenyum."
bob "W-What ... __tag_0__hic ...__ tag_0__ maksud Anda?"
ms "Bob masih tidak percaya. Sangat mengejutkan baginya sehingga dia mulai cegukan lagi."
ms "Seringai merayap ke bibirku."
m "Jika Anda mendapatkan promosi di tempat kerja, __ tag_0__ saya akan berdiri dengan gaya doggy di sofa ini dan menyebarkan pantat saya."
m "Saya akan berlutut, atau apa pun yang Anda inginkan dan melahap ayam besar Anda, bahkan jika saya tersedak."
m "Saya akan memanjat pangkuan Anda, dan mengendarai Anda seperti tidak ada hari esok"
m "Dan setiap kali Anda cum, saya akan memeras setiap tetes air mani Anda dan meminta lebih banyak."
ms "Bob membuka dan menutup mulutnya, tidak bisa menjawab."
ms "Saya terkikik."
m "Bagaimana suaranya? __ tag_0__ tidak apa -apa untuk Anda?"
ms "Jantungku berdebar kencang di dadaku."
ms "Kami memasukkan fantasi kami ke dalam kata -kata, dan tiba -tiba semuanya menjadi nyata."
ms "Meskipun belum ada yang terjadi, mereka menjadi begitu dekat."
ms "Saya membuka pintu dan berbalik ke arah koridor."
show mila robe_from_behind_looking
m "Selamat malam, Bob."
bob "..."
m "Dan menyiapkan hal -hal yang Anda butuhkan besok ..."
m "Aku akan datang untuk berpose untukmu."
ms "Bob diam -diam mengikutiku dengan matanya, masih dalam keadaan kaget."
play sound "door-open-close.mp3"
scene bg doors with fade
ms "Saat pintu tertutup di wajah saya, saya merasakan kesejukan udara malam."
ms "Angin sepoi-sepoi merayap di bawah pakaian saya dan membelai kulit saya yang tertutup keringat."
ms "Tiba -tiba menjadi dingin."
m "..."
show mila robe_closed_eyes_kiss
m "Achoo!"
m "..."
m "Saya harap saya tidak sakit ..."


scene bg a125_mila_puzzled with fade
ms "Saya berjalan ke rumah dan meletakkan punggung saya ke pintu."
ms "Dalam keheningan koridor, saya bisa dengan jelas mendengar jantung saya berdetak kencang."
ms "Sesuatu berubah dalam diriku ...__ tag_0__ dan di mana -mana ..."
ms "..."
ms "Apa yang baru saja terjadi?"
ms "..."
ms "Apakah saya, um. setuju untuk tidur dengan Bob?"
ms "..."
p "Bayi!"
ms "Suara Paul datang dari kamar tidur."
ms "Aku menarik napas dalam -dalam, menenangkan diri."
ms "..."
ms "Saya mungkin harus memberi tahu dia tentang apa yang terjadi ..."
ms "Tapi bagaimana? __ tag_0__ di mana saya harus memulai ..."
ms "Hai Paul, Anda tahu Bob akan segera meniduri saya .__ tag_0__ Anda tidak keberatan, bukan?"
ms "..."
scene bg a125_mila_worried
ms "..."
ms "Dia tidak keberatan, bukan?"
ms "..."
ms "Aku menghela nafas sekali lagi dan pergi ke kamar tidur."
scene bg bedroom
ms "Paul menungguku dengan seringai yang sama di wajahnya."
ms "..."
show mila robe_curious at center
ms "Saya melihat sekeliling, tetapi saya tidak melihat sesuatu yang mencurigakan."
m "Jadi ...__ tag_0__ di mana kejutannya?"
ms "Paul bersenandung."
p "Nanti."
p "Pertama, ceritakan bagaimana hasilnya dengan Bob."
ms "Saya memberi tahu Paul apa yang terjadi."
ms "Dan ketika saya sampai pada kondisi ketiga Bob, saya melihat kilatan di mata Paul."
ms "Dia menjadi sangat bersemangat."
show screen nts_stats_overlay
menu:
    "Saya harus berhati -hati dengan perasaannya (keterlambatan Mila + 1)":
        $ dom += 1
        jump a125_mila_sub
    "Paul suka menggoda (dominasi Mila + 1)":
        $ mila_dom += 1
        jump a125_mila_dom

label a125_mila_sub:
show mila robe_excited_and_shy at center
ms "Saya bertanya -tanya bagaimana dia akan bereaksi terhadap kata -kata saya ..."
hide screen nts_stats_overlay
ms "Apa ...__ tag_0__ yang akan dia katakan padaku untuk lakukan?"
ms "...{w}{image=emoji/heart.png}"
m "Dia bilang dia akan membawaku ke lutut ..."
show mila robe_blush_smirk
m "Dan persetan denganku .__ tag_0__ sulit ..."
ms "Paul menelan."
p "Berlangsung."
ms "Matanya terbakar dengan nafsu."
ms "Aku bisa merasakan tatapannya yang terbakar di kulitku."
m "Dia ...__ tag_0__ Dia bilang dia akan mengambil rambutku."
m "Dan meletakkan kemaluannya di tenggorokanku."
show mila robe_puzzled
m "Dan Anda tahu .__ tag_0__ Saya khawatir saya akan mati lemas darinya."
m "Ketika dia meniduri wajahku terakhir kali, kupikir aku akan mati ..."
ms "Paul menjilat bibirnya dan menyeringai."
p "Anda kekurangan latihan."
show mila robe_puzzled_frown
m "Hmm?"
ms "Saya menatapnya dengan terkejut."
ms "Paul mengeluarkan dildo besar dari suatu tempat dan berjalan ke arahku."
show mila robe_worried_open_mouth_wait
p "Anda tahu, saya punya pemikiran ..."
p "Saya mendengarkan cerita Anda, __ tag_0__ Saya berfantasi tentang apa yang Anda lakukan dan bagaimana Anda melakukannya."
p "Tapi itu tidak cukup. Saya tidak bisa melihatnya"
p "Jadi ternyata Anda melakukannya dengan sangat buruk."
ms "Saya mengerutkan kening dengan marah."
show mila robe_irritated_open_mouth
m "Saya tidak..."
p "Kesunyian."
show mila robe_worried_open_mouth_wait
ms "Paul mengatakannya keras dan keras."
ms "Suaranya beresonansi di dadaku, mengeluarkan kesemutan yang gatal di perut bagian bawahku."
ms "Saya langsung menutup mulut dan menghindari pandangan saya."
ms "Oh, bung. Saya menyukainya saat dia bertindak seperti ini ..."
p "Setiap hari saya semakin menyadari bagaimana saya menginginkannya."
m "..."
p "Dan Anda tahu apa? Saya pikir sudah waktunya untuk pelatihan Anda."
ms "Saya menatap Paul dengan bingung."
m "Pelatihan?"
ms "Paul melambaikan dildo di depan wajahku."
p "Keluarkan rambut Anda dari wajah Anda."
ms "Saya menatapnya tanpa prehendir."
p "Pindahkan rambut Anda ke bagian belakang kepala Anda."
m "..."
ms "Saya masih diam, Paul mengerutkan kening."
p "Apa yang Anda tunggu, lakukanlah!"
scene bg a125_mila_fix_hair
ms "Saya tertelan, __ tag_0__ Saya mengeluarkan karet gelang dan mengumpulkan rambut saya menjadi kuncir kuda."
p "Berlutut."
scene bg a125_mila_from_above
ms "Serangan Bob masih belum memudar dari ingatanku."
ms "Itu sebabnya mematuhi perintah Paul itu sulit."
p "Tangan di belakang punggung Anda."
ms "Tetapi dengan setiap detik, kegembiraan itu memadati kecemasan."
ms "Aku ingin tahu apa yang Paulus muncul saat ini?"
ms "Paul membawa mainan itu ke wajahku."
p "Buka mulutmu."
ms "Lingga besar di depan wajah saya menyerupai ayam bob .__ tag_0__ hanya bau dari sesuatu yang artifisial, __ tag_0__ bahan kimia, __ tag_0__ tidak sama sekali seperti bob."
scene bg a125_mila_from_above_penis_cringe
ms "Aku ngeri karena baunya."
ms "Paul mengerutkan kening."
p "Itu tidak bagus."
p "Anda terlalu banyak berpikir."
p "Hanya ada satu emosi yang harus Anda rasakan saat Anda melihat seekor ayam!"
p "Itu kebahagiaan."
scene bg a125_mila_from_above_penis_cringe_look_up
ms "Saya tidak cukup terangsang untuk berbicara kotor secara positif."
ms "Sepertinya penghinaan sederhana."
p "Aduh, terjadi lagi."
ms "Paul memegang rambutku dan menarikku ke bawah."
scene bg a125_mila_from_above_struggle
m "Ay yay yay!"
ms "Aku meraih lengannya mencoba mendorongnya."
p "Tangan di belakang punggung Anda!"
ms "Saya tidak mendengarkan."
ms "Paul mencondongkan tubuh ke wajahku."
p "Mengapa Anda menolak? __ tag_0__ apakah menurut Anda saya tidak dapat melihat jus menetes di antara paha Anda? __ tag_0__ kepala Anda menghalangi kesenangan Anda."
p "Anda seorang pelacur. Anda ingin bercinta seperti pelacur .__ tag_0__ tubuh Anda ingin diperlakukan seperti pelacur."
p "Tapi kepala buruk Anda terlalu penuh dengan pikiran dan ilusi tentang siapa Anda."
m "..."
ms "Paul meludahi wajahku."
scene bg a125_mila_from_above_spit
ms "Tenggorokan saya terbakar dengan kebencian. Mataku dipenuhi dengan air mata."
ms "Paul tidak bisa mengatakan itu tentang saya. Dia tidak berpikir begitu. Itu semua adalah permainan ..."
ms "Itu tidak nyata ..."
scene bg a125_mila_from_above_spit_tears
ms "Paul menyeringai."
p "Buka mulut Anda, pelacur, dan tegang lidah Anda."
ms "Aku menekankan bibirku pada prinsipnya."
ms "Paul bersandar dengan jengkel."
p "Anda tidak ingin mengakuinya, bukan?"
p "Anda ingin semuanya berhenti."
p "Anda ingin bangun besok pagi, masih merupakan istri yang sempurna yang sama, bukan?"
m "..."
p "Oke kalau begitu, __ tag_0__ Saya akan berbicara dengan Bob .__ tag_0__ saya akan memberitahunya bahwa Anda sama sekali bukan pelacur, __ tag_0__ tetapi seorang istri yang setia."
p "Dan kemudian Anda dapat terus melakukan pekerjaan rumah .__ tag_0__ seperti sebelumnya."
scene bg a125_mila_from_above_spit_looking_aside
ms "..."
ms "TIDAK..."
ms "Saya tidak menginginkan itu ..."
ms "Saya tidak ingin mati karena kebosanan lagi ..."
ms "Juga..."
ms "Kenapa dia mengatakan itu? __ tag_0__ kenapa dia begitu kejam padaku?"
ms "..."
ms "Karena ...__ tag_0__ karena saya menyukainya."
ms "Saya akhirnya bisa menelan benjolan di tenggorokan saya."
scene bg a125_mila_from_above_spit_sucking
ms "Perlahan aku melonggarkan bibirku dan membuka mulutku."
ms "Suara batin saya histeris berteriak pada saya."
ms "Bahwa saya harus menghormati diri sendiri .__ tag_0__ bahwa ini bukan saya .__ tag_0__ bahwa semua penghinaan ini tidak dapat diterima."
ms "Tapi tatapan Paul yang menghina dan memerintah menenggelamkan suara itu."
ms "Membekapnya dengan kehadirannya yang luar biasa."
ms "Dan saya meleleh di bawah tatapan itu."
scene bg a125_mila_from_side_suck
p "Itu saja .__ tag_0__ gadis yang baik."
ms "Kata -kata itu seperti balsem hangat bagi saya."
ms "Aku melepaskan tangannya dan perlahan -lahan meletakkan tanganku di belakang."
p "Tunjukkan bagaimana Anda mengisap penis bob, pelacur"
ms "Nafsu saya menenggelamkan semua perasaan dan pikiran lainnya."
ms "Hanya ada satu keinginan tersisa .__ tag_0__ untuk dipatuhi."
ms "Perlahan -lahan aku membawa mainan itu ke mulutku dan mulai mengisap kepalanya."
ms "..."
m "Mmm."
m "..."
m "..."
ms "Paul mengawasiku sebentar, lalu menghembuskan napas dengan kesal."
p "Sungguh pemandangan yang menyedihkan ..."
scene bg a125_mila_from_above_pout
ms "Saya mengerutkan kening dan membiarkan mainan itu keluar dari mulut saya."
p "Saya sudah lama bermaksud memberi tahu Anda ..."
p "Terus mengisap, kenapa kamu berhenti?"
m "..."
scene bg a125_mila_from_side_suck
ms "Saya dengan enggan dipatuhi."
p "Saya sudah lama bermaksud memberi tahu Anda - Anda mengerikan dalam mengisap."
scene bg a125_mila_from_side_suck_2
ms "Oh, maafkan saya! __ tag_0__ jika Anda tidak menyukainya, hisap sendiri ..."
ms "Saya hampir menangis dengan kebencian."
p "Dan inilah alasan mengapa saya tetap diam - reaksi Anda .__ tag_0__ Saya takut Anda akan dihina dan menangis."
scene bg a125_mila_from_side_suck_2_2
ms "Aku membeku dan menatap Paul."
p "Tapi sekarang saya tahu bahwa Anda ingin menjadi pelacur yang sebenarnya. __Tag_0__so saya dengan benar melatih Anda untuk menjadi satu."
p "Menghisapnya .__ tag_0__ lebih dalam."
scene bg a125_mila_from_side_suck_2
m "..."
m "..."
m "..."
p "Ya..."
m "..."
m "..."
p "Baiklah, itu sudah cukup."
scene bg a125_mila_from_above_pout
ms "Aku bersandar dan menyeka bibirku."
p "Pertama, Anda perlu menggunakan lebih banyak air liur, comprende?"
p "Dan tidak hanya sedikit lagi, Anda harus memiliki banyak hal yang mengalir di bola dan dagu Anda."
p "Mengerti?"
ms "Saya dengan enggan mengangguk sebagai tanggapan."
p "Jawab, ya tuan."
m "..."
m "Ya ... tuan ..."
p "Kedua, Anda harus belajar rileks tenggorokan."
p "Tubuh Anda harus menjadi Onahole yang hidup mengeluarkan jus cinta."
p "Ingatlah itu - Anda hanya cumdump."
p "Sekarang, katakan dengan keras."
ms "Sungguh omong kosong ..."
m "..."
p "Lakukan itu."
scene bg a125_mila_from_above_admit
m "Saya ...__ tag_0__ Saya hanya cumdump ..."
ms "Entah bagaimana itu tidak terdengar sebagai penghinaan atau penghinaan."
ms "Rasanya seperti pujian ...__ tag_0__?"
ms "Paul mendorong dildo ke mulut saya sampai di tenggorokan saya."
scene bg a125_mila_from_side_suck_3_1
m "Mgmm!"
ms "Kepala karet menekan ke tenggorokan saya, memicu refleks muntah."
scene bg a125_mila_from_side_suck_3_3
p "Anda masih berjuang."
scene bg a125_mila_from_side_suck_3_2
m "(batuk)"
scene bg a125_mila_from_side_suck_3_3
p "Saya tidak menyukainya."
p "Ulangi di kepala Anda - Saya hanya cumdump."
ms "..."
scene bg a125_mila_from_side_suck_3_2
m "(batuk)"
scene bg a125_mila_from_side_suck_3_3
ms "Saya hanya seorang cumdump ..."
scene bg a125_mila_from_side_suck_3_2
m "(tersedak)"
scene bg a125_mila_from_side_suck_3_3
ms "Saya hanya seorang cumdump ..."
p "Longgarkan tenggorokan Anda, pelacur."
p "Aku tidak bisa melakukannya untukmu."
p "Merupakan hak istimewa pelacur sejati untuk belajar mengabaikan refleks muntah mereka untuk mengisap ayam."
p "Dan Anda akan menjadi pelacur itu."
p "Anda harus melepaskan keinginan egois Anda untuk kesenangan."
p "Anda harus melepaskan keinginan egois Anda untuk kesenangan."
scene bg a125_mila_from_side_suck_3_2
m "(batuk)"
scene bg a125_mila_from_side_suck_3_4
p "Anda harus menyadari bahwa tujuan Anda adalah untuk memberikan kesenangan"
p "Dan untuk melakukan itu, Anda harus belajar menikmati rasa sakit, penghinaan, mati lemas."
scene bg a125_mila_from_side_suck_3_5
m "(batuk)"
scene bg a125_mila_from_side_suck_3_4
p "Angsa."
ms "Saya tidak bisa ..."
scene bg a125_mila_from_side_suck_3_5
m "(batuk)"
scene bg a125_mila_from_side_suck_3_4
p "Saya bilang menelan."
ms "Tidak mungkin ...__ tag_0__ saya tidak bisa melakukannya ..."
ms "Saya mengambil napas dalam -dalam melalui hidung saya .__ tag_0__ lalu saya rileks, meskipun merasakan tekanan di tenggorokan saya"
ms "Dan kemudian ...__ tag_0__ saya hanya tertelan."
scene bg a125_mila_from_side_suck_4
p "Itu saja. Anak yang baik."
ms "Saya tidak tahu bagaimana sesuatu yang begitu tebal turun ke tenggorokan saya."
ms "Tapi itu benar"
ms "Tenggorokan saya meregangkan dan meliputi kepalanya"
ms "Mulut saya dipenuhi air liur yang licin"
ms "Paul terus mendorong, mendorong mainan itu lebih dalam"
scene bg a125_mila_from_side_suck_5
m "(batuk)"
p "Itu gadisku"
p "Anak yang baik"
p "Itu saja."
ms "Saya merasa seperti mainan itu sudah tenggelam di perut saya."
ms "Tenggorokan saya sebentar -sebentar berkontraksi dan mencoba mendorong benda asing keluar."
scene bg a125_mila_from_side_suck_6
m "(tersedak)"
p "Untuk bola, sayang."
p "Itu saja. Anak yang baik."
ms "Bola karet menusuk daguku."
ms "Mulut saya dipenuhi air liur"
ms "Air mata memenuhi mataku."
ms "Tapi saya bisa melihat kepuasan Paulus, dan itu memberi saya kekuatan."
ms "Saya mencoba untuk bersantai, tetapi saya tidak pandai dalam hal itu."
ms "Ketidaknyamanan itu terlalu banyak ..."
m "(batuk)"
ms "Paul perlahan menarik mainan itu keluar dari tenggorokan saya, dan saya hampir tidak bisa menahan tersumbat dari sensasi."
m "..."
scene bg a125_mila_from_side_breather
ms "Aku bernafas dengan rakus dan terus menelan air liur pahit."
p "Itu sudah cukup .__ tag_0__ Buka mulut Anda dan lengket lidah Anda."
ms "Tidak ada pikiran yang tersisa di kepalaku."
scene bg a125_mila_from_side_suck_3_4
ms "Saya menurut, terlepas dari sensasi yang tidak menyenangkan."
ms "Semakin sedikit saya memikirkannya, semakin baik."
ms "Lingga menyelinap ke dalam mulutku dan ke tenggorokanku."
ms "Saya memejamkan mata dan mencoba bersantai."
scene bg a125_mila_from_side_suck_3_5
m "(batuk)"
p "Ayo .__ tag_0__ lebih dalam, pelacur."
ms "Aku tertelan, dan ayam itu memasuki tenggorokanku."
scene bg a125_mila_from_side_suck_4
m "(batuk)"
scene bg a125_mila_from_side_suck_5
p "Itu saja."
p "Begitulah seharusnya Anda mengisap ayam Bob."
scene bg a125_mila_from_side_suck_6
ms "Bola karet kembali lagi, menusuk daguku."
p "Gunakan lidah Anda juga. __Tag_0__ Anda hanya cumdump. __Tag_0__ Gunakan semua yang Anda miliki untuk menyenangkan pria itu."
m "..."
scene bg a125_mila_from_side_suck_7
p "Anak yang baik. __Tag_0__ itu saja."
p "Bayangkan bagaimana rasanya .__ TAG_0__ Pub -pubnya yang besar dan berbulu akan bertentangan dengan hidung Anda."
p "Anda akan mencium bau bau asam keringatnya."
p "Dan kemaluannya akan jatuh ke tenggorokan Anda"
p "Begitulah cara pelacur memberikan blowjobs"
m "(batuk)"
scene bg a125_mila_from_side_breather
ms "Paul menarik mainan itu keluar dari mulutku lagi."
ms "Saya mencoba mengatur napas saat ini."
ms "Paul melambaikan lingga di depan wajahku."
p "Sekarang buktikan bahwa Anda tahu cara melakukannya."
p "Mengisap 'bob' dengan cara yang membuat saya percaya Anda menginginkan cum -nya."
scene bg a125_mila_from_side_pulling_cock
ms "Saya ragu -ragu sejenak, tetapi kemudian saya mengambil ayam di tangan saya dan membimbingnya ke mulut saya."
p "Lepas tangan."
scene bg a125_mila_from_side_suck_2
ms "Aku menjatuhkan kepala ke dalam mulutku dan mulai mengisapnya dengan rajin."
p "Sialan yang kamu lakukan lagi? __ tag_0__ fuck .__ tag_0__ your .__ tag_0__ tenggorokan."
scene bg a125_mila_from_side_suck_5
ms "Ketika saya harus menggerakkan kepala saya sendiri, tenggorokan saya tegang."
scene bg a125_mila_from_side_suck_4
m "(batuk)"
scene bg a125_mila_from_side_suck_5
ms "Dan itu membuat saya lebih sulit untuk bersantai."
p "Anda hanya seorang cumdump."
scene bg a125_mila_from_side_suck_4
m "(batuk)"
scene bg a125_mila_from_side_suck_5
p "Anda terlalu banyak berpikir lagi"
p "Tugas Anda adalah membawa kesenangan"
scene bg a125_mila_from_side_suck_4
m "(batuk)"
scene bg a125_mila_from_side_suck_5
p "Lakukan itu"
ms "Sobat, kedengarannya sangat bodoh ..."
ms "..."
scene bg a125_mila_from_side_suck_4
m "(batuk)"
scene bg a125_mila_from_side_suck_5
ms "Persetan."
ms "Saya hanya seorang cumdump ..."
ms "Saya seorang pelacur mesum."
ms "Saya suka mengisap ayam."
ms "Saya ingin mandi dalam cum."
ms "Saya ingin gangbanged"
ms "Saya ingin digunakan sebagai 'benda'"
scene bg a125_mila_from_side_suck_4
ms "Saya hanya seorang cumdump"
p "Itu saja .__ tag_0__ gadis yang baik."
scene bg a125_mila_from_side_suck_8
ms "Aku tidak memperhatikan ketika ayam itu mulai tenggelam dengan tenang di tenggorokanku."
ms "Dan kali ini, saya tidak merasa tidak nyaman."
ms "Saya menginginkannya lebih dalam."
scene bg a125_mila_from_side_suck_9
ms "Saya menekan wajah saya ke dalam bola karet."
ms "Lingga melebar tenggorokan saya sehingga saya tidak bisa bernapas."
ms "Tetapi saya mencoba mendorongnya bahkan lebih dalam, seperti saya mencoba menelannya utuh."
scene bg a125_mila_from_side_suck_10
ms "Aku menjulurkan lidahku dan mencoba menjilat bola di dildo"
ms "Dan saat itulah saya merasakan tetesan panas di wajah saya."
scene bg a125_mila_from_side_cum1
p "Ya, pelacur!"
p "Itu saja .__ tag_0__ tersedak pada ayam gemuk itu .__ tag_0__ oh, sial, kamu sempurna ..."
scene bg a125_mila_from_side_cum2
p "Oh, bercinta"
scene bg a125_mila_from_side_cum3
p "Ya"
ms "Menyadari bahwa Paul sudah cumming dan saya berlari keluar dari udara, saya akhirnya menarik kembali dan mulai menelan udara."
scene bg a125_after_fellatio
m "Haaaaah ...__ tag_0__ hahaha ...__ tag_0__ haaaa ..."
ms "Senyum merayap di wajahku .__ tag_0__ Aku merasa sangat senang bahwa Paul datang."
ms "Sepertinya saya benar -benar memenuhi tujuan saya."
p "Anak yang baik"
p "Aku akan menidurimu dengan mainan itu, tapi masalahnya adalah__tag_0__ kamu dilarang cum."
p "Dan dilihat dari genangan air di antara kaki Anda, Anda tidak jauh dari orgasme."
p "Jadi ... __tag_0__tough Luck, huh?"
scene bg a125_after_fellatio2
ms "..."
ms "Apa yang baru saja terjadi?"
ms "..."
ms "...{w}{image=emoji/heart.png}"
if _in_replay:
    return
jump a126

label a125_mila_dom:
show mila robe_blush_smirk at center
m "Apakah Anda tahu apa yang akan dia lakukan pada istri Anda?"
p "..."
hide screen nts_stats_overlay
m "Dia ingin aku naik ke sofa dan menyebarkan pantatku."
ms "Aku memunggungi Paul."
scene bg a125_all_fours
m "Seperti ini, mungkin?"
m "Dia akan meraih rambutku dan meletakkan kemaluannya di dalam mulutku, sampai ke bolanya."
p "..."
ms "Ayam Paul jelas menonjol dari celana panjangnya."
scene bg a125_all_fours_grin
m "Dan kemudian, aku akan berlutut."
scene bg a125_fellatio_gesture
m "Buka mulutku dan biarkan dia bercinta wajahku."
p "..."
m "Mmm? Apa itu?"
m "Ingin melihat?"
scene bg a125_smirk
m "Apakah Anda ingin melihat istri Anda yang tidak setia menghisap penis pria lain?"
m "Bagaimana bolanya akan menampar vaginaku?"
m "Bagaimana dia akan menuangkan galon air mani di seluruh wajahku?"
p "...__ tag_0__ ya ..."
m "Uhuh ..."
m "Tapi saya khawatir Anda hanya harus hidup dengan fantasi Anda untuk saat ini."
m "Tetapi jika Anda menginginkannya, saya bisa pulang ke rumah dengan cumnya lain kali."
m "Apakah Anda ingin melihatnya?"
scene bg a125_grin
p "Ya!"
p "Ya, ya ya!"
m "Mmm, saya pikir seseorang menjadi terlalu fantasi ..."
scene bg a125_smirk
m "Tapi Anda tahu, Bob melarang saya menjadi cum."
m "Jadi saya tidak dapat membantu Anda dengan masalah Anda."
ms "Aku mengangguk pada kemaluannya."
m "..."
m "Mengapa Anda melihat saya seperti itu?"
m "..."
scene bg a125_dildo
m "Apa itu?"
ms "Paul mendorong dildo besar di depan wajahku."
p "Ini adalah kejutan yang saya ceritakan."
m "Hmmm ..."
scene bg a125_dildo_smirk
m "Dan apa yang Anda ingin saya lakukan dengan kejutan ini ...__ tag_0__?"
p "..."
ms "Paul tidak menjawab .__ tag_0__ Anda ingin saya menggoda Anda, ya?"
m "Wow ...__ tag_0__ sangat besar!"
m "Sepertinya ayam Bob ..."
m "Anda tahu .__ tag_0__ Saya sangat ingin mencoba seperti apa .__ tag_0__ untuk mengendarai raksasa seperti itu."
m "Saya membuang jubah saya"
ms "Sial, __ tag_0__ Saya sangat bersemangat ... __tag_0__but bob melarang saya untuk cum ...__ tag_0__ saya tidak boleh berbohong padanya"
ms "Jadi saya harus menahan diri secara serius"
scene bg a125_dildo_squating
m "..."
m "Ya Tuhan, ini sangat besar!"
m "Saya tidak berpikir itu akan muat di dalam diri saya"
m "Bagaimana menurutmu?"
m "Mmm."
m "Anda dapat menyentak ayam Anda saat raksasa ini meniduri istri Anda."
ms "Paul dengan tergesa -gesa menarik kemaluannya keluar dari celananya dan meraihnya seolah dia ingin merobeknya."
m "Ahahhh ..."
scene bg a125_dildo_squating2
m "Mmm ...__ tag_0__ menonton ayam bob meregangkan vagina saya."
m "Shhhh ... __tag_0__ ouch ... __tag_0__ oh, Tuhan, sangat besar"
m "Aaahhhh ..."
m "Mmm ..."
m "Oh Bob, luangkan waktu Anda, biarkan saya terbiasa ..."
m "Aku tidak pernah kacau oleh penis yang begitu besar ..."
m "..."
m "Hehe ... apakah kamu suka acaranya?"
p "Y-ya ..."
m "Kemudian saya akan berusaha lebih keras untuk Anda dan mencoba duduk lebih rendah ..."
scene bg a125_dildo_squating3
m "Ahhh ..."
m "Ohh fuck ..."
m "Bob kamu akan mencabik -cabikku ...__ tag_0__ Hati -hati ..."
m "Mmm ..."
m "Uff ...__ tag_0__ Saya pikir ini adalah batas saya, Bob ..."
ms "Mainan itu mengisi vaginaku .__ tag_0__ Dia sangat besar sehingga saya merasa lebih sakit daripada kesenangan."
m "Saya duduk sedalam yang saya bisa .__ tag_0__ dan dildo bersandar pada rahim saya, memberikan sensasi yang menyenangkan."
m "..."
m "Mmm"
scene bg a125_dildo_squating4
m "Apakah kamu menyukainya?"
p "Ya! Sangat!"
m "Ahah"
m "Apakah Anda ingin cum?"
p "Ya! __ tag_0__ Saya sudah dekat ..."
m "Anda tidak diizinkan untuk cum di vagina saya, itulah hak istimewa Bob."
m "Dia memesannya."
m "Itu sebabnya Anda akan cum di kaki saya"
m "Bersyukur"
m "..."
scene bg a125_dildo_squating_feet
ms "Saya harus menahan diri agar tidak menusuk diri saya bahkan lebih dalam pada penis Bob ...__ tag_0__ maksud saya ... __tag_0__ pada dildo, tentu saja."
ms "Saya masih menaruh beban pada selangkangan saya, dan itu mendorong dildo lebih dalam membuat saya mengerutkan kening kesakitan"
ms "Paul, merasakan sentuhan kakiku, segera mulai cum."
scene bg a125_dildo_squating_feet_cum
m "Pfff ...__ tag_0__ ahaha ..."
m "Anak yang baik."
m "Lepaskan semuanya ke kakiku ..."
m "..."
m "Anak yang baik"
m "Apakah kamu bahagia?"
p "..."
m "Apakah Anda suka bagaimana istri Anda melompat pada penis besar ini?"
p "..."
scene bg a125_dildo_squating_feet_cum_pout
m "Tidak? __ tag_0__ Maaf maka saya tidak akan pernah melakukan ini lagi ..."
p "...__ tag_0__ __tag_1__ saya menyukainya ..."
m "Hmmm ...__ tag_0__ apa itu?"
p "__Tag_0__ saya berkata, saya menyukainya ..."
scene bg a125_dildo_squating_feet_cum
m "Oh ya? __ tag_0__ Saya tidak tahu! __Tag_0__ jadi apakah Anda ingin saya melakukannya lagi?"
p "... __tag_0__yes."
m "Hehe"
m "Sangat disayangkan, bahwa saya tidak bisa cum, saya ingin sekali membuat orgasme juga ..."
ms "Saya dengan hati -hati berdiri dari penis dan membalikkan punggung saya ke Paul."
m "Lihat."
scene bg a125_after_sex_spread
ms "Saya sengaja tidak tegang otot vagina saya sehingga vagina saya akan terlihat sekuat mungkin."
m "..."
p "... __tag_0__wow."
m "Apakah kamu menyukainya?"
p "Y-ya ..."
m "Aku akan terangsang seperti bercinta setelah beberapa hari tanpa cumming"
m "Dan kemudian Bob akan meniduri istrimu di vagina yang membutuhkan itu"
p "..."
m "Apakah itu yang kamu inginkan, sayang?"
ms "Paul menelan."
m "Saya ingin Anda mengatakannya"
p "... __tag_0__A Saya ingin Anda kacau oleh Bob ... __tag_0__ dan maka saya ingin melihat Anda tertutup cum ..."
scene bg a125_after_sex_spread_grin
m "Hehe ...__ tag_0__ jika suamiku menginginkannya, aku akan melakukannya"
if _in_replay:
    return


label a126:

ms "..."
scene 126_mila_sleeping with fade
ms "Saya sangat tidur."
scene 126_nightmare_blink
ms "Sepanjang malam saya disiksa oleh semacam mimpi buruk erotis ..."
ms "Monster mengejar saya, menangkap saya dan memperkosa saya."
ms "Takut dicampur dengan kegembiraan, jijik dengan nafsu"
ms "Saya bangun lebih lambat dari biasanya, tertutup keringat dingin"
ms "..."
scene 126_mila_morning
m "Sialan ...__ tag_0__ tidak hanya saya tidak cukup tidur ..."
m "Tapi vaginaku gatal ..."
m "Saya bukan nymphomaniac ...__ tag_0__ tetapi saat ada sesuatu yang dilarang - Anda mulai menginginkannya"
scene 126_mila_morning_blush
ms "..."
ms "Kepalaku dipenuhi dengan pikiran tentang apa yang terjadi kemarin."
ms "Tentang percakapan dengan Bob ...__ tag_0__ dan apa yang terjadi setelahnya."
ms "..."
scene 126_mila_morning_phone
ms "Hmmm ..."
ms "Ada beberapa lusin pesan yang belum dibaca dari Bob di ponsel saya."
ms "Ini adalah tautan ke klip porno."
ms "Dilihat dari waktu pengirim, dia menghabiskan sepanjang malam berkumpul dan mengirimnya kepada saya."
ms "..."
m "Mungkin itu sebabnya saya tidur sangat buruk?"
scene 126_mila_morning_phone_smirk
ms "Mungkin dia monster terangsang itu, dan keinginannya yang semakin besar yang saya rasakan?"
ms "Sial ... sekarang saya ingin menghukum Bob untuk ini."
play sound "shot.mp3"
scene 126_mila_morning_selfie with flash_nightmare
ms "..."
ms "Terlihat bagus"
ms "Tapi ... __tag_0__ Saya pikir saya perlu menutupi puting saya ...__ tag_0__ saya masih merasa agak tidak aman ..."
ms "Ya. Itu lebih baik"
ma "Selamat pagi!"
ma "__tag_0__"
ms "Bob tidak perlu menunggu lama untuk jawaban."
bob_message "!"
scene 126_mila_morning_phone_grin
ms "Ahah ..."
ms "Sekarang duduk di sana dan sembunyikan sosis Anda dari kolega Anda."
ms "hehe"
scene 126_mila_morning_phone_smirk
ma "Satu tanda seru tidak cukup untuk jawaban yang lengkap."
ms "Saya melihat bahwa status pesan berubah menjadi "baca", tetapi tidak ada tanggapan"
ma "Haruskah saya berasumsi bahwa perjanjian kami tidak valid?"
bob_message "TIDAK."
ms "Bob segera merespons"
bob_message "Saya tidak tahu bagaimana menjawab ..."
bob_message "Kamu sangat cantik."
ma "Terima kasih Bob."
scene 126_mila_morning_phone_grin
ms "hehe"
ms "Oke, ini akan dilakukan pertama kali."
bob_message "Apakah Anda sudah menonton klipnya?"
scene 126_mila_morning_phone
ms "..."
m "Kapan dia menjadi begitu gigih?"
ma "Tidak Bob, saya baru saja bangun."
bob_message "Selamat pagi."
scene 126_mila_morning_phone_smirk
ms "Inilah yang seharusnya Anda katakan di awal."
ms "..."
ms "Oke, mari kita lihat apa yang ada di sana."
ms "Setelah berpikir sedikit, saya memutuskan untuk merekam pesan suara saat saya menonton video."
ms "Ini akan lebih mudah daripada menulis teks nanti."
ms "..."
scene 126_video_1 with fade
m "Hai Bob. Saya mulai menonton video Anda."
m "The title says \"A good stretch\"..."
m "Yang pertama adalah tentang seorang gadis di gym? __ tag_0__ bahkan dianggap pornografi? __Tag_0__ok, mari kita lihat ..."
ms "..."
scene 126_video_2
m "Oh, dia fleksibel .__ tag_0__ saya masih bisa melakukan hal seperti itu juga, saya pikir"
ms "..."
scene 126_video_3
m "Dan ini rupanya pelatih."
ms "..."
m "Ya, dia ingin membantunya dengan peregangan."
m "Dia terlihat seperti balerina atau pesenam. __Tag_0__nice"
scene 126_video_4
ms "..."
m "Ah..."
m "Oooh ..."
m "Ini tentang peregangan semacam itu ..."
scene 126_video_5
ms "..."
m "Sialan ..."
m "Dia besar"
m "Apakah kamu bercanda? __ tag_0__ tidak mungkin ..."
m "Itu tidak cocok."
m "Keledai tidak akan meregang sebanyak itu."
scene 126_video_6
ms "..."
m "Oke, saya mengambil kata -kata saya kembali."
m "..."
m "Apa yang ditemukan pria di anal?"
m "Lubang ini tidak dimaksudkan untuk seks."
scene 126_video_sex
ms "..."
m "Saya agak mengerti ..."
m "Untuk beberapa alasan terlihat panas"
ms "Tanganku turun ke vaginaku."
m "Mmm ..."
ms "Sial, yang utama bukanlah cum."
m "Bob, bisakah kamu mendengar suara -suara itu?"
"shlick__tag_0__ shlick__tag_0__ shlick"
m "Jangan khawatir ...__ tag_0__mmm ...__ tag_0__ saya akan menepati janjiku ...__ tag_0__ahhh ...__ tag_0__ dan aku akan berhenti tepat waktu ..."
m "Mmm ..."
"shlick__tag_0__ shlick__tag_0__ shlick"
m "Sial, tapi ini akan sulit."
scene 126_video_8
ms "..."
m "Tunggu, dia ingin dia menghisapnya?"
ms "..."
m "Tapi penisnya hanya ada di pantatnya ..."
scene 126_video_9
m "..."
m "Tentu saja, dia akan memaksanya untuk melakukannya ..."
m "Um ...__ tag_0__ apakah kamu suka ini?"
ms "..."
m "Itu memalukan"
m "Meskipun saya tidak akan menyembunyikannya, ada sesuatu dalam hal ini."
m "Sesuatu yang kotor .__ tag_0__ dalam arti literal kata."
ms "..."
m "Juga, saya pikir penis Anda lebih besar."
scene 126_video_cum
m "Oh, dia sedang cumming di wajahnya"
m "Ada sesuatu yang sangat nakal tentang finishing di wajah, kan?"
m "Itu saja?"
m "Video keren, saya menyukainya."
ms "Saya mematikan rekaman."
scene 126_mila_morning_phone with fade
ms "Vagina saya gatal karena keinginan."
m "Saya butuh semacam gangguan ..."
ms "Saya ingin Bob mengalami kesulitan berkonsentrasi juga."
m "Hmmm ..."
scene 126_mila_morning_phone_smirk
ms "..."
ms "Mungkin saya juga harus melakukan sedikit peregangan?"
ms "Saya berganti pakaian dan mengatur kamera"
ms "Vagina saya sangat basah sehingga legging saya direndam dengan jus saya."
play sound "shot.mp3"
scene 126_mila_stretching with flash_nightmare
ms "Hmmm ..."
ms "Apakah terlalu banyak?"
ms "Saya pada dasarnya menunjukkan vaginaku padanya ..."
ms "...__ tag_0__ jadi apa?"
ms "Dia akan segera meniduriku."
ms "..."
ms "Hehe"
ms "Mari kita lihat reaksinya"
ma "Saya menonton video pertama"
ma "Saya menyukainya!"
ma "Itu membuatku berpikir ..."
ma "Apakah Anda ingin membantu saya meregangkan?"
ma "__tag_0__"
bob_message "Ya Tuhan ..."
ms "hehe ..."
ma "Hanya itu yang bisa Anda katakan?"
ma "Apakah menurut Anda saya fleksibel?"
bob_message "Ya"
bob_message "Maaf, saya belum melupakan pesan audio Anda ..."
ma "Saya yakin sulit bagi Anda di sana."
ms "hehe"
ma "Tapi saya masih membutuhkan komentar yang lebih rinci tentang gambar saya."
bob_message "Saya dapat membantu Anda ... dengan peregangan."
ma "Oh terima kasih! Anda sangat baik."
ma "Apa yang Anda bayangkan ketika Anda melihat saya di posisi ini?"
ms "Bob membaca pesan saya lagi tetapi tidak menanggapi."
ma "Bob"
ma "Itu baru bagiku juga."
ma "Tapi saya merekam seluruh pesan suara untuk Anda saat saya menonton film porno."
ma "Saya yakin Anda juga bisa mengatakan sesuatu yang nakal ..."
ma "Saya menginginkannya"
ms "Bob tidak menjawab"
ma "Please Please?"
ms "Butuh beberapa saat untuk menjawab"
ms "..."
ms "Ayo, Bob, ceritakan sesuatu yang kotor ..."
bob_message "Saya membayangkan melepas legging Anda dan meniduri pantat Anda."
ms "Pantatku?!"
ma "Kenapa pantatku?"
bob_message "Aku tidak tahu. Saya menyukainya"
ma "Saya khawatir itu tidak mungkin, Bob"
ma "Pernahkah Anda melihat penis Anda?"
bob_message "Anus dapat meregangkan hingga 14 cm tanpa usaha."
ms "Hingga 14! .. Saya tidak percaya."
bob_message "Jadi jangan khawatir tentang itu."
ms "Tunggu sebentar. Apa maksudmu jangan khawatir?"
ma "Saya tidak berencana melakukan seks anal, Bob."
bob_message "Oh..."
bob_message "OKE..."
ms "Saya ingin mendukungnya entah bagaimana, jadi saya mengambil selfie lain."
ms "..."
play sound "shot.mp3"
scene 126_mila_selfie with flash_nightmare
ma "Tapi saya berencana untuk melakukan sesuatu yang lain;)"
ma "__tag_0__"
bob_message "Ya Tuhan ..."
bob_message "Mila, jika Anda tidak berhenti mengirimi saya foto -foto seperti itu, saya mungkin cum di celana saya hanya dari menggosok lalat saya."
ms "Pfft, hahahaha."
ms "Ini adalah jenis komentar yang saya bicarakan!"
ma "Hati -hati di luar sana."
ms "Saya menonton beberapa video lagi dari koleksi dan merekam pesan audio."
ms "Ketika saya melakukan ini, saya tidak melihat malam itu telah tiba."
m "Sial, aku belum melakukan sesuatu yang berguna hari ini ..."
ms "Saya merasa seperti freeloader sekarang ..."
ms "..."
ms "Baiklah, mari kita asumsikan bahwa hari ini adalah hari libur saya."


scene br with fade
ms "..."
scene 126_mila_after_shower
ms "Paul belum kembali ke rumah ketika saya mendengar Bob memasuki apartemennya."
ms "Saya mandi untuk sedikit menyegarkan."
ms "Saya ingin mengenakan jubah saya yang biasa, tetapi tiba -tiba saya merasa tidak cocok"
ms "Tubuh saya berubah seiring dengan pikiran saya"
ms "Saya ingin menarik perhatian"
ms "Saya ingin pria menginginkan saya"
ms "Anak buahku"
scene 126_mila_after_shower_naughty
m "Hehe ..."
ms "Masalahnya adalah saya tidak benar -benar menyembunyikan tubuh saya sebelumnya."
ms "Tapi sekarang saya ingin menyoroti barang saya"
ms "..."
scene 126_mila_after_shower_top
ms "Saya datang ke kamar tidur dan mencari -cari pakaian untuk menemukan sesuatu yang sesuai dengan __esc_0 __ '' getaran yang baru saya '' lebih baik."
ms "Saya memilih bagian atas tanpa tali"
ms "Saya ingat itu terus jatuh dari dadaku, dan aku berhenti memakainya."
ms "Sekarang, ini bukan masalah .__ tag_0__ baik, bahkan jika itu jatuh, jadi apa?"
ms "Saya akan menyenangkan beberapa orang yang lewat dengan payudara telanjang saya"
ms "Saya tidak keberatan"
scene 126_mila_after_shower_from_behind
ms "Saya juga menemukan celana pendek yang sudah lama saya beli untuk pergi ke pantai."
ms "Saya tidak pernah berani pergi ke luar di dalamnya."
ms "Mereka terlihat terlalu slutty untukku"
ms "Aku berputar -putar di cermin mengagumi refleksiku."
ms "fufu ...__ tag_0__ Saya bertanya -tanya apa yang akan dikatakan Bob ..."
ms "Oke, waktunya untuk pergi ..."
scene 126_mila_hi
ms "..."
m "Hai Bob! __ tag_0__ saya datang!"
ms "Bob duduk di sofa ruang tamu di depan album kecil pensil."
ms "Ada kamera di tangannya."
bob "Hei, __ tag_0__ melepas pakaian Anda."
bob "Saya ingin mengambil beberapa gambar untuk referensi."
scene 126_mila_surprised
ms "..."
ms "Saya sedikit mundur dari tekanannya."
ms "Tapi Bob tetap duduk, jadi aku tidak takut atau tidak nyaman dari tekanan ini."
ms "Saya bahkan merasa sedikit tersinggung karena dia tidak mengatakan apa -apa tentang penampilan saya."
scene 126_mila_worried
m "W-tunggu. Mari kita bergerak secara bertahap."
ms "Bob mengerutkan kening."
bob "Lagi?"
scene 126_mila_serious
m "Saya tidak akan kembali dengan kata -kata saya."
m "Cukup menggunakan kata -kata Anda sendiri - bagaimana saya bisa menjamin Anda akan memenuhi bagian kesepakatan Anda?"
bob "..."
m "Jika saya melepas pakaian saya sekarang, Anda akan mengambil beberapa gambar, dan kemudian Anda tidak akan menggambar apa pun."
bob "Saya tidak akan melakukan itu."
scene 126_mila_worried
m "Yah, saya akan menepati janji saya juga, tetapi Anda tidak mempercayai saya."
m "Mengapa saya harus mempercayai Anda?"
bob "..."
bob "Saya tidak suka kemana perginya"
bob "Apa yang Anda sarankan?"
m "..."
scene 126_mila_serious
m "Ayo lakukan ini ..."
m "Saya akan menanggalkan pakaian .__ tag_0__ sepotong demi sepotong .__ tag_0__ dan Anda akan menggambar saya di setiap langkah .__ tag_0__ bagaimana suara itu?"
bob "..."
bob "Tapi saya akan membutuhkan banyak waktu untuk setiap sketsa."
m "Jadi? __ tag_0__ Apakah kita sedang terburu -buru?"
bob "..."
m "..."
scene 126_mila_smile
bob "Bagus."
bob "Tapi kemudian, saya ingin Anda berubah menjadi sesuatu."
scene 126_mila_serious
ms "Saya melihat diri saya sendiri."
ms "Dan mengapa saya memilih pakaian ini?"
m "Jika tidak lebih terbuka dari apa yang sudah saya kenakan, baiklah."
ms "Bob memalingkan muka"
bob "Tidak, itu ... TAG_0__ sebaliknya, milik saya lebih bijaksana."
scene 126_mila_smile
bob "Ngomong -ngomong, kamu terlihat hebat ..."
ms "Untuk beberapa alasan, pujiannya membuat saya tersenyum dengan puas."
ms "Bob pergi ke kamar tidur, merayuk pakaiannya di sana sebentar, dan kembali ke ruang tamu."
bob "Erm ...__ tag_0__ ada di tempat tidur."
ms "Saya menarik ke kamarnya dan menutup pintu."
scene 126_bobs_room_uniform with fade
m "..."
if dom >= mila_dom:
    ms "Apakah Anda bercanda?"
    m "Bob, apakah kamu serius?"
    bob "S-Sorry ...__ tag_0__ i ..."
    bob "Ini ...__ tag_0__ ini adalah mimpiku sejak sekolah ..."
    m "Haaa ..."
    jump continue_126
ms "Hooo ..."
ms "Bob adalah anak laki -laki yang kotor ..."
ms "Saya lebih suka pakaian guru lebih banyak, tapi ini juga baik -baik saja"
ms "Saya bisa membayangkan bagaimana saya akan menggodanya di masa depan"

label continue_126:
scene 126_bobs_room_mila_changed
ms "Saya melepas pakaian saya dan berganti"
ms "Lebih baik tidak memikirkan di mana dia mendapatkan setelan ini dan apa yang dia lakukan dengannya."
m "..."
scene 126_bobs_room_mila_smirk
ms "Meskipun saya bisa membayangkan bagaimana dia tersentak di atasnya ...__ tag_0__ itu lebih menarik daripada menjijikkan."
m "..."
ms "Kapan saya menjadi cabul?"
scene 126_bobs_room_mila_changed
ms "Atau apakah saya selalu seperti ini? .."
if dom >= mila_dom:
    scene 126_living_room_mila_shy with fade
    m "..."
    ms "Saya pergi ke tengah ruangan."
    bob "..."
    m "..."
    bob "..."
    scene 126_living_room_mila_sad_smile
    m "Um ...__ tag_0__ bob?"
    ms "Bob tersentak"
    bob "S-Sorry .__ tag_0__ itu sangat cantik! __ tag_0__ Anda cantik!"
    scene 126_living_room_mila_giggle
    m "Hehe ..."
    m "Terima kasih."
    scene 126_living_room_mila_teasing
    m "Tapi serius, Bob ...__ tag_0__ saya sudah terlihat seperti remaja, tetapi Anda masih ingin mendandani saya dengan seragam sekolah?"
    bob "S-Sorry ..."
    scene 126_living_room_mila_giggle
    m "Tidak apa -apa .__ tag_0__ tapi jangan perhatikan, saya tidak akan menelepon Anda ayah .__ tag_0__ itu cringey ..."
    bob "..."
    ms "Bob tidak bisa berkata -kata dan hanya menatapku dengan mulut terbuka."
    jump continue_126_2
scene 126_living_room_mila_smug with fade
m "Selamat pagi, Bob, bisakah aku meminjam pekerjaan rumahmu?"
bob "..."
m "..."
scene 126_living_room_mila_teasing
m "Oh ...__ tag_0__ Anda ingin saya menyebut Anda sensei, kan?"
m "Tidak akan terjadi"
bob "..."
scene 126_living_room_mila_shy
m "Erm ...__ tag_0__ bob? __ tag_0__ halo?"
ms "Bob tersentak"
bob "S-Sorry! __ tag_0__ Saya hanya ...__ tag_0__ maksud saya ...__ tag_0__ wow ..."
scene 126_living_room_mila_giggle
m "Ahah"
m "Apakah Anda suka penampilan saya?"
bob "Ya Tuhan, ya!"
scene 126_living_room_mila_raised_eyebrow
m "Jadi tidak cukup bagi Anda bahwa saya sudah terlihat seperti remaja?"
m "Anda ingin mendandani saya seperti itu?"
bob "Saya minta maaf"
scene 126_living_room_mila_giggle
m "Jangan. Aku hanya mengacaukanmu."

label continue_126_2:
scene 126_living_room_mila_teasing
m "..."
m "Nah, apa selanjutnya?"
bob "Erm ...__ tag_0__ Bisakah Anda duduk di atas meja dan menyilangkan kaki?"
scene 126_living_room_mila_sitting_crossed_legs
m "..."
m "Seperti itu?"
bob "Ya."
ms "Bob mengeluarkan pensil dan mulai dengan panik menggeseknya di atas kertas."
m "..."
bob "..."
ms "Secara fisik saya merasakan tatapannya merangkak ke tubuh saya."
ms "Saya mendengar gemerisik stylus di kanvas"
ms "Suara itu mengirim menggigil ke tubuh saya .__ tag_0__ seolah -olah dia membimbingnya di sepanjang saraf saya yang terbuka."
ms "Saya mencoba untuk tidak bergerak, yang membuat saya merasa lebih seperti pameran di museum."
ms "Sesuatu yang harus dikagumi"
scene 126_living_room_mila_sitting_crossed_legs_nipples
ms "Kulit saya menjadi sensitif, dan karena itu, pakaiannya tampak berduri dan gatal"
ms "Saya ingin membuangnya"
ms "Saya membiarkan tatapannya membelai tubuh saya secara langsung, tanpa hambatan tambahan"
ms "Dan keheningannya hanya memperburuk perasaan ini."
scene 126_living_room_mila_sitting_crossed_legs_nipples_open_mouth
m "Apakah Anda pernah jatuh cinta?"
ms "Saya ingat pengakuannya dan segera merasa menyesal"
scene 126_living_room_mila_sitting_crossed_legs_nipples_worried
m "Maksudku, sebelum ..."
ms "Bob Froze sejenak"
scene 126_living_room_mila_sitting_crossed_legs_nipples
bob "Ya..."
m "..."
bob "Pertama kali di sekolah ..."
bob "Namanya ...__ tag_0__ Anna."
scene 126_living_room_mila_sitting_crossed_legs_nipples_warm_smile
m "Itu nama yang indah."
bob "Ya."
bob "Dia duduk di depan saya di sekolah menengah."
bob "Aku mengaguminya ... punggungnya."
scene 126_living_room_mila_sitting_crossed_legs_nipples_giggle_smirk
ms "Saya menyeringai."
m "__Tag_0__back__tag_1__ -nya?"
bob "Ya."
m "Maksudmu pantatnya?"
bob "..."
m "..."
bob "..."
bob "Bisakah sekarang Anda melepaskan dasi Anda, lepaskan kemeja Anda sedikit dan condong ke depan?"
ms "Suaranya yang menuntut membuatku menggigil"
scene 126_living_room_mila_sitting_leaning_forward
m "..."
m "Seperti ini?"
bob "Ya, sempurna."
ms "Pensil mulai merangkak melintasi kertas lagi."
scene 126_living_room_mila_sitting_leaning_forward_open_mouth
m "Apakah Anda mengakuinya?"
scene 126_living_room_mila_sitting_leaning_forward
bob "..."
bob "TIDAK."
ms "Sebelum saya bisa mengajukan pertanyaan berikutnya, Bob melanjutkan."
bob "She started dating one of the bullies.{w} His name was Billie. Billie \"the truck\"mereka memanggilnya"
m "Truk? __ tag_0__ kenapa begitu?"
bob "..."
bob "Dia entah bagaimana menyeret dua bek pada dirinya sendiri .__ tag_0__ mereka mulai memanggilnya seperti itu setelah itu."
m "Apakah ini sesuatu dari sepak bola atau lainnya?"
bob "Jenis .__ tag_0__ rugby."
bob "Nah, secara umum - dia kuat, populer, agresif, dan bodoh .__ tag_0__ klasik."
bob "Mengapa setiap gadis baik selalu tertarik pada douchebag?"
scene 126_living_room_mila_sitting_leaning_forward_open_mouth_sceptical
ms "Saya mengangkat bahu."
m "Tidak semua orang .__ tag_0__ Saya tidak pernah menyukai pamer, misalnya .__ tag_0__ Paul adalah seorang kutu buku."
scene 126_living_room_mila_sitting_leaning_forward
ms "Bob memotret saya, tetapi tidak mengomentari kata -kata saya."
bob "Kemudian nilainya semakin buruk."
bob "Dan kemudian dia benar -benar mulai berkencan dengan bayaran."
bob "Menurut rumor setidaknya ..."
scene 126_living_room_mila_sitting_leaning_forward_open_mouth
m "..."
m "Sudahkah Anda mencoba berbicara dengannya?"
bob "Siapa yang mau mendengarkan saya?"
scene 126_living_room_mila_sitting_leaning_forward_warm_smile
m "Saya akan."
bob "..."
m "..."
bob "Bisakah Anda duduk dengan punggung ke saya?"
scene 126_living_room_mila_sitting_from_behind
m "..."
m "Seperti ini?"
bob "Ya."
m "..."
bob "Dan..."
bob "Bisakah Anda juga ...__ tag_0__ mengangkat rok Anda?"
ms "Darah bergegas ke wajahku."
scene 126_living_room_mila_sitting_from_behind_lift
ms "Saya dengan patuh menarik rok saya dan menunjukkan pantat saya kepada Bob."
ms "Dia menelan."
bob "__Tag_0__oh Tuhan, kasihanilah aku ..."
m "..."
scene 126_living_room_mila_sitting_from_behind_lift_open_mouth
m "Dan apa yang terjadi selanjutnya? __ tag_0__ untuk gadis ini, maksud saya"
ms "Berbicara membantu saya untuk tidak terlalu memikirkan apa yang saya lakukan sekarang"
bob "..."
bob "Aku tidak tahu."
bob "Saya ...__ tag_0__ Saya marah padanya dan berhenti memperhatikan."
m "Hmm..."
bob "Saya pikir kemudian saya menyadari bahwa semua wanita berpikir dengan pussies mereka."
scene 126_living_room_mila_sitting_from_behind_lift_sceptical
m "Web lakukan?"
m "Dan kamu?"
bob "Bagaimana dengan saya?"
m "Apakah Anda tidak berpikir dengan penis Anda?"
bob "..."
m "Seks adalah sumber motivasi manusia tertua."
scene 126_living_room_mila_pants_pull
ms "Aku berdiri, berbalik ke samping ke Bob, meletakkan tanganku di bawah rokku dan menarik celana dalamku."
m "Semua yang kami lakukan adalah untuk seks atau tentang seks."
m "Dan dalam hal ini Anda tidak berbeda dari gadis itu."
ms "Celana saya menggantung di lutut saya. Hanya rok saya yang menutupi vaginaku."
ms "Bob terengah -engah dan membelai tonjolan di celananya."
ms "Tatapannya menjadi berat ... predator."
ms "Saya merasa seperti mangsa lagi."
ms "Saya merasa takut lagi .__ tag_0__ dan keinginan."
scene 126_living_room_mila_after
ms "Saya tertelan dan berdiri."
m "Saya pikir itu cukup untuk hari ini."
bob "Tapi kamu tidak telanjang!"
ms "Bob menatapku dengan marah."
m "Saya sedikit lebih takut, dan Anda tidak akan bisa menahan diri, dan Anda hanya akan menyerang saya."
m "Dan ini bukan apa yang Anda, dan saya sepakat."
ms "Bob meringis."
bob "Ini benar -benar bukan apa yang kami sepakati .__ tag_0__ Anda berjanji untuk berpose untuk saya __tag_1__naked__tag_2__"
ms "Bob mengerutkan kening"
scene 126_mila_after_door
ms "Sudah di pintu aku berhenti, berbalik dan menatap Bob."
m "Aku menjanjikanmu itu"
m "Dan saya akan"
bob "..."
m "Dan agar Anda tidak berpikir bahwa saya tidak menepati janji saya."
scene 126_mila_after_skirt_lift
m "..."
bob "..."
m "Selamat malam, Bob."
"..."


play sound "door-open-close.mp3"
scene bg door with fade
ms "..."
show mila schoolgirl_pout at center:
    xpos 0.6
ms "Meskipun saya menghabiskan lebih dari satu jam dengan Bob, Paul belum kembali."
ms "Dia meluangkan waktu hari ini"
show mila walk_achoo
m "Achoo!"
ms "..."
show mila walk_thoughtful
ms "Apakah karena debu?"
ms "Saya harus membersihkan setidaknya sedikit ..."
scene bg apartments with fade
ms "Paul pulang segera, ketika saya berganti pakaian."
show paul suit_open_mouth_blush at left
p "Sayang aku ho ... woah .__ tag_0__ wow!"
show mila slutty_smirk
m "Bagaimana Anda menyukai pakaian saya?"
if dom >= mila_dom:
    show paul suit_smirk
    p "Sangat indah!"
    p "Anda terlihat seperti pelacur sungguhan"
    show mila slutty_embarassed
    m "I ...__ tag_0__ itu niat saya ..."
    p "Berbalik .__ tag_0__ tunjukkan pantatmu"
    show mila slutty_from_behind
    p "..."
    p "Mmm ...__ tag_0__ celana pendek yang bagus."
    show mila slutty_from_behind_smirk
    m "Terima kasih ...__ tag_0__ master."
    jump walk_126_continue_1

show paul suit_blush_looking_aside
ms "Paul memalingkan muka dan memerah"
ms "Aku menggerakkan pahaku."
m "Izinkan saya memberi Anda petunjuk - saya terlihat seperti pelacur, kan?"
ms "Paul menembakkan matanya padaku."
ms "Aku memunggungi dia."
show mila slutty_from_behind_ass_support
m "Lihat pantat ini."
m "Anda benar -benar ingin memukulnya, bukan?"
ms "Paul menelan."
show mila slutty_from_behind_grin
m "Ahah .__ tag_0__ Maaf, saya tidak bermaksud untuk menggodamu terlalu banyak."
m "Apakah kamu menyukainya?"
p "... Ya."
m "Saya senang."

label walk_126_continue_1:
show paul suit_open_mouth_neutral
p "Ngomong -ngomong, aku sekarat karena kelaparan."
show mila slutty_awkward
m "Um ..."
m "Kamu tahu..."
m "Masalahnya adalah ...__ tag_0__ Saya tidak memasak apa pun hari ini."
ms "Paul menatapku"
p "Sesuatu terjadi?"
m "Tidak terlalu..."
show mila slutty_awkward_smile
m "Saya berbaring di tempat tidur saya sepanjang hari dan menonton film porno"
show paul suit_smirk
p "..."
m "..."
p "Kedengarannya ... tangguh ..."
m "..."
p "..."
show mila slutty_giggle
show paul suit_grin
m "Pfff! ha ha ha!"
ms "..."
if dom >= mila_dom:
    show paul suit_smirk
    ms "Seringai merayap ke wajah Paul."
    p "Haruskah kita berjalan -jalan?"
    show mila slutty_smirk
    m "Dengan senang hati! Izinkan saya mengganti pakaian saya"
    p "TIDAK."
    show mila slutty_concerned
    m "? .."
    p "Anda akan masuk ini. Anda tidak hanya berpakaian seperti itu"
    p "Saya bahkan akan menambahkan sesuatu."
    scene 126_slutty_mila_before_walk
    m "..."
    jump walk_126_continue_2

show paul suit_open_mouth_neutral
p "Um ... mungkin kita bisa makan di suatu tempat?"
show mila slutty_smirk
m "Ayo."
ms "Paul tersenyum puas."
ms "Saya menuju pintu keluar."
m "Ayo pergi?"
show paul suit_open_mouth_blush
p "..."
p "Erm ..."
p "Anda tidak akan pergi ke luar seperti itu, bukan?"
show mila slutty_concerned
ms "Saya melihat diri saya sendiri"
m "Oh, benar ...__ tag_0__ Maaf, beri aku sedikit detik."
"..."
scene 126_slutty_mila_before_walk
m "..."
m "Itu lebih baik?"
p "..."
p "Anda ingin pergi seperti itu?"
m "Ya"
p "..."
label walk_126_continue_2:
m "Bagaimana penampilan saya?"
p "..."
ms "Paul tersenyum."
p "Cantik, sayang."
m "Jadi? __ tag_0__ ayo pergi?"
ms "..."
scene bg park with fade
ms "Matahari belum sepenuhnya terbenam di bawah cakrawala .__ tag_0__ Sinarnya melukis taman ratusan nada kuning."
ms "Angin hangat mengacak -acak rambut saya dan membelai kulit telanjang saya dengan sentuhan lembut."
ms "Bau manis bunga dan aroma segar rumput dicampur dengan aroma makanan yang disiapkan di nampan."
ms "Saya baru saja menyadari betapa saya ingin makan."
ms "Perut Paul menggeram dengan keras."
scene 126_walk_date_grin
ms "Kami saling memandang."
m "Ahah .__ tag_0__ bagaimana dengan jagung rebus?"
p "Tidak, saya ingin sesuatu yang lebih bergizi."
ms "Saya terus-menerus menangkap pandangan orang yang lewat sementara kami mencari tempat makan."
ms "Setelah memilih bangku kecil Meksiko, kami duduk di kursi tinggi."
scene 126_walk_date_cafe
ms "..."
ms "Paul melihat sekeliling dengan gugup sebentar."
ms "Saya sangat lapar sehingga saya tidak segera memahami alasan perhatiannya."
ms "Tetapi begitu saya mengisi perut saya, saya menyadari bahwa mata hampir semua orang di sekitar saya diarahkan pada saya."
scene 126_walk_date_cafe_aroused
ms "Aku menelan dan merasa hampir telanjang."
m "..."
ms "Yah ... __tag_0__i praktis telanjang."
ms "..."
scene 126_walk_date_cafe_aroused_biting_lip
ms "Saya sedikit mencondongkan tubuh ke depan"
m "Apakah Anda pikir mereka bisa melihat pantat saya dengan baik?"
if dom >= mila_dom:
    p "Saya pikir mereka akan dengan senang hati melakukan celana pendek Anda dan meniduri Anda tepat di kursi ini."
    scene 126_walk_date_cafe_smirk
    m "Hmmm ...__ tag_0__ menurutmu begitu?"
    m "Apakah Anda ingin melihatnya?"
    p "Sangat. Sialan. Banyak."
    jump walk_126_continue_3

ms "Paul memandang rendah rasa malu."
scene 126_walk_date_cafe_smirk
m "Saya bisa menarik celana pendek saya sekarang dan mengambil tangan Anda."
m "Dan beberapa orang bodoh akan duduk di belakangku dan bercinta denganku"
p "..."
m "Bayangkan wajah saya pada saat itu."
scene 126_walk_date_cafe_pretend with dissolve
pause 0.5
scene 126_walk_date_cafe_smirk
ms "Paul menelan."
m "hehe"
label walk_126_continue_3:
scene bg park with fade
ms "Ketika kami selesai makan, Paul menatapku dengan aneh dan mengundangku untuk berjalan di taman."
ms "..."
show mila slutty_concerned at right
ms "Sebenarnya, ini aneh - Paul tidak terlalu suka berjalan"
ms "Aku meliriknya dengan curiga"
m "Apakah Anda merencanakan sesuatu?"
show paul suit_smirk at center
ms "Paul hanya tersenyum dan mengulurkan tangannya kepada saya."
m "..."
show mila slutty_idle:
    easein 0.7 xpos 0.8
ms "Saya masih merasa tidak yakin pada tumit, jadi saya meraih Paul."
ms "Untungnya, kami berjalan perlahan, jadi saya menjaga keseimbangan dengan mudah"
ms "Dan saya benar -benar merasakan bagaimana tumit menyoroti pantat saya"
show mila slutty_from_behind_ass_support
ms "Hampir setiap orang yang lewat menatap kaki dan pantat saya"
ms "Wanita dan orang tua mengerutkan kening dan menggerutu sesuatu di bawah napas."
ms "Seorang nenek bahkan dengan jelas menyebut saya pelacur"
show mila slutty_from_behind_grin
ms "Saya hanya tersenyum kembali"
ms "Orang -orang menoleh dan mengikuti kami dengan pandangan mereka."
ms "Saya melirik Paul. Dia berseri -seri dengan bangga."
show mila slutty_proud
m "Heh."
ms "Reaksinya memberi saya lebih percaya diri, menyebabkan saya meluruskan punggung saya dan mulai mengguncang pinggul saya lebih banyak."
show mila slutty_concerned
ms "Kemana kita sebenarnya pergi?"
ms "Hampir tidak ada orang di bagian taman ini."
ms "Saya menatap paul dengan bertanya."
show paul suit_grin
ms "Dia hanya menyeringai."
m "..."
ms "Oke, mari kita lihat apa yang dia hasilkan."
m "..."
ms "Kami menemukan bangku gratis dan duduk."
show mila slutty_awkward
ms "Saya melihat sekeliling .__ tag_0__ itu tidak sepenuhnya sepi, tetapi ada orang yang lewat pada jarak tertentu."
ms "Saya berharap Paul tidak ingin berhubungan seks di sini ..."
ms "Seseorang pasti akan memanggil polisi ..."
show mila slutty_concerned
m "..."
ms "Dan apakah satu -satunya hal yang mengganggu saya?"
m "..."
show mila slutty_giggle
ms "Hah."
ms "..."





label hscene_netorase_park:
scene bg park
show mila slutty_giggle at right:
    xpos 0.8
show paul suit_grin at center
p "Apakah Anda melihat pria itu?"
show mila slutty_idle
ms "Saya muncul dari pikiran saya."
m "Mmm? __Tag_0__ di mana? __ tag_0__ yang itu dengan ransel? __ tag_0__ ya, bagaimana dengan dia?"
p "Dia terlihat kesepian."
show mila slutty_concerned
m "Erm ...__ tag_0__ yeah ...__ tag_0__ dia .__ tag_0__ pria miskin."
ms "Saya tidak mengerti apa kesepakatan Paul"
p "Mengingatkan saya sedikit Bob, bukan?"
show mila slutty_suspicious
m "..."
ms "Apa yang dia dapatkan?"
m "Maaay-be?"
show paul suit_smirk
p "Saya pikir dia perlu terinspirasi entah bagaimana ...__ tag_0__ apa yang Anda katakan?"
m "Terinspirasi?"
p "..."
show mila slutty_surprised
m "..."
m "Apakah kamu memintaku? .."
p "..."
show mila slutty_surprised2
m "Anda tidak serius, bukan?"
p "..."
show mila slutty_serious
m "Apakah kamu serius?"
p "Ya."
m "..."
show mila slutty_concerned
m "And how can I \"inspire\"dia?"
p "Hmmm ...__ tag_0__ baik, Anda tahu lebih baik dari saya ..."
m "Jadi terserah saya untuk memutuskan?"
p "..."
p "Ya."
show mila slutty_awkward
m "..."
p "..."
m "Saya tidak memiliki kondom."
show paul suit_open_mouth_neutral
ms "Paul mengangkat alisnya."
p "Wow. Apakah Anda berencana untuk menginspirasi dia sebanyak itu?"
show mila slutty_frown
m "Lalu apa maksudmu?"
show paul suit_open_mouth_blush
p "Erm ...__ tag_0__ maksud saya ...__ tag_0__ ya, pada prinsipnya itu akan menginspirasi ..."
show mila slutty_suspicious
m "Sebenarnya, saya berpikir untuk memberinya blowjob .__ tag_0__ dengan kondom."
p "Ah ...__ tag_0__ ok ..."
show mila slutty_frown
m "Ok?{w} Is it \"OK!\" type of ok,{w} or an \"I get it\"jenis ok?"
p "It's \"OK\"..."
show mila slutty_surprised
ms "Oke?.."
show mila slutty_surprised2
ms "OKE?!"
ms "Saya tidak punya banyak waktu untuk memproses apa yang baru saja dikatakan Paul"
m "!"
m "Sial, dia akan pergi!"
scene 126_walk_date_lee_meeting_1
ms "Mematuhi dorongan tiba -tiba, saya melompat dan berlari"
ms "Saya tidak tahu apa yang akan saya lakukan ketika saya mengejar dia"
ms "Dan saya tidak tahu bagaimana saya tidak bunuh diri saat berlari dengan sepatu hak tinggi"
scene 126_walk_date_lee_meeting_2
m "Tunggu!"
m "Maaf!"
ms "Pria itu menatapku"
"???" "Um ...__ tag_0__ apakah kamu berbicara denganku?"
scene 126_walk_date_lee_meeting_3
m "Ya!"
m "Bisakah Anda membantu saya?"
"???" "...__ tag_0__ um ...__ tag_0__ maaf, saya tidak punya uang ..."
ms "Pria itu menurunkan matanya."
scene 126_walk_date_lee_meeting_4
ms "Hah .__ tag_0__ dia benar -benar mengingatkan saya pada Bob dalam beberapa hal."
m "Tidak apa-apa."
ms "Pria itu menatapku dengan curiga dan menurunkan tatapannya lagi."
ms "Jadi ...__ tag_0__ jadi apa selanjutnya?"
ms "Saya tidak bisa hanya menawarkan pekerjaan pukulan padanya, bukan?"
scene 126_walk_date_lee_meeting_5
m "Erm ..."
ms "Saya melihat lebih dekat pada pria itu."
ms "Saya telah melihat lencana ini di suatu tempat ..."
ms "Sepertinya itu dari beberapa jenis permainan ..."
ms "Hmmm...{w} \"OverSee\"atau sesuatu?"
ms "Benar, ini permainan yang Bob katakan padaku tentang"
scene 126_walk_date_lee_meeting_6
m "Erm,{w} listen,{w} are you a fan of \"OverSee\"?"
ms "Pria itu menatapku dengan terkejut."
"???" "Um ...__ tag_0__ yah ya ..."
m "Dengar, saya melakukan cosplay dari satu karakter ..."
m "Tapi saya tidak tahu banyak tentang itu, bisakah Anda melihatnya?"
scene 126_walk_date_lee_meeting_6
"???" "Baiklah, oke."
ms "Saya menunjukkan kepadanya fotonya."
"..."
ms "Pria itu meluncurkan penjelasan panjang tentang bagaimana cosplay saya mengisap, dan apa yang perlu diubah."
ms "Saya berpura -pura mendengarkan dengan cermat dan mengangguk."
ms "Pria itu, tampaknya merasakan kepura -puraanku, mengerutkan kening."
scene 126_walk_date_lee_meeting_8
"???" "Mengapa Anda menginginkannya? Apakah Anda bersiap -siap untuk komiket?"
m "Ya, saya ..."
ms "I started scrolling through the photos and \"accidentally\"menunjukkan beberapa selfie telanjang saya"
scene 126_walk_date_lee_meeting_9
m "Oopsie."
m "Maaf."
ms "Pria itu tersipu"
"???" "..."
m "..."
"???" "Apakah Anda melakukannya untuk Onlyfans?"
scene 126_walk_date_lee_meeting_10
ms "Whaaa? .."
m "Um ...__ tag_0__ Onlychans?"
"???" "Jangan bermain bodoh."
"???" "Anda ingin membuat video reaksi saya terhadap telanjang Anda, benarkah saya benar?"
ms "Apakah dia pikir ini semacam lelucon orang dewasa?"
ms "Saya bisa menggunakan ini, saya pikir ..."
scene 126_walk_date_lee_meeting_11
m "Tidak, sebenarnya, saya ingin membuat beberapa ... jenis konten yang berbeda ..."
ms "Pria itu mengerutkan kening."
m "..."
m "Saya ingin Anda memfilmkan saya saat saya menghisap penis Anda"
scene 126_walk_date_lee_meeting_12
"???" "W-apa?"
m "Nah, __ tAG_0__ jika Anda tidak keberatan tentu saja."
m "Saya akan menghisap Anda, dan Anda akan merekamnya."
m "Untuk satu -satunya Chance saya."
"???" "Onlyfans."
m "Benar .__ tag_0__ Itulah yang saya katakan."
ms "Apa pun"
"???" "..."
"???" "O-OK ..."
scene 126_walk_date_lee_meeting_13
m "Ayo pergi."
"???" "__Tag_0__i berharap saya tidak akan dibunuh di sana ..."
ms "Aku dengan cepat berbalik dan mengedipkan mata pada Paul, lalu mengambil tangan lelaki itu dan membawanya ke toilet umum."
"..."
scene 126_walk_date_lee_toilet_1 with fade
m "Agak sempit di sini ..."
m "Saya tidak akan menutup kios, oke?"
m "Saya harap kami tidak akan tertangkap"
m "Apakah Anda kebetulan memiliki kondom?"
"???" "Ya!"
scene 126_walk_date_lee_toilet_2
m "Manis! Terkunci dan dimuat, ya? Ahah"
"???" "Saya memilikinya untuk keberuntungan."
m "Dan seperti yang Anda lihat, Anda beruntung"
ms "Dia memberiku kondom."
scene 126_walk_date_lee_toilet_3
m "Terima kasih."
m "Apakah Anda suka blowjobs?"
"???" "I ...__ tag_0__ tidak tahu ...__ tag_0__ kurasa?"
ms "Apakah ini pertama kalinya?"
ms "..."
scene 126_walk_date_lee_toilet_4
ms "Manis"
m "Oh ok, itu bukan masalah besar."
m "Apakah Anda ingin saya melepas celana Anda?"
"???" "N-no, saya akan melakukannya sendiri"
m "Tentu."
ms "Pria itu buru -buru membuka kancing celana jinsnya."
ms "Tiba -tiba itu mengejutkan saya apa yang sedang terjadi"
ms "Tapi untuk beberapa alasan saya tidak merasa tidak enak sama sekali"
ms "Saya merasa mengendalikan situasi"
ms "Dan itulah mengapa ...__ tag_0__ itu menyenangkan"
scene 126_walk_date_lee_toilet_3
m "Luangkan waktu Anda, saya tidak ke mana -mana."
ms "..."
"???" "W-Why? Saya tidak..."
ms "Penisnya tetap lembut"
"???" "Ayo! Bangunlah!"
ms "Dia dengan kejang meraih penisnya yang lembek dan mulai menghancurkannya"
scene 126_walk_date_lee_toilet_2
m "Hati -hati, Anda akan merobeknya."
"???" "Nah ... kenapa sekarang!?"
ms "Pria itu siap menangis"
scene 126_walk_date_lee_toilet_4
m "Anda hanya gugup. Lihat aku."
"???" "..."
m "Lihat aku."
ms "Dia mendongak."
scene 126_walk_date_lee_toilet_5
m "Semuanya baik -baik saja, jangan khawatir."
m "Nama saya Mila, __ TAG_0__ Apa milik Anda?"
"???" "..."
"???" "Lee ..."
scene 126_walk_date_lee_toilet_6
m "Lee?"
m "Itu nama yang menarik, __ tag_0__ adalah orang tuamu dari Cina?"
"???" "Tidak .__ tag_0__ orang tuaku idiot."
scene 126_walk_date_lee_toilet_2
m "Ahah, maaf."
scene 126_walk_date_lee_toilet_1
m "Apakah Anda menyukai saya, Lee?"
"???" "...__ tag_0__ ya, kamu cantik ..."
scene 126_walk_date_lee_toilet_2
m "Ahah .__ tag_0__ terima kasih."
scene 126_walk_date_lee_toilet_5
m "Apakah Anda ingin menyentuh payudara saya, Lee?"
"???" "Bolehkah saya?"
m "Tentu!"
scene 126_walk_date_lee_toilet_7
ms "Saya meletakkan tangan saya di belakang."
ms "Pria itu meraih putingku dan mencubitnya dengan keras"
scene 126_walk_date_lee_toilet_8
m "Aduh!"
m "Tidak terlalu kasar"
"???" "S-Sorry ..."
m "Tidak ada .__ tag_0__ Just ...__ tag_0__ menjadi lembut, oke?"
"???" "..."
scene 126_walk_date_lee_toilet_9
m "Menyukai?"
"???" "Ya, sangat banyak!"
scene 126_walk_date_lee_toilet_10
m "(heh)"
m "Anda dapat menarik top down saya .__ tag_0__ Anda ingin melihatnya juga, kan?"
ms "Pria itu menelan dan menarik ke bawah"
scene 126_walk_date_lee_toilet_11
"???" "Wow..."
m "Apakah Anda menyukai titties saya?"
"???" "..."
m "Saya melihat Anda melakukannya"
ms "Saya mengarahkan jari saya ke penisnya."
m "Sekarang, dia sudah siap."
"???" "Y-ya ..."
m "Ini ponsel saya .__ tag_0__ Bisakah Anda duduk? __ tag_0__ Anda dapat merekam saya sesuka Anda."
m "Siap?"
"???" "..."
"???" "Ya."
scene 126_walk_date_lee_record_1 with fade
m "Halo semuanya, hari ini saya bertemu pria yang luar biasa di taman ini."
m "Namanya Lee .__ TAG_0__ Sapa semua orang, Lee!"
ms "Saya langsung masuk ke peran itu."
ms "Sejujurnya, saya menikmati situasi ini."
"???" "H-hi semuanya ...__ tag_0__ saya lee."
m "Lee tidak bisa menahan diri untuk meraba -raba saya sebelum rekaman dimulai."
scene 126_walk_date_lee_record_2
m "Lihatlah puting merah saya, itu karena Lee meraihnya dengan sekuat tenaga."
"???" "B-tapi katamu ..."
m "Tidak apa -apa, saya bercanda."
scene 126_walk_date_lee_record_3
m "Nah Lee di sini memberi tahu saya bahwa dia menginginkan blowjob dari saya"
m "Apakah itu benar?"
"???" "Y-ya ..."
m "Saya harus sampai ke sana."
m "Izinkan saya menunjukkan sedikit trik"
ms "Saya membuka kondom dan memasukkannya ke dalam mulut saya."
scene 126_walk_date_lee_record_4
ms "Aku berjongkok, mengambil penisnya, dan mengarahkannya ke mulutku, menarik kondom sepanjang seluruhnya."
scene 126_walk_date_lee_record_5
"..."
scene 126_walk_date_lee_record_6
"..."
scene 126_walk_date_lee_record_7
ms "Kontolnya lebih kecil dari pada Bob, tetapi masih menekan tenggorokan saya."
ms "Jadi saya harus membantu diri saya dengan tangan saya."
scene 126_walk_date_lee_record_8
"..."
m "Dan sudah selesai"
if dom >= mila_dom:
    ms "Pelajaran Paul terlintas dalam pikiran"
    scene 126_walk_date_lee_record_9
    "..."
    scene 126_walk_date_lee_record_10
    "..."
    scene 126_walk_date_lee_record_11
    ms "Saya mengumpulkan air liur sebanyak mungkin dan perlahan mulai menundukkan kepala sampai penisnya mengenai tenggorokan saya."
    scene 126_walk_date_lee_record_12
    ms "Lalu saya mencoba untuk bersantai dan tertelan"
    scene 126_walk_date_lee_record_13
    ms "Dick meluncur lebih dalam"
    "???" "Ooohhhh fuck ..."
    "???" "Astaga..."
    scene 126_walk_date_lee_record_14
    ms "Penisnya berbau sesuatu yang asam"
    ms "Di sini dia juga menyerupai Bob."
    m "Mmm ..."
    scene 126_slutty_blowjob
    m "..."
    m "*payah*__ tag_0 __*payah*__ tag_0 __*payah*__ tag_0__"
    m "..."
    ms "Saya mencoba untuk rileks, mengambilnya sedalam yang saya bisa, dan menjulurkan lidah untuk menjilat bolanya"
    scene 126_walk_date_lee_record_16
    m "..."
    "???" "Ohhh wow ..."
    ms "..."
    scene 126_walk_date_lee_record_17
    m "*batuk*"
    scene 126_walk_date_lee_record_16
    m "..."
    scene 126_walk_date_lee_record_17
    m "*batuk*"
    scene 126_walk_date_lee_record_18
    ms "..."
    scene 126_walk_date_lee_record_19
    ms "..."
    scene 126_walk_date_lee_record_20
    m "Haa ...__ tag_0__ haaa ...__ tag_0__ haaa ..."
    "???" "Apakah kamu baik -baik saja?"
    scene 126_walk_date_lee_record_21
    m "Tentu"
    m "Apakah kamu menyukainya?"
    "???" "Ya! Itu luar biasa!"
    scene 126_walk_date_lee_record_22
    m "Ahah."
    m "Saya senang Anda menyukainya"
    scene 126_walk_date_lee_record_23
    ms "Saya merasa bahwa saya sudah cukup hangat."
    ms "Jadi saya menginginkan sesuatu yang lebih."
    ms "Saya ingin merasa seperti ... sesuatu lagi ..."
    ms "Saya hanya cum dump ..."
    scene 126_walk_date_lee_record_24
    m "Apakah Anda ingin ...__ tag_0__ bercinta tenggorokan saya?"
    "???" "W-apa?"
    m "Berdiri"
    "..."
    scene 126_walk_date_facefucking_1 with fade
    ms "Saya meletakkan tangan saya di belakang."
    m "Persetan mulutku, Lee."
    ms "Saya membuka mulut saya dan menjulurkan lidah saya."
    "???" "Wow..."
    scene 126_walk_date_facefucking_2
    ms "Lee dengan ragu -ragu meletakkan tangannya di kepalaku dan dengan lembut mendorong kemaluannya ke dalam mulutku."
    scene 126_walk_date_facefucking_3
    ms "Saya mencoba tersenyum dengan penisnya di mulut saya untuk mendorongnya"
    ms "Jangan khawatir anak besar, kamu tidak akan menghancurkanku"
    scene 126_slutty_irrumatio_slow
    m "..."
    ms "Lee begitu berangkat, sehingga membuatku tersenyum"
    ms "Nah ...__ tag_0__ tidak secara harfiah ...__ tag_0__ kemaluannya mengebor mulut saya, jadi saya tidak bisa senyum yang sebenarnya"
    ms "Tapi dia tidak pernah mendorongnya dengan kekuatan penuh"
    ms "Mungkin itu sebabnya saya hampir tidak mengalami ketidaknyamanan."
    ms "Vagina saya gatal karena keinginan."
    ms "Ayo anak besar, Anda bisa mendorongnya lebih dalam ..."
    ms "Gunakan aku ..."
    ms "Saya harus menunjukkan kepadanya, bahwa dia bisa sedikit lebih kasar"
    ms "Saya mulai menambahkan tekanan dan kecepatan"
    scene 126_slutty_irrumatio_fast
    ms "..."
    ms "Ya..."
    ms "Persetan denganku ..."
    ms "Gerakan Lee menjadi lebih kasar .__ tag_0__ Mungkin dia melihatnya di mata saya .__ tag_0__ saya menginginkannya"
    scene 126_walk_date_facefucking_4_1
    ms "Dia berhenti sejenak untuk mengumpulkan kuncir kuda saya untuk cengkeraman yang lebih baik"
    ms "Saya tidak menghentikannya"
    ms "Dan kemudian dia baru saja mulai meniduri kepalaku."
    scene 126_slutty_irrumatio_fast_2
    ms "Langkahnya menjadi lebih cepat, dan juga dia mulai memberikan lebih banyak tekanan"
    ms "Saat itulah kemaluannya akhirnya meluncur ke tenggorokan saya"
    scene 126_walk_date_facefucking_6clean
    m "*muntah*"
    ms "Lee berhenti"
    ms "Saya tidak yakin mengapa ... __tag_0__meybe dia menikmati momen__tag_0__ atau hanya takut untuk melanjutkan"
    scene 126_walk_date_facefucking_6
    ms "Terlepas dari air mata berlari, saya mencoba mendorongnya."
    ms "Gunakan saya seperti anak pelacur besar ...__ tag_0__ saya tidak keberatan"
    ms "Lee mendorong kemaluannya lebih dalam"
    scene 126_walk_date_facefucking_7
    m "*Muntah*"
    scene 126_walk_date_facefucking_8_cough
    m "*batuk*"
    scene 126_walk_date_facefucking_8
    ms "Saya hanya cum dump ..."
    scene 126_walk_date_facefucking_8_cough
    m "*batuk*"
    scene 126_walk_date_facefucking_8
    ms "Saya hanya cum dump ..."
    "???" "Oh fuck, aku akan cum!"
    ms "Pria itu menempelkan perutnya ke hidungku dan mendorong penisnya jauh ke tenggorokanku"
    ms "Saya merasakan bagaimana kemaluannya mulai berdenyut di dalam"
    scene 126_walk_date_facefucking_7
    "???" "Yeees !!!"
    scene 126_walk_date_facefucking_8_cough
    "???" "Sialan ..."
    scene 126_walk_date_facefucking_8a
    "???" "Ya"
    scene 126_walk_date_facefucking_8_cough
    "???" "Oooh ..."
    scene 126_walk_date_facefucking_8aa
    ms "Kondom itu membentang di tenggorokan saya."
    ms "Saya merasakan sperma menumpuk di dalamnya."
    m "..."
    ms "Akhirnya dia bersandar dan menarik penisnya."
    scene 126_walk_date_facefucking_9
    m "Haaa ...__ tag_0__ haaaaa"
    "???" "Kamu tidak apa apa?"
    scene 126_walk_date_facefucking_10
    m "Ahaha .__ tag_0__ jangan khawatir, saya baik -baik saja"
    "..."
    scene 126_walk_date_facefucking_10a
    ms "Saya dengan hati -hati menarik kondom dari penisnya dan mengikatnya."
    ms "Saya akan memberikannya kepada Paul nanti."
    ms "Wajah saya mungkin berantakan ... Saya perlu sedikit segar"
    jump walk_126_continue_4

scene 126_slutty_blowjob_lazy
ms "Saya mulai mengisap penisnya, membantu diri saya sendiri dengan tangan"
m "..."
"???" "Ohh ya ..."
"???" "Ya Tuhan ..."
ms "Gatal di vaginaku ..."
ms "Saya bertanya -tanya bagaimana Paul akan bereaksi jika saya mengendarai anak ini sekarang"
ms "Sial, ini tak tertahankan ..."
ms "Saya ingin cum ..."
ms "Tapi aku seharusnya tidak ..."
ms "..."
ms "Tunggu, __ tag_0__ Apa yang akan terjadi jika saya datang?"
m "..."
ms "Saya akan mematahkan kepercayaan Bob."
ms "Dan dia tidak akan mempercayai saya lagi?"
ms "Ayo."
m "..."
scene 126_walk_date_lee_record_dom_1
ms "Saya tidak melihat bagaimana tangan saya berakhir di celana pendek saya."
m "Mmm ..."
ms "Saya ingin penis, saya ingin penis, saya ingin penis."
ms "Hell With It!"
scene 126_walk_date_lee_record_dom_2
ms "Saya berdiri dan menarik celana pendek saya dan melepas atasan saya"
ms "Lee menelan"
scene 126_walk_date_lee_record_dom_3
ms "Rasanya menyenangkan telanjang di tempat umum ...__ tag_0__ dan membebaskan"
m "Maaf, saya sedikit terlalu berlebihan"
m "Maukah Anda jika saya mengubah jenis layanan?"
"???" "Erm ..."
scene 126_walk_date_lee_record_dom_4
m "Aku ingin penismu di sini"
ms "Mata hitam kamera melacak setiap gerakan"
ms "Saya membayangkan bagaimana Paul akan menonton rekaman"
ms "Mmm ... __tag_0__i ingin menggodanya lebih banyak ..."
m "Bersandar sedikit"
scene 126_walk_date_lee_record_dom_5 with fade
ms "Saya mengambil penisnya dan memasukkannya ke dalam vaginaku"
m "Ohhh fffuck ..."
ms "Saya siap untuk cum pada detik itu"
ms "Tapi saya memberi diri saya waktu untuk membiasakan diri dengan sensasi"
scene 126_walk_date_lee_record_dom_5a
m "Mmm ..."
ms "Sangat menyenangkan untuk menjaga diri Anda tetap berada di tepi ..."
ms "Mungkin saya harus benar -benar mencoba untuk tidak cum?"
scene 126_walk_date_lee_record_dom_6
ms "Saya mulai menggosok vaginaku di penisnya"
"???" "..."
ms "Lee menatapku seperti tikus kecil"
scene 126_walk_date_lee_record_dom_7
ms "Kamu sangat lucu."
scene 126_walk_date_lee_record_dom_7a
m "Apakah Anda menyukai vagina saya, Lee?"
scene 126_walk_date_lee_record_dom_7
"???" "Y-ya ..."
scene 126_walk_date_lee_record_dom_7a
m "Mmm ..."
scene 126_walk_date_lee_record_dom_7
m "Apakah Anda ingin saya duduk lebih rendah?"
scene 126_walk_date_lee_record_dom_7a
"???" "Ya! Silakan!"
scene 126_walk_date_lee_record_dom_7aa
m "Ahah"
scene 126_walk_date_lee_record_dom_7a
m "Maukah Anda cum untuk saya jika saya duduk lebih rendah?"
scene 126_walk_date_lee_record_dom_7
"???" "Saya pikir begitu ...__ tag_0__ saya di tepi, nona ..."
ms "Saya sendirian ...__ tag_0__ jika saya mulai bergerak lebih banyak saya mungkin juga cum"
scene 126_walk_date_lee_record_dom_7a
m "Apakah Anda ingin cum di vagina saya? Atau di mulutku?"
"???" "Di vagina!"
scene 126_walk_date_lee_record_dom_7aa
m "Ahah."
scene 126_walk_date_lee_record_dom_7a
m "Bagus."
scene 126_walk_date_lee_record_dom_8
m "Cum untukku Lee."
scene 126_walk_date_lee_record_dom_9
m "Cum di vaginaku."
scene 126_walk_date_lee_record_dom_8
"???" "Ahhh"
scene 126_walk_date_lee_record_dom_9
"???" "Ya!!!"
scene 126_walk_date_lee_record_dom_10
ms "Aku merasakan ayam Lee mulai berdenyut, memompa sperma ke kondom."
ms "Saya mendapati diri saya berpikir bahwa saya ingin dia datang tanpa kondom."
ms "Stimulasi vagina hampir membawa saya ke orgasme, jadi saya harus menahan diri dengan sekuat tenaga."
ms "Fuck! __ tag_0__ bob harus bercinta denganku sangat bagus untuk mengimbangi ini ..."
"???" "Haa ... haaa ... haaa ..."
scene 126_walk_date_lee_record_dom_11
ms "Setelah menarik napas sedikit, saya menarik penisnya"
ms "Lalu aku melepas kondom dan mengikatnya."
ms "Saya akan memberikannya kepada Paul sebagai piala."

label walk_126_continue_4:
scene 126_walk_date_after_light_smile with fade
ms "Aku memperbaiki pakaianku dan sedang menunggu Lee berpakaian"
ms "Pussy saya yang basah kuyup, menuntut perhatian"
ms "Sensasi itu membuat semua pikiran saya pergi"
ms "Saya tidak memberikan banyak pemikiran tentang apa yang baru saja terjadi"
ms "Saya hanya ingin berhubungan seks ..."
scene 126_walk_date_after_worried
ms "Saya melihat Lee. Dia duduk di toilet, tenggelam dalam pikirannya"
ms "Lee sangat tenang"
m "Apakah semuanya baik -baik saja?"
ms "Dia tersentak"
"???" "Ya ...__ tag_0__ saya hanya ... __tag_0__ Ini adalah hari terbaik dalam hidup saya."
scene 126_walk_date_after_grin
m "Ah..."
m "Saya senang mendengarnya .__ tag_0__ terima kasih atas waktu Anda, saya juga menyukainya"
ms "Saya mengambil telepon saya darinya dan meluruskan pakaian saya."
scene 126_walk_date_after_light_smile
m "Oke, saya akan pergi .__ tag_0__ terima kasih lagi."
"???" "Wait!"
scene 126_walk_date_after_surprised
m "Mmm?"
ms "Saya berbalik."
"???" "C-can saya mengambil fotomu?"
"???" "Foto memori ..."
scene 126_walk_date_after_worried
ms "Saya memikirkannya."
ms "Di satu sisi, saya sudah membagikan foto saya dengan orang asing."
ms "Di sisi lain ... ini masih sangat berisiko."
if mila_dom > dom:
    ms "Aku baru saja menidurinya."
else:
    ms "...__ tag_0__i baru saja menghisapnya ..."
ms "Apa yang bisa lebih berisiko dari itu?"
scene 126_walk_date_after_grin
m "Jika Anda ingin pamer ...__ tag_0__ akan lebih baik untuk mengambil selfie bersama, bukankah menurut Anda? __ tag_0__ mendekat"
scene 126_walk_date_after_selfie with fade
play sound "shot.mp3"
"..."
"???" "Terima kasih! Terima kasih!"
ms "Lee mengambil waktu sebelum menarik tangannya"
ms "Saya benar -benar harus keluar dari lengannya"
ms "Sejenak saya memiliki perasaan menjijikkan tentang kehilangan kendali ini"
ms "Tapi Lee akhirnya membiarkan saya keluar"
ms "Dan saya bergegas ke pintu keluar"
scene 126_walk_date_after_worried
m "Semoga harimu menyenangkan, Lee."
m "Selamat tinggal."
ms "..."
scene bg public_toilet with fade
show paul suit_sad at left
show mila slutty_serious at right
ms "Paul menungguku di luar."
ms "Saya memandangnya dan semua kekhawatiran saya menghilang begitu saja"
show mila slutty_giggle:
    easein 1 xpos 0.5
ms "Saya menyapanya sambil tersenyum."
m "Anda terlihat seperti germo"
p "..."
show paul suit_smirk
p "Karena Anda terlihat seperti pelacur."
show mila slutty_proud
m "Ahah, terima kasih .__ tag_0__ Saya akan menganggapnya sebagai pujian."
p "Semuanya baik -baik saja?"
show mila slutty_proud_condom
ms "Saya menunjukkannya kondom."
m "Saya merekam video yang menarik untuk Anda."
show paul suit_open_mouth_blush
p "Ya Tuhan ..."
ms "Saya tidak bisa membaca ekspresi di wajahnya"
ms "Tapi sesaat setelah dia tersenyum"
show paul suit_smirk
p "Tidak sabar untuk melihatnya."
show mila slutty_smirk
m "Saya pikir Anda juga ingin melihat ini"
scene 126_walk_date_after_condom_pour
m "..."
scene 126_walk_date_after_condom_close_mouth
m "..."
scene 126_walk_date_after_condom_close_mouth_2
m "..."
play sound "swallow.wav"
m "..."
scene 126_walk_date_after_condom_open_mouth
m "..."
p "..."
p "Sialan ..."
scene 126_walk_date_after_condom_giggle
m "Ahah"
m "Apakah kamu suka itu?"
p "Sialan ya!"
scene 126_walk_date_after_condom_naughty
if _in_replay:
    return



label a127:
"..."
scene 127_mirror_disgust with fade
ms "Astaga ..."
ms "Saya masih memiliki rasa cum di mulut saya meskipun saya telah menyikat gigi dan mencuci wajah saya."
scene 127_mirror_serious with dissolve
ms "Tenggorokan saya terasa sakit."
"..."
scene 127_in_bed_paul_alone with fade
ms "Paul sudah berada di tempat tidur ketika saya kembali."
ms "Dia begitu tenggelam dalam pikirannya sehingga dia tidak memperhatikan saya memasuki kamar tidur."
m "..."
scene 127_in_bed_mila_and_paul with dissolve
ms "Aku merangkak di bawah selimut dan berbaring di sebelahnya tanpa mengucapkan sepatah kata pun."
ms "Setelah semua yang terjadi, saya merasakan campuran perasaan yang aneh."
ms "Ketakutan ...__ tag_0__ bersalah ...__ tag_0__ gairah ..."
ms "Saya sangat fokus pada perasaan saya sendiri sehingga saya lupa tentang perasaan Paul"
scene 127_in_bed_worried with dissolve
m "Kamu tidak apa apa?"
m "..."
p "..."
m "Paul?"
p "?"
ms "Paul meringis."
p "Oh maaf .__ tag_0__ saya tersesat dalam pikiran."
p "Apa pertanyaannya?"
scene 127_in_bed_smile with dissolve
m "Tidak apa-apa"
m "Apakah semuanya baik -baik saja?"
p "..."
scene 127_in_bed_worried with dissolve
m "..."
p "..."
m "Paul?"
scene 127_in_bed_worried_2 with dissolve
p "*mendesah*"
ms "Ketakutan memakan saya .__ tag_0__ seolah -olah itu meraih kepalaku dengan jari es dan menarik rambutku ke belakang."
ms "Saya tertelan."
scene 127_in_bed_worried with dissolve
p "I ...__ tag_0__ Saya tidak bisa memahami perasaan saya."
m "..."
p "Segala sesuatu yang terjadi ... membuat saya benar -benar liar."
p "Tapi saya punya perasaan bahwa kita adalah __tag_0__ terpisah ..."
scene 127_in_bed_hug with dissolve
ms "Saya menekan seluruh tubuh saya ke arahnya."
m "Hanya ada satu cara untuk lebih dekat, tetapi saat ini tidak tersedia bagi kami."
p "..."
scene 127_in_bed_hug_2 with dissolve
p "..."
p "Nah, apakah Anda mengerti apa yang saya maksud?"
m "Tentu."
p "..."
scene 127_in_bed_mila_and_paul with dissolve
m "Kamu tahu..."
m "Kami memiliki bulan ketika kami tidak berhubungan seks ..."
scene 127_in_bed_worried with dissolve
m "Apakah kamu ingat?"
ms "Paul mengangguk."
p "Bukannya aku berhenti mencintaimu ..."
ms "I shook my head."
scene 127_in_bed_mila_and_paul_2 with dissolve
m "Saya tahu .__ tag_0__ saya merasakan hal yang sama ..."
m "Rutin .__ tag_0__ kebiasaan .__ tag_0__ kebosanan."
m "Cinta dan seks sepertinya dipisahkan."
m "Dan seks tidak lagi diperlukan."
scene 127_in_bed_shy with dissolve
m "Saya hanya ...__ tag_0__ terkadang masturbasi ...__ tag_0__ dan itu sudah cukup."
p "..."
m "Tapi sekarang ..."
scene 127_in_bed_naughty with dissolve
m "Hanya tiga hari, Paul, dan aku sudah menjadi gila."
m "Di kepala saya hanya ada seks, seks, dan seks."
m "Saya baru saja keluar dari kamar mandi, tetapi saya sudah bisa merasa vaginaku basah."
ms "Paul membelai punggung saya dan sentuhannya menyebabkan kesemutan yang menyenangkan di seluruh tubuh saya."
m "Yang ingin saya katakan adalah ..."
m "Terkadang pembatasan dan fantasi menambah kegembiraan."
m "Sensasi baru."
p "..."
scene 127_in_bed_smug with dissolve
m "Bagaimana kalau saya melarang Anda berhubungan seks dengan saya sampai sesuatu selesai?"
scene 127_in_bed_smug_frown with dissolve
p "..."
p "Misalnya?"
m "Misalnya, lain kali Anda berhubungan seks hanya akan seperti yang Anda inginkan."
m "Tapi itu pasti sesuatu yang baru."
p "..."
scene 127_in_bed_naughty with dissolve
p "Misalnya, bagaimana jika saya ingin melihat Anda dengan orang lain?"
m "Nah, Anda sudah bisa, saya mengirimi Anda video."
p "..."
p "Lalu, saya ingin bercinta dengan Anda saat Anda meniup orang lain."
scene 127_in_bed_smirk with dissolve
m "Kedengarannya panas."
m "Kesepakatan."
ms "Paul meremas pantatku."
scene 127_in_bed_pleasure with dissolve
m "Aahh ..."
scene 127_in_bed_pout with dissolve
m "Berhentilah menggodaku, aku hampir tidak bisa bertahan."
"..."
scene bg apartments with fade
show mila oversized_shirt_haaa at center:
    xpos 0.6
m "Haaa ..."
show mila oversized_shirt_pout
ms "Oke, __ tag_0__ saya mencoba."
ms "Tapi ini sangat tak tertahankan - tidak peduli apa yang saya lakukan, semua pikiran saya masih meluncur ke arah seks."
ms "Saya melihat jam."
show mila oversized_shirt_shock
m "Baru jam 11 malam?!"
show mila oversized_shirt_haaa
m "Haaa ..."
show mila oversized_shirt_pout
show 127_bobs_sketch at right:
    xzoom 0.6 yzoom 0.6 ypos 0.9 xpos 0.8
bob_message "__tag_0__"
hide 127_bobs_sketch
show mila oversized_shirt_surprised
ma "Wow!"
show mila oversized_shirt_happy
ma "Bob itu sangat bagus! Anda seharusnya tidak mengatakan Anda buruk dalam hal itu"
bob_message "Apakah kamu menyukainya?"
ma "Ya, Anda hebat dalam menggambar!"
bob_message "Terima kasih..."
show mila oversized_shirt_cheeky_grin
ma "Dan bahkan ada sesuatu yang menusuk pantat saya"
bob_message "Maaf..."
ma "Jangan berkeringat"
show mila oversized_shirt_shy_smile
ms "..."
ms "Dia agak terobsesi dengan pantatku"
show mila oversized_shirt_cheeky_grin
ms "Hehe"
bob_message "Saya memposting beberapa pekerjaan saya di Sinterest."
show mila oversized_shirt_shy_open_mouth
ms "Ini tidak seperti seseorang yang bisa mengenali saya dalam gambarnya, kan?"
ms "Itu hanya gambar ..."
show mila oversized_shirt_shy_smile
ms "Tapi agak panas membayangkan beberapa orang anonim menyentak pantatku ..."
bob_message "Dan menerima banyak komentar positif"
ma "Saya senang"
bob_message "Rasanya ... tidak diterima"
bob_message "Saya pikir ini lebih seperti pencapaian Anda, lalu saya ..."
show mila oversized_shirt_haaa
ms "Haaa ..."
ms "Demi bercinta, Bob ..."
show mila oversized_shirt_pout
ms "Saya harus mendukungnya entah bagaimana ..."
show mila oversized_shirt_cheeky_grin
ms "\"Inspire\", ya?"
ms "Seperti Lee?"
show mila oversized_shirt_shy_smile
ms "..."
ms "Saya masih memiliki pakaian sekolah ..."
show mila oversized_shirt_cheeky_grin
m "Hah."
play sound "shot.mp3"
scene 127_spread_selfie with flash
ma "Inilah beberapa inspirasi untuk Anda"
ma "__tag_0__"
scene bg bedroom with fade
bob_message "Oh wow ..."
bob_message "Pantat yang luar biasa ..."
show mila schoolgirl_cheeky_grin at center:
    xpos 0.6
ms "..."
ma "Ingin memberikannya yang baik?"
bob_message "Saya ingin memukulnya"
show mila schoolgirl_shy
ms "..."
ms "Gairah kami membuat kami lebih kasar dengan kata -kata"
show mila schoolgirl_slight_smile
ms "Tapi saya akan berbohong jika saya mengatakan bahwa saya tidak menyukainya"
show mila schoolgirl_masturbating
ms "Saya meletakkan tangan saya di bawah rok saya dan memeras klitoris saya"
show mila schoolgirl_pain_pinch
m "Aduh..."
ms "Rasa sakit sedikit membersihkan pikiran, tetapi kemudian meninggalkan gema yang menyenangkan"
show mila schoolgirl_shy
m "Sial, aku ingin bercinta ..."
ms "Saya merasa seperti anak sekolah dengan spermotoksikosis"
show mila schoolgirl_slight_smile
ms "Semua pikiran saya adalah tentang seks ..."
m "Oke, mari kita tonton video Bob ..."
scene 127_porn_1 with fade
ms "..."
m "Bob, it's time for the next chapter of \"Mila is watching your favorite porn\"."
ms "..."
m "Saya tidak dapat membantu tetapi memperhatikan bahwa semua gadis di video Anda cukup mungil"
m "Omong -omong, pakaian keren"
ms "..."
scene 127_porn_2 with dissolve
m "Biarkan saya menebak"
m "Itu akan anal lagi?"
m "Saya tidak bisa menyangkalnya - itu pasti terlihat indah."
m "Tapi apa kesenangannya?"
scene 127_porn_3 with dissolve
ms "..."
m "Oh wow"
m "Itu plug anal yang sangat besar!"
scene 127_porn_4 with dissolve
m "..."
m "Terlihat sangat bejat saat pantat Anda diregangkan seperti itu ..."
m "Dia bahkan mencoba tersenyum, jiwa yang malang ..."
scene 127_porn_5 with dissolve
ms "..."
ms "Untuk sepersekian detik saya membayangkan diri saya di tempat gadis itu"
ms "Kata -kata Paul tidak bisa lepas dari pikirannya."
m "Saya ingin bercinta seperti itu ..."
scene 127_porn_6 with dissolve
show mila schoolgirl_surprised at center:
    xpos 0.6
m "!"
ms "Apakah saya mengatakan itu dengan keras?"
show mila schoolgirl_shy
m "..."
show mila schoolgirl_slight_smile
ms "Jadi apa?"
ms "Bob sudah tahu bahwa saya seorang pelacur"
ms "..."
show mila schoolgirl_cheeky_grin
ms "Hehe"
scene 127_porn_7 with dissolve
m "Asap Suci ..."
m "..."
m "Apakah Anda bercanda?"
m "Oh gadis malang ..."
m "Saya bahkan tidak bisa membayangkan bagaimana rasanya begitu penuh"
ms "Terlepas dari kenyataan bahwa apa yang terjadi di layar itu brutal dan kasar"
ms "Saya menurunkan tangan saya dan mulai membelai diri"
m "*shlick shlick shlick*"
ms "Seiring dengan kegembiraan yang semakin besar, saya menonton gadis itu di video"
scene 127_porn_8 with dissolve
ms "Ekspresinya berubah ..."
ms "Dan kemudian dia menggali kukunya ke bagian belakang salah satu pria dan berteriak"
ms "Otot -otot kakinya menegang, dia menahan napas, lalu kejang."
ms "Saya menghentikan video dan mengirim komentar saya kepada Bob."
scene bg bedroom with fade
show mila schoolgirl_surprised at center:
    xpos 0.6
m "Wow..."
show mila schoolgirl_biting_lips
ms "Saya belum pernah melihat orgasme yang kuat seperti itu"
ms "Saya tidak bisa mengeluarkan adegan orgasme ini dari kepala saya."
m "Apakah itu palsu? __ tag_0__ atau benar -benar mungkin untuk mengalami orgasme dari pantat sialan, saya bertanya -tanya?"
m "..."
show cg 127_anus_rub with moveintop
ms "Saya sendiri tidak memperhatikan bagaimana jari -jari saya sudah mulai membelai cincin anus."
hide cg with moveoutbottom
show mila schoolgirl_slight_smile
m "Heh"
m "Jika dia sangat terobsesi dengan keledai ..."
m "Saya perlu mengambil foto lain untuk Bob."
play sound "shot.mp3"
scene 127_fingering_selfie with flash
ms "..."
show mila schoolgirl_shy at center:
    xpos 0.6
ma "__tag_0__"
ma "Saya tidak tahu tentang 14cm, sulit untuk memasukkan satu jari."
bob_message "Oh wow, Mila!"
bob_message "Suka sekali!"
bob_message "Itu gambar yang luar biasa!"
bob_message "Aku sangat terangsang sekarang, oh fuck ..."
scene bg bedroom with fade
show mila schoolgirl_biting_lips at center:
    xpos 0.6
ms "Dia sangat bersemangat atas gambar ini ..."
ms "Itu agak lucu ..."
bob_message "Apakah itu menyakitkan?"
show mila schoolgirl_slight_smile
ma "Tidak terlalu"
ma "Lebih seperti ... tidak menyenangkan?"
show mila schoolgirl_pout
ma "Sejujurnya, saya tidak mengerti, itu hanya tidak nyaman ..."
ma "Saya pikir orgasme anal yang Anda lihat dalam pornografi adalah mitos."
ms "Bob tidak menjawab sebentar"
bob_message "Anda benar dan salah pada saat bersamaan ..."
bob_message "Tidak ada orgasme lain selain yang klitoris."
bob_message "Setidaknya itulah yang dikatakan dokter."
bob_message "Namun seks anal bisa sangat menyenangkan"
bob_message "Karena itu merangsang vagina Anda dari sudut yang sangat tidak biasa"
show mila schoolgirl_slight_smile
ms "Kami memiliki ahli anal di sini ..."
show mila schoolgirl_cheeky_grin
ms "Haruskah saya memanggil Anda anal sensei mulai sekarang?"
ma "Entah bagaimana saya meragukannya"
bob_message "Ingin bertaruh?"
show mila schoolgirl_shy
ms "..."
ms "Saya hampir setuju."
ma "Saya takut membayangkan bagaimana tepatnya Anda akan membuktikannya ...__ tag_0__"
bob_message "Saya mungkin tidak terlihat seperti itu, tetapi semua gadis yang pernah saya katakan bahwa saya sangat pandai anilingus"
show mila schoolgirl_embarassed
bob_message "Saya ingin memperkenalkan Anda ke lidah saya alih -alih jari -jari Anda dan menjilat Anda dari kepala hingga ujung kaki suatu hari nanti"
bob_message "Ini adalah foto yang bagus, Mila, terima kasih."
ma "__tag_0__"
ms "..."


label hscene_2nd_drawing_session:
scene evening with fade
pause 1
scene bg apartments with dissolve
bob_message "Saya di rumah."
show mila schoolgirl_shy at center:
    xpos 0.6
ms "Aku tahu"
ms "Saya mendengar Anda masuk"
ma "Saya datang"
ms "..."
show mila schoolgirl_slight_smile
ms "Saya pikir saya telah memperoleh semacam kekuatan super."
ms "Sebelumnya, saya tidak memperhatikan apa yang terjadi di luar apartemen."
ms "Dan sekarang saya mendengar Bob bersiap -siap untuk bekerja dan kembali ke rumah."
ms "..."
ms "Saya melihat diri saya sendiri."
show mila schoolgirl_biting_lips
m "Saya mungkin akan pergi seperti ini ..."
m "Pada saat yang sama, saya bisa mengembalikan pakaian ini."
show mila schoolgirl_thinking
ms "..."
m "Mungkin saya harus mencucinya terlebih dahulu?"
m "Meskipun..."
show mila schoolgirl_slight_smile
m "Saya pikir dia akan lebih menyukainya jika saya tidak melakukannya"
ms "..."
ms "Sudah ada di pintu, mataku terikat pada ketinggian"
show mila schoolgirl_thinking
ms "Akhir -akhir ini saya merasa cukup percaya diri pada mereka."
m "Bob mungkin tidak keberatan jika saya memakainya, kan?"
bob_message "Apakah Anda akan segera hadir?"
show mila schoolgirl_haaaa
ms "Ya, ya, saya datang"
show mila schoolgirl_biting_lips
ms "Bob is so persistent...{w}{image=emoji/heart.png}"
ms "Saya perlu bergegas"
play sound "door-open-close.mp3"
scene bg doors with fade
show mila schoolgirl_oops at center:
    xpos 0.6
ms "..."
ms "Ups"
ms "Saya lupa kunci saya."
ms "..."
play sound "knock.mp3"
scene 127_drawing_event_1 with fade
m "H-hello"
bob "..."
scene 127_drawing_event_2 with dissolve
m "Saya lupa kunci saya."
bob "..."
m "..."
scene 127_drawing_event_3 with dissolve
m "Erm ..."
m "Bisakah saya masuk?"
bob "Oh ya, maaf."
bob "Saya mendapat sedikit starstruck"
scene 127_drawing_event_4 with dissolve
m "Ahah"
m "Saya memutuskan untuk mengembalikan pakaian Anda juga, jadi saya datang ke dalamnya."
bob "..."
m "Nah, saya masuk!"
"..."
scene 127_drawing_event_5 with fade
bob "Apa yang sedang kamu lakukan?"
scene 127_drawing_event_6 with dissolve
m "HM?"
scene 127_drawing_event_7 with dissolve
m "Membuka pakaian?"
bob "..."
scene 127_drawing_event_8 with dissolve
m "Ngomong -ngomong, saya sangat menyukai gambar Anda."
scene 127_drawing_event_9 with dissolve
m "Saya tidak tahu mengapa Anda menjatuhkan diri Anda begitu banyak"
scene 127_drawing_event_10 with dissolve
m "Haruskah saya melepas stoking?"
m "..."
scene 127_drawing_event_11 with dissolve
m "Bob?"
bob "..."
scene 127_drawing_event_12 with dissolve
m "Heeeeey"
bob "Maaf ...__ tag_0__ Saya tidak berharap Anda melepas pakaian Anda ..."
scene 127_drawing_event_13 with dissolve
m "Oh..."
scene 127_drawing_event_12 with dissolve
m "Haruskah saya berpakaian?"
bob "Tidak, tidak! __ tag_0__ semuanya baik -baik saja"
scene 127_drawing_event_14 with dissolve
m "..."
scene 127_drawing_event_11 with dissolve
m "Jadi apa yang harus saya lakukan?"
bob "Aku tidak tahu..."
bob "Bisakah Anda menunjukkan pose senam keren?"
scene 127_drawing_event_15 with dissolve
m "Hmmm ..."
ms "Bagus karena saya baru -baru ini meregangkan."
scene 127_drawing_event_12 with dissolve
m "Saya tidak ingin jatuh, jadi saya akan lepas landas, oke?"
scene 127_drawing_event_16 with fade
m "Biarkan saya mencoba ..."
scene 127_drawing_event_17 with dissolve
m "..."
bob "Sial ..."
scene 127_drawing_event_18 with dissolve
m "Keren, ya?"
bob "Bisakah saya mengambil foto?"
m "Tolong lakukan, sebenarnya saya sudah berada di batas saya"
play sound "shot.mp3"
ms "Saya dirasuki oleh kegembiraan yang aneh"
ms "Kekaguman dan tatapan Bob membuatku ingin pamer."
ms "Akhir -akhir ini saya tidak memiliki banyak kesempatan untuk menunjukkan apa yang mampu dilakukan tubuh saya."
scene 127_drawing_event_19 with fade
m "..."
bob "Sial!"
play sound ["shot.mp3", "shot.mp3", "shot.mp3", "shot.mp3"]
"..."
ms "Berapa banyak foto yang akan dia ambil?"
scene 127_drawing_event_20 with fade
ms "Tiba -tiba menjadi panas di kamar"
ms "Semua latihan ini membuatku berkeringat"
m "..."
m "Bagaimana Anda menyukai peregangan saya?"
bob "Sial, saya tidak berpikir beberapa pose itu bahkan mungkin"
scene 127_drawing_event_21 with dissolve
m "Tubuh manusia luar biasa, jika Anda memiliki keinginan, apa pun bisa diregangkan"
m "..."
scene 127_drawing_event_22 with dissolve
ms "Arti kedua dari frasa terakhir yang saya sadari"
ms "Pantat saya terkepal dalam rasa takut untuk mengantisipasi kemungkinan peregangan"
scene 127_drawing_event_23 with dissolve
m "Hmm..."
scene 127_drawing_event_20 with dissolve
m "Apa selanjutnya? __ tag_0__ Saya agak bosan dengan pose berat"
m "Mari kita lakukan sesuatu yang kurang ekstrem"
ms "Bob menjadi merah, terengah -engah."
scene 127_drawing_event_22 with dissolve
ms "Saya jelas melihat tonjolan di celananya"
ms "Tapi kegembiraan saya dan kencan terakhir saya dengan Paul memberi saya kekuatan dan keberanian"
ms "Bob melahapku dengan matanya"
ms "Dan mengetahui preferensi -Nya, saya ingin lebih menggodanya."
scene 127_drawing_event_24 with dissolve
m "Saya yakin Anda ingin melihat pantat saya, kan?"
bob "Bob menelan"
m "Ini dia"
scene 127_drawing_event_25 with fade
m "..."
m "Apakah Anda suka pantat saya?"
bob "..."
m "Bob ... jangan diam"
play sound "shot.mp3"
scene 127_drawing_event_26 with dissolve
m "Saya bisa tetap dalam posisi ini untuk waktu yang lama, Anda bisa mulai menggambar."
bob "Saya ... hmm"
ms "Suara Bob terdengar serak dan dia berdeham."
bob "Saya takut melewatkan beberapa detail ..."
m "Oh! __ tag_0__ detail sangat penting!"
scene 127_drawing_event_26a with dissolve
ms "Gairah mendadak pikiran saya"
m "You can spread my ass to see \"the details\"lebih baik, jika anda mau"
ms "Bob Tangus"
ms "Dia mendekati saya"
ms "Ya ampun, dia sangat besar ..."
ms "Celananya meledak dari dalam"
scene 127_drawing_event_27 with dissolve
ms "Bob dengan lembut meletakkan tangannya di pipi pantatku"
ms "Aku merasakan jarinya hampir menyentuh vaginaku"
ms "Saya hampir tidak berhasil menahan erangan"
bob "Kamu sangat seksi, mila ..."
scene 127_drawing_event_28 with dissolve
ms "Saya sangat terangsang sekarang ...__ tag_0__ jika dia menurunkan celananya dan memasukkannya ke dalam ..."
ms "Ayam gemuknya yang besar akan merobek vaginaku ..."
ms "Aku hanya perlu mendorongnya sedikit lagi ..."
ms "Ayo ...__ tag_0__ sebarkan pipiku ..."
scene 127_drawing_event_29 with dissolve
m "Jadi Anda bisa melihat detailnya dengan lebih baik?"
ms "Suaraku pecah"
ms "Bob menatap vagina dan pantatku, terengah -engah"
ms "Vagina saya bocor, dan Bob bisa merasakan basah saya dengan jari -jarinya"
scene 127_drawing_event_30 with dissolve
ms "Aku seperti wanita jalang panas ..."
ms "Ayo Bob, Persetan denganku"
bob "Mila ...__ tag_0__ Saya pikir kita harus berhenti ..."
bob "Saya nyaris tidak memegang ..."
ms "Dia melepaskan tangannya dari saya dan bersandar"
scene 127_drawing_event_31 with dissolve
ms "..."
ms "Kata -katanya membawa saya ke akal sehat"
ms "Apa yang terjadi dengan saya?"
ms "Saya hampir tidak bisa mengendalikan diri sekarang ..."
scene 127_drawing_event_32 with fade
ms "Saya masih terangsang sekali"
ms "Dan malu"
ms "Itu sebabnya saya meraih bantal untuk memeluk .__ tag_0__ sebagai perisai ..."
scene 127_drawing_event_33 with dissolve
m "Hmm ...__ tag_0__ besok adalah hari terakhir, kan?"
bob "...__ tag_0__ ya"
ms "Sial, aku ingin melihat betapa dia akan cum ..."
scene 127_drawing_event_34 with dissolve
m "Erm ... jika Anda mau, saya bisa datang lagi dan Anda bisa menyentak di tubuh telanjang saya"
ms "Kedengarannya sangat cabul ..."
bob "..."
ms "Bob diam"
scene 127_drawing_event_35 with dissolve
m "Anda tidak suka idenya?"
ms "Saya merasa terhina"
bob "Saya pikir ...__ tag_0__ saya mendapat promosi"
scene 127_drawing_event_36 with dissolve
m "Anda sudah melakukannya? __ tag_0__?!"
ms "Saya pikir itu akan memakan waktu lebih lama ..."
bob "Saya pergi ke wawancara dengan pesaing kami ..."
bob "Mereka membayar lebih di sana .__ tag_0__ tidak lebih, tapi tetap saja"
bob "Entah bagaimana saya takut memposting resume saya sebelumnya ..."
bob "Saya berpikir bahwa jika bos mengetahuinya, kami akan melakukan percakapan yang tidak menyenangkan ..."
bob "Tapi jujur saja, saya tidak peduli lagi ..."
bob "Terima kasih, kurasa ..."
scene 127_drawing_event_33 with dissolve
ms "Saya perhatikan bahwa Bob sekarang berbicara dengan cara yang berbeda"
ms "Suaranya berubah .__ tag_0__ Dia berbicara dalam kalimat yang lebih pendek dan lebih percaya diri ..."
ms "Pussy saya mengepal untuk mengantisipasi."
ms "Dia mendapat promosi ..."
scene 127_drawing_event_37 with dissolve
ms "Yang berarti ...__ tag_0__ besok"
bob "Secara umum, saya menulis pernyataan, tetapi secara resmi akan mulai berlaku dalam beberapa minggu."
bob "Benar, saya dipanggil untuk berbicara dengan HR"
bob "Saya harus tahan dengan obrolan mereka sebentar."
bob "..."
bob "Apakah ini dihitung?"
scene 127_drawing_event_32 with dissolve
m "Hmmm ..."
scene 127_drawing_event_33 with dissolve
m "Bagaimana menurutmu?"
ms "Bob meremehkan"
bob "*Mendesah*"
bob "Yah, tentu saja tidak ..."
m "..."
scene 127_drawing_event_36 with dissolve
m "Mengapa tidak?"
m "Saya pikir itu penting"
ms "Bob menatapku dengan terkejut."
bob "Apa?"
scene 127_drawing_event_37 with dissolve
m "Cukup untuk membawa perjanjian sewa yang ditandatangani sebagai bukti."
m "Atau beberapa makalah lain"
m "Atau gaji bonus"
m "Atau Anda tidak bisa tidak membawa apa -apa."
m "Hanya kata -kata Anda sudah cukup untuk saya."
bob "Saya bisa berbohong, Anda tahu."
scene 127_drawing_event_38 with dissolve
m "Anda yakin bisa"
m "Tapi aku percaya padamu."
m "Aku percaya padamu, Bob."
ms "Dia tersenyum."
ms "Ekspresi aneh merayap ke wajahnya - campuran rasa malu dan kebingungan."
bob "Um ...__ tag_0__ itu artinya, __ tag_0__ besok ..."
scene 127_drawing_event_37 with dissolve
m "Ya."
m "Besok aku milikmu."
bob "..."
m "Selamat malam Bob"
bob "..."
if _in_replay:
    return


scene bg bedroom with fade
"..."
ms "Ketika Paul kembali ke rumah, saya mengatakan kepadanya bahwa Bob telah memenuhi kondisi ketiga."
show mila slutty_serious at center:
    xpos 0.6
m "..."
show paul suit_blush_looking_aside at left
p "Jadi, cerita panjang, besok kalian berdua akan berhubungan seks"
show mila slutty_idle
m "...__ tag_0__ ya ..."
show paul suit_sad
p "Hmm..."
show mila slutty_concerned
m "Paul, saya tidak yakin saya bisa berhenti setelah ini ..."
m "Hari ini saya kesulitan mengendalikan diri"
m "Sepertinya saya dirasuki oleh entitas penuh nafsu"
show mila slutty_serious
m "Jika saya terus memanjakannya ...__ tag_0__it dapat mengkonsumsi saya"
m "Saya tidak yakin saya akan pernah bisa menyingkirkannya di masa depan ..."
show paul suit_smirk
ms "Paul menatapku dengan serius"
p "Dan saya tidak ingin Anda berhenti"
m "..."
show mila slutty_suspicious
m "Akankah ...__ tag_0__ akankah cintamu tetap sama setelahnya?"
show paul suit_sad
p "..."
p "TIDAK."
show mila slutty_tearing_up
m "..."
show paul suit_grin
p "Aku akan lebih mencintaimu"
show mila slutty_tearing_up_smile
m "Aku pun mencintaimu."
show paul suit_smirk
p "..."
m "Paul ..."
m "Apakah Anda ingin memiliki anak?"
show paul suit_shock
p "Wow, melompat ke topik lain ..."
show mila slutty_tearing_up_grin
m "Tiba -tiba saya ingin hamil"
show paul suit_open_mouth_neutral
p "Hah"
p "Belum."
p "Saya memikirkannya .__ tag_0__ sebelumnya"
show paul suit_blush_looking_aside
p "Dan sekarang ... Saya ingin sesuatu yang sedikit berbeda ..."
show paul suit_grin
p "Plus ...__ tag_0__ saya punya beberapa ide ..."
show mila slutty_frown
m "Ide? __ tag_0__ ide apa?"
show paul suit_smirk
p "Aku akan memberitahumu nanti."
m "Anda tahu bahwa saya membencinya saat Anda melakukannya"
p "Tapi saya masih belum ingin tahu apa -apa."
show paul suit_grin
p "Yang bisa saya katakan adalah bahwa saya yakin Anda akan menyukai idenya."
show mila slutty_suspicious
m "Oke, kurasa ..."
p "Ngomong -ngomong, saya menonton video kemarin"
show mila slutty_idle
m "Anda melakukannya? __ tag_0__ dan bagaimana ...__ tag_0__ bagaimana?"
show paul suit_smirk
p "Sangat indah."
show mila slutty_giggle
p "Anda adalah pelacur sejati"
p "Porno terbaik dalam hidupku"
show mila slutty_idle
m "Lagi nga?"
show paul suit_blush_looking_aside
p "..."
p "Ya"
scene 127_mila_morning with fade
ms "Saya tidak tidur nyenyak lagi."
ms "Kali ini saya mengejar monster dengan penis besar"
ms "Saya menangkap mereka dan menidurinya. Dan saya masih tidak bisa cum"
scene bg bedroom with fade
show mila slutty_concerned at center:
    xpos 0.6
ms "Saya melirik jam"
play sound "ticking.mp3"
"*tic*__ tag_0 __*tok*__ tag_0 __*tic*__ tag_0 __*tok*"
show mila slutty_haaaa
m "Haaaa"
show mila slutty_frown
ms "Saya seharusnya tidak melihat jam, membuat waktu lebih lambat ..."
m "Kenapa aku melakukan ini setiap ..."
show mila slutty_serious
ms "Saya melihat jam"
m "Dua menit"
m "..."
show mila slutty_haaaa
m "Fuck."
m "Saya melihat lagi."
show mila slutty_idle
m "..."
ma "Bagaimana kabarmu?"
bob_message "Sibuk"
show mila slutty_haaaa
m "Haaaa ..."
show mila slutty_frown
m "Aku benci menunggu"
m "..."
show mila slutty_idle
m "Aku akan menyegarkan diri di kamar mandi"
"..."
scene 127_b-day_shower with fade
play sound "shower.mp3"
ms "Aliran air panas membawa saya kembali ke akal sehat saya"
ms "Selama beberapa menit saya hanya berdiri dan menikmati sensasi"
ms "Saya takut untuk membayangkan apa negara bagian Bob ..."
jump a127_bday_branch

label after_the_bday:
    scene bg doors with fade
    play sound "door-open-close.mp3"
    ms "..."
    show mila nude_new_shy at right
    ms "Saya sangat lelah sehingga saya bahkan tidak berpikir untuk mulai mengkhawatirkan ketika saya meninggalkan apartemen telanjang."
    ms "Pada akhirnya, ini jam tiga pagi dan tidak akan ada orang di sana."
    ms "Udara malam yang sejuk terasa mendidih."
    scene bg door with fade
    play sound "door-open-close.mp3"
    show mila nude_new_shy at right
    ms "Bagi saya sepertinya saya semua terbakar."
    ms "Kepalaku berputar dari kelelahan."
    scene 127_b-day_shower with fade
    play sound "shower.mp3"
    ms "Dengan kekuatan terakhir saya, saya pergi ke kamar mandi dan dibilas."
    scene bg apartments with fade
    ms "Ketika saya selesai dan meninggalkan kamar mandi yang saya lihat, bahwa Paul menunggu saya di ruang tamu"
    show mila robe_excited_and_shy at right
    ms "Penampilannya yang bersemangat dan khawatir membuat saya tersenyum"
    m "Saya di rumah ..."
    ms "Saya benar -benar ingin tidur .__ tag_0__ ruangan bergoyang di depan mata saya."
    p "Apa kabarmu?"
    m "SAYA..."
    m "Saya pikir saya sedikit overdid."
    scene 129_faint with hpunch
    play sound "body-fall.mp3"
    ms "Ruangan itu berbalik di sampingnya dan menjadi gelap."
    p "Sayang! Sayang!"
    ms "Saya mendengar suara Paul dari jauh dan jatuh ke dalam kebahagiaan manis."
    ms "Tidur ...__ tag_0__ Aku sangat ingin tidur ..."

label after_faint:
jump not_yet

label not_yet:
scene under_constr
play music anthem
"Maaf, ini adalah akhir dari jalur ini untuk versi ini :("
"Tapi saya bekerja keras untuk membuat lebih banyak :)"
"Lihat __tag_0__my Star Star Page__tag_1__ untuk mengetahui berita terbaru"
jump end


label end:
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
