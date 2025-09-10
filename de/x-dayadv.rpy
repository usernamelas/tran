label dayadv:
    scene black
    menu:
        "Maju 1 jam":
            $ Hour +=1
            "Waktu Maju Satu Jam"
            if Hour >=21:
                $ Hour =21
                jump broom_menu
            else:
                pass
            scene broom_day with fade
            "..."
            call screen gnav
        "Maju 2 jam":

            $ Hour +=2
            "Waktu Maju Dua Jam"
            if Hour >=21:
                $ Hour =21
                jump broom_menu
            else:
                pass
            scene broom_day with fade
            "..."
            call screen gnav
        "Maju 3 jam":



            $ Hour +=3
            "Waktu Maju Tiga Jam"
            if Hour >=21:
                $ Hour =21
                jump broom_menu
            else:
                pass
            scene broom_day with fade
            "..."
            call screen gnav
        "Maju 4 jam":


            $ Hour +=4
            "Waktu Maju Empat Jam"
            if Hour >=21:
                $ Hour =21
                jump broom_menu
            else:
                pass
            scene broom_day with fade
            "..."
            jump broom_menu
        "Maju sampai akhir hari":


            $ Hour =21
            jump broom_menu
        "Kembali":

            jump broom_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
