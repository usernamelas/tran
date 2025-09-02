label onlineshop:
    scene black
    "..."
    menu:
        "Tidak perlu membeli apapun saat ini":
            "..."
            jump broom_menu


        "Beli sesuatu untuk [nama]" if mnvylingerie ==0 and mfuckedsober >=1:
            scene menvy with fade
            b "Hmm"
            b "100 $"
            b "Ok"
            menu:
                "Beli" if mny>=100:
                    $ mny -= 100
                    b "Saya akan segera mendapatkannya"
                    $ mnvylingerie = 1
                    jump broom_menu
                "Tidak ada uang sekarang":

                    b "Saya akan meninggalkannya sampai nanti"
                    jump broom_menu

        "Beli pakaian dalam untuk [mname]" if springstring ==0:
            scene spstring with fade
            b "Hmm"
            b "100 $"
            b "Ok"
            menu:
                "Beli" if mny>=100:
                    $ mny -= 100
                    b "Saya akan segera mendapatkannya"
                    $ springstring = 1
                    jump broom_menu
                "Tidak ada uang sekarang":

                    b "Saya akan meninggalkannya sampai nanti"
                    jump broom_menu


        "Beli cermin untuk [mname]" if mmirror ==1:
            b "Hmm"
            b "100 $"
            b "Ok"
            menu:
                "Beli" if mny>=100:
                    $ mny -= 100
                    b "Saya akan segera mendapatkannya"
                    $ mmirror = 2
                    jump broom_menu
                "Tidak ada uang sekarang":

                    b "Saya akan meninggalkannya sampai nanti"
                    jump broom_menu




        "Pesan kamera untuk aula" if gnight >=2 and hallcamera ==0:
            b "Hmm"
            b "100 $"
            b "Ok"
            menu:
                "Beli" if mny>=100:
                    $ mny -= 100
                    b "Itu harus tiba besok"
                    $ hallcamera = 1
                    jump broom_menu
                "Tidak ada uang sekarang":

                    b "Saya akan meninggalkannya sampai nanti"
                    jump broom_menu


        "Pesan kamera untuk aula" if smalonenight >=4  and hallcamera ==0:
            b "Hmm"
            b "100 $"
            b "Ok"
            menu:
                "Beli" if mny>=100:
                    $ mny -= 100
                    b "Itu harus tiba besok"
                    $ hallcamera = 1
                    jump broom_menu
                "Tidak ada uang sekarang":

                    b "Saya akan meninggalkannya sampai nanti"
                    jump broom_menu


        "Pesan beberapa minuman keras untuk malam perempuan" if strongdrinksforgirlnight == 1:
            b "Hmm"
            b "100 $"
            b "Ok"
            menu:
                "Beli" if mny>=100:
                    $ mny -= 100
                    b "Itu harus tiba besok"
                    $ strongdrinksforgirlnight = 2
                    jump broom_menu
                "Tidak ada uang sekarang":

                    b "Saya akan meninggalkannya sampai nanti"
                    jump broom_menu

        "Pesan minuman keras untuk [sname]" if snamedrink == 1:
            b "Hmm"
            b "75 $"
            b "Ok"
            menu:
                "Beli" if mny>=75:
                    $ mny -= 75
                    b "Itu harus tiba besok"
                    $ snamedrink = 2
                    jump broom_menu
                "Tidak ada uang sekarang":

                    b "Saya akan meninggalkannya sampai nanti"
                    jump broom_menu



        "Pesan driver sekrup" if toidoorscrew ==1:
            b "Hmm"
            b "Ini seharusnya membantu pintu toilet"
            b "20 $"
            menu:
                "Beli" if mny>=20:
                    $ mny -= 20
                    b "Itu harus tiba besok"
                    $ toidoorscrew = 2
                    jump broom_menu
                "Tidak ada uang sekarang":

                    b "Saya akan meninggalkannya sampai nanti"
                    jump broom_menu

        "Memesan sesuatu untuk [sname]" if spiercings ==0:
            scene spiercing with fade
            b "40 $"
            menu:
                "Beli" if mny>=40:
                    $ mny -= 20
                    b "Itu harus segera tiba"
                    b "Saya berharap dia akan menyukainya"
                    $ spiercings = 1
                    jump broom_menu
                "Tidak ada uang sekarang":

                    b "Saya akan meninggalkannya sampai nanti"
                    jump broom_menu

        "Beli pakaian perawat untuk [mname]" if mnurse_im == 1 and mnurseoutfit ==0:
            scene nurse with fade
            b "100 $"
            menu:
                "Beli" if mny >=100:
                    $ mny -= 100
                    b "Itu harus tiba dalam 2 hari"
                    b "Saya berharap dia akan menyukainya"
                    $ mnurseoutfit = 1
                    jump broom_menu
                "Tidak ada uang sekarang":

                    b "Saya akan meninggalkannya sampai nanti"
                    jump broom_menu

        "Dapatkan sesuatu untuk disimpan [sname] di rumah pada hari Minggu" if beachalone == 1:
            b "Mari kita lihat"
            scene giftcard with dissolve
            b "Apa -apaan, hanya satu denominasi!"
            b "200 $"
            menu:
                "Beli" if mny >=200:
                    $ mny -= 00
                    b "Received"
                    b "Saya berharap ini akan melakukan trik"
                    b "Saya akan memberikannya saat makan siang pada hari Sabtu"
                    $ beachalone = 2
                    jump broom_menu
                "Tidak ada uang sekarang":

                    b "Saya akan meninggalkannya sampai nanti"
                    jump broom_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc