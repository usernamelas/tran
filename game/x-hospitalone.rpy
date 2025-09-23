label hospitalAB:
    $ renpy.music.play("audio/sounds/Purple Planet Music Rendezvous.mp3", channel = 'music', if_changed = True)
    play sound walk
    scene black with Dissolve(1)
    scene 29-14 hospital corridor anna pink dress new hair with Dissolve(1)
    "Anna came back to the hospital she had had enough time to think things through."
    if doctormanipulations == True:
        "She had to choose which doctor to side with."
        "On one hand, Dr. Eilhart was the better choice because she was honest and a good person."
        "She only wanted justice to be served."
        "And To fix a compromising situation, which she didn't have much control over."
        "But on the other hand, Dr. Schmidt could help Anna understand her condition much better and help solve it."
        menu:
            "Go to Dr. Schmidt for help.":
                jump SchmidtEventTwo
            "Ask Dr. Eilhart for Help.":
                jump hospitalEilhartOne
    else:
        "Anna had already made up her mind to side with Dr. Eilhart."
        "No way she was going to let some asshole do some sexually explicit things to her."
        jump hospitalEilhartOne
label hospitalAC:
    hide screen disableClick
label hospitalScreen:
    $ isActivePlace = 15
    $ renpy.music.play("audio/sounds/Purple Planet Music Rendezvous.mp3", channel = 'music', if_changed = True)
    $ sceneIsActive.ShowScreens()
    show screen disableClick
    show screen characterScreen
    call screen HospitalScreen
    pause
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
