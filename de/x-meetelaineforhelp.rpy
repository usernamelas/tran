label meetelaineforhelp:
    scene ehelp with fade
    e "Apa itu [bname]"
    b "Mari kita duduk dan berbicara"
    scene ehelp1 with fade
    $ persistent.unlock_40 = True
    "Anda memberi tahu dia tentang masalah dengan Cheryl"
    e "Benar-benar?"
    b "Ya, itulah yang terjadi"
    e "Sayangku kau mengacaukannya"
    e "Sepertinya dilema Anda sekarang"
    b "Jadi apa? Apakah Anda akan membantu?"
    e "Ya, tapi bagaimana dengan Cheryl, tahukah Anda di mana dia tinggal?"
    b "Yes"
    e "Apakah dia punya teman di sini?"
    b "Ya Melinda, pemilik kedai kopi"
    b "Dan toko telepon"
    e "Hmm"
    e "Biarkan saya melihat apa yang bisa saya lakukan"
    e "Beri aku waktu"
    b "Ok tapi tolong buat cepat"
    e "Mungkin sampai versi berikutnya"
    b "Baiklah, saya harap kita bisa menunggu"
    $ bnamefixcheryl = 2
    jump broom_menu


label meetelaineforhelp1:
    scene ehelp3 with fade
    e "Hi [bname]"
    b "Hi"
    e "Sit"
    $ persistent.unlock_42 = True
    scene ehelp4 with dissolve
    e "Saya pikir saya memiliki sesuatu yang bisa kita gunakan untuk ..."
    scene ehelp5 with dissolve
    e "... buat Cheryl ..."
    b "Err"
    scene ehelp4 with dissolve
    e "... Ubah Pikirannya"
    b "Dimana Rob?"
    scene ehelp6 with dissolve
    e "Jangan khawatir dia mengunjungi saudara perempuannya"
    e "Dia tidak akan segera berada di sini"
    b "Oke, jadi apa yang kamu katakan padaku"
    scene ehelp4 with dissolve
    e "Saya pikir Cheryl terhubung dengan pemilik kedai kopi"
    b "Maksudmu Melinda?"
    e "Yes"
    b "Saya tahu itu"
    e "Apa yang kamu tahu?"
    b "Saya tahu bahwa mereka adalah teman"
    scene ehelp6 with dissolve
    e "Ya tapi saya merasa ada sesuatu yang lebih dari persahabatan di antara mereka"
    b "Apa maksudmu?"
    e "Saya tidak tahu tetapi kita harus mencari tahu"
    e "Anda harus menonton Melinda itu, jika Anda ingin menemukan sesuatu"
    b "Hmm"
    $ bnamefixcheryl = 4
    b "Saya akan"
    e "Mereka biasanya hangout di dekat toko manis dan toko roti"
    b "Ok"
    e "Beri tahu saya jika Anda membutuhkan bantuan"
    b "Sure"
    e "Anda bisa pergi sekarang"
    scene ehelp2 with fade
    e "Kecuali Anda ingin menemani saya sampai Rob kembali"
    b "Hmm"
    menu:
        "Tinggal":
            scene ehelp7 with dissolve
            b "Ok"
            scene ehelp8 with hpunch
            e "Sit"
            scene ehelp9 with dissolve
            b "..."
            scene ehelp10 with dissolve
            "..."
            scene ehelp11 with dissolve
            e "Ahh"
            scene ehelp12 with fade
            e "Apakah kamu dekat?"
            b "Yes"
            scene ehelp13 with dissolve
            b "Aku akan pergi"
            scene ehelp14 with hpunch
            b "Cum"
            scene ehelp2 with fade
            e "Sampai jumpa"
            jump broom_menu
        "Meninggalkan":

            b "Saya harus pergi"
            e "Ok"
            jump broom_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
