label slaundry:
    s "Ayo ambil dari kamar saya saat Anda selesai"
    b "Sure"
    scene s_laundry with fade
    b "Wow saya melihat Anda sudah siap"
    s "Yeah"
    scene s_laundry1 with dissolve
    s "Thank youuuu"
    b "{i}(Damn){/i}"
    b "{i} (dimana pakaian dalam sialan itu?) {/i}"
    s "Apa yang kamu tunggu?"
    b "Nothing"
    scene s_laundry2 with dissolve
    show screen srelup
    s "Ok terima kasih, Anda yang terbaik"
    hide screen srelup
    "..."
    $ sdom -= 1
    $ srel += 5
    show screen sdomdw
    b "{i} (apa -apaan, saya melakukan semua ini secara gratis) {/i}"
    hide screen sdomdw
    scene hall_d with fade
    b "{i}(Damn it){/i}"
    call screen gnav

label slaundryalt:
    s "Ayo ambil dari kamar saya saat Anda selesai"
    b "Sure"
    scene s_laundry with fade
    b "Wow saya melihat Anda sudah siap"
    s "Yeah"
    scene s_laundry3 with dissolve
    s "Thank youuuu"
    b "Hmm"
    s "Apa yang kamu tunggu?"
    b "Wow"
    b "Apa celana ini?"
    scene s_laundry2 with dissolve
    s "Apa maksudmu?"
    b "Saya tidak pernah melihatnya"
    b "Saya tidak pernah tahu bahwa Anda memiliki thong"
    s "Tentu saja saya punya"
    b "Hmm"
    scene s_laundry4 with dissolve
    s "Apa yang sedang kamu lakukan?!"
    b "Mencoba mencari tahu kapan dan di mana Anda mengenakan ini"
    scene s_laundry5 with dissolve
    s "Ya ampun ...!"
    scene s_laundry4 with dissolve
    b "Setelah saya mencucinya, saya ingin melihat Anda di dalamnya"
    scene s_laundry2 with dissolve
    s "Saya akan memikirkannya"
    show screen srelup
    s "Sampai jumpa"
    hide screen srelup
    "..."
    $ sdom -= 1
    $ srel += 1
    $ thong = 1
    show screen sdomdw
    "..."
    hide screen sdomdw
    scene hall_d with fade
    b "{i} (...) {/i}"
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc