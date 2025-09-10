
image slanod:
    "sla00.jpg"
    pause 0.01
    "sla01.jpg"
    pause 0.01
    "sla02.jpg"
    pause 0.01
    "sla03.jpg"
    pause 0.01
    "sla04.jpg"
    pause 0.01
    "sla05.jpg"
    pause 0.01
    "sla06.jpg"
    pause 0.01
    "sla07.jpg"
    pause 0.01
    "sla08.jpg"
    pause 0.01
    "sla09.jpg"
    pause 0.01
    "sla10.jpg"
    pause 0.01
    "sla11.jpg"
    pause 0.01
    "sla12.jpg"
    pause 0.01
    "sla13.jpg"
    pause 0.01
    "sla14.jpg"
    pause 0.01
    "sla15.jpg"
    pause 0.01
    "sla16.jpg"
    pause 0.01
    "sla17.jpg"
    pause 0.01
    "sla18.jpg"
    pause 0.01
    "sla19.jpg"
    pause 0.01
    "sla20.jpg"
    pause 0.01
    "sla21.jpg"
    pause 0.01
    "sla22.jpg"
    pause 0.01
    "sla23.jpg"
    pause 0.01
    "sla24.jpg"
    pause 0.01
    "sla25.jpg"
    pause 0.01
    "sla26.jpg"
    pause 0.01
    "sla27.jpg"
    pause 0.01
    "sla28.jpg"
    pause 0.01
    "sla29.jpg"
    pause 0.01
    "sla30.jpg"
    pause 0.01
    "sla31.jpg"
    pause 0.01
    "sla32.jpg"
    pause 0.01
    "sla33.jpg"
    pause 0.01
    "sla34.jpg"
    pause 0.01
    "sla35.jpg"
    pause 0.01
    "sla36.jpg"
    pause 0.01
    "sla37.jpg"
    pause 0.01
    "sla38.jpg"
    pause 0.01
    "sla39.jpg"
    pause 0.01
    "sla40.jpg"
    pause 0.01
    "sla41.jpg"
    pause 0.01
    "sla42.jpg"
    pause 0.01
    "sla43.jpg"
    pause 0.01
    "sla44.jpg"
    pause 0.01
    "sla45.jpg"
    pause 0.01
    "sla46.jpg"
    pause 0.01
    "sla47.jpg"
    pause 0.01
    "sla48.jpg"
    pause 0.01
    "sla49.jpg"
    pause 0.01
    "sla50.jpg"
    pause 0.01
    repeat

label lunch_hall:
    if workrequest ==3 and worktalk ==1:
        scene slunch with fade
        s "Hmmm"
        b "[mname] isn't back yet?"
        s "No"
        s "She told me to prepare lunch today"
        b "Then why it's the same thing, why didn't you prepare something nice"
        scene slunch1 with dissolve
        s "Sit!"
        b "Yes ma'am"
        b "Hahaha!"
        scene slunch2 with dissolve
        s "Now eat!"
        scene slunch3 with fade
        "..."
        b "Do you think she'll get the job?"
        s "I don't know"
        b "I hope she doesn't because I don't like this place"
        s "Why?"
        b "I just don't like it"
        s "Well I hope she does because me I do like it"
        b "It's easy for you to say because you have Rowena around"
        s "Well, you can change that"
        s "You should get more social, and stop being a pervert nerd"
        b "Mee!"
        scene slunch4 with dissolve
        s "Yes you"
        b "What the ..."
        s "Let me eat please"
        b "Ok"
        scene slunch5 with fade
        b "See you later"
        s "..."
        scene broom_day with fade
        "..."
        call screen gnav


    elif workrequest ==3 and worktalk ==2 and day !=7:
        if snaked_lunch == 1:
            jump s_hot_lunch
        else:

            pass
        scene slunch with fade
        s "Hmmm"
        b "What's for lunch"
        scene slunch1 with dissolve
        s "Sit!"
        scene slunch2 with dissolve
        s "Now eat!"
        scene slunch6 with dissolve
        s "Without questions"
        b "Yes ma'am"
        if nadiaasksforstrongdrinks == 1 and snamedrink == 0:
            $ snamedrink = 1
            scene slunch3 with dissolve
            s "I only ask questions"
            b "Uh huh!"
            s "Do you have that strong drink you brought last time?"
            b "Hehe why do you need it?"
            s "I just want to try it again"
            s "Can you get me a bottle?"
            b "Of course"
            b "What do I get in return?"
            s "Get it and you'll see"
            b "Ok"
            pass
        else:


            scene slunch7 with dissolve
            s "Good"
            b "Hahahaha"
            pass

        scene slunch3 with fade
        b "Happy now? She's got the job"
        s "Yes of course"
        if snameworkmelinda ==1:
            b "By the way, I have something to ask you"
            s "What is it?"
            b "Do you want to have some part time job?"
            s "No"
            b "You don't want to know how much money you can get?"
            s "Is it too much?"
            b "Something like $500 to $1000 per visit"
            s "Hmm"
            s "Let me guess, escort?"
            b "Yes, but they are high quality, private"
            b "Sort of a private club"
            s "I'll think about it"
            $ snameworkmelinda = 3
            b "Ok"
            pass
        elif snameworkmelinda == 4:
            b "Did you decide about Melinda's offer"
            s "No"
            b "Why?"
            s "I need to think about it"
            b "There's nothing to think about"
            s "How can you find alibi for me leaving the house for a week or more?"
            b "Hmm true"
            b "We need to think about that"
            pass
        else:
            pass
            "..."
        if snamedrink == 3:
            $ snamedrink = 4
            b "Look"
            b "I've got this drink for you"
            scene slunch3v with dissolve
            s "Yaaay!"
            s "Thank you"
            jump sdrinkreward

        elif elaineshowsup >=1 and day ==6:
            if beachalone == 2:
                $ beachalone = 3
                b "Look"
                b "I've got this voucher for you"
                b "You can use it tomorrow"
                s "What kind of voucher"
                b "Shopping voucher, to the mall nearby"
                s "How much in it!"
                $ giftcardrepeat += 1
                b "200 $"
                s "Wow seriously!"
                b "Yes"
                scene slunch3v with dissolve
                s "Yaaay!"
                s "I'll go with Rowena"
                b "Great"
                if giftcardrepeat >= 4:
                    s "Wait here, I'll be right back"
                    b "Hmmm"
                    scene slkmo with fade
                    b "What the ..."
                    b "Fuck!"
                    scene slunch_hot3 with dissolve
                    s "This was your reward because you got me the voucher"
                    s "Now eat!"
                    b "Yes ma'am"
                    scene slunch_hot4 with dissolve
                    "..."
                    scene slunch_hot5 with fade
                    b "Nice meal"
                    s "You like it?"
                    b "Yeah"
                    scene slunch_hot6 with dissolve
                    b "Lovely dress"
                    s "Yes"
                    b "Can I see it?"
                    s "After we eat"
                    b "Ok"
                    scene slkmo1 with fade
                    b "Hmmm"
                    b "Fucking hot"
                    scene slkmo2 with dissolve
                    s "Wait!"
                    b "Wow you're not wearing panties?"
                    scene slkmo3 with dissolve
                    s "..."
                    b "Let's see"
                    scene slkmo4 with dissolve
                    s "Please stop [bname]"
                    b "Hmm"
                    b "Let's take photos of you in this"
                    s "For my page?"
                    b "Yes"
                    s "Ok cool"
                    scene slkmo5 with fade
                    s "I will put the panties on"
                    b "You don't need to"
                    b "It doesn't show anyway"
                    b "Change the pose"
                    scene slkmo6 with dissolve
                    "..."
                    scene slkmo7 with dissolve
                    b "I think you should take it off!"
                    s "No"
                    b "Then, let me take sexy closeups without face"
                    b "It's good for the page"
                    s "Hmm"
                    s "Ok"
                    b "{i}(Hehehe everyone will know it's you){/i}"
                    menu:
                        "Standing":
                            scene slkmo8 with dissolve
                            b "That's cool"
                            scene slkmo9 with dissolve
                            "..."
                            scene slkmo10 with dissolve
                            b "Great shot"
                            b "Let me make a closeup"
                            scene slkmo11 with dissolve
                            "..."
                            b "A little more up"
                            scene slkmo12 with dissolve
                            b "Awesome"
                            b "A little more up?"
                            s "No [bname] that's enough"
                            b "Ohh..."
                            b "All right"
                            scene slkmo5 with fade
                            b "See you"
                            scene door with fade
                            b "{i}(...){/i}"
                            call screen gnav


                        "All fours" if giftcardrepeat > 1:
                            scene slkmo13 with dissolve
                            b "That's not on all four"
                            s "Yes"
                            b "But I'll take something nice"
                            b "Stay as you are"
                            scene slkmo14 with dissolve
                            b "Done"
                            b "Change the pose"
                            scene slkmo15 with dissolve
                            s "Is the dress ok?"
                            b "Yes awesome"
                            b "Wait let me take it from several angles"
                            scene slkmo16 with dissolve
                            "..."
                            s "No face, OK!?"
                            b "Yes sure"
                            scene slkmo17 with dissolve
                            b "Nice"
                            b "Try something more, I trust you can do better"
                            scene slkmo18 with dissolve
                            $ persistent.unlock_14 = True
                            s "No face"
                            b "Ok Ok"
                            s "I think that's enough"
                            b "Yes as you wish"
                            b "I'll work on them later"
                            b "See you"
                            scene door with fade
                            b "{i}(...){/i}"
                            call screen gnav

                elif srel >= 400:
                    s "Wait here, I'll be right back"
                    b "Hmmm"
                    scene slkmo with fade
                    b "What the ..."
                    b "Fuck!"
                    scene slunch_hot3 with dissolve
                    s "This was your reward because you got me the voucher"
                    s "Now eat!"
                    b "Yes ma'am"
                    scene slunch_hot4 with dissolve
                    "..."
                    scene slunch_hot5 with fade
                    b "Nice meal"
                    s "You like it?"
                    b "Yeah"
                    scene slunch_hot6 with dissolve
                    b "Lovely dress"
                    s "Yes"
                    b "Can I see it?"
                    s "After we eat"
                    b "Ok"
                    scene slkmo1 with fade
                    b "Hmmm"
                    b "Fucking hot"
                    scene slkmo2 with dissolve
                    s "Wait!"
                    b "Wow you're not wearing panties?"
                    scene slkmo3 with dissolve
                    s "..."
                    b "Let's see"
                    scene slkmo4 with dissolve
                    s "Please stop [bname]"
                    b "Hmm"
                    b "Let's take photos of you in this"
                    s "For my page?"
                    b "Yes"
                    s "Ok cool"
                    scene slkmo5 with fade
                    s "I will put the panties on"
                    b "You don't need to"
                    b "It doesn't show anyway"
                    b "Change the pose"
                    scene slkmo6 with dissolve
                    "..."
                    scene slkmo7 with dissolve
                    b "I think you should take it off!"
                    s "No"
                    b "Then, let me take sexy closeups without face"
                    b "It's good for the page"
                    s "Hmm"
                    s "Ok"
                    b "{i}(Hehehe everyone will know it's you){/i}"
                    menu:
                        "Standing":
                            scene slkmo8 with dissolve
                            b "That's cool"
                            scene slkmo9 with dissolve
                            "..."
                            scene slkmo10 with dissolve
                            b "Great shot"
                            b "Let me make a closeup"
                            scene slkmo11 with dissolve
                            "..."
                            b "A little more up"
                            scene slkmo12 with dissolve
                            b "Awesome"
                            b "A little more up?"
                            s "No [bname] that's enough"
                            b "Ohh..."
                            b "All right"
                            scene slkmo5 with fade
                            b "See you"
                            scene door with fade
                            b "{i}(...){/i}"
                            call screen gnav


                        "All fours" if giftcardrepeat > 1:
                            scene slkmo13 with dissolve
                            b "That's not on all four"
                            s "Yes"
                            b "But I'll take something nice"
                            b "Stay as you are"
                            scene slkmo14 with dissolve
                            b "Done"
                            b "Change the pose"
                            scene slkmo15 with dissolve
                            b "Awesome"
                            b "Wait let me take it from several angles"
                            scene slkmo16 with dissolve
                            "..."
                            s "No face, OK!?"
                            b "Yes sure"
                            scene slkmo17 with dissolve
                            b "Nice"
                            b "Try something more, I trust you can do better"
                            scene slkmo18 with dissolve
                            s "No face"
                            b "Ok Ok"
                            s "I think that's enough"
                            b "Yes as you wish"
                            b "I'll work on them later"
                            b "See you"
                            scene door with fade
                            b "{i}(...){/i}"
                            call screen gnav
                else:


                    pass
            else:

                pass
            b "By the way"
            b "Did you know that Elaine slept here last night?"
            s "Really?"
            b "I don't but something is going on between her and her bf"
            b "She's sleeping in [mname]'s room"
            s "Ah, Ok"
            pass
        else:
            if beachalone == 2 and day ==6:
                $ beachalone = 3
                b "Look"
                b "I've got this voucher for you"
                b "You can use it tomorrow"
                s "What kind of voucher"
                b "Shopping voucher, to the mall nearby"
                s "How much in it!"
                b "200 $"
                s "Wow seriously!"
                b "Yes"
                scene slunch3v with dissolve
                s "Yaaay!"
                s "I'll go with Rowena"
                b "Great"
                pass
            else:
                pass

        scene slunch4 with dissolve
        s "Let me eat please"
        b "Ok"
        scene slunch8 with fade
        b "Thank you for the lunch [sname]"
        s "You're welcome"
        menu:
            "Help her with the dishes":
                if srel >=30:
                    scene slunch9a with fade
                    b "I'll help you with the dishes"
                    scene slunch10a with dissolve
                    s "Huh!"
                    scene slunch11a with vpunch
                    s "[bname]! I thought you're going to help me with the dishes"
                    b "I will of course"
                    s "Then do it please"
                    scene slunch10 with fade
                    b "Done"
                    scene slunch11 with dissolve
                    s "Thank you"
                    s "See ya!"
                    b "{i}(What the fuck! Only thank you, maybe next time I should try not helping her){/i}"
                    menu:
                        "Grab her" if workrequest ==3 and day !=7:
                            scene slunchdom with hpunch
                            b "Come here!"
                            scene slunchdom1 with dissolve
                            if sdom >=100:
                                s "Let me go [bname]!"
                                menu:
                                    "Let her go":
                                        if srel >=200:
                                            s "Hmm"
                                            scene slunchdom8 with dissolve
                                            s "Why did you grab me if you want to let me go?"
                                            b "Seriously?"
                                            b "You just asked me to leave you alone"
                                            scene slunchdom9 with dissolve
                                            s "Yes but I thought you wanted to kiss me"
                                            b "Oh all right"
                                            scene slunchdom10 with dissolve
                                            s "Hmm"
                                            scene slunchdom11 with fade
                                            "..."
                                            scene slunchdom12 with dissolve
                                            s "Hehe"
                                            scene slunchdom13 with dissolve
                                            "..."
                                            scene slunchdom14 with dissolve
                                            s "I'll go to my room now"
                                            b "Ok"
                                            if srel >=400:
                                                scene slunchdom16 with fade
                                                s "{i}(Will he come?){/i}"
                                                scene slunchdom15 with dissolve
                                                b "Wow"
                                                scene slunchdom17 with dissolve
                                                b "Nice"
                                                menu:
                                                    "Can I feel it?":
                                                        $ smaid += 1
                                                        scene slunchdom28 with dissolve
                                                        s "You didn't say you want to make me feel something"
                                                        b "Hehe"
                                                        scene slunchdom29 with dissolve
                                                        s "Ahh"
                                                        scene slunchdom30 with dissolve
                                                        s "Ahhh"
                                                        scene slunchdom31 with dissolve
                                                        "..."
                                                        scene slunchdom32 with dissolve
                                                        s "Ahhhh"
                                                        scene slunchdom33 with dissolve
                                                        s "[bname]!!!"
                                                        scene slunchdom34 with hpunch
                                                        b "Ahh"
                                                        scene slunchdom35 with fade
                                                        "..."
                                                        scene broom_day with fade
                                                        "..."
                                                        call screen gnav 
                                                    "Let's take some photos":

                                                        if smaid >= 3:
                                                            s "Hmm"
                                                            s "You didn't ask to feel it?"
                                                            b "No need"
                                                            scene slunchdom18 with fade
                                                            "..."
                                                            scene slunchdom19 with dissolve
                                                            "..."
                                                            scene slunchdom20 with dissolve
                                                            b "Hmm"
                                                            menu:
                                                                "Fuck her":
                                                                    scene slanod
                                                                    s "Ahhh"
                                                                    "..."
                                                                    b "Hhh"
                                                                    "..."
                                                                    s "Fuck harder"
                                                                    b "Yess"
                                                                    scene slunchdom21 with dissolve
                                                                    s "Ahhh"
                                                                    scene slunchdom22 with fade
                                                                    s "What the hell [bname]"
                                                                    b "Sorry, I pulled out"
                                                                    s "Yes pull out, but don't spray me all over with your cum"
                                                                    b "Hehehe sorry"
                                                                    pass
                                                                "Play with her":

                                                                    scene slunchdom23 with dissolve
                                                                    s "Hmmm"
                                                                    scene slunchdom24 with dissolve
                                                                    s "Ah"
                                                                    scene slunchdom25 with dissolve
                                                                    s "Are you going to put it in or now?"
                                                                    b "No"
                                                                    scene slunchdom26 with dissolve
                                                                    "..."
                                                                    scene slunchdom27 with dissolve
                                                                    s "Mhhhm"
                                                                    b "See you later"
                                                                    pass
                                                        else:


                                                            s "Yes, only one"
                                                            scene slunchdom18 with fade
                                                            s "That's it"
                                                            pass
                                            else:
                                                pass
                                        else:

                                            "RAISE YOUR POINTS TO 200"
                                            pass
                                    "Take her to the table" if srel >=200:
                                        s "..."
                                        scene slunchdom2 with dissolve
                                        b "Ouch!"
                                        s "Where are you taking me?"
                                        scene slunchdom3 with dissolve
                                        b "For a kiss"
                                        scene slunchdom4 with dissolve
                                        s "Hmmm"
                                        scene slunchdom3 with dissolve
                                        s "Thank you [bname]"
                                        s "I have to go"
                                        menu:
                                            "Cup her breast":
                                                scene slunchdom5 with dissolve
                                                s "[bname]! Are you out of your mind"
                                                b "No I'm not"
                                                s "Then remove your hand"
                                                b "I don't want"
                                                if scorr >= 60:
                                                    scene slunchdom6 with dissolve
                                                    s "And I'll do this"
                                                    b "Ouch! My balls"
                                                    s "Hahaha"
                                                    b "You hurt me"
                                                    scene slunchdom7 with dissolve
                                                    s "Hahaha"
                                                    s "What are you going to do about it!"
                                                    b "We'll see"
                                                    s "Put your best foot forward hahaha!"
                                                    jump staughtalesson
                                                else:

                                                    s "Enough [bname]"
                                                    s "See you later"
                                                    scene broom_day with fade
                                                    "RAISE YOUR CORRUPTION POINTS TO 60"
                                                    call screen gnav 
                                            "Continue":


                                                "..."
                                                pass
                                        s "See you later"
                                        scene broom_day with fade
                                        "..."
                                        call screen gnav 
                            else:

                                s "Let me go [bname]!"
                                "RAISE YOUR DOMINATION POINTS TO 100"
                                pass
                        "Continue":

                            pass
                    scene broom_day with fade
                    "..."
                    call screen gnav   
                else:

                    scene slunch9 with fade
                    b "I'll help you with the dishes"
                    scene slunch10 with dissolve
                    show screen srelup
                    "..."
                    $ srel += 2
                    b "Done"
                    hide screen srelup
                    scene slunch11 with dissolve
                    s "Thank you"
                    b "See ya!"
                    scene broom_day with fade
                    "..."
                    call screen gnav    
            "No need":



                scene slunch5 with fade
                show screen sreldw
                b "See you later"
                $ srel -= 1
                s "..."
                hide screen sreldw
                scene slunch5_hr with dissolve
                s "Hey!"
                s "Aren't you going to help me with the dishes?"
                b "Hmm"
                menu:
                    "What do I get in return?":
                        s "Huh!"
                        s "What do you want?"
                        menu:
                            "I want to see the bikini I bought for you" if bikini3 == 2:
                                s "Whaaat!?"
                                b "Yes, you heard me"
                                if sdom >=25 and srel >=60:
                                    scene slunch6_hr with dissolve
                                    b "Come on! What are you thinking about?"
                                    $ sstrip = 1
                                    s "Go start washing, I'll be thinking about it"
                                    b "Ok cool"
                                    scene slunch12 with fade
                                    "..."
                                    b "Done!"
                                    s "Ok, sit on the couch and wait for me"
                                    scene slunch7_hr with fade
                                    "..."
                                    scene slunch8_hr with dissolve
                                    s "It's going to be a quick glance"
                                    b "... OK"
                                    if hotphotos_done == 1:
                                        b "{i}(Hehe quick glance my ass){/i}"
                                        scene slunch9_hra with dissolve
                                        "..."
                                        b "Looks goood on you"
                                        s "Thanks"
                                        scene slunch10_hr with dissolve
                                        "..."
                                        scene slunch19_hr with dissolve
                                        b "{i}(Cool! she changed after we did the hot shoot){/i}"
                                        scene slunch20_hr with dissolve
                                        if elaineshowsup ==1 and day ==6:
                                            e "Where can I get some water please?"
                                            scene slunchse with dissolve
                                            s "Huh!"
                                            e "Nice bikini [sname]"
                                            s "Thanks"
                                            b "Water is there on the kitchen table"
                                            scene slunchse1 with dissolve
                                            e "Ok"
                                            scene slunchse2 with dissolve
                                            e "I'll go back to sleeping"
                                            e "Thank you guys"
                                            e "You can continue whatever you were doing"
                                            s "Happy now?"
                                            pass

                                        elif elaineagain ==2 and day ==6:
                                            e "Where can I get some water please?"
                                            scene slunchse with dissolve
                                            s "Huh!"
                                            e "Nice bikini [sname]"
                                            s "Thanks"
                                            b "Water is there on the kitchen table"
                                            scene slunchse1 with dissolve
                                            e "Ok"
                                            scene slunchse2 with dissolve
                                            e "I'll go back to sleeping"
                                            e "Thank you guys"
                                            e "You can continue whatever you were doing"
                                            e "Mhm [sname]"
                                            scene slunchse with dissolve
                                            s "Yes?"
                                            e "Can I ask you something?"
                                            s "Sure"
                                            e "Privately please"
                                            s "Yes let's go to my room"
                                            jump etalkwithsname
                                        else:




                                            s "Happy now?"
                                            pass

                                        b "Hmm"
                                        menu:
                                            "Do you want to do a photo shoot?":
                                                b "Of course I am happy"
                                                b "Do you want to take some photos in this?"
                                                scene slunch21_hr with dissolve
                                                s "At this time?"
                                                b "Yes why not"
                                                s "Only few photos"
                                                b "Yes"
                                                jump sroom_day_photos
                                            "Of course I am":

                                                scene slunch22_hr with dissolve
                                                s "I'll go now"
                                                if srel >=200:
                                                    scene slunched with hpunch
                                                    b "Wait"
                                                    s "What do you want?"
                                                    b "Nothing extra?"
                                                    s "Not now"
                                                    if sdom >=35:
                                                        b "Hmm why?"
                                                        s "I don't feel like it"
                                                        b "But me I feel like it"
                                                        scene slunched1 with vpunch
                                                        b "Take it off"
                                                        s "Hmmm"
                                                        scene slunched2 with fade
                                                        s "..."
                                                        jump slunchplus
                                                    else:


                                                        b "Hmm why?"
                                                        s "I don't feel like it"
                                                        b "Ok"
                                                        b "Bye"
                                                        "Raise your domination points to 35"
                                                        b "Thank you for the reward"
                                                        scene broom_day with fade
                                                        "..."
                                                        call screen gnav   
                                                else:

                                                    pass

                                                b "Thank you for the reward"
                                                scene broom_day with fade
                                                "..."
                                                call screen gnav   
                                    else:
                                        pass
                                    scene slunch9_hr with dissolve
                                    "..."
                                    b "Looks goood on you"
                                    s "Enough please"
                                    scene slunch10_hr with dissolve
                                    s "I'll go now"
                                    b "Thank you"
                                    scene broom_day with fade
                                    b "{i}(Cool){/i}"
                                    call screen gnav   
                                else:
                                    scene slunch6_hrefuse with dissolve
                                    s "I'll washes the dishes myself"
                                    s "There's the way out!"
                                    b "Damn!"
                                    b "Ok Ok"
                                    scene broom_day with fade
                                    "RAISE YOUR DOMINATION POINTS TO 25 AND RELATIONSHIP TO 60"
                                    call screen gnav  
                            "A kiss":

                                if srel >=200:
                                    s "Ok"
                                    pass
                                else:
                                    s "Whaaat!?"
                                    b "Yes, just a kiss"
                                    pass
                                scene slunch6_hr with dissolve
                                b "Come on! What are you thinking about?"
                                s "Go start washing, I'll be thinking about it"
                                b "Ok cool"
                                scene slunch10 with fade
                                "..."
                                b "Done!"
                                scene slunch11hr with fade
                                s "Ok"
                                s "No pervy stuff!"
                                scene slunch12hr with dissolve
                                "..."
                                menu:
                                    "Take a look":
                                        scene slunch13hr with dissolve
                                        b "Hmmm"
                                        menu:
                                            "Cup it":
                                                scene slunch13hra with hpunch
                                                "..."
                                                if srel >=300 and scorr >=30:
                                                    s "Huh"
                                                    b "{i}(Cool! no reaction){/i}"
                                                    scene slunch19hr with dissolve
                                                    b "Huh!"
                                                    scene slunch20hr with dissolve
                                                    b "Ouch!"
                                                    b "leave my penis alone"
                                                    scene slunch11hr with dissolve
                                                    s "You think you can touch my boobs"
                                                    s "And I can't touch yours"
                                                    b "Well if you touch mine, you have to take care of it"
                                                    s "Same here"
                                                    s "And you touched first, so you'd better finish what you started"
                                                    b "That's Ok but you put on something nice for me"
                                                    s "Ok"
                                                    jump sposing
                                                else:



                                                    scene slunch13hrb with dissolve
                                                    s "Hey!"
                                                    b "Err"
                                                    b "Sorry"
                                                    scene broom_day with fade
                                                    b "{i}(Damn){/i}"
                                                    call screen gnav  
                                            "Don't":
                                                pass
                                    "Pervy stuff":

                                        scene slunch13hr with dissolve
                                        "..."
                                        if srel >=100:
                                            scene slunch14hr with dissolve
                                            "..."
                                            scene slunch16hr with dissolve
                                            b "{i}(Cool! no reaction){/i}"
                                            scene slunch19hr with dissolve
                                            b "Huh!"
                                            if srel >=300 and scorr >=30:
                                                scene slunch20hr with dissolve
                                                b "Ouch!"
                                                b "leave my penis alone"
                                                scene slunch11hr with dissolve
                                                s "You think you can touch my boobs"
                                                s "And I can't touch yours"
                                                b "Well if you touch mine, you have to take care of it"
                                                s "Same here"
                                                s "And you touched first, so you'd better finish what you started"
                                                jump sboobjob
                                            else:
                                                "RAISE RELATIONSHIP TO 300 AND CORRUPTION TO 30"
                                                pass


                                        elif sblowjobdone == 1:
                                            scene slunch14hr with dissolve
                                            "..."
                                            scene slunch16hr with dissolve
                                            b "{i}(Cool! no reaction){/i}"
                                            scene slunch19hr with dissolve
                                            b "Huh!"
                                            if srel >=300 and scorr >= 30:
                                                scene slunch20hr with dissolve
                                                b "Ouch!"
                                                b "leave my penis alone"
                                                scene slunch11hr with dissolve
                                                s "You think you can touch my boobs"
                                                s "And I can't touch yours"
                                                b "Well if you touch mine, you have to take care of it"
                                                s "Same here"
                                                s "And you touched first, so you'd better finish what you started"
                                                jump sboobjob
                                            else:
                                                "RAISE RELATIONSHIP TO 300 AND CORRUPTION TO 30"
                                                pass

                                        elif sphotos_progress == 2:
                                            scene slunch14hr with dissolve
                                            "..."
                                            scene slunch17hr with dissolve
                                            b "{i}(Cool! no reaction){/i}"
                                            scene slunch19hr with dissolve
                                            b "Huh!"
                                            if srel >=300 and scorr >= 30:
                                                scene slunch20hr with dissolve
                                                b "Ouch!"
                                                b "leave my penis alone"
                                                scene slunch11hr with dissolve
                                                s "You think you can touch my boobs"
                                                s "And I can't touch yours"
                                                b "Well if you touch mine, you have to take care of it"
                                                s "Same here"
                                                s "And you touched first, so you'd better finish what you started"
                                                jump sboobjob
                                            else:
                                                "RAISE RELATIONSHIP TO 300 AND CORRUPTION TO 30"
                                                pass
                                        else:





                                            scene slunch15hr with dissolve
                                            s "Huh!"
                                            scene slunch18hr with hpunch
                                            s "Pervert"
                                            b "Ouch!"
                                            b "She snapped"
                                            scene broom_day with fade
                                            "..."
                                            call screen gnav 
                                    "No need":

                                        pass

                                scene slunch11hr with fade
                                s "Thank you"
                                s "For washing the dishes"
                                b "See ya!"
                                scene broom_day with fade
                                "..."
                                call screen gnav  
                    "Help her":







                        b "Ok"
                        scene slunch10 with fade
                        show screen srelup
                        "..."
                        $ srel += 2
                        b "Done"
                        hide screen srelup
                        scene slunch11 with dissolve
                        s "Thank you"
                        b "See ya!"
                        scene broom_day with fade
                        "..."
                        call screen gnav   
    else:






        scene lunch with fade
        m "Sit [bname]"
        scene lunch1 with fade
        "..."
        menu:
            "What's wrong?":
                b "What's wrong?"
                scene lunch2 with dissolve
                m "Why aren't you eating?"
                b "I am!"
                pass
            "Talk to [sname]":

                scene lunch3 with dissolve
                b "How are your studies [sname]?"
                scene lunch4 with dissolve
                s "Everything is okay"
                menu:
                    "Let me know if you need help":
                        s "I will"
                        pass
                    "Good":

                        b "Good"
                        scene lunch3 with dissolve
                        "..."
                        pass


            "Wandering eyes" if wk>=3:
                b "{i}(Hmm){/i}"
                b "{i}(Left or right?){/i}"
                menu:
                    "Right":
                        scene lunch_m_peek with dissolve
                        "..."
                        m "[bname]!"
                        scene lunch_m_s with dissolve
                        b "Yes"
                        pass
                    "Left":
                        scene lunch_s_peek with dissolve
                        "..."
                        m "[bname]!"
                        scene lunch_m_s with dissolve
                        b "Yes?"
                        pass

                scene lunch2 with dissolve
                m "Why aren't you eating?"
                b "I am!"
                pass


        if wk>=2:
            scene lunch6 with fade
            $ smoneym = 1
            if persistent.patch_enabled:
                s "Mom?"
                pass
            else:
                s "Madam"
                pass
            if smobilegiven == 1:
                pass
            else:
                m "What?"
                s "About my phone"
                s "Can I buy a new one?"
                m "[sname] I have no money for phones!"
                scene lunch7 with dissolve
                s "But..."
                s "The battery is getting exhausted"
                m "I said no"
        else:
            pass
        scene lunch1 with dissolve
        m "It's eating time, not speaking time"
        b "OK"
        scene lunch5 with fade
        if persistent.patch_enabled:
            b "{i}Thank you for the lunch mom{/i}"
            pass
        else:
            b "{i}Thank you for the lunch ma'am{/i}"
            pass
        if workrequest ==3:
            menu:
                "Do you need help with the dishes?":
                    scene lunch8 with fade
                    m "That would be nice of you"
                    scene lunch9 with fade
                    "..."
                    m "Thank you [bname]"
                    show screen mrelup
                    $ mrel += 2
                    b "It's ok"
                    hide screen mrelup
                    m "I've got to go, I have a nails appointment"
                    if mnailpolish == 1:
                        b "Cool you've decided to do them?"
                        m "Yes"
                        menu:
                            "Can I come with you?":
                                m "Not in this version"
                                b "Ok"
                                pass
                            "Continue":

                                pass
                    else:
                        b "Cool, no worries"
                        pass

                    scene hall_d with fade
                    b "{i}(Nail, appointment!){/i}"
                    b "{i}(Hmm, let's try to find out){/i}"
                    menu:
                        "Go to the window":
                            pass
                        "Follow her" if elaine_convince == 4:
                            jump mgettingreadyfornails
                    scene mstairs with fade
                    "..."
                    scene lunch_stairs_nail with dissolve
                    b "{i}(Dressing up...){/i}"
                    scene lunch_stairs_nail3 with dissolve
                    b "{i}(Hmmm){/i}"
                    if mrel >=200 and elaine_convince == 4:
                        scene lunch_stairs_nail3a with dissolve
                        m "{i}(Hmmm, there's someone at the window){/i}"
                        m "{i}(Could it be the neighbours boy){/i}"
                        m "{i}(I'll report him to the police){/i}"
                        scene lunch_stairs_nail4a with dissolve
                        m "{i}(Or not...){/i}"
                        m "{i}(Hmmm, it's nice to be admired anyway){/i}"
                    else:
                        pass
                    scene lunch_stairs_nail1 with dissolve
                    b "{i}(This looks like more than a nails appointment...){/i}"
                    scene lunch_stairs_nail2 with dissolve
                    m "{i}(Finally, a day for myself){/i}"
                    m "{i}(I'll do nails, laser){/i}"
                    m "{i}(And have lunch with Melinda){/i}"
                    "HEY YOU!"
                    scene mstairs3 with vpunch
                    "I'LL CALL POLICE"
                    b "Damn, it's not what you think it is!"
                    "I'm calling the police now!"
                    b "Damn"
                    b "{i}(I should leave){/i}"
                    scene hall_d with fade
                    b "{i}(Damn, [mname] left){/i}"
                    b "I think I should go see her"
                    b "We don't need any scandal"
                    menu:
                        "Go see her":
                            jump neighb
                        "No need":
                            call screen gnav
                "Leave":


                    pass
        else:
            pass
        scene hall_d with fade
        b "{i}(...){/i}"
        call screen gnav
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
