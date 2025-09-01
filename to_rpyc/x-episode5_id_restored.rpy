image ep5_106 = Movie(play="video/episode5/106.webm", loop = True)
image ep5_107 = Movie(play="video/episode5/107.webm", loop = True)
image ep5_109 = Movie(play="video/episode5/109.webm", loop = True)
image ep5_110 = Movie(play="video/episode5/110.webm", loop = True)
image ep5_111 = Movie(play="video/episode5/111.webm", loop = True)
image ep5_112 = Movie(play="video/episode5/112.webm", loop = True)
image ep5_134 = Movie(play="video/episode5/134.webm", image="images/episode5/134.webp", loop = False)
image ep5_176 = Movie(play="video/episode5/176.webm", image="images/episode5/176.webp", loop = False)
image ep5_276 = Movie(play="video/episode5/276.webm", image="images/episode5/276.webp", loop = False)
image ep5_278 = Movie(play="video/episode5/278.webm", loop = True)
image ep5_285 = Movie(play="video/episode5/285.webm", image="images/episode5/285.webp", loop = False)
image ep5_286 = Movie(play="video/episode5/286.webm", loop = True)
image ep5_299 = Movie(play="video/episode5/299.webm", loop = True)
image ep5_300 = Movie(play="video/episode5/300.webm", loop = True)
image ep5_301 = Movie(play="video/episode5/301.webm", loop = True)
image ep5_302 = Movie(play="video/episode5/302.webm", loop = True)
image ep5_303 = Movie(play="video/episode5/303.webm", loop = True)
image ep5_317 = Movie(play="video/episode5/317.webm", image="images/episode5/318.webp", loop = False)
image ep5_336 = Movie(play="video/episode5/336.webm", loop = True)
image ep5_337 = Movie(play="video/episode5/337.webm", loop = True)
image ep5_338 = Movie(play="video/episode5/338.webm", loop = True)
image ep5_339 = Movie(play="video/episode5/339.webm", loop = True)


label episode5:
    stop music fadeout 4.0
    $ progress = 65
    scene expression ("images/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(1, 5) with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    call episode5_sunday_morning from _call_episode5_sunday_morning
    call episode5_sunday_emma from _call_episode5_sunday_emma
    call episode5_gym from _call_episode5_gym
    if ep3_lieGirls == True:
        if lisa_path == True:
            call episode5_sunday_dateLisa from _call_episode5_sunday_dateLisa
        else:
            call episode5_sunday_dateLauren from _call_episode5_sunday_dateLauren

        call episode5_sunday_clubDrive from _call_episode5_sunday_clubDrive
    else:

        call episode5_sunday_clubAlone from _call_episode5_sunday_clubAlone
        if lisa_path == True:
            call episode5_sunday_club_lisa from _call_episode5_sunday_club_lisa
        elif lauren_path:
            call episode5_sunday_club_lauren from _call_episode5_sunday_club_lauren

    if lisa_path or lauren_path:
        call episode5_sunday_clubDance from _call_episode5_sunday_clubDance
        if lisa_path:
            call episode5_sunday_night_lisa from _call_episode5_sunday_night_lisa
        else:
            call episode5_sunday_night_lauren from _call_episode5_sunday_night_lauren

    call episode5_sunday_night from _call_episode5_sunday_night

    call episode5_monday_morning from _call_episode5_monday_morning

    call episode5_monday_evening from _call_episode5_monday_evening

    if beatrice_path:
        call episode5_monday_beatrice from _call_episode5_monday_beatrice

    call episode5_monday_night from _call_episode5_monday_night


    return


label episode5_sunday_morning:
    $ progress = 66
    show screen ui_message("Sunday") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()


    if charlotte_rel < 7:
        scene expression ("images/episode5/001.webp") with dissolve
        hide screen ui_message
        hide screen ui_newEpisode
        $ ep4_nightWithCharlotte = False
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Wow, I slept so well. I can't remember the last time slept this good.{/i}"
        scene expression ("images/episode5/002.webp") with dissolve
        toby "Pagi!"
    else:
        scene expression ("images/episode5/003.webp") with dissolve
        hide screen ui_message
        hide screen ui_newEpisode
        $ ep4_nightWithCharlotte = True
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm never going to sleep on that couch again. My neck is stiff as hell!{/i}"
        scene expression ("images/episode5/004.webp") with dissolve
        toby "Pagi!"

    scene expression ("images/episode5/005.webp") with dissolve
    charlotte "Sayang pagi! Bagaimana Anda tidur?"
    if ep4_nightWithCharlotte == False:
        toby "Sangat baik, sebenarnya!"
        scene expression ("images/episode5/006.webp") with dissolve
        patricia "Nah, saya senang Anda melakukannya. Aku nyaris tidak tidur mengedipkan mata karena dengkuranmu."
        toby "Saya tidak mendengkur!"
    else:
        toby "Tidak bagus, itu terakhir kali saya tidur di sofa jelek itu!"
        scene expression ("images/episode5/007.webp") with dissolve
        patricia "Mengapa tidak? Sangat menyenangkan memiliki tempat tidur untuk diri saya sendiri untuk ganti!"
        toby "Anda terlalu manja!"
        patricia "Sejak kapan ada tempat tidur untuk diri Anda sendiri dianggap sebagai kemewahan?"
    scene expression ("images/episode5/008.webp") with dissolve
    toby "Jadi, apa yang kamu lihat?"
    scene expression ("images/episode5/009.webp") with dissolve
    charlotte "Saya menunjukkan kepadanya beberapa ide yang saya miliki untuk halaman. Kami bermimpi besar."
    scene expression ("images/episode5/010.webp") with dissolve
    toby "Seperti yang Anda sebutkan kemarin dengan bak mandi air panas dan semuanya?"
    scene expression ("images/episode5/011.webp") with dissolve
    patricia "Yup, tapi kami baru saja selesai. Dan selanjutnya kami pindah ke loteng, karena sudah saatnya Anda pindah dari kamar saya."
    scene expression ("images/episode5/012.webp") with dissolve
    toby "Anda benar -benar ingin saya keluar dari ruangan seburuk itu? Saya terluka, [sis]."
    scene expression ("images/episode5/011.webp") with dissolve
    patricia "Jangan mengambilnya secara pribadi, tetapi Anda kentut dalam tidur Anda."
    scene expression ("images/episode5/012.webp") with dissolve
    toby "Dan Anda mendengkur!"
    scene expression ("images/episode5/013.webp") with dissolve
    patricia "Tidak!"
    scene expression ("images/episode5/012.webp") with dissolve
    toby "Anda tidak tahu, kadang -kadang saya menggunakan headphone saya supaya saya bisa mencoba tidur."
    scene expression ("images/episode5/013.webp") with dissolve
    patricia "Anda berbohong. Saya tidak mendengkur."
    scene expression ("images/episode5/012.webp") with dissolve
    toby "Apakah saya? Mungkin Anda memiliki septum yang menyimpang."
    scene expression ("images/episode5/011.webp") with dissolve
    patricia "Atau mungkin saya tersedak kentut Anda dan itulah mengapa saya mendengkur."
    scene expression ("images/episode5/014.webp") with dissolve
    charlotte "Anda tidak mendengkur, dia hanya mengacaukan Anda dan saya cukup yakin [toby!c] tidak kentut dalam tidurnya."
    scene expression ("images/episode5/015.webp") with dissolve
    patricia "Bagaimana Anda bisa begitu yakin?"
    scene expression ("images/episode5/010.webp") with dissolve
    toby "Ya [mom], bagaimana Anda tahu Tris tidak mendengkur?"
    scene expression ("images/episode5/016.webp") with dissolve
    charlotte "Saya akan menelepon beberapa kontraktor dan melihat berapa biaya untuk memperbaiki loteng dan halaman."
    charlotte "Saya tidak ingin mendengar kalian berdua."
    scene expression ("images/episode5/017.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Yeah [sis]. Make sure you breathe with your mouth open.{/i}"
    scene expression ("images/episode5/018.webp") with dissolve
    patricia "Dan Anda lebih baik meletakkan jari ke atas pantat Anda sehingga Anda tidak kentut."
    scene expression ("images/episode5/017.webp") with dissolve
    toby "Saya memiliki ide yang lebih baik, saya akan menjatuhkan celana saya dan Anda dapat memilih jari apa pun yang ingin Anda tempel di pantat saya."
    scene expression ("images/episode5/019.webp") with dissolve
    charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Hey, you're both young adults, act like it...{/i}"
    scene expression ("images/episode5/020.webp") with dissolve
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Yeah, Hi! I'd like to get a quote for some renovations we are considering.{/i}"
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Both.{/i}"
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}First, I would like to renovate the attic. It's currently unfinished, only a subfloor, so we'd like a hardwood laminate installed. The ceilings and walls are bare studs, so sheetrock and then paint.{/i}"
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}I understand. I just need a ballpark price.{/i}"
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}Around 16 feet by 13 feet.{/i}"
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    scene expression ("images/episode5/021.webp") with dissolve
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}10k? Just for the labor?{/i}"
    scene expression ("images/episode5/017.webp") with dissolve
    toby "Itu terlalu tinggi. Saya lebih suka memperbaikinya sendiri daripada menghabiskan sebanyak itu untuk persalinan."
    scene expression ("images/episode5/022.webp") with dissolve
    patricia "Seperti Anda akan tahu cara melakukannya."
    scene expression ("images/episode5/023.webp") with dissolve
    toby "Seberapa sulit itu?"
    scene expression ("images/episode5/022.webp") with dissolve
    patricia "Mungkin tidak terlalu sulit, tetapi Anda tidak tahu apa -apa tentang konstruksi."
    scene expression ("images/episode5/023.webp") with dissolve
    toby "Anda tidak tahu dengan siapa Anda berbicara."
    scene expression ("images/episode5/022.webp") with dissolve
    patricia "Saya sangat menyesal, Tuan Handyman!"
    scene expression ("images/episode5/024.webp") with dissolve
    toby "Mari kita bertaruh."
    toby "Jika saya berhasil merenovasi loteng sendiri, Anda harus membersihkan kamar baru saya selama sebulan penuh."
    scene expression ("images/episode5/025.webp") with dissolve
    patricia "Anda akan melakukan loteng dan halaman dan jika Anda tidak bisa menyelesaikan keduanya, Anda harus membelikan saya mobil."
    toby "Saya tidak melihat bagaimana itu taruhan yang adil."
    patricia "Nah, Anda orang yang mengatakan itu tidak bisa terlalu sulit."
    toby "Tapi Anda memberi terlalu sedikit jika saya menang."
    patricia "Bagus. Dua bulan."
    scene expression ("images/episode5/026.webp") with dissolve
    toby "Dan Anda akan memakai pakaian yang saya pilih untuk Anda saat Anda membersihkan!"
    patricia "Bagus. Tapi tidak ada yang buruk."
    toby "Biarkan saya khawatir tentang pakaiannya, Anda khawatir tentang mobil. Tapi mobil tidak bisa lebih mahal daripada renovasi."
    patricia "Satu bulan dengan pakaian yang Anda pilih dan Anda telah mendapatkan kesepakatan!"
    scene expression ("images/episode5/020.webp") with dissolve
    charlotte "Saya mengerti. Jadi itu akan menjadi 40k untuk semuanya?"
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte "Jadi begitu. Terima kasih atas informasinya dan waktu Anda."
    scene expression ("images/episode5/027.webp") with dissolve
    charlotte "Saya menyesal anak -anak, tetapi mengingat situasi kami saat ini, bahkan jika kami menemukan tenaga kerja yang lebih murah saya tidak melihatnya membuat perbedaan besar. Anda hanya perlu berbagi kamar tidur selama beberapa bulan lagi."
    scene expression ("images/episode5/028.webp") with dissolve
    toby "Jangan khawatir [mom], itu tidak sulit. Saya akan melakukan loteng dan halaman sendiri. Anda hanya menunjukkan apa yang ada dalam pikiran Anda untuk halaman."
    scene expression ("images/episode5/027.webp") with dissolve
    charlotte "Tidak, lupakan tentang itu, [son]. Anda tidak harus melakukan itu."
    scene expression ("images/episode5/029.webp") with dissolve
    patricia "Oh, jangan khawatir [mom], dia tidak akan melakukannya, tapi aku ingin melihatnya mencoba!"
    scene expression ("images/episode5/030.webp") with dissolve
    toby "Dan, jangan khawatir [sis], mulailah mencari di internet untuk membersihkan video tutorial."
    patricia "Sebenarnya, saya pikir saya akan mencari mobil."
    toby "Bersenang -senang dengan itu."
    return

label episode5_sunday_emma:
    $ progress = 67

    scene expression ("images/episode5/031.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmmm... 5 missed call and 14 new messages.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}All from Emma.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I must have slept like a rock.{/i}"
    scene expression ("images/episode5/031_texting.webp") with dissolve
    call sms_incoming ("emma", "Hi there, my love. \nHow are you?") from _call_sms_incoming_11
    call sms_incoming ("emma", "I miss you!") from _call_sms_incoming_12
    call sms_incoming ("emma", "I don't want to sound too clingy, but I really miss you and I would like to hear your voice.") from _call_sms_incoming_13
    call sms_incoming ("emma", "I'm sorry for sending so many messages, but I really need to know that you're okay.") from _call_sms_incoming_14
    call sms_incoming ("emma", "Maybe you're asleep.") from _call_sms_incoming_15
    call sms_incoming ("emma", "Good night, my everything!") from _call_sms_incoming_16
    call sms_incoming ("emma", "I hope you're asleep and you're not avoiding me.") from _call_sms_incoming_17
    call sms_incoming ("emma", "Did I do something wrong?") from _call_sms_incoming_18
    call sms_incoming ("emma", "Please tell me if I've done something wrong. I don't want to lose you.") from _call_sms_incoming_19
    call sms_incoming ("emma", "Please, love. Answer me.") from _call_sms_incoming_20
    call sms_incoming ("emma", "I guess you're asleep. Love you!") from _call_sms_incoming_21
    call sms_incoming ("emma", "Let me know when you're awake.") from _call_sms_incoming_22
    call sms_incoming ("emma", "Love you", img_icon="images/episode5/032_icon.webp", img="images/episode5/032.webp") from _call_sms_incoming_23
    call sms_incoming ("emma", "Morning my love. Sorry for last night. I watched a movie where the main character cheated on his girlfriend and I got a little anxious.") from _call_sms_incoming_24
    hide screen message
    scene expression ("images/episode5/031.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Oh my God. Poor girl. I really need to pay more attention to her...or maybe it's better we take a break until we can be together as a normal couple and not this long distance bullshit.{/i}"
    scene expression ("images/episode5/031_texting.webp") with dissolve
    call sms_sent ("emma", "Morning Emma. Sorry, I was really tired last night and I feel asleep pretty early.") from _call_sms_sent_9
    hide screen message
    scene expression ("images/episode5/033.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And now she's video calling me while I'm taking a shit.{/i}"
    scene expression ("images/episode5/031_texting.webp") with dissolve
    call sms_incoming ("emma", "Please answer the phone. I really need to see you and hear your voice.") from _call_sms_incoming_25
    call sms_sent ("emma", "I'll call you back in a second, I just need to finish some business.") from _call_sms_sent_10
    call sms_incoming ("emma", "XOXO. Are you taking a poo?") from _call_sms_incoming_26
    call sms_sent ("emma", "I said I'm taking care of some business.") from _call_sms_sent_11
    call sms_incoming ("emma", "LOL. Happy pooping.") from _call_sms_incoming_27
    call sms_sent ("emma", "You're hopeless!") from _call_sms_sent_12
    call sms_incoming ("emma", "Love you!") from _call_sms_incoming_28
    call sms_incoming ("emma", "Don't forget to wash your hands!") from _call_sms_incoming_29
    call sms_sent ("emma", "You're terrible!") from _call_sms_sent_13
    hide screen message
    scene expression ("images/episode5/034.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'd better call her now, before she freaks out!{/i}"
    scene expression ("images/episode5/035_laugh.webp") with dissolve
    emma "Juara pagi! Bagaimana kotoranmu?"
    scene expression ("images/episode5/036_laugh.webp") with dissolve
    toby "Bisakah seorang pria mengambil dump dengan damai?"
    scene expression ("images/episode5/035_smile.webp") with dissolve
    emma "Dia bisa, tetapi tidak ketika pacarnya tidak bisa tidur sepanjang malam karena dia menonton film yang salah."
    scene expression ("images/episode5/036_laugh.webp") with dissolve
    toby "Saya sudah berpikir saya harus mengubah kata sandi Netflicks."
    scene expression ("images/episode5/035_surprised.webp") with dissolve
    emma "Anda tidak memiliki jiwa! Tidak pernah Anda meninggalkan saya di sini sendirian. Sekarang Anda akan mengambil netflick saya juga?"
    emma "Bagaimana saya akan menghabiskan waktu saya?"
    scene expression ("images/episode5/036_laugh.webp") with dissolve
    toby "Umm ... mengerjakan pekerjaan rumah?"
    scene expression ("images/episode5/035_laugh.webp") with dissolve
    emma "Ya ... tidak!"
    scene expression ("images/episode5/036_smile.webp") with dissolve
    toby "Apakah Anda baik -baik saja, karena tadi malam Anda jelas tidak!"
    scene expression ("images/episode5/035_smile.webp") with dissolve
    emma "Katakan saja padaku bahwa kamu mencintaiku dan aku akan baik -baik saja."
    scene expression ("images/episode5/036_thinking.webp") with dissolve
    menu:
        "[JGR] Aku semakin mencintaimu setiap hari!"(csq="Emma +1 & Galeri Gambar"):

            $ emma_rel += 1
            $ unlockImage(persistent.emma_05)
            scene expression ("images/episode5/035_smile.webp") with dissolve
            emma "Bahkan jika saya tidak ada di sana untuk mengisap ayam Anda setiap hari?"
            scene expression ("images/episode5/036_smile.webp") with dissolve
            toby "Saya pikir kita melewati titik itu dalam hubungan kita. Bukan hanya nafsu yang menghubungkan kita."
            scene expression ("images/episode5/035_happyCry.webp") with dissolve
            emma "Aku akan menangis! Uhum ... maaf!"
            scene expression ("images/episode5/034.webp") with dissolve
            toby "Hei ... nyalakan kamera Anda kembali!"
            emma "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}{/i}I'm ugly when I cry!"
            toby "Anda adalah wanita cantik dan cantik saya. Anda tidak jelek saat Anda menangis! Anda sedikit bodoh karena berpikir bahwa saya tidak akan berpikir Anda cantik saat Anda menangis."
            scene expression ("images/episode5/035_happyCry.webp") with dissolve
            emma "Anda bodoh!"
            scene expression ("images/episode5/036_laugh.webp") with dissolve
            toby "Aku? Apa yang saya lakukan?"
            scene expression ("images/episode5/035_smile.webp") with dissolve
            emma "Anda tidak menjawab telepon Anda!"
            scene expression ("images/episode5/036_smile.webp") with dissolve
            toby "Sudah kubilang. Saya lagi tidur!"
            scene expression ("images/episode5/035_laugh.webp") with dissolve
            emma "Itu terlalu buruk untukmu. Karena saya datang berkunjung pada hari Selasa!"
            scene expression ("images/episode5/036_surprised.webp") with dissolve
            toby "Apakah kamu serius?"
            scene expression ("images/episode5/035_ashamed.webp") with dissolve
            emma "Mungkin!"
            scene expression ("images/episode5/036_laugh.webp") with dissolve
            toby "Saya minta maaf saya tertawa, karena saya tidak bisa menunggu, tapi itu sangat lucu!"
            scene expression ("images/episode5/035_ashamed.webp") with dissolve
            emma "Ha ha. Lucu sekali. Aku merindukanmu, jadi aku akan memperbaikinya!"
            scene expression ("images/episode5/036_smile.webp") with dissolve
            toby "Aku sangat mencintaimu!"
            scene expression ("images/episode5/035_smile.webp") with dissolve
            emma "Aku juga mencintaimu, tetapi jika kamu tidak ingin aku keluar dari sekolah menengah dan mendapatkan tempat di dekatmu, kamu lebih baik mengangkat telepon saat aku menelepon!"
            scene expression ("images/episode5/036_happy.webp") with dissolve
            toby "Mengapa mendapatkan tempat Anda sendiri saat Anda bisa tinggal dengan saya. Kami akan segera merenovasi loteng."
            toby "Jadi? Apakah Anda memiliki preferensi tentang dekorasi?"
            scene expression ("images/episode5/035_laugh.webp") with dissolve
            emma "Saya ingin menjadi merah muda dengan dinding kedap suara dan tempat tidur besar, tetapi pastikan tempat tidur memiliki hal -hal di mana Anda dapat memasang borgol!"
            scene expression ("images/episode5/036_laugh.webp") with dissolve
            toby "Benar-benar? Dinding merah muda?"
            scene expression ("images/episode5/035_smile.webp") with dissolve
            emma "Mereka perlu mencocokkan borgol."
            scene expression ("images/episode5/036_smile.webp") with dissolve
            toby "Tolong beritahu saya bahwa Anda tidak membeli borgol merah muda."
            scene expression ("images/episode5/035_ashamed.webp") with dissolve
            emma "Umm ... Aku tidak bisa tidur tadi malam dan kamu pantas dipukuli karena tidak menjawab panggilanku."
            scene expression ("images/episode5/035_happyMad.webp") with dissolve
            emma "Dan untuk berpikir saya seorang penggali emas."
            scene expression ("images/episode5/036_smile.webp") with dissolve
            toby "Saya tidak pernah mengatakan Anda adalah penggali emas."
            scene expression ("images/episode5/035_laugh.webp") with dissolve
            emma "Nah, sekarang Anda tahu bahwa saya bukan penggali emas. Saya membeli borgol merah muda dengan uang saya sendiri!"
            scene expression ("images/episode5/036_surprised.webp") with dissolve
            toby "Tolong beritahu saya bahwa Anda bercanda."
            scene expression ("images/episode5/035_laugh.webp") with dissolve
            emma "Baik, baiklah! Saya. Mereka bukan merah muda!"
            scene expression ("images/episode5/036_laugh.webp") with dissolve
            toby "Anda tidak ada harapan!"
            scene expression ("images/episode5/035_kiss.webp") with dissolve
            emma "Aku benar -benar perlu tidur siang. Saya hampir tidak tidur sama sekali tadi malam!"
            scene expression ("images/episode5/036_smile.webp") with dissolve
            toby "Selamat malam, atau selamat pagi. Saya tidak yakin yang mana sekarang."
            scene expression ("images/episode5/035_smile.webp") with dissolve
            emma "\"Love you\"harus melakukan trik!"
            scene expression ("images/episode5/036_smile.webp") with dissolve
            toby "Aku mencintaimu, Emma!"
            scene expression ("images/episode5/035_smile.webp") with dissolve
            emma "Aku pun mencintaimu!"
            scene expression ("images/episode5/035_ashamed.webp") with dissolve
            emma "Dan maaf karena sangat melekat."
            scene expression ("images/episode5/036_laugh.webp") with dissolve
            toby "Pergi tidur saja. Ini baik -baik saja!"
            scene expression ("images/episode5/035_kiss.webp") with dissolve
            emma "Bye Lover!"
            scene expression ("images/episode5/036_smile.webp") with dissolve
            toby "Selamat tinggal!"
            scene expression ("images/episode5/037.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Can't wait to see her!{/i}"
        "{i} hindari jawaban {/i} [JWRN5]"(csq="Istirahat hubungan"):


            $ renpy.notify("Relationship break with Emma!")
            $ emma_break = True
            scene expression ("images/episode5/036_normal.webp") with dissolve
            toby "Lihat. Anda tahu bagaimana perasaan saya tentang Anda, hanya saja jarak ini tidak membantu kami sama sekali."
            scene expression ("images/episode5/035_sad.webp") with dissolve
            emma "Katakan saja padaku bahwa kamu mencintaiku!"
            scene expression ("images/episode5/036_normal.webp") with dissolve
            toby "Saya lakukan, tetapi sangat sulit untuk melanjutkan hubungan ini tanpa saling bertemu."
            scene expression ("images/episode5/035_sad.webp") with dissolve
            emma "Apa yang sangat sulit? Aku mencintaimu dan kamu mencintaiku. Anda benar -benar membutuhkan saya untuk mengisap kemaluan Anda untuk membuat Anda lebih mencintaiku?"
            scene expression ("images/episode5/036_sad.webp") with dissolve
            toby "Jangan seperti itu. Anda tahu itu bukan yang saya katakan."
            scene expression ("images/episode5/035_mad.webp") with dissolve
            emma "Apakah saya?"
            scene expression ("images/episode5/035_sad.webp") with dissolve
            emma "Saya hanya tahu bahwa karena alasan tertentu Anda merasa sulit untuk melanjutkan hubungan kami!"
            scene expression ("images/episode5/036_sad.webp") with dissolve
            toby "Lihat. Anda adalah pacar saya dan tentu saja saya mencintaimu, tetapi kami harus jujur satu sama lain."
            toby "Ini tidak seperti sebelumnya."
            scene expression ("images/episode5/035_sad.webp") with dissolve
            emma "Tolong beritahu saya bahwa Anda tidak ingin putus!"
            scene expression ("images/episode5/036_normal.webp") with dissolve
            toby "Saya tidak mengatakan itu."
            scene expression ("images/episode5/035_mad.webp") with dissolve
            emma "Lalu apa yang kamu katakan? Anda mencintaiku, tetapi Anda tidak bisa mengatakannya."
            emma "Aku tidak harus menidurimu agar kamu tetap mencintaiku, namun jarak dan kekurangannya membuatmu mengatakan itu sulit bagimu untuk tetap mencintaiku."
            emma "Jadi apa yang akan terjadi, [toby!c]? Saya tidak mengerti!"
            scene expression ("images/episode5/036_normal.webp") with dissolve
            toby "Anda tahu saya tidak baik dengan kata -kata. Tolong, mengerti. Saya hanya mengatakan bahwa sulit dengan jarak."
            scene expression ("images/episode5/035_mad.webp") with dissolve
            emma "Apa yang sangat sulit? Kami masih sama. Cukup hubungi saya lebih sering dan jawab telepon ketika saya menelepon Anda, kirimi saya pesan dari waktu ke waktu sehingga saya tahu Anda masih hidup."
            scene expression ("images/episode5/035_sad.webp") with dissolve
            emma "Melihat? Ini tidak terlalu sulit!"
            scene expression ("images/episode5/036_normal.webp") with dissolve
            toby "Lihat ... Aku tidak memanggilmu untuk berdebat."
            scene expression ("images/episode5/035_mad.webp") with dissolve
            emma "Dan apakah Anda pikir saya tidak tidur sepanjang malam karena saya mencoba menemukan alasan untuk berdebat?"
            scene expression ("images/episode5/035_sad.webp") with dissolve
            emma "Anda tidak menelepon saya. Anda menghindari mengatakan kepada saya bahwa Anda mencintaiku. Anda pikir saya adalah penggali emas!"
            emma "Apa aku untukmu? Apakah saya pacar Anda atau hanya pelacur yang Anda tidak harus membayar setelah berhubungan seks?"
            scene expression ("images/episode5/036_angry.webp") with dissolve
            toby "Sekarang Anda membesar -besarkan!"
            scene expression ("images/episode5/035_mad.webp") with dissolve
            emma "Apakah saya?"
            scene expression ("images/episode5/036_normal.webp") with dissolve
            toby "Ya!"
            scene expression ("images/episode5/035_normal.webp") with dissolve
            emma "Bagus. Dalam hal ini, beri tahu saya bagaimana kami dapat memperbaiki hubungan jika Anda mengatakan Anda mencintaiku dan semua itu."
            scene expression ("images/episode5/036_normal.webp") with dissolve
            toby "Seperti yang saya katakan, masalah dalam hubungan kami bukanlah Anda atau saya, jaraknya."
            scene expression ("images/episode5/035_sad.webp") with dissolve
            emma "Jarak seharusnya tidak menjadi masalah [toby!c]. Anda terlalu pintar untuk percaya itu."
            scene expression ("images/episode5/036_sad.webp") with dissolve
            toby "Tapi saya benar -benar percaya itu?"
            scene expression ("images/episode5/035_sad.webp") with dissolve
            emma "Lihat. Dalam dua bulan saya lulus dari sekolah menengah dan kemudian saya akan berada di sana bersama Anda!"
            emma "Silakan. Mari kita coba dan kerjakan sampai saat itu!"
            scene expression ("images/episode5/036_normal.webp") with dissolve
            toby "Mungkin kita harus istirahat sampai saat itu, itu akan memengaruhi kita berdua. Anda membuat final Anda berkonsentrasi."
            toby "Saya memiliki pekerjaan saya."
            scene expression ("images/episode5/035_normal.webp") with dissolve
            emma "Benar-benar? Itulah yang Anda inginkan? Anda ingin istirahat?"
            scene expression ("images/episode5/036_normal.webp") with dissolve
            toby "Saya tidak menginginkannya, tapi mungkin itu hal terbaik untuk kita berdua!"
            scene expression ("images/episode5/035_cry.webp") with dissolve
            emma "Tolong, [toby!c]. Jangan lakukan ini. Saya tahu itu sulit, tetapi kita harus menjadi kuat hanya selama dua bulan lagi!"
            scene expression ("images/episode5/036_normal.webp") with dissolve
            toby "Lihat, jika kita memang seharusnya, maka kita akan kembali bersama, tapi ini ... ini tidak berfungsi!"
            scene expression ("images/episode5/035_cry.webp") with dissolve
            emma "Aku mencintaimu [toby!c]. Tolong, jangan lakukan ini."
            scene expression ("images/episode5/036_sad.webp") with dissolve
            toby "Tolong, jangan menangis. Kami akan baik -baik saja, mungkin istirahat ini akan membantu kami."
            scene expression ("images/episode5/035_cry.webp") with dissolve
            emma "Atau hancurkan kami!"
            scene expression ("images/episode5/036_normal.webp") with dissolve
            toby "Jangan pergi ke sana!"
            scene expression ("images/episode5/035_sad.webp") with dissolve
            emma "Apa pun. Sedih sekali bahwa Anda tidak dapat mencintaiku jika Anda tidak bisa pergi seminggu tanpa meniduri saya!"
            emma "Maaf, maksud saya jika ada jarak di antara kami!"
            scene expression ("images/episode5/036_sad.webp") with dissolve
            toby "..."
            scene expression ("images/episode5/035_sad.webp") with dissolve
            emma "Saya hanya akan mengatakan ini. Aku mencintaimu dan tidak ada yang akan mengubahnya. Jika Anda ingin istirahat, baiklah. Kami akan istirahat."
            emma "Saya tidak tahu apa arti istirahat bagi Anda dan saya tidak ingin tahu. Lakukan apa pun yang ingin Anda lakukan, tapi tolong ketika saya sampai di sana mari kita coba dan membuatnya bekerja."
            emma "Saya hanya berharap itu belum terlambat!"
            scene expression ("images/episode5/036_normal.webp") with dissolve
            toby "..."
            scene expression ("images/episode5/035_sad.webp") with dissolve
            emma "Bye [toby!c]!"
            scene expression ("images/episode5/036_sad.webp") with dissolve
            toby "Bye Emma."
            scene expression ("images/episode5/038.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I hate to see a girl cry, but this is probably best for both of us.{/i}"

    scene expression ("images/episode5/039.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}All right, I should go to the gym, cuz I'm gonna need to build more muscle if I'm going to do those renovations!{/i}"

    return

label episode5_gym:
    $ progress = 68
    scene expression ("images/episode5/040.webp") with fade
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/041.webp") with dissolve
    clerk "Pagi [toby!c]."
    toby "Hai, yang di sana. Bisakah saya mendapatkan kunci?"
    clerk "Tentu!"
    scene expression ("images/episode5/042.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmm... I wonder what I should do first. I think I'll need to do some bench press, pull-ups & squats.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Bench press wins today.{/i}"
    scene expression ("images/episode5/043.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I guess I'll head over to the bench.{/i}"
    if toby_job == 0:

        katrina "Baik halo. Jika itu bukan karyawan favorit pacar saya."
        scene expression ("images/episode5/044.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        toby "Uhum ... Mrs. Katrina? Halo."
        scene expression ("images/episode5/045.webp") with dissolve
        katrina "Apa yang kamu lakukan di sini seksi?"
        scene expression ("images/episode5/046.webp") with dissolve
        toby "Uhum ... saya pelatihan. Bagaimana denganmu?"
        scene expression ("images/episode5/045.webp") with dissolve
        katrina "Menjadi seksi. Saya belum pernah melihat Anda di sini sebelumnya."
        scene expression ("images/episode5/046.webp") with dissolve
        toby "Nah, ini adalah gym terdekat di rumah saya."
        scene expression ("images/episode5/047.webp") with dissolve
        katrina "Jadi Anda tidak datang ke sini hanya untuk melihat gadis -gadis telanjang di ruang ganti?"
        scene expression ("images/episode5/046.webp") with dissolve
        toby "Sejujurnya saya tidak tahu tentang bagian itu sebelum saya mendaftar. Saya tahu sesudahnya."
        scene expression ("images/episode5/045.webp") with dissolve
        katrina "Apa yang akan Anda lakukan jika Anda tahu?"
        scene expression ("images/episode5/048.webp") with dissolve
        toby "Mungkin bukan satu hal pun, tidak seperti itu mengganggu saya."
        scene expression ("images/episode5/049.webp") with dissolve
        katrina "Apakah Anda seorang cabul, [toby!c]?"
        toby "Tidak, tidak juga. Maksud saya, baiklah dengan saya. Saya tidak perlu malu dan saya tidak akan melihat."
        katrina "Sayang sekali Anda bukan tipe orang yang terlihat karena saya akan memberi tahu Anda ketika saya pergi ke ruang ganti."
        toby "Ya ... dalam hidup beberapa kali Anda kalah dan terkadang Anda tidak menang!"
        scene expression ("images/episode5/050.webp") with dissolve
        katrina "Aku menyukaimu [toby!c]. Jadi, bagaimana pacar saya memperlakukan Anda? Apakah dia membayar Anda dengan baik?"
        toby "Sejujurnya, dia lebih dari adil!"
        katrina "Saya senang mendengarnya. Dia tampak sangat senang denganmu!"
        scene expression ("images/episode5/051.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        if sheila_path == True:
            scene expression ("images/episode5/052.webp") with dissolve
            sheila "Hei, pria besar! Kamu sudah merindukanku?"
            toby "Oh, hai Sheila! Mungkin."
            sheila "Saya akan memastikan lain kali Anda tidak akan melupakan saya."
        else:
            scene expression ("images/episode5/052.webp") with dissolve
            sheila "Hai [toby!c]. Senang melihat Anda kembali ke sini!"
            toby "Oh, ya. Kami akan memulai beberapa renovasi di rumah dan saya akan membutuhkan semua otot yang bisa saya dapatkan."
            sheila "Haha ... semoga sukses dengan itu!"

        scene expression ("images/episode5/053.webp") with dissolve
        sheila "Maaf. Saya Sheila. Saya bekerja di sini sebagai pelatih kebugaran."
        scene expression ("images/episode5/054.webp") with dissolve
        katrina "Dan Anda pasti bugar!"
        if sheila_path == True:
            scene expression ("images/episode5/055.webp") with dissolve
        else:
            scene expression ("images/episode5/055_1.webp") with dissolve
        sheila "Bagaimanapun. Aku akan membiarkan kalian berbicara!"
        scene expression ("images/episode5/056.webp") with dissolve
        if sheila_path == True:
            katrina "Itu benar ada pantat yang sempurna!"
            scene expression ("images/episode5/057.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode5/058.webp") with dissolve
            katrina "Sebenarnya, saya tidak yakin mengapa saya repot -repot menunjukkannya kepada Anda, sepertinya Anda sudah tahu semua tentang itu!"
            toby "Mari kita katakan bahwa seorang pria tidak pernah membual."
            scene expression ("images/episode5/059.webp") with dissolve
            katrina "Jadi, seperti yang saya katakan, Darlene sangat senang dengan Anda. Dia bahkan berpikir untuk mengundang Anda untuk makan malam kapan -kapan."
            scene expression ("images/episode5/060.webp") with dissolve
            toby "Saya akan menyukainya."
            scene expression ("images/episode5/059.webp") with dissolve
            katrina "Anda mengatakan sesuatu?"
            scene expression ("images/episode5/061.webp") with dissolve:
                yalign 1.0
                xalign 0.0
                linear 10.0 yalign 0.0 xalign 0.8

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            toby "Jangan khawatir. Tidak apa -apa!"
            scene expression ("images/episode5/062.webp") with dissolve
            katrina "Aku sangat cemburu padamu sekarang!"
            katrina "Jangan beri tahu Darlene tentang ini!"
            toby "Saya menang!"
            scene expression ("images/episode5/063.webp") with dissolve
            katrina "Bagaimanapun. Saya harus pergi ... pastikan Anda tidak memiliki di dalam. Saya tidak ingin Anda merusaknya!"
            toby "..."
            scene expression ("images/episode5/064.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}That woman is crazy!{/i}"
        else:

            katrina "Itu benar ada pantat yang sempurna!"
            scene expression ("images/episode5/058.webp") with dissolve
            katrina "Ya. Jangan Pikirkan Aku!"
            scene expression ("images/episode5/059.webp") with dissolve
            katrina "Jadi seperti yang saya katakan, Darlene sangat senang dengan Anda. Dia bahkan berpikir untuk mengundang Anda untuk makan malam kapan -kapan."
            scene expression ("images/episode5/060.webp") with dissolve
            toby "Saya akan menyukainya."
            scene expression ("images/episode5/059.webp") with dissolve
            katrina "Anda mengatakan sesuatu?"
            scene expression ("images/episode5/062.webp") with dissolve
            toby "Jangan khawatir."
            katrina "Sialan neraka. Dia sempurna."
            scene expression ("images/episode5/063.webp") with dissolve
            katrina "Bagaimanapun. Saya harus pergi ..."
            katrina "Ngomong -ngomong, jangan beri tahu Darlene tentang ini!"
            toby "Saya menang!"
            scene expression ("images/episode5/064.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmm... Mrs. Darlene and Katrina are quite an interesting couple!{/i}"
    else:

        darlene "Hai [toby!c]."

        scene expression ("images/episode5/065.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        toby "Hai ma \ 'am. Apa kabarmu?"
        scene expression ("images/episode5/066.webp") with dissolve
        darlene "Sangat baik, terima kasih. Saya baru saja melakukan beberapa latihan."
        darlene "Jadi saya kira Kat membujuk Anda untuk bergabung dengan gym ini juga?"
        scene expression ("images/episode5/067.webp") with dissolve
        toby "Sama sekali tidak. Saya tidak tahu dia adalah anggota di sini."
        scene expression ("images/episode5/066.webp") with dissolve
        darlene "Maka Anda tunggu sampai dia mengetahui bahwa Anda datang ke sini. Aku mulai sedikit cemburu padamu."
        scene expression ("images/episode5/068.webp") with dissolve
        toby "Kenapa begitu?"
        scene expression ("images/episode5/069.webp") with dissolve
        darlene "Karena setiap kali dia pulang, dia hanya berbicara tentang Anda, betapa baiknya Anda, betapa pintar dan sebagainya."
        scene expression ("images/episode5/066.webp") with dissolve
        toby "Aku akan memerah. Saya tidak terbiasa dengan banyak pujian."
        scene expression ("images/episode5/069.webp") with dissolve
        darlene "Kemudian berpura -pura Anda tidak tahu tentang mereka. Saya tidak berpikir dia menghargai saya mengatakan ini kepada Anda."
        darlene "Saya yakin dia bertingkah tangguh!"
        scene expression ("images/episode5/068.webp") with dissolve
        toby "Ya, terkadang, tapi baik -baik saja."
        scene expression ("images/episode5/069.webp") with dissolve
        darlene "Jadi? Apakah Anda suka bekerja untuknya?"
        scene expression ("images/episode5/067.webp") with dissolve
        toby "Ini pekerjaan yang menarik, saya harus jujur."
        scene expression ("images/episode5/051.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        if sheila_path == True:
            scene expression ("images/episode5/070.webp") with dissolve
            sheila "Hai seksi! Merindukanku?"
            toby "Mari kita katakan aku datang untuk Babak 2."
            sheila "Anda benar -benar jahat."
        else:
            scene expression ("images/episode5/070.webp") with dissolve
            sheila "Hai [toby!c]."
            toby "Halo Sheila."
        scene expression ("images/episode5/071.webp") with dissolve
        sheila "Ngomong -ngomong, aku Sheila. Saya bekerja di sini sebagai instruktur kebugaran!"
        scene expression ("images/episode5/072.webp") with dissolve
        darlene "Hai Sheila. Saya Darlene."
        sheila "Anda tampak sangat akrab, apakah Anda pada kebetulan pemilik Carpe Diem Realty?"
        scene expression ("images/episode5/073.webp") with dissolve
        darlene "Saya sebenarnya, bagaimana Anda mengenal saya?"
        sheila "Yah, kami berbicara pada hari Jumat melalui telepon tentang sewa, tetapi saya harus membatalkan pertemuan."
        darlene "Oh, kamu itu Sheila itu. Senang akhirnya menaruh wajah pada namanya."
        sheila "Ya. Maaf tentang itu, tapi bisakah kita bertemu mungkin nanti hari ini?"
        darlene "Yah, saya mencoba untuk tidak bekerja pada hari Minggu tetapi saya akan membuat pengecualian untuk Anda sayang!"
        sheila "Terima kasih, terima kasih banyak!"
        scene expression ("images/episode5/074.webp") with dissolve
        sheila "Bagaimanapun. Senang berbicara denganmu. Saya memiliki kelas dimulai. Sampai jumpa."
        toby "Sampai jumpa!"
        darlene "Nanti!"

        scene expression ("images/episode5/075_1.webp") with dissolve
        darlene "Dia tampak sangat baik."
        darlene "Bagaimanapun, saya harus pergi. Senang berbicara denganmu."
        scene expression ("images/episode5/075_2.webp") with dissolve
        toby "Ya, sama di sini."
        scene expression ("images/episode5/076.webp") with dissolve
        darlene "Berhati -hatilah [toby!c] dan cobalah untuk tidak terlalu terintimidasi oleh Kat. Dia tidak terlalu sulit."
        toby "Saya akan mencoba mengingatnya!"
        darlene "Oh dan aku akan memintanya untuk mengundangmu untuk makan malam kapan -kapan."
        toby "Itu akan bagus!"
        scene expression ("images/episode5/064.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She seems so nice. I wonder how she ended up with a woman like Katrina.{/i}"

    $ progress = 69
    scene expression ("images/episode5/077.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}OK, I should start doing some exercises.{/i}"
    scene expression ("images/episode5/078.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/079.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}One!{/i}"
    scene expression ("images/episode5/078.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/079.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Two!{/i}"
    scene expression ("images/episode5/078.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/079.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Three!{/i}"
    if sheila_path == True:
        scene expression ("images/episode5/080.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's doing that on purpose.{/i}"
        menu:
            "{i} [JGR] Lihat lebih dekat {/i}"(csq="Sheila +1 & Galeri Gambar"):

                $ sheila_rel += 1
                $ unlockImage(persistent.sheila_06)
                scene expression ("images/episode5/081.webp") with dissolve:
                    xalign 1.0
                    yalign 1.0
                    linear 10.0 xalign 0.2 yalign 0.3

                $ ui.pausebehavior(9.3)
                $ ui.saybehavior()
                $ ui.interact()

                scene expression ("images/episode5/078.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode5/079.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Four!{/i}"

                scene expression ("images/episode5/078.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode5/079.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Five!{/i}"

                scene expression ("images/episode5/082.webp") with dissolve:
                    yalign 1.0
                    linear 10.0 yalign 0.0

                $ ui.pausebehavior(9.3)
                $ ui.saybehavior()
                $ ui.interact()

                scene expression ("images/episode5/083.webp") with dissolve
                sheila "Menikmati pemandangan?"

                scene expression ("images/episode5/084.webp") with dissolve
                with shake

                toby "{size=12}{color=#FDCA6E}* murmuring *{/color}{/size}\n{i}Shit, shit, shit!{/i}"
                sheila "Ya Tuhan, [toby!c], kamu baik -baik saja?"
                scene expression ("images/episode5/085.webp") with dissolve
                toby "Umm ... terima kasih!"
                scene expression ("images/episode5/086.webp") with dissolve
                sheila "Anda harus berhati -hati untuk tidak menatap gadis -gadis seksi di gym atau Anda mungkin terluka!"
                toby "Ya, saya harus mengingatnya."
                scene expression ("images/episode5/087.webp") with dissolve
                sheila "Umm ... apakah kamu punya sesuatu di saku?"
                scene expression ("images/episode5/088.webp") with dissolve
                toby "Maaf. Saya tidak bisa membantu, Anda sangat seksi!"
                scene expression ("images/episode5/086.webp") with dissolve
                sheila "Pegang kudamu seksi, kami di depan umum!"
                toby "Ini akan lebih mudah jika Anda turun dari saya."
                scene expression ("images/episode5/089.webp") with dissolve
                sheila "Cobalah untuk tidak terluka, kami masih memiliki tanggal yang Anda janjikan kepada saya."
                scene expression ("images/episode5/090.webp") with dissolve
                toby "Apakah saya?"
                scene expression ("images/episode5/089.webp") with dissolve
                sheila "Maksud saya, Anda harus melakukannya!"
                scene expression ("images/episode5/090.webp") with dissolve
                toby "Aku akan meneleponmu!"
            "{i} berkonsentrasi pada pelatihan Anda {/i}":

                pass





    show screen ui_message("Some time later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/091.webp") with dissolve
    hide screen ui_message
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/092.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    $ progress = 70
    if sheila_path == False:


        scene expression ("images/episode5/093.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I didn't even realize we had curtains.{/i}"
        scene expression ("images/episode5/094.webp") with dissolve
        if toby_job == 0:
            sheila "Jadi siapa wanita yang menakutkan itu?"
            toby "Oh, dia adalah pacar bosku."
            scene expression ("images/episode5/095.webp") with dissolve
            sheila "Benar-benar. Nyonya Darlene adalah seorang lesbian?"
            toby "Yup, saya juga sedikit terkejut, tetapi saya lebih terkejut dengan kenyataan bahwa mereka sangat berbeda."
            sheila "Ya..."
            sheila "Dan apa yang dia lakukan?"
            toby "Nah, dia adalah pemilik klub. Saya tidak tahu terlalu banyak tentang itu."
            scene expression ("images/episode5/096.webp") with dissolve
            sheila "Oh, saya mengerti, apakah Anda pikir dia suka pelatih pribadi?"
            toby "Saya tidak yakin, tetapi Anda bisa bertanya padanya."
            sheila "Saya akan melakukannya, tetapi dia terlihat sangat menakutkan."
            toby "Lain kali Anda melihat kami berbicara, bergabunglah dengan kami dan saya akan memperkenalkan Anda."
            sheila "Terima kasih [toby!c]. Anda sangat keren dan menyesal tentang hari Jumat, jika saya terlalu bersikeras."
            toby "Jangan khawatir. Kami baik -baik saja!"
        else:

            sheila "Jadi tahukah Anda wanita baik itu?"
            toby "Oh, Darlene? Ya. Dia adalah pacar bos saya."
            scene expression ("images/episode5/095.webp") with dissolve
            sheila "Dia sangat beruntung memilikinya."
            toby "Ya, dia adalah dia."
            sheila "Oh jadi itu berarti wanita dengan tato dan rambut hitam sebenarnya adalah pemilik klub?"
            toby "Yup. Itu Katrina."
            sheila "Saya pikir saya juga melihatnya di gym."
            scene expression ("images/episode5/096.webp") with dissolve
            toby "Ya. Darlene menyebutkan sesuatu tentang itu."
            sheila "Bagaimana dia? Bos Anda?"
            toby "Yah, dia pasti terlihat menakutkan, tapi saya pikir begitu Anda mengenalnya, dia bisa sangat baik."
            sheila "Apakah Anda pikir dia menyukai pelatih pribadi?"
            toby "Saya tidak tahu, mengapa Anda tidak bertanya padanya?"
            sheila "Karena dia terlihat menakutkan."
            toby "Baik, saya akan mencoba berbicara dengannya tentang hal itu jika kita pernah bertemu di gym."
            sheila "Terima kasih [toby!c]. Anda sangat keren dan minta maaf tentang hari Jumat, jika saya memberi Anda sinyal yang salah."
            toby "Jangan khawatir. Kami baik -baik saja!"

        scene expression ("images/episode5/097.webp") with dissolve
        sheila "Bagaimanapun, saya harus pergi. Sampai jumpa [toby!c]."
        toby "Lihat ya!"
        scene expression ("images/episode5/098.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode5/099.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
    else:

        label memory_16:
            if _in_replay:
                scene expression ("images/episode5/091.webp") with dissolve
                hide screen ui_message
                $ ui.saybehavior()
                $ ui.interact()

                scene expression ("images/episode5/092.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()


            scene expression ("images/episode5/100.webp") with dissolve
            sheila "Apakah Anda mengikuti saya?"
            scene expression ("images/episode5/101.webp") with dissolve
            toby "Jika saya, saya akan datang ke kamar mandi Anda alih -alih pergi ke yang berikutnya."
            scene expression ("images/episode5/102.webp") with dissolve
            sheila "Apa yang bisa saya katakan. Sayang sekali kamu tidak mengikutiku."
            scene expression ("images/episode5/101.webp") with dissolve
            toby "Apakah Anda ingin diikuti?"
            scene expression ("images/episode5/102.webp") with dissolve
            sheila "Mari kita katakan bahwa Anda sedang menuju ke kamar mandi yang salah."
            scene expression ("images/episode5/103.webp") with dissolve
            toby "Dan ini yang tepat?"
            sheila "Yah, tentu saja. Di sinilah Anda terakhir kali. Mulai sekarang, Anda harus mandi di sini."
            toby "Dan apa yang terjadi jika ditempati?"
            sheila "Anda tidak peduli, itu milik Anda."
            scene expression ("images/episode5/104.webp") with dissolve
            sheila "Dan ini milikku!"
            scene expression ("images/episode5/105.webp") with dissolve
            sheila "Aku menyukaimu [toby!c]. Aku hampir tidak menyentuh kemaluanmu dan itu sudah sulit."
            toby "Apakah Anda tidak mengatakan Anda tidak diizinkan berhubungan seks di tempat kerja Anda?"


            show ep5_106
            $ ui.saybehavior()
            $ ui.interact()
            sheila "Siapa bilang kita akan berhubungan seks?"
            toby "Burukku. Saya sedikit bingung. Biasanya setelah ini datang seks."
            scene expression ("images/episode5/106.webp")
            hide ep5_106

            show ep5_107
            sheila "Tidak kali ini. Setelah ini muncul sesuatu yang lain."
            toby "Benar-benar?"
            sheila "Tentu saja!"
            scene expression ("images/episode5/107.webp")
            hide ep5_107

            scene expression ("images/episode5/108.webp")
            sheila "Melihat? Kami tidak akan bercinta. Aku hanya akan sedikit mengisap penismu, tapi kami tidak sialan!"
            toby "Saya pikir Anda menemukan celah yang sangat manis dalam sistem."
            sheila "Saya bisa menjelaskan lebih banyak tentang celah itu, tetapi saya pikir saya harus menunjukkan kepada Anda."
            toby "Ya ... lakukan itu!"

            show ep5_109
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode5/109.webp")
            hide ep5_109

            show ep5_110
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck me... This is so good!{/i}"
            scene expression ("images/episode5/110.webp")
            hide ep5_110

            show ep5_111
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode5/111.webp")
            hide ep5_111

            show ep5_112
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, she's deepthroating me. This is the best blowjob I've ever had.{/i}"
            $ ui.saybehavior()
            $ ui.interact()
            toby "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI'm going to cum!"
            scene expression ("images/episode5/112.webp")
            hide ep5_112

            with flash
            scene expression ("images/episode5/113.webp") with dissolve
            with flash
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck... That was so, so good!{/i}"
            scene expression ("images/episode5/114.webp") with dissolve
            toby "Apa yang telah saya lakukan untuk mendapatkan ini?"
            sheila "Belum ada, tapi saya berharap Anda mencuci punggung untuk ini."
            toby "Saya suka kesepakatan ini."
            scene expression ("images/episode5/115.webp") with dissolve
            sheila "Apa yang bisa saya katakan, kesenangan adalah milik saya!"

            $ unlockMemory(persistent.memory_16)
            $ renpy.end_replay()

        scene expression ("images/episode5/116.webp") with dissolve
        if toby_job == 0:
            sheila "Jadi [toby!c] sayang, siapa wanita menarik yang Anda ajak bicara."
            scene expression ("images/episode5/117.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Her ass is so perfect.{/i}"
            scene expression ("images/episode5/118.webp") with dissolve
            sheila "Baik, nikmati pemandangannya, kami akan mengobrol nanti!"
            toby "Maaf, Anda mengatakan sesuatu?"
            sheila "Saya bertanya kepada Anda dengan siapa wanita itu yang Anda ajak bicara."
            scene expression ("images/episode5/116.webp") with dissolve
            toby "Oh, dia adalah pacar bosku."
            sheila "Benar-benar. Nyonya Darlene adalah seorang lesbian?"
            toby "Yup, saya juga sedikit terkejut, tetapi saya lebih terkejut dengan kenyataan bahwa mereka sangat berbeda."
            sheila "Ya..."
            sheila "Dan apa yang dia lakukan?"
            toby "Nah, dia adalah pemilik klub. Saya tidak tahu terlalu banyak tentang itu."
            scene expression ("images/episode5/119.webp") with dissolve
            sheila "Oh, saya mengerti, apakah Anda pikir dia suka pelatih pribadi?"
            toby "Saya tidak yakin, tetapi Anda bisa bertanya padanya."
            sheila "Saya akan melakukannya, tetapi dia terlihat sangat menakutkan."
            toby "Lain kali Anda melihat kami berbicara, bergabunglah dengan kami dan saya akan memperkenalkan Anda."
            sheila "Terima kasih [toby!c]. Anda yang terbaik."
        else:
            sheila "Jadi [toby!c] Sayang, bagaimana Anda mengenal Mrs. Darlene?"
            scene expression ("images/episode5/117.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Her ass is so perfect.{/i}"
            scene expression ("images/episode5/118.webp") with dissolve
            sheila "Baik, nikmati pemandangannya, kami akan mengobrol nanti!"
            toby "Maaf, Anda mengatakan sesuatu?"
            sheila "Saya bertanya bagaimana Anda mengenal Ny. Darlene."
            toby "Oh, Darlene? Dia adalah pacar bos saya."
            scene expression ("images/episode5/116.webp") with dissolve
            sheila "Dia sangat beruntung memilikinya."
            toby "Ya, dia adalah dia."
            sheila "Oh jadi itu berarti wanita dengan tato dan rambut hitam sebenarnya adalah pemilik klub?"
            toby "Yup. Itu Katrina."
            sheila "Saya pikir saya telah melihatnya di gym juga."
            scene expression ("images/episode5/119.webp") with dissolve
            toby "Ya. Darlene menyebutkan sesuatu tentang itu."
            sheila "Bagaimana dia? Bos Anda?"
            toby "Yah, dia terlihat sedikit mengintimidasi, tapi saya pikir jika Anda tahu bagaimana berbicara dengannya dia bisa sangat baik."
            sheila "Apakah Anda pikir dia menyukai pelatih pribadi?"
            toby "Saya tidak tahu, mengapa Anda tidak bertanya padanya?"
            sheila "Karena dia terlihat menakutkan."
            toby "Baik, saya akan mencoba berbicara dengannya tentang itu jika kita pernah bertemu di gym."
            sheila "Terima kasih [toby!c]. Anda yang terbaik!"

        scene expression ("images/episode5/120.webp") with dissolve
        sheila "Bagaimanapun, itu harus melakukannya. Lebih baik kami kembali sebelum seseorang menangkap kami!"
        scene expression ("images/episode5/121.webp") with dissolve
        sheila "Terima kasih telah membantu saya mencuci punggung saya!"
        toby "Selama saya mendapatkan hadiah saya, itu akan selalu menjadi kesenangan saya!"
        sheila "Tentu saja. Kompensasi."

    if ep3_lieGirls == True:

        scene expression ("images/episode5/122.webp") with fade
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Oh, I got a message.{/i}"
        scene expression ("images/episode5/123_texting.webp") with dissolve
        if lisa_path == True:
            call sms_incoming ("lisa", "Sorry about this, but I lost a bet with Lauren and now I have to send you a silly picture", img_icon="images/episode5/124_icon.webp", img="images/episode5/124.webp") from _call_sms_incoming_30
            call sms_sent ("lisa", "Haha... You're so cute. I hope you'll lose more bets like this.") from _call_sms_sent_14
            call sms_incoming ("lisa", "Hey... You're not supposed to be on Lauren's side.") from _call_sms_incoming_31
            call sms_sent ("lisa", "I'll side with anyone who makes you send me pictures.") from _call_sms_sent_15
            call sms_incoming ("lisa", "Here. I'll send you however many pictures you want as long as you're on my team.", img_icon="images/episode5/125_icon.webp", img="images/episode5/125.webp") from _call_sms_incoming_32
            call sms_sent ("lisa", "Fine, you convinced me. I'm on your side!") from _call_sms_sent_16
            call sms_incoming ("lisa", "Perfect!") from _call_sms_incoming_33
            call sms_incoming ("lisa", "Anyway, what are you up to?") from _call_sms_incoming_34
            call sms_sent ("lisa", "I just finished my training.") from _call_sms_sent_17
            call sms_incoming ("lisa", "That's so cool.") from _call_sms_incoming_35
            call sms_sent ("lisa", "What about you?") from _call_sms_sent_18
            call sms_incoming ("lisa", "I don't want to answer.") from _call_sms_incoming_36
            call sms_sent ("lisa", "Now you really made me curious.") from _call_sms_sent_19
            call sms_incoming ("lisa", "I'm still in my pajamas. I'm being lazy.") from _call_sms_incoming_37
            call sms_sent ("lisa", "Let me fix that for you.") from _call_sms_sent_20
            call sms_incoming ("lisa", "How do you plan on doing that?") from _call_sms_incoming_38
            call sms_sent ("lisa", "You have 30 minutes to get ready. We're going out.") from _call_sms_sent_21
            call sms_incoming ("lisa", "Only if you promise to bring me home before 6PM. I promised Lauren we'd go clubbing.") from _call_sms_incoming_39
            call sms_sent ("lisa", "Perfect! I'll go change and come pick you up.") from _call_sms_sent_22
        else:
            call sms_incoming ("lauren", "Ummm. I need to explain this picture. It's Lisa's fault!", img_icon="images/episode5/126_icon.webp", img="images/episode5/126.webp") from _call_sms_incoming_40
            call sms_sent ("lauren", "If this is Lisa's fault, all I can say is 'I love her'.") from _call_sms_sent_23
            call sms_incoming ("lauren", "Hey... You're supposed to love me not her.") from _call_sms_incoming_41
            call sms_sent ("lauren", "You need to up your game then.") from _call_sms_sent_24
            call sms_incoming ("lauren", "Speaking of up. Is it up now?", img_icon="images/episode5/127_icon.webp", img="images/episode5/127.webp") from _call_sms_incoming_42
            call sms_sent ("lauren", "We're talking about the game, right?") from _call_sms_sent_25
            call sms_incoming ("lauren", "Maybe!") from _call_sms_incoming_43
            call sms_sent ("lauren", "Fine. You win! I love you more than I love her.") from _call_sms_sent_26
            call sms_incoming ("lauren", "Perfect!") from _call_sms_incoming_44
            call sms_sent ("lauren", "By the way, wanna go grab a coffee later?") from _call_sms_sent_27
            call sms_incoming ("lauren", "Well since I found you, I told Lisa we'd go clubbing tonight so she can find someone at least half as sexy as you!") from _call_sms_incoming_45
            call sms_sent ("lauren", "We'll be back at 6 so you can get ready!") from _call_sms_sent_28
            call sms_incoming ("lauren", "Perfect! See you in an hour?") from _call_sms_incoming_46
            call sms_sent ("lauren", "Make it 30 minutes. I'll go change my clothes and come pick you up.") from _call_sms_sent_29
            call sms_incoming ("lauren", "I can't promise I'll be ready in 30 minutes, but I promise I'll try.") from _call_sms_incoming_47
            call sms_sent ("lauren", "That will work. See you then!") from _call_sms_sent_30

        hide screen message


    scene expression ("images/episode5/128.webp") with dissolve
    if ep3_lieGirls:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should get going. I wonder if there are any cool coffee shops around.{/i}"
    else:
        $ ui.saybehavior()
        $ ui.interact()
    $ progress = 71
    return

label episode5_sunday_dateLisa:
    stop music fadeout 1.0
    scene expression ("images/episode5/129.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should tell her I'm here.{/i}"
    scene expression ("images/episode5/129_texting.webp") with dissolve
    call sms_sent ("lisa", "I'm downstairs.") from _call_sms_sent_31
    call sms_incoming ("lisa", "Ummm... Already?") from _call_sms_incoming_48
    call sms_incoming ("lisa", "I'm not ready yet!") from _call_sms_incoming_49
    call sms_sent ("lisa", "No worries. Take your time!") from _call_sms_sent_32
    call sms_incoming ("lisa", "I'll be down in 2 minutes.") from _call_sms_incoming_50
    hide screen message

    show screen ui_message("10 minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/130.webp") with dissolve
    hide screen ui_message
    lisa "Maaf, maaf, maaf. Saya berjanji saya melakukan yang terbaik untuk bergegas, tapi ..."

    scene expression ("images/episode5/131.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    toby "Tidak masalah, itu sepadan!"
    scene expression ("images/episode5/132.webp") with dissolve
    lisa "Anda hanya mengatakan itu untuk membuat saya merasa lebih baik."
    scene expression ("images/episode5/133.webp") with dissolve
    toby "Tidak, kamu terlihat hebat."

    show ep5_134 with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/134.webp") with dissolve
    hide ep5_134
    lisa "Oke, saya percaya Anda sekarang!"
    scene expression ("images/episode5/135.webp") with dissolve
    toby "Hanya sekarang?"
    lisa "Anda perlu membuktikannya kepada saya. Kata -kata tidak ada artinya tanpa tindakan."
    menu:
        "[JGR] Haruskah kita kembali ke atas dan memberi Anda lebih banyak bukti?"(csq="Lisa +1 & Galeri Gambar"):
            $ lisa_rel += 1
            $ unlockImage(persistent.lisa_06)
            scene expression ("images/episode5/136.webp") with dissolve
            lisa "Anda konyol!"
        "{i} ubah subjek {/i}":
            pass

    scene expression ("images/episode5/137.webp") with dissolve
    toby "Jadi apakah kamu suka kopi?"
    lisa "Apakah Anda bercanda? Saya menyukainya!"
    toby "Sempurna. Saya menemukan kedai kopi yang nyaman di dekatnya."
    lisa "Hebat, saya sedang mencari kedai kopi dekat, karena kami membeli pembuat kopi baru dan itu!"
    scene expression ("images/episode5/138.webp") with dissolve
    toby "Bahasa, wanita muda!"
    lisa "Maaf, Ayah."
    toby "Cobalah untuk tidak menelepon saya ayah setelah kami hanya berciuman. Ini sedikit aneh."
    lisa "Anda membuatnya aneh sekarang."

    scene expression ("images/episode5/139.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/139_1.webp") with dissolve:
        xalign 1.0
        yalign 1.0
        linear 10.0 xalign 0.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/140.webp") with dissolve
    lisa "Saya pikir saya baru saja menemukan tempat favorit baru saya."
    toby "Senang Anda menyukainya!"
    scene expression ("images/episode5/141.webp") with dissolve
    barista "Hai, yang di sana. Apa yang bisa saya dapatkan dari Anda?"
    scene expression ("images/episode5/142.webp") with dissolve
    lisa "Saya ingin latte macchiato dan croissant."
    scene expression ("images/episode5/141.webp") with dissolve
    barista "Besar. Dan untukmu?"
    scene expression ("images/episode5/143.webp") with dissolve
    toby "Cappuccino dan satu air diam."
    scene expression ("images/episode5/141.webp") with dissolve
    barista "Untuk di sini atau pergi?"
    scene expression ("images/episode5/143.webp") with dissolve
    toby "Di Sini."
    scene expression ("images/episode5/141.webp") with dissolve
    barista "Tolong buat diri Anda nyaman dan saya akan membawa semuanya ke meja."
    scene expression ("images/episode5/144.webp") with dissolve
    lisa "Jadi [toby!c]. Apa kabar hari ini?"
    toby "Nah, mengingat fakta bahwa masih lebih awal, belum banyak terjadi kecuali bahwa saya bertaruh dengan kecil saya [sister]."
    lisa "Katakan, dan apa yang perlu Anda lakukan untuk menang."
    toby "Saya harus merenovasi loteng dan halaman, sendirian."
    scene expression ("images/episode5/145.webp") with dissolve
    lisa "Saya tidak pernah membayangkan Anda sebagai pekerja konstruksi."
    toby "Baik, saya tidak."
    scene expression ("images/episode5/146.webp") with dissolve
    toby "Terima kasih!"
    barista "Tentu."
    scene expression ("images/episode5/147_laugh.webp") with dissolve
    lisa "Dan bagaimana Anda berencana memenangkan taruhan?"
    scene expression ("images/episode5/148_awkward.webp") with dissolve
    toby "Dunno. Tutorial?"
    scene expression ("images/episode5/147_laugh.webp") with dissolve
    lisa "Astaga. Saya ingin melihat Anda dengan sekop di tangan Anda."
    scene expression ("images/episode5/148_curious.webp") with dissolve
    toby "Tongkat ... apa?"
    scene expression ("images/episode5/147_smile.webp") with dissolve
    lisa "Anda bahkan lebih buruk dari yang saya kira."
    scene expression ("images/episode5/148_laugh.webp") with dissolve
    toby "Pertama, Anda menjelaskan kepada saya apa hal itu dan kemudian Anda bisa menilai."
    scene expression ("images/episode5/147_smile.webp") with dissolve
    lisa "Nah, sekop adalah alat yang Anda gunakan untuk meletakkan ubin keramik atau batu bata."
    scene expression ("images/episode5/147_cute.webp") with dissolve
    lisa "Dan roller cat adalah alat yang Anda ..."
    scene expression ("images/episode5/148_meh.webp") with dissolve
    toby "Saya tahu apa itu roller cat. Pokoknya seperti yang saya katakan, betapa sulitnya belajar cara menggunakan trol itu atau apa pun."
    scene expression ("images/episode5/147_cute.webp") with dissolve
    lisa "Sekop."
    scene expression ("images/episode5/148_curious.webp") with dissolve
    toby "Anda tahu banyak sekali tentang konstruksi."
    scene expression ("images/episode5/147_laugh.webp") with dissolve
    lisa "Apa yang bisa saya katakan, saya sangat pintar."
    scene expression ("images/episode5/147_smile.webp") with dissolve
    lisa "Dan ayah saya memiliki perusahaan konstruksi sendiri dan ..."
    lisa "Itu tidak penting."
    scene expression ("images/episode5/148_curious.webp") with dissolve
    toby "Ya, memang begitu! Sekarang Anda membuat saya sangat penasaran!"
    scene expression ("images/episode5/147_cute.webp") with dissolve
    lisa "Ini bukan apa -apa. Hanya saja ketika saudara lelaki saya masih muda, sebagai hukuman atas perilaku buruk ia harus bekerja di sana."
    scene expression ("images/episode5/148_normal.webp") with dissolve
    toby "Sesuatu memberi tahu saya bahwa dia bukan satu -satunya yang terjadi di lokasi konstruksi."
    scene expression ("images/episode5/147_laugh.webp") with dissolve
    lisa "Lihat aku. Apakah saya benar -benar terlihat seperti seorang gadis yang menghabiskan hari -hari musim panasnya di lokasi konstruksi?"
    scene expression ("images/episode5/148_laugh.webp") with dissolve
    toby "Tidak. Tidak juga, tetapi sesuatu memberi tahu saya bahwa Anda bukan gadis baik yang Anda klaim."
    scene expression ("images/episode5/147_shy.webp") with dissolve
    lisa "Baik, baiklah. Anda menangkap saya. Tetapi dalam pertahanan saya, pekerjaan saya adalah membersihkan alat dan menyapu kamar."
    scene expression ("images/episode5/148_laugh.webp") with dissolve
    toby "Hanya karena penasaran apakah Anda harus mengenakan topi plastik konyol itu?"
    scene expression ("images/episode5/147_tongue.webp") with dissolve
    lisa "Untuk informasi Anda, itu adalah topi yang sulit, dan ya, saya membunuhnya."
    scene expression ("images/episode5/148_laugh.webp") with dissolve
    toby "Saya hanya bisa membayangkan."
    scene expression ("images/episode5/148_normal.webp") with dissolve
    toby "Saya tidak sabar untuk memulai sekarang karena saya tahu saya memiliki seseorang yang dapat membantu saya."
    scene expression ("images/episode5/147_cute.webp") with dissolve
    lisa "Saya benar -benar ingin membantu Anda, tetapi tidakkah Anda mengatakan bahwa Anda harus melakukan semuanya sendiri?"
    scene expression ("images/episode5/148_sad.webp") with dissolve
    toby "Kotoran!"
    scene expression ("images/episode5/147_laugh.webp") with dissolve
    lisa "Saya suka [sister] Anda. Dia tahu bagaimana membuat kesepakatan."
    scene expression ("images/episode5/148_smile.webp") with dissolve
    toby "Lihat siapa yang ada di tim yang salah kali ini."
    scene expression ("images/episode5/147_smile.webp") with dissolve
    lisa "Maaf, maksud saya saya benci betapa baiknya dia. Aku sangat sedih karena aku tidak bisa membantumu."
    scene expression ("images/episode5/148_smile.webp") with dissolve
    toby "Aku tidak melihat air mata di matamu?"
    scene expression ("images/episode5/147_laugh.webp") with dissolve
    lisa "Saya memiliki kondisi langka di mana air mata saya tersangkut di dalam."
    scene expression ("images/episode5/148_laugh.webp") with dissolve
    toby "Ya ... itu kondisi yang sangat langka."
    scene expression ("images/episode5/147_smile.webp") with dissolve
    lisa "Saya tahu, saya tahu. Ini sangat sulit."
    scene expression ("images/episode5/148_smile.webp") with dissolve
    toby "Anda sangat konyol!"
    scene expression ("images/episode5/147_normal.webp") with dissolve
    lisa "Itu tidak mengganggu Anda, saya harap?"
    scene expression ("images/episode5/148_smile.webp") with dissolve
    toby "Tidak sama sekali ... Saya benar -benar menyukainya."
    scene expression ("images/episode5/147_arogant.webp") with dissolve
    lisa "Apa yang bisa saya katakan. Anda sangat beruntung telah menemukan saya."
    scene expression ("images/episode5/148_laugh.webp") with dissolve
    toby "Ya ... beruntung aku!"


    scene expression ("images/episode5/149.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/150.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/151.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/152.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/153.webp") with dissolve:
        xalign 0.5
        yalign 0.2
        zoom 0.5
        linear 10.0 zoom 0.8 yalign 0.0
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    $ progress = 72
    scene expression ("images/episode5/154.webp") with dissolve
    lisa "Saya pikir kita harus pulang sehingga kita bisa bersiap -siap untuk malam ini."
    toby "Kami?"
    lisa "Tentu saja. Apakah Anda benar -benar berpikir saya membiarkan Anda pulang? Anda datang ke klub bersama kami."
    if toby_job == 1:
        toby "Hanya jika kita pergi ke klimaks, karena aku seharusnya ada di sana malam ini."
        lisa "Tentu saja!"
    else:
        toby "Itu bukan malam perempuan?"
        lisa "Tidak. Kami akan mencari pasangan seksual untuk Lauren, tetapi kami membutuhkan pendapat ketiga."
        toby "Beruntung aku!"
    scene expression ("images/episode5/155.webp") with dissolve
    toby "Aku akan menunggumu di sini."
    lisa "Tidak. Anda akan datang ke atas, saya tidak bisa membiarkan Anda menunggu di sini selama tiga puluh menit."
    scene expression ("images/episode5/156_1.webp") with dissolve
    toby "Tiga puluh menit? Memimpin jalan itu."
    scene expression ("images/episode5/156_2.webp") with dissolve
    lisa "Baik ya. Lauren membutuhkan waktu lama untuk bersiap -siap."
    scene expression ("images/episode5/156_1.webp") with dissolve
    toby "Anda sudah meyakinkan saya."
    scene expression ("images/episode5/157.webp") with fade
    lauren "Saya pikir Anda akan membuat saya hantu."
    scene expression ("images/episode5/158.webp") with dissolve
    lisa "Saya berjanji. Bukankah aku?"
    scene expression ("images/episode5/159.webp") with dissolve
    lisa "Buat diri Anda nyaman di sofa. Saya akan selesai dalam sepuluh menit."
    scene expression ("images/episode5/157.webp") with dissolve
    lauren "Lebih seperti tiga puluh."
    scene expression ("images/episode5/160.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    if lauren_sidePath:
        scene expression ("images/episode5/161.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()
        lauren "Jadi? Bagaimana tanggal Anda?"
        scene expression ("images/episode5/162.webp") with dissolve
        toby "..."
        lauren "Anda lebih baik tidak melihat pantat saya setelah kencan dengan Lisa."
        scene expression ("images/episode5/163.webp") with dissolve
        toby "Maaf, saya sedang bermimpi. Anda mengatakan sesuatu?"
        scene expression ("images/episode5/164.webp") with dissolve
        lauren "Saya berkata, saya tidak mengenakan celana dalam apa pun."
        scene expression ("images/episode5/165.webp") with dissolve
        toby "Ummm ..."
        menu:
            "{i} [JGR] Minta Bukti {/i}"(csq="Lauren +1 & Galeri Gambar"):
                $ lauren_rel += 1
                toby "My [mom] told me \"Don't believe everything you hear\"."
                scene expression ("images/episode5/166.webp") with dissolve:
                    yalign 1.0
                    linear 10.0 yalign 0.0

                $ ui.pausebehavior(9.3)
                $ ui.saybehavior()
                $ ui.interact()
                $ unlockImage(persistent.lauren_06)
                lauren "[mother] Anda adalah wanita yang cerdas."
                toby "Saya tidak pernah curiga bahwa saran [mom] saya akan membuat saya sejauh ini."
                scene expression ("images/episode5/167.webp") with dissolve
                lauren "Jangan lupa untuk memberitahunya betapa dia membantu Anda hari ini."
                scene expression ("images/episode5/168.webp") with dissolve
                toby "Saya pikir kita akan melewatkan bagian itu."
            "{i} tidak mengatakan apa -apa {/i}":
                pass
        scene expression ("images/episode5/169.webp") with dissolve
        lauren "Ngomong -ngomong ... bagaimana kencanmu?"
    else:
        scene expression ("images/episode5/169.webp") with dissolve
        lauren "Jadi? Bagaimana tanggal Anda?"
    toby "Nah, pertama kami pergi ke kedai kopi dan kemudian ..."

    show screen ui_message("Half an hour later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/170.webp") with dissolve
    hide screen ui_message
    lisa "Ta da ..."

    scene expression ("images/episode5/171.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    toby "Wow ... kamu terlihat cantik."
    lauren "Dan dia hanya membutuhkan waktu setengah jam, bayangkan jika dia tidak terburu -buru."
    lisa "Hei ... itu tidak benar."
    scene expression ("images/episode5/172.webp") with dissolve
    toby "Dia mengatakan kepada saya bahwa Anda adalah orang yang membutuhkan waktu lama untuk bersiap -siap."
    lauren "Apakah dia sekarang. Setiap kali saya terlambat, itu karena dia."
    scene expression ("images/episode5/173.webp") with dissolve
    lisa "Jangan dengarkan dia. Dia tidak tahu apa yang dia bicarakan. Lepaskan."

    return


label episode5_sunday_dateLauren:
    scene expression ("images/episode5/129.webp") with fade
    call sms_sent ("lauren", "I'm downstairs.") from _call_sms_sent_33
    call sms_incoming ("lauren", "Be right there!") from _call_sms_incoming_51
    hide screen message


    scene expression ("images/episode5/174.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    lauren "Hai [toby!c]. Saya harap Anda tidak menunggu saya terlalu lama."
    scene expression ("images/episode5/175.webp") with dissolve
    toby "Sama sekali tidak."

    show ep5_176 with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/176.webp") with dissolve
    hide ep5_176
    toby "Ngomong -ngomong, kamu terlihat cantik."
    scene expression ("images/episode5/177.webp") with dissolve
    lauren "Anda mencoba membuat saya tersipu."
    toby "Apakah itu berhasil?"
    scene expression ("images/episode5/178.webp") with dissolve
    lauren "Mungkin!"
    lauren "Jadi kemana kamu membawaku?"
    toby "Nah, saya belum minum kopi pagi ini, ingin mengambilnya?"
    scene expression ("images/episode5/179.webp") with dissolve
    lauren "Itu akan sempurna."
    lauren "Saya suka cara Anda berpikir."

    scene expression ("images/episode5/180_1.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/180_2.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/181.webp") with dissolve
    toby "Kedai kopi ini memiliki beberapa ulasan terbaik."
    lauren "Saya suka betapa nyamannya, kami mencari kedai kopi untuk datang, karena pembuat kopi yang kami beli membuat kencing mutlak."
    toby "Saya tahu apa yang saya dapatkan untuk Anda untuk ulang tahun Anda!"
    scene expression ("images/episode5/182.webp") with dissolve
    lauren "Saya berharap sesuatu yang jahat yang tidak melibatkan pembuat kopi."
    toby "Bagus. Saya tidak tahu apa yang saya dapatkan untuk Anda untuk ulang tahun Anda."
    scene expression ("images/episode5/183.webp") with dissolve
    barista "Halo. Apa yang bisa saya dapatkan dari Anda?"
    scene expression ("images/episode5/184.webp") with dissolve
    lauren "Tolong putih datar!"
    scene expression ("images/episode5/185.webp") with dissolve
    lauren "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Because I'm white and flat.{/i}"
    menu:
        "[JGR] Anda membutuhkan cermin baru, karena tidak ada yang datar."(csq="Lauren +1 & Galeri Gambar"):
            $ lauren_rel += 1
            $ unlockImage(persistent.lauren_07)
            lauren "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}You mean I'm fat? I have abs so I do have something flat.{/i}"
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}If you don't let me order my coffee I'll slap your ass till it gets flat.{/i}"
            lauren "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Don't tempt me. I'd almost like to see you try.{/i}"
        "Anda baik -baik saja.":
            lauren "{size=12}{color=#FDCA6E} whispering *{/color}{/size}\n{i}Well, if you say so, I'll believe you.{/i}"
    scene expression ("images/episode5/186.webp") with dissolve
    toby "Dan cappuccino untuk saya."
    scene expression ("images/episode5/183.webp") with dissolve
    barista "Untuk di sini atau pergi?"
    scene expression ("images/episode5/186.webp") with dissolve
    toby "Di sini, tolong!"
    scene expression ("images/episode5/183.webp") with dissolve
    barista "Tolong buat diri Anda nyaman dan saya akan membawa kopi dalam sedetik."
    scene expression ("images/episode5/187.webp") with dissolve
    toby "Jadi, bagaimana Anda menyukai kota sejauh ini? Berhasil menetap?"
    lauren "Anda akan terkejut betapa saya sangat menyukainya di sini."
    toby "Benar-benar? Saya belum melihat terlalu banyak kota."
    lauren "Saya juga tidak, tetapi saya telah menemukan studio di mana saya dapat melatih tarian eksotis saya."
    scene expression ("images/episode5/188.webp") with dissolve
    toby "Kami benar -benar perlu membicarakan lebih banyak tentang hobi Anda."
    scene expression ("images/episode5/189.webp") with dissolve
    lauren "Terima kasih banyak."
    barista "Dengan senang hati, sayang!"
    scene expression ("images/episode5/190_laugh.webp") with dissolve
    lauren "Jadi apa yang ingin Anda ketahui tentang hobi saya."
    scene expression ("images/episode5/191_flirty.webp") with dissolve
    toby "Kapan Anda akan tampil untuk publik."
    scene expression ("images/episode5/190_flirty.webp") with dissolve
    lauren "Khalayak luas atau yang kecil?"
    scene expression ("images/episode5/191_laugh.webp") with dissolve
    toby "Saya sudah berpikir lebih pribadi."
    scene expression ("images/episode5/190_laugh.webp") with dissolve
    lauren "Seorang penonton, jenis pribadi?"
    scene expression ("images/episode5/191_flirty.webp") with dissolve
    toby "Nah, kenapa tidak!?"
    scene expression ("images/episode5/190_sexy.webp") with dissolve
    lauren "Dan apakah Anda memiliki seseorang dalam pikiran yang bisa saya lakukan?"
    scene expression ("images/episode5/191_flirty.webp") with dissolve
    toby "Saya tidak tahu, tetapi seseorang yang mungkin sangat dekat dengan Anda. Baik secara emosional maupun fisik."
    scene expression ("images/episode5/190_flirty.webp") with dissolve
    lauren "Seperti beberapa meter jauhnya, agak dekat secara fisik?"
    scene expression ("images/episode5/191_flirty.webp") with dissolve
    toby "Mengapa tidak?"
    scene expression ("images/episode5/190_turn.webp") with dissolve
    lauren "Sekarang setelah Anda menyebutkannya, barista kami cukup panas!"
    scene expression ("images/episode5/191_fu.webp") with dissolve
    toby "Anda tahu apa. Mengisapnya!"
    scene expression ("images/episode5/190_laugh.webp") with dissolve
    lauren "Baik, baiklah. Jika Anda seorang anak yang baik, saya akan memberi Anda hadiah ulang tahun yang istimewa!"
    scene expression ("images/episode5/191_curious.webp") with dissolve
    toby "Apakah Anda bahkan tahu kapan ulang tahun saya?"
    scene expression ("images/episode5/190_awkward.webp") with dissolve
    lauren "Belum, tapi saya akan mengetahuinya."
    scene expression ("images/episode5/191_smile.webp") with dissolve
    toby "Nah, hari ini!"
    scene expression ("images/episode5/190_laugh.webp") with dissolve
    lauren "Ya, benar."
    scene expression ("images/episode5/191_normal.webp") with dissolve
    toby "..."
    scene expression ("images/episode5/190_surprised.webp") with dissolve
    lauren "Tunggu ... apakah kamu serius?"
    scene expression ("images/episode5/191_normal.webp") with dissolve
    toby "Apakah saya terlihat seperti bercanda?"
    scene expression ("images/episode5/190_awkward.webp") with dissolve
    lauren "Mengapa Anda tidak mengatakan itu sebelumnya?"
    scene expression ("images/episode5/191_laugh.webp") with dissolve
    toby "Tidak masalah sekarang. Yang penting adalah Anda tahu sekarang, jadi saya berharap hadiah saya!"
    scene expression ("images/episode5/190_doubtful.webp") with dissolve
    lauren "Anda berbohong kepada saya kan?"
    scene expression ("images/episode5/191_laugh.webp") with dissolve
    toby "Kapan saya pernah berbohong kepada Anda."
    scene expression ("images/episode5/190_doubtful.webp") with dissolve
    lauren "Anda tertawa. Saya tidak tahu harus berpikir apa."
    scene expression ("images/episode5/191_laugh.webp") with dissolve
    toby "Apa yang bisa saya katakan. Saya orang yang bahagia."
    scene expression ("images/episode5/190_flirty.webp") with dissolve
    lauren "Saya akan memberi Anda tes, untuk melihat apakah Anda hanya mengacaukan saya."
    scene expression ("images/episode5/191_smile.webp") with dissolve
    toby "Bawa."
    scene expression ("images/episode5/190_sexy.webp") with dissolve
    lauren "Jika ini hari ulang tahun Anda, Anda akan mendapatkan tarian pribadi Anda, tetapi jika tidak kami akan berhubungan seks hari ini."
    lauren "Jadi? Apakah ini ulang tahun Anda atau tidak?"
    scene expression ("images/episode5/191_laugh.webp") with dissolve
    toby "Neraka tidak. Kami berhubungan seks malam ini!"
    scene expression ("images/episode5/190_laugh.webp") with dissolve
    lauren "Itulah yang saya pikirkan."
    scene expression ("images/episode5/190_doubtful.webp") with dissolve
    lauren "Jadi ini bukan hari ulang tahunmu hari ini."
    scene expression ("images/episode5/191_laugh.webp") with dissolve
    toby "Tidak, tidak!"
    scene expression ("images/episode5/190_laugh.webp") with dissolve
    lauren "Anda tidak mengatakan hanya untuk meniduriku kan?"
    scene expression ("images/episode5/191_flirty.webp") with dissolve
    toby "Tidak ada dan di sampingnya aku akan menidurimu."
    scene expression ("images/episode5/190_flirty.webp") with dissolve
    lauren "Seseorang yakin percaya diri di sini."
    scene expression ("images/episode5/191_laugh.webp") with dissolve
    toby "Seseorang sangat menyukaimu!"
    scene expression ("images/episode5/190_shy.webp") with dissolve
    lauren "Ummm ..."
    lauren "Kopi ini sangat enak!"

    scene expression ("images/episode5/192.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/193.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/194.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/195.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/196.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    $ progress = 72
    scene expression ("images/episode5/197.webp") with dissolve
    lauren "Sial, hampir jam 6. Kita harus bersiap -siap untuk klub."
    toby "Kami? Saya pikir itu hanya seorang gadis malam."
    lauren "Dan bosan dengan Lisa mengatakan bahwa dia tidak seperti anak laki -laki yang saya pilih untuknya?"
    lauren "Neraka tidak. Anda Pak, akan ikut dengan kami."
    toby "Baik ... mari kita bosan bersama."

    scene expression ("images/episode5/198.webp") with fade
    toby "Aku akan menunggumu di lantai bawah."
    lauren "Neraka Anda dan selain itu, Anda meninggalkan sepeda di sini. Kami akan mengambil mobil Lisa."
    toby "Anda tidak menyukai sepeda saya?"
    scene expression ("images/episode5/199.webp") with dissolve
    lauren "Berhenti bertingkah seperti diva. Mari kita naik ke atas."
    toby "Bertingkah seperti diva. Lihat siapa yang berbicara."
    scene expression ("images/episode5/200.webp") with dissolve
    lauren "Sayang. Saya pulang!"

    scene expression ("images/episode5/201.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/202.webp") with dissolve
    lisa "Saya pikir Anda memberi tahu saya setelah Anda berbicara dengan saya untuk keluar."
    lauren "Umm ... mungkin Anda ingin tahu bahwa [toby!c] akan datang bersama kami."
    lisa "Dingin. Setidaknya kita akan bersenang -senang seperti itu."
    scene expression ("images/episode5/203.webp") with dissolve
    toby "Umm ... terima kasih!"
    scene expression ("images/episode5/204.webp") with dissolve
    lisa "Sial ... sial ... kamu di sini?"
    scene expression ("images/episode5/203.webp") with dissolve
    toby "Maaf?"
    scene expression ("images/episode5/205.webp") with dissolve
    lisa "Lauren !!! Aku akan membunuhmu, mengapa kamu tidak memberitahuku bahwa dia ada di sini."
    scene expression ("images/episode5/206.webp") with dissolve
    lauren "Saya pikir Anda ingin mencuri pria saya jadi saya membiarkan Anda melakukan pekerjaan Anda."
    scene expression ("images/episode5/205.webp") with dissolve
    lisa "Anda benar -benar menyebalkan!"
    lisa "Maaf [toby!c], saya tidak berarti bagi Anda untuk melihat saya seperti itu."
    toby "Jangan khawatir."
    scene expression ("images/episode5/207_1.webp") with dissolve
    lauren "Saya akan berubah. Tunggu aku di sofa dan jangan biarkan Lisa mencurimu."
    scene expression ("images/episode5/207_2.webp") with dissolve
    toby "Tentu. Saya menang!"
    scene expression ("images/episode5/208.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/209.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    if lisa_sidePath == True:
        scene expression ("images/episode5/210.webp") with dissolve
        lisa "Maaf Anda harus melihat saya seperti itu."
        toby "Jangan khawatir, aku tidak terlihat."
        scene expression ("images/episode5/211.webp") with dissolve
        lisa "Benar."
        scene expression ("images/episode5/212.webp") with dissolve
        toby "Anda terlihat seperti Anda tidak percaya padaku."
        scene expression ("images/episode5/213.webp") with dissolve
        lisa "Saya percaya Anda, tetapi saya hanya ingat apa yang Anda katakan di pantai ketika Lauren bertanya kepada Anda siapa yang Anda pikir adalah gadis terpanas."
        scene expression ("images/episode5/212.webp") with dissolve
        toby "Oh ... baiklah aku tidak mengatakan kamu tidak panas. Saya baru saja mengatakan bahwa saya tidak terlihat."
        scene expression ("images/episode5/213.webp") with dissolve
        lisa "Anda benar -benar pria. Lauren pasti sangat beruntung."
        scene expression ("images/episode5/212.webp") with dissolve
        toby "Baik, saya terlihat sedikit."
        scene expression ("images/episode5/213.webp") with dissolve
        lisa "Itu membuatku beruntung juga?"
        scene expression ("images/episode5/212.webp") with dissolve
        menu:
            "[JGR] Itu membuatmu panas."(csq="Lisa +1 & Galeri Gambar"):
                $ lisa_rel += 1
                $ unlockImage(persistent.lisa_07)
            "Anda bisa mengatakan itu.":
                pass
        scene expression ("images/episode5/214.webp") with dissolve
        lisa "Anda adalah pemikat seperti itu."
        scene expression ("images/episode5/212.webp") with dissolve
        toby "Aku tahu. Anda pasti sangat cemburu pada Lauren sekarang."
        scene expression ("images/episode5/211.webp") with dissolve
        lisa "Jangan sampai pada diri kita sendiri."
        scene expression ("images/episode5/215.webp") with dissolve
        toby "Baik, baiklah!"
    else:
        scene expression ("images/episode5/210.webp") with dissolve
        lisa "Maaf sebelumnya."
        toby "Saya perlu meminta maaf. Aku seharusnya tinggal di bawah, tetapi Lauren benar -benar bersikeras."
        scene expression ("images/episode5/213.webp") with dissolve
        lisa "Mari kita menyalahkan semuanya pada Lauren dan kami sama -sama bahagia."
        scene expression ("images/episode5/215.webp") with dissolve
        toby "Bekerja untuk saya."

    show screen ui_message("A few minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/216.webp") with dissolve
    hide screen ui_message
    lauren "Saya pikir Anda tidak membiarkan dia mencuri Anda?"

    scene expression ("images/episode5/217.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    toby "Wow ... kamu cantik."
    lauren "Terima kasih. Jadi itu artinya Anda masih milik saya?"

    scene expression ("images/episode5/218.webp") with dissolve
    lisa "Dia semua milikmu."
    if lisa_sidePath == True:
        scene expression ("images/episode5/219.webp") with dissolve
        lisa "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}For now anyway.{/i}"
        scene expression ("images/episode5/220.webp") with dissolve
        lauren "Kamu jalang. Saya mendengar itu!"
    scene expression ("images/episode5/221.webp") with dissolve
    toby "Kita harus pergi."

    return

label episode5_sunday_clubDrive:
    $ progress = 73
    stop music fadeout 1.0
    scene expression ("images/episode5/222.webp") with fade
    lauren "Ngomong -ngomong, Lisa, berikan [toby!c] kunci Anda."
    scene expression ("images/episode5/223.webp") with dissolve
    lisa "Saya tidak mengemudi seburuk itu."
    scene expression ("images/episode5/222_2.webp") with dissolve
    lauren "Tidak ... Anda tidak mengemudi seburuk itu, karena apa yang Anda lakukan di belakang kemudi tidak dapat dianggap mengemudi."
    scene expression ("images/episode5/224.webp") with dissolve
    lisa "Bagus..."
    toby "Buruk itu?"
    lisa "Dia melebih -lebihkan."
    lauren "Apakah saya?"

    scene expression ("images/episode5/225_1.webp") with fade
    toby "Jadi? Apa yang ingin kalian lakukan?"
    scene expression ("images/episode5/225_2.webp") with dissolve
    lauren "Saya merasa ingin menari."
    scene expression ("images/episode5/225_3.webp") with dissolve
    lisa "Dan saya merasa seperti satu atau dua minuman pertama jadi saya tidak peduli bahwa saya benar -benar tidak tahu cara menari."
    scene expression ("images/episode5/225_1.webp") with dissolve
    toby "Anda tidak bisa seburuk itu."
    scene expression ("images/episode5/226.webp") with dissolve
    lisa "..."
    scene expression ("images/episode5/227.webp") with dissolve
    lauren "Dia tidak. Itu hanya dia membandingkan dirinya dengan saya."

    scene expression ("images/episode5/228.webp") with dissolve
    if toby_job == 0:
        katrina "Lihat siapa itu. Jika itu bukan agen real estat favorit saya."
        toby "Oh ... selamat malam, ma."
        scene expression ("images/episode5/229.webp") with dissolve
        katrina "Halo wanita cantik, pikiran jika saya mencuri pria Anda selama beberapa menit?"
        lauren "Tentu. Kami akan mendapatkan meja. Bertemu kami di sana?"
        toby "Tentu."
        katrina "Dan nona -nona, silakan minum sesuatu. Itu ada di rumah."
        lisa "Terima kasih, ma \ 'am."
        katrina "Tidak masalah cantik."
        scene expression ("images/episode5/231.webp") with dissolve
        katrina "Jadi? Ubah pikiran Anda tentang bekerja untuk saya?"
        scene expression ("images/episode5/230.webp") with dissolve
        toby "Saya minta maaf, tapi saya sangat suka bekerja untuk Darlene."
        scene expression ("images/episode5/231.webp") with dissolve
        katrina "Sayang sekali. Kami bisa bersenang -senang bersama."
        scene expression ("images/episode5/231.webp") with dissolve
        katrina "Jadi, yang mana milikmu?"
        scene expression ("images/episode5/230.webp") with dissolve
        if lisa_path == True:
            if lauren_sidePath:
                toby "Mari kita katakan keduanya."
            else:
                toby "Si pirang."
        else:
            if lisa_sidePath:
                toby "Mari kita katakan keduanya."
            else:
                toby "Si rambut merah."
        scene expression ("images/episode5/231.webp") with dissolve
        katrina "Aku menyukaimu. Anda tahu apa yang Anda inginkan dan omong -omong saya masih cemburu pada Darlene karena mencuri Anda dari saya."
        scene expression ("images/episode5/230.webp") with dissolve
        toby "Saya akan mengingatnya."
        scene expression ("images/episode5/232.webp") with dissolve
        katrina "Saya akan membiarkan Anda kembali ke teman kencan Anda, tetapi hanya agar Anda tahu, tawaran saya masih berdiri."
        toby "Terima kasih Ma \ 'Am."
    else:

        katrina "Lihat siapa itu. Jika itu bukan karyawan favorit saya dan dengan dua wanita cantik."
        toby "Oh, hai Mrs. Katrina."
        scene expression ("images/episode5/229.webp") with dissolve
        katrina "Apakah Anda Hot Ladies Mind jika saya mencuri pria Anda selama beberapa menit?"
        lauren "Tentu. Tidak masalah."
        katrina "Dapatkan diri Anda sesuatu untuk diminum. Itu ada di rumah."
        lisa "Terima kasih, ma \ 'am."
        scene expression ("images/episode5/231.webp") with dissolve
        katrina "Saya senang melihat Anda menganggap serius pekerjaan Anda."
        katrina "Saya akan memberi Anda uang tambahan jika Anda bercinta salah satunya di sini di depan umum."
        scene expression ("images/episode5/230.webp") with dissolve
        toby "Saya tidak berpikir kita pada saat itu, tetapi saya akan mengingatnya."
        scene expression ("images/episode5/231.webp") with dissolve
        katrina "Itu memalukan, saya akan senang melihat penis Anda di salah satu dari mereka."
        if katrina_path:
            scene expression ("images/episode5/230.webp") with dissolve
            toby "Anda sangat tertarik dengan penisku untuk seorang lesbian."
            scene expression ("images/episode5/231.webp") with dissolve
            katrina "Saya tertarik dengan vagina mereka, tetapi jika berpikir itu membuat ayam Anda sulit, lalu mengapa tidak."
            scene expression ("images/episode5/230.webp") with dissolve
            toby "Katakanlah aku percaya padamu."
        scene expression ("images/episode5/232.webp") with dissolve
        katrina "Saya akan membiarkan Anda kembali ke kencan Anda, tetapi jangan lupa tentang tawaran saya."
        toby "Tentu!"

    scene expression ("images/episode5/233.webp") with dissolve
    toby "Maaf tentang itu."
    if lisa_path:
        scene expression ("images/episode5/234_normal_3.webp") with dissolve
        lisa "Haruskah saya cemburu?"
        scene expression ("images/episode5/236_normal_1.webp") with dissolve
        if toby_job == 0:
            toby "Dia adalah pacar bos saya."
            scene expression ("images/episode5/235_flirty_3.webp") with dissolve
            lauren "Dia panas!"
        else:
            toby "Bos saya? Apakah Anda ingin cemburu?"
            scene expression ("images/episode5/235_flirty_1.webp") with dissolve
            lauren "Saya akan. Dia panas sekali."
        scene expression ("images/episode5/234_laugh_3.webp") with dissolve
        lisa "Jangan pedulikan dia. Dia hanya bodoh."
        if lauren_sidePath:
            scene expression ("images/episode5/236_laugh_2.webp") with dissolve
            toby "Anda tidak suka berbagi."
            scene expression ("images/episode5/235_flirty_3.webp") with dissolve
            lauren "Berbagi itu peduli."
            scene expression ("images/episode5/234_shy.webp") with dissolve
            lisa "Saya pikir kita harus pergi menari."
        else:
            scene expression ("images/episode5/236_normal_1.webp") with dissolve
            toby "Biarkan menari."
    else:
        scene expression ("images/episode5/235_flirty_3.webp") with dissolve
        lauren "Siapa wanita jalang yang seksi itu?"
        scene expression ("images/episode5/236_normal_2.webp") with dissolve
        if toby_job == 0:
            toby "Itu akan menjadi pacar bos saya."
            scene expression ("images/episode5/234_laugh_3.webp") with dissolve
            lisa "Dia cemburu."
            scene expression ("images/episode5/235_flirty_1.webp") with dissolve
            lauren "Nah ... aku berpikir tentang threesome."
        else:
            toby "Dia bosku."
            scene expression ("images/episode5/235_flirty_3.webp") with dissolve
            lauren "Haruskah saya cemburu?"
            scene expression ("images/episode5/236_laugh_2.webp") with dissolve
            toby "Aku harus menjadi yang cemburu. Dia seorang lesbian dan Anda agak panas untuknya."
            scene expression ("images/episode5/235_flirty_1.webp") with dissolve
            lauren "Sial ... Aku sudah bermimpi tentang threesome."

        scene expression ("images/episode5/234_laugh_2.webp") with dissolve
        lisa "[toby!c], bosnya dan pacarnya?"
        scene expression ("images/episode5/235_laugh_1.webp") with dissolve
        lauren "Anda benar -benar menyebalkan!"
        if lisa_sidePath:
            scene expression ("images/episode5/236_laugh_1.webp") with dissolve
            toby "Saya pikir dia bermaksud Anda, saya dan dia."
            scene expression ("images/episode5/235_flirty_3.webp") with dissolve
            lauren "Anda benar -benar jahat!"
            scene expression ("images/episode5/234_shy.webp") with dissolve
            lisa "Saya pikir kita harus pergi menari."
        else:
            scene expression ("images/episode5/236_laugh_2.webp") with dissolve
            toby "Saya pikir kita harus pergi menari."

    return


label episode5_sunday_clubAlone:
    $ progress = 73
    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/237.webp") with dissolve
    hide screen ui_message
    if toby_job == 0:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This city is so boring. I really need to make some friends.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And what better place to find people than the club. Maybe I should go to Katrina's club.{/i}"
        scene expression ("images/episode5/238.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I didn't know that her club was this cool.{/i}"
        scene expression ("images/episode5/239.webp") with dissolve
        katrina "Yah, yah, yah. Lihat apa yang diseret kucing itu."
        toby "Oh. Halo ma \ 'am."
        scene expression ("images/episode5/240.webp") with dissolve
        katrina "Biarkan saya menebak. Anda di sini untuk meminta saya untuk membawa Anda masuk?"
        scene expression ("images/episode5/241.webp") with dissolve
        toby "Saya tidak suka mengecewakan wanita cantik, tetapi sebenarnya saya sangat senang dengan pekerjaan Darlene."
        scene expression ("images/episode5/240.webp") with dissolve
        katrina "Anda membosankan. Lihatlah berapa banyak wanita cantik di sini dan Anda bekerja di sana dengan pacar pantat jelek saya."
        scene expression ("images/episode5/242.webp") with dissolve
        katrina "Misalnya dua wanita cantik itu."
        scene expression ("images/episode5/243.webp") with dissolve
        toby "Kotoran!"
        katrina "Anda tahu mereka?"
        toby "Apa yang bisa saya katakan, saya harus bertemu mereka di pekerjaan saya yang membosankan."
        scene expression ("images/episode5/244.webp") with dissolve
        katrina "Baik aku akan terkutuk. Lalu aku tidak akan mengganggumu. Aku akan membiarkanmu bersenang -senang."
    else:

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmm... It's almost 7PM. I guess I should go to work.{/i}"
        scene expression ("images/episode5/238.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I wonder what I'll have to do tonight.{/i}"
        scene expression ("images/episode5/239.webp") with dissolve
        katrina "Lihat siapa yang memutuskan untuk datang bekerja."
        toby "Saya \ m maafkan saya terlambat."
        scene expression ("images/episode5/240.webp") with dissolve
        katrina "Jangan khawatir, sayang. Anda di sini tepat pada waktunya. Pacar Anda baru saja tiba."
        scene expression ("images/episode5/241.webp") with dissolve
        toby "Pacar saya? Saya tidak punya."
        scene expression ("images/episode5/242.webp") with dissolve
        katrina "Keduanya telah melihat Anda sejak Anda masuk."
        toby "Kotoran."
        scene expression ("images/episode5/243.webp") with dissolve
        katrina "Apa yang kamu tunggu? Bicaralah dengan mereka."
        toby "Aku agak mengacaukannya."
        scene expression ("images/episode5/244.webp") with dissolve
        katrina "Baik dalam hal ini, saya akan membiarkan Anda mencari cara untuk menanganinya."

    scene expression ("images/episode5/245.webp") with dissolve
    if emma_break:


        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmmm... What should I do? Should I go over there and tell them the truth about Emma and that I wanted to end that the right way first before moving forward?{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Do I really want that. Have I really broken up with Emma for this?{/i}"
        menu:
            "{i} Bicaralah dengan Lisa {/i} [JLIRP]"(csq="Buka kembali jalur Lisa") if lisa_path == True:
                $ renpy.notify("Lisa's path has been reopened!")
                $ lisa_pathReopend = True
                return
            "{i} Bicaralah dengan Lauren {/i} [JLARP]"(csq="Buka kembali jalur Lauren") if lauren_path == True:
                $ renpy.notify("Lauren's path has been reopened!")
                $ lauren_pathReopened = True
                return
            "{i} tinggalkan mereka sendiri {/i} [JGV]"(csq="Tutup jalan selamanya"):
                $ renpy.notify("Lisa and Lauren's path have been closed!")
                $ lisa_path = False
                $ lauren_path = False
                pass


    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I don't really want to talk to them. I just want to enjoy a drink and maybe some dancing.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It's not like I owe them anything.{/i}"
    $ lisa_path = False
    $ lauren_path = False
    return


label episode5_sunday_club_lisa:
    scene expression ("images/episode5/246.webp") with dissolve
    toby "Hai, yang di sana. Bolehkah saya duduk, saya pikir kita harus bicara."
    scene expression ("images/episode5/247.webp") with dissolve
    lauren "Lihat [toby!c], Anda seorang pria yang keren, tetapi Lisa pantas mendapatkan seseorang yang lebih baik atau setidaknya lajang."
    scene expression ("images/episode5/246.webp") with dissolve
    toby "Dan Anda adalah teman yang baik, tetapi saya benar -benar ingin berbicara dengan Lisa saat ini."
    scene expression ("images/episode5/248.webp") with dissolve
    lisa "Bisakah Anda mengambil sesuatu untuk diminum?"
    lauren "Anda yakin?"
    lisa "Tentu saja."
    scene expression ("images/episode5/249.webp") with dissolve
    lauren "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Please don't be an ass.{/i}"
    toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Don't worry about me.{/i}"
    scene expression ("images/episode5/250_normal.webp") with dissolve
    toby "Pertama -tama saya ingin mengucapkan terima kasih telah mendengar saya."
    scene expression ("images/episode5/251_smile.webp") with dissolve
    lisa "Ini baik -baik saja. Ini tidak seperti Anda telah melakukan kesalahan. Saya mungkin telah meningkatkan hal -hal."
    scene expression ("images/episode5/250_normal.webp") with dissolve
    toby "Saya bingung. Saya pikir Anda marah pada saya."
    scene expression ("images/episode5/251_normal.webp") with dissolve
    lisa "Saya marah kepada Anda karena tidak memberi tahu saya bahwa Anda punya pacar, tetapi sungguh, itu tidak seperti saya memberi Anda kesempatan untuk memberi tahu saya."
    lisa "Saya adalah orang yang memulai ciuman pertama. Saya adalah orang yang mengajak Anda keluar."
    scene expression ("images/episode5/251_awkward.webp") with dissolve
    lisa "Dan saya terlalu marah ketika Anda mengatakan kepada saya bahwa Anda punya pacar. Lagipula itu tidak seperti kita bersama atau apapun. Anda tidak menipu saya [toby!c], jadi Anda tidak punya alasan untuk meminta maaf jika itu sebabnya Anda datang ke sini."
    scene expression ("images/episode5/250_smile.webp") with dissolve
    toby "Sebenarnya, saya ingin memberi tahu Anda sesuatu yang lain."
    scene expression ("images/episode5/250_normal.webp") with dissolve
    toby "Hubungan saya sudah agak pecah dan sekarang dengan jarak. Itu tidak berfungsi. Ketika Anda bertanya apakah saya punya pacar, saya benar -benar ingin mengatakan bahwa saya tidak, tetapi saya tidak ingin berbohong kepada Anda."
    toby "Masalahnya adalah bahwa beberapa hari terakhir ini, saya telah banyak memikirkan Anda."
    toby "Jadi itu benar -benar membuat saya banyak berpikir tentang perasaan saya."
    scene expression ("images/episode5/250_smile.webp") with dissolve
    toby "Alasan saya di sini adalah untuk memberi tahu Anda bahwa saya putus dengan pacar saya dan satu -satunya hal yang saya inginkan sekarang adalah untuk mengenal Anda lebih baik."
    scene expression ("images/episode5/251_shy.webp") with dissolve
    lisa "Aku merasa tidak enak karena membuatmu putus dengannya."
    scene expression ("images/episode5/250_smile.webp") with dissolve
    toby "Jangan merasa buruk. Seperti yang saya katakan, hubungan kami sudah cukup rusak. Masalahnya, saya tidak ingin Anda bergerak maju dengan Anda sebelum memperjelas hal -hal dalam hidup saya."
    scene expression ("images/episode5/251_normal.webp") with dissolve
    lisa "Saya harap Anda tidak mengharapkan saya sekarang untuk melompat pada Anda dan mencium Anda, kan?"
    scene expression ("images/episode5/250_laugh.webp") with dissolve
    toby "Nah ... ini dia mimpi itu."
    scene expression ("images/episode5/251_laugh.webp") with dissolve
    lisa "Anda seperti orang bodoh."
    scene expression ("images/episode5/250_smile.webp") with dissolve
    toby "Saya tidak mengharapkan apapun. Saya ingin sekali mengenal Anda lebih baik, tetapi jika Anda tidak menginginkan hal yang sama, itu baik -baik saja."
    scene expression ("images/episode5/250_laugh.webp") with dissolve
    toby "Sebenarnya itu tidak baik, tapi saya akan hidup."
    scene expression ("images/episode5/251_laugh.webp") with dissolve
    lisa "Terima kasih untuk ini."
    scene expression ("images/episode5/252.webp") with dissolve
    toby "Yah ... saya bilang kedamaian saya. Saya akan mendapatkan sesuatu untuk diminum. Saya harap Anda memiliki malam yang menyenangkan."
    lisa "Ya ... kamu juga."
    scene expression ("images/episode5/253.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/245.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}At least I said what was on my mind.{/i}"

    show screen ui_message("A few minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/254.webp") with dissolve
    hide screen ui_message
    lisa "Baik ... aku akan memintamu menari jika kamu menang."
    scene expression ("images/episode5/255.webp") with dissolve
    toby "Umm ... aku tidak berpikir kamu menerima."
    lisa "Nah, Lauren meminta saya untuk mengundang Anda untuk menari bersama kami."
    toby "Apakah dia sekarang."
    scene expression ("images/episode5/256.webp") with dissolve
    lisa "Anda tidak pernah tahu."
    return


label episode5_sunday_club_lauren:
    scene expression ("images/episode5/246.webp") with dissolve
    toby "Hai, yang di sana. Bolehkah saya duduk, saya pikir kita harus bicara."
    scene expression ("images/episode5/257.webp") with dissolve
    lauren "Tolong beri kami sesuatu untuk minum kami?"
    scene expression ("images/episode5/248.webp") with dissolve
    lisa "Jika Anda mau."

    scene expression ("images/episode5/258_arogant.webp") with dissolve
    lauren "Biarkan saya menebak. Anda ingin pergi ke kamar mandi dan membuat saya menghisap penis Anda?"
    scene expression ("images/episode5/259_laugh.webp") with dissolve
    toby "Siapa saya untuk mengatakan tidak pada sesuatu seperti itu."
    scene expression ("images/episode5/258_arogant.webp") with dissolve
    lauren "Tunggu aku di kamar mandi kalau begitu, tetapi jika aku tidak ada di sana dalam tiga jam itu berarti aku berubah pikiran."
    scene expression ("images/episode5/259_smile.webp") with dissolve
    toby "Sebelum itu. Saya ingin mengatakan bahwa saya menyesal saya tidak memberi tahu Anda sebelumnya bahwa saya punya pacar."
    scene expression ("images/episode5/258_laugh.webp") with dissolve
    lauren "Maksud Anda, Anda punya pacar yang tidak punya pacar."
    scene expression ("images/episode5/259_normal.webp") with dissolve
    toby "Punya pacar. Kami putus karena hubungan kami tidak lagi bekerja. Selain itu, bagaimana saya melanjutkan hubungan ketika yang bisa saya pikirkan hanyalah Anda."
    scene expression ("images/episode5/258_surprised.webp") with dissolve
    lauren "Tolong beritahu saya bahwa Anda berbohong."
    scene expression ("images/episode5/259_smile.webp") with dissolve
    toby "Aku tidak berbohong padamu saat itu, mengapa aku mulai sekarang?"
    scene expression ("images/episode5/258_arogant.webp") with dissolve
    lauren "Jadi kita bisa pergi ke kamar mandi?"
    scene expression ("images/episode5/259_laugh.webp") with dissolve
    toby "Saya tidak akan melakukan itu."
    scene expression ("images/episode5/259_normal.webp") with dissolve
    toby "Lihat. Aku sangat menginginkanmu. Anda pintar, panas, cantik, keterampilan mengisap Anda bukan yang terbaik, tetapi kami dapat mengerjakannya nanti."
    scene expression ("images/episode5/258_laugh.webp") with dissolve
    lauren "Ah, benarkah?"
    scene expression ("images/episode5/259_laugh.webp") with dissolve
    toby "Baik, baiklah. Anda hebat, tetapi saya tidak ingin berhubungan seks, saya ingin mengenal Anda lebih baik."
    scene expression ("images/episode5/258_shy.webp") with dissolve
    lauren "Anda benar -benar putus dengan pacar Anda?"
    scene expression ("images/episode5/259_normal.webp") with dissolve
    toby "Ya."
    scene expression ("images/episode5/258_shy.webp") with dissolve
    lauren "Dan Anda tidak mengatakan bahwa hanya untuk mengikuti saya, kan?"
    scene expression ("images/episode5/259_laugh.webp") with dissolve
    toby "Itu akan menjadi alasan yang cukup bagus, tetapi tidak. Saya tidak hanya mengatakan itu dan jika Anda mau, saya bisa membuktikannya kepada Anda."
    scene expression ("images/episode5/258_arogant.webp") with dissolve
    lauren "Bagaimana?"
    scene expression ("images/episode5/260.webp") with dissolve
    toby "Selamat malam Lauren."
    lauren "Jika Anda pergi, saya tidak akan mengejar Anda."
    toby "Nah, jangan sampai jika Anda datang, kami akan berhubungan seks malam ini dan bukan itu yang saya inginkan dari Anda sekarang."
    lauren "Apakah Anda benar -benar berpikir psikologi terbalik akan bekerja pada saya?"
    scene expression ("images/episode5/261.webp") with dissolve
    toby "Nikmati malam Anda."

    scene expression ("images/episode5/245.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/254.webp") with dissolve
    lisa "Apakah Anda benar -benar ingin membiarkan kami menari sendirian?"
    scene expression ("images/episode5/255.webp") with dissolve
    toby "Biarkan saya menebak ... dia mengirimmu?"
    scene expression ("images/episode5/256.webp") with dissolve
    lisa "Jangan membuat saya lebih dari roda ketiga daripada saya."

    return


label episode5_sunday_clubDance:
    $ progress = 74


    scene expression ("images/episode5/262.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/263.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/264.webp") with dissolve:
        xalign 0.0
        linear 10.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/265.webp") with dissolve:
        xalign 1.0
        linear 10.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/266.webp") with dissolve:
        yalign 1.0
        xalign 0.0
        linear 10.0 yalign 0.0 xalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/267.webp") with dissolve:
        yalign 0.0
        xalign 1.0
        linear 10.0 yalign 1.0 xalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/268.webp") with dissolve:
        yalign 0.0
        linear 10.0 yalign 1.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/269.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()


    if lisa_path:
        scene expression ("images/episode5/270.webp") with dissolve
        lauren "Saya akan mendapatkan sesuatu untuk diminum. Apakah Anda menginginkan sesuatu?"
        lisa "Tidak sayang. Saya baik-baik saja."
        toby "Ya, saya juga."
        scene expression ("images/episode5/271.webp") with dissolve
        lauren "Tentu saja Anda baik -baik saja. Jika Anda benar -benar haus, Anda hanya bisa bertukar ludah satu sama lain."
        scene expression ("images/episode5/272.webp") with dissolve
        lisa "Lalu, temukan dirimu seseorang untuk mencium juga."
        scene expression ("images/episode5/273.webp") with dissolve
        toby "Bye Lauren."
        scene expression ("images/episode5/274.webp") with dissolve
        lisa "Maaf untuk itu. Dia agak gila."
        toby "Mungkin, tapi idenya sebenarnya tidak terlalu buruk."
        lisa "Apakah Anda haus?"
        toby "Apakah kamu tidak?"
        scene expression ("images/episode5/275.webp") with dissolve
        lisa "Mengapa Anda bermain dengan saya?"

        show ep5_276 with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode5/276.webp") with dissolve
        hide ep5_276

        scene expression ("images/episode5/277.webp") with dissolve
        toby "Siapa yang bermain denganmu?"

        show ep5_278
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode5/278.webp")
        hide ep5_278

        scene expression ("images/episode5/279.webp") with dissolve
        if lauren_sidePath:
            lauren "Biarkan saya bergabung, kalian."
            scene expression ("images/episode5/280.webp")
            lisa "Temukan sendiri [toby!c]."
        else:
            lauren "Dapatkan kamar kalian berdua."
            scene expression ("images/episode5/280.webp")
            lisa "Saya sudah memiliki apartemen, tetapi saya membaginya dengan Anda."
            scene expression ("images/episode5/279.webp") with dissolve
            lauren "Baik, baiklah ... aku akan tidur di sofa."
            scene expression ("images/episode5/280.webp") with dissolve
            lisa "Idiot."
    else:

        scene expression ("images/episode5/281.webp") with dissolve
        lisa "Saya pergi ke kamar mandi. Cobalah untuk tidak membuat bayi sampai saya kembali!"
        scene expression ("images/episode5/282.webp") with dissolve
        lauren "Oke Bu!"
        scene expression ("images/episode5/283.webp") with dissolve
        toby "Saya suka idenya."
        lauren "Anda harus menunggu sampai kita pulang."
        toby "Jangan beri tahu saya bahwa Anda malu."
        scene expression ("images/episode5/284.webp") with dissolve
        lauren "Jangan menguji saya."

        show ep5_285 with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode5/285.webp") with dissolve
        hide ep5_285
        toby "Mari kita tegang untuk bermesraan saat ini."
        lauren "Itu hanya ciuman. Saya akan menunjukkan cara bercumbu jika Anda suka."

        show ep5_286
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode5/286.webp")
        hide ep5_286

        if lisa_sidePath:
            scene expression ("images/episode5/287.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode5/288.webp") with dissolve
            lauren "Seseorang menikmati pertunjukan."
            scene expression ("images/episode5/289.webp") with dissolve
            lisa "Saya sedang memeriksa untuk melihat apakah saya perlu menelepon pemadam kebakaran untuk mendinginkan kalian berdua."
        else:
            scene expression ("images/episode5/289.webp") with dissolve
            lisa "Kenakan beberapa kondom terlebih dahulu."
            scene expression ("images/episode5/288.webp") with dissolve
            lauren "Bisakah kamu membawakan kami satu?"
            toby "Jadikan dua."
            scene expression ("images/episode5/290.webp") with dissolve
            lisa "Kalian berdua berhak mendapatkan satu sama lain."

    return


label episode5_sunday_night_lisa:
    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()


    $ progress = 75


    scene expression ("images/episode5/291.webp") with dissolve
    hide screen ui_message
    lisa "Terima kasih untuk malam ini. Itu luar biasa."
    if lisa_pathReopend:
        toby "Terima kasih telah mendengar saya."
        lisa "Yah, saya mencoba untuk berdiri keras, tetapi Anda tahu cara menggunakan kata -kata Anda."
        toby "Ketika mereka datang dari hati, itu tidak sulit."
    else:
        toby "Saya harus berterima kasih. Saya harus menghabiskan waktu dengan wanita yang luar biasa."

    scene expression ("images/episode5/292.webp") with dissolve
    lisa "Apakah Anda mencoba membuat saya jatuh cinta pada Anda, [toby!c]?"
    toby "Apakah ini berhasil?"
    lisa "Mari kita katakan saya ingin melanjutkan percakapan ini di dalam."
    scene expression ("images/episode5/293.webp") with dissolve
    lauren "Baiklah aku akan membiarkan kalian berdua berbicara. Saya akan berada di dalam. Selamat malam [toby!c]."
    scene expression ("images/episode5/294.webp") with dissolve
    toby "Sebenarnya Anda tidak menyingkirkan saya dengan mudah."
    scene expression ("images/episode5/295.webp") with dissolve
    lisa "Saya mengundangnya."
    scene expression ("images/episode5/296.webp") with dissolve
    lauren "MHM ..."
    label memory_17:


        scene expression ("images/episode5/297.webp") with dissolve
        lisa "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}You're heading to the wrong room.{/i}"
        scene expression ("images/episode5/298.webp") with dissolve
        toby "Apakah saya di ruang yang tepat, sekarang?"
        lisa "Cium aku dan kamu akan mencari tahu."

        show ep5_299
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode5/299.webp")
        hide ep5_299


        toby "Ya ... Saya di ruang yang tepat."

        show ep5_299
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode5/299.webp")
        hide ep5_299

        show ep5_300
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode5/300.webp")
        hide ep5_300

        show ep5_301
        lisa "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\n{i}My nipples are so sensitive.{/i}"
        scene expression ("images/episode5/301.webp")
        hide ep5_301

        show ep5_302
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode5/302.webp")
        hide ep5_302

        show ep5_303
        $ ui.saybehavior()
        $ ui.interact()
        lisa "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\n{i}I want you [toby!c]. I want you so bad.{/i}"
        scene expression ("images/episode5/303.webp")
        hide ep5_303

        scene expression ("images/episode5/304.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode5/305.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode5/306.webp") with dissolve
        toby "Mari kita pergi ke tempat tidur."
        scene expression ("images/episode5/307.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        lisa "Anda \ 're {w} hanya {w} sempurna."
        scene expression ("images/episode5/308.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode5/309.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode5/310.webp") with dissolve
        lisa "Berhenti. Tolong, Berhenti. Saya tidak bisa melakukannya."
        lisa "Tolong jangan membenciku, tapi aku hanya bisa melakukannya sekarang."

        if lauren_sidePath:
            scene expression ("images/episode5/311.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()

        scene expression ("images/episode5/312.webp") with dissolve
        toby "Tidak ada tekanan. Setiap kali Anda siap, saya akan berada di sini untuk Anda."
        scene expression ("images/episode5/313.webp") with dissolve
        lisa "Anda tahu Anda hebat, bukan?"
        toby "Saya memiliki kekurangan, tetapi kebanyakan saya hebat."
        scene expression ("images/episode5/314.webp") with dissolve
        lisa "Beruntung Anda rendah hati."
        toby "Ya. Saya tidak tahan dengan orang -orang yang nakal."
        lisa "Saya tahu, benar!"
        scene expression ("images/episode5/315.webp") with dissolve
        toby "Ya Tuhan, kamu sangat cantik."
        scene expression ("images/episode5/316.webp") with dissolve
        lisa "Anda membuat saya memerah."
        scene expression ("images/episode5/315.webp") with dissolve
        toby "Mari kita menyalahkan alkohol."
        scene expression ("images/episode5/316.webp") with dissolve
        lisa "Saya berharap saya bisa ..."
        scene expression ("images/episode5/315.webp") with dissolve
        toby "Jangan khawatir. Tidak apa -apa, tidak ada yang terburu -buru untuk melakukan apa pun."

        show ep5_317 with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode5/318.webp")
        hide ep5_317

        lisa "Untuk apa itu?"
        toby "Karena seperti ini."
        scene expression ("images/episode5/319.webp") with dissolve
        lisa "Bahkan jika Anda tidak mendapatkan apa yang Anda inginkan?"
        toby "Tapi saya mendapatkan apa yang saya inginkan."
        scene expression ("images/episode5/318.webp") with dissolve
        toby "Aku ingin menciummu dan melihatmu tersenyum, jadi aku mendapatkan apa yang aku inginkan."
        lisa "Anda konyol."

        scene expression ("images/episode5/320.webp") with dissolve:
            xalign 0.0
            linear 10.0 xalign 1.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode5/321.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode5/322.webp") with dissolve:
            yalign 0.0
            xalign 0.0
            linear 10.0 yalign 1.0 xalign 1.0

        $ ui.saybehavior()
        $ ui.interact()

        $ unlockMemory(persistent.memory_17)
        $ renpy.end_replay()

    scene expression ("images/episode5/323.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/324.webp") with dissolve
    lauren "Sudah pergi?"
    scene expression ("images/episode5/325.webp") with dissolve
    toby "Nah, saya tidak bisa membiarkan Anda tidur di sofa."
    scene expression ("images/episode5/324.webp") with dissolve
    lauren "Anda tidak perlu khawatir tentang saya. Kami memiliki aturan, jika salah satu dari kami membawa seorang pria pulang yang lain tidur di sofa."
    scene expression ("images/episode5/325.webp") with dissolve
    toby "Dan apa yang terjadi jika Anda berdua pulang dengan seorang pria?"
    scene expression ("images/episode5/324.webp") with dissolve
    lauren "Dia mendapatkan kamar tidur dan saya mendapatkan ruang tamu dan dapur, karena saya lebih gila."

    if lauren_sidePath:
        scene expression ("images/episode5/326.webp") with dissolve
        lauren "Namun saya tidak yakin apa yang akan terjadi ketika kami berdua membawa pulang orang yang sama."
        scene expression ("images/episode5/325.webp") with dissolve
        toby "Siapa tahu, mungkin Anda akan mencari tahu suatu hari nanti."
        scene expression ("images/episode5/326.webp") with dissolve
        lauren "Saya bisa berharap begitu."

    scene expression ("images/episode5/327.webp") with dissolve
    toby "Selamat malam."
    lauren "Kamu juga."

    return

label episode5_sunday_night_lauren:
    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    $ progress = 75


    scene expression ("images/episode5/328.webp") with dissolve
    hide screen ui_message
    lauren "Ingin masuk?"
    toby "Nah, jika Anda bersikeras. Bagaimana saya bisa menolak wanita cantik seperti Anda."
    lauren "Ya, saya hampir harus memohon."
    scene expression ("images/episode5/329.webp") with dissolve
    toby "Saya suka sarkasme Anda, tetapi saya benar -benar perlu melihat Anda menginginkan saya di dalam."
    lauren "Oh, aku menginginkanmu di dalam."
    lauren "Di dalam diriku."
    scene expression ("images/episode5/330.webp") with dissolve
    lauren "Sayang, jika aku jadi kamu, aku akan menggunakan headphone."
    scene expression ("images/episode5/331.webp") with dissolve
    lisa ". {w}. {w}."
    lisa "Selamat bersenang-senang."

    label memory_18:


        scene expression ("images/episode5/332.webp") with dissolve
        if ep3_lieGirls == True:
            lauren "Anda tahu [toby!c]? Saya bukan orang yang menyesali sesuatu, tetapi saya memiliki satu penyesalan."
            toby "Dan itu?"
            lauren "Fakta bahwa saya tidak membiarkan Anda bercinta dengan saya di pantai. Saya terangsang sepanjang minggu setelah itu."
        else:
            lauren "Anda tahu [toby!c]? Saya senang Anda putus dengan pacar Anda. Aku akan merasa tidak enak karena menidurimu saat kamu dalam suatu hubungan."
            toby "Ketika saya memberi tahu Anda bahwa saya punya pacar, Anda sangat kesal."
            lauren "Mungkin, tapi saya terangsang sepanjang minggu, jadi cepat atau lambat saya akan menelepon."

        toby "Kita bisa memperbaiki bagian terangsang."
        scene expression ("images/episode5/333.webp") with dissolve
        lauren "Oh, percayalah. Kami."

        scene expression ("images/episode5/334.webp") with dissolve:
            yalign 1.0
            linear 10.0 yalign 0.0

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        scene expression ("images/episode5/335.webp") with dissolve
        lauren "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Pull down your pants, because I can't hold it anymore.{/i}"
        lauren "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I promise you that next time I'll be more romantic and stuff, but tonight I want you to fuck me.{/i}"
        toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}You want me to fuck you like a whore?{/i}"
        lauren "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Tonight I'm your whore.{/i}"

        show ep5_336
        lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck... You're so big."
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode5/336.webp")
        hide ep5_336

        show ep5_337
        lauren "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nRight there."
        lauren "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nYes... {w}yes... {w}YES."
        scene expression ("images/episode5/337.webp")
        hide ep5_337

        show ep5_338
        $ ui.saybehavior()
        $ ui.interact()
        lauren "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nDon't stop. Don't you dare stop."
        scene expression ("images/episode5/338.webp")
        hide ep5_338

        show ep5_339

        lauren "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck me."
        lauren "{size=12}{color=#FDCA6E}* yelling *{/color}{/size}\nFuck your whore."
        scene expression ("images/episode5/339.webp")
        hide ep5_339

        if lisa_sidePath:
            scene expression ("images/episode5/340.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is Lisa spying on us?{/i}"
        toby "Saya akan pergi ke cum."
        scene expression ("images/episode5/341.webp") with dissolve
        lauren "Datanglah ke dalam Aku. Saya sedang minum pil."

        if lisa_sidePath:
            scene expression ("images/episode5/342.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yup... Look at me. {/i}"
        else:
            scene expression ("images/episode5/344.webp") with dissolve

        with flash
        with flash
        $ ui.saybehavior()
        $ ui.interact()
        if lisa_sidePath:
            scene expression ("images/episode5/343.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She must have panicked.{/i}"
        else:
            scene expression ("images/episode5/345.webp") with dissolve

        lauren "Sial ... itu sangat bagus."
        scene expression ("images/episode5/346.webp") with dissolve
        toby "Saya sangat membutuhkannya."
        lauren "Ya, saya juga."

        scene expression ("images/episode5/347.webp") with dissolve:
            xalign 1.0
            linear 10.0 xalign 0.0

        toby "Saya pikir saya harus pergi. Saya merasa tidak enak untuk membuat Lisa tidur di sofa."
        lauren "Ya. Saya juga. Meskipun kami membuat aturan bahwa jika salah satu dari kami pulang dengan seseorang, yang lain tidur di sofa, tetapi kami baru saja pindah ke sini beberapa hari yang lalu dan dia sudah harus tidur di sofa."

        scene expression ("images/episode5/348.webp") with dissolve:
            xalign 1.0
            yalign 0.0
            linear 10.0 xalign 0.0 yalign 0.8

        toby "Dia tidak tahu apa pelacur itu."
        lauren "Ups."

        $ unlockMemory(persistent.memory_18)
        $ renpy.end_replay()

    scene expression ("images/episode5/349.webp") with dissolve
    lauren "Maaf jika kami terlalu keras."
    scene expression ("images/episode5/350.webp") with dissolve
    lisa "Jangan khawatir, saya yakin Anda bisa lebih keras dari itu."
    scene expression ("images/episode5/349.webp") with dissolve
    lauren "Ketika Anda memiliki seseorang yang bercinta dengan Anda, Anda tidak dapat melakukan hal lain selain berteriak."
    scene expression ("images/episode5/351.webp") with dissolve
    toby "Saya pikir saya harus pergi."
    scene expression ("images/episode5/350.webp") with dissolve
    lisa "Bye [toby!c]."
    scene expression ("images/episode5/352.webp") with dissolve
    toby "Bye Lisa."
    scene expression ("images/episode5/353.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Bye sexy.{/i}"
    lauren "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Bye sexy! Thank you for tonight.{/i}"
    lauren "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}It was perfect.{/i}"

    return

label episode5_sunday_night:
    $ progress = 76
    stop music fadeout 1.0
    scene expression ("images/episode5/354.webp") with fade
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm so beat.{/i}"
    if lisa_path == True:


        scene expression ("images/episode5/355.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It looks like I got a message from Lisa.{/i}"
        scene expression ("images/episode5/355_texting.webp") with dissolve
        call sms_incoming ("lisa", "Hey. Sorry that I fell asleep.") from _call_sms_incoming_52
        call sms_sent ("lisa", "No problem darling. It's fine.") from _call_sms_sent_34
        call sms_incoming ("lisa", "You didn't had to leave by the way.") from _call_sms_incoming_53
        call sms_sent ("lisa", "Lauren told me about your deal.") from _call_sms_sent_35
        call sms_incoming ("lisa", "Yeah... Anyway, thank you for being so understanding.") from _call_sms_incoming_54
        call sms_incoming ("lisa", "I mean about tonight.") from _call_sms_incoming_55
        call sms_sent ("lisa", "Sure, no problem.") from _call_sms_sent_36
        $ unlockImage(persistent.lisa_08)
        call sms_incoming ("lisa", "Good night dear.", img_icon="images/episode5/356_icon.webp", img="images/episode5/356.webp") from _call_sms_incoming_56
        call sms_sent ("lisa", "Good night!") from _call_sms_sent_38
    elif lauren_path == True:

        scene expression ("images/episode5/355.webp") with dissolve
        if lisa_sidePath == True:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It looks like I've got a message from Lauren and one from Lisa.{/i}"
        else:
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It looks like I got a message from Lauren.{/i}"

        scene expression ("images/episode5/355_texting.webp") with dissolve
        $ unlockImage(persistent.lauren_08)
        call sms_incoming ("lauren", "Your cock was so big that my pussy hurts. We'll need to stretch this baby.", img_icon="images/episode5/357_icon.webp", img="images/episode5/357.webp") from _call_sms_incoming_57
        call sms_sent ("lauren", "It will be my pleasure.") from _call_sms_sent_39
        call sms_incoming ("lauren", "Of course it will be your pleasure. I mean, have you seen how I look naked?") from _call_sms_incoming_58
        call sms_sent ("lauren", "Sorry. I didn't. I was thinking about old ladies with hairy pussy so I didn't cum too fast.") from _call_sms_sent_40
        call sms_incoming ("lauren", "Ouch... That hurt. You were thinking about someone else when you were pumping me?") from _call_sms_incoming_59
        call sms_sent ("lauren", "I'm kidding, but now that I think about it, I think it could work.") from _call_sms_sent_41
        call sms_incoming ("lauren", "Well, if that's your thing. I'll let my pubic hair grow and maybe I could even paint some wrinkles on my ass.") from _call_sms_incoming_60
        call sms_sent ("lauren", "Don't worry, I have a really good imagination.") from _call_sms_sent_42
        call sms_incoming ("lauren", "LOL... You're crazy.") from _call_sms_incoming_61
        call sms_incoming ("lauren", "Anyway... Have a good night sexy.") from _call_sms_incoming_62
        call sms_sent ("lauren", "Yeah, you too!") from _call_sms_sent_43

        if lisa_sidePath:
            hide screen message
            scene expression ("images/episode5/355.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see what Lisa wants.{/i}"
            scene expression ("images/episode5/355_texting.webp") with dissolve
            call sms_incoming ("lisa", "Just so you know, I'm not a perv.") from _call_sms_incoming_63
            call sms_sent ("lisa", "Of course not. I mean a perv would look at her friend getting fucked, but you didn't.") from _call_sms_sent_44
            call sms_incoming ("lisa", "I just wanted to make sure she was ok, she was surprisingly loud.") from _call_sms_incoming_64
            call sms_sent ("lisa", "She's so lucky to have you.") from _call_sms_sent_45
            call sms_sent ("lisa", "At least you enjoyed the show?") from _call_sms_sent_46
            call sms_incoming ("lisa", "Have a good night!", img_icon="images/episode5/358_icon.webp", img="Images/episode5/358.webp") from _call_sms_incoming_65
    hide screen message
    return

label episode5_monday_morning:
    $ progress = 78

    show screen ui_message("Monday") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/359.webp") with fade
    hide screen ui_message
    $ ui.saybehavior()
    $ ui.interact()
    if toby_job == 0:
        scene expression ("images/episode5/360.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Looks like I got a new message from Mrs. Darlene.{/i}"
        scene expression ("images/episode5/360_texting.webp") with dissolve
        call sms_incoming ("darlene", "Good morning. Please come by the office around 2PM. I need your help with some papers.") from _call_sms_incoming_66
        call sms_sent ("darlene", "Sure thing. I'll be there.") from _call_sms_sent_47
        call sms_incoming ("darlene", "Thank you dear.") from _call_sms_incoming_67
        hide screen message

    scene expression ("images/episode5/361.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmm... What should I do today?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'll get something to eat first, then I think I better start watching some construction videos on the internet because I really don't wanna lose that bet.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Besides, we really need to do something about the attic and the yard.{/i}"
    if toby_job == 0:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And then I'll go to work.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And then maybe I'll hit the gym.{/i}"

    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/362.webp") with dissolve
    hide screen ui_message

    if toby_job == 0:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit. It's already 12:30 and I learned nothing about construction. I need to take a shower and get to work.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm so beat. I need to take a shower and then hit the gym.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Who knew construction was so complicated?{/i}"

    scene expression ("images/episode5/363.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/364.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/365.webp") with dissolve
    patricia "Oh. Kotoran. Maaf [bro], saya tidak berharap untuk menangkap Anda berpakaian."
    scene expression ("images/episode5/366.webp") with dissolve
    toby "Apakah kita akan membiasakan ini?"
    scene expression ("images/episode5/367.webp") with dissolve
    patricia "Sepertinya begitu."
    patricia "I really don't want to sound like a bitch. Usually I'm just teasing you with \"this is my room\", tapi bisakah Anda pergi sehingga saya bisa berubah."
    scene expression ("images/episode5/366.webp") with dissolve
    toby "Anda tidak ingin terdengar seperti wanita jalang, namun Anda melakukannya."
    scene expression ("images/episode5/367.webp") with dissolve
    patricia "Saya membawa pulang Bea sehingga kami dapat mengerjakan pekerjaan rumah dan mungkin menonton beberapa film dan saat ini dia berbicara dengan [mom] dan Anda tidak pernah tahu kapan dia akan mulai berbicara tentang hal -hal bodoh."
    patricia "Seperti Anda dan saya tidur di tempat tidur yang sama dan siapa yang tahu hal -hal bodoh apa lagi yang dia bawa."
    patricia "Atau lebih buruk. Tanyakan padanya tentang anak laki -laki di sekolah saya."
    scene expression ("images/episode5/369.webp") with dissolve
    toby "Oke mari kita menjadi pintar tentang ini. Jika saya meninggalkan ruangan yang sama, Anda baru saja masuk hanya mengenakan handuk, itu akan terlihat mencurigakan."
    toby "Jadi dia akan mengetahui bahwa kita membagikannya."
    scene expression ("images/episode5/368.webp") with dissolve
    patricia "Ya..."
    scene expression ("images/episode5/366.webp") with dissolve
    toby "Ngomong -ngomong, pada titik ini, sampai saya menyelesaikan loteng saya, kami akan tersandung satu sama lain telanjang atau dalam situasi canggung beberapa kali lagi."
    scene expression ("images/episode5/367.webp") with dissolve
    patricia "Maksudmu, aku akan tersandung padamu saat kamu mengirim foto kontol?"
    scene expression ("images/episode5/369.webp") with dissolve
    toby "Maksudku, pada titik ini kita bisa menjadi orang dewasa dan berpaling, tutup mata kita dan sebagainya. Dengan cara ini kita mungkin akan menghindari situasi yang canggung."
    toby "Jika Anda datang ke kamar dan saya berubah, lihat saja sampai saya selesai dan tidak ada salahnya tidak melakukan pelanggaran."
    scene expression ("images/episode5/367.webp") with dissolve
    patricia "Dan Anda akan melakukan hal yang sama?"
    scene expression ("images/episode5/370.webp") with dissolve
    toby "Nah, itulah idenya. Aku akan mengabaikanmu."
    scene expression ("images/episode5/371.webp") with dissolve
    patricia "Ya, tapi saya seksi. Bisakah Anda berpaling dari ini?"
    scene expression ("images/episode5/369.webp") with dissolve
    toby "Saya akan melakukan yang terbaik."
    scene expression ("images/episode5/367.webp") with dissolve
    patricia "Oke, tapi jika saya pernah menangkap Anda mengintip saya, saya menendang bola Anda."
    scene expression ("images/episode5/369.webp") with dissolve
    toby "Dan aku akan memberimu pukulan."
    scene expression ("images/episode5/372.webp") with dissolve
    patricia "Anda mendapatkan kesepakatan. Sekarang cepat dan berpakaian, karena kita tidak bisa meninggalkan ruangan secara bersamaan."
    toby "Hanya jangan membuatku memukulmu!"
    patricia "Betapa menggoda yang mungkin terdengar, saya akan mencoba untuk tidak melihat."
    scene expression ("images/episode5/373.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/374.webp") with dissolve
    patricia "Ngomong -ngomong, saya juga berubah, jadi ketika Anda berbalik, jauhkan kepala Anda."
    scene expression ("images/episode5/375.webp") with dissolve
    toby "Saya akan menahan mereka."
    scene expression ("images/episode5/376.webp") with dissolve
    patricia "Jamak? Berapa banyak kepala yang Anda miliki?"
    scene expression ("images/episode5/377.webp") with dissolve
    toby "Sampai jumpa nanti malam."

    scene expression ("images/episode5/378.webp") with dissolve
    toby "Hai Bea!"
    scene expression ("images/episode5/379.webp") with dissolve
    beatrice "Hai [toby!c]. Bagaimana Anda menyukai es krim saya?"
    scene expression ("images/episode5/380.webp") with dissolve
    toby "Itu yang terbaik. Saya akan memastikan untuk mengunjungi truk Anda Sabtu depan."
    scene expression ("images/episode5/381.webp") with dissolve
    beatrice "Saudaraku seharusnya mengambil truk itu akhir pekan ini, tetapi karena kamu ingin mengunjungi aku, aku akan pastikan untuk berada di sana."
    scene expression ("images/episode5/382.webp") with dissolve
    toby "Terima kasih!"
    scene expression ("images/episode5/383.webp") with dissolve
    charlotte "Kemana kamu pergi?"
    scene expression ("images/episode5/384.webp") with dissolve
    if toby_job == 0:
        toby "Untuk bekerja!"
    else:
        toby "Ke gym. Saya membutuhkan setiap otot jika saya akan merenovasi rumah."
    toby "Sampai jumpa lagi."
    scene expression ("images/episode5/385.webp") with dissolve
    charlotte "Selamat tinggal sayang."
    scene expression ("images/episode5/386.webp") with dissolve
    beatrice "Bye [toby!c]."

    return

label episode5_monday_evening:
    $ progress = 79


    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/387.webp") with dissolve
    hide screen ui_message
    toby "Heya. Bagaimana kabarmu?"
    scene expression ("images/episode5/388.webp") with dissolve
    beatrice "Hai [toby!c]."
    patricia "Anda sudah kembali?"
    scene expression ("images/episode5/389.webp") with dissolve
    toby "Aku terluka! Saya sangat berharap Anda merindukan saya."
    scene expression ("images/episode5/390.webp") with dissolve
    patricia "Saya tidak. Apakah Anda?"
    scene expression ("images/episode5/391.webp") with dissolve
    if toby_job == 0:
        beatrice "Umm ... bagaimana kerjanya?"
    else:
        beatrice "Umm ... bagaimana gymnya?"
    scene expression ("images/episode5/392.webp") with dissolve
    toby "Itu sebenarnya bagus."
    scene expression ("images/episode5/393.webp") with dissolve
    toby "Apa yang kita tonton?"
    scene expression ("images/episode5/394.webp") with dissolve
    patricia "Beberapa romansa, tetapi kami berdua tahu bahwa Anda tidak menyukai film semacam ini."
    scene expression ("images/episode5/395.webp") with dissolve
    beatrice "Mungkin Anda akan menyukai yang ini. Ingin bergabung?"
    scene expression ("images/episode5/392.webp") with dissolve
    toby "Terima kasih, tapi saya harus menolak. Mungkin lain kali kita akan menonton sesuatu dengan lebih banyak aksi."
    scene expression ("images/episode5/396.webp") with dissolve
    patricia "Apakah Anda yakin ingin lebih banyak tindakan? Maksud saya, Anda tidak menangani tindakan terlalu bagus."
    scene expression ("images/episode5/397.webp") with dissolve
    beatrice "Apakah Anda takut?"
    scene expression ("images/episode5/398.webp") with dissolve
    toby "Tidak, saya tidak. Saya tidak tahu apa yang dia bicarakan."
    scene expression ("images/episode5/399.webp") with dissolve
    pause 1.0
    scene expression ("images/episode5/400.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Oh, I know what you meant. I'll get you for that.{/i}"
    patricia "Ya ... lelucon saya bukan untuk semua orang."
    scene expression ("images/episode5/401.webp") with dissolve
    toby "Saya akan membiarkan Anda menikmati film Anda. Lihat ya!"

    scene expression ("images/episode5/402.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode5/403.webp") with dissolve
    toby "Hai [mom]. Apa kabarmu?"

    if toby_job == 0:
        scene expression ("images/episode5/404.webp") with dissolve
        charlotte "Oh. Hai [toby!c]. Sudah kembali ke rumah?"
        scene expression ("images/episode5/405.webp") with dissolve
        toby "Ya. Saya hanya perlu membantu Ny. Darlene dengan beberapa kertas, jadi tidak terlalu lama."
    else:
        scene expression ("images/episode5/404.webp") with dissolve
        charlotte "Oh. Hai [toby!c]. Anda tinggal sebentar di gym hari ini."
        scene expression ("images/episode5/405.webp") with dissolve
        toby "Ya. Saya mulai dengan cardio dan kemudian melakukan kembali dan bisep. Jadi itu adalah sesi yang panjang."
    toby "Bagaimanapun. Temukan ide untuk halaman?"
    scene expression ("images/episode5/406.webp") with dissolve
    charlotte "Saya berhenti mencari hal -hal untuk halaman karena Anda ingin mengurusnya, saya membiarkan Anda menjadi gila."

    scene expression ("images/episode5/407_normal.webp") with dissolve
    charlotte "Speaking of crazy. Sorry about our so called \"date\"."
    scene expression ("images/episode5/408_curious.webp") with dissolve
    toby "Tidak yakin saya tahu maksud Anda."
    scene expression ("images/episode5/407_awkward.webp") with dissolve
    charlotte "Semua hal buruk yang kami katakan, godaan yang tidak bersalah. Saya memiliki seorang suami dan lebih dari itu saya [mother] Anda."
    scene expression ("images/episode5/408_warm.webp") with dissolve
    toby "Lihat [mom], Anda tidak perlu meminta maaf. Sangat menyenangkan melihat Anda tersenyum untuk perubahan dan selain itu tidak seperti kami melintasi batas apa pun."
    toby "Anda tetap saja saya [mom] dan tidak ada yang akan mengubahnya. Aku mencintaimu dan aku mengerti bahwa kamu perlu melarikan diri."
    scene expression ("images/episode5/407_smile.webp") with dissolve
    charlotte "Saya senang Anda melihat hal -hal seperti itu, karena saya merasa sangat baik."
    charlotte "Anda telah tumbuh dengan sangat baik. Saya senang Anda sangat dewasa."
    scene expression ("images/episode5/408_laugh.webp") with dissolve
    toby "Anda tahu apa yang mereka katakan. Seperti [mother] seperti [son]."
    scene expression ("images/episode5/407_flirty.webp") with dissolve
    charlotte "Maksudmu aku sudah dewasa dengan baik?"
    scene expression ("images/episode5/408_flirty.webp") with dissolve
    toby "Oh, Anda sudah dewasa."
    scene expression ("images/episode5/407_laugh.webp") with dissolve
    charlotte "[toby!c] ... apakah Anda menggoda dengan [mother] Anda?"
    scene expression ("images/episode5/408_laugh.webp") with dissolve
    toby "Apa yang bisa saya katakan, sebelum menjadi [son] saya seorang pria. Dan sangat sulit bagi seorang pria untuk tidak menggoda dengan makhluk yang begitu cantik."
    scene expression ("images/episode5/407_laugh.webp") with dissolve
    charlotte "Makhluk cantik? Saya pikir makhluk itu adalah hal -hal yang menyembuhkan."
    scene expression ("images/episode5/408_smile.webp") with dissolve
    toby "Anda mengambil sesuatu secara harfiah."
    scene expression ("images/episode5/407_smile.webp") with dissolve
    charlotte "Apa yang bisa saya katakan. Ada banyak hal yang perlu saya pelajari tentang generasi muda ini."
    scene expression ("images/episode5/408_laugh.webp") with dissolve
    toby "Oh tolong ... tidak seperti kamu tua."
    scene expression ("images/episode5/407_laugh.webp") with dissolve
    charlotte "Ya, saya masih ingat ketika guru Anda bertanya mengapa [sister] Anda pergi ke pertemuan [parents]."
    scene expression ("images/episode5/408_warm.webp") with dissolve
    toby "Sekarang Anda hanya menyombongkan diri."
    scene expression ("images/episode5/407_smile.webp") with dissolve
    charlotte "Bisakah seorang wanita merasa muda dan cantik?"
    scene expression ("images/episode5/408_curious.webp") with dissolve
    toby "Apakah saya mengatakan Anda cantik? Saya hanya ingat mengatakan Anda masih muda."
    scene expression ("images/episode5/407_laugh.webp") with dissolve
    charlotte "Saya selalu merasa cantik. Bagian usia adalah tempat saya memiliki masalah."
    scene expression ("images/episode5/408_smile.webp") with dissolve
    toby "Sepertinya Anda memiliki masalah pada bagian kesederhanaan juga."
    scene expression ("images/episode5/407_laugh.webp") with dissolve
    if ep4_nightWithCharlotte:
        charlotte "Jika saya memiliki masalah dengan itu semua salah Anda. Anda yang membuat saya merasa cantik dan seksi."
    else:
        charlotte "Bisa aja. Ini tidak seperti pikiran Anda."
    scene expression ("images/episode5/408_laugh.webp") with dissolve
    toby "Bagus. Bagus. Kamu menang."
    scene expression ("images/episode5/409.webp") with dissolve
    toby "Ngomong -ngomong, apa yang kamu tulis?"
    scene expression ("images/episode5/410.webp") with dissolve
    charlotte "Tidak ada ... aku hanya bermain -main."
    scene expression ("images/episode5/408_curious.webp") with dissolve
    toby "Anda bermain -main ketika Anda menulis 2 paragraf bukan 10 halaman atau apa pun yang Anda miliki di sana. Sepertinya banyak."
    scene expression ("images/episode5/407_shy.webp") with dissolve
    charlotte "Ini adalah hobi lama saya."
    scene expression ("images/episode5/408_warm.webp") with dissolve
    toby "Sekarang saya tertarik."
    scene expression ("images/episode5/407_awkward.webp") with dissolve
    charlotte "Nah, ketika saya seusia Anda, saya masih kuliah, tidak seperti orang lain yang saya kenal."
    scene expression ("images/episode5/408_laugh.webp") with dissolve
    toby "Sudah kubilang. Saya masih berpikir untuk kuliah, tetapi saya tidak menemukan apa pun yang ingin saya lakukan sepanjang hidup saya."
    scene expression ("images/episode5/407_normal.webp") with dissolve
    charlotte "Kaum muda. Anda semua sama."
    scene expression ("images/episode5/408_normal.webp") with dissolve
    toby "Anda berbicara tentang saat Anda masih kuliah ..."
    scene expression ("images/episode5/407_laugh.webp") with dissolve
    charlotte "Baik, baiklah. Kembali ketika saya masih kuliah, saya mendapat penghargaan untuk esai terbaik. Itu adalah kontes yang diadakan antara 10 perguruan tinggi."
    scene expression ("images/episode5/408_surprised.webp") with dissolve
    toby "Itu sangat keren."
    scene expression ("images/episode5/407_smile.webp") with dissolve
    charlotte "Bagian yang keren adalah fakta bahwa seiring dengan penghargaan itu datang hadiah 10k."
    scene expression ("images/episode5/408_curious.webp") with dissolve
    toby "Jika Anda sebagus itu, mengapa Anda tidak menulis buku atau semacamnya."
    scene expression ("images/episode5/407_sad.webp") with dissolve
    charlotte "Saya melakukannya, tetapi setiap kali saya membacanya, saya terus menemukan hal lain yang perlu diubah."
    charlotte "Sampai saya benar -benar membakar segalanya."
    scene expression ("images/episode5/408_curious.webp") with dissolve
    toby "Biarkan saya meluruskan ini. Setelah menghabiskan berjam -jam menulis buku, dengan tangan, Anda memutuskan untuk membakar semuanya, tanpa cara mendapatkannya kembali?"
    scene expression ("images/episode5/407_arogant.webp") with dissolve
    charlotte "Itu merangkumnya, tetapi untuk informasi Anda, saya adalah salah satu anak yang keren. Saya punya mesin tik."
    scene expression ("images/episode5/408_laugh.webp") with dissolve
    toby "Oh, maafkan aku, Mrs. Typewriter."
    scene expression ("images/episode5/408_curious.webp") with dissolve
    toby "Ngomong -ngomong, jadi itu berarti hal yang Anda sembunyikan di laptop adalah buku Anda berikutnya yang mungkin?"
    scene expression ("images/episode5/407_smile.webp") with dissolve
    charlotte "Jangan sampai pada diri kita sendiri. Saya hanya menulis dan kemudian mempostingnya di suatu tempat di internet."
    scene expression ("images/episode5/408_smile.webp") with dissolve
    toby "Kapan itu akan dilakukan?"
    scene expression ("images/episode5/407_normal.webp") with dissolve
    charlotte "Itu tidak penting. Saya tidak akan membiarkan Anda membacanya."
    scene expression ("images/episode5/408_curious.webp") with dissolve
    toby "Jadi erotika?"
    scene expression ("images/episode5/407_laugh.webp") with dissolve
    charlotte "Tidak, itu bukan erotika. Ini romansa, tanpa konten eksplisit. Tapi bukan itu sebabnya aku tidak membiarkanmu membacanya."
    scene expression ("images/episode5/407_smile.webp") with dissolve
    charlotte "Saya tidak berpikir itu akan baik dan karena Anda sangat berpikir saya tidak ingin mengubah pikiran Anda."
    scene expression ("images/episode5/408_smile.webp") with dissolve
    toby "Tetapi bagaimana jika itu akan lebih baik dari yang saya harapkan?"
    scene expression ("images/episode5/407_normal.webp") with dissolve
    charlotte "Maksud Anda, Anda mengharapkan saya untuk menulis omong kosong?"
    scene expression ("images/episode5/408_laugh.webp") with dissolve
    toby "Mungkin."
    scene expression ("images/episode5/407_smile.webp") with dissolve
    charlotte "Maka Anda tidak pantas membaca karya seni saya."
    scene expression ("images/episode5/408_laugh.webp") with dissolve
    toby "Tidak ada skenario di mana saya memenangkan ini, kan?"
    scene expression ("images/episode5/407_flirty.webp") with dissolve
    charlotte "Bukan satu pun."
    scene expression ("images/episode5/408_flirty.webp") with dissolve
    toby "Lalu aku akan mengikatmu ke tempat tidur dan aku akan mencuri komputermu."
    scene expression ("images/episode5/407_laugh.webp") with dissolve
    charlotte "Itu dilindungi kata sandi."
    scene expression ("images/episode5/408_laugh.webp") with dissolve
    toby "Saya suka bagaimana Anda tidak mengeluh tentang saya mengikat Anda ke tempat tidur."
    scene expression ("images/episode5/407_arogant.webp") with dissolve
    charlotte "Anda tidak akan pernah bisa melakukan itu pada [mother] Anda, jadi saya tidak takut."
    scene expression ("images/episode5/408_laugh.webp") with dissolve
    toby "Maka Anda harus memasukkan kata sandi yang lebih baik di komputer Anda."
    scene expression ("images/episode5/407_surprised.webp") with dissolve
    charlotte "Anda tahu kata sandi saya?"
    scene expression ("images/episode5/408_laugh.webp") with dissolve
    toby "Ini ulang tahun Tris."
    scene expression ("images/episode5/407_arogant.webp") with dissolve
    charlotte "Tidak lagi. Saya mengubahnya."
    scene expression ("images/episode5/408_laugh.webp") with dissolve
    toby "Lalu itu ulang tahunku."
    scene expression ("images/episode5/407_normal.webp") with dissolve
    charlotte "Bagus. Saya akan mengubah kata sandi."
    $ progress = 80
    scene expression ("images/episode5/411.webp") with dissolve
    patricia "Hei [bro] Bisakah Anda membawa pulang Bea? Sudah terlambat baginya untuk berjalan."
    scene expression ("images/episode5/412.webp") with dissolve
    charlotte "Anda bisa mengambil mobil kami, sayang."
    scene expression ("images/episode5/413.webp") with dissolve
    patricia "Saya pikir [dad] pergi dengan mobil."
    scene expression ("images/episode5/412.webp") with dissolve
    charlotte "Tidak. Seseorang menjemputnya."
    if beatrice_path:
        scene expression ("images/episode5/413.webp") with dissolve
        patricia "Tapi aku juga hanya pernah mengemudi dengan kalian di mobil juga."
        scene expression ("images/episode5/414.webp") with dissolve
        menu:
            "{i} [JGR] Bawa pulang {/i}":
                toby "Bagus. Aku akan membawanya pulang."
                return
            "{i} don \ 't lakukan {/i} [JWRN6]"(csq="Tutup jalur Beatrice"):
                $ renpy.notify("Beatrice's path has been closed!")
                $ beatrice_path = False
                toby "Saya tidak ingin membawanya. Dia temanmu."
    scene expression ("images/episode5/412.webp") with dissolve
    charlotte "Ambil mobil, cepat atau lambat Anda harus belajar mengemudi sendiri."
    scene expression ("images/episode5/413.webp") with dissolve
    patricia "Jadi Anda mempercayai keterampilan mengemudi saya?"
    scene expression ("images/episode5/412.webp") with dissolve
    charlotte "Saya mempercayai asuransi kami."
    scene expression ("images/episode5/415.webp") with dissolve
    patricia "Aduh. Itu menyakitkan."
    scene expression ("images/episode5/412.webp") with dissolve
    charlotte "Berkendara aman."
    scene expression ("images/episode5/416_1.webp") with dissolve
    toby "Bagaimanapun, saya harus pergi ke kamar saya."
    scene expression ("images/episode5/416_2.webp") with dissolve
    charlotte "Terima kasih telah datang mengunjungi saya."
    scene expression ("images/episode5/416_1.webp") with dissolve
    toby "Jika Anda ingin saya datang lebih sering, Anda harus membiarkan saya membaca buku Anda."
    scene expression ("images/episode5/417_1.webp") with dissolve
    charlotte "Kemudian lihatlah dengan baik di sekeliling ruangan karena Anda tidak akan pernah melihatnya lagi."
    scene expression ("images/episode5/417_2.webp") with dissolve
    toby "Selamat malam, [mom]."
    scene expression ("images/episode5/417_1.webp") with dissolve
    charlotte "Selamat malam!"

    return

label episode5_monday_beatrice:


    scene expression ("images/episode5/418.webp") with dissolve
    toby "Jadi Bea, ceritakan lebih banyak tentang diri Anda."
    scene expression ("images/episode5/419_curious.webp") with dissolve
    beatrice "Anda ingin mengenal saya lebih baik?"
    scene expression ("images/episode5/420_smile.webp") with dissolve
    toby "Nah, karena Anda tahu di mana saya tinggal sekarang, saya perlu memastikan bahwa saya tidak membutuhkan keamanan ekstra. Siapa yang tahu maniak seperti apa yang hidup di dalam truk es krim."
    scene expression ("images/episode5/419_laugh.webp") with dissolve
    beatrice "Apakah saya terlihat seperti orang gila bagi Anda?"
    scene expression ("images/episode5/420_laugh.webp") with dissolve
    toby "Anda memiliki truk dan sudah menawari saya es krim gratis."
    scene expression ("images/episode5/419_laugh.webp") with dissolve
    beatrice "Hmm ... sekarang kamu menyebutkannya, mungkin aku."
    scene expression ("images/episode5/419_curious.webp") with dissolve
    beatrice "Apakah Anda yakin ingin mengambil risiko membawa saya pulang?"
    scene expression ("images/episode5/420_flirty.webp") with dissolve
    toby "Jangan khawatir, saya mengirim lokasi langsung ke [mom] saya. Skenario kasus terburuk adalah dia akan menemukan saya mati."
    scene expression ("images/episode5/419_happy.webp") with dissolve
    beatrice "Tunggu, tunggu, tunggu. Bagaimana saya tahu Anda bukan pembunuh berantai. Maksud saya jika saya, saya mulai menunjuk jari ke arah Anda, sehingga saya bisa melarikan diri."
    scene expression ("images/episode5/420_laugh.webp") with dissolve
    toby "Nah, saya bertanya lebih banyak tentang diri Anda dan Anda menghindari jawabannya, jadi bagaimana saya bisa mengambilnya?"
    scene expression ("images/episode5/419_flirty.webp") with dissolve
    beatrice "Itu untuk beberapa alasan, meskipun Anda tidak yakin Anda akan hidup sepanjang hari, Anda ingin mengenal saya lebih baik."
    scene expression ("images/episode5/420_smile.webp") with dissolve
    toby "Mungkin, tapi itu hanya asumsi."
    scene expression ("images/episode5/419_happy.webp") with dissolve
    beatrice "Nah, jika Anda benar -benar ingin tahu, saya lahir dan besar di sini di kota ini. Sekitar 5 tahun yang lalu saya mulai membantu ibu dan ayah saya dengan truk es krim."
    scene expression ("images/episode5/420_normal.webp") with dissolve
    toby "Itu sangat matang dari Anda. Maksud saya, biasanya pada usia itu Anda malu untuk membantu bisnis keluarga, terutama ketika orang yang Anda kenal bisa melihat Anda."
    scene expression ("images/episode5/419_laugh.webp") with dissolve
    beatrice "Siapa bilang aku tidak malu? Saya benci pekerjaan itu. Maksud saya, saya suka di mana Anda bisa makan es krim sebanyak yang Anda inginkan, tetapi setelah beberapa saat Anda terbiasa dengan itu juga."
    scene expression ("images/episode5/420_laugh.webp") with dissolve
    toby "Betapa sulitnya bagi Anda untuk terbiasa dengan es krim."
    scene expression ("images/episode5/419_awkward.webp") with dissolve
    beatrice "Tentu saja itu sulit. Setelah musim panas pertama saya membantu mereka, saya naik 20 pound."
    scene expression ("images/episode5/419_chubby.webp") with dissolve
    beatrice "Saya menjadi gemuk."
    scene expression ("images/episode5/420_laugh.webp") with dissolve
    toby "Itu adalah pemeragaan yang sangat bagus."
    scene expression ("images/episode5/419_laugh.webp") with dissolve
    beatrice "Terima kasih. Ketika saya masih muda, saya ingin menjadi seorang aktris."
    scene expression ("images/episode5/420_curious.webp") with dissolve
    toby "Dan mengapa Anda tidak ingin melakukannya lagi?"
    scene expression ("images/episode5/419_smile.webp") with dissolve
    beatrice "Saya menyadari bahwa saya lebih suka membantu orang daripada saya suka menghibur mereka."
    scene expression ("images/episode5/420_curious.webp") with dissolve
    toby "Bantuan, maksudmu ...?"
    scene expression ("images/episode5/419_smile.webp") with dissolve
    beatrice "Saya akan menjadi dokter atau perawat. Saya masih memperdebatkan yang mana."
    scene expression ("images/episode5/420_happy.webp") with dissolve
    toby "Anda memiliki kurang dari 3 bulan untuk memutuskan apa yang ingin Anda lakukan."
    scene expression ("images/episode5/419_sad.webp") with dissolve
    beatrice "Sebenarnya saya bahkan tidak punya waktu itu, karena kelulusan dalam sebulan dan tepat setelah itu saya harus memutuskan perguruan tinggi mana yang akan saya hadiri di musim gugur."
    scene expression ("images/episode5/419_smile.webp") with dissolve
    beatrice "Tetapi bagian yang penting adalah saya ingin bekerja di bidang medis, perawat atau dokter tidak benar -benar penting."
    scene expression ("images/episode5/420_laugh.webp") with dissolve
    toby "Itu bagus karena saya mulai melakukan renovasi rumah, jadi jika saya menghancurkan jari saya dengan palu, saya akan tahu siapa yang harus dihubungi."
    scene expression ("images/episode5/419_surprised.webp") with dissolve
    beatrice "NOOO ... Jangan lakukan itu. Saya belum memulai kursus apa pun. Saya tidak tahu apa -apa tentang memperlakukan Anda."
    scene expression ("images/episode5/420_smile.webp") with dissolve
    toby "Anda harus tahu sesuatu."
    scene expression ("images/episode5/419_flirty.webp") with dissolve
    beatrice "Hanya ciuman boo boo. \ 'Yang diperhitungkan?"
    scene expression ("images/episode5/420_smile.webp") with dissolve
    toby "Mengapa Anda tidak mengatakan itu sejak awal. Saya pikir saya memiliki ide yang lebih baik sekarang."
    scene expression ("images/episode5/419_curious.webp") with dissolve
    beatrice "Sekarang saya tertarik."
    scene expression ("images/episode5/420_laugh.webp") with dissolve
    toby "Alih -alih memegang paku dengan jari -jari saya, saya akan memegangnya dengan bibir saya. Lagi pula, saya perlu merawat jari saya dengan baik."
    scene expression ("images/episode5/419_laugh.webp") with dissolve
    $ unlockImage(persistent.beatrice_02)
    beatrice "Anda sangat konyol."
    scene expression ("images/episode5/421.webp") with dissolve
    beatrice "Ini aku."
    toby "Di Sini?"
    scene expression ("images/episode5/422.webp") with dissolve
    beatrice "Yup. Terima kasih atas perjalanannya dan lain kali saya mengajukan pertanyaan dan Anda menjawab, karena Anda agak bermain dengan saya sepanjang perjalanan."
    beatrice "Dan saya masih tidak tahu apa -apa tentang Anda."
    toby "Mungkin, tapi setidaknya aku akan tidur lebih nyenyak mengetahui kamu bukan pembunuh berantai."
    scene expression ("images/episode5/423.webp") with dissolve
    beatrice "Itu membuat salah satu dari kita, karena saya masih harus mengunci pintu sampai saya belajar lebih banyak tentang Anda."
    toby "Ya. Lakukan itu."
    scene expression ("images/episode5/424.webp") with dissolve
    beatrice "Sekali lagi terima kasih atas perjalanannya dan berhati -hatilah dengan palu itu."
    toby "Akan melakukannya ... sampai jumpa."
    beatrice "Selamat malam [toby!c]."
    toby "Kamu juga."

    return

label episode5_monday_night:
    $ progress = 81


    scene expression ("images/episode5/425.webp") with fade
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode5/426.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    if beatrice_path == True:
        scene expression ("images/episode5/427.webp") with dissolve
        patricia "Anda sudah kembali?"
        scene expression ("images/episode5/428.webp") with dissolve
        toby "Ya. Dia tinggal cukup dekat. Lima menit atau lebih."
    else:
        scene expression ("images/episode5/428.webp") with dissolve
        toby "Anda sudah kembali?"
        scene expression ("images/episode5/427.webp") with dissolve
        patricia "Dan mandi. Saya secepat cheetah."
        scene expression ("images/episode5/428.webp") with dissolve
        toby "Dia tinggal dekat?"
        scene expression ("images/episode5/427.webp") with dissolve
        patricia "Lima menit atau lebih."
    label memory_19:


        scene expression ("images/episode5/429.webp") with dissolve
        patricia "Saya akan berubah, jangan melihat ke arah ini."
        toby "Tentu. Tidak masalah."
        scene expression ("images/episode5/430.webp") with dissolve
        menu:
            "{i} [JGR] Lihat saat dia mengubah {/i}"(csq="Galeri Gambar & Penting untuk Tris \ 'Path"):
                $ ep5_trisChange = True
                $ unlockImage(persistent.patricia_11)
                scene expression ("images/episode5/431.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode5/432.webp") with dissolve:
                    yalign 1.0
                    linear 10.0 yalign 0.0

                $ ui.pausebehavior(9.3)
                $ ui.saybehavior()
                $ ui.interact()
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She has such a good looking figure.{/i}"
                scene expression ("images/episode5/433.webp") with dissolve
                $ ui.saybehavior()
                $ ui.interact()
                scene expression ("images/episode5/434.webp") with dissolve
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Can't believe she hasn't had any boyfriends with an ass like that.{/i}"
                scene expression ("images/episode5/435.webp") with dissolve
                patricia "Saya harap Anda tidak melihat atau saya harus menendang Anda."
                scene expression ("images/episode5/436.webp") with dissolve
                toby "Tidak. Saya suka mereka tepat di tempat mereka berada."
                scene expression ("images/episode5/435.webp") with dissolve
                patricia "Itulah yang saya pikirkan."

            "{i} menjadi anak yang baik {/i}" if not _in_replay:
                pass

        scene expression ("images/episode5/437.webp") with dissolve
        patricia "Ngomong -ngomong, apa yang kamu lakukan? Mencari mobil sejak saya akan memenangkan taruhan?"
        scene expression ("images/episode5/436.webp") with dissolve
        toby "Sebenarnya saya sedang mencari pakaian pelayan."
        scene expression ("images/episode5/438.webp") with dissolve
        patricia "Anda membuang -buang waktu Anda."
        scene expression ("images/episode5/436.webp") with dissolve
        toby "Tidak apa -apa, saya bisa hidup dengan itu, tetapi dapatkah Anda membersihkan kamar saya selama sebulan penuh?"
        scene expression ("images/episode5/439.webp") with dissolve
        patricia "Saya kira kita tidak akan pernah tahu."
        if ep5_trisChange == True:
            $ unlockMemory(persistent.memory_19)
        $ renpy.end_replay()

    if beatrice_path:
        scene expression ("images/episode5/440_curious.webp") with dissolve
        patricia "Jadi? Bagaimana teman kencan Anda dengan Bea?"
        scene expression ("images/episode5/441_laugh.webp") with dissolve
        toby "Anda menyebutnya kencan?"
        scene expression ("images/episode5/440_curious.webp") with dissolve
        patricia "Apakah Anda mengatakan Anda tidak akan berkencan dengannya?"
        scene expression ("images/episode5/441_smile.webp") with dissolve
        toby "Ya, saya akan melakukannya. Itulah mengapa kita keluar besok."
        scene expression ("images/episode5/440_surprised.webp") with dissolve
        patricia "Benar-benar? Tidakkah kamu punya pacar?"
        scene expression ("images/episode5/441_flirty.webp") with dissolve
        if emma_break:
            toby "Tidak. Saya bebas sebagai burung. Saya semua tersedia untuk BEA, sekarang."
            scene expression ("images/episode5/440_doubt.webp") with dissolve
            patricia "Hmm ... dia lebih baik dari Emma, tapi aku masih tidak percaya dia menerima, karena dia sudah tertarik pada orang lain."
            scene expression ("images/episode5/441_normal.webp") with dissolve
            toby "Dia tidak tertarik pada orang lain, dia benar -benar terbuka untuk menggoda sebenarnya."
            scene expression ("images/episode5/440_laugh.webp") with dissolve
            patricia "Ya benar. Seperti saya akan mempercayai apa pun yang Anda katakan."
            scene expression ("images/episode5/441_normal.webp") with dissolve
            toby "Yah, percaya apa yang Anda inginkan, tapi dia mencium saya ketika saya mengantarnya."
        else:
            toby "Oh benar. Dia akan datang ke sini besok. Kira saya akan pergi keluar dengan mereka berdua."
            scene expression ("images/episode5/440_doubt.webp") with dissolve
            patricia "Seperti dia akan menerima sesuatu seperti itu. Dia lebih baik daripada pelacur yang biasanya Anda nongkrong."
            scene expression ("images/episode5/441_laugh.webp") with dissolve
            toby "Saya tidak tahu tentang itu. Ketika saya mengatakan kepadanya bahwa saya punya pacar, dia mengatakan kepada saya bahwa dia juga punya pacar, jadi selama kita keduanya baik -baik saja dengan itu, itu baik -baik saja."
            scene expression ("images/episode5/440_surprised.webp") with dissolve
            patricia "Dia memberitahumu tentang dia? Dia bukan pacarnya, itu hanya seorang pria yang dia bicarakan dari waktu ke waktu."
            scene expression ("images/episode5/441_normal.webp") with dissolve
            toby "Aku tidak tahu tentang itu, aku hanya tahu dia menciumku ketika aku mengantarnya."

        scene expression ("images/episode5/440_surprised.webp") with dissolve
        patricia "Tidak mungkin dia menciummu."
        scene expression ("images/episode5/440_curious.webp") with dissolve
        patricia "Benar? Maksudku, bahkan jika dia melakukannya, aku yakin itu hanya ciuman di pipi."
        scene expression ("images/episode5/441_laugh.webp") with dissolve
        toby "Sebenarnya itu di antara pipi. Jenis ciuman dengan kaki di udara."
        scene expression ("images/episode5/440_sad.webp") with dissolve
        patricia "Tidak mungkin dia melakukan itu."
        scene expression ("images/episode5/441_normal.webp") with dissolve
        toby "Jika Anda tidak percaya, Anda dapat bertanya besok di sekolah dan dia akan memberi tahu Anda."
        scene expression ("images/episode5/440_angry.webp") with dissolve
        patricia "Saya tidak punya apa -apa untuk dibicarakan dengannya."
        scene expression ("images/episode5/441_laugh.webp") with dissolve
        toby "Cemburu?"
        scene expression ("images/episode5/440_arogant.webp") with dissolve
        patricia "Mengapa saya cemburu? Anda adalah [brother] bukan pacar saya."
        scene expression ("images/episode5/441_curious.webp") with dissolve
        toby "Lalu kenapa kamu begitu bekerja?"
        scene expression ("images/episode5/440_normal.webp") with dissolve
        patricia "Um ... {w} karena saya tidak mengira dia perempuan jalang yang akan mencium siapa pun hanya karena membawanya pulang."
        scene expression ("images/episode5/441_laugh.webp") with dissolve
        toby "Aku sekarat ... kamu benar -benar percaya dia menciumku?"
        scene expression ("images/episode5/440_surprised.webp") with dissolve
        patricia "Dia tidak?"
        scene expression ("images/episode5/441_laugh.webp") with dissolve
        toby "Tidak, tentu saja dia tidak. Apakah Anda benar -benar percaya itu?"
        scene expression ("images/episode5/440_arogant.webp") with dissolve
        patricia "Tentu saja tidak. Saya hanya bermain untuk melihat berapa banyak lagi yang akan Anda bohongi."
        scene expression ("images/episode5/441_laugh.webp") with dissolve
        toby "Ya benar."
        scene expression ("images/episode5/440_curious.webp") with dissolve
        patricia "Jadi? Apa yang kamu bicarakan?"
        scene expression ("images/episode5/441_normal.webp") with dissolve
        toby "Anda tahu ... barang, keluarga, kuliah ..."
        toby "Berbicara tentang kuliah, apakah Anda memutuskan kemana kamu ingin pergi?"
    else:

        scene expression ("images/episode5/440_normal.webp") with dissolve
        patricia "Tidak akan terjadi karena Anda terlalu malas dan selain itu, Anda tidak tahu apa -apa tentang konstruksi."
        scene expression ("images/episode5/441_laugh.webp") with dissolve
        toby "Anda akan terkejut dengan betapa banyak hal yang dapat Anda pelajari di internet."
        scene expression ("images/episode5/440_laugh.webp") with dissolve
        patricia "Ya benar."
        scene expression ("images/episode5/441_normal.webp") with dissolve
        toby "Jangan khawatir tentang keterampilan konstruksi saya. Anda hanya khawatir tentang bagaimana Anda akan membersihkan kamar saya saat Anda kuliah."
        toby "Berbicara tentang kuliah, sudahkah Anda memutuskan kemana Anda ingin pergi?"

    scene expression ("images/episode5/440_smile.webp") with dissolve
    patricia "Yah ada perguruan tinggi yang hebat di kota ini, jadi saya tidak mengerti mengapa saya harus pergi ke tempat lain."
    scene expression ("images/episode5/441_normal.webp") with dissolve
    toby "Ya. Emma memberitahuku tentang itu."
    scene expression ("images/episode5/440_curious.webp") with dissolve
    patricia "Dia akan belajar di sana juga?"
    scene expression ("images/episode5/441_laugh.webp") with dissolve
    toby "Yup. Kalian berdua akan menjadi teman sekelas dan akan menjadi BFF."
    scene expression ("images/episode5/440_arogant.webp") with dissolve
    patricia "Persetan! Aku benci nyali."
    scene expression ("images/episode5/441_smile.webp") with dissolve
    toby "Itu tidak masalah, dia tetap datang ke sini."
    scene expression ("images/episode5/440_curious.webp") with dissolve
    $ progress = 82
    if emma_break == True:
        if beatrice_path == True:
            patricia "Apakah Anda pikir dia masih akan datang ke sini karena kalian berdua tidak ada lagi?"
        else:
            patricia "Tidak bisakah Anda putus setidaknya sampai dia menemukan perguruan tinggi lain di kota yang berbeda?"
            scene expression ("images/episode5/441_normal.webp") with dissolve
            toby "Sampai pagi ini kita tidak bersama."
            scene expression ("images/episode5/440_surprised.webp") with dissolve
            patricia "Benar-benar? Kenapa?"
            scene expression ("images/episode5/441_normal.webp") with dissolve
            toby "Maaf, tapi saya tidak berpikir saya ingin membicarakannya."
            scene expression ("images/episode5/440_curious.webp") with dissolve
            patricia "Jadi, apakah Anda masih berpikir dia akan datang ke sini karena kalian berdua tidak ada lagi?"
        scene expression ("images/episode5/441_normal.webp") with dissolve
        toby "Saya tidak tahu, mungkin kita akan menyelesaikan masalah."
    else:
        patricia "Tidak bisakah Anda putus setidaknya sampai dia menemukan perguruan tinggi lain di kota yang berbeda?"
        scene expression ("images/episode5/441_normal.webp") with dissolve
        toby "Apakah kamu benar -benar menanyakan itu padaku?"
        scene expression ("images/episode5/440_guilty.webp") with dissolve
        patricia "Saya bercanda ..."

    scene expression ("images/episode5/441_curious.webp") with dissolve
    toby "Ngomong -ngomong, apakah Anda sudah memutuskan apa yang akan Anda pelajari?"
    scene expression ("images/episode5/440_sad.webp") with dissolve
    patricia "Belum. Saya berpikir mungkin seorang perawat seperti Bea, dia membuatnya terdengar sangat bagus."
    scene expression ("images/episode5/441_laugh.webp") with dissolve
    toby "Anda takut pada jarum. Bagaimana Anda bisa bekerja sebagai perawat?"
    scene expression ("images/episode5/440_angry.webp") with dissolve
    patricia "Saya takut pada jarum yang menuju ke lengan saya."
    scene expression ("images/episode5/441_laugh.webp") with dissolve
    toby "Dan Anda juga sakit saat melihat darah."
    scene expression ("images/episode5/440_tongue.webp") with dissolve
    patricia "Seperti Anda lebih baik dari saya."
    scene expression ("images/episode5/441_laugh.webp") with dissolve
    toby "Setidaknya saya tidak ingin menjadi perawat."
    scene expression ("images/episode5/440_laugh.webp") with dissolve
    patricia "Ya Anda terlihat lucu dalam gaun itu."
    scene expression ("images/episode5/441_smile.webp") with dissolve
    toby "Jadi Anda ingin menjadi perawat untuk pakaian itu?"
    scene expression ("images/episode5/441_flirty.webp") with dissolve
    toby "Jika itu masalahnya, beri tahu saya dan saya akan membelikan Anda beberapa online dan kemudian Anda akan memikirkan sesuatu yang sangat Anda kuasai."
    scene expression ("images/episode5/440_normal.webp") with dissolve
    patricia "Itu adalah umpan. Saya tidak ingin memakai pakaian yang Anda beli dari toko seks."
    scene expression ("images/episode5/441_flirty.webp") with dissolve
    toby "Saya tidak memikirkan hal itu, tetapi karena Anda menyebutkannya, saya pikir saya baru saja datang dengan ide untuk pakaian pelayan."
    scene expression ("images/episode5/440_surprised.webp") with dissolve
    patricia "No tidak!"
    scene expression ("images/episode5/441_laugh.webp") with dissolve
    toby "Saya pikir Anda mengatakan saya akan kalah, jadi mengapa Anda peduli pakaian apa yang saya pilih, karena Anda tidak akan memakainya?"
    scene expression ("images/episode5/440_normal.webp") with dissolve
    patricia "Ya, tapi bagaimana jika."
    patricia "Anda seorang perv. Anda tahu itu benar?"
    scene expression ("images/episode5/441_curious.webp") with dissolve
    toby "Dan mengapa Anda mengatakan itu?"
    scene expression ("images/episode5/440_curious.webp") with dissolve
    patricia "Karena seperti apa [brother] ingin melihat [sister] dalam pakaian pelayan yang seksi."
    scene expression ("images/episode5/441_laugh.webp") with dissolve
    toby "Saya melihat gambaran besar di sini."
    scene expression ("images/episode5/440_laugh.webp") with dissolve
    patricia "Dan gambaran besar apa?"
    scene expression ("images/episode5/441_smile.webp") with dissolve
    toby "Anda memakai sesuatu yang seksi dan sedikit terbuka yang akan membuat Anda merasa malu. Jadi untuk menyingkirkan pakaian lebih cepat Anda hanya akan bekerja lebih keras."
    toby "Pada akhirnya itu menang, menang."
    scene expression ("images/episode5/440_laugh.webp") with dissolve
    patricia "Teori Anda terdengar menarik tetapi memiliki masalah."
    scene expression ("images/episode5/441_curious.webp") with dissolve
    toby "Yang?"
    scene expression ("images/episode5/440_doubt.webp") with dissolve
    patricia "Saya tidak melihat apa yang saya menang?"
    scene expression ("images/episode5/441_curious.webp") with dissolve
    toby "Siapa yang mengatakan sesuatu tentang kamu memenangkan sesuatu?"
    scene expression ("images/episode5/441_laugh.webp") with dissolve
    toby "Ini adalah kemenangan bagi saya bahwa Anda membersihkan kamar saya lebih cepat."
    scene expression ("images/episode5/441_flirty.webp") with dissolve
    toby "Dan kemenangan bagi saya karena melihat Anda hampir telanjang."
    scene expression ("images/episode5/442.webp") with dissolve
    patricia "Anda orang cabul yang sakit!"
    toby "Aku bercanda, kamu jalang gila."
    scene expression ("images/episode5/443.webp") with dissolve
    patricia "Saya akan tidur sekarang, pada saat saya bangun, saya harap Anda akan memiliki lebih banyak akal dalam diri Anda."
    scene expression ("images/episode5/444.webp") with dissolve
    if toby_job == 0:
        toby "Bagus. Jika saya menyukai pekerjaan Anda setelah satu bulan, saya mungkin membayar Anda untuk terus membersihkan kamar saya."
        scene expression ("images/episode5/445.webp") with dissolve
        patricia "Tidak terima kasih. Saya dapat meyakinkan Anda untuk memberi saya uang tanpa membersihkan ruangan. Hanya wajah cemberut dan Anda akan memberi saya semua uang yang saya butuhkan."
        scene expression ("images/episode5/444.webp") with dissolve
        toby "Anda benar -benar berpikir Anda bisa bermain saya?"
        scene expression ("images/episode5/445.webp") with dissolve
        patricia "Sejauh ini bekerja dengan baik."
        scene expression ("images/episode5/444.webp") with dissolve
        toby "Itu saja. Saya mencari pakaian di kelinci merah."
    else:

        toby "Ngomong -ngomong, ada penjualan pada pakaian pelayan. Jika Anda membeli pakaian, Anda mendapatkan cambuk secara gratis."
        toby "Apa yang kamu katakan? Haruskah saya membelinya jika saya tidak suka bagaimana Anda membersihkan kamar saya?"
        scene expression ("images/episode5/446.webp") with dissolve
        patricia "Hanya jika Anda memiliki beberapa fetish aneh dan rencanakan untuk mencambuk diri sendiri."
        scene expression ("images/episode5/444.webp") with dissolve
        toby "Maaf, tidak seperti itu, jadi saya kira kami harus puas dengan pantat Anda."
    scene expression ("images/episode5/446.webp") with dissolve
    patricia "{size=12}{color=#FDCA6E}* murmuring *{/color}{/size}\n{i}Idiot!{/i}"
    scene expression ("images/episode5/447.webp") with dissolve
    toby "Selamat malam."
    scene expression ("images/episode5/448.webp") with dissolve
    patricia "Kamu juga, bodoh [brother]."
    scene expression ("images/episode5/447.webp") with dissolve
    toby "Ya, ya. Aku pun mencintaimu."
    scene expression ("images/episode5/448.webp") with dissolve
    patricia "{size=12}{color=#FDCA6E}* murmuring *{/color}{/size}\n{i}Me too.{/i}"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
