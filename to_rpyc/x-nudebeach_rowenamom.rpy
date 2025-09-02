label nudebeach_rowenamom:
    scene nbrm with fade
    rm "Tempat yang bagus"
    scene nbrm1 with dissolve
    $ persistent.unlock_30 = True
    b "Yeah"
    scene nbrm2 with vpunch
    b "Aduh!"
    s "Stop it"
    scene nbrm3 with fade
    "Anda tinggal sebentar sebelum kembali ke rumah"
    scene nbrm4 with fade
    rm "Rowena memberi tahu saya bahwa Anda baik dalam memperbaiki gadget"
    b "Ya saya mencoba yang terbaik"
    rm "Di sini ambil nomor saya dan hubungi saya, saya berharap beberapa hal untuk memperbaiki"
    b "Yes sure"
    $ rowena_mom_number = 1
    b "{i} (hmmm i \ 'll hubungi di sini di siang hari besok) {/i}"
    "Itu saja untuk versi ini"
    scene hall_d with fade
    b "{i} (...) {/i}"
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc