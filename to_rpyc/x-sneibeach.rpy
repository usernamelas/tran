label sneibeach:
    scene neist4 with fade
    s "{i}(Boring){/i}"
    b "Haruskah kita berenang?"
    b "Kami tidak ada di sini untuk meletakkan sepanjang hari"
    scene neist5 with fade
    "..."
    scene neist6 with dissolve
    b "Damn"
    scene neist7 with dissolve
    s "{i} (gadis itu tidak berbicara) {/i}"
    b "Apakah Anda ingin saya mengoleskan minyak"
    s "Ya, akhirnya"
    scene neist8 with dissolve
    b "{i} (sialan pantat ini) {/i}"
    b "Masha, apakah Anda ingin saya mengoleskan minyak untuk Anda?"
    nd "Errr"
    scene neist9 with dissolve
    s "..."
    s "Kita harus pulang [bname]"
    b "Tidak, kami tidak"
    s "Apakah Anda lupa apa yang harus kami lakukan?"
    b "Apa?"
    s "Kami akan pulang"
    s "Bye Masha"
    b "Dia tinggal di gedung yang sama duh!"
    s "Ya mari kita pergi kita semua"
    scene neist10 with fade
    nd "Terima kasih atas waktu yang menyenangkan"
    s "{i} (yeah jalang kanan) {/i}"
    b "Sampai jumpa"
    scene hall_d with fade
    "..."
    call screen gnav

label mashabeach:
    scene neist11 with fade
    nd "Saya pikir [sname] akan datang"
    b "Nah, lebih baik kamu dan aku"
    nd "Biarkan berenang"
    scene neist12 with fade
    b "Apakah Anda ingin saya menerapkan lotion?"
    nd "Biarkan saya menebak"
    nd "Di punggungku"
    b "Yes everywhere"
    scene neist13 with dissolve
    b "Dengarkan ada pantai yang bagus di dekatnya"
    b "Apakah Anda ingin mengunjunginya?"
    nd "Ya, tapi apa tangkapannya"
    b "Anda akan melihat"
    scene neist14 with fade
    nd "Apakah ini pantai telanjang?"
    b "Ya, kita tidak bisa tetap seperti ini"
    nd "Ok"
    scene neist15 with fade
    "..."
    scene neist16 with dissolve
    nd "Huh"
    scene neist17 with dissolve
    b "Apa? Tidak pernah melihat yang seperti ini"
    scene neist18 with dissolve
    nd "No"
    b "Aku juga belum melihat puting seperti milikmu"
    nd "Saya suka bagaimana Anda lurus ke depan [bname]"
    b "Lalu mari kita pergi ke belakang semak -semak"
    nd "Let's go"
    scene neist19 with fade
    "..."
    b "Kemarilah"
    scene neist20 with dissolve
    "..."
    scene neist21 with dissolve
    "..."
    $ persistent.unlock_63 = True
    scene neist22 with dissolve
    nd "Enough [bname]"
    menu:
        "Jangan dengarkan dia, lanjutkan":
            scene neist23 with dissolve
            nd "Please stop"
            scene neist25 with dissolve
            nd "Ah"
            scene neist24 with dissolve
            b "Huh wait"
            scene hall_d with fade
            b "{i} (terima kasih Tuhan tidak ada orang di sini) {/i}"
            call screen gnav
        "Berhenti":

            scene neist20 with dissolve
            nd "Terima kasih"
            scene hall_d with fade
            b "{i} (terima kasih Tuhan tidak ada orang di sini) {/i}"
            call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc