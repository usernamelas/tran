# Define characters with color codes and tags
define e = Character("Elena", color="#C8FFC8", image="Elena")
define m = Character("Marcus", color="#C8C8FF", image="Marcus")
define n = Character("Narator", color="#ffffff")

# Variables that can affect dialogue
default player_name = "Alex"
default friendship_elena = 50
default friendship_marcus = 30
default has_sword = False
default knows_secret = False
default day = 1

# Image definitions (for sprites)
image elena happy = "elena_happy.png"
image elena angry = "elena_angry.png"
image marcus neutral = "marcus_neutral.png"
image marcus surprised = "marcus_surprised.png"

# The game starts here
label start:
    
    n "Day [1]: {3} petualangan Anda {2} dimulai di kota kecil Riverwood. {4}"
    
    scene bg town_day
    
    show elena happy at left
    show marcus neutral at right
    
    e "Oh! Anda harus menjadi pelancong baru yang dibicarakan semua orang!"
    
    menu:
        "Ya, saya {1} [2]. Senang berkenalan dengan Anda.":
            $ friendship_elena += 5
            e "Senang bertemu dengan Anda, [2]! Saya Elena."
            
        "Siapa yang bertanya?":
            $ friendship_elena -= 10
            show elena angry
            e "Yah, itu tidak terlalu ramah! Saya hanya mencoba menyambut Anda."
    
    m "Jangan pedulikan Elena. Dia selalu terlalu antusias dengan pendatang baru."
    
    if friendship_elena > 45:
        show elena happy
        e "MARCU! Jangan berikan kesan yang salah tentang saya!"
    else:
        e "Setidaknya seseorang di sekitar sini memiliki sopan santun ..."
    
    menu:
        "Kalian berdua tampak dekat. Berapa lama Anda saling kenal?":
            $ friendship_marcus += 5
            m "Sejak kami masih anak -anak. Keluarga Elena pindah ke sini ketika kami berusia tujuh tahun."
            
        "Saya tidak peduli dengan latar belakang Anda. Saya butuh persediaan.":
            $ friendship_elena -= 15
            $ friendship_marcus -= 10
            show elena angry
            show marcus surprised
            e "Wow, banyak sekali?"
            m "Toko umum ada di ujung jalan. Semoga berhasil dengan sikap itu."
    
    # Conditional dialogue based on variables
    if friendship_elena >= 50 and friendship_marcus >= 35:
        e "Anda tahu, [2], Anda tampak baik -baik saja. Mungkin kami bisa menunjukkan kepada Anda?"
        m "Ya, kami dapat memperkenalkan Anda kepada beberapa orang penting di kota."
        
        menu:
            "Saya menghargai itu, terima kasih!":
                $ friendship_elena += 10
                $ friendship_marcus += 10
                e "Besar! Mari kita mulai dengan pandai besi."
                
            "Saya lebih suka menjelajah sendiri.":
                $ friendship_marcus -= 5
                m "Sesuai dengan diri Anda. Jangan menangis jika Anda tersesat."
                
    elif friendship_elena < 30:
        e "Nah, jika Anda memaafkan kami, kami memiliki hal -hal yang harus dilakukan."
        hide elena with dissolve
        hide marcus with dissolve
        n "Elena dan Marcus pergi, jelas tidak terkesan dengan sikap Anda."
        
    else:
        m "Bagaimanapun, kita harus pergi. Sampai jumpa, [2]."
    
    # Another scene with different conditions
    scene bg forest with fade
    
    if has_sword:
        show elena happy at center
        e "Saya melihat Anda memiliki pedang! Itu akan berguna melawan bandit di hutan ini."
    else:
        show elena angry at center
        e "Anda datang ke hutan tanpa senjata? Apakah Anda mencoba membuat diri Anda terbunuh?"
        
        menu:
            "Saya bertarung lebih baik dengan tinju saya.":
                e "Yah ... semoga sukses dengan itu, kurasa."
                
            "Saya berharap Anda akan melindungi saya.":
                if friendship_elena > 60:
                    e "Oh kamu! * terkikik* Baik, aku akan mengawasi punggungmu."
                    $ friendship_elena += 5
                else:
                    e "Ugh, kamu putus asa."
                    $ friendship_elena -= 5
    
    # Secret reveal based on flags
    if knows_secret:
        show elena angry
        e "Tunggu ... Bagaimana Anda tahu tentang artefak kuno? Itu seharusnya menjadi rahasia!"
        
        menu:
            "Marcus memberitahuku.":
                $ friendship_marcus -= 20
                e "Idiot itu! Aku akan membunuhnya!"
                
            "Saya mendengar Anda membicarakannya.":
                e "Anda menguping? Itu pelanggaran kepercayaan yang serius!"
                $ friendship_elena -= 30
                
            "Saya memiliki cara saya.":
                e "Nah ... jangan menyebarkannya, oke?"
                $ friendship_elena += 5
    
    # End of this segment
    n "Saat matahari terbenam, Anda kembali ke kota, hubungan Anda diubah oleh acara hari ini."
    $ day += 1
    
    return