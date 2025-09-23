label johnone1:
    play music lounge
    scene black
    scene 30-1 morning 3 with Dissolve(1)
    "Anna exited the room and went to get some coffee, She saw that John had already woken up."
    a "{i}...Oh, John's up. I don't know how I will tell him the bad news."
    a "{i}...I have to tell him that, he needs to know..."
    a "{i}...Poor John..."
    a "{i}... Why is he half naked though?..."
    scene 30-1 morning 4 with Dissolve(1)
    menu:
        "Well, I remember him being completely naked in front of me before.":
            $ johnBeenNaked = True
            $ relationship_func("John Relationship +1, Anna Corruption +3")
            $ JohnRelationship += 1
            $ AnnaCorruption += 3
            jump johnnakedyes
        "I should ask him to put something on. I don't feel comfortable with this":
            jump johnnakedno
    return
label johnnakedno:
    scene 30-1 morning 5 with Dissolve(1)
    a "Good morning John, I hope you are doing well."
    j "Hello Anna, I'm just making coffee, do you want some?"
    a "Thank you, John, That'd be great."
    a "I will have to ask you to put something on next time though, ok?"
    a "I don't feel completely comfortable you walking around like this..."
    j "Oh, sorry Anna, you won't have this problem again."
    jump johntwo
    return
label johnnakedyes:
    a "Good morning John, I hope you are doing well."
    j "Hello Anna, I'm just making coffee, do you want some?"
    a "Thanks John, I'd like that."
    jump johntwo
    return
label johntwo:
    scene 30-1 morning 6 with Dissolve(1)
    a "Hey, I would like to talk to you about Andrew."
    j "Sure, just let me make my morning coffee. It's what I need first before I do anything else."
    a "So, how are you doing?"
    j "Uh, just fine, you know, business as usual. can't complain."
    j "The car has been giving me some trouble lately. Should go to the service and check it out."
    scene 30-1 morning 7 with Dissolve(1)
    j "The damn thing is pretty old now..."
    a "Listen, John, I can't. Something terrible has happened."
    j "Bad enough to disturb my morning coffee?"
    a "I'm sorry but yes..."
    a "Andrew's been shot and is in the hospital right now."
    stop music
    play audio surprise2
    play audio heartbeat
    scene 30-1 morning 8
    with vpunch
    play music tense
    "John is completely shocked and drops his cup, splashing the coffee everywhere..."
    j "..."
    j "I... I.. What?"
    with vpunch
    j "It can't be... WHAT??!!"
    with vpunch
    j "He was just fine not long ago!!!"
    scene 30-1 morning 9 with flash
    j "I CAN'T BELIEVE THIS!! WHAT?!!!"
    j "What happened? You need to tell me what happened!"
    scene 30-1 morning 10 with Dissolve(1)
    menu:
        "Tell him the truth":
            $ relationship_func("John Relationship +1")
            $ JohnRelationship += 1
            jump johntruth
        "Tell him lies":

            jump johnlies
    return
label johntruth:
    a "It's just, oh my god... Things happened so fast."
    a "I was at a hotel with some people, trying to find out Rebecca because she was kidnapped..."
    a "Then some people I was working with broke in looking for those people after I gave them a signal, Andrew was there in the middle of this."
    a "Then one of the bad guys opened fire and..."
    with vpunch
    a "And...shot Andrew {b}*sob*{/b}...then the people I worked with killed the bad guy, but another one got away."
    a "Andrew had to be rushed to ER because he was seriously injured."
    jump johnthree
    return
label johnlies:
    a "Andrew and I decided to go have an adventure in the bad part of town to spice things up a bit."
    a "We had decided a spot so I went there..."
    a "But when I got there, he... {b}*sob*{/b} he... was shot in the chest..."
    with vpunch
    a "I was in shock but I managed to pull myself together enough to call 911 and get him to the hospital..."
    jump johnthree
    return
