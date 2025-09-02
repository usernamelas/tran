label chprb:
    scene cprb with fade
    c "Hi [mname]"
    m "Hai, tolong masuk"
    c "Saya tidak punya waktu"
    c "Saya di sini untuk hal lain"
    m "Apa itu?"
    scene cprb1 with dissolve
    c "Lihat..."
    c "Saya tahu segalanya tentang sifat pekerjaan Anda"
    c "Dan Anda hanya beruntung adalah bahwa saya tidak bisa mencapai Stewart"
    c "Dan begitu saya berhasil menghubunginya, saya akan langsung memberi tahu dia tentang semua ini"
    m "Tetapi..."
    c "Itu semua, sampai jumpa"
    scene cprb2 with dissolve
    b "{i} (Saya harus melakukan sesuatu) {/i}"
    scene cprb3 with dissolve
    m "Anda di sini?"
    b "Ya dan saya mendengar segalanya"
    b "Saya akan memperbaikinya"
    m "Bagaimana Anda akan melakukannya"
    b "Saya akan mengikuti dan berbicara dengannya"
    m "Hmmm"
    b "Biarkan saya mencoba"
    scene cprb4 with dissolve
    m "{i} (Saya kira saya tidak akan rugi) {/i}"
    m "{i} (itu bisa menjadi kesempatan terakhir) {/i}"
    m "Oke, lakukanlah"
    scene cprb5 with dissolve
    b "Wait"
    scene cprb6 with dissolve
    c "Apa itu?"
    if persistent.patch_enabled:
        b "Dengar, tolong jangan beri tahu ayah tentang ini"
        pass
    else:
        b "Dengar, tolong jangan beri tahu Stewart tentang ini"
        pass
    c "Mengapa tidak?"
    b "Tolong, jangan katakan padanya untuk saat ini"
    b "Aku akan memberitahumu mengapa nanti"
    $ bnamefixcheryl = 1
    b "I promise"
    scene cprb7 with dissolve
    c "Hmm"
    b "Apa yang kamu katakan?"
    scene cprb6 with dissolve
    c "Ok"
    b "Terima kasih"
    scene cprb8 with fade
    b "Selesai, saya meyakinkannya"
    m "Apa kamu yakin?"
    b "Ya dia menang"
    m "Apa yang Anda katakan padanya"
    b "Jangan khawatir tentang hal itu, yang penting adalah dia tidak akan memberitahunya"
    m "Hmm"
    m "Ok"
    scene cprb9 with dissolve
    m "Baiklah saya akan tidur"
    b "..."
    menu:
        "Pergi tidur":
            scene broom_night with fade
            b "{i} (...) {/i}"
            jump newdays
        "Tonton film dan tunggu [sname] muncul":
            scene eom1 with fade
            "..."
            scene eom2 with dissolve
            s "Astaga!"
            s "Apa yang kamu tonton!?"
            b "Film romansa"
            pass
    scene eom3 with dissolve
    s "Sepertinya lebih dari film porno"
    b "Jadi apa, itu keren"
    if persistent.patch_enabled:
        s "Apakah Anda takut ibu melihat Anda?"
        pass
    else:
        s "Apakah Anda takut [mname] melihat Anda?"
        pass
    b "Dia tidur"
    s "OK"
    b "Saya mendapatkan bir, apakah Anda menginginkannya?"
    s "Yes please"
    scene eom4 with dissolve
    s "..."
    scene eom5 with dissolve
    s "Eww apakah kamu serius!"
    b "Ya, itu bagus"
    scene eom6 with dissolve
    s "It's dirty"
    b "Kotor itu panas"
    b "Saya bisa melakukan ini dengan Anda jika Anda mau"
    scene eom5 with dissolve
    s "Anda gila"
    b "Tidak, aku tidak"
    scene eom7 with dissolve
    "..."
    scene eom8 with dissolve
    s "Menjilati atau jari?"
    scene eom12 with dissolve
    b "..."
    scene eom8 with dissolve
    b "Keduanya!"
    s "Dapatkan kami satu bir"
    scene eom13 with fade
    "..."
    scene eom9 with fade
    "..."
    b "Jadi Anda tidak menjawab saya?"
    s "Jawab Apa?"
    b "Anda ingin jari atau menjilati?"
    b "Atau ini?"
    s "Eww"
    b "Jangan \ t eww saya, saya ingin membuktikan bahwa rasanya menyenangkan"
    s "[bname] Apa hal yang kita tonton ini?"
    s "Bagaimana jika [mname] datang?"
    if srel >=250:
        b "Jangan khawatir dia menang"
        "..."
        scene eom14 with hpunch
        s "[bname]! Saya pikir saya mabuk"
        b "2 bir?"
        b "Dengan serius?"
        s "Tolong bawa saya ke kamar saya"
        scene eom15 with dissolve
        s "Bawa aku"
        scene eom25 with hpunch
        s "Ahhh"
        b "Apa?"
        s "I'm OK"
        s "Bawa aku"
        scene eom26 with fade
        "..."
        scene eom27 with dissolve
        "..."
        scene sroompier6 with fade
        s "Ahhh"
        scene eom28 with dissolve
        b "Mhhm"
        s "DAPATKAN DI SINI [bname]"
        scene eom29 with dissolve
        s "Tidak .. ah"
        s "Masukkan ke dalam"
        scene eom30 with fade
        s "..."
        scene eom31 with vpunch
        s "Ahhh"
        scene sroompier12 with fade
        b "..."
        b "Selamat malam"
        scene broom_night with fade
        b "{i} (i \ 'll pergi tidur) {/i}"
        jump newdays
    else:


        scene eom10 with dissolve
        s "Tolong ubah"
        b "Mengapa?"
        s "Ubah saja"
        b "Saya tidak menginginkannya"
        s "Lalu aku pergi"
        scene eom11 with dissolve
        b "Apa -apaan!"
        "Naikkan poin hubungan Anda menjadi 250"
        scene broom_night with fade
        b "{i} (saya kira saya akan tidur) {/i}"
        jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc