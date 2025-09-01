image ep4_215 = Movie(play="video/episode4/215.webm", loop = True)
image ep4_221 = Movie(play="video/episode4/221.webm", loop = True)
image ep4_223 = Movie(play="video/episode4/223.webm", loop = True)
image ep4_275 = Movie(play="video/episode4/275.webm", loop = True)
image ep4_276 = Movie(play="video/episode4/276.webm", loop = True)
image ep4_301 = Movie(play="video/episode4/301.webm", loop = True)
image ep4_302 = Movie(play="video/episode4/302.webm", loop = True)
image ep4_303 = Movie(play="video/episode4/303.webm", loop = True)
image ep4_304 = Movie(play="video/episode4/304.webm", loop = True)
image ep4_306 = Movie(play="video/episode4/306.webm", loop = True)
image ep4_307 = Movie(play="video/episode4/307.webm", loop = True)
image ep4_308 = Movie(play="video/episode4/308.webm", loop = True)
image ep4_309 = Movie(play="video/episode4/309.webm", loop = True)
image ep4_330 = Movie(play="video/episode4/330.webm", loop = True)
image ep4_331 = Movie(play="video/episode4/331.webm", loop = True)
image ep4_332 = Movie(play="video/episode4/332.webm", loop = True)
image ep4_333 = Movie(play="video/episode4/333.webm", loop = True)
image ep4_335 = Movie(play="video/episode4/335.webm", loop = True)
image ep4_336 = Movie(play="video/episode4/336.webm", loop = True)
image ep4_337 = Movie(play="video/episode4/337.webm", loop = True)
image ep4_338 = Movie(play="video/episode4/338.webm", loop = True)

label episode4:
    stop music fadeout 4.0
    if lisa_path == False and lauren_path == False:
        if lisa_rel >= 1:
            $ lisa_path = True
        else:
            $ lauren_path = True

    scene expression ("images/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(1, 4) with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_newEpisode

    $ progress = 51
    show screen ui_message("Friday") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message

    call episode4_friday_morning_tris_bath from _call_episode4_friday_morning_tris_bath
    call episode4_friday_morning_erwin from _call_episode4_friday_morning_erwin
    call episode4_friday_morning_shower from _call_episode4_friday_morning_shower
    call episode4_friday_morning_breakfast from _call_episode4_friday_morning_breakfast
    call episode4_friday_gym from _call_episode4_friday_gym

    if toby_job == 0:
        call episode4_friday_realEstate from _call_episode4_friday_realEstate
        if sheila_path:
            call episode4_sheila_apartment from _call_episode4_sheila_apartment
    else:
        call episode4_friday_club from _call_episode4_friday_club

    call episode4_saturday_morning from _call_episode4_saturday_morning

    call episode4_saturday_date from _call_episode4_saturday_date

    return



label episode4_friday_morning_tris_bath:
    label memory_10:

        scene expression ("images/episode4/001.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck my bladder! I drank way too much water last night.{/i}"
        scene expression ("images/episode4/002.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I feel like I'm going to explode!{/i}"
        scene expression ("images/episode4/003.webp") with dissolve
        patricia "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n[toby!u]!!! I'm taking a shower."
        scene expression ("images/episode4/004.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.saybehavior()
        $ ui.interact()

        toby "Maaf [sis]. Saya akan cepat. Saya benar -benar perlu buang air kecil!"
        scene expression ("images/episode4/005.webp") with dissolve
        patricia "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nCan't you see I'm naked here?"
        toby "Tidak, saya tidak melihat dan saya berjanji untuk tidak melakukannya! Saya benar -benar perlu pergi!"
        scene expression ("images/episode4/006.webp") with dissolve
        patricia "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nOUT! NOW!"
        toby "Berhenti berteriak. Saya baru saja bangun dan saya hanya berjanji untuk tidak melihat!"
        scene expression ("images/episode4/007_1.webp") with dissolve
        patricia "Apakah kamu serius? Anda benar -benar akan buang air kecil saat saya sedang mandi?"
        scene expression ("images/episode4/007_2.webp") with dissolve
        toby "Saya akan cepat, tetapi tidak mungkin saya bisa menahannya lagi!"
        scene expression ("images/episode4/007_1.webp") with dissolve
        patricia "Kencing di dalam botol."
        scene expression ("images/episode4/008.webp") with dissolve
        toby "Saya tidak dapat menemukan botol dengan lubang yang cukup besar!"
        patricia "Anda kotor!"
        scene expression ("images/episode4/009.webp") with dissolve
        patricia "Hanya tidak mengintip atau aku akan memotongnya!"
        toby "Aku sudah memberitahumu bahwa aku tidak akan melihat, jadi kamu juga tidak boleh!"
        scene expression ("images/episode4/010.webp") with dissolve
        patricia "Ini tidak seperti aku belum pernah melihatnya saat kita menonton film, dan sejujurnya tidak banyak yang bisa dilihat!"
        toby "Jika Anda mengatakannya!"
        scene expression ("images/episode4/011.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm almost done. I can't believe I just did this.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What was I thinking? Peeing while my [sister] is taking a shower.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's literally naked 2 feet away from me.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Should I take a peek?{/i}"
        menu:
            "{i} [JGR] Lakukan {/i}"(csq="Tris +1 & Galeri Gambar"):
                $ patricia_rel += 1
                $ unlockImage(persistent.patricia_09)
                scene expression ("images/episode4/012.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is she trying to look at my cock? What the hell is she doing?{/i}"
                scene expression ("images/episode4/013.webp") with dissolve
                pause 1
                scene expression ("images/episode4/014.webp") with long_dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode4/012.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Of course I'm getting a boner now, knowing that my little [sister] is looking at my cock. What is wrong with me!{/i}"
                scene expression ("images/episode4/015.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She noticed. Shit!{/i}"
                scene expression ("images/episode4/016.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit! Shit! Shit! We made eye contact!{/i}"
                scene expression ("images/episode4/017.webp") with dissolve
                patricia "Saya pikir Anda mengatakan Anda tidak akan terlihat."
                toby "Dan Anda mengatakan bahwa Anda tidak akan terlihat juga!"
                patricia "Saya hanya memastikan Anda tepat sasaran!"
                toby "Dan saya memastikan Anda tidak ketinggalan tempat!"
                scene expression ("images/episode4/018.webp") with dissolve
                patricia "Keluar! Sekarang!"
                $ unlockMemory(persistent.memory_10)
            "{i} don \ 't do it {/i}" if not _in_replay:
                pass
        scene expression ("images/episode4/019.webp") with dissolve
        toby "Terima kasih telah mengizinkan saya kencing."
        patricia "Sepertinya aku bisa menghentikanmu!"
        scene expression ("images/episode4/020.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}That was a little awkward, but at least I'm not going to explode!{/i}"
        $ renpy.end_replay()
    return

label episode4_friday_morning_erwin:

    $ progress = 52
    scene expression ("images/episode4/021.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why did he have to come downstairs now? I really don't want to talk to him after everything he did to [mom].{/i}"
    scene expression ("images/episode4/022.webp") with dissolve
    erwin "Juara pagi! Anda bangun pagi!"
    scene expression ("images/episode4/023.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm just going to ignore him. It's too early to start a fight.{/i}"
    scene expression ("images/episode4/024.webp") with dissolve
    erwin "Benar-benar? Begitulah cara Anda memperlakukan [dad] Anda?"
    erwin "Sudah tumbuh. Anda tidak bisa marah pada saya hanya karena saya tidak suka terlambat!"
    scene expression ("images/episode4/025.webp") with dissolve
    toby "Anda benar -benar berpikir saya gila karena Anda berteriak pada kami karena terlambat 10 menit?"
    toby "Anda adalah delusi, orang tua!"
    scene expression ("images/episode4/026.webp") with dissolve
    erwin "Lalu apa masalahmu?"
    scene expression ("images/episode4/027.webp") with dissolve
    toby "Apakah Anda benar -benar ingin tahu apa masalah saya?"
    erwin "Biarkan saya menebak. Anda tidak mendapatkan tunjangan Anda?"
    toby "Masalah saya adalah Anda memperlakukan [mom] seperti kotoran, tidak hanya secara pribadi, tetapi di depan umum!"
    toby "Masalah saya adalah fakta bahwa Anda membuatnya menjadi pelacur di depan mitra bisnis Anda!"
    toby "Wanita yang berada di sisi Anda selama yang Anda ingat. Anda bilang dia pelacur!"
    scene expression ("images/episode4/028.webp") with dissolve
    erwin "Tidak seperti itu. Saya menghormati [mother] Anda dan saya tidak akan mengatakan hal seperti itu tentang dia!"
    toby "Baiklah... Kau benar! Kau mengatakan itu \"Begitulah para jalang itu. Asal kamu beri mereka uang, mereka akan melakukan apa saja untukmu..\""
    erwin "Mungkin saya mabuk. Anda tahu bahwa saya tidak baik dengan alkohol."
    toby "Itu masih belum ada alasan untuk memperlakukannya seperti kotoran! Dia istrimu demi bercinta!"
    scene expression ("images/episode4/029.webp") with dissolve
    erwin "Bahasa, anak muda!"
    toby "Saya akan berbicara bagaimana saya ingin sampai Anda belajar cara menghormati [mom]."
    erwin "Saya mencoba. Saya mencoba menjadi orang yang lebih baik [father] dan suami yang lebih baik, tetapi pekerjaan saya sangat menegangkan akhir -akhir ini."
    scene expression ("images/episode4/030.webp") with dissolve
    toby "Maka Anda adalah bajingan yang beruntung. Karena tidak peduli seberapa besar seorang bajingan Anda, dia tidak ingin menceraikan Anda."
    toby "Siapa yang tahu mengapa!"
    scene expression ("images/episode4/029.webp") with dissolve
    erwin "Demi sake, nak! Berhentilah bersumpah! Saya masih [father] Anda."
    toby "Nah, jika Anda ingin rasa hormat saya maka Anda harus mendapatkannya kembali."
    toby "Pertama -tama Anda perlu belajar cara menghormati [mom]."
    erwin "Tapi aku sangat menghormatinya. Hanya saja aku sangat stres dan kadang -kadang aku membiarkan semuanya padanya, kamu dan bahkan Tris. Saya tidak menginginkannya. Itu hanya bagaimana saya."
    toby "Temui saya pada jam 4 \ 'di gym setempat."

    scene expression ("images/episode4/031.webp") with dissolve
    erwin "Saya tidak punya waktu untuk game. Saya terlalu sibuk!"
    toby "Saya tidak berbicara tentang game. Saya berbicara tentang kemarahan Anda. Anda akan menekan tas meninju sampai Anda tidak memiliki energi lagi untuk berteriak di [mom]."
    toby "Baik dia atau Tris bukan tas tinju Anda!"
    erwin "Saya tidak akan pernah memukul salah satu dari mereka!"
    scene expression ("images/episode4/030.webp") with dissolve
    toby "Terkadang kata -kata lebih menyakitkan, jadi jika Anda benar -benar ingin menyelamatkan pernikahan Anda seperti yang Anda katakan, saya akan menunggu Anda pada jam 4 o \ '. Saya akan mengirimkan lokasi!"
    scene expression ("images/episode4/032.webp") with long_dissolve
    patricia "Tolong beritahu saya bahwa Anda belum berdebat!"
    scene expression ("images/episode4/033.webp") with dissolve
    toby "Tidak, kami tidak! Saya menunggu Anda untuk menyelesaikan kamar mandi Anda!"
    erwin "Dan saya akan bekerja."
    erwin "Semoga harimu menyenangkan anak -anak!"
    scene expression ("images/episode4/034.webp") with dissolve
    patricia "Janji?"
    toby "Jangan khawatir [sis], semuanya akan baik -baik saja!"
    scene expression ("images/episode4/035.webp") with dissolve
    patricia "Aku mencintaimu [toby!c]."
    toby "Aku juga mencintaimu [sis]."
    scene expression ("images/episode4/036.webp") with dissolve
    patricia "Apakah Anda mencuci tangan setelah Anda mengencingi?"
    toby "Seseorang membuat saya pergi secepat mungkin!"
    scene expression ("images/episode4/037.webp") with dissolve
    patricia "Ewww ... kamu kotor!"
    toby "Idiot!"
    scene expression ("images/episode4/038.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    return


label episode4_friday_morning_shower:
    $ progress = 53
    scene expression ("images/episode4/039.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm really curious to see if [dad]'s gonna show up at the gym.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This is the last chance I'm giving him then he's like dead to me.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}He can't talk about [mom] like that.{/i}"
    scene expression ("images/episode4/040.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I love both of them. They are my [parents] but sometimes I feel like they would be better off without each other.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But who knows... We'll see if this will help my [dad].{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}At least for me it did. Whenever I felt an argument with Emma brewing, I went to the gym or the swimming pool to clear my mind.{/i}"
    scene expression ("images/episode4/041.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's just hope it does help, because it will break my heart to see my [parents] get divorced.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Well, maybe I won't feel that bad, but I'm sure Tris will be devastated.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Anyway, I should go find the closest gym.{/i}"


    scene expression ("images/episode4/042.webp") with dissolve
    toby "Bon Appétit!"
    patricia "Terima kasih!"
    toby "Apakah Anda terlambat ke sekolah?"
    patricia "Ini baru 7:10. Sekolah dimulai dalam waktu sekitar 40 menit. Pertanyaan sebenarnya adalah mengapa Anda bangun begitu awal?"
    toby "Benar-benar? Ini baru jam 7 pagi? Saya tidak tahu mengapa saya juga naik terlalu awal."
    scene expression ("images/episode4/043.webp") with dissolve
    patricia "Aku tahu kenapa kamu bangun pagi -pagi sekali!"
    toby "Apakah memberi tahu?"
    patricia "Ini salah satu dari dua opsi!"
    toby "Ah, benarkah? Anda bahkan punya dua opsi?"
    patricia "Anda memiliki kandung kemih kecil!"
    toby "Mari kita dengarkan opsi lainnya."
    scene expression ("images/episode4/044.webp") with dissolve
    patricia "Anda seorang perv yang benar -benar ingin melihat kecilnya [sister] telanjang!"
    toby "Idiot!"

    scene expression ("images/episode4/045.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's put on some clothes and then find the closest gym.{/i}"
    scene expression ("images/episode4/046.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/047.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/048.webp") with dissolve
    toby "Apakah kita akan membuat kebiasaan masuk sementara yang lain telanjang?"
    scene expression ("images/episode4/049.webp") with dissolve
    patricia "Anda memulainya!"
    scene expression ("images/episode4/048.webp") with dissolve
    toby "Sebenarnya, Anda yang masuk saat saya mengambil selfie!"
    scene expression ("images/episode4/049.webp") with dissolve
    patricia "Itu bukan selfie. Itu adalah foto penis!"
    scene expression ("images/episode4/048.webp") with dissolve
    toby "Anda tahu banyak sekali untuk seorang gadis yang belum punya pacar!"
    scene expression ("images/episode4/050.webp") with dissolve
    patricia "Saya seorang perawan, bukan pemalu!"
    scene expression ("images/episode4/051.webp") with dissolve
    toby "Uhum ... apa yang kamu lakukan?"
    scene expression ("images/episode4/050.webp") with dissolve
    patricia "Menunggu Anda selesai berubah sehingga saya bisa bersiap -siap untuk sekolah!"
    scene expression ("images/episode4/051.webp") with dissolve
    toby "Dan kenapa kamu tidak menunggu di luar!?"
    scene expression ("images/episode4/050.webp") with dissolve
    patricia "Saya memiliki pertanyaan yang sama persis pagi ini ketika Anda datang di kamar mandi. Kenapa kamu tidak menunggu di luar!"
    scene expression ("images/episode4/051.webp") with dissolve
    toby "Jadi Anda tidak akan pergi?"
    scene expression ("images/episode4/052.webp") with dissolve
    patricia "Tidak!"
    menu:
        "{i} [JGR] Jadilah Shameless {/i}"(csq="Tris +1"):
            scene expression ("images/episode4/053.webp") with dissolve
            toby "Oke kalau begitu ... aku akan mengabaikanmu sepenuhnya!"
            scene expression ("images/episode4/054.webp") with dissolve
            patricia "Ewww! Anda kotor!"
            scene expression ("images/episode4/055.webp") with dissolve
            toby "Aku menyuruhmu pergi!"
            scene expression ("images/episode4/054.webp") with dissolve
            patricia "Setidaknya Anda bisa berbalik!"
            scene expression ("images/episode4/057.webp") with dissolve
            toby "Terlambat sekarang!"
        "{i} Cobalah untuk diubah tanpa dia melihat Anda! {/i}":

            scene expression ("images/episode4/056.webp") with dissolve
            toby "Moron!"
            scene expression ("images/episode4/052.webp") with dissolve
            patricia "Aku tidak tahu kamu begitu pemalu!"
            scene expression ("images/episode4/056.webp") with dissolve
            toby "Dan saya tidak tahu bahwa Anda adalah orang yang begitu!"
            scene expression ("images/episode4/052.webp") with dissolve
            patricia "Saya bukan orang cabul. Saya baru saja membalas budi!"
            scene expression ("images/episode4/057.webp") with dissolve
            pass
    toby "Saya kira kita tidak begitu berbeda. Saya ingin melihat kecil [sister] telanjang dan Anda juga ingin melihat [brother] telanjang Anda yang lebih tua."
    scene expression ("images/episode4/058.webp") with dissolve
    patricia "Jadi saya benar! Anda bangun supaya Anda bisa mencoba melihat saya telanjang!"
    scene expression ("images/episode4/059.webp") with dissolve
    toby "Dan Anda tidak menyangkal bahwa Anda ingin melihat saya telanjang!"
    scene expression ("images/episode4/060.webp") with dissolve
    patricia "Apa yang sedang kamu lakukan?"
    scene expression ("images/episode4/059.webp") with dissolve
    toby "Umm ... aku hanya mencari gym!"
    scene expression ("images/episode4/060.webp") with dissolve
    patricia "Maksudku ... kenapa kamu masih di sini? Saya perlu bersiap -siap untuk sekolah."
    scene expression ("images/episode4/059.webp") with dissolve
    toby "Anda tidak pergi ketika saya berubah, jadi mengapa saya harus?"
    scene expression ("images/episode4/061.webp") with dissolve
    patricia "Karena ini kamarku. Kamar Anda ada di loteng!"
    toby "[mom!c] mengatakan bahwa kami berbagi ruangan ini sampai loteng selesai, yang membuat kamar ini saya sama seperti milik Anda!"
    scene expression ("images/episode4/062.webp") with dissolve
    patricia "Aku membencimu!"
    scene expression ("images/episode4/063.webp") with dissolve
    toby "Jika saya jadi Anda, saya akan menggunakan tangan saya untuk memegang handuk itu alih -alih memukul saya!"
    scene expression ("images/episode4/064.webp") with dissolve
    patricia "Moron!"
    toby "Aku mencintaimu!"
    scene expression ("images/episode4/065.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see where the closest gym is.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmm... NMR Gym. I wonder what NMR stands for?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}No More Rules. Interesting.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe it's the kind of gym with a bunch of motivational speakers as trainers and bullshit like that.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Jerks who always drone on about the fact that you should leave your routine way of life and get out of your comfort zone.{/i}"
    scene expression ("images/episode4/066.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}As long as it has all the equipment and a punching bag I don't really care about anything else!{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should text [dad] the address!{/i}"

    scene expression ("images/episode4/067_texting.webp") with dissolve
    call sms_sent ("erwin", "Here's the gym's location. Don't be late.", img_icon="images/episode4/067_icon.webp") from _call_sms_sent_8
    call sms_incoming ("erwin", "...") from _call_sms_incoming_10
    scene expression ("images/episode4/067.webp") with dissolve
    hide screen message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}He could have at least said \"OK\". {/i}"

    scene expression ("images/episode4/068.webp") with dissolve
    charlotte "Pagi [toby!c]. Apakah Anda tidur nyenyak?"
    toby "Uhum ... apakah sesuatu terjadi? Anda tampak kesal!"
    charlotte "Ingin menjelaskan mengapa Anda tidak meninggalkan ruangan sehingga [sister] Anda bisa diubah?"
    scene expression ("images/episode4/069.webp") with dissolve
    toby "Oh itu! Saya hanya bermain dengannya!"
    charlotte "Anda beruntung saya mendengar diskusi Anda dengan [father] Anda."
    scene expression ("images/episode4/070.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/071.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck... [mom!c]'s boobs are amazing.{/i}"
    scene expression ("images/episode4/072.webp") with dissolve
    charlotte "Terima kasih telah mencoba menyelamatkan pernikahan saya. Anda yang terbaik [son] yang pernah saya minta!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Did she notice I was staring at her boobs and raise my head?{/i}"
    toby "Tentu [mom]. Saya akan melakukan apapun sehingga Anda bisa bahagia!"
    scene expression ("images/episode4/073.webp") with dissolve
    charlotte "Saya membuat sarapan. Ingin beberapa?"
    toby "Ya tolong!"
    charlotte "Oke kalau begitu. Jangan terlambat!"
    toby "Tentu [mom]!"

    return

label episode4_friday_morning_breakfast:
    $ progress = 54
    scene expression ("images/episode4/074.webp") with long_dissolve
    toby "Hmm ... ada sesuatu yang harum di sini."

    scene expression ("images/episode4/075.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    charlotte "Tunggu saja sampai Anda mencicipinya!"

    scene expression ("images/episode4/076.webp") with dissolve
    toby "Saya hanya bisa membayangkan!"
    scene expression ("images/episode4/077.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the hell is wrong with you. She's your [mother].{/i}"
    scene expression ("images/episode4/078.webp") with dissolve
    charlotte "Jadi sayang ... bagaimana Anda menyukai kota baru ini? Apakah Anda sudah mendapatkan teman baru?"
    scene expression ("images/episode4/079.webp") with dissolve
    toby "Lebih sulit untuk mendapatkan teman baru karena saya tidak di sekolah menengah atau bahkan kuliah, tetapi saya pikir saya akan membuat beberapa teman melalui pekerjaan ini."
    toby "Saya bisa bertemu banyak orang, jadi cepat atau lambat saya akan mendapatkan beberapa teman baru."
    scene expression ("images/episode4/078.webp") with dissolve
    charlotte "Saya senang mendengarnya. Jadi, apakah Anda pernah melihat sesuatu di kota di samping pantai?"
    scene expression ("images/episode4/079.webp") with dissolve
    toby "Selain pergi ke pantai dua kali, saya pergi berjalan dengan Tris di taman di dekatnya."
    scene expression ("images/episode4/080.webp") with dissolve

    charlotte "Tunggu. Apakah Anda mengatakan pantai dua kali?"
    scene expression ("images/episode4/081.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... I shouldn't have said that.{/i}"
    toby "Ya, ya. Saya pergi ke sana kemarin dengan beberapa teman."
    scene expression ("images/episode4/080.webp") with dissolve
    charlotte "Teman dari tempat kerja?"
    scene expression ("images/episode4/081.webp") with dissolve
    toby "Anda bisa mengatakan itu."
    scene expression ("images/episode4/081.webp") with dissolve
    charlotte "Apakah Anda menyembunyikan sesuatu dari [mom] Anda?"
    if toby_job == 0:
        toby "Nah, dua klien mengundang saya ke pantai bersama mereka."
    else:
        toby "Nah, pada hari pertama saya di tempat kerja saya bertemu dengan dua klien ini dan mereka mengundang saya ke pantai."
    scene expression ("images/episode4/082.webp") with dissolve
    charlotte "You put too much emphasis on the word \"client\"."
    charlotte "Saya harap Anda tidak selingkuh dengan Emma dengan salah satu dari mereka, atau keduanya!"
    scene expression ("images/episode4/081.webp") with dissolve
    toby "Siapa bilang mereka perempuan?"
    scene expression ("images/episode4/083.webp") with dissolve
    charlotte "Wajahmu melakukannya. Dikatakan bahwa mereka sangat cantik!"

    if ep3_lieGirls == False:
        scene expression ("images/episode4/084.webp") with dissolve
        toby "Anda tidak perlu khawatir. Saya hanya ingin memberi tahu mereka secara langsung bahwa saya tidak tersedia. Saya ingin memiliki mereka sebagai teman, tetapi mereka perlu tahu saya punya pacar."
        charlotte "Dan bagaimana mereka bereaksi?"
        toby "Itu baik -baik saja. Mereka mengerti."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Understood my ass... I was in deep shit!{/i}"
        charlotte "Saya senang Anda menyelesaikannya!"
    else:
        scene expression ("images/episode4/084.webp") with dissolve
        toby "Berhati -hatilah untuk tidak membakar makanan."
        charlotte "[toby!u] ... itu bukan bagaimana kami membesarkan Anda!"
        toby "Saya tahu [mom]. Saya akan melakukan yang benar oleh semua orang. Jangan khawatir!"

    scene expression ("images/episode4/078.webp") with dissolve
    charlotte "Lihat. Saya tidak menyuruh Anda putus atau tetap bersama Emma. Dia seorang kekasih dan aku menyukainya. Anda tahu itu."
    charlotte "Tetapi jika Anda mulai menyukai gadis lain, hanya adil untuk menghentikan hubungan Anda saat ini sebelum bergerak maju."
    charlotte "Maksud saya, jelas bahwa gadis pertama tidak tepat untuk Anda, karena Anda memiliki mata untuk orang lain."
    scene expression ("images/episode4/085.webp") with dissolve
    charlotte "Saya senang bahwa Anda tidak menyukai [father] Anda, tetapi dalam hal ini, Anda seharusnya."
    charlotte "Saya hanya ingin Anda tahu bahwa saya di sini untuk Anda, jika Anda perlu membicarakan apa pun."
    charlotte "Dan jika Anda akan memulai hubungan baru, saya akan senang bertemu dengannya seperti yang kami lakukan dengan Emma."

    if ep3_lieGirls == False:
        scene expression ("images/episode4/086.webp") with dissolve
        toby "[mom!c] ... Sudah kubilang. Ini baik -baik saja. Tidak ada apa pun di antara saya dan salah satu gadis yang saya temui kemarin."
    else:
        scene expression ("images/episode4/086.webp") with dissolve
        toby "Jangan khawatir [mom]. Anda akan menjadi orang pertama yang tahu apakah saya putus dengan Emma!"

    scene expression ("images/episode4/087.webp") with dissolve
    charlotte "Baik ... Aku tidak akan mengganggumu tentang ini lagi!"
    scene expression ("images/episode4/088_happy.webp") with dissolve
    charlotte "Jadi bagaimana Emma? Sudahkah Anda berbicara dengannya akhir -akhir ini?"
    scene expression ("images/episode4/089_normal.webp") with dissolve
    toby "Nah, kami berbicara kemarin. Dia tidak merasa begitu baik. Dia masuk angin."
    scene expression ("images/episode4/088_flirty.webp") with dissolve
    charlotte "Dia kehilangan panasnya tubuh telanjang Anda?"
    scene expression ("images/episode4/089_surprised.webp") with dissolve
    toby "[mom!u] !!!"
    scene expression ("images/episode4/088_laugh.webp") with dissolve
    charlotte "Apa?! Ini tidak seperti Anda seorang perawan. Kami berdua tahu itu."
    scene expression ("images/episode4/089_awkward.webp") with dissolve
    toby "[mom!u]! Hentikan."
    toby "Dan tidak, Emma tidak masuk angin karena aku tidak ada di sana untuk menghangatkan tempat tidurnya."
    scene expression ("images/episode4/088_happy.webp") with dissolve
    charlotte "Apa kamu yakin?"
    scene expression ("images/episode4/089_normal.webp") with dissolve
    toby "Ya, [mom]. Saya yakin! Kami baik -baik saja."
    scene expression ("images/episode4/088_happy.webp") with dissolve
    charlotte "Saya senang mendengarnya."
    charlotte "Saya hanya ingin Anda tahu bahwa jika Anda merasa seperti Anda kehilangan pacar Anda atau Anda kehilangan sentuhannya dan mungkin tubuhnya yang telanjang, dia bisa datang kapan -kapan. Itu baik -baik saja!"
    scene expression ("images/episode4/088_flirty.webp") with dissolve
    charlotte "Saya tidak punya masalah dengan dia datang!"
    scene expression ("images/episode4/089_awkward.webp") with dissolve
    toby "Terima kasih [mom], tapi saya tidak berpikir itu akan terjadi, kecuali jika Anda akan membiarkan kami berhubungan seks di sofa atau mungkin di tempat tidur yang sama dengan Tris."
    toby "Kami akan mencoba diam!"
    scene expression ("images/episode4/088_surprised.webp") with dissolve
    charlotte "Bagaimana Anda bisa mengatakan sesuatu seperti itu?"
    scene expression ("images/episode4/089_laugh.webp") with dissolve
    toby "Hei, kamu memulainya!"
    toby "Jangan salah paham, saya menghargai Anda mencoba menjadi keren [mom], tetapi jujur saja. Ketika dia berkunjung, saya hanya akan mendapatkan kamar hotel. Benar -benar tidak banyak ruang di sini."
    scene expression ("images/episode4/088_curious.webp") with dissolve
    charlotte "Tapi bagaimana saya akan menikmati kopi pagi saya saat dia mengolok -olok Anda?"
    scene expression ("images/episode4/089_normal.webp") with dissolve
    toby "Ya ... jangan khawatir, kami akan makan sarapan di sini!"
    scene expression ("images/episode4/088_happy.webp") with dissolve
    charlotte "Janji?"
    scene expression ("images/episode4/089_normal.webp") with dissolve
    toby "Janji kelingking!"
    scene expression ("images/episode4/088_flirty.webp") with dissolve
    charlotte "Tidak peduli gadis itu? Anda akan membawanya ke sini untuk sarapan?"
    scene expression ("images/episode4/089_normal.webp") with dissolve
    if ep3_lieGirls == False:
        toby "Hubungan saya dengan Emma solid. Tidak akan ada gadis lain dalam waktu dekat!"
        toby "Jadi ya, setiap pagi kami akan berada di sini bersamamu."
        toby "Senang?"
    else:
        toby "Baik ... Saya akan membawa setiap pacar di sini sehingga Anda dapat bersenang -senang."
        toby "Senang?"
    scene expression ("images/episode4/088_curious.webp") with dissolve
    charlotte "Saya akan mengejar Anda menjawab satu pertanyaan lagi."
    scene expression ("images/episode4/089_normal.webp") with dissolve
    toby "Menembak!"
    scene expression ("images/episode4/088_flirty.webp") with dissolve
    charlotte "Ceritakan tentang gadis -gadis itu?"
    scene expression ("images/episode4/090.webp") with dissolve
    toby "Kita harus makan, sebelum menjadi dingin."
    scene expression ("images/episode4/091.webp") with dissolve
    charlotte "Anda tidak menyenangkan!"
    scene expression ("images/episode4/090.webp") with dissolve
    toby "Dan Anda tidak ada harapan!"
    scene expression ("images/episode4/091.webp") with dissolve
    charlotte "Oh tolong ... apa yang Anda harapkan untuk saya lakukan?"
    charlotte "[dad] Anda selalu bekerja dan itu tidak seperti ketika dia pulang, dia banyak pembicara."
    charlotte "Belum lagi, hidupnya membosankan."
    scene expression ("images/episode4/092.webp") with dissolve
    charlotte "Kehidupan [sister] Anda bahkan lebih membosankan daripada hidup saya."
    charlotte "Anda satu -satunya di rumah ini dengan kehidupan yang menarik."
    scene expression ("images/episode4/090.webp") with dissolve
    toby "Kami tidak ingin makanan menjadi dingin. Saya sangat menghormati pekerjaan Anda, saya menganggap tragedi untuk membiarkan sarapan yang baik ini menjadi dingin."
    scene expression ("images/episode4/092.webp") with dissolve
    charlotte "Aku akan membuatmu yang lain."
    scene expression ("images/episode4/093.webp") with dissolve
    charlotte "Silakan!"
    scene expression ("images/episode4/094.webp") with dissolve
    toby "Bagus."
    charlotte "Aku mencintaimu! Jadi?"
    scene expression ("images/episode4/089_normal.webp") with dissolve
    if ep3_lieGirls == False:
        toby "Hanya untuk menjadi jelas. Saya pergi ke sana hanya untuk memberi tahu mereka bahwa saya punya pacar."
        scene expression ("images/episode4/088_curious.webp") with dissolve
        charlotte "Melihat? Itulah yang tidak saya dapatkan. Mengapa Anda perlu memperjelas hal -hal yang baru saja Anda temui?"
        scene expression ("images/episode4/089_awkward.webp") with dissolve
        toby "Tidak masalah. Anda bertanya tentang gadis -gadis itu!"
    else:
        pass

    toby "Jadi ada Lisa dan Lauren. Mereka berdua datang ke sini untuk kuliah."
    toby "Lisa is blonde with green eyes and Lauren is a red head with light-gray/blue eyes."
    scene expression ("images/episode4/088_flirty.webp") with dissolve
    charlotte "Dan mana yang lebih panas?"
    menu:
        "Telurnya":
            scene expression ("images/episode4/095.webp") with dissolve
            charlotte "Baik ... Anda lapar!"
        "[JGR] Anda yang terpanas dari mereka semua!"(csq="Charlotte +1 & Galeri Gambar"):
            $ charlotte_rel += 1
            $ unlockImage(persistent.charlotte_09)
            scene expression ("images/episode4/095.webp") with dissolve
            charlotte "Anda pasti benar -benar lapar. Saya pikir mata Anda sedang memainkan trik pada Anda!"

    scene expression ("images/episode4/096.webp") with fade
    toby "Terima kasih untuk sarapan!"
    charlotte "Bagaimana?"
    toby "Selain kedinginan? Sangat, sangat bagus!"
    scene expression ("images/episode4/097.webp") with dissolve
    charlotte "Sangat lucu!"
    charlotte "Omong-omong. Apakah Anda sibuk sekarang?"
    toby "Jika Anda berbicara tentang Pilates maka ya, saya sangat sibuk. Jika tidak, maka saya bebas sebagai burung!"
    scene expression ("images/episode4/098.webp") with dissolve
    charlotte "Sempurna, karena saya butuh bantuan untuk membersihkan tempat."
    charlotte "Maksud saya, saya bisa melakukannya sendiri, tetapi mengapa saya harus ketika saya memiliki pria yang kuat di sekitar rumah?"
    scene expression ("images/episode4/099.webp") with dissolve
    toby "Beruntung aku!"
    scene expression ("images/episode4/098.webp") with dissolve
    charlotte "Oh, jangan bertindak seperti Anda tidak ingin menghabiskan waktu dengan kesepian Anda [mother]."
    scene expression ("images/episode4/099.webp") with dissolve
    toby "Dan sekarang dia berperan sebagai korban."
    scene expression ("images/episode4/100.webp") with dissolve
    toby "Jadi apa yang Anda butuhkan untuk saya lakukan?"
    charlotte "Saya akan membersihkan tempat itu dan Anda bisa menyedot debu!"
    toby "Oke kalau begitu ... mari kita mulai!"
    scene expression ("images/episode4/101.webp") with dissolve
    charlotte "Terima kasih banyak [toby!c]."
    scene expression ("images/episode4/102.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/103.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/104.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/105.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    if toby_job == 0:
        scene expression ("images/episode4/106.webp") with dissolve
        play sound "audio/fx/Cell Phone Ring Sound Effect - Free Sound Effects.mp3"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I almost forgot I have a boss now.{/i}"
        scene expression ("images/episode4/108.webp") with dissolve
        darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Hi [toby!c]. How are you today?{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Hi ma'am. I'm fine thank you. How are you?{/i}"
        darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I'm very fine except that I am missing my most trustworthy employee.{/i}"
        darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}So, what do you say? Think you can come by the office at 6 o'clock? You need to sign some papers and I need to talk to you about some apartments.{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Of course. I'll be there.{/i}"
        darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Perfect... See you soon then.{/i}"
    else:
        scene expression ("images/episode4/107.webp") with dissolve
        play sound "audio/fx/Cell Phone Ring Sound Effect - Free Sound Effects.mp3"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Someone's in trouble.{/i}"
        scene expression ("images/episode4/108.webp") with dissolve
        katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Hi sexy. How is my favorite employee?{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Hi ma'am. I'm fine. I was just helping [mom] out.{/i}"
        katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Such a good boy.{/i}"
        katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I need you tonight at the club around 6 o'clock.{/i}"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Sure. I'll be there.{/i}"
        katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}See you soon sexy.{/i}"

    scene expression ("images/episode4/109.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I guess I'm going to work today!{/i}"

    return


label episode4_friday_gym:

    $ progress = 55
    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/110.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This must be the No More Rules gym.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should get a membership and wait for [dad] to come.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}If he's not too busy being stupid.{/i}"
    scene expression ("images/episode4/111.webp") with dissolve
    cashier "Halo Pak. Bagaimana saya bisa membantu Anda?"
    toby "Halo, saya ingin mendapatkan keanggotaan selama sebulan."
    cashier "Pertama kali di gym kami?"
    scene expression ("images/episode4/112.webp") with dissolve
    toby "Ya, saya baru saja pindah ke lingkungan."
    cashier "Itu sangat keren. Apakah Anda memiliki ID pada Anda?"
    toby "Uhum, tentu saja. Tapi mengapa Anda membutuhkan ID saya?"
    cashier "Oh, kamu tidak tahu? Gym ini hanya orang dewasa sehingga saya perlu memverifikasi usia Anda dan menggunakan informasi untuk membuat kartu keanggotaan Anda."
    scene expression ("images/episode4/113.webp") with dissolve
    toby "Menarik. Saya pikir ini adalah gym pertama yang saya dengar hanya untuk orang dewasa."
    cashier "Ya, kami kehilangan kasing beberapa tahun yang lalu, karena seseorang ingin menggunakan ruang ganti wanita, jadi kami akhirnya menjadikannya ruang ganti dan mandi bersama."
    scene expression ("images/episode4/114.webp") with dissolve
    toby "Saya mengerti. Dan apakah wanita masih datang mengetahui bahwa mereka berbagi ruang ganti?"
    cashier "Yah, kami memang memiliki penurunan keanggotaan, tetapi kami kembali berdiri dan ada aturan tidak tertulis di antara para anggota."
    cashier "Para pria menerima kunci untuk satu sisi ruang ganti dan para wanita menerima kunci untuk yang lain."
    toby "Dan Anda tidak bisa melihat apa -apa?"
    scene expression ("images/episode4/115.webp") with dissolve
    cashier "Anda bisa, tetapi tidak sopan untuk menatap, bukan?"
    toby "Ya, Anda benar."
    scene expression ("images/episode4/116.webp") with dissolve
    cashier "Ini ID dan kartu keanggotaan Anda."
    toby "Terima kasih."
    toby "Satu pertanyaan lagi, dapatkah Anda membayar biaya untuk mendapatkan tamu? Saya menunggu seseorang dan saya tidak yakin dia akan sering datang."
    cashier "Anda baik -baik saja. Kebijakan kami adalah anggota dapat membawa satu tamu secara gratis."
    toby "Besar! Terima kasih atas semuanya."
    scene expression ("images/episode4/117.webp") with dissolve
    toby "Aku hanya akan pergi dan menunggunya di sana."
    scene expression ("images/episode4/118.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm not sure bringing [dad] to a gym like this is the best idea, given his situation with [mom].{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But I guess it's too late to back out now.{/i}"
    show screen ui_message("20 minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/119.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yup... He ghosted me. That's it. He doesn't deserve my help or respect.{/i}"
    scene expression ("images/episode4/120.webp") with dissolve
    toby "Saya kira dia tidak datang. Ruang ganti ada di lorong?"
    cashier "Ya. Seperti apa teman Anda? Jika dia datang, saya akan memberi tahu dia di mana Anda berada."
    toby "Jangan khawatir. Dia tidak datang. Dia kadang -kadang melakukan itu."
    cashier "Saya mengerti."
    cashier "Nah, nikmati latihan Anda, [toby!c]."
    scene expression ("images/episode4/121.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should hurry so I can get to work at 6:00.{/i}"
    scene expression ("images/episode4/122.webp") with dissolve
    erwin "Maaf ma \ 'am. Saya seharusnya bertemu dengan seorang pemuda di sini."
    cashier "Anda harus menjadi teman [toby!c]."
    erwin "Ya. I \ M -nya [father]."
    cashier "Dia hanya pergi ke ruang ganti."
    scene expression ("images/episode4/123.webp") with dissolve
    toby "Hai [dad]. Anda terlambat!"
    erwin "Apa yang bisa saya katakan, tidak mudah bagi saya untuk keluar dari pekerjaan untuk pergi ke gym di tengah hari."
    erwin "Dan jika Anda berpikir ini mungkin membantu saya harus mencobanya."
    toby "Bagus. Biarkan masuk!"
    erwin "Jangan aku harus membayar terlebih dahulu?"
    cashier "Jangan khawatir, Pak. Semuanya telah diurus oleh [son] Anda."
    scene expression ("images/episode4/124.webp") with dissolve
    erwin "Apakah Anda mencoba untuk mendapatkan sisi baik saya?"
    toby "Tidak. Itu gratis!"
    erwin "..."
    scene expression ("images/episode4/125.webp") with dissolve
    erwin "Bagaimana hari Anda sejauh ini [son]?"
    toby "Itu baik -baik saja. Saya membantu [mom] di sekitar rumah."
    erwin "Saya senang mendengarnya. Kami beruntung memiliki Anda."
    erwin "Jadi, saya mendengar bahwa Anda mendapat pekerjaan. Bagaimana sejauh ini?"
    scene expression ("images/episode4/126.webp") with dissolve
    toby "Biarkan melewatkan pembicaraan kecil. Ini tidak seperti Anda benar -benar peduli."
    erwin "Jangan seperti itu. Tentu saja saya peduli, hanya saja ..."
    scene expression ("images/episode4/127.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/128.webp") with dissolve
    erwin "Maaf Nona. Saya pikir Anda berada di ruang yang salah."
    scene expression ("images/episode4/129.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.saybehavior()
    $ ui.interact()

    woman "Jangan khawatir tentang saya, orang tua. Saya tidak akan melihat jika Anda tidak."
    scene expression ("images/episode4/130.webp") with dissolve
    toby "Ya, orang tua. Cobalah yang terbaik untuk tidak terlihat."
    scene expression ("images/episode4/131.webp") with dissolve
    woman "Sampai jumpa di sekitar anak laki -laki!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Did she just wink at me?{/i}"
    scene expression ("images/episode4/132.webp") with dissolve
    erwin "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}You're just like me, when I was young. All the ladies looked at me, until I found your [mother].{/i}"
    erwin "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Then they were looking at her with jealousy in their eyes.{/i}"
    scene expression ("images/episode4/133.webp") with dissolve
    toby "Biarkan orang tua menjadi orang tua!"


    scene expression ("images/episode4/134.webp") with long_dissolve
    erwin "Anda cari apa?"
    toby "Saya sedang mencari tas meninju."
    erwin "Itu tidak ada gunanya. Tas tinju hanya membutuhkan pukulan. Jika Anda benar -benar ingin membantu saya, mengenakan sarung tangan dan melawan saya."
    toby "Jika saya melakukannya, maka Anda akan berakhir di rumah sakit."
    scene expression ("images/episode4/135.webp") with dissolve
    erwin "Kamu sangat membenciku?"
    scene expression ("images/episode4/136.webp") with dissolve
    toby "Aku tidak membencimu. Aku hanya membenci perilakumu."
    scene expression ("images/episode4/135.webp") with dissolve
    erwin "Lalu lawan aku!"
    scene expression ("images/episode4/136.webp") with dissolve
    toby "Berhenti memukulku!"
    scene expression ("images/episode4/135.webp") with dissolve
    erwin "Takut [father] Anda?"
    scene expression ("images/episode4/137.webp") with dissolve
    toby "Oke, baiklah! Kamu menang."
    toby "Jangan bilang aku tidak memperingatkanmu!"
    scene expression ("images/episode4/138.webp") with dissolve
    erwin "Jadi bagaimana cara kerjanya?"
    toby "Aku akan menunjukkan kepadamu dalam sesaat!"
    scene expression ("images/episode4/139.webp") with dissolve
    with shake
    toby "Jadi, beri tahu saya orang tua. Apa yang mengganggumu?"
    scene expression ("images/episode4/140.webp") with dissolve
    with shake
    erwin "Fakta bahwa [son] saya meninju seperti seorang gadis kecil."
    scene expression ("images/episode4/139.webp") with dissolve
    with shake
    toby "Aku mencoba untuk tidak membunuhmu!"
    scene expression ("images/episode4/140.webp") with dissolve
    with shake
    erwin "Jangan coba -coba. Lalu saya tidak akan punya masalah."
    scene expression ("images/episode4/141.webp") with dissolve
    with shake
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Did he just say that if he dies he won't have any problems?{/i}"
    scene expression ("images/episode4/142.webp") with dissolve
    with shake
    toby "Itu saja? Anda hanya ingin mati, karena hidup terlalu sulit?"
    scene expression ("images/episode4/143.webp") with dissolve
    with shake
    erwin "Saya tidak ingin mati. Saya hanya mengatakan bahwa itu akan lebih mudah."
    scene expression ("images/episode4/142.webp") with dissolve
    with shake
    toby "Dan sejak kapan Anda ingin hidup menjadi lebih mudah?"
    scene expression ("images/episode4/144.webp") with dissolve
    with shake
    toby "Apa yang terjadi dengan semua pelajaran yang Anda ajarkan kepada saya?"
    toby "What happened to \"It’s hard to beat a person who never gives up\"?"
    scene expression ("images/episode4/145.webp") with dissolve
    with shake
    toby "Where is the man who told me \"What defines us is how we pick ourselves up after falling\"?"
    scene expression ("images/episode4/142.webp") with dissolve
    with shake
    toby "\"There is some good in this world, and it’s worth fighting for\"."
    scene expression ("images/episode4/143.webp") with dissolve
    with shake
    erwin "Jangan beri aku omong kosong itu. Itu adalah waktu yang berbeda."
    scene expression ("images/episode4/144.webp") with dissolve
    with shake
    toby "\"You’re so much stronger than your excuses\"."
    scene expression ("images/episode4/146.webp") with dissolve
    with shake
    erwin "Saya tidak mencari alasan. Ini kenyataan."
    scene expression ("images/episode4/142.webp") with dissolve
    with shake
    toby "Realitas pantatku. Anda membuat kesalahan dan mencari orang lain untuk disalahkan."
    scene expression ("images/episode4/146.webp") with dissolve
    with shake
    erwin "Saya tidak menyalahkan siapa pun. Saya menyalahkan diri sendiri."
    scene expression ("images/episode4/147.webp") with dissolve
    with shake
    erwin "Karena saya ... kami bangkrut."
    scene expression ("images/episode4/148.webp") with dissolve
    with shake
    erwin "Karena kesalahan saya, kami kehilangan rumah kami."
    erwin "Aku ingin memberi kalian segalanya dan sekarang aku tidak bisa memberimu omong kosong!"
    scene expression ("images/episode4/147.webp") with dissolve
    with shake
    erwin "Saya kehilangan semua uang kami. Tris tidak akan bisa pergi ke perguruan tinggi terbaik!"
    erwin "Anda harus menjual mobil yang saya berikan kepada Anda untuk ulang tahun ke -18 Anda!"
    scene expression ("images/episode4/149.webp") with dissolve
    with shake
    erwin "Anda tidak menghormati saya lagi ... [sister] Anda tidak menghormati saya!"
    erwin "Istri saya tidak menghormati saya!"
    scene expression ("images/episode4/147.webp") with dissolve
    with shake
    erwin "Saya kehilangan perusahaan saya! Saya harus memasukkan 100 orang!"
    erwin "100 orang tidak akan bisa memberi makan keluarga mereka!"
    scene expression ("images/episode4/150.webp") with dissolve
    with shake
    toby "Anda memiliki dewan direksi. Ini tidak semua salahmu."
    scene expression ("images/episode4/147.webp") with dissolve
    with shake
    erwin "Katakan itu kepada istri dan anak yang tertinggal setelah salah satu karyawan saya bunuh diri."
    erwin "Dan saya tidak bisa membantu mereka!"
    scene expression ("images/episode4/148.webp") with dissolve
    with shake
    erwin "Katakan itu kepada orang yang menderita kanker dan tidak mampu membayar tagihan medisnya!"
    scene expression ("images/episode4/144.webp") with dissolve
    with shake
    toby "Hidup itu sulit. Itu bisa terjadi, tetapi tidak semuanya adalah kesalahan Anda."
    scene expression ("images/episode4/150.webp") with dissolve
    with shake
    toby "Dan aku pasti tidak ada kesalahan [mom]."
    toby "Satu -satunya hal yang telah dia lakukan adalah berada di sisi Anda!"
    scene expression ("images/episode4/151.webp") with dissolve
    with shake
    toby "Dia selalu bersamamu. Dia selalu setia padamu."
    toby "Dia membesarkan kami untuk mencintaimu, apa pun yang terjadi."
    scene expression ("images/episode4/145.webp") with dissolve
    with shake
    toby "Dia cantik. Dia dapat memiliki pria yang dia inginkan, namun dia tetap bersamamu."
    toby "Dan Anda memanggilnya pelacur!"
    scene expression ("images/episode4/147.webp") with dissolve
    with shake
    erwin "Cepat atau lambat dia akan meninggalkan saya. Aku tidak punya apa -apa untuk diberikan padanya."
    scene expression ("images/episode4/150.webp") with dissolve
    with shake
    toby "Dia hanya ingin dicintai. Kekasihnya! Hormati dia!"
    scene expression ("images/episode4/148.webp") with dissolve
    with shake
    erwin "Saya bisa! Saya tidak bisa memberinya apa yang dia butuhkan."
    scene expression ("images/episode4/151.webp") with dissolve
    with shake
    toby "Coba saja!"
    scene expression ("images/episode4/149.webp") with dissolve
    with shake
    erwin "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n{i}We haven't had sex in like 5 years.{/i}"
    scene expression ("images/episode4/152.webp") with dissolve
    with shake
    toby "Lalu persetan dengan dia! Persetan istrimu, kawan!"
    scene expression ("images/episode4/153.webp") with dissolve
    with shake
    stop music fadeout 0.3
    play sound "audio/fx/DJ Disc Scratch Sound Effect.mp3"

    erwin "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n{i}I CAN'T! I CAN'T HAVE SEX ANYMORE!{/i}"
    erwin "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n{i}I CAN'T GET MY DICK HARD!{/i}"
    scene expression ("images/episode4/154.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit! Did he yell that?{/i}"
    scene expression ("images/episode4/155.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yup... He sure did!{/i}"
    toby "Uhmm ..."
    scene expression ("images/episode4/156.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What should I do now?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck me! This is not what I expected!{/i}"
    scene expression ("images/episode4/157.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should go talk to him. But what the hell should I say?{/i}"
    scene expression ("images/episode4/158.webp") with long_dissolve


    toby "Hei [dad]. Apakah kamu baik -baik saja?"
    erwin "Jangan khawatir tentang saya juara. Saya akan baik -baik saja."
    erwin "Hanya saja saya melihat [mother] Anda dan saya melihat betapa baiknya dia mencari usianya dan yang saya tunggu -tunggu hanyalah dia menemukan seseorang yang jauh lebih muda dari saya."
    scene expression ("images/episode4/159.webp") with dissolve
    erwin "Terima kasih untuk hari ini. Itu sangat membantu saya."
    toby "Ya, tentu. Tidak masalah. Saya minta maaf atas apa yang terjadi di sana."
    erwin "Jangan khawatir tentang saya. Ini tidak seperti saya akan kembali ke sini."
    erwin "Tapi Anda di sisi lain ..."
    toby "Saya akan baik -baik saja."
    menu:
        "{i} [JGR] Nyatakan dia {/i}"(csq="Erwin +1"):
            $ erwin_rel += 1
            $ ep4_erwinComfort = True
            scene expression ("images/episode4/160.webp") with dissolve
            toby "Hati-hati di jalan!"
            erwin "Anda juga, [son]."
        "{i} Say Goodbye {/i}":
            pass
    scene expression ("images/episode4/161.webp") with dissolve
    erwin "Tolong jangan beri tahu [mother] Anda apa yang terjadi di sini."
    toby "Tentu."
    erwin "Sampai jumpa?"
    toby "Belum. Saya akan bekerja. Mungkin nanti malam."
    erwin "Hati-hati di jalan!"

    $ progress = 56
    scene expression ("images/episode4/162.webp") with dissolve
    if ep4_erwinComfort:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}My feelings are so mixed right now.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I feel bad for him, for everything that happening to him, but still he treats [mom] like shit.{/i}"
    else:

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}After everything he told me, why don't I feel bad for him?{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}He's still my [father].{/i}"

    scene expression ("images/episode4/163.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should take a shower and get to work.{/i}"
    scene expression ("images/episode4/164.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()


    scene expression ("images/episode4/165.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/166.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/167.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/168.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is she really checking me out?{/i}"
    scene expression ("images/episode4/169.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, fuck, fuck. I can't get a boner now. She'll think I'm some kind of pervert.{/i}"
    menu:
        "{i} Tutupi dirimu {/i}":
            scene expression ("images/episode4/170.webp") with dissolve
            woman "Hari pertama?"
            scene expression ("images/episode4/171.webp") with dissolve
            toby "Apakah itu jelas?"
        "{i} [JGR] Bangga dengan perhiasan Anda {/i}"(csq="Sheila +1 & Galeri Gambar"):
            $ sheila_rel += 1
            $ unlockImage(persistent.sheila_01)
            scene expression ("images/episode4/171.webp") with dissolve
            woman "Halo, pria besar. Hari pertama?"
            toby "Apakah itu jelas?"
    scene expression ("images/episode4/172.webp") with dissolve
    woman "Sama sekali tidak! Hanya saja saya belum pernah melihat Anda di sini sebelumnya."
    scene expression ("images/episode4/173.webp") with dissolve
    sheila "Ngomong -ngomong, aku Sheila!"
    toby "[toby!c]. Saya pikir kita bisa melewatkan jabat tangan."
    scene expression ("images/episode4/174.webp") with dissolve
    sheila "Saya bisa datang jika Anda benar -benar ingin berjabat tangan."
    menu:
        "{i} [JGR] Jadilah genit {/i}"(csq="Sheila +1"):
            $ sheila_rel += 1
            scene expression ("images/episode4/173.webp") with dissolve
            toby "Itu mungkin bukan ide yang bagus. Siapa tahu, Anda mungkin akhirnya mengguncang sesuatu yang lain."
            scene expression ("images/episode4/174.webp") with dissolve
            sheila "Ya, Anda benar. Kami tidak menginginkan itu, bukan?"
            scene expression ("images/episode4/173.webp") with dissolve
            toby "Anda benar."
        "{i} bertindak normal {/i}":
            scene expression ("images/episode4/173.webp") with dissolve
            toby "Kami akan melewatkannya kali ini."
    scene expression ("images/episode4/175.webp") with dissolve
    sheila "Saya harus mengakui, [toby!c]. Saya suka cara Anda bekerja. Saya tidak pernah melihat seorang psikolog menghancurkan klien dengan baik."
    toby "Saya tidak punya psikolog."
    sheila "Maka Anda harus mempertimbangkan untuk menjadi satu. Sangat menarik apa yang Anda dan lelaki tua itu lakukan di sana."
    sheila "Meskipun itu menyedihkan baginya."
    scene expression ("images/episode4/176.webp") with dissolve
    sheila "Jadi, jika Anda bukan seorang psikolog, apa yang Anda lakukan untuk hidup?"
    scene expression ("images/episode4/177.webp") with dissolve
    toby "Bukankah itu canggung berbicara seperti ini?"
    scene expression ("images/episode4/176.webp") with dissolve
    sheila "Nah, Anda tidak mengundang saya ke kios Anda!"
    scene expression ("images/episode4/177.webp") with dissolve
    if sheila_rel >= 1:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This girl is crazy. I love it!{/i}"
        toby "Anda dipersilakan untuk datang kapan pun Anda mau."
        scene expression ("images/episode4/176.webp") with dissolve
        sheila "Oh, saya akan, tetapi tidak hari ini. Anda tidak seharusnya bercinta di tempat kerja Anda."
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This girl is crazy.{/i}"
        scene expression ("images/episode4/176.webp") with dissolve
        sheila "Jangan khawatir. Aku tidak akan datang, aku tidak diizinkan untuk bercinta di tempat kerja!"
    scene expression ("images/episode4/178.webp") with dissolve
    toby "Kamu bekerja di sini?"
    scene expression ("images/episode4/176.webp") with dissolve
    sheila "Ya. Saya seorang pelatih pribadi!"
    scene expression ("images/episode4/178.webp") with dissolve
    toby "Oh, itu luar biasa!"
    scene expression ("images/episode4/176.webp") with dissolve
    sheila "Jadi? Apakah Anda akan memberi tahu saya apa yang Anda lakukan untuk mencari nafkah?"
    scene expression ("images/episode4/178.webp") with dissolve
    if toby_job == 0:
        toby "Saya adalah agen real estat."
        scene expression ("images/episode4/179.webp") with dissolve
        sheila "Itu sangat keren. Saya benar -benar mencari apartemen baru."
        sheila "Anda bekerja untuk perusahaan apa?"
        scene expression ("images/episode4/178.webp") with dissolve
        toby "Carpe Diem Realty! Ini adalah yang kecil, tapi itu berhasil."
        scene expression ("images/episode4/179.webp") with dissolve
        sheila "Saya suka tag line!"
    else:
        toby "Saya bekerja sebagai asisten manajer di klub malam."
        scene expression ("images/episode4/179.webp") with dissolve
        sheila "Itu sangat keren. Klub apa?"
        scene expression ("images/episode4/178.webp") with dissolve
        toby "Klimaks."
        scene expression ("images/episode4/179.webp") with dissolve
        sheila "Saya suka klub itu. Kenapa kita tidak pernah bertemu?"
        scene expression ("images/episode4/178.webp") with dissolve
        toby "Saya baru saja memulai minggu ini."
        scene expression ("images/episode4/179.webp") with dissolve
        sheila "Itu keren. Mungkin sampai jumpa di sana suatu hari nanti."
        scene expression ("images/episode4/178.webp") with dissolve
        toby "Ya ... mungkin Anda akan melakukannya."
    scene expression ("images/episode4/180.webp") with dissolve
    toby "Sayangnya, saya harus pergi. Senang bertemu denganmu Sheila."
    sheila "Sampai jumpa di sekitar pria besar!"

    return


label episode4_friday_realEstate:

    $ progress = 57
    scene expression ("images/episode4/181.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/182.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmm... I wonder where Darlene is.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She might be in the other room.{/i}"
    scene expression ("images/episode4/183.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/184.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/185.webp") with dissolve
    toby "Halo, Nyonya Darlene. Apa kabarmu hari ini?"
    scene expression ("images/episode4/186.webp") with dissolve
    darlene "Hai [toby!c]. Saya melihat beberapa bangunan yang mungkin kami beli. Aku akan bersamamu sebentar lagi!"
    scene expression ("images/episode4/185.webp") with dissolve
    toby "Apakah ada yang bisa saya bantu?"
    scene expression ("images/episode4/186.webp") with dissolve
    darlene "Belum. Tunggu saja saya di sana karena kami mengharapkan klien segera."
    scene expression ("images/episode4/185.webp") with dissolve
    toby "Oke, akan melakukannya."

    show screen ui_message("A few minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/187.webp") with dissolve
    hide screen ui_message

    darlene "Maaf untuk itu. Saya menemukan bangunan yang sangat masuk akal untuk dijual yang berpotensi kami beli dan renovasi."
    darlene "Jadi saya melihat -lihat struktur untuk melihat apakah itu sepadan dengan investasi."
    scene expression ("images/episode4/188.webp") with dissolve
    toby "Jangan khawatir sama sekali."
    toby "Apa ini?"
    darlene "Beberapa makalah untuk Anda tandatangani. Setelah ini Anda secara resmi bekerja untuk saya."
    scene expression ("images/episode4/189.webp") with dissolve
    toby "Maafkan saya, ma, tetapi dikatakan di sini bahwa saya bekerja sebagai asisten Anda bukan agen real estat. Saya pikir saya akan menjadi agen."
    scene expression ("images/episode4/190.webp") with dissolve
    darlene "Apakah Anda yakin ingin menjadi agen?"
    darlene "Karena aku sangat menyukaimu dan ingin sekali kamu ada. Belum lagi, bekerja sebagai asisten saya Anda sebenarnya akan memiliki lebih banyak waktu luang dan lebih banyak uang."
    scene expression ("images/episode4/191.webp") with dissolve
    darlene "Jika Anda membaca semuanya, Anda akan melihat bahwa Anda akan mendapatkan persentase dari setiap penjualan yang dilakukan oleh perusahaan kami, dan persentase yang lebih besar pada penjualan Anda sendiri."
    darlene "Bagian terbaik dari pekerjaan ini adalah Anda tidak akan harus bekerja 8 jam sehari, hanya ketika saya membutuhkan Anda."
    toby "Uhum ... dan apa yang terjadi jika kita tidak menjual sesuatu?"
    scene expression ("images/episode4/192.webp") with dissolve
    darlene "Itu dieja di sini. Jika persentase Anda berakhir di bawah, 500 dalam bulan tertentu, Anda masih akan mendapatkan pembayaran dasar, 500. Tetapi dari apa yang saya lihat sejauh ini, saya ragu itu akan menjadi masalah."
    scene expression ("images/episode4/193.webp") with dissolve
    toby "Saya tidak tahu harus berkata apa. Saya tidak ingin terdengar tidak berterima kasih, karena saya sangat bersyukur, hanya saja saya tidak tahu apa yang saya lakukan untuk mendapatkan semua ini."
    scene expression ("images/episode4/191.webp") with dissolve
    darlene "Mari kita katakan bahwa saya suka senyum Anda dan Anda terlihat seperti pria yang cerdas."
    scene expression ("images/episode4/193.webp") with dissolve
    toby "Nah dalam hal ini, di mana saya harus menandatangani?"
    scene expression ("images/episode4/194.webp") with dissolve
    darlene "Di Sini!"
    scene expression ("images/episode4/195.webp") with dissolve
    menu:
        "[JGR] Keinginan Anda adalah perintah saya!"(csq="Darlene +1"):
            $ darlene_rel += 1
            scene expression ("images/episode4/196.webp") with dissolve
            darlene "Saya suka antusiasme Anda. Anda akan menjadi asisten yang baik, tetapi mari kita tegang untuk menandatangani kertas untuk saat ini."
        "Uhum ... maaf?":
            scene expression ("images/episode4/196.webp") with dissolve
            darlene "Maaf. Saya memiliki hari yang panjang dan saya hanya bermain -main."
    darlene "Masuk di bagian bawah setiap halaman dan itu harus melakukannya."
    scene expression ("images/episode4/197.webp") with dissolve
    toby "Jadi, tentang bangunan yang Anda sebutkan itu. Tentang apa itu?"
    scene expression ("images/episode4/198.webp") with dissolve
    darlene "Dengan baik. Ini adalah bangunan 3 lantai dengan 6 apartemen. Setiap cerita memiliki 2 apartemen, tetapi mereka tidak dalam kondisi yang sangat baik dan mereka perlu direnovasi."
    darlene "Kami akan punya banyak waktu untuk membicarakan tentang hari lain itu. Bagaimana Anda menyukai kota kami sejauh ini?"
    scene expression ("images/episode4/193.webp") with dissolve
    toby "Yah, saya tidak bisa mengatakan bahwa saya telah melihat banyak dari itu. Saya sudah pergi ke pantai dua kali dan pergi berbelanja, di luar itu saya tidak bisa mengatakan saya telah melihat banyak."
    scene expression ("images/episode4/198.webp") with dissolve
    darlene "Anda sangat suka pergi ke pantai?"
    scene expression ("images/episode4/199.webp") with dissolve
    toby "Tidak juga, itu hanya terjadi. Hari saya datang untuk wawancara saya pergi dengan [mom] dan [sister]."
    scene expression ("images/episode4/198.webp") with dissolve
    darlene "Dan waktu lainnya? Biarkan saya menebak. Anda pergi ke sana dengan wanita cantik yang cantik?"
    scene expression ("images/episode4/199.webp") with dissolve
    toby "Anda dekat, tetapi tidak, tidak cukup. Saya benar -benar pergi dengan dua wanita!"
    scene expression ("images/episode4/200.webp") with dissolve
    darlene "Begitu? Betapa pemain yang kami dapatkan di sini."
    scene expression ("images/episode4/199.webp") with dissolve
    toby "Aku hanya mengacaukanmu. Tidak ada apa pun di antara saya dan keduanya. Hanya saja kita semua baru di kota dan mereka ingin melihat pantai."
    toby "Saya hanya pemandu mereka."
    scene expression ("images/episode4/200.webp") with dissolve
    darlene "Dua gadis baru di kota. Hmm ... bisakah kita berbicara tentang dua pelanggan kita, Lisa dan yang lainnya?"
    scene expression ("images/episode4/201.webp") with dissolve
    toby "Saya tidak berkencan dengan klien."
    scene expression ("images/episode4/196.webp") with dissolve
    darlene "Saya pikir Anda mengatakan tidak ada apa pun di antara Anda dan salah satu dari keduanya, namun Anda menyebutnya kencan?"
    scene expression ("images/episode4/201.webp") with dissolve
    toby "Kata -kata itu salah!"
    scene expression ("images/episode4/196.webp") with dissolve
    darlene "Saya mengerti. Ngomong -ngomong, dalam beberapa menit klien baru harus datang. Cobalah untuk tidak menidurinya juga."
    scene expression ("images/episode4/199.webp") with dissolve
    toby "Pertama -tama, saya belum melakukan apa pun dengan gadis dan selain itu, saya terlalu lelah hari ini."
    toby "Saya mampir ke gym sebelum datang ke sini."
    scene expression ("images/episode4/202.webp") with dissolve
    darlene "Benar-benar? Apakah kamu sekarang?"
    scene expression ("images/episode4/203.webp") with dissolve
    toby "Ya, tapi saya tidak tinggal lama sehingga saya bisa sampai di sini."
    label memory_11:


        scene expression ("images/episode4/204.webp") with dissolve
        darlene "Hmm ... mungkin saya harus memberi Anda kenaikan gaji, sehingga Anda mampu benar -benar pergi ke gym dan tidak hanya mampir."
        toby "Sangat lucu."
        scene expression ("images/episode4/205.webp") with dissolve
        darlene "Jadi Anda bilang Anda terlalu lelah untuk berhubungan seks? Itulah mengapa saya suka wanita. Mereka tidak pernah terlalu lelah untuk itu."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... her touching me like that is giving me a boner.{/i}"
        scene expression ("images/episode4/206.webp") with dissolve
        darlene "Apa ini? Tidak terlihat seperti Anda terlalu lelah. Sepertinya Anda siap untuk pergi."
        menu:
            "{i} hentikan {/i} [JWRN4]"(csq="Jalur Darlene ditutup") if not _in_replay:
                $ renpy.notify("Darlene's path has been closed!")
                $ darlene_path = False
                scene expression ("images/episode4/207.webp") with dissolve
                toby "Maaf ma \ 'am. Tapi saya tidak berpikir ini tepat."
                scene expression ("images/episode4/208.webp") with dissolve
                darlene "Maaf [toby!c]. Saya hanya bermain -main. Seperti yang saya katakan, saya terlalu lelah."
                toby "Ya, tentu. Tidak masalah."
                scene expression ("images/episode4/209.webp") with dissolve
                darlene "Kami harus menunggu klien kami."
            "{i} [JGR] Kendalikan situasi {/i}"(csq="Darlene +1 & Galeri Gambar"):

                $ darlene_rel += 1
                $ darlene_path = True
                $ unlockImage(persistent.darlene_04)
                scene expression ("images/episode4/210.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Oh, so you like to play with fire, do you?{/i}"
                darlene "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}What could happen?{/i}"
                scene expression ("images/episode4/211.webp") with dissolve
                toby "Salah satu dari tiga hasil berapi -api."
                darlene "Ah, benarkah? Biarkan saya mendengar kemungkinan."
                scene expression ("images/episode4/212.webp") with dissolve
                toby "Skenario pertama adalah bahwa Anda disimpan sebelum kembang api. Oleh klien kami, yang bisa berjalan dalam waktu dekat sekarang."
                toby "Kedua adalah Anda berlutut perlahan dan hanya bibir Anda yang terbakar."
                scene expression ("images/episode4/213.webp") with dissolve
                toby "Dan skenario terakhir adalah Anda memberi saya kunci ke kantor, saya pergi mengunci pintu, maka bahkan petugas pemadam kebakaran tidak dapat menyelamatkan Anda dari terbakar."
                scene expression ("images/episode4/214.webp") with dissolve
                darlene "Anda jelas tahu saya menyukai kepribadian yang kuat, tetapi saya bisa melihat melalui Anda. Anda masih hanya seorang anak yang jelas -jelas telah menonton terlalu banyak pornografi."
                darlene "Aku menyukaimu, tapi rutinitas pria tangguh tidak cocok untukmu."
                darlene "Saya yakin jika saya melepas rok saya dari Anda akan berlutut secepat mungkin untuk mengubur lidah Anda di vagina saya sambil membelai ayam keras Anda!"

                show ep4_215
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode4/215.webp")
                hide ep4_215

                scene expression ("images/episode4/216.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}You're my boss and I respect you, but this isn't a game.{/i}"
                toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}So my dear Darlene, should I pull my pants down now, or are you gonna lock the door first?{/i}"
                scene expression ("images/episode4/217.webp") with dissolve
                darlene "Anda menyadari bahwa saya tidak dihidupkan oleh pria?"
                toby "Namun tanganmu menyentuh penisku!"
                darlene "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Ok, I'll admit I'm curious. Show me what you're packing.{/i}"
                scene expression ("images/episode4/218.webp") with dissolve
                darlene "Tidak, maaf sayang, tapi ini tidak melakukan apa pun untukku. Saya masih menyukai wanita."
                toby "Matamu mengatakan sesuatu yang lain."
                scene expression ("images/episode4/219.webp") with dissolve
                darlene "Apa yang mereka katakan?"
                toby "Bahwa Anda ingin mencicipinya."
                scene expression ("images/episode4/220.webp") with dissolve
                darlene "Anda seperti itu, saya yakin, tapi salah! Saya hanya ingin membelai, untuk melihat seperti apa rasanya penis yang sebenarnya sehingga saya bisa mendapatkan mainan yang lebih realistis untuk saya dan pacar saya!"

                show ep4_221
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It's my second day at work and my boss is jerking me off. This is not going to end well.{/i}"
                scene expression ("images/episode4/221.webp")
                hide ep4_221

                scene expression ("images/episode4/222.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()

                show ep4_223
                darlene "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}You sir, are going to get me in trouble.{/i}"
                toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}The feeling is mutual{/i}"

                scene expression ("images/episode4/223.webp")
                hide ep4_223

                scene expression ("images/episode4/224.webp") with dissolve
                play sound "audio/fx/Knocking-on-door-five-knocks-www.fesliyanstudios.com.mp3"
                darlene "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Pull your pants up! NOW!{/i}"
                $ unlockMemory(persistent.memory_11)

        $ renpy.end_replay()


    $ progress = 58
    scene expression ("images/episode4/225.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    sheila "Permisi. Apakah Carpe Diem Realty ini?"


    scene expression ("images/episode4/226.webp") with dissolve
    darlene "Anda berada di tempat yang tepat. Anda pasti Sheila, kan?"
    scene expression ("images/episode4/227.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the hell is she doing here?{/i}"
    scene expression ("images/episode4/228.webp") with dissolve
    darlene "Saya ingin Anda bertemu [toby!c]. Dia asisten saya dan dia akan menunjukkan kepada Anda apartemen yang kami miliki."
    sheila "Anda terlihat sangat akrab. Sudahkah kita bertemu?"
    scene expression ("images/episode4/227.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Ok, then. Two can play at this game.{/i}"
    scene expression ("images/episode4/229.webp") with dissolve
    toby "Aku tidak yakin aku pernah melihatmu sebelumnya, tapi aku yakin kamu akan mengingatku jika kita bertemu."
    sheila "Ahh, ya! Saya yakin saya melihat Anda di gym hari ini, melatih seorang lelaki tua?"
    scene expression ("images/episode4/230.webp") with dissolve
    darlene "Anda menyebutkan sesuatu tentang pergi ke gym, tetapi saya tidak tahu Anda adalah pelatih pribadi di waktu luang Anda."
    scene expression ("images/episode4/231.webp") with dissolve
    toby "Saya tidak. Itu pekerjaannya. Saya hanya membantu [dad] saya."
    scene expression ("images/episode4/232.webp") with dissolve
    sheila "Saya pikir Anda mengatakan Anda belum pernah bertemu saya sebelumnya dan sekarang Anda tahu pekerjaan saya?"
    scene expression ("images/episode4/233.webp") with dissolve
    toby "Anda terlihat sangat bugar. Saya yakin Anda adalah pelatih pribadi."
    scene expression ("images/episode4/234.webp") with dissolve
    darlene "Itu salah satu dari banyak hadiahnya, dia membaca orang dengan sangat baik."
    scene expression ("images/episode4/235.webp") with dissolve
    sheila "Anda pasti sangat bangga memilikinya."
    scene expression ("images/episode4/234.webp") with dissolve
    darlene "Tentu saja, dia salah satu yang terbaik."
    scene expression ("images/episode4/236.webp") with dissolve
    darlene "Ngomong -ngomong, izinkan saya menunjukkan apartemen yang kami miliki untuk disewa dan kemudian [toby!c] dapat membawa Anda ke salah satu yang ingin Anda lihat!"
    sheila "Saya sangat menyukainya."
    scene expression ("images/episode4/237.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's messing with me. I'm not sure she's even interested in apartments.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But what can I do. I'll have to show her the place.{/i}"

    show screen ui_message("20 minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message

    scene expression ("images/episode4/238.webp") with dissolve
    sheila "Saya suka yang ini. Saya pikir itu sempurna untuk saya."
    darlene "Saya senang mendengarnya. Nah, saya akan membiarkan [toby!c] membawa Anda dalam tur."
    scene expression ("images/episode4/239.webp") with dissolve
    sheila "Itu akan sangat bagus."
    scene expression ("images/episode4/240.webp") with dissolve
    toby "Saya punya sepeda di luar. Haruskah kita bertemu di sana atau Anda ingin naik dengan saya?"
    scene expression ("images/episode4/239.webp") with dissolve
    sheila "Saya belum pernah naik sepeda sebelumnya. Aku suka."
    scene expression ("images/episode4/241.webp") with dissolve
    darlene "Itu sempurna kalau begitu. Saya harap Anda menyukai apartemen ini."
    sheila "Terima kasih atas segalanya."
    darlene "Dengan senang hati!"

    scene expression ("images/episode4/242.webp") with dissolve
    sheila "Jadi, [toby!c]. Bos Anda berpikir Anda pandai membaca orang. Jadi apa yang bisa Anda ceritakan tentang diri saya sendiri?"
    menu:
        "{i} [JGR] Pendekatan genit {/i}"(csq="Gambar galeri"):
            $ sheila_rel += 1
            $ sheila_path = True
            $ unlockImage(persistent.sheila_02)
            toby "Selain fakta bahwa Anda cantik?"
            sheila "Yup. Selain itu."
            scene expression ("images/episode4/243.webp") with dissolve
            toby "Anda tipe orang yang suka membuat pria gila. Anda memiliki kemampuan untuk mendapatkan apa pun yang Anda inginkan dari seorang pria dan Anda mengetahuinya."
            toby "Anda suka bermain kucing & mouse."
            toby "Seperti sekarang, Anda bahkan tidak terlalu tertarik dengan apartemen. Anda hanya ingin bermain dengan mouse Anda."
        "{i} pendekatan normal {/i} [JWRN2]"(csq="Jalur Sheila ditutup"):
            $ sheila_path = False
            $ renpy.notify("Sheila's path has been closed!")
            scene expression ("images/episode4/243.webp") with dissolve
            toby "Mari kita katakan saja saya tidak berpikir Anda tertarik pada apartemen. Anda hanya ingin bermain dengan saya."
    scene expression ("images/episode4/244.webp") with dissolve
    sheila "Salah! Saya benar -benar membutuhkan apartemen dan seingat saya, saya katakan sebelumnya. Tapi saya kira mengetahui bahwa saya telanjang tepat di sebelah Anda membuat Anda melupakannya."
    sheila "Jadi? Haruskah kita?"
    scene expression ("images/episode4/245.webp") with dissolve
    toby "Ya, kami akan!"

    scene expression ("images/episode4/246_0.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode4/247_0.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode4/248.webp") with dissolve
    toby "Jadi? Apa yang kamu katakan? Anda menyukainya?"
    sheila "Apakah Anda bercanda? Saya menyukainya. Ini sangat bagus. Persis seperti yang saya inginkan."
    toby "Senang mendengarnya."
    scene expression ("images/episode4/249.webp") with dissolve
    sheila "Jadi, kapan menurut Anda saya bisa pindah, karena saya tinggal di hotel saat ini."
    toby "Saya perlu membahas beberapa detail dengan bos saya, tetapi saya yakin kami dapat mengerjakan sesuatu untuk membawa Anda ke sini dengan cepat."
    toby "Biarkan saya meneleponnya."
    scene expression ("images/episode4/250.webp") with dissolve
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Yes, [toby!c]. Something wrong?{/i}"
    toby "Hai Darlene. Tidak, semuanya hebat, hanya saja Miss Sheila sangat menyukai apartemen dan ingin pindah sesegera mungkin. Dia saat ini tinggal di hotel."
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Well in that case, tell her that she needs to come by the office tomorrow to sign the papers, but if she wants, she can move in tonight after she pays the security deposit.{/i}"
    toby "Yang?"
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}It's twice the monthly rent. She'll get that money back when she moves out.{/i}"
    toby "Oke. Saya akan memberi tahu dia!"
    if darlene_path == True:
        darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Bye sexy. See you Monday at the office.{/i}"
    else:
        darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Bye dear. See you Monday at the office.{/i}"
    scene expression ("images/episode4/251.webp") with dissolve
    toby "Kabar Baik! Saya baru saja berbicara dengan bos saya dan dia mengatakan kepada saya bahwa jika Anda suka, Anda dapat pindah hari ini setelah Anda membayar uang jaminan yang Anda akan kembali ketika Anda pindah, jika semuanya beres."
    sheila "Jangan khawatir sayang, aku gadis yang baik. Saya tidak akan melempar pesta pora apa pun di sini."
    if sheila_path == True:
        scene expression ("images/episode4/252.webp") with dissolve
        sheila "Tetapi jika saya akan pergi, saya akan mengundang Anda!"
        toby "Maka saya kira saya harus memberikan nomor telepon saya!"
        sheila "Tolong lakukan!"
        scene expression ("images/episode4/253.webp") with dissolve
        sheila "Saya tidak ingin memanfaatkan Anda, tetapi apakah Anda pikir Anda dapat membantu saya dengan tas saya? Saya perlu mendapatkannya dari kamar hotel saya."
        menu:
            "[JGR] Tentu. Lepaskan.":
                sheila "Terima kasih sayang!"
                return
            "Maaf, tapi saya punya beberapa hal untuk diurus terlebih dahulu. [JWRN2]"(csq="Jalur Sheila ditutup"):
                $ sheila_path = False
                $ renpy.notify("Sheila's path has been closed!")
                sheila "Saya mengerti. Tidak masalah."
    else:
        toby "Selama dinding dan jendela adalah tempatnya, Anda dapat melakukan apa pun yang Anda inginkan."

    scene expression ("images/episode4/254.webp") with dissolve
    sheila "Terima kasih atas segalanya, [toby!c]."
    toby "Senang berbisnis dengan Anda dan nikmati apartemen baru Anda."

    if sheila_path == False:
        scene expression ("images/episode4/469.webp") with dissolve
        sheila "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I'm sorry, sir. Plan A fizzled out. Moving on to Plan B.{/i}"

    return

label episode4_friday_club:
    $ progress = 57

    scene expression ("images/episode4/181.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.saybehavior()
    $ ui.interact()
    label memory_12:
        scene expression ("images/episode4/255.webp") with dissolve

        toby "Selamat malam."
        scene expression ("images/episode4/256.webp") with dissolve
        katrina "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nHello dear. Next time please knock before entering."
        scene expression ("images/episode4/257.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck... I caught her masturbating.{/i}"
        scene expression ("images/episode4/258.webp") with dissolve
        toby "Maaf ma \ 'am. Saya tidak tahu Anda sibuk. Saya akan kembali lagi nanti."
        scene expression ("images/episode4/256.webp") with dissolve
        katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nDon't leave... I'm almost done. Take a seat and wait for me to finish!"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This woman is crazy.{/i}"
        scene expression ("images/episode4/259.webp") with dissolve
        katrina "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nSo, how is your girlfriend doing?"
        toby "Dia menangkap seorang yang dingin, jadi kurasa dia tidak terlalu baik."
        scene expression ("images/episode4/260.webp") with dissolve
        katrina "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nThat... Is... Not... Good?"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's looking directly at me while she's playing with her dildo.{/i}"
        toby "Jadi bagaimana harimu?"
        scene expression ("images/episode4/261.webp") with dissolve
        katrina "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nNo, no! Tell me more about your girlfriend. How good is she in bed?"
        toby "Uhm ..."
        katrina "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nAcutally, tell me how long can you last in bed with her."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the hell is with these questions.{/i}"
        scene expression ("images/episode4/262.webp") with dissolve
        katrina "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nFucking piece of shit!"
        toby "Maaf?"
        scene expression ("images/episode4/263.webp") with dissolve
        katrina "Bukan kamu ... baterai mati di sampah itu!"
        scene expression ("images/episode4/264.webp") with dissolve
        katrina "Kemarilah [toby!c]! Jika Anda tidak akan menggunakan lidah Anda menggambarkan seberapa baik pacar Anda di tempat tidur, setidaknya berlutut dan jilat vaginaku sehingga saya bisa cum!"
        scene expression ("images/episode4/265.webp") with dissolve
        menu:
            "{i} Refuse {/i} [JWRN3]"(csq="Jalur Katrina ditutup") if not _in_replay:
                $ katrina_path = False
                $ renpy.notify("Katrina's path has been closed!")
                scene expression ("images/episode4/266.webp") with dissolve
                toby "Saya akan menunggu di luar sampai Anda menyelesaikan apa yang Anda mulai."
                katrina "Membosankan!"
                play sound "audio/fx/Knocking-on-door-five-knocks-www.fesliyanstudios.com.mp3"
                scene expression ("images/episode4/277.webp") with dissolve
                neal "Maaf mengganggu Anda, apakah kami punya situasi di sini!"
                pass
            "{i} [JGR] Kontrol situasi {/i}"(csq="Katrina +1 & Gambar Galeri"):

                $ katrina_path = True
                $ katrina_rel += 1
                $ unlockImage(persistent.katrina_04)
                scene expression ("images/episode4/267.webp") with dissolve
                katrina "Baik!"
                toby "Oh, Anda mungkin ingin memegang pemikiran itu."
                scene expression ("images/episode4/268.webp") with dissolve
                toby "Anda adalah bos saya dan saya menghormati Anda, tetapi jika Anda pikir saya ada di sini hanya untuk menjadi mainan seks Anda, Anda sudah mendapatkan hal lain."
                toby "Saya tidak, dan tidak akan pernah menjadi dua penis berkaki Anda."
                toby "Jika Anda ingin vagina Anda menjilat maka gunakan mulut cantik Anda dan mulai mengisap penisku!"
                scene expression ("images/episode4/269.webp") with dissolve
                katrina "Anda tidak tahu dengan siapa Anda berbicara, jadi saya sarankan membuang sikap ini dan berlutut!"
                toby "Aku akan jujur padamu. Aku ingin sekali menidurimu sampai kamu menjadi lurus. Sial, aku bahkan akan menjilat vaginamu."
                toby "Tapi jangan berharap aku menjadi mainan seksmu! Anda menginginkan sesuatu dari saya, Anda harus mengembalikan sesuatu!"
                scene expression ("images/episode4/270.webp") with dissolve
                katrina "Menurut Anda, di dunia apa Anda tinggal, nak?"
                toby "Di dunia di mana mainan Anda tidak memiliki baterai dan Anda membutuhkan saya!"
                katrina "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Pull down your pants.{/i}"
                scene expression ("images/episode4/271.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}If you want it so bad, then do it yourself.{/i}"
                katrina "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}You're playing a dangerous game, are you sure you're ready to play with the big dogs?{/i}"
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Honestly, she scares the hell out of me. But she looks so hot and horny right now, and I never realized scary plus hot was such a turn on!{/i}"
                toby "Anda terus mengatakan hal -hal dengan mulut Anda, tetapi mata Anda menceritakan kisah yang berbeda!"
                katrina "Apa kata mataku?"
                toby "Bahwa Anda ingin menarik celanaku!"
                scene expression ("images/episode4/272.webp") with dissolve
                katrina "Apa lagi yang dikatakan mataku?"
                toby "Bahwa Anda ingin mencium penis saya!"
                scene expression ("images/episode4/273.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode4/274.webp") with dissolve
                katrina "Sekarang apa?"
                toby "Sekarang Anda mengambil penis saya di mulut Anda dan mulai mengisapnya seperti pelacur!"
                katrina "Maksudmu seperti ini?"

                scene expression ("images/episode4/275.webp") with dissolve
                show ep4_275
                toby "Sama seperti itu, tetapi dengan lebih sedikit sikap, karena Anda tidak memegang kendali, saya!"
                toby "Saat Anda melakukannya, mengapa Anda tidak mulai menggosok vagina Anda karena saya tidak akan menjilatnya hari ini, karena Anda tidak menghormati saya!"
                hide ep4_275

                scene expression ("images/episode4/276.webp") with dissolve
                show ep4_276
                toby "Sama seperti itu. Anda melakukannya dengan benar."
                play sound "audio/fx/Knocking-on-door-five-knocks-www.fesliyanstudios.com.mp3"
                hide ep4_276

                scene expression ("images/episode4/277.webp") with dissolve
                neal "Maaf mengganggu Anda, tetapi kami punya situasi di sini!"
                scene expression ("images/episode4/278.webp") with dissolve
                katrina "Yah, kurasa hari ini bukan hari keberuntunganmu juga. Oh, dan omong -omong ... Lain kali Anda ingin bertingkah keras dengan saya, pastikan senjataku tidak ada di atas meja, atau aku mungkin harus menembak kemaluanmu!"
                scene expression ("images/episode4/279.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck!!! How in the hell did I not see that!?{/i}"
                pass
                $ unlockMemory(persistent.memory_12)
        $ renpy.end_replay()

    scene expression ("images/episode4/280.webp") with dissolve
    katrina "Anda mungkin masuk!"
    scene expression ("images/episode4/281.webp") with dissolve
    neal "Maaf, tetapi idiot ini menjual obat -obatan buruk di klub kami dengan harga kami!"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Bad drugs... Our price? What the hell is going on here?{/i}"
    scene expression ("images/episode4/282.webp") with dissolve
    katrina "Pergi bersenang -senang di klub sayang!"
    toby "Ya ma \ 'am."
    scene expression ("images/episode4/283.webp") with long_dissolve
    toby "Tolong wiski!"
    barman "Datang segera!"
    scene expression ("images/episode4/284.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    $ progress = 58
    scene expression ("images/episode4/285.webp") with dissolve
    sheila "Saya akan memiliki apa pun yang dia miliki!"
    scene expression ("images/episode4/286.webp") with dissolve
    toby "Baik jika tidak ini kejutan yang menyenangkan!"
    sheila "Oh, sungguh mengejutkan! Aku bahkan tidak melihatmu di sana."
    toby "Benar. Itulah mengapa Anda meminta apa pun yang saya dapatkan?"


    scene expression ("images/episode4/287.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    $ ui.saybehavior()
    $ ui.interact()
    sheila "Apa yang bisa dikatakan. Bersalah!"

    scene expression ("images/episode4/288.webp") with dissolve
    barman "Ini minuman Anda!"
    sheila "Berapa harganya?"
    menu:
        "{i} cuti {/i} [JWRN2]"(csq="Jalur Sheila ditutup"):
            $ sheila_path = False
            $ renpy.notify("Sheila's path has been closed!")
            scene expression ("images/episode4/289.webp") with dissolve
            sheila "Senang bertemu denganmu!"
            scene expression ("images/episode4/290.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I feel like a douchebag, but it's more fun this way!{/i}"

            show screen ui_message("20 minutes later") with long_dissolve
            $ ui.saybehavior()
            $ ui.interact()


            scene expression ("images/episode4/319.webp") with dissolve
            hide screen ui_message
            $ ui.saybehavior()
            $ ui.interact()
        "[JGR] Jangan khawatir, itu saya!"(csq="Sheila +1 & Galeri Gambar"):

            $ sheila_rel += 1
            $ unlockImage(persistent.sheila_03)
            $ sheila_path = True
            $ ep4_fuckSheila = True
            scene expression ("images/episode4/291.webp") with dissolve
            sheila "Terima kasih banyak Pak. Anda sangat baik!"
            scene expression ("images/episode4/292.webp") with dissolve
            toby "Sebenarnya beri saya seluruh botol!"
            scene expression ("images/episode4/293.webp") with dissolve
            toby "Biarkan saja!"
            sheila "Kemana kita akan pergi?"
            toby "Di suatu tempat kita dapat berbicara tanpa harus meneriakkan paru -paru kita!"
            label memory_13:


                scene expression ("images/episode4/294.webp") with dissolve
                sheila "Jadi ini area VIP?"
                toby "Sebut apa pun yang Anda inginkan, tetapi bagi saya ini adalah tempat favorit saya di seluruh klub. Anda dapat melihat semua orang dari sini."
                sheila "Tapi itu berarti semua orang bisa melihat kita jika kita menjadi kotor!"
                scene expression ("images/episode4/295.webp") with dissolve
                toby "Apakah Anda ingin menjadi kotor?"
                sheila "Mungkin, saya lakukan. Mungkin aku tidak, tapi aku akan memberitahumu sebuah rahasia. Saya sangat terangsang memikirkan tempat -tempat berisiko."
                toby "Apa arti tempat berisiko?"
                scene expression ("images/episode4/296.webp") with dissolve
                sheila "Seperti memegang erat -erat di rel ini saat Anda meniduriku dari belakang?"
                sheila "Tempat -tempat yang berisiko seperti itu."
                toby "Saya pikir saya mendapatkan fotonya"
                sheila "Sayang sekali kamu tidak membawaku ke sini untuk meniduriku, hanya untuk berbicara!"
                scene expression ("images/episode4/297.webp") with dissolve
                toby "Ya. Sungguh memalukan!"
                toby "Jadi Sheila ... mengapa Anda tidak memberi tahu saya lebih banyak tentang diri Anda?"
                sheila "Apakah Anda benar -benar tertarik dengan saya?"
                toby "Jawaban yang jujur?"
                sheila "Ya!"
                scene expression ("images/episode4/298.webp") with dissolve
                toby "Saya masih memikirkan bagian kereta api."
                scene expression ("images/episode4/299.webp") with dissolve
                sheila "Lalu janganlah membodohi diri kita sendiri. Jika Anda ingin tahu lebih banyak tentang saya, kami bisa berkencan, tetapi malam ini kami berdua menginginkan hal yang sama."
                scene expression ("images/episode4/300.webp") with dissolve
                toby "Saya pikir kita keduanya di halaman yang sama!"

                scene expression ("images/episode4/301.webp") with dissolve
                show ep4_301
                $ ui.saybehavior()
                $ ui.interact()
                hide ep4_301

                scene expression ("images/episode4/302.webp") with dissolve
                show ep4_302
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's teasing me so much!{/i}"
                hide ep4_302

                scene expression ("images/episode4/303.webp") with dissolve
                show ep4_303
                $ ui.saybehavior()
                $ ui.interact()
                hide ep4_303

                scene expression ("images/episode4/304.webp") with dissolve
                show ep4_304
                $ ui.saybehavior()
                $ ui.interact()
                toby "Saya pikir sudah waktunya untuk pergi ke rel!"
                hide ep4_304

                scene expression ("images/episode4/305.webp") with dissolve
                sheila "Saya pikir Anda tidak akan pernah bertanya!"

                scene expression ("images/episode4/306.webp") with dissolve
                show ep4_306
                sheila "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nFuck me... You're so big!"
                sheila "{size=12}{color=#FDCA6E}* loud *{/color}{/size}\nGive it to me HARD."
                hide ep4_306

                scene expression ("images/episode4/307.webp") with dissolve
                show ep4_307
                sheila "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nYes. YES... YES! Right there don't stop!"
                toby "Jika Anda tidak ingin semua orang tahu apa yang kami lakukan di sini, saya akan menurunkan suara saya!"
                sheila "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nFuck them... Your dick is so good!"
                hide ep4_307

                if katrina_path == True:
                    scene expression ("images/episode4/310.webp") with dissolve
                    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is that Katrina? Looking at us!{/i}"
                    scene expression ("images/episode4/311.webp") with dissolve
                    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck... She is!{/i}"

                scene expression ("images/episode4/308.webp") with dissolve
                show ep4_308
                sheila "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nFuck me harder!"
                sheila "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nHARDER!"
                hide ep4_308

                if katrina_path == True:
                    scene expression ("images/episode4/312.webp") with dissolve
                    $ ui.saybehavior()
                    $ ui.interact()
                    scene expression ("images/episode4/313.webp") with dissolve
                    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's so crazy!{/i}"

                scene expression ("images/episode4/309.webp") with dissolve
                show ep4_309
                sheila "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nFuck me harder!"
                sheila "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nHARDER!"
                toby "Apakah Anda menggunakan kontrasepsi?"
                sheila "Tidak ... cum di mulutku!"
                hide ep4_309

                scene expression ("images/episode4/315.webp") with flash
                with flash
                $ unlockImage(persistent.sheila_05)
                $ ui.saybehavior()
                $ ui.interact()
                if katrina_path:
                    scene expression ("images/episode4/316.webp") with dissolve
                    sheila "Ini sangat bagus!"
                    toby "Mmhmm ... ya itu!"
                    scene expression ("images/episode4/317.webp") with dissolve
                    $ ui.saybehavior()
                    $ ui.interact()
                else:
                    pass
                scene expression ("images/episode4/318.webp") with dissolve
                sheila "Ini adalah bercinta paling intens yang pernah saya miliki."
                toby "Saya senang Anda menyukainya!"

                $ unlockMemory(persistent.memory_13)
                $ renpy.end_replay()

            scene expression ("images/episode4/319.webp") with dissolve
            toby "Saya minta maaf sayang. Bos saya hanya meminta saya untuk turun. Tunggu aku di sini, tolong!"
            sheila "Saya harap kita tidak dalam masalah!"
            toby "Jangan khawatir!"

    scene expression ("images/episode4/320.webp") with dissolve
    toby "Anda ingin melihat saya?"
    scene expression ("images/episode4/321.webp") with dissolve
    if ep4_fuckSheila:
        katrina "Ya. Melihat Anda di lantai atas sialan pelacur itu, membuat saya benar -benar terangsang jadi saya akan pergi lebih awal dan pergi bercinta pacar saya."
        katrina "Jadi saya hanya ingin memberi Anda gaji Anda hari ini sebelum saya pergi."
        if katrina_path == True:
            toby "Terima kasih Ma \ 'Am. Ngomong -ngomong, lain kali Anda merasakan ini terangsang, jangan ragu untuk bergabung dengan pesta!"
        else:
            toby "Terima kasih Ma \ 'Am."
    else:
        katrina "Ya, saya akan pergi lebih awal jadi saya hanya ingin memberi Anda bayaran untuk hari ini."

    scene expression ("images/episode4/322.webp") with dissolve
    katrina "Sampai jumpa di hari Minggu!"

    scene expression ("images/episode4/470.webp") with dissolve
    if sheila_path == True:
        sheila "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Yes sir. Everything went according to plan!{/i}"
    else:
        sheila "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I'm sorry, sir. Plan A fizzled out. Moving on to Plan B.{/i}"

    return

label episode4_sheila_apartment:

    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/323.webp") with dissolve
    hide screen ui_message

    sheila "Ini seharusnya segalanya! Terima kasih banyak!"
    toby "Tidak masalah. Jika Anda membutuhkan bantuan saya, hubungi saya!"
    label memory_14:


        scene expression ("images/episode4/324.webp") with dissolve
        sheila "Ingin naik ke atas untuk minum kopi?"
        toby "Kopi? Ya, saya akan menyukainya!"
        scene expression ("images/episode4/325.webp") with dissolve
        sheila "Tolong buat diri Anda nyaman. Saya akan segera kembali!."
        scene expression ("images/episode4/326.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode4/327.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.saybehavior()
        $ ui.interact()

        sheila "Hei seksi, saya harap Anda menyetujui cara saya berterima kasih kepada Anda karena telah membantu saya hari ini."
        toby "Saya akan menjadi gay atau gila untuk tidak menyetujui sesuatu seperti ini."
        scene expression ("images/episode4/328.webp") with dissolve
        toby "Sial, kamu sangat seksi!"
        scene expression ("images/episode4/329.webp") with dissolve
        sheila "Shhh ... biarkan aku menjagamu!"

        scene expression ("images/episode4/330.webp") with dissolve
        show ep4_330
        $ ui.saybehavior()
        $ ui.interact()
        hide ep4_330

        scene expression ("images/episode4/331.webp") with dissolve
        show ep4_331
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's such a tease!{/i}"
        hide ep4_331

        scene expression ("images/episode4/332.webp") with dissolve
        show ep4_332
        $ ui.saybehavior()
        $ ui.interact()
        hide ep4_332

        scene expression ("images/episode4/333.webp") with dissolve
        show ep4_333
        $ ui.saybehavior()
        $ ui.interact()
        hide ep4_333

        scene expression ("images/episode4/334.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}My turn to take care of you now!{/i}"
        sheila "Ya, tolong!"

        scene expression ("images/episode4/335.webp") with dissolve
        show ep4_335
        sheila "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\n{i}Fuck... You're so big!{/i}"
        sheila "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\n{i}Yes... Yes... Give it to me.{/i}"
        hide ep4_335

        scene expression ("images/episode4/336.webp") with dissolve
        show ep4_336
        sheila "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\n{i}Harder... Harder!!! HARDER!!!{/i}"
        hide ep4_336

        scene expression ("images/episode4/337.webp") with dissolve
        show ep4_337
        sheila "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\n{i}Right there... Yes...{/i}"
        sheila "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\n{i}Fuck me!{/i}"
        hide ep4_337

        scene expression ("images/episode4/338.webp") with dissolve
        show ep4_338
        sheila "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\n{i}Yes... Yes... Yesss...{/i}"
        toby "Aku akan cum!"
        sheila "Jangan cum di dalam!"
        hide ep4_338

        scene expression ("images/episode4/339.webp") with flash
        with flash
        pause 1.0
        scene expression ("images/episode4/339_1.webp") with dissolve
        $ unlockImage(persistent.sheila_04)
        toby "Sungguh!"
        scene expression ("images/episode4/340.webp") with dissolve
        sheila "Anda sempurna!"
        sheila "Saya harap ini bukan hal yang satu kali!"
        toby "Jangan khawatir. Anda terlalu panas untuk hanya menjadi stand satu malam."

        $ unlockMemory(persistent.memory_14)
        $ renpy.end_replay()

    scene expression ("images/episode4/471.webp") with long_dissolve
    toby "Tapi, saya benar -benar menyesal harus pergi."
    sheila "Jangan khawatir. Saya tidak berharap untuk berpelukan setelahnya."
    toby "Sampai berjumpa lagi."

    scene expression ("images/episode4/472.webp") with dissolve
    sheila "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Yes sir! Everything went according to plan.{/i}"

    return


label episode4_saturday_morning:
    $ progress = 59
    stop music  fadeout 2.0
    show screen ui_message("Saturday") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()


    play sound "audio/fx/Popular Alarm Clock Sound Effect.mp3"
    scene expression ("images/episode4/341.webp") with dissolve
    hide screen ui_message
    $ ui.saybehavior()
    $ ui.interact()
    stop sound

    scene expression ("images/episode4/342.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* mumbling *{/color}{/size}\n{i}Who the hell sets an alarm on a Saturday?{/i}"
    patricia "Saya lakukan, karena kita harus berlari."
    toby "{size=12}{color=#FDCA6E}* mumbling *{/color}{/size}\n{i}I must still be asleep, because I could have sworn you said \"WE\". {/i}"
    scene expression ("images/episode4/343.webp") with dissolve
    patricia "Oh tolong ... jangan menjadi anak seperti itu. Tolong ikut dengan saya. Anda tahu saya tidak suka berlari sendiri!"
    scene expression ("images/episode4/344.webp") with dissolve
    toby "Ini jam 9 pagi!"
    scene expression ("images/episode4/345.webp") with dissolve
    patricia "Sebenarnya, ini 7:30."
    scene expression ("images/episode4/344.webp") with dissolve
    toby "Apa?"
    scene expression ("images/episode4/345.webp") with dissolve
    patricia "Jadi? Apakah kamu datang?"
    scene expression ("images/episode4/344.webp") with dissolve
    toby "No tidak!"
    scene expression ("images/episode4/346.webp") with dissolve
    patricia "Aku akan membayarmu."
    scene expression ("images/episode4/347.webp") with dissolve
    toby "Anda tidak punya uang!"
    scene expression ("images/episode4/346.webp") with dissolve
    patricia "Siapa yang mengatakan sesuatu tentang uang?"
    scene expression ("images/episode4/348.webp") with dissolve
    patricia "Aku akan membayarmu dengan cinta!"
    patricia "Banyak!"
    scene expression ("images/episode4/349.webp") with dissolve
    toby "Apakah saya terlihat tidak memiliki cinta dan perhatian?"
    patricia "Ya. Anda melakukannya. Dan yang terpenting, Anda merindukan ciuman!"
    scene expression ("images/episode4/350.webp") with dissolve
    toby "Anda mencium mata saya!"
    scene expression ("images/episode4/351.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/352.webp") with dissolve
    toby "Baik ... Baik! Aku datang, berhenti menciumku!"
    scene expression ("images/episode4/353.webp") with dissolve
    patricia "Saya senang saya berhasil meyakinkan Anda tanpa mencium bibir Anda, karena saya pikir saya harus melakukan itu juga."
    toby "Apakah Anda benar -benar berpikir saya akan membiarkan Anda mencium saya tanpa menyikat gigi terlebih dahulu?"
    patricia "Idiot!"
    scene expression ("images/episode4/354.webp") with dissolve
    patricia "Sekarang, bisakah Anda pergi sehingga saya bisa berubah?"
    toby "Anda membangunkan saya hanya untuk mendorong saya keluar dari ruangan?"
    patricia "Saya berpikir untuk menjadi gadis yang baik dan diubah di kamar mandi, tetapi berbahaya meninggalkan Anda sendirian dengan tempat tidur."
    patricia "Kalian berdua memiliki hubungan yang sangat istimewa!"
    scene expression ("images/episode4/355.webp") with dissolve
    toby "Baik ... Aku akan mendapatkan pakaianku."

    scene expression ("images/episode4/356.webp") with long_dissolve
    toby "Jadi? Dimana?"
    patricia "Anda tidak bisa berlari begitu saja. Anda harus meregangkan otot Anda!"
    toby "Ayo sudah pergi sehingga saya bisa kembali tidur!"


    scene expression ("images/episode4/357.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.saybehavior()
    $ ui.interact()

    patricia "Peregangan dulu!"
    scene expression ("images/episode4/358.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It looks like the morning runs are working for her.{/i}"
    scene expression ("images/episode4/359.webp") with dissolve
    patricia "Seberapa jauh pantainya dari sini?"
    toby "Anda ingin lari ke sana?"
    patricia "Ya?"
    scene expression ("images/episode4/360_1.webp") with dissolve
    toby "Bisakah Anda berlari selama 2 jam berturut -turut?"
    scene expression ("images/episode4/360_2.webp") with dissolve
    patricia "Mungkin!"
    scene expression ("images/episode4/361.webp") with dissolve
    toby "Kami pergi ke taman hari ini. Kami akan meninggalkan pantai untuk hari lain!"
    patricia "Tunggu aku!"
    scene expression ("images/episode4/362.webp") with dissolve
    patricia "Jadi, dimana kamu tadi malam?"
    toby "Merindukanku?"
    patricia "Bahkan tidak sedikit. Saya hanya penasaran."
    toby "Saya sedang bekerja."
    scene expression ("images/episode4/363.webp") with dissolve
    if toby_job == 0:
        patricia "Anda bekerja sebagai agen real estat. Mengapa Anda bekerja pada jam itu?"
        toby "Saya memiliki klien yang menyewa salah satu apartemen kami jadi saya harus menunjukkan tempat itu padanya."
        toby "Kemudian lakukan kertas dan sebagainya. Itu sangat terlambat."
        patricia "Pekerjaan Anda aneh. Anda pergi kapan pun Anda mau dan hanya bekerja di malam hari."
        toby "Yah, saya bukan agen. Saya lebih banyak asisten manajer, jadi bekerja untuk semua orang."
        scene expression ("images/episode4/364.webp") with dissolve
        patricia "Jadi apa sebenarnya yang Anda lakukan?"
        toby "Belum yakin. Kemarin saya menandatangani kontrak saya dan dikatakan bahwa saya mendapatkan persentase dari semua penjualan dan persentase yang lebih besar dari penjualan saya sendiri, tetapi juga jadwal saya aneh. Saya hanya pergi ketika bos saya menelepon saya."
    else:

        patricia "Anda hanya bekerja malam di klub?"
        toby "Agak. Maksudku, apa gunanya berada di sana saat klub kosong?"
        patricia "Apa pekerjaan Anda apa sebenarnya di sana?"
        toby "Saya memastikan orang -orang tidak mulai berkelahi."
        patricia "Seperti Anda bisa menghentikan mereka dari melakukan itu."
        toby "Lucu sekali."
        scene expression ("images/episode4/364.webp") with dissolve
        toby "Saya juga memastikan gadis -gadis tidak terganggu oleh orang idiot."
        toby "Dan yang paling penting saya harus mengundang lebih banyak orang ke dalam."
        patricia "Kedengarannya seperti semacam manajer."
        toby "Ya. Lebih kurang!"

    patricia "Apakah Anda bercinta dengan bos baru Anda?"
    toby "Tidak, saya tidak! Saya punya pacar."
    patricia "Ini tidak seperti Anda belum menipu dia!"
    toby "Aku tidak memberitahumu mulai sekarang!"

    scene expression ("images/episode4/365.webp") with dissolve
    toby "Jadi, apakah Anda akan memberi tahu saya mengapa Anda ingin tahu di mana saya tadi malam?"
    patricia "Jangan khawatir tentang itu. Ini baik -baik saja."
    toby "Sekarang saya sangat penasaran."
    patricia "[mom!c] dan [dad] bertengkar tadi malam. Lagi!"
    toby "Neraka berdarah. Mengapa mereka bertarung lagi?"
    scene expression ("images/episode4/366.webp") with dissolve
    patricia "Dia pulang lebih awal dengan bunga membicarakan beberapa hal yang Anda katakan kepadanya dan kemudian meminta [mom] untuk berkencan."
    toby "Jadi apa yang salah?"
    patricia "Saya berada di kamar saya jadi saya tidak mendengar banyak, tetapi mereka berdebat tentang beberapa gaun. Saya pikir sesuatu terjadi pada gaun itu dan dia kesal."
    patricia "Sesuatu seperti dia melempar uang ke jendela!"
    toby "Saya tidak tahu harus berkata apa. Dia adalah [dad] kita, tapi aku membencinya karena bagaimana dia memperlakukan [mom]."
    scene expression ("images/episode4/367.webp") with dissolve
    toby "Bagaimanapun, bagaimana sekolah. Apakah Anda mendapatkan teman baru?"
    toby "Mungkin seorang pacar?"
    patricia "Saya telah menurunkan standar saya dan masih belum ada anak laki -laki yang cukup pintar dan tampan muncul."
    patricia "Saya pikir anak laki -laki seusia saya bodoh."
    scene expression ("images/episode4/368.webp") with dissolve
    toby "Umm ... ya. Saya pikir Anda terlalu berharap dari anak laki -laki."
    toby "Maksudku, sampai aku mencapai 20, aku juga sedikit bodoh."
    patricia "Maksudmu kamu tidak lagi melakukan hal -hal bodoh?"
    toby "Saya lakukan, tetapi tidak sesering. Biasanya anak laki -laki menjadi sedikit lebih dewasa begitu mereka lulus SMA."
    patricia "Ya tapi meski begitu ... Saya tidak ingat Anda menjadi sebodoh ini di sekolah menengah!"
    scene expression ("images/episode4/369.webp") with dissolve
    toby "Saya tidak ingin membual, tetapi Anda tidak akan menemukan pria lain seperti saya."
    patricia "Sempurna!"
    toby "Apa maksudmu, sempurna? Beberapa hari yang lalu Anda mengatakan bahwa Anda ingin menemukan pria seperti saya dan sekarang hanya karena saya membuat kesalahan, saya tidak lagi cukup baik?"
    patricia "Saya tidak akan menjelaskan. Anda mengambilnya sesuka Anda."
    scene expression ("images/episode4/370.webp") with dissolve
    toby "Sekarang saya sangat penasaran."
    patricia "Aku tidak memberitahumu."
    toby "Jadi jika bukan karena saya selingkuh di Emma, lalu apa masalahnya?"
    scene expression ("images/episode4/371.webp") with dissolve
    patricia "Enyah. Aku tidak memberitahumu apa pun."
    toby "Oh ... aku akan menangkapmu dan aku akan memaksanya keluar darimu!"
    patricia "Anda tidak bisa menangkap saya."
    scene expression ("images/episode4/372.webp") with dissolve
    patricia "Aku tidak memberitahumu!"
    toby "Ayo ... jangan menjadi anak seperti itu!"
    scene expression ("images/episode4/373.webp") with dissolve
    toby "Gotcha!"
    scene expression ("images/episode4/374.webp") with dissolve
    toby "Oke, mari kita memilikinya. Apa masalahnya?"
    patricia "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Your penis.{/i}"
    toby "Saya apa? Penisku adalah masalahnya?"
    patricia "Saya tidak akan mengatakan lebih dari itu."
    toby "Tunggu, apa yang salah dengan penisku?"
    scene expression ("images/episode4/375.webp") with dissolve
    patricia "Hal yang Anda sebut ayam sangat besar. Itu akan menyakitkan seperti neraka. Saya tidak ingin pacar dengan penis sebesar itu!"
    toby "Itu masalah Anda? Anda tidak perlu khawatir, kebanyakan pria memiliki ayam kecil."
    patricia "Seberapa kecil?"
    toby "Apakah Anda benar -benar ingin membicarakan hal ini?"
    patricia "Tidak juga ... itu hanya ..."
    scene expression ("images/episode4/376.webp") with dissolve
    toby "Mari kita duduk sebentar."
    scene expression ("images/episode4/377.webp") with dissolve
    toby "Uhmm ... aneh bagiku untuk berbicara denganmu tentang penisku, tapi aku berusaha sekuat mungkin."
    toby "Ukuran berbeda dari manusia ke manusia. Kebanyakan orang tidak memiliki penis yang begitu besar."
    patricia "Tapi kebanyakan orang yang memiliki pornografi memiliki penis besar."
    toby "Karena itu biasanya harus ada di industri itu, tetapi orang normal memiliki penis yang lebih kecil."
    scene expression ("images/episode4/378.webp") with dissolve
    patricia "Jadi Anda bisa bekerja di industri pornografi?"
    toby "Semua orang bisa, tapi ya, mungkin saya akan memiliki kesempatan yang lebih baik untuk dipekerjakan, tetapi seperti yang saya katakan, tidak semua pria berbakat seperti saya."
    patricia "Apakah bagus untuk memiliki penis besar?"
    toby "Saya tidak tahu itu, [sis]. Saya hanya bisa mengatakan bahwa beberapa wanita menyukai ayam besar, sementara yang lain menyukai yang lebih kecil."
    patricia "Dan apa yang diinginkan orang gay?"
    scene expression ("images/episode4/379.webp") with dissolve
    toby "Saya tidak tahu dan saya tidak terlalu penasaran, dan istirahat sudah berakhir."
    patricia "Bagus."
    scene expression ("images/episode4/380.webp") with dissolve
    toby "Jadi hanya untuk rekap, Anda ingin pria seperti saya dengan ayam yang lebih kecil."
    patricia "Dan tidak menipu."
    toby "Haruskah kita membeli beberapa kucing sekarang?"
    scene expression ("images/episode4/381.webp") with dissolve
    patricia "Saya tidak akan berubah menjadi wanita tua dengan 50 kucing."
    toby "Kami akan melihat tentang itu!"


    scene expression ("images/episode4/382.webp") with long_dissolve
    $ progress = 60
    patricia "Bisakah kita berhenti untuk es krim?"
    toby "Apa gunanya melakukan olahraga jika Anda akan makan es krim setelahnya?"
    patricia "Seperti Anda yang tahu apa yang baik atau buruk. Anda tinggal di tempat tidur sepanjang hari."
    toby "Saya pergi ke gym kemarin."
    scene expression ("images/episode4/383.webp") with dissolve
    patricia "Maka itu berarti Anda membakar kalori yang cukup untuk dapat menikmati es krim."
    toby "Baik, tapi Anda membayar kembali!"
    patricia "Anda murah!"
    scene expression ("images/episode4/384.webp") with dissolve
    clerk "Apa yang bisa saya dapatkan dari Anda?"
    patricia "Umm ... saya ingin beberapa ..."
    scene expression ("images/episode4/385.webp") with dissolve
    patricia "Bea?"
    scene expression ("images/episode4/385_1.webp") with dissolve
    beatrice "Tris?"
    scene expression ("images/episode4/385_2.webp") with dissolve
    patricia "Apa yang kamu lakukan di sini?"
    scene expression ("images/episode4/385_3.webp") with dissolve
    beatrice "Nah, ini pekerjaan akhir pekan saya. Orang tua saya memiliki beberapa truk di sekitar kota dan saya dan saudara lelaki saya menghabiskan akhir pekan untuk bekerja."
    patricia "Itu sangat keren."
    beatrice "Jadi apa yang bisa saya dapatkan untuk Anda dan pacar Anda?"
    scene expression ("images/episode4/386.webp") with dissolve
    patricia "Dia? Pacarku? Itu sangat lucu."
    toby "Saya dia [brother]."
    beatrice "Oh, maaf saya buruk!"
    scene expression ("images/episode4/387_0.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    beatrice "Saya beatrice, tetapi orang -orang memanggil saya Bea."

    scene expression ("images/episode4/387.webp") with dissolve
    menu:
        "{i} [JGR] Flirt {/i}"(csq="Beatrice +1"):
            scene expression ("images/episode4/388.webp") with dissolve
            $ beatrice_rel += 1
            toby "I \ 'M [toby!c]. Tapi Anda bisa menelepon saya kapan pun Anda mau."
            scene expression ("images/episode4/389.webp") with dissolve
            patricia "Jangan memperhatikannya. Dia bodoh!"
        "{i} don \ 't flirt {/i}":

            scene expression ("images/episode4/388.webp") with dissolve
            toby "[toby!c]. Senang berkenalan dengan Anda!"

    scene expression ("images/episode4/390.webp") with dissolve
    toby "Jadi, bagaimana kalian berdua saling kenal?"
    beatrice "Kami berada di kelas yang sama."
    patricia "Dia satu -satunya gadis normal di seluruh kelas."
    beatrice "Anda bisa mengatakan bahwa kami adalah satu -satunya gadis normal di kelas itu."
    scene expression ("images/episode4/391_1.webp") with dissolve
    beatrice "Bagaimanapun. Apa yang bisa saya dapatkan dari Anda?"
    scene expression ("images/episode4/392.webp") with dissolve
    patricia "Saya akan punya vanilla dengan stroberi, tolong!"
    scene expression ("images/episode4/391_2.webp") with dissolve
    beatrice "Dan kamu, [toby!c]?"
    scene expression ("images/episode4/393.webp") with dissolve
    toby "Kejutan saya."
    scene expression ("images/episode4/391_2.webp") with dissolve
    beatrice "Katakan padamu, aku akan memberimu rasa favoritku."
    scene expression ("images/episode4/394.webp") with dissolve
    beatrice "Di Sini. Saya harap Anda akan menyukai mereka."
    toby "Berapa banyak kami berhutang budi pada Anda?"
    beatrice "Itu ada di rumah."
    if beatrice_rel == 1:
        menu:
            "{i} [JGR] bersikeras membayar {/i}"(csq="Beatrice Path Opens & Galeri Gambar"):
                $ beatrice_path = True
                $ unlockImage(persistent.beatrice_01)
                toby "Akan sangat memalukan untuk memberikannya secara gratis.Saya minta maaf, tapi saya tidak bisa menerimanya. Masalah Anda perlu dihargai. Anda menempatkan jiwa Anda ke dalam es krim ini."
                scene expression ("images/episode4/395.webp") with dissolve
                beatrice "Terima kasih, [toby!c]."
                toby "Tidak masalah sayang!"
            "Apakah kamu yakin itu oke?":

                beatrice "Ya ... jangan khawatir."
    else:
        toby "Apakah kamu yakin itu oke?"
        beatrice "Ya ... jangan khawatir!"

    scene expression ("images/episode4/396.webp") with dissolve
    toby "Terima kasih atas es krimnya, Bea!"
    beatrice "Pastikan untuk mengunjungi kami lagi."
    patricia "Anda bertaruh!"

    if beatrice_path == True:
        scene expression ("images/episode4/397.webp") with dissolve
        patricia "Itu halus!"
        toby "Oh tolong ... saya tidak melakukan apa pun."
        patricia "Of course. \"DEAR\"."
        scene expression ("images/episode4/397_1.webp") with dissolve
        toby "Moron!"
    else:
        scene expression ("images/episode4/397.webp") with dissolve
        patricia "Jadi? Apakah kamu menyukainya?"
        toby "Saya punya pacar."
        patricia "Tidak seperti itu menghentikan Anda sebelumnya."
        scene expression ("images/episode4/397_1.webp") with dissolve
        toby "Jangan menjadi hag tua!"

    scene expression ("images/episode4/398.webp") with dissolve
    patricia "Hei!, Apa -apaan, idiot!"
    scene expression ("images/episode4/399.webp") with dissolve
    toby "Maaf, saya tidak bermaksud menabrak siku Anda!"
    patricia "Cukup bersihkan, aku tidak punya tisu."
    toby "Gunakan jari Anda."
    patricia "Mereka akan menjadi lengket. Tidak bisakah kamu menggunakan milikmu?"
    toby "Anda diva seperti itu!"
    scene expression ("images/episode4/400.webp") with dissolve
    patricia "Silakan?"
    menu:
        "{i} Gunakan jari Anda {/i}":
            scene expression ("images/episode4/401.webp") with dissolve
            patricia "Terima kasih!"
            toby "Apa yang bisa saya katakan. Untuk apa sebesar itu!"
        "{i} [JGR] Jilat es krim {/i}"(csq="Tris +1 & Galeri Gambar"):
            $ patricia_rel += 1
            $ unlockImage(persistent.patricia_10)
            scene expression ("images/episode4/402.webp") with dissolve
            patricia "Apa yang kamu lakukan, [toby!c]?"
            scene expression ("images/episode4/403.webp") with dissolve
            toby "Tidak membuat tanganku lengket!"
            patricia "Moron!"
            toby "Idiot!"

    scene expression ("images/episode4/404.webp") with fade

    toby "Dan akhirnya, kami pulang. Tidak bisa menunggu untuk mandi. Saya berbau!"
    patricia "Sayang sekali kami hanya memiliki satu mandi dan saya akan menjadi yang pertama menggunakannya, jadi terbiasa dengan bau Anda!"
    scene expression ("images/episode4/405.webp") with dissolve
    toby "Tidak, Anda tidak!"
    patricia "[toby!c] !!! Tidakkah kamu tahu bagaimana menjadi seorang pria?"
    toby "Saya lakukan, tetapi tidak untuk seseorang yang membangunkan saya pada jam 7 pagi untuk berlari."
    scene expression ("images/episode4/406.webp") with dissolve
    patricia "Saya benar -benar perlu mandi dulu!"
    toby "Jadi saya!"
    scene expression ("images/episode4/407.webp") with dissolve
    patricia "Anda sangat bodoh!"
    toby "Anda bodoh! Saya sampai di sini dulu."
    scene expression ("images/episode4/408.webp") with dissolve
    patricia "Mengapa Anda selalu harus seperti itu?"
    scene expression ("images/episode4/409.webp") with dissolve
    toby "Aku akan mandi dengan atau tanpa kamu di kamar mandi."
    scene expression ("images/episode4/410.webp") with dissolve
    patricia "Tidak, Anda tidak, karena saya akan mandi dengan atau tanpa Anda ada."
    toby "Apakah Anda benar -benar ingin bermain game ini?"
    patricia "Anda tidak tahu dengan siapa Anda mengacaukan!"
    scene expression ("images/episode4/411.webp") with dissolve
    toby "Kamu juga tidak."
    patricia "Anda baru saja menjatuhkan celana Anda. Wow."
    scene expression ("images/episode4/412.webp") with dissolve
    patricia "Saya akan mandi, jadi silakan pergi."
    toby "Apakah Anda akan mandi di pakaian dalam Anda?"
    patricia "Saya menunggu Anda pergi!"
    scene expression ("images/episode4/413.webp") with dissolve
    toby "Sayang sekali, karena saya tidak akan pergi sampai saya selesai!"
    scene expression ("images/episode4/414.webp") with dissolve
    patricia "Eww ... aku [sister], tolol. Anda tidak seharusnya menunjukkan penis Anda!"
    toby "Aku menyuruhmu pergi. Bukankah aku?"
    scene expression ("images/episode4/415.webp") with dissolve
    patricia "Asal tahu saja, saya tidak tahu mengapa saya begitu takut. Anda sebenarnya memiliki penis kecil!"
    toby "Kenapa kamu masih di sini?"
    patricia "Idiot!"
    scene expression ("images/episode4/416.webp") with dissolve

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I think I might have pushed the issue, but at least I'm the first to take a shower!{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I can't believe my little [sister] got undressed in front of me just to prove a point.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I was not expecting her to go that far.{/i}"
    scene expression ("images/episode4/417.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Although it was funny!{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I just hope she won't tell [mom] what happened, after what happened yesterday, I doubt she'd like to hear about this also.{/i}"

    $ progress = 61
    scene expression ("images/episode4/418.webp") with long_dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This was so refreshing!{/i}"
    scene expression ("images/episode4/419.webp") with dissolve
    charlotte "Anda lebih awal!"
    toby "Ya ... Tris membangunkan saya untuk berlari."
    charlotte "Aku tahu. Dia meminta saya kemarin untuk bergabung dengannya dan saya menyuruhnya membangunkan Anda!"
    scene expression ("images/episode4/420.webp") with dissolve
    toby "Mustahil! Jadi Anda alasan saya harus bangun jam 7 pagi?"
    scene expression ("images/episode4/421.webp") with dissolve
    charlotte "Bersalah, tetapi dalam pembelaan saya, saya harus memastikan Anda berada dalam kondisi terbaik Anda untuk hari ini."
    scene expression ("images/episode4/420.webp") with dissolve
    toby "Hari ini?"
    scene expression ("images/episode4/421.webp") with dissolve
    charlotte "Jangankah Anda ingat apa yang harus Anda lakukan hari ini?"
    scene expression ("images/episode4/422.webp") with dissolve
    toby "Saya tidak punya pekerjaan rumah, bukan?"
    scene expression ("images/episode4/421.webp") with dissolve
    charlotte "Anda tidak mengerjakan pekerjaan rumah Anda ketika Anda masih di sekolah menengah, apakah Anda akan melakukan beberapa sekarang?"
    scene expression ("images/episode4/422.webp") with dissolve
    toby "Titik wajar."
    scene expression ("images/episode4/421.webp") with dissolve
    charlotte "Jadi ... apakah Anda ingat apa yang Anda janjikan kepada saya?"
    scene expression ("images/episode4/423.webp") with dissolve
    toby "Saya sudah membuat reservasi untuk teman kencan kami, jangan Anda khawatir!"
    toby "Malam ini saya akan memastikan Anda melupakan semua masalah Anda."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit, I completely forgot about our bet. I need to find a nice restaurants around.{/i}"
    scene expression ("images/episode4/424.webp") with dissolve
    charlotte "Glad to hear you didn't forgot about our so called \"DATE\"."
    scene expression ("images/episode4/423.webp") with dissolve
    toby "Anda hanya memastikan Anda berpakaian bagus untuk membuat saya terkesan."
    scene expression ("images/episode4/424.webp") with dissolve
    charlotte "Saya akan melakukan yang terbaik!"

    return


label episode4_saturday_date:
    $ progress = 62
    show screen ui_message("Later that day") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/425_1.webp") with dissolve
    hide screen ui_message


    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why the hell am I so nervous?{/i}"
    scene expression ("images/episode4/425_2.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/426_1.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It's not like I'm going on an actual date. I'm just going out with my [mom].{/i}"
    scene expression ("images/episode4/426_2.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/425_1.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I shouldn't be nervous.{/i}"
    scene expression ("images/episode4/425_2.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode4/426_1.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yet I'm pacing around the house like a kid on his first date.{/i}"
    scene expression ("images/episode4/426_2.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode4/427.webp") with dissolve
    charlotte "Sayang yang gugup?"
    toby "Tidak ... hanya ingin keluar."
    charlotte "Bagus!"
    charlotte "Jadi? Bagaimana penampilan saya?"

    scene expression ("images/episode4/428.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.saybehavior()
    $ ui.interact()

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She looks stunning!{/i}"

    charlotte "Saya harap saya tidak terlalu berpakaian."
    toby "Don't worry [mom], you look perfect for this \"date\"Lai"

    scene expression ("images/episode4/429.webp") with dissolve
    charlotte "Tonight I'm Charlotte, so it feels more like \"date\", jika itu adalah kata yang akan kita gunakan untuk ini."
    toby "Oke Charlotte."
    scene expression ("images/episode4/430.webp") with dissolve
    toby "Haruskah kita?"
    charlotte "Anda mendapatkan kunci mobil?"
    toby "Malam ini kami akan meninggalkan mobil pulang, karena saya tidak akan membiarkan Anda bersenang -senang sendiri!"
    scene expression ("images/episode4/431.webp") with long_dissolve
    toby "Izinkan saya!"
    charlotte "Betapa prianya! Saya tidak tahu saya membesarkan pria seperti itu."
    toby "Dinaikkan? Saya pikir kita bukan [son] dan [mother] malam ini."
    scene expression ("images/episode4/432.webp") with dissolve
    charlotte "Maksudku, siapa pun yang membesarkanmu melakukan pekerjaan dengan baik!"
    toby "Saya pasti akan memberi tahu dia!"
    scene expression ("images/episode4/433.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Tonight it's going to be fun. I like pretending I'm on a date with my [mom]. It's funny.{/i}"
    scene expression ("images/episode4/434.webp") with dissolve
    charlotte "Jadi? Kemana kamu membawaku malam ini, [toby!c]?"
    toby "Nah, Charlotte, saya tidak mengatakan karena itu mengejutkan. Tapi saya yakin Anda akan menyukainya."
    charlotte "Apakah kamu pernah ke sana sebelumnya?"
    toby "Umm ... tidak, tapi itu memiliki ulasan yang bagus."
    scene expression ("images/episode4/435.webp") with dissolve
    charlotte "Anak muda!"
    toby "Jika Anda tidak suka, kami akan mengulang tanggal Sabtu depan!"
    scene expression ("images/episode4/436.webp") with dissolve
    charlotte "Jangan beri saya ide!"
    toby "Tidak, tidak ... kami tidak bermain seperti itu. Anda tidak akan bisa berbohong padaku!"
    charlotte "Baik ... saya menang!"

    scene expression ("images/episode4/437.webp") with long_dissolve
    $ progress = 63
    toby "Dan kami di sini!"
    charlotte "Saya merasa tidak enak sekarang, membuat Anda membawa saya ke restoran yang bagus. Saya akan mengurus tagihan."
    toby "Anda akan melakukannya. Saya tidak mengizinkan Anda membayar pada kencan pertama kami!"
    scene expression ("images/episode4/438.webp") with dissolve
    charlotte "Kencan pertama? Haruskah saya mengharapkan lebih?"
    toby "Nah Anda memang mengatakan bahwa Anda mungkin tidak suka di sini jadi saya harus membawa Anda ke tempat lain Sabtu depan!"
    charlotte "Apa yang tidak disukai di sini? Lihat saja tempat ini! Dan saya masih merasa tidak enak karena membuat Anda membawa saya ke sini."
    scene expression ("images/episode4/439.webp") with dissolve
    toby "Malam ini tentang Anda [mom]. Maksud saya Charlotte."
    toby "Anda melakukan banyak hal untuk kami. Bagi saya, untuk Tris. Anda pantas mendapatkan yang terbaik, jadi tolong berhenti mengkhawatirkan tagihan atau apa pun."
    charlotte "Anda sangat manis. Terima kasih."
    scene expression ("images/episode4/440_smile.webp") with dissolve
    charlotte "Saya sangat senang Anda tidak seperti [father] Anda. Calon istri Anda akan menjadi wanita paling bahagia di dunia."
    scene expression ("images/episode4/441_laugh.webp") with dissolve
    toby "Itu jauh dari jauh. Saya tidak berpikir untuk menikah sampai saya setidaknya 28."
    scene expression ("images/episode4/440_laugh.webp") with dissolve
    charlotte "Pria pintar. Nanti Anda akan menikah nanti Anda bisa bertengkar dengan istri Anda."
    scene expression ("images/episode4/441_sad.webp") with dissolve
    toby "Berbicara tentang perkelahian, mengapa Anda dan [dad] bertarung tadi malam? Tris memberitahuku bahwa kamu terlibat pertarungan lain."
    toby "Saya pikir membawanya ke gym untuk melepaskan beberapa uap akan membantu."
    scene expression ("images/episode4/440_awkward.webp") with dissolve
    charlotte "Kami hampir keluar, tetapi kemudian dia meminta saya untuk mengenakan gaun yang saya kenakan ke acara itu."
    scene expression ("images/episode4/441_curious.webp") with dissolve
    toby "Maksud Anda gaun yang Anda potong sehingga Anda bisa naik sepeda motor?"
    scene expression ("images/episode4/440_awkward.webp") with dissolve
    charlotte "Yup. Exactly that one, and you can bet he didn't like the fact that I \"ruined\"gaun baru."
    scene expression ("images/episode4/440_smile.webp") with dissolve
    charlotte "Ngomong -ngomong, jangan membicarakannya. Saya sangat ingin melupakan masalah saya malam ini."
    charlotte "Anda berjanji kepada saya."
    scene expression ("images/episode4/441_laugh.webp") with dissolve
    toby "Saya tidak ingat bahwa saya berjanji, tetapi saya mengatakan kami akan mencoba."
    scene expression ("images/episode4/442.webp") with dissolve
    waitress "Selamat datang. Apa yang bisa saya dapatkan dari malam ini?"
    toby "Halo. Apa steak terbaikmu?"
    waitress "Nah, saya akan merekomendasikan steak T-bone kami dalam saus anggur jamur yang dipasangkan dengan kentang panggang dan medley wortel & wortel."
    toby "Sempurna, kami akan memiliki dua medium langka."
    waitress "Dan apakah Anda menginginkan sesuatu dari daftar anggur kami? Kami memiliki anggur Prancis yang sangat eksklusif."
    toby "Ya tolong, kedengarannya bagus! Sebotol Cabernet Sauvignon terbaik Anda akan bekerja dengan baik."
    waitress "Aku akan kembali sebentar lagi."

    scene expression ("images/episode4/440_flirty.webp") with dissolve
    charlotte "Anda benar -benar ingin membuat saya terkesan?"
    scene expression ("images/episode4/441_laugh.webp") with dissolve
    toby "Uhmm? Saya tidak yakin apa yang Anda maksud."
    scene expression ("images/episode4/440_smile.webp") with dissolve
    charlotte "Anda terlihat sangat percaya diri, lucu untuk melihat seberapa banyak Anda telah tumbuh."
    scene expression ("images/episode4/441_awkward.webp") with dissolve
    toby "Anda akan membuat saya memerah."
    scene expression ("images/episode4/440_smile.webp") with dissolve
    charlotte "Baik ... Aku tidak akan memberikan tekanan lagi padamu."
    scene expression ("images/episode4/441_curious.webp") with dissolve
    toby "Jadi? Bagaimana hari Anda [mom]?"
    scene expression ("images/episode4/440_flirty.webp") with dissolve
    charlotte "Maksudmu, Charlotte!"
    scene expression ("images/episode4/441_laugh.webp") with dissolve
    toby "Maaf! Jadi? Bagaimana hari Anda, Charlotte?"
    scene expression ("images/episode4/440_smile.webp") with dissolve
    charlotte "Buruk sekali. Saya memberi diri saya mulas melihat -lihat ide -ide halaman."
    scene expression ("images/episode4/441_laugh.webp") with dissolve
    toby "Anda ingin merenovasi halaman kami?"
    scene expression ("images/episode4/440_normal.webp") with dissolve
    charlotte "Tidak? Mungkin rumput yang bagus dengan kolam kecil."
    scene expression ("images/episode4/441_laugh.webp") with dissolve
    toby "Anda menyadari bahwa halaman kami adalah ukuran ruangan. Di mana kita pas dengan kolam kecil?"
    scene expression ("images/episode4/440_laugh.webp") with dissolve
    charlotte "Bagus. Jacuzzi kecil dan dua kursi lounger."
    scene expression ("images/episode4/441_curious.webp") with dissolve
    toby "Mengapa Anda tidak pergi ke pantai saja? Ini tidak sejauh itu."
    scene expression ("images/episode4/440_awkward.webp") with dissolve
    charlotte "Aku terlalu sadar diri untuk tan di sana!"
    scene expression ("images/episode4/441_laugh.webp") with dissolve
    toby "Apakah kamu sekarang? Saya telah melihat Anda di pantai. Anda tampak sangat nyaman."
    scene expression ("images/episode4/440_shy.webp") with dissolve
    charlotte "Saya tidak topless. Saya tidak ingin garis tan dan saya tidak bisa melakukannya di pantai."
    scene expression ("images/episode4/441_awkward.webp") with dissolve
    toby "Oh ... aku tidak mengharapkan itu!"
    scene expression ("images/episode4/441_laugh.webp") with dissolve
    toby "Aku akan merenovasi halaman untukmu."
    scene expression ("images/episode4/440_laugh.webp") with dissolve
    charlotte "Saya menghargainya, tetapi prioritasnya adalah merenovasi loteng!"
    scene expression ("images/episode4/440_smile.webp") with dissolve
    charlotte "Anda terlalu tua untuk tidur di tempat tidur yang sama dengan [sister] Anda."
    scene expression ("images/episode4/441_laugh.webp") with dissolve
    toby "Bagus. Setelah saya merenovasi loteng, saya akan melakukan halaman!"
    scene expression ("images/episode4/440_normal.webp") with dissolve
    charlotte "Jangan khawatir sayang. [father] Anda dan saya akan mengurus halaman. Anda masih muda. Anda memiliki hal -hal yang lebih baik untuk dilakukan dengan uang Anda."
    scene expression ("images/episode4/441_laugh.webp") with dissolve
    toby "Jangan khawatir. Saya masih bisa membawa Anda ke restoran mewah bahkan jika saya berinvestasi di halaman."
    scene expression ("images/episode4/440_laugh.webp") with dissolve
    charlotte "Betapa bijaksana!"
    scene expression ("images/episode4/440_smile.webp") with dissolve
    charlotte "Aku mencintaimu, [toby!c]."
    scene expression ("images/episode4/441_laugh.webp") with dissolve
    toby "Sekarang, sekarang! Kami berada di kencan pertama kami dan Anda sudah mengatakan Anda mencintaiku. Saya suka kecepatan yang kami lakukan."
    scene expression ("images/episode4/443.webp") with dissolve
    charlotte "Anda seperti orang bodoh!"
    toby "Aku juga mencintaimu, Charlotte!"
    scene expression ("images/episode4/444.webp") with dissolve
    charlotte "Saya masih tidak percaya Anda menerima taruhan itu dengan saya."
    toby "Bagaimana saya bisa tahu bahwa Anda begitu pandai di kolam renang?"
    scene expression ("images/episode4/445.webp") with dissolve
    charlotte "Saya perlu memberi tahu Anda lebih banyak tentang masa muda saya."
    toby "Tolong lakukan. Saya ingin tahu. Jika saya membawa Anda ke jajaran penembakan, apakah Anda akan membuat saya terlihat seperti orang bodoh?"
    scene expression ("images/episode4/446.webp") with dissolve
    charlotte "Terima kasih, sayang!"
    waitress "Terima kasih kembali!"
    scene expression ("images/episode4/447.webp") with dissolve
    charlotte "Siapa tahu. Mungkin!"
    charlotte "Saya tidak akan membuat taruhan lain jika saya adalah Anda."
    toby "Baik, saya akan menemukan sesuatu yang lebih baik dari saya dan kemudian saya akan membuat Anda membawa saya keluar berkencan!"
    charlotte "Sempurna."
    scene expression ("images/episode4/448.webp") with dissolve
    charlotte "Mmm ... steak ini terlihat lezat."
    toby "Biarkan makan."


    scene expression ("images/episode4/449_smile.webp") with long_dissolve
    charlotte "Saya masih merasa tidak enak karena membuat Anda membawa saya ke restoran yang begitu bagus, tetapi makanannya sangat baik, jadi jika saya harus membuat taruhan yang sama lagi, saya akan melakukannya!"
    scene expression ("images/episode4/450_laugh.webp") with dissolve
    toby "Itu membatalkan gagasan merasa buruk."
    scene expression ("images/episode4/449_laugh.webp") with dissolve
    charlotte "Mungkin, tapi hanya sedikit."
    scene expression ("images/episode4/449_flirty.webp") with dissolve
    charlotte "Kencan saya lucu. Anggurnya bagus. Tapi bisakah kamu menyalahkanku? Saya tidak punya siapa -siapa untuk bertengkar.Maksud saya malam ini sempurna. Makanannya sempurna."
    scene expression ("images/episode4/450_smile.webp") with dissolve
    toby "Saya senang Anda merasa baik."
    scene expression ("images/episode4/449_laugh.webp") with dissolve
    charlotte "Satu -satunya hal yang hilang adalah alasan bagi saya untuk memakai pakaian dalam seksi yang saya beli tempo hari."
    scene expression ("images/episode4/450_flirty.webp") with dissolve
    toby "Nah jika Anda sangat ingin memakainya, kami bisa pulang dan setelah semua orang tertidur, Anda bisa memakainya sebanyak yang Anda inginkan. Jika Anda suka, saya dapat mengirimi Anda teks saat saya tertidur."
    scene expression ("images/episode4/449_laugh.webp") with dissolve
    charlotte "Bagaimana Anda akan mengirimi saya teks jika Anda tidur."
    scene expression ("images/episode4/450_smile.webp") with dissolve
    toby "Saya akan menemukan jalan, jangan Anda khawatir tentang saya."
    scene expression ("images/episode4/449_sad.webp") with dissolve
    charlotte "Apa gunanya mengenakan pakaian dalam 00 jika tidak ada yang melihat saya di dalamnya?"
    scene expression ("images/episode4/450_flirty.webp") with dissolve
    toby "Baik, Anda meyakinkan saya, saya akan tetap terjaga."
    scene expression ("images/episode4/449_wine.webp") with dissolve
    charlotte "Saya tidak tahu apakah itu anggur, tetapi untuk beberapa alasan saya menjadi sangat terangsang sekarang."
    scene expression ("images/episode4/450_flirty.webp") with dissolve
    toby "Haruskah saya membeli botol lain?"
    scene expression ("images/episode4/449_laugh.webp") with dissolve
    charlotte "Tidak ... tidak apa -apa. Saya bukan tipe wanita yang berhubungan seks di kencan pertama."
    scene expression ("images/episode4/450_wine.webp") with dissolve
    toby "Saya pikir Anda memiliki satu gelas anggur terlalu banyak. Saya akan menyelesaikan ini sendiri."
    scene expression ("images/episode4/449_smile.webp") with dissolve
    charlotte "Hati -hati, karena Anda mungkin juga benar -benar terangsang!"
    scene expression ("images/episode4/450_smile.webp") with dissolve
    toby "Saya harus hidup dengannya."
    scene expression ("images/episode4/449_laugh.webp") with dissolve
    charlotte "Tidak ada yang bisa Anda perbaiki dengan brengsek, bukan?"
    scene expression ("images/episode4/450_laugh.webp") with dissolve
    toby "Anda kotor. Apakah Anda berpikir tentang masturbasi [son] Anda?"
    scene expression ("images/episode4/449_flirty.webp") with dissolve
    charlotte "Saya [son]? Saya tidak tahu apa yang Anda bicarakan. Saya pikir kami \ 're charlotte dan [toby!c] malam ini."
    scene expression ("images/episode4/449_normal.webp") with dissolve
    charlotte "Tapi saya pikir kita harus menghentikan ini. Ini terlalu seksual."
    charlotte "Untuk kencan pertama."
    scene expression ("images/episode4/450_normal.webp") with dissolve
    toby "Ya, saya pikir Anda benar. Saya akan meminta cek dan kita bisa pulang."
    scene expression ("images/episode4/449_flirty.webp") with dissolve
    charlotte "Or maybe, we can go back to that bar for another game of pool and I can release the \"tiger\"lagi?"
    scene expression ("images/episode4/450_laugh.webp") with dissolve
    toby "Pertama, tidak, karena saya tidak suka menendang pantat saya. Dan kedua, saya cukup yakin semua orang di bar itu mengira Anda seorang cougar, bukan harimau."
    scene expression ("images/episode4/449_normal.webp") with dissolve
    charlotte "Dan itu mengganggu Anda bahwa orang -orang mengira Anda keluar dengan cougar?"
    scene expression ("images/episode4/450_flirty.webp") with dissolve
    toby "Tidak tidak tidak! Apakah Anda bercanda? Pria mana pun akan menganggap dirinya beruntung sekali untuk keluar dengan seorang wanita sepanas Anda!"
    scene expression ("images/episode4/450_awkward.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Holy shit, did I just tell my [mom] I thought she was hot?!?!{/i}"
    scene expression ("images/episode4/449_flirty.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Dammit. Yes, yes I did. Shit.{/i}"
    scene expression ("images/episode4/449_normal.webp") with dissolve
    charlotte "Wow, terima kasih sayang. Anda tidak tahu seberapa besar pendengarannya bagi saya saat ini."
    scene expression ("images/episode4/449_laugh.webp") with dissolve
    charlotte "Dan kali ini, saya bisa memilih taruhan.Dan itu baik -baik saja, kami tidak ingin Anda malu. Saya akan memberi Anda waktu untuk berlatih. Tapi Anda masih akan kalah."
    scene expression ("images/episode4/450_smile.webp") with dissolve
    toby "Kesepakatan!"


    scene expression ("images/episode4/451.webp") with long_dissolve
    $ progress = 64
    charlotte "Terima kasih banyak untuk malam ini! Anda adalah pria yang sempurna."
    toby "Saya senang Anda menyukainya. Kami dapat melakukan ini lebih sering, Anda tahu."
    charlotte "Saya akan menyukainya."
    scene expression ("images/episode4/452.webp") with dissolve
    charlotte "Untuk beberapa alasan saya tidak ingin kembali ke dalam. Malam ini saya merasa muda untuk pertama kalinya selamanya!"
    charlotte "Saya tahu ini bukan tanggal atau apa pun. Saya seorang wanita yang sudah menikah dan selain itu, Anda adalah [son] saya, tetapi saya tidak ingin itu berakhir."
    scene expression ("images/episode4/453.webp") with dissolve
    toby "Saya senang Anda sangat menikmatinya!"
    charlotte "Saya akan meminta Anda untuk masuk, tetapi saya tidak melakukan itu pada kencan pertama."
    toby "Jadi haruskah saya menunggu selama 5 menit sebelum masuk ke dalam?"
    scene expression ("images/episode4/454.webp") with dissolve
    charlotte "Itu bisa berhasil."
    scene expression ("images/episode4/453.webp") with dissolve
    toby "Berbicara tentang hal -hal yang tidak kita lakukan pada tanggal pertama. Aku akan menciummu sekarang, tapi apa yang bisa aku katakan. Saya juga bukan tipe orang yang mencium pada kencan pertama, juga."
    charlotte "Ya ... Sayang sekali kita bukan tipe orang seperti itu."
    menu:
        "{i} [JGR] Cium pipinya {/i}"(csq="Charlotte +1 & Penting untuk Path Charlotte \ '"):
            $ charlotte_rel += 1
            $ ep4_charlotteMovie = True
            scene expression ("images/episode4/455.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode4/456.webp") with dissolve
            charlotte "Aku mencintaimu, [toby!c]."
            toby "Aku juga mencintaimu, [mom]."
        "{i} Say Goodbye {/i}":

            toby "Saya senang kita harus menghabiskan waktu bersama."


    if charlotte_rel >= 7:

        scene expression ("images/episode4/457.webp") with dissolve
        toby "Karena tidak satu pun dari kita yang ingin tanggal ini berakhir, merawat film?"
        charlotte "Itu akan bagus, tetapi saya perlu berubah menjadi sesuatu yang lebih nyaman."

        label memory_15:


            scene expression ("images/episode4/458.webp") with long_dissolve
            charlotte "Jadi? Apa yang kita tonton?"
            scene expression ("images/episode4/459.webp") with dissolve
            toby "Wow ... kamu terlihat cantik."

            $ unlockImage(persistent.charlotte_10)
            scene expression ("images/episode4/460.webp") with dissolve:
                yalign 1.0
                linear 10.0 yalign 0.0

            $ ui.saybehavior()
            $ ui.interact()

            charlotte "Benar-benar? Saya tidak akan mengatakan itu. Saya hanya mengambil sesuatu dari lemari dan turun."

            scene expression ("images/episode4/461.webp") with dissolve
            toby "Dan hal pertama yang Anda temukan kebetulan adalah pakaian dalam seksi yang Anda bicarakan di restoran?"
            charlotte "Anda membuat saya merasa sangat cantik, dihargai dan dicintai. Dan saya menyukai perasaan itu."
            charlotte "Dan pakaian dalam ini membuatku merasa seksi dan cantik."
            scene expression ("images/episode4/462.webp") with dissolve
            toby "Anda sempurna, [mom]."
            charlotte "Terima kasih."
            charlotte "Jadi? Apa yang kita tonton?"
            scene expression ("images/episode4/463.webp") with dissolve
            toby "Saya menemukan dua film. Sebuah film aksi tentang beberapa pencuri mobil dan yang lainnya beberapa film romantis tentang seorang wanita yang belum menua."
            charlotte "Nah, karena Anda membuat saya merasa sangat muda malam ini, saya ingin menonton film romantis!"
            toby "Sempurna ... biarkan menonton."
            scene expression ("images/episode4/464.webp") with dissolve
            charlotte "Biarkan saya membuat diri saya nyaman dulu."

            show screen ui_message("2 hours later") with long_dissolve
            $ ui.saybehavior()
            $ ui.interact()


            scene expression ("images/episode4/465.webp") with dissolve
            hide screen ui_message
            charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Looks like someone fell asleep.{/i}"
            scene expression ("images/episode4/466.webp") with dissolve
            charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Good night handsome.{/i}"
            scene expression ("images/episode4/467.webp") with dissolve
            charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I'll just lay here with you sweetie.{/i}"
            $ unlockMemory(persistent.memory_15)
            $ renpy.end_replay()

        scene expression ("images/episode4/476.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()


        scene expression ("images/episode4/473.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
    else:

        scene expression ("images/episode4/457.webp") with dissolve
        charlotte "Biarkan masuk ke dalam."
        scene expression ("images/episode4/468.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode4/474.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode4/475.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    scene expression ("images/episode4/477.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if ep3_lieGirls == True:
        scene expression ("images/episode4/479.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0
        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

    scene expression ("images/episode4/478.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode4/480.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
