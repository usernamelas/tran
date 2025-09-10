label cherylsawmc:
    ml "Hi Daniel"
    scene cfm1 with dissolve
    dn "Hi"
    c "Kejutan yang menyenangkan"
    c "Apa yang kamu lakukan di sini [bname]"
    b "{i} (sialan!) {/i}"
    b "Errr"
    scene cfm2 with dissolve
    $ persistent.unlock_18 = True
    ml "Anda saling kenal?"
    c "Of course"
    b "Err i \ 'm bekerja di sini"
    c "Apakah Anda tinggal di kota ini?"
    b "{i} (apa yang harus dikatakan padanya, persetan!) {/i}"
    b "Err no"
    c "Hmm ok, dan bagaimana [mname] dan [sname]"
    b "Mereka baik -baik saja, permisi saya harus pergi sekarang"
    ml "Kami juga akan pergi"
    scene cfm with fade
    b "{i} (Saya harus memastikan dia tidak mengikuti saya) {/i}"
    scene hall_d with fade
    b "{i} (hebat! Saya sudah berhasil menyelinap tanpa ada yang mengikuti) {/i}"
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
