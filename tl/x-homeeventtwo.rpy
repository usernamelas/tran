label HomeEventTwo:
    play music tranquility
    play sound walk
    scene black with Dissolve(2)
    "Anna get's home."
    play sound undress
    scene 33-0 morning 0 with Dissolve(1)
    "Get's into bed."
    "She thinks about all the events of the day."
    "It had been a colorful one."
    scene black with Dissolve(2)
    play music lounge
    scene 33-0 morning 1 with Dissolve(1)
    "Anna woke up."
    "Today was the day that she had to close the contract."
    "Ready or not, she had to close it."
    scene 33-0 morning 2 with Dissolve(1)
    a "{i}...What should I wear today..."
    a "{i}...I'm in the mood for something experiemntal..."
    scene 33 red outfit with Dissolve(1)
    a "{i}...This will do nicely..."
    a "{i}...Pretty sexy. Bound to get some turning heads..."
    if dianaGoodRelations == False:
        jump AnnaContractEventOne
    else:
        jump AnnaContractEventOneOne
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
