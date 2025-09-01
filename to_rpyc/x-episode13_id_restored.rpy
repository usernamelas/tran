image ep13_048 = Movie(play="video/episode13/048.webm", image="images/episode13/048.webp", loop = False)
image ep13_215 = Movie(play="video/episode13/215.webm", loop = True)
image ep13_216 = Movie(play="video/episode13/216.webm", loop = True)
image ep13_217 = Movie(play="video/episode13/217.webm", loop = True)
image ep13_218 = Movie(play="video/episode13/218.webm", loop = True)
image ep13_221 = Movie(play="video/episode13/221.webm", loop = True)
image ep13_222 = Movie(play="video/episode13/222.webm", loop = True)
image ep13_223 = Movie(play="video/episode13/223.webm", loop = True)
image ep13_224 = Movie(play="video/episode13/224.webm", loop = True)
image ep13_225 = Movie(play="video/episode13/225.webm", loop = True)
image ep13_226 = Movie(play="video/episode13/226.webm", loop = True)
image ep13_290 = Movie(play="video/episode13/290.webm", image="images/episode13/290.webp", loop = False)
image ep13_307 = Movie(play="video/episode13/307.webm", image="images/episode13/307.webp", loop = False)

label episode13:
    $ progress = 168
    stop music fadeout 10.0
    scene expression ("images/utils/black.png") with Dissolve(5)
    show screen ui_newEpisode(2, 7) with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_newEpisode

    call episode13_morning_bedroom from _call_episode13_morning_bedroom
    call episode13_breakfast from _call_episode13_breakfast
    call episode13_groceries from _call_episode13_groceries
    call episode13_gym_reception from _call_episode13_gym_reception
    call episode13_gym_workout from _call_episode13_gym_workout
    call episode13_gym_showers from _call_episode13_gym_showers
    call episode13_gym_sheila from _call_episode13_gym_sheila
    call episode13_work from _call_episode13_work

    return

label episode13_morning_bedroom:

    show screen ui_message("Monday") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message



    scene expression ("images/episode13/001.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()

    if toby_job == 0:
        call episode13_morning_bedroom_darlene from _call_episode13_morning_bedroom_darlene
    else:
        call episode13_morning_bedroom_katrina from _call_episode13_morning_bedroom_katrina

    return

label episode13_morning_bedroom_darlene:
    scene expression ("images/episode13/002.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... I forgot to put my phone on silent last night, I guess it's time to start my day.{/i}"
    scene expression ("images/episode13/004.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Oh, it's Darlene. I wonder what she wants.{/i}"
    scene expression ("images/episode13/004_texting.webp") with dissolve
    call sms_incoming ("darlene", "Morning, [toby!c]. I hope you had a great weekend. Sadly, the weekend is over and we have a lot to. Please be at the office by noon.") from _call_sms_incoming_265
    call sms_sent ("darlene", "Morning, Mrs. Darlene. Sure, I'll be there before then.") from _call_sms_sent_214
    call sms_incoming ("darlene", "Perfect. Sorry, but please also cancel any evening plans, there's a lot to do.") from _call_sms_incoming_266
    call sms_sent ("darlene", "No problem at all. I didn't have any.") from _call_sms_sent_215
    call sms_incoming ("darlene", "I find it hard to believe that a good looking guy like you doesn't have any plans tonight.") from _call_sms_incoming_267
    call sms_sent ("darlene", "Maybe I'm not as good looking as you thought.") from _call_sms_sent_216
    call sms_incoming ("darlene", "Yeah, I suppose it's possible.") from _call_sms_incoming_268
    if darlene_path:
        call sms_sent ("darlene", "Nah, you were right the first time. I mean, I can't see how a woman as beautiful as you could possibly fall for some ugly guy.") from _call_sms_sent_217
        call sms_incoming ("darlene", "I'm with Kat. Talk to you later.") from _call_sms_incoming_269
        call sms_sent ("darlene", "Oh, Sure. Sorry.") from _call_sms_sent_218
        hide screen message
        scene expression ("images/episode13/005.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... That was dumb. I need to be more careful about flirting with her over text.{/i}"
    else:
        call sms_sent ("darlene", "OK, see you later.") from _call_sms_sent_219
        call sms_incoming ("darlene", "Sure.") from _call_sms_incoming_270
        hide screen message
        scene expression ("images/episode13/005.webp") with dissolve

    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}OK, Now that I'm going back to work, How can I help Sheila?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I suppose I could start looking at Katrina's building. But I have to be careful. I have a feeling that none of this is a game.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Dammit all to hell, why did I agree to help her? Well, there's the simple fact that I sure wouldn't want to be in her shoes. I can't imagine how I would feel or what I would do if Tris were kidnapped.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But Sheila has been trained for things like this. She's an undercover cop, for fuck sake. I'm just a schmuck who didn't go to college because it was too much work.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}How in the hell did I get involved in this? I can't. I shouldn't. I should just call Sheila and tell her I'm out.{/i}"
    scene expression ("images/episode13/006.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But shit, how could I live with myself knowing that some girl got kidnapped and who knows how many others? And maybe I could do something...but I'm so fucking scared.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Ok, shithead - get a grip. People need your help. Maybe I can ask Darlene a few innocent questions about Katrina's building without raising suspicions. And if that turns out to be a dead end, I just tell Sheila I didn't find anything.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She mentioned something about a BDSM club. Katrina's building is an apartment building. I don't see how a club like that could possibly work in that building without anyone finding out.{/i}"
    scene expression ("images/episode13/007.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Okay, so what can I do? I could try to find out where the club operates and then just let the cops do their job. This is already way out of my league.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I don't think anyone would blame me. I'm just a 20 year old guy. I don't want to get involved with the mafia or whatever the hell this is.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'll just ask Darlene a few questions about Katrina and that's it. That's the safest thing to do.{/i}"

    scene expression ("images/episode13/008.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Anyway, since I've got a little time to kill, I'll go hit the gym. It's been a while since my last workout. I'm already feeling like an old man. Rusty and stiff.{/i}"
    scene expression ("images/episode13/009.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I need to grab something to eat before I go. I can't work out on an empty belly!{/i}"

    return

label episode13_morning_bedroom_katrina:
    scene expression ("images/episode13/003.webp") with dissolve
    play sound "audio/fx/notification_5.mp3"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... I forgot to put my phone on silent last night, I guess it's time to start my day.{/i}"
    scene expression ("images/episode13/004.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}A text from Katrina this early? I wonder what the hell she wants.{/i}"
    scene expression ("images/episode13/004_texting.webp") with dissolve
    call sms_incoming ("katrina", "Where were you last night?") from _call_sms_incoming_271
    call sms_sent ("katrina", "Umm... Morning to you too. I was out.") from _call_sms_sent_220
    call sms_incoming ("katrina", "You were supposed to be at the club. Have you forgotten your actual job? Your job is to bring people in the club.") from _call_sms_incoming_272
    call sms_sent ("katrina", "Well forgive me, but in the last 2 months I've only done that twice, since you usually have something else for me to do. I can't actually tell what my job is.") from _call_sms_sent_221
    call sms_incoming ("katrina", "You're my lap dog. You do what I tell you to do.") from _call_sms_incoming_273
    call sms_sent ("katrina", "Lap dog? You better be careful, because this dog just might bite you.") from _call_sms_sent_222
    call sms_incoming ("katrina", "Someone woke up all cranky and shit.") from _call_sms_incoming_274
    if katrina_path:
        call sms_sent ("katrina", "And someone clearly needs a good fuck, because you're starting to get a little bitchy again.") from _call_sms_sent_223
        call sms_incoming ("katrina", "And who do you think can give me a good fuck? You? Don't make me laugh.") from _call_sms_incoming_275
        call sms_sent ("katrina", "Did you want something? Or do you just miss the taste of my cock in your dirty mouth.") from _call_sms_sent_224
    else:
        call sms_sent ("katrina", "Did you have something important to say, or did you just feel like offending me early in the morning?") from _call_sms_sent_225
    call sms_incoming ("katrina", "Get your ass to the club by noon. We have work to do.") from _call_sms_incoming_276
    call sms_sent ("katrina", "Fine. See you then.") from _call_sms_sent_226
    hide screen message
    scene expression ("images/episode13/005.webp") with dissolve
    if katrina_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fucking bitch. She needs to be put back in her place. I can't say I hate fucking her, but she needs to learn to respect me.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fucking bitch. She treats everybody like this. I don't understand how Darlene puts up with her.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}And fuck me... How the hell am I going to help Sheila without getting my ass killed. If Katrina finds out I'm helping the cops, she's going to shoot me dead in the face.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, fuck, fuck! What have I gotten myself into? Why did I tell Sheila I would help her? I'm lucky enough that Katrina hasn't killed me already. That bitch is absolutely insane.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I mean, I can't imagine what Sheila and her [sister] are going through right now, if she's even still alive, that is. But how can I help them?{/i}"
    scene expression ("images/episode13/006.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Why should I even help the cops? If I believe everything Sheila said, then Katrina's more dangerous than I already know her to be.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}How the fuck can I help her without Katrina knowing? Because if she suspects me having any involvement with anything, I'm dead. Immunity won't keep me alive.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Not to mention, I'm a nobody. All the privileges and respect I get, it's because I work for her. Nobody dares talk back to me, because they know I work for her. But if they find out that I snitched on her, I'm done.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, fuck, motherfucker! I can't help Sheila.{/i}"
    scene expression ("images/episode13/007.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I just can't. It's too risky. Besides, I've kind of started liking being the bad guy. I enjoy the respect I get. If she goes down, I'm going down with her. Even if she doesn't find out about my involvement, I'm still done.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But wait. Whoever comes after her wouldn't give a fuck about me. So the best thing for me to do would be to make sure she's not caught until I've made a name for myself. I could pretend to help Sheila, while I'm really helping myself.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}That way, when Kat goes down, I'll still have my name and respect. Hell, maybe I'd even continue making that \"Hooker\"obat yang jelas sangat populer. {/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmmm....That's actually not a terrible idea. If I could take her place that would be perfect. The cops would know me as the good guy who helped them. In their eyes, I'm a nobody. They wouldn't suspect me of anything.{/i}"
    scene expression ("images/episode13/008.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What the Fuck?!?! What am I thinking? I'm not like this.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Or I should say, I never used to be like this.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Holy fuck I can't think straight. I need to clear my head. I'll go to the gym since I've got some time to kill before I have to go to the club.{/i}"
    scene expression ("images/episode13/009.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I need to get something to eat first. I can't lift weights on an empty stomach.{/i}"

    return

label episode13_breakfast:
    $ progress = 169
    scene expression ("images/episode13/010.webp") with dissolve:
        yalign 1.0
        linear 10.0 yalign 0.0

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode13/011.webp") with dissolve
    toby "Pagi, [mom]."
    scene expression ("images/episode13/012.webp") with dissolve
    charlotte "{size=12}{color=#FDCA6E}* loudly *{/color}{/size}\nUhh... What!?"
    scene expression ("images/episode13/013.webp") with dissolve
    charlotte "Ya Tuhan, kamu mengejutkanku. Saya sangat fokus."
    scene expression ("images/episode13/014.webp") with dissolve
    if charlotte_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She must not have heard me coming. I bet she's working on her book. I wonder what Mrs. Etolla Rahc and the hot waiter are up to these days?{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}That's strange. She must not have heard me coming.{/i}"
    toby "Maaf, saya tidak bermaksud menakut -nakuti Anda."
    scene expression ("images/episode13/015.webp") with dissolve
    charlotte "Tidak, Anda tidak. Saya hanya fokus pada sesuatu. Bagaimana Anda tidur?"
    scene expression ("images/episode13/016.webp") with dissolve
    toby "Sangat bagus, sebenarnya. Saya tidur seperti batu. Aku tidak ingat apa pun setelah kepalaku menabrak bantal."
    if patricia_path:
        charlotte "Sepertinya Anda dan Tris bersenang -senang tadi malam. Butuh waktu hampir 15 menit untuk membangunkannya di sekolah."
        toby "Dia sudah pergi?"
        scene expression ("images/episode13/017.webp") with dissolve
        charlotte "Ya, dia mencoba mengatakan sesuatu tentang bahwa kelas pertama tidak sampai jam 10:00, tapi saya tahu kapan dia berbohong."
        toby "Nah, dia buruk dalam berbohong."
        charlotte "Ya, dia."
        scene expression ("images/episode13/016.webp") with dissolve
        charlotte "Jadi apa yang kalian berdua lakukan tadi malam?"
        toby "Tidak ada yang gila. Kami pergi ke sebuah bar, dan ternyata, itu adalah bar yang sama di mana Anda menendang pantat saya di kolam renang. Kami memiliki beberapa bir ringan dengan lemon dan baru saja membicarakan hal -hal."
        scene expression ("images/episode13/017.webp") with dissolve
        charlotte "Sejak kapan Anda minum bir dengan lemon?"
        toby "Dan orang yang tidak tahu cara minum.Bisa aja. Tris tidak bisa menangani alkoholnya, aku hanya mencoba membantunya meningkatkan toleransi. Dia seorang gadis cantik dan tidak bersalah."
        scene expression ("images/episode13/018.webp") with dissolve
        if toby_job == 0:
            toby "Saya tidak ingin idiot mencoba memanfaatkannya."
            charlotte "Anda baik [brother] untuknya. Aku senang dia punyamu untuk memperhatikannya."
            toby "Nah ... ada banyak idiot di luar sana yang akan melompat pada kesempatan untuk mengambil keuntungan dari seorang gadis mabuk."
        else:
            toby "Saya tidak ingin beberapa brengsek mencoba memanfaatkannya."
            charlotte "Selain bahasa Anda, Anda baik [brother] untuknya. Aku senang dia punyamu untuk merawatnya."
            toby "[mom!c], saya bekerja di sebuah klub. Saya telah melihat banyak orang brengsek mencoba memanfaatkan gadis -gadis mabuk. Saya berjanji kepada Anda, itu tidak akan terjadi pada Tris."
        scene expression ("images/episode13/016.webp") with dissolve
        charlotte "Tidak semua orang memiliki [mother] yang baik untuk mengajari mereka cara yang tepat untuk memperlakukan seorang wanita."
        scene expression ("images/episode13/017.webp") with dissolve
    else:
        charlotte "Ya, saya tahu. Saya pergi ke kamar Anda untuk melihat Anda jika Anda ingin menonton film, tetapi Anda sudah tidur."
        toby "Mengapa Anda tidak membangunkan saya?"
        charlotte "Jenis [mother] apa yang akan saya lakukan jika saya membangunkan Anda hanya untuk menonton film?"
        scene expression ("images/episode13/017.webp") with dissolve
        toby "Mungkin bukan yang bagus."
        charlotte "Tepat. Saya orang yang baik."
    toby "Dan apakah ini baik [mother] saya ingin membuat saya sarapan sebelum saya pergi ke gym?"
    scene expression ("images/episode13/019.webp") with dissolve
    charlotte "Apa yang kamu suka?"
    scene expression ("images/episode13/020.webp") with dissolve
    toby "Sesuatu yang cepat dan mudah. Telur dan Bacon? Saya akan membutuhkan protein."
    if charlotte_path:
        scene expression ("images/episode13/021_2.webp") with dissolve
        charlotte "Tentu, sayang."
        scene expression ("images/episode13/021_3.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I could stare at that ass all day.{/i}"
    else:
        scene expression ("images/episode13/021_1.webp") with dissolve
        charlotte "Tentu, sayang."
    scene expression ("images/episode13/022.webp") with dissolve
    charlotte "Terkadang saya benar -benar rindu pergi ke gym."
    scene expression ("images/episode13/023_curious.webp") with dissolve
    toby "Saya yakin Anda akan menyukainya di sana.Jadi mengapa kamu tidak ikut denganku? Gym yang saya kunjungi cukup kecil dan nyaman. Itu tidak ramai."
    scene expression ("images/episode13/024_normal.webp") with dissolve
    charlotte "Saya tidak berpikir itu gym yang saya rindukan. Yang sangat saya rindukan, adalah keluar dari rumah sialan ini."
    scene expression ("images/episode13/023_normal.webp") with dissolve
    toby "Lalu keluar saja. Temukan diri Anda sonia lain untuk pergi bersama dan melakukan sesuatu."
    scene expression ("images/episode13/024_laugh.webp") with dissolve
    charlotte "Aku benar -benar tidak sedekat itu dengan Sonia. Saya tidak punya orang lain untuk pergi keluar, tetapi karena kami adalah tetangga, itu adalah dia, atau pergi sendirian."
    scene expression ("images/episode13/024_normal.webp") with dissolve
    charlotte "Sonia lebih baik daripada siapa pun, dan itulah sebabnya saya bergaul dengannya. Tapi dia sangat dimanjakan oleh suaminya."
    scene expression ("images/episode13/023_laugh.webp") with dissolve
    toby "Sebutkan seorang wanita di lingkungan lama kami yang tidak dimanjakan oleh suaminya."
    scene expression ("images/episode13/024_arogant.webp") with dissolve
    charlotte "Wanita ini, di sini."
    scene expression ("images/episode13/023_smile.webp") with dissolve
    toby "Baik, pengecualian untuk aturan, tetapi bisakah Anda menyebutkan nama orang lain?"
    scene expression ("images/episode13/024_laugh.webp") with dissolve
    charlotte "Tidak, saya bisa \ 't. Mereka semua sombong."
    scene expression ("images/episode13/023_normal.webp") with dissolve
    toby "Jadi kembali ke subjek yang ada. Mengapa Anda tidak menemukan orang lain untuk pergi keluar, atau menunggu sampai besok ketika [aunt] Denise datang dan Anda bisa pergi bersamanya."
    scene expression ("images/episode13/024_sad.webp") with dissolve
    charlotte "Aku tidak tahu. Saya tidak ingin keluar akhir -akhir ini. Saya tidak berumur 20 tahun."
    scene expression ("images/episode13/023_thinking.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}[mom!c] is hiding something. She looks sad.{/i}"
    scene expression ("images/episode13/023_curious.webp") with dissolve
    toby "Anda baru saja mengatakan bahwa Anda rindu keluar."
    scene expression ("images/episode13/024_sad.webp") with dissolve
    charlotte "Saya berbohong. Saya baru saja berbicara kecil."
    scene expression ("images/episode13/023_normal.webp") with dissolve
    toby "Tahukah Anda bagaimana Anda bisa tahu kapan Tris berbohong hanya dengan menatapnya? Yah, dia jelas mendapatkannya dari Anda."
    scene expression ("images/episode13/024_awkward.webp") with dissolve
    charlotte "Saya bukan pembohong yang buruk."
    scene expression ("images/episode13/023_laugh.webp") with dissolve
    toby "So are you admitting you lied about \"I don't wanna go to the gym\", or \"I don't feel like going out\"?"
    scene expression ("images/episode13/024_normal.webp") with dissolve
    charlotte "Usaha yang bagus. Saya tidak ingin melakukan salah satu dari hal -hal itu, jadi tolong berhenti mengganggu saya tentang ini."
    scene expression ("images/episode13/023_thinking.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Something is definitely up with her. She's not usually like this.{/i}"
    scene expression ("images/episode13/025_1.webp") with dissolve
    charlotte "Di Sini. Makanlah makanan Anda dan pergi ke gym. Anda sudah memiliki terlalu banyak energi pagi ini."
    scene expression ("images/episode13/025_2.webp") with dissolve
    toby "Terima kasih untuk sarapan."
    scene expression ("images/episode13/026_1.webp") with dissolve
    charlotte "Jadi, apa rencanamu hari ini?"
    scene expression ("images/episode13/026_2.webp") with dissolve
    toby "Nah, pagi ini bos saya mengirim sms kepada saya untuk tidak membuat rencana untuk malam ini karena ternyata ada banyak hal yang harus dilakukan. Jadi saya kira saya akan pergi ke gym, lalu bunuh waktu dan setelah itu hanya pergi bekerja. Tidak banyak."
    toby "Bagaimana denganmu?"
    scene expression ("images/episode13/026_1.webp") with dissolve
    charlotte "Nah hari saya hampir sama. Aku hanya ..."
    $ progress = 170
    play sound "audio/fx/Cell Phone Ring Sound Effect - Free Sound Effects.mp3"
    scene expression ("images/episode13/027.webp") with dissolve
    charlotte "Saya harus mengambil ini. Ini adalah [aunt] Anda."
    scene expression ("images/episode13/028.webp") with dissolve
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nWell, hello to you too, dear [sister]."
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nI just made some breakfast for [toby!c]."
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nYeah, he's right here. Wanna talk to him?"
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"

    if denise_path:
        charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nHe is not."
        charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
        charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nFine, I'll tell him."
        charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
        scene expression ("images/episode13/029.webp") with dissolve
        charlotte "[aunt] milikmu mengatakan \"Berhentilah memanjakan semua wanita di sekitarmu.\"
        scene expression ("images/episode13/030.webp") with dissolve
        toby "Katakan itu padanya \"I'm only memanjakan wanita yang pantas mendapatkannya.\"
        scene expression ("images/episode13/028.webp") with dissolve
        charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nHe claims he does it only for those of us who deserve it."
        charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    else:
        scene expression ("images/episode13/029.webp") with dissolve
        charlotte "Anda [aunt] mengatakan \"Hai.\"
        scene expression ("images/episode13/030.webp") with dissolve
        toby "Hai [auntie]."
        scene expression ("images/episode13/028.webp") with dissolve

    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nReally? Do I have to?"
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nYou and your secrets. He can't hear what you're saying."
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    scene expression ("images/episode13/031.webp") with dissolve
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nFine... I'l go upstairs."
    charlotte "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n{i}...{/i}"
    scene expression ("images/episode13/032.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I want to know what they're talking about. Maybe later I'll try to convince [mom] to tell me what they're talking about.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Wait....Stop it. I sound like an old lady who needs to know everything.{/i}"
    scene expression ("images/episode13/033.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Hmmm... Speaking of secrets. Maybe I could take a quick look at what [mom] was doing on her laptop.{/i}"
    if charlotte_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe I was wrong and she wasn't working on her book, but looking at porn. That could be interesting.{/i}"
    scene expression ("images/episode13/034.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see what you're hiding here, [mom].{/i}"
    scene expression ("images/episode13/035.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This isn't even close to what I was expecting. Is she looking for a job?{/i}"
    if patricia_path:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... That's right. Tris mentioned yesterday that [mom] doesn't have any money left.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But why would she look for a job?{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm earning plenty of money to help her out.{/i}"
    scene expression ("images/episode13/036.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Is this why she doesn't want to come with me to the gym and why she won't go out?{/i}"
    $ progress = 171
    scene expression ("images/episode13/037.webp") with dissolve
    charlotte "Menurut Anda apa yang Anda lakukan?"
    scene expression ("images/episode13/038.webp") with dissolve
    toby "Mengapa Anda mencari pekerjaan? Jika Anda membutuhkan uang, beri tahu saya dan saya akan membantu Anda. Anda sudah cukup bekerja. Giliran saya untuk membantu Anda."
    scene expression ("images/episode13/039.webp") with dissolve
    charlotte "Tidakkah kamu tahu itu tidak baik untuk menempelkan hidungmu di mana itu bukan milik? Dan bagaimana Anda tahu kata sandi saya?"
    scene expression ("images/episode13/040.webp") with dissolve
    toby "Tolong, saya selalu berpikir bahwa saya adalah favorit Anda [child], tetapi saya tidak berpikir Anda akan begitu berani tentang hal itu untuk menggunakan nama saya sebagai kata sandi Anda."
    scene expression ("images/episode13/041.webp") with dissolve
    charlotte "Saya seharusnya tidak perlu melindungi kata sandi komputer saya, karena Anda harus tahu lebih baik daripada mengintip dalam hal saya. Jadi? Mau jelaskan?"
    scene expression ("images/episode13/042.webp") with dissolve
    toby "Lihat [mom], saya minta maaf saya mengintip di laptop Anda, tapi bukan itu yang penting saat ini. Tris membutuhkanmu. Jika Anda mendapatkan pekerjaan, Anda akan berada di sekitar. Dia masih muda."
    charlotte "Jangan mengubah topik pembicaraan, anak muda. Berapa lama Anda tahu kata sandi saya? Apakah ini pertama kalinya Anda mengintip di komputer saya?"
    toby "Jika Anda membutuhkan uang, tanyakan saja kepada saya."
    charlotte "Bukan itu yang saya minta."
    scene expression ("images/episode13/043.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I hate to lie to you [mom], but ...{/i}"
    toby "Ya, ini pertama kalinya. Saya mencoba nama Tris dan kemudian milik saya. Saya ingin tahu mengapa Anda menjadi sangat takut pagi ini."
    scene expression ("images/episode13/044_normal.webp") with dissolve
    toby "Jadi, sekarang kembali ke masalah kita yang sebenarnya. Mengapa Anda tidak memberi tahu saya bahwa Anda memiliki masalah uang?"
    if charlotte_path:
        scene expression ("images/episode13/045_curious.webp") with dissolve
        charlotte "Jadi Anda tidak melihat hal lain?"
        scene expression ("images/episode13/044_thinking.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}If by \"something else\"Maksud Anda, buku Anda di mana Anda berfantasi tentang seorang pria muda yang memiliki nama yang sama dengan saya, ya, ya, ya saya melihatnya. {/i}"
        scene expression ("images/episode13/044_sad.webp") with dissolve
        toby "Tidak, [mom]. Saya tidak melihat hal lain, jadi tolong berhenti menghindari pertanyaan dan beri tahu saya. Mengapa Anda tidak memberi tahu saya bahwa Anda memiliki masalah uang?"

    scene expression ("images/episode13/045_normal.webp") with dissolve
    charlotte "Karena saya seorang wanita yang cerdas dan mandiri yang dapat melakukan apa pun yang diinginkannya, tidak peduli apa yang dipikirkan suaminya atau [son]. Saya akan mendapatkan pekerjaan."

    scene expression ("images/episode13/046.webp") with dissolve
    if charlotte_path:
        toby "Apakah Anda benar -benar akan memainkan kartu itu dengan saya? Lagipula kita sudah lalu? Kita berdua tahu bahwa hubungan kita jauh melewati hal [mother]-[son]."
        toby "Jadi saya tidak tahu mengapa Anda begitu memusuhi saya. Ini tidak ada hubungannya tentang Anda yang tidak pintar atau mandiri, atau apa pun."
        if toby_job == 0:
            toby "Anda tahu bahwa saya mencintai dan menghormati Anda."
        else:
            toby "Anda tahu bahwa saya mencintai dan menghormati Anda, jadi jika Anda menginginkan ini, apa pun ini untuk melanjutkan, saya sarankan Anda mulai jujur kepada saya."
    else:
        toby "Sungguh, [mom]? Apakah Anda benar -benar akan memainkan kartu itu dengan saya?"
        if toby_job == 0:
            toby "Anda tahu betapa saya mencintai dan menghormati Anda."
        else:
            toby "Anda tahu betapa saya mencintai dan menghormati Anda, jadi jangan pernah membandingkan saya dengan [dad]."
    scene expression ("images/episode13/045_sad.webp") with dissolve
    charlotte "Saya minta maaf, sayang. Aku tidak bermaksud membuatmu kesal. Tetapi Anda harus mengerti bahwa saya tidak dapat meminta uang. Bukan tanggung jawab Anda untuk membantu saya."
    scene expression ("images/episode13/044_normal.webp") with dissolve
    toby "Tapi saya ingin membantu Anda."
    scene expression ("images/episode13/045_sad.webp") with dissolve
    charlotte "Sungguh luar biasa bahwa Anda menghasilkan banyak uang, tetapi pada akhirnya Anda akan menemukan seseorang dan memutuskan untuk pindah bersama.Sayang. Anda masih muda. Anda memiliki seluruh hidup Anda di depan Anda."
    scene expression ("images/episode13/045_normal.webp") with dissolve
    charlotte "Atau mungkin Anda hanya akan memutuskan untuk pindah dan memulai hidup Anda sendiri sebagai orang dewasa. Saya tidak ingin menyeret Anda ke bawah. Waktunya akan tiba ketika Anda ingin membeli mobil, rumah, sesuatu. Menjadi muda itu mahal."
    scene expression ("images/episode13/045_kind.webp") with dissolve
    charlotte "Saya sangat senang bahwa Anda tumbuh menjadi pemuda independen ini yang memiliki gaji yang baik dan semuanya, tetapi saya juga memiliki [daughter] yang masih perlu saya dukung secara finansial."
    scene expression ("images/episode13/045_sad.webp") with dissolve
    charlotte "Adalah tugas saya untuk memberinya semua yang dia butuhkan. Saya tidak ingin dia merasa selama satu detik bahwa saya tidak bisa memberikan apa yang dia butuhkan."
    scene expression ("images/episode13/045_normal.webp") with dissolve
    charlotte "Saya tidak ingin dia keluar kuliah hanya karena saya tidak dapat lagi mendukungnya secara finansial."
    scene expression ("images/episode13/044_sad.webp") with dissolve
    toby "Lihat, [mom]. Saya mengerti, tetapi Tris juga memiliki [father]. Itu juga tanggung jawabnya dan selain itu, saya ingat Anda meletakkan uang di samping untuk kuliahnya."
    scene expression ("images/episode13/045_angry.webp") with dissolve
    charlotte "What [father]? What responsibility? Ever since we moved here neither I nor Tris have seen one cent from him. Everything he earns, he \"INVESTS\"di crypto atau apa pun."
    scene expression ("images/episode13/044_angry.webp") with dissolve
    toby "Dia belum memberi Anda uang sama sekali?"
    scene expression ("images/episode13/045_angry.webp") with dissolve
    charlotte "Tidak. Tidak satu sen pun."
    scene expression ("images/episode13/045_sad.webp") with dissolve
    charlotte "Jadi hari ini saya harus meminjam dari dana perguruan tinggi Tris \ sehingga saya dapat membeli bahan makanan.Kami telah hidup dengan uang yang saya tabung. Tapi coba tebak? Minggu lalu saya menghabiskan yang terakhir dan sekarang saya tidak punya uang untuk membeli bahan makanan."
    scene expression ("images/episode13/045_normal.webp") with dissolve
    charlotte "Sekarang Anda mengerti mengapa saya perlu mendapatkan pekerjaan? Atau setidaknya mencoba mendapatkannya ... karena coba tebak?"
    scene expression ("images/episode13/044_sad.webp") with dissolve
    toby "Apa?"
    scene expression ("images/episode13/045_sad.webp") with dissolve
    charlotte "Saya tidak memenuhi syarat untuk apa pun dan saya sudah terlalu tua. Saya menikah muda dan [father] Anda tidak pernah membiarkan saya bekerja, jadi saya tidak punya pengalaman."
    scene expression ("images/episode13/044_normal.webp") with dissolve
    toby "Itulah mengapa Anda harus membiarkan saya membantu Anda."
    scene expression ("images/episode13/045_normal.webp") with dissolve
    charlotte "Saya tidak bisa mengambil uang Anda.TIDAK! Ini uang Anda. Anda mendapatkannya."
    scene expression ("images/episode13/044_curious.webp") with dissolve
    toby "Tetapi Anda dapat mengambil uang Tris?"
    scene expression ("images/episode13/045_sad.webp") with dissolve
    charlotte "Anda membuat saya kotor sekarang. Anda tahu itu, kan?"
    scene expression ("images/episode13/044_normal.webp") with dissolve
    toby "Nah, saya benar."
    scene expression ("images/episode13/045_normal.webp") with dissolve
    charlotte "Saya akan mendapatkan pekerjaan dan mengembalikannya. Tahun pertamanya kuliah sudah dibayar penuh. Sebelum dia membutuhkan sisanya, aku akan mendapatkan pekerjaan dan mengembalikannya."
    scene expression ("images/episode13/044_sad.webp") with dissolve
    toby "Dengar, aku tidak bisa menghentikanmu bekerja. Saya memahami situasi Anda, tetapi setidaknya biarkan saya membantu Anda sampai Anda mendapatkan pekerjaan."
    scene expression ("images/episode13/045_sad.webp") with dissolve
    charlotte "Jenis [mother] apa yang akan saya lakukan jika saya menerima uang dari [children] saya?"
    scene expression ("images/episode13/044_smile.webp") with dissolve
    toby "Sama sekali tidak ada yang salah dengan Anda mengambil uang dari saya."
    scene expression ("images/episode13/045_curious.webp") with dissolve
    charlotte "Baik, tapi hanya sampai saya mendapatkan pekerjaan."
    scene expression ("images/episode13/044_laugh.webp") with dissolve
    toby "Ya Tuhan, kamu bangga."
    scene expression ("images/episode13/047.webp") with dissolve
    charlotte "Oh, percayalah. Pride bukan satu -satunya alasan bagi saya tidak ingin mengambil uang dari Anda."
    if charlotte_path:
        toby "Aku mencintaimu, [mom]."
        show ep13_048
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode13/048.webp") with dissolve
        hide ep13_048
        $ unlockImage(persistent.charlotte_22)
        charlotte "Aku juga mencintaimu, sayang."
        scene expression ("images/episode13/049.webp") with dissolve
        charlotte "Anda anak yang baik. Anda tahu itu, kan?"
        toby "Saya akan melakukan apa saja untuk Anda, [mom]."
        charlotte "Aku tahu itu, sayang."
    else:
        toby "Aku mencintaimu [mom]."
        charlotte "Aku juga mencintaimu, sayang."
        scene expression ("images/episode13/049.webp") with dissolve
        charlotte "Anda anak yang baik. Anda tahu itu, kan?"
        toby "Saya akan melakukan apa saja untuk Anda, [mom]."
        charlotte "Aku tahu itu, sayang."

    scene expression ("images/episode13/044_smile.webp") with dissolve
    toby "Oke, jadi berapa banyak yang Anda butuhkan?"
    scene expression ("images/episode13/045_laugh.webp") with dissolve
    charlotte "Nah, pertama -tama saya ingin Anda menyelesaikan sarapan Anda, karena sudah dingin, maka saya ingin Anda ikut dengan saya ke toko kelontong."
    scene expression ("images/episode13/044_smile.webp") with dissolve
    toby "Bukan itu yang saya minta. Saya bertanya berapa banyak uang yang Anda butuhkan?"
    scene expression ("images/episode13/045_kind.webp") with dissolve
    charlotte "Oh, tidak. Bukan itu cara kerjanya. Saya akan menerima bantuan Anda, tetapi saya tidak akan menyentuh uang Anda. Anda ikut dengan saya dan membayar apa yang kami butuhkan."
    scene expression ("images/episode13/044_smile.webp") with dissolve
    toby "Jangan konyol. Anda memberi tahu saya betapa Anda membutuhkan atau saya hanya akan menebak."
    scene expression ("images/episode13/045_laugh.webp") with dissolve
    charlotte "Anda akan menjadi menyakitkan di pantat saya tentang ini, bukan?"
    scene expression ("images/episode13/044_laugh.webp") with dissolve
    toby "Ya."
    scene expression ("images/episode13/045_normal.webp") with dissolve
    charlotte "Oke, 0 seharusnya cukup untuk minggu ini."
    scene expression ("images/episode13/044_laugh.webp") with dissolve
    toby "Seperti neraka yang cukup. Saya memberi Anda 00."
    scene expression ("images/episode13/045_normal.webp") with dissolve
    charlotte "Bahasa, anak muda! Saya menyadari Anda adalah pria di rumah sekarang, tetapi saya masih Anda [mother] dan begitu saya mendapatkan pekerjaan, saya akan mengambil kembali peran saya sebagai penyedia untuk keluarga ini."
    scene expression ("images/episode13/044_smile.webp") with dissolve
    toby "Tuhan, kamu tidak ada harapan."
    scene expression ("images/episode13/045_normal.webp") with dissolve
    charlotte "Potong, potong! Selesaikan sarapan Anda, karena kami punya bahan makanan!"
    scene expression ("images/episode13/044_curious.webp") with dissolve
    toby "Saya pikir Anda mengatakan Anda mengambil uang itu?"
    scene expression ("images/episode13/045_smile.webp") with dissolve
    charlotte "Ya, tapi [father] Anda mengambil mobil dan saya tidak bisa membawa tas sendiri."
    scene expression ("images/episode13/044_curious.webp") with dissolve
    toby "Jadi kami akan mengambil sepeda saya?"
    scene expression ("images/episode13/045_laugh.webp") with dissolve
    charlotte "Ya, oke. Anda mengemudi dan saya akan memegang tas di tangan saya."
    scene expression ("images/episode13/044_laugh.webp") with dissolve
    toby "Ya. Itu bukan ide yang bagus."
    scene expression ("images/episode13/044_smile.webp") with dissolve
    toby "Aku akan memberimu taksi kalau begitu."
    scene expression ("images/episode13/050.webp") with dissolve
    charlotte "Tidak. Kami berjalan kaki. Anda terlihat seperti dapat menangani dua tas dan baik -baik saja, saya bisa menggunakan kardio."
    toby "Jika Anda ingin melakukan kardio, maka datanglah ke gym dengan saya."
    charlotte "Cukup buruk, saya mengambil uang dari Anda untuk bahan makanan."
    scene expression ("images/episode13/051.webp") with dissolve
    charlotte "Jadi selesaikan sarapan Anda dan biarkan pergi."
    toby "Bagus!"

    return

label episode13_groceries:
    $ progress = 172

    if charlotte_path:
        scene expression ("images/episode13/052.webp") with fade
        charlotte "Jadi, apakah Anda yakin tidak melihat hal lain di komputer saya?"
        toby "Tidak. Saya hanya melihat daftar pekerjaan."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}That's the only thing I saw...today.{/i}"
        toby "Kenapa kamu bertanya? Apakah Anda memiliki beberapa kerangka di lemari Anda?"
        scene expression ("images/episode13/053.webp") with dissolve
        charlotte "Anda bisa mengatakan itu."
        charlotte "Jadi apa yang ingin Anda makan begitu Anda pulang kerja? Karena itu uang Anda, hanya adil untuk bertanya kepada Anda."
        scene expression ("images/episode13/054.webp") with dissolve
        toby "Apakah bibir Anda ada di menu malam ini?"
        scene expression ("images/episode13/055.webp") with dissolve
        charlotte "[toby!u]! ... apakah kamu gila? Bagaimana jika seseorang mendengarmu?"
        scene expression ("images/episode13/054.webp") with dissolve
        toby "Tidak ada yang mengenal kami di sini. Tidak ada yang tahu Anda [mother] saya."
        scene expression ("images/episode13/055.webp") with dissolve
        charlotte "Lihatlah perbedaan usia di antara kita, siapa lagi yang bisa saya lakukan?"
        scene expression ("images/episode13/054.webp") with dissolve
        toby "Pertama -tama, Anda terlihat hebat. Siapa bilang kamu tidak bisa menjadi pacarku?"
        scene expression ("images/episode13/056.webp") with dissolve
        charlotte "Saya suka pujian Anda, tetapi jujur saja, tidak ada yang akan percaya itu."
        scene expression ("images/episode13/057.webp") with dissolve
        toby "Ambil tanganku dan kamu akan melihat bahwa tidak ada yang akan mengawasi kita. Sangat normal bagi seorang pria muda untuk tertarik pada wanita yang lebih dewasa."
        charlotte "Saya tidak melakukan itu! Anda terlalu gila untuk kebaikan Anda sendiri."
        toby "Ayo, coba saja. Kami akan membayar bahan makanan kami dan kemudian ketika kami meninggalkan toko, saya akan mengambil tangan Anda dan Anda melihat kasir. Anda akan melihat bahwa dia tidak akan peduli."
        scene expression ("images/episode13/058.webp") with dissolve
        charlotte "Dan bagaimana jika dia melakukannya?"
        toby "Lalu itu masalahnya."
        charlotte "Dan kemudian masalah Anda akan membersihkan rumah selama seminggu."
        scene expression ("images/episode13/059.webp") with dissolve
        toby "Tidak cukup bahwa saya menyediakan uang untuk rumah, sekarang saya harus melakukan pembersihan juga?"
        charlotte "Saya minta maaf, saya ..."
        toby "Saya bercanda, [mom]."
        charlotte "Anda tidak bisa bercanda tentang itu, [toby!c]. Anda tahu betapa buruknya saya mengambil uang dari Anda. Anda tidak bisa melemparkannya ke wajah saya."
        scene expression ("images/episode13/060.webp") with dissolve
        toby "Saya minta maaf tentang itu. Itu tidak akan terjadi lagi."
        charlotte "Tetapi Anda benar, tidak adil bahwa Anda harus membersihkan rumah karena Anda melakukan banyak hal untuk kami. Itu yang paling tidak bisa saya lakukan."
        scene expression ("images/episode13/061.webp") with dissolve
        toby "Ayo ... mari kita periksa dan mainkan game kami. Jika kasir menatap kami dengan cara apa pun, saya akan membersihkan rumah selama seminggu dan jika tidak, Anda harus tidur di kamar saya selama seminggu."
        charlotte "Taruhan itu tidak adil. Saya menang dalam kedua situasi."
        scene expression ("images/episode13/062.webp") with dissolve
        toby "Jadi, sayang, apa yang ingin Anda lakukan saat kita pulang?"
        charlotte "Umm ..."
        scene expression ("images/episode13/064.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode13/063.webp") with dissolve
        charlotte "Aku tidak tahu. Mungkin nongkrong di bak mandi air panas?"
        if toby_job == 0:
            toby "Sempurna. Saya suka melihat Anda di bikini Anda."
        else:
            toby "Sempurna. Tidak bisa menunggu untuk melihat Anda di bikini yang saya beli untuk ulang tahun kami."
        $ unlockImage(persistent.charlotte_23)
        scene expression ("images/episode13/065.webp") with dissolve
        charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}[toby!c]...{/i}"
        scene expression ("images/episode13/066.webp") with dissolve
        cashier "Itu akan menjadi 7.66."
        scene expression ("images/episode13/067.webp") with dissolve
        toby "Izinkan aku, sayang."
        charlotte "Terima kasih."
        scene expression ("images/episode13/068.webp") with dissolve
        cashier "Kalian berdua menjadi pasangan yang hebat. Hampir tidak adil bagi pasangan lain untuk melihat seberapa baik Anda terlihat bersama."
        scene expression ("images/episode13/067.webp") with dissolve
        toby "Kenapa, terima kasih banyak. Anda tidak tahu seberapa besar artinya bagi kami."
        scene expression ("images/episode13/069.webp") with dissolve
        toby "Mari pulang, sayang. Saya punya beberapa ide untuk krim kocok yang baru saja kami beli."
        charlotte "Tuhan, [toby!c]! Anda akan menjadi kematian saya."
        scene expression ("images/episode13/070.webp") with dissolve
        toby "Melihat? Aku sudah memberitahumu? Dia bahkan tidak berpikir sejenak bahwa Anda bisa menjadi [mother] saya."
        charlotte "Baik, Anda benar. Mungkin saya terlihat cukup baik untuk usia saya."
        scene expression ("images/episode13/071.webp") with dissolve
        $ ui.pausebehavior(0.5)
        $ ui.saybehavior()
        $ ui.interact()
        scene expression ("images/episode13/072.webp") with dissolve
        toby "Salah! Anda terlihat bagus dan itu."
        scene expression ("images/episode13/073.webp") with dissolve
        charlotte "Apakah Anda baru saja menampar pantat saya?"
        toby "Itulah yang Anda dapatkan karena berbicara omong kosong. Apakah Anda ingat bagaimana ketika saya masih kecil Anda akan memukul saya karena bersumpah? Saya baru saja membalas budi."
        charlotte "Pacar yang berpura -pura ini telah pergi ke kepala Anda."
        scene expression ("images/episode13/074.webp") with dissolve
        charlotte "Di sini ... ambil yang ini juga. Anda tidak dapat dipercaya dengan tangan kosong."
        scene expression ("images/episode13/075.webp") with fade
        toby "Jadi bagaimana cardio Anda? Melihat bagaimana saya membawa semua tas?"
    else:

        scene expression ("images/episode13/075.webp") with fade
        toby "Jadi bagaimana kabarmu dengan kalori?"

    scene expression ("images/episode13/076.webp") with dissolve
    charlotte "Mengapa semua orang peduli dengan kalori saya hari ini? Apakah saya benar -benar gemuk?"
    toby "Jangan berani -berani menaruh ini padaku. Saya ingin naik taksi, tetapi Anda mengatakan ingin membakar beberapa kalori, sehingga Anda tidak dapat mempermainkan korban kali ini."
    toby "Saya dan tangan saya adalah satu -satunya korban di sini."
    scene expression ("images/episode13/077.webp") with dissolve
    charlotte "Apakah tasnya benar -benar berat?"
    toby "Ini baik -baik saja. Mereka tidak seburuk itu."
    toby "But you need to tell me who else picked on you about your \"calories\"Hari ini?"
    scene expression ("images/episode13/078.webp") with dissolve
    charlotte "Bukan siapa-siapa."
    toby "Anda baru saja mengatakan bahwa semua orang memilih Anda tentang kalori Anda hari ini, jadi siapa?"
    charlotte "Itu Denise! Apakah Anda ingin tahu tentang semua hal rahasia itu?"
    toby "Ya, saya sudah penasaran."
    scene expression ("images/episode13/079.webp") with dissolve
    charlotte "Itu adalah tipu muslihat yang bodoh untuk membuatku naik ke atas hanya demi kalori yang terbakar. Dia mengatakan bahwa ketika dia tiba besok kita pergi keluar jadi aku harus bugar."
    toby "Maaf saya tertawa, tapi saya tidak percaya Anda jatuh cinta untuk itu."
    charlotte "Jika Anda tidak berhenti tertawa, saya akan memukul Anda di sini di tengah jalan."
    if charlotte_path:
        scene expression ("images/episode13/080.webp") with dissolve
        toby "Hati -hati, sayang. Kami tidak ingin didenda untuk PDA."
        charlotte "Tampilan kasih sayang publik? Apakah Anda bercanda? Memukul adalah hukuman Anda bukan kasih sayang."
        toby "Anda dapat mengubah pukulan dalam apa pun yang Anda inginkan. Hukuman, kesenangan, pada dasarnya tidak terbatas."
    else:
        scene expression ("images/episode13/080.webp") with dissolve
        toby "Saya menelepon Layanan Perlindungan Anak dan mereka akan mengambil saya dari Anda. Lalu siapa yang akan membawa tas Anda?"
        charlotte "Haruskah saya memanggil mereka sendiri, karena tangan Anda penuh membawa tas?"
        toby "Menggertak."
    scene expression ("images/episode13/081.webp") with dissolve
    charlotte "Ayo, biarkan lebih cepat. Saya tidak akan membakar kalori yang cukup dengan kecepatan ini."
    toby "Lalu datanglah ke gym bersamaku setelah itu."
    charlotte "Mengapa saya ingin pergi ke gym ketika saya memiliki semua yang saya butuhkan di rumah? Jika saya pergi ke gym, saya hanya akan menggunakan treadmill. Jadi itu uang yang terbuang."
    scene expression ("images/episode13/082.webp") with dissolve
    toby "Benar -benar Denise tidak bisa mengolok -olok Anda lagi. Yang saya minta hanyalah satu bulan. Saya akan melatih Anda dan jika Anda tidak melihat kemajuan apa pun setelah sebulan, saya akan berhenti mengganggu Anda."
    charlotte "Oke baik -baik saja. Saya akan datang jika itu penting bagi Anda untuk membawa [mommy] Anda ke gym."
    charlotte "Aku tidak tahu di mana aku salah denganmu. Anda berusia 20 tahun dan masih tidak bisa pergi ke mana pun tanpa saya."
    toby "Ha, ha, sangat lucu. Lelucon kecil itu akan dikenakan biaya."
    toby "Saya harap Anda tidak punya rencana malam ini, karena ketika Anda pulang, Anda akan sangat sakit, Anda tidak akan bisa turun dari sofa."

    scene expression ("images/episode13/083.webp") with fade
    toby "Oke, jadi mari kita turunkan bahan makanan dan pergi ke gym."
    charlotte "Kedengarannya seperti rencana."

    return

label episode13_gym_reception:
    $ progress = 173
    scene expression ("images/episode13/084.webp") with dissolve:
        moveUp
    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode13/085.webp") with dissolve:
        moveRight

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode13/086.webp") with dissolve:
        moveDown

    $ ui.pausebehavior(9.3)
    $ ui.saybehavior()
    $ ui.interact()




    scene expression ("images/episode13/087.webp") with fade
    charlotte "Anda benar -benar perlu mendapatkan helm. Itu tidak aman."
    toby "Jangan khawatir, saya akan membeli mobil dan kemudian saya tidak akan membutuhkan helm."
    scene expression ("images/episode13/088.webp") with dissolve
    charlotte "Anda berencana membeli mobil? Itu bagus! Tahukah Anda mobil apa yang Anda inginkan?"
    toby "Yah, saya berpikir mungkin sesuatu yang dapat dikonversi."
    charlotte "Jadi Anda masih membutuhkan helm."
    scene expression ("images/episode13/089_2.webp") with dissolve
    toby "Benar-benar? Anda ingin membuat saya memakai helm di dalam mobil?"
    scene expression ("images/episode13/089_1.webp") with dissolve
    charlotte "Hanya saat bagian atasnya turun."
    scene expression ("images/episode13/089_2.webp") with dissolve
    toby "Terlalu protektif?"
    scene expression ("images/episode13/090.webp") with dissolve
    charlotte "Saya melindungi sumber pendapatan saya."
    toby "Penggali emas."
    charlotte "Ayo, sayang. Anda memiliki keanggotaan gym untuk membelikan saya."
    scene expression ("images/episode13/091.webp") with dissolve
    if charlotte_path:
        toby "Halo. Saya ingin mendapatkan keanggotaan untuk gadis saya, di sini."
    else:
        toby "Halo. Saya ingin mendapatkan keanggotaan."
    scene expression ("images/episode13/092.webp") with dissolve
    cashier "Hai, [toby!c]. Selamat Datang kembali. Saya akan senang membantu. Bolehkah saya mendapatkan ID?"
    if charlotte_path:
        scene expression ("images/episode13/093.webp") with dissolve
    else:
        scene expression ("images/episode13/094.webp") with dissolve
    charlotte "Tentu saja. Ini dia."

    if charlotte_path:
        scene expression ("images/episode13/095.webp") with dissolve
        charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Are you out of your mind? What's wrong with you? The girlfriend game is not going to work here. What if she notices our last name? What do you think she'll say?{/i}"
        toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}You think too much. Don't worry.{/i}"
        toby "Jadi? Bagaimana menurutmu? Anda suka gym?"
    else:
        pass
    scene expression ("images/episode13/096.webp") with dissolve
    charlotte "Kamu benar. Gymnya nyaman. Saya pikir saya akan suka di sini."

    scene expression ("images/episode13/097.webp") with dissolve
    if charlotte_path:
        cashier "Ini kartu Anda. Saya yakin suami Anda memberi tahu Anda semua yang perlu diketahui tentang fasilitas kami, tetapi jika Anda memiliki pertanyaan lain, beri tahu saya."
        scene expression ("images/episode13/098.webp") with dissolve
        charlotte "Saya ... umm ... ya, dia melakukannya."
    else:
        cashier "Ini kartu Anda. Saya yakin [toby!c] memberi tahu Anda semua yang perlu diketahui tentang fasilitas kami, tetapi jika Anda memiliki pertanyaan lain, beri tahu saya."

    scene expression ("images/episode13/099.webp") with dissolve
    charlotte "Terima kasih!"

    if charlotte_path:
        scene expression ("images/episode13/100.webp") with dissolve
        toby "Ayo, istri. Mari kita berubah."
        scene expression ("images/episode13/102.webp") with dissolve
        charlotte "Tuhan, [toby!c]. Apa yang salah denganmu? Saya tidak ingat menjatuhkan Anda di kepala Anda saat Anda masih kecil."
        toby "Anda perlu belajar cara bersenang -senang."
        charlotte "Saya tahu cara bersenang -senang."
        toby "Tidak, Anda tidak. Anda terlalu tegang dan Anda terlalu peduli tentang apa yang dipikirkan orang lain."
        scene expression ("images/episode13/103.webp") with dissolve
        charlotte "Gadis itu ke sesuatu ketika dia melihat ID saya."
        toby "Yah, dia pikir kamu adalah istriku. Tidak ada yang salah dengan itu. Seperti yang saya katakan, tidak ada yang mencurigai Anda [mother] saya. Jadi Anda harus belajar bagaimana bersenang -senang."
    else:
        scene expression ("images/episode13/101.webp") with dissolve
        toby "Ayo. Mari kita berubah."

    charlotte "Bagus. Jadi di mana ruang ganti wanita?"
    scene expression ("images/episode13/104.webp") with dissolve
    toby "Ya. Tentang itu. Gym kehilangan gugatan beberapa saat yang lalu, hanya karena beberapa pemilik Dick ingin berganti di ruang ganti wanita dan mereka kalah, jadi sekarang gym telah berbagi ruang ganti."
    charlotte "Saya tidak percaya Anda meyakinkan saya untuk bergabung dengan gym dengan ruang ganti bersama."
    scene expression ("images/episode13/105.webp") with dissolve
    toby "Jangan khawatir, wanita mendapatkan kunci untuk sisi jauh ruang ganti."
    toby "Jadi mari kita berubah."
    $ progress = 174
    if charlotte_path:
        label memory_46:


            scene expression ("images/episode13/106.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Wait, why did she give me a new locker key? I don't see that number here.{/i}"
            scene expression ("images/episode13/107.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Don't tell me it's in the women's section...{/i}"
            scene expression ("images/episode13/108.webp") with dissolve:
                moveUp

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode13/109.webp") with dissolve
            charlotte "Apa yang kamu lakukan di sini, [toby!c]? Saya pikir Anda mengatakan bahwa pria mendapatkan loker di bagian lain."
            toby "Nah, sepertinya loker saya tepat di sebelah Anda. Saya kira itulah yang terjadi pada pasangan yang sudah menikah."
            charlotte "Saya mulai menyesali ini."
            scene expression ("images/episode13/110.webp") with dissolve
            toby "Jangan khawatir, aku tidak akan melihat."
            charlotte "Janji?"
            toby "Sangat."
            scene expression ("images/episode13/111.webp") with dissolve:
                horizontalLoop
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode13/112.webp") with dissolve:
                verticalLoop
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode13/113.webp") with dissolve:
                horizontalLoop
            $ ui.saybehavior()
            $ ui.interact()
            $ unlockImage(persistent.charlotte_24)
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}God, [mom] looks so good, but a promise is a promise. I should stop looking.{/i}"
            scene expression ("images/episode13/114_0.webp") with fade:
                moveUp
            charlotte "Jadi? Haruskah kita?"

            $ unlockMemory(persistent.memory_46)
            $ renpy.end_replay()
    else:
        pass

    return

label episode13_gym_workout:
    $ progress = 175

    scene expression ("images/episode13/114.webp") with fade
    charlotte "Oke, jadi apa yang harus saya lakukan terlebih dahulu?"
    toby "Nah ada beberapa treadmill di dekat jendela. Anda harus melakukannya selama 10 menit dengan kecepatan sedang, tetapi sudut setinggi mungkin."
    scene expression ("images/episode13/115.webp") with dissolve
    sheila "Nah, halo! Lihat siapa yang memutuskan untuk muncul. Sepertinya selamanya sejak aku melihatmu."
    scene expression ("images/episode13/116.webp") with dissolve
    sheila "Dan dengan siapa kecantikan ini?"
    scene expression ("images/episode13/117.webp") with dissolve
    charlotte "Saya Charlotte. GI -nya ..."
    scene expression ("images/episode13/118.webp") with dissolve
    toby "[mother!c]. Dia adalah [mother] saya."
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit, shit, shit! She's a cop for fuck sake, she probably already knows she's my [mom]. Bad time to want to have fun.{/i}"
    scene expression ("images/episode13/119.webp") with dissolve
    sheila "Wow. Dengan serius? Saya tidak akan memberi Anda lebih dari 30."
    scene expression ("images/episode13/120.webp") with dissolve
    charlotte "Terima kasih."
    scene expression ("images/episode13/121.webp") with dissolve
    sheila "Saya Sheila. Apakah ini pertama kalinya Anda di sini?"
    scene expression ("images/episode13/120.webp") with dissolve
    charlotte "Ya. Saya baru saja mendapatkan keanggotaan."
    scene expression ("images/episode13/121.webp") with dissolve
    sheila "Itu bagus. Ikutlah denganku dan aku akan menunjukkan kepadamu. Saya adalah pelatih pribadi di sini. Saya bisa melatih Anda jika Anda mau."
    scene expression ("images/episode13/122.webp") with dissolve
    charlotte "Oh, kamu tidak harus, itu sebabnya aku punya [toby!c] di sini. Dia berjanji untuk melatih saya."
    scene expression ("images/episode13/123.webp") with dissolve
    sheila "Saya telah melihat [toby!c] melatih dan percayalah, dia tidak memiliki apa -apa untuk ditunjukkan kepada Anda."
    sheila "Tapi selain itu dia salah satu dari orang -orang terbaik di sekitar. Dia banyak membantu saya dengan sesuatu dan karena dia terlalu bangga membiarkan saya melatihnya, itu yang paling tidak bisa saya lakukan untuk membayarnya."
    charlotte "Um ... berapa banyak ..."
    sheila "Tolong, Anda [toby!c] \ 'S [mother]. Saya tidak pernah bisa mengambil uang Anda."
    charlotte "Terima kasih!"
    scene expression ("images/episode13/124.webp") with dissolve
    toby "Permisi? Saya tidak punya apa -apa untuk ditunjukkan padanya?"
    scene expression ("images/episode13/125.webp") with dissolve
    sheila "Melihat? Sudah kubilang dia terlalu bangga."
    charlotte "Jangan lihat aku. Akulah alasan dia salah satu dari orang -orang terbaik. Kesombongan berasal dari [father]."
    scene expression ("images/episode13/126.webp") with dissolve
    sheila "Aku mencintainya."
    sheila "Sekarang mengapa Anda tidak pergi dan melakukan pelatihan yang disebut Anda sementara para wanita berolahraga seperti pro nyata."
    scene expression ("images/episode13/127.webp") with dissolve
    charlotte "Bye, sayang!"
    scene expression ("images/episode13/128.webp") with dissolve
    toby "Nikmati hal yang mengikat otot wanita Anda."

    scene expression ("images/episode13/129.webp") with dissolve:
        horizontalLoop

    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode13/130.webp") with dissolve:
        horizontalLoop_reverse

    $ ui.saybehavior()
    $ ui.interact()

    if charlotte_path:
        scene expression ("images/episode13/131.webp") with dissolve:
            verticalLoop

        $ ui.saybehavior()
        $ ui.interact()

    if sheila_path:
        scene expression ("images/episode13/132.webp") with dissolve:
            verticalLoop

        $ ui.saybehavior()
        $ ui.interact()



    scene expression ("images/episode13/133.webp") with dissolve:
        horizontalLoop_reverse

    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode13/134.webp") with dissolve:
        horizontalLoop

    $ ui.saybehavior()
    $ ui.interact()

    if sheila_path:
        scene expression ("images/episode13/136.webp") with dissolve:
            verticalLoop

        $ ui.saybehavior()
        $ ui.interact()

    if charlotte_path:
        scene expression ("images/episode13/135.webp") with dissolve:
            horizontalLoop_reverse

        $ ui.saybehavior()
        $ ui.interact()

    scene expression ("images/episode13/137.webp") with dissolve:
        horizontalLoop

    $ ui.saybehavior()
    $ ui.interact()

    scene expression ("images/episode13/138.webp") with dissolve:
        verticalLoop

    $ ui.saybehavior()
    $ ui.interact()

    if charlotte_path:
        scene expression ("images/episode13/139.webp") with dissolve:
            verticalLoop

        $ ui.saybehavior()
        $ ui.interact()

    if sheila_path:
        scene expression ("images/episode13/140.webp") with dissolve:
            horizontalLoop

        $ ui.saybehavior()
        $ ui.interact()

    scene expression ("images/episode13/141.webp") with dissolve
    toby "Bagaimana kabarmu?"
    scene expression ("images/episode13/142.webp") with dissolve
    sheila "Anda sudah selesai?"
    scene expression ("images/episode13/141_2.webp") with dissolve
    toby "Nah, beberapa dari kita harus pergi bekerja. Tidak semua orang mampu bekerja hanya 4 jam sehari."
    scene expression ("images/episode13/143.webp") with dissolve
    charlotte "Kapan terakhir kali Anda bekerja lebih dari 4 jam?"
    scene expression ("images/episode13/144.webp") with dissolve
    toby "Hari ini adalah hari itu."
    scene expression ("images/episode13/142.webp") with dissolve
    sheila "Hanya empat lagi dan kami selesai."
    scene expression ("images/episode13/145.webp") with dissolve
    toby "Empat Apa? Jangan beri tahu saya empat seri lagi."
    scene expression ("images/episode13/146.webp") with dissolve
    sheila "Tiga."
    scene expression ("images/episode13/147.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode13/146.webp") with dissolve
    sheila "Dua."
    scene expression ("images/episode13/147.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode13/146.webp") with dissolve
    sheila "Satu."
    scene expression ("images/episode13/147.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode13/148.webp") with dissolve
    sheila "Kerja bagus, gadis. Anda luar biasa."
    scene expression ("images/episode13/149_1.webp") with dissolve
    charlotte "Saya merasakan sakit pada otot yang saya tidak tahu saya punya."
    scene expression ("images/episode13/149_2.webp") with dissolve
    sheila "Jangan khawatir, Anda akan merasa jauh lebih baik dalam beberapa hari."
    scene expression ("images/episode13/150.webp") with dissolve
    charlotte "Membantu wanita tua, bukan?"
    scene expression ("images/episode13/151.webp") with dissolve
    toby "Karena saya tidak melihat wanita tua, saya akan membantu Anda."
    scene expression ("images/episode13/152.webp") with dissolve
    sheila "Jadi? Sampai jumpa hari Rabu?"
    scene expression ("images/episode13/153.webp") with dissolve
    charlotte "Anda bertaruh!"
    charlotte "Dan terima kasih banyak untuk hari ini. Ini adalah pelatihan terbaik yang pernah saya miliki."
    scene expression ("images/episode13/152.webp") with dissolve
    sheila "Saya senang Anda menikmatinya."
    scene expression ("images/episode13/154.webp") with dissolve
    sheila "Aku akan membiarkanmu pulang sekarang. Sampai jumpa hari Rabu, dan jika Anda suka dilatih oleh saya, berhentilah mencoba memberi saya uang. Oke?"
    scene expression ("images/episode13/155_1.webp") with dissolve
    charlotte "Bagus."
    scene expression ("images/episode13/155_2.webp") with dissolve
    toby "Haruskah kita?"
    charlotte "Ya, tolong bawa aku pulang."
    scene expression ("images/episode13/156.webp") with dissolve
    charlotte "Bye, Sheila dan terima kasih banyak."
    scene expression ("images/episode13/157.webp") with dissolve
    sheila "Bye, Charlotte. Jika Anda membutuhkan sesuatu, minta saja [toby!c] untuk memberi Anda nomor saya."
    scene expression ("images/episode13/158.webp") with dissolve
    toby "Jadi? Bagaimana perasaanmu?"
    charlotte "Aku sudah mati. Jika setiap sesi pelatihan seperti ini, Denise akan mati karena kecemburuan dalam sebulan."
    toby "Saya senang Anda menyukainya."
    if charlotte_path:
        scene expression ("images/episode13/159_1.webp") with dissolve
    else:
        scene expression ("images/episode13/159_2.webp") with dissolve
    charlotte "Jadi? Apa cerita antara Anda dan Sheila?"
    toby "Tidak ada cerita. Saya hanya membantunya dengan sesuatu."
    charlotte "Oke, jangan beri tahu saya. Simpan rahasia Anda untuk diri sendiri."
    if charlotte_path:
        scene expression ("images/episode13/159_3.webp") with dissolve
        charlotte "Ngomong -ngomong, saya pikir Anda ingin saya bersenang -senang, namun ketika saya akan memperkenalkan diri sebagai pacar Anda, Anda menghentikan saya."
        toby "Dan saya menghentikan Anda karena dia mungkin tahu Anda [mom] saya. Kami hanya bersenang -senang dengan orang -orang yang tidak mengenal kami."
    scene expression ("images/episode13/160.webp") with dissolve
    toby "Ayo, mari kita mandi."
    charlotte "Tolong beritahu saya bahwa kami setidaknya memiliki beberapa tirai."
    toby "Tidak ada yang akan melihat Anda di kamar mandi.Ya, kita lakukan. Berhenti khawatir. Anda sudah melihat bahwa gym cukup kosong, terutama pada jam ini."
    charlotte "Ya, saya suka di sini."

    return

label episode13_gym_showers:
    $ progress = 176
    scene expression ("images/episode13/161.webp") with fade
    toby "Saya akan mengambil kios ini."
    scene expression ("images/episode13/162.webp") with dissolve
    charlotte "Saya akan mengambil yang berikutnya."
    scene expression ("images/episode13/163.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm going to take a shower, bring [mom] home and then I need to get to work.{/i}"
    if charlotte_path:
        label memory_47:
            if _in_replay:
                scene expression ("images/episode13/163.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Speaking of [mom], for some reason I find it very arousing that she's naked next to me with only a thin wall between us.{/i}"

            scene expression ("images/episode13/164.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's right there behind this wall, all naked with water drops on her beautiful, gorgeous naked body.{/i}"
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}How I wish I could see her.{/i}"
            scene expression ("images/episode13/165.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode13/166.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode13/167.webp") with dissolve
            charlotte "Sial ... lenganku sangat sakit. Saya bahkan tidak dapat menggunakannya dengan benar."
            charlotte "Sayang, saya menjatuhkan sampo saya dan saya tidak bisa mengambilnya. Apakah Anda pikir Anda dapat mengambilnya untuk saya?"
            scene expression ("images/episode13/168.webp") with dissolve
            toby "Tentu..."
            scene expression ("images/episode13/169.webp") with dissolve
            toby "Izinkan saya memeriksa untuk memastikan tidak ada yang ada di sekitar."
            scene expression ("images/episode13/170.webp") with dissolve
            charlotte "Anda sudah telanjang? Lalu jangan repot -repot. Saya akan menemukan cara untuk mengambilnya."
            scene expression ("images/episode13/171.webp") with dissolve
            toby "Terlambat. Saya sudah ada di sini."
            scene expression ("images/episode13/172.webp") with dissolve
            charlotte "Ya Tuhan, sakit hanya meregangkan lenganku."
            toby "Di Sini."
            scene expression ("images/episode13/173.webp") with dissolve
            toby "Apakah Anda membutuhkan sesuatu yang lain?"
            scene expression ("images/episode13/174.webp") with dissolve
            charlotte "Apa maksudmu?"
            scene expression ("images/episode13/175.webp") with dissolve
            toby "Nah, karena lengan Anda sangat sakit, apakah Anda membutuhkan saya untuk mencuci punggung?"
            scene expression ("images/episode13/174.webp") with dissolve
            charlotte "Anda tahu itu ide yang buruk bukan?"
            scene expression ("images/episode13/175.webp") with dissolve
            toby "Mungkin, tapi apakah Anda pikir Anda bisa mengatasinya?"
            scene expression ("images/episode13/176.webp") with dissolve
            charlotte "..."
            scene expression ("images/episode13/177.webp") with dissolve
            charlotte "Oke, tapi jangan mencoba sesuatu yang lucu. Anda mencuci punggung dan kemudian kembali ke kios Anda."
            scene expression ("images/episode13/178.webp") with dissolve
            toby "Tentu saja."
            scene expression ("images/episode13/179.webp") with dissolve:
                moveDown

            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode13/180.webp") with dissolve
            charlotte "Jika Anda selesai mengagumi pantat saya, sekarang akan menjadi saat yang tepat untuk mulai mencuci punggung saya."
            toby "Maaf, saya hanya ... Saya tidak bisa percaya betapa baiknya penampilan Anda."
            charlotte "Saya lupa memberi tahu Anda aturannya. Anda harus mencuci punggung dengan mata tertutup."
            scene expression ("images/episode13/181.webp") with dissolve
            toby "Akan tidak sopan bagi Anda untuk menutup mata saya."
            charlotte "Dan bernafsu pada tubuh saya bukanlah tidak sopan? Lagipula."
            scene expression ("images/episode13/182.webp") with dissolve
            toby "Apa yang membuatmu berpikir aku bernafsu pada tubuhmu?"
            charlotte "Anda tidak?"
            toby "Tidak. Saya baru saja mengurus bisnis saya sendiri."
            scene expression ("images/episode13/183.webp") with dissolve
            toby "Memastikan pantat Anda semuanya dibersihkan."
            charlotte "Ya, benar. Jadikan itu bagus dan mengkilap."
            toby "Itu rencananya."
            scene expression ("images/episode13/184.webp") with dissolve
            toby "Melihat? Tidak ada yang bernafsu setelah apapun."
            charlotte "Jadi maksud Anda bahwa jika saya mengambil langkah mundur, saya tidak akan merasakan sesuatu yang menyentuh pipi pantat saya?"
            scene expression ("images/episode13/185.webp") with dissolve
            toby "Tidak."
            charlotte "Aku tidak yakin mengapa, tapi aku tidak percaya padamu."
            toby "Kemudian cari tahu sendiri."
            scene expression ("images/episode13/186.webp") with dissolve
            charlotte "Anda berbohong kepada saya. Saya benar-benar merasakan sesuatu yang menyentuh pipi pantat saya."
            scene expression ("images/episode13/187.webp") with dissolve
            toby "Maka mungkin saya harus memeras payudara Anda sehingga Anda tidak melihat penisku menekan pipi pantatmu."
            scene expression ("images/episode13/188.webp") with dissolve
            charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}You're killing me. You know that, right?{/i}"
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Turn around.{/i}"
            scene expression ("images/episode13/189.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I want you so bad.{/i}"
            scene expression ("images/episode13/190.webp") with dissolve
            charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}How bad do you want me?{/i}"
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Really, really bad.{/i}"
            charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}But, I am your [mother].{/i}"
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}And you're the most perfect woman I know.{/i}"
            scene expression ("images/episode13/191.webp") with dissolve
            charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}So do you want this hand to go lower?{/i}"
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I'd love that.{/i}"
            scene expression ("images/episode13/192.webp") with dissolve
            charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}So what now?{/i}"
            if toby_job == 0:
                toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Surprise me.{/i}"
                scene expression ("images/episode13/193.webp") with dissolve
                charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}How's this for a surprise?{/i}"
            else:
                toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Now you take my cock in your hand.{/i}"
                scene expression ("images/episode13/193.webp") with dissolve
                charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Like this?{/i}"
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Fuck, your hand feels so good around my cock.{/i}"
            $ unlockImage(persistent.charlotte_25)
            scene expression ("images/episode13/194.webp") with dissolve
            charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Please don't be mad at me, but I can't do this and I can't blame it on the alcohol this time.{/i}"
            toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Would you want to be able to blame it on the alcohol?{/i}"
            charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Maybe...{/i}"
            if toby_job == 0:
                toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I understand. I'll leave then.{/i}"
                charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}That would be best.{/i}"
            else:

                toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Just move your hand a little bit up and down.{/i}"
                charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Sorry honey, I can't do it. It feels so wrong.{/i}"
                toby "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}I'll leave then.{/i}"
                charlotte "{size=12}{color=#FDCA6E}* whispering *{/color}{/size}\n{i}Please do!{/i}"

            scene expression ("images/episode13/195.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()

            $ unlockMemory(persistent.memory_47)
            $ renpy.end_replay()


        scene expression ("images/episode13/196.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck, fuck... I can't believe that [mom] almost gave me a hand job. Shit, why does everything that's wrong feel so good?{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Her hand felt so good on my cock.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}If things keep going like this, sooner or later we'll go past the point of no return.{/i}"
        scene expression ("images/episode13/197.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I should finish my shower and leave. All this heat is going to my head.{/i}"
    else:

        scene expression ("images/episode13/197.webp") with dissolve
        $ ui.saybehavior()
        $ ui.interact()
    scene expression ("images/episode13/198.webp") with fade
    toby "Saya sudah selesai. Aku akan menunggumu di ruang ganti."
    scene expression ("images/episode13/199.webp") with dissolve
    charlotte "Oke, sayang."

    return

label episode13_gym_sheila:
    $ progress = 177
    scene expression ("images/episode13/200.webp") with dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode13/201.webp") with dissolve
    sheila "Anda meluangkan waktu Anda."
    scene expression ("images/episode13/202.webp") with dissolve
    toby "Apakah Anda menungguku?"
    scene expression ("images/episode13/203.webp") with dissolve
    sheila "Ya. Saya ingin memberi tahu Anda bahwa saya berbicara dengan atasan saya dan mereka setuju untuk memberi Anda kekebalan jika Anda membantu kami menangkap lesbian."
    toby "Itu berita bagus. Saya lega mendengarnya."
    scene expression ("images/episode13/204_curious.webp") with dissolve
    sheila "Jadi? Sudahkah Anda membuat kemajuan?"
    scene expression ("images/episode13/205_normal.webp") with dissolve
    toby "Yah, belum. Ini adalah pertama kalinya saya kembali bekerja sejak kami berbicara."
    scene expression ("images/episode13/204_normal.webp") with dissolve
    sheila "Apakah Anda pikir bos Anda mencurigai Anda tentang sesuatu?"
    scene expression ("images/episode13/205_smile.webp") with dissolve
    toby "Dia tidak bisa mencurigai saya. Terakhir kali saya berbicara dengannya, saya tidak tahu apa -apa tentang seluruh operasi ini. Mulai hari ini yang akan menjadi lebih sulit."
    scene expression ("images/episode13/204_normal.webp") with dissolve
    sheila "Saya mengerti, tapi jangan khawatir. Tetap tenang, alami, Anda tidak melakukan hal buruk. Lakukan saja pekerjaan Anda dan buka mata dan telinga Anda."
    scene expression ("images/episode13/205_laugh.webp") with dissolve
    toby "Kedengarannya jauh lebih mudah dari yang sebenarnya."
    scene expression ("images/episode13/204_smile.webp") with dissolve
    sheila "Anda akan baik -baik saja. Saya yakin akan hal itu."
    scene expression ("images/episode13/205_curious.webp") with dissolve
    toby "Ngomong -ngomong, Anda tidak memberi tahu saya apa pun tentang [sister] Anda. Seperti apa namanya, seperti apa penampilannya?"
    scene expression ("images/episode13/204_normal.webp") with dissolve
    sheila "Ya, saya merasa sangat nyaman dengan Anda sehingga saya merasa seperti saya sudah mengenal Anda selamanya. Saya kira itu sebabnya saya mengharapkan Anda sudah tahu Kalela."
    scene expression ("images/episode13/205_curious.webp") with dissolve
    toby "Kalela adalah namanya?"
    scene expression ("images/episode13/204_sad.webp") with dissolve
    sheila "Ya, tetapi sejak saya mulai menyelidiki Katrina, saya bahkan tidak pernah menemukan namanya. Jadi saya tidak tahu harus percaya apa."
    scene expression ("images/episode13/205_normal.webp") with dissolve
    toby "Mungkin dia mengubah namanya."
    scene expression ("images/episode13/204_normal.webp") with dissolve
    sheila "Ya, saya juga mempertimbangkannya. Ngomong -ngomong, aku tidak tahu bagaimana penampilannya sekarang, tetapi ketika kita masih muda, kita dulu terlihat sangat mirip, jadi dia mungkin masih terlihat sangat mirip denganku."
    scene expression ("images/episode13/205_smile.webp") with dissolve
    toby "Oke kalau begitu. Saya akan melihat apa yang bisa saya lakukan."
    if toby_job == 0:
        scene expression ("images/episode13/205_sad.webp") with dissolve
        toby "Saya tidak bisa berjanji kepada Anda, karena saya bekerja untuk Darlene, tetapi saya dapat mulai mengajukan pertanyaan dan mungkin menyelidiki sedikit."
    else:
        scene expression ("images/episode13/205_normal.webp") with dissolve
        toby "Saya tidak bisa menjanjikan Anda, karena Katrina belum sepenuhnya mempercayai saya dan di klub kami belum mendengar apa pun tentang klub bdsm itu atau apa pun. Tapi saya akan mencoba mengajukan beberapa pertanyaan, mungkin sedikit menyelidiki."
    scene expression ("images/episode13/204_sad.webp") with dissolve
    sheila "Hanya jangan melakukan sesuatu yang bodoh. Sebagian besar tetap membuka mata dan telinga Anda. Jangan mengambil risiko yang tidak perlu."
    if sheila_path:
        scene expression ("images/episode13/205_smile.webp") with dissolve
        toby "Anda peduli jika sesuatu terjadi pada saya?"
        scene expression ("images/episode13/204_normal.webp") with dissolve
        sheila "Tentu saja, Anda idiot. Aku sangat menyukaimu."
        scene expression ("images/episode13/205_laugh.webp") with dissolve
        toby "Saya merasa tersanjung."
    else:
        scene expression ("images/episode13/205_laugh.webp") with dissolve
        toby "Jangan khawatir, saya telah dalam situasi yang jauh lebih berbahaya dari ini."
        scene expression ("images/episode13/204_curious.webp") with dissolve
        sheila "Benar-benar?"
        scene expression ("images/episode13/205_laugh.webp") with dissolve
        toby "No tidak!"

    scene expression ("images/episode13/204_normal.webp") with dissolve
    sheila "Saya masih tidak percaya bagaimana seorang pria yang saya temui hanya dua bulan lalu akan setuju untuk membantu saya, tanpa mengharapkan atau meminta imbalan apa pun."
    if toby_job == 0:

        scene expression ("images/episode13/205_laugh.webp") with dissolve
        toby "Saya dibesarkan dengan benar. Sekarang setelah Anda bertemu [mother] saya dapat berterima kasih padanya secara langsung."
        scene expression ("images/episode13/204_smile.webp") with dissolve
        sheila "Percayalah, saya akan melakukannya."
    else:
        scene expression ("images/episode13/205_laugh.webp") with dissolve
        toby "Siapa bilang saya tidak ingin imbalan apa pun?"
        scene expression ("images/episode13/204_smile.webp") with dissolve
        sheila "Apakah kamu?"
        if not sheila_path:
            scene expression ("images/episode13/205_laugh.webp") with dissolve
            toby "Nah ... aku hanya mengacaukanmu."

    if sheila_path:
        label memory_48:

            if _in_replay:
                scene expression ("images/utils/black.png") with dissolve
                menu:
                    "Pilih pekerjaan Anda"
                    "Agen real estat":
                        $ toby_job == 0
                    "Manajer klub":
                        $ toby_job == 1
            scene expression ("images/episode13/208.webp") with dissolve
            if toby_job == 0:
                toby "Yah, aku juga tidak akan mengatakan tidak pada apresiasi."
            else:
                toby "Sejujurnya saya tidak akan mengatakan tidak pada apresiasi."
            scene expression ("images/episode13/209.webp") with dissolve
            sheila "Benar-benar? Anda tidak akan keberatan?"
            toby "Sama sekali tidak."
            scene expression ("images/episode13/210.webp") with dissolve
            sheila "Apa yang Anda katakan kami melakukan sesuatu yang gila?"
            toby "Di Sini?"
            sheila "Ya kenapa tidak?"
            scene expression ("images/episode13/211.webp") with dissolve
            toby "Bagaimana jika [mom] kembali dari kamar mandi."
            sheila "Kami akan mendengarnya dan jika kami tidak, maka dia hanya akan melihat apa yang dia angkat."
            scene expression ("images/episode13/212.webp") with dissolve
            if toby_job == 0:
                toby "Aku sangat menginginkanmu."
                scene expression ("images/episode13/213.webp") with dissolve:
                    verticalLoop
                $ unlockImage(persistent.sheila_09)
                sheila "Aku juga menginginkanmu."
            else:
                toby "Apa yang kamu tunggu? Berlutut dan sampai ke sana, sebelum seseorang datang."
                scene expression ("images/episode13/213.webp") with dissolve:
                    verticalLoop
                $ unlockImage(persistent.sheila_09)
                sheila "Ya, Tuan!"

            scene expression ("images/episode13/214.webp") with dissolve:
                horizontalLoop
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/utils/black.png")
            show ep13_215
            sheila "Apakah ini yang Anda harapkan sebagai penghargaan?"
            toby "Sejujurnya, ini persis seperti yang saya bayangkan akan dimulai."
            sheila "Ah, benarkah? Anda ingin lebih?"
            toby "Tentu saja saya lakukan. Dua kali terakhir Anda hanya menggodaku, saya menginginkan Anda."
            sheila "Maaf tentang itu. Saya kira saya harus memperbaikinya."

            show ep13_216 with dissolve
            hide ep13_215

            toby "Ini jauh lebih baik."
            $ ui.saybehavior()
            $ ui.interact()
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck... Her mouth feels so good on my cock.{/i}"

            show ep13_217 with dissolve
            hide ep13_216

            if toby_job == 0:
                toby "Itu saja, sayang ... rasanya sangat enak."
            else:
                toby "Itu saja, sayang ... mengisap penisku seperti pelacur kecil."
            $ ui.saybehavior()
            $ ui.interact()
            toby "Anda adalah polisi terbaik yang pernah ada."

            show ep13_218 with dissolve
            hide ep13_217

            $ ui.saybehavior()
            $ ui.interact()
            toby "Saya akan mengatakan tidak berhenti, tapi saya pikir kami berdua menginginkan lebih dari itu."


            scene expression ("images/episode13/219_1.webp") with dissolve:
                verticalLoop
            hide ep13_218
            sheila "Anda tidak tahu betapa sulitnya bagi saya untuk hanya menggoda Anda."

            scene expression ("images/episode13/219_2.webp") with dissolve:
                horizontalLoop
            sheila "Sudah lama sekali sejak aku merasakan kemaluanmu di dalam diriku."

            scene expression ("images/episode13/220.webp") with dissolve:
                verticalLoop_reverse
            $ ui.saybehavior()
            $ ui.interact()
            sheila "{size=12}{color=#FDCA6E}* moaning slightly *{/color}{/size}\nYour cock feels perfect. It's like it was made for my pussy."

            scene expression ("images/utils/black.png")
            show ep13_221
            sheila "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nYes [toby!c], yes, yes, yes!"
            sheila "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nIt feels so good."
            $ ui.saybehavior()
            $ ui.interact()
            sheila "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nI love how good your cock feels inside me."

            show ep13_222 with dissolve
            hide ep13_221

            sheila "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes, right there."
            sheila "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck yes, [toby!c]. Fuck me!"
            $ ui.saybehavior()
            $ ui.interact()

            show ep13_223 with dissolve
            hide ep13_222

            sheila "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nFuck, fuck, fuck!"
            sheila "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nThis feels so good."
            $ ui.saybehavior()
            $ ui.interact()

            show ep13_224 with dissolve
            hide ep13_223

            sheila "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nGive it to me, [toby!c]. Don't stop!"
            sheila "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nDon't stop, don't stop."
            $ ui.saybehavior()
            $ ui.interact()
            sheila "{size=12}{color=#FDCA6E}* gasping *{/color}{/size}\nThere, right there!"

            show ep13_225 with dissolve
            hide ep13_224

            sheila "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nFuck! Fuck me, [toby!c]. Fuck me hard."
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Sheila's pussy feels so good. I don't know how much longer I can hold it.{/i}"
            $ ui.saybehavior()
            $ ui.interact()
            sheila "{size=12}{color=#FDCA6E}* panting *{/color}{/size}\nYes, yes, yes!"

            show ep13_226 with dissolve
            hide ep13_225

            toby "Saya dekat."
            sheila "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nMe too."
            $ ui.saybehavior()
            $ ui.interact()
            toby "Saya akan pergi ke cum."
            sheila "{size=12}{color=#FDCA6E}* moaning *{/color}{/size}\nCum inside me. I'm on pill."

            scene expression ("images/episode13/227_1.webp") with dissolve:
                moveUp

            hide ep13_226
            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            scene expression ("images/episode13/227_2.webp") with dissolve:
                moveRight

            $ unlockImage(persistent.sheila_10)
            $ ui.pausebehavior(9.3)
            $ ui.saybehavior()
            $ ui.interact()

            $ unlockMemory(persistent.memory_48)
            $ renpy.end_replay()


        scene expression ("images/episode13/228.webp") with dissolve:
            moveDown

        $ ui.pausebehavior(9.3)
        $ ui.saybehavior()
        $ ui.interact()

        stop music fadeout 2.0
        scene expression ("images/episode13/229.webp") with dissolve
        sheila "Kotoran! [mom] Anda akan datang! Cepat, tutupi diri Anda!"

        scene expression ("images/episode13/230.webp") with dissolve
        charlotte "Hai teman -teman."
        scene expression ("images/episode13/231.webp") with dissolve
        toby "Hai, [mom]. Bagaimana mandi Anda?"
        sheila "Bagaimana perasaanmu? Apakah Anda bisa mandi?"
        scene expression ("images/episode13/230_2.webp") with dissolve
        charlotte "Apakah semuanya baik -baik saja?"
        scene expression ("images/episode13/232.webp") with dissolve
        sheila "Ya tentu. Saya baru saja memberi tahu [toby!c] di sini bahwa Anda mungkin adalah gadis emas saya."
        scene expression ("images/episode13/233.webp") with dissolve
        charlotte "Maksudnya itu apa?"
        scene expression ("images/episode13/232.webp") with dissolve
        sheila "Ini berarti bahwa jika semuanya berjalan dengan baik, dalam waktu kurang dari sebulan kita akan melihat perubahan luar biasa dan saya dapat menggunakan kemajuan Anda untuk mempromosikan pelatihan saya."
        scene expression ("images/episode13/233.webp") with dissolve
        charlotte "Apakah Anda benar -benar berpikir begitu?"
        scene expression ("images/episode13/234.webp") with dissolve
        sheila "Tentu saja, sayang. Aku akan membiarkan kalian berubah."
        scene expression ("images/episode13/235_1.webp") with dissolve
        charlotte "Bisakah Anda mempercayainya? Dia berpikir bahwa saya adalah klien terbaiknya."
        toby "Saya tidak pernah meragukannya."
        scene expression ("images/episode13/235_2.webp") with dissolve
        charlotte "Saya menyukainya. Bagaimana kalian berdua bertemu?"
        scene expression ("images/episode13/235_3.webp") with dissolve
        toby "Nah, kami bertemu di sini di gym pada kunjungan pertama saya."
        scene expression ("images/episode13/236_1.webp") with dissolve
        toby "Kita harus diubah."
        scene expression ("images/episode13/236_2.webp") with dissolve
        charlotte "Ya kita harus."
        scene expression ("images/episode13/237.webp") with dissolve
        charlotte "Apa hubungan Anda dengan Sheila?"
        scene expression ("images/episode13/238.webp") with dissolve
        toby "Aku tidak tahu. Kami rukun."
        scene expression ("images/episode13/237.webp") with dissolve
        charlotte "Itu saja? Karena aku bisa bersumpah aku mendengar dia meneriakkan namamu."
        scene expression ("images/episode13/239.webp") with dissolve
        toby "Umm ..."
        scene expression ("images/episode13/237.webp") with dissolve
        charlotte "Sebenarnya, jangan beri tahu saya. Saya menyukainya sebagai pelatih pribadi. Saya tidak ingin mengubah pendapat saya tentang dia atau tentang Anda."
        scene expression ("images/episode13/238.webp") with dissolve
        toby "Mau mu."
        if charlotte_path:
            scene expression ("images/episode13/240.webp") with dissolve
            charlotte "Sebenarnya saya ingin tahu."
            scene expression ("images/episode13/239.webp") with dissolve
            toby "Apa yang terjadi pada \"Aku sangat menyukainya dan aku tidak ingin mengubah pendapatku tentangnya.\"
            scene expression ("images/episode13/240.webp") with dissolve
            charlotte "Nah, saya tidak ingin terlihat bodoh jika dia berbicara tentang Anda seperti Anda adalah pacarnya."
            scene expression ("images/episode13/238.webp") with dissolve
            toby "Dia bukan pacarku."
            scene expression ("images/episode13/240.webp") with dissolve
            charlotte "Jadi itu hanya seks tanpa emosi?"
            scene expression ("images/episode13/239.webp") with dissolve
            toby "Siapa bilang kami berhubungan seks?"
            scene expression ("images/episode13/241.webp") with dissolve
            charlotte "Saya [mother] Anda dan dapat membaca Anda seperti buku terbuka. Ketika saya masuk, kalian berdua tampak seperti tertangkap melakukan sesuatu dan meskipun saya sedang mandi saya bisa mendengar beberapa suara."
            toby "Kita harus berpakaian."
            if emma_path:
                charlotte "Anda tahu bahwa saya akan selalu mencintaimu sayang, tapi ini tidak baik. Anda memiliki Emma. Dia pacarmu. Anda tidak bisa menipu dia."
                if toby_job == 0:
                    toby "Hubungan kami sedikit lebih rumit. Selain itu, Anda juga dalam hal ini. Ingat semua ciuman kita?"
                else:
                    toby "Itu kaya yang datang dari Anda. Apakah kamu sudah lupa semua ciuman kami? Aku sudah berselingkuh, bersamamu."
                scene expression ("images/episode13/242.webp") with dissolve
                charlotte "Ya, kita harus berpakaian."
            else:
                charlotte "Tidak apa -apa [toby!c]. Saya mengajari Anda lebih baik dari ini. Saya mengerti, seks itu bagus, tetapi Anda tidak boleh melakukannya dengan seseorang yang tidak Anda cintai."
                toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's jealous?{/i}"
                toby "Maksudmu, kamu? Karena tidak ada orang yang lebih saya cintai dari Anda."
                scene expression ("images/episode13/243.webp") with dissolve
                charlotte "Kita harus berpakaian. Anda mulai berbicara bodoh."
    else:


        scene expression ("images/episode13/206.webp") with dissolve
        sheila "Bagaimanapun. Saya akan membiarkan Anda berubah. Saya tidak ingin [mother] Anda mendapatkan ide lain."
        toby "Oke, kalau begitu. Aku akan terus mengabarimu."
        sheila "Jangan SMS saya. Setiap kali Anda ingin memberi tahu saya sesuatu, datang saja ke gym dan kami akan berbicara di sini."
        toby "Banyak paranoid?"
        sheila "Anda tidak pernah tahu siapa yang mendengarkan panggilan kami dan siapa yang ada di daftar gaji Katrina."
        toby "Ya, Anda benar."
        toby "Kurasa kita akan mengubah ruang ganti ini menjadi gua kelelawar kita."
        scene expression ("images/episode13/207.webp") with dissolve
        sheila "Anda menonton terlalu banyak film."
        sheila "Bagaimanapun. Sampai jumpa."
        toby "Bye Sheila!"

    stop music fadeout 2.0
    return

label episode13_work:
    $ progress = 178
    scene expression ("images/utils/black.png")
    show screen ui_message("Later that day") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    hide screen ui_message

    if toby_job == 0:
        call episode13_work_0_1 from _call_episode13_work_0_1
    else:
        call episode13_work_1_1 from _call_episode13_work_1_1

    $ progress = 179
    call episode13_restaurant from _call_episode13_restaurant

    show screen ui_message("A few hours later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()

    $ progress = 180
    if toby_job == 0:
        call episode13_work_0_2 from _call_episode13_work_0_2
    else:
        call episode13_work_1_2 from _call_episode13_work_1_2
    return

label episode13_work_0_1:

    scene expression ("images/episode13/244.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Looks like Mrs. Darlene isn't here yet. Should I call her and ask her what I need to do?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Or maybe just wait for her like 5 minutes. Maybe she just went to the bathroom.{/i}"
    show screen ui_message("Ten minutes later") with long_dissolve
    $ ui.saybehavior()
    $ ui.interact()
    scene expression ("images/episode13/245.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Yeah, I think I'll call her.{/i}"
    scene expression ("images/episode13/246.webp") with dissolve
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nYes, [toby!c]?"
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nGood afternoon ma'am. I arrived at the office a few minutes ago and I don't know what I need to do today."
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nOh sorry, I completely forgot I asked you to come around noon. I went out to eat, so I won't be back for at least an hour."
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nHowever, there's a file on my desktop with a few apartments that just went up for sale. Could you contact the owners and try to get us some meetings for tomorrow."
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nSure thing. Does the time matter?"
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nNot really, just make sure they say yes, not everybody wants a firm to help them sell their apartments."
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nOkay, I'll make sure they will agree to meet us."
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nPerfect. Don't let me down [toby!c]."
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nI won't."
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nEnjoy your lunch."
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nThank you. See you in an hour."
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nOkay, bye."
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nWait!"
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nYes?"
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nDid you eat anything yet?"
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nNo, not yet."
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nI'll send you the address of the restaurant I'm at."
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nI'm not hungry yet and besides, it might take a while for me to get there. I don't want to ruin your plans."
    if darlene_path:
        darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nYou won't ruin anything. Would you really leave me here to eat all alone?"
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nFine, I'll come over, just text me the address."
    else:
        darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nYou won't ruin anything, just come. Don't let me eat alone. I'll text you the address."
        toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nOkay. You win."
    darlene "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nWell, in that case, see you in a few minutes."
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nSure."

    return

label episode13_work_1_1:

    scene expression ("images/episode13/247.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Looks like she's not here. Maybe she's somewhere in the club.{/i}"
    scene expression ("images/episode13/248.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}\"Come to work [toby!c]. You have a lot of work to do, but I won't be there to tell you what to do\". {/i}"
    scene expression ("images/episode13/249.webp") with dissolve
    toby "Hei Neal. Pernahkah Anda melihat Katrina?"
    neal "Ya."
    toby "Di mana?"
    neal "Kenapa aku memberitahumu? Itu bukan pekerjaan saya. Cari tahu sendiri."
    scene expression ("images/episode13/250.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fucking piece of shit. He doesn't like me because I'm Katrina's right hand instead of him.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Well, I'm sorry, but you're only muscle. You need a brain too.{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I'm going to call Katrina to see where she's at.{/i}"
    scene expression ("images/episode13/251.webp") with dissolve
    katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n[toby!c]... Do you miss your mommy? Is that why you called me?"
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nYeah... What do I have to do today?"
    katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nOh, mommy misses you too. I'll send you an address. Get there quickly."
    toby "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nWhatever."

    return

label episode13_restaurant:
    scene expression ("images/episode13/252.webp") with dissolve
    if toby_job == 0:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see where Darlene's at.{/i}"
        scene expression ("images/episode13/253.webp") with dissolve
        darlene "Hai, [toby!c]. Di sini."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I thought she said she was alone.{/i}"
    else:
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Let's see where I can find Katrina. I wonder what business she has with this restaurant.{/i}"
        scene expression ("images/episode13/254.webp") with dissolve
        katrina "[toby!c]. Kami di sini. Bergabunglah dengan kami."
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}For some reason I don't think this has anything to do with business.{/i}"
    scene expression ("images/episode13/255.webp") with dissolve
    toby "Halo, nona."
    if toby_job == 0:
        scene expression ("images/episode13/256.webp") with dissolve
        darlene "Senang Anda bisa membuatnya."
        scene expression ("images/episode13/258_1.webp") with dissolve
        toby "Saya pikir Anda bilang Anda sendirian?"
        scene expression ("images/episode13/258_2.webp") with dissolve
        darlene "Bahaya pekerjaan. Saya sangat terbiasa berbohong kepada orang -orang untuk mendapatkan apa yang saya inginkan, bahwa kadang -kadang saya tidak bisa berhenti."
        scene expression ("images/episode13/259_2.webp") with dissolve
        katrina "Anda ingin menghabiskan waktu sendirian dengan pacar saya [toby!c]? Apakah itu yang Anda inginkan? Kamu menginginkannya?"
        scene expression ("images/episode13/259_1.webp") with dissolve
        toby "Tidak, tentu saja tidak. Jika saya tahu Anda ada di sini, saya akan berpakaian lebih seksi."
        scene expression ("images/episode13/259_2.webp") with dissolve
        katrina "Anda tahu bahwa saya menjadi wanita, kan? Jadi bagi saya seksi berarti belahan dada besar, beberapa jala, rok atau celana pendek yang sangat pendek dan sepatu hak besar."
        scene expression ("images/episode13/259_1.webp") with dissolve
        toby "Ya ... saya pikir saya bisa melakukannya."
        scene expression ("images/episode13/260.webp") with dissolve
        katrina "Saya menyukainya. Ketika dia membuatmu kesal dan kamu memecatnya, katakan padaku dan aku akan membawanya."
        darlene "Tidak, Anda akan menghancurkannya. Dia terlalu bagus untukmu."
    else:
        scene expression ("images/episode13/257.webp") with dissolve
        katrina "Anda terlambat."
        scene expression ("images/episode13/259_1.webp") with dissolve
        toby "Yah, saya harus pergi ke klub terlebih dahulu, lalu datang ke sini."
        scene expression ("images/episode13/259_2.webp") with dissolve
        katrina "Mengapa?"
        scene expression ("images/episode13/259_1.webp") with dissolve
        toby "Karena untuk beberapa alasan saya melewatkan teks Anda di mana Anda mengatakan Anda ingin bertemu saya di sini."
        scene expression ("images/episode13/259_2.webp") with dissolve
        katrina "Anda harus memeriksa ponsel Anda lebih sering."
        scene expression ("images/episode13/259_1.webp") with dissolve
        toby "Ya, apa yang bisa saya katakan. Bodoh aku."
        toby "Oh tunggu. Saya tidak mendapatkan teks apa pun, saya pergi ke klub dan kemudian setelah mencari Anda di seluruh klub, saya memutuskan untuk menelepon Anda."
        scene expression ("images/episode13/259_2.webp") with dissolve
        katrina "Mengapa Anda mencari saya di klub? Bagaimana jika saya menyenangkan diri sendiri di toilet? Apakah Anda ingin melihat itu, [toby!c]? Apakah itu yang Anda harapkan? Nakal, nakal, [toby!c]."
        scene expression ("images/episode13/260.webp") with dissolve
        darlene "Kenapa kamu menyebalkan untuk bocah itu? Tinggalkan dia sendiri."
        katrina "Anda tahu betapa saya menyukainya. Saya suka menggodanya."
    scene expression ("images/episode13/261.webp") with dissolve
    waitress "Selamat datang, Pak. Apakah Anda membutuhkan menu?"
    toby "Ya tentu. Terima kasih."
    scene expression ("images/episode13/262.webp") with dissolve
    katrina "Dia akan memiliki apa yang kita miliki."
    scene expression ("images/episode13/263_1.webp") with dissolve
    waitress "Ummm ..."
    scene expression ("images/episode13/263_2.webp") with dissolve
    toby "Tentu, saya akan mengambil apa pun yang mereka miliki. Terima kasih."
    scene expression ("images/episode13/263_1.webp") with dissolve
    waitress "Bisakah saya memberi Anda sesuatu untuk diminum?"
    scene expression ("images/episode13/263_2.webp") with dissolve
    toby "Tolong, segelas air saja."
    scene expression ("images/episode13/263_1.webp") with dissolve
    waitress "Tentu."
    scene expression ("images/episode13/264.webp") with dissolve
    darlene "Anda tahu Anda menyebalkan, kan?"
    scene expression ("images/episode13/265.webp") with dissolve
    katrina "Apa? Saya lapar. Dia akan melihat menu itu selama lima menit, akan membutuhkan sepuluh lagi untuk pelacur itu untuk kembali untuk mengambil pesanannya dan kemudian dia akan mengatakan bahwa mereka kehabisan itu hari ini atau apa pun."
    katrina "Dan coba tebak? Dia akan memesan hal yang sama yang kita dapatkan. Jadi saya baru saja menyelamatkan kami lima belas menit yang baik."
    scene expression ("images/episode13/266.webp") with dissolve
    darlene "Kami punya ayam dengan saus gorgonzola dengan sayuran. Jika Anda ingin memesan hal lain yang Anda bisa. Jangan dengarkan dia, dia menyebalkan ketika dia lapar."
    scene expression ("images/episode13/267.webp") with dissolve
    toby "Jangan khawatir. Itu sempurna."
    if toby_job == 0:
        scene expression ("images/episode13/268_curious_3.webp") with dissolve
        katrina "Jadi, [toby!c]. Bagaimana Anda suka bekerja untuk Darlene?"
        scene expression ("images/episode13/269_awkward_1.webp") with dissolve
        darlene "Bukan ini lagi."
        scene expression ("images/episode13/270_smile_1.webp") with dissolve
        toby "Sejujurnya, saya sangat menikmati bekerja untuknya. Saya harus banyak belajar."
        scene expression ("images/episode13/268_flirty_3.webp") with dissolve
        katrina "Saya yakin Anda melakukannya. Dia sangat terampil dengan lidahnya dan bukan hanya itu, Anda ingin dia menjilat kemaluan Anda, kan?"
        if darlene_path:
            scene expression ("images/episode13/270_thinking.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Does she know about us?{/i}"
        scene expression ("images/episode13/270_awkward_1.webp") with dissolve
        toby "Ummm. Saya berbicara sangat profesional. Saya harus banyak belajar darinya, secara profesional."
        scene expression ("images/episode13/269_awkward.webp") with dissolve
        darlene "Tuhan! Saya seharusnya tidak mengundang [toby!c] untuk makan siang."
        scene expression ("images/episode13/270_smile_2.webp") with dissolve
        toby "Anda tidak perlu khawatir, itu baik -baik saja. [mother] saya sering menggodaku dengan pertanyaan seperti ini. Saya sudah terbiasa."
        scene expression ("images/episode13/268_laugh_3.webp") with dissolve
        katrina "Jadi Anda melihat saya seperti sosok keibuan? Menarik."
        scene expression ("images/episode13/269_normal_1.webp") with dissolve
        darlene "Bagaimana Anda sampai pada kesimpulan itu? Tolong, berhenti saja. Tinggalkan dia sendiri."
        scene expression ("images/episode13/268_smile_2.webp") with dissolve
        katrina "Apa? Saya tidak melakukan apa -apa. Saya hanya mencoba mengenal karyawan favorit Anda dengan lebih baik. Itu semua."
        scene expression ("images/episode13/268_flirty_3.webp") with dissolve
        katrina "Jadi, [toby!c]. Apakah Anda melihat Darlene sebagai seorang ibu?"
        scene expression ("images/episode13/270_normal_1.webp") with dissolve
        toby "Saya pikir Anda bertanya apakah saya melihat Anda sebagai seorang ibu."
        scene expression ("images/episode13/268_laugh_3.webp") with dissolve
        katrina "Kami hidup di masa yang aneh. Semuanya bisa berubah dalam sekejap mata."
        scene expression ("images/episode13/268_smile_3.webp") with dissolve
        katrina "Jadi? Bagaimana Anda melihat Darlene?"
        scene expression ("images/episode13/270_normal_1.webp") with dissolve
        toby "Saya tidak akan mengatakan saya melihatnya sebagai seorang ibu, tetapi dalam beberapa hal saya kira dia. Dia mengajari saya segala sesuatu yang perlu diketahui tentang real estat."
        scene expression ("images/episode13/268_horny_3.webp") with dissolve
        katrina "Dan apakah Anda menyukai itu? Apakah itu salah satu fetish Anda?"
        scene expression ("images/episode13/269_angry_1.webp") with dissolve
        darlene "Itu saja. Anda membuatnya tidak nyaman. Dia tamuku, jadi kamu tidak diizinkan untuk menggodanya."
        scene expression ("images/episode13/268_eyes.webp") with dissolve
        katrina "Kalian berdua membosankan. Aku hanya ingin tahu apakah dia ingin bercinta denganmu."
        scene expression ("images/episode13/268_normal_2.webp") with dissolve
        katrina "Anda tahu betapa cemburu yang saya dapatkan ketika ada pria tampan di sekitar Anda."
        if darlene_path:
            scene expression ("images/episode13/270_thinking.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She must suspect something's going on between me and Darlene. We need to be more careful...because this woman is crazy."
        scene expression ("images/episode13/269_normal_1.webp") with dissolve
        darlene "Hentikan, Kat. Anda bersikap konyol. [toby!c] Tidak ingin tidur dengan saya. Anda hanya membuatnya tidak nyaman."
        scene expression ("images/episode13/268_curious_2.webp") with dissolve
        katrina "Bagaimana Anda bisa begitu yakin? Apakah Anda tahu fantasinya? Apakah Anda tahu fetish apa yang dimilikinya?"
        scene expression ("images/episode13/270_normal_1.webp") with dissolve
        toby "Anda tidak perlu khawatir."
        scene expression ("images/episode13/268_flirty_3.webp") with dissolve
        katrina "Itu bagi saya untuk memutuskan. Jadi? Apa fetish Anda?"
        scene expression ("images/episode13/269_angry_1.webp") with dissolve
        darlene "Kat!"
        scene expression ("images/episode13/268_smile_2.webp") with dissolve
        katrina "Apa? Tidakkah kamu ingin tahu apa fetisinya? Akan menarik untuk mengetahui apa yang dia lakukan."
        scene expression ("images/episode13/269_awkward_1.webp") with dissolve
        darlene "Tuhan! Ini adalah terakhir kali saya membiarkan Anda meyakinkan saya untuk mengundangnya untuk makan siang bersama kami."
        scene expression ("images/episode13/268_horny_3.webp") with dissolve
        katrina "Jadi [toby!c], saya mendengarkan. Apa fetish Anda? Apakah Anda menyukai wanita yang lebih tua?"
        scene expression ("images/episode13/269_normal_3.webp") with dissolve
        darlene "Anda benar -benar tidak harus menjawab."
        scene expression ("images/episode13/270_thinking.webp") with dissolve

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I know I don't have to, but maybe I could use this to try to get a little info about the BDSM club.{/i}"
        scene expression ("images/episode13/268_laugh_2.webp") with dissolve
        katrina "Dia berpikir. Sepertinya dia akan memberitahuku. Saya suka pria ini."
        scene expression ("images/episode13/269_awkward_1.webp") with dissolve
        darlene "Dia berpikir bagaimana menghindari pantat bodohmu."
        scene expression ("images/episode13/268_laugh_2.webp") with dissolve
        katrina "Dia bisa \ 't."
        scene expression ("images/episode13/268_flirty_3.webp") with dissolve
        katrina "Jadi, [toby!c]? Apa yang kamu suka?"
        scene expression ("images/episode13/270_normal_1.webp") with dissolve
        toby "Yah saya tidak bisa mengatakan saya ke dalamnya, tapi saya ingin mencoba beberapa barang bdsm."
        scene expression ("images/episode13/269_surprised_3.webp") with dissolve
        darlene "Umm ... kamu benar -benar tidak seharusnya menjawab."
        scene expression ("images/episode13/270_smile_2.webp") with dissolve
        toby "Dia penasaran."
        scene expression ("images/episode13/268_flirty_2.webp") with dissolve
        katrina "Ya, sayang. Saya penasaran. Apa yang salah dengan itu?"
        scene expression ("images/episode13/268_horny_3.webp") with dissolve
        katrina "Bdsm katamu? Itu menarik. Anda suka dicambuk dan diikat ke langit -langit dengan ayam Anda di kandang kecil?"
        scene expression ("images/episode13/270_laugh_1.webp") with dissolve
        toby "Anda salah. Saya tidak ingin diikat dan dipukuli. Saya ingin menjadi orang yang bertanggung jawab."
        scene expression ("images/episode13/268_normal_3.webp") with dissolve
        katrina "Nah, itu membosankan. Saya berharap menemukan mainan."
        scene expression ("images/episode13/269_awkward.webp") with dissolve
        darlene "Tuhan! Bagaimana kita berakhir di sini?"
        scene expression ("images/episode13/269_normal_1.webp") with dissolve
        darlene "Dia tidak ingin menjadi mainan Anda. Tidak ada yang menginginkan itu, jadi bisakah kita mengubah topik pembicaraan?"
        scene expression ("images/episode13/268_flirty_3.webp") with dissolve
        katrina "Jadi ... apa yang akan Anda lakukan untuk pengalaman BDSM? Berapa banyak yang Anda inginkan?"
        scene expression ("images/episode13/270_thinking.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Looks like she's taking the bait. I need to play innocent.{/i}"
        scene expression ("images/episode13/270_curious_1.webp") with dissolve
        toby "Satu -satunya orang yang bisa membantu saya adalah pacar saya, tetapi saya belum menemukan seorang gadis yang terbuka untuk itu.Saya tidak yakin saya mengerti pertanyaan Anda. Mengapa itu penting? Ini tidak seperti Anda bisa membantu saya dengan itu."
        scene expression ("images/episode13/268_normal_3.webp") with dissolve
        katrina "Mungkin Anda tidak melihat di tempat yang tepat, dan siapa bilang itu harus menjadi pacar Anda? Anda bisa memiliki pacar manis yang tidak bersalah yang menunggu Anda di ruang tamu, semuanya sambil memiliki pelacur kecil di ruang bawah tanah yang tidak diketahui siapa pun."
        scene expression ("images/episode13/270_curious_1.webp") with dissolve
        toby "Ya, saya tidak terlalu banyak menculik."
        scene expression ("images/episode13/268_laugh_3.webp") with dissolve
        katrina "Siapa bilang sesuatu tentang penculikan? Dia bisa hidup dengan sukarela di ruang bawah tanah."
        scene expression ("images/episode13/270_smile_1.webp") with dissolve
        toby "Ya saya mendengar tentang klub BDSM yang melakukan hal seperti ini."
        scene expression ("images/episode13/268_flirty_3.webp") with dissolve
        katrina "Jadi? Seberapa besar Anda menginginkan pengalaman BDSM?"
        stop music fadeout 2.0
        scene expression ("images/episode13/269_angry_1.webp") with dissolve
        $ unlockImage(persistent.darlene_katrina_01)
        darlene "Kat! Hentikan."
        scene expression ("images/episode13/268_curious_2.webp") with dissolve
        katrina "Apa yang salah?"
        scene expression ("images/episode13/269_normal_1.webp") with dissolve
        darlene "Itu cukup! Dia akan menemukan dirinya sebagai pacar yang suka dicambuk dan itu saja. Jangan menaruh ide -ide bodoh di kepalanya."
        scene expression ("images/episode13/270_normal_2.webp") with dissolve
        toby "Maybe it's not stupid? After all, it's not like I could just ask my girlfriend, \"Hey do you like to be whipped?\"Jadi jika dia punya ide, saya terbuka untuk saran."
        scene expression ("images/episode13/268_doubt_3.webp") with dissolve
        katrina "Hmm ... itu menarik. Anda tampaknya sangat yakin bisa membantu Anda."
        scene expression ("images/episode13/270_scared_1.webp") with dissolve
        toby "Saya tidak, saya hanya ingin tahu tentang ide ruang bawah tanah Anda."
        scene expression ("images/episode13/268_normal_3.webp") with dissolve
        katrina "Basement apa? Aku hanya mengacaukanmu."
        scene expression ("images/episode13/270_thinking.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit. She's backing down, I should do the same.{/i}"
        scene expression ("images/episode13/270_laugh_1.webp") with dissolve
        toby "Oh sial ... kamu mendapatkanku. Untuk sesaat di sana saya bersemangat ketika saya pikir impian saya bisa memiliki kesempatan untuk menjadi kenyataan."
        scene expression ("images/episode13/268_laugh_3.webp") with dissolve
        katrina "Anda seperti itu, anak laki -laki kotor dan kotor, tetapi sayangnya saya tidak bisa membantu Anda."
        scene expression ("images/episode13/269_smile_1.webp") with dissolve
        darlene "Sekarang, bisakah kita membicarakan hal lain?"
        scene expression ("images/episode13/271.webp") with dissolve
        katrina "Mari kita bicara tentang seberapa panas penampilan pelayan kami membawa piring -piring itu."
        darlene "Anda tidak ada harapan."
    else:

        scene expression ("images/episode13/269_curious_3.webp") with dissolve
        darlene "Jadi, [toby!c]? Bagaimana Anda suka bekerja untuk Kat?"
        scene expression ("images/episode13/268_laugh_2.webp") with dissolve
        katrina "Anda tidak mencuri dia dariku."
        scene expression ("images/episode13/269_laugh_1.webp") with dissolve
        darlene "Siapa bilang sesuatu tentang mencuri dia? Saya hanya mengajukan pertanyaan kepada anak laki -laki itu, tetapi jika dia tidak suka bekerja untuk pelacur seperti Anda mungkin saya bisa memberinya sesuatu yang lain untuk dilakukan."
        scene expression ("images/episode13/270_laugh_2.webp") with dissolve
        toby "Terima kasih atas tawarannya, tetapi meskipun kadang -kadang saya dan Katrina tidak melihat mata ke mata, pada akhirnya itu benar -benar bagus. Saya suka bekerja untuknya."
        scene expression ("images/episode13/270_smile_2.webp") with dissolve
        toby "Dan selain itu, ada banyak manfaat dengan pekerjaan ini. Selain minuman keras dan gadis -gadis cantik yang datang yang datang ke klub, orang -orang menghormati saya."
        scene expression ("images/episode13/269_smile_3.webp") with dissolve
        darlene "Ya ada banyak manfaat yang memiliki Kat di pihak Anda. Saya ingat ketika seorang klien menyadari bahwa saya adalah pacarnya, dia bahkan tidak punya nyali untuk menegosiasikan harga. Dia baru saja membayar harga daftar lengkap."
        scene expression ("images/episode13/268_laugh_2.webp") with dissolve
        katrina "Apa yang bisa saya katakan, saya adalah seorang badass."
        scene expression ("images/episode13/268_smile_2.webp") with dissolve
        katrina "Dan meskipun saya tidak pernah mengatakan ini kepadanya, [toby!c] menjadi semakin banyak badass juga."
        if katrina_path:
            scene expression ("images/episode13/268_flirty_3.webp") with dissolve
            katrina "I still remember the first time you talked back to me and even had the guts to put your hands on my face, telling me something like \"I'm not your two legged ... lapdog\"."
            scene expression ("images/episode13/270_thinking.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I clearly remember that I didn't say \"two legged lapdog\", but \"two legged dick\". Tapi saya rasa dia tidak ingin Darlene tahu bahwa dia meminta saya untuk menjilat vaginanya. {/i}"
            scene expression ("images/episode13/269_surprised_3.webp") with dissolve
            darlene "Benar-benar? Anda benar -benar melakukan itu?"
            scene expression ("images/episode13/270_laugh_2.webp") with dissolve
            toby "Apa yang bisa saya katakan? Itu adalah hari kedua atau ketiga saya di tempat kerja dan dia menjadi perempuan jalang. Itu sebelum aku tahu betapa gilanya dia."
            scene expression ("images/episode13/268_smile_3.webp") with dissolve
            katrina "Ya ... itu ketika saya tahu saya melakukan hal yang benar dengan Anda."
            scene expression ("images/episode13/269_laugh_1.webp") with dissolve
            darlene "Jadi satu -satunya alasan dia adalah orang yang begitu buruk adalah karena dia tidak tahu betapa gilanya Anda?"
            scene expression ("images/episode13/268_smile_2.webp") with dissolve
            katrina "Tidak terlalu. Dia juga gila, dia hanya benci mengakuinya. Minggu lalu saya mengancamnya dengan pistol di mulutnya dan dia tidak untuk sesaat tampak ketakutan."
            scene expression ("images/episode13/269_laugh_1.webp") with dissolve
            darlene "Ya Tuhan, kalian berdua gila. Saya merasa seperti Anda menemukan diri Anda seorang putra."
            scene expression ("images/episode13/268_normal_2.webp") with dissolve
            katrina "Tidak, saya belum."
        else:

            scene expression ("images/episode13/269_surprised_1.webp") with dissolve
            darlene "Apa itu? Apakah Anda benar -benar hanya memberinya pujian saat dia ada? Anda menjadi orang yang lembut."
            scene expression ("images/episode13/270_laugh_2.webp") with dissolve
            toby "Apa maksudmu saat aku sekitar? Apakah itu berarti bahwa ketika saya tidak ada di sekitar, dia berbicara baik tentang saya?"
            scene expression ("images/episode13/268_angry_2.webp") with dissolve
            katrina "Jangan berani -berani!"
            scene expression ("images/episode13/269_laugh_3.webp") with dissolve
            darlene "Dia tidak ingin Anda tahu, tetapi dia tidak bisa berhenti berbicara tentang Anda. Dia terus mengatakan bahwa Anda adalah karyawan terbaik yang pernah dia miliki."
            scene expression ("images/episode13/270_surprised_2.webp") with dissolve
            toby "Benar-benar? Itu pertama kalinya saya mendengarnya."
            scene expression ("images/episode13/270_smile_1.webp") with dissolve
            toby "Jadi kamu sangat menyukaiku? Semua luak hanyalah sebuah taktik?"
            scene expression ("images/episode13/268_angry_2.webp") with dissolve
            katrina "Anda akan membayar banyak waktu untuk malam ini."
            scene expression ("images/episode13/269_laugh_3.webp") with dissolve
            darlene "Karena saya sudah dalam masalah besar, saya akan melanjutkan. Terkadang saya pikir dia melihat Anda seperti putra yang tidak pernah dia miliki."
            scene expression ("images/episode13/270_laugh_1.webp") with dissolve
            toby "Benar-benar? Anda menganggap saya sebagai seorang putra? Itu sangat manis."
            scene expression ("images/episode13/268_normal_3.webp") with dissolve
            katrina "Tidak saya tidak."

        scene expression ("images/episode13/270_laugh_1.webp") with dissolve
        toby "Benarkah, Bu? Anda tidak melihat saya sebagai seorang putra?"
        scene expression ("images/episode13/269_laugh_1.webp") with dissolve
        darlene "Tuhan! Saya suka pria ini."
        scene expression ("images/episode13/268_normal_3.webp") with dissolve
        katrina "Benar-benar? Anda melihat saya sebagai ibu? Lalu kenapa kamu melihat pantatku saat aku memakai rok pendek? Apakah Anda menyukai itu?"
        scene expression ("images/episode13/268_flirty_3.webp") with dissolve
        katrina "Apakah Anda keriting itu? Atau saya harus mengatakan kotor? Saya belum memutuskan."
        scene expression ("images/episode13/270_normal_1.webp") with dissolve
        toby "Jangan taruh ini padaku. Anda orang yang melihat saya sebagai seorang putra. Apakah Anda menyukai itu?"
        if katrina_path:
            scene expression ("images/episode13/268_normal_3.webp") with dissolve
            katrina "Tidak, saya bukan anak muda yang kotor yang suka wanita yang lebih tua berharap bahwa dia sedang bercinta dengan ibunya."
            scene expression ("images/episode13/269_curious_1.webp") with dissolve
            darlene "Tunggu sebentar. Sialan? Apa yang kamu bicarakan?"
            scene expression ("images/episode13/270_thinking.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit! This stupid slut talks too much.{/i}"
            scene expression ("images/episode13/268_normal_2.webp") with dissolve
            katrina "Saya tidak membicarakan apa pun. Saya hanya ingin memecahkan [toby!c] untuk melihat apa yang dia lakukan."
            scene expression ("images/episode13/268_flirty_3.webp") with dissolve
            katrina "Jadi [toby!c]? Apa yang kamu suka? Apa fetish Anda?"
        else:
            scene expression ("images/episode13/268_flirty_3.webp") with dissolve
            katrina "Bagaimana mungkin saya tidak? Maksudku, siapa yang tahu apa yang terjadi melalui kepala kecilmu. Saya tidak tahu fetish Anda."

        scene expression ("images/episode13/270_laugh_1.webp") with dissolve
        toby "Ini bukan tentang saya dan selain itu, saya tidak ingin merusak makanan kami untuk Darlene dengan fetish kotor saya."
        scene expression ("images/episode13/269_laugh_3.webp") with dissolve
        darlene "Jangan khawatir. Saya mungkin terlihat seperti wanita yang terhormat, tetapi saya dalam hubungan dengan Katrina. Saya bisa mengambil sedikit kotor dan selain sekarang Anda membuat saya benar -benar penasaran betapa kotor pikiran Anda."
        scene expression ("images/episode13/268_horny_3.webp") with dissolve
        katrina "Jadi? Apa yang kamu suka? Apakah Anda suka kaki? Mungkin anal?"
        scene expression ("images/episode13/269_laugh_1.webp") with dissolve
        darlene "Dia bilang dia memiliki beberapa fetish kotor. Anal dan kaki tidak terlalu kotor. Saya yakin dia bisa melakukan lebih baik dari itu."
        scene expression ("images/episode13/270_normal_2.webp") with dissolve
        toby "Bagaimana kita berakhir di sini?"
        scene expression ("images/episode13/269_laugh_3.webp") with dissolve
        darlene "Jangan tanya saya. Beri tahu kami apa yang Anda lakukan dan kami akan selesai dengan itu. Lalu kita akan pindah ke subjek lain."
        scene expression ("images/episode13/268_flirty_3.webp") with dissolve
        katrina "Jadi? Tersedak? Penghinaan? Suami yg istrinya tdk setia?"
        scene expression ("images/episode13/269_laugh_1.webp") with dissolve
        darlene "Itu harus lebih buruk. Mungkin wanita hamil?"
        scene expression ("images/episode13/268_laugh_3.webp") with dissolve
        katrina "Anda suka wanita hamil sialan, [toby!c]?"
        if katrina_path:
            scene expression ("images/episode13/270_normal_1.webp") with dissolve
            toby "Saya tidak tahu, apakah Anda hamil?"
        else:
            scene expression ("images/episode13/270_awkward_1.webp") with dissolve
            toby "Tidak, aku tidak!"
        scene expression ("images/episode13/268_horny_3.webp") with dissolve
        katrina "Saya tahu apa yang dia lakukan. Dia sepertinya bisa menjadi seorang eksibisionis atau mungkin voyeurisme?"
        scene expression ("images/episode13/269_smile_3.webp") with dissolve
        darlene "Dia suka perbudakan, mencambuk.Nah. Lihat dia. Dia terlalu keren dan mungkin sedikit gila."
        scene expression ("images/episode13/270_thinking.webp") with dissolve

        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit. That's right. This is the right moment to find out more about Katrina's BDSM club.{/i}"
        scene expression ("images/episode13/270_normal_2.webp") with dissolve
        toby "Bagus. Anda mendapatkan saya. Saya menjadi bdsm."
        scene expression ("images/episode13/268_surprised_3.webp") with dissolve
        katrina "Benar-benar? Itu menarik. Jadi Anda suka dicambuk, diikat ke kursi, memiliki ayam kecil Anda dimasukkan ke dalam kandang kecil?"
        scene expression ("images/episode13/270_normal_1.webp") with dissolve
        toby "Saya lebih suka berada di sisi lain dari itu. Saya suka menjadi orang yang memegang kendali."
        scene expression ("images/episode13/268_sad_3.webp") with dissolve
        katrina "Dan di sini saya berpikir saya menemukan diri saya mainan baru."
        scene expression ("images/episode13/269_normal_1.webp") with dissolve
        darlene "Anda sudah memiliki mainan yang seharusnya Anda sukai."
        scene expression ("images/episode13/268_smile_2.webp") with dissolve
        katrina "Oh, sayang. Anda bukan mainan. Anda adalah orang favorit saya di dunia."
        scene expression ("images/episode13/268_curious_3.webp") with dissolve
        katrina "Jadi apa yang paling Anda sukai dari seluruh BDSM ini?"
        scene expression ("images/episode13/270_normal_1.webp") with dissolve
        toby "Yah untuk memiliki bagian favorit, orang harus mencobanya terlebih dahulu, yang belum saya miliki. Saya belum menemukan pacar yang bersedia melakukan hal -hal ini."
        scene expression ("images/episode13/268_laugh_3.webp") with dissolve
        katrina "Siapa bilang itu harus menjadi pacarmu? Anda membutuhkan seorang gadis tak berdosa yang manis yang menunggu Anda di ruang tamu, sementara Anda memiliki pelacur di ruang bawah tanah."
        scene expression ("images/episode13/270_normal_1.webp") with dissolve
        toby "Aku tidak sakit. Saya bilang saya ingin tahu tentang bdsm tidak menculik."
        scene expression ("images/episode13/268_laugh_3.webp") with dissolve
        katrina "Siapa bilang sesuatu tentang penculikan? Ada banyak wanita yang rela tinggal di ruang bawah tanah menunggu perhatian semacam itu."
        scene expression ("images/episode13/268_curious_3.webp") with dissolve
        $ unlockImage(persistent.darlene_katrina_01)
        katrina "Jadi, seberapa besar Anda ingin memiliki pengalaman BDSM?"
        scene expression ("images/episode13/269_normal_1.webp") with dissolve
        darlene "Mengapa? Anda ingin membantunya?"
        scene expression ("images/episode13/268_laugh_2.webp") with dissolve
        katrina "Aku? Membantunya? Apakah kamu gila? Anda tahu saya suka memegang kendali."
        if katrina_path:
            scene expression ("images/episode13/270_normal_2.webp") with dissolve
            toby "Itu bagus karena dia bukan tipe saya."
            scene expression ("images/episode13/268_surprised_3.webp") with dissolve
            katrina "Bukan tipe Anda, bajingan? Anda akan menjadi pria paling beruntung yang hidup untuk memiliki wanita seperti saya."
            scene expression ("images/episode13/270_smile_1.webp") with dissolve
            toby "Apakah Anda mencoba meyakinkan saya bahwa saya ingin mengikat Anda ke meja dan melambang pantat Anda?"
            scene expression ("images/episode13/268_laugh_3.webp") with dissolve
            katrina "Anda tidak akan pernah mencambuk pantat saya."
            scene expression ("images/episode13/270_laugh_1.webp") with dissolve
            toby "Saya tidak mengatakan saya ingin melakukan itu. Aku bilang pantatmu dicambuk. Saya akan membayar orang lain untuk melakukannya untuk saya. Saya tidak berpikir Anda akan pantas mendapatkan waktu saya."
            scene expression ("images/episode13/268_angry_3.webp") with dissolve
            katrina "Anda bajingan, saya akan menunjukkan cara ...."
            scene expression ("images/episode13/269_normal_1.webp") with dissolve
            darlene "Ummm ... untungnya Anda punya pacar dan seperti yang Anda katakan, Anda tidak bisa membantunya."
            scene expression ("images/episode13/270_thinking.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I love to control Katrina, but now I should try and bring the BDSM club into the discussion. Maybe if I suggest that I heard something about it in the club it would be more credible.{/i}"
            scene expression ("images/episode13/270_curious_2.webp") with dissolve
            toby "Atau mungkin dia bisa."
        else:
            scene expression ("images/episode13/270_thinking.webp") with dissolve
            toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}What's going on here? It's clear that Darlene is suggesting the BDSM club, but maybe Katrina doesn't trust me yet. Maybe if I suggest that I heard something about it in the club it would be more credible.{/i}"
            scene expression ("images/episode13/270_curious_2.webp") with dissolve
            toby "Ya. Saya setuju. Mungkin dia bisa membantu saya."

        scene expression ("images/episode13/268_curious_3.webp") with dissolve
        katrina "Bagaimana saya bisa membantu Anda dan mengapa saya?"
        scene expression ("images/episode13/270_normal_1.webp") with dissolve
        toby "Saya mendengar beberapa rumor di klub tentang bagian pribadi."
        scene expression ("images/episode13/268_doubt_3.webp") with dissolve
        katrina "Tidak ada bagian pribadi klub."
        scene expression ("images/episode13/270_normal_1.webp") with dissolve
        toby "Persis seperti apa yang saya katakan kepada orang yang bertanya kepada saya tentang bagaimana dia bisa bergabung ... Saya tidak tahu apa yang dia sebut, klub bdsm."
        scene expression ("images/episode13/268_normal_3.webp") with dissolve
        katrina "Tidak ada hal seperti itu."
        stop music fadeout 2.0
        scene expression ("images/episode13/269_curious_1.webp") with dissolve
        darlene "..."
        scene expression ("images/episode13/268_normal_3.webp") with dissolve
        katrina "Jika ada yang bertanya tentang itu, Anda hanya menyuruh mereka pergi."
        scene expression ("images/episode13/270_thinking.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}She's way too defensive. She either hides it from Darlene, which is weird because she seemed like she knew, or she still doesn't trust me yet.{/i}"
        scene expression ("images/episode13/271.webp") with dissolve
        katrina "Ngomong -ngomong, sepertinya makanan kita akan datang."


    scene expression ("images/episode13/272.webp") with dissolve
    waitress "Selamat makan."
    darlene "Terima kasih."

    scene expression ("images/episode13/273.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}There's an awkward silence at the table.{/i}"
    scene expression ("images/episode13/274.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It looks like I poked the bear. I should let this cool down for a while, but I'm sure I'm on the right track.{/i}"
    scene expression ("images/episode13/275.webp") with dissolve
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe I could find a way to convince Katrina that I really want to join her club. But shit, how do I do that?{/i}"
    if toby_job == 0:
        scene expression ("images/episode13/274.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}How could I get access to Katrina? Maybe I should invite her on a double date and then somehow get some alone time with Katrina.{/i}"
        scene expression ("images/episode13/275.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe if she's drunk she'd be willing to talk more.{/i}"
        scene expression ("images/episode13/274.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But who should be my plus one? The best person for this job would be Sheila, because I can tell her my plan. No. This is a bad plan. I can't risk Katrina tying me to the cops.{/i}"
        scene expression ("images/episode13/275.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}It can't be Sheila. It has to be someone else, but I can't risk it. Katrina is dangerous.{/i}"
        scene expression ("images/episode13/274.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}So that won't work. Somehow I need to get Darlene to invite me over to their place, or even another lunch like this one. {/i}"
        scene expression ("images/episode13/275.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Maybe I could invite both of them to dinner to show my appreciation to Darlene.{/i}"
        scene expression ("images/episode13/274.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Shit... I need to think this through.{/i}"
    else:
        scene expression ("images/episode13/274.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck... Katrina doesn't trust me yet. She won't tell me anything about her other business, which is strange given the fact that she trusts me to be her errand boy for everything else.{/i}"
        scene expression ("images/episode13/275.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I mean, she trusts me enough to deliver her drugs, but she doesn't trust me with something less nefarious.{/i}"
        scene expression ("images/episode13/274.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Or maybe it's not less nefarious. Maybe this is actually worse. That's why she hides it.{/i}"
        scene expression ("images/episode13/275.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck. Why did I get myself into this mess?{/i}"
        scene expression ("images/episode13/274.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I shouldn't have agreed to help Sheila. She's a cop. She should do her job. Not get civilians involved.{/i}"
        scene expression ("images/episode13/275.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}But I do understand her. I would probably do the same if Tris were kidnapped.{/i}"
        scene expression ("images/episode13/274.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Fuck! Fuck! Fuck! How can I earn Katrina's trust to tell me more about the BDSM club?{/i}"
    scene expression ("images/episode13/276.webp") with dissolve
    darlene "Apakah kamu baik -baik saja? Apakah semuanya baik -baik saja?"
    scene expression ("images/episode13/277.webp") with dissolve
    toby "Ummm ... ya. Tidak, saya baik -baik saja. Jangan khawatir. Saya hanya merasa tidak enak bahwa saya merusak makanan ini untuk Anda berbicara tentang fetish bodoh saya. Aku seharusnya tidak membawanya."
    if toby_job == 0:
        scene expression ("images/episode13/276.webp") with dissolve
        darlene "Anda tidak merusak apapun. Jangan khawatir."
        darlene "Ngomong -ngomong, setelah kita selesai makan, aku tidak akan kembali ke kantor. Saya mengadakan pertemuan dengan klien, jadi Anda harus kembali dan mulai memanggil pemilik apartemen tersebut."
        scene expression ("images/episode13/277.webp") with dissolve
        toby "Pasti."
    else:
        scene expression ("images/episode13/278.webp") with dissolve
        katrina "Anda tidak merusak apapun. Untuk apa layak Anda membuatnya lebih menarik."
        katrina "Ngomong -ngomong, setelah kita selesai saya akan memiliki beberapa bisnis untuk diperhatikan. Jadi Anda harus kembali ke klub dan memastikan semua orang berperilaku dan tidak ada yang membawa barang -barang di luar di klub."
        katrina "Dan jika seseorang bertanya kepada Anda tentang BDSM dan hal -hal konyol seperti itu, katakan saja mereka untuk bercinta."
        scene expression ("images/episode13/279.webp") with dissolve
        toby "Ya tentu."

    return

label episode13_work_0_2:
    scene expression ("images/episode13/280.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Okay, so two more people to convince and I'm done for the day.{/i}"
    scene expression ("images/episode13/281.webp") with dissolve


    darlene "Hai, [toby!c]. Apa yang masih kamu lakukan di sini?"
    scene expression ("images/episode13/282.webp") with dissolve
    toby "Nah, Anda mengatakan kepada saya untuk meyakinkan pemilik untuk membiarkan kami menjual apartemen mereka, dan itulah yang telah saya lakukan."
    scene expression ("images/episode13/283.webp") with dissolve
    darlene "Sudah jam 9 o \ 'sudah. Pulang dan aku akan menyelesaikannya besok pagi."
    scene expression ("images/episode13/284.webp") with dissolve
    toby "Saya hanya memiliki dua orang lagi untuk diajak bicara dan saya akan selesai."
    scene expression ("images/episode13/283.webp") with dissolve
    darlene "Sudah terlambat. Orang -orang tidak ingin dipanggil pada jam 9 o \ 'dan Anda lelah."
    scene expression ("images/episode13/285.webp") with dissolve
    toby "Saya tidak menyadari betapa terlambatnya itu. Ya, saya kira sudah waktunya pulang."
    toby "Saya memperbarui jadwal Anda untuk besok jadi Anda tahu pertemuan apa yang Anda miliki."
    darlene "Anda berhasil meyakinkan semuanya?"
    toby "Ya. Beberapa dari mereka membutuhkan sedikit bujukan ekstra, tetapi pada akhirnya semuanya berhasil."
    darlene "Saya tahu Anda adalah pria untuk pekerjaan ini."
    scene expression ("images/episode13/286.webp") with dissolve
    darlene "Dan [toby!c]. Maaf sore ini. Aku tidak tahu Kat akan menekanmu untuk membicarakan hal itu."
    toby "Jangan khawatir. Saya anak laki -laki besar. Saya bisa menjaga diri saya sendiri."
    if darlene_path:
        label memory_49:


            scene expression ("images/episode13/287.webp") with dissolve
            toby "Sementara kita tentang masalah ini, apakah dia mencurigai sesuatu? Maksudku, dia bertingkah agak aneh dan dia tampak hampir cemburu."
            darlene "Kenapa dia mencurigai sesuatu? Apakah ada yang dicurigai?"
            scene expression ("images/episode13/288_1.webp") with dissolve
            toby "Aku tidak tahu. Anda memberi tahu saya. Apakah dia curiga aku ingin mencium bibirmu?"
            scene expression ("images/episode13/288_2.webp") with dissolve
            darlene "Tidak, dia tidak mencurigai hal seperti itu. Maksudku, apakah kamu akan mencium bibirku untuk memberinya sesuatu untuk dicurigai?"
            scene expression ("images/episode13/288_1.webp") with dissolve
            toby "Apakah Anda ingin saya memberinya sesuatu untuk dicurigai?"
            scene expression ("images/episode13/289.webp") with dissolve
            darlene "Aku tidak tahu. Saya akan membiarkan Anda memutuskan."
            show ep13_290
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode13/290.webp") with dissolve
            toby "Beri tahu saya jika dia mencurigai itu."
            darlene "Aku akan memberitahumu besok."
            toby "Saya harus pergi sekarang."
            darlene "Ya, kamu harus."
            $ unlockImage(persistent.darlene_08)
            hide ep13_290
            $ unlockMemory(persistent.memory_49)
            $ renpy.end_replay()

    scene expression ("images/episode13/291.webp") with dissolve
    toby "Jadi, jam berapa saya harus masuk?"
    scene expression ("images/episode13/292.webp") with dissolve
    darlene "Nah karena Anda melakukannya dengan sangat baik dengan klien -klien ini, datanglah sebentar lagi di pagi hari untuk menyelesaikan 2 terakhir Anda dan Anda dapat libur sisa hari ini."
    scene expression ("images/episode13/291.webp") with dissolve
    toby "Oke kalau begitu. Sampai jumpa besok pagi."
    scene expression ("images/episode13/292.webp") with dissolve
    darlene "Selamat malam [toby!c]."
    scene expression ("images/episode13/291.webp") with dissolve
    toby "Selamat malam!"

    return

label episode13_work_1_2:
    scene expression ("images/episode13/293.webp") with dissolve
    hide screen ui_message
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}This is getting boring. The club is empty. I mean it's a Monday. Who the fuck comes to a club on a Monday?{/i}"
    toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}I still think Katrina keeps the club open just to launder money she gets from the drug business.{/i}"

    scene expression ("images/episode13/294.webp") with dissolve
    katrina "Apa yang masih kamu lakukan di sini?"
    scene expression ("images/episode13/295.webp") with dissolve
    toby "Nah, Anda bilang pastikan semuanya baik -baik saja."
    scene expression ("images/episode13/296.webp") with dissolve
    katrina "Saya memiliki pengawal untuk itu. Bisakah Anda melihat ada seperti 5 orang di sini?"
    toby "Ya, tapi Anda mengatakan kepada saya untuk memastikan semuanya berjalan dengan baik, jadi itulah yang saya lakukan."
    katrina "Pulang saja."
    toby "Saya pikir kami memiliki banyak bisnis untuk diurus hari ini?"
    scene expression ("images/episode13/297.webp") with dissolve
    katrina "Kami akan melakukannya besok. Sesuatu muncul dan saya harus mengubah rencana saya. Saya tidak tahu apa lagi yang bisa saya lakukan, jadi saya katakan untuk mengawasi klub."
    toby "Ya. Saya pikir ini bukan apa yang telah Anda rencanakan untuk saya hari ini."
    katrina "Nah, Anda harus mendapatkan uang Anda dalam beberapa cara, bukan?"
    toby "Yup."
    scene expression ("images/episode13/298.webp") with dissolve
    toby "Jadi haruskah saya pulang sekarang?"
    scene expression ("images/episode13/299.webp") with dissolve
    katrina "Tentu. Sampai jumpa besok pagi."
    scene expression ("images/episode13/298.webp") with dissolve
    toby "Jam berapa saya harus masuk?"
    scene expression ("images/episode13/299.webp") with dissolve
    katrina "Mari kita katakan 10. Kita masih memiliki banyak hal yang harus dilakukan."
    scene expression ("images/episode13/300.webp") with dissolve
    toby "Oke ... sampai jumpa besok."
    if katrina_path:
        label memory_50:


            scene expression ("images/episode13/301.webp") with dissolve
            katrina "Hanya karena penasaran, wanita macam apa yang Anda suka?"
            scene expression ("images/episode13/302.webp") with dissolve
            toby "Anda ingin tahu jika Anda tipe saya?"
            scene expression ("images/episode13/301.webp") with dissolve
            katrina "Tolong jalang. Saya bukan remaja konyol yang perlu disukai oleh semua orang."
            scene expression ("images/episode13/303.webp") with dissolve
            toby "TIDAK? Anda tidak? Karena saya bisa bersumpah bahwa Anda ingin saya menyukai Anda."
            scene expression ("images/episode13/304.webp") with dissolve
            katrina "Itu lebih penting.Anda mengigau. Saya tidak perlu disukai. Saya takut."
            toby "Ya, itu, tapi tidak ada gunanya jika Anda tidak ditakuti oleh orang yang Anda inginkan."
            scene expression ("images/episode13/305.webp") with dissolve
            katrina "Jangan membuatku tertawa. Tindakan tangguh Anda adalah omong kosong."
            toby "Berhentilah aksi, pelacur. Anda menginginkan saya. Anda ingin saya mengendalikan Anda."
            scene expression ("images/episode13/306.webp") with dissolve
            toby "Vagina Anda basah saat saya memberi tahu Anda bahwa saya akan membuat Anda dicambuk. Saya bisa mencium aroma jus vagina Anda dari bawah meja."
            show ep13_307
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode13/307.webp") with dissolve
            toby "Sekarang hubungi Lapdog Anda dan katakan padanya untuk membawamu beberapa borgol, karena saya punya hadiah untuk Anda."
            katrina "Anda adalah lapdog saya. Jadi Anda mengambil beberapa borgol."
            hide ep13_307
            scene expression ("images/episode13/308.webp") with dissolve
            toby "Jika neal tidak ada di sini dengan borgol dalam 2 menit ke depan, saya akan pulang."
            scene expression ("images/episode13/309.webp") with dissolve
            katrina "Beri aku itu."
            scene expression ("images/episode13/310.webp") with dissolve
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nDon't you \"WHAT\"Saya. Anda memiliki satu menit untuk membawakan saya beberapa borgol ke bagian VIP."
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\n..."
            katrina "{size=12}{color=#FDCA6E}* on the phone *{/color}{/size}\nYeah, of course it's me, you moron."
            scene expression ("images/episode13/311_1.webp") with dissolve
            katrina "Apakah kamu bahagia sekarang?"
            scene expression ("images/episode13/311_2.webp") with dissolve
            toby "Belum."
            toby "Saya akan senang ketika Neal membawa borgol."
            scene expression ("images/episode13/312.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode13/313.webp") with dissolve
            $ ui.saybehavior()
            $ ui.interact()
            scene expression ("images/episode13/314.webp") with dissolve
            neal "Ini dia, ma \ 'am."
            scene expression ("images/episode13/315.webp") with dissolve
            toby "Terima kasih."
            toby "Sekarang, tinggalkan kami. Kami memiliki beberapa hal yang harus diurus."
            scene expression ("images/episode13/316.webp") with dissolve
            neal "Bu?"
            scene expression ("images/episode13/317.webp") with dissolve
            katrina "Anda mendengar pria itu. Meninggalkan!"
            scene expression ("images/episode13/318_1.webp") with dissolve
            toby "Sekarang, dimana kita?"
            scene expression ("images/episode13/318_2.webp") with dissolve
            katrina "..."
            scene expression ("images/episode13/318_3.webp") with dissolve
            toby "Kamu bisa bicara sayang. Katakan padaku apa yang kamu ingin aku lakukan."
            scene expression ("images/episode13/319.webp") with dissolve
            katrina "Saya ingin Anda mengikat saya ke pegangan dan kemudian kami bercinta."
            scene expression ("images/episode13/320_1.webp") with dissolve
            toby "Seperti ini?"
            scene expression ("images/episode13/320_2.webp") with dissolve
            katrina "Ya!"
            $ unlockImage(persistent.katrina_08)
            scene expression ("images/episode13/321.webp") with dissolve
            toby "Sayang sekali kamu tidak tahu bagaimana menjawab pertanyaan itu. Ketika aku bertanya padamu, \"Apa yang kamu ingin aku lakukan?\", kamu menjawab, \"Terserah Anda mau yang mana, Tuan!\"
            toby "Bisnis adalah bisnis dan kesenangan adalah kesenangan. Anda adalah bos ketika kami melakukan bisnis dan saya menghormatinya."
            toby "Tetapi ketika kami bersenang -senang, saya bertanggung jawab sehingga Anda harus menghormati saya. Hubungan ini atau apa pun itu, hanya bisa bekerja seperti ini. Dipahami?"
            scene expression ("images/episode13/322.webp") with dissolve
            katrina "Anda cukup beruntung sehingga saya membiarkan Anda meniduri saya.Hormati kamu? Saya bos Anda. Anda harus mencium kakiku."
            katrina "Sekarang lutut dan lutut. Saya ingin vagina saya menjilat."
            scene expression ("images/episode13/323.webp") with dissolve
            toby "Hampir menyakitkan saya bahwa Anda tidak pantas mendapatkan kacau. Jadi sayangnya saya harus mengajari Anda pelajaran."
            toby "Harap dipahami bahwa ini tidak memberi saya kesenangan. Saya melakukan ini untuk kebaikan Anda sendiri."
            scene expression ("images/episode13/324.webp") with dissolve
            toby "Saya akan pergi sekarang, dan Anda dapat memikirkan apa yang Anda lakukan salah."
            scene expression ("images/episode13/325.webp") with dissolve
            katrina "Buka aku saat ini!"
            scene expression ("images/episode13/324.webp") with dissolve
            toby "Saya akan sayang, tetapi Anda belum belajar pelajaran Anda."
            scene expression ("images/episode13/325.webp") with dissolve
            katrina "Jika Anda tidak membiarkan saya keluar dari manset ini sekarang, saya bersumpah saya akan membunuh Anda."
            scene expression ("images/episode13/326.webp") with dissolve
            toby "Tidak, Anda tidak. Karena jauh di dalam, Anda sangat senang. Anda suka kehilangan kendali dan tidak ada pria lain yang akan berpikir untuk melakukan ini kepada Anda."
            toby "Karena semua pria di sekitar Anda takut pada Anda. Satu -satunya orang yang tidak takut padamu adalah Darlene, dan itulah sebabnya kamu mencintainya."
            toby "Jadi Anda tidak akan berisiko kehilangan satu -satunya pria yang dapat memuaskan Anda."
            scene expression ("images/episode13/327.webp") with dissolve
            katrina "[toby!c]! Demi fuck. Saya bersumpah jika Anda pergi, Anda akan menyesalinya."
            scene expression ("images/episode13/326.webp") with dissolve
            toby "Jangan khawatir, saya pasti akan memberi tahu Neal bahwa Anda tidak akan terganggu, sehingga Anda dapat memiliki waktu untuk memikirkan kesalahan Anda."
            $ unlockMemory(persistent.memory_50)
            $ renpy.end_replay()

        scene expression ("images/episode13/328_1.webp") with fade
        toby "Hai teman, maaf atas apa yang terjadi di lantai atas, tetapi Katrina ingin mengajari saya pelajaran. Dia mengatakan sesuatu tentang tidak cukup manusia. Dia mengatakan bahwa saya harus belajar bagaimana memberi perintah."
        toby "Jadi itu sebabnya saya adalah keledai di lantai atas dan sekarang dia mengatakan kepada saya untuk datang ke sini dan memberi Anda pesanan lain. Tetapi menurut pendapat saya, kami hanya membuat karyawan, dan itu membuat kami setara. Saya bukan bos Anda untuk memberi Anda perintah."
        toby "Jadi inilah yang akan kami lakukan. Dia ingin mendapatkan pizza dari tempat pizza yang sangat dia cintai dari Srausea."
        scene expression ("images/episode13/328_2.webp") with dissolve
        neal "Tapi itu seperti 2 jam jauhnya."
        scene expression ("images/episode13/328_1.webp") with dissolve
        toby "Aku tahu. Persis seperti yang saya katakan padanya. Terlambat, tidak ada yang mau pergi ke sana, tetapi dia bersikeras bahwa saya memberi Anda pesanan ini, jadi di sinilah saya, tetapi saya bertanya dengan baik."
        scene expression ("images/episode13/328_2.webp") with dissolve
        neal "Dia memberitahumu untuk memberi saya pesanan? Anda?"
        scene expression ("images/episode13/328_1.webp") with dissolve
        toby "Lihatlah, Anda telah melihat bagaimana dia bertindak ketika saya mencoba memerintahkan Anda untuk pergi. Saya terjebak di tengah. Apa yang Anda ingin saya lakukan?"
        toby "Saya tidak suka memerintah orang -orang di sekitar, saya tidak suka itu, jadi saya hanya di sini meminta Anda dengan baik untuk membawakan pizza padanya."
        scene expression ("images/episode13/329.webp") with dissolve
        neal "Sial ... aku benci menjadi pesona."
        toby "Aku tahu kawan, itu sebabnya jika aku jadi kamu, aku akan mendapatkan pizza dari tempat lain lalu pergi menonton film atau sesuatu dan setelah dua jam membawanya padanya."
        toby "Tapi letakkan di atas piring sehingga dia tidak akan tahu dari mana sebenarnya berasal."
        neal "Tidakkah menurutmu dia akan memperhatikan?"
        toby "Aku akan memberinya beberapa minuman sehingga dia mabuk. Dia bahkan tidak akan memperhatikan perbedaannya."
        scene expression ("images/episode13/330.webp") with dissolve
        neal "Terima kasih man."
        toby "Anda tidak harus berterima kasih kepada saya. Seperti yang saya katakan. Aku bukan bosmu."
        scene expression ("images/episode13/331.webp") with dissolve
        neal "Kalau begitu aku akan mendapatkan pizza itu."
        toby "Ya, lakukan itu."
        scene expression ("images/episode13/332.webp") with dissolve
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Idiot! She's going to have you skinned for keeping her tied to a handrail for two hours and then the only thing that could possibly calm her down would be that pizza she loves so much, but I guess it's a shame she won't be getting it.{/i}"
        toby "{size=12}{color=#FDCA6E}* thinking *{/color}{/size}\n{i}Looks like it's time to go home.{/i}"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
