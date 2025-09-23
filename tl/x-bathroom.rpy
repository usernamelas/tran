label bathroomone:
    scene black with Dissolve(1)
    if annafirsttimehome == False:
        scene 29-17 shower 1 with Dissolve(1)
        a "{i}...What is going on with everything... My life is in such a complicated place right now..."
        a "{i}...Hopefully, this shower helps to relax a bit..."
        play sound equipsound
        scene black with Dissolve(2)
        play sound shower2
        scene 29-17 shower 2 with Dissolve(1)
        a "{i}...This whole situation, this whole charade... It's almost too much..."
        a "{i}...But something doesn't stop me, I wonder if it's something to do with my condition?..."
        a "{i}...Perhaps my inhibitions are out of my control... I don't know..."
        a "{i}...I wonder how things will turn out after all this mess..."
        scene 29-17 shower 3 with Dissolve(1)
        a "{i}...We managed to get Rebecca back..."
        a "{i}...Unfortunate that someone is dead..."
        a "{i}...The fact that Andrew was shot, makes it even worse..."
        a "{i}...I have to also make sure he comes out of this just fine..."
        a "{i}...That means I have to get that money..."
        scene 29-17 shower 4 with Dissolve(1)
        a "{i}...Ah, it's so complicated... Stupid Andrew, why did you have to do this shit..."
        a "{i}...No... I can't say that... It makes me so angry though..."
        a "{i}...Rebecca is right about a lot of things, I'm starting to think that she is also right about Andrew."
        a "{i}...I still can't wrap my head around the fact that he was shot and is in a coma right now..."
        a "{i}...I truly hope that he recovers...Even if we have had our differences, I still care about him..."
        scene 29-17 shower 5 with Dissolve(1)
        a "{i}...I just mostly hope that Sergey cleaned up the scene and left no clues as to what exactly happened."
        a "{i}...If the cops came sniffing, I'm certain that I would also take the fall..."
        a "{i}...I hope that neither Andrew nor I become loose ends for Fitzgerald or Sergey to 'fix'."
        a "{i}...Still, I should watch my back...for now atleast..."
        play sound undress
        scene 29-17 shower 7 with Dissolve(1)
        a "{i}...That was a very nice shower...It did help a bit..."
        a "{i}...Anyway, there, put on my nightgown...It's very beautiful..."
        a "{i}...I should go to sleep now...I'm so tired...At least my sleep should be solid... So tired..."
        $ annafirsttimehome = True
        scene black with Dissolve(1)
        jump bedroomone
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
