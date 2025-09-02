label rbffightrp:
    scene rcall2 with fade
    a "Hai [bname] masuk"
    rb "Apa yang Anda inginkan darinya?"
    b "Hanya ingin menyapa"
    rb "Saat ini?"
    scene rcall3 with hpunch
    rb ".."
    menu:
        "Melawan*":
            scene rcall4 with hpunch
            a "Aaaah !!!"
            scene rcall5 with hpunch
            a "Berhenti!!"
            scene black
            "..."
            scene rcall6 with fade
            s "Hah!"
            s "Apa yang Terjadi padamu"
            b "Saya bertengkar"
            s "Dengan siapa?"
            b "Err aku tidak mengenalnya, di jalanan"
            scene rcall7 with dissolve
            s "Ya Tuhan, ayo biarkan aku membawamu ke kamarmu"
            menu:
                "Lebih baik jika Anda menelepon [mname]*":
                    jump bruisesjen
                "Oke":
                    jump bruisesnad
        "Jangan":

            scene rcall8 with hpunch
            b "Ahhh"
            a "Berhenti!!!"
            scene rcall9 with dissolve
            a "Biarkan dia pergi! Anda membunuhnya"
            scene rcall10 with fade
            a "..."
            scene rcall11 with dissolve
            $ rowenacall = 3
            a "Ya ampun ..."
            b "Tolong beri saya perban"
            scene rcall12 with fade
            a "Here"
            b "Bisakah Anda membantu saya dengan itu?"
            scene rcall13 with fade
            a "..."
            b "Bisakah Anda memeriksa apakah saya memiliki memar di paha bagian dalam saya?"
            scene rcall14 with dissolve
            a "Huh"
            a "Yes"
            scene rcall15 with dissolve
            a "Hah!"
            b "Apa?"
            menu:
                "Berhenti menatap":
                    a "Ah maaf!"
                    "Rowena! Rowena!"
                    scene rcall17 with dissolve
                    a "{i} itu ibuku memanggil {/i}"
                    b "{i} oh saya pikir saya harus pergi {/i}"
                    "Rowena! Kamu ada di mana?"
                    scene broom_night with fade
                    "..."
                    $ rowena_mom = 1
                    call screen gnav
                "Berhenti menatap atau aku akan bercerita [sname] tentang lipstik*":

                    a "Hmmm"
                    a "Jadi itulah masalahnya!"
                    b "Apa maksudmu?"
                    b "Halo!! Lihatlah memar saya!"
                    b "Anda menyebabkan semua ini, bukan saya"
                    scene rcall12 with dissolve
                    a "Jadi apa yang kamu inginkan sekarang?"
                    b "A kiss"
                    scene rcall18 with dissolve
                    "..."
                    scene rcall19 with dissolve
                    "Halo semuanya"
                    scene rcall20 with dissolve
                    a "Oh hai ibu"
                    b "Hello ma'am"
                    b "Saya baru saja pergi"
                    scene broom_night with fade
                    $ rowena_mom = 1
                    b "{i} (Saya merasa saya telah melihat ibunya di suatu tempat) {/i}"
                    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc