label EP11_Begin:
    scene black
    "Anna got home..."
    show text "{size=+20}Press Space{/size}"
    pause
    $ EP11_var_1 = True
    hide text


label EP11_Sleep_1:
    $ EP11_var_2 = True
    a "So much stuff has happened... I need some good sleep."
    a "This bed is so comfy."
    a "Goodnight..."
    stop music fadeout 1
    scene black with Dissolve(1)
    play sound interface_sound
    show text "Thursday morning..." with Dissolve(1)
    pause
    hide text
    scene 31-1 morning 3 with Dissolve(1)
    if EarlHelp == True:
        "Anna got a text to meet up with Earl at the precinct."
        jump EP11_Precinct
    else:
        $ EP11_var_4 = True
        jump EP11_Work_1

    jump bedroom

label EP11_Precinct:
    scene black with Dissolve(1)
    play sound door2
    play music distantsong
    scene 39-3 earl 1 with Dissolve(1)
    "Anna entered the police station."
    "A shiver moved down her spine."
    "While she thought she could leave this part behind her..."
    "It kept creeping back, stalking her."
    scene 39-3 earl 2 with Dissolve(1)
    a "Hi. Is Detective Earl in?"
    d4 "Your name?"
    scene 39-3 earl 3 with Dissolve(1)
    a "Anna."
    scene 39-3 earl 4 with Dissolve(1)
    d4 "Yes, Earl will be here in a moment."
    a "Thanks."
    d4 "No problem. Is there anything else?"
    scene 39-3 earl 3 with Dissolve(1)
    a "Umm..."
    $ EP11_menu_1_var_1 = False
    $ EP11_menu_1_var_2 = False
    menu EP11_menu_1:
        "How long has Earl worked here?" if EP11_menu_1_var_1 == False:
            scene 39-3 earl 5 with Dissolve(1)
            d4 "I might be wrong, but he is the oldest, still working, guy in the force. Around 40 years, maybe."
            d4 "He is very experienced."
            a "Damn."
            scene 39-3 earl 4 with Dissolve(1)
            d4 "That's all I'm allowed to disclose."
            $ EP11_menu_1_var_1 = True
            jump EP11_menu_1
        "How many people has Earl put away?" if EP11_menu_1_var_2 == False:
            scene 39-3 earl 4 with Dissolve(1)
            d4 "I think he's coming up to three hundred."
            a "I didn't expect that many..."
            scene 39-3 earl 5 with Dissolve(1)
            d4 "He is the most successful officer in the history of the precinct."
            d4 "He has received several commendations and awards for his efforts."
            a "I see."
            $ EP11_menu_1_var_2 = True
            jump EP11_menu_1
        "That's all.":
            pass
    play sound surprise
    scene 39-3 earl 6 with Dissolve(1)
    d4 "Sir. She's here for you."
    earl "Yeah. Thanks. I'll take it from here."
    scene 39-3 earl 7 with Dissolve(1)
    earl "Got here in one piece, I see."
    earl "{i}...One piece of nice ass...{/i}"
    scene 39-3 earl 8 with Dissolve(1)
    a "I couldn't {b}wait{/b} what other surprises you had for me."
    "Anna shrugged off condescendingly."
    scene 39-3 earl 9 with Dissolve(1)
    earl "Right... How about we continue this somewhere else?"
    a "Sure."
    play sound cloth_sound1
    scene 39-3 earl 10 with Dissolve(1)
    a "Called me here to antagonize?"
    earl "Enough with the shit."
    earl "I called you here because it's not over..."
    scene 39-3 earl 11 with Dissolve(1)
    a "..."
    scene 39-3 earl 12 with Dissolve(1)
    a "What am I supposed to do with that information?"
    a "I'm not the police officer. Not the one investigating, making sure everything's ok."
    scene 39-3 earl 13 with Dissolve(1)
    earl "I might come off as a hard ass..."
    earl "But it's my way of working. So don't take my previous behavior for granted."
    earl "I have info that suggests that you are under threat."
    earl "That someone knows and has informed certain 'people' of your involvement."
    earl "Someone in the station..."
    earl "While I get it under control, I can trust nobody."
    scene 39-3 earl 14 with Dissolve(1):
        linear 60 zoom 1.2
    a "What?"
    a "How do I deal with this?"
    a "You won't just leave me out to dry?"
    "While Anna was shooting questions left and right..."
    "Earl was lost in thought."
    scene 39-3 earl 15 with Dissolve(1):
        linear 60 zoom 1.2
    "Fantasies rushed through his head."
    "He was plotting a new plan."
    "A way of getting what he wants..."
    play sound surprise
    scene 39-3 earl 16 with vpunch
    a "Hello?"
    "Anna finally settled down before people started looking."
    a "How are we gonna deal with this?"
    scene 39-3 earl 17 with Dissolve(1)
    earl "I've got an idea!"
    earl "I'll spare you all but the most important details."
    earl "I know how to root out the bad guy. But you will have to stay at a hotel for the duration."
    scene 39-3 earl 18 with Dissolve(1)
    earl "Simple, really. It's a sting."
    earl "I will get someone to help me, and we'll catch the culprit."
    earl "I will plant some 'clues' so that the person coming after you are certain they will catch you."
    scene 39-3 earl 19 with Dissolve(1)
    play sound jacketcloth
    earl "Meanwhile..."
    earl "You'll have to stay at this hotel."
    earl "It's probably for a night only."
    earl "You should manage."
    earl "I will take care of the expenses."
    scene 39-3 earl 20 with Dissolve(1)
    a "I hope this works."
    earl "It will... Oh, it will..."
    scene 39-3 earl 21 with Dissolve(1)
    earl "Hehe..."
    "The man was plotting and plotting. Getting the best out of every situation."
    scene 39-3 earl 22 with Dissolve(1)
    a "I sure hope this is the last time I get involved in this."
    scene 39-3 earl 23 with Dissolve(1)
    "As she was walking out, she noticed someone in the interrogation room."
    a "It can't be..."
    "Was it the nerves... Or something else..."
    "It felt like he was watching her."
    scene 39-3 earl 24 with Dissolve(1)
    "..."
    scene black with Dissolve(2)
    $ EP11_var_4 = True
    pause 1.5
    jump EP11_Work_1
screen EP11_Emails(received, label_name, email_who, content_message, signature):
    zorder 250
    sensitive (not renpy.get_screen("say"))
    add "images/office/office_imagemap/email_background.jpg"
    frame:
        background None
        xsize 500
        ysize 100
        xalign 0.1
        yalign 0.1
        if received == True:
            text "From: " + email_who size 25 color "#000"
        else:
            text "To: " + email_who size 25 color "#000"
    frame:
        background None
        xsize 1400
        ysize 400
        xalign 0.1
        yalign 0.3
        has vbox
        text content_message color "#000"
        text signature color "#000"
    if received == True and label_name != "None":
        imagebutton auto "images/office/office_imagemap/reply_%s.png":
            focus_mask True
            action [Hide("EP11_Emails", transition=Dissolve(1)), Jump(label_name)]
screen EP11_Write_Email():
    zorder 250
    sensitive (not renpy.get_screen("say"))
    add "images/office/office_imagemap/email_background.jpg"
    frame:
        background None
        xsize 500
        ysize 100
        xalign 0.1
        yalign 0.1
        text "To: Tombale@BBDInc.org" size 25 color "#000"
    frame:
        background None
        xsize 1400
        ysize 400
        xalign 0.1
        yalign 0.3
        has vbox
        for i in range(len(content_message_list)):
            text content_message_list[i] color "#000"
        if EP11_Email_Pic_var_1 == True:
            if EP11_Email_Pic_var_2 == True:
                add im.Scale("images/other/Episode_11/EP11_RegularWork/generic office 6.jpg", 800, 450)

label EP11_Work_1:
    play music jazzmusic
    scene generic office 6 with Dissolve(1)
    "Anna entered her office. Immediately thinking to herself. What has to be done."
    a "I should check my emails first."
    if dianaGoodRelations == False:
        a "Probably some email from Jeremy."
    else:
        a "Perhaps an email from Ethan."
    a "I think there is a new company on the horizon that requires our services."
    scene generic office 1 with Dissolve(1)
    a "Right, let's see."
    play sound mouse_click_1
    $ EP11_Emails_1 = False
    $ EP11_Emails_2 = False
    $ EP11_Emails_3 = False
    menu EP11_Work_1_Emails:
        "Email from Jeremy." if dianaGoodRelations == False and EP11_Emails_1 == False:
            show screen disableClick
            $ EP11_Emails_1 = True
            show screen EP11_Emails(True, "EP11_Work_2","jeremy.direct@jercomp.org", "I've heard of a new company looking to expand their interests in this hemisphere. BBDInc. They are on our radar for some time. Send them an email.", "")
            pause
            label EP11_Work_2:
                hide screen disableClick
                show screen EP11_Emails(False, "None", "anna.direct@jercomp.org", "Ok, I'm on it.", "Anna")
                pause
                hide screen EP11_Emails with Dissolve(1)
            jump EP11_Work_1_Emails
        "Email from Ethan." if dianaGoodRelations == True and EP11_Emails_1 == False:
            show screen disableClick
            $ EP11_Emails_1 = True
            show screen EP11_Emails(True, "EP11_Work_3","ethan.direct@jercomp.org", "Hey, Anna. I think you've heard of BBD inc? By the looks of it, they are trying to expand. Send them an email, thanks!", "Ethan")
            pause
            label EP11_Work_3:
                hide screen disableClick
                show screen EP11_Emails(False, "None", "anna.direct@jercomp.org", "Ok, I'm on it.", "Anna")
                pause
                hide screen EP11_Emails with Dissolve(1)
            jump EP11_Work_1_Emails
        "Send an Email to BBD Inc." if EP11_Emails_1 == True:
            pass
label EP11_Work_4:
    show screen EP11_Write_Email
    menu:
        "Hello, my name is Anna, and I'm a representative of Jercomp. An all-inclusive service company.":
            $ content_message_list.append("Hello, my name is Anna and I'm a representative of Jercomp. An all-inclusive service company.")
        "Welcome to the western Hemisphere. My name is Anna, and I'm a partner at a company called Jercomp. We provide the highest quality business-to-business service packets.":
            $ content_message_list.append("Welcome to the western Hemisphere. My name is Anna and I'm a partner at a company called Jercomp. We provide highest quality business to business service packets.")
    show screen EP11_Write_Email with Dissolve(1)
    pause
    menu:
        "We can provide services like accounting in an international context, streamlined contract oversight, legal advice, and others. The full packages can be found at jercomp.org.":
            $ content_message_list.append("We can provide services like accounting in international context, streamlined contract oversight, legal advice and others. The full packages can be found at jercomp.org.")
        "Our service packets contain many legal, financial, and other services. see jercomp.org for more info.":
            $ content_message_list.append("Our service packets contain many legal, financial and other services. see jercomp.org for more info.")
    show screen EP11_Write_Email with Dissolve(1)
    pause
    menu:
        "You can also have a personalized, for the company, service package. Essentially you won't have to worry about your dealings in other markets as we will take care of the day-to-day.":
            $ content_message_list.append("You can also have a personalized, for the company, service package. Essentially you won't have to worry about your dealings in other markets as we will take care of the day to day.")
        "We will provide the best service and you will be able to forget about the worries of unknown markets.":
            $ content_message_list.append("We will provide the best service, and you will be able to forget about the worries of unknown markets.")
    show screen EP11_Write_Email with Dissolve(1)
    pause
    menu:
        "We will eagerly await your reply and hope for future business together.":
            $ content_message_list.append("We will eagerly await your reply and hope for future business together.")
        "I will wait for your reply eagerly, as I value your input.":
            $ content_message_list.append("I will wait for you reply eagerly, as I value your input.")
    show screen EP11_Write_Email with Dissolve(1)
    pause
    menu:
        "Signature: Anna":
            $ content_message_list.append("Anna")
        "Signature: Anna, you're future slut. (IF Corruption > 30)":
            $ content_message_list.append("Anna, you're future slut.")
    pause
    scene generic office 2
    hide screen EP11_Write_Email with Dissolve(1)
    a "There. I hope they respond by tomorrow. Probably actively looking for help in this market."
    play sound notifsound
    a "An email just came in, can't be BBD just yet, can it?"
    scene generic office 1 with Dissolve(1)
    a "Nope, just Madison."
    show screen disableClick
    show screen EP11_Emails(True, "EP11_Work_5", "madison.direct@jercomp.org", "I've got some news for you, I don't know if you are aware of this, Don't go anywhere, I will go upstairs in a couple mins.", "")
    pause
    label EP11_Work_5:
        hide screen disableClick
        show screen EP11_Emails(False, "None", "madison.direct@.jercomp.org", "Ok, I'll grab a coffee. Waiting.", "")
        pause
    scene 31-3 jeremy 20
    hide screen EP11_Emails with Dissolve(1)
    a "Huh... Well I'll go grab a coffee in the meantime."
    scene black with Dissolve(1)
    play sound door2
    scene 39-1 meeting 2 with Dissolve(1)
    a "Ah... Emily, My favourite!"
    scene 39-1 meeting 3 with Dissolve(1)
    e "I wouldn't have it any other way."
    e "How have you been?"
    a "Well, just sent an email to another company that we could do business with."
    e "Oh. More work for me, haha!"
    a "Don't worry, I think we will need to expand in the near future."
    scene 39-1 meeting 4 with Dissolve(1)
    e "Oh?"
    a "Yeah."
    e "Cheers to that."
    scene 39-1 meeting 5 with Dissolve(1)
    e "But how have you been in general? Asking personally."
    a "Oh..."
    menu:
        "Things are looking up, to be honest.":
            scene 39-1 meeting 6 with Dissolve(1)
            a "Starting to put some things behind me. Moving up in the world."
            a "Taking you with me. Heh."
            e "Of course. If you drink martinis, I wanna drink them, too."
        "Plenty of not-so-good things have been happening.":
            a "And on top of that: Work, home, work, home."
            e "Riight... I know you ain't that bland."
            e "What about your sexual endeavors?"
            scene 39-1 meeting 6 with Dissolve(1)
            a "They are private, as you know..."
            e "Really? I wouldn't have thought. Haha."
            e "You'll tell me later, won't you?"
            a "Of course, there is plenty of tea to spill. haha."
            a "As long as you also give me something."
            e "What do you take me for? Of course, I got plenty."
    play sound woman_hmm_1
    scene 39-1 meeting 7 with Dissolve(1)
    m1 "Hey, Anna. Glad I caught you."
    a "Hey. Yeah?"
    scene 39-1 meeting 8 with Dissolve(1)
    m1 "Listen, umm... I don't know how we missed this, but..."
    m1 "There is a board meeting in a couple of hours."
    play sound surprise
    a "What?"
    scene 39-1 meeting 8-1 with Dissolve(1)
    m1 "Just heard about it from Ethan."
    m1 "I don't know how no one was notified."
    m1 "I think we somehow missed the memo."
    scene 39-1 meeting 9 with Dissolve(1)
    a "Wow. That is a bit of a situation."
    if dianaGoodRelations == False:
        a "Jeremy also hadn't notified me."
        m1 "Yeah, me neither. I don't know."
    scene 39-1 meeting 10 with Dissolve(1)
    a "Huh... Well."
    a "What's it about?"
    m1 "Quarterly."
    a "Ok..."
    a "Umm... Well, we have to get ontop of the situation."
    if dianaGoodRelations == False:
        a "Where is Jeremy?"
        m1 "No where to be found..."
        a "Of course."
    scene 39-1 meeting 12-1 with Dissolve(1)
    e "Hey... Hey..."
    e "It's all good."
    scene 39-1 meeting 12 with Dissolve(1)
    e "Let's get some lunch afterward, you can tell me about it."
    e "Right now, we've got to get the make the presentation."
    e "I will take care of the internals."
    scene 39-1 meeting 11-1 with Dissolve(1)
    a "Emily... You are a gem."
    e "Well, it's nothing Haha."
    scene 39-1 meeting 11 with Dissolve(1)
    a "Yeah, let's get lunch later. Thanks again!"
    scene 39-1 meeting 14 with Dissolve(1)
    a "So, What else do we need."
    m1 "We need quarterly results, basically."
    m1 "I will work on business partners and everything else with Emily and we'll create it."
    scene 39-1 meeting 15 with Dissolve(1)
    a "Great. I Will make the presentation, then."
    a "Let's get it done... Eh..."
    scene black with Dissolve(1)
    play sound door2
    scene 31-3 jeremy 19 with Dissolve(1)
    a "So... I've got all of this info to take care of."
    "Anna was going through the documents and murmuring under her breath."
    a "Client satisfaction, income... generated profit..."
    a "gross income..."
    jump EP11_Work_6
screen EP11_Document_CheckList:
    frame:
        xalign 1.0
        xsize 763
        ysize 1080
        background "#FFF"
        has vbox
        spacing 50
        xfill True
        text "Quarterly Check List" color "#000" bold True size 40 xalign 0.5
        vbox:
            xfill True
            spacing 20
            for i in range(len(EP11_meeting_questions_bool)):
                if EP11_meeting_questions_bool[i] == True:
                    text "{image=images/icons/check-mark.png}" + EP11_meeting_quesitons[i] color "#000" xalign 0.5
                else:
                    text "{image=images/icons/cross.png}" + EP11_meeting_quesitons[i] color "#000" xalign 0.5

        if EP11_meeting_doc_var_1 == True:
            text "Votes:" color "#000" bold True size 40 xalign 0.5
            vbox:
                xfill True
                spacing 20
                hbox:
                    xalign 0.5
                    spacing 20
                    if EP11_meeting_questions_var_1 == 1:
                        text "{image=images/icons/check-mark.png}" + "Employee salaries" color "#000"
                        text "{image=images/icons/cross.png}" + "Partner salaries" color "#000"
                    if EP11_meeting_questions_var_1 == 2:
                        text "{image=images/icons/cross.png}" + "Employee salaries" color "#000"
                        text "{image=images/icons/check-mark.png}" + "Partner salaries" color "#000"
                hbox:
                    xalign 0.5
                    spacing 20
                    if EP11_meeting_questions_var_2 == 1:
                        text "{image=images/icons/check-mark.png}" + "Donate to a Charity" color "#000"
                        text "{image=images/icons/cross.png}" + "Raise Partner benefits" color "#000"
                    if EP11_meeting_questions_var_2 == 2:
                        text "{image=images/icons/cross.png}" + "Donate to a Charity" color "#000"
                        text "{image=images/icons/check-mark.png}" + "Raise Partner benefits" color "#000"

        if EP11_meeting_doc_var_2 == True:
            text "Targets:" color "#000" bold True size 40 xalign 0.5
            vbox:
                xfill True
                spacing 20
                for i in range(len(EP11_meeting_questions_1)):
                    text "{image=images/icons/check-mark.png}" + EP11_meeting_questions_1[i] color "#000" text_align 0.5 xalign 0.5

label EP11_Work_6:
    show screen EP11_Document_CheckList with Dissolve(1)
    menu:
        "Expansion to the Middle Eastern sector.":
            a "We did that."
            $ EP11_meeting_questions_bool.append(True)
            $ EP11_meeting_quesitons.append("Expansion to the Middle Eastern sector.")
    show screen EP11_Document_CheckList with Dissolve(1)
    pause
    menu:
        "Shingzhou contract closed.":
            if office_var_two == False:
                a "I closed it. Nice."
                $ EP11_meeting_questions_bool.append(True)
                $ EP11_meeting_quesitons.append("Shingzhou Contract closed.")
            else:
                a "I refused to do the dirty things..."
                $ EP11_meeting_questions_bool.append(False)
                $ EP11_meeting_quesitons.append("Shingzhou Contract closed.")
    show screen EP11_Document_CheckList with Dissolve(1)
    pause
    menu:
        "Contract closed with BBD Inc.":
            a "Haven't done it yet, didn't know it was a target for this quarter."
            $ EP11_meeting_questions_bool.append(False)
            $ EP11_meeting_quesitons.append("BBD Inc Contract Closed.")

    show screen EP11_Document_CheckList with Dissolve(1)
    pause
    menu:
        "Income goal reached.":
            a "With me closing deals, we are definitely in the green."
            $ EP11_meeting_questions_bool.append(True)
            $ EP11_meeting_quesitons.append("Income goal reached.")
    show screen EP11_Document_CheckList with Dissolve(1)
    pause
    a "What's next."
    $ EP11_meeting_doc_var_1 = True
    show screen EP11_Document_CheckList with Dissolve(1)
    pause
    menu:
        "Increase partner salaries or Employee salaries"
        "Employee salaries":
            $ EP11_meeting_questions_var_1 = 1
        "Increase partner salaries":
            $ EP11_meeting_questions_var_1 = 2
    show screen EP11_Document_CheckList with Dissolve(1)
    pause
    menu:
        "Raise Partner benefits or donate to a charity."
        "Donate to a Charity.":
            $ EP11_meeting_questions_var_2 = 1
        "Raise Partner benefits.":
            $ EP11_meeting_questions_var_2 = 2
    show screen EP11_Document_CheckList with Dissolve(1)
    pause
    a "This is how it should be."
    a "Let's see... Targets."
    $ EP11_meeting_doc_var_2 = True
    show screen EP11_Document_CheckList with Dissolve(1)
    a "Definitely gotta close BBD Inc."
    a "My bonuses will rely upon that."
    $ EP11_meeting_questions_1.append("Make BBD Inc a Client.")
    show screen EP11_Document_CheckList with Dissolve(1)
    pause
    menu:
        "Expand influence in the Sun City, find new clients here.":
            $ EP11_meeting_questions_var_3 = 1
            $ EP11_meeting_questions_1.append("Expand influence, gain new clients in the Sun City.")
        "Find new clients from abroad, expand international influence.":
            $ EP11_meeting_questions_var_3 = 2
            $ EP11_meeting_questions_1.append("Find new clients from abroad, Expand international influence.")

    show screen EP11_Document_CheckList with Dissolve(1)
    pause
    menu:
        "Create a Real Estate department, Buy up land in Sun City.":
            $ EP11_meeting_questions_var_4 = 1
            $ EP11_meeting_questions_1.append("Create a Real Estate department, Invest in Sun City property")
        "Create an AI research department, Invest in High-grade computing power.":
            $ EP11_meeting_questions_var_4 = 2
            $ EP11_meeting_questions_1.append("AI Research Department, Invest in High-grade computing power")
    show screen EP11_Document_CheckList with Dissolve(1)
    pause
    scene generic office 2 with Dissolve(1)
    a "Damn. I've had to make some big choices."
    a "I think these look good."
    a "I should go to Madison and check up on her progress."
    $ pinkoutfit = False
    $ red_outfit = False
    $ EP11_var_5 = True
    hide screen EP11_Document_CheckList with Dissolve(1)
    scene black with Dissolve(1)
label EP11_Work_7:
    scene black with Dissolve(1)
    play sound high_heels_walking
    scene 31-3 jeremy 11 with Dissolve(1)
    a "Hey, Madison. I've done all on my side, you ready?"
    m1 "Yes, Anna. We are ready for the meeting."
    a "Great."
    scene 31-3 jeremy 18 with Dissolve(1)
    a "Had any trouble with info?"
    m1 "Not really. I've got my own way of archiving info, I keep everything ready and nearby."
    a "That's great. I knew you were the right choice for this job."
    m1 "Awww... Thanks. Hah."
    a "Ok, shall we?"
    m1 "Mhm."
    stop music fadeout 1.2
    scene black with Dissolve(1)
    play sound door2
    queue music (chill_song_2, chill_song_3) fadein 0.5 loop
    scene 39-1 meeting 16 with Dissolve(1)
    a "So... This is us, huh."
    m1 "Yeah. The meeting won't start for another 20 or so minutes."
    scene 39-1 meeting 17 with Dissolve(1)
    a "Perfect. Enough time for us to set up."
    a "You've been a real help, Madison."
    m1 "Thanks, Hah. Just doing my job."
    scene 39-1 meeting 18 with Dissolve(1)
    a "Doing it perfectly."
    a "I mean, I didn't even know about the meeting a couple of hours ago."
    a "You saved my ass, kind of."
    m1 "Alright, I'll go prepare everything."
    scene 39-1 meeting 19 with Dissolve(1)
    "Anna was a little nervous. She had to come up with this all on such short notice..."
    "Will it be enough, though?"
    play sound door2
    scene 39-1 meeting 20 with Dissolve(1)
    e1 "Anna!"
    e1 "How are you?"
    play sound woman_hmm_1
    a "Well, As good as one can be."
    e1 "Are you ready?"
    a "Yeah, but it would've been better if I had gotten a bit of a heads up."
    e1 "Sorry?"
    scene 39-1 meeting 21 with Dissolve(1)
    a "Well, I just found out about the meeting today."
    e1 "What?"
    e1 "Oh, well... It's... I think I might've made a mistake there..."
    play sound woman_reaction_mhm_1
    scene 39-1 meeting 22 with Dissolve(1)
    a "Eh... We're fine, managed to get everything set up."
    e1 "I'm sure I sent out the memo a couple of weeks ago."
    a "A couple of weeks is a long time."
    a "Besides..."
    if dianaGoodRelations == True:
        a "I haven't been a partner for that long."
        menu:
            "Anna choses to be more dominant and scold Ethan.":
                $ dom_var +=1
                a "And I'd expect, in the future, for you to keep me in the loop."
                a "Things are going to start changing around here a lot more, now that I'm a partner."
                e1 "Yes, Anna... Sorry."
            "Anna chooses to refrain from any conflict.":
                a "But, ok."
                a "It's done. Let's move on."
    else:
        a "I haven't been department head for that long."
    e1 "Right..."
    scene 39-1 meeting 23 with Dissolve(1)
    a "Anyway, I think we are as ready as we'll ever be."
    scene 39-1 meeting 24 with Dissolve(1)
    e1 "It's mostly a formality, an informational event."
    if dianaGoodRelations == True:
        e1 "The board members also want to meet the newest partner."
    play sound woman_reaction_mhm_1
    a "I see."
    play sound jacketcloth
    scene 39-1 meeting 25 with Dissolve(1)
    e1 "We all ready?"
    m1 "Yes, sir. Copies have been distributed."
    m1 "Presentation set up."
    scene 39-1 meeting 26 with Dissolve(1)
    a "Great."
    e1 "An efficient team, I like it."
    scene 39-1 meeting 27 with Dissolve(1)
    pause 1
    play sound notification
    scene 39-1 meeting 28 with Dissolve(1)
    pause 1
    scene 39-1 meeting 29 with Dissolve(1)
    a "Alright, everything seems to be working."
    m1 "I asked Timothy to come in beforehand and make sure the system worked, was up to date, etc."
    a "Nice thinking."
    scene 39-1 meeting 30 with Dissolve(1)
    d "Excuse me, Mr. Tadayaki has arrived."
    e1 "Come in, Come in, Namura."
    scene 39-1 meeting 31 with Dissolve(1)
    mta "It is an honor, Miss Anna."
    mta "I've heard many great things about you."
    "Anna hadn't met any of the board members, yet..."
    scene 39-1 meeting 32 with Dissolve(1)
    a "Um... Like wise, sir."
    a "You've been a very wise investor in this company."
    scene 39-1 meeting 33 with Dissolve(1)
    a "I hope I can prove to you today, that these investments are well worth it."
    mta "Indeed."
    scene 39-1 meeting 34 with Dissolve(1)
    if dianaGoodRelations == False:
        a "Do you know where Jeremy is?"
        d "No..."
        "Anna leaned in..."
        menu:
            "I thought you were his personal whore.":
                a "You'd know."
                d "You and I both know, you are his whore."
                a "Get out of here..."
            "He's just gone.":
                d "Good for us..."
                a "Oh. hey... You're right."
                "For a moment both women were sincere."
    else:
        d "The rest of the members will arrive shortly."
        a "Thanks, Diane. Appreciated."
        scene 39-1 meeting 35 with Dissolve(1)
        d "I got you, Anna."
        a "Good luck."
    play sound door2
    scene 39-1 meeting 36 with Dissolve(1)
    a "And there they are."
    if escort_industry_var == True:
        "Anna froze for a second..."
        a "Whaa..."
        "It was the man, she went to as an escort."
        a "{i}...This is not good..."
        a "{i}...He will definitely recognize me."
    mb1 "And so we bought out the company for pennies on the dollar."
    th "Hah... As expected. They deserved it, trying to leverage against you."
    scene 39-1 meeting 37 with Dissolve(1)
    th "Ah... The main attraction. I'm Turna Hoeburn. I bought the previous board members, Mr. Gelders shares."
    a "I see. Great, This meeting will be just the thing to bring you up to speed."
    th "I hope so. If you are as smart as you are visually appealing, this will go along nicely."
    scene 39-1 meeting 38 with Dissolve(1)
    a "Khem... Yeah."
    scene 39-1 meeting 39 with Dissolve(1)
    mb1 "Greetings, Anna."
    th "You two know each other?"
    mb1 "I surely know who are the partners of the company."
    th "Fair enough."
    mb1 "Are we ready?"
    scene 39-1 meeting 40 with Dissolve(1)
    if escort_industry_var == True:
        a "{i}...Perhaps he forgot? Hopefully..."
    a "Yeah. You can all take seats, and we can get this meeting underway."
    scene 39-1 meeting 41 with Dissolve(1)
    a "Is there anything you'd like? Water, coffee?"
    mb1 "We'll be fine. Thanks."
    scene 39-1 meeting 42 with Dissolve(1)
    if dianaGoodRelations == True:
        a "Thanks, Diane."
        d "If you need anything, let me know."
    else:
        a "You can go now."
        d "..."
    scene 39-1 meeting 43 with Dissolve(1)
    a "Alright..."
    a "So, once again for everyone. I'm Anna."
    if dianaGoodRelations == True:
        a "I'm the newest partner at the company."
        a "After Jeremy's... situation..."
        a "And I'd like to make a statement."
        menu:
            "Ethan and I, as partners, want to make this company as profitable, successful, and long-lasting as possible.":
                a "So for the quarterly report, we have made some new targets."
                a "Certain internal policies will also be updated."
                a "As well as we're actively looking for new clients for the company."
            "I personally want to make this company as profitable as possible.":
                a "And I have made some new targets."
                a "Certain internal policies will also be updated."
                a "As well as I'm actively looking for new clients for the company."
    else:
        a "Jeremy couldn't be here for external reasons... So I'm pitching it as department head."
        a "And so, with the help of the partners, Liam, Ethan, Jeremy, we've come up with some new targets for the quarterly, as well."
    scene 39-1 meeting 44 with Dissolve(1)
    a "With the help of Madison, our newest assistant, we've compiled the documents."
    a "You can take a look at the details in your copies."
    scene 39-1 meeting 46 with Dissolve(1)
    th "Yeah, um... Question!"
    a "Yes, Mrs. Hoeburn?"
    th "I see, from the looks of it, that BBD Inc angle hasn't been covered, yet?"
    th "Do explain."
    menu:
        "Anna was honest.":
            $ EP11_meeting_alignment += 1
            scene 39-1 meeting 45 with Dissolve(1)
            a "To be honest, I haven't been a partner that long, so certain things missed my ear."
            a "I only sent them an email today."
            a "I will keep you all in the loop, personally."
            a "I am, however, very certain we will give them a great deal."
            scene 39-1 meeting 46 with Dissolve(1)
            th "Very well, don't keep us waiting."
            th "It was, after all, a goal for the quarterly."
        "Anna was defensive and lied.":
            scene 39-1 meeting 45 with Dissolve(1)
            $ EP11_meeting_alignment -= 1
            a "Well, there is development, nothing solid yet."
            a "We will keep you in the loop with further news."
            scene 39-1 meeting 46 with Dissolve(1)
            th "Sounds like empty excuses."
            th "It was after all, a goal for the quarterly."
    scene 39-1 meeting 45 with Dissolve(1)
    a "That's correct, however, the graph shows a different picture."
    a "Our profits have reached AND exceeded the targets."
    scene 39-1 meeting 47 with Dissolve(1)
    a "In the graph you can see the distribution of funds amongst investments that we've made this quarter."
    a "All of which were a part of the quarterly target's agenda."
    a "We have also added, as clients, the East Oil Conglomerate."
    a "Which might become our most profitable client, as they plan to expand their operation."
    scene 39-1 meeting 48 with Dissolve(1)
    a "Also, I'm speculating here of course, but that potentially opens doors to other companies from the Middle East."
    if office_var_two == False:
        $ EP11_meeting_alignment +=1
        a "We've also helped Shingzhou Corp with the merger and have gained them as our biggest clients."
        a "So for the quarterly goals, we have reached most, and in terms of revenue, exceeded the goals."
        a "I'd say that's a win."
        scene 39-1 meeting 49 with Dissolve(1)
        mta "Miss Anna?"
        scene 39-1 meeting 50 with Dissolve(1)
        mta "I would like to understand how well has Shingzhou Corps merger affected their advances?"
        mta "That was, after all, one of the main goals of the quarter."
        scene 39-1 meeting 51 with Dissolve(1)
        a "Yes... So. On to the next slide."
        scene 39-1 meeting 52 with Dissolve(1)
        a "Their profit hasn't simply doubled."
        a "They have tripled."
        a "And we as the service company get an increased workload, which directly impacts our income."
    else:
        $ EP11_meeting_alignment -=1
        a "Unfortunately, we were unable to close Shingzhou Corp, which has, potentially cut into future profits."
        a "There were some problems that couldn't be resolved."
        a "However, EOC and BBD Inc, which I'm sure I will close, both will make up for the shortcomings."
        a "Also, we will try once more in the future, because, as far as I understand, they still haven't come up with a better company to provide services."
        scene 39-1 meeting 49 with Dissolve(1)
        mta "Miss Anna?"
        mta "This is unacceptable!"
        scene 39-1 meeting 50 with Dissolve(1)
        mta "I would like to understand how well has Shingzhou Corps merger affected their advances?"
        mta "That was, after all one of the main goals of the quarter."
        scene 39-1 meeting 51 with Dissolve(1)
        a "Yes... So. On to the next slide."
        scene 39-1 meeting 52 with Dissolve(1)
        a "Their profits haven't simply doubled."
        a "They have tripled."
        a "But, like I said, I'm confident if we approach them once more, we will find a compromise."
        mta "Due to this news, Ethan, you will have to take over Shingzhou. I only trust you with this."
        e1 "Will do."
    a "Regarding the vote."
    scene 39-1 meeting 53 with Dissolve(1)
    if EP11_meeting_questions_var_1 == 1:
        a "I've voted to increase Employee salaries."
    if EP11_meeting_questions_var_1 == 2:
        a "I've voted to increase partner salaries as a by-product of our success."
    a "As well as..."
    if EP11_meeting_questions_var_2 == 1:
        a "Donate to a charity fund."
    if EP11_meeting_questions_var_2 == 2:
        a "Increase partner benefits."
    a "You will, of course, have the final say."
    scene 39-1 meeting 54 with Dissolve(1)
    a "For targets we have..."
    if EP11_meeting_questions_var_3 == 1:
        a "A plan to expand the influence and gain clients locally, Sun City, etc."
    if EP11_meeting_questions_var_3 == 2:
        a "A plan to expand in an international context and gain influence and clients as such."
    a "As well as..."
    if EP11_meeting_questions_var_4 == 1:
        a "I propose that we create a new department that deals with Real Estate."
    if EP11_meeting_questions_var_4 == 2:
        a "I propose to create a new AI research department that would further the ever-advancing neural networks etc. As well as investing our money into high-grade servers and computers as a foundation for this field."
    scene 39-1 meeting 55 with Dissolve(1)
    if EP11_meeting_alignment > 0:
        mb1 "Well, well..."
        mb1 "I accept the vote as well as the targets!"
        mb1 "You've outdone yourself, Anna."
        if dianaGoodRelations == True:
            mb1 "As a new partner, very impressive."
        scene 39-1 meeting 56 with Dissolve(1)
        mb1 "If this meeting has shown me anything, we can trust in the leadership of this company."
        mb1 "I also believe, bonuses are in order."
        mb1 "We'll have the accounting push that through. Good job."
    if EP11_meeting_alignment < 0:
        mb1 "Well... Looks like there have been some hiccups."
        mb1 "I accept the vote and the targets, however, we will have to have a deeper look at the failures of this quarter."
        mb1 "For now, I'd say, as a new partner, it's understandable, however, this cannot reoccur."
        scene 39-1 meeting 56 with Dissolve(1)
        mb1 "If this meeting has shown me anything, we will have to keep a closer eye on things, but for now, everything seems stable."
    if EP11_meeting_alignment == 0:
        mb1 "For now, things are fine."
        mb1 "I accept the vote as well as the targets."
    a "Thank you, sir."
    scene 39-1 meeting 57 with Dissolve(1)
    if EP11_meeting_alignment > 0:
        th "While I keep a higher level of scrutiny towards these things, I have to agree with Mr. Burnsfield on this."
        th "He knows what he's doing."
        th "So for now, you have my vote of confidence, too."
        scene 39-1 meeting 58 with Dissolve(1)
        mta "Yes... You have mine as well, but. I will keep a close eye on the developments."
        mta "We are moving into uncertain times and thus investments have to be meticulous and pragmatic."
        mta "Not wild and impulsive."
        a "Of course. I will do my best to not let you down."
    if EP11_meeting_alignment < 0:
        th "I do not like how you've handled certain aspects of the company..."
        th "So I will also keep a closer eye on you for the time being, and if things deteriorate, I will call for a vote to remove you."
        th "So do not screw things up anymore."
        a "Yes, ma'am."
        scene 39-1 meeting 59 with Dissolve(1)
        mta "I don't have any comments at this time..."
        mta "I will be in contact... Certain things have to be changed here..."
        mta "Hopefully, you do not make anymore mistakes..."
        a "I won't, sir."
    if EP11_meeting_alignment == 0:
        th "While I keep a higher level of scrutiny towards these things, I have to agree with Mr. Burnsfield on this."
        th "He knows what he's doing."
        th "So for now, you have my vote of confidence, too."
        scene 39-1 meeting 58 with Dissolve(1)
        mta "Yes... You have mine as well, but. I will keep a close eye on the developments."
        mta "We are moving into uncertain times and thus investments have to be meticulous and pragmatic."
        mta "Not wild and impulsive."
        a "Of course. I will do my best to not let you down."
    if office_var_two == True:
        scene 39-1 meeting 59 with Dissolve(1)
        mta "See that you do. Shingzhou was one of the most important deals in recent history."
        mta "Luckily we can still save it."
    scene 39-1 meeting 60 with Dissolve(1)
    if EP11_meeting_alignment > 0:
        "Anna just kept the smile..."
    a "Since I've covered everything... We are adjourned."
    "The meeting had come to an end, members were leaving... Anna felt a wave of relief wash over her."
    scene 39-1 meeting 61 with Dissolve(1)
    mb1 "You are very good at this, I'll tell you this much."
    mb1 "But you do have plenty to prove still..."
    scene 39-1 meeting 62 with Dissolve(1)
    if escort_industry_var == True:
        mb1 "And... I do remember you, Anna."
        a "Oh..."
        mb1 "I just didn't bring it up to keep things professional."
        scene 39-1 meeting 64 with Dissolve(1)
        a "But, it's not what it looks like..."
        scene 39-1 meeting 61 with Dissolve(1)
        mb1 "Don't worry, your secret is safe with me."
        mb1 "From my perspective, it won't change anything."
        scene 39-1 meeting 63 with Dissolve(1)
        a "Oh, hah... Thanks, sir..."
        mb1 "That being said, I look forward to the next time we meet. Heh."
        a "Me too..."
        scene 39-1 meeting 65 with Dissolve(1)
        pause 1.5
        scene 39-1 meeting 66 with Dissolve(1)
        th "Wait... So you do know about her?"
        mb1 "No idea what you're talking about..."
        th "What about our arrangement?"
        scene 39-1 meeting 67 with Dissolve(1)
        mb1 "Don't you worry about it."
    else:
        mb1 "Keep at it. I know a dedicated person when I see one."
        a "Thank you, sir..."
        mb1 "Good luck and keep us posted."
    scene 39-1 meeting 68 with Dissolve(1)
    e1 "Well... that's over."
    e1 "I don't like these meetings."
    e1 "I like sitting on the balcony of my beach house and drinking mojitos."
    a "Hah, I'd like that, too."
    m1 "Me three."
    scene 39-1 meeting 69 with Dissolve(1)
    a "So you'd say we nailed it?"
    e1 "They were all pretty impressed."
    if office_var_two == True:
        e1 "Besides Shingzhou..."
        e1 "But I will fix that."
    scene 39-1 meeting 70 with Dissolve(1)
    m1 "You did great, Anna."
    a "Whew... I'm tired."
    scene 39-1 meeting 68 with Dissolve(1)
    e1 "Keep this up, and you'll be able to afford a beach house in no time."
    a "I look forward to that."
    $ EP11_var_6 = True
    jump EP11_Lunch
label EP11_Lunch:
    play sound high_heels_walking
    scene black with Dissolve(1)
    $ EP11_var_7 = True
    scene 39-2 lunch 1 with Dissolve(1)
    a "Emily!"
    a "Ah. I'm done with the meeting."
    a "Quite stressful, that was."
    scene 39-2 lunch 2 with Dissolve(1)
    a "You ready for lunch?"
    e "Sure am!"
    play sound walk
    play ambience citytraffic
    scene black with Dissolve(1)
    scene 39-2 lunch 3 with Dissolve(1)
    a "I am rather hungry, to be honest."
    a "That meeting took a lot. Haha!"
    e "Tell me about it. I could just feel the energy emanating from that area of the building."
    a "Haha."
    scene 39-2 lunch 4 with Dissolve(1)
    pause 1.5
    play sound door2
    scene black with Dissolve(1)
    pause 1
    stop ambience
    scene 39-2 lunch 5 with Dissolve(1)
    barista "Hello, What would you like to order?"
    a "I'll have a latte..."
    e "The same for me."
    a "And what kind of cakes do you have today?"
    barista "We just got a new batch of Emerald Grove bakery."
    a "No way. Those are some nasty good cakes."
    scene 39-2 lunch 6 with Dissolve(1)
    barista "Indeed."
    barista "We have a full choclate cake."
    barista "Apple cake."
    barista "Orange/lime cake."
    a "I'll have aslice of the full chocolate."
    e "An apple cake for me."
    barista "Coming right up."
    scene black with Dissolve(1)
    play sound jacketcloth
    pause 0.5
    scene 39-2 lunch 7 with Dissolve(1)
    e "So, tell me about the meeting."
    a "Well..."
    a "And what else you've got on mind today?"
    $ EP11_Lunch_menu_var_1 = False
    $ EP11_Lunch_menu_var_2 = False
    if escort_industry_var == False:
        $ EP11_Lunch_menu_var_2 = True
    $ EP11_Lunch_menu_var_3 = False
    menu EP11_Lunch_menu:
        "I finally saw all the board members." if EP11_Lunch_menu_var_1 == False:
            $ EP11_Lunch_menu_var_1 = True
            scene 39-2 lunch 8 with Dissolve(1)
            a "There was Namura Tadayaki. A Japanese investor seemed a very traditional man."
            a "Turna Hoeburn. She's a stickler for 'by the book' stuff. I mean, she was on my ass mostly."
            a "Gordon Burnsfield. A laid-back man. A very attractive, older man. Between 45-50 No doubt."
            scene 39-2 lunch 7 with Dissolve(1)
            a "Each of them had a different angle, but at the end of the day, Mr. Burnsfield is pulling the most strings."
            a "I think he actually has the most shares."
            jump EP11_Lunch_menu
        "Anna had some gossip about Mr. Burnsfield" if escort_industry_var == True and EP11_Lunch_menu_var_1 == True and EP11_Lunch_menu_var_2 == False:
            $ EP11_Lunch_menu_var_2 = True
            scene 39-2 lunch 8 with Dissolve(1)
            a "So basically, if you must know."
            e "Oh I know this will be good."
            a "Mr. Burnsfield, the main investor? I've seen him before."
            scene 39-2 lunch 9 with Dissolve(1)
            e "Do tell?"
            a "I went to him as an... Escort..."
            a "As a job through Dylan."
            scene 39-2 lunch 10 with Dissolve(1)
            e "Bullshit..."
            a "Dead serious."
            e "You crazy girl, haha!"
            e "And?"
            scene 39-2 lunch 8 with Dissolve(1)
            a "Well, I might go to him again, strictly professional."
            e "Oh, right! strictly on-the-knees-professional. Haha."
            a "But it pays, plus he seemed charming."
            jump EP11_Lunch_menu
        "I'm going to a fashion show today." if EP11_Lunch_menu_var_3 == False:
            $ EP11_Lunch_menu_var_3 = True
            scene 39-2 lunch 9 with Dissolve(1)
            e "Wait, just to watch?"
            scene 39-2 lunch 8 with Dissolve(1)
            a "No, no, no. I'm going to the Runway."
            a "Alfred got some sort of rare piece of clothing."
            a "Wants me to wear it."
            e "So, my Anna will finally get a real crack at the model career?"
            scene 39-2 lunch 7 with Dissolve(1)
            a "I'm very excited."
            jump EP11_Lunch_menu
        "That's all." if EP11_Lunch_menu_var_3 == True and EP11_Lunch_menu_var_1 == True and EP11_Lunch_menu_var_2 == True:
            pass
    scene 39-2 lunch 11 with Dissolve(1)
    a "Well, I'm all done with the cake."
    a "Didn't even notice how I finished it, haha."
    e "Me neither, it went down so easy."
    scene 39-2 lunch 12 with Dissolve(1)
    e "I need to go to the bathroom, You comin'?"
    a "Sure."
    scene black with Dissolve(1)
    play sound door2
    pause 1
    scene 39-2 lunch 13 with Dissolve(1)
    e "Anyway."
    scene 39-2 lunch 14 with Dissolve(1)
    a "What about you?"
    a "Got some thoughts?"
    scene 39-2 lunch 16 with Dissolve(1)
    e "Actually, yeah."
    e "You going to the bar on Friday, right?"
    a "Sure am."
    if bar_var_1 == False:
        a "We'll be opening the bar this friday."
        a "Since the unfortunate accident."
        e "That was very scary."
        e "I feel like we're kind of to blame."
        a "No, we're not..."
        a "Just forget about it."
    scene 39-2 lunch 17 with Dissolve(1)
    e "I'm really looking forward to having more fun there."
    a "I'm pretty sure things will get even crazier."
    e "That's what I like to hear."
    scene 39-2 lunch 18 with Dissolve(1)
    pause 1
    play sound undress
    scene 39-2 lunch 19 with Dissolve(1)
    pause 1
    scene 39-2 lunch 20 with Dissolve(1)
    pause 1
    scene 39-2 lunch 21 with Dissolve(1)
    if bar_var_1 == False:
        e "Wait, what exactly is going to happen now, that Patrick's out of the picture?"
        scene 39-2 lunch 22 with Dissolve(1)
        a "Well, Jim and I are taking over, kind of. I will follow his lead for now."
        a "But I'm kind of becoming the leader of it."
    else:
        e "So Patrick's still in charge?"
        scene 39-2 lunch 22 with Dissolve(1)
        a "Yeah. He's not the nicest boss, but things work under him."
        e "Shouldn't take it."
        a "It's not really that bad."
    e "How are you and Timothy doing, eh?"
    a "Hah. You are never satiated."
    scene 39-2 lunch 23 with Dissolve(1)
    a "I haven't done much with him lately."
    a "Went to him. We made pizza..."
    if timothySexContent == True:
        a "Oh wait... We umm, had sex there."
        e "HAHA! Of course..."
    scene 39-2 lunch 24 with Dissolve(1)
    e "You've got men lining up like crazy."
    e "How do you do it?"
    a "Me?"
    scene 39-2 lunch 25 with Dissolve(1)
    a "You are keeping busy yourself, don't say you don't..."
    a "You little minx."
    e "Hehe... Fair enough."
    a "Alright, let's go."
    a "I've got to prepare for the fashion show."
    scene black with Dissolve(1)
    jump EP11_Alfred_House
label EP11_Earl_Hotel:
    play music chill_song_4 fadein 2
    scene 39-4 earl 1 with Dissolve(1)
    a "Well, well... I hope that this will be enough to put this all behind me..."
    a "It does seem a bit strange..."
    a "How he made me come here..."
    a "But... The choice has been made..."
    scene 39-4 earl 2 with Dissolve(1)
    a "This seems..."
    a "Simple, But what did I expect."
    scene 39-4 earl 3 with Dissolve(1)
    a "Eh..."
    scene 39-4 earl 4 with Dissolve(1)
    a "This mess has been dragging on for so long."
    a "Alright... Alright."
    scene 39-4 earl 5 with Dissolve(1)
    a "I guess if I'm going to stay the night here..."
    a "Might get a shower."
    play sound door2
    scene 39-4 earl 6 with Dissolve(1)
    pause 1
    scene black with Dissolve(1)
    play sound jacketcloth
    scene 39-4 earl 7 with Dissolve(1)
    pause 1
    play sound shower_sound
    scene 39-4 earl 8 with Dissolve(1)
    a "..."
    play audio woman_sigh_1
    pause 1.5
    scene 39-4 earl 9 with Dissolve(1)
    pause 1
    scene 39-4 earl 10 with Dissolve(1)
    pause 1.5
    scene 39-4 earl 11 with Dissolve(1)
    pause 1.5
    stop sound fadeout 1
    scene black with Dissolve(1)
    pause 1
    scene 39-4 earl 12 with Dissolve(1)
    a "That's better..."
    a "A shower always helps..."
    play sound cloth_sound1
    scene 39-4 earl 13 with Dissolve(1)
    pause 1.5
    play sound undress
    scene 39-4 earl 14 with Dissolve(1)
    pause 2
    scene black with Dissolve(1)
    "..."
    pause 1
    play music tense2
    play sound surprise2
    scene 39-4 earl 15 with vpunch
    a "Huh?"
    play sound man_evil_laugh_1
    scene 39-4 earl 15-1 with Dissolve(1)
    pause 2
    scene 39-4 earl 16 with Dissolve(1)
    earl "Took your time in the shower?"
    a "I'm sorry... This is inappropriate."
    earl "Bah. Not really."
    scene 39-4 earl 17 with Dissolve(1)
    earl "I just came around to make sure you're settling in okay for the night?"
    a "I mean..."
    "Anna was shocked..."
    a "I am, but... Could you have made it any less obvious that you'd come?"
    scene 39-4 earl 18 with Dissolve(1)
    "Anna turned around, she felt his eyes piercing her."
    a "Next time, please knock!"
    earl "Next time?"
    a "I mean, there won't be one, but in case."
    earl "I will do my best to remember that."
    scene 39-4 earl 19 with Dissolve(1)
    earl "You know, I brought a bottle of something good."
    earl "To... Celebrate our victory."
    scene 39-4 earl 20 with Dissolve(1)
    a "Your victory."
    earl "Nonsense. We both did our part. You will be much better off, trust me."
    a "I just want to put it all behind me."
    play sound pourwater
    scene 39-4 earl 21 with Dissolve(1)
    earl "You will. Don't worry about that."
    earl "For Carl and Sergey thing's are just beginning..."
    a "Carl, too?"
    e "He's a serious accomplice, you know?"
    scene 39-4 earl 22 with Dissolve(1)
    earl "Here, this should help you relax."
    scene 39-4 earl 23 with Dissolve(1)
    a "Yeah... I need a drink..."
    "Anna was letting her guard down a bit."
    scene 39-4 earl 24 with Dissolve(1)
    a "But... He's, he's important to Rebecca."
    earl "And that means what exactly?"
    earl "You know I've done a great deal already to keep you out of it."
    play sound drinkingBeverage
    scene 39-4 earl 25 with Dissolve(1)
    "Anna chug the bourbon."
    scene 39-4 earl 25-1 with Dissolve(1)
    earl "{i}...Yeah, just like that..."
    scene 39-4 earl 26 with Dissolve(1)
    a "Is there nothing that can be done?"
    earl "Well..."
    earl "There might be..."
    a "Name your price..."
    play sound pourwater
    scene 39-4 earl 27 with Dissolve(1)
    earl "That isn't as simple..."
    earl "I think... You might know what it is that I want..."
    "Anna was thinking hard..."
    a "{i}...Does he..."
    play sound drinkingBeverage
    scene 39-4 earl 28 with Dissolve(1)
    pause 1
    scene 39-4 earl 29 with Dissolve(1)
    earl "If you 'persuade' me, I might help Carl's situation..."
    "Did Anna really want to get Carl out of there that much?"
    menu:
        "Alright, what's your game?":
            $ EP11_var_Earl_Sex = True
            $ persistent.scene_34 = True
            earl "Hehe..."
            jump EP11_Earl_Hotel_Sex
        "I'm not going to fall for your bullshit.":
            scene 39-4 earl 138 with Dissolve(1)
            a "I put up with you enough!"
            a "I'm not going sell my body to you!"
            a "Unless you have a better idea, you can get the fuck out of here and catch the bad guys!"
            scene 39-4 earl 139 with Dissolve(1)
            earl "Whoa... I was just..."
            "For a moment Anna's answer put Earl into a shock."
            "He didn't expect her to shoot back at him like that."
            earl "I was just messing around."
            a "GET OUT!"
            scene 39-4 earl 140 with Dissolve(1)
            earl "Alright, alright."
            earl "You ain't getting Carl out then."
            earl "Deal with it."
            a "Enough. GO!"
            scene 39-4 earl 141 with Dissolve(1)
            "Anna stood up for herself."
            "She felt a breath of relief."
            "Didn't hold in her anger any longer."
            scene black with Dissolve(1)
            play sound jacketcloth
            scene 39-4 earl 135 with Dissolve(1)
            a "I just hope he catches the bad guy who's after me..."
            a "If there even is one..."
            scene black with Dissolve(1)
            $ EP11_var_14 = True
            jump EP11_Episode_End
label EP11_Earl_Hotel_Sex:
    play music SexyTimeSong3
    scene 39-4 earl 30 with Dissolve(1)
    earl "I want to taste you..."
    a "Ah..."
    "Anna felt his cold, stinky breath on her neck..."
    "But she tried to convince herself that Carl was worth it..."
    play sound surprise2
    play audio drinkingBeverage
    scene 39-4 earl 31 with vpunch
    earl "Drink some more, girl..."
    play sound female_cough_1
    pause 1
    play sound drinkingBeverage
    scene 39-4 earl 32 with Dissolve(1)
    "Earl drank some more, too..."
    a "You're so close to me..."
    a "I don't feel... Comf..."
    scene 39-4 earl 32-1 with Dissolve(1)
    earl "Empty... Haha!"
    earl "That's the good shit, you know?"
    earl "I paid a hefty price for the bottle..."
    scene 39-4 earl 33 with Dissolve(1)
    earl "I want to enjoy you, Anna... Been wanting to ever since I found out about you..."
    a "Is there nothing else I can offer you?"
    earl "Besides your sister, no..."
    a "I..."
    earl "If you let me have my way, I will do my best to get what you want."
    scene 39-4 earl 34 with Dissolve(1)
    earl "That's a promise..."
    a "Oah..."
    scene 39-4 earl 36 with Dissolve(1)
    earl "Deal?"
    a "Deal..."
    play sound surprise2
    scene 39-4 earl 36-1 with vpunch
    pause 1
    scene 39-4 earl 36-2 with vpunch
    a "AH..."
    earl "You know you're one piece of sexy ass..."
    a "Don't be too harsh, ok?"
    play sound man_evil_laugh_1
    earl "Hehe..."
    scene 39-4 earl 37 with Dissolve(1)
    earl "You don't need this."
    play sound undress
    scene 39-4 earl 38 with Dissolve(0.2)
    pause 0.5
    scene 39-4 earl 39 with Dissolve(0.2)
    pause 0.5
    scene 39-4 earl 40 with Dissolve(0.2)
    pause 0.5
    play sound item_falls
    scene 39-4 earl 41 with Dissolve(0.2)
    "As the towel fell, it was a sign, that Anna had agreed to Earl's request."
    scene 39-4 earl 42 with Dissolve(0.2)
    earl "This is... Marvelous."
    earl "You've no idea how long I have waited for this."
    play sound licking_1
    scene 39-4 earl 43 with Dissolve(1)
    a "Ah..."
    scene 39-4 earl 44 with Dissolve(1)
    "Anna reacted instinctively."
    earl "Come here..."
    play sound kisspeck
    scene 39-4 earl 45 with Dissolve(1)
    pause 1
    scene 39-4 earl 46 with Dissolve(1)
    earl "Mmmm..."
    "Anna pushed through with motivation that this was worth it."
    scene 39-4 earl 47 with Dissolve(1)
    "But as soon as Earl touched her breasts..."
    "She felt something change..."
    play sound femmoan_2
    a "Ah..."
    scene 39-4 earl 48 with Dissolve(1)
    pause 2
    play sound jerk
    play sound femmoan_3
    scene 39-4 earl 49 with Dissolve(1)
    a "Ah..."
    "And when Earl pressed his fingers around her vagina..."
    "She felt sudden arousal engulf her."
    scene 39-4 earl 50 with Dissolve(1)
    "Anna was once more being taken by her condition..."
    "Starting to lose touch with her inhibitions."
    play sound jerk2
    scene 39-4 earl 51 with Dissolve(1)
    pause 1
    scene 39-4 earl 52 with Dissolve(1)
    pause 1
    play sound female_moan_2
    a "AH..."
    scene 39-4 earl 52-1 with Dissolve(1)
    pause 1.5
    scene 39-4 earl 53 with Dissolve(1)
    earl "Yes... This is perfect..."
    play sound cloth_sound1
    scene 39-4 earl 54 with Dissolve(1)
    earl "There, be a nice girl and sit."
    play sound undress
    scene 39-4 earl 55 with Dissolve(1)
    earl "You know... Heh... I like when women touch my cock."
    earl "I know you'll make it even better."
    scene 39-4 earl 56 with Dissolve(1)
    a "{i}...I... This is... His cock's big..."
    "Anna didn't know what to do with herself. A part of her reasoned as to why she's doing it."
    "Another part of her craved. Something deep and dark inside of her..."
    play sound move_whoosh
    play audio femmoan_4
    scene 39-4 earl 57 with Dissolve(1)
    a "Gentle... Please..."
    earl "Oh come on. I know you like it rough..."
    earl "Rub it."
    scene 39-4 earl 58 with Dissolve(1)
    a "Oh... Ok."
    "Anna hesitantly did as the manipulative Detective asked."
    scene 39-4 earl 59 with Dissolve(1)
    pause 1
    scene 39-4 earl 60 with Dissolve(1)
    earl "How about you..."
    scene 39-4 earl 61 with Dissolve(1)
    earl "Spread those legs."
    earl "My pals won't believe what a chick I landed."
    scene 39-4 earl 62 with Dissolve(1)
    pause 1.5
    scene 39-4 earl 63 with Dissolve(1)
    earl "Lemme just..."
    scene 39-4 earl 64 with Dissolve(1)
    pause 1
    scene 39-4 earl 65 with Dissolve(1)
    a "{i}...What have I gotten myself into..."
    a "{i}...But... It's for Carl...Right?..."
    "Anna wrestled with her own thoughts."
    play sound licking_2
    scene 39-4 earl 66 with Dissolve(1)
    "Earl wasted no time."
    earl "Mmm..."
    play sound female_moan_1
    scene 39-4 earl 67 with Dissolve(1)
    "As soon as Earl's tongue touched Anna's pussy..."
    a "Ah..."
    play sound jerk3
    scene 39-4 earl 68 with Dissolve(1)
    pause 3
    scene 39-4 earl 69 with Dissolve(1)
    pause 3
    scene 39-4 earl 70 with Dissolve(1)
    pause 3
    scene 39-4 earl 70-1 with Dissolve(1)
    "Anna instinctively grabbed his head to push it a bit more."
    "Earl wasn't gentle, though."
    earl "{i}...This is fucking NUTS!..."
    play sound female_moan_3
    scene 39-4 earl 71 with Dissolve(1)
    pause 3
    scene 39-4 earl 72 with Dissolve(1)
    pause 2
    scene 39-4 earl 73 with Dissolve(1)
    pause 1
    scene 39-4 earl 74 with Dissolve(1)
    pause 1
    play sound female_moan_4
    scene 39-4 earl 75 with Dissolve(1)
    a "OH..AHHHH..."
    "As Earls fingers entered Anna, all sense left her."
    scene 39-4 earl 76 with Dissolve(1)
    menu:
        "Put the finger in Anna's asshole?":
            earl "What about that other, beautiful, beautiful hole..."
            scene 39-4 earl 77 with Dissolve(1)
            a "Wait..."
            a "That's... Forbidden..."
            play sound jerk
            scene 39-4 earl 78 with Dissolve(1)
            pause 0.5
            scene 39-4 earl 79 with Dissolve(1)
            pause 2
            scene 39-4 earl 80 with Dissolve(1)
            a "Even Anna's anus was sensitive. with ever slight movement she was thrown back..."
            scene 39-4 earl 81 with Dissolve(1)
        "Don't put The finger in Anna's asshole.":
            pass

    pause 2
    play sound man_evil_laugh_1
    scene 39-4 earl 82 with Dissolve(1)
    earl "Hehe..."
    earl "Yess... That's just right, you like my fingers, eh slut?"
    scene 39-4 earl 83 with Dissolve(1)
    a "Wha?"
    earl "How about we get it on?"
    earl "Time to earn Carl's freedom..."
    scene black with Dissolve(1)
    play sound jacketcloth
    scene 39-4 earl 84 with Dissolve(1)
    "The old, ugly man stripped bare."
    scene 39-4 earl 85 with Dissolve(1)
    a "So... Um..."
    a "What do you want to do?"
    earl "Well... How about you get on your knees?"
    earl "And then we'll see..."
    scene 39-4 earl 86 with Dissolve(1)
    a "Umm... Ok..."
    "With each moment, Anna started to want that cock more and more."
    "She couldn't do much to resist..."
    "Like an unsatiable nymphomaniac."
    scene 39-4 earl 87 with Dissolve(1)
    pause 1
    scene 39-4 earl 88-1 with Dissolve(1)
    "She took his cock next to her mouth... Trying to tease him more."
    "That would get her on his good side more."
    scene EP11_Earl_Anim_3 with Dissolve(1)
label EP11_Earl_Sex_1:
    $ config.menu_include_disabled = True
    $ different_choice_menu = True
    play sound jerk2 loop
    menu EP11_Earl_Sex_Menu_1:
        "Lick":
            scene EP11_Earl_Anim_4 with Dissolve(1)
            jump EP11_Earl_Sex_Menu_1
        "Blowjob":
            jump EP11_Earl_Sex_2
label EP11_Earl_Sex_2:
    $ config.menu_include_disabled = True
    $ different_choice_menu = True
    play sound jerk2 loop
    scene 39-4 earl 88 with Dissolve(1)
    pause 1
    scene 39-4 earl 89 with Dissolve(1)
    menu EP11_Earl_Sex_Menu_2:
        "View 1":
            scene EP11_Earl_Anim_1 with Dissolve(1)
            jump EP11_Earl_Sex_Menu_2
        "View 2":
            scene EP11_Earl_Anim_2 with Dissolve(1)
            jump EP11_Earl_Sex_Menu_2
        "View 3":
            scene EP11_Earl_Anim_5 with Dissolve(1)
            jump EP11_Earl_Sex_Menu_2
        "Next":
            pass
    scene 39-4 earl 90 with Dissolve(1)
    pause 1
    scene 39-4 earl 91 with Dissolve(1)
    "Earl grabbed Anna by her head and pushed his cock deeper."
    play sound female_moan_5
    scene EP11_Earl_Anim_7 with Dissolve(1)
    earl "Yeah... That's a good mouth!"
    earl "You like to choke on old men's cock, don't ya?"
    scene EP11_Earl_Anim_7_Faster with Dissolve(1)
    a "MMmm..."
    scene 39-4 earl 92 with Dissolve(1)
    pause 1
    play sound surprise2
    scene 39-4 earl 93 with vpunch
    a "MMM!!!"
    a "KHAAA!"
    scene 39-4 earl 94 with vpunch
    pause 1.5
    play sound female_cough_1
    scene 39-4 earl 95 with Dissolve(1)
    a "Khe..."
    earl "Get on the bed. I'm about to fuck you raw."
    a "Lemme catch my breath."
    earl "No time, hehe."
    scene 39-4 earl 96 with Dissolve(1)
    a "Ah."
    scene 39-4 earl 97 with Dissolve(1)
    "Earl lunged into bed, eager to fuck Anna's brains out."
    earl "Hehe. This is great. Fuck, you're hot."
    scene 39-4 earl 98 with Dissolve(1)
    "Anna just went with it. Seeing the ugly man didn't make her feel any better."
    "She felt repulsed, even. But in Anna's mind, it was worth it."
    scene 39-4 earl 99 with Dissolve(1)
    earl "Now spread them legs."
    scene 39-4 earl 100 with Dissolve(1)
    earl "Oh yeah..."
    earl "This is the shit I've been fantasizing about."
    a "So, all this time..."
    a "You've only wanted to use me?"
    earl "Girl, ain't nothing in this world for free."
    earl "You want Carl free? You work for it."
    play sound jacketcloth
    scene 39-4 earl 101 with Dissolve(1)
    earl "Yeaahhh..."
    scene 39-4 earl 102 with Dissolve(1)
    earl "Time to enjoy you."
    a "Just don't go too fast at first."
    earl "Whatever."
    scene 39-4 earl 103 with Dissolve(1)
    "Anna was conflicted. A part of her liked being used, another didn't."
    "She was unable to decide which one it was."
    "Earl didn't care though, he rubbed away on her clit."
    scene EP11_Earl_Anim_6 with Dissolve(1)
    earl "Oh, yeah. You like it when I rub against your pussy?"
    "Anna didn't respond. She acted neutral."
    earl "I like it when women keep quiet, hehe."
    scene 39-4 earl 104 with Dissolve(1)
    earl "How about I..."
    scene 39-4 earl 105 with Dissolve(1)
    a "Ah..."
    a "It's..."
    "She gave up choosing. The moment Earl's cock started to enter her..."
    "She loved it."
    play sound female_moan_3
    scene 39-4 earl 106 with vpunch
    a "AAAHH!"
    scene 39-4 earl 107 with vpunch
    earl "YEAH!"
    scene 39-4 earl 108 with Dissolve(1)
    earl "Fuck... This pussy's loose."
    earl "You one good slut, eh?"
    earl "I love it when sluts are loose."
    scene 39-4 earl 109 with Dissolve(1)
    pause 1
    scene EP11_Earl_Anim_8 with Dissolve(1)
    play sound jerk2 loop
    $ EP11_Sex_Menu_var = 1
    menu EP11_Earl_Sex_Menu_3:
        "View 1":
            $ EP11_Sex_Menu_var = 1
            scene EP11_Earl_Anim_8 with Dissolve(1)
            jump EP11_Earl_Sex_Menu_3
        "View 2":
            $ EP11_Sex_Menu_var = 2
            scene EP11_Earl_Anim_9 with Dissolve(1)
            jump EP11_Earl_Sex_Menu_3
        "Faster":
            if EP11_Sex_Menu_var == 1:
                scene EP11_Earl_Anim_8_Faster with Dissolve(1)
            if EP11_Sex_Menu_var == 2:
                scene EP11_Earl_Anim_9_Faster with Dissolve(1)
            jump EP11_Earl_Sex_Menu_3
        "Slower":
            if EP11_Sex_Menu_var == 1:
                scene EP11_Earl_Anim_8 with Dissolve(1)
            if EP11_Sex_Menu_var == 2:
                scene EP11_Earl_Anim_9 with Dissolve(1)
            jump EP11_Earl_Sex_Menu_3
        "Continue":
            pass
    "Earl continued fucking Anna nice and good."
    "With fast pace."
    "Anna was moaning uncontrollably at this point."
    menu:
        "Put the cock in her ass!":
            "The cock had sent her over the edge."
            earl "How about I..."
            scene 39-4 earl 110 with Dissolve(1)
            "He pulled out and went straight for her rear entrance."
            scene 39-4 earl 111 with Dissolve(1)
            "By now, Anna was getting stimulated even by anal."
            play audio female_moan_1
            $ EP11_Sex_Menu_var = 1
            scene EP11_Earl_Anim_10 with Dissolve(1)
            menu EP11_Earl_Sex_Menu_4:
                "View 1":
                    $ EP11_Sex_Menu_var = 1
                    scene EP11_Earl_Anim_10 with Dissolve(1)
                    jump EP11_Earl_Sex_Menu_4
                "View 2":
                    $ EP11_Sex_Menu_var = 2
                    scene EP11_Earl_Anim_11 with Dissolve(1)
                    jump EP11_Earl_Sex_Menu_4
                "Faster":
                    if EP11_Sex_Menu_var == 1:
                        scene EP11_Earl_Anim_10_Faster with Dissolve(1)
                    if EP11_Sex_Menu_var == 2:
                        scene EP11_Earl_Anim_11_Faster with Dissolve(1)
                    jump EP11_Earl_Sex_Menu_4
                "Slower":
                    if EP11_Sex_Menu_var == 1:
                        scene EP11_Earl_Anim_10 with Dissolve(1)
                    if EP11_Sex_Menu_var == 2:
                        scene EP11_Earl_Anim_11 with Dissolve(1)
                    jump EP11_Earl_Sex_Menu_4
                "Continue":
                    pass
        "Don't give her Anal.":
            pass
    earl "How about I flip you over."
    earl "Just like a proper slut!"
    play sound whoosh_1
    scene 39-4 earl 114 with Dissolve(1)
    pause 1
    play sound femgasp
    $ EP11_Sex_Menu_var = 1
    scene EP11_Earl_Anim_12 with Dissolve(1)
    menu EP11_Earl_Sex_Menu_6:
        "View 1":
            $ EP11_Sex_Menu_var = 1
            scene EP11_Earl_Anim_12 with Dissolve(1)
            jump EP11_Earl_Sex_Menu_6
        "View 2":
            $ EP11_Sex_Menu_var = 2
            scene EP11_Earl_Anim_15 with Dissolve(1)
            jump EP11_Earl_Sex_Menu_6
        "Faster":
            if EP11_Sex_Menu_var == 1:
                scene EP11_Earl_Anim_12_Faster with Dissolve(1)
            if EP11_Sex_Menu_var == 2:
                scene EP11_Earl_Anim_15_Faster with Dissolve(1)
            jump EP11_Earl_Sex_Menu_6
        "Slower":
            if EP11_Sex_Menu_var == 1:
                scene EP11_Earl_Anim_12 with Dissolve(1)
            if EP11_Sex_Menu_var == 2:
                scene EP11_Earl_Anim_15 with Dissolve(1)
            jump EP11_Earl_Sex_Menu_6
        "Continue":
            pass
    earl "Oh yeah."
    earl "Your ass looks magnificent."
    play sound female_moan_4
    a "Fuck..."
    earl "How about the other hole, heh."
    menu:
        "Anal":
            scene 39-4 earl 115 with Dissolve(1)
            pause 2
            scene EP11_Earl_Anim_13 with Dissolve(1)
            $ EP11_Sex_Menu_var = 1
            menu EP11_Earl_Sex_Menu_5:
                "View 1":
                    $ EP11_Sex_Menu_var = 1
                    scene EP11_Earl_Anim_13 with Dissolve(1)
                    jump EP11_Earl_Sex_Menu_5
                "View 2":
                    $ EP11_Sex_Menu_var = 2
                    scene EP11_Earl_Anim_14 with Dissolve(1)
                    jump EP11_Earl_Sex_Menu_5
                "Faster":
                    if EP11_Sex_Menu_var == 1:
                        scene EP11_Earl_Anim_13_Faster with Dissolve(1)
                    if EP11_Sex_Menu_var == 2:
                        scene EP11_Earl_Anim_14_Faster with Dissolve(1)
                    jump EP11_Earl_Sex_Menu_5
                "Slower":
                    if EP11_Sex_Menu_var == 1:
                        scene EP11_Earl_Anim_13 with Dissolve(1)
                    if EP11_Sex_Menu_var == 2:
                        scene EP11_Earl_Anim_14 with Dissolve(1)
                    jump EP11_Earl_Sex_Menu_5
                "Cum":
                    pass
        "Cum":
            pass
    earl "AAHH..."
    earl "FUCK!"
    "Suddenly Earl felt the point of no return..."
    menu:
        "Cum in her ass":
            with flash
            earl "Fuck!!!"
            earl "I'll fill you up!"
            with flash
            play sound cum_sound
            play audio moaning_1
            scene 39-4 earl 116 with flash_vpunch
            pause 0.5
            scene 39-4 earl 120 with flash_vpunch
            pause 0.5
            scene 39-4 earl 121 with flash_vpunch
            earl "AAHHH!"
            scene 39-4 earl 117 with Dissolve(1)
            pause
        "Cum in her pussy":
            scene EP11_Earl_Anim_12 with Dissolve(1)
            with flash
            play audio moaning_1
            earl "I will fill up that pussy good!!!!"
            earl "YEAAAAH!!"
            with flash
            earl "AAH."
            play sound cum_sound
            scene 39-4 earl 118 with flash_vpunch
            pause 0.5
            scene 39-4 earl 120 with flash_vpunch
            pause 0.5
            scene 39-4 earl 121 with flash_vpunch
            pause 2
            scene 39-4 earl 119 with Dissolve(1)
            pause
        "Cum in her mouth":
            earl "SHIT, SHIT!"
            with flash
            earl "Turn AROUND!"
            scene 39-4 earl 122 with Dissolve(0.5)
            pause 0.5
            scene 39-4 earl 123 with Dissolve(0.5)
            play sound cum_sound
            scene 39-4 earl 124 with flash_vpunch
            pause 2
            scene 39-4 earl 125 with Dissolve(1)
            a "AAhh..."
            earl "FUCK YEAH!"
            scene 39-4 earl 126 with Dissolve(1)
            pause
    $ renpy.end_replay()
    scene 39-4 earl 128 with Dissolve(1)
    a "Are... Are you done?"
    earl "Hehe... I gotta run, but this isn't the end."
    earl "Fuck you're as good as I thought. Better than I expected, actually."
    a "Will you catch the person that's behind this?"
    scene 39-4 earl 130 with Dissolve(1)
    earl "Yes, ofcooourse... Hehe..."
    a "And... And what about Carl?"
    earl "Like I said, this isn't the end. You might have me convinced... But..."
    scene black with Dissolve(1)
    play sound jacketcloth
    scene 39-4 earl 131 with Dissolve(1)
    earl "You still have to convince my pals."
    a "WHAT?"
    scene 39-4 earl 132 with Dissolve(1)
    earl "It's simple. You want Carl to be free? You gotta play by my rules."
    a "But..."
    scene 39-4 earl 133 with Dissolve(1)
    earl "Think on it."
    earl "I will be in touch."
    play sound door2
    scene 39-4 earl 134 with Dissolve(1)
    a "What..."
    a "This is..."
    scene 39-4 earl 135 with Dissolve(1)
    "Anna was so deep in thought."
    "At this point she didn't even feel much remorse for this kind of a thing."
    a "I'd better get some sleep..."
    $ different_choice_menu = False
    $ EP11_var_14 = True
    jump EP11_Episode_End
label EP11_Alfred_House:
    play sound high_heels_walking
    scene black with Dissolve(1)
    pause 1
    play music SpeedBumpsSong
    scene 39-5 alfred 1 with Dissolve(1)
    a2 "Ah. Anna!"
    a2 "So good to see you. so good."
    a "And you too, Alfred."
    a "How are you holding up?"
    scene 39-5 alfred 1-1 with Dissolve(1)
    a2 "As nervous as ever, haha!"
    a2 "I will manage. What about you, love?"
    a "I'm doing good. Excited for this opportunity."
    a2 "You and me both."
    scene 39-5 alfred 2 with Dissolve(1)
    a2 "Patricia will be with us shortly."
    play sound door2
    scene 39-5 alfred 3 with Dissolve(1)
    p2 "Hey, guys!"
    a2 "And speak of the devil, haha."
    scene 39-5 alfred 3-1 with Dissolve(1)
    p2 "OH, haha. Alfred, you seem in a jolly good mood today?"
    a2 "Hah. Don't mind me, I'm just masking my nervousness with joy."
    p2 "The best way to do it."
    scene 39-5 alfred 4-1 with Dissolve(1)
    a "So, where we at?"
    a2 "Well, I've prepped all the outfits. I'm waiting on Hector. He'll take us to Westpoint."
    a "That's like an hour's ride, isn't it?"
    a2 "Just about."
    scene 39-5 alfred 4 with Dissolve(1)
    a2 "We'll probably spend a couple of hours there at most."
    a "No problem."
    a2 "You can go pack up at your place, and we'll await you downstairs. Sounds good?"
    a "Yes. Will get on it right away."
    scene black with Dissolve(1)
    pause 2
    play sound zipper_1
    scene 39-5 alfred 6 with Dissolve(0.2)
    pause 1
    scene 39-5 alfred 7 with Dissolve(0.2)
    pause 1
    play ambience citytraffic
    scene black with Dissolve(1)
    pause 2
    scene 39-5 alfred 8 with Dissolve(1)
    a2 "A wonderful day indeed."
    a2 "Perfect for a fashion show, haha!"
    p2 "Look at you, all happy. I love it when you're like this, Alfred."
    scene 39-5 alfred 9 with Dissolve(1)
    a "Alright guys, I'm ready."
    scene 39-5 alfred 10 with Dissolve(1)
    a2 "Great."
    h1 "Anna! Great to see you."
    h1 "Look as good as ever."
    a "Hah, thanks, Hector."
    scene 39-5 alfred 11 with Dissolve(1)
    h1 "Big day ahead of you, eh?"
    a "Quite so. I'm excited."
    h1 "Wonderful, wonderful."
    scene 39-5 alfred 12 with Dissolve(1)
    a "I've been wanting to be a model for a long time."
    h1 "And now is your chance."
    a "Thanks to Alfred."
    h1 "Of course."
    scene 39-5 alfred 13 with Dissolve(1)
    h1 "Our Alfred has given us a lot of opportunities."
    scene 39-5 alfred 14 with Dissolve(1)
    a2 "I think we should get going."
    a2 "Wouldn't wanna miss it."
    h1 "Right away."
    play sound car_door_open
    scene 39-5 alfred 15 with Dissolve(1)
    pause 1
    play sound car_door_close
    play ambience car_engine_ambience
    scene 39-5 alfred 16 with Dissolve(1)
    h1 "So you all guys ready?"
    h1 "Alfred, got the outfits?"
    a2 "I wouldn't miss them for the world."
    h1 "How you girls doing in the back?"
    h1 "All comfortable?"
    a "We are, thanks."
    scene 39-5 alfred 17 with Dissolve(1)
    p2 "Did you take the spares?"
    a2 "Oh... I forgot..."
    p2 "Hehe, I took them, don't worry."
    a2 "Patricia, you are a lifesaver."
    scene 39-5 alfred 18 with Dissolve(1)
    a "What exactly awaits us?"
    p2 "Well, there will be only select individuals who work in the fashion business."
    p2 "It's a semi-closed, special event. Only people with invitations got in."
    scene 39-5 alfred 18-1 with Dissolve(1)
    a "So high-level designers and fashion 'people'?"
    a "Hector, too?"
    scene 39-5 alfred 19 with Dissolve(1)
    p2 "Alfred pulled strings."
    p2 "I'm his number two, and you are the main model."
    p2 "Also, I think Aldo will so join."
    scene 39-5 alfred 19-1 with Dissolve(1)
    p2 "They are 'investors'"
    h1 "Hey. I'm your personal chauffeur, as well!"
    h1 "Haha."
    scene 39-5 alfred 20 with Dissolve(1)
    a2 "Watch the road, chauffeur!"
    h1 "On it, chief."
    a2 "Otherwise we'll have the same situation as that one time in Corkridge."
    h1 "That... That was an accident."
    scene 39-5 alfred 21 with Dissolve(1)
    a2 "Yeah. It was! You didn't watch the road."
    p2 "What happened?"
    a2 "We drove on the sidewalk and hit a postbox."
    a "Haha."
    scene 39-5 alfred 21-1 with Dissolve(1)
    a2 "Hector was quite the rest of the drive."
    a2 "But it seems he wants to pay another 300$ for front bumper change?"
    scene 39-5 alfred 22 with Dissolve(1)
    h1 "Alright, Alright. I get your point."
    h1 "But what about that one time when you were driving?"
    a2 "Don't start with the 'whataboutism' You know it wasn't my fault at all."
    h1 "I beg to differ..."
    scene 39-5 alfred 23 with Dissolve(1)
    "While both old men were discussing the details of their driving..."
    "Anna felt a little sleepish."
    a "I think, I will take a little nap."
    p2 "Sure."
    scene 39-5 alfred 24 with Dissolve(1)
    p2 "Oh... I mean..."
    p2 "That's ok."
    "Anna quickly fell asleep."
    scene 39-5 alfred 25 with Dissolve(1)
    pause 1
    scene 39-5 alfred 26 with Dissolve(1)
    pause 1
    scene black with Dissolve(1)
    pause 1
    scene 39-5 alfred 27 with Dissolve(1)
    p2 "Anna..."
    p2 "Anna?"
    scene 39-5 alfred 28 with Dissolve(1)
    a "Huh. Wha?"
    p2 "Wakey, wakey. We're here."
    a "That was fast."
    p2 "Yeah, you passed out so fast."
    p2 "Must've been tired."
    scene 39-5 alfred 29 with Dissolve(1)
    a "Damn, those look like some serious people."
    a "Expensive cars."
    a "Models."
    scene 39-5 alfred 31 with Dissolve(1)
    h1 "Ok, guys. I'll drop you off here and park the car in the back."
    a2 "Alright, you'll bring the outfits from there, ye?"
    h1 "Yes, sir."
    scene 39-5 alfred 30 with Dissolve(1)
    a2 "Alright, this is it. Let's show them how we do it un Sun City, eh?"
    a "Yes!"
    p2 "Wohoooo!"
    stop ambience fadeout 1
    scene black with Dissolve(1)
    pause 1
    play sound door2
    scene 39-5 alfred 32 with Dissolve(1)
    a2 "So, this is us."
    a "Uuuuh... I'm getting nervous."
    a2 "You've got this, Anna. You are a natural."
    scene 39-5 alfred 33 with Dissolve(1)
    a2 "The show will start in some 20 mins or so."
    a2 "We got here in the nick of time."
    h1 "Thanks to my good driving."
    a2 "Right..."
    scene 39-5 alfred 34 with Dissolve(1)
    a "Ooh... This is actually happening."
    a "Will there be a lot of people?"
    a2 "Not that many. This is a closed event for the fashion industry only, mostly."
    a2 "The open one will happen later."
    scene 39-5 alfred 35 with Dissolve(1)
    a2 "Listen, we've got to get to our seats, you'll manage right?"
    a2 "Patricia will help you with the outfits"
    a2 "Anna, you got this. Good luck!"
    play sound door2
    scene 39-5 alfred 36 with Dissolve(1)
    p2 "Are you ready?"
    a "I... I don't know."
    p2 "What am I saying, of course you are."
    scene 39-5 alfred 37 with Dissolve(1)
    a "It's just that I've never done anything this big."
    p2 "There is a first time for everything, you know that."
    p2 "Besides, gotta take the step some time, right?"
    a "I mean... Yeah."
    scene 39-5 alfred 38 with Dissolve(1)
    p2 "Trust me, if anyone's got it, it's you."
    a "Alright... I got this, Let's get me into the first outfit."
    scene 39-5 alfred 38-1 with Dissolve(1)
    p2 "That's what I'm talking about, hehe!"
    p2 "Alright, get naked, girl."
    scene 39-5 alfred 39 with Dissolve(1)
    a "Ooh. Sassy, I like it."
    a "Where are the outfits?"
    p2 "Don't worry, I'll bring 'em."
    scene 39-5 alfred 40 with Dissolve(1)
    pause 1
    play sound undress
    scene 39-5 alfred 41 with Dissolve(1)
    pause 1
    scene black with Dissolve(1)
    play sound jacketcloth
    pause 1
    play sound cloth_sound1
    scene 39-5 alfred 42 with Dissolve(1)
    p2 "And we're golden."
    p2 "You look great in this."
    a "This is one of the outfits from Alfred's collections?"
    p2 "Yes."
    scene 39-5 alfred 43 with Dissolve(1)
    a "My nipples, though."
    a "You can see them a little."
    p2 "Not a problem, trust me."
    p2 "It is that way for a reason, you know?"
    play sound door2
    scene 39-5 alfred 44 with Dissolve(1)
    a2 "Well, well... You look great."
    a2 "We all set?"
    scene 39-5 alfred 45 with Dissolve(1)
    a "Yeah."
    p2 "Anna looks great in this thing. You got the measurements perfectly."
    a2 "The show's about to start, Anna should get into position."
    a2 "Let's go, Patricia."
    scene 39-5 alfred 46 with Dissolve(1)
    p2 "You've got this, Anna. Just do what you do best."
    a "And that is?"
    p2 "Look fucking amazing."
    a "Haha."
    play sound door2
    scene black with Dissolve(1)
    play music Runway_Song
    scene 39-5 alfred 47 with Dissolve(1)
    a "Ok... This is it..."
    a "Gotta wait for my queue."
    a "I'm ready..."
    scene 39-5 alfred 48 with Dissolve(1)
    a "Ok, my turn."
    "Anna started to walk, feeling fully in character."
    "Leaving all doubts behind her."
    scene 39-5 alfred 49 with Dissolve(1)
    "As she entered, it's like the runway lit up."
    "People were curious. They had never seen Anna before."
    "Interested in both the clothing and the model."
    scene 39-5 alfred 50 with Dissolve(1)
    "Anna was flaming."
    a "{i}...This is so cool..."
    a "{i}...I'm finally on the runway, I've been wanting to do this for so long."
    scene 39-5 alfred 51 with Dissolve(1)
    pause 3
    scene 39-5 alfred 52 with Dissolve(1)
    pause 2
    scene 39-5 alfred 53 with Dissolve(1)
    gc1 "Who is that girl?"
    gc1 "I've never seen here."
    h1 "That is Anna. She's Alfred's model."
    scene 39-5 alfred 54 with Dissolve(1)
    a2 "Not bad for the first outfit. Can you go and help her change?"
    p2 "On it, Alfred."
    scene 39-5 alfred 55 with Dissolve(1)
    a "ooOO... I'm so exciiteeed."
    play sound door2
    scene 39-5 alfred 56 with Dissolve(1)
    p2 "That was great, Anna!"
    p2 "You had the proper stride, and everything didn't linger for too long on the runway either."
    p2 "Gave the people just enough."
    p2 "You can take your panties off, too."
    a "You sure?"
    p2 "The outfit will look better."
    play sound undress
    scene 39-5 alfred 57 with Dissolve(1)
    pause 1
    play sound jacketcloth
    scene 39-5 alfred 58 with Dissolve(1)
    a "Well, well..."
    a "This a lot skimpier."
    p2 "I know, so sexy, though."
    scene 39-5 alfred 59 with Dissolve(1)
    p2 "Alright, we don't have much time."
    p2 "I'll run back, and you get ready."
    scene 39-5 alfred 60 with Dissolve(1)
    a "Will do."
    p2 "You are doing great, Anna."
    a "I know, haha. I'm feeling so confident right now."
    p2 "That's great! Good luck!"
    play sound door2
    scene black with Dissolve(1)
    pause 1
    scene 39-5 alfred 61 with Dissolve(1)
    "Anna got on the runway with the second outfit and now was piquing the interest of everyone."
    "This was a lot skimpier a lot more succulent."
    scene 39-5 alfred 62 with Dissolve(1)
    "People were gazing up on the magnificence in front of them."
    pause 1
    scene 39-5 alfred 63 with Dissolve(1)
    pause 1
    scene 39-5 alfred 64 with Dissolve(1)
    pause 2
    scene 39-5 alfred 65 with Dissolve(1)
    pause 1
    scene 39-5 alfred 66 with Dissolve(1)
    al1 "Anna is really hitting her stride."
    h1 "Oh, yeah."
    scene 39-5 alfred 67 with Dissolve(1)
    pause 1
    scene 39-5 alfred 67-1 with Dissolve(1)
    gc1 "Hold on... She isn't wearing panties?"
    h1 "Alfred's collection is all about the succulence of the female body."
    h1 "You know that empires have crumbled because of that."
    gc1 "Huh... Interesting, thought."
    scene 39-5 alfred 68 with Dissolve(1)
    pause 2
    scene black with Dissolve(1)
    pause 0.5
    scene 39-5 alfred 69 with Dissolve(1)
    a "Ooohhh... I'm so excited. Everyone's looking at me, that's crazy."
    p2 "I thought you had gotten used to people looking at you."
    a "Yeah, but... This is a bit different, I can't. So exciting."
    scene 39-5 alfred 69-1 with Dissolve(1)
    a "And all of them are people working in the fashion industry?"
    p2 "Many of them are representatives and other designers."
    scene 39-5 alfred 70 with Dissolve(1)
    p2 "So yeah, word will get around about you."
    p2 "Anyway, the last outfit."
    p2 "The main attraction."
    play sound undress
    scene 39-5 alfred 71 with Dissolve(1)
    a "It was beautiful, I remember."
    play sound undress
    scene 39-5 alfred 72-1 with Dissolve(0.5)
    pause 0.5
    scene 39-5 alfred 72-2 with Dissolve(0.5)
    pause 0.5
    scene 39-5 alfred 72 with Dissolve(0.5)
    pause 0.5
    scene 39-5 alfred 73 with Dissolve(1)
    a "Gorgeous."
    p2 "Agreed. It's so seductive."
    scene 39-5 alfred 74 with Dissolve(1)
    p2 "Oh, and remember. for this one, keep your face neutral."
    p2 "The main focus is the outfit."
    a "Ok. Got it."
    scene 39-5 alfred 75 with Dissolve(1)
    p2 "Anyway, I'll go. Don't want to miss it."
    p2 "Good luck!"
    scene 39-5 alfred 76 with Dissolve(1)
    "Anna pulled out her phone for a quick selfie."
    play sound takephoto
    with flash
    scene 39-5 alfred 76-1 with Dissolve(1)
    "And another."
    play sound takephoto
    with flash
    a "Alright. Time to go."
    scene black with Dissolve(1)
    scene 39-5 alfred 77 with Dissolve(1)
    "Anna got on the stage."
    a "Time to get my serious face on."
    play music BombshellSong fadein 5
    scene 39-5 alfred 78 with Dissolve(1)
    pause 1
    scene 39-5 alfred 80 with Dissolve(1)
    pause 2
    scene EP11_Alfred_Fashion_Runway with Dissolve(1)
    pause 12
    scene 39-5 alfred 82-1 with Dissolve(1)
    al1 "Damn... I can't believe he pulled it off."
    al1 "People will fall over each other for this outfit now."
    h1 "I know. He's good at this."
    scene 39-5 alfred 82 with Dissolve(1)
    a "Wheeew..."
    a "That was nuts!"
    a "I could see all the open mouths, they were all impressed."
    scene 39-5 alfred 83 with Dissolve(1)
    a2 "Haha! You are absolutely amazing at this."
    a2 "You should've seen the competition's faces."
    a2 "This will be the talk of the week in the fashion world."
    menu:
        "The adrenaline rush made Anna as horny as ever.":
            $ persistent.scene_33 = True
            jump EP11_Alfred_Sex_Label
        "Anna refrained from sexual involvement.":
            a "Anyway... I will take a breather."
            a "It's been rather stressful."
            a2 "Yeah, me too."
            a2 "Voting will begin shortly, and after that, the winner will be announced."
            a2 "I'll go to the toilet."
            a "Alright."
            scene black with Dissolve(1)
            pause
            jump EP11_Alfred_Fashion_Finished
label EP11_Alfred_Sex_Label:
    scene 39-5 alfred 84 with Dissolve(1)
    a "Shush..."
    a "I'm so full of excitement right now..."
    a2 "Oh... Hah..."
    play music SexyTimeSong2
    scene 39-5 alfred 85 with Dissolve(1)
    a "I know you want me, Alfred."
    a2 "I... So succulent, so carnal."
    scene 39-5 alfred 86 with Dissolve(1)
    pause 2
    scene 39-5 alfred 87 with Dissolve(1)
    a "How about I give you a reward for your good work?"
    a2 "My good work?"
    a "Oh yeah. This outfit made me look irresistible."
    scene 39-5 alfred 88 with Dissolve(1)
    pause 1
    play sound undress
    scene 39-5 alfred 89 with Dissolve(1)
    pause 1
    a2 "Ahh..."
    scene EP11_Alfred_Anim_1 with Fade(0.2, 0, 0.2)
    $ EP11_Alfred_menu_option_1 = False
    $ config.menu_include_disabled = True
    $ different_choice_menu = True
    play sound jerk loop
    menu EP11_Alfred_Menu_1:
        "Faster" if EP11_Alfred_menu_option_1 == False:
            $ EP11_Alfred_menu_option_1 = True
            scene EP11_Alfred_Anim_1_Faster with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_1
        "Slower" if EP11_Alfred_menu_option_1 == True:
            $ EP11_Alfred_menu_option_1 = False
            scene EP11_Alfred_Anim_1 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_1
        "Continue":
            pass
    a "Hehe..."
    a "How about I..."
    scene 39-5 alfred 90 with Dissolve(1)
    a2 "Oh, Anna..."
    pause 1
    scene EP11_Alfred_Anim_2 with Fade(0.2, 0, 0.2)
    $ EP11_Alfred_menu_option_1 = False
    menu EP11_Alfred_Menu_2:
        "Lick" if EP11_Alfred_menu_option_1 == False:
            $ EP11_Alfred_menu_option_1 = True
            scene EP11_Alfred_Anim_3 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_2
        "Handjob" if EP11_Alfred_menu_option_1 == True:
            $ EP11_Alfred_menu_option_1 = False
            scene EP11_Alfred_Anim_2 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_2
        "Continue":
            pass
    scene EP11_Alfred_Anim_4 with Fade(0.2, 0, 0.2)
    pause 1.8
    scene EP11_Alfred_Anim_5 with Fade(0.2, 0, 0.2)
    $ EP11_Alfred_menu_option_2 = 1
    menu EP11_Alfred_Menu_4:
        "View 1":
            $ EP11_Alfred_menu_option_2 = 1
            scene EP11_Alfred_Anim_5 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_4
        "View 2":
            $ EP11_Alfred_menu_option_2 = 2
            scene EP11_Alfred_Anim_6 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_4
        "Faster":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_5_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_4
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_6_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_4
        "Slower":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_5 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_4
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_6 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_4
        "Continue":
            pass
    stop sound
    scene 39-5 alfred 91 with Dissolve(1)
    a2 "Let's get out of sight."
    a "Good idea, hehe..."
    scene 39-5 alfred 92 with Dissolve(1)
    "They forgot to close the door, though."
    "They also didn't care."
    play sound jacketcloth
    scene 39-5 alfred 93 with Dissolve(1)
    pause 1
    play sound cloth_sound1
    scene 39-5 alfred 94 with Dissolve(1)
    a "Ah..."
    a "I want you inside of me, now!"
    a2 "I must oblige."
    a "Fuck me right now... Ah..."
    scene 39-5 alfred 95 with Dissolve(1)
    "Alfred waited not a moment longer and put his dick deep up Anna's pussy."
    "She felt intoxicated from the excitement."
    scene EP11_Alfred_Anim_7 with Fade(0.2, 0, 0.2)
    $ EP11_Alfred_menu_option_2 = 1
    play sound jerk2
    play audio female_moan_2
    menu EP11_Alfred_Menu_5:
        "View 1":
            $ EP11_Alfred_menu_option_2 = 1
            scene EP11_Alfred_Anim_7 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_5
        "View 2":
            $ EP11_Alfred_menu_option_2 = 2
            scene EP11_Alfred_Anim_8 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_5
        "Faster":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_7_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_5
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_8_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_5
        "Slower":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_7 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_5
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_8 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_5
        "Continue":
            pass
    a "FUCK!"
    play audio female_moan_1
    a "AAHHH!!!"
    scene EP11_Alfred_Anim_9 with Fade(0.2, 0, 0.2)
    a2 "That pussyy..."
    a "Alfred, your cock..."
    "Both of them were enjoying the sex deeply."
    "Both ecstatic in more than one way."
    $ EP11_Alfred_menu_option_2 = 1
    menu EP11_Alfred_Menu_6:
        "View 1":
            $ EP11_Alfred_menu_option_2 = 1
            scene EP11_Alfred_Anim_9 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_6
        "View 2":
            $ EP11_Alfred_menu_option_2 = 2
            scene EP11_Alfred_Anim_10 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_6
        "Faster":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_9_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_6
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_10_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_6
        "Slower":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_9 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_6
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_10 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_6
        "Continue":
            pass
    a2 "Lemme slow down for a bit... Ahh.."
    a2 "Your pussy is almost too much to handle."
    a "Alfred... You are the best fucker ever..."
    play sound female_moan_3
    scene EP11_Alfred_Anim_11 with Fade(0.2, 0, 0.2)
    a "Continue like this for a moment..."
    pause
    "Anna was feeling stimulated every moment of the intercourse."
    "Alfred's cock was filling her up perfectly."
    scene EP11_Alfred_Anim_11_Faster with Fade(0.2, 0, 0.2)
    pause
    a "Yeah..."
    a2 "Mhhh..."
    "Alfred was feeling young again."
    "Like he could conquer the world."
    play audio female_moan_5
    "A young, unexplainably hot girl in front of him."
    "A Fashion show to win..."
    "Everything was going great for the man."
    play sound whoosh
    play sound jerk loop
    scene EP11_Alfred_Anim_15 with Fade(0.2, 0, 0.2)
    "Alfred flipped Anna over for a change."
    "And to take a breath."
    a2 "Whew... I think I haven't fucked like this in a while."
    a "Hehe... You've always got something going on with me, you know that right?"
    $ EP11_Alfred_menu_option_1 = False
    menu EP11_Alfred_Menu_8:
        "Faster" if EP11_Alfred_menu_option_1 == False:
            $ EP11_Alfred_menu_option_1 = True
            scene EP11_Alfred_Anim_15_Faster with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_8
        "Slower" if EP11_Alfred_menu_option_1 == True:
            $ EP11_Alfred_menu_option_1 = False
            scene EP11_Alfred_Anim_15 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_8
        "Continue":
            pass

    scene EP11_Alfred_Anim_13 with Fade(0.2, 0, 0.2)
    a "AHHh... Alfred... Your cock..."
    a2 "I'm getting close..."
    play audio female_moan_4
    a2 "Not long anymore... FUUCK!!!"
    $ EP11_Alfred_menu_option_2 = 1
    menu EP11_Alfred_Menu_7:
        "View 1":
            $ EP11_Alfred_menu_option_2 = 1
            scene EP11_Alfred_Anim_13 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_7
        "View 2":
            $ EP11_Alfred_menu_option_2 = 2
            scene EP11_Alfred_Anim_14 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_7
        "Faster":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_13_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_7
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_14_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_7
        "Slower":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_13 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_7
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_14 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_7
        "Cum!":
            pass
    "Both perverts started to cum..."
    with flash_vpunch
    play audio moaninglong_1
    play sound jerk2 loop
    a2 "AHHH!!!"
    a2 "ANNA!!!"
    a2 "I'm cummiiingg!!"
    with flash_vpunch
    with flash_vpunch
    a "ALFRED!!"
    a "FUUUCKK!!!"
    a "FILL ME UPPP!!!!!"
    scene 39-5 alfred 97 with vpunch
    pause 1
    scene 39-5 alfred 98 with vpunch
    pause 1
    play sound cum_sound
    with flash
    a "Oh, Alfred..."
    scene 39-5 alfred 99 with Dissolve(1)
    a2 "Pardon..."
    a2 "I feel a bit dizzy..."
    scene 39-5 alfred 100 with Dissolve(1)
    a "I'm holding you... You're safe."
    a2 "Heh... This is amazing, Anna."
    a2 "I'd like to stay here for a moment and hold you."
    scene 39-5 alfred 101 with Dissolve(1)
    a "Me too."
    scene 39-5 alfred 102 with Dissolve(1)
    a "Somebody's coming!"
    a2 "Ok, shit."
    scene black with Dissolve(1)
    scene 39-5 alfred 103 with Dissolve(1)
    a2 "Yes?"
    a2 "What is it???"
    scene 39-5 alfred 104 with Dissolve(1)
    al1 "Well, the award ceremony will start soon."
    al1 "Voting has ended."
    a2 "Ah, right. Ok, I'm going."
    scene 39-5 alfred 105 with Dissolve(1)
    "Alfred rushed away without hesitation."
    "Anna was still coming down from the session."
    a "Whew... This is crazy..."
    scene 39-5 alfred 106 with Dissolve(1)
    h1 "What's that?"
    al1 "Wait."
    scene 39-5 alfred 107 with vpunch
    h1 "Hello, hello, Anna."
    h1 "Nice show."
    a "Thank you."
    h1 "You know, I think we found something that belongs to you?"
    scene 39-5 alfred 108 with Dissolve(1)
    al1 "Looks like you lost it indeed."
    scene 39-5 alfred 109 with Dissolve(1)
    a "Oh... Um..."
    a "Thanks."
    scene 39-5 alfred 110 with Dissolve(1)
    a "Well, I'd better get going."
    a "Wouldn't wanna miss the ceremony."
    h1 "Oh, don't go yet. We still have a moment."
    scene 39-5 alfred 111 with Dissolve(1)
    h1 "We're pretty sure what happened here."
    h1 "How about we get some, too?"
    h1 "You are, after all, a slut."
    $ different_choice_menu = False
    menu:
        "Hehe... Well, I might be... (IF Corruption > 30)" if AnnaCorruption >=30:
            pass
        "Yeah, perhaps, but only Alfred's slut.":
            a "You ain't getting any."
            $ renpy.end_replay()
            jump EP11_Alfred_Fashion_Finished
        "How can you talk in this tone? NO!":
            a "And that's final. Please leave me alone now."
            $ renpy.end_replay()
            jump EP11_Alfred_Fashion_Finished
    play music closuresong
    play sound undress
    scene black with Dissolve(1)
    scene 39-5 alfred 112 with Dissolve(1)
    pause 1
    play sound surprise2
    scene 39-5 alfred 113 with Dissolve(1)
    al1 "Well, then? How about you get on with it?"
    a "Ok."
    scene 39-5 alfred 114 with Dissolve(1)
    h1 "Yes... That looks good!"
    "Anna embraced her inner slut even more."
    a "You wanna enjoy my mouth?"
    h1 "Hell yeah, girl!"
    play sound jerk3 loop
    scene EP11_Alfred_Anim_16 with Fade(0.2, 0, 0.2)
    $ EP11_Alfred_menu_option_2 = 1
    $ different_choice_menu = True
    menu EP11_Alfred_Menu_9:
        "View 1":
            $ EP11_Alfred_menu_option_2 = 1
            scene EP11_Alfred_Anim_16 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_9
        "View 2":
            $ EP11_Alfred_menu_option_2 = 2
            scene EP11_Alfred_Anim_17 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_9
        "Faster":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_16_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_9
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_17_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_9
        "Slower":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_16 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_9
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_17 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_9
        "Continue":
            pass
    a "MM..."
    h1 "This mouth is just indescribable!"
    al1 "The truth!"

    scene EP11_Alfred_Anim_18 with Fade(0.2, 0, 0.2)
    "Anna had become a fuck hole for these two."
    "She accepted it..."
    $ different_choice_menu = True
    $ EP11_Alfred_menu_option_1 = False
    menu EP11_Alfred_Menu_10:
        "View 1" if EP11_Alfred_menu_option_1 == True:
            $ EP11_Alfred_menu_option_1 = False
            scene EP11_Alfred_Anim_18 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_10
        "View 2" if EP11_Alfred_menu_option_1 == False:
            $ EP11_Alfred_menu_option_1 = True
            scene EP11_Alfred_Anim_19 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_10
        "Continue":
            pass
    al1 "Aghh... I wanna enter your pussy!"
    a "Mhmm..."
    al1 "Oh, Yeah!"
    a "Don't hesitate, fuck me!"
    al1 "As you wish, hehe."
    play sound jerk loop
    scene EP11_Alfred_Anim_20 with Fade(0.2, 0, 0.2)
    al1 "Fuuck, This pussy's good!"
    h1 "Don't go too long, I wanna fuck her, too!"
    $ EP11_Alfred_menu_option_2 = 1
    $ different_choice_menu = True
    stop sound
    queue sound(female_moan_1, female_moan_2, femmoan_3, female_moan_5, femgasp_1, MoaningNine, femmoan_4, female_moan_4) loop
    menu EP11_Alfred_Menu_11:
        "View 1":
            $ EP11_Alfred_menu_option_2 = 1
            scene EP11_Alfred_Anim_20 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_11
        "View 2":
            $ EP11_Alfred_menu_option_2 = 2
            scene EP11_Alfred_Anim_21 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_11
        "Faster":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_20_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_11
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_21_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_11
        "Slower":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_20 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_11
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_21 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_11
        "Continue":
            pass
    stop sound
    play audio undress
    scene 39-5 alfred 115-1 with Dissolve(1)
    "Aldo removed Anna's bra in one smooth motion."
    play audio female_moan_2
    al1 "I want to see them naked tits."
    al1 "And bury my face in them."
    play audio jerk loop
    scene EP11_Alfred_Anim_22 with Fade(0.2, 0, 0.2)
    play audio female_moan_1
    $ EP11_Alfred_menu_option_2 = 1
    $ different_choice_menu = True
    queue sound(female_moan_1, female_moan_2, femmoan_3, female_moan_5, femgasp_1, MoaningNine, femmoan_4, female_moan_4) loop
    menu EP11_Alfred_Menu_12:
        "View 1":
            $ EP11_Alfred_menu_option_2 = 1
            scene EP11_Alfred_Anim_22 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_12
        "View 2":
            $ EP11_Alfred_menu_option_2 = 2
            scene EP11_Alfred_Anim_23 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_12
        "Faster":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_22_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_12
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_23_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_12
        "Slower":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_22 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_12
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_23 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_12
        "Continue":
            pass
    play audio female_moan_5
    a "AAHHHH..."
    h1 "Let me have a go at that pussy!"
    al1 "Fuuuck..."
    scene EP11_Alfred_Anim_24 with Fade(0.2, 0, 0.2)
    play audio femmoan_3
    $ EP11_Alfred_menu_option_2 = 1
    $ different_choice_menu = True
    play sound jerk loop
    menu EP11_Alfred_Menu_13:
        "View 1":
            play audio femgasp
            $ EP11_Alfred_menu_option_2 = 1
            scene EP11_Alfred_Anim_24 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_13
        "View 2":
            play audio femmoan_4
            $ EP11_Alfred_menu_option_2 = 2
            scene EP11_Alfred_Anim_25 with Fade(0.2, 0, 0.2)
            jump EP11_Alfred_Menu_13
        "Faster":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_24_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_13
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_25_Faster with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_13
        "Slower":
            if EP11_Alfred_menu_option_2 == 1:
                scene EP11_Alfred_Anim_24 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_13
            if EP11_Alfred_menu_option_2 == 2:
                scene EP11_Alfred_Anim_25 with Fade(0.2, 0, 0.2)
                jump EP11_Alfred_Menu_13
        "Cum!":
            play sound moaninglong_1
            pass
    h1 "Fuck... I'm close... Ah..."
    with flash
    h1 "Get on your knees!!"
    a "Fuuck!"
    h1 "I'm about to explode in your mouth!!!"
    scene 39-5 alfred 116 with Dissolve(1)
    pause
    play sound cum_sound
    scene 39-5 alfred 117 with flash_vpunch
    h1 "AAAHHH!!!"
    scene 39-5 alfred 118 with Dissolve(1)
    al1 "QUICK! MY DICK, TOO!!"
    a "SO MUCH CUUMMM!!!"
    play sound cum_sound
    scene 39-5 alfred 119 with flash_vpunch
    pause 2
    scene black with Dissolve(1)
    scene 39-5 alfred 120 with Dissolve(1)
    a "So much..."
    h1 "Fucking amazing!"
    al1 "I'm spent..."
    scene black with Dissolve(1)
    "Anna cleaned up..."
    play sound undress
    scene 39-5 alfred 121 with Dissolve(1)
    h1 "Well... I'd say this was a good investment."
    al1 "Have to absolutely agree."
    h1 "Let's have some fun together again sometime, eh Anna?"
    a "Perhaps... I have to run now."
    $ renpy.end_replay()
label EP11_Alfred_Fashion_Finished:
    play music SexyTimeSong6 fadein 3
    "Sometime later."
    scene 39-5 alfred 122 with Dissolve(1)
    "And the first place goes to..."
    "Alfred, Alf's Fashion!"
    a2 "YEAH!"
    scene 39-5 alfred 123 with Dissolve(1)
    a2 "Well, I just have one thing to say, honestly."
    a2 "It couldn't have been possible without my muse."
    scene 39-5 alfred 124 with Dissolve(1)
    a2 "Anna!"
    a2 "She's been truly inspirational!"
    a "Oh..."
    scene 39-5 alfred 125 with Dissolve(1)
    a2 "Thank you all for giving me this opportunity."
    a2 "This is a dream come true, to be honest!"
    scene 39-5 alfred 126 with Dissolve(1)
    "Alfred took a moment to savor this occasion."
    "Everyone applauded for the winner."
    h1 "Congratulations!"
    scene 39-5 alfred 128 with Dissolve(1)
    a2 "Thank you a lot, Anna."
    a2 "I couldn't have done this without you..."
    scene black with Dissolve(3)
    pause
    play ambience car_engine_ambience
    scene 39-5 alfred 129 with Dissolve(1)
    p2 "That was awesome."
    p2 "I still can't believe it."
    a "Yeah, tell me about it."
    scene 39-5 alfred 130 with Dissolve(1)
    a "So what's next after this?"
    p2 "Well, the proceeds will go towards expanding Alfred's clothing line."
    a "Can't wait to see it."
    p2 "You'll be the first to."
    scene black with Dissolve(1)
    play sound car_door
    scene 39-5 alfred 131 with Dissolve(1)
    p2 "Thank you for today."
    a2 "Yes, indeed."
    a "Thank you, guys, for this amazing opportunity."
    scene 39-5 alfred 132 with Dissolve(1)
    a2 "Well, I'm off to my shop."
    a2 "Still gotta do some stuff there."
    scene 39-5 alfred 133 with Dissolve(1)
    a "I think I will go to the beach."
    p2 "Oooh, sounds lovely."
    a "Bye, guys!"
    a2 "Come visit soon."
    a "Definitely."
    $ different_choice_menu = False
    scene black with Dissolve(1)
    $ EP11_var_8 = True
    stop ambience
    scene black with Dissolve(1)
    jump EP11_Beach

label EP11_Beach:
    play ambience beach_ambience
    play music chill_song_6 fadein 4
    scene 39-7 beach 1 with Dissolve(1)
    a "Ah..."
    a "This is so nice."
    a "After such a long day, I can finally relax a little bit."
    if EarlHelp == True:
        a "God knows what'll happen at the hotel later tonight."
    scene 39-7 beach 2 with Dissolve(1)
    bb1 "Welcome, Anna."
    bb1 "Long time, no see, eh?"
    a "Haha, yes, it's been a while."
    bb1 "So, what'll it be?"
    scene 39-7 beach 3 with Dissolve(1)
    a "Actually. I'll go for a beer this time."
    bb1 "A good choice, nothing refreshes better than a cold beer."
    a "Yeah, totally."
    a "So how's business?"
    scene 39-7 beach 4 with Dissolve(1)
    bb1 "Oh, the season's in full swing. Not a lot of people right now, but will show up later, probably."
    bb1 "Anyway, enjoy the beer."
    bb1 "I'll be here if you need me."
    a "Thanks!"
    play sound cloth_sound1
    scene 39-7 beach 5 with Dissolve(1)
    a "This is so nice."
    a "There really don't seem to be a lot of people, perhaps a nude tan would do just fine."
    play sound jacketcloth
    scene 39-7 beach 6 with Dissolve(1)
    pause 1
    scene 39-7 beach 7 with Dissolve(1)
    a "Yeah..."
    a "Let em swing, hehe."
    a "Gotta take my lotion."
    scene 39-7 beach 8 with Dissolve(1)
    "Anna massaged her entire body."
    "Her legs, her thighs..."
    "Her breasts..."
    scene EP11_Beach_Anim_1 with Dissolve(1)
    a "Ah... This is so relaxing."
    $ different_choice_menu = True
    menu EP11_Beach_Menu_1:
        "View 1":
            scene EP11_Beach_Anim_1 with Dissolve(1)
            jump EP11_Beach_Menu_1
        "View 2":
            scene EP11_Beach_Anim_2 with Dissolve(1)
            jump EP11_Beach_Menu_1
        "View 3":
            scene EP11_Beach_Anim_3 with Dissolve(1)
            jump EP11_Beach_Menu_1
        "Continue":
            pass
    $ different_choice_menu = False
    a "Mhmm..."
    a "This is turning me on a bit..."
    a "Alright... That should be enough, heh."
    scene 39-7 beach 9 with Dissolve(1)
    "Some young dudes had arrived for a beach day."
    du1 "Wassup Greg!"
    du1 "Working hard?"
    bb1 "Someone's gotta make money."
    du2 "Riiight."
    scene 39-7 beach 10 with Dissolve(1)
    du2 "Damn, I can't wait for the party on Saturday."
    du2 "Tell me again why we ain't partying already tomorrow?"
    du1 "Cuz the damn teachers put a test. ON A SATURDAY!"
    du3 "Yeah, no idea how that's legal."
    du2 "Maybe because school was on lockdown due to that stink bomb you left in the girl's bathrooms?"
    du3 "Haha. That was some stupid shit man."
    scene 39-7 beach 11 with Dissolve(1)
    du3 "I mean, we ain't kids anymore."
    du3 "This is College, bro."
    du1 "Whatever... Anyway."
    scene 39-7 beach 12 with Dissolve(1)
    du3 "Yo, check it out."
    du3 "Some chick, nude tanning."
    du2 "Dammmn... She is so fucking hot..."
    scene 39-7 beach 13 with Dissolve(1)
    du1 "Wtf. That's like the hottest girl I've seen."
    du1 "Wait, I know her."
    du3 "What?"
    du1 "Yeah, she's... I think she's my neighbor."
    du3 "No shit."
    scene 39-7 beach 14 with Dissolve(1)
    du2 "Bro. You gotta ask her if she wants to come to our party."
    du1 "No way. Bro look at her, she'll deny me harder than Jessica."
    du2 "It can't be any worse than Jessica, trust me."
    du2 "Yeah, You've got nothing to lose."
    du2 "Come on."
    du3 "Dude, ask her!"
    du1 "Fuck... Alright, shit. I will."
    scene 39-7 beach 15 with Dissolve(1)
    du2 "At least we'll get a good laugh, haha!"
    du3 "Damn, I hope she actually agrees."
    du2 "You can't be serious."
    du2 "Girls like that? They probably hang out with the rich dudes."
    du3 "Who cares."
    scene 39-7 beach 16 with Dissolve(1)
    pause 1
    scene 39-7 beach 17 with Dissolve(1)
    du1 "He... Hey..."
    a "Hello."
    du1 "Ummm... So how's the weather down there?"
    a "What?"
    scene 39-7 beach 18 with Dissolve(1)
    du1 "I mean, the weather is awesome, right?"
    a "Hehe..."
    a "It's alright."
    du1 "Umm... Don't you live on 150A Baker street?"
    a "How do you know?"
    du1 "I think we might be neighbors."
    scene 39-7 beach 19 with Dissolve(1)
    a "Is that so?"
    du1 "Ye... Yeah."
    a "So you just came to say hi?"
    scene 39-7 beach 21 with Dissolve(1)
    du1 "Well... Not exactly."
    du1 "We are having a little party on Saturday, at my place."
    du1 "I was just umm... Wondering if you'd like to join?"
    scene 39-7 beach 19 with Dissolve(1)
    a "Huh... Well..."
    du1 "What if you give me your number, and umm. And I'll type you up on Saturday?"
    menu:
        "Ok, I'll give you my number.":
            $ EP11_Party_var_1 = True
            a "It's +981 2020 4222."
            scene 39-7 beach 20 with Dissolve(1)
            du1 "Awesome."
            du1 "You are awesome."
            a "Hehe, thank you."
            du1 "Alright, I will type you up on Saturday."
            a "Ok, I will think about it."
            du1 "Great, Cool..."
            du1 "Have a nice tanning session."
            a "I will, thanks."
            scene 39-7 beach 22 with Dissolve(1)
            pause 1
            scene 39-7 beach 23 with Dissolve(1)
            du1 "Dudes. I've got that ultra rizz."
            du3 "Hold no. No Fucking way."
            du1 "I got her number."
            du2 "What? The fuck."
            du1 "Yeah, she might actually come to our party."
            du3 "THAT IS SO SIIIIICCCK!!!"
        "No thanks, I'm good.":
            du1 "Oh, Well, umm... Ok..."
            a "Good luck, though."
        "Nope, scram, loser!":
            du1 "Oh, Well, umm... Ok..."
    scene 39-7 beach 24 with Dissolve(1)
    "Anna continued to sunbathe for a good while..."
    scene black with Dissolve(1)
    scene 39-7 beach 24 with Dissolve(1)
    a "Alright... It's going to start getting dark soon."
    a "Time to pack up..."
    play sound undress
    scene 39-7 beach 25 with Dissolve(1)
    a "I think that's enough..."
    if EarlHelp == True:
        a "Gotta go to that hotel..."
    if EP11_Party_var_1 == True:
        scene 39-7 beach 26 with Dissolve(1)
        a "Cheers..."
        du1 "No waayyy..."
        "Anna winked at the dudes."
    $ EP11_var_9 = True
    scene black with Dissolve(1)
    stop ambience
    if EarlHelp == True:
        jump EP11_Earl_Hotel
    jump EP11_Episode_End
label EP11_Episode_End:
    stop sound
    stop audio
    scene black with Dissolve(1)
    jump EP12_Begin
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
