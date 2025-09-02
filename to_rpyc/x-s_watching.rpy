label s_watching:
    scene bporn_s9 with dissolve
    s "{i} (hmm biarkan \ menakutnya dia) {/i}"
    scene bporn_s10 with dissolve
    s "{i} (apa ...!) {/i}"
    s "..."
    if srel >=100:
        s "{i} (ini memalukan) {/i}"
        s "{i} (saya harus pergi) {/i}"
        scene bporn_s11 with fade
        s "Mmmm"
        scene bporn_s12 with dissolve
        s "{i} (tidak bagus [sname]) {/i}"
        scene bporn_s13 with dissolve
        s "{i} (saya harus tidur) {/i}"
        "Itu semua di sini"
        jump newdays
    else:
        "Naikkan poin hubungan Anda menjadi 100"
        jump newdays

label s_watching_m:
    scene bporn_s9 with dissolve
    s "{i} (hmm biarkan \ menakutnya dia) {/i}"
    scene bporn_s10 with dissolve
    s "{i} (apa ...!) {/i}"
    s "..."
    if srel >=100:
        s "{i} (ini memalukan) {/i}"
        s "{i} (saya harus pergi) {/i}"
        scene bporn_s11 with fade
        s "Mmmm"
        scene bporn_s12 with dissolve
        s "{i} (tidak bagus [sname]) {/i}"
        scene bporn_s14 with dissolve
        s "{i} (apa yang salah denganmu [sname]) {/i}"
        s "{i} (saya harus tidur) {/i}"
        "..."
        jump newdays
    else:
        "Naikkan poin hubungan Anda menjadi 100"
        jump newdays
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc