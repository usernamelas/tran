label EthanEventTwo:
    play sound carsound
    scene black with Dissolve(2)
    "Anna came in to work, changed clothes and got to business."
    scene 30-6 ethan 8 with Dissolve(1)
    "Anna sat down at her desk and started to sift through the all of her tasks."
    "She cleaned up the mailbox."
    "And calculated some spreadsheets."
    a "{i}...If I take this cell and use the pie chart, I will be able to show a much better visible representation of the data."
    "She also started going through the contracts she had been assigned."
    scene 30-6 ethan 9 with Dissolve(1)
    "Anna did some of the tasks and took a quick breather."
    "Then suddenly..."
    play sound door2
    scene 31-4 office 4 with Dissolve(1)
    "Ethan entered Anna's office with another female."
    e1 "Hello, Anna. Hope you are adjusting to your new work place well?"
    e1 "You will be taking lead on a lot of the new contracts we have."
    e1 "So try to be thorough. Of course, if you need any help or advice, you can contact me."
    a "Sure, will do."
    e1 "Anyway, I've hired a new assistant for both of us."
    e1 "This is Madison."
    scene 31-4 office 5 with Dissolve(1)
    "The both had a formal kiss."
    "Anna was a bit surprised as to Madison's approach."
    "She didn't, however, dislike it. Perhaps Madison was a headstrong newcomer."
    m1 "Nice to meet you, Anna."
    m1 "I'm Madison Carter."
    a "Nice to meet you too, Madison."
    scene 31-4 office 6 with Dissolve(1)
    e1 "Anyway, since the pleasantries are over, I will just quickly explain how this will go."
    e1 "Since you, Anna, are rather busy with getting used to things with your new role. I will take lead on teaching Madison everything."
    e1 "Luckily, it shouldn't be too hard based on her previous work experience."
    e1 "Like I said earlier, she will be our assistant. She will help us go through the contracts like you did before Jeremy's premature death."
    a "Yeah... Thank you, Madison for joining us."
    e1 "She will sit downstairs where you used to sit, I'm also thinking of moving into Jeremy's old office, but we will see about that."
    e1 "Anyway, If that will be all, we shall begin the training. Take care, Anna. And good luck with the contracts. You can send them to Madison to proofread afterward."
    a "Okay, Ethan. Thanks."
    play sound door2
    scene 31-3 jeremy 20 with Dissolve(1)
    "Both Madison and Ethan exited the office, and Anna got back to her duties."
    "She thought about the new assistant, Madison, for a while."
    a "{i}...She is gorgeous. I'm sure she will be a good addition to our team..."
    "She continued working on the contracts and proofreading them for any legal issues."
    "She went at it for an hour more and had finally gone through the basics."
    "Anna knew that there was more work to do, but she had made good progress."
    $ ContractProgress = 20
    "Contract Analysis progress: [ContractProgress]%%"
    "Anna decided to take a break and go talk to Madison."
    $ MadisonIsAtWork = True
    $ EthanEventTwoQuest = 1
    jump madisonEthanOne
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