label johnthree:
    scene 30-1 morning 11 with Dissolve(1)
    a "I can't John, how could it get so bad??? {b}*sob*{/b}"
    j "I don't know Anna, I don't know..."
    j "How did he even get into this situation?"
    a "It's a long story, John. I will tell you some other time."
    j "Alright."
    j "What is his condition right now?!"
    a "The bullet was removed, but the doctor said that further surgery is recommended if we want to avoid serious complications..."
    a "Right now he is an artificially induced coma..."
    j "Oh my god, at least he is alive..."
    scene 30-1 morning 12 with Dissolve(1)
    a "The surgery is really expensive, I will try to find the money for it... I don't know how but I have to do it..."
    j "Take a breather, Anna, it's okay..."
    j "We will figure this out. don't worry okay?"
    j "I'm here. You don't have to worry about it right now..."
    j "I will pay him a visit as soon as I can. I have to make sure he is okay..."
    a "Okay, please do that..."
    play music lounge
    scene 30-1 morning 13 with flash
    j "Damn, I need a drink..."
    j "My hands are literally shaking..."
    j "I don't remember the last time my heart was pounding like this..."
    j "But that's understandable under the circumstances..."
    j "Will you be okay, Anna?"
    a "Yeah, I have to do some stuff that might take my mind off of it for a moment."
    a "Then I have to get back figuring out how to help Andrew..."
    j "Alright, we will figure this out, as I said."
    a "Yeah, I have to head to work anyway."
    $ GlossaryUnlockJohn = True
    $ johnconvo = True
    stop music fadeout 1.0
    play sound carsound
    scene black with Dissolve(2)
    jump officeDianeOne
label johnEventTwo:
    scene black with Dissolve(1)
    play sound door2
    scene 30-14 home 1-1 with Dissolve(1)
    play sound surprise
    "Anna entered the house and saw John and a woman from before."
    "They seemed to not notice her."
    "She was thinking to herself about both of them and that lady."
    a "{i}...Ah, John is here with this girl..."
    if johnBeenNaked == True:
        a "{i}...This skank again... Ugh, where does he find these bitches."
        a "{i}...I just want some peace and quiet after such a day, but then I see this..."
        a "{i}...Just pushing my buttons again and again."
        "Anna was a bit jealous."
        a "{i}...Ugh... I can't believe this."
        a "{i}..The fucking prick, He lives here on our generosity, and the brings her here again?"
        a "{i}...I can't believe this..."
    a "Excuse me."
    scene 30-14 home 1-2 with Dissolve(1)
    play sound surprise
    j "Oh, Hey Anna."
    a "What is the meaning of this?"
    j "Oh, I was just getting ready go out with Janine."
    if johnBeenNaked == True:
        a "Again?"
        j "Are you ok, Anna?"
        j "You seem a bit shaky."
        a "Yeah... YES, I'm fine..."
    j "Right... Anyway. I visited Andrew at the hospital."
    j "He looks pretty terrible, but at least his condition is stable. That's what the doctor's told me."
    scene 30-14 home 1-3 with Dissolve(1)
    a "Sure, sure. But he still needs the surgery to be completely ok."
    j "I asked the doctor's, what's going to happen next and then they told me you are taking care of it."
    a "Right..."
    j "Yeah, I know. How is it going, by the way?"
    a "How is what going?"
    j "Getting the funds for the surgery?"
    a "Oh, so that's how it is?"
    a "Have you thought about this yourself? Like helping me?"
    j "You know I have it rough right now, I have to keep my work afloat, but I will help with what I can, you know that."
    scene 30-14 home 1-2 with Dissolve(1)
    a "Yeah, I don't know at the moment but it might not be as expensive as I thougth at the beginning."
    "Anna was trying to be hopeful."
    if johnBeenNaked == True:
        "But John was so good with Anna in bed before."
        "That's why she couldn't be angry at him anyway."
    j "I'm sorry Anna."
    j "I promise, we will figure this out."
    a "Sure..."
    j "Right... Anyway, I will get going."
    a "Yeah, go, go. I need time to think."

    scene black with Dissolve(1)
    play sound door2
    scene 30-14 home 1 with Dissolve(1)
    if johnBeenNaked == True:
        a "{i}...That bastard, how could he. I like him and stuff but this just starts to ruin things..."
        a "{i}...This bitch, here again, I don't like that... As a matter of fact, I hate it..."
    else:
        a "{i}...It's great that he has found a girl."
    "Anna thought to herself for a bit."
    a "{i}...I should get changed into something more comfortable."
    a "{i}...Then I might feel a bit better, Should put on a movie or something..."
    a "{i}...Think things through about the hospital and the police."
    scene black with Dissolve(1)
    jump AlfredEvening
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
