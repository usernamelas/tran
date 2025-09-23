label alfredeventOne:
    play music lounge
    play sound carsound
    scene black with Dissolve(2)
    scene 30-13 hall 1 with Dissolve(1)
    "Anna was returning home from the hospital."
    "She entered the hall and noticed that Alfred was also there."
    "Alfred was returning from his regular appointment with the masseuse."
    "Anna thought she would say hi to him."
    a2 "{i}...Ah... My back and everything else feels much better after the appointment..."
    a2 "{i}...Can't wait to go again, hehe..."
    scene 30-13 hall 2 with Dissolve(1)
    "As Anna was approaching Alfred, she pondered about a lot of things."
    "How her entire day had turned out."
    "What she had to do. The police situation, the hospital situation."
    "She also wondered about her relationship with Alfred."
    a "{i}...I've known Alfred for some time."
    menu:
        "All the dirty thing's we have done...":
            $ AlfredRelationship = True
            $ relationship_func("Alfred Relationship +4, Anna Corruption +3")
            $ AlfredAffection += 4
            $ AnnaCorruption +=3
            jump AlfredNaughtyRelationship
        "He always seemed like a nice neighbour.":
            $ AlfredRelationship = False
            jump AlfredSimpleRelationship

    return
label AlfredNaughtyRelationship:
    scene 30-13 hall 3 with Dissolve(1)
    "Anna approached Alfred and greeted him."
    a "Good evening, Alfred. How are you?"
    a2 "Ah, hello, Anna, dear... I'm very good today..."
    a2 "Had a massage session... Can't complain about the back now."
    a2 "Also, I think you should come to the clothing store at some point."
    a2 "We have a new collection, and I'm pretty sure you might like it."
    a2 "And Thanks to the fact that you participated in the collection catwalk, everything is great again at the shop again."
    a "No problem, Alfred. It was my pleasure. And I will make sure to drop by."
    a "How is Patricia doing, by the way?"
    a2 "Patricia is also quite excited about the collection, and she just talks about it and you non-stop."
    a2 "She can't wait for you to come by again."
    a2 "Thanks about the little 'event' at the pool, That was amazing."
    a "That's great, Alfred."
    a2 "Anna, you seem a bit off today."
    a2 "Are you okay?"
    scene 30-13 hall 4 with Dissolve(1)
    a "Well... Not really, a lot of things have happened in the past couple of days."
    a "I have to come up with a lot of money... changes at work."
    a "And... Well, I don't really wanna talk about it."
    a2 "Oh no... Anna... I'm so sorry."
    a2 "I understand... You don't have to if you don't wish to do it."
    a "Thanks, Alfred, I appreciate it."
    a "But it involves getting a lot of money."
    scene 30-13 hall 5 with Dissolve(1)
    a "I don't know what to do. I have to get money, but all those options are so hard and might take time..."
    a "And that needs to happen soon."
    a "I don't think I will get the money in time for it."
    a "If I want to get it faster, I have to do some, possibly, perverted things."
    a "It's a lot to take in right now."
    a2 "That sounds, terrible Anna..."
    scene 30-13 hall 6 with Dissolve(1)
    a2 "I'm so sorry, Anna. I hope you will succeed at what you are doing, if I could, I would help you. You know that."
    a "Yeah, Alfred, I do."
    a2 "I believe that you will find the money for the surgery."
    a2 "I know you. you are resourceful, Anna."
    a2 "You are great, Anna. You got that?"
    a "Really?"
    a2 "Yes, Anna. One of the greatest girls I know. In all manner of things."
    a "Thanks, Alfred."
    a "Anyway, I will get going right now."
    a "I wanna get into something more comfortable."
    a2 "Ok, I won't hold you."
    $ AlfredEvent = 1
    jump johnEventTwo
    return

label AlfredSimpleRelationship:
    "Anna approached Alfred and greeted him."
    a "Good evening, Alfred. How are you?"
    a2 "Ah, hello, Anna, dear... I'm very good today..."
    a2 "Had a massage session... Can't complain about the back now."
    a2 "Also, I think you should come to the clothing store at some point."
    a2 "We have a new collection, and I'm pretty sure you might like it."
    a2 "And Thanks to the fact that you participated in the collection catwalk, everything is great again at the shop again."
    a "No problem, Alfred. It was my pleasure. And I will make sure to drop by."
    a "How is Patricia doing, by the way?"
    a2 "Patricia is also quite excited about the collection, and she just talks about it and you non-stop."
    a2 "She can't wait for you to come by again."
    a2 "Thanks about the little 'event' at the pool, That was amazing."
    a "That's great, Alfred."
    a2 "Anna, you seem a bit off today."
    a2 "Are you okay?"
    scene 30-13 hall 4 with Dissolve(1)
    a "Well... Not really, a lot of things have happened in the past couple of days."
    a "I have to come up with a lot of money... changes at work."
    a "And... Well, I don't really wanna talk about it."
    a2 "Oh no... Anna... I'm so sorry."
    a2 "I understand... You don't have to if you don't wish to do it."
    a "Thanks, Alfred, I appreciate it."
    a "But it involves getting a lot of money."
    a2 "I'm so sorry, Anna. I hope you will succeed at what you are doing, if I could, I would help you. You know that."
    a "Yeah, Alfred, I do."
    a2 "I believe that you will find the money for the surgery."
    a "Thanks, Alfred."
    a "Anyway, I will get going right now."
    a2 "Ok, I won't hold you."
    $ AlfredEvent = 1
    jump johnEventTwo
    return


label AlfredEvening:
    play sound door2
    scene black with Dissolve(1)
    scene 30-14 home 2 with Dissolve(1)
    "Anna changed into something more comfortable."
    "She did her hair into the usual braid real quick."
    "So the hair wouldn't bother right now."
    "She was rather lost in thought of all the things that happened today and in the past few days."
    "Those were not a few things that had happened."
    a "{i}...I would just love a bottle of wine right now, get drunk, and pass out. That would help a lot... to relax..."
    "Anna suddenly feels rather exhausted."
    a "{i}...Time for a movie... Need to completely turn off everything else."
    a "{i}...And I'm starving... When's the last time I had something to eat?"
    "Anna asked herself."
    scene 30-14 home 2-1 with Dissolve(1)
    "She went straight to the fridge to look for something to eat."
    "There were some random things in the fridge."
    "Some salad, some leftover chicken from John."
    "Some fast food that had been there for a couple of weeks."
    "Anna felt too tired to do any cleaning right now."
    "She just picked the salad."
    a "{i}...I think the salad will be perfect."
    a "{i}...Tasty salad. a bunch of things."
    scene 30-14 home 2-2 with Dissolve(1)
    "Anna took the salad from the fridge. It was on the plate already."
    "As if somebody had put it there for her specifically."
    a "{i}...This will taste perfect after such a long and gruesome day."
    "Anna was just looking a the plate full of lust. Like she would devour the salad within seconds."
    a "{i}...I should just go to the sofa and eat it there."
    "Anna packed everything and went to the sofa in the living room area."
    scene 30-14 home 2-4 with Dissolve(1)
    "Anna sat down on the sofa and prepared to eat the salad."
    "But before anything, she turned on the TV."
    "There was this one certain TV series that she liked to watch."
    "She was watching the episode so intensely that she almost forgot about her food."
    "As soon as she remembered, she dug right into it."
    a "{i}...Nothing better than watching a great series and eating something tasty."
    "Anna quickly devoured the food and left the plate on the little table."
    scene 30-14 home 3 with Dissolve(1)
    "She was watching The Mandalorian."
    "By all accounts a great show and she very much enjoyed it."
    "It brought her thoughts off of real-life problems and hers specifically."
    a "{i}...I wish I could be just a bounty hunter in that universe."
    a "{i}...And take care of that little baby, so cute..."
    "She was watching the episode for a good while."
    scene 30-14 home 4 with Dissolve(1)
    "But then her thoughts shifted back to the entire mess that was her life right now."
    "The doctor issues, Andrews complicated condition, Dilan's request, changes at work, relationships."
    "All of that made her very exhausted."
    a "{i}...I can't seem to shake non of these thoughts for a while..."
    a "{i}...I need to fix them, and I will..."
    "Anna was headstrong, she believed herself, but there was no one here to support her."
    "She felt lonely."
    scene 30-14 home 5 with Dissolve(1)
    "The stress was a lot to bear by herself and no one to really help or listen to her."
    "Anna was thinking about all those issues."
    "She could barely hold herself together."
    "But she had to. She was strong and had pulled through before."
    "This time, however, things are more complicated and bring lots of impact."
    scene 30-14 home 6 with Dissolve(1)
    "Anna lowered her head on her legs and closed her eyes for a moment."
    "Just trying no to cry."
    a "{i}...Why me, though..."
    "Anna thought to herself about all the problems."
    a "{i}...Why do I have to endure this right now."
    a "{i}...Did I do this to myself?"
    a "{i}...Or was it not my fault... I cannot be held responsible for all these things, can I?"
    if AlfredRelationship == True:
        "Suddenly..."
        scene 30-14 home 7
        play sound doorknock
        with vpunch
        "Anna heard a knock on the door."
        "She was surprised and perplexed as to who could be knocking on her door this late in the evening."
        "She was also a bit hesitant to open cause she was unsure about who it might be."
        a "{i}...Could it be Sergey, trying to clean up loose ends?"
        a "{i}...Could it be John? Who else???"
        "Anna was rather confused and a bit scared actually."
        "But she had no choice but to open the door."
        "Anna went to the door."
        scene black with Dissolve(1)
        "Then she opened them."
        scene 30-14 home 8 with Dissolve(1)
        play audio door2
        play audio surprise
        "It turned out to be no else other than Alfred."
        "Anna was surprised as to why Alfred was here."
        a2 "Hello, Anna. Sorry for disturbing you at this hour, but you seemed distressed."
        a2 "Since I've grown older, I've understood the value of peace of mind."
        a2 "Sometimes it requires us to drink a bit, sometimes working on ourselves works."
        a2 "But I thought that a bottle of wine would be just perfect for your evening."
        a "Oh, Alfred, Hey... I don't know... It's rather late."
        a2 "And so we shall drink a bit, ok?"
        a2 "You need to unwind a bit. From the sound of it, you've been under some heavy stress recently."
        scene 30-14 home 9 with Dissolve(1)
        a "That's true."
        a2 "So, what do you say? May I come in?"
        a "Umm... Sure."
        a2 "I promise you, you won't regret this."
        a "I never have before."
        a2 "That's good to hear, Anna."
        a2 "All this is sure to help you, I knew it was the right thing to come and support you."
        a "Thanks, Alfred. I genuinely appreciate this."
        a2 "Think nothing of it, Anna."
        scene 30-14 home 10 with Dissolve(1)
        "Alfred entered Anna's flat. He was thoughtful, truly his best at heart."
        "Anna was, meanwhile, still a bit shocked as to why and how Alfred knew that she needed some support."
        "As if some higher power had brought this upon her."
        "She already felt a bit more at peace."
        a "Anyway, comfortable, I will take the bottle and set us up."
        a2 "Anna, dear... Please, let me. I may be senile, but that doesn't mean I'm not capable of taking care of a bottle myself."
        a "Ok, Alfred. Then come with me to the kitchen."
        scene 30-14 home 11 with Dissolve(1)
        "Anna and Alfred both went to the kitchen to set up for the evening."
        "Anna's mood had turned to the better she got a wine bottle ready to be used."
        "And she had a company that she actually enjoyed."
        "Alfred was really thoughtful this time."
        a "{i}...I can't believe Alfred thought of joining me here, right now."
        a "Anyway, What made you decide to come and join me?"
        a2 "Well, I saw how you felt in the hall."
        a2 "I knew something had to be done. but I wasn't sure if you'd want to be disturbed."
        a2 "Some people deal with problems by themselves, some don't."
        a2 "I thought, that it's better if I try and fail if need be, rather not try at all."
        a2 "If you needed my support and I didn't come, that would be worse than trying."
        a "True, I see your point."
        play music pianosound
        scene 30-14 home 12 with Dissolve(1)
        "Both of them had opened the bottle and gone to the living room."
        "Alfred had poured them both a nice glass."
        "Anna smelled the wine."
        a "What wine is this, Alfred."
        a2 "It's a special one I got from a buddy I met during the vietnam war."
        a2 "After the war, the guy decided to visit me and gifted me a couple of bottles of Château Lafite Rothschild."
        a2 "I've been keeping them for special occasions. And I thought that this is a fitting one."
        a2 "It's a very special wine, for a special person. So I would take offense if you decided not to drink it."
        a "Haha... Alfred. I would never say no to a good wine."
        scene 30-14 home 13 with Dissolve(1)
        a "Or to good company..."
        a2 "I'm glad to hear that, Anna."
        "Both of them were enjoying the good wine and the series."
        a2 "I could never get myself into watching these science-fiction razzle dazzles."
        a "Why?"
        a2 "Well, For one, I can barely keep up with the latest technologies, I used to take interest in comics when I was much younger, but that age has passed."
        a2 "I remember the very first super-hero comics when I was but a lad."
        a2 "I was so awe-inspired by them. Those comics were what kind of motivated me to really participate in the military."
        a2 "I was inspired by the bravery of the heroes that I wanted to be just like them."
        a "That is very impressive, Alfred."
        a2 "Yeah, well... Those days are over now."
        scene 30-14 home 14 with Dissolve(1)
        "Anna was emptying wine glasses like there was no tomorrow."
        a2 "Anyway, I wanted to ask you, what exactly made you cry?"
        a "Well... It's a bit hard to talk about, but my boyfriend got shot."
        with vpunch
        a2 "Oh no..."
        a2 "How are you holding up?"
        a "I'm doing my best. This wine is definitely helping."
        a "I don't really wanna talk about it anyway."
        a "I wanna relax right now."
        a2 "I understand."
        a "This is some good stuff, you know?"
        a2 "All the best for my Anna."
        a "Oh, stop it, Alfred. I'm not your favourite."
        a2 "Yes, Yes, you are."
        scene 30-14 home 15 with Dissolve(1)
        a "Well, Anyway, how are things going with your new clothing collection?"
        "Alfred's thoughts had wondered for a bit because he noticed Anna's pussy hair exposed."
        "He was intrigued, and a bit turned on."
        a2 "{i}...Oh, her pussy, I've always liked it..."
        a2 "{i}...Perhaps now is not the time."
        a2 "Better than expected. I've received a lot of applications from aspiring new models that would want to try it out."
        a2 "But..."
        a2 "I think you are such a better fit for this."
        a "Really?"
        a2 "Yeah, We have all kinds of new outfits, and I really want to see you try them on."
        a2 "They would fit you very well, you have curves that would also really show what the outfits and the story behind them is about."
        a2 "You've proved yourself in the past, and I'm still really thankful about that time when you participated in the catwalk show."
        scene 30-14 home 16 with Dissolve(1)
        a2 "The collection is really popular right now, and that is thanks to you."
        a2 "It really pulled us through, and that alone is worth this bottle. So I don't know how to repay you, honestly."
        a "Don't mention it, Alfred. You are doing enough right now."
        a2 "The pool party was also a very fun experience hehe... I was rather surprise about it."
        a2 "I mean, girls organizing a wet t-shirt party?"
        a2 "I don't know what spells fun better than that."
        a "Oh, You did enjoy it, didn't you."
        a2 "Absolutely, If I could I would want to enjoy it again."
        a "Everything is possible."
        "Anna smiled and looked at Alfred with a little devilish grin."
        a2 "By the way, Patricia talks about you all the time."
        a2 "You should come visit as soon as you can."
        a "Sure, I will drop by, I wanna see the new collection as well."
        scene 30-14 home 16-1 with Dissolve(1)
        "Alfred took the bottle."
        a2 "Let me pour you another one. This one is empty."
        a "Thanks, Alfred. I don't know what I would do without you."
        a2 "Well, for starters, you wouldn't be getting drunk with an old bastard like me. hehe."
        a "Haha, You are funny, Alfred."
        a2 "I've tried to be on many occasions, it usually doesn't work. people don't often understand my jokes."
        a "Well, screw them."
        a2 "Yeah, screw them all, not literally, though."
        a "Oh... Haha..."
        scene 30-14 home 17 with Dissolve(1)
        play sound pourwater
        "Anna was getting really inebriated."
        a2 "How are you enjoying the wine, Anna?"
        a "It's actually one of the best ones I've ever had, to be honest."
        a2 "Well, the French guy knew, what he was giving me."
        a "Anyway..."
        scene 30-14 home 18 with Dissolve(1)
        a "Thanks about everything, Alfred."
        a2 "I'm doing what needed to be done, and what I wanted to do."
        "Things get quiet for a moment."
        a "Alfred, May I just lean closer?"
        a2 "Sure, Anna."
        "She changed her tone and was about to ask Alfred a question."
        "But before that, she gets more comfortable."
        scene 30-14 home 19 with Dissolve(1)
        a "Thank you again for coming, Alfred, I'm pretty tired, but I really appreciate you coming here and supporting me."
        a2 "Don't mention it, Anna."
        a2 "Just an old fool's thoughts."
        a "Don't say that."
        a2 "Ah, don't mind me. I've done a lot of bad in my life, and things I regret, but not this, right here with you."
        "Anna got a little bit lost in time."
        "She was taken back by memories. Back in a time and place when things were different."
        "Memories of her childhood, with her grandpa."
        "Those were the best memories of Anna's childhood."
        "She always felt good around him, and so safe like nothing could harm her."
        a "Alfred."
        a2 "Yes, Anna?"
        a "how come you never talk about your family."
        scene 30-14 home 20 with Dissolve(1)
        "Alfred gets quiet for a moment..."
        a2 "Umm..."
        a2 "Well, My memories of those times aren't the best."
        a2 "I have a daughter, actually."
        a "Really?"
        a "You've never talked about your family before."
        a2 "Because her mother took her with her when she was young."
        a2 "And I've not seen them since."
        a "Oh... I'm sorry, Alfred."
        a2 "I've missed her every day, ever since she was taken."
        a2 "I've tried to find her, but my searches have come up fruitless."
        a2 "I was in a dark place for some time..."
        a2 "Clothes and all this helped me get through it, turned into a passion fueled by a hope that I might seem my daughter again."
        a2 "See her wearing some of the adequate collections, she was a beauty right from the beginning, Nothing more to it. I just loved my daughter very much."
        a "Your so sweet, Alfred. Perhaps you should try and search for them again."
        a2 "Perhaps I will."
        scene 30-14 home 21 with Dissolve(1)
        a "What was she like?"
        a2 "Oh, she was lovely... You would have loved her."
        a2 "She was as smart as a whip right from an early age."
        a2 "She had dark hair, similar to yours."
        a2 "When I saw you in the hall with your hair out today, you very much reminded me of her."
        a "I'm sorry that I brought back painful memories."
        a2 "Don't think about it, It always gives a bit of hope."
        a2 "By the way, I love your new hair, let it flow, let it tell your story."
        a "Well said, Alfred."
        scene 30-14 home 22 with Dissolve(1)
        "Anna had gotten pretty sleepy and was kind of passing out, getting a bit touchy."
        "Alfred was not entirely sure what to do."
        "Anna was saying all kinds of things under her breath."
        a "{i}...What pineapples would you like today, sir..."
        "She was blabbering. looked like she had almost passed out."
        "Alfred, however, was a nice guy."
        "He was wondering what to do, can't really leave her like this."
        a2 "Anna, I think you should go to bed."
        scene 30-14 home 23 with Dissolve(1)
        a2 "Hey, Anna..."
        a "...I will take... two lattes please."
        a2 "Anna!"
        with vpunch
        "Anna wasn't responding."
        a2 "{i}...Ah, well done, Alfred, old fool."
        a2 "{i}...What am I supposed to do with her right now..."
        "Alfred was wondering for a good moment."
        scene 30-14 home 24 with Dissolve(1)
        "He got up from the sofa and looked at Anna."
        a2 "{i}...She literally passed out..."
        a2 "Anna!"
        "There was barely any response."
        "Alfred decided to try and take her to her bed."
        "He was old and senile, but what he lacked in age, he didn't lack in willpower and focus."
        a2 "{i}...Alright, let's see what this back can do after an amazing massage."
        "Alfred prepared to pick Anna up in one fell swoop."
        play sound undress
        scene 30-14 home 25 with Dissolve(1)
        "Alfred picked her up by employing multiple muscles that he hadn't used in a long time."
        a2 "AAH... That's right. it hurts just perfectly."
        "Alfred felt alive, as he once did when he was young."
        "He felt impressed and proud of his doing."
        a2 "Now it's time to take you to bed, Anna."
        a "Take me to the nearest... burger joint, please."
        "Anna was talking incoherent nonsense, and Alfred was just ignoring it."
        a2 "Alright, alright. Take it easy."
        a "I hope I'm not too heavy."
        a2 "Anna, I may be old, but I'm not weak. hehe."
        a "Yes, my hero, Alfred."
        scene 30-14 home 26 with Dissolve(1)
        "Alfred carried her in her room."
        "The room was dimly lit already, so there was little need for adjustments."
        "Alfred was wondering about what he should do in this situation, get her some water, just make her comfortable?"
        "Leave?"
        a2 "Anna... You passed out really fast."
        a "I'm a light... weight..."
        a2 "It looks like it. hehe... No worries."
        a2 "This wine won't leave you hungover in the next morning."
        scene 30-14 home 27 with Dissolve(1)
        "Alfred puts her down in the bed, makes her comfortable."
        "Anna regains some of her senses."
        a "What? Thanks, Alfred."
        a2 "Don't mention it... {b}*pant*{/b}..."
        "Alfred actually got tired. He wasn't young anymore."
        "That did put a bit of strain on his back."
        a2 "My back hurts a bit, but I will be fine."
        a "I'm sorry, Alfred."
        a2 "Don't worry, Anna."
        a2 "Can I get you anything, water, juice?"
        a "I'm fine. Thank you."
        a2 "Okay, Anna... This was a fun night."
        scene 30-14 home 28 with Dissolve(1)
        a2 "In that case, I will be going. I hope you had time to unwind."
        a2 "And forget about all the troubles."
        a "Thank you a lot, Alfred. Again and again."
        "Anna started to wonder about whether she should ask him to stay or not."
        menu:
            "Please stay with me tonight, Alfred.":
                jump alfredstaysthenight
            "Thank you for everything this evening, Alfred.":
                $ AlfredLeaves = True
                jump alfredleaves
    else:

        scene 30-14 home 5 with Dissolve(1)
        "Anna decided to go to bed, atleast she would try to get some good night's sleep."
        "All of the problems would go away if she was asleep, without any worries, perhaps some better dreams this time."
        a "{i}...A bottle of wine wouldn't have hurt, though..."
        a "{i}...Perhaps another time."
        "Anna thought."
        scene black with Dissolve(1)
        play sound undress
        scene 30-14 home 32 with Dissolve(1)
        "Anna got under the blanket and got comfortable."
        a "{i}...Nothing beats my bed... Ah..."
        "Anna was tired from all of today's issues."
        "Both physically and mentaly."
        "She fell asleep quickly."
        scene black with Dissolve(3)
        jump dayThreeMorning
        return
