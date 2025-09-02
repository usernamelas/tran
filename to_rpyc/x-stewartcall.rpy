label stewartcall:
    scene stecall with fade
    play sound "sounds/mobilering.wav"
    if persistent.patch_enabled:
        b "{i} (oh it \ 's dad) {/i}"
        pass
    else:
        b "{i} (oh it \ stewart) {/i}"
        pass

    stop sound
    scene nxday5 with fade
    b "Hello"
    scene nxday11 with fade
    d "Hi [bname]"
    d "Apa kabarmu?"
    b "{i} i \ \ 'm good, kamu? {/Saya}"
    s "Bagus, saya sedang berlibur bulan depan"
    s "Saya akan mengunjungi Anda, dan segera kami akan kembali bersama kita semua"
    scene nxday5 with dissolve
    b "{i} (oh fuck, aku tidak bisa membiarkan dia datang dan merusak segalanya) {/i}"
    b "Err"
    scene nxday11 with dissolve
    d "Apakah kamu senang!"
    scene nxday5 with dissolve
    b "Tentu saja saya"
    b "Tapi kamu ... kamu tidak tahu di mana kita tinggal sekarang"
    d "{i} saya lakukan, jangan khawatir {/i}"
    d "{i} Sampai jumpa bulan depan {/i}"
    d "Bye"
    b "Sampai jumpa"
    scene stecall with dissolve
    b "{i} (sialan, saya perlu memikirkan sesuatu) {/i}"
    "..."
    b "{i} (i \ ve get it!) {/i}"
    b "{i} (Saya akan memberi tahu dia bahwa dia punya pacar dan dia pindah) {/i}"
    "Dia tidak datang dalam versi ini"
    scene broom_day with fade
    $ stewartcalled = 1
    "..."
    call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc