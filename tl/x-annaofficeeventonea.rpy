label AnnaContractEventOneOne:
    play music PPMCasualReception fadein 0.5
    play sound walk
    scene black with Dissolve(1)
    "She got to work."
    scene 33-1 contract 1 with Dissolve(1)
    "Anna sits down at her desk to finish up with the documentation of the contract."
    "She had almost finished it anyway."
    a "Right, what do we have here... Mostly, these terms are pretty unfavorable for the opposing party..."
    a "No one in their right mind would sign this... But maybe I could convince them..."
    scene 33-1 contract 2 with Dissolve(1)
    "As Anna was working, she noticed Emily storming right her way."
    "Even though she enjoys the company, she needed to finish this up..."
    play sound surprise
    e "Anna! Hey! How are you, my dear?"
    a "Hey, Emily. I'm ok... I've been busy... And Am busy, right now."
    e "Hey, I won't take much of your time. I just have this idea."
    if dianaGoodRelations == False:
        e "By the way, I heard that you had an argument with Diane?"
        e "Are you ok, sweety?"
        a "Yeah, I'm fine. It's... I don't know..."
        e "She's a hoe... Forget about her."
    scene 33-1 contract 3 with Dissolve(1)
    a "Ok, so. What do you have in mind?"
    e "Well, since I know that you are currently going through some stuff..."
    e "I thought, you definitely need the relaxation. So. We could have some sort of a day out during the weekend, huh?"
    a "Huh, I haven't thought about it. I've been so busy with work and life that I had forgotten about something like relaxation."
    e "Yeah, I can see it."
    scene 33-1 contract 4 with Dissolve(1)
    e "Soo... I thought that maybe we could go to the beach during the weekend, huh? And during the evening, we could go for drinks."
    a "The beach sounds nice... But I don't know about partying."
    e "Oh, come on. You know it will be fun. Why stop yourself?"
    a "I've been into some crazy things recently, I've done a lot of... Um... {i}Perverted{/i} things."
    a "And I kind of feel like I keep digging a hole for myself..."
    e "You are not! Trust me when I say that you are young and should have fun. When you're old, then you settle down."
    play sound surprise
    scene 33-1 contract 5 with Dissolve(1)
    a "What are you implying? Are you talking about Andrew?"
    e "Yes. I know he is in a tough place right now, but so are you. And you deserve a break."
    e "He isn't going anywhere, besides... I don't think he is the best you can get out of life..."
    a "Now you are starting to talk like Rebecca..."
    e "Oh, so she agrees? I mean, come on. There are way better options for you..."
    e "Anyway, I've been... Umm, enjoying my new toys, hehe..."
    a "Whatever do you mean? Oh... I get it..."
    scene 33-1 contract 6 with Dissolve(1)
    e "I even have one with me right now... hehe..."
    a "Oh, Emily... You are such a slutty girl, hehe..."
    e "You know I am. I've always been... I enjoy the pleasure of life. Like I should."
    a "Can't argue there, but still... Here? In the office?"
    e "I like to explore my sexuality, I feel excited..."
    scene 33-1 contract 7 with Dissolve(1)
    t "Excited about what?"
    e "About my new..."
    with vpunch
    a "About our weekend plans!"
    t "Oh... That's cool. I've been thinking of going out myself this weekend."
    e "Speak of the devil, hehe..."
    e "One option right there, such a lovely dude..."
    scene 33-1 contract 8 with Dissolve(1)
    t "I'm sorry? What did you mean?"
    e "Nothing... Hehe..."
    a "Emily told me that she wants to hang out this weekend and..."
    e "And we would like you to come with us."
    t "You mean... Like... With you guys?"
    if timothySexContent == True:
        t "I think we can arrange something."
        e "Splendid!"
    else:
        t "I... I don't think I have the time you know..."
        e "Oh, come on Timothy..."
    scene 33-1 contract 9 with Dissolve(1)
    if timothySexContent == True:
        a "I mean, I would definitely enjoy the company."
        e "Of course she would, Timothy. We like you..."
        t "I like you guys, too."
        e "Imagine yourself with two bombshells, just hanging out."
        e "Just all yours... wouldn't it be crazy?"
        t "{b}*Gulp{/b}... It would..."
    else:
        e "Don't be so shy. We are all friends here..."
        t "I... I know, but... I don't know about it..."
        e "What don't you know? When two girls are inviting you out?"
        e "Two attractive, sexy girls asking you out for a day of drinks?"
        t "I... I'm..."
        "Timothy was starting to sweat. Emily was playing with him, but she was serious about it, too."
    scene 33-1 contract 10 with Dissolve(1)
    "Emily leaned in and whispered..."
    if timothySexContent == True:
        e "Just, imagine..."
        a "Hey, what are you guys talking about!?"
        "They were talking, and Anna couldn't make out the conversation..."
        t "I'm... Pretty sure..."
        "Emily kept whispering something into Timothy's ear."
    else:
        e "Timothy..."
        a "Guys, What are you talking about there?!"
        "Anna Couldn't hear what they were talking about there..."
        t "I... I'm... Ah..."
        "Emily kept whispering something into Timothy's ear."
    e "Just imagine..."
    scene 33-1 contract 11 with Dissolve(1)
    "They both turned to Anna, who had no idea what they were talking about."
    e "She definitely wants to have fun..."
    e "Don't you?"
    if timothySexContent == True:
        t "I'm certain that I do."
        e "Then we have a deal. We are going out on Sunday."
        a "What? I mean... Ok..."
        e "You have no choice, Anna. This is going to be fun."
    else:
        t "I don't think I'm ready for this..."
        e "Oh, come on, Timothy..."
        a "Ready for what?"
        t "I... I'm sorry..."
    scene 33-1 contract 12-1 with Dissolve(1)
    e1 "Hello, guys. Sorry for interrupting, but Anna has the contract closing today."
    e "Oh. We are so sorry. Anna is so kind and didn't want me to interrupt my stupid talk. Haha..."
    e "I'm sorry, sweety..."
    a "It's ok, dear."
    scene 33-1 contract 13-1 with Dissolve(1)
    e1 "How are you feeling today, Anna?"
    e1 "Are you ready? Have you read through the contract properly?"
    a "I believe I have."
    e1 "High ups made some last moment amendments. I hope you had time to go over those?"
    a "Shit... I Didn't..."
    e1 "Ah... Well, it's alright. I thought it might happen. It's their fault. But I have an idea."
    scene 33-1 contract 14-1 with Dissolve(1)
    e "We are leaving, then. Take care and good luck, Anna!"
    a "Thanks!"
    e1 "You guys go take a break, ok?"
    e "We planned on it anyway."
    e1 "After Anna leaves, we will have a monthly meeting. I expect you all to have read and prepared your reports."
    e "Already done and ready."
    scene 33-1 contract 15-1 with Dissolve(1)
    e1 "Alright. So on to the business itself."
    e1 "I realized that it could be a bit hectic, and you might've missed the last amendments."
    e1 "Which, by the way, are completely moronic, if you ask me."
    e1 "So I've decided to give you some advantage."
    a "Oh?"
    scene 33-1 contract 17-1 with Dissolve(1)
    e1 "Well, I don't know what you expect, but I cannot deny that you have some very... Um..."
    e1 "Good assets, and in time such as these, we could really use them."
    a "Whatever do you mean by that..."
    e1 "The deal, as you know, originally isn't very good, but we are hopeful that you might persuade them to change their minds."
    scene 33-1 contract 19-1 with Dissolve(1)
    e1 "That's why I have this..."
    a "Is that an outfit?"
    e1 "Correct. I don't know if you are willing to wear it, but consider this."
    e1 "If we close this deal, it will be a very big step in your career already."
    e1 "Additionally, you will receive a very nice bonus and commission for this deal."
    a "I don't think I want to be used as a tool, like that."
    e1 "Believe me, we are all tools. We can play the game or not. That's up to us."
    play sound undress
    scene 33-1 contract 20-2 with Dissolve(1)
    "Anna realized that it could help her strengthen the partner position and also help with closing the deal."
    a "I hope you won't be peeking? I wish for some privacy."
    e1 "Oh, No worries. I shall turn around."
    "Ethan was salivating from the thought of seeing Anna naked."
    "However, he was never rude enough to attempt something like that."
    play sound undress
    scene 33-1 contract 21-2 with Dissolve(1)
    e1 "Don't worry, I'm not looking."
    a "I hope this outfit isn't too revealing or too sexy."
    e1 "Actually, I wouldn't know, I didn't pick it out..."
    a "Then who did?"
    e1 "Ah... Well, one of the board members. He's started to take interest in your work."
    e1 "Since you've become a partner."
    play sound undress
    scene 33-1 contract 24-1 with Dissolve(1)
    e1 "Splendid. It's... Well... Rather revealing actually."
    a "Yeah... I know... I can't wear this..."
    e1 "Umm... I believe it would be in everyone's best interest, including yours, to carry on with it."
    a "But, it's so... Revealing..."
    e1 "Remember that this might only increase your chances at closing the deal."
    a "Right..."
    scene 33-1 contract 25-1 with Dissolve(1)
    e1 "Anyway... I hope you've read through the documents and are ready to go through with this."
    e1 "No one will accompany you. It isn't the right procedure, but the board member insisted."
    e1 "There is a car waiting outside for you."
    e1 "Good luck to you."
    a "Thanks, I will need it."
    play sound door2
    $ renpy.sound.play("audio/sounds/city_traffic.mp3", fadein=1)
    play music tense2
    scene 33-1 contract 26-1 with Dissolve(2)
    "Anna exited the office building, and a limousine was waiting for her."
    a "{i}...Oh wow, I've never driven with my personal chauffeur. I hope he is nice..."
    a "{i}...I guess there is no turning back. Got to give it my best... But this outfit..."
    scene 33-1 contract 27-1 with Dissolve(1)
    di "Hello, ma'am. I hope you are having an amazing day."
    a "Oh. Hi, and you are?"
    di "Pardon my manners, I'm Alex, your chauffeur."
    a "Nice to meet you, Alex."
    scene 33-1 contract 28-1 with Dissolve(1)
    di "We will be heading out soon. Get comfortable."
    di "There are also some drinks at the front, if you wish to indulge."
    a "Thank you."
    a "{i}...Nice, my very own limo driver. That's a step up..."
    play sound carsound2
    scene 33-1 contract 29-1 with Dissolve(1)
    "For a moment, Anna forgot about the worries of the contract deal."
    "She just enjoyed the premium feeling she was getting."
    a "{i}...If I continue like this, maybe someday I can get my own jet and mansion... Oh..."
    a "{i}...That would be amazing..."
    scene 33-1 contract 33-1 with Dissolve(1)
    di "We are going to the Shengzhou Corp offices. It's not a long ride."
    a "I know, I know."
    di "How are you doing so far, ma'am?"
    a "I'm enjoying the premium service."
    di "All part of the partner benefits, ma'am."
    stop sound fadeout 1
    play sound carsound
    scene 33-1 contract 35-1 with Dissolve(1)
    "They had arrived at the office."
    a "Thank you, Alex."
    di "I will bet waiting for you here."
    a "Very nice. Catch you later."
    scene black with Dissolve(1)
    play audio door2
    play music PPMEtheralEternity
    scene 33-1 contract 40-1 with Dissolve(1)
    "Anna enters their office and is met by both representatives immediately."
    c2 "Greetings, my Mr. Chen."
    z1 "And I'm Mr. Zhao."
    a "Hello, I'm Anna. I'm one of the new partners."
    "They looked at Anna with lustful eyes. They were surprised someone like this could be a partner."
    "But that also made them hopeful about what might come next."
    scene 33-1 contract 41-1 with Dissolve(1)
    "They were eyeballing her, and an awkward silence followed."
    a "Umm... So. I've arrived here today to discuss the terms of the deal and perhaps even close it today."
    c2 "Indeed... Well... It might be harder than you'd expect."
    a "How so?"
    c2 "This deal has been very... unfavorable for us from the very beginning."
    a "I'm sure the terms are justified."
    scene 33-1 contract 42-1 with Dissolve(1)
    c2 "Well... I'm not sure, but they could be justified by some other means."
    a "I don't know what you are getting at, but perhaps we can discuss it first?"
    c2 "Yes... Discuss..."
    scene 33-1 contract 44-1 with Dissolve(1)
    a "Please, take a seat, gentlemen. I shall go over the terms at once."
    "Anna could feel that they were distracted by her outfit."
    "And she realized that she could use it to her advantage."
    a "{i}...Alright, Anna... Showtime..."
    play sound undress
    scene 33-1 contract 45 with Dissolve(1)
    a "As you know, the hostile takeover was declined very early in the contract talks."
    a "That was due to shareholders, in this case, the partners, being unwilling to sell out their shares."
    a "But an early compromise was made to change the terms to a mutual, joint effort."
    a "As stated in the contract, we would lend out offices and services from within our company to you."
    a "On the basis that we would get a 35%% cut from every deal closed by your company."
    scene 33-1 contract 46-1 with Dissolve(1)
    c2 "The changes were made that you would get 45%% cut from each deal."
    c2 "That is the first part that we are unwilling to accept."
    a "Oh, I see. Well, it can be argued that our services are of the highest quality and our track record speaks for itself."
    c2 "True, but the next amendment that I want to address is the services provided."
    c2 "Originally, it was stated that our deals would be supervised by your experts in full. Total contract follow-through."
    c2 "And now it is changed to partial supervision. That is unacceptable."
    a "Partial services rendered still means complete contract proofing, legal document preparation, etc."
    c2 "Let me see the changes."
    scene 33-1 contract 47 with Dissolve(1)
    c2 "Oh, but by the looks of it, you've gone even further! The deal is changed from an unlimited amount of contract supervision to 12 per year."
    c2 "We close at least 34 contracts per year! If you are the best, you drive a very hard bargain, and we might have to look elsewhere."
    a "{i}...How did I miss this..."
    a "Umm... I see... That amendment was made due to heavy load our company has, because of our quality services, we have many clients."
    a "And that amendment could be changed in the future if our cut is reasonable enough to hire more associates and employees."
    scene 33-1 contract 48 with Dissolve(1)
    c2 "Haha... I love this... I let you come here, hoping that you would have come to your senses..."
    c2 "But it seems that you've become even crazier... This is just outrageous!"
    c2 "We simply cannot sign such a devious contract. It pretty much tells us that you are robbing us!"
    a "That is not the intention here... We simply value our services very highly."
    c2 "Right, right. For what you are asking, we could hire two firms and still get better profits!"
    scene 33-1 contract 49-1 with Dissolve(1)
    c2 "And as to your entire... Charade with your skimpy outfit... Well..."
    c2 "This was lower than low... Do you even respect yourself?"
    a "I... I..."
    c2 "All has been said. I'm not willing to discuss these terms any further."
    scene 33-1 contract 51-1 with Dissolve(1)
    a "I think we will have to take a recess."
    c2 "I doubt there is anything you could do to change my mind..."
    a "I have something in mind..."
    c2 "You've come in our office and have tried to make fun of us with these outlandish terms."
    c2 "What kind of a different reaction did you expect? That we would simply bow down?"
    a "Not at all..."
    scene 33-1 contract 54-1 with Dissolve(1)
    a "Perhaps we could come to a different kind of arrangement?"
    c2 "And what would that be?"
    a "I believe there is one thing that you want, and I know what it is..."
    c2 "Oh, do you know? Well, what is it?"
    scene 33-1 contract 54-2 with Dissolve(1)
    "Anna hesitated for a moment and thought to herself if this is really worth it..."
    a "{i}...Should I just go through with my idea..."
    menu:
        "Anna decides 'persuade' them":
            pass
        "Anna decides to stop it right there and cancel the deal.":
            a "I'm sorry, I shouldn't have said anything."
            a "I will be on my way. You can contact my superiors for further course of action."
            c2 "What?"
            scene 33-1 contract 27-1 with Dissolve(1)
            "Anna exited the building and went straight to the limo."
            $ office_var_one = True
            $ office_var_two = True
            jump AnnaContractEventOneOneEnding
    scene 33-1 contract 54 with Dissolve(1)
    a "It's me."
    c2 "What?"
    a "Plus the previous terms, before the outrageous amendments."
    c2 "Those are still not beneficial to us."
    a "What if we added an unwritten secret term that stated that you get something special?"
    scene 33-1 contract 55 with Dissolve(1)
    a "To be frank, the deal is reasonable. If we consider how good our services are. You cannot deny that."
    c2 "True. That's the main reason we turned to you."
    a "Right. But there are other things that we or specifically I can do good."
    c2 "Which are?"
    scene 33-1 contract 56 with Dissolve(1)
    a "Whatever you wish..."
    c2 "Huh..."
    z1 "Well... I think if you could 'convince' us better... We would consider."
    a "How would I convince you?"
    scene 33-1 contract 57 with Dissolve(1)
    z1 "Well... You could attend to some of our, more, immediate needs."
    z1 "The physical ones..."
    a "Perhaps you'd like to see something interesting?"
    z1 "I'm interested."
    scene 33-1 contract 58 with Dissolve(1)
    a "Like... Like that?"
    z1 "I do love a good pair of beautiful melons, but these are just next level..."
    "Mr. Zhao lustfully stared at Anna's breasts."
    z1 "Amazing, absolutely amazing."
    a "Do you like them?"
    z1 "Do I? The only thing I can think about right now."
    play sound surprise
    scene 33-1 contract 59 with Dissolve(1)
    c2 "You know that Mr. Zhao is not the one closing the deal? I am."
    c2 "So you better have solid arguments to convince me."
    c2 "Or rather, good skills to change my mind... Hehe..."
    a "I think we can arrange something..."
    play sound undress
    scene 33-1 contract 60 with Dissolve(1)
    "Anna moved to Mr. Chen with her titties peeking out."
    a "What do you wish to experience?"
    c2 "I want the entire package. And then I will consider signing."
    c2 "If you satisfy the requirements, we will be more lenient."
    a "Ah... I see..."
    scene 33-1 contract 61 with Dissolve(1)
    a "Perhaps a little bit of incentive at first."
    "Anna put her hand to Mr. Chen's crotch, and he immediately felt excited."
    c2 "Ah... Very nice..."
    a "I can do plenty of things..."
    c2 "I'm counting on it."
    scene 33-1 contract 62-1 with Dissolve(1)
    "Mr. Chen started touching her breasts with slow, sensual movements."
    c2 "You know, I've been in this business for over 35 years. And never have I met an individual such as yourself."
    a "I'm special."
    c2 "Indeed... Ah..."
    "Anna's hands were doing a very good job on Mr. Chen's concealed cock."
    scene 33-1 contract 62 with Dissolve(1)
    c2 "All of your 'assets' are just so perfect... I can't believe your superiors were withholding such a great tool..."
    a "Well, leave the best for last, eh?"
    c2 "Well said... Hmf..."
    c2 "Perhaps... We should arrange a meeting later on so we can 'discuss' the contract in {b}Deep{/b} detail."
    scene 33-1 contract 63 with Dissolve(1)
    c2 "And you would show us every nook and cranny of the agreement, and we shall enjoy it."
    a "Y... Yes..."
    "Mr. Chen was enjoying Anna's presence to the maximum. He was so excited about her that he forgot about the contract."
    "Perhaps Anna could pull this off after all."
    scene 33-1 contract 64 with Dissolve(1)
    c2 "Ok. We will give you another chance, but..."
    c2 "You have to change back the details, and then we will go up to our resort and have a long, long discussion about this."
    c2 "Do you understand?"
    a "I do."
    c2 "Great. I will see you then."
    c2 "This might turn out to be one of the best contract closings so far."
    scene 33-1 contract 65 with Dissolve(1)
    c2 "See you then."
    c2 "And thank your superiors for such an amazing employee on our behalf. You are truly gifted."
    a "{i}...That was easy... But it's just the beginning, who knows what they have in mind..."
    a "Will do. Thank you for reconsidering this deal."
    scene black with Dissolve(1)
    play sound carsound2
label AnnaContractEventOneOneEnding:
    play sound carsound2
    scene 33-1 contract 66-1 with Dissolve(1)
    "Anna got in the car, and they drove away immediately."
    di "So. How was your contract closing?"
    if office_var_two == True:
        a "I botched it... I don't know what I will do now."
        di "I'm sure you will come up with something."
    else:
        a "It went smoother than I expected."
        a "But that's only the beginning."
        a "I will have plenty of more work to do before it's closed."
    play sound carsound
    scene 33-1 contract 69-1 with Dissolve(1)
    di "We are here."
    a "Thank you again, Alex."
    di "Just doing my job, ma'am."
    a "Well, do you often get ladies such as myself in your limo?"
    di "Unfortunately, no, it's mostly old farts... Sorry for the language."
    a "Haha... I know what you mean."
    scene 33-1 contract 70 with Dissolve(1)
    a "Well, I will be seeing you around then."
    di "You can count on it, ma'am."
    scene black with Dissolve(1)
    "Anna got changed."
    "As Anna walking, she got a call from Alfred."
    a2 "Hello, Anna. How is my favourite neighbour doing?"
    a "Hey, Alfred! I'm good, good. Had a big day at the office."
    a2 "That's great. I was calling because I needed your help with something."
    a2 "Would you mind come over to my place?"
    a "Sure, I have nothing to do right now."
    a2 "Splendid."
    jump AlfredEventTwo
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
