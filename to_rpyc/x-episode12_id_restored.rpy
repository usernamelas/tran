image ep12_015 = Movie(play="video/episode12/015.webm", image="images/episode12/015.webp", loop = False)
image ep12_059 = Movie(play="video/episode12/059.webm", image="images/episode12/059.webp", loop = False)
image ep12_064 = Movie(play="video/episode12/064.webm", loop = True)
image ep12_065 = Movie(play="video/episode12/065.webm", loop = True)
image ep12_066 = Movie(play="video/episode12/066.webm", loop = True)
image ep12_069 = Movie(play="video/episode12/069.webm", loop = True)
image ep12_070 = Movie(play="video/episode12/070.webm", loop = True)
image ep12_071 = Movie(play="video/episode12/071.webm", loop = True)
image ep12_072 = Movie(play="video/episode12/072.webm", loop = True)
image ep12_073 = Movie(play="video/episode12/073.webm", loop = True)
image ep12_074 = Movie(play="video/episode12/074.webm", loop = True)
image ep12_092 = Movie(play="video/episode12/092.webm", image="images/episode12/092.webp", loop = False)
image ep12_107 = Movie(play="video/episode12/107.webm", image="images/episode12/107.webp", loop = False)
image ep12_139 = Movie(play="video/episode12/139.webm", loop = True)
image ep12_140 = Movie(play="video/episode12/140.webm", loop = True)
image ep12_141 = Movie(play="video/episode12/141.webm", loop = True)
image ep12_142 = Movie(play="video/episode12/142.webm", loop = True)
image ep12_143 = Movie(play="video/episode12/143.webm", loop = True)
image ep12_144 = Movie(play="video/episode12/144.webm", loop = True)
image ep12_148 = Movie(play="video/episode12/148.webm", loop = True)
image ep12_149 = Movie(play="video/episode12/149.webm", loop = True)
image ep12_150 = Movie(play="video/episode12/150.webm", loop = True)
image ep12_151 = Movie(play="video/episode12/151.webm", loop = True)
image ep12_152 = Movie(play="video/episode12/152.webm", loop = True)
image ep12_153 = Movie(play="video/episode12/153.webm", loop = True)
image ep12_168 = Movie(play="video/episode12/168.webm", image="images/episode12/168.webp", loop = False)
image ep12_179 = Movie(play="video/episode12/179.webm", loop = True)
image ep12_310 = Movie(play="video/episode12/310.webm", image="images/episode12/310.webp", loop = False)
image ep12_373 = Movie(play="video/episode12/373.webm", loop = True)
image ep12_374 = Movie(play="video/episode12/374.webm", loop = True)
image ep12_375 = Movie(play="video/episode12/375.webm", loop = True)
image ep12_376 = Movie(play="video/episode12/376.webm", loop = True)
image ep12_377 = Movie(play="video/episode12/377.webm", loop = True)

label episode12:
    $ progress = 154
    stop music fadeout 10.0
    scene expression ("images/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(2, 6) with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_newEpisode

    show screen ui_message("Sunday") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message


    if emma_break == True:
        $ emma_path = False

    if lisa_path or lauren_path:
        call episode12_girlsDate from _call_episode12_girlsDate
    else:
        call episode12_alone from _call_episode12_alone

    call episode12_trisCharlotte_yard from _call_episode12_trisCharlotte_yard

    if charlotte_path:
        call episode12_massage_charlotte from _call_episode12_massage_charlotte

    if patricia_path:
        call episode12_patricia_shower from _call_episode12_patricia_shower

        call episode12_patricia_date from _call_episode12_patricia_date

    return

label episode12_girlsDate:

    $ ep12_girlsDate = True
    scene expression ("images/episode12/001.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* reading *{/color}{/size}\n{i}\"Eye contact is important. On a first date you are trying to read each other and human beings are notoriously bad at reading facial expressions of strangers.\"{/i}"
    toby "{size=12}{color=#FDCA6E}* reading *{/color}{/size}\n{i}\"Shifty eye contact or too much eye contact can make it difficult for people to trust you and figuring out the middle ground is helpful in both dating and business.\"{/i}"

    if lisa_path:
        if lauren_sidePath:
            call episode12_lauren_side from _call_episode12_lauren_side
        else:
            call episode12_lisa_main from _call_episode12_lisa_main
    else:
        if lisa_sidePath:
            call episode12_lisa_side from _call_episode12_lisa_side
        else:
            call episode12_lauren_main from _call_episode12_lauren_main

    call episode12_backFromDate from _call_episode12_backFromDate

    return

label episode12_lisa_main:
    scene expression ("images/episode12/002.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Speaking of dates. Yesterday I promised Lisa we'd go out today.{/i}"
    if patricia_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit! I also promised Tris we'd go out tonight. That means I'll have to go out with Lisa in the morning so I can leave my evening free for Tris.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I kinda want to go out with her right now. I really want to see her.{/i}"
    scene expression ("images/episode12/004_texting.webp") with dissolve
    call sms_sent ("lisa", "Good morning, beautiful!") from _call_sms_sent_166
    call sms_incoming ("lisa", "Now this is what I call waking up nicely.") from _call_sms_incoming_216
    call sms_sent ("lisa", "I think I can think of of a few better ways of waking up than this.") from _call_sms_sent_167
    call sms_incoming ("lisa", "Surprise me!") from _call_sms_incoming_217
    call sms_sent ("lisa", "Waking you up with a kiss and breakfast in bed.") from _call_sms_sent_168
    call sms_incoming ("lisa", "Stop it, or I'm going to ask you to marry me.") from _call_sms_incoming_218
    call sms_sent ("lisa", "On one knee and all that?") from _call_sms_sent_169
    call sms_incoming ("lisa", "And a big shiny ring.") from _call_sms_incoming_219
    call sms_sent ("lisa", "Stop it, or I might say yes.") from _call_sms_sent_170
    call sms_incoming ("lisa", "You're an idiot! I love it!") from _call_sms_incoming_220
    call sms_sent ("lisa", "Speaking of breakfast? Wanna go out get some?") from _call_sms_sent_171
    call sms_incoming ("lisa", "Ooooh... A morning date? We've never had one of those.") from _call_sms_incoming_221
    call sms_sent ("lisa", "So that's a yes?") from _call_sms_sent_172
    call sms_incoming ("lisa", "That's a \"Hell yeah\".") from _call_sms_incoming_222
    call sms_sent ("lisa", "Cool. Pick you up in 30 minutes?") from _call_sms_sent_173
    call sms_incoming ("lisa", "Car or bike?") from _call_sms_incoming_223
    call sms_sent ("lisa", "Bike.") from _call_sms_sent_174
    call sms_incoming ("lisa", "Helmets?") from _call_sms_incoming_224
    call sms_sent ("lisa", "Nope!") from _call_sms_sent_175
    call sms_incoming ("lisa", "Then not going to happen. I'll come pick you up. I get it, you're cool, no helmet and stuff, but I'm planning on living to see 101 years old.") from _call_sms_incoming_225
    call sms_sent ("lisa", "101? Why not 100.") from _call_sms_sent_176
    call sms_incoming ("lisa", "Because Lauren plans on living to 100 and I want to live at least one more year without her to see what I've missed out on because she told me that when I get married I have to adopt her.") from _call_sms_incoming_226
    call sms_sent ("lisa", "Cool. Here's the address then.", img_icon="images/episode12/005_icon.webp") from _call_sms_sent_177
    call sms_incoming ("lisa", "Perfect. I'll pick you up in 20 minutes.") from _call_sms_incoming_227
    call sms_sent ("lisa", "That hungry?") from _call_sms_sent_178
    call sms_incoming ("lisa", "Or maybe I just wanna spend some time with you.") from _call_sms_incoming_228
    call sms_sent ("lisa", "Maybe?") from _call_sms_sent_179
    call sms_incoming ("lisa", "Maybe.") from _call_sms_incoming_229
    call sms_sent ("lisa", "And here I was thinking that since you're not going to wear any panties it'll take you less time to get ready.") from _call_sms_sent_180
    call sms_incoming ("lisa", "Too late. I'm already wearing them.", img_icon="images/episode12/006_icon.webp", img="images/episode12/006.webp") from _call_sms_incoming_230
    call sms_sent ("lisa", "I remember you saying something different yesterday.") from _call_sms_sent_181
    call sms_incoming ("lisa", "I have no recollection of that.") from _call_sms_incoming_231
    call sms_sent ("lisa", "You're bad!") from _call_sms_sent_182
    call sms_incoming ("lisa", "Talk to you later. I have a date with a sexy guy in 20 minutes and I need to get ready.") from _call_sms_incoming_232
    call sms_sent ("lisa", "Cool. Let me know how that goes.") from _call_sms_sent_183
    call sms_incoming ("lisa", "I sure will.") from _call_sms_incoming_233
    hide screen message
    scene expression ("images/episode12/007.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Guess I'd better get ready too.{/i}"

    call episode12_morningCharlotte from _call_episode12_morningCharlotte
    $ progress = 155

    scene expression ("images/episode12/012.webp") with fade
    toby "Pagi, cantik!"

    scene expression ("images/episode12/013.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    lisa "Pagi, tampan!"
    scene expression ("images/episode12/014.webp") with dissolve
    toby "Ya Tuhan, kamu cantik."
    lisa "Anda hanya mengatakan itu agar Anda bisa mencium saya."
    show ep12_015
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/015.webp") with dissolve
    hide ep12_015
    toby "Saya mengatakan itu karena saya benar -benar berpikir Anda cantik, tetapi ciuman itu sebenarnya ide yang bagus."
    scene expression ("images/episode12/016.webp") with dissolve
    toby "Jadi, apakah Anda ingin pergi ke kedai kopi itu? Saya mendengar bahwa mereka memiliki sarapan yang sangat enak."
    scene expression ("images/episode12/017.webp") with dissolve
    lisa "Terima kasih! Saya tidak tahu Anda adalah pria yang begitu baik."
    toby "Ya, Anda selamat datang, tapi saya pikir Anda berada di kursi saya."
    lisa "Tidak. Aku benci mengemudi, dan seperti keberuntungan, aku punyamu untuk mengantarku hari ini."
    toby "Apakah Anda yakin Anda mempercayai saya mengendarai mobil Anda?"
    lisa "Jujur saja, saya bukan pengemudi terbaik. Saya pikir Anda dapat melakukan pekerjaan yang jauh lebih baik daripada saya."
    scene expression ("images/episode12/018.webp") with dissolve
    toby "Jadi? Coffeeshop?"
    lisa "Kedengarannya bagus!"

    scene expression ("images/episode12/019.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode12/020.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode12/021.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode12/022.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode12/023.webp") with dissolve:
        xalign 0.5
        yalign 0.5
        zoom 0.8
        linear 20.0 zoom 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode12/024.webp") with fade
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/025.webp") with dissolve
    barista "Selamat pagi. Apa yang bisa saya dapatkan dari Anda?"
    scene expression ("images/episode12/026.webp") with dissolve
    toby "Pancake Special dan cappuccino."
    scene expression ("images/episode12/027.webp") with dissolve
    toby "Dan untukmu?"
    scene expression ("images/episode12/028.webp") with dissolve
    lisa "Hal yang sama, tetapi dengan latte bukan cappuccino."
    scene expression ("images/episode12/025.webp") with dissolve
    barista "Sempurna. Silakan duduk dan itu akan keluar hanya dalam satu menit."
    scene expression ("images/episode12/029.webp") with dissolve
    toby "Izinkan saya."
    lisa "Anda tahu bahwa Anda tidak lagi harus membuat saya terkesan kan? Aku sudah menjadi milikmu."
    toby "Saya suka bagaimana kedengarannya."
    scene expression ("images/episode12/030.webp") with dissolve
    lisa "The \"I'm yours\"bagian?"
    if toby_job == 0:
        toby "Ya. Kedengarannya manis."
        scene expression ("images/episode12/031.webp") with dissolve
        lisa "Kamu benar -benar berpikir begitu?"
        toby "Ya Tuhan, kamu cantik!"
        scene expression ("images/episode12/032.webp") with dissolve
        lisa "Hentikan sudah. Anda membuat saya memerah."
        toby "Saya tidak melakukan apa -apa. Saya hanya mengatakan apa yang saya lihat."
    else:
        toby "Ya. Kedengarannya agak kotor."
        lisa "Kedengarannya kotor karena Anda memiliki pikiran yang kotor."
        toby "Mungkin."
        scene expression ("images/episode12/031.webp") with dissolve
        lisa "Sebenarnya, saya memang ingin itu terdengar sedikit kotor."
        toby "Anda suka berbicara kotor?"
        scene expression ("images/episode12/032.webp") with dissolve
        lisa "Hentikan sudah. Anda membuat saya memerah."
        toby "Saya tidak melakukan apa -apa."

    scene expression ("images/episode12/033_1.webp") with dissolve
    barista "Ini latte Anda."
    lisa "Terima kasih!"
    scene expression ("images/episode12/033_2.webp") with dissolve
    barista "Saya akan kembali dengan makanan Anda dalam beberapa menit."
    toby "Jangan khawatir."
    scene expression ("images/episode12/034.webp") with dissolve
    lisa "Ya Tuhan, aku suka latte ini. Bau, rasanya, semuanya tentang itu, itu sempurna."
    if toby_job == 0:
        toby "Sempurna! Sama sepertimu!"
    else:
        toby "Ya. Ini sangat bagus."

    scene expression ("images/episode12/035_curious.webp") with dissolve
    toby "Bagaimanapun. Selain kopi, apa lagi yang kamu suka?"
    scene expression ("images/episode12/036_thinking.webp") with dissolve
    lisa "Hmm. Saya tidak berpikir ada apa pun yang saya suka seperti kopi, sebenarnya. Maksud saya, saya menikmati koktail dari waktu ke waktu, tetapi jujur saja, saya pikir kopi adalah minuman favorit saya."
    scene expression ("images/episode12/035_smile.webp") with dissolve
    toby "Dan makanan?"
    scene expression ("images/episode12/036_flirty.webp") with dissolve
    lisa "Mencoba mengenal saya lebih baik?"
    scene expression ("images/episode12/035_smile.webp") with dissolve
    toby "Nah, masuk akal. Lagi pula, kami telah berkencan selama hampir dua bulan."
    scene expression ("images/episode12/036_smile.webp") with dissolve
    lisa "Dua bulan yang hebat."
    scene expression ("images/episode12/036_thinking.webp") with dissolve
    lisa "Adapun makanan favorit saya, saya harus pergi dengan sushi."
    scene expression ("images/episode12/035_normal.webp") with dissolve
    toby "Benar-benar? Saya tidak tahan dengan teksturnya. Ketika saya merasakan ikan mentah di lidah saya, saya merasa seperti akan sakit."
    scene expression ("images/episode12/036_smile.webp") with dissolve
    lisa "Itu karena kamu tidak pergi ke tempat yang tepat. Kami harus pergi ke restoran yang saya temukan bersama Lauren beberapa minggu yang lalu."
    scene expression ("images/episode12/035_laugh.webp") with dissolve
    toby "Tidak bisakah saya mengatakan saya bersemangat, tapi pasti."
    if toby_job == 0:
        toby "Apa yang tidak akan saya lakukan untuk gadis cantik seperti Anda."
    else:
        toby "Apa yang tidak akan saya lakukan untuk gadis seksi seperti Anda."

    scene expression ("images/episode12/036_flirty.webp") with dissolve
    lisa "Kamu benar -benar berpikir begitu?"
    scene expression ("images/episode12/035_smile.webp") with dissolve
    toby "Tidak terdengar dangkal, tetapi apakah Anda pikir saya akan berkencan dengan Anda jika saya tidak berpikir begitu?"
    scene expression ("images/episode12/036_curious.webp") with dissolve
    lisa "Apakah itu satu -satunya alasan Anda berkencan dengan saya?"
    scene expression ("images/episode12/035_laugh.webp") with dissolve
    toby "Seperti yang saya katakan, saya tidak ingin terdengar terlalu dangkal."
    scene expression ("images/episode12/036_curious.webp") with dissolve
    lisa "Jadi apa sebenarnya yang Anda sukai dari saya?"
    scene expression ("images/episode12/035_smile.webp") with dissolve
    if toby_job == 0:
        pass
    else:
        toby "Selain pantat cantik Anda, payudara sempurna dan wajah cantik Anda?"
        scene expression ("images/episode12/036_laugh.webp") with dissolve
        lisa "Ya selain itu. Apa yang sebenarnya Anda sukai dari saya?"

    toby "Aku menyukaimu untukmu. Wanita pintar, wanita cantik, gadis manis. Anda secara keseluruhan, saya tidak bisa mengatakan saya suka ini atau itu, karena tidak ada satu hal yang saya tidak suka tentang Anda."
    toby "Saya suka cara Anda berbicara, saya suka cara Anda mendapatkan semua canggung ketika saya memberi Anda pujian, cara Anda tersenyum ketika Anda melihat saya, gairah yang Anda masukkan ketika Anda berbicara tentang bagaimana Anda akan menjadi seorang guru."
    toby "Saya suka betapa perhatian yang Anda bayar untuk setiap detail, dan bagaimana Anda mendengarkan saya ketika saya berbicara tentang masalah saya. Sulit untuk tidak menyukaimu."
    if toby_job == 0:
        scene expression ("images/episode12/036_smile.webp") with dissolve
        lisa "Ya Tuhan, hentikan, atau aku akan menangis!"
        scene expression ("images/episode12/035_surprised.webp") with dissolve
        toby "Menangis? Bukan tanggapan yang saya harapkan ..."
        scene expression ("images/episode12/036_shy.webp") with dissolve
        lisa "Itu adalah hal yang saya miliki. Saya tidak tahu mengapa, tetapi setiap kali saya sangat senang saya akhirnya menangis. Saya cengeng."
        scene expression ("images/episode12/035_smile.webp") with dissolve
        toby "Tidak. Anda tidak! Anda hanya orang yang sangat emosional, itu hal lain yang saya sukai dari Anda."
        scene expression ("images/episode12/036_smile.webp") with dissolve
        lisa "Terima kasih, [toby!c]."
        scene expression ("images/episode12/037.webp") with dissolve
        toby "Sepertinya sarapan kami ada di sini."
    else:
        scene expression ("images/episode12/036_flirty.webp") with dissolve
        lisa "Tuhan, hentikan, atau kita tidak akan makan sarapan sama sekali."
        scene expression ("images/episode12/035_flirty.webp") with dissolve
        toby "Saya tidak melihat masalah dengan itu."
        scene expression ("images/episode12/036_laugh.webp") with dissolve
        lisa "Oke, itu cukup. Diskusi ini semakin panas dari yang seharusnya."
        scene expression ("images/episode12/037.webp") with dissolve
        toby "Disimpan oleh bel."

    scene expression ("images/episode12/038.webp") with dissolve
    barista "Nikmati sarapan Anda!"
    toby "Terima kasih!"
    scene expression ("images/episode12/039.webp") with dissolve
    lisa "Mari kita lihat apakah makanan di sini sebagus kopi."
    toby "Tidak pernah mencobanya?"
    lisa "Tidak. Apakah kamu?"
    toby "Belum, tapi tidak seperti Anda, saya tidak datang ke sini setiap hari."
    scene expression ("images/episode12/040.webp") with dissolve
    lisa "Bon Appetit!"
    scene expression ("images/episode12/041.webp") with dissolve
    toby "Bon Appetit."
    $ ui.saybehavior()
    $ ui.interact()
    show screen ui_message("A few minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/042.webp") with dissolve
    hide screen ui_message
    toby "Sekarang giliran Anda."
    lisa "Giliran saya untuk apa?"
    if toby_job == 0:
        toby "Saya memberi tahu Anda apa yang saya sukai dari Anda, jadi hanya adil untuk mendengar apa yang Anda sukai dari saya."
        scene expression ("images/episode12/043.webp") with dissolve
        lisa "Anda ingin dihujani pujian?"
        toby "Hanya ketika pujian datang dari seorang gadis cantik seperti Anda."
    else:

        toby "Untuk memberi tahu saya apa yang Anda sukai dari saya."
        scene expression ("images/episode12/043.webp") with dissolve
        lisa "Anda ingin dihujani pujian?"
        toby "Hanya ketika pujian datang dari gadis seksi seperti Anda."

    scene expression ("images/episode12/044.webp") with dissolve
    lisa "Pertama -tama, Anda seorang pria yang tampan, ada itu. Tidak ada yang menyangkal itu."
    lisa "Setiap kali aku bersamamu, aku melupakan semua masalahku.Senyummu. Ya Tuhan, aku suka senyummu. Saya suka bagaimana Anda selalu begitu positif, sangat bahagia, selalu tertawa."
    lisa "Saya juga suka fakta bahwa Anda sangat dewasa dan kami dapat membicarakan hal -hal serius, tetapi juga hal -hal kecil yang bodoh. Sulit untuk menjadi keduanya."
    lisa "Biasanya orang terlalu dewasa atau terlalu tidak dewasa, tetapi Anda, Anda berbeda."
    scene expression ("images/episode12/045.webp") with dissolve
    lisa "Satu hal yang saya hargai adalah kenyataan bahwa Anda menghormati saya. Anda memiliki kesabaran dengan saya, menghormati saya, tidak pernah meminta saya telanjang atau melakukan hal lain yang tidak nyaman bagi saya."
    toby "Jadi apakah itu berarti jika saya meminta telanjang, Anda akan mencampakkan saya?"
    scene expression ("images/episode12/043.webp") with dissolve
    lisa "Anda konyol. Yang ingin saya katakan adalah bahwa Anda tidak pernah memaksa saya untuk mengirimi Anda telanjang. Tapi siapa tahu, mungkin saya akan mulai mengirimi Anda beberapa untuk mengingat saya."
    toby "Saya suka itu."
    lisa "Ya, itu hal lain yang saya sukai dari Anda. Anda membantu saya keluar dari cangkang saya. Saya tidak pernah berpikir saya bisa menjadi promiscuous ini. Anda membantu saya menemukan sisi gila dari saya, yang bahkan tidak pernah saya ketahui ada."
    toby "Namun, saya tidak meyakinkan Anda untuk tidak memakai celana dalam."

    scene expression ("images/episode12/046.webp") with dissolve
    lisa "Apakah kamu yakin tentang itu?"
    toby "Tunggu, jangan beri tahu aku, apakah kamu ..."
    scene expression ("images/episode12/047.webp") with dissolve
    lisa "Nah, lalu saya tidak akan mengucapkan sepatah kata pun."
    label memory_38:
        if _in_replay:

            scene expression ("images/utils/black.png") with dissolve
            menu:
                "Pilih pekerjaan Anda"
                "Agen real estat":
                    $ toby_job == 0
                "Manajer klub":
                    $ toby_job == 1
        scene expression ("images/episode12/048.webp") with dissolve
        lisa "Oopsies. Sepertinya saya menjatuhkan garpu saya. Maukah Anda menjadi sayang dan mengambilnya untuk saya?"
        toby "Tentu saja, wanita."
        $ progress = 156
        scene expression ("images/episode12/049.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode12/049_1.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        $ unlockImage(persistent.lisa_11)
        scene expression ("images/episode12/050.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Holy Shit! She really isn't wearing any panties!{/i}"
        scene expression ("images/episode12/051.webp") with dissolve
        toby "Aku sangat menginginkanmu sekarang."
        lisa "Aku sangat terangsang sekarang. Jantungku memompa keluar dari dadaku. Saya tidak pernah melakukan sesuatu yang gila sebelumnya ini sebelumnya."
        toby "Ingin melakukan sesuatu yang lebih gila?"
        lisa "Apa yang lebih gila daripada tidak mengenakan celana dalam di depan umum?"
        scene expression ("images/episode12/052.webp") with dissolve
        toby "Mari ikut saya. Saya punya ide."

        scene expression ("images/episode12/053.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode12/054.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode12/055.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        if emma_path:
            scene expression ("images/episode12/056.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

        scene expression ("images/episode12/057.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode12/058.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        lisa "Tuhan ... Aku menyala dan takut pada saat yang sama. Saya tahu Anda gila, tetapi saya tidak pernah tahu Anda gila!"

        show ep12_059
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode12/059.webp") with dissolve
        hide ep12_059

        scene expression ("images/episode12/060.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        toby "Aku sangat menginginkanmu sekarang."

        scene expression ("images/episode12/061.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        if toby_job == 0:
            lisa "Oh, aku juga, tapi pertama -tama aku ingin menjagamu sebentar."
        else:
            lisa "Anda menginginkan saya? Anda ingin bercinta dengan saya dengan ayam besar Anda? Bagaimana kalau pertama aku mengisap penismu sebentar."

        scene expression ("images/episode12/062.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        if toby_job == 0:
            toby "Jika wanita itu bersikeras ..."
        else:
            toby "Kapan Anda menjadi pelacur kecil yang baik?"
            lisa "Itu semua karena kamu. Anda membantu saya menemukan sisi saya ini yang tidak pernah saya tahu ada di sana."

        scene expression ("images/episode12/063.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        if toby_job == 0:
            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()
        else:
            toby "Itu dia, sayang. Mengisap ayam itu!"

        show ep12_064
        $ ui.saybehavior()
        $ ui.interact()
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's really trying her best. I can see that she wants to make me feel good.{/i}"
        scene expression ("images/episode12/064.webp")
        hide ep12_064

        show ep12_065
        if toby_job == 0:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think I'm in love with this girl. She's so innocent, yet look at her blowing me in public. I never thought this would even be a possibility.{/i}"
        else:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I love how my innocent Lisa is turning into my little slut.{/i}"
        $ ui.saybehavior()
        $ ui.interact()
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck this feels so good.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And she knows that I like it. I can almost see her smiling when I moan.{/i}"
        scene expression ("images/episode12/065.webp")
        hide ep12_065

        show ep12_066
        toby "Ya Tuhan, ini sangat bagus."
        lisa "{size=12}{color=#FDCA6E}* moaning slightly *{/color}{/size}\n{i}Mhmmm.{/i}"
        $ ui.saybehavior()
        $ ui.interact()
        if toby_job == 0:
            toby "Oke, oke, berhentilah. Aku menginginkanmu. Saya ingin berhubungan seks dengan Anda sekarang, saya ingin membuat Anda merasa baik juga."
        else:
            toby "Sial ... hentikan. Aku ingin menidurimu begitu keras sehingga kamu akan meneriakkan namaku seolah -olah tidak ada yang bisa mendengarmu."
        scene expression ("images/episode12/066.webp")
        hide ep12_066

        scene expression ("images/episode12/067.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        lisa "Saya akan menyukainya."

        scene expression ("images/episode12/068.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        if toby_job == 0:
            toby "Anda sangat sempurna."
        else:
            lisa "Persetan denganku. Persetan denganku, [toby!c]."

        show ep12_069
        if toby_job == 0:
            lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nMmmm... Yes! This feel so good."
        else:
            lisa "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nMmmm... You're so big."
        $ ui.saybehavior()
        $ ui.interact()
        if toby_job == 0:
            lisa "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nI love how good it feels to have you inside me."
        else:
            lisa "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nI love how good it feels to have your cock inside me."
        scene expression ("images/episode12/069.webp")
        hide ep12_069

        show ep12_070
        lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes, yes, yes! Right there..."
        lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nThis feels so good."
        $ ui.saybehavior()
        $ ui.interact()
        lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nRight there. Don't stop!"
        scene expression ("images/episode12/070.webp")
        hide ep12_070

        show ep12_071
        lisa "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes, yes, yes, YES!"
        if toby_job == 1:
            lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck me, [toby!c]. Fuck me hard!"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I love it how she's trying to talk dirty for me.{/i}"
        lisa "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nDon't stop, please. Don't stop! Keep going."
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode12/072.webp")
        hide ep12_072

        show ep12_073
        lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYou feel so good, yes! YES!"
        lisa "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nI could do this all day. It feels so, so good!"
        toby "Anda menyukai bagaimana perasaan saya di dalam diri Anda?"
        lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI love it!"
        scene expression ("images/episode12/073.webp")
        hide ep12_073

        show ep12_074
        lisa "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nI'm going to cum soon."
        toby "Saya juga!"
        lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nLet's cum together."
        $ ui.saybehavior()
        $ ui.interact()
        lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes, yes, yes! I'm close."
        toby "Saya akan pergi ke cum!"
        scene expression ("images/episode12/074.webp")
        hide ep12_074

        scene expression ("images/episode12/075_1.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        with flash
        with flash
        lisa "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes! Mhmmm. God, yes!"
        with flash
        lisa "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nGod, that was so good."

        scene expression ("images/episode12/075_2.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        $ unlockImage(persistent.lisa_12)
        $ unlockMemory(persistent.memory_38)
        $ renpy.end_replay()

    if emma_path:
        stop music fadeout 5.0
        scene expression ("images/episode12/076.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Oh, Fuck! Emma! Please tell me she didn't see that.{/i}"
        scene expression ("images/episode12/077.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, fuck, FUCK!{/i}"
        menu:
            "{i} [JGR] Jalanlah setelah Emma {/i}":
                $ emma_pissed = True
                scene expression ("images/episode12/079.webp") with dissolve
                lisa "Kemana kamu pergi?"
                toby "Ummm ... aku ..."
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck! What should I tell her?{/i}"
                toby "Saya pikir seseorang sedang mengambil video kami. Saya akan memastikan mereka menghapusnya."
                scene expression ("images/episode12/080.webp") with dissolve
                lisa "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nWhat? They did what?"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Really, [toby!c]? That's the best you could come up with?{/i}"
                toby "Kembali!"

                call episode12_emmaFight from _call_episode12_emmaFight

                scene expression ("images/episode12/098.webp") with fade
                lisa "Jadi? Apakah Anda mendapatkannya?"
                toby "Ya, jangan khawatir. Itu hanya seorang teman dari pekerjaan yang menguatkan saya. Tidak mencatat apapun."
                scene expression ("images/episode12/099.webp") with dissolve
                lisa "Ya Tuhan, kamu membuatku takut sebentar. Saya pikir saya akan menjadi viral di beberapa situs porno."
                toby "Jangan khawatir, sayang. Semuanya baik -baik saja."

                scene expression ("images/episode12/081.webp") with fade
                lisa "Saya tidak percaya kami baru saja melakukan itu!"
                toby "Ya, itu bagus."
                lisa "Dan ketika Anda meninggalkan saya di sini semua telanjang itu sebenarnya agak menarik."
                toby "Seru? Saya tidak pernah tahu Anda memiliki sisi ini."
                scene expression ("images/episode12/082.webp") with dissolve
                lisa "Apakah Anda bercanda? Aku bahkan tidak tahu aku punya sisi ini."
                toby "Apa yang bisa saya katakan. Senang saya bisa membantu Anda menemukan diri sendiri."
                lisa "Itu menyenangkan, tapi kami tidak akan melakukannya lagi. Cukup bahwa satu orang melihat kita."
                toby "Ya, Anda benar."
                scene expression ("images/episode12/083.webp") with dissolve
                lisa "Saya pikir kita harus kembali ke rumah, saya punya ujian besok, tetapi saya tidak bisa melewatkan kencan dengan Anda."
                toby "Saya merasa tidak enak sekarang."
                lisa "Jangan khawatir, aku tidak akan gagal dan selain itu, itu bukan ujian yang sangat penting."
                toby "Oke, kalau begitu. Mari pulang."

                return
            "{i} tetap dengan lisa {/i} [JWRN11]"(csq="Jalur Emma ditutup"):

                $ renpy.notify("Emma's path has been closed!")
                $ emma_path = False
                $ emma_pissed = True
                pass

    scene expression ("images/episode12/078.webp") with dissolve
    lisa "Aku mencintaimu, [toby!c]."
    if toby_job == 0:
        toby "Aku juga mencintaimu, Lisa!"
        if ep7_lisa_loveYouBack:
            lisa "Itu membuat saya sangat senang akhirnya mendengarnya. Saya pikir Anda tidak akan pernah mengatakannya kembali!"
            toby "Maaf tentang itu. Saya terkejut."
    else:
        toby "Anda sempurna!"

    scene expression ("images/episode12/081.webp") with fade
    lisa "Saya tidak percaya kami baru saja melakukan itu!"
    toby "Ya, itu bagus."
    lisa "Mengetahui bahwa seseorang bisa masuk ke kami, membuatnya begitu mendebarkan."
    toby "Saya tidak pernah tahu Anda memiliki sisi ini."
    scene expression ("images/episode12/082.webp") with dissolve
    lisa "Apakah Anda bercanda? Aku bahkan tidak tahu aku punya sisi ini."
    toby "Apa yang bisa saya katakan. Senang saya bisa membantu Anda menemukan diri sendiri."
    lisa "Itu menyenangkan, tapi kami tidak akan melakukannya lagi dalam waktu dekat. Saya masih lebih suka tempat tidur."
    toby "Ya, Anda benar."
    scene expression ("images/episode12/083.webp") with dissolve
    lisa "Saya pikir kita harus kembali ke rumah, saya punya ujian besok, tetapi saya tidak bisa melewatkan kencan dengan Anda."
    toby "Saya merasa tidak enak sekarang."
    lisa "Jangan khawatir, aku tidak akan gagal dan selain itu, itu bukan ujian yang sangat penting."
    toby "Oke, kalau begitu. Mari pulang."

    return

label episode12_lisa_side:
    play sound "audio/fx/notification_5.mp3"
    scene expression ("images/episode12/003_lisa.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}A message from Lisa? Definitely not what I was expecting.{/i}"
    scene expression ("images/episode12/004_texting.webp") with dissolve
    call sms_incoming ("lisa", "Okay!") from _call_sms_incoming_234
    call sms_sent ("lisa", "Morning, Lisa. I'm happy for you, but okay what?") from _call_sms_sent_184
    call sms_incoming ("lisa", "You asked me a question yesterday.") from _call_sms_incoming_235
    call sms_sent ("lisa", "You gotta be more specific. Don't get me wrong, it's nice to know that you agree with me, but on what?") from _call_sms_sent_185
    call sms_incoming ("lisa", "You're really going to make me say it?") from _call_sms_incoming_236
    call sms_sent ("lisa", "Sure?") from _call_sms_sent_186
    call sms_incoming ("lisa", "You asked me if I wanted to go out with you today.") from _call_sms_incoming_237
    call sms_incoming ("lisa", "To talk about football, cars and girls.") from _call_sms_incoming_238
    call sms_sent ("lisa", "Oh, Right! Of course. Pick you up in 30 minutes?") from _call_sms_sent_187
    call sms_incoming ("lisa", "You want to meet up right now, in broad daylight?") from _call_sms_incoming_239
    call sms_sent ("lisa", "Look Lisa, you're a beautiful woman. I think dating you in the morning might be the best choice, because usually at night I get all kinds of weird ideas.") from _call_sms_sent_188
    call sms_incoming ("lisa", "How weird?") from _call_sms_incoming_240
    call sms_sent ("lisa", "Let's just say that I would look into your gorgeous eyes, those beautiful lips and all I would think about is kissing you. Kissing your long thin neck, your bare shoulders...") from _call_sms_sent_189
    call sms_incoming ("lisa", "Yeah, you're right. That is weird. ") from _call_sms_incoming_241
    call sms_sent ("lisa", "So pick you up in 30 minutes?") from _call_sms_sent_190
    call sms_incoming ("lisa", "No. I can't risk Lauren seeing us. She would never forgive me.") from _call_sms_incoming_242
    call sms_sent ("lisa", "We won't do anything bad.") from _call_sms_sent_191
    call sms_incoming ("lisa", "She doesn't know that. So let's just meet at the coffee shop in 30 minutes.") from _call_sms_incoming_243
    call sms_sent ("lisa", "That's perfect.") from _call_sms_sent_192
    call sms_incoming ("lisa", "Am I going to regret this?") from _call_sms_incoming_244
    call sms_sent ("lisa", "I don't know about you, but I won't.") from _call_sms_sent_193
    call sms_incoming ("lisa", "Fine. Then I won't regret it either.") from _call_sms_incoming_245
    call sms_sent ("lisa", "See you in 30 minutes.") from _call_sms_sent_194
    call sms_incoming ("lisa", "See ya.") from _call_sms_incoming_246
    scene expression ("images/episode12/007.webp") with dissolve
    hide screen message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Ummm... I never expected that, but I can't say I don't like it.{/i}"

    call episode12_morningCharlotte from _call_episode12_morningCharlotte_1

    scene expression ("images/episode12/084.webp") with fade
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/085.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is that Lisa?{/i}"
    scene expression ("images/episode12/086.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()


    $ progress = 155
    scene expression ("images/episode12/087.webp") with dissolve
    toby "Pagi."
    lisa "Pagi, [toby!c]."
    toby "Kamu terlihat cantik pagi ini."
    scene expression ("images/episode12/024.webp") with dissolve
    lisa "Tapi tidak seindah Lauren, kan?"
    toby "Anda bermain keras."

    scene expression ("images/episode12/025.webp") with fade
    barista "Selamat pagi. Apa yang bisa saya dapatkan dari Anda?"
    scene expression ("images/episode12/026.webp") with dissolve
    toby "Pancake Special dan cappuccino."
    scene expression ("images/episode12/027.webp") with dissolve
    toby "Dan untukmu?"
    scene expression ("images/episode12/028.webp") with dissolve
    lisa "Hal yang sama, tetapi dengan latte bukan cappuccino."
    scene expression ("images/episode12/025.webp") with dissolve
    barista "Sempurna. Silakan duduk dan itu akan keluar hanya dalam satu menit."
    scene expression ("images/episode12/029.webp") with dissolve
    toby "Izinkan saya."
    lisa "Mengapa Anda mencoba membuat saya terkesan?"
    toby "Siapa yang mengatakan apapun tentang mengesankanmu. Saya hanya memastikan Anda merasa nyaman sementara kami berbicara tentang mobil, sepak bola, dan gadis."
    scene expression ("images/episode12/030.webp") with dissolve
    lisa "Ya. Mobil, sepak bola, dan gadis."
    toby "Jadi? Apa tim sepak bola favorit Anda?"
    lisa "Hmmm ... Sebenarnya, mari kita bicara tentang mobil."
    scene expression ("images/episode12/031.webp") with dissolve
    toby "Apa mobil favoritmu?"
    lisa "Mobil favorit saya? Pfft ... itu yang sulit. Mungkin kita harus berbicara tentang gadis."
    lisa "Siapa gadis favoritmu?"
    toby "Itu juga sulit, tapi saya harus mengatakan bahwa Anda berada di lima besar saya."
    scene expression ("images/episode12/032.webp") with dissolve
    lisa "Hanya lima?"
    toby "Ya, Anda benar. Sepuluh teratas sebenarnya."
    scene expression ("images/episode12/033_1.webp") with dissolve
    barista "Ini latte Anda."
    lisa "Terima kasih!"
    scene expression ("images/episode12/033_2.webp") with dissolve
    barista "Saya akan kembali dengan makanan Anda hanya dalam beberapa menit."
    toby "Jangan khawatir."
    scene expression ("images/episode12/034.webp") with dissolve
    lisa "Ya Tuhan, aku suka kopi ini. Kedai kopi ini pasti berada di posisi tiga teratas saya. Lihat, begitulah cara Anda melakukannya."
    scene expression ("images/episode12/035_smile.webp") with dissolve
    toby "Ya, tapi Anda sudah minum kopi. Tempat ini tidak ada dalam tiga teratas Anda sebelum mencicipi kopi mereka."
    scene expression ("images/episode12/036_surprised.webp") with dissolve
    lisa "Jadi Anda harus mencicipi saya terlebih dahulu sebelum saya mencapai tiga besar?"
    scene expression ("images/episode12/035_laugh.webp") with dissolve
    toby "Ya, sebelum Anda mendapat kesempatan untuk menjadi yang teratas, karena siapa tahu. Saya mungkin tidak menyukainya."
    scene expression ("images/episode12/036_flirty.webp") with dissolve
    lisa "Oh, percayalah. Anda akan menyukainya."
    scene expression ("images/episode12/035_normal.webp") with dissolve
    toby "Saya tipe pria yang membutuhkan bukti."
    scene expression ("images/episode12/036_shy.webp") with dissolve
    lisa "Ya Tuhan, ini adalah ide yang bodoh. Saya seharusnya tidak datang. Saya harus pergi."
    scene expression ("images/episode12/035_laugh.webp") with dissolve
    toby "Tunggu. Tolong jangan pergi. Saya akan berhenti menggoda."
    scene expression ("images/episode12/035_smile.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}For now.{/i}"
    scene expression ("images/episode12/036_laugh.webp") with dissolve
    lisa "Saya mendengarnya."
    scene expression ("images/episode12/035_laugh.webp") with dissolve
    toby "Bagus. Jadi mengapa Anda tidak memberi tahu saya lebih banyak tentang diri Anda."
    scene expression ("images/episode12/036_thinking.webp") with dissolve
    lisa "Saya pikir kami akan berbicara tentang sepak bola, mobil, dan gadis."
    scene expression ("images/episode12/035_smile.webp") with dissolve
    toby "Ya, kami agak kelelahan topik -topik itu dan yang tersisa adalah tentang Anda."
    scene expression ("images/episode12/036_laugh.webp") with dissolve
    lisa "Dan kamu."
    scene expression ("images/episode12/035_flirty.webp") with dissolve
    toby "Anda ingin mengenal saya?"
    scene expression ("images/episode12/036_flirty.webp") with dissolve
    lisa "Saya pikir Anda akan berhenti menggoda?"
    scene expression ("images/episode12/035_laugh.webp") with dissolve
    toby "Sangat sulit untuk menahan diri ketika saya sarapan dengan seseorang secantik Anda."
    scene expression ("images/episode12/036_shy.webp") with dissolve
    lisa "Ya Tuhan, aku merasa sangat malu. Ini adalah kesalahan. Anda adalah pacar Lauren."
    scene expression ("images/episode12/035_normal.webp") with dissolve
    toby "Saya minta maaf jika saya membuat Anda tidak nyaman, saya berjanji akan berhenti."
    scene expression ("images/episode12/036_smile.webp") with dissolve
    lisa "Terima kasih."
    scene expression ("images/episode12/035_smile.webp") with dissolve
    toby "Jadi? Ceritakan lebih banyak tentang diri Anda. Apakah Anda punya saudara kandung? Adakah mimpi yang menarik, aspirasi?"
    scene expression ("images/episode12/036_smile.webp") with dissolve
    lisa "Ya, saya punya kakak. Ya Tuhan, kita biasa bertarung sepanjang waktu."
    scene expression ("images/episode12/035_laugh.webp") with dissolve
    toby "Untuk itulah kakak laki -laki."
    scene expression ("images/episode12/036_laugh.webp") with dissolve
    lisa "Ya, saya pikir Anda benar."
    scene expression ("images/episode12/036_smile.webp") with dissolve
    lisa "Giliran Anda sekarang. Ceritakan sesuatu tentang diri Anda. Sesuatu yang menarik terjadi pada Anda belakangan ini?"
    scene expression ("images/episode12/035_normal.webp") with dissolve
    toby "Faktanya, ya itu terjadi. Saya menemukan beberapa keterampilan baru."
    scene expression ("images/episode12/036_curious.webp") with dissolve
    lisa "Anda tidak mengatakan. Keterampilan apa?"
    scene expression ("images/episode12/035_smile.webp") with dissolve
    toby "Saya agak profesional konstruksi."
    scene expression ("images/episode12/036_smile.webp") with dissolve
    lisa "Benar-benar? Itu menarik. Ayah saya memiliki perusahaan konstruksi."
    scene expression ("images/episode12/036_laugh.webp") with dissolve
    if toby_job == 0:
        lisa "Nah, jika hal real estat tidak berhasil, saya bisa meminta ayah saya untuk membawa Anda."
    else:
        lisa "Nah, jika Anda muak dengan apa pun yang Anda lakukan di klub itu, saya bisa memintanya untuk mempekerjakan Anda."
    scene expression ("images/episode12/035_laugh.webp") with dissolve
    toby "Profesional mungkin sedikit kuat. Baru -baru ini saya merenovasi loteng dan halaman kami, tetapi saya harus mengatakan, keduanya sebenarnya keluar cukup bagus."
    scene expression ("images/episode12/036_curious.webp") with dissolve
    lisa "Punya gambar?"
    scene expression ("images/episode12/035_normal.webp") with dissolve
    toby "Tidak terlalu. Maksud saya, saya tidak berharap Anda tertarik pada kemampuan konstruksi saya."
    scene expression ("images/episode12/036_smile.webp") with dissolve
    lisa "Apa yang bisa saya katakan. Anda bukan satu -satunya dengan keterampilan itu."
    scene expression ("images/episode12/035_curious.webp") with dissolve
    toby "Anda berbicara tentang ayah dan saudara laki -laki Anda, kan?"
    scene expression ("images/episode12/036_laugh.webp") with dissolve
    lisa "And their sister/daughter."
    scene expression ("images/episode12/035_surprised.webp") with dissolve
    toby "Sekarang saya sangat penasaran."
    scene expression ("images/episode12/036_laugh.webp") with dissolve
    lisa "Jangan menjadi. Saya kebanyakan membersihkan alat dan menyapu."
    scene expression ("images/episode12/035_laugh.webp") with dissolve
    toby "Benar-benar? Saya tidak bisa membayangkan Anda dengan salah satu topi kuning di situs konstruksi."
    scene expression ("images/episode12/036_cool.webp") with dissolve
    lisa "Itu disebut topi keras."
    scene expression ("images/episode12/035_smile.webp") with dissolve
    toby "Ya, ya ..."
    scene expression ("images/episode12/036_laugh.webp") with dissolve
    lisa "Yah, aku tidak selalu menjadi gadis yang baik. Setiap kali saya mendapat masalah, ayah saya akan membawa saya dan saudara lelaki saya ke situs konstruksi sebagai hukuman."
    scene expression ("images/episode12/035_laugh.webp") with dissolve
    toby "Itulah yang saya sebut pengasuhan yang baik."
    scene expression ("images/episode12/036_smile.webp") with dissolve
    lisa "Giliran Anda sekarang. Apa hukuman Anda karena berperilaku buruk?"
    scene expression ("images/episode12/037.webp") with dissolve
    toby "Disimpan oleh bel."
    lisa "Oh, tidak ada tuan. Anda tidak bisa melepaskannya dengan mudah."
    lisa "Anda beruntung bahwa saya benar -benar lapar, tetapi setelah kami makan, Anda dan saya akan menyelesaikan percakapan ini."
    scene expression ("images/episode12/038.webp") with dissolve
    barista "Menikmati!"
    toby "Terima kasih!"
    scene expression ("images/episode12/039.webp") with dissolve
    lisa "Mari kita lihat apakah makanan di sini sebagus kopi."
    toby "Tidak pernah mencobanya?"
    lisa "Tidak. Apakah kamu?"
    toby "Belum, tapi tidak seperti Anda, saya tidak datang ke sini setiap hari."
    scene expression ("images/episode12/040.webp") with dissolve
    lisa "Bon Appetit!"
    toby "Bon Appetit."
    scene expression ("images/episode12/041.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    show screen ui_message("A few minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/042.webp") with dissolve
    hide screen ui_message
    lisa "Jadi? Bagaimana Anda dihukum saat Anda masih kecil?"
    toby "Umm ... sebenarnya aku tidak terlalu jauh dari milikmu. Suatu kali saya mencuri uang dan sebagai hukuman saya harus membersihkan kantor selama sebulan."
    lisa "Selama sebulan? Berapa banyak uang yang Anda curi?"
    toby "Sekitar 00?"
    scene expression ("images/episode12/043.webp") with dissolve
    lisa "00? Untuk apa Anda membutuhkan 00?"
    toby "Nah, ada gadis ini di kelas saya. Gadis cantik. Mata hijau besar, rambut pirang. Semua yang bisa Anda harapkan dari seorang gadis."
    scene expression ("images/episode12/044.webp") with dissolve
    lisa "Ini hampir seperti Anda memiliki tipe."
    toby "Ya. Itu selalu menjadi kelemahan saya."
    scene expression ("images/episode12/046.webp") with dissolve
    lisa "Dan apa yang Anda lakukan dengan 00?"
    toby "Yah, aku tahu dia tidak punya sepeda, jadi aku pergi dan membelikannya sepeda merah muda dengan keranjang putih kecil yang lucu, yang aku isi dengan permen. Saya menghabiskan sisa uang untuk permen."
    scene expression ("images/episode12/043.webp") with dissolve
    lisa "Seorang pemikat sejati. Berapa umurmu?"
    toby "Aku tidak tahu. Dua belas?"
    lisa "Jadi? Bagaimana dia membalasmu?"
    toby "Dia menciumku. Itu adalah ciuman pertamaku."
    $ progress = 156
    scene expression ("images/episode12/045.webp") with dissolve
    lisa "Itu ciuman yang mahal."
    toby "Itu bernilai setiap sen."
    lisa "Apakah Anda masih memiliki panjang yang sama untuk ciuman?"
    toby "Selalu. Terutama jika gadis itu memiliki mata hijau dan rambut pirang."
    scene expression ("images/episode12/088.webp") with dissolve
    lisa "Maaf, [toby!c]. Anda orang yang baik, tapi ini kesalahan. Saya seharusnya tidak datang."
    toby "Lisa, tunggu. Saya tahu saya bilang saya berhenti. Saya minta maaf."
    scene expression ("images/episode12/089.webp") with dissolve
    lisa "Bukan itu, tetapi Anda adalah pacar Lauren. Dia sahabatku. Saya tidak bisa melakukan ini."
    toby "Lakukan apa?"
    lisa "Anda tahu persis apa yang kami lakukan. Anda menggoda dengan saya dan tidak membuat saya salah, ini bagus. Ini sebenarnya tanggal terbaik yang pernah saya kunjungi dalam beberapa bulan."
    lisa "Anda seorang pria yang hebat, tetapi saya tidak bisa. Saya tidak bisa melakukan ini. Aku mulai menyukaimu dan itu salah."
    scene expression ("images/episode12/090.webp") with dissolve
    toby "Berhentilah memikirkannya sebentar. Kami bersenang -senang. Sebenarnya sangat bagus."
    lisa "Ya, sudah."
    toby "Lihat, kamu cantik, pintar, lucu dan lucu. Saya minta maaf jika saya membuat Anda merasa tidak nyaman, tetapi saya tidak bisa membantu. Ketika saya melihat Anda, yang ingin saya lakukan hanyalah mencium Anda."
    scene expression ("images/episode12/091.webp") with dissolve
    lisa "..."
    toby "Tolong jangan membenci saya untuk ini."
    show ep12_092
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/092.webp") with dissolve
    hide ep12_092
    $ unlockImage(persistent.lisa_13)
    lisa "..."
    toby "Bisakah kita kembali ke tempat duduk kita sekarang?"
    if emma_path:
        stop music fadeout 5.0
        scene expression ("images/episode12/093.webp") with dissolve
        lisa "Saya maafkan, [toby!c]. Aku harus pergi!"
        scene expression ("images/episode12/095.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit, shit, shit! She saw that.{/i}"
        scene expression ("images/episode12/096.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, fuck, FUCK!{/i}"
        menu:
            "{i} [JGR] Jalanlah setelah Emma {/i}":
                $ emma_pissed = True
                call episode12_emmaFight from _call_episode12_emmaFight_1
            "{i} don \ 't mengejar Emma {/i} [JWRN11]"(csq="Jalur Emma ditutup"):

                $ emma_path = False
                $ emma_pissed = True
                scene expression ("images/episode12/097.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What's the point? It's not like she's going to forgive me. Fuck!{/i}"
    else:
        scene expression ("images/episode12/094.webp") with dissolve
        lisa "Saya maafkan, [toby!c]. Aku harus pergi!"
        scene expression ("images/episode12/097.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I sure hope I didn't mess things up!{/i}"

    return

label episode12_lauren_main:

    scene expression ("images/episode12/002.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Speaking of dates, Yesterday I promised Lauren that we'd go out today.{/i}"
    if patricia_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit! I also promised Tris we'd go out tonight. That means I'll have to go out with Lauren for breakfast so I can have my evening free for Tris.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I kinda want to go out with her right now. After all, I did tell her we'd get a room today.{/i}"
    scene expression ("images/episode12/004_texting.webp") with dissolve
    call sms_sent ("lauren", "Morning sexy. You awake?") from _call_sms_sent_195
    call sms_incoming ("lauren", "What do you think?", img_icon="images/episode12/100_icon.webp", img="images/episode12/100.webp") from _call_sms_incoming_247
    call sms_sent ("lauren", "That you look really, really sexy.") from _call_sms_sent_196
    call sms_incoming ("lauren", "And you haven't seen all of it.") from _call_sms_incoming_248
    call sms_sent ("lauren", "Why don't you show me then.") from _call_sms_sent_197
    call sms_incoming ("lauren", "How about now?", img_icon="images/episode12/101_icon.webp", img="images/episode12/101.webp") from _call_sms_incoming_249
    call sms_sent ("lauren", "Now I'm really glad that I decided to text you this morning.") from _call_sms_sent_198
    call sms_incoming ("lauren", "Why is that?") from _call_sms_incoming_250
    call sms_sent ("lauren", "Because I told you we'd go out today, so I wanted to see if you still want to do something.") from _call_sms_sent_199
    call sms_incoming ("lauren", "Actually you said that we'd go in, not out. Something about a room, if I remember correctly.") from _call_sms_incoming_251
    call sms_sent ("lauren", "First we need to eat something. After all, we'll need energy if we're going to fuck all day long.") from _call_sms_sent_200
    call sms_incoming ("lauren", "All day long?") from _call_sms_incoming_252
    call sms_sent ("lauren", "Of course. I'll come pick you up in 30 minutes and we have the whole day at our disposal.") from _call_sms_sent_201
    call sms_incoming ("lauren", "Oh my. How am I going to dance tomorrow in my dance class? Will I be able to stand or sit at all after you're done with me?") from _call_sms_incoming_253
    call sms_sent ("lauren", "Maybe. I'll try to be careful to not ruin you completely.") from _call_sms_sent_202
    call sms_incoming ("lauren", "Then I guess I should get ready.") from _call_sms_incoming_254
    call sms_sent ("lauren", "Yes, you should.") from _call_sms_sent_203
    call sms_incoming ("lauren", "Call me when you're downstairs.") from _call_sms_incoming_255
    call sms_sent ("lauren", "Sure.") from _call_sms_sent_204
    scene expression ("images/episode12/007.webp") with dissolve
    hide screen message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I love how crazy Lauren is.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'd better get ready too.{/i}"

    call episode12_morningCharlotte from _call_episode12_morningCharlotte_2

    $ progress = 155
    scene expression ("images/episode12/084.webp") with fade
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/102.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/103.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should call Lauren and let her know I'm here.{/i}"
    scene expression ("images/episode12/104.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nHi sexy."
    lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nHi there, my stallion."
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nStallion?"
    lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nWould you prefer lion? They are both very virile."
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nLet's go for stallion for now because it's more accurate. Physically."
    lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nYeah, I think you're right. No difference in size whatsoever."
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nI'm glad we agree on that."
    lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nAre you downstairs?"
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nYes, I am."
    lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nCool. Be down in a minute."
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nI'll be waiting for you."
    lauren "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nSee ya."
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nSee ya."


    scene expression ("images/episode12/105.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    lauren "Hai seksi."
    scene expression ("images/episode12/106.webp") with dissolve
    toby "Maksudmu kuda jantan."

    scene expression ("images/episode12/106_2.webp") with dissolve
    $ unlockImage(persistent.lauren_11)
    lauren "Oh benar ..."
    lauren "Salahku. Maksudku, \"Hai, kuda jantan seksi.\""
    toby "Saya bisa hidup dengan itu."
    lauren "Dan aku bisa mencium."
    show ep12_107
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/107.webp") with dissolve
    hide ep12_107

    lauren "Jadi? Dimana sekarang?"
    toby "Sekarang kami pergi ke kedai kopi yang sangat Anda dan Lisa sangat mencintai dan mengambil sarapan dan kemudian jika Anda seorang gadis yang baik, sangat dekat dengan kedai kopi di sana adalah motel yang mungkin harus kita kunjungi."
    scene expression ("images/episode12/108.webp") with dissolve
    lauren "Dan jika saya seorang gadis nakal?"
    toby "Lalu kita pergi ke motel terlebih dahulu."
    lauren "Belakang ... Jangan menggoda saya."
    scene expression ("images/episode12/109.webp") with dissolve
    toby "Naik sekali!"
    scene expression ("images/episode12/110.webp") with dissolve
    lauren "Dengan senang hati."
    scene expression ("images/episode12/111.webp") with dissolve
    toby "Setelah Anda."
    lauren "Apakah Anda menjadi seorang pria atau Anda hanya ingin menatap pantat saya."
    if toby_job == 0:
        toby "Mari kita katakan bahwa aku seorang pria yang menikmati pilihan hidupnya."
    else:
        toby "Saya bisa menatap pantat Anda selama berjam -jam dan tidak bosan."
        lauren "Saya akan menjadi gadis yang baik sehingga kami pergi ke motel itu dan menguji teori itu."
    scene expression ("images/episode12/112.webp") with dissolve
    barista "Pagi. Apa yang bisa saya dapatkan dari Anda?"
    scene expression ("images/episode12/113.webp") with dissolve
    toby "Saya suka pancake khusus dan cappuccino."
    scene expression ("images/episode12/114.webp") with dissolve
    lauren "Tolong, hal yang sama untuk saya!"
    scene expression ("images/episode12/112.webp") with dissolve
    barista "Sempurna. Silakan duduk dan itu akan keluar hanya dalam satu menit."
    scene expression ("images/episode12/115.webp") with dissolve
    toby "Jadi Anda memiliki kelas dansa besok?"
    lauren "Ya. Saya suka kelas itu dan Mrs. Lopez, guru saya, adalah yang terbaik. Dia menari, sangat bagus."
    scene expression ("images/episode12/116.webp") with dissolve
    lauren "Saya ingin sekali menjadi penari sebaik dia."
    toby "Saya yakin Anda adalah penari yang baik."
    lauren "Apakah Anda bercanda? Saya adalah penari terbaik yang pernah Anda ketahui, karena Anda tidak akan pernah bertemu dengan Nyonya Lopez."
    toby "Saya akan percaya ketika saya akan melihatnya."
    scene expression ("images/episode12/117.webp") with dissolve
    lauren "Anda ingin saya menari untuk Anda di sini dan sekarang? Karena saya akan melakukannya."
    toby "Saya berpikir mungkin menari untuk saya sesudahnya."
    lauren "Saya tidak tahu tarian semacam itu, Anda cabul."
    scene expression ("images/episode12/118.webp") with dissolve
    barista "Permisi. Ini kopimu. Makanan Anda akan keluar hanya dalam beberapa menit."
    toby "Tidak masalah, ma \ 'am. Terima kasih!"
    scene expression ("images/episode12/119.webp") with dissolve
    lauren "Mengapa Anda tidak memberi tahu saya bahwa dia ada di sana. Anda membiarkan saya mempermalukan diri sendiri."
    toby "Jangan khawatir, dia tidak tahu apa yang kita bicarakan."
    scene expression ("images/episode12/120_meh.webp") with dissolve
    lauren "Ya, karena sangat sulit untuk menguraikan apa yang kita bicarakan."
    scene expression ("images/episode12/121_flirty.webp") with dissolve
    toby "Jadi, kembali ke pertanyaan kami. Kapan Anda akan menari untuk saya?"
    scene expression ("images/episode12/120_laugh.webp") with dissolve
    lauren "Sudah kubilang, aku tidak tahu tarian kotor."
    scene expression ("images/episode12/121_normal.webp") with dissolve
    toby "Okay, I believe you, but you also promised me you're going to pole dance for me. Actually it was a \"private\"Sesi dansa, tapi ya saya akan sangat tertarik untuk melihatnya."
    scene expression ("images/episode12/120_laugh.webp") with dissolve
    lauren "Jangan beri tahu saya bahwa motel telah dipasang tiang di kamar, karena saya mungkin mendapatkan kecurigaan."
    scene expression ("images/episode12/121_laugh.webp") with dissolve
    toby "Tidak, tentu saja tidak."
    scene expression ("images/episode12/121_smile.webp") with dissolve
    toby "Sebenarnya saya tidak tahu. Saya tidak pernah ke sana, jadi saya tidak tahu. Tapi kemungkinan besar mereka tidak memiliki tiang di kamar."
    scene expression ("images/episode12/120_curious.webp") with dissolve
    lauren "Jadi Anda tidak pernah membawa pelacur Anda ke motel ini yang Anda bicarakan?"

    if toby_job == 0:
        scene expression ("images/episode12/121_laugh.webp") with dissolve
        toby "Ya. Saya tidak punya pelacur. Saya hanya punya pacar."
        scene expression ("images/episode12/120_surprised.webp") with dissolve
        lauren "Berapa banyak pacar yang Anda punya?"
    else:
        scene expression ("images/episode12/121_flirty.webp") with dissolve
        toby "Pernahkah saya membawa Anda ke sana? Jadi tidak, saya belum mengambil pelacur saya ke sana."
        scene expression ("images/episode12/120_surprised.webp") with dissolve
        lauren "Jadi Anda tidak menyangkalnya. Berapa banyak pelacur yang kamu punya?"

    scene expression ("images/episode12/121_curious.webp") with dissolve
    toby "Berapa banyak yang saya izinkan tanpa Anda marah pada saya?"
    scene expression ("images/episode12/120_laugh.webp") with dissolve
    lauren "Hmmm ... itu yang sulit. Mari kita katakan empat."
    scene expression ("images/episode12/121_smile.webp") with dissolve
    toby "Ah oke. Kami baik -baik saja. Saya hanya punya tiga."
    scene expression ("images/episode12/120_surprised.webp") with dissolve
    lauren "Apakah kamu serius?"
    scene expression ("images/episode12/121_laugh.webp") with dissolve
    toby "Tidak, tentu saja tidak. Saya memiliki lebih dari empat."
    scene expression ("images/episode12/120_normal.webp") with dissolve
    lauren "Anda mengolok -olok saya."
    scene expression ("images/episode12/121_smile.webp") with dissolve
    toby "Siapa? Aku? Tentu saja tidak!"
    scene expression ("images/episode12/120_cool.webp") with dissolve
    lauren "Perhatikan bayi punggung Anda. Atau lebih baik lagi, perhatikan kemaluanmu, karena aku akan menggigitnya."
    scene expression ("images/episode12/121_smile.webp") with dissolve
    toby "Kira kita akan melewatkan foreplay hari ini. Tidak ada blowjobs untukku."
    scene expression ("images/episode12/120_normal.webp") with dissolve
    lauren "Tidak ... Saya suka foreplay."
    if toby_job == 0:
        scene expression ("images/episode12/121_smile.webp") with dissolve
        toby "Nah, dalam hal ini, saya tidak bisa mengambil kesenangan Anda."
    else:

        scene expression ("images/episode12/121_flirty.webp") with dissolve
        toby "Anda suka mengisap ayam, jangan Anda!"
        scene expression ("images/episode12/120_laugh.webp") with dissolve
        lauren "Anda membuatnya terdengar sangat kotor, tetapi jujur saja, saya ingin melihat Anda semua bersemangat."
        scene expression ("images/episode12/121_smile.webp") with dissolve
        toby "Bagus. Kami tidak akan melewatkan foreplay."

    scene expression ("images/episode12/120_smile.webp") with dissolve
    lauren "Terima kasih, Sayang!"
    scene expression ("images/episode12/121_laugh.webp") with dissolve
    toby "Kesenangan itu milikku."
    scene expression ("images/episode12/120_laugh.webp") with dissolve
    lauren "Kecuali ketika saya menggigit kemaluan Anda, tetapi selain itu, ya kesenangan akan menjadi milik Anda."
    scene expression ("images/episode12/121_smile.webp") with dissolve
    toby "Jadi saya kira saya tidak diizinkan memiliki lebih dari satu pacar."
    scene expression ("images/episode12/120_normal.webp") with dissolve
    lauren "Tidak, Anda diizinkan, tetapi hanya jika gadis itu dapat memberi Anda sesuatu yang saya bisa. Jika Anda membutuhkan sesuatu dan saya tidak bisa memberikannya, maka masuk akal bagi Anda untuk memiliki lebih dari satu pacar."
    scene expression ("images/episode12/121_curious.webp") with dissolve
    toby "Itu cara berpikir yang menarik."
    scene expression ("images/episode12/120_smile.webp") with dissolve
    lauren "Terima kasih! Saya tahu, saya yang terbaik. Jadi jika dia menidurimu lebih baik dari yang aku bisa, maka itu baik -baik saja. Tetapi jika tidak, maka saya minta maaf sayang."
    scene expression ("images/episode12/121_curious.webp") with dissolve
    toby "Tetapi untuk mengetahui apakah dia lebih baik, tidakkah itu berarti saya harus mencobanya?"
    scene expression ("images/episode12/120_thinking.webp") with dissolve
    lauren "Hmmm ... itu poin yang valid. Saya kira Anda tidak diizinkan mencari seorang gadis yang bisa meniduri Anda lebih baik dari saya, jadi itu tidak ada gunanya, sungguh. Anda tidak bisa menemukan orang yang lebih baik dari saya."
    scene expression ("images/episode12/121_laugh.webp") with dissolve
    toby "Seseorang bersikap sombong di sini."
    scene expression ("images/episode12/120_flirty.webp") with dissolve
    lauren "Saya tahu keterampilan saya, sayang."
    scene expression ("images/episode12/122.webp") with dissolve
    lauren "Because when I'm on top of you, I'm going to ride you like a true cowgirl. I put the \"girl\"di posisi cowgirl."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's going to do it again.{/i}"
    lauren "Tidak bisa menunggu untuk selesai makan sehingga kami bisa pergi dan mengendarai Anda sepanjang hari, sampai Anda tidak memiliki lagi cum di bola -bola Anda."
    scene expression ("images/episode12/123.webp") with dissolve
    barista "Permisi. Ini makananmu."
    toby "Terima kasih Ma \ 'Am."
    barista "Menikmati!"
    scene expression ("images/episode12/124.webp") with dissolve
    lauren "Anda bajingan! Anda membiarkan saya melakukannya lagi. Apa yang akan dipikirkan wanita ini tentang saya?"
    toby "Dia akan mengira Anda seorang gadis yang sangat nakal."
    lauren "Persetan denganmu, [toby!c]."
    toby "Segera, sayang. Segera!"
    scene expression ("images/episode12/125.webp") with dissolve
    lauren "Tak sabar menunggu."
    scene expression ("images/episode12/126.webp") with dissolve
    toby "Bon Appetit."
    lauren "Bon Appetit."
    show screen ui_message("A few minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/127.webp") with dissolve
    hide screen ui_message
    lauren "Ini adalah sarapan terbaik yang saya miliki selama bertahun -tahun."
    toby "Senang Anda menyukainya."
    scene expression ("images/episode12/128.webp") with dissolve
    toby "Bagaimana dengan hidangan penutup sekarang?"
    lauren "Memimpin jalan, koboi."
    scene expression ("images/episode12/129.webp") with dissolve
    toby "For my \"cowgirl\"?"
    lauren "Bisakah Anda mengatakan itu lebih keras?"
    toby "Jika itu yang Anda inginkan."


    $ progress = 156
    scene expression ("images/episode12/130.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    lauren "Tidak, Anda menang!"

    label memory_39:
        if _in_replay:

            scene expression ("images/utils/black.png") with dissolve
            menu:
                "Pilih pekerjaan Anda"
                "Agen real estat":
                    $ toby_job == 0
                "Manajer klub":
                    $ toby_job == 1
        scene expression ("images/episode12/131.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode12/132.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        if emma_path:
            scene expression ("images/episode12/133.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode12/134.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()
        else:

            scene expression ("images/episode12/135.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

        scene expression ("images/episode12/136.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode12/137.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode12/138.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        lauren "Jangan khawatir, aku tidak akan menggigitnya."

        show ep12_139
        $ ui.saybehavior()
        $ ui.interact()
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck... This is so good.{/i}"
        if toby_job == 0:
            toby "Anda sangat cantik seperti ini."
        else:
            toby "Anda sangat pandai dalam hal ini. Anda harus suka mengisap penis saya karena Anda sangat baik."
        scene expression ("images/episode12/139.webp")
        hide ep12_139

        show ep12_140
        lauren "{size=12}{color=#FDCA6E}* moaning slightly *{/color}{/size}\nMhmm..."
        if toby_job == 0:
            toby "Itu sayang. Jangan berhenti."
        else:
            toby "Mengisap ayam seperti yang Anda maksudkan."
        $ ui.saybehavior()
        $ ui.interact()
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck me, this must be the best blowjob ever.{/i}"
        scene expression ("images/episode12/140.webp")
        hide ep12_140

        show ep12_141
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wonder if she can deepthroat.{/i}"
        if toby_job == 0:
            toby "Apakah Anda pikir Anda bisa memasukkan lebih banyak ke dalam mulut Anda?"
        else:
            toby "Bagaimana kalau Anda menunjukkan kepada saya betapa pelacurnya Anda dan mendalam untuk saya."
        $ ui.saybehavior()
        $ ui.interact()
        lauren "{size=12}{color=#FDCA6E}* moaning slightly *{/color}{/size}\nMhOmmKmmmAmmmY..."
        scene expression ("images/episode12/141.webp")
        hide ep12_141

        show ep12_142
        $ ui.saybehavior()
        $ ui.interact()
        if toby_job == 0:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, I can feel her throat with the tip of my cock.{/i}"
        else:
            toby "Itu sayang. Saya suka bagaimana saya bisa merasakan tenggorokan Anda."
        scene expression ("images/episode12/142.webp")
        hide ep12_142

        show ep12_143
        if toby_job == 0:
            toby "Anda yang terbaik, sayang."
        else:
            toby "Saya suka suara yang Anda buat saat penis saya mengenai tenggorokan Anda. Anda sangat seksi."
        $ ui.saybehavior()
        $ ui.interact()
        lauren "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nGgggogggogogo..."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, this feels good.{/i}"
        scene expression ("images/episode12/143.webp")
        hide ep12_143

        show ep12_144
        $ ui.saybehavior()
        $ ui.interact()
        if toby_job == 0:
            toby "Itu cukup. Saya ingin lebih."
        else:
            toby "Aku bisa membiarkanmu mengisap penisku sepanjang hari, tapi aku benar -benar ingin bercinta denganmu juga."
        scene expression ("images/episode12/144.webp")
        hide ep12_144

        scene expression ("images/episode12/145.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        lauren "Persetan aku kalau begitu."

        scene expression ("images/episode12/146.webp") with dissolve:
            xalign 0.0
            yalign 0.0
            linear 10.0 yalign 1.0 xalign 1.0

        lauren "{size=12}{color=#FDCA6E}* screaming *{/color}{/size}\n[toby!u]!"

        scene expression ("images/episode12/147_1.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        if toby_job == 0:
            toby "Aku sangat menginginkanmu sekarang."
        else:
            toby "Aku akan menidurimu begitu keras, kamu tidak akan bisa berjalan selama seminggu."

        scene expression ("images/episode12/147_2.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode12/147_3.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        if toby_job == 0:
            lauren "Bawa aku, kalau begitu."
        else:
            lauren "Persetan denganku, [toby!c]."

        scene expression ("images/episode12/147_4.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        show ep12_148
        $ ui.saybehavior()
        $ ui.interact()
        if toby_job == 0:
            toby "Vagina Anda terasa sangat enak."
            lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nThat's because it's yours."
        else:
            toby "Anda sangat ketat untuk pelacur."
            lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nThat's because I'm your slut."
        scene expression ("images/episode12/148.webp")
        hide ep12_148

        show ep12_149
        toby "Saya suka suara itu."
        $ ui.saybehavior()
        $ ui.interact()
        lauren "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nYes, [toby!c]. Fuck me. Fuck me hard!"
        lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nGive it to me. Give it to me, hard!"
        scene expression ("images/episode12/149.webp")
        hide ep12_149

        show ep12_150
        if toby_job == 0:
            lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI love feeling you inside me. Yes... Yes... "
            lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nGod YES!"
        else:
            lauren "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes, yes, yes!"
            lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck your slut. Give it to me hard."
        $ ui.saybehavior()
        $ ui.interact()
        lauren "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes, yes, yes! Don't stop!"
        scene expression ("images/episode12/150.webp")
        hide ep12_150

        show ep12_151
        lauren "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nI love it. I love feeling you inside me."
        lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYES! Fuck me [toby!c]."
        if toby_job == 0:
            toby "Anda menyukainya?"
        else:
            toby "Anda menyukainya, pelacur?"
        lauren "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes, yes, YES! I love it!"
        $ ui.saybehavior()
        $ ui.interact()
        lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI love how you fuck me."
        scene expression ("images/episode12/151.webp")
        hide ep12_151

        show ep12_152
        lauren "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nDon't stop. Fuck me. Fuck me hard!"
        lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes, yes, yes. Right there."
        $ ui.saybehavior()
        $ ui.interact()
        lauren "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nDon't stop."
        lauren "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nYes, yes, yes!"
        scene expression ("images/episode12/152.webp")
        hide ep12_152

        show ep12_153
        $ ui.saybehavior()
        $ ui.interact()
        lauren "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nI'm close. Don't stop."
        toby "Saya akan segera cum."
        lauren "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nCum inside me, please. Fill me up!"
        scene expression ("images/episode12/153.webp")
        hide ep12_153

        scene expression ("images/episode12/154.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        with flash
        with flash
        lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI'm cumming. Yes! Fuck yes."
        toby "Saya juga!"
        if toby_job == 0:
            lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFill me up [toby!c]. Fill me up with your cum."
        else:
            lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFill my cunt with your cum. Fill me up, [toby!c]."

        scene expression ("images/episode12/155.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0
        $ unlockImage(persistent.lauren_12)
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        $ unlockMemory(persistent.memory_39)
        $ renpy.end_replay()


    if emma_path:
        stop music fadeout 5.0
        scene expression ("images/episode12/156.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Who the hell is watching us?{/i}"
        scene expression ("images/episode12/157.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck my life. That's Emma.{/i}"
        scene expression ("images/episode12/158.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit, shit, shit! She saw me fuck Lauren. How could this happen?{/i}"

        menu:
            "{i} [JGR] Jalanlah setelah Emma {/i}":
                $ emma_pissed = True
                scene expression ("images/episode12/159.webp") with dissolve
                lauren "Kemana kamu pergi?"
                toby "Ummm ... aku ..."
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck! What should I tell her.{/i}"
                toby "Seseorang sedang mengawasi kami. Saya akan memastikan mereka tidak video kami."
                scene expression ("images/episode12/159_2.webp") with dissolve
                lauren "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nWhat the hell? What kind of perverts are around?"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Really [toby!c]? That's the best you could come up with?{/i}"
                toby "Kembali!"

                call episode12_emmaFight from _call_episode12_emmaFight_2

                scene expression ("images/episode12/160.webp") with fade
                lauren "Apakah semuanya baik -baik saja?"
                toby "Ya, jangan khawatir. Itu hanya teman saya. Dia melihat kami sampai di sini dan ingin mengolok -olok saya, tetapi tidak membuat film apa pun."
                lauren "Anda sudah sakit. Siapa yang mengolok -olok temannya ketika dia berhubungan seks."
                scene expression ("images/episode12/161.webp") with dissolve
                toby "Aku cukup yakin dia mengawasimu, tapi bagaimanapun, di mana kita?"
                scene expression ("images/episode12/162.webp") with dissolve
                lauren "Saya tidak tahu mengapa Anda berpakaian. Bagaimanapun, Anda menjanjikan saya sehari penuh."
                toby "Apakah saya sekarang?"
                scene expression ("images/episode12/163_1.webp") with dissolve
                lauren "Ya, Anda melakukannya. Jadi apa yang kita lakukan sekarang?"
                toby "Sekarang kami menunggu beberapa menit untuk menarik napas dan kemudian kami melanjutkan ke babak kedua."
                lauren "Sementara saya suka suara itu, saya benar -benar harus kembali ke rumah dan belajar untuk ujian yang saya miliki besok."
                toby "Apa yang terjadi sepanjang hari?"
                lauren "Seperti halnya saya menikmati itu, saya hanya mengacaukan Anda, karena saya benar -benar perlu belajar, tetapi saya tidak bisa mengatakan tidak pada tanggal ini dengan Anda."
                scene expression ("images/episode12/164_1.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode12/164_12.webp") with dissolve
                toby "Kira aku harus membawamu pulang sekarang."
                lauren "Sayangnya ya."
                toby "Oke kalau begitu. Mari kita berpakaian."

                return
            "{i} tetap dengan Lauren {/i} [JWRN11]"(csq="Jalur Emma ditutup"):

                $ emma_path = False
                $ emma_pissed = True
                scene expression ("images/episode12/163_2.webp") with dissolve
                lauren "Jadi, apa yang kita lakukan sekarang?"
    else:
        scene expression ("images/episode12/163_2.webp") with dissolve
        lauren "Jadi, apa yang kita lakukan sekarang?"

    toby "Sekarang kami menunggu beberapa menit untuk menarik napas dan kemudian kami melanjutkan ke babak kedua."
    lauren "Sementara saya suka suara itu, saya benar -benar harus kembali ke rumah dan belajar untuk ujian yang saya miliki besok."
    toby "Apa yang terjadi sepanjang hari?"
    lauren "Seperti halnya saya menikmati itu, saya hanya mengacaukan Anda, karena saya benar -benar perlu belajar, tetapi saya tidak bisa mengatakan tidak pada tanggal ini dengan Anda."
    scene expression ("images/episode12/164_2.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/164_22.webp") with dissolve
    toby "Kira aku harus membawamu pulang sekarang."
    lauren "Sayangnya ya."
    toby "Oke kalau begitu. Mari kita berpakaian."

    return

label episode12_lauren_side:
    play sound "audio/fx/notification_5.mp3"
    scene expression ("images/episode12/003_lauren.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}A message from Lauren? This is going to be interesting.{/i}"
    scene expression ("images/episode12/004_texting.webp") with dissolve
    call sms_incoming ("lauren", "Morning, sexy.", img_icon="images/episode12/100_icon.webp", img="images/episode12/100.webp") from _call_sms_incoming_256
    call sms_sent ("lauren", "Morning, sexy. How are you?") from _call_sms_sent_205
    call sms_incoming ("lauren", "Eager to see you. You haven't changed your mind, right?") from _call_sms_incoming_257
    call sms_sent ("lauren", "Nope, I haven't.") from _call_sms_sent_206
    call sms_incoming ("lauren", "So what time and where?") from _call_sms_incoming_258
    call sms_sent ("lauren", "I want you right here, right now.") from _call_sms_sent_207
    call sms_incoming ("lauren", "As much I love that idea, I don't think I'm ready to meet your [parents]. However, the \"right now\" sounds interesting.") from _call_sms_incoming_259
    call sms_sent ("lauren", "Then let's go to the coffee shop you usually go with Lisa to and get some breakfast.") from _call_sms_sent_208
    call sms_incoming ("lauren", "Sounds good. After all, we will need energy.") from _call_sms_incoming_260
    call sms_sent ("lauren", "You're crazy. You know that, right?") from _call_sms_sent_209
    call sms_incoming ("lauren", "Who? Me? I think you're exaggerating.", img_icon="images/episode12/101_icon.webp", img="images/episode12/101.webp") from _call_sms_incoming_261
    call sms_sent ("lauren", "Fuck, you're sexy.") from _call_sms_sent_210
    call sms_incoming ("lauren", "So, see you there in 30 minutes?") from _call_sms_incoming_262
    call sms_sent ("lauren", "I can come pick you up.") from _call_sms_sent_211
    call sms_incoming ("lauren", "As much as I'd love that, I don't think that's the best plan. I don't want Lisa to see us. I might be a bitch, but I still love that girl.") from _call_sms_incoming_263
    call sms_sent ("lauren", "Yeah, you're right. Let's meet there in 30 minutes then.") from _call_sms_sent_212
    call sms_incoming ("lauren", "Okay sexy. See you there.") from _call_sms_incoming_264
    call sms_sent ("lauren", "See ya.") from _call_sms_sent_213
    scene expression ("images/episode12/007.webp") with dissolve
    hide screen message
    if emma_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the fuck am I doing? Not only am I dating Emma, but I'm also dating Lisa, who I really like and now I'm going to go out with her best friend.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the fuck am I doing? I'm already dating Lisa and I really, really like her and now I'm going out with her best friend.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What if they find out about each other?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck it! I'll cross that bridge when I come to it.{/i}"
    call episode12_morningCharlotte from _call_episode12_morningCharlotte_3
    $ progress = 155
    scene expression ("images/episode12/084.webp") with fade
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/085.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I guess she's not here yet.{/i}"
    scene expression ("images/episode12/165.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Actually she is.{/i}"

    scene expression ("images/episode12/166.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()
    lauren "Pagi, seksi."
    toby "Pagi, seksi."
    scene expression ("images/episode12/167.webp") with dissolve
    toby "Apakah Anda sudah memesan?"
    lauren "Itu bukan cara yang tepat untuk menyambut saya."
    show ep12_168
    $ ui.saybehavior()
    $ ui.interact()
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This girl is really forward. I like it.{/i}"
    lauren "Tidak, saya belum memesan. Aku menunggumu."
    toby "Oh keren."
    scene expression ("images/episode12/168.webp") with dissolve
    hide ep12_168

    scene expression ("images/episode12/112.webp") with dissolve
    barista "Pagi. Apa yang bisa saya dapatkan dari Anda?"
    scene expression ("images/episode12/113.webp") with dissolve
    toby "Saya suka pancake khusus dan cappuccino."
    scene expression ("images/episode12/114.webp") with dissolve
    lauren "Tolong, hal yang sama untuk saya!"
    scene expression ("images/episode12/112.webp") with dissolve
    barista "Sempurna. Ini akan segera keluar."
    scene expression ("images/episode12/115.webp") with dissolve
    toby "Asal tahu saja, saya suka cara Anda menyapa orang. Kita harus saling menyapa lebih sering."
    lauren "Jika itu yang Anda inginkan, bagaimana saya bisa mengatakan tidak?"
    toby "Senang mendengarnya."
    scene expression ("images/episode12/116.webp") with dissolve
    lauren "Saya senang Anda setuju untuk pergi keluar dengan saya."
    toby "Sangat sulit untuk mengatakan tidak untuk ini. Bagaimanapun, kami sudah lama menggoda."
    lauren "Saya mengatakan mungkin terlalu lama."
    toby "Mungkin, tapi dengan cara ini akan lebih menarik."
    scene expression ("images/episode12/117.webp") with dissolve
    lauren "Apa yang akan lebih menarik? Seks? Ya itu bisa lebih menarik karena Anda juga meniduri sahabat saya."
    toby "Umm, Lauren ..."
    lauren "Masalah apa, sayang? Itulah kebenarannya. Setelah kami menyelesaikan sarapan kami, saya akan mengendarai Anda sampai saya mengosongkan bola Anda."
    scene expression ("images/episode12/118.webp") with dissolve
    barista "Permisi. Ini kopimu. Saya akan mengeluarkan makanan Anda dalam beberapa menit."
    toby "Tidak masalah, ma \ 'am. Terima kasih!"
    scene expression ("images/episode12/119.webp") with dissolve
    lauren "Mengapa Anda tidak memberi tahu saya bahwa dia ada di sana? Anda membiarkan saya mempermalukan diri sendiri."
    if toby_job == 0:
        toby "Saya mencoba memperingatkan Anda, tetapi Anda sangat bangga dengan betapa Anda akan mengendarai saya, saya tidak bisa mengganggu Anda."
        scene expression ("images/episode12/120_flirty.webp") with dissolve
        lauren "Saya sedikit bangga akan hal itu, bukan?"
    else:
        toby "Saya mencoba memperingatkan Anda, tetapi Anda sangat bangga dengan betapa pelacur Anda, saya tidak bisa mengganggu Anda."
        scene expression ("images/episode12/120_flirty.webp") with dissolve
        lauren "Saya seorang pelacur kecil, bukan?"

    scene expression ("images/episode12/121_laugh.webp") with dissolve
    toby "Saya tidak akan menggunakan sedikit, tapi ya."
    scene expression ("images/episode12/120_smile.webp") with dissolve
    lauren "Anda bisa tertawa sekarang, tetapi aksi yang Anda tarik hanya menghabiskan biaya seks untuk hari ini."
    scene expression ("images/episode12/121_flirty.webp") with dissolve
    toby "Lalu apa yang masih kita lakukan di sini, jika kita tidak akan berhubungan seks setelahnya?"
    scene expression ("images/episode12/120_normal.webp") with dissolve
    lauren "Bung ... aku masih punya perasaan."
    scene expression ("images/episode12/121_normal.webp") with dissolve
    toby "Maaf, saya tidak bermaksud. Saya ..."
    scene expression ("images/episode12/120_flirty.webp") with dissolve
    lauren "Saya bercanda. Lagi pula, saya masih akan menyedot ayam besar Anda."
    scene expression ("images/episode12/121_flirty.webp") with dissolve
    toby "Anda benar -benar kotor. Anda tahu itu, kan?"
    scene expression ("images/episode12/120_smile.webp") with dissolve
    lauren "Saya tidak selalu seperti ini, tetapi sekarang saya benar -benar, benar -benar gugup dan karena Anda memiliki Lisa, bagaimana lagi saya bisa membuat Anda terkesan."
    scene expression ("images/episode12/120_normal.webp") with dissolve
    lauren "Dia tampan, manis, lucu, pintar ... dan aku, aku hanya ... aku hanya lauren. Yang saya miliki hanyalah seksualitas saya."
    scene expression ("images/episode12/121_smile.webp") with dissolve
    toby "Berhentilah bersikap keras pada diri sendiri. Anda juga orang yang sangat cantik, lucu, manis, cerdas. Aku menyukaimu. Aku tidak mengajakmu kalah agar kami bisa bercinta. Saya sangat ingin mengenal Anda lebih baik."
    scene expression ("images/episode12/120_shy.webp") with dissolve
    lauren "Ya Tuhan, Lisa benar -benar memukul jackpot dengan pacar sepertimu."
    scene expression ("images/episode12/121_smile.webp") with dissolve
    toby "Terima kasih, tapi saya bukan yang terbaik, Anda tahu. Pacar yang baik tidak akan meminta sahabatnya."
    scene expression ("images/episode12/120_laugh.webp") with dissolve
    lauren "Dan sahabat baik tidak akan menerima. Jadi kita berdua orang jahat?"
    scene expression ("images/episode12/121_smile.webp") with dissolve
    toby "Agak. Tapi cukup tentang Lisa. Ceritakan lebih banyak tentang diri Anda."
    scene expression ("images/episode12/120_curious.webp") with dissolve
    lauren "Apa yang ingin Anda ketahui?"
    scene expression ("images/episode12/121_curious.webp") with dissolve
    toby "Aku tidak tahu. Apakah Anda punya hobi?"
    scene expression ("images/episode12/120_normal.webp") with dissolve
    lauren "Nah, Anda sudah tahu bahwa saya suka menari, tetapi apa yang mungkin tidak Anda ketahui, adalah kenyataan bahwa saya benar -benar menikmati tarian eksotis."
    scene expression ("images/episode12/121_curious.webp") with dissolve
    toby "Dengan tarian eksotis yang Anda maksud tarian tiang, atau saya tidak tahu apa -apa tentang menari dan sekarang saya terdengar seperti cabul?"
    scene expression ("images/episode12/120_surprised.webp") with dissolve
    lauren "Anda adalah orang cabul. Anda benar -benar berpikir saya akan menikmati tarian tiang?"
    scene expression ("images/episode12/121_laugh.webp") with dissolve
    toby "Saya agak berharap Anda akan melakukannya."
    scene expression ("images/episode12/120_laugh.webp") with dissolve
    lauren "Kalau begitu, Anda beruntung, karena itulah yang saya bicarakan. Saya telah mengambil beberapa kelas belakangan ini."
    scene expression ("images/episode12/121_curious.webp") with dissolve
    toby "Dan bagaimana saya beruntung?"
    scene expression ("images/episode12/121_flirty.webp") with dissolve
    toby "Oh, Anda akan tampil untuk saya."
    scene expression ("images/episode12/120_flirty.webp") with dissolve
    lauren "Anda seperti itu, tidakkah Anda?"
    scene expression ("images/episode12/121_laugh.webp") with dissolve
    toby "Pria waras apa yang tidak akan?"
    scene expression ("images/episode12/120_smile.webp") with dissolve
    lauren "Cukup tentang itu atau Anda mungkin berakhir dengan kesalahan dan kami tidak memiliki cara untuk menghadapinya di sini."
    scene expression ("images/episode12/121_laugh.webp") with dissolve
    toby "Apakah Anda yakin kami tidak?"
    scene expression ("images/episode12/122.webp") with dissolve
    lauren "Yah, saya bisa masuk ke bawah meja dan mengambil penis besar Anda di mulut saya dan menyedotnya sangat, sangat keras."
    scene expression ("images/episode12/123.webp") with dissolve
    barista "Permisi. Ini makananmu."
    toby "Terima kasih Ma \ 'Am."
    barista "Menikmati!"
    scene expression ("images/episode12/124.webp") with dissolve
    lauren "Anda bajingan! Anda membiarkan saya melakukannya lagi. Apa yang akan dipikirkan wanita ini tentang saya?"
    toby "Dia akan mengira Anda seorang gadis yang sangat nakal."
    lauren "Persetan denganmu, [toby!c]."
    toby "Segera, sayang. Segera!"
    scene expression ("images/episode12/125.webp") with dissolve
    lauren "Tidak. Aku hampir memaafkanmu untuk pertama kalinya. Lagi pula, Anda memang mencoba memperingatkan saya. Tapi kali ini Anda melakukannya dengan sengaja."
    scene expression ("images/episode12/126.webp") with dissolve
    toby "Itu artinya saya tidak mendapatkan blowjob saya yang dijanjikan?"
    lauren "Menurut Anda, seperti apa saya? Tentu saja Anda mengerti. Lagi pula, saya ingin mengisap kemaluan Anda, tapi hanya itu yang Anda dapatkan hari ini."
    toby "Bon Appetit kalau begitu."
    lauren "Apakah itu untuk blowjob, atau makanan?"
    toby "Keduanya."
    lauren "Terima kasih!"
    scene expression ("images/episode12/127.webp") with fade
    toby "Itu sangat bagus."
    lauren "Ya. Saya tidak tahu mengapa saya belum sarapan di sini sebelumnya."
    toby "Saya harus pergi membayar dan kemudian keluar. Ada motel tepat di sudut."
    label memory_40:

        $ progress = 156
        scene expression ("images/episode12/169.webp") with dissolve
        lauren "Jangan pergi dulu."
        toby "Mengapa tidak? Mendapatkan Kaki Dingin?"
        scene expression ("images/episode12/170.webp") with dissolve
        lauren "Sebenarnya, ya! Anda bisa merasakan betapa dinginnya kaki saya."
        toby "Anda gila. Anda tahu itu, kan?"
        scene expression ("images/episode12/171.webp") with dissolve
        lauren "Aku tahu."
        toby "Fuck. Saya mendapatkan kesalahan besar sekarang."
        lauren "Saya bisa merasakannya."
        scene expression ("images/episode12/172.webp") with dissolve
        lauren "Dan sekarang Anda bisa membayar."
        toby "Aku tidak akan pergi ke sana dengan boner."
        scene expression ("images/episode12/173.webp") with dissolve
        lauren "Saya pergi. Jika Anda tidak di luar dalam satu menit, saya akan pulang."

        scene expression ("images/episode12/174.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck... This woman is crazy.{/i}"

        scene expression ("images/episode12/175.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}How the fuck am I going to pay like this.{/i}"

        scene expression ("images/episode12/176.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Please, please, please don't look down.{/i}"

        scene expression ("images/episode12/177.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck! She noticed.{/i}"

        scene expression ("images/episode12/178.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm so gonna get you for that.{/i}"

        scene expression ("images/episode12/132.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        if emma_path:
            scene expression ("images/episode12/133.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode12/134.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()
        else:


            scene expression ("images/episode12/135.webp") with dissolve:
                xalign 0.0
                linear 10.0 xalign 1.0

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

        scene expression ("images/episode12/136.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode12/137.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode12/138.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        show ep12_139
        $ ui.saybehavior()
        $ ui.interact()
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck... This is so good.{/i}"
        if toby_job == 0:
            toby "Anda sangat cantik seperti ini."
        else:
            toby "Anda sangat pandai dalam hal ini. Anda harus suka mengisap penis saya karena Anda sebagus ini."
        scene expression ("images/episode12/139.webp")
        hide ep12_139

        show ep12_140
        lauren "{size=12}{color=#FDCA6E}* moaning slightly *{/color}{/size}\nMhmm..."
        if toby_job == 0:
            toby "Itu sayang. Jangan berhenti."
        else:
            toby "Mengisap ayam seperti yang Anda maksudkan."
        $ ui.saybehavior()
        $ ui.interact()
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck me, this might be the best blowjob ever. She could teach Lisa a thing or two.{/i}"
        scene expression ("images/episode12/140.webp")
        hide ep12_140

        show ep12_141
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wonder if she can deepthroat?{/i}"
        if toby_job == 0:
            toby "Apakah Anda pikir Anda bisa memasukkan lebih banyak ke dalam mulut Anda?"
        else:
            toby "Bagaimana kalau Anda menunjukkan kepada saya betapa pelacurnya Anda dan mendalam saya."
        $ ui.saybehavior()
        $ ui.interact()
        lauren "{size=12}{color=#FDCA6E}* moaning slightly *{/color}{/size}\nMhOmmKmmmAmmmY..."
        scene expression ("images/episode12/141.webp")
        hide ep12_141

        show ep12_142
        $ ui.saybehavior()
        $ ui.interact()
        if toby_job == 0:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, I can feel her throat with the tip of my cock.{/i}"
        else:
            toby "Itu sayang. Saya suka bagaimana saya bisa merasakan tenggorokan Anda."
        scene expression ("images/episode12/142.webp")
        hide ep12_142

        show ep12_143
        if toby_job == 0:
            toby "Anda yang terbaik, sayang."
        else:
            toby "Saya suka suara yang Anda buat saat penis saya mengenai tenggorokan Anda. Anda sangat seksi."
        $ ui.saybehavior()
        $ ui.interact()
        lauren "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nGgggogggogogo..."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, this feels good.{/i}"
        scene expression ("images/episode12/143.webp")
        hide ep12_143

        show ep12_144
        $ ui.saybehavior()
        $ ui.interact()
        toby "Saya akan pergi ke cum."
        scene expression ("images/episode12/144.webp")
        hide ep12_144

        show ep12_179
        if toby_job == 0:
            lauren "Cum di wajahku, sayang."
        else:
            lauren "Cum di wajahku, sayang. Aku pelacurmu. Tutupi wajah saya dengan air mani Anda."
        scene expression ("images/episode12/179.webp")
        hide ep12_179

        scene expression ("images/episode12/180.webp") with dissolve:
            xalign 0.0
            yalign 1.0
            linear 10.0 xalign 1.0 yalign 0.0

        with flash
        with flash
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode12/181.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        toby "Itu mungkin saja blowjob terbaik yang pernah saya miliki."
        lauren "Saya sangat senang Anda menikmatinya. Saya mencoba yang terbaik untuk membuat Anda terkesan."
        $ unlockImage(persistent.lauren_13)
        $ unlockMemory(persistent.memory_40)
        $ renpy.end_replay()


    if emma_path:

        stop music fadeout 5.0
        scene expression ("images/episode12/156.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Who the hell is watching us?{/i}"
        scene expression ("images/episode12/157.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck my life. That's Emma.{/i}"
        scene expression ("images/episode12/158.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit, shit, shit! She saw us. How could this happen?{/i}"

        menu:
            "{i} [JGR] Jalanlah setelah Emma {/i}":
                $ emma_pissed = True
                scene expression ("images/episode12/182.webp") with dissolve
                lauren "Kemana kamu pergi?"
                toby "Ummm ... aku ..."
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck! What should I tell her.{/i}"
                toby "Saya pikir seorang teman Lisa melihat kami."
                scene expression ("images/episode12/183.webp") with dissolve
                lauren "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nWhat the hell? Fuck!"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Really [toby!c]? That's the best you could come up with?{/i}"
                toby "Kembali!"

                call episode12_emmaFight from _call_episode12_emmaFight_3

                scene expression ("images/episode12/184.webp") with fade
                lauren "Apakah semuanya baik -baik saja?"
                toby "Ya, jangan khawatir. Dia berjanji untuk tidak memberi tahu jiwa."
                lauren "Dan apakah Anda mempercayainya?"
                scene expression ("images/episode12/185.webp") with dissolve
                toby "Yah saya memberinya 100 alasan untuk tidak memberi tahu."
                lauren "Saya minta maaf untuk itu."
                toby "Ini baik -baik saja. Aku benar -benar menikmati menghabiskan waktu bersamamu."
                lauren "Ya, saya juga."
                scene expression ("images/episode12/186.webp") with dissolve
                lauren "Bagaimanapun. Seperti halnya aku ingin tinggal bersamamu, aku harus kembali ke rumah. Saya punya ujian besok."
                toby "Aku akan membawamu pulang."

                return
            "{i} tetap dengan Lauren {/i} [JWRN11]"(csq="Jalur Emma ditutup"):

                $ renpy.notify("Emma's path has been closed!")
                $ emma_path = False
                $ emma_pissed = True
                pass
    else:


        pass

    scene expression ("images/episode12/187_1.webp") with dissolve
    toby "Ya Tuhan, kamu cantik."
    scene expression ("images/episode12/187_2.webp") with dissolve
    lauren "Terima kasih."
    scene expression ("images/episode12/187_3.webp") with dissolve
    lauren "Bagaimanapun. Seperti halnya aku ingin tinggal bersamamu, aku harus kembali ke rumah. Saya punya ujian besok."
    toby "Aku akan membawamu pulang."

    return

label episode12_morningCharlotte:
    show screen ui_message("20 minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/008.webp")
    hide screen ui_message

    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/009.webp") with dissolve
    charlotte "Pagi, sayang."
    scene expression ("images/episode12/010.webp") with dissolve
    toby "Pagi, [mom]."
    scene expression ("images/episode12/009.webp") with dissolve
    charlotte "Di mana Anda akan terburu -buru ini pagi -pagi sekali?"
    scene expression ("images/episode12/010.webp") with dissolve
    toby "Oh, aku hanya pergi keluar dengan seorang teman."
    if emma_path:
        scene expression ("images/episode12/009.webp") with dissolve
        charlotte "Sapa Emma dariku."
    else:
        scene expression ("images/episode12/009.webp") with dissolve
        charlotte "Seorang teman yang Anda katakan? Pastikan Anda tidak membuatnya hamil."

    scene expression ("images/episode12/011.webp") with dissolve
    toby "Selamat tinggal, [mom]!"

    return

label episode12_emmaFight:
    $ progress = 157
    scene expression ("images/episode12/188.webp") with fade
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode12/189.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nEmma, wait! We need to talk."
    scene expression ("images/episode12/190.webp") with dissolve
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nWe have nothing to talk about. I don't want to talk to you ever again."
    scene expression ("images/episode12/191.webp") with dissolve
    toby "Berhenti berlari dan biarkan bicara."
    scene expression ("images/episode12/192.webp") with dissolve
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nWhat is there to talk about?"
    scene expression ("images/episode12/194.webp") with dissolve
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nYou're cheating on me! I hate you!"
    scene expression ("images/episode12/193.webp") with dissolve
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nI fucking gave you everything!"
    scene expression ("images/episode12/194.webp") with dissolve
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nI gave you everything you wanted. I never said no!"
    scene expression ("images/episode12/193.webp") with dissolve
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nYou fucking broke my heart! I loved you like crazy. I would have done anything for you!"
    scene expression ("images/episode12/194.webp") with dissolve
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nI hate you! I hate everything. I hate this fucking city. I moved here for you. I came here for you!"
    scene expression ("images/episode12/193.webp") with dissolve
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nI came here because I loved you. All I did, I did for us, because I wanted to have a future together."
    scene expression ("images/episode12/194.webp") with dissolve
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nAnd you? You don't give a fuck about me! You don't call me, you don't spend time with me. I'm done making excuses for you."
    scene expression ("images/episode12/193.webp") with dissolve
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nI was lying to myself. \"He's busy with the work\", \"he's just more mature\", \"he fucking loves me\". Tebak apa?"
    scene expression ("images/episode12/194.webp") with dissolve
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nYou don't fucking love me! You only fucking love yourself. You love being loved, but you don't give anything back."
    scene expression ("images/episode12/193.webp") with dissolve
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nI gave you everything. I fucking gave you my virginity! I gave you my whole heart and you fucking tore it apart."
    scene expression ("images/episode12/194.webp") with dissolve
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nWhat does she have that I don't?"
    scene expression ("images/episode12/195.webp") with dissolve
    toby "Tolong berhenti memukul saya. Lihat. Saya minta maaf, saya tidak bermaksud menyakitimu."
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nNo. You didn't mean to get caught! You don't care about me."
    toby "Itu kecelakaan."
    scene expression ("images/episode12/196.webp") with dissolve
    if lisa_path:
        if lauren_sidePath:
            emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nAn accident? Are you stupid or something? She accidentally fell with her mouth on your cock?"
        else:
            emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nAn accident? Are you stupid or something? What? You accidentally slipped and fell with your cock in her pussy?"
    else:
        if lisa_sidePath:
            emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nAn accident? Are you stupid or something? What? You accidentally fell with your tongue in her mouth."
        else:
            emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nAn accident? Are you stupid or something? What? You accidentally slipped and fell with your cock in her pussy?"
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nThe accident was me stumbling in on you. Yeah. That's what the accident was."
    toby "Tolong, berhentilah berteriak."
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nWhy should I? Are you ashamed that people might find out what a fucking bastard you are?"
    toby "Itu tidak ada artinya. Dia tidak berarti apa -apa bagiku, karena aku hanya mencintaimu."
    scene expression ("images/episode12/197.webp") with dissolve
    emma "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nLove? You don't even know what love is. What you feel is selfish love. You love only yourself. You love feeling good. You love using stupid girls like me!"
    emma "Anda menyukai seks dan itu semua. Anda akan melakukan apapun untuk mendapatkan vagina di kontol bodoh Anda."
    scene expression ("images/episode12/198.webp") with dissolve
    emma "Aku membencimu, [toby!c]. Aku sangat membenci semua yang kamu perjuangkan."
    toby "Tolong, tolong dengarkan aku."
    scene expression ("images/episode12/199.webp") with dissolve
    emma "Tolong tinggalkan aku sendiri. Aku membencimu."
    toby "Saya minta maaf."
    emma "Aku sangat membencimu."
    toby "Dan aku mencintaimu."
    emma "Aku benci aku mencintaimu, tapi kamu ... kamu tidak mencintaiku. Jika Anda melakukannya, maka Anda tidak akan melakukannya."
    scene expression ("images/episode12/200.webp") with dissolve
    emma "Kenapa, [toby!c]? Mengapa Anda melakukannya? Apa yang dia miliki yang saya tidak?"
    emma "Anda suka gadis dengan bibir besar, jadi saya memperbaikinya. Anda menyukai payudara besar, dan saya mendapat pekerjaan payudara. Saya melihat bagaimana Anda memandang gadis -gadis dengan rambut pendek, jadi saya memotongnya juga. Apa lagi yang perlu saya ubah agar Anda menyukai saya?"
    toby "Jangan ubah apapun. Anda sempurna apa adanya."
    emma "Namun, saya tidak cukup baik untuk Anda."
    scene expression ("images/episode12/201.webp") with dissolve
    toby "Tapi kamu."
    emma "Tolong, [toby!c]. Biarkan aku pergi. Saya ingin pulang."
    scene expression ("images/episode12/202.webp") with dissolve
    toby "Bisakah saya menelepon Anda nanti?"
    emma "Tolong jangan tidak. Saya benar -benar tidak ingin berbicara dengan Anda sekarang."
    toby "Aku mencintaimu."
    emma "Tolong berhenti mengatakan itu, karena itu tidak benar. Anda menghancurkan hati saya."
    scene expression ("images/episode12/203.webp") with dissolve
    emma "Perpisahan, [toby!c]."
    scene expression ("images/episode12/204.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I fucked up big time. Fuck, fuck, fuck!{/i}"

    scene expression ("images/episode12/205.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I lost Emma. God, how could have I been this stupid?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, fuck, fuck!{/i}"

    if lisa_path:
        if lauren_sidePath:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should get back to Lauren. She might get worried because of my stupid lie.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'll just tell her I paid her $100 not to tell Lisa. Fuck!{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yeah, I'll do that, because lying has worked out well so far.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm so stupid. I was so focused on hiding from Lisa, that I forgot about Emma.{/i}"
        else:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, Lisa! I should get back to her. I must have scared her with that stupid lie.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'll just tell her that a friend of mine saw us and wanted to prank me.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yeah, I'll do that, because lying has worked out well so far.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck! I'm so stupid. How could I be so careless?{/i}"
    else:
        if lisa_sidePath:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck! Fuck, fuck! I was so focused on hiding from Lauren that I forgot about Emma.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}How could I be so careless?{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should just go home.{/i}"
        else:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit! Lauren. I forgot about her. What am I going to tell her? She might be scared thinking that someone filmed us having sex.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the fuck was with that lie? Am I stupid or what?{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm just going to tell her that a friend of mine wanted to pull a prank on me.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yeah, I'll do that, because lying has worked out well so far.{/i}"

    return


label episode12_backFromDate:
    $ progress = 158
    scene expression ("images/episode12/206.webp") with fade
    if emma_pissed:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Back home! I should try to give Emma a call.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}That date was really nice, actually. I'm glad I asked her out.{/i}"
    scene expression ("images/episode12/207.webp") with dissolve
    if emma_pissed:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Interesting. Nobody is here. I'll try to call Emma then.{/i}"
        scene expression ("images/episode12/208.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She turned off her phone. Fuck!{/i}"
        scene expression ("images/episode12/209.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wonder where everybody is.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Interesting. No one is here. Where is everyone?{/i}"


    scene expression ("images/episode12/210.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Looks like [mom] and Tris are enjoying the hot tub.{/i}"
    scene expression ("images/episode12/213.webp") with dissolve
    if emma_pissed:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe relaxing in the hot tub will help get my mind off Emma.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should go join them.{/i}"

    return


label episode12_alone:
    $ progress = 158
    scene expression ("images/episode12/001.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* reading *{/color}{/size}\n{i}\"Eye contact is important. On a first date you are trying to read each other and human beings are notoriously bad at reading facial expressions of strangers.\"{/i}"
    toby "{size=12}{color=#FDCA6E}* reading *{/color}{/size}\n{i}\"Shifty eye contact or too much eye contact can make it difficult for people to trust you and figuring out the middle ground is helpful in both dating and business.\"{/i}"
    scene expression ("images/episode12/002.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}God, my life is depressing. I've been reading this book all morning.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wonder what everyone is doing.{/i}"
    scene expression ("images/episode12/211.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmm, where is everyone?{/i}"
    scene expression ("images/episode12/212.webp") with dissolve

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Looks like [mom] and Tris are having fun in the hot tub.{/i}"
    scene expression ("images/episode12/213.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should join them. I didn't work on that yard 2 months just so they could have fun without me.{/i}"
    return


label episode12_trisCharlotte_yard:
    scene expression ("images/episode12/214.webp") with dissolve
    toby "Halo, perempuan!"

    if ep12_girlsDate:
        scene expression ("images/episode12/215.webp") with dissolve
        charlotte "Hei, Casanova. Bagaimana tanggal Anda?"
        if patricia_path:
            scene expression ("images/episode12/216.webp") with dissolve
            patricia "Anda berkencan, koboi?"
            scene expression ("images/episode12/218_0.webp") with dissolve
            if emma_pissed:
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Tris seems a little upset. Shit! I can't deal with any more drama today.{/i}"
            else:
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Tris seems a little upset.{/i}"
            scene expression ("images/episode12/218.webp") with dissolve
            toby "Apa? Anda sedang bermain asosiasi kata?"
            scene expression ("images/episode12/219.webp") with dissolve
            patricia "Ya, [mom] ... kita bisa memainkan asosiasi kata."
            charlotte "Tidak, Tris kami tidak bisa!"
            patricia "Bagus!"
            scene expression ("images/episode12/220_0.webp") with dissolve
            patricia "Jadi? Bagaimana?"
            scene expression ("images/episode12/220_2.webp") with dissolve
            toby "Yah, itu tidak ada yang istimewa. Saya benar -benar tidak ingin membicarakannya. Apa yang kalian berdua lakukan?"
        else:
            scene expression ("images/episode12/217.webp") with dissolve
            patricia "Anda sedang berkencan? Jadi? Bagaimana kabarmu, koboi?"
            scene expression ("images/episode12/218.webp") with dissolve
            toby "Apa? Anda sedang bermain asosiasi kata?"
            scene expression ("images/episode12/219.webp") with dissolve
            patricia "Ya, [mom] ... kita bisa memainkan asosiasi kata."
            charlotte "Tidak, Tris kami tidak bisa!"
            patricia "Bagus!"
            scene expression ("images/episode12/220_1.webp") with dissolve
            patricia "Jadi? Bagaimana?"
            scene expression ("images/episode12/220_2.webp") with dissolve
            toby "Tidak apa -apa, kurasa. Bagaimanapun. Apa yang kalian berdua lakukan?"
    else:
        scene expression ("images/episode12/215.webp") with dissolve
        charlotte "Halo, sayang. Anda akhirnya memutuskan untuk meninggalkan kamar Anda?"
        scene expression ("images/episode12/217.webp") with dissolve
        patricia "Kamu di rumah, sayang?"
        scene expression ("images/episode12/218.webp") with dissolve
        toby "Apa? Anda sedang bermain asosiasi kata?"
        scene expression ("images/episode12/219.webp") with dissolve
        patricia "Ya, [mom] ... kita bisa memainkan asosiasi kata."
        charlotte "Tidak, Tris kami tidak bisa!"
        patricia "Bagus!"
        scene expression ("images/episode12/220_2.webp") with dissolve
        toby "Bagaimanapun. Apa yang kalian berdua lakukan?"

    scene expression ("images/episode12/221_normal_3.webp") with dissolve
    charlotte "Tris di sini, menyebut saya membosankan karena saya tidak ingin bermain game apa pun dengannya. Dia tidak mengerti bahwa saya suka berada di bak mandi air panas untuk bersantai."
    scene expression ("images/episode12/222_normal_1.webp") with dissolve
    patricia "Kami sudah duduk di bak mandi air panas selama satu jam dan yang kami lakukan adalah gosip."
    scene expression ("images/episode12/223_laugh_1.webp") with dissolve
    toby "That's very not nice, [mom]. What happened to, \"I never want to hear you gossip. You're better than that.\"?"
    scene expression ("images/episode12/222_laugh_1.webp") with dissolve
    patricia "Ya, [mom]. Apa yang terjadi dengan semua itu?"
    scene expression ("images/episode12/221_normal_2.webp") with dissolve
    charlotte "Jangan berani -berani, wanita muda. Anda sama bersalahnya dengan saya."
    scene expression ("images/episode12/221_smile_3.webp") with dissolve
    charlotte "I don't think \"gossip\"adalah kata yang tepat. Kami hanya berbicara tentang orang yang berbeda. Misalnya, kami berbicara tentang bagaimana [aunt] Anda akan berkunjung lagi pada hari Selasa."
    charlotte "Melihat? Tidak bergosip."
    scene expression ("images/episode12/222_smile_3.webp") with dissolve
    patricia "Yeah, our \"slutty [aunt]\". The one who \"likes to show her abdomen and small boobies\"."
    scene expression ("images/episode12/223_laugh_1.webp") with dissolve
    toby "Ya. Itu tidak terdengar seperti gosip sama sekali."
    scene expression ("images/episode12/221_normal_3.webp") with dissolve
    charlotte "Hai! Dia bilang aku gemuk."
    scene expression ("images/episode12/222_normal_1.webp") with dissolve
    patricia "Dan Anda mengatakan dia memiliki payudara kecil, yang membiarkan jujur, sebenarnya ukuran yang sempurna untuk seorang wanita yang belum punya anak."
    scene expression ("images/episode12/223_normal_1.webp") with dissolve
    toby "Ya, saya pikir dia benar. Dia memang memiliki payudara berukuran layak."
    scene expression ("images/episode12/221_surprised_3.webp") with dissolve
    charlotte "[toby!c]. Pernahkah Anda melihat dada [aunt] Anda?"
    scene expression ("images/episode12/222_laugh_3.webp") with dissolve
    patricia "Seseorang nakal."
    scene expression ("images/episode12/223_normal_1.webp") with dissolve
    toby "Tidak, saya belum."
    scene expression ("images/episode12/222_flirty_3.webp") with dissolve
    patricia "Nakal, nakal!"
    scene expression ("images/episode12/223_attention_2.webp") with dissolve
    toby "Saya belum. Hanya saja dia terlihat bagus. Saya hanya memperhatikan."
    if patricia_path:
        scene expression ("images/episode12/222_flirty_3.webp") with dissolve
        patricia "Nakal, nakal, [brother]. Jangan tahu itu tidak baik untuk merpati pada anggota [family] Anda."
    else:
        scene expression ("images/episode12/222_laugh_3.webp") with dissolve
        patricia "Kamu sakit, sakit. Jangan tahu itu tidak baik untuk merpati pada anggota [family] Anda."
    scene expression ("images/episode12/223_smile_2.webp") with dissolve
    toby "Pertama -tama, saya tidak melakukan apa pun pada siapa pun."
    scene expression ("images/episode12/221_laugh_3.webp") with dissolve
    charlotte "Tidak mungkin Anda bisa keluar dari ini sekarang. Anda telah memasuki ruang singa."
    scene expression ("images/episode12/222_curious_3.webp") with dissolve
    patricia "Jadi menurut Anda siapa yang lebih tampan? [mom!c] atau [aunt] Denise?"
    scene expression ("images/episode12/223_smile_2.webp") with dissolve
    toby "Saya tidak akan memberi Anda kepuasan."
    scene expression ("images/episode12/221_normal_3.webp") with dissolve
    charlotte "Ya, [toby!c]. Menurut Anda, siapa yang terlihat lebih baik? Saya atau [aunt] Denise."
    scene expression ("images/episode12/223_laugh_1.webp") with dissolve
    toby "Saya tidak akan menjawab. Seperti yang Anda katakan, saya memasuki sarang singa. Saya tidak akan lebih dalam di gua."
    scene expression ("images/episode12/221_sad_3.webp") with dissolve
    charlotte "Jadi Anda pikir dia terlihat lebih baik. Senang mengetahui bahwa bahkan satu -satunya [son] saya berpikir saya cantik."
    scene expression ("images/episode12/222_normal_3.webp") with dissolve
    patricia "Bagaimana Anda mengatakan sesuatu seperti itu? Anda sangat buruk [son]."
    scene expression ("images/episode12/223_normal_2.webp") with dissolve
    toby "Anda tahu apa? Kalian berdua adalah yang terburuk. Seperti [mother] seperti [daughter]. Saya tidak berpikir ini adalah sarang singa. Saya pikir saya dikelilingi oleh hyena."
    scene expression ("images/episode12/221_laugh_3.webp") with dissolve
    charlotte "Bisa aja. Anda terlalu banyak menonton kartun."
    scene expression ("images/episode12/222_curious_3.webp") with dissolve
    patricia "Jadi? Jawaban Akhir?"
    if charlotte_path:
        scene expression ("images/episode12/223_smile_2.webp") with dissolve
        toby "Ya, saya pikir [mom] terlihat jauh lebih baik. Saya benar -benar berpikir begitu. Dia wanita terpanas di sekitar dan aku beruntung memiliki istri seindah dan seksi [mom] suatu hari nanti."
        scene expression ("images/episode12/221_surprised_3.webp") with dissolve
        charlotte "..."
        scene expression ("images/episode12/223_smile_1.webp") with dissolve
        toby "Ya, [mom]. Anda adalah wanita tercantik yang pernah saya lihat. Anda cantik. Ada sesuatu tentang Anda yang tidak dimiliki banyak wanita. Anda memiliki pesona yang hanya dimiliki seorang wanita dengan kelas."
        scene expression ("images/episode12/222_surprised_3.webp") with dissolve
        patricia "Sekarang saya benar -benar berpikir Anda sedikit sakit, tetapi saya harus setuju dengan Anda tentang itu."
        scene expression ("images/episode12/222_laugh_3.webp") with dissolve
        patricia "Tapi Anda masih sakit."
        scene expression ("images/episode12/224.webp") with dissolve
        toby "Itu sudah cukup. Saya meninggalkan sarang hyena."
    else:
        scene expression ("images/episode12/224.webp") with dissolve
        toby "Itu sudah cukup. Saya meninggalkan sarang hyena."

    scene expression ("images/episode12/222_laugh_3.webp") with dissolve
    patricia "Tunggu, jangan pergi. Saya berjanji saya tidak akan menggoda Anda lagi."
    scene expression ("images/episode12/221_smile_3.webp") with dissolve
    charlotte "Saya juga."
    scene expression ("images/episode12/223_smile_1.webp") with dissolve
    toby "Terima kasih!"
    scene expression ("images/episode12/223_smile_2.webp") with dissolve
    toby "Jadi game apa yang ingin kamu mainkan?"
    scene expression ("images/episode12/221_laugh_3.webp") with dissolve
    charlotte "\"I spy with my little eye\"."
    scene expression ("images/episode12/223_laugh_2.webp") with dissolve
    toby "Ayo, Tris. Itu adalah permainan anak -anak."
    scene expression ("images/episode12/222_ashamed.webp") with dissolve
    patricia "Saya memiliki momen kelemahan."
    scene expression ("images/episode12/222_smile_3.webp") with dissolve
    patricia "Tapi Anda memberi saya ide yang lebih baik. Biarkan Asosiasi Word Play."
    scene expression ("images/episode12/221_relax.webp") with dissolve
    charlotte "Oke anak -anak, Anda bersenang -senang. Saya akan menikmati bak mandi air panas."
    scene expression ("images/episode12/223_normal_2.webp") with dissolve
    toby "Nah, jika [mom] tidak bermain, saya juga tidak bermain. Ini semakin tua mengalahkanmu."
    scene expression ("images/episode12/222_surprised_3.webp") with dissolve
    patricia "Kamu apa? Apa yang kamu katakan? Apakah Anda pikir Anda bisa mengalahkan saya?"
    scene expression ("images/episode12/222_angry_3.webp") with dissolve
    patricia "Nak konyol, saya menemukan game ini!"
    scene expression ("images/episode12/223_relax.webp") with dissolve
    toby "Sayang sekali Anda tidak dapat membuktikannya. Saya akan santai seperti [mom]."
    scene expression ("images/episode12/222_sad_1.webp") with dissolve
    patricia "Ayo, [mom]. Bermain dengan kami. Bantu saya mengajarkan ini [son] pelajaran Anda."
    scene expression ("images/episode12/223_laugh_2.webp") with dissolve
    toby "Semoga berhasil dengan itu."
    scene expression ("images/episode12/221_smile_2.webp") with dissolve
    charlotte "Anda berjanji untuk tidak kalah?"
    scene expression ("images/episode12/222_laugh_1.webp") with dissolve
    patricia "Janji kelingking."
    scene expression ("images/episode12/223_smile_2.webp") with dissolve
    toby "Semoga berhasil dengan itu juga."
    scene expression ("images/episode12/221_laugh_2.webp") with dissolve
    charlotte "Mari kita ajari dia pelajaran. Dia menjadi terlalu sombong untuk kebaikannya sendiri."
    scene expression ("images/episode12/222_smile_1.webp") with dissolve
    patricia "Kami akan mengajarinya pelajaran, baik -baik saja. Mari kita tunjukkan kepadanya bahwa dia tidak bisa mengacaukan para wanita di rumah ini."
    scene expression ("images/episode12/223_laugh_2.webp") with dissolve
    toby "Anda menyadari bahwa game ini tidak dimaksudkan untuk dimainkan dengan tim, bukan?"
    scene expression ("images/episode12/221_normal_3.webp") with dissolve
    charlotte "Tidak ada yang bekerja sama dengan siapa pun."
    scene expression ("images/episode12/222_smile_3.webp") with dissolve
    patricia "Biarkan bermain."
    scene expression ("images/episode12/223_smile_2.webp") with dissolve
    toby "Ini pemakaman Anda."
    $ progress = 159
    if patricia_path and charlotte_path:
        $ ep12_stripWordAssociation = True

        scene expression ("images/episode12/222_normal_3.webp") with dissolve
        patricia "Oh ya? Mari kita buat sedikit taruhan."
        scene expression ("images/episode12/223_curious_2.webp") with dissolve
        toby "Taruhan apa?"
        scene expression ("images/episode12/222_normal_3.webp") with dissolve
        patricia "Yang kalah harus memberikan 0 kepada dua lainnya."
        scene expression ("images/episode12/223_smile_2.webp") with dissolve
        toby "Kesepakatan."
        scene expression ("images/episode12/221_normal_3.webp") with dissolve
        charlotte "Jika Anda mau, Anda dapat bermain untuk tantangan atau hukuman.Tidak ada kesepakatan. Anda tidak memainkan permainan bodoh ini untuk mendapatkan uang. Saya tidak membiarkan Anda membuang uang."
        scene expression ("images/episode12/223_flirty_1.webp") with dissolve
        toby "Yang kalah harus menghapus artikel pakaian."
        scene expression ("images/episode12/221_surprised_3.webp") with dissolve
        charlotte "[toby!c]!"
        scene expression ("images/episode12/222_laugh_1.webp") with dissolve
        patricia "Apa? Apakah Anda takut, [mom]?"
        scene expression ("images/episode12/221_normal_2.webp") with dissolve
        charlotte "Aku tidak takut, sayang. Anda orang yang seharusnya takut. Anda selalu kalah di game ini."
        scene expression ("images/episode12/222_smile_1.webp") with dissolve
        patricia "Tapi aku tidak seburuk dulu. Selain itu, sekarang saya di perguruan tinggi, tidak seperti orang lain, saya tahu lebih banyak kata. Satu -satunya yang seharusnya takut adalah [toby!c]. Dia hanya memiliki satu barang pakaian."
        scene expression ("images/episode12/223_smile_2.webp") with dissolve
        toby "Jangan menyodok beruang itu."
        scene expression ("images/episode12/222_laugh_3.webp") with dissolve
        patricia "Saya tahu Anda ingin terdengar pintar, tetapi Anda tidak sepintar yang Anda pikirkan, tuan."
        scene expression ("images/episode12/221_drink.webp") with dissolve
        charlotte "Saya tidak percaya saya membiarkan Anda membujuk saya untuk ini. Saya akan membutuhkan minuman untuk ini. Atau dua."
        $ unlockImage(persistent.charlotte_tris_01)

    scene expression ("images/episode12/222_cool_3.webp") with dissolve
    patricia "Anda akan turun, tuan!"
    scene expression ("images/episode12/223_normal_2.webp") with dissolve
    toby "Saya memberi Anda satu kesempatan lagi untuk berubah pikiran."
    scene expression ("images/episode12/222_cool_3.webp") with dissolve
    patricia "Bawalah, sayang!"
    scene expression ("images/episode12/223_smile_2.webp") with dissolve
    toby "Saya akan memberi Anda keuntungan. Kamu pergi dulu!"
    scene expression ("images/episode12/222_smile_3.webp") with dissolve
    patricia "Ini pemakaman Anda."
    scene expression ("images/episode12/223_flirty_2.webp") with dissolve
    toby "Bawalah, Sayang."
    scene expression ("images/episode12/221_normal_3.webp") with dissolve
    charlotte "Ini tidak akan berakhir dengan baik."
    scene expression ("images/episode12/222_smile_1.webp") with dissolve
    patricia "Jangan khawatir [mom], saya tahu apa yang saya lakukan. Aku akan mengacaukan pikirannya. Saya bermain pria di sini, bukan permainannya."
    if ep12_stripWordAssociation:
        scene expression ("images/episode12/223_flirty_2.webp") with dissolve
        toby "Cobalah untuk tidak kehilangan pakaian Anda."
    else:
        scene expression ("images/episode12/223_normal_2.webp") with dissolve
        toby "Cobalah untuk tidak kalah."
    scene expression ("images/episode12/222_normal_3.webp") with dissolve
    patricia "Jangan khawatir tentang saya."
    scene expression ("images/episode12/222_smile_3.webp") with dissolve
    patricia "Mari kita mulai, pecundang."
    scene expression ("images/episode12/223_curious_2.webp") with dissolve
    toby "Apakah itu kata pertama Anda, atau apakah Anda hanya mendaftarkan kata -kata yang menggambarkan Anda?"
    scene expression ("images/episode12/221_drink.webp") with dissolve
    charlotte "Saya akan membutuhkan minuman lagi."
    scene expression ("images/episode12/222_normal_3.webp") with dissolve
    patricia "No, baby. The word is \"menstruation\"."
    scene expression ("images/episode12/221_drink.webp") with dissolve
    charlotte "Ho! Saya pasti akan membutuhkan minuman lagi."
    scene expression ("images/episode12/223_smile_2.webp") with dissolve
    toby "Game On, sayang."
    menu:
        "Burung"(csq="salah"):
            $ ep12_wordAssociation = 1
            call ep12_wordAssociation_looser_1 from _call_ep12_wordAssociation_looser_1
            return
        "[JGR] Darah"(csq="benar"):

            pass
        "Pantai"(csq="salah"):
            $ ep12_wordAssociation = 1
            call ep12_wordAssociation_looser_1 from _call_ep12_wordAssociation_looser_1_1
            return

    scene expression ("images/episode12/221_normal_3.webp") with dissolve
    charlotte "Anda anak -anak akan menjadi kematian saya."
    scene expression ("images/episode12/222_smile_1.webp") with dissolve
    patricia "Kurang berbicara, [mom]. Lebih banyak bermain."
    scene expression ("images/episode12/221_normal_2.webp") with dissolve
    charlotte "Anda membuat dua musuh di sini sayang."
    scene expression ("images/episode12/222_laugh_1.webp") with dissolve
    patricia "Saya bisa membawa kalian berdua."
    scene expression ("images/episode12/223_smile_2.webp") with dissolve
    toby "Lebih sedikit bicara, lebih banyak bermain, sayang!"
    scene expression ("images/episode12/221_normal_3.webp") with dissolve
    charlotte "\"Vampire\"."
    scene expression ("images/episode12/222_normal_3.webp") with dissolve
    patricia "\"Virgin\"."
    scene expression ("images/episode12/223_curious_2.webp") with dissolve
    toby "Really? \"Virgin\"?"
    scene expression ("images/episode12/221_drink.webp") with dissolve
    charlotte "Yup. Saya akan membutuhkan lebih banyak dari ini."
    scene expression ("images/episode12/222_normal_3.webp") with dissolve
    patricia "Ya. Ada legenda bahwa vampir minum darah perawan."
    scene expression ("images/episode12/223_smile_2.webp") with dissolve
    toby "Bagus."
    menu:
        "[JGR] Hymen"(csq="benar"):
            pass
        "Menakutkan"(csq="salah"):
            $ ep12_wordAssociation = 1
            call ep12_wordAssociation_looser_1 from _call_ep12_wordAssociation_looser_1_2
            return
        "Erotis"(csq="salah"):
            $ ep12_wordAssociation = 1
            call ep12_wordAssociation_looser_1 from _call_ep12_wordAssociation_looser_1_3
            return
    scene expression ("images/episode12/221_normal_2.webp") with dissolve
    charlotte "\"Woman\"."
    scene expression ("images/episode12/222_normal_3.webp") with dissolve
    patricia "\"Breasts\"."
    scene expression ("images/episode12/223_normal_2.webp") with dissolve
    menu:
        "Ninja"(csq="salah"):
            $ ep12_wordAssociation = 1
            call ep12_wordAssociation_looser_1 from _call_ep12_wordAssociation_looser_1_4
            return
        "Pakaian"(csq="salah"):

            $ ep12_wordAssociation = 1
            call ep12_wordAssociation_looser_1 from _call_ep12_wordAssociation_looser_1_5
            return
        "[JGR] Puting"(csq="benar"):

            pass

    scene expression ("images/episode12/221_surprised_3.webp") with dissolve
    charlotte "Anak-anak!"
    scene expression ("images/episode12/222_laugh_1.webp") with dissolve
    patricia "Kamu kalah!"
    scene expression ("images/episode12/221_normal_2.webp") with dissolve
    charlotte "Lihatlah dia, dia tidak memiliki penyesalan. Satu -satunya yang malu di sini adalah saya, jadi pilih kata -kata yang lebih normal.Saya tidak kalah! Kalian berdua harus memilih kata -kata normal. Anda tidak memainkannya."
    scene expression ("images/episode12/222_normal_1.webp") with dissolve
    patricia "Baik, tapi kamu masih kalah. Anda mengatakan anak -anak."
    scene expression ("images/episode12/223_normal_2.webp") with dissolve
    toby "Anak -anak baik -baik saja. Anak -anak mengisap puting."
    scene expression ("images/episode12/221_normal_3.webp") with dissolve
    charlotte "Mereka memakan puting, mereka tidak menghisapnya. Mereka hanya anak -anak, tidak seperti dua orang mesum yang saya angkat."
    scene expression ("images/episode12/222_laugh_1.webp") with dissolve
    patricia "Bagus. Anak -anak baik -baik saja."
    scene expression ("images/episode12/221_drink.webp") with dissolve
    charlotte "Ketika permainan ini sudah berakhir, kalian berdua perlu membawa saya ke rumah sakit untuk perawatan keracunan alkohol."
    scene expression ("images/episode12/222_normal_1.webp") with dissolve
    patricia "So you said \"children\". Then I'll go for \"adult\"."
    scene expression ("images/episode12/223_normal_1.webp") with dissolve
    menu:
        "[JGR] Game"(csq="benar"):
            pass
        "Pacar perempuan"(csq="salah"):
            $ ep12_wordAssociation = 1
            call ep12_wordAssociation_looser_1 from _call_ep12_wordAssociation_looser_1_6
            return
        "Panas"(csq="salah"):
            $ ep12_wordAssociation = 1
            call ep12_wordAssociation_looser_1 from _call_ep12_wordAssociation_looser_1_7
            return
    scene expression ("images/episode12/222_laugh_3.webp") with dissolve
    patricia "Anda cabul. Anda dan permainan dewasa Anda."
    scene expression ("images/episode12/223_smile_2.webp") with dissolve
    toby "Lebih sedikit bicara, lebih banyak bermain. Dengan begitu Anda tidak punya waktu untuk memikirkan jawaban Anda."
    scene expression ("images/episode12/222_normal_3.webp") with dissolve
    patricia "Ini bukan giliranku."
    scene expression ("images/episode12/223_smile_2.webp") with dissolve
    toby "Ini bukan, tetapi Anda memberi [mom] lebih banyak waktu untuk berpikir. Tidak ada lagi yang berbicara. Hanya kata -kata."
    scene expression ("images/episode12/222_curious_1.webp") with dissolve
    patricia "Jadi, [mom]. Apa kata -katamu?"
    scene expression ("images/episode12/221_smile_2.webp") with dissolve
    charlotte "Karena kita tentang masalah game dewasa."
    if charlotte_path:
        scene expression ("images/episode12/221_flirty_3.webp") with dissolve
        charlotte "\"Sex\"."
    else:
        scene expression ("images/episode12/221_normal_2.webp") with dissolve
        charlotte "\"Sex\"."
    scene expression ("images/episode12/222_surprised_1.webp") with dissolve
    patricia "[mom!c]! Anda nakal, nakal."
    scene expression ("images/episode12/223_laugh_2.webp") with dissolve
    toby "Berhenti bicara. Hanya kata -kata."
    scene expression ("images/episode12/221_laugh_2.webp") with dissolve
    charlotte "Ya, Tris. Lebih sedikit bicara, lebih banyak bermain."
    scene expression ("images/episode12/222_normal_1.webp") with dissolve
    patricia "Anda berada di tim yang salah, sayang!"
    scene expression ("images/episode12/223_smile_2.webp") with dissolve
    toby "Anda masih berbicara."
    scene expression ("images/episode12/222_normal_3.webp") with dissolve
    patricia "Fine. So it was \"sex\". Then my word is \"oral\"."
    scene expression ("images/episode12/223_laugh_1.webp") with dissolve
    menu:
        "[JGR] Anal"(csq="benar"):
            pass
        "Tidur"(csq="salah"):
            $ ep12_wordAssociation = 1
            call ep12_wordAssociation_looser_1 from _call_ep12_wordAssociation_looser_1_8
            return
        "Malam"(csq="salah"):
            $ ep12_wordAssociation = 1
            call ep12_wordAssociation_looser_1 from _call_ep12_wordAssociation_looser_1_9
            return
    scene expression ("images/episode12/221_drink.webp") with dissolve
    charlotte "\"Ass\"."
    scene expression ("images/episode12/222_normal_3.webp") with dissolve
    patricia "\"Curves\"."
    scene expression ("images/episode12/223_normal_1.webp") with dissolve
    menu:
        "Lumba -lumba"(csq="salah"):
            $ ep12_wordAssociation = 1
            call ep12_wordAssociation_looser_1 from _call_ep12_wordAssociation_looser_1_10
            return
        "Seks"(csq="salah"):
            $ ep12_wordAssociation = 1
            call ep12_wordAssociation_looser_1 from _call_ep12_wordAssociation_looser_1_11
            return
        "[JGR] Lingkaran"(csq="benar"):
            pass
    scene expression ("images/episode12/221_flirty_2.webp") with dissolve
    charlotte "\"Condom\"."
    scene expression ("images/episode12/222_laugh_3.webp") with dissolve
    patricia "\"Penis\"."
    scene expression ("images/episode12/223_laugh_1.webp") with dissolve
    menu:
        "Kerangka"(csq="salah"):
            $ ep12_wordAssociation = 1
            call ep12_wordAssociation_looser_1 from _call_ep12_wordAssociation_looser_1_12
            return
        "[JGR] cum"(csq="benar"):
            pass
        "Kereta"(csq="salah"):
            $ ep12_wordAssociation = 1
            call ep12_wordAssociation_looser_1 from _call_ep12_wordAssociation_looser_1_13
            return
    scene expression ("images/episode12/221_normal_2.webp") with dissolve
    charlotte "\"Pregnant\"."
    scene expression ("images/episode12/222_normal_3.webp") with dissolve
    patricia "\"Children\"Lai"
    scene expression ("images/episode12/223_surprised_2.webp") with dissolve
    toby "You said \"Children\"?"
    scene expression ("images/episode12/222_ups_3.webp") with dissolve
    patricia "No! I meant \"babies\"."
    scene expression ("images/episode12/223_laugh_2.webp") with dissolve
    toby "I don't care what you meant. You said \"children\"dan [mom] sudah menggunakannya."
    scene expression ("images/episode12/222_normal_3.webp") with dissolve
    patricia "Ya, tapi dia tidak bermaksud seperti itu. Dia hanya mengatakannya."
    scene expression ("images/episode12/221_laugh_2.webp") with dissolve
    charlotte "Nah, Anda memang bermain setelah saya mengucapkan kata itu. Jadi?"
    $ progress = 160
    if ep12_stripWordAssociation == False:
        stop music fadeout 5.0
        scene expression ("images/episode12/225.webp") with dissolve
        patricia "Lagipula ini adalah permainan yang bodoh."
        scene expression ("images/episode12/226.webp") with dissolve
        charlotte "Apa yang terjadi, sayang? Anda tidak tahu bagaimana cara kalah?"
        scene expression ("images/episode12/227.webp") with dissolve
        patricia "Game ini bodoh."
        scene expression ("images/episode12/228_1.webp") with dissolve
        toby "Yup. Dia masih tidak tahu bagaimana cara kalah."
        scene expression ("images/episode12/227.webp") with dissolve
        patricia "Game ini bodoh."
        scene expression ("images/episode12/228_2.webp") with dissolve
        toby "Mungkin atau Anda tidak cukup pintar untuk itu."
        scene expression ("images/episode12/229.webp") with dissolve
        patricia "Hei, [toby!c]. Ambil ini!"
        scene expression ("images/episode12/230.webp") with dissolve
        charlotte "Tris! Kembalilah ke sini sekarang."
        scene expression ("images/episode12/231.webp") with dissolve
        patricia "Maaf, [mom]. Harus mandi."
        scene expression ("images/episode12/232.webp") with dissolve
        charlotte "Tuhan, gadis itu."
        toby "Jangan khawatir, [mom]. Dia akan kembali dalam 20 menit untuk meminta maaf."
        scene expression ("images/episode12/233.webp") with dissolve
        toby "Bagaimanapun, saya harus membiarkan Anda rileks sekarang."
        if charlotte_path:
            scene expression ("images/episode12/279.webp") with dissolve
            charlotte "Bisakah Anda meletakkan tabir surya di punggung saya sebelum Anda pergi? Saya akan tinggal di bawah sinar matahari untuk sementara waktu."
            toby "Tentu. Tidak masalah."
        return
    else:

        pass

    label memory_41:

        scene expression ("images/episode12/222_surprised_1.webp") with dissolve
        patricia "Anda akan membiarkan saya menelanjangi di depan [brother] saya? Jenis [mother] apa itu?"
        scene expression ("images/episode12/221_laugh_2.webp") with dissolve
        charlotte "Jenis yang cukup minum untuk tidak peduli dengan upaya Anda untuk membuat saya bersalah."
        scene expression ("images/episode12/223_laugh_1.webp") with dissolve
        toby "Saya suka mabuk [mom]."
        scene expression ("images/episode12/246.webp") with dissolve
        patricia "Hanya Anda tunggu, nona, karena Anda akan kalah juga. Kemudian saya akan melihat Anda telanjang di depan [children] Anda."
        scene expression ("images/episode12/247.webp") with dissolve
        charlotte "Mengapa Anda masih memakai atasan Anda, sayang?"
        scene expression ("images/episode12/248.webp") with dissolve
        patricia "Perhatikan saja punggung Anda, sayang."

        $ unlockImage(persistent.patricia_23)
        scene expression ("images/episode12/249.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        patricia "Apakah kamu bahagia sekarang?"
        if patricia_path:
            scene expression ("images/episode12/249_1.webp") with dissolve
            toby "Saya lebih bahagia jika Anda tidak menutupi diri Anda."
            scene expression ("images/episode12/250.webp") with dissolve
            patricia "Anda harus mengawasi punggung Anda juga."
            scene expression ("images/episode12/251.webp") with dissolve
            toby "Oooooh ... aku takut. Saya gemetar, tetapi Anda tidak bisa memberi tahu karena air."
        else:
            scene expression ("images/episode12/249_2.webp") with dissolve
            charlotte "Katakanlah itu berhasil untuk saat ini."

        scene expression ("images/episode12/252.webp") with dissolve
        patricia "Aku akan membuat kalian berdua telanjang. Hanya Anda tunggu."
        toby "Ya, ya. Kami sudah tahu itu."
        patricia "Hanya Anda tunggu."

        $ unlockMemory(persistent.memory_41)
        $ renpy.end_replay()

    scene expression ("images/episode12/253_normal_2.webp") with dissolve
    charlotte "Oke anak -anak, tapi tolong berhenti menggunakan kata -kata kotor. Saya tidak merasa nyaman."
    scene expression ("images/episode12/254_normal_1.webp") with dissolve
    patricia "So you're okay with me showing my tits to my [brother], but you're not okay when I say \"sex\", \"penis\" or \"masturbation\"?"
    scene expression ("images/episode12/255_laugh_1.webp") with dissolve
    toby "Kami tidak membuat janji."
    scene expression ("images/episode12/254_normal_3.webp") with dissolve
    patricia "Mari kita mainkan. Saya ingin menang."
    scene expression ("images/episode12/253_laugh_2.webp") with dissolve
    charlotte "Anda tahu bahwa untuk menang, Anda harus menjaga pakaian Anda, bukan sebaliknya."
    scene expression ("images/episode12/254_angry_1.webp") with dissolve
    patricia "Game On, Bitch!"
    scene expression ("images/episode12/253_surprised_2.webp") with dissolve
    charlotte "Apa yang kamu panggil aku, wanita muda?"
    scene expression ("images/episode12/254_scared_1.webp") with dissolve
    patricia "Umm... I didn't call you anything. I said game on. And then the first word is \"bitch\"."
    scene expression ("images/episode12/253_normal_2.webp") with dissolve
    charlotte "Itulah yang saya pikir maksud Anda."
    scene expression ("images/episode12/254_awkward_1.webp") with dissolve
    patricia "Ayo, [mom]. Apakah Anda benar -benar berpikir saya akan memanggil Anda seperti itu? Saya menghormati Anda."
    scene expression ("images/episode12/255_laugh_2.webp") with dissolve
    toby "Oke kalau begitu, Ms. hormat. Biarkan bermain."
    scene expression ("images/episode12/255_smile_1.webp") with dissolve
    menu:
        "[JGR] Threesome"(csq="benar"):
            pass
        "Payung"(csq="salah"):
            $ ep12_wordAssociation = 2
            call ep12_wordAssociation_looser_2 from _call_ep12_wordAssociation_looser_2
            return
        "Pasir"(csq="salah"):
            $ ep12_wordAssociation = 2
            call ep12_wordAssociation_looser_2 from _call_ep12_wordAssociation_looser_2_1
            return

    scene expression ("images/episode12/253_normal_2.webp") with dissolve
    charlotte "\"Sex\"."
    scene expression ("images/episode12/254_surprised_1.webp") with dissolve
    patricia "Oooh... You said \"sex\"? Itu kata yang buruk."
    scene expression ("images/episode12/253_normal_2.webp") with dissolve
    charlotte "Apa? Anda berdua menggunakan kata -kata buruk."
    scene expression ("images/episode12/255_smile_1.webp") with dissolve
    toby "Ya, tapi kata -kata kami tidak digunakan sebelumnya."
    scene expression ("images/episode12/253_curious_3.webp") with dissolve
    charlotte "Apa? Kita tidak bisa menggunakan kata -kata dari sebelumnya?"
    scene expression ("images/episode12/254_laugh_1.webp") with dissolve
    patricia "Tentu saja kita bisa \ 't. Apa kita, dua belas?"
    scene expression ("images/episode12/253_normal_2.webp") with dissolve
    charlotte "Ah, okay, I didn't know. I'll say \"moan\"Kemudian."
    scene expression ("images/episode12/254_laugh_1.webp") with dissolve
    patricia "Tidak, Anda tidak bisa mengatakan apa pun dengan top Anda."
    label memory_42:


        scene expression ("images/episode12/253_normal_2.webp") with dissolve
        charlotte "Ayo teman -teman. I \ m Anda [mother]. Apakah Anda benar -benar mengharapkan saya menanggalkan pakaian di depan Anda?"
        scene expression ("images/episode12/254_angry_1.webp") with dissolve
        patricia "Lihat aku? I \ m Anda [daughter]. Anda tidak menunjukkan penyesalan ketika Anda membuat saya menghapus atasan saya."
        scene expression ("images/episode12/253_normal_2.webp") with dissolve
        charlotte "Berhati -hatilah dengan siapa Anda."
        scene expression ("images/episode12/254_laugh_1.webp") with dissolve
        patricia "Aku akan bersamanya setelah Anda menghapus atasan Anda. Kami akan menjadi hotness topless."
        scene expression ("images/episode12/255_laugh_2.webp") with dissolve
        toby "Hotness topless?"
        scene expression ("images/episode12/254_laugh_3.webp") with dissolve
        patricia "Ya. Itu nama tim kami."
        if charlotte_path:
            scene expression ("images/episode12/255_laugh_1.webp") with dissolve
            toby "Nah, [mom]. Saya kira Anda harus menghapus atasan Anda untuk bergabung dengan klub panas topless."
        else:
            scene expression ("images/episode12/254_laugh_1.webp") with dissolve
            patricia "Ayo, [mom]. Kehilangan atasan Anda sehingga Anda dapat bergabung dengan tim hotness topless."

        scene expression ("images/episode12/256.webp") with dissolve
        charlotte "Tidak ada tim dalam game ini."
        scene expression ("images/episode12/257.webp") with dissolve
        charlotte "Dan selain itu, mengapa saya melepas atasan saya dan kemudian mencoba menyembunyikan payudara saya seperti Anda, ketika saya bisa melepas bagian bawah setelan saya dan membiarkan air menutupi saya."

        scene expression ("images/episode12/254_angry_1.webp") with dissolve
        patricia "Anda curang."
        scene expression ("images/episode12/253_laugh_2.webp") with dissolve
        charlotte "Bagaimana curang itu? Aturannya kehilangan satu item pakaian. Tidak ada yang dikatakan tentang yang mana."
        $ progress = 161

        scene expression ("images/episode12/255_thinking.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck. I can't believe [mom] isn't wear her suit bottom. If I try hard enough I can almost see her pussy.{/i}"
        $ unlockImage(persistent.charlotte_20)
        scene expression ("images/episode12/258.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think I can see something.{/i}"
        scene expression ("images/episode12/259.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit. She closed her legs.{/i}"
        $ unlockMemory(persistent.memory_42)
        $ renpy.end_replay()

    charlotte "[toby!c]! Apakah Anda bersama kami?"
    scene expression ("images/episode12/260.webp") with dissolve
    toby "Uhhh ... apa?"
    scene expression ("images/episode12/253_laugh_3.webp") with dissolve
    charlotte "Apakah Anda di sini bersama kami?"
    scene expression ("images/episode12/254_flirty_3.webp") with dissolve
    patricia "Apakah Anda memeriksa selangkangan [mom]?"
    scene expression ("images/episode12/255_awkward_2.webp") with dissolve
    toby "TIDAK."
    scene expression ("images/episode12/253_smile_3.webp") with dissolve
    charlotte "Kemudian ucapkan sepatah kata pun."
    scene expression ("images/episode12/255_normal_1.webp") with dissolve
    toby "Anda mengucapkan sepatah kata pun. Anda orang yang kalah putaran terakhir."
    scene expression ("images/episode12/254_laugh_3.webp") with dissolve
    patricia "Yah dia sudah melakukannya, tetapi Anda terlalu fokus pada selangkangannya untuk mendengarnya."
    scene expression ("images/episode12/255_normal_2.webp") with dissolve
    toby "Kemudian Anda mengucapkan sepatah kata pun. Giliran Anda."
    scene expression ("images/episode12/253_smile_3.webp") with dissolve
    charlotte "Dia juga mengatakan sepatah kata pun."
    scene expression ("images/episode12/255_curious_1.webp") with dissolve
    toby "Kata apa?"
    scene expression ("images/episode12/254_normal_3.webp") with dissolve
    patricia "Tidak. Kami tidak memberi tahu Anda. Katakan saja kata -kata Anda dan berharap yang terbaik."
    scene expression ("images/episode12/255_thinking.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit. What word would they say? I can't believe I'm going to lose this.{/i}"
    scene expression ("images/episode12/261.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is she giving me hint, or she's just waiting for me to fail?{/i}"
    menu:
        "Kepala"(csq="salah"):
            $ ep12_wordAssociation = 2
            call ep12_wordAssociation_looser_2 from _call_ep12_wordAssociation_looser_2_2
            return
        "[JGR] Rambut"(csq="benar"):
            pass
        "Mata"(csq="salah"):

            $ ep12_wordAssociation = 2
            call ep12_wordAssociation_looser_2 from _call_ep12_wordAssociation_looser_2_3
            return
    scene expression ("images/episode12/262.webp") with dissolve
    charlotte "Bagus. Bagaimanapun, dia memperhatikan."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Thank you, sweet [mother].{/i}"


    scene expression ("images/episode12/253_smile_2.webp") with dissolve
    charlotte "\"Blonde\"."
    scene expression ("images/episode12/254_normal_3.webp") with dissolve
    patricia "\"Bimbo\"."
    scene expression ("images/episode12/255_laugh_1.webp") with dissolve
    menu:
        "Rusa"(csq="salah"):
            $ ep12_wordAssociation = 2
            scene expression ("images/episode12/254_laugh_3.webp") with dissolve
            patricia "Itu bamby."
            scene expression ("images/episode12/255_normal_2.webp") with dissolve
            patricia "Hal yang sama."
            call ep12_wordAssociation_looser_2 from _call_ep12_wordAssociation_looser_2_6
            return
        "Mall"(csq="salah"):
            $ ep12_wordAssociation = 2
            call ep12_wordAssociation_looser_2 from _call_ep12_wordAssociation_looser_2_7
            return
        "[JGR] Plastik"(csq="benar"):
            pass

    scene expression ("images/episode12/253_normal_2.webp") with dissolve
    charlotte "\"Toy\"."
    scene expression ("images/episode12/254_laugh_3.webp") with dissolve
    patricia "\"Dildo\"."
    scene expression ("images/episode12/253_drink.webp") with dissolve
    charlotte "Aduh, terjadi lagi."
    scene expression ("images/episode12/255_normal_1.webp") with dissolve
    menu:
        "Nakal"(csq="salah"):
            $ ep12_wordAssociation = 2
            call ep12_wordAssociation_looser_2 from _call_ep12_wordAssociation_looser_2_8
            return
        "Kuda"(csq="salah"):
            $ ep12_wordAssociation = 2
            call ep12_wordAssociation_looser_2 from _call_ep12_wordAssociation_looser_2_9
            return
        "[JGR] Gag"(csq="benar"):
            pass
    scene expression ("images/episode12/253_drink.webp") with dissolve
    charlotte "\"Reflex\"."
    scene expression ("images/episode12/254_laugh_3.webp") with dissolve
    patricia "\"Arousal\"."
    scene expression ("images/episode12/255_laugh_1.webp") with dissolve
    menu:
        "Sekitar"(csq="salah"):
            $ ep12_wordAssociation = 2
            call ep12_wordAssociation_looser_2 from _call_ep12_wordAssociation_looser_2_10
            return
        "[JGR] Stimulasi"(csq="benar"):
            pass
        "Musik"(csq="salah"):
            $ ep12_wordAssociation = 2
            call ep12_wordAssociation_looser_2 from _call_ep12_wordAssociation_looser_2_11
            return
    if charlotte_path:
        scene expression ("images/episode12/253_flirty_3.webp") with dissolve
    else:
        scene expression ("images/episode12/253_laugh_2.webp") with dissolve
    charlotte "\"Erection\"."
    scene expression ("images/episode12/254_cool_3.webp") with dissolve
    patricia "\"Dick\"."
    scene expression ("images/episode12/255_normal_1.webp") with dissolve
    menu:
        "[JGR] Vagina"(csq="benar"):
            pass
        "Peternakan"(csq="salah"):
            $ ep12_wordAssociation = 2
            scene expression ("images/episode12/254_laugh_3.webp") with dissolve
            patricia "Salah."
            scene expression ("images/episode12/255_curious_2.webp") with dissolve
            toby "Bagaimana itu salah? Anda bisa mengatakan penis atau ayam. Dan ayam tinggal di pertanian."
            call ep12_wordAssociation_looser_2 from _call_ep12_wordAssociation_looser_2_12
            return
        "Pisang"(csq="salah"):
            $ ep12_wordAssociation = 2
            scene expression ("images/episode12/254_laugh_3.webp") with dissolve
            patricia "Salah."
            scene expression ("images/episode12/255_curious_2.webp") with dissolve
            toby "Bagaimana itu salah? Dick berbentuk seperti pisang."
            call ep12_wordAssociation_looser_2 from _call_ep12_wordAssociation_looser_2_13
            return

    scene expression ("images/episode12/253_normal_2.webp") with dissolve
    charlotte "\"Fetus\"."
    scene expression ("images/episode12/254_smile_3.webp") with dissolve
    patricia "\"Child\"."
    scene expression ("images/episode12/255_laugh_2.webp") with dissolve
    toby "Permainan selesai."
    scene expression ("images/episode12/254_surprised_3.webp") with dissolve
    patricia "Mengapa?"
    scene expression ("images/episode12/255_normal_2.webp") with dissolve
    toby "You said \"child\". It's the same as saying \"children\"."
    scene expression ("images/episode12/254_angry_3.webp") with dissolve
    patricia "Tidak, itu tidak. Mereka adalah dua kata yang berbeda."
    scene expression ("images/episode12/253_smile_2.webp") with dissolve
    charlotte "Sayang, kamu tersesat."
    scene expression ("images/episode12/254_angry_1.webp") with dissolve
    patricia "Saya tidak. Mereka adalah dua kata yang berbeda."
    scene expression ("images/episode12/255_normal_2.webp") with dissolve
    toby "Anda juga tidak diizinkan menggunakan jamak.Mereka tidak. Ini kata yang sama. Itu hanya jamak."
    $ progress = 162
    label memory_43:


        scene expression ("images/episode12/263.webp") with dissolve
        patricia "Game ini bodoh. Saya keluar dari sini."
        scene expression ("images/episode12/264.webp") with dissolve
        toby "Ayam."
        scene expression ("images/episode12/265.webp") with dissolve
        charlotte "Tinggalkan dia. Dia hanya pecundang yang sakit."
        scene expression ("images/episode12/266.webp") with dissolve
        patricia "Saya bukan pecundang yang sakit. Saya tidak marah ketika saya kalah."
        scene expression ("images/episode12/267.webp") with dissolve
        toby "Lalu mengapa Anda masih memakai pantat Anda?"
        scene expression ("images/episode12/269_1.webp") with dissolve
        patricia "Persetan kalian berdua!"
        scene expression ("images/episode12/270.webp") with dissolve
        patricia "Di sana ... simpan mereka. Pastikan Anda mengambil foto, Anda sesat."
        $ unlockImage(persistent.patricia_24)
        scene expression ("images/episode12/271.webp") with dissolve
        charlotte "Tujuan bagus, sayang!"
        scene expression ("images/episode12/272.webp") with dissolve
        patricia "Sampai jumpa!"
        $ unlockMemory(persistent.memory_43)
        $ renpy.end_replay()

    scene expression ("images/episode12/273.webp") with dissolve
    charlotte "Kembali ke sini dan minta maaf, nona muda! Saya tidak mengizinkan bahasa semacam itu di rumah saya."
    scene expression ("images/episode12/274.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Thank you, Tris!{/i}"
    scene expression ("images/episode12/275.webp") with dissolve
    charlotte "Pandang, sayang, atau Anda membumi."
    toby "Saya tidak berpikir ancaman semacam itu bekerja pada saya lagi."
    charlotte "Jangan menguji saya, anak kecil."
    charlotte "Sekarang, lihatlah agar saya bisa berpakaian."
    scene expression ("images/episode12/276.webp") with dissolve
    toby "Saya tidak melihat."
    charlotte "Seperti aku akan mempercayaimu. Seberapa cepat Anda lupa bahwa Anda membutuhkan bantuan saya karena Anda tersesat dalam pikiran Anda."
    toby "Terima kasih untuk itu."
    toby "Bagaimanapun, saya harus pergi juga."
    scene expression ("images/episode12/279.webp") with dissolve
    charlotte "Sebelum Anda pergi, bisakah Anda meletakkan tabir surya di punggung saya? Saya akan tinggal di bawah sinar matahari untuk sementara waktu."
    toby "Tentu. Tidak masalah."

    return

label ep12_wordAssociation_looser_1:
    stop music fadeout 5.0
    scene expression ("images/episode12/222_laugh_3.webp") with dissolve
    patricia "Itu tidak bagus."
    scene expression ("images/episode12/223_smile_2.webp") with dissolve
    toby "Apa? Itu bagus."
    scene expression ("images/episode12/221_normal_3.webp") with dissolve
    charlotte "Tidak. Tidak bekerja."
    scene expression ("images/episode12/223_normal_1.webp") with dissolve
    toby "Itu benar."
    scene expression ("images/episode12/222_normal_3.webp") with dissolve
    patricia "Tidak, itu tidak. Kamu kalah!"
    if ep12_stripWordAssociation:
        scene expression ("images/episode12/222_laugh_3.webp") with dissolve
        patricia "Ayo [toby!c]. Kehilangan batang itu."
        scene expression ("images/episode12/223_normal_2.webp") with dissolve
        toby "Saya tidak akan menelanjangi di depan [mother] dan [sister] saya. Ini adalah ide bodoh di tempat pertama."
        scene expression ("images/episode12/221_laugh_3.webp") with dissolve
        charlotte "Saya mengatakan hal yang sama, tetapi Anda tidak setuju dengan saya, jadi sekarang mari kita lihat sedikit [toby!c]."
        scene expression ("images/episode12/222_laugh_1.webp") with dissolve
        patricia "Sedikit [toby!c]. Ya Tuhan, itu hal paling lucu yang pernah saya dengar!"
        scene expression ("images/episode12/234.webp") with dissolve
        toby "Bagus! Tetapi jika [dad] pulang, Anda akan menjadi orang yang menjelaskan mengapa [son] Anda telanjang di bak mandi air panas dengan Anda dan [daughter] Anda."
        scene expression ("images/episode12/235.webp") with dissolve
        charlotte "Perjalanan bersalah tidak akan bekerja pada saya sekarang. Aku terlalu mabuk untuk itu, jadi potong, potong!"
        scene expression ("images/episode12/236.webp") with dissolve
        patricia "Potong, potong, [toby!c]! Tunjukkan sedikit [toby!c]!"
        scene expression ("images/episode12/237.webp") with dissolve
        toby "Senang sekarang?"
        if charlotte_path:
            charlotte "Saya lebih bahagia jika Anda memiliki kesalahan, tetapi baik -baik saja."
        else:
            patricia "Akan lebih baik jika Anda sulit."
        scene expression ("images/episode12/238.webp") with dissolve
        toby "Nah, saya tidak akan mendapatkan kesalahan saat melihat kalian."
        scene expression ("images/episode12/239.webp") with dissolve
        if charlotte_path:
            charlotte "Itu dia. Itu jauh lebih baik."
        else:
            patricia "Sedikit [toby!c] tidak lagi sedikit lagi."
        scene expression ("images/episode12/240.webp") with dissolve
        charlotte "Saya pikir itu cukup. Anda harus berpakaian."
        scene expression ("images/episode12/241.webp") with dissolve
        toby "Aku tidak percaya aku kalah melawan kalian berdua."
    scene expression ("images/episode12/242.webp") with dissolve
    patricia "Ngomong -ngomong, aku akan mandi. Saya tidak ingin menghabiskan waktu lagi dengan pecundang."
    toby "Ha ha. Sangat lucu."
    scene expression ("images/episode12/243_0.webp") with dissolve
    patricia "Bye [mom]."
    scene expression ("images/episode12/243_1.webp") with dissolve
    patricia "Bye Loser!"
    scene expression ("images/episode12/243_2.webp") with dissolve
    toby "Persetan denganmu."
    scene expression ("images/episode12/244.webp") with dissolve
    charlotte "[toby!c]! Anda meminta maaf saat ini."
    scene expression ("images/episode12/245.webp") with dissolve
    toby "Dia memulainya."
    scene expression ("images/episode12/244.webp") with dissolve
    charlotte "Dan Anda harus menyelesaikannya."
    scene expression ("images/episode12/243_0.webp") with dissolve
    patricia "Jangan khawatir, [mom]. Aku sudah terbiasa dengannya. Dia hanya pecundang yang sakit."
    scene expression ("images/episode12/232_2.webp") with dissolve
    charlotte "Anda tahu bahwa saya tidak menyukai bahasa semacam itu."
    toby "Maaf, [mom]."
    toby "Bagaimanapun, saya pikir saya akan pergi juga. Aku akan membiarkanmu rileks."
    if charlotte_path:
        scene expression ("images/episode12/279.webp") with dissolve
        charlotte "Sebelum Anda pergi, dapatkah Anda meletakkan tabir surya di punggung saya? Saya akan tinggal di bawah sinar matahari untuk sementara waktu."
        toby "Tentu. Tidak masalah."

    return

label ep12_wordAssociation_looser_2:
    stop music fadeout 5.0
    scene expression ("images/episode12/254_laugh_3.webp") with dissolve
    patricia "Itu tidak bagus."
    scene expression ("images/episode12/255_normal_2.webp") with dissolve
    toby "Apa? Itu bagus."
    scene expression ("images/episode12/253_laugh_3.webp") with dissolve
    charlotte "Tidak. Tidak bekerja."
    scene expression ("images/episode12/255_normal_1.webp") with dissolve
    toby "Itu benar."
    scene expression ("images/episode12/254_cool_3.webp") with dissolve
    patricia "Tidak, itu tidak. Kamu kalah!"
    scene expression ("images/episode12/254_laugh_3.webp") with dissolve
    patricia "Ayo, [toby!c]. Kehilangan batang itu!"
    scene expression ("images/episode12/255_normal_2.webp") with dissolve
    toby "Saya tidak akan menelanjangi di depan [mother] dan [sister] saya. Ini adalah ide bodoh di tempat pertama."
    scene expression ("images/episode12/253_laugh_3.webp") with dissolve
    charlotte "Lihatlah kami. Anda tidak berpikir itu adalah ide yang buruk saat itu, sekarang mari kita lihat sedikit [toby!c]."
    scene expression ("images/episode12/254_laugh_1.webp") with dissolve
    patricia "Sedikit [toby!c]. Ya Tuhan, itu hal paling lucu yang pernah saya dengar!"

    scene expression ("images/episode12/280.webp") with dissolve
    toby "Bagus! Tetapi jika [dad] pulang, Anda akan menjadi orang yang menjelaskan mengapa kita semua telanjang di bak mandi."
    scene expression ("images/episode12/281.webp") with dissolve
    charlotte "Manipulasi emosional tidak akan bekerja pada saya sekarang. Aku terlalu mabuk untuk itu, jadi potong, potong!"
    scene expression ("images/episode12/282.webp") with dissolve
    patricia "Potong, potong, [toby!c]! Tunjukkan sedikit [toby!c]!"
    scene expression ("images/episode12/283.webp") with dissolve
    toby "Senang sekarang?"
    if charlotte_path:
        charlotte "Saya lebih bahagia jika Anda memiliki kesalahan, tetapi baik -baik saja."
    else:
        patricia "Akan lebih baik jika Anda sulit."
    scene expression ("images/episode12/238.webp") with dissolve
    toby "Nah, saya tidak akan mendapatkan kesalahan saat melihat kalian."
    scene expression ("images/episode12/239.webp") with dissolve
    if charlotte_path:
        charlotte "Itu dia. Itu jauh lebih baik."
    else:
        patricia "Sedikit [toby!c] tidak lagi sedikit lagi."
    scene expression ("images/episode12/281.webp") with dissolve
    charlotte "Saya pikir itu cukup. Anda harus berpakaian."
    scene expression ("images/episode12/255_normal_1.webp") with dissolve
    toby "Saya tidak percaya saya kalah."
    scene expression ("images/episode12/284.webp") with dissolve
    patricia "Ngomong -ngomong, aku akan mandi. Saya tidak ingin menghabiskan waktu lagi dengan pecundang."
    toby "Ummm ... di mana atasan Anda, sedikit [sister]?"
    scene expression ("images/episode12/285_1.webp") with dissolve
    patricia "Sampai jumpa!"
    toby "Persetan denganmu."
    scene expression ("images/episode12/244.webp") with dissolve
    charlotte "[toby!c]! Appisieze saat ini."
    scene expression ("images/episode12/245.webp") with dissolve
    toby "Dia memulainya."
    scene expression ("images/episode12/244.webp") with dissolve
    charlotte "Dan Anda tidak boleh menyelesaikannya."
    scene expression ("images/episode12/285_2.webp") with dissolve
    patricia "Jangan khawatir [mom]. Aku sudah terbiasa dengannya. Dia hanya pecundang yang sakit."
    scene expression ("images/episode12/232.webp") with dissolve
    charlotte "Anda tahu bahwa saya tidak menyukai bahasa semacam itu."
    toby "Maaf, [mom]."
    toby "Bagaimanapun, saya pikir saya akan pergi juga. Aku akan membiarkanmu rileks."
    if charlotte_path:
        scene expression ("images/episode12/279.webp") with dissolve
        charlotte "Sebelum Anda pergi, dapatkah Anda meletakkan tabir surya di punggung saya? Saya akan tinggal di bawah sinar matahari untuk sementara waktu."
        toby "Tentu. Tidak masalah."

    return

label episode12_massage_charlotte:
    $ progress = 163
    label memory_44:

        scene expression ("images/episode12/286.webp") with dissolve
        charlotte "Saya siap untuk tangan ajaib Anda."
        scene expression ("images/episode12/287.webp") with dissolve
        toby "Tidakkah Anda ingin menghapus atasan Anda? Saya pikir Anda tidak menyukai garis tan."
        scene expression ("images/episode12/288.webp") with dissolve
        charlotte "Anda tahu ini ide yang buruk, bukan?"
        toby "Karena beberapa alasan, tapi tetap saja, garis tan?"
        charlotte "Berjanji Anda akan berperilaku?"
        scene expression ("images/episode12/289.webp") with dissolve
        toby "Janji saya akan mencoba."
        scene expression ("images/episode12/290.webp") with dissolve
        charlotte "Itu cukup dekat."
        scene expression ("images/episode12/291.webp") with dissolve
        toby "Jadi? Bagaimana hal -hal antara Anda dan [dad]?"
        scene expression ("images/episode12/292.webp") with dissolve
        charlotte "Yah, dia membawakanku bunga kemarin ketika dia pulang kerja dan meminta maaf atas segalanya, tapi sejujurnya aku bosan dengan bunga dan alasan."
        charlotte "You can't just keep doing stupid stuff and then with one, \"I'm sorry\", mengharapkan hal -hal untuk kembali normal secara ajaib."
        charlotte "Saya sangat senang Anda tidak menyukai [father] Anda."
        if emma_pissed:
            scene expression ("images/episode12/293.webp") with dissolve
            toby "Ya. Aku tidak seperti dia."
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}At least [dad] doesn't cheat on [mom].{/i}"
        scene expression ("images/episode12/294.webp") with dissolve
        charlotte "Ngomong -ngomong, jangan membicarakannya. Saya tidak terlalu mood untuk itu."
        toby "Untuk apa Anda berminat?"
        charlotte "Untuk pijatan terbaik sepanjang masa."
        scene expression ("images/episode12/295.webp") with dissolve
        toby "Saya pikir saya menerapkan tabir surya, tidak memijat punggung Anda."
        charlotte "Itu juga, tapi tanganmu sangat bagus. Saya pikir saya harus membayar Anda untuk ini. Terlalu bagus untuk itu bebas."
        toby "Jangan khawatir, saya mendapatkan pembayaran saya."
        scene expression ("images/episode12/296.webp") with dissolve
        charlotte "Begitu?"
        charlotte "Apakah Anda mencuri uang dari dompet saya?"
        toby "Satu -satunya hal yang saya curi adalah beberapa pandangan ke tubuh Anda yang cantik."
        charlotte "Dan apakah pembayaran itu cukup?"
        scene expression ("images/episode12/297.webp") with dissolve
        toby "Biasanya ya."
        charlotte "Dan apa yang terjadi ketika itu menjadi tidak cukup?"
        toby "Saya dibesarkan untuk dengan senang hati membantu mereka yang membutuhkan, jadi saya mendapatkan kesenangan hanya dari membantu Anda dengan tabir surya Anda."
        charlotte "Seseorang membesarkanmu dengan baik."
        scene expression ("images/episode12/298.webp") with dissolve
        toby "Tolong sebarkan kaki Anda, jadi saya dapat memiliki akses yang lebih baik."
        scene expression ("images/episode12/299.webp") with dissolve
        charlotte "Akses yang lebih baik ke?"
        toby "Ke kakimu."
        charlotte "Oh, ya. Benar. Lagi pula, kaki saya juga harus dilindungi dari matahari."
        scene expression ("images/episode12/300.webp") with dissolve
        toby "Tentu saja. Kami tidak ingin kaki -kaki cantik ini terbakar."
        charlotte "Anda pikir saya memiliki kaki yang bagus?"
        toby "Apakah Anda bercanda? Tentu saja. Anda tidak?"
        charlotte "Ayo. Saya tidak berusia 20 tahun lagi. Anda tidak mungkin berpikir mereka terlihat bagus."
        scene expression ("images/episode12/301.webp") with dissolve
        toby "Apa yang tidak disukai? Kulit Anda lebih halus dari sutra. Otot Anda sempurna, tidak terlalu berotot, namun tidak lemak juga."
        charlotte "Apakah ada hal lain yang Anda sukai dari saya secara fisik?"

        call episode12_massage_charlotte_choices from _call_episode12_massage_charlotte_choices

        $ progress = 164
        scene expression ("images/episode12/322.webp") with dissolve
        toby "Baik itu tentang semua."
        charlotte "Saya tidak berpikir saya pernah menerima pujian yang begitu bagus. Aku terbakar. Anda membuat saya tersipu."
        toby "Apakah kamu yakin aku membuatmu tersipu?"
        charlotte "Apa lagi yang bisa?"
        toby "Saya tidak tahu, mungkin Anda terlalu bersemangat."
        scene expression ("images/episode12/323.webp") with dissolve
        charlotte "Mungkin, tapi kami tidak pernah tahu, karena sekarang Anda akan mendinginkan semuanya dengan memberi tahu saya kekurangan saya."
        toby "Apa yang membuat Anda berpikir Anda memiliki kekurangan?"
        charlotte "Oh tolong, jangan bertindak seperti saya sempurna. Kami berdua tahu saya tidak."
        scene expression ("images/episode12/324.webp") with dissolve
        toby "Sejujurnya, Anda memiliki satu kekurangan."
        charlotte "Dan apa itu?"
        toby "Fakta bahwa Anda adalah [mother] saya."
        charlotte "Maaf melanggar Anda, tetapi saya memiliki satu kelemahan lagi. Saya juga menikah."
        toby "Ya. Betapa saya berharap Anda sempurna."
        scene expression ("images/episode12/325.webp") with dissolve
        charlotte "Dan apa yang akan Anda lakukan jika saya tidak memiliki kedua kekurangan ini dan sempurna?"
        scene expression ("images/episode12/326.webp") with dissolve
        toby "Sebagai permulaan saya akan memberi tahu Anda bahwa Anda bisa mendapatkan garis tan tidak hanya dari atas Anda."
        charlotte "Benar-benar? Saya bisa berakhir dengan garis tan?"
        scene expression ("images/episode12/327.webp") with dissolve
        toby "Ya."
        charlotte "Kami tidak menginginkannya, bukan?"
        toby "Tentu saja kami tidak!"
        scene expression ("images/episode12/328.webp") with dissolve
        toby "Kemudian saya akan mulai menggosok tabir surya itu di seluruh paha bagian dalam Anda, berhati -hati untuk tidak melewatkan satu tempat pun."
        scene expression ("images/episode12/329.webp") with dissolve
        charlotte "Ya. Menutupi semua tempat sangat penting."
        scene expression ("images/episode12/330.webp") with dissolve
        toby "Sangat penting."
        $ unlockImage(persistent.charlotte_21)
        scene expression ("images/episode12/331.webp") with dissolve
        toby "Lagipula, aku memang mencintaimu dan ingin merawatmu dengan baik."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck me... She's so wet right now.{/i}"
        scene expression ("images/episode12/332.webp") with dissolve
        charlotte "[toby!c], tolong berhenti. Saya tidak bisa melakukan ini."
        toby "Apakah Anda yakin ingin saya berhenti?"
        charlotte "Satu -satunya hal yang saya yakin, adalah jika kita melakukan ini kita tidak dapat kembali."
        toby "Mengapa kembali?"
        scene expression ("images/episode12/333.webp") with dissolve
        charlotte "Saya mengerti Anda terangsang dan tidak ada gunanya menyembunyikannya. Saya juga sangat terangsang. Saya tidak ingat kapan terakhir kali saya merasa sangat bersemangat tentang sesuatu, tetapi kita harus berhenti."
        charlotte "Anda mengatakannya sendiri. Saya [mother] Anda dan tidak peduli seberapa mabuk saya, saya tidak akan pernah bisa melupakannya."
        charlotte "Tidak mudah untuk melawan wanita di dalam diri saya, orang yang ingin membiarkan Anda menyentuh setiap inci tubuh saya, tetapi saya belum siap."
        scene expression ("images/episode12/334.webp") with dissolve
        toby "Apakah Anda pikir Anda akan pernah menjadi?"
        scene expression ("images/episode12/335.webp") with dissolve
        charlotte "Demi kewarasan saya, saya harap saya akan melakukannya, karena Anda membunuh saya, tetapi pada saat yang sama saya tidak dapat mengabaikan fakta bahwa saya adalah [mother] dan kami tidak boleh melakukan hal -hal ini."
        scene expression ("images/episode12/334.webp") with dissolve
        toby "Saya mengerti dan saya pikir Anda benar."
        toby "Saya harus pergi sekarang."
        scene expression ("images/episode12/336.webp") with dissolve
        charlotte "Beri aku pelukan, pertama."
        scene expression ("images/episode12/337.webp") with dissolve
        charlotte "Saya maafkan saya tidak bisa memberikan semua yang Anda inginkan."
        toby "Anda tidak perlu meminta maaf. Aku mencintaimu, [mom]."
        charlotte "Aku mencintaimu, sayangku [son]."
        scene expression ("images/episode12/338.webp") with dissolve
        toby "Nah, nikmati matahari dan jangan berbalik. Saya hanya melakukan punggung Anda."
        scene expression ("images/episode12/339.webp") with dissolve
        charlotte "Hargai tipnya."
        $ unlockMemory(persistent.memory_44)
        $ renpy.end_replay()

    return

label episode12_massage_charlotte_choices:
    menu:
        "{i} mata {/i}" if "mata" not in ep12_charlotte_likes:
            $ ep12_charlotte_likes.append("eyes")
            scene expression ("images/episode12/304.webp") with dissolve
            toby "Saya benar -benar berpikir Anda memiliki mata yang indah. Saya suka warna kuning-hijau itu."
            toby "Tapi lebih dari itu, saya suka bagaimana terkadang saya tersesat di dalamnya. Saya terus menatap dan saya merasa bisa melanjutkan selamanya."
            toby "Anda memiliki tampilan yang sangat penuh kasih."
            scene expression ("images/episode12/305.webp") with dissolve
            charlotte "Anda benar -benar mencoba membuat saya tersipu, bukan?"
            toby "Apakah ini berhasil?"
            charlotte "Ada lagi?"
            call episode12_massage_charlotte_choices from _call_episode12_massage_charlotte_choices_1

        "{i} hidung {/i}" if "hidung" not in ep12_charlotte_likes:
            $ ep12_charlotte_likes.append("nose")
            scene expression ("images/episode12/306.webp") with dissolve
            toby "Hidung Anda sempurna. Ini sangat lucu, tetapi pada saat yang sama, saya tidak tahu caranya, itu bahkan terlihat seksi."
            scene expression ("images/episode12/303.webp") with dissolve
            charlotte "Seksi? Apa yang bisa seksi tentang hidung?"
            toby "Bentuknya. Mungkin saja apa yang membuat media sosial membuat kami percaya, tetapi bentuk hidung Anda sempurna. Ada banyak wanita yang akan membayar banyak uang untuk hidung seperti milik Anda."
            charlotte "Saya akan mengingatnya jika seseorang meminta saya untuk menjadi model hidung."
            toby "Anda mengolok -olok saya."
            charlotte "Maaf, hanya saja saya tidak terbiasa dihujani dengan pujian. Jadi? Ada lagi?"
            call episode12_massage_charlotte_choices from _call_episode12_massage_charlotte_choices_2

        "{i} bibir {/i}" if "bibir" not in ep12_charlotte_likes:
            $ ep12_charlotte_likes.append("lips")
            scene expression ("images/episode12/307.webp") with dissolve
            toby "Bibir Ya Tuhan, aku mencintai bibirmu."
            charlotte "Anda hanya mengatakan itu karena Anda berharap untuk ciuman lain, tetapi Anda berjanji kepada Anda."
            toby "Saya berjanji untuk mencoba, tetapi bukan itu yang saya maksud."
            toby "Ya, saya suka bagaimana perasaan bibir Anda di bibir saya, tetapi yang saya sukai dari mereka adalah seberapa penuh, lezat, lembut, simetris."
            scene expression ("images/episode12/308.webp") with dissolve
            charlotte "Bagus. Anda bisa berhenti berbohong dan mencium mereka."
            toby "Saya pikir Anda ingin saya berperilaku."
            charlotte "Datang saja ke sini, sebelum saya berubah pikiran."
            scene expression ("images/episode12/309.webp") with dissolve
            toby "Saya benar. Mereka memang terlihat simetris dan penuh, lembut dan ..."
            charlotte "Diam dan cium aku sudah."

            show ep12_310
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode12/310.webp") with dissolve
            hide ep12_310
            toby "Oh, saya hampir lupa. Saya juga suka betapa menyenangkannya lidah Anda."
            charlotte "Berikutnya."

            call episode12_massage_charlotte_choices from _call_episode12_massage_charlotte_choices_3

        "{i} dada {/i}" if "dada" not in ep12_charlotte_likes:
            $ ep12_charlotte_likes.append("chest")
            scene expression ("images/episode12/311.webp") with dissolve
            toby "Nah ada dadamu."
            charlotte "Saya pikir kami melewati titik di mana Anda perlu menggunakan nama yang berbeda untuk payudara saya. Saya yakin itu yang Anda maksud, bukan dada saya yang sebenarnya."
            toby "Anda benar tentang itu. Saya sangat menyukai payudara Anda. Mereka seperti ukuran yang sempurna, bagaimana mereka pas di tangan saya, terutama ketika saya memerasnya sambil memberi Anda pijatan."
            scene expression ("images/episode12/312.webp") with dissolve
            charlotte "Maksud Anda saat Anda menerapkan tabir surya."
            toby "Iya benar sekali."
            charlotte "Anda mengatakan itu, tetapi Anda tidak menaruh tabir surya pada mereka hari ini. Bagaimana jika saya ingin berbalik? Saya akan membakar mereka."
            scene expression ("images/episode12/313.webp") with dissolve
            toby "Aku selalu bisa mencium boo-boo."
            charlotte "Anda seperti itu, tidak akan Anda."
            scene expression ("images/episode12/314.webp") with dissolve
            toby "Ya, saya tahu saya akan melakukannya."
            charlotte "{size=12}{color=#FDCA6E}* moaning slightly *{/color}{/size}\nToo bad. That's not going to happen anytime soon."
            scene expression ("images/episode12/315_1.webp") with dissolve
            toby "Saya bisa bersabar saat dibutuhkan."
            scene expression ("images/episode12/315_2.webp") with dissolve
            charlotte "{size=12}{color=#FDCA6E}* moaning slightly *{/color}{/size}\nI can see that."
            scene expression ("images/episode12/316.webp") with dissolve
            charlotte "Saya pikir Anda telah menerapkan tabir surya yang cukup."
            toby "Ya, Anda mungkin benar."
            scene expression ("images/episode12/317.webp") with dissolve
            charlotte "Apakah ada yang lain?"
            call episode12_massage_charlotte_choices from _call_episode12_massage_charlotte_choices_4

        "{i} ass {/i}" if "pantat" not in ep12_charlotte_likes:
            $ ep12_charlotte_likes.append("ass")
            scene expression ("images/episode12/318.webp") with dissolve
            toby "Anda memiliki pantat bulat besar ini, yang tampak bagus dalam gaun ketat, celana jeans, tapi bercinta, ketika Anda memakai bikini, itu adalah akhir dari saya."
            scene expression ("images/episode12/319.webp") with dissolve
            toby "Sangat menarik dan keras. Itu sempurna."
            toby "Saya ingat ketika saya pertama kali melihat Anda dalam gaun emas itu, ketika kami pergi ke bar itu dan bermain biliar. Tuhan, yang bisa saya lakukan hanyalah menatap betapa cantiknya pantat Anda sebenarnya."
            scene expression ("images/episode12/320.webp") with dissolve
            charlotte "Jadi, itulah mengapa Anda kalah?"
            toby "Saya cukup yakin. Lain kali Anda mengenakan tas sampah."
            charlotte "Tas lateks yang ketat?"
            toby "Anda akan berlayar perairan berbahaya di sini."
            scene expression ("images/episode12/303.webp") with dissolve
            charlotte "Bagus. Apakah ada yang lain?"

            call episode12_massage_charlotte_choices from _call_episode12_massage_charlotte_choices_5

        "{i} kaki {/i}" if "kaki" not in ep12_charlotte_likes:
            $ ep12_charlotte_likes.append("legs")
            scene expression ("images/episode12/321.webp") with dissolve
            toby "Kaki pembunuh Anda."
            charlotte "Anda sudah mengatakan kaki."
            toby "Bukan salahku, kau memiliki kaki yang sempurna."
            scene expression ("images/episode12/312.webp") with dissolve
            charlotte "Jika itu masalahnya, mungkin saya harus mulai mengenakan lebih banyak rok."
            toby "Tolong lakukan itu."
            scene expression ("images/episode12/303.webp") with dissolve
            charlotte "Saya akan memikirkannya. Sementara itu saya suka dihujani dengan pujian."

            call episode12_massage_charlotte_choices from _call_episode12_massage_charlotte_choices_6

        "{i} kaki {/i}"(csq="Aktifkan fetish kaki") if "kaki" not in ep12_charlotte_likes:
            $ foot_fetish = True
            $ ep12_charlotte_likes.append("feet")

            scene expression ("images/episode12/302.webp") with dissolve
            toby "Sejujurnya, saya sangat suka kaki Anda."
            charlotte "Ya Tuhan, aku mengacaukanmu. Anda memiliki fetish kaki sekarang?"
            toby "Saya tidak tahu, mungkin."
            toby "Tapi saya sangat suka bentuk, ukuran, betapa mengkilapnya telapak tangan Anda, panjang jari kaki Anda, bagaimana Anda selalu merawat kuku Anda bahkan ketika Anda tidak memakai cat kuku."
            scene expression ("images/episode12/303.webp") with dissolve
            charlotte "Anda tidak akan mengisap jari kaki saya, kan?"
            toby "Jangan khawatir, [mom]. Aku hanya memberimu pijatan."
            charlotte "Maksud Anda membantu saya dengan tabir surya saya."
            toby "Ya. Itu!"

            charlotte "Ada lagi?"
            call episode12_massage_charlotte_choices from _call_episode12_massage_charlotte_choices_7
        "{i} Lanjutkan {/i}":

            return

    return

label episode12_patricia_shower:
    stop music fadeout 5.0
    $ progress = 165
    if charlotte_path:
        scene expression ("images/episode12/340.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit. I touched [mom]'s pussy. I can't believe how wet she was.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}God! She's the perfect woman. Why does she have to be my [mother]?{/i}"
        if "lips" in ep12_charlotte_likes:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I love those lips. She kisses so good, but I really want more.{/i}"
        else:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I love everything about her, but fuck I really want more.{/i}"
        scene expression ("images/episode12/341.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should take a shower, calm myself down and get ready for my date with Tris.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck! What am I doing with my life. First I touch my [mother]'s pussy and now I'm going on a date with my [sister].{/i}"
    else:
        scene expression ("images/episode12/340.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should take a shower and get ready for my date with Tris, but I think she's still in the shower.{/i}"
        scene expression ("images/episode12/342.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should wait for her. After our conversation I don't think she'd appreciate me barging in on her while she's taking a shower.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}We both feel the same way about each other, but we agreed on taking things slow until we figure out what the hell is going on.{/i}"

        show screen ui_message("Twenty minutes later") with long_dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode12/343.webp") with dissolve
        hide screen ui_message
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Now she's testing my patience.{/i}"
        scene expression ("images/episode12/341.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Screw it, I'm going in. She's had plenty of time to finish her shower.{/i}"

    label memory_45:
        if _in_replay:
            scene expression ("images/utils/black.png") with dissolve
            menu:
                "Pilih pekerjaan Anda"
                "Agen real estat":
                    $ toby_job = 0
                "Manajer klub":
                    $ toby_job = 1


        scene expression ("images/episode12/344.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode12/345.webp") with dissolve
        patricia "Jika Anda berharap melihat saya telanjang, Anda terlambat."
        scene expression ("images/episode12/346.webp") with dissolve
        toby "Tidak semua orang cabul seperti Anda. Saya hanya ingin mandi, tetapi sepertinya Anda memutuskan untuk membuat diri Anda di rumah di sini."
        scene expression ("images/episode12/347.webp") with dissolve
        patricia "Saya seorang cabul? Apa yang membuatmu berpikir begitu?"
        toby "Nah, Anda orang yang selalu masuk ke saya saat saya mandi berharap melihat saya telanjang."
        patricia "Saya tidak terlalu peduli jika Anda telanjang atau berpakaian, saya benar -benar tidak melihat perbedaan."
        scene expression ("images/episode12/348_1.webp") with dissolve
        toby "Jadi Anda mengatakan bahwa Anda tidak peduli jika saya menanggalkan pakaian sekarang dan mandi?"
        scene expression ("images/episode12/348_2.webp") with dissolve
        patricia "Maksud saya untuk mengatakan bahwa saya tidak bisa peduli. Lagi pula, Anda yang memiliki semua perasaan aneh itu, bukan sebaliknya."
        scene expression ("images/episode12/349.webp") with dissolve
        toby "Jika Anda mengatakannya."
        scene expression ("images/episode12/350.webp") with dissolve
        patricia "Kenapa begitu kecil?"
        scene expression ("images/episode12/351.webp") with dissolve
        toby "Karena saya tidak terangsang atau apapun. Tidak ada alasan untuk mendapatkan kesalahan."
        scene expression ("images/episode12/352.webp") with dissolve
        patricia "Apakah Anda ingin alasan untuk mendapatkan kesalahan?"
        if emma_pissed:
            toby "Seperti halnya saya menyukai permainan kecil kami, saya tidak benar -benar dalam mood. Saya mengalami pagi yang buruk."
            patricia "Apa yang telah terjadi?"
            toby "Saya bertarung dengan seseorang."
            patricia "Anda bertarung dengan Emma?"
            toby "Itu tidak masalah siapa. Aku benar -benar tidak dalam mood."
        else:
            toby "Seperti halnya saya menyukai permainan kecil kami, saya tidak benar -benar dalam mood."
            patricia "Apa yang telah terjadi?"
            toby "Aku hanya membenci bola biru."
        scene expression ("images/episode12/353.webp") with dissolve
        patricia "Saya mengerti."
        scene expression ("images/episode12/354.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        patricia "Ups. Sepertinya handuk saya jatuh. Burukku, aku sangat canggung."

        scene expression ("images/episode12/355.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode12/356.webp") with dissolve
        patricia "Dan sepertinya seseorang bangun. Apakah itu buruk juga, atau Anda buruk? Saya tidak begitu yakin bagaimana cara kerjanya."

        if toby_job == 0:
            scene expression ("images/episode12/357.webp") with dissolve
            toby "Sungguh, [sis]? Aku baru saja memberitahumu. Mengapa Anda selalu harus seperti itu?"
            toby "Ya, saya mengerti. Itu lucu. Saya terangsang setiap kali saya melihat Anda telanjang. Anda mungkin berpikir ini lucu dan memvalidasi seberapa tampan Anda. Tapi aku benar -benar tidak ingin bola biru."
            toby "Sekarang bisakah Anda keluar agar saya bisa mandi dan berurusan dengan situasi ini?Anda benar -benar membutuhkan saya untuk mengatakannya? Anda cantik. Anda memiliki tubuh yang indah."
            scene expression ("images/episode12/359.webp") with dissolve
            patricia "Saya minta maaf. Saya tidak berpikir itu akan mengganggu Anda. Kami selalu tertawa pada akhirnya."
        else:
            scene expression ("images/episode12/358.webp") with dissolve
            toby "Benarkah [sis]? Apakah Anda tuli? Aku baru saja memberitahumu. Mengapa Anda harus menjadi bocah manja?"
            toby "Apakah Anda benar -benar merasa lucu memberi saya bola biru? Aku memberitahumu. Saya tidak dalam mood. Apakah ini benar -benar bagaimana Anda perlu mendapatkan validasi bahwa Anda adalah wanita yang tampan?"
            toby "Ya. Anda cantik. Anda memiliki tubuh yang cantik. Anda seksi, tetapi Anda perlu mengerti bahwa tidak berarti tidak."
            toby "Jadi keluarkan saja dari sini dan biarkan aku menyentak dengan tenang."
            scene expression ("images/episode12/359.webp") with dissolve
            patricia "Saya minta maaf. Aku tidak berpikir kamu akan marah padaku. Kami selalu tertawa pada akhirnya."

        scene expression ("images/episode12/360.webp") with dissolve
        toby "Dan kemungkinan besar kita akan menertawakan ini malam ini atau apa pun, tapi aku benar -benar tidak suka mendapatkan boner aneh di sekitarmu. Cukup buruk kita memiliki perasaan ini terhadap satu sama lain."
        patricia "Tidak bisakah Anda melakukannya dengan cepat dan dilakukan dengan itu? Itu tidak bisa seburuk yang Anda lakukan."
        toby "Saya tidak mengatakan itu buruk atau bagus, tetapi saya tidak memiliki telepon saya sehingga akan membutuhkan waktu lama untuk cum dan selain itu, saya tidak benar -benar mendapatkan banyak kesenangan dari tangan saya sendirian."
        scene expression ("images/episode12/361.webp") with dissolve
        patricia "Dapatkah saya membantu Anda dengan cara tertentu, tanpa, Anda tahu, melakukan apa pun yang tidak kami lakukan?"
        if toby_job == 0:
            toby "Tidak, Anda tidak bisa membantu saya. Tolong pergi saja."
            patricia "Saya tidak tahu apakah itu membantu, tetapi saya bisa berdiri di sini telanjang dan Anda dapat melakukan hal Anda menatap saya."
            toby "Saya menghargai itu, tetapi saya tidak akan menyentak menatap Anda. Ini akan benar -benar canggung jika kita saling menatap mata. Jika Anda ingin membantu saya, maka cobalah untuk tidak membuat saya semua bekerja."
            scene expression ("images/episode12/362.webp") with dissolve
            patricia "Maaf. Saya tidak bermaksud. Saya hanya berpikir itu lucu dan menyenangkan bahwa kami memiliki hal aneh kami sendiri."
        else:
            toby "Tanpa kami berhubungan seks, meniup saya, atau menyentak saya? Tidak. Tidak ada yang bisa Anda lakukan selain pergi."
            patricia "Saya tidak tahu apakah itu membantu, tetapi saya bisa berdiri di sini telanjang dan Anda dapat melakukan hal Anda menatap saya."
            toby "Sama seperti saya menghargai tawaran itu, bahwa \ 'akan menjadi sangat canggung jika kita saling memandang di mata. Jika Anda benar -benar ingin membantu saya, maka cobalah untuk tidak membuat saya semua bekerja."
            scene expression ("images/episode12/362.webp") with dissolve
            patricia "Saya minta maaf. Aku tidak bermaksud membuatmu marah padaku. Saya hanya berpikir itu lucu dan menyenangkan bahwa kami memiliki hal aneh kami sendiri."

        patricia "Ngomong -ngomong, saya akan mengerti jika Anda tidak ingin pergi bersamaku malam ini setelah ini."
        scene expression ("images/episode12/363.webp") with dissolve
        toby "Jangan seperti itu, [sis]. Ya, mungkin saya bereaksi berlebihan sedikit, tetapi ini tidak ada hubungannya dengan apa yang kita bicarakan. Toleransi alkohol Anda terlalu rendah dan kami perlu mengerjakannya."
        toby "Aku tidak akan berubah pikiran tentang pergi bersamamu karena ini."
        scene expression ("images/episode12/364.webp") with dissolve
        patricia "Terima kasih!"
        toby "Tidak masalah. Sekarang, saya benar -benar harus berurusan dengan situasi saya, jadi jika Anda bisa pergi, jadi kami dapat mencoba membuat situasi canggung ini kurang canggung, itu akan menjadi hebat."
        scene expression ("images/episode12/365.webp") with dissolve
        patricia "Tidak bisa kamu ..."
        toby "Bisakah i?"
        scene expression ("images/episode12/366.webp") with dissolve
        patricia "Lupakan. Itu bodoh."
        toby "Lebih bodoh dari kita berdua telanjang di kamar mandi?"
        patricia "Jauh lebih buruk dari itu."
        toby "Sekarang Anda membuat saya penasaran."
        scene expression ("images/episode12/365.webp") with dissolve
        patricia "Jadi saya merasa tidak enak karena memberi Anda bola biru, atau apa pun yang Anda sebut dan saya melihat sesuatu di internet yang mungkin dapat membantu Anda."
        toby "Saya mendengarkan."
        patricia "Saya pikir itu disebut assjob. Anda menggunakan pipi pantat saya untuk membantu Anda menyelesaikan lebih cepat dan dengan cara itu kami tidak harus saling memandang di mata dan pada dasarnya saya tidak menyentuh apa pun yang tidak seharusnya saya lakukan."
        scene expression ("images/episode12/367.webp") with dissolve
        toby "Ya, itu bisa berhasil. Tapi apakah Anda yakin Anda baik -baik saja dengan ini? Anda menyadari bahwa kami harus hidup dengan ini setelahnya, kan?"
        if ep7_tris_gallery:
            patricia "Yah, itu tidak seperti ini adalah satu -satunya hal yang aneh di antara kita. Ingat saat Anda tersentak di foto saya? Itu juga sangat aneh dan saya belajar bagaimana hidup dengannya."
        else:
            patricia "Yah, itu tidak seperti ini adalah satu -satunya hal yang aneh di antara kita."
        patricia "Selain itu, untuk Anda, saya hanya akan menjadi bagian dari pantat, Anda hanya melihat pantat saya dan bagi saya itu seperti pijatan. Seseorang memijat pipi pantatku."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck. I can't believe what my little [sister] is suggesting. Can't say I dislike the idea, but fuck, how this will affect our relationship?{/i}"
        scene expression ("images/episode12/368.webp") with dissolve
        toby "Oke, tetapi jika Anda mulai merasa tidak nyaman, Anda memberi tahu saya dan saya akan berhenti."
        patricia "Dan kita tidak pernah membicarakannya lagi?"
        toby "Dan kami tidak pernah membicarakannya lagi."
        scene expression ("images/episode12/369.webp") with dissolve
        patricia "Bagaimana saya harus berdiri?"
        toby "Saya kira jika Anda sedikit bersandar pada wastafel, itu seharusnya baik -baik saja, tetapi saya menanyakan sekali lagi, apakah Anda yakin Anda menginginkan ini?"
        scene expression ("images/episode12/370.webp") with dissolve
        patricia "Saya yakin saya ingin Anda merasa lebih baik. Anda selalu begitu baik untuk saya dan saya menyebalkan dengan semua menggoda, jadi saya pikir itu hanya adil."
        if toby_job == 0:
            toby "Seperti halnya saya menghargai ini, jika Anda tidak mau, Anda tidak harus melakukannya."
            patricia "Diam dan menempelkan ayam Anda di antara asscheeks saya."
        scene expression ("images/episode12/371.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck me. I can't believe I'm going to do this. Look at this perfect ass and I'm going to hump it.{/i}"
        scene expression ("images/episode12/372.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Her ass feels great. Her asscheeks are so soft and firm at the same time.{/i}"
        patricia "Kami tidak punya waktu sepanjang hari. Cukup buruk [mom] adalah rumah. Saya tidak ingin dia melihat kami seperti ini."

        show ep12_373
        toby "Jika suatu saat Anda ingin saya berhenti, beri tahu saya."
        patricia "Jangan khawatir. Tidak apa -apa."
        $ ui.saybehavior()
        $ ui.interact()
        patricia "Apakah setidaknya terasa baik?"
        toby "Rasanya sangat bagus."
        patricia "Saya senang mendengarnya, tetapi Anda bisa mempercepat dan menyelesaikannya dengan cepat?"
        scene expression ("images/episode12/373.webp")
        hide ep12_373

        show ep12_374
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck. I can't believe how good this feels. I can't believe I'm fucking my [sister]'s asscheeks.{/i}"
        patricia "{size=12}{color=#FDCA6E}* moaning slightly *{/color}{/size}\nMhmmm."
        patricia "{size=12}{color=#FDCA6E}* moaning slightly *{/color}{/size}\nDoes my moaning help?"
        toby "Ya, tapi cobalah untuk tidak terlalu keras. Seperti yang Anda katakan, ini bukan yang kami inginkan [mom] menangkap kami."
        patricia "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes... You're right."
        scene expression ("images/episode12/374.webp")
        hide ep12_374

        show ep12_375
        patricia "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nYes [toby!c], yes! Like that."
        patricia "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nWhat are girls supposed to say during this?"
        toby "Jangan memikirkannya, katakan saja apa pun yang terlintas dalam pikiran Anda."
        patricia "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nGod, this is the best ass massage ever."
        toby "Pijat?"
        patricia "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes. You forgot? I was supposed to think about it as being a massage and you focus only on my ass."
        toby "Ya, Anda benar."
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode12/375.webp")
        hide ep12_375

        show ep12_376
        $ ui.saybehavior()
        $ ui.interact()
        patricia "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nDo you like it?"
        toby "Ya, rasanya sangat enak."
        patricia "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nDo you like my ass? Don't you think it's too small?"
        toby "Kecil? Apakah Anda bercanda? Pantatmu benar -benar sempurna."
        patricia "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nThank you."
        patricia "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nJust like that, [bro]. Focus on my ass."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I shouldn't look at her and just focus on her ass, but fuck, I really want to see her pretty face when she moans.{/i}"
        scene expression ("images/episode12/376.webp")
        hide ep12_376

        show ep12_377
        $ ui.saybehavior()
        $ ui.interact()
        patricia "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYou weren't supposed to look at me."
        toby "Sulit untuk tidak melihat Anda saat Anda sangat cantik."
        patricia "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nYes, yes, yes! Right there [toby!c]."
        patricia "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nAre you close?"
        toby "Sangat."
        if toby_job == 0:
            toby "Bisakah saya menyelesaikan di punggung Anda?"
            patricia "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nYes! Finish on my back!"
        else:
            toby "Saya akan pergi ke cum."
        patricia "Cum di punggung saya, [toby!c]. Cum pada saya!"
        scene expression ("images/episode12/377.webp")
        hide ep12_377

        scene expression ("images/episode12/378.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        with flash
        with flash
        toby "Saya cumming."

        $ unlockImage(persistent.patricia_25)
        scene expression ("images/episode12/379.webp") with dissolve:
            yalign 0.0
            linear 10.0 yalign 1.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode12/380.webp") with dissolve
        patricia "..."
        scene expression ("images/episode12/381.webp") with dissolve
        patricia "Saya pikir saya harus pergi. Anda perlu mandi."
        scene expression ("images/episode12/382.webp") with dissolve
        patricia "Dan saya akan membutuhkan ini untuk menghapus punggung saya."
        scene expression ("images/episode12/383.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()

        $ unlockMemory(persistent.memory_45)
        $ renpy.end_replay()



    scene expression ("images/episode12/384.webp") with dissolve
    patricia "Jam berapa saya harus siap?"
    toby "Umm ... ayo katakan 8:30."
    patricia "Besar."
    scene expression ("images/episode12/385.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I can't believe what just happened and on top of that, it was actually her idea.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And then she acted like nothing happened.{/i}"
    scene expression ("images/episode12/386.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck! This is not going to end well.{/i}"

    scene expression ("images/episode12/387.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode12/388.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode12/389.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode12/390.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode12/391.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if charlotte_path:
        scene expression ("images/episode12/392.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode12/393.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    scene expression ("images/episode12/394.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode12/395.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode12/396.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode12/397.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()


    return

label episode12_patricia_date:
    $ progress = 166
    show screen ui_message("Later that day") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/398.webp") with dissolve
    hide screen ui_message
    toby "Hei, [sis]. Apakah kamu siap?"
    scene expression ("images/episode12/399.webp") with dissolve
    patricia "Sesaat."
    scene expression ("images/episode12/400.webp") with dissolve
    toby "Kamu terlihat hebat."
    scene expression ("images/episode12/401.webp") with dissolve
    patricia "Terima kasih!"
    scene expression ("images/episode12/400.webp") with dissolve
    toby "Apakah Anda baik -baik saja setelah apa yang terjadi?"
    scene expression ("images/episode12/402.webp") with dissolve
    patricia "Mengapa saya tidak? Sesuatu terjadi?"
    toby "Tidak ada yang terjadi, saya hanya ..."
    patricia "Tepat. Tidak ada yang terjadi dan kami tidak membicarakan apa pun."
    scene expression ("images/episode12/403_1.webp") with dissolve
    patricia "Jadi? Kemana kita akan pergi?"
    scene expression ("images/episode12/403_2.webp") with dissolve
    toby "Ini adalah bar yang saya temukan beberapa minggu yang lalu. Bahkan memiliki meja biliar jika Anda merasa cukup berani."
    scene expression ("images/episode12/403_1.webp") with dissolve
    patricia "That's not my game. I thought I was really good at it, till I was out with [mom] one day and she said, \"Oh look, a pool table. Let's play\"."
    scene expression ("images/episode12/404_1.webp") with dissolve
    patricia "Dan saya benar -benar sombong, mengatakan kepadanya bahwa saya tidak ingin mempermalukannya dan sebagainya. Coba tebak? Saya bangkrut dan itu adalah satu -satunya tembakan saya. Dia menjalankan meja."
    toby "Jangan khawatir, dia melakukan hal yang persis sama padaku."
    scene expression ("images/episode12/404_2.webp") with dissolve
    patricia "Dia buruk [mother]."
    toby "Yup. Dia tidak memiliki belas kasihan."
    scene expression ("images/episode12/405_0.webp") with dissolve
    charlotte "Siapa yang buruk [mother]?"
    scene expression ("images/episode12/406.webp") with dissolve
    patricia "Anda. Kami hanya berbicara tentang bagaimana Anda mengalahkan pantat kami di kolam renang."
    scene expression ("images/episode12/405.webp") with dissolve
    charlotte "Anda pergi bermain biliar?"
    scene expression ("images/episode12/407.webp") with dissolve
    toby "Tidak. Sebenarnya, kami berdua ingin keluar dari permainan."
    scene expression ("images/episode12/406.webp") with dissolve
    patricia "Karena kamu. Anda tidak memiliki belas kasihan."
    scene expression ("images/episode12/405.webp") with dissolve
    charlotte "Yah, saya tidak tahu saya mengangkat dua pussies."
    scene expression ("images/episode12/408.webp") with dissolve
    patricia "Ya, itulah tepatnya bagaimana dia berbicara kepada saya, ketika dia meninggalkan saya untuk mati di meja biliar."
    toby "Saya pikir saya ingat dia mengatakan sesuatu yang serupa."
    toby "Dia semacam pengganggu, bukan?"
    patricia "Tepat. Itu kata yang tepat. Saya tidak yakin apa kata terbaik untuk menggambarkannya, tapi ya. Dia seorang pengganggu."
    scene expression ("images/episode12/409.webp") with dissolve
    charlotte "Saya bukan pengganggu. Faktanya, jika Anda mau, saya bisa berubah dan ikut dengan Anda. Anda akan melihat saya bukan pengganggu."
    scene expression ("images/episode12/410.webp") with dissolve
    patricia "Terlambat untuk itu. Kami tidak pergi dengan pengganggu. Selamat tinggal."
    scene expression ("images/episode12/411.webp") with fade

    patricia "Bisakah saya mengemudi?"
    toby "Tidak."
    patricia "Silakan. Anda selalu mengemudi. Tolong izinkan saya mengemudi kali ini."
    scene expression ("images/episode12/412.webp") with dissolve
    toby "Ini adalah pelajaran satu. Anda tidak minum dan mengemudi, seperti yang dilakukan seseorang kemarin.Saya juga tidak mengemudi. Kami pergi minum. Saya tidak mempertaruhkan kedua kehidupan kita."
    scene expression ("images/episode12/413.webp") with dissolve
    patricia "Ummm. Saya tidak tahu apa yang Anda bicarakan, tapi ya. Pelajaran yang dipelajari."
    scene expression ("images/episode12/414.webp") with dissolve
    toby "Jadi? Apa kabar hari ini?"
    patricia "Anda selalu memulai kencan Anda seperti ini?"
    if toby_job == 0:
        if ep12_wordAssociation == 0 and ep12_stripWordAssociation == True:
            toby "Ya, Anda benar. Mari kita bicara tentang apa yang terjadi di bak mandi air panas. Maksudku, Tuhan, kamu sangat buruk dalam permainan itu. Tidak bisa percaya Anda benar -benar setuju untuk bermain strip Word Association. Kamu sangat telanjang."
        else:
            toby "Ya, Anda benar. Mari kita bicara tentang apa yang terjadi setelah bak mandi air panas, di kamar mandi."
    else:
        toby "Ya, Anda benar. Apa warna celana Anda?"
    scene expression ("images/episode12/415.webp") with dissolve
    patricia "Ya ... jadi hariku!"
    patricia "Yah saya bangun pagi ini dan pergi dengan [mom] untuk mendapatkan bahan makanan dan kami berbicara tentang betapa sempurna cuaca untuk hari pantai, tetapi dia tidak ingin pergi ke pantai, jadi kami memutuskan untuk meletakkan semua kerja keras Anda menjadikan kami halaman terbaik untuk digunakan dengan baik."
    toby "Saya hampir merasa terhormat."
    scene expression ("images/episode12/416.webp") with dissolve
    patricia "Anda seharusnya, karena [mom] menggunakan bak mandi air panas Anda sepenuhnya."
    toby "Maksudku, dia sudah menjaga rumah terlalu bersih.Jujur saja, apa lagi yang bisa dia lakukan sepanjang hari. Lagi pula, dia tidak bekerja, dia hanya duduk di rumah. Apa lagi yang bisa dia lakukan?"
    patricia "Saya benar -benar tidak mendapatkan mengapa Anda dan [dad] tidak membiarkannya bekerja. Dia harus keluar dari rumah."
    toby "Dia [mom] kami. Dia cukup dilakukan untuk kita, sekarang akan menjadi saat yang tepat untuk melakukan sesuatu untuknya. Nah, dia bisa keluar dari rumah. Untuk membiarkannya rileks.Pergi berbelanja, jalan -jalan. Aku tidak tahu."
    scene expression ("images/episode12/417.webp") with dissolve
    patricia "Pergi berbelanja dengan uang apa? [dad!c] tidak memberinya uang receh. Bahkan untuk bahan makanan. Saya pikir dia menggunakan hampir semua simpanannya."
    toby "Mengapa dia tidak bertanya padaku? Saya akan selalu memberinya beberapa."
    patricia "Benar-benar? Apakah Anda mengharapkannya untuk meminta uang kepadanya [son]?"
    toby "Ya, Anda benar. Dia tidak akan pernah meminta saya uang."
    scene expression ("images/episode12/418.webp") with dissolve
    patricia "Ngomong -ngomong, kemana kita pergi? Bar apa yang disebut ini?"
    toby "Nah, kami hampir sampai di sana. Lima menit atasan."
    scene expression ("images/episode12/419.webp") with fade
    toby "Di sinilah kita."
    scene expression ("images/episode12/420.webp") with dissolve
    patricia "Jadi bagaimana cara kerja pelatihan alkohol ini?"
    toby "Aku akan menunjukkan kepadamu sebentar lagi. Mari kita ambil meja."
    scene expression ("images/episode12/421.webp") with dissolve
    toby "Saya akan segera kembali."
    scene expression ("images/episode12/422.webp") with dissolve
    barmaid "Apa yang bisa saya dapatkan dari Anda?"
    toby "Selamat malam. Empat bir ringan dengan lemon, sebotol wiski dan dua gelas."
    scene expression ("images/episode12/424.webp") with dissolve
    barmaid "Tentu, saya akan membawa semuanya ke meja Anda dalam satu menit."
    scene expression ("images/episode12/425.webp") with dissolve
    toby "Terima kasih! Saya akan berada di kamar sebelah."
    scene expression ("images/episode12/430.webp") with fade
    patricia "Anda memesan bahkan tanpa bertanya kepada saya apa yang saya inginkan?"
    toby "Cukup banyak."
    patricia "Bagaimana jika saya tidak menyukai apa yang Anda pesan?"
    toby "Lalu aku akan meminum semuanya sendirian."
    scene expression ("images/episode12/431.webp") with dissolve
    patricia "Saya tahu Anda adalah pria yang sempurna."
    scene expression ("images/episode12/432.webp") with dissolve
    barmaid "Ini minuman Anda."
    scene expression ("images/episode12/433.webp") with dissolve
    toby "Terima kasih, Nona."
    scene expression ("images/episode12/435.webp") with dissolve
    patricia "Dengan serius? Lemon dalam bir? Apa saya? Dua belas?"
    scene expression ("images/episode12/437_cheers.webp") with dissolve
    toby "Tidak, tapi Anda mabuk seperti anak berusia dua belas tahun."
    scene expression ("images/episode12/438.webp") with dissolve
    patricia "Saya pikir wiski itu untuk Anda."
    scene expression ("images/episode12/439.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/437_smile.webp") with dissolve
    toby "Tidak. Saya minum apa yang Anda minum. Begitulah cara kerjanya."
    scene expression ("images/episode12/437_curious.webp") with dissolve
    toby "Jadi? Bagaimana sekolahmu? Apakah Anda mendapatkan teman baru?"
    scene expression ("images/episode12/436_normal.webp") with dissolve
    patricia "Tidak terlalu. Setelah semua itu hanya minggu pertama, tetapi semakin menarik. Ada beberapa gadis baik di beberapa kelas saya."
    scene expression ("images/episode12/437_smile.webp") with dissolve
    toby "Senang mendengarnya. Saya mendengar bahwa di perguruan tinggi Anda membuat kenangan dan teman baik terbaik, jadi saya yakin Anda akan baik -baik saja."
    scene expression ("images/episode12/436_smile.webp") with dissolve
    patricia "Ya, tapi biasanya itu berlaku untuk mereka yang tinggal di asrama. Sebagai seorang komuter, yah, itu sedikit berbeda."
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Jangan khawatir. Anda juga akan berteman baik. Selain itu, Anda senang bergaul."
    scene expression ("images/episode12/437_beer.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/437_smile.webp") with dissolve
    toby "Terutama setelah Anda tahu cara minum secara bertanggung jawab."
    scene expression ("images/episode12/436_beer.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/436_smile.webp") with dissolve
    patricia "Sebenarnya ini tidak terasa terlalu buruk."
    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "Menurut Anda mengapa itu buruk?"
    scene expression ("images/episode12/436_awkward.webp") with dissolve
    patricia "I don't know. But I remember back in Highschool, everybody made fun of putting lemon in a beer, calling it a \"little girl's drink\"."
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Jangan dengarkan mereka. Lemon sedikit merobohkan kekerasan dan membuatnya terasa lebih enak."
    scene expression ("images/episode12/436_curious.webp") with dissolve
    patricia "Jadi, bagaimana pekerjaan Anda?"
    scene expression ("images/episode12/437_smile.webp") with dissolve
    toby "Benar -benar bagus. Saya sangat beruntung mendapatkan pekerjaan bergaji yang baik. Saya sudah berpikir saya akan segera membeli mobil."
    scene expression ("images/episode12/436_surprised.webp") with dissolve
    patricia "Benar-benar? Itu luar biasa! Mobil apa?"
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Saya belum yakin, tapi saya berpikir karena saya masih muda dan cuaca di sini sangat bagus, mungkin saya bisa pergi untuk convertible."
    scene expression ("images/episode12/436_curious.webp") with dissolve
    patricia "Saya tidak tahu merek apa itu."
    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "Ini bukan merek. Itu gaya. Itu adalah salah satu tempat di mana bagian atas turun."
    scene expression ("images/episode12/436_awkward.webp") with dissolve
    patricia "Oh ... aku tahu itu."
    scene expression ("images/episode12/436_beer.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/437_beer.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "Saya yakin."
    scene expression ("images/episode12/436_smile.webp") with dissolve
    patricia "Warna apa?"
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Saya tidak tahu, mungkin hitam."
    scene expression ("images/episode12/436_normal.webp") with dissolve
    patricia "Bagaimana dengan merah?"
    scene expression ("images/episode12/437_curious.webp") with dissolve
    toby "Mengapa saya membeli mobil merah?"
    scene expression ("images/episode12/436_smile.webp") with dissolve
    patricia "Karena saya terlihat lebih baik mengendarai mobil merah."
    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "Apa yang membuat Anda berpikir saya akan membiarkan Anda mengendarainya?"
    scene expression ("images/episode12/436_pouty.webp") with dissolve
    patricia "Karena Anda tidak dapat mengatakan tidak pada wajah ini."
    scene expression ("images/episode12/437_smile.webp") with dissolve
    toby "Apakah kamu sangat yakin?"
    scene expression ("images/episode12/436_pouty.webp") with dissolve
    patricia "Ya. Ini adalah teori yang terbukti."
    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "Ayo coba. Anda tidak akan mengendarai mobil saya."
    scene expression ("images/episode12/437_smile.webp") with dissolve
    toby "Itu lebih mudah dari yang saya harapkan."
    scene expression ("images/episode12/436_tongue.webp") with dissolve
    patricia "Idiot!"
    scene expression ("images/episode12/437_beer.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/437_smile.webp") with dissolve
    toby "Saya tahu, saya tahu. Aku pun mencintaimu."
    scene expression ("images/episode12/436_curious.webp") with dissolve
    patricia "Anda berbicara dengan bir Anda? Karena saya cukup yakin itu tidak ditujukan kepada saya, karena jika ya, saya akan merasakan cinta Anda."
    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "Anda merasa cukup cinta saya hari ini di kamar mandi."
    scene expression ("images/episode12/436_ashamed.webp") with dissolve
    patricia "Kita seharusnya membicarakan hal itu. Saya melakukan itu untuk Anda dan sekarang Anda mengolok -olok saya."
    scene expression ("images/episode12/436_cool.webp") with dissolve
    patricia "Tidak, Pak. Bukan itu yang kita mainkan. Saya yakin berharap rasanya enak karena saya tidak akan pernah membiarkan Anda melakukannya lagi. Pernah!"
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Sejujurnya, rasanya cukup hebat."
    scene expression ("images/episode12/436_curious.webp") with dissolve
    patricia "Lebih baik dari seks?"
    scene expression ("images/episode12/437_smile.webp") with dissolve
    toby "Jangan konyol. Tidak ada yang terasa lebih baik dari seks."
    scene expression ("images/episode12/436_curious.webp") with dissolve
    patricia "Bagaimana rasanya seks?"
    scene expression ("images/episode12/437_smile.webp") with dissolve
    toby "Aku tahu. Mari kita mainkan game."
    scene expression ("images/episode12/436_normal.webp") with dissolve
    patricia "Pertama, Anda menjawab pertanyaan saya."
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Itu permainannya. Kami masing -masing mengajukan lima pertanyaan dan Anda menjawab atau minum."
    scene expression ("images/episode12/436_smile.webp") with dissolve
    patricia "Kedengarannya bagus untukku."
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Jadi untuk menjawab pertanyaan pertama Anda. Saya tidak tahu bagaimana rasanya bagi seorang wanita, tetapi bagi kita, pada awalnya adalah perasaan senang. Anda merasakan jantung Anda berdetak lebih cepat dan kemudian Anda merasa otot Anda tegang."
    scene expression ("images/episode12/437_smile.webp") with dissolve
    toby "Penis menjadi sangat sensitif dan kemudian ketika Anda mencapai orgasme, Anda merasa seperti pelepasan di seluruh tubuh Anda."
    scene expression ("images/episode12/436_normal.webp") with dissolve
    patricia "Kedengarannya bagus."
    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "Yah rasanya enak, tidak hanya kedengarannya bagus."
    scene expression ("images/episode12/436_thinking.webp") with dissolve
    patricia "Oke, pertanyaan kedua saya."
    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "That's not how the game works, because I'll answer all your questions firsat and then you'll be like, \"I don't feel like playing anymore\". Anda mengajukan pertanyaan lalu saya mengajukan satu dan sebagainya."
    scene expression ("images/episode12/436_meh.webp") with dissolve
    patricia "Membosankan, tapi apa pun."
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Do you remember when we played rock/paper/scissors and you had to answer a question, but [mom] called and you never did?"
    scene expression ("images/episode12/436_laugh.webp") with dissolve
    patricia "Apa yang membuat Anda berpikir bahwa saya akan menjawabnya sekarang?"
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Karena kamu harus?"
    scene expression ("images/episode12/436_beer.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/436_laugh.webp") with dissolve
    patricia "Sepertinya giliranku sekarang."
    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "Anda tidak mengizinkan saya mengajukan pertanyaan."
    scene expression ("images/episode12/436_normal.webp") with dissolve
    patricia "Anda akan bertanya kepada saya siapa yang saya pikirkan ketika saya masturbasi dan tidak ada jalan di neraka saya menjawab pertanyaan itu."
    scene expression ("images/episode12/437_smile.webp") with dissolve
    toby "Tidak. Itu bukan pertanyaan, jadi masih giliranku."
    scene expression ("images/episode12/436_laugh.webp") with dissolve
    patricia "Anda tidak bisa memainkan kartu itu. Kami berdua tahu itu pertanyaannya. Jadi sekarang pertanyaan kedua saya."
    scene expression ("images/episode12/436_curious.webp") with dissolve
    patricia "Berapa banyak gadis yang berhubungan seks dengan Anda."
    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "You already asked me that question when we played rock/paper/scissors."
    scene expression ("images/episode12/436_laugh.webp") with dissolve
    $ progress = 167
    patricia "Ya, tapi itu hampir 2 bulan yang lalu. Banyak hal bisa terjadi dalam dua bulan."
    if darlene_path == False and katrina_path == False and lauren_path == False and lisa_path == False and sheila_path == False:
        scene expression ("images/episode12/437_normal.webp") with dissolve
        toby "Jawabannya masih sama. Hanya tiga"
        scene expression ("images/episode12/436_smile.webp") with dissolve
        patricia "Saya selalu berpikir Anda adalah semacam Casanova, tetapi itu tampaknya tidak terjadi. Anda benar -benar mengejutkan saya."
    else:
        scene expression ("images/episode12/437_beer.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        if emma_break == False:
            scene expression ("images/episode12/436_surprised.webp") with dissolve
            patricia "Tidak mungkin ... Anda berselingkuh di Emma? Anda penipu!"
        else:
            scene expression ("images/episode12/436_surprised.webp") with dissolve
            patricia "Kamu anak kotor dan kotor. Berapa banyak?"
            scene expression ("images/episode12/437_smile.webp") with dissolve
            toby "Kira Anda tidak akan pernah tahu."

    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "Sekarang, pertanyaan kedua saya."
    scene expression ("images/episode12/437_curious.webp") with dissolve
    toby "Jenis porno apa yang Anda tonton?"
    scene expression ("images/episode12/436_laugh.webp") with dissolve
    patricia "Apa yang membuatmu berpikir aku menonton film porno."
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Silakan. Semua orang melakukannya."
    scene expression ("images/episode12/436_ashamed.webp") with dissolve
    patricia "Aku tidak tahu. Porno normal? Satu pria, satu wanita?"
    scene expression ("images/episode12/437_curious.webp") with dissolve
    toby "Ada tag khusus? Maksud saya, apa yang Anda cari?"
    scene expression ("images/episode12/436_laugh.webp") with dissolve
    patricia "Tidak. Itu pertanyaan lain."
    scene expression ("images/episode12/437_surprised.webp") with dissolve
    toby "Anda memberi saya jawaban omong kosong. Saya cukup yakin Anda tidak suka menonton hewan berhubungan seks.Itu tidak. Ini pertanyaan yang sama. Anda baru saja tidak menjawab yang pertama."
    scene expression ("images/episode12/436_laugh.webp") with dissolve
    patricia "Nah, beberapa dari mereka bertindak seperti binatang."
    scene expression ("images/episode12/437_curious.webp") with dissolve
    toby "Jadi Anda menonton seks kasar?"
    scene expression ("images/episode12/436_normal.webp") with dissolve
    patricia "TIDAK! Saya tidak suka itu. Saya tidak suka ketika mereka menggunakan wanita seperti sepotong daging."
    scene expression ("images/episode12/437_curious.webp") with dissolve
    toby "Jadi? Apa yang kamu tonton?"
    scene expression ("images/episode12/436_beer.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/436_laugh.webp") with dissolve
    patricia "Giliran saya sekarang."
    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "Anda tidak bisa terus minum. Anda harus menjawab beberapa pertanyaan."
    scene expression ("images/episode12/436_smile.webp") with dissolve
    patricia "Perhatikan aku."
    scene expression ("images/episode12/437_curious.webp") with dissolve
    toby "Apakah itu benar -benar seburuk itu?"
    scene expression ("images/episode12/436_thinking.webp") with dissolve
    patricia "Mari kita lihat. Pertanyaan ketiga saya. Ini pasti bagus."
    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "Threesome? Anal? Lesbian?"
    scene expression ("images/episode12/436_laugh.webp") with dissolve
    patricia "Pertanyaan ketiga saya adalah ..."
    scene expression ("images/episode12/437_curious.webp") with dissolve
    toby "Creampie? Amatir? Onani?"
    scene expression ("images/episode12/436_normal.webp") with dissolve
    patricia "Tidak. Saya tidak akan menjawab. Saya sudah minum."
    scene expression ("images/episode12/437_flirty.webp") with dissolve
    toby "Bdsm, oral, cumshots?"
    scene expression ("images/episode12/436_laugh.webp") with dissolve
    patricia "Anda menyadari bahwa semua yang Anda lakukan mengonfirmasi betapa mesum Anda."
    scene expression ("images/episode12/437_curious.webp") with dissolve
    toby "Porno inses? Keluarga tiri?"
    scene expression ("images/episode12/436_ashamed.webp") with dissolve
    patricia "Ummm ..."
    scene expression ("images/episode12/436_awkward.webp") with dissolve
    patricia "Mengapa Anda menatap mata saya sore ini di kamar mandi?"
    scene expression ("images/episode12/437_surprised.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... That's it. She's watching taboo porn.{/i}"
    scene expression ("images/episode12/436_normal.webp") with dissolve
    patricia "Berhentilah memikirkan kategori porno dan jawab pertanyaan saya, karena saya tidak akan menjawab Anda."
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Saya tidak penasaran lagi. Saya pikir saya memiliki jawaban saya."
    scene expression ("images/episode12/436_laugh.webp") with dissolve
    patricia "Tidak. Ini bukan porno inses atau apa pun yang Anda katakan. Aku tidak sakit sepertimu."
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Jika Anda mengatakannya. Jadi untuk menjawab pertanyaan Anda ..."
    scene expression ("images/episode12/437_beer.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/436_pissed.webp") with dissolve
    patricia "Hei ... itu tidak adil."
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Saya akan menjawab pertanyaan Anda ketika Anda mulai menjawab saya."
    scene expression ("images/episode12/436_ashamed.webp") with dissolve
    patricia "Bagus. Saya akan menjawab pertanyaan Anda sebelumnya."
    scene expression ("images/episode12/437_cool.webp") with dissolve
    toby "Terlambat, saya tidak lagi tertarik dengan pertanyaan itu dan selain itu, Anda sudah minum, jadi kami beralih ke pertanyaan berikutnya."
    scene expression ("images/episode12/436_pissed.webp") with dissolve
    patricia "Idiot!"
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Kami berdua tahu bahwa saya merasa baik setelah assjob di kamar mandi, tetapi bagaimana perasaan Anda?"
    scene expression ("images/episode12/436_curious.webp") with dissolve
    patricia "Bisakah saya minum?"
    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "Anda bisa, tetapi kemudian saya juga akan minum."
    scene expression ("images/episode12/436_ashamed.webp") with dissolve
    patricia "Itu membuat saya merasa diinginkan."
    scene expression ("images/episode12/437_smile.webp") with dissolve
    toby "Dan Anda suka merasa diinginkan?"
    scene expression ("images/episode12/436_laugh.webp") with dissolve
    patricia "Apakah Anda yakin ingin itu menjadi pertanyaan keempat Anda, karena saya akan menjawabnya."
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Tidak ... mari kita dengar yang keempat terlebih dahulu."
    scene expression ("images/episode12/436_curious.webp") with dissolve
    patricia "Jika Anda dapat memilih apa yang saya kenakan sekarang, apa yang akan Anda pilih?"
    scene expression ("images/episode12/437_flirty.webp") with dissolve
    toby "Tentang waktu Anda mengajukan pertanyaan yang layak dijawab. Yah, saya pikir saya akan menggunakan rok kulit hitam pendek tanpa celana dalam dan atasan tembus pandang hitam yang tidak meninggalkan banyak imajinasi."
    scene expression ("images/episode12/436_surprised.webp") with dissolve
    patricia "Di sekitar orang -orang ini?"
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Ya, Anda benar. Aku akan membiarkanmu memakai bra merah di bawah bagian atas itu, tapi rok pendek tanpa celana dalam."
    scene expression ("images/episode12/436_flirty.webp") with dissolve
    patricia "Anda keriting."
    scene expression ("images/episode12/437_flirty.webp") with dissolve
    toby "Oh, dan choker renda merah dengan anting -anting lingkaran emas besar."
    scene expression ("images/episode12/436_laugh.webp") with dissolve
    patricia "Anda berpakaian sangat slutty. Saya tahu Anda punya sesuatu untuk gadis -gadis slutty."
    scene expression ("images/episode12/437_flirty.webp") with dissolve
    toby "Atau mungkin saya hanya ingin membuat Anda merasa tidak nyaman. Anda lucu saat Anda keluar dari zona nyaman Anda."
    scene expression ("images/episode12/436_meh.webp") with dissolve
    patricia "Wow, kamu sangat menyenangkan!"
    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "Giliranku. Pernahkah Anda berpikir untuk membeli mainan seks?"
    scene expression ("images/episode12/436_normal.webp") with dissolve
    patricia "Ya. Dildo merah muda kecil, tapi saya tidak ingin mitra pertama saya menjadi mainan. Mungkin di masa depan."
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Nah, jika keperawanan Anda sangat berarti bagi Anda, Anda bisa mencoba anal."
    scene expression ("images/episode12/436_awkward.webp") with dissolve
    patricia "Dan pertanyaan Anda adalah?"
    scene expression ("images/episode12/437_laugh.webp") with dissolve
    toby "Pernahkah Anda berpikir untuk mencoba anal?"
    scene expression ("images/episode12/436_laugh.webp") with dissolve
    if emma_break == False:
        patricia "Eww ... tidak! Saya bukan Emma."
        scene expression ("images/episode12/437_surprised.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What does that mean? Does she know me and Emma tried anal?{/i}"
        scene expression ("images/episode12/437_curious.webp") with dissolve
        toby "Arti?"
        scene expression ("images/episode12/436_awkward.webp") with dissolve
        patricia "Yah dia tampak seperti seorang gadis yang akan mencoba sesuatu seperti itu."
        scene expression ("images/episode12/437_thinking.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's acting strange.{/i}"
    else:
        patricia "TIDAK! Bukan itu tujuan pantatku, kau cabul!"
    scene expression ("images/episode12/436_smile.webp") with dissolve
    patricia "Jadi pertanyaan terakhir saya."
    scene expression ("images/episode12/436_thinking.webp") with dissolve
    patricia "Ini harus bagus."
    scene expression ("images/episode12/437_normal.webp") with dissolve
    toby "Bawa."
    scene expression ("images/episode12/436_flirty.webp") with dissolve
    patricia "Apa yang akan Anda lakukan kepada saya jika saya tidak bisa mengatakan tidak dan saya bukan [sister] Anda."
    scene expression ("images/episode12/437_flirty.webp") with dissolve
    toby "Nah, karena Anda masih perawan, saya tidak akan melakukan sesuatu yang terlalu gila, karena saya tidak akan pernah ingin menyakiti Anda. Tapi saya mungkin akan meninggalkan bar ini sekarang dan membawa Anda ke hotel yang bagus."
    scene expression ("images/episode12/440.webp") with dissolve
    toby "Kami akan naik ke tempat tidur dan aku akan mencium setiap inci tubuhmu yang cantik. Saya mungkin akan mulai dengan leher sempurna Anda."
    scene expression ("images/episode12/441.webp") with dissolve
    toby "Lalu aku sedikit memeras payudaramu, karena aku harus berkata, aku suka bagaimana kamu mengerang."
    scene expression ("images/episode12/442.webp") with dissolve
    toby "Lalu aku sedikit mengisap putingmu yang sudah keras."
    scene expression ("images/episode12/443.webp") with dissolve
    toby "Kemudian pindah ke perut Anda, menjilati dan berciuman bergerak menuju hadiah nyata."
    scene expression ("images/episode12/444.webp") with dissolve
    toby "Lalu aku akan mencapai vaginamu. Saya akan sangat dekat dengan itu sehingga saya hampir bisa merasakannya."
    scene expression ("images/episode12/436_horny.webp") with dissolve
    patricia "{size=12}{color=#FDCA6E}* moaning slightly *{/color}{/size}\n{i}Ummm... Let's move on to your last question.{/i}"
    scene expression ("images/episode12/437_smile.webp") with dissolve
    toby "Anda tidak ingin mendengar bagaimana ini berakhir?"
    scene expression ("images/episode12/436_smile.webp") with dissolve
    patricia "Tidak. Saya pikir saya punya ide yang bagus."
    scene expression ("images/episode12/437_flirty.webp") with dissolve
    toby "Jika saya bukan [brother] Anda, apakah Anda ingin semua yang baru saja saya katakan?"
    scene expression ("images/episode12/436_beer.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode12/437_surprised.webp") with dissolve
    toby "Anda membuat saya kotor."
    scene expression ("images/episode12/436_laugh.webp") with dissolve
    patricia "Mari pulang."
    scene expression ("images/episode12/445.webp") with dissolve
    toby "Kami masih memiliki sebotol wiski."
    scene expression ("images/episode12/446.webp") with dissolve
    patricia "Aku sudah mabuk. Anda dapat membawa pulang botol itu dan kami akan meminumnya di bak mandi air panas."
    scene expression ("images/episode12/447.webp") with dissolve
    toby "Oke kalau begitu. Biarkan pulang."
    scene expression ("images/episode12/448.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
