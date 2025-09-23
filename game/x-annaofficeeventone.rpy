label AnnaContractEventOne:
    play music PPMCasualReception fadein 0.5
    play sound walk
    scene black with Dissolve(1)
    "She got to work."
    scene 33-1 contract 1 with Dissolve(1)
    "Anna sits down at her desk to finish up with the documentation of the contract."
    "She had almost finished it anyway."
    a "Right, what do we have here... Mostly, these terms are pretty unfavorable for the opposing party..."
    a "No one in their right mind would sign this... But maybe I could convince them..."
    play sound notification
    a "{i}...Oh, Jeremy just sent me an email..."
    scene 33-1 contract 2 with Dissolve(1)
    "As Anna was working, she noticed Emily storming right her way."
    "Even though she enjoys the company, she needed to finish this up..."
    play sound surprise
    e "Anna! Hey! How are you, my dear?"
    a "Hey, Emily. I'm ok... I've been busy... And Am busy, right now."
    e "Hey, I won't take much of your time. I just have this idea."
    scene 33-1 contract 3 with Dissolve(1)
    if dianaGoodRelations == False:
        e "By the way, I heard that you had an argument with Diane?"
        e "Are you, ok sweety?"
        a "Yeah, I'm fine. It's... I don't know..."
        e "She's a hoe... Forget about her."
    a "Ok, so. What do you have in mind?"
    e "Well, since I know that you are currently going through some stuff..."
    e "I thought, you definitely need the relaxation. So. We could have some sort of a day out during the weekend, huh?"
    a "I haven't thought about it. I've been so busy with work and life that I had forgotten about something like relaxation."
    e "Yeah, I can see it."
    scene 33-1 contract 4 with Dissolve(1)
    e "Soo... I thought that maybe we could go to the beach during the weekend? And during the evening, we could go for drinks."
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
    a "Now you are starting to sound like Rebecca..."
    e "Oh, so she agrees? I mean, come on. There are way better options for you..."
    e "Anyway, I've been... Umm, enjoying my new toys, hehe..."
    a "Whatever do you mean? Oh... I get it..."
    scene 33-1 contract 6 with Dissolve(1)
    e "I even have one with me right now... hehe..."
    a "Oh, Emily... You are such a slutty girl, hehe..."
    e "You know I am. I've always been... I enjoy the pleasure of life. Like I should."
    a "Can't argue there, but still... Here? In the office?"
    e "I like to explore my sexuality, I feel excited..."
    play sound surprise2
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
        t "{b}*Gulp*{/b}... It would..."
    else:
        e "Don't be so shy. We are all friends here..."
        t "I... I know, but... I don't know about it..."
        e "What don't you know? When two girls are inviting you out?"
        e "Two attractive, sexy girls asking you out for a day of drinks?"
        t "I... I'm..."
        "Timothy was starting to sweat. Emily was playing with him, but she was serious about it, too."
    scene 33-1 contract 10 with Dissolve(1)
    "Emily leaned in and whispered to Timothy..."
    if timothySexContent == True:
        e "Just, imagine..."
        a "Hey, what are you guys talking about!?"
        "They were talking and Anna couldn't make out the conversation..."
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
    play sound surprise2
    scene 33-1 contract 12 with Dissolve(1)
    j1 "What is all this racket?"
    j1 "Why aren't you all working? We gotta make them KPIs work!"
    e "Here comes the party pooper..."
    scene 33-1 contract 13 with Dissolve(1)
    "The atmosphere shifted quickly. The fun had faded, but the plan for the weekend was already made."
    j1 "I will act as if I didn't hear that, Emily."
    e "I don't care either way."
    j1 "Anna, just the person I'm looking for, are you busily working through the contract?"
    a "Yeah. I am."
    j1 "Ok. As I would expect."
    j1 "I have business to talk with Anna about. You can leave."
    scene 33-1 contract 14 with Dissolve(1)
    e "You don't have to tell me twice to leave your presence."
    j1 "As charming as ever... We will have a little talk about insubordination at the workplace a bit later."
    e "You would like to try..."
    j1 "Hehe... I like the way you fight back... It makes it that much more satisfying."
    "Both Emily and Timothy went for a lunch break."
    scene 33-1 contract 15 with Dissolve(1)
    j1 "Now onto serious business. I believe that you've gone through the papers?"
    a "As much as I can, yes..."
    j1 "That will have to do... Now... I've made changes to the documents..."
    a "What? I wasn't aware of this..."
    j1 "You would have been if you hadn't been chatting with your friends."
    a "I can explain..."
    j1 "No need. We will do fine. I trust in your..."
    scene 33-1 contract 16 with Dissolve(1)
    j1 "Skills..."
    j1 "Are you ready to put them to the test? I've all wrapped up with my business."
    j1 "Our meeting is within the hour..."
    a "I... Why wasn't I aware of the time?"
    j1 "I believe that the email I sent you with the attached amendments also mentioned the time of our departure..."
    scene 33-1 contract 17 with Dissolve(1)
    a "Oh... I'm so sorry..."
    j1 "Regardless of what you've done here... We have to get ready."
    j1 "I brought the outfit from yesterday..."
    a "Is it absolutely necessary?"
    j1 "Now more than ever, since you are not up to speed with the new changes."
    if jeremySexContent == True:
        a "{i}...This bastard... He did this on purpouse..."
    else:
        "a{i}... I suppose he's right..."
    scene 33-1 contract 19 with Dissolve(1)
    a "Do I have to change here?"
    j1 "Yes."
    a "But what about our colleagues. They will notice."
    j1 "Come on. All of them are on a lunch break."
    a "I hope this will be worth it."
    j1 "Well, you better do. Otherwise, they will decline our offer."
    a "Then maybe we should've given them better contract terms?"
    j1 "Nonsense, I am positive that your capabilities will be enough."
    j1 "Now get changed..."
    play sound undress
    if jeremySexContent == True:
        scene 33-1 contract 20 with Dissolve(1)
        "Anna turned around and felt uncomfortable yet again. But there wasn't much she could do..."
        "It was that or declined contract... And that was still up for debate."
        a "Can you at least turn around while I change?"
        j1 "I cannot. I have to examine how you look in this light."
        a "Ugh..."
        j1 "Just change already."
    else:
        scene 33-1 contract 20-1 with Dissolve(1)
        "Anna turned around and was at ease since Jeremy was respecting boundaries."
        "But the outfit was still on. She had to choose between that or declined contract."
        "And even that was still unclear."
        a "Please don't peek."
        j1 "Of course..."
    play sound undress
    if jeremySexContent == True:
        scene 33-1 contract 21 with Dissolve(1)
        j1 "Yes... You are an absolute snack, as always."
        a "You know, it makes me uncomfortable..."
        j1 "I'm sure it does. But that doesn't matter, honestly."
        a "Why are you like this? Huh?"
        j1 "Don't ask me senseless questions and keep changing!"
    else:
        scene 33-1 contract 21-1 with Dissolve(1)
        j1 "How is it going there?"
        a "I'm getting ready, hold on."
        j1 "Sorry for being a bit pushy, but we are on the clock."
        a "It's... Alright..."
        "Jeremy was rather nice this time around, still kind of an ass but not a terrible person."
    play sound surprise2
    scene 33-1 contract 22 with Dissolve(1)
    l1 "Jeremy, Hey. I was looking for you. Oh, I see you are busy with something."
    a "{i}...Oh no... This is embarrassing... And Diane is here, too... She will definitely harass me for this..."
    j1 "Yeah, we are preparing for the contract closing. Going soon."
    l1 "Ah... Right, the one with Shengzhou Corp?"
    j1 "Correct, What was it that you wanted?"
    scene 33-1 contract 23 with Dissolve(1)
    l1 "Oh nothing, that can wait. Looks like you are having some fun, eh?"
    if jeremySexContent == True:
        j1 "You bet, hehe..."
        j1 "I think with the new outfit, I've really outdone myself."
        l1 "Well, I will believe it when I see it."
        d "That bitch... Nice."
    else:
        j1 "No, we are just in a bit of a hurry, so Anna's changing here."
        j1 "We are going to move out soon, got to morally prep ourselves for the contract."
        l1 "Yeah. Anna definitely needs moral preparations for what's coming up... hehe..."
        j1 "Stop being an ass, ok?"
        l1 "Whow... Ok... Sheesh..."
        j1 "Now go. We don't have time for this."
    play sound undress
    if jeremySexContent == True:
        scene 33-1 contract 24 with Dissolve(1)
        "She had finally changed and looked at them with embarrassment."
        "They all gloated and stared, even Diane."
        "She couldn't deny, even after their fights, that she wanted to take advantage of Anna."
        "Make her submit to Diane."
        l1 "Well, well... I'm impressed."
        j1 "Right? I also decided to add stockings. Those will definitely help."
    else:
        scene 33-1 contract 24-2 with Dissolve(1)
        j1 "Well, well... I'm impressed. Sorry if I'm starring a bit."
        a "It's... Ok..."
        j1 "It looks just as I imagined, I'm sorry it came down to this, but we need every advantage we can get."
        d "Those tits, almost naked... I like... hehe..."
        a "I... I have to agree, you are right. If that means more profits for us, then I'm in."
        j1 "Great."
    if jeremySexContent == True:
        scene 33-1 contract 25 with Dissolve(1)
        l1 "Can't agree more. I'm liking the look."
        l1 "She should come to work every day like this."
        j1 "I will think about it..."
        a "No... Absolutely not."
        j1 "You won't have much say in it."
        j1 "Anyway, shall we?"
        l1 "Good luck."
    else:
        scene 33-1 contract 25-2 with Dissolve(1)
        j1 "Now, are you ready?"
        a "As ready as I will ever be."
        j1 "Ok, let's hope that you've memorized the contract to the best of your knowledge."
        a "I will try to do my best, sir."
        j1 "With a bit of luck, we might even pull this off."
    play audio door2
    $ renpy.sound.play("audio/sounds/city_traffic.mp3", fadein=1)
    play music tense2

    scene 33-1 contract 26 with Dissolve(1)
    "They walked down to the car, and it was a long limousine."
    "With a decent-looking driver."
    di "Hello, sir. I believe everything is in order."
    a "I didn't even know we had a limousine."
    j1 "We have a lot of things. In time, you will see."
    scene 33-1 contract 27 with Dissolve(1)
    di "Are we ready to depart?"
    j1 "Yes we are, Alex."
    di "Are we headed to the usual place, sir?"
    play audio surprise
    scene 33-1 contract 28 with Dissolve(1)
    if jeremySexContent == True:
        j1 "Jeez, you perv! Not yet, hehe..."
    else:
        j1 "You are out of line!"
    j1 "She is our new partner."
    j1 "We are headed to the Shengzhou offices."
    j1 "We have a contract to sign today."
    di "Right away, sir."
    stop sound fadeout 1
    play audio carsound2
    scene 33-1 contract 29 with Dissolve(1)
    j1 "Alright, I think you already know everything that you need to know."
    a "Well, besides the important amendments you did to the contract!"
    j1 "Hey... You deal with the situation you have, not the one you wish you had."
    a "Huh..."
    if jeremySexContent == True:
        j1 "We will arrive there soon, so prepare, get your slut game on."
    else:
        j1 "We will arrive there soon, so prepare, get a little bit more... Um... Seductive."
    play audio surprise
    play audio carsound3
    scene 33-1 contract 30 with Dissolve(1)
    a "I'm sorry?"
    j1 "Just try to be slutty, and convince them with your looks."
    j1 "And try to take away their attention from the less appealing terms."
    if jeremySexContent == True:
        a "Is that all I am to you in this situation? Just an object? A tool to use?"
        j1 "Exactly! You are catching up now. Hehe..."
    else:
        a "I don't like the sound of that, but I will comply."
        j1 "Thank you, we will get something out of this."
    if jeremySexContent == True:
        scene 33-1 contract 31 with Dissolve(1)
        "Jeremy grabs Anna by her hand."
        j1 "And if all goes well, you will earn a nice bonus..."
        a "What are you doing?"
        j1 "Just examining your readiness a bit."
        play audio surprise2
        play audio undress
        with vpunch
        scene 33-1 contract 32 with Dissolve(1)
        a "What... Hey!"
        j1 "Yes... Yes... This is so nice... I like it."
        menu:
            "(SUB)Anna decides to Submit to Jeremy's will.":
                $ sub_var +=1
                a "Ah... Fine... As you wish..."
                j1 "That's right. Submit to me."
            "(DOM) Anna realizes that she could use this to her advantage.":
                $ dom_var +=1
                a "Yeah... Touch them... If you are a good boy, I might give you more."
                j1 "Oh, feisty. If you keep this up. I might even give you a raise."
        play sound carsound3
        scene 33-1 contract 33 with Dissolve(1)
        "The chauffeur was looking back and enjoying the view."
        "He hadn't seen Anna before."
        di "{i}...Ah... She is so hot... I hope Jeremy lets me take her for a ride some time..."
        di "{i}...She is probably very good in the sack..."
        scene 33-1 contract 34 with Dissolve(1)
        j1 "Yess... They are getting a bit hard right now..."
        j1 "That's exactly what we need. Those nipples harder, so they stick out more during the meeting."
        a "Is that appropriate? It's... A bit perverted."
        j1 "Hah... None of this is appropriate. Just sit back and let me get them hard."
        a "Jeremy, it hurts a bit. You are squeezing them too hard."
        j1 "It's amazing how I can get them hard like this. Are you enjoying it?"
        a "N... No..."
        j1 "I think you are... You dirty girl."
        scene 33-1 contract 35 with Dissolve(1)
        "Anna was twitching from the sensation a bit."
        "She couldn't control how the physical stimulation was controlling her."
        a "Ah..."
        j1 "Oh... Some moans even? I like that even more... You and I are going to have fun."
        j1 "And, of course, Shengzhou will, too."
        scene 33-1 contract 36 with Dissolve(1)
        a "That's enough..."
        j1 "I believe it is... Put those puppies away."
        j1 "We are going to be there soon so prepare your best arguments and try to look seductive."
        a "Ok..."
    scene 33-1 contract 37 with Dissolve(1)
    j1 "I hope you understand the importance of this. You are our ace, so to speak."
    j1 "If we close it properly, our firm will be able to expand much faster."
    j1 "That means more profits for everyone, including you."
    a "I could see that as a good upside, but it all depends on my performance."
    j1 "Yes, it always does. You are kind of taking a lead on this. We all do, as partners."
    j1 "You are not one yet, but if you perform well and bring in good deals, I might consider making you one later on."
    if jeremySexContent == True:
        j1 "{i}...Hehe... That will keep her hopeful..."
    scene 33-1 contract 38 with Dissolve(1)
    di "Ok, sir. We are at the Shengzhou offices."
    j1 "Thank you, Alex. We shall be heading in."
    j1 "Remember everything I've told you, and you will get out of this unscathed."
    j1 "If we fail, you will, of course, receive punishment..."
    j1 "So at the end of the day, I kind of win in every scenario."
    play audio carsound
    scene black with Dissolve(1)
    play audio door2
    play music PPMEtheralEternity
    scene 33-1 contract 40 with Dissolve(1)
    "The moment they stepped in the office building, the men very eyeballing Anna."
    j1 "Greetings, Mr. Chen, Mr. Zhao."
    j1 "I hope you properly read through the contract and are ready to go forward with our deal?"
    j1 "As a great man once said: Every contract you don't close is like a missed shot."
    c2 "I've never heard of such a saying."
    j1 "I came up with it hehe..."
    z1 "Yeah, Right... Jeremy... Stop pretending."
    scene 33-1 contract 41 with Dissolve(1)
    j1 "So, are we ready to sit down and discuss the details?"
    z1 "Well, I will start by saying that the deal is very... one-sided."
    c2 "We are willing to discuss the details, of course, but you have to give a very good reason for such terms."
    j1 "No problem at all, gentlemen. I've brought my foremost expert on this matter. She knows the contract in and out."
    play sound surprise
    scene 33-1 contract 42 with Dissolve(1)
    j1 "let me introduce Anna, my head of department."
    z1 "A pleasure to meet such an... Expressive female employee."
    c2 "You are indeed very... memorable."
    a "Hello and thank you."
    "Anna was a bit confused. She was hoping that Jeremy will just use her as eye candy."
    "She felt that she wasn't equipped to discuss the contract in detail since the amendments."
    scene 33-1 contract 43 with Dissolve(1)
    "She whispered to Jeremy..."
    a "I thought that I will just help you out. I'm not prepared for this."
    j1 "You will have to do. I told you your importance in this."
    j1 "Improvise if you have to..."
    a "Fine..."
    scene 33-1 contract 44 with Dissolve(1)
    a "Alright... Gentlemen, please take a seat. I shall go over the basic details."
    c2 "We already know the basics. But please, take your time. We enjoy your company here."
    z1 "Indeed we do."
    play sound undress
    scene 33-1 contract 45 with Dissolve(1)
    a "As you know, the hostile takeover was declined very early in the contract talks."
    a "That was due to shareholders, in this case, the partners, being unwilling to sell out their shares."
    a "But an early compromise was made to change the terms to a mutual, joint effort."
    a "As stated in the contract, we would lend out offices and services from within our company to you."
    a "On the basis that we would get a 35%% cut from every deal closed by your company."
    play sound surprise
    scene 33-1 contract 46 with Dissolve(1)
    c2 "The changes were made that you would get 45%% cut from each deal."
    c2 "That is the first part that we are unwilling to accept."
    a "Oh, I see. Well, it can be argued that our services are of the highest quality and our track record speaks for itself."
    c2 "True, but the next amendment that I want to address is the services provided."
    c2 "Originally, it was stated that our deals would be supervised by your experts in full. Total contract follow-through."
    c2 "And now it is changed to partial supervision. That is unacceptable."
    a "Partial services rendered still means complete contract proofing, legal document preparation, etc."
    c2 "Let me see the changes."
    play music tense2
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
    scene 33-1 contract 49 with Dissolve(1)
    c2 "I asked you to change those points back, but you've left them unchanged! And added more ridiculous terms!"
    a "I... I..."
    c2 "All has been said. I'm not willing to discuss these terms any further."
    c2 "Jeremy, you've lost your mind."
    play sound surprise
    scene 33-1 contract 50 with Dissolve(1)
    j1 "Oh... My apologies, I thought that Anna made the necessary changes."
    a "What?"
    c2 "I knew that you were an asshole, but I didn't realize you were this bad!"
    c2 "I doubt there is anything you could do to change my mind..."
    j1 "Perhaps, perhaps not..."
    j1 "Let's take five, shall we?"
    scene 33-1 contract 51 with Dissolve(1)
    c2 "No, I don't think so. It's time for you both to leave."
    j1 "Oh, so you say. Well..."
    c2 "You've come in our office and have tried to make fun of us with these outlandish terms."
    c2 "What kind of a different reaction did you expect? That we would simply bow down?"
    scene 33-1 contract 52 with Dissolve(1)
    a "Why did you make those amendments last minute?"
    j1 "Because they are assholes. First, they tried to buy us out. Now I want my revenge."
    j1 "I wanted to see how far we could push them."
    a "The deal was decent at the beginning. We could've convinced them then."
    j1 "Either way, if you can change their minds even with the previous terms, we will still win big time."
    j1 "And your cut depends on it after all. So go and change their minds..."
    scene 33-1 contract 53 with Dissolve(1)
    "Anna was left to fend all for herself..."
    a "{i}...Shit... Alright. I can do this..."
    a "{i}...I can easily convince them. I just have to use some of my charms..."
    c2 "Excuse me, did you forget something here?"
    play sound door2
    scene 33-1 contract 54 with Dissolve(1)
    a "Well... Maybe... What if we could agree upon the previous terms?"
    c2 "Those are still not beneficial to us."
    a "What if we added an unwritten secret term that stated that you get something special?"
    c2 "Whatever do you mean by that?"
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
    play sound undress
    scene 33-1 contract 58 with Dissolve(1)
    a "What about these?"
    z1 "Exactly. I do love a good pair of beautiful melons, but these are just next level..."
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
    scene 33-1 contract 60 with Dissolve(1)
    "Anna moved to Mr. Chen with her titties peeking out."
    a "What do you wish to experience?"
    c2 "I want the entire package. And then I will consider signing."
    c2 "If you accommodate the requirements, we will be more lenient."
    a "I see... I believe that there are plenty of things you'd wish to enjoy..."
    play sound undress
    scene 33-1 contract 61 with Dissolve(1)
    a "Perhaps a little bit of incentive at first."
    "Anna put her hand to Mr. Chen's crotch, and he immediately felt excited."
    c2 "Very nice..."
    a "I can do plenty of things..."
    c2 "I'm counting on it."
    scene 33-1 contract 62-1 with Dissolve(1)
    "Mr. Chen started touching her breasts with slow, sensual movements."
    c2 "You know, I've been in this business for over 35 years. And never have I met an individual such as yourself."
    a "I'm special."
    c2 "Indeed... Ah..."
    "Anna's hands were doing a very good job on Mr. Chen's concealed cock."
    scene 33-1 contract 62 with Dissolve(1)
    c2 "All of your 'assets' are just so perfect... I can't believe Jeremy was withholding such a great tool..."
    a "Well, leave the best for last, right?"
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
    scene 33-1 contract 65 with Dissolve(1)
    c2 "Be on your way and tell Jeremy that we are willing to negotiate."
    c2 "And thank him for being such an amazing employee. You are truly gifted."
    a "{i}...That was easy... But it's just the beginning. Who knows what they have in mind."
    a "Will do. Thank you for reconsidering this deal."
    scene black with Dissolve(1)
    play music tranquility
    play sound carsound2
    scene 33-1 contract 67 with Dissolve(1)
    j1 "So. I believe you've reinitiated the talks?"
    a "It was... a bit difficult, but yeah. They've invited me to their resort."
    j1 "Ah... Very well done."
    j1 "I will arrange transport and get in contact with them."
    scene 33-1 contract 68 with Dissolve(1)
    a "What happens now?"
    j1 "Well, if it was difficult before, it will probably be even more difficult further on."
    if jeremySexContent == True:
        j1 "And far more enjoyable for me and those guys."
        j1 "So prepare yourself for some good times... hehe..."
        a "I don't like the sound of that."
        j1 "You don't have to."
    else:
        j1 "But I have faith that you will pull through."
        j1 "That will land you a good, big bonus."
        a "Ah... I hope so."
    play sound carsound
    scene 33-1 contract 69 with Dissolve(1)
    "They arrived back at the main building."
    j1 "Consider all the things you've learned today. About how the corporate world works."
    j1 "And prepare yourself for the second meeting."
    a "Ok..."
    di "A pleasure, ma'am."
    scene black with Dissolve(1)
    "Anna went and changed. She was finished with the workday."
    "It was a relief, but nothing was over just yet."
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
