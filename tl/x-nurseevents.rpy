label NurseEventOne:
    show screen HospitalScreen
    hide screen disableClick
    if nursemonologue == 0:
        "The same nurse as yesterday, she is really good looking."
        $ nursemonologue += 1
        jump hospitalScreen
    if nursemonologue == 1:
        "She is really good looking, and seems nice."
        $ nursemonologue += 1
        jump hospitalScreen
    if nursemonologue == 2:
        "I wonder what she's like."
        $ nursemonologue += 1
        jump hospitalScreen
    if nursemonologue == 3:
        "Her skin is really beautiful."
        $ nursemonologue += 1
        jump hospitalScreen
    if nursemonologue == 4:
        "I wonder what kind of product's she uses."
        $ nursemonologue = 0
        jump hospitalScreen
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
