label ep5:
    centered "{size=+10}{color=FFFFFF}Episode 5{/color}{/size}"
    narrador "In this update, we're introducing hints for those who want to know exactly which path they're choosing."
    narrador "You're not gonna be able to change it later so we recommend you to save here."
    menu:
        "Hints on":
            $ hints_loyal = "{color=02bd02}Loyal +1{/color}"
            $ hints_nts = "{color=#bd02a4}NTS/Sharing +1{/color}"
            $ hints_cheating = "{color=#FF0000}Cheating +1{/color}"
            $ hints_swinging = "{color=#bd02a4}Swinging +1{/color}"
            $ hints_exhibitionism = "{color=#bd02a4}Exhibitionism +1{/color}"
            $ hints_corruption = "{color=#bd02a4}Corruption +1{/color}"
            $ hints_lust = "{color=#bd02a4}Lust +1{/color}"
            $ hints_love = "{color=#bd02a4}Love +1{/color}"
            $ hints_ted = "{color=#bd02a4}MC +1{/color}"
            $ hints_violet = "{color=#bd02a4}FMC +1{/color}"
            $ hints_herold = "{color=#bd02a4}Herold +1{/color}"
            $ hints_melanie = "{color=#bd02a4}Melanie +1{/color}"
            $ hints_mike = "{color=#bd02a4}Mike +1{/color}"
            $ hints_derek = "{color=#bd02a4}Derek +1{/color}"
            $ hints_amelia = "{color=#bd02a4}Amelia +1{/color}"
            $ hints_jeff = "{color=#bd02a4}Jeff +1{/color}"
            $ hints_justin = "{color=#bd02a4}Justin +1{/color}"
            $ hints_trevor = "{color=#bd02a4}Trevor +1{/color}"
            $ hints_lee = "{color=#bd02a4}Lee +1{/color}"
            $ hints_yukio = "{color=#bd02a4}Yukio +1{/color}"
            $ hints_mei = "{color=#bd02a4}Mei +1{/color}"
            $ hints_others = "{color=#bd02a4}Others +1{/color}"
            $ no_major_changes = "No major changes"
            "You've enable hints."
        "Hints off":

            $ hints_loyal = ""
            $ hints_nts = ""
            $ hints_cheating = ""
            $ hints_swinging = ""
            $ hints_exhibitionism = ""
            $ hints_corruption = ""
            $ hints_lust = ""
            $ hints_love = ""
            $ hints_ted = ""
            $ hints_violet = ""
            $ hints_herold = ""
            $ hints_melanie = ""
            $ hints_mike = ""
            $ hints_derek = ""
            $ hints_amelia = ""
            $ hints_jeff = ""
            $ hints_justin = ""
            $ hints_trevor = ""
            $ hints_lee = ""
            $ hints_yukio = ""
            $ hints_mei = ""
            $ hints_others = ""
            $ no_major_changes = "No major changes"
            "You've disable hints."

    scene 1179
    play music neighborhood fadein 1.5 volume 0.2
    mct "Hm... [violet]'s been long for quite some time now."
    mct "I knew she would get lost here."
    mct "Maybe I should go look for her."
    play sound phonevibrating
    scene 1180
    mct "Oh, it's my phone."
    mct "Could be her... let me see."
    scene 1177
    nvl clear
    v_nvl "Babe. Are you there?"
    mc_nvl "I'm here... are you okay? Where are you?"
    v_nvl "I'm in the toilet right now."
    mct "Alright, looks like she found the toilet."
    mct "So why is she taking so long?"
    v_nvl "{image=Send photos 305x350/messagehide.png}"
    mct "Oh, she's sending me a picture..."
    mct "Let's see..."
    mct "Oh, it's a selfie."
    mct "She looks kinda worried tho."
    mct "Wait, is that a..."
    scene 1178
    mct "WHAT IS THAT??"
    scene 1181
    mct "IT'S A DICK!"
    scene blackscreen
    show 1171
    mct "No fucking way."
    mct "It's a gloryhole!"
    mct "I don't think [violet] knows what that is..."
    mct "I'd never thought that a place like this would have a gloryhole in their toilet."
    mct "That's just crazy!"
    scene 1181
    mc_nvl "WTF??"
    v_nvl "I know, right?"
    mc_nvl "How did this happen?"
    v_nvl "Well..."
    scene 1151
    play music publicbathroom volume 0.2
    vs "I took so long to find the toilet that I was not even paying too much attention when I got in."
    vs "I was just trying to pee."
    scene 1155
    vs "Then I heard footsteps... it stopped in the stall right next to mine."
    vs "When I turned my head I saw this hole in the wall... I didn't see it when I walked in."
    scene 1156
    vs "Before I could do something, the man approached the hole and..."
    play sound zipper
    scene 1169
    vs "He stuck his penis in there!"
    vs "I was so shocked..."
    scene 1170
    vs "... I didn't know what to do, so I took the picture to send it to you."
    scene 1172
    nvl clear
    v_nvl "And now I'm here... messaging you while there's an erect penis right by my side."
    v_nvl "I don't know what to do."
    v_nvl "I'm so scared. What does he want?"
    play music neighborhood fadein 1.5 volume 0.2
    scene 1178
    mc_nvl "Holy shit, babe!"
    scene 1180
    mct "Oh man, why do these things keep happening?"
    scene 1183
    mct "And again I have this weird feeling..."
    mct "What should I tell her?"
    menu:
        "Tell her to get out of there fast. [hints_loyal]":
            $ get_out = "1"
            $ calm_her_down = "2"
            scene 1177
            mct "I can't let this happen!"
            mc_nvl "Babe, get out of there fast, just open the door and run over here."
            mc_nvl "I'll be waiting here in the lobby and if he tries to come after you I'll deal with him."
            v_nvl "Okay, I'm getting out of here."
            scene blackscreen
            pause 1.0
            scene 1271
            mc "Honey, are you okay?"
            v "Babe, I..."
            scene 1273
            v "Thank god you're here."
            scene 1272
            v "I was so scared."
            v "I didn't know what to do."
            v "He could be coming after me."
            mc "Calm down baby, I'm here now."
            mc "It's okay, he's probably used to do this, I think he wouldn't get out."
            mc "I'm just shocked they have something like this in this hotel."
            v "Me too..."
            scene 1274
            play sound elevatordoor
            mc "Hey look, they're finally here!"
        "Tell her to calm down. [hints_nts]":


            $ calm_her_down = "1"
            $ get_out = "2"
            scene 1177
            mct "I think this is a great opportunity."
            mct "Meybe she feels the same if I calm her down a bit."
            mc_nvl "Calm down babe, you don't need to be scared..."
            scene 1182
            mc_nvl "You know... I think this could even be fun for us."
            scene 1172
            play music publicbathroom volume 0.2
            v_nvl "What? Fun?"
            mc_nvl "Yeah, I think this is the perfect opportunity for us to experiment."
            v_nvl "Really? Here??"
            mc_nvl "Why not? It's perfect, he can't even see you."
            v_nvl "Are you sure this is safe?"
            mc_nvl "Of course! He just wants you to touch it or something."
            scene 1173
            stranger "What are you wating for? I don't have all day?"
            stranger "Don't be afraid of the size. C'mon girl, hold it in your hand."
            vt "Oh my god! [mcname] is right, he's wants me to do something..."
            scene 1172
            v_nvl "Honey, you're right. He just wants me to grab his penis..."
            mc_nvl "See, I told you! You can do it if you want."
            mc_nvl "I would like to see this, I think it would be hot."
            if go_in_naked == "1":
                mc_nvl "And it's not like it's a big deal..."
                mc_nvl "You've done something similar with Herold in his bathroom..."
            mc_nvl "What do you think? Do you like the idea?"
            v_nvl "Me??"
            mc_nvl "Yeah... How do you feel about it?"
            scene 1184
            vt "I know [mcname] is having this fantasies recently and I mean..."
            vt "I can't lie that I feel something inside me everytime..."
            scene 1185
            vt "I won't deny that this situation is getting me horny, to say the least..."
            vt "And I gotta say, that's not a bad dick."
            scene 1186
            stranger "C'mon girl, why are you taking so long?"
            stranger "Don't play hard to get girl, I know you want to..."
            stranger "Oh I know what you want..."
            stranger "Here, take it."
            scene 1188
            ""
            scene 1189
            play sound slap
            ""
            scene 1190
            vt "WOAH!"
            vt "He's giving me money??"
            scene 1191
            vt "There's gotta be more than a thousand dollars in there!"
            scene 1186
            vt "Who would do such a thing?"
            vt "Is he really willing to spend that much just for me to touch his dick?"
            scene 1187
            vt "He must think I'm some cheap whore."
            vt "Hahaha, [mcname] is right, this could be fun!"
            scene 1192
            v_nvl "Hey babe, you're not gonna believe this."
            mc_nvl "What?"
            v_nvl "He's tossing cash over the stall."
            v_nvl "I guess he is used to pay the girls for this."
            mc_nvl "Wow, I'm surprised they would have something like this in such a fancy hotel."
            v_nvl "Yeah, me too..."
            scene 1172
            v_nvl "So... I'm willing to do this if you're really sure that you don't mind."
            mc_nvl "Really? I told you I don't mind at all."
            mc_nvl "Just make sure to show me everything."
            v_nvl "Oh, okay. I'll try to hold the phone close."
            scene 1174
            vt "Okay... I'm really gonna do this now."
            vt "[mcname] likes this, I would do anything to please him."
            vt "Besides, I'm starting to like it more and more..."
            if go_in_naked == "1":
                scene 614
                vt "First with Herold in the shower..."
                scene 623
                vt "Although I was just cleaning him..."
                vt "Knowing that [mcname] was watching made me feel something inside me I can't explain."
            if let_it_happen == "1":
                scene 1129
                vt "And yesterday at his friend's house..."
                vt "I touched his friend's dick while he was cumming inside me... Lee even came on my tits..."
                vt "We still need to talk about that night..."
            scene 1174
            vt "And now, I'm about to jerk this stranger off."
            vt "Oh my... just saying this makes me wet."
            scene 1175
            vt "I'm gonna do it."
            vt "I wanna feel it in my hand!"
            scene 1176
            stranger "Uhhh... Oh, you have such warm hands. I love it!"
            scene 1182
            play music neighborhood fadein 1.5 volume 0.2
            mct "Fuck! She really did it!"
            scene 1211
            mct "She's holding a stranger's dick."
            if go_in_naked == "1":
                mct "And it's not the same thing as it was with Herold..."
                mct "She's not pretending to help him wash his penis or something like this."
            scene blackscreen
            show 1193
            mct "The look on her face..."
            mct "She can't hide it... she loves it just as much as I do."
            mct "She's so close to it. I wonder what's going on inside her head right now."
            scene 1201
            play music publicbathroom volume 0.2
            stranger "What do you think? You like it don't you?"
            stranger "Don't be afraid. You can start stroking it."
            vt "Okay... I'm not gonna back out now. Here I go."
            scene handjobgloryhole
            play sound handjobwet loop volume 0.6
            ""
            vt "Wow! It feels weird to be doing this to a stranger..."
            vt "The sounds of it... makes me feel so dirty."
            scene 1224
            vt "Makes my pussy so wet..."
            vt "I can feel it dripping."
            scene blackscreen
            show handjobgloryhole2
            mct "This is crazy!"
            mct "I can't believe I'm watching this."
            scene handjobgloryhole3
            play music neighborhood fadein 1.5 volume 0.2
            play sound handjobwet loop volume 0.2
            mct "I've had this fantasie for so long and now that I'm finally seeing it happen... I don't know what to say."
            mct "I didn't think she'd actually do it."
            scene handjobgloryhole
            play music publicbathroom volume 0.2
            play sound handjobwet loop volume 0.6
            stranger "Hey girl, don't get me wrong, you're doing a great job but..."
            stranger "If you really wanna make me cum, you gotta do better than this."
            scene 1194
            stop sound
            vt "Ohh..."
            scene 1225
            vt "He's right, I didn't think this through."
            vt "How far am I willing to go?"
            vt "Or how far would [mcname] want me to go?"
            if go_in_naked == "1":
                scene 649
                vt "I was so scared thinking he'd be mad at me after what happened at Herold's bathroom."
                scene 672
                vt "But no. We kissed and he said he loved me."
            if let_it_happen == "1":
                scene 1126
                vt "When Lee touched my breasts..."
                scene 1129
                vt "And I touched his penis..."
                vt "I thought he was gonna think bad of me or something."
                scene 1148
                vt "But he looks at me like his love for me has grown stronger, and I feel the same way about him."
                vt "Somehow, he seems happy whenever something like this happens."
            scene 1227
            vt "Besides... He's still watching and if I did something he didn't like, he'd just call me."
            scene 1226
            vt "That's it! I've decided."
            vt "I'm gonna do my best to make this guy cum for me."
            scene handjobgloryholefast
            play sound handjob loop volume 5.0
            stranger "Uhhh yeah! Now we're talking."
            stranger "That's much better!"
            scene blackscreen
            show handjobgloryhole2fast
            mct "Holy shit! She stroking it harder now."
            mct "When she stopped for a second I thought she was gonna back out..."
            mct "But now it looks she's doing it with more desire."
            scene handjobgloryhole3fast
            play music neighborhood fadein 1.5 volume 0.2
            play sound handjob loop volume 2.0
            mct "I'm loving it!"
            scene handjobgloryhole4fast
            mct "If she keeps this up..."
            play audio ahemmale volume 0.5
            scene handjobgloryhole5fast
            guard "Ahem..."
            mct "Huh? Why is he looking at me like..."
            scene handjobgloryhole4fast
            pause 1.0
            scene handjobgloryhole5fast
            mct "..."
            mct "Oh fuck!"
            mct "He can hear the sounds..."
            mct "He must think I'm watching porn."
            mct "He's not entirely wrong tho..."
            mc "Ahmm, sorry... I'll keep it down."
            guard "Good!"
            stop sound fadeout 3.0
            scene handjobgloryhole4fast
            mct "I better turn the volume off."
            mct "Fuck! I got so distracted watching [violet] that I forgot where I was..."
            mct "I should tell [violet] to hurry up."
            play music publicbathroom volume 0.2
            scene handjobgloryholefast
            play sound handjob loop volume 5.0
            vt "..."
            vt "This guys is taking so long to cum."
            vt "I'm doing my best here, my arm is getting tired."
            play sound message
            scene 1202
            pause 0.2
            scene 1229
            vt "Huh?"
            vt "He sent me another message."
            mc_nvl "Honey, you gotta hurry up."
            mc_nvl "Lee and Yukio might be coming back any minute now."
            v_nvl "Oh, you want me to stop?"
            scene 1202
            vt "He's not typing anything..."
            v_nvl "Babe?"
            mc_nvl "No."
            mc_nvl "I don't want you to stop."
            mc_nvl "It's just... maybe you could do something more..."
            scene 1203
            v_nvl "What?"
            v_nvl "Are you serious?"
            v_nvl "Are you really asking me to do what I think you are?"
            mc_nvl "Is it too much?"
            scene 1202
            v_nvl "I don't know..."
            mc_nvl "I'm sure he's not gonna last long if you do it..."
            mc_nvl "And to be honest, I really wanna see it."
            scene 1201
            vt "I don't know what's happening, but this is turning me on more and more."
            vt "Just thinking about putting it in my mouth..."
            vt "And [mcname] says he wanna see it too."
            scene 1202
            v_nvl "Okay, I'll do it."
            v_nvl "I'll turn video chat back on."
            mc_nvl "Sure!"
            scene 1231
            vt "His face doesn't lie. He really want this."
            scene 1201
            vt "And I want it too."
            scene 1204
            vt "I wanna suck a stranger's dick."
            scene 1205
            vt "And I'm gonna enjoy every second of it."
            scene 1206
            stranger "W-what?"
            stranger "Is that your tongue on my cock?"
            scene 1207
            stranger "OH MY GOD!!"
            stranger "OH FUCK!!!"
            stranger "I CAN'T HOLD IT!"
            scene 1208
            play sound guycum
            stranger "THAT'S IT!! I'M CUMMING!!!"
            v "WHAT?"
            play audio girlsigh
            scene 1209
            play sound guycum2
            play audio cum1
            v "AHHH."
            play audio cum1
            scene 1210
            ""
            play audio cumbody
            scene 1199
            ""
            vt "Oh my god!"
            vt "That was so close."
            scene 1223
            vt "I can't believe he came so much just by me touching his tip with my tongue."
            vt "If I didn't dodge it in time my mouth would be full with his cum right now."
            vt "He still has some on his penis, maybe I..."
            scene 1232
            stranger "That was so good!"
            stranger "I'll be sure to come back for more soon!"
            scene 1233
            vt "Oh... he's leaving."
            scene 1234
            pause 0.6
            scene 1235
            pause 0.6
            scene 1236
            pause 1.0
            scene 1237
            vt "Oh my god!"
            vt "I feel sorry for whoever has to clean this up later."
            play sound dooropen
            scene 1238
            stranger "Bye now! I hope you liked it as much as I did, haha."
            scene 1239
            ""
            scene 1240
            vt "Hum...[mcname] was right, this was actually fun."
            scene 1241
            vt "Speaking of which..."
            vt "He's seems to be loving this."
            vt "Maybe I should tease him a little more."
            scene 1242
            v "Tell me babe, did you like that?"
            mc "Are you kidding me? That was great!"
            mc "I loved it! I think we should try to do things like this more often."
            v "Oh, really? Hold on."
            scene 1243
            v "Maybe I'm not quite done here yet."
            mc "Huh? What are you doing, babe?"
            v "Oh, You'll see..."
            scene blackscreen
            show 1244
            v "What do you say we play a little game?"
            v "A game with imagination..."
            mc "Imagination? What do you mean?"
            show 1245
            v "I mean... Imagine if I bend over like this..."
            v "Do you get any ideas?"
            mc "I mean, I..."
            show 1246
            v "Or maybe like this."
            v "And then I could..."
            show 1247
            v "Turn around a little bit."
            v "What do you think could happen?"
            mc "Holy shit, babe!"
            scene 1249
            mct "She's teasing me so much."
            mct "Her pussy is just a few inches from touching that guy's cum."
            mct "And she knows it!"
            mct "Thank god he's out of there!"
            scene blackscreen
            show 1247
            play sound dooropen2 volume 0.5
            mct "Wait..."
            scene 1254
            mct "What's that noise?"
            scene 1255
            mct "Did someone just come in?"
            play sound doorclose volume 0.1
            scene 1256
            ""
            scene 1250
            strangert "Oh, so it's true, they really have one of those in here..."
            scene 1251
            strangert "I know I'm gonna have a lot of fun here."
            strangert "And would you look at that..."
            scene 1248
            strangert "Looks like I won't have to wait."
            scene blackscreen
            show 1247
            mc "Babe wait, I think I heard someone coming in."
            v "Haha, nice try! But now I'm gonna do the teasing!"
            v "Can't you see I'm waiting for a dick to enter me?"
            scene 1177
            mct "Shit, she thinks I'm playing."
            scene blackscreen
            show 1261
            play sound heartbeatslow volume 0.5 loop
            mct "What do I do now??"
            mct "I can see the shoes!"
            v "My pussy is begging for it!"
            v "I need a dick inside it right now, any dick!"
            scene 1178
            mct "Shit, it's definitely another dude!"
            scene blackscreen
            show 1261
            mct "I need to say something."
            mct "Otherwise he's gonna..."
            scene 1257
            strangert "Oh, I'm definitely not gonna make her wait!"
            play audio dress volume 0.2
            scene 1258
            ""
            scene 1268
            stop audio
            mct "He's gonna..."
            scene 1258
            pause 0.8
            scene 1259
            mct "He's gonna put his dick in..."
            scene 1252
            ""
            scene blackscreen
            show 1260
            mct "And [violet] doesn't know what's about to happen."
            v "Why are you so quiet all of a sudden, babe?"
            v "Cat got your tongue?"
            v "Don't you wanna see me getting fucked right here?"
            scene 1268
            mct "Fuck, I don't have time!"
            mct "Why can't I move or say anything?"
            scene 1269
            mct "I can't let this happen!"
            mct "Come on [mcname]! Do something!"
            mct "What is happening to me??"
            scene 1266
            mct "Do something... I need to do something."
            scene 1265
            mct "DO SOMETHING!!"
            scene 1253
            stop sound
            v "Alright, that's it."
            scene blackscreen
            show 1262
            mct "What?"
            mct "Did he..."
            show 1263
            v "I think I've teased you enough."
            v "The show is over, I'm coming back to you now."
            scene 1243
            mc "O-ok honey..."
            scene 1267
            v "Hahaha, it's so funny to see you like this."
            v "I love teasing you."
            mc "Hehe, I love it too, babe."
            mct "Oh god, that was close..."
            play sound doorclose
            scene 1270
            ""
            stranger "..."
            stranger "Hm... Hello?"
            scene 1264
            stranger "Are you there?"
            stranger "My dick is ready for you..."
            stranger "Hello??"
            scene blackscreen
            pause 1.0
            play music neighborhood fadein 1.5 volume 0.2
            scene 1275
            v "Hey, I found the way back to you!"
            v "You were right, this place is huge."
            scene 1276
            mc "Are you okay?"
            scene 1277
            v "Yes babe, of course. Why?"
            scene 1276
            mct "Oh, it seems she doesn't realize what almost happened there..."
            scene 1278
            v "What's that face? You look like you've seen a ghost."
            scene 1279
            mc "Oh no, nothing."
            mc "I'm still processing what happened there."
            mc "And all that teasing you did..."
            scene 1278
            play sound girlsmirk
            v "Haha, sorry about that."
            v "But you enjoyed it, right?"
            scene 1279
            mc "Yeah, I mean... It was kinda my idea after all."
            mc "What about you? Did you like it?"
            scene 1280
            v "Well, It did caught me a bit of guard, but I can't deny, I liked it..."
            v "It was pretty fun, but we still need to communicate this things better."
            scene 1281
            v "Like, I know you have this fantasies but... what would be the limit for you?"
            v "How far are you willing to go?"
            scene 1282
            mc "I... I'm not sure yet..."
            mc "I just know that I don't want you to do anything you're not comfortable with just to please me."
            scene 1281
            v "Don't worry about that, I'm not."
            v "I think the most important thing is that we communicate our feelings and trust each other."
            scene 1279
            mc "Right!"
            mc "And if I take it too far don't be afraid to say something."
            v "Sure!"
            scene 1283
            play sound elevatordoor
            mc "Hey look, they're finally here!"


    scene 1284
    yukio "Hey guys! Nice to meet you."
    scene 1287
    v "Oh hello! You must be Yukio, right?"
    scene 1286
    yukio "Yep! That's me."
    yukio "And you must be [violet] and [mcname]."
    scene 1285
    mct "Oh god, it's her!"
    scene 1286
    mct "Now looking at her..."
    mct "I can't stop thinking about that picture."
    scene blackscreen
    show 1289
    mct "I saw her tits..."
    mct "And Lee told me it was her idea to make him send it to me."
    scene 1290
    yukio "So, tell me [mcname], did you like it?"
    mct "What? Is she really asking me this?"
    mct "I can't... I'm not gonna..."
    scene 1288
    v "Babe?"
    v "Babe? Are you okay? She's asking you a question?"
    scene 1291
    mc "Huh? What?"
    v "What happened? Why are you so quiet?"
    mc "Oh, sorry. I got distracted, I was just thinking about something else..."
    scene 1290
    yukio "I was just asking if you like it."
    yukio "The hotel you know..."
    scene 1292
    mct "She's totally teasing me, she knows exactly what I was thinking..."
    mct "Well... two can play that game."
    scene 1293
    mc "Oh, I think it's a fine. From what I could see."
    mc "I could only see the front, you know."
    scene 1290
    yukio "Really?"
    yukio "Maybe I could show you the rest sometime."
    scene 1294
    lee "Why would you do that?"
    lee "We're about to leave..."
    yukio "You're right, we can go now."
    yukio "The hotel staff will take the rest of my things later."
    scene 1295
    v "Alright! Let's go."
    v "You guys are gonna love our home."
    yukio "Haha, I'm sure we will."
    scene blackscreen
    pause 1.5
    scene 1296
    v "We're here!"
    v "This is our house."
    v "As you can see, the neighborhood is pretty chill."
    scene 1297
    lee "Holy shit, dude! That must've cost you a fortune."
    yukio "It's a nice house indeed."
    v "Thanks! We just arrived, I haven't even seen all the rooms myself, can you believe that? Haha."
    yukio "Oh, I believe, haha."
    play sound dooropen1 volume 0.5
    scene 1298
    lee "Wow! You even have a swimming pool."
    lee "I need to dive in!"
    yukio "Calm down, you're acting like a little boy."
    scene 1299
    mc "That's the Lee I grew up with."
    v "Don't worry, you're gonna have a lot of time for that later."
    mc "Yeah, let me show you your room first."
    v "Go ahead honey, I'm gonna show yukio the rest of the house."
    mc "Alright. Lee follow me."
    scene 1300
    mc "So this is the guest room, first door left, you can't miss it."
    mc "You're gonna be staying here."
    lee "Cool."
    play sound dooropen
    scene 1301
    mc "And here it is..."
    mc "It has a bed... a wardrobe, and I guess that's it."
    scene 1302
    lee "That's all I need, haha."
    lee "Just one question. How thick are the walls?"
    mc "What?"
    mc "Ahhh... shut up dude!"
    lee "What? I'm serious man, Yukio is a sex machine, I'm telling you."
    lee "And I make her scream very loud if you know what I mean."
    scene 1303
    mc "Yeah, I know what you mean, you're annoying as fuck and she yells at you to shut up."
    lee "Haha, kinda like that."
    mc "Haha, it's gonna be nice having you around man."
    lee "I feel the same, bro."
    scene blackscreen
    pause 1.0
    scene 1305
    v "And we're back in the living room."
    v "What do you think?"
    yukio "I love it! You have a beautiful house."
    yukio "Thanks again for letting us stay here."
    v "Not a problem, really."
    scene 1307
    yukio "I don't know if Lee told you about my dad... he's rich."
    yukio "But he doesn't like that I moved away from Japan."
    yukio "He's very traditional. He still helps me with some money but he won't help me buy a house here, no matter what."
    yukio "So Lee and me are gonna save money and move as soon as we can."
    v "Oh, don't worry about that, you guys can stay as long as you want."
    scene 1305
    v "Besides, I think it's gonna be nice having another woman around here, you know."
    yukio "Yeah, I agree!"
    scene 1306
    yukio "Now tell me, have you done it in all the furniture already?"
    v "What?"
    v "No... we're not like that..."
    yukio "Aw, c'mon girl don't give me that, you guys are both young and hot, I'm sure you can't stay away from each other."
    scene 1308
    v "I mean, we're doing great, I just don't talk about my sex life like this..."
    yukio "Why not? I'm very open about my sexual life, I don't see a problem with that."
    yukio "I love sex and I'm not ashamed about it."
    yukio "You'll see, we'll spend a lot of time together now, I'll help you open up."
    v "Hm... okay."
    vt "I wonder what she means by that?"
    play sound phonering
    vt "Huh?"
    scene 1309
    vt "Oh good, saved by the phone call..."
    v "Oh sorry, I have to get this, it's my mom."
    yukio "No problem."
    stop sound
    scene blackscreen
    pause 1.0
    scene 1303
    v "[mcname]! Could you come here, please?"
    scene 1304
    mc "Huh?"
    mc "Okay baby, I'm coming."
    scene 1310
    mc "I'm here. What happened?"
    v "I don't really know yet."
    v "My mom just called, asking if we can go there right now..."
    mc "Why, is she okay?"
    v "She didn't say much, just said she wanted to talk to you and me."
    scene 1311
    mc "Okay, but what about Lee and Yukio, they just got here."
    mc "It sucks to leave them alone while we go out."
    lee "Hey, it's okay man, don't worry about us, we're gonna be fine here."
    lee "Just go see what's going on."
    scene 1312
    mc "Really?"
    lee "Yeah dude, it's okay. We'll use this time to get familiar with the house."
    lee "We can do something together when you get back."
    mc "Well... okay."
    mc "We'll be back soon."
    scene 1313
    mc "Alright, tell her we're coming."
    mc "I'm sure it's nothing serious."
    scene 1314
    v "You must be right."
    v "I'm gonna call her and tell that we're leaving."
    v "But first let me change these clothes, I'm wearing this since yesterday."
    scene 1313
    mc "Yeah, me too... it's starting to smell like Lee's bedroom."
    scene 1312
    lee "You better get used to it, I'm about to leave my scent all over here."
    mc "..."
    scene 1313
    mc "Babe, let's stop by a market on the way back and buy some scented candles."
    play audio girlsmirk2
    play sound girlsmirk3
    girls "Hahahaha."
    scene blackscreen
    pause 1.5
    play sound doorbell
    amelia "I'm coming..."
    play audio dooropen
    scene 1315
    amelia "Oh hello guys! I'm so glad you're here."
    amelia "Sorry to bother, you guys probably have something more important to do than come here, so thank you."
    scene 1316
    mc "It's nothing. Really."
    v "Yeah mom, you can call us whenever you need something."
    v "Now tell us... what happened?"
    v "You sounded sad on the phone."
    v "Does Jeff have something to do with this?"
    scene 1317
    amelia "Yeah, he kinda does."
    amelia "But don't worry, I'll explain everything."
    scene 1318
    amelia "Come on in first, I'll tell you everything."
    amelia "Let's just try to keep it down, Jeff is still sleeping."
    v "Okay."
    scene 1319
    amelia "[mcname], can you close the door for me?"
    mc "Y-yes of course."
    mct "Man, the way she's dressed... I gotta take a better look."
    menu:
        "Don't look.":
            $ dont_look = "1"
            $ check_her_out = "2"
            scene 1321
            mct "No, what am I thinking..."
            mct "She's [violet]'s mom, I can't think about her like this..."
            mct "I need to be careful around her..."
        "Check her out. [hints_amelia]":

            $ check_her_out = "1"
            $ dont_look = "2"
            scene 1320
            mct "Oh god, she's so hot."
            scene 1322
            pause 0.5
            scene 1322 at slow_up
            pause 2.0
            mct "I know I shoudn't be looking but..."
            mct "She's so sexy."
            scene 1324
            mct "Oh shit! She caught me looking."
            mct "If she tells [violet] I'm fucked..."
            scene 1323
            mct "Wait, what?"
            mct "She's... smiling at me."
            mct "She's such a tease... "
            mct "I need to be careful around her."

    scene blackscreen
    play sound doorclose volume 0.5
    pause 1.0
    scene 1326
    v "Alright mom, now can you now tell us what's going on?"
    v "I'm starting to get worried about you."
    scene 1325
    amelia "You don't need to worry about me, it's nothing serious."
    amelia "I mean, it's serious... but it's..."
    amelia "Okay, I'm just gonna say it..."
    scene 1330
    amelia "Jeff's been cheating on me."
    scene 1331
    v "What? Really?"
    v "I thought you guys were good, you said he was a perfect husband."
    amelia "Turns out I was lying to you, I'm sorry."
    amelia "You guys are starting a new life here, I didn't want you to worry about me."
    v "You should've told us."
    v "But wait, are you sure about that?"
    scene 1330
    amelia "Yes, I'm sure..."
    amelia "And it's not with just one girl."
    amelia "I saw his phone, he texts a lot of different girls."
    amelia "They send him nude pictures and he does the same..."
    amelia "There was even a video he recorded of one of his dates with this girl."
    amelia "I'm so dumb, I should've realized..."
    amelia "He doesn't even touch me anymore."
    scene 1327
    amelia "Right after we got married."
    mct "Man, Jeff's gotta be kidding me."
    mct "how can he do this to Amelia?"
    scene 1328
    mct "I mean, just look at her..."
    scene 1329
    mct "She has such a fine body."
    mct "A lot of young girls would kill to look like this."
    mct "And a lot of men would do it just to be with her."
    scene 1328
    mct "I just don't get it."
    scene 1326
    v "So, what are you gonna do now?"
    scene 1325
    amelia "I think I'm gonna divorce him..."
    scene 1326
    v "Wow, really?"
    amelia "I want to, but I'm not sure..."
    v "Why?"
    v "You can count on us, mom. We'll help you get through this."
    scene 1325
    amelia "That's so sweet, honey."
    amelia "Thanks, really."
    amelia "I just don't want you guys to worry too much about me."
    amelia "I'm sure you and [mcname] have your own problems."
    scene 1326
    v "That's nonsense, mom."
    v "We're happy to help you with anything, right [mcname]?"
    scene 1332
    mc "Yeah, of course, Amelia."
    mc "One of the reasons we moved to this neighborhood was so you could be a part of our lives again."
    amelia "That makes me so happy, you have no idea."
    amelia "That's why I need to make sure Jeff leaves the house."
    amelia "I wanna be here next to you guys."
    scene 1333
    v "I mean, you could just stay with us at our house until you get the divorce done."
    v "We'd love to have you, mom."
    v "Right, [mcname]?"
    scene 1332
    mc "Yes, for sure..."
    mc "I just don't know if we'll have the space... my friend is gonna stay there for a while now."
    amelia "No, honey. As much as I'd love to stay with you two, I know how important it is to have your privacy."
    scene 1334
    amelia "You guys have just moved in and I know how it is."
    amelia "You don't wanna have your mother around for that, haha."
    scene 1335
    v "Come on, mom. It's not like that..."
    v "But if you're sure about this, I won't insist."
    scene 1332
    mc "So, Amelia, do you have a lawyer yet?"
    scene 1333
    v "I'm sorry to interrupt, but I really need to go to the bathroom."
    vt "With everything that happened at the hotel bathroom, I couldn't pee..."
    amelia "Oh, it's okay honey. It's the second door on the left."
    scene 1336
    v "Okay, I'll be right back."
    amelia "Take your time."
    scene 1337
    vt "Second door on the left..."
    scene 1338
    vt "Must be this one."
    scene blackscreen
    play sound dooropen
    pause 1.5
    play sound doorclose
    scene 1339
    ""
    scene 1340
    vt "..."
    vt "Well, that was something..."
    vt "I think my mom is doing the right thing leaving Jeff."
    vt "I've always been on the back foot with their relationship."
    if dont_let_him_pee == "1":
        scene 212
        vt "And after recent events, I guess that's good for everyone if she leaves him."
    if let_him_pee == "1":
        scene 305
        vt "And after recent events, I guess that's good for everyone if she leaves him."
    if let_him_finish == "1":
        scene 360
        vt "I can't believe I let him jerk off to me and cum on my leg."
    if dont_let_him_finish == "1":
        scene 337
        vt "I can't believe I let him jerk off looking at me."
    scene 1341
    vt "Good thing this is all in the past now..."
    scene 1342
    vt "[mcname] is gonna help her find a place soon and..."
    scene 1343
    play sound girlsigh
    v "Huh?"
    scene 1344
    v "JEFF??"
    scene 1345
    ""
    scene 1346
    ""
    play sound fall1
    scene 1347
    ""
    scene blackscreen
    $ renpy.pause(1.0, hard=True)
    narrador "Meanwhile..."
    scene 1409
    amelia "And from that moment I knew he didn't care about me at all..."
    amelia "You know how I feel, right?"
    mc "Yeah, sure..."
    mct "Man... I hate when [violet] leaves me alone with her mom in this situations."
    mct "She just starts talking about her personal life and I don't know what to say to make her feel better."
    mct "I guess she just wants someone who can listen to her."
    scene 1329
    mct "I just can't concentrate when she's wearing this shorts right by my side."
    if violet_shower == "1":
        mct "When I touched her butt, I could feel what an amazing ass she have."
    mct "I really wanna see more... maybe if a bend myself just a little..."
    scene 1356
    mct "Wow! What is that?!"
    mct "She's not wearing panties!"
    mct "I can see her pussy!"
    play sound ahem
    pause 0.5
    scene 1410
    if ted_shower == "1":
        ameliat "The nerve of this guy, he's looking at my pussy, haha."
        ameliat "Well, I guess that makes us even after I've seen his big dick."
    amelia "Tell me [mcname]. Do you like what you see?"
    scene 1411
    mct "Oh shit! She caught me..."
    mc "What? N-no Amelia... I wasn't looking at your pussy, I swear..."
    scene 1410
    amelia "Oh, really?"
    amelia "I didn't say you were looking at my pussy."
    amelia "I asked if you liked what you saw."
    amelia "But now I know, just look at you, haha."
    scene 1412
    mc "What?"
    mct "Oh fuck! I'm hard again."
    if calm_her_down == "1":
        mct "I'm still horny after what happened at the hotel and..."
    mct "Looking at Amelia's pussy already made me hard..."
    if violet_shower == "1":
        mct "This is the second time she sees me with a boner..."
    scene 1413
    mc "I-I'm so sorry, Amelia."
    mc "I didn't want to offend you."
    mc "It's just..."
    scene 1410
    amelia "Offend me?"
    amelia "Oh trust me, you didn't."
    amelia "I feel flattered that I can still cause such a reaction in a young man like you."
    amelia "Besides... If you wanted to look."
    play sound undress2
    scene 1414
    amelia "You just needed to ask..."
    mc "Woah!"
    scene 1415
    mct "WTF!"
    mct "No way this is happening!"
    scene 1416
    mc "Amelia! W-what are you doing??"
    mc "Are you crazy?"
    scene 1414
    amelia "What? You wanted to look, right?"
    amelia "I'm just giving you a better view."
    scene 1417
    mc "No, you're definitely crazy..."
    mc "Why are you doing this?"
    mc "What would happen if [violet] came back right now?"
    mc "I don't think I could explain this..."
    scene 1418
    amelia "Come on [mcname]. You think too much."
    amelia "Don't tell me you've never imagined me like this?"
    scene 1417
    mc "What? N-no, of course not..."
    if violet_shower == "1":
        scene 1418
        amelia "Really? Cuz I remember feeling your dick getting hard when you grabbed my ass before."
        scene 1417
        mc "T-that was an accident..."
    scene 1419
    amelia "What? So you're saying you don't find me sexy anymore?"
    amelia "Am I this old?"
    scene 1420
    mc "No... it's not like this... you're not old, Amelia."
    mc "You look pretty good, don't get me wrong, but..."
    mc "We can't be doing this... I don't think [violet] would like this, you know."
    scene 1419
    amelia "Well, you can't know that."
    amelia "She said you'd help me get through this, and lately..."
    amelia "I've been feeling so lonely..."
    scene 1421
    amelia "Let me take a look at the reaction I caused right there."
    amelia "I know you want this too."
    amelia "There's nothing wrong with that."
    amelia "Don't you want to help me feel better?"
    mc "I... I don't know..."
    scene 1422
    mct "Hm?"
    mct "What is that?"
    scene 1423
    mct "She's been drinking..."
    mct "She's trying to mask her feelings in front of [violet] but it's clear to me..."
    mct "She's mad with Jeff, a lot... maybe she wants to take revenge on him doing this with me now."
    mct "I don't know if I should do this."
    menu:
        "Interrupt her. [hints_loyal]":
            $ interrupt_her = "1"
            $ let_her_keep_going = "2"
            mct "I can't let her do this."
            scene 1424
            mc "Amelia, stop."
            mc "I'm sorry if I mislead you, that was not my intention, but this is not right."
            mc "I can't do this to [violet] and to {b}you{/b} too."
            mc "I think you drank too much and you're not thinking straight..."
            scene 1425
            amelia "..."
            amelia "Oh god. You're right..."
            amelia "What am I doing?"
            amelia "I'm sorry... you must think I'm a slut for throwing myself at you."
            scene 1424
            mc "No, you're not a slut. Again, it's my fault..."
            mc "You're vulnerable right now, this things can happen..."
            mc "But it's okay, you've done nothing wrong."
            scene 1425
            amelia "Are you sure?"
            mc "Of course, don't worry about it."
            amelia "My daughter is so lucky to have such an amazing husband like you, [mcname]."
            mc "Thanks. Now, put your shorts back on and let's pretend this never happened, okay?"
            amelia "Okay..."
        "Let her keep going. [hints_amelia]":


            $ let_her_keep_going = "1"
            $ interrupt_her = "2"
            scene 1422
            mct "Fuck, I shouldn't be doing this, but It's too hard for me to resist..."
            play sound pants
            amelia "Alright, Let's see what we're working with."
            mct "I need to stop her, but..."
            play sound undress
            scene 1427
            amelia "Oh, wow!"
            amelia "Already that hard for me, huh?"
            scene 1426
            amelia "[violet] is one lucky lady..."
            scene 1428
            mct "OH FUCK!"
            amelia "That's a nice cock you have!"
            amelia "I think you're gonna love this!"
            scene 1429
            amelia "I know I will!"
            scene 1430
            mc "Wait... Amelia, what are you..."
            scene 1431
            mc "DOING!?"
            scene blowjobamelia1
            play sound bjnormal loop
            mct "F-FUCK!"
            mct "WTF IS SHE DOING??"
            mct "I can't believe this!"
            mct "My wife's mom is sucking my cock while she's in the bathroom."
            mct "Shit! My wife... [violet]... I can't..."
            mc "Amelia... Y-you need to... stop this... [violet] could come back... any second now..."
            mc "..."
            mct "Fuck... She's not listening to me... I need to do something."
            mct "But damn... her mouth feels so good!"
            mct "I don't really wanna stop her now..."
            scene blowjobamelia2
            ""
            mct "Fuck... this is too good."
            mct "She just keeps going..."
            mct "I'm in trouble here. If [violet] sees me like this... it's over."
            stop sound


    scene blackscreen
    $ renpy.pause(1.0, hard=True)
    narrador "Back to [violet]..."
    scene 1347
    v "Ouch!"
    scene 1348
    vt "Oh my god! Why is Jeff here?"
    vt "Wait, is he... wet?"
    menu:
        "Get up immediately! [hints_loyal]":
            $ get_up_fast = "1"
            $ dont_try_to_get_up_yet = "2"
            v "Ahhh!"
        "Don't try to get up yet. [hints_nts]":


            $ dont_try_to_get_up_yet = "1"
            $ get_up_fast = "2"
            v "Jeff! What are you doing here?"
            jeff "Hm... I mean, I'm in my house, and this is my bathroom..."
            scene 1350
            v "Yeah but... why are you here right now?"
            jeff "I was taking a shower."
            v "A shower?"
            v "..."
            vt "That means he's..."
            scene 1349
            vt "NAKED!"
            scene 1351
            vt "So what I'm touching isn't his leg... it's his dick!"
            vt "Oh god, it's hetting hard!"
            vt "I need to get up!"


    scene 1352
    vt "Don't look at it! Don't look at it!"
    scene 1353
    v "Jeff! Why didn't you lock the door?"
    v "I thought there was no one inside."
    scene 1354
    jeff "Why would I lock the door? I live here alone with Amelia."
    scene 1353
    v "Yeah but, don't you ever receive visitors?"
    v "Anyone could come in..."
    v "And why aren't you covering up?"
    scene 1354
    jeff "What? You're the one who barged in without knocking."
    scene 1355
    if let_him_pee == "1":
        jeff "Besides... you've already seen it before..."
    if violet_shower == "1":
        jeff "We seem to like meeting in bathrooms, huh?"
    jeff "Why don't you take a look a it?"
    scene 1357
    vt "What? This is crazy!"
    vt "He wants me to take a look!"
    menu:
        "Get out of there! [hints_loyal]":
            $ get_out_of_there = "1"
            $ take_a_look = "2"
            v "No!"
            scene 1339
            v "Fuck this!"
            v "I'm out of here!"
            play sound dooropen
            scene 1359
            jeff "Fuck... She's really hard to get..."
            jeff "I don't know what to do..."
            jeff "Maybe I've lost my touch."
        "Take a look at it [hints_nts]":


            $ take_a_look = "1"
            $ get_out_of_there = "2"
            vt "Fuck... I'm seriously considering it."
            vt "What's wrong with me?"
            if allow_him_to_jerk_off == "1":
                vt "After all, he's right... I've seen it before and much more, I've watched him masturbate."
            scene 1358
            vt "Okay, there's no point in trying to avoid it now."
            scene 1360
            jeff "There you go!"
            jeff "Take a good look!"
            v "Oh my god! Why do you have a boner?"
            vt "Why is it so big?"
            scene 1355
            jeff "What do you expect, you were pressing against it with your hand."
            jeff "How would I not be hard?"
            if let_him_pee=="1":
                scene 1362
                vt "Oh my... so he's gonna try this again, huh."
                vt "He thinks I'm gonna feel bad again and help him..."
                vt "Haha, I could tease him a bit... I guess [mcname] would love that."
                vt "Alright, time to act."
            scene 1361
            v "Oh... So you're saying it's my fault you're like this?"
            scene 1363
            jeff "Well, kinda..."
            jeff "You know, Amelia and me don't get intimate anymore."
            jeff "She's goona leave me, I know that."
            jeff "And you jumped on me, you know."
            scene 1361
            v "Oh, I'm sorry about that..."
            v "I didn't mean to."
            v "What can I do now?"
            scene 1363
            jeff "Well... you could help me."
            v "Help you with what?"
            jeff "Help me relieve..."
            jeff "I mean, I can't get out like this."
            scene 1361
            v "Oh, I guess you're right."
            v "I kinda owe you that..."
            scene 1355
            jeff "So you're gonna do it?"
            v "Yes, of course."
            jeff "Nice! Come on, go ahead, get naked and start jerking me off."
            scene 1361
            v "You want me to get naked??"
            scene 1355
            jeff "Yeah, I can't be the only one naked here."
            scene 1364
            vt "Alright, I guess it's time to end this."
            vt "I've teased him enough."
            vt "Or did I?"
            menu:
                "Stop the teasing, this is going too far. [hints_nts]":
                    $ stop_teasing = "1"
                    $ keep_going = "2"
                    vt "Yeah, I should stop, it was fun teasing him but this is going too far now."
                    scene 1362
                    v "You know what, I think I've changed my mind."
                    v "You can do it yourself."
                    scene 1339
                    v "I'm out of here!"
                    jeff "What??"
                    play sound dooropen
                    scene 1359
                    jeff "Fuck... She's really hard to get..."
                    jeff "I don't know what to do..."
                    jeff "Maybe I've lost my touch."
                "Keep going. [hints_cheating]":


                    $ keep_going = "1"
                    $ stop_teasing = "2"
                    vt "I don't think [mcname] is gonna like this..."
                    vt "But this situation is making me feel something weird..."
                    vt "And now that my mom is leaving him, I don't feel that bad about it..."
                    vt "I kinda wanna do it..."
                    scene 1365
                    v "Okay Jeff, I'll do it..."
                    scene 1366
                    jeff "Wow!"
                    scene 1367
                    v "Alright, done."
                    v "Is this what you wanted?"
                    jeff "What? No!"
                    scene 1368
                    jeff "C'mon, you know what I want."
                    v "Ahhh! What are you doing?"
                    jeff "I'm showing you what I want."
                    jeff "Don't pretend you don't like it."
                    scene 1369
                    vt "Oh my god! He's so strong and dominating."
                    vt "What is happening to me?"
                    scene 1368
                    jeff "Let me take this off for you."
                    scene 1370
                    play sound dress
                    v "Ahhh."
                    v "No, you can't..."
                    scene 1371
                    vt "Fuck, he took off my bra so easily!"
                    vt "I can't even react."
                    v "Please Jeff, don't..."
                    play sound girlmoan1 volume 0.5
                    scene 1372
                    v "Oohh!"
                    jeff "Yeah, moan for me."
                    jeff "I know you like that."
                    jeff "Now come hee, let me take this off too."
                    play sound fall1
                    scene 1373
                    v "Wait! This is going too far."
                    v "We can't do this!"
                    jeff "Oh, don't worry... I'm not gonna do anything you don't want to."
                    scene 1374
                    jeff "Oh yeah! That's a nice little pussy you got!"
                    jeff "I'm gonna enjoy sliding my dick inside of it."
                    v "What??"
                    v "No!"
                    scene 1375
                    v "Jeff, we just can't do this."
                    v "I'm not gonna cheat on [mcname] like this!"
                    scene 1376
                    jeff "What? It's not cheating. You're just helping me out."
                    jeff "What's wrong with that?"
                    scene 1375
                    v "I don't see it like this... for me this is cheating!"
                    v "I'm not gonna let you fuck me!"
                    scene 1376
                    jeff "Alright, relax..."
                    jeff "Well, if we're not fucking..."
                    scene 1377
                    jeff "Maybe you could blow me at least..."
                    scene 1375
                    v "What? You can't be serious."
                    jeff "Why not? It's a way you could help me without having sex."
                    jeff "And it's definitely not cheating."
                    v "I-I don't know..."
                    scene 1378
                    vt "A handjob."
                    vt "Maybe I could do that..."
                    if calm_her_down == "1":
                        vt "It's not like I haven't done that before anyway."
                    scene 1380
                    vt "And I can't deny I'm getting wet looking at his dick."
                    vt "I really wanna do it..."
                    scene 1379
                    v "Okay Jeff, I'll tell you what."
                    v "I can give you a handjob and that's it!"
                    v "After that, we're done! Got it?"
                    scene 1377
                    jeff "I guess that works for me, haha."
                    jeff "Come here, sit by my side."
                    scene 1382
                    v "Okay, what now?"
                    jeff "Now you can touch it a little."
                    scene 1381
                    v "You can't tell anyone about this, okay?"
                    jeff "Relax, I'm not gonna tell anyone..."
                    jeff "Why would I do that?"
                    v "I don't know..."
                    jeff "C'mon, just touch the tip a little, feel it."
                    v "Okay..."
                    scene 1383
                    jeff "Yeah, that's it."
                    v "I can't believe I'm doing this."
                    jeff "You didn't do anything yet."
                    jeff "Grab it now, feel it in your hand."
                    scene 1384
                    v "Oh god..."
                    v "Why is it so hard already?"
                    jeff "Oh I've been waiting so long for this."
                    jeff "Come on, [violet]."
                    jeff "Stroke it for me."
                    scene handjobjeff1
                    play sound handjobslow  volume 3.0 loop
                    ""
                    v "Like this?"
                    jeff "Yeah, it's good."
                    scene handjobjeff2
                    v "Are you gonna cum soon?"
                    scene handjobjeff3
                    jeff "Haha, you'll have to do better than this to make that happen, sweetie."
                    v "What? Really?"
                    jeff "Yes, why don't you try to do it faster?"
                    jeff "Or you could blow me... I'm sure I'd cum in no time if you suck my dick."
                    play sound handjobwet loop
                    scene handjobjeff1fast
                    v "N-no... I-I'm just gonna do it faster."
                    vt "I'm not gonna suck him... that'd be too much... right?"
                    scene handjobjeff2fast
                    v "Is it good like this?"
                    jeff "Yeah..."
                    scene handjobjeff3fast
                    jeff "But, you know... I'm sure you can do it faster."
                    v "Faster?"
                    v "Hm... okay."
                    play sound handjob volume 5.0 loop
                    scene handjobjeff1faster
                    jeff "Oh yeah, that's better!"
                    vt "Oh god... It's so hard on my hand."
                    vt "If feels so wrong..."
                    if calm_her_down == "1":
                        vt "I know I did it earlier in the hotel bathroom, but..."
                        vt "That was different... [mcname] asked me to do it."
                        vt "It was some stranger, I didn't get to see his face while doing it..."
                        vt "And he came so fast..."
                    scene handjobjeff2faster
                    vt "Jeff is taking so long."
                    vt "I can't believe he didn't cum yet."
                    v "Jeff, tell me you're close."
                    scene handjobjeff3faster
                    jeff "Oh, I'm sorry dear, I feel it's gonna take a little longer like this."
                    jeff "Just keep up this pace, okay?"
                    v "But my arm is getting tired."
                    v "And we don't have much time."
                    jeff "Well, you know what could make me finish in seconds."
                    scene 1388
                    vt "Oh god... here he comes again with that."
                    vt "He's not gonna give up..."
                    scene 1389
                    vt "I can't believe I'm even thinking about doing it."
                    vt "[mcname] must be waiting for me..."
                    vt "I need to make a decision fast."
                    stop sound
                    menu:
                        "Leave while you can.":
                            $ leave_while_you_can = "1"
                            $ give_him_a_blowjob = "2"
                            stop sound
                            scene 1388
                            v "I'm sorry Jeff, I can't do this."
                            scene 1381
                            jeff "What? You're kidding me, right?"
                            scene 1378
                            v "No, I'm not."
                            v "I'm gonna put my clothes and leave."
                            play sound dress
                            scene blackscreen
                            pause 0.5
                            scene 1339
                            v "Bye, Jeff."
                            jeff "Wait, you can't leave me like this."
                            scene 1359
                            jeff "Fuck... She's really hard to get..."
                            jeff "I don't know what to do..."
                            jeff "Maybe I've lost my touch"
                        "Give him a blowjob. [hints_cheating]":

                            $ give_him_a_blowjob = "1"
                            $ leave_while_you_can = "2"
                            stop sound
                            scene 1388
                            v "Jeff, stand up."
                            scene 1381
                            jeff "Oh... what do you have in mind?"
                            v "You'll see..."
                            scene 1390
                            jeff "Uuuhhh... I like where this is going."
                            v "Shut up."
                            v "I swear... no one can know about this."
                            jeff "Don't worry!"
                            jeff "No one's gonna know."
                            scene 1391
                            vt "Alright, I'm about to do it..."
                            vt "No going back now."
                            if calm_her_down == "1":
                                scene 1205
                                show past
                                vt "It's the second penis I'm about to suck today..."
                                scene 1206
                                show past
                                vt "The guy in the hotel bathroom came just by me licking his tip..."
                                scene 1207
                                show past
                                ""
                                scene 1208
                                show past
                                ""
                                scene 1209
                                show past
                                ""
                            scene 1391
                            vt "Maybe Jeff will cum just by feeling my tongue on his dick..."
                            vt "Okay, I'll try this."
                            scene 1392
                            $ renpy.pause(0.5, hard=True)
                            scene 1393
                            $ renpy.pause(0.5, hard=True)
                            scene 1392
                            $ renpy.pause(0.5, hard=True)
                            scene 1393
                            $ renpy.pause(0.5, hard=True)
                            scene 1392
                            $ renpy.pause(0.5, hard=True)
                            scene 1393
                            $ renpy.pause(0.5, hard=True)
                            scene 1392
                            $ renpy.pause(0.5, hard=True)
                            scene 1393
                            $ renpy.pause(0.5, hard=True)
                            scene 1394
                            vt "Nothing..."
                            jeff "What's going on?"
                            jeff "Are you gonna do it or not?"
                            jeff "Put it in your mouth."
                            vt "I see... he's not gonna cum so easily."
                            scene 1391
                            vt "I'm gonna have to go all the way."
                            vt "I just don't know if I can do it..."
                            vt "I think [mcname]'s dick is a little bit longer, but Jeff beats him in thickness..."
                            scene 1395
                            vt "I don't think it's gonna fit in my mouth..."
                            vt "But here I go."
                            scene 1396
                            vt "Oh my god..."
                            scene 1397
                            jeff "Yes!"
                            jeff "Finally! Keep going."
                            scene 1398
                            play sound gag1
                            jeff "You're doing great!"
                            jeff "Try to go deeper."
                            scene 1397
                            pause 0.2
                            scene 1395
                            play sound relieve
                            vt "Oh fuck!"
                            vt "I almost choked on it."
                            scene 1394
                            v "I don't think I can go deeper than that."
                            scene 1399
                            jeff "What?"
                            jeff "No, you can do it, come on."
                            jeff "Just try again, no hands this time, I'm gonna help you."
                            scene 1400
                            v "You promise you're gonna cum soon?"
                            jeff "For sure! If you do as I say, I'm gonna cum in no time, trust me."
                            scene 1401
                            v "Alright..."
                            jeff "Yes, that's it..."
                            scene 1402
                            jeff "I know you can go further than that, c'mon."
                            scene a37_00
                            vt "I can't go further than this."
                            jeff "Perfect!"
                            jeff "Now, open wide! I'll take care of the rest."
                            vt "What does he mean by...?"
                            play sound bjsloopy loop
                            scene blowjobjeff1
                            v "*SLURP*"
                            jeff "Yeah! Nice!"
                            jeff "See? I knew you could take it!"
                            vt "Fuck! He's fucking my mouth!"
                            vt "I'm suffocating on his dick!"
                            vt "But if I back out now he's not gonna cum so soon, and I don't have much time."
                            ""
                            scene blowjobjeff3
                            jeff "Ohh, I've waited so long for this moment."
                            jeff "You have no idea."
                            vt "I need to endure it!"
                            ""
                            scene blowjobjeff2
                            jeff "Your mouth feels so good on my dick, [violet]."
                            jeff "You have such soft lips."
                            vt "God... this is so degrading."
                            vt "Letting him fuck my mouth like this..."
                            vt "So why I'm I getting wet?"
                            ""
                            scene blowjobjeff1
                            jeff "You want me to cum for you, don't ya?"
                            v "P-pleashh... *SLURP*"
                            jeff "Yeah! I'm gonna give it to you."
                            scene blowjobjeff1fast
                            play sound sucking3 loop
                            play music suckinggag
                            jeff "Take it!"
                            v "*AGHHRR*"
                            vt "He's making me gag!"
                            vt "I'm so horny! I want him to cum for me!"
                            scene blowjobjeff3fast
                            jeff "Yeah! Fuck, I'm really close now!"
                            jeff "Don't stop!"
                            scene blowjobjeff2fast
                            jeff "OH FUCK!"
                            jeff "THAT'S SO FUCKING GOOD!"
                            scene blowjobjeff1fast
                            jeff "I wanna cum on your tits!"
                            jeff "Just a little more..."
                            jeff "Fuck, I'm gonna cum!!"
                            stop sound
                            stop music
                            scene 1403
                            play sound relieve
                            jeff "TAKE IT BITCH!"
                            scene 1404
                            play sound guycum2
                            play audio cum1
                            jeff "UUUUNNNGGGHHHHHH!!!!"
                            play audio cumbody
                            scene 1405
                            v "Ahhh!"
                            vt "He really came on my tits..."
                            jeff "Oh, that was nice!"
                            scene 1406
                            v "I hope you had fun... look at the mess you've made on me."
                            v "Now I'm gonna have to clean myself."
                            jeff "Feel free, we're in the bathroom afterall, haha."
                            jeff "And don't give me that look, I know you enjoyed it."
                            scene 1407
                            v "No, I didn't..."
                            v "I just did this because I didn't have a choice."
                            jeff "Oh, you did have a choice... and you made the right one, haha."
                            scene 1408
                            jeff "Alright, I'm gonna get back to bed."
                            jeff "That was really good, I hope we can repeat it soon."
                            scene 1407
                            vt "What have I done..."
                            vt "Jeff is right... I liked it."
                            vt "Feeling used like that... I don't know why, but it got me aroused..."
                            vt "How am I gonna explain this to [mcname]?"
                            vt "I hope he can forgive me..."


    play music neighborhood fadein 1.5 volume 0.2
    scene blackscreen
    $ renpy.pause(1.0, hard=True)
    scene 1335
    if interrupt_her == "1":
        scene 1440
        vt "Oh god... what just happened in that bathroom?"
        vt "My mom is right about Jeff, he's a bastard!"
        vt "I can't believe he's doing things like this behind her back..."
        vt "I need to go home."
        scene 1443
        vt "I hope they're done talking..."

    if let_her_keep_going == "1":
        play sound bjnormal loop
        scene blowjobamelia2
        mc "Holy shit, Amelia!"
        mc "How are you so good at this?"
        scene 1442
        mc "If you keep this up I'm gonna..."
        scene blowjobamelia3
        play audio doorclose volume 0.2
        $ renpy.pause(2.0, hard=True)
        scene a41_0
        mct "Huh? What was that?"
        mct "..."
        scene 1437
        mct "FUCK! SHE'S COMING!"
        mc "Amelia, stop. I think she's coming back."
        amelia "Mmmh... whatsh ditsh you saidgh?"
        stop sound
        scene 1439
        mc "Stop sucking my dick! [violet] is coming!"
        scene 1438
        amelia "WHAT?"
        mc "Quick, get dressed! She can't see us like this!"
        amelia "Oh fuck! Alright!"
        scene blackscreen
        pause 0.5
        scene 1440
        vt "Oh god... what just happened in that bathroom?"
        vt "My mom is right about Jeff, he's a bastard!"
        vt "I can't believe he's doing things like this behind her back..."
        if keep_going == "1":
            scene 1441
            vt "Wait, who am I to judge him?"
            vt "I didn't stop him... I'm just as bad."
            vt "I did all this behind [mcname]'s back..."
            vt "I... I don't know what he'll think if I tell him what happened..."
            scene 1440
            vt "Maybe I should keep this to myself, no one has to know about this."
            vt "And I'm never doing something like this again!"
        vt "I need to go home."
        scene 1443
        vt "I hope they're done talking..."
        scene 1444
        ""


    scene 1445
    mc "So that's all I can say to you..."
    amelia "Oh ok, that helps, thanks!"
    v "Hey. I'm back..."
    scene 1446
    mc "Hey babe, took you long enough there, are you okay?"
    v "Yes... I'm okay now..."
    v "What about you, mom?"
    amelia "Yes honey, I'm feeling really good now."
    amelia "I'll give you a call to tell the details later, don't worry."
    scene 1448
    mc "Alright, that's settled then."
    mc "Do you need anything else, Amelia?"
    mc "I don't want to be rude but our friends are waiting for us, we should get going."
    amelia "Oh, no, don't worry... you guys can go, thanks for helping me out."
    amelia "And I'm sorry for making you come here."
    scene 1447
    v "You don't need to thank us, mom."
    v "And it's always good to see you."
    scene 1446
    v "So, let's go?"
    mc "Yeah, sure."
    scene 1449
    play sound door
    mc "Bye now, don't be afraid to call us if you need anything."
    amelia "Don't worry, I won't."
    amelia "And I hope we can see each other in a better setting than this soon."
    v "I'm sure we will, mom."
    v "Take care."
    scene blackscreen
    $ renpy.pause(2.0, hard=True)
    scene 1450
    mc "I think it's good that she's leaving Jeff, I don't know what it is, I just don't like the guy."
    v "What do you mean?"
    mc "I don't know, I just don't trust him."
    mc "I know I've always gotten along with him..."
    if show_you_are_okay == "1":
        mc "And I know we had that moment when you were in the shower..."
        mc "And it was fun, I don't regret that."
    mc "But I think after everything that happened with Amelia, it's the best if we don't interact with him anymore."
    scene 1451
    v "Oh..."
    mc "What? Don't you agree?"
    v "I..."
    if keep_going == "1":
        menu:
            "Don't tell him what happened. [hints_cheating]":
                $ dont_tell_him_what_happened = "1"
                $ tell_him_what_happened = "2"
                vt "I can't tell him, he'll never forgive me."
                scene 1452
                v "Yeah... I agree."
                v "We should stay away from him."
                mc "I'm glad you agree."
                scene 1451
                vt "Oh god... I hope I'm making the right decision..."
            "Tell him what happened. [hints_loyal] [hints_nts]":


                $ tell_him_what_happened = "1"
                $ dont_tell_him_what_happened = "2"
                v "..."
                scene 1452
                v "Babe, I need to tell you something..."

    if get_out_of_there == "1" or stop_teasing == "1":
        v "..."
        scene 1452
        v "Babe, I need to tell you something..."


    scene blackscreen
    $ renpy.pause(2.0, hard=True)
    scene 1453
    if get_out_of_there == "1":
        v "So I just left him naked there and went back to the living room."
        mc "Whoa!"
        mc "I can't believe he asked you to take a look at it."
        mc "Amelia was right about him... I'm glad you're okay."
        mc "You did the right thing, babe."
        mc "I hope we never see him again."
        v "Yeah, me too."

    if stop_teasing == "1":
        v "So I just stopped with the teasing and went back to the living room."
        mc "Whoa!"
        mc "So you teased him and let him there naked with a hard on..."
        v "Yes... do you think I overdid it?"
        scene 1454
        mc "What? Hahaha, no! that was awesome, babe."
        mc "He deserves that for treating Amelia that bad."
        v "Really? You're not mad?"
        mc "Of course not, baby."
        mc "I love when you tease them."
        scene 1455
        v "Even if I don't tell you before?"
        mc "Yeah, I love it! I find it pretty hot, to be honest."
        mc "As long as you always tell me everything."
        scene 1456
        v "You're something else, you know that, right?"
        mc "Why?"
        v "Why did it take you so long to tell me you had these feelings?"
        scene 1457
        mc "Yeah, I don't know..."
        mc "Guess I've never really thought about it before."
        mc "And I'm still not thinking too much about it."
        scene 1458
        mc "As long as we're both having fun I don't see a reason to stop."
        mc "And I see no problem if you take the initiative sometimes, you know?"
        if calm_her_down == "1":
            mc "Just like you did in the hotel."
            mc "Teasing me like that."
        scene 1455
        mc "But as much as I like it, we should be careful with Jeff."
        mc "It's fun to tease him, but he can be a little unpredictable too, so let's mess with him too much, okay?"
        scene 1459
        v "You're right!"
        v "After all that's happening, the best option is to keep our distance from him."
        scene 1463
        mc "Now, come here."
        mc "I love you so much!"
        v "I love you too, baby."
        scene 1464
        play sound kiss
        ""
        scene 1465
        ""

    if tell_him_what_happened == "1":
        scene 1453
        if keep_going == "1":
            v "So after I jerked him a little..."
        if leave_while_you_can == "1":
            v "I got out of there."

        if give_him_a_blowjob == "1":
            v "I knew he wasn't going to cum so I needed to do something more."
            v "I'm not proud of this but... I had to use my mouth, I'm sorry."
            mc "What!?"
            v "When he finished, he simply went out, leaving me there... with cum on my tits..."
            v "After that I went back to the living room."
            v "I feel so ashamed... but I needed to tell you the truth."
            v "I wouldn't be able to live if I didn't."
            v "Do you think you can forgive me?"
            scene 1460
            mc "Wow... I don't even know what to say."
            mc "I mean... how did it come to this?"
            v "I don't know what came over me... it all happened so fast."
            v "I guess the recent events have left me in this state."
            v "I couldn't say no..."
            v "I'm so sorry."
            if let_her_keep_going == "1":
                mct "Well, it's not like I can say much... I was doing the same, with her mother..."
                mct "I can't be mad at her after all the influence I had over the past few days."
            scene 1461
            mc "Babe... look at me."
            mc "Listen, I'm not gonna pretend I like all this, but part of this is my fault."
            mc "In the last few days, I've put you in some situations that I'm not sure I should've..."
            mc "Although most of it was fun, I know I didn't think much about it and we didn't come to an agreement of how far things could go..."
            scene 1462
            mc "That said, I'm happy you told me the truth."
            mc "That's the most important thing for me."
            mc "At the end of the day our relationship it's stronger than any of this."
            v "So you forgive me?"
            mc "Of course!"
            scene 1463
            mc "Come here."
            mc "I love you so much!"
            v "I love you too, baby."
            scene 1464
            play sound kiss
            ""
            scene 1465
            ""


    scene blackscreen
    pause 1.0
    scene 1466
    mc "Phew, we're finally here!"
    v "It was quite a walk, huh."
    scene 1467
    mc "All that walking around it's starting to have an effect on my legs."
    v "Yeah, you're getting old."
    scene 1468
    mc "You're one year younger than me, if I'm old so are you..."
    v "My legs are just fine, haha."
    scene 1469
    mc "Oh really? I'll make sure your legs are trembling when I'm finished then..."
    v "Ooooh, I can't wait for that!"
    scene 1470
    play sound door
    mc "Anyway, do you think Lee and Yukio are feeling comfortable here already?"
    v "I guess it'll take a little while, but they'll get comfortable soon enough."
    scene 1471
    mc "Yeah, I'm sure they will..."
    scene 1472
    yukio "Yes, put it in me..."
    mct "Huh?"
    scene 1473
    mct "WHAT?!"
    scene 1474
    mct "They're having sex!"
    mct "I can't believe they're doing this in the middle of the living room."
    yukio "I need a dick inside me right now!"
    scene 1475
    yukiot "Huh? Oh, they're back already."
    scene 1482
    yukio "Hi [mcname]!"
    lee "What? Are they're back?"
    scene 1476
    yukiot "Haha, take a good look, handsome."
    yukiot "I bet you love my tits, huh?"
    scene 1473
    mct "Fuck! What is she doing?"
    mct "She's not stopping! I mean, Lee told me she was kind of an exhibitionist..."
    mct "But this..."
    scene 1477
    v "What's going on, honey?"
    mc "Hmm... n-nothing, babe."
    v "Why don't you get inside?"
    mc "I... I don't know if we should..."
    v "Why?"
    scene 1486
    mc "I mean, the weather is great, and we don't know all the neighborhood yet..."
    mc "We could go for a walk..."
    v "What? Didn't you just say your legs were tired from all the walking around?"
    mc "I mean, I..."
    mc "..."
    scene 1478
    play sound door
    v "Alright, you can stand there if you want..."
    v "I'm getting inside."
    mc "Wait..."
    scene 1479
    v "I'm tired and I need a shower."
    scene 1480
    v "I don't know why you don't want me to come in."
    scene 1481
    play sound chockfemale
    v "Uhhh!"
    v "What is that??"
    scene 1483
    mc "Babe, try not to freak out, okay?"
    mc "They're just..."
    v "I can't believe they did this!"
    v "They moved the furniture."
    scene 1484
    mc "What?"
    scene 1487
    mct "Wait, they left..."
    mct "I guess she told Lee to get out while I was talking to [violet]."
    scene 1485
    mct "And [violet] reacted like this because of the furniture?..."
    mct "Sometimes I forget how crazy she can be about that stuff."
    scene 1488
    mc "Oh no! How could they do this?"
    mc "Fucking monsters!"
    v "Ha ha ha, very funny..."
    v "I'm not mad, just surprised."
    scene 1487
    v "I actually kinda like it, we have a lot of space here now."
    v "I was probably gonna do it myself anyway."
    scene 1489
    v "But I'm still not a fan of this sofa tho..."
    mc "Why? What's wrong with it?"
    scene 1490
    v "I don't think it's big enough for us to host an orgy."
    mc "Oh, we're planning to host some?"
    v "Haha, maybe."
    mc "C'mon..."
    scene 1491
    v "I just don't like the color."
    v "And I mean, we've had this sofa for so long, since we moved to that tiny apartment."
    v "I think it's fair that I buy a new one for us."
    scene 1492
    mc "You don't need to, I can buy it."
    v "I really wanna do it."
    v "You've done so much already, let me contribute with something for once, okay?"
    mc "Hm..."
    scene 1493
    mc "Well, I wouldn't mind a comfy sofa and a new bed too."
    mc "I like to be comfortable in my orgies."
    play sound girlsmirk3
    v "Hahahaha."
    scene 1494
    yukio "Did I hear that right?"
    yukio "Are you having an orgy?"
    yukio "You can count me in!"
    scene 1496
    mc "Ah... no, we're just joking around, you know?"
    v "We're gonna buy a new sofa, that's it."
    scene 1495
    yukio "Oh, that's a shame."
    yukio "It would be pretty fun being in an orgy with you two."
    yukio "You both look hot!"
    scene 1497
    mc "Hum... thanks... I guess."
    mc "I mean, you look pretty good too."
    scene 1498
    mc "Lee was very lucky to find you."
    vt "Look at that... she's clearly flirting with him, and [mcname]'s responding."
    vt "A while ago I would be annoyed by this, but now I think we're past that."
    vt "I even like it, to be honest."
    vt "I wonder if he thinks the same about me doing something similar."
    scene 1495
    yukio "So, is everything okay with your mom, [violet]?"
    v "Yes, she's fine, don't worry about it."
    scene 1499
    lee "Hey, you guys are back already."
    yukio "Oh, look who decided to join us."
    yukio "You're a bit late though, all conversation about orgies are over now."
    scene 1500
    lee "What?"
    yukio "Haha, nevermind."
    scene 1501
    yukio "So, what are your plans for tonight?"
    scene 1502
    v "I don't think we have any."
    v "We're kinda tired."
    v "We might just watch a movie or something and go to sleep."
    scene 1501
    yukio "That's so boring!"
    yukio "Are you guys 40?"
    scene 1502
    v "What? No..."
    v "We're just a little tired, maybe going to bed early today will help."
    scene 1501
    yukio "C'mon, it's too early for that."
    yukio "Hear me out, what do you think about playing some games?"
    scene 1502
    mc "Huh? Wha kind of games are you talking about?"
    scene 1504
    yukio "I don't know... do you guys have maybe... a card game or something?"
    mc "No, we don't have any..."
    scene 1506
    lee "Hey, we don't need that... I mean, we could play a drinking game, like truth or dare, you know?"
    yukio "Oh, good one, baby!"
    yukio "That's why I'm with you, haha."
    scene 1507
    yukio "Alright, that's it, let's play a drinking game!"
    scene 1505
    v "What? Do you really wanna play this?"
    v "I remember playing these games in college... some would get really sexual pretty fast."
    v "What type of games are you thinking?"
    scene 1507
    yukio "I'm thinking exactly about that kind, haha."
    yukio "Why? You don't like the idea of having fun with me?"
    yukio "Do you think I'm ugly or something?"
    scene 1505
    v "What? No, I..."
    yukio "Oh I see, you're just too shy to do anything a little more daring, isn't it?"
    scene 1508
    mct "Oh, she just found [violet]'s soft spot, she hates being called shy."
    mc "Hm, babe?"
    mc "Are you okay?"
    v "..."
    v "You know what."
    scene 1503
    v "Alright, I'm in!"
    v "Let's play!"
    play sound transition
    scene blackscreen
    play music menusong fadein 0.1
    centered "{size=+10}{color=FFFFFF}This is the end of episode 5. Please roll back one screen and save your game.{/color}{/size}"
    centered "{size=+10}{color=FFFFFF}If you enjoyed the game, please consider supporting me on Patreon so I can release bigger and faster updates, while also receiving exclusive content and news about the progress and voting for future content.{/color}{/size}"
    centered "{size=+10}{color=FFFFFF}Thanks for playing and for all the support so far, it really means a lot to me. See you in the next update!{/color}{/size}"
    centered "{size=+10}{color=FFFFFF}Special Thanks to Facialalot!{/color}{/size}"
    scene 897
    menu:
        "Go back to game menu":
            pause 0.1




    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
