image sfbja:
    "sfbj0000.jpg"
    pause 0.01
    "sfbj0001.jpg"
    pause 0.01
    "sfbj0002.jpg"
    pause 0.01
    "sfbj0003.jpg"
    pause 0.01
    "sfbj0004.jpg"
    pause 0.01
    "sfbj0005.jpg"
    pause 0.01
    "sfbj0006.jpg"
    pause 0.01
    "sfbj0007.jpg"
    pause 0.01
    "sfbj0008.jpg"
    pause 0.01
    "sfbj0009.jpg"
    pause 0.01
    "sfbj0010.jpg"
    pause 0.01
    "sfbj0011.jpg"
    pause 0.01
    "sfbj0012.jpg"
    pause 0.01
    "sfbj0013.jpg"
    pause 0.01
    "sfbj0014.jpg"
    pause 0.01
    "sfbj0015.jpg"
    pause 0.01
    "sfbj0016.jpg"
    pause 0.01
    "sfbj0017.jpg"
    pause 0.01
    "sfbj0018.jpg"
    pause 0.01
    "sfbj0019.jpg"
    pause 0.01
    "sfbj0020.jpg"
    pause 0.01
    "sfbj0021.jpg"
    pause 0.01
    "sfbj0022.jpg"
    pause 0.01
    "sfbj0023.jpg"
    pause 0.01
    "sfbj0024.jpg"
    pause 0.01
    "sfbj0025.jpg"
    pause 0.01
    "sfbj0026.jpg"
    pause 0.01
    "sfbj0027.jpg"
    pause 0.01
    "sfbj0028.jpg"
    pause 0.01
    "sfbj0029.jpg"
    pause 0.01
    "sfbj0030.jpg"
    pause 0.01
    "sfbj0031.jpg"
    pause 0.01
    "sfbj0032.jpg"
    pause 0.01
    "sfbj0033.jpg"
    pause 0.01
    "sfbj0034.jpg"
    pause 0.01
    "sfbj0035.jpg"
    pause 0.01
    "sfbj0036.jpg"
    pause 0.01
    "sfbj0037.jpg"
    pause 0.01
    "sfbj0038.jpg"
    pause 0.01
    "sfbj0039.jpg"
    pause 0.01
    "sfbj0040.jpg"
    pause 0.01
    "sfbj0041.jpg"
    pause 0.01
    "sfbj0042.jpg"
    pause 0.01
    "sfbj0043.jpg"
    pause 0.01
    "sfbj0044.jpg"
    pause 0.01
    "sfbj0045.jpg"
    pause 0.01
    "sfbj0046.jpg"
    pause 0.01
    "sfbj0047.jpg"
    pause 0.01
    "sfbj0048.jpg"
    pause 0.01
    "sfbj0049.jpg"
    pause 0.01
    "sfbj0050.jpg"
    pause 0.01
    repeat


label slunchplus:
    b "Bagaimana Anda menginginkannya?"
    s "Apa maksudmu?"
    b "Maksud saya, saya akan membiarkan Anda memilih kali ini"
    menu:
        "Coba di lantai" if sdom >=150 and srel >=400:
            scene sfbja
            s "Uhh"
            "..."
            b "Yesss"
            s "Ughh"
            "..."
            b "Ahhh fuck!"
            scene slunchedend with fade
            s "Hhh"
            b "Terima kasih atas hadiahnya"
            scene broom_day with fade
            "..."
            call screen gnav
        "Duduk":


            scene slunched3 with dissolve
            "..."
            s "Ughh"
            scene slunched4 with dissolve
            b "Ahhh"
            scene slunched5 with fade
            s "Grrr"
            b "Hehe"
            b "Terima kasih atas hadiahnya"
            scene broom_day with fade
            "Ada pilihan lain selain duduk"
            "Jika Anda tidak mendapatkannya menaikkan poin DOM Anda menjadi 150 dan hubungan menunjuk ke 400"
            call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
