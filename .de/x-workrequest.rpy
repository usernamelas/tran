label workrequest:
    $ Hour += 1
    $ workrequest = 3
    $ worktalk = 1
    scene work_going with fade
    b "Hi there"
    b "Keluar?"
    scene work_going1 with dissolve
    m "Hi [bname]"
    m "Ya pergi untuk wawancara kerja"
    b "Ah keren, semoga berhasil"
    scene black
    "..."
    scene work_going2 with fade
    "..."
    scene black
    "Kembali ke [bname]"
    jump broom_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