label alfredstaysthenight:
    a "Alfred, can you stay...please..."
    a2 "Are you sure?"
    a2 "If you want I can just sleep on the couch in the living room."
    a "No, I want you to stay here, please."
    a2 "Ok, Anna."
    "Alfred started to take off his clothes and sat down on the bed."
    play sound undress
    scene 30-14 home 29 with Dissolve(1)
    a2 "You sure about this, Anna?"
    a "I don't want to stay alone."
    a "I feel safe in your presence."
    a2 "That's sweet, Anna."
    "Anna was glad that Alfred had decided to stay."
    a "Thank you, Alfred, I appreciate this."
    a2 "Don't mention it, Anna. You need my support, so here I am."
    play sound undress
    scene 30-14 home 30 with Dissolve(1)
    "Anna was getting sleepier by the second."
    a2 "You will be alright, Anna. I believe you."
    "Alfred was trying to be a supportive as he could."
    "He also felt good around her, she was a sweet and caring person."
    "Same thoughts filled Annas mind. Alfred was very amazing today. He had thought about all the details."
    "She was barely awake now."
    "But She didn't have no bad thoughts in her mind. She just felt safe and simply good."
    "Meanwhile, Alfred watched her fall asleep, making sure everything was okay."
    scene 30-14 home 31 with Dissolve(1)
    "Anna turned around and change her position into small spoon."
    "Alfred only knew that he had to get closer."
    "He hugged Anna and she had fallen asleep already, but with a smile. She felt amazing."
    "Best situation she could be in right now, considering the circumstances."
    scene black with Dissolve(3)
    jump dayThreeMorning
    return
label alfredleaves:
    a2 "Alright, Anna. This was very nice, thank you."
    scene 30-14 home 32 with Dissolve(1)
    play sound door2
    "Alfred cleaned up quickly, turned off the lights and the TV and left."
    "Anna got comfortable in the bed."
    "Thought about all the things."
    a "{i}...Nothing beats my bed... Ah..."
    "Anna was tired from all of today's issues."
    "But Alfred had helped her get through the evening. She felt much better because of that."
    "Anna fell asleep quickly..."
    scene black with Dissolve(3)
    jump dayThreeMorning
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
